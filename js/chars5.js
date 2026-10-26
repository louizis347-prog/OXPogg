/* Pogglot · personagens ilustrados (parte 5): elenco reconhecível das obras do curso regular de inglês.
   Cada personagem é uma ficha (cores, chapéu, adereço) desenhada com PogPerson; sem arte oficial. */
(function(){
'use strict';
if(!window.PogChars||!window.PogPerson)return;
const {person,HATS}=window.PogPerson;
HATS.witch=o=>`<ellipse cx="50" cy="32" rx="30" ry="5" fill="#2b2531"/><path d="M36 32 L50 -4 L64 32Z" fill="#2b2531"/><rect x="38" y="24" width="24" height="5" fill="${o.hatc||'#8b5cf6'}"/>`;
HATS.tiara=o=>`<path d="M36 28 L40 18 L46 26 L50 14 L54 26 L60 18 L64 28Z" fill="#f2c94c"/><circle cx="50" cy="20" r="2.4" fill="#e8434d"/>`;
HATS.bow=o=>`<path d="M50 24 L38 16 L38 32Z M50 24 L62 16 L62 32Z" fill="${o.hatc||'#e8434d'}"/><circle cx="50" cy="24" r="4" fill="${o.hatc||'#e8434d'}"/>`;
HATS.green=o=>`<path d="M28 36 Q30 14 52 14 L76 8 L66 22 Q72 30 72 36Z" fill="${o.hatc||'#3f9a5a'}"/><path d="M66 20 L78 6" stroke="#e8434d" stroke-width="3" stroke-linecap="round"/>`;
const gl='<g fill="none" stroke="#2a2230" stroke-width="2"><circle cx="41" cy="48" r="7"/><circle cx="59" cy="48" r="7"/><path d="M48 48 H52"/></g>';
const cape=c=>`<path d="M30 80 L18 132 Q50 142 82 132 L70 80Z" fill="${c}"/>`;
const wand='<path d="M82 90 L92 64" stroke="#8a5a2b" stroke-width="3" stroke-linecap="round"/><circle cx="92" cy="62" r="3.4" fill="#f2c94c"/>';
const ears='<ellipse cx="34" cy="24" rx="5" ry="12" fill="#f4f4f6"/><ellipse cx="66" cy="24" rx="5" ry="12" fill="#f4f4f6"/>';
const bat='<path d="M80 120 L92 84" stroke="#8a5a2b" stroke-width="5" stroke-linecap="round"/>';
const sword='<path d="M86 120 L86 70" stroke="#cfd6de" stroke-width="4" stroke-linecap="round"/><rect x="80" y="118" width="12" height="3" fill="#8a5a2b"/>';
const lant='<rect x="76" y="100" width="12" height="16" rx="2" fill="#f2c94c" stroke="#8a5a2b"/>';
const K={
  /* The Wizard of Oz / Alice / Peter Pan extras e continuações */
  glinda:{skirt:1,top:'#f4a6cf',hair:'#f2c94c',hairStyle:'long',hat:'tiara',extra:wand,shoe:'#c07ab0'},
  wizardoz:{top:'#3f9a5a',bot:'#2c6e43',hair:'#c9c9c9',hairStyle:'bald',beard:'#c9c9c9',hat:'tophat',hatc:'#2c6e43',shoe:'#2a2230'},
  tinman:{top:'#b8c0cc',bot:'#a5adb9',hair:'#b8c0cc',hairStyle:'bald',skin:'#cfd6de',hat:'funnel',shoe:'#8a929c',extra:'<path d="M82 112 L94 70" stroke="#8a929c" stroke-width="4" stroke-linecap="round"/>'},
  madhatter:{top:'#7c4dff',bot:'#3a2a62',hair:'#e8793a',hairStyle:'short',hat:'tophat',hatc:'#22a06b',shoe:'#2a2230',stache:'#e8793a'},
  queenhearts:{skirt:1,top:'#c0392b',hair:'#2a2230',hairStyle:'bob',hat:'crown',shoe:'#7a1f16'},
  whiterabbit:{top:'#4a6fa5',bot:'#3a4a7a',hair:'#f4f4f6',hairStyle:'none',skin:'#f4f4f6',extra:ears,front:'<circle cx="50" cy="96" r="6" fill="#f2c94c"/>',shoe:'#8a929c'},
  captainhook:{top:'#8b1e2d',bot:'#2a2230',hair:'#2a2230',hairStyle:'long',hat:'feather',stache:'#2a2230',shoe:'#2a2230',extra:'<path d="M80 108 Q92 100 88 92" stroke="#cfd6de" stroke-width="4" fill="none" stroke-linecap="round"/>'},
  /* Harry Potter */
  harry:{top:'#2a2230',bot:'#2a2230',hair:'#1a1420',hairStyle:'short',extra:wand+cape('#4a3a62'),over:gl+'<path d="M30 36 L40 30 L44 38Z" fill="#1a1420"/><path d="M46 26 L50 32 L54 26" stroke="#c0392b" stroke-width="2" fill="none"/>',shoe:'#2a2230',front:'<path d="M50 78 V126" stroke="#c0392b" stroke-width="3"/>'},
  hermione:{top:'#2a2230',bot:'#2a2230',hair:'#8a5a2b',hairStyle:'long',extra:wand,shoe:'#2a2230',front:'<path d="M42 78 L58 100" stroke="#c0392b" stroke-width="4"/>'},
  dumbledore:{top:'#5b3d9a',bot:'#4a2f82',hair:'#e6e6e6',hairStyle:'long',beard:'#e6e6e6',over:gl,shoe:'#2a2230'},
  /* clássicos */
  sherlock:{top:'#6b5a45',bot:'#4a4033',hair:'#3a2a22',hairStyle:'short',hat:'fedora',hatc:'#6b5a45',extra:'<circle cx="86" cy="104" r="7" fill="none" stroke="#2a2230" stroke-width="2"/><path d="M82 110 L74 120" stroke="#2a2230" stroke-width="2"/>',shoe:'#2a2230'},
  watson:{top:'#4a6fa5',bot:'#3a4a7a',hair:'#8a5a2b',hairStyle:'short',stache:'#8a5a2b',shoe:'#2a2230'},
  robin:{top:'#3f9a5a',bot:'#6b5a45',hair:'#8a5a2b',hairStyle:'short',hat:'green',extra:'<path d="M84 70 Q96 100 84 130" stroke="#8a5a2b" stroke-width="3" fill="none"/>',shoe:'#6b4f2a'},
  pinocchio:{top:'#e8434d',bot:'#f2c94c',hair:'#6b4f2a',hairStyle:'short',hat:'pointed',hatc:'#f4f4f6',skin:'#e8c08a',extra:'<path d="M54 54 L74 58 L54 60Z" fill="#e8c08a" stroke="#b5902f" stroke-width="1"/>',shoe:'#6b3a2a'},
  dorothyx:{skirt:1,top:'#2b6cb0',hair:'#6b4f2a',hairStyle:'long',front:'<path d="M36 110 H64 M33 120 H67" stroke="#fff" stroke-width="2" opacity=".5"/>',shoe:'#c0392b'},
  matilda:{skirt:1,top:'#3a63b5',hair:'#2a2230',hairStyle:'bob',extra:'<rect x="76" y="96" width="14" height="18" rx="2" fill="#c0392b"/>',shoe:'#6b3a2a'},
  willywonka:{top:'#7c4dff',bot:'#5a2fc2',hair:'#8a5a2b',hairStyle:'bob',hat:'tophat',hatc:'#e8434d',shoe:'#2a2230',extra:'<path d="M80 106 L92 66" stroke="#8a5a2b" stroke-width="3" stroke-linecap="round"/><circle cx="92" cy="64" r="4" fill="#e8434d"/>'},
  arthur:{top:'#3a63b5',bot:'#6b5a45',hair:'#c9a064',hairStyle:'short',hat:'crown',extra:sword,shoe:'#6b3a2a'},
  gandalf:{top:'#9aa3b5',bot:'#7a8396',hair:'#e6e6e6',hairStyle:'long',beard:'#e6e6e6',hat:'pointed',hatc:'#9aa3b5',extra:'<path d="M86 138 L88 62" stroke="#8a5a2b" stroke-width="4" stroke-linecap="round"/>',shoe:'#4a3a30'},
  frodo:{top:'#6b8a4a',bot:'#6b5a45',hair:'#6b4f2a',hairStyle:'short',extra:'<circle cx="88" cy="100" r="6" fill="none" stroke="#f2c94c" stroke-width="3"/>',shoe:'#b5651d'},
  simba:{top:'#e8a23a',bot:'#e8a23a',hair:'#b5651d',hairStyle:'long',skin:'#f0b85a',extra:'<circle cx="34" cy="26" r="6" fill="#e8a23a"/><circle cx="66" cy="26" r="6" fill="#e8a23a"/>',shoe:'#b5651d'},
  elsa:{skirt:1,top:'#7fc8f0',hair:'#f4f4f6',hairStyle:'long',skin:'#fbe4d0',front:'<path d="M50 80 V132" stroke="#fff" stroke-width="2" opacity=".6"/>',shoe:'#7fc8f0',extra:'<circle cx="86" cy="100" r="5" fill="#bfe8ff"/>'},
  mulan:{skirt:1,top:'#c0392b',hair:'#1a1420',hairStyle:'long',extra:sword,shoe:'#7a1f16'},
  pocahontas:{skirt:1,top:'#c98a2e',hair:'#1a1420',hairStyle:'long',skin:'#d9a37a',shoe:'#8a5a2b'},
  aladdin:{top:'#f4f4f6',bot:'#7c4dff',hair:'#1a1420',hairStyle:'short',skin:'#d9a37a',front:'<path d="M32 90 H68" stroke="#e8434d" stroke-width="5"/>',extra:lant,shoe:'#8a5a2b'},
  jasmine:{skirt:1,top:'#3fb5b0',hair:'#1a1420',hairStyle:'long',skin:'#d9a37a',shoe:'#3fb5b0'},
  sam:{top:'#f4f4f6',bot:'#3a4a7a',hair:'#8a5a2b',hairStyle:'short',hat:'cap',extra:bat,shoe:'#2a2230'}
};
HATS.funnel=o=>`<path d="M36 34 L50 6 L64 34Z" fill="#b8c0cc" stroke="#8a929c" stroke-width="1.2"/>`;
const C={};
Object.keys(K).forEach(k=>{C[k]=()=>{const o=Object.assign({},K[k]),ov=o.over||'';delete o.over;return person(o).replace('</svg>',ov+'</svg>')}});
window.POG_WORKCAST={ids:Object.keys(K)};
const SH='<ellipse cx="50" cy="146" rx="26" ry="3.6" fill="#000" opacity=".16"/>';
const old=window.PogChars;
window.PogChars={
  ids:old.ids.concat(Object.keys(C)),
  svg:id=>C[id]?C[id]():old.svg(id),
  face:id=>C[id]?C[id]().replace('viewBox="0 0 100 150"','viewBox="14 2 72 72"').replace(SH,''):old.face(id)
};
})();
