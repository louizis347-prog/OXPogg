function wordUseGap(line,target){
  const prepared=lessonLevelText(line);
  const term=lessonLevelText(target).replace(/[.…?!]+$/u,'');
  if(!prepared||!term)return '';
  const escaped=term.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  const pattern=['jpn','cmn'].includes(lang)?escaped:'(?<![\\p{L}\\p{N}])'+escaped+'(?![\\p{L}\\p{N}])';
  const gap=prepared.replace(new RegExp(pattern,'giu'),'_____');
  return gap!==prepared?gap:'';
}
function wordUseCases(lesson){
  const {vocabulary,practiceContent}=lesson;
  const targets=[vocabulary.word,vocabulary.expression];
  const original=vocabulary.sceneSource;
  const translated=vocabulary.sceneTranslation;
  const rows=original?targets.map((_,i)=>({text:original[i+3],pt:translated[i+3]})):
    [vocabulary.wordExample,vocabulary.expressionExample];
  const meaning=vocabulary.meanings||(original?translated.slice(1,3):
    [companionText(glosses[lang][level]),companionText(phrases[lang][level][1])]);
  const all=[...rows,...practiceContent.reading,...practiceContent.dialogue].filter(row=>row?.text&&row.pt);
  const used=[];
  const available=row=>!used.some(text=>assessExercise(row.text,text));
  const take=(predicate,preferred=all)=>{
    const line=preferred.find(row=>row?.text&&row.pt&&available(row)&&predicate(row));
    if(line)used.push(line.text);
    return line;
  };
  const cases=targets.map((term,i)=>{
    const line=take(row=>wordUseGap(row.text,term),[rows[i],...all]);
    return {term,line,gap:wordUseGap(line?.text,term),meaning:meaning[i]};
  });
  const includesTarget=row=>targets.some(term=>wordUseGap(row.text,term));
  const enoughWords=row=>wordUseTokens(row.text).length>2;
  const order=take(row=>enoughWords(row)&&includesTarget(row))||take(enoughWords)||take(()=>true);
  const speaking=take(includesTarget)||take(()=>true);
  return {cases,order,speaking,targets};
}
function wordUseTokens(text){
  const prepared=lessonLevelText(text);
  if(!['jpn','cmn'].includes(lang))return prepared.split(/\s+/);
  if(typeof Intl.Segmenter!=='function')return Array.from(prepared);
  return [...new Intl.Segmenter(languages[lang][2],{granularity:'word'}).segment(prepared)].map(part=>part.segment);
}
function wordUseOrder(line){
  const tokens=wordUseTokens(line.text);
  const positions=tokens.map((_,index)=>index);
  let seed=unit+level*251+197;
  for(let i=positions.length-1;i>0;i--){
    seed=(1664525*seed+1013904223)>>>0;
    const j=seed%(i+1);
    [positions[i],positions[j]]=[positions[j],positions[i]];
  }
  if(positions.length>1&&positions.every((position,i)=>position===i))positions.push(positions.shift());
  return '<section class="word-use-case word-use-order"><h4>'+routeLabel('Monte a frase','Build the sentence','Ordena la frase')+'</h4><p>'+
    routeLabel('Leia o sentido e toque nos blocos para montar a frase. Toque de novo para retirar um bloco.','Read the meaning and tap the tiles to build the sentence. Tap a tile again to remove it.','Lee el sentido y toca los bloques para armar la frase. Toca un bloque de nuevo para quitarlo.')+
    '</p><p lang="'+supportTag()+'">'+clean(line.pt)+'</p><div class="word-use-assembled" data-word-use-assembled aria-label="'+
    routeLabel('Sua frase','Your sentence','Tu frase')+'"></div><div class="word-use-options" data-word-use-bank>'+
    positions.map(index=>'<button type="button" data-word-use-token="'+index+'">'+nativeText(tokens[index])+'</button>').join('')+
    '</div><div class="controls"><button type="button" data-word-use-order="check">'+routeLabel('Conferir ordem','Check order','Comprobar orden')+
    '</button><button type="button" data-word-use-order="reset">'+routeLabel('Recomeçar','Start over','Empezar de nuevo')+
    '</button></div><p class="word-use-feedback" role="status"></p><div class="word-use-model" hidden>'+
    nativeText(lessonLevelText(line.text),'p')+lessonPlayButton(line.text,{compact:true})+'</div></section>';
}
function wordUseSpeaking(line,targets){
  const model=lessonLevelText(line.text);
  const target=targets.find(term=>wordUseGap(model,term))||'';
  const canRecognize=window.SpeechRecognition||window.webkitSpeechRecognition;
  return '<section class="word-use-case word-use-speaking"><h4>'+routeIcon('chat')+' '+
    routeLabel('Diga em voz alta','Say it aloud','Dilo en voz alta')+'</h4><p>'+
    routeLabel('Diga a frase a partir da pista. Depois, compare as palavras reconhecidas com o modelo.',
      'Say the line from the cue. Then compare the words recognized with the model.',
      'Di la frase a partir de la pista. Después, compara las palabras reconocidas con el modelo.')+
    '</p><blockquote lang="'+supportTag()+'">'+clean(line.pt)+'</blockquote>'+
    (target?'<p>'+routeLabel('Tente usar','Try using','Intenta usar')+' · '+nativeText(target)+'</p>':'')+
    (canRecognize?'<button type="button" class="primary" data-word-use-recognize data-target="'+clean(target)+'">'+
      routeLabel('Analisar minha fala','Analyze my speech','Analizar mi voz')+'</button><p class="meta">'+
      routeLabel('O reconhecimento do navegador compara as palavras ouvidas com o modelo. Ele pode precisar de internet.',
        'Browser recognition compares the words it heard with the model. It may require internet access.',
        'El reconocimiento del navegador compara las palabras que oye con el modelo. Puede requerir internet.')+'</p>':
      '<p class="meta">'+routeLabel('Use a gravação abaixo para comparar sua fala com o modelo.',
        'Use the recording below to compare your speech with the model.',
        'Usa la grabación de abajo para comparar tu voz con el modelo.')+'</p>')+
    '<p class="word-use-feedback" data-speech-status role="status"></p><div data-speech-result hidden></div>'+
    recordControls(model,{withModel:false})+
    '<details><summary>'+routeLabel('Conferir minha fala','Compare my speech','Comparar mi intervención')+'</summary>'+
    '<div data-speech-model>'+nativeText(model,'p')+exampleAudio(model)+'</div></details></section>';
}
function renderWordUse(lesson){
  const {cases,order,speaking,targets}=wordUseCases(lesson);
  const options=unit%2?[...targets].reverse():targets;
  return '<section class="word-use lesson-card" aria-labelledby="wordUseHeading"><div class="word-use-heading">'+routeIcon('notebook')+
    '<h3 id="wordUseHeading">'+routeLabel('Palavra em uso','Word in use','Palabra en uso')+'</h3></div><p>'+
    routeLabel('Monte uma frase, teste o vocabulário em contexto e pratique uma fala da cena.',
      'Build a sentence, test vocabulary in context, and practice a line from the scene.',
      'Ordena una frase, practica el vocabulario en contexto y di una intervención de la escena.')+'</p>'+
    (order?wordUseOrder(order):'')+'<section class="word-use-context"><h4>'+routeLabel('Escolha pelo contexto','Choose by context','Elige según el contexto')+'</h4>'+
    '<div class="word-use-grid">'+cases.map(({term,line,gap,meaning},i)=>
      '<article class="word-use-case"><h4>'+routeLabel('Situação ','Situation ','Situación ')+(i===0?'A':'B')+'</h4>'+
      (gap?'<p>'+routeLabel('Qual opção completa a fala?','Which option completes the line?','¿Qué opción completa la intervención?')+'</p>'+
        nativeText(gap,'p')+'<p class="meta" lang="'+supportTag()+'">'+clean(line.pt)+'</p>':
        '<p>'+routeLabel('Qual opção tem este sentido?','Which option has this meaning?','¿Qué opción tiene este significado?')+
        '</p><p lang="'+supportTag()+'">'+clean(meaning)+'</p>')+
      '<div class="word-use-options">'+options.map(option=>'<button type="button" data-word-use-choice="'+
        (option===lessonLevelText(term)?'correct':'retry')+'" aria-pressed="false">'+nativeText(option)+'</button>').join('')+'</div>'+
      '<p class="word-use-feedback" role="status"></p><div class="word-use-model" hidden>'+
      (line?nativeText(line.text,'p')+lessonPlayButton(line.text,{compact:true})+
        '<p class="meta" lang="'+supportTag()+'">'+clean(line.pt)+'</p>':'')+'</div></article>').join('')+'</div>'+
    '</section>'+(speaking?wordUseSpeaking(speaking,targets):'')+'</section>';
}
function handleWordUseClick(event){
  const microphone=event.target.closest('[data-word-use-recognize]');
  if(microphone){recognizeWordUse(microphone);return true;}
  const action=event.target.closest('[data-word-use-token],[data-word-use-order]');
  if(action){
    const card=action.closest('.word-use-order');
    const bank=card.querySelector('[data-word-use-bank]');
    const assembled=card.querySelector('[data-word-use-assembled]');
    const status=card.querySelector('[role="status"]');
    const model=card.querySelector('.word-use-model');
    if(action.dataset.wordUseOrder==='check'){
      const used=[...assembled.children];
      const complete=!bank.children.length;
      const correct=complete&&assessExercise(used.map(button=>button.textContent).join(['jpn','cmn'].includes(lang)?'':' '),model.querySelector('p').textContent);
      status.dataset.feedback=correct?'correct':'retry';
      status.textContent=correct?routeLabel('Certo. Ouça a frase inteira.','Correct. Listen to the full sentence.','Correcto. Escucha la frase completa.'):
        complete?routeLabel('Ainda não. Experimente outra ordem.','Try a different order.','Prueba otro orden.'):
          routeLabel('Use todos os blocos antes de conferir.','Use every tile before checking.','Usa todos los bloques antes de comprobar.');
      model.hidden=!correct;
    }else{
      if(action.dataset.wordUseOrder==='reset')bank.append(...assembled.children);
      else{
        (action.parentElement===bank?assembled:bank).append(action);
        action.focus();
      }
      status.textContent='';
      model.hidden=true;
    }
    return true;
  }
  const button=event.target.closest('[data-word-use-choice]');
  if(!button)return false;
  const card=button.closest('.word-use-case');
  const status=card.querySelector('[role="status"]');
  const correct=button.dataset.wordUseChoice==='correct';
  for(const option of card.querySelectorAll('[data-word-use-choice]')){
    option.setAttribute('aria-pressed',String(option===button));
    option.disabled=correct;
  }
  status.dataset.feedback=correct?'correct':'retry';
  status.textContent=correct?
    routeLabel('Certo. Agora ouça a fala completa.','Correct. Now listen to the full line.','Correcto. Ahora escucha la intervención completa.'):
    routeLabel('Tente de novo. Veja qual opção combina com o sentido do trecho.','Try again. Check which option matches the meaning.','Inténtalo de nuevo. Fíjate en qué opción coincide con el sentido.');
  if(correct)card.querySelector('.word-use-model').hidden=false;
  return true;
}

