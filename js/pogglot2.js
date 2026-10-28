/* Pogglot · design 2: início, cursos, Episódios, Estante, Painel do estudante.
   Carrega por último e substitui topbar/home/hub/course/profile e o roteador interno do PogUI.
   O player, as lições e os dados continuam os mesmos. */
(function(){
'use strict';
const PU=()=>window.PogUI,PC=()=>window.PogCover;
const L0=()=>ST.homeLang==='es'?'es':'pt';
const E=s=>String(s==null?'':s).replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]));
const me=()=>{try{return window.PogCloud&&PogCloud.user?PogCloud.user():null}catch(e){return null}};
const norm=s=>String(s==null?'':s).normalize('NFD').replace(/[̀-ͯ]/g,'').toLowerCase();
const nf=n=>Number(n||0).toLocaleString(L0()==='es'?'es':'pt-BR');

/* ---------- textos ---------- */
const TX={
 pt:{shMy:'Minha estante',shSort1:'Recentes',shSort2:'A–Z',shSearch:'Buscar obra ou autor',shMile:'Próxima meta',shAuth:'autores',shWorks:'obras',shQueue:'Na fila para entrar na estante',shEmptyT:'Sua estante está vazia',shEmptyP:'Conclua um episódio e a obra que você conheceu ganha seu lugar aqui.',shGo:'Começar um curso',shNone:'Nenhuma obra encontrada.',shClose:'Fechar',shBy:'de',
  cefrT:'Do A1 ao C2',cefrSub:'Os seis níveis do Quadro Europeu (MCER). No espanhol, também alinhado ao DELE.',
  l1:'Iniciante',l2:'Básico',l3:'Intermediário',l4:'Avançado inicial',l5:'Avançado',l6:'Domínio',
  commHd:'Estude acompanhado',achHd:'Conquistas',seeAll:'Ver tudo',openComm:'Abrir comunidade',openRank:'Ver ranking',
  commTx:'Converse com outros alunos, corrija e seja corrigido, e ache parceiros que falam o idioma que você estuda.',rankTx:'Ganhe XP, mantenha a sequência e suba de liga.',
  heroPill:'Episódios de 10 minutos',viewCourses:'Ver cursos',
  navCourses:'Cursos',coursesPage:'Todos os cursos',coursesPageSub:'Escolha um curso e abra a sua página: níveis, trilha e episódios.',
  nbSec:'Neighbors',nbSecSub:'Conversação, personagens e situações reais — uma série para aprender falando.',
  clSec:'Cursos Regulares',clSecSub:'Trilhas estruturadas do A1 ao C2, com cultura, gramática, leitura e preparação para exames.',
  howT:'Como funciona',howSub:'Cada episódio dura cerca de 10 minutos e segue quatro passos.',
  h1t:'Cena real',h1d:'Você ouve um diálogo curto, de uma situação de verdade, com legenda e tradução.',
  h2t:'Vocabulário',h2d:'Seis palavras-chave por episódio, com som, imagem e dica de pronúncia.',
  h3t:'Prática',h3d:'Quadros e mini-jogos para fixar o que ouviu, sem decorar regras.',
  h4t:'Voz',h4d:'Você fala em voz alta e recebe retorno sobre a sua pronúncia.',
  metT:'Nossa metodologia',metSub:'Fala primeiro. A gramática aparece pelo uso, não por tabelas.',
  me1t:'Fala primeiro',me1d:'Você começa ouvindo e falando situações reais; a gramática vem depois, pelo uso.',
  me2t:'Cultura de verdade',me2d:'Cada episódio parte de uma obra, um país ou uma tradição, para dar contexto e memória.',
  me3t:'Alinhado ao MCER',me3d:'Níveis A1 a C2 do Quadro Europeu. O espanhol também segue o DELE do Instituto Cervantes.',
  me4t:'Revisão espaçada',me4d:'As palavras voltam na hora certa para ficarem na memória de longo prazo.',
  fnT:'O que há no Pogglot',fnSub:'Tudo o que você usa para estudar, em um só lugar.',
  f1t:'Voz e pronúncia',f1d:'Áudio nativo em cada fala e prática de fala com correção.',
  f2t:'Quadros e jogos',f2d:'Portas, balões, pesca, memória e muito mais para praticar de forma leve.',
  f3t:'Revisão espaçada',f3d:'Cartões de vocabulário prontos para rever no momento certo.',
  f4t:'Trilha e metas',f4d:'Meta diária de XP, trilha do dia e mini-testes por arco.',
  f5t:'Conquistas e ligas',f5d:'Ganhe XP, mantenha a sequência e suba de liga.',
  f6t:'Comunidade',f6d:'Converse com outros alunos, corrija e seja corrigido, ache parceiros.',
  f7t:'Estante cultural',f7d:'Cada episódio concluído adiciona uma obra à sua biblioteca.',
  f8t:'Português e Español',f8d:'A interface funciona em português e em espanhol.',
  seeCourses:'Ver todos os cursos',nbBanner:'Novo: Neighbors em inglês (A1–C2) e em espanhol (A1)',nbBannerGo:'Abrir Neighbors',
  navHome:'Início',navEps:'Episódios',navShelf:'Estante',navComm:'Comunidade',navPanel:'Painel',days:'dias seguidos',
  hello:'Olá! Bom ver você',h1a:'Aprenda idiomas',h1b:'pela cultura',lead:'Filmes, livros, músicas e tradições de cada país, em episódios curtos com voz, prática e uma comunidade para conversar.',
  m1:'Cena real',m2:'Vocabulário',m3:'Prática',m4:'Voz',
  cont:'Continuar',contSub:'Continue de onde parou',contBtn:'Continuar',start:'Começar agora',startSub:'Escolha um idioma e abra o primeiro episódio.',startBtn:'Começar',
  sStreak:'dias seguidos',sXp:'pontos XP',sEps:'episódios feitos',sAcc:'de acerto',
  courses:'Seus cursos',coursesSub:'Cada idioma tem os próprios níveis, trilhas e progresso.',lessons:'episódios',available:'disponíveis',planned:'planejados',open:'Abrir',levels:'níveis',regular:'Regular',neighbors:'Neighbors',
  shelf:'Estante cultural',shelfSub:'Obras que você já conheceu nos episódios.',shelfAll:'Ver estante',shelfEmpty:'Conclua um episódio para ganhar o primeiro livro.',
  level:'Nível',epsT:'Episódios',of:'de',done:'concluídos',all:'Todos',search:'Buscar episódio ou obra',noRes:'Nenhum episódio encontrado.',more:'Mostrar mais',
  review:'Rever',continue:'Continuar',begin:'Começar',soon:'Em breve',seeCover:'Ver capa',ep:'EPISÓDIO',min:'MIN',arc:'Arco',
  resumeT:'Continue de onde parou',finished:'Você concluiu este curso',finishedSub:'Reveja seus episódios favoritos ou escolha outro nível.',
  test:'Mini-teste',testGo:'Fazer teste',testRedo:'Refazer',pickLevel:'Escolha seu nível',pickLevelSub:'Cada nível é um curso independente, com seu próprio progresso.',back:'Todos os idiomas',
  shelfT:'Estante cultural',shelfP:'Cada obra que você conhece nos episódios ganha um lugar aqui.',next:'Próximas obras',shelfBooks:'obras na estante',
  panel:'Painel do estudante',panelSub:'Seu progresso, suas metas e suas conquistas em um só lugar.',student:'Estudante',lg:'Liga',toNext:'para a próxima liga',top:'Você está na liga mais alta',
  goal:'Meta de hoje',goalDone:'Meta batida!',review2:'Revisão espaçada',review2Sub:'cartões prontos para rever',review2Go:'Revisar agora',review2None:'Nenhum cartão pendente por hoje.',
  myCourses:'Seus cursos',myCoursesSub:'Onde você está em cada trilha.',noCourses:'Você ainda não começou nenhum curso.',pick:'Escolher um curso',
  ach:'Conquistas',achSub:'Pequenos marcos que mostram o seu caminho.',unlocked:'Desbloqueadas',inProg:'Em andamento',
  acc:'Sua conta',accIn:'Conectado como',out:'Sair',acc2:'Entre para aparecer no ranking e conversar com a comunidade.',signin:'Entrar ou criar conta',login:'Entrar',
  sBest:'melhor sequência',sBooks:'livros',
  rank:'Ranking',chat:'Conversas',partners:'Parceiros',commT:'Comunidade',commSub:'Veja quem está na frente, converse e ache parceiros de estudo.',
  join:'Entre para aparecer no ranking',joinSub:'Crie sua conta gratuita para entrar na disputa, conversar e corrigir mensagens.',
  yourPos:'Sua posição',all2:'Todos',pts:'XP',daysU:'dias',epsU:'eps'},
 en:{shMy:'My shelf',shSort1:'Recent',shSearch:'Search work or author',shAuth:'authors',shWorks:'works',shEmptyT:'Your shelf is empty',shGo:'Start a course',shClose:'Close',
  cefrT:'From A1 to C2',cefrSub:'The six levels of the European Framework (CEFR).',
  l1:'Beginner',l2:'Basic',l3:'Intermediate',l4:'Upper intermediate',l5:'Advanced',l6:'Mastery',
  commHd:'Study together',achHd:'Achievements',seeAll:'See all',openComm:'Open community',openRank:'See ranking',
  commTx:'Chat with other learners, correct and get corrected, and find partners who speak the language you study.',rankTx:'Earn XP, keep your streak and climb leagues.',
  heroPill:'10-minute episodes',viewCourses:'See courses',navCourses:'Courses',coursesPage:'All courses',
  howT:'How it works',howSub:'Each episode lasts about 10 minutes and follows four steps.',
  h1t:'Real scene',h1d:'You hear a short dialogue from a real situation, with subtitles and translation.',
  h2t:'Vocabulary',h2d:'Six key words per episode, with sound, image and pronunciation tip.',
  h3t:'Practice',h3d:'Boards and mini-games to lock in what you heard, without memorizing rules.',
  h4t:'Voice',h4d:'You speak out loud and get feedback on your pronunciation.',
  navHome:'Home',navEps:'Episodes',navShelf:'Shelf',navComm:'Community',navPanel:'Dashboard',days:'day streak',
  hello:'Hi! Good to see you',h1a:'Learn languages',h1b:'through culture',lead:'Films, books, music and traditions from each country, in short episodes with voice, practice and a community to talk to.',
  cont:'Continue',contSub:'Pick up where you left off',contBtn:'Continue',start:'Start now',startBtn:'Start',
  sStreak:'day streak',sXp:'XP points',sEps:'episodes done',sAcc:'accuracy',
  courses:'Your courses',coursesSub:'Each language has its own levels, paths and progress.',lessons:'episodes',open:'Open',levels:'levels',
  shelf:'Cultural shelf',shelfAll:'See shelf',goal:'Today\'s goal',goalDone:'Goal reached!',review2:'Spaced review',review2Go:'Review now',rank:'Ranking',ach:'Achievements',available:'available',planned:'planned',regular:'Regular',neighbors:'Neighbors',
  chat:'Chats',partners:'Partners',commT:'Community',review:'Review',continue:'Continue',begin:'Start',ep:'EPISODE',min:'MIN'},
 es:{shMy:'Mi estante',shSort1:'Recientes',shSort2:'A–Z',shSearch:'Buscar obra o autor',shMile:'Próxima meta',shAuth:'autores',shWorks:'obras',shQueue:'En cola para entrar en la estante',shEmptyT:'Tu estante está vacía',shEmptyP:'Termina un episodio y la obra que conociste gana su lugar aquí.',shGo:'Empezar un curso',shNone:'No se encontraron obras.',shClose:'Cerrar',shBy:'de',
  cefrT:'De A1 a C2',cefrSub:'Los seis niveles del Marco Europeo (MCER). En español, también alineado con el DELE.',
  l1:'Principiante',l2:'Básico',l3:'Intermedio',l4:'Intermedio alto',l5:'Avanzado',l6:'Dominio',
  commHd:'Estudia acompañado',achHd:'Logros',seeAll:'Ver todo',openComm:'Abrir comunidad',openRank:'Ver ranking',
  commTx:'Conversa con otros alumnos, corrige y recibe correcciones, y encuentra compañeros que hablan el idioma que estudias.',rankTx:'Gana XP, mantén la racha y sube de liga.',
  heroPill:'Episodios de 10 minutos',viewCourses:'Ver cursos',
  navCourses:'Cursos',coursesPage:'Todos los cursos',coursesPageSub:'Elige un curso y abre su página: niveles, ruta y episodios.',
  nbSec:'Neighbors',nbSecSub:'Aprende conversando con vecinos: cada episodio es una persona, una ciudad y una situación real.',
  clSec:'Cursos por idioma',clSecSub:'Cursos clásicos, de A1 a C2, con películas, libros, canciones y tradiciones.',
  howT:'Cómo funciona',howSub:'Cada episodio dura unos 10 minutos y sigue cuatro pasos.',
  h1t:'Escena real',h1d:'Escuchas un diálogo corto de una situación real, con subtítulos y traducción.',
  h2t:'Vocabulario',h2d:'Seis palabras clave por episodio, con sonido, imagen y pista de pronunciación.',
  h3t:'Práctica',h3d:'Cuadros y minijuegos para fijar lo que oíste, sin memorizar reglas.',
  h4t:'Voz',h4d:'Hablas en voz alta y recibes una opinión sobre tu pronunciación.',
  metT:'Nuestra metodología',metSub:'Primero hablar. La gramática aparece con el uso, no con tablas.',
  me1t:'Primero hablar',me1d:'Empiezas escuchando y hablando situaciones reales; la gramática viene después, con el uso.',
  me2t:'Cultura de verdad',me2d:'Cada episodio parte de una obra, un país o una tradición, para dar contexto y memoria.',
  me3t:'Alineado al MCER',me3d:'Niveles A1 a C2 del Marco Europeo. El español también sigue el DELE del Instituto Cervantes.',
  me4t:'Repaso espaciado',me4d:'Las palabras vuelven en el momento justo para quedar en la memoria a largo plazo.',
  fnT:'Qué hay en Pogglot',fnSub:'Todo lo que usas para estudiar, en un solo lugar.',
  f1t:'Voz y pronunciación',f1d:'Audio nativo en cada frase y práctica de habla con corrección.',
  f2t:'Cuadros y juegos',f2d:'Puertas, globos, pesca, memoria y más para practicar de forma ligera.',
  f3t:'Repaso espaciado',f3d:'Tarjetas de vocabulario listas para repasar en el momento justo.',
  f4t:'Ruta y metas',f4d:'Meta diaria de XP, ruta del día y minitests por arco.',
  f5t:'Logros y ligas',f5d:'Gana XP, mantén la racha y sube de liga.',
  f6t:'Comunidad',f6d:'Conversa con otros alumnos, corrige y recibe correcciones, encuentra compañeros.',
  f7t:'Estante cultural',f7d:'Cada episodio terminado agrega una obra a tu biblioteca.',
  f8t:'Português y Español',f8d:'La interfaz funciona en portugués y en español.',
  seeCourses:'Ver todos los cursos',nbBanner:'Nuevo: Neighbors en inglés (A1–C2) y en español (A1)',nbBannerGo:'Abrir Neighbors',
  navHome:'Inicio',navEps:'Episodios',navShelf:'Estante',navComm:'Comunidad',navPanel:'Panel',days:'días seguidos',
  hello:'¡Hola! Qué bueno verte',h1a:'Aprende idiomas',h1b:'con cultura',lead:'Películas, libros, canciones y tradiciones de cada país, en episodios cortos con voz, práctica y una comunidad para conversar.',
  m1:'Escena real',m2:'Vocabulario',m3:'Práctica',m4:'Voz',
  cont:'Continuar',contSub:'Sigue donde lo dejaste',contBtn:'Continuar',start:'Empezar ahora',startSub:'Elige un idioma y abre el primer episodio.',startBtn:'Empezar',
  sStreak:'días seguidos',sXp:'puntos XP',sEps:'episodios hechos',sAcc:'de acierto',
  courses:'Tus cursos',coursesSub:'Cada idioma tiene sus propios niveles, rutas y progreso.',lessons:'episodios',available:'disponibles',planned:'planificados',open:'Abrir',levels:'niveles',regular:'Regular',neighbors:'Neighbors',
  shelf:'Estante cultural',shelfSub:'Obras que ya conociste en los episodios.',shelfAll:'Ver estante',shelfEmpty:'Termina un episodio para ganar el primer libro.',
  level:'Nivel',epsT:'Episodios',of:'de',done:'completados',all:'Todos',search:'Buscar episodio u obra',noRes:'No se encontraron episodios.',more:'Mostrar más',
  review:'Repasar',continue:'Continuar',begin:'Empezar',soon:'Próximamente',seeCover:'Ver portada',ep:'EPISODIO',min:'MIN',arc:'Arco',
  resumeT:'Sigue donde lo dejaste',finished:'Terminaste este curso',finishedSub:'Repasa tus episodios favoritos o elige otro nivel.',
  test:'Mini-test',testGo:'Hacer test',testRedo:'Rehacer',pickLevel:'Elige tu nivel',pickLevelSub:'Cada nivel es un curso independiente, con su propio progreso.',back:'Todos los idiomas',
  shelfT:'Estante cultural',shelfP:'Cada obra que conoces en los episodios gana un lugar aquí.',next:'Próximas obras',shelfBooks:'obras en el estante',
  panel:'Panel del estudiante',panelSub:'Tu progreso, tus metas y tus logros en un solo lugar.',student:'Estudiante',lg:'Liga',toNext:'para la próxima liga',top:'Estás en la liga más alta',
  goal:'Meta de hoy',goalDone:'¡Meta cumplida!',review2:'Repaso espaciado',review2Sub:'tarjetas listas para repasar',review2Go:'Repasar ahora',review2None:'No hay tarjetas pendientes por hoy.',
  myCourses:'Tus cursos',myCoursesSub:'Dónde estás en cada ruta.',noCourses:'Aún no empezaste ningún curso.',pick:'Elegir un curso',
  ach:'Logros',achSub:'Pequeños hitos que muestran tu camino.',unlocked:'Desbloqueados',inProg:'En progreso',
  acc:'Tu cuenta',accIn:'Sesión iniciada como',out:'Salir',acc2:'Entra para aparecer en el ranking y conversar con la comunidad.',signin:'Entrar o crear cuenta',login:'Entrar',
  sBest:'mejor racha',sBooks:'libros',
  rank:'Ranking',chat:'Conversaciones',partners:'Compañeros',commT:'Comunidad',commSub:'Mira quién va al frente, conversa y encuentra compañeros de estudio.',
  join:'Entra para aparecer en el ranking',joinSub:'Crea tu cuenta gratis para entrar en la competencia, conversar y corregir mensajes.',
  yourPos:'Tu posición',all2:'Todos',pts:'XP',daysU:'días',epsU:'eps'}
};
const LT=()=>ST.uiEn?'en':L0();
const t=k=>{const o=TX[LT()];return o&&o[k]!=null?o[k]:TX.pt[k]};

