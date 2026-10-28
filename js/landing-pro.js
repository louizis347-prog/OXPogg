/* Landing: celulares realistas (moldura, ilha dinâmica, barra de status, botões laterais, reflexo), telas cheias e animadas,
   tutorial passo a passo e menu do topo com indicador deslizante. Depende de HomeArt e PogObra. */
(function(){
'use strict';
const $=(s,r)=>(r||document).querySelector(s),$$=(s,r)=>[].slice.call((r||document).querySelectorAll(s));
const reduce=()=>{try{return matchMedia('(prefers-reduced-motion:reduce)').matches}catch(e){return false}};
if(!window.HomeArt||!window.PogObra)return;
const ART=PogObra.svg(7009801,'obra-cover'),ARTP=PogObra.svg(7009801,'sticker'),ART2=PogObra.svg(9801,'obra-cover'),FACE=id=>PogObra.face(id);

/* ---------- aparelho ---------- */
const SB=`<span class="sb-i"><svg viewBox="0 0 18 12" width="1.7em" height="1.1em"><rect x="0" y="8" width="3" height="4" rx="1"/><rect x="5" y="5.5" width="3" height="6.5" rx="1"/><rect x="10" y="3" width="3" height="9" rx="1"/><rect x="15" y="0" width="3" height="12" rx="1"/></svg><svg viewBox="0 0 16 12" width="1.5em" height="1.1em"><path d="M8,11.4 L5.6,8.7 A3.6,3.6 0 0 1 10.4,8.7Z M2.6,6 A7.2,7.2 0 0 1 13.4,6 L11.9,7.4 A5,5 0 0 0 4.1,7.4Z M0.3,3.4 A10.4,10.4 0 0 1 15.7,3.4 L14.2,4.8 A8.4,8.4 0 0 0 1.8,4.8Z"/></svg><svg viewBox="0 0 27 12" width="2.3em" height="1.1em"><rect x=".6" y=".6" width="22" height="10.8" rx="3.2" fill="none" stroke="currentColor" opacity=".5"/><rect x="2.2" y="2.2" width="17" height="7.6" rx="2" fill="currentColor"/><rect x="24" y="4" width="2" height="4" rx="1" fill="currentColor" opacity=".5"/></svg></span>`;
function device(inner,o){
  o=o||{};
  return `<div class="dv ${o.cls||''}" ${o.attr||''}><span class="dv-b l1"></span><span class="dv-b l2"></span><span class="dv-b l3"></span><span class="dv-b r1"></span>
  <div class="dv-fr"><div class="dv-scr"><div class="dv-isl"><i></i></div><div class="dv-sb"><b>9:41</b>${SB}</div>${inner}<span class="dv-home"></span></div></div><span class="dv-gl"></span></div>`;
}
const bar=(n,t,close)=>`<div class="sx-bar"><span class="sx-x">${close===false?'':'✕'}</span><div class="sx-seg">${Array.from({length:6},(_,i)=>`<i class="${i<n?'on':''}"></i>`).join('')}</div><b>${t}</b></div>`;

/* ---------- telas ---------- */
const SCR={
 cover:()=>`<div class="sx sx-cover">${bar(1,'Capa 1/19')}
  <div class="sx-art">${ARTP}<span class="sx-tag">📖 Alice's Adventures in Wonderland · 1865</span><span class="sx-play">▶</span></div>
  <span class="sx-chip">EP 2 · A1</span><h4>Quem está aí?<br>Are you…?</h4><p class="sx-sub">Em 10 minutos você faz perguntas como a Alice.</p>
  <div class="sx-say"><span class="sx-av">${FACE('alice')}</span><div><small>Alice</small><b>Wait! Are you in a hurry?</b><em>Espere! Você está com pressa?</em></div><i>🔊</i></div>
  <div class="sx-cta">Começar o episódio</div></div>`,
 home:()=>`<div class="sx sx-home"><div class="sx-hd">${HomeArt.logo({size:26})}<span class="sx-coins">${window.PogCoins?'':''}<svg width="1.5em" height="1.5em" viewBox="0 0 32 32"><circle cx="16" cy="16" r="14" fill="#FFB627" stroke="#9A5A00" stroke-width="2.4"/><path d="M12.6,22.5 L12.6,9.8 L17.6,9.8 Q22,9.8 22,14 Q22,18.2 17.6,18.2 L12.6,18.2" fill="none" stroke="#9A5A00" stroke-width="2.8" stroke-linecap="round"/></svg>120</span></div>
  <div class="sx-land"><div class="sx-sc">${HomeArt.scene()}</div><span class="sx-chip2">Episódios de 10 minutos</span><h4>Que bom te<br>ver de volta</h4><div class="sx-pog">${HomeArt.mascot({scarf:'#FF7A45'})}</div></div>
  <div class="sx-cont"><div class="sx-th">${ART2}</div><div><small>CONTINUE DE ONDE PAROU</small><b>Quem é você? · I'm</b><span class="sx-pr"><i></i></span></div></div>
  <div class="sx-q">${['listen','review','shelf','rank'].map(k=>`<span style="--t1:${HomeArt.QT[k][0]};--t2:${HomeArt.QT[k][1]}"><svg viewBox="0 0 48 48">${HomeArt.QI[k]}</svg></span>`).join('')}</div>
  <div class="sx-today"><div class="sx-ring"><svg viewBox="0 0 40 40"><circle cx="20" cy="20" r="16" fill="none" stroke="#E6EEE9" stroke-width="5"/><circle cx="20" cy="20" r="16" fill="none" stroke="#16B58F" stroke-width="5" stroke-linecap="round" stroke-dasharray="100.5" stroke-dashoffset="40" transform="rotate(-90 20 20)"/></svg><b>60%</b></div><div><small>META DO DIA</small><b>12/20 XP</b></div><span class="sx-btn">Continuar</span></div></div>`,
 scene:()=>`<div class="sx sx-scene">${bar(2,'Cena 2/19')}
  <div class="sx-strip">${ART}<span class="sx-tag">📖 Alice's Adventures in Wonderland</span></div>
  <div class="sx-chat">
   <div class="sx-b l" style="--d:.15s"><span class="sx-av">${FACE('alice')}</span><div><small>Alice</small><b>Wait! Are you in a hurry?</b><em>Espere! Você está com pressa?</em></div><i>🔊</i></div>
   <div class="sx-b r" style="--d:.9s"><span class="sx-av">${FACE('rabbit')}</span><div><small>Coelho Branco</small><b>Yes, I am. I'm late!</b><em>Sim, estou. Estou atrasado!</em></div><i>🔊</i></div>
   <div class="sx-b l" style="--d:1.7s"><span class="sx-av">${FACE('alice')}</span><div><small>Alice</small><b>Are you new here?</b><em>Você é novo aqui?</em></div><i>🔊</i></div></div>
  <div class="sx-ctl"><span>🐢 Devagar</span><span class="sx-pl">▶ Ouvir a cena</span><span>Aa Tradução</span></div></div>`,
 rule:()=>`<div class="sx sx-rule">${bar(3,'Padrão 3/19')}
  <h4>Perguntar com <mark>Are you…?</mark></h4>
  <div class="sx-eq"><span class="k1">Are you</span><span class="k2">in a hurry</span><span class="k3">?</span></div>
  <p class="sx-hint">Troque as peças coloridas e invente frases novas.</p>
  <div class="sx-mold"><div class="blk k1">Are you <i>⟳</i></div><div class="blk k2" style="--d:.5s">tired <i>⟳</i></div><div class="blk k3" style="--d:1s">?</div></div>
  <div class="sx-out"><small>VOCÊ MONTOU</small><b>Are you tired?</b><em>Você está cansado?</em><i>🔊</i></div>
  <div class="sx-tiles"><span>Are you ready?</span><span>Are you hungry?</span><span>Are you new?</span></div></div>`,
 quiz:()=>`<div class="sx sx-quiz">${bar(4,'Prática 5/19')}
  <div class="sx-top"><b>O que ficou claro?</b><span class="sx-n">1/3</span></div>
  <div class="sx-qc"><p>Who is late? <i>🔊</i></p><small>Quem está atrasado?</small>
   <div class="sx-o" style="--d:.2s">😺 The Cat</div><div class="sx-o ok" style="--d:.2s">🐰 The Rabbit <i>✓</i></div><div class="sx-o" style="--d:.2s">👧 Alice</div></div>
  <div class="sx-react"><span class="sx-av">${FACE('alice')}</span><b>Curiosíssimo… e certo!</b></div>
  <div class="sx-feed"><span class="sx-combo">⚡ Sequência ×3</span><span class="sx-gain">🪙 +10</span></div>
  <div class="sx-dots"><i class="on"></i><i class="on"></i><i class="on"></i><i></i><i></i></div></div>`,
 speak:()=>`<div class="sx sx-speak">${bar(5,'Sons 14/19')}
  <h4>Laboratório de sons</h4><p class="sx-sub">Ouça, repita e veja o quanto você chegou perto.</p>
  <div class="sx-word">“Are you in a <mark>hurry</mark>?”</div>
  <div class="sx-wave">${Array.from({length:21},(_,i)=>`<i style="--h:${22+((i*37)%58)}%;--d:${(i%7)*.12}s"></i>`).join('')}</div>
  <div class="sx-ph"><span>/ɑːr/</span><span>/juː/</span><span class="hl">/ˈhɝː.i/</span></div>
  <div class="sx-mic"><i></i><i></i><span>🎤</span></div><small class="sx-cap">Toque e fale</small>
  <div class="sx-score"><b>92%</b><span>Boa pronúncia!</span></div></div>`,
 end:()=>`<div class="sx sx-end">${bar(6,'Resultado',false)}
  <div class="sx-medal"><span class="sx-ray"></span><b>🥇</b><strong>Medalha de ouro</strong><small>14 de 15 respostas de primeira</small></div>
  <div class="sx-gain2"><svg width="1.6em" height="1.6em" viewBox="0 0 32 32"><circle cx="16" cy="16" r="14" fill="#FFB627" stroke="#9A5A00" stroke-width="2.4"/><path d="M12.6,22.5 L12.6,9.8 L17.6,9.8 Q22,9.8 22,14 Q22,18.2 17.6,18.2 L12.6,18.2" fill="none" stroke="#9A5A00" stroke-width="2.8" stroke-linecap="round"/></svg><b>+14 Pogcoins</b></div>
  <div class="sx-st"><div class="sx-sa">${ARTP}<span class="sx-stars">★★★</span></div><b>Alice's Adventures in Wonderland</b><small>FIGURINHA DOURADA · Nº 002</small></div>
  <div class="sx-cta">Próximo episódio</div>
  <i class="sx-sp s1">✦</i><i class="sx-sp s2">✦</i><i class="sx-sp s3">★</i><i class="sx-sp s4">✦</i></div>`
};

/* ---------- herói ---------- */
function hero(){
  const st=$('.hero2 .stage');if(!st)return;
  st.innerHTML=`<div class="st-glow"></div>${device(SCR.home(),{cls:'back'})}${device(SCR.cover(),{cls:'front'})}
   <div class="hero-pog" aria-hidden="true">${HomeArt.mascot({scarf:'#FF7A45'})}</div>
   <span class="chip2 c-top">Aprenda pela cultura <b>✦</b></span><span class="chip2 c-bot"><b>10 min</b> por episódio</span><span class="chip2 c-mid">🪙 +10 Pogcoins</span>`;
  if(reduce())return;
  st.addEventListener('pointermove',e=>{const r=st.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;st.style.setProperty('--rx',(-y*7).toFixed(2)+'deg');st.style.setProperty('--ry',(x*9).toFixed(2)+'deg')});
  st.addEventListener('pointerleave',()=>{st.style.setProperty('--rx','0deg');st.style.setProperty('--ry','0deg')});
}

/* ---------- tutorial ---------- */
const STEPS=[
 {k:'cover',acc:'#0B7C88',chips:['📖 Obra de verdade','🎬 Capa ilustrada']},
 {k:'scene',acc:'#3E7BE0',chips:['🔊 Voz nativa','Aa Tradução']},
 {k:'rule',acc:'#E0647E',chips:['🧩 Troque as peças','✨ Frases novas']},
 {k:'quiz',acc:'#16B58F',chips:['🪙 +10 Pogcoins','⚡ Sequência ×3']},
 {k:'speak',acc:'#FF7A45',chips:['🎤 Fale no microfone','92% de acerto']},
 {k:'end',acc:'#D9901A',chips:['🥇 Medalha','🎴 Figurinha nova']}
];
function tutorial(){
  const sec=$('#tutorial');if(!sec)return;
  const stage=$('.tut-stage',sec),btns=$$('#tutSteps button',sec);if(!stage||!btns.length)return;
  stage.innerHTML=`<div class="tp-wrap"><div class="tp-blob"></div>${device('<div class="tp-screen" id="tutScreen"></div>',{cls:'tut'})}
   <span class="tp-chip a" id="tpA"></span><span class="tp-chip b" id="tpB"></span><div class="tp-pog" aria-hidden="true">${HomeArt.mascot({scarf:'#FF7A45'})}</div></div>
   <div class="tut-bar" aria-hidden="true"><i id="tutBar"></i></div>
   <div class="acts"><a class="btn primary lg sun" href="app.html">Experimentar um episódio <i aria-hidden="true">→</i></a></div>`;
  const scr=$('#tutScreen'),barEl=$('#tutBar'),ca=$('#tpA'),cb=$('#tpB');
  let cur=0,t0=0,paused=false,raf=0;const DUR=6500;
  function show(i,auto){
    cur=i;const s=STEPS[i];
    btns.forEach((b,k)=>{b.classList.toggle('on',k===i);b.classList.toggle('done',k<i);b.setAttribute('aria-current',k===i?'step':'false')});
    sec.style.setProperty('--acc',s.acc);
    scr.classList.remove('in');scr.innerHTML=SCR[s.k]();void scr.offsetWidth;scr.classList.add('in');
    [ca,cb].forEach((c,k)=>{c.classList.remove('in');c.textContent=s.chips[k];void c.offsetWidth;c.classList.add('in')});
    t0=performance.now();
  }
  function loop(t){
    if(!paused){const p=Math.min(1,(t-t0)/DUR);barEl.style.width=(p*100)+'%';const on=btns[cur];if(on)on.style.setProperty('--p',(p*100).toFixed(1));if(p>=1)show((cur+1)%STEPS.length,true)}
    raf=requestAnimationFrame(loop);
  }
  btns.forEach((b,k)=>b.addEventListener('click',()=>show(k)));
  const grid=$('.tut-grid',sec);
  grid.addEventListener('pointerenter',()=>{paused=true});
  grid.addEventListener('pointerleave',()=>{paused=false;t0=performance.now()-((parseFloat(barEl.style.width)||0)/100)*DUR});
  grid.addEventListener('focusin',()=>{paused=true});grid.addEventListener('focusout',()=>{paused=false});
  show(0);
  if(reduce()){paused=true;barEl.style.width='100%'}
  new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){if(!raf)raf=requestAnimationFrame(loop)}else{cancelAnimationFrame(raf);raf=0}}),{threshold:.2}).observe(grid);
}

