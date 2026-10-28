/* Arte da home e da landing: paisagem ilustrada (SVG), Poggie e a abertura animada.
   Sem dependências: funciona na landing (index.html) e no app (app.html). */
(function(){
'use strict';
let UID=0;
const INK='#0E2F3A';

/* Poggie (ornitorrinco): mesma figura do app, com ids únicos e classes de animação próprias */
function mascot(o){
  o=o||{};const scarf=o.scarf||'#FF7A45',id='hm'+(++UID);
  return `<svg class="ha-m ${o.cls||''}" viewBox="0 0 200 200" role="img" aria-label="Poggie, o ornitorrinco">
  <defs>
    <radialGradient id="${id}f" cx="45%" cy="35%" r="70%"><stop offset="0" stop-color="#B0794F"/><stop offset="1" stop-color="#6E4429"/></radialGradient>
    <linearGradient id="${id}b" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFC06A"/><stop offset="1" stop-color="#E08421"/></linearGradient>
    <linearGradient id="${id}t" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#5B3721"/><stop offset="1" stop-color="#7C4F32"/></linearGradient>
  </defs>
  <ellipse cx="100" cy="186" rx="58" ry="8" fill="rgba(0,0,0,.16)"/>
  <g class="ha-whole">
    <g class="ha-tail"><path d="M58 150 C20 150 8 132 12 118 C18 104 44 110 64 128 Z" fill="url(#${id}t)"/>
      <path d="M22 122 l30 16 M20 132 l32 10 M30 116 l24 18" stroke="#4A2C19" stroke-width="2" opacity=".5"/></g>
    <path d="M64 180 q-4 6 -14 6 q6 -2 4 -8 z M136 180 q4 6 14 6 q-6 -2 -4 -8 z" fill="#F08F2A"/>
    <ellipse cx="100" cy="126" rx="50" ry="56" fill="url(#${id}f)"/>
    <ellipse cx="100" cy="140" rx="31" ry="36" fill="#D2A47C"/>
    <path d="M78 176 q-6 8 -18 8 q8 -8 6 -12 z M122 176 q6 8 18 8 q-8 -8 -6 -12 z" fill="#F29B34"/>
    <path d="M60 110 q40 26 80 0 l2 12 q-42 26 -84 0 z" fill="${scarf}"/>
    <path class="ha-scarf" d="M122 118 q10 18 2 34 l-12 -4 q6 -14 -2 -26 z" fill="${scarf}"/>
    <path d="M70 110 q6 22 44 32" stroke="#3D2517" stroke-width="3" fill="none" opacity=".5"/>
    <g class="ha-arm"><path d="M138 126 q20 -10 22 -30 q2 -8 -6 -6 q-6 12 -22 22 z" fill="#7C4F32"/>
      <rect x="148" y="72" width="22" height="28" rx="2" fill="#FFB627" transform="rotate(12 159 86)"/><rect x="150" y="74" width="4" height="24" fill="#D9901A" transform="rotate(12 159 86)"/></g>
    <path d="M62 132 q-14 10 -10 24 q8 2 14 -10 z" fill="#7C4F32"/>
    <circle cx="80" cy="84" r="13" fill="#fff"/><circle cx="120" cy="84" r="13" fill="#fff"/>
    <g class="ha-blink"><circle cx="82" cy="86" r="7" fill="#15233B"/><circle cx="118" cy="86" r="7" fill="#15233B"/>
      <circle cx="85" cy="83" r="2.4" fill="#fff"/><circle cx="121" cy="83" r="2.4" fill="#fff"/></g>
    <ellipse cx="66" cy="98" rx="7" ry="4" fill="#F08A8A" opacity=".6"/><ellipse cx="134" cy="98" rx="7" ry="4" fill="#F08A8A" opacity=".6"/>
    <path d="M70 96 C70 92 130 92 130 96 C150 98 160 108 150 116 C140 122 60 122 50 116 C40 108 50 98 70 96 Z" fill="url(#${id}b)"/>
    <ellipse cx="90" cy="102" rx="3" ry="2" fill="#9A5A12"/><ellipse cx="110" cy="102" rx="3" ry="2" fill="#9A5A12"/>
    <path d="M56 116 C80 124 120 124 144 116 C140 126 60 126 56 116 Z" fill="#C9741A"/>
    <path d="M72 58 q28 -18 56 0 q-10 -6 -28 -6 q-18 0 -28 6z" fill="#5F3C25" opacity=".6"/>
  </g></svg>`;
}

/* ícones redondos das obras (cinema, livro, música, teatro) */
const ICO={
 film:`<rect x="-14" y="-6" width="28" height="20" rx="3" fill="#fff" stroke="${INK}" stroke-width="2.4"/><path d="M-14,-6 L14,-6 L12,-14 L-16,-14Z" fill="${INK}"/><path d="M-6,-14 L-2,-6 M4,-14 L8,-6" stroke="#fff" stroke-width="2.4"/>`,
 book:`<path d="M-15,-12 Q-4,-16 0,-9 Q4,-16 15,-12 L15,12 Q4,8 0,15 Q-4,8 -15,12Z" fill="#fff" stroke="${INK}" stroke-width="2.4" stroke-linejoin="round"/><path d="M0,-9 L0,15" stroke="${INK}" stroke-width="2.2"/>`,
 music:`<path d="M-6,10 L-6,-12 L12,-16 L12,6" fill="none" stroke="${INK}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/><ellipse cx="-10" cy="11" rx="6" ry="4.4" fill="${INK}"/><ellipse cx="8" cy="7" rx="6" ry="4.4" fill="${INK}"/>`,
 mask:`<path d="M-14,-12 Q0,-18 14,-12 Q16,6 0,15 Q-16,6 -14,-12Z" fill="#fff" stroke="${INK}" stroke-width="2.4" stroke-linejoin="round"/><path d="M-9,-3 Q-6,-6 -3,-3 M3,-3 Q6,-6 9,-3" stroke="${INK}" stroke-width="2.4" fill="none" stroke-linecap="round"/><path d="M-6,6 Q0,11 6,6" stroke="${INK}" stroke-width="2.4" fill="none" stroke-linecap="round"/>`
};
const badge=(k,x,y,c,cls)=>`<g class="ha-float ${cls}" transform="translate(${x} ${y})"><g class="ha-fl-in"><circle r="30" fill="${c}"/><circle r="30" fill="none" stroke="#fff" stroke-width="3" opacity=".8"/><g>${ICO[k]}</g></g></g>`;

/* paisagem da home: céu de amanhecer, sol, nuvens, colinas com monumentos e um caminho */
function scene(o){
  o=o||{};const id='hs'+(++UID);
  return `<svg class="ha-scene" viewBox="0 0 1200 520" preserveAspectRatio="xMidYMax slice" aria-hidden="true" focusable="false">
  <defs>
    <linearGradient id="${id}sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9ADBE0"/><stop offset=".55" stop-color="#FFF0CF"/><stop offset="1" stop-color="#FFD9A6"/></linearGradient>
    <radialGradient id="${id}sun" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FFF3B0" stop-opacity=".95"/><stop offset="1" stop-color="#FFE08A" stop-opacity="0"/></radialGradient>
    <linearGradient id="${id}h1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9ED8C6"/><stop offset="1" stop-color="#7CCBB4"/></linearGradient>
    <linearGradient id="${id}h2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4FBE9F"/><stop offset="1" stop-color="#34A98A"/></linearGradient>
    <linearGradient id="${id}h3" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1E9A7E"/><stop offset="1" stop-color="#107A68"/></linearGradient>
  </defs>
  <rect width="1200" height="520" fill="url(#${id}sky)"/>
  <circle cx="850" cy="205" r="170" fill="url(#${id}sun)"/>
  <g transform="translate(850 205)"><g class="ha-rays">${[...Array(12)].map((_,i)=>`<path d="M-7,-96 L0,-150 L7,-96Z" fill="#FFD25E" opacity=".5" transform="rotate(${i*30})"/>`).join('')}</g></g>
  <circle cx="850" cy="205" r="62" fill="#FFC94A"/><circle cx="850" cy="205" r="62" fill="none" stroke="#FFE7A0" stroke-width="6"/>
  <g class="ha-cloud c1"><path d="M0,40 Q-8,14 20,12 Q30,-12 58,2 Q84,-8 96,16 Q122,16 118,40Z" fill="#fff" opacity=".95"/></g>
  <g class="ha-cloud c2"><path d="M0,34 Q-6,12 18,10 Q28,-8 52,4 Q76,-4 86,16 Q106,16 102,34Z" fill="#fff" opacity=".85"/></g>
  <g class="ha-cloud c3"><path d="M0,30 Q-6,10 14,8 Q24,-6 44,4 Q64,-2 72,14 Q90,14 86,30Z" fill="#fff" opacity=".8"/></g>
  <g class="ha-bird b1"><path d="M0,0 Q8,-8 16,0 Q24,-8 32,0" fill="none" stroke="${INK}" stroke-width="2.4" stroke-linecap="round" opacity=".55"/></g>
  <g class="ha-bird b2"><path d="M0,0 Q6,-6 12,0 Q18,-6 24,0" fill="none" stroke="${INK}" stroke-width="2.2" stroke-linecap="round" opacity=".45"/></g>
  <path d="M0,330 Q150,282 300,318 Q470,268 640,312 Q820,270 980,306 Q1100,284 1200,312 L1200,520 L0,520Z" fill="url(#${id}h1)"/>
  <g fill="#6FB8A6" stroke="#5FA895" stroke-width="2" stroke-linejoin="round" opacity=".95">
    <path d="M190,306 L206,306 L210,250 L214,306 L230,306 L214,318 L206,318Z M200,262 L220,262" opacity=".0"/>
    <path d="M236,312 L246,312 L250,236 L254,312 L264,312 L254,322 L246,322Z M242,268 L258,268 M244,292 L256,292" />
    <rect x="330" y="262" width="22" height="52"/><path d="M326,262 L341,238 L356,262Z"/><circle cx="341" cy="276" r="6" fill="#CFEFE6"/>
    <path d="M520,314 L520,284 Q520,262 548,262 Q576,262 576,284 L576,314Z M590,314 L590,290 Q590,270 612,270 Q634,270 634,290 L634,314Z"/>
    <path d="M730,314 L730,276 M790,314 L790,276 M718,276 L802,276 M722,266 L798,266" stroke="#E7826A" stroke-width="7" stroke-linecap="round" fill="none"/>
    <path d="M1010,314 L1010,270 L1030,262 L1050,270 L1050,314Z"/><path d="M1030,262 L1030,236 M1030,250 L1008,240 M1030,250 L1052,240 M1030,250 L1014,266 M1030,250 L1048,266" stroke="#5FA895" stroke-width="5" stroke-linecap="round" fill="none"/>
  </g>
  <path d="M0,372 Q180,326 360,362 Q560,318 760,362 Q960,322 1200,366 L1200,520 L0,520Z" fill="url(#${id}h2)"/>
  ${[[110,352],[420,350],[870,350],[1120,356]].map(([x,y],k)=>`<g transform="translate(${x} ${y})"><rect x="-4" y="0" width="8" height="26" fill="#7A5A3A"/><circle cy="-6" r="${24-k*2}" fill="#2FA384"/><circle cx="14" cy="4" r="14" fill="#38B493"/></g>`).join('')}
  <path d="M0,430 Q260,372 520,420 Q800,372 1200,412 L1200,520 L0,520Z" fill="url(#${id}h3)"/>
  <path d="M470,520 Q430,452 560,420 Q690,392 640,350 Q620,334 650,322" fill="none" stroke="#FFF0C7" stroke-width="46" stroke-linecap="round" opacity=".95"/>
  <path d="M470,520 Q430,452 560,420 Q690,392 640,350 Q620,334 650,322" fill="none" stroke="#F6D88E" stroke-width="4" stroke-dasharray="2 16" stroke-linecap="round"/>
  ${[[70,470,'#FF7A45'],[150,490,'#FFB627'],[300,484,'#FF7A45'],[880,470,'#FFB627'],[1010,488,'#FF7A45'],[1120,466,'#FFB627']].map(([x,y,c],k)=>`<g transform="translate(${x} ${y})" class="ha-flower"><path d="M0,0 L0,24" stroke="#0E6B58" stroke-width="3"/><circle cy="-2" r="7" fill="${c}"/><circle cy="-2" r="3" fill="#fff6d8"/></g>`).join('')}
  ${badge('film',670,205,'#FF9B73','f1')}${badge('book',750,285,'#FFD866','f2')}${badge('music',1030,200,'#8FD9C9','f3')}${badge('mask',1100,285,'#FFB3A0','f4')}
  </svg>`;
}

/* abertura animada: Poggie entra, o nome aparece e a tela sobe. Uma vez por sessão; qualquer toque pula. */
function splash(done){
  try{
    if(matchMedia('(prefers-reduced-motion:reduce)').matches||sessionStorage.getItem('pogglot:intro')){done&&done();return}
    sessionStorage.setItem('pogglot:intro','1');
  }catch(e){done&&done();return}
  const d=document.createElement('div');d.id='hnSplash';d.setAttribute('role','presentation');
  d.innerHTML=`<div class="sp-bg">${scene()}</div><div class="sp-in"><div class="sp-pog">${mascot()}</div><div class="sp-word" aria-label="Pogglot"><span>P</span><span>o</span><span>g</span><span>g</span><span class="l">l</span><span class="l">o</span><span class="l">t</span></div><p>Aprenda idiomas pela cultura</p></div>`;
  document.body.appendChild(d);
  let fin=false;const end=()=>{if(fin)return;fin=true;d.classList.add('out');setTimeout(()=>{d.remove();done&&done()},520)};
  d.addEventListener('click',end);setTimeout(end,2300);
}
window.HomeArt={mascot,scene,splash,badge,ICO};
})();