/* ---------- ícones ---------- */
const sv=p=>`<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${p}</svg>`;
const IC={
 home:()=>PU().IC.home,comm:()=>PU().IC.comm,me:()=>PU().IC.me,
 eps:()=>sv('<rect x="3" y="5" width="18" height="14" rx="3.5"/><path d="M10.2 9.4l4.6 2.6-4.6 2.6z"/>'),
 shelf:()=>sv('<path d="M4 20V5.5A1.5 1.5 0 015.5 4H8a1 1 0 011 1v15M9 20V7h4a1 1 0 011 1v12M14.5 19.5l3-12.6a1 1 0 011.2-.7l1.9.5a1 1 0 01.7 1.2l-3 12.6"/><path d="M3 20h18"/>'),
 gear:()=>sv('<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 00.3 1.8l.1.1a2 2 0 11-2.8 2.8l-.1-.1a1.7 1.7 0 00-1.8-.3 1.7 1.7 0 00-1 1.5V21a2 2 0 11-4 0v-.1a1.7 1.7 0 00-1.1-1.5 1.7 1.7 0 00-1.8.3l-.1.1a2 2 0 11-2.8-2.8l.1-.1a1.7 1.7 0 00.3-1.8 1.7 1.7 0 00-1.5-1H3a2 2 0 110-4h.1a1.7 1.7 0 001.5-1.1 1.7 1.7 0 00-.3-1.8l-.1-.1a2 2 0 112.8-2.8l.1.1a1.7 1.7 0 001.8.3H9a1.7 1.7 0 001-1.5V3a2 2 0 114 0v.1a1.7 1.7 0 001 1.5 1.7 1.7 0 001.8-.3l.1-.1a2 2 0 112.8 2.8l-.1.1a1.7 1.7 0 00-.3 1.8V9a1.7 1.7 0 001.5 1H21a2 2 0 110 4h-.1a1.7 1.7 0 00-1.5 1z"/>'),
 flame:()=>sv('<path d="M12 3c1 3.5 5 5.5 5 10a5 5 0 01-10 0c0-2.2 1-3.3 2-4.6.4 1.6 1.2 2 2 2C10.600 7.500 11 5.500 12 3z"/>'),
 bolt:()=>sv('<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>'),
 check:()=>sv('<path d="M5 12.5l4.5 4.5L19 7.500"/>'),
 target:()=>sv('<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.200"/>'),
 chev:()=>sv('<path d="M6 9l6 6 6-6"/>'),
 play:()=>sv('<path d="M7 4.500l12 7.500-12 7.500z"/>'),
 search:()=>sv('<circle cx="11" cy="11" r="7"/><path d="M20 20l-3.500-3.500"/>'),
 lock:()=>sv('<rect x="5" y="11" width="14" height="9" rx="2.500"/><path d="M8 11V8a4 4 0 018 0v3"/>'),
 arrow:()=>sv('<path d="M5 12h14M13 6l6 6-6 6"/>'),
 book:()=>sv('<path d="M4 5.500A2.500 2.500 0 016.500 3H20v16H6.500A2.500 2.500 0 004 21.500z"/><path d="M4 21.500V5.500"/>'),
 trophy:()=>sv('<path d="M8 21h8M12 17v4"/><path d="M7 4h10v6a5 5 0 01-10 0V4z"/><path d="M7 6H4v2a3 3 0 003 3M17 6h3v2a3 3 0 01-3 3"/>')
};
const NAV=[['home','navHome','home'],['courses','navCourses','book'],['shelf','navShelf','shelf'],['comm','navComm','comm']];
const NAV_M=NAV.concat([['profile','navPanel','me']]);
const curOf=()=>{const c=PU().cur;return c==='rank'?'comm':(c==='episodes'||c==='lang')?'courses':c};
const setHash=h=>{try{if(PU().setHash)PU().setHash(h)}catch(e){}};

