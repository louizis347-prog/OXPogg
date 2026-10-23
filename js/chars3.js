/* Pogglot · personagens ilustrados (parte 3): elenco das obras dos primeiros episódios do A1 de espanhol.
   Estende window.PogChars (mesmo desenho 100×150 de js/chars.js e js/chars2.js). */
(function(){
'use strict';
if(!window.PogChars)return;
const SK='#f4c7a1';
const eye=(x,y,r)=>`<circle cx="${x}" cy="${y}" r="${r||3.2}" fill="#2a2230"/><circle cx="${x+1}" cy="${y-1.1}" r="${(r||3.2)*.38}" fill="#fff"/>`;
const smile=(x,y,w)=>`<path d="M${x-w} ${y} Q${x} ${y+w*.9} ${x+w} ${y}" stroke="#7a3b2e" stroke-width="2" fill="none" stroke-linecap="round"/>`;
const cheek=(x,y)=>`<ellipse cx="${x}" cy="${y}" rx="4.2" ry="2.6" fill="#ff8aa0" opacity=".4"/>`;
const wrap=b=>`<svg class="ps-ch" viewBox="0 0 100 150" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true"><ellipse cx="50" cy="146" rx="26" ry="3.6" fill="#000" opacity=".16"/>${b}</svg>`;
const SHADOW_RE='<ellipse cx="50" cy="146" rx="26" ry="3.6" fill="#000" opacity=".16"/>';
function person(o){
  o=Object.assign({skin:SK,top:'#5b8def',bot:'#3a4a7a',shoe:'#4a3320',hair:'#3a2a22',hairStyle:'short',skirt:0,hat:'',beard:'',stache:'',front:'',extra:'',bare:0,arm:null},o);
  const sk=o.skin;
  const legs=o.skirt?`<rect x="39" y="128" width="8" height="14" rx="3" fill="${sk}"/><rect x="53" y="128" width="8" height="14" rx="3" fill="${sk}"/>`:
    `<rect x="38" y="122" width="10" height="21" rx="4" fill="${o.bot}"/><rect x="52" y="122" width="10" height="21" rx="4" fill="${o.bot}"/>`;
  const shoes=`<ellipse cx="42" cy="143" rx="9" ry="4.4" fill="${o.shoe}"/><ellipse cx="58" cy="143" rx="9" ry="4.4" fill="${o.shoe}"/>`;
  const body=o.skirt?`<path d="M50 74 L24 134 Q50 142 76 134 Z" fill="${o.top}"/>`:`<path d="M27 126 Q23 88 38 78 L62 78 Q77 88 73 126 Z" fill="${o.top}"/>`;
  const arms=`<path d="M30 84 Q20 98 24 106" stroke="${o.arm||o.top}" stroke-width="9" stroke-linecap="round" fill="none"/><path d="M70 84 Q80 98 76 106" stroke="${o.arm||o.top}" stroke-width="9" stroke-linecap="round" fill="none"/><circle cx="24" cy="106" r="5.5" fill="${sk}"/><circle cx="76" cy="106" r="5.5" fill="${sk}"/>`;
  const H={short:`<path d="M26 48 Q26 22 50 22 Q74 22 74 48 Q64 34 50 36 Q36 34 26 48Z" fill="${o.hair}"/>`,
    long:`<path d="M24 52 Q20 86 32 96 Q30 64 34 44Z M76 52 Q80 86 68 96 Q70 64 66 44Z" fill="${o.hair}"/><path d="M26 48 Q26 22 50 22 Q74 22 74 48 Q64 34 50 36 Q36 34 26 48Z" fill="${o.hair}"/>`,
    bob:`<path d="M23 58 Q20 20 50 19 Q80 20 77 58 Q72 66 66 56 L34 56 Q28 66 23 58Z" fill="${o.hair}"/>`,
    bald:`<path d="M30 40 Q30 28 50 27 Q70 28 70 40 Q60 32 50 33 Q40 32 30 40Z" fill="${o.hair}"/>`,
    none:''};
  const hat={cap:`<path d="M27 38 Q28 16 50 16 Q72 16 73 38 Q50 30 27 38Z" fill="${o.hatc||'#c0392b'}"/><path d="M62 33 Q86 30 90 38 Q76 40 62 38Z" fill="${o.hatc||'#c0392b'}"/>`,
    helmet:`<ellipse cx="50" cy="34" rx="30" ry="6" fill="#b8bec7"/><path d="M26 34 Q28 12 50 12 Q72 12 74 34Z" fill="#cfd6de"/><rect x="48" y="12" width="4" height="10" fill="#e8434d"/>`,
    beret:`<ellipse cx="50" cy="24" rx="26" ry="9" fill="#2b2531"/>`,
    chavo:`<path d="M28 36 Q30 12 50 12 Q70 12 72 36Z" fill="#e8c25a"/><path d="M26 36 Q50 30 74 36" stroke="#b5902f" stroke-width="3" fill="none"/>`}[o.hat]||'';
  const beard=o.beard?`<path d="M36 60 Q40 78 50 80 Q60 78 64 60 Q56 70 50 68 Q44 70 36 60Z" fill="${o.beard}"/>`:'';
  const stache=o.stache?`<path d="M38 60 Q50 54 62 60 Q56 66 50 62 Q44 66 38 60Z" fill="${o.stache}"/>`:'';
  return wrap(`${legs}${shoes}${body}${o.front}${arms}${o.extra}<circle cx="50" cy="48" r="24" fill="${sk}"/>${H[o.hairStyle]||H.short}${hat}${eye(41,48)}${eye(59,48)}${cheek(34,56)}${cheek(66,56)}${smile(50,58,6)}${stache}${beard}`);
}
const mask='<ellipse cx="50" cy="88" rx="8" ry="10" fill="#f7efe3" stroke="#2a2230" stroke-width="1.4"/><path d="M45 86 Q47 84 49 86 M51 86 Q53 84 55 86" stroke="#2a2230" stroke-width="1.4" fill="none"/><path d="M45 94 Q50 97 55 94" stroke="#2a2230" stroke-width="1.4" fill="none"/><path d="M44 80 Q50 74 56 80" stroke="#2a2230" stroke-width="1.6" fill="none"/>';
const lance='<path d="M88 30 V142" stroke="#8a5a2b" stroke-width="3.4" stroke-linecap="round"/><path d="M88 30 L84 42 L92 42Z" fill="#cfd6de"/>';
const bag='<path d="M30 100 H48 L46 122 H32Z" fill="#c98a2e"/><path d="M33 100 Q39 90 45 100" stroke="#8a5a2b" stroke-width="2" fill="none"/>';
const sombrero='<ellipse cx="50" cy="34" rx="34" ry="6" fill="#d9a441"/><path d="M34 34 Q36 14 50 14 Q64 14 66 34Z" fill="#e8bd5a"/>';
const C={
  tokio:()=>person({top:'#c0392b',bot:'#c0392b',hair:'#2a2230',hairStyle:'bob',skin:'#f0c29b',shoe:'#2a2230',front:'<path d="M50 80 V126" stroke="#7a1f16" stroke-width="2"/>'}),
  rio:()=>person({top:'#c0392b',bot:'#c0392b',hair:'#3a2a22',hairStyle:'short',skin:'#ecb790',shoe:'#2a2230',front:'<path d="M50 80 V126" stroke="#7a1f16" stroke-width="2"/>',extra:mask}),
  quijote:()=>person({top:'#aab2bd',bot:'#8a929c',hair:'#c9c9c9',hairStyle:'bald',skin:'#e0aa84',hat:'helmet',beard:'#bfbfbf',stache:'#bfbfbf',shoe:'#6b5a45',extra:lance}),
  sancho:()=>person({top:'#7a9a5a',bot:'#6b5a45',hair:'#3a2a22',hairStyle:'short',skin:'#e8b894',hat:'beret',extra:bag}),
  chavo:()=>person({top:'#e8c25a',bot:'#3a63b5',hair:'#4b3320',hairStyle:'short',hat:'chavo',skin:'#f0c29b',front:'<path d="M40 80 V122 M60 80 V122" stroke="#3a63b5" stroke-width="5"/>',shoe:'#6b3a2a'}),
  florinda:()=>person({skirt:1,top:'#d86aa0',hair:'#2a2230',hairStyle:'bob',skin:'#f0c29b',shoe:'#7a3b2e',front:'<path d="M36 112 H64 M32 122 H68" stroke="#fff" stroke-width="2" opacity=".35"/>'})
};
const old=window.PogChars;
window.PogChars={
  ids:old.ids.concat(Object.keys(C)),
  svg:id=>C[id]?C[id]():old.svg(id),
  face:id=>C[id]?C[id]().replace('viewBox="0 0 100 150"','viewBox="14 2 72 72"').replace(SHADOW_RE,''):old.face(id)
};
})();
