/* Pogglot · retratos ilustrados: rosto com olhos, sobrancelhas, nariz, boca, orelhas, cabelo e roupa.
   PogFace.bust(opts) devolve um <g> SVG numa caixa de 100×130 (cabeça centrada em 50,42; corpo cortado em y=130).
   PogFace.fromEmoji(emoji) lê gênero, tom de pele e cabelo de um emoji de pessoa (ex.: 👩🏽‍🦱). */
(function(){
'use strict';
const hx=h=>{if(h.length===4)h='#'+h[1]+h[1]+h[2]+h[2]+h[3]+h[3];return [parseInt(h.slice(1,3),16),parseInt(h.slice(3,5),16),parseInt(h.slice(5,7),16)]};
const mix=(a,b,k)=>{const x=hx(a),y=hx(b);return '#'+x.map((v,i)=>Math.round(v+(y[i]-v)*k).toString(16).padStart(2,'0')).join('')};
const hash=s=>{let h=2166136261;s=String(s);for(let i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619)}return h>>>0};
const rng=seed=>{let a=seed>>>0||1;return()=>{a^=a<<13;a>>>=0;a^=a>>>17;a^=a<<5;a>>>=0;return a/4294967296}};
const pick=(R,a)=>a[Math.floor(R()*a.length)%a.length];
const SKIN=['#F8DCC8','#EEC3A0','#D29B73','#A56C47','#6A4228'];
const HAIR_DARK=['#1B1410','#2B1B12','#3D2616','#54351D'];
const SHIRTS=['#E8795A','#4C7FD6','#F4C26B','#6FB7C9','#9CCB86','#C99BD6','#D9534F','#2E8B7A','#F08FB1','#5B6BC9','#F2F2F2','#394867'];
let UID=0;
function fromEmoji(em){
  const cps=Array.from(String(em||'')).map(c=>c.codePointAt(0));
  const o={g:'n',tone:null,hairKind:null,age:'adult',beard:false};
  cps.forEach(c=>{
    if(c===0x1F469||c===0x1F467)o.g='f';else if(c===0x1F468||c===0x1F466)o.g='m';else if(c===0x1F9D4){o.g='m';o.beard=true}
    else if(c===0x1F475){o.g='f';o.age='old'}else if(c===0x1F474){o.g='m';o.age='old'}else if(c===0x1F9D3)o.age='old';
    else if(c===0x1F467||c===0x1F466||c===0x1F9D2)o.age='kid';
    if(c>=0x1F3FB&&c<=0x1F3FF)o.tone=c-0x1F3FB;
    if(c===0x1F9B0)o.hairKind='red';if(c===0x1F9B1)o.hairKind='curly';if(c===0x1F9B3)o.hairKind='gray';if(c===0x1F9B2)o.hairKind='bald';
  });
  return o;
}
function bust(o){
  o=o||{};const seed=o.seed!=null?o.seed:hash(JSON.stringify(o)),R=rng(seed),u='f'+(++UID)+'_';
  const g=o.g==='f'||o.g==='m'?o.g:(R()<.5?'f':'m');
  const tone=o.tone!=null?Math.max(0,Math.min(4,o.tone)):Math.floor(R()*5);
  const age=o.age||'adult';
  const skin=SKIN[tone],skinL=mix(skin,'#fff',.32),skinD=mix(skin,'#4a1f12',.34),skinDD=mix(skin,'#2a0f08',.5);
  let hair=pick(R,HAIR_DARK);
  if(o.hairKind==='red')hair='#A24A24';else if(o.hairKind==='gray'||age==='old')hair=pick(R,['#C9C9D0','#E3E3E8','#B2B2BB']);
  else if(tone<=1&&R()<.3)hair=pick(R,['#C9A25B','#8A5A2B','#6b4528']);
  else if(tone===4)hair='#120C09';
  if(o.hair)hair=o.hair;
  const hairD=mix(hair,'#000',.35),hairL=mix(hair,'#fff',.28);
  const style=o.hairKind==='bald'?'bald':o.hairKind==='curly'?'curly':(o.style||(g==='f'?pick(R,['long','long','wavy','bun','bob']):pick(R,['short','short','side','curly','short'])));
  const beard=o.beard!=null?o.beard:(g==='m'&&age!=='kid'&&R()<.28);
  const glasses=o.glasses!=null?o.glasses:R()<.17;
  const shirt=o.shirt||pick(R,SHIRTS),shirtD=mix(shirt,'#000',.3),shirtL=mix(shirt,'#fff',.2);
  const neck=pick(R,['crew','v','collar','crew']);
  const iris=pick(R,['#4A2F1B','#3B2A1E','#6B4A2B','#2E4A5C','#4C6B3A','#1F1A17']);
  const mood=o.mood||pick(R,['smile','smile','grin','soft']);
  const lipC=mix(tone>=3?'#7B3B34':'#C46A6E',skin,.15),lipD=mix(lipC,'#000',.25);
  const fem=g==='f';
  o.skinOut=skin;o.shirtOut=shirt;o.hairOut=hair;
  const rich=o.rich|0,Lt=o.light||null,ld=Lt?Lt.d:-1,lc=Lt?Lt.c:'#fff',lk=Lt?Lt.k:.6;
  let s=`<g>`;
  s+=`<defs><radialGradient id="${u}fc" cx="${Lt?(ld<0?.33:.67):.4}" cy=".32" r=".85"><stop offset="0" stop-color="${skinL}"/><stop offset=".55" stop-color="${skin}"/><stop offset="1" stop-color="${skinD}"/></radialGradient>
   <linearGradient id="${u}nk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${skinDD}"/><stop offset=".45" stop-color="${skinD}"/><stop offset="1" stop-color="${skin}"/></linearGradient>
   <linearGradient id="${u}sh" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${shirtL}"/><stop offset="1" stop-color="${shirtD}"/></linearGradient>
   <linearGradient id="${u}hr" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="${hairL}"/><stop offset=".5" stop-color="${hair}"/><stop offset="1" stop-color="${hairD}"/></linearGradient>
   <linearGradient id="${u}sd" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".28"/></linearGradient></defs>`;
  /* cabelo de trás */
  if(style==='long'||style==='wavy')s+=`<path d="M25 42 C17 72 20 100 29 112 L71 112 C80 100 83 72 75 42Z" fill="url(#${u}hr)"/>`;
  if(style==='bob')s+=`<path d="M26 40 C20 58 22 74 30 80 L70 80 C78 74 80 58 74 40Z" fill="url(#${u}hr)"/>`;
  if(style==='curly'&&fem)s+=`<circle cx="50" cy="38" r="31" fill="url(#${u}hr)"/>`;
  if(style==='bun')s+=`<circle cx="50" cy="11" r="9.5" fill="url(#${u}hr)"/><circle cx="46.5" cy="8" r="3" fill="${hairL}" fill-opacity=".5"/>`;
  /* tronco */
  s+=`<g transform="translate(0 -5)"><path d="M4 240 L4 130 C4 104 20 92 37 88 L63 88 C80 92 96 104 96 130 L96 240Z" fill="url(#${u}sh)"/><path d="M4 240 L4 130 C4 104 20 92 37 88 L63 88 C80 92 96 104 96 130 L96 240Z" fill="url(#${u}sd)"/>`;
  s+=`<path d="M22 112 C28 100 38 94 50 100" stroke="${shirtL}" stroke-opacity=".35" stroke-width="2" fill="none" stroke-linecap="round"/><path d="M78 110 C72 100 62 94 56 100" stroke="${shirtD}" stroke-opacity=".35" stroke-width="2" fill="none" stroke-linecap="round"/>`;
  if(rich>1){const sx=ld<0?1:-1;
    s+=`<defs><pattern id="${u}wv" width="2.6" height="2.6" patternUnits="userSpaceOnUse" patternTransform="rotate(35)"><rect width="2.6" height="1.1" fill="#000" fill-opacity=".08"/></pattern></defs><path d="M4 240 L4 130 C4 104 20 92 37 88 L63 88 C80 92 96 104 96 130 L96 240Z" fill="url(#${u}wv)"/>`;
    s+=`<g fill="none" stroke-linecap="round"><path d="M${50+sx*-22} 118 C${50+sx*-18} 132 ${50+sx*-24} 150 ${50+sx*-20} 170" stroke="${shirtD}" stroke-opacity=".3" stroke-width="2.4"/><path d="M${50+sx*14} 112 C${50+sx*20} 128 ${50+sx*16} 150 ${50+sx*22} 172" stroke="${shirtD}" stroke-opacity=".26" stroke-width="2"/><path d="M${50+sx*-30} 108 C${50+sx*-34} 118 ${50+sx*-36} 130 ${50+sx*-34} 142" stroke="${shirtL}" stroke-opacity=".38" stroke-width="2.2"/><path d="M${50+sx*-8} 124 C${50+sx*-4} 140 ${50+sx*-6} 156 ${50+sx*-2} 176" stroke="${shirtD}" stroke-opacity=".18" stroke-width="1.6"/></g>`;
    }
  if(rich){
    s+=`<path d="M${ld<0?4:96} 130 C${ld<0?4:96} 108 ${ld<0?16:84} 96 ${ld<0?34:66} 90" stroke="${lc}" stroke-opacity="${(.5*lk).toFixed(2)}" stroke-width="2" fill="none" stroke-linecap="round"/><ellipse cx="${ld<0?24:76}" cy="108" rx="14" ry="9" fill="${lc}" fill-opacity="${(.12*lk).toFixed(2)}"/>`}
  s+=`</g>`;
  /* pescoço + sombra do queixo */
  s+=`<path d="M40.5 56 L40.5 84 Q50 93 59.5 84 L59.5 56Z" fill="url(#${u}nk)"/>`;
  s+=`<g transform="translate(0 -5)">`;
  if(neck==='v')s+=`<path d="M38 88 L50 108 L62 88 Q50 96 38 88Z" fill="${skin}"/><path d="M38 88 L50 108 L62 88" stroke="${shirtD}" stroke-width="1.6" fill="none"/>`;
  else if(neck==='collar')s+=`<path d="M39 87 L50 104 L44 87Z" fill="#fff"/><path d="M61 87 L50 104 L56 87Z" fill="#f0f0f0"/><path d="M39 87 L50 104 L61 87" stroke="${shirtD}" stroke-opacity=".5" fill="none"/>`;
  else s+=`<path d="M37 88.5 Q50 99 63 88.5" stroke="${shirtD}" stroke-width="2.4" fill="none" stroke-linecap="round"/><path d="M38 88 Q50 97 62 88 Q50 100 38 88Z" fill="${skin}" fill-opacity=".0"/>`;
  s+=`</g><ellipse cx="50" cy="67" rx="13" ry="5.5" fill="${skinDD}" fill-opacity=".38"/>`;
  /* orelhas */
  [[31.2,1],[68.8,-1]].forEach(([x,d])=>{s+=`<ellipse cx="${x}" cy="45" rx="3.4" ry="5.2" fill="${skin}"/><ellipse cx="${x+d*.4}" cy="45.4" rx="1.5" ry="3" fill="${skinD}" fill-opacity=".55"/>`});
  /* rosto */
  s+=`<path d="M31 38 C31 17 69 17 69 38 C69 53 61 67 50 67.5 C39 67 31 53 31 38Z" fill="url(#${u}fc)"/>`;
  s+=`<ellipse cx="37.5" cy="53" rx="5.4" ry="3.2" fill="${tone>=3?'#C46A5A':'#F0707C'}" fill-opacity="${tone>=3?.16:.22}"/><ellipse cx="62.5" cy="53" rx="5.4" ry="3.2" fill="${tone>=3?'#C46A5A':'#F0707C'}" fill-opacity="${tone>=3?.16:.22}"/>`;
  if(rich){const sx=ld<0?1:-1,fx=50+sx*19;
    s+=`<path d="M${50+sx*19} 38 C${50+sx*19} 53 ${50+sx*11} 67 50 67.5 C${50+sx*7} 60 ${50+sx*12} 50 ${50+sx*12} 40 C${50+sx*12} 30 ${50+sx*8} 23 ${50+sx*2} 19.4 C${50+sx*14} 20.4 ${50+sx*19} 28 ${50+sx*19} 38Z" fill="${skinDD}" fill-opacity=".24"/>`;
    if(rich>1)s+=`<ellipse cx="${50-sx*6}" cy="27" rx="9" ry="3.6" fill="${lc}" fill-opacity="${(.2*lk).toFixed(2)}"/><ellipse cx="${50-sx*12}" cy="52" rx="4.6" ry="3" fill="#fff" fill-opacity=".12"/>`}
  /* barba */
  if(beard)s+=`<path d="M30.5 44 C30.5 62 38 71 50 71.5 C62 71 69.5 62 69.5 44 C66.5 53 62 57.5 55.5 58 L44.5 58 C38 57.5 33.5 53 30.5 44Z" fill="url(#${u}hr)" fill-opacity=".96"/><path d="M42 56.6 Q50 54.4 58 56.6 Q50 57.6 42 56.6Z" fill="${hairD}"/>`;
  /* olhos */
  const ey=43.2;
  [[41,-1],[59,1]].forEach(([x,d])=>{
    s+=`<ellipse cx="${x}" cy="${ey}" rx="4.9" ry="3" fill="#fff"/><ellipse cx="${x}" cy="${ey+.1}" rx="4.9" ry="3" fill="${skinD}" fill-opacity=".14"/>`;
    s+=`<circle cx="${x+d*.3}" cy="${ey+.1}" r="2.55" fill="${iris}"/><circle cx="${x+d*.3}" cy="${ey+.1}" r="1.15" fill="#0b0706"/><circle cx="${x+d*.3+.9}" cy="${ey-.8}" r=".8" fill="#fff"/>`;
    s+=`<path d="M${x-5.2} ${ey+.2} Q${x} ${ey-4.8} ${x+5.2} ${ey+.2}" stroke="${mix(hairD,'#000',.3)}" stroke-width="${fem?1.7:1.4}" fill="none" stroke-linecap="round"/><path d="M${x-4.2} ${ey+1.8} Q${x} ${ey+3.6} ${x+4.2} ${ey+1.8}" stroke="${skinD}" stroke-opacity=".5" stroke-width=".9" fill="none" stroke-linecap="round"/>`;
    if(fem)s+=`<path d="M${x+d*4.6} ${ey-.4} l${d*1.9} -1.4 M${x+d*3.4} ${ey-1.9} l${d*1.4} -1.7" stroke="${hairD}" stroke-width=".9" stroke-linecap="round"/>`;
    /* sobrancelhas */
    const by=ey-6.4,lift=mood==='soft'?-.6:mood==='grin'?-1:0;
    s+=`<path d="M${x-5.6} ${by+1.2+lift*-1} Q${x-.5} ${by-1.8+lift} ${x+5.4} ${by+.6+(d>0?.4:-.4)}" stroke="${hairD}" stroke-width="${fem?1.6:2.3}" fill="none" stroke-linecap="round" stroke-opacity=".92"/>`;
  });
  if(age==='old')s+=`<g stroke="${skinD}" stroke-opacity=".5" stroke-width=".7" fill="none" stroke-linecap="round"><path d="M33.5 41 l-2 -1.2 M33.4 43.5 l-2.2 .2 M33.6 46 l-2 1.2 M66.5 41 l2 -1.2 M66.6 43.5 l2.2 .2 M66.4 46 l2 1.2"/><path d="M40 30 Q50 28 60 30 M41 32.6 Q50 31 59 32.6"/><path d="M41.5 59.5 q-2 3 0 6 M58.5 59.5 q2 3 0 6"/></g>`;
  /* óculos */
  if(glasses)s+=`<g fill="#fff" fill-opacity=".1" stroke="${pick(R,['#2a2a33','#6b3d1e','#c0392b'])}" stroke-width="1.5"><circle cx="41" cy="${ey}" r="6.6"/><circle cx="59" cy="${ey}" r="6.6"/><path d="M47.6 ${ey} Q50 ${ey-1.8} 52.4 ${ey}" fill="none"/><path d="M34.4 ${ey-.4} L31.6 ${ey-1.4} M65.6 ${ey-.4} L68.4 ${ey-1.4}" fill="none"/></g>`;
  /* nariz */
  s+=`<path d="M50.2 44.4 C49.2 49 48.2 52.4 47.6 54 Q50 56 52.4 54" stroke="${skinD}" stroke-opacity=".75" stroke-width="1.15" fill="none" stroke-linecap="round" stroke-linejoin="round"/><ellipse cx="48.2" cy="54.4" rx="1" ry=".7" fill="${skinDD}" fill-opacity=".55"/><ellipse cx="51.8" cy="54.4" rx="1" ry=".7" fill="${skinDD}" fill-opacity=".55"/><ellipse cx="49.6" cy="49.6" rx="1.1" ry="3.4" fill="#fff" fill-opacity=".2"/>`;
  if(rich>1){const sx=ld<0?1:-1;
    [[41,-1],[59,1]].forEach(([x,d])=>{s+=`<ellipse cx="${x}" cy="${ey+3.6}" rx="4.8" ry="1.5" fill="${skinDD}" fill-opacity=".16"/><path d="M${x-5.4} ${ey-1.6} Q${x} ${ey-6.6} ${x+5.4} ${ey-1.6}" stroke="${skinD}" stroke-opacity=".5" stroke-width=".7" fill="none"/><circle cx="${x+d*.3}" cy="${ey+.1}" r="2.55" fill="none" stroke="#000" stroke-opacity=".35" stroke-width=".45"/><path d="M${x-2} ${ey+1.2} Q${x+d*.3} ${ey+2.5} ${x+2} ${ey+1.2}" stroke="#fff" stroke-opacity=".22" stroke-width=".6" fill="none"/>`});
    s+=`<path d="M${50-sx*1.4} 40 C${50-sx*1.6} 45 ${50-sx*2} 49 ${50-sx*2.4} 52" stroke="#fff" stroke-opacity=".2" stroke-width="1.4" fill="none" stroke-linecap="round"/><path d="M${50+sx*2.4} 46 C${50+sx*3.4} 50 ${50+sx*3.8} 53 ${50+sx*2.6} 55" stroke="${skinDD}" stroke-opacity=".22" stroke-width="1.6" fill="none" stroke-linecap="round"/><path d="M48.6 56.4 Q50 57.4 51.4 56.4" stroke="${skinDD}" stroke-opacity=".28" stroke-width=".6" fill="none"/>`}
  /* boca */
  const my=60.4;
  if(mood==='grin'){s+=`<path d="M43.2 ${my-1} Q50 ${my+7.6} 56.8 ${my-1} Q50 ${my-.6} 43.2 ${my-1}Z" fill="#7a2228"/><path d="M44.6 ${my-.3} Q50 ${my+2.2} 55.4 ${my-.3} L55.4 ${my-1} Q50 ${my-.4} 44.6 ${my-1}Z" fill="#fff"/>`}
  s+=`<path d="M43.4 ${my} Q46.8 ${my-1.9} 50 ${my-.8} Q53.2 ${my-1.9} 56.6 ${my} Q50 ${my+(mood==='soft'?.8:1.4)} 43.4 ${my}Z" fill="${lipD}"/>`;
  s+=`<path d="M44.2 ${my+.3} Q50 ${my+(mood==='grin'?4.2:mood==='soft'?3:3.8)} 55.8 ${my+.3} Q50 ${my+1.8} 44.2 ${my+.3}Z" fill="${lipC}"/><path d="M47.6 ${my+2.6} Q50 ${my+3.2} 52.4 ${my+2.6}" stroke="#fff" stroke-opacity=".28" stroke-width=".9" fill="none" stroke-linecap="round"/>`;
  if(mood!=='soft')s+=`<path d="M43.2 ${my-.2} q-1.3 -.3 -1.7 -1.4 M56.8 ${my-.2} q1.3 -.3 1.7 -1.4" stroke="${skinD}" stroke-opacity=".6" stroke-width=".8" fill="none" stroke-linecap="round"/>`;
  if(beard)s+=`<path d="M41.6 ${my-1.6} Q46 ${my-4.4} 50 ${my-3.2} Q54 ${my-4.4} 58.4 ${my-1.6} Q54 ${my-2.6} 50 ${my-2} Q46 ${my-2.6} 41.6 ${my-1.6}Z" fill="${hairD}"/>`;
  /* cabelo da frente */
  const shine=`<path d="M38 25 Q50 20 62 26" stroke="${hairL}" stroke-opacity=".6" stroke-width="1.6" fill="none" stroke-linecap="round"/><path d="M34 31 Q42 24 50 24" stroke="${hairL}" stroke-opacity=".4" stroke-width="1.1" fill="none" stroke-linecap="round"/>`;
  if(style==='short')s+=`<path d="M30 40 C27 13 73 11 70 40 C68.5 31 64 27 58 26 C54 30 42 31 36 27 C32 30 30.4 34 30 40Z" fill="url(#${u}hr)"/>${shine}`;
  else if(style==='side')s+=`<path d="M30 41 C26 12 74 10 70 41 C69 32 66 27 60 25 C50 30 38 29 33 24 C31 29 30 34 30 41Z" fill="url(#${u}hr)"/><path d="M33 24 C42 24 52 22 62 25" stroke="${hairD}" stroke-width="1" fill="none"/>${shine}`;
  else if(style==='long'||style==='wavy'||style==='bun'||style==='bob')s+=`<path d="M30 44 C24 12 76 8 70 44 C69 33 64 25 52 24 C44 31 36 30 34 38 C32 40 31 42 30 44Z" fill="url(#${u}hr)"/><path d="M52 24 C48 29 42 33 34 36" stroke="${hairD}" stroke-opacity=".5" stroke-width="1" fill="none"/>${shine}`;
  else if(style==='curly'){let c='';for(let i=0;i<13;i++){const a=Math.PI*(1.05+i*.083),r=20+R()*3,x=50+Math.cos(a)*r*1.18,y=40+Math.sin(a)*r*1.1;c+=`<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="${(6+R()*2.4).toFixed(1)}" fill="${i%3?hair:hairD}"/>`}s+=c+`<path d="M33 34 Q50 20 67 34 C64 27 58 24 50 24 C42 24 36 27 33 34Z" fill="url(#${u}hr)"/>`+shine}
  else if(style==='bald')s+=`<path d="M32 36 C34 22 66 22 68 36" stroke="${hairL}" stroke-opacity=".28" stroke-width="2" fill="none" stroke-linecap="round"/><ellipse cx="44" cy="26" rx="6" ry="2.2" fill="#fff" fill-opacity=".18"/>`;
  if(rich&&style!=='bald'){let st='';if(rich>1){const hs=rng(seed+3);
    if(rich>1)for(let i=0;i<9;i++){const a=-.35+i*.09+hs()*.05,x0=33+i*4.2,y0=24+Math.abs(i-4)*1.4;st+=`M${x0.toFixed(1)} ${(y0+7).toFixed(1)}Q${(x0+2+hs()*3).toFixed(1)} ${(y0-2).toFixed(1)} ${(x0+9+i*.4).toFixed(1)} ${(y0-3+hs()*3).toFixed(1)}`}
    s+=`<path d="${st}" stroke="${hairL}" stroke-opacity=".34" stroke-width=".55" fill="none" stroke-linecap="round"/>`}
    s+=`<path d="M${ld<0?31.2:68.8} 36 C${ld<0?31:69} 26 ${ld<0?38:62} 18.6 50 17.6" stroke="${lc}" stroke-opacity="${(.55*lk).toFixed(2)}" stroke-width="1.1" fill="none" stroke-linecap="round"/>`}
  if(age==='kid')s=s.replace('<g>','<g>');
  if(o.hat==='cap')s+=`<path d="M28 33 C28 10 72 10 72 33Z" fill="${o.hatColor||'#2F6BE8'}"/><path d="M66 31 L86 35 Q84 39 64 36Z" fill="${mix(o.hatColor||'#2F6BE8','#000',.25)}"/>`;
  s+='</g>';
  if(o.grade){const G=o.grade,cache={};s=s.replace(/#[0-9a-fA-F]{6}\b/g,c=>cache[c]||(cache[c]=mix(c,G.c,G.k)))}
  return s;
}
/* avatar redondo (só o rosto) a partir do emoji do personagem; usado nos chats */
function avatar(em,name,color){
  const o=fromEmoji(em);o.seed=hash(String(name||em));
  if(!o.g||o.g==='n')o.g=(/^(you|voc)/i.test(String(name))?'m':(o.g||undefined));
  if(color&&/^#[0-9a-f]{6}$/i.test(color))o.shirt=color;
  if(em==='🙂'||em==='😀'||!/[\u{1F466}-\u{1F469}\u{1F9D1}-\u{1F9D4}\u{1F474}\u{1F475}]/u.test(em||''))o.g=o.g||undefined;
  return '<svg viewBox="16 8 68 68" width="100%" height="100%" aria-hidden="true">'+bust(o)+'</svg>';
}
window.PogFace={bust,fromEmoji,avatar,SHIRTS};
})();
