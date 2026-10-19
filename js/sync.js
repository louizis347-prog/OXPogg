/* Pogglot · sincronização do progresso entre aparelhos (Supabase, tabela user_state; veja backend/sync.sql).
 * Regras: concluídos e testes feitos = união; XP e contadores = maior valor; mapas (revisão espaçada etc.) = união com o mais recente vencendo;
 * o resto = o mais recente vence. Dados de outro aparelho só entram ao abrir o app (com recarga), nunca no meio de uma lição. */
(function(){
'use strict';
var PRE='pogglot:',TSK=PRE+'_ts';
var SYNC=['done','testDone','xp','totalCorrect','totalAnswered','maxStreak','srs','writing','errs','xphist','ach','know','quiz','plan','wk','shelf','streak','homeLang','lastCourse','lastEp','wallet','mis','goal','remind','daily','since','placed','romaji','a11y','comm'];
var UNION_TRUE=['done','testDone'],MAXN=['xp','totalCorrect','totalAnswered','maxStreak'],MAPS=['srs','writing','errs','xphist','ach','know','quiz','plan','wk'];
var ls=window.localStorage,rawSet=Storage.prototype.setItem,rawRem=Storage.prototype.removeItem,off=false,timer=null,busy=false,tsCache=null;
function syncable(k){if(k.indexOf(PRE)!==0)return false;var n=k.slice(PRE.length);return SYNC.indexOf(n)>=0||n.indexOf('exam:')===0}
function rd(k){try{return JSON.parse(ls.getItem(PRE+k))}catch(e){return null}}
function tsGet(){if(tsCache)return tsCache;try{tsCache=JSON.parse(ls.getItem(TSK)||'{}')||{}}catch(e){tsCache={}}return tsCache}
function tsSave(){try{rawSet.call(ls,TSK,JSON.stringify(tsCache||{}))}catch(e){}}
/* marca quando cada chave mudou neste aparelho */
Storage.prototype.setItem=function(k,v){var r=rawSet.apply(this,arguments);try{if(this===ls&&syncable(k)){tsGet()[k.slice(PRE.length)]=Date.now();tsSave();schedule()}}catch(e){}return r};
Storage.prototype.removeItem=function(k){var r=rawRem.apply(this,arguments);try{if(this===ls&&syncable(k))schedule()}catch(e){}return r};
function localBlob(){var vals={},ts=tsGet(),t2={},now=Date.now();
  for(var i=0;i<ls.length;i++){var k=ls.key(i);if(!syncable(k))continue;var n=k.slice(PRE.length);vals[n]=ls.getItem(k);t2[n]=ts[n]||0}
  return{v:1,vals:vals,ts:t2}}
function parse(s){try{return JSON.parse(s)}catch(e){return null}}
function mergeKey(n,lv,lt,rv,rt){/* devolve [valorString,ts] */
  var a=parse(lv),b=parse(rv),newer=rt>lt;
  if(lv==null)return[rv,rt];if(rv==null)return[lv,lt];
  if(UNION_TRUE.indexOf(n)>=0&&a&&b&&typeof a==='object'){var o=Object.assign({},newer?a:b,newer?b:a);Object.keys(o).forEach(function(x){if((a[x]===true)||(b[x]===true))o[x]=true});return[JSON.stringify(o),Math.max(lt,rt)]}
  if(n.indexOf('exam:')===0&&a&&b)return[JSON.stringify((b.pct||0)>(a.pct||0)?b:a),Math.max(lt,rt)];
  if(MAXN.indexOf(n)>=0&&typeof a==='number'&&typeof b==='number')return[String(Math.max(a,b)),Math.max(lt,rt)];
  if(MAPS.indexOf(n)>=0&&a&&b&&typeof a==='object'&&!Array.isArray(a)&&typeof b==='object')return[JSON.stringify(Object.assign({},newer?a:b,newer?b:a)),Math.max(lt,rt)];
  if(n==='shelf'&&Array.isArray(a)&&Array.isArray(b)){var seen={},out=[];(newer?b.concat(a):a.concat(b)).forEach(function(x){var j=JSON.stringify(x);if(!seen[j]){seen[j]=1;out.push(x)}});return[JSON.stringify(out),Math.max(lt,rt)]}
  return newer?[rv,rt]:[lv,lt]}
function merge(l,r){var vals={},ts={},names={};Object.keys(l.vals).concat(Object.keys(r.vals||{})).forEach(function(n){names[n]=1});
  Object.keys(names).forEach(function(n){var m=mergeKey(n,l.vals[n],l.ts[n]||0,(r.vals||{})[n],(r.ts||{})[n]||0);vals[n]=m[0];ts[n]=m[1]});
  return{v:1,vals:vals,ts:ts}}
function apply(m,l){var changed=false,t=tsGet();
  Object.keys(m.vals).forEach(function(n){if(m.vals[n]!==l.vals[n]){try{rawSet.call(ls,PRE+n,m.vals[n]);changed=true}catch(e){}}t[n]=m.ts[n]});tsSave();return changed}
async function run(opts){
  if(off||busy||!window.PogCloud||!PogCloud.syncAvailable||!PogCloud.syncAvailable())return;
  busy=true;
  try{var row=await PogCloud.stateGet(),l=localBlob(),r=row&&row.data&&row.data.vals?row.data:{v:1,vals:{},ts:{}};
    var m=merge(l,r),changed=opts&&opts.pull?apply(m,l):false;
    if(changed&&!document.getElementById('player')){var g=+(sessionStorage.getItem('pogglot:syncReload')||0);
      if(Date.now()-g>60000){try{sessionStorage.setItem('pogglot:syncReload',String(Date.now()))}catch(e){}location.reload();return}}
    /* envia só se houver algo novo para o servidor */
    var mm=opts&&opts.pull?merge(localBlob(),r):merge(l,r);
    if(JSON.stringify(mm.vals)!==JSON.stringify(r.vals||{}))await PogCloud.statePut(mm);
    try{rawSet.call(ls,PRE+'_synced',String(Date.now()))}catch(e){}
  }catch(e){var c=e&&e.code,msg=String(e&&e.message||'');
    if(/user_state|relation|schema cache|404|PGRST/i.test(msg)||c==='PGRST205')off=true; /* tabela ainda não criada: desliga em silêncio */
  }finally{busy=false}}
function schedule(){clearTimeout(timer);timer=setTimeout(function(){run({pull:false})},6000)}
function boot(){if(!window.PogCloud)return;
  PogCloud.onAuth(function(u){if(u)setTimeout(function(){run({pull:true})},1200)});
  try{if(PogCloud.user&&PogCloud.user())setTimeout(function(){run({pull:true})},2500)}catch(e){}
  document.addEventListener('visibilitychange',function(){
    if(document.visibilityState==='hidden')run({pull:false});
    else{var last=+ls.getItem(PRE+'_synced')||0;if(Date.now()-last>5*60000)run({pull:true})}})}
window.PogSync={run:run,merge:merge,mergeKey:mergeKey,now:function(){return run({pull:true})}};
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',boot);else boot();
})();
