/* Aula Quest 1 · camada visual: cenas do curso (RS) + pessoas realistas (estilo Pocket) em SVG, fundo translúcido, faixas por quadro.
   Não altera a estrutura nem os textos dos 36 quadros. */
(function(){'use strict';
var H=function(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})};
var $=function(s,r){return(r||document).querySelector(s)},$$=function(r,s){return Array.prototype.slice.call(r.querySelectorAll(s))};
var UID=0,SH=['#3b6ea5','#b5543c','#4d8f6b','#7a5fa8','#c58a2f','#2f7f86'];
var ROLE={barista:{apron:'#7a4a2b',shirt:'#f2efe6',prop:'cup'},customer:{},friend:{}};
/* ---------- pessoa de corpo inteiro: cabeça do curso (PogFace) + corpo desenhado em peças ---------- */
var SKINS=['#F8DCC8','#EEC3A0','#D29B73','#A56C47','#6A4228'];
var TOPS=['#3b6ea5','#b5543c','#4d8f6b','#7a5fa8','#c58a2f','#2f7f86','#d9708f','#4a5a8a'];
var PANTS=['#2f3550','#4a3b32','#3b4a63','#6b5d49','#35384a','#27496d'];
var SHOES=['#1d1a22','#5a3a28','#e8e4da','#2c3e50'];
var ROLE={barista:{apron:'#7a4a2b',top:'#f2efe6'},customer:{},friend:{}};
function shade(hex,k){var h=String(hex||'#8a8a8a').replace('#','');if(h.length===3)h=h.replace(/./g,'$&$&');var n=parseInt(h,16),r=(n>>16)&255,g=(n>>8)&255,b=n&255;var f=k<0?0:255,t=Math.abs(k);r=Math.round(r+(f-r)*t);g=Math.round(g+(f-g)*t);b=Math.round(b+(f-b)*t);return '#'+[r,g,b].map(function(x){return x.toString(16).padStart(2,'0')}).join('')}
function person(c){var F=window.PogFace;if(!F||!F.bust)return '';var name=c.n||'x',h=7;for(var i=0;i<name.length;i++)h=(h*31+name.charCodeAt(i))>>>0;
  var g=c.g==='f'?'f':'m',R=ROLE[c.role]||{},tone=c.tone!=null?c.tone:h%4,skin=SKINS[Math.max(0,Math.min(SKINS.length-1,tone|0))];
  var top=c.shirt||R.top||TOPS[h%TOPS.length],pants=c.pants||PANTS[(h>>2)%PANTS.length],shoe=SHOES[(h>>4)%SHOES.length],hair=c.hair||['#4a3228','#2b211c','#7a4a2b','#5b3a29'][h%4];
  var style=c.style||(R.apron?'tee':['tee','hoodie','jacket','shirt','dress'][g==='f'?h%5:h%4]);
  var bo={g:g,tone:tone,style:(g==='f'?['long','wavy','bob','bun']:['short','side','short','curly'])[(h>>3)%4],hair:hair,shirt:top,seed:h,refined:true,natural:true,rich:2,mood:c.mood||'grin',glasses:!!c.glasses,beard:false};
  var k=.19,head='<svg x="-9.5" y="-50.1" width="19" height="24.7" viewBox="0 0 100 130" overflow="hidden">'+F.bust(bo)+'</svg>';
  var dk=shade(top,-.22),lt=shade(top,.18),pdk=shade(pants,-.25),sdk=shade(skin,-.14);
  var S='<ellipse cx="0" cy=".1" rx="10.5" ry="1.7" fill="#000" fill-opacity=".28"/>';
  var legs='',torso='',arms='',extra='';
  var dress=style==='dress'&&g==='f';
  if(dress){var dc=top;legs='<rect x="-3.7" y="-11.5" width="2.5" height="8.6" rx="1.1" fill="'+skin+'"/><rect x="1.2" y="-11.5" width="2.5" height="8.6" rx="1.1" fill="'+skin+'"/>'
     +'<path d="M-4.4 -3 Q-2.6 -1.3 -.4 -3 L-.4 -1.5 Q-3 -.6 -4.8 -1.5Z M.4 -3 Q2.6 -1.3 4.4 -3 L4.8 -1.5 Q3 -.6 .4 -1.5Z" fill="'+shoe+'"/>';
     torso='<path d="M-6.2 -31.6 Q-4 -34.4 0 -34.9 Q4 -34.4 6.2 -31.6 L6.7 -28.8 Q6.4 -25.6 5.2 -22 L9.2 -10.6 Q0 -8.6 -9.2 -10.6 L-5.2 -22 Q-6.4 -25.6 -6.7 -28.8Z" fill="'+dc+'"/><path d="M-5.2 -22 Q0 -20.8 5.2 -22" stroke="'+dk+'" stroke-width=".7" fill="none"/><path d="M-4.2 -19 L-7.6 -10.8 M0 -19.5 L0 -10.4 M4.2 -19 L7.6 -10.8" stroke="'+dk+'" stroke-width=".35" opacity=".6"/>'}
  else{legs='<path d="M-6 -19.4 L-.3 -19.4 L-.7 -3.3 L-5.2 -3.3Z" fill="'+pants+'"/><path d="M.3 -19.4 L6 -19.4 L5.2 -3.3 L.7 -3.3Z" fill="'+pdk+'"/>'
     +'<path d="M-5.4 -3.3 L-.7 -3.3 L-.5 -1.7 Q-3 -.9 -6.2 -1.7Z M.7 -3.3 L5.4 -3.3 L6.2 -1.7 Q3 -.9 .5 -1.7Z" fill="'+shoe+'"/>'
     +'<rect x="-6.1" y="-20.1" width="12.2" height="1.3" fill="'+shade(pants,-.4)+'"/><rect x="-.9" y="-20" width="1.8" height="1.1" fill="#d9c58a"/>';
     var torsoPath='M-6.6 -31.6 Q-4.2 -34.4 0 -34.9 Q4.2 -34.4 6.6 -31.6 L7.1 -28.6 Q7.4 -24.4 6.2 -19.8 L-6.2 -19.8 Q-7.4 -24.4 -7.1 -28.6Z';
     if(style==='hoodie'){torso='<path d="M-3.6 -34.8 Q0 -32 3.6 -34.8 L4.4 -33.4 Q0 -30 -4.4 -33.4Z" fill="'+dk+'"/><path d="'+torsoPath+'" fill="'+top+'"/><path d="M-4.4 -22.6 L4.4 -22.6 L5 -19.8 L-5 -19.8Z" fill="'+dk+'" opacity=".55"/><path d="M-1.3 -32 L-1.6 -26.5 M1.3 -32 L1.6 -26.5" stroke="'+lt+'" stroke-width=".5"/>'}
     else if(style==='jacket'){var inner=shade(top,.55);torso='<path d="'+torsoPath+'" fill="'+inner+'"/><path d="M-6.6 -31.6 Q-4.2 -34.4 -1.6 -34.7 L-1.8 -19.8 L-6.2 -19.8 Q-7.4 -24.4 -7.1 -28.6Z M6.6 -31.6 Q4.2 -34.4 1.6 -34.7 L1.8 -19.8 L6.2 -19.8 Q7.4 -24.4 7.1 -28.6Z" fill="'+shade(top,-.12)+'"/><path d="M-1.6 -33.2 L0 -29 L1.6 -33.2" fill="'+shade(skin,0)+'"/><path d="M-1.8 -33 L-3.3 -29 L-1.7 -28.4Z M1.8 -33 L3.3 -29 L1.7 -28.4Z" fill="'+dk+'"/>'}
     else if(style==='shirt'){torso='<path d="'+torsoPath+'" fill="'+shade(top,.35)+'"/><path d="M-1.8 -33.2 L0 -30.4 L1.8 -33.2 L2.6 -32.6 L0 -28.6 L-2.6 -32.6Z" fill="#fff" opacity=".95"/><path d="M0 -30 L0 -19.8" stroke="'+shade(top,-.2)+'" stroke-width=".4"/><circle cx="0" cy="-26.5" r=".35" fill="'+dk+'"/><circle cx="0" cy="-23.5" r=".35" fill="'+dk+'"/>'}
     else{torso='<path d="'+torsoPath+'" fill="'+top+'"/><path d="M-2.2 -33.6 Q0 -31.4 2.2 -33.6" stroke="'+dk+'" stroke-width=".8" fill="none"/><path d="M-5.6 -27 Q-5 -23 -4.6 -20 M5.6 -27 Q5 -23 4.6 -20" stroke="'+dk+'" stroke-width=".4" fill="none" opacity=".6"/>'}
     if(R.apron){var ap=R.apron;extra='<path d="M-4.4 -30.4 L4.4 -30.4 L5.4 -11.2 L-5.4 -11.2Z" fill="'+ap+'"/><path d="M-3.8 -30.4 L-2 -34 M3.8 -30.4 L2 -34" stroke="'+shade(ap,-.3)+'" stroke-width=".7"/><rect x="-2.5" y="-24" width="5" height="3.4" rx=".5" fill="'+shade(ap,-.2)+'"/><path d="M-5.4 -11.2 L5.4 -11.2" stroke="'+shade(ap,-.35)+'" stroke-width=".5"/>'}}
  var sl=style==='dress'||style==='jacket'||style==='shirt'?top:top,short=style==='tee'||dress||R.apron;
  var pose=c.pose||['rest','talk','hold','pocket','rest','talk'][(h>>6)%6];
  var armOf=function(sx){var sc=sx<0?top:shade(top,-.1),side=sx>0,ex,ey,hx,hy,hid=false,sh=sx*6.1;
    if(pose==='talk'&&side){ex=10.6;ey=-26.4;hx=11.2;hy=-32.6}
    else if(pose==='wave'&&side){ex=11;ey=-30;hx=12.2;hy=-38.4}
    else if(pose==='hold'){ex=sx*8;ey=-24.6;hx=sx*1.5;hy=-23.4}
    else if(pose==='pocket'&&!side){ex=-9.1;ey=-25.6;hx=-5.6;hy=-20.4;hid=true}
    else{ex=sx*8.7;ey=-25;hx=sx*7.5;hy=-19.4}
    var tw=short?2.3:3;
    var up='<path d="M'+sh+' -31.3 Q'+((sh+ex)/2+sx*.7)+' '+((-31.3+ey)/2-.4)+' '+ex+' '+ey+'" stroke="'+sc+'" stroke-width="3.1" fill="none" stroke-linecap="round"/>';
    var low='<path d="M'+ex+' '+ey+' L'+hx+' '+hy+'" stroke="'+(short?skin:sc)+'" stroke-width="'+tw+'" fill="none" stroke-linecap="round"/>';
    var cuff=short?'':'<circle cx="'+(hx*.94+ex*.06)+'" cy="'+(hy*.94+ey*.06)+'" r="1.3" fill="'+shade(sc,-.18)+'"/>';
    var hand=hid?'':'<ellipse cx="'+hx+'" cy="'+(hy+(hy<-28?-.7:.5))+'" rx="1.25" ry="1.6" fill="'+skin+'"/><path d="M'+(hx-sx*.6)+' '+(hy-.3)+' q'+(sx*-.5)+' .9 '+(sx*-.2)+' 1.5" stroke="'+sdk+'" stroke-width=".25" fill="none" opacity=".7"/>';
    var pit='<path d="M'+(sx*6.3)+' -29.2 Q'+(sx*7)+' -26.5 '+(sx*6.4)+' -23.6" stroke="'+shade(top,-.3)+'" stroke-width=".45" fill="none" opacity=".5"/>';
    return up+low+cuff+pit+hand};
  arms=armOf(-1)+armOf(1);
  var neck='<rect x="-1.7" y="-36.2" width="3.4" height="3.6" fill="'+sdk+'"/>';
  var pr=c.prop||R.prop,prop=pr==='cup'?'<g transform="translate(10.2 -19.4)"><path d="M-1.9 -2 L1.9 -2 L1.4 2.6 L-1.4 2.6Z" fill="#f6f1e6" stroke="#bda98a" stroke-width=".25"/><rect x="-2.1" y="-2.6" width="4.2" height="1" rx=".4" fill="#7a4a2b"/><rect x="-1.6" y="-.8" width="3.2" height="1.1" fill="#c58a2f" opacity=".85"/></g>':pr==='phone'?'<g transform="translate(9.8 -20)"><rect x="-1.6" y="-2.6" width="3.2" height="5.2" rx=".6" fill="#2b3550"/><rect x="-1.3" y="-2.2" width="2.6" height="4.2" fill="#9cd3f0"/></g>':pr==='bag'?'<g transform="translate(10 -17)"><rect x="-2.6" y="-2.2" width="5.2" height="5.4" rx=".7" fill="#c58a2f"/><path d="M-1.5 -2.2 Q0 -4.6 1.5 -2.2" stroke="#8a5f1e" fill="none" stroke-width=".45"/></g>':'';
  return '<svg class="qp-fig" viewBox="-14 -50.5 28 53" preserveAspectRatio="xMidYMax meet" aria-hidden="true">'+S+legs+neck+head+torso+extra+arms+prop+'</svg>'}
