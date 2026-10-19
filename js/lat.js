/* Pogglot · Episódio de regras: "rdg" (leitura curta com regra + pergunta) e "wlat" (escrever na tela, alfabeto latino).
   wlat: traçar sobre o modelo (nota automática) e escrever de memória (autoavaliação). Reaproveita o desenho do write.js. */
(function(){
if(typeof FXR==='undefined'||typeof FX_KIND==='undefined')return;
FX_KIND.rdg='story';FX_LABEL.rdg='Leitura';FX_KIND.wlat='practice';FX_LABEL.wlat='Escreva na tela';
const q=(s,r)=>(r||document).querySelector(s);
const H=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const say2=(t,slow)=>{try{fxSay(String(t),null,slow)}catch(e){}};
const css=document.createElement('style');css.textContent=`
.rdg{padding-bottom:12px}
.rdg-text{display:grid;gap:6px;margin:8px 0}
.rdg-s{display:block;width:100%;text-align:left;border:0;border-radius:16px;padding:10px 14px;background:#fff;box-shadow:0 6px 18px -12px rgba(40,30,90,.5);font:600 17px/1.35 system-ui;color:#25203f;min-height:44px;cursor:pointer}
.rdg-s mark{background:linear-gradient(transparent 55%,#ffe08a 55%);color:inherit;border-radius:3px;padding:0 1px;font-weight:800}
.rdg-s small{display:none;margin-top:4px;font:500 14px system-ui;color:#6b6591}.rdg-s.open small{display:block}
.rdg-rule{display:flex;gap:10px;align-items:flex-start;margin:10px 0;padding:12px 14px;border-radius:16px;background:linear-gradient(135deg,#eaf7f6,#fff);border:2px solid #bfe6e3;color:#0b5f5d;font:600 15px/1.35 system-ui}
.rdg-rule b{font-weight:900}
.rdg-q{font:800 19px/1.3 system-ui;color:#25203f;margin:10px 0}
.rdg-o{display:grid;gap:8px}.rdg-o button{border:2px solid #e6e1f7;background:#fff;border-radius:16px;padding:12px 14px;min-height:48px;font:700 17px system-ui;color:#25203f;text-align:left;cursor:pointer}
.rdg-o button.ok{border-color:#2cc673;background:#e7f9ef}.rdg-o button.no{border-color:#ef6a4c;background:#fff0ec}
.wl{--g1:#0C7A78;--g2:#3fc1bd;padding-bottom:12px}
.wl-st{display:flex;gap:6px;justify-content:center;margin:6px 0}.wl-st i{width:26px;height:8px;border-radius:6px;background:#dcefee}.wl-st i.on{background:linear-gradient(90deg,var(--g1),var(--g2))}
.wl-info{text-align:center;margin:4px 0}.wl-info b{display:block;font:900 20px system-ui;color:#25203f}.wl-info small{display:block;font:600 14px system-ui;color:#5b5578}
.wl-mode{display:table;margin:0 auto 8px;border-radius:999px;padding:4px 12px;font:800 12px system-ui;background:#e3f4f3;color:#0b5f5d}
.wl-cv{position:relative;width:100%;max-width:420px;aspect-ratio:2/1;margin:8px auto;border-radius:22px;background:#fff;box-shadow:0 10px 26px rgba(20,60,60,.14);touch-action:none;overflow:hidden}
.wl-cv canvas{position:absolute;inset:0;width:100%;height:100%;touch-action:none}
.wl-cv .gd{position:absolute;inset:0;pointer-events:none;background:linear-gradient(#0000 61%,#d9ecea 61% 62.2%,#0000 62.2%)}
.wl-fb{min-height:40px;text-align:center;font:800 15px/1.35 system-ui;color:#25203f;margin:6px 0}.wl-fb.ok{color:#1f9d5c}.wl-fb.no{color:#d9480f}
.wl-stars{font-size:26px;letter-spacing:4px}
@media(prefers-color-scheme:dark){.rdg-s,.rdg-o button,.wl-cv{background:#1b2230;color:#eef;}.rdg-q,.wl-info b,.wl-fb{color:#eef}.rdg-rule{background:#10292a;color:#9fe3df;border-color:#1d5d5a}}
`;document.head.appendChild(css);
const CW=520,CH=260;
const FONT='700 %spx "Nunito","Segoe UI",system-ui,sans-serif';
const fsFor=t=>Math.min(150,Math.floor(CW*.92/Math.max(2,[...t].length*.58)));
function paintW(x,text,color,alpha,extra){const fs=fsFor(text);x.save();x.globalAlpha=alpha;x.font=FONT.replace('%s',fs);x.textAlign='center';x.textBaseline='alphabetic';x.fillStyle=color;const y=CH*.62+fs*.3;x.fillText(text,CW/2,y);if(extra){x.lineWidth=extra;x.lineJoin='round';x.strokeStyle=color;x.strokeText(text,CW/2,y)}x.restore()}
function score(strokes,text){
  const S=.5,w=CW*S,h=CH*S;
  const mk=fn=>{const c=document.createElement('canvas');c.width=w;c.height=h;const x=c.getContext('2d');x.scale(S,S);fn(x);return x.getImageData(0,0,w,h).data};
  const inkFn=lw=>x=>{x.lineWidth=lw;x.lineCap='round';x.lineJoin='round';x.strokeStyle='#000';strokes.forEach(s=>{x.beginPath();s.forEach((p,i)=>i?x.lineTo(p[0],p[1]):x.moveTo(p[0],p[1]));if(s.length===1)x.lineTo(s[0][0]+.1,s[0][1]+.1);x.stroke()})};
  const glyph=mk(x=>paintW(x,text,'#000',1)),tight=mk(x=>paintW(x,text,'#000',1,14)),tol=mk(x=>paintW(x,text,'#000',1,34)),inkThin=mk(inkFn(12)),inkTol=mk(inkFn(34));
  let g=0,gh=0,i=0,ih=0,it=0;
  for(let p=3;p<glyph.length;p+=4){if(glyph[p]>40){g++;if(inkTol[p]>40)gh++}if(inkThin[p]>40){i++;if(tol[p]>40)ih++;if(tight[p]>40)it++}}
  const r={cov:g?gh/g:0,pre:i?ih/i:0,tight:i?it/i:0};const m=Math.min(r.cov,r.pre,r.tight+.15);r.s=m>=.8?3:m>=.65?2:m>=.5?1:0;return r}
/* ---------- leitura ---------- */
FXR.rdg=function(f,st,n){
  const lines=f.s||[];let phase=0;
  const mkL=s=>H(s).replace(/\{\{(.+?)\}\}/g,'<mark>$1</mark>');
  const plainL=s=>String(s).replace(/\{\{|\}\}/g,'');
  const view=()=>{
    if(phase===0){
      st.innerHTML=`<div class="step fx rdg">${fxKindBar(f,n)}<h2 class="fx-h">${H(f.title||'Leitura')}</h2>
      <div class="rdg-text">${lines.map((l,i)=>`<button type="button" class="rdg-s" data-i="${i}">${mkL(l[0])}<small>${H(l[1])}</small></button>`).join('')}</div>
      ${f.rule?`<div class="rdg-rule"><span>📌</span><span>${mk(f.rule)}</span></div>`:''}</div>`;
      st.querySelectorAll('.rdg-s').forEach(b=>b.onclick=()=>{b.classList.toggle('open');say2(plainL(lines[+b.dataset.i][0]))});
      P.fx.cta=()=>{if(f.q){phase=1;view();return true}return false};cta(f.q?'Entendi — uma pergunta ▶':P.t.cont,true,true);say(f.say||'Toque nas frases para ouvir e ver a tradução.');
    }else{
      const Q=f.q;
      st.innerHTML=`<div class="step fx rdg">${fxKindBar(f,n)}<h2 class="fx-h">${H(f.title||'Leitura')}</h2><div class="rdg-q">${H(Q.q)}</div>
      <div class="rdg-o">${Q.o.map((o,i)=>`<button type="button" data-i="${i}">${H(o)}</button>`).join('')}</div><div id="fb"></div></div>`;
      let done=false;P.fx.cta=null;cta('Escolha uma resposta',false);
      st.querySelectorAll('.rdg-o button').forEach(b=>b.onclick=()=>{if(done)return;done=true;const i=+b.dataset.i,ok=i===Q.a;
        b.classList.add(ok?'ok':'no');if(!ok)st.querySelectorAll('.rdg-o button')[Q.a].classList.add('ok');if(ok)P.score++;
        fxGrade(ok,Q.why||'',Q.o[Q.a]);P.answered=true;cta(P.t.cont,true,true)});
    }};
  view()};
/* ---------- escrever na tela ---------- */
FXR.wlat=function(f,st,n){
  const items=f.items||[];let wi=0,phase=0,tries=0;const total=items.length*2;
  P.fx.done=false;P.fx.cta=()=>!P.fx.done;
  const render=()=>{
    const it=items[wi],text=it.w,mode=phase===0?'trace':'recall',step=wi*2+phase;
    st.innerHTML=`<div class="step fx wl">${fxKindBar(f,n)}<h2 class="fx-h">${H(f.title||'Escreva na tela')}</h2>
    <div class="wl-st">${Array.from({length:total},(_,i)=>`<i class="${i<step?'on':''}"></i>`).join('')}</div>
    <div class="wl-info"><span class="wl-mode">${mode==='trace'?'1 · Trace sobre o modelo':'2 · Escreva de memória'}</span><b>${H(it.m||'')}</b></div>
    <div class="wl-cv"><canvas id="wlm" width="${CW}" height="${CH}"></canvas><div class="gd"></div><canvas id="wli" width="${CW}" height="${CH}"></canvas></div>
    <div class="wl-fb" id="wlfb">${mode==='trace'?'Passe o dedo por cima das letras, sem pressa.':'Agora sem modelo: escreva a palavra. Depois você confere.'}</div>
    <div class="nb-tools" style="justify-content:center"><button class="nb-chip" id="wls">🔊 Ouvir</button><button class="nb-chip" id="wlc">↩︎ Apagar</button></div></div>`;
    const cm=q('#wlm',st).getContext('2d'),ci=q('#wli',st),ix=ci.getContext('2d');
    if(mode==='trace')paintW(cm,text,'#bfe0de',1);
    ix.lineWidth=14;ix.lineCap='round';ix.lineJoin='round';ix.strokeStyle='#0C7A78';ix.shadowColor='rgba(12,122,120,.3)';ix.shadowBlur=6;
    q('#wls',st).onclick=()=>say2(it.s||text);
    let strokes=[],cur=null,on=false,checked=false;
    const pos=e=>{const r=ci.getBoundingClientRect();return[(e.clientX-r.left)*CW/r.width,(e.clientY-r.top)*CH/r.height]};
    ci.onpointerdown=e=>{if(checked)return;on=true;const p=pos(e);cur=[p];strokes.push(cur);ci.setPointerCapture&&ci.setPointerCapture(e.pointerId);ix.beginPath();ix.moveTo(p[0],p[1]);ix.lineTo(p[0]+.1,p[1]+.1);ix.stroke();cta(mode==='trace'?'Verificar':'Conferir',true,true)};
    ci.onpointermove=e=>{if(!on)return;const p=pos(e),l=cur[cur.length-1];ix.beginPath();ix.moveTo(l[0],l[1]);ix.lineTo(p[0],p[1]);ix.stroke();cur.push(p)};
    ci.onpointerup=ci.onpointercancel=()=>{on=false};
    const fb=q('#wlfb',st);
    q('#wlc',st).onclick=()=>{if(checked)return;ix.clearRect(0,0,CW,CH);strokes=[];cta('Escreva',false);P.fx.cta=()=>!P.fx.done&&verify()};
    const nextBtn=()=>cta(phase===0?'Agora de memória ▶':(wi<items.length-1?'Próxima palavra ▶':'Concluir'),true,true);
    const next=()=>{phase++;tries=0;if(phase>1){wi++;phase=0;if(wi>=items.length)return finish()}render()};
    const verify=()=>{
      if(checked){next();return true}
      if(!strokes.length)return true;
      if(mode==='trace'){
        const r=score(strokes,text);
        if(r.s<1&&tries<1){tries++;fb.className='wl-fb no';fb.textContent=r.cov<.4?'Quase! Faltou cobrir parte da palavra. Apague e tente de novo.':'Os traços saíram do modelo. Apague e tente de novo, com calma.';cta('Verificar',true,true);return true}
        checked=true;try{sfx(r.s>0?'burst':'oops')}catch(e){}
        fb.className='wl-fb '+(r.s>=2?'ok':'no');fb.innerHTML=`<div class="wl-stars">${'★'.repeat(r.s)}${'☆'.repeat(3-r.s)}</div>`+(r.s>=3?'Perfeito!':r.s===2?'Muito bom!':r.s===1?'Bom começo.':'Vamos praticar: o modelo vem de novo.');
        nextBtn();P.fx.cta=()=>{next();return true};return true}
      checked=true;paintW(cm,text,'#2cc673',.55);
      fb.className='wl-fb';fb.innerHTML=`Confira com o modelo verde. Parecido?<div class="nb-tools" style="justify-content:center;margin-top:6px"><button class="nb-chip" id="wly">✅ Acertei</button><button class="nb-chip" id="wln">🔁 Quase</button></div>`;
      const fin=ok=>{try{sfx(ok?'burst':'oops')}catch(e){}if(ok)P.streak=(P.streak||0)+1;else P.streak=0;fb.className='wl-fb '+(ok?'ok':'no');fb.textContent=ok?'Isso! Você escreveu de memória.':'Sem problema, na próxima fica melhor.';nextBtn();P.fx.cta=()=>{next();return true}};
      q('#wly',st).onclick=()=>fin(true);q('#wln',st).onclick=()=>fin(false);cta('Escolha uma opção',false);P.fx.cta=()=>true;return true};
    cta('Escreva',false);P.fx.cta=()=>!P.fx.done&&verify();
    say(mode==='trace'?'Trace sobre o modelo.':'Agora escreva de memória.')};
  const finish=()=>{P.fx.done=true;P.score++;try{sfx('tada');confetti(60)}catch(e){}
    st.innerHTML=`<div class="step fx wl">${fxKindBar(f,n)}<h2 class="fx-h">${H(f.title||'Escreva na tela')}</h2><div class="wl-info"><b>Muito bem! ✍️</b><small>Você escreveu ${items.map(i=>H(i.w)).join(', ')}.</small></div></div>`;
    P.fx.cta=null;cta(P.t.cont,true,true);say('Escrever com a mão ajuda a memória!')};
  render()};
})();
