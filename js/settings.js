/* Pogglot · Ajustes: voz e áudio, meta diária, lembretes, instalar no celular e uso offline */
(function(){
'use strict';
const store={get(k,d){try{const v=localStorage.getItem('pogglot:'+k);return v?JSON.parse(v):d}catch(e){return d}},set(k,v){try{localStorage.setItem('pogglot:'+k,JSON.stringify(v))}catch(e){}}};
const esc=s=>String(s==null?'':s).replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]));
const L0=()=>(window.ST&&ST.homeLang==='es')?'es':'pt';
const K={
 pt:{title:'Ajustes',close:'Fechar',voice:'Voz e áudio',lang:'Idioma da voz',accent:'Sotaque',vname:'Voz do aparelho',auto:'Automática (a melhor disponível)',speed:'Velocidade',preview:'Ouvir',
  vq:'Qualidade',noV:'Este aparelho não tem voz instalada para este idioma. No Android: Configurações › Texto para fala (instale o Google TTS e a voz do idioma). No iPhone: Ajustes › Acessibilidade › Conteúdo Falado › Vozes. No Windows, use o Edge: ele traz vozes “Natural” de alta qualidade.',
  tipV:'Dica: vozes marcadas como Alta (neurais, Premium, Enhanced, Natural) soam muito mais humanas.',
  cloudOn:'Voz neural em nuvem ligada. Os áudios ficam guardados no aparelho.',cloudOff:'Voz neural em nuvem não configurada. Quem hospeda o app liga isso em config.js (campo tts).',
  dl:'Baixar áudio do próximo episódio',dlOk:'Áudio guardado para uso offline',cached:'áudios guardados',clr:'Apagar áudios guardados',
  goal:'Meta diária',goalSub:'Quantos pontos de XP você quer fazer por dia?',gLight:'Leve',gNorm:'Normal',gSerious:'Sério',gIntense:'Intenso',today:'Hoje',gStreak:'dias seguidos batendo a meta',
  rem:'Lembrete diário',remSub:'Um aviso no horário que você escolher. Funciona com o app aberto ou instalado; para lembrar com o app fechado em qualquer aparelho, use o lembrete do calendário.',
  remOn:'Ativar lembrete',remAt:'Horário',remMsg:'Hora de praticar! Sua meta de hoje ainda está esperando.',remDenied:'As notificações estão bloqueadas neste navegador. Libere nas configurações do site.',
  ics:'Adicionar ao calendário (todo dia)',icsOk:'Arquivo de calendário criado.',
  install:'Instalar e usar offline',installSub:'Coloque o Pogglot na tela inicial e baixe cursos para estudar sem internet.',
  installBtn:'Instalar no celular',ios:'No iPhone/iPad: toque em Compartilhar e depois em “Adicionar à Tela de Início”.',installed:'App instalado',
  swOn:'Modo offline ativo',swOff:'O modo offline precisa que o app esteja hospedado em https (no seu site). Aqui na prévia ele fica desligado.',
  dlCourse:'Baixar este curso para offline',dlDone:'Curso pronto para usar offline',dlProg:'Baixando…',
  prac:'Pratique hoje!',goalDone:'Meta batida! 🎉',of:'de',
  acc:'Acessibilidade',accSub:'Ajuste o tamanho do texto, o contraste e os movimentos da tela.',accSize:'Tamanho do texto',accHC:'Alto contraste',accRM:'Reduzir movimento e animações',accReset:'Restaurar padrão'},
 es:{title:'Ajustes',close:'Cerrar',voice:'Voz y audio',lang:'Idioma de la voz',accent:'Acento',vname:'Voz del dispositivo',auto:'Automática (la mejor disponible)',speed:'Velocidad',preview:'Escuchar',
  vq:'Calidad',noV:'Este dispositivo no tiene voz instalada para este idioma. En Android: Ajustes › Texto a voz (instala Google TTS y la voz del idioma). En iPhone: Ajustes › Accesibilidad › Contenido hablado › Voces. En Windows usa Edge: trae voces “Natural” de alta calidad.',
  tipV:'Consejo: las voces marcadas como Alta (neuronales, Premium, Enhanced, Natural) suenan mucho más humanas.',
  cloudOn:'Voz neuronal en la nube activada. Los audios se guardan en el dispositivo.',cloudOff:'Voz neuronal en la nube no configurada. Quien aloja la app la activa en config.js (campo tts).',
  dl:'Descargar audio del próximo episodio',dlOk:'Audio guardado para uso sin conexión',cached:'audios guardados',clr:'Borrar audios guardados',
  goal:'Meta diaria',goalSub:'¿Cuántos puntos de XP quieres hacer por día?',gLight:'Ligera',gNorm:'Normal',gSerious:'En serio',gIntense:'Intensa',today:'Hoy',gStreak:'días seguidos cumpliendo la meta',
  rem:'Recordatorio diario',remSub:'Un aviso a la hora que elijas. Funciona con la app abierta o instalada; para recordar con la app cerrada en cualquier dispositivo, usa el recordatorio del calendario.',
  remOn:'Activar recordatorio',remAt:'Hora',remMsg:'¡Hora de practicar! Tu meta de hoy te está esperando.',remDenied:'Las notificaciones están bloqueadas en este navegador. Permítelas en la configuración del sitio.',
  ics:'Agregar al calendario (todos los días)',icsOk:'Archivo de calendario creado.',
  install:'Instalar y usar sin conexión',installSub:'Pon Pogglot en la pantalla de inicio y descarga cursos para estudiar sin internet.',
  installBtn:'Instalar en el móvil',ios:'En iPhone/iPad: toca Compartir y luego “Añadir a pantalla de inicio”.',installed:'App instalada',
  swOn:'Modo sin conexión activo',swOff:'El modo sin conexión necesita que la app esté alojada en https (en tu sitio). En esta vista previa queda desactivado.',
  dlCourse:'Descargar este curso para uso sin conexión',dlDone:'Curso listo para usar sin conexión',dlProg:'Descargando…',
  prac:'¡Practica hoy!',goalDone:'¡Meta cumplida! 🎉',of:'de',
  acc:'Accesibilidad',accSub:'Ajusta el tamaño del texto, el contraste y los movimientos de la pantalla.',accSize:'Tamaño del texto',accHC:'Alto contraste',accRM:'Reducir movimiento y animaciones',accReset:'Restablecer'}
};
const k=key=>(K[L0()][key]!=null?K[L0()][key]:K.pt[key]);
const LNAMES={en:'Inglês',es:'Espanhol',fr:'Francês',de:'Alemão',it:'Italiano',pt:'Português'};
const LCODE={en:'en-US',es:'es-ES',fr:'fr-FR',de:'de-DE',it:'it-IT',ja:'ja-JP',pt:'pt-BR'};
const GOALS=[[10,'gLight'],[20,'gNorm'],[40,'gSerious'],[80,'gIntense']];

