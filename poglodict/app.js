const $ = id => document.getElementById(id);
const icon = id => '<svg aria-hidden="true"><use href="#'+id+'"/></svg>';
const languages = {
  eng:['EN','Inglês','en-US','English'], spa:['ES','Espanhol','es-ES','Spanish'],
  ita:['IT','Italiano','it-IT','Italian'], deu:['DE','Alemão','de-DE','German'],
  ara:['AR','Árabe','ar','Arabic'], jpn:['JA','Japonês','ja-JP','Japanese'], por:['PT','Português brasileiro','pt-BR','Portuguese'], cmn:['ZH','Mandarim','zh-CN','Chinese']
};
const levels = ['A1','A2','B1','B2','C1','C2'];
const classes = {name:'Nome próprio',contraction:'Contração',noun:'Substantivo',verb:'Verbo',adj:'Adjetivo',adv:'Advérbio',phrase:'Expressão',proverb:'Provérbio',intj:'Interjeição',pron:'Pronome',prep:'Preposição',conj:'Conjunção',num:'Numeral',det:'Determinante',particle:'Partícula',postp:'Posposição',counter:'Classificador'};
const themes = [
  ['Comida e bebida','cup',/food|dish|ingredient|breakfast|lunch|dinner|fruit|vegetable|beverage|wine|cheese|coffee|bread|tea|restaurant|cook|eating|meat|drink|soup|sauce/],
  ['Viagem e transporte','plane',/travel|transport|train|aircraft|airport|journey|ticket|vehicle|bicycle|flight|hotel|passport|bus|station|railway|ship|road/],
  ['Casa e cidade','pin',/house|apartment|furniture|kitchen|bedroom|bathroom|building|city|street|village|room|town|garden|door|window|roof|floor/],
  ['Pessoas e relações','heart',/friend|family|sister|brother|father|mother|relative|child|marry|marriage|love|relationship|neighbor|parent|cousin|spouse/],
  ['Trabalho e estudo','book',/work|business|employ|school|student|teacher|education|office|salary|company|university|course|lesson|study|learning|book/],
  ['Natureza','sun',/animal|plant|fish|bird|tree|forest|mountain|river|weather|sea|water|flower|insect|species|ocean|soil|climate/],
  ['Corpo e saúde','heart',/health|medical|disease|body|blood|illness|exercise|injury|hospital|pain|doctor|medicine|muscle|bone|skin|infection/]
];
const lessonIcons=['cup','pin','plane','chat','book','sun'];
const scenes=[
  '<path d="M23 28h36v16a13 13 0 0 1-13 13H36a13 13 0 0 1-13-13z" fill="#fff8e8"/><path d="M59 32h7a6 6 0 0 1 0 12h-7M15 61h54M35 21q-7-5 0-11m12 11q-7-5 0-11"/>',
  '<path d="M15 57V41h25V23h29" fill="none" stroke-dasharray="4 4"/><path d="M34 19c0 9-9 18-9 18s-9-9-9-18a9 9 0 1 1 18 0z" fill="#e5abca"/><circle cx="25" cy="19" r="3"/><path d="M71 18h-9v-9h9z" fill="#fff8e8"/>',
  '<rect x="20" y="26" width="47" height="32" rx="6" fill="#e5abca"/><path d="M36 26v-7h15v7M31 26v32m25-32v32m-28 0v5m30-5v5"/>',
  '<path d="M16 15h47v25H42l-13 10V40H16z" fill="#fff8e8"/><path d="M45 36h24v23H58l-7 7v-7h-6z" fill="#e5abca"/><path d="M23 24h27m-27 7h16"/>',
  '<path d="M43 23q-13-10-29-6v38q16-4 29 7 13-11 29-7V17q-16-4-29 6v39" fill="#fff8e8"/><path d="M23 29h11m-11 9h11m18-9h11m-11 9h11"/>',
  '<circle cx="43" cy="36" r="13" fill="#fff8e8"/><path d="M43 10v8m0 36v8M17 36h8m36 0h8M25 18l6 6m24 24 6 6M25 54l6-6m24-24 6-6"/>'
];
const scene = i => '<svg class="scene" aria-hidden="true" viewBox="0 0 86 72"><rect x="1" y="1" width="84" height="70" rx="16" fill="'+['#f6d677','#e1ead7','#f6d677','#e1ead7','#f6d677','#ecc2d4'][i]+'"/><g stroke="#202820" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" fill="none">'+scenes[i]+'</g></svg>';
const clean = val => String(val ?? '').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const normalize = val => val.normalize('NFKD').replace(/[’‘]/g,"'").replace(/\p{M}/gu,'').toLocaleLowerCase();
const num = n => n.toLocaleString(supportTag());
function read(key,fallback){
  try { return JSON.parse(localStorage.getItem('lpd-'+key)) ?? fallback; }
  catch { return fallback; }
}
function write(key,value){try{localStorage.setItem('lpd-'+key,JSON.stringify(value));}catch{/* Sessão sem armazenamento. */}}
let lang=read('language','eng');
if (!Object.hasOwn(languages,lang)) lang='eng';
let level=read('level',0);
if (!Number.isInteger(level)||level<0||level>5) level=0;
let support=read('support-language','eng')==='spa'?'spa':'eng';
let portugueseSupport={};
let mandarinSupport={};
const reviews=read('review-schedule',{});
const done=read('done',{});
const saved=new Set(read('saved',[]));
const cache={};
const loadingCourses=new Set();
let loadingError=false, limit=18;
function nativeText(text,tag='span'){
  if(screen==='licao')text=lessonLevelText(text);
  return '<'+tag+' lang="'+languages[lang][2]+'" dir="auto">'+clean(text)+'</'+tag+'>'}
