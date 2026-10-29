/* Pogglot · palco ilustrado dos episódios no modelo "padrão do dia" (episódios com pilot:1).
   Cena pintada inteira (sem cortes) + personagens desenhados + balão de fala. Também define o quadro "hotscene" (cena clicável). */
(function(){
'use strict';
if(typeof FXR==='undefined'||typeof FX_KIND==='undefined')return;
const H=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const q=(s,r)=>(r||document).querySelector(s);
let UID=0;
const tts=(t,slow)=>{try{fxSay(String(t),null,slow)}catch(e){}};
const frag=h=>{const t=document.createElement('template');t.innerHTML=h;return t.content};
const bg=k=>{try{return window.RS&&RS[k]?RS[k]('pg'+(++UID)):''}catch(e){return ''}};
const chars=list=>(list||[]).map(c=>{
  const id=c[0],x=c[1]==null?50:c[1],fl=c[2]?' fl':'',sc=c[3]||1;
  return `<span class="ps-c${fl}" data-c="${id}" style="left:${x}%;--s:${sc}">${window.PogChars?PogChars.svg(id):''}</span>`}).join('');
/* palco: {rs, chars:[[id, x%, espelhar?, escala]], h:'cover'|'scene'|'strip', hot:[…]} */
function stage(o){
  return `<div class="ps-stage ${o.h||'strip'}"><div class="ps-stage-bk">${bg(o.rs||'street')}</div><div class="ps-chars">${chars(o.chars)}</div>${o.over||''}</div>`;
}
function bubble(b){
  if(!b)return '';
  return `<button type="button" class="ps-say" data-say="${H(b[1])}"><span class="ps-say-who">${H(b[0])}</span><b>${H(b[1])}</b>${b[2]?`<small>${H(b[2])}</small>`:''}<i aria-hidden="true">🔊</i></button>`;
}
/* fala do personagem: vai para a barra de baixo, junto com a fala do Poggie, e não dentro do quadro */
function footLine(b){
  const foot=document.querySelector('#player .p-foot');if(!foot)return;
  let el=foot.querySelector('#pcl');
  if(!el){el=document.createElement('div');el.id='pcl';el.className='pcl';foot.insertBefore(el,foot.firstChild)}
  if(!b||!b[1]){el.hidden=true;el.innerHTML='';return}
  el.hidden=false;
  el.innerHTML=`<button type="button" class="pcl-b" data-say="${H(b[1])}"><span class="pcl-who">${H(b[0])}</span><b>${H(b[1])}</b>${b[2]?`<small>${H(b[2])}</small>`:''}<i aria-hidden="true">🔊</i></button>`;
  el.querySelector('.pcl-b').onclick=()=>tts(b[1]);
}
function bindBubble(root){
  root.querySelectorAll('.ps-say').forEach(b=>b.onclick=()=>tts(b.dataset.say));
}
/* aplica o palco no quadro já renderizado */
function decorate(step,f,e){
  try{
    if(f.k!=='combo')footLine(null);
    const host=step.parentNode;if(host){host._pgf=f;host._pge=e;if(!host._pgo){host._pgo=new MutationObserver(()=>{try{
      if(!P||!P.e||P.e!==host._pge||!P.e.pilot||!/^fx\d+$/.test(P.steps[P.i]||''))return;
      const sp=host.querySelector('.step');if(sp&&!sp.querySelector('.ps-stage'))decorate(sp,host._pgf,host._pge)}catch(x){}});host._pgo.observe(host,{childList:true})}}
    const main=e.stage||{};const mk=(h,extra)=>Object.assign({rs:f.rs||main.rs,chars:f.chars||main.chars,h},extra||{});
    if(f.k==='cover'){
      const sc=step.querySelector('.az-scene');
      const st=stage({rs:f.stage&&f.stage.rs||main.rs,chars:f.stage&&f.stage.chars||main.chars,h:'cover',
        over:f.obra?`<span class="ps-obra">📖 ${H(f.obra)}</span>`:''});
      if(sc){sc.innerHTML=st;sc.classList.add('ps-cover');try{if(window.PogObra)PogObra.coverFix(sc,e)}catch(_){}}
      const hero=step.querySelector('.az-hero');
      if(hero&&f.gancho&&!hero.querySelector('.ps-say')){hero.insertAdjacentHTML('beforeend',bubble(Array.isArray(f.gancho)?f.gancho:['Referência de hoje',String(f.gancho)]));bindBubble(hero)}
      return;
    }
    step.classList.add('ps-2col');
    if(/^(hotscene|pgscene|pgrule|pgspeak|combo)$/.test(f.k))return;
    if(f.k==='wrap'){
      const hero=step.querySelector('.wr-hero');if(!hero||step.querySelector('.ps-sticker'))return;
      const s=f.sticker||{};
      hero.insertAdjacentHTML('afterend',`<div class="ps-sticker"><div class="ps-sticker-in">${stage({rs:s.rs||main.rs,chars:s.chars||main.chars,h:'sticker'})}<div class="ps-sticker-t"><small>Figurinha desbloqueada</small><b>${H(s.title||'')}</b><span>${H(s.sub||'')}</span></div></div></div>`);
      const nx=step.querySelector('.fx-next');if(nx&&PogStage.nextCard){const c=PogStage.nextCard();if(c)nx.outerHTML=c}
      return;
    }
    if(step.querySelector('.ps-stage'))return;
    const h=f.avatar?'avatar':(f.stageH||'strip');
    const html=`<div class="ps-top">${stage(mk(h))}</div>`;
    const anchor=step.querySelector('.fx-h')||step.firstElementChild;
    if(anchor&&anchor.parentNode===step)anchor.before(frag(html));else step.prepend(frag(html));
    const top=step.querySelector('.ps-top');if(top)bindBubble(top);footLine(f.bubble);
  }catch(x){if(window.console)console.warn('pgstage',x)}
}
window.PogStage={stage,bubble,decorate,bindBubble,footLine};
const spk2=()=>(typeof spk!=='undefined'?spk:'🔊');

/* ---------- quadro: cena clicável ---------- */
FX_KIND.hotscene='story';FX_LABEL.hotscene='Explore a cena';
FXR.hotscene=function(f,st,n){
  const e=P.e,main=e.stage||{};const hot=f.hot||[];const seen=new Set();let last=-1;
  const btns=hot.map((o,i)=>`<button type="button" class="ps-hot" data-i="${i}" style="left:${o.x}%;top:${o.y}%" aria-label="${H(o.en)}"><span>${o.e}</span><i class="ps-ping"></i></button>`).join('');
  st.innerHTML=`<div class="step fx ps-hs">${fxKindBar(f,n)}<h2 class="fx-h">${H(f.title||'Explore a cena')} <small id="pghc">0/${hot.length}</small></h2>
  ${stage({rs:f.rs||main.rs,chars:f.chars||main.chars,h:'hot',over:btns})}
  <div class="ps-hot-info" id="pghi"><b>${H(f.hint||'Toque nos objetos brilhantes para ouvir o nome em inglês.')}</b></div>
  <div class="ps-hot-bank" id="pghb">${hot.map((o,i)=>`<button type="button" class="ps-hb" data-i="${i}"><span>${o.e}</span><b>${H(o.en)}</b><i>?</i></button>`).join('')}</div>
  <div class="ps-obralock" id="pglock">🔒 Descubra os ${hot.length} objetos para abrir a obra do dia</div>
  <div class="ps-obracard" id="pgobra" hidden></div></div>`;
  const info=q('#pghi',st),cnt=q('#pghc',st),obra=q('#pgobra',st),bank=q('#pghb',st),lock=q('#pglock',st);
  const reveal=()=>{
    const o=f.obra||{};
    obra.hidden=false;if(lock)lock.hidden=true;
    obra.innerHTML=`${o.pa&&typeof CULT_PROC==='function'?`<div class="ps-obra-art">${CULT_PROC(o.pa)}</div>`:''}
    <div class="ps-obra-t"><small>A obra de hoje · ${H(o.kind||'')}</small><h3>${H(o.name||'')}</h3><p>${H(o.text||'')}</p>
    ${o.line?`<button type="button" class="ps-line" data-say="${H(o.line[0])}"><span>🔊</span><div><b>${H(o.line[0])}</b><small>${H(o.line[1]||'')}</small></div></button>`:''}</div>`;
    obra.querySelectorAll('.ps-line').forEach(b=>b.onclick=()=>tts(b.dataset.say));
    obra.scrollIntoView({behavior:'smooth',block:'nearest'});
    cta('Continuar',true,true);
  };
  st.querySelectorAll('.ps-hot').forEach(b=>b.onclick=()=>{
    const i=+b.dataset.i,o=hot[i];seen.add(i);b.classList.add('seen');last=i;const hb=bank&&bank.querySelector('[data-i="'+i+'"]');if(hb){hb.classList.add('seen');hb.querySelector('i').textContent='✓'}
    info.innerHTML=`<span class="ps-hot-e">${o.e}</span><div><b>${H(o.en)}</b><small>${H(o.pt)}</small>${o.say?`<em>${H(o.say)}</em>`:''}${o.sayPt?`<small class="ps-hot-spt">${H(o.sayPt)}</small>`:''}</div><button type="button" class="ps-hot-sp" aria-label="Ouvir">🔊</button>`;
    info.classList.remove('pop');void info.offsetWidth;info.classList.add('pop');
    const sp=q('.ps-hot-sp',info);if(sp)sp.onclick=()=>tts(o.say||o.en);
    tts(o.say||o.en);cnt.textContent=seen.size+'/'+hot.length;
    if(seen.size===hot.length&&obra.hidden)setTimeout(reveal,700);
  });
  cta('Toque nos objetos da cena',false);
  P.fx.cta=null;
  if(f.intro)setTimeout(()=>tts(f.intro),400);
  say(f.say||'Toque nos objetos brilhantes!');
};
})();
