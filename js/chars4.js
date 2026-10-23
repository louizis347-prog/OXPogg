/* Pogglot · personagens paramétricos (parte 4): qualquer personagem novo sem desenhar um SVG à mão.
   "p:<cabelo>:<corCabelo>:<pele>:<corRoupa>:<acessório>:<traje>"  ex.: p:long:6b3f26:f4c7a1:c0392b:crown:dress
   cabelo: short|long|bun|curly|bald|cap · acessório: none|glasses|hat|crown|scarf|beard|bow · traje: shirt|dress|suit
   "e:<emoji>" = bicho/objeto como personagem (um emoji grande). Estende window.PogChars. */
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
function param(id){
  const [,hs='short',hc='3b2a20',sk='f4c7a1',top='2f5fa8',acc='none',out='shirt']=id.split(':');
  const H='#'+hc,S='#'+sk,T='#'+top;
  let body;
  if(out==='dress')body=`<path d="M50 74 L24 132 Q50 142 76 132 Z" fill="${T}"/><rect x="40" y="74" width="20" height="10" rx="4" fill="${T}"/>`;
  else if(out==='suit')body=`<path d="M28 130 Q24 86 38 76 L62 76 Q76 86 72 130 Z" fill="${T}"/><path d="M50 78 L44 100 L50 130 L56 100Z" fill="#fff"/><path d="M50 80 L47 92 L50 120 L53 92Z" fill="#c0392b"/>`;
  else body=`<path d="M28 130 Q24 86 38 76 L62 76 Q76 86 72 130 Z" fill="${T}"/><path d="M50 76 V130" stroke="#00000022" stroke-width="2"/>`;
  const legs=out==='dress'?'':`<rect x="37" y="126" width="10" height="18" rx="4" fill="#33415c"/><rect x="53" y="126" width="10" height="18" rx="4" fill="#33415c"/>`;
  const shoes=`<ellipse cx="42" cy="144" rx="8" ry="3.4" fill="#2a2230"/><ellipse cx="58" cy="144" rx="8" ry="3.4" fill="#2a2230"/>`;
  let back='',front='';
  if(hs==='long')back=`<path d="M24 56 Q18 24 50 22 Q82 24 76 56 Q80 84 68 90 Q70 60 62 40 L38 40 Q30 60 32 90 Q20 84 24 56Z" fill="${H}"/>`;
  if(hs==='bun')back=`<circle cx="50" cy="20" r="10" fill="${H}"/>`;
  if(hs==='curly')back=`<circle cx="30" cy="40" r="11" fill="${H}"/><circle cx="70" cy="40" r="11" fill="${H}"/><circle cx="36" cy="28" r="12" fill="${H}"/><circle cx="64" cy="28" r="12" fill="${H}"/><circle cx="50" cy="24" r="13" fill="${H}"/>`;
  if(hs!=='bald')front=`<path d="M26 46 Q26 22 50 22 Q74 22 74 46 Q66 34 50 34 Q34 34 26 46Z" fill="${H}"/>`;
  if(hs==='cap')front=`<path d="M25 44 Q26 20 50 20 Q74 20 75 44 Z" fill="${T}"/><path d="M60 42 H84 Q84 46 78 47 H60Z" fill="${T}"/>`;
  let ac='';
  if(acc==='glasses')ac=`<circle cx="41" cy="50" r="7" fill="none" stroke="#2a2230" stroke-width="2"/><circle cx="59" cy="50" r="7" fill="none" stroke="#2a2230" stroke-width="2"/><path d="M48 50 H52" stroke="#2a2230" stroke-width="2"/>`;
  if(acc==='hat')ac=`<ellipse cx="50" cy="32" rx="32" ry="6" fill="#7a4a24"/><path d="M32 32 Q34 12 50 12 Q66 12 68 32Z" fill="#9a5f30"/>`;
  if(acc==='crown')ac=`<path d="M32 30 L36 12 L44 24 L50 10 L56 24 L64 12 L68 30Z" fill="#f2c94c" stroke="#b8891a" stroke-width="1.6"/>`;
  if(acc==='scarf')ac=`<path d="M34 72 Q50 84 66 72 L68 82 Q50 94 32 82Z" fill="#c0392b"/>`;
  if(acc==='beard')ac=`<path d="M30 56 Q50 92 70 56 Q62 72 50 72 Q38 72 30 56Z" fill="${H}"/>`;
  if(acc==='bow')ac=`<path d="M50 24 L38 16 L38 32Z M50 24 L62 16 L62 32Z" fill="#e6568c"/><circle cx="50" cy="24" r="4" fill="#c2306b"/>`;
  return wrap(`${legs}${shoes}${body}${hand(26,106,S)}${hand(74,106,S)}${back}<circle cx="50" cy="48" r="24" fill="${S}"/>${front}${eye(41,50)}${eye(59,50)}${cheek(35,58)}${cheek(65,58)}${acc==='beard'?'':smile(50,61,6)}${ac}`);
}
function emo(id){
  const g=Array.from(id.slice(2))[0]||'🐾';
  return wrap(`<ellipse cx="50" cy="118" rx="30" ry="22" fill="#00000012"/><text x="50" y="100" font-size="82" text-anchor="middle" font-family="Apple Color Emoji,Segoe UI Emoji,Noto Color Emoji,sans-serif">${g}</text>`);
}
const old=window.PogChars;
const mine=id=>id.startsWith('p:')?param(id):id.startsWith('e:')?emo(id):'';
window.PogChars={
  ids:old.ids,
  svg:id=>mine(id)||old.svg(id),
  face:id=>{const s=mine(id);return s?s.replace('viewBox="0 0 100 150"',id.startsWith('e:')?'viewBox="8 28 84 84"':'viewBox="14 2 72 72"').replace(shadow,''):old.face(id)}
};
})();
