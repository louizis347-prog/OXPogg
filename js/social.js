/* Pogglot · Turmas (painel de professor), desafios entre amigos e comentários por episódio.
 * Precisa de backend/social.sql rodado no Supabase. Depende de PogCloud, PogUI e PogComm. */
(function(){
'use strict';
var S={
 pt:{tab:'Turmas',cls:'Turmas',chs:'Desafios',newC:'Criar turma',joinC:'Entrar com código',newCh:'Criar desafio',joinCh:'Entrar com código',name:'Nome',days:'Duração (dias)',code:'Código',create:'Criar',join:'Entrar',
  none:'Nada por aqui ainda.',open:'Abrir',back:'Voltar',loading:'Carregando…',share:'Compartilhe este código com seus alunos ou amigos:',copy:'Copiar',copied:'Copiado!',
  roster:'Alunos',xp:'XP',streak:'Sequência',eps:'Episódios',ach:'Conquistas',teacher:'Professor',leave:'Sair',del:'Apagar',confirmDel:'Apagar? Isso não pode ser desfeito.',confirmLeave:'Sair?',
  score:'XP ganho',ends:'termina em',endedAt:'encerrado',days_:'dias',winner:'Vencedor',needLogin:'Entre na sua conta para usar turmas e desafios.',
  off:'Este recurso ainda não foi ativado no servidor. Quem hospeda o app precisa rodar backend/social.sql no Supabase.',
  tipC:'Como professor, crie uma turma e passe o código aos alunos. Você acompanha XP, sequência e episódios de cada um.',tipCh:'Convide amigos: vence quem ganhar mais XP durante o período.',
  cmBtn:'💬 Dúvidas e comentários deste episódio',cmT:'Comentários do episódio',cmPh:'Escreva uma dúvida ou comentário…',cmSend:'Enviar',cmNone:'Seja o primeiro a comentar.',cmClose:'Fechar',cmDel:'Apagar',you:'Você',
  last:'Ativo',today:'hoje',yest:'ontem',dago:'d',never:'—',tasks:'Tarefas da turma',newT:'Nova tarefa',tTitle:'Descrição da tarefa',tKind:'Tipo',kFree:'Marcar como concluída',kXp:'Ganhar XP',tTarget:'Meta de XP',tDays:'Prazo em dias (opcional)',tNone:'Nenhuma tarefa ainda.',tDue:'prazo',tDone:'concluíram',iDone:'Concluí',doneL:'Concluída',tDel:'Apagar tarefa',export:'📥 Exportar planilha (CSV)',student:'Aluno',
  ovr:function(n,t){return n+' passou você no desafio “'+t+'”!'},wonMsg:function(t){return 'O desafio “'+t+'” terminou e você ficou em 1º lugar! 🏆'},endMsg:function(t,n){return 'O desafio “'+t+'” terminou. Vencedor: '+n},allowN:'Ativar avisos de desafio no aparelho'},
 es:{tab:'Clases',cls:'Clases',chs:'Desafíos',newC:'Crear clase',joinC:'Entrar con código',newCh:'Crear desafío',joinCh:'Entrar con código',name:'Nombre',days:'Duración (días)',code:'Código',create:'Crear',join:'Entrar',
  none:'Aún no hay nada.',open:'Abrir',back:'Volver',loading:'Cargando…',share:'Comparte este código con tus alumnos o amigos:',copy:'Copiar',copied:'¡Copiado!',
  roster:'Alumnos',xp:'XP',streak:'Racha',eps:'Episodios',ach:'Logros',teacher:'Profesor',leave:'Salir',del:'Borrar',confirmDel:'¿Borrar? No se puede deshacer.',confirmLeave:'¿Salir?',
  score:'XP ganado',ends:'termina en',endedAt:'terminado',days_:'días',winner:'Ganador',needLogin:'Inicia sesión para usar clases y desafíos.',
  off:'Este recurso aún no está activado en el servidor. Quien aloja la app debe ejecutar backend/social.sql en Supabase.',
  tipC:'Como profesor, crea una clase y pasa el código a tus alumnos. Verás XP, racha y episodios de cada uno.',tipCh:'Invita a amigos: gana quien consiga más XP durante el período.',
  cmBtn:'💬 Dudas y comentarios de este episodio',cmT:'Comentarios del episodio',cmPh:'Escribe una duda o comentario…',cmSend:'Enviar',cmNone:'Sé el primero en comentar.',cmClose:'Cerrar',cmDel:'Borrar',you:'Tú',
  last:'Activo',today:'hoy',yest:'ayer',dago:'d',never:'—',tasks:'Tareas de la clase',newT:'Nueva tarea',tTitle:'Descripción de la tarea',tKind:'Tipo',kFree:'Marcar como completada',kXp:'Ganar XP',tTarget:'Meta de XP',tDays:'Plazo en días (opcional)',tNone:'Aún no hay tareas.',tDue:'plazo',tDone:'completaron',iDone:'Completé',doneL:'Completada',tDel:'Borrar tarea',export:'📥 Exportar hoja de cálculo (CSV)',student:'Alumno',
  ovr:function(n,t){return n+' te pasó en el desafío “'+t+'”!'},wonMsg:function(t){return 'El desafío “'+t+'” terminó y quedaste en 1.er lugar! 🏆'},endMsg:function(t,n){return 'El desafío “'+t+'” terminó. Ganador: '+n},allowN:'Activar avisos de desafío en el dispositivo'}
};
var C=function(){return window.PogComm},U=function(){return window.PogUI},cl=function(){return window.PogCloud};
function t(k){var L=U().L0();return(S[L]&&S[L][k]!=null)?S[L][k]:S.pt[k]}
function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(m){return({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'})[m]})}
function $(s,r){return(r||document).querySelector(s)}
function rest(m,p,body){return cl().rest(m,p,body===undefined?{}:{body:body})}
function rpc(fn,body){return rest('POST','/rest/v1/rpc/'+fn,body||{})}
function errMsg(e){var m=String(e&&e.message||'');return /relation|schema cache|PGRST|does not exist|function public|Could not find/i.test(m)?t('off'):(m||t('off'))}
function ago(ts){if(!ts)return t('never');var d=Math.floor((Date.now()-new Date(ts).getTime())/864e5);return d<=0?t('today'):d===1?t('yest'):d+t('dago')}
function enc(x){return encodeURIComponent(x)}
function sum(o){var n=0;if(o&&typeof o==='object')Object.keys(o).forEach(function(k){n+=+o[k]||0});return n}
function cnt(o){return o&&typeof o==='object'?Object.keys(o).length:0}
function rows(a){return Array.isArray(a)?a:(a?[a]:[])}
var st={tab:'classes',cur:null};

/* ---------- aba Turmas/Desafios ---------- */
async function page(arg){
  if(arg&&arg.tab)st.tab=arg.tab;st.cur=null;
  C().shell(C().subtabs('class')+'<div class="sc-wrap"><div class="sc-head"><h2>🎓 '+esc(t('tab'))+'</h2></div>'+
   '<div class="sc-chips"><button class="pg-chip" data-t="classes" aria-pressed="'+(st.tab==='classes')+'">🏫 '+esc(t('cls'))+'</button><button class="pg-chip" data-t="challenges" aria-pressed="'+(st.tab==='challenges')+'">🏁 '+esc(t('chs'))+'</button></div>'+
   '<p class="sc-tip">'+esc(st.tab==='classes'?t('tipC'):t('tipCh'))+'</p><div id="sc-body"><p class="pg-empty">'+esc(t('loading'))+'</p></div></div>');
  C().wireTabs();
  $('.sc-chips').onclick=function(e){var b=e.target.closest('[data-t]');if(b){st.tab=b.dataset.t;page()}};
  if(!C().user()||!cl()||cl().mode==='demo'){$('#sc-body').innerHTML='<p class="pg-empty">'+esc(t('needLogin'))+'</p>';return}
  list()}
async function list(){
  var body=$('#sc-body'),isC=st.tab==='classes';if(!body)return;
  try{
    var items=isC?await rest('GET','/rest/v1/classes?select=id,name,code,owner,created_at&order=created_at.desc'):
      await rest('GET','/rest/v1/challenges?select=id,title,code,owner,starts_at,ends_at&order=created_at.desc');
    var me=C().user().id;
    body.innerHTML='<div class="sc-acts"><button class="pg-btn" id="sc-new">＋ '+esc(isC?t('newC'):t('newCh'))+'</button><button class="pg-btn ghost" id="sc-join">🔑 '+esc(isC?t('joinC'):t('joinCh'))+'</button></div><div id="sc-form"></div>'+
      '<div class="sc-list">'+(items.length?items.map(function(x){var nm=isC?x.name:x.title,sub=isC?(x.owner===me?'👩‍🏫 '+t('teacher')+' · '+t('code')+': <b>'+esc(x.code)+'</b>':''):chSub(x,me);
        return '<button class="sc-card" data-id="'+esc(x.id)+'"><b>'+esc(nm)+'</b><small>'+sub+'</small><span>'+esc(t('open'))+' ›</span></button>'}).join(''):'<p class="pg-empty">'+esc(t('none'))+'</p>')+'</div>';
    $('#sc-new').onclick=function(){form(true)};$('#sc-join').onclick=function(){form(false)};
    $('.sc-list').onclick=function(e){var b=e.target.closest('[data-id]');if(b)detail(b.dataset.id,items.find(function(x){return x.id===b.dataset.id}))};
  }catch(e){body.innerHTML='<p class="pg-empty">'+esc(errMsg(e))+'</p>'}}
function chSub(x,me){var end=new Date(x.ends_at).getTime(),d=Math.ceil((end-Date.now())/864e5);
  return(d>0?t('ends')+' '+d+' '+t('days_'):t('endedAt'))+(x.owner===me?' · '+t('code')+': <b>'+esc(x.code)+'</b>':'')}
function form(create){var isC=st.tab==='classes',f=$('#sc-form');
  f.innerHTML='<form class="sc-form">'+(create?'<label>'+esc(t('name'))+'<input name="n" maxlength="60" required></label>'+(isC?'':'<label>'+esc(t('days'))+'<input name="d" type="number" min="1" max="60" value="7"></label>'):'<label>'+esc(t('code'))+'<input name="c" maxlength="12" required style="text-transform:uppercase"></label>')+
    '<button class="pg-btn" type="submit">'+esc(create?t('create'):t('join'))+'</button><p class="sc-err" hidden></p></form>';
  var fm=f.firstChild,er=$('.sc-err',f);fm.n&&fm.n.focus();fm.c&&fm.c.focus();
  fm.onsubmit=async function(ev){ev.preventDefault();er.hidden=true;
    try{
      if(isC)await(create?rest('POST','/rest/v1/classes',{name:fm.n.value.trim()}):rpc('join_class',{p_code:fm.c.value}));
      else await(askNotif(),create?rpc('create_challenge',{p_title:fm.n.value.trim(),p_days:+fm.d.value||7}):rpc('join_challenge',{p_code:fm.c.value}));
      list()}catch(e){er.hidden=false;er.textContent=errMsg(e)}}}
async function detail(id,meta){
  var isC=st.tab==='classes',body=$('#sc-body'),me=C().user().id;body.innerHTML='<p class="pg-empty">'+esc(t('loading'))+'</p>';
  try{
    var data=await rpc(isC?'class_roster':'challenge_board',isC?{p_class:id}:{p_challenge:id});data=rows(data);
    var own=meta&&meta.owner===me,max=Math.max.apply(null,data.map(function(r){return isC?(+r.xp||0):(+r.score||0)}).concat([1]));
    var head='<button class="pg-btn ghost" id="sc-back">‹ '+esc(t('back'))+'</button><h3 class="sc-title">'+esc(meta?(meta.name||meta.title):'')+'</h3>';
    var share=own?'<div class="sc-share">'+esc(t('share'))+' <b class="sc-code">'+esc(meta.code)+'</b> <button class="pg-chip" id="sc-copy">'+esc(t('copy'))+'</button></div>':'';
    var tbl;
    if(isC)tbl='<div class="sc-table" role="table"><div class="sc-tr hd" role="row"><span>#</span><span>'+esc(t('roster'))+'</span><span>'+esc(t('xp'))+'</span><span>🔥</span><span>'+esc(t('eps'))+'</span><span>🏅</span><span>'+esc(t('last'))+'</span></div>'+
      data.map(function(r,i){return '<div class="sc-tr'+(r.uid===me?' me':'')+'" role="row"><span>'+(i+1)+'</span><span class="nm">'+esc(r.avatar||'🙂')+' '+esc(r.name||'Aluno')+(r.is_owner?' <em>'+esc(t('teacher'))+'</em>':'')+'</span><span>'+(+r.xp||0)+'</span><span>'+(+r.streak||0)+'</span><span>'+sum(r.eps)+'</span><span>'+cnt(r.ach)+'</span><span>'+esc(ago(r.last_active))+'</span></div>'}).join('')+'</div>';
    else{var ended=meta&&new Date(meta.ends_at).getTime()<Date.now();
      tbl='<p class="sc-tip">'+esc(meta?chSub(meta,'x'):'')+'</p><div class="sc-board">'+data.map(function(r,i){var w=Math.round((+r.score||0)/max*100);
        return '<div class="sc-bar'+(r.uid===me?' me':'')+'"><span class="nm">'+(i===0&&ended?'🏆 ':(i+1)+'. ')+esc(r.avatar||'🙂')+' '+esc(r.name||'Aluno')+'</span><i style="width:'+w+'%"></i><b>'+(+r.score||0)+' '+esc(t('score'))+'</b></div>'}).join('')+'</div>'}
    body.innerHTML=head+share+tbl+'<button class="pg-btn danger" id="sc-del">'+esc(own?t('del'):t('leave'))+'</button>';
    $('#sc-back').onclick=list;
    if(isC)loadTasks(id,own,me,data,meta);
    var cp=$('#sc-copy');if(cp)cp.onclick=function(){try{navigator.clipboard.writeText(meta.code)}catch(e){}cp.textContent=t('copied')};
    $('#sc-del').onclick=async function(){if(!confirm(own?t('confirmDel'):t('confirmLeave')))return;
      try{var base=isC?'classes':'challenges',mem=isC?'class_members?class_id=eq.':'challenge_members?challenge_id=eq.';
        if(own)await rest('DELETE','/rest/v1/'+base+'?id=eq.'+encodeURIComponent(id));
        else await rest('DELETE','/rest/v1/'+mem+encodeURIComponent(id)+'&uid=eq.'+encodeURIComponent(me));
        list()}catch(e){body.insertAdjacentHTML('beforeend','<p class="sc-err">'+esc(errMsg(e))+'</p>')}};
  }catch(e){body.innerHTML='<button class="pg-btn ghost" id="sc-back">‹ '+esc(t('back'))+'</button><p class="pg-empty">'+esc(errMsg(e))+'</p>';$('#sc-back').onclick=list}}


/* ---------- tarefas da turma, exportação e última atividade ---------- */
function dueTxt(d){if(!d)return '';var x=new Date(d);return ' · '+t('tDue')+' '+x.toLocaleDateString(U().L0()==='es'?'es':'pt-BR')}
async function loadTasks(id,own,me,roster,meta){
  var box=document.createElement('div');box.id='sc-tasks';box.className='sc-tasks';
  var anchor=$('#sc-del');if(!anchor||!anchor.parentNode)return;anchor.parentNode.insertBefore(box,anchor);
  var ts=[],bd=[];
  try{ts=rows(await rest('GET','/rest/v1/class_tasks?select=id,title,kind,target,due_at,created_at&class_id=eq.'+enc(id)+'&order=created_at.desc'));
    bd=ts.length?rows(await rpc('class_task_board',{p_class:id})):[]}catch(e){if(!own)return}
  function draw(){
    var h='<h4>📝 '+esc(t('tasks'))+'</h4>'+(own?'<button class="pg-btn" id="st-new">＋ '+esc(t('newT'))+'</button><div id="st-form"></div>':'')+
      (ts.length?ts.map(function(k){var rs=bd.filter(function(b){return b.task_id===k.id}),ok=rs.filter(function(b){return b.done}).length,mine=rs.find(function(b){return b.uid===me});
        var line=own?'<small>'+ok+'/'+rs.length+' '+esc(t('tDone'))+'</small>':(mine?(mine.done?'<span class="sc-ok">✓ '+esc(t('doneL'))+'</span>':(k.kind==='xp'?'<small>'+(+mine.progress||0)+'/'+k.target+' XP</small>':'<button class="pg-btn" data-done="'+esc(k.id)+'">'+esc(t('iDone'))+'</button>')):'');
        var detail=own?'<div class="sc-tp">'+rs.map(function(b){return '<span class="'+(b.done?'ok':'')+'">'+(b.done?'✓ ':'')+esc(b.avatar||'')+' '+esc(b.name||'')+(k.kind==='xp'?' ('+(+b.progress||0)+')':'')+'</span>'}).join('')+'</div>':'';
        return '<div class="sc-task"><div><b>'+esc(k.title)+'</b><small>'+(k.kind==='xp'?'🎯 '+k.target+' XP':'')+esc(dueTxt(k.due_at))+'</small></div>'+line+detail+(own?'<button class="sc-del" data-tdel="'+esc(k.id)+'">'+esc(t('tDel'))+'</button>':'')+'</div>'}).join(''):'<p class="pg-empty">'+esc(t('tNone'))+'</p>')+
      (own?'<button class="pg-btn ghost" id="st-exp">'+esc(t('export'))+'</button>':'');
    box.innerHTML=h;
    var nb=$('#st-new',box);if(nb)nb.onclick=function(){taskForm()};
    var ex=$('#st-exp',box);if(ex)ex.onclick=function(){exportCsv(meta,roster,ts,bd)};
    box.onclick=async function(e){var b=e.target.closest('[data-done]'),d=e.target.closest('[data-tdel]');
      try{if(b){await rpc('mark_task_done',{p_task:b.dataset.done});await reload()}
        else if(d&&confirm(t('confirmDel'))){await rest('DELETE','/rest/v1/class_tasks?id=eq.'+enc(d.dataset.tdel));await reload()}}catch(x){box.insertAdjacentHTML('beforeend','<p class="sc-err">'+esc(errMsg(x))+'</p>')}}}
  async function reload(){ts=rows(await rest('GET','/rest/v1/class_tasks?select=id,title,kind,target,due_at,created_at&class_id=eq.'+enc(id)+'&order=created_at.desc'));bd=ts.length?rows(await rpc('class_task_board',{p_class:id})):[];draw()}
  function taskForm(){var f=$('#st-form',box);
    f.innerHTML='<form class="sc-form"><label>'+esc(t('tTitle'))+'<input name="n" maxlength="120" required></label><label>'+esc(t('tKind'))+'<select name="k"><option value="free">'+esc(t('kFree'))+'</option><option value="xp">'+esc(t('kXp'))+'</option></select></label><label class="sc-xp" hidden>'+esc(t('tTarget'))+'<input name="x" type="number" min="1" max="100000" value="100"></label><label>'+esc(t('tDays'))+'<input name="d" type="number" min="1" max="365"></label><button class="pg-btn" type="submit">'+esc(t('create'))+'</button><p class="sc-err" hidden></p></form>';
    var fm=f.firstChild,er=$('.sc-err',f);fm.n.focus();fm.k.onchange=function(){$('.sc-xp',f).hidden=fm.k.value!=='xp'};
    fm.onsubmit=async function(ev){ev.preventDefault();er.hidden=true;
      try{await rpc('create_class_task',{p_class:id,p_title:fm.n.value.trim(),p_kind:fm.k.value,p_target:fm.k.value==='xp'?(+fm.x.value||0):0,p_days:fm.d.value?+fm.d.value:null});await reload()}catch(x){er.hidden=false;er.textContent=errMsg(x)}}}
  draw()}
function csvCell(v){v=String(v==null?'':v);return /[";\n]/.test(v)?'"'+v.replace(/"/g,'""')+'"':v}
function exportCsv(meta,roster,ts,bd){
  var head=[t('student'),t('xp'),t('streak'),t('eps'),t('ach'),t('last')].concat(ts.map(function(k){return k.title}));
  var lines=[head].concat(roster.filter(function(r){return!r.is_owner}).map(function(r){
    return[r.name||'',+r.xp||0,+r.streak||0,sum(r.eps),cnt(r.ach),r.last_active?new Date(r.last_active).toLocaleDateString(U().L0()==='es'?'es':'pt-BR'):''].concat(ts.map(function(k){
      var b=bd.find(function(x){return x.task_id===k.id&&x.uid===r.uid});if(!b)return'';return k.kind==='xp'?((+b.progress||0)+'/'+k.target+' XP'+(b.done?' ✓':'')):(b.done?'Sim':'Não')}))}));
  var csv='﻿'+lines.map(function(l){return l.map(csvCell).join(';')}).join('\r\n');
  try{var a=document.createElement('a');a.href=URL.createObjectURL(new Blob([csv],{type:'text/csv;charset=utf-8'}));a.download=('turma-'+(meta&&meta.name||'pogglot')).replace(/[^\w-]+/g,'_')+'.csv';document.body.appendChild(a);a.click();setTimeout(function(){a.remove();URL.revokeObjectURL(a.href)},500)}catch(e){}}

/* ---------- aviso quando alguém passa você num desafio ---------- */
var CHK='pogglot:chrank',wTimer=null,wBusy=false;
function chStore(v){try{if(v===undefined)return JSON.parse(localStorage.getItem(CHK)||'{}')||{};localStorage.setItem(CHK,JSON.stringify(v))}catch(e){return{}}}
function pushMsg(msg){try{if(window.PogUI&&PogUI.toast)PogUI.toast(msg)}catch(e){}
  try{if(document.visibilityState==='hidden'&&window.PogSettings&&PogSettings.notify)PogSettings.notify(msg)}catch(e){}}
async function watchOnce(){
  if(wBusy||!window.PogCloud||!cl().user||!cl().user()||cl().mode==='demo')return;wBusy=true;
  try{var me=cl().user().id,since=new Date(Date.now()-3*864e5).toISOString(),db=chStore(),dirty=false;
    var chs=rows(await rest('GET','/rest/v1/challenges?select=id,title,ends_at&ends_at=gt.'+enc(since)));
    for(var i=0;i<chs.length;i++){var c=chs[i],board=rows(await rpc('challenge_board',{p_challenge:c.id})),idx=board.findIndex(function(r){return r.uid===me}),prev=db[c.id]||{};
      if(idx<0)continue;var ended=new Date(c.ends_at).getTime()<=Date.now(),above=board.slice(0,idx).map(function(r){return r.uid});
      if(ended){if(!prev.fin){var w=board[0];pushMsg(w&&w.uid===me?t('wonMsg')(c.title):t('endMsg')(c.title,(w&&w.name)||'?'));db[c.id]={fin:1};dirty=true}continue}
      if(prev.above){var passed=board.slice(0,idx).filter(function(r){return prev.above.indexOf(r.uid)<0});
        if(passed.length)pushMsg(t('ovr')(passed[0].name||'Alguém',c.title))}
      if(JSON.stringify(prev.above)!==JSON.stringify(above)){db[c.id]={above:above};dirty=true}}
    if(dirty)chStore(db)}catch(e){/* tabelas ainda não criadas ou sem rede: ignora */}finally{wBusy=false}}
function startWatch(){clearInterval(wTimer);setTimeout(watchOnce,6000);wTimer=setInterval(function(){if(document.visibilityState==='visible')watchOnce()},120000)}
document.addEventListener('visibilitychange',function(){if(document.visibilityState==='visible')setTimeout(watchOnce,1500)});
function bootWatch(){try{if(window.PogCloud){PogCloud.onAuth(function(u){if(u)startWatch();else clearInterval(wTimer)});if(PogCloud.user&&PogCloud.user())startWatch()}}catch(e){}}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',bootWatch);else setTimeout(bootWatch,0);
function askNotif(){try{if('Notification' in window&&Notification.permission==='default')Notification.requestPermission()}catch(e){}}

/* ---------- comentários por episódio ---------- */
async function thread(ep,title){
  var old=$('#sc-cm');if(old)old.remove();
  var el=document.createElement('div');el.id='sc-cm';el.className='sc-modal';el.setAttribute('role','dialog');el.setAttribute('aria-modal','true');el.setAttribute('aria-label',t('cmT'));
  el.innerHTML='<div class="sc-modal-card"><div class="sc-mh"><h3>💬 '+esc(t('cmT'))+'</h3><button class="sc-x" aria-label="'+esc(t('cmClose'))+'">×</button></div><p class="sc-tip">'+esc(title||'')+'</p><div class="sc-cl" id="sc-cl"><p class="pg-empty">'+esc(t('loading'))+'</p></div><form class="sc-cf"><textarea maxlength="800" rows="2" placeholder="'+esc(t('cmPh'))+'" required></textarea><button class="pg-btn" type="submit">'+esc(t('cmSend'))+'</button></form></div>';
  document.body.appendChild(el);
  var close=function(){el.remove()};$('.sc-x',el).onclick=close;el.onclick=function(e){if(e.target===el)close()};
  var logged=C()&&C().user&&C().user()&&cl()&&cl().mode!=='demo',me=logged?C().user().id:null,box=$('#sc-cl',el),fm=$('.sc-cf',el);
  if(!logged){box.innerHTML='<p class="pg-empty">'+esc(t('needLogin'))+'</p>';fm.hidden=true;return}
  async function load(){try{
    var rs=rows(await rest('GET','/rest/v1/episode_comments?select=id,body,created_at,uid,profiles(name,avatar)&ep=eq.'+encodeURIComponent(ep)+'&order=created_at.desc&limit=50'));
    box.innerHTML=rs.length?rs.map(function(r){var p=r.profiles||{};return '<div class="sc-cmt"><b>'+esc(p.avatar||'🙂')+' '+esc(r.uid===me?t('you'):(p.name||'Aluno'))+'</b><small>'+esc(new Date(r.created_at).toLocaleDateString(U().L0()==='es'?'es':'pt-BR'))+'</small><p>'+esc(r.body)+'</p>'+(r.uid===me?'<button class="sc-del" data-id="'+r.id+'">'+esc(t('cmDel'))+'</button>':'')+'</div>'}).join(''):'<p class="pg-empty">'+esc(t('cmNone'))+'</p>';
  }catch(e){box.innerHTML='<p class="pg-empty">'+esc(errMsg(e))+'</p>';fm.hidden=true}}
  box.onclick=async function(e){var b=e.target.closest('.sc-del');if(!b)return;try{await rest('DELETE','/rest/v1/episode_comments?id=eq.'+encodeURIComponent(b.dataset.id));load()}catch(x){}};
  fm.onsubmit=async function(ev){ev.preventDefault();var ta=fm.querySelector('textarea'),v=ta.value.trim();if(!v)return;
    try{await rest('POST','/rest/v1/episode_comments',{ep:ep,body:v});ta.value='';load()}catch(e){box.insertAdjacentHTML('afterbegin','<p class="sc-err">'+esc(errMsg(e))+'</p>')}};
  load()}
/* botão na tela final do episódio */
var _r=window.render;
if(typeof _r==='function')window.render=function(){var r=_r.apply(this,arguments);
  try{if(typeof P!=='undefined'&&P&&!P.isTest&&P.steps&&P.steps[P.i]==='done'&&P.e){var st0=document.getElementById('pstage');
    if(st0&&!document.getElementById('sc-open')){var b=document.createElement('button');b.id='sc-open';b.className='pg-btn ghost sc-open';b.textContent=t('cmBtn');
      var ep=String(P.cid)+'-'+P.e.n;b.onclick=function(){thread(ep,P.e.t||'')};st0.appendChild(b)}}}catch(e){}
  return r};
window.PogSocial={page:page,thread:thread,watchOnce:watchOnce,exportCsv:exportCsv};
})();
