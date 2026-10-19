/* Pogglot · Escreva: treino de escrita à mão nos episódios (japonês). Traçar com modelo, depois de memória, com nota automática
   (cobertura do modelo × precisão do traço). Guarda as estrelas por caractere em localStorage (pogglot:kw). */
(function(){
if(typeof FXR==='undefined'||typeof FX_KIND==='undefined')return;
FX_KIND.nbwrite='practice';FX_LABEL.nbwrite='Escreva';
const q=(s,r)=>(r||document).querySelector(s);
const H=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const FONT='"Noto Sans JP","Hiragino Sans","Yu Gothic",IPAGothic,"Meiryo",system-ui,sans-serif';
const CW=520,CH=260;
const say2=(t,slow)=>{try{fxSay(String(t),null,slow)}catch(e){}};
const store=(k,v)=>{try{if(v===undefined)return JSON.parse(localStorage.getItem('pogglot:'+k)||'null');localStorage.setItem('pogglot:'+k,JSON.stringify(v))}catch(e){return null}};
const css=document.createElement('style');css.textContent=`
.kw{--g1:#6C5CE7;--g2:#A29BFE;padding-bottom:12px}
.kw-st{display:flex;gap:6px;justify-content:center;margin:6px 0}.kw-st i{width:34px;height:8px;border-radius:6px;background:#e4e0f5}.kw-st i.on{background:linear-gradient(90deg,var(--g1),var(--g2))}
.kw-info{text-align:center;margin:4px 0}.kw-info b{display:block;font:900 20px system-ui;color:#25203f}.kw-info small{display:block;font:600 14px system-ui;color:#5b5578}
.kw-mode{display:table;margin:0 auto 8px;border-radius:999px;padding:4px 12px;font:800 12px system-ui;background:#EFEAFF;color:#5a46c8;margin-bottom:6px}
.kw-cv{position:relative;width:100%;max-width:420px;aspect-ratio:2/1;margin:8px auto;border-radius:22px;background:#fff;box-shadow:0 10px 26px rgba(40,30,90,.14);touch-action:none;overflow:hidden}
.kw-cv canvas{position:absolute;inset:0;width:100%;height:100%;touch-action:none}
.kw-cv .gd{position:absolute;inset:0;pointer-events:none;background:linear-gradient(#0000 49.4%,#ece8f7 49.4% 50.6%,#0000 50.6%)}
.kw-fb{min-height:44px;text-align:center;font:800 15px/1.35 system-ui;color:#25203f;margin:6px 0}
.kw-fb.ok{color:#1f9d5c}.kw-fb.no{color:#d9480f}
.kw-stars{font-size:26px;letter-spacing:4px}
`;document.head.appendChild(css);
const stars=(r)=>{const m=Math.min(r.cov,r.pre,r.tight+.15);return m>=.8?3:m>=.65?2:m>=.5?1:0};
function fsFor(n){return Math.min(160,Math.floor(CW*0.9/Math.max(1,n)))}
function paintText(x,text,color,alpha,extra){const n=[...text].length,fs=fsFor(n);x.save();x.globalAlpha=alpha;x.font='500 '+fs+'px '+FONT;x.textAlign='center';x.textBaseline='middle';x.fillStyle=color;x.fillText(text,CW/2,CH/2+fs*.05);if(extra){x.lineWidth=extra;x.lineJoin='round';x.strokeStyle=color;x.strokeText(text,CW/2,CH/2+fs*.05)}x.restore()}
function score(strokes,text){
  const S=.5,w=CW*S,h=CH*S;
  const mk=fn=>{const c=document.createElement('canvas');c.width=w;c.height=h;const x=c.getContext('2d');x.scale(S,S);fn(x);return x.getImageData(0,0,w,h).data};
  const inkFn=lw=>x=>{x.lineWidth=lw;x.lineCap='round';x.lineJoin='round';x.strokeStyle='#000';strokes.forEach(s=>{x.beginPath();s.forEach((p,i)=>i?x.lineTo(p[0],p[1]):x.moveTo(p[0],p[1]));if(s.length===1)x.lineTo(s[0][0]+.1,s[0][1]+.1);x.stroke()})};
  const glyph=mk(x=>paintText(x,text,'#000',1)),glyphTight=mk(x=>paintText(x,text,'#000',1,16)),glyphTol=mk(x=>paintText(x,text,'#000',1,34)),inkThin=mk(inkFn(12)),inkTol=mk(inkFn(34));
  let g=0,gh=0,i=0,ih=0,it=0;
  for(let p=3;p<glyph.length;p+=4){if(glyph[p]>40){g++;if(inkTol[p]>40)gh++}if(inkThin[p]>40){i++;if(glyphTol[p]>40)ih++;if(glyphTight[p]>40)it++}}
  return{cov:g?gh/g:0,pre:i?ih/i:0,tight:i?it/i:0,ink:i/Math.max(1,g)}}
window.PogWrite={score,paintText,CW,CH};
FXR.nbwrite=function(f,st,n){
  const items=f.items||[];let wi=0,phase=0,tries=0;const total=items.length*2;let ok=0;
  P.fx.done=false;P.fx.cta=()=>!P.fx.done;
  const render=()=>{
    const it=items[wi],mode=phase===0?'trace':'recall',step=wi*2+phase,text=it.w.replace(/\s+/g,'');
    st.innerHTML=`<div class="step fx nbx kw" style="--g1:${(f.g||['#6C5CE7','#A29BFE'])[0]};--g2:${(f.g||['#6C5CE7','#A29BFE'])[1]}">${fxKindBar(f,n)}<h2 class="fx-h">${H(f.title||'Escreva')}</h2>
    <div class="kw-st">${Array.from({length:total},(_,i)=>`<i class="${i<step?'on':''}"></i>`).join('')}</div>
    <div class="kw-info"><span class="kw-mode">${mode==='trace'?'1 · Trace sobre o modelo':'2 · Escreva de memória'}</span><b>${H(it.m||'')}</b><small>${H(it.r||'')}</small></div>
    <div class="kw-cv" id="kwcv"><canvas id="kwm" width="${CW}" height="${CH}"></canvas><div class="gd"></div><canvas id="kwi" width="${CW}" height="${CH}"></canvas></div>
    <div class="kw-fb" id="kwfb">${mode==='trace'?'Cubra as letras com o dedo, da esquerda para a direita e de cima para baixo.':'Agora sem modelo: escreva a palavra. Toque em 👁️ Dica se precisar.'}</div>
    <div class="nb-tools" style="justify-content:center"><button class="nb-chip" id="kws">🔊 Ouvir</button><button class="nb-chip" id="kwc">↩︎ Apagar</button><button class="nb-chip" id="kwh">👁️ ${mode==='trace'?'Modelo':'Dica'}</button></div></div>`;
    const cm=q('#kwm',st),cx=cm.getContext('2d'),ci=q('#kwi',st),ix=ci.getContext('2d');
    const draw=(alpha,color)=>{cx.clearRect(0,0,CW,CH);if(alpha>0)paintText(cx,text,color||'#bdb5e0',alpha)};
    draw(mode==='trace'?1:0);
    ix.lineWidth=20;ix.lineCap='round';ix.lineJoin='round';ix.strokeStyle=(f.g||['#6C5CE7'])[0];
    let strokes=[],cur=null,on=false,checked=false,hint=false;
    const pos=e=>{const r=ci.getBoundingClientRect();return[(e.clientX-r.left)*CW/r.width,(e.clientY-r.top)*CH/r.height]};
    ci.onpointerdown=e=>{if(checked)return;on=true;const p=pos(e);cur=[p];strokes.push(cur);ci.setPointerCapture&&ci.setPointerCapture(e.pointerId);ix.beginPath();ix.moveTo(p[0],p[1]);ix.lineTo(p[0]+.1,p[1]+.1);ix.stroke();cta('Verificar',true,true)};
    ci.onpointermove=e=>{if(!on)return;const p=pos(e),l=cur[cur.length-1];ix.beginPath();ix.moveTo(l[0],l[1]);ix.lineTo(p[0],p[1]);ix.stroke();cur.push(p)};
    ci.onpointerup=ci.onpointercancel=()=>{on=false};
    q('#kws',st).onclick=()=>say2(it.s||it.w);
    q('#kwc',st).onclick=()=>{if(checked)return;ix.clearRect(0,0,CW,CH);strokes=[];cta('Escreva',false);P.fx.cta=()=>!P.fx.done&&verify()};
    q('#kwh',st).onclick=()=>{hint=!hint;draw(mode==='trace'?(hint?1:.45):(hint?.3:0))};
    const next=()=>{if(phase===0){phase=1;tries=0;render()}else{wi++;phase=0;tries=0;if(wi<items.length)render();else finish()}};
    const verify=()=>{
      if(checked){next();return true}
      if(!strokes.length)return true;
      const r=score(strokes,text),s=stars(r),fb=q('#kwfb',st);
      const pass=mode==='trace'?s>=1:true;
      if(!pass&&tries<1){tries++;fb.className='kw-fb no';fb.textContent=r.cov<.4?'Quase! Faltou cobrir parte do modelo. Apague e tente de novo.':'Seus traços saíram do modelo. Apague e tente de novo, com calma.';cta('Verificar',true,true);return true}
      checked=true;if(mode==='recall'){const km=store('kw')||{};[...text].forEach(c=>{km[c]=Math.max(km[c]||0,s)});store('kw',km);draw(.8,'#2cc673')}
      ok+=s>0?1:0;try{sfx(s>0?'burst':'oops')}catch(e){}
      fb.className='kw-fb '+(s>=2?'ok':'no');
      fb.innerHTML=`<div class="kw-stars">${'★'.repeat(s)}${'☆'.repeat(3-s)}</div>`+(s>=3?'Perfeito!':s===2?'Muito bom!':s===1?'Bom começo. Pratique mais.':'Vamos praticar: o modelo ficou visível para comparar.');
      if(mode==='recall'&&s===0)draw(.8,'#2cc673');
      cta(phase===0?'Agora de memória ▶':(wi<items.length-1?'Próxima palavra ▶':'Concluir'),true,true);P.fx.cta=()=>{next();return true};return true};
    const finish=()=>{P.fx.done=true;P.score++;try{sfx('tada');confetti(60)}catch(e){}st.innerHTML=`<div class="step fx nbx kw" style="--g1:${(f.g||['#6C5CE7'])[0]}">${fxKindBar(f,n)}<h2 class="fx-h">${H(f.title||'Escreva')}</h2><div class="kw-info"><b>Palavras escritas!</b><small>${items.map(i=>H(i.w)).join(' · ')}</small></div><div class="kw-fb ok">Você escreveu ${items.length} palavras à mão. Quanto mais treinar, mais firme fica o traço.</div></div>`;cta('Continuar',true,true);P.fx.cta=null};
    cta('Escreva',false);P.fx.cta=()=>!P.fx.done&&verify();
    say(mode==='trace'?'Trace sobre o modelo para treinar o desenho.':'Agora escreva de memória.');
  };
  render()};
})();

