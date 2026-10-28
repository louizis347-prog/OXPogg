/* Capas ilustradas das obras: identidade visual própria por obra (traço de nanquim, cor chapada com uma sombra,
   textura de papel). Usadas na capa do episódio e na figurinha. Obras: Paddington, Alice, O Mágico de Oz, Peter Pan, Toy Story. */
(function(){
'use strict';
const INK='#2b1d3a';
let UID=0;
const stk=(w)=>`stroke="${INK}" stroke-width="${w==null?3:w}" stroke-linejoin="round" stroke-linecap="round"`;
const P=(d,fill,w,extra)=>`<path d="${d}" fill="${fill}" ${w===0?'':stk(w)} ${extra||''}/>`;
const E=(cx,cy,rx,ry,fill,w,extra)=>`<ellipse cx="${cx}" cy="${cy}" rx="${rx}" ry="${ry}" fill="${fill}" ${w===0?'':stk(w)} ${extra||''}/>`;
const C=(cx,cy,r,fill,w,extra)=>E(cx,cy,r,r,fill,w,extra);
const R=(x,y,w,h,fill,rx,sw)=>`<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${rx||0}" fill="${fill}" ${sw===0?'':stk(sw)}/>`;
const L=(x1,y1,x2,y2,w,fill)=>`<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${INK}" stroke-width="${w+6}" stroke-linecap="round"/><line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${fill}" stroke-width="${w}" stroke-linecap="round"/>`;
const eyes=(x,y,gap,r)=>{gap=gap||13;r=r||4.4;return [-1,1].map(s=>`<ellipse cx="${x+s*gap}" cy="${y}" rx="${r}" ry="${r*1.3}" fill="${INK}"/><circle cx="${x+s*gap+1.4}" cy="${y-2}" r="${r*.38}" fill="#fff"/>`).join('')};
const blush=(x,y,gap)=>[-1,1].map(s=>`<ellipse cx="${x+s*gap}" cy="${y}" rx="7" ry="4.4" fill="#ff8aa0" opacity=".55"/>`).join('');
const smile=(x,y,w)=>`<path d="M${x-w} ${y} Q${x} ${y+w*.95} ${x+w} ${y}" fill="none" stroke="${INK}" stroke-width="2.8" stroke-linecap="round"/>`;
const grp=(t,inner)=>`<g transform="${t}">${inner}</g>`;
const shadow=(w)=>E(0,0,w||44,8,'rgba(30,20,50,.22)',0);

/* ---------- criança genérica (origem: pés; altura ~190) ---------- */
function kid(o){
  const sk=o.skin||'#ffd7b5',hair=o.hair||'#f4d06f',top=o.top||'#7ec8f2',bot=o.bot||top;let g=shadow();
  if(o.hairStyle==='long')g+=P('M-37,-142 Q-46,-198 0,-198 Q46,-198 37,-142 Q43,-98 30,-88 L-30,-88 Q-43,-98 -37,-142Z',hair);
  if(o.hairStyle==='braids')g+=[-1,1].map(s=>L(s*30,-132,s*40,-92,13,hair)+C(s*40,-90,6,o.ribbon||'#e8473b',2.4)).join('');
  if(o.dress){
    g+=L(-12,-52,-13,-9,12,o.legs||sk)+L(12,-52,13,-9,12,o.legs||sk);
    g+=E(-16,-5,15,7,o.shoe||'#3a3550',2.6)+E(16,-5,15,7,o.shoe||'#3a3550',2.6);
    g+=P('M-22,-112 L22,-112 L46,-44 Q0,-34 -46,-44 Z',top);
    if(o.apron)g+=P('M-13,-110 L13,-110 L26,-48 Q0,-40 -26,-48 Z','#fff');
    if(o.gingham){for(let i=0;i<5;i++)g+=`<path d="M${-32+i*16},-92 L${-38+i*18},-48" stroke="#fff" stroke-width="3" opacity=".55"/>`;for(let j=0;j<3;j++)g+=`<path d="M-30,${-100+j*18} L30,${-100+j*18}" stroke="#fff" stroke-width="3" opacity=".5"/>`}
  }else{
    g+=L(-10,-70,-12,-10,16,o.bot||'#4a6fa5')+L(10,-70,12,-10,16,o.bot||'#4a6fa5');
    g+=E(-15,-6,16,8,o.shoe||'#6b3f22',2.6)+E(15,-6,16,8,o.shoe||'#6b3f22',2.6);
    g+=P('M-24,-116 L24,-116 L26,-62 Q0,-54 -26,-62 Z',top);
    if(o.belt)g+=R(-26,-70,52,9,o.belt,3,2.4);
  }
  const A=o.arms||'down';const hands={down:[[-40,-62],[40,-62]],up:[[-44,-150],[44,-150]],wave:[[-40,-62],[46,-156]],out:[[-58,-100],[58,-100]],point:[[-40,-62],[66,-120]],fly:[[-62,-130],[62,-96]]}[A];
  g+=L(-24,-106,hands[0][0],hands[0][1],10,o.sleeve||top)+L(24,-106,hands[1][0],hands[1][1],10,o.sleeve||top);
  g+=C(hands[0][0],hands[0][1],7,sk,2.6)+C(hands[1][0],hands[1][1],7,sk,2.6);
  if(o.dress)g+=C(-24,-108,12,o.sleeve||top,2.8)+C(24,-108,12,o.sleeve||top,2.8);
  if(o.ears)g+=[-1,1].map(s=>P(`M${s*30},-146 L${s*50},-166 L${s*36},-132Z`,sk)).join('');
  g+=C(0,-140,34,sk);
  if(o.hairStyle==='long')g+=P('M-35,-146 Q-31,-178 0,-176 Q31,-178 35,-146 Q14,-162 0,-160 Q-14,-162 -35,-146Z',hair);
  if(o.hairStyle==='braids')g+=P('M-35,-144 Q-32,-178 0,-177 Q32,-178 35,-144 Q12,-158 0,-156 Q-12,-158 -35,-144Z',hair);
  if(o.hairStyle==='short')g+=P('M-35,-144 Q-36,-180 0,-178 Q36,-180 35,-144 Q20,-166 6,-158 Q-10,-170 -35,-144Z',hair);
  if(o.band)g+=`<path d="M-36,-150 Q0,-184 36,-150" fill="none" stroke="${o.band}" stroke-width="7" stroke-linecap="round"/>`+P('M-36,-152 L-50,-162 L-48,-144Z M-36,-152 L-26,-164 L-24,-146Z',o.band,2.4);
  g+=eyes(0,-140,13)+blush(0,-128,22)+smile(0,-125,9);
  if(o.hat==='cowboy')g+=P('M-52,-168 Q-30,-176 -20,-182 Q0,-212 20,-182 Q30,-176 52,-168 Q30,-158 0,-160 Q-30,-158 -52,-168Z',o.hatColor||'#8a5a2b');
  if(o.hat==='cap')g+=P('M-34,-166 Q-6,-196 38,-168 Q8,-164 -34,-166Z',o.hatColor||'#2f9d5b')+P('M14,-176 Q40,-212 52,-196 Q40,-190 24,-172Z','#e8473b',2.4);
  return g;
}

/* ---------- personagens ---------- */
const CH={
 alice(){return kid({hair:'#f4d06f',hairStyle:'long',top:'#7ec8f2',apron:true,dress:true,legs:'#fff',band:'#2a6fd6',arms:'wave'})},
 mrs(){return kid({skin:'#f2c9a4',hair:'#7a4a2a',hairStyle:'short',top:'#2f9d8f',dress:true,legs:'#f2c9a4',arms:'wave'})},
 dorothy(){return kid({hair:'#7a4a2a',hairStyle:'braids',ribbon:'#e8473b',top:'#6fa8e8',gingham:true,dress:true,shoe:'#e03a4e',legs:'#fff',arms:'down'})},
 wendy(){return kid({hair:'#7a4a2a',hairStyle:'long',top:'#dce9ff',dress:true,legs:'#ffd7b5',shoe:'#ffd7b5',arms:'out'})},
 peter(){return kid({hair:'#e8803a',hairStyle:'short',top:'#2f9d5b',bot:'#3f8a4a',ears:true,hat:'cap',arms:'fly',shoe:'#6b3f22'})},
 woody(){return kid({skin:'#ffd7b5',hair:'#6a3f22',hairStyle:'short',top:'#f2c63d',bot:'#3f6fb5',hat:'cowboy',belt:'#7a4a22',arms:'down',shoe:'#7a4a22'})+P('M-22,-112 L-10,-112 L-10,-66 L-24,-70Z M22,-112 L10,-112 L10,-66 L24,-70Z','#f4f0e8',2.4)+C(-16,-96,4,INK,0)+C(16,-84,4,INK,0)+P('M-14,-116 L0,-100 L14,-116Z','#e8473b',2.4)},
 buzz(){let g=shadow();
  g+=L(-11,-70,-12,-12,17,'#f4f4f8')+L(11,-70,12,-12,17,'#f4f4f8')+E(-15,-6,17,8,'#7b4cc2',2.6)+E(15,-6,17,8,'#7b4cc2',2.6);
  g+=P('M-30,-120 L30,-120 L28,-62 Q0,-54 -28,-62Z','#f4f4f8')+P('M-30,-120 L-12,-120 L-12,-84 L-28,-84Z M30,-120 L12,-120 L12,-84 L28,-84Z','#7b4cc2',2.6)+R(-10,-108,20,18,'#fff',3,2.4)+C(-4,-99,2.4,'#3fbf5b',0)+C(4,-99,2.4,'#e8473b',0);
  g+=L(-30,-112,-50,-70,12,'#f4f4f8')+L(30,-112,52,-130,12,'#f4f4f8')+C(-50,-70,8,'#7bd26b',2.6)+C(52,-130,8,'#7bd26b',2.6);
  g+=P('M-30,-150 Q-60,-170 -52,-124 Q-40,-134 -30,-132Z M30,-150 Q60,-170 52,-124 Q40,-134 30,-132Z','#7b4cc2',2.8);
  g+=C(0,-144,32,'#f4f4f8')+E(0,-138,21,24,'#ffd7b5',2.6)+P('M-33,-148 Q-34,-178 0,-178 Q34,-178 33,-148 Q20,-158 0,-158 Q-20,-158 -33,-148Z','#3fbf5b',2.8);
  g+=eyes(0,-142,11,4)+smile(0,-124,8)+P('M-8,-152 L8,-152','#000',2);return g},
 paddington(){let g=shadow(54);
  g+=L(-16,-52,-18,-12,20,'#7a4a2a')+L(16,-52,18,-12,20,'#7a4a2a')+E(-20,-8,18,9,'#4a2f1a',2.8)+E(20,-8,18,9,'#4a2f1a',2.8);
  g+=P('M-42,-132 Q-52,-80 -40,-44 Q0,-34 40,-44 Q52,-80 42,-132 Q0,-146 -42,-132Z','#2f5fb8');
  g+=R(-4,-130,8,86,'#1f4584',2,2);
  for(let i=0;i<3;i++)g+=P(`M-24,${-110+i*22} Q-12,${-114+i*22} -6,${-106+i*22} Q-12,${-98+i*22} -24,${-104+i*22}Z`,'#e0b86a',2.4);
  g+=L(-38,-112,-58,-74,14,'#2f5fb8')+L(38,-112,56,-84,14,'#2f5fb8')+C(-58,-74,10,'#7a4a2a',2.8)+C(56,-84,10,'#7a4a2a',2.8);
  g+=[-1,1].map(s=>E(s*34,-170,15,15,'#7a4a2a')+E(s*34,-170,8,8,'#d9a15a',0)).join('');
  g+=E(0,-150,42,38,'#7a4a2a')+E(0,-138,24,19,'#e8c58f')+P('M-9,-146 Q0,-154 9,-146 Q8,-138 0,-136 Q-8,-138 -9,-146Z','#1b1224',2.2);
  g+=eyes(0,-160,17,5.2)+`<path d="M-6,-128 Q0,-122 6,-128" fill="none" stroke="${INK}" stroke-width="2.6" stroke-linecap="round"/>`;
  g+=P('M-52,-172 Q-30,-182 -22,-190 Q0,-216 22,-190 Q30,-182 52,-172 Q30,-162 0,-164 Q-30,-162 -52,-172Z','#d63a2f')+P('M-18,-190 Q0,-198 18,-190','none',2.4);
  return g},
 rabbit(){let g=shadow(36);
  g+=L(-10,-50,-12,-10,13,'#fff')+L(10,-50,12,-10,13,'#fff')+E(-15,-6,16,8,'#fff',2.6)+E(15,-6,16,8,'#fff',2.6);
  g+=P('M-26,-112 L26,-112 L30,-52 Q0,-44 -30,-52Z','#fff')+P('M-26,-112 L-6,-112 L-6,-48 L-30,-52Z M26,-112 L6,-112 L6,-48 L30,-52Z','#e8473b',2.6);
  g+=L(-26,-104,-40,-66,10,'#fff')+L(26,-104,34,-72,10,'#fff')+C(-40,-66,7,'#fff',2.6)+C(34,-72,7,'#fff',2.6);
  g+=C(34,-62,11,'#f2c63d',2.6)+C(34,-62,7,'#fff',1.6)+`<path d="M34,-62 L34,-67 M34,-62 L38,-62" stroke="${INK}" stroke-width="1.6"/>`;
  g+=[-1,1].map(s=>E(s*14,-176,9,32,'#fff')+E(s*14,-176,4.5,24,'#ffb3c0',0)).join('');
  g+=E(0,-134,30,28,'#fff')+eyes(0,-138,11,3.8)+P('M-4,-128 Q0,-124 4,-128 Q2,-122 0,-122 Q-2,-122 -4,-128Z','#ff8aa0',2)+blush(0,-128,18);
  return g},
 cat(){let g='';
  g+=P('M-62,-30 Q-70,-100 -30,-130 Q0,-140 30,-130 Q70,-100 62,-30 Q30,-10 -30,-10 Q-62,-14 -62,-30Z','#9b6ad8');
  [-86,-60,-34].forEach((y,i)=>{g+=`<path d="M${-58+i*3},${y+30} Q0,${y+48} ${58-i*3},${y+30}" fill="none" stroke="#5d3a96" stroke-width="6" stroke-linecap="round" opacity=".7"/>`});
  g+=P('M-48,-118 L-70,-160 L-24,-136Z M48,-118 L70,-160 L24,-136Z','#9b6ad8')+P('M-44,-128 L-58,-150 L-34,-136Z M44,-128 L58,-150 L34,-136Z','#f3a6c8',0);
  g+=E(0,-98,48,40,'#9b6ad8')+[-1,1].map(s=>E(s*20,-110,13,13,'#f6e66a')+E(s*20,-110,3.6,9,INK,0)).join('');
  g+=P('M-40,-82 Q0,-52 40,-82 Q30,-60 0,-58 Q-30,-60 -40,-82Z','#fff')+`<path d="M-30,-70 L30,-70 M-14,-76 L-12,-60 M0,-76 L0,-58 M14,-76 L12,-60" stroke="${INK}" stroke-width="2.2" fill="none"/>`;
  return g},
 toto(){let g=shadow(26);
  g+=E(0,-24,28,18,'#3a2d3f')+L(-14,-14,-16,-2,8,'#3a2d3f')+L(14,-14,16,-2,8,'#3a2d3f')+C(26,-36,15,'#3a2d3f')+P('M20,-48 L18,-66 L30,-52Z M32,-46 L38,-62 L40,-44Z','#3a2d3f')+C(31,-34,3,'#000',0)+C(24,-40,2.6,'#fff',0)+P('M-28,-28 Q-44,-40 -38,-48','none',4)+E(36,-30,5,3.6,'#000',0);
  return g},
 scarecrow(){let g=shadow(40);
  g+=L(-12,-66,-14,-12,16,'#8a6a3a')+L(12,-66,14,-12,16,'#8a6a3a')+E(-16,-8,16,7,'#5a3f22',2.4)+E(16,-8,16,7,'#5a3f22',2.4);
  g+=P('M-26,-116 L26,-116 L28,-62 Q0,-54 -28,-62Z','#c4944a')+P('M-8,-100 L8,-100 L8,-82 L-8,-82Z','#d9503f',2.2);
  g+=L(-26,-108,-66,-96,11,'#c4944a')+L(26,-108,66,-96,11,'#c4944a')+[-1,1].map(s=>[0,1,2].map(i=>`<path d="M${s*(66+i*4)},-96 L${s*(78+i*5)},${-104+i*8}" stroke="#e8c870" stroke-width="3" stroke-linecap="round"/>`).join('')).join('');
  g+=C(0,-142,32,'#e8c58f')+`<path d="M-26,-128 L-6,-126 M26,-128 L6,-126" stroke="${INK}" stroke-width="2"/>`+eyes(0,-144,11,4)+P('M-4,-132 L4,-132 L0,-126Z','#d9503f',2)+`<path d="M-12,-118 Q0,-110 12,-118" fill="none" stroke="${INK}" stroke-width="2.4"/>`+`<path d="M-8,-118 L-8,-112 M0,-116 L0,-110 M8,-118 L8,-112" stroke="${INK}" stroke-width="1.6"/>`;
  g+=P('M-46,-158 Q-30,-166 -22,-174 Q0,-206 22,-174 Q30,-166 46,-158 Q24,-152 0,-153 Q-24,-152 -46,-158Z','#6a4a2a')+P('M-24,-176 Q0,-184 24,-176','none',2.4)+[0,1,2].map(i=>`<path d="M${-32+i*6},-156 L${-38+i*7},-140" stroke="#e8c870" stroke-width="3" stroke-linecap="round"/>`).join('');
  return g},
 lion(){let g=shadow(44);
  g+=P('M32,-52 Q70,-66 66,-98 Q60,-82 36,-72Z','#e8923a')+C(66,-100,7,'#a8501f',2.4);
  g+=L(-14,-60,-16,-12,19,'#e8a24a')+L(14,-60,16,-12,19,'#e8a24a')+E(-18,-8,18,8,'#e8a24a',2.6)+E(18,-8,18,8,'#e8a24a',2.6);
  g+=P('M-34,-118 Q-44,-70 -34,-52 Q0,-42 34,-52 Q44,-70 34,-118 Q0,-130 -34,-118Z','#e8a24a')+E(0,-80,20,26,'#f6d9a0',0);
  g+=L(-32,-108,-50,-70,13,'#e8a24a')+L(32,-108,50,-70,13,'#e8a24a');
  g+=C(0,-150,50,'#c4651f')+[...Array(10)].map((_,i)=>{const a=i/10*Math.PI*2;return C(Math.cos(a)*44,-150+Math.sin(a)*44,12,'#c4651f',2.6)}).join('')+C(0,-148,40,'#c4651f',0);
  g+=C(0,-148,31,'#e8a24a')+[-1,1].map(s=>C(s*28,-174,10,'#e8a24a',2.8)+C(s*28,-174,5,'#f3a6a0',0)).join('');
  g+=E(0,-136,17,13,'#f6d9a0')+P('M-7,-142 Q0,-148 7,-142 Q4,-134 0,-134 Q-4,-134 -7,-142Z','#5a2f22',2)+eyes(0,-153,12,4)+`<path d="M0,-134 L0,-128 M-8,-126 Q0,-120 8,-126" stroke="${INK}" stroke-width="2.2" fill="none"/>`;
  return g},
 tinker(){let g='';
  g+=P('M-4,-26 Q-36,-62 -16,-86 Q-10,-62 -2,-34Z M4,-26 Q36,-62 16,-86 Q10,-62 2,-34Z','rgba(190,240,255,.8)',2.2);
  g+=P('M-8,-40 L8,-40 L12,-8 L-12,-8Z','#7fe08f',2.4)+L(-4,-8,-5,12,5,'#ffd7b5')+L(5,-8,6,12,5,'#ffd7b5')+L(-8,-36,-18,-20,5,'#ffd7b5')+L(8,-36,18,-26,5,'#ffd7b5');
  g+=C(0,-52,11,'#ffd7b5')+P('M-11,-52 Q-12,-66 0,-66 Q12,-66 11,-52 Q4,-58 0,-58 Q-4,-58 -11,-52Z','#f4d06f',2.2)+C(0,-70,5,'#f4d06f',2.2)+eyes(0,-52,4.4,1.7)+smile(0,-46,3);
  return g}
};

/* ---------- cenários ---------- */
const defsCommon=(id)=>`<filter id="gr${id}" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" seed="${id%9+2}"/><feColorMatrix values="0 0 0 0 .2  0 0 0 0 .15  0 0 0 0 .1  0 0 0 .09 0"/></filter>
<radialGradient id="vg${id}" cx=".5" cy=".5" r=".75"><stop offset=".6" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#1b1030" stop-opacity=".38"/></radialGradient>`;
const finish=(id)=>`<rect width="800" height="450" filter="url(#gr${id})"/><rect width="800" height="450" fill="url(#vg${id})"/>`;
const star=(x,y,r,f)=>`<path d="M${x},${y-r} L${x+r*.3},${y-r*.3} L${x+r},${y} L${x+r*.3},${y+r*.3} L${x},${y+r} L${x-r*.3},${y+r*.3} L${x-r},${y} L${x-r*.3},${y-r*.3}Z" fill="${f||'#fff6c8'}"/>`;
const cloud=(x,y,s,f)=>grp(`translate(${x} ${y}) scale(${s})`,`<path d="M-60,0 Q-70,-30 -36,-34 Q-24,-60 6,-48 Q36,-62 50,-34 Q80,-30 66,0Z" fill="${f||'#fff'}" ${stk(2.6)}/>`);
const place=(id,x,y,s,flip)=>grp(`translate(${x} ${y}) scale(${flip?-s:s} ${s})`,CH[id]());

const SCN={
 paddington(){const i=++UID;
  return `<defs>${defsCommon(i)}<linearGradient id="sk${i}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f6d9a8"/><stop offset="1" stop-color="#e8946a"/></linearGradient></defs>
  <rect width="800" height="450" fill="url(#sk${i})"/>
  <g opacity=".95">${[0,1,2,3].map(k=>`<path d="M${k*220-40},320 L${k*220-40},150 Q${k*220+70},40 ${k*220+180},150 L${k*220+180},320Z" fill="rgba(255,255,255,.28)" ${stk(3)}/>`).join('')}${[0,1,2,3].map(k=>`<path d="M${k*220-40},170 Q${k*220+70},60 ${k*220+180},170 M${k*220+70},62 L${k*220+70},320" fill="none" stroke="${INK}" stroke-width="2.4"/>`).join('')}</g>
  <path d="M0,70 L800,70" stroke="${INK}" stroke-width="3"/><path d="M0,98 Q400,30 800,98" fill="none" stroke="${INK}" stroke-width="3"/>
  <g>${[0,1,2,3,4,5,6,7].map(k=>`<path d="M${k*110},70 L${k*110+55},98" stroke="${INK}" stroke-width="2.4"/>`).join('')}</g>
  <rect y="320" width="800" height="130" fill="#6d5a78"/><path d="M0,320 L800,320" stroke="${INK}" stroke-width="3"/>
  ${[0,1,2,3,4,5].map(k=>`<path d="M${k*150-20},450 L${k*150+30},320" stroke="#4d3d58" stroke-width="3" opacity=".6"/>`).join('')}
  ${R(560,232,150,90,'#e8473b',6)}${R(566,238,138,16,'#fff',3,0)}<text x="635" y="251" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="12" fill="${INK}">PADDINGTON</text>${C(698,260,12,'#f2c63d',2.6)}
  ${[0,1].map(k=>`<g transform="translate(${90+k*40} 320)"><rect x="-26" y="-60" width="52" height="60" rx="6" fill="${k?'#2f9d8f':'#d9a15a'}" ${stk(3)}/><path d="M-26,-34 L26,-34" stroke="${INK}" stroke-width="2.6"/></g>`).join('')}
  <g transform="translate(330 392)">${P('M-62,-6 L62,-6 L50,-70 L-50,-70Z','#a8501f')}${R(-62,-70,124,14,'#8a3f18',4)}${P('M-20,-72 Q0,-96 20,-72','none',4)}${R(-14,-48,28,26,'#f6d9a0',4)}<text x="0" y="-30" text-anchor="middle" font-family="Georgia,serif" font-size="9" font-weight="700" fill="${INK}">LONDON</text></g>
  ${place('paddington',440,408,1.22)}${place('mrs',620,380,.98,true)}
  <g opacity=".5">${[0,1,2].map(k=>cloud(120+k*260,104+k*10,.5,'#fff')).join('')}</g>${finish(i)}`},
 alice(){const i=++UID;
  return `<defs>${defsCommon(i)}<linearGradient id="sk${i}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7fd8cf"/><stop offset="1" stop-color="#f6e8a8"/></linearGradient></defs>
  <rect width="800" height="450" fill="url(#sk${i})"/>
  ${[0,1,2,3,4].map(k=>`<g transform="translate(${60+k*170} ${150+(k%2)*30})"><path d="M0,0 Q-6,80 0,160" stroke="#2f8f6a" stroke-width="8" fill="none"/>${[0,1,2,3,4].map(j=>E(Math.cos(j*1.256)*24,Math.sin(j*1.256)*24-6,18,18,['#ff8fb1','#ffd35c','#9b6ad8','#ff8fb1','#7ec8f2'][(k+j)%5],2.8)).join('')}${C(0,-6,13,'#f6c84c',2.8)}</g>`).join('')}
  <path d="M0,300 Q200,250 400,290 Q600,330 800,270 L800,450 L0,450Z" fill="#4ea866" ${stk(3)}/><path d="M0,350 Q250,320 500,350 Q700,372 800,340 L800,450 L0,450Z" fill="#3f9457" ${stk(3)}/>
  ${[0,1,2,3,4,5,6].map(k=>`<path d="M${40+k*120},${330+(k%3)*18} l6,-22 l6,22 M${52+k*120},${330+(k%3)*18} l6,-16 l5,16" stroke="#2c7a46" stroke-width="3" fill="none" stroke-linecap="round"/>`).join('')}
  ${[0,1,2].map(k=>`<g transform="translate(${620+k*50} ${300+k*14}) scale(${1-k*.2})"><path d="M-8,0 L-8,-40 Q-34,-44 -34,-62 Q0,-84 34,-62 Q34,-44 8,-40 L8,0Z" fill="${['#e8473b','#ffd35c','#9b6ad8'][k]}" ${stk(2.8)}/>${[-16,0,16].map(x=>C(x,-62,4,'#fff',0)).join('')}</g>`).join('')}
  
  ${[0,1,2].map(k=>`<g transform="translate(${700-k*40} ${70+k*24}) rotate(${k*9-8})">${R(-20,-28,40,56,'#fff',5)}<text x="-12" y="-8" font-family="Georgia,serif" font-weight="700" font-size="18" fill="#e8473b">${['♥','♠','♦'][k]}</text></g>`).join('')}
  ${place('cat',612,196,.7)}${place('alice',250,408,1.18)}${place('rabbit',430,398,1.12,true)}
  ${star(60,60,9)}${star(310,40,7)}${star(520,70,8)}${finish(i)}`},
 oz(){const i=++UID;
  return `<defs>${defsCommon(i)}<linearGradient id="sk${i}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4fb8e8"/><stop offset="1" stop-color="#cdf0f7"/></linearGradient></defs>
  <rect width="800" height="450" fill="url(#sk${i})"/>
  ${['#e8473b','#f29b34','#f6d35c','#3fb86b','#3e8fd8','#7b4cc2'].map((c,k)=>`<path d="M60,330 Q400,${-20+k*0} 740,330" transform="translate(0 ${k*13})" fill="none" stroke="${c}" stroke-width="15" opacity=".92"/>`).join('')}
  ${cloud(110,300,.9)}${cloud(690,310,.9)}
  <g transform="translate(560 170)">${[[-70,70,34,'#3fb86b'],[-34,50,40,'#34a862'],[0,26,48,'#3fb86b'],[34,50,40,'#34a862'],[70,70,34,'#3fb86b']].map(([x,y,h,c])=>`<g><rect x="${x-14}" y="${y-h}" width="28" height="${h*2.2}" fill="${c}" ${stk(2.8)}/>${P(`M${x-17},${y-h} L${x},${y-h-30} L${x+17},${y-h}Z`,c)}</g>`).join('')}${star(0,-30,10,'#fff')}</g>
  <path d="M470,450 Q420,380 520,350 Q620,320 560,290 Q530,276 570,262 L640,262" fill="none" stroke="#f6c200" stroke-width="64" stroke-linecap="round"/>
  <path d="M0,450 L0,360 Q250,330 470,372 L470,450Z" fill="#4ea866" ${stk(3)}/><path d="M800,450 L800,330 Q700,300 600,330 L560,450Z" fill="#4ea866" ${stk(3)}/>
  <path d="M470,450 Q430,390 520,360 Q610,330 566,296" fill="none" stroke="#f6c200" stroke-width="64" stroke-linecap="round"/>
  ${[0,1,2,3,4].map(k=>`<path d="M${400+k*18},${430-k*18} l22,-6 M${470+k*10},${376-k*14} l22,-6" stroke="#c98a00" stroke-width="3" opacity=".7"/>`).join('')}
  ${[0,1,2,3].map(k=>grp(`translate(${20+k*34} ${380+k*6})`,`<path d="M0,0 L0,-50 M0,-30 Q-20,-40 -26,-60 M0,-34 Q20,-44 26,-64" stroke="#2f8f6a" stroke-width="6" fill="none" stroke-linecap="round"/>${C(-26,-62,10,['#e8473b','#f6c84c','#ff8fb1','#9b6ad8'][k],2.6)}${C(26,-66,10,['#f6c84c','#ff8fb1','#9b6ad8','#e8473b'][k],2.6)}`)).join('')}
  ${place('scarecrow',250,424,1.12)}${place('lion',590,432,.98,true)}${place('dorothy',385,430,1.14)}${place('toto',470,436,1.2)}
  ${star(70,70,9)}${star(300,52,7)}${finish(i)}`},
 peterpan(){const i=++UID;
  return `<defs>${defsCommon(i)}<linearGradient id="sk${i}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#14183f"/><stop offset=".65" stop-color="#2d3f8f"/><stop offset="1" stop-color="#6a6fc8"/></linearGradient><radialGradient id="mn${i}"><stop offset="0" stop-color="#fff9d8"/><stop offset=".55" stop-color="#ffe98a"/><stop offset="1" stop-color="#ffe98a" stop-opacity="0"/></radialGradient></defs>
  <rect width="800" height="450" fill="url(#sk${i})"/>
  <circle cx="610" cy="130" r="150" fill="url(#mn${i})"/><circle cx="610" cy="130" r="74" fill="#fff4b8" ${stk(3)}/>${C(588,112,14,'#f2dc86',0)}${C(632,150,10,'#f2dc86',0)}${C(600,156,7,'#f2dc86',0)}
  ${[...Array(26)].map((_,k)=>star((k*97)%790+10,(k*53)%240+10,k%4===0?8:4)).join('')}
  <g transform="translate(120 330)">${R(-22,-250,44,250,'#1b2252',0,3)}${P('M-30,-250 L0,-300 L30,-250Z','#1b2252')}${C(0,-206,17,'#f6e8a8',2.8)}<path d="M0,-206 L0,-218 M0,-206 L8,-206" stroke="${INK}" stroke-width="2.4"/>${R(-44,-130,22,130,'#1b2252',0,3)}${R(22,-110,26,110,'#1b2252',0,3)}</g>
  <path d="M0,370 Q120,350 240,372 Q400,392 560,366 Q700,346 800,372 L800,450 L0,450Z" fill="#161b44" ${stk(3)}/>
  ${[0,1,2,3,4,5,6].map(k=>`<g transform="translate(${40+k*118} ${372+(k%2)*10})">${R(-14,-26,28,26,'#1f2a66',0,2.4)}${P('M-18,-26 L0,-44 L18,-26Z','#1f2a66',2.4)}${R(-4,-18,8,10,'#ffd35c',0,0)}</g>`).join('')}
  ${cloud(260,290,1.1,'#cdd4ff')}${cloud(690,300,1.2,'#cdd4ff')}${cloud(500,330,.9,'#dfe4ff')}
  <g transform="translate(676 318) scale(.55)"><path d="M-110,0 Q-90,-30 -50,-34 L60,-34 Q96,-30 116,0Z" fill="#7a4a2a" ${stk(3)}/><path d="M0,-34 L0,-170" stroke="${INK}" stroke-width="5"/>${P('M0,-166 Q70,-130 60,-50 L0,-40Z','#f4f0e8')}${P('M-4,-150 Q-64,-110 -54,-50 L-4,-42Z','#e9e2d2')}${P('M0,-170 L30,-160 L0,-150Z','#e8473b',2.4)}</g>
  ${place('wendy',200,422,1.02)}
  <g transform="translate(470 318) rotate(-14) scale(1.02)">${CH.peter()}</g>
  <g transform="translate(318 168)"><circle r="46" fill="#aff7c0" opacity=".28"/>${star(-36,-30,6,'#d9ffe6')}${star(42,20,5,'#d9ffe6')}<g transform="scale(1.6)">${CH.tinker()}</g></g>
  ${finish(i)}`},
 toystory(){const i=++UID;
  return `<defs>${defsCommon(i)}<linearGradient id="sk${i}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5eb4ee"/><stop offset="1" stop-color="#bfe4fb"/></linearGradient></defs>
  <rect width="800" height="450" fill="url(#sk${i})"/>
  ${[[80,70,.9],[260,120,1.1],[470,60,.9],[660,110,1.2],[160,220,.8],[560,230,.9]].map(([x,y,s])=>cloud(x,y,s,'#fff')).join('')}
  <rect y="352" width="800" height="98" fill="#b8854f"/><path d="M0,352 L800,352" stroke="${INK}" stroke-width="3"/>${[0,1,2,3,4,5,6,7].map(k=>`<path d="M${k*110},352 L${k*110-40},450" stroke="#8a5d30" stroke-width="3" opacity=".6"/>`).join('')}
  <g transform="translate(70 352)">${R(0,-90,78,90,'#e8473b',6)}${R(86,-72,64,72,'#f2c63d',6)}${R(24,-160,60,70,'#3e8fd8',6)}<text x="39" y="-52" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="32" fill="#fff">A</text><text x="118" y="-26" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="30" fill="${INK}">B</text><text x="54" y="-110" text-anchor="middle" font-family="Georgia,serif" font-weight="700" font-size="32" fill="#fff">C</text></g>
  <g transform="translate(690 352)">${E(0,-30,44,16,'#e8473b',3)}${R(-44,-30,88,30,'#e8473b',0,3)}${C(-26,-2,16,'#2b1d3a',3)}${C(26,-2,16,'#2b1d3a',3)}${C(-26,-2,6,'#c9c9d4',0)}${C(26,-2,6,'#c9c9d4',0)}${R(-14,-66,28,36,'#f2c63d',4)}</g>
  ${star(400,38,10,'#ffe27a')}${star(720,40,8,'#ffe27a')}${star(60,160,7,'#ffe27a')}
  ${place('woody',290,418,1.2)}${place('buzz',510,418,1.2,true)}${finish(i)}`}
};
const KEY={9801:'paddington',7009801:'alice',70001:'oz',7070001:'peterpan',30001:'toystory'};
const keyOf=x=>{if(!x)return null;const n=typeof x==='object'?(x.n!=null?x.n:(x.e&&x.e.n)):x;return KEY[n]||null};
const VB={paddington:'250 26 480 424',alice:'190 26 480 424',oz:'180 26 480 424',peterpan:'130 26 480 424',toystory:'160 26 480 424'};
const svg=(k,cls)=>{const f=SCN[k];if(!f)return '';const vb=/sticker/.test(cls||'')?VB[k]:'0 0 800 450';return `<svg class="obra-svg ${cls||''}" viewBox="${vb}" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img">${f()}</svg>`};

/* troca a cena + personagens da capa pelo cartaz ilustrado */
function coverFix(sc,e){
  const k=keyOf(e);if(!k||!sc)return;
  const bk=sc.querySelector('.ps-stage-bk'),ch=sc.querySelector('.ps-chars');
  if(!bk)return;bk.innerHTML=svg(k,'obra-cover');if(ch)ch.style.display='none';sc.classList.add('has-obra');
}
window.PogObra={has:x=>!!keyOf(x),key:keyOf,svg:(x,cls)=>svg(keyOf(x),cls),coverFix};
})();
