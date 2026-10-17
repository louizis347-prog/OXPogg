/* Pogglot · Perguntas e respostas (estilo HiNative). Depende de PogCloud, PogUI e PogComm. */
(function(){
'use strict';
const S={
 pt:{tab:'Perguntas',ask:'Perguntar',askT:'Faça sua pergunta',all:'Todos os idiomas',allK:'Todas',unans:'Sem resposta',forMe:'Para eu responder',
  meaning:'O que significa?',say:'Como se diz?',natural:'Soa natural?',diff:'Qual a diferença?',other:'Outra dúvida',
  about:'Idioma da pergunta',type:'Tipo',text:'Sua pergunta',ctx:'Contexto (opcional)',textPh:'Ex.: “I am agree” soa natural?',ctxPh:'Onde você viu ou ouviu isso?',send:'Publicar',cancel:'Cancelar',
  answers:'respostas',answer:'resposta',noQ:'Nenhuma pergunta por aqui ainda. Seja o primeiro a perguntar!',more:'Ver mais',back:'Voltar',
  yourAns:'Sua resposta',ansPh:'Responda e, se puder, dê um exemplo.',reply:'Responder',noA:'Ainda sem respostas. Se você fala esse idioma, ajude!',
  best:'Melhor resposta',pick:'Escolher como melhor',unpick:'Tirar destaque',useful:'Útil',report:'Denunciar',reported:'Denúncia enviada. Obrigado!',del:'Apagar',delQ:'Apagar esta pergunta?',
  native:'Nativo',speaks:'fala',learns:'aprende',loading:'Carregando…',err:'Sem conexão. Tente de novo.',tooShort:'Escreva um pouco mais (mínimo 3 letras).',
  solved:'Respondida',needLogin:'Entre na sua conta para perguntar e responder.',yours:'Você',
  tip:'Dica: pergunte a quem fala o idioma como nativo. Quanto mais contexto, melhor a resposta.'},
 es:{tab:'Preguntas',ask:'Preguntar',askT:'Haz tu pregunta',all:'Todos los idiomas',allK:'Todas',unans:'Sin respuesta',forMe:'Para que yo responda',
  meaning:'¿Qué significa?',say:'¿Cómo se dice?',natural:'¿Suena natural?',diff:'¿Cuál es la diferencia?',other:'Otra duda',
  about:'Idioma de la pregunta',type:'Tipo',text:'Tu pregunta',ctx:'Contexto (opcional)',textPh:'Ej.: ¿“I am agree” suena natural?',ctxPh:'¿Dónde lo viste o lo oíste?',send:'Publicar',cancel:'Cancelar',
  answers:'respuestas',answer:'respuesta',noQ:'Aún no hay preguntas. ¡Sé el primero en preguntar!',more:'Ver más',back:'Volver',
  yourAns:'Tu respuesta',ansPh:'Responde y, si puedes, da un ejemplo.',reply:'Responder',noA:'Aún sin respuestas. Si hablas ese idioma, ¡ayuda!',
  best:'Mejor respuesta',pick:'Elegir como mejor',unpick:'Quitar destaque',useful:'Útil',report:'Denunciar',reported:'Denuncia enviada. ¡Gracias!',del:'Borrar',delQ:'¿Borrar esta pregunta?',
  native:'Nativo',speaks:'habla',learns:'aprende',loading:'Cargando…',err:'Sin conexión. Inténtalo de nuevo.',tooShort:'Escribe un poco más (mínimo 3 letras).',
  solved:'Respondida',needLogin:'Inicia sesión para preguntar y responder.',yours:'Tú',
  tip:'Consejo: pregunta a quien habla el idioma como nativo. Cuanto más contexto, mejor la respuesta.'}
};
const KINDS=['meaning','say','natural','diff','other'],KIC={meaning:'❓',say:'💬',natural:'👌',diff:'⚖️',other:'✍️'};
const C=()=>window.PogComm,U=()=>window.PogUI,cloud=()=>window.PogCloud;
const t=key=>{const L=U().L0();return (S[L]&&S[L][key]!=null)?S[L][key]:S.pt[key]};
const esc=s=>U().esc(s);
const st={lang:null,kind:null,unans:false,forMe:false,qs:[],more:false,cur:null};
const $=(s,r)=>(r||document).querySelector(s);

/* ---------- dados: Supabase (via PogCloud.rest) ou demo (localStorage) ---------- */
const enc=encodeURIComponent;
function pq(r){const p=r.profiles||{};return{id:r.id,uid:r.uid,name:p.name||'Aluno',avatar:p.avatar||'🙂',native:p.native||'',lang:r.lang,kind:r.kind,text:r.text,ctx:r.ctx||'',answers:r.answers||0,best:r.best||null,ts:Date.parse(r.created_at)}}
function pa(r){const p=r.profiles||{};return{audio:r.audio||null,id:r.id,qid:r.qid,uid:r.uid,name:p.name||'Aluno',avatar:p.avatar||'🙂',native:p.native||'',text:r.text,likes:r.likes||0,ts:Date.parse(r.created_at)}}
const sbk={
 async list(o){let q='/rest/v1/questions?select='+enc('*,profiles(name,avatar,native)')+'&order=id.desc&limit='+(o.limit+1);
  if(o.lang)q+='&lang=eq.'+enc(o.lang);if(o.kind)q+='&kind=eq.'+enc(o.kind);if(o.unans)q+='&answers=eq.0';if(o.before)q+='&id=lt.'+enc(o.before);
  const rows=await cloud().rest('GET',q);return{items:rows.slice(0,o.limit).map(pq),more:rows.length>o.limit}},
 async get(id){const me=cloud().user().id;
  const [qr,ar,lk]=await Promise.all([
   cloud().rest('GET','/rest/v1/questions?select='+enc('*,profiles(name,avatar,native)')+'&id=eq.'+enc(id)+'&limit=1'),
   cloud().rest('GET','/rest/v1/answers?select='+enc('*,profiles(name,avatar,native)')+'&qid=eq.'+enc(id)+'&order=id.asc&limit=200'),
   cloud().rest('GET','/rest/v1/answer_likes?select=aid')]);
  if(!qr.length)throw Object.assign(new Error('Pergunta não encontrada.'),{code:'not_found'});
  return{q:pq(qr[0]),answers:ar.map(pa),liked:new Set(lk.map(x=>x.aid))}},
 async ask(d){const me=cloud().user().id;await cloud().rest('POST','/rest/v1/questions',{headers:{Prefer:'return=minimal'},body:{uid:me,lang:d.lang,kind:d.kind,text:d.text,ctx:d.ctx}})},
 async answer(qid,text,audio){const body={qid:qid,uid:cloud().user().id,text:text};if(audio)body.audio=audio;await cloud().rest('POST','/rest/v1/answers',{headers:{Prefer:'return=minimal'},body})},
 async like(aid,on){const me=cloud().user().id;
  if(on)await cloud().rest('POST','/rest/v1/answer_likes',{headers:{Prefer:'return=minimal'},body:{aid:aid,uid:me}});
  else await cloud().rest('DELETE','/rest/v1/answer_likes?aid=eq.'+enc(aid)+'&uid=eq.'+enc(me),{headers:{Prefer:'return=minimal'}})},
 async best(qid,aid){await cloud().rest('POST','/rest/v1/rpc/pick_best',{body:{p_qid:qid,p_aid:aid||0}})},
 async report(kind,ref,reason){try{await cloud().rest('POST','/rest/v1/forum_reports',{headers:{Prefer:'return=minimal'},body:{kind:kind,ref:ref,reporter:cloud().user().id,reason:reason||''}})}catch(e){if(!/\(409\)/.test(e.message||''))throw e}},
 async del(kind,id){await cloud().rest('DELETE','/rest/v1/'+(kind==='q'?'questions':'answers')+'?id=eq.'+enc(id),{headers:{Prefer:'return=minimal'}})}
};
/* demo: tudo no navegador */
const DK='pogglot:forum';
function dload(){try{const v=JSON.parse(localStorage.getItem(DK)||'null');if(v)return v}catch(e){}
 const now=Date.now();return{seq:3,q:[
  {id:1,uid:'demo-james',name:'James Carter',avatar:'🏀',native:'en',lang:'pt',kind:'say',text:'Como se diz “I’m running late” em português?',ctx:'Quero avisar um amigo.',best:null,ts:now-36e5},
  {id:2,uid:'demo-lucia',name:'Lucía Fernández',avatar:'🌙',native:'es',lang:'en',kind:'natural',text:'Is “I am agree with you” natural?',ctx:'Escrevi isso numa prova.',best:null,ts:now-72e5}],
  a:[{id:1,qid:1,uid:'demo-mateus',name:'Mateus Oliveira',avatar:'🎸',native:'pt',text:'“Estou atrasado” ou, mais informal, “vou chegar atrasado”.',likes:2,ts:now-30e5}],likes:{}}}
function dsave(d){try{localStorage.setItem(DK,JSON.stringify(d))}catch(e){}}
const dem={
 async list(o){const d=dload();let l=d.q.slice().sort((a,b)=>b.id-a.id);
  if(o.lang)l=l.filter(x=>x.lang===o.lang);if(o.kind)l=l.filter(x=>x.kind===o.kind);
  const cnt=id=>d.a.filter(a=>a.qid===id).length;if(o.unans)l=l.filter(x=>!cnt(x.id));if(o.before)l=l.filter(x=>x.id<o.before);
  return{items:l.slice(0,o.limit).map(x=>Object.assign({},x,{ctx:x.ctx||'',answers:cnt(x.id)})),more:l.length>o.limit}},
 async get(id){const d=dload(),q=d.q.find(x=>x.id==id);if(!q)throw new Error('Pergunta não encontrada.');const as=d.a.filter(a=>a.qid==id);
  const me=cloud().user().id,lk=new Set(Object.keys(d.likes).filter(k=>k.split(':')[1]===me).map(k=>+k.split(':')[0]));
  return{q:Object.assign({},q,{ctx:q.ctx||'',answers:as.length}),answers:as,liked:lk}},
 async ask(x){const d=dload(),u=cloud().user();d.q.push({id:++d.seq,uid:u.id,name:u.name,avatar:u.avatar||'🙂',native:u.native||'',lang:x.lang,kind:x.kind,text:x.text,ctx:x.ctx,best:null,ts:Date.now()});dsave(d)},
 async answer(qid,text){const d=dload(),u=cloud().user();d.a.push({id:++d.seq,qid:qid,uid:u.id,name:u.name,avatar:u.avatar||'🙂',native:u.native||'',text:text,likes:0,ts:Date.now()});dsave(d)},
 async like(aid,on){const d=dload(),k=aid+':'+cloud().user().id,a=d.a.find(x=>x.id===aid);if(!a)return;if(on&&!d.likes[k]){d.likes[k]=1;a.likes++}else if(!on&&d.likes[k]){delete d.likes[k];a.likes=Math.max(0,a.likes-1)}dsave(d)},
 async best(qid,aid){const d=dload(),q=d.q.find(x=>x.id===qid);if(q){q.best=aid||null;dsave(d)}},
 async report(){},
 async del(kind,id){const d=dload();if(kind==='q'){d.q=d.q.filter(x=>x.id!==id);d.a=d.a.filter(x=>x.qid!==id)}else d.a=d.a.filter(x=>x.id!==id);dsave(d)}
};
const DB=()=>cloud().mode==='supabase'?sbk:dem;

/* ---------- interface ---------- */
const ago=ts=>C().timeFmt(ts);
const lbl=id=>C().lname(id);
function badge(m,lang){return m.native&&m.native===lang?`<span class="fq-nat">🌎 ${t('native')}</span>`:''}
function who(m,lang){return `<span class="av" data-prof="${esc(m.uid)}" style="cursor:pointer">${esc(m.avatar||'🙂')}</span><div class="who"><b data-prof="${esc(m.uid)}" style="cursor:pointer">${esc(m.name)}</b>${badge(m,lang)}<small>${m.native?esc(t('speaks'))+' '+esc(lbl(m.native))+' · ':''}${esc(ago(m.ts))}</small></div>`}

async function page(arg){
  if(arg&&arg.startsWith&&arg.startsWith('q:'))return detail(arg.slice(2));
  const me=C().user();
  C().shell(`${C().subtabs('ask')}<div class="fq-head"><div><h2>❓ ${t('tab')}</h2><p>${t('tip')}</p></div><button class="pg-btn" id="fq-new">＋ ${t('ask')}</button></div>
   <div class="fq-chips" id="fq-lang"><button class="pg-chip" data-l="" aria-pressed="${!st.lang}">${t('all')}</button>${C().LIDS.map(i=>`<button class="pg-chip" data-l="${i}" aria-pressed="${st.lang===i}">${esc(lbl(i))}</button>`).join('')}</div>
   <div class="fq-chips" id="fq-kind"><button class="pg-chip" data-k="" aria-pressed="${!st.kind}">${t('allK')}</button>${KINDS.map(x=>`<button class="pg-chip" data-k="${x}" aria-pressed="${st.kind===x}">${KIC[x]} ${t(x)}</button>`).join('')}
    <button class="pg-chip" id="fq-un" aria-pressed="${st.unans}">🕊️ ${t('unans')}</button>${me&&me.native?`<button class="pg-chip" id="fq-me" aria-pressed="${st.forMe}">🌎 ${t('forMe')}</button>`:''}</div>
   <div id="fq-list" class="fq-list"><p class="pg-empty">${t('loading')}</p></div>`);
  C().wireTabs();
  $('#fq-lang').onclick=e=>{const b=e.target.closest('[data-l]');if(b){st.lang=b.dataset.l||null;st.forMe=false;page()}};
  $('#fq-kind').onclick=e=>{const b=e.target.closest('[data-k]');if(b){st.kind=b.dataset.k||null;page()}};
  $('#fq-un').onclick=()=>{st.unans=!st.unans;page()};
  const fm=$('#fq-me');if(fm)fm.onclick=()=>{st.forMe=!st.forMe;if(st.forMe)st.lang=me.native;page()};
  $('#fq-new').onclick=()=>askForm();
  $('#fq-list').onclick=e=>{const c=e.target.closest('[data-q]');if(c)C().open('ask','q:'+c.dataset.q);const m=e.target.closest('#fq-more');if(m)load(true)};
  load(false);
}
async function load(append){
  const box=$('#fq-list');if(!box)return;
  try{
    const before=append&&st.qs.length?st.qs[st.qs.length-1].id:null;
    const r=await DB().list({lang:st.lang,kind:st.kind,unans:st.unans,before:before,limit:20});
    st.qs=append?st.qs.concat(r.items):r.items;st.more=r.more;
    if(!$('#fq-list'))return;
    box.innerHTML=st.qs.length?st.qs.map(card).join('')+(st.more?`<button class="pg-btn ghost" id="fq-more" style="margin:10px auto;display:flex">${t('more')}</button>`:''):`<p class="pg-empty">${t('noQ')}</p>`;
  }catch(e){box.innerHTML=`<p class="pg-empty">${esc(e.message||t('err'))}</p>`}
}
function card(q){
  return `<article class="pg-card fq-card" data-q="${esc(q.id)}" tabindex="0"><div class="top">${who(q,q.lang)}</div>
   <div class="fq-tags"><span class="fq-k">${KIC[q.kind]||''} ${esc(t(q.kind))}</span><span class="fq-l">${esc(lbl(q.lang))}</span>${q.best?`<span class="fq-ok">✅ ${t('solved')}</span>`:''}</div>
   <p class="fq-text">${esc(q.text)}</p>${q.ctx?`<p class="fq-ctx">${esc(q.ctx)}</p>`:''}
   <div class="fq-foot">💬 ${q.answers} ${q.answers===1?t('answer'):t('answers')}</div></article>`;
}
function askForm(){
  const me=C().user();if(!me)return C().open('auth');
  const box=$('#fq-list')||document.body;let lang=st.lang||(me.learning&&me.learning[0])||'en',kind='natural';
  const wrap=document.createElement('div');wrap.className='fq-modal';
  wrap.innerHTML=`<div class="pg-card fq-form" role="dialog" aria-modal="true"><h3>${t('askT')}</h3>
   <div class="pg-field"><span>${t('about')}</span><div class="pg-chips" id="f-lang">${C().LIDS.map(i=>`<button type="button" class="pg-chip" data-l="${i}" aria-pressed="${i===lang}">${esc(lbl(i))}</button>`).join('')}</div></div>
   <div class="pg-field"><span>${t('type')}</span><div class="pg-chips" id="f-kind">${KINDS.map(x=>`<button type="button" class="pg-chip" data-k="${x}" aria-pressed="${x===kind}">${KIC[x]} ${t(x)}</button>`).join('')}</div></div>
   <label class="pg-field"><span>${t('text')}</span><textarea id="f-text" maxlength="600" rows="3" placeholder="${esc(t('textPh'))}"></textarea></label>
   <label class="pg-field"><span>${t('ctx')}</span><textarea id="f-ctx" maxlength="300" rows="2" placeholder="${esc(t('ctxPh'))}"></textarea></label>
   <div class="pg-err" id="f-err" role="alert"></div>
   <div style="display:flex;gap:10px;justify-content:flex-end"><button class="pg-btn ghost" id="f-cancel">${t('cancel')}</button><button class="pg-btn" id="f-send">${t('send')}</button></div></div>`;
  document.body.appendChild(wrap);const close=()=>wrap.remove();
  wrap.onclick=e=>{if(e.target===wrap)close()};$('#f-cancel',wrap).onclick=close;
  $('#f-lang',wrap).onclick=e=>{const b=e.target.closest('[data-l]');if(!b)return;lang=b.dataset.l;wrap.querySelectorAll('#f-lang button').forEach(x=>x.setAttribute('aria-pressed',x===b))};
  $('#f-kind',wrap).onclick=e=>{const b=e.target.closest('[data-k]');if(!b)return;kind=b.dataset.k;wrap.querySelectorAll('#f-kind button').forEach(x=>x.setAttribute('aria-pressed',x===b))};
  $('#f-send',wrap).onclick=async()=>{const text=$('#f-text',wrap).value.trim(),ctx=$('#f-ctx',wrap).value.trim(),er=$('#f-err',wrap),bt=$('#f-send',wrap);
    if(text.length<3){er.textContent=t('tooShort');return}
    bt.disabled=true;er.textContent='';
    try{await DB().ask({lang,kind,text,ctx});if(window.PogUI&&PogUI.bump)try{PogUI.bump('msgs')}catch(e){}close();st.lang=lang;page()}
    catch(x){er.textContent=x.message||t('err');bt.disabled=false}};
  setTimeout(()=>{const f=$('#f-text',wrap);if(f)f.focus()},50);
}
async function detail(id){
  C().shell(`${C().subtabs('ask')}<div id="fq-d"><p class="pg-empty">${t('loading')}</p></div>`);C().wireTabs();
  const box=$('#fq-d'),me=C().user();
  const draw=async()=>{
    let d;try{d=await DB().get(isNaN(+id)?id:+id)}catch(e){box.innerHTML=`<button class="pg-btn ghost sm" id="fq-b">← ${t('back')}</button><p class="pg-empty">${esc(e.message||t('err'))}</p>`;$('#fq-b').onclick=()=>C().open('ask');return}
    const q=d.q,mine=q.uid===me.id;
    const as=d.answers.slice().sort((a,b)=>(b.id===q.best)-(a.id===q.best)||b.likes-a.likes||a.id-b.id);
    box.innerHTML=`<button class="pg-btn ghost sm" id="fq-b" style="margin-bottom:12px">← ${t('back')}</button>
     <article class="pg-card fq-card big"><div class="top">${who(q,q.lang)}</div>
      <div class="fq-tags"><span class="fq-k">${KIC[q.kind]||''} ${esc(t(q.kind))}</span><span class="fq-l">${esc(lbl(q.lang))}</span></div>
      <p class="fq-text">${esc(q.text)}</p>${q.ctx?`<p class="fq-ctx">${esc(q.ctx)}</p>`:''}
      <div class="fq-acts">${mine?`<button data-dq>🗑 ${t('del')}</button>`:`<button data-rq>🚩 ${t('report')}</button>`}</div></article>
     <h3 class="fq-h">${as.length} ${as.length===1?t('answer'):t('answers')}</h3>
     <div class="fq-answers">${as.length?as.map(a=>{const best=a.id===q.best,lk=d.liked.has(a.id),own=a.uid===me.id;
       return `<article class="pg-card fq-ans ${best?'best':''}">${best?`<div class="fq-bt">✅ ${t('best')}</div>`:''}<div class="top">${who(a,q.lang)}</div>${a.audio&&window.PogExtras?PogExtras.voiceHTML(a.audio):`<p class="fq-text">${esc(a.text)}</p>`}
       <div class="fq-acts"><button data-like="${esc(a.id)}" aria-pressed="${lk}">👍 ${t('useful')} · ${a.likes}</button>
       ${mine?`<button data-best="${esc(a.id)}">${best?t('unpick'):'✅ '+t('pick')}</button>`:''}${own?`<button data-da="${esc(a.id)}">🗑 ${t('del')}</button>`:`<button data-ra="${esc(a.id)}">🚩 ${t('report')}</button>`}</div></article>`}).join(''):`<p class="pg-empty">${t('noA')}</p>`}</div>
     <form class="pg-card fq-reply" id="fq-f"><label class="pg-field"><span>${t('yourAns')}</span><textarea id="fq-t" maxlength="1000" rows="3" placeholder="${esc(t('ansPh'))}"></textarea></label>
      <div class="pg-err" id="fq-e" role="alert"></div><div style="display:flex;gap:8px;justify-content:flex-end">${window.PogExtras?PogExtras.micBtn():''}<button class="pg-btn" id="fq-s">${t('reply')}</button></div></form>`;
    $('#fq-b').onclick=()=>C().open('ask');
    const act=async fn=>{try{await fn();draw()}catch(x){alert(x.message||t('err'))}};
    box.onclick=e=>{
      const l=e.target.closest('[data-like]');if(l)return act(()=>DB().like(+l.dataset.like||l.dataset.like,l.getAttribute('aria-pressed')!=='true'));
      const b=e.target.closest('[data-best]');if(b){const aid=+b.dataset.best||b.dataset.best;return act(()=>DB().best(q.id,q.best===aid?0:aid))}
      if(e.target.closest('[data-dq]')){if(confirm(t('delQ')))DB().del('q',q.id).then(()=>C().open('ask')).catch(x=>alert(x.message));return}
      const da=e.target.closest('[data-da]');if(da)return act(()=>DB().del('a',+da.dataset.da||da.dataset.da));
      const rq=e.target.closest('[data-rq]');if(rq){const w=prompt(t('report')+'?','');if(w===null)return;DB().report('q',q.id,w).then(()=>alert(t('reported'))).catch(x=>alert(x.message));return}
      const ra=e.target.closest('[data-ra]');if(ra){const w=prompt(t('report')+'?','');if(w===null)return;DB().report('a',+ra.dataset.ra||ra.dataset.ra,w).then(()=>alert(t('reported'))).catch(x=>alert(x.message))}
    };
    const mic=$('[data-mic]');if(mic)mic.onclick=()=>PogExtras.record($('#fq-f'),async blob=>{const path=await cloud().uploadVoice(blob);await DB().answer(q.id,'🎤',path);draw()});
    $('#fq-f').onsubmit=async ev=>{ev.preventDefault();const tx=$('#fq-t').value.trim(),er=$('#fq-e');if(!tx)return;$('#fq-s').disabled=true;er.textContent='';
      try{await DB().answer(q.id,tx);try{PogUI.bump('msgs')}catch(e){}draw()}catch(x){er.textContent=x.message||t('err');$('#fq-s').disabled=false}};
  };
  draw();
}
window.PogForum={page};
})();
