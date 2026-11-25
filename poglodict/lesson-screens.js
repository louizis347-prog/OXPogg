const lessonsPerArc=50;
const lessonsPerBlock=10;
const arcArt=['map','ticket','city','chat','notebook','park','flag'];
const lessonGlyphs={
  map:'<path d="M7 12 17 8l14 4 10-4v26l-10 4-14-4-10 4zm10-4v26m14-22v26"/><circle cx="23" cy="21" r="2.5"/><path d="m20 27 8-9"/>',
  ticket:'<path d="M6 14h36v8a4 4 0 0 0 0 8v7H6v-7a4 4 0 0 0 0-8zm25 2v3m0 4v3m0 4v3M12 25h10"/>',
  city:'<path d="M5 38h38M9 38V19l10-5v24m0 0V8h15v30m0 0V23h6v15M24 14h4m-4 7h4m-4 7h4m-15-3h2"/>',
  chat:'<path d="M9 10h25a5 5 0 0 1 5 5v11a5 5 0 0 1-5 5H20l-9 7v-7H9a5 5 0 0 1-5-5V15a5 5 0 0 1 5-5zM12 17h20m-20 7h13"/><path d="m34 35 7 5v-6"/>',
  notebook:'<path d="M13 8h23a3 3 0 0 1 3 3v27H13a5 5 0 0 1-5-5V13a5 5 0 0 1 5-5zm4 0v30M4 15h9m-9 8h9m-9 8h9m10-13h10m-10 7h7"/>',
  park:'<path d="M7 38h34M19 38V23m-9 3c-5-1-6-7-2-10 1-6 6-10 11-9 5 0 9 3 10 7 6 3 6 9 2 12H10zm23 12v-7m-4 0h9"/>',
  flag:'<path d="M12 39V8m0 2c7-5 16 4 25-1v17c-9 5-18-4-25 1M6 39h31"/><circle cx="23" cy="18" r="2"/>',
  cup:'<path d="M9 21h24v8a10 10 0 0 1-10 10h-4A10 10 0 0 1 9 29zm24 1h4a5 5 0 0 1 0 10h-4M6 42h36m-24-25c-6-5 4-5-1-10m10 10c-6-5 4-5-1-10"/>',
  health:'<path d="M10 13h28v27H10zm8-1V8h12v4m-6 7v14m-7-7h14"/>',
  book:'<path d="M4 10c8-3 15-1 20 4 5-5 12-7 20-4v26c-8-3-15-1-20 4-5-5-12-7-20-4zm20 4v25m-15-21h9m-9 7h9m13-7h8m-8 7h8"/>',
  puzzle:'<path d="M9 8h12c0 6 7 6 7 0h11v12c-6 0-6 7 0 7v13H27c0-6-7-6-7 0H9V27c6 0 6-7 0-7z"/>',
  story:'<path d="M9 13h31v24H9zm6 5h17m-17 5h19m-19 5h12M7 8h27m-26 34h28"/><path d="m39 5 1 3 3 1-3 1-1 3-1-3-3-1 3-1z"/>',
  vocabulary:'<rect x="8" y="8" width="25" height="32" rx="5" fill="var(--study-icon-shade)"/><path d="m13 28 5.5-12L24 28m-9.5-3h8M30 15h9a3 3 0 0 1 3 3v15a3 3 0 0 1-3 3h-9l-5 4v-9"/><path d="M32 21h5m-5 6h5"/>',
  grammar:'<rect x="5" y="8" width="15" height="12" rx="3" fill="var(--study-icon-shade)"/><rect x="25" y="8" width="18" height="12" rx="3"/><rect x="12" y="30" width="24" height="10" rx="3" fill="var(--study-icon-shade)"/><path d="M12.5 20v4h21.5v-4M24 24v6M10 14h5m14 0h10m-21 21h12"/>',
  check:'<path d="m10 25 9 9 19-20"/>'
};
const lessonColors={
  cup:['#f8ddb1','#784519','#8e4b2e'],ticket:['#d8e5f4','#214e73','#7694b4'],
  city:['#d7e9dd','#1c5943','#6d957f'],chat:['#f0dceb','#6c365f','#aa7299'],
  notebook:['#e1e1f7','#484774','#817cad'],park:['#e3e9bc','#495915','#849043'],
  health:['#f5ddd6','#8a4a39','#b78473'],map:['#d9ecec','#24565d','#67a5a6'],
  flag:['#f4e2ba','#65491b','#a88752']
};
const lessonArtByTheme=['cup','ticket','city','chat','notebook','park','health','map'];
function routeLabel(pt,en,es){
  if(lang!=='por')return pt;
  return support==='spa'?es:en;
}
function catalogHash(language=lang,cefr=level,companion=support){
  return '#licoes/'+language+'/'+levels[cefr]+(language==='por'?'/'+companion:'');
}
function lessonHash(index,language=lang,cefr=level,companion=support){
  return '#licao/'+language+'/'+levels[cefr]+'/'+(index+1)+(language==='por'?'/'+companion:'');
}
function parseLessonRoute(hash=location.hash){
  const fields=hash.replace(/^#/,'').split('/');
  const [view,language,cefr]=fields;
  if(!['licao','licoes'].includes(view)||!Object.hasOwn(languages,language))return null;
  const levelIndex=levels.indexOf(cefr?.toUpperCase());
  if(levelIndex<0)return null;
  const isLesson=view==='licao', baseLength=isLesson?4:3;
  const companion=fields[baseLength];
  if(fields.length>baseLength+1||(companion!==undefined&&(language!=='por'||!['eng','spa'].includes(companion))))return null;
  const number=isLesson&&/^[1-9][0-9]{0,2}$/.test(fields[3])?Number(fields[3]):0;
  if(isLesson&&(number<1||number>lessonCount(language,levelIndex)))return null;
  return {screen:isLesson?'licao':'estudo',language,level:levelIndex,unit:isLesson?number-1:null,companion};
}
function goToLesson(index){
  if(!Number.isInteger(index)||index<0||index>=lessonCount())return;
  const hash=lessonHash(index);
  if(location.hash===hash)$('lessonHeading')?.focus();
  else location.hash=hash;
}
function routeIcon(key){
  return '<svg class="route-icon" viewBox="0 0 48 48" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">'+
    lessonGlyphs[key]+'</svg>';
}
function routeIllustration(key){
  const [background,ink,accent]=lessonColors[key];
  return '<svg class="route-illustration" viewBox="0 0 192 112" aria-hidden="true">'+
    '<rect x="3" y="3" width="186" height="106" rx="24" fill="'+background+'"/>'+
    '<path d="M15 84c21 12 43 10 62 0s43-10 64-2 31 8 39 4" fill="none" stroke="'+accent+'" stroke-width="1.5" stroke-dasharray="3 5"/>'+
    '<circle cx="59" cy="43" r="18" fill="#fff" opacity=".48"/><circle cx="147" cy="31" r="9" fill="#fff" opacity=".58"/>'+
    '<circle cx="100" cy="57" r="39" fill="#fff" opacity=".62"/>'+
    '<g transform="translate(67 24) scale(1.4)" fill="none" stroke="'+ink+'" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">'+
    lessonGlyphs[key]+'</g><path d="M30 24v13m-6-6h12m126 19v13m-6-6h12" stroke="'+ink+'" stroke-width="1.5" stroke-linecap="round"/></svg>';
}
function lessonStatusAt(index){
  return Boolean(done[starterKey(level,index)]);
}
function studyTitleAt(index){
  const plan=englishLessonPlan(index);
  if(plan){
    return {title:plan.title,art:englishStore().themes[index]||'map',word:plan.words[0][0]};
  }
  if(index===0){
    const theme=study[lang][level][0];
    return {title:ui(theme),art:lessonArtByTheme[[0,2,1,3,4,7][level]],word:study[lang][level][1].split(' (')[0]};
  }
  const item=curriculum[lang]?.[level]?.[index-1];
  if(!item)return {title:'',art:'map',word:''};
  const scene=activeScene(index,item);
  return {title:scene.city?cityPortuguese[0]:lang==='por'||scene.authored?scene.translation[0]:themeScenes.pt[scene.key][0],
    art:lessonArtByTheme[scene.key],word:item.row[0]};
}
let catalogSignature='';
const catalogExpanded=new Map();
function keepCatalogExpansion(){
  const container=$('arcCatalog');
  if(!container.dataset.track)return;
  const state={arcs:[],blocks:[],unit:Number(container.dataset.unit)};
  for(const arc of container.querySelectorAll('[data-arc][open]'))state.arcs.push(Number(arc.dataset.arc));
  for(const block of container.querySelectorAll('[data-block][open]'))state.blocks.push(Number(block.dataset.block));
  catalogExpanded.set(container.dataset.track,state);
}
function drawCatalog(){
  if(screen!=='estudo')return;
  document.title=ui(languages[lang][1])+' '+levels[level]+' · Pogolo Dict';
  const container=$('arcCatalog'),track=lang+'-'+level+'-'+(lang==='por'?support:'');
  const complete=Array.from({length:lessonCount()},(_,i)=>lessonStatusAt(i));
  $('catalogContinue').href=lessonHash(unit);
  $('catalogPosition').textContent=routeLabel('Continuar na lição ','Continue at lesson ','Continuar en la lección ')+(unit+1);
  const signature=track+'|'+unit+'|'+Boolean(curriculum[lang])+'|'+complete.map(Number).join('');
  if(catalogSignature===signature)return;
  keepCatalogExpansion();
  catalogSignature=signature;
  container.dataset.track=track;
  container.dataset.unit=String(unit);
  const currentArc=Math.floor(unit/lessonsPerArc),currentBlock=Math.floor(unit/lessonsPerBlock);
  const state=catalogExpanded.get(track);
  const arcOpen=i=>state?state.arcs.includes(i)||(state.unit!==unit&&i===currentArc):i===currentArc;
  const blockOpen=i=>state?state.blocks.includes(i)||(state.unit!==unit&&i===currentBlock):i===currentBlock;
  const range=(first,last)=>routeLabel('Lições ','Lessons ','Lecciones ')+first+'–'+last;
  const rows=(first,last)=>Array.from({length:last-first},(_,i)=>first+i).map(i=>{
    const {title,art,word}=studyTitleAt(i);
    const milestone=(i+1)%lessonsPerBlock===0;
    const label=ui('Lição')+' '+(i+1);
    return '<li><a class="lesson-link'+(i===unit?' is-resume':'')+'" href="'+lessonHash(i)+'">'+
      '<span class="lesson-link-icon theme-'+art+'">'+(lang==='eng'&&level===0&&i<20?mangaArtwork(i+1,'icon'):routeIcon(art))+'</span><span class="lesson-link-copy">'+
      '<strong>'+clean(label+(title?' · '+title:''))+'</strong>'+
      (word?'<span>'+nativeText(word)+'</span>':'')+'</span><span class="lesson-link-indicators">'+
      (milestone?'<span class="lesson-indicator story-indicator" aria-label="'+routeLabel('Inclui mini-história','Includes short story','Incluye minicuento')+'">'+routeIcon('story')+'</span>':'')+
      (complete[i]?'<span class="lesson-indicator done-indicator" aria-label="'+routeLabel('Concluída','Completed','Completada')+'">'+routeIcon('check')+'</span>':'')+
      '</span></a></li>';
  }).join('');
  container.innerHTML=Array.from({length:Math.ceil(lessonCount()/lessonsPerArc)},(_,arc)=>{
    const start=arc*lessonsPerArc,end=Math.min(start+lessonsPerArc,lessonCount());
    const total=complete.slice(start,end).filter(Boolean).length;
    const blocks=Array.from({length:Math.ceil((end-start)/lessonsPerBlock)},(_,block)=>{
      const from=start+block*lessonsPerBlock,to=Math.min(from+lessonsPerBlock,end);
      return '<details class="arc-block" data-block="'+Math.floor(from/lessonsPerBlock)+'"'+(blockOpen(Math.floor(from/lessonsPerBlock))?' open':'')+'>'+
        '<summary>'+clean(range(from+1,to))+'<span>'+complete.slice(from,to).filter(Boolean).length+'/'+(to-from)+'</span></summary>'+
        '<ol class="lesson-links" start="'+(from+1)+'">'+rows(from,to)+'</ol></details>';
    }).join('');
    return '<details class="arc-card" data-arc="'+arc+'"'+(arcOpen(arc)?' open':'')+'><summary>'+
      routeIllustration(arcArt[Math.min(arc,arcArt.length-1)])+'<span class="arc-title"><strong>'+routeLabel('Arco ','Arc ','Arco ')+(arc+1)+'</strong><span>'+clean(range(start+1,end))+'</span></span>'+
      '<span class="arc-progress"><span>'+total+'/'+(end-start)+' '+routeLabel('concluídas','completed','completadas')+'</span>'+
      '<progress max="'+(end-start)+'" value="'+total+'" aria-label="'+routeLabel('Progresso do arco','Arc progress','Progreso del arco')+'"></progress></span></summary>'+
      '<div class="arc-blocks">'+blocks+'</div></details>';
  }).join('');
}
function lessonHeader(){
  const {title,art}=studyTitleAt(unit);
  const arc=Math.floor(unit/lessonsPerArc)+1;
  $('lessonBack').href=catalogHash();
  $('lessonBack').textContent=routeLabel('Voltar à trilha','Back to course','Volver al recorrido');
  $('lessonContext').textContent=ui(languages[lang][1])+' · '+levels[level]+' · '+routeLabel('Arco ','Arc ','Arco ')+arc;
  $('lessonHeading').textContent=title||ui('Lição')+' '+(unit+1);
  document.title=$('lessonHeading').textContent+' · '+ui('Lição')+' '+(unit+1)+' · Pogolo Dict';
  $('lessonPosition').textContent=ui('Lição')+' '+(unit+1)+' '+ui('de')+' '+lessonCount();
  const plan=englishLessonPlan();
  $('lessonArtwork').innerHTML=plan&&!plan.file?routeIllustration(art):lessonPhotoFrame((plan&&englishPlanPhoto(plan))||photoForMoment(art,0,'reading'),'lesson-hero-photo',true);
  const visible=Object.entries(lessonPanels).filter(([key])=>key!=='story'||(unit+1)%lessonsPerBlock===0);
  $('lessonSections').innerHTML=visible.map(([key,[mark,...label]])=>
    '<button type="button" aria-controls="'+(key==='story'?'lessonStory':'lesson-panel-'+key)+'" data-lesson-section="'+key+'">'+routeIcon(mark)+clean(routeLabel(...label))+'</button>').join('');
}
const lessonPanels={
  lexicon:['vocabulary','Vocabulário','Vocabulary','Vocabulario'],
  grammar:['grammar','Gramática','Grammar','Gramática'],
  pronunciation:['chat','Pronúncia','Pronunciation','Pronunciación'],
  reading:['book','Leitura','Reading','Lectura'],
  dialogue:['chat','Diálogo','Dialogue','Diálogo'],
  sceneVocabulary:['book','Vocabulário da cena','Scene vocabulary','Vocabulario de la escena'],
  workshop:['chat','Conversa guiada','Guided conversation','Conversación guiada'],
  story:['story','Mini-história','Short story','Minicuento'],
  practice:['puzzle','Prática','Practice','Práctica']
};
const lessonOrientations={
  lexicon:[
    ['Entenda antes de memorizar','Understand before memorizing','Comprende antes de memorizar'],
    ['A palavra central ajuda a reconhecer o assunto da cena. A expressão mostra como você pode dizer algo inteiro nessa situação. Ouça as duas e tente imaginar quem poderia usá-las e em que momento.','The key word helps you recognize the topic. The expression lets you say something complete in that setting. Listen to both and imagine who might use them and when.','La palabra central te ayuda a reconocer el tema. La expresión te permite decir algo completo en esa situación. Escucha las dos e imagina quién podría usarlas y cuándo.'],
    ['Leia o significado, compare os exemplos e guarde uma frase que você realmente diria. Ao terminar, tente repetir essa frase sem olhar.','Read the meaning, compare the examples and pick a sentence you would actually say. Then try saying it without looking.','Lee el significado, compara los ejemplos y elige una frase que usarías. Después intenta decirla sin mirar.']
  ],
  grammar:[
    ['Uma regra para construir frases','A rule for building sentences','Una regla para construir frases'],
    ['Comece identificando o que a estrutura permite fazer: perguntar, localizar, descrever ou ligar ideias. Depois veja quais partes precisam ficar juntas e quais você pode trocar para dizer algo novo.','Start by identifying what the structure lets you do: ask, locate, describe or connect ideas. Then see what must stay together and what you can change to say something new.','Empieza por identificar para qué sirve la estructura: preguntar, ubicar, describir o unir ideas. Después observa qué debe quedarse junto y qué puedes cambiar para decir algo nuevo.'],
    ['Leia a regra e use-a para fazer uma previsão. Consulte o exemplo para verificar sua hipótese e, no desafio, tente aplicar a mesma lógica em outro contexto.','Read the rule and make a prediction. Check it against an example, then apply the same logic in a new context.','Lee la regla y formula una hipótesis. Compruébala con un ejemplo y aplica la misma lógica en otro contexto.']
  ],
  pronunciation:[
    ['Da escuta ao movimento','From listening to movement','De la escucha al movimiento'],
    ['Preste atenção a um traço de cada vez: a posição da língua, a duração ou a altura do som. Essa atenção ajuda você a reconhecer o mesmo padrão quando a palavra aparece em outra frase.','Focus on one feature at a time: tongue position, duration or pitch. This helps you recognize the same pattern when the word appears in another sentence.','Fíjate en un rasgo cada vez: la posición de la lengua, la duración o el tono. Así podrás reconocer el mismo patrón en otra frase.'],
    ['Ouça a primeira palavra em velocidade normal e depois em velocidade lenta. Repita e procure o mesmo som na segunda palavra antes de fazer a atividade.','Hear the first word at normal speed and then slowly. Repeat it and listen for the same sound in the second word before doing the activity.','Escucha la primera palabra a velocidad normal y luego más despacio. Repítela y busca el mismo sonido en la segunda antes de hacer la actividad.']
  ],
  reading:[
    ['Conecte as pistas do texto','Connect the clues in the text','Conecta las pistas del texto'],
    ['Na primeira leitura, procure quem está na cena, onde a ação começa e o que a pessoa quer fazer. É possível entender a situação mesmo com palavras desconhecidas.','On your first read, find who is in the scene, where it starts and what the person wants to do. You can make sense of the scene even with unfamiliar words.','En la primera lectura, busca quién está en la escena, dónde empieza y qué quiere hacer la persona. Puedes entender la situación aunque haya palabras desconocidas.'],
    ['Volte ao texto para localizar a frase que sustenta sua interpretação. Confira a tradução desse trecho e conte a ideia principal em uma frase.','Go back to find the line that supports your interpretation. Check its translation and summarize the main idea in one sentence.','Vuelve al texto para localizar la frase que sustenta tu interpretación. Comprueba su traducción y resume la idea principal en una oración.']
  ],
  dialogue:[
    ['Escute o que cada pessoa quer conseguir','Listen for each speaker’s goal','Escucha qué quiere conseguir cada persona'],
    ['Uma fala pode abrir a conversa, pedir um detalhe ou confirmar uma decisão. Ao ouvir as duas vozes, repare como a segunda pessoa usa o que ouviu para responder.','A line can open a conversation, ask for a detail or confirm a decision. As you hear both voices, notice how the second speaker responds to what they heard.','Una intervención puede abrir la conversación, pedir un detalle o confirmar una decisión. Al escuchar las dos voces, observa cómo responde la segunda persona.'],
    ['Ouça a primeira fala e tente prever a próxima. Depois escute o diálogo inteiro e identifique em que ponto as duas pessoas chegam a um acordo ou encerram a conversa.','Listen to the first line and predict the next one. Then hear the whole dialogue and identify where the speakers agree or end the conversation.','Escucha la primera intervención y anticipa la siguiente. Luego escucha todo el diálogo e identifica cuándo llegan a un acuerdo o cierran la conversación.']
  ],
  sceneVocabulary:[
    ['Use a mesma ideia em outra situação','Use the idea in another situation','Usa la misma idea en otra situación'],
    ['Aqui você volta às palavras da leitura e do diálogo e descobre como elas ajudam a dar continuidade a uma conversa. Observe o que a expressão permite fazer, como pedir uma informação, oferecer uma opção ou confirmar um detalhe.','Here you revisit words from the reading and dialogue and see how they help a conversation continue. Notice what the expression lets you do, such as ask for information, offer an option or confirm a detail.','Aquí retomas palabras de la lectura y del diálogo y ves cómo ayudan a continuar una conversación. Observa qué te permite hacer la expresión: pedir información, ofrecer una opción o confirmar un detalle.'],
    ['Ouça a continuação e escolha uma fala. Troque um detalhe sem mudar sua intenção original. Depois compare o que permaneceu igual.','Listen to the continuation and pick a line. Change one detail while keeping its original purpose. Then compare what stayed the same.','Escucha la continuación y elige una intervención. Cambia un detalle sin alterar su intención. Después compara qué se mantuvo igual.']
  ],
  workshop:[
    ['Passe de ouvir a responder','Move from listening to replying','Pasa de escuchar a responder'],
    ['Nas quatro rodadas de escuta, escolha a resposta que faz a conversa avançar. Se duas parecerem possíveis, volte à pergunta e procure o detalhe que uma delas resolve melhor.','In the four listening rounds, choose the reply that moves the conversation forward. If two seem possible, listen again and find the detail that one addresses better.','En las cuatro rondas de escucha, elige la respuesta que hace avanzar la conversación. Si dos parecen posibles, vuelve a escuchar y busca el detalle que una resuelve mejor.'],
    ['No improviso, escolha um papel, leia o imprevisto e escreva sua fala. Use um molde se precisar e só depois compare com a versão de referência.','For the role-play, choose a role, read the twist and write your line. Use a template if you need one, then compare with the reference.','En la improvisación, elige un papel, lee el giro y escribe tu intervención. Usa un molde si lo necesitas y después compara con la referencia.']
  ],
  story:[
    ['Acompanhe o que muda na história','Follow what changes in the story','Sigue lo que cambia en la historia'],
    ['Primeiro descubra o que os personagens querem. Depois procure o acontecimento que muda o plano. Esse fio ajuda a ligar as frases sem traduzir palavra por palavra.','First find out what the characters want. Then look for the event that changes their plan. This connects the sentences without translating word by word.','Primero descubre qué quieren los personajes. Después busca el hecho que cambia su plan. Así conectarás las oraciones sin traducir palabra por palabra.'],
    ['Ouça uma vez para acompanhar a ação. Na segunda leitura, use a tradução nos pontos em que perdeu o fio e tente recontar o final com suas palavras.','Listen once to follow the action. On the second read, use the translation where you lost track, then retell the ending in your own words.','Escucha una vez para seguir la acción. En la segunda lectura, usa la traducción donde te hayas perdido e intenta contar el final con tus palabras.']
  ]
};
function lessonStudyBadge(key){
  return '<span class="lesson-preview-icon lesson-study-icon lesson-study-icon--'+key+'" aria-hidden="true">'+
    routeIcon(lessonPanels[key][0])+'</span>';
}
function lessonOrientation(key){
  const info=lessonOrientations[key];
  if(!info)return '';
  const badge=['lexicon','grammar'].includes(key)?lessonStudyBadge(key):'';
  return '<div class="lesson-orientation"><h2'+(badge?' class="lesson-study-heading"':'')+'>'+
    badge+clean(routeLabel(...info[0]))+'</h2>'+
    '<div class="lesson-orientation-copy"><p>'+clean(routeLabel(...info[1]))+'</p><p>'+clean(routeLabel(...info[2]))+'</p></div></div>';
}
function lessonPanel(key,preview,content,{extraClass='',id='lesson-panel-'+key,used}={}){
  const [mark,...label]=lessonPanels[key];
  const index=Object.keys(lessonPanels).indexOf(key);
  const topicPreview=['lexicon','grammar'].includes(key);
  const photo=topicPreview&&!mangaPilot()?null:photoForMoment(lessonVisualTheme(),index,'preview','',used);
  const image=photo?.manga?mangaArtwork(photo.n,'thumb',index):(topicPreview||!photo)?lessonStudyBadge(key):'<img class="lesson-preview-photo" src="'+clean(photo.file)+'" alt="" width="'+photo.width+'" height="'+photo.height+'" loading="lazy" decoding="async">';
  return '<details id="'+id+'" class="lesson-disclosure '+extraClass+'" data-lesson-panel="'+key+'"><summary>'+
    image+'<span class="lesson-preview-text"><strong>'+(topicPreview?'':routeIcon(mark))+clean(routeLabel(...label))+'</strong>'+
    '<span>'+preview+'</span></span>'+lessonPreviewActions(routeLabel(...label))+'</summary>'+
    '<div class="lesson-disclosure-content">'+lessonFocusToolbar()+lessonOrientation(key)+content+'</div></details>';
}
function openLessonSection(key){
  const target=document.querySelector('#lesson [data-lesson-panel="'+key+'"]');
  if(!target)return;
  if(focusedLessonPanel&&focusedLessonPanel.panel!==target)closeLessonFocus(false);
  target.open=true;
  target.querySelector('summary').focus({preventScroll:true});
  target.scrollIntoView?.({block:'start'});
}
function applyLessonRoute(route){
  if(!route)return false;
  const courseChanged=route.language!==lang;
  changeCourse(route.language);
  if(route.companion){
    support=route.companion;
    write('support-language',support);
  }
  level=route.level;courseLevels[lang]=level;
  write('level',level);write('course-levels',courseLevels);
  if(route.unit===null){
    unit=selectedUnit();

  }else{
    setUnit(route.unit);
    resetExercises();
  }
  exactWord='';
  drawLanguages();
  drawLesson();
  if(courseChanged||!cache[lang])loadWords();
  if(route.screen==='licao'){
    $('lessonHeading').focus?.({preventScroll:true});
    $('licao').scrollIntoView?.({block:'start'});
  }else{
    $('catalogHeading').focus?.({preventScroll:true});
    $('estudo').scrollIntoView?.({block:'start'});
  }
  return true;
}
