/* [obra-ficha] Capa da obra a partir de uma FICHA (js/fichas-*.js → window.PogFichas[n]).
   ficha = { scene, tod, cast:[{p:{…pessoa}|a:'bicho', c, c2, s, x, flip}], prop:{id,c,at,s}, decor:[...], accent }
   Sem ficha, nada acontece: o gerador antigo (js/obra-art.js) continua valendo. As peças estão em js/obra-ficha-lib.js. */
(function(){
'use strict';
const Lb=window.PogFichaLib;if(!Lb)return;
const {INK,stk,P,E,C,R,L,G,star5,mix,dark,light}=Lb.prim;
let UID=0;
const hash=s=>{let h=2166136261;s=String(s);for(let i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619)}return h>>>0};
const rngOf=seed=>{let a=(seed>>>0)||1;return()=>{a^=a<<13;a>>>=0;a^=a>>>17;a^=a<<5;a>>>=0;return a/4294967296}};

/* ---------- hora do dia ---------- */
const TOD={
 day:{s1:'#7fcff0',s2:'#eaf8ff',g1:'#7cc36a',g2:'#5aa656',far:'#a9d8b0',glow:'#fff7c8',stars:0},
 dawn:{s1:'#f1a7c0',s2:'#fde9c4',g1:'#8fbf78',g2:'#6aa062',far:'#d9b7c6',glow:'#ffe2a8',stars:0},
 dusk:{s1:'#5a4a9a',s2:'#f6a56a',g1:'#6b9a5c',g2:'#4e7a4c',far:'#9a7aa8',glow:'#ffd08a',stars:1},
 night:{s1:'#141e4c',s2:'#46549a',g1:'#35557a',g2:'#274260',far:'#2c3a78',glow:'#fff3b8',stars:2},
 indoor:{s1:'#f3dcb8',s2:'#f8ead0',g1:'#b98a5a',g2:'#9a6e44',far:'#e8cfa2',glow:'#fff3b8',stars:0}
};
const tint=(c,t,acc)=>acc?mix(c,acc,.22):c;

/* ---------- peças de cenário ---------- */
const cloud=(x,y,s,f)=>G(`translate(${x} ${y}) scale(${s})`,`<path d="M-60,0 Q-70,-30 -36,-34 Q-24,-60 6,-48 Q36,-62 50,-34 Q80,-30 66,0Z" fill="${f||'#fff'}" ${stk(2.6)}/>`);
const hill=(x,y,w,h,f)=>`<path d="M${x-w},${y} Q${x-w*.4},${y-h} ${x},${y-h} Q${x+w*.4},${y-h} ${x+w},${y}Z" fill="${f}" ${stk(3)}/>`;
const treeRound=(x,y,s,f,tr)=>G(`translate(${x} ${y}) scale(${s})`,R(-8,-50,16,52,tr||'#8a5a2b',3)+C(0,-84,44,f)+C(-28,-62,28,f)+C(28,-62,28,f)+C(-10,-100,14,light(f,.18),0));
const treePine=(x,y,s,f)=>G(`translate(${x} ${y}) scale(${s})`,R(-7,-30,14,32,'#6a3f22',3)+P('M-44,-26 L0,-82 L44,-26Z',f)+P('M-36,-58 L0,-112 L36,-58Z',light(f,.1))+P('M-26,-92 L0,-138 L26,-92Z',light(f,.2)));
const house=(x,y,s,wall,roof)=>G(`translate(${x} ${y}) scale(${s})`,R(-40,-56,80,56,wall,3)+P('M-50,-56 L0,-100 L50,-56Z',roof)+R(-9,-34,18,34,'#8a5a2b',3,2.6)+R(-32,-44,16,16,'#bfe6f6',2,2.4)+R(16,-44,16,16,'#bfe6f6',2,2.4));
const tower=(x,y,s,wall,roof)=>G(`translate(${x} ${y}) scale(${s})`,R(-24,-120,48,120,wall,3)+P('M-32,-120 L0,-176 L32,-120Z',roof)+R(-6,-92,12,24,'#2b2538',6,2)+R(-6,-50,12,24,'#2b2538',6,2));
const castleFar=(x,y,s,wall,roof)=>G(`translate(${x} ${y}) scale(${s})`,R(-90,-70,180,70,wall,3)+[-1,1].map(k=>tower(k*80,0,.9,wall,roof)).join('')+tower(0,-20,1.1,wall,roof)+R(-14,-34,28,34,'#6a3f22',14,2.6));
const flower=(x,y,s,c)=>G(`translate(${x} ${y}) scale(${s})`,L(0,0,0,-34,3,'#4fae6a')+[0,72,144,216,288].map(a=>E(Math.cos(a*Math.PI/180)*8,-38+Math.sin(a*Math.PI/180)*8,6,6,c,1.4)).join('')+C(0,-38,4.4,'#f6c84c',1.2));
const tuft=(x,y,s)=>G(`translate(${x} ${y}) scale(${s||1})`,`<path d="M0,0 l-6,-20 l10,14 l4,-22 l6,22 l10,-12 l-4,18" fill="none" ${stk(2.6)}/>`);
const mush=(x,y,s,c)=>G(`translate(${x} ${y}) scale(${s})`,R(-6,-4,12,24,'#f7e7c4',5,2.4)+P('M-26,-2 Q-26,-30 0,-30 Q26,-30 26,-2Q0,6 -26,-2Z',c,2.6)+[[-10,-16],[6,-20],[14,-10]].map(p=>C(p[0],p[1],3.6,'#fff',0)).join(''));
const sparkle=(x,y,s)=>`<path d="M${x} ${y-s}Q${x+s*.15} ${y-s*.15} ${x+s} ${y}Q${x+s*.15} ${y+s*.15} ${x} ${y+s}Q${x-s*.15} ${y+s*.15} ${x-s} ${y}Q${x-s*.15} ${y-s*.15} ${x} ${y-s}Z" fill="#fff6c8" opacity=".95"/>`;
const butterfly=(x,y,c)=>G(`translate(${x} ${y})`,P('M0 0Q-22 -26 -30 -4Q-26 16 0 6Z',c,2.4)+P('M0 0Q22 -26 30 -4Q26 16 0 6Z',c,2.4)+L(0,-4,0,10,3,INK));
const balloonD=(x,y,c)=>G(`translate(${x} ${y})`,P('M0 0Q-26 -4 -24 -38Q0 -64 24 -38Q26 -4 0 0z',c,3)+`<path d="M0 0 Q6 20 -4 40" fill="none" stroke="${INK}" stroke-width="2.4"/>`);
const bird=(x,y,s)=>`<path d="M${x-14*s} ${y} Q${x-7*s} ${y-9*s} ${x} ${y} Q${x+7*s} ${y-9*s} ${x+14*s} ${y}" fill="none" stroke="${INK}" stroke-width="3" stroke-linecap="round"/>`;
const heartD=(x,y,s,c)=>G(`translate(${x} ${y}) scale(${s})`,Lb.PROP.heart(c));
const leaf=(x,y,r,c)=>G(`translate(${x} ${y}) rotate(${r})`,P('M0,0 Q10,-14 0,-28 Q-10,-14 0,0Z',c,2));
const flake=(x,y,s)=>G(`translate(${x} ${y}) scale(${s})`,`<g stroke="#fff" stroke-width="3" stroke-linecap="round">`+[0,60,120].map(a=>`<line x1="0" y1="-9" x2="0" y2="9" transform="rotate(${a})"/>`).join('')+`</g>`);
const bubble=(x,y,r)=>`<circle cx="${x}" cy="${y}" r="${r}" fill="rgba(255,255,255,.28)" stroke="#fff" stroke-width="2" opacity=".9"/><circle cx="${x-r*.3}" cy="${y-r*.3}" r="${r*.22}" fill="#fff" opacity=".8"/>`;
const firefly=(x,y)=>`<circle cx="${x}" cy="${y}" r="7" fill="#fff6a8" opacity=".35"/><circle cx="${x}" cy="${y}" r="3" fill="#fff6a8"/>`;
const starD=(x,y,r)=>star5(x,y,r,'#fff6c8');
const wave=(y,c,amp,off)=>`<path d="M0,${y} `+[...Array(9)].map((_,i)=>`Q${i*100+50+off},${y+(i%2?amp:-amp)} ${i*100+100},${y}`).join(' ')+` L800,450 L0,450Z" fill="${c}" ${stk(3)}/>`;
const window_=(x,y,w,h,f)=>R(x,y,w,h,f||'#bfe6f6',3,3)+`<path d="M${x+w/2},${y} L${x+w/2},${y+h} M${x},${y+h/2} L${x+w},${y+h/2}" stroke="${INK}" stroke-width="2.4"/>`;

/* ---------- céu ---------- */
function sky(id,tod,acc){
  const T=TOD[tod]||TOD.day,s1=tint(T.s1,0,acc),s2=tint(T.s2,0,acc);let g=`<linearGradient id="sk${id}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${s1}"/><stop offset="1" stop-color="${s2}"/></linearGradient><rect width="800" height="450" fill="url(#sk${id})"/>`;
  if(T.stars)g+=[[60,40],[140,90],[250,30],[330,70],[470,36],[560,90],[690,44],[740,100],[400,110],[610,30]].map((p,i)=>starD(p[0],p[1],T.stars>1?5+i%3*2:3+i%2*2)).join('');
  return g;
}
/* sol/lua conforme o horário */
function lumin(tod,x){if(tod==='night')return G(`translate(${x||620} 70)`,Lb.PROP.moon());if(tod==='dusk')return G(`translate(${x||620} 150) scale(.8)`,`<circle r="46" fill="#ffd08a" opacity=".55"/><circle r="32" fill="#ffb86a"/>`);if(tod==='dawn')return G(`translate(${x||200} 160) scale(.8)`,`<circle r="46" fill="#ffe2a8" opacity=".6"/><circle r="32" fill="#ffd27a"/>`);if(tod==='day')return G(`translate(${x||640} 70) scale(.7)`,Lb.PROP.sun());return''}

/* ---------- cenários ---------- */
const SCENES={
 meadow(c){const T=c.T;return hill(160,330,320,150,T.far)+hill(620,340,360,130,mix(T.far,T.g1,.4))+`<rect y="330" width="800" height="120" fill="${T.g1}"/><path d="M0,330 L800,330" stroke="${INK}" stroke-width="3"/>`+treeRound(90,336,.8,T.g2)+treeRound(730,332,.7,T.g2)+c.ground(T.g2)},
 forest(c){const T=c.T;return [0,1,2,3,4,5,6].map(i=>treePine(60+i*125,300,.7+(i%3)*.12,mix(T.g2,'#1d4a38',.3))).join('')+`<rect y="320" width="800" height="130" fill="${T.g2}"/><path d="M0,320 L800,320" stroke="${INK}" stroke-width="3"/>`+treePine(40,350,1.1,mix(T.g1,'#1d4a38',.2))+treePine(760,350,1.1,mix(T.g1,'#1d4a38',.2))+c.ground(T.g1)},
 hills(c){const T=c.T;return hill(120,340,340,170,T.far)+hill(430,350,420,200,mix(T.far,T.g1,.35))+hill(740,340,300,150,T.far)+`<rect y="340" width="800" height="110" fill="${T.g1}"/><path d="M0,340 L800,340" stroke="${INK}" stroke-width="3"/>`+c.ground(T.g2)},
 castle(c){const T=c.T;return castleFar(400,330,1.6,'#d8cfe6','#8a5ac8')+hill(120,350,300,90,T.g1)+hill(700,350,320,100,T.g1)+`<rect y="340" width="800" height="110" fill="${T.g1}"/><path d="M0,340 L800,340" stroke="${INK}" stroke-width="3"/>`+treeRound(70,346,.7,T.g2)+treeRound(740,346,.7,T.g2)+c.ground(T.g2)},
 village(c){const T=c.T,roofs=['#d9503f','#4a7be0','#e8923a','#8a5ac8'];return hill(400,330,500,70,T.far)+[0,1,2,3,4].map(i=>house(70+i*165,336,.95,['#f2dca4','#f6e8c8','#e8c58f','#f3d6c8','#f2dca4'][i],roofs[(i+c.seed)%4])).join('')+`<rect y="336" width="800" height="114" fill="${mix(T.g1,'#c4a46a',.5)}"/><path d="M0,336 L800,336" stroke="${INK}" stroke-width="3"/>`+`<path d="M280,450 L360,336 L440,336 L520,450Z" fill="#e8d4a8" ${stk(3)}/>`+c.ground(T.g1)},
 farm(c){const T=c.T;return hill(150,330,320,110,T.far)+R(520,230,170,106,'#c4503f',4)+P('M506,230 L605,160 L704,230Z','#8a3a2a')+R(572,270,66,66,'#f6e8c8',2,3)+`<path d="M572,270 L638,336 M638,270 L572,336" stroke="${INK}" stroke-width="3"/>`+R(700,190,40,146,'#c9ccd6',6)+`<rect y="336" width="800" height="114" fill="${T.g1}"/><path d="M0,336 L800,336" stroke="${INK}" stroke-width="3"/>`+[0,1,2,3,4,5,6,7].map(i=>L(40+i*60,336,40+i*60,370,5,'#c4944a')).join('')+`<path d="M20,350 L500,350 M20,364 L500,364" stroke="${INK}" stroke-width="4"/>`+c.ground(T.g2)},
 seaside(c){const T=c.T;return `<rect y="250" width="800" height="200" fill="${mix('#4aa8d8',T.s1,.25)}"/>`+wave(262,mix('#7ed0ee',T.s2,.2),8,0)+wave(300,'#58b8e0',10,30)+`<path d="M0,370 Q400,330 800,370 L800,450 L0,450Z" fill="#f2dca4" ${stk(3)}/>`+c.ground('#e8c58f',1)},
 harbor(c){const T=c.T;return `<rect y="230" width="800" height="220" fill="#4a98c8"/>`+wave(244,'#7ac8e8',7,0)+[0,1,2].map(i=>G(`translate(${120+i*270} 250)`,Lb.PROP.boat(['#d9a15a','#e8473b','#4a7be0'][i]))).join('')+R(0,340,800,110,'#a8884a',0)+[...Array(14)].map((_,i)=>`<path d="M${i*60},340 L${i*60},450" stroke="${INK}" stroke-width="3"/>`).join('')+`<path d="M0,340 L800,340" stroke="${INK}" stroke-width="3.4"/>`+c.ground('#8a6a3a',1)},
 ship(c){return `<rect y="260" width="800" height="190" fill="#3f8ec0"/>`+wave(270,'#6ec2e6',9,0)+G('translate(400 330) scale(2.2)',Lb.PROP.ship())+wave(350,'#58b0da',10,30)+c.ground('#58b0da',1)},
 mountain(c){const T=c.T;return P('M-20,340 L170,120 L300,260 L400,170 L560,340Z',mix('#8f9ab8',T.far,.3),3)+P('M170,120 L205,168 L180,160 L160,176 L140,160Z','#fff',2.6)+P('M380,340 L580,100 L780,340Z',mix('#7b86a8',T.far,.3),3)+P('M580,100 L618,156 L592,148 L574,166 L554,148Z','#fff',2.6)+`<rect y="334" width="800" height="116" fill="${T.g2}"/><path d="M0,334 L800,334" stroke="${INK}" stroke-width="3"/>`+treePine(90,350,.8,mix(T.g2,'#1d4a38',.3))+treePine(720,350,.9,mix(T.g2,'#1d4a38',.3))+c.ground(T.g1)},
 snow(c){return hill(160,340,340,120,'#dff0fb')+hill(640,340,360,140,'#cfe6f6')+`<rect y="336" width="800" height="114" fill="#f4faff"/><path d="M0,336 L800,336" stroke="${INK}" stroke-width="3"/>`+treePine(80,352,.9,'#3f7a68')+treePine(730,352,.8,'#3f7a68')+[...Array(22)].map((_,i)=>flake((i*37+c.seed*13)%800,30+(i*53)%280,.8+(i%3)*.35)).join('')},
 desert(c){return `<path d="M0,330 Q200,290 400,330 T800,320 L800,450 L0,450Z" fill="#f2cf8a" ${stk(3)}/>`+`<path d="M-20,380 Q220,330 420,376 T820,370 L820,450 L-20,450Z" fill="#ecc27a" ${stk(3)}/>`+G('translate(120 340)',P('M-44,0 L0,-86 L44,0Z','#e8b96a',3)+P('M-24,0 L0,-46 L24,0Z','#d9a15a',0))+G('translate(660 350) scale(1.1)',R(-9,-90,18,92,'#4fae6a',8)+R(-34,-62,14,40,'#4fae6a',6)+R(20,-70,14,40,'#4fae6a',6))+c.ground('#d9a15a',1)},
 jungle(c){const T=c.T;return [0,1,2,3,4].map(i=>L(40+i*180,450,40+i*180,60,16,'#6a3f22')).join('')+[0,1,2,3,4,5,6].map(i=>P(`M${i*130-30},90 Q${i*130+30},30 ${i*130+90},90 Q${i*130+30},70 ${i*130-30},90Z`,i%2?'#3fa056':'#2f8a4a',2.6)).join('')+`<rect y="350" width="800" height="100" fill="${mix(T.g2,'#1d4a38',.35)}"/><path d="M0,350 L800,350" stroke="${INK}" stroke-width="3"/>`+[0,1,2].map(i=>flower(120+i*280,372,1.2,['#e8473b','#f6a23a','#e8709f'][i])).join('')+c.ground(T.g2)},
 city(c){const T=c.T,cols=['#8a96b8','#a08ab8','#8aa8b8','#b89a8a','#7a86a8'];return [...Array(10)].map((_,i)=>{const h=120+((i*53+c.seed*17)%150),w=70;return R(i*80-4,340-h,w,h,mix(cols[i%5],T.far,.3),2)+[...Array(Math.floor(h/32))].map((_,j)=>[0,1].map(k=>R(i*80+8+k*28,340-h+10+j*30,14,16,c.night?'#f6d35c':'#cfe9f8',2,1.8)).join('')).join('')}).join('')+`<rect y="340" width="800" height="110" fill="#6d7488"/><path d="M0,340 L800,340" stroke="${INK}" stroke-width="3"/>`+[...Array(8)].map((_,i)=>R(30+i*100,392,60,8,'#f1f1f4',3,0)).join('')},
 park(c){const T=c.T;return hill(400,330,500,70,T.far)+treeRound(110,340,1.1,T.g2)+treeRound(660,336,1,T.g2)+`<rect y="336" width="800" height="114" fill="${T.g1}"/><path d="M0,336 L800,336" stroke="${INK}" stroke-width="3"/>`+`<path d="M-20,450 Q300,380 820,360 L820,380 Q320,404 -20,450Z" fill="#e8d4a8" ${stk(3)}/>`+G('translate(560 352)',R(-34,-26,68,8,'#a8501f',2,2.4)+R(-34,-46,68,8,'#a8501f',2,2.4)+L(-28,-26,-28,-4,5,'#6a3f22')+L(28,-26,28,-4,5,'#6a3f22'))+c.ground(T.g2)},
 school(c){const T=c.T;return `<rect x="150" y="150" width="500" height="190" fill="#e8a24a" ${stk(3)}/>`+P('M130,150 L400,70 L670,150Z','#8a3a2a')+R(370,200,60,140,'#6a3f22',3)+[0,1,2].map(i=>window_(190+i*86,196,56,60)).join('')+[0,1,2].map(i=>window_(458+i*60,196,44,60)).join('')+G('translate(400 112)',C(0,0,22,'#fffaf0',3)+`<path d="M0,0 L0,-14 M0,0 L10,5" stroke="${INK}" stroke-width="3" stroke-linecap="round"/>`)+`<rect y="336" width="800" height="114" fill="${T.g1}"/><path d="M0,336 L800,336" stroke="${INK}" stroke-width="3"/>`+treeRound(70,346,.8,T.g2)+treeRound(740,346,.8,T.g2)+c.ground(T.g2)},
 classroom(c){return `<rect width="800" height="450" fill="#f2e3c2"/><rect y="330" width="800" height="120" fill="#b98a5a"/><path d="M0,330 L800,330" stroke="${INK}" stroke-width="3"/>`+R(150,70,500,170,'#2f6a5a',6,5)+`<path d="M180,110 Q260,100 330,120 M200,150 L420,150 M200,184 L360,184" stroke="#fff" stroke-width="5" fill="none" stroke-linecap="round" opacity=".85"/>`+window_(20,90,100,120)+window_(680,90,100,120)+[0,1,2].map(i=>R(60+i*260,380,150,12,'#a8501f',3,3)).join('')},
 kitchen(c){return `<rect width="800" height="450" fill="#f6e3b8"/><rect y="330" width="800" height="120" fill="#c9a574"/><path d="M0,330 L800,330" stroke="${INK}" stroke-width="3"/>`+R(60,60,230,110,'#fff',6)+window_(80,76,90,70)+[...Array(5)].map((_,i)=>R(60+i*46,190,40,100,'#e8c58f',4)).join('')+R(400,250,300,90,'#c4944a',6)+R(420,240,260,14,'#8a5a2b',4)+[0,1,2].map(i=>R(430+i*88,266,76,60,'#d6a860',4)).join('')+Lb.PROP.teapot('#e8709f').replace(/^/,'').length*0+G('translate(500 232) scale(.5)',Lb.PROP.teapot('#e8709f'))+G('translate(640 232) scale(.5)',Lb.PROP.bowl())},
 livingroom(c){return `<rect width="800" height="450" fill="#f2dcc0"/><rect y="340" width="800" height="110" fill="#b98a5a"/><path d="M0,340 L800,340" stroke="${INK}" stroke-width="3"/>`+window_(540,70,170,130)+R(70,100,110,150,'#c4944a',4)+G('translate(125 175) scale(.8)',Lb.PROP.clock())+R(60,250,520,16,'#6a3f22',6)+P('M620,340 Q600,260 700,260 Q790,262 780,340Z','#d9304a')+R(420,296,190,50,'#7a9ad8',10)+`<ellipse cx="300" cy="400" rx="180" ry="26" fill="#e8c58f" ${stk(3)}/>`},
 bedroom(c){return `<rect width="800" height="450" fill="#cfe0f6"/><rect y="340" width="800" height="110" fill="#b98a5a"/><path d="M0,340 L800,340" stroke="${INK}" stroke-width="3"/>`+window_(70,70,150,130,c.night?'#243b7a':'#bfe6f6')+(c.night?starD(110,110,8)+starD(170,150,6)+C(180,100,0,'none',0):'')+R(380,210,370,140,'#8a5a2b',8)+R(396,226,340,70,'#fff',10)+R(396,226,110,70,'#f6e8c8',14)+R(396,270,340,40,c.accent||'#7a9ad8',6)+R(260,300,100,50,'#c4944a',4)+G('translate(310 276) scale(.5)',Lb.PROP.lantern('#f6c84c'))},
 library(c){return `<rect width="800" height="450" fill="#e8d4a8"/><rect y="350" width="800" height="100" fill="#8a5a3a"/><path d="M0,350 L800,350" stroke="${INK}" stroke-width="3"/>`+[0,1,2].map(i=>R(40+i*250,40,210,300,'#a8501f',6)+[0,1,2,3].map(j=>R(48+i*250,56+j*72,194,8,'#6a3f22',0,0)+[...Array(9)].map((_,k)=>R(52+i*250+k*21,18+56+j*72-34+34,16,34-(k%3)*4,['#d9304a','#4a7be0','#4fae6a','#f6c84c','#8a5ac8'][(k+j+i)%5],2,1.8)).join('')).join('')).join('')},
 market(c){const cs=['#d9304a','#4a7be0','#f6a23a','#4fae6a'];return `<rect width="800" height="450" fill="${c.T.s2}"/><rect y="340" width="800" height="110" fill="#c9a574"/><path d="M0,340 L800,340" stroke="${INK}" stroke-width="3"/>`+[0,1,2].map(i=>G(`translate(${60+i*250} 330)`,R(-8,-130,8,130,'#6a3f22',2)+R(160,-130,8,130,'#6a3f22',2)+P('M-20,-130 L190,-130 L170,-170 L0,-170Z',cs[(i+c.seed)%4])+[0,1,2,3,4].map(k=>P(`M${-20+k*42},-130 L${-20+(k+1)*42},-130 L${-14+(k+1)*40},-140Z`,k%2?'#fff':cs[(i+c.seed)%4],2)).join('')+R(-4,-34,172,34,'#a8501f',3)+[0,1,2,3,4].map(k=>C(14+k*34,-40,14,['#e04a3a','#f6c84c','#8fd04a'][k%3],2.4)).join(''))).join('')},
 station(c){const T=c.T;return `<rect width="800" height="450" fill="${T.s2}"/>`+[0,1,2,3].map(i=>P(`M${i*220-40},300 L${i*220-40},130 Q${i*220+70},30 ${i*220+180},130 L${i*220+180},300Z`,'rgba(255,255,255,.35)',3)).join('')+`<path d="M0,64 L800,64" stroke="${INK}" stroke-width="3"/>`+G('translate(400 100)',C(0,0,26,'#fffaf0',3)+`<path d="M0,0 L0,-16 M0,0 L11,6" stroke="${INK}" stroke-width="3" stroke-linecap="round"/>`)+`<rect y="320" width="800" height="130" fill="#6d5a78"/><path d="M0,320 L800,320" stroke="${INK}" stroke-width="3"/>`+G('translate(560 310)',R(-60,-120,120,120,'#4a7be0',8)+R(-48,-104,96,42,'#cfeaf8',4,2.6)+C(-30,0,10,'#2b2538')+C(30,0,10,'#2b2538'))+[0,1,2].map(i=>`<path d="M${i*150},450 L${60+i*150},320" stroke="#4d3d58" stroke-width="3" opacity=".6"/>`).join('')},
 circus(c){return `<rect width="800" height="450" fill="#7a4aa8"/>`+[0,1,2,3,4,5,6,7].map(i=>`<path d="M400,-20 L${i*115-60},300 L${i*115+55},300Z" fill="${i%2?'#e8473b':'#fff3d6'}" opacity=".9"/>`).join('')+`<ellipse cx="400" cy="372" rx="380" ry="70" fill="#c4944a" ${stk(3)}/>`+`<ellipse cx="400" cy="372" rx="250" ry="42" fill="#e8c58f"/>`+[0,1,2,3,4,5].map(i=>star5(80+i*130,70+(i%2)*28,12,'#f6c84c')).join('')},
 stage(c){return `<rect width="800" height="450" fill="#5a1f3a"/>`+[0,1].map(i=>P(`M${i?800:0},0 L${i?560:240},0 Q${i?640:160},220 ${i?800:0},450Z`,'#c4202f',3)).join('')+`<rect y="330" width="800" height="120" fill="#8a5a2b"/><path d="M0,330 L800,330" stroke="${INK}" stroke-width="3"/>`+[0,1,2].map(i=>`<path d="M${200+i*200},0 L${130+i*200},330 L${270+i*200},330Z" fill="rgba(255,243,184,.25)"/>`).join('')+[...Array(10)].map((_,i)=>C(40+i*80,442,16,'#2b1d3a',0)).join('')},
 garden(c){const T=c.T;return `<rect y="300" width="800" height="150" fill="${T.g1}"/><path d="M0,300 L800,300" stroke="${INK}" stroke-width="3"/>`+[...Array(12)].map((_,i)=>R(i*70,230,60,70,'#4fae6a',22,3)).join('')+[...Array(9)].map((_,i)=>flower(40+i*90,330+(i%3)*14,1.1,['#e8473b','#f6a23a','#e8709f','#8a5ac8'][i%4])).join('')+G('translate(400 300)',R(-60,-120,12,120,'#c9ccd6',3)+R(48,-120,12,120,'#c9ccd6',3)+P('M-70,-120 Q0,-190 70,-120',"none",8,`stroke="#c9ccd6"`))+c.ground(T.g2)},
 pond(c){const T=c.T;return hill(160,320,300,80,T.far)+hill(660,320,320,90,T.far)+`<rect y="320" width="800" height="130" fill="${T.g1}"/><path d="M0,320 L800,320" stroke="${INK}" stroke-width="3"/>`+`<ellipse cx="400" cy="380" rx="330" ry="52" fill="#5aaee0" ${stk(3)}/>`+`<ellipse cx="400" cy="378" rx="250" ry="34" fill="#8fd0f0" opacity=".6"/>`+[0,1,2].map(i=>G(`translate(${250+i*150} ${380+(i%2)*10})`,E(0,0,28,10,'#4fae6a',2.6)+P('M0,0 L12,-8',"none",2))).join('')+[0,1,2,3,4].map(i=>L(40+i*40,336,40+i*40,300-i%2*20,4,'#8a6a3a')).join('')+c.ground(T.g2)},
 cave(c){return `<rect width="800" height="450" fill="#3a3050"/>`+P('M0,0 L800,0 L800,90 Q700,40 640,100 Q560,40 480,110 Q400,50 320,110 Q240,40 160,100 Q80,40 0,100Z','#2a2238',3)+`<path d="M0,360 Q200,330 400,360 T800,350 L800,450 L0,450Z" fill="#5a4a6a" ${stk(3)}/>`+[0,1,2,3].map(i=>P(`M${100+i*190},0 L${130+i*190},100 L${160+i*190},0Z`,'#4a3e60',2.6)).join('')+[0,1,2].map(i=>G(`translate(${140+i*250} 344)`,P('M-12,0 L0,-44 L12,0Z','#7ec8f2',2.6)+P('M6,0 L16,-26 L24,0Z','#a8e0ff',2.2))).join('')},
 space(c){return `<rect width="800" height="450" fill="#150f3a"/>`+[...Array(40)].map((_,i)=>`<circle cx="${(i*131+c.seed*7)%800}" cy="${(i*73)%420}" r="${1+(i%3)*.9}" fill="#fff" opacity=".9"/>`).join('')+G('translate(160 110)',C(0,0,54,'#e8923a')+E(0,0,86,16,'none',4,'stroke="#f6d35c" transform="rotate(-20)"')+C(-16,-14,10,'#c4651f',0))+G('translate(660 350)',C(0,0,120,'#5a4a9a')+C(-30,-30,16,'#4a3e80',0)+C(20,20,22,'#4a3e80',0))+C(0,0,0,'none',0)},
 underwater(c){return `<rect width="800" height="450" fill="#2f8ec0"/><linearGradient id="uw${c.id}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8fe0f6" stop-opacity=".7"/><stop offset="1" stop-color="#0a3a78" stop-opacity=".5"/></linearGradient><rect width="800" height="450" fill="url(#uw${c.id})"/>`+`<path d="M0,380 Q200,350 400,380 T800,370 L800,450 L0,450Z" fill="#e8c58f" ${stk(3)}/>`+[0,1,2,3,4].map(i=>G(`translate(${60+i*170} 392)`,P('M0,0 Q-10,-30 0,-60 Q10,-30 0,0Z',['#e8709f','#f6a23a','#8a5ac8'][i%3],2.6)+P('M10,0 Q4,-24 14,-46',"none",3,'stroke="#e8709f"'))).join('')+[...Array(10)].map((_,i)=>bubble((i*97+c.seed*11)%800,60+(i*61)%300,5+(i%3)*4)).join('')},
 bakery(c){return `<rect width="800" height="450" fill="#f6e3b8"/><rect y="340" width="800" height="110" fill="#c9a574"/><path d="M0,340 L800,340" stroke="${INK}" stroke-width="3"/>`+P('M40,70 L760,70 L730,120 L70,120Z','#e8709f')+[...Array(9)].map((_,i)=>P(`M${40+i*80},70 L${120+i*80},70 L${110+i*80},120 L${50+i*80},120Z`,i%2?'#fff':'#e8709f',2)).join('')+R(60,200,680,140,'#d9a15a',6)+R(80,216,640,40,'#fff3d6',6)+[0,1,2,3,4,5].map(i=>G(`translate(${130+i*100} 240) scale(.5)`,Lb.PROP[['bread','cake','bread','cake','bread','cake'][i]](['#d9a15a','#f3a6c8','#e8c58f','#e8709f','#d9a15a','#f6e8c8'][i]))).join('')},
 playground(c){const T=c.T;return hill(400,340,500,60,T.far)+`<rect y="336" width="800" height="114" fill="${mix(T.g1,'#e8d4a8',.45)}"/><path d="M0,336 L800,336" stroke="${INK}" stroke-width="3"/>`+G('translate(150 336)',L(-60,0,-30,-130,8,'#c9ccd6')+L(60,0,30,-130,8,'#c9ccd6')+L(-30,-130,30,-130,8,'#c9ccd6')+L(-20,-130,-26,-40,3,INK)+L(20,-130,26,-40,3,INK)+R(-40,-44,40,10,'#e8473b',3)+R(10,-44,40,10,'#f6c84c',3))+G('translate(580 336)',P('M-70,0 L-10,-110 L-10,-90 L-60,0Z','#4a7be0',3)+R(-14,-122,40,12,'#c9ccd6',3)+P('M26,-110 L96,0 L80,0 L26,-90Z','#f6c84c',3))+c.ground(T.g1)},
 barn(c){const T=c.T;return `<rect y="330" width="800" height="120" fill="#c9a574"/><path d="M0,330 L800,330" stroke="${INK}" stroke-width="3"/>`+`<rect width="800" height="330" fill="#a8501f"/>`+[...Array(14)].map((_,i)=>`<path d="M${i*60},0 L${i*60},330" stroke="${INK}" stroke-width="2" opacity=".5"/>`).join('')+`<path d="M200,330 L200,120 L400,70 L600,120 L600,330Z" fill="#8a3a2a" ${stk(3)}/><path d="M200,330 L600,120 M600,330 L200,120" stroke="#f6e8c8" stroke-width="7"/>`+[0,1,2].map(i=>R(60+i*250,334,70,26,'#d9a15a',3)).join('')},
 bridge(c){const T=c.T;return hill(160,330,300,100,T.far)+hill(660,330,320,110,T.far)+`<rect y="340" width="800" height="110" fill="#4a98c8"/>`+wave(352,'#7ac8e8',7,0)+P('M0,260 Q400,170 800,260 L800,300 Q400,220 0,300Z','#c9a574',3)+[...Array(11)].map((_,i)=>`<path d="M${i*80},${268-Math.sin(i/10*Math.PI)*60} L${i*80},${300-Math.sin(i/10*Math.PI)*60}" stroke="${INK}" stroke-width="3"/>`).join('')+c.ground(T.g2,1)},
 camp(c){const T=c.T;return hill(400,340,500,60,T.far)+treePine(70,352,1,'#2f6a52')+treePine(730,352,1,'#2f6a52')+`<rect y="340" width="800" height="110" fill="${T.g2}"/><path d="M0,340 L800,340" stroke="${INK}" stroke-width="3"/>`+G('translate(560 350)',P('M-80,0 L0,-110 L80,0Z','#e8923a',3)+P('M-24,0 L0,-50 L24,0Z','#6a3f22',2.6))+G('translate(250 366)',[0,1,2].map(i=>L(-20+i*20,0,-12+i*12,-30,6,'#6a3f22')).join('')+P('M0,-26 Q-14,-48 0,-62 Q14,-48 0,-26Z','#f6a23a',2.6)+P('M0,-30 Q-6,-42 0,-50 Q6,-42 0,-30Z','#f6d35c',0))},
 skyline(c){return SCENES.city(c)},
 beach(c){return SCENES.seaside(c)},
 attic(c){return `<rect width="800" height="450" fill="#8a6a4a"/><path d="M0,0 L400,-60 L800,0 L800,450 L0,450Z" fill="#a8845a" ${stk(3)}/><rect y="360" width="800" height="90" fill="#6a4a2a"/><path d="M0,360 L800,360" stroke="${INK}" stroke-width="3"/>`+window_(330,110,140,140,c.night?'#243b7a':'#bfe6f6')+G('translate(110 360) scale(1.2)',Lb.PROP.chest())+G('translate(680 360) scale(1)',Lb.PROP.suitcase('#6a3f22'))},
 throne(c){return `<rect width="800" height="450" fill="#7a2f4a"/><rect y="340" width="800" height="110" fill="#d9c8e8"/><path d="M0,340 L800,340" stroke="${INK}" stroke-width="3"/>`+[0,1,2,3].map(i=>R(60+i*220,0,50,340,'#e6ddf0',4)).join('')+P('M280,340 L280,120 Q400,60 520,120 L520,340Z','#c4202f',3)+R(300,170,200,170,'#f6c84c',8)+P('M380,60 L400,30 L420,60Z','#f6c84c',2.6)},
 workshop(c){return `<rect width="800" height="450" fill="#d9bf94"/><rect y="340" width="800" height="110" fill="#8a6a3a"/><path d="M0,340 L800,340" stroke="${INK}" stroke-width="3"/>`+R(60,120,300,18,'#6a3f22',4)+R(440,170,300,18,'#6a3f22',4)+[0,1,2,3,4].map(i=>G(`translate(${100+i*56} 120) scale(.4)`,Lb.PROP[['hammer','scissors','ladder','paintbrush','bell'][i]]())).join('')+G('translate(600 330)',R(-70,-60,140,60,'#a8501f',4)+R(-80,-70,160,14,'#c4944a',4))}
};
SCENES.plaza=c=>SCENES.village(c);
SCENES.road=c=>SCENES.hills(c)+`<path d="M330,450 L400,336 L470,450Z" fill="#8f95a8" ${stk(3)}/>`;

/* ---------- decoração ---------- */
function decor(list,c,rnd){
  let g='';const T=c.T;
  (list||[]).forEach(d=>{
    if(d==='flowers')g+=[...Array(8)].map((_,i)=>flower(20+rnd()*760,372+rnd()*60,1.2+rnd()*.6,['#e8473b','#f6a23a','#e8709f','#8a5ac8','#fff'][i%5])).join('');
    else if(d==='mushrooms')g+=[...Array(4)].map(()=>mush(30+rnd()*740,385+rnd()*50,.9+rnd()*.5,['#e8473b','#e8709f','#f6a23a'][Math.floor(rnd()*3)])).join('');
    else if(d==='butterflies')g+=[...Array(3)].map(()=>butterfly(100+rnd()*600,110+rnd()*160,['#e8709f','#f6a23a','#7ec8f2'][Math.floor(rnd()*3)])).join('');
    else if(d==='birds')g+=[...Array(3)].map(()=>bird(80+rnd()*640,50+rnd()*120,1+rnd()*.5)).join('');
    else if(d==='clouds')g+=[...Array(3)].map((_,i)=>cloud(100+i*280+rnd()*60,60+rnd()*60,.6+rnd()*.4,T.stars>1?'#4a5a9a':'#fff')).join('');
    else if(d==='balloons')g+=[...Array(3)].map(()=>balloonD(80+rnd()*640,80+rnd()*120,['#e8473b','#f6c84c','#4a7be0','#e8709f'][Math.floor(rnd()*4)])).join('');
    else if(d==='stars')g+=[...Array(7)].map(()=>starD(30+rnd()*740,30+rnd()*150,4+rnd()*7)).join('');
    else if(d==='hearts')g+=[...Array(4)].map(()=>heartD(100+rnd()*600,60+rnd()*160,.28+rnd()*.15,'#e8473b')).join('');
    else if(d==='leaves')g+=[...Array(9)].map(()=>leaf(rnd()*800,40+rnd()*320,rnd()*360,['#e8923a','#d9304a','#f6c84c'][Math.floor(rnd()*3)])).join('');
    else if(d==='snow')g+=[...Array(18)].map(()=>flake(rnd()*800,rnd()*340,.7+rnd()*.6)).join('');
    else if(d==='bubbles')g+=[...Array(9)].map(()=>bubble(rnd()*800,40+rnd()*320,4+rnd()*9)).join('');
    else if(d==='fireflies')g+=[...Array(10)].map(()=>firefly(rnd()*800,120+rnd()*240)).join('');
    else if(d==='sparkles')g+=[...Array(7)].map(()=>sparkle(40+rnd()*720,40+rnd()*300,7+rnd()*8)).join('');
    else if(d==='grass')g+=[...Array(10)].map(()=>tuft(rnd()*800,360+rnd()*80,.9+rnd()*.5)).join('');
  });
  return g;
}

/* ---------- composição ---------- */
function groundLayer(c){return (col,sea)=>{if(sea)return'';return [...Array(7)].map((_,i)=>tuft(30+i*115+c.rnd()*40,418+c.rnd()*20,1)).join('')}}
function castSvg(cast,c){
  const n=cast.length;if(!n)return'';
  const slots={1:[400],2:[300,520],3:[230,400,570],4:[190,330,470,610],5:[160,280,400,520,640]}[Math.min(5,n)];
  let g='';
  const items=cast.map((m,i)=>{const x=m.x!=null?m.x:slots[i],big=m.p?1.2:1;const s=(m.s||1)*big*(n>3?.85:1);return {m,x,s,i}});
  items.sort((a,b)=>(a.m.back?-1:0)-(b.m.back?-1:0));
  items.forEach(({m,x,s,i})=>{
    let inner='';
    if(m.p){const o=Object.assign({},m.p);if(o.holds&&!o.arms)o.arms='hold';inner=Lb.person(o)}
    else if(m.a){const f=Lb.ANIMAL[m.a];inner=f?f(m.c,m.c2):''}
    const y=m.y!=null?m.y:(c.indoorFloor?396:402+((i%2)?6:0));
    g+=G(`translate(${x} ${y}) scale(${m.flip?-s:s} ${s})`,inner);
  });
  return g;
}
function propSvg(pr,cast){
  if(!pr||!Lb.PROP[pr.id])return'';
  const at=pr.at||'front',s=pr.s||1.5;
  const pos={front:[400,340],sky:[400,110],left:[110,330],right:[690,330],between:[400,380],'sky-left':[170,110],'sky-right':[630,110]}[at]||[400,340];
  if(at==='held')return'';
  const x=pr.x!=null?pr.x:pos[0],y=pr.y!=null?pr.y:pos[1];
  return G(`translate(${x} ${y}) scale(${s})`,Lb.PROP[pr.id](pr.c));
}
function stage(f,seed){
  const id=++UID,tod=f.tod&&TOD[f.tod]?f.tod:'day',rnd=rngOf(hash(seed));
  const T=Object.assign({},TOD[tod]);if(f.accent){T.g1=mix(T.g1,f.accent,.18);T.far=mix(T.far,f.accent,.25)}
  const indoor=/^(classroom|kitchen|livingroom|bedroom|library|market|bakery|cave|attic|throne|workshop|stage|circus)$/.test(f.scene);
  const c={id,T,tod,night:tod==='night'||tod==='dusk',seed:hash(seed)%7,rnd,accent:f.accent,indoorFloor:indoor};
  c.ground=groundLayer(c);
  const scene=SCENES[f.scene]||SCENES.meadow;
  const useSky=!/^(classroom|kitchen|livingroom|bedroom|library|bakery|cave|attic|throne|workshop|stage|circus|space|underwater|ship|harbor|seaside|market|station|barn|beach)$/.test(f.scene);
  let g=`<defs><filter id="gr${id}" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" seed="${id%9+2}"/><feColorMatrix values="0 0 0 0 .2  0 0 0 0 .15  0 0 0 0 .1  0 0 0 .09 0"/></filter><radialGradient id="vg${id}" cx=".5" cy=".5" r=".75"><stop offset=".6" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#1b1030" stop-opacity=".38"/></radialGradient></defs>`;
  if(useSky||/^(seaside|harbor|ship|market|station|barn|beach)$/.test(f.scene)){g+=sky(id,tod,f.accent);if(!/^(market|station|barn)$/.test(f.scene))g+=lumin(tod,f.sunx)}
  g+=scene(c);
  if(useSky&&tod!=='night'&&!(f.decor||[]).includes('clouds'))g+=cloud(150,90,.8)+cloud(560,70,.6);
  g+=decor(f.decor,c,rnd);
  return {g,id,c};
}
const countEl=g=>(g.match(/<(path|ellipse|circle|rect|line|polygon|g)\b/g)||[]).length;
/* enriquece cenas esparsas com enfeites discretos (nunca sobre o elenco: vêm antes dele) até o detalhe mínimo das capas desenhadas */
function enrich(g,S,f,body){
  const rnd=rngOf(hash('enr'+(f.scene||'')+(f.tod||'')+g.length)),T=S.c.T,indoor=S.c.indoorFloor,night=S.c.night;
  let add='',i=0;
  while(countEl(g+add+body)<122&&i++<8){
    if(indoor){add+=[...Array(3)].map(()=>sparkle(40+rnd()*720,40+rnd()*260,6+rnd()*7)).join('')+[...Array(2)].map(()=>starD(40+rnd()*720,40+rnd()*200,5+rnd()*5)).join('')}
    else{
      add+=[...Array(3)].map(()=>flower(20+rnd()*760,380+rnd()*60,1+rnd()*.5,['#e8473b','#f6a23a','#e8709f','#8a5ac8','#fff'][Math.floor(rnd()*5)])).join('')+[...Array(3)].map(()=>tuft(rnd()*800,375+rnd()*70,.9+rnd()*.4)).join('');
      add+=night?[...Array(3)].map(()=>firefly(rnd()*800,140+rnd()*240)).join(''):butterfly(80+rnd()*640,100+rnd()*150,['#e8709f','#f6a23a','#7ec8f2'][Math.floor(rnd()*3)])+sparkle(60+rnd()*680,50+rnd()*200,6+rnd()*6);
    }
  }
  return add;
}
function compose(f,seed,mode){
  const S=stage(f,seed),cast=(f.cast||[]).slice(0,5);
  let g=S.g;
  const bodyProp=propSvg(f.prop&&f.prop.at!=='held'?f.prop:null,cast),bodyCast=castSvg(cast,S.c);
  g+=enrich(g,S,f,bodyProp+bodyCast);
  g+=bodyProp;
  g+=bodyCast;
  if(f.prop&&f.prop.at==='front'&&f.propOver)g+=propSvg(f.prop,cast);
  g+=`<rect width="800" height="450" filter="url(#gr${S.id})"/><rect width="800" height="450" fill="url(#vg${S.id})"/>`;
  return g;
}
const VBM={cover:'0 0 800 450',sticker:'110 20 580 420',strip:'100 140 600 200',face:'0 0 800 450'};
function faceSvg(f){const m=(f.cast||[])[0];if(!m)return'';const o=m.p?Lb.person(Object.assign({},m.p,{holds:null})):(Lb.ANIMAL[m.a]?Lb.ANIMAL[m.a](m.c,m.c2):'');const vb=m.p?'-52 -214 104 104':'-56 -190 112 112';return `<svg class="obra-face" viewBox="${vb}" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true">${o}</svg>`}
function fichaOf(e){const n=e&&(e.n!=null?e.n:(e.e&&e.e.n));return (window.PogFichas&&window.PogFichas[n])||null}
function svg(e,mode){
  const f=fichaOf(e);if(!f)return'';
  if(mode==='face'||/face/.test(mode||''))return faceSvg(f);
  const key=/sticker/.test(mode||'')?'sticker':/strip/.test(mode||'')?'strip':'cover';
  return `<svg class="obra-art obra-svg obra-${key}" viewBox="${VBM[key]}" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img">${compose(f,(e.n||'')+'|'+(f.scene||''),key)}</svg>`;
}
const DECOR=['flowers','mushrooms','butterflies','birds','clouds','balloons','stars','hearts','leaves','snow','bubbles','fireflies','sparkles','grass'];
const PROPAT=['front','sky','left','right','between','sky-left','sky-right','held'];
window.PogFicha={VOCAB:{scene:Object.keys(SCENES),tod:Object.keys(TOD),decor:DECOR,propAt:PROPAT},has:e=>!!fichaOf(e),svg,compose,SCENES,TOD,fichaOf,face:e=>{const f=fichaOf(e);return f?faceSvg(f):''}};
})();
