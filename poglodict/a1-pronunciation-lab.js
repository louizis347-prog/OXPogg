let a1Playback=null;
const a1MouthPoses={
  rest:[20,2,2],closed:[22,0,1],open:[17,8,23],round:[10,8,15],
  wide:[27,4,10],small:[13,5,10],relaxed:[19,3,7],
  teeth:[22,4,5],tongue:[21,7,12],alveolar:[22,5,10]
};
const a1PoseLabels={
  rest:'Posição neutra',closed:'Lábios juntos',open:'Mandíbula aberta',round:'Lábios arredondados',
  wide:'Lábios mais abertos para os lados',small:'Abertura menor',relaxed:'Lábios soltos',
  teeth:'Dentes próximos ao lábio inferior',tongue:'Ponta da língua entre os dentes',
  alveolar:'Ponta da língua atrás dos dentes superiores'
};
function a1MouthPath([width,upper,lower]){
  return 'M'+(110-width)+' 122 Q110 '+(122-upper*2)+' '+(110+width)+' 122 Q110 '+(122+lower*2)+' '+(110-width)+' 122Z';
}
function a1PronunciationLabRow(){return englishLessonPlan()?a1PronunciationLab[unit]:null;}
function a1Speaker(){
  return '<svg class="a1-speaker" viewBox="0 0 220 180" aria-hidden="true">'+
    '<circle cx="110" cy="89" r="78" fill="#dcece0"/><path d="M42 180c9-31 36-44 68-44s59 13 68 44" fill="#2e6856"/>'+
    '<path d="M93 135h34v27q-17 13-34 0z" fill="#b97554"/>'+
    '<ellipse cx="65" cy="100" rx="12" ry="15" fill="#cb8e67"/><ellipse cx="155" cy="100" rx="12" ry="15" fill="#cb8e67"/>'+
    '<path d="M67 81q0-41 43-45t43 45v22q0 49-43 52-43-3-43-52z" fill="#d49a75"/>'+
    '<path d="M61 88Q48 41 84 30q38-19 65 4 21 11 12 53l-12-13-4-24q-30 22-66 12l-5 18z" fill="#263c39"/>'+
    '<path d="M80 86q9-6 17 0m26 0q9-6 17 0" fill="none" stroke="#61403a" stroke-width="2" stroke-linecap="round"/>'+
    '<ellipse cx="89" cy="95" rx="2.7" ry="3.4" fill="#202820"/><ellipse cx="132" cy="95" rx="2.7" ry="3.4" fill="#202820"/>'+
    '<path d="M111 96l-5 13 7 1" fill="none" stroke="#a6614f" stroke-width="2" stroke-linecap="round"/>'+
    '<path data-a1-mouth d="'+a1MouthPath(a1MouthPoses.rest)+'" fill="#6d3140" stroke="#733942" stroke-width="2"/>'+
    '<path class="a1-speaker-teeth" d="M93 121q17-5 34 0l-3 5h-28z" fill="#fff4df"/>'+
    '<path class="a1-speaker-tongue" d="M100 128q10-5 20 0l-2 6h-16z" fill="#ef9b9e"/>'+
    '<path d="M167 102q8 3 10 9m-4-20q13 3 18 13" class="a1-speaker-sound" fill="none" stroke="#37795c" stroke-width="2.5" stroke-linecap="round"/>'+
    '</svg><svg class="a1-mouth-closeup" viewBox="78 105 64 44" aria-hidden="true">'+
    '<rect x="78" y="105" width="64" height="44" rx="10" fill="#d49a75"/>'+
    '<path data-a1-mouth d="'+a1MouthPath(a1MouthPoses.rest)+'" fill="#4f2231" stroke="#843a4b" stroke-width="2"/>'+
    '<path class="a1-speaker-teeth" d="M93 121q17-6 34 0l-3 5h-28z" fill="#fff4df"/>'+
    '<path class="a1-speaker-tongue" d="M100 126q10-7 20 0l-2 6h-16z" fill="#ef9b9e"/></svg>';
}
function renderA1Pronunciation(row){
  const [title,tip,clips]=row;
  return '<section class="lesson-card a1-pronunciation" id="pronunciationSection" aria-labelledby="pronunciationTitle">'+
    '<div class="a1-pronunciation-demo"><div class="a1-speaker-frame" data-mouth-pose="rest">'+a1Speaker()+'</div>'+
    '<p class="a1-current-word" data-a1-word lang="en-US">'+clean(clips[0][0])+'</p>'+
    '<p class="a1-mouth-label" data-a1-pose>Posição neutra</p>'+
    '<div class="a1-sound-track" aria-hidden="true"><div data-a1-progress></div></div>'+
    '<p class="meta">Observe a boca em close. Nas consoantes finais, repare se os lábios fecham, se a língua muda de posição ou se o ar continua saindo.</p></div>'+
    '<div class="a1-pronunciation-controls"><h3 id="pronunciationTitle">Pronúncia em ação</h3><h4>'+clean(title)+'</h4><p>'+clean(tip)+'</p>'+
    '<p>Escolha um exemplo para ouvir e observar. Em seguida, tente dizer a palavra no mesmo ritmo.</p>'+
    '<div class="a1-word-buttons">'+clips.map(([word],i)=>'<button type="button" data-a1-play="'+i+'" aria-pressed="'+(i===0)+'">'+icon('speaker')+nativeText(word)+'</button>').join('')+'</div>'+
    '<div class="controls a1-pronunciation-tools"><button type="button" data-a1-slow>Ouvir devagar</button><button type="button" data-a1-step>Ver posição por posição</button>'+
    '<button type="button" data-a1-stop>Parar áudio</button></div><p class="meta" role="status" data-a1-status></p>'+
    '<audio class="a1-pronunciation-audio" preload="none"></audio>'+
    '<div class="a1-pronunciation-quiz"><h4>Qual você ouviu?</h4><p>Ouça um exemplo da lista e escolha o que ouviu.</p><button type="button" data-a1-challenge>Ouvir desafio</button>'+
    '<div class="a1-word-buttons" data-a1-answers hidden>'+clips.map(([word],i)=>'<button type="button" data-a1-guess="'+i+'">'+nativeText(word)+'</button>').join('')+
    '</div><p data-a1-feedback role="status"></p></div></div></section>';
}
function setA1Mouth(panel,pose,geometry=a1MouthPoses[pose]){
  const frame=panel.querySelector('.a1-speaker-frame');
  if(frame.dataset.mouthPose!==pose){
    frame.dataset.mouthPose=pose;
    panel.querySelector('[data-a1-pose]').textContent=a1PoseLabels[pose];
  }
  const path=a1MouthPath(geometry);
  for(const mouth of frame.querySelectorAll('[data-a1-mouth]'))mouth.setAttribute('d',path);
}
function stopA1Pronunciation(completed=false){
  const state=a1Playback;
  if(!state)return;
  a1Playback=null;
  cancelAnimationFrame(state.frame);
  state.audio.onended=null;
  state.audio.onerror=null;
  state.audio.pause();
  setA1Mouth(state.panel,'rest');
  state.panel.classList.remove('is-a1-playing');
  state.progress.style.width=completed?'100%':'0%';
  state.status.textContent=completed?'Áudio completo. Tente repetir até o último som.':'';
}
function updateA1Playback(state){
  if(a1Playback!==state)return;
  const {audio,panel,clip,progress}=state;
  if(!audio.paused){
    const time=audio.currentTime;
    const motions=clip[2];
    const i=motions.findLastIndex(([start])=>start<=time);
    const [start,pose]=motions[i]||[0,'rest'];
    const previous=a1MouthPoses[motions[i-1]?.[1]||'rest'];
    const amount=Math.min(1,Math.max(0,(time-start)/.038));
    const geometry=a1MouthPoses[pose].map((value,n)=>previous[n]+(value-previous[n])*amount);
    setA1Mouth(panel,pose,geometry);
    if(audio.duration>0)progress.style.width=(100*time/audio.duration)+'%';
  }
  state.frame=requestAnimationFrame(()=>updateA1Playback(state));
}
function playA1Clip(panel,clip,rate){
  stopLessonPlayback();
  window.speechSynthesis?.cancel();
  stopA1Pronunciation();
  const audio=panel.querySelector('audio');
  const status=panel.querySelector('[data-a1-status]');
  const progress=panel.querySelector('[data-a1-progress]');
  const state={audio,panel,clip,status,progress,frame:0};
  a1Playback=state;
  progress.style.width='0%';
  panel.classList.add('is-a1-playing');
  status.textContent=rate===1?'Reproduzindo…':'Reproduzindo devagar…';
  const source='a1-audio/'+clip[1]+'.mp3';
  if(audio.getAttribute('src')!==source)audio.setAttribute('src',source);
  else audio.currentTime=0;
  audio.playbackRate=rate;
  audio.preservesPitch=true;
  const fail=()=>{
    if(a1Playback!==state)return;
    stopA1Pronunciation();
    status.textContent='Não foi possível reproduzir o áudio. Tente novamente.';
  };
  audio.onended=()=>{if(a1Playback===state)stopA1Pronunciation(true);};
  audio.onerror=fail;
  try{Promise.resolve(audio.play()).then(()=>updateA1Playback(state),fail);}
  catch{fail();}
}
function selectA1Word(panel,index,clip){
  panel.dataset.a1Selected=String(index);
  panel.dataset.a1StepIndex='-1';
  const label=panel.querySelector('[data-a1-word]');
  label.setAttribute('lang','en-US');
  label.textContent=clip[0];
  for(const button of panel.querySelectorAll('[data-a1-play]'))button.setAttribute('aria-pressed',String(Number(button.dataset.a1Play)===index));
}
function handleA1PronunciationClick(event){
  const button=event.target.closest('button');
  const panel=button?.closest('.a1-pronunciation');
  if(!panel)return false;
  const clips=a1PronunciationLabRow()[2];
  const selected=Number(panel.dataset.a1Selected||0);
  const feedback=panel.querySelector('[data-a1-feedback]');
  if(button.hasAttribute('data-a1-play')){
    const index=Number(button.dataset.a1Play);
    selectA1Word(panel,index,clips[index]);
    playA1Clip(panel,clips[index],1);
  }else if(button.hasAttribute('data-a1-slow')){
    selectA1Word(panel,selected,clips[selected]);
    playA1Clip(panel,clips[selected],.72);
  }else if(button.hasAttribute('data-a1-stop')){
    stopA1Pronunciation();
    panel.querySelector('[data-a1-status]').textContent='Áudio interrompido.';
  }else if(button.hasAttribute('data-a1-step')){
    stopA1Pronunciation();
    const clip=clips[selected];
    const poses=clip[2].filter(([,pose],i,steps)=>pose!=='rest'&&pose!==steps[i-1]?.[1]);
    const index=(Number(panel.dataset.a1StepIndex??-1)+1)%Math.max(1,poses.length);
    panel.dataset.a1StepIndex=String(index);
    const label=panel.querySelector('[data-a1-word]');
    label.setAttribute('lang','en-US');
    label.textContent=clip[0];
    setA1Mouth(panel,poses[index]?.[1]||'rest');
    panel.querySelector('[data-a1-status]').textContent='Posição '+(index+1)+' de '+Math.max(1,poses.length)+'.';
  }else if(button.hasAttribute('data-a1-challenge')){
    const previous=panel.dataset.a1ChallengeIndex;
    const index=previous===undefined?unit%clips.length:(Number(previous)+1)%clips.length;
    panel.dataset.a1ChallengeIndex=String(index);
    panel.querySelector('[data-a1-answers]').hidden=false;
    panel.querySelector('[data-a1-word]').textContent='Som do desafio';
    panel.querySelector('[data-a1-word]').removeAttribute('lang');
    feedback.textContent='';
    for(const choice of panel.querySelectorAll('[data-a1-guess]'))choice.disabled=false;
    playA1Clip(panel,clips[index],1);
  }else if(button.hasAttribute('data-a1-guess')){
    const index=Number(panel.dataset.a1ChallengeIndex);
    if(Number(button.dataset.a1Guess)!==index){feedback.textContent='Tente outra vez. Preste atenção aos sons da gravação e tente de novo.';return true;}
    feedback.textContent='Certo! Ouça a palavra devagar e repita.';
    selectA1Word(panel,index,clips[index]);
    for(const choice of panel.querySelectorAll('[data-a1-guess]'))choice.disabled=true;
    playA1Clip(panel,clips[index],.72);
  }else return false;
  return true;
}

document.addEventListener('visibilitychange',()=>{
  if(!document.hidden||!a1Playback)return;
  const status=a1Playback.panel.querySelector('[data-a1-status]');
  stopA1Pronunciation();
  status.textContent='Áudio interrompido.';
});