function dateKey(){
  const d=new Intl.DateTimeFormat('sv-SE',{timeZone:'America/Sao_Paulo',year:'numeric',month:'2-digit',day:'2-digit'}).format(new Date());
  return d;
}
function dailyIndex(){return Math.floor(Date.parse(dateKey())/86400000);}
function displayDailyWord(){
  const word=(englishLessonPlan()?.words[0][0]||currentLesson?.focus?.word||currentLesson?.vocabulary.word);
  const exists=word&&wordIndex[lang]?.lookup.has(word);
  $('findDaily').hidden=!exists;
  $('dailyWord').innerHTML=word?nativeText(word)+lessonVocabularyAudio(word):ui('Carregando o acervo…');
}
function speech(text,rate=.88,locale=languages[lang][2],options={}){
  stopA1Pronunciation();
  if(!window.speechSynthesis||typeof SpeechSynthesisUtterance==='undefined')return false;
  if(!options.onend&&lessonPlayback)stopLessonPlayback();
  const engine=window.speechSynthesis;
  const utterance=new SpeechSynthesisUtterance(text);
  const voices=engine.getVoices();
  const exact=voices.filter(voice=>voice.lang.toLowerCase()===locale.toLowerCase());
  const matching=exact.length?exact:voices.filter(voice=>voice.lang.split('-')[0]===locale.split('-')[0]);
  const voice=matching[options.voiceIndex]||matching[0];
  if(voice)utterance.voice=voice;
  utterance.lang=locale;
  utterance.rate=rate;
  if(options.onend)utterance.onend=options.onend;
  utterance.onerror=options.onerror||((event)=>{
    if(!['interrupted','canceled'].includes(event.error))$('resultCount').textContent='A voz deste idioma não está disponível no navegador.';
  });
  try{
    if(options.cancelFirst!==false)engine.cancel();
    engine.speak(utterance);
    return true;
  }catch{return false;}
}
function drawLanguages(){
  refreshInterface();
  drawWriting();
  $('courseSelector').innerHTML=Object.entries(languages).map(([key,[,label]])=>'<option value="'+key+'">'+clean(ui(label))+'</option>').join('');
  $('courseSelector').value=lang;
  $('lessonsNav').textContent=routeLabel('Lições','Lessons','Lecciones');
  $('catalogHeading').textContent=routeLabel('Trilha de lições','Course lessons','Recorrido de lecciones');
  $('studyTitle').textContent=routeLabel('Lições por nível','Lessons by level','Lecciones por nivel');
  switchScreen();
  $('languages').innerHTML=Object.entries(languages).map(([k,[short,label]])=>'<button data-language="'+k+'" aria-pressed="'+(lang===k)+'"><span>'+short+'</span>'+clean(ui(label))+'</button>').join('');
}
const positions=read('lesson-position',{});
const courseLevels=read('course-levels',{});
if(!Object.hasOwn(courseLevels,lang))courseLevels[lang]=level;
function changeCourse(next){
  if(next===lang)return;
  courseLevels[lang]=level;
  lang=next;
  const savedLevel=courseLevels[next];
  level=Number.isInteger(savedLevel)&&savedLevel>=0&&savedLevel<levels.length?savedLevel:0;
  write('course-levels',courseLevels);
  write('level',level);
  write('language',lang);
}

