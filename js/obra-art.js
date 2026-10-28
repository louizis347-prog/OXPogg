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
function workOf(e){return (e&&e.a&&e.a.w)||((e&&e.fr||[]).find(f=>f.k==='cover')||{}).obra||e&&e.t||'Pogglot';}
function keyOf(e){
 const w=workOf(e), base=norm(w).replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'').slice(0,28)||'obra';
 return 'w-'+base+'-'+hash(w).toString(36).slice(0,5);
}
function motifOf(e,w){const text=`${w} ${(e&&e.a&&e.a.k)||''} ${(e&&e.s)||''}`;return MOTIFS.find(x=>x.re.test(text))||null;}
function sceneOf(e,w){const text=`${w} ${(e&&e.sc)||''} ${(e&&e.rs)||''} ${(e&&e.s)||''}`,motif=motifOf(e,w);if(motif)return motif.scene;for(const [k,re] of Object.entries(SCENE_WORDS))if(re.test(text))return k;return 'city';}
function castIds(e,m){const motif=motifOf(e,m.w);if(motif)return motif.ids;const ids=[];const add=x=>{if(x&&!ids.includes(x))ids.push(x)};for(const f of (e&&e.fr)||[]){for(const c of (f.chars||[]))add(c[0]);for(const c of Object.values(f.cast||{})){if(Array.isArray(c))add(c[0]);}}return ids.length?ids.slice(0,3):['tom','polly'];}
const AUTO_OBJECTS=[
 [/train|railway|subway|metro|station/i,'train'],[/camera|photograph|photo|film/i,'camera'],[/newspaper|journal|press|report/i,'paper'],[/map|journey|travel|voyage|road/i,'map'],
 [/tea|coffee|cafe|café|restaurant|dinner|meal/i,'cup'],[/dance|ballerina|ballet/i,'ribbon'],[/sport|tennis|football|soccer|baseball|game/i,'trophy'],[/garden|flower|rose|spring/i,'flower'],
 [/school|classroom|teacher|student|university/i,'chalk'],[/market|shop|store|money|bank/i,'ticket'],[/ship|boat|harbor|sea|ocean/i,'anchor'],[/city|street|avenue|new york|london|paris/i,'streetlamp'],
 [/war|battle|soldier|army|king|queen|castle/i,'crown'],[/space|moon|star|planet|astronaut/i,'rocket'],[/science|laboratory|research|medicine|doctor/i,'flask'],[/painting|portrait|museum|artist|sculpture/i,'frame']
];
function objectOf(e,w,scene){const text=`${w} ${(e&&e.a&&e.a.k)||''} ${(e&&e.a&&e.a.d)||''} ${(e&&e.s)||''}`;for(const [re,obj] of AUTO_OBJECTS)if(re.test(text))return obj;return OBJECTS[scene]||'window';}

