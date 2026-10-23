/* Pogglot · quadros completos do modelo "padrão do dia" (episódios pilot:1):
   pgscene (diálogo com personagens), pgsheet (várias perguntas de uma vez), pgrule (padrão com ilustração),
   pgspeak (fale, todas as frases juntas) e o cartão grande do próximo episódio. */
(function(){
'use strict';
if(typeof FXR==='undefined'||typeof FX_KIND==='undefined'||!window.PogStage)return;
const S=window.PogStage;
const H=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const q=(s,r)=>(r||document).querySelector(s);
const qa=(s,r)=>[...(r||document).querySelectorAll(s)];
const tts=(t,slow)=>{try{fxSay(String(t),null,slow)}catch(e){}};
const MK=s=>(typeof mk==='function'?mk(s):H(s));
const face=id=>window.PogChars?PogChars.face(id):'';
const spkr=()=>(typeof spk!=='undefined'?spk:'🔊');

/* ---------------- diálogo ---------------- */
FX_KIND.pgscene='story';FX_LABEL.pgscene='A cena';
FXR.pgscene=function(f,st,n){
  const lines=f.lines||[],sp=f.speakers||{},cast=f.cast||{};
  const col=nm=>(cast[nm]&&cast[nm][1])||'#2b6cb0';
  const clean=t=>String(t).replace(/\*\*/g,'');
  const hl=t=>H(t).replace(/\*\*(.+?)\*\*/g,'<mark>$1</mark>');
  const ln=(l,i)=>`<button type="button" class="ps-ln ${i%2?'r':''}" data-i="${i}" style="--c:${col(l[0])}"><span class="ps-face">${face(sp[l[0]])||`<b>${(cast[l[0]]||[''])[0]}</b>`}</span><div><b class="who">${H(l[0])}</b><span class="en">${hl(l[1])}</span><small class="pt">${H(l[2]||'')}</small></div><i aria-hidden="true">🔊</i></button>`;
  st.innerHTML=`<div class="step fx ps-sc">${fxKindBar(f,n)}${f.title?`<h2 class="fx-h ps-sc-t">${H(f.title)}</h2>`:''}${S.stage({rs:f.rs,chars:f.chars,h:'scene'})}
  <div class="ps-sc-main"><div class="ps-sc-bar"><button type="button" class="ps-btn main" id="pgall">▶ Ouvir a cena</button><button type="button" class="ps-btn" id="pgslow">🐢 Devagar</button><button type="button" class="ps-btn tog" id="pgtr" aria-pressed="true">🇧🇷 Tradução</button></div>
  <div class="ps-lines" id="pgl">${lines.map(ln).join('')}</div></div></div>`;
  const wrap=q('.ps-sc',st),box=q('#pgl',st);let timer=null,run=0;
  const alive=()=>!!(P&&P.steps[P.i]==='fx'+n&&document.body.contains(wrap));
  const talk=(who,on)=>{const id=sp[who];qa('.ps-c',st).forEach(c=>c.classList.toggle('talk',!!on&&c.dataset.c===id))};
  const mark=i=>{qa('.ps-ln',box).forEach((b,j)=>b.classList.toggle('on',j===i));const b=qa('.ps-ln',box)[i];if(b&&b.scrollIntoView)b.scrollIntoView({block:'nearest',behavior:'smooth'})};
  const stop=()=>{clearTimeout(timer);run++;talk('',false);qa('.ps-ln',box).forEach(b=>b.classList.remove('on'))};
  const play=slow=>{stop();const my=run;let i=0;const step=()=>{if(my!==run||!alive())return;if(i>=lines.length){talk('',false);qa('.ps-ln',box).forEach(b=>b.classList.remove('on'));return}
    const l=lines[i];mark(i);talk(l[0],true);tts(clean(l[1]),slow);const ms=Math.max(1500,clean(l[1]).length*(slow?140:85)+500);i++;timer=setTimeout(step,ms)};step()};
  q('#pgall',st).onclick=()=>play(false);q('#pgslow',st).onclick=()=>play(true);
  q('#pgtr',st).onclick=ev=>{const b=ev.currentTarget,on=b.getAttribute('aria-pressed')!=='true';b.setAttribute('aria-pressed',on);wrap.classList.toggle('no-pt',!on)};
  qa('.ps-ln',box).forEach(b=>b.onclick=()=>{stop();const l=lines[+b.dataset.i];mark(+b.dataset.i);talk(l[0],true);tts(clean(l[1]));setTimeout(()=>talk('',false),1600)});
  const watch=setInterval(()=>{if(!alive()){clearInterval(watch);stop()}},300);
  P.fx.cta=null;cta('Continuar',true,true);
  setTimeout(()=>{if(P&&P.steps[P.i]==='fx'+n)play(false)},500);
  say(f.say||'Ouça a cena e leia junto.');
};

/* ---------------- várias perguntas de uma vez ---------------- */
FX_KIND.pgsheet='practice';FX_LABEL.pgsheet='Pratique';
const optHTML=o=>Array.isArray(o)?`<em>${o[0]}</em><span>${H(o[1])}</span>`:`<span>${H(o)}</span>`;
function cardHTML(it,i){
  const blank='<span class="ps-blank">&nbsp;</span>';
  const text=it.text?H(it.text).replace(/___/g,blank).replace(/\*\*(.+?)\*\*/g,'<mark>$1</mark>'):'';
  return `<div class="ps-q${it.pic?' pic':''}" data-i="${i}">
    ${it.fig?`<button type="button" class="ps-fig" data-say="${H(it.say||'')}" aria-label="Ouvir"><span>${it.fig}</span><i>🔊</i></button>`:''}
    <div class="ps-q-b">
      ${it.tag?`<small class="ps-q-tag">${H(it.tag)}</small>`:''}
      ${text?`<div class="ps-q-t">${text}</div>`:''}
      ${it.ask?`<div class="ps-q-a">${H(it.ask)}${it.speak?` <button type="button" class="ps-mini" data-say="${H(it.speak)}" aria-label="Ouvir">🔊</button>`:''}</div>`:''}
      ${it.pt?`<small class="ps-q-pt">${H(it.pt)}</small>`:''}
      <div class="ps-opts">${(it.opts||[]).map((o,j)=>`<button type="button" class="ps-o" data-j="${j}">${optHTML(o)}</button>`).join('')}</div>
      <div class="ps-why" hidden></div>
    </div></div>`}
/* liga as perguntas de um contêiner; onAnswer(i, ok) é chamado a cada resposta */
function bindCards(root,items,onAnswer){
  const done=[];
  qa('.ps-fig,.ps-mini',root).forEach(b=>b.onclick=()=>tts(b.dataset.say));
  qa('.ps-q',root).forEach(c=>{const i=+c.dataset.i,it=items[i];
    qa('.ps-o',c).forEach(b=>b.onclick=()=>{
      if(done[i]!=null)return;const j=+b.dataset.j,ok=j===it.a;done[i]=ok;
      qa('.ps-o',c).forEach((x,k)=>{x.disabled=true;if(k===it.a)x.classList.add('ok');else if(k===j)x.classList.add('no')});
      c.classList.add(ok?'ok':'no');
      const o=it.opts[it.a],right=Array.isArray(o)?o[1]:o;
      const bl=q('.ps-blank',c);if(bl){bl.textContent=right;bl.classList.add('on')}
      const w=q('.ps-why',c);w.hidden=false;w.innerHTML=(ok?'✅ ':'❌ ')+MK(it.why||'');
      try{beep(ok)}catch(e){}
      tts(it.say||(it.text&&it.text.replace(/___/g,right))||'');
      onAnswer(i,ok)})});
}
S.cardHTML=cardHTML;S.bindCards=bindCards;
FXR.pgsheet=function(f,st,n){
  const items=f.items||[];const N=items.length;let answered=0,hits=0;
  st.innerHTML=`<div class="step fx ps-sh">${fxKindBar(f,n)}<div class="ps-sh-h"><h2 class="fx-h">${H(f.title||'Pratique')}</h2><span class="ps-count" id="pgcnt">0/${N}</span></div>
    <div class="ps-qs ${f.layout==='grid'?'grid':''}" id="pgqs">${items.map(cardHTML).join('')}</div></div>`;
  bindCards(st,items,(i,ok)=>{answered++;if(ok){hits++;P.score++}
    q('#pgcnt',st).textContent=answered+'/'+N;
    if(answered===N){cta('Continuar',true,true);say(hits===N?'Tudo certo! Muito bem!':'Bom trabalho! Revise o que errou.',hits===N?'happy':'')}
    else cta('Faltam '+(N-answered),false)});
  P.fx.cta=null;cta('Responda tudo: '+N+' perguntas',false);
  say(f.say||'Responda todas as perguntas.');
};


/* ---------------- expressões comuns e gírias ---------------- */
FX_KIND.pgexp='story';FX_LABEL.pgexp='Expressões e gírias';
FXR.pgexp=function(f,st,n){
  const items=f.items||[];
  const card=it=>`<article class="ps-exc"><div class="ps-exh"><span class="ps-ico big">${it.ic}</span><div class="ps-exm"><span class="ps-extag ${it.tag==='Gíria'?'g':it.tag==='Informal'?'i':'e'}">${H(it.tag)}</span>
    <button type="button" class="ps-exen" data-say="${H(it.en)}"><b>${H(it.en)}</b><i>🔊</i></button><span class="ps-expt">${H(it.pt)}</span></div></div>
    <p class="ps-exuse">${MK(it.use)}</p>
    <button type="button" class="ps-exex" data-say="${H(it.ex[0])}"><span>🗣️</span><div><b>${H(it.ex[0])}</b><small>${H(it.ex[1])}</small></div><i>🔊</i></button></article>`;
  st.innerHTML=`<div class="step fx ps-ex">${fxKindBar(f,n)}<div class="ps-sh-h"><h2 class="fx-h">${H(f.title||'Expressões e gírias')}</h2><span class="ps-count">${items.length} para levar</span></div>
    <p class="ps-note">${MK(f.intro||'Expressões e gírias não se traduzem palavra por palavra. Aprenda cada uma como um **bloco inteiro**.')}</p><div class="ps-exl">${items.map(card).join('')}</div></div>`;
  qa('[data-say]',st).forEach(b=>b.onclick=()=>tts(b.dataset.say));
  P.fx.cta=null;cta('Continuar',true,true);
  say(f.say||'Toque para ouvir cada expressão.');
};

/* ---------------- laboratório de sons (tudo em um quadro) ---------------- */
FX_KIND.pglab='practice';FX_LABEL.pglab='Laboratório de sons';
FXR.pglab=function(f,st,n){
  const I=f.intro||{},rounds=f.rounds||[];
  const sec=(ic,h,t)=>t?`<section class="ps-sec"><h3>${ic} ${H(h)}</h3><p class="ps-lp">${MK(t)}</p></section>`:'';
  const ex=(f.ex||[]).map(x=>`<button type="button" class="ps-lx" data-say="${H(x[0])}"><span class="ps-ico">🔊</span><div><b>${H(x[0])} <em>${H(x[1]||'')}</em></b><small>${H(x[2]||'')}${x[3]?' · '+H(x[3]):''}</small></div></button>`).join('');
  const pr=(f.pairs||[]).map(p=>`<div class="ps-pr"><div class="ps-pr-b"><button type="button" class="ps-btn" data-say="${H(p[0])}">🔊 ${H(p[0])}</button><span>×</span><button type="button" class="ps-btn" data-say="${H(p[1])}">🔊 ${H(p[1])}</button></div><small>${H(p[2]||'')}</small></div>`).join('');
  const ph=f.phrase?`<section class="ps-sec"><h3>🗣️ Frase de treino</h3><div class="ps-spt"><div><b>${H(f.phrase[0])}</b><small>${H(f.phrase[1]||'')}</small></div></div>
    <div class="ps-sp-tools"><button type="button" class="ps-btn main" id="pslph">🔊 Ouvir</button><button type="button" class="ps-btn" id="pslsl">🐢 Devagar</button></div><div id="pslmic" class="pv-host"></div></section>`:'';
  const items=rounds.map(r=>Object.assign({},r));
  st.innerHTML=`<div class="step fx ps-lab">${fxKindBar(f,n)}<h2 class="fx-h">${H(f.title||'Laboratório de sons')}</h2>
    ${sec('🎧','O som',I.what)}${sec('👄','Como fazer',I.how)}${sec('🇧🇷','Comparando com o português',I.pt)}
    ${ex?`<section class="ps-sec"><h3>🔊 Ouça os exemplos</h3><div class="ps-lxl">${ex}</div></section>`:''}
    ${pr?`<section class="ps-sec"><h3>↔️ Ouça a diferença</h3><div class="ps-prl">${pr}</div></section>`:''}
    ${ph}${f.tip?`<div class="ps-tip">💡 <span>${MK(f.tip)}</span></div>`:''}
    ${items.length?`<section class="ps-sec"><h3>👂 Treino do ouvido <span class="ps-count" id="pslc">0/${items.length}</span></h3><div class="ps-qs" id="pslq">${items.map(cardHTML).join('')}</div></section>`:''}</div>`;
  qa('[data-say]',st).forEach(b=>{if(!b.classList.contains('ps-fig')&&!b.classList.contains('ps-mini'))b.onclick=()=>tts(b.dataset.say)});
  if(f.phrase){const pl=String(f.phrase[0]);q('#pslph',st).onclick=()=>tts(pl);q('#pslsl',st).onclick=()=>tts(pl,true);if(window.PogVoice){try{PogVoice.mount(q('#pslmic',st),{target:pl,lang:(P.c&&P.c.tts)||'en-US'})}catch(e){}}}
  let k=0;if(items.length)bindCards(q('#pslq',st),items,(i,ok)=>{k++;if(ok)P.score++;q('#pslc',st).textContent=k+'/'+items.length});
  P.fx.cta=null;cta('Continuar',true,true);
  say(f.say||'Primeiro entenda o som, depois treine o ouvido.');
};

/* ---------------- padrão com ilustração ---------------- */
FX_KIND.pgrule='story';FX_LABEL.pgrule='O padrão';
const CC=['c0','c1','c2','c3'];
const chip=(t,c)=>`<span class="ps-chip ${CC[c%4]||'c0'}">${H(t)}</span>`;
FXR.pgrule=function(f,st,n){
  const R=f.rule||{};
  const hero=`<header class="ps-ru-hero"><div class="ps-ru-av">${R.who?S.stage({rs:f.rs,chars:[[R.who,50,0,1]],h:'avatar'}):''}</div><div class="ps-ru-ht"><small>Padrão do dia</small><h2>${H(R.head||'')}</h2><p>${H(R.sub||'')}</p></div>${R.say?`<button type="button" class="ps-line ps-ru-say" data-say="${H(R.say[0])}"><span>🔊</span><div><b>${H(R.say[0])}</b><small>${H(R.say[1]||'')}</small></div></button>`:''}</header>`;
  const form=(R.formula||[]).length?`<section class="ps-sec"><h3>🧩 Como funciona</h3>${R.formula.map(r=>`<div class="ps-form"><div class="ps-fg">${r.from.map((x,i)=>chip(x[0],x[1])).join('')}</div><span class="ps-arrow">➜</span><div class="ps-fg">${r.to.map(x=>chip(x[0],x[1])).join('')}</div>${r.say?`<button type="button" class="ps-mini" data-say="${H(r.say)}" aria-label="Ouvir">🔊</button>`:''}</div>${r.note?`<p class="ps-note">${MK(r.note)}</p>`:''}`).join('')}</section>`:'';
  const pairs=(R.pairs||[]).length?`<section class="ps-sec"><h3>${H(R.pairsHead||'👀 Um → vários')}</h3><div class="ps-pairs">${R.pairs.map(p=>`<button type="button" class="ps-pair" data-say="${H(p.a.replace(/<[^>]+>/g,''))}, ${H(p.b.replace(/<[^>]+>/g,''))}"><div class="ps-pc one"><span class="ps-big">${p.ico}</span><b>${p.a}</b><small>${H(p.pta||'')}</small></div><span class="ps-arrow">➜</span><div class="ps-pc many"><span class="ps-big">${p.ico.repeat(p.n||2)}</span><b>${p.b}</b><small>${H(p.ptb||'')}</small></div></button>`).join('')}</div></section>`:'';
  const uses=(R.uses||[]).length?`<section class="ps-sec"><h3>💬 ${H(R.usesHead||'Quando usar')}</h3><div class="ps-uses">${R.uses.map(u=>`<button type="button" class="ps-use" data-say="${H(u.en)}"><span class="ps-ico">${u.ico}</span><div>${u.tag?`<small class="ps-tag">${H(u.tag)}</small>`:''}<b>${H(u.en)}</b><small>${H(u.pt||'')}</small></div><i>🔊</i></button>`).join('')}</div></section>`:'';
  const rules=(R.rules||[]).length?`<section class="ps-sec"><h3>📌 Regra</h3><div class="ps-rules">${R.rules.map(r=>`<div class="ps-rule"><span class="ps-rt ${CC[r.c||0]}">${H(r.tag)}</span><p>${MK(r.text)}${r.ex?` <em>${H(r.ex)}</em>`:''}</p></div>`).join('')}</div></section>`:'';
  const tips=(R.tips||[]).length?`<section class="ps-sec ps-tipsec">${R.tips.map(t=>`<div class="ps-tip">💡 <span>${MK(t)}</span></div>`).join('')}</section>`:'';
  const Q=f.q;
  const qq=Q?`<section class="ps-sec ps-qq"><h3>🎯 Teste rápido</h3><div class="ps-q-a">${H(Q.q)}</div><div class="ps-opts">${Q.o.map((o,j)=>`<button type="button" class="ps-o" data-j="${j}"><span>${H(o)}</span></button>`).join('')}</div><div class="ps-why" hidden></div></section>`:'';
  st.innerHTML=`<div class="step fx ps-ru">${fxKindBar(f,n)}${hero}<div class="ps-ru-body">${form}${pairs}${uses}${rules}${tips}${qq}</div></div>`;
  qa('[data-say]',st).forEach(b=>b.onclick=()=>tts(b.dataset.say));
  let done=false;
  qa('.ps-qq .ps-o',st).forEach(b=>b.onclick=()=>{if(done)return;done=true;const j=+b.dataset.j,ok=j===Q.a;
    qa('.ps-qq .ps-o',st).forEach((x,k)=>{x.disabled=true;if(k===Q.a)x.classList.add('ok');else if(k===j)x.classList.add('no')});
    const w=q('.ps-qq .ps-why',st);w.hidden=false;w.innerHTML=(ok?'✅ ':'❌ ')+MK(Q.why||'');if(ok)P.score++;try{beep(ok)}catch(e){}
    cta('Continuar',true,true)});
  P.fx.cta=null;
  if(Q)cta('Responda o teste rápido',false);else cta('Continuar',true,true);
  say(f.say||'Veja o padrão com figuras e ouça os exemplos.');
};

/* ---------------- fale: todas as frases juntas ---------------- */
FX_KIND.pgspeak='speak';FX_LABEL.pgspeak='Fale';
FXR.pgspeak=function(f,st,n){
  const items=f.items||[],lang=(P.c&&P.c.tts)||'en-US',hasV=!!window.PogVoice,sc=[];
  st.innerHTML=`<div class="step fx ps-sp"><div class="ps-sh-h"><h2 class="fx-h">${H(f.title||'Sua vez de falar')}</h2><span class="ps-count" id="pgcnt">0/${items.length}</span></div>
  <div class="ps-spl">${items.map((it,i)=>`<div class="ps-spc" data-i="${i}"><div class="ps-spt"><span class="ps-face">${face(f.who)}</span><div><b>${H(it[0])}</b><small>${H(it[1]||'')}</small></div></div>
    <div class="ps-sp-tools"><button type="button" class="ps-btn main" data-a="p">🔊 Ouvir</button><button type="button" class="ps-btn" data-a="s">🐢 Devagar</button><button type="button" class="ps-btn rec" data-a="m">${hasV?'🎤 Falar':'✓ Já falei'}</button></div><div class="pv-host ps-mic" hidden></div><div class="ps-score" hidden></div></div>`).join('')}</div>
  ${hasV?'':'<p class="ps-note">Este navegador não reconhece voz: repita em voz alta e toque em “Já falei”.</p>'}</div>`;
  const count=()=>{q('#pgcnt',st).textContent=sc.filter(x=>x!=null).length+'/'+items.length};
  qa('.ps-spc',st).forEach(c=>{const i=+c.dataset.i,it=items[i];
    q('[data-a=p]',c).onclick=()=>tts(it[0]);q('[data-a=s]',c).onclick=()=>tts(it[0],true);
    q('[data-a=m]',c).onclick=ev=>{
      if(!hasV){sc[i]=-1;c.classList.add('ok');ev.currentTarget.disabled=true;count();return}
      const host=q('.ps-mic',c);host.hidden=false;if(host.dataset.m)return;host.dataset.m=1;
      PogVoice.mount(host,{target:it[0],lang,onDone:r=>{sc[i]=r.score;const s=q('.ps-score',c);s.hidden=false;s.textContent=r.score>=85?'🌟 Pronúncia ótima! '+r.score+'%':r.score>=65?'👍 Muito bem! '+r.score+'%':'🔁 Ouça o modelo e tente de novo. '+r.score+'%';c.classList.toggle('ok',r.score>=65);if(r.score>=65)P.score++;count()},onFail:()=>{}});
    }});
  P.fx.cta=null;cta('Continuar',true,true);
  say(f.say||'Ouça cada frase e repita em voz alta.');
};

/* ---------------- cartão do próximo episódio ---------------- */
function nextCard(){
  try{
    const L=(typeof EP!=='undefined'&&EP[P.cid])||[],ne=L[(P.idx||0)+1];if(!ne)return '';
    const st=ne.stage||{};let rs=st.rs;
    if(!rs&&window.AZ&&AZ.scn)rs=AZ.scn(ne,'scene');
    const art=(ne.fr||[]).find(x=>x.k==='cover');
    const w=(ne.a&&ne.a.w)||'';
    return `<div class="ps-next"><small class="ps-next-k">Próximo episódio · ${(P.idx||0)+2}</small>${S.stage({rs:rs||'street',chars:st.chars||[],h:'next'})}<div class="ps-next-t"><h3>${H(ne.t)}</h3><p>${H(ne.s||'')}</p>${w?`<span class="ps-next-obra">📖 ${H(w)}${ne.a&&ne.a.y?' · '+H(ne.a.y):''}</span>`:''}</div></div>`;
  }catch(e){return ''}
}
S.nextCard=nextCard;
})();