/* ---------- utilidades de curso ---------- */
const lvlOf=cid=>{let v='';try{v=cl(cid)||''}catch(e){}if(!v){const m=String(cid).match(/-([abc][12])$/i);v=m?m[1].toUpperCase():''}return v};
const groupId=cid=>{const c=COURSES[cid];return c?(c.group||c.id):cid};
const langOf=cid=>PU().LANGS.find(l=>l.id===groupId(cid))||PU().LANGS[0];
const nOf=cid=>EP_COUNT[cid]||0;
const pctOf=cid=>{const n=nOf(cid);return n?Math.min(1,doneCountFor(cid)/n):0};
const isDone=(cid,e)=>!!ST.done[cid+'-'+e.n];
const LANG_ICON={en:'liberty',es:'guitar',fr:'eiffel',de:'castle',it:'colosseum',enes:'globe',pt:'palm'};
const LV_ICON={A1:'abc',A2:'chat',B1:'map',B2:'bulb',C1:'scroll',C2:'crown'};
const kindCache=new WeakMap();
function kindOf(e){let k=kindCache.get(e);if(!k){k=PC().kindInfo((e.a||{}).k);kindCache.set(e,k)}return k}
function kindLabel(e){const k=kindOf(e),g=PC().GROUPS[k.g];return g?g[L0()]:k.label}
const firstCourse=()=>{
  if(ST.lastCourse&&COURSES[ST.lastCourse])return ST.lastCourse;
  try{const p=JSON.parse(localStorage.getItem('pogglot:learningProfile')||'null');if(p&&p.preference==='Conversação'&&COURSES['nbeng-a1'])return'nbeng-a1';}catch(e){}
  return'en-a1';
};
function nextIdx(cid){const eps=EP[cid]||[];return eps.findIndex(e=>!isPlannedEpisode(e)&&!isDone(cid,e))}
function loadCourse(cid,fn){return navLoading(()=>ensureLangLoaded(cid).then(fn))}

/* ---------- barra superior e navegação inferior ---------- */
function ddCourses(cur){
  const ls=PU().LANGS;
  return `<div class="p2dd"><button data-go="courses" ${(cur==='courses'||cur==='episodes')?'aria-current="page"':''} aria-haspopup="true">${IC.book()}${E(t('navCourses'))}${IC.chev()}</button>
   <div class="p2ddp" role="menu"><a class="all" data-go="courses" role="menuitem">${E(t('seeCourses'))}${IC.arrow()}</a>${ls.map(l=>`<button role="menuitem" ${l.sub.length>1?`data-lang="${l.id}"`:`data-course="${l.sub[0]}"`} style="--c:${l.c}"><i></i><span>${E(l.n[L0()])}</span><small>${l.sub.length>1?'A1–C2':lvlOf(l.sub[0])}</small></button>`).join('')}</div></div>`;
}
window.topbar=function(){
  const u=me(),cur=curOf(),n=ST.streak.n||0,due=(()=>{try{return srsDueCount()}catch(e){return 0}})();
  return `<header class="pgbar p2bar"><div class="in">
   <button class="logo" data-go="home" aria-label="Pogglot"><span class="mini">${poggie({scarf:'#6DDFDB'})}</span><span>Pogg<b>lot</b></span></button>
   <nav class="pgtabs p2tabs" aria-label="Menu">${NAV.map(([id,key,ic])=>id==='courses'?ddCourses(cur):`<button data-go="${id}" ${cur===id?'aria-current="page"':''}>${IC[ic]()}${E(t(key))}</button>`).join('')}</nav>
   <div class="pgright">
    <span class="pgstat fire" title="${E(t('days'))}">${IC.flame()}<span data-pgstreak>${n}</span><span class="dw"> ${E(t('days'))}</span></span>
    <span class="pgstat xp hide-s" title="XP">${IC.bolt()}<span data-pgxp>${nf(ST.xp)}</span><span class="dw"> XP</span></span>
    ${due?`<button class="pgstat rev hide-s" data-go="review" title="${E(t('review2'))}">🔁 ${due}</button>`:''}
    <button class="pgstat gear theme" data-act="theme" aria-label="Tema">${window.PogTheme&&PogTheme.eff()==='dark'?'🌙':'☀️'}</button>
    <button class="pgstat gear hide-s" data-act="settings" aria-label="Ajustes" title="Ajustes">${IC.gear()}</button>
    ${u?`<button class="pgme" data-go="profile" title="${E(u.name)}"><span class="av">${E(u.avatar||'🙂')}</span><span class="nm">${E((u.name||'').split(' ')[0])}</span></button>`
       :`<button class="pgme guest" data-go="profile">${IC.me()}<span class="nm">${E(t('navPanel'))}</span></button>`}
    ${window.pgLangHTML()}
   </div></div></header>`;
};
window.pgLangHTML=()=>{const cur=ST.uiEn?'en':(ST.homeLang==='es'?'es':'pt'),fl=c=>{try{return fxIcon('flag:'+c,22)}catch(e){return c.toUpperCase()}};
 return `<div class="pglang pgflags" role="group" aria-label="Idioma / Language">${[['pt','br','Português'],['es','es','Español'],['en','us','English']].map(([k,c,n])=>`<button data-hl="${k}" aria-pressed="${cur===k}" aria-label="${n}" title="${n}">${fl(c)}</button>`).join('')}</div>`};
function mountNav(){
  let nav=document.getElementById('pgnav');
  if(!nav){nav=document.createElement('nav');nav.id='pgnav';nav.className='pgnav';nav.setAttribute('aria-label','Menu');document.body.appendChild(nav);document.body.classList.add('pg-has-nav')}
  const cur=curOf();
  nav.innerHTML=NAV_M.map(([id,key,ic])=>`<button data-go="${id}" ${cur===id?'aria-current="page"':''}>${IC[ic]()}<span>${E(t(key))}</span></button>`).join('');
}
function shell(inner,cls){app.innerHTML=window.topbar()+`<main class="p2 ${cls||''}">${inner}</main>`;mountNav();scrollTo(0,0)}

/* ---------- peças reutilizáveis ---------- */
const bar=p=>`<div class="p2bar-p" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="${Math.round(p*100)}"><i style="width:${(p*100).toFixed(1)}%"></i></div>`;
function sectionHead(h,p,right){return `<div class="p2sh"><div><h2>${E(h)}</h2>${p?`<p>${E(p)}</p>`:''}</div>${right||''}</div>`}
function langArt(l,iconId,sub){
  return `<div class="art" style="--c:${l.c};--cd:${l.cd}"><b class="wm">${E(l.mono)}</b><i class="tile">${PC().icon(iconId||LANG_ICON[l.id]||'globe',58,l.cd)}</i>${sub?`<span class="sub">${E(sub)}</span>`:''}</div>`;
}
const LANG_SC={en:'street',es:'plaza',fr:'paris',frbr:'paris',de:'station',it:'lisboa',ja:'japan',ko:'seoul',pt:'ipanema',nb:'plaza',nbes:'plaza',nbfr:'paris',nbde:'station',nbpt:'ipanema',nbit:'lisboa',nbeng:'street',nbja:'station',enes:'street'};
const LV_SC={A1:'cafe',A2:'street',B1:'office',B2:'station',C1:'library',C2:'ballroom'};
const sceneArt=(key,sc)=>{try{return PC().svg({t:String(key),sc,a:{w:String(key),k:'Cidade'},n:0},{noChar:true})}catch(e){return ''}};
function workCover(w,k){const e={t:w.w||w.t||'',n:0,a:{w:w.w||w.t||'',k:k||w.k||''}};return PC().work(e)}

