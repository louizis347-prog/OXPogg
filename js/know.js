/* Pogglot · painel "O que eu já sei"
   Mostra, por idioma: quantas palavras, expressões e estruturas o aluno já aprendeu, como está a memória
   dessas palavras (revisão espaçada) e quanto ele já entende de séries e livros (inglês).
   Carregado depois de ui.js. Dados de compreensão: data/know-en.json (frequência de palavras em legendas
   de filmes/séries + texto de livros em domínio público). */
(function(){
'use strict';
const L0=()=>ST.homeLang==='es'?'es':'pt';
const esc=s=>String(s==null?'':s).replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]));
const fmt=n=>Number(n).toLocaleString(L0()==='es'?'es-ES':'pt-BR');
const reduceMotion=()=>{try{return matchMedia('(prefers-reduced-motion: reduce)').matches}catch(e){return false}};

/* ---------- textos ---------- */
const K={
 pt:{title:'O que eu já sei',sub:'Tudo o que você já aprendeu, em números de verdade.',back:'Voltar',
  words:'palavras',exprs:'expressões',structs:'estruturas',
  deltaYes:'Desde sua última visita',deltaNone:'Este é o seu ponto de partida. Volte depois para ver o quanto você cresceu.',deltaSame:'Nada novo desde a última visita. Que tal um episódio hoje?',
  cta1:'O que eu já sei',ctaGo:'Ver',ctaTxt:'Veja quantas palavras e estruturas você já domina e quanto já entende de séries e livros.',ctaTxtN:(w)=>`${w} palavras na memória · veja quanto você já entende de séries e livros`,
  mediaH:'Quanto você entende',mediaP:'Quanto das palavras de cada obra você já reconhece. Com 90% dá para acompanhar a história; com 95% fica confortável.',
  tv:'Séries como Friends',tvSub:'Comédias e falas rápidas do dia a dia',
  alice:'Alice no País das Maravilhas',aliceSub:'Livro · Lewis Carroll · 1865',emma:'Emma',emmaSub:'Livro · Jane Austen · 1815',moby:'Moby-Dick',mobySub:'Livro · Herman Melville · 1851 · desafio',
  tick90:'acompanha',tick95:'confortável',
  st0:'Ainda difícil de acompanhar',st1:'Dá para acompanhar a história',st2:'Você assiste com conforto',
  need:(n)=>`Faltam ~${fmt(n)} palavras para chegar a 95%`,needMany:'Ainda falta bastante vocabulário para chegar a 95%',needDone:'Você já passou dos 95%!',
  noCov:'A estimativa de compreensão por obra está disponível para o inglês. Para este idioma você acompanha aqui palavras, expressões e estruturas.',
  covErr:'Não deu para carregar os dados de compreensão agora. Confira sua conexão e tente de novo.',retry:'Tentar de novo',
  memH:'Seu vocabulário na memória',memP:'Cada palavra e expressão vira um cartão de revisão. Quanto mais você acerta em dias diferentes, mais firme ela fica.',
  tNew:'Novas',tFix:'Fixando',tFirm:'Firmes',tNewD:'acabou de aprender',tFixD:'em fixação',tFirmD:'acertou em vários dias',
  review:(n)=>`Revisar ${n} agora`,deck:'Abrir baralho',allSet:'Tudo em dia na revisão!',
  recentH:'Aprendidas por último',
  strH:'Estruturas que você domina',strP:'Padrões de frase que você já estudou.',next:'Próximas na trilha',more:(n)=>`Ver todas (${n})`,less:'Ver menos',
  emptyH:'Seu painel começa no primeiro episódio',emptyP:'Conclua um episódio e suas primeiras palavras e estruturas aparecem aqui.',emptyGo:'Começar agora',
  howH:'Como calculamos',
  how:'A compreensão é uma estimativa. Contamos as palavras que apareceram nas lições que você concluiu (vocabulário, diálogos e exemplos) e vemos que parte do texto elas cobrem. Para séries, usamos a frequência das palavras em legendas de filmes e séries (OpenSubtitles); para livros, o texto completo de obras em domínio público (Project Gutenberg). Nomes próprios contam como conhecidos. Não usamos roteiros de séries, que têm direitos autorais. Reconhecer 95% das palavras não garante entender tudo, mas é o ponto em que estudos de leitura e escuta mostram que a compreensão fica confortável.',
  langs:'Idioma',pts:'pts'},
 es:{title:'Lo que ya sé',sub:'Todo lo que ya aprendiste, en números de verdad.',back:'Volver',
  words:'palabras',exprs:'expresiones',structs:'estructuras',
  deltaYes:'Desde tu última visita',deltaNone:'Este es tu punto de partida. Vuelve después para ver cuánto creciste.',deltaSame:'Nada nuevo desde la última visita. ¿Un episodio hoy?',
  cta1:'Lo que ya sé',ctaGo:'Ver',ctaTxt:'Mira cuántas palabras y estructuras ya dominas y cuánto entiendes de series y libros.',ctaTxtN:(w)=>`${w} palabras en la memoria · mira cuánto entiendes de series y libros`,
  mediaH:'Cuánto entiendes',mediaP:'Qué parte de las palabras de cada obra ya reconoces. Con 90% puedes seguir la historia; con 95% estás cómodo.',
  tv:'Series como Friends',tvSub:'Comedias y diálogos rápidos del día a día',
  alice:'Alicia en el País de las Maravillas',aliceSub:'Libro · Lewis Carroll · 1865',emma:'Emma',emmaSub:'Libro · Jane Austen · 1815',moby:'Moby Dick',mobySub:'Libro · Herman Melville · 1851 · desafío',
  tick90:'sigues la trama',tick95:'cómodo',
  st0:'Todavía difícil de seguir',st1:'Ya puedes seguir la historia',st2:'La ves con comodidad',
  need:(n)=>`Faltan ~${fmt(n)} palabras para llegar a 95%`,needMany:'Aún falta bastante vocabulario para llegar a 95%',needDone:'¡Ya pasaste el 95%!',
  noCov:'La estimación de comprensión por obra está disponible para el inglés. En este idioma sigues aquí palabras, expresiones y estructuras.',
  covErr:'No se pudieron cargar los datos de comprensión ahora. Revisa tu conexión e inténtalo de nuevo.',retry:'Reintentar',
  memH:'Tu vocabulario en la memoria',memP:'Cada palabra y expresión se vuelve una tarjeta de repaso. Cuanto más aciertas en días distintos, más firme queda.',
  tNew:'Nuevas',tFix:'Afianzando',tFirm:'Firmes',tNewD:'recién aprendidas',tFixD:'afianzando',tFirmD:'acertaste varios días',
  review:(n)=>`Repasar ${n} ahora`,deck:'Abrir mazo',allSet:'¡Todo al día en el repaso!',
  recentH:'Aprendidas por último',
  strH:'Estructuras que dominas',strP:'Patrones de frase que ya estudiaste.',next:'Próximas en la ruta',more:(n)=>`Ver todas (${n})`,less:'Ver menos',
  emptyH:'Tu panel empieza en el primer episodio',emptyP:'Termina un episodio y tus primeras palabras y estructuras aparecen aquí.',emptyGo:'Empezar ahora',
  howH:'Cómo calculamos',
  how:'La comprensión es una estimación. Contamos las palabras que aparecieron en las lecciones que terminaste (vocabulario, diálogos y ejemplos) y vemos qué parte del texto cubren. Para series usamos la frecuencia de palabras en subtítulos de películas y series (OpenSubtitles); para libros, el texto completo de obras de dominio público (Project Gutenberg). Los nombres propios cuentan como conocidos. No usamos guiones de series, que tienen derechos de autor. Reconocer 95% de las palabras no garantiza entenderlo todo, pero es el punto en que los estudios de lectura y escucha muestran una comprensión cómoda.',
  langs:'Idioma',pts:'pts'}
};
const k=key=>{const v=K[L0()][key];return v!=null?v:K.pt[key]};

