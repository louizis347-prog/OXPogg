function lessonCoach(title,instruction,answer=''){
  return '<aside class="lesson-coach"><strong>'+clean(title)+'</strong><p>'+clean(instruction)+'</p>'+
    (answer?'<details><summary>'+routeLabel('Conferir','Check','Comprobar')+'</summary>'+answer+'</details>':'')+'</aside>';
}
function grammarArcPrompt(){
  const arc=Math.min(6,Math.floor(unit/lessonsPerArc));
  const supportIndex=lang==='por'?(support==='spa'?2:1):0;
  const goals=[
    ['Leia o primeiro exemplo. Aponte onde a regra aparece antes de consultar o modelo.','Read the first example and point out the pattern before checking.','Lee el primer ejemplo y señala el patrón antes de comprobar.'],
    ['Leia os dois primeiros exemplos e encontre a parte da construção que se repete.','Read the first two examples and find the part of the pattern they share.','Lee los dos primeros ejemplos y encuentra la parte del patrón que comparten.'],
    ['Cubra o primeiro exemplo e tente reconstruí-lo de memória. Confira a ordem das palavras.','Cover the first example and reconstruct it from memory. Check the word order.','Tapa el primer ejemplo y reconstrúyelo de memoria. Comprueba el orden.'],
    ['Troque um detalhe do primeiro exemplo e preserve a regra. Diga a nova frase em voz alta.','Change one detail in the first example while keeping the rule. Say your new sentence aloud.','Cambia un detalle del primer ejemplo y conserva la regla. Di tu nueva frase en voz alta.'],
    ['Escolha dois exemplos e explique que informação mudaria se você trocasse uma parte da construção.','Pick two examples and explain what would change if you replaced one part of the pattern.','Elige dos ejemplos y explica qué cambiaría si sustituyeras una parte del patrón.'],
    ['Use a construção para responder a uma fala do diálogo ou escrever uma nova pergunta.','Use the pattern to reply to a line from the dialogue or write a new question.','Utiliza el patrón para responder a una intervención o escribir una pregunta nueva.'],
    ['Escreva uma frase sua com a construção, compare com os exemplos e justifique sua escolha.','Write your own sentence using the pattern, compare it with the examples and explain your choice.','Escribe una frase con el patrón, compárala con los ejemplos y justifica tu elección.']
  ];
  const guide=routeLabel('Na sua versão, confira três coisas: o que a frase comunica, a posição das palavras e a parte da regra que precisa permanecer.','Check three things in your version: what the sentence communicates, the word order and the part of the pattern that must stay.','Comprueba tres cosas en tu versión: qué comunica la frase, el orden de las palabras y la parte del patrón que debe mantenerse.');
  return lessonCoach(routeLabel('Experimente a regra','Try the rule','Pon a prueba la regla'),goals[arc][supportIndex],'<p>'+clean(guide)+'</p>');
}
function grammarPanel(language,levelIndex,guided,topic,audio,usedPhotos){
  const [title,tip,model,modelPt]=topic;
  const i=levelIndex+(guided?6:0);
  const [second,secondPt,third,thirdPt]=extraGrammar[language][i];
  const examples=[[model,modelPt],[second,secondPt],[third,thirdPt],fourthGrammar[language][i]];
  return renderGrammarRule(title,tip,grammarNotes[language][i],examples,audio,usedPhotos);
}
function renderGrammarRule(title,tip,note,examples,audio,usedPhotos,check=''){
  return '<div class="grammar-panel"><h3>'+clean(companionText(title))+'</h3>'+
    '<div class="grammar-rule"><h4>'+routeLabel('Como funciona','How it works','Cómo funciona')+'</h4><p>'+clean(companionText(tip))+'</p>'+
    '<p>'+clean(companionText(note))+'</p></div>'+shortFormsGuide()+
    '<h4>'+routeLabel('Veja em contexto','See it in context','Observa en contexto')+'</h4><div class="lesson-example-grid">'+
    examples.map(([text,translation],n)=>{
      audio['grammar'+n]=lessonLevelText(text);
      return renderExample({text,translation},n+1,undefined,usedPhotos);
    }).join('')+'</div>'+check+grammarArcPrompt()+'</div>';
}
function englishArticleCheck(){
  const cases=[
    {word:'honest',sentence:'She gave me ___ honest answer.',article:'an',reason:'O h de honest é mudo. A palavra começa com som de vogal.'},
    {word:'European',sentence:'We met ___ European student.',article:'a',reason:'European começa com o som de y em yes. Por isso usamos a.'}
  ];
  if(unit%2)cases.reverse();
  return '<section class="grammar-choice"><h4>Escolha pelo som</h4><p>Ouça a palavra que vem depois da lacuna. Decida se o primeiro som é de consoante ou de vogal e faça sua escolha.</p>'+
    cases.map(({word,sentence,article,reason})=>'<div class="grammar-choice-case"><p lang="en">'+clean(sentence)+'</p>'+
      lessonPlayButton(word,{compact:true})+'<div class="controls">'+['a','an'].map(option=>
        '<button type="button" data-grammar-choice="'+option+'">'+option+'</button>').join('')+'</div>'+
      '<p class="grammar-choice-status" role="status" data-correct="'+article+'" data-reason="'+clean(reason)+'"></p></div>').join('')+'</section>';
}
function handleGrammarChoice(event){
  const button=event.target.closest('[data-grammar-choice]');
  if(!button)return false;
  const status=button.closest('.grammar-choice-case').querySelector('[role="status"]');
  const right=button.dataset.grammarChoice===status.dataset.correct;
  status.textContent=right?'Certo. '+status.dataset.reason:
    (status.dataset.wrong||'Ouça o primeiro som da palavra após a lacuna e tente de novo.');
  status.dataset.feedback=right?'correct':'retry';
  return true;
}