/* ================= INÍCIO ================= */
function resumeHTML(){
  const res=resumeTarget();
  if(!res){
    return `<div class="p2res empty"><div class="rtxt"><small>${E(t('start'))}</small><b>${E(t('startSub'))}</b></div><button class="p2btn light" data-course="${firstCourse()}">${E(t('startBtn'))}${IC.arrow()}</button></div>`;
  }
  const c=COURSES[res.cid],lv=lvlOf(res.cid);
  return `<div class="p2res"><div class="cv">${PC().svg(res.e,{num:res.e.en||res.idx+1})}</div><div class="rtxt"><small>${E(t('contSub'))} · ${E(langOf(res.cid).n[L0()])}${lv?' '+lv:''}</small><b>${E(res.e.t)}</b><span>${E(t('ep'))} ${String(res.e.en||res.idx+1).padStart(2,'0')}${(res.e.a&&res.e.a.w)?' · '+E(res.e.a.w):''}</span></div><button class="p2btn light" data-ep="${res.cid}:${res.idx}">${E(t('contBtn'))}${IC.play()}</button></div>`;
}
function langCard(l,i){
  let n=0,d=0;l.sub.forEach(cid=>{n+=nOf(cid);d+=doneCountFor(cid)});
  const g=GROUPS[l.id]||COURSES[l.id]||{},p=n?d/n:0,multi=l.sub.length>1;
  const hd=multi?`data-lang="${l.id}"`:`data-course="${l.sub[0]}"`;
  const chips=multi?`<div class="lvls">${l.sub.map(cid=>`<button class="lv ${doneCountFor(cid)?'on':''}" data-course="${cid}" title="${E(COURSES[cid].name[L0()])}">${E(lvlOf(cid))}</button>`).join('')}</div>`
    :`<button class="p2btn soft sm" data-course="${l.sub[0]}">${E(d?t('continue'):t('begin'))}${IC.arrow()}</button>`;
  return `<article class="p2lang" style="--c:${l.c};--cd:${l.cd};--cl:${l.cl};animation-delay:${i*40}ms">
   <button class="hd" ${hd} aria-label="${E(l.n[L0()])}">${langArt(l,LANG_ICON[l.id],multi?`A1–C2`:'')}</button>
   <div class="bd"><span class="fl">${typeof flagPair==='function'?flagPair(g.flag||''):E(g.flag||'')}</span><h3>${E(l.n[L0()])}</h3><p>${E(g.desc?g.desc[L0()]:'')}</p>
    ${bar(p)}<div class="mt"><span>${nf(d)} ${E(t('of'))} ${nf(n)} ${E(t('lessons'))}</span><b>${Math.round(p*100)}%</b></div>${chips}</div></article>`;
}
function shelfStripHTML(){
  if(!ST.shelf.length)return `<div class="p2shelf-empty">${IC.book()}<span>${E(t('shelfEmpty'))}</span></div>`;
  return `<div class="p2strip">${ST.shelf.slice(-14).reverse().map(b=>`<figure class="p2book" title="${E(b.w)}${b.au?' — '+E(b.au):''}"><div class="cv">${workCover(b)}</div><figcaption>${E(b.w)}</figcaption></figure>`).join('')}</div>`;
}
window.home=function(){
  PU().cur='home';setHash('#/');
  const s=PU().stats(),acc=ST.totalAnswered?Math.round(ST.totalCorrect/ST.totalAnswered*100):0,L=L0();
  let got={},ACH=[];try{got=store.get('ach',{});ACH=PU().ACH||[]}catch(e){}
  const nextA=ACH.filter(a=>!got[a.id]).sort((a,b)=>b.cur(s)/b.goal-a.cur(s)/a.goal).slice(0,4);
  const showA=nextA.length?nextA:ACH.slice(0,4);
  const lv=['A1','A2','B1','B2','C1','C2'],steps=[['🎬','1'],['🔤','2'],['🎮','3'],['🎤','4']];
  const res=(()=>{try{return resumeTarget()}catch(e){return null}})(),u=me();
  let goal=null;try{goal=window.PogSettings&&PogSettings.goalState?PogSettings.goalState():null}catch(e){}
  const due=(()=>{try{return srsDueCount()}catch(e){return 0}})();
  const ls0=PU().LANGS,order=['en','es','nb','fr','de','it','nbes','nbfr','nbde','nbpt','nbja','pt','enes'],started=l=>{let d=0;try{l.sub.forEach(c=>{d+=doneCountFor(c)})}catch(e){}return d>0?0:1},ls=ls0.slice().sort((x,y)=>(started(x)-started(y))||((order.indexOf(x.id)<0?99:order.indexOf(x.id))-(order.indexOf(y.id)<0?99:order.indexOf(y.id))));
  const first=u&&u.name?String(u.name).split(' ')[0]:'';
  const rc=res?COURSES[res.cid]:null,rlv=res?lvlOf(res.cid):'';
  const pill=(ic,v,l)=>`<span class="px-pill"><i>${ic}</i><b data-cu>${v}</b><small>${E(l)}</small></span>`;
  const quick=[['listen','🎧',L0()==='es'?'Escuchar':'Ouvir',''],['review',due?'🔁':'🔁',t('review2'),due||''],['shelf','📚',t('navShelf'),''],['comm','💬',t('navComm'),''],['rank','🏆',t('rank'),''],['ach','🎖️',t('achHd'),`${(()=>{try{return Object.keys(got).length}catch(e){return ''}})()||''}`],['profile','👤',t('navPanel'),'']];
  const langPill=l=>{let n=0,d=0;l.sub.forEach(cid=>{n+=nOf(cid);d+=doneCountFor(cid)});const g=GROUPS[l.id]||COURSES[l.id]||{},p=n?d/n:0,multi=l.sub.length>1,hd=multi?`data-lang="${l.id}"`:`data-course="${l.sub[0]}"`;
    return `<button class="px-lang" ${hd} style="--c:${l.c};--cd:${l.cd};--cl:${l.cl};--p:${(p*100).toFixed(0)}"><span class="bgart">${sceneArt(l.id,LANG_SC[l.id]||'plaza')}</span><span class="fl">${typeof flagPair==='function'?flagPair(g.flag||''):E(g.flag||'')}</span><span class="mono">${E(l.mono)}</span><b>${E(l.n[L0()])}</b><small>${multi?'A1–C2':E(lvlOf(l.sub[0])||'')} · ${nf(n)} ${E(t('lessons'))}</small><span class="rg"><i></i><em>${Math.round(p*100)}%</em></span></button>`};
  shell(`
  <section class="px-hero ${res?'has':''}">
   <div class="px-hl"><span class="px-eyebrow">${first?E(t('hello'))+', '+E(first)+' 👋':E(t('heroPill'))}</span>
    ${res?`<h1>${E(res.e.t)}</h1><p>${E(langOf(res.cid).n[L0()])}${rlv?' · '+E(rlv):''} · ${E(t('ep'))} ${String(res.e.en||res.idx+1).padStart(2,'0')}${(res.e.a&&res.e.a.w)?' · '+E(res.e.a.w):''}</p>`
         :`<h1>${E(t('h1a'))} <em>${E(t('h1b'))}</em></h1><p>${E(t('lead'))}</p>`}
    <div class="px-acts">${res?`<button class="px-cta" data-ep="${res.cid}:${res.idx}">${IC.arrow()}<span>${E(t('contBtn'))}</span></button>`:`<button class="px-cta" data-course="${firstCourse()}">${IC.arrow()}<span>${E(t('startBtn'))}</span></button>`}<button class="px-ghost" data-go="courses">${E(t('viewCourses'))}</button></div>
    <div class="px-pills">${pill('🔥',nf(ST.streak.n||0),t('sStreak'))}${pill('⚡',nf(ST.xp||0),'XP')}${pill('✅',nf(s.eps),t('sEps'))}${ST.totalAnswered?pill('🎯',acc+'%',t('sAcc')):''}</div></div>
   <div class="px-hr">${res?`<div class="px-cover" data-ep="${res.cid}:${res.idx}">${PC().svg(res.e,{num:res.e.en||res.idx+1,full:true})}<span class="px-play">▶</span></div>`:`<div class="p2-course-showcase"><img src="img/course-showcase.webp" alt="Cenas de estudo em diferentes cidades e idiomas" loading="eager"><div class="p2-course-caption"><b>${E(L0()==='es'?'Un idioma abre nuevos lugares':'Um idioma abre novos lugares')}</b><span>${E(L0()==='es'?'Cursos regulares y Neighbors':'Cursos regulares e Neighbors')}</span></div></div>`}
    ${goal?`<div class="px-goal"><div class="rg">${PogSettings.ringHTML(goal.pct,54,7)}<span>${Math.round(goal.pct*100)}%</span></div><div><small>${E(t('goal'))}</small><b>${nf(goal.xp)}/${nf(goal.goal)} XP</b></div></div>`:''}</div>
  </section>
  <section class="px-quick" aria-label="Atalhos">${quick.map(([id,ic,l,bd])=>`<button ${id==='listen'?`data-listen="${ST.lastCourse||''}"`:`data-go="${id}"`}><i>${ic}${bd?`<em>${bd}</em>`:''}</i><span>${E(l)}</span></button>`).join('')}</section>
  <div class="pt-today-slot"></div>
  ${(()=>{try{return srsBanner()||''}catch(e){return ''}})()}
  <section class="px-sec">${sectionHead(t('courses'),t('coursesSub'),`<button class="p2link" data-go="courses">${E(t('seeAll'))}${IC.arrow()}</button>`)}<div class="px-langs">${ls.map(langPill).join('')}</div></section>
  ${window.PogMissions?PogMissions.cardHTML():''}
  ${window.PogRecap?PogRecap.recapHTML():''}
  ${res||ST.xp>0?'':`<section class="px-sec">${sectionHead(t('howT'))}<div class="px-steps">${steps.map(([ic,i])=>`<div class="st"><span class="n">${i}</span><i>${ic}</i><b>${E(t('h'+i+'t'))}</b><small>${E(t('h'+i+'d'))}</small></div>`).join('')}</div></section>`}
  ${res||ST.xp>0?'':`<section class="px-sec">${sectionHead(t('cefrT'))}<div class="px-cefr">${lv.map((x,i)=>`<div class="l l${i}"><b>${x}</b><small>${E(t('l'+(i+1)))}</small></div>`).join('')}</div></section>`}
  ${showA.length?`<section class="px-sec">${sectionHead(t('achHd'),'',`<button class="p2link" data-go="ach">${E(t('seeAll'))}${IC.arrow()}</button>`)}<div class="px-achrow">${showA.map(a=>`<div class="a ${got[a.id]?'':'lock'}" style="--p:${got[a.id]?100:Math.min(100,Math.round(a.cur(s)/a.goal*100))}"><span class="rg"><i>${a.ic}</i></span><b>${E(a.n[L])}</b><small>${got[a.id]?'✓':Math.min(a.cur(s),a.goal)+'/'+a.goal}</small></div>`).join('')}</div></section>`:''}`,'home');
  try{
    const host=document.querySelector('.pt-today-slot');
    if(host&&window.PogPath&&PogPath.renderCard){const sec=document.createElement('section');sec.className='pt-today';host.replaceWith(sec);PogPath.renderCard()}
    else if(host)host.remove();
  }catch(e){}
  /* se o curso do "continuar" ainda não foi carregado, carrega em segundo plano */
  if(ST.lastCourse&&COURSES[ST.lastCourse]&&!(EP[ST.lastCourse]||[]).length){
    ensureLangLoaded(ST.lastCourse).then(()=>{const h=document.getElementById('p2resume');if(h&&PU().cur==='home')h.innerHTML=resumeHTML()}).catch(()=>{});
  }
};

