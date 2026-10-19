/* Pogglot · Episódio de regras: "rdg" (leitura curta com regra + pergunta) e "wlat" (escrever na tela, alfabeto latino).
   wlat: traçar sobre o modelo (nota automática) e escrever de memória (autoavaliação). Reaproveita o desenho do write.js. */
(function(){
if(typeof FXR==='undefined'||typeof FX_KIND==='undefined')return;
FX_KIND.rdg='story';FX_LABEL.rdg='Leitura';FX_KIND.cultob='story';FX_LABEL.cultob='A obra';FX_KIND.cultgame='practice';FX_LABEL.cultgame='Missão da obra';FX_KIND.culttl='practice';FX_LABEL.culttl='Linha do tempo';FX_KIND.cultx='story';FX_LABEL.cultx='Dentro da obra';FX_KIND.cultq='practice';FX_LABEL.cultq='Cultura em jogo';FX_KIND.cult='story';FX_LABEL.cult='Você sabia?';FX_KIND.rdgplay='story';FX_LABEL.rdgplay='Missão da conversa';FX_KIND.wlat='practice';FX_LABEL.wlat='Escreva na tela';
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
.cx{padding-bottom:12px}
.cx-t{display:block;width:100%;text-align:left;border:0;border-radius:18px;padding:0;margin:8px 0;background:#fff;box-shadow:0 8px 20px -14px rgba(40,30,90,.6);overflow:hidden;cursor:pointer;font:inherit}
.cx-h{display:flex;align-items:center;gap:10px;padding:11px 14px;min-height:50px;font:800 16px system-ui;color:#25203f}
.cx-h em{font-style:normal;font-size:22px}.cx-h i{margin-left:auto;font-style:normal;color:#0C7A78;font-size:20px}
.cx-b{display:none;padding:0 14px 12px;font:500 15px/1.4 system-ui;color:#3b3558}
.cx-t.on .cx-b{display:block;animation:rpIn .3s both}.cx-t.on .cx-h i{transform:rotate(45deg)}
.cx-q{font:800 17px/1.3 system-ui;color:#0b5f5d}.cx-q small{display:block;font:500 13px system-ui;color:#6b6591;margin-top:3px}
.cx-st{text-align:center;font:800 14px system-ui;color:#F29B34;margin:2px 0}
.cb-chips{display:flex;gap:6px;flex-wrap:wrap;margin:4px 0 6px}.cb-chips span{font:700 12px system-ui;color:#0b5f5d;background:#e3f4f3;border-radius:99px;padding:4px 10px}
.cb-hook{font:italic 700 16px/1.35 Georgia,serif;color:#7a5200;margin:6px 0 10px;padding-left:10px;border-left:4px solid #F29B34}
.cb-p{display:flex;gap:10px;align-items:flex-start;margin:7px 0;padding:11px 13px;border-radius:16px;background:#fff;box-shadow:0 8px 18px -14px rgba(40,30,90,.6);font:600 15px/1.4 system-ui;color:#25203f;animation:rpIn .4s both}
.cb-p b{flex:none;width:26px;height:26px;border-radius:50%;display:grid;place-items:center;background:linear-gradient(135deg,#F29B34,#E85D75);color:#fff;font:900 14px system-ui}
.cg-c{display:block;width:100%;text-align:left;margin:7px 0;padding:11px 13px;border:2px solid #e6e1f7;border-radius:16px;background:#fff;font:600 15px/1.35 system-ui;color:#25203f;cursor:pointer;min-height:48px;position:relative}
.cg-c.pick{border-color:#2cc673;background:#e7f9ef}.cg-c.no{animation:rpShake .4s;border-color:#ef6a4c}
.cg-c i{position:absolute;right:10px;top:10px;font-style:normal;font:900 14px system-ui;color:#fff;background:#2cc673;border-radius:50%;width:24px;height:24px;display:none;place-items:center}.cg-c.pick i{display:grid}
.cg-q{font:800 18px/1.35 system-ui;color:#25203f;margin:8px 0}.cg-en{font:800 20px/1.35 system-ui;color:#0b5f5d;margin:8px 0 2px}.cg-pt{font:500 14px system-ui;color:#6b6591;margin-bottom:8px}
.cg-tf{display:flex;gap:10px;margin:10px 0}.cg-tf button{flex:1;border:0;border-radius:16px;padding:14px;min-height:52px;font:900 17px system-ui;color:#fff;cursor:pointer;box-shadow:0 5px 0 rgba(0,0,0,.2)}
.cg-tf .t{background:linear-gradient(135deg,#0C7A78,#3fc1bd)}.cg-tf .f{background:linear-gradient(135deg,#E85D75,#f38aa0)}
.cg-yr{display:none;margin-left:6px;font:900 13px system-ui;color:#0b5f5d}.cg-c.rev .cg-yr{display:inline}
.vw-bar{height:8px;border-radius:6px;background:#e1f1f0;overflow:hidden;margin:6px 0 10px}.vw-bar i{display:block;height:100%;background:linear-gradient(90deg,#0C7A78,#3fc1bd);transition:width .3s}
.vw-g{display:inline-block;min-width:74px;border-bottom:3px dashed #F29B34;color:#F29B34;text-align:center}.vw-g.ok{border-bottom:3px solid #2cc673;color:#1b7a4b;background:#e7f9ef;border-radius:8px}
.vw-o{display:flex;gap:8px;flex-wrap:wrap;justify-content:center;margin:14px 0 4px}
.vw-o button{border:0;border-radius:16px;padding:12px 16px;min-height:48px;font:800 17px system-ui;color:#fff;background:linear-gradient(135deg,#6C3FEF,#9a7bff);box-shadow:0 6px 0 #4a28b3;cursor:pointer}
.vw-o button.no{background:#e9e4f5;color:#a59cc0;box-shadow:none;animation:rpShake .4s}
.vw-h{min-height:22px;text-align:center;font:700 14px/1.3 system-ui;color:#b4560a;margin-top:6px}
.cu2{padding-bottom:12px}
.cu2-art{border-radius:22px;overflow:hidden;box-shadow:0 12px 24px -14px rgba(20,40,80,.5);margin:6px 0;max-height:150px}
.cu2-art svg{display:block;width:100%;height:150px;object-fit:cover}
.cu2-work{display:flex;gap:8px;align-items:center;margin:8px 0 2px;font:900 19px/1.2 system-ui;color:#25203f}
.cu2-work small{font:700 12px system-ui;color:#0b5f5d;background:#e3f4f3;border-radius:99px;padding:3px 10px}
.cu2-fact{margin:8px 0;padding:12px 14px;border-radius:16px;background:linear-gradient(135deg,#fff7e0,#fff);border:2px solid #ffd978;color:#7a5200;font:600 15px/1.4 system-ui}
.cu2-q{font:800 18px/1.3 system-ui;color:#25203f;margin:10px 0 6px}
.rp{padding-bottom:12px}
.rp-chat{display:grid;gap:8px;margin:6px 0}
.rp-b{display:flex;gap:8px;align-items:flex-end;animation:rpIn .35s both}
.rp-b.r{flex-direction:row-reverse}
.rp-av{flex:none;width:36px;height:36px;border-radius:50%;display:grid;place-items:center;font-size:20px;box-shadow:0 4px 10px -4px rgba(0,0,0,.4)}
.rp-bb{max-width:78%;padding:9px 13px;border-radius:18px 18px 18px 4px;background:#fff;box-shadow:0 6px 16px -12px rgba(40,30,90,.6);font:600 17px/1.35 system-ui;color:#25203f}
.rp-b.r .rp-bb{border-radius:18px 18px 4px 18px;background:#e6f6f5}
.rp-bb small{display:none;margin-top:3px;font:500 13px system-ui;color:#6b6591}.rp-bb.on small{display:block}
.rp-gap{display:inline-block;min-width:64px;padding:0 8px;border-bottom:3px dashed #F29B34;color:#F29B34;text-align:center;animation:rpPulse 1.2s infinite}
.rp-gap.ok{border-bottom:3px solid #2cc673;color:#1b7a4b;background:#e7f9ef;border-radius:8px;animation:rpPop .4s}
.rp-opts{display:flex;gap:8px;flex-wrap:wrap;justify-content:center;margin:12px 0 4px}
.rp-opts button{border:0;border-radius:16px;padding:12px 18px;min-height:48px;font:800 17px system-ui;color:#fff;background:linear-gradient(135deg,#0C7A78,#3fc1bd);box-shadow:0 6px 0 #095a58;cursor:pointer}
.rp-opts button:active{transform:translateY(3px);box-shadow:0 3px 0 #095a58}
.rp-opts button.no{background:#e9e4f5;color:#a59cc0;box-shadow:none;animation:rpShake .4s}
.rp-hint{min-height:22px;text-align:center;font:700 14px/1.3 system-ui;color:#b4560a}
.rp-rule{display:flex;gap:10px;align-items:flex-start;margin:10px 0;padding:12px 14px;border-radius:16px;background:linear-gradient(135deg,#fff7e0,#fff);border:2px solid #ffd978;color:#7a5200;font:600 15px/1.35 system-ui;animation:rpIn .4s both}
.rp-res{text-align:center;font:900 22px system-ui;color:#F29B34;letter-spacing:4px;margin-top:6px}
@keyframes rpIn{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
@keyframes rpPulse{50%{opacity:.5}}
@keyframes rpPop{50%{transform:scale(1.2)}}
@keyframes rpShake{25%{transform:translateX(-5px)}75%{transform:translateX(5px)}}
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
/* ---------- "Dentro da obra": cartões que o aluno abre (história, frase, curiosidade, como entrar) ---------- */
FXR.cultx=function(f,st,n){
  const T=f.tiles,seen=new Set();P.fx.done=false;P.fx.cta=null;
  const art=f.pa?`<div class="cu2-art">${CULT_PROC(f.pa,1)}</div>`:'';
  st.innerHTML=`<div class="step fx cx">${fxKindBar(f,n)}<h2 class="fx-h">${H(f.title)}</h2>${art}
  <div class="cu2-work"><span>${H(f.work)}</span>${f.tag?`<small>${H(f.tag)}</small>`:''}</div><div class="cx-st" id="cxs">Toque nos cartões · 0/${T.length}</div>
  ${T.map((t,i)=>`<button type="button" class="cx-t" data-i="${i}"><div class="cx-h"><em>${t.ic}</em><span>${H(t.l)}</span><i>＋</i></div><div class="cx-b">${t.en?`<div class="cx-q">“${H(t.en)}”<small>${H(t.pt)}</small></div>`:mk(t.t)}</div></button>`).join('')}</div>`;
  cta('Abra os cartões',false);
  st.querySelectorAll('.cx-t').forEach(b=>b.onclick=()=>{const i=+b.dataset.i,t=T[i];b.classList.toggle('on');
    if(b.classList.contains('on')){try{sfx('pop')}catch(e){}if(t.en)say2(t.en)}
    seen.add(i);q('#cxs',st).textContent=seen.size>=T.length?'Tudo aberto! 🎉':'Toque nos cartões · '+seen.size+'/'+T.length;
    if(seen.size>=T.length)cta(P.t.cont,true,true)});
  say(f.say||'Vamos conhecer a obra por dentro? Abra cada cartão!')};
/* ---------- cultura: apresentação (cultob) · atividade (cultgame) · linha do tempo (culttl) ---------- */
FXR.cultob=function(f,st,n){
  P.fx.done=false;P.fx.cta=null;
  const art=f.pa?`<div class="cu2-art">${CULT_PROC(f.pa,1)}</div>`:'';
  st.innerHTML=`<div class="step fx cu2">${fxKindBar(f,n)}<h2 class="fx-h">${H(f.title)}</h2>${art}
  <div class="cu2-work"><span>${H(f.work)}</span></div><div class="cb-chips">${(f.chips||[]).map(c=>`<span>${H(c)}</span>`).join('')}</div>
  ${f.hook?`<div class="cb-hook">${mk(f.hook)}</div>`:''}
  ${(f.panels||[]).map((t,i)=>`<div class="cb-p" style="animation-delay:${i*120}ms"><b>${i+1}</b><span>${mk(t)}</span></div>`).join('')}</div>`;
  cta(P.t.cont,true,true);say(f.say||'Conheça a obra de hoje!')};
FXR.cultgame=function(f,st,n){
  const R=f.rounds;let ri=0,hits=0;P.fx.done=false;P.fx.cta=null;
  const head=()=>`${fxKindBar(f,n)}<h2 class="fx-h">${H(f.title)} <small>${ri+1}/${R.length}</small></h2><div class="vw-bar"><i style="width:${ri/R.length*100}%"></i></div>`;
  const next=ok=>{if(ok)hits++;P.fx.cta=()=>{ri++;draw();return true};cta(ri<R.length-1?'Próximo desafio ▶':'Ver resultado ▶',true,true)};
  const finish=()=>{P.score+=hits;P.fx.done=true;const sc=R.length?hits/R.length:1,stars=sc>=.8?3:sc>=.5?2:1;
    st.innerHTML=`<div class="step fx cu2">${fxKindBar(f,n)}<h2 class="fx-h">${H(f.title)}</h2><div class="rp-res">${'★'.repeat(stars)}${'☆'.repeat(3-stars)}</div><div class="rp-rule"><span>🎉</span><span><b>Você conhece a obra!</b><br>${H(f.work||'')} agora faz parte do seu repertório em inglês.</span></div></div>`;
    try{sfx('tada');confetti(50)}catch(e){}P.fx.cta=null;cta(P.t.cont,true,true);say('Missão da obra cumprida!')};
  const draw=()=>{
    if(ri>=R.length)return finish();const r=R[ri];let done=false;
    if(r.t==='order'){
      const items=r.items.map((t,i)=>({t,i}));let need=0,miss=0;
      st.innerHTML=`<div class="step fx cu2">${head()}<div class="cg-q">${H(r.q||'Ponha a história na ordem: toque do início ao fim.')}</div>${fxShuffle(items).map(o=>`<button type="button" class="cg-c" data-i="${o.i}">${mk(o.t)}<i></i></button>`).join('')}<div id="fb"></div></div>`;
      cta('Toque na ordem certa',false);
      st.querySelectorAll('.cg-c').forEach(b=>b.onclick=()=>{if(b.classList.contains('pick')||done)return;const i=+b.dataset.i;
        if(i===need){b.classList.add('pick');b.querySelector('i').textContent=need+1;need++;try{sfx('pop')}catch(e){}
          if(need>=items.length){done=true;P.streak=miss?0:(P.streak||0)+1;fxGrade(true,'',null);next(!miss)}}
        else{miss++;b.classList.add('no');setTimeout(()=>b.classList.remove('no'),450);P.streak=0;try{sfx('oops')}catch(e){}}});
    }else if(r.t==='gap'){
      st.innerHTML=`<div class="step fx cu2">${head()}<div class="cg-q">Complete a frase famosa:</div><div class="cg-en">“${H(r.en).replace('___','<span class="vw-g" id="cgg">＿＿＿</span>')}”</div><div class="cg-pt">${H(r.pt)}</div><div class="vw-o">${fxShuffle(r.o).map(o=>`<button type="button">${H(o)}</button>`).join('')}</div><div class="vw-h" id="cgh"></div><div id="fb"></div></div>`;
      cta('Escolha a palavra',false);let tries=0;
      st.querySelectorAll('.vw-o button').forEach(b=>b.onclick=()=>{if(done)return;
        if(b.textContent===r.a){done=true;const g=q('#cgg',st);g.textContent=r.a;g.classList.add('ok');st.querySelectorAll('.vw-o button').forEach(x=>x.disabled=true);P.streak=tries?0:(P.streak||0)+1;fxGrade(true,'',r.a);say2(r.en.replace('___',r.a));next(!tries)}
        else{tries++;b.classList.add('no');b.disabled=true;q('#cgh',st).textContent='💡 Ouça a frase de novo e pense no sentido.';P.streak=0;try{sfx('oops');say2(r.en.replace('___',''))}catch(e){}}});
    }else if(r.t==='tf'){
      st.innerHTML=`<div class="step fx cu2">${head()}<div class="cg-q">Verdade ou mito?</div><div class="cu2-fact">${mk(r.s)}</div><div class="cg-tf"><button type="button" class="t">✅ Verdade</button><button type="button" class="f">❌ Mito</button></div><div id="fb"></div></div>`;
      cta('Verdade ou mito?',false);
      st.querySelectorAll('.cg-tf button').forEach(b=>b.onclick=()=>{if(done)return;done=true;const ok=(b.classList.contains('t'))===r.a;P.streak=ok?(P.streak||0)+1:0;fxGrade(ok,r.why||'',r.a?'Verdade':'Mito');next(ok)});
    }else{
      st.innerHTML=`<div class="step fx cu2">${head()}<div class="cu2-q">${H(r.q)}</div><div class="rdg-o">${r.o.map((o,i)=>`<button type="button" data-i="${i}">${H(o)}</button>`).join('')}</div><div id="fb"></div></div>`;
      cta('Escolha uma resposta',false);
      st.querySelectorAll('.rdg-o button').forEach(b=>b.onclick=()=>{if(done)return;done=true;const ok=+b.dataset.i===r.a;b.classList.add(ok?'ok':'no');if(!ok)st.querySelectorAll('.rdg-o button')[r.a].classList.add('ok');P.streak=ok?(P.streak||0)+1:0;fxGrade(ok,r.why||'',r.o[r.a]);next(ok)});
    }
    say(r.t==='order'?'Qual vem primeiro? Toque na ordem da história.':'Missão da obra!')};
  draw()};
FXR.culttl=function(f,st,n){
  const W=f.works;let need=0,miss=0,done=false;P.fx.done=false;P.fx.cta=null;
  const order=W.map((w,i)=>({w,i})).sort((a,b)=>a.w.y-b.w.y).map(o=>o.i);
  const art=f.pa?`<div class="cu2-art">${CULT_PROC(f.pa,1)}</div>`:'';
  st.innerHTML=`<div class="step fx cu2">${fxKindBar(f,n)}<h2 class="fx-h">${H(f.title)}</h2>${art}
  ${f.fact?`<div class="cu2-fact">${mk(f.fact)}</div>`:''}<div class="cg-q">Linha do tempo: toque da obra mais ANTIGA para a mais NOVA.</div>
  ${fxShuffle(W.map((w,i)=>({w,i}))).map(o=>`<button type="button" class="cg-c" data-i="${o.i}"><b>${H(o.w.k)}</b> ${H(o.w.n)}<span class="cg-yr">· ${o.w.y}</span><i></i></button>`).join('')}<div id="fb"></div></div>`;
  cta('Toque na ordem do tempo',false);
  st.querySelectorAll('.cg-c').forEach(b=>b.onclick=()=>{if(b.classList.contains('pick')||done)return;const i=+b.dataset.i;
    if(i===order[need]){b.classList.add('pick','rev');b.querySelector('i').textContent=need+1;need++;try{sfx('pop')}catch(e){}
      if(need>=W.length){done=true;st.querySelectorAll('.cg-c').forEach(x=>x.classList.add('rev'));P.streak=miss?0:(P.streak||0)+1;if(!miss)P.score++;fxGrade(!miss,'As datas apareceram: confira a ordem.',null);P.fx.done=true;cta(P.t.cont,true,true)}}
    else{miss++;b.classList.add('no');setTimeout(()=>b.classList.remove('no'),450);P.streak=0;try{sfx('oops')}catch(e){}}});
  say(f.say||'Qual obra veio primeiro? Monte a linha do tempo!')};
/* ---------- cultura: cartão ilustrado + pergunta (cultq: toque único · cult: curiosidade + pergunta) ---------- */
function cultStep(kind){return function(f,st,n){
  const QS=f.qs||[f.q];let qi=0;
  const art=f.pa?`<div class="cu2-art">${CULT_PROC(f.pa,1)}</div>`:'';
  const draw=()=>{const Q=QS[qi];let done=false;
    st.innerHTML=`<div class="step fx cu2">${fxKindBar(f,n)}<h2 class="fx-h">${H(f.title)}${QS.length>1?` <small>${qi+1}/${QS.length}</small>`:''}</h2>${qi===0?art:''}
    ${f.work&&qi===0?`<div class="cu2-work"><span>${H(f.work)}</span>${f.tag?`<small>${H(f.tag)}</small>`:''}</div>`:''}
    ${f.fact&&qi===0?`<div class="cu2-fact">${mk(f.fact)}</div>`:''}
    <div class="cu2-q">${H(Q.q)}</div><div class="rdg-o">${Q.o.map((o,i)=>`<button type="button" data-i="${i}">${H(o)}</button>`).join('')}</div><div id="fb"></div></div>`;
    P.fx.cta=null;cta('Escolha uma resposta',false);
    st.querySelectorAll('.rdg-o button').forEach(b=>b.onclick=()=>{if(done)return;done=true;const i=+b.dataset.i,ok=i===Q.a;
      b.classList.add(ok?'ok':'no');if(!ok)st.querySelectorAll('.rdg-o button')[Q.a].classList.add('ok');if(ok)P.score++;
      fxGrade(ok,Q.why||'',Q.o[Q.a]);P.answered=true;
      if(qi<QS.length-1){P.fx.cta=()=>{qi++;draw();return true};cta('Próxima pergunta ▶',true,true)}else cta(P.t.cont,true,true)});
    say(f.say||'Uma curiosidade cultural! Toque na resposta.')};
  draw()}}
FXR.cultq=cultStep('q');FXR.cult=cultStep('c');
/* ---------- leitura lúdica: conversa com lacunas ---------- */
FXR.rdgplay=function(f,st,n){
  const T=f.turns,cast=f.cast;let ti=0,hits=0,gaps=0,tries=0,tm=0;
  P.fx.done=false;P.fx.cta=()=>false;
  st.innerHTML=`<div class="step fx rp">${fxKindBar(f,n)}<h2 class="fx-h">${H(f.title)}</h2><div class="rp-chat" id="rpc"></div><div class="rp-opts" id="rpo"></div><div class="rp-hint" id="rph"></div><div id="rpe"></div><div id="fb"></div></div>`;
  const chat=q('#rpc',st),opts=q('#rpo',st),hint=q('#rph',st);
  const plain=t=>t.replace(/\[\[|\]\]/g,'');
  const mkB=(t,gap)=>{const c=cast[t.w],r=t.w%2?'r':'';const txt=H(t.t).replace(/\[\[(.+?)\]\]/,gap?'<span class="rp-gap" id="rpg">＿＿＿</span>':'<span class="rp-gap ok">$1</span>');
    const d=document.createElement('div');d.className='rp-b '+r;d.innerHTML=`<span class="rp-av" style="background:${c[1]}22">${c[0]}</span><div class="rp-bb"><p>${txt}</p><small>${H(t.pt)}</small></div>`;
    d.querySelector('.rp-bb').onclick=e=>{e.currentTarget.classList.toggle('on');say2(plain(t.t))};chat.appendChild(d);return d};
  const show=()=>{
    if(!P||!chat.isConnected)return;if(ti>=T.length)return finish();
    const t=T[ti];tries=0;hint.textContent='';opts.innerHTML='';
    if(!t.o){mkB(t,false);say2(plain(t.t));ti++;tm=setTimeout(show,1500);return}
    mkB(t,true);gaps++;const ans=t.o[0];
    cta('Toque na resposta certa',false);
    fxShuffle(t.o).forEach(o=>{const b=document.createElement('button');b.type='button';b.textContent=o;
      b.onclick=()=>{
        if(o===ans){const g=q('#rpg',st);g.textContent=o;g.classList.add('ok');g.removeAttribute('id');opts.innerHTML='';hint.textContent='';
          if(tries===0)hits++;P.streak=tries===0?(P.streak||0)+1:0;fxGrade(true,'',ans);
          say2(plain(t.t));ti++;tm=setTimeout(show,1500)}
        else{tries++;b.classList.add('no');b.disabled=true;hint.textContent='💡 '+t.h;P.streak=0;try{sfx('oops')}catch(e){}}};
      opts.appendChild(b)})};
  const finish=()=>{
    opts.innerHTML='';hint.textContent='';P.score+=hits;P.fx.done=true;
    const sc=gaps?hits/gaps:1,stars=sc>=.8?3:sc>=.5?2:1;
    q('#rpe',st).innerHTML=`<div class="rp-res">${'★'.repeat(stars)}${'☆'.repeat(3-stars)}</div><div class="rp-rule"><span>📌</span><span><b>Você descobriu a regra!</b><br>${mk(f.rule)}</span></div>`;
    try{sfx('tada');confetti(50)}catch(e){}
    P.fx.cta=null;cta(P.t.cont,true,true);say('Regra descoberta jogando! 🎉');setTimeout(()=>{const b=document.querySelector('#pbody');if(b)b.scrollTop=b.scrollHeight},60)};
  say(f.say||'Complete a conversa tocando na resposta certa!');show();
  return()=>clearTimeout(tm)};
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
