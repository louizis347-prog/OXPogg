/* Pogglot · interface moderna: barra, home, página por idioma, conquistas.
   Carregado depois do script principal; substitui topbar/home/hub e envolve profile/course. */
(function(){
'use strict';
const L0=()=>ST.homeLang==='es'?'es':'pt';
const K={
 pt:{courses:'Cursos',comm:'Comunidade',rank:'Ranking',ach:'Conquistas',me:'Perfil',login:'Entrar',review:'Revisar',
  hi:'Aprenda idiomas',hi2:'pela cultura',lead:'Filmes, livros, músicas e tradições de cada país — em lições curtas, com voz, prática e uma comunidade para conversar.',
  cont:'Continuar de onde parei',contBtn:'Continuar',choose:'Escolha um idioma',start:'Começar agora',pick:'Escolha seu idioma',pickSub:'Cada idioma tem a sua própria página, níveis e progresso.',
  streak:'dias seguidos',xp:'pontos XP',eps:'episódios',league:'liga',
  commT:'Converse com outros alunos',commP:'Troque mensagens, corrija e seja corrigido, e ache parceiros que falam o idioma que você estuda.',commB:'Abrir comunidade',
  rankT:'Ranking de alunos',rankP:'Ganhe XP, mantenha a sequência e suba de liga. Veja quem está na frente.',rankB:'Ver ranking',
  achT:'Suas conquistas',achAll:'Ver todas',eps2:'eps',progress:'Seu progresso',levels:'Níveis',arcs:'Trilha por arcos',back:'Todos os idiomas',
  yourCourse:'Seu curso',startC:'Começar curso',contC:'Continuar curso',reviewC:'Rever curso',notStarted:'Ainda não começou',
  unlocked:'Conquista desbloqueada',lockedT:'Em andamento',doneT:'Desbloqueadas',of:'de',library:'Sua biblioteca',libSub:'Livros que você adicionou ao concluir episódios.',libEmpty:'Conclua um episódio para ganhar seu primeiro livro.',
  account:'Sua conta',accIn:'Você está conectado como',out:'Sair',acc2:'Entre para aparecer no ranking e conversar com a comunidade.',signin:'Entrar ou criar conta',
  chatLang:'Sala do idioma'},
 es:{courses:'Cursos',comm:'Comunidad',rank:'Ranking',ach:'Logros',me:'Perfil',login:'Entrar',review:'Repasar',
  hi:'Aprende idiomas',hi2:'con cultura',lead:'Películas, libros, canciones y tradiciones de cada país, en lecciones cortas con voz, práctica y una comunidad para conversar.',
  cont:'Seguir donde lo dejé',contBtn:'Continuar',choose:'Elige un idioma',start:'Empezar ahora',pick:'Elige tu idioma',pickSub:'Cada idioma tiene su propia página, niveles y progreso.',
  streak:'días seguidos',xp:'puntos XP',eps:'episodios',league:'liga',
  commT:'Conversa con otros alumnos',commP:'Intercambia mensajes, corrige y recibe correcciones, y encuentra compañeros que hablan el idioma que estudias.',commB:'Abrir comunidad',
  rankT:'Ranking de alumnos',rankP:'Gana XP, mantén tu racha y sube de liga. Mira quién va al frente.',rankB:'Ver ranking',
  achT:'Tus logros',achAll:'Ver todos',eps2:'eps',progress:'Tu progreso',levels:'Niveles',arcs:'Ruta por arcos',back:'Todos los idiomas',
  yourCourse:'Tu curso',startC:'Empezar curso',contC:'Continuar curso',reviewC:'Repasar curso',notStarted:'Aún no empezaste',
  unlocked:'Logro desbloqueado',lockedT:'En progreso',doneT:'Desbloqueados',of:'de',library:'Tu biblioteca',libSub:'Libros que agregaste al terminar episodios.',libEmpty:'Termina un episodio para ganar tu primer libro.',
  account:'Tu cuenta',accIn:'Sesión iniciada como',out:'Salir',acc2:'Entra para aparecer en el ranking y conversar con la comunidad.',signin:'Entrar o crear cuenta',
  chatLang:'Sala del idioma'}
};
const k=key=>(K[L0()][key]!=null?K[L0()][key]:K.pt[key]);

/* ---------- idiomas ---------- */
const LANGS=[
 {id:'en',mono:'EN',c:'#1CB0F6',cd:'#0E86C2',cl:'#CDEFFD',n:{pt:'Inglês',es:'Inglés'},sub:['en-a1','en-a2','en-b1','en-b2','en-c1','en-c2']},
 {id:'es',mono:'ES',c:'#FF6B4A',cd:'#D44A2C',cl:'#FFD9D0',n:{pt:'Espanhol',es:'Español'},sub:['es-a1','es-a2','es-b1','es-b2','es-c1','es-c2']},
 {id:'fr',mono:'FR',c:'#7B61FF',cd:'#5A41D9',cl:'#DDD6FF',n:{pt:'Francês',es:'Francés'},sub:['fr']},
 {id:'de',mono:'DE',c:'#F5A400',cd:'#C28000',cl:'#FFEBB8',n:{pt:'Alemão',es:'Alemán'},sub:['de']},
 {id:'it',mono:'IT',c:'#F0508B',cd:'#C73068',cl:'#FFD5E4',n:{pt:'Italiano',es:'Italiano'},sub:['it']},
 {id:'enes',mono:'EN',c:'#2E9E6A',cd:'#1F7A4F',cl:'#D2F2E0',n:{pt:'Inglês p/ hispanofalantes',es:'Inglés para hispanohablantes'},sub:['enes-a1']},
 {id:'nb',mono:'NB',c:'#E0703A',cd:'#B5521F',cl:'#FFE0CE',n:{pt:'Neighbors · Inglês',es:'Neighbors · Inglés'},sub:['nb-a1','nb-a2','nb-b1','nb-b2','nb-c1','nb-c2']},
 {id:'nbes',mono:'NB',c:'#D9467A',cd:'#A82D5C',cl:'#FFDCE8',n:{pt:'Neighbors · Espanhol',es:'Neighbors · Español'},sub:['nbes-a1']},
 {id:'nbfr',mono:'NB',c:'#2F6BE8',cd:'#1F4DB8',cl:'#D7E3FF',n:{pt:'Neighbors · Francês',es:'Neighbors · Francés'},sub:['nbfr-a1']},
 {id:'pt',mono:'PT',c:'#3FBF3F',cd:'#2A962A',cl:'#D2F2D2',n:{pt:'Português',es:'Portugués'},sub:['pt']}
];
const LANG=id=>LANGS.find(l=>l.id===id)||LANGS[0];
const langOfCourse=cid=>{const c=COURSES[cid];return (c&&(c.group||c.id))||cid.split('-')[0]};
const lstyle=l=>`--c:${l.c};--cd:${l.cd};--cl:${l.cl}`;
const langInfo=l=>{const L=L0();let n=0,d=0;l.sub.forEach(cid=>{n+=EP_COUNT[cid]||0;d+=doneCountFor(cid)});
  const g=GROUPS[l.id]||COURSES[l.id];return{n,d,pct:n?d/n:0,name:l.n[L],tag:g.flag,desc:g.desc[L],scene:g.scene};};
const esc2=s=>String(s==null?'':s).replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]));

