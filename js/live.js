/* Aula ao vivo: agenda em horário de Brasília, reserva e link único do Google Meet por horário. */
(function(){'use strict';
var $=function(s,r){return(r||document).querySelector(s)},$$=function(s,r){return[].slice.call((r||document).querySelectorAll(s))};
var CFG=window.POGGLOT_CONFIG||{},SB=(CFG.supabaseUrl||'').replace(/\/+$/,''),KEY=CFG.supabaseAnonKey||'';
var BRT='America/Sao_Paulo',MY=Intl.DateTimeFormat().resolvedOptions().timeZone||BRT;
var S=null,G=null,live=!!(SB&&KEY),demoWhy='',avail={},sel=null,cur=null;
var LS='pg_live_bookings';
function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function pad(n){return(n<10?'0':'')+n}
function chime(){try{var c=new(window.AudioContext||window.webkitAudioContext)(),t=c.currentTime;[659,784,988].forEach(function(f,i){var o=c.createOscillator(),g=c.createGain();o.type='sine';o.frequency.value=f;g.gain.setValueAtTime(0,t+i*.11);g.gain.linearRampToValueAtTime(.14,t+i*.11+.02);g.gain.exponentialRampToValueAtTime(.0001,t+i*.11+.5);o.connect(g).connect(c.destination);o.start(t+i*.11);o.stop(t+i*.11+.55)})}catch(e){}}
/* ---------- datas ---------- */
function fmt(ts,tz,o){return new Intl.DateTimeFormat('pt-BR',Object.assign({timeZone:tz},o)).format(new Date(ts))}
function dayLabel(ts,tz){return fmt(ts,tz,{weekday:'long',day:'2-digit',month:'long'})}
function hm(ts,tz){return fmt(ts,tz,{hour:'2-digit',minute:'2-digit'})}
function sameZone(){return fmt(Date.now(),MY,{timeZoneName:'longOffset'})===fmt(Date.now(),BRT,{timeZoneName:'longOffset'})}
function slotsOf(g){var out=[],now=Date.now(),b=new Date(now-3*3600e3),y=b.getUTCFullYear(),m=b.getUTCMonth(),d=b.getUTCDate();
  for(var i=0;i<S.weeks*7;i++){var day=new Date(Date.UTC(y,m,d+i)),dow=day.getUTCDay();
    g.slots.forEach(function(s){if(s.dow!==dow)return;var p=s.time.split(':'),st=Date.UTC(day.getUTCFullYear(),day.getUTCMonth(),day.getUTCDate(),+p[0]+3,+p[1]);
      if(st<now+30*60e3)return;out.push({id:g.id+'_'+day.getUTCFullYear()+pad(day.getUTCMonth()+1)+pad(day.getUTCDate()),group:g.id,start:st})})}
  return out.sort(function(a,b){return a.start-b.start})}
/* ---------- servidor ---------- */
function hdr(){var h={apikey:KEY,'Content-Type':'application/json'};if(/^eyJ/.test(KEY))h.Authorization='Bearer '+KEY;return h}
function rest(path,body){return fetch(SB+'/rest/v1/'+path,{method:body?'POST':'GET',headers:hdr(),body:body?JSON.stringify(body):undefined}).then(function(r){return r.text().then(function(t){var j=null;try{j=JSON.parse(t)}catch(e){}if(!r.ok){var e=new Error((j&&(j.message||j.hint))||('http_'+r.status));e.status=r.status;throw e}return j})})}
function loadAvail(ids){if(!live||!ids.length)return Promise.resolve();
  return rest('live_slot_public?select=id,booked,capacity,link_ready&id=in.('+ids.join(',')+')').then(function(rows){(rows||[]).forEach(function(r){avail[r.id]=r})}).catch(function(e){live=false;demoWhy=(e.status===404||/relation|schema|PGRST/i.test(e.message))?'A agenda ainda não foi ativada no servidor.':'Não foi possível falar com o servidor agora.'})}
function ensureLink(b){return fetch(SB+'/functions/v1/live-meet',{method:'POST',headers:hdr(),body:JSON.stringify({booking_id:b.booking_id,token:b.token})}).then(function(r){return r.json().then(function(j){return{status:r.status,j:j}})})}
function pollLink(b,tries){return rest('rpc/live_link',{p_booking:b.booking_id,p_token:b.token}).then(function(j){if(j&&j.meet_url)return j.meet_url;if(tries<=0)return null;return new Promise(function(r){setTimeout(r,3500)}).then(function(){return pollLink(b,tries-1)})}).catch(function(){return null})}
/* ---------- reservas locais ---------- */
function mine(){try{return JSON.parse(localStorage.getItem(LS)||'[]')}catch(e){return[]}}
function saveMine(a){try{localStorage.setItem(LS,JSON.stringify(a))}catch(e){}}
function putMine(b){var a=mine().filter(function(x){return x.slot_id!==b.slot_id});a.push(b);saveMine(a);renderBadge()}
function renderBadge(){var n=mine().filter(function(b){return b.start+b.duration*60000>Date.now()}).length,el=$('#mineN');el.textContent=n;el.hidden=!n}
/* ---------- tela ---------- */
function groupOf(id){return G.filter(function(g){return g.id===id})[0]}
function renderGroups(){
  $('#groups').innerHTML=G.map(function(g){var next=slotsOf(g)[0];return '<button type="button" class="lv-g'+(sel===g.id?' on':'')+'" role="radio" aria-checked="'+(sel===g.id)+'" data-g="'+g.id+'" style="--c:'+g.accent+'"><span class="lv-gi">'+g.icon+'</span><span class="lv-gt"><small>'+esc(g.teaches)+' · '+esc(g.audience)+'</small><b>'+esc(g.title)+'</b></span><p>'+esc(g.blurb)+'</p><span class="lv-gn">'+(next?'Próxima: <b>'+fmt(next.start,BRT,{weekday:'short',day:'2-digit',month:'short'})+' · '+hm(next.start,BRT)+'</b>':'')+'</span></button>'}).join('');
  $$('#groups .lv-g').forEach(function(b){b.onclick=function(){pick(b.dataset.g)}})}
function pick(id){sel=id;renderGroups();var g=groupOf(id),list=slotsOf(g);
  $('#tzInfo').innerHTML=sameZone()?'Horários em <b>horário de Brasília</b>':'Horário de Brasília e <b>no seu fuso</b> ('+esc(MY.replace('_',' '))+')';
  $('#slots').innerHTML='<p class="lv-load">Carregando vagas…</p>';
  loadAvail(list.map(function(s){return s.id})).then(function(){renderSlots(g,list);note();$('#agenda').scrollIntoView({behavior:'smooth',block:'start'})})}
function note(){var n=$('#demoNote');if(live){n.hidden=true;return}n.hidden=false;n.innerHTML='<b>Modo de demonstração.</b> '+esc(demoWhy||'A agenda online ainda não está conectada.')+' Reservas feitas aqui ficam só neste aparelho e não geram link do Google Meet.'}
function renderSlots(g,list){
  $('#slots').innerHTML=list.map(function(s){var a=avail[s.id]||{booked:0,capacity:S.capacity},left=Math.max(0,(a.capacity||S.capacity)-(a.booked||0)),full=left<=0,have=mine().some(function(b){return b.slot_id===s.id});
    var local=sameZone()?'':'<span class="lv-lz">No seu horário: <b>'+hm(s.start,MY)+'</b> · '+fmt(s.start,MY,{weekday:'short',day:'2-digit',month:'short'})+'</span>';
    return '<article class="lv-s'+(full?' full':'')+'" style="--c:'+g.accent+'"><div class="lv-d"><b>'+fmt(s.start,BRT,{day:'2-digit'})+'</b><span>'+fmt(s.start,BRT,{month:'short'}).replace('.','')+'</span></div><div class="lv-i"><b>'+esc(dayLabel(s.start,BRT))+'</b><span class="lv-t">'+hm(s.start,BRT)+' – '+hm(s.start+S.durationMin*60000,BRT)+' <em>Brasília</em></span>'+local+'<span class="lv-v">'+(full?'Lotado':(left<=3?'Últimas '+left+' vagas':left+' vagas'))+'</span></div><button type="button" class="lv-btn sm" data-s="'+s.id+'" '+(full&&!have?'disabled':'')+'>'+(have?'Ver minha reserva':full?'Lotado':'Reservar')+'</button></article>'}).join('')||'<p class="lv-load">Sem horários nas próximas semanas.</p>';
  $$('#slots [data-s]').forEach(function(b){b.onclick=function(){var s=list.filter(function(x){return x.id===b.dataset.s})[0],ex=mine().filter(function(x){return x.slot_id===s.id})[0];if(ex)showDone(ex);else openForm(g,s)}})}
/* ---------- modal ---------- */
function open(id){var m=$(id);m.hidden=false;document.body.classList.add('lv-lock');setTimeout(function(){var f=$('input,button.lv-btn',m);if(f)f.focus()},60)}
function closeAll(){$$('.lv-modal').forEach(function(m){m.hidden=true});document.body.classList.remove('lv-lock')}
document.addEventListener('keydown',function(e){if(e.key==='Escape')closeAll()});
$$('.lv-modal').forEach(function(m){m.addEventListener('click',function(e){if(e.target===m||e.target.closest('[data-close]'))closeAll()})});
function openForm(g,s){cur={g:g,s:s};$('#bkForm').hidden=false;$('#bkDone').hidden=true;$('#bkK').textContent=g.teaches+' · '+g.audience;$('#bk-t').textContent=g.title;
  $('#bkWhen').innerHTML='<b>'+esc(dayLabel(s.start,BRT))+'</b> · '+hm(s.start,BRT)+' – '+hm(s.start+S.durationMin*60000,BRT)+' (Brasília)'+(sameZone()?'':'<br>No seu horário: <b>'+esc(dayLabel(s.start,MY))+' · '+hm(s.start,MY)+'</b>');
  $('#err').hidden=true;$('#go').disabled=false;$('#go').textContent='Reservar minha vaga';open('#bk')}
var ERR={slot_full:'Este horário acabou de lotar. Escolha outro.',slot_closed:'As reservas deste horário já fecharam.',invalid_input:'Confira o nome e o e-mail.',slot_not_found:'Horário não encontrado. Atualize a página.'};
$('#f').addEventListener('submit',function(e){e.preventDefault();var f=e.target,name=f.name.value.trim(),email=f.email.value.trim(),wa=f.wa.value.trim(),err=$('#err');
  if(!name||!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)){err.textContent=ERR.invalid_input;err.hidden=false;return}
  var go=$('#go');go.disabled=true;go.textContent='Reservando…';err.hidden=true;
  var base={slot_id:cur.s.id,group:cur.g.id,start:cur.s.start,duration:S.durationMin,name:name,email:email};
  if(!live){putMine(Object.assign(base,{booking_id:'local-'+Date.now(),token:'',meet_url:null,demo:true}));showDone(mine().filter(function(x){return x.slot_id===cur.s.id})[0]);return}
  rest('rpc/live_book',{p_slot:cur.s.id,p_name:name,p_email:email,p_whatsapp:wa||null}).then(function(r){
    var b=Object.assign(base,{booking_id:r.booking_id,token:r.token,meet_url:r.meet_url||null,already:!!r.already});putMine(b);showDone(b);chime();ensure(b)})
  .catch(function(e2){go.disabled=false;go.textContent='Reservar minha vaga';err.textContent=ERR[(e2.message||'').trim()]||'Não foi possível reservar agora. Tente de novo em instantes.';err.hidden=false})});
function ensure(b){if(b.meet_url||b.demo)return;
  ensureLink(b).then(function(r){if(r.j&&r.j.meet_url)return r.j.meet_url;return pollLink(b,10)}).catch(function(){return pollLink(b,10)}).then(function(url){
    var a=mine();a.forEach(function(x){if(x.slot_id===b.slot_id&&url){x.meet_url=url}});saveMine(a);var nb=mine().filter(function(x){return x.slot_id===b.slot_id})[0];if(nb&&!$('#bkDone').hidden&&$('#bkDone').dataset.slot===b.slot_id)showDone(nb,!url);renderMine()})}
function ics(b,g){var s=new Date(b.start),e=new Date(b.start+b.duration*60000),z=function(d){return d.getUTCFullYear()+pad(d.getUTCMonth()+1)+pad(d.getUTCDate())+'T'+pad(d.getUTCHours())+pad(d.getUTCMinutes())+'00Z'};
  var t=['BEGIN:VCALENDAR','VERSION:2.0','PRODID:-//Pogglot//Aula ao vivo//PT','BEGIN:VEVENT','UID:'+b.slot_id+'@pogglot','DTSTAMP:'+z(new Date()),'DTSTART:'+z(s),'DTEND:'+z(e),'SUMMARY:Pogglot · '+(g?g.title:'Aula ao vivo'),'DESCRIPTION:'+(b.meet_url?'Link do Google Meet: '+b.meet_url:'O link do Google Meet aparece na página de Minhas reservas.'),'URL:'+(b.meet_url||location.href),'END:VEVENT','END:VCALENDAR'].join('\r\n');
  return 'data:text/calendar;charset=utf-8,'+encodeURIComponent(t)}
function showDone(b,failed){var g=groupOf(b.group)||{title:'Aula ao vivo',teaches:''},el=$('#bkDone');el.dataset.slot=b.slot_id;$('#bkForm').hidden=true;el.hidden=false;
  var link=b.demo?'<div class="lv-link demo">Modo de demonstração: nenhum link foi gerado. A reserva não foi enviada ao servidor.</div>'
    :b.meet_url?'<div class="lv-link ok"><small>Seu link do Google Meet (o mesmo para todos deste horário)</small><input readonly value="'+esc(b.meet_url)+'" aria-label="Link do Google Meet"><div class="lv-row"><a class="lv-btn" href="'+esc(b.meet_url)+'" target="_blank" rel="noopener">Entrar na aula</a><button type="button" class="lv-btn ghost" id="cp">Copiar link</button></div></div>'
    :failed?'<div class="lv-link bad"><b>Ainda não conseguimos gerar o link.</b> Sua vaga está garantida. <button type="button" class="lv-btn ghost sm" id="retry">Tentar de novo</button></div>'
    :'<div class="lv-link wait"><span class="lv-spin"></span> Gerando o seu link do Google Meet…</div>';
  el.innerHTML='<div class="lv-ok">'+(b.demo?'Reserva de demonstração':b.already?'Você já tinha reservado este horário':'Vaga reservada! 🎉')+'</div><h3>'+esc(g.title)+'</h3><p class="lv-when"><b>'+esc(dayLabel(b.start,BRT))+'</b> · '+hm(b.start,BRT)+' – '+hm(b.start+b.duration*60000,BRT)+' (Brasília)'+(sameZone()?'':'<br>No seu horário: <b>'+esc(dayLabel(b.start,MY))+' · '+hm(b.start,MY)+'</b>')+'</p>'+link+'<div class="lv-row"><a class="lv-btn ghost" download="aula-pogglot.ics" href="'+ics(b,g)+'">Adicionar à agenda</a><button type="button" class="lv-btn ghost" data-close>Fechar</button></div>'+(b.demo?'':'<p class="lv-fine">Você também recebe o convite do Google Agenda no e-mail '+esc(b.email||'')+'.</p>');
  open('#bk');var cp=$('#cp',el);if(cp)cp.onclick=function(){try{navigator.clipboard.writeText(b.meet_url);cp.textContent='Copiado ✓'}catch(e){$('input',el).select()}};
  var rt=$('#retry',el);if(rt)rt.onclick=function(){showDone(b);ensure(b)}}
function renderMine(){var a=mine().filter(function(b){return b.start+b.duration*60000>Date.now()}).sort(function(x,y){return x.start-y.start});
  $('#mineList').innerHTML=a.length?a.map(function(b){var g=groupOf(b.group)||{title:'Aula ao vivo'};return '<article class="lv-m"><div><b>'+esc(g.title)+'</b><span>'+esc(dayLabel(b.start,BRT))+' · '+hm(b.start,BRT)+' (Brasília)</span></div>'+(b.meet_url?'<a class="lv-btn sm" href="'+esc(b.meet_url)+'" target="_blank" rel="noopener">Entrar</a>':b.demo?'<em>demonstração</em>':'<button type="button" class="lv-btn ghost sm" data-gen="'+b.slot_id+'">Gerar link</button>')+'</article>'}).join(''):'<p class="lv-load">Você ainda não tem reservas.</p>';
  $$('#mineList [data-gen]').forEach(function(x){x.onclick=function(){var b=mine().filter(function(y){return y.slot_id===x.dataset.gen})[0];x.textContent='Gerando…';ensure(b)}})}
$('#openMine').onclick=function(){renderMine();open('#mine')};
/* ---------- início ---------- */
$('#yr').textContent=new Date().getFullYear();
fetch('data/live-schedule.json').then(function(r){return r.json()}).then(function(j){S=j;G=j.groups;renderGroups();renderBadge();
  var first=location.hash.replace('#','');if(groupOf(first))pick(first);else{var m=mine().filter(function(b){return b.start>Date.now()})[0];$('#slots').innerHTML='<p class="lv-load">Escolha um grupo acima para ver os horários.</p>'}})
.catch(function(){$('#groups').innerHTML='<p class="lv-load">Não foi possível carregar a agenda. Atualize a página.</p>'});
})();
