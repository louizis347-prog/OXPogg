/* Pogglot · remodelagem dos quadros (out/2026)
   1) player de áudio no diálogo da cena (pausar, continuar de onde parou, ir para qualquer fala, velocidade)
   2) frase de treino do laboratório de sons passa para o quadro seguinte
   3) contextos variados (ctxv) e "Troque a peça" (ppat), práticas novas
   4) "Sua vez" guiado: objetivos que se marcam sozinhos, microfone e comparação com o modelo */
(function(){
'use strict';
if(typeof FXR==='undefined'||typeof P==='undefined')return;

/* ── ilustrações realistas, sem nenhum texto, para não entregar a resposta ── */
const SV={
atm:`<svg viewBox="0 0 64 64" class="rw-svg" role="img" aria-label="imagem"><defs><linearGradient id="rwa1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e4e9ef"/><stop offset="1" stop-color="#aab4c0"/></linearGradient><linearGradient id="rwa2" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2e7bd6"/><stop offset="1" stop-color="#123c78"/></linearGradient></defs>
<rect x="9" y="4" width="46" height="56" rx="4" fill="url(#rwa1)" stroke="#7d8896" stroke-width="1.2"/>
<rect x="13" y="8" width="38" height="20" rx="2" fill="#1b2430"/><rect x="15" y="10" width="34" height="16" rx="1.2" fill="url(#rwa2)"/>
<rect x="18" y="13" width="14" height="2.4" rx="1" fill="#bfe0ff"/><rect x="18" y="18" width="22" height="2" rx="1" fill="#7fb8f2"/><rect x="18" y="22" width="9" height="2" rx="1" fill="#7fb8f2"/>
<rect x="11" y="12" width="2.2" height="3" fill="#59616d"/><rect x="11" y="18" width="2.2" height="3" fill="#59616d"/><rect x="50.8" y="12" width="2.2" height="3" fill="#59616d"/><rect x="50.8" y="18" width="2.2" height="3" fill="#59616d"/>
<rect x="13" y="31" width="22" height="16" rx="2" fill="#4a5360"/>${[0,1,2].map(r=>[0,1,2].map(c=>`<rect x="${15+c*6.6}" y="${33+r*4.4}" width="5" height="3.4" rx=".8" fill="#d7dde4"/>`).join('')).join('')}
<rect x="38" y="31" width="13" height="5" rx="1" fill="#2a2f37"/><rect x="40" y="32.4" width="9" height="1.4" fill="#4cd37a"/>
<rect x="38" y="39" width="13" height="8" rx="1.5" fill="#6a7482"/><circle cx="44.5" cy="43" r="2" fill="#2f353d"/>
<rect x="14" y="50" width="36" height="7" rx="1.5" fill="#262b33"/><rect x="17" y="52" width="30" height="3" rx="1" fill="#0d1014"/><rect x="21" y="49" width="22" height="3.4" rx=".8" fill="#7bc47f"/><rect x="23" y="49.6" width="18" height="1" fill="#a6e0a4"/></svg>`,
elevator:`<svg viewBox="0 0 64 64" class="rw-svg" role="img" aria-label="imagem"><defs><linearGradient id="rwe1" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#9aa3ad"/><stop offset=".5" stop-color="#e3e8ed"/><stop offset="1" stop-color="#a8b1ba"/></linearGradient></defs>
<rect x="6" y="3" width="52" height="58" rx="2" fill="#5b6470"/><rect x="10" y="7" width="44" height="54" fill="#2d333b"/>
<rect x="11" y="8" width="21" height="53" fill="url(#rwe1)"/><rect x="33" y="8" width="21" height="53" fill="url(#rwe1)"/>${[14,22,30,38,46,54].map(y=>`<line x1="12" y1="${y}" x2="31" y2="${y-3}" stroke="#fff" stroke-opacity=".35" stroke-width="1.4"/><line x1="34" y1="${y}" x2="53" y2="${y-3}" stroke="#fff" stroke-opacity=".35" stroke-width="1.4"/>`).join('')}
<line x1="32.5" y1="8" x2="32.5" y2="61" stroke="#2a3038" stroke-width="1.2"/>
<rect x="57" y="22" width="6" height="18" rx="2" fill="#2f3640"/><path d="M60 26.5 L58.2 29.6 H61.8Z" fill="#ffd45a"/><path d="M60 35.5 L58.2 32.4 H61.8Z" fill="#c8ced6"/>
<path d="M26 2.5 H38 L36 6 H28Z" fill="#2f3640"/><path d="M32 3.2 L30.4 5.4 H33.6Z" fill="#7bffa0"/></svg>`,
exit:`<svg viewBox="0 0 64 64" class="rw-svg" role="img" aria-label="imagem"><rect x="10" y="2" width="44" height="60" rx="2" fill="#6c5a49"/><rect x="14" y="14" width="36" height="48" fill="#8b6f52"/><rect x="14" y="14" width="36" height="48" fill="none" stroke="#5a4533" stroke-width="1.2"/>
<rect x="18" y="20" width="12" height="16" rx="1" fill="#a58563"/><rect x="34" y="20" width="12" height="16" rx="1" fill="#a58563"/><rect x="18" y="40" width="28" height="18" rx="1" fill="#a58563"/>
<rect x="12" y="40" width="40" height="3.4" rx="1.4" fill="#c9ced4" stroke="#7f8791" stroke-width=".7"/>
<rect x="16" y="3" width="32" height="10" rx="2" fill="#12823d" stroke="#0a5a28" stroke-width=".8"/><circle cx="25" cy="6.2" r="1.3" fill="#fff"/><path d="M24 8 L27 8.4 L28.6 10.6 M27 8.4 L25.6 11 M27.4 8 L30 7 M30 6.2 L33 6.2 M36 5 H44 M36 8 H44" stroke="#fff" stroke-width="1" fill="none" stroke-linecap="round"/></svg>`,
stairs:`<svg viewBox="0 0 64 64" class="rw-svg" role="img" aria-label="imagem"><path d="M4 60 V48 H16 V38 H28 V28 H40 V18 H52 V8 H60 V60Z" fill="#c9bfae"/><path d="M4 48 H16 V38 H28 V28 H40 V18 H52 V8" fill="none" stroke="#8d8372" stroke-width="1.6"/><path d="M16 48 V60 M28 38 V60 M40 28 V60 M52 18 V60" stroke="#9c927f" stroke-width="1"/>
<path d="M6 40 L54 2" stroke="#2f3a46" stroke-width="2.6" stroke-linecap="round"/>${[10,22,34,46].map(x=>`<line x1="${x}" y1="${46-(x-4)*0.79}" x2="${x}" y2="${52-(x-4)*0.79+ (x>0?0:0)}" stroke="#2f3a46" stroke-width="1.4"/>`).join('')}</svg>`,
restroom:`<svg viewBox="0 0 64 64" class="rw-svg" role="img" aria-label="imagem"><rect x="4" y="6" width="56" height="52" rx="4" fill="#dfe6ee" stroke="#9aa6b3" stroke-width="1.2"/><rect x="7" y="9" width="24" height="46" rx="2" fill="#2a6fb8"/><rect x="33" y="9" width="24" height="46" rx="2" fill="#c2417b"/>
<circle cx="19" cy="20" r="4.2" fill="#fff"/><path d="M14 27 H24 L25 40 H22.6 L22 49 H20 V41 H18 V49 H16 L15.4 40 H13Z" fill="#fff"/>
<circle cx="45" cy="20" r="4.2" fill="#fff"/><path d="M45 26 L52 42 H38Z" fill="#fff"/><path d="M42.5 42 V49 M47.5 42 V49" stroke="#fff" stroke-width="2.2"/></svg>`
};
const _fxIcon=window.fxIcon;
window.fxIcon=function(ic,px){if(typeof ic==='string'&&ic.startsWith('svg:')){const s=SV[ic.slice(4)];if(s){const p=px||72;return s.replace('<svg ','<svg width="'+p+'" height="'+p+'" ')}}return _fxIcon?_fxIcon(ic,px):ic};

const ico={
  play:'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>',
  pause:'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 5h4v14H7zM13 5h4v14h-4z"/></svg>',
  prev:'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6h2v12H6zM20 6v12L9.5 12z"/></svg>',
  next:'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16 6h2v12h-2zM4 6l10.5 6L4 18z"/></svg>',
  redo:'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5V2L7 6l5 4V7a5 5 0 1 1-5 5H5a7 7 0 1 0 7-7z"/></svg>'
};
const lang=()=>(P&&P.c&&P.c.tts)||'en-US';

/* ------------------------------------------------------------------ rótulos */
FX_KIND.ctxv='practice';FX_LABEL.ctxv='Contextos variados';
FX_KIND.ppat='practice';FX_LABEL.ppat='Escolha a peça';
FX_LABEL.pbridge='Monte a frase na ponte';
FX_KIND.sphr='practice';FX_LABEL.sphr='Frase de treino';

const _ft=window.fxTotal;
window.fxTotal=function(e){let n=_ft(e);(e.fr||[]).forEach(f=>{if(f.k==='ctxv')n+=f.items.length;else if(f.k==='ppat')n+=f.rounds.length;else if(f.k==='sphr')n+=(f.blanks||[]).length});return n};

if(window.PogTTS&&PogTTS.episodeTexts){
  const o=PogTTS.episodeTexts;
  PogTTS.episodeTexts=function(e){
    const out=o(e),seen=new Set(out.map(x=>x.text+'|'+(x.speaker||'')));
    const add=(t,sp)=>{t=String(t||'').replace(/\*\*/g,'').trim();const k=t+'|'+(sp||'');if(t&&t.length<400&&!seen.has(k)){seen.add(k);out.push({text:t,speaker:sp||null})}};
    (e.fr||[]).forEach(f=>{
      if(f.k==='ctxv')(f.items||[]).forEach(it=>{let k=0;it.lines.forEach(l=>add(l[1].replace(/___/g,()=>it.ans[k++]),l[0]||null))});
      if(f.k==='ppat')(f.rounds||[]).forEach(r=>{const o=r.opts[r.a];add(String(r.q).replace('___',Array.isArray(o)?o[1]:o))});
      if(f.k==='sphr'&&f.phrase)add(f.phrase[0]);
      if(f.k==='pbridge'||f.k==='pballoon')(f.rounds||[]).forEach(r=>add(r.t));
    });
    return out;
  };
}

/* ------------------------------------------------------------------ 1) player do diálogo */
function makePlayer(L,onState,onLine){
  let idx=0,playing=false,slow=false,tok=0,ended=false;
  const txt=i=>plain(L[i][1]);
  const state=()=>onState(idx,playing,slow,ended);
  function stopAudio(){fxStopAudio()}
  function playFrom(i){
    i=Math.max(0,Math.min(L.length-1,i));
    stopAudio();const my=++tok;idx=i;playing=true;ended=false;state();onLine&&onLine(i);
    let adv=false;const t=txt(i);
    const next=()=>{
      if(adv||my!==tok||!playing)return;adv=true;clearTimeout(fxSeq.t);clearTimeout(fxSeq.t2);
      fxSeq.t=setTimeout(()=>{
        if(my!==tok||!playing)return;
        if(i+1>=L.length){playing=false;ended=true;state()}else playFrom(i+1);
      },slow?900:450);
    };
    window.__speakEnd=next;
    fxSay(t,L[i][0],slow?FX_TURTLE:false);
    clearTimeout(fxSeq.t2);fxSeq.t2=setTimeout(next,t.length*(slow?230:150)+3500);
  }
  return{
    get idx(){return idx},get playing(){return playing},get slow(){return slow},
    toggle(){
      if(playing){playing=false;tok++;stopAudio();state()}
      else playFrom(ended?0:idx);
    },
    pause(){if(playing){playing=false;tok++;stopAudio();state()}},
    playFrom,
    seek(i){
      i=Math.max(0,Math.min(L.length-1,i));
      if(playing)playFrom(i);else{idx=i;ended=false;state();onLine&&onLine(i,true)}
    },
    prev(){this.seek(idx-1)},next(){this.seek(idx+1)},
    repeat(){playFrom(idx)},
    setSlow(v){slow=!!v;if(playing)playFrom(idx);else state()}
  };
}

FXR.scene=function(f,st,n){
  const cast=f.cast||{},names=Object.keys(cast).slice(0,2),L=f.lines,N=L.length;
  let revealed=0,touched=false;
  st.innerHTML=`<div class="step fx">${fxKindBar(f,n)}<div class="fx-stagewrap">${fxArt(f.art,.48)}<div class="fx-cast">${names.map((nm,i)=>`<div class="fx-av ${i?'r':'l'}" data-n="${esc(nm)}"><span>${cast[nm][0]}</span></div>`).join('')}</div></div>
  <div class="dp" id="dp" role="group" aria-label="Player do diálogo">
    <div class="dp-now" id="dpnow" aria-live="polite">Toque em ▶ para ouvir a cena</div>
    <div class="dp-row">
      <button type="button" class="dp-play" id="dpplay" aria-label="Tocar">${ico.play}</button>
      <button type="button" class="dp-b" id="dpprev" aria-label="Fala anterior">${ico.prev}</button>
      <div class="dp-track" id="dptrack">${L.map((l,i)=>`<button type="button" class="dp-seg" data-i="${i}" aria-label="Ir para a fala ${i+1}"></button>`).join('')}</div>
      <button type="button" class="dp-b" id="dpnext" aria-label="Próxima fala">${ico.next}</button>
      <button type="button" class="dp-b" id="dprep" aria-label="Repetir esta fala">${ico.redo}</button>
      <span class="dp-sp" role="group" aria-label="Velocidade"><button type="button" data-s="0" aria-label="Velocidade natural" title="Natural">1×</button><button type="button" data-s="1" aria-label="Falar devagar" title="Devagar">🐢</button></span>
    </div>
  </div>
  <div class="fx-lines" id="fxl"></div>${fxCul(f)}</div>`;
  const root=st.querySelector('#dp'),box=st.querySelector('#fxl'),segs=[...st.querySelectorAll('.dp-seg')],
        playBtn=st.querySelector('#dpplay'),now=st.querySelector('#dpnow');
  const bubbles=[];
  const addBubble=k=>{
    const l=L[k],c=cast[l[0]]||['🙂','#888'];
    const d=document.createElement('div');d.className='fx-line '+(names.indexOf(l[0])===1?'r':'l');d.style.setProperty('--c',c[1]);
    d.innerHTML=`<span class="fx-lav">${c[0]}</span><div class="fx-bub"><b>${esc(l[0])}</b><p>${mk(l[1])}</p><small class="fx-tr">${esc(l[2])}</small></div><button type="button" class="dp-go" aria-label="Ouvir daqui">${ico.play}</button>`;
    d.onclick=ev=>{d.classList.toggle('tr');touched=true;pl.playFrom(k)};
    box.appendChild(d);bubbles[k]=d;
  };
  const reveal=upto=>{while(revealed<=upto&&revealed<N){addBubble(revealed);revealed++}};
  const setCta=()=>{if(revealed>=N)cta('Continuar',true,false);else cta('Próxima fala ▶',true,true)};
  const pl=makePlayer(L.map(l=>[l[0],l[1]]),(i,playing,slow,ended)=>{
    if(!root.isConnected)return;
    reveal(i);
    segs.forEach((s,k)=>{s.classList.toggle('done',k<i||(ended&&k===i));s.classList.toggle('cur',k===i&&!ended)});
    playBtn.innerHTML=playing?ico.pause:ico.play;playBtn.setAttribute('aria-label',playing?'Pausar':'Tocar');
    root.classList.toggle('on',playing);
    now.textContent=ended?'Fim da cena · toque em ▶ para ouvir de novo':`Fala ${i+1} de ${N} · ${L[i][0]}${playing?'':' · pausado'}`;
    st.querySelectorAll('.fx-av').forEach(a=>a.classList.toggle('talk',playing&&a.dataset.n===L[i][0]));
    bubbles.forEach((b,k)=>b&&b.classList.toggle('dp-cur',k===i));
    {const pv=st.querySelector('#dpprev'),nx=st.querySelector('#dpnext');if(pv)pv.disabled=i<=0;if(nx)nx.disabled=i>=N-1}
    root.querySelectorAll('.dp-sp button').forEach(b=>b.classList.toggle('on',(b.dataset.s==='1')===slow));
    setCta();
  },(i,silent)=>{if(L[i][3]&&!silent)sfx(L[i][3]);const b=bubbles[i];if(b&&!silent)b.scrollIntoView({behavior:'smooth',block:'nearest'})});
  playBtn.onclick=()=>{touched=true;pl.toggle()};
  st.querySelector('#dpprev').onclick=()=>{touched=true;pl.prev()};
  st.querySelector('#dpnext').onclick=()=>{touched=true;pl.next()};
  st.querySelector('#dprep').onclick=()=>{touched=true;pl.repeat()};
  segs.forEach(s=>s.onclick=()=>{touched=true;pl.seek(+s.dataset.i)});
  root.querySelectorAll('.dp-sp button').forEach(b=>b.onclick=()=>{touched=true;pl.setSlow(b.dataset.s==='1')});
  P.fx.cta=()=>{
    if(revealed<N){touched=true;pl.playFrom(revealed);return true}
    pl.pause();return false;
  };
  cta('Próxima fala ▶',true,true);
  /* se o aluno sair do quadro, o áudio para */
  const watch=setInterval(()=>{if(!root.isConnected){clearInterval(watch);pl.pause()}},500);
  setTimeout(()=>{if(!touched&&root.isConnected)pl.playFrom(0)},450);
  say('Use o player: pause, volte uma fala ou toque numa fala para ouvir dali.');
};


/* ------------------------------------------------------------------ 1b) "Ordene o diálogo" com o mesmo player compacto */
const _order=FXR.order;
FXR.order=function(f,st,n){
  _order.call(this,f,st,n);
  try{
    const hn=st.querySelector('#fxall');if(hn){hn.click();hn.click()}   // desliga o autoplay antigo
    const row=st.querySelector('.fx-hearrow');if(!row)return;
    const full=(f.audio&&f.audio.length?f.audio:f.lines).map(l=>[l[0],l[1]]),N=full.length;
    const box=document.createElement('div');box.className='dp';box.id='dp';
    box.innerHTML=`<div class="dp-now" id="dpnow" aria-live="polite">Toque em ▶ para ouvir a conversa</div>
      <div class="dp-row"><button type="button" class="dp-play" id="dpplay" aria-label="Tocar">${ico.play}</button>
      <button type="button" class="dp-b" id="dpprev" aria-label="Fala anterior">${ico.prev}</button>
      <div class="dp-track">${full.map((l,i)=>`<button type="button" class="dp-seg" data-i="${i}" aria-label="Ir para a fala ${i+1}"></button>`).join('')}</div>
      <button type="button" class="dp-b" id="dpnext" aria-label="Próxima fala">${ico.next}</button>
      <span class="dp-sp"><button type="button" data-s="1" aria-label="Falar devagar" title="Devagar">🐢</button></span></div>`;
    row.replaceWith(box);
    const segs=[...box.querySelectorAll('.dp-seg')],playBtn=box.querySelector('#dpplay'),now=box.querySelector('#dpnow');
    const pl=makePlayer(full,(i,playing,slow,ended)=>{
      segs.forEach((s,k)=>{s.classList.toggle('done',k<i||(ended&&k===i));s.classList.toggle('cur',k===i&&!ended)});
      playBtn.innerHTML=playing?ico.pause:ico.play;box.classList.toggle('on',playing);
      now.textContent=ended?'Fim · toque em ▶ para ouvir de novo':`Fala ${i+1} de ${N}${playing?'':' · pausado'}`;
      st.querySelectorAll('.fx-av').forEach(a=>a.classList.toggle('talk',playing&&a.dataset.n===full[i][0]));
      box.querySelector('#dpprev').disabled=i<=0;box.querySelector('#dpnext').disabled=i>=N-1;
      box.querySelectorAll('.dp-sp button').forEach(b=>b.classList.toggle('on',slow));
    });
    playBtn.onclick=()=>pl.toggle();
    box.querySelector('#dpprev').onclick=()=>pl.prev();box.querySelector('#dpnext').onclick=()=>pl.next();
    segs.forEach(s=>s.onclick=()=>pl.seek(+s.dataset.i));
    box.querySelector('.dp-sp button').onclick=e=>pl.setSlow(!e.currentTarget.classList.contains('on'));
    const bank=st.querySelector('#fxb');
    if(bank)bank.addEventListener('click',()=>pl.pause(),true);
    const watch=setInterval(()=>{if(!box.isConnected){clearInterval(watch);pl.pause()}},500);
    let touched=false;box.addEventListener('click',()=>{touched=true},true);
    setTimeout(()=>{if(!touched&&box.isConnected)pl.playFrom(0)},700);
  }catch(e){console.warn('order',e)}
};

/* ------------------------------------------------------------------ 2) frase de treino no quadro seguinte ao sound lab */
function stripPhrase(st){
  const m=st.querySelector('#slph');if(!m)return;
  const box=m.closest('.fx-model'),h=box&&box.previousElementSibling;
  [h&&h.classList.contains('sl-h')?h:null,box,st.querySelector('#slslow'),st.querySelector('#slmic')].forEach(x=>x&&x.remove());
}
function carryPhrase(st,lab){
  const step=st.querySelector('.step');if(!step||step.querySelector('.rw-phrase'))return;
  const pl=plain(lab.phrase[0]);
  const d=document.createElement('section');d.className='rw-phrase';
  d.innerHTML=`<div class="rw-ph-h"><span>🎤</span><div><small>Do laboratório de sons${lab.short?' · '+esc(lab.short):''}</small><b>Frase de treino</b></div></div>
    <div class="fx-model"><div><small>Repita em voz alta</small><b>${mk(lab.phrase[0])}</b><small>${esc(lab.phrase[1]||'')}</small></div><button type="button" class="say2" id="rwph" aria-label="Ouvir">${spk}</button></div>
    <button type="button" class="pill light" id="rwslow">🐢 Ouvir devagar</button><div id="rwmic" class="pv-host"></div>`;
  const anchor=step.querySelector('.fx-cul');
  anchor?anchor.before(d):step.appendChild(d);
  d.querySelector('#rwph').onclick=()=>fxSay(pl);
  d.querySelector('#rwslow').onclick=()=>fxSay(pl,null,true);
  if(window.PogVoice)PogVoice.mount(d.querySelector('#rwmic'),{target:pl,lang:lang()});
}
const _rf=window.renderFx;
window.renderFx=function(n,st,lng){
  _rf(n,st,lng);
  try{
    const fr=P.e.fr,f=fr[n],prev=fr[n-1];
    if(f.k==='soundlab'&&f.phrase)stripPhrase(st);
  }catch(e){console.warn('rework',e)}
};


/* ------------------------------------------------------------------ 2b) frase de treino: reconhecer pelo som, completar e repetir */
FXR.sphr=function(f,st,n){
  const en=f.phrase[0],B=f.blanks||[];
  const toks=en.split(/\s+/);const parts_done=new Set();
  const parts=toks.map(t=>{
    const w=t.replace(/\*\*/g,'').replace(/^[^\w']+|[^\w']+$/g,'');
    const k=B.findIndex(b=>b.w.toLowerCase()===w.toLowerCase());
    if(k>=0&&!parts_done.has(k)){parts_done.add(k);const pre=t.replace(/\*\*/g,'').match(/^[^\w']*/)[0],post=t.replace(/\*\*/g,'').match(/[^\w']*$/)[0];
      return `${esc(pre)}<span class="rw-sph-slot" data-k="${k}"><i>?</i></span>${esc(post)}`}
    return mk(t)});
  let cur=0,tries=0;
  const parts_done_reset=0;
  const sentence=parts.join(' ');
  st.innerHTML=`<div class="step fx">${fxKindBar(f,n)}<h2 class="fx-h">${esc(f.title||'Frase de treino')}</h2>
    ${fxEn('👂','OUÇA E COMPLETE','Ouça a frase e toque na palavra que você escuta em cada lacuna.')}
    <div class="rw-sph"><div class="rw-sph-s" id="rwsent">${sentence}</div>
      <div class="rw-sph-ctl"><button type="button" class="pill" id="rwhear">${spk} Ouvir a frase</button><button type="button" class="pill light" id="rwslow">🐢 Devagar</button></div></div>
    <div class="fx-opts g2" id="rwopts"></div><div id="fb"></div>
    <div class="rw-sph-end" id="rwend" hidden><div class="rw-sph-pt">${esc(f.phrase[1]||'')}</div><div class="sl-h">🎤 Agora diga a frase em voz alta</div><div id="rwmic" class="pv-host"></div></div></div>`;
  const pl=plain(en);
  const hear=slow=>fxSay(pl,null,!!slow);
  st.querySelector('#rwhear').onclick=()=>hear(false);
  st.querySelector('#rwslow').onclick=()=>hear(true);
  const slots=[...st.querySelectorAll('.rw-sph-slot')];
  const drawOpts=()=>{
    const b=B[cur];tries=0;
    slots.forEach((s,i)=>s.classList.toggle('on',i===cur));
    const o=fxShuffle([b.w,b.alt]);
    const box=st.querySelector('#rwopts');
    box.innerHTML=o.map((w,i)=>`<button type="button" class="fx-o" data-w="${esc(w)}">${esc(w)}</button>`).join('');
    box.querySelectorAll('.fx-o').forEach(btn=>btn.onclick=()=>{
      if(P.answered)return;
      const ok=btn.dataset.w===b.w;
      if(!ok){tries++;btn.disabled=true;btn.classList.add('no');beep(false);
        fxGrade(false,'Ouça de novo: repare no som que muda entre as duas palavras.',null);return}
      if(tries===0)P.score++;
      btn.classList.add('ok');const s=slots[cur];s.classList.add('ok');s.querySelector('i').textContent=b.w;
      sfx('pop');fxSay(b.w);
      cur++;
      if(cur<B.length){fxGrade(true,'Isso! Próxima lacuna.',null);setTimeout(drawOpts,500)}
      else{
        P.answered=true;box.innerHTML='';fxGrade(true,'Frase completa! Agora é a sua vez de falar.',null);
        setTimeout(()=>hear(false),500);
        const end=st.querySelector('#rwend');end.hidden=false;
        if(window.PogVoice)PogVoice.mount(end.querySelector('#rwmic'),{target:pl,lang:lang()});
        cta('Continuar',true,true);
      }
    });
  };
  P.answered=false;cta('Complete a frase',false);
  if(B.length){drawOpts()}else{P.answered=true;st.querySelector('#rwend').hidden=false;cta('Continuar',true,true)}
  setTimeout(()=>{if(st.isConnected)hear(false)},500);
  say(f.say||'Ouça com atenção e complete a frase.');
};

/* ------------------------------------------------------------------ 3a) contextos variados */
FXR.ctxv=function(f,st,n){
  FXR.ctx(Object.assign({},f,{title:f.title||'Situações novas'}),st,n);
  try{
    const en=st.querySelector('.fx-en-t small'),p=st.querySelector('.fx-en-t p');
    if(en)en.textContent='SITUAÇÕES NOVAS';
    if(p)p.textContent='Ouça cada situação e escolha as palavras que completam o diálogo.';
  }catch(e){}
};

/* ------------------------------------------------------------------ 3b) troque a peça: o padrão fica, a peça muda */
FXR.ppat=function(f,st,n){
  const R=f.rounds;let ri=0,tries=0;
  R.forEach(r=>{r.opts=r.opts.map(o=>Array.isArray(o)?o:['',o])});
  const PAL=['#7C4DFF','#12B3A8','#FF6F59','#E0499D','#2F8FE0'];
  const draw=()=>{
    const r=R[ri];tries=0;
    const toks=r.q.split(/\s+/);
    const pat=toks.map((t,i)=>{const m=t.match(/^(.*)___(.*)$/);
      return m?`${m[1]?`<span class="rw-pn">${esc(m[1])}</span>`:''}<span class="rw-slot" id="rwslot" aria-label="peça que falta"><i>?</i></span>${m[2]?`<span class="rw-pn">${esc(m[2])}</span>`:''}`
        :`<span class="fx-blk" style="--b:${PAL[i%PAL.length]};--i:${i}">${esc(t)}</span>`}).join('');
    st.innerHTML=`<div class="step fx">${fxKindBar(f,n)}<h2 class="fx-h">${esc(f.title||'Escolha a peça')}${R.length>1?` <small>${ri+1}/${R.length}</small>`:''}</h2>${r.rev?'<span class="rw-rev">↺ revisão do episódio anterior</span>':''}
      ${fxEn('🧩','ESCOLHA A PEÇA',`Escolha a peça que completa a frase: <b>${esc(r.pt)}</b>`)}
      <div class="rw-pat">${pat}</div>
      <div class="fx-opts g2">${r.opts.map((o,i)=>`<button type="button" class="fx-o${o[0]?' img':''}" data-i="${i}">${o[0]?`<span>${fxIcon(o[0],72)}</span>`:''}${o[0]?'<small>'+esc(o[1])+'</small>':esc(o[1])}</button>`).join('')}</div>
      <div id="fb"></div><div id="rwmic" class="pv-host" hidden></div></div>`;
    const slot=st.querySelector('#rwslot');
    st.querySelectorAll('.fx-o').forEach(b=>b.onclick=()=>{
      if(P.answered)return;
      const i=+b.dataset.i,ok=i===r.a;
      if(!ok){tries++;b.disabled=true;b.classList.add('no');beep(false);
        fxGrade(false,(r.wf&&r.wf[i])||(tries>1?null:'Releia a frase em português e procure a peça com o mesmo sentido.'),null);return}
      P.answered=true;
      st.querySelectorAll('.fx-o').forEach((x,j)=>{x.disabled=true;if(j===r.a)x.classList.add('ok')});
      slot.classList.add('ok');slot.querySelector('i').textContent=r.opts[r.a][1];
      if(tries===0)P.score++;
      const full=plain(r.q.replace('___',r.opts[r.a][1]));
      fxGrade(true,(r.why||'A peça mudou; o padrão ficou.')+' → **'+full+'**',null);
      setTimeout(()=>fxSay(full),250);
      if(window.PogVoice&&PogVoice.supported()&&ri===R.length-1){
        const hm=st.querySelector('#rwmic');hm.hidden=false;
        hm.innerHTML='<div class="sl-h">🎤 Diga a última frase em voz alta</div><div class="pv-in"></div>';
        PogVoice.mount(hm.querySelector('.pv-in'),{target:full,lang:lang()});
      }
      cta(ri<R.length-1?'Próxima peça ▶':'Continuar',true,true);
    });
    P.answered=false;cta('Escolha a peça certa',false);
  };
  P.fx.cta=()=>{if(P.answered&&ri<R.length-1){ri++;draw();return true}return false};
  draw();say(f.say||'O padrão não muda: troque só a peça.');
};

/* ------------------------------------------------------------------ 4) "Sua vez" guiado */
const _produce=FXR.produce;
FXR.produce=function(f,st,n){
  _produce.call(this,f,st,n);
  try{enhanceProduce(f,st)}catch(e){console.warn('produce',e)}
};
function enhanceProduce(f,st){
  const step=st.querySelector('.step'),ta=step&&step.querySelector('#fxta');if(!ta||step.querySelector('.rw-sit'))return;
  const old=step.querySelector('.fx-prompt'),chips=step.querySelector('.fx-chips'),mbtn=step.querySelector('#fxm'),mod=step.querySelector('#fxmod');
  const goals=(f.check||[]).map((c,i)=>({t:c,re:f.kw&&f.kw[i]?new RegExp(f.kw[i],'i'):null,ok:false}));
  /* 1) missão */
  const sit=document.createElement('div');sit.className='rw-sit';
  sit.innerHTML=`<span class="rw-sit-ic" aria-hidden="true">🎬</span><div><small>Sua missão</small><p>${mk(f.prompt)}</p></div>`;
  old.replaceWith(sit);
  /* 2) passos */
  const steps=document.createElement('ol');steps.className='rw-steps';
  steps.innerHTML='<li class="on" data-s="1"><b>1</b> Comece com uma peça</li><li data-s="2"><b>2</b> Escreva ou fale</li><li data-s="3"><b>3</b> Confira os objetivos</li><li data-s="4"><b>4</b> Compare com o modelo</li>';
  sit.after(steps);
  if(chips){chips.classList.add('rw-chips');const lab=document.createElement('small');lab.className='rw-lab';lab.textContent='Toque para começar a frase';chips.before(lab)}
  /* 3) escrever ou falar */
  const bar=document.createElement('div');bar.className='rw-bar';
  const canMic=!!(window.PogVoice&&PogVoice.supported());
  bar.innerHTML=`${canMic?'<button type="button" class="pill light" id="rwdict">🎤 Falar em vez de escrever</button>':''}<span class="rw-count" id="rwcnt"></span>`;
  ta.after(bar);
  ta.placeholder=f.ph||'Escreva em inglês, ou toque em 🎤 e fale';
  /* 4) objetivos */
  const ul=document.createElement('ul');ul.className='rw-goals';
  ul.innerHTML=goals.map((g,i)=>`<li data-i="${i}" class="${g.re?'auto':'manual'}" ${g.re?'':'role="checkbox" aria-checked="false" tabindex="0"'}><span class="rw-box"></span><span>${esc(g.t)}</span></li>`).join('');
  if(goals.length){const h=document.createElement('small');h.className='rw-lab';h.textContent=goals.some(g=>g.re)?'Objetivos (marcam sozinhos enquanto você escreve)':'Objetivos (toque para marcar)';bar.after(h);h.after(ul)}
  const upd=()=>{
    const v=ta.value;let c=0;
    goals.forEach((g,i)=>{if(g.re)g.ok=g.re.test(v);const li=ul.children[i];if(!li)return;li.classList.toggle('done',g.ok);if(li.getAttribute('role'))li.setAttribute('aria-checked',g.ok);if(g.ok)c++});
    const cnt=step.querySelector('#rwcnt');if(cnt)cnt.textContent=goals.length?`${c}/${goals.length} objetivos`:'';
    const s=v.trim().length>=3?(c===goals.length&&goals.length?3:2):1;
    steps.querySelectorAll('li').forEach(li=>li.classList.toggle('on',+li.dataset.s<=s+(mod&&!mod.hidden?1:0)));
  };
  ul.querySelectorAll('li.manual').forEach(li=>{const t=()=>{const g=goals[+li.dataset.i];g.ok=!g.ok;sfx('key');upd()};li.onclick=t;li.onkeydown=e=>{if(e.key===' '||e.key==='Enter'){e.preventDefault();t()}}});
  ta.addEventListener('input',upd);
  step.querySelectorAll('.fx-chip').forEach(c=>c.addEventListener('click',()=>setTimeout(upd,0)));
  /* 5) ditar por voz */
  const dict=step.querySelector('#rwdict');
  if(dict){
    let h=null;
    dict.onclick=()=>{
      if(h){h.stop();return}
      dict.textContent='⏹ Ouvindo… toque para parar';dict.classList.add('rec');
      h=PogVoice.listen({lang:lang(),maxMs:12000,onInterim:t=>{ta.dataset.interim=t},
        onDone:r=>{h=null;dict.textContent='🎤 Falar em vez de escrever';dict.classList.remove('rec');
          if(r.alts&&r.alts[0]){ta.value+=(ta.value&&!/\s$/.test(ta.value)?' ':'')+r.alts[0];ta.dispatchEvent(new Event('input'))}
          else{const c=step.querySelector('#rwcnt');if(c)c.textContent='Não ouvi nada. Tente de novo.'}}});
    };
  }
  /* 6) modelo comparado */
  if(mbtn){
    mbtn.textContent='👀 Ver o modelo e comparar';
    mbtn.addEventListener('click',()=>{
      if(mod&&!mod.querySelector('.rw-mine')){
        const mine=document.createElement('div');mine.className='rw-mine';
        mine.innerHTML=`<small>Você escreveu</small><p>${esc(ta.value.trim()||'—')}</p>`;
        mod.prepend(mine);
      }
      upd();
    });
  }
  upd();
}


/* ------------------------------------------------------------------ 5) práticas dos "verbos" e das "combinações" */
FX_KIND.vprac='practice';FX_LABEL.vprac='Pratique os verbos';
FX_KIND.xprac='practice';FX_LABEL.xprac='Pratique as combinações';

const _ft2=window.fxTotal;
window.fxTotal=function(e){let n=_ft2(e);(e.fr||[]).forEach(f=>{if(f.k==='vprac'||f.k==='xprac')n+=(f.rounds||[]).length});return n};

const hashS=str=>{let h=2166136261;for(let i=0;i<str.length;i++){h^=str.charCodeAt(i);h=Math.imul(h,16777619)}return h>>>0};
const rng=seed=>{let a=seed||1;return()=>{a=(a+0x6D2B79F5)|0;let t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296}};
const shuf=(arr,r)=>{const a=arr.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(r()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a};
const core=t=>{const m=String(t).match(/^([^A-Za-z']*)([A-Za-z']+)([\s\S]*)$/);return m?{a:m[1],w:m[2],z:m[3]}:null};

function verbForms(it){
  const parts=String(it.v).toLowerCase().split(/\s+/),base=parts[0],S=new Set([base]);
  (it.f||[]).forEach(x=>String(x[1]).split(/\s+/).forEach(w=>{if(w.indexOf('**')>=0){const c=w.replace(/\*\*/g,'').replace(/[^A-Za-z']/g,'').toLowerCase();if(c)S.add(c)}}));
  [base+'s',base+'es',base+'ed',base+'d',base+'ing',base+base.slice(-1)+'ing',base+base.slice(-1)+'ed'].forEach(x=>S.add(x));
  if(/y$/.test(base)){S.add(base.slice(0,-1)+'ies');S.add(base.slice(0,-1)+'ied')}
  if(/e$/.test(base))S.add(base.slice(0,-1)+'ing');
  return {S,rest:parts.slice(1)};
}
function buildVprac(vf){
  const R=[];
  (vf.items||[]).forEach((it,vi)=>{
    if(!it.ex||!it.ex[0])return;
    const {S,rest}=verbForms(it),toks=String(it.ex[0]).split(/\s+/);
    for(let j=0;j<toks.length;j++){
      const c=core(toks[j]);if(!c||!S.has(c.w.toLowerCase()))continue;
      let span=[c.w],endTok=j;
      if(rest.length){
        let ok=true;for(let k=0;k<rest.length;k++){const d=toks[j+1+k]&&core(toks[j+1+k]);if(!d||d.w.toLowerCase()!==rest[k]){ok=false;break}}
        if(!ok)continue;
        for(let k=0;k<rest.length;k++)span.push(core(toks[j+1+k]).w);
        endTok=j+rest.length;
      }
      const last=core(toks[endTok]);
      const q=toks.slice(0,j).concat([c.a+'___'+last.z]).concat(toks.slice(endTok+1)).join(' ');
      R.push({vi,ic:it.ic,pt:it.ex[1],q,form:span.join(' '),note:it.note||''});
      break;
    }
  });
  if(R.length<3)return null;
  const r=rng(hashS(vf.items.map(x=>x.v).join('|')));
  return {k:'vprac',title:'Pratique os verbos',items:vf.items.map(x=>({v:x.v,pt:x.pt,ic:x.ic})),rounds:shuf(R,r),
    say:'Cada situação pede um verbo. Qual deles combina?'};
}
function buildXprac(xf){
  const items=xf.items||[],pool=[];
  items.forEach(it=>(it.b||[]).forEach(b=>pool.push(String(b[0]))));
  const R=[];
  items.forEach((it,i)=>{
    const w=(it.b||[]).map(b=>String(b[0]));if(w.length<2||!it.pt)return;
    const lw=w.map(x=>x.toLowerCase().replace(/[^a-z']/g,''));
    let hide=-1,wrong=null;
    if(it.slot!=null&&it.wr&&w[it.slot]){hide=it.slot;wrong=it.wr[0]}
    else if(it.no){
      const nt=String(it.no).split(/\s+/).map(x=>x.toLowerCase().replace(/[^a-z']/g,'')),ws=new Set(lw);
      const ei=nt.findIndex(x=>x&&!ws.has(x));
      if(ei>=0){
        wrong=String(it.no).split(/\s+/)[ei].replace(/[^A-Za-z']/g,'');
        const nxt=nt[ei+1];
        const bi=nxt!=null?lw.indexOf(nxt):-1;
        const ns=new Set(nt);
        const own=lw.findIndex(x=>!ns.has(x));
        hide=own>=0?own:(bi>=0?bi:-1);
      }else{
        const ns=new Set(nt);const own=lw.findIndex(x=>!ns.has(x));if(own>=0)hide=own;
      }
    }
    if(hide<0){let bl=-1;lw.forEach((x,j)=>{if(j>0&&x.length>bl){bl=x.length;hide=j}});if(hide<0)hide=w.length-1}
    const ans=w[hide],al=lw[hide];if(!al)return;
    const taken=new Set(lw);
    const opts=[ans];
    if(wrong&&wrong.toLowerCase()!==al&&!opts.some(o=>o.toLowerCase()===wrong.toLowerCase()))opts.push(wrong);
    if(it.slot!=null&&it.wr&&it.wr[1]&&!opts.some(o=>o.toLowerCase()===String(it.wr[1]).toLowerCase()))opts.push(it.wr[1]);
    const r0=rng(hashS(String(it.pt)+i));
    const cand=shuf(pool.filter(x=>x.length>1&&!taken.has(x.toLowerCase().replace(/[^a-z']/g,''))),r0);
    for(const x of cand){if(opts.length>=3)break;if(!opts.some(o=>o.toLowerCase()===x.toLowerCase()))opts.push(x)}
    if(opts.length<2)return;
    const o2=shuf(opts,r0);
    R.push({ic:it.ic,pt:it.pt,w,hide,opts:o2,a:o2.indexOf(ans),note:it.note||'',ex:it.ex||null});
  });
  if(R.length<3)return null;
  const r=rng(hashS(items.map(x=>x.pt).join('|')));
  return {k:'xprac',title:'Pratique as combinações',rounds:shuf(R,r),say:'Complete o bloco que falta e monte a combinação natural.'};
}
/* ---- práticas extras (verbos, combinações, laboratório de sons): montadas a partir dos dados do próprio episódio ---- */
const _cl=s=>String(s||'').replace(/\*\*/g,'');
const _nrm=s=>_cl(s).toLowerCase().replace(/[^a-z0-9']/g,'');
const _ing=b=>{b=b.toLowerCase();if(/ie$/.test(b))return b.slice(0,-2)+'ying';if(/[^e]e$/.test(b))return b.slice(0,-1)+'ing';if(/^(swim|win|run|sit|get|put|stop|plan)$/.test(b))return b+b.slice(-1)+'ing';return b+'ing'};
function _scramble(arr,r){let a=shuf(arr,r),t=0;while(a.length>1&&a.every((x,i)=>x===arr[i])&&t++<5)a=shuf(arr,r);return a}
function buildVdrill(vf){
  const items=vf.items||[],r=rng(hashS(items.map(x=>x.v).join('|')+'vd'));
  const F=[],B=[];
  items.forEach((it,vi)=>{
    const he=it.f&&it.f[1]&&it.f[1][1];
    if(he){
      const toks=String(he).split(/\s+/),j=toks.findIndex(t=>t.indexOf('**')>=0);
      if(j>=0){
        const t=toks[j],form=t.replace(/\*\*/g,'').replace(/[^A-Za-z']/g,''),base=String(it.v||'').split(/\s+/)[0].toLowerCase();
        const post=(t.split('**').pop()||'').replace(/[A-Za-z']/g,'');
        if(form&&base&&form.toLowerCase()!==base){
          const opts=[form,base];const g=_ing(base);if(g!==form&&g!==base)opts.push(g);
          const o2=shuf(opts,r),full=_cl(he);
          F.push({t:'pick',ic:it.ic,head:'QUEM FAZ A AÇÃO? ESCOLHA A FORMA',pt:it.pt+' · ele / ela / isso leva -s',q:toks.slice(0,j).concat(['___'+post]).concat(toks.slice(j+1)).map(_cl).join(' '),opts:o2,a:o2.indexOf(form),say:full,why:(it.note||'')+' → **'+full+'**'});
        }
      }
    }
    const ex=it.ex;
    if(ex&&ex[0]){
      const tk=_cl(ex[0]).split(/\s+/).filter(Boolean);
      if(tk.length>=3&&tk.length<=9)B.push({t:'build',ic:it.ic,head:'OUÇA E MONTE A FRASE',pt:ex[1],words:_scramble(tk,r),target:tk,say:_cl(ex[0]),auto:1,why:it.note||''});
    }
  });
  const R=shuf(F,r).concat(shuf(B,r));
  if(R.length<4)return null;
  return {k:'vdrill',title:'Treino dos verbos',rounds:R,say:'Agora treine a forma certa do verbo e monte frases com eles.'};
}
function buildXdrill(xf){
  const items=xf.items||[],r=rng(hashS(items.map(x=>x.pt).join('|')+'xd'));
  const N=[],B=[];
  items.forEach(it=>{
    const w=(it.b||[]).map(b=>String(b[0]));if(w.length<2||!it.pt)return;
    const nat=w.join(' ');
    if(it.no&&_nrm(it.no)!==_nrm(nat)){
      const o2=shuf([nat,String(it.no)],r);
      N.push({t:'pick',ic:it.ic,head:'QUAL SOA NATURAL EM INGLÊS?',pt:it.pt,opts:o2,a:o2.indexOf(nat),say:(it.ex&&it.ex[0])?_cl(it.ex[0]):nat,why:(it.note||'')+' → **'+nat+'**'});
    }
    const lw=new Set(w.map(_nrm));let extra=null;
    if(it.no){const x=String(it.no).split(/\s+/).find(t=>t&&!lw.has(_nrm(t)));if(x)extra=x.replace(/[^A-Za-z']/g,'');}
    const tiles=_scramble(extra?w.concat([extra]):w,r);
    B.push({t:'build',ic:it.ic,head:'MONTE A COMBINAÇÃO NATURAL',pt:it.pt,words:tiles,target:w,say:(it.ex&&it.ex[0])?_cl(it.ex[0]):nat,why:(it.note||'')+' → **'+nat+'**'});
  });
  const R=shuf(N,r).concat(shuf(B,r));
  if(R.length<4)return null;
  return {k:'xdrill',title:'Treino das combinações',rounds:R,say:'Escolha o que soa natural e monte as combinações do dia.'};
}
function buildSdrill(sl){
  const P2=(sl.pairs||[]).filter(p=>p&&p[0]&&p[1]),ex=sl.ex||[];
  if(P2.length<3)return null;
  const r=rng(hashS(String(sl.short||sl.title)+'sd')),R=[];
  const n=Math.min(5,P2.length);
  for(let i=0;i<n;i++){
    const A1=P2[i][0],B=P2[i][1],A2=P2[(i+1)%P2.length][0];
    if(A1===A2)continue;
    const o=shuf([{w:A1},{w:A2},{w:B}],r);
    R.push({t:'odd',head:'QUAL SOM É DIFERENTE?',opts:o,a:o.findIndex(x=>x.w===B),why:'**'+B+'** é o diferente. '+(P2[i][2]||'')});
  }
  ex.slice(0,4).forEach(x=>R.push({t:'say',w:x[0],ph:x[1]||'',pt:x[2]||'',tip:x[3]||''}));
  if(R.length<4)return null;
  return {k:'sdrill',title:'Treino do laboratório',rounds:R,short:sl.short||'',say:'Ouça três palavras, ache a diferente e depois repita em voz alta.'};
}
function injectPractice(e){
  try{
    if(!e||!e.fr||e._pr)return;e._pr=1;
    if(e.mdl===2){
      const vf=e.fr.find(f=>f.k==='verbs'),pf=e.fr.find(f=>f.k==='pat');
      
      e.fr.forEach(f=>{
        if(f.k==='xpr'&&!(f.then||[]).some(x=>x.k==='xprac')){const a=buildXprac(f),b=buildXdrill(f);f.then=(f.then||[]).concat([a,b].filter(Boolean))}
      });
      return;
    }
    if(e.mdl){
      e.fr.forEach(f=>{
        if(f.k==='verbs'&&!(f.then||[]).some(x=>x.k==='vprac')){const v=buildVprac(f);if(v)f.then=(f.then||[]).concat([v])}
        if(f.k==='xpr'&&!(f.then||[]).some(x=>x.k==='xprac')){const x=buildXprac(f);if(x)f.then=(f.then||[]).concat([x])}
        if(f.k==='verbs'&&!(f.then||[]).some(x=>x.k==='vdrill')){const v=buildVdrill(f);if(v)f.then=(f.then||[]).concat([v])}
        if(f.k==='xpr'&&!(f.then||[]).some(x=>x.k==='xdrill')){const x=buildXdrill(f);if(x)f.then=(f.then||[]).concat([x])}
        if(f.k==='soundlab'&&!(f.then||[]).some(x=>x.k==='sdrill')){const x=buildSdrill(f);if(x)f.then=(f.then||[]).concat([x])}
      });
      return;
    }
    const out=[];
    e.fr.forEach(f=>{
      out.push(f);
      if(f.k==='verbs'&&!e.fr.some(x=>x.k==='vprac')){const v=buildVprac(f);if(v)out.push(v)}
      if(f.k==='xpr'&&!e.fr.some(x=>x.k==='xprac')){const x=buildXprac(f);if(x)out.push(x)}
    });
    if(out.length!==e.fr.length){e.fr.length=0;out.forEach(x=>e.fr.push(x))}
  }catch(err){}
}
if(typeof window.fxBridge==='function'){const _fb=window.fxBridge;window.fxBridge=function(e){injectPractice(e);return _fb.apply(this,arguments)}}
if(window.PogTTS&&PogTTS.episodeTexts){
  const o2=PogTTS.episodeTexts;
  PogTTS.episodeTexts=function(e){
    injectPractice(e);
    const out=o2(e),seen=new Set(out.map(x=>x.text+'|'+(x.speaker||'')));
    const add=t=>{t=String(t||'').replace(/\*\*/g,'').trim();const k=t+'|';if(t&&t.length<400&&!seen.has(k)){seen.add(k);out.push({text:t,speaker:null})}};
    (e.fr||[]).forEach(f=>{
      if(f.k==='vprac')(f.rounds||[]).forEach(r=>add(String(r.q).replace('___',r.form)));
      if(f.k==='xprac')(f.rounds||[]).forEach(r=>{add(r.w.join(' '));if(r.ex)add(r.ex[0])});
      if(f.k==='vdrill'||f.k==='xdrill'||f.k==='sdrill')(f.rounds||[]).forEach(r=>{if(r.say)add(r.say);if(r.t==='odd')(r.opts||[]).forEach(o=>add(o.w));if(r.t==='say')add(r.w)});
    });
    return out;
  };
}

const PALV=['#7C4DFF','#12B3A8','#FF6F59','#E0499D','#2F8FE0'];
function slotHTML(){return `<span class="rw-slot" id="rwslot" aria-label="peça que falta"><i>?</i></span>`}
function sitHTML(ic,pt,label){
  return `<div class="rw-sit2"><span class="rw-sit2-ic" aria-hidden="true">${fxIcon(ic||'💬',54)}</span><div><small>${label}</small><p>${esc(pt)}</p></div></div>`;
}

FXR.vprac=function(f,st,n){
  const R=f.rounds,V=f.items,used=new Set();let ri=0,tries=0;
  const draw=()=>{
    const r=R[ri];tries=0;
    const toks=r.q.split(/\s+/);
    const pat=toks.map((t,i)=>{const m=t.match(/^(.*)___(.*)$/);
      return m?`${m[1]?`<span class="rw-pn">${esc(m[1])}</span>`:''}${slotHTML()}${m[2]?`<span class="rw-pn">${esc(m[2])}</span>`:''}`
        :`<span class="fx-blk" style="--b:${PALV[i%PALV.length]};--i:${i}">${esc(t)}</span>`}).join('');
    const free=V.map((v,i)=>[v,i]).filter(x=>!used.has(x[1]));
    st.innerHTML=`<div class="step fx">${fxKindBar(f,n)}<h2 class="fx-h">${esc(f.title)} <small>${ri+1}/${R.length}</small></h2>
      ${sitHTML(r.ic,r.pt,'SITUAÇÃO · QUAL VERBO ENTRA?')}
      <div class="rw-pat">${pat}</div>
      <div class="fx-opts g2">${free.map(([v,i])=>`<button type="button" class="fx-o rw-vo" data-i="${i}"><b>${esc(v.v)}</b><small>${esc(v.pt)}</small></button>`).join('')}</div>
      <div id="fb"></div><div id="rwmic" class="pv-host" hidden></div></div>`;
    const slot=st.querySelector('#rwslot');
    st.querySelectorAll('.rw-vo').forEach(b=>b.onclick=()=>{
      if(P.answered)return;
      const i=+b.dataset.i;
      if(i!==r.vi){tries++;b.disabled=true;b.classList.add('no');beep(false);
        fxGrade(false,tries>1?null:'Leia a situação em português e escolha o verbo com o mesmo sentido.',null);return}
      P.answered=true;used.add(i);
      st.querySelectorAll('.rw-vo').forEach(x=>{x.disabled=true;if(+x.dataset.i===i)x.classList.add('ok')});
      slot.classList.add('ok');slot.querySelector('i').textContent=r.form;
      if(tries===0)P.score++;
      const full=plain(r.q.replace('___',r.form));
      fxGrade(true,(r.note?r.note+' ':'')+'→ **'+full+'**',null);
      setTimeout(()=>fxSay(full),250);
      if(window.PogVoice&&PogVoice.supported()&&ri===R.length-1){
        const hm=st.querySelector('#rwmic');hm.hidden=false;
        hm.innerHTML='<div class="sl-h">🎤 Diga a última frase em voz alta</div><div class="pv-in"></div>';
        PogVoice.mount(hm.querySelector('.pv-in'),{target:full,lang:lang()});
      }
      cta(ri<R.length-1?'Próxima situação ▶':'Continuar',true,true);
    });
    P.answered=false;cta('Escolha o verbo certo',false);
  };
  P.fx.cta=()=>{if(P.answered&&ri<R.length-1){ri++;draw();return true}return false};
  draw();say(f.say||'Cada situação pede um verbo.');
};

FXR.xprac=function(f,st,n){
  const R=f.rounds;let ri=0,tries=0;
  const draw=()=>{
    const r=R[ri];tries=0;
    const pat=r.w.map((t,i)=>i===r.hide?slotHTML():`<span class="fx-blk" style="--b:${PALV[i%PALV.length]};--i:${i}">${esc(t)}</span>`).join('');
    st.innerHTML=`<div class="step fx">${fxKindBar(f,n)}<h2 class="fx-h">${esc(f.title)} <small>${ri+1}/${R.length}</small></h2>
      ${sitHTML(r.ic,r.pt,'COMO SE DIZ? ENCAIXE O BLOCO')}
      <div class="rw-pat">${pat}</div>
      <div class="fx-opts g2">${r.opts.map((o,i)=>`<button type="button" class="fx-o rw-xo" data-i="${i}"><b>${esc(o)}</b></button>`).join('')}</div>
      <div id="fb"></div><div id="rwmic" class="pv-host" hidden></div></div>`;
    const slot=st.querySelector('#rwslot');
    st.querySelectorAll('.rw-xo').forEach(b=>b.onclick=()=>{
      if(P.answered)return;
      const i=+b.dataset.i;
      if(i!==r.a){tries++;b.disabled=true;b.classList.add('no');beep(false);
        fxGrade(false,tries>1?(r.note||null):'Pense em como os nativos dizem. Qual bloco encaixa?',null);return}
      P.answered=true;
      st.querySelectorAll('.rw-xo').forEach((x,j)=>{x.disabled=true;if(j===r.a)x.classList.add('ok')});
      slot.classList.add('ok');slot.querySelector('i').textContent=r.opts[r.a];
      if(tries===0)P.score++;
      const full=r.w.join(' ');
      fxGrade(true,(r.note?r.note+' ':'')+'→ **'+full+'**',null);
      setTimeout(()=>fxSay(plain(full)),250);
      if(window.PogVoice&&PogVoice.supported()&&ri===R.length-1){
        const hm=st.querySelector('#rwmic');hm.hidden=false;
        hm.innerHTML='<div class="sl-h">🎤 Diga a última combinação em voz alta</div><div class="pv-in"></div>';
        PogVoice.mount(hm.querySelector('.pv-in'),{target:plain(full),lang:lang()});
      }
      cta(ri<R.length-1?'Próxima combinação ▶':'Continuar',true,true);
    });
    P.answered=false;cta('Escolha o bloco certo',false);
  };
  P.fx.cta=()=>{if(P.answered&&ri<R.length-1){ri++;draw();return true}return false};
  draw();say(f.say||'Complete a combinação natural.');
};


/* ---- renderer único das práticas extras ---- */
FX_KIND.vdrill=FX_KIND.xdrill=FX_KIND.sdrill='practice';
FX_LABEL.vdrill='Treino dos verbos';FX_LABEL.xdrill='Treino das combinações';FX_LABEL.sdrill='Treino dos sons';
function drillRun(f,st,n){
  const R=f.rounds;let ri=0;
  const next=lab=>cta(ri<R.length-1?lab:'Continuar',true,true);
  const draw=()=>{
    const r=R[ri];let tries=0,done=false;P.answered=false;clearTimeout(fxSeq.t);
    const h=`${fxKindBar(f,n)}<h2 class="fx-h">${esc(f.title)} <small>${ri+1}/${R.length}</small></h2>`;
    const goNext=()=>{if(done&&ri<R.length-1){ri++;draw();return true}return false};
    if(r.t==='pick'){
      const toks=r.q?r.q.split(/\s+/):null;
      const pat=toks?`<div class="rw-pat">${toks.map((t,i)=>{const m=t.match(/^(.*)___(.*)$/);return m?`${m[1]?`<span class="rw-pn">${esc(m[1])}</span>`:''}${slotHTML()}${m[2]?`<span class="rw-pn">${esc(m[2])}</span>`:''}`:`<span class="fx-blk" style="--b:${PALV[i%PALV.length]};--i:${i}">${esc(t)}</span>`}).join('')}</div>`:'';
      st.innerHTML=`<div class="step fx">${h}${sitHTML(r.ic,r.pt,r.head)}${pat}<div class="fx-opts g2">${r.opts.map((o,i)=>`<button type="button" class="fx-o rw-dp" data-i="${i}"><b>${esc(o)}</b></button>`).join('')}</div><div id="fb"></div></div>`;
      const slot=st.querySelector('#rwslot');
      st.querySelectorAll('.rw-dp').forEach(b=>b.onclick=()=>{
        if(done)return;const i=+b.dataset.i;
        if(i!==r.a){tries++;b.disabled=true;b.classList.add('no');beep(false);fxGrade(false,tries>1?'Releia a pista de cima e tente a outra opção.':'Quase! Pense na regra e escolha de novo.',null);return}
        done=true;P.answered=true;if(tries===0)P.score++;
        st.querySelectorAll('.rw-dp').forEach(x=>{x.disabled=true;if(+x.dataset.i===r.a)x.classList.add('ok')});
        if(slot){slot.classList.add('ok');slot.querySelector('i').textContent=r.opts[r.a]}
        fxGrade(true,r.why||null,null);setTimeout(()=>fxSay(plain(r.say||r.opts[r.a])),250);
        next('Próximo ▶');
      });
      P.fx.cta=goNext;cta('Escolha a resposta',false);
    }else if(r.t==='build'){
      const sel=[];let tn=0,checked=false;
      st.innerHTML=`<div class="step fx">${h}${sitHTML(r.ic,r.pt,r.head)}${r.auto?`<div class="rw-sph-ctl" style="margin:6px 0"><button type="button" class="pill light" id="rwhear">${spk} Ouvir a frase</button><button type="button" class="pill light" id="rwslow">🐢 Devagar</button></div>`:''}<div class="rw-pat" id="rwans"></div><div class="ctx-chips" id="rwtiles"></div><div id="fb"></div></div>`;
      const ans=st.querySelector('#rwans'),pool=st.querySelector('#rwtiles');
      const paint=()=>{
        ans.innerHTML=sel.length?sel.map((i,k)=>`<button type="button" class="fx-blk rw-bk" data-k="${k}" style="--b:${PALV[k%PALV.length]};--i:${k};cursor:pointer">${esc(r.words[i])}</button>`).join(''):'<span class="rw-pn">toque nas palavras na ordem certa…</span>';
        pool.innerHTML=r.words.map((w,i)=>`<button type="button" class="ctx-chip fx-o${sel.includes(i)?' used':''}" data-i="${i}">${esc(w)}</button>`).join('');
        ans.querySelectorAll('.rw-bk').forEach(b=>b.onclick=()=>{if(checked)return;sel.splice(+b.dataset.k,1);sfx('pop');paint()});
        pool.querySelectorAll('.ctx-chip').forEach(b=>b.onclick=()=>{if(checked||b.classList.contains('used'))return;sel.push(+b.dataset.i);sfx('key');paint()});
        cta(sel.length===r.target.length?'Conferir':'Monte a frase',sel.length===r.target.length,true);
      };
      if(r.auto){const hear=slow=>fxSay(plain(r.say),null,!!slow);st.querySelector('#rwhear').onclick=()=>hear(false);st.querySelector('#rwslow').onclick=()=>hear(true);setTimeout(()=>{if(st.isConnected)hear(false)},450)}
      paint();
      P.fx.cta=()=>{
        if(!checked){
          if(sel.length!==r.target.length)return true;
          const got=sel.map(i=>_nrm(r.words[i])),want=r.target.map(_nrm),ok=got.every((g,i)=>g===want[i]);
          if(ok){checked=true;done=true;P.answered=true;if(tn===0)P.score++;ans.querySelectorAll('.rw-bk').forEach(b=>b.classList.add('ok'));fxGrade(true,r.why||null,null);setTimeout(()=>fxSay(plain(r.say)),250);next('Próximo ▶');return true}
          tn++;
          if(tn>=3){checked=true;done=true;P.answered=true;fxGrade(false,r.why||null,r.target.join(' '));setTimeout(()=>fxSay(plain(r.say)),250);next('Próximo ▶');return true}
          fxGrade(false,tn>1?'Dica: comece pela primeira palavra e confira a ordem natural.':'Ainda não. Toque nas palavras para tirar e reorganize.',null);return true;
        }
        return goNext();
      };
    }else if(r.t==='odd'){
      let selI=-1,checked=false,timers=[];
      st.innerHTML=`<div class="step fx">${h}${fxEn('👂',r.head,'Ouça as três palavras. Duas têm o mesmo som; toque na que é <b>diferente</b>.')}<div class="rw-sph-ctl" style="margin:6px 0"><button type="button" class="pill light" id="rwhear">${spk} Ouvir as três</button></div><div class="fx-opts g3" id="rwodd">${r.opts.map((o,i)=>`<button type="button" class="fx-o rw-od" data-i="${i}"><b>${spk} ${i+1}</b><small class="rw-odw" hidden>${esc(o.w)}</small></button>`).join('')}</div><div id="fb"></div></div>`;
      const play3=()=>{timers.forEach(clearTimeout);timers=[];r.opts.forEach((o,i)=>timers.push(setTimeout(()=>{if(st.isConnected&&!checked)fxSay(o.w,null,true)},i*1600)))};
      st.querySelector('#rwhear').onclick=play3;setTimeout(()=>{if(st.isConnected)play3()},450);
      const bs=[...st.querySelectorAll('.rw-od')];
      bs.forEach(b=>b.onclick=()=>{if(checked)return;timers.forEach(clearTimeout);selI=+b.dataset.i;bs.forEach(x=>x.classList.toggle('sel',x===b));sfx('pop');fxSay(r.opts[selI].w,null,true);cta('Confirmar',true,true)});
      cta('Toque numa palavra',false);
      P.fx.cta=()=>{
        if(!checked){
          if(selI<0)return true;checked=true;done=true;P.answered=true;
          bs.forEach((x,i)=>{x.disabled=true;x.querySelector('.rw-odw').hidden=false;if(i===r.a)x.classList.add('ok');else if(i===selI)x.classList.add('no')});
          const ok=selI===r.a;if(ok)P.score++;
          fxGrade(ok,r.why||null,ok?null:r.opts[r.a].w);next('Próximo ▶');return true;
        }
        return goNext();
      };
    }else{ // say
      st.innerHTML=`<div class="step fx">${h}${fxEn('🎤','AGORA É A SUA VEZ','Ouça e repita em voz alta, imitando o som. Cada palavra é uma chance de treinar.')}
        <div class="fx-model"><div><small>${esc(r.ph)} · ${esc(r.pt)}</small><b style="font-size:1.6em">${esc(r.w)}</b>${r.tip?`<small>${mk(r.tip)}</small>`:''}</div><button type="button" class="say2" id="rwhear">${spk}</button></div>
        <div class="rw-sph-ctl" style="margin:6px 0"><button type="button" class="pill light" id="rwslow">🐢 Devagar</button></div>
        <div id="rwmic" class="pv-host"></div><div id="fb"></div></div>`;
      st.querySelector('#rwhear').onclick=()=>fxSay(r.w);st.querySelector('#rwslow').onclick=()=>fxSay(r.w,null,true);
      setTimeout(()=>{if(st.isConnected)fxSay(r.w)},450);
      if(window.PogVoice)PogVoice.mount(st.querySelector('#rwmic'),{target:r.w,lang:lang()});
      done=true;P.answered=true;next('Próxima palavra ▶');
      P.fx.cta=goNext;
    }
  };
  draw();say(f.say||'Vamos treinar.');
}
FXR.vdrill=FXR.xdrill=FXR.sdrill=drillRun;

/* ------------------------------------------------------------------ 6) modelo oficial: quadros encadeados ("then") e revisão do pai */
const _rfThen=window.renderFx;
window.renderFx=function(n,st,lang){
  const f=P.e.fr[n];
  if(!f||!f.then||!f.then.length)return _rfThen(n,st,lang);
  P.fx={n,cta:null};clearTimeout(fxSeq.t);
  const parts=[f].concat(f.then);let pi=0,inner=null;
  const wrapper=()=>{
    if(inner&&inner())return true;
    if(pi<parts.length-1){pi++;run();return true}
    return false;
  };
  Object.defineProperty(P.fx,'cta',{get:()=>wrapper,set:v=>{inner=v},configurable:true});
  const run=()=>{
    inner=null;const g=parts[pi],fn=FXR[g.k];
    P.answered=false;
    if(!fn){st.innerHTML='<div class="step"><p>Quadro indisponível.</p></div>';cta(P.t.cont,true);return}
    fn(g,st,n);
    try{fxEsHook(st)}catch(e){}
    try{const sc=document.querySelector('#pbody');if(sc)sc.scrollTop=0}catch(e){}
  };
  run();
};
const _ft3=window.fxTotal;
window.fxTotal=function(e){let n=_ft3(e);(e.fr||[]).forEach(f=>{if(f.then&&f.then.length)n+=_ft3({fr:f.then})+((f.then||[]).reduce((a,g)=>a+((g.k==='vprac'||g.k==='xprac'||g.k==='ppat')?(g.rounds||[]).length:g.k==='ctxv'?(g.items||[]).length:g.k==='sphr'?(g.blanks||[]).length:0),0))});return n};
if(window.PogTTS&&PogTTS.episodeTexts){
  const o3=PogTTS.episodeTexts;
  PogTTS.episodeTexts=function(e){
    const flat=[];(e.fr||[]).forEach(f=>{flat.push(f);(f.then||[]).forEach(g=>flat.push(g))});
    return o3(Object.assign({},e,{fr:flat}));
  };
}
/* selo "revisão do episódio anterior" nos verbos e combinações marcados com rev:true */
['verbs','xpr'].forEach(k=>{
  const o=FXR[k];if(!o)return;
  FXR[k]=function(f,st,n){
    o(f,st,n);
    try{
      const sel=k==='verbs'?'.vb-card':'.xp-tile',mainSel=k==='verbs'?'.vb-main':'.xp-pt',tag=st.querySelectorAll(sel);
      (f.items||[]).forEach((it,i)=>{if(it.rev&&tag[i]){const b=document.createElement('span');b.className='rw-rev';b.textContent='↺ revisão do episódio anterior';const m=tag[i].querySelector(mainSel)||tag[i];m.parentNode.insertBefore(b,m.nextSibling)}});
    }catch(e){}
  };
});

/* ------------------------------------------------------------------ 7) curso Inglés para hispanohablantes: três tipos de episódio
   decode (jerga), reg (registro) e tline (linha do tempo) são práticas próprias dos episódios de inglês jovem e de história */
FX_KIND.decode='practice';FX_LABEL.decode='Descifra la jerga';
FX_KIND.reg='practice';FX_LABEL.reg='¿Formal o casual?';
FX_KIND.tline='practice';FX_LABEL.tline='Línea del tiempo';
const micLast=(st,full)=>{
  if(window.PogVoice&&PogVoice.supported()){
    const hm=st.querySelector('#rwmic');if(!hm)return;hm.hidden=false;
    hm.innerHTML='<div class="sl-h">🎤 Dilo en voz alta</div><div class="pv-in"></div>';
    PogVoice.mount(hm.querySelector('.pv-in'),{target:full,lang:lang()});
  }
};
FXR.decode=function(f,st,n){
  const R=f.rounds;let ri=0,tries=0;
  const draw=()=>{
    const r=R[ri];tries=0;
    st.innerHTML=`<div class="step fx">${fxKindBar(f,n)}<h2 class="fx-h">${esc(f.title||'Descifra la jerga')}${R.length>1?` <small>${ri+1}/${R.length}</small>`:''}</h2>
      ${fxEn('💬','DESCIFRA LA JERGA',`¿Qué significa <b>${esc(r.term)}</b> aquí?`)}
      <div class="rw-msg">${r.who?`<b>${esc(r.who)}</b>`:''}<span>${mk(r.s)}</span><button type="button" class="rw-msg-p" aria-label="Escuchar">${spk}</button></div>
      <div class="fx-opts">${r.opts.map((o,i)=>`<button type="button" class="fx-o" data-i="${i}">${esc(o)}</button>`).join('')}</div>
      <div id="fb"></div><div id="rwmic" class="pv-host" hidden></div></div>`;
    st.querySelector('.rw-msg-p').onclick=()=>fxSay(plain(r.s));
    st.querySelectorAll('.fx-o').forEach(b=>b.onclick=()=>{
      if(P.answered)return;
      const i=+b.dataset.i;
      if(i!==r.a){tries++;b.disabled=true;b.classList.add('no');beep(false);
        fxGrade(false,(r.wf&&r.wf[i])||'Ojo: la jerga casi nunca se traduce palabra por palabra. Piensa en la situación.',null);return}
      P.answered=true;
      st.querySelectorAll('.fx-o').forEach((x,j)=>{x.disabled=true;if(j===r.a)x.classList.add('ok')});
      if(tries===0)P.score++;
      fxGrade(true,(r.why||'')+(r.lit?' (Literal: '+r.lit+'.)':''),null);
      setTimeout(()=>fxSay(plain(r.s)),250);
      if(ri===R.length-1)micLast(st,plain(r.s));
      cta(ri<R.length-1?'Siguiente ▶':'Continuar',true,true);
    });
    P.answered=false;cta('Elige el significado',false);
  };
  P.fx.cta=()=>{if(P.answered&&ri<R.length-1){ri++;draw();return true}return false};
  draw();say(f.say||'La jerga no se traduce palabra por palabra: busca el sentido.');
};
FXR.reg=function(f,st,n){
  const R=f.rounds;let ri=0,tries=0;
  const LV=[['🎩','Formal'],['🙂','Casual'],['📱','Jerga o chat']];
  const draw=()=>{
    const r=R[ri];tries=0;
    st.innerHTML=`<div class="step fx">${fxKindBar(f,n)}<h2 class="fx-h">${esc(f.title||'¿Formal o casual?')}${R.length>1?` <small>${ri+1}/${R.length}</small>`:''}</h2>
      ${fxEn('🎚️','REGISTRO','¿En qué tono suena esta frase? Escúchala y elige.')}
      <div class="rw-msg"><span>${mk(r.t)}</span><button type="button" class="rw-msg-p" aria-label="Escuchar">${spk}</button></div>
      <div class="rw-reg">${LV.map((l,i)=>`<button type="button" class="fx-o rw-lv" data-i="${i}"><i>${l[0]}</i><b>${l[1]}</b></button>`).join('')}</div>
      <div id="fb"></div></div>`;
    st.querySelector('.rw-msg-p').onclick=()=>fxSay(plain(r.t));
    setTimeout(()=>fxSay(plain(r.t)),300);
    st.querySelectorAll('.rw-lv').forEach(b=>b.onclick=()=>{
      if(P.answered)return;
      const i=+b.dataset.i;
      if(i!==r.a){tries++;b.disabled=true;b.classList.add('no');beep(false);
        fxGrade(false,(r.wf&&r.wf[i])||'Piensa: ¿se lo dirías a un jefe, a un amigo o en un chat?',null);return}
      P.answered=true;
      st.querySelectorAll('.rw-lv').forEach((x,j)=>{x.disabled=true;if(j===r.a)x.classList.add('ok')});
      if(tries===0)P.score++;
      fxGrade(true,r.why||'',null);
      cta(ri<R.length-1?'Siguiente ▶':'Continuar',true,true);
    });
    P.answered=false;cta('Elige el tono',false);
  };
  P.fx.cta=()=>{if(P.answered&&ri<R.length-1){ri++;draw();return true}return false};
  draw();say(f.say||'El mismo mensaje cambia según con quién hablas.');
};
FXR.tline=function(f,st,n){
  const I=f.items.map((x,i)=>({i,y:x[0],t:x[1],es:x[2]}));
  let pool=I.slice().sort(()=>Math.random()-.5);
  if(pool.every((x,k)=>x.i===k))pool.reverse();
  let nx=0,miss=0;
  const draw=()=>{
    st.innerHTML=`<div class="step fx">${fxKindBar(f,n)}<h2 class="fx-h">${esc(f.title||'Ordena la historia')}</h2>
      ${fxEn('⏳','LÍNEA DEL TIEMPO','Toca los hechos en el orden en que ocurrieron: del más antiguo al más reciente.')}
      <ol class="rw-tl">${I.map((x,k)=>`<li class="${k<nx?'on':''}" data-k="${k}"><b>${k<nx?esc(x.y):'?'}</b><span>${k<nx?mk(x.t):''}</span><small>${k<nx?esc(x.es):''}</small></li>`).join('')}</ol>
      <div class="rw-tp">${pool.filter(x=>x.i>=nx).map(x=>`<button type="button" class="fx-o" data-i="${x.i}">${mk(x.t)}</button>`).join('')}</div>
      <div id="fb"></div></div>`;
    st.querySelectorAll('.rw-tp .fx-o').forEach(b=>b.onclick=()=>{
      if(P.answered)return;
      const i=+b.dataset.i;
      if(i!==nx){miss++;b.classList.add('no');beep(false);setTimeout(()=>b.classList.remove('no'),500);
        fxGrade(false,f.hint||'Todavía no: piensa qué pasó antes.',null);return}
      sfx('pop');fxSay(plain(I[i].t));nx++;
      if(nx<I.length){draw();return}
      P.answered=true;if(miss===0)P.score++;draw();
      fxGrade(true,f.why||'¡Línea del tiempo completa!',null);
      cta('Continuar',true,true);
    });
    if(!P.answered)cta('Toca el primer hecho',false);
  };
  P.answered=false;P.fx.cta=()=>false;
  draw();say(f.say||'Ordena los hechos como en un libro de historia.');
};

/* textos de interface em português usados pelas camadas novas → espanhol (cursos com ui:'es') */
if(typeof FXES_MAP!=='undefined')Object.assign(FXES_MAP,{
'OUÇA E TOQUE':'ESCUCHA Y TOCA','Ouvir':'Escuchar','Toque em ▶ para ouvir a cena':'Toca ▶ para escuchar la escena','Player do diálogo':'Reproductor del diálogo','Tocar':'Reproducir',
'Fala anterior':'Frase anterior','Próxima fala':'Frase siguiente','Repetir esta fala':'Repetir esta frase','Velocidade':'Velocidad','Falar devagar':'Hablar despacio','Devagar':'Despacio',
'ORDENE O DIÁLOGO':'ORDENA EL DIÁLOGO','Toque em ▶ para ouvir a conversa':'Toca ▶ para escuchar la conversación','Dica: ver a primeira fala':'Pista: ver la primera frase','Sua ordem':'Tu orden','Falas':'Frases',
'Use o player: pause, volte uma fala ou toque numa fala para ouvir dali.':'Usa el reproductor: pausa, retrocede una frase o toca una frase para escuchar desde ahí.',
'Toque no microfone e fale':'Toca el micrófono y habla','TROQUE A PEÇA':'CAMBIA LA PIEZA','Mesmo padrão, peça nova. Complete conforme a situação:':'Mismo patrón, pieza nueva. Completa según la situación:',
'peça que falta':'pieza que falta','Escolha a peça certa':'Elige la pieza correcta','Próxima peça ▶':'Siguiente pieza ▶','O padrão não muda: troque só a peça.':'El patrón no cambia: solo cambia la pieza.',
'Releia a frase em português e procure a peça com o mesmo sentido.':'Relee la frase en español y busca la pieza con el mismo sentido.',
'SITUAÇÕES NOVAS':'SITUACIONES NUEVAS','Mesmo padrão, outras situações: ouça e preencha as lacunas.':'Mismo patrón, otras situaciones: escucha y completa los huecos.','Toque nas palavras para completar':'Toca las palabras para completar',
'OUÇA E COMPLETE':'ESCUCHA Y COMPLETA','Ouça a frase e toque na palavra que você escuta em cada lacuna.':'Escucha la frase y toca la palabra que oyes en cada hueco.','Ouça com atenção e complete a frase.':'Escucha con atención y completa la frase.',
'Isso! Próxima lacuna.':'¡Eso! Siguiente hueco.','Frase completa! Agora é a sua vez de falar.':'¡Frase completa! Ahora te toca hablar a ti.','Próxima situação ▶':'Siguiente situación ▶',
'SITUAÇÃO':'SITUACIÓN','Sua missão':'Tu misión','Comece com uma peça':'Empieza con una pieza','Escreva ou fale':'Escribe o habla','Confira os objetivos':'Revisa los objetivos','Compare com o modelo':'Compara con el modelo',
'Toque para começar a frase':'Toca para empezar la frase','🎤 Falar em vez de escrever':'🎤 Hablar en vez de escribir','Objetivos (toque para marcar)':'Objetivos (toca para marcar)',
'🤖 Corrigir meu texto':'🤖 Corregir mi texto','👀 Ver o modelo e comparar':'👀 Ver el modelo y comparar','Modelo':'Modelo','Você escreveu':'Escribiste','Escreva em inglês, ou toque em 🎤 e fale':'Escribe en inglés, o toca 🎤 y habla',
'MONTE A FRASE':'ARMA LA FRASE','Ouvir e escrever treina o ouvido e a ortografia ao mesmo tempo.':'Escuchar y escribir entrena el oído y la ortografía al mismo tiempo.','Ouça o diálogo e monte a conversa na ordem certa.':'Escucha el diálogo y ordena la conversación.','OUÇA E ESCREVA':'ESCUCHA Y ESCRIBE','Poggie, o ornitorrinco':'Poggie, el ornitorrinco',
'Do laboratório de sons':'Del laboratorio de sonidos','Frase de treino':'Frase de práctica','Repita em voz alta':'Repite en voz alta','🎤 Agora diga a frase em voz alta':'🎤 Ahora di la frase en voz alta',
'Próxima combinação ▶':'Siguiente combinación ▶','Complete a frase':'Completa la frase','Complete a combinação natural.':'Completa la combinación natural.','Cada situação pede um verbo.':'Cada situación pide un verbo.',
'Escolha o bloco certo':'Elige el bloque correcto','Escolha o verbo certo':'Elige el verbo correcto','Pense em como os nativos dizem. Qual bloco encaixa?':'Piensa cómo lo dicen los nativos. ¿Qué bloque encaja?',
'Leia a situação em português e escolha o verbo com o mesmo sentido.':'Lee la situación en español y elige el verbo con el mismo sentido.','Ouça de novo: repare no som que muda entre as duas palavras.':'Escucha de nuevo: fíjate en el sonido que cambia entre las dos palabras.'
});


const _ft5=window.fxTotal;
window.fxTotal=function(e){let n=_ft5(e);(e.fr||[]).forEach(f=>(f.then||[]).forEach(g=>{if(g.k==='vdrill'||g.k==='xdrill'||g.k==='sdrill')n+=(g.rounds||[]).filter(r=>r.t!=='say').length}));return n};
window.RWB={makePlayer,ico,buildVprac,buildVdrill,buildXprac,buildXdrill,buildSdrill};
})();