/* Mapa de escrita (hiragana e katakana) na página dos cursos de japonês */
(function(){
const HIRA='あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん';
const toKata=s=>[...s].map(c=>String.fromCharCode(c.charCodeAt(0)+96)).join('');
const KATA=toKata(HIRA);
const css=document.createElement('style');css.textContent=`
.kw-map{margin:14px 0;padding:16px;border-radius:24px;background:#fff;border:1px solid #ECE7FF;box-shadow:0 14px 30px -22px rgba(60,40,160,.6)}
.kw-map h3{margin:0 0 2px;font:900 17px system-ui;color:#25203f}.kw-map p{margin:0 0 10px;font:600 13px system-ui;color:#6b6591}
.kw-tabs{display:flex;gap:6px;margin-bottom:10px}.kw-tabs button{border:0;border-radius:999px;padding:8px 14px;min-height:40px;font:800 13px system-ui;background:#F1EDFF;color:#5a46c8}.kw-tabs button.on{background:#6C5CE7;color:#fff}
.kw-g{display:grid;grid-template-columns:repeat(5,1fr);gap:6px}
.kw-g span{aspect-ratio:1.35;display:grid;place-items:center;border-radius:12px;background:#F4F2FA;color:#b9b3d3;font:700 22px "Noto Sans JP","Hiragino Sans","Yu Gothic",IPAGothic,system-ui,sans-serif}
.kw-g span.s1{background:#FFF1C9;color:#9a6b00}.kw-g span.s2{background:#DDF6E8;color:#1b7a4b}.kw-g span.s3{background:#2CC673;color:#fff}
.kw-leg{display:flex;gap:10px;flex-wrap:wrap;margin-top:10px;font:700 12px system-ui;color:#6b6591}.kw-leg i{display:inline-block;width:12px;height:12px;border-radius:4px;vertical-align:-2px;margin-right:4px}
html[data-theme="dark"] .kw-map{background:#1B1740;border-color:#2D2760}html[data-theme="dark"] .kw-map h3{color:#EDEAFF}html[data-theme="dark"] .kw-g span{background:#2A2360;color:#6f679f}
`;document.head.appendChild(css);
function card(){
  const km=(function(){try{return JSON.parse(localStorage.getItem('pogglot:kw')||'null')||{}}catch(e){return {}}})();
  const sec=document.createElement('section');sec.className='kw-map';sec.setAttribute('aria-label','Mapa de escrita');
  const paint=set=>{const L=set==='k'?KATA:HIRA,n3=[...L].filter(c=>km[c]>=3).length;
    sec.innerHTML=`<h3>✍️ Mapa de escrita</h3><p>${n3}/46 caracteres dominados (★★★). Escreva nos episódios para colorir o mapa.</p>
    <div class="kw-tabs"><button data-s="h" class="${set==='h'?'on':''}">Hiragana</button><button data-s="k" class="${set==='k'?'on':''}">Katakana</button></div>
    <div class="kw-g">${[...L].map(c=>`<span class="${km[c]?'s'+km[c]:''}">${c}</span>`).join('')}</div>
    <div class="kw-leg"><span><i style="background:#F4F2FA"></i>novo</span><span><i style="background:#FFF1C9"></i>★</span><span><i style="background:#DDF6E8"></i>★★</span><span><i style="background:#2CC673"></i>★★★</span></div>`;
    sec.querySelectorAll('.kw-tabs button').forEach(b=>b.onclick=()=>paint(b.dataset.s))};
  paint('h');return sec}
function mount(cid){
  if(!/^nbja/.test(cid||'')||document.querySelector('.kw-map'))return;
  const host=document.querySelector('.exam-card')||document.querySelector('.p2tools')||document.querySelector('main.wrap .road');if(!host)return;
  host.parentNode.insertBefore(card(),host.nextSibling&&host.matches('.exam-card')?host.nextSibling:host)}
const c0=window.course;
if(typeof c0==='function')window.course=function(id){const r=c0.apply(this,arguments);try{mount(id)}catch(e){console.error('kw-map',e)}return r};
})();
