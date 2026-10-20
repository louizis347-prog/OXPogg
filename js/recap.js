/* Pogglot · retrospectiva semanal, cartão de aluno (com imagem para compartilhar) e animações de números */
(function(){
'use strict';
const HL=()=>(ST.homeLang==='es'?'es':'pt');
const T={pt:{wk:'Sua semana',wkSub:'Resumo dos últimos 7 dias',xp:'XP',eps:'episódios',ans:'respostas',best:'melhor dia',share:'Compartilhar',card:'Cartão de aluno',since:'Aluno desde',lg:'Liga',streak:'dias seguidos',days:['D','S','T','Q','Q','S','S'],empty:'Estude hoje para começar o seu gráfico.',copied:'Texto copiado!',stud:'Estudante'},
 es:{wk:'Tu semana',wkSub:'Resumen de los últimos 7 días',xp:'XP',eps:'episodios',ans:'respuestas',best:'mejor día',share:'Compartir',card:'Carné de alumno',since:'Alumno desde',lg:'Liga',streak:'días seguidos',days:['D','L','M','X','J','V','S'],empty:'Estudia hoy para empezar tu gráfico.',copied:'¡Texto copiado!',stud:'Estudiante'}};
const k=x=>(T[HL()]||T.pt)[x];
const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const dk=d=>{d=d||new Date();return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0')};
const cur=()=>({xp:ST.xp||0,eps:Object.keys(ST.done||{}).length,ans:ST.totalAnswered||0});
/* ---------- registro diário ---------- */
function track(){
  const w=store.get('wk',{snap:null,days:{}}),c=cur(),today=dk();
  if(!w.snap){w.snap=c;store.set('wk',w);if(!store.get('since',null))store.set('since',today);return w}
  const dx=Math.max(0,c.xp-w.snap.xp),de=Math.max(0,c.eps-w.snap.eps),da=Math.max(0,c.ans-w.snap.ans);
  if(dx||de||da){const d=w.days[today]||{xp:0,eps:0,ans:0};d.xp+=dx;d.eps+=de;d.ans+=da;w.days[today]=d}
  w.snap=c;
  const keep={},lim=new Date(Date.now()-40*864e5);Object.keys(w.days).forEach(x=>{if(new Date(x)>=lim)keep[x]=w.days[x]});w.days=keep;
  store.set('wk',w);if(!store.get('since',null))store.set('since',today);return w;
}
function week(){
  const w=track(),out=[];
  for(let i=6;i>=0;i--){const d=new Date(Date.now()-i*864e5),v=w.days[dk(d)]||{xp:0,eps:0,ans:0};out.push({d,dow:d.getDay(),xp:v.xp,eps:v.eps,ans:v.ans,today:i===0})}
  const tot=out.reduce((a,x)=>({xp:a.xp+x.xp,eps:a.eps+x.eps,ans:a.ans+x.ans}),{xp:0,eps:0,ans:0});
  const best=out.reduce((a,x)=>x.xp>a.xp?x:a,out[0]);
  return{days:out,tot,best};
}
function recapHTML(){
  const W=week(),max=Math.max(1,...W.days.map(x=>x.xp)),dn=k('days');
  return `<section class="px-recapw"><div class="hd"><div><small>${esc(k('wkSub'))}</small><h2>${esc(k('wk'))}</h2></div><button class="sh" data-recap="week" aria-label="${esc(k('share'))}">⤴ ${esc(k('share'))}</button></div>
   <div class="chart">${W.days.map(x=>`<div class="c ${x.today?'t':''}"><i style="height:${Math.max(6,Math.round(x.xp/max*100))}%" title="${x.xp} XP"></i><span>${dn[x.dow]}</span></div>`).join('')}</div>
   <div class="tots"><div><b data-cu>${W.tot.xp}</b><small>${esc(k('xp'))}</small></div><div><b data-cu>${W.tot.eps}</b><small>${esc(k('eps'))}</small></div><div><b data-cu>${W.tot.ans}</b><small>${esc(k('ans'))}</small></div></div>
   ${W.tot.xp?'':`<p class="em">${esc(k('empty'))}</p>`}</section>`;
}
function user(){try{return PogCloud&&PogCloud.user&&PogCloud.user()}catch(e){return null}}
function cardData(){
  const u=user(),lg=PogUI.league(ST.xp||0),since=store.get('since',dk());
  return{name:(u&&u.name)||k('stud'),avatar:(u&&u.avatar)||'🙂',lg:lg.name,color:lg.color,xp:ST.xp||0,streak:ST.streak.n||0,eps:cur().eps,books:(ST.shelf||[]).length,since};
}
function cardHTML(){
  const c=cardData(),sd=new Date(c.since).toLocaleDateString(HL()==='es'?'es':'pt-BR',{month:'short',year:'numeric'});
  return `<section class="px-idc" style="--lc:${c.color}"><div class="shine"></div><div class="row"><span class="av">${esc(c.avatar)}</span><div class="id"><small>${esc(k('card'))}</small><b>${esc(c.name)}</b></div><span class="lg">${esc(k('lg'))} ${esc(c.lg)}</span></div>
   <div class="stats"><div><b>${c.streak}</b><small>${esc(k('streak'))}</small></div><div><b>${c.xp}</b><small>XP</small></div><div><b>${c.eps}</b><small>${esc(k('eps'))}</small></div><div><b>${c.books}</b><small>📚</small></div></div>
   <div class="ft"><span>${esc(k('since'))} ${esc(sd)}</span><span class="lgo">Pogg<b>lot</b></span><button data-recap="card">⤴ ${esc(k('share'))}</button></div></section>`;
}
/* ---------- imagem para compartilhar ---------- */
function rr(x,a,b,w,h,r){x.beginPath();x.moveTo(a+r,b);x.arcTo(a+w,b,a+w,b+h,r);x.arcTo(a+w,b+h,a,b+h,r);x.arcTo(a,b+h,a,b,r);x.arcTo(a,b,a+w,b,r);x.closePath()}
function draw(kind){
  const W=1080,H=1350,cv=document.createElement('canvas');cv.width=W;cv.height=H;const x=cv.getContext('2d');
  const g=x.createLinearGradient(0,0,W,H);g.addColorStop(0,'#2A1670');g.addColorStop(.55,'#6B3BF0');g.addColorStop(1,'#C13BD6');x.fillStyle=g;x.fillRect(0,0,W,H);
  const r1=x.createRadialGradient(W,0,0,W,0,700);r1.addColorStop(0,'rgba(255,120,210,.55)');r1.addColorStop(1,'rgba(255,120,210,0)');x.fillStyle=r1;x.fillRect(0,0,W,H);
  const r2=x.createRadialGradient(0,H,0,0,H,700);r2.addColorStop(0,'rgba(60,190,255,.4)');r2.addColorStop(1,'rgba(60,190,255,0)');x.fillStyle=r2;x.fillRect(0,0,W,H);
  const F='"Plus Jakarta Sans","Plus Jakarta Sans",system-ui,sans-serif';x.fillStyle='#fff';x.textBaseline='alphabetic';
  x.font='800 54px '+F;x.fillText('Pogglot',72,120);
  if(kind==='card'){
    const c=cardData();
    x.font='700 36px '+F;x.globalAlpha=.8;x.fillText(k('card'),72,230);x.globalAlpha=1;
    x.font='180px serif';x.fillText(c.avatar,72,470);
    x.font='800 88px '+F;x.fillText(c.name.slice(0,16),72,590);
    x.font='800 44px '+F;x.fillStyle='rgba(255,255,255,.18)';rr(x,72,630,520,86,43);x.fill();x.fillStyle='#fff';x.fillText(k('lg')+' '+c.lg,110,690);
    const items=[[c.streak,k('streak')],[c.xp,'XP'],[c.eps,k('eps')],[c.books,'📚']];
    items.forEach((it,i)=>{const px=72+(i%2)*470,py=800+Math.floor(i/2)*230;x.fillStyle='rgba(255,255,255,.14)';rr(x,px,py,440,200,40);x.fill();x.fillStyle='#fff';x.font='800 92px '+F;x.fillText(String(it[0]),px+36,py+110);x.font='700 34px '+F;x.globalAlpha=.8;x.fillText(it[1],px+36,py+160);x.globalAlpha=1});
  }else{
    const wk=week(),max=Math.max(1,...wk.days.map(d=>d.xp)),dn=k('days');
    x.font='700 36px '+F;x.globalAlpha=.8;x.fillText(k('wkSub'),72,230);x.globalAlpha=1;
    x.font='800 110px '+F;x.fillText(k('wk'),72,360);
    wk.days.forEach((d,i)=>{const bw=100,gap=(W-144-bw*7)/6,px=72+i*(bw+gap),bh=Math.max(34,d.xp/max*380),py=820-bh;x.fillStyle=d.today?'#FFE58A':'rgba(255,255,255,.55)';rr(x,px,py,bw,bh,28);x.fill();x.fillStyle='#fff';x.font='800 36px '+F;x.textAlign='center';x.fillText(dn[d.dow],px+bw/2,880);x.textAlign='left'});
    [[wk.tot.xp,k('xp')],[wk.tot.eps,k('eps')],[wk.tot.ans,k('ans')]].forEach((it,i)=>{const px=72+i*320;x.fillStyle='rgba(255,255,255,.14)';rr(x,px,1000,296,230,40);x.fill();x.fillStyle='#fff';x.font='800 96px '+F;x.fillText(String(it[0]),px+30,1110);x.font='700 34px '+F;x.globalAlpha=.8;x.fillText(it[1],px+30,1170);x.globalAlpha=1});
  }
  x.font='700 34px '+F;x.globalAlpha=.75;x.fillText('pogglot · '+(location.host||''),72,H-60);x.globalAlpha=1;
  return cv;
}
async function share(kind){
  const cv=draw(kind);
  const blob=await new Promise(r=>cv.toBlob(r,'image/png'));
  const name='pogglot-'+kind+'.png';
  try{const f=new File([blob],name,{type:'image/png'});if(navigator.canShare&&navigator.canShare({files:[f]})){await navigator.share({files:[f],title:'Pogglot'});return}}catch(e){if(e&&e.name==='AbortError')return}
  const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download=name;document.body.appendChild(a);a.click();setTimeout(()=>{URL.revokeObjectURL(a.href);a.remove()},500);
}
document.addEventListener('click',e=>{const b=e.target.closest&&e.target.closest('[data-recap]');if(b){e.preventDefault();share(b.dataset.recap).catch(()=>{})}});
/* ---------- números que "contam" ---------- */
function countUp(el){
  if(el.dataset.cud)return;el.dataset.cud='1';
  const txt=el.textContent.trim(),pct=/%$/.test(txt),n=parseInt(txt.replace(/[^\d]/g,''),10);
  if(!isFinite(n)||n<=0||matchMedia('(prefers-reduced-motion: reduce)').matches)return;
  const dur=Math.min(1100,500+n*2),t0=performance.now(),fmt=v=>(txt.indexOf('.')>=0||txt.indexOf(',')>=0?v.toLocaleString(HL()==='es'?'es':'pt-BR'):String(v))+(pct?'%':'');
  (function f(t){const p=Math.min(1,(t-t0)/dur),e=1-Math.pow(1-p,3);el.textContent=fmt(Math.round(n*e));if(p<1)requestAnimationFrame(f)})(t0);
}
function scan(){document.querySelectorAll('[data-cu]:not([data-cud])').forEach(countUp)}
const host=document.getElementById('app')||document.body;
new MutationObserver(()=>{clearTimeout(scan.t);scan.t=setTimeout(scan,30)}).observe(host,{childList:true});
track();setInterval(track,45000);document.addEventListener('visibilitychange',()=>{if(document.hidden)track()});
window.PogRecap={recapHTML,cardHTML,week,track,share};
})();