let unit=0, currentLesson, exactWord='';
function selectedUnit(){
  const stored=positions[lang+'-'+level];
  return Number.isInteger(stored)&&stored>=0&&stored<lessonsPerLevel?stored:0;
}
function setUnit(next){
  unit=Math.max(0,Math.min(lessonsPerLevel-1,next));
  positions[lang+'-'+level]=unit;
  write('lesson-position',positions);
}
function openingExamples(first,second,third,usedPhotos){
  return '<div class="lesson-example-grid">'+[first,second,third].map((example,i)=>renderExample(example,i+1,undefined,usedPhotos)).join('')+'</div>';
}
function buildCore(){
  const [theme,word,example,translation,title,tip,grammar,grammarPt]=study[lang][level];
  const [phrase,phraseGloss,phraseExample,phrasePt]=phrases[lang][level];
  const [word2,word2Pt,phrase2,phrase2Pt]=coreSeconds[lang][level];
  const [word3,word3Pt,phrase3,phrase3Pt]=extraOpening[lang][level];
  const head=word.split(' (')[0];
  const item=wordIndex[lang]?.lookup.get(head);
  const links=item?connections(item):curriculum[lang]?.[level]?.[0]?connections(curriculum[lang][level][0]):'';
  const usedPhotos=new Set();
  const vocabCover=lessonSectionPhoto(lessonVisualTheme(),'section',usedPhotos);
  const grammarCover=lessonSectionPhoto(lessonVisualTheme(),'grammar',usedPhotos);
  const section='<article class="lesson-card">'+vocabCover+'<span class="tag">'+icon(lessonIcons[level])+' '+clean(ui(theme))+'</span>'+
    '<div class="term-heading"><h3>'+nativeText(head)+'</h3>'+lessonVocabularyAudio(head)+'</div><p class="meta">'+clean(companionText(glosses[lang][level]))+
    (word.includes(' (')?' · '+clean(word.slice(word.indexOf(' (')+2,-1)):'')+'</p>'+
    openingExamples({text:example,translation},{text:word2,translation:word2Pt},{text:word3,translation:word3Pt},usedPhotos)+
    '<details><summary>'+ui('Mais uma expressão')+'</summary><div class="term-heading"><h3>'+nativeText(phrase)+'</h3>'+lessonVocabularyAudio(phrase)+'</div><p>'+clean(companionText(phraseGloss))+'</p>'+
    openingExamples({text:phraseExample,translation:phrasePt},{text:phrase2,translation:phrase2Pt},{text:phrase3,translation:phrase3Pt},usedPhotos)+
    '</details>'+links+'</article>';
  const audio={word:example,phrase:phraseExample};
  const tipSection='<article class="lesson-card">'+grammarCover+'<span class="tag">'+icon('book')+' '+ui('Gramática')+' · '+levels[level]+'</span>'+
    grammarPanel(lang,level,false,[title,tip,grammar,grammarPt],audio,usedPhotos)+'</article>';
  return {cards:[section,tipSection],cardPhotos:usedPhotos,grammarTitle:title,cue:lang==='por'?ui('Como você diria em português?'):'Como você diria em '+languages[lang][1].toLowerCase()+'?',
    clue:companionText(grammarPt),answer:grammar,answerNative:true,audio,
    vocabulary:{word:head,expression:phrase,wordExample:{text:example,pt:companionText(translation)},expressionExample:{text:phraseExample,pt:companionText(phrasePt)}}};
}
let paintedLesson='';
function drawLesson(){
  stopA1Pronunciation();
  closeLessonFocus(false);
  const route=screen==='licao'?lessonHash(unit):'';
  if(paintedLesson!==route)$('dailyFocusToolbar').closest('details').open=false;
  const expanded=paintedLesson===route?
    [...$('lesson').querySelectorAll('[data-lesson-panel]')].filter(panel=>panel.open).map(panel=>panel.dataset.lessonPanel):[];
  paintedLesson=route;
  stopLessonPlayback();
  stopVoiceTools();
  drawStudyHome();
  drawStatistics();
  $('levels').innerHTML=levels.map((l,i)=>'<button data-level="'+i+'" aria-pressed="'+(i===level)+'">'+l+'</button>').join('');
  const key=starterKey(level,unit);
  const count=Array.from({length:lessonsPerLevel},(_,i)=>done[starterKey(level,i)]).filter(Boolean).length;
  $('progress').textContent=ui(languages[lang][1])+' · '+levels[level]+' · '+count+' '+ui('de')+' '+lessonsPerLevel+' '+ui('lições concluídas');
  $('levelProgress').value=count;
  $('levelDescription').textContent=[
    'A1 · Entender e usar frases simples no dia a dia.',
    'A2 · Lidar com conversas e situações rotineiras.',
    'B1 · Contar experiências e dar explicações simples.',
    'B2 · Defender pontos de vista e adaptar o tom.',
    'C1 · Usar o idioma com precisão em contextos variados.',
    'C2 · Compreender nuances e reformular ideias com precisão.'
  ][level];
  $('completionStatus').textContent=done[key]?'Esta lição está concluída.':'Você pode abrir qualquer lição. O progresso conta as que você marcou como concluídas.';
  if(screen!=='licao'){
    currentLesson=null;
    $('lesson').innerHTML='';
    drawCatalog();
    return;
  }
  lessonHeader();
  const lesson=curriculum[lang]?.[level][unit-1];
  const plan=englishLessonPlan();
  const authored=plannedEnglishContent();
  currentLesson=authored?buildCompletedEnglishLesson(plan,authored):unit===0?buildCore():lesson?buildThematicLesson(unit,lesson):null;
  displayDailyWord();
  const navigation='<div class="lesson-nav"><div><strong>'+ui('Lição')+' '+(unit+1)+' '+ui('de')+' '+lessonsPerLevel+'</strong><p class="meta">'+
    ui(unit===0?'Lição de abertura':'Prática guiada')+'</p></div><div class="controls">'+
    '<button id="previousLesson" '+(unit===0?'disabled':'')+'>'+ui('Anterior')+'</button>'+
    '<button id="nextLesson" '+(unit===lessonsPerLevel-1?'disabled':'')+'>'+ui('Próxima')+'</button>'+
    '<form id="goLesson"><label for="lessonNumber">'+ui('Ir à lição')+'</label><input type="number" id="lessonNumber" min="1" max="'+lessonsPerLevel+'" value="'+(unit+1)+'" required><button>'+ui('Ir')+'</button></form></div></div>';
  if(!currentLesson){
    $('lesson').innerHTML=navigation+'<p role="status">'+(loadingError?'O conteúdo da lição não carregou. <button type="button" id="lessonRetry">Tentar novamente</button>':'Carregando a prática guiada…')+'</p>';
    return;
  }
  const {cards,vocabulary}=currentLesson;
  const active=Boolean(done[key]);
  const content=authored||lessonText(lang,unit,level,vocabulary);
  currentLesson.practiceContent=content;
  const theme=lessonVisualTheme();
  const used=new Set(currentLesson.cardPhotos);
  const [vocabularyPhoto,grammarPhoto]=authored?englishA1BlockPhotos():[];
  if(authored){if(vocabularyPhoto)used.add(vocabularyPhoto.file);if(grammarPhoto)used.add(grammarPhoto.file);}
  const status=plan?'<div class="lesson-plan-status"><strong>Inglês americano '+levels[level]+' · Lote '+(level===1?'431–560':unit>=180?'181–300':'01–180')+'</strong><p>Estude o vocabulário em contexto, ouça a cena e aplique a gramática na prática.</p><a href="'+(level===1?'plano-ingles-a2-431-560.csv':unit>=180?'plano-ingles-a1-181-300.csv':'plano-ingles-a1-01-50.csv')+'" download>Baixar a planilha deste lote</a></div>':'';
  $('lesson').innerHTML=navigation+status+lessonAudioBar()+'<div class="lesson-panels">'+
    lessonPanel('lexicon',plan?plan.words.slice(0,2).map(([term])=>nativeText(term)).join(' · '):nativeText(currentLesson.focus?.word||vocabulary.word)+' · '+nativeText(vocabulary.expression),
      (authored?renderCompletedEnglishVocabulary(plan,content,vocabularyPhoto):cards[0])+renderWordUse(currentLesson),{used})+
    lessonPanel('grammar',clean(plan?.grammar||companionText(currentLesson.grammarTitle)),authored?renderCompletedEnglishGrammar(plan,content,grammarPhoto,used):cards[1],{used})+
    lessonPanel('pronunciation',routeLabel('Um som para ouvir e repetir','A sound to hear and repeat','Un sonido para escuchar y repetir'),renderPronunciation(),{used})+
    renderLessonText(content,used)+
    lessonPanel('sceneVocabulary',plan?clean(plan.title):clean(routeLabel(...sceneExtensionAt(theme).title)),authored?renderCompletedEnglishScene(plan,content):renderSceneArticle(content,vocabulary,theme),{used})+
    lessonPanel('workshop',routeLabel('Quatro rodadas de escuta e uma fala sua','Four listening rounds and your own line','Cuatro rondas de escucha y una intervención propia'),renderSceneWorkshop(vocabulary,theme),{used})+
    storySection(unit+1,used)+
    lessonPanel('practice',routeLabel('14 exercícios em sete áreas','14 exercises across seven areas','14 ejercicios en siete áreas'),exercisePane(currentLesson),{used})+'</div>'+
    '<div class="controls lesson-end-actions"><button id="complete" class="primary" aria-pressed="'+active+'">'+icon('check')+(' '+ui(active?'Lição concluída':'Marcar como estudada'))+'</button>'+
    '<button id="daily">'+icon('sun')+' '+ui('Escolher próxima lição de estudo')+'</button></div>'+
    '<p class="status" id="lessonStatus" role="status"></p>';
  for(const panel of $('lesson').querySelectorAll('[data-lesson-panel]')){
    panel.open=expanded.includes(panel.dataset.lessonPanel);
    panel.addEventListener('toggle',()=>{
      if(panel.open)return;
      if(panel.contains(lessonPlayback?.row||lessonPlayback?.button||null))stopLessonPlayback();
      if(panel.dataset.lessonPanel==='pronunciation')stopA1Pronunciation();
      if(['practice','lexicon'].includes(panel.dataset.lessonPanel))stopVoiceTools();
    });
  }
  connectStory();
}
function parseWordHash(){
  const match=location.hash.match(/^#verbete\/([a-z]{3})\/(.+)$/);
  if(!match||!Object.hasOwn(languages,match[1]))return null;
  try{const word=decodeURIComponent(match[2]);return {language:match[1],word:match[1]==='eng'&&word==='tom'?'Tom':word};}catch{return null;}
}
function clearWordHash(){
  exactWord='';
  if(parseWordHash())history.replaceState(null,'','#dicionario');
}
function openPortugueseCourse(){
  const chosen={'#portugues-en':'eng','#portugues-es':'spa'}[location.hash];
  if(!chosen)return false;
  support=chosen;changeCourse('por');unit=selectedUnit();reviewOpen=false;
  write('language',lang);write('support-language',support);
  exactWord='';$('query').value='';$('type').value='';$('theme').value='';
  drawLanguages();drawLesson();loadWords();renderReview();
  location.hash=catalogHash();
  return true;
}
function followWordHash(){
  stopA1Pronunciation();
  closeLessonFocus(false);
  stopLessonPlayback();
  stopVoiceTools();
  switchScreen();
  if(applyLessonRoute(parseLessonRoute())||openPortugueseCourse())return;
  const target=parseWordHash();
  if(!target){
    if(exactWord){exactWord='';$('query').value='';drawWords();}
    if(screen==='estudo')drawLesson();
    return;
  }
  const changed=lang!==target.language;
  changeCourse(target.language);
  if(changed){write('language',lang);unit=selectedUnit();reviewOpen=false;drawLanguages();drawLesson();renderReview();}
  exactWord=target.word;
  $('query').value=target.word;$('type').value='';$('theme').value='';$('dictLevel').value='';limit=18;
  if(changed||!cache[lang])loadWords();
  else drawWords();
  $('dicionario').scrollIntoView?.();
  focusLinkedEntry();
}
function loadWords(){
  const selected=lang;
  loadingError=false;
  drawWords();
  if(cache[selected]||loadingCourses.has(selected))return;
  loadingCourses.add(selected);
  const paths=[selected+'.json',selected+'-examples.json',selected+'-audit.json',selected+'-third.json'];
  if(selected==='por'||selected==='cmn')paths.push(selected+'-support.json');
  const forms=selected==='cmn'?Promise.resolve({}):loadJson(selected+'-forms.json').catch(()=>({}));
  Promise.all([Promise.all(paths.map(loadJson)),forms]).then(([[rows,examples,audit,third,translations],metadata])=>{
    catalogForms[selected]=metadata;
    if(selected==='por')portugueseSupport=translations;
    if(selected==='cmn')mandarinSupport=translations;
    thirdExamples[selected]=third;
    lexiconAudits[selected]=audit;
    corpusExamples[selected]=examples;
    const makeItem=(row,lessonEntry)=>{
      const [w,g]=row;
      const theme=lessonEntry?themes.find(t=>t[0]===lessonEntry.theme):
        themes.find(t=>g.toLowerCase().split(/[^a-z]+/).some(word=>word.length>2&&t[2].test(word)));
      return {row, key:selected+'|'+w, theme:theme?.[0]||'Vocabulário geral',icon:theme?.[1],
        terms:focusTerms(g),search:normalize([w,g,row[8],row[10]].join(' ')),lessonEntry};
    };
    const base=localizedEntries(selected,rows).map(row=>makeItem(row));
    curriculum[selected]=lessonItems(base);
    applyReviewedEntries(selected,base);
    const supplements=addSceneWords(selected,lessonLexicon(selected));
    const words=new Map(base.map(item=>[item.row[0],item]));
    for(const [word,entry] of supplements){
      const existing=words.get(word);
      const item=makeItem(entry.row,entry);
      if(existing){
        item.search+=' '+existing.search;
        item.original=existing.row;
        item.row[8] ||= existing.row[8];
      }
      words.set(word,item);
    }
    const index=courseLevelIndex(selected);
    cache[selected]=[...words.values()];
    for(const item of cache[selected])item.courseLevel=index.get(item.row[0]);
    wordIndex[selected]=makeIndex(base);
    wordIndex[selected].lookup=words;
    if(lang===selected){drawWords();drawLesson();renderReview();if(screen==='favoritos')renderFavorites();focusLinkedEntry();}
  }).catch(()=>{if(lang===selected){loadingError=true;drawWords();drawLesson();}}).finally(()=>loadingCourses.delete(selected));
}
function focusLinkedEntry(){
  if(exactWord)$('results').querySelector('h3')?.focus({preventScroll:true});
}
function card(item,i){
  const [w,g,p,f,,,,,reading,,ptWord,,,ptId,ptAuthor,origin]=item.row;
  const info=ui(classes[p]||p);
  const tag=f===2?ui('Gíria / coloquial'):f===1&&p!=='phrase'?info+' · '+ui('Expressão'):info;
  const mark=f===2||f===1?'chat':p==='verb'?'bolt':item.icon||'book';
  const dictUrl='https://en.wiktionary.org/wiki/'+encodeURIComponent(w)+'#'+languages[lang][3];
  const ptSource=ptId&&!Object.hasOwn(lexiconAudits[lang],w)?'<a href="https://tatoeba.org/en/sentences/show/'+clean(ptId)+'" target="_blank" rel="noopener">Tradução'+(ptAuthor?' · '+clean(ptAuthor):'')+'</a>':'';
  const original=item.original&&item.original[15]!=='original'
    ?'<details><summary>Definição no acervo</summary><p lang="en">'+clean(item.original[1])+'</p></details>':'';
  const examples=examplesHtml(item,illustration(item));
  const definition=lang==='cmn'&&mandarinSupport.definitions?.[g]?'<span lang="pt-BR">'+clean(mandarinSupport.definitions[g])+'</span>':lang==='por'?'<span lang="'+(support==='spa'&&companionText(g)!==g?'es':'en')+'">'+clean(companionText(g))+'</span>':
    item.lessonEntry||item.reviewed?'<span lang="pt-BR">'+clean(g)+'</span>':(ptWord?'<b>'+clean(ptWord)+'</b> · ':'')+'<span lang="en">'+clean(g)+'</span>';
  const status=item.courseLevel?'<span class="tag"> '+item.courseLevel+'</span>':'';
  return '<article class="entry"><div class="entry-head"><div><span class="tag">'+icon(mark)+' '+clean(tag)+'</span><h3 tabindex="-1">'+nativeText(w)+'</h3>'+(reading?'<span class="meta"'+(lang==='cmn'?' lang="zh-Latn"':'')+'>'+clean(reading)+'</span>':pinyinLine(w))+'</div><div class="controls"><button data-audio="'+i+'" aria-label="Ouvir '+clean(w)+'">'+icon('speaker')+'</button><button data-save="'+i+'" aria-label="Favorito para '+clean(w)+'" aria-pressed="'+saved.has(item.key)+'">'+icon('heart')+'</button></div></div><p>'+definition+'</p>'+status+examples+entryNote(item)+original+dictionaryExtras(item)+connections(item)+'<p class="meta">'+(item.theme?clean(ui(item.theme))+' · ':'')+'<a href="'+dictUrl+'" target="_blank" rel="noopener">'+(origin?'Consultar no Wiktionary':'Wiktionary')+'</a>'+(ptSource?' · '+ptSource:'')+'</p><button type="button" data-report="'+i+'">Reportar erro</button><div class="entry-report" hidden></div></article>';
}
let visible=[];
function drawWords(){
  $('results').innerHTML='';
  $('clearQuery').hidden=!$('query').value;
  $('more').hidden=true;
  const words=cache[lang];
  displayDailyWord();
  $('total').textContent=words?num(words.length)+' · '+ui(languages[lang][1]):ui('Carregando o acervo…');
  if(!words){
    $('resultCount').innerHTML=loadingError?'O acervo não carregou. <button id="retry">Tentar novamente</button>':'';
    $('retry')?.addEventListener('click',loadWords);
    return;
  }
  const query=normalize($('query').value.trim());
  const type=$('type').value,theme=$('theme').value,filterLevel=$('dictLevel').value;
  showSuggestions(words,query);
  const matching=words.filter(x=>(exactWord?x.row[0]===exactWord:!query||x.search.includes(query)||(lang==='por'&&support==='spa'&&normalize(companionText(x.row[1])).includes(query)))&&(!theme||x.theme===theme)&&(!filterLevel||x.courseLevel===filterLevel)&&(!type||(type==='saved'?saved.has(x.key):type==='1'?isExpression(x):type==='2'?x.row[3]===2:x.row[2]===type)));
  if(query) matching.sort((a,b)=>Number(normalize(b.row[0])===query)-Number(normalize(a.row[0])===query)||Number(normalize(b.row[0]).startsWith(query))-Number(normalize(a.row[0]).startsWith(query)));
  visible=matching.slice(0,limit);
  $('resultCount').textContent=matching.length?num(matching.length)+' '+ui(matching.length===1?'resultado':'resultados')+' · '+num(visible.length)+' '+ui('na lista'):ui('Nenhum verbete encontrado.');
  $('results').innerHTML=visible.map(card).join('');
  $('more').hidden=visible.length===matching.length;
}
$('languages').addEventListener('click',e=>{
  const choice=e.target.closest('[data-language]');
  if(!choice||choice.dataset.language===lang)return;
  if(['licao','estudo'].includes(screen)){
    const next=choice.dataset.language;
    const savedLevel=courseLevels[next];
    location.hash=catalogHash(next,Number.isInteger(savedLevel)&&savedLevel>=0&&savedLevel<levels.length?savedLevel:0);
    return;
  }
  changeCourse(choice.dataset.language);
  clearWordHash();unit=selectedUnit();limit=18;$('query').value='';
  reviewOpen=false;drawLanguages();drawLesson();loadWords();renderReview();
});
$('levels').addEventListener('click',e=>{
  const button=e.target.closest('[data-level]');
  if(button)location.hash=catalogHash(lang,Number(button.dataset.level));
});
$('lessonSections').addEventListener('click',event=>{
  const button=event.target.closest('[data-lesson-section]');
  if(button)openLessonSection(button.dataset.lessonSection);
});
$('lesson').addEventListener('submit',e=>{
  if(handleExerciseSubmit(e))return;
  if(e.target.id!=='goLesson')return;
  e.preventDefault();
  const value=Number($('lessonNumber').value);
  if(!Number.isInteger(value)||value<1||value>lessonsPerLevel)return;
  goToLesson(value-1);
});
$('lesson').addEventListener('change',changeSceneRole);
$('lesson').addEventListener('input',event=>{
  if(['exerciseInput','exerciseDraft'].includes(event.target.id))exerciseAttempt().draft=event.target.value;
  if(event.target.id==='roleplayDraft')storeRoleplayDraft(event.target.value);
});
$('lesson').addEventListener('click',e=>{
  if(handleA1PronunciationClick(e)||handleWordUseClick(e)||handleSceneRoleplay(e)||handleGrammarChoice(e)||handleA1Quiz(e))return;
  handleSceneResponse(e);
  if(handleLessonTools(e))return;
  const b=e.target.closest('button');
  if(!b)return;
  if(b.id==='lessonRetry'){loadWords();drawLesson();return;}
  if(b.dataset.say){
    const line=currentLesson?.audio[b.dataset.say];
    if(line&&!speech(line))$('lessonStatus').textContent='O navegador não oferece leitura em voz alta.';
    return;
  }
  if(b.id==='complete'){
    const key=starterKey(level,unit);
    if(done[key])delete done[key];else done[key]=dateKey();
    write('done',done);
  } else if(b.id==='daily'){
    const next=Array.from({length:lessonsPerLevel},(_,i)=>i).find(i=>!done[starterKey(level,i)]);
    goToLesson(next??dailyIndex()%lessonsPerLevel);return;
  } else if(b.id==='previousLesson'){goToLesson(unit-1);return;}
  else if(b.id==='nextLesson'){goToLesson(unit+1);return;}
  else return;
  drawLesson();
  $(b.id)?.focus();
});
for(const id of ['query','type','theme','dictLevel'])$(id).addEventListener(id==='query'?'input':'change',()=>{
  clearWordHash();limit=18;drawWords();
});
function clearDictionarySearch(){
  $('query').value='';
  clearWordHash();
  limit=18;
  drawWords();
  $('query').focus();
}
$('clearQuery').addEventListener('click',clearDictionarySearch);
$('query').addEventListener('keydown',event=>{
  if(event.key==='Escape'&&$('query').value){
    event.preventDefault();
    clearDictionarySearch();
  }
});
$('findDaily').addEventListener('click',()=>{
  const word=(englishLessonPlan()?.words[0][0]||currentLesson?.focus?.word||currentLesson?.vocabulary.word);
  if(!word||!wordIndex[lang]?.lookup.has(word))return;
  location.hash=wordHash(word);
});
window.addEventListener('hashchange',followWordHash);
$('more').addEventListener('click',()=>{
  const first=limit;
  limit+=18;drawWords();
  $('results').querySelector('[data-audio="'+first+'"]')?.focus({preventScroll:true});
});
$('results').addEventListener('click',e=>{
  if(handleLessonTools(e))return;
  const b=e.target.closest('button');
  if(!b)return;
  if(b.dataset.report!==undefined){
    const item=visible[Number(b.dataset.report)];
    const block=b.closest('.entry').querySelector('.entry-report');
    block.innerHTML='<label>Relato para a equipe do curso<textarea rows="4"></textarea></label><button type="button">Copiar relato</button><p role="status"></p>';
    const input=block.querySelector('textarea');
    input.value=languages[lang][1]+' · '+item.row[0]+'\nProblema encontrado: ';
    block.querySelector('button').addEventListener('click',async event=>{
      event.stopPropagation();
      try{await navigator.clipboard.writeText(input.value);block.querySelector('p').textContent='Relato copiado.';}
      catch{input.focus();input.select?.();block.querySelector('p').textContent='Selecione e copie o relato.';}
    });
    block.hidden=false;input.focus();return;
  }
  if(b.dataset.audio!==undefined){
    if(!speech(visible[b.dataset.audio].row[0]))$('resultCount').textContent='O navegador não oferece leitura em voz alta.';
    return;
  }
  if(b.dataset.save===undefined)return;
  const item=visible[b.dataset.save];
  if(saved.has(item.key))saved.delete(item.key);else saved.add(item.key);
  write('saved',[...saved]);reviewOpen=false;renderReview();b.setAttribute('aria-pressed',String(saved.has(item.key)));
  if($('type').value==='saved'&&!saved.has(item.key)){drawWords();$('type').focus();}
});
$('writing').addEventListener('click',event=>{
  const button=event.target.closest('[data-writing-say]');
  if(button&&!speech(button.dataset.writingSay))$('writingStatus').textContent='A voz desse idioma não está disponível no navegador.';
});
$('courseSelector').addEventListener('change',event=>{
  const wanted=event.target.value;
  if(Object.hasOwn(languages,wanted))$('languages').querySelector('[data-language="'+wanted+'"]')?.click();
});
$('supportLanguage').addEventListener('change',e=>{
  support=e.target.value==='spa'?'spa':'eng';
  write('support-language',support);reviewOpen=false;
  const route=parseLessonRoute();
  if(route&&lang==='por'){
    location.hash=route.screen==='licao'?lessonHash(unit):catalogHash();
  }else{drawLanguages();drawLesson();drawWords();renderReview();}
});
$('reviewCard').addEventListener('click',event=>{
  const button=event.target.closest('button');
  if(!button)return;
  if(button.id==='reviewReveal'){reviewOpen=true;renderReview();$('reviewCard').querySelector('[data-grade]')?.focus();return;}
  if(!button.dataset.grade||!reviewOpen)return;
  const item=dueReviews()[0];
  if(item){rateReview(item,button.dataset.grade);reviewOpen=false;renderReview();$('reviewReveal')?.focus();}
});
const initialWord=parseWordHash();
if(initialWord)changeCourse(initialWord.language);
unit=selectedUnit();
setupProfessional();
bindLessonAudio();
drawLanguages();drawLesson();renderReview();
if(initialWord||parseLessonRoute())followWordHash();else if(!openPortugueseCourse())loadWords();

setupLessonFocus();
