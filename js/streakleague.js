/* Pogglot · proteção de sequência (até 2 🧊) + liga semanal de treino.
   Tudo local (localStorage via store). Kill-switch: window.POG_STREAKLEAGUE=false. */
(function(){
'use strict';
if(window.POG_STREAKLEAGUE===false)return;
try{
if(typeof ST==='undefined'||typeof store==='undefined')return;
var MAXF=2,EVERY=7,DAY=864e5;
var HL=function(){return ST.homeLang==='es'?'es':'pt'};
var TX={pt:{
 saved:function(n,d){return 'Sua proteção salvou sua sequência de '+n+' dias 🧊'+(d>1?' (usou '+d+')':'')},
 earn:'Você ganhou uma proteção de sequência 🧊 (a cada 7 dias seguidos)',full:'Estoque de proteções cheio (máx. 2)',
 chip:'Proteções de sequência',chipD:function(n){return n+' de 2 proteções'},how:'Ganhe 1 🧊 a cada 7 dias seguidos ou compre com 💎. Ela cobre 1 dia sem estudar.',
 lost:'Sua sequência recomeçou. Estude hoje para começar outra!',
 lg:'Liga semanal',train:'liga de treino · rivais simulados',tiers:['Bronze','Prata','Ouro','Safira','Rubi','Ametista','Diamante'],
 left:function(d){return d<=1?'termina hoje':'faltam '+d+' dias'},you:'Você',pts:'XP',up:'Zona de promoção',down:'Zona de rebaixamento',
 sub:function(r,n){return r+'º de '+n},prom:function(t){return '⬆️ Você subiu para '+t+'!'},dem:function(t){return '⬇️ Você desceu para '+t},stay:function(t){return 'Você ficou em '+t},
 last:'Semana passada',zero:'Ganhe XP para sair do zero',sim:'simulado',more:'Ver placar',less:'Ocultar',tip:'Top 5 sobem, os 3 últimos descem. Reinicia na segunda.'},
es:{
 saved:function(n,d){return 'Tu protección salvó tu racha de '+n+' días 🧊'+(d>1?' (usó '+d+')':'')},
 earn:'Ganaste una protección de racha 🧊 (cada 7 días seguidos)',full:'Almacén de protecciones lleno (máx. 2)',
 chip:'Protecciones de racha',chipD:function(n){return n+' de 2 protecciones'},how:'Gana 1 🧊 cada 7 días seguidos o cómprala con 💎. Cubre 1 día sin estudiar.',
 lost:'Tu racha se reinició. ¡Estudia hoy para empezar otra!',
 lg:'Liga semanal',train:'liga de entrenamiento · rivales simulados',tiers:['Bronce','Plata','Oro','Zafiro','Rubí','Amatista','Diamante'],
 left:function(d){return d<=1?'termina hoy':'faltan '+d+' días'},you:'Tú',pts:'XP',up:'Zona de ascenso',down:'Zona de descenso',
 sub:function(r,n){return r+'.º de '+n},prom:function(t){return '⬆️ ¡Subiste a '+t+'!'},dem:function(t){return '⬇️ Bajaste a '+t},stay:function(t){return 'Te quedaste en '+t},
 last:'Semana pasada',zero:'Gana XP para salir de cero',sim:'simulado',more:'Ver tabla',less:'Ocultar',tip:'Los 5 primeros suben, los 3 últimos bajan. Se reinicia el lunes.'}};
var T=function(){return TX[HL()]};
var COLORS=['#C98A4B','#8E9BB0','#E9A800','#2F8FE0','#E5484D','#9B5DE5','#12B5BC'];
var E=function(x){return String(x).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})};

/* ---------- dia local ---------- */
function pad(n){return (n<10?'0':'')+n}
function key(d){return d.getFullYear()+'-'+pad(d.getMonth()+1)+'-'+pad(d.getDate())}
function ord(k){var m=/^(\d{4})-(\d\d)-(\d\d)/.exec(k||'');return m?Math.round(Date.UTC(+m[1],+m[2]-1,+m[3])/DAY):null} /* UTC puro: imune a horário de verão */
function today(){return key(new Date())}
function addDays(k,n){var m=/^(\d{4})-(\d\d)-(\d\d)/.exec(k),d=new Date(+m[1],+m[2]-1,+m[3]+n);return key(d)}
function weekStart(d){var x=new Date(d.getFullYear(),d.getMonth(),d.getDate());x.setDate(x.getDate()-((x.getDay()+6)%7));return key(x)} /* segunda local */

/* ---------- migração segura ---------- */
function mig(){
  var s=ST.streak;if(!s||typeof s!=='object'){s=ST.streak={n:0,last:null}}
  if(typeof s.n!=='number'||!isFinite(s.n)||s.n<0)s.n=0;
  if(typeof s.earned!=='number')s.earned=Math.floor(s.n/EVERY)*EVERY; /* não premia retroativamente */
  if(typeof s.saves!=='number')s.saves=0;
}
function wallet(){var w=store.get('wallet',{gems:0,freeze:0});if(!w||typeof w!=='object')w={gems:0,freeze:0};w.gems=+w.gems||0;w.freeze=Math.max(0,Math.min(MAXF,+w.freeze||0));return w}
function setWallet(w){store.set('wallet',w)}
function persist(){try{save()}catch(e){}}

function toast(msg){try{var d=document.createElement('div');d.className='px-toast sl-toast';d.textContent=msg;document.body.appendChild(d);requestAnimationFrame(function(){d.classList.add('on')});setTimeout(function(){d.classList.remove('on');setTimeout(function(){d.remove()},300)},3600)}catch(e){}}

/* ---------- reconcilia dias perdidos ---------- */
function reconcile(){
  mig();var s=ST.streak;if(!s.last||s.n<=0)return;
  var t=ord(today()),l=ord(s.last);if(t==null||l==null)return;
  var missed=t-l-1;if(missed<=0)return;
  var w=wallet();
  if(w.freeze>=missed){
    w.freeze-=missed;setWallet(w);s.last=addDays(today(),-1);s.saves+=missed;persist();
    var n=s.n;setTimeout(function(){toast(T().saved(n,missed))},500);
  }else{
    /* faltaram proteções: a sequência zera (o estoque fica intacto) */
    s.n=0;s.earned=0;persist();setTimeout(function(){toast(T().lost)},500);
  }
}

/* ---------- registra o dia (substitui o bumpStreak antigo, que usava UTC) ---------- */
window.bumpStreak=function(){
  try{
    mig();reconcile();
    var k=today(),s=ST.streak;if(s.last===k)return;
    s.n=(s.last&&ord(k)-ord(s.last)===1)?s.n+1:1;s.last=k;
    if(s.n>(+store.get('maxStreak',0)||0))store.set('maxStreak',s.n);
    if(s.n%EVERY===0&&s.n>s.earned){
      s.earned=s.n;var w=wallet();
      if(w.freeze<MAXF){w.freeze++;setWallet(w);setTimeout(function(){toast(T().earn)},900)}else setTimeout(function(){toast(T().full)},900);
    }
    persist();
  }catch(e){}
  setTimeout(function(){try{paint()}catch(e){}},50);
};

/* limite de 2 também na compra com 💎 (a loja de missions.js cobra gemas) */
document.addEventListener('click',function(e){
  try{var b=e.target.closest&&e.target.closest('[data-ms="buy"]');if(!b)return;
    if(wallet().freeze>=MAXF){e.stopImmediatePropagation();e.preventDefault();toast(T().full)}
  }catch(x){}
},true);

/* ---------- liga semanal ---------- */
var NAMES=['Ipê','Jabuti','Lua','Brisa','Cacau','Pitanga','Coral','Sereno','Tucano','Névoa','Açaí','Faísca','Bambu','Pampa','Girassol','Caju'];
function rng(seed){var h=2166136261;for(var i=0;i<seed.length;i++){h^=seed.charCodeAt(i);h=Math.imul(h,16777619)}return function(){h+=0x6D2B79F5;var t=Math.imul(h^h>>>15,1|h);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}}
var BASE=[110,170,250,350,470,610,780];
function rivals(wk,tier){
  var r=rng('pog|'+wk+'|'+tier),out=[],i,used={};
  for(i=0;i<14;i++){var nm;do{nm=NAMES[Math.floor(r()*NAMES.length)]}while(used[nm]&&Object.keys(used).length<NAMES.length);used[nm]=1;
    var tot=Math.round(BASE[tier]*(.25+r()*1.5)),shape=.7+r()*.6;out.push({name:'Poggler '+nm,total:tot,shape:shape})}
  return out;
}
function frac(){var n=new Date(),ws=new Date(n.getFullYear(),n.getMonth(),n.getDate());ws.setDate(ws.getDate()-((ws.getDay()+6)%7));return Math.min(1,Math.max(0,(n-ws)/(7*DAY)))}
function board(wk,tier,meXp,f){
  var rows=rivals(wk,tier).map(function(r){return{name:r.name,xp:Math.round(r.total*Math.pow(f,r.shape)),me:false}});
  rows.push({name:T().you,xp:meXp,me:true});
  rows.sort(function(a,b){return b.xp-a.xp||(a.me?-1:1)});
  rows.forEach(function(r,i){r.pos=i+1});return rows;
}
function lgState(){
  var L=store.get('lg',null),wk=weekStart(new Date());
  if(!L||typeof L!=='object'||typeof L.tier!=='number'){L={wk:wk,tier:0,base:ST.xp||0,res:null};store.set('lg',L);return L}
  L.tier=Math.max(0,Math.min(6,L.tier|0));
  if(L.wk!==wk){
    if(ord(L.wk)==null||ord(L.wk)>ord(wk)){L.wk=wk;L.base=ST.xp||0}
    var guard=0,first=true;
    var m0=/^(\d{4})-(\d\d)-(\d\d)/.exec(L.wk);L.wk=weekStart(new Date(+m0[1],+m0[2]-1,+m0[3]));
    while(ord(L.wk)<ord(wk)&&guard++<12){
      var spent=first?Math.max(0,(ST.xp||0)-(L.base||0)):0;first=false;
      var me=board(L.wk,L.tier,spent,1).filter(function(r){return r.me})[0],res='stay',t0=L.tier;
      if(me.pos<=5&&spent>0&&L.tier<6){L.tier++;res='up'}else if(me.pos>=12&&L.tier>0){L.tier--;res='down'}
      L.res={wk:L.wk,from:t0,to:L.tier,pos:me.pos,xp:spent,r:res};
      L.wk=addDays(L.wk,7);
    }
    L.wk=wk;L.base=ST.xp||0;
    store.set('lg',L);
  }
  if((ST.xp||0)<L.base){L.base=ST.xp||0;store.set('lg',L)} /* XP nunca negativo na semana */
  return L;
}
function daysLeft(){var n=new Date(),d=(7-((n.getDay()+6)%7));return d}
function leagueHTML(open){
  var L=lgState(),t=T(),tier=L.tier,xp=Math.max(0,(ST.xp||0)-L.base),rows=board(L.wk,tier,xp,frac()),me=rows.filter(function(r){return r.me})[0];
  var col=COLORS[tier],nm=t.tiers[tier],N=rows.length;
  var show=rows.filter(function(r){return open?true:(Math.abs(r.pos-me.pos)<=1||r.pos<=3)});
  var rowH=function(r,i){var z=r.pos<=5?'up':(r.pos>=12?'dn':'');
    return '<li class="'+(r.me?'me ':'')+z+'"><span class="p">'+r.pos+'</span><span class="n">'+E(r.name)+(r.me?'':' <em>'+E(t.sim)+'</em>')+'</span><b>'+r.xp+' '+t.pts+'</b></li>'};
  var last=L.res&&L.res.wk!==L.wk?L.res:null,ln='';
  if(last&&!store.get('lgSeen_'+last.wk,0)){ln='<p class="sl-res '+last.r+'">'+E(t.last)+': '+E(last.r==='up'?t.prom(t.tiers[last.to]):last.r==='down'?t.dem(t.tiers[last.to]):t.stay(t.tiers[last.to]))+' · '+last.pos+'º</p>'}
  return '<section class="sl-lg" id="sl-lg" style="--sl-c:'+col+'"><div class="hd"><span class="gem" aria-hidden="true"></span><div><h2>'+E(t.lg)+' · '+E(nm)+'</h2><p>'+E(t.sub(me.pos,N))+' · '+xp+' XP · '+E(t.left(daysLeft()))+'</p></div></div>'
   +ln+'<ol class="sl-rows">'+show.map(rowH).join('')+'</ol>'
   +'<div class="ft"><button type="button" class="tg" data-sl="tg">'+E(open?t.less:t.more)+'</button><small>'+E(t.train)+'</small></div>'
   +'<small class="sl-tip">'+E(t.tip)+(xp===0?' · '+E(t.zero):'')+'</small></section>';
}
var openBoard=false;
function freezeHTML(){var w=wallet(),t=T(),n=w.freeze,ic='';for(var i=0;i<MAXF;i++)ic+='<i class="'+(i<n?'on':'')+'">🧊</i>';
  return '<section class="sl-fz" id="sl-fz"><div class="ic">'+ic+'</div><div><b>'+E(t.chip)+' · '+E(t.chipD(n))+'</b><small>'+E(t.how)+'</small></div></section>'}

/* ---------- pintura na home e no painel ---------- */
function paint(){
  try{
    var app=document.getElementById('app');if(!app)return;
    var fire=document.querySelector('.pgstat.fire')||app.querySelector('.topbar .stats .chip');
    if(fire&&fire.parentNode){var c=fire.parentNode.querySelector('.sl-chip'),n=wallet().freeze;
      if(!c){c=document.createElement('span');c.className='pgstat chip sl-chip';fire.insertAdjacentElement('afterend',c)}
      var tx='🧊 '+n;if(c.textContent!==tx)c.textContent=tx;c.title=T().chipD(n)}
    var mis=app.querySelector('#px-mis'),dash=app.querySelector('.px-stats')||app.querySelector('.dash-stats');
    var anchor=mis||dash;
    var lg=app.querySelector('#sl-lg'),fz=app.querySelector('#sl-fz');
    if(!anchor){return}
    var html=leagueHTML(openBoard);
    if(!lg){anchor.insertAdjacentHTML('afterend',html)}
    else if(lg.dataset.k!==html){var t=document.createElement('div');t.innerHTML=html;lg.replaceWith(t.firstElementChild)}
    var cur=app.querySelector('#sl-lg');if(cur)cur.dataset.k=html;
    if(dash&&!fz){anchor.insertAdjacentHTML('afterend',freezeHTML())}
    else if(fz){var f2=document.createElement('div');f2.innerHTML=freezeHTML();if(fz.innerHTML!==f2.firstElementChild.innerHTML)fz.replaceWith(f2.firstElementChild)}
  }catch(e){}
}
document.addEventListener('click',function(e){
  var b=e.target.closest&&e.target.closest('[data-sl="tg"]');if(!b)return;
  openBoard=!openBoard;try{var L=lgState();if(L.res)store.set('lgSeen_'+L.res.wk,1)}catch(x){}paint();
});
var timer=null;
function later(){clearTimeout(timer);timer=setTimeout(paint,40)}
function boot(){
  try{mig();reconcile();lgState()}catch(e){}
  var app=document.getElementById('app');
  if(app){new MutationObserver(function(m){
    for(var i=0;i<m.length;i++){var a=m[i].addedNodes;for(var j=0;j<a.length;j++){var nd=a[j];if(nd.nodeType===1&&nd.id!=='sl-lg'&&nd.id!=='sl-fz'&&!(nd.classList&&nd.classList.contains('sl-chip'))){later();return}}}
  }).observe(app,{childList:true,subtree:true})}
  document.addEventListener('visibilitychange',function(){if(!document.hidden){try{reconcile();lgState()}catch(e){}later()}});
  paint();
}
window.PogStreak={reconcile:reconcile,paint:paint,league:lgState,board:board,freeze:function(){return wallet().freeze}};
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',boot);else boot();
}catch(e){try{console.warn('streakleague',e)}catch(x){}}
})();
