let lessonPlayback=null;
let lessonRate=.88;
function audioMessage(text){
  const status=$('lessonAudioStatus');
  if(status)status.textContent=text;
}
function lessonAudioBar(){
  return '<div class="lesson-audio-bar"><div><strong>'+routeLabel('Áudio da lição','Lesson audio','Audio de la lección')+'</strong>'+
    '<label for="lessonAudioRate">'+routeLabel('Velocidade','Speed','Velocidad')+'</label>'+
    '<select id="lessonAudioRate"><option value="0.88"'+(lessonRate===.88?' selected':'')+'>'+routeLabel('Normal','Normal','Normal')+'</option>'+
    '<option value="0.65"'+(lessonRate===.65?' selected':'')+'>'+routeLabel('Lenta','Slow','Lenta')+'</option></select>'+
    '<button type="button" data-lesson-audio-stop disabled>'+routeLabel('Parar','Stop','Detener')+'</button></div>'+
    '<p id="lessonAudioStatus" class="meta" role="status"></p></div>';
}
function lessonPlayButton(text,{label,voice=0,compact=false,line=false}={}){
  if(screen==='licao')text=lessonLevelText(text);
  const caption=label||ui('Ouvir');
  return '<button type="button" class="lesson-play'+(compact?' lesson-play-compact':'')+'" data-lesson-say="'+clean(text)+
    '" data-lesson-voice="'+voice+'"'+(line?' data-line-audio':'')+' aria-label="'+clean(caption+' · '+text)+'">'+
    icon('speaker')+(compact?'<span class="lesson-play-caption">'+clean(caption)+'</span>':' '+clean(caption))+'</button>';
}
function sectionPlayButton(kind,label){
  return '<button type="button" class="lesson-play section-play" data-lesson-play-group="'+kind+'">'+icon('speaker')+' '+clean(label)+'</button>';
}
function clearLessonHighlight(state){
  state?.row?.classList.remove('is-playing');
  state?.button?.removeAttribute('aria-current');
}
function stopLessonPlayback(announce=false){
  const previous=lessonPlayback;
  lessonPlayback=null;
  clearLessonHighlight(previous);
  if(previous)window.speechSynthesis?.cancel();
  const stop=document.querySelector('#licao [data-lesson-audio-stop]');
  if(stop)stop.disabled=true;
  if(announce)audioMessage(routeLabel('Reprodução parada.','Playback stopped.','Reproducción detenida.'));
}
function playLessonSelection(buttons,label=''){
  stopLessonPlayback();
  if(!buttons.length)return;
  const state={row:null,button:null};
  const locale=languages[lang][2];
  lessonPlayback=state;
  const stop=document.querySelector('#licao [data-lesson-audio-stop]');
  if(stop)stop.disabled=false;
  const play=index=>{
    if(lessonPlayback!==state)return;
    clearLessonHighlight(state);
    if(index>=buttons.length){
      stopLessonPlayback();
      audioMessage(routeLabel('Reprodução concluída.','Playback finished.','Reproducción finalizada.'));
      return;
    }
    const button=buttons[index];
    if(!button?.isConnected){stopLessonPlayback();return;}
    state.button=button;
    state.row=button.closest('[data-audio-line]');
    state.row?.classList.add('is-playing');
    button.setAttribute('aria-current','true');
    audioMessage(label?label+' · '+(index+1)+'/'+buttons.length:routeLabel('Reproduzindo áudio…','Playing audio…','Reproduciendo audio…'));
    const fail=()=>{
      if(lessonPlayback!==state)return;
      stopLessonPlayback();
      audioMessage(routeLabel('Instale uma voz para este idioma no navegador ou no dispositivo.',
        'Install a voice for this language on your browser or device.',
        'Instala una voz de este idioma en el navegador o dispositivo.'));
    };
    if(!speech(button.dataset.lessonSay,lessonRate,locale,{voiceIndex:Number(button.dataset.lessonVoice)||0,
      cancelFirst:index===0,onend:()=>play(index+1),onerror:fail}))fail();
  };
  play(0);
}
function lessonWordTokens(text){
  const locale=languages[lang][2];
  const word=t=>t.replace(/^[’'-]+|[’'-]+$/g,'');
  let tokens;
  if(typeof Intl.Segmenter==='function'){
    tokens=[...new Intl.Segmenter(locale,{granularity:'word'}).segment(text)].filter(segment=>segment.isWordLike).map(segment=>segment.segment);
  }else{
    tokens=text.match(/[\p{Script=Han}\p{Script=Hiragana}\p{Script=Katakana}]|[\p{L}\p{M}\p{N}]+(?:['’\-][\p{L}\p{M}\p{N}]+)*/gu)||[];
  }
  return tokens.map(word).filter(Boolean);
}
function lessonWordPicker(text,voice=0){
  text=lessonLevelText(text);
  return '<details class="line-word-picker" data-lesson-token-source="'+clean(text)+'" data-token-voice="'+voice+'"><summary>'+
    routeLabel('Ouvir palavra por palavra','Listen word by word','Escuchar palabra por palabra')+'</summary><div class="line-word-buttons"></div></details>';
}
function bindLessonAudio(){
  lessonRate=read('lesson-audio-rate',.88)===.65?.65:.88;
  const region=$('licao');
  region.addEventListener('change',event=>{
    if(event.target.id!=='lessonAudioRate')return;
    lessonRate=event.target.value==='0.65'?.65:.88;
    write('lesson-audio-rate',lessonRate);
  });
  region.addEventListener('click',event=>{
    const button=event.target.closest('button');
    if(!button)return;
    if(button.dataset.lessonSay!==undefined){playLessonSelection([button]);return;}
    if(button.dataset.lessonPlayGroup){
      const group=button.closest('[data-playback-block]');
      if(group)playLessonSelection([...group.querySelectorAll('[data-line-audio]')],button.textContent.trim());
      return;
    }
    if(button.hasAttribute('data-lesson-audio-stop'))stopLessonPlayback(true);
  });
  region.addEventListener('toggle',event=>{
    const details=event.target;
    if(!details.open||details.dataset.lessonTokenSource===undefined)return;
    const slot=details.querySelector('.line-word-buttons');
    if(slot.hasChildNodes())return;
    const voice=Number(details.dataset.tokenVoice)||0;
    slot.innerHTML=lessonWordTokens(details.dataset.lessonTokenSource).map(word=>
      '<button type="button" class="line-word" data-lesson-voice="'+voice+'" data-lesson-say="'+clean(word)+'">'+nativeText(word)+'</button>').join('');
    if(!slot.hasChildNodes())slot.textContent=routeLabel('A frase pode ser ouvida inteira.','You can listen to the full line.','Puedes escuchar la frase completa.');
  },true);
}