function stage(a,h){if(!a||!a.rs)return '';var bk='';try{bk=window.RS&&RS[a.rs]?RS[a.rs]('l1'+(++UID)):''}catch(e){}
  var pp=(a.cast||[]).map(function(c){return '<span class="qp'+(c.flip?' fl':'')+'" style="left:'+(c.x==null?50:c.x)+'%;--s:'+(c.s||1)+'">'+person(c)+'</span>'}).join('');
  return '<div class="ps-stage '+(h||'scene')+'"><div class="ps-stage-bk">'+bk+'</div><div class="ps-chars">'+pp+'</div></div>'}
var ANA=function(x,fl,o){return Object.assign({n:'Ana',g:'f',role:'customer',x:x,flip:fl||0},o||{})},EV=function(x,fl,o){return Object.assign({n:'Evan',g:'m',role:'barista',x:x,flip:fl==null?1:fl},o||{})},FR=function(n,g,x,fl){return{n:n,g:g,role:'friend',x:x,flip:fl||0}};
/* uma cena por quadro (36), variando o cenário; só repete quando a cena precisa voltar */
var ART=[
 {rs:'cafe',cast:[ANA(30),EV(70,1,{prop:'cup'})]},
 {rs:'cafe3',cast:[ANA(30),FR('Leo','m',70,1)]},
 {rs:'cafe2',cast:[EV(70)]},{rs:'bakery',cast:[ANA(30),EV(72)]},
 {pair:[{rs:'bakery',cast:[FR('Lia','f',50)]},{rs:'cafe',cast:[ANA(50)]}]},
 {rs:'cafe2',cast:[EV(74)]},{rs:'cafe3',cast:[ANA(30)]},
 {rs:'cafe',cast:[ANA(28),FR('Leo','m',66,1)]},
 {rs:'nyc',cast:[ANA(48)]},{rs:'cafe2',cast:[ANA(30),EV(70,1)]},{rs:'cafe3',cast:[ANA(30,0,{prop:'cup'}),EV(70,1)]},
 {rs:'cafe',cast:[ANA(50)]},{rs:'cafe2',cast:[EV(50)]},{rs:'park2',cast:[ANA(50,0,{prop:'cup'})]},{rs:'cafe3',cast:[ANA(30),EV(70,1)]},{rs:'nyc',cast:[ANA(50)]},
 {rs:'cafe',cast:[ANA(30),EV(70,1)]},{rs:'cafe2',cast:[ANA(30),EV(70,1)]},
 {rs:'cafe',cast:[ANA(30),EV(70,1)]},{rs:'cafe2',cast:[ANA(30),EV(70,1,{prop:'cup'})]},{rs:'cafe3',cast:[ANA(30),EV(70,1)]},{rs:'bakery',cast:[ANA(30),EV(72,1)]},{rs:'cafe2',cast:[ANA(30),EV(70,1,{prop:'cup'})]},{rs:'cafe',cast:[ANA(30),EV(70,1)]},
 {rs:'bakery',cast:[ANA(30),EV(72,1)]},{rs:'cafe2',cast:[ANA(30),EV(70,1,{prop:'cup'})]},
 {rs:'cafe',cast:[ANA(30),EV(70,1)]},{rs:'cafe3',cast:[ANA(30),EV(70,1)]},
 {rs:'park2',cast:[ANA(50,0,{prop:'cup'})]},
 {rs:'cafe2',cast:[ANA(30),FR('Sam','m',70,1)]},{rs:'cafe',cast:[ANA(30),EV(70,1)]},
 {rs:'cafe3',cast:[ANA(28),EV(72,1)]},
 {rs:'home1',cast:[ANA(50,0,{prop:'phone'})]},{rs:'home1',cast:[ANA(50,0,{prop:'phone'})]},
 {rs:'park',cast:[ANA(38,0,{prop:'cup'}),FR('Sam','m',66,1)]},{rs:'cafe',cast:[ANA(32),EV(68,1,{prop:'cup'})]}];
