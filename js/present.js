/* Pogglot · lupa (zoom do conteúdo) e modo apresentação (tela expandida) do player. */
(function(){
'use strict';
if(typeof render!=='function'||typeof closePlayer!=='function')return;
const ZL=[1,1.15,1.3,1.5,1.75];let zi=0;
try{zi=Math.max(0,Math.min(ZL.length-1,(+localStorage.getItem('pg:zi'))||0))}catch(e){}
const pl=()=>document.getElementById('player');
function apply(){
  const p=pl();if(!p)return;p.style.setProperty('--pgz',ZL[zi]);
  const b=document.getElementById('ps-zoom');if(b){b.classList.toggle('on',zi>0);const l=b.querySelector('b');if(l)l.textContent=Math.round(ZL[zi]*100)+'%'}
}
function toast(t){
  const old=document.querySelector('.ps-ztoast');if(old)old.remove();
  const d=document.createElement('div');d.className='ps-ztoast';d.textContent=t;document.body.appendChild(d);setTimeout(()=>d.remove(),1100);
}
function setWide(on){
  const p=pl();if(!p)return;p.classList.toggle('ps-wide',!!on);
  const b=document.getElementById('ps-full');if(b){b.classList.toggle('on',!!on);b.textContent=on?'⤡':'⛶';b.title=on?'Sair da tela expandida':'Expandir a tela'}
  try{
    if(on&&p.requestFullscreen&&!document.fullscreenElement)p.requestFullscreen({navigationUI:'hide'}).catch(()=>{});
    if(!on&&document.fullscreenElement&&document.exitFullscreen)document.exitFullscreen().catch(()=>{});
  }catch(e){}
}
function ensure(){
  const p=pl();if(!p)return;const h=p.querySelector('.p-head');if(!h||h.querySelector('.ps-hbtns'))return;
  h.insertAdjacentHTML('beforeend','<div class="ps-hbtns"><button type="button" id="ps-zoom" class="ps-hbtn z" aria-label="Ampliar o conteúdo (lupa)" title="Ampliar o conteúdo">🔍<b>100%</b></button><button type="button" id="ps-full" class="ps-hbtn" aria-label="Expandir a tela" title="Expandir a tela">⛶</button></div>');
  h.querySelector('#ps-zoom').onclick=()=>{zi=(zi+1)%ZL.length;try{localStorage.setItem('pg:zi',zi)}catch(e){}apply();toast('🔍 '+Math.round(ZL[zi]*100)+'%')};
  h.querySelector('#ps-full').onclick=()=>setWide(!p.classList.contains('ps-wide'));
}
const _r=window.render;
window.render=function(){const o=_r.apply(this,arguments);try{ensure();apply()}catch(e){}return o};
document.addEventListener('fullscreenchange',()=>{if(!document.fullscreenElement){const p=pl();if(p&&p.classList.contains('ps-wide'))setWide(false)}});
const _c=window.closePlayer;
window.closePlayer=function(){try{if(document.fullscreenElement)document.exitFullscreen()}catch(e){}return _c.apply(this,arguments)};
})();
