/* Pogglot · Kanji do dia (japonês): significado, leituras on/kun, palavras de exemplo, mini-quiz e escrita com ordem dos traços.
   Dados: data/kanji.json (conteúdo Pogglot) e data/kanji-strokes.json (KanjiVG, CC BY-SA 3.0, https://kanjivg.tagaini.net). */
(function(){
if(typeof FXR==='undefined'||typeof FX_KIND==='undefined')return;
FX_KIND.nbkanji='vocab';FX_LABEL.nbkanji='Kanji do dia';
const q=(s,r)=>(r||document).querySelector(s);
const H=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const say2=(t,slow)=>{try{fxSay(String(t),null,slow)}catch(e){}};
const FONT='"Noto Sans JP","Hiragino Sans","Yu Gothic",IPAGothic,system-ui,sans-serif';
const css=document.createElement('style');css.textContent=`
.kj{--g1:#E17055;--g2:#FDCB6E;padding-bottom:12px}
.kj-big{text-align:center;background:linear-gradient(135deg,#FFF3E8,#FFE8D6);border-radius:26px;padding:16px;margin:8px 0;box-shadow:0 10px 26px -18px rgba(180,80,20,.6)}
.kj-big .ch{font:900 120px/1.05 ${FONT};color:#d6492a}.kj-big .mn{font:900 20px system-ui;color:#23383C;margin-top:2px}
.kj-rd{display:grid;gap:6px;margin:10px 0}.kj-rd div{display:flex;gap:8px;align-items:baseline;flex-wrap:wrap;background:#fff;border:1px solid #F3E3D6;border-radius:14px;padding:8px 12px;font:700 15px system-ui;color:#23383C}
.kj-rd small{font:800 11px system-ui;color:#b4582f;text-transform:uppercase;letter-spacing:.04em;min-width:76px}.kj-rd span{font:800 17px ${FONT}}.kj-rd em{font:600 13px system-ui;color:#768B93;font-style:normal}
.kj-w{display:grid;gap:6px;margin:8px 0}.kj-w button{display:flex;align-items:center;gap:10px;border:0;border-radius:14px;background:#fff;box-shadow:0 4px 12px rgba(37,77,83,.1);padding:10px 12px;text-align:left;font:700 14px system-ui;color:#23383C;min-height:48px}
.kj-w b{font:900 22px ${FONT};min-width:62px}.kj-w i{font-style:normal;color:#768B93;font-weight:600}
.kj-opts{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;margin:12px 0}.kj-opts button{border:0;border-radius:18px;background:#fff;box-shadow:0 6px 16px rgba(37,77,83,.12);padding:14px 8px;min-height:56px;font:800 16px/1.2 ${FONT};color:#23383C}
.kj-opts button.ok{background:#d9f8e5;outline:3px solid #2cc673}.kj-opts button.no{background:#ffe0e0;outline:3px solid #ff6b6b}
.kj-q{text-align:center;font:800 17px system-ui;color:#23383C;margin:10px 0}.kj-q b{font:900 54px ${FONT};display:block;color:#d6492a}
html[data-theme="dark"] .kj-big{background:#212F31}html[data-theme="dark"] .kj-rd div,html[data-theme="dark"] .kj-w button,html[data-theme="dark"] .kj-opts button{background:#1C373B;color:#EDFCFB;border-color:#2D545A}
`;document.head.appendChild(css);
let KD=null,KDP=null;const loadKD=()=>KDP||(KDP=fetch('data/kanji.json?v=1').then(r=>r.json()).then(j=>{KD=j;return j}).catch(()=>({})));
window.PogKanji={load:loadKD};
const shuf=a=>a.slice().sort(()=>Math.random()-.5);
FXR.nbkanji=function(f,st,n){
  const ch=f.c;P.fx.done=false;P.fx.cta=()=>!P.fx.done;
  const theme=`style="--g1:${(f.g||['#E17055','#FDCB6E'])[0]};--g2:${(f.g||['#E17055','#FDCB6E'])[1]}"`;
  const intro=d=>{
    const ex=d.w[0];
    st.innerHTML=`<div class="step fx nbx kj" ${theme}>${fxKindBar(f,n)}<h2 class="fx-h">Kanji do dia</h2>
    <div class="kj-big"><div class="ch">${H(ch)}</div><div class="mn">${H(d.m)}</div></div>
    <div class="kj-rd" data-norj="1"><div><small>Leitura on</small>${d.on.length?d.on.map(r=>`<span>${H(r[0])}</span><em>${H(r[1])}</em>`).join(' '):'<em>—</em>'}</div>
    <div><small>Leitura kun</small>${d.kun.length?d.kun.map(r=>`<span>${H(r[0])}</span><em>${H(r[1])}</em>`).join(' '):'<em>—</em>'}</div></div>
    <div class="nb-hint" style="text-align:center">Toque nas palavras para ouvir</div>
    <div class="kj-w">${d.w.map((w,i)=>`<button data-i="${i}"><b>${H(w[0])}</b><span>${H(w[1])}</span><i>${H(w[2])}</i> 🔊</button>`).join('')}</div></div>`;
    st.querySelectorAll('.kj-w button').forEach(b=>b.onclick=()=>say2(d.w[+b.dataset.i][1]));
    say2(ex[1]);cta('Testar o que aprendi ▶',true,true);P.fx.cta=()=>{quiz(d);return true};
    say('Este é o kanji do dia. Veja os significados e as leituras.')};
  const quiz=d=>{
    const all=Object.keys(KD),others=shuf(all.filter(c=>c!==ch)).slice(0,3);
    const qs=[{q:`O que significa <b>${H(ch)}</b>?`,opts:shuf([d.m].concat(others.map(c=>KD[c].m))),a:d.m},
      {q:`Como se lê <b>${H(d.w[0][0])}</b>?`,opts:shuf([d.w[0][1]].concat(shuf(all.filter(c=>c!==ch&&KD[c].w[0][1]!==d.w[0][1])).slice(0,3).map(c=>KD[c].w[0][1]))),a:d.w[0][1]}];
    let qi=0;
    const draw=()=>{const Q=qs[qi];
      st.innerHTML=`<div class="step fx nbx kj" ${theme}>${fxKindBar(f,n)}<h2 class="fx-h">Kanji do dia</h2><div class="kj-q">${Q.q}</div>
      <div class="kj-opts">${Q.opts.map(o=>`<button data-o="${H(o)}">${H(o)}</button>`).join('')}</div></div>`;
      let lk=false;st.querySelectorAll('.kj-opts button').forEach(b=>b.onclick=()=>{if(lk)return;if(b.dataset.o===Q.a){lk=true;b.classList.add('ok');try{sfx('burst')}catch(e){}setTimeout(()=>{qi++;if(qi<qs.length)draw();else write(d)},650)}else{b.classList.add('no');try{sfx('oops')}catch(e){}}});
      cta('Escolha a resposta',false);P.fx.cta=()=>!P.fx.done};
    draw()};
  const write=d=>{
    const g=f.g||['#E17055','#FDCB6E'];
    FXR.nbwrite({k:'nbwrite',g,title:'Escreva o kanji',items:[{w:ch,m:d.m,r:'on: '+d.on.map(r=>r[1]).join(', ')+(d.kun.length?' · kun: '+d.kun.map(r=>r[1]).join(', '):''),s:d.w[0][1]}]},st,n)};
  Promise.all([loadKD(),(window.PogWrite&&PogWrite.loadKS?PogWrite.loadKS():Promise.resolve())]).then(()=>{if(!KD||!KD[ch]){P.fx.done=true;cta('Continuar',true,true);return}intro(KD[ch])})};
})();