function wordUseSpeechTokens(text){
  const words=wordUseTokens(text).map(token=>token.trim()).filter(token=>/[\p{L}\p{N}]/u.test(token));
  return words.map(label=>({label,key:normalize(label).replace(/[^\p{L}\p{N}]/gu,'')}));
}
function alignWordUseSpeech(model,transcript){
  const expected=wordUseSpeechTokens(model),heard=wordUseSpeechTokens(transcript);
  const lengths=Array.from({length:expected.length+1},()=>new Uint16Array(heard.length+1));
  for(let i=expected.length-1;i>=0;i--){
    for(let j=heard.length-1;j>=0;j--){
      lengths[i][j]=expected[i].key===heard[j].key?1+lengths[i+1][j+1]:Math.max(lengths[i+1][j],lengths[i][j+1]);
    }
  }
  let i=0,j=0;
  while(i<expected.length&&j<heard.length){
    if(expected[i].key===heard[j].key){expected[i++].matched=true;j++;}
    else if(lengths[i+1][j]>=lengths[i][j+1])i++;
    else j++;
  }
  return expected;
}
function showWordUseSpeech(card,model,transcript,target){
  const result=card.querySelector('[data-speech-result]');
  const words=alignWordUseSpeech(model,transcript);
  const matched=words.filter(word=>word.matched).length;
  const focus=wordUseSpeechTokens(target).map(word=>word.key);
  const heard=wordUseSpeechTokens(transcript).map(word=>word.key);
  const gotFocus=focus.length&&heard.some((_,i)=>focus.every((key,j)=>heard[i+j]===key));
  const matchedLabel=routeLabel('Reconhecida em ordem','Recognized in order','Reconocida en orden');
  const retryLabel=routeLabel('Para praticar','To practice','Para practicar');
  const advice=matched===words.length?
    routeLabel('As palavras do modelo apareceram em ordem. Ouça o ritmo e repita mais uma vez.','The model words appeared in order. Listen to the rhythm and repeat.','Las palabras del modelo aparecieron en orden. Escucha el ritmo y repite.'):
    routeLabel('Ouça o modelo e repita prestando atenção às palavras marcadas. O navegador também pode interpretar uma palavra de outro jeito.',
      'Listen to the model and repeat, focusing on the marked words. The browser can also mishear a word.',
      'Escucha el modelo y repite, prestando atención a las palabras marcadas. El navegador también puede oír una palabra de otra manera.');
  result.innerHTML='<div class="speech-result-head"><strong>'+routeLabel('O que o navegador ouviu','What the browser heard','Lo que oyó el navegador')+
    '</strong><span>'+matched+' / '+words.length+' '+routeLabel('em ordem','in order','en orden')+'</span></div>'+
    nativeText(transcript,'p')+'<ul class="speech-word-list">'+words.map(({label,matched})=>'<li data-match="'+Boolean(matched)+'">'+
      '<span aria-hidden="true">'+(matched?'✓':'↻')+'</span>'+nativeText(label)+
      '<span class="speech-word-status">'+(matched?matchedLabel:retryLabel)+'</span></li>').join('')+'</ul>'+
    (focus.length?'<p><strong>'+routeLabel('Vocabulário-alvo','Target vocabulary','Vocabulario objetivo')+' · </strong>'+
      nativeText(target)+' · '+(gotFocus?routeLabel('reconhecido','recognized','reconocido'):retryLabel)+'</p>':'')+
    '<p>'+advice+'</p>'+exampleAudio(model);
  result.hidden=false;
}
function recognizeWordUse(button){
  const Speech=window.SpeechRecognition||window.webkitSpeechRecognition;
  const card=button.closest('.word-use-speaking');
  const status=card.querySelector('[data-speech-status]');
  if(!Speech||activeRecognition||recording?.state==='recording')return;
  const model=card.querySelector('[data-speech-model] p').textContent;
  const recognizer=new Speech();
  recognizer.lang=languages[lang][2];
  activeRecognition=recognizer;
  card.querySelector('[data-speech-result]').hidden=true;
  stopLessonPlayback();
  window.speechSynthesis?.cancel();
  button.disabled=true;
  status.textContent=routeLabel('Fale agora.','Speak now.','Habla ahora.');
  let received=false;
  const retry=routeLabel('Não consegui transcrever. Tente novamente ou use a gravação para comparar com o modelo.',
    'Speech could not be transcribed. Try again or use the recording to compare with the model.',
    'No se pudo transcribir. Inténtalo otra vez o usa la grabación para comparar con el modelo.');
  recognizer.onresult=event=>{
    if(activeRecognition!==recognizer)return;
    const transcript=event.results[0]?.[0]?.transcript?.trim();
    if(!transcript)return;
    received=true;
    showWordUseSpeech(card,model,transcript,button.dataset.target);
    status.textContent=routeLabel('Comparação disponível abaixo.','Comparison available below.','Comparación disponible abajo.');
  };
  recognizer.onend=()=>{
    button.disabled=false;
    if(activeRecognition!==recognizer){status.textContent='';return;}
    activeRecognition=null;
    if(!received)status.textContent=retry;
  };
  try{recognizer.start();}
  catch{activeRecognition=null;button.disabled=false;status.textContent=retry;}
}
