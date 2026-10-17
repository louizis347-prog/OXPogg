/* Pogglot · guarda de áudio: a voz do Poggie e o áudio do quadro nunca se atropelam.
   - Áudio automático do quadro (leitura, cena, conversa) espera o Poggie terminar de falar.
   - Toque do aluno (clique) tem prioridade: interrompe o Poggie e toca na hora. */
(function(){
  const POG={until:0,tok:0};
  const est=t=>400+String(t||'').length*68;           /* ~15 caracteres por segundo */
  const busy=()=>{try{return !!(window.speechSynthesis&&speechSynthesis.speaking)}catch(e){return false}};
  const orig=window.speak;
  if(typeof orig!=='function')return;
  window.speak=function(text,lang,btn,speaker,slow){
    if(speaker==='Poggie'){POG.tok++;POG.until=Date.now()+est(text);return orig.apply(this,arguments)}
    const user=!!(window.event&&window.event.isTrusted);
    if(user||Date.now()>=POG.until){if(user){POG.until=0;POG.tok++}return orig.apply(this,arguments)}
    const my=++POG.tok,args=arguments,self=this;let tries=0;
    (function wait(){
      if(my!==POG.tok)return;                           /* chegou algo mais novo: este pedido caducou */
      if((Date.now()>=POG.until&&!busy())||++tries>60){POG.until=0;orig.apply(self,args);return}
      setTimeout(wait,120);
    })();
  };
  const stop0=window.fxStopAudio;
  if(typeof stop0==='function')window.fxStopAudio=function(){
    const user=!!(window.event&&window.event.isTrusted);
    if(!user&&Date.now()<POG.until&&busy()){      /* parada automática do quadro: não corta o Poggie no meio da frase */
      try{clearTimeout(fxSeq.t);clearTimeout(fxSeq.t2)}catch(e){}
      window.__speakEnd=null;return}
    POG.tok++;return stop0.apply(this,arguments)};
  const close0=window.closePlayer;
  if(typeof close0==='function')window.closePlayer=function(){POG.tok++;POG.until=0;return close0.apply(this,arguments)};
})();