/* ================= PÁGINA DO IDIOMA (níveis) ================= */
window.hub=function(id){
  const l=PU().LANG(id);
  if(l.sub.length===1){const cid=l.sub[0];return loadCourse(cid,()=>window.course(cid))}
  PU().cur='courses';setHash('#/lang/'+l.id);
  const g=GROUPS[l.id]||{},L=L0();
  let n=0,d=0;l.sub.forEach(cid=>{n+=nOf(cid);d+=doneCountFor(cid)});const p=n?d/n:0;
  shell(`<button class="p2back" data-go="home">${IC.arrow()}<span>${E(t('back'))}</span></button>
  <section class="p2lhead px-hero2" style="--c:${l.c};--cd:${l.cd}"><div class="bgart">${sceneArt(l.id,LANG_SC[l.id]||'plaza')}</div><div class="tx"><span class="p2eyebrow on">${typeof flagPair==='function'?flagPair(g.flag||''):''}</span><h1>${E(l.n[L])}</h1><p>${E(g.desc?g.desc[L]:'')}</p>
   <div class="pr"><div class="p2bar-p inv"><i style="width:${(p*100).toFixed(1)}%"></i></div><span>${nf(d)} ${E(t('of'))} ${nf(n)} · ${Math.round(p*100)}%</span></div></div>${langArt(l,LANG_ICON[l.id])}</section>
  ${(l.id==='nbes'||l.id==='nbfr')?'<div id="goalcard" class="goalcard"></div>':''}
  ${sectionHead(t('pickLevel'),t('pickLevelSub'))}
  <div class="p2levels">${l.sub.map((cid,i)=>{const c=COURSES[cid],lv=lvlOf(cid),cn=nOf(cid),cd=doneCountFor(cid),cp=cn?cd/cn:0,pal=PC().palette(cid);
    return `<article class="p2level" style="--c1:${pal.c1};--c2:${pal.c2};animation-delay:${i*45}ms"><button class="hd" data-course="${cid}"><b class="big">${E(lv||'•')}</b><span class="bgart">${sceneArt(cid,LV_SC[lv]||'plaza')}</span></button>
     <div class="bd"><h3>${E(t('level'))} ${E(lv)}</h3><p>${E(c.desc[L])}</p>${bar(cp)}<div class="mt"><span>${nf(cd)} ${E(t('of'))} ${nf(cn)} ${E(t('lessons'))}</span><b>${Math.round(cp*100)}%</b></div>
     <button class="p2btn ${cd?'pri':'soft'} sm" data-course="${cid}">${E(cd?(cd>=cn&&cn?t('review'):t('continue')):t('begin'))}${IC.arrow()}</button></div></article>`}).join('')}</div>`,'lang');
  if(document.getElementById('goalcard')&&typeof goalCard==='function')goalCard(l.id);
};

