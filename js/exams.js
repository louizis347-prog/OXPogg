/* Pogglot · Simulados de exame: prova cronometrada montada com o conteúdo do curso (inspirada em DELF, DELE, JLPT, Goethe...). */
(function(){
'use strict';
var esc=function(s){return String(s==null?'':s).replace(/[&<>"']/g,function(m){return({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'})[m]})};
var EXAM={fr:'DELF',es:'DELE',de:'Goethe-Zertifikat',it:'CELI',ja:'JLPT',en:'Cambridge/TOEFL',pt:'Celpe-Bras'};
var JLPT={a1:'N5',a2:'N4',b1:'N3',b2:'N2',c1:'N1',c2:'N1'};
var MIN={a1:30,a2:40,b1:60,b2:80,c1:100,c2:120};
var store;
function info(cid){var m=/^(?:nb)?([a-z]{2})(?:-(a1|a2|b1|b2|c1|c2))?/.exec(cid||'')||[],lg=m[1]||'en',lv=m[2]||'a1';
  var nm=lg==='ja'?EXAM.ja+' '+JLPT[lv]:EXAM[lg]+' '+lv.toUpperCase();return{name:nm,min:MIN[lv]||30,lv:lv}}
function realCount(cid){return((typeof EP!=='undefined'&&EP[cid])||[]).filter(function(e){return!isPlannedEpisode(e)&&!e.rev}).length}
function card(cid){var i=info(cid),b=store('exam:'+cid);
  var best=b?'<small>Melhor nota: <b>'+b.pct+'%</b> · '+esc(b.date)+'</small>':'<small>'+i.min+' min · 40 questões · aprovação 60%</small>';
  return '<section class="exam-card" role="region" aria-label="Simulado"><div class="ex-i">🎓</div><div class="ex-t"><b>Simulado '+esc(i.name)+'</b>'+best+'</div><button class="ex-b" id="ex-go">Começar</button></section>'}
store=function(k,v){try{if(v===undefined)return JSON.parse(localStorage.getItem('pogglot:'+k)||'null');localStorage.setItem('pogglot:'+k,JSON.stringify(v))}catch(e){return null}};
function start(cid){
  if(typeof playTest!=='function')return;
  var i=info(cid);playTest(cid,'exam');
  if(typeof P==='undefined'||!P||!P.isTest||P.test.id!=='exam')return;
  clearInterval(P.timer);P.limit=i.min*60;P.test.t='Simulado '+i.name;
  var tick=function(){var left=Math.max(0,P.limit-(((Date.now()-P.t0)/1000)|0)),el=document.getElementById('ptime');
    if(el){el.textContent='⏳ '+(left/60|0)+':'+String(left%60).padStart(2,'0');el.classList.toggle('warn',left<300)}
    if(left<=0){clearInterval(P.timer);if(P.i<P.total){P.i=P.total;render()}}};
  P.timer=setInterval(tick,1000);tick()}
function mount(cid){
  if(realCount(cid)<8||document.querySelector('.exam-card'))return;
  var host=document.querySelector('.p2tools')||document.querySelector('main.wrap .road')||document.querySelector('main.wrap');if(!host)return;
  host.insertAdjacentHTML(host.matches('.p2tools,.road')?'beforebegin':'afterbegin',card(cid));
  var b=document.getElementById('ex-go');if(b)b.onclick=function(){
    var i=info(cid);if(confirm('Simulado '+i.name+'\n\n40 questões em '+i.min+' minutos. O tempo corre sem pausa. Boa prova!'))start(cid)}}
var _c=window.course;
if(typeof _c==='function')window.course=function(id){var r=_c.apply(this,arguments);try{mount(id)}catch(e){console.error('exam',e)}return r};
/* guarda a melhor nota ao terminar */
var _r=window.renderTest;
if(typeof _r==='function')window.renderTest=function(){var r=_r.apply(this,arguments);
  try{if(typeof P!=='undefined'&&P&&P.isTest&&P.test&&P.test.id==='exam'&&P.i>=P.total&&!P.saved){P.saved=1;var pct=Math.round(P.score/P.total*100),o=store('exam:'+P.cid);
    if(!o||pct>o.pct)store('exam:'+P.cid,{pct:pct,date:new Date().toLocaleDateString('pt-BR')});
    var rc=document.querySelector('.step.done .recap');if(rc){var i=info(P.cid),sec=Math.round((Date.now()-P.t0)/1000);
      rc.insertAdjacentHTML('afterbegin','<p><b>Nota estimada: '+Math.round(pct)+'/100</b> · tempo usado: '+(sec/60|0)+' min '+(sec%60)+' s de '+i.min+' min. Esta é uma prova de treino com o conteúdo do curso, não o exame oficial.</p>')}}}catch(e){}
  return r};
window.PogExam={start:start,info:info};
})();
