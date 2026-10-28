/* Pogglot · arte editorial por obra
 * Gera capas, faixas e figurinhas em SVG a partir da obra cultural do episódio.
 * A arte é determinística: a mesma obra mantém personagens, paleta e cenário.
 */
(function(){
'use strict';
const INK='#2b1d3a', PAPER='#fffaf0';
const esc=s=>String(s==null?'':s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const norm=s=>String(s||'').normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
const hash=s=>{let h=2166136261;for(const c of String(s||'')){h^=c.charCodeAt(0);h=Math.imul(h,16777619)}return h>>>0};
const pick=(a,h)=>a[h%a.length];
const hsl=(h,sa,l)=>{h=((h%360)+360)%360;sa/=100;l/=100;const a=sa*Math.min(l,1-l),f=n=>{const k=(n+h/30)%12,c=l-a*Math.max(-1,Math.min(k-3,9-k,1));return Math.round(255*c).toString(16).padStart(2,'0')};return '#'+f(0)+f(8)+f(4)};
/* paleta própria da obra: matiz do hash, harmonia escolhida pelo hash (análoga, complementar, tríade, quente/fria) */
function palOf(h){const hue=h%360,mode=(h>>>9)%5,off=[35,180,120,-40,150][mode],sa=48+(h>>>12)%22,lt=80+(h>>>15)%6;
 return [hsl(hue,sa,lt),hsl(hue+off,sa-6,56+(h>>>17)%8),hsl(hue+off/2,38,24+(h>>>19)%8),hsl(hue,62,94+(h>>>21)%3)];}
const SCENE_LIST=['city','water','forest','stage','lab','library','museum','kitchen','mountain','night'];
const PALETTES=[
 ['#f7d6a5','#6d8fbd','#203b66','#f8efe1'],['#d8e9c5','#d46f58','#3c5545','#f6f4df'],
 ['#efd0de','#6c73b8','#342b5d','#fff3f4'],['#c8e7e8','#e28b42','#355b63','#eff9f5'],
 ['#f5dca9','#7c9c6c','#354d39','#fff8e8'],['#d9d1ed','#bf6b9b','#4a315d','#f7f0ff']
];
const SCENE_WORDS={
 water:/sea|ocean|river|lake|island|harbor|port|boat|ship|whale|moana|mermaid|fisher/i,
 city:/building|city|street|new york|paris|london|tokyo|rome|chicago|brooklyn|manhattan|architecture|chapel|bridge|station/i,
 forest:/forest|jungle|tree|garden|alice|hobbit|narnia|beauty|beast|lion|panda|animal|wolf|wood/i,
 stage:/theatre|theater|opera|musical|hamlet|romeo|juliet|shakespeare|movie|film|cinema|actor|director|broadway/i,
 lab:/science|physics|chemistry|atom|space|moon|planet|robot|machine|technology|black mirror|mathematics/i,
 library:/book|novel|poem|poetry|literature|library|author|writer|women|dickens|austen|tolstoy|shakespeare/i,
 museum:/painting|museum|art|artist|sculpt|sculpture|monet|picasso|van gogh|chapel|parthenon|building/i,
 kitchen:/food|cook|kitchen|restaurant|chocolate|tea|bread|chef|recipe|ratatouille|pizza/i
};
const OBJECTS={water:'wave',city:'window',forest:'leaf',stage:'mask',lab:'atom',library:'book',museum:'frame',kitchen:'cup'};
const MOTIFS=[
 {re:/paddington|bear called/i,scene:'city',ids:['bear','mrs'],obj:'suitcase'},
 {re:/alice|wonderland|looking glass/i,scene:'forest',ids:['alice','rabbit','cat'],obj:'clock'},
 {re:/wizard of oz|oz|dorothy/i,scene:'forest',ids:['dorothy','scarecrow','lion'],obj:'rainbow'},
 {re:/peter pan|neverland/i,scene:'forest',ids:['wendy','peter','tinker'],obj:'starburst'},
 {re:/three musketeers|musketeer/i,scene:'stage',ids:['dartagnan','athos'],obj:'swords'},
 {re:/don quixote|quixote/i,scene:'city',ids:['quijote','sancho'],obj:'windmill'},
 {re:/little prince|petit prince/i,scene:'lab',ids:['petitprince'],obj:'planet'},
 {re:/asterix/i,scene:'forest',ids:['asterix','obelix'],obj:'shield'},
 {re:/ratatouille/i,scene:'kitchen',ids:['remy','linguini'],obj:'chef'},
 {re:/lion king/i,scene:'forest',ids:['lion'],obj:'sunrise'},
 {re:/mozart|beethoven|symphony|sonata|music|opera/i,scene:'stage',ids:['tom','polly'],obj:'notes'},
 {re:/parthenon|notre-dame|chapel|building|house|architecture/i,scene:'museum',ids:['tommy','oliver'],obj:'columns'},
 {re:/black mirror|robot|space|planet|dispossessed/i,scene:'lab',ids:['pilote','tokio'],obj:'orbit'},
 {re:/dracula|frankenstein|horror|ghost/i,scene:'stage',ids:['huck','ahab'],obj:'moon'},
 {re:/little red hen|peter rabbit|rabbit/i,scene:'forest',ids:['peterrabbit','mcgregor'],obj:'wheat'}
];
const KEY=Object.create(null),VB=Object.create(null),SCN=Object.create(null),THEME=Object.create(null);
let uid=0;
function workOf(e){return (e&&e.a&&e.a.w)||e&&e.w||((e&&e.fr||[]).find(f=>f.k==='cover')||{}).obra||e&&e.title||e&&e.t||'Pogglot';}
function keyOf(e){
 const w=workOf(e), base=norm(w).replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'').slice(0,28)||'obra';
 return 'w-'+base+'-'+hash(w).toString(36).slice(0,5);
}
function motifOf(e,w){const text=`${w} ${(e&&e.a&&e.a.k)||(e&&e.k)||''} ${(e&&e.s)||''}`;return MOTIFS.find(x=>x.re.test(text))||null;}
function sceneOf(e,w){const text=`${w} ${(e&&e.sc)||''} ${(e&&e.rs)||''} ${(e&&e.s)||''}`,motif=motifOf(e,w);if(motif)return motif.scene;for(const [k,re] of Object.entries(SCENE_WORDS))if(re.test(text))return k;return SCENE_LIST[(hash(w)>>>5)%SCENE_LIST.length];}
function castIds(e,m){const motif=motifOf(e,m.w);if(motif)return motif.ids;const ids=[];const add=x=>{if(x&&!ids.includes(x))ids.push(x)};for(const f of (e&&e.fr)||[]){for(const c of (f.chars||[]))add(c[0]);for(const c of Object.values(f.cast||{})){if(Array.isArray(c))add(c[0]);}}return ids.length?ids.slice(0,3):['tom','polly'];}
const AUTO_OBJECTS=[
 [/train|railway|subway|metro|station/i,'train'],[/camera|photograph|photo|film/i,'camera'],[/newspaper|journal|press|report/i,'paper'],[/map|journey|travel|voyage|road/i,'map'],
 [/tea|coffee|cafe|café|restaurant|dinner|meal/i,'cup'],[/dance|ballerina|ballet/i,'ribbon'],[/sport|tennis|football|soccer|baseball|game/i,'trophy'],[/garden|flower|rose|spring/i,'flower'],
 [/school|classroom|teacher|student|university/i,'chalk'],[/market|shop|store|money|bank/i,'ticket'],[/ship|boat|harbor|sea|ocean/i,'anchor'],[/city|street|avenue|new york|london|paris/i,'streetlamp'],
 [/war|battle|soldier|army|king|queen|castle/i,'crown'],[/space|moon|star|planet|astronaut/i,'rocket'],[/science|laboratory|research|medicine|doctor/i,'flask'],[/painting|portrait|museum|artist|sculpture/i,'frame']
];
function objectOf(e,w,scene){const text=`${w} ${(e&&e.a&&e.a.k)||''} ${(e&&e.a&&e.a.d)||''} ${(e&&e.s)||''}`;for(const [re,obj] of AUTO_OBJECTS)if(re.test(text))return obj;const pool=['window','map','ribbon','trophy','flower','chalk','ticket','anchor','streetlamp','crown','rocket','flask','cup','paper','camera','book','frame'];return pool[(hash(w)>>>7)%pool.length];}

function meta(e){
 const w=workOf(e),h=hash(w),key=keyOf(e),pal=palOf(h),motif=motifOf(e,w),scene=sceneOf(e,w);
 KEY[e&&e.n||key]=key;VB[key]='100 40 600 400';SCN[key]=scene;
 const title=w.split(/[:·–—]/)[0].trim();
 const who=(e&&e.fr||[]).flatMap(f=>Object.keys(f.cast||{})).find(Boolean)||'Pog';
 const names=['Mina','Theo','Lena','Sam','Noah','Ari'];
 const out={key,w,title,year:(e&&e.a&&e.a.y)||(e&&e.y)||'',scene,pal,motif:motif&&motif.obj||objectOf(e,w,scene),ids:castIds(e,{w}),who,names:[names[h%names.length],names[(h>>>4)%names.length]]};
 THEME[key]=out;return out;
}
function P(x,y,w,h,fill,rx){return `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${rx||0}" fill="${fill}" stroke="${INK}" stroke-width="4"/>`;}
function E(x,y,rx,ry,fill){return `<ellipse cx="${x}" cy="${y}" rx="${rx}" ry="${ry}" fill="${fill}" stroke="${INK}" stroke-width="4"/>`;}
function L(x1,y1,x2,y2,stroke,sw){return `<path d="M${x1} ${y1}L${x2} ${y2}" fill="none" stroke="${stroke||INK}" stroke-width="${sw||4}" stroke-linecap="round"/>`;}
function cloud(x,y,s,c){return `<g transform="translate(${x} ${y}) scale(${s})" fill="${c}" stroke="${INK}" stroke-width="3"><ellipse cx="0" cy="8" rx="36" ry="13"/><ellipse cx="26" cy="1" rx="25" ry="18"/><ellipse cx="-22" cy="2" rx="22" ry="16"/></g>`;}
function star(x,y,s,c){return `<path d="M${x} ${y-s}l${s*.28} ${s*.62} ${s*.72} ${s*.1}-${s*.55} ${s*.48} ${s*.18} ${s*.7}-${s*.63}-${s*.38}-${s*.58} ${s*.42} ${s*.18}-${s*.7}z" fill="${c}" stroke="${INK}" stroke-width="2"/>`;}
function kid(x,y,s,skin,hair,shirt,flip,look){look=look|0;const hr=look%4;
 const tr=`translate(${x} ${y}) scale(${flip?-s:s} ${s})`;
 return `<g transform="${tr}" stroke="${INK}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"><path d="M-28 90L-38 150M28 90L38 150" fill="none"/><path d="M-43 150h18M25 150h18" fill="none"/><path d="M-48 72Q-48 36 0 30Q48 36 48 72v54h-96z" fill="${shirt}"/><circle cx="0" cy="0" r="40" fill="${skin}"/>${hr===1?`<path d="M-44 10Q-52-50 0-52Q52-50 44 10L40 48Q34 20 30-10Q0-24-30-10Q-34 20-40 48z" fill="${hair}"/>`:hr===2?`<circle cx="0" cy="-58" r="20" fill="${hair}"/><path d="M-40-8Q-34-49 0-48Q36-48 42-6Q23-24 0-20Q-22-26-40-8z" fill="${hair}"/>`:hr===3?`<path d="M-44-6Q-40-52 0-50Q40-52 44-6z" fill="${hair}"/><path d="M-44-6H70" fill="none"/>`:`<path d="M-40-8Q-34-49 0-48Q36-48 42-6Q23-24 0-20Q-22-26-40-8z" fill="${hair}"/>`}<circle cx="-14" cy="2" r="4" fill="${INK}" stroke="none"/><circle cx="14" cy="2" r="4" fill="${INK}" stroke="none"/><path d="M-12 20Q0 29 12 20" fill="none"/>${look&4?`<circle cx="-14" cy="2" r="11" fill="none"/><circle cx="14" cy="2" r="11" fill="none"/><path d="M-3 2h6" fill="none"/>`:''}</g>`;
}
function charFor(id,x,y,s,flip,fall,look){
 try{if(window.PogChars&&PogChars.svg){const raw=PogChars.svg(id);if(raw){const inner=raw.replace(/^<svg[^>]*>/,'').replace(/<\/svg>\s*$/,'');return `<g transform="translate(${x-50*s} ${y}) scale(${flip?-s:s} ${s})" filter="drop-shadow(0 5px 5px rgba(43,29,58,.2))">${inner}</g>`;}}}catch(e){}
 return kid(x,y,s,fall.skin,fall.hair,fall.shirt,flip,look);
}
function object(kind,x,y,s,c){
 const z=s||1;
 if(kind==='wave')return `<g transform="translate(${x} ${y}) scale(${z})"><path d="M0 32q25-30 50 0t50 0" fill="none" stroke="${c}" stroke-width="18" stroke-linecap="round"/><path d="M22 62q25-30 50 0t50 0" fill="none" stroke="${c}" stroke-width="12" stroke-linecap="round"/></g>`;
 if(kind==='window')return `<g transform="translate(${x} ${y}) scale(${z})">${P(0,0,110,92,'#f4e8c8',7)}<path d="M55 0v92M0 46h110" stroke="${INK}" stroke-width="4"/><path d="M12 36l20-20 20 20M66 28l16-14 20 20" fill="none" stroke="${c}" stroke-width="5"/></g>`;
 if(kind==='leaf')return `<g transform="translate(${x} ${y}) scale(${z})"><path d="M4 84Q22 12 90 4Q76 65 4 84z" fill="${c}" stroke="${INK}" stroke-width="4"/><path d="M10 78L72 18" stroke="${INK}" stroke-width="3"/></g>`;
 if(kind==='mask')return `<g transform="translate(${x} ${y}) scale(${z})"><path d="M8 20Q55-8 102 20v32q-18 30-47 34Q26 82 8 52z" fill="${c}" stroke="${INK}" stroke-width="4"/><ellipse cx="35" cy="42" rx="12" ry="8" fill="${PAPER}" stroke="${INK}" stroke-width="3"/><ellipse cx="75" cy="42" rx="12" ry="8" fill="${PAPER}" stroke="${INK}" stroke-width="3"/><path d="M42 68q13 9 26 0" fill="none" stroke="${INK}" stroke-width="3"/></g>`;
 if(kind==='atom')return `<g transform="translate(${x} ${y}) scale(${z})" fill="none" stroke="${c}" stroke-width="6"><ellipse cx="50" cy="50" rx="44" ry="18"/><ellipse cx="50" cy="50" rx="44" ry="18" transform="rotate(60 50 50)"/><ellipse cx="50" cy="50" rx="44" ry="18" transform="rotate(120 50 50)"/><circle cx="50" cy="50" r="9" fill="${c}" stroke="${INK}" stroke-width="3"/></g>`;
 if(kind==='book')return `<g transform="translate(${x} ${y}) scale(${z})">${P(0,8,82,62,'#fff',6)}<path d="M41 8v62" stroke="${c}" stroke-width="5"/><path d="M13 24h18M13 38h18M51 24h18M51 38h18" stroke="${c}" stroke-width="4" stroke-linecap="round"/></g>`;
 if(kind==='frame')return `<g transform="translate(${x} ${y}) scale(${z})">${P(0,0,100,84,'#f0bd65',4)}${P(12,12,76,60,c,2)}<path d="M20 60l18-22 12 12 10-13 20 23" fill="none" stroke="${PAPER}" stroke-width="4"/></g>`;
 if(kind==='clock')return `<g transform="translate(${x} ${y}) scale(${z})"><circle cx="50" cy="50" r="42" fill="#fff" stroke="${INK}" stroke-width="5"/><path d="M50 50V24M50 50l18 12" stroke="${c}" stroke-width="5" stroke-linecap="round"/><circle cx="50" cy="50" r="5" fill="${c}"/></g>`;
 if(kind==='rainbow')return `<g transform="translate(${x} ${y}) scale(${z})"><path d="M5 82a45 45 0 0 1 90 0" fill="none" stroke="${c}" stroke-width="12" stroke-linecap="round"/><path d="M20 82a30 30 0 0 1 60 0" fill="none" stroke="#fff" stroke-width="11" stroke-linecap="round"/><path d="M35 82a15 15 0 0 1 30 0" fill="none" stroke="${PAPER}" stroke-width="10" stroke-linecap="round"/><circle cx="9" cy="82" r="9" fill="#fff" stroke="${INK}" stroke-width="3"/><circle cx="91" cy="82" r="9" fill="#fff" stroke="${INK}" stroke-width="3"/></g>`;
 if(kind==='sunrise')return `<g transform="translate(${x} ${y}) scale(${z})"><circle cx="50" cy="50" r="28" fill="#f5c84f" stroke="${INK}" stroke-width="4"/>${[0,45,90,135,180,225,270,315].map(a=>`<path d="M50 8v-18M50 92v18M8 50h-18M92 50h18M20 20L7 7M80 20L93 7M20 80L7 93M80 80L93 93" transform="rotate(${a} 50 50)" stroke="${c}" stroke-width="5" stroke-linecap="round"/>`).join('')}</g>`;
 if(kind==='starburst')return `<g transform="translate(${x} ${y}) scale(${z})">${star(50,50,42,c)}${star(50,50,20,'#fff')}</g>`;
 if(kind==='swords')return `<g transform="translate(${x} ${y}) scale(${z})"><path d="M18 84L78 12M22 24l56 60" stroke="#fff" stroke-width="10" stroke-linecap="round"/><path d="M18 84L78 12M22 24l56 60" stroke="${c}" stroke-width="3"/><path d="M30 56l16 14M54 42l16 14" stroke="${INK}" stroke-width="6"/></g>`;
 if(kind==='windmill')return `<g transform="translate(${x} ${y}) scale(${z})"><path d="M38 90l8-60h18l8 60z" fill="#f1cf9b" stroke="${INK}" stroke-width="4"/><circle cx="55" cy="30" r="8" fill="${c}" stroke="${INK}" stroke-width="3"/>${[0,90,180,270].map(a=>`<path d="M55 30l${55+Math.cos(a*Math.PI/180)*38} ${30+Math.sin(a*Math.PI/180)*38}" stroke="${c}" stroke-width="9" stroke-linecap="round"/>`).join('')}</g>`;
 if(kind==='planet')return `<g transform="translate(${x} ${y}) scale(${z})"><circle cx="50" cy="50" r="34" fill="${c}" stroke="${INK}" stroke-width="4"/><ellipse cx="50" cy="50" rx="58" ry="14" fill="none" stroke="${INK}" stroke-width="5" transform="rotate(-18 50 50)"/><circle cx="36" cy="39" r="5" fill="${PAPER}"/><circle cx="67" cy="61" r="7" fill="${PAPER}"/></g>`;
 if(kind==='shield')return `<g transform="translate(${x} ${y}) scale(${z})"><path d="M50 5l38 14v29c0 24-16 40-38 48C28 88 12 72 12 48V19z" fill="${c}" stroke="${INK}" stroke-width="5"/><path d="M50 20v58M24 48h52" stroke="${PAPER}" stroke-width="5"/></g>`;
 if(kind==='chef')return `<g transform="translate(${x} ${y}) scale(${z})">${P(8,36,84,52,'#fff',10)}<path d="M20 38q-8-34 14-32 16-16 32 0 22-2 14 32" fill="${c}" stroke="${INK}" stroke-width="4"/></g>`;
 if(kind==='notes')return `<g transform="translate(${x} ${y}) scale(${z})"><path d="M30 16v54M68 8v54M30 16l38-8" stroke="${c}" stroke-width="7" stroke-linecap="round"/><ellipse cx="22" cy="74" rx="14" ry="10" fill="${c}"/><ellipse cx="60" cy="66" rx="14" ry="10" fill="${c}"/></g>`;
 if(kind==='columns')return `<g transform="translate(${x} ${y}) scale(${z})">${P(8,76,84,10,'#e8cfad',2)}${[16,39,62,85].map(xx=>`<path d="M${xx} 76V20" stroke="${c}" stroke-width="10" stroke-linecap="round"/>`).join('')}<path d="M8 18h84" stroke="${INK}" stroke-width="6"/></g>`;
 if(kind==='orbit')return `<g transform="translate(${x} ${y}) scale(${z})"><circle cx="50" cy="50" r="12" fill="${c}" stroke="${INK}" stroke-width="3"/><ellipse cx="50" cy="50" rx="44" ry="17" fill="none" stroke="${c}" stroke-width="6"/><circle cx="90" cy="50" r="6" fill="${c}" stroke="${INK}" stroke-width="3"/></g>`;
 if(kind==='moon')return `<g transform="translate(${x} ${y}) scale(${z})"><circle cx="50" cy="50" r="38" fill="#f7d77b" stroke="${INK}" stroke-width="4"/><circle cx="66" cy="37" r="38" fill="${PAPER}"/><circle cx="30" cy="25" r="3" fill="${c}"/><circle cx="18" cy="76" r="3" fill="${c}"/></g>`;
 if(kind==='wheat')return `<g transform="translate(${x} ${y}) scale(${z})"><path d="M20 90L50 12M50 90L50 12M80 90L50 12" stroke="${c}" stroke-width="5"/><path d="M20 28l-14-8M28 42l-16-6M72 31l16-8M72 47l17-5M43 28L30 17M57 29l14-13" stroke="${c}" stroke-width="6" stroke-linecap="round"/></g>`;
 if(kind==='suitcase')return `<g transform="translate(${x} ${y}) scale(${z})">${P(8,26,86,60,'#c96c4b',8)}${P(38,10,26,20,'none',5)}<path d="M16 47h70M50 26v60" stroke="#f7d6a5" stroke-width="4"/></g>`;
 if(kind==='train')return `<g transform="translate(${x} ${y}) scale(${z})">${P(4,28,94,52,c,8)}${P(16,40,24,20,'#dff4f5',3)}${P(54,40,24,20,'#dff4f5',3)}<circle cx="25" cy="88" r="9" fill="${INK}"/><circle cx="76" cy="88" r="9" fill="${INK}"/><path d="M0 100h108" stroke="${INK}" stroke-width="4"/></g>`;
 if(kind==='camera')return `<g transform="translate(${x} ${y}) scale(${z})">${P(8,28,90,58,c,8)}${P(33,16,30,16,'#fff',4)}<circle cx="53" cy="57" r="21" fill="#fff" stroke="${INK}" stroke-width="4"/><circle cx="53" cy="57" r="10" fill="${c}"/><circle cx="82" cy="39" r="4" fill="#f7d77b"/></g>`;
 if(kind==='paper')return `<g transform="translate(${x} ${y}) scale(${z})">${P(10,5,80,88,'#fff',4)}<path d="M22 25h54M22 40h54M22 55h40M22 70h48" stroke="${c}" stroke-width="4" stroke-linecap="round"/></g>`;
 if(kind==='map')return `<g transform="translate(${x} ${y}) scale(${z})">${P(5,12,96,72,'#fff3c8',4)}<path d="M14 67Q34 20 55 55T92 24" fill="none" stroke="${c}" stroke-width="6"/><circle cx="14" cy="67" r="5" fill="${c}"/><circle cx="92" cy="24" r="5" fill="${c}"/></g>`;
 if(kind==='ribbon')return `<g transform="translate(${x} ${y}) scale(${z})"><path d="M18 86q25-56 50-56t22 40q-8 27-36 7" fill="none" stroke="${c}" stroke-width="12" stroke-linecap="round"/><path d="M54 28l-8-16M54 28l14-12" stroke="${INK}" stroke-width="4"/></g>`;
 if(kind==='trophy')return `<g transform="translate(${x} ${y}) scale(${z})"><path d="M26 12h58v30a29 29 0 0 1-58 0z" fill="#f6c84b" stroke="${INK}" stroke-width="4"/><path d="M26 20H8q0 28 20 30M84 20h18q0 28-20 30" fill="none" stroke="${INK}" stroke-width="5"/><path d="M55 71v17M35 94h40" stroke="${INK}" stroke-width="6" stroke-linecap="round"/></g>`;
 if(kind==='flower')return `<g transform="translate(${x} ${y}) scale(${z})"><path d="M50 42v56" stroke="${c}" stroke-width="6"/><circle cx="50" cy="28" r="14" fill="#f2bd52" stroke="${INK}" stroke-width="3"/>${[[50,6],[72,28],[50,50],[28,28]].map(q=>`<circle cx="${q[0]}" cy="${q[1]}" r="14" fill="${c}" stroke="${INK}" stroke-width="3"/>`).join('')}</g>`;
 if(kind==='chalk')return `<g transform="translate(${x} ${y}) scale(${z})">${P(8,12,94,70,'#456a64',4)}<path d="M20 33h46M20 50h66M20 67h36" stroke="#fffaf0" stroke-width="4" stroke-linecap="round"/></g>`;
 if(kind==='ticket')return `<g transform="translate(${x} ${y}) scale(${z})">${P(8,26,94,48,'#f4c26b',5)}<path d="M35 26v48M74 26v48" stroke="${INK}" stroke-width="3" stroke-dasharray="6 5"/><circle cx="20" cy="50" r="7" fill="${c}"/><circle cx="91" cy="50" r="7" fill="${c}"/></g>`;
 if(kind==='anchor')return `<g transform="translate(${x} ${y}) scale(${z})"><circle cx="50" cy="18" r="9" fill="none" stroke="${c}" stroke-width="7"/><path d="M50 28v56M28 44h44M14 68q8 22 36 22t36-22" fill="none" stroke="${c}" stroke-width="7" stroke-linecap="round"/></g>`;
 if(kind==='streetlamp')return `<g transform="translate(${x} ${y}) scale(${z})"><path d="M50 88V18q0-12 14-12h18" fill="none" stroke="${INK}" stroke-width="7"/><path d="M70 8h24v14H70z" fill="#f7d77b" stroke="${INK}" stroke-width="3"/><path d="M30 92h42" stroke="${INK}" stroke-width="7" stroke-linecap="round"/></g>`;
 if(kind==='crown')return `<g transform="translate(${x} ${y}) scale(${z})"><path d="M10 76l9-54 26 27 14-40 16 40 26-27 9 54z" fill="#f2c94c" stroke="${INK}" stroke-width="4"/><path d="M10 76h100v14H10z" fill="#f2c94c" stroke="${INK}" stroke-width="4"/></g>`;
 if(kind==='rocket')return `<g transform="translate(${x} ${y}) scale(${z})"><path d="M55 4q38 26 26 76H29Q17 30 55 4z" fill="#fff" stroke="${INK}" stroke-width="4"/><circle cx="55" cy="37" r="9" fill="${c}" stroke="${INK}" stroke-width="3"/><path d="M30 58L10 78l25-5M80 58l20 20-25-5" fill="${c}" stroke="${INK}" stroke-width="3"/></g>`;
 if(kind==='flask')return `<g transform="translate(${x} ${y}) scale(${z})"><path d="M37 8h30M45 8v30L18 82q-6 12 12 12h44q18 0 12-12L55 38V8" fill="${c}" fill-opacity=".7" stroke="${INK}" stroke-width="4"/><path d="M28 75h52" stroke="#fff" stroke-width="4"/></g>`;
 return `<g transform="translate(${x} ${y}) scale(${z})">${P(10,25,68,45,'#fff',12)}<path d="M78 35q20 0 20 14t-20 14" fill="none" stroke="${INK}" stroke-width="4"/><path d="M22 16q-4-14 8-20M42 16Q38 2 50-4" fill="none" stroke="${c}" stroke-width="4" stroke-linecap="round"/></g>`;
}
/* ---------- arte rica: personagens, bichinho e cenário no mesmo traço das capas desenhadas à mão ---------- */
const stk=w=>`stroke="${INK}" stroke-width="${w==null?3:w}" stroke-linejoin="round" stroke-linecap="round"`;
const Pp=(d,fill,w,ex)=>`<path d="${d}" fill="${fill}" ${w===0?'':stk(w)} ${ex||''}/>`;
const Ee=(cx,cy,rx,ry,fill,w)=>`<ellipse cx="${cx}" cy="${cy}" rx="${rx}" ry="${ry}" fill="${fill}" ${w===0?'':stk(w)}/>`;
const Cc=(cx,cy,r,fill,w)=>Ee(cx,cy,r,r,fill,w);
const Rr=(x,y,w,h,fill,rx,sw)=>`<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${rx||0}" fill="${fill}" ${sw===0?'':stk(sw)}/>`;
const Ln=(x1,y1,x2,y2,w,fill)=>`<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${INK}" stroke-width="${w+6}" stroke-linecap="round"/><line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${fill}" stroke-width="${w}" stroke-linecap="round"/>`;
const eyes2=(x,y,gap,r)=>{gap=gap||13;r=r||4.4;return [-1,1].map(s=>`<ellipse cx="${x+s*gap}" cy="${y}" rx="${r}" ry="${r*1.3}" fill="${INK}"/><circle cx="${x+s*gap+1.4}" cy="${y-2}" r="${r*.38}" fill="#fff"/>`).join('')};
const blush2=(x,y,gap)=>[-1,1].map(s=>`<ellipse cx="${x+s*gap}" cy="${y}" rx="7" ry="4.4" fill="#ff8aa0" opacity=".55"/>`).join('');
const smile2=(x,y,w)=>`<path d="M${x-w} ${y} Q${x} ${y+w*.95} ${x+w} ${y}" fill="none" stroke="${INK}" stroke-width="2.8" stroke-linecap="round"/>`;
const shadow2=w=>Ee(0,0,w||44,8,'rgba(30,20,50,.22)',0);
const SKINS=['#ffd7b5','#f1c7a8','#d9a273','#b57a52','#8b5a3c'],HAIRS=['#f4d06f','#2b1d3a','#5a3425','#a65d2f','#243b53','#d9503f','#7a4a8a'];
/* criança (origem nos pés; altura ~200) */
function rkid(o){
 const sk=o.skin,hair=o.hair,top=o.top;let g=shadow2();
 if(o.hairStyle==='long')g+=Pp('M-37,-142 Q-46,-198 0,-198 Q46,-198 37,-142 Q43,-98 30,-88 L-30,-88 Q-43,-98 -37,-142Z',hair);
 if(o.hairStyle==='braids')g+=[-1,1].map(s=>Ln(s*30,-132,s*40,-92,13,hair)+Cc(s*40,-90,6,o.ribbon||'#e8473b',2.4)).join('');
 if(o.hairStyle==='bun')g+=Cc(0,-190,17,hair);
 if(o.dress){
  g+=Ln(-12,-52,-13,-9,12,o.legs||sk)+Ln(12,-52,13,-9,12,o.legs||sk)+Ee(-16,-5,15,7,o.shoe,2.6)+Ee(16,-5,15,7,o.shoe,2.6);
  g+=Pp('M-22,-112 L22,-112 L46,-44 Q0,-34 -46,-44 Z',top);
  if(o.apron)g+=Pp('M-13,-110 L13,-110 L26,-48 Q0,-40 -26,-48 Z','#fff');
  for(let i=0;i<3;i++)g+=`<path d="M${-30+i*30},-60 q4,8 0,16" stroke="#fff" stroke-width="3" fill="none" opacity=".5"/>`;
 }else{
  g+=Ln(-10,-70,-12,-10,16,o.bot)+Ln(10,-70,12,-10,16,o.bot)+Ee(-15,-6,16,8,o.shoe,2.6)+Ee(15,-6,16,8,o.shoe,2.6);
  g+=Pp('M-24,-116 L24,-116 L26,-62 Q0,-54 -26,-62 Z',top);
  g+=Rr(-26,-70,52,9,o.belt,3,2.4);
  g+=Cc(0,-92,4,'#fff6d6',2);
 }
 const A={down:[[-40,-62],[40,-62]],wave:[[-40,-62],[46,-156]],out:[[-58,-100],[58,-100]],up:[[-44,-150],[44,-150]]}[o.arms];
 g+=Ln(-24,-106,A[0][0],A[0][1],10,o.sleeve)+Ln(24,-106,A[1][0],A[1][1],10,o.sleeve)+Cc(A[0][0],A[0][1],7,sk,2.6)+Cc(A[1][0],A[1][1],7,sk,2.6);
 if(o.dress)g+=Cc(-24,-108,12,o.sleeve,2.8)+Cc(24,-108,12,o.sleeve,2.8);
 g+=Cc(0,-140,34,sk);
 if(o.hairStyle==='short'||o.hairStyle==='bun')g+=Pp('M-35,-144 Q-36,-180 0,-178 Q36,-180 35,-144 Q20,-166 6,-158 Q-10,-170 -35,-144Z',hair);
 else g+=Pp('M-35,-146 Q-31,-178 0,-176 Q31,-178 35,-146 Q14,-162 0,-160 Q-14,-162 -35,-146Z',hair);
 if(o.band)g+=`<path d="M-36,-150 Q0,-184 36,-150" fill="none" stroke="${o.band}" stroke-width="7" stroke-linecap="round"/>`+Pp('M-36,-152 L-50,-162 L-48,-144Z M-36,-152 L-26,-164 L-24,-146Z',o.band,2.4);
 g+=eyes2(0,-140,13)+blush2(0,-128,22)+smile2(0,-125,9);
 if(o.glasses)g+=`<circle cx="-13" cy="-140" r="11" fill="rgba(255,255,255,.25)" ${stk(2.4)}/><circle cx="13" cy="-140" r="11" fill="rgba(255,255,255,.25)" ${stk(2.4)}/><path d="M-2,-140h4" ${stk(2.4)} fill="none"/>`;
 if(o.hat==='cap')g+=Pp('M-34,-166 Q-6,-196 38,-168 Q8,-164 -34,-166Z',o.hatColor)+Pp('M14,-176 Q40,-212 52,-196 Q40,-190 24,-172Z','#e8473b',2.4);
 if(o.hat==='bonnet')g+=Pp('M-38,-156 Q-30,-190 0,-190 Q30,-190 38,-156 Q20,-148 0,-150 Q-20,-148 -38,-156Z',o.hatColor)+Pp('M-40,-158 Q0,-146 40,-158 L36,-150 Q0,-140 -36,-150Z',o.hatColor,2.4);
 if(o.hat==='top')g+=Rr(-30,-196,60,40,'#2b2538',6,3)+Ee(0,-158,44,9,'#2b2538',3)+Rr(-30,-170,60,9,o.hatColor,0,2.4);
 if(o.hat==='crown')g+=Pp('M-26,-166 L-30,-196 L-14,-182 L0,-204 L14,-182 L30,-196 L26,-166Z','#f6c84c')+Cc(0,-186,4,'#e8473b',2);
 return g;
}
/* bichinho companheiro (origem nos pés; altura ~120) */
function critter(kind,c1,c2){
 let g=shadow2(34);
 const face=(y)=>eyes2(0,y,10,3.6)+blush2(0,y+9,17)+`<ellipse cx="0" cy="${y+8}" rx="4.4" ry="3.2" fill="#e8798f" ${stk(2)}/>`+smile2(0,y+12,6);
 if(kind==='bunny'){g+=[-1,1].map(s=>Ee(s*13,-118,9,28,c1)+Ee(s*13,-116,4.4,19,'#ffc2cf',0)).join('')+Ee(0,-36,26,32,c1)+Ee(0,-32,15,22,'#fff',0)+Cc(0,-76,25,c1)+face(-78)+[-1,1].map(s=>Ee(s*14,-6,13,7,c1,2.6)).join('');}
 else if(kind==='cat'){g+=Pp('M30,-30 Q64,-50 52,-88',  'none',7)+Ee(0,-36,25,30,c1)+Cc(0,-76,26,c1)+[-1,1].map(s=>Pp(`M${s*24},-84 L${s*30},-112 L${s*10},-98Z`,c1)).join('')+[-1,0,1].map(i=>`<path d="M${i*9},-98 v9" ${stk(2.4)} fill="none"/>`).join('')+face(-78)+[-1,1].map(s=>Ee(s*12,-6,12,7,c1,2.6)).join('');}
 else if(kind==='bear'){g+=Ee(0,-38,28,34,c1)+Ee(0,-32,16,22,c2,0)+Cc(0,-80,27,c1)+[-1,1].map(s=>Cc(s*22,-102,10,c1)).join('')+Ee(0,-72,13,10,c2)+face(-82)+[-1,1].map(s=>Ee(s*14,-6,13,7,c1,2.6)).join('');}
 else if(kind==='fox'){g+=Pp('M26,-26 Q70,-44 56,-84 Q38,-60 24,-52Z',c1)+Ee(0,-36,24,30,c1)+Cc(0,-76,25,c1)+[-1,1].map(s=>Pp(`M${s*20},-86 L${s*30},-120 L${s*6},-98Z`,c1)).join('')+Pp('M-20,-70 Q0,-50 20,-70 Q0,-56 -20,-70Z','#fff',2)+face(-80)+[-1,1].map(s=>Ee(s*12,-6,12,7,c2,2.6)).join('');}
 else {g+=Ee(0,-44,28,32,c1)+Pp('M-8,-44 Q30,-70 34,-34 Q16,-24 -8,-44Z',c2)+Cc(0,-84,22,c1)+Pp('M20,-84 L40,-78 L20,-72Z','#f6c84c',2.6)+eyes2(-2,-88,8,3.6)+blush2(-2,-78,15)+Pp('M-6,-18 v12M6,-18 v12','none',3);}
 return g;
}
function flowerBig(x,y,s,hue){const cols=[0,72,144,216,288].map(d=>hsl(hue+d,70,66));let g=Ln(x,y,x,y+210,5,'#4c9a5c')+Pp(`M${x} ${y+130} q-34 -14 -40 -44 q34 4 40 44z`,'#6cc07a',2.4);
 for(let i=0;i<5;i++){const a=i*72*Math.PI/180;g+=Cc((x+Math.sin(a)*32*s).toFixed(1),(y-Math.cos(a)*32*s).toFixed(1),22*s,cols[i],3);}
 return `<g data-decor="1">${g+Cc(x,y,15*s,'#f6c84c',3)}</g>`;}
function mushroom(x,y,s,c){return `<g data-decor="1" transform="translate(${x} ${y}) scale(${s})">${Rr(-9,-4,18,44,'#f7e7c4',6)}${Pp('M-40,-2 Q-40,-46 0,-46 Q40,-46 40,-2Z',c)}${[[-18,-22],[4,-32],[20,-16]].map(q=>Cc(q[0],q[1],5.5,'#fff',0)).join('')}</g>`;}
function sparkle(x,y,s){return `<path data-decor="1" d="M${x} ${y-s}Q${x+s*.15} ${y-s*.15} ${x+s} ${y}Q${x+s*.15} ${y+s*.15} ${x} ${y+s}Q${x-s*.15} ${y+s*.15} ${x-s} ${y}Q${x-s*.15} ${y-s*.15} ${x} ${y-s}z" fill="#fff6d6" opacity=".9"/>`;}
function tuft(x,y){return `<path data-decor="1" d="M${x} ${y}l-6 -22l10 16l4 -24l6 24l10 -14l-4 20" fill="none" ${stk(3)}/>`;}
function butterfly(x,y,c){return `<g data-decor="1" transform="translate(${x} ${y})">${Pp('M0 0Q-22 -26 -30 -4Q-26 16 0 6Z',c)}${Pp('M0 0Q22 -26 30 -4Q26 16 0 6Z',c)}${Cc(-14,-6,4,'#fff',0)}${Cc(14,-6,4,'#fff',0)}<path d="M0 -4v16" ${stk(3)}/></g>`;}
function balloon(x,y,c){return `<g data-decor="1" transform="translate(${x} ${y})"><path d="M0 0Q-26 -4 -24 -38Q0 -64 24 -38Q26 -4 0 0z" fill="${c}" ${stk(3)}/><path d="M0 0l-4 8h8z" fill="${c}" ${stk(2.4)}/><path d="M0 8Q-8 30 4 50" fill="none" ${stk(2.4)}/><ellipse cx="-9" cy="-30" rx="5" ry="9" fill="#fff" opacity=".45"/></g>`;}
function lookOf(h,pal,k){
 const hh=h>>>(k*3),dress=(hh>>>2)%2===0,tops=[pal[1],hsl(h+60,60,64),hsl(h+200,60,66),'#7ec8f2','#e8473b','#f6c84c'];
 const arms=['down','wave','out','wave'][(hh>>>5)%4],hats=[null,null,'cap','bonnet','top','crown',null,null];
 return {skin:SKINS[(hh>>>1)%5],hair:HAIRS[(hh>>>4)%7],hairStyle:['long','braids','short','bun','long','short'][(hh>>>7)%6],dress,apron:dress&&(hh>>>9)%2,
  top:tops[(hh>>>3)%6],bot:pal[2],belt:pal[1],sleeve:tops[(hh>>>3)%6],shoe:'#3a3550',ribbon:'#e8473b',band:(hh>>>11)%3===0?hsl(h+30,70,48):null,
  glasses:(hh>>>13)%4===0,hat:hats[(hh>>>15)%8],hatColor:hsl(h+90,55,58),arms};
}
/* cenário rico: céu e chão em gradiente, colinas, flores gigantes, cogumelos, brilhos, tufos, borboletas */
function decor(h,pal,id){
 let back='',front='';
 const hue=h%360,kinds=[(h>>>3)%3,(h>>>6)%3];
 for(let i=0;i<3;i++){const x=70+i*270+((h>>>(i+4))%60);back+=flowerBig(x,70+((h>>>(i+8))%60),1,hue+i*40);}
 back+=mushroom(560+((h>>>5)%80),330,.8+((h>>>9)%3)*.1,hsl(hue+160,70,58))+mushroom(650+((h>>>7)%60),345,.55,hsl(hue+80,65,62));
 for(let i=0;i<6;i++)back+=sparkle(30+((h>>>i)%12)*62+i*9,24+((h>>>(i+2))%90),6+(i%3)*4);
 back+=cloud(130+((h>>>4)%300),48+((h>>>8)%40),.7,'#fff');
 back+=butterfly(60+((h>>>3)%600),150+((h>>>6)%80),hsl(hue+120,75,64));
 back+=balloon(700,110+((h>>>10)%40),hsl(hue+200,70,62));
 front+=`<path d="M0 352Q200 322 400 350T800 336V450H0z" fill="url(#${id}-g)" ${stk(3)}/>`;
 for(let i=0;i<7;i++)front+=tuft(40+i*112+((h>>>i)%30),392+((h>>>(i+3))%34));
 return {back,front};
}
function body(e,mode,gid){
 const m=meta(e),{pal,scene}=m,h=hash(m.w),bg=pal[3],accent=pal[1],dark=pal[2],light=pal[0];
 let s=`<rect width="800" height="450" fill="url(#${gid}-s)"/>`;
 if(scene==='water'){s+=`<path d="M0 290Q110 250 220 290T440 290T660 290T880 290V450H0z" fill="${light}" stroke="${INK}" stroke-width="4"/>`;for(let i=0;i<5;i++)s+=`<path d="M${i*175-20} 332q42-17 84 0t84 0" fill="none" stroke="${accent}" stroke-width="7" stroke-linecap="round"/>`;s+=cloud(115,72,.8,'#fff');}
 else if(scene==='forest'){s+=`<path d="M0 320Q150 260 300 320T600 320T900 320V450H0z" fill="${light}" stroke="${INK}" stroke-width="4"/>`;for(let i=0;i<6;i++){const x=i*150+35;s+=`<path d="M${x} 330L${x+14} 125L${x+28} 330z" fill="${accent}" stroke="${INK}" stroke-width="4"/><circle cx="${x+14}" cy="${125+(i%2)*25}" r="34" fill="${dark}" stroke="${INK}" stroke-width="4"/>`;}}
 else if(scene==='stage'){s+=`<path d="M0 0h170v450H0zM630 0h170v450H630z" fill="${accent}" stroke="${INK}" stroke-width="4"/><rect x="170" width="460" height="450" fill="${bg}" stroke="${INK}" stroke-width="4"/>`;for(let i=0;i<4;i++)s+=star(250+i*105,78+(i%2)*20,12,light);}
 else if(scene==='lab'){s+=`<rect x="0" y="310" width="800" height="140" fill="${light}" stroke="${INK}" stroke-width="4"/>`;for(let i=0;i<5;i++)s+=`<circle cx="${110+i*145}" cy="${90+(i%2)*35}" r="${18+(i%3)*5}" fill="${accent}" fill-opacity=".28" stroke="${INK}" stroke-width="3"/>`;}
 else if(scene==='library'){s+=P(40,55,720,300,'#f4e4c8',8);for(let r=0;r<3;r++)for(let i=0;i<10;i++)s+=P(65+i*68,80+r*78,46,56,pick([accent,light,dark,'#d88970'],(h+i+r)%4),3);s+=P(0,355,800,95,light,0);}
 else if(scene==='museum'){s+=P(40,55,720,300,'#eee4d4',8);for(let i=0;i<4;i++)s+=object('frame',76+i*185,95+(i%2)*28,.8,pick([accent,light,dark],(h+i)%3));s+=P(0,355,800,95,light,0);}
 else if(scene==='kitchen'){s+=P(0,280,800,170,light,0)+P(60,84,680,210,'#f4e9d7',8)+object('cup',630,150,1,accent);}
 else if(scene==='mountain'){s+=`<path d="M0 330L150 150L250 250L390 90L560 280L670 190L800 320V450H0z" fill="${light}" stroke="${INK}" stroke-width="4"/><path d="M390 90l-34 52 34-16 28 22zM150 150l-26 38 26-12 22 18z" fill="#fff" stroke="${INK}" stroke-width="3"/><path d="M0 345Q200 310 400 345T800 340V450H0z" fill="${accent}" fill-opacity=".55" stroke="${INK}" stroke-width="4"/>`+cloud(640,70,.7,'#fff');}
 else if(scene==='night'){s+=`<rect width="800" height="450" fill="${dark}"/><circle cx="${120+(h%5)*120}" cy="92" r="38" fill="#fff6d6" stroke="${INK}" stroke-width="4"/>`;for(let i=0;i<14;i++)s+=star(40+((h>>>i)%7)*115+i*5,30+((i*37+h)%150),5+(i%3)*3,'#fff6d6');s+=P(0,300,800,150,light,0);for(let i=0;i<5;i++){const w=90+((h>>>i)%4)*22,x=i*160+8;s+=P(x,200-((h>>>(i+3))%4)*28,w,110+((h>>>(i+3))%4)*28,accent,4);}}
 else {s+=P(0,275,800,175,light,0);const n=4+(h>>>3)%4,wd=Math.floor(780/n);for(let i=0;i<n;i++){const x=10+i*wd,t=(h>>>(i+2))%4,hh=130+t*28,y=275-hh+30,bw=wd-18;s+=P(x,y,bw,hh,pick([accent,dark,light,'#e0a07c'],(h>>>(i+1))+i),5);const cols=bw>100?3:2,rows=Math.max(1,Math.floor((hh-50)/52));for(let r=0;r<rows;r++)for(let c=0;c<cols;c++)s+=P(x+14+c*((bw-28)/cols),y+18+r*52,(bw-28)/cols-10,36,bg,2);}
 if((h>>>6)%2)s+=`<circle cx="${620+(h%120)}" cy="70" r="34" fill="#f7d77b" stroke="${INK}" stroke-width="4"/>`;}
 const dc=decor(h,pal,gid);s+=dc.back+dc.front;
 s+=object(m.motif||OBJECTS[scene]||'window',640,96,.7,accent);
 const A=lookOf(h,pal,0),B=lookOf(h,pal,1),K=['bunny','cat','bear','fox','bird'][(h>>>6)%5],ck=[hsl(h,45,86),hsl(h+40,60,64),hsl(h+200,50,70)];
 if(B.skin===A.skin&&B.hair===A.hair)B.hair=HAIRS[(HAIRS.indexOf(A.hair)+2)%7];
 const fig=(x,y,sc,inner,fy)=>`<g data-fig="${x},${Math.round(y-fy*sc)}" transform="translate(${x} ${y}) scale(${sc})">${inner}</g>`;
 s+=fig(245,418,1.2,rkid(A),140)+fig(430,414,1.15,rkid(B),140)+fig(590,410,1.25,critter(K,ck[(h>>>9)%3],ck[((h>>>9)+1)%3]),78);
 s+=`<rect x="6" y="6" width="788" height="438" rx="26" fill="none" stroke="${INK}" stroke-width="6" opacity=".75"/>`;
 return s;
}
function svg(e,mode){const m=meta(e),id='obra-'+(++uid),view=mode==='sticker'?(VB[m.key]||'100 40 600 400'):mode==='strip'?'110 150 600 200':mode==='face'?'140 150 210 190':'0 0 800 450',par=mode==='strip'?'xMidYMid slice':'xMidYMid meet';
 return `<svg class="obra-art obra-${esc(mode||'cover')}" data-obra="${esc(m.key)}" viewBox="${view}" width="800" height="450" preserveAspectRatio="${par}" role="img" aria-label="${esc(m.title)}"><defs><linearGradient id="${id}-s" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${m.pal[0]}"/><stop offset="1" stop-color="${m.pal[3]}"/></linearGradient><linearGradient id="${id}-g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${m.pal[1]}"/><stop offset="1" stop-color="${m.pal[2]}" stop-opacity=".85"/></linearGradient><filter id="${id}-paper"><feTurbulence type="fractalNoise" baseFrequency=".7" numOctaves="2" seed="${hash(m.w)%99}"/><feColorMatrix values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 .16 0"/></filter><radialGradient id="${id}-v"><stop offset="55%" stop-color="#fff" stop-opacity="0"/><stop offset="100%" stop-color="#2b1d3a" stop-opacity=".22"/></radialGradient></defs>${body(e,mode,id)}<rect width="800" height="450" filter="url(#${id}-paper)" opacity=".22" pointer-events="none"/><rect width="800" height="450" fill="url(#${id}-v)" pointer-events="none"/></svg>`;
}
function face(e){return svg(e,'face');}
function playerState(){try{return window.P||(0,eval)('typeof P!=="undefined"&&typeof P==="object"?P:null')}catch(_){return null}}
function coverFix(step,e){
 if(!step||!has(e))return;
 const host=step.querySelector('.ps-stage')||step.querySelector('.az-scene');
 if(host){
  host.classList.add('obra-stage');host.dataset.obraKey=key(e);
  /* Preserve only an explicitly authored hand-drawn layer. The regular
     player also places a generic backdrop in .ps-stage; treating that as
     authored made the work-specific illustration disappear. */
  const authored=host.querySelector('.obra-art,.obra-cover-hand,[data-hand-art]');
  if(!authored)host.innerHTML=svg(e,'cover');
 }
 const hero=step.querySelector('.az-hero,.fx-hero');if(hero)hero.classList.add('obra-hero');
}
const PRACTICE=new Set(['pgsheet','pgrule','pgmold','verbs','vplay','pgexp','pglab','pgspeak','pgmission']);
function strip(step,e,f){if(!PRACTICE.has(f.k)||step.querySelector('.obra-strip'))return;const m=meta(e),d=document.createElement('div');d.className='obra-strip';d.innerHTML=`<div class="obra-strip-art">${svg(e,'strip')}</div><div class="obra-strip-copy"><span>Obra em foco</span><b>${esc(m.title)}</b></div>`;const a=step.querySelector('.fx-h,.sl-hero,.wr-hero')||step.firstElementChild;if(a&&a.parentNode===step)a.before(d);else step.prepend(d);}
function sticker(step,e,f){if(f.k!=='wrap')return;const host=step.querySelector('.ps-sticker .ps-stage');if(host&&!host.dataset.obraSticker){host.classList.add('obra-stage');host.dataset.obraSticker='1';host.innerHTML=svg(e,'sticker');}}
function decorate(step,f,e){if(!has(e)||!step)return;const k=f&&f.k;if(k==='cover')coverFix(step,e);else if(k==='wrap')sticker(step,e,f);else if(PRACTICE.has(k))strip(step,e,f);}
function has(e,cid){
 const p=playerState(),course=String(cid||(p&&p.cid)||e&&e.cid||'');
 const regular=!!(e&&(/^en-/.test(course))&&(e.presentation==='regular-pilot-v1'||!e.presentation));
 return !!(regular&&workOf(e));
}
function key(e){return meta(e).key;}
window.PogObra={has,key,svg,face,coverFix,decorate,meta,THEME,KEY,VB,SCN,palette:e=>meta(e).pal,work:workOf};
const install=()=>{if(!window.PogStage||window.PogStage._obraPatch)return;const orig=window.PogStage.decorate;window.PogStage.decorate=function(step,f,e){orig.call(this,step,f,e);try{decorate(step,f,e)}catch(x){console.warn('obra-art',x)}};window.PogStage._obraPatch=1};
if(window.PogStage)install();else{let n=0;const t=setInterval(()=>{install();if(window.PogStage&&window.PogStage._obraPatch||++n>100)clearInterval(t)},20)}
})();
