/* Neighbors · 3 quadros de abertura inseridos automaticamente em todo episódio (em tempo de execução):
   nbopen1 Abertura (título com marca-texto, etiquetas, citação, pergunta de opinião),
   nbopen2 Leitura (texto curto com palavras-alvo tocáveis + ilustração),
   nbopen3 Compreensão + escolha da palavra certa (vale 1-2 pontos).
   Kill-switch: window.POG_NBOPEN=false. Não altera os JSON: envolve fxBridge (chamado em play) e fxTotal. */
(function(){
if(window.POG_NBOPEN===false)return;
if(typeof FXR==='undefined'||typeof FX_KIND==='undefined')return;
FX_KIND.nbopen1='story';FX_KIND.nbopen2='story';FX_KIND.nbopen3='practice';FX_KIND.nbfluency='story';FX_KIND.nbscene='story';FX_KIND.nbreply='speak';FX_KIND.nbreview='practice';FX_KIND.nbchoice='practice';FX_KIND.nbprag='story';
FX_LABEL.nbopen1='Abertura';FX_LABEL.nbopen2='Leitura';FX_LABEL.nbopen3='Compreensão e palavra certa';FX_LABEL.nbfluency='Linguagem natural';FX_LABEL.nbscene='Fio da história';FX_LABEL.nbreply='Sua vez';FX_LABEL.nbreview='Revisão do Neighbors';FX_LABEL.nbchoice='Escolha o tom';FX_LABEL.nbprag='Como isso soa';FX_LABEL.nbmilestone='Marco do arco';FX_LABEL.nbreflection='Fechamento do arco';
FX_KIND.nbmilestone='reward';FX_KIND.nbreflection='reward';
const q=(s,r)=>(r||document).querySelector(s);
const H=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const say2=(t,who,slow)=>{try{fxSay(String(t),who,slow)}catch(e){}};
const sfx2=n=>{try{sfx(n)}catch(e){}};

/* ---------- textos de interface (PT / ES) ---------- */
const TX={
pt:{unit:'Unidade',sec1:'Conversa e opinião',today:'Missão de hoje',gram:'Gramática',voc:'Vocabulário',pron:'Pronúncia',
 q1:'Qual destas frases você mais usaria nessa situação?',q1h:'Toque numa opção, não há resposta errada.',quote:'Frase do dia · toque para ouvir',
 keyYes:'Essa é a frase-chave de hoje! Você vai usá-la durante todo o episódio.',keyNo:'Boa escolha! A frase-chave de hoje é',
 pick:'Escolha uma opção',cont:'Continuar',read:'Leitura',readH:'Toque nas palavras marcadas para ver o significado.',
 comp:'Compreensão',gapT:'Escolha a palavra certa',topicQ:'Sobre o que é este texto?',firstQ:n=>'O que '+n+' disse primeiro?',
 gapQ:'Complete a frase com a palavra certa.',you:'Você',answer:'Responda as duas perguntas',sayOpen:'Vamos aquecer: o que você diria?',
 sayRead:'Leia e toque nas palavras marcadas.',sayComp:'Agora mostre o que você entendeu.',tt:'Texto',sayOk:'Isso mesmo!',
 rev:'Revisão do arco',secR:'Revisão e opinião',qR:'Qual destas frases do arco você mais quer reforçar?',places:'Lugares',phr:'Frases',
 revIn:c=>'Você ouviu essa frase em '+c+'. Vamos revê-la agora.',revAny:'Boa escolha! Vamos revê-la ao longo desta revisão.',
 whereQ:x=>'Em qual lugar aconteceu: “'+x+'”?',sayRevOpen:'Vamos rever o arco: qual frase você quer reforçar?',sayRevOk:'Boa escolha!'},
es:{unit:'Unidad',sec1:'Conversación y opinión',today:'Misión de hoy',gram:'Gramática',voc:'Vocabulario',pron:'Pronunciación',
 q1:'¿Cuál de estas frases usarías más en esta situación?',q1h:'Toca una opción, no hay respuesta incorrecta.',quote:'Frase del día · toca para escuchar',
 keyYes:'¡Esa es la frase clave de hoy! La usarás durante todo el episodio.',keyNo:'¡Buena elección! La frase clave de hoy es',
 pick:'Elige una opción',cont:'Continuar',read:'Lectura',readH:'Toca las palabras marcadas para ver el significado.',
 comp:'Comprensión',gapT:'Elige la palabra correcta',topicQ:'¿De qué trata este texto?',firstQ:n=>'¿Qué dijo '+n+' primero?',
 gapQ:'Completa la frase con la palabra correcta.',you:'Tú',answer:'Responde las dos preguntas',sayOpen:'Vamos a calentar: ¿qué dirías?',
 sayRead:'Lee y toca las palabras marcadas.',sayComp:'Ahora muestra lo que entendiste.',tt:'Texto',sayOk:'¡Eso es!',
 rev:'Repaso del arco',secR:'Repaso y opinión',qR:'¿Cuál de estas frases del arco quieres reforzar más?',places:'Lugares',phr:'Frases',
 revIn:c=>'Escuchaste esta frase en '+c+'. Vamos a repasarla ahora.',revAny:'¡Buena elección! La repasaremos a lo largo de este repaso.',
 whereQ:x=>'¿En qué lugar ocurrió: “'+x+'”?',sayRevOpen:'Vamos a repasar el arco: ¿qué frase quieres reforzar?',sayRevOk:'¡Buena elección!'}
};
const tx=()=>{let es=false;try{es=(P&&P.c&&P.c.ui==='es')||(typeof ST!=='undefined'&&ST&&ST.homeLang==='es')}catch(e){}return TX[es?'es':'pt']};

/* ---------- utilitários de texto ---------- */
const CJK=/[぀-ヿ㐀-鿿]/;
const ART=/^(the|a|an|o|os|as|um|uma|el|la|los|las|un|una|le|les|l'|der|die|das|il|lo|gli|i|un'|to)$/i;
const rx=s=>s.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
function forms(w){w=String(w||'').replace(/\(.*?\)/g,' ').replace(/[«»“”"]/g,'').replace(/\s+/g,' ').trim();if(!w)return[];
  const out=[];const add=x=>{x=x.trim();if(x&&out.indexOf(x)<0)out.push(x)};
  w.split(/\s*[\/;,]\s*/).forEach(part=>{add(part);const p=part.split(' ');if(p.length>1&&ART.test(p[0]))add(p.slice(1).join(' '))});
  return out.sort((a,b)=>b.length-a.length)}
function mkRe(fs){if(!fs.length)return null;const cj=fs.some(f=>CJK.test(f));
  const body=fs.map(rx).join('|');
  try{return cj?new RegExp('('+body+')','giu'):new RegExp('(?<![\\p{L}\\p{N}])('+body+')(?![\\p{L}\\p{N}])','giu')}catch(e){return null}}
const wc=t=>CJK.test(t)?Math.ceil(t.replace(/\s/g,'').length/1.5):(t.trim().split(/\s+/).filter(Boolean).length);
const hash=s=>{let h=7;String(s).split('').forEach(c=>{h=(h*31+c.charCodeAt(0))>>>0});return h};
function seeded(seed){let s=seed>>>0||1;return()=>{s=(s*1664525+1013904223)>>>0;return s/4294967296}}
function shuf(a,seed){a=a.slice();const r=seeded(seed);for(let i=a.length-1;i>0;i--){const j=(r()*(i+1))|0;[a[i],a[j]]=[a[j],a[i]]}return a}
const cap=s=>s.charAt(0).toUpperCase()+s.slice(1);
const isCap=s=>/^\p{Lu}/u.test(s);
const sameN=(a,b)=>String(a).toLowerCase().replace(/[^\p{L}\p{N}]/gu,'')===String(b).toLowerCase().replace(/[^\p{L}\p{N}]/gu,'');

/* ---------- montagem dos dados a partir do episódio ---------- */
function collect(e){
  const fr=e.fr||[];const hero=fr.find(f=>f.k==='nbhero');if(!hero)return collectRev(e,fr);
  const lines=[];const seen=new Set();let cast=null,me=null;
  fr.filter(f=>f.k==='nbchat'&&f.lines).forEach(f=>{if(!cast)cast=f.cast;if(!me)me=f.me;f.lines.forEach(l=>{if(l&&l[1]&&!seen.has(l[1])){seen.add(l[1]);lines.push(l)}})});
  const hook=hero.hook||(e.h&&e.h.l?[e.h.l,e.h.tr||'']:null);
  const shadow=fr.find(f=>f.k==='nbshadow');
  const character=e.character||{};
  return {hero,lines,cast:cast||{},me:me||hero.name,hook,key:(e.g&&e.g.t)||(hero.hook&&hero.hook[0])||'',vocab:(e.v||[]).filter(v=>v&&v[0]),shadow,character,community:e.community||{}};
}
/* ----- revisões de arco (sem nbhero): começam com nbtrip ou nbchat "Mapa do arco" ----- */
function parsePlace(l){
  const m=/^(.{1,40}?)\s*[:：]\s*(.+)$/.exec(String((l&&l[1])||''));if(!m)return null;
  const c=m[1].replace(/^(In|En|Em|À|Au|Aux|A|Nach|Zu|Bei)\s+(?=\S)/i,'').trim();if(!c)return null;
  return {c,t:m[2].trim(),tr:String(l[2]||'').split(' · ')[0]}}
function collectRev(e,fr){
  if(!e.rev)return null;
  const trip=fr.find(f=>f&&f.k==='nbtrip'&&f.stops&&f.stops.length);
  const chat=fr.find(f=>f&&f.k==='nbchat'&&f.lines&&f.lines.length);
  if(!trip&&!chat)return null;
  const seen=new Set(),lines=[],vocab=[],vs=new Set();
  const addL=(who,t,tr)=>{t=String(t||'').trim();if(!t||seen.has(t.toLowerCase())||wc(t)<3||t.length>90)return;seen.add(t.toLowerCase());lines.push([who||'',t,tr||''])};
  const addV=(w,tr)=>{w=String(w||'').trim();if(!w||vs.has(w.toLowerCase()))return;vs.add(w.toLowerCase());vocab.push([w,tr||''])};
  let places=[];
  if(trip){
    places=trip.stops.map(s=>({c:s.c,t:s.t,nm:s.nm,fc:s.fc,ln:s.ln}));
    trip.stops.forEach(s=>{if(s.ln)addL(s.nm,s.ln[0],s.ln[1]);(s.w||[]).forEach(w=>addV(w[0],w[1]))});
  }else{
    places=chat.lines.slice(1,-1).map(parsePlace).filter(Boolean)}
  fr.forEach(f=>{if(!f)return;
    if(f.k==='nbshadow')(f.items||[]).forEach(i=>addL('',i[0],i[1]));
    else if(f.k==='wrap')(f.recap||[]).forEach(i=>addL('',i[0],i[1]));
    else if(f.k==='nbtap')(f.items||[]).forEach(i=>{if(i.ln)addL('',i.ln[1],'')});
    else if(f.k==='nbvocab'||f.k==='nbfind')(f.items||[]).forEach(i=>addV(i[0],i[2]))});
  lines.sort((a,b)=>(b[0]?1:0)-(a[0]?1:0));
  const tr0=(e.h&&e.h.tr)||'';
  const g=(trip&&trip.g)||(chat&&chat.g)||['#6C5CE7','#FF7AA8'];
  const emo=places.map(p=>p.fc).filter(Boolean).slice(0,4);
  const hero={g,num:'',lvl:e.lv||'',name:'Poggie',face:'🧭',emo:emo.length?emo:['🧭','🗺️','📍','🎒'],mission:e.p||'',sub:e.s||'',hook:(e.h&&e.h.l)?[e.h.l,tr0]:null,rev:1};
  return {rev:1,hero,lines,cast:{},me:'Poggie',hook:hero.hook,key:'',vocab,shadow:null,places,nSent:lines.length};
}
function revOpts(e,d){
  const pool=[];const seen=new Set();
  const push=(t,tr,where,who)=>{t=String(t||'').trim();if(!t||seen.has(t.toLowerCase())||t.length>70)return;seen.add(t.toLowerCase());pool.push({t,tr:tr||'',key:false,where:where||'',who:who||''})};
  d.places.forEach(p=>{if(p.ln)push(p.ln[0],p.ln[1],p.c,p.nm)});
  d.lines.forEach(l=>push(l[1],l[2],'',l[0]));
  if(pool.length<3)d.places.forEach(p=>{if(!p.ln)push(p.t,p.tr,p.c)});
  if(pool.length<3)return null;
  const seed=hash((P&&P.cid||'')+e.n+'r');
  return shuf(pool,seed).slice(0,5)}
function whereQ(e,d,seed){
  const ps=d.places.filter(p=>p.c&&p.t&&d.places.filter(x=>x.c===p.c).length===1&&String(p.t).length<=60);
  const cities=[...new Set(d.places.map(p=>p.c))];if(!ps.length||cities.length<3)return null;
  const p=ps[seed%ps.length];
  const wrong=shuf(cities.filter(c=>c!==p.c),seed+5).slice(0,3);if(wrong.length<2)return null;
  const opts=shuf([p.c,...wrong],seed+1);
  return {qk:'where',qp:p.t.replace(/[.!?。]+$/,''),opts,a:opts.indexOf(p.c),why:'“'+p.t+'” — '+p.c,say:[p.ln?p.ln[0]:p.t,p.nm||'Poggie']}}
function gapTok(e,d,lines,seed){
  const used=(lines.length>=2?lines:d.lines).filter(l=>!CJK.test(l[1])&&wc(l[1])>=4);
  const toks=s=>[...s.matchAll(/[\p{L}][\p{L}'’-]{3,}/gu)].map(m=>({w:m[0],i:m.index})).sort((a,b)=>b.w.length-a.w.length);
  const c=used.map(l=>({l,t:toks(l[1])[0]})).filter(x=>x.t&&x.t.w.length>=5);
  if(!c.length)return null;const k=c[seed%c.length];const sent=k.l[1],surf=k.t.w;
  const pool=[...new Set(d.lines.filter(l=>l!==k.l).flatMap(l=>toks(l[1]).slice(0,2).map(x=>x.w)).filter(w=>w.length>=4&&!sameN(w,surf)&&!sent.toLowerCase().includes(w.toLowerCase())))];
  if(pool.length<3)return null;
  const up=k.t.i===0;const wrong=shuf(pool,seed+7).slice(0,3).map(w=>up?cap(w):(isCap(w)?w.toLowerCase():w));
  const opts=shuf([surf,...wrong],seed+3);
  return {before:sent.slice(0,k.t.i),after:sent.slice(k.t.i+surf.length),opts,a:opts.indexOf(surf),sent,tr:k.l[2]||'',who:k.l[0],why:sent+(k.l[2]?' — '+k.l[2]:'')}}
function titleHtml(e,d){
  const t=String(e.t||'');let best=null;
  d.vocab.forEach(v=>{forms(v[0]).forEach(f=>{const re=mkRe([f]);const m=re&&re.exec(t);if(m&&(!best||m[0].length>best[1].length))best=[m.index,m[0]]})});
  if(!best){const key=forms(d.key)[0];if(key){const re=mkRe([key]);const m=re&&re.exec(t);if(m)best=[m.index,m[0]]}}
  if(!best){const toks=[...t.matchAll(/[^\s,.!?¿¡:;]+/g)].filter(m=>m[0].length>=3).sort((a,b)=>b[0].length-a[0].length);if(toks[0])best=[toks[0].index,toks[0][0]]}
  if(!best)return H(t);
  return H(t.slice(0,best[0]))+'<mark>'+H(best[1])+'</mark>'+H(t.slice(best[0]+best[1].length))}
function pronTag(d){
  const r=d.shadow&&d.shadow.real&&d.shadow.real[2];
  if(r){const m=/[“"]([^”"]{2,28})[”"]/.exec(String(r));if(m)return m[1].trim();const p=String(r).split(/→|->/);if(p.length>1){const s=p[1].replace(/[“”"].*$/,'').trim();if(s&&s.length<=28)return s}}
  const v=d.vocab[0];return v?v[0]:''}
function opinionOpts(e,d){
  const seen=new Set(),pool=[];
  const push=(t,tr,key)=>{t=String(t||'').trim();if(!t||seen.has(t.toLowerCase()))return;seen.add(t.toLowerCase());pool.push({t,tr:tr||'',key:!!key})};
  if(d.hook)push(d.hook[0],d.hook[1],true);
  const nice=d.lines.filter(l=>wc(l[1])>=2&&l[1].length<=70);
  const k0=d.hook?d.hook[0]:'';
  nice.filter(l=>d.key&&forms(d.key).some(f=>{const re=mkRe([f]);return re&&re.test(l[1])})).forEach(l=>push(l[1],l[2],sameN(l[1],k0)));
  nice.forEach(l=>push(l[1],l[2],false));
  if(pool.length<4)d.vocab.forEach(v=>push(v[0],v[1],false));
  const n=Math.min(6,pool.length);if(n<3)return null;
  const keyO=pool.find(o=>o.key)||pool[0];keyO.key=true;
  let rest=shuf(pool.filter(o=>o!==keyO),hash(e.n+'o')).slice(0,n-1);
  const at=hash(e.n+'k')%Math.min(4,n);rest.splice(at,0,keyO);return rest}
function readingText(d){
  const out=[];let tot=0;
  for(const l of d.lines){const w=wc(l[1]);if(tot+w>80&&tot>=40)break;if(tot+w>95&&out.length)break;out.push(l);tot+=w;if(tot>=72)break}
  return out.length>=2?out:null}
function vocabHits(lines,vocab){
  /* palavras do vocabulário que aparecem no texto: [{v,re,forms}] */
  const txt=lines.map(l=>l[1]).join(' ');const hits=[];
  vocab.forEach(v=>{const fs=forms(v[0]);const re=mkRe(fs);if(re&&re.test(txt)){re.lastIndex=0;hits.push({v,fs,re})}});
  return hits}
function topicQ(e,t,seed){
  const cid=(typeof P!=='undefined'&&P&&P.cid)||'';let pool=[];
  try{pool=(EP[cid]||[]).filter(x=>x&&x.s&&x.n!==e.n&&!sameN(x.s,e.s)).map(x=>x.s)}catch(x){}
  pool=[...new Set(pool)];if(pool.length<3)return null;
  const wrong=shuf(pool,seed).slice(0,3);const opts=shuf([e.s,...wrong],seed+1);
  return {qk:'topic',opts,a:opts.indexOf(e.s),why:'“'+e.t+'” — '+e.s}}
function firstQ(e,d,t,seed){
  const l0=d.lines[0];if(!l0||!l0[2])return null;
  const other=[...new Set(d.lines.slice(1).map(l=>l[2]).filter(x=>x&&x!==l0[2]))];if(other.length<3)return null;
  const wrong=shuf(other,seed).slice(0,3);const opts=shuf([l0[2],...wrong],seed+1);
  return {qk:'first',qn:l0[0],opts,a:opts.indexOf(l0[2]),why:l0[1]+' — '+l0[2],say:[l0[1],l0[0]]}}
function gapQ(e,d,lines,t,seed){
  const used=lines.length>=2?lines:d.lines;
  const cands=[];
  used.forEach(l=>{d.vocab.forEach(v=>{const fs=forms(v[0]);const re=mkRe(fs);if(!re)return;re.lastIndex=0;const m=re.exec(l[1]);
    if(m&&m[0].length>=2&&wc(l[1])>=3&&l[1].replace(m[0],'').trim().length>=6)cands.push({l,v,m:m[0],idx:m.index,fs})})});
  if(!cands.length)return null;
  const c=cands[hash(e.n+'g')%cands.length];
  const sent=c.l[1];const surf=c.m;
  const low=!isCap(surf)||c.idx>0;
  const fmt=s=>low?s:cap(s);
  const others=d.vocab.filter(v=>v!==c.v).map(v=>{const f=forms(v[0]);return f[f.length-1]}).filter(x=>x&&!sameN(x,surf)&&!sent.toLowerCase().includes(x.toLowerCase()));
  let pool=[...new Set(others)];
  if(pool.length<3){try{const cid=P.cid;(EP[cid]||[]).slice(0,40).forEach(x=>(x.v||[]).forEach(v=>{const f=forms(v[0]);const w=f[f.length-1];if(w&&!sameN(w,surf)&&!sent.toLowerCase().includes(w.toLowerCase()))pool.push(w)}))}catch(x){}pool=[...new Set(pool)]}
  if(pool.length<3)return null;
  const wrong=shuf(pool,seed+7).slice(0,3).map(w=>CJK.test(w)?w:(isCap(surf)&&c.idx===0?cap(w):(surf===surf.toUpperCase()&&surf.length>1?w:w)));
  const right=surf;const opts=shuf([right,...wrong],seed+3);
  const before=sent.slice(0,c.idx),after=sent.slice(c.idx+surf.length);
  return {before,after,opts,a:opts.indexOf(right),sent,tr:c.l[2]||'',who:c.l[0],why:sent+(c.l[2]?' — '+c.l[2]:'')}}

function priorEpisode(e){try{const all=EP[P.cid]||[],i=all.findIndex(x=>x.n===e.n);return i>0?all[i-1]:null}catch(x){return null}}
function buildThread(e,d){
  const prev=priorEpisode(e),hero=d.hero||{};if(!hero||!d.lines.length)return null;
  const next=d.lines.find(l=>l[0]==='You')||d.lines[1]||d.lines[0];
  let memory='';try{memory=ST&&ST.nbTone?ST.nbTone:''}catch(x){}
  let arc='';try{const a=(ARCS[P.cid]||[]).filter(x=>EP[P.cid].findIndex(y=>y.n===x[0])<=P.idx).slice(-1)[0];arc=a?a[1]:''}catch(x){}
  let skill='';try{skill=ST&&ST.nbSkill?ST.nbSkill:''}catch(x){}
  return {k:'nbscene',g:hero.g||['#6C5CE7','#FF7AA8'],name:hero.name||'Neighbors',city:hero.city||'',mission:hero.mission||e.p||'',hook:d.hook,previous:prev?prev.t:'',memory,skill,arc,current:e.t||hero.sub||'',prompt:next&&next[1]||'',translation:next&&next[2]||''};
}
function buildReply(e,d){
  const li=d.lines.findIndex((l,i)=>i>0&&l[0]&&l[0]!=='You');
  const line=li>=0?d.lines[li]:d.lines[0],ai=d.lines.findIndex(l=>l[0]==='You'),answer=ai>=0?d.lines[ai]:d.lines[1];
  if(!line||!answer||!answer[1])return null;
  const reaction=d.lines.slice(Math.max(ai+1,0)).find(l=>l[0]&&l[0]!=='You')||null;
  return {k:'nbreply',g:d.hero.g||['#6C3FEF','#9a7bff'],name:d.hero.name||'',heard:line[1],heardTr:line[2]||'',situation:d.hero.mission||e.p||'',model:answer[1],modelTr:answer[2]||'',tokens:forms(answer[1]).filter(x=>x.length>2).slice(0,4),reaction:reaction?reaction[1]:'',reactionTr:reaction?reaction[2]||'':'',reactionWho:reaction?reaction[0]:'',consequence:'A resposta muda o próximo turno: observe se o interlocutor confirma, pergunta, aceita ou pede outra coisa.'};
}
function buildReview(e){
  const prev=priorEpisode(e);if(!prev)return null;const pf=(prev.fr||[]).find(f=>f&&f.k==='nbchat');if(!pf||!pf.lines)return null;
  const rows=pf.lines.filter(l=>l&&l[1]&&l[2]).slice(0,2);if(!rows.length)return null;const current=(e.fr||[]).find(f=>f&&f.k==='nbchat');const wrong=(current&&current.lines||[]).map(l=>l[2]).filter(Boolean);if(!wrong.length)(e.fr||[]).filter(f=>f&&f.k==='nbtap').forEach(f=>(f.items||[]).forEach(i=>(i.opts||[]).forEach(o=>{if(o&&o[1])wrong.push(o[1])})));
  return {k:'nbreview',g:['#00B894','#0984E3'],from:prev.t,rows:rows.map((l,i)=>{const opts=[l[2],...(wrong.filter(x=>x!==l[2]).slice(i,i+2))];return {en:l[1],pt:l[2],opts:[...new Set(opts)].slice(0,3)}})};
}
function buildChoice(e,d){
  const line=d.lines.find((l,i)=>i>0&&l[0]&&l[0]!=='You')||d.lines[0],model=d.lines.find(l=>l[0]==='You')||d.lines[1];if(!line||!model)return null;
  const lv=String(d.hero.lvl||e.lv||'A1').toUpperCase(),formal=/B2|C1|C2/.test(lv);
  const opts=[{label:model[1],tone:formal?'claro e profissional':'natural',out:'Você mantém o objetivo da conversa.'},{label:line[1].replace(/[.!?]+$/,'')+'?',tone:'pedir esclarecimento',out:'Você ganha tempo e confirma o que entendeu.'},{label:'I am not sure. Could we come back to this?',tone:'mais cauteloso',out:'Você sinaliza dúvida e abre espaço para continuar.'}];
  return {k:'nbchoice',g:d.hero.g||['#E17055','#6C5CE7'],heard:line[1],heardTr:line[2]||'',opts,level:lv};
}
function buildPrag(e,d){
  const lv=String(d.hero.lvl||e.lv||'A1').toUpperCase(),advanced=/B2|C1|C2/.test(lv),city=d.hero.city||'';
  return {k:'nbprag',g:d.hero.g||['#00B894','#0984E3'],city,level:lv,scene:e.s||d.hero.sub||'',tips:advanced?['Escolha o registro: direto, diplomático ou formal.','Observe o que fica implícito e o que precisa ser dito.','Uma frase correta pode soar brusca dependendo do contexto.']:['Ouça a situação antes de responder.','Use “please”, “thanks” e perguntas curtas para soar natural.','A mesma ideia pode ter mais de uma forma correta.']};
}
function buildFluency(e,d){
  if(d.rev)return null;
  const lv=String(d.hero.lvl||e.lv||'A1').toUpperCase();
  const advanced=/B2|C1|C2/.test(lv),chunks=d.vocab.slice(0,6).map(v=>[forms(v[0])[0]||v[0],v[1]||'']);
  const lines=d.lines.filter(l=>l&&l[1]&&l[1].length>18).slice(0,3);
  const repair=advanced?'Could you clarify what you mean?':'Sorry, could you say that again?';
  return {k:'nbfluency',g:d.hero.g||['#2D98DA','#20BF6B'],level:lv,scene:e.s||d.hero.sub||'',chunks,lines,repair,ladder:advanced?['ouça o sentido geral','perceba o registro e o subtexto','responda com precisão e diplomacia']:['ouça a frase inteira','repita o bloco de palavras','responda com naturalidade']};
}
function buildMilestone(e,d){
  try{const a=(ARCS[P.cid]||[]).find(x=>x[0]===e.n);if(!a)return null;return {k:'nbmilestone',g:d.hero.g||['#F2A900','#E85D75'],title:a[1],level:d.hero.lvl||e.lv||'',mission:d.hero.mission||e.p||'',city:d.hero.city||''}}catch(x){return null}
}
function buildReflection(e,d){if(!e.rev)return null;const lv=String(d.hero.lvl||e.lv||'A1').toUpperCase(),opts=/B2|C1|C2/.test(lv)?['ser mais preciso','ajustar o registro','sustentar minha opinião']:['responder com mais naturalidade','pedir esclarecimento','usar uma frase-chave sem traduzir'];return {k:'nbreflection',g:d.hero.g||['#F2A900','#E85D75'],level:lv,title:e.t||'Revisão do arco',mission:e.p||'Reveja as situações e escolha uma habilidade para levar adiante.',opts}}
function build(e){
  const d=collect(e);if(!d||!d.lines.length)return null;
  const g=d.hero.g||['#6C5CE7','#FF7AA8'];const out=[];
  const rv=!!d.rev;
  const opts=rv?revOpts(e,d):opinionOpts(e,d);
  const tags=[];
  if(rv){const cs=[...new Set(d.places.map(p=>p.c))];if(cs.length)tags.push(['places',cs.slice(0,3).join(' · ')+(cs.length>3?'…':'')]);
    const vw=d.vocab.slice(0,3).map(v=>forms(v[0]).slice(-1)[0]).filter(Boolean);if(vw.length)tags.push(['voc',vw.join(' · ')]);
    if(d.nSent)tags.push(['phr',d.nSent+' frases'])}
  else if(d.key)tags.push(['gram',d.key]);
  if(!rv){const vs=d.vocab.slice(0,3).map(v=>forms(v[0]).slice(-1)[0]).filter(Boolean);if(vs.length)tags.push(['voc',vs.join(' · ')]);
  const pr=pronTag(d);if(pr)tags.push(['pron',pr])}
  if(opts)out.push({k:'nbopen1',g,lvl:d.hero.lvl||e.lv||'',num:d.hero.num||e.o||'',name:d.hero.name,hook:d.hook,title:titleHtml(e,d),topic:e.s||d.hero.sub||'',mission:d.hero.mission||'',tags,opts,keyPhrase:d.key,face:d.hero.face,rev:rv,community:!rv&&d.community?d.community:null,characterRole:!rv&&d.character?d.character.role:''});
  const rl=readingText(d);
  if(rl){out.push({k:'nbopen2',g,lines:rl,vocab:d.vocab,hook:d.hook,name:d.hero.name,face:d.hero.face,emo:d.hero.emo||[],lvl:d.hero.lvl||'',topic:e.s||''})}
  const seed=hash((rv?(P&&P.cid||''):'')+e.n+'c');const t0=TX.pt;
  const subs=[];
  const cq=rv?whereQ(e,d,seed):(hash(e.n)%2?firstQ(e,d,t0,seed)||topicQ(e,t0,seed):topicQ(e,t0,seed)||firstQ(e,d,t0,seed));
  const gq=gapQ(e,d,rl||[],t0,seed)||(rv?gapTok(e,d,rl||[],seed):null);
  if(cq)subs.push({t:'q',d:cq});if(gq)subs.push({t:'g',d:gq});
  if(subs.length)out.push({k:'nbopen3',g,subs,cnt:subs.length,name:d.hero.name,reading:rl?1:0});
  const thread=buildThread(e,d);if(thread)out.push(thread);
  const reply=buildReply(e,d),choice=buildChoice(e,d),prag=buildPrag(e,d),fluency=buildFluency(e,d),review=buildReview(e);
  /* O percurso varia levemente entre episódios: a conversa pode vir antes
     da explicação de tom, evitando que o curso pareça uma lista mecânica. */
  const englishNeighbors=typeof P!=='undefined'&&P&&/^nb(?:-|es-|fr-|pt-|de-)/.test(String(P.cid||''));
  const extras=hash(e.n)%2?[reply,choice,prag,englishNeighbors?fluency:null,review]:[prag,englishNeighbors?fluency:null,reply,choice,review];extras.forEach(x=>{if(x)out.push(x)});
  const milestone=buildMilestone(e,d);if(milestone)out.unshift(milestone);
  const reflection=buildReflection(e,d);if(reflection)out.push(reflection);
  return out.length?out:null}

function inject(e){
  if(!e||!e.fr||e._nbo)return;e._nbo=1;
  if(window.POG_NBOPEN===false)return;
  if(e.fr.some(f=>f&&/^nbopen/.test(f.k)))return;
  let hi=e.fr.findIndex(f=>f&&f.k==='nbhero');
  if(hi>=0)hi++;
  else{if(!e.rev)return;hi=e.fr.findIndex(f=>f&&(f.k==='nbtrip'||f.k==='nbchat'));if(hi<0)return}
  const fr=build(e);if(!fr)return;
  e.fr.splice(hi,0,...fr)}

/* ---------- CSS ---------- */

/* ---------- ajuste para caber em UMA tela ---------- */
function fit(st){try{
  const b=document.querySelector('#pbody');if(!b||!st||!st.isConnected)return;
  st.classList.remove('nbo-t1','nbo-t2','nbo-t3','nbo-t4','nbo-t5','nbo-t6');
  for(let i=0;i<=6;i++){if(i)st.classList.add('nbo-t'+i);if(b.scrollHeight<=b.clientHeight+1)break}
  if(b.scrollHeight>b.clientHeight+1&&st.classList.contains('nbo2')){
    const lns=()=>st.querySelectorAll('.nbo-ln');while(b.scrollHeight>b.clientHeight+1&&lns().length>2){const a=lns();a[a.length-1].remove()}}
}catch(e){}}
function fitSoon(st){fit(st);requestAnimationFrame(()=>fit(st));[120,400,900].forEach(ms=>setTimeout(()=>fit(st),ms))}
if(!window._nboRz){window._nboRz=1;window.addEventListener('resize',()=>{const s=document.querySelector('#pstage .step.nbo');if(s)fit(s)})}
const theme=f=>{const g=f.g||['#6C5CE7','#FF7AA8'];return 'style="--g1:'+g[0]+';--g2:'+g[1]+'"'};
const L3=['a','b','c','d','e','f'];

/* ---------- 1 · Abertura ---------- */
FXR.nbopen1=function(f,st,n){
  const t=tx();let picked=false;
  const lt=String(f.lvl||'A').charAt(0).toUpperCase();
  st.innerHTML='<div class="step fx nbo nbo1" '+theme(f)+'>'+fxKindBar(f,n)+
  '<div class="nbo-grid"><div class="nbo-l">'+
   '<header class="nbo-strip"><span class="nbo-letter">'+H(lt)+'</span><div class="nbo-st"><small>'+(f.rev?t.rev:t.unit+' '+H(f.num))+' · '+H(f.lvl)+'</small><h1 class="nbo-title">'+f.title+'</h1><p class="nbo-topic">'+H(f.topic)+'</p></div></header>'+
   '<div class="nbo-tags">'+f.tags.map(x=>'<span class="nbo-tag nbo-'+x[0]+'"><b>'+t[x[0]]+'</b>'+H(x[1])+'</span>').join('')+'</div>'+
   (f.community?'<p class="nbo-character"><b>Personagem recorrente</b> · '+H(f.community.name||'')+(f.characterRole?' · '+H(f.characterRole):'')+'</p>':'')+
   (f.hook?'<button type="button" class="nbo-quote" id="nboq"><span class="nbo-qm">“</span><div><b>'+H(f.hook[0])+'</b><em>'+H(f.hook[1]||'')+'</em><small>— '+H(f.name)+' · '+t.quote+'</small></div></button>':'')+
   (f.mission?'<p class="nbo-hand"><small>'+t.today+'</small>'+H(f.mission)+'</p>':'')+
  '</div><div class="nbo-r"><section class="nbo-card"><span class="nbo-sec">'+(f.rev?t.secR:t.sec1)+'</span><h3 class="nbo-q">'+(f.rev?t.qR:t.q1)+'</h3>'+
   '<ul class="nbo-opts">'+f.opts.map((o,i)=>'<li><button type="button" class="nbo-opt" data-i="'+i+'"><i>'+L3[i]+'</i><span>'+H(o.t)+'</span></button></li>').join('')+'</ul>'+
   '<div class="nbo-fb" id="nbofb" aria-live="polite"><small>'+t.q1h+'</small></div></section></div></div></div>';
  const root=q('.nbo',st);
  const hq=q('#nboq',st);if(hq)hq.onclick=()=>say2(f.hook[0],f.name);
  st.querySelectorAll('.nbo-opt').forEach(b=>b.onclick=()=>{
    const o=f.opts[+b.dataset.i];st.querySelectorAll('.nbo-opt').forEach(x=>x.classList.remove('sel'));b.classList.add('sel');
    sfx2(o.key||f.rev?'burst':'pop');say2(o.t,o.who||f.name);
    const fb=q('#nbofb',st);
    fb.innerHTML='<p class="nbo-tr"><b>'+H(o.t)+'</b> — '+H(o.tr||'')+'</p><p class="nbo-why">'+(f.rev?(o.where?t.revIn(H(o.where)):t.revAny):(o.key?t.keyYes:t.keyNo+' <i>“'+H(f.keyPhrase||(f.hook&&f.hook[0])||'')+'”</i>.'))+'</p>';
    if(!f.rev)st.querySelectorAll('.nbo-opt').forEach(x=>{if(f.opts[+x.dataset.i].key)x.classList.add('key')});
    if(!picked){picked=true;cta(t.cont,true,true);say(f.rev?t.sayRevOk:(o.key?t.sayOk:t.keyNo),'happy')}
    fit(root)});
  cta(t.pick,false);say(f.rev?t.sayRevOpen:t.sayOpen);fitSoon(root)};

/* ---------- 2 · Leitura ---------- */
function artHtml(f){
  try{const e=P.e;
    if(window.PogIllus){let r=null;
      try{if(PogIllus.auto)r=PogIllus.auto(e,{mood:'day'})}catch(x){}
      if(r&&typeof r==='string'&&r.indexOf('<')>=0)return r;
      if(r&&r.nodeType===1)return r.outerHTML}
  }catch(x){}
  try{if(window.PogCover&&PogCover.svg)return PogCover.svg(P.e)}catch(x){}
  const g=f.g||['#6C5CE7','#FF7AA8'];
  return '<svg viewBox="0 0 320 180" xmlns="http://www.w3.org/2000/svg" role="img"><defs><linearGradient id="nbg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="'+g[0]+'"/><stop offset="1" stop-color="'+g[1]+'"/></linearGradient></defs><rect width="320" height="180" fill="url(#nbg)"/><circle cx="250" cy="50" r="26" fill="#fff" opacity=".25"/><text x="160" y="112" font-size="64" text-anchor="middle">'+H(f.face||'🙂')+'</text>'+(f.emo||[]).slice(0,4).map((m,i)=>'<text x="'+(34+i*84)+'" y="160" font-size="24" text-anchor="middle">'+H(m)+'</text>').join('')+'</svg>'}
function paragraph(f,t){
  const hits=f.vocab.map((v,i)=>({i,fs:forms(v[0])})).filter(h=>h.fs.length);
  const all=[];hits.forEach(h=>h.fs.forEach(x=>all.push({x,i:h.i})));
  all.sort((a,b)=>b.x.length-a.x.length);
  const re=mkRe(all.map(a=>a.x));const lookup=s=>{const a=all.find(a=>a.x.toLowerCase()===s.toLowerCase());return a?a.i:-1};
  const used=new Set();
  return f.lines.map((l,li)=>{
    const txt=l[1];let html='',last=0;
    if(re){re.lastIndex=0;let m;while((m=re.exec(txt))){const i=lookup(m[0]);if(i<0||used.has(i)||used.size>=5){continue}used.add(i);
      html+=H(txt.slice(last,m.index))+'<button type="button" class="nbo-w" data-v="'+i+'">'+H(m[0])+'</button>';last=m.index+m[0].length}}
    html+=H(txt.slice(last));
    const who=l[0]==='You'?t.you:l[0];
    return '<span class="nbo-ln" data-l="'+li+'">'+(who?'<b class="nbo-who">'+H(who)+'</b> ':'')+html+'</span>'}).join(' ')}
FXR.nbopen2=function(f,st,n){
  const t=tx();
  const key=f.hook?f.hook:[f.lines[0][1],f.lines[0][2]||''];
  st.innerHTML='<div class="step fx nbo nbo2" '+theme(f)+'>'+fxKindBar(f,n)+
  '<div class="nbo-grid"><div class="nbo-l"><figure class="nbo-fig"><div class="nbo-art">'+artHtml(f)+'</div><figcaption>'+H(f.topic)+'</figcaption></figure>'+
  '<blockquote class="nbo-pull"><b>“'+H(key[0])+'”</b><em>'+H(key[1])+'</em><small>— '+H(f.name)+'</small></blockquote></div>'+
  '<div class="nbo-r"><section class="nbo-card nbo-read"><span class="nbo-sec">'+t.read+'</span><p class="nbo-text">'+paragraph(f,t)+'</p><div class="nbo-hint">'+t.readH+'</div></section></div></div><div class="nbo-pop" id="nbopop" hidden></div></div>';
  const root=q('.nbo',st),pop=q('#nbopop',st);
  const hide=()=>{pop.hidden=true};
  st.querySelectorAll('.nbo-w').forEach(b=>b.onclick=ev=>{ev.stopPropagation();const v=f.vocab[+b.dataset.v];
    sfx2('pop');say2(b.textContent,f.name);
    pop.innerHTML='<b>'+H(b.textContent)+'</b><span>'+H(v[1]||'')+'</span>'+(v[2]?'<small>'+H(v[2])+'</small>':'');pop.hidden=false;
    const rb=root.getBoundingClientRect(),br=b.getBoundingClientRect();
    const pw=Math.min(pop.offsetWidth,rb.width-16);
    let x=br.left-rb.left+br.width/2-pw/2;x=Math.max(8,Math.min(x,rb.width-pw-8));
    let y=br.top-rb.top-pop.offsetHeight-8;if(y<4)y=br.bottom-rb.top+8;
    pop.style.left=x+'px';pop.style.top=y+'px';b.classList.add('seen')});
  st.querySelectorAll('.nbo-ln').forEach(s=>s.addEventListener('click',ev=>{if(ev.target.closest('.nbo-w'))return;hide();const l=f.lines[+s.dataset.l];say2(l[1],l[0]||f.name);}));
  root.addEventListener('click',ev=>{if(!ev.target.closest('.nbo-w'))hide()});
  cta(t.cont,true,true);say(t.sayRead);fitSoon(root)};

/* ---------- 3 · Compreensão + palavra certa ---------- */
FXR.nbopen3=function(f,st,n){
  const t=tx();const subs=f.subs;let done=0;const state=subs.map(()=>({wrong:0,ok:false}));
  /* perguntas geradas em PT; os textos de interface são trocados para ES no render */
  const card=(s,i)=>{
    if(s.t==='q'){return '<section class="nbo-card" data-i="'+i+'"><span class="nbo-sec">'+t.comp+'</span><h3 class="nbo-q">'+H(s.d.qk==='first'?t.firstQ(s.d.qn==='You'?t.you:s.d.qn):s.d.qk==='where'?t.whereQ(s.d.qp):t.topicQ)+'</h3>'+
      '<ul class="nbo-opts">'+s.d.opts.map((o,k)=>'<li><button type="button" class="nbo-opt" data-k="'+k+'"><i>'+L3[k]+'</i><span>'+H(o)+'</span></button></li>').join('')+'</ul></section>'}
    return '<section class="nbo-card" data-i="'+i+'"><span class="nbo-sec">'+t.gapT+'</span><h3 class="nbo-q">'+t.gapQ+'</h3>'+
      '<p class="nbo-gap">'+(s.d.who==='You'?'':'<b class="nbo-who">'+H(s.d.who)+'</b> ')+H(s.d.before)+'<span class="nbo-bl" id="nbobl'+i+'">_____</span>'+H(s.d.after)+'</p>'+(s.d.tr?'<p class="nbo-gtr">'+H(s.d.tr)+'</p>':'')+
      '<ul class="nbo-opts nbo-chips">'+s.d.opts.map((o,k)=>'<li><button type="button" class="nbo-opt" data-k="'+k+'"><i>'+L3[k]+'</i><span>'+H(o)+'</span></button></li>').join('')+'</ul></section>'};
  st.innerHTML='<div class="step fx nbo nbo3" '+theme(f)+'>'+fxKindBar(f,n)+'<div class="nbo-grid">'+subs.map((s,i)=>'<div class="'+(i?'nbo-r':'nbo-l')+'">'+card(s,i)+'<div class="nbo-fb" id="fbx'+i+'"></div></div>').join('')+'</div></div>';
  const root=q('.nbo',st);
  P.fx.done=false;P.fx.cta=()=>!P.fx.done;
  const fin=()=>{if(done>=subs.length){P.fx.done=true;cta(t.cont,true,true);try{confetti(40)}catch(x){}}else cta(t.answer,false)};
  subs.forEach((s,i)=>{const sec=q('section[data-i="'+i+'"]',st);const fbx=q('#fbx'+i,st);
    sec.querySelectorAll('.nbo-opt').forEach(b=>b.onclick=()=>{
      if(state[i].ok)return;const k=+b.dataset.k;const ok=k===s.d.a;
      fbx.id='fb';
      if(ok){
        state[i].ok=true;b.classList.add('ok');sec.querySelectorAll('.nbo-opt').forEach(x=>x.disabled=true);
        if(!state[i].wrong)P.score++;
        fxGrade(true,s.d.why);
        if(s.t==='g'){const bl=q('#nbobl'+i,st);bl.textContent=s.d.opts[k];bl.classList.add('ok');say2(s.d.sent,s.d.who||f.name)}
        else if(s.d.say)say2(s.d.say[0],s.d.say[1]);
        done++;fin();
      }else{
        state[i].wrong++;b.classList.add('no');b.disabled=true;
        fxGrade(false,'',null);
      }
      fbx.id='fbx'+i;fit(root)})});
  cta(t.answer,false);say(t.sayComp);fitSoon(root)};

/* ---------- 4 · continuidade narrativa ---------- */
FXR.nbscene=function(f,st,n){
  const t=tx(),prev=f.previous?'<p class="nb-thread"><b>Antes:</b> '+H(f.previous)+'</p>':'';
  const arc=f.arc?'<p class="nbo-hint"><b>Arco atual:</b> '+H(f.arc)+'</p>':'';
  const mem=f.memory?'<p class="nbo-hint"><b>Você vem praticando:</b> '+H(f.memory)+'. Tente perceber se esse tom também funciona aqui.</p>':'';const skill=f.skill?'<p class="nbo-hint"><b>Habilidade escolhida antes:</b> '+H(f.skill)+'.</p>':'';
  st.innerHTML='<div class="step fx nbo nbscene" '+theme(f)+'>'+fxKindBar(f,n)+'<div class="nbo-card nb-thread-card"><span class="nbo-sec">Fio da história</span><h2 class="nbo-q">'+H(f.current)+'</h2>'+arc+prev+mem+skill+'<p class="nbo-hand"><small>'+t.today+'</small>'+H(f.mission||'Resolva a situação usando o inglês da conversa.')+'</p><div class="nbo-quote"><b>Agora você entra na conversa:</b><em>“'+H(f.prompt)+'”</em><small>'+H(f.translation||'Ouça, pense na intenção e responda com suas palavras.')+'</small></div><p class="nbo-hint">Preste atenção em quem fala, no objetivo e no tom. A próxima atividade é sua.</p></div></div>';
  cta(t.cont,true,true);say('A história continua. Agora observe a situação antes de responder.');fitSoon(q('.nbscene',st))};

/* ---------- 5 · produção livre guiada ---------- */
FXR.nbreply=function(f,st,n){
  const t=tx();let checked=false;
  st.innerHTML='<div class="step fx nbo nbreply" '+theme(f)+'>'+fxKindBar(f,n)+'<div class="nbo-grid"><div class="nbo-l"><span class="nbo-sec">Sua vez</span><h2 class="nbo-q">Responda sem copiar</h2><p class="nbo-topic">'+H(f.situation)+'</p><div class="nbo-quote"><b>'+H(f.name||'A outra pessoa')+'</b><em>“'+H(f.heard)+'”</em><small>'+H(f.heardTr)+'</small></div></div><div class="nbo-r"><section class="nbo-card"><label class="nbo-sec" for="nbreplyin">O que você diria?</label><textarea id="nbreplyin" rows="4" placeholder="Escreva ou fale em inglês…" style="display:block;width:100%;box-sizing:border-box;margin:10px 0;padding:12px;border:2px solid #e6e1f7;border-radius:14px;font:600 16px/1.4 system-ui;resize:vertical"></textarea><p class="nbo-hint">Inclua pelo menos uma ideia da situação. Depois compare com um modelo possível.</p><div class="nbo-fb" id="nbreplyfb" aria-live="polite"></div></section></div></div></div>';
  const root=q('.nbreply',st),inp=q('#nbreplyin',st);const ready=()=>cta(checked?t.cont:'Ver meu modelo',checked||!!String(inp.value||'').trim(),true);
  inp.oninput=()=>{if(!checked)ready()};
  P.fx.cta=()=>{if(!checked){checked=true;const val=String(inp.value||'').toLowerCase();const hits=(f.tokens||[]).filter(x=>val.includes(String(x).toLowerCase())).length;const fb=q('#nbreplyfb',st);fb.innerHTML='<p class="nbo-tr"><b>Modelo possível:</b> '+H(f.model)+'</p><p class="nbo-why">'+H(f.modelTr)+'<br>Você retomou '+hits+' palavra(s)-chave. A resposta pode ser diferente: o objetivo é comunicar a intenção.</p>'+(f.reaction?'<div class="nbo-reaction"><b>Consequência comunicativa · '+H(f.reactionWho||'interlocutor')+':</b><br>'+H(f.reaction)+'<small>'+H(f.reactionTr||'')+'</small><p>'+H(f.consequence||'A próxima fala depende da sua intenção.')+'</p></div>':'');fb.className='nbo-fb';inp.disabled=true;P.score++;say('Muito bem. Compare sua intenção com o modelo e tente dizer a sua resposta em voz alta.','happy');ready();fit(root);return true}return false};
  ready();say('Agora é você quem conduz a conversa.');fitSoon(root)};

/* ---------- 6 · revisão espaçada ---------- */
FXR.nbreview=function(f,st,n){
  const t=tx();let ri=0,hits=0,done=false;const draw=()=>{const r=f.rows[ri];if(!r){done=true;P.score+=hits;st.innerHTML='<div class="step fx nbo nbreview" '+theme(f)+'>'+fxKindBar(f,n)+'<div class="nbo-card"><span class="nbo-sec">Revisão do Neighbors</span><h2 class="nbo-q">Você trouxe a conversa de volta</h2><p class="nbo-hand">'+hits+'/'+f.rows.length+' frases recuperadas de primeira. Esse resgate prepara você para a situação atual.</p></div></div>';cta(t.cont,true,true);say('Revisão concluída! O que você aprendeu antes continua disponível.');P.fx.cta=null;return}const opts=shuf(r.opts,hash(f.from+ri));st.innerHTML='<div class="step fx nbo nbreview" '+theme(f)+'>'+fxKindBar(f,n)+'<div class="nbo-card"><span class="nbo-sec">Revisão · '+(ri+1)+'/'+f.rows.length+'</span><h2 class="nbo-q">O que esta fala quer dizer?</h2><div class="nbo-quote"><b>'+H(r.en)+'</b><small>Toque na melhor tradução.</small></div><ul class="nbo-opts">'+opts.map((o,i)=>'<li><button type="button" class="nbo-opt" data-i="'+i+'"><i>'+L3[i]+'</i><span>'+H(o)+'</span></button></li>').join('')+'</ul><div class="nbo-fb" id="nbrfb"></div></div></div>';cta('Escolha uma resposta',false);st.querySelectorAll('.nbo-opt').forEach(b=>b.onclick=()=>{if(b.disabled)return;const ok=b.textContent.includes(r.pt);if(ok){hits++;b.classList.add('ok')}else{b.classList.add('no');st.querySelectorAll('.nbo-opt').forEach(x=>{if(x.textContent.includes(r.pt))x.classList.add('ok')})}st.querySelectorAll('.nbo-opt').forEach(x=>x.disabled=true);q('#nbrfb',st).innerHTML=ok?'<p class="nbo-tr"><b>Boa!</b> Você recuperou a fala.</p>':'<p class="nbo-why">A tradução era: '+H(r.pt)+'</p>';cta(ri<f.rows.length-1?'Próxima fala ▶':t.cont,true,true);P.fx.cta=()=>{ri++;draw();return true}})};P.fx.cta=null;draw()};
FXR.nbchoice=function(f,st,n){let picked=false;st.innerHTML='<div class="step fx nbo nbchoice" '+theme(f)+'>'+fxKindBar(f,n)+'<div class="nbo-card"><span class="nbo-sec">Escolha o tom · '+H(f.level)+'</span><h2 class="nbo-q">Como você quer conduzir esta conversa?</h2><div class="nbo-quote"><b>Você ouviu:</b><em>“'+H(f.heard)+'”</em><small>'+H(f.heardTr)+'</small></div><ul class="nbo-opts">'+f.opts.map((o,i)=>'<li><button type="button" class="nbo-opt" data-i="'+i+'"><i>'+L3[i]+'</i><span>'+H(o.label)+'<small style="display:block;opacity:.7">'+H(o.tone)+'</small></span></button></li>').join('')+'</ul><div class="nbo-fb" id="nbchfb" aria-live="polite"></div></div></div>';cta('Escolha uma resposta',false);st.querySelectorAll('.nbo-opt').forEach(b=>b.onclick=()=>{if(picked)return;picked=true;const o=f.opts[+b.dataset.i];try{ST.nbTone=o.tone;save()}catch(x){}b.classList.add('ok');st.querySelectorAll('.nbo-opt').forEach(x=>x.disabled=true);q('#nbchfb',st).innerHTML='<p class="nbo-tr"><b>'+H(o.tone)+'</b> — '+H(o.out)+'</p><p class="nbo-why">A fala muda o tom, mas você continua no controle da situação.</p>';P.score++;P.fx.cta=()=>false;cta(tx().cont,true,true);say('Boa escolha. Em inglês, intenção e tom também comunicam.','happy')})};
FXR.nbprag=function(f,st,n){st.innerHTML='<div class="step fx nbo nbprag" '+theme(f)+'>'+fxKindBar(f,n)+'<div class="nbo-card"><span class="nbo-sec">Como isso soa · '+H(f.level)+'</span><h2 class="nbo-q">A mesma frase muda com a situação</h2><p class="nbo-topic">'+H(f.scene)+(f.city?' · '+H(f.city):'')+'</p><ul class="nbo-list">'+f.tips.map(x=>'<li>'+H(x)+'</li>').join('')+'</ul><p class="nbo-hint">Antes de responder, pergunte: estou sendo claro, natural e adequado para esta relação?</p></div></div>';cta(tx().cont,true,true);say('Não basta estar gramaticalmente correto. O contexto também importa.')};
FXR.nbfluency=function(f,st,n){
  const chunks=f.chunks||[], lines=f.lines||[];
  st.innerHTML='<div class="step fx nbo nbfluency" '+theme(f)+'>'+fxKindBar(f,n)+'<div class="nbo-grid"><div class="nbo-l"><section class="nbo-card"><span class="nbo-sec">Linguagem natural · '+H(f.level)+'</span><h2 class="nbo-q">Blocos que você leva para a conversa</h2><p class="nbo-topic">'+H(f.scene)+'</p><ul class="nbo-list">'+chunks.map(x=>'<li><b>'+H(x[0])+'</b><small style="display:block;opacity:.72">'+H(x[1])+'</small></li>').join('')+'</ul></section></div><div class="nbo-r"><section class="nbo-card"><span class="nbo-sec">Escuta em camadas</span><ul class="nbo-list">'+(f.ladder||[]).map(x=>'<li>'+H(x)+'</li>').join('')+'</ul><div class="nbo-quote"><b>Estratégia de reparo</b><em>'+H(f.repair)+'</em><small>Use quando precisar ganhar tempo ou confirmar a intenção.</small></div><div class="nbo-fb"><b>Toque numa fala para ouvir com atenção:</b><div style="display:grid;gap:6px;margin-top:8px">'+lines.map((l,i)=>'<button type="button" class="nbo-opt" data-nbf="'+i+'" style="text-align:left">'+H(l[1])+'</button>').join('')+'</div></div></section></div></div></div>';
  st.querySelectorAll('[data-nbf]').forEach(b=>b.onclick=()=>say2(lines[+b.dataset.nbf][1],lines[+b.dataset.nbf][0]));
  cta(tx().cont,true,true);say('Agora observe os blocos de linguagem e o ritmo da fala.');fitSoon(q('.nbfluency',st));
};

FXR.nbmilestone=function(f,st,n){st.innerHTML='<div class="step fx nbo nbmilestone" '+theme(f)+'>'+fxKindBar(f,n)+'<div class="nbo-card"><span class="nbo-sec">Marco do arco · '+H(f.level)+'</span><h2 class="nbo-q">'+H(f.title)+'</h2><p class="nbo-hand"><small>O que você vai construir</small>'+H(f.mission)+'</p><p class="nbo-hint">Este arco reúne situações conectadas. Ao avançar, observe como as mesmas habilidades reaparecem em novos contextos.</p></div></div>';cta(tx().cont,true,true);say('Novo arco desbloqueado. Vamos construir essa habilidade passo a passo.','happy')};
FXR.nbreflection=function(f,st,n){let picked=false;st.innerHTML='<div class="step fx nbo nbreflection" '+theme(f)+'>'+fxKindBar(f,n)+'<div class="nbo-card"><span class="nbo-sec">Fechamento do arco · '+H(f.level)+'</span><h2 class="nbo-q">'+H(f.title)+'</h2><p class="nbo-hand"><small>Leve isto com você</small>'+H(f.mission)+'</p><div class="nbo-hint"><b>Escolha uma habilidade:</b> o que você quer levar para as próximas situações?</div><ul class="nbo-opts">'+f.opts.map((o,i)=>'<li><button type="button" class="nbo-opt" data-i="'+i+'"><i>'+L3[i]+'</i><span>'+H(o)+'</span></button></li>').join('')+'</ul><div class="nbo-fb" id="nbrefb"></div></div></div>';cta('Escolha uma habilidade',false);st.querySelectorAll('.nbo-opt').forEach(b=>b.onclick=()=>{if(picked)return;picked=true;const o=f.opts[+b.dataset.i];try{ST.nbSkill=o;save()}catch(x){}b.classList.add('ok');st.querySelectorAll('.nbo-opt').forEach(x=>x.disabled=true);q('#nbrefb',st).innerHTML='<p class="nbo-tr"><b>Registrado:</b> '+H(o)+'</p><p class="nbo-why">Na próxima sequência, procure uma oportunidade de usar essa habilidade.</p>';cta(tx().cont,true,true);say('Escolha registrada. Leve essa habilidade com você.','happy')})};

/* ---------- ligação: fxBridge (inserção) e fxTotal (pontos) ---------- */
function install(){
  try{
    const ob=window.fxBridge;
    if(typeof ob==='function'&&!ob._nbo){const nf=function(e){const r=ob.apply(this,arguments);try{inject(e)}catch(x){try{console.warn('nbopen',x)}catch(_){}}return r};nf._nbo=1;window.fxBridge=nf}
    const ot=window.fxTotal;
    if(typeof ot==='function'&&!ot._nbo){const nt=function(e){let n=ot.apply(this,arguments);try{const NB=['nbtap','nbswap','nbmatch','nbreply','nbchoice','nbshadow','nbctx','nbvocab','nbfind','nbtrip','nbreview','nbfluency'];const nb=(e.fr||[]).some(f=>f&&(f.k==='nbhero'||f.k==='nbtrip'||(e.rev&&f.k==='nbtap')));(e.fr||[]).forEach(f=>{if(!f)return;if(f.k==='nbopen3')n+=f.cnt||0;else if(f.k==='nbreply'||f.k==='nbchoice')n+=1;else if(f.k==='nbreview')n+=f.rows?f.rows.length:1;else if(nb&&NB.indexOf(f.k)>=0&&!window.__NB_TOTAL_OK)n+=1})}catch(x){}return n};nt._nbo=1;window.fxTotal=nt}
  }catch(x){}
}
install();
window.PogNbOpen={build,inject,fit,forms,install,collect};
})();
