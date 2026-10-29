/* Pogglot · "Ache no cenário" (pgfind): o aluno descobre a palavra pelo CONTEXTO da frase e toca o objeto no cenário completo.
   Sem figurinha isolada e sem a palavra à vista: a pista é uma frase com lacuna. */
(function(){
'use strict';
if(typeof FXR==='undefined'||typeof FX_KIND==='undefined'||!window.PogStage)return;
const H=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const q=(s,r)=>(r||document).querySelector(s);
const qa=(s,r)=>[...(r||document).querySelectorAll(s)];
FX_KIND.pgfind='practice';FX_LABEL.pgfind='Ache no cenário';
const POS=[[13,20],[38,16],[63,20],[87,16],[24,82],[50,86],[76,82]];
FXR.pgfind=function(f,st,n){
  const items=f.items||[],board=f.board||items.map(i=>i.e);
  let cur=0,hits=0,tries=0,done=false;
  const objs=board.map((e,i)=>`<button type="button" class="pf-o" data-e="${H(e)}" style="left:${POS[i%POS.length][0]}%;top:${POS[i%POS.length][1]}%">${e}</button>`).join('');
  st.innerHTML=`<div class="step fx ps-find">${fxKindBar(f,n)}<div class="ps-sh-h"><h2 class="fx-h">${H(f.title||'Ache no cenário')}</h2><span class="ps-count" id="pfc">0/${items.length}</span></div>
   <div class="pf-grid"><div class="pf-scene">${PogStage.stage({rs:f.rs,chars:f.chars,h:'scene',over:objs})}</div>
   <div class="pf-side"><div class="pf-clue" id="pfq"></div><div class="pf-fb" id="pfb" hidden></div></div></div></div>`;
  const clue=q('#pfq',st),fb=q('#pfb',st);
  const full=it=>it.s.replace('___',it.w);
  const show=()=>{
    const it=items[cur];tries=0;done=false;fb.hidden=true;
    qa('.pf-o',st).forEach(b=>b.classList.remove('ok','no','off'));
    clue.innerHTML=`<small>Que objeto completa a frase?</small><p class="pf-s">${H(it.s).replace('___','<u class="pf-b">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u>')}</p><button type="button" class="ps-btn" id="pfl">🔊 Ouvir a frase</button>`;
    q('#pfl',st).onclick=()=>fxSay(it.s.replace('___','hmm'),null,false);
    P.fx.cta=null;cta('Toque no objeto certo',false);
  };
  qa('.pf-o',st).forEach(b=>b.onclick=()=>{
    if(done)return;const it=items[cur];
    if(b.dataset.e===it.e){
      done=true;b.classList.add('ok');if(!tries){hits++;P.score++}
      clue.querySelector('.pf-s').innerHTML=H(it.s).replace('___','<mark>'+H(it.w)+'</mark>');
      fb.hidden=false;fb.innerHTML=`<b>${H(it.w)}</b> ${it.pt?'· '+H(it.pt):''}`;
      try{beep(true)}catch(e){}fxSay(full(it),null,false);
      q('#pfc',st).textContent=(cur+1)+'/'+items.length;
      if(cur<items.length-1)cta('Próxima frase',true,true),P.fx.cta=()=>{cur++;show();return true};
      else{P.fx.cta=null;cta('Continuar',true,true);say(hits===items.length?'Tudo certo! Muito bem!':'Bom trabalho!',hits===items.length?'happy':'')}
    }else{tries++;b.classList.add('no');try{beep(false)}catch(e){}setTimeout(()=>b.classList.remove('no'),500)}
  });
  show();
  say(f.say||'Descubra pela frase qual objeto está faltando.');
};
const _ft=window.fxTotal;
window.fxTotal=function(e){let n=_ft(e);(e.fr||[]).forEach(f=>{if(f.k==='pgfind')n+=(f.items||[]).length});return n};
})();
