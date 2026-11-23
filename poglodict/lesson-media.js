function lessonVisualTheme(){return studyTitleAt(unit).art;}
function lessonLinesMarkup(lines,kind,{id='',hideTranslation=false,theme=lessonVisualTheme(),used=new Set()}={}){
  const dialogue=['dialogue','continuation','practice'].includes(kind);
  return '<ol class="lesson-lines illustrated-lines"'+(id?' id="'+id+'"':'')+'>'+lines.map(({text,pt},index)=>{
    const voice=dialogue?index%2:0;
    const marker=dialogue?routeLabel('Pessoa ','Speaker ','Persona ')+(voice?'B':'A'):
      routeLabel('Trecho ','Line ','Fragmento ')+(index+1);
    return '<li class="illustrated-line" data-audio-line>'+lessonPhotoFrame(photoForMoment(theme,index,kind,pt,used),'lesson-line-photo')+
      '<div class="illustrated-line-content"><div class="illustrated-line-top"><span class="line-marker">'+clean(marker)+'</span>'+
      lessonPlayButton(text,{label:ui('Ouvir'),voice,compact:true,line:true})+'</div><div class="line-target">'+nativeText(text,'p')+pinyinLine(text)+'</div>'+
      '<p class="lesson-pt"'+(hideTranslation?' hidden':'')+' lang="'+supportTag()+'">'+clean(pt)+'</p>'+
      lessonWordPicker(text,voice)+'</div></li>';
  }).join('')+'</ol>';
}
function illustratedExampleControls(text,index,translation,used){
  return '<div class="illustrated-example-tools" data-audio-line>'+lessonPhotoFrame(photoForMoment(lessonVisualTheme(),index,'example',translation||text,used),'lesson-example-photo')+
    '<div>'+lessonPlayButton(text,{label:routeLabel('Ouvir exemplo','Listen to example','Escuchar ejemplo'),compact:true})+
    lessonWordPicker(text)+'</div></div>';
}
function lessonVocabularyAudio(word){
  return lessonPlayButton(word,{compact:true,label:routeLabel('Ouvir palavra','Listen to the word','Escuchar palabra')});
}
function scenePracticeLines(theme){
  const authored=plannedEnglishContent();
  if(authored)return authored.dialogue;
  const script=dialoguePracticeText[theme]||dialoguePracticeText.map;
  const content=script[lang==='por'?'pt':lang].split('|');
  const translated=script[supportLocale()].split('|');
  return content.map((text,index)=>({text:lessonLevelText(text),pt:translated[index]}));
}
function scenePracticeRound(lines,round){
  const cue=lines[round*2],reply=lines[round*2+1];
  const options=[1,3,5,7].filter(index=>index!==round*2+1);
  options.splice((unit+level+round)%options.length,1);
  options.splice((unit+level+round)%3,0,round*2+1);
  return '<div class="scene-practice-round" data-round="'+round+'">'+
    '<p class="scene-round-label" tabindex="-1">'+routeLabel('Rodada ','Round ','Ronda ')+(round+1)+' / 4</p>'+
    (round?'<details class="scene-recap"><summary>'+routeLabel('Rever a conversa até aqui','Review the conversation so far','Repasar la conversación hasta aquí')+'</summary>'+
      '<ol>'+lines.slice(0,round*2).map(({text},index)=>'<li>'+nativeText(text)+lessonPlayButton(text,{compact:true,voice:index%2})+'</li>').join('')+'</ol></details>':'')+
    '<div class="scene-round-cue">'+nativeText(cue.text,'p')+pinyinLine(cue.text)+lessonPlayButton(cue.text)+
    '<details><summary>'+routeLabel('Ver tradução da pergunta','Show question translation','Ver traducción de la pregunta')+'</summary>'+
    '<p lang="'+supportTag()+'">'+clean(cue.pt)+'</p></details></div>'+
    '<div class="workshop-choices">'+options.map(index=>'<div><button type="button" class="workshop-choice" data-scene-answer="'+
      (index===round*2+1?'correct':'wrong')+'">'+nativeText(lines[index].text)+'</button>'+lessonPlayButton(lines[index].text,{compact:true,voice:1})+'</div>').join('')+'</div>'+
    '<p id="sceneFeedback" role="status"></p><div class="scene-round-confirmation" hidden>'+
    '<p lang="'+supportTag()+'">'+clean(reply.pt)+'</p><button type="button" data-scene-next>'+
    (round===3?routeLabel('Ver diálogo completo','See the full dialogue','Ver el diálogo completo'):
      routeLabel('Próxima rodada','Next round','Siguiente ronda'))+'</button></div></div>';
}
function renderSceneWorkshop(vocabulary,theme){
  const lines=scenePracticeLines(theme);
  return '<section class="lesson-card scene-workshop" aria-labelledby="workshopTitle">'+
    '<header>'+lessonPhotoFrame(photoForMoment(theme,0,'example',lines[0].pt),'lesson-workshop-photo')+'<div><h3 id="workshopTitle">'+
    routeLabel('Da escuta à conversa','From listening to conversation','De la escucha a la conversación')+'</h3><p>'+
    routeLabel('Ouça e use o contexto para montar uma conversa sobre o tema da lição.','Listen and use the context to build a conversation about the lesson topic.','Escucha y usa el contexto para construir una conversación sobre el tema de la lección.')+'</p></div></header>'+
    '<div class="workshop-grid"><div><h4>'+routeLabel('Reconheça a próxima fala','Recognize the next line','Reconoce la siguiente intervención')+'</h4>'+
    '<div id="scenePractice" data-scene-theme="'+theme+'">'+scenePracticeRound(lines,0)+'</div></div>'+
    (englishLessonPlan()?renderCompletedEnglishRoleplay(englishLessonPlan(),plannedEnglishContent()):renderSceneRoleplay(vocabulary,theme))+'</div></section>';
}
function handleSceneResponse(event){
  const button=event.target.closest('[data-scene-answer],[data-scene-next],[data-scene-restart]');
  if(!button)return;
  const panel=$('scenePractice');
  const roundPanel=panel.querySelector('[data-round]');
  if(button.hasAttribute('data-scene-answer')){
    const correct=button.dataset.sceneAnswer==='correct';
    const status=$('sceneFeedback');
    status.textContent=correct?
      routeLabel('Certo! Veja a tradução e siga para a próxima parte da conversa.','Correct! See the translation and continue the conversation.','¡Correcto! Mira la traducción y continúa la conversación.'):
      routeLabel('Essa fala responde a outra pergunta. Ouça novamente e procure a resposta que encaixa aqui.','That line answers a different question. Listen again and find the reply that fits here.','Esa intervención responde a otra pregunta. Escucha de nuevo y busca la respuesta que encaja aquí.');
    status.dataset.feedback=correct?'correct':'retry';
    if(correct){
      for(const choice of roundPanel.querySelectorAll('[data-scene-answer]'))choice.disabled=true;
      const confirmation=roundPanel.querySelector('.scene-round-confirmation');
      confirmation.hidden=false;
      confirmation.querySelector('button').focus();
    }
    return;
  }
  const theme=panel.dataset.sceneTheme;
  const lines=scenePracticeLines(theme);
  const next=button.hasAttribute('data-scene-restart')?0:Number(roundPanel.dataset.round)+1;
  stopLessonPlayback();
  panel.innerHTML=next<4?scenePracticeRound(lines,next):
    '<div data-playback-block><h5 class="scene-round-label" tabindex="-1">'+
    routeLabel('Diálogo completo · 4 rodadas concluídas','Full dialogue · 4 rounds complete','Diálogo completo · 4 rondas completadas')+'</h5>'+
    sectionPlayButton('scene-practice',routeLabel('Ouvir diálogo completo','Play the full dialogue','Escuchar el diálogo completo'))+
    lessonLinesMarkup(lines,'practice',{theme})+
    '<button type="button" data-scene-restart>'+routeLabel('Jogar de novo','Play again','Volver a jugar')+'</button></div>';
  panel.querySelector('.scene-round-label').focus();
}