/* ---------- meta diária: XP de hoje a partir da diferença do XP total ---------- */
const dayKey=(d)=>{d=d||new Date();return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0')};
function daily(){
  let D=store.get('daily',null);const t=dayKey(),xp=(window.ST&&ST.xp)||0;
  if(!D||D.date!==t){
    if(D){const h=store.get('xphist',{});h[D.date]=Math.max(0,xp-D.base);const ks=Object.keys(h).sort();while(ks.length>60)delete h[ks.shift()];store.set('xphist',h)}
    D={date:t,base:xp,notified:false};store.set('daily',D);
  }
  return D;
}
const goalXp=()=>store.get('goal',{xp:20}).xp||20;
function todayXp(){const D=daily();return Math.max(0,((window.ST&&ST.xp)||0)-D.base)}
function goalStreak(){
  const h=store.get('xphist',{}),g=goalXp();let n=0;const d=new Date();
  if(todayXp()>=g)n++;
  for(let i=1;i<60;i++){const dd=new Date(d.getFullYear(),d.getMonth(),d.getDate()-i);const v=h[dayKey(dd)];if(v!=null&&v>=g)n++;else break}
  return n;
}
function goalState(){const g=goalXp(),x=todayXp();return{goal:g,xp:x,pct:Math.min(1,x/g),met:x>=g,streak:goalStreak()}}
function ringHTML(pct,size,sw,col){const R=(size-sw)/2,C=2*Math.PI*R;
  return `<svg width="${size}" height="${size}" viewBox="0 0 ${size} ${size}"><circle cx="${size/2}" cy="${size/2}" r="${R}" fill="none" stroke="rgba(124,77,255,.15)" stroke-width="${sw}"/><circle cx="${size/2}" cy="${size/2}" r="${R}" fill="none" stroke="${col||'#7C4DFF'}" stroke-width="${sw}" stroke-linecap="round" stroke-dasharray="${C}" stroke-dashoffset="${C*(1-pct)}" transform="rotate(-90 ${size/2} ${size/2})"/></svg>`}

/* ---------- lembretes ---------- */
const R0=()=>store.get('remind',{on:false,time:'19:00',last:''});
async function ensureNotif(){
  if(!('Notification' in window))return 'unsupported';
  if(Notification.permission==='granted')return 'granted';
  if(Notification.permission==='denied')return 'denied';
  try{return await Notification.requestPermission()}catch(e){return 'denied'}
}
async function notify(msg){
  const title='Pogglot';
  try{const reg=window.__pgsw;if(reg&&reg.showNotification){await reg.showNotification(title,{body:msg,icon:'icon-192.png',badge:'icon-192.png',tag:'pogglot-daily'});return true}}catch(e){}
  try{new Notification(title,{body:msg,icon:'icon-192.png'});return true}catch(e){}
  return false;
}
let remTimer=0;
function checkReminder(){
  const r=R0();if(!r.on)return;
  const now=new Date(),[h,m]=String(r.time||'19:00').split(':').map(Number);
  const at=new Date(now.getFullYear(),now.getMonth(),now.getDate(),h||0,m||0);
  if(now<at||r.last===dayKey())return;
  if(goalState().met){r.last=dayKey();store.set('remind',r);return}
  r.last=dayKey();store.set('remind',r);
  if(window.Notification&&Notification.permission==='granted')notify(k('remMsg'));
  banner(k('remMsg'));
}
function banner(msg){
  if(document.getElementById('pgs-banner')||document.getElementById('player'))return;
  const d=document.createElement('div');d.id='pgs-banner';d.className='pgs-banner';d.setAttribute('role','status');
  d.innerHTML=`<span>⏰</span><b>${esc(msg)}</b><button aria-label="${esc(k('close'))}">×</button>`;
  d.querySelector('button').onclick=()=>d.remove();
  document.body.appendChild(d);setTimeout(()=>d.remove(),12000);
}
function startRemTimer(){clearInterval(remTimer);remTimer=setInterval(()=>{try{checkReminder()}catch(e){}},30000);setTimeout(()=>{try{checkReminder()}catch(e){}},2500)}
function icsFile(time){
  const [h,m]=String(time||'19:00').split(':'),now=new Date(),d=dayKey(now).replace(/-/g,'');
  const stamp=new Date().toISOString().replace(/[-:]/g,'').replace(/\.\d+/,'');
  return ['BEGIN:VCALENDAR','VERSION:2.0','PRODID:-//Pogglot//Lembrete//PT','BEGIN:VEVENT','UID:pogglot-daily-'+Date.now()+'@pogglot','DTSTAMP:'+stamp,
    'DTSTART:'+d+'T'+String(h).padStart(2,'0')+String(m).padStart(2,'0')+'00','DURATION:PT15M','RRULE:FREQ=DAILY','SUMMARY:Pogglot: hora de praticar','DESCRIPTION:Sua meta diária está esperando. Abra o Pogglot e faça uma lição.',
    'BEGIN:VALARM','ACTION:DISPLAY','DESCRIPTION:Pogglot: hora de praticar','TRIGGER:PT0S','END:VALARM','END:VEVENT','END:VCALENDAR'].join('\r\n');
}

/* ---------- PWA ---------- */
let deferredInstall=null;
window.addEventListener('beforeinstallprompt',e=>{e.preventDefault();deferredInstall=e;const b=document.getElementById('pgs-inst');if(b)b.hidden=false});
window.addEventListener('appinstalled',()=>{deferredInstall=null;store.set('installed',true)});
const isStandalone=()=>(window.matchMedia&&matchMedia('(display-mode: standalone)').matches)||navigator.standalone===true;
async function registerSW(){
  try{
    if(!('serviceWorker' in navigator))return null;
    if(!(location.protocol==='https:'||location.hostname==='localhost'||location.hostname==='127.0.0.1'))return null;
    const reg=await navigator.serviceWorker.register('sw.js');window.__pgsw=reg;
    try{if(reg.periodicSync&&'permissions' in navigator){const st=await navigator.permissions.query({name:'periodic-background-sync'});if(st.state==='granted')await reg.periodicSync.register('pogglot-reminder',{minInterval:12*3600*1000})}}catch(e){}
    return reg;
  }catch(e){return null}
}
async function courseFiles(groupId){
  const m=window.MANIFEST||(await (await fetch('data/manifest.json')).json());
  const subs=(window.PogUI&&PogUI.LANG(groupId).sub)||[groupId];
  const out=[];subs.forEach(c=>(m[c]||[]).forEach(f=>out.push('data/'+f)));out.push('data/manifest.json','data/counts.json');return out;
}
async function downloadCourse(groupId,onProg){
  const files=await courseFiles(groupId),ca=await caches.open('pogglot-data-v1');let n=0;
  for(const f of files){try{const hit=await ca.match(f);if(!hit){const r=await fetch(f);if(r.ok)await ca.put(f,r)}}catch(e){}n++;onProg&&onProg(n,files.length)}
  store.set('offline:'+groupId,Date.now());
}

/* ---------- modal ---------- */
function open(){
  close();
  const S=PogTTS.settings(),cur=(window.P&&P.c&&P.c.id&&(P.c.group||P.c.id))||(window.ST&&ST.lastCourse&&(String(ST.lastCourse).split('-')[0]))||'en';
  let lang=store.get('setlang',cur)||'en';if(!LNAMES[lang])lang='en';
  const el=document.createElement('div');el.className='pgs-modal';el.id='pgs';el.setAttribute('role','dialog');el.setAttribute('aria-modal','true');el.setAttribute('aria-label',k('title'));
  document.body.appendChild(el);document.body.classList.add('pgs-open');
  const end=()=>close();
  const draw=async()=>{
    const code=LCODE[lang],vs=PogTTS.voicesFor(code).slice().sort((a,b)=>PogTTS.quality(b)-PogTTS.quality(a));
    const acc=PogTTS.ACCENTS[lang]||[],cs=PogTTS.settings();
    const g=goalState(),rem=R0(),cnt=await PogTTS.cacheCount(),A=window.PogA11y?PogA11y.get():{zoom:100,contrast:false,motion:false};
    const swOn=!!(navigator.serviceWorker&&navigator.serviceWorker.controller);
    const best=vs[0],ql=best?PogTTS.qualityLabel(best):'';
    el.innerHTML=`<div class="pgs-card"><div class="pgs-head"><h2>⚙️ ${esc(k('title'))}</h2><button class="pgs-x" aria-label="${esc(k('close'))}">×</button></div>
     <section><h3>🔊 ${esc(k('voice'))}</h3>
      <label>${esc(k('lang'))}<select id="s-lang">${Object.keys(LNAMES).map(l=>`<option value="${l}" ${l===lang?'selected':''}>${LNAMES[l]}</option>`).join('')}</select></label>
      ${acc.length>1?`<label>${esc(k('accent'))}<select id="s-acc">${acc.map(a=>`<option value="${a[0]}" ${cs.accent[lang]===a[0]?'selected':''}>${esc(a[2])}</option>`).join('')}</select></label>`:''}
      ${vs.length?`<label>${esc(k('vname'))}<select id="s-voice"><option value="">${esc(k('auto'))}</option>${vs.map(v=>`<option value="${esc(v.voiceURI||v.name)}" ${cs.voice[lang]===(v.voiceURI||v.name)?'selected':''}>${esc(v.name)} · ${esc(v.lang)} · ${esc(PogTTS.qualityLabel(v))}</option>`).join('')}</select></label>
        <p class="pgs-note">${esc(k('vq'))}: <b class="q-${ql}">${esc(ql)}</b> · ${esc(k('tipV'))}</p>`
        :`<p class="pgs-note warn">${esc(k('noV'))}</p>`}
      <label>${esc(k('speed'))}: <b id="s-rv">${(cs.rate||1).toFixed(2)}×</b><input type="range" id="s-rate" min="0.6" max="1.25" step="0.05" value="${cs.rate||1}"></label>
      <button class="pgs-btn" id="s-prev">🔊 ${esc(k('preview'))}</button>
      <p class="pgs-note ${PogTTS.cloud()?'ok':''}">${esc(PogTTS.cloud()?k('cloudOn'):k('cloudOff'))}${PogTTS.cloud()?` (${cnt} ${esc(k('cached'))})`:''}</p>
      ${PogTTS.cloud()?`<div class="pgs-row"><button class="pgs-btn ghost" id="s-dl">${esc(k('dl'))}</button><button class="pgs-btn ghost" id="s-clr">${esc(k('clr'))}</button></div><div class="pgs-prog" id="s-dlp" hidden><i></i></div>`:''}
     </section>
     <section><h3>🎯 ${esc(k('goal'))}</h3><p class="pgs-note">${esc(k('goalSub'))}</p>
      <div class="pgs-goals">${GOALS.map(([x,key])=>`<button class="pgs-goal ${x===g.goal?'on':''}" data-g="${x}"><b>${x} XP</b><small>${esc(k(key))}</small></button>`).join('')}</div>
      <div class="pgs-today"><div class="ring">${ringHTML(g.pct,64,8)}<span>${Math.round(g.pct*100)}%</span></div><div><b>${esc(k('today'))}: ${g.xp} ${esc(k('of'))} ${g.goal} XP</b><small>${g.met?esc(k('goalDone')):''} ${g.streak?`🔥 ${g.streak} ${esc(k('gStreak'))}`:''}</small></div></div>
     </section>
     <section><h3>🔔 ${esc(k('rem'))}</h3><p class="pgs-note">${esc(k('remSub'))}</p>
      <label class="pgs-chk"><input type="checkbox" id="s-ron" ${rem.on?'checked':''}> ${esc(k('remOn'))}</label>
      <label>${esc(k('remAt'))}<input type="time" id="s-rt" value="${esc(rem.time||'19:00')}"></label>
      <p class="pgs-note warn" id="s-rmsg" hidden></p>
      <button class="pgs-btn ghost" id="s-ics">📅 ${esc(k('ics'))}</button>
     </section>
     <section><h3>♿ ${esc(k('acc'))}</h3><p class="pgs-note">${esc(k('accSub'))}</p>
      <label>${esc(k('accSize'))}: <b id="a-zv">${A.zoom}%</b></label>
      <div class="pgs-a11y"><button class="pgs-btn ghost" id="a-dn" aria-label="A−">A−</button><input type="range" id="a-z" min="90" max="150" step="10" value="${A.zoom}" aria-label="${esc(k('accSize'))}" style="flex:1"><button class="pgs-btn ghost" id="a-up" aria-label="A+">A+</button></div>
      <label class="pgs-chk"><input type="checkbox" id="a-hc" ${A.contrast?'checked':''}> ${esc(k('accHC'))}</label>
      <label class="pgs-chk"><input type="checkbox" id="a-rm" ${A.motion?'checked':''}> ${esc(k('accRM'))}</label>
      <button class="pgs-btn ghost" id="a-rs">${esc(k('accReset'))}</button>
     </section>
     <section><h3>📲 ${esc(k('install'))}</h3><p class="pgs-note">${esc(k('installSub'))}</p>
      ${isStandalone()?`<p class="pgs-note ok">✓ ${esc(k('installed'))}</p>`:`<button class="pgs-btn" id="pgs-inst" ${deferredInstall?'':'hidden'}>${esc(k('installBtn'))}</button><p class="pgs-note" ${deferredInstall?'hidden':''}>${esc(k('ios'))}</p>`}
      <p class="pgs-note ${swOn?'ok':''}">${esc(swOn?k('swOn'):k('swOff'))}</p>
      ${swOn?`<button class="pgs-btn ghost" id="s-offl">${esc(k('dlCourse'))}</button><div class="pgs-prog" id="s-op" hidden><i></i></div>`:''}
     <p class="pgs-note" style="opacity:.6;margin-top:10px">Versão do app: 20/10/2026 · v105</p>
     </section></div>`;
    const q=s=>el.querySelector(s);
    if(window.PogA11y){const az=q('#a-z');
      const setZ=v=>{v=Math.max(90,Math.min(150,v));PogA11y.set({zoom:v});az.value=v;q('#a-zv').textContent=v+'%'};
      az.oninput=e=>setZ(+e.target.value);q('#a-dn').onclick=()=>setZ(+az.value-10);q('#a-up').onclick=()=>setZ(+az.value+10);
      q('#a-hc').onchange=e=>PogA11y.set({contrast:e.target.checked});q('#a-rm').onchange=e=>PogA11y.set({motion:e.target.checked});
      q('#a-rs').onclick=()=>{PogA11y.reset();draw()}}
    q('.pgs-x').onclick=end;
    q('#s-lang').onchange=e=>{lang=e.target.value;store.set('setlang',lang);draw()};
    const sa=q('#s-acc');if(sa)sa.onchange=e=>{PogTTS.setAccent(lang,e.target.value);draw()};
    const sv=q('#s-voice');if(sv)sv.onchange=e=>{PogTTS.setVoice(lang,e.target.value);draw()};
    q('#s-rate').oninput=e=>{PogTTS.setRate(e.target.value);q('#s-rv').textContent=(+e.target.value).toFixed(2)+'×'};
    const SAMPLE={en:'Hello! Nice to meet you. How are you today?',es:'¡Hola! Mucho gusto. ¿Cómo estás hoy?',pt:'Olá! Tudo bem? Prazer em conhecer você.',fr:'Bonjour ! Enchanté. Comment allez-vous ?',de:'Hallo! Freut mich. Wie geht es Ihnen?',it:'Ciao! Piacere di conoscerti. Come stai?'};
    q('#s-prev').onclick=()=>{try{speechSynthesis.cancel()}catch(e){}speak(SAMPLE[lang],LCODE[lang],null,null,false)};
    el.querySelectorAll('.pgs-goal').forEach(b=>b.onclick=()=>{store.set('goal',{xp:+b.dataset.g});draw();refreshHome()});
    const ron=q('#s-ron'),rt=q('#s-rt'),rm=q('#s-rmsg');
    const saveRem=async()=>{const r=R0();r.on=ron.checked;r.time=rt.value||'19:00';
      if(r.on){const p=await ensureNotif();if(p==='denied'){rm.hidden=false;rm.textContent=k('remDenied')}else rm.hidden=true;if(p==='granted')registerSW()}
      store.set('remind',r);startRemTimer()};
    ron.onchange=saveRem;rt.onchange=saveRem;
    q('#s-ics').onclick=()=>{try{const blob=new Blob([icsFile(rt.value)],{type:'text/calendar'}),a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='pogglot-lembrete.ics';document.body.appendChild(a);a.click();a.remove();rm.hidden=false;rm.className='pgs-note ok';rm.textContent=k('icsOk')}catch(e){}};
    const inst=q('#pgs-inst');if(inst)inst.onclick=async()=>{if(deferredInstall){deferredInstall.prompt();try{await deferredInstall.userChoice}catch(e){}deferredInstall=null;draw()}};
    const dl=q('#s-dl');if(dl)dl.onclick=async()=>{
      const t=window.PogPath&&PogPath.nextEp?PogPath.nextEp():null;if(!t)return;
      const p=q('#s-dlp');p.hidden=false;const items=PogTTS.episodeTexts(t.e);
      try{await PogTTS.prefetch(items,LCODE[(t.cid||'en').split('-')[0]]||'en-US',(d,n)=>{p.firstElementChild.style.width=(d/n*100)+'%'});dl.textContent='✓ '+k('dlOk')}catch(e){dl.textContent='⚠️ '+e.message}
      draw()};
    const clr=q('#s-clr');if(clr)clr.onclick=async()=>{await PogTTS.clearCache();draw()};
    const od=q('#s-offl');if(od)od.onclick=async()=>{const p=q('#s-op');p.hidden=false;await downloadCourse(lang,(n,t)=>{p.firstElementChild.style.width=(n/t*100)+'%'});od.textContent='✓ '+k('dlDone')};
  };
  el.addEventListener('click',e=>{if(e.target===el)end()});
  document.addEventListener('keydown',function esc1(e){if(e.key==='Escape'){end();document.removeEventListener('keydown',esc1)}});
  draw();
}
function close(){const e=document.getElementById('pgs');if(e)e.remove();document.body.classList.remove('pgs-open')}
function refreshHome(){try{if(window.PogUI&&PogUI.cur==='home'&&!document.getElementById('player')&&!location.hash.includes('lang')&&!location.hash.includes('course'))home()}catch(e){}}

/* ---------- engrenagem na barra e atalhos ---------- */
{const _top=window.topbar;if(_top)window.topbar=function(L){const h=_top.apply(this,arguments);return h.replace('<div class="pglang"','<button class="pgstat gear" data-act="settings" aria-label="'+esc(k('title'))+'" title="'+esc(k('title'))+'">⚙️</button><div class="pglang"')}}
document.addEventListener('click',e=>{const b=e.target.closest('[data-act="settings"]');if(b){e.preventDefault();open()}});

/* garante o contador do dia e liga os avisos */
const _save=window.save;if(_save)window.save=function(){const r=_save.apply(this,arguments);try{daily();if(R0().on)setTimeout(checkReminder,800)}catch(e){}return r};
daily();startRemTimer();
if(R0().on)ensureNotif().then(p=>{if(p==='granted')registerSW()});
registerSW();
window.PogSettings={open,close,goalState,ringHTML,k,todayXp,goalXp,banner,notify,registerSW,downloadCourse,isStandalone};
})();
