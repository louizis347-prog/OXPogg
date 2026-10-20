/* Pogglot · paginador de quadros: nenhum quadro precisa de rolagem.
   Se o conteúdo do quadro não cabe na tela (celular ou PC), ele é dividido em "partes" (blocos que cabem juntos).
   O botão principal vira "Continuar ▶" até a última parte; na última, volta o botão e a lógica originais do quadro.
   Nada é cortado: todo o conteúdo e todas as práticas continuam lá, só em partes. */
(function(){
if(window.POG_PAGER===false)return;
const PG={step:null,pages:null,idx:0,timer:0,lastCta:null};
const $b=()=>document.querySelector('#pbody');
const css=document.createElement('style');
css.textContent=`#pbody{position:relative}.pg-dots{position:absolute;left:0;right:0;bottom:4px;display:flex;justify-content:center;gap:8px;pointer-events:none}.pg-dot{pointer-events:auto;width:10px;height:10px;padding:0;border:0;border-radius:99px;background:color-mix(in srgb,var(--az1,#1FAE9B) 28%,#fff);cursor:pointer;min-width:10px}.pg-dot.on{width:26px;background:var(--az1,#1FAE9B)}.pg-hide{display:none!important}.pg-in{animation:pgIn .28s both}@keyframes pgIn{from{opacity:.0;transform:translateY(8px)}to{opacity:1;transform:none}}.pg-part{margin-left:6px;padding:2px 8px;border-radius:99px;background:var(--azl,#E3F6F0);color:var(--azd,#0F6E62);font-weight:800;letter-spacing:.04em}`;
document.head.appendChild(css);
function dots(){
  const b=$b();if(!b)return;let d=b.querySelector(':scope>.pg-dots');
  if(!PG.pages){if(d)d.remove();return}
  if(!d){d=document.createElement('div');d.className='pg-dots';b.appendChild(d)}
  d.innerHTML=PG.pages.map((_,k)=>`<button type="button" class="pg-dot${k===PG.idx?' on':''}" data-k="${k}" aria-label="Parte ${k+1} de ${PG.pages.length}"></button>`).join('');
  d.querySelectorAll('.pg-dot').forEach(x=>x.onclick=()=>apply(+x.dataset.k,true));
}
const isHeader=el=>el.classList&&(el.classList.contains('eyebrow')||(el.tagName==='H2'&&el.classList.contains('fx-h')));
const more=()=>PG.pages&&PG.idx<PG.pages.length-1;
function partTag(){
  const st=PG.step;if(!st)return;const ey=st.querySelector(':scope>.eyebrow');if(!ey)return;
  let t=ey.querySelector('.pg-part');if(!PG.pages){if(t)t.remove();return}
  if(!t){t=document.createElement('span');t.className='pg-part';ey.appendChild(t)}
  t.textContent='parte '+(PG.idx+1)+'/'+PG.pages.length;
}
function apply(i,anim){
  PG.idx=i;const st=PG.step;if(!st||!PG.pages)return;
  PG.pages.forEach((pg,k)=>pg.forEach(el=>el.classList.toggle('pg-hide',k!==i)));
  document.querySelectorAll('#pstage .stage>.sc-open, #pstage>.sc-open').forEach(x=>x.classList.toggle('pg-hide',i<PG.pages.length-1));
  partTag();dots();const b=$b();if(b)b.scrollTop=0;
  if(anim)PG.pages[i].forEach(el=>{el.classList.remove('pg-in');void el.offsetWidth;el.classList.add('pg-in')});
  if(anim&&window.POG_LIFE)POG_LIFE.turn();
  refreshCta();
}
function refreshCta(){const c=PG.lastCta;if(!window.__pgCta||!c)return;window.__pgCta(c.l,c.en,c.am,true);if(PG.pages&&window.FOOT){FOOT.off=true;FOOT.upd()}}
function reset(){
  const st=PG.step;if(st)[...st.children].forEach(k=>k.classList.remove('pg-hide','pg-in'));
  PG.pages=null;PG.idx=0;partTag();dots();document.querySelectorAll('.sc-open.pg-hide').forEach(x=>x.classList.remove('pg-hide'));
}
function paginate(keepIdx,focus){
  const st=document.querySelector('#pstage .step'),b=$b();
  if(!st||!b||typeof P==='undefined'||!P||P.isTest)return;
  if(st!==PG.step){PG.step=st;PG.pages=null;PG.idx=0;PG.lastCta=PG.lastCta}
  const kids=[...st.children];kids.forEach(k=>k.classList.remove('pg-hide'));
  let margin=0;b.scrollTop=0;const fits=()=>{if(!margin)return b.scrollHeight<=b.clientHeight+1;const sr=document.querySelector('#pstage').getBoundingClientRect(),br=b.getBoundingClientRect();return sr.bottom<=br.bottom-margin+1};
  st.classList.remove('pg-compact');
  if(fits()){PG.pages=null;PG.idx=0;partTag();dots();refreshCta();return}
  st.classList.add('pg-compact');                       /* 2º passo: modo compacto (menos margens e fontes) */
  if(fits()){PG.pages=null;PG.idx=0;partTag();dots();refreshCta();return}
  let i=0;const header=[];while(i<kids.length&&isHeader(kids[i])){header.push(kids[i]);i++}
  const rest=kids.slice(i).filter(k=>k.getBoundingClientRect().height>0&&!k.classList.contains('az-media'));
  if(rest.length<2){PG.pages=null;return}
  const closing=st.classList.contains('done')||st.classList.contains('m2-wrap')||st.classList.contains('fx-wrap');
  let first=null;
  if(closing){
    const rc=rest.findIndex(k=>k.classList.contains('recap')||k.classList.contains('m2-bagh2')||k.classList.contains('m2-bag')||k.classList.contains('fx-recap'));
    if(rc>0)first=rest.slice(0,rc);
  }
  rest.forEach(k=>k.classList.add('pg-hide'));
  margin=26;                                          /* espaço para as bolinhas das partes */
  const pages=[];let shown=[];
  const todo=first?rest.slice(first.length):rest;
  if(first){first.forEach(k=>k.classList.remove('pg-hide'));pages.push(first);first.forEach(k=>k.classList.add('pg-hide'))}
  for(const k of todo){
    k.classList.remove('pg-hide');
    if(!fits()&&shown.length){
      shown.forEach(x=>x.classList.add('pg-hide'));pages.push(shown);shown=[];
    }
    shown.push(k);
  }
  if(shown.length)pages.push(shown);
  if(pages.length<2){kids.forEach(k=>k.classList.remove('pg-hide'));PG.pages=null;partTag();return}
  PG.pages=pages;
  let idx=keepIdx?Math.min(PG.idx,pages.length-1):0;
  if(focus){const f=pages.findIndex(pg=>pg.some(el=>el===focus||el.contains(focus)));if(f>=0)idx=f}
  apply(idx,false);
}
function schedule(keep,focus){clearTimeout(PG.timer);PG.timer=setTimeout(()=>{try{paginate(keep,focus)}catch(e){console.warn('pager',e)}},140)}
/* observa a troca de quadro e mudanças nos blocos do quadro */
function watch(){
  const st=document.querySelector('#pstage');if(!st||st._pgw)return;st._pgw=1;
  let stepObs=null;
  const bind=()=>{const s=st.querySelector('.step');if(!s)return;if(stepObs)stepObs.disconnect();
    stepObs=new MutationObserver(m=>{const added=m.flatMap(x=>[...x.addedNodes]).find(n=>n.nodeType===1&&!n.classList.contains('pg-hide'));schedule(true,added)});
    stepObs.observe(s,{childList:true})};
  new MutationObserver(()=>{const s=st.querySelector('.step');if(s!==PG.step){PG.step=s;PG.pages=null;PG.idx=0;bind();schedule(false);setTimeout(()=>{if(PG.step===s)schedule(true)},650);setTimeout(()=>{if(PG.step===s)schedule(true)},1500)}}).observe(st,{childList:true});
  bind();schedule(false);
}
/* intercepta o botão principal, voltar e a atualização do rótulo */
const _cta=window.cta;
if(typeof _cta==='function'){
  window.__pgCta=function(l,en,am,internal){const c=PG.lastCta||{};return _cta.call(this,more()?(c.en?'Continuar ▶':'Ver mais ▶'):l,more()?true:en,more()?true:am)};
  window.cta=function(l,en,am){PG.lastCta={l,en,am};return window.__pgCta(l,en,am)};
}
const _cc=window.ctaClick;
if(typeof _cc==='function')window.ctaClick=function(){if(typeof P!=='undefined'&&P&&!P.isTest&&more()){apply(PG.idx+1,true);return}return _cc.apply(this,arguments)};
const _bc=window.backClick;
if(typeof _bc==='function')window.backClick=function(){if(typeof P!=='undefined'&&P&&!P.isTest&&PG.pages&&PG.idx>0){apply(PG.idx-1,true);return}return _bc.apply(this,arguments)};
/* o player é criado a cada episódio: espera #pstage aparecer */
new MutationObserver(()=>{if(document.querySelector('#pstage'))watch()}).observe(document.body,{childList:true,subtree:false});
window.addEventListener('resize',()=>schedule(true));
window.POG_PAGER_DEBUG=PG;
})();
