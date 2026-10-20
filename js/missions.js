/* Pogglot · missões diárias, baú, gemas e congelar sequência (tudo local no aparelho) */
(function(){
'use strict';
const HL=()=>(ST.homeLang==='es'?'es':'pt');
const T={pt:{h:'Missões de hoje',sub:'Complete as 3 missões e abra o baú.',claim:'Pegar',done:'Pego',chest:'Abrir baú',chestDone:'Baú aberto hoje',shop:'Congelar sequência',shopD:'Protege sua sequência se você faltar 1 dia.',buy:'Comprar',own:'tem',noGems:'Gemas insuficientes',saved:'Sequência salva!',
  xp30:'Ganhe 30 XP',xp60:'Ganhe 60 XP',eps1:'Conclua 1 episódio',ans12:'Responda 12 perguntas',book1:'Descubra 1 obra nova',got:'Você ganhou',chestT:'Baú aberto!',more:'Ver as outras',less:'Ocultar',left:n=>n+(n===1?' missão para hoje':' missões para hoje'),allok:'Todas concluídas!'},
 es:{h:'Misiones de hoy',sub:'Completa las 3 misiones y abre el cofre.',claim:'Recoger',done:'Recogido',chest:'Abrir cofre',chestDone:'Cofre abierto hoy',shop:'Congelar racha',shopD:'Protege tu racha si faltas 1 día.',buy:'Comprar',own:'tienes',noGems:'Gemas insuficientes',saved:'¡Racha salvada!',
  xp30:'Gana 30 XP',xp60:'Gana 60 XP',eps1:'Completa 1 episodio',ans12:'Responde 12 preguntas',book1:'Descubre 1 obra nueva',got:'Ganaste',chestT:'¡Cofre abierto!',more:'Ver las otras',less:'Ocultar',left:n=>n+(n===1?' misión para hoy':' misiones para hoy'),allok:'¡Todas completadas!'}};
const tr=k=>(T[HL()]||T.pt)[k];
const POOL=[{id:'xp30',m:'xp',n:30,g:5},{id:'eps1',m:'eps',n:1,g:8},{id:'ans12',m:'ans',n:12,g:5},{id:'book1',m:'book',n:1,g:6},{id:'xp60',m:'xp',n:60,g:8}];
const FREEZE_COST=50;
const dayKey=()=>{const d=new Date();return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0')};
const cur=()=>({xp:ST.xp||0,eps:Object.keys(ST.done||{}).length,ans:ST.totalAnswered||0,book:(ST.shelf||[]).length});
const wallet=()=>store.get('wallet',{gems:0,freeze:0});
const setWallet=w=>store.set('wallet',w);
function hash(s){let h=0;for(let i=0;i<s.length;i++)h=(h*31+s.charCodeAt(i))>>>0;return h}
function state(){
  let s=store.get('mis',null);const k=dayKey();
  if(!s||s.day!==k){
    const h=hash(k),ids=[];let i=h%POOL.length;while(ids.length<3){const id=POOL[i%POOL.length].id;if(!ids.includes(id)&&!(id==='xp30'&&ids.includes('xp60'))&&!(id==='xp60'&&ids.includes('xp30')))ids.push(id);i++}
    s={day:k,base:cur(),ids,claimed:[],chest:false};store.set('mis',s);
  }
  return s;
}
function list(){const s=state(),c=cur();return s.ids.map(id=>{const d=POOL.find(x=>x.id===id),v=Math.max(0,Math.min(d.n,c[d.m]-s.base[d.m]));return{id,label:tr(id),v,n:d.n,g:d.g,ok:v>=d.n,claimed:s.claimed.includes(id)}})}
function claim(id){const s=state(),m=list().find(x=>x.id===id);if(!m||!m.ok||m.claimed)return 0;s.claimed.push(id);store.set('mis',s);const w=wallet();w.gems+=m.g;setWallet(w);return m.g}
function openChest(){const s=state();if(s.chest||list().some(m=>!m.claimed))return null;s.chest=true;store.set('mis',s);const w=wallet(),g=15+hash(s.day)%11,xp=30;w.gems+=g;setWallet(w);ST.xp+=xp;try{save()}catch(e){}return{g,xp}}
function buyFreeze(){const w=wallet();if(w.gems<FREEZE_COST)return false;w.gems-=FREEZE_COST;w.freeze=(w.freeze||0)+1;setWallet(w);return true}
function cardHTML(){
  const L=list(),w=wallet(),s=state(),all=L.every(m=>m.claimed);
  const E=x=>String(x).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  const row=m=>`<div class="r ${m.ok?'ok':''} ${m.claimed?'cl':''}"><span class="ic">${m.claimed?'✅':m.ok?'🎁':'🎯'}</span><div class="tx"><b>${E(m.label)}</b><div class="bar"><i style="width:${(m.v/m.n*100).toFixed(0)}%"></i></div><small>${m.v}/${m.n}</small></div>
     ${m.claimed?`<span class="dn">${E(tr('done'))}</span>`:`<button class="cl" data-ms="claim:${m.id}" ${m.ok?'':'disabled'}>+${m.g} 💎<em>${E(tr('claim'))}</em></button>`}</div>`;
  /* só a missão mais próxima fica à vista; o resto abre sob demanda */
  const pend=L.filter(m=>!m.claimed),lead=pend.find(m=>m.ok)||pend[0]||null,rest=L.filter(m=>m!==lead);
  const sub=all?tr('allok'):tr('left')(pend.length);
  return `<section class="px-mis" id="px-mis"><div class="hd"><div><h2>${E(tr('h'))}</h2><p>${E(sub)}</p></div><div class="wal"><span class="g">💎 <b>${w.gems}</b></span><span class="f" title="${E(tr('shop'))}">🧊 <b>${w.freeze||0}</b></span></div></div>
   ${lead?`<div class="rows">${row(lead)}</div>`:''}
   <details class="more"><summary><span class="o">${E(tr('more'))}</span><span class="c">${E(tr('less'))}</span></summary>
    ${rest.length?`<div class="rows">${rest.map(row).join('')}</div>`:''}
    <div class="ft"><button class="chest ${all&&!s.chest?'rdy':''}" data-ms="chest" ${all&&!s.chest?'':'disabled'}><span>${s.chest?'📭':'🎁'}</span>${E(s.chest?tr('chestDone'):tr('chest'))}</button>
    <button class="shop" data-ms="buy" title="${E(tr('shopD'))}"><span>🧊</span><div><b>${E(tr('shop'))}</b><small>${FREEZE_COST} 💎</small></div></button></div></details></section>`;
}
function rerender(){const el=document.getElementById('px-mis');if(el){const op=el.querySelector('details.more');const was=!!(op&&op.open);const t=document.createElement('div');t.innerHTML=cardHTML();const n=t.firstElementChild;if(was){const d=n.querySelector('details.more');if(d)d.open=true}el.replaceWith(n)}}
function toast(msg){const d=document.createElement('div');d.className='px-toast';d.textContent=msg;document.body.appendChild(d);requestAnimationFrame(()=>d.classList.add('on'));setTimeout(()=>{d.classList.remove('on');setTimeout(()=>d.remove(),300)},2200)}
document.addEventListener('click',e=>{
  const b=e.target.closest&&e.target.closest('[data-ms]');if(!b||b.disabled)return;
  const a=b.dataset.ms;
  if(a.startsWith('claim:')){const g=claim(a.slice(6));if(g){try{confetti(30)}catch(x){}toast('+'+g+' 💎')}}
  else if(a==='chest'){const r=openChest();if(r){try{confetti(80)}catch(x){}toast(tr('chestT')+' +'+r.g+' 💎 +'+r.xp+' XP')}}
  else if(a==='buy'){if(buyFreeze())toast('🧊 +1');else toast(tr('noGems'))}
  rerender();try{if(window.PogUI&&PogUI.syncNow)0}catch(x){}
});
/* congelar sequência: se faltou exatamente 1 dia e há congelamento, a sequência continua */
const orig=window.bumpStreak;
if(typeof orig==='function')window.bumpStreak=function(){
  try{const d=new Date(),k=d.toISOString().slice(0,10),y2=new Date(d-2*864e5).toISOString().slice(0,10),y1=new Date(d-864e5).toISOString().slice(0,10);
    if(ST.streak.last&&ST.streak.last!==k&&ST.streak.last===y2&&ST.streak.n>0){const w=wallet();if(w.freeze>0){w.freeze--;setWallet(w);ST.streak.last=y1;setTimeout(()=>{try{toast('🧊 '+tr('saved'))}catch(x){}},400)}}
  }catch(e){}
  return orig.apply(this,arguments);
};
window.PogMissions={cardHTML,list,claim,openChest,buyFreeze,wallet,state};
})();
