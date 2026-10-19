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
  cmBtn:'💬 Dúvidas e comentários deste episódio',cmT:'Comentários do episódio',cmPh:'Escreva uma dúvida ou comentário…',cmSend:'Enviar',cmNone:'Seja o primeiro a comentar.',cmClose:'Fechar',cmDel:'Apagar',you:'Você'},
 es:{tab:'Clases',cls:'Clases',chs:'Desafíos',newC:'Crear clase',joinC:'Entrar con código',newCh:'Crear desafío',joinCh:'Entrar con código',name:'Nombre',days:'Duración (días)',code:'Código',create:'Crear',join:'Entrar',
  none:'Aún no hay nada.',open:'Abrir',back:'Volver',loading:'Cargando…',share:'Comparte este código con tus alumnos o amigos:',copy:'Copiar',copied:'¡Copiado!',
  roster:'Alumnos',xp:'XP',streak:'Racha',eps:'Episodios',ach:'Logros',teacher:'Profesor',leave:'Salir',del:'Borrar',confirmDel:'¿Borrar? No se puede deshacer.',confirmLeave:'¿Salir?',
  score:'XP ganado',ends:'termina en',endedAt:'terminado',days_:'días',winner:'Ganador',needLogin:'Inicia sesión para usar clases y desafíos.',
  off:'Este recurso aún no está activado en el servidor. Quien aloja la app debe ejecutar backend/social.sql en Supabase.',
  tipC:'Como profesor, crea una clase y pasa el código a tus alumnos. Verás XP, racha y episodios de cada uno.',tipCh:'Invita a amigos: gana quien consiga más XP durante el período.',
  cmBtn:'💬 Dudas y comentarios de este episodio',cmT:'Comentarios del episodio',cmPh:'Escribe una duda o comentario…',cmSend:'Enviar',cmNone:'Sé el primero en comentar.',cmClose:'Cerrar',cmDel:'Borrar',you:'Tú'}
};
var C=function(){return window.PogComm},U=function(){return window.PogUI},cl=function(){return window.PogCloud};
function t(k){var L=U().L0();return(S[L]&&S[L][k]!=null)?S[L][k]:S.pt[k]}
function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(m){return({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'})[m]})}
function $(s,r){return(r||document).querySelector(s)}
function rest(m,p,body){return cl().rest(m,p,body===undefined?{}:{body:body})}
function rpc(fn,body){return rest('POST','/rest/v1/rpc/'+fn,body||{})}
function errMsg(e){var m=String(e&&e.message||'');return /relation|schema cache|PGRST|does not exist|function public|Could not find/i.test(m)?t('off'):(m||t('off'))}
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
      else await(create?rpc('create_challenge',{p_title:fm.n.value.trim(),p_days:+fm.d.value||7}):rpc('join_challenge',{p_code:fm.c.value}));
      list()}catch(e){er.hidden=false;er.textContent=errMsg(e)}}}
async function detail(id,meta){
  var isC=st.tab==='classes',body=$('#sc-body'),me=C().user().id;body.innerHTML='<p class="pg-empty">'+esc(t('loading'))+'</p>';
  try{
    var data=await rpc(isC?'class_roster':'challenge_board',isC?{p_class:id}:{p_challenge:id});data=rows(data);
    var own=meta&&meta.owner===me,max=Math.max.apply(null,data.map(function(r){return isC?(+r.xp||0):(+r.score||0)}).concat([1]));
    var head='<button class="pg-btn ghost" id="sc-back">‹ '+esc(t('back'))+'</button><h3 class="sc-title">'+esc(meta?(meta.name||meta.title):'')+'</h3>';
    var share=own?'<div class="sc-share">'+esc(t('share'))+' <b class="sc-code">'+esc(meta.code)+'</b> <button class="pg-chip" id="sc-copy">'+esc(t('copy'))+'</button></div>':'';
    var tbl;
    if(isC)tbl='<div class="sc-table" role="table"><div class="sc-tr hd" role="row"><span>#</span><span>'+esc(t('roster'))+'</span><span>'+esc(t('xp'))+'</span><span>🔥</span><span>'+esc(t('eps'))+'</span><span>🏅</span></div>'+
      data.map(function(r,i){return '<div class="sc-tr'+(r.uid===me?' me':'')+'" role="row"><span>'+(i+1)+'</span><span class="nm">'+esc(r.avatar||'🙂')+' '+esc(r.name||'Aluno')+(r.is_owner?' <em>'+esc(t('teacher'))+'</em>':'')+'</span><span>'+(+r.xp||0)+'</span><span>'+(+r.streak||0)+'</span><span>'+sum(r.eps)+'</span><span>'+cnt(r.ach)+'</span></div>'}).join('')+'</div>';
    else{var ended=meta&&new Date(meta.ends_at).getTime()<Date.now();
      tbl='<p class="sc-tip">'+esc(meta?chSub(meta,'x'):'')+'</p><div class="sc-board">'+data.map(function(r,i){var w=Math.round((+r.score||0)/max*100);
        return '<div class="sc-bar'+(r.uid===me?' me':'')+'"><span class="nm">'+(i===0&&ended?'🏆 ':(i+1)+'. ')+esc(r.avatar||'🙂')+' '+esc(r.name||'Aluno')+'</span><i style="width:'+w+'%"></i><b>'+(+r.score||0)+' '+esc(t('score'))+'</b></div>'}).join('')+'</div>'}
    body.innerHTML=head+share+tbl+'<button class="pg-btn danger" id="sc-del">'+esc(own?t('del'):t('leave'))+'</button>';
    $('#sc-back').onclick=list;
    var cp=$('#sc-copy');if(cp)cp.onclick=function(){try{navigator.clipboard.writeText(meta.code)}catch(e){}cp.textContent=t('copied')};
    $('#sc-del').onclick=async function(){if(!confirm(own?t('confirmDel'):t('confirmLeave')))return;
      try{var base=isC?'classes':'challenges',mem=isC?'class_members?class_id=eq.':'challenge_members?challenge_id=eq.';
        if(own)await rest('DELETE','/rest/v1/'+base+'?id=eq.'+encodeURIComponent(id));
        else await rest('DELETE','/rest/v1/'+mem+encodeURIComponent(id)+'&uid=eq.'+encodeURIComponent(me));
        list()}catch(e){body.insertAdjacentHTML('beforeend','<p class="sc-err">'+esc(errMsg(e))+'</p>')}};
  }catch(e){body.innerHTML='<button class="pg-btn ghost" id="sc-back">‹ '+esc(t('back'))+'</button><p class="pg-empty">'+esc(errMsg(e))+'</p>';$('#sc-back').onclick=list}}

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
window.PogSocial={page:page,thread:thread};
})();
