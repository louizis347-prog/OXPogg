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
  if(o.extra)g+=o.extra;
  g+=C(0,-140,34,sk);
  if(o.hairStyle==='long'&&!o.bald)g+=P('M-35,-146 Q-31,-178 0,-176 Q31,-178 35,-146 Q14,-162 0,-160 Q-14,-162 -35,-146Z',hair);
  if(o.hairStyle==='braids')g+=P('M-35,-144 Q-32,-178 0,-177 Q32,-178 35,-144 Q12,-158 0,-156 Q-12,-158 -35,-144Z',hair);
  if(o.hairStyle==='short')g+=P('M-35,-144 Q-36,-180 0,-178 Q36,-180 35,-144 Q20,-166 6,-158 Q-10,-170 -35,-144Z',hair);
  if(o.band)g+=`<path d="M-36,-150 Q0,-184 36,-150" fill="none" stroke="${o.band}" stroke-width="7" stroke-linecap="round"/>`+P('M-36,-152 L-50,-162 L-48,-144Z M-36,-152 L-26,-164 L-24,-146Z',o.band,2.4);
  g+=eyes(0,-140,13)+blush(0,-128,22)+smile(0,-125,9);
  if(o.stache)g+=P('M-14,-131 Q-6,-136 0,-131 Q6,-136 14,-131 Q8,-126 0,-129 Q-8,-126 -14,-131Z',o.stache,2.2);
  if(o.whisk)g+=[-1,1].map(s=>P(`M${s*30},-148 Q${s*40},-126 ${s*26},-112 Q${s*24},-128 ${s*28},-146Z`,o.whisk,2)).join('');
  if(o.beard)g+=P('M-24,-124 Q0,-92 24,-124 Q16,-112 0,-110 Q-16,-112 -24,-124Z',o.beard,2.4);
  if(o.hat==='cowboy')g+=P('M-52,-168 Q-30,-176 -20,-182 Q0,-212 20,-182 Q30,-176 52,-168 Q30,-158 0,-160 Q-30,-158 -52,-168Z',o.hatColor||'#8a5a2b');
  if(o.hat==='cap')g+=P('M-34,-166 Q-6,-196 38,-168 Q8,-164 -34,-166Z',o.hatColor||'#2f9d5b')+P('M14,-176 Q40,-212 52,-196 Q40,-190 24,-172Z','#e8473b',2.4);
  if(o.hat==='top')g+=R(-30,-196,60,40,'#2b2538',6,3)+E(0,-158,44,9,'#2b2538',3)+R(-30,-170,60,9,'#d9503f',0,2.4);
  if(o.hat==='turban')g+=P('M-36,-156 Q-34,-196 0,-196 Q34,-196 36,-156 Q0,-170 -36,-156Z',o.hatColor||'#e8473b')+P('M-34,-166 Q0,-182 34,-166','none',2.4)+C(0,-174,5,'#f6c84c',2);
  if(o.hat==='veil')g+=`<path d="M-34,-150 Q0,-186 34,-150" fill="none" stroke="#f6c84c" stroke-width="6" stroke-linecap="round"/>`+C(0,-166,6,'#e8473b',2.2)+P('M-30,-120 Q0,-100 30,-120 L24,-98 Q0,-88 -24,-98Z','rgba(255,255,255,.55)',2);
  if(o.hat==='bonnet')g+=P('M-38,-156 Q-30,-190 0,-190 Q30,-190 38,-156 Q20,-148 0,-150 Q-20,-148 -38,-156Z',o.hatColor||'#f6d35c')+P('M-40,-158 Q0,-146 40,-158 L36,-150 Q0,-140 -36,-150Z',o.hatColor||'#f6d35c',2.4);
  if(o.hat==='wimple')g+=P('M-40,-130 Q-42,-190 0,-190 Q42,-190 40,-130 Q40,-98 24,-90 L-24,-90 Q-40,-98 -40,-130Z','#1f1f2e')+C(0,-138,28,sk,2.6)+P('M-30,-120 Q0,-92 30,-120 L26,-96 Q0,-84 -26,-96Z','#fff',2.4)+eyes(0,-140,10,4)+smile(0,-126,7);
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
 snowwhite(){return kid({hair:'#caa46a',hairStyle:'braids',ribbon:'#fff',top:'#f4f4fa',dress:true,legs:'#fff',shoe:'#3a3550',arms:'out',extra:C(-34,-70,9,'#fff',2.4)+C(-34,-70,4,'#f6d35c',0)})},
 rosered(){return kid({hair:'#3a2218',hairStyle:'braids',ribbon:'#e8473b',top:'#d9304a',dress:true,legs:'#fff',shoe:'#3a3550',arms:'out',extra:C(34,-70,9,'#e8473b',2.4)+C(34,-70,4,'#f6d35c',0)})},
 bear(){let g=shadow(48);
  g+=L(-18,-44,-20,-8,24,'#7a4a2a')+L(18,-44,20,-8,24,'#7a4a2a')+E(-22,-6,20,9,'#5a3418',2.8)+E(22,-6,20,9,'#5a3418',2.8);
  g+=E(0,-84,50,50,'#8a5a32')+E(0,-70,28,30,'#d9a15a',0);
  g+=L(-40,-96,-58,-60,18,'#8a5a32')+L(40,-96,58,-60,18,'#8a5a32');
  g+=[-1,1].map(s=>C(s*34,-146,14,'#8a5a32')+C(s*34,-146,7,'#d9a15a',0)).join('')+C(0,-128,40,'#8a5a32')+E(0,-118,20,15,'#e8c58f')+P('M-7,-124 Q0,-130 7,-124 Q4,-117 0,-117 Q-4,-117 -7,-124Z','#1b1224',2)+eyes(0,-136,15,4.4)+smile(0,-108,6);
  return g},
 fogg(){return kid({skin:'#f2c9a4',hair:'#a6a6ae',hairStyle:'short',top:'#3a3550',bot:'#3a3550',hat:'top',stache:'#a6a6ae',whisk:'#a6a6ae',shoe:'#1b1224',arms:'down',extra:P('M-9,-114 L0,-96 L9,-114Z','#fff',2)+`<path d="M-14,-96 Q0,-88 14,-96" fill="none" stroke="#f6c84c" stroke-width="3"/>`+C(14,-96,4,'#f6c84c',1.6)})},
 passepartout(){return kid({skin:'#f2c9a4',hair:'#2b1d1d',hairStyle:'short',top:'#d9503f',bot:'#4a6fa5',hat:'cap',hatColor:'#3a3550',stache:'#2b1d1d',shoe:'#5a3418',arms:'wave',extra:[0,1,2].map(i=>`<path d="M-24,${-104+i*16} L24,${-104+i*16}" stroke="#fff" stroke-width="4" opacity=".7"/>`).join('')})},
 kim(){return kid({skin:'#c98d5a',hair:'#1f1818',hairStyle:'short',top:'#f0e0b8',bot:'#c4a46a',shoe:'#c98d5a',arms:'point'})},
 lama(){return kid({skin:'#d9a066',bald:true,beard:'#d8d8d8',top:'#8e2a2a',dress:true,legs:'#8e2a2a',shoe:'#6b3f22',arms:'down',sleeve:'#e0a030',extra:`<path d="M-22,-110 Q0,-84 22,-110" fill="none" stroke="#e0a030" stroke-width="6"/>`+[...Array(7)].map((_,i)=>C(-18+i*6,-100+Math.sin(i/6*Math.PI)*14,3,'#5a3418',1.4)).join('')})},
 scheherazade(){return kid({skin:'#e0b080',hair:'#1f1830',hairStyle:'long',top:'#7b4cc2',dress:true,legs:'#e0b080',shoe:'#e0b080',hat:'veil',arms:'out',sleeve:'#f6c84c',extra:`<path d="M-22,-76 L22,-76" stroke="#f6c84c" stroke-width="5"/>`+P('M-22,-112 L22,-112 L26,-100 L-26,-100Z','#f6c84c',2.4)})},
 madeline(){return kid({hair:'#e0602a',hairStyle:'short',top:'#2e66c8',dress:true,legs:'#fff',shoe:'#2b1d3a',hat:'bonnet',hatColor:'#f6d35c',arms:'up'})},
 clavel(){return kid({skin:'#f2c9a4',top:'#1f1f2e',dress:true,legs:'#1f1f2e',shoe:'#111',hat:'wimple',arms:'down',sleeve:'#1f1f2e'})},
 lamp(){let g='';g+=P('M-30,-14 Q-34,-30 -10,-34 L10,-34 Q34,-30 30,-14 Q0,-4 -30,-14Z','#f2c63d')+P('M-10,-34 Q0,-46 10,-34','none',3)+P('M30,-22 Q50,-30 46,-44 Q36,-36 30,-30Z','#f2c63d')+P('M-30,-20 L-46,-30 L-34,-14Z','#f2c63d')+`<path d="M0,-46 Q-14,-70 6,-90 Q26,-110 0,-130" fill="none" stroke="#b58cf0" stroke-width="10" stroke-linecap="round" opacity=".8"/>`;return g}
 ,
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
 ,snow(){const i=++UID;
  return `<defs>${defsCommon(i)}<linearGradient id="sk${i}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#17234f"/><stop offset=".7" stop-color="#2f5a9a"/><stop offset="1" stop-color="#9cc6e8"/></linearGradient><radialGradient id="gl${i}"><stop offset="0" stop-color="#ffd58a" stop-opacity=".9"/><stop offset="1" stop-color="#ffd58a" stop-opacity="0"/></radialGradient></defs>
  <rect width="800" height="450" fill="url(#sk${i})"/>${[...Array(30)].map((_,k)=>star((k*83)%790+8,(k*47)%200+8,k%4===0?6:3)).join('')}
  ${[0,1,2,3,4,5,6].map(k=>grp(`translate(${30+k*120} ${290+(k%2)*20}) scale(${1+(k%3)*.15})`,`<path d="M0,0 L-34,70 L34,70Z M0,-34 L-28,30 L28,30Z M0,-66 L-22,-6 L22,-6Z" fill="#245a4a" ${stk(2.6)}/><path d="M-12,-34 L0,-66 L12,-34Z M-18,10 L0,-34 L18,10Z" fill="#fff" opacity=".85"/>`)).join('')}
  <g transform="translate(560 252)">${R(-90,0,180,110,'#8a5a32',4)}${P('M-110,2 L0,-80 L110,2Z','#f4f4fa')}${P('M-100,2 L0,-72 L100,2Z','#a8502f',2.6,'opacity=".0"')}${R(-70,26,52,48,'#ffd58a',3)}<circle cx="-44" cy="50" r="80" fill="url(#gl${i})" opacity=".55"/>${R(20,34,44,76,'#5a3418',4)}${R(40,-90,24,50,'#6b4a2a',3)}${P('M36,-92 L68,-92 L64,-100 L40,-100Z','#f4f4fa')}<path d="M52,-104 Q40,-130 58,-150 Q74,-170 52,-190" stroke="#d9d9ea" stroke-width="9" fill="none" stroke-linecap="round" opacity=".7"/></g>
  <path d="M0,380 Q200,360 400,382 Q600,402 800,372 L800,450 L0,450Z" fill="#eef4fb" ${stk(3)}/><path d="M0,420 Q300,404 600,424 Q720,432 800,418 L800,450 L0,450Z" fill="#dce8f5"/>
  ${[[70,360],[330,372],[740,366]].map(([x,y],k)=>grp(`translate(${x} ${y})`,`<path d="M0,0 L0,-40" stroke="#2f8f6a" stroke-width="5"/>${[[-14,-38],[12,-50],[-4,-64],[16,-30]].map(([dx,dy],j)=>C(dx,dy,10,j%2?'#e8473b':'#fff',2.6)+C(dx,dy,3.4,'#f6c84c',0)).join('')}`)).join('')}
  ${place('bear',650,438,.84,true)}${place('snowwhite',230,420,1.08)}${place('rosered',370,424,1.08,true)}
  <g opacity=".9">${[...Array(46)].map((_,k)=>C((k*61)%800,(k*37)%440,k%3?2:3,'#fff',0)).join('')}</g>${finish(i)}`}
 ,around(){const i=++UID;
  return `<defs>${defsCommon(i)}<linearGradient id="sk${i}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5a3f9a"/><stop offset=".55" stop-color="#e8708a"/><stop offset="1" stop-color="#ffd58a"/></linearGradient></defs>
  <rect width="800" height="450" fill="url(#sk${i})"/>${C(210,250,70,'#fff1b0',0,'opacity=".8"')}
  <g transform="translate(110 130)"><circle r="62" fill="#fff8e6" ${stk(4)}/>${[...Array(12)].map((_,k)=>{const a=k/12*Math.PI*2;return `<path d="M${Math.cos(a)*50},${Math.sin(a)*50} L${Math.cos(a)*56},${Math.sin(a)*56}" stroke="${INK}" stroke-width="3"/>`}).join('')}<path d="M0,0 L0,-40 M0,0 L28,16" stroke="${INK}" stroke-width="5" stroke-linecap="round"/><text y="26" text-anchor="middle" font-family="Georgia,serif" font-weight="900" font-size="22" fill="#d9503f">80</text></g>
  <g transform="translate(650 110) scale(.78)"><path d="M-70,0 Q-72,-90 0,-96 Q72,-90 70,0 Q40,50 0,60 Q-40,50 -70,0Z" fill="#e8473b" ${stk(3.4)}/>${[-46,-18,18,46].map((x,k)=>`<path d="M${x*0.1},-94 Q${x*1.35},-10 ${x*.5},58" fill="none" stroke="${k%2?'#f6d35c':'#fff'}" stroke-width="12" opacity=".9"/>`).join('')}<path d="M-26,56 L-20,96 M26,56 L20,96" stroke="${INK}" stroke-width="3"/>${R(-30,92,60,36,'#a8702f',6)}<path d="M-30,72 Q0,86 30,72" fill="none" stroke="#fff" stroke-width="0"/></g>
  <path d="M0,300 L180,230 L340,300Z" fill="#c4944a" ${stk(3)}/><path d="M250,300 L400,210 L560,300Z" fill="#d9a15a" ${stk(3)}/><path d="M400,210 L338,256 L400,300Z" fill="rgba(0,0,0,.14)"/>
  <rect y="300" width="800" height="150" fill="#3a6aa8"/><path d="M0,300 L800,300" stroke="${INK}" stroke-width="3"/>${[0,1,2,3,4,5].map(k=>`<path d="M${k*150},${330+k%3*26} q20,-8 40,0 q20,8 40,0" stroke="#bfe0ff" stroke-width="3" fill="none" opacity=".7"/>`).join('')}
  <g transform="translate(610 340)">${P('M-130,0 L130,0 L100,48 L-100,48Z','#2b3a5c')}${R(-60,-46,120,46,'#f4f4f8',4)}${R(-10,-84,32,38,'#d9503f',4)}${R(-4,-104,20,22,'#2b3a5c',3)}${[-40,-16,8,32].map(x=>C(x,-24,7,'#7ec8f2',2.4)).join('')}<path d="M10,-110 Q-10,-136 14,-156 Q40,-176 8,-200" stroke="#d9d9ea" stroke-width="12" fill="none" stroke-linecap="round" opacity=".65"/></g>
  <rect y="388" width="800" height="62" fill="#8a6a4a"/><path d="M0,388 L800,388" stroke="${INK}" stroke-width="3"/>${[...Array(14)].map((_,k)=>`<path d="M${k*60},388 L${k*60-10},450" stroke="#5a3f28" stroke-width="3" opacity=".6"/>`).join('')}
  <g transform="translate(510 410)">${R(-34,-44,68,44,'#a8502f',6)}${R(-34,-30,68,6,'#f6c84c',0)}${R(-6,-48,12,6,'#5a3418',2,2)}</g>
  <g transform="translate(150 392)"><circle cx="0" cy="-66" r="46" fill="#3e8fd8" ${stk(3.2)}/><path d="M-46,-66 Q0,-86 46,-66 M-46,-66 Q0,-46 46,-66 M0,-112 Q-22,-66 0,-20 M0,-112 Q22,-66 0,-20" fill="none" stroke="#7bd26b" stroke-width="6"/>${R(-6,-20,12,16,'#7a4a22',2,2.4)}${E(0,-2,22,6,'#7a4a22',2.6)}</g>
  ${place('fogg',300,418,1.1)}${place('passepartout',430,424,1.04,true)}${finish(i)}`}
 ,kim(){const i=++UID;
  return `<defs>${defsCommon(i)}<linearGradient id="sk${i}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f08a4a"/><stop offset=".6" stop-color="#f8c878"/><stop offset="1" stop-color="#fde9b4"/></linearGradient></defs>
  <rect width="800" height="450" fill="url(#sk${i})"/>${C(640,130,66,'#fff2c0',0)}${C(640,130,48,'#fff9e0',0)}
  <g transform="translate(520 300)">${R(-20,-40,40,40,'#fff',0,3)}${P('M-70,-40 Q-70,-150 0,-170 Q70,-150 70,-40Z','#fff')}${P('M-12,-170 L0,-200 L12,-170Z','#f6c84c',2.6)}${R(-100,-120,28,120,'#fff',4)}${R(72,-120,28,120,'#fff',4)}${P('M-100,-120 L-86,-146 L-72,-120Z M72,-120 L86,-146 L100,-120Z','#e8473b',2.6)}${P('M-34,0 L-34,-66 Q0,-96 34,-66 L34,0Z','#e8c58f')}${[...Array(6)].map((_,k)=>R(-120+k*40,0,0,0,'#fff',0,0)).join('')}</g>
  <g transform="translate(120 330)">${R(-14,-170,28,170,'#7a4a2a',4)}${[[-70,-170,80],[0,-210,100],[74,-170,80],[-40,-130,60],[44,-130,60]].map(([x,y,r],k)=>C(x,y,r,['#3f9457','#4ea866','#3f9457','#58b872','#4ea866'][k],3)).join('')}${[[-50,-100],[50,-84]].map(([x,y])=>`<path d="M${x},${y} L${x},0" stroke="#7a4a2a" stroke-width="8"/>`).join('')}</g>
  <path d="M0,340 Q300,320 600,350 Q720,362 800,346 L800,450 L0,450Z" fill="#d9a15a" ${stk(3)}/><path d="M0,400 Q300,384 600,406 Q720,412 800,400 L800,450 L0,450Z" fill="#c4883f"/>
  <g>${[...Array(12)].map((_,k)=>`<path d="M${k*80},60 Q${k*80+40},84 ${k*80+80},60" fill="none" stroke="${INK}" stroke-width="2.4"/>${P(`M${k*80+10},66 L${k*80+34},72 L${k*80+22},96Z`,['#e8473b','#f6c84c','#3fb86b','#3e8fd8','#fff'][k%5],2)}`).join('')}</g>
  ${place('kim',300,420,1.1)}${place('lama',480,424,1.1,true)}${finish(i)}`}
 ,nights(){const i=++UID;
  return `<defs>${defsCommon(i)}<linearGradient id="sk${i}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#150f3a"/><stop offset=".7" stop-color="#3a2a7a"/><stop offset="1" stop-color="#8a5ab8"/></linearGradient></defs>
  <rect width="800" height="450" fill="url(#sk${i})"/>${[...Array(40)].map((_,k)=>star((k*89)%790+8,(k*43)%260+8,k%5===0?8:3)).join('')}
  <g transform="translate(120 110)"><circle r="64" fill="#fff4b8" ${stk(3)}/><circle cx="26" cy="-8" r="58" fill="#3a2a7a"/></g>
  ${[[40,300,70,150],[150,300,60,200],[280,300,80,120],[420,300,56,210],[560,300,84,140],[700,300,60,190]].map(([x,y,w,h],k)=>grp(`translate(${x} ${y})`,`${R(0,-h,w,h,'#2a1f5e',0,3)}${P(`M${-4},${-h} Q${w/2},${-h-w*.9} ${w+4},${-h}Z`,k%2?'#4a3a9a':'#3a2a7a')}${R(w/2-2,-h-w*.45-22,4,22,'#f6c84c',0,2)}${[0,1,2].map(j=>R(10+j*(w/3),-h+24+(k%3)*10,10,16,'#ffd35c',2,0)).join('')}`)).join('')}
  <rect y="300" width="800" height="150" fill="#1b1445"/><path d="M0,300 L800,300" stroke="${INK}" stroke-width="3"/>
  <g transform="translate(430 340) rotate(-5)">${P('M-170,0 Q0,16 170,0 L160,30 Q0,48 -160,30Z','#c0392b')}${P('M-160,6 Q0,22 160,6','none',0)}${[...Array(9)].map((_,k)=>`<path d="M${-140+k*35},12 l8,14 l8,-14" stroke="#f6c84c" stroke-width="3" fill="none"/>`).join('')}${[...Array(22)].map((_,k)=>`<path d="M${-166+k*15},${28+Math.sin(k)*2} L${-166+k*15},${44}" stroke="#f6c84c" stroke-width="3" stroke-linecap="round"/>`).join('')}</g>
  <g transform="translate(560 346)">${CH.lamp()}</g>${place('scheherazade',330,350,1.1)}
  <path d="M120,140 Q220,100 300,150" fill="none" stroke="#b58cf0" stroke-width="3" opacity=".0"/>${finish(i)}`}
 ,madeline(){const i=++UID;
  return `<defs>${defsCommon(i)}<linearGradient id="sk${i}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9ccdf0"/><stop offset=".7" stop-color="#f8d4d8"/><stop offset="1" stop-color="#fdecc8"/></linearGradient></defs>
  <rect width="800" height="450" fill="url(#sk${i})"/>${cloud(120,90,.9)}${cloud(660,70,1)}${cloud(420,60,.7)}
  ${[0,1,2,3,4,5].map(k=>grp(`translate(${k*140-20} 300)`,`${R(0,-130,124,130,k%2?'#f2e2c0':'#e8d4a8',0,3)}${P(`M-6,-130 L22,-170 L102,-170 L130,-130Z`,'#6a7aa0')}${[0,1].map(j=>R(18+j*50,-104,26,38,'#8fb8e0',2,2.4)+R(18+j*50,-50,26,34,'#8fb8e0',2,2.4)).join('')}`)).join('')}
  <g transform="translate(560 300)">${P('M-40,0 L-18,-200 L-6,-200 L-2,-290 L2,-290 L6,-200 L18,-200 L40,0Z','#5a4a6a')}${P('M-30,-60 L30,-60 M-24,-110 L24,-110 M-14,-170 L14,-170','none',3)}${R(-44,-62,88,10,'#5a4a6a',2,3)}${R(-24,-114,48,8,'#5a4a6a',2,3)}<path d="M-18,0 Q0,-50 18,0" fill="#f8d4d8" stroke="${INK}" stroke-width="3"/></g>
  <rect y="388" width="800" height="62" fill="#b8a58a"/><path d="M0,388 L800,388" stroke="${INK}" stroke-width="3"/>${[...Array(40)].map((_,k)=>E((k*53)%800,400+(k*17)%46,12,5,k%2?'#a8957a':'#c4b198',0)).join('')}
  ${[0,1].map(r=>[0,1,2,3,4,5].map(k=>grp(`translate(${520-k*58-r*14} ${410+r*14}) scale(.34)`,`${L(-12,-52,-12,-8,14,'#fff')}${L(12,-52,12,-8,14,'#fff')}${E(-14,-4,18,8,'#2b1d3a',3)}${E(14,-4,18,8,'#2b1d3a',3)}${P('M-34,-124 L34,-124 L40,-48 Q0,-38 -40,-48Z','#2e66c8')}${L(-34,-116,-44,-70,12,'#2e66c8')}${L(34,-116,44,-70,12,'#2e66c8')}${C(0,-150,34,'#ffd7b5')}${P('M-38,-158 Q-30,-196 0,-196 Q30,-196 38,-158 Q20,-150 0,-152 Q-20,-150 -38,-158Z','#f6d35c')}${eyes(0,-148,13)}${smile(0,-130,9)}`)).join('')).join('')}
  ${place('clavel',590,430,.9,true)}${place('madeline',150,424,1.0)}${finish(i)}`}

};
const KEY={9801:'paddington',7009801:'alice',70001:'oz',7070001:'peterpan',30001:'toystory',7030001:'snow',9802:'around',7009802:'kim',30002:'nights',7030002:'madeline'};
const keyOf=x=>{if(!x)return null;const n=typeof x==='object'?(x.n!=null?x.n:(x.e&&x.e.n)):x;return KEY[n]||null};
const VB={paddington:'250 26 480 424',alice:'190 26 480 424',oz:'180 26 480 424',peterpan:'130 26 480 424',toystory:'160 26 480 424',snow:'130 26 480 424',around:'200 26 480 424',kim:'200 26 480 424',nights:'180 26 480 424',madeline:'60 26 480 424'};
const svg=(k,cls)=>{const f=SCN[k];if(!f)return '';const vb=/sticker/.test(cls||'')?VB[k]:'0 0 800 450';return `<svg class="obra-svg ${cls||''}" viewBox="${vb}" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img">${f()}</svg>`};

/* troca a cena + personagens da capa pelo cartaz ilustrado */
function coverFix(sc,e){
  const k=keyOf(e);if(!k||!sc)return;
  const bk=sc.querySelector('.ps-stage-bk'),ch=sc.querySelector('.ps-chars');
  if(!bk)return;bk.innerHTML=svg(k,'obra-cover');if(ch)ch.style.display='none';sc.classList.add('has-obra');
}
window.PogObra={has:x=>!!keyOf(x),key:keyOf,svg:(x,cls)=>svg(keyOf(x),cls),coverFix};
})();
