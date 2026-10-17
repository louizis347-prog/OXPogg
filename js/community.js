/* Pogglot · área de membros: login, chat, parceiros e ranking. Depende de PogCloud (js/cloud.js) e PogUI (js/ui.js). */
(function(){
'use strict';
const C={
 pt:{signin:'Entrar',signup:'Criar conta',title:'Área de membros',sub:'Converse com outros alunos, ache parceiros de idioma e entre no ranking.',
  email:'E-mail',pass:'Senha (mín. 6 caracteres)',name:'Seu nome',avatar:'Escolha um avatar',speak:'Eu falo',learn:'Quero aprender',go1:'Entrar',go2:'Criar minha conta',
  forgot:'Esqueci a senha',sent:'Se o e-mail existir, enviamos um link para redefinir a senha.',demo:'Modo demonstração: as contas e mensagens ficam só neste navegador e os membros de exemplo são fictícios. Para ativar a comunidade real, configure o backend (veja backend/README.md).',
  weekTab:'Semana',askTab:'Perguntas',adminTab:'Moderação',notif:'Ativar avisos de mensagens',chat:'Chat',partners:'Parceiros',rooms:'Salas',dms:'Conversas privadas',noDm:'Nenhuma conversa privada ainda. Procure alguém em Parceiros.',pick:'Escolha uma sala para conversar.',
  write:'Escreva uma mensagem…',send:'Enviar',fix:'Corrigir',report:'Denunciar',reported:'Denúncia enviada. Obrigado!',block:'Bloquear',blocked:'Usuário bloqueado.',
  fixing:'Corrigindo a mensagem de',cancel:'Cancelar',fixTag:'✏️ Correção',noMsgs:'Ninguém falou aqui ainda. Seja o primeiro!',back:'Voltar',you:'Você',
  search:'Buscar por nome',speaks:'Fala',learns:'Aprende',any:'Qualquer idioma',match:'✨ Combinam comigo',talk:'Conversar',noMem:'Nenhum membro encontrado com esses filtros.',
  rank:'Ranking',all:'Todos os idiomas',xp:'XP',streak:'Sequência',eps:'Episódios',pts:'pts',days:'dias',epsU:'eps',yourPos:'Sua posição',noRank:'Ninguém no ranking ainda. Estude um episódio e apareça aqui!',
  logged:'Conectado como',out:'Sair',loading:'Carregando…',errNet:'Sem conexão. Tente de novo.',fixOf:'Em resposta a',
  general:'Geral',lg:'Liga'},
 es:{signin:'Entrar',signup:'Crear cuenta',title:'Área de miembros',sub:'Conversa con otros alumnos, encuentra compañeros de idioma y entra en el ranking.',
  email:'Correo',pass:'Contraseña (mín. 6 caracteres)',name:'Tu nombre',avatar:'Elige un avatar',speak:'Hablo',learn:'Quiero aprender',go1:'Entrar',go2:'Crear mi cuenta',
  forgot:'Olvidé mi contraseña',sent:'Si el correo existe, enviamos un enlace para restablecer la contraseña.',demo:'Modo demostración: las cuentas y los mensajes se guardan solo en este navegador y los miembros de ejemplo son ficticios. Para activar la comunidad real, configura el backend (mira backend/README.md).',
  weekTab:'Semana',askTab:'Preguntas',adminTab:'Moderación',notif:'Activar avisos de mensajes',chat:'Chat',partners:'Compañeros',rooms:'Salas',dms:'Conversaciones privadas',noDm:'Aún no hay conversaciones privadas. Busca a alguien en Compañeros.',pick:'Elige una sala para conversar.',
  write:'Escribe un mensaje…',send:'Enviar',fix:'Corregir',report:'Denunciar',reported:'Denuncia enviada. ¡Gracias!',block:'Bloquear',blocked:'Usuario bloqueado.',
  fixing:'Corrigiendo el mensaje de',cancel:'Cancelar',fixTag:'✏️ Corrección',noMsgs:'Nadie ha hablado aquí todavía. ¡Sé el primero!',back:'Volver',you:'Tú',
  search:'Buscar por nombre',speaks:'Habla',learns:'Aprende',any:'Cualquier idioma',match:'✨ Hacen match conmigo',talk:'Conversar',noMem:'No se encontraron miembros con esos filtros.',
  rank:'Ranking',all:'Todos los idiomas',xp:'XP',streak:'Racha',eps:'Episodios',pts:'pts',days:'días',epsU:'eps',yourPos:'Tu posición',noRank:'Aún no hay nadie en el ranking. ¡Estudia un episodio y aparece aquí!',
  logged:'Sesión iniciada como',out:'Salir',loading:'Cargando…',errNet:'Sin conexión. Inténtalo de nuevo.',fixOf:'En respuesta a',
  general:'General',lg:'Liga'}
};
const U=()=>window.PogUI,k=key=>{const L=U().L0();return (C[L][key]!=null?C[L][key]:C.pt[key])},esc=s=>U().esc(s);
const LN={pt:{pt:'Português',es:'Espanhol',en:'Inglês',fr:'Francês',de:'Alemão',it:'Italiano'},es:{pt:'Portugués',es:'Español',en:'Inglés',fr:'Francés',de:'Alemán',it:'Italiano'}};
const lname=id=>(LN[U().L0()]||LN.pt)[id]||id;
const AVS=['🙂','😎','🤓','🦊','🐼','🐯','🦉','🐙','🌻','🚀','🎧','📚'];
const LIDS=['en','es','pt','fr','de','it'];
const state={tab:'chat',room:null,unsub:null,init:null,fixing:null,msgs:[],peer:null};
const $=(s,r)=>(r||document).querySelector(s);
const cloud=()=>window.PogCloud;
const user=()=>cloud()&&cloud().user();
function ready(){if(!state.init)state.init=cloud().init().catch(e=>console.warn('PogCloud.init',e));return state.init}
function stopSub(){if(state.unsub){try{state.unsub()}catch(e){}state.unsub=null}}
function shell(inner,tab){
  const L=U().L0();
  app.innerHTML=topbar(L)+`<main class="pg">${cloud().mode==='demo'?`<div class="pg-demo">🧪 <span>${esc(k('demo'))}</span></div>`:''}${inner}</main>`;
  U().mountNav();scrollTo(0,0);
}
function subtabs(active){
  const T=U().T2||(x=>x);
  return `<div class="pg-subtabs" role="tablist"><button data-ct="rank" aria-pressed="${active==='rank'}">🏆 ${esc(T('rank'))}</button><button data-ct="chat" aria-pressed="${active==='chat'}">💬 ${k('chat')}</button><button data-ct="ask" aria-pressed="${active==='ask'}">❓ ${(window.PogForum?'':'')}${k('askTab')}</button><button data-ct="partners" aria-pressed="${active==='partners'}">🤝 ${k('partners')}</button><button data-ct="profile" aria-pressed="${active==='profile'}">👤</button>${state.admin?`<button data-ct="admin" aria-pressed="${active==='admin'}">🛡️ ${k('adminTab')}</button>`:''}</div>`;
}
function timeFmt(ts){const d=new Date(ts),n=new Date(),hh=d.toLocaleTimeString([], {hour:'2-digit',minute:'2-digit'});
  return d.toDateString()===n.toDateString()?hh:d.toLocaleDateString(U().L0()==='es'?'es':'pt-BR',{day:'2-digit',month:'short'})+' '+hh}
function roomLabel(r){
  if(LIDS.includes(r.id)){const l=U().LANG(r.id);return{ic:`<span class="mono" style="--c:${l.c};--cd:${l.cd};width:38px;height:38px;font-size:14px;border-radius:12px">${l.mono}</span>`,name:lname(r.id)}}
  if(r.id==='geral')return{ic:'💬',name:k('general')};
  return{ic:esc(r.emoji||'💬'),name:r.name};
}
const goto=(tab,arg)=>open(tab,arg);

/* ---------- entrada ---------- */
async function open(tab,arg){
  stopSub();state.tab=tab;
  await ready();
  U().cur=tab==='rank'?'rank':'comm';
  try{history.pushState(null,'',tab==='rank'?'#/rank':tab==='partners'?'#/comm/partners':tab==='ask'?'#/comm/ask':tab==='profile'?'#/comm/profile':tab==='admin'?'#/comm/admin':'#/comm')}catch(e){}
  if(tab==='rank'){if(user())U().syncNow();return rankPage()}
  if(tab==='auth'||!user())return authPage(tab==='auth'?'chat':tab,arg);
  U().syncNow();
  if(tab==='partners')return partnersPage();
  if(state.admin==null&&window.PogExtras)state.admin=await PogExtras.isAdmin();
  if(tab==='ask'&&window.PogForum)return PogForum.page(arg);
  if(tab==='profile'&&window.PogExtras)return PogExtras.profile(arg);
  if(tab==='admin'&&window.PogExtras)return PogExtras.admin();
  return chatPage(arg);
}

/* ---------- login / cadastro ---------- */
function authPage(next,arg,mode){
  mode=mode||'signin';const L=U().L0();
  const native=L==='es'?'es':'pt';
  let av=AVS[0],learn=new Set([L==='es'?'pt':'en']);
  const learnChips=()=>LIDS.filter(i=>i!==$('#a-native')?.value).map(i=>{const l=U().LANG(i);return `<button type="button" class="pg-chip" data-learn="${i}" aria-pressed="${learn.has(i)}" style="--c:${l.c};--cd:${l.cd}">${esc(lname(i))}</button>`}).join('');
  shell(`<section class="pg-card pg-auth"><h2>${k('title')}</h2><p class="sub">${k('sub')}</p>
   <div class="tabs"><button data-m="signin" aria-pressed="${mode==='signin'}">${k('signin')}</button><button data-m="signup" aria-pressed="${mode==='signup'}">${k('signup')}</button></div>
   <form id="authf" novalidate>
    ${mode==='signup'?`<label class="pg-field"><span>${k('name')}</span><input id="a-name" maxlength="40" autocomplete="nickname"></label>
    <div class="pg-field"><span>${k('avatar')}</span><div class="pg-avpick" id="a-av">${AVS.map((a,i)=>`<button type="button" data-av="${a}" aria-pressed="${i===0}">${a}</button>`).join('')}</div></div>
    <label class="pg-field"><span>${k('speak')}</span><select id="a-native">${LIDS.map(i=>`<option value="${i}" ${i===native?'selected':''}>${esc(lname(i))}</option>`).join('')}</select></label>
    <div class="pg-field"><span>${k('learn')}</span><div class="pg-chips" id="a-learn">${learnChips()}</div></div>`:''}
    <label class="pg-field"><span>${k('email')}</span><input id="a-email" type="email" autocomplete="email" inputmode="email"></label>
    <label class="pg-field"><span>${k('pass')}</span><input id="a-pass" type="password" autocomplete="${mode==='signup'?'new-password':'current-password'}"></label>
    <div class="pg-err" id="a-err" role="alert"></div>
    <button class="pg-btn" style="width:100%" id="a-go">${mode==='signup'?k('go2'):k('go1')}</button>
    ${mode==='signin'?`<p style="text-align:center;margin:12px 0 0"><button type="button" id="a-forgot" style="color:#5B2FE0;font-weight:800">${k('forgot')}</button></p>`:''}
   </form></section>`);
  const f=$('#authf');
  $('.pg-auth .tabs').onclick=e=>{const b=e.target.closest('[data-m]');if(b)authPage(next,arg,b.dataset.m)};
  if(mode==='signup'){
    $('#a-av').onclick=e=>{const b=e.target.closest('[data-av]');if(!b)return;av=b.dataset.av;$('#a-av').querySelectorAll('button').forEach(x=>x.setAttribute('aria-pressed',x===b))};
    $('#a-learn').onclick=e=>{const b=e.target.closest('[data-learn]');if(!b)return;const i=b.dataset.learn;learn.has(i)?learn.delete(i):learn.add(i);b.setAttribute('aria-pressed',learn.has(i))};
    $('#a-native').onchange=()=>{learn.delete($('#a-native').value);$('#a-learn').innerHTML=learnChips()};
  }
  const fp=$('#a-forgot');if(fp)fp.onclick=async()=>{const em=$('#a-email').value.trim();const er=$('#a-err');if(!em){er.textContent=k('email')+'?';return}
    try{await cloud().resetPassword(em);er.className='pg-ok';er.textContent=k('sent')}catch(x){er.className='pg-err';er.textContent=x.message}};
  f.onsubmit=async ev=>{ev.preventDefault();const er=$('#a-err'),go=$('#a-go');er.className='pg-err';er.textContent='';go.disabled=true;
    try{
      const email=$('#a-email').value.trim(),pass=$('#a-pass').value;
      if(mode==='signup'){
        const name=$('#a-name').value.trim()||email.split('@')[0];
        await cloud().signUp({email,password:pass,name,avatar:av,native:$('#a-native').value,learning:[...learn]});
      }else await cloud().signIn(email,pass);
      U().syncNow();
      open(next==='auth'?'chat':next,arg);
    }catch(x){er.textContent=x.message||k('errNet');go.disabled=false}};
}

/* ---------- chat ---------- */
async function chatPage(roomArg){
  const me=user(),rooms=cloud().rooms.slice();
  const mine=new Set([me.native,...(me.learning||[])]);
  rooms.sort((a,b)=>(mine.has(b.id)?1:0)-(mine.has(a.id)?1:0)||0);
  const g=rooms.findIndex(r=>r.id==='geral');if(g>0){rooms.unshift(rooms.splice(g,1)[0])}
  let dms=[];try{dms=await cloud().dmList()}catch(e){}
  const room=roomArg||state.room||'geral';state.room=room;
  shell(`${subtabs('chat')}<section class="pg-chat ${roomArg?'in-conv':''}" id="pgchat">
    <aside class="pg-card pg-rooms"><h4>${k('rooms')}</h4>${rooms.map(r=>{const l=roomLabel(r);return `<button class="pg-room" data-room="${r.id}" aria-current="${room===r.id}"><span class="ic">${l.ic}</span><span class="tx">${esc(l.name)}</span></button>`}).join('')}
     ${notifBtn()}<h4>${k('dms')}</h4>${dms.length?dms.map(d=>`<button class="pg-room" data-room="${esc(d.room)}" aria-current="${room===d.room}"><span class="ic">${esc(d.peer.avatar||'🙂')}</span><span class="tx">${esc(d.peer.name)}<small>${esc(d.last?d.last.text:'')}</small></span></button>`).join(''):`<p class="pg-empty" style="padding:8px;font-size:13px">${k('noDm')}</p>`}</aside>
    <div class="pg-card pg-conv" id="pgconv"></div></section>`);
  wireTabs();
  const nb=$('#c-notif');if(nb)nb.onclick=e=>{e.stopPropagation();Notification.requestPermission().then(()=>{nb.remove();startInbox()})};
  $('#pgchat').onclick=e=>{const b=e.target.closest('.pg-room[data-room]');if(!b)return;e.stopPropagation();openRoom(b.dataset.room,true)};
  openRoom(room,!!roomArg);
}
function wireTabs(){const s=$('.pg-subtabs');if(s)s.onclick=e=>{const b=e.target.closest('[data-ct]');if(b)open(b.dataset.ct)}}

async function openRoom(room,focus){
  stopSub();state.room=room;state.fixing=null;state.msgs=[];
  const chat=$('#pgchat');if(!chat)return;if(focus)chat.classList.add('in-conv');
  chat.querySelectorAll('.pg-room').forEach(b=>b.setAttribute('aria-current',b.dataset.room===room));
  const conv=$('#pgconv'),me=user();let title='',sub='',isDm=room.startsWith('dm:'),peerId=null;
  if(isDm){peerId=room.split(':').filter(x=>x!=='dm'&&x!==me.id)[0];
    try{state.peer=await cloud().getProfile(peerId)}catch(e){state.peer=null}
    const p=state.peer||{name:'?',avatar:'🙂'};title=`<span class="av" style="font-size:24px">${esc(p.avatar||'🙂')}</span> ${esc(p.name)}`;
  }else{const r=cloud().rooms.find(x=>x.id===room)||{id:room,name:room,emoji:'💬'},l=roomLabel(r);title=`${l.ic} ${esc(l.name)}`}
  conv.innerHTML=`<div class="hd"><button class="bk pg-btn ghost sm" id="c-back" aria-label="${k('back')}">←</button><span style="display:flex;align-items:center;gap:8px;flex:1;min-width:0">${title}</span>${isDm?`<button class="pg-btn ghost sm" id="c-block">${k('block')}</button>`:''}</div>
   <div class="pg-msgs" id="pgmsgs" aria-live="polite"><p class="pg-empty">${k('loading')}</p></div>
   <div id="c-fixbar"></div>
   <form class="pg-compose" id="c-form"><input class="pg-in" id="c-in" maxlength="1000" placeholder="${esc(k('write'))}" autocomplete="off">${window.PogExtras?PogExtras.micBtn():''}<button class="pg-btn" id="c-send">${k('send')}</button></form>`;
  $('#c-back').onclick=()=>{stopSub();chat.classList.remove('in-conv')};
  const bl=$('#c-block');if(bl)bl.onclick=async()=>{if(!confirm(k('block')+'?'))return;try{await cloud().block(peerId);alert(k('blocked'));open('chat','geral')}catch(e){alert(e.message)}};
  const box=$('#pgmsgs');
  try{
    state.msgs=await cloud().messages(room,{limit:60});
    renderMsgs(true);
    const last=state.msgs.length?state.msgs[state.msgs.length-1].id:null;
    state.unsub=cloud().subscribe(room,news=>{
      if(!document.getElementById('pgmsgs')||state.room!==room){stopSub();return}
      const have=new Set(state.msgs.map(m=>m.id)),add=news.filter(m=>!have.has(m.id));
      if(add.length){state.msgs.push(...add);renderMsgs(false)}
    },{after:last});
  }catch(e){box.innerHTML=`<p class="pg-empty">${esc(e.message||k('errNet'))}</p>`}
  $('#c-form').onsubmit=async ev=>{ev.preventDefault();const inp=$('#c-in'),txt=inp.value.trim();if(!txt)return;
    const fx=state.fixing;$('#c-send').disabled=true;
    try{const m=await cloud().send(room,txt,{fixOf:fx?fx.id:null});inp.value='';
      if(!state.msgs.some(x=>x.id===m.id))state.msgs.push(m);
      state.fixing=null;fixBar();renderMsgs(true);
      U().bump('msgs');if(fx&&fx.uid!==user().id)U().bump('fixes');
    }catch(x){alert(x.message||k('errNet'))}
    finally{const b=$('#c-send');if(b)b.disabled=false;inp.focus()}};
  const mic=$('[data-mic]');if(mic)mic.onclick=()=>PogExtras.record($('#c-form').parentNode,async(blob)=>{
    const path=await cloud().uploadVoice(blob);const m=await cloud().send(room,'🎤',{audio:path});
    if(!state.msgs.some(x=>x.id===m.id))state.msgs.push(m);renderMsgs(true);U().bump('msgs')});
  box.onclick=e=>{
    const f=e.target.closest('[data-fix]');if(f){const m=state.msgs.find(x=>String(x.id)===f.dataset.fix);if(m){state.fixing=m;fixBar();const inp=$('#c-in');inp.value=m.text;inp.focus();inp.setSelectionRange(inp.value.length,inp.value.length)}return}
    const r=e.target.closest('[data-rep]');if(r){const why=prompt(k('report')+'?','');if(why===null)return;cloud().report(r.dataset.rep,why||'').then(()=>alert(k('reported'))).catch(x=>alert(x.message))}
  };
}
function fixBar(){const b=$('#c-fixbar');if(!b)return;const f=state.fixing;
  b.innerHTML=f?`<div class="pg-demo" style="margin:0;border-radius:0;border-width:2px 0;background:#EAFBF2;border-color:#9FE0BE;color:#14573A">✏️ <span>${k('fixing')} <b>${esc(f.name)}</b>: “${esc(f.text.slice(0,60))}”</span><button style="margin-left:auto;font-weight:900" id="c-fixno">${k('cancel')}</button></div>`:'';
  const n=$('#c-fixno');if(n)n.onclick=()=>{state.fixing=null;fixBar();$('#c-in').value=''}}
function renderMsgs(stick){
  const box=$('#pgmsgs');if(!box)return;const me=user().id;
  const near=box.scrollHeight-box.scrollTop-box.clientHeight<90;
  if(!state.msgs.length){box.innerHTML=`<p class="pg-empty">${k('noMsgs')}</p>`;return}
  const byId=new Map(state.msgs.map(m=>[m.id,m]));
  box.innerHTML=state.msgs.map(m=>{const mine=m.uid===me,orig=m.fixOf!=null?byId.get(m.fixOf):null;
    return `<div class="pg-msg ${mine?'me':''} ${m.fixOf!=null?'fix':''}"><span class="av">${esc(m.avatar||'🙂')}</span><div><div class="bb">${mine?'':`<span class="who">${esc(m.name||'?')}</span>`}${m.fixOf!=null?`<span class="pg-fixtag">${k('fixTag')}</span>${orig?`<span class="pg-quote">${esc(orig.text)}</span>`:''}`:''}${m.audio?(window.PogExtras?PogExtras.voiceHTML(m.audio):''):esc(m.text)}</div>
     <div class="meta"><span>${timeFmt(m.ts)}</span>${mine?'':`<button data-fix="${esc(m.id)}">✏️ ${k('fix')}</button><button data-rep="${esc(m.id)}">🚩 ${k('report')}</button>`}</div></div></div>`}).join('');
  if(stick||near)box.scrollTop=box.scrollHeight;
}

/* ---------- parceiros ---------- */
let pf={q:'',native:'',learning:'',match:true};
async function partnersPage(){
  const me=user();
  if(pf.match&&pf.native===''&&pf.learning===''){pf.native=(me.learning||[])[0]||'';pf.learning=me.native||''}
  shell(`${subtabs('partners')}
   <div class="pg-filters"><input class="pg-in" id="p-q" placeholder="${esc(k('search'))}" value="${esc(pf.q)}">
    <select class="pg-in" id="p-n" style="flex:none;width:auto"><option value="">${k('speaks')}: ${k('any')}</option>${LIDS.map(i=>`<option value="${i}" ${pf.native===i?'selected':''}>${k('speaks')}: ${esc(lname(i))}</option>`).join('')}</select>
    <select class="pg-in" id="p-l" style="flex:none;width:auto"><option value="">${k('learns')}: ${k('any')}</option>${LIDS.map(i=>`<option value="${i}" ${pf.learning===i?'selected':''}>${k('learns')}: ${esc(lname(i))}</option>`).join('')}</select>
    <button class="pg-btn sm" id="p-match">${k('match')}</button></div>
   <div id="pg-pod"></div>
   <section class="pg-members" id="pgmem"><p class="pg-empty">${k('loading')}</p></section>`);
  wireTabs();
  if(window.PogExtras&&cloud().mode==='supabase')PogExtras.partner(me).then(h=>{const b=$('#pg-pod');if(b)b.innerHTML=h});
  const run=async()=>{
    pf.q=$('#p-q').value;pf.native=$('#p-n').value;pf.learning=$('#p-l').value;
    const box=$('#pgmem');
    try{const list=await cloud().members({q:pf.q,native:pf.native||null,learning:pf.learning||null,limit:60});
      if(!document.getElementById('pgmem'))return;
      box.innerHTML=list.length?list.map(m=>`<article class="pg-card pg-mem"><div class="top" data-prof="${esc(m.id)}" style="cursor:pointer"><span class="av">${esc(m.avatar||'🙂')}</span><div><b>${esc(m.name)}${m.demo?'<span class="pg-badge-demo">demo</span>':''}</b><small>${esc(U().league(m.xp||0).name)} · ${m.xp||0} XP</small></div></div>
        ${m.bio?`<p class="bio">${esc(m.bio)}</p>`:''}
        <div class="pg-exch"><span class="sp">${k('speaks')}: ${esc(lname(m.native))}</span>${(m.learning||[]).map(i=>`<span class="le">${k('learns')}: ${esc(lname(i))}</span>`).join('')}</div>
        <button class="pg-btn sm" data-dm="${esc(m.id)}">💬 ${k('talk')}</button></article>`).join(''):`<p class="pg-empty" style="grid-column:1/-1">${k('noMem')}</p>`;
    }catch(e){box.innerHTML=`<p class="pg-empty" style="grid-column:1/-1">${esc(e.message||k('errNet'))}</p>`}
  };
  let tm;$('#p-q').oninput=()=>{clearTimeout(tm);tm=setTimeout(run,300)};$('#p-n').onchange=run;$('#p-l').onchange=run;
  $('#p-match').onclick=()=>{$('#p-n').value=(me.learning||[])[0]||'';$('#p-l').value=me.native||'';run()};
  $('#pgmem').onclick=e=>{const b=e.target.closest('[data-dm]');if(b)open('chat',cloud().dmRoom(b.dataset.dm))};
  $('#pg-pod').onclick=e=>{const b=e.target.closest('[data-dm]');if(b)open('chat',cloud().dmRoom(b.dataset.dm))};
  run();
}

/* ---------- ranking ---------- */
let rf={lang:null,by:'xp'};
async function rankPage(){
  const L=U().L0(),T=U().T2||(x=>x),u=user();
  shell(`<div class="p2c-head"><h1>${esc(T('commT'))}</h1><p>${esc(T('commSub'))}</p></div>${subtabs('rank')}
   ${u?'':`<div class="p2rank-join"><div class="tx"><b>${esc(T('join'))}</b><small>${esc(T('joinSub'))}</small></div><button class="p2btn light" data-go="auth">${esc(T('signin'))}</button></div>`}
   <div class="p2rfilters" id="r-lang"><button class="p2chip" data-l="" aria-pressed="${!rf.lang}">${k('all')}</button>${LIDS.map(i=>`<button class="p2chip" data-l="${i}" aria-pressed="${rf.lang===i}">${esc(lname(i))}</button>`).join('')}</div>
   <div class="pg-subtabs" id="r-by"><button data-b="xp" aria-pressed="${rf.by==='xp'}">⚡ ${k('xp')}</button><button data-b="streak" aria-pressed="${rf.by==='streak'}">🔥 ${k('streak')}</button><button data-b="week" aria-pressed="${rf.by==='week'}">📅 ${k('weekTab')}</button><button data-b="eps" aria-pressed="${rf.by==='eps'}">📚 ${k('eps')}</button></div>
   <div id="r-body"><p class="p2empty">${k('loading')}</p></div>`);
  $('.pg-subtabs').onclick=e=>{const b=e.target.closest('[data-ct]');if(b)open(b.dataset.ct)};
  $('#r-lang').onclick=e=>{const b=e.target.closest('[data-l]');if(b){rf.lang=b.dataset.l||null;rankPage()}};
  $('#r-by').onclick=e=>{const b=e.target.closest('[data-b]');if(b){rf.by=b.dataset.b;rankPage()}};
  const body=$('#r-body');
  try{
    if(u){try{await cloud().flush()}catch(e){}}
    if(rf.by==='week'&&u&&window.PogExtras)return PogExtras.weekly(body);
    const list=await cloud().leaderboard({lang:rf.lang,by:rf.by==='week'?'xp':rf.by,limit:50});
    if(!document.getElementById('r-body'))return;
    if(!list.length){body.innerHTML=`<p class="p2empty">${k('noRank')}</p>`;return}
    const me=u?u.id:null,unit=rf.by==='xp'?k('pts'):rf.by==='streak'?k('days'):k('epsU');
    const sc=m=>(m.score!=null?m.score:(rf.by==='xp'?m.xp:rf.by==='streak'?m.streak:m.epsTotal))||0;
    const top=list.slice(0,3),rest=list.slice(3);
    const ord=top.length===3?[top[1],top[0],top[2]]:top;
    const pod=m=>{const idx=list.indexOf(m)+1;return `<div class="pd k${idx}" data-prof="${esc(m.id)}" style="cursor:pointer"><span class="md">${idx}</span><div class="av">${esc(m.avatar||'🙂')}</div><b>${esc(m.name)}${m.id===me?' ('+k('you')+')':''}</b><div class="sc">${sc(m)}</div><small>${unit}</small></div>`};
    const row=m=>{const lg=U().league(m.xp||0);return `<div class="p2row ${m.id===me?'me':''}" data-prof="${esc(m.id)}" style="cursor:pointer"><span class="pos">${m.rank||list.indexOf(m)+1}</span><span class="av">${esc(m.avatar||'🙂')}</span><div class="nm"><b>${esc(m.name)}${m.id===me?' ('+k('you')+')':''}${m.demo?'<span class="dm">demo</span>':''}</b><small><span class="lg" style="--lc:${lg.color}">${lg.name}</span>${esc(lname(m.native))} → ${(m.learning||[]).map(lname).map(esc).join(', ')}</small></div><span class="pts">${sc(m)} <small>${unit}</small></span></div>`};
    const mine=me&&list.find(m=>m.id===me);
    body.innerHTML=`${mine?`<div class="p2rank-me">${esc(T('yourPos'))} <b>#${mine.rank||list.indexOf(mine)+1}</b></div>`:''}
     <div class="p2pod">${ord.map(pod).join('')}</div>${rest.length?`<div class="p2rows">${rest.map(row).join('')}</div>`:''}`;
  }catch(e){body.innerHTML=`<p class="p2empty">${esc(e.message||k('errNet'))}</p>`}
}


/* ---------- avisos de mensagens privadas ---------- */
let inboxStop=null,unread=0;const baseTitle=document.title;
function notify(m){
  const title=(m.name||'Pogglot'),opt={body:String(m.text||'').slice(0,120),tag:'pg-dm',icon:'icons/icon-192.png',data:{room:m.room}};
  try{
    if(navigator.serviceWorker&&navigator.serviceWorker.getRegistration){
      navigator.serviceWorker.getRegistration().then(r=>{if(r&&r.showNotification)r.showNotification(title,opt);else{const n=new Notification(title,opt);n.onclick=()=>{window.focus();open('chat',m.room)}}}).catch(()=>{});
    }else{const n=new Notification(title,opt);n.onclick=()=>{window.focus();open('chat',m.room)}}
  }catch(e){}
}
function startInbox(){
  if(inboxStop||!user()||cloud().mode!=='supabase'||!cloud().watchInbox)return;
  inboxStop=cloud().watchInbox(msgs=>{
    const viewing=!document.hidden&&document.getElementById('pgmsgs');
    const fresh=msgs.filter(m=>!(viewing&&m.room===state.room));
    if(!fresh.length)return;
    if(document.hidden||!viewing){unread+=fresh.length;document.title='('+unread+') '+baseTitle}
    if(window.Notification&&Notification.permission==='granted'&&document.hidden)notify(fresh[fresh.length-1]);
  });
}
document.addEventListener('visibilitychange',()=>{if(!document.hidden&&unread){unread=0;document.title=baseTitle}});
function notifBtn(){
  if(!window.Notification||Notification.permission!=='default'||cloud().mode!=='supabase')return '';
  return `<button class="pg-btn ghost sm" id="c-notif" style="margin:8px 0">🔔 ${esc(k('notif'))}</button>`;
}
setTimeout(()=>{ready().then(()=>{startInbox();if(cloud().onAuth)cloud().onAuth(u=>{if(u)startInbox();else if(inboxStop){inboxStop();inboxStop=null}})})},2000);
window.PogComm={open,state,shell,subtabs,wireTabs,timeFmt,lname,user,LIDS,k};
})();
