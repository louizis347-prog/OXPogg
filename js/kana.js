/* Pogglot · alfabetização em japonês: kintro (apresentação), ktrace (traçar), klisten (ouvir e escolher), kmatch (kana ↔ romaji), kwords (ler palavras) */
(function(){
if(typeof FXR==='undefined'||typeof FX_KIND==='undefined')return;
const L={kintro:'Novos caracteres',ktrace:'Traçar',klisten:'Ouça e escolha',kmatch:'Kana e romaji',kwords:'Ler palavras'};
Object.keys(L).forEach(k=>{FX_KIND[k]='practice';FX_LABEL[k]=L[k]});
const q=(s,r)=>(r||document).querySelector(s);
const H=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const say2=(t,slow)=>{try{fxSay(String(t),null,slow)}catch(e){}};
const win=label=>{P.fx.done=true;P.score++;try{sfx('tada');confetti(60)}catch(e){}cta(label||'Continuar',true,true)};
const lock=()=>{P.fx.done=false;P.fx.cta=()=>!P.fx.done};
const theme=f=>`style="--g1:${(f.g||['#E84393','#FD79A8'])[0]};--g2:${(f.g||['#E84393','#FD79A8'])[1]}"`;
const head=(f,n,t)=>`${fxKindBar(f,n)}<h2 class="fx-h">${H(f.title||t)}</h2>`;
const shuf=a=>{try{return fxShuffle(a.slice())}catch(e){return a.slice().sort(()=>Math.random()-.5)}};
const css=document.createElement('style');css.textContent=`
.kx{--g1:#E84393;--g2:#FD79A8;padding-bottom:12px}
.kx-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;margin:12px 0}
.kx-c{border:0;border-radius:18px;background:#fff;box-shadow:0 6px 16px rgba(40,30,90,.12);padding:10px 2px;cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:2px}
.kx-c b{font:900 30px/1.1 "Noto Sans JP","Hiragino Sans","Yu Gothic",system-ui,sans-serif;color:#25203f}.kx-c small{font:800 11px system-ui;opacity:.6;color:#25203f}
.kx-c.seen{background:linear-gradient(135deg,var(--g1),var(--g2))}.kx-c.seen b,.kx-c.seen small{color:#fff;opacity:1}
.kx-big{background:#fff;border-radius:26px;box-shadow:0 10px 30px rgba(40,30,90,.14);padding:16px;margin:10px 0;text-align:center}
.kx-big .ch{font:900 110px/1.05 "Noto Sans JP","Hiragino Sans","Yu Gothic",system-ui,sans-serif;color:var(--g1)}
.kx-big .ro{font:900 26px system-ui;color:#25203f}.kx-big .mn{margin:8px 0;font:600 14.5px/1.4 system-ui;color:#4a4468}
.kx-big .ex{display:inline-flex;align-items:center;gap:8px;background:#f4f1ff;border-radius:16px;padding:8px 12px;font:800 15px system-ui;color:#25203f;cursor:pointer}
.kx-big .ex em{font-style:normal;font:600 12px system-ui;opacity:.7}
.kx-cv{position:relative;width:260px;height:260px;margin:10px auto;border-radius:22px;background:#fff;box-shadow:0 8px 22px rgba(40,30,90,.14);touch-action:none}
.kx-cv .gh{position:absolute;inset:0;display:grid;place-items:center;font:900 190px/1 "Noto Sans JP","Hiragino Sans","Yu Gothic",system-ui,sans-serif;color:#e7e3f3;user-select:none;pointer-events:none}
.kx-cv .gd{position:absolute;inset:0;pointer-events:none;background:linear-gradient(#0000 49.4%,#e1dcf0 49.4% 50.6%,#0000 50.6%),linear-gradient(90deg,#0000 49.4%,#e1dcf0 49.4% 50.6%,#0000 50.6%);border-radius:22px}
.kx-cv canvas{position:absolute;inset:0;width:100%;height:100%;border-radius:22px;touch-action:none}
.kx-q{font:900 64px/1.1 "Noto Sans JP","Hiragino Sans","Yu Gothic",system-ui,sans-serif;text-align:center;margin:18px 0;color:#25203f}
.kx-opts{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;margin:10px 0}
.kx-opt{border:0;border-radius:20px;background:#fff;box-shadow:0 6px 16px rgba(40,30,90,.12);padding:16px 8px;font:900 40px "Noto Sans JP","Hiragino Sans","Yu Gothic",system-ui,sans-serif;color:#25203f;cursor:pointer}
.kx-opt.sm{font:800 16px system-ui}.kx-opt.ok{background:#d9f8e5;outline:3px solid #2cc673}.kx-opt.no{background:#ffe0e0;outline:3px solid #ff6b6b;animation:kxs .3s}
@keyframes kxs{25%{transform:translateX(-6px)}75%{transform:translateX(6px)}}
.kx-pair{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:10px 0}.kx-col{display:flex;flex-direction:column;gap:8px}
.kx-pb{border:0;border-radius:16px;background:#fff;box-shadow:0 5px 14px rgba(40,30,90,.12);padding:12px;font:900 28px "Noto Sans JP","Hiragino Sans","Yu Gothic",system-ui,sans-serif;color:#25203f;cursor:pointer}
.kx-pb.r{font:900 20px system-ui}.kx-pb.sel{outline:3px solid var(--g1)}.kx-pb.fd{opacity:.35;pointer-events:none;background:#d9f8e5}
.kx-w{font:900 46px/1.15 "Noto Sans JP","Hiragino Sans","Yu Gothic",system-ui,sans-serif;text-align:center;margin:14px 0;color:#25203f}
`;document.head.appendChild(css);

/* 1 · apresentação dos caracteres */
FXR.kintro=function(f,st,n){
  const C=f.chars,seen=new Set();lock();
  st.innerHTML=`<div class="step fx nbx kx" ${theme(f)}>${head(f,n,'Novos caracteres')}<div class="nb-hint">${H(f.note||'Toque em cada caractere para ver e ouvir.')}</div>
  <div class="kx-grid">${C.map((x,i)=>`<button class="kx-c" data-i="${i}"><b>${H(x.c)}</b><small>${H(x.r)}</small></button>`).join('')}</div><div id="kxd"></div></div>`;
  const show=i=>{const x=C[i];seen.add(i);st.querySelectorAll('.kx-c')[i].classList.add('seen');
    q('#kxd',st).innerHTML=`<div class="kx-big"><div class="ch">${H(x.c)}</div><div class="ro">${H(x.r)}</div><div class="mn">${H(x.m||'')}</div>
    ${x.w?`<div class="ex" id="kxex">${H(x.w[3]||'')} <span>${H(x.w[0])}</span> <em>${H(x.w[1])} · ${H(x.w[2])}</em> 🔊</div>`:''}
    <div class="nb-tools" style="justify-content:center;margin-top:8px"><button class="nb-chip" id="kxs">🔊 Ouvir som</button><button class="nb-chip" id="kxsl">🐢 Devagar</button></div></div>`;
    q('#kxs',st).onclick=()=>say2(x.s||x.c);q('#kxsl',st).onclick=()=>say2(x.s||x.c,true);const ex=q('#kxex',st);if(ex)ex.onclick=()=>say2(x.w[0]);
    say2(x.s||x.c);if(seen.size>=C.length){P.fx.done=true;cta('Continuar',true,true)}};
  st.querySelectorAll('.kx-c').forEach(b=>b.onclick=()=>show(+b.dataset.i));
  cta('Toque em todos',false);say('Toque em cada caractere: ouça o som e veja a dica.')};

/* 2 · traçar sobre o modelo */
FXR.ktrace=function(f,st,n){
  const C=f.chars;let ri=0;lock();
  const draw=()=>{const x=C[ri];let drew=0;
    st.innerHTML=`<div class="step fx nbx kx" ${theme(f)}>${head(f,n,'Traçar')}<div class="nb-prog">${C.map((_,i)=>`<i class="${i<ri?'on':''}"></i>`).join('')}</div>
    <div class="nb-hint" style="text-align:center">Trace por cima do modelo com o dedo ou o mouse. <b>${H(x.r)}</b></div>
    <div class="kx-cv" id="kxcv"><div class="gh">${H(x.c)}</div><div class="gd"></div><canvas id="kxc" width="520" height="520"></canvas></div>
    <div class="nb-tools" style="justify-content:center"><button class="nb-chip" id="kxs">🔊 Ouvir</button><button class="nb-chip" id="kxcl">↩︎ Apagar</button><button class="nb-chip" id="kxg">👁️ Modelo</button></div></div>`;
    const cv=q('#kxc',st),ctx=cv.getContext('2d');ctx.lineWidth=26;ctx.lineCap='round';ctx.lineJoin='round';ctx.strokeStyle=(f.g||['#E84393'])[0];
    let on=false,last=null;const pos=e=>{const r=cv.getBoundingClientRect();return[(e.clientX-r.left)*cv.width/r.width,(e.clientY-r.top)*cv.height/r.height]};
    cv.onpointerdown=e=>{on=true;last=pos(e);cv.setPointerCapture&&cv.setPointerCapture(e.pointerId);ctx.beginPath();ctx.moveTo(last[0],last[1]);ctx.lineTo(last[0]+.1,last[1]+.1);ctx.stroke()};
    cv.onpointermove=e=>{if(!on)return;const p=pos(e);ctx.beginPath();ctx.moveTo(last[0],last[1]);ctx.lineTo(p[0],p[1]);ctx.stroke();last=p;drew++;if(drew===8){cta(ri<C.length-1?'Próximo ▶':'Concluir',true,true);P.fx.cta=()=>{ri++;if(ri<C.length){draw();return true}P.fx.cta=()=>!P.fx.done;win();return false}}};
    cv.onpointerup=cv.onpointercancel=()=>{on=false};
    q('#kxs',st).onclick=()=>say2(x.s||x.c);q('#kxcl',st).onclick=()=>{ctx.clearRect(0,0,cv.width,cv.height)};
    q('#kxg',st).onclick=()=>{const g=q('.gh',st);g.style.color=g.style.color==='rgb(176, 168, 205)'?'':'#b0a8cd'};
    say2(x.s||x.c);cta('Trace o caractere',false);P.fx.cta=()=>!P.fx.done};
  draw();say('Trace cada caractere do jeito que quiser; o importante é treinar o desenho.')};

/* 3 · ouvir e escolher o caractere */
FXR.klisten=function(f,st,n){
  const pool=f.pool||f.chars,R=shuf(pool).slice(0,Math.min(f.rounds||8,pool.length));let ri=0,hits=0;lock();
  const draw=()=>{const x=R[ri],opts=shuf([x].concat(shuf(pool.filter(y=>y.c!==x.c)).slice(0,3)));
    st.innerHTML=`<div class="step fx nbx kx" ${theme(f)}>${head(f,n,'Ouça e escolha')}<div class="nb-prog">${R.map((_,i)=>`<i class="${i<ri?'on':''}"></i>`).join('')}</div>
    <div class="nb-hint" style="text-align:center">Ouça e toque no caractere certo</div><div class="kx-q"><button class="nb-chip" id="kxs" style="font-size:22px">🔊</button></div>
    <div class="kx-opts">${opts.map(o=>`<button class="kx-opt" data-c="${H(o.c)}">${H(o.c)}</button>`).join('')}</div></div>`;
    q('#kxs',st).onclick=()=>say2(x.s||x.c);setTimeout(()=>say2(x.s||x.c),300);let lk=false;
    st.querySelectorAll('.kx-opt').forEach(b=>b.onclick=()=>{if(lk)return;if(b.dataset.c===x.c){lk=true;b.classList.add('ok');sfx('burst');hits++;setTimeout(()=>{ri++;if(ri<R.length)draw();else win()},650)}else{b.classList.add('no');sfx('oops')}})};
  draw();cta('Escolha o caractere',false);say('Ouça o som e ache o caractere.')};

/* 4 · ligar kana e romaji */
FXR.kmatch=function(f,st,n){
  const pool=f.pool||f.chars,S=shuf(pool).slice(0,Math.min(f.pairs||6,pool.length));let a=null,done=0;lock();
  const Rr=shuf(S);
  st.innerHTML=`<div class="step fx nbx kx" ${theme(f)}>${head(f,n,'Kana e romaji')}<div class="nb-hint" style="text-align:center">Toque no caractere e depois na leitura correspondente.</div>
  <div class="kx-pair"><div class="kx-col" id="kxa">${S.map((x,i)=>`<button class="kx-pb" data-c="${H(x.c)}">${H(x.c)}</button>`).join('')}</div>
  <div class="kx-col" id="kxb">${Rr.map(x=>`<button class="kx-pb r" data-c="${H(x.c)}">${H(x.r)}</button>`).join('')}</div></div></div>`;
  const A=[...st.querySelectorAll('#kxa .kx-pb')],B=[...st.querySelectorAll('#kxb .kx-pb')];
  A.forEach(b=>b.onclick=()=>{A.forEach(x=>x.classList.remove('sel'));b.classList.add('sel');a=b;const c=S.find(y=>y.c===b.dataset.c);say2(c.s||c.c)});
  B.forEach(b=>b.onclick=()=>{if(!a)return;if(a.dataset.c===b.dataset.c){a.classList.remove('sel');a.classList.add('fd');b.classList.add('fd');a=null;sfx('burst');done++;if(done>=S.length)setTimeout(()=>win(),700)}else{b.classList.add('no');sfx('oops');setTimeout(()=>b.classList.remove('no'),500)}});
  cta('Ligue os pares',false);say('Ligue cada caractere à sua leitura.')};

/* 5 · ler palavras */
FXR.kwords=function(f,st,n){
  const R=f.items;let ri=0;lock();
  const draw=()=>{const it=R[ri];
    st.innerHTML=`<div class="step fx nbx kx" ${theme(f)}>${head(f,n,'Ler palavras')}<div class="nb-prog">${R.map((_,i)=>`<i class="${i<ri?'on':''}"></i>`).join('')}</div>
    <div class="nb-hint" style="text-align:center">Leia a palavra e escolha o significado</div><div class="kx-w">${H(it.w)}</div>
    <div class="nb-tools" style="justify-content:center"><button class="nb-chip" id="kxs">🔊 Ouvir</button><button class="nb-chip" id="kxr">あ/a Ver leitura</button></div><div class="nb-hint" id="kxro" style="text-align:center;min-height:20px"></div>
    <div class="kx-opts">${it.opts.map((o,i)=>`<button class="kx-opt sm" data-i="${i}">${o[0]} ${H(o[1])}</button>`).join('')}</div></div>`;
    q('#kxs',st).onclick=()=>say2(it.w);q('#kxr',st).onclick=()=>{q('#kxro',st).textContent=it.r||''};let lk=false;
    st.querySelectorAll('.kx-opt').forEach(b=>b.onclick=()=>{if(lk)return;if(+b.dataset.i===it.a){lk=true;b.classList.add('ok');sfx('burst');say2(it.w);setTimeout(()=>{ri++;if(ri<R.length)draw();else win()},900)}else{b.classList.add('no');sfx('oops')}})};
  draw();cta('Escolha o significado',false);say('Leia cada palavra: você já conhece todos os caracteres.')};
})();
