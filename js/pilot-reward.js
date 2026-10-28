/* Recompensas do episódio (piloto): trilha do Poggie com estrelas, reação a cada resposta,
   sequência de acertos e medalha com a figurinha da obra. Ativo só nos 5 primeiros episódios do inglês A1. */
(function(){
'use strict';
const K_OFF='pogglot:fxoff',K_MEDALS='pogglot:medals';
const TIERS={gold:{ico:'🥇',name:'Medalha de ouro',rar:'Dourada',min:.9},silver:{ico:'🥈',name:'Medalha de prata',rar:'Rara',min:.7},bronze:{ico:'🥉',name:'Medalha de bronze',rar:'Comum',min:0}};
const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const rd=()=>{try{return matchMedia('(prefers-reduced-motion:reduce)').matches}catch(e){return false}};
const isOff=()=>{try{return localStorage.getItem(K_OFF)==='1'}catch(e){return false}};
const calm=()=>rd()||isOff();
function active(){return typeof P!=='undefined'&&!!P&&P.cid==='en-a1'&&P.idx<5&&!!P.e&&P.e.presentation==='regular-pilot-v1'&&!P.isTest}
function $q(s,r){return (r||document).querySelector(s)}

/* ---------- trilha de progresso ---------- */
function buildTrail(){
  const head=$q('#player .p-head');if(!head||$q('.pr-trail',head))return;
  const n=P.steps.length;
  const trail=document.createElement('div');trail.className='pr-trail';trail.setAttribute('aria-hidden','true');
  trail.innerHTML=`<div class="pr-line"><i class="pr-fill"></i></div>${P.steps.map((_,i)=>`<b class="pr-star" style="left:${(i/Math.max(1,n-1)*100).toFixed(2)}%">★</b>`).join('')}<span class="pr-pog" id="prpog">${typeof poggie==='function'?poggie({scarf:P.c&&P.c.scarf}):'🦜'}</span>`;
  const prog=$q('.prog',head);if(prog)prog.classList.add('pr-sr');
  const row=document.createElement('div');row.className='pr-row';row.append(trail);
  const tg=document.createElement('button');tg.type='button';tg.className='pr-toggle';tg.id='prtg';
  const syncTg=()=>{tg.textContent=isOff()?'✨ off':'✨';tg.setAttribute('aria-pressed',isOff()?'false':'true');tg.setAttribute('aria-label',isOff()?'Ligar animações de recompensa':'Desligar animações de recompensa')};
  tg.onclick=()=>{try{localStorage.setItem(K_OFF,isOff()?'0':'1')}catch(e){}syncTg()};syncTg();
  row.append(tg);head.append(row);
}
function update(){
  const pl=$q('#player');if(!pl)return;
  if(!active()){pl.classList.remove('pr-on');return}
  pl.classList.add('pr-on');buildTrail();
  const n=P.steps.length,pct=P.i/Math.max(1,n-1)*100;
  const fill=$q('.pr-fill'),pog=$q('#prpog');
  if(fill)fill.style.width=pct+'%';if(pog)pog.style.left=pct+'%';
  document.querySelectorAll('.pr-star').forEach((s,i)=>{
    const lit=i<P.i;
    if(lit&&!s.classList.contains('on')){s.classList.add('on');if(!calm()){s.classList.remove('pop');void s.offsetWidth;s.classList.add('pop')}}
    if(!lit)s.classList.remove('on','pop');
  });
}

/* ---------- camada de efeitos ---------- */
function layer(){let l=$q('#prlayer');if(!l){l=document.createElement('div');l.id='prlayer';l.className='pr-layer';document.body.appendChild(l)}return l}
function sparks(x,y,n){
  const l=layer();
  for(let i=0;i<n;i++){
    const s=document.createElement('i');s.className='pr-spark';
    const a=Math.PI*2*i/n+Math.random()*.6,d=26+Math.random()*30;
    s.style.left=x+'px';s.style.top=y+'px';s.style.setProperty('--dx',Math.cos(a)*d+'px');s.style.setProperty('--dy',Math.sin(a)*d+'px');
    s.textContent=i%3===0?'✦':'•';l.appendChild(s);setTimeout(()=>s.remove(),600);
  }
}
/* ---------- reação a cada resposta ---------- */
function figOn(){return !!(window.PogFig&&PogFig.active())}
function answer(ok,el){
  const pilot=active();
  if(!pilot&&!figOn())return;
  P.prTries=(P.prTries||0)+1;
  const r=el&&el.getBoundingClientRect?el.getBoundingClientRect():{left:innerWidth/2,top:innerHeight/2,width:0,height:0};
  const x=r.left+Math.min(r.width,260)/2,y=r.top+Math.min(r.height,80)/2;
  if(ok){
    P.prHits=(P.prHits||0)+1;P.prCombo=(P.prCombo||0)+1;
    if(pilot&&!calm())sparks(x,y,P.prCombo>=3?12:7);
  }else{
    P.prCombo=0;
    if(!pilot)return;
    if(!calm()&&el&&el.classList){el.classList.remove('pr-shake');void el.offsetWidth;el.classList.add('pr-shake')}
    const bub=$q('#pbub');if(bub)bub.textContent='Quase! Leia a dica abaixo e siga em frente: errar faz parte.';
  }
}

/* ---------- fim do episódio ---------- */
function tier(){
  const t=P.prTries||0,acc=t?(P.prHits||0)/t:1;
  const key=acc>=TIERS.gold.min?'gold':acc>=TIERS.silver.min?'silver':'bronze';
  return {key,acc,hits:P.prHits||0,tries:t};
}
function saveMedal(res){
  try{
    const all=JSON.parse(localStorage.getItem(K_MEDALS)||'{}'),k=P.cid+'-'+P.e.n,rank={bronze:0,silver:1,gold:2};
    if(!all[k]||rank[res.key]>rank[all[k].tier])all[k]={tier:res.key,acc:Math.round(res.acc*100),w:(P.e.a||{}).w||'',t:Date.now()};
    localStorage.setItem(K_MEDALS,JSON.stringify(all));
  }catch(e){}
}
function medalHTML(){
  if(!active())return '';
  const res=tier(),T=TIERS[res.key],a=P.e.a||{};saveMedal(res);
  const sub=res.tries?`${res.hits} de ${res.tries} respostas de primeira`:'Episódio concluído';
  return `<div class="pr-medal ${res.key}"><div class="pr-disc" aria-hidden="true">${T.ico}</div><div class="pr-mt"><b>${T.name}</b><small>${esc(sub)}</small></div></div>
  <div class="pr-sticker ${res.key}"><div class="pr-st-face"><small>FIGURINHA ${esc(T.rar.toUpperCase())}</small><b>${esc(a.w||P.e.t)}</b><span>${esc(a.k||'')}${a.y?' · '+esc(a.y):''}</span></div></div>`;
}
function celebrate(){
  if(!active()&&!figOn())return false;
  if(calm())return true;
  const c=$q('#confetti');if(!c)return true;
  const x=c.getContext('2d');c.width=innerWidth;c.height=innerHeight;
  const cols=['#F2C94C','#F29B34','#E85D75','#0C7A78','#6B3FA0'];
  const side=i=>i%2?1:0;
  const ps=[...Array(56)].map((_,i)=>({x:side(i)?innerWidth-8:8,y:innerHeight*.35,vx:(side(i)?-1:1)*(2+Math.random()*5),vy:-(5+Math.random()*7),r:4+Math.random()*3,c:cols[i%cols.length],a:Math.random()*6,s:(Math.random()-.5)*.3}));
  let f=0;(function tick(){
    x.clearRect(0,0,c.width,c.height);const al=Math.max(0,1-f/72);
    ps.forEach(p=>{p.vy+=.35;p.x+=p.vx;p.y+=p.vy;p.vx*=.985;p.a+=p.s;x.save();x.globalAlpha=al*.8;x.translate(p.x,p.y);x.rotate(p.a);x.fillStyle=p.c;x.fillRect(-p.r/2,-p.r/4,p.r,p.r/2);x.restore()});
    if(++f<72)requestAnimationFrame(tick);else x.clearRect(0,0,c.width,c.height);
  })();
  return true;
}

/* liga a trilha ao progresso do player */
const prev=window.setProg;
if(typeof prev==='function'){window.setProg=function(){const r=prev.apply(this,arguments);try{update()}catch(e){}return r}}
window.PogReward={active,answer,medalHTML,celebrate,update};
})();
