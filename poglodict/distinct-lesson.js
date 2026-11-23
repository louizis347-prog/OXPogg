// Authored beginner scenes. Each row has a title, two terms, three examples, five reading lines and six turns.
const englishBeginnerScenes={
  2:{key:1,
    eng:['Finding the station','way','on the left','Is this the way to the station?','The station is on the left.','Can you show me the way?',
      'Lia is on King Street.','She has a small map.','She stops at a café to ask the way.','The man at the café points to a bridge.','Lia crosses the bridge and finds the station.',
      'Excuse me. Is this the way to the station?','Yes. Walk to the bridge.','Do I cross the bridge?','Yes. The station is on the left.','Is it far?','No. It is a five-minute walk.'],
    pt:['O caminho até a estação','caminho','à esquerda','É por aqui que se vai à estação?','A estação fica à esquerda.','Pode me mostrar o caminho?',
      'Lia está na King Street.','Ela tem um mapa pequeno.','Ela para num café para perguntar o caminho.','O homem do café aponta para uma ponte.','Lia atravessa a ponte e encontra a estação.',
      'Com licença. É por aqui que se vai à estação?','Sim. Caminhe até a ponte.','Eu atravesso a ponte?','Sim. A estação fica à esquerda.','É longe?','Não. São cinco minutos a pé.']},
  3:{key:4,
    eng:['Packing a school bag','things','in my bag','These are my things.','My notebook is in my bag.','Put your things on the desk.',
      'Ravi is getting ready for class.','He puts three things on the desk.','He has a notebook, a pencil and a book.','The pencil falls under the desk.','Lia picks it up and gives it to him.',
      'Are these your things, Ravi?','Yes. I need them for class.','Is your book in your bag?','Yes, but my pencil is not in my bag.','Here it is. It was under the desk.','Thank you. Now I am ready.'],
    pt:['Arrumando a mochila','coisas','na minha mochila','Estas são as minhas coisas.','Meu caderno está na minha mochila.','Coloque suas coisas sobre a mesa.',
      'Ravi está se preparando para a aula.','Ele coloca três coisas sobre a mesa.','Ele tem um caderno, um lápis e um livro.','O lápis cai embaixo da mesa.','Lia pega o lápis e o entrega a ele.',
      'Estas são as suas coisas, Ravi?','Sim. Preciso delas para a aula.','Seu livro está na sua mochila?','Sim, mas meu lápis não está na mochila.','Aqui está. Ele estava embaixo da mesa.','Obrigado. Agora estou pronto.']},
  4:{key:2,
    eng:['Waiting outside the library','there','next to the door','My friend is there.','The bench is next to the door.','You can wait there.',
      'Lia arrives at the library.','The library opens at ten.','It is nine now.','There is a bench next to the door.','Lia waits on the bench and reads a book.',
      'Is the library open?','No. It opens at ten.','Can I wait here?','Yes. You can sit on that bench.','Is it the bench next to the door?','Yes, that one. I can meet you there.'],
    pt:['A espera na biblioteca','lá','ao lado da porta','Meu amigo está lá.','O banco fica ao lado da porta.','Você pode esperar lá.',
      'Lia chega à biblioteca.','A biblioteca abre às dez.','Agora são nove horas.','Tem um banco ao lado da porta.','Lia espera no banco e lê um livro.',
      'A biblioteca está aberta?','Não. Ela abre às dez.','Posso esperar aqui?','Sim. Pode se sentar naquele banco.','É o banco ao lado da porta?','Sim, esse mesmo. Posso encontrar você lá.']}
};
function assignedLessonWord(item,sceneWord){
  if(!item||item.row[0]===sceneWord)return null;
  const [word,definition]=item.row;
  const gloss=item.row[10];
  const lengthLimit=[13,18,24,32,40,48][level];
  const maxChars=['jpn','cmn'].includes(lang)?lengthLimit*3:lengthLimit*9;
  const examples=exampleList(item).filter(example=>{
    const translation=exampleTranslation(example);
    return example.text&&translation.text&&!example.context&&(!example.english||lang==='por')&&
      example.text.trim().split(/\s+/).length<=lengthLimit&&example.text.length<=maxChars;
  }).slice(0,2);
  return {word,meaning:companionText(gloss||definition),definitionLang:lang==='por'||gloss?supportTag():'en',examples};
}
function assignedPracticeExample(focus){
  if(!focus?.examples.length)return null;
  const example=focus.examples[0];
  return {word:focus.word,text:example.text,pt:exampleTranslation(example).text};
}
function renderAssignedLessonWord(focus,usedPhotos){
  const item=wordIndex[lang]?.lookup.get(focus.word);
  return '<section class="assigned-lesson-word" aria-labelledby="assignedWordHeading"><h3 id="assignedWordHeading">'+
    routeLabel('Palavra desta lição','Word for this lesson','Palabra de esta lección')+'</h3><div class="term-heading">'+
    (item?linkTo(item,''):nativeText(focus.word,'strong'))+lessonVocabularyAudio(focus.word)+'</div>'+
    '<details><summary>'+routeLabel('Conferir o significado','Check the meaning','Comprobar el significado')+'</summary>'+
    '<p lang="'+focus.definitionLang+'">'+clean(focus.meaning)+'</p></details>'+
    (focus.examples.length?'<p>'+routeLabel('Leia este exemplo e observe em que situação a palavra aparece.','Read the example and notice when the word is used.','Lee el ejemplo y observa en qué situación aparece la palabra.')+'</p>'+
      '<div class="lesson-example-grid">'+focus.examples.map((example,i)=>renderExample(example,i+1,undefined,usedPhotos)).join('')+'</div>':
      '<p>'+routeLabel('Ouça a palavra e tente usá-la em uma frase curta. Confira as acepções disponíveis no verbete.','Listen to the word and try using it in a short sentence. Check the dictionary entry for its senses.','Escucha la palabra e intenta usarla en una frase corta. Consulta sus acepciones en el diccionario.')+'</p>')+'</section>';
}
