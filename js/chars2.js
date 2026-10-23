/* Pogglot · personagens ilustrados (parte 2): elenco das obras dos episódios 86–110 do A1 de inglês.
   Mesmo desenho 100×150 de js/chars.js (pés em y=146, cabeça em torno de (50,48)). Estende window.PogChars. */
(function(){
'use strict';
if(!window.PogChars)return;
const SK='#f4c7a1';
const eye=(x,y,r)=>`<circle cx="${x}" cy="${y}" r="${r||3.2}" fill="#2a2230"/><circle cx="${x+1}" cy="${y-1.1}" r="${(r||3.2)*.38}" fill="#fff"/>`;
const cheek=(x,y)=>`<ellipse cx="${x}" cy="${y}" rx="4.2" ry="2.6" fill="#ff8aa0" opacity=".45"/>`;
const smile=(x,y,w)=>`<path d="M${x-w} ${y} Q${x} ${y+w*.9} ${x+w} ${y}" stroke="#7a3b2e" stroke-width="2" fill="none" stroke-linecap="round"/>`;
const shadow='<ellipse cx="50" cy="146" rx="26" ry="3.6" fill="#000" opacity=".16"/>';
const wrap=b=>`<svg class="ps-ch" viewBox="0 0 100 150" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true">${shadow}${b}</svg>`;
const hand=(x,y,c)=>`<circle cx="${x}" cy="${y}" r="5.5" fill="${c||SK}"/>`;

/* ---------- crianças e adultos ---------- */
const HAIR={
  short:h=>`<path d="M26 48 Q26 22 50 22 Q74 22 74 48 Q64 34 50 36 Q36 34 26 48Z" fill="${h}"/>`,
  tuft:h=>`<path d="M26 48 Q26 22 50 22 Q74 22 74 48 Q64 34 50 36 Q36 34 26 48Z" fill="${h}"/><path d="M44 24 Q50 8 58 22Z" fill="${h}"/>`,
  long:h=>`<path d="M24 52 Q20 86 32 96 Q30 64 34 44Z M76 52 Q80 86 68 96 Q70 64 66 44Z" fill="${h}"/><path d="M26 48 Q26 22 50 22 Q74 22 74 48 Q64 34 50 36 Q36 34 26 48Z" fill="${h}"/>`,
  bob:h=>`<path d="M23 58 Q20 20 50 19 Q80 20 77 58 Q72 66 66 56 L34 56 Q28 66 23 58Z" fill="${h}"/><path d="M30 46 Q50 28 70 46 Q60 36 50 38 Q40 36 30 46Z" fill="${SK}" opacity="0"/>`,
  braids:h=>`<path d="M28 50 Q28 74 24 90" stroke="${h}" stroke-width="8" stroke-linecap="round" fill="none"/><path d="M72 50 Q72 74 76 90" stroke="${h}" stroke-width="8" stroke-linecap="round" fill="none"/><circle cx="24" cy="92" r="3.2" fill="#d62828"/><circle cx="76" cy="92" r="3.2" fill="#d62828"/><path d="M26 48 Q26 22 50 22 Q74 22 74 48 Q64 34 50 36 Q36 34 26 48Z" fill="${h}"/>`,
  bun:h=>`<circle cx="50" cy="17" r="10" fill="${h}"/><path d="M26 48 Q26 22 50 22 Q74 22 74 48 Q64 34 50 36 Q36 34 26 48Z" fill="${h}"/>`,
  curly:h=>`<g fill="${h}"><circle cx="30" cy="38" r="8"/><circle cx="40" cy="28" r="9"/><circle cx="52" cy="25" r="9"/><circle cx="63" cy="29" r="9"/><circle cx="71" cy="39" r="8"/></g>`,
  none:()=>'',
};
const HAT={
  straw:()=>`<ellipse cx="50" cy="33" rx="33" ry="7" fill="#e5c26a"/><path d="M33 33 Q35 12 50 12 Q65 12 67 33Z" fill="#f0d27e"/><path d="M33 29 Q50 35 67 29" stroke="#b5482b" stroke-width="3" fill="none"/>`,
  cap:c=>`<path d="M27 38 Q28 16 50 16 Q72 16 73 38 Q50 30 27 38Z" fill="${c}"/><path d="M62 33 Q86 30 90 38 Q76 40 62 38Z" fill="${c}"/>`,
  captain:()=>`<ellipse cx="50" cy="36" rx="28" ry="5" fill="#1d2b4a"/><path d="M28 36 Q30 14 50 13 Q70 14 72 36Z" fill="#26386a"/><rect x="46" y="22" width="8" height="8" rx="2" fill="#f2c94c"/>`,
  bonnet:c=>`<path d="M24 56 Q18 18 50 16 Q82 18 76 56 Q66 36 50 38 Q34 36 24 56Z" fill="${c}"/><path d="M26 54 Q36 40 50 42 Q64 40 74 54" stroke="#fff" stroke-width="2.4" fill="none"/>`,
  cocked:()=>`<path d="M16 38 Q26 14 50 14 Q74 14 84 38 Q50 26 16 38Z" fill="#5b3b8a"/><path d="M16 38 Q50 44 84 38" stroke="#3d2563" stroke-width="3" fill="none"/><path d="M62 22 Q92 6 94 26 Q82 16 66 28Z" fill="#e8434d"/>`,
  tophat:()=>`<ellipse cx="50" cy="33" rx="28" ry="5.5" fill="#1c1722"/><rect x="34" y="6" width="32" height="28" rx="3" fill="#2b2531"/><rect x="34" y="24" width="32" height="5" fill="#8b1e2d"/>`,
  baseball:()=>`<path d="M27 38 Q28 16 50 16 Q72 16 73 38 Q50 30 27 38Z" fill="#c0392b"/><path d="M62 33 Q86 30 90 38 Q76 40 62 38Z" fill="#8f1f17"/><circle cx="50" cy="26" r="4.5" fill="#fff"/>`,
};
function kid(o){
  o=Object.assign({skin:SK,top:'#5b8def',bot:'#3a4a7a',shoe:'#4a3320',hair:'#6b3f26',style:'short',hat:'',hatc:'#3b6fd0',skirt:0,beard:'',stache:'',extra:'',front:'',stripe:'',bare:0},o);
  const sk=o.skin;
  const legs=o.skirt?`<rect x="39" y="128" width="8" height="14" rx="3" fill="${sk}"/><rect x="53" y="128" width="8" height="14" rx="3" fill="${sk}"/>`:
    `<rect x="38" y="122" width="10" height="21" rx="4" fill="${o.bot}"/><rect x="52" y="122" width="10" height="21" rx="4" fill="${o.bot}"/>`;
  const shoes=o.bare?`<ellipse cx="42" cy="143" rx="7" ry="3.6" fill="${sk}"/><ellipse cx="58" cy="143" rx="7" ry="3.6" fill="${sk}"/>`:`<ellipse cx="42" cy="143" rx="9" ry="4.4" fill="${o.shoe}"/><ellipse cx="58" cy="143" rx="9" ry="4.4" fill="${o.shoe}"/>`;
  const body=o.skirt?`<path d="M50 74 L24 134 Q50 142 76 134 Z" fill="${o.top}"/><path d="M36 112 H64 M32 122 H68" stroke="#fff" stroke-width="2" opacity=".35"/>`:
    `<path d="M27 126 Q23 88 38 78 L62 78 Q77 88 73 126 Z" fill="${o.top}"/>${o.stripe?[92,102,112,122].map(y=>`<path d="M26 ${y} H74" stroke="${o.stripe}" stroke-width="3.4"/>`).join(''):''}<path d="M50 78 V126" stroke="#000" stroke-width="1.4" opacity=".14"/>`;
  const collar=`<path d="M40 76 L50 88 L60 76Z" fill="#fff" opacity=".9"/>`;
  const hairF=(HAIR[o.style]||HAIR.short)(o.hair);
  const beard=o.beard?`<path d="M30 56 Q30 82 50 84 Q70 82 70 56 Q62 70 50 68 Q38 70 30 56Z" fill="${o.beard}"/>`:'';
  const stache=o.stache?`<path d="M38 60 Q50 54 62 60 Q56 66 50 62 Q44 66 38 60Z" fill="${o.stache}"/>`:'';
  const hat=o.hat?(HAT[o.hat]?HAT[o.hat](o.hatc):''):'';
  return wrap(`${legs}${shoes}${body}${o.skirt?'':collar}${hand(24,106,sk)}${hand(76,106,sk)}
 ${o.style==='long'||o.style==='braids'?hairF:''}
 <circle cx="50" cy="48" r="24" fill="${sk}"/>${o.style==='long'||o.style==='braids'?'':hairF}
 ${o.style==='long'||o.style==='braids'?HAIR.short(o.hair):''}
 ${eye(41,50)}${eye(59,50)}${cheek(35,58)}${cheek(65,58)}${beard}${o.beard?'':smile(50,61,6)}${stache}${hat}${o.front}${o.extra}`);
}

/* ---------- bichos de pé ---------- */
function mouse(o){
  o=Object.assign({fur:'#9aa3b5',belly:'#e6e9f0',cloth:'#b8352f',hat:'',tie:1,tail:'#c9a0a0'},o);
  return wrap(`<path d="M72 128 Q98 124 92 100 Q90 116 70 120" stroke="${o.tail}" stroke-width="5" fill="none" stroke-linecap="round"/>
 <ellipse cx="40" cy="142" rx="9" ry="4.2" fill="${o.fur}"/><ellipse cx="60" cy="142" rx="9" ry="4.2" fill="${o.fur}"/>
 <path d="M28 130 Q25 90 38 80 L62 80 Q75 90 72 130 Z" fill="${o.cloth}"/><ellipse cx="50" cy="108" rx="11" ry="18" fill="${o.belly}" opacity=".9"/>
 ${o.tie?`<path d="M45 80 L50 88 L55 80Z M48 88 L52 88 L53 102 L50 106 L47 102Z" fill="#f2c94c"/>`:''}
 ${hand(25,106,o.fur)}${hand(75,106,o.fur)}
 <circle cx="29" cy="32" r="13" fill="${o.fur}"/><circle cx="71" cy="32" r="13" fill="${o.fur}"/><circle cx="29" cy="32" r="7.5" fill="#ffb3c4"/><circle cx="71" cy="32" r="7.5" fill="#ffb3c4"/>
 <ellipse cx="50" cy="54" rx="22" ry="21" fill="${o.fur}"/><ellipse cx="50" cy="62" rx="12" ry="9" fill="${o.belly}"/>
 ${eye(41,50,3)}${eye(59,50,3)}<circle cx="50" cy="58" r="3.4" fill="#ff8aa0"/>
 <path d="M44 66 Q50 71 56 66" stroke="#7a3b2e" stroke-width="1.8" fill="none" stroke-linecap="round"/>
 <path d="M30 60 L14 56 M30 64 L14 66 M70 60 L86 56 M70 64 L86 66" stroke="#555" stroke-width="1" stroke-linecap="round"/>${o.hat==='straw'?HAT.straw():''}`);
}
function peterrabbit(){
  return wrap(`<ellipse cx="40" cy="142" rx="10" ry="4.4" fill="#a9733f"/><ellipse cx="60" cy="142" rx="10" ry="4.4" fill="#a9733f"/>
 <path d="M28 130 Q26 88 38 78 L62 78 Q74 88 72 130 Z" fill="#2f6bb8"/><path d="M50 80 V128" stroke="#1f4f8f" stroke-width="2"/><circle cx="44" cy="96" r="2.4" fill="#f2c94c"/><circle cx="44" cy="110" r="2.4" fill="#f2c94c"/><circle cx="44" cy="124" r="2.4" fill="#f2c94c"/>
 ${hand(24,104,'#b9824a')}${hand(76,104,'#b9824a')}
 <ellipse cx="37" cy="24" rx="7.5" ry="19" fill="#b9824a"/><ellipse cx="63" cy="24" rx="7.5" ry="19" fill="#b9824a"/><ellipse cx="37" cy="26" rx="3.6" ry="13" fill="#f3c9a4"/><ellipse cx="63" cy="26" rx="3.6" ry="13" fill="#f3c9a4"/>
 <circle cx="50" cy="54" r="22" fill="#b9824a"/><ellipse cx="50" cy="62" rx="12" ry="9" fill="#f1dcc0"/>
 ${eye(41,50,3)}${eye(59,50,3)}<ellipse cx="50" cy="57" rx="3.6" ry="2.6" fill="#7a3b2e"/>
 <path d="M44 65 Q50 70 56 65" stroke="#7a3b2e" stroke-width="1.8" fill="none" stroke-linecap="round"/>`);
}
function lamb(){
  return wrap(`<ellipse cx="40" cy="142" rx="8" ry="4" fill="#3a2f33"/><ellipse cx="60" cy="142" rx="8" ry="4" fill="#3a2f33"/>
 <rect x="35" y="118" width="7" height="24" rx="3" fill="#3a2f33"/><rect x="58" y="118" width="7" height="24" rx="3" fill="#3a2f33"/>
 <g fill="#fbf7f2" stroke="#e8e0d6" stroke-width="1.2"><circle cx="30" cy="104" r="14"/><circle cx="70" cy="104" r="14"/><circle cx="50" cy="96" r="17"/><circle cx="36" cy="120" r="12"/><circle cx="64" cy="120" r="12"/><circle cx="50" cy="118" r="14"/></g>
 <path d="M28 40 Q16 34 14 48 Q22 54 32 50Z" fill="#3a2f33"/><path d="M72 40 Q84 34 86 48 Q78 54 68 50Z" fill="#3a2f33"/>
 <g fill="#fbf7f2" stroke="#e8e0d6" stroke-width="1.2"><circle cx="38" cy="30" r="9"/><circle cx="50" cy="26" r="10"/><circle cx="62" cy="30" r="9"/></g>
 <ellipse cx="50" cy="52" rx="19" ry="21" fill="#3a2f33"/>
 ${eye(43,48,3)}${eye(57,48,3)}<ellipse cx="50" cy="58" rx="3" ry="2.2" fill="#ff8aa0"/><path d="M45 64 Q50 68 55 64" stroke="#fff" stroke-width="1.6" fill="none" stroke-linecap="round"/>
 <path d="M38 76 Q50 84 62 76 L60 84 Q50 90 40 84Z" fill="#e8434d"/>`);
}
function wolf(){
  return wrap(`<path d="M74 128 Q100 130 96 104 Q92 120 72 122" fill="#7b8794"/>
 <ellipse cx="40" cy="142" rx="10" ry="4.6" fill="#4b5563"/><ellipse cx="60" cy="142" rx="10" ry="4.6" fill="#4b5563"/>
 <path d="M26 130 Q22 88 38 78 L62 78 Q78 88 74 130 Z" fill="#8a96a3"/><path d="M38 100 Q50 118 62 100 L62 128 Q50 132 38 128Z" fill="#cbd2d9"/>
 ${hand(23,106,'#6f7b88')}${hand(77,106,'#6f7b88')}
 <path d="M26 44 L22 12 L44 28Z" fill="#6f7b88"/><path d="M74 44 L78 12 L56 28Z" fill="#6f7b88"/><path d="M29 38 L27 22 L38 30Z" fill="#f4a5b3"/><path d="M71 38 L73 22 L62 30Z" fill="#f4a5b3"/>
 <ellipse cx="50" cy="52" rx="26" ry="23" fill="#8a96a3"/><ellipse cx="50" cy="64" rx="15" ry="12" fill="#cbd2d9"/>
 <ellipse cx="39" cy="48" rx="6" ry="6.5" fill="#fff4b3"/><ellipse cx="61" cy="48" rx="6" ry="6.5" fill="#fff4b3"/><circle cx="39" cy="49" r="2.6" fill="#2a2230"/><circle cx="61" cy="49" r="2.6" fill="#2a2230"/>
 <path d="M34 40 L45 44 M66 40 L55 44" stroke="#3a4350" stroke-width="2.2" stroke-linecap="round"/>
 <path d="M44 58 L56 58 L50 65Z" fill="#2a2230"/><path d="M38 70 Q50 82 62 70 Q50 74 38 70Z" fill="#fff" stroke="#7a3b2e" stroke-width="1.4"/><path d="M42 71 V75 M50 73 V78 M58 71 V75" stroke="#7a3b2e" stroke-width="1.2"/>`);
}
function kitten(o){
  o=Object.assign({fur:'#e0a35a',belly:'#fbe6c4',mit:'#e8434d',stripe:'#b9782e',bow:'#4aa3e0'},o);
  return wrap(`<path d="M76 128 Q104 120 94 90 Q94 112 72 120" stroke="${o.fur}" stroke-width="8" fill="none" stroke-linecap="round"/>
 <ellipse cx="40" cy="142" rx="10" ry="4.6" fill="${o.fur}"/><ellipse cx="60" cy="142" rx="10" ry="4.6" fill="${o.fur}"/>
 <path d="M27 130 Q23 88 38 78 L62 78 Q77 88 73 130 Z" fill="${o.fur}"/><ellipse cx="50" cy="108" rx="13" ry="20" fill="${o.belly}"/>
 <path d="M30 96 H38 M30 108 H38 M62 96 H70 M62 108 H70" stroke="${o.stripe}" stroke-width="3" stroke-linecap="round"/>
 <path d="M22 104 L16 118" stroke="${o.fur}" stroke-width="9" stroke-linecap="round"/><path d="M78 104 L84 118" stroke="${o.fur}" stroke-width="9" stroke-linecap="round"/>
 <circle cx="15" cy="121" r="7" fill="${o.mit}"/><circle cx="85" cy="121" r="7" fill="${o.mit}"/>
 <path d="M24 46 L22 14 L44 30Z" fill="${o.fur}"/><path d="M76 46 L78 14 L56 30Z" fill="${o.fur}"/><path d="M28 40 L27 24 L38 31Z" fill="#ffb3c4"/><path d="M72 40 L73 24 L62 31Z" fill="#ffb3c4"/>
 <ellipse cx="50" cy="52" rx="27" ry="23" fill="${o.fur}"/><path d="M42 32 V40 M50 30 V38 M58 32 V40" stroke="${o.stripe}" stroke-width="3" stroke-linecap="round"/>
 <ellipse cx="50" cy="62" rx="14" ry="10" fill="${o.belly}"/>
 ${eye(40,50,3.4)}${eye(60,50,3.4)}<path d="M47 58 L53 58 L50 62Z" fill="#ff8aa0"/><path d="M44 65 Q50 70 56 65" stroke="#7a3b2e" stroke-width="1.8" fill="none" stroke-linecap="round"/>
 <path d="M30 60 L12 56 M30 64 L12 66 M70 60 L88 56 M70 64 L88 66" stroke="#666" stroke-width="1" stroke-linecap="round"/>
 <path d="M42 78 L50 82 L58 78 L58 86 L50 83 L42 86Z" fill="${o.bow}"/><circle cx="50" cy="82" r="3" fill="${o.bow}"/>`);
}

/* ---------- elenco ---------- */
const bowl='<ellipse cx="50" cy="120" rx="13" ry="3.4" fill="#8a6a3b"/><path d="M37 112 Q38 126 50 126 Q62 126 63 112Z" fill="#c9a064"/>';
const pail='<path d="M84 96 Q90 80 78 82" stroke="#6b7280" stroke-width="2" fill="none"/><path d="M76 96 H92 L90 114 H78Z" fill="#8aa0b8" stroke="#5b6f86" stroke-width="1.4"/>';
const book='<rect x="30" y="102" width="40" height="26" rx="3" fill="#d9822b"/><rect x="33" y="105" width="34" height="20" rx="2" fill="#fff4d6"/><path d="M50 105 V125" stroke="#c9a064" stroke-width="1.6"/><path d="M36 111 H47 M36 116 H47 M53 111 H64 M53 116 H64" stroke="#b8a37a" stroke-width="1.4"/>';
const staff='<path d="M90 70 V142" stroke="#8a5a2b" stroke-width="3.4" stroke-linecap="round"/><path d="M90 70 Q98 66 96 76" stroke="#8a5a2b" stroke-width="3" fill="none" stroke-linecap="round"/>';
const sword='<path d="M86 84 L96 134" stroke="#cfd6de" stroke-width="3.4" stroke-linecap="round"/><path d="M80 90 L92 86" stroke="#c9a064" stroke-width="3.4" stroke-linecap="round"/>';
const whistle='<circle cx="50" cy="92" r="4.2" fill="#e8434d"/><path d="M50 78 V90" stroke="#e8434d" stroke-width="1.4"/>';
const ball='<circle cx="82" cy="118" r="8" fill="#fff" stroke="#c0392b" stroke-width="1.4"/><path d="M76 112 Q82 118 76 124 M88 112 Q82 118 88 124" stroke="#c0392b" stroke-width="1.2" fill="none"/>';
const cross='<path d="M44 92 H56 M50 84 V104" stroke="#f2c94c" stroke-width="3.4" stroke-linecap="round"/>';
const C={
  polly:()=>kid({skirt:1,top:'#f2b84b',hair:'#8a5a3b',style:'braids',shoe:'#c0392b'}),
  tommy:()=>kid({top:'#d6453d',bot:'#355a8f',hair:'#c98a2e',style:'tuft',extra:bowl}),
  oliver:()=>kid({top:'#a98f6b',bot:'#6b5a45',hair:'#8a5a3b',style:'short',bare:1,extra:bowl}),
  bumble:()=>kid({top:'#3b3340',bot:'#2b2531',hair:'#7a7a7a',style:'none',hat:'tophat',skin:'#e8b894',stache:'#6b6b6b',shoe:'#1c1722'}),
  ishmael:()=>kid({top:'#f4f4f6',stripe:'#3a63b5',bot:'#2b3a5a',hair:'#4b3320',style:'short',hat:'cap',hatc:'#2b4a7a'}),
  ahab:()=>kid({top:'#26386a',bot:'#1d2b4a',hair:'#d8d8d8',style:'none',hat:'captain',beard:'#d8d8d8',skin:'#e0aa84',shoe:'#1c1722',front:'<circle cx="59" cy="50" r="5.6" fill="#1c1722"/><path d="M27 42 L59 50 L73 45" stroke="#1c1722" stroke-width="1.6" fill="none"/>'}),
  townmouse:()=>mouse({fur:'#9aa3b5',cloth:'#b8352f',tie:1}),
  countrymouse:()=>mouse({fur:'#b98a5a',belly:'#f1dcc0',cloth:'#4f8f4a',tie:0,hat:'straw',tail:'#d9b79a'}),
  mary:()=>kid({skirt:1,top:'#f48fb1',hair:'#a8602a',style:'bob',hat:'bonnet',hatc:'#f8bbd0',shoe:'#7a3b2e'}),
  lamb:()=>lamb(),
  shepherd:()=>kid({top:'#5fa35a',bot:'#6b5a45',hair:'#8a5a2b',style:'short',hat:'straw',extra:staff}),
  wolf:()=>wolf(),
  matilda:()=>kid({skirt:1,top:'#4a7fd0',hair:'#3a2a22',style:'bob',extra:book,front:'<path d="M28 34 Q50 22 72 34" stroke="#e8434d" stroke-width="4" fill="none" stroke-linecap="round"/>',shoe:'#6b3a2a'}),
  misshoney:()=>kid({skirt:1,top:'#c9a0dc',hair:'#b9824a',style:'long',skin:'#f4c7a1',shoe:'#7a3b2e'}),
  jack:()=>kid({top:'#d6453d',bot:'#3a4a7a',hair:'#c98a2e',style:'curly',extra:pail}),
  jill:()=>kid({skirt:1,top:'#f2c94c',hair:'#6b3f26',style:'braids',extra:pail,shoe:'#7a3b2e'}),
  tom:()=>kid({top:'#f4f0e6',bot:'#7a5a3a',hair:'#8a5a2b',style:'short',hat:'straw',bare:1,front:'<path d="M34 80 V120 M66 80 V120" stroke="#7a5a3a" stroke-width="4"/>'}),
  huck:()=>kid({top:'#8aa07a',bot:'#6b5a45',hair:'#4b3320',style:'short',hat:'straw',bare:1,front:'<rect x="40" y="96" width="8" height="8" fill="#c9a064"/>',skin:'#e8b894'}),
  peterrabbit:()=>peterrabbit(),
  mcgregor:()=>kid({top:'#6b8f4a',bot:'#4a6aa0',hair:'#5b3b1c',style:'none',hat:'straw',stache:'#5b3b1c',skin:'#e8b894',shoe:'#4a3320'}),
  kittenA:()=>kitten({fur:'#9aa3b5',belly:'#e6e9f0',mit:'#e8434d',stripe:'#6f7b88',bow:'#4aa3e0'}),
  kittenB:()=>kitten({fur:'#e0a35a',belly:'#fbe6c4',mit:'#3a63b5',stripe:'#b9782e',bow:'#e8434d'}),
  dartagnan:()=>kid({top:'#3a63b5',bot:'#2b3a5a',hair:'#5b3b1c',style:'long',hat:'cocked',stache:'#5b3b1c',extra:sword,front:cross,shoe:'#2b1b12'}),
  athos:()=>kid({top:'#26386a',bot:'#1d2b4a',hair:'#3a2a22',style:'short',hat:'cocked',beard:'#3a2a22',extra:sword,front:cross,shoe:'#2b1b12'}),
  slugger:()=>kid({top:'#fff',stripe:'#c0392b',bot:'#fff',hair:'#6b3f26',style:'short',hat:'baseball',extra:ball,shoe:'#222'}),
  coach:()=>kid({top:'#26386a',bot:'#2b3a5a',hair:'#d8d8d8',style:'none',hat:'cap',hatc:'#26386a',skin:'#e0aa84',extra:whistle,stache:'#d8d8d8'})
};

const old=window.PogChars;
const shadowRe=shadow;
window.PogChars={
  ids:old.ids.concat(Object.keys(C)),
  svg:id=>C[id]?C[id]():old.svg(id),
  face:id=>C[id]?C[id]().replace('viewBox="0 0 100 150"','viewBox="14 2 72 72"').replace(shadowRe,''):old.face(id)
};
})();
