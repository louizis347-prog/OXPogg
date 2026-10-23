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
  return `<span class="pg-c${fl}" data-c="${id}" style="left:${x}%;--s:${sc}">${window.PogChars?PogChars.svg(id):''}</span>`}).join('');
/* palco: {rs, chars:[[id, x%, espelhar?, escala]], h:'cover'|'scene'|'strip', hot:[…]} */
function stage(o){
  return `<div class="pg-stage ${o.h||'strip'}"><div class="pg-stage-bk">${bg(o.rs||'street')}</div><div class="pg-chars">${chars(o.chars)}</div>${o.over||''}</div>`;
}
function bubble(b){
  if(!b)return '';
  return `<button type="button" class="pg-say" data-say="${H(b[1])}"><span class="pg-say-who">${H(b[0])}</span><b>${H(b[1])}</b>${b[2]?`<small>${H(b[2])}</small>`:''}<i aria-hidden="true">🔊</i></button>`;
}
function bindBubble(root){
  root.querySelectorAll('.pg-say').forEach(b=>b.onclick=()=>tts(b.dataset.say));
}
/* aplica o palco no quadro já renderizado */
function decorate(step,f,e){
  try{
    const host=step.parentNode;if(host){host._pgf=f;host._pge=e;if(!host._pgo){host._pgo=new MutationObserver(()=>{try{
      if(!P||!P.e||P.e!==host._pge||!P.e.pilot||!/^fx\d+$/.test(P.steps[P.i]||''))return;
      const sp=host.querySelector('.step');if(sp&&!sp.querySelector('.pg-stage'))decorate(sp,host._pgf,host._pge)}catch(x){}});host._pgo.observe(host,{childList:true})}}
    const main=e.stage||{};const mk=(h,extra)=>Object.assign({rs:f.rs||main.rs,chars:f.chars||main.chars,h},extra||{});
    if(f.k==='cover'){
      const sc=step.querySelector('.az-scene');
      const st=stage({rs:f.stage&&f.stage.rs||main.rs,chars:f.stage&&f.stage.chars||main.chars,h:'cover',
        over:f.obra?`<span class="pg-obra">📖 ${H(f.obra)}</span>`:''});
      if(sc){sc.innerHTML=st;sc.classList.add('pg-cover')}
      const hero=step.querySelector('.az-hero');
      if(hero&&f.gancho&&!hero.querySelector('.pg-say')){hero.insertAdjacentHTML('beforeend',bubble(f.gancho));bindBubble(hero)}
      return;
    }
    if(f.k==='scene'){
      const w=step.querySelector('.fx-stagewrap');if(!w||w.querySelector('.pg-stage'))return;
      w.insertAdjacentHTML('afterbegin',stage(mk('scene')));w.classList.add('pg-sw');return;
    }
    if(f.k==='hotscene')return;
    if(f.k==='wrap'){
      const hero=step.querySelector('.wr-hero');if(!hero||step.querySelector('.pg-sticker'))return;
      const s=f.sticker||{};
      hero.insertAdjacentHTML('afterend',`<div class="pg-sticker"><div class="pg-sticker-in">${stage({rs:s.rs||main.rs,chars:s.chars||main.chars,h:'sticker'})}<div class="pg-sticker-t"><small>Figurinha desbloqueada</small><b>${H(s.title||'')}</b><span>${H(s.sub||'')}</span></div></div></div>`);
      return;
    }
    if(step.querySelector('.pg-stage'))return;
    const h=f.avatar?'avatar':(f.stageH||'strip');
    const html=`<div class="pg-top">${stage(mk(h))}${bubble(f.bubble)}</div>`;
    const anchor=step.querySelector('.fx-h')||step.firstElementChild;
    if(anchor&&anchor.parentNode===step)anchor.before(frag(html));else step.prepend(frag(html));
    const top=step.querySelector('.pg-top');if(top)bindBubble(top);
  }catch(x){if(window.console)console.warn('pgstage',x)}
}
window.PogStage={stage,bubble,decorate,bindBubble};
const spk2=()=>(typeof spk!=='undefined'?spk:'🔊');