window.L1VIS={person:person,stage:stage,art:ART,H:H,$:$,$$:$$,ANA:ANA,EV:EV,FR:FR,toast:function(t){var el=document.createElement('div');el.className='q1v-toast';el.textContent=t;document.body.appendChild(el);setTimeout(function(){el.classList.add('out')},1800);setTimeout(function(){el.remove()},2300)}};
/* ---------- decoração por quadro: painel de cena nítido ao lado do conteúdo ---------- */
var W=[50,46,42,38,34,30],HH=[30,27,24,21,18,15];
function fit(b){if(!b||!b.isConnected)return;b.classList.remove('q1v-tight','q1v-nohero');if(window.matchMedia&&matchMedia('(max-width:820px)').matches){b.scrollTop=0;return}
  function set(i){b.style.setProperty('--q1w',W[i]);b.style.setProperty('--q1h',HH[i])}
  function over(){return b.scrollHeight-b.clientHeight>2}
  var i=0;set(0);for(i=0;i<W.length&&over();i++)set(i);
  if(over()){b.classList.add('q1v-tight');for(i=0;i<W.length&&over();i++)set(i)}
  if(over())b.classList.add('q1v-nohero')}
function heroEl(art,h){var a=art.pair?art.pair[1]:art;var d=document.createElement('div');d.className='q1v-hero';d.innerHTML=stage(a,h||'scene');return d}
/* coluna esquerda = cena; direita = conteúdo original */
function split(b,art,side){var main=document.createElement('div');main.className='q1v-main';while(b.firstChild)main.appendChild(b.firstChild);
  var sp=document.createElement('div');sp.className='q1v-split'+(side==='right'?' right':'');var hero=heroEl(art);
  if(side==='right'){sp.appendChild(main);sp.appendChild(hero)}else{sp.appendChild(hero);sp.appendChild(main)}
  b.appendChild(sp);return{split:sp,hero:hero,main:main}}