/* ---------- ícones ---------- */
const IC={
 home:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l9-8 9 8"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/></svg>',
 comm:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a8 8 0 01-11.6 7.1L4 20l1-4.6A8 8 0 1121 12z"/><path d="M8.5 11h7M8.5 14h4"/></svg>',
 rank:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 21h8M12 17v4"/><path d="M7 4h10v6a5 5 0 01-10 0V4z"/><path d="M7 6H4v2a3 3 0 003 3M17 6h3v2a3 3 0 01-3 3"/></svg>',
 ach:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="9" r="6"/><path d="M8.5 14L7 22l5-3 5 3-1.5-8"/></svg>',
 me:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4 21c1-4 4-6 8-6s7 2 8 6"/></svg>'
};
const TABS=[['home','courses','home'],['comm','comm','comm'],['rank','rank','rank'],['ach','ach','ach'],['profile','me','me']];

/* ---------- ligas ---------- */
const LEAGUES=[[0,'Bronze','#C98A4B'],[500,'Prata','#8E9BB0'],[2000,'Ouro','#E9A800'],[5000,'Safira','#2F8FE0'],[10000,'Diamante','#12B5BC']];
function league(xp){let r=LEAGUES[0];for(const l of LEAGUES)if(xp>=l[0])r=l;return{name:r[1],color:r[2],min:r[0]}}

