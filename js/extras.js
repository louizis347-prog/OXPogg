/* Pogglot · extras da comunidade: voz, liga semanal, perfil público, convites, parceiro do dia, painel de moderação. */
(function(){
'use strict';
const S={
 pt:{rec:'Gravar voz',recording:'Gravando…',send:'Enviar',cancel:'Cancelar',play:'Ouvir',micDenied:'Não consegui usar o microfone. Libere a permissão do navegador.',voice:'🎤 Mensagem de voz',tooLong:'Limite de 60 segundos.',
  week:'Semana',weekT:'Liga da semana',weekSub:'Quem ganhou mais XP nesta semana na sua liga. Zera toda segunda-feira.',weekNo:'Ninguém pontuou nesta semana ainda. Estude e apareça aqui!',pts:'XP',you:'Você',league:'Liga',
  partner:'Parceiro do dia',partnerSub:'Fala o que você estuda e estuda o que você fala.',talk:'Conversar',profile:'Ver perfil',noPartner:'',
  prof:'Perfil',streak:'Sequência',days:'dias',eps:'Episódios',ach:'Conquistas',asked:'Perguntas',answered:'Respostas',useful:'Úteis recebidos',bestA:'Melhores respostas',invited:'Amigos convidados',
  speaks:'Fala',learns:'Aprende',block:'Bloquear',blocked:'Usuário bloqueado.',back:'Voltar',invite:'Convide amigos',inviteSub:'Para cada amigo que criar conta pelo seu link você ganha 100 XP (até 20 amigos).',copy:'Copiar link',copied:'Link copiado!',share:'Compartilhar',
  inviteText:'Venha estudar idiomas comigo no Pogglot!',support:'💜 Apoiar o Pogglot',loading:'Carregando…',err:'Sem conexão. Tente de novo.',
  admin:'Moderação',reports:'Denúncias',stats:'Estatísticas',noRep:'Nenhuma denúncia. 🎉',hide:'Ocultar',unhide:'Mostrar',del:'Apagar',mute:'Silenciar autor 24 h',unmute:'Tirar silêncio',
  hidden:'oculto',nRep:'denúncias',by:'por',msg:'Mensagem',q:'Pergunta',a:'Resposta',confirm:'Confirmar?',forbidden:'Sem permissão de administrador.',
  users:'Alunos',new7:'Novos (7 dias)',act7:'Ativos (7 dias)',act1:'Ativos (24 h)',qs:'Perguntas',unans:'Sem resposta',ans:'Respostas',msgs:'Mensagens',muted:'Silenciados',
  langs:'Episódios concluídos por idioma',learning:'Idiomas mais estudados',drop:'Onde mais abandonam (início sem concluir)',hard:'Episódios com menor nota média',noData:'Ainda sem dados.',ep:'Ep.',adminHow:'Para virar administrador, rode no SQL Editor: update public.profiles set is_admin = true where id = (select id from auth.users where email = \'seu@email.com\');'},
 es:{rec:'Grabar voz',recording:'Grabando…',send:'Enviar',cancel:'Cancelar',play:'Escuchar',micDenied:'No pude usar el micrófono. Permite el acceso en el navegador.',voice:'🎤 Mensaje de voz',tooLong:'Límite de 60 segundos.',
  week:'Semana',weekT:'Liga de la semana',weekSub:'Quién ganó más XP esta semana en tu liga. Se reinicia cada lunes.',weekNo:'Nadie ha puntuado esta semana. ¡Estudia y aparece aquí!',pts:'XP',you:'Tú',league:'Liga',
  partner:'Compañero del día',partnerSub:'Habla lo que estudias y estudia lo que hablas.',talk:'Conversar',profile:'Ver perfil',noPartner:'',
  prof:'Perfil',streak:'Racha',days:'días',eps:'Episodios',ach:'Logros',asked:'Preguntas',answered:'Respuestas',useful:'Útiles recibidos',bestA:'Mejores respuestas',invited:'Amigos invitados',
  speaks:'Habla',learns:'Aprende',block:'Bloquear',blocked:'Usuario bloqueado.',back:'Volver',invite:'Invita amigos',inviteSub:'Por cada amigo que cree su cuenta con tu enlace ganas 100 XP (hasta 20 amigos).',copy:'Copiar enlace',copied:'¡Enlace copiado!',share:'Compartir',
  inviteText:'¡Ven a estudiar idiomas conmigo en Pogglot!',support:'💜 Apoyar Pogglot',loading:'Cargando…',err:'Sin conexión. Inténtalo de nuevo.',
  admin:'Moderación',reports:'Denuncias',stats:'Estadísticas',noRep:'Ninguna denuncia. 🎉',hide:'Ocultar',unhide:'Mostrar',del:'Borrar',mute:'Silenciar autor 24 h',unmute:'Quitar silencio',
  hidden:'oculto',nRep:'denuncias',by:'por',msg:'Mensaje',q:'Pregunta',a:'Respuesta',confirm:'¿Confirmar?',forbidden:'Sin permiso de administrador.',
  users:'Alumnos',new7:'Nuevos (7 días)',act7:'Activos (7 días)',act1:'Activos (24 h)',qs:'Preguntas',unans:'Sin respuesta',ans:'Respuestas',msgs:'Mensajes',muted:'Silenciados',
  langs:'Episodios completados por idioma',learning:'Idiomas más estudiados',drop:'Dónde más abandonan (inicio sin terminar)',hard:'Episodios con menor nota media',noData:'Aún sin datos.',ep:'Ep.',adminHow:'Para ser administrador, ejecuta en el SQL Editor: update public.profiles set is_admin = true where id = (select id from auth.users where email = \'tu@correo.com\');'}
};
const C=()=>window.PogComm,U=()=>window.PogUI,cloud=()=>window.PogCloud;
const t=key=>{const L=U().L0();return (S[L]&&S[L][key]!=null)?S[L][key]:S.pt[key]};
const esc=s=>U().esc(s);
const $=(s,r)=>(r||document).querySelector(s);

/* ---------- voz ---------- */
let rec=null;
function fmt(s){s=Math.max(0,Math.round(s));return Math.floor(s/60)+':'+String(s%60).padStart(2,'0')}
function micBtn(){return cloud().voiceSupported&&cloud().voiceSupported()?`<button type="button" class="pg-btn ghost pg-mic" data-mic aria-label="${esc(t('rec'))}" title="${esc(t('rec'))}">🎤</button>`:''}
/* grava e entrega o arquivo; host = elemento que recebe a barra de gravação */
async function record(host,onSend){
  if(rec)return;
  let stream;try{stream=await navigator.mediaDevices.getUserMedia({audio:true})}catch(e){alert(t('micDenied'));return}
  const types=['audio/webm;codecs=opus','audio/webm','audio/mp4','audio/ogg;codecs=opus'];
  const mt=types.find(x=>window.MediaRecorder.isTypeSupported&&MediaRecorder.isTypeSupported(x))||'';
  const mr=new MediaRecorder(stream,mt?{mimeType:mt,audioBitsPerSecond:32000}:{audioBitsPerSecond:32000}),chunks=[];let t0=Date.now(),tick=null,cancelled=false;
  const bar=document.createElement('div');bar.className='pg-recbar';
  bar.innerHTML=`<span class="dot"></span><b id="rb-t">0:00</b><span>${esc(t('recording'))}</span><button type="button" class="pg-btn ghost sm" id="rb-c">${esc(t('cancel'))}</button><button type="button" class="pg-btn sm" id="rb-s">${esc(t('send'))}</button>`;
  host.appendChild(bar);
  const stop=()=>{clearInterval(tick);try{stream.getTracks().forEach(x=>x.stop())}catch(e){}bar.remove();rec=null};
  mr.ondataavailable=e=>{if(e.data&&e.data.size)chunks.push(e.data)};
  mr.onstop=async()=>{stop();if(cancelled||!chunks.length)return;const blob=new Blob(chunks,{type:mr.mimeType||mt||'audio/webm'});
    try{await onSend(blob,Math.round((Date.now()-t0)/1000))}catch(x){alert(x.message||t('err'))}};
  rec=mr;mr.start();
  tick=setInterval(()=>{const s=(Date.now()-t0)/1000;$('#rb-t',bar).textContent=fmt(s);if(s>=60){alert(t('tooLong'));mr.state!=='inactive'&&mr.stop()}},250);
  $('#rb-c',bar).onclick=()=>{cancelled=true;mr.state!=='inactive'&&mr.stop()};
  $('#rb-s',bar).onclick=()=>{mr.state!=='inactive'&&mr.stop()};
}
function voiceHTML(path){return `<button type="button" class="pg-voice" data-audio="${esc(path)}">▶ ${esc(t('play'))}</button>`}
let curAudio=null,curBtn=null;
async function playVoice(btn){
  if(curAudio){curAudio.pause();if(curBtn)curBtn.textContent='▶ '+t('play');if(curBtn===btn){curAudio=null;curBtn=null;return}}
  btn.textContent='…';
  try{const url=await cloud().voiceUrl(btn.dataset.audio);const a=new Audio(url);curAudio=a;curBtn=btn;
    a.onended=()=>{btn.textContent='▶ '+t('play');curAudio=null;curBtn=null};await a.play();btn.textContent='⏸ '+t('play')}
  catch(e){btn.textContent='▶ '+t('play');alert(e.message||t('err'))}
}
document.addEventListener('click',e=>{const b=e.target.closest&&e.target.closest('[data-audio]');if(b){e.stopPropagation();playVoice(b)}},true);

/* ---------- liga semanal ---------- */
async function weekly(body){
  const me=C().user();body.innerHTML=`<p class="p2empty">${t('loading')}</p>`;
  try{
    const all=await cloud().weekly({limit:200});
    const lg=U().league((me&&me.xp)||0).name;
    const list=all.filter(m=>m.id===(me&&me.id)||U().league(m.xp||0).name===lg).filter(m=>(m.week||0)>0||m.id===(me&&me.id));
    if(!document.getElementById('r-body'))return;
    if(!list.length){body.innerHTML=`<p class="p2empty">${t('weekNo')}</p>`;return}
    body.innerHTML=`<div class="pg-wk-h"><b>🏆 ${t('weekT')} · ${esc(lg)}</b><small>${t('weekSub')}</small></div><div class="p2rows">${list.slice(0,50).map((m,i)=>`<div class="p2row ${me&&m.id===me.id?'me':''}" data-prof="${esc(m.id)}"><span class="pos">${i+1}</span><span class="av">${esc(m.avatar||'🙂')}</span><div class="nm"><b>${esc(m.name)}${me&&m.id===me.id?' ('+t('you')+')':''}</b></div><span class="sc">${m.week||0} ${t('pts')}</span></div>`).join('')}</div>`;
  }catch(e){body.innerHTML=`<p class="p2empty">${esc(e.message||t('err'))}</p>`}
}

/* ---------- parceiro do dia ---------- */
async function partner(me){
  try{
    const l=(me.learning||[])[0];if(!l||!me.native)return '';
    let list=await cloud().members({native:l,learning:me.native,limit:60});
    if(!list.length)list=await cloud().members({native:l,limit:60});
    if(!list.length)return '';
    const day=Math.floor(Date.now()/864e5);let h=0;for(const ch of me.id+day)h=(h*31+ch.charCodeAt(0))>>>0;
    const m=list[h%list.length];
    return `<div class="pg-card pg-pod"><span class="av">${esc(m.avatar||'🙂')}</span><div class="tx"><small>🤝 ${t('partner')}</small><b>${esc(m.name)}</b><small>${t('partnerSub')}</small></div>
      <div class="bt"><button class="pg-btn sm" data-dm="${esc(m.id)}">💬 ${t('talk')}</button><button class="pg-btn ghost sm" data-prof="${esc(m.id)}">${t('profile')}</button></div></div>`;
  }catch(e){return ''}
}

/* ---------- perfil público ---------- */
async function profile(id){
  const me=C().user();id=id||(me&&me.id);
  C().shell(`${C().subtabs('')}<div id="pf-b"><p class="pg-empty">${t('loading')}</p></div>`);C().wireTabs();
  const box=$('#pf-b');
  try{
    const [p,st]=await Promise.all([cloud().getProfile(id),cloud().profileStats(id).catch(()=>({}))]);
    if(!$('#pf-b'))return;
    const lg=U().league(p.xp||0),eps=p.eps||{},self=me&&me.id===p.id,achN=Object.keys(p.ach||{}).length;
    const epsTot=Object.values(eps).reduce((a,b)=>a+(+b||0),0);
    const link=self&&cloud().inviteLink?cloud().inviteLink():'';
    const sup=(window.POGGLOT_CONFIG||{}).supportUrl;
    box.innerHTML=`<button class="pg-btn ghost sm" id="pf-back" style="margin-bottom:12px">← ${t('back')}</button>
     <section class="pg-card pg-prof"><div class="hd"><span class="av">${esc(p.avatar||'🙂')}</span><div><h2>${esc(p.name)}</h2><span class="lg" style="--c:${lg.color}">🏅 ${esc(lg.name)}</span></div></div>
      ${p.bio?`<p class="bio">${esc(p.bio)}</p>`:''}
      <div class="pg-exch"><span class="sp">${t('speaks')}: ${esc(C().lname(p.native))}</span>${(p.learning||[]).map(i=>`<span class="le">${t('learns')}: ${esc(C().lname(i))}</span>`).join('')}</div>
      <div class="pg-pstats"><div><b>${p.xp||0}</b><small>${t('pts')}</small></div><div><b>🔥 ${p.streak||0}</b><small>${t('streak')}</small></div><div><b>${epsTot}</b><small>${t('eps')}</small></div><div><b>${achN}</b><small>${t('ach')}</small></div></div>
      <div class="pg-pstats"><div><b>${st.questions||0}</b><small>${t('asked')}</small></div><div><b>${st.answers||0}</b><small>${t('answered')}</small></div><div><b>${st.likes||0}</b><small>${t('useful')}</small></div><div><b>${st.best||0}</b><small>${t('bestA')}</small></div></div>
      ${self?'':`<div style="display:flex;gap:8px;flex-wrap:wrap"><button class="pg-btn" id="pf-dm">💬 ${t('talk')}</button><button class="pg-btn ghost" id="pf-bl">${t('block')}</button></div>`}
     </section>
     ${self&&link?`<section class="pg-card pg-inv"><h3>🎁 ${t('invite')}</h3><p>${t('inviteSub')} <b>${st.invited||0}</b> ${t('invited').toLowerCase()}.</p><input class="pg-in" readonly value="${esc(link)}" id="pf-link"><div style="display:flex;gap:8px;margin-top:8px"><button class="pg-btn" id="pf-copy">${t('copy')}</button>${navigator.share?`<button class="pg-btn ghost" id="pf-share">${t('share')}</button>`:''}</div></section>`:''}
     ${self&&window.PogBilling?PogBilling.badge():''}
     ${self&&sup?`<a class="pg-btn ghost pg-sup" href="${esc(sup)}" target="_blank" rel="noopener">${t('support')}</a>`:''}`;
    $('#pf-back').onclick=()=>history.length>1&&false?history.back():C().open('rank');
    const dm=$('#pf-dm');if(dm)dm.onclick=()=>C().open('chat',cloud().dmRoom(p.id));
    const bl=$('#pf-bl');if(bl)bl.onclick=async()=>{if(!confirm(t('block')+'?'))return;try{await cloud().block(p.id);alert(t('blocked'));C().open('chat','geral')}catch(e){alert(e.message)}};
    const cp=$('#pf-copy');if(cp)cp.onclick=async()=>{try{await navigator.clipboard.writeText(link)}catch(e){$('#pf-link').select();document.execCommand('copy')}cp.textContent=t('copied')};
    const sh=$('#pf-share');if(sh)sh.onclick=()=>navigator.share({title:'Pogglot',text:t('inviteText'),url:link}).catch(()=>{});
  }catch(e){box.innerHTML=`<p class="pg-empty">${esc(e.message||t('err'))}</p>`}
}
/* abre o perfil ao tocar em qualquer [data-prof] */
document.addEventListener('click',e=>{const b=e.target.closest&&e.target.closest('[data-prof]');if(!b||!C()||!C().user())return;e.stopPropagation();C().open('profile',b.dataset.prof)},true);

/* ---------- painel de moderação ---------- */
let adminFlag=null;
async function isAdmin(){
  if(adminFlag!==null&&adminFlag.uid===(C().user()||{}).id)return adminFlag.v;
  let v=false;try{if(cloud().mode==='supabase'&&C().user())v=(await cloud().rest('POST','/rest/v1/rpc/is_admin',{body:{}}))===true}catch(e){}
  adminFlag={uid:(C().user()||{}).id,v};return v;
}
const adm={tab:'reports'};
async function admin(){
  if(!await isAdmin()){C().shell(`${C().subtabs('')}<p class="pg-empty">${t('forbidden')}</p><p class="pg-empty" style="font-size:12px">${esc(t('adminHow'))}</p>`);C().wireTabs();return}
  C().shell(`${C().subtabs('admin')}<div class="pg-subtabs" id="ad-t"><button data-t="reports" aria-pressed="${adm.tab==='reports'}">🚩 ${t('reports')}</button><button data-t="stats" aria-pressed="${adm.tab==='stats'}">📊 ${t('stats')}</button><button data-t="plan" aria-pressed="${adm.tab==='plan'}">⭐ Planos</button></div><div id="ad-b"><p class="pg-empty">${t('loading')}</p></div>`);
  C().wireTabs();
  $('#ad-t').onclick=e=>{const b=e.target.closest('[data-t]');if(b){adm.tab=b.dataset.t;admin()}};
  adm.tab==='stats'?adminStats():adm.tab==='plan'&&window.PogBilling?PogBilling.adminPanel($('#ad-b')):adminReports();
}
const KN={m:'msg',q:'q',a:'a'};
async function adminReports(){
  const box=$('#ad-b');
  try{
    const rows=await cloud().rest('POST','/rest/v1/rpc/admin_reports',{body:{}});
    if(!rows.length){box.innerHTML=`<p class="pg-empty">${t('noRep')}</p>`;return}
    box.innerHTML=rows.map(r=>`<article class="pg-card pg-rep ${r.hidden?'is-hidden':''}"><div class="h"><span class="fq-k">${t(KN[r.kind])}</span><b>${r.n} ${t('nRep')}</b>${r.hidden?`<span class="fq-ok" style="background:#FFE9E9;color:#9B1C1C">${t('hidden')}</span>`:''}<small>${t('by')} ${esc(r.author_name)}</small></div>
      <p class="fq-text">${esc(r.txt)}</p>
      <div class="fq-acts"><button data-h="${r.kind}:${r.ref}:${r.hidden?0:1}">${r.hidden?'👁 '+t('unhide'):'🙈 '+t('hide')}</button><button data-d="${r.kind}:${r.ref}">🗑 ${t('del')}</button><button data-m="${esc(r.author)}:24">🔇 ${t('mute')}</button><button data-m="${esc(r.author)}:0">🔊 ${t('unmute')}</button></div></article>`).join('');
    box.onclick=async e=>{const h=e.target.closest('[data-h]'),d=e.target.closest('[data-d]'),m=e.target.closest('[data-m]');
      try{
        if(h){const [k,id,hide]=h.dataset.h.split(':');await cloud().rest('POST','/rest/v1/rpc/admin_set_hidden',{body:{p_kind:k,p_ref:+id,p_hide:hide==='1'}})}
        else if(d){if(!confirm(t('confirm')))return;const [k,id]=d.dataset.d.split(':');await cloud().rest('POST','/rest/v1/rpc/admin_delete',{body:{p_kind:k,p_ref:+id}})}
        else if(m){const [u,hrs]=m.dataset.m.split(':');await cloud().rest('POST','/rest/v1/rpc/admin_mute',{body:{p_uid:u,p_hours:+hrs}})}
        else return;
        adminReports();
      }catch(x){alert(x.message||t('err'))}};
  }catch(e){box.innerHTML=`<p class="pg-empty">${esc(e.message||t('err'))}</p>`}
}
async function adminStats(){
  const box=$('#ad-b');
  try{
    const s=await cloud().rest('POST','/rest/v1/rpc/admin_stats',{body:{}});
    const card=(l,v)=>`<div class="pg-card pg-stat"><b>${v}</b><small>${l}</small></div>`;
    const obj=o=>{const k=Object.keys(o||{}).sort((a,b)=>o[b]-o[a]);return k.length?k.map(x=>`<li><span>${esc(C().lname(x))}</span><b>${o[x]}</b></li>`).join(''):`<li>${t('noData')}</li>`};
    const lst=(a,f)=>a&&a.length?a.map(f).join(''):`<li>${t('noData')}</li>`;
    box.innerHTML=`<div class="pg-stats">${card(t('users'),s.users)}${card(t('new7'),s.new7)}${card(t('act7'),s.active7)}${card(t('act1'),s.active1)}${card(t('qs'),s.questions)}${card(t('unans'),s.unanswered)}${card(t('ans'),s.answers)}${card(t('msgs'),s.messages)}${card(t('muted'),s.muted)}</div>
     <div class="pg-twocol"><section class="pg-card pg-lst"><h4>${t('langs')}</h4><ul>${obj(s.langs)}</ul></section><section class="pg-card pg-lst"><h4>${t('learning')}</h4><ul>${obj(s.learning)}</ul></section>
     <section class="pg-card pg-lst"><h4>${t('drop')}</h4><ul>${lst(s.drop,d=>`<li><span>${esc(d.cid)} · ${t('ep')} ${d.n}</span><b>${d.pct_drop}% (${d.starts})</b></li>`)}</ul></section>
     <section class="pg-card pg-lst"><h4>${t('hard')}</h4><ul>${lst(s.hard,d=>`<li><span>${esc(d.cid)} · ${t('ep')} ${d.n}</span><b>${d.avg_score}% (${d.dones})</b></li>`)}</ul></section></div>`;
  }catch(e){box.innerHTML=`<p class="pg-empty">${esc(e.message||t('err'))}</p>`}
}
window.PogExtras={micBtn,record,voiceHTML,weekly,partner,profile,admin,isAdmin};
})();
