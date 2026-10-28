/* Figurinhas das obras + Álbum cultural.
   Cada episódio concluído dos cursos regulares rende uma figurinha da obra (cena e personagens do episódio),
   com raridade pelo desempenho (comum, rara, dourada). O álbum reúne tudo por seções (filmes, séries, livros…). */
(function(){
'use strict';
const K='pogglot:figs';
const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const load=()=>{try{return JSON.parse(localStorage.getItem(K)||'{}')}catch(e){return {}}};
const save=o=>{try{localStorage.setItem(K,JSON.stringify(o))}catch(e){}};
const RANK={bronze:0,silver:1,gold:2};
const TIER={gold:{ico:'🥇',medal:'Medalha de ouro',rar:'Dourada'},silver:{ico:'🥈',medal:'Medalha de prata',rar:'Rara'},bronze:{ico:'🥉',medal:'Medalha de bronze',rar:'Comum'}};
const CATS=[
  {id:'film',name:'Filmes e animações',ico:'🎬',c1:'#E85D75',c2:'#7B2350'},
  {id:'series',name:'Séries e TV',ico:'📺',c1:'#3E8FD8',c2:'#1B4585'},
  {id:'book',name:'Livros e contos',ico:'📖',c1:'#F29B34',c2:'#9A4E14'},
  {id:'music',name:'Música e poesia',ico:'🎵',c1:'#9B6AD8',c2:'#4A2A86'},
  {id:'art',name:'Arte e arquitetura',ico:'🖼️',c1:'#2FB0A0',c2:'#166057'},
  {id:'theatre',name:'Teatro e ópera',ico:'🎭',c1:'#D8493B',c2:'#6B1D18'},
  {id:'game',name:'Jogos e quadrinhos',ico:'🎮',c1:'#2FAE6C',c2:'#0F5A37'},
  {id:'history',name:'História e lugares',ico:'🏛️',c1:'#C08A2A',c2:'#6A4410'}
];
const CAT=Object.fromEntries(CATS.map(c=>[c.id,c]));
function categorize(a){
  const t=((a&&a.k)||'').toLowerCase().replace(/[^\p{L}\s]/gu,' ');
  const w=((a&&a.w)||'').toLowerCase();
  const has=re=>re.test(t);
  if(has(/s[eé]rie|sitcom|seriado|programa de tv|reality|telenovela|\btv\b/))return 'series';
  if(has(/\bgame|videogame|jogo|quadrinh|mang[aá]|tirinha|\bhq\b|graphic/))return 'game';
  if(has(/[oó]pera|pe[cç]a|teatro|shakespeare|musical/))return 'theatre';
  if(has(/filme|pel[ií]cula|anima[cç][aã]o|cinema|document[aá]rio|longa/))return 'film';
  if(has(/m[uú]sica|can[cç][aã]o|canci[oó]n|cantiga|rima|poema|poesia|hino|[aá]lbum|banda|letra/))return 'music';
  if(has(/pintura|escultura|fotografia|\barte\b|quadro|artista|arquitet|fresco|afresco|desenho|museu|obra de arte/))return 'art';
  if(has(/livro|romance|conto|f[aá]bula|novela|biografia|fic[cç][aã]o|literatura|mem[oó]rias|lenda|di[aá]rio|ensaio|ci[eê]ncia/))return 'book';
  if(has(/hist[oó]ri|evento|discurso|documento|mito|cidade|lugar|monumento|institui|empresa|festival|parque|ilha|marca/))return 'history';
  if(/ ?ii|wars?|story|movie/.test(w))return 'film';
  return 'history';
}
const hash=s=>{let h=7;for(let i=0;i<String(s).length;i++)h=(h*31+String(s).charCodeAt(i))>>>0;return h};

/* ---------- dados da figurinha ---------- */
function infoFromEp(e,cid){
  if(!e)return null;
  const a=(e.a&&typeof e.a==='object')?e.a:null;
  const wrap=(e.fr||[]).find(f=>f.k==='wrap')||{};
  const st=wrap.sticker||{};
  const main=e.stage||{};
  const title=(a&&a.w)||st.title||e.t||'';
  if(!title)return null;
  return {key:cid+'-'+e.n,cid,n:e.n,ep:e.en||'',no:(()=>{try{return (EP[cid]||[]).indexOf(e)+1}catch(x){return 0}})(),title,sub:st.sub||(a?(a.w+(a.y?' · '+a.y:'')):''),
    rs:st.rs||main.rs||e.rs||'street',chars:st.chars||main.chars||[],
    cat:categorize(a),k:(a&&a.k)||'',w:(a&&a.w)||title,y:(a&&a.y)||'',d:(a&&a.d)||'',t:e.t||''};
}
function record(info,tier,acc){
  const all=load(),cur=all[info.key];
  const up=!cur||RANK[tier]>RANK[cur.tier];
  const rec=Object.assign({},cur||info,info,{tier:up?tier:cur.tier,acc:up?Math.round(acc*100):cur.acc,time:cur?cur.time:Date.now()});
  all[info.key]=rec;save(all);
  return {rec,fresh:!cur,upgraded:!!cur&&up};
}

/* ---------- carta ---------- */
let UID=0;
function art(info){
  if(window.PogObra&&PogObra.has(info))return `<div class="ps-stage sticker obra"><div class="ps-stage-bk">${PogObra.svg(info,'sticker')}</div></div>`;
  if(window.PogStage&&PogStage.stage){try{return PogStage.stage({rs:info.rs,chars:info.chars,h:'sticker'})}catch(e){}}
  return `<div class="fg-noart">${(CAT[info.cat]||CAT.history).ico}</div>`;
}
function cardHTML(info,o){
  o=o||{};const c=CAT[info.cat]||CAT.history,tier=o.lock?'lock':(info.tier||'bronze');
  const seed=hash(info.title),rot=((seed%5)-2)*0.35;
  if(o.lock)return `<div class="fg fg-lock ${o.cls||''}" style="--c1:${c.c1};--c2:${c.c2}" data-fkey="${esc(info.key||'')}"><div class="fg-top"><span class="fg-kind">${c.ico}</span><span class="fg-no">${info.no?'Nº '+String(info.no).padStart(3,'0'):(info.ep?'EP '+esc(info.ep):'')}</span></div><div class="fg-win"><span class="fg-q">?</span><i>${c.ico}</i></div><div class="fg-name"><b>Figurinha escondida</b><span class="fg-sub">${esc(c.name)}</span></div></div>`;
  return `<div class="fg fg-${tier} ${o.cls||''}" style="--c1:${c.c1};--c2:${c.c2};--rot:${rot}deg" data-fkey="${esc(info.key||'')}">
    <span class="fg-shine"></span>
    <div class="fg-top"><span class="fg-kind">${c.ico} <span class="fg-em">${esc(c.name.split(' ')[0])}</span></span><span class="fg-no">${info.no?'Nº '+String(info.no).padStart(3,'0'):(info.ep?'EP '+esc(info.ep):'')}</span></div>
    <div class="fg-win">${art(info)}<span class="fg-rar">${tier==='gold'?'★★★':tier==='silver'?'★★':'★'}</span></div>
    <div class="fg-name"><b>${esc(info.title)}</b><span class="fg-sub">${esc(info.y?info.y:(info.sub||''))}</span></div>
    <div class="fg-foot"><span>${TIER[tier].rar}</span><span>${esc(c.name)}</span></div></div>`;
}

/* ---------- fim do episódio ---------- */
function active(){
  try{return typeof P!=='undefined'&&!!P&&!P.isTest&&typeof isRegularCourse==='function'&&isRegularCourse(P.cid)&&!!infoFromEp(P.e,P.cid)}catch(e){return false}
}
function tierOf(){
  const t=P.prTries||0;let acc;
  if(t)acc=(P.prHits||0)/t;else acc=Math.min(1,(P.score||0)/Math.max(1,P.total||1));
  return {tier:acc>=.9?'gold':acc>=.7?'silver':'bronze',acc,hits:P.prHits||0,tries:t};
}
function revealHTML(){
  if(!active())return '';
  const info=infoFromEp(P.e,P.cid),r=tierOf(),res=record(info,r.tier,r.acc),T=TIER[res.rec.tier];
  const n=Object.keys(load()).length;
  const label=res.fresh?'🎴 NOVA FIGURINHA!':res.upgraded?'✨ FIGURINHA MELHORADA!':'🎴 Você já tinha esta figurinha';
  const sub=r.tries?`${r.hits} de ${r.tries} respostas de primeira`:'Episódio concluído';
  return `<div class="fg-reveal"><div class="fg-medal ${res.rec.tier}"><span class="fg-disc" aria-hidden="true">${T.ico}</span><div><b>${T.medal}</b><small>${esc(sub)}</small></div></div>
    <p class="fg-new">${label}</p><div class="fg-flip">${cardHTML(res.rec,{cls:'fg-lg'})}</div>
    <button type="button" class="fg-open" data-fig-open="${esc(P.cid)}">📚 Ver no álbum <small>${n} figurinha${n>1?'s':''}</small></button></div>`;
}
function celebrate(){
  if(!active())return false;
  if(window.PogReward&&PogReward.celebrate)return PogReward.celebrate();
  return false;
}

/* ---------- álbum ---------- */
const PAGE=24;
let AL={cid:null,cat:'all',shown:PAGE};
function courseList(){
  try{return Object.keys(COURSES).filter(id=>isRegularCourse(id)&&EP_COUNT&&EP_COUNT[id])}catch(e){return []}
}
const LANGN={en:'🇺🇸 Inglês',es:'🇪🇸 Espanhol',pt:'🇧🇷 Português',fr:'🇫🇷 Francês',frbr:'🇫🇷 Francês',zhbr:'🇨🇳 Chinês',de:'🇩🇪 Alemão',it:'🇮🇹 Italiano',ja:'🇯🇵 Japonês',ko:'🇰🇷 Coreano',enesh:'🇺🇸 Inglês (ES)'};
function courseLabel(id){
  const m=/^([a-z]+)-([a-z0-9]+)$/.exec(id)||[];
  return (LANGN[m[1]]||id)+' · '+String(m[2]||'').toUpperCase();
}
async function ensure(cid){try{if(typeof ensureLangLoaded==='function')await ensureLangLoaded(cid)}catch(e){}}
function slots(cid){
  const eps=(typeof EP!=="undefined"&&EP[cid])||[],all=load(),out=[];
  eps.forEach((e,ix)=>{
    const info=infoFromEp(e,cid);if(!info)return;info.no=ix+1;
    const done=typeof ST!=='undefined'&&ST.done&&ST.done[cid+'-'+e.n];
    const rec=all[info.key];
    if(rec){rec.no=ix+1;out.push({info:rec,got:true})}
    else if(done){out.push({info:Object.assign({},info,{tier:'bronze',acc:0}),got:true,legacy:true})}
    else out.push({info,got:false});
  });
  return out;
}
function paint(root){
  const cid=AL.cid,sl=slots(cid);
  const got=sl.filter(s=>s.got).length;
  const by=id=>sl.filter(s=>s.info.cat===id);
  const list=(AL.cat==='all'?sl:by(AL.cat));
  const pct=sl.length?Math.round(got/sl.length*100):0;
  const shown=list.slice(0,AL.shown);
  const gold=sl.filter(s=>s.got&&s.info.tier==='gold').length;
  root.querySelector('.fa-body').innerHTML=`
   <div class="fa-hero"><div class="fa-ring" role="img" aria-label="${got} de ${sl.length} figurinhas coletadas"><svg viewBox="0 0 120 120" aria-hidden="true"><circle cx="60" cy="60" r="52" fill="none" stroke="rgba(255,255,255,.14)" stroke-width="12"/><circle class="fa-arc" cx="60" cy="60" r="52" fill="none" stroke="#FFB627" stroke-width="12" stroke-linecap="round" stroke-dasharray="${(2*Math.PI*52).toFixed(1)}" stroke-dashoffset="${(2*Math.PI*52*(1-Math.max(pct,got?2:0)/100)).toFixed(1)}" transform="rotate(-90 60 60)"/></svg><div class="fa-rn"><b>${got}</b><i></i><small>${sl.length}</small></div></div>
    <div class="fa-hero-t"><h2>Álbum cultural</h2><p>Filmes, séries, músicas, livros e mais. Conclua episódios para colecionar as figurinhas das obras.</p><div class="fa-chips"><span>🎴 ${got} de ${sl.length} coletadas</span><span>🥇 ${gold} douradas</span><span>${pct}% completo</span></div></div></div>
   <label class="fa-sel"><span>Curso</span><select id="faCourse">${courseList().map(id=>`<option value="${esc(id)}" ${id===cid?'selected':''}>${esc(courseLabel(id))}</option>`).join('')}</select></label>
   <div class="fa-tabs" role="tablist"><button type="button" class="${AL.cat==='all'?'on':''}" data-cat="all">Todas <i>${got}/${sl.length}</i></button>${CATS.map(c=>{const b=by(c.id);if(!b.length)return '';return `<button type="button" class="${AL.cat===c.id?'on':''}" data-cat="${c.id}" style="--c1:${c.c1}">${c.ico} ${esc(c.name)} <i>${b.filter(s=>s.got).length}/${b.length}</i></button>`}).join('')}</div>
   <div class="fa-grid">${shown.length?shown.map((s,i)=>`<button type="button" class="fa-cell" data-i="${sl.indexOf(s)}" style="--d:${Math.min(i,12)*30}ms" aria-label="${s.got?esc(s.info.title):'Figurinha escondida'}">${cardHTML(s.info,{lock:!s.got})}</button>`).join(''):'<p class="fa-empty">Nada por aqui ainda.</p>'}</div>
   ${list.length>shown.length?`<button type="button" class="fa-more" id="faMore">Mostrar mais (${list.length-shown.length})</button>`:''}`;
  root.querySelector('#faCourse').onchange=async ev=>{AL.cid=ev.target.value;AL.cat='all';AL.shown=PAGE;await ensure(AL.cid);paint(root)};
  root.querySelectorAll('[data-cat]').forEach(b=>b.onclick=()=>{AL.cat=b.dataset.cat;AL.shown=PAGE;paint(root)});
  const more=root.querySelector('#faMore');if(more)more.onclick=()=>{AL.shown+=PAGE;paint(root)};
  root.querySelectorAll('.fa-cell').forEach(b=>b.onclick=()=>detail(root,sl[+b.dataset.i]));
}
function detail(root,s){
  if(!s)return;
  const c=CAT[s.info.cat]||CAT.history,T=TIER[s.info.tier||'bronze'];
  const m=document.createElement('div');m.className='fa-detail';
  m.innerHTML=`<div class="fa-dbox" role="dialog" aria-label="${esc(s.info.title)}"><button type="button" class="fa-x" aria-label="Fechar">✕</button>
   <div class="fg-flip show">${cardHTML(s.info,{lock:!s.got,cls:'fg-lg'})}</div>
   ${s.got?`<h3>${esc(s.info.w||s.info.title)}</h3><p class="fa-meta">${c.ico} ${esc(s.info.k?s.info.k.replace(/^[^\p{L}]+/u,''):c.name)}${s.info.y?' · '+esc(s.info.y):''} · ${T.rar}</p><p>${esc(s.info.d||'Uma referência cultural que aparece neste episódio.')}</p><button type="button" class="fa-play" data-play="${esc(s.info.cid)}|${esc(s.info.n)}">▶ Jogar o episódio${s.info.tier!=='gold'?' e melhorar a medalha':''}</button>`
     :`<h3>Figurinha escondida</h3><p class="fa-meta">${c.ico} ${esc(c.name)}${s.info.ep?' · EP '+esc(s.info.ep):''}</p><p>Conclua este episódio para revelar a figurinha${s.info.ep?'':''}.</p><button type="button" class="fa-play" data-play="${esc(s.info.cid)}|${esc(s.info.n)}">▶ Jogar este episódio</button>`}</div>`;
  m.onclick=ev=>{if(ev.target===m||ev.target.closest('.fa-x'))m.remove();const p=ev.target.closest('[data-play]');if(p){const [cid,n]=p.dataset.play.split('|');m.remove();close();playEp(cid,n)}};
  document.body.appendChild(m);
}
function playEp(cid,n){
  try{const idx=EP[cid].findIndex(e=>String(e.n)===String(n));if(idx>=0)play(cid,idx)}catch(e){}
}
function close(){const r=document.getElementById('fgAlbum');if(r)r.remove();document.body.style.overflow=(typeof P!=='undefined'&&P)?'hidden':''}
async function open(cid){
  close();
  const list=courseList();
  AL.cid=(cid&&list.includes(cid))?cid:(typeof ST!=='undefined'&&ST.lastCourse&&list.includes(ST.lastCourse)?ST.lastCourse:(list[0]||'en-a1'));
  AL.cat='all';AL.shown=PAGE;
  const root=document.createElement('div');root.id='fgAlbum';root.className='fa';root.setAttribute('role','dialog');root.setAttribute('aria-label','Álbum cultural');
  root.innerHTML='<div class="fa-bar"><button type="button" class="fa-back" aria-label="Fechar o álbum">←</button><b>🎴 Álbum cultural</b></div><div class="fa-body"><p class="fa-empty">Carregando…</p></div>';
  document.body.appendChild(root);document.body.style.overflow='hidden';
  root.querySelector('.fa-back').onclick=close;
  await ensure(AL.cid);paint(root);
}
document.addEventListener('click',ev=>{const b=ev.target.closest&&ev.target.closest('[data-fig-open]');if(b){ev.preventDefault();open(b.dataset.figOpen)}});
document.addEventListener('keydown',ev=>{if(ev.key==='Escape'){const d=document.querySelector('.fa-detail');if(d)d.remove();else if(document.getElementById('fgAlbum'))close()}});

/* atalho na página do curso */
const _course=window.course;
if(typeof _course==='function')window.course=function(id){
  const r=_course.apply(this,arguments);
  try{setTimeout(()=>{
    if(!isRegularCourse(id)||document.querySelector('.fa-btn'))return;
    const host=document.querySelector('.p2levelsw')||document.querySelector('.p2banner')||document.querySelector('.p5h')||document.querySelector('.p2lhead');if(!host)return;
    const n=Object.keys(load()).length;
    const b=document.createElement('button');b.type='button';b.className='fa-btn';b.dataset.figOpen=id;
    b.innerHTML=`<span class="fa-btn-ico">🎴</span><span><b>Álbum cultural</b><small>${n} figurinha${n===1?'':'s'} coletada${n===1?'':'s'}</small></span><i>›</i>`;
    host.insertAdjacentElement('afterend',b);
  },80)}catch(e){}
  return r;
};

/* quadro "Para levar": a figurinha só é revelada no resultado (a raridade depende do desempenho) */
const _render=window.render;
if(typeof _render==='function')window.render=function(){
  const r=_render.apply(this,arguments);
  try{
    const pl=document.getElementById('player');
    if(pl)pl.classList.toggle('fg-on',active());
    if(active()&&P.e.fr&&/^fx\d+$/.test(P.steps[P.i]||'')&&P.e.fr[+P.steps[P.i].slice(2)]&&P.e.fr[+P.steps[P.i].slice(2)].k==='wrap'){
      setTimeout(()=>{
        const host=document.querySelector('#pstage .wr-hero');if(!host||document.querySelector('#pstage .fg-teaser'))return;
        const info=infoFromEp(P.e,P.cid),c=CAT[info.cat]||CAT.history;
        host.insertAdjacentHTML('afterend',`<div class="fg-teaser" style="--c1:${c.c1};--c2:${c.c2}"><span>${c.ico}</span><div><b>Sua figurinha está quase pronta</b><small>${esc(info.title)} · a raridade aparece no resultado</small></div></div>`);
      },650);
    }
  }catch(e){}
  return r;
};

/* a cena enche a janela da carta (corta as bordas em vez de deixar faixas) */
const fitArt=root=>{(root||document).querySelectorAll('.fg .ps-stage-bk svg:not([data-fit])').forEach(v=>{v.setAttribute('preserveAspectRatio','xMidYMid slice');v.dataset.fit='1'})};
try{new MutationObserver(m=>{for(const x of m){if(x.addedNodes.length){fitArt();break}}}).observe(document.body,{childList:true,subtree:true})}catch(e){}
window.PogFig={active,revealHTML,celebrate,cardHTML,infoFromEp,categorize,open,load,CATS};
})();