/* ---------- conquistas ---------- */
const A=(id,ic,pt,es,dpt,des,goal,cur)=>({id,ic,n:{pt,es},d:{pt:dpt,es:des},goal,cur});
const ACH=[
 A('ep1','🌱','Primeiro passo','Primer paso','Conclua seu primeiro episódio.','Termina tu primer episodio.',1,s=>s.eps),
 A('ep10','📚','Pegando o jeito','Agarrando el ritmo','Conclua 10 episódios.','Termina 10 episodios.',10,s=>s.eps),
 A('ep50','🏅','Meio centenário','Medio centenar','Conclua 50 episódios.','Termina 50 episodios.',50,s=>s.eps),
 A('ep100','🎓','Centenário','Centenario','Conclua 100 episódios.','Termina 100 episodios.',100,s=>s.eps),
 A('ep250','🏆','Maratonista','Maratonista','Conclua 250 episódios.','Termina 250 episodios.',250,s=>s.eps),
 A('ep500','👑','Lenda da cultura','Leyenda cultural','Conclua 500 episódios.','Termina 500 episodios.',500,s=>s.eps),
 A('st3','🔥','Esquentando','Calentando','3 dias seguidos.','3 días seguidos.',3,s=>s.streak),
 A('st7','⚡','Semana de fogo','Semana de fuego','7 dias seguidos.','7 días seguidos.',7,s=>s.streak),
 A('st30','🌋','Hábito de ferro','Hábito de hierro','30 dias seguidos.','30 días seguidos.',30,s=>s.streak),
 A('xp100','✨','Faísca','Chispa','Some 100 XP.','Suma 100 XP.',100,s=>s.xp),
 A('xp1000','💎','Mil de XP','Mil de XP','Some 1.000 XP.','Suma 1.000 XP.',1000,s=>s.xp),
 A('xp5000','🚀','Foguete','Cohete','Some 5.000 XP.','Suma 5.000 XP.',5000,s=>s.xp),
 A('lg2','🌍','Dois mundos','Dos mundos','Estude 2 idiomas.','Estudia 2 idiomas.',2,s=>s.langs),
 A('lg4','🗺️','Viajante','Viajero','Estude 4 idiomas.','Estudia 4 idiomas.',4,s=>s.langs),
 A('lg6','🪐','Poliglota','Políglota','Estude os 6 idiomas.','Estudia los 6 idiomas.',6,s=>s.langs),
 A('en10','🗽','Americano de coração','Americano de corazón','10 episódios de inglês.','10 episodios de inglés.',10,s=>s.by.en||0),
 A('es10','💃','Hola, amigo!','¡Hola, amigo!','10 episódios de espanhol.','10 episodios de español.',10,s=>s.by.es||0),
 A('fr10','🥐','Bonjour!','¡Bonjour!','10 episódios de francês.','10 episodios de francés.',10,s=>s.by.fr||0),
 A('de10','🥨','Guten Tag!','¡Guten Tag!','10 episódios de alemão.','10 episodios de alemán.',10,s=>s.by.de||0),
 A('it10','🍝','Ciao, bella!','¡Ciao, bella!','10 episódios de italiano.','10 episodios de italiano.',10,s=>s.by.it||0),
 A('pt10','🌴','Olá, amigo!','¡Olá, amigo!','10 episódios de português.','10 episodios de portugués.',10,s=>s.by.pt||0),
 A('cc','🏁','Curso completo','Curso completo','Termine todos os episódios de um curso.','Termina todos los episodios de un curso.',1,s=>s.coursesDone),
 A('bk1','📖','Leitor','Lector','Adicione seu primeiro livro.','Agrega tu primer libro.',1,s=>s.shelf),
 A('bk10','🏛️','Biblioteca viva','Biblioteca viva','Reúna 10 livros.','Reúne 10 libros.',10,s=>s.shelf),
 A('sr50','🔁','Memória de elefante','Memoria de elefante','50 cartões de revisão.','50 tarjetas de repaso.',50,s=>s.srs),
 A('ac90','🎯','Na mosca','En el blanco','90% de acertos (mín. 100 respostas).','90% de aciertos (mín. 100 respuestas).',90,s=>s.answered>=100?s.acc:0),
 A('mb','🎫','Membro','Miembro','Crie sua conta na comunidade.','Crea tu cuenta en la comunidad.',1,s=>s.member?1:0),
 A('m1','💬','Quebra-gelo','Rompehielo','Envie sua primeira mensagem.','Envía tu primer mensaje.',1,s=>s.msgs),
 A('m50','🗣️','Papo firme','Charla firme','Envie 50 mensagens.','Envía 50 mensajes.',50,s=>s.msgs),
 A('fx1','✏️','Professor honorário','Profesor honorario','Corrija uma mensagem de outro aluno.','Corrige un mensaje de otro alumno.',1,s=>s.fixes)
];
function stats(){
  const by={};let eps=0;
  for(const key in ST.done){if(!ST.done[key])continue;const l=langOfCourse(key.replace(/-\d+$/,''));by[l]=(by[l]||0)+1;eps++}
  const mx=Math.max(ST.streak.n||0,store.get('maxStreak',0));
  if(mx>store.get('maxStreak',0))store.set('maxStreak',mx);
  let cd=0;for(const cid in COURSES){const n=EP_COUNT[cid]||0;if(n&&doneCountFor(cid)>=n)cd++}
  const c=store.get('comm',{msgs:0,fixes:0});
  return{xp:ST.xp||0,streak:mx,eps,by,langs:Object.keys(by).length,coursesDone:cd,shelf:ST.shelf.length,srs:Object.keys(ST.srs||{}).length,
    acc:ST.totalAnswered?Math.round(ST.totalCorrect/ST.totalAnswered*100):0,answered:ST.totalAnswered||0,
    msgs:c.msgs||0,fixes:c.fixes||0,member:!!(window.PogCloud&&PogCloud.user&&PogCloud.user())};
}
let achBusy=false;
function checkAch(silent){
  const s=stats(),got=store.get('ach',{});const fresh=[];
  for(const a of ACH){if(!got[a.id]&&a.cur(s)>=a.goal){got[a.id]=Date.now();fresh.push(a)}}
  if(fresh.length){store.set('ach',got);if(!silent)fresh.forEach((a,i)=>setTimeout(()=>toast(a),i*2600));}
  return s;
}
function toast(a){
  const L=L0(),d=document.createElement('div');d.className='pg-toast';d.setAttribute('role','status');
  d.innerHTML=`<span class="ic">${a.ic}</span><div><small>${k('unlocked')}</small>${esc2(a.n[L])}</div>`;
  document.body.appendChild(d);requestAnimationFrame(()=>d.classList.add('show'));
  try{if(typeof confetti==='function')confetti(70)}catch(e){}
  setTimeout(()=>{d.classList.remove('show');setTimeout(()=>d.remove(),600)},2600);
}
function pushNow(){
  try{if(window.PogCloud&&PogCloud.user()){const s=stats();PogCloud.pushStats({xp:s.xp,streak:s.streak,eps:s.by,ach:store.get('ach',{})}).catch(()=>{})}}catch(e){}
}
let t0=0;
function afterSave(){clearTimeout(t0);t0=setTimeout(()=>{try{checkAch();pushNow();syncStatChips()}catch(e){console.warn(e)}},350)}
function syncStatChips(){const s=stats();document.querySelectorAll('[data-pgxp]').forEach(e=>e.textContent=s.xp);document.querySelectorAll('[data-pgstreak]').forEach(e=>e.textContent=ST.streak.n)}
{const _save=window.save;window.save=function(){const r=_save.apply(this,arguments);afterSave();return r}}

