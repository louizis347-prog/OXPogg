/* Pogglot · treino de pronúncia com nota (reconhecimento de fala do navegador).
 * O aluno ouve, repete e recebe nota de 0 a 100 e as palavras marcadas (certa / quase / errada). */
(function(){
'use strict';
var KEY='pogglot:pron';
var T={
 pt:{btn:'🎤 Treinar pronúncia',title:'Treino de pronúncia',sub:'Ouça, repita em voz alta e veja sua nota.',listen:'Ouvir',rec:'Falar',stop:'Ouvindo…',avg:'Média',best:'Melhor',tries:'tentativas',
  heard:'Entendi',again:'Tentar de novo',nosup:'Este navegador não reconhece fala. Use o Chrome ou o Safari para ter nota. Você ainda pode ouvir e repetir.',noperm:'Libere o microfone nas configurações do navegador.',
  nospeech:'Não ouvi nada. Fale mais perto do microfone.',err:'Não consegui ouvir. Tente de novo.',close:'Fechar',none:'Este episódio não tem frases para treinar.',
  s3:'Excelente!',s2:'Muito bom!',s1:'Bom começo, repita para melhorar.',s0:'Ouça de novo e tente mais devagar.',legend:'verde = certo · amarelo = quase · vermelho = faltou ou diferente'},
 es:{btn:'🎤 Practicar pronunciación',title:'Práctica de pronunciación',sub:'Escucha, repite en voz alta y mira tu nota.',listen:'Escuchar',rec:'Hablar',stop:'Escuchando…',avg:'Media',best:'Mejor',tries:'intentos',
  heard:'Entendí',again:'Intentar de nuevo',nosup:'Este navegador no reconoce voz. Usa Chrome o Safari para tener nota. Aún puedes escuchar y repetir.',noperm:'Permite el micrófono en la configuración del navegador.',
  nospeech:'No oí nada. Habla más cerca del micrófono.',err:'No pude oír. Inténtalo de nuevo.',close:'Cerrar',none:'Este episodio no tiene frases para practicar.',
  s3:'¡Excelente!',s2:'¡Muy bien!',s1:'Buen comienzo, repite para mejorar.',s0:'Escucha otra vez e inténtalo más despacio.',legend:'verde = bien · amarillo = casi · rojo = faltó o distinto'}
};
function L(){try{return(window.ST&&ST.homeLang==='es')?'es':'pt'}catch(e){return'pt'}}
function t(k){return(T[L()][k]!=null?T[L()][k]:T.pt[k])}
function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(m){return({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'})[m]})}
function store(v){try{if(v===undefined)return JSON.parse(localStorage.getItem(KEY)||'{}')||{};localStorage.setItem(KEY,JSON.stringify(v))}catch(e){return{}}}

/* ---------- pontuação ---------- */
function norm(s,lang){var x=String(s||'').toLowerCase().replace(/[’‘`]/g,"'");
  if(/^(ja|zh)/.test(lang||''))return x.normalize('NFC');
  x=x.normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/œ/g,'oe').replace(/æ/g,'ae').replace(/ß/g,'ss');
  if(/^(fr|it|ca)/.test(lang||''))x=x.replace(/\b(?:l|j|d|qu|n|c|s|m|t|jusqu|lorsqu|puisqu|dell|all|nell|sull|un)'\s*/g,' ');
  return x.replace(/'/g,'')}
function toks(s,lang){var n=norm(s,lang);
  if(/^(ja|zh)/.test(lang||''))return n.replace(/[\s。、，．,.!?！？「」『』~〜…]/g,'').split('');
  return n.replace(/[^\p{L}\p{N} ]/gu,' ').split(/\s+/).filter(Boolean)}
function lev(a,b){var m=a.length,n=b.length;if(!m)return n;if(!n)return m;var p=[],i,j;for(j=0;j<=n;j++)p[j]=j;
  for(i=1;i<=m;i++){var c=[i];for(j=1;j<=n;j++)c[j]=Math.min(p[j]+1,c[j-1]+1,p[j-1]+(a[i-1]===b[j-1]?0:1));p=c}return p[n]}
function dist(a,b){var m=Math.max(a.length,b.length);return m?lev(a,b)/m:0}
/* alinha as palavras ouvidas com as do alvo; devolve nota 0-100 e o estado de cada palavra do alvo */
function score(heard,target,lang,conf){
  var A=toks(target,lang),B=toks(heard,lang),n=A.length,m=B.length,i,j;
  if(!n)return{score:0,words:[],extra:0};
  var D=[],P=[];for(i=0;i<=n;i++){D[i]=[];P[i]=[];for(j=0;j<=m;j++){D[i][j]=0;P[i][j]=0}}
  for(i=1;i<=n;i++){D[i][0]=i;P[i][0]=1}for(j=1;j<=m;j++){D[0][j]=j;P[0][j]=2}
  for(i=1;i<=n;i++)for(j=1;j<=m;j++){var c=dist(A[i-1],B[j-1]),sub=D[i-1][j-1]+Math.min(1,c*1.4),del=D[i-1][j]+1,ins=D[i][j-1]+1,v=Math.min(sub,del,ins);D[i][j]=v;P[i][j]=v===sub?0:(v===del?1:2)}
  var st=new Array(n),extra=0;i=n;j=m;
  while(i>0||j>0){var p=(i>0&&j>0)?P[i][j]:(i>0?1:2);
    if(p===0){var d=dist(A[i-1],B[j-1]);st[i-1]=d<=.25?'ok':(d<=.55?'near':'bad');i--;j--}
    else if(p===1){st[i-1]='bad';i--}else{extra++;j--}}
  var credit=0;st.forEach(function(x){credit+=x==='ok'?1:(x==='near'?.55:0)});
  var s=credit/n*100-Math.min(15,extra*4);
  if(conf>0&&conf<=1)s=s*.85+conf*100*.15;
  s=Math.max(0,Math.min(100,Math.round(s)));
  return{score:s,words:A.map(function(w,k){return{w:w,st:st[k]||'bad'}}),extra:extra}}
function stars(s){return s>=90?3:s>=70?2:s>=50?1:0}

/* ---------- reconhecimento ---------- */
var busy=false,rec=null;
function listen(lang,cb){
  var R=window.SpeechRecognition||window.webkitSpeechRecognition;if(!R)return cb({error:'nosup'});
  if(busy)return;busy=true;
  var r=new R(),done=false;rec=r;r.lang=lang;r.interimResults=false;r.maxAlternatives=3;
  function fin(o){if(done)return;done=true;busy=false;rec=null;cb(o)}
  r.onresult=function(ev){var alts=[];for(var k=0;k<ev.results[0].length;k++)alts.push({text:ev.results[0][k].transcript,conf:ev.results[0][k].confidence});fin({alts:alts})};
  r.onerror=function(ev){fin({error:(ev.error==='not-allowed'||ev.error==='service-not-allowed')?'noperm':(ev.error==='no-speech'?'nospeech':'err')})};
  r.onend=function(){fin({error:'nospeech'})};
  try{r.start()}catch(e){fin({error:'err'})}}
function stopRec(){try{if(rec)rec.abort()}catch(e){}busy=false;rec=null}
/* escolhe a melhor alternativa reconhecida */
function best(o,target,lang){var b=null;o.alts.forEach(function(a){var s=score(a.text,target,lang,a.conf);if(!b||s.score>b.res.score)b={text:a.text,res:s}});return b}

/* ---------- frases do episódio ---------- */
function phrases(e){var out=[],seen={};
  function add(a,b){a=String(a||'').trim();if(!a||a.length>110||seen[norm(a,'')])return;seen[norm(a,'')]=1;out.push([a,String(b||'')])}
  (e.fr||[]).forEach(function(f){if(f&&f.k==='nbshadow')(f.items||[]).forEach(function(i){add(i[0],i[1])})});
  (e.fr||[]).forEach(function(f){if(f&&f.k==='wrap')(f.recap||[]).forEach(function(i){add(i[0],i[1])})});
  if(e.h&&e.h.l)add(e.h.l,e.h.tr||'');
  return out.slice(0,10)}

/* ---------- interface ---------- */
function ring(s){var c=s>=90?'#2f9e44':s>=70?'#74b816':s>=50?'#f08c00':'#e03131';return '<div class="pr-ring" style="--p:'+s+';--c:'+c+'"><b>'+s+'</b></div>'}
function wordsHTML(res){return '<div class="pr-words">'+res.words.map(function(w){return '<span class="pr-w '+w.st+'">'+esc(w.w)+'</span>'}).join(' ')+'</div>'}
function open(e,cid,lang){
  var ps=phrases(e),old=document.getElementById('pr-modal');if(old)old.remove();
  var el=document.createElement('div');el.id='pr-modal';el.className='pr-modal';el.setAttribute('role','dialog');el.setAttribute('aria-modal','true');el.setAttribute('aria-label',t('title'));
  var key=function(i){return cid+'-'+e.n+':'+i};
  function draw(){var db=store(),sc=ps.map(function(p,i){return db[key(i)]});var done=sc.filter(Boolean),avg=done.length?Math.round(done.reduce(function(a,x){return a+x.best},0)/done.length):0;
    el.innerHTML='<div class="pr-card"><div class="pr-h"><h3>'+esc(t('title'))+'</h3><button class="pr-x" aria-label="'+esc(t('close'))+'">×</button></div><p class="pr-sub">'+esc(t('sub'))+'</p>'+
     (done.length?'<div class="pr-avg">'+esc(t('avg'))+': <b>'+avg+'</b>/100</div>':'')+'<p class="pr-leg">'+esc(t('legend'))+'</p>'+
     (ps.length?ps.map(function(p,i){var s=sc[i];return '<div class="pr-row" data-i="'+i+'"><div class="pr-t"><b>'+esc(p[0])+'</b><small>'+esc(p[1])+'</small></div><div class="pr-act"><button class="pr-b ls" aria-label="'+esc(t('listen'))+'">🔊</button><button class="pr-b mic" aria-label="'+esc(t('rec'))+'">🎤</button></div><div class="pr-res">'+(s?ring(s.best)+'<small>'+esc(t('best'))+' · '+s.n+' '+esc(t('tries'))+'</small>':'')+'</div></div>'}).join(''):'<p class="pr-empty">'+esc(t('none'))+'</p>')+'</div>';
    el.querySelector('.pr-x').onclick=close;
    el.querySelectorAll('.pr-row').forEach(function(row){var i=+row.dataset.i,p=ps[i];
      row.querySelector('.ls').onclick=function(ev){try{speak(p[0],lang,ev.currentTarget)}catch(x){}};
      row.querySelector('.mic').onclick=function(ev){var b=ev.currentTarget,res=row.querySelector('.pr-res');
        try{if(window.PogTTS)PogTTS.stop();speechSynthesis.cancel()}catch(x){}
        b.classList.add('on');res.innerHTML='<small>'+esc(t('stop'))+'</small>';
        listen(lang,function(o){b.classList.remove('on');
          if(o.error){res.innerHTML='<small class="pr-err">'+esc(t(o.error)||t('err'))+'</small>';return}
          var bt=best(o,p[0],lang),db2=store(),k=key(i),old=db2[k]||{best:0,n:0};
          db2[k]={best:Math.max(old.best,bt.res.score),n:old.n+1,ts:Date.now()};store(db2);
          var msg=t('s'+stars(bt.res.score));
          res.innerHTML=ring(bt.res.score)+'<div class="pr-fb"><b>'+esc(msg)+'</b>'+wordsHTML(bt.res)+'<small>'+esc(t('heard'))+': “'+esc(bt.text)+'”</small></div>';
          try{if(window.PogUI&&PogUI.toast&&bt.res.score>=90)PogUI.toast('🎤 '+bt.res.score)}catch(x){}})}})}
  function close(){stopRec();el.remove()}
  el.onclick=function(ev){if(ev.target===el)close()};document.body.appendChild(el);draw()}
/* botão na tela final do episódio */
var _r=window.render;
if(typeof _r==='function')window.render=function(){var r=_r.apply(this,arguments);
  try{if(typeof P!=='undefined'&&P&&!P.isTest&&P.steps&&P.steps[P.i]==='done'&&P.e){var st0=document.getElementById('pstage');
    if(st0&&!document.getElementById('pr-open')&&phrases(P.e).length){var b=document.createElement('button');b.id='pr-open';b.className='pg-btn ghost sc-open';b.textContent=t('btn');
      var e=P.e,cid=P.cid,lang=(P.c&&P.c.tts)||'en-US';b.onclick=function(){open(e,cid,lang)};st0.appendChild(b)}}}catch(x){}
  return r};
window.PogPron={score:score,toks:toks,open:open,phrases:phrases,stars:stars,stats:function(){var db=store(),k=Object.keys(db),s=0;k.forEach(function(x){s+=db[x].best});return{phrases:k.length,avg:k.length?Math.round(s/k.length):0}}};
})();
