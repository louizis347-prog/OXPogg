/* Aula Quest 1 · camada visual: cenas do curso (RS) + pessoas realistas (estilo Pocket) em SVG, fundo translúcido, faixas por quadro.
   Não altera a estrutura nem os textos dos 36 quadros. */
(function(){'use strict';
var H=function(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})};
var $=function(s,r){return(r||document).querySelector(s)},$$=function(r,s){return Array.prototype.slice.call(r.querySelectorAll(s))};
var UID=0,SH=['#3b6ea5','#b5543c','#4d8f6b','#7a5fa8','#c58a2f','#2f7f86'];
var ROLE={barista:{apron:'#7a4a2b',shirt:'#f2efe6',prop:'cup'},customer:{},friend:{}};
/* ---------- pessoa de corpo inteiro ---------- */
function person(c){var F=window.PogFace;if(!F||!F.bust)return '';var name=c.n||'x',h=7;for(var i=0;i<name.length;i++)h=(h*31+name.charCodeAt(i))>>>0;
  var g=c.g==='f'?'f':'m',R=ROLE[c.role]||{},col=c.shirt||R.shirt||SH[h%SH.length],hair=c.hair||['#4a3228','#2b211c','#7a4a2b','#5b3a29'][h%4];
  var bo={g:g,tone:c.tone!=null?c.tone:h%4,style:(g==='f'?['long','wavy','bob','bun']:['short','side','short','curly'])[(h>>3)%4],hair:hair,shirt:col,seed:h,refined:true,natural:true,rich:2,mood:c.mood||'grin',glasses:!!c.glasses,beard:false};
  var k=.2,by=-17-120*k,pants=c.pants||['#2f3550','#4a3b32','#3b4a63','#35384a'][h%4],pd='#20263a';
  var face='<svg x="'+(-46*k).toFixed(2)+'" y="'+by.toFixed(2)+'" width="'+(92*k).toFixed(2)+'" height="'+(120*k).toFixed(2)+'" viewBox="4 6 92 120" overflow="hidden">'+F.bust(bo)+'</svg>';
  var arm=function(sx,cl){return '<path d="M'+(sx*7.4)+' '+(by+88*k).toFixed(2)+' Q'+(sx*9.3)+' -20 '+(sx*8.7)+' -12.5" stroke="'+cl+'" stroke-width="2.4" fill="none" stroke-linecap="round"/><ellipse cx="'+(sx*8.7)+'" cy="-10.8" rx="1.25" ry="1.6" fill="#e6b896"/>'};
  var apron=R.apron?'<path d="M-4.7 -27.5 L4.7 -27.5 L5.6 -17.2 L-5.6 -17.2Z" fill="'+R.apron+'"/><path d="M-4 -27.5 L-2.2 -31 M4 -27.5 L2.2 -31" stroke="'+R.apron+'" stroke-width=".7"/>':'';
  var pr=c.prop||R.prop,prop=pr==='cup'?'<g transform="translate(9.6 -13)"><path d="M-1.9 -1.6 L1.9 -1.6 L1.4 2.4 L-1.4 2.4Z" fill="#f6f1e6" stroke="#bda98a" stroke-width=".25"/><rect x="-2.1" y="-2.1" width="4.2" height=".8" fill="#7a4a2b"/></g>':pr==='phone'?'<g transform="translate(9.4 -14)"><rect x="-1.5" y="-2.4" width="3" height="4.8" rx=".5" fill="#2b3550"/><rect x="-1.2" y="-2" width="2.4" height="3.8" fill="#9cd3f0"/></g>':'';
  return '<svg class="qp-fig" viewBox="-14 -48 28 50" preserveAspectRatio="xMidYMax meet" aria-hidden="true"><ellipse cx="0" cy=".2" rx="11" ry="1.9" fill="#000" fill-opacity=".3"/><path d="M-6.2 -17.5 L-5.6 -2.4 L-.6 -2.4 L-.4 -17.5Z" fill="'+pants+'"/><path d="M.4 -17.5 L.6 -2.4 L5.6 -2.4 L6.2 -17.5Z" fill="'+pd+'"/><path d="M-6.4 -3 Q-3.4 -4.4 -.5 -3 L-.5 -1.2 L-6.8 -1.2Z M.5 -3 Q3.4 -4.4 6.4 -3 L6.8 -1.2 L.5 -1.2Z" fill="#15151c"/>'+face+arm(-1,col)+arm(1,'#00000033')+apron+prop+'</svg>'}
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
var W=[44,40,36,32,28,24],HH=[26,22,18,15,12,9];
function fit(b){if(!b||!b.isConnected)return;b.classList.remove('q1v-tight','q1v-nohero');
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
var DECOR={};window.L1DECOR=DECOR;
var previous=window.RL_REGISTER;
window.RL_REGISTER=function(R,A){if(previous)previous(R,A);var orig=R.q1;if(!orig)return;
 R.q1=function(p,b){orig(p,b);var art=ART[p._i]||ART[0];try{
   b.classList.add('q1v');
   var hero=$('.q1-art',b);
   if(hero&&(p.kind==='cover'||p.kind==='work'||p.kind==='finish')){var d=heroEl(art,'cover');hero.replaceWith(d)}
   else if(DECOR[p.kind])DECOR[p.kind](p,b,art,A);
   else if(p.kind==='reading'){var side=$('.q1-reading-side',b);if(side){var col=document.createElement('div');col.className='q1v-col';side.replaceWith(col);col.appendChild(heroEl(art));col.appendChild(side)}}
   else if(p.kind==='compare'){var row=document.createElement('div');row.className='q1v-pairrow';row.innerHTML='<div><span>Brasil</span>'+stage(art.pair[0],'scene')+'</div><div><span>Estados Unidos</span>'+stage(art.pair[1],'scene')+'</div>';var f=$('.q1-facts',b);b.insertBefore(row,f)}
   else if(SPLIT_KINDS[p.kind])split(b,art);
  }catch(e){console.error(e)}
  setTimeout(function(){fit(b)},60);setTimeout(function(){fit(b)},400)}};
window.L1FIT=fit;window.L1SPLIT=split;window.L1HERO=heroEl;
addEventListener('resize',function(){var b=$('.pb.q1v');if(b)fit(b)});
document.addEventListener('fullscreenchange',function(){setTimeout(function(){var b=$('.pb.q1v');if(b)fit(b)},250)});
})();