/* ================= EPISÓDIOS ================= */
const V={cid:null,filter:'all',q:'',open:new Set(),lim:36,arcs:[]};
function buildArcs(cid){
  const list=EP[cid]||[],A=ARCS[cid]||[],out=[];
  A.forEach((a,ai)=>{const s=list.findIndex(e=>e.n===a[0]);if(s>=0)out.push({ai,s,title:String(a[1]).replace(/^Arco\s*/,''),tests:[]})});
  out.sort((x,y)=>x.s-y.s);
  if(out.length){out.forEach((o,k)=>{o.e=k+1<out.length?out[k+1].s:list.length});if(out[0].s>0)out.unshift({ai:-1,s:0,e:out[0].s,title:t('arc'),tests:[]})}
  else{for(let s=0;s<list.length;s+=24)out.push({ai:-2,s,e:Math.min(list.length,s+24),title:`${s+1}–${Math.min(list.length,s+24)}`,tests:[]})}
  const arcOfIdx=i=>out.find(o=>i>=o.s&&i<o.e);
  let ts=[];try{ts=arcTests(cid).concat(cpTests(cid))}catch(e){}
  ts.forEach(x=>{const o=out.find(a=>a.ai===x.arcIdx);if(o)o.tests.push(x)});
  (TESTS[cid]||[]).forEach(x=>{
    let i=-1;if(x.afterId!=null)i=list.findIndex(e=>e.n===x.afterId);else if(x.afterN!=null){for(let k=0;k<list.length;k++)if(list[k].n<=x.afterN)i=k}
    const o=arcOfIdx(Math.max(0,i));if(o)o.tests.push(x)});
  return out;
}
function epCard(cid,e,i,nextI){
  const num=e.en||i+1,numS=String(num).padStart(2,'0'),L=L0();
  if(isPlannedEpisode(e)){
    return `<article class="p2ep soon"><button class="cv" data-plan="${cid}:${i}" aria-label="${E(e.t)}">${PC().locked(e,{num})}<span class="kd">${IC.lock()}${E(t('soon'))}</span></button>
     <div class="bd"><small class="meta">${E(t('ep'))} ${numS}</small><h3>${E(e.t)}</h3><p class="src">${E(kindLabel(e))}${(e.a&&e.a.w)?' · '+E(e.a.w):''}</p><button class="p2btn ghost sm" data-plan="${cid}:${i}">${E(t('seeCover'))}</button></div></article>`;
  }
  const done=isDone(cid,e),isNext=i===nextI,k=kindOf(e);
  const btn=done?['ghost',t('review')]:isNext?['pri',t('continue')]:['soft',t('begin')];
  return `<article class="p2ep ${done?'done':''} ${isNext?'next':''}"><button class="cv" data-ep="${cid}:${i}" aria-label="${E(e.t)}">${(e.pilot&&window.PogStage&&e.stage)?PogStage.stage({rs:e.stage.rs,chars:(e.stage.chars||[]).slice(0,1).map(c=>[c[0],50,0,.95]),h:'card'}):PC().svg(e,{num})}
    <span class="kd"><i>${PC().icon(k.ic,14,'#fff')}</i>${E(kindLabel(e))}</span>${done?`<span class="ck">${IC.check()}</span>`:''}</button>
   <div class="bd"><small class="meta">${E(t('ep'))} ${numS} · 10 ${E(t('min'))}</small><h3>${E(e.t)}</h3>${e.s?`<p class="sub">${E(e.s)}</p>`:''}<p class="src">${(e.a&&e.a.w)?E(e.a.w):''}</p>
    <button class="p2btn ${btn[0]} sm" data-ep="${cid}:${i}">${E(btn[1])}</button>${e.pilot?`<button type="button" class="p2btn ghost sm ps-revbtn" data-rev="${cid}:${i}">🔁 ${E(L==='es'?'Repaso':'Revisão')}</button>`:''}</div></article>`;
}
function testCard(cid,ts){
  const done=!!ST.testDone[cid+'-'+ts.id];
  return `<button class="p2test ${done?'done':''}" data-test="${cid}:${ts.id}"><span class="ic">${PC().icon('trophy',34,'#8a3b10')}</span><span class="tx"><b>${E(ts.t)}</b><small>${E(ts.sub||'')}</small></span><em>${E(done?t('testRedo'):t('testGo'))}</em></button>`;
}
function arcBodyHTML(o,nextI){
  const list=EP[V.cid]||[];let h='<div class="p2grid">';
  for(let i=o.s;i<o.e;i++)h+=epCard(V.cid,list[i],i,nextI);
  h+='</div>';
  if(o.tests.length)h+=`<div class="p2tests">${o.tests.map(x=>testCard(V.cid,x)).join('')}</div>`;
  return h;
}
function matches(e,i){
  if(V.filter!=='all'&&kindOf(e).g!==V.filter)return false;
  if(V.q){const q=norm(V.q);return norm(e.t).includes(q)||norm(e.s).includes(q)||norm((e.a||{}).w).includes(q)||String(e.en||i+1)===q}
  return true;
}
function listHTML(){
  const cid=V.cid,list=EP[cid]||[],nextI=nextIdx(cid);
  if(V.q||V.filter!=='all'){
    const hit=[];list.forEach((e,i)=>{if(matches(e,i))hit.push(i)});
    if(!hit.length)return `<p class="p2empty">${E(t('noRes'))}</p>`;
    return `<div class="p2grid">${hit.slice(0,V.lim).map(i=>epCard(cid,list[i],i,nextI)).join('')}</div>${hit.length>V.lim?`<div class="p2morewrap"><button class="p2btn soft" data-p2more>${E(t('more'))} (${hit.length-V.lim})</button></div>`:''}`;
  }
  return V.arcs.map((o,k)=>{
    const eps=list.slice(o.s,o.e).filter(e=>!isPlannedEpisode(e)),d=eps.filter(e=>isDone(cid,e)).length,p=eps.length?d/eps.length:0,open=V.open.has(k);
    return `<section class="p2arc ${open?'open':''} ${p>=1&&eps.length?'complete':''}" data-k="${k}"><button class="ah" data-p2arc="${k}" aria-expanded="${open}">
      <span class="num">${p>=1&&eps.length?IC.check():k+1}</span>${(list[o.s]&&!isPlannedEpisode(list[o.s]))?`<span class="th">${PC().svg(list[o.s],{noChar:false})}</span>`:''}<span class="tt"><b>${E(o.title)}</b><small>${nf(d)}/${nf(eps.length)} ${E(t('lessons'))}</small></span>
      <span class="mini">${bar(p)}</span><span class="cv">${IC.chev()}</span></button><div class="ab">${open?arcBodyHTML(o,nextI):''}</div></section>`}).join('');
}
function chipsHTML(){
  const cid=V.cid,list=EP[cid]||[],cnt={};
  list.forEach(e=>{if(isPlannedEpisode(e))return;const g=kindOf(e).g;cnt[g]=(cnt[g]||0)+1});
  const ids=Object.keys(cnt).sort((a,b)=>cnt[b]-cnt[a]).slice(0,7);
  return `<button class="p2chip" data-p2f="all" aria-pressed="${V.filter==='all'}">${E(t('all'))}</button>`+ids.map(g=>`<button class="p2chip" data-p2f="${g}" aria-pressed="${V.filter===g}">${E(PC().GROUPS[g][L0()])}<small>${cnt[g]}</small></button>`).join('');
}
function bannerHTML(cid){
  const list=EP[cid]||[],ni=nextIdx(cid);
  if(ni<0&&list.some(x=>isPlannedEpisode(x))){const e=list.find(x=>!isPlannedEpisode(x)),all=!e;return `<div class="p2banner done"><div class="tx"><small>${all?'Trilha planejada':'Você concluiu os episódios disponíveis'}</small><b>${all?'Os episódios deste nível chegam em breve. Veja o plano abaixo: títulos, descrições e metas.':'Os próximos episódios já estão planejados na trilha abaixo.'}</b></div>${e?`<button class="p2btn light" data-ep="${cid}:${list.indexOf(e)}">${E(t('review'))}</button>`:''}</div>`}
  if(ni<0){const e=list.find(x=>!isPlannedEpisode(x));return `<div class="p2banner done"><div class="tx"><small>${E(t('finished'))}</small><b>${E(t('finishedSub'))}</b></div>${e?`<button class="p2btn light" data-ep="${cid}:${list.indexOf(e)}">${E(t('review'))}</button>`:''}</div>`}
  const e=list[ni];
  return `<div class="p2banner"><div class="cv">${PC().svg(e,{num:e.en||ni+1})}</div><div class="tx"><small>${E(t('resumeT'))}</small><b>${E(e.t)}</b><span>${E(t('ep'))} ${String(e.en||ni+1).padStart(2,'0')}${e.a&&e.a.w?' · '+E(e.a.w):''}</span></div><button class="p2btn light" data-ep="${cid}:${ni}">${E(t('continue'))}${IC.play()}</button></div>`;
}
function refreshList(){const box=document.getElementById('p2list');if(box)box.innerHTML=listHTML();const ch=document.getElementById('p2chips');if(ch)ch.innerHTML=chipsHTML()}
window.course=function(id){
  const c=COURSES[id];if(!c)return window.home();
  const L=L0(),l=langOf(id),lv=lvlOf(id),n=nOf(id),d=doneCountFor(id),p=n?d/n:0,list=EP[id]||[];
  PU().cur='episodes';setHash('#/course/'+id);
  const fresh=V.cid!==id;
  if(fresh){V.cid=id;V.filter='all';V.q='';V.lim=36;V.open=new Set();V.arcs=buildArcs(id)}else V.arcs=buildArcs(id);
  if(fresh||!V.open.size){const ni=nextIdx(id),k=V.arcs.findIndex(o=>ni>=0?(ni>=o.s&&ni<o.e):false);V.open.add(k>=0?k:0)}
  const g=GROUPS[c.group];const sibs=g&&g.sub.length>1?g.sub:null;
  const RG=2*Math.PI*36;
  shell(`<button class="p2back" data-go="courses">${IC.arrow()}<span>${E(t('navCourses'))}</span></button>
   <section class="p5h px-hero2" style="--c:${l.c};--cd:${l.cd}"><div class="bgart">${(()=>{const ni0=nextIdx(id),e0=list[ni0>=0?ni0:0];return e0?PC().svg(e0,{noChar:true}):sceneArt(id,LANG_SC[c.group]||'plaza')})()}</div><div class="tx"><span class="p2eyebrow on">${E(l.n[L].toUpperCase())}${lv?' · '+E(t('level').toUpperCase())+' '+E(lv):''}</span><h1>${E(c.name[L])}</h1><p>${E(c.desc[L])}</p>
     <div class="st"><span class="chip"><b>${nf(d)}</b> ${E(t('of'))} ${nf(n)} ${E(t('done'))}</span>${lv?`<span class="chip">${E(t('level'))} ${E(lv)}</span>`:''}<span class="chip">⏱ 10 ${E(t('min').toLowerCase())}</span></div></div>
     <div class="rg"><svg width="86" height="86" viewBox="0 0 86 86"><circle cx="43" cy="43" r="36" fill="none" stroke="rgba(255,255,255,.25)" stroke-width="8"/><circle cx="43" cy="43" r="36" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round" stroke-dasharray="${RG}" stroke-dashoffset="${RG*(1-p)}" transform="rotate(-90 43 43)"/></svg><span>${Math.round(p*100)}%</span></div></section>
   ${sibs?`<div class="p2levelsw" role="tablist">${sibs.map(cid=>`<button class="p2chip lvl" data-course="${cid}" aria-pressed="${cid===id}">${E(lvlOf(cid))}</button>`).join('')}</div>`:''}
   ${bannerHTML(id)}
   <div class="p2tools"><div class="p2chips" id="p2chips">${chipsHTML()}</div><label class="p2search">${IC.search()}<input id="p2q" type="search" placeholder="${E(t('search'))}" aria-label="${E(t('search'))}" value=""></label></div>
   <div id="p2list" class="p2list">${listHTML()}</div>`,'eps');
  const q=document.getElementById('p2q');let tm=0;
  if(q)q.oninput=()=>{clearTimeout(tm);tm=setTimeout(()=>{V.q=q.value.trim();V.lim=36;refreshList()},160)};
};
function openEpisodes(){const cid=firstCourse();loadCourse(cid,()=>window.course(cid))}

document.addEventListener('click',ev=>{
  if(typeof P!=='undefined'&&P)return;
  const a=ev.target.closest('[data-p2arc]');
  if(a){const k=+a.dataset.p2arc;if(V.open.has(k))V.open.delete(k);else V.open.add(k);
    const sec=a.closest('.p2arc'),o=V.arcs[k],open=V.open.has(k);
    sec.classList.toggle('open',open);a.setAttribute('aria-expanded',open);
    sec.querySelector('.ab').innerHTML=open?arcBodyHTML(o,nextIdx(V.cid)):'';return}
  const f=ev.target.closest('[data-p2f]');
  if(f){V.filter=f.dataset.p2f;V.lim=36;refreshList();return}
  const m=ev.target.closest('[data-p2more]');
  if(m){V.lim+=36;refreshList();return}
});

