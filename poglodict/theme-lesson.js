const cityEnglish=[
 'Where I live','city','small town',
 'I live in a city near the sea.','My sister lives in a small town.','There’s a park in the city.',
 'Lia lives in a small town near the sea.','She meets Ravi in the city on Saturday.','They walk through a park.',
 'They see a bakery at the end of the street.','They stop there for coffee.',
 'Where do you live, Lia?','I live in a small town near the sea.','Is there a park in your town?',
 'Yes. There’s a park near the station.','Can we meet at the park?','Sure. We can get coffee after that.'
];
const cityPortuguese=[
 'Onde eu moro','cidade','cidade pequena',
 'Moro em uma cidade perto do mar.','Minha irmã mora em uma cidade pequena.','Tem um parque na cidade.',
 'Lia mora em uma cidade pequena perto do mar.','Ela encontra Ravi na cidade no sábado.','Eles passam por um parque.',
 'Eles veem uma padaria no fim da rua.','Param lá para tomar café.',
 'Onde você mora, Lia?','Moro em uma cidade pequena perto do mar.','Tem um parque na sua cidade?',
 'Tem, sim. Fica perto da estação.','Podemos nos encontrar no parque?','Claro. Depois podemos tomar um café.'
];
function activeScene(index,lesson){
  const authored=lang==='eng'&&level===0&&englishBeginnerScenes[index];
  if(authored)return {key:authored.key,source:authored.eng,translation:authored.pt,authored:true};
  const candidate=themes.findIndex(theme=>theme[0]===lesson.theme);
  const key=lang==='eng'&&level===0&&(index===11||lesson.row[0]==='city')?2:candidate<0?7:candidate;
  const city=lang==='eng'&&level===0&&key===2;
  const selected=lang==='por'?'pt':lang;
  const reference=lang==='por'?supportLocale():'pt';
  return {key,city,source:city?cityEnglish:themeScenes[selected][key],
    translation:city?cityPortuguese:themeScenes[reference][key]};
}
function sceneItems(language){
  const native=themeScenes[language==='por'?'pt':language];
  return native.map((source,i)=>{
    const translation=themeScenes[language==='por'?'eng':'pt'][i];
    const other=language==='por'?themeScenes.spa[i]:null;
    const pt=index=>other?bilingual(translation[index],other[index]):translation[index];
    return [1,2].map((j)=>{
      const n=j===1?3:4;
      return {word:source[j],theme:themes[i]?.[0]||'Vocabulário geral',part:j===1?'noun':'phrase',reading:sceneReadings[language]?.[i]?.[j-1]||'',
        definition:pt(j),example:{text:source[n],translation:pt(n)}};
    });
  }).flat();
}
const englishArticleExamples=[
  [
    ['I’d like a coffee, please.','Eu gostaria de um café, por favor.'],
    ['I need a cup for my coffee.','Preciso de um copo para o meu café.'],
    ['Can I have an iced coffee?','Posso pedir um café gelado?'],
    ['She ordered a coffee and an orange juice.','Ela pediu um café e um suco de laranja.']
  ],
  [
    ['I need a ticket to the next town.','Preciso de uma passagem para a cidade vizinha.'],
    ['I bought a round-trip ticket.','Comprei uma passagem de ida e volta.'],
    ['Can I buy an extra ticket for my friend?','Posso comprar uma passagem a mais para meu amigo?'],
    ['Is there an early train? I need a ticket for it.','Tem um trem cedo? Preciso de uma passagem para ele.']
  ],
  [
    ['It’s a city near the sea.','É uma cidade perto do mar.'],
    ['She lives in a small town.','Ela mora em uma cidade pequena.'],
    ['There’s an old park in the city.','Tem um parque antigo na cidade.'],
    ['Is there an airport near the small town?','Tem um aeroporto perto da cidade pequena?']
  ],
  [
    ['I’m having dinner with a friend.','Vou jantar com uma amiga.'],
    ['We need a table for two.','Precisamos de uma mesa para duas pessoas.'],
    ['I sent a friend an invitation.','Mandei um convite para uma amiga.'],
    ['Is an early dinner okay for your friend?','Tudo bem para sua amiga jantar cedo?']
  ],
  [
    ['I brought a notebook to class.','Trouxe um caderno para a aula.'],
    ['Can we share a notebook?','Podemos usar um caderno juntas?'],
    ['Write an answer in your notebook.','Escreva uma resposta no caderno.'],
    ['I need a pencil and an eraser for my notebook.','Preciso de um lápis e uma borracha para o meu caderno.']
  ],
  [
    ['There’s a park near here.','Tem um parque perto daqui.'],
    ['Let’s take a walk in the park.','Vamos dar uma volta no parque.'],
    ['There’s an old tree in the park.','Tem uma árvore antiga no parque.'],
    ['Bring an umbrella for your walk in the park.','Leve um guarda-chuva para sua caminhada no parque.']
  ],
  [
    ['I need to make an appointment.','Preciso marcar uma consulta.'],
    ['I have an appointment at three.','Tenho uma consulta às três.'],
    ['Can I book a morning appointment?','Posso marcar uma consulta de manhã?'],
    ['There’s an opening at four if you need an appointment.','Tem um horário livre às quatro se você precisar de uma consulta.']
  ],
  [
    ['Can I leave a message?','Posso deixar um recado?'],
    ['There’s a message for Ravi.','Tem um recado para o Ravi.'],
    ['Can I send an urgent message?','Posso mandar um recado urgente?'],
    ['Please leave a message with an address.','Por favor, deixe um recado com um endereço.']
  ]
];
function buildThematicLesson(index,item){
  const {key,city,source,translation,authored}=activeScene(index,item);
  const [title,word,expression]=source;
  const audio={};
  const localized=lang==='por';
  const [lessonTitle]=localized||authored?translation:themeScenes.pt[key];
  const readings=sceneReadings[lang]?.[key];
  const pronunciation=i=>readings?.[i]?'<span class="meta"> '+clean(readings[i])+'</span>':'';
  const [wordPt,expressionPt]=translation.slice(1,3);
  const usedPhotos=new Set();
  const vocabCover=lessonSectionPhoto(lessonVisualTheme(),'section',usedPhotos);
  const grammarCover=lessonSectionPhoto(lessonVisualTheme(),'grammar',usedPhotos);
  const focus=assignedLessonWord(item,word);
  const focusBlock=focus?renderAssignedLessonWord(focus,usedPhotos):'';
  const vocab='<article class="lesson-card">'+vocabCover+'<span class="tag">'+clean(ui(themes[key]?.[0]||'Vocabulário geral'))+'</span><h3>'+
    clean(city?cityPortuguese[0]:lessonTitle)+'</h3>'+focusBlock+
    (focus?'<h4>'+routeLabel(authored?'Palavras da cena':'Palavras da cena de revisão',authored?'Scene words':'Review scene words',authored?'Palabras de la escena':'Palabras de la escena de repaso')+'</h4>':'')+'<dl class="scene-lexicon"><dt>'+nativeText(word)+pronunciation(0)+lessonVocabularyAudio(word)+'</dt><dd>'+clean(wordPt)+'</dd><dt>'+nativeText(expression)+pronunciation(1)+lessonVocabularyAudio(expression)+'</dt><dd>'+clean(expressionPt)+'</dd></dl><div class="lesson-example-grid">'+
    [3,4,5].map((slot,i)=>renderExample({text:source[slot],translation:translation[slot]},i+1,undefined,usedPhotos)).join('')+'</div></article>';
  const arc=Math.floor(index/lessonsPerArc);
  const guided=arc%2===0;
  let grammar;
  const topic=guided?grammarPractice[lang][level]:study[lang][level].slice(4,8);
  const grammarTitle=lang==='eng'&&level===0&&guided?'Artigo indefinido · a/an':topic[0];
  if(lang==='eng'&&level===0&&guided){
    grammar=renderGrammarRule(grammarTitle,
      'Use a ou an para mencionar uma coisa contável no singular pela primeira vez, como uma passagem ou uma consulta. Para escolher, escute o som que vem logo depois do artigo.',
      'Use a antes de som de consoante e an antes de som de vogal. Se houver um adjetivo, escute o adjetivo: a park, mas an old park. Em an hour, o h é mudo. Em a university, o primeiro som é parecido com o y de yes.',
      englishArticleExamples[key],audio,usedPhotos,englishArticleCheck());
  }else{
    grammar=grammarPanel(lang,level,guided,topic,audio,usedPhotos);
  }
  const card='<article class="lesson-card">'+grammarCover+'<span class="tag">'+clean(ui('Gramática'))+' · '+levels[level]+'</span>'+grammar+'</article>';
  const [headSample,phraseSample]=source.slice(3,5);
  const vocabulary={word,expression,sceneSource:source,sceneTranslation:translation,extension:item};
  return {cards:[vocab,card],cardPhotos:usedPhotos,grammarTitle,focus,reviewScene:!authored,cue:ui('Praticar compreensão'),clue:headSample,answer:translation[3],audio,vocabulary,
    tasks:{word,phrase:expression,sentence:headSample,translation:translation[3],alternative:phraseSample}};
}
function addSceneWords(language,base){
  const words=new Map(base);
  const make=(entry,overrides={})=>{
    const {word,definition,part,theme,example,reading}=entry;
    return {theme,row:[word,definition,part,part==='phrase'?1:0,example.text,'','',example.translation,reading||'','',definition,0,'','','','lesson'],
      second:null,...overrides};
  };
  for(const entry of sceneItems(language)){
    if(!words.has(entry.word))words.set(entry.word,make(entry));
  }
  if(language==='eng'){
    for(const [i,word] of cityEnglish.slice(1,3).entries()){
      const examples=i===0?[[3,3],[5,5],[7,7]]:[[4,4],[6,6],[12,12]];
      const [one,two,three]=examples.map(([native,pt])=>({text:cityEnglish[native],translation:cityPortuguese[pt]}));
      const previous=words.get(word);
      words.set(word,make({word,definition:cityPortuguese[1+i],part:i?'phrase':'noun',theme:'Casa e cidade',example:one},
        {second:two,third:three,...(previous?.row[8]?{reading:previous.row[8]}:{})}));
    }
  }
  return words;
}