/* ---------- menu do topo ---------- */
function menu(){
  const top=$('.top');if(!top)return;
  const nav=$('.nav',top);if(nav){
    const ind=document.createElement('span');ind.className='nav-ind';nav.prepend(ind);
    const links=$$('a',nav);let active=null;
    const move=a=>{if(!a){ind.style.opacity=0;return}const r=a.getBoundingClientRect(),n=nav.getBoundingClientRect();ind.style.opacity=1;ind.style.width=r.width+'px';ind.style.transform=`translateX(${r.left-n.left}px)`};
    links.forEach(a=>{a.addEventListener('pointerenter',()=>move(a));a.addEventListener('focus',()=>move(a))});
    nav.addEventListener('pointerleave',()=>move(active));
    const secs=links.map(a=>$(a.getAttribute('href'))).filter(Boolean);
    const spy=()=>{let cur=null;const y=innerHeight*.35;secs.forEach((s,i)=>{const r=s.getBoundingClientRect();if(r.top<=y&&r.bottom>y)cur=links.find(a=>a.getAttribute('href')==='#'+s.id)});if(cur!==active){links.forEach(a=>a.classList.toggle('on',a===cur));active=cur;move(active)}};
    addEventListener('scroll',spy,{passive:true});addEventListener('resize',()=>move(active));setTimeout(spy,300);
  }
  const onS=()=>top.classList.toggle('scrolled',scrollY>8);addEventListener('scroll',onS,{passive:true});onS();
  /* menu no celular */
  const right=$('.right',top);
  if(right&&nav){
    const bt=document.createElement('button');bt.type='button';bt.className='iconbtn burger';bt.setAttribute('aria-label','Abrir menu');bt.setAttribute('aria-expanded','false');bt.innerHTML='<i></i><i></i><i></i>';
    right.prepend(bt);
    const sheet=document.createElement('div');sheet.className='nav-sheet';sheet.innerHTML=$$('a',nav).map(a=>`<a href="${a.getAttribute('href')}">${a.textContent}</a>`).join('');top.appendChild(sheet);
    const set=o=>{top.classList.toggle('open',o);bt.setAttribute('aria-expanded',o)};
    bt.addEventListener('click',()=>set(!top.classList.contains('open')));sheet.addEventListener('click',e=>{if(e.target.closest('a'))set(false)});
  }
}

hero();tutorial();menu();
window.LandingPro={device,SCR};
})();
