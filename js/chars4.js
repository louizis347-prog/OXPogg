/* Pogglot · personagens ilustrados (parte 4): elenco dos primeiros episódios do A1 de português (para hispanofalantes), italiano e alemão.
   Usa o mesmo desenho de js/chars3.js (PogPerson) e estende window.PogChars. */
(function(){
'use strict';
if(!window.PogChars||!window.PogPerson)return;
const {person,HATS}=window.PogPerson;
HATS.tophat=o=>`<ellipse cx="50" cy="33" rx="26" ry="5" fill="#1c1722"/><rect x="35" y="8" width="30" height="26" rx="3" fill="#2b2531"/><rect x="35" y="24" width="30" height="5" fill="${o.hatc||'#8b1e2d'}"/>`;
HATS.fedora=o=>`<ellipse cx="50" cy="34" rx="30" ry="6" fill="${o.hatc||'#4a3a30'}"/><path d="M32 34 Q34 14 50 15 Q66 14 68 34Z" fill="${o.hatc||'#4a3a30'}"/><path d="M33 31 Q50 36 67 31" stroke="#c9a064" stroke-width="3" fill="none"/>`;
HATS.crown=o=>`<path d="M34 28 L38 14 L44 24 L50 12 L56 24 L62 14 L66 28Z" fill="#f2c94c" stroke="#b5902f" stroke-width="1.2"/>`;
HATS.alpine=o=>`<ellipse cx="50" cy="32" rx="26" ry="5" fill="${o.hatc||'#5a6b3a'}"/><path d="M33 32 Q36 12 52 14 Q64 14 67 32Z" fill="${o.hatc||'#5a6b3a'}"/><path d="M60 22 L74 6" stroke="#e8434d" stroke-width="3" stroke-linecap="round"/>`;
HATS.pointed=o=>`<path d="M30 34 L50 -2 L70 34Q50 28 30 34Z" fill="${o.hatc||'#f4f4f6'}" stroke="#d6d6d6" stroke-width="1.2"/>`;
HATS.feather=o=>`<path d="M32 30 Q50 22 68 30" stroke="#d9a441" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M62 28 Q70 6 78 12 Q74 22 66 30Z" fill="#e8434d"/><path d="M58 28 Q62 8 70 6 Q68 18 62 30Z" fill="#2f9e6a"/>`;
const glasses='<g fill="none" stroke="#3a3340" stroke-width="1.6"><circle cx="41" cy="48" r="6"/><circle cx="59" cy="48" r="6"/><path d="M47 48 H53"/></g>';
const briefcase='<rect x="66" y="110" width="26" height="20" rx="3" fill="#6b4f2a"/><rect x="74" y="106" width="10" height="5" rx="2" fill="none" stroke="#6b4f2a" stroke-width="2"/>';
const horn='<path d="M70 104 L92 96 L92 114Z" fill="#f2c94c" stroke="#b5902f" stroke-width="1.2"/><ellipse cx="70" cy="106" rx="4" ry="6" fill="#b5902f"/>';
const nose='<path d="M54 50 L84 58 L54 58Z" fill="#c98a4a"/>';
const cart='<path d="M62 100 H92 L88 124 H66Z" fill="none" stroke="#6b7280" stroke-width="2.4"/><circle cx="70" cy="130" r="3.6" fill="#6b7280"/><circle cx="84" cy="130" r="3.6" fill="#6b7280"/><path d="M62 100 L58 92" stroke="#6b7280" stroke-width="2.4"/>';
const strands='<path d="M42 24 L40 8 M46 22 L45 4 M50 21 L50 2 M54 22 L55 4 M58 24 L60 8" stroke="#2a2230" stroke-width="2.4" stroke-linecap="round"/>';
const apron='<path d="M38 92 H62 L66 126 H34Z" fill="#fff" opacity=".85"/>';
const sash='<path d="M32 84 L68 120" stroke="#c0392b" stroke-width="7"/>';
const scarf='<path d="M38 78 Q50 90 62 78 L64 84 Q50 96 36 84Z" fill="#c0392b"/>';
const bag='<path d="M30 100 H48 L46 122 H32Z" fill="#6b4f2a"/><path d="M33 100 Q39 90 45 100" stroke="#4a3a28" stroke-width="2" fill="none"/>';
const suspend='<path d="M40 80 V124 M60 80 V124" stroke="#8a5a2b" stroke-width="5"/>';
const P=(o)=>()=>person(o);
const C={
  // português (Brasil)
  monica:P({skirt:1,top:'#d9342b',hair:'#2a2230',hairStyle:'bob',shoe:'#d9342b',skin:'#f4c7a1'}),
  cebolinha:P({top:'#3f9a5a',bot:'#3f9a5a',hair:'#2a2230',hairStyle:'bald',front:strands,shoe:'#f4f4f6'}),
  benta:P({skirt:1,top:'#8a5a9a',hair:'#d4d4d4',hairStyle:'bob',extra:glasses,skin:'#f0c29b',shoe:'#4a3320'}),
  pedrinho:P({top:'#c0392b',bot:'#3a4a7a',hair:'#4b3320',hairStyle:'short',hat:'cap',hatc:'#f2c94c'}),
  bentinho:P({top:'#2b2531',bot:'#2b2531',hair:'#3a2a22',hairStyle:'short',hat:'tophat',hatc:'#5a5a62',skin:'#ecb790',shoe:'#1c1722',front:scarf}),
  capitu:P({skirt:1,top:'#6a8fc0',hair:'#1c1722',hairStyle:'long',skin:'#e8b894',shoe:'#4a3320'}),
  macunaima:P({top:'#d9a441',bot:'#6b4f2a',hair:'#1c1722',hairStyle:'short',hat:'feather',skin:'#b9764a',bare:1}),
  mae:P({skirt:1,top:'#7a9a5a',hair:'#2a2230',hairStyle:'bob',skin:'#b9764a',front:apron,shoe:'#4a3320'}),
  // italiano
  pinocchio:P({top:'#d6453d',bot:'#f2c94c',hair:'#8a5a2b',hairStyle:'short',hat:'pointed',extra:nose,shoe:'#6b3a2a',skin:'#e8c08a'}),
  geppetto:P({top:'#8a6a3b',bot:'#5a4a35',hair:'#e8e8e8',hairStyle:'bald',stache:'#e8e8e8',extra:glasses,front:apron,skin:'#e8b894',shoe:'#4a3320'}),
  postino:P({top:'#4a6a8a',bot:'#4a6a8a',hair:'#3a2a22',hairStyle:'short',hat:'cap',hatc:'#2b4a7a',extra:bag,skin:'#e8b894'}),
  neruda:P({top:'#4a4a55',bot:'#33333b',hair:'#cfcfcf',hairStyle:'bald',hat:'fedora',hatc:'#33333b',front:scarf,skin:'#e8b894',shoe:'#1c1722'}),
  tancredi:P({top:'#c0392b',bot:'#2b2531',hair:'#3a2a22',hairStyle:'short',stache:'#3a2a22',skin:'#ecb790',shoe:'#1c1722'}),
  principe:P({top:'#26386a',bot:'#1d2b4a',hair:'#5b4a3a',hairStyle:'bald',beard:'#5b4a3a',hat:'tophat',hatc:'#26386a',skin:'#e0aa84',shoe:'#1c1722'}),
  anna:P({skirt:1,top:'#f4f4f6',hair:'#a8602a',hairStyle:'bob',hat:'crown',skin:'#f4c7a1',shoe:'#c9a064'}),
  joe:P({top:'#8a7a6a',bot:'#4a4a55',hair:'#5b3b1c',hairStyle:'short',hat:'fedora',hatc:'#6b5a45',front:'<path d="M50 80 V126" stroke="#5a4a3a" stroke-width="2"/>',skin:'#ecb790'}),
  marcovaldo:P({top:'#4a6aa0',bot:'#3a5a90',hair:'#3a2a22',hairStyle:'short',hat:'cap',hatc:'#4a5a7a',extra:cart,skin:'#e8b894'}),
  domitilla:P({skirt:1,top:'#d9a441',hair:'#5b3b1c',hairStyle:'bob',front:apron,skin:'#f0c29b',shoe:'#6b3a2a'}),
  // alemão
  gregor:P({top:'#6b6b73',bot:'#4a4a52',hair:'#3a2a22',hairStyle:'short',extra:briefcase,front:'<path d="M46 80 L50 96 L54 80Z" fill="#c0392b"/>',skin:'#ecb790',shoe:'#1c1722'}),
  prokurist:P({top:'#2b2531',bot:'#2b2531',hair:'#2a2230',hairStyle:'bald',stache:'#2a2230',hat:'tophat',hatc:'#2b2531',skin:'#e0aa84',shoe:'#1c1722'}),
  sissi:P({skirt:1,top:'#5b8def',hair:'#6b3f26',hairStyle:'long',hat:'crown',skin:'#f4c7a1',shoe:'#c9a064'}),
  franz:P({top:'#f4f4f6',bot:'#c0392b',hair:'#a8602a',hairStyle:'short',front:sash,stache:'#a8602a',skin:'#f0c29b',shoe:'#1c1722'}),
  heidi:P({skirt:1,top:'#d86aa0',hair:'#6b3f26',hairStyle:'long',front:apron,skin:'#f4c7a1',shoe:'#6b3a2a'}),
  grossvater:P({top:'#5a4a35',bot:'#6b5a45',hair:'#e8e8e8',hairStyle:'bald',beard:'#e8e8e8',stache:'#e8e8e8',hat:'alpine',skin:'#e0aa84',shoe:'#4a3320'}),
  emil:P({top:'#4a6aa0',bot:'#3a4a7a',hair:'#3a2a22',hairStyle:'short',hat:'cap',hatc:'#3a4a7a',skin:'#f0c29b',shoe:'#4a3320'}),
  gustav:P({top:'#d9a441',bot:'#5a4a35',hair:'#5b3b1c',hairStyle:'short',hat:'cap',hatc:'#c0392b',extra:horn,skin:'#ecb790'}),
  hansel:P({top:'#f4f4f6',bot:'#8a5a2b',hair:'#d9a441',hairStyle:'short',front:suspend,skin:'#f4c7a1',shoe:'#4a3320'}),
  gretel:P({skirt:1,top:'#e8c25a',hair:'#d9a441',hairStyle:'long',front:apron,skin:'#f4c7a1',shoe:'#6b3a2a'})
};
const old=window.PogChars;
const SH='<ellipse cx="50" cy="146" rx="26" ry="3.6" fill="#000" opacity=".16"/>';
window.PogChars={
  ids:old.ids.concat(Object.keys(C)),
  svg:id=>C[id]?C[id]():old.svg(id),
  face:id=>C[id]?C[id]().replace('viewBox="0 0 100 150"','viewBox="14 2 72 72"').replace(SH,''):old.face(id)
};
})();