/* ---------- barra e navegação ---------- */
function me(){return window.PogCloud&&PogCloud.user?PogCloud.user():null}
window.topbar=function(L){
  const u=me(),cur=PogUI.cur;
  return `<header class="pgbar"><div class="in">
   <button class="logo" data-go="home" aria-label="Pogglot"><span class="mini">${poggie({scarf:'#7C4DFF'})}</span><span>Pogg<b>lot</b></span></button>
   <nav class="pgtabs" aria-label="Menu">${TABS.filter(t=>t[0]!=='profile').map(([id,key,ic])=>`<button data-go="${id}" ${cur===id?'aria-current="page"':''}>${IC[ic]}${k(key)}</button>`).join('')}</nav>
   <div class="pgright">
    <span class="pgstat fire" title="${k('streak')}">🔥 <span data-pgstreak>${ST.streak.n}</span></span>
    <span class="pgstat xp hide-s" title="XP">⚡ <span data-pgxp>${ST.xp}</span></span>
    <button class="pgstat rev hide-s" data-go="review" title="${k('review')}">🔁 ${srsDueCount()||''}</button>
    ${u?`<button class="pgme" data-go="profile" title="${esc2(u.name)}"><span class="av">${esc2(u.avatar||'🙂')}</span><span class="nm">${esc2((u.name||'').split(' ')[0])}</span></button>`
       :`<button class="pgme guest" data-go="auth">${k('login')}</button>`}
    <div class="pglang" role="group" aria-label="Idioma"><button data-hl="pt" aria-pressed="${ST.homeLang!=='es'}">PT</button><button data-hl="es" aria-pressed="${ST.homeLang==='es'}">ES</button></div>
   </div></div></header>`;
};
function mountNav(){
  let n=document.getElementById('pgnav');
  if(!n){n=document.createElement('nav');n.id='pgnav';n.className='pgnav';n.setAttribute('aria-label','Menu');document.body.appendChild(n);document.body.classList.add('pg-has-nav')}
  n.innerHTML=TABS.map(([id,key,ic])=>`<button data-go="${id}" ${PogUI.cur===id?'aria-current="page"':''}>${IC[ic]}<span>${k(key)}</span></button>`).join('');
}
new MutationObserver(()=>document.body.classList.toggle('pg-playing',!!document.getElementById('player'))).observe(document.body,{childList:true});

