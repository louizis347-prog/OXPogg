let focusedLessonPanel=null;
function lessonFocusGlyph(expanded){
  const path=expanded?'M9 4v5H4m11-5v5h5M9 20v-5H4m11 5v-5h5':'M9 4H4v5m11-5h5v5M4 15v5h5m11-5v5h-5';
  return '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="'+path+'"/></svg>';
}
function lessonFocusLabel(expanded){
  return expanded?routeLabel('Sair da tela cheia','Exit full screen','Salir de pantalla completa'):
    routeLabel('Ampliar bloco','Expand section','Ampliar sección');
}
function lessonPreviewActions(label){
  return '<span class="lesson-preview-actions"><button type="button" class="lesson-preview-expand" data-focus-preview aria-label="'+
    clean(lessonFocusLabel(false)+' · '+label)+'" title="'+clean(lessonFocusLabel(false))+'">'+lessonFocusGlyph(false)+
    '<span>'+routeLabel('Tela cheia','Full screen','Pantalla completa')+'</span></button>'+
    '<span class="lesson-disclosure-indicator" aria-hidden="true"></span></span>';
}
function lessonFocusToolbar(){
  return '<div class="lesson-panel-toolbar"><strong class="lesson-focus-title" hidden></strong><button type="button" class="lesson-focus-stop" data-focus-stop hidden>'+
    routeLabel('Parar áudio','Stop audio','Detener audio')+'</button><button type="button" class="lesson-focus-button" data-lesson-focus aria-pressed="false">'+
    lessonFocusGlyph(false)+clean(lessonFocusLabel(false))+'</button></div>';
}
function closeLessonFocus(restore=true){
  if(!focusedLessonPanel)return;
  const {panel,trigger,opener,inert}=focusedLessonPanel;
  focusedLessonPanel=null;
  if(document.fullscreenElement===panel)document.exitFullscreen?.().catch(()=>{});
  document.body.classList.remove('lesson-focus-active');
  panel.classList.remove('is-lesson-focused');
  for(const sibling of inert)sibling.removeAttribute('inert');
  panel.removeAttribute('role');
  panel.removeAttribute('aria-modal');
  panel.removeAttribute('aria-label');
  trigger.setAttribute('aria-pressed','false');
  trigger.innerHTML=lessonFocusGlyph(false)+clean(lessonFocusLabel(false));
  panel.querySelector('[data-focus-stop]').hidden=true;
  panel.querySelector('.lesson-focus-title').hidden=true;
  if(restore&&opener.isConnected)opener.focus({preventScroll:true});
}
function openLessonFocus(panel,opener){
  if(focusedLessonPanel?.panel===panel){closeLessonFocus();return;}
  closeLessonFocus(false);
  panel.open=true;
  const inert=[];
  for(let node=panel;node&&node!==document.body;node=node.parentElement){
    for(const sibling of node.parentElement.children){
      if(sibling!==node&&!sibling.hasAttribute('inert')){
        inert.push(sibling);
        sibling.setAttribute('inert','');
      }
    }
  }
  const trigger=panel.querySelector('[data-lesson-focus]');
  focusedLessonPanel={panel,trigger,opener,inert,native:false};
  panel.classList.add('is-lesson-focused');
  document.body.classList.add('lesson-focus-active');
  panel.setAttribute('role','dialog');
  panel.setAttribute('aria-modal','true');
  const label=panel.querySelector('summary strong').textContent.trim();
  panel.setAttribute('aria-label',label);
  const title=panel.querySelector('.lesson-focus-title');
  title.textContent=label;
  title.hidden=false;
  panel.querySelector('[data-focus-stop]').hidden=false;
  trigger.setAttribute('aria-pressed','true');
  trigger.innerHTML=lessonFocusGlyph(true)+clean(lessonFocusLabel(true));
  panel.scrollTop=0;
  trigger.focus({preventScroll:true});
  // When the host disallows the Fullscreen API, the fixed in-page view still fills the viewport.
  const session=focusedLessonPanel;
  if(typeof panel.requestFullscreen==='function'){
    try{
      Promise.resolve(panel.requestFullscreen()).then(()=>{
        if(focusedLessonPanel!==session&&document.fullscreenElement===panel)document.exitFullscreen?.().catch(()=>{});
      }).catch(()=>{});
    }catch{}
  }
}
function setupLessonFocus(){
  $('licao').addEventListener('click',event=>{
    const stop=event.target.closest('[data-focus-stop]');
    if(stop){
      stopA1Pronunciation();
      stopLessonPlayback(true);
      window.speechSynthesis?.cancel();
      return;
    }
    const trigger=event.target.closest('[data-lesson-focus],[data-focus-preview]');
    if(trigger){
      event.preventDefault();
      openLessonFocus(trigger.closest('.lesson-disclosure'),trigger);
    }
  });
  document.addEventListener('fullscreenchange',()=>{
    if(!focusedLessonPanel)return;
    if(document.fullscreenElement===focusedLessonPanel.panel)focusedLessonPanel.native=true;
    else if(focusedLessonPanel.native)closeLessonFocus();
  });
  document.addEventListener('keydown',event=>{
    if(!focusedLessonPanel)return;
    if(event.key==='Escape'){
      event.preventDefault();
      closeLessonFocus();
    }
    if(event.key!=='Tab')return;
    const controls=[...focusedLessonPanel.panel.querySelectorAll('button:not([disabled]),a[href],input:not([disabled]),textarea:not([disabled]),select:not([disabled]),summary')].
      filter(control=>control.getClientRects().length);
    if(!controls.length)return;
    const edge=event.shiftKey?controls[0]:controls.at(-1);
    if(document.activeElement===edge){
      event.preventDefault();
      (event.shiftKey?controls.at(-1):controls[0]).focus();
    }
  });
}
