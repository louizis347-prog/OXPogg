const pages=['estudo','revisao','dicionario','favoritos','metodo','fontes','teste'];
let screen='estudo';
const catalogForms={};
function screenFromHash(){
  const lessonRoute=parseLessonRoute();
  if(lessonRoute)return lessonRoute.screen;
  const route=location.hash.slice(1);
  return route.startsWith('verbete/')?'dicionario':pages.includes(route)?route:'estudo';
}
function switchScreen(){
  const previous=screen;
  screen=screenFromHash();
  if(previous==='teste'&&screen!=='teste')window.speechSynthesis?.cancel();
  const titles={dicionario:ui('Dicionário'),favoritos:ui('Favoritos'),revisao:ui('Revisar palavras'),metodo:'Método',fontes:'Fontes e licenças',teste:'Teste de nível de inglês'};
  if(Object.hasOwn(titles,screen))document.title=titles[screen]+' · Pogolo Dict';
  for(const element of document.querySelectorAll('[data-screen]')){
    element.hidden=element.dataset.screen!==screen||element.id==='writing'&&!['jpn','cmn'].includes(lang);
  }
  for(const a of document.querySelectorAll('header nav a')){
    if(a.getAttribute('href')==='#'+screen||screen==='licao'&&a.id==='lessonsNav')a.setAttribute('aria-current','page');
    else a.removeAttribute('aria-current');
  }
  if(screen==='favoritos')renderFavorites();
  if(screen==='revisao')renderReview();
  if(previous!==screen&&location.hash==='#'+screen)$(screen)?.scrollIntoView?.();
}
function exampleAudio(text){
  if(screen==='licao')text=lessonLevelText(text);
  return '<span class="audio-pair"><button type="button" data-inline-say="'+clean(text)+'">'+ui('Ouvir')+'</button>'+
    '<button type="button" data-inline-say="'+clean(text)+'" data-rate=".65">'+routeLabel('Lento','Slow','Lento')+'</button></span>';
}
function recordControls(text,{withModel=true}={}){
  return '<details class="voice-panel"><summary>'+routeLabel('Gravar minha fala','Record my speech','Grabar mi voz')+'</summary><p>'+
    routeLabel('A gravação fica nesta página. Ouça o que você disse antes de conferir o modelo.','The recording stays on this page. Listen to what you said before checking the model.','La grabación se queda en esta página. Escucha lo que dijiste antes de comprobar el modelo.')+'</p>'+
    (withModel?exampleAudio(text):'')+'<button type="button" data-record>'+routeLabel('Gravar minha voz','Record my voice','Grabar mi voz')+'</button><audio controls hidden></audio><p class="voice-status" role="status"></p></details>';
}
const exerciseModes=[
  ['gap','Lacuna','Fill the gap','Completa la frase'],
  ['choice','Sentido','Meaning','Significado'],
  ['order','Ordem','Word order','Orden'],
  ['dictation','Ditado','Dictation','Dictado'],
  ['dialogue','Diálogo','Dialogue','Diálogo'],
  ['voice','Fala','Speaking','Habla'],
  ['rewrite','Escrita','Writing','Escritura']
];
const exercisesPerMode=2;
let exerciseKind='gap';
let exerciseResults={};
let exerciseRounds={};
function resetExercises(){exerciseKind='gap';exerciseResults={};exerciseRounds={};}
function exerciseRound(){return exerciseRounds[exerciseKind]??0;}
function exerciseAttempt(kind=exerciseKind,round=exerciseRound()){
  return exerciseResults[kind+'-'+round]??={sequence:[],draft:'',result:'',attempted:false,reveal:false,done:false};
}
function exerciseSample(lesson,kind=exerciseKind,round=exerciseRound()){
  const {vocabulary,practiceContent}=lesson;
  const source=lesson.tasks||{
    word:vocabulary.word,sentence:vocabulary.wordExample?.text||lesson.clue,
    translation:vocabulary.wordExample?.pt||lesson.answer
  };
  const primary={word:lessonLevelText(source.word),sentence:lessonLevelText(source.sentence),translation:source.translation};
  const {reading,dialogue}=practiceContent;
  const expression=vocabulary.expressionExample||{text:source.alternative,pt:vocabulary.sceneTranslation?.[4]};
  const phrase={...expression,word:vocabulary.expression};
  const preferred={
    gap:[phrase,reading[1]],choice:[reading[2],dialogue[1]],order:[phrase,dialogue[2]],
    dictation:[dialogue[1],dialogue[3]],voice:[dialogue[2],dialogue[5]],rewrite:[reading[1],reading[4]]
  };
  const additional=assignedPracticeExample(lesson.focus);
  const candidates=[...(preferred[kind]||[]),phrase,...reading,...dialogue];
  const preferredPractice=['dictation','voice','rewrite'].includes(kind);
  const pack=line=>({word:lessonLevelText(line.word||source.word),sentence:lessonLevelText(line.text),translation:line.pt});
  const available=candidates.filter(line=>line?.text&&line.pt).map(pack);
  const first=preferredPractice?available[0]||primary:primary;
  const additionalExamples=additional&&kind!=='dialogue'?[pack(additional)]:[];
  const second=[...additionalExamples,...available].find(row=>row.sentence!==first.sentence&&
    (kind!=='choice'||row.translation!==first.translation));
  const model=round&&second?second:first;
  const wordPattern=model.word.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  const unspaced=['jpn','cmn'].includes(lang);
  const boundary=unspaced?wordPattern:'(?<![\\p{L}\\p{N}])'+wordPattern+'(?![\\p{L}\\p{N}])';
  const pattern=new RegExp(boundary,'iu');
  const tokens=unspaced
    ? (typeof Intl.Segmenter==='function'
      ? [...new Intl.Segmenter(languages[lang][2],{granularity:'word'}).segment(model.sentence)].map(s=>s.segment)
      : Array.from(model.sentence))
    : model.sentence.split(/\s+/);
  const match=model.sentence.match(pattern);
  const fallback=kind==='gap'&&!match?
    tokens.map(token=>token.match(/[\p{L}\p{M}]+/u)?.[0]).find(token=>token&&(token.length>=2||unspaced)):'';
  return {...model,tokens,joiner:unspaced?'':' ',
    gap:match?model.sentence.replace(pattern,'_____'):fallback?model.sentence.replace(fallback,'_____'):'',
    target:match?.[0]||fallback||model.sentence};
}
function exerciseDialogue(lesson,round=exerciseRound()){
  const lines=lesson.practiceContent.dialogue;
  const indices=[0,2,4].filter(index=>lines[index+1]&&lines.some((line,i)=>i!==index&&i!==index+1&&line.text!==lines[index].text&&line.text!==lines[index+1].text));
  const at=indices[(unit+level+round)%indices.length]??0;
  const expected=lines[at+1];
  const alternatives=lines.filter((_,i)=>i!==at&&i!==at+1).map(line=>line.text);
  const options=[...new Set(alternatives)].filter(text=>text!==expected.text&&text!==lines[at].text).slice(0,2);
  options.splice((unit+level)%(options.length+1),0,expected.text);
  return {cue:lines[at],expected,options};
}
function exerciseSupportText(value){return '<span lang="'+supportTag()+'">'+clean(value)+'</span>';}
function exerciseButton(label,key){return '<button type="button" data-exercise-action="'+key+'">'+clean(label)+'</button>';}
function exerciseOptions(options,key){
  return '<div class="exercise-choice">'+options.map(value=>'<button type="button" data-'+key+'="'+clean(value)+
    '" aria-pressed="'+(exerciseAttempt().draft===value)+'">'+(key==='choice'?exerciseSupportText(value):nativeText(value))+'</button>').join('')+'</div>';
}
function exerciseWriting(data,round){
  const tasks=[
    ['Troque um lugar, objeto ou pessoa e leia a nova frase em voz alta.','Change a place, object or person, then read your sentence aloud.','Cambia un lugar, un objeto o una persona y lee la frase en voz alta.'],
    ['Mude a situação para amanhã e acrescente um detalhe de horário.','Move the situation to tomorrow and add a time detail.','Traslada la situación a mañana y añade un detalle de horario.'],
    ['Reescreva a frase do ponto de vista de outra pessoa e acrescente um motivo.','Rewrite the sentence from someone else’s perspective and add a reason.','Reescribe la frase desde el punto de vista de otra persona y añade un motivo.'],
    ['Adapte a frase para uma mensagem a alguém que não conhece a situação. Inclua o contexto necessário.','Adapt the sentence for a message to someone who doesn’t know the situation. Add the context they need.','Adapta la frase para un mensaje a alguien que desconoce la situación. Añade el contexto necesario.'],
    ['Escreva duas versões, uma para um amigo e outra para uma situação formal. Compare o tom das duas.','Write two versions, for a friend and for a formal setting. Compare their tone.','Escribe dos versiones, para un amigo y para una situación formal. Compara el tono.'],
    ['Reformule a frase para destacar outra informação. Em seguida, explique em uma frase como a ênfase mudou.','Rewrite the sentence to highlight a different detail. Then explain in one sentence how the emphasis changed.','Reformula la frase para destacar otro detalle. Después explica en una frase cómo cambió el énfasis.']
  ];
  const production=level<2?
    routeLabel('Escreva uma fala ligada à situação abaixo. Acrescente um horário, um lugar ou um nome.','Write a line for the situation below. Add a time, place or name.','Escribe una intervención para la situación indicada. Añade una hora, un lugar o un nombre.'):
    routeLabel('Escreva duas frases para continuar a situação. Na segunda, justifique sua decisão ou faça uma pergunta de seguimento.','Write two sentences to continue the situation. In the second, explain your decision or ask a follow-up question.','Escribe dos frases para continuar la situación. En la segunda, justifica tu decisión o haz una pregunta de seguimiento.');
  const cue=round?'<p class="exercise-prompt">'+exerciseSupportText(data.translation)+'</p>':
    '<div class="exercise-prompt">'+nativeText(data.sentence,'p')+exampleAudio(data.sentence)+'</div>';
  return '<p>'+(round?production:routeLabel(...tasks[level]))+'</p>'+cue+
    '<label for="exerciseDraft">'+routeLabel('Escreva sua versão','Write your version','Escribe tu versión')+'</label>'+
    '<textarea id="exerciseDraft" rows="3" dir="auto" lang="'+languages[lang][2]+'">'+clean(exerciseAttempt().draft)+'</textarea>'+
    '<details><summary>'+routeLabel('Revisar minha resposta','Review my answer','Revisar mi respuesta')+'</summary><ul>'+
    [routeLabel('Mantive a ideia que queria comunicar?','Did I keep the meaning I wanted to convey?','¿Mantuve la idea que quería comunicar?'),
      routeLabel('Ajustei as palavras que precisavam mudar?','Did I adjust the words that needed to change?','¿Ajusté las palabras que debían cambiar?'),
      routeLabel('Minha versão faz sentido quando leio em voz alta?','Does my version make sense when I read it aloud?','¿Mi versión tiene sentido al leerla en voz alta?')]
      .map(text=>'<li>'+clean(text)+'</li>').join('')+'</ul></details>'+
    exerciseButton(routeLabel('Marcar como revisada','Mark as reviewed','Marcar como revisada'),'review');
}
const exerciseInstructions={
  gap:['Use o que vem antes e depois da lacuna para decidir que palavra ou expressão encaixa. Depois leia a frase inteira para verificar o sentido.','Use the words before and after the blank to choose what fits. Read the whole sentence to check the meaning.','Usa las palabras antes y después del hueco para decidir qué encaja. Lee la frase entera para comprobar el sentido.'],
  choice:['Identifique quem está falando, o que aconteceu e qual detalhe muda o sentido. Compare essas informações antes de escolher.','Identify who is speaking, what happened and which detail changes the meaning. Compare those details before choosing.','Identifica quién habla, qué pasó y qué detalle cambia el sentido. Compara esos datos antes de elegir.'],
  order:['Procure blocos que costumam andar juntos, como artigo e substantivo. Monte a ideia principal e encaixe os detalhes de tempo ou lugar.','Look for pieces that belong together, such as an article and noun. Build the main idea, then add time or place details.','Busca bloques que van juntos, como artículo y sustantivo. Arma la idea principal y añade los detalles de tiempo o lugar.'],
  dictation:['Na primeira escuta, capte a ideia geral. Na segunda, escreva o que ouviu. Use o áudio lento se precisar separar os sons.','On the first listen, catch the main idea. On the second, write what you hear. Use slow audio to separate the sounds if needed.','Primero capta la idea general. En la segunda escucha, escribe lo que oyes. Usa el audio lento si necesitas distinguir los sonidos.'],
  dialogue:['Observe a intenção da fala: perguntar, confirmar ou combinar algo. A melhor resposta retoma essa intenção e dá sequência à cena.','Notice the purpose of the line: asking, confirming or making a plan. The best reply addresses that purpose and moves the scene forward.','Observa la intención: preguntar, confirmar o acordar algo. La mejor respuesta retoma esa intención y hace avanzar la escena.'],
  voice:['Na primeira rodada, imite o ritmo que você ouve. Na segunda, formule a frase a partir da ideia escrita. Você pode se gravar para comparar.','In the first round, imitate the rhythm you hear. In the second, speak from the written cue. Record yourself if you want to compare.','En la primera ronda, imita el ritmo que oyes. En la segunda, formula la frase a partir de la pista escrita. Puedes grabarte para comparar.'],
  rewrite:['Primeiro, adapte uma frase. Depois, escreva a partir de uma situação. Releia conferindo se sua versão comunica o que você queria dizer.','First adapt a sentence. Then write from a situation. Reread your version to check that it conveys what you intended.','Primero adapta una frase. Luego escribe a partir de una situación. Relee tu versión para comprobar si comunica lo que querías decir.']
};
function exerciseNavigation(){
  const counts=Object.fromEntries(exerciseModes.map(([kind])=>[kind,[0,1].filter(round=>exerciseResults[kind+'-'+round]?.done).length]));
  const total=Object.values(counts).reduce((sum,count)=>sum+count,0);
  const max=exerciseModes.length*exercisesPerMode;
  const progress='<label class="exercise-progress">'+routeLabel(total+' de '+max+' concluídos',total+' of '+max+' complete',total+' de '+max+' completados')+
    '<progress max="'+max+'" value="'+total+'"></progress></label>';
  const tabs='<div class="controls exercise-tabs">'+exerciseModes.map(([kind,...label])=>
    '<button type="button" data-exercise="'+kind+'" aria-pressed="'+(exerciseKind===kind)+'">'+clean(routeLabel(...label))+
    ' <span class="exercise-count">'+counts[kind]+'/'+exercisesPerMode+'</span></button>').join('')+'</div>';
  const rounds='<div class="controls exercise-rounds">'+[0,1].map(round=>
    '<button type="button" data-exercise-round="'+round+'" aria-pressed="'+(round===exerciseRound())+'">'+
    routeLabel('Exercício ','Exercise ','Ejercicio ')+(round+1)+(exerciseResults[exerciseKind+'-'+round]?.done?' '+icon('check'):'')+'</button>').join('')+'</div>';
  return {progress,tabs,rounds};
}
function exercisePane(lesson){
  const round=exerciseRound();
  const data=exerciseSample(lesson);
  const state=exerciseAttempt();
  const navigation=exerciseNavigation();
  const input=(label,clue='')=>'<form id="exerciseAnswer"><label for="exerciseInput">'+label+'</label>'+
    (clue?'<p>'+clue+'</p>':'')+'<input id="exerciseInput" lang="'+languages[lang][2]+'" dir="auto" required autocomplete="off" value="'+clean(state.draft)+'"><button>'+routeLabel('Conferir','Check','Comprobar')+'</button></form>';
  let body, hint, answer=data.sentence, translation=data.translation;
  if(exerciseKind==='gap'){
    body=data.gap?input(routeLabel('Complete com a palavra da lição','Fill in the lesson word','Completa con la palabra de la lección'),nativeText(data.gap)+'<br>'+exerciseSupportText(data.translation)):
      input(routeLabel('Reconstrua a frase da lição','Recreate the lesson sentence','Reconstruye la frase de la lección'),exerciseSupportText(data.translation));
    hint=routeLabel('Compare a tradução com o texto e procure a ideia que ainda está faltando.','Compare the translation with the text and look for the idea that is still missing.','Compara la traducción con el texto y busca la idea que todavía falta.');
  }else if(exerciseKind==='choice'){
    const correct=data.translation;
    const candidates=[...lesson.practiceContent.reading,...lesson.practiceContent.dialogue].map(line=>line.pt)
      .concat(themeScenes[lang==='por'?supportLocale():'pt'].map(row=>row[3]));
    const options=[...new Set(candidates)].filter(value=>value&&value!==correct).slice(0,2);
    options.splice((unit+level)%3,0,correct);
    const cue=round?
      routeLabel('Ouça a frase e escolha a opção que transmite o sentido.','Listen to the sentence and choose the option that conveys its meaning.','Escucha la frase y elige la opción que transmite su sentido.'):
      routeLabel('Qual opção transmite o sentido da frase?','Which option conveys the meaning?','¿Qué opción transmite el sentido?');
    body='<p>'+cue+'</p>'+(round?'':nativeText(data.sentence,'p'))+exampleAudio(data.sentence)+exerciseOptions(options,'choice');
    hint=routeLabel('Localize a palavra da lição e compare quem faz o quê em cada opção.','Find the lesson word and compare who does what in each option.','Localiza la palabra y compara quién hace qué en cada opción.');
  }else if(exerciseKind==='order'){
    const choices=data.tokens.map((_,i)=>i);
    let seed=unit+101*(level+1)+43*round;
    for(let i=choices.length-1;i>0;i--){
      seed=(1664525*seed+1013904223)>>>0;
      const j=seed%(i+1);
      [choices[i],choices[j]]=[choices[j],choices[i]];
    }
    if(choices.length>1&&choices.every((index,i)=>index===i))choices.push(choices.shift());
    const parts=state.sequence.map(i=>data.tokens[i]).join(data.joiner);
    body='<p>'+routeLabel('Toque nos blocos para montar a frase. Depois confira a ordem.','Tap the pieces to build the sentence, then check their order.','Toca los bloques para formar la frase y comprueba el orden.')+'</p>'+
      '<p>'+exerciseSupportText(data.translation)+'</p><p class="order-answer" aria-live="polite">'+(parts?nativeText(parts):routeLabel('Sua frase aparecerá aqui.','Your sentence will appear here.','Tu frase aparecerá aquí.'))+
      '</p><div class="controls">'+choices.filter(i=>!state.sequence.includes(i)).map(i=>'<button type="button" data-order="'+i+'">'+nativeText(data.tokens[i])+'</button>').join('')+
      '</div><div class="controls"><button type="button" data-order-action="undo">'+routeLabel('Desfazer','Undo','Deshacer')+'</button>'+
      '<button type="button" data-order-action="check">'+routeLabel('Conferir','Check','Comprobar')+'</button></div>';
    hint=routeLabel('O primeiro bloco é','The first piece is','El primer bloque es')+' '+nativeText(data.tokens[0]);
  }else if(exerciseKind==='dictation'){
    body='<p>'+routeLabel('Ouça a frase inteira. Se precisar, use o áudio lento antes de escrever.','Listen to the whole sentence. Use slow audio if you need it before writing.','Escucha la frase completa. Si lo necesitas, usa el audio lento antes de escribir.')+
      '</p>'+exampleAudio(data.sentence)+input(routeLabel('Escreva o que ouviu','Write what you heard','Escribe lo que oíste'));
    hint=routeLabel('Sentido da frase','Meaning of the sentence','Sentido de la frase')+' · '+exerciseSupportText(data.translation);
  }else if(exerciseKind==='dialogue'){
    const {cue,expected,options}=exerciseDialogue(lesson);
    answer=expected.text;
    translation=expected.pt;
    body='<p>'+routeLabel('Ouça a fala. Escolha a resposta que vem em seguida no diálogo da lição.','Listen to the line. Choose the reply that comes next in the lesson dialogue.','Escucha la intervención. Elige la respuesta que sigue en el diálogo de la lección.')+
      '</p>'+nativeText(cue.text,'p')+exampleAudio(cue.text)+exerciseOptions(options,'reply');
    hint=exerciseSupportText(cue.pt);
  }else if(exerciseKind==='rewrite'){
    body=exerciseWriting(data,round);
  }else{
    const available=window.SpeechRecognition||window.webkitSpeechRecognition;
    const instruction=round?
      routeLabel('Diga a frase a partir da ideia abaixo. Se puder, grave sua fala antes de conferir a frase da lição.','Say the sentence from the idea below. If you can, record yourself before checking the lesson sentence.','Di la frase a partir de la idea de abajo. Si puedes, grábate antes de comprobar la frase de la lección.'):
      routeLabel('Ouça o modelo sem ler. Repita em voz alta, imitando as pausas e o ritmo.','Listen without reading. Repeat aloud, imitating the pauses and rhythm.','Escucha sin leer. Repite en voz alta, imitando las pausas y el ritmo.');
    body='<p>'+instruction+'</p>'+(round?'<p class="exercise-prompt">'+exerciseSupportText(data.translation)+'</p>':exampleAudio(data.sentence))+
      (available?'<button type="button" id="recognizeSpeech">'+routeLabel('Transcrever minha fala','Transcribe my speech','Transcribir mi voz')+'</button>':'')+
      recordControls(data.sentence,{withModel:false})+exerciseButton(routeLabel('Marcar como praticada','Mark as practiced','Marcar como practicada'),'review');
  }
  const explanation={
    gap:data.gap?routeLabel('A palavra que completa a frase é','The missing word is','La palabra que falta es')+' '+nativeText(data.target)+'.':
      routeLabel('Compare a sua reconstrução com a frase da lição, prestando atenção às palavras de ligação.','Compare your reconstruction with the lesson sentence. Look for linking words.','Compara tu reconstrucción con la frase de la lección y fíjate en las palabras de enlace.'),
    choice:routeLabel('Leia a frase e sua tradução juntas. Observe qual informação as duas têm em comum.','Read the sentence and its translation together. Notice what information they share.','Lee la frase junto a su traducción y fíjate en la información que comparten.'),
    order:routeLabel('O modelo começa com','The model begins with','El modelo empieza con')+' '+nativeText(data.tokens[0])+
      '. '+routeLabel('Compare o lugar de cada bloco com a sequência que você montou.','Compare each piece with the sequence you built.','Compara el lugar de cada bloque con la secuencia que formaste.'),
    dictation:routeLabel('Ouça novamente acompanhando o texto. Compare as terminações e os espaços com o que escreveu.','Listen again while reading. Compare word endings and spacing with what you wrote.','Escucha otra vez mientras lees. Compara las terminaciones y los espacios con lo que escribiste.'),
    dialogue:routeLabel('Esta é a próxima fala da cena original. Veja como ela responde ou dá continuidade ao que você ouviu.','This is the next line from the original dialogue. Notice how it answers or follows what you heard.','Esta es la siguiente intervención de la escena original. Observa cómo responde o continúa lo que escuchaste.')
  };
  const labels={
    correct:routeLabel('Correto! Confira o modelo e ouça a frase completa.','Correct! Check the model and listen to the full sentence.','¡Correcto! Mira el modelo y escucha la frase completa.'),
    retry:routeLabel('Ainda não. Compare com a pista e tente outra vez.','Not yet. Use the hint and try again.','Todavía no. Usa la pista y vuelve a intentarlo.'),
    incomplete:routeLabel('Use todos os blocos antes de conferir.','Use every piece before checking.','Usa todos los bloques antes de comprobar.'),
    empty:routeLabel('Escreva sua versão antes de marcar a revisão.','Write your version before marking it reviewed.','Escribe tu versión antes de marcar la revisión.'),
    reviewed:routeLabel('Prática concluída.','Practice complete.','Práctica completada.')
  };
  return '<section id="exercise" class="exercise-panel lesson-card" aria-labelledby="exerciseTitle"><header><div><h3 id="exerciseTitle">'+routeIcon('puzzle')+' '+routeLabel('Prática da lição','Lesson practice','Práctica de la lección')+'</h3><p>'+
    routeLabel('Cada área tem dois exercícios. Comece por qualquer um e tente responder antes de consultar o modelo. Os rascunhos ficam aqui enquanto você alterna entre exercícios.','Each area has two exercises. Start anywhere and try before checking the model. Your drafts stay here as you move between exercises.','Cada área tiene dos ejercicios. Empieza por cualquiera e inténtalo antes de consultar el modelo. Tus borradores se conservan al cambiar de ejercicio.')+
    '</p></div>'+navigation.progress+'</header><div class="exercise-layout">'+navigation.tabs+'<div class="exercise-main">'+
    '<p class="exercise-area-intro">'+routeLabel(...exerciseInstructions[exerciseKind])+'</p>'+navigation.rounds+'<div class="exercise-body">'+body+
    (hint?'<div class="exercise-help"><details><summary>'+routeLabel('Ver pista','Show hint','Ver pista')+'</summary><p>'+hint+'</p></details>'+
      (state.attempted&&!state.reveal?exerciseButton(routeLabel('Ver a resposta','Show answer','Ver respuesta'),'reveal'):'')+'</div>':'')+
    '<p id="exerciseFeedback" data-result="'+state.result+'" role="status">'+clean(labels[state.result]||'')+'</p>'+
    (state.reveal&&exerciseKind!=='rewrite'?'<div class="exercise-model"><strong>'+routeLabel('Modelo da lição','Lesson model','Modelo de la lección')+'</strong>'+
      nativeText(answer,'p')+pinyinLine(answer)+'<p>'+exerciseSupportText(translation)+'</p>'+exampleAudio(answer)+(explanation[exerciseKind]?'<p class="exercise-explanation">'+explanation[exerciseKind]+'</p>':'')+'</div>':'')+
    (state.done&&round===0?'<button type="button" class="exercise-next" data-exercise-round="1">'+
      routeLabel('Ir para o exercício 2','Go to exercise 2','Ir al ejercicio 2')+'</button>':'')+'</div></div></div></section>';
}
function assessExercise(response,expected){
  const compare=text=>{
    const plain=normalize(text).replace(/'/g,'').replace(/[^\p{L}\p{N}]+/gu,' ').trim();
    return ['jpn','cmn'].includes(lang)?plain.replace(/ /g,''):plain;
  };
  return Boolean(compare(response))&&compare(response)===compare(expected);
}
function updateExercise(){
  const old=$('exercise');
  if(old)old.outerHTML=exercisePane(currentLesson);
}
function checkExercise(response,expected){
  const state=exerciseAttempt();
  state.draft=response;
  state.attempted=Boolean(response.trim());
  const right=assessExercise(response,expected);
  state.result=right?'correct':'retry';
  if(right){state.reveal=true;state.done=true;}
  updateExercise();
}
let recording=null;
let recordingStream=null;
let activeRecognition=null;
function handleLessonTools(event){
  const button=event.target.closest('button');
  if(!button)return false;
  if(button.dataset.inlineSay!==undefined){
    if(!speech(button.dataset.inlineSay,Number(button.dataset.rate)||.88)){
      const status=$('lessonStatus')||$('resultCount');
      if(status)status.textContent='Voz indisponível neste navegador.';
    }
    return true;
  }
  if(button.dataset.record!==undefined){
    const area=button.closest('.voice-panel'),status=area.querySelector('.voice-status');
    if(recording?.state==='recording'){
      recording.stop();
      return true;
    }
    if(typeof navigator==='undefined'||!navigator.mediaDevices?.getUserMedia||!window.MediaRecorder){status.textContent='Gravação indisponível neste navegador.';return true;}
    button.disabled=true;
    navigator.mediaDevices.getUserMedia({audio:true}).then(stream=>{
      if(!area.isConnected){stream.getTracks().forEach(track=>track.stop());return;}
      recordingStream=stream;
      const recorder=new MediaRecorder(stream),chunks=[];
      recording=recorder;
      recorder.ondataavailable=e=>{if(e.data.size)chunks.push(e.data);};
      recorder.onstop=()=>{
        stream.getTracks().forEach(track=>track.stop());
        recording=null;recordingStream=null;
        const audio=area.querySelector('audio');
        if(audio.src)URL.revokeObjectURL(audio.src);
        if(chunks.length){audio.src=URL.createObjectURL(new Blob(chunks,{type:recorder.mimeType}));audio.hidden=false;}
        button.textContent='Gravar minha voz';
        status.textContent=chunks.length?'Gravação pronta para comparar.':'Não houve áudio para reproduzir.';
      };
      recorder.onerror=()=>{
        stream.getTracks().forEach(track=>track.stop());
        recording=null;recordingStream=null;
        button.textContent='Gravar minha voz';
        status.textContent='Não foi possível gravar.';
      };
      recorder.start();button.textContent='Parar gravação';status.textContent='Gravando…';
    }).catch(()=>{recordingStream?.getTracks().forEach(track=>track.stop());recordingStream=null;recording=null;status.textContent='Microfone indisponível ou sem permissão.';}).finally(()=>{button.disabled=false;});
    return true;
  }
  if(button.dataset.exercise||button.dataset.exerciseRound!==undefined){
    stopVoiceTools();
    stopLessonPlayback();
    window.speechSynthesis?.cancel();
    if(button.dataset.exercise)exerciseKind=button.dataset.exercise;
    else exerciseRounds[exerciseKind]=Number(button.dataset.exerciseRound);
    updateExercise();
    const selector=button.dataset.exercise?'.exercise-tabs':'.exercise-rounds';
    $('exercise').querySelector(selector+' [aria-pressed="true"]')?.focus();
    return true;
  }
  if(!currentLesson||!$('exercise'))return false;
  const state=exerciseAttempt();
  if(button.dataset.exerciseAction==='reveal'){
    if(!state.attempted)return true;
    state.reveal=true;
    updateExercise();
    $('exercise').querySelector('.exercise-model button')?.focus();
    return true;
  }
  if(button.dataset.exerciseAction==='review'){
    const ready=exerciseKind!=='rewrite'||Boolean(state.draft.trim());
    state.result=ready?'reviewed':'empty';
    if(ready){state.done=true;state.reveal=exerciseKind==='voice';}
    // Keep the student's recording and draft mounted. Refresh just the feedback and navigation.
    const refreshed=document.createElement('div');
    refreshed.innerHTML=exercisePane(currentLesson);
    for(const selector of ['#exerciseFeedback','.exercise-progress','.exercise-tabs','.exercise-rounds']){
      $('exercise').querySelector(selector).replaceWith(refreshed.querySelector(selector));
    }
    for(const selector of ['.exercise-model','.exercise-next']){
      $('exercise').querySelector(selector)?.remove();
      const element=refreshed.querySelector(selector);
      if(element)$('exercise').querySelector('.exercise-body').appendChild(element);
    }
    return true;
  }
  const data=exerciseSample(currentLesson);
  if(button.dataset.choice!==undefined||button.dataset.reply!==undefined){
    const dialogue=button.dataset.reply!==undefined;
    checkExercise(dialogue?button.dataset.reply:button.dataset.choice,dialogue?exerciseDialogue(currentLesson).expected.text:data.translation);
    $('exercise').querySelector('.exercise-choice [aria-pressed="true"]')?.focus();
    return true;
  }
  if(button.dataset.order!==undefined){
    state.sequence.push(Number(button.dataset.order));state.result='';updateExercise();
    ($('exercise').querySelector('[data-order]')||$('exercise').querySelector('[data-order-action="check"]'))?.focus();
    return true;
  }
  if(button.dataset.orderAction==='undo'){
    state.sequence.pop();state.result='';updateExercise();
    $('exercise').querySelector('[data-order-action="undo"]')?.focus();
    return true;
  }
  if(button.dataset.orderAction==='check'){
    if(state.sequence.length!==data.tokens.length){state.result='incomplete';updateExercise();}
    else checkExercise(state.sequence.map(i=>data.tokens[i]).join(data.joiner),data.sentence);
    $('exercise').querySelector('[data-order-action="check"]')?.focus();
    return true;
  }
  if(button.id==='recognizeSpeech'){
    const Speech=window.SpeechRecognition||window.webkitSpeechRecognition;
    if(!Speech||activeRecognition)return true;
    const recognizer=new Speech();activeRecognition=recognizer;recognizer.lang=languages[lang][2];
    const status=$('exerciseFeedback');status.textContent='Ouvindo…';
    recognizer.onresult=e=>{
      if(!status.isConnected)return;
      const heard=e.results[0][0].transcript;
      status.textContent=routeLabel('Transcrição','Transcript','Transcripción')+' · '+heard+' · '+
        (assessExercise(heard,data.sentence)?routeLabel('As palavras coincidem com o modelo.','The words match the model.','Las palabras coinciden con el modelo.'):
          routeLabel('Compare as palavras transcritas com o modelo.','Compare the transcript with the model.','Compara la transcripción con el modelo.'));
    };
    recognizer.onerror=()=>{status.textContent='Não foi possível reconhecer sua fala. Confira a permissão do microfone ou use a gravação.';};
    recognizer.onend=()=>{if(activeRecognition===recognizer)activeRecognition=null;};
    try{recognizer.start();}catch{activeRecognition=null;status.textContent='O reconhecimento de voz não pôde iniciar.';}
    return true;
  }
  return false;
}
function stopVoiceTools(){
  if(activeRecognition){activeRecognition.abort?.();activeRecognition=null;}
  if(recording?.state==='recording')recording.stop();
  recordingStream?.getTracks().forEach(track=>track.stop());
}
function handleExerciseSubmit(event){
  if(event.target.id!=='exerciseAnswer')return false;
  event.preventDefault();
  const data=exerciseSample(currentLesson);
  checkExercise($('exerciseInput').value,exerciseKind==='gap'?data.target:data.sentence);
  $('exerciseInput')?.focus();
  return true;
}
function dictionaryExtras(item){
  const data=catalogForms[lang]?.[item.row[0]];
  if(!data||item.reviewed&&lang==='eng'&&item.row[0]==='Tom')return '';
  const [forms,synonyms,ipa]=data;
  const labels={plural:'plural',past:'passado',present:'presente',participle:'particípio',
    'first-person':'1ª pessoa','third-person':'3ª pessoa',preterite:'pretérito',imperfect:'imperfeito',singular:'singular',nominative:'nominativo'};
  return '<details><summary>Pronúncia, formas e sinônimos</summary>'+
    (ipa?'<p>IPA '+nativeText(ipa)+'</p>':'')+
    (forms.length?'<ul>'+forms.map(([word,tags])=>'<li>'+nativeText(word)+' <span class="meta">'+clean(tags.map(tag=>labels[tag]||tag).join(', '))+'</span></li>').join('')+'</ul>':'')+
    (synonyms.length?'<p>Sinônimos: '+synonyms.map(word=>nativeText(word)).join(', ')+'</p>':'')+'</details>';
}
function courseLevelIndex(language){
  const table=new Map();
  curriculum[language].forEach((rows,idx)=>rows.forEach(item=>table.set(item.row[0],levels[idx])));
  study[language].forEach((row,idx)=>table.set(row[1].split(' (')[0],levels[idx]));
  for(const word of sceneItems(language).map(entry=>entry.word))if(!table.has(word))table.set(word,'A1');
  if(language==='eng'){table.set('city','A1');table.set('small town','A1');}
  return table;
}
function editsWithin(a,b,max=2){
  if(Math.abs(a.length-b.length)>max)return max+1;
  let previous=Array.from({length:b.length+1},(_,i)=>i);
  for(let i=1;i<=a.length;i++){
    const row=[i];
    for(let j=1;j<=b.length;j++)row[j]=Math.min(row[j-1]+1,previous[j]+1,previous[j-1]+Number(a[i-1]!==b[j-1]));
    if(Math.min(...row)>max)return max+1;
    previous=row;
  }
  return previous[b.length];
}
function showSuggestions(words,query){
  const box=$('suggestions');box.innerHTML='';
  if(screen!=='dicionario'||exactWord||query.length<2||query.length>30)return;
  let candidates=words.filter(x=>normalize(x.row[0]).startsWith(query)&&normalize(x.row[0])!==query).slice(0,6);
  if(!candidates.length&&query.length>=3){
    const max=query.length<=5?1:2;
    candidates=words.filter(item=>editsWithin(query,normalize(item.row[0]),max)<=max).slice(0,5);
  }
  box.innerHTML=candidates.map(item=>'<a class="search-suggestion" href="'+clean(wordHash(item.row[0]))+'">'+nativeText(item.row[0])+'</a>').join('');
}
const lists=Object.create(null);
let studyMinutes;
function setupProfessional(){
  Object.assign(lists,read('favorite-lists',{}));
  studyMinutes=read('study-seconds',{});
  if(read('theme','light')==='dark')document.documentElement.dataset.theme='dark';
  $('modeTheme').textContent=document.documentElement.dataset.theme==='dark'?'Tema claro':'Tema escuro';
  $('modeTheme').addEventListener('click',()=>{
    const theme=document.documentElement.dataset.theme==='dark'?'light':'dark';
    document.documentElement.dataset.theme=theme;write('theme',theme);
    $('modeTheme').textContent=theme==='dark'?'Tema claro':'Tema escuro';
  });
  $('favoriteList').addEventListener('change',renderFavorites);
  $('favoriteEntries').addEventListener('submit',e=>{
    const form=e.target.closest('[data-favorite-key]');
    if(!form)return;
    e.preventDefault();
    const key=form.dataset.favoriteKey;
    const value=form.querySelector('input').value.trim().slice(0,45);
    if(value)lists[key]=value;else delete lists[key];
    write('favorite-lists',lists);renderFavorites();
  });
  $('favoriteEntries').addEventListener('click',e=>{
    const button=e.target.closest('[data-remove-favorite]');
    if(!button)return;
    saved.delete(button.dataset.removeFavorite);
    write('saved',[...saved]);renderFavorites();renderReview();
  });
  $('exportProgress').addEventListener('click',exportBackup);
  $('importProgress').addEventListener('click',importBackup);
  let lastActive=Date.now(),lastTick=lastActive;
  for(const type of ['pointerdown','keydown','touchstart'])document.addEventListener(type,()=>{lastActive=Date.now();},{passive:true});
  if(typeof window.setInterval==='function'){
    const timer=window.setInterval(()=>{
      const current=Date.now();
      if(!document.hidden&&['licao','revisao'].includes(screen)&&current-lastActive<=90000){
        const today=dateKey();
        studyMinutes[today]=(studyMinutes[today]||0)+Math.min(15,Math.max(0,Math.round((current-lastTick)/1000)));
        write('study-seconds',studyMinutes);drawStatistics();
      }
      lastTick=current;
    },15000);
    timer?.unref?.();
  }
  renderPlacement();
  setupMethodArt();
  setupOffline();
  switchScreen();
}
function renderFavorites(){
  const items=(cache[lang]||[]).filter(item=>saved.has(item.key));
  const input=$('favoriteList');
  const old=input.value;
  const labels=[...new Set(items.map(item=>lists[item.key]).filter(Boolean))].sort();
  input.innerHTML='<option value="">Todas</option>'+labels.map(label=>'<option value="'+clean(label)+'">'+clean(label)+'</option>').join('');
  input.value=labels.includes(old)?old:'';
  const showing=input.value?items.filter(item=>lists[item.key]===input.value):items;
  $('favoriteEntries').innerHTML=showing.length?showing.map(item=>'<article class="entry"><h3>'+
    '<a href="'+clean(wordHash(item.row[0]))+'">'+nativeText(item.row[0])+'</a></h3><p>'+clean(companionText(item.row[10]||item.row[1]))+'</p>'+
    '<form data-favorite-key="'+clean(item.key)+'"><label>Nome da lista <input maxlength="45" list="existingLists" value="'+clean(lists[item.key]||'')+'"></label>'+
    '<button>Salvar na lista</button></form><button type="button" data-remove-favorite="'+clean(item.key)+'">Remover favorito</button></article>').join('')+
    '<datalist id="existingLists">'+labels.map(label=>'<option value="'+clean(label)+'"></option>').join('')+'</datalist>':
    '<p>Salve palavras no dicionário para reuni-las aqui.</p>';
}
function recentDates(count){
  const now=Date.parse(dateKey());
  return Array.from({length:count},(_,i)=>new Date(now-i*86400000).toISOString().slice(0,10));
}
function drawStatistics(){
  if(!studyMinutes||!$('studyStats'))return;
  const today=dateKey(),minutes=Math.floor((studyMinutes[today]||0)/60);
  const completed=new Set(Object.values(done));
  const active=key=>completed.has(key)||(studyMinutes[key]||0)>=60;
  const dates=recentDates(7);
  const streakDays=recentDates(366);
  const first=active(today)?0:1;
  let streak=0;
  for(let i=first;i<streakDays.length&&active(streakDays[i]);i++)streak++;
  const recent=Object.values(done).filter(day=>dates.includes(day)).length;
  const weekly=dates.reduce((sum,day)=>sum+Math.floor((studyMinutes[day]||0)/60),0);
  if(!$('studyStats').querySelector('form')){
    $('studyStats').innerHTML='<div class="lesson-card"><h3>Ritmo de estudo</h3><p id="dailyMeter"></p><progress id="dailyProgress" aria-label="Meta de minutos de hoje"></progress><p id="weeklySummary"></p><p id="achievement"></p>'+
      '<form id="goalForm"><label>Meta diária em minutos <input id="goalMinutes" type="number" min="1" max="120" value="'+dailyGoal()+'"></label><button>Salvar meta</button></form></div>';
    $('goalForm').addEventListener('submit',event=>{event.preventDefault();const goal=Number($('goalMinutes').value);
      if(Number.isInteger(goal)&&goal>=1&&goal<=120){write('study-goal',goal);drawStatistics();}});
  }
  const goal=dailyGoal();
  $('dailyMeter').textContent=minutes+' de '+goal+' minutos hoje · Sequência de '+streak+(streak===1?' dia':' dias');
  $('dailyProgress').max=goal;$('dailyProgress').value=Math.min(minutes,goal);
  $('weeklySummary').textContent='Últimos 7 dias · '+recent+' lições concluídas · '+weekly+' minutos';
  const badges=[Object.keys(done).length>=1?'Primeira lição':null,streak>=3?'Três dias seguidos':null,minutes>=goal?'Meta do dia':null].filter(Boolean);
  $('achievement').textContent=badges.length?'Conquistas: '+badges.join(' · '):'Conclua uma lição para desbloquear sua primeira conquista.';
}
function dailyGoal(){
  const saved=Number(read('study-goal',10));
  return Number.isInteger(saved)&&saved>=1&&saved<=120?saved:10;
}
function exportBackup(){
  const payload={version:1,active:{language:lang,level,support},done,saved:[...saved],positions,reviews,lists,studyMinutes,courseLevels,goal:dailyGoal()};
  const bytes=new TextEncoder().encode(JSON.stringify(payload));
  let binary='';
  for(const byte of bytes)binary+=String.fromCharCode(byte);
  $('restoreCode').value='PG1.'+btoa(binary);
  $('restoreCode').focus();$('restoreCode').select?.();
  $('backupStatus').textContent='Código gerado. Copie o conteúdo e guarde-o em um local seguro.';
}
function importBackup(){
  const status=$('backupStatus');
  try{
    const field=$('restoreCode').value.trim();
    if(!field.startsWith('PG1.')||field.length>1500000)throw Error('invalid');
    const text=new TextDecoder().decode(Uint8Array.from(atob(field.slice(4)),v=>v.charCodeAt(0)));
    const data=JSON.parse(text);
    if(data?.version!==1||!Array.isArray(data.saved)||!data.done||typeof data.done!=='object')throw Error('invalid');
    const validDate=value=>typeof value==='string'&&/^\d{4}-\d{2}-\d{2}$/.test(value);
    const validWord=key=>typeof key==='string'&&/^(eng|spa|ita|deu|ara|jpn|por|cmn)\|.{1,180}$/u.test(key);
    const existingActivity=Object.keys(done).length>0||Object.keys(positions).length>0||saved.size>0;
    let completed=0;
    for(const [key,value] of Object.entries(data.done))if(/^(eng|spa|ita|deu|ara|jpn|por|cmn)-[0-5](-[1-9][0-9]{0,2})?$/.test(key)&&validDate(value)){
      if(!done[key])completed++;
      if(!done[key]||done[key]<value)done[key]=value;
    }
    for(const key of data.saved)if(validWord(key))saved.add(key);
    for(const [key,value] of Object.entries(data.positions||{}))if(/^(eng|spa|ita|deu|ara|jpn|por|cmn)-[0-5]$/.test(key)&&Number.isInteger(value)&&value>=0&&value<lessonsPerLevel){
      if(!Object.hasOwn(positions,key))positions[key]=value;
    }
    for(const [key,value] of Object.entries(data.reviews||{}))if(validWord(key)&&saved.has(key)&&value&&Number.isFinite(value.due)&&Number.isInteger(value.days)&&value.days>=0&&value.days<36500){
      if(!reviews[key]||reviews[key].due<value.due)reviews[key]={due:value.due,days:value.days};
    }
    for(const [key,label] of Object.entries(data.lists||{}))if(validWord(key)&&saved.has(key)&&typeof label==='string'&&label.trim()&&!lists[key])lists[key]=label.trim().slice(0,45);
    for(const [day,seconds] of Object.entries(data.studyMinutes||{}))if(validDate(day)&&Number.isInteger(seconds)&&seconds>=0&&seconds<=86400)studyMinutes[day]=Math.max(studyMinutes[day]||0,seconds);
    for(const [key,value] of Object.entries(data.courseLevels||{}))if(Object.hasOwn(languages,key)&&!Object.hasOwn(courseLevels,key)&&Number.isInteger(value)&&value>=0&&value<levels.length)courseLevels[key]=value;
    if(read('study-goal',null)===null&&Number.isInteger(data.goal)&&data.goal>=1&&data.goal<=120)write('study-goal',data.goal);
    write('done',done);write('saved',[...saved]);write('lesson-position',positions);write('review-schedule',reviews);
    write('favorite-lists',lists);write('study-seconds',studyMinutes);write('course-levels',courseLevels);
    const active=data.active;
    if(!existingActivity&&active&&Object.hasOwn(languages,active.language)&&Number.isInteger(active.level)&&active.level>=0&&active.level<levels.length){
      changeCourse(active.language);level=active.level;courseLevels[lang]=level;
      support=active.support==='spa'?'spa':'eng';
      write('level',level);write('course-levels',courseLevels);write('support-language',support);
      drawLanguages();loadWords();
    }
    unit=selectedUnit();drawLesson();renderReview();drawWords();
    status.textContent='Dados mesclados. '+completed+' lições concluídas foram acrescentadas.';
  }catch{status.textContent='Código inválido. Confira se copiou o código completo.';}
}
let installPrompt;
function setupOffline(){
  const status=$('offlineStatus'),button=$('saveOffline');
  if(window.POGGLO_OFFLINE){button.hidden=true;status.textContent='Você está usando a versão offline do ZIP.';return;}
  window.addEventListener('beforeinstallprompt',event=>{
    event.preventDefault();installPrompt=event;$('installApp').hidden=false;
  });
  $('installApp').addEventListener('click',async()=>{
    if(!installPrompt)return;
    await installPrompt.prompt();
    installPrompt=null;$('installApp').hidden=true;
  });
  if(typeof navigator==='undefined'||!navigator.serviceWorker){button.disabled=true;status.textContent='Use o ZIP para estudar offline neste navegador.';return;}
  navigator.serviceWorker.register('service-worker.js').catch(()=>{button.disabled=true;status.textContent='Instalação offline indisponível. Use o ZIP.';});
  button.addEventListener('click',async()=>{
    button.disabled=true;status.textContent='Salvando o curso…';
    try{
      const registration=await navigator.serviceWorker.ready;
      const channel=new MessageChannel(),language=lang;
      const result=new Promise((resolve,reject)=>{
        const timer=setTimeout(()=>reject(Error('timeout')),90000);
        channel.port1.onmessage=event=>{clearTimeout(timer);resolve(event.data);};
      });
      registration.active.postMessage({type:'cache-course',language},[channel.port2]);
      if(!await result)throw Error('offline');
      status.textContent=languages[language][1]+' salvo neste dispositivo para usar offline.';
    }catch{status.textContent='Não foi possível salvar. Tente novamente ou use o ZIP.';}
    finally{button.disabled=false;}
  });
}
