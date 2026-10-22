/* Pogglot · "Revisar hoje": revisão espaçada diária de palavras e expressões (as mesmas do painel Meu vocabulário).
 * Usa o baralho ST.srs (caixas de Leitner: 1, 3, 7, 14, 30 e 60 dias). Cartões de expressão entram aos poucos (cerca de 15 por dia). */
(function(){
'use strict';
var T={
 pt:{title:'Revisar hoje',due:'para revisar hoje',words:'palavras',expr:'expressões',start:'Começar',startN:function(n){return 'Começar ('+n+')'},none:'Nada para revisar agora. Volte amanhã!',noDeck:'Conclua episódios para montar seu baralho de revisão.',
  all:'Todos',size:'Por sessão',streak:'dias seguidos revisando',doneToday:'revisados hoje',forecast:'Próximos 7 dias',boxes:'Seu baralho por caixa',deck:'cartões no baralho',
  show:'Mostrar resposta',again:'Errei',hard:'Difícil',good:'Acertei',listen:'Ouvir',q1:'O que significa?',q2:'Como se diz?',box:'Caixa',of:'de',close:'Fechar',finish:'Revisão concluída!',acc:'Acertos',xp:'XP',
  tip:'Errou? O cartão volta hoje. Acertou? Volta em 1, 3, 7, 14, 30 e 60 dias.',loading:'Montando seu baralho…',next:'Próxima revisão',tomorrow:'amanhã',inDays:function(n){return 'em '+n+' dias'},kb:'Atalhos: 1 errei · 2 difícil · 3 acertei · espaço mostra',
  bonus:'Meta do dia cumprida!',wk:['dom','seg','ter','qua','qui','sex','sáb'],today:'hoje',newCards:'cartões novos de expressões chegam a cada dia'},
 es:{title:'Repasar hoy',due:'para repasar hoy',words:'palabras',expr:'expresiones',start:'Empezar',startN:function(n){return 'Empezar ('+n+')'},none:'Nada para repasar ahora. ¡Vuelve mañana!',noDeck:'Completa episodios para armar tu mazo de repaso.',
  all:'Todos',size:'Por sesión',streak:'días seguidos repasando',doneToday:'repasados hoy',forecast:'Próximos 7 días',boxes:'Tu mazo por caja',deck:'tarjetas en el mazo',
  show:'Mostrar respuesta',again:'Fallé',hard:'Difícil',good:'Acerté',listen:'Escuchar',q1:'¿Qué significa?',q2:'¿Cómo se dice?',box:'Caja',of:'de',close:'Cerrar',finish:'¡Repaso completado!',acc:'Aciertos',xp:'XP',
  tip:'¿Fallaste? La tarjeta vuelve hoy. ¿Acertaste? Vuelve en 1, 3, 7, 14, 30 y 60 días.',loading:'Armando tu mazo…',next:'Próximo repaso',tomorrow:'mañana',inDays:function(n){return 'en '+n+' días'},kb:'Atajos: 1 fallé · 2 difícil · 3 acerté · espacio muestra',
  bonus:'¡Meta del día cumplida!',wk:['dom','lun','mar','mié','jue','vie','sáb'],today:'hoy',newCards:'cada día llegan tarjetas nuevas de expresiones'}
};
function L(){try{return ST.homeLang==='es'?'es':'pt'}catch(e){return'pt'}}
function t(k){return T[L()][k]!=null?T[L()][k]:T.pt[k]}
function E(s){return String(s==null?'':s).replace(/[&<>"']/g,function(m){return({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'})[m]})}
var RV='pogglot:rv';
function rvGet(){try{return JSON.parse(localStorage.getItem(RV)||'{}')||{}}catch(e){return{}}}
function rvSet(v){try{localStorage.setItem(RV,JSON.stringify(v))}catch(e){}}
function streakNow(){var r=rvGet(),d=srsToday();return(r.day===d||r.day===d-1)?(r.streak||0):0}
function doneToday(){var r=rvGet();return r.day===srsToday()?(r.n||0):0}
function kindOf(c){return c.t==='x'?'x':'w'}
/* ---------- expressões entram no baralho aos poucos ---------- */
function addExpr(cid,e){var n=0;if(!window.PogVocab||!PogVocab.extract)return 0;
  PogVocab.extract(e,function(kind,a,b){if(kind!=='x'||!a||a.length>90)return;
    if((String(a).match(/[\p{L}\p{N}]+/gu)||[]).length<2)return;
    var k=srsKey(cid,a);if(ST.srs[k])return;
    ST.srs[k]={w:a,m:b,d:'',c:cid,b:0,due:srsToday()+Math.floor(NEWQ.i++/15),ep:e.n,t:'x'};n++});return n}
var NEWQ={i:0};
function backfillExpr(){NEWQ.i=0;var n=0;try{
  var pend=Object.keys(ST.srs).filter(function(k){return ST.srs[k].t==='x'&&ST.srs[k].due>srsToday()}).length;NEWQ.i=pend;
  Object.keys(COURSES).forEach(function(cid){var eps=EP[cid];if(!eps||!eps.length)return;
    eps.forEach(function(e){if(isPlannedEpisode(e)||e.rev||!ST.done[cid+'-'+e.n])return;n+=addExpr(cid,e)})});
  if(n)save()}catch(err){}return n}
async function prepare(){
  var cs=Object.keys(COURSES).filter(function(c){return doneCountFor(c)>0});
  await Promise.all(cs.map(function(c){return typeof ensureLangLoaded==='function'?ensureLangLoaded(c):0}));
  var before={};Object.keys(ST.srs).forEach(function(k){before[k]=1});
  try{srsBackfill()}catch(e){}
  var fresh=Object.keys(ST.srs).filter(function(k){return!before[k]});
  if(fresh.length>20){fresh.forEach(function(k,i){ST.srs[k].due=srsToday()+Math.floor(i/15)});save()}   /* baralho antigo entra aos poucos */
  backfillExpr()}
/* ---------- consultas ---------- */
function dueCards(course){var d=srsToday();
  return Object.keys(ST.srs).filter(function(k){var c=ST.srs[k];return c.due<=d&&(!course||c.c===course)}).map(function(k){return{k:k,c:ST.srs[k]}})
   .sort(function(a,b){return a.c.due-b.c.due||a.c.b-b.c.b})}
function mix(list,n){var w=list.filter(function(x){return kindOf(x.c)==='w'}),x=list.filter(function(x){return kindOf(x.c)==='x'}),out=[],i=0;
  while(out.length<n&&(w.length||x.length)){if(i%2===0&&w.length)out.push(w.shift());else if(x.length)out.push(x.shift());else out.push(w.shift());i++}return out}
function forecast(){var d=srsToday(),f=[0,0,0,0,0,0,0];Object.keys(ST.srs).forEach(function(k){var x=ST.srs[k].due-d;if(x>=1&&x<=7)f[x-1]++});return f}
function boxes(){var b=[0,0,0,0,0,0,0];Object.keys(ST.srs).forEach(function(k){b[Math.min(6,ST.srs[k].b||0)]++});return b}
function flagOf(cid){var c=COURSES[cid]||{};return c.flag||cid}
function roma(s,cid){try{return window.PogRomaji&&/^ja/.test((COURSES[cid]||{}).tts||'')?PogRomaji.conv(s):''}catch(e){return''}}
/* ---------- tela ---------- */
var st={course:'',size:20};
function shell(){var old=document.getElementById('rvw');if(old)old.remove();
  var el=document.createElement('div');el.id='rvw';el.className='rvw';el.setAttribute('role','dialog');el.setAttribute('aria-modal','true');el.setAttribute('aria-label',t('title'));
  document.body.appendChild(el);document.body.style.overflow='hidden';return el}
function close(){var el=document.getElementById('rvw');if(el)el.remove();document.body.style.overflow='';document.removeEventListener('keydown',onKey);
  try{var cur=ST.lastCourse;if(document.querySelector('.p2tools')&&cur&&EP[cur])course(cur);else home()}catch(e){}}
var onKey=function(){};
async function open(){
  var el=shell();el.innerHTML='<div class="rv-card"><div class="rv-h"><h2>🔁 '+E(t('title'))+'</h2><button class="rv-x" aria-label="'+E(t('close'))+'">×</button></div><p class="rv-sub">'+E(t('loading'))+'</p></div>';
  el.querySelector('.rv-x').onclick=close;
  await prepare();dash(el)}
function dash(el){
  var tot=Object.keys(ST.srs).length,all=dueCards(''),courses={};Object.keys(ST.srs).forEach(function(k){courses[ST.srs[k].c]=1});
  var list=dueCards(st.course),w=list.filter(function(x){return kindOf(x.c)==='w'}).length,x=list.length-w,n=Math.min(st.size,list.length);
  var f=forecast(),mx=Math.max.apply(null,f.concat([1])),bx=boxes(),bm=Math.max.apply(null,bx.concat([1])),wd=new Date(),days=[];
  for(var i=0;i<7;i++){var dd=new Date(wd.getTime()+(i+1)*864e5);days.push(t('wk')[dd.getDay()])}
  var cc=Object.keys(courses);
  el.innerHTML='<div class="rv-card"><div class="rv-h"><h2>🔁 '+E(t('title'))+'</h2><button class="rv-x" aria-label="'+E(t('close'))+'">×</button></div>'+
   (!tot?'<p class="rv-sub">'+E(t('noDeck'))+'</p>':
   '<div class="rv-hero"><div class="rv-ring" style="--p:'+(all.length?Math.min(100,doneToday()/(doneToday()+all.length)*100):100)+'"><b>'+list.length+'</b><small>'+E(t('due'))+'</small></div><div class="rv-meta"><span>📖 '+w+' '+E(t('words'))+'</span><span>💬 '+x+' '+E(t('expr'))+'</span><span>🔥 '+streakNow()+' '+E(t('streak'))+'</span><span>✅ '+doneToday()+' '+E(t('doneToday'))+'</span></div></div>'+
   (cc.length>1?'<div class="rv-chips" id="rv-c"><button class="pg-chip" data-c="" aria-pressed="'+(!st.course)+'">'+E(t('all'))+'</button>'+cc.map(function(c){return '<button class="pg-chip" data-c="'+E(c)+'" aria-pressed="'+(st.course===c)+'">'+E(flagOf(c))+'</button>'}).join('')+'</div>':'')+
   '<div class="rv-chips" id="rv-s"><span>'+E(t('size'))+':</span>'+[10,20,40].map(function(v){return '<button class="pg-chip" data-s="'+v+'" aria-pressed="'+(st.size===v)+'">'+v+'</button>'}).join('')+'</div>'+
   (n?'<button class="pg-btn rv-go" id="rv-go">'+E(t('startN')(n))+'</button>':'<p class="rv-sub">'+E(t('none'))+'</p>')+
   '<h4 class="rv-h4">'+E(t('forecast'))+'</h4><div class="rv-fc">'+f.map(function(v,i){return '<div><i style="height:'+Math.max(4,Math.round(v/mx*54))+'px"></i><b>'+v+'</b><small>'+E(days[i])+'</small></div>'}).join('')+'</div>'+
   '<h4 class="rv-h4">'+E(t('boxes'))+' · '+tot+' '+E(t('deck'))+'</h4><div class="rv-bx">'+bx.map(function(v,i){return '<div><i style="width:'+Math.max(3,Math.round(v/bm*100))+'%"></i><small>'+(i+1)+'</small><b>'+v+'</b></div>'}).join('')+'</div>'+
   '<p class="rv-note">'+E(t('tip'))+' '+E(t('newCards'))+'.</p>')+'</div>';
  el.querySelector('.rv-x').onclick=close;
  var cb=el.querySelector('#rv-c');if(cb)cb.onclick=function(e){var b=e.target.closest('[data-c]');if(b){st.course=b.dataset.c;dash(el)}};
  var sb=el.querySelector('#rv-s');if(sb)sb.onclick=function(e){var b=e.target.closest('[data-s]');if(b){st.size=+b.dataset.s;dash(el)}};
  var g=el.querySelector('#rv-go');if(g)g.onclick=function(){session(el,mix(list,st.size))}}
function session(el,items){
  var q=items.map(function(x){return x.k}),n0=q.length,R={i:0,ok:0,done:0,retry:{}};
  var wasToday=doneToday();
  function bar(){return '<div class="rv-h"><button class="rv-x" id="rv-q" aria-label="'+E(t('close'))+'">×</button><div class="rv-bar"><i style="width:'+(n0?Math.round(R.done/n0*100):100)+'%"></i></div><span class="rv-cnt">'+Math.min(R.done+1,n0)+'/'+n0+'</span></div>'}
  function finish(){
    document.removeEventListener('keydown',onKey);
    var xp=R.ok*2,d=srsToday(),r=rvGet();
    if(r.day===d){r.n=(r.n||0)+R.done}else{r.streak=(r.day===d-1)?(r.streak||0)+1:1;r.day=d;r.n=R.done}
    rvSet(r);if(xp){ST.xp+=xp}save();
    var nxt=Object.keys(ST.srs).map(function(k){return ST.srs[k].due}).filter(function(x){return x>d}).sort(function(a,b){return a-b})[0];
    el.innerHTML='<div class="rv-card"><div class="rv-h"><h2>🎉 '+E(t('finish'))+'</h2><button class="rv-x" id="rv-q" aria-label="'+E(t('close'))+'">×</button></div>'+
     '<div class="rv-sum"><div><b>'+R.ok+'/'+n0+'</b><small>'+E(t('acc'))+'</small></div><div><b>+'+xp+'</b><small>'+E(t('xp'))+'</small></div><div><b>🔥 '+r.streak+'</b><small>'+E(t('streak'))+'</small></div></div>'+
     (nxt?'<p class="rv-sub">'+E(t('next'))+': '+E(nxt-d===1?t('tomorrow'):t('inDays')(nxt-d))+'.</p>':'')+
     '<button class="pg-btn rv-go" id="rv-back">'+E(t('title'))+'</button></div>';
    el.querySelector('#rv-q').onclick=close;el.querySelector('#rv-back').onclick=function(){dash(el)};try{if(R.ok)confetti(80)}catch(e){}}
  function show(){
    if(R.i>=q.length)return finish();
    var k=q[R.i],c=ST.srs[k],lang=(COURSES[c.c]||{}).tts||'en-US',rev=(kindOf(c)==='x'&&c.b>=3)||(kindOf(c)==='w'&&c.b>=4),rm=roma(c.w,c.c);
    var front=rev?'<div class="rv-w">'+E(c.m)+'</div>':'<div class="rv-w">'+E(c.w)+'</div>'+(rm?'<div class="rv-rm">'+E(rm)+'</div>':'')+'<button class="pg-btn ghost" id="rv-say">🔊 '+E(t('listen'))+'</button>';
    var back=rev?'<div class="rv-w">'+E(c.w)+'</div>'+(rm?'<div class="rv-rm">'+E(rm)+'</div>':'')+'<button class="pg-btn ghost" id="rv-say2">🔊 '+E(t('listen'))+'</button>':'<div class="rv-m">'+E(c.m)+'</div>'+(c.d?'<div class="rv-d">'+E(c.d)+'</div>':'');
    el.innerHTML='<div class="rv-card">'+bar()+'<div class="rv-q">'+E(rev?t('q2'):t('q1'))+' <span class="rv-tag">'+(kindOf(c)==='x'?'💬':'📖')+'</span></div><div class="rv-flash">'+front+'<div class="rv-back" id="rv-back" hidden>'+back+'<small>'+E(t('box'))+' '+(c.b+1)+' '+E(t('of'))+' 7 · '+E(flagOf(c.c))+'</small></div></div><div class="rv-foot" id="rv-foot"><button class="pg-btn rv-go" id="rv-show">'+E(t('show'))+'</button></div><p class="rv-note">'+E(t('kb'))+'</p></div>';
    el.querySelector('#rv-q').onclick=close;
    var say=function(ev){try{speak(c.w,lang,ev&&ev.currentTarget)}catch(e){}};
    var s1=el.querySelector('#rv-say');if(s1){s1.onclick=say;setTimeout(function(){say()},250)}
    var reveal=function(){
      var bk=el.querySelector('#rv-back');if(!bk||!bk.hidden)return;bk.hidden=false;
      var s2=el.querySelector('#rv-say2');if(s2){s2.onclick=say;say()}
      el.querySelector('#rv-foot').innerHTML='<button class="pg-btn danger" id="g-again">'+E(t('again'))+' (1)</button><button class="pg-btn ghost" id="g-hard">'+E(t('hard'))+' (2)</button><button class="pg-btn rv-ok" id="g-good">'+E(t('good'))+' (3)</button>';
      el.querySelector('#g-again').onclick=function(){grade('again')};el.querySelector('#g-hard').onclick=function(){grade('hard')};el.querySelector('#g-good').onclick=function(){grade('good')}};
    el.querySelector('#rv-show').onclick=reveal;
    function grade(g){var cc=ST.srs[k],d=srsToday();
      if(g==='good'){cc.b=Math.min(6,cc.b+1);cc.due=d+SRS_STEPS[cc.b];R.ok++;R.done++}
      else if(g==='hard'){cc.due=d+1;R.done++}
      else{cc.b=0;cc.due=d;R.retry[k]=(R.retry[k]||0)+1;if(R.retry[k]<=1)q.push(k);else cc.due=d+1;R.done=Math.min(R.done+1,n0)}
      save();try{beep(g!=='again')}catch(e){}R.i++;show()}
    onKey=function(ev){var b=el.querySelector('#rv-back');
      if(ev.key==='Escape')return close();
      if(ev.key===' '||ev.key==='Enter'){ev.preventDefault();return reveal()}
      if(b&&!b.hidden){if(ev.key==='1')grade('again');else if(ev.key==='2')grade('hard');else if(ev.key==='3')grade('good')}};
    document.removeEventListener('keydown',onKey);document.addEventListener('keydown',onKey)}
  document.addEventListener('keydown',function esc0(ev){});
  show()}
/* ---------- integra no app ---------- */
window.openReview=open;
var _b=window.srsBanner;
window.srsBanner=function(){try{var tot=Object.keys(ST.srs).length;if(!tot)return '';var due=dueCards('').length;
  return '<section class="srs-banner"><div><b>🔁 '+E(t('title'))+'</b><p>'+(due?due+' '+E(t('due'))+' · 🔥 '+streakNow():E(t('none')))+'</p></div><button class="pill light" data-go="review">'+E(due?t('start'):t('title'))+'</button></section>'}catch(e){return _b?_b():''}};
window.PogReview={open:open,dueCards:dueCards,backfillExpr:backfillExpr,prepare:prepare,streak:streakNow};
})();
