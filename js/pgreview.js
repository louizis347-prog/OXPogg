/* Pogglot · Revisão do arco: botão ao lado de cada episódio piloto abre uma tela cheia com os padrões vistos
   (ilustrados), as palavras com figura e uma prática misturada de todos os episódios até ali. */
(function(){
'use strict';
const H=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const q=(s,r)=>(r||document).querySelector(s);
const qa=(s,r)=>[...(r||document).querySelectorAll(s)];
const tts=(t,slow)=>{try{fxSay(String(t),null,slow)}catch(e){}};
const shuffle=a=>{a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.random()*(i+1)|0;[a[i],a[j]]=[a[j],a[i]]}return a};

function collect(cid,idx){
  const L=(EP[cid]||[]).slice(0,idx+1).map((e,i)=>({e,i})).filter(x=>x.e.pilot);
  return L.map(({e,i})=>{
    const rule=(e.fr.find(f=>f.k==='pgrule')||{}).rule||{};
    const sheets=e.fr.filter(f=>f.k==='pgsheet');
    const words=[];sheets.forEach(f=>(f.items||[]).forEach(it=>{if(it.fig&&it.fig!=='🎧'&&it.say&&!words.some(w=>w.say===it.say))words.push({fig:it.fig,say:it.say,pt:it.ptWord||''})}));
    const items=[];sheets.forEach(f=>{if(f.review===false)return;(f.items||[]).forEach(it=>items.push(Object.assign({},it,{tag:e.pattern||e.t,ep:i})))});
    return {e,i,rule,words,items,stage:e.stage||{}};
  });
}

function open(cid,idx){
  if(typeof EP==='undefined'||!EP[cid])return;
  const data=collect(cid,idx);if(!data.length)return;
  const last=data[data.length-1];
  const old=document.getElementById('ps-rev');if(old)old.remove();
  const el=document.createElement('div');el.id='ps-rev';el.className='ps-rev';el.setAttribute('role','dialog');el.setAttribute('aria-label','Revisão');
  const S=window.PogStage;
  const patterns=data.map(d=>{const R=d.rule;return `<article class="ps-rv-card"><div class="ps-rv-av">${S.stage({rs:(d.stage.rs)||'street',chars:(d.stage.chars||[]).slice(0,2),h:'next'})}</div>
    <div class="ps-rv-ct"><small>Episódio ${d.i+1} · ${H((d.e.a&&d.e.a.w)||'')}</small><h3>${H(R.head||d.e.t)}</h3><p>${H(R.sub||d.e.s||'')}</p>
    ${(R.uses||[]).slice(0,2).map(u=>`<button type="button" class="ps-use" data-say="${H(u.en)}"><span class="ps-ico">${u.ico}</span><div><b>${H(u.en)}</b><small>${H(u.pt||'')}</small></div><i>🔊</i></button>`).join('')}
    ${(R.pairs||[]).slice(0,3).map(p=>`<button type="button" class="ps-pair mini" data-say="${H(p.a.replace(/<[^>]+>/g,''))}, ${H(p.b.replace(/<[^>]+>/g,''))}"><div class="ps-pc one"><span class="ps-big">${p.ico}</span><b>${p.a}</b></div><span class="ps-arrow">➜</span><div class="ps-pc many"><span class="ps-big">${p.ico.repeat(p.n||2)}</span><b>${p.b}</b></div></button>`).join('')}
    <button type="button" class="ps-btn" data-ep="${d.i}">↩ Rever o episódio</button></div></article>`}).join('');
  const words=[];data.forEach(d=>d.words.forEach(w=>{if(!words.some(x=>x.say===w.say))words.push(w)}));
  const pool=shuffle(data.flatMap(d=>d.items)).slice(0,Math.min(8,data.flatMap(d=>d.items).length));
  el.innerHTML=`<div class="ps-rv-top"><button type="button" class="ps-hbtn" id="pgrx" aria-label="Fechar">×</button><div><small>Revisão do arco</small><h2>Do episódio 1 ao ${last.i+1}</h2></div></div>
  <div class="ps-rv-body">
   <section class="ps-rv-hero">${S.stage({rs:last.stage.rs||'street',chars:last.stage.chars||[],h:'scene'})}<p>Você já viu <b>${data.length}</b> ${data.length>1?'padrões':'padrão'} e <b>${words.length}</b> palavras com figura. Rever é o que fixa!</p></section>
   <section><h3 class="ps-rv-h">📌 Padrões que você já viu</h3><div class="ps-rv-cards">${patterns}</div></section>
   <section><h3 class="ps-rv-h">🖼️ Palavras com figura <small>toque para ouvir</small></h3><div class="ps-rv-words">${words.map(w=>`<button type="button" class="ps-rv-w" data-say="${H(w.say)}"><span>${w.fig}</span><b>${H(w.say)}</b></button>`).join('')}</div></section>
   <section><h3 class="ps-rv-h">🎯 Pratique tudo <span class="ps-count" id="pgrvc">0/${pool.length}</span></h3><div class="ps-qs" id="pgrvq">${pool.map(S.cardHTML).join('')}</div><div class="ps-rv-sum" id="pgrvs" hidden></div></section>
  </div>`;
  document.body.appendChild(el);document.body.style.overflow='hidden';
  const close=()=>{el.remove();document.body.style.overflow=''};
  q('#pgrx',el).onclick=close;
  qa('[data-say]',el).forEach(b=>{if(!b.classList.contains('ps-fig')&&!b.classList.contains('ps-mini'))b.onclick=()=>tts(b.dataset.say)});
  qa('[data-ep]',el).forEach(b=>b.onclick=()=>{close();try{play(cid,+b.dataset.ep)}catch(e){}});
  let hits=0,n=0;const miss=new Set();
  S.bindCards(q('#pgrvq',el),pool,(i,ok)=>{n++;if(ok)hits++;else miss.add(pool[i].tag);q('#pgrvc',el).textContent=n+'/'+pool.length;
    if(n===pool.length){const s=q('#pgrvs',el);s.hidden=false;s.innerHTML=`<b>${hits} de ${pool.length} certas</b><p>${miss.size?'Vale rever: '+[...miss].map(H).join(' · '):'Você dominou todos os padrões até aqui! 🌟'}</p>`;s.scrollIntoView({behavior:'smooth',block:'nearest'});try{if(window.confetti&&hits===pool.length)confetti(60)}catch(e){}}});
  el.scrollTop=0;
}
window.PogReview={open,collect};
/* botão "Revisão" ao lado do episódio no mapa do curso */
document.addEventListener('click',ev=>{
  const b=ev.target.closest&&ev.target.closest('[data-rev]');if(!b)return;
  ev.preventDefault();ev.stopPropagation();
  const [cid,i]=b.dataset.rev.split(':');open(cid,+i);
},true);
document.addEventListener('keydown',ev=>{if((ev.key==='Enter'||ev.key===' ')&&ev.target&&ev.target.dataset&&ev.target.dataset.rev){ev.preventDefault();ev.stopPropagation();const [cid,i]=ev.target.dataset.rev.split(':');open(cid,+i)}},true);
})();