/* ---------- roteamento por hash ---------- */
let routing=false;
function setHash(h){if(routing)return;try{if(location.hash!==h)history.pushState(null,'',h)}catch(e){}}
function route(h){
  routing=true;
  try{
    const p=(h||'').replace(/^#\/?/,'').split('/');
    if(p[0]==='lang'&&LANGS.some(l=>l.id===p[1]))hub(p[1]);
    else if(p[0]==='course'&&COURSES[p[1]])navLoading(()=>ensureLangLoaded(p[1]).then(()=>course(p[1])));
    else if(p[0]==='comm')PogUI.go(p[1]==='partners'?'comm:partners':'comm');
    else if(p[0]==='rank')PogUI.go('rank');
    else if(p[0]==='ach')PogUI.go('ach');
    else if(p[0]==='profile')PogUI.go('profile');
    else if(p[0]==='episodes')PogUI.go('episodes');
    else if(p[0]==='shelf')PogUI.go('shelf');
    else if(p[0]==='courses')PogUI.go('courses');
    else home();
  }finally{routing=false}
}
const playing=()=>{try{return !!P}catch(e){return false}};
window.addEventListener('popstate',()=>{if(playing())return;route(location.hash)});

/* ---------- home ---------- */
const BUBS=[['EN',8,10],['ES',78,4],['FR',90,52],['DE',70,88],['IT',6,74],['PT',-2,42]];
window.home=function(){
  PogUI.cur='home';setHash('#/');
  const L=L0(),res=resumeTarget(),u=me();
  const doneEp=Object.values(COURSES).reduce((s,c)=>s+doneCountFor(c.id),0),s=stats(),lg=league(s.xp);
  const got=store.get('ach',{});
  const next=ACH.filter(a=>!got[a.id]).sort((a,b)=>b.cur(s)/b.goal-a.cur(s)/a.goal).slice(0,6);
  const show=next.length?next:ACH.slice(0,6);
  app.innerHTML=topbar(L)+`<main class="pg">
  <section class="pg-hero"><div>
    <h1>${k('hi')} <em>${k('hi2')}</em></h1><p class="lead">${k('lead')}</p>
    ${res?`<div class="pg-resume"><span style="font-size:26px">▶️</span><div><small>${k('cont')}</small><b>${esc2(COURSES[res.cid].name[L])} · ${esc2(res.e.t)}</b></div></div>
    <div class="cta-row"><button class="pg-btn" data-ep="${res.cid}:${res.idx}">${k('contBtn')}</button><button class="pg-btn alt" data-go="ach">🏆 ${k('ach')}</button></div>`
    :`<div class="cta-row"><button class="pg-btn" data-lang="en">${k('start')}</button><button class="pg-btn alt" data-go="comm">💬 ${k('comm')}</button></div>`}
  </div>
  <div class="pg-orbit"><div class="blob"></div><div class="pgm">${poggie({cls:'',scarf:'#FFE58A'})}</div>
   ${BUBS.map(([m,x,y],i)=>{const l=LANG(m.toLowerCase());return `<span class="pg-bub" style="${lstyle(l)};left:${x}%;top:${y}%;animation-delay:-${i*.8}s">${monoFlag(m)}</span>`}).join('')}</div></section>
  <section class="pg-stats" aria-label="Resumo">
   <div class="pg-stat" style="--tint:#FFF0E2"><span class="ic">🔥</span><div><b data-pgstreak>${ST.streak.n}</b><small>${k('streak')}</small></div></div>
   <div class="pg-stat" style="--tint:#F0EAFF"><span class="ic">⚡</span><div><b data-pgxp>${ST.xp}</b><small>${k('xp')}</small></div></div>
   <div class="pg-stat" style="--tint:#E1F7EA"><span class="ic">📚</span><div><b>${doneEp}</b><small>${k('eps')}</small></div></div>
   <div class="pg-stat" style="--tint:${lg.color}33"><span class="ic">🛡️</span><div><b style="color:${lg.color}">${lg.name}</b><small>${k('league')}</small></div></div>
  </section>
  ${srsBanner()}
  <div class="pg-sec"><div><h2>${k('pick')}</h2><p>${k('pickSub')}</p></div></div>
  <section class="pg-langs">${LANGS.map((l,i)=>{const I=langInfo(l);return `<button class="pg-lang" data-lang="${l.id}" style="${lstyle(l)};animation:rise .5s ${i*.06}s both">
    <div class="art">${SC.get(I.scene)}<span class="tagc">${flagPair(I.tag)}</span></div><span class="mono">${monoFlag(l.mono)}</span>
    <div class="bd"><h3>${esc2(I.name)}</h3><p>${esc2(I.desc)}</p>
    <div class="ft"><div class="bar"><i style="width:${(I.pct*100).toFixed(1)}%"></i></div><span>${I.d}/${I.n} ${k('eps2')}</span></div></div></button>`}).join('')}</section>
  <div class="pg-sec"><div><h2>${k('comm')}</h2></div></div>
  <section class="pg-comm">
   <div class="pg-card pg-tease chat"><h3>💬 ${k('commT')}</h3><p>${k('commP')}</p><div class="pg-av-row"><span>🧑‍🎤</span><span>👩‍💻</span><span>🧑‍🏫</span><span>🧑‍🍳</span><span>👨‍🎨</span></div><div><button class="pg-btn" data-go="comm">${k('commB')}</button></div></div>
   <div class="pg-card pg-tease rank"><h3>🏆 ${k('rankT')}</h3><p>${k('rankP')}</p><div class="pg-av-row"><span>🥇</span><span>🥈</span><span>🥉</span></div><div><button class="pg-btn" data-go="rank" style="--c:#F5A400;--cd:#C28000">${k('rankB')}</button></div></div>
  </section>
  <div class="pg-sec"><div><h2>${k('achT')}</h2></div><button class="pg-btn ghost sm" data-go="ach">${k('achAll')}</button></div>
  <div class="pg-ach-row">${show.map(a=>`<div class="pg-ach-mini ${got[a.id]?'':'lock'}"><div class="ic">${a.ic}</div><b>${esc2(a.n[L])}</b><small>${got[a.id]?'✓':Math.min(a.cur(s),a.goal)+'/'+a.goal}</small></div>`).join('')}</div>
  </main>`;
  mountNav();scrollTo(0,0);
};

/* ---------- página de um idioma ---------- */
window.hub=function(id){
  const l=LANG(id),L=L0();
  navLoading(()=>Promise.all(l.sub.map(ensureLangLoaded))).then(()=>{
    PogUI.cur='home';setHash('#/lang/'+l.id);
    const I=langInfo(l),RING=2*Math.PI*40;
    // próximo episódio
    let tgt=null;for(const cid of l.sub){const eps=EP[cid]||[];const nx=eps.find(e=>!ST.done[cid+'-'+e.n]&&!e.pl);if(nx){tgt={cid,idx:eps.indexOf(nx)};break}}
    const started=I.d>0;
    app.innerHTML=topbar(L)+`<main class="pg" style="${lstyle(l)}">
    <button class="pg-back" data-go="home">← ${k('back')}</button>
    <section class="pg-lhero"><div class="scene">${SC.get(I.scene)}</div>
     <div class="ring"><svg width="92" height="92" viewBox="0 0 92 92"><circle cx="46" cy="46" r="40" fill="none" stroke="rgba(255,255,255,.25)" stroke-width="8"/><circle cx="46" cy="46" r="40" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round" stroke-dasharray="${RING}" stroke-dashoffset="${RING*(1-I.pct)}"/></svg><span>${Math.round(I.pct*100)}%</span></div>
     <div class="ov"><span class="tag">${flagPair(I.tag)}</span><h1>${esc2(I.name)}</h1><p>${esc2(I.desc)}</p>
      <div class="row">${tgt?`<button class="pg-btn" data-ep="${tgt.cid}:${tgt.idx}">${started?k('contC'):k('startC')}</button>`:''}<button class="pg-btn alt" data-room="${l.id}">💬 ${k('chatLang')}</button></div></div></section>
    ${l.sub.length>1?`<div class="pg-sec"><div><h2>${k('levels')}</h2><p>${I.d}/${I.n} ${k('eps2')}</p></div></div>
     <section class="pg-levels">${l.sub.map((cid,i)=>{const c=COURSES[cid],n=EP_COUNT[cid]||0,d=doneCountFor(cid),lv=cid.split('-')[1].toUpperCase();
       return `<button class="pg-level" data-course="${cid}" style="animation:rise .5s ${i*.06}s both"><div class="top"><span class="mono">${lv}</span><div><h3>${esc2(c.name[L].replace(/^Curso de Inglês Americano para Brasileiros /,'Inglês ').replace(/^Inglés americano /,'Inglés '))}</h3></div></div>
        <p>${esc2(c.desc[L])}</p><div class="bar"><i style="width:${n?d/n*100:0}%"></i></div><div class="ft"><span>${d}/${n} ${k('eps2')}</span><span>${d?k('contC'):k('startC')} →</span></div></button>`}).join('')}</section>`
    :arcsHTML(l.sub[0],L)}
    ${l.sub.length>1?arcExplorer(l.sub,L,tgt):''}
    </main>`;
    mountNav();scrollTo(0,0);mountArcs();
  });
};
function monoFlag(m){const M={EN:'us',ES:'es',FR:'fr',DE:'de',IT:'it',PT:'br'};const c=M[String(m).toUpperCase()];return c&&typeof fxIcon==='function'?fxIcon('flag:'+c,34):m}
function arcsHTML(cid,L){
  const head=`<div class="pg-sec"><div><h2>${k('yourCourse')}</h2></div></div><section class="pg-levels" style="grid-template-columns:minmax(0,1fr)"><button class="pg-level" data-course="${cid}"><div class="top"><span class="mono">${monoFlag(LANG(langOfCourse(cid)).mono)}</span><div><h3>${esc2(COURSES[cid].name[L])}</h3></div></div><p>${esc2(COURSES[cid].desc[L])}</p><div class="bar"><i style="width:${(EP_COUNT[cid]?doneCountFor(cid)/EP_COUNT[cid]*100:0)}%"></i></div><div class="ft"><span>${doneCountFor(cid)}/${EP_COUNT[cid]||0} ${k('eps2')}</span><span>${doneCountFor(cid)?k('contC'):k('startC')} →</span></div></button></section>`;
  return head+arcExplorer([cid],L);
}
/* explorador de arcos: abre o arco e entra direto em qualquer episódio, sem passar pela trilha */
function arcExplorer(subs,L,tgt){
  const first=(subs.find(c=>(EP[c]||[]).some(e=>!ST.done[c+'-'+e.n]&&!e.pl))||subs[0]);
  const cur=(tgt&&tgt.cid)||first;
  const chips=subs.length>1?`<div class="pg-lv-chips">${subs.map(c=>`<button class="pg-chip ${c===cur?'on':''}" data-arclv="${c}">${c.split('-')[1].toUpperCase()}</button>`).join('')}</div>`:'';
  return `<div class="pg-sec"><div><h2>${k('arcs')}</h2><p>${L==='es'?'Toca un arco y entra directo en cualquier episodio.':'Toque num arco e entre direto em qualquer episódio.'}</p></div></div>${chips}<section class="pg-arcs" id="pgarcs" data-subs="${subs.join(',')}" data-cur="${cur}"></section>`;
}
/* arco por posição na trilha (a ordem vem de e.o; e.n não é sequencial) */
function arcPos(eps,arcs,i){const st=x=>{const k=eps.findIndex(e=>e.n===arcs[x][0]);return k};const s=st(i);if(s<0)return[];const nx=i+1<arcs.length?st(i+1):-1;return eps.slice(s,nx<0?eps.length:nx)}
function drawArcs(cid){
  const host=document.getElementById('pgarcs');if(!host)return;host.dataset.cur=cid;
  const L=L0(),arcs=ARCS[cid]||[],eps=(EP[cid]||[]).filter(e=>!e.pl);
  const nx=eps.find(e=>!ST.done[cid+'-'+e.n]);
  const rows=arcs.map((a,i)=>{const lo=a[0];const inA=arcPos(eps,arcs,i),d=inA.filter(e=>ST.done[cid+'-'+e.n]).length;
    if(!inA.length)return '';const open=nx&&inA.includes(nx);
    return `<div class="pg-arcw ${open?'open':''}" data-lo="${lo}"><button class="pg-arc ${d&&d===inA.length?'done':''}" data-arc="${lo}" aria-expanded="${!!open}"><span class="n">${d&&d===inA.length?'✓':i+1}</span><div><b>${esc2(String(a[1]).replace(/^Arco\s+[A-C][12]·\d+\s*·\s*/,''))}</b><div class="bar"><i style="width:${d/inA.length*100}%"></i></div></div><span class="pc">${d}/${inA.length}</span><span class="chev">›</span></button><div class="pg-arc-eps">${open?arcEps(cid,inA):''}</div></div>`}).join('');
  host.innerHTML=rows||'';
  const o=host.querySelector('.pg-arcw.open');if(o&&!host.dataset.scrolled){host.dataset.scrolled=1}
}
function arcEps(cid,list){
  const all=EP[cid]||[];
  return list.map(e=>{const idx=all.indexOf(e),done=!!ST.done[cid+'-'+e.n];
    return `<button class="pg-aep ${done?'done':''}" data-ep="${cid}:${idx}"><span class="num">${done?'✓':(e.en||idx+1)}</span><span class="t"><b>${esc2(e.t)}</b>${e.a&&e.a.w&&e.a.w!==e.t?`<small>${esc2(e.a.w)}</small>`:''}</span><span class="go">▶</span></button>`}).join('');
}
function mountArcs(){
  const host=document.getElementById('pgarcs');if(!host)return;
  drawArcs(host.dataset.cur);
  const sec=host.previousElementSibling;
  const ch=host.parentNode.querySelector('.pg-lv-chips');
  if(ch)ch.onclick=ev=>{const b=ev.target.closest('[data-arclv]');if(!b)return;ch.querySelectorAll('.pg-chip').forEach(x=>x.classList.toggle('on',x===b));drawArcs(b.dataset.arclv)};
  host.onclick=ev=>{
    const h=ev.target.closest('[data-arc]');if(!h)return;
    const w=h.parentNode,cid=host.dataset.cur,lo=+h.dataset.arc;
    const opening=!w.classList.contains('open');w.classList.toggle('open',opening);h.setAttribute('aria-expanded',opening);
    const box=w.querySelector('.pg-arc-eps');
    if(opening&&!box.innerHTML){const arcs=ARCS[cid]||[],i=arcs.findIndex(a=>a[0]===lo);box.innerHTML=arcEps(cid,arcPos((EP[cid]||[]).filter(e=>!e.pl),arcs,i))}
  };
}

/* ---------- conquistas ---------- */
function achPage(){
  PogUI.cur='ach';setHash('#/ach');const L=L0(),s=checkAch(true),got=store.get('ach',{});
  const done=ACH.filter(a=>got[a.id]),todo=ACH.filter(a=>!got[a.id]);
  const card=a=>{const c=Math.min(a.cur(s),a.goal),on=!!got[a.id];
    return `<div class="pg-card pg-ach ${on?'':'lock'}"><div class="ic">${a.ic}</div><b>${esc2(a.n[L])}</b><small>${esc2(a.d[L])}</small>${on?`<span class="when">✓ ${new Date(got[a.id]).toLocaleDateString(L==='es'?'es':'pt-BR')}</span>`:`<div class="prog"><i style="width:${c/a.goal*100}%"></i></div><small>${c}/${a.goal}</small>`}</div>`};
  app.innerHTML=topbar(L)+`<main class="pg"><div class="pg-sec" style="margin-top:6px"><div><h2>🏆 ${k('ach')}</h2><p>${done.length} ${k('of')} ${ACH.length}</p></div></div>
   ${me()?'':`<div class="pg-demo">ℹ️ ${k('acc2')} <button class="pg-btn sm" data-go="auth" style="margin-left:auto">${k('login')}</button></div>`}
   ${done.length?`<h3 style="margin:18px 0 10px">${k('doneT')}</h3><div class="pg-ach-grid">${done.map(card).join('')}</div>`:''}
   <h3 style="margin:22px 0 10px">${k('lockedT')}</h3><div class="pg-ach-grid">${todo.map(card).join('')}</div></main>`;
  mountNav();scrollTo(0,0);
}

/* ---------- perfil / curso envolvendo telas antigas ---------- */
{const _profile=window.profile;window.profile=function(){
  PogUI.cur='profile';setHash('#/profile');_profile.apply(this,arguments);
  const L=L0(),u=me(),main=document.querySelector('#app main.wrap');
  if(main){
    main.insertAdjacentHTML('beforeend',`<div class="sec-h"><h2>${k('account')}</h2></div><section class="pg-card" style="padding:18px;display:flex;gap:14px;align-items:center;flex-wrap:wrap">
      ${u?`<span style="font-size:38px">${esc2(u.avatar||'🙂')}</span><div style="flex:1;min-width:160px"><small style="color:var(--pg-mute);font-weight:700">${k('accIn')}</small><b style="display:block;font-size:18px">${esc2(u.name)}</b><small style="color:var(--pg-mute)">${esc2(u.email||'')}</small></div><button class="pg-btn ghost sm" data-go="logout">${k('out')}</button>`
         :`<div style="flex:1;min-width:200px;font-weight:700">${k('acc2')}</div><button class="pg-btn" data-go="auth">${k('signin')}</button>`}</section>
      <div class="sec-h"><h2>${k('library')}</h2><p>${k('libSub')}</p></div>
      <div class="pg-shelf">${ST.shelf.length?ST.shelf.map(b=>`<div class="spine" style="background:${b.c};height:${96+(b.w.length%4)*10}px" title="${esc2(b.w)} — ${esc2(b.au||'')}">${esc2(b.w)}</div>`).join(''):`<span class="empty">${k('libEmpty')}</span>`}</div>`);
  }
  mountNav();};}
{const _course=window.course;window.course=function(id){PogUI.cur='home';setHash('#/course/'+id);_course.apply(this,arguments);mountNav();try{const sv=document.querySelector('.course-top svg.scene');if(sv)sv.setAttribute('preserveAspectRatio','xMidYMid slice')}catch(e){}};}

/* ---------- API pública ---------- */
const PogUI=window.PogUI={cur:'home',K,k,L0,LANGS,LANG,ACH,stats,league,checkAch,toast,achPage,mountNav,esc:esc2,IC,setHash,
  bump(key){const c=store.get('comm',{msgs:0,fixes:0});c[key]=(c[key]||0)+1;store.set('comm',c);afterSave()},
  syncNow(){checkAch();pushNow()},
  refresh(){const h=location.hash||'';route(h)},
  start(){checkAch(true);if(location.hash&&location.hash!=='#/'&&location.hash!=='#')route(location.hash);},
  go(name){
    const [a,b]=String(name).split(':');
    if(a==='home')return home(),true;
    if(a==='ach')return achPage(),true;
    if(a==='comm'){if(window.PogComm)PogComm.open(b||'chat');return true}
    if(a==='rank'){if(window.PogComm)PogComm.open('rank');return true}
    if(a==='auth'){if(window.PogComm)PogComm.open('auth');return true}
    if(a==='logout'){if(window.PogCloud)PogCloud.signOut().then(()=>PogUI.refresh());return true}
    return false;
  }};

document.addEventListener('click',ev=>{
  if(playing())return;
  const lb=ev.target.closest('[data-lang]');if(lb){hub(lb.dataset.lang);return}
  const rb=ev.target.closest('[data-room]');if(rb){if(window.PogComm)PogComm.open('chat',rb.dataset.room);return}
  const g=ev.target.closest('[data-go]');
  if(g&&!['home','review','profile'].includes(g.dataset.go))PogUI.go(g.dataset.go);
});
})();