var SPLIT_KINDS={facts:1,artifact:1,quiz:1,exit:1};
function themeSvg(em,n){var s=n*7919+13;function r(){s=(s*9301+49297)%233280;return s/233280}var out='<svg viewBox="0 0 1600 900" preserveAspectRatio="xMidYMid slice" aria-hidden="true">',k=0;for(var y=60;y<920;y+=135)for(var x=(Math.floor(y/135)%2?30:100);x<1640;x+=190){var e=em[k++%em.length],sz=40+Math.floor(r()*22),rot=Math.floor(r()*50-25);out+='<text x="'+Math.round(x+r()*40)+'" y="'+Math.round(y+r()*30)+'" font-size="'+sz+'" transform="rotate('+rot+' '+x+' '+y+')" opacity=".26">'+e+'</text>'}return out+'</svg>'}
function applyTheme(A){var L=A.lesson&&A.lesson(),th=L&&L.theme,st=$('#stage');if(!th||!st)return;st.style.setProperty('--ta',th.a);st.style.setProperty('--tb',th.b);var old=$('.q1v-theme',st);if(old)old.remove();var d=document.createElement('div');d.className='q1v-theme';d.innerHTML=themeSvg(th.emojis,L.n);st.insertBefore(d,st.firstChild)}
function react(b){var hero=$('.q1v-hero',b);if(!hero)return;$$(b,'[data-answer],[data-choice]').forEach(function(x){x.addEventListener('click',function(){setTimeout(function(){var good=x.classList.contains('right'),d=$('.q1v-react',hero);if(!d){d=document.createElement('div');hero.appendChild(d)}d.className='q1v-react '+(good?'ok':'no');d.textContent=good?['🎉 Isso!','👏 Muito bem!','✨ Perfeito!'][Math.floor(Math.random()*3)]:'🤔 Quase! Veja o porquê.'},30)})})}
var DECOR={};window.L1DECOR=DECOR;
var previous=window.RL_REGISTER;
window.RL_REGISTER=function(R,A){if(previous)previous(R,A);var orig=R.q1;if(!orig)return;
 R.q1=function(p,b){try{b.scrollTop=0}catch(z){}try{orig(p,b)}catch(err){if(!DECOR[p.kind])throw err}var art=p.art||ART[p._i]||ART[0];try{
   b.classList.add('q1v');
   var hero=$('.q1-art',b);
   if(hero&&(p.kind==='cover'||p.kind==='work'||p.kind==='finish')){var d=heroEl(art,'cover');hero.replaceWith(d)}
   else if(DECOR[p.kind])DECOR[p.kind](p,b,art,A);
   else if(p.kind==='reading'){var side=$('.q1-reading-side',b);if(side){var col=document.createElement('div');col.className='q1v-col';side.replaceWith(col);col.appendChild(heroEl(art));col.appendChild(side)}}
   else if(p.kind==='compare'){var row=document.createElement('div');row.className='q1v-pairrow';row.innerHTML='<div><span>Brasil</span>'+stage(art.pair[0],'scene')+'</div><div><span>Estados Unidos</span>'+stage(art.pair[1],'scene')+'</div>';var f=$('.q1-facts',b);b.insertBefore(row,f)}
   else if(SPLIT_KINDS[p.kind])split(b,art);
   if(p.kind==='quiz'||p.kind==='choice')react(b);
   applyTheme(A);
  }catch(e){console.error(e)}
  setTimeout(function(){fit(b)},60);setTimeout(function(){fit(b)},400)}};
window.L1FIT=fit;window.L1SPLIT=split;window.L1HERO=heroEl;
addEventListener('resize',function(){var b=$('.pb.q1v');if(b)fit(b)});
document.addEventListener('fullscreenchange',function(){setTimeout(function(){var b=$('.pb.q1v');if(b)fit(b)},250)});
})();