/* ================= ESTANTE ================= */
const SH={q:'',sort:'new'};
function shelfBooks(){
  let l=ST.shelf.map((b,i)=>({b,i}));
  if(SH.q){const q=norm(SH.q);l=l.filter(x=>norm(x.b.w).includes(q)||norm(x.b.au).includes(q))}
  l=SH.sort==='az'?l.sort((x,y)=>norm(x.b.w).localeCompare(norm(y.b.w))):l.reverse();
  return l;
}
const workPal=w=>{try{const e={t:w.w||w.t||'',n:0,a:{w:w.w||w.t||'',k:w.k||''}};return PC().palette(PC().analyse(e).seed)}catch(x){return{c1:'#6DDFDB',c2:'#3699A8'}}};
function workCard(b,i,lock){const pal=workPal(b);
  return `<button class="px-work ${lock?'lock':''}" ${lock?'':`data-bk="${i}"`} style="--wc:${pal.c1};--wd:${pal.c2}" title="${E(b.w)}"><div class="cv">${workCover(b)}${lock?`<span class="lk">${IC.lock()}</span>`:`<span class="pl">▶</span>`}</div><b>${E(b.w)}</b><small>${E(b.au||'')}</small></button>`;
}
function shelfRowsHTML(){
  const l=shelfBooks();if(!l.length)return `<p class="p2empty">${E(t('shNone'))}</p>`;
  return `<div class="px-wgrid">${l.map(({b,i})=>workCard(b,i)).join('')}</div>`;
}
function workEpisodes(w){
  const key=norm(w.w),out=[];
  Object.keys(EP||{}).forEach(cid=>{(EP[cid]||[]).forEach((e,i)=>{if(out.length<10&&e.a&&e.a.w&&norm(e.a.w)===key&&!isPlannedEpisode(e))out.push({cid,i,e})})});
  return out;
}
function shelfSheet(i){
  const b=ST.shelf[i];if(!b)return;
  let d=document.getElementById('p4sheet');if(d)d.remove();
  const pal=workPal(b),eps=workEpisodes(b),L=L0();
  d=document.createElement('div');d.id='p4sheet';d.className='px-wp';d.style.setProperty('--wc',pal.c1);d.style.setProperty('--wd',pal.c2);
  d.innerHTML=`<div class="bg" data-x></div><div class="sheet" role="dialog" aria-label="${E(b.w)}"><button class="x" data-x aria-label="${E(t('shClose'))}">✕</button>
   <div class="hd"><div class="cv">${workCover(b)}</div><div class="tx"><small>${E(t('shWorks').toUpperCase())}</small><h2>${E(b.w)}</h2>${b.au?`<p>${E(t('shBy'))} <b>${E(b.au)}</b></p>`:''}
    <div class="acts">${eps[0]?`<button class="px-play-btn" data-x data-ep="${eps[0].cid}:${eps[0].i}">▶ <span>${E(L==='es'?'Abrir episodio':'Abrir episódio')}</span></button>`:''}<button class="px-share" data-share="${E(b.w)}" aria-label="Compartilhar">⤴</button></div></div></div>
   ${eps.length?`<h3>${E(L==='es'?'Aparece en':'Aparece em')}</h3><div class="eps">${eps.map(({cid,i,e},k)=>`<button class="ep" data-x data-ep="${cid}:${i}"><span class="n">${k+1}</span><span class="t"><b>${E(e.t)}</b><small>${E(langOf(cid).n[L])}${lvlOf(cid)?' '+E(lvlOf(cid)):''} · ${E(t('ep'))} ${String(e.en||i+1).padStart(2,'0')}</small></span><span class="go">▶</span></button>`).join('')}</div>`:`<p class="none">${E(L==='es'?'Abre un curso para ver los episodios donde aparece esta obra.':'Abra um curso para ver os episódios em que esta obra aparece.')}</p>`}</div>`;
  document.body.appendChild(d);document.body.classList.add('px-lockscroll');requestAnimationFrame(()=>d.classList.add('on'));
  const close=()=>{d.classList.remove('on');document.body.classList.remove('px-lockscroll');setTimeout(()=>d.remove(),240)};
  d.addEventListener('click',e=>{
    const sh=e.target.closest('[data-share]');if(sh){const txt=`${b.w}${b.au?' — '+b.au:''} · Pogglot`;try{if(navigator.share)navigator.share({title:'Pogglot',text:txt,url:location.origin+location.pathname});else navigator.clipboard.writeText(txt)}catch(x){}return}
    if(e.target.closest('[data-x]'))close();
  });
}
function shelf(){
  PU().cur='shelf';setHash('#/shelf');
  const n=ST.shelf.length,au=new Set(ST.shelf.map(b=>norm(b.au)).filter(Boolean)).size;
  const MS=[5,10,25,50,100],nx=MS.find(x=>x>n)||MS[MS.length-1],prev=MS.filter(x=>x<=n).pop()||0,pc=n>=MS[MS.length-1]?1:(n-prev)/(nx-prev),R=2*Math.PI*34;
  shell(`<section class="p4hero"><div class="tx"><span class="p2eyebrow on">${E(t('shMy').toUpperCase())}</span><h1>${E(t('shelfT'))}</h1><p>${E(t('shelfP'))}</p>
    <div class="nums"><div><b>${nf(n)}</b><small>${E(t('shWorks'))}</small></div><div><b>${nf(au)}</b><small>${E(t('shAuth'))}</small></div></div></div>
    <div class="ring"><svg width="92" height="92" viewBox="0 0 92 92"><circle cx="46" cy="46" r="34" fill="none" stroke="rgba(255,255,255,.22)" stroke-width="9"/><circle cx="46" cy="46" r="34" fill="none" stroke="#ffe58a" stroke-width="9" stroke-linecap="round" stroke-dasharray="${R}" stroke-dashoffset="${R*(1-pc)}" transform="rotate(-90 46 46)"/></svg><span>${n}/${nx}</span><small>${E(t('shMile'))}</small></div></section>
   ${n?`${(()=>{const rec=ST.shelf.map((x,i)=>({b:x,i})).reverse().slice(0,12);const cnt={};ST.shelf.forEach(x=>{if(x.au)cnt[x.au]=(cnt[x.au]||0)+1});const top=Object.entries(cnt).sort((x,y)=>y[1]-x[1])[0];
       return `<section class="px-sec"><div class="p2sh"><div><h2>${E(L0()==='es'?'Añadidas recientemente':'Adicionadas recentemente')}</h2></div></div><div class="px-rail">${rec.map(({b,i})=>workCard(b,i)).join('')}</div></section>
       ${top?`<section class="px-recap"><span class="e">📖</span><div><small>${E(L0()==='es'?'TU AÑO EN OBRAS':'SEU ANO EM OBRAS')}</small><b>${n} ${E(t('shWorks'))} · ${au} ${E(t('shAuth'))}</b><p>${E(L0()==='es'?'Autor más frecuente':'Autor mais frequente')}: <em>${E(top[0])}</em> (${top[1]})</p></div></section>`:''}`})()}
     <section class="px-sec"><div class="p2sh"><div><h2>${E(L0()==='es'?'Toda la colección':'Toda a coleção')}</h2></div></div>
     <div class="p4tools"><label class="p2search">${IC.search()}<input id="p4q" type="search" placeholder="${E(t('shSearch'))}" aria-label="${E(t('shSearch'))}"></label>
     <div class="seg" role="group"><button data-p4s="new" aria-pressed="${SH.sort==='new'}">${E(t('shSort1'))}</button><button data-p4s="az" aria-pressed="${SH.sort==='az'}">${E(t('shSort2'))}</button></div></div>
     <div class="p4case" id="p4case">${shelfRowsHTML()}</div></section>
     <div class="p4ms">${MS.map(m=>`<span class="${n>=m?'on':''}"><i>${n>=m?'★':'☆'}</i>${m}</span>`).join('')}</div>`
    :`<div class="p4empty"><div class="gh">${[0,1,2].map(k=>`<i style="--k:${k}"></i>`).join('')}</div><h3>${E(t('shEmptyT'))}</h3><p>${E(t('shEmptyP'))}</p><button class="p2btn pri" data-go="courses">${E(t('shGo'))}${IC.arrow()}</button></div>`}
   <section id="p2next"></section>`,'shelfpg');
  const q=document.getElementById('p4q');let tm=0;
  if(q)q.oninput=()=>{clearTimeout(tm);tm=setTimeout(()=>{SH.q=q.value.trim();const c=document.getElementById('p4case');if(c)c.innerHTML=shelfRowsHTML()},150)};
  const cid=ST.lastCourse&&COURSES[ST.lastCourse]?ST.lastCourse:null;
  if(cid)ensureLangLoaded(cid).then(()=>{
    const host=document.getElementById('p2next');if(!host||PU().cur!=='shelf')return;
    const have=new Set(ST.shelf.map(b=>norm(b.w))),seen=new Set(),out=[];
    for(const e of (EP[cid]||[])){if(isPlannedEpisode(e)||isDone(cid,e))continue;const w=(e.a||{}).w;if(!w)continue;const key=norm(w);if(have.has(key)||seen.has(key))continue;seen.add(key);out.push(e);if(out.length>=12)break}
    if(!out.length)return;
    host.innerHTML=`<section class="px-sec">${sectionHead(t('shQueue'),L0()==='es'?'Se desbloquean al terminar los episodios.':'Desbloqueiam quando você concluir os episódios.')}<div class="px-rail">${out.map(e=>workCard({w:e.a.w,au:'',k:e.a.k},0,true)).join('')}</div></section>`;
  }).catch(()=>{});
}
document.addEventListener('click',ev=>{
  if(typeof P!=='undefined'&&P)return;
  const bk=ev.target.closest('[data-bk]');if(bk){shelfSheet(+bk.dataset.bk);return}
  const sb=ev.target.closest('[data-p4s]');if(sb&&PU().cur==='shelf'){SH.sort=sb.dataset.p4s;document.querySelectorAll('[data-p4s]').forEach(x=>x.setAttribute('aria-pressed',x===sb));const c=document.getElementById('p4case');if(c)c.innerHTML=shelfRowsHTML()}
});