function meta(e){
 const w=workOf(e),h=hash(w),key=keyOf(e),pal=pick(PALETTES,h),motif=motifOf(e,w),scene=sceneOf(e,w);
 KEY[e&&e.n||key]=key;VB[key]='120 45 560 370';SCN[key]=scene;
 const title=w.split(/[:·–—]/)[0].trim();
 const who=(e&&e.fr||[]).flatMap(f=>Object.keys(f.cast||{})).find(Boolean)||'Pog';
 const names=['Mina','Theo','Lena','Sam','Noah','Ari'];
 const out={key,w,title,year:(e&&e.a&&e.a.y)||'',scene,pal,motif:motif&&motif.obj||objectOf(e,w,scene),ids:castIds(e,{w}),who,names:[names[h%names.length],names[(h>>>4)%names.length]]};
 THEME[key]=out;return out;
}
function P(x,y,w,h,fill,rx){return `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${rx||0}" fill="${fill}" stroke="${INK}" stroke-width="4"/>`;}
function E(x,y,rx,ry,fill){return `<ellipse cx="${x}" cy="${y}" rx="${rx}" ry="${ry}" fill="${fill}" stroke="${INK}" stroke-width="4"/>`;}
function L(x1,y1,x2,y2,stroke,sw){return `<path d="M${x1} ${y1}L${x2} ${y2}" fill="none" stroke="${stroke||INK}" stroke-width="${sw||4}" stroke-linecap="round"/>`;}
function cloud(x,y,s,c){return `<g transform="translate(${x} ${y}) scale(${s})" fill="${c}" stroke="${INK}" stroke-width="3"><ellipse cx="0" cy="8" rx="36" ry="13"/><ellipse cx="26" cy="1" rx="25" ry="18"/><ellipse cx="-22" cy="2" rx="22" ry="16"/></g>`;}
function star(x,y,s,c){return `<path d="M${x} ${y-s}l${s*.28} ${s*.62} ${s*.72} ${s*.1}-${s*.55} ${s*.48} ${s*.18} ${s*.7}-${s*.63}-${s*.38}-${s*.58} ${s*.42} ${s*.18}-${s*.7}z" fill="${c}" stroke="${INK}" stroke-width="2"/>`;}
function kid(x,y,s,skin,hair,shirt,flip){
 const tr=`translate(${x} ${y}) scale(${flip?-s:s} ${s})`;
 return `<g transform="${tr}" stroke="${INK}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"><path d="M-28 90L-38 150M28 90L38 150" fill="none"/><path d="M-43 150h18M25 150h18" fill="none"/><path d="M-48 72Q-48 36 0 30Q48 36 48 72v54h-96z" fill="${shirt}"/><circle cx="0" cy="0" r="40" fill="${skin}"/><path d="M-40-8Q-34-49 0-48Q36-48 42-6Q23-24 0-20Q-22-26-40-8z" fill="${hair}"/><circle cx="-14" cy="2" r="4" fill="${INK}" stroke="none"/><circle cx="14" cy="2" r="4" fill="${INK}" stroke="none"/><path d="M-12 20Q0 29 12 20" fill="none"/></g>`;
}
function charFor(id,x,y,s,flip,fall){
 try{if(window.PogChars&&PogChars.svg){const raw=PogChars.svg(id);if(raw){const inner=raw.replace(/^<svg[^>]*>/,'').replace(/<\/svg>\s*$/,'');return `<g transform="translate(${x-50*s} ${y}) scale(${flip?-s:s} ${s})" filter="drop-shadow(0 5px 5px rgba(43,29,58,.2))">${inner}</g>`;}}}catch(e){}
 return kid(x,y,s,fall.skin,fall.hair,fall.shirt,flip);
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
function body(e,mode){
 const m=meta(e),{pal,scene}=m,h=hash(m.w),bg=pal[3],accent=pal[1],dark=pal[2],light=pal[0];
 let s=`<rect width="800" height="450" fill="${bg}"/>`;
 if(scene==='water'){s+=`<path d="M0 290Q110 250 220 290T440 290T660 290T880 290V450H0z" fill="${light}" stroke="${INK}" stroke-width="4"/>`;for(let i=0;i<5;i++)s+=`<path d="M${i*175-20} 332q42-17 84 0t84 0" fill="none" stroke="${accent}" stroke-width="7" stroke-linecap="round"/>`;s+=cloud(115,72,.8,'#fff');}
 else if(scene==='forest'){s+=`<path d="M0 320Q150 260 300 320T600 320T900 320V450H0z" fill="${light}" stroke="${INK}" stroke-width="4"/>`;for(let i=0;i<6;i++){const x=i*150+35;s+=`<path d="M${x} 330L${x+14} 125L${x+28} 330z" fill="${accent}" stroke="${INK}" stroke-width="4"/><circle cx="${x+14}" cy="${125+(i%2)*25}" r="34" fill="${dark}" stroke="${INK}" stroke-width="4"/>`;}}
 else if(scene==='stage'){s+=`<path d="M0 0h170v450H0zM630 0h170v450H630z" fill="${accent}" stroke="${INK}" stroke-width="4"/><rect x="170" width="460" height="450" fill="${bg}" stroke="${INK}" stroke-width="4"/>`;for(let i=0;i<4;i++)s+=star(250+i*105,78+(i%2)*20,12,light);}
 else if(scene==='lab'){s+=`<rect x="0" y="310" width="800" height="140" fill="${light}" stroke="${INK}" stroke-width="4"/>`;for(let i=0;i<5;i++)s+=`<circle cx="${110+i*145}" cy="${90+(i%2)*35}" r="${18+(i%3)*5}" fill="${accent}" fill-opacity=".28" stroke="${INK}" stroke-width="3"/>`;}
 else if(scene==='library'){s+=P(40,55,720,300,'#f4e4c8',8);for(let r=0;r<3;r++)for(let i=0;i<10;i++)s+=P(65+i*68,80+r*78,46,56,pick([accent,light,dark,'#d88970'],(h+i+r)%4),3);s+=P(0,355,800,95,light,0);}
 else if(scene==='museum'){s+=P(40,55,720,300,'#eee4d4',8);for(let i=0;i<4;i++)s+=object('frame',76+i*185,95+(i%2)*28,.8,pick([accent,light,dark],(h+i)%3));s+=P(0,355,800,95,light,0);}
 else if(scene==='kitchen'){s+=P(0,280,800,170,light,0)+P(60,84,680,210,'#f4e9d7',8)+object('cup',630,150,1,accent);}
 else {s+=P(0,275,800,175,light,0);for(let i=0;i<6;i++){const x=40+i*135;s+=P(x,125-(i%2)*35,98,150+(i%2)*35,accent,5)+P(x+18,147-(i%2)*35,28,42,bg,2)+P(x+57,147-(i%2)*35,28,42,bg,2);}}
 s+=object(m.motif||OBJECTS[scene]||'window',575,188,.85,accent);
 const skins=['#f1c7a8','#c88e67','#8b5a3c','#f5d3ba'],hairs=['#2b1d3a','#5a3425','#a65d2f','#243b53'],shirts=[accent,light,dark,'#c65b6f'],fallback={skin:skins[h%4],hair:hairs[(h>>>2)%4],shirt:shirts[(h>>>3)%4]};
 const ids=m.ids&&m.ids.length?m.ids:['tom','polly'];
 s+=`<g class="obra-shadow"><ellipse cx="303" cy="374" rx="96" ry="15" fill="#2b1d3a" opacity=".14"/><ellipse cx="525" cy="374" rx="96" ry="15" fill="#2b1d3a" opacity=".14"/></g>`;
 s+=charFor(ids[0],300,220,.95,false,fallback);
 s+=charFor(ids[1]||ids[0],525,226,.9,true,fallback);
 s+=`<rect x="6" y="6" width="788" height="438" rx="26" fill="none" stroke="${INK}" stroke-width="6" opacity=".75"/>`;
 return s;
}
function svg(e,mode){const m=meta(e),id='obra-'+(++uid),view=mode==='sticker'?(VB[m.key]||'155 58 490 355'):mode==='strip'?'0 205 800 120':mode==='face'?'245 150 310 230':'0 0 800 450';
 return `<svg class="obra-art obra-${esc(mode||'cover')}" data-obra="${esc(m.key)}" viewBox="${view}" width="800" height="450" preserveAspectRatio="xMidYMid meet" role="img" aria-label="${esc(m.title)}"><defs><filter id="${id}-paper"><feTurbulence type="fractalNoise" baseFrequency=".7" numOctaves="2" seed="${hash(m.w)%99}"/><feColorMatrix values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 .16 0"/></filter><radialGradient id="${id}-v"><stop offset="55%" stop-color="#fff" stop-opacity="0"/><stop offset="100%" stop-color="#2b1d3a" stop-opacity=".22"/></radialGradient></defs>${body(e,mode)}<rect width="800" height="450" filter="url(#${id}-paper)" opacity=".22" pointer-events="none"/><rect width="800" height="450" fill="url(#${id}-v)" pointer-events="none"/></svg>`;
}
function face(e){return svg(e,'face');}
function coverFix(step,e){
 if(!step||!has(e))return;
 const host=step.querySelector('.ps-stage')||step.querySelector('.az-scene');
 if(host){host.classList.add('obra-stage');host.dataset.obraKey=key(e);host.innerHTML=svg(e,'cover');}
 const hero=step.querySelector('.az-hero,.fx-hero');if(hero)hero.classList.add('obra-hero');
}
const PRACTICE=new Set(['pgsheet','pgrule','pgmold','verbs','vplay','pgexp','pglab','pgspeak','pgmission']);
function strip(step,e,f){if(!PRACTICE.has(f.k)||step.querySelector('.obra-strip'))return;const m=meta(e),d=document.createElement('div');d.className='obra-strip';d.innerHTML=`<div class="obra-strip-art">${svg(e,'strip')}</div><div class="obra-strip-copy"><span>Obra em foco</span><b>${esc(m.title)}</b></div>`;const a=step.querySelector('.fx-h,.sl-hero,.wr-hero')||step.firstElementChild;if(a&&a.parentNode===step)a.before(d);else step.prepend(d);}
function sticker(step,e,f){if(f.k!=='wrap')return;const host=step.querySelector('.ps-sticker .ps-stage');if(host&&!host.dataset.obraSticker){host.classList.add('obra-stage');host.dataset.obraSticker='1';host.innerHTML=svg(e,'sticker');}}
function decorate(step,f,e){if(!has(e)||!step)return;const k=f&&f.k;if(k==='cover')coverFix(step,e);else if(k==='wrap')sticker(step,e,f);else if(PRACTICE.has(k))strip(step,e,f);}
function has(e){return !!(e&&/^en-/.test(String(window.P&&P.cid||''))&&e.presentation==='regular-pilot-v1'&&workOf(e));}
function key(e){return meta(e).key;}
window.PogObra={has,key,svg,face,coverFix,decorate,meta,THEME,KEY,VB,SCN,palette:e=>meta(e).pal,work:workOf};
const install=()=>{if(!window.PogStage||window.PogStage._obraPatch)return;const orig=window.PogStage.decorate;window.PogStage.decorate=function(step,f,e){orig.call(this,step,f,e);try{decorate(step,f,e)}catch(x){console.warn('obra-art',x)}};window.PogStage._obraPatch=1};
if(window.PogStage)install();else{let n=0;const t=setInterval(()=>{install();if(window.PogStage&&window.PogStage._obraPatch||++n>100)clearInterval(t)},20)}
})();
