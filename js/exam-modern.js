/* Pogglot · Simulados e testes no layout moderno: faixa ilustrada (cenário refinado), selo do exame,
   contador de questões e cartões de resposta com letras. Só envolve renderTest; a lógica não muda. */
(function(){
'use strict';
var SCENES=['classroom','library','office','lobby','plaza','cafe'];
var esc=function(s){return String(s==null?'':s).replace(/[&<>"']/g,function(m){return({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'})[m]})};
function hash(s){var h=0;s=String(s);for(var i=0;i<s.length;i++)h=(h*31+s.charCodeAt(i))|0;return Math.abs(h)}
function badge(){
  try{var t=P.test.t||'';return t}catch(e){return ''}}
function banner(){
  var q=P.i+1,n=P.total,pct=Math.round((P.i/n)*100),h=hash(P.cid+(P.test&&P.test.id)),sc=SCENES[(h+((P.i/10)|0))%SCENES.length],art='';
  try{if(window.PogScene)art=PogScene.wide({sc:sc,t:badge(),n:h%997,a:{w:badge()||P.cid,d:''}},{})}catch(e){art=''}
  return '<div class="xm-hero">'+(art?'<div class="xm-art">'+art+'</div>':'')+
    '<div class="xm-shade"></div><div class="xm-top"><span class="xm-tag">🎓 '+esc(badge())+'</span><span class="xm-count"><b>'+q+'</b>/'+n+'</span></div>'+
    '<div class="xm-bar"><i style="width:'+pct+'%"></i></div></div>'}
function decorate(){
  var pl=document.getElementById('player');if(!pl||typeof P==='undefined'||!P||!P.isTest)return;
  pl.classList.add('exam-modern');
  var st=document.getElementById('pstage'),step=st&&st.querySelector('.step');if(!step||step.classList.contains('done')||step.querySelector('.xm-hero'))return;
  if(P.i>=P.total)return;
  step.insertAdjacentHTML('afterbegin',banner());
  var opts=step.querySelectorAll('.opt');opts.forEach(function(b,i){if(!b.querySelector('.xm-l'))b.insertAdjacentHTML('afterbegin','<span class="xm-l">'+String.fromCharCode(65+i)+'</span>')})}
var r0=window.renderTest;
if(typeof r0==='function'){window.renderTest=function(){var r=r0.apply(this,arguments);try{decorate()}catch(e){console.error('exam-modern',e)}return r}}
})();