/* ================= PAINEL DO ESTUDANTE ================= */
const LEAGUE_MIN=[0,500,2000,5000,10000];
window.profile=function(){
  PU().cur='profile';setHash('#/profile');
  const L=L0(),u=me(),s=PU().checkAch(true),ACH=PU().ACH;
  let earned={};try{earned=store.get('ach',{})||{}}catch(e){}
  const lg=PU().league(ST.xp||0),nxt=LEAGUE_MIN.find(x=>x>(ST.xp||0));
  const lgp=nxt?((ST.xp||0)-lg.min)/(nxt-lg.min):1;
  const acc=ST.totalAnswered?Math.round(ST.totalCorrect/ST.totalAnswered*100):0;
  let goal=null;try{goal=window.PogSettings&&PogSettings.goalState?PogSettings.goalState():null}catch(e){}
  const due=(()=>{try{return srsDueCount()}catch(e){return 0}})();
  const rows=Object.values(COURSES).map(c=>({c,n:nOf(c.id),d:doneCountFor(c.id)})).filter(r=>r.n&&(r.d||r.c.id===ST.lastCourse)).sort((a,b)=>b.d-a.d);
  const done=ACH.filter(a=>earned[a.id]),todo=ACH.filter(a=>!earned[a.id]);
  const ach=a=>{const cur=Math.min(a.cur(s),a.goal),on=!!earned[a.id];
    return `<div class="p2ach ${on?'on':''}"><i class="ic">${a.ic}</i><div class="tx"><b>${E(a.n[L])}</b><small>${E(a.d[L])}</small>${on?`<span class="when">${IC.check()}${new Date(earned[a.id]).toLocaleDateString(L==='es'?'es':'pt-BR')}</span>`:`<div class="p2bar-p"><i style="width:${(cur/a.goal*100).toFixed(1)}%"></i></div><span class="cnt">${nf(cur)}/${nf(a.goal)}</span>`}</div></div>`};
  const stat=(cls,ic,v,l)=>`<div class="p2stat ${cls}"><i>${ic}</i><div><b>${v}</b><small>${E(l)}</small></div></div>`;
  const px=(cls,ic,v,l)=>`<div class="px-stat ${cls}"><i>${ic}</i><b>${v}</b><small>${E(l)}</small></div>`;
  const todoS=todo.slice().sort((x,y)=>Math.min(y.cur(s),y.goal)/y.goal-Math.min(x.cur(s),x.goal)/x.goal);
  const bd=(a,on)=>{const cur=Math.min(a.cur(s),a.goal);return `<div class="px-badge ${on?'on':''}" title="${E(a.d[L])}" style="--p:${on?100:Math.round(cur/a.goal*100)}"><span class="rg"><i>${a.ic}</i></span><b>${E(a.n[L])}</b><small>${on?'✓ '+new Date(earned[a.id]).toLocaleDateString(L==='es'?'es':'pt-BR'):nf(cur)+'/'+nf(a.goal)}</small></div>`};
  shell(`
  <section class="px-me" style="--lc:${lg.color}">
   <div class="top"><div class="px-av" style="--p:${(Math.max(0,Math.min(1,lgp))*100).toFixed(0)}"><span>${u?E(u.avatar||'🙂'):poggie({scarf:'#6DDFDB'})}</span></div>
    <div class="tx"><span class="px-eyebrow">${E(t('panel'))}</span><h1>${E(u?u.name:t('student'))}</h1><span class="px-lg">${E(t('lg'))} ${E(lg.name)}</span></div>
    <button class="px-gear" data-act="settings" aria-label="Ajustes">${IC.gear()}</button></div>
   <div class="px-lgbar"><div class="p2bar-p inv"><i style="width:${(Math.max(0,Math.min(1,lgp))*100).toFixed(1)}%"></i></div><small>${nxt?`${nf(nxt-(ST.xp||0))} XP ${E(t('toNext'))}`:E(t('top'))}</small></div>
   <div class="px-key"><div><b data-cu>${nf(s.streak)}</b><small>${E(t('sBest'))}</small></div><div><b data-cu>${nf(ST.xp||0)}</b><small>XP</small></div><div><b data-cu>${nf(s.eps)}</b><small>${E(t('sEps'))}</small></div></div></section>
  ${window.PogRecap?PogRecap.cardHTML():''}
  <section class="px-stats">${px('s4',IC.target(),acc+'%',t('sAcc'))}${px('s5',IC.book(),nf(ST.shelf.length),t('sBooks'))}${px('s6',IC.trophy(),`${done.length}/${ACH.length}`,t('ach'))}</section>
  <section class="p2duo">
   ${goal?`<div class="p2card goal"><div class="ring">${PogSettings.ringHTML(goal.pct,72,9)}<span>${Math.round(goal.pct*100)}%</span></div><div><small>${E(t('goal'))}</small><b>${nf(goal.xp)} / ${nf(goal.goal)} XP</b>${goal.met?`<em>${E(t('goalDone'))}</em>`:''}</div></div>`:''}
   <div class="p2card srs"><div><small>${E(t('review2'))}</small><b>${due?`${due} ${E(t('review2Sub'))}`:E(t('review2None'))}</b></div>${due?`<button class="p2btn pri sm" data-go="review">${E(t('review2Go'))}</button>`:''}</div></section>
  <section class="px-sec">${sectionHead(t('myCourses'),t('myCoursesSub'))}${rows.length?`<div class="p2crs">${rows.map(({c,n,d})=>{const l=langOf(c.id),p=n?d/n:0,lv=lvlOf(c.id);return `<button class="p2crow" data-course="${c.id}" style="--c:${l.c};--cd:${l.cd}"><span class="mono">${E(l.mono)}</span><span class="tx"><b>${E(l.n[L])}${lv?' · '+E(lv):''}</b><small>${nf(d)} ${E(t('of'))} ${nf(n)} ${E(t('lessons'))}</small>${bar(p)}</span><em>${Math.round(p*100)}%</em></button>`}).join('')}</div>`:`<div class="p2sh-empty"><p>${E(t('noCourses'))}</p><button class="p2btn pri sm" data-go="courses">${E(t('pick'))}</button></div>`}</section>
  <section class="px-sec" id="p2ach">${sectionHead(t('ach'),`${done.length} ${E(t('of'))} ${ACH.length} · ${E(t('achSub'))}`)}
   <div class="px-badges">${done.map(a=>bd(a,true)).join('')}${todoS.map((a,i)=>`<div class="px-bw ${i>=8?'more':''}">${bd(a,false)}</div>`).join('')}</div>
   ${todoS.length>8?`<button class="px-more" data-pxmore>${E(L==='es'?'Ver todos':'Ver todas')} (${todoS.length-8})</button>`:''}</section>
  <section class="px-sec">${sectionHead(t('acc'))}<div class="p2card acct">${u?`<span class="av">${E(u.avatar||'🙂')}</span><div class="tx"><small>${E(t('accIn'))}</small><b>${E(u.name)}</b><small>${E(u.email||'')}</small></div><button class="p2btn ghost sm" data-go="logout">${E(t('out'))}</button>`
     :`<div class="tx"><b>${E(t('acc2'))}</b></div><button class="p2btn pri sm" data-go="auth">${E(t('signin'))}</button>`}</div></section>`,'panel');
};
document.addEventListener('click',e=>{const m=e.target.closest&&e.target.closest('[data-pxmore]');if(!m)return;const g=document.querySelector('.px-badges');if(g){g.classList.toggle('all');m.style.display='none'}});


/* ================= PÁGINA CURSOS (menu superior) ================= */
function card5(l,i,big){
  let n=0,d=0,av=0;l.sub.forEach(c=>{n+=nOf(c);d+=doneCountFor(c);av+=(window.EP_AVAILABLE&&EP_AVAILABLE[c]&&EP_AVAILABLE[c].available!=null)?EP_AVAILABLE[c].available:nOf(c)});
  const g=GROUPS[l.id]||COURSES[l.id]||{},p=n?d/n:0,multi=l.sub.length>1,hd=multi?`data-lang="${l.id}"`:`data-course="${l.sub[0]}"`;
  const neighbors=/^nb/.test(l.id),mode=neighbors?t('neighbors'):t('regular');
  const chips=multi?`<div class="lvs">${l.sub.map(cid=>`<button class="lv ${doneCountFor(cid)?'on':''}" data-course="${cid}" title="${E(COURSES[cid].name[L0()])}">${E(lvlOf(cid))}</button>`).join('')}</div>`
    :`<button class="p2btn soft sm go" data-course="${l.sub[0]}">${E(d?t('continue'):t('begin'))}${IC.arrow()}</button>`;
  return `<article class="p5c ${big?'big':''} ${neighbors?'is-neighbors':'is-regular'}" style="--c:${l.c};--cd:${l.cd};--cl:${l.cl};animation-delay:${i*50}ms">
   <button class="ban" ${hd} tabindex="-1" aria-hidden="true">${sceneArt(l.id+(big?'b':''),LANG_SC[l.id]||'plaza')}<span class="sh"></span></button>
   <button class="top" ${hd}><span class="mk">${E(l.mono)}</span><span class="nm"><span class="p5mode">${E(mode)}</span><h3>${E(l.n[L0()])}</h3><small>${multi?'A1–C2':E(lvlOf(l.sub[0])||'')} · ${nf(av)} ${E(t('available'))||'disponíveis'}${av<n?' · '+nf(n)+' '+E(t('planned')):''}</small></span><span class="ar">${IC.arrow()}</span></button>
   <p>${E(g.desc?g.desc[L0()]:'')}</p>
   <div class="pr"><div class="p2bar-p">${''}<i style="width:${(p*100).toFixed(1)}%"></i></div><b>${Math.round(p*100)}%</b></div>${chips}</article>`;
}
window.coursesPage=function(){
  PU().cur='courses';setHash('#/courses');
  const ls=PU().LANGS,nb=ls.filter(l=>/^nb(es|fr|de|pt|ja|eng|it)?$/.test(l.id)),rest=ls.filter(l=>!/^nb(es|fr|de|pt|ja|eng|it)?$/.test(l.id));
  const order=['en','es','fr','de','it','pt','enes'];rest.sort((a,b)=>order.indexOf(a.id)-order.indexOf(b.id));
  shell(`<header class="p3ch"><span class="p2eyebrow">${E(t('navCourses').toUpperCase())}</span><h1>${E(t('coursesPage'))}</h1><p>${E(t('coursesPageSub'))}</p></header>
  <section class="p3nbsec">${sectionHead(t('nbSec'),t('nbSecSub'))}<div class="p5grid two">${nb.map((l,i)=>card5(l,i,true)).join('')}</div></section>
  <section class="p3sec">${sectionHead(t('clSec'),t('clSecSub'))}<div class="p5grid">${rest.map((l,i)=>card5(l,i)).join('')}</div></section>`,'courses');
};

/* ================= ROTEAMENTO ================= */
const go0=PU().go;
PU().go=function(name){
  const [a,b]=String(name).split(':');
  if(a==='home')return window.home(),true;
  if(a==='courses')return window.coursesPage(),true;
  if(a==='episodes')return openEpisodes(),true;
  if(a==='shelf')return shelf(),true;
  if(a==='profile')return window.profile(),true;
  if(a==='ach'){window.profile();setTimeout(()=>{const x=document.getElementById('p2ach');if(x)x.scrollIntoView({behavior:'smooth',block:'start'})},60);return true}
  if(a==='comm'){if(window.PogComm)PogComm.open(b||'rank');return true}
  return go0.call(this,name);
};
PU().mountNav=mountNav;
PU().T2=t;
PU().openEpisodes=openEpisodes;
PU().shelf=shelf;
try{document.body.classList.add('p2on')}catch(e){}
})();
