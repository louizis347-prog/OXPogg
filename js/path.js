/* Pogglot · trilha personalizada
   - teste de nível (adaptativo, com perguntas do próprio curso)
   - caderno de erros: o que o aluno erra (quiz e fala) volta em uma revisão prioritária
   - cartão "Para você hoje" na tela inicial: meta do dia, próximo episódio, erros e teste de nível */
(function(){
'use strict';
const store={get(k,d){try{const v=localStorage.getItem('pogglot:'+k);return v?JSON.parse(v):d}catch(e){return d}},set(k,v){try{localStorage.setItem('pogglot:'+k,JSON.stringify(v))}catch(e){}}};
const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const bold=s=>esc(s).replace(/\*\*(.+?)\*\*/g,'<b>$1</b>');
const HL=()=>(typeof ST!=='undefined'&&ST.homeLang)||'pt';
const TX={
 pt:{today:'Para você hoje',goal:'Meta do dia',next:'Seu próximo passo',cont:'Continuar',errs:'Seus pontos fracos',errsN:n=>n+(n===1?' item para reforçar':' itens para reforçar'),errsNone:'Nenhum erro guardado. Continue assim!',rev:'Reforçar agora',
  test:'Teste de nível',testSub:'Descubra por onde começar. Leva uns 3 minutos.',testBtn:'Fazer o teste',placed:'Seu ponto de partida',redo:'Refazer teste',start:'Começar aqui',
  lang:'Idioma do teste',q:'Pergunta',dk:'Não sei',stop:'Fechar',res:'Resultado',lvl:'Você começa em',none:'Do começo',noPool:'Ainda não há perguntas suficientes para este idioma.',loading:'Preparando perguntas…',
  review:'Reforço dos seus erros',of:'de',again:'Ouça e tente de novo',next2:'Próxima ▶',done:'Concluir',allDone:'Reforço concluído! Os itens que você acertou saíram da lista.',right:'Certo!',wrong:'Quase! A resposta é',say:'Diga em voz alta',steps:'Etapa',
  daily:'XP hoje',goalOk:'Meta batida! 🎉',open:'Abrir ajustes'},
 es:{today:'Para ti hoy',goal:'Meta del día',next:'Tu próximo paso',cont:'Continuar',errs:'Tus puntos débiles',errsN:n=>n+(n===1?' ítem por reforzar':' ítems por reforzar'),errsNone:'Ningún error guardado. ¡Sigue así!',rev:'Reforzar ahora',
  test:'Prueba de nivel',testSub:'Descubre por dónde empezar. Dura unos 3 minutos.',testBtn:'Hacer la prueba',placed:'Tu punto de partida',redo:'Repetir prueba',start:'Empezar aquí',
  lang:'Idioma de la prueba',q:'Pregunta',dk:'No sé',stop:'Cerrar',res:'Resultado',lvl:'Empiezas en',none:'Desde el inicio',noPool:'Aún no hay preguntas suficientes para este idioma.',loading:'Preparando preguntas…',
  review:'Refuerzo de tus errores',of:'de',again:'Escucha e inténtalo de nuevo',next2:'Siguiente ▶',done:'Terminar',allDone:'¡Refuerzo terminado! Lo que acertaste salió de la lista.',right:'¡Correcto!',wrong:'Casi. La respuesta es',say:'Dilo en voz alta',steps:'Etapa',
  daily:'XP hoy',goalOk:'¡Meta cumplida! 🎉',open:'Abrir ajustes'}
};
const k=key=>{const t=TX[HL()]||TX.pt;return t[key]!=null?t[key]:TX.pt[key]};
const LNAME={en:'Inglês',es:'Espanhol',pt:'Português',fr:'Francês',de:'Alemão'};
const SUBS=['en-a1','en-a2','en-b1','en-b2','en-c1','en-c2'];
const LABELS={en:['A1','A2','B1','B2','C1','C2'],es:['A1','A2','B1','B2','C1','C2']};
const SUBS_BY={en:SUBS,es:['es-a1','es-a2','es-b1','es-b2','es-c1','es-c2']};
const LABELS_OTHER=['Início','Básico','Intermediário','Avançado','Fluente'];
const grp=cid=>String(cid).split('-')[0];
const shuf=a=>{a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a};
const hash=s=>{let h=0;for(const c of String(s))h=(h*31+c.charCodeAt(0))>>>0;return h.toString(36)};
const langOf=cid=>(typeof COURSES!=='undefined'&&COURSES[cid]&&COURSES[cid].tts)||'en-US';
const say=(t,lang)=>{try{if(typeof speak==='function')speak(String(t).replace(/\*\*/g,''),lang)}catch(e){}};

/* ================= caderno de erros ================= */
const MAXE=120;
const E=()=>store.get('errs',{});
const saveE=e=>store.set('errs',e);
function miss(o){
  try{
    const q=String(o.q||o.a||'');if(!q)return;
    const e=E(),key=(o.kind||'q')+'|'+hash((o.cid||'')+q+(o.a||''));
    const it=e[key]||{c:0,first:Date.now()};
    Object.assign(it,{kind:o.kind||'choose',cid:o.cid,n:o.n,q:o.q,opts:o.opts||null,a:o.a,ai:o.ai,say:o.say||'',why:o.why||'',lang:o.lang||langOf(o.cid),last:Date.now()});
    it.c=Math.min(9,(it.c||0)+1);e[key]=it;
    const ks=Object.keys(e);if(ks.length>MAXE){ks.sort((a,b)=>e[a].last-e[b].last).slice(0,ks.length-MAXE).forEach(x=>delete e[x])}
    saveE(e);
  }catch(x){}
}
function hit(o){ /* acertou um item que estava na lista: baixa o peso */
  try{const e=E(),key=(o.kind||'q')+'|'+hash((o.cid||'')+String(o.q||o.a||'')+(o.a||''));
    if(e[key]){e[key].c-=1;if(e[key].c<=0)delete e[key];saveE(e)}}catch(x){}
}
function errList(){const e=E(),now=Date.now();return Object.keys(e).map(key=>({key,it:e[key],w:e[key].c*3+Math.max(0,3-(now-e[key].last)/864e5)})).sort((a,b)=>b.w-a.w)}
function errCount(){return Object.keys(E()).length}
document.addEventListener('pogglot:speak',ev=>{
  const d=ev.detail||{};if(!d.target)return;
  const cid=(typeof P!=='undefined'&&P&&P.cid)||null;
  if(d.score<65)miss({kind:'speak',cid,n:(typeof P!=='undefined'&&P&&P.e&&P.e.n)||0,q:d.target,a:d.target,lang:d.lang||langOf(cid),say:d.target});
  else if(d.score>=85)hit({kind:'speak',cid,q:d.target,a:d.target});
});

/* ================= estrutura de níveis ================= */
const placed=()=>store.get('placed',{});
function nextEp(){
  try{
    let cid=ST.lastCourse;
    const pl=placed();
    if(!cid||!COURSES[cid]){const g=Object.keys(pl)[0];cid=g?pl[g].cid:'en-a1'}
    const eps=EP[cid];if(!eps||!eps.length)return{cid,idx:0,e:null};
    const p=pl[grp(cid)],start=p&&p.cid===cid?p.start||0:0,done=x=>ST.done[cid+'-'+x.n]||isPlannedEpisode(x);
    let idx=eps.findIndex((x,i)=>i>=start&&!done(x));if(idx<0)idx=eps.findIndex(x=>!done(x));
    return idx<0?null:{cid,idx,e:eps[idx]};
  }catch(e){return null}
}

/* ================= teste de nível ================= */
function okRound(r){return r&&typeof r.q==='string'&&Array.isArray(r.opts)&&r.opts.length>=2&&r.opts.every(o=>typeof o==='string')&&typeof r.a==='number'&&(!r.t||r.t==='choose'||r.t==='gap'||r.t==='trap')}
function poolFrom(eps,cid){
  const out=[];
  eps.forEach(e=>(e.fr||[]).forEach(f=>{if(f.k==='gap'||f.k==='choose'||f.k==='trap')(f.rounds||[]).forEach(r=>{if(okRound(r))out.push({cid,n:e.n,e:e.n,q:r.q,opts:r.opts,a:r.a,why:r.why||'',style:r.t||f.k})})}));
  return out;
}
async function getJSON(f){const r=await fetch('data/'+f);if(!r.ok)throw new Error('fetch');return r.json()}
async function buildBands(gid){
  if(SUBS_BY[gid]){
    const out=[],SB=SUBS_BY[gid];
    for(let i=0;i<SB.length;i++){
      const cid=SB[i],files=(MANIFEST&&MANIFEST[cid])||[];
      let eps=[];
      const chosen=shuf(files).slice(0,2);
      for(const f of chosen){try{eps=eps.concat(await getJSON(f))}catch(e){}}
      out.push({cid,start:0,label:LABELS[gid][i],pool:shuf(poolFrom(eps,cid))});
    }
    return out;
  }
  await ensureLangLoaded(gid);
  const eps=EP[gid]||[];if(eps.length<10)return[];
  const B=eps.length>=100?5:eps.length>=40?4:3,out=[];
  for(let b=0;b<B;b++){
    const a=Math.floor(b*eps.length/B),z=Math.floor((b+1)*eps.length/B);
    const labels=B===5?LABELS_OTHER:B===4?['Início','Básico','Intermediário','Avançado']:['Início','Intermediário','Avançado'];
    out.push({cid:gid,start:a,label:labels[b],pool:shuf(poolFrom(eps.slice(a,z),gid))});
  }
  return out;
}
function pickQ(band,used){
  const seen=new Set(used.map(u=>u.n));
  let c=band.pool.find(q=>!seen.has(q.n)&&!used.includes(q))||band.pool.find(q=>!used.includes(q));
  return c||null;
}
function shell(){
  closeM();
  const el=document.createElement('div');el.className='ptm';el.id='ptm';el.setAttribute('role','dialog');el.setAttribute('aria-modal','true');
  document.body.appendChild(el);document.body.classList.add('pgs-open');return el;
}
function closeM(){const e=document.getElementById('ptm');if(e)e.remove();document.body.classList.remove('pgs-open');try{speechSynthesis.cancel()}catch(x){}}
function startEp(cid,idx){
  closeM();
  const b=document.createElement('button');b.dataset.ep=cid+':'+idx;b.style.display='none';document.body.appendChild(b);b.click();b.remove();
}

async function openTest(gid){
  const el=shell();
  const langs=['en','es','pt','fr','de'];
  if(!gid){
    const cur=(typeof P!=='undefined'&&P&&P.cid&&grp(P.cid))||(ST.lastCourse&&grp(ST.lastCourse))||'en';
    el.innerHTML=`<div class="ptm-card"><div class="ptm-top"><b>🧭 ${esc(k('test'))}</b><button class="ptm-x" aria-label="${esc(k('stop'))}">×</button></div>
      <p class="ptm-sub">${esc(k('testSub'))}</p><div class="ptm-langs">${langs.filter(l=>l!=='pt'||true).map(l=>`<button class="ptm-lang ${l===cur?'on':''}" data-l="${l}">${LNAME[l]}</button>`).join('')}</div></div>`;
    el.querySelector('.ptm-x').onclick=closeM;
    el.querySelectorAll('.ptm-lang').forEach(b=>b.onclick=()=>openTest(b.dataset.l));
    return;
  }
  el.innerHTML=`<div class="ptm-card"><div class="ptm-top"><b>🧭 ${esc(k('test'))} · ${esc(LNAME[gid]||gid)}</b><button class="ptm-x">×</button></div><p class="ptm-sub">${esc(k('loading'))}</p></div>`;
  el.querySelector('.ptm-x').onclick=closeM;
  let bands=[];try{bands=await buildBands(gid)}catch(e){}
  bands=bands.filter(b=>b.pool.length>=2);
  if(!document.getElementById('ptm'))return;
  if(bands.length<2){el.querySelector('.ptm-sub').textContent=k('noPool');return}
  let bi=0,asked=[],right=0,qn=0,passed=-1;
  const used=[];
  const finish=()=>{
    const first=passed+1>=bands.length?bands.length-1:passed+1;/* onde começar: primeira faixa não dominada */
    const b=bands[first];
    const lvl=passed<0?k('none'):bands[passed].label;
    const rec={band:first,cid:b.cid,start:b.start,label:passed<0?bands[0].label:b.label,passed:lvl,date:Date.now()};
    const p=placed();p[gid]=rec;store.set('placed',p);
    if(gid==='en'||first===0){try{ST.lastCourse=b.cid;save()}catch(e){}}
    el.innerHTML=`<div class="ptm-card"><div class="ptm-top"><b>🧭 ${esc(k('res'))}</b><button class="ptm-x">×</button></div>
      <div class="ptm-res"><small>${esc(k('lvl'))}</small><b>${esc(rec.label)}</b><span>${esc(LNAME[gid]||gid)}</span></div>
      <div class="ptm-bars">${bands.map((x,i)=>`<i class="${i<=passed?'ok':i===first?'now':''}" title="${esc(x.label)}"><em>${esc(x.label)}</em></i>`).join('')}</div>
      <button class="ptm-btn" id="ptgo">${esc(k('start'))} ▶</button></div>`;
    el.querySelector('.ptm-x').onclick=()=>{closeM();refreshHome()};
    el.querySelector('#ptgo').onclick=()=>{navStart(rec)};
  };
  const navStart=async rec=>{try{await ensureLangLoaded(rec.cid)}catch(e){}const eps=EP[rec.cid]||[];let idx=Math.max(0,eps.findIndex((x,i)=>i>=rec.start&&!ST.done[rec.cid+'-'+x.n]));startEp(rec.cid,idx<0?rec.start:idx)};
  const ask=()=>{
    const band=bands[bi];
    if(!asked[bi])asked[bi]={n:0,ok:0};
    const A=asked[bi];
    /* decisão: 2 acertos seguidos de 2 → passa; 0 de 2 → para; 1 de 2 → pergunta uma terceira */
    if(A.n===2&&A.ok===2||A.n===3&&A.ok>=2){passed=bi;if(bi===bands.length-1)return finish();bi++;return ask()}
    if(A.n===2&&A.ok===0||A.n===3&&A.ok<2)return finish();
    const q=pickQ(band,used);if(!q){if(A.ok>=A.n/2&&A.n>0){passed=bi;if(bi===bands.length-1)return finish();bi++;return ask()}return finish()}
    used.push(q);qn++;
    const total=bands.length;
    const opts=q.opts.map((o,i)=>[o,i]);const sh=shuf(opts);
    el.innerHTML=`<div class="ptm-card"><div class="ptm-top"><b>🧭 ${esc(k('test'))} · ${esc(LNAME[gid]||gid)}</b><button class="ptm-x">×</button></div>
      <div class="ptm-prog"><i style="width:${Math.round(bi/total*100)}%"></i></div><small class="ptm-n">${esc(k('q'))} ${qn}</small>
      <div class="ptm-q">${bold(q.q).replace('___','<span class="hole">____</span>')}</div>
      <div class="ptm-opts">${sh.map(([o,i])=>`<button class="ptm-o" data-i="${i}">${esc(o)}</button>`).join('')}<button class="ptm-o dk" data-i="-1">${esc(k('dk'))}</button></div></div>`;
    el.querySelector('.ptm-x').onclick=()=>{closeM();refreshHome()};
    el.querySelectorAll('.ptm-o').forEach(b=>b.onclick=()=>{
      const i=+b.dataset.i,ok=i===q.a;A.n++;if(ok)A.ok++;
      if(!ok&&i>=0)miss({kind:'choose',cid:q.cid,n:q.n,q:q.q,opts:q.opts,a:q.a,why:q.why,lang:langOf(q.cid)});
      el.querySelectorAll('.ptm-o').forEach(x=>{x.disabled=true;if(+x.dataset.i===q.a)x.classList.add('ok');else if(x===b)x.classList.add('no')});
      setTimeout(ask,ok?500:900);
    });
  };
  ask();
}

/* ================= reforço dos erros ================= */
function openReview(){
  const list=errList().slice(0,10);
  const el=shell();
  if(!list.length){el.innerHTML=`<div class="ptm-card"><div class="ptm-top"><b>🎯 ${esc(k('review'))}</b><button class="ptm-x">×</button></div><p class="ptm-sub">${esc(k('errsNone'))}</p></div>`;el.querySelector('.ptm-x').onclick=()=>{closeM();refreshHome()};return}
  let i=0,fixed=0;
  const draw=()=>{
    if(i>=list.length){
      el.innerHTML=`<div class="ptm-card"><div class="ptm-top"><b>🎯 ${esc(k('review'))}</b><button class="ptm-x">×</button></div><div class="ptm-res"><b>${fixed}/${list.length}</b><span>${esc(k('allDone'))}</span></div><button class="ptm-btn" id="ptfin">${esc(k('done'))}</button></div>`;
      el.querySelector('.ptm-x').onclick=el.querySelector('#ptfin').onclick=()=>{closeM();refreshHome()};
      try{ST.xp+=fixed*2;save()}catch(e){}return}
    const {it}=list[i];
    const head=`<div class="ptm-top"><b>🎯 ${esc(k('review'))}</b><button class="ptm-x">×</button></div><div class="ptm-prog"><i style="width:${Math.round(i/list.length*100)}%"></i></div><small class="ptm-n">${i+1} ${esc(k('of'))} ${list.length}</small>`;
    if(it.kind==='speak'){
      el.innerHTML=`<div class="ptm-card">${head}<div class="ptm-q"><button class="ptm-play" id="pl">🔊</button> <b>${esc(it.q)}</b></div><p class="ptm-sub">${esc(k('say'))}</p><div id="ptmic" class="pv-host"></div><button class="ptm-btn ghost" id="pnx">${esc(k('next2'))}</button></div>`;
      el.querySelector('#pl').onclick=()=>say(it.q,it.lang);setTimeout(()=>say(it.q,it.lang),250);
      el.querySelector('.ptm-x').onclick=()=>{closeM();refreshHome()};
      el.querySelector('#pnx').onclick=()=>{i++;draw()};
      if(window.PogVoice)PogVoice.mount(el.querySelector('#ptmic'),{target:it.q,lang:it.lang,onDone:r=>{if(r.score>=75)fixed++}});
      return}
    const opts=(it.opts||[]).map((o,j)=>[Array.isArray(o)?o[1]:o,j]),sh=shuf(opts);
    el.innerHTML=`<div class="ptm-card">${head}<div class="ptm-q">${it.say?`<button class="ptm-play" id="pl">🔊</button> `:''}${bold(it.q||'').replace('___','<span class="hole">____</span>')}</div>
      <div class="ptm-opts">${sh.map(([o,j])=>`<button class="ptm-o" data-i="${j}">${esc(o)}</button>`).join('')}</div><div id="ptfb"></div></div>`;
    el.querySelector('.ptm-x').onclick=()=>{closeM();refreshHome()};
    const pl=el.querySelector('#pl');if(pl)pl.onclick=()=>say(it.say,it.lang);
    el.querySelectorAll('.ptm-o').forEach(b=>b.onclick=()=>{
      const j=+b.dataset.i,ok=j===it.ai;
      el.querySelectorAll('.ptm-o').forEach(x=>{x.disabled=true;if(+x.dataset.i===it.ai)x.classList.add('ok');else if(x===b)x.classList.add('no')});
      if(ok){fixed++;hit({kind:it.kind,cid:it.cid,q:it.q,a:it.a})}else miss({kind:it.kind,cid:it.cid,n:it.n,q:it.q,opts:it.opts,a:it.a,ai:it.ai,say:it.say,why:it.why,lang:it.lang});
      const right=(it.opts||[])[it.ai];
      el.querySelector('#ptfb').innerHTML=`<div class="ptm-fb ${ok?'ok':'no'}"><b>${ok?esc(k('right')):esc(k('wrong'))+' '+esc(Array.isArray(right)?right[1]:right)}</b>${it.why?'<br>'+bold(it.why):''}</div><button class="ptm-btn" id="pnx">${esc(k('next2'))}</button>`;
      el.querySelector('#pnx').onclick=()=>{i++;draw()};
      if(it.say&&ok)say(it.say,it.lang);
    });
  };
  draw();
}

/* ================= cartão da tela inicial ================= */
function refreshHome(){try{if(typeof P!=='undefined'&&P)return;if(document.querySelector('.pt-today'))renderCard()}catch(e){}}
function cardHTML(){
  const S=window.PogSettings,g=S&&S.goalState?S.goalState():null;
  const nx=nextEp(),n=errCount(),pl=placed();
  const nm=nx&&COURSES[nx.cid]?COURSES[nx.cid].name[HL()]||COURSES[nx.cid].name.pt:'';
  const p=nx?pl[grp(nx.cid)]:null;
  return `<div class="pt-h"><h2>🌟 ${esc(k('today'))}</h2></div><div class="pt-grid">
    ${g?`<div class="pt-c pt-goal"><div class="ring">${S.ringHTML(g.pct,64,8)}<span>${Math.round(g.pct*100)}%</span></div><div><small>${esc(k('goal'))}</small><b>${g.xp}/${g.goal} XP</b><em>${g.met?esc(k('goalOk')):(g.streak?'🔥 '+g.streak:'')}</em></div><button class="pt-link" data-pt="settings" aria-label="${esc(k('open'))}">⚙️</button></div>`:''}
    ${nx?`<div class="pt-c"><small>${esc(k('next'))}</small><b>${nx.e?'EP '+(nx.e.en||nx.idx+1)+' · '+esc(nx.e.t):esc(nm)}</b><em>${esc(nm)}${p?' · '+esc(p.label):''}</em><button class="pill" data-ep="${nx.cid}:${nx.idx}">${esc(k('cont'))} ▶</button></div>`:''}
    <div class="pt-c"><small>${esc(k('errs'))}</small><b>${n?esc(k('errsN')(n)):esc(k('errsNone'))}</b>${n?`<button class="pill" data-pt="review">${esc(k('rev'))}</button>`:''}</div>
    <div class="pt-c"><small>${esc(k('test'))}</small><b>${Object.keys(pl).length?esc(k('placed'))+': '+Object.keys(pl).map(x=>esc((LNAME[x]||x)+' '+pl[x].label)).join(' · '):esc(k('testSub'))}</b><button class="pill light" data-pt="test">${Object.keys(pl).length?esc(k('redo')):esc(k('testBtn'))}</button></div></div>`;
}
let loadingFor=null;
function renderCard(){
  const host=document.querySelector('.pt-today');if(!host)return;host.innerHTML=cardHTML();
  const nx=nextEp();
  /* não baixa o curso inteiro só para escrever o título do próximo episódio: espera ficar ocioso e pula em conexão lenta ou economia de dados */
  const slowNet=()=>{try{const c=navigator.connection;return !!(c&&(c.saveData||/(^|-)(2g|3g)$/.test(c.effectiveType||'')))}catch(e){return false}};
  if(nx&&!nx.e&&loadingFor!==nx.cid&&typeof ensureLangLoaded==='function'&&!slowNet()){loadingFor=nx.cid;const cid=nx.cid,go=()=>ensureLangLoaded(cid).then(()=>{loadingFor=null;if(document.querySelector('.pt-today'))renderCard()}).catch(()=>{loadingFor=null});
    setTimeout(()=>{(window.requestIdleCallback||(f=>f()))(go,{timeout:3000})},4000)}
}
{const _home=window.home;if(_home)window.home=function(){const r=_home.apply(this,arguments);
  try{const hero=document.querySelector('#app .pg-stats')||document.querySelector('#app .pg-hero')||document.querySelector('#app .hero');if(hero&&!document.querySelector('.pt-today')){const s=document.createElement('section');s.className='pt-today';hero.insertAdjacentElement('afterend',s);renderCard()}}catch(e){}
  return r}}
document.addEventListener('click',ev=>{
  const b=ev.target.closest('[data-pt]');if(!b)return;ev.preventDefault();
  const a=b.dataset.pt;
  if(a==='test')openTest();
  else if(a==='review'){const cs=new Set(errList().slice(0,10).map(x=>x.it.cid).filter(Boolean));Promise.all([...cs].map(c=>typeof ensureLangLoaded==='function'?ensureLangLoaded(c):0)).catch(()=>{}).then(openReview)}
  else if(a==='settings'&&window.PogSettings)PogSettings.open();
});

window.PogPath={nextEp,miss,hit,errCount,errList,openTest,openReview,placed,closeM,renderCard};
})();
