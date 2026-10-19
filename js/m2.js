/* Pogglot · modelo 2 de episódio (mdl:2)
   Capa com a obra · Reading · Palavras em frases · Estrutura · Common Expressions · Revisão + diálogo incompleto
   + ponte do Poggie modernizada + microfones aguardando indicação */
(function(){
'use strict';
if(typeof FXR==='undefined'||!window.RWB)return;
const RB=window.RWB,ico=RB.ico;
const is2=()=>{try{return !!(P&&P.e&&P.e.mdl===2)}catch(e){return false}};
const lang=()=>(P&&P.c&&P.c.tts)||'en-US';
const uline=h=>h.replace(/\{\{(.+?)\}\}/g,'<u class="m2-u">$1</u>');
const bare=s=>String(s).replace(/\{\{|\}\}/g,'');
const H=s=>uline(mk(s));
const T=s=>plain(bare(s));

/* ---------- rótulos ---------- */
Object.assign(FX_KIND,{read:'story',wsent:'vocab',pat:'grammar',cexp:'vocab',review:'story',dfill:'practice'});
Object.assign(FX_LABEL,{read:'Reading',wsent:'Palavras em frases',pat:'Estrutura da frase',cexp:'Common Expressions',review:'Revisão',dfill:'Complete o diálogo'});
FX_LABEL.ppat='Escolha a peça';

/* ---------- textos para o áudio ---------- */
if(window.PogTTS&&PogTTS.episodeTexts){
  const o=PogTTS.episodeTexts;
  PogTTS.episodeTexts=function(e){
    const out=o(e),seen=new Set(out.map(x=>x.text+'|'+(x.speaker||'')));
    const add=(t,sp)=>{t=T(t).trim();const k=t+'|'+(sp||'');if(t&&t.length<400&&!seen.has(k)){seen.add(k);out.push({text:t,speaker:sp||null})}};
    const walk=f=>{
      if(f.k==='read')(f.s||[]).forEach(x=>add(x[0]));
      if(f.k==='wsent')(f.items||[]).forEach(x=>add(x.en));
      if(f.k==='pat'){(f.ex||[]).forEach(x=>add(x[0]));(f.formulas||[]).forEach(fm=>add(fm.blocks.map(b=>b[0]).join(' ')));
        (f.pages||[]).forEach(p=>{const base=p.slots.map(()=>0);add(patBuild(p,base)[0]);p.slots.forEach((sl,k)=>{if(sl.opts.length>1&&sl.dep==null)sl.opts.forEach((o,j)=>{const s2=base.slice();s2[k]=j;add(patBuild(p,s2)[0])})})})}
      if(f.k==='xpr')(f.items||[]).forEach(it=>{if(it.sw&&it.slot!=null){it.sw.forEach(q=>{const b=it.b.map(x=>x[0]);b[it.slot]=q[0]+(it.tail||'');add(b.join(' '))})}});
      if(f.k==='cexp')(f.items||[]).forEach(x=>{add(x.x);add(x.ex[0],x.who||null)});
      if(f.k==='review')(f.recap||[]).forEach(x=>add(x[0]));
      if(f.k==='dfill')(f.lines||[]).forEach(l=>add(l[1],l[0]));
      (f.then||[]).forEach(walk);
    };
    (e.fr||[]).forEach(walk);
    return out;
  };
}

/* ---------- microfone: oculto no modelo 2 até o professor indicar os pontos ---------- */
if(window.PogVoice&&PogVoice.mount){
  const m=PogVoice.mount;
  PogVoice.mount=function(host,o){
    if(is2()&&!(o&&o.force)){
      try{const h=host&&(host.closest('.pv-host')||host);if(h){h.hidden=true;h.style.display='none';const p=h.previousElementSibling;if(p&&p.classList.contains('sl-h'))p.style.display='none'}
        const sh=host&&host.parentElement&&host.parentElement.querySelector(':scope>.sl-h');if(sh)sh.style.display='none'}catch(e){}
      return;
    }
    return m.apply(this,arguments);
  };
}

/* ---------- player compacto reutilizável ---------- */
function dpMarkup(N,aria){
  return `<div class="dp" role="group" aria-label="${aria}"><div class="dp-now" aria-live="polite">Toque em ▶ para ouvir</div>
  <div class="dp-row"><button type="button" class="dp-play" aria-label="Tocar">${ico.play}</button>
  <button type="button" class="dp-b dp-prev" aria-label="Anterior">${ico.prev}</button>
  <div class="dp-track">${Array.from({length:N},(_,i)=>`<button type="button" class="dp-seg" data-i="${i}" aria-label="Ir para ${i+1}"></button>`).join('')}</div>
  <button type="button" class="dp-b dp-next" aria-label="Próxima">${ico.next}</button>
  <button type="button" class="dp-b dp-rep" aria-label="Repetir">${ico.redo}</button>
  <span class="dp-sp" role="group" aria-label="Velocidade"><button type="button" data-s="0" aria-label="Velocidade natural" title="Natural">1×</button><button type="button" data-s="1" aria-label="Falar devagar" title="Devagar">🐢</button></span></div></div>`;
}
function wirePlayer(root,L,unit,hooks){
  hooks=hooks||{};const N=L.length;
  const segs=[...root.querySelectorAll('.dp-seg')],play=root.querySelector('.dp-play'),now=root.querySelector('.dp-now');
  const pl=RB.makePlayer(L,(i,playing,slow,ended)=>{
    segs.forEach((s,k)=>{s.classList.toggle('done',k<i||(ended&&k===i));s.classList.toggle('cur',k===i&&!ended)});
    play.innerHTML=playing?ico.pause:ico.play;play.setAttribute('aria-label',playing?'Pausar':'Tocar');
    root.classList.toggle('on',playing);
    now.textContent=ended?'Fim · toque em ▶ para ouvir de novo':`${unit} ${i+1} de ${N}${playing?'':' · pausado'}`;
    root.querySelector('.dp-prev').disabled=i<=0;root.querySelector('.dp-next').disabled=i>=N-1;
    root.querySelectorAll('.dp-sp button').forEach(b=>b.classList.toggle('on',(b.dataset.s==='1')===slow));
    hooks.state&&hooks.state(i,playing,slow,ended);
  },(i,silent)=>{hooks.line&&hooks.line(i,silent)});
  play.onclick=()=>pl.toggle();
  root.querySelector('.dp-prev').onclick=()=>pl.prev();
  root.querySelector('.dp-next').onclick=()=>pl.next();
  root.querySelector('.dp-rep').onclick=()=>pl.repeat();
  segs.forEach(s=>s.onclick=()=>pl.seek(+s.dataset.i));
  root.querySelectorAll('.dp-sp button').forEach(b=>b.onclick=()=>pl.setSlow(b.dataset.s==='1'));
  const watch=setInterval(()=>{if(!root.isConnected){clearInterval(watch);pl.pause()}},500);
  return pl;
}

/* ---------- 1) Capa: a obra em cena ---------- */
const _cover=FXR.cover;
FXR.cover=function(f,st,n){
  if(!f.cw){if(!f.b2)return _cover(f,st,n);const g0=Object.assign({},f,{hook:['',''],chips:[],cul:null});_cover(g0,st,n);st.querySelectorAll('.fx-hook,.fx-chips,.fx-cul').forEach(x=>x.remove());cta('Começar o episódio',true,true);return}
  const g=Object.assign({},f,{hook:['',''],chips:[],cul:null});
  _cover(g,st,n);
  const step=st.querySelector('.step'),c=f.cw;
  step.querySelectorAll('.fx-hook,.fx-chips,.fx-cul').forEach(x=>x.remove());
  const art=c.pa?fxArt({pa:c.pa},.62):(c.scene?fxArt(c.scene,.62):'');
  const d=document.createElement('section');d.className='m2-work';
  d.style.setProperty('--c1',(c.c||['#ffb347','#7b4397'])[0]);d.style.setProperty('--c2',(c.c||['#ffb347','#7b4397'])[1]);
  d.innerHTML=`<div class="m2w-art">${art}<span class="m2w-type">${esc(c.kind)} · ${esc(c.year)}</span></div>
   <div class="m2w-body"><small class="m2w-k">🎭 OBRA EM CENA</small><h2>${esc(c.work)}</h2><p class="m2w-by">${esc(c.by)}</p>
   <p class="m2w-intro">${mk(c.intro)}</p>
   <div class="m2w-fact"><span class="m2w-fi">${c.fact[0]}</span><div><small>${esc(c.fact[1])}</small><p>${mk(c.fact[2])}</p></div></div></div>`;
  step.appendChild(d);
  cta('Começar o episódio',true,true);
};

/* ---------- 2) Reading ---------- */
FXR.read=function(f,st,n){
  const S=f.s,N=S.length;let tr=false,touched=false;
  st.innerHTML=`<div class="step fx m2-read">${fxKindBar(f,n)}<h2 class="fx-h">${esc(f.title)}</h2>
   ${dpMarkup(N,'Player do reading')}
   <article class="m2-text" aria-label="Texto">${S.map((s,i)=>`<button type="button" class="m2-s" data-i="${i}">${H(s[0])}</button>`).join(' ')}</article>
   <div class="m2-curtr" id="m2ct" hidden><small>🇧🇷 Tradução da frase</small><p></p></div>
   <button type="button" class="m2-trb" id="m2tb">🇧🇷 Ver tradução</button>
   <div class="m2-tr" id="m2tr" hidden>${S.map(s=>`<p>${esc(s[1])}</p>`).join('')}</div>
   <div class="m2-hint"><u class="m2-u">Sublinhadas</u> = palavras que você vai aprender no próximo quadro.</div></div>`;
  const root=st.querySelector('.dp'),sp=[...st.querySelectorAll('.m2-s')];
  const L=S.map(s=>[null,bare(s[0])]);
  const showTr=i=>{const c=st.querySelector('#m2ct');if(!c||i==null||!S[i])return;c.hidden=false;c.querySelector('p').textContent=S[i][1]};
  const pl=wirePlayer(root,L,'Frase',{state:(i,pl_,sl,en)=>{sp.forEach((x,k)=>x.classList.toggle('cur',k===i&&!en));if(!en&&i!=null&&i>=0)showTr(i)},
    line:(i,silent)=>{const b=sp[i];if(b&&!silent)b.scrollIntoView({behavior:'smooth',block:'nearest'})}});
  sp.forEach(b=>b.onclick=()=>{touched=true;showTr(+b.dataset.i);pl.playFrom(+b.dataset.i)});
  st.querySelector('#m2tb').onclick=e=>{tr=!tr;st.querySelector('#m2tr').hidden=!tr;e.currentTarget.textContent=tr?'🇧🇷 Esconder tradução':'🇧🇷 Ver tradução'};
  cta('Ver as palavras',true,true);
  setTimeout(()=>{if(!touched&&root.isConnected)pl.playFrom(0)},600);
  say(f.say||'Leia e ouça. As palavras sublinhadas são as de hoje!');
};

/* ---------- 3) Palavras em frases (lúdico: revele a palavra escondida) ---------- */
FXR.wsent=function(f,st,n){
  const R=f.items,seen=new Set();
  const part=en=>{const m=/\{\{(.+?)\}\}/.exec(en);return m?[en.slice(0,m.index),m[1],en.slice(m.index+m[0].length)]:[en,'','']};
  st.innerHTML=`<div class="step fx m2-ws">${fxKindBar(f,n)}
   <div class="m2-wh"><h2 class="fx-h">${esc(f.title||'As palavras em frases')}</h2><span class="m2-stars" id="m2st">⭐ 0/${R.length}</span></div>
   <p class="m2-lead">${esc(f.lead||'Cada frase esconde uma palavra de hoje. Toque na figura para revelar!')}</p>
   <div class="m2-wl">${R.map((w,i)=>{const p=part(w.en);return `<div class="m2-wc" data-i="${i}" style="--i:${i};--hue:${(i*47+20)%360}">
     <p class="m2-wg"><span>${esc(p[0])}</span><button type="button" class="m2-chip" aria-label="Revelar a palavra"><span class="m2-cf m2-front">${fxIcon(w.ic,38)}<small>toque</small></span><span class="m2-cf m2-back"><b>${esc(p[1])}</b></span></button><span>${esc(p[2])}</span></p>
     <div class="m2-wp"><small>${esc(w.pt)}</small><button type="button" class="m2-wsay say2" aria-label="Ouvir de novo">${spk}</button></div></div>`}).join('')}</div>
   <p class="fx-hint" id="fxhint">Toque nas figuras: cada uma vira a palavra certa.</p></div>`;
  const boom=(host)=>{for(let k=0;k<8;k++){const s=document.createElement('i');s.className='m2-spk';const a=k/8*6.283;s.style.setProperty('--x',Math.cos(a)*34+'px');s.style.setProperty('--y',Math.sin(a)*26+'px');s.textContent=['✨','⭐','💫'][k%3];host.appendChild(s);setTimeout(()=>s.remove(),700)}};
  st.querySelectorAll('.m2-wc').forEach(c=>{
    const i=+c.dataset.i,chip=c.querySelector('.m2-chip');
    const go=()=>{
      const first=!c.classList.contains('open');c.classList.add('open');seen.add(i);sfx(first?'key':'pop');
      if(first)boom(chip);
      fxSay(T(R[i].en));
      const h=st.querySelector('#fxhint'),sc=st.querySelector('#m2st');sc.textContent=`⭐ ${seen.size}/${R.length}`;
      if(seen.size>=R.length){cta('Continuar',true,true);h.textContent='Todas reveladas! 🎉'}else h.textContent=`${seen.size}/${R.length} palavras reveladas`;
    };
    chip.onclick=go;c.querySelector('.m2-wsay').onclick=ev=>{ev.stopPropagation();sfx('pop');fxSay(T(R[i].en))};
  });
  cta('Revele todas as palavras',false);say(f.say||'Palavra solta é fácil de esquecer. Dentro da frase, ela fica!');
};

/* ---------- 4) Estrutura da frase: molde em 3 páginas com troca de peças ---------- */
const PATC=['#7C4DFF','#12B3A8','#FF6F59','#E0499D','#FFB020'];
const cap1=s=>s?s.charAt(0).toUpperCase()+s.slice(1):s;
function patBuild(p,sel){
  let en='',pt='';
  p.slots.forEach((sl,k)=>{
    const o=sl.opts[sl.dep!=null?sel[sl.dep]:sel[k]]||sl.opts[0];
    const pre=sl.pre!=null?sl.pre:' ';
    if(k)en+=pre;en+=o[0];
    if(o[1]){pt+=(pt?(sl.pre!=null?sl.pre:' '):'')+o[1]}
  });
  return [cap1(en)+(p.end?p.end[0]:''),cap1(pt)+(p.end?p.end[1]:'')];
}
window.M2PatBuild=patBuild;
FXR.pat=function(f,st,n){
  const PG=f.pages,NP=PG.length;let pi=0,reach=0;
  const sel=PG.map(p=>p.slots.map(()=>0)),sw=PG.map(()=>0),act=PG.map(p=>Math.max(0,p.slots.findIndex(s=>s.opts.length>1&&s.dep==null)));
  const NEED=2;
  st.innerHTML=`<div class="step fx m2-pat">${fxKindBar(f,n)}
   <div class="m2-pq"><small>${esc(f.kicker||'ESTRUTURA DA FRASE · O MOLDE')}</small><h2 class="fx-h">${esc(f.title)}</h2>${f.sub?`<p>${esc(f.sub)}</p>`:''}</div>
   <div class="m2-tabs" id="m2tabs"></div><div class="m2-pcard" id="m2pc"></div>
   ${f.tip?`<div class="fx-tip">💡 ${mk(f.tip)}</div>`:''}</div>`;
  const tabs=st.querySelector('#m2tabs'),box=st.querySelector('#m2pc');
  const ctaState=()=>{
    const ok=sw[pi]>=NEED,last=pi===NP-1;
    if(ok)cta(last?'Continuar':'Próxima estrutura ▶',true,true);else cta(`Troque ${NEED-sw[pi]} peça${NEED-sw[pi]>1?'s':''} para continuar`,false);
  };
  const drawTabs=()=>{tabs.innerHTML=PG.map((p,j)=>`<button type="button" class="m2-tab${j===pi?' on':''}${j>reach?' lock':''}" data-j="${j}" ${j>reach?'disabled':''}><b>${j+1}</b><span>${esc(p.label)}</span></button>`).join('');
    tabs.querySelectorAll('.m2-tab').forEach(b=>b.onclick=()=>{pi=+b.dataset.j;sfx('pop');draw()})};
  let pop=-1;
  const draw=()=>{
    const p=PG[pi],s=sel[pi],a=act[pi],[en,pt]=patBuild(p,s);
    drawTabs();
    const cats=p.slots.map((sl,k)=>`<div class="m2-sl${sl.opts.length>1&&sl.dep==null?' sw':' fx'}${k===a?' act':''}${k===pop?' pop':''}" style="--b:${PATC[k%PATC.length]}"><small>${esc(sl.cat)}${sl.catpt?`<em>${esc(sl.catpt)}</em>`:''}</small>
      <button type="button" class="m2-blk" data-k="${k}" ${sl.opts.length>1&&sl.dep==null?'':'tabindex="-1"'}><b>${esc(sl.opts[sl.dep!=null?s[sl.dep]:s[k]][0])}</b>${sl.opts.length>1&&sl.dep==null?'<i>🔁</i>':''}</button></div>`).join('<i class="m2-pl">+</i>');
    const sl=p.slots[a];
    box.innerHTML=`<div class="m2-pg"><em>PÁGINA ${pi+1}/${NP}</em><h3>${esc(p.label)}</h3></div>
      <div class="m2-struct">${cats}</div>
      ${sl&&sl.opts.length>1&&sl.dep==null?`<div class="m2-swap"><small>🔁 Troque a peça <b>${esc(sl.cat)}</b> por:</small><div class="m2-opts">${sl.opts.map((o,j)=>`<button type="button" class="m2-opt${j===s[a]?' on':''}" data-j="${j}">${esc(o[0])}</button>`).join('')}</div></div>`:''}
      <button type="button" class="m2-live" id="m2lv"><span class="say2">${spk}</span><div><b>${esc(en)}</b><small>${esc(pt)}</small></div></button>
      <p class="fx-hint" id="fxhint">${sw[pi]>=NEED?'Muito bem! Pode trocar mais peças ou seguir. 🎉':`Troque pelo menos ${NEED} peças (${Math.min(sw[pi],NEED)}/${NEED}).`}</p>`;
    pop=-1;
    box.querySelectorAll('.m2-sl.sw .m2-blk').forEach(b=>b.onclick=()=>{act[pi]=+b.dataset.k;sfx('pop');draw()});
    box.querySelectorAll('.m2-opt').forEach(b=>b.onclick=()=>{
      const j=+b.dataset.j;if(j===sel[pi][a]){fxSay(plain(en));return}
      sel[pi][a]=j;sw[pi]++;pop=a;sfx('key');
      const [e2]=patBuild(p,sel[pi]);draw();fxSay(plain(e2));
    });
    box.querySelector('#m2lv').onclick=()=>{sfx('pop');fxSay(plain(en))};
    ctaState();
  };
  P.fx.cta=()=>{if(sw[pi]>=NEED&&pi<NP-1){pi++;reach=Math.max(reach,pi);draw();try{st.scrollTo({top:0,behavior:'smooth'})}catch(e){}return true}return false};
  draw();say(f.say||'Esse é o molde da frase. É só trocar as peças!');
};

/* ---------- 5) Common Expressions ---------- */
FXR.cexp=function(f,st,n){
  const R=f.items,seen=new Set();
  st.innerHTML=`<div class="step fx m2-cx">${fxKindBar(f,n)}
   <div class="vb-head"><div><small class="vb-kicker">🗨️ ${R.length} expressões que os americanos usam</small><h2 class="fx-h">${esc(f.title||'Common Expressions')}</h2></div></div>
   ${f.intro?`<p class="m2-lead">${mk(f.intro)}</p>`:''}
   <div class="m2-cl">${R.map((x,i)=>`<div class="m2-ce" data-i="${i}" style="--i:${i}">
     <button type="button" class="m2-cet" aria-expanded="false"><span class="m2-cei">${fxIcon(x.ic,44)}</span><span class="m2-cem"><b>${esc(x.x)}</b><small>${esc(x.pt)}</small></span><span class="say2">${spk}</span></button>
     <div class="m2-cmore"><p class="m2-use">${mk(x.use)}</p><div class="m2-cult"><span>🌎</span><p>${mk(x.cult)}</p></div>
     <button type="button" class="xp-say m2-cex" data-s="${esc(T(x.ex[0]))}" data-w="${esc(x.who||'')}"><span class="vb-bub"><p>${H(x.ex[0])}</p><small>${esc(x.ex[1])}</small></span><span class="say2">${spk}</span></button></div></div>`).join('')}</div>
   <p class="fx-hint" id="fxhint">Toque em cada expressão.</p></div>`;
  st.querySelectorAll('.m2-ce').forEach(c=>{
    const i=+c.dataset.i,it=R[i];
    c.querySelector('.m2-cet').onclick=()=>{
      c.classList.add('open');c.querySelector('.m2-cet').setAttribute('aria-expanded','true');seen.add(i);sfx('pop');fxSay(T(it.x));
      setTimeout(()=>{try{c.scrollIntoView({behavior:'smooth',block:'nearest'})}catch(e){}},120);
      const h=st.querySelector('#fxhint');
      if(seen.size>=R.length){cta('Continuar',true,true);h.textContent='Todas descobertas! 🎉'}else h.textContent=`${seen.size}/${R.length} expressões`;
    };
    c.querySelector('.m2-cex').onclick=ev=>{ev.stopPropagation();sfx('pop');fxSay(ev.currentTarget.dataset.s,ev.currentTarget.dataset.w||undefined)};
  });
  cta('Descubra todas as expressões',false);say(f.say||'Expressão pronta não se traduz palavra por palavra. Aprenda como um bloco!');
};

/* ---------- 6) Revisão do episódio anterior ---------- */
FXR.review=function(f,st,n){
  st.innerHTML=`<div class="step fx m2-rv">${fxKindBar(f,n)}
   <div class="m2-rvh"><span class="m2-rvi">↺</span><div><small>NO EPISÓDIO ANTERIOR</small><h2 class="fx-h">${esc(f.prev)}</h2>${f.work?`<p>🎭 ${esc(f.work)}</p>`:''}</div></div>
   <p class="m2-lead">${esc(f.lead||'Um resumo rápido antes de começar. Toque para ouvir.')}</p>
   <div class="m2-rl">${f.recap.map((x,i)=>`<button type="button" class="fx-vr" data-s="${esc(T(x[0]))}"><span class="say2">${spk}</span><div><b>${H(x[0])}</b><small>${esc(x[1])}</small></div></button>`).join('')}</div>
   ${f.next?`<div class="fx-tip">🎯 ${mk(f.next)}</div>`:''}</div>`;
  cta('Testar o que lembro',true,true);say(f.say||'Bora relembrar antes de seguir!');
};

/* ---------- 7) Diálogo com falas em falta ---------- */
FXR.dfill=function(f,st,n){
  const cast=f.cast||{},names=Object.keys(cast).slice(0,2),L=f.lines,gaps=new Set(f.gaps);
  const pieces=fxShuffle(f.gaps.map(i=>({i,t:L[i][1]})));
  const filled={};let selP=null,selS=null,errs=0;
  st.innerHTML=`<div class="step fx m2-df">${fxKindBar(f,n)}
   <h2 class="fx-h">${esc(f.title||'Complete o diálogo')}</h2>
   <p class="m2-lead">${esc(f.intro||'Ouça o diálogo no player. Depois toque numa fala-peça e no espaço onde ela encaixa.')}</p>
   ${dpMarkup(L.length,'Player do diálogo')}
   <div class="m2-dl">${L.map((l,i)=>{const c=cast[l[0]]||['🙂','#888'];const side=names.indexOf(l[0])===1?'r':'l';
     return `<div class="fx-line ${side}" data-i="${i}" style="--c:${c[1]}"><span class="fx-lav">${c[0]}</span><div class="fx-bub"><b>${esc(l[0])}</b>${gaps.has(i)?`<button type="button" class="m2-slot" data-i="${i}"><span>🔊 Fala ${i+1}: ouça e escolha a peça</span></button>`:`<p>${mk(l[1])}</p><small class="fx-tr">${esc(l[2]||'')}</small>`}</div></div>`}).join('')}</div>
   <div class="m2-bank-h">Peças-fala</div>
   <div class="m2-bank">${pieces.map((p,k)=>`<button type="button" class="m2-pc" data-i="${p.i}">${esc(p.t)}</button>`).join('')}</div>
   <div id="fb"></div></div>`;
  const root=st.querySelector('.dp'),rows=[...st.querySelectorAll('.m2-dl .fx-line')];
  const pl=wirePlayer(root,L.map(l=>[l[0],l[1]]),'Fala',{state:(i,p,s,en)=>rows.forEach((r,k)=>r.classList.toggle('dp-cur',k===i&&!en)),
    line:(i,silent)=>{const r=rows[i];if(r&&!silent)r.scrollIntoView({behavior:'smooth',block:'nearest'})}});
  const mark=()=>{st.querySelectorAll('.m2-pc').forEach(b=>b.classList.toggle('sel',selP!=null&&+b.dataset.i===selP&&!b.disabled));
    st.querySelectorAll('.m2-slot').forEach(b=>b.classList.toggle('sel',selS!=null&&+b.dataset.i===selS))};
  const attempt=()=>{
    if(selP==null||selS==null)return;
    const sl=st.querySelector(`.m2-slot[data-i="${selS}"]`),pc=st.querySelector(`.m2-pc[data-i="${selP}"]`);
    if(selP===selS){
      const l=L[selS],row=rows[selS];
      row.querySelector('.fx-bub').innerHTML=`<b>${esc(l[0])}</b><p>${mk(l[1])}</p><small class="fx-tr">${esc(l[2]||'')}</small>`;
      row.classList.add('m2-okrow');pc.disabled=true;pc.classList.add('used');filled[selS]=1;sfx('plank');fxGrade(true,null,null);
      selP=selS=null;mark();
      if(Object.keys(filled).length>=f.gaps.length){setTimeout(()=>{sfx('tada');try{confetti(60)}catch(e){}},200);cta('Continuar',true,true);st.querySelector('#fb').innerHTML=`<div class="feedback ok"><div><b>Diálogo completo! 🎉</b>${errs?`Você trocou ${errs}x, mas chegou lá.`:'Sem nenhum erro.'} Ouça tudo de novo no player.</div></div>`}
    }else{
      errs++;sl.classList.remove('shake');void sl.offsetWidth;sl.classList.add('shake');beep(false);
      st.querySelector('#fb').innerHTML=`<div class="feedback no"><div><b>Essa peça não encaixa aí.</b>Toque no espaço para ouvir aquela fala no player e tente outra peça.</div></div>`;
      pl.playFrom(selS);selP=null;mark();
    }
  };
  st.querySelectorAll('.m2-pc').forEach(b=>b.onclick=()=>{if(b.disabled)return;selP=+b.dataset.i;sfx('pop');fxSay(L[selP][1],L[selP][0]);mark();attempt()});
  st.querySelectorAll('.m2-slot').forEach(b=>b.onclick=()=>{selS=+b.dataset.i;pl.playFrom(selS);mark();attempt()});
  cta('Complete o diálogo',false);say('Ouça o diálogo e encaixe as falas que estão faltando.');
};

/* ---------- 8) Ponte do Poggie modernizada ---------- */
const DECO=`<svg class="pgm-svg" viewBox="0 0 400 230" preserveAspectRatio="xMidYMax slice" aria-hidden="true">
<defs><linearGradient id="pgmS" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7FD1F2"/><stop offset=".62" stop-color="#FFE9B8"/><stop offset="1" stop-color="#FFC7A0"/></linearGradient>
<linearGradient id="pgmW" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5EC9E6"/><stop offset="1" stop-color="#1B7FB8"/></linearGradient></defs>
<rect width="400" height="230" fill="url(#pgmS)"/>
<circle cx="318" cy="58" r="30" fill="#FFF3C4" opacity=".9"/><circle cx="318" cy="58" r="20" fill="#FFE07A"/>
<g fill="#fff" opacity=".92" class="pgm-cl"><ellipse cx="70" cy="46" rx="30" ry="9"/><ellipse cx="92" cy="40" rx="20" ry="9"/><ellipse cx="226" cy="30" rx="26" ry="7"/><ellipse cx="244" cy="26" rx="15" ry="7"/></g>
<path d="M0 120 L48 84 L86 112 L142 66 L196 118 L250 80 L300 116 L352 76 L400 112 V150 H0Z" fill="#9CB7E6" opacity=".75"/>
<path d="M142 66 l14 14 -8 -3 -6 8 -6 -8 -8 3z M352 76 l12 12 -7 -2 -5 7 -5 -7 -7 2z" fill="#fff" opacity=".85"/>
<path d="M0 142 Q70 112 150 138 T300 130 T400 138 V170 H0Z" fill="#6CC59A"/>
<path d="M0 156 Q90 134 190 154 T400 146 V180 H0Z" fill="#46A872"/>
<g fill="#2E7A54"><path d="M30 156 l9 -34 9 34z M44 158 l8 -26 8 26z M338 152 l9 -36 9 36z M356 154 l8 -28 8 28z M372 156 l7 -22 7 22z"/></g>
<g fill="#7A5230"><rect x="37" y="156" width="4" height="8"/><rect x="350" y="152" width="4" height="8"/></g>
<rect y="168" width="400" height="62" fill="url(#pgmW)"/>
<g stroke="#fff" stroke-width="2" fill="none" opacity=".55" class="pgm-rp"><path d="M40 196 q10 -5 20 0 t20 0"/><path d="M150 212 q10 -5 20 0 t20 0"/><path d="M270 192 q10 -5 20 0 t20 0"/><path d="M330 214 q10 -5 20 0 t20 0"/></g>
<g stroke="#2B3A55" stroke-width="1.6" fill="none" opacity=".7"><path d="M120 40 q5 -6 10 0 q5 -6 10 0"/><path d="M150 54 q4 -5 8 0 q4 -5 8 0"/></g>
<g><rect x="6" y="132" width="5" height="40" fill="#8A5A2B"/><circle cx="8.5" cy="128" r="6" fill="#FFD76A"/><rect x="389" y="132" width="5" height="40" fill="#8A5A2B"/><circle cx="391.5" cy="128" r="6" fill="#FFD76A"/></g>
</svg>`;
const _pb=FXR.pbridge;
FXR.pbridge=function(f,st,n){
  _pb(f,st,n);
  if(!is2())return;
  const dec=()=>{const sc=st.querySelector('.pgx-scene.pgb');if(!sc||sc.querySelector('.pgm-deco'))return;
    sc.classList.add('m2');const d=document.createElement('div');d.className='pgm-deco';d.innerHTML=DECO;sc.prepend(d);
    const rail=document.createElement('div');rail.className='pgm-rail';sc.appendChild(rail)};
  dec();
  if(st._pgm)st._pgm.disconnect();
  st._pgm=new MutationObserver(dec);st._pgm.observe(st,{childList:true,subtree:true});
};
const _rfm=window.renderFx;
window.renderFx=function(n,st,lng){
  _rfm(n,st,lng);
  try{
    if(!is2())return;const f=P.e.fr[n];
    if(f&&f.then&&f.then.length){
      const bar=document.getElementById('azbar');if(bar&&window.AZ&&AZ.rail)bar.innerHTML=AZ.rail(f,n);
      st.querySelectorAll('.eyebrow').forEach(x=>x.remove());
      const step=st.querySelector('.step');if(step&&step.querySelector('.az-ill')===null){}
    }
  }catch(e){}
};

/* =====================================================================
   v47: compreensão do diálogo, laboratório lúdico, expressões comuns, situações novas
   ===================================================================== */
FX_KIND.dquiz='practice';FX_LABEL.dquiz='Você entendeu?';
const _fs=FXR.sound;
FXR.sound=function(f,st,n){FX_LABEL.sound=is2()?'Ouça e escolha':'Laboratório de sons';return _fs.apply(this,arguments)};
const _ftm=window.fxTotal;
window.fxTotal=function(e){let t=_ftm.apply(this,arguments);try{(e.fr||[]).forEach(f=>{if(f.k==='dquiz')t+=(f.items||[]).length})}catch(x){}return t};
if(window.PogTTS&&PogTTS.episodeTexts){
  const o2=PogTTS.episodeTexts;
  PogTTS.episodeTexts=function(e){
    const out=o2(e),seen=new Set(out.map(x=>x.text+'|'+(x.speaker||'')));
    const add=(t)=>{t=T(t).trim();const k=t+'|';if(t&&t.length<400&&!seen.has(k)){seen.add(k);out.push({text:t,speaker:null})}};
    const walk=f=>{if(f.k==='dquiz')(f.items||[]).forEach(x=>{add(x.q);(x.opts||[]).forEach(o=>add(o[1]))});(f.then||[]).forEach(walk)};
    (e.fr||[]).forEach(walk);return out;
  };
}
const burst=(host,em)=>{for(let k=0;k<10;k++){const s=document.createElement('i');s.className='m2-spk';const a=k/10*6.283;s.style.setProperty('--x',Math.cos(a)*(40+k%3*10)+'px');s.style.setProperty('--y',Math.sin(a)*(30+k%2*14)+'px');s.textContent=(em||['✨','⭐','💫','🎉'])[k%4];host.appendChild(s);setTimeout(()=>s.remove(),800)}};

/* ---------- compreensão do diálogo ---------- */
FXR.dquiz=function(f,st,n){
  const R=f.items,L=f.lines||[];let ri=0,tries=0,done=0;
  const draw=()=>{
    const r=R[ri];tries=0;P.answered=false;
    st.innerHTML=`<div class="step fx m2-dq">${fxKindBar(f,n)}
     <div class="m2-wh"><h2 class="fx-h">${esc(f.title||'Você entendeu?')} <small>${ri+1}/${R.length}</small></h2><span class="m2-stars">⭐ ${done}/${R.length}</span></div>
     <button type="button" class="m2-dqq" id="m2q"><span class="m2-dqe">🧐</span><div><b>${esc(r.q)}</b><small>${esc(r.pt)}</small></div><span class="say2">${spk}</span></button>
     <div class="m2-dqo c${r.opts.length}">${r.opts.map((o,i)=>`<button type="button" class="m2-dqc" data-i="${i}" style="--i:${i}"><span class="m2-dqi">${fxIcon(o[0],58)}</span><b>${esc(o[1])}</b></button>`).join('')}</div>
     <div id="m2ev"></div><div id="fb"></div></div>`;
    const sayq=()=>fxSay(plain(r.q));st.querySelector('#m2q').onclick=()=>{sfx('pop');sayq()};setTimeout(sayq,350);
    st.querySelectorAll('.m2-dqc').forEach(b=>b.onclick=()=>{
      if(P.answered)return;const i=+b.dataset.i;
      if(i!==r.a){tries++;b.disabled=true;b.classList.add('no');beep(false);fxGrade(false,tries>1?'Ouça o diálogo de novo: a resposta está lá.':'Quase! Pense no que cada pessoa disse.',null);return}
      P.answered=true;st.querySelectorAll('.m2-dqc').forEach((x,j)=>{x.disabled=true;if(j===r.a)x.classList.add('ok')});
      burst(b);sfx('key');if(tries===0){P.score++;done++}else done++;
      st.querySelector('.m2-stars').textContent=`⭐ ${done}/${R.length}`;
      const ln=L[r.line];
      if(ln)st.querySelector('#m2ev').innerHTML=`<button type="button" class="m2-ev"><span class="m2-eva">${esc(ln[0].slice(0,1))}</span><div><small>${esc(ln[0])} disse:</small><b>“${esc(ln[1])}”</b><em>${esc(ln[2]||'')}</em></div><span class="say2">${spk}</span></button>`;
      const evb=st.querySelector('.m2-ev');if(evb)evb.onclick=()=>{sfx('pop');fxSay(plain(ln[1]),ln[0])};
      fxGrade(true,r.why,null);
      setTimeout(()=>fxSay(plain(r.opts[r.a][1])),150);
      cta(ri<R.length-1?'Próxima pergunta ▶':'Continuar',true,true);
    });
    cta('Escolha a resposta',false);
  };
  P.fx.cta=()=>{if(P.answered&&ri<R.length-1){ri++;draw();return true}return false};
  draw();say(f.say||'Vamos ver se você entendeu o diálogo? Toque na resposta certa!');
};

/* ---------- laboratório de sons (lúdico) ---------- */
const _sl=FXR.soundlab;
FXR.soundlab=function(f,st,n){
  if(!is2())return _sl.apply(this,arguments);
  const I=f.intro||{},EX=f.ex||[],PR=f.pairs||[];
  const INF=[['🎧','O som',I.what],['👄','Como fazer',I.how],['🇧🇷','Comparando com o português',I.pt]].filter(x=>x[2]);
  const infoSeen=new Set(),exSeen=new Set();const needEx=Math.min(3,EX.length);
  const hue=i=>(i*53+160)%360;
  st.innerHTML=`<div class="step fx m2-lab">${fxKindBar(f,n)}
   <div class="sl-hero"><span class="sl-ic">🔬</span><div><small>Laboratório de sons</small><b>${esc(f.short||String(f.title||'').replace(/^Laborat[^:]*:\s*/,''))}</b></div><span class="sl-wave"><i></i><i></i><i></i><i></i><i></i></span></div>
   <div class="m2-wh"><p class="m2-lead" style="margin:0">Abra os 3 cartões e ouça os exemplos.</p><span class="m2-stars" id="m2lp">🎯 0/${INF.length+needEx}</span></div>
   <div class="m2-lt">${INF.map((x,i)=>`<div class="m2-ltc" data-i="${i}" style="--i:${i};--hue:${hue(i)}"><button type="button" class="m2-ltt"><span class="m2-lti">${x[0]}</span><b>${esc(x[1])}</b><i>＋</i></button><div class="m2-ltb"><p>${mk(x[2])}</p></div></div>`).join('')}</div>
   ${EX.length?`<div class="m2-h">🔊 Ouça os exemplos</div><div class="m2-exg">${EX.map((x,i)=>`<button type="button" class="m2-exc" data-i="${i}" style="--i:${i};--hue:${hue(i+3)}"><span class="m2-exw">${esc(x[0])}</span><i class="m2-exp">${esc(x[1]||'')}</i><small>${esc(x[2]||'')}</small>${x[3]?`<em>${mk(x[3])}</em>`:''}<span class="say2">${spk}</span></button>`).join('')}</div>`:''}
   ${PR.length?`<div class="m2-h">👂 Ouça a diferença</div><div class="m2-prs">${PR.map(p=>`<div class="m2-pr"><button type="button" class="m2-pw" data-w="${esc(p[0])}">🔊 ${esc(p[0])}</button><b>VS</b><button type="button" class="m2-pw" data-w="${esc(p[1])}">🔊 ${esc(p[1])}</button><small>${esc(p[2]||'')}</small></div>`).join('')}</div>`:''}
   ${f.tip?`<div class="fx-tip">💡 ${mk(f.tip)}</div>`:''}</div>`;
  const prog=()=>{const t=infoSeen.size+Math.min(exSeen.size,needEx),need=INF.length+needEx;
    st.querySelector('#m2lp').textContent=`🎯 ${t}/${need}`;
    if(t>=need){cta('Continuar',true,true)}};
  st.querySelectorAll('.m2-ltc').forEach(c=>c.querySelector('.m2-ltt').onclick=()=>{const first=!c.classList.contains('open');c.classList.toggle('open');sfx('pop');infoSeen.add(+c.dataset.i);if(first)burst(c.querySelector('.m2-lti'),['✨','💫']);prog()});
  st.querySelectorAll('.m2-exc').forEach(b=>b.onclick=()=>{const i=+b.dataset.i;b.classList.add('open');exSeen.add(i);sfx('pop');fxSay(EX[i][0]);prog()});
  st.querySelectorAll('.m2-pw').forEach(b=>b.onclick=()=>{sfx('pop');fxSay(b.dataset.w)});
  cta('Abra os cartões e ouça os exemplos',false);say(f.say||'Primeiro entenda o som, depois treine o ouvido.');
  P.fx.cta=()=>false;
};

/* ---------- Common Expressions (mesmo estilo das expressões coringa) ---------- */
FXR.cexp=function(f,st,n){
  const R=f.items;
  const g=Object.assign({},f,{items:R.map(x=>({t:'cexp',b:String(x.x).replace(/…/g,'').split(/\s+/).filter(Boolean).map(w=>[w]),ic:x.ic,pt:x.pt,ex:x.ex,note:x.use,cult:x.cult})),
    kicker:'💬 '+R.length+' expressões comuns',intro:f.intro,hint:'Toque em cada expressão: ouça e veja quando usar.',cta:'Descubra todas as expressões',
    tip:'Aprenda cada uma como um bloco: não traduza palavra por palavra.',say:'Os americanos dizem essas frases o tempo todo. Toque e ouça!'});
  FXR.xpr(g,st,n);
};

/* ---------- Situações novas (lúdico: verbos, coringa e comuns) ---------- */
const _cv=FXR.ctxv;
FXR.ctxv=function(f,st,n){
  if(!f.m2)return _cv.apply(this,arguments);
  const R=f.items;let ri=0;
  const KD={verbo:['⚡','Verbo'],coringa:['🃏','Expressão coringa'],comum:['💬','Expressão comum']};
  const draw=()=>{
    const it=R[ri],nb=it.ans.length,val=new Array(nb).fill(null);let checked=false,act=0,k=0;
    const chips=fxShuffle(it.opts),kd=KD[it.kind]||KD.verbo;
    const lines=it.lines.map((l,j)=>`<div class="m2-sb ${j%2?'r':'l'}"><span class="m2-sav" style="--h:${(j*70+200)%360}">${esc((l[0]||'?').slice(0,1))}</span><div class="m2-sbb">${l[0]?`<small>${esc(l[0])}</small>`:''}<p>${esc(l[1]).replace(/___/g,()=>`<button type="button" class="ctx-hole m2-hole" data-h="${k++}">&nbsp;</button>`)}</p></div></div>`).join('');
    st.innerHTML=`<div class="step fx m2-sit">${fxKindBar(f,n)}
     <div class="m2-sith k-${it.kind}"><span class="m2-sitic">${fxIcon(it.ic,52)}</span><div><small>SITUAÇÃO ${ri+1}/${R.length}</small><b>${esc(it.place)}</b></div><span class="m2-kind">${kd[0]} ${kd[1]}</span></div>
     <div class="m2-sitp"><button type="button" class="pill light" id="m2sp">🔊 Ouvir a cena</button><button type="button" class="pill light" id="m2ss">🐢 Devagar</button></div>
     <div class="m2-sitb">${lines}</div>
     <div class="m2-sitc">${chips.map(c=>`<button type="button" class="m2-chp" data-c="${esc(c)}">${esc(c)}</button>`).join('')}</div><div id="fb"></div></div>`;
    let ak=0;const FL2=it.lines.map(l=>[l[0]||null,l[1].replace(/___/g,()=>it.ans[ak++])]);
    const play=slow=>{clearTimeout(fxSeq.t);if(slow){let i=0;const go=()=>{if(!P||i>=FL2.length)return;fxSay(plain(FL2[i][1]),FL2[i][0],true);const ms=Math.max(2200,plain(FL2[i][1]).length*150+600);i++;fxSeq.t=setTimeout(go,ms)};go()}else fxSeq(FL2.map(l=>[l[0],l[1]]),0)};
    st.querySelector('#m2sp').onclick=()=>play(false);st.querySelector('#m2ss').onclick=()=>play(true);
    const holes=[...st.querySelectorAll('.m2-hole')],cs=[...st.querySelectorAll('.m2-chp')];
    const refresh=()=>{holes.forEach((h,i)=>{h.textContent=val[i]||' ';h.classList.toggle('filled',!!val[i]);h.classList.toggle('act',!checked&&i===act)});
      cs.forEach(c=>c.classList.toggle('used',val.includes(c.dataset.c)));
      const all=val.every(Boolean);cta(all?'Conferir':'Toque nas palavras para completar',all,true)};
    holes.forEach((h,i)=>h.onclick=()=>{if(checked)return;if(val[i]){val[i]=null;act=i;sfx('pop');refresh()}else{act=i;refresh()}});
    cs.forEach(c=>c.onclick=()=>{if(checked||c.classList.contains('used'))return;const w=c.dataset.c;let i=val[act]===null?act:val.indexOf(null);if(i<0)return;val[i]=w;act=val.indexOf(null);if(act<0)act=i;sfx('key');fxSay(w);refresh()});
    P.fx.cta=()=>{if(!checked){if(!val.every(Boolean))return true;checked=true;let good=0;
        holes.forEach((h,i)=>{const ok=val[i]===it.ans[i];if(ok)good++;h.classList.add(ok?'ok':'no');if(!ok)h.textContent=val[i]+' → '+it.ans[i]});
        cs.forEach(c=>c.disabled=true);const all=good===nb;if(all){P.score++;burst(st.querySelector('.m2-sitb'))}
        fxGrade(all,(it.pt?'**Tradução:** '+it.pt+' ':'')+(it.why||''),all?null:it.ans.join(' · '));
        clearTimeout(fxSeq.t);
        cta(ri<R.length-1?'Próxima situação ▶':'Continuar',true,true);return true}
      if(ri<R.length-1){ri++;draw();return true}return false};
    refresh();
  };
  draw();say(f.say||'Ouça a situação e complete com as palavras certas.');
};


/* =====================================================================
   v48: missão dos verbos, caça-sons, ponte lúdica, situações com ilustração
   ===================================================================== */
FX_KIND.vplay=FX_KIND.lplay='practice';FX_LABEL.vplay='Missão dos verbos';FX_LABEL.lplay='Caça-sons';
const _ftm2=window.fxTotal;
window.fxTotal=function(e){let t=_ftm2.apply(this,arguments);try{(e.fr||[]).forEach(f=>{if(f.k==='vplay')t+=(f.items||[]).length*4;if(f.k==='lplay')t+=(f.rounds||[]).length})}catch(x){}return t};
if(window.PogTTS&&PogTTS.episodeTexts){
  const o3=PogTTS.episodeTexts;
  PogTTS.episodeTexts=function(e){
    const out=o3(e),seen=new Set(out.map(x=>x.text+'|'+(x.speaker||'')));
    const add=t=>{t=T(t).replace(/\*\*/g,'').trim();const k=t+'|';if(t&&t.length<400&&!seen.has(k)){seen.add(k);out.push({text:t,speaker:null})}};
    (e.fr||[]).forEach(f=>{
      if(f.k==='vplay')(f.items||[]).forEach(it=>{add(it.v);add(it.ex[0]);(it.f||[]).forEach(x=>add(x[1]))});
      if(f.k==='lplay')(f.rounds||[]).forEach(r=>{add(r.say);(r.opts||[]).forEach(o=>add(Array.isArray(o)?o[1]:o))});
      if(f.k==='ctxv'&&f.m2)(f.items||[]).forEach(it=>{let k=0;it.lines.forEach(l=>add(l[1].replace(/___/g,()=>it.ans[k++])))});
    });
    return out;
  };
}

/* ---------- Missão dos verbos: prática guiada em 3 passos por verbo ---------- */
FXR.vplay=function(f,st,n){
  const V=f.items,N=V.length;let ti=0,score=0;
  const LK=['read','lead','need','feed','seed','heat','eat','meet','mean','beat','leave','live','love','lose','like','look','book','cook','took','take','make','wake','bake','talk','walk','work','word','fork','pack','park','pick','kick','sick','sit','set','get','let','bet','hit','hide','ride','rise','wise','wish','fish','dish','miss','kiss','mix','fix','fill','feel','heel','call','fall','tall','tell','sell','smell','spell','stay','play','pay','say','stop','shop','drop','hope','hop','cope','rope','turn','burn','learn','earn','hear','near','wear','tear','bear','pass','push','pull','call','cross','dress','press','guess','check','chat','cheat','chase','change','charge','choose','chose','listen','glisten','answer','enter','order','offer','visit','wait','weight','paint','point','print','plant','plan','pray','prey','show','slow','snow','sing','ring','sink','think','thank','drink','shrink','ask','mask','task','open','often','shake','share','shave','save','wave','have','hang','bang','sang','start','smart','chart','copy','cope','wrap','drip','rest','test','nest','best','board','hoard','score','store','shore','sort','short','sport','fly','try','cry','dry','buy','bay','guy','sleep','sweep','steep','sheep','swim','slim','skim','stir','star','stare','steer','stay','study','stud','repeat','retreat','repair','prepare','repay'];
  const lev=(a,b)=>{const m=[];for(let i=0;i<=a.length;i++){m[i]=[i];for(let j=1;j<=b.length;j++)m[i][j]=i?0:j}for(let i=1;i<=a.length;i++)for(let j=1;j<=b.length;j++)m[i][j]=Math.min(m[i-1][j]+1,m[i][j-1]+1,m[i-1][j-1]+(a[i-1]===b[j-1]?0:1));return m[a.length][b.length]};
  const look=(v,ban)=>{v=String(v).toLowerCase();if(/\s/.test(v))return null;let best=null,bd=9;LK.forEach(w=>{if(w===v||ban.includes(w)||w.length<2)return;const d=lev(v,w)+(w[0]===v[0]?-0.6:0);if(d<bd){bd=d;best=w}});return bd<=3.2?best:null};
  const thirdOf=w=>/(s|x|ch|sh|z|o)$/.test(w)?w+'es':/[^aeiou]y$/.test(w)?w.slice(0,-1)+'ies':w+'s';
  let tasks=[];const mk=()=>{const a=[];if(Array.isArray(f.plan))f.plan.forEach(p=>{if(V[p[0]]&&!(p[1]===2&&!third(V[p[0]])))a.push({v:p[0],s:p[1]})});else for(let s=0;s<4;s++)V.forEach((x,i)=>{if(s===2&&!third(x))return;a.push({v:i,s})});
    const okp=l=>l.every((t,i)=>!i||t.v!==l[i-1].v&&t.s!==l[i-1].s);
    let best=null;for(let k=0;k<400;k++){const c=fxShuffle(a.slice());if(okp(c)){best=c;break}if(!best)best=c}
    return best};
  const strip=s=>String(s).replace(/\*\*/g,'');
  const toks=s=>strip(s).split(/\s+/).filter(Boolean);
  const msgs=['Passo 1: leia a frase e escolha o verbo que completa.','Passo 2: monte a frase tocando as palavras na ordem.','Passo 3: com ele ou ela, o verbo muda! Qual forma é a certa?','Passo 4: ouça a frase e escolha o que ela significa.'];
  const hole=(s,w)=>{const t=toks(s),i=t.findIndex(x=>x.replace(/[^\p{L}']/gu,'').toLowerCase()===w.toLowerCase());return i<0?null:[t,i]};
  const FM=x=>x.vf||x.v,ES=!/^en/i.test(lang());
  const third=(it)=>{const s=strip((it.f&&it.f[1]&&it.f[1][1])||'');if(it.v3){const t=s.split(/\s+/);const i=t.findIndex(x=>x.replace(/[^\p{L}]/gu,'').toLowerCase()===it.v3.toLowerCase());return i<0?null:{t,i,w:t[i].replace(/[^\p{L}]/gu,'')}}const p=it.v.slice(0,Math.max(2,it.v.length-2)).toLowerCase();const t=s.split(/\s+/);const i=t.findIndex(x=>x.replace(/[^A-Za-z]/g,'').toLowerCase().startsWith(p));return i<0?null:{t,i,w:t[i].replace(/[^A-Za-z]/g,'')}};
  const hh=t=>t.map(x=>x==='___'?'<span class="m2-vph2">?</span>':esc(x)).join(' ');
  const draw=()=>{
    const T0=tasks[ti],vi=T0.v,step=T0.s,it=V[vi],ex=strip(it.ex[0]);let tries=0;P.answered=false;
    const head=`<div class="m2-vph"><div class="m2-vps" style="width:100%;gap:3px">${tasks.map((_,j)=>`<b class="${j<ti?'ok':j===ti?'on':''}" style="flex:1"></b>`).join('')}</div></div>
      <div class="m2-vpb"><span>🦫</span><p>${esc(msgs[step])}</p></div>`;
    let body='';
    if(step===0){
      const ho=hole(ex,FM(it))||[toks(ex),0];const t=ho[0].slice();t[ho[1]]='___';
      const lk=ES?null:look(it.v,V.map(x=>x.v.toLowerCase())),oth=fxShuffle(V.filter(x=>x!==it)).slice(0,lk?2:3),opts=fxShuffle([it].concat(oth).concat(lk?[{v:lk}]:[]));
      body=`<div class="m2-vpc"><div class="m2-vpi">${fxIcon(it.ic,96)}</div><div class="m2-vpt"><b>${hh(t)}</b></div></div>
        <div class="m2-vpo">${opts.map((o,i)=>`<button type="button" class="m2-vpk" data-v="${esc(FM(o))}"><b>${esc(FM(o))}</b></button>`).join('')}</div>`;
    }else if(step===1){
      const tk=toks(ex),sh=fxShuffle(tk.map((w,i)=>({w,i})));
      body=`<div class="m2-vpc"><div class="m2-vpi">${fxIcon(it.ic,96)}</div><small>${esc(it.ex[1])}</small><div class="m2-vpa" id="m2vpa"></div></div>
        <div class="m2-vpo wrap" id="m2vpb">${sh.map(o=>`<button type="button" class="m2-vpw" data-w="${esc(o.w)}">${esc(o.w)}</button>`).join('')}</div>`;
    }else if(step===2){
      const th=third(it);
      {
        const tt=th.t.slice();tt[th.i]='___';const base=it.v,ok=th.w;
        const lw=ES?null:look(base,[base.toLowerCase()]);const cand=it.d?[ok].concat(it.d):[ok,base,lw?thirdOf(lw):null,(()=>{const o=V.filter(x=>x!==it&&!/\s/.test(x.v));return o.length?thirdOf(o[0].v.toLowerCase()):null})(),thirdOf(base)!==ok?thirdOf(base):null];const opts=fxShuffle(cand.filter((x,i,a)=>x&&a.indexOf(x)===i).slice(0,4));
        body=`<div class="m2-vpc"><div class="m2-vpi">${fxIcon(it.ic,96)}</div><div class="m2-vpt"><b>${hh(tt)}</b></div><small>${esc((it.f[1]||[])[0]||'')} · ele/ela</small></div>
          <div class="m2-vpo">${opts.map(o=>`<button type="button" class="m2-vpk" data-v="${esc(o)}"><b>${esc(o)}</b></button>`).join('')}</div>`;
      }
    }
    if(step===3){
      const pool=[it.ex[1]].concat(V.filter(x=>x!==it).map(x=>x.ex[1])).filter((x,i,a)=>a.indexOf(x)===i).slice(0,4);
      body=`<div class="m2-vpc"><div class="m2-vpi">${fxIcon(it.ic,96)}</div><button type="button" class="pill light" id="m2vl">🔊 Ouvir a frase</button><small>O que ela significa?</small></div>
        <div class="m2-vpo col">${fxShuffle(pool).map(o=>`<button type="button" class="m2-vpk" data-v="${esc(o)}"><b>${esc(o)}</b></button>`).join('')}</div>`;
    }
    st.innerHTML=`<div class="step fx m2-vp">${fxKindBar(f,n)}<div class="m2-wh"><h2 class="fx-h">${esc(f.title||'Missão dos verbos')} <small>${ti+1}/${tasks.length}</small></h2><span class="m2-stars">⭐ ${score}</span></div>${head}${body}<div id="fb"></div></div>`;
    const done=(good,full)=>{
      P.answered=true;if(good){score++;P.score++}
      st.querySelector('.m2-stars').textContent='⭐ '+score;burst(st.querySelector('.m2-vpc'));sfx('key');
      fxSay(plain(full));
      cta(ti<tasks.length-1?'Próximo ▶':'Continuar',true,true);
    };
    if(step===0||step===2||step===3){
      const vl=st.querySelector('#m2vl');if(vl)vl.onclick=()=>fxSay(ex);
      st.querySelectorAll('.m2-vpk').forEach(b=>b.onclick=()=>{
        if(P.answered)return;const w=b.dataset.v;
        const right=step===0?FM(it):step===3?it.ex[1]:third(it).w;
        if(w.toLowerCase()!==right.toLowerCase()){tries++;b.disabled=true;b.classList.add('no');beep(false);
          fxGrade(false,tries>1?(step===0?'Dica: o verbo significa “'+it.pt+'”.':step===3?'Dica: toque em “Ouvir a frase” e pense em “'+it.pt+'”.':(it.h3||'Com he/she, o verbo ganha **-s** (ou **-es**).')):'Quase! Leia a frase de novo.',null);return}
        st.querySelectorAll('.m2-vpk').forEach(x=>{x.disabled=true;if(x===b)x.classList.add('ok')});
        const ph=st.querySelector('.m2-vph2');if(ph){ph.textContent=right;ph.classList.add('ok')}
        fxGrade(true,step===0?'**'+it.v+'** = '+it.pt+'.':step===3?'**'+ex+'** = '+it.ex[1]:(it.note||''),null);
        done(tries===0,step===0||step===3?ex:strip(it.f[1][1]));
      });
    }else{
      const tk=toks(ex);let pos=0,mist=0;const area=st.querySelector('#m2vpa');
      st.querySelectorAll('.m2-vpw').forEach(b=>b.onclick=()=>{
        if(P.answered||b.classList.contains('used'))return;
        if(b.dataset.w===tk[pos]){b.classList.add('used');const sp=document.createElement('span');sp.className='m2-vpx';sp.textContent=b.dataset.w;area.appendChild(sp);sfx('pop');pos++;
          if(pos>=tk.length){fxGrade(true,'Isso! **'+ex+'**',null);done(mist===0,ex)}}
        else{mist++;b.classList.remove('shake');void b.offsetWidth;b.classList.add('shake');beep(false);
          if(mist>=2){const t=st.querySelector(`.m2-vpw:not(.used)[data-w="${CSS.escape(tk[pos])}"]`);if(t)t.classList.add('hint')}}
      });
    }
    P.answered=false;cta('Faça o passo para continuar',false);
  };
  P.fx.cta=()=>{
    if(!P.answered)return true;
    if(ti>=tasks.length-1)return false;
    ti++;draw();return true;
  };
  tasks=mk();draw();say(f.say||'Missão dos verbos: 16 passos com os verbos misturados. Eu ajudo você!');
};

/* ---------- Caça-sons: listening lúdico ---------- */
FXR.lplay=function(f,st,n){
  const R=f.rounds,N=R.length;let ri=0,score=0,streak=0,best=0;
  const draw=()=>{
    const r=R[ri];let tries=0;P.answered=false;
    st.innerHTML=`<div class="step fx m2-lp">${fxKindBar(f,n)}
     <div class="m2-wh"><h2 class="fx-h">${esc(f.title||'Caça-sons')} <small>${ri+1}/${N}</small></h2><span class="m2-stars" id="m2lps">⭐ ${score}${streak>1?' · 🔥'+streak:''}</span></div>
     <div class="m2-lpt"><i style="width:${ri/N*100}%"></i></div>
     <div class="m2-lpq"><button type="button" class="m2-lpb" id="m2lb" aria-label="Ouvir"><span class="m2-lw"><i></i><i></i><i></i><i></i><i></i><i></i><i></i></span><b>Toque para ouvir</b></button><button type="button" class="pill light" id="m2ls">🐢 Devagar</button></div>
     <p class="m2-lead" style="text-align:center;margin:8px 0 12px">${r.t==='p'?'Ouça e toque na figura da palavra.':'Ouça e toque na palavra que você escutou.'}</p>
     <div class="m2-lpo ${r.t==='p'?'pic':''}">${r.opts.map((o,i)=>r.t==='p'?`<button type="button" class="m2-lpc" data-i="${i}" style="--i:${i}"><span>${fxIcon(o[0],72)}</span></button>`:`<button type="button" class="m2-lpc txt" data-i="${i}" style="--i:${i}"><b>${esc(o)}</b></button>`).join('')}</div>
     <div id="fb"></div></div>`;
    const wave=st.querySelector('.m2-lw');
    const play=slow=>{wave.classList.add('on');fxSay(r.say,null,!!slow);clearTimeout(play.t);play.t=setTimeout(()=>wave.classList.remove('on'),1500)};
    st.querySelector('#m2lb').onclick=()=>play(false);st.querySelector('#m2ls').onclick=()=>play(true);setTimeout(()=>play(false),450);
    st.querySelectorAll('.m2-lpc').forEach(b=>b.onclick=()=>{
      if(P.answered)return;const i=+b.dataset.i;
      if(i!==r.a){tries++;streak=0;b.disabled=true;b.classList.add('no');beep(false);st.querySelector('#m2lps').textContent='⭐ '+score;
        fxGrade(false,tries>1?'Ouça de novo, devagar. Preste atenção no começo da palavra.':'Quase! Toque em “Ouvir” e escute com calma.',null);return}
      P.answered=true;st.querySelectorAll('.m2-lpc').forEach((x,j)=>{x.disabled=true;if(j===r.a)x.classList.add('ok')});
      if(tries===0){score++;streak++;best=Math.max(best,streak);P.score++}else streak=0;
      st.querySelector('#m2lps').textContent='⭐ '+score+(streak>1?' · 🔥'+streak:'');burst(b);sfx('key');
      const word=r.t==='p'?r.opts[r.a][1]:r.opts[r.a];
      fxGrade(true,r.t==='p'?'**'+word+'** = '+(r.pt||'')+'.':(r.why||'Isso mesmo: **'+word+'**.'),null);
      setTimeout(()=>fxSay(r.say),250);
      cta(ri<N-1?'Próximo som ▶':'Continuar',true,true);
    });
    cta('Ouça e escolha',false);
  };
  P.fx.cta=()=>{if(P.answered&&ri<N-1){ri++;draw();return true}return false};
  draw();say(f.say||'Abra bem os ouvidos! Ouça e toque na resposta.');
};

/* ---------- Ponte do Poggie: mais lúdica (trilha, estrelas, combo, rodadas de escuta) ---------- */
const _pb2=FXR.pbridge;
FXR.pbridge=function(f,st,n){
  _pb2(f,st,n);
  if(!is2())return;
  const N=f.rounds.length;
  const deco=()=>{
    const step=st.querySelector('.fx-pg');if(!step||step.dataset.m2d===String(st.querySelector('.fx-h small')&&st.querySelector('.fx-h small').textContent))return;
    const sm=st.querySelector('.fx-h small');const cur=sm?parseInt(sm.textContent,10)-1:0;step.dataset.m2d=sm?sm.textContent:'';
    const h=step.querySelector('.fx-h');
    if(!step.querySelector('.m2-trail'))h.insertAdjacentHTML('afterend',`<div class="m2-trail">${Array.from({length:N},(_,j)=>`<span class="${j<cur?'ok':j===cur?'on':''}">${j<cur?'⭐':j===cur?'🦫':j+1}</span>`).join('<i></i>')}</div><div class="m2-combo" id="m2cb"></div>`);
    const listen=cur%2===1;const ask=step.querySelector('.pgx-ask');
    if(listen&&ask&&!ask.dataset.l){ask.dataset.l=1;const pt=ask.querySelector('b').textContent;ask.classList.add('listen');
      ask.innerHTML=`<span>Rodada de escuta · ouça o Poggie</span><b>🎧 Toque para ouvir e monte a ponte</b><div class="m2-lbtn"><button type="button" class="pill light" id="m2pl">🔊 Ouvir</button><button type="button" class="pill light" id="m2ps">🐢 Devagar</button><button type="button" class="pill light" id="m2pt">💡 Dica</button></div><em id="m2pe" hidden>${pt}</em>`;
      const r=f.rounds[cur];
      ask.querySelector('#m2pl').onclick=()=>{try{PGX.FX_SAY(r.t,'Poggie')}catch(e){fxSay(r.t)}};
      ask.querySelector('#m2ps').onclick=()=>{try{PGX.FX_SAY(r.t,'Poggie',true)}catch(e){fxSay(r.t,null,true)}};
      ask.querySelector('#m2pt').onclick=()=>{ask.querySelector('#m2pe').hidden=false};
      setTimeout(()=>{try{PGX.FX_SAY(r.t,'Poggie')}catch(e){}},600);
    }
    let streak=0;const cb=step.querySelector('#m2cb');
    step.querySelectorAll('.pgx-t').forEach(b=>b.addEventListener('click',()=>setTimeout(()=>{
      if(b.classList.contains('used')){streak++;burst(b,['⭐','✨']);if(streak>=2){cb.textContent='🔥 combo x'+streak;cb.classList.remove('pop');void cb.offsetWidth;cb.classList.add('pop')}}
      else if(b.classList.contains('shake')){streak=0;cb.textContent=''}
    },30)));
  };
  deco();
  if(st._pgm2)st._pgm2.disconnect();
  st._pgm2=new MutationObserver(deco);st._pgm2.observe(st,{childList:true,subtree:false});
};

/* ---------- Situações novas: ilustração por situação ---------- */
const _cv2=FXR.ctxv;
FXR.ctxv=function(f,st,n){
  _cv2.apply(this,arguments);
  if(!f.m2)return;
  const decorate=()=>{
    const sp=st.querySelector('.m2-sit');if(!sp)return;
    const sm=sp.querySelector('.m2-sith small');const i=sm?parseInt(sm.textContent.replace(/\D+/,''),10)-1:0;const it=f.items[i];
    if(!it||!it.rs||sp.querySelector('.m2-ill'))return;
    let svg='';try{svg=(window.AZ&&AZ.svg)?AZ.svg(it.rs):''}catch(e){}
    const art=(it.art||[]).slice(0,3).map((e,j)=>`<span class="m2-ae a${j}">${e}</span>`).join('');
    sp.querySelector('.m2-sith').insertAdjacentHTML('afterend',`<div class="m2-ill"><div class="m2-ibg">${svg}</div><div class="m2-art">${art}</div><span class="m2-ipl">${esc(it.place)}</span></div>`);
  };
  decorate();
  if(st._cvo)st._cvo.disconnect();
  st._cvo=new MutationObserver(decorate);st._cvo.observe(st,{childList:true});
};


/* ---------- v49: mochila do episódio anterior (revisão lúdica) ---------- */
FXR.review=function(f,st,n){
  const bag=f.bag||[];const seen=new Set();let stars=0;
  st.innerHTML=`<div class="step fx m2-rv m2-bagw">${fxKindBar(f,n)}
   <div class="m2-rvh"><span class="m2-rvi">🎒</span><div><small>MOCHILA DO EPISÓDIO ANTERIOR</small><h2 class="fx-h">${esc(f.prev)}</h2>${f.work?`<p>🎭 ${esc(f.work)}</p>`:''}</div><span class="m2-stars" id="m2bs">🎒 0/${bag.length}</span></div>
   <div class="m2-vpb"><span>🦫</span><p>${esc(f.lead||'Abra cada bolso da mochila e relembre o que você aprendeu!')}</p></div>
   <div class="m2-bagrow">${bag.map((t,i)=>`<button type="button" class="m2-bt c${i%5}" data-i="${i}" style="--i:${i}"><span class="m2-bti">${t.ic}</span><b>${esc(t.l)}</b><small>${t.items.length}</small><i class="m2-btk">✓</i></button>`).join('')}</div>
   <div class="m2-bagopen" id="m2bo"><p class="m2-bagh">👆 Toque num bolso para abrir</p></div>
   ${f.next?`<div class="fx-tip">🎯 ${mk(f.next)}</div>`:''}</div>`;
  st.querySelectorAll('.m2-rl .fx-vr').forEach(b=>b.onclick=()=>{sfx('pop');fxSay(b.dataset.s)});
  const box=st.querySelector('#m2bo');
  st.querySelectorAll('.m2-bt').forEach(b=>b.onclick=()=>{
    const i=+b.dataset.i,t=bag[i];sfx('pop');
    st.querySelectorAll('.m2-bt').forEach(x=>x.classList.toggle('cur',x===b));
    b.classList.add('open');
    box.innerHTML=`<p class="m2-bagh">${t.ic} ${esc(t.l)}</p><div class="m2-bagit">${t.items.map((it,j)=>`<button type="button" class="m2-bi" style="--j:${j}" data-s="${esc(it.s||it.t)}"><span>${it.ic?fxIcon(it.ic,34):''}</span><b>${esc(it.t)}</b>${it.pt?`<small>${esc(it.pt)}</small>`:''}</button>`).join('')}</div>`;
    box.querySelectorAll('.m2-bi').forEach(x=>x.onclick=()=>{sfx('pop');fxSay(x.dataset.s)});
    if(!seen.has(i)){seen.add(i);burst(b,['⭐','✨','🎒']);st.querySelector('#m2bs').textContent='🎒 '+seen.size+'/'+bag.length;
      if(seen.size>=bag.length){sfx('tada');try{confetti(40)}catch(e){}cta('Testar o que lembro',true,true)}}
    setTimeout(()=>fxSay(t.say||t.items.map(x=>x.s||x.t).slice(0,3).join('. ')),200);
  });
  cta('Abra os bolsos da mochila',bag.length===0,false);say(f.say||'Bora abrir a mochila e relembrar o episódio anterior!');
};

/* ---------- v49: "Sua vez" com ilustração ---------- */
const _pr49=FXR.produce;
FXR.produce=function(f,st,n){
  _pr49.apply(this,arguments);
  if(!is2())return;
  try{
    const step=st.querySelector('.step'),h=step&&step.querySelector('.fx-h');if(!h||step.querySelector('.m2-ill'))return;
    const rd=(P.e.fr||[]).find(x=>x.k==='read');
    const art=(f.art||(rd&&rd.props)||['💬','🙂','✨']).slice(0,3).map((e,j)=>`<span class="m2-ae a${j}">${typeof fxIcon==="function"&&String(e).startsWith("flag:")?fxIcon(e,34):e}</span>`).join('');
    let svg='';try{svg=AZ.svg(f.rs||P.e.rs)}catch(e){}
    let pg='';try{pg=poggie({scarf:(P.c&&P.c.scarf)||'#FFE58A'})}catch(e){}
    h.insertAdjacentHTML('afterend',`<div class="m2-ill m2-yt"><div class="m2-ibg">${svg}</div><div class="m2-art">${art}</div><span class="m2-ipg">${pg}</span><span class="m2-yb">Sua vez! 🎤</span></div>`);
  }catch(e){console.warn('yt',e)}
};

/* ---------- v49: fechamento do episódio ---------- */
const _wr49=FXR.wrap;
FXR.wrap=function(f,st,n){
  _wr49.apply(this,arguments);
  if(!is2())return;
  try{
    const step=st.querySelector('.step'),h=step&&step.querySelector('.fx-h');if(!step||!h)return;
    step.classList.add('m2-wrap');
    const fr=P.e.fr||[],g=k=>fr.find(x=>x.k===k)||{};
    const rows=[['🔤','Palavras',(g('words').items||[]).map(w=>w[1])],['🏃','Verbos',(g('verbs').items||[]).map(v=>v.ic)],['🃏','Coringas',(g('xpr').items||[]).map(i=>i.ic)],['💬','Expressões',(g('cexp').items||[]).map(i=>i.ic)],['🎧','Sons',['🔬','👂']]];
    let pg='';try{pg=poggie({scarf:(P.c&&P.c.scarf)||'#FFE58A'})}catch(e){}
    const sc=Math.max(0,P.score||0);
    h.insertAdjacentHTML('beforebegin',`<div class="m2-fin"><div class="m2-fin-sky"><span class="m2-fs s0">✨</span><span class="m2-fs s1">⭐</span><span class="m2-fs s2">🎉</span><span class="m2-fs s3">✨</span><span class="m2-fs s4">🎊</span></div>
      <div class="m2-fin-pg">${pg}</div>
      <div class="m2-fin-t"><div class="m2-medal">🏅</div><small>EPISÓDIO CONCLUÍDO</small><h2>${esc(P.e.t)}</h2><p>⭐ ${sc} acertos de primeira · 🎒 mochila cheia</p></div>
      <div class="m2-fin-g">${rows.map((r,i)=>`<button type="button" class="m2-fg c${i}" style="--i:${i}" data-i="${i}"><span class="m2-fgi">${r[0]}</span><b>${r[1]}</b><span class="m2-fge">${r[2].slice(0,6).map(e=>fxIcon(e,22)).join('')}</span></button>`).join('')}</div></div>
      <div class="m2-bagh2">Frases para levar</div>`);
    step.querySelectorAll('.m2-fg').forEach(b=>b.onclick=()=>{sfx('pop');burst(b,['⭐','✨'])});
    setTimeout(()=>{try{confetti(70)}catch(e){}},300);
  }catch(e){console.warn('wrap49',e)}
};

/* textos de áudio extras (bolsos da mochila) */
if(window.PogTTS&&PogTTS.episodeTexts){
  const o49=PogTTS.episodeTexts;
  PogTTS.episodeTexts=function(e){
    const out=o49(e),seen=new Set(out.map(x=>x.text+'|'+(x.speaker||'')));
    (e.fr||[]).forEach(f=>{if(f.k==='review')(f.bag||[]).forEach(t=>t.items.forEach(it=>{const x=T(it.s||it.t).trim();if(x&&x.length<200&&!seen.has(x+'|')){seen.add(x+'|');out.push({text:x,speaker:null})}}))});
    return out;
  };
}

/* ---------- v82: Trem da frase (estrutura da frase, 5 passos) ---------- */
FX_KIND.sbuild='practice';FX_LABEL.sbuild='Trem da frase';
FXR.sbuild=function(f,st,n){
  const R=f.rounds,N=R.length;let ri=0,score=0;
  const COL=['#E0499D','#7C4DFF','#12B3A8','#FF8A3D','#2F80ED'];
  const draw=()=>{
    const r=R[ri],bl=r.b;let pos=0,mist=0;P.answered=false;
    const sh=fxShuffle(bl.map((b,i)=>({t:b[0],i})).concat((r.x||[]).map((x,k)=>({t:x,i:-1-k}))));
    st.innerHTML=`<div class="step fx m2-sb5">${fxKindBar(f,n)}
     <div class="m2-wh"><h2 class="fx-h">${esc(f.title||'Trem da frase')} <small>${ri+1}/${N}</small></h2><span class="m2-stars">⭐ ${score}</span></div>
     <div class="m2-vpb"><span>🦫</span><p>${esc(r.tip||'Monte o trem na ordem certa: cada vagão tem uma função!')}</p></div>
     <div class="m2-train"><span class="m2-loco">🚂</span>${bl.map((b,i)=>`<div class="m2-car" data-i="${i}" style="--c:${COL[i%5]}"><small>${esc(b[1])}</small><b>&nbsp;</b></div>`).join('')}</div>
     <small class="m2-sbpt">${esc(r.pt)}</small>
     <div class="m2-vpo wrap">${sh.map(o=>`<button type="button" class="m2-vpw m2-tblk" data-i="${o.i}" style="--c:${o.i<0?'#7b8498':COL[o.i%5]}">${esc(o.t)}</button>`).join('')}</div><div id="fb"></div></div>`;
    const cars=[...st.querySelectorAll('.m2-car')];
    st.querySelectorAll('.m2-tblk').forEach(b=>b.onclick=()=>{
      if(P.answered||b.classList.contains('used'))return;
      if(+b.dataset.i===pos){
        b.classList.add('used');const c=cars[pos];c.classList.add('on');c.querySelector('b').textContent=bl[pos][0];sfx('pop');fxSay(bl[pos][0]);pos++;
        if(pos>=bl.length){
          P.answered=true;const full=bl.map(x=>x[0]).join(' ')+(r.end||'.');
          if(mist===0){score++;P.score++}
          st.querySelector('.m2-stars').textContent='⭐ '+score;st.querySelector('.m2-train').classList.add('go');burst(st.querySelector('.m2-train'));sfx('key');
          fxGrade(true,'Trem completo! **'+full+'**',null);setTimeout(()=>fxSay(full),500);
          cta(ri<N-1?'Próximo trem ▶':'Continuar',true,true);
        }
      }else{
        mist++;b.classList.remove('shake');void b.offsetWidth;b.classList.add('shake');beep(false);
        if(mist>=2){const t=st.querySelector(`.m2-tblk:not(.used)[data-i="${pos}"]`);if(t)t.classList.add('hint')}
        const c=cars[pos];if(c){c.classList.add('ask');setTimeout(()=>c.classList.remove('ask'),700)}
      }
    });
    cta('Monte o trem para continuar',false);
  };
  P.fx.cta=()=>{if(!P.answered)return true;if(ri<N-1){ri++;draw();return true}return false};
  draw();say(f.say||'Trem da frase: cada vagão tem uma função. Quem? Faz o quê? Onde? Quando? Monte na ordem!');
};
(function(){const o=window.fxTotal;window.fxTotal=function(e){let t=o.apply(this,arguments);try{(e.fr||[]).forEach(f=>{if(f.k==='sbuild')t+=(f.rounds||[]).length})}catch(x){}return t}})();

/* ---------- v82: "Sua vez" com trilha de estrelas ---------- */
const _pr82=FXR.produce;
FXR.produce=function(f,st,n){
  _pr82.apply(this,arguments);
  try{
    const step=st.querySelector('.step'),ul=step&&step.querySelector('.rw-goals');
    if(!step||!ul||step.querySelector('.yt-game'))return;
    const total=ul.children.length;if(!total)return;
    const gm=document.createElement('div');gm.className='yt-game';
    gm.innerHTML=`<div class="yt-track"><span class="yt-line"></span><span class="yt-fill"></span>${[...Array(total)].map((_,i)=>`<span class="yt-st" data-i="${i}" style="left:${(i+1)/(total+1)*100}%">⭐</span>`).join('')}<span class="yt-fin">🏆</span><span class="yt-pg">🦫</span></div><p class="yt-msg">Escreva ou fale: cada objetivo acende uma estrela!</p>`;
    const anchor=step.querySelector('.rw-steps')||step.querySelector('.rw-sit');
    if(anchor){anchor.classList.add('yt-hide');anchor.after(gm)}else step.prepend(gm);
    let last=0,won=false;
    const MS=['Escreva ou fale: cada objetivo acende uma estrela!','Boa! A primeira estrela acendeu!','Ótimo! Continue, falta pouco!','Quase lá! Mais uma estrela!'];
    const upd=()=>{
      const c=ul.querySelectorAll('li.done').length;
      gm.querySelector('.yt-fill').style.width=(c/(total+1)*100)+'%';
      gm.querySelector('.yt-pg').style.left=(c/(total+1)*100)+'%';
      gm.querySelectorAll('.yt-st').forEach((x,i)=>x.classList.toggle('lit',i<c));
      if(c>last){sfx('key');burst(gm.querySelector('.yt-track'),['⭐','✨'])}
      last=c;
      gm.querySelector('.yt-msg').textContent=c>=total?'🏆 Missão cumprida! Veja o modelo e compare.':(MS[Math.min(c,MS.length-1)]);
      if(c>=total&&!won){won=true;gm.classList.add('won');sfx('tada');try{confetti(50)}catch(e){}}
    };
    new MutationObserver(upd).observe(ul,{attributes:true,subtree:true,attributeFilter:['class']});
    upd();
  }catch(e){console.warn('yt82',e)}
};

})();

/* ---------- v93: barra verde (CTA) some ao trocar de quadro ---------- */
(function(){
  const FOOT={off:false};
  const live=()=>typeof P!=='undefined'&&P&&P.e&&P.e.fr&&document.querySelector('#pcta');
  FOOT.upd=function(){
    try{
      if(!live())return;
      const b=document.querySelector('#pcta'),body=document.querySelector('#pbody');if(!body)return;
      const isDone=P.steps&&P.steps[P.i]==='done';
      const atB=body.scrollHeight-body.scrollTop-body.clientHeight<56;
      const show=isDone||(!b.disabled&&(FOOT.off||atB));
      b.classList.toggle('foot-hid',!show);
    }catch(e){}
  };
  const _cta=window.cta;
  if(typeof _cta==='function')window.cta=function(l,en){if(!en)FOOT.off=true;const r=_cta.apply(this,arguments);FOOT.upd();return r};
  const _render=window.render;
  if(typeof _render==='function')window.render=function(){
    FOOT.off=false;
    try{const b=document.querySelector('#pcta');if(b&&P&&P.e&&P.e.fr&&P.steps[P.i]!=='done')b.classList.add('foot-hid')}catch(e){}
    const r=_render.apply(this,arguments);
    FOOT.upd();setTimeout(FOOT.upd,250);setTimeout(FOOT.upd,900);
    return r;
  };
  document.addEventListener('scroll',e=>{if(e.target&&e.target.id==='pbody')FOOT.upd()},true);
  window.addEventListener('resize',FOOT.upd);
  new MutationObserver(()=>{if(FOOT.t)return;FOOT.t=setTimeout(()=>{FOOT.t=0;FOOT.upd()},80)}).observe(document.body,{childList:true,subtree:true});
  window.FOOT=FOOT;
})();