/* ---------- tokenização e famílias de palavras (inglês) ---------- */
const IRR={};
function irr(base,forms){forms.split(' ').forEach(f=>{IRR[f]=base})}
irr('be',"am is are was were been being 's 'm 're ain isn aren wasn weren");
irr('have',"has had having 've hasn haven hadn");
irr('do',"does did done doing don didn doesn");
irr('will',"'ll won");irr('would',"'d wouldn");irr('could',"couldn");irr('should',"shouldn");irr('must',"mustn");irr('need',"needn");irr('not',"'t");
irr('go',"goes went gone going");irr('say',"says said saying");irr('get',"gets got gotten getting");irr('make',"makes made making");
irr('know',"knows knew known knowing");irr('think',"thinks thought thinking");irr('take',"takes took taken taking");irr('see',"sees saw seen seeing");
irr('come',"comes came coming");irr('give',"gives gave given giving");irr('find',"finds found finding");irr('tell',"tells told telling");
irr('feel',"feels felt feeling");irr('leave',"leaves left leaving");irr('keep',"keeps kept keeping");irr('begin',"begins began begun beginning");
irr('eat',"eats ate eaten eating");irr('drink',"drinks drank drunk drinking");irr('write',"writes wrote written writing");irr('run',"runs ran running");
irr('sit',"sits sat sitting");irr('stand',"stands stood standing");irr('buy',"buys bought buying");irr('bring',"brings brought bringing");
irr('hear',"hears heard hearing");irr('meet',"meets met meeting");irr('pay',"pays paid paying");irr('send',"sends sent sending");
irr('spend',"spends spent spending");irr('understand',"understands understood understanding");irr('lose',"loses lost losing");
irr('speak',"speaks spoke spoken speaking");irr('sleep',"sleeps slept sleeping");irr('wake',"wakes woke woken waking");irr('fall',"falls fell fallen falling");
irr('grow',"grows grew grown growing");irr('draw',"draws drew drawn drawing");irr('drive',"drives drove driven driving");irr('ride',"rides rode ridden riding");
irr('fly',"flies flew flown flying");irr('swim',"swims swam swum swimming");irr('sing',"sings sang sung singing");irr('choose',"chooses chose chosen choosing");
irr('break',"breaks broke broken breaking");irr('forget',"forgets forgot forgotten forgetting");irr('hold',"holds held holding");irr('lead',"leads led leading");
irr('teach',"teaches taught teaching");irr('catch',"catches caught catching");irr('fight',"fights fought fighting");irr('build',"builds built building");
irr('sell',"sells sold selling");irr('wear',"wears wore worn wearing");irr('throw',"throws threw thrown throwing");irr('hide',"hides hid hidden hiding");
irr('let',"lets letting");irr('put',"puts putting");irr('cut',"cuts cutting");irr('set',"sets setting");irr('hit',"hits hitting");
irr('i',"me my mine myself");irr('you',"your yours yourself yourselves");irr('he',"him his himself");irr('she',"her hers herself");
irr('it',"its itself");irr('we',"us our ours ourselves");irr('they',"them their theirs themselves");
irr('this',"these");irr('that',"those");irr('good',"better best");irr('bad',"worse worst");irr('much',"more most many");irr('little',"less least");
irr('child',"children");irr('man',"men");irr('woman',"women");irr('person',"people");irr('foot',"feet");irr('tooth',"teeth");irr('mouse',"mice");irr('life',"lives");
const DBL=/(bb|gg|mm|nn|pp|rr|tt)$/;
function norm(s){
  const n=s.length;
  if(n<=3)return s;
  if(/ies$/.test(s)&&n>4)s=s.slice(0,-3)+'y';
  else if(/(ss|us|is)$/.test(s)){}
  else if(/(ch|sh|x|z)es$/.test(s)||/oes$/.test(s))s=s.slice(0,-2);
  else if(/s$/.test(s))s=s.slice(0,-1);
  if(/iness$/.test(s)&&s.length>6)s=s.slice(0,-5)+'y';
  else if(/ness$/.test(s)&&s.length>6)s=s.slice(0,-4);
  if(/ily$/.test(s)&&s.length>5)s=s.slice(0,-3)+'y';
  else if(/ly$/.test(s)&&s.length>4)s=s.slice(0,-2);
  if(/ied$/.test(s)&&s.length>4)s=s.slice(0,-3)+'y';
  else if(/(ier|iest)$/.test(s)&&s.length>5)s=s.replace(/(ier|iest)$/,'y');
  else if(/ing$/.test(s)&&s.length>5){s=s.slice(0,-3);if(DBL.test(s))s=s.slice(0,-1);}
  else if(/ed$/.test(s)&&s.length>4){s=s.slice(0,-2);if(DBL.test(s))s=s.slice(0,-1);}
  if(s.length>3&&/e$/.test(s))s=s.slice(0,-1);
  if(s.length>3&&/y$/.test(s))s=s.slice(0,-1)+'i';
  return s;
}
const stemCache=new Map();
function stem(w){let r=stemCache.get(w);if(r!==undefined)return r;r=norm(IRR[w]||w);stemCache.set(w,r);return r}
const toks=str=>String(str==null?'':str).toLowerCase().replace(/[’‘`]/g,"'").match(/[a-z]+|'[a-z]+/g)||[];
const FREE=new Set("oh uh um mm hmm ah ooh huh ha ow ugh whoa wow hey ok okay yeah yep nope shh aw aww oops hm eh mmm uhh ohh ahh".split(' '));

/* texto em inglês que o aluno viu num episódio concluído */
function englishStrings(e){
  const out=[];
  (e.v||[]).forEach(v=>{if(v&&v[0])out.push(plain(v[0]))});
  if(e.h&&e.h.l)out.push(e.h.l);
  (e.fr||[]).forEach(f=>{if(!f)return;
    switch(f.k){
      case 'cult1':(f.lines||[]).forEach(l=>{if(l&&l[0])out.push(plain(l[0]))});break;
      case 'cwords':(f.items||[]).forEach(i=>{if(i&&i[0])out.push(i[0])});break;
      case 'cover':if(f.hook&&f.hook[0])out.push(f.hook[0]);break;
      case 'scene':(f.lines||[]).forEach(l=>{if(l&&l[1])out.push(l[1])});break;
      case 'words':(f.items||[]).forEach(i=>{if(i&&i[0])out.push(i[0])});break;
      case 'chunk':(f.blocks||[]).forEach(b=>{if(b&&b[0])out.push(b[0])});(f.variants||[]).forEach(v=>{if(v&&v[0])out.push(v[0])});break;
      case 'grammar':(f.examples||[]).forEach(x=>{if(x&&x[0])out.push(plain(x[0]))});(f.tiles||[]).forEach(t=>{if(Array.isArray(t))t.forEach(s=>out.push(s))});break;
      case 'build':(f.items||[]).forEach(i=>{if(i&&i[0])out.push(i[0])});break;
      case 'dictate':(f.lines||[]).forEach(l=>{if(l&&l[0])out.push(l[0])});break;
      case 'order':(f.lines||[]).forEach(l=>{if(l&&l[1])out.push(l[1])});break;
      case 'wrap':(f.recap||[]).forEach(r=>{if(r&&r[0])out.push(r[0])});break;
      case 'convo':(f.turns||[]).forEach(t=>{if(t.npc&&t.npc[0])out.push(t.npc[0]);(t.opts||[]).forEach(o=>{if(o&&o[0])out.push(o[0])})});break;
      case 'ctx':(f.items||[]).forEach(it=>(it.lines||[]).forEach(l=>{if(l&&l[1])out.push(String(l[1]).replace(/_+/g,' '))}));break;
    }
  });
  return out;
}

/* ---------- dados de compreensão (inglês) ---------- */
let COV=null,COV_P=null;
function loadCov(){
  if(COV)return Promise.resolve(COV);
  if(COV_P)return COV_P;
  COV_P=fetch('data/know-en.json').then(r=>{if(!r.ok)throw new Error('http '+r.status);return r.json()}).then(d=>{
    const W=d.tv.w,tvStem=new Array(W.length);
    for(let i=0;i<W.length;i++)tvStem[i]=stem(W[i]);
    const nm=new Set(d.tv.nm||[]);
    d.books.forEach(b=>{b.st=b.w.map(x=>stem(x[0]))});
    COV={d,tvStem,nm};return COV;
  }).catch(e=>{COV_P=null;throw e});
  return COV_P;
}
/* cobertura de uma lista (formas, contagens, famílias): devolve % e quantas famílias faltam para cada meta */
function coverage(items,known,total,fixed,targets){
  let hit=fixed||0;const unk=new Map();
  for(let i=0;i<items.length;i++){const it=items[i];
    if(it.free||known.has(it.s))hit+=it.c;else unk.set(it.s,(unk.get(it.s)||0)+it.c)}
  const pct=hit/total,fam=[...unk.values()].sort((a,b)=>b-a),need={};
  for(const t of targets){
    if(pct>=t){need[t]=0;continue}
    let h=hit,n=0,r=-1;for(const c of fam){h+=c;n++;if(h/total>=t){r=n;break}}
    need[t]=r;
  }
  return{pct,need};
}
function mediaCoverage(cv,known){
  const d=cv.d,T=[.9,.95],rows=[];
  const tvItems=d.tv.w.map((w,i)=>({s:cv.tvStem[i],c:d.tv.c[i],free:FREE.has(w)||cv.nm.has(w)}));
  rows.push(Object.assign({id:'tv',ico:'📺'},coverage(tvItems,known,d.tv.t,0,T)));
  const ico={alice:'🐇',emma:'🎩',moby:'🐋'};
  d.books.forEach(b=>{
    const items=b.w.map((x,i)=>({s:b.st[i],c:x[1]}));
    rows.push(Object.assign({id:b.id,ico:ico[b.id]||'📖'},coverage(items,known,b.tot,b.prop,T)));
  });
  return rows;
}

/* ---------- cálculo do painel ---------- */
const langOfCourse=cid=>{const c=COURSES[cid];return (c&&(c.group||c.id))||cid.split('-')[0]};
const lvOf=cid=>{const m=/^(?:en|es)-(a1|a2|b1|b2|c1|c2)$/.exec(cid);return m?m[1].toUpperCase():''};
function shortStruct(t){
  t=plain(t||'').trim();
  if(t.length<=54)return t;
  const p=t.search(/\s*\(/);
  if(p>12&&p<=54)return t.slice(0,p);
  return t.slice(0,52).replace(/[\s,;+]+\S*$/,'')+'…';
}
function compute(l){
  try{srsBackfill()}catch(e){}
  const isEn=l.id==='en',words=new Map(),exprs=new Map(),structs=new Map(),known=new Set();
  let doneEps=0;const recent=[];
  for(const cid of l.sub){
    const eps=EP[cid];if(!eps)continue;
    for(const e of eps){
      if(isPlannedEpisode(e)||!ST.done[cid+'-'+e.n])continue;
      doneEps++;
      (e.v||[]).forEach(v=>{
        if(!v||!v[0])return;
        const w=plain(v[0]).trim(),key=w.toLowerCase();if(!key)return;
        const multi=/\s/.test(w);
        const bag=multi?exprs:words;
        const card=ST.srs&&ST.srs[srsKey(cid,w)];
        const b=card?card.b:0;
        const cur=bag.get(key);
        if(!cur){bag.set(key,{w,m:plain(v[1]||''),b});if(!multi)recent.push(key)}
        else if(b>cur.b)cur.b=b;
      });
      if(e.g&&e.g.t){const t=plain(e.g.t).trim(),key=t.toLowerCase();if(key&&!structs.has(key))structs.set(key,{t:shortStruct(t),full:t,lv:lvOf(cid)})}
      if(isEn){try{englishStrings(e).forEach(s=>toks(s).forEach(w=>known.add(stem(w))))}catch(err){}}
    }
  }
  const items=[...words.values(),...exprs.values()];
  const tiers={n:0,f:0,s:0};
  items.forEach(x=>{if(x.b>=4)tiers.s++;else if(x.b>=2)tiers.f++;else tiers.n++});
  // próximas estruturas na trilha atual
  const next=[];
  const cur=(ST.lastCourse&&l.sub.includes(ST.lastCourse))?ST.lastCourse:(l.sub.find(cid=>EP[cid]&&EP[cid].some(e=>!isPlannedEpisode(e)&&!ST.done[cid+'-'+e.n]))||l.sub[0]);
  const ceps=EP[cur]||[];
  for(const e of ceps){if(next.length>=4)break;if(isPlannedEpisode(e)||ST.done[cur+'-'+e.n])continue;if(e.g&&e.g.t){const t=shortStruct(e.g.t);if(!next.includes(t))next.push(t)}}
  return{l,isEn,words:words.size,exprs:exprs.size,structs:[...structs.values()],tiers,total:items.length,known,doneEps,
    recent:recent.slice(-14).reverse().map(k=>words.get(k)),next};
}

/* ---------- histórico (para "desde sua última visita") ---------- */
const dayNum=()=>Math.floor((Date.now()-new Date().getTimezoneOffset()*60000)/86400000);
function snapDelta(lid,now){
  const all=store.get('know',{}),arr=all[lid]||[],t=dayNum();
  const prev=[...arr].reverse().find(s=>s.d<t);
  const same=arr.find(s=>s.d===t);
  const next=arr.filter(s=>s.d!==t);
  next.push(Object.assign({d:t},now));
  all[lid]=next.slice(-60);
  store.set('know',all);
  // se hoje já havia um registro anterior, o delta continua sendo contra o último dia anterior
  return prev||null;
}

/* ---------- estilos ---------- */
function injectCss(){
  if(document.getElementById('kn-css'))return;
  const s=document.createElement('style');s.id='kn-css';
  s.textContent=`
.kn{max-width:1120px;margin:0 auto;padding:22px 16px 0}
.kn *{box-sizing:border-box}
.kn-head{display:flex;align-items:flex-end;justify-content:space-between;gap:12px;flex-wrap:wrap;margin:6px 0 14px}
.kn-head h1{font:800 clamp(28px,5vw,40px)/1.05 var(--f-display);margin:0;letter-spacing:-.02em}
.kn-head p{margin:6px 0 0;color:var(--pg-mute);font-weight:700}
.kn-tabs{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 14px}
.kn-tab{display:inline-flex;align-items:center;gap:8px;padding:8px 14px;border-radius:999px;border:2px solid var(--pg-line);background:#fff;font-weight:900;font-size:14px;color:var(--pg-ink)}
.kn-tab i{width:10px;height:10px;border-radius:50%;background:var(--c,#6DDFDB)}
.kn-tab[aria-pressed="true"]{border-color:var(--c,#6DDFDB);background:var(--cl,#EDFCFB)}
.kn-hero{position:relative;border-radius:28px;padding:24px;color:#fff;overflow:hidden;background:linear-gradient(135deg,var(--c,#6DDFDB) 0%,var(--c2,#86E4E1) 55%,#FF7AB6 130%);box-shadow:0 18px 40px -22px rgba(36,48,73,.7)}
.kn-hero::after{content:"";position:absolute;right:-60px;top:-60px;width:220px;height:220px;border-radius:50%;background:rgba(255,255,255,.12)}
.kn-nums{position:relative;z-index:1;display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.kn-n b{display:block;font:800 clamp(38px,8vw,64px)/1 var(--f-display);letter-spacing:-.03em;font-variant-numeric:tabular-nums}
.kn-n small{display:block;margin-top:4px;font-weight:900;font-size:13px;letter-spacing:.08em;text-transform:uppercase;opacity:.92}
.kn-delta{position:relative;z-index:1;margin:18px 0 0;display:flex;gap:8px;flex-wrap:wrap;align-items:center;font-weight:800;font-size:14px}
.kn-chip{display:inline-flex;align-items:center;gap:6px;padding:5px 12px;border-radius:999px;background:rgba(255,255,255,.2);border:1.5px solid rgba(255,255,255,.35);font-weight:900;font-size:13px}
.kn-sec{display:flex;align-items:end;justify-content:space-between;gap:12px;margin:30px 0 12px;flex-wrap:wrap}
.kn-sec h2{font:800 26px/1.1 var(--f-display);margin:0}
.kn-sec p{margin:4px 0 0;color:var(--pg-mute);font-weight:600;max-width:70ch;font-size:14.5px}
.kn-card{background:#fff;border:2px solid var(--pg-line);border-radius:20px;box-shadow:var(--pg-shadow);padding:18px}
.kn-media{display:grid;gap:12px}
.kn-row{display:grid;grid-template-columns:auto 1fr auto;gap:6px 14px;align-items:center}
.kn-row .ic{width:52px;height:52px;border-radius:16px;display:grid;place-items:center;font-size:28px;background:var(--tint,#EDFCFB)}
.kn-row h3{margin:0;font:800 17px/1.2 var(--f-display)}
.kn-row .sb{display:block;color:var(--pg-mute);font-weight:700;font-size:12.5px;margin-top:2px}
.kn-row .pc{font:800 34px/1 var(--f-display);letter-spacing:-.02em;font-variant-numeric:tabular-nums;color:var(--sc,#243049);text-align:right}
.kn-row .pc small{font-size:18px}
.kn-row.big .ic{width:64px;height:64px;font-size:34px;border-radius:20px}
.kn-row.big h3{font-size:21px}
.kn-row.big .pc{font-size:52px}
.kn-bar{grid-column:1/-1;position:relative;height:16px;border-radius:99px;background:#EDF0F7;margin:8px 0 22px}
.kn-bar i{position:absolute;inset:0 auto 0 0;width:0;border-radius:99px;background:var(--sc,#6DDFDB);transition:width 1.1s cubic-bezier(.2,.8,.2,1)}
.kn-bar i::after{content:"";position:absolute;left:8px;right:8px;top:3px;height:4px;border-radius:99px;background:rgba(255,255,255,.4)}
.kn-bar u{position:absolute;top:-4px;bottom:-4px;width:3px;border-radius:2px;background:#243049;opacity:.55;text-decoration:none}
.kn-bar u span{position:absolute;top:26px;right:-1px;white-space:nowrap;font:800 11px var(--f-ui);color:var(--pg-mute)}
.kn-bar u.t95 span{right:auto;left:-1px}
.kn-row .ft{grid-column:1/-1;display:flex;gap:8px 14px;flex-wrap:wrap;align-items:center;font-weight:800;font-size:13px}
.kn-row .stt{padding:3px 10px;border-radius:99px;background:var(--stl,#EDFCFB);color:var(--sc,#42BACD)}
.kn-row .nd{color:var(--pg-mute)}
.kn-hr{height:2px;background:var(--pg-line);border:0;margin:6px 0}
.kn-tiers{display:flex;height:22px;border-radius:99px;overflow:hidden;background:#EDF0F7;margin:4px 0 14px}
.kn-tiers i{display:block;height:100%;width:0;transition:width 1s cubic-bezier(.2,.8,.2,1)}
.kn-leg{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.kn-leg div{padding:10px 12px;border-radius:14px;background:var(--lb)}
.kn-leg b{display:block;font:800 24px/1 var(--f-display);font-variant-numeric:tabular-nums}
.kn-leg span{display:block;font-weight:900;font-size:13px;margin-top:2px}
.kn-leg small{display:block;color:var(--pg-mute);font-weight:700;font-size:12px}
.kn-mem{display:flex;gap:12px;align-items:center;flex-wrap:wrap;margin-top:16px}
.kn-mem .tx{flex:1;min-width:180px;font-weight:700;color:var(--pg-mute);font-size:14px}
.kn-chips{display:flex;flex-wrap:wrap;gap:8px}
.kn-w{display:inline-flex;flex-direction:column;padding:7px 12px;border-radius:14px;background:#F3F6FC;border:2px solid var(--pg-line);line-height:1.2}
.kn-w b{font-weight:900;font-size:14.5px}
.kn-w small{color:var(--pg-mute);font-weight:700;font-size:12px}
.kn-s{display:inline-flex;align-items:center;gap:6px;padding:7px 12px;border-radius:999px;background:var(--cl,#EDFCFB);color:var(--cd,#42BACD);font-weight:800;font-size:13.5px}
.kn-s::before{content:"✓";font-weight:900}
.kn-s.nx{background:#fff;border:2px dashed var(--pg-line);color:var(--pg-mute)}
.kn-s.nx::before{content:"🔒";font-size:12px}
.kn-lv{margin:16px 0 8px;display:flex;align-items:center;gap:8px;font:800 15px var(--f-display)}
.kn-lv:first-child{margin-top:0}
.kn-lv em{font-style:normal;font-family:var(--f-ui);font-weight:900;font-size:12px;padding:2px 9px;border-radius:99px;background:var(--pg-line);color:var(--pg-ink)}
.kn-more{margin-top:10px;font-weight:900;font-size:13px;color:var(--pg-mute);text-decoration:underline;padding:4px 0}
.kn-how{margin-top:26px;border-radius:16px;background:#fff;border:2px solid var(--pg-line);padding:4px 16px}
.kn-how summary{cursor:pointer;font-weight:900;padding:12px 0;list-style:none}
.kn-how summary::-webkit-details-marker{display:none}
.kn-how summary::before{content:"ⓘ  ";color:var(--pg-mute)}
.kn-how p{margin:0 0 14px;color:var(--pg-mute);font-weight:600;font-size:13.5px;line-height:1.55}
.kn-note{padding:14px 16px;border-radius:16px;background:#FFF8DB;border:2px solid #FFE58A;color:#7A5B00;font-weight:700;font-size:14px}
.kn-note.err{background:#FDE3E9;border-color:#F5B5C2;color:#8A1D29}
.kn-note button{margin-left:10px;font-weight:900;text-decoration:underline}
.kn-empty{text-align:center;padding:36px 18px}
.kn-empty .e{font-size:52px}
.kn-empty h2{font:800 24px var(--f-display);margin:8px 0 6px}
.kn-empty p{margin:0 0 16px;color:var(--pg-mute);font-weight:700}
.kn-back{display:inline-flex;align-items:center;gap:6px;font-weight:800;color:var(--pg-mute);padding:6px 4px}
.kn-back:hover{color:var(--pg-ink)}
.kn-cta{display:flex;align-items:center;gap:14px;width:100%;text-align:left;margin-top:16px;padding:14px 16px;border-radius:20px;background:#fff;border:2px solid var(--pg-line);box-shadow:var(--pg-shadow);transition:transform .15s,border-color .2s}
.kn-cta:hover{transform:translateY(-2px);border-color:#6DDFDB}
.kn-cta .ic{flex:none;width:48px;height:48px;border-radius:16px;display:grid;place-items:center;font-size:26px;background:linear-gradient(135deg,#EDFCFB,#FDE6F3)}
.kn-cta b{display:block;font:800 17px var(--f-display)}
.kn-cta small{display:block;color:var(--pg-mute);font-weight:700;font-size:13px;margin-top:2px}
.kn-cta .go{margin-left:auto;flex:none;font-weight:900;color:#6DDFDB;white-space:nowrap}
@media(max-width:620px){
 .kn-hero{padding:18px;border-radius:24px}
 .kn-row{grid-template-columns:auto 1fr}
 .kn-row .pc{grid-column:2;text-align:left;font-size:30px}
 .kn-row.big .pc{font-size:44px}
 .kn-leg{grid-template-columns:1fr}
 .kn-cta .go{display:none}
}
@media(prefers-reduced-motion:reduce){.kn-bar i,.kn-tiers i{transition:none}}
`;
  document.head.appendChild(s);
}

/* ---------- tela ---------- */
const MEDIA_ORDER=['tv','alice','emma','moby'];
const STATE_COL=['#6DDFDB','#E39A00','#1FAE6B'],STATE_BG=['#EDFCFB','#FFF1CC','#DEF7EA'];
let FROM='home',CUR=null,EXPANDED={},LOADING_LANG=null;

function langsWithProgress(){
  const L=(window.PogUI&&PogUI.LANGS)||[];
  return L.filter(l=>l.sub.some(cid=>doneCountFor(cid)>0));
}
function pickLang(){
  const L=(window.PogUI&&PogUI.LANGS)||[];
  const prog=langsWithProgress();
  if(CUR&&L.some(l=>l.id===CUR))return CUR;
  const last=ST.lastCourse&&langOfCourse(ST.lastCourse);
  if(last&&prog.some(l=>l.id===last))return last;
  return prog.length?prog[0].id:(last&&L.some(l=>l.id===last)?last:'en');
}
function loadFor(l){
  const need=new Set(l.sub.filter(cid=>doneCountFor(cid)>0));
  if(ST.lastCourse&&l.sub.includes(ST.lastCourse))need.add(ST.lastCourse);
  if(!need.size&&l.sub[0])need.add(l.sub[0]);
  return Promise.all([...need].map(ensureLangLoaded));
}

function mediaRowHtml(r,i){
  const pct=Math.max(0,Math.min(100,r.pct*100));
  const st=pct>=95?2:(pct>=90?1:0);
  const L=L0(),big=i===0;
  const shown=pct>0&&pct<1?'<1':String(Math.round(pct));
  const need=r.need[.95];
  const needTxt=need===0?k('needDone'):(need>0?k('need')(need):k('needMany'));
  const tint={tv:'#EDFCFB',alice:'#FDE6F3',emma:'#FFF1CC',moby:'#DDF1FD'}[r.id]||'#EDFCFB';
  return `<div class="kn-card"><div class="kn-row${big?' big':''}" style="--sc:${STATE_COL[st]};--stl:${STATE_BG[st]};--tint:${tint}">
    <div class="ic" aria-hidden="true">${r.ico}</div>
    <div><h3>${esc(k(r.id))}</h3><span class="sb">${esc(k(r.id+'Sub'))}</span></div>
    <div class="pc"><span data-to="${pct.toFixed(1)}" data-dec="0">${shown}</span><small>%</small></div>
    <div class="kn-bar" role="img" aria-label="${esc(k(r.id))}: ${shown}%"><i data-w="${pct.toFixed(2)}"></i><u style="left:90%"><span>90%</span></u><u class="t95" style="left:95%"><span>95%</span></u></div>
    <div class="ft"><span class="stt">${esc(k('st'+st))}</span><span class="nd">${esc(needTxt)}</span></div>
  </div></div>`;
}

function render(data,cov,covErr,delta){
  const L=L0(),l=data.l,prog=langsWithProgress();
  const lc=`--c:${l.c};--cd:${l.cd};--cl:${l.cl};--c2:${l.cd}`;
  const tabs=prog.length>1?`<div class="kn-tabs" role="group" aria-label="${esc(k('langs'))}">${prog.map(x=>`<button class="kn-tab" data-know="lang" data-l="${x.id}" style="--c:${x.c};--cl:${x.cl}" aria-pressed="${x.id===l.id}"><i></i>${esc(x.n[L])}</button>`).join('')}</div>`:'';
  let body='';
  if(!data.doneEps){
    body=`<div class="kn-card kn-empty"><div class="e">🌱</div><h2>${esc(k('emptyH'))}</h2><p>${esc(k('emptyP'))}</p><button class="pg-btn" data-lang="${l.id}">${esc(k('emptyGo'))}</button></div>`;
  }else{
    // hero
    let dl='';
    if(delta){
      const dw=data.words+data.exprs-delta.w,ds=data.structs.length-delta.s,dc=cov&&delta.c!=null?cov[0].pct*100-delta.c:null;
      const parts=[];
      if(dw>0)parts.push(`+${fmt(dw)} ${k('words')}`);
      if(ds>0)parts.push(`+${fmt(ds)} ${k('structs')}`);
      if(dc!=null&&dc>=0.5)parts.push(`+${dc.toFixed(1).replace('.',L==='es'?',':',')} ${k('pts')} · ${k('tv')}`);
      dl=parts.length?`<span>${esc(k('deltaYes'))}:</span>${parts.map(p=>`<span class="kn-chip">${esc(p)}</span>`).join('')}`:`<span>${esc(k('deltaSame'))}</span>`;
    }else dl=`<span>${esc(k('deltaNone'))}</span>`;
    body+=`<section class="kn-hero" aria-label="${esc(k('title'))}"><div class="kn-nums">
      <div class="kn-n"><b data-to="${data.words}">0</b><small>${esc(k('words'))}</small></div>
      <div class="kn-n"><b data-to="${data.exprs}">0</b><small>${esc(k('exprs'))}</small></div>
      <div class="kn-n"><b data-to="${data.structs.length}">0</b><small>${esc(k('structs'))}</small></div></div>
      <div class="kn-delta">${dl}</div></section>`;
    // compreensão
    body+=`<div class="kn-sec"><div><h2>${esc(k('mediaH'))}</h2><p>${esc(k('mediaP'))}</p></div></div>`;
    if(data.isEn){
      if(cov){
        const order=MEDIA_ORDER.map(id=>cov.find(r=>r.id===id)).filter(Boolean);
        body+=`<div class="kn-media">${order.map(mediaRowHtml).join('')}</div>`;
      }else{
        body+=`<div class="kn-note err">${esc(k('covErr'))}<button data-know="retry">${esc(k('retry'))}</button></div>`;
      }
    }else body+=`<div class="kn-note">${esc(k('noCov'))}</div>`;
    // memória
    const t=data.tiers,tot=Math.max(1,data.total),due=(function(){try{return srsDueCount()}catch(e){return 0}})();
    body+=`<div class="kn-sec"><div><h2>${esc(k('memH'))}</h2><p>${esc(k('memP'))}</p></div></div>
     <div class="kn-card"><div class="kn-tiers" role="img" aria-label="${esc(k('tNew'))} ${t.n}, ${esc(k('tFix'))} ${t.f}, ${esc(k('tFirm'))} ${t.s}">
       <i data-w="${(t.s/tot*100).toFixed(2)}" style="background:#1FAE6B"></i><i data-w="${(t.f/tot*100).toFixed(2)}" style="background:#F5A400"></i><i data-w="${(t.n/tot*100).toFixed(2)}" style="background:#6DDFDB"></i></div>
       <div class="kn-leg">
        <div style="--lb:#DEF7EA"><b data-to="${t.s}">0</b><span>${esc(k('tFirm'))}</span><small>${esc(k('tFirmD'))}</small></div>
        <div style="--lb:#FFF1CC"><b data-to="${t.f}">0</b><span>${esc(k('tFix'))}</span><small>${esc(k('tFixD'))}</small></div>
        <div style="--lb:#EDFCFB"><b data-to="${t.n}">0</b><span>${esc(k('tNew'))}</span><small>${esc(k('tNewD'))}</small></div></div>
       <div class="kn-mem"><div class="tx">${esc(due?'':k('allSet'))}</div><button class="pg-btn sm" data-go="review">🔁 ${esc(due?k('review')(due):k('deck'))}</button></div>
       ${data.recent.length?`<hr class="kn-hr" style="margin:16px 0 12px"><div style="font-weight:900;font-size:13px;color:var(--pg-mute);margin-bottom:8px;text-transform:uppercase;letter-spacing:.06em">${esc(k('recentH'))}</div>
       <div class="kn-chips">${data.recent.map(w=>`<span class="kn-w"><b>${esc(w.w)}</b><small>${esc(w.m)}</small></span>`).join('')}</div>`:''}
     </div>`;
    // estruturas
    const groups=[],gm={};
    data.structs.forEach(s=>{const key=s.lv||'';if(!gm[key]){gm[key]={lv:key,items:[]};groups.push(gm[key])}gm[key].items.push(s)});
    const LIM=18;
    body+=`<div class="kn-sec"><div><h2>${esc(k('strH'))}</h2><p>${esc(k('strP'))}</p></div></div><div class="kn-card">
      ${data.structs.length?groups.map(g=>{
        const open=EXPANDED[g.lv],list=open?g.items:g.items.slice(0,LIM);
        return `<div class="kn-lv" ${g.lv?'':'style="display:none"'}>${esc(g.lv)} <em>${g.items.length}</em></div><div class="kn-chips" style="${lc}">${list.map(s=>`<span class="kn-s" title="${esc(s.full)}">${esc(s.t)}</span>`).join('')}</div>
        ${g.items.length>LIM?`<button class="kn-more" data-know="more" data-lv="${esc(g.lv)}">${esc(open?k('less'):k('more')(g.items.length))}</button>`:''}`}).join('')
       :`<div class="kn-note">${esc(k('emptyP'))}</div>`}
      ${data.next.length?`<div class="kn-lv" style="margin-top:20px">${esc(k('next'))}</div><div class="kn-chips">${data.next.map(s=>`<span class="kn-s nx">${esc(s)}</span>`).join('')}</div>`:''}
    </div>`;
    body+=`<details class="kn-how"><summary>${esc(k('howH'))}</summary><p>${esc(k('how'))}</p></details>`;
  }
  const html=topbar(L)+`<main class="kn" style="${lc}">
    <button class="kn-back" data-know="back">← ${esc(k('back'))}</button>
    <div class="kn-head"><div><h1>🧠 ${esc(k('title'))}</h1><p>${esc(k('sub'))}</p></div></div>
    ${tabs}${body}</main>`;
  app.innerHTML=html;
  try{PogUI.cur='profile';PogUI.mountNav()}catch(e){}
  scrollTo(0,0);
  animate();
}

function animate(){
  const root=document.querySelector('main.kn');if(!root)return;
  const nums=root.querySelectorAll('[data-to]'),bars=root.querySelectorAll('[data-w]');
  const rm=reduceMotion();
  nums.forEach(el=>{
    const to=parseFloat(el.dataset.to)||0,dec=parseInt(el.dataset.dec||'0',10);
    const show=v=>{if(dec===0&&el.dataset.to.indexOf('.')>-1&&to>0&&to<1)return;el.textContent=dec?v.toFixed(dec):fmt(Math.round(v))};
    if(rm||to===0){if(to>0)show(to);return}
    const t0=performance.now(),dur=900;
    (function step(now){const p=Math.min(1,(now-t0)/dur),e=1-Math.pow(1-p,3);
      if(el.dataset.to.indexOf('.')>-1&&!dec)el.textContent=String(Math.round(to*e)).replace(/^0$/,to>0&&to<1?'<1':'0');else show(to*e);
      if(p<1)requestAnimationFrame(step);else if(el.dataset.to.indexOf('.')>-1&&!dec)el.textContent=to>0&&to<1?'<1':String(Math.round(to));else show(to)})(t0);
  });
  requestAnimationFrame(()=>requestAnimationFrame(()=>bars.forEach(b=>{b.style.width=b.dataset.w+'%'})));
}

let TOKEN=0;
function show(from,lid){
  if(from)FROM=from;
  injectCss();
  const my=++TOKEN;
  const L=(window.PogUI&&PogUI.LANGS)||[];
  CUR=lid||pickLang();
  const l=L.find(x=>x.id===CUR)||L[0];if(!l)return;
  const run=()=>loadFor(l).then(()=>{
    const data=compute(l);
    let covP=Promise.resolve(null);
    if(data.isEn&&data.doneEps)covP=loadCov().then(cv=>mediaCoverage(cv,data.known)).catch(()=>false);
    return covP.then(cov=>{
      if(my!==TOKEN)return;
      const rows=cov||null;
      const prev=data.doneEps?snapDelta(l.id,{w:data.words+data.exprs,s:data.structs.length,c:rows?rows[0].pct*100:null}):null;
      render(data,rows,cov===false,prev);
    });
  });
  try{history.pushState(null,'','#/know')}catch(e){}
  return (typeof navLoading==='function'?navLoading(run):run());
}
function back(){
  if(FROM==='profile'){window.profile();return}
  window.home();
}

/* ---------- ligações com o resto do app ---------- */
function ctaHtml(from){
  const n=Object.keys(ST.srs||{}).length;
  return `<button class="kn-cta" data-know="open" data-from="${from}"><span class="ic" aria-hidden="true">🧠</span><div><b>${esc(k('cta1'))}</b><small>${esc(n?k('ctaTxtN')(fmt(n)):k('ctaTxt'))}</small></div><span class="go">${esc(k('ctaGo'))} →</span></button>`;
}
function wrapScreen(name,selector,from){
  const orig=window[name];if(typeof orig!=='function')return;
  window[name]=function(){
    const r=orig.apply(this,arguments);
    try{injectCss();const el=document.querySelector('#app .pt-today')&&name==='home'?document.querySelector('#app .pt-today'):document.querySelector('#app '+selector);if(el&&!document.querySelector('#app .kn-cta'))el.insertAdjacentHTML('afterend',ctaHtml(from))}catch(e){console.warn(e)}
    return r;
  };
}
function isPlaying(){try{return !!P}catch(e){return false}}
document.addEventListener('click',ev=>{
  const b=ev.target.closest('[data-know]');if(!b||isPlaying())return;
  const a=b.dataset.know;
  if(a==='open'){ev.preventDefault();show(b.dataset.from||'home')}
  else if(a==='lang'){CUR=b.dataset.l;show(FROM,CUR)}
  else if(a==='more'){const lv=b.dataset.lv;EXPANDED[lv]=!EXPANDED[lv];show(FROM,CUR)}
  else if(a==='retry'){COV_P=null;show(FROM,CUR)}
  else if(a==='back'){back()}
});
window.addEventListener('popstate',()=>{if(!isPlaying()&&location.hash==='#/know')show(FROM,CUR)});

wrapScreen('home','.pg-stats','home');
wrapScreen('profile','.dash-head','profile');
if(window.PogUI){const _start=PogUI.start;PogUI.start=function(){const r=_start.apply(this,arguments);if(location.hash==='#/know')show('home');return r}}

window.PogKnow={show,stem,toks,norm,englishStrings,compute,coverage,mediaCoverage,loadCov};
})();
