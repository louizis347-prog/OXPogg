/* Pogglot · Meu vocabulário: palavras e expressões aprendidas (de episódios concluídos) contra as metas do curso (9.000 palavras e 2.000 expressões). */
(function(){
'use strict';
var GOAL={words:9000,expr:2000};
var T={
 pt:{card:'📚 Meu vocabulário',cardSub:function(w,x){return w+' palavras · '+x+' expressões'},open:'Ver painel',title:'Meu vocabulário',words:'Palavras',expr:'Expressões',goal:'Meta do idioma',learned:'aprendidas',of:'de',
  levels:'Por nível',search:'Buscar…',none:'Conclua episódios para ver suas palavras aqui.',noRes:'Nada encontrado.',close:'Fechar',recent:'Mais recentes primeiro',
  note:'Contamos as palavras e expressões dos episódios que você concluiu (vocabulário, diálogos-resumo e gírias).',loading:'Calculando…',more:'Mostrar mais'},
 es:{card:'📚 Mi vocabulario',cardSub:function(w,x){return w+' palabras · '+x+' expresiones'},open:'Ver panel',title:'Mi vocabulario',words:'Palabras',expr:'Expresiones',goal:'Meta del idioma',learned:'aprendidas',of:'de',
  levels:'Por nivel',search:'Buscar…',none:'Completa episodios para ver tus palabras aquí.',noRes:'No se encontró nada.',close:'Cerrar',recent:'Más recientes primero',
  note:'Contamos las palabras y expresiones de los episodios que completaste (vocabulario, diálogos-resumen y jergas).',loading:'Calculando…',more:'Mostrar más'}
};
function L(){try{return ST.homeLang==='es'?'es':'pt'}catch(e){return'pt'}}
function t(k){return T[L()][k]!=null?T[L()][k]:T.pt[k]}
function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(m){return({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'})[m]})}
function fmt(n){return Number(n).toLocaleString(L()==='es'?'es':'pt-BR')}
function plain(s){return String(s==null?'':s).replace(/<[^>]*>/g,'').replace(/\*\*/g,'').trim()}
function strip(w){return plain(w).replace(/^(?:l'|d'|un |une |des |les |le |la |el |los |las |una |unos |unas |il |lo |gli |der |die |das |ein |eine |the |a |an |o |os |as |um |uma )\s*/i,'').replace(/[.!?¡¿,;:]+$/g,'').trim()}
function key(s){return s.toLowerCase().normalize('NFC')}
function nwords(s){return(String(s).match(/[\p{L}\p{N}]+/gu)||[]).length}
/* extrai palavras e expressões de um episódio */
function extract(e,add){
  (e.v||[]).forEach(function(v){if(v&&v[0])add('w',strip(v[0]),plain(v[1]))});
  (e.fr||[]).forEach(function(f){if(!f)return;
    if(f.k==='nbvocab'||f.k==='nbfind')(f.items||[]).forEach(function(i){if(i&&i[0])add('w',strip(i[0]),plain(i[2]||i[1]))});
    else if(f.k==='wrap')(f.recap||[]).forEach(function(r){if(r&&r[0])add('x',plain(r[0]),plain(r[1]))});
    else if(f.k==='nbslang'&&f.gl)Object.keys(f.gl).forEach(function(g){add('x',plain(g),plain(f.gl[g]))});
    else if(f.k==='chunk')(f.blocks||[]).forEach(function(b){if(b&&b[0])add('x',plain(b[0]),plain(b[1]))});
    else if(f.k==='words')(f.items||[]).forEach(function(i){if(i&&i[0])add('w',strip(i[0]),plain(i[1]))});
  })}
function collect(cid){var W=new Map(),X=new Map(),eps=(window.EP&&EP[cid])||(typeof EP!=='undefined'?EP[cid]:[])||[];
  eps.forEach(function(e){if(isPlannedEpisode(e)||e.rev||!ST.done[cid+'-'+e.n])return;
    extract(e,function(kind,a,b){if(!a||a.length>80)return;var k=key(a);
      if(kind==='w'){if(nwords(a)<=3&&!W.has(k))W.set(k,{a:a,b:b,n:e.n,cid:cid})}
      else if(nwords(a)>=2&&!X.has(k))X.set(k,{a:a,b:b,n:e.n,cid:cid})})});
  return{W:W,X:X}}
function groupOf(cid){var c=COURSES[cid]||{};return c.group||cid}
function subsOf(cid){var g=groupOf(cid),G=GROUPS[g];return(G&&G.sub&&G.sub.length)?G.sub:[cid]}
function lvl(cid){var m=/-(a1|a2|b1|b2|c1|c2)$/.exec(cid);return m?m[1]:''}
var cache={};
async function compute(cid){
  var subs=subsOf(cid),res={levels:[],W:[],X:[]},plan=null;
  try{var r=await fetch('data/plan_'+groupOf(cid)+'.json');if(r.ok)plan=await r.json()}catch(e){}
  for(var i=0;i<subs.length;i++){var c=subs[i];
    if(doneCountFor(c)>0&&typeof ensureLangLoaded==='function')await ensureLangLoaded(c);
    var o=collect(c),lv=lvl(c),pl=plan&&plan.levels&&plan.levels[lv];
    res.levels.push({cid:c,lv:lv.toUpperCase(),w:o.W.size,x:o.X.size,wt:pl?pl.words_target:0,xt:pl?pl.expr_target:0});
    o.W.forEach(function(v){res.W.push(v)});o.X.forEach(function(v){res.X.push(v)})}
  res.W.sort(function(a,b){return b.n-a.n});res.X.sort(function(a,b){return b.n-a.n});return res}
function bar(p,c){return '<div class="vc-bar"><i style="width:'+Math.min(100,Math.round(p*100))+'%;background:'+c+'"></i></div>'}
function lineOf(name,v,goal,color){return '<div class="vc-line"><div><b>'+esc(name)+'</b><span>'+fmt(v)+' '+esc(t('of'))+' '+fmt(goal)+'</span></div>'+bar(goal?v/goal:0,color)+'</div>'}
async function open(cid){
  var old=document.getElementById('vc-modal');if(old)old.remove();
  var el=document.createElement('div');el.id='vc-modal';el.className='pr-modal';el.setAttribute('role','dialog');el.setAttribute('aria-modal','true');el.setAttribute('aria-label',t('title'));
  el.innerHTML='<div class="pr-card"><div class="pr-h"><h3>'+esc(t('title'))+'</h3><button class="pr-x" aria-label="'+esc(t('close'))+'">×</button></div><p class="pr-sub">'+esc(t('loading'))+'</p></div>';
  document.body.appendChild(el);el.onclick=function(e){if(e.target===el)el.remove()};el.querySelector('.pr-x').onclick=function(){el.remove()};
  var d=await compute(cid);cache[groupOf(cid)]=d;
  var tw=d.W.length,tx=d.X.length,tab='w',q='',lim=60;
  function draw(){var list=(tab==='w'?d.W:d.X).filter(function(v){return!q||(v.a+' '+v.b).toLowerCase().indexOf(q)>=0});
    el.querySelector('.pr-card').innerHTML='<div class="pr-h"><h3>'+esc(t('title'))+'</h3><button class="pr-x" aria-label="'+esc(t('close'))+'">×</button></div>'+
     '<p class="pr-sub">'+esc(t('goal'))+'</p>'+lineOf(t('words'),tw,GOAL.words,'#79E2DE')+lineOf(t('expr'),tx,GOAL.expr,'#12b886')+
     '<h4 class="vc-h">'+esc(t('levels'))+'</h4>'+d.levels.filter(function(l){return l.w||l.x||l.wt}).map(function(l){return '<div class="vc-lv"><b>'+esc(l.lv||'')+'</b><div>'+
        '<small>'+esc(t('words'))+': '+fmt(l.w)+(l.wt?' / '+fmt(l.wt):'')+'</small>'+bar(l.wt?l.w/l.wt:Math.min(1,l.w/GOAL.words*6),'#79E2DE')+
        '<small>'+esc(t('expr'))+': '+fmt(l.x)+(l.xt?' / '+fmt(l.xt):'')+'</small>'+bar(l.xt?l.x/l.xt:Math.min(1,l.x/GOAL.expr*6),'#12b886')+'</div></div>'}).join('')+
     '<div class="vc-tabs"><button class="pg-chip" data-t="w" aria-pressed="'+(tab==='w')+'">'+esc(t('words'))+' ('+fmt(tw)+')</button><button class="pg-chip" data-t="x" aria-pressed="'+(tab==='x')+'">'+esc(t('expr'))+' ('+fmt(tx)+')</button></div>'+
     '<input class="vc-q" type="search" placeholder="'+esc(t('search'))+'" aria-label="'+esc(t('search'))+'" value="'+esc(q)+'">'+
     (list.length?'<ul class="vc-list">'+list.slice(0,lim).map(function(v){return '<li><b>'+esc(v.a)+'</b><span>'+esc(v.b)+'</span></li>'}).join('')+'</ul>'+(list.length>lim?'<button class="pg-btn ghost" id="vc-more">'+esc(t('more'))+'</button>':''):'<p class="pr-empty">'+esc(tw+tx?t('noRes'):t('none'))+'</p>')+
     '<p class="pr-leg">'+esc(t('note'))+'</p>';
    el.querySelector('.pr-x').onclick=function(){el.remove()};
    el.querySelector('.vc-tabs').onclick=function(e){var b=e.target.closest('[data-t]');if(b){tab=b.dataset.t;lim=60;draw()}};
    var qi=el.querySelector('.vc-q');qi.oninput=function(){q=qi.value.trim().toLowerCase();var pos=qi.selectionStart;lim=60;draw();var n=el.querySelector('.vc-q');n.focus();try{n.setSelectionRange(pos,pos)}catch(x){}};
    var mo=document.getElementById('vc-more');if(mo)mo.onclick=function(){lim+=120;draw()}}
  draw()}
function mount(cid){
  if(document.querySelector('.vc-card'))return;var host=document.querySelector('.p2tools');if(!host||typeof ST==='undefined')return;
  var subs=subsOf(cid),any=subs.some(function(c){return doneCountFor(c)>0});
  host.insertAdjacentHTML('beforebegin','<section class="exam-card vc-card" role="region" aria-label="'+esc(t('title'))+'" style="background:linear-gradient(135deg,#0ca678,#3b8bff)"><div class="ex-t"><b>'+esc(t('card'))+'</b><small id="vc-sub">'+esc(any?t('loading'):t('none'))+'</small></div><button class="ex-b" id="vc-go" style="color:#087f5b">'+esc(t('open'))+'</button></section>');
  document.getElementById('vc-go').onclick=function(){open(cid)};
  if(any)compute(cid).then(function(d){cache[groupOf(cid)]=d;var s=document.getElementById('vc-sub');if(s)s.textContent=t('cardSub')(fmt(d.W.length),fmt(d.X.length))}).catch(function(){})}
var _c=window.course;
if(typeof _c==='function')window.course=function(id){var r=_c.apply(this,arguments);try{mount(id)}catch(e){console.error('vocab',e)}return r};
window.PogVocab={open:open,compute:compute,collect:collect,extract:extract};
})();