/* ---------- quadro: cena clicável ---------- */
FX_KIND.hotscene='story';FX_LABEL.hotscene='Explore a cena';
FXR.hotscene=function(f,st,n){
  const e=P.e,main=e.stage||{};const hot=f.hot||[];const seen=new Set();let last=-1;
  const btns=hot.map((o,i)=>`<button type="button" class="pg-hot" data-i="${i}" style="left:${o.x}%;top:${o.y}%" aria-label="${H(o.en)}"><span>${o.e}</span><i class="pg-ping"></i></button>`).join('');
  st.innerHTML=`<div class="step fx pg-hs">${fxKindBar(f,n)}<h2 class="fx-h">${H(f.title||'Explore a cena')} <small id="pghc">0/${hot.length}</small></h2>
  ${stage({rs:f.rs||main.rs,chars:f.chars||main.chars,h:'hot',over:btns})}
  <div class="pg-hot-info" id="pghi"><b>${H(f.hint||'Toque nos objetos brilhantes para ouvir o nome em inglês.')}</b></div>
  <div class="pg-obracard" id="pgobra" hidden></div></div>`;
  const info=q('#pghi',st),cnt=q('#pghc',st),obra=q('#pgobra',st);
  const reveal=()=>{
    const o=f.obra||{};
    obra.hidden=false;
    obra.innerHTML=`${o.pa&&typeof CULT_PROC==='function'?`<div class="pg-obra-art">${CULT_PROC(o.pa)}</div>`:''}
    <div class="pg-obra-t"><small>A obra de hoje · ${H(o.kind||'')}</small><h3>${H(o.name||'')}</h3><p>${H(o.text||'')}</p>
    ${o.line?`<button type="button" class="pg-line" data-say="${H(o.line[0])}"><span>🔊</span><div><b>${H(o.line[0])}</b><small>${H(o.line[1]||'')}</small></div></button>`:''}</div>`;
    obra.querySelectorAll('.pg-line').forEach(b=>b.onclick=()=>tts(b.dataset.say));
    obra.scrollIntoView({behavior:'smooth',block:'nearest'});
    cta('Continuar',true,true);
  };
  st.querySelectorAll('.pg-hot').forEach(b=>b.onclick=()=>{
    const i=+b.dataset.i,o=hot[i];seen.add(i);b.classList.add('seen');last=i;
    info.innerHTML=`<span class="pg-hot-e">${o.e}</span><div><b>${H(o.en)}</b><small>${H(o.pt)}</small>${o.say?`<em>${H(o.say)}</em>`:''}</div><button type="button" class="pg-hot-sp" aria-label="Ouvir">🔊</button>`;
    info.classList.remove('pop');void info.offsetWidth;info.classList.add('pop');
    const sp=q('.pg-hot-sp',info);if(sp)sp.onclick=()=>tts(o.say||o.en);
    tts(o.say||o.en);cnt.textContent=seen.size+'/'+hot.length;
    if(seen.size===hot.length&&obra.hidden)setTimeout(reveal,700);
  });
  cta('Toque nos objetos da cena',false);
  P.fx.cta=null;
  if(f.intro)setTimeout(()=>tts(f.intro),400);
  say(f.say||'Toque nos objetos brilhantes!');
};

/* ---------- quadro: fale ---------- */
FX_KIND.pgspeak='speak';FX_LABEL.pgspeak='Fale';
FXR.pgspeak=function(f,st,n){
  const items=f.items||[];let i=0;const sc=[];const lang=(P.c&&P.c.tts)||'en-US';
  const end=()=>{
    const ok=sc.filter(x=>x>=65).length,avg=sc.length?Math.round(sc.reduce((a,b)=>a+b,0)/sc.length):0;
    st.innerHTML=`<div class="step fx pg-sp">${fxKindBar(f,n)}<h2 class="fx-h">Resultado da fala</h2>
    <div class="pv-score ${avg>=85?'great':avg>=65?'good':avg>=40?'ok':'low'} big"><b>${sc.length?avg+'%':'—'}</b><span>${sc.length?ok+' de '+items.length+' falas acima de 65%':'Você pulou a fala. Volte quando puder usar o microfone.'}</span></div>
    <div class="pg-sp-list">${items.map(it=>`<button type="button" class="pg-line" data-say="${H(it[0])}"><span>🔊</span><div><b>${H(it[0])}</b><small>${H(it[1]||'')}</small></div></button>`).join('')}</div></div>`;
    st.querySelectorAll('.pg-line').forEach(b=>b.onclick=()=>tts(b.dataset.say));
    P.fx.cta=null;cta('Continuar',true,true);say(sc.length?'Falar em voz alta faz toda a diferença!':'Quando puder, treine a fala.');
  };
  const draw=()=>{
    if(i>=items.length)return end();
    const it=items[i],hasV=!!window.PogVoice;
    st.innerHTML=`<div class="step fx pg-sp">${fxKindBar(f,n)}<h2 class="fx-h">Sua vez de falar <small>${i+1}/${items.length}</small></h2>
    <div class="pg-sp-card"><div class="pg-sp-t"><button type="button" class="fx-play" id="pgt">${spk2()}</button><div><b>${H(it[0])}</b><small>${H(it[1]||'')}</small></div></div>
    <div class="pg-sp-tools"><button type="button" class="pill light" id="pgsl">🐢 Devagar</button></div>
    <div id="pgmic" class="pv-host"></div><button type="button" class="pill light" id="pgskip">${hasV?'Pular':'Já falei ✓'}</button></div></div>`;
    const next=()=>{i++;draw()};
    q('#pgt',st).onclick=()=>tts(it[0]);q('#pgsl',st).onclick=()=>tts(it[0],true);setTimeout(()=>tts(it[0]),350);
    if(hasV){
      q('#pgskip',st).onclick=next;
      PogVoice.mount(q('#pgmic',st),{target:it[0],lang,
        onDone:r=>{sc[i]=r.score;P.fx.cta=()=>{next();return true};cta(i<items.length-1?'Próxima ▶':'Ver resultado',true,true)},
        onFail:c=>{if(c==='unsupported'){P.fx.cta=()=>{next();return true};cta(i<items.length-1?'Próxima ▶':'Ver resultado',true,true)}}});
      P.fx.cta=null;cta('Fale e veja sua nota',false);
    }else{
      q('#pgskip',st).onclick=()=>{P.fx.cta=()=>{next();return true};cta(i<items.length-1?'Próxima ▶':'Ver resultado',true,true);q('#pgskip',st).disabled=true};
      P.fx.cta=null;cta('Repita em voz alta',false);
    }
  };
  draw();say(f.say||'Toque no microfone e repita a frase.');
};
})();
