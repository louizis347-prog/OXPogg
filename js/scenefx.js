/* Pogglot · PogSceneFX: camadas de realismo para as capas de cena (js/scenes.js).
   Luz direcional por hora do dia, sombras projetadas, reflexos em vidro, brilho de madeira/metal/tecido,
   névoa de profundidade, bokeh, vapor, poeira, grão e vinheta — tudo SVG vetorial inline, sem rede e sem imagens.
   scenes.js chama: back(ctx) (sobre o cenário, sob o personagem), hands(ctx) e front(ctx) (sobre o personagem).
   ctx.lite = versão leve para listas/miniaturas: sem filtros SVG, sem animação, menos detalhes. */
(function(w){
'use strict';
const W=320,H=172;
const n1=v=>Math.round(v*10)/10;
const hash=s=>{let h=2166136261;s=String(s);for(let i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619)}return h>>>0};
const rng=seed=>{let a=seed>>>0||1;return()=>{a^=a<<13;a>>>=0;a^=a>>>17;a^=a<<5;a>>>=0;return a/4294967296}};
const hx=h=>{if(h.length===4)h='#'+h[1]+h[1]+h[2]+h[2]+h[3]+h[3];return [parseInt(h.slice(1,3),16),parseInt(h.slice(3,5),16),parseInt(h.slice(5,7),16)]};
const mix=(a,b,k)=>{const x=hx(a),y=hx(b);return '#'+x.map((v,i)=>Math.round(v+(y[i]-v)*k).toString(16).padStart(2,'0')).join('')};
const O=a=>a==null?'':` fill-opacity="${a}"`;
const rect=(x,y,w,h,f,a,x2)=>`<rect x="${n1(x)}" y="${n1(y)}" width="${n1(w)}" height="${n1(h)}" fill="${f}"${O(a)}${x2||''}/>`;
const circ=(x,y,r,f,a,x2)=>`<circle cx="${n1(x)}" cy="${n1(y)}" r="${n1(r)}" fill="${f}"${O(a)}${x2||''}/>`;
const ell=(x,y,rx,ry,f,a,x2)=>`<ellipse cx="${n1(x)}" cy="${n1(y)}" rx="${n1(rx)}" ry="${n1(ry)}" fill="${f}"${O(a)}${x2||''}/>`;
const path=(d,f,a,x2)=>`<path d="${d}" fill="${f}"${O(a)}${x2||''}/>`;
const line=(d,c,sw,a,x2)=>`<path d="${d}" fill="none" stroke="${c}" stroke-width="${sw}"${a!=null?` stroke-opacity="${a}"`:''} stroke-linecap="round"${x2||''}/>`;
const lg=(id,x1,y1,x2,y2,st)=>`<linearGradient id="${id}" x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}">${st.map(s=>`<stop offset="${s[0]}" stop-color="${s[1]}" stop-opacity="${s[2]==null?1:s[2]}"/>`).join('')}</linearGradient>`;
const rg=(id,st,cx,cy,r)=>`<radialGradient id="${id}"${cx!=null?` cx="${cx}" cy="${cy}" r="${r}"`:''}>${st.map(s=>`<stop offset="${s[0]}" stop-color="${s[1]}" stop-opacity="${s[2]==null?1:s[2]}"/>`).join('')}</radialGradient>`;

/* luz por hora: cor da chave, intensidade, cor ambiente e correção de cor */
const KEY={dawn:'#FFC6A0',day:'#FFF1CF',golden:'#FFB45E',dusk:'#FF9068',night:'#8DA4FF'};
const INT={dawn:.5,day:.5,golden:.72,dusk:.5,night:.28};
const WARM='#FFC977';
const GRADE={dawn:['#ff9fae',.05],day:null,golden:['#ffa850',.07],dusk:['#c45a8c',.07],night:['#1d2a78',.22]};

/* ================== INTERIORES ================== */
const FB={cafe:127,shop:127,kitchen:116,library:127,restaurant:H,living:H,office:H,classroom:H,clinic:H,hall:H,gym:H,museum:H,ballroom:H,cinema:H,subwaycar:H};

function steam(p,x,y,n,lite,s){
  let q='';for(let i=0;i<n;i++){const dx=(i-(n-1)/2)*2.6;
    q+=`<path class="${p}st" style="animation-delay:${i*.7}s" d="M${n1(x+dx)} ${y} C${n1(x+dx-3)} ${y-4} ${n1(x+dx+3)} ${y-7} ${n1(x+dx)} ${y-11}${lite?'':` S${n1(x+dx+2)} ${y-17} ${n1(x+dx-1)} ${y-20}`}" fill="none" stroke="#fff" stroke-opacity="${n1(.5-i*.08)}" stroke-width="${n1(1.3*(s||1))}" stroke-linecap="round"/>`}
  return q;
}
function cup(p,x,y,lite,k){
  k=k||1;
  let q=ell(x,y+1,9*k,2,'#000',.22)+ell(x,y,8.4*k,2.2,'#EDE6D8')+ell(x,y-.4,8*k,1.8,'#fff',.7);
  q+=path(`M${n1(x-5*k)} ${n1(y-1)} L${n1(x+5*k)} ${n1(y-1)} L${n1(x+4*k)} ${n1(y-10*k)} L${n1(x-4*k)} ${n1(y-10*k)}Z`,'url(#'+p+'cup)');
  q+=ell(x,y-10*k,4*k,1.3,'#4a2410')+ell(x-.8,y-10.3*k,2.4*k,.6,'#a0663a',.7)+`<path d="M${n1(x+4.6*k)} ${n1(y-8*k)} q${n1(4*k)} .5 ${n1(3.4*k)} ${n1(4.6*k)} q-1 2 ${n1(-4*k)} ${n1(2*k)}" fill="none" stroke="#e6dfd0" stroke-width="1.3"/>`;
  q+=rect(x-3.4*k,y-9*k,1,7*k,'#fff',.55);
  return q+(lite?'':steam(p,x,y-12*k,2,lite,.9));
}
function leaves(x,y,n,len,col,R,rot){
  let q='';for(let i=0;i<n;i++){const a=(-90+(i-(n-1)/2)*(150/Math.max(1,n-1))+(rot||0))*Math.PI/180,l=len*(.75+R()*.35),ex=x+Math.cos(a)*l,ey=y+Math.sin(a)*l,mx=x+Math.cos(a)*l*.5+Math.sin(a)*l*.16,my=y+Math.sin(a)*l*.5-Math.cos(a)*l*.16;
    q+=path(`M${n1(x)} ${n1(y)} Q${n1(mx+Math.sin(a)*l*.22)} ${n1(my-Math.cos(a)*l*.22)} ${n1(ex)} ${n1(ey)} Q${n1(mx-Math.sin(a)*l*.22)} ${n1(my+Math.cos(a)*l*.22)} ${n1(x)} ${n1(y)}Z`,i%2?col:mix(col,'#000',.18))+line(`M${n1(x)} ${n1(y)} L${n1(ex)} ${n1(ey)}`,mix(col,'#fff',.35),.5,.6)}
  return q;
}
function pot(x,y,w,h,col){return path(`M${n1(x-w/2)} ${n1(y)} L${n1(x+w/2)} ${n1(y)} L${n1(x+w/2-w*.12)} ${n1(y+h)} L${n1(x-w/2+w*.12)} ${n1(y+h)}Z`,col)+rect(x-w/2,y,w,h*.18,mix(col,'#fff',.25))+rect(x+w*.12,y+h*.18,w*.3,h*.82,'#000',.18)}
function shelfShade(x,y,w,rows){let q='';for(let r=0;r<rows;r++)q+=rect(x,y+r*17+15.4,w,4,'url(#SHD)');return q}

const IN={};
IN.cafe=function(c,p,R){
  let d='',s='';const lite=c.lite,night=c.tm==='night',lit=c.T.lit;
  d+=lg(p+'cup',0,0,1,0,[[0,'#fff'],[.6,'#EFE9DC'],[1,'#B9B0A0']])+lg(p+'cm',0,0,1,0,[[0,'#E4EAF0'],[.35,'#8892A6'],[.6,'#C9CED9'],[1,'#5c6477']])+lg(p+'bd',0,0,0,1,[[0,'#fff',.14],[1,'#000',.3]]);
  /* prateleira: sombras e plantinha */
  s+=shelfShade(210,24,84,2).replace(/SHD/g,p+'ao')+rect(210,24,84,34,'url(#'+p+'bd)',1,' opacity=".6"');
  s+=pot(279,24,9,7,'#C0634A').replace('</g>','')+leaves(279,24,6,10,'#3E9A63',R)+line('M270 24 q-6 6 -4 14 M272 24 q-3 8 -1 16','#3E9A63',1.1,.9)+line('M294 38 q4 7 1 14','#3E9A63',1,.8);
  /* quadro de giz */
  s+=rect(18,24,52,2.2,'#fff',.22)+rect(18,24,2,36,'#fff',.14)+rect(18,58,52,2.2,'#000',.3)+rect(20,26,48,32,'#22332d')+(c.lite?'':rect(20,26,48,32,'url(#'+p+'chk)'));
  s+=`<text x="26" y="36.5" font-family="'Plus Jakarta Sans',system-ui,sans-serif" font-weight="800" font-size="6.2" fill="#fff" fill-opacity=".9" letter-spacing=".6">CAFÉ</text>`+line('M26 40 h16 M26 45 h22 M26 50 h12','#fff',1,.55)+line('M54 40 h8 M54 45 h8 M54 50 h8','#F4C26B',1,.7)+`<path d="M52 29 q1 -3 0 -5 M55 29 q1 -3 0 -5" stroke="#fff" stroke-opacity=".5" fill="none" stroke-width=".7"/>`;
  if(!lite)s+=ell(42,44,12,8,'#fff',.05)+ell(60,52,6,3,'#fff',.05);
  /* luzes pendentes: cones de luz + lâmpadas */
  [[70,14],[150,26],[240,18]].forEach(([x,l])=>{
    const by=l+9,a=c.tm==='day'?.1:(c.tm==='night'?.3:.2);
    s+=path(`M${x-8} ${by} L${x+8} ${by} L${x+50} ${126} L${x-50} ${126}Z`,'url(#'+p+'cone)',1,` opacity="${n1(a*.7)}"`)+path(`M${x-6} ${by} L${x+6} ${by} L${x+26} ${126} L${x-26} ${126}Z`,'url(#'+p+'cone)',1,` opacity="${n1(a*.9)}"`)+ell(x,by-1,5,2.2,'#FFF1C8',.95)+rect(x-5,by-8,2,5,'#fff',.35)+rect(x-.4,0,.8,l,'#fff',.25);
  });
  d+=lg(p+'cone',0,0,0,1,[[0,WARM,.55],[1,WARM,0]]);
  /* balcão */
  s+=rect(0,128,W,1.4,'#fff',.4)+rect(0,129.4,W,4,'url(#'+p+'wt)')+rect(0,133.4,W,1.4,'#000',.28);
  d+=lg(p+'wt',0,0,0,1,[[0,'#fff',.22],[1,'#000',.0]]);
  if(c.win){const wx=c.win.x+c.win.w/2;s+=ell(wx+(-c.ld)*10,131,50,2.2,c.key,.4*c.I)}
  if(!lite){for(let i=0;i<9;i++){const y=137+i*3.5;s+=line(`M0 ${y} C${80+R()*40} ${y-1} ${180+R()*50} ${y+1} ${W} ${y}`,'#000',.5,.16)}
    for(let i=1;i<8;i++)s+=rect(i*42,134,.8,38,'#000',.2)+rect(i*42+.8,134,.5,38,'#fff',.07);
    s+=rect(0,159,W,2.6,'url(#'+p+'cm)',1,' opacity=".85"')+rect(0,159,W,.7,'#fff',.7)+rect(0,161.6,W,3,'#000',.22)+rect(30,160,2.4,10,'#9aa0b5')+rect(150,160,2.4,10,'#9aa0b5')+rect(270,160,2.4,10,'#9aa0b5');}
  /* máquina de espresso: cromado, grupo, manômetro */
  s+=rect(212,102,34,26,'url(#'+p+'cm)',1,' opacity=".55"')+rect(212,102,34,2,'#fff',.7)+rect(214,104,4,22,'#fff',.4)+rect(222,104,1,22,'#000',.25)+rect(224,114,12,3,'#2a2f45')+rect(226,117,8,1.6,'#555')+rect(228,119,4,5,'#1b1b22');
  s+=circ(236,112,4.4,'none',null,' stroke="#C9CED9" stroke-width="1.1"')+line('M236 112 L238.4 110.2','#E8493A',.9)+line('M246 118 q6 2 5 8','#C9CED9',1.2,.9)+rect(214,106,3,1,'#E8493A',.9);
  s+=rect(246,118,18,9,'#E8DCC4')+rect(246,118,18,1.5,'#fff',.6)+rect(248,120,6,4,'#C0634A')+rect(255,120,6,4,'#8a5a2a')+ell(255,127,12,1.4,'#000',.2);
  /* xícaras */
  [[60,126],[90,126],[180,126],[290,126]].forEach(([x,y])=>{s+=cup(p,x,y,lite)});
  /* cúpula com croissants */
  s+=ell(130,125.6,17,2.2,'#000',.2)+ell(130,122,16,6,'#F4EDDD',.9)+ell(130,122,16,6,'none',null,' stroke="#C9BFA5" stroke-width=".6"');
  s+=path('M122 121 q4 -6 9 -1 q3 1 5 3 q-6 3 -14 -2Z','#D9944A')+path('M127 120 q2 -3 5 -1M130 122 q2 -3 5 -1M124 121 q1 -2 3 -2','none',' stroke="#9a5c24" stroke-width=".6" fill="none"')+path('M132 124 q5 -5 11 -1 q-4 4 -11 1Z','#C98237');
  s+=path('M113 123 Q130 98 147 123Z','#cfe8ff',.18)+path('M117 121 Q124 106 134 104','none',' stroke="#fff" stroke-opacity=".6" stroke-width="1.3" fill="none" stroke-linecap="round"')+circ(130,103,1.6,'#fff',.7);
  /* reflexos dos itens no tampo */
  s+=ell(130,131,14,1.4,'#fff',.1);
  return {d,s};
};
IN.restaurant=function(c,p,R){
  let d='',s='';const lite=c.lite;
  d+=lg(p+'cone',0,0,0,1,[[0,WARM,.5],[1,WARM,0]]);
  [[60,22],[160,34],[262,22]].forEach(([x,l])=>{s+=path(`M${x-9} ${l+9} L${x+9} ${l+9} L${x+46} ${132} L${x-46} ${132}Z`,'url(#'+p+'cone)',1,` opacity="${c.tm==='day'?.1:.26}"`)+ell(x,l+8,5,2,'#FFF1C8',.95)+rect(x-.4,0,.8,l,'#fff',.25)});
  [[70,132,1],[170,144,1.15],[262,132,1]].forEach(([tx,ty,k],i)=>{
    s+=`<g transform="translate(${tx} ${ty}) scale(${k})">`+ell(0,32,28,3,'#000',.25)+
     path('M-24 1 L24 1 L20 9 L-20 9Z','#fff',.16)+line('M-14 3 L-12 9 M-2 3 L-1.6 9.6 M10 3 L10.6 9','#000',.5,.2)+rect(-24,-2,48,1,'#fff',.7)+
     ell(-10,-3.4,5,1.4,'#fff',.9)+ell(10,-3.4,5,1.4,'#fff',.9)+ell(-10,-3.8,2.6,.7,'#E3A95B')+ell(10,-3.8,2.6,.7,'#9CCB86')+
     /* taça */`<path d="M-1.6 -3 q-2.4 -6 0 -9 h3.2 q2.4 3 0 9z" fill="#fff" fill-opacity=".28"/><path d="M-1.4 -5 h2.8 q.6 -2.6 -.2 -4 h-2.4 q-.8 1.4 -.2 4z" fill="#9a2a3a" fill-opacity=".8"/>`+rect(-.2,-3,.4,4,'#fff',.6)+
     /* vela */rect(5,-8,1.8,6,'#F4EDDD')+`<path d="M5.9 -8.6 q-1.3 -2 0 -3.6 q1.3 1.6 0 3.6z" fill="#FFC970"/>`+circ(5.9,-10,6,'url(#'+p+'fl)',.8)+
     '</g>';
  });
  d+=rg(p+'fl',[[0,'#FFD98A',.9],[1,'#FFD98A',0]]);
  s+=`<path d="M0 ${c.horizon} h${W}" stroke="#fff" stroke-opacity=".08"/>`;
  if(!lite)for(let i=0;i<6;i++){const y=122+i*8;s+=rect(0,y,W,.6,'#000',.13)}
  return {d,s};
};
IN.kitchen=function(c,p,R){
  let d='',s='';const lite=c.lite;
  d+=lg(p+'cm',0,0,1,0,[[0,'#E4EAF0'],[.35,'#8892A6'],[.6,'#C9CED9'],[1,'#5c6477']]);
  /* azulejos: rejunte, brilho */
  for(let i=1;i<8;i++)s+=rect(i*40+1,58,.7,24,'#000',.16);
  s+=rect(0,70,W,.7,'#000',.16)+path('M0 82 H320 V86 H0Z','url(#'+p+'ao)',1)+rect(0,58,W,1.2,'#fff',.55);
  if(!lite)for(let i=0;i<8;i++)s+=path(`M${i*40+6} 80 L${i*40+22} 60 L${i*40+26} 60 L${i*40+10} 80Z`,'#fff',.12);
  /* coifa metálica */
  s+=rect(120,30,70,30,'url(#'+p+'cm)',1,' opacity=".6"')+rect(120,30,70,1.6,'#fff',.5)+line('M132 46 h46 M132 50 h46 M132 54 h46','#000',.8,.25)+rect(120,59,70,1.6,'#000',.3)+ell(155,62,40,4,WARM,.3*(c.T.lit+.3));
  /* utensílios */
  [[60],[100],[230],[262]].forEach(([px],i)=>{s+=rect(px-8,76,16,1.4,'#fff',.45)+rect(px-6,78,2,11,'#fff',.3)+ell(px,91,7,1.2,'#000',.18)+path(`M${px-1} 60 q-2 6 0 14`,'none',' stroke="#C9CED9" stroke-width=".8" fill="none"')});
  /* bancada */
  s+=rect(0,116,W,1.2,'#fff',.7)+rect(0,117.2,W,4.8,'url(#'+p+'ao)',1,' transform="rotate(180 160 119.6)"')+rect(0,122,W,50,'url(#'+p+'ao2)');
  d+=lg(p+'ao2',0,0,0,1,[[0,'#000',.0],[1,'#000',.25]]);
  if(!lite)for(let i=0;i<30;i++)s+=circ(R()*W,117+R()*3,.5,i%2?'#fff':'#000',.2);
  /* fogão: bocas, botões, panela com vapor */
  s+=rect(130,124,60,2,'#fff',.4)+circ(150,134,6,'none',null,' stroke="#777" stroke-width=".8"')+circ(172,134,6,'none',null,' stroke="#777" stroke-width=".8"');
  s+=rect(143,121,14,6,'url(#'+p+'cm)')+rect(142,119,16,2.6,'#8892A6')+ell(150,119,8,1.4,'#fff',.4)+rect(158,121,5,1.2,'#333')+steam(p,150,118,3,lite,1);
  s+=circ(140,148,1.6,'#E8493A',.9)+circ(148,148,1.6,'#ddd',.9)+circ(172,148,1.6,'#ddd',.9)+circ(180,148,1.6,'#ddd',.9);
  /* frutas na bancada */
  s+=circ(196,112,7,'#9CCB86')+circ(206,111,6,'#E8795A')+circ(194,109.6,2,'#fff',.45)+circ(204,108.6,1.8,'#fff',.5)+line('M196 105 q1 -3 3 -3','#3E7A3E',1);
  return {d,s};
};
IN.living=function(c,p,R){
  let d='',s='';const lite=c.lite;
  d+=lg(p+'sf',0,0,0,1,[[0,'#fff',.14],[.5,'#000',0],[1,'#000',.28]]);
  /* quadros: vidro, sombra */
  [[210,26,36,28],[258,36,30,22]].forEach(([fx,fy,fw,fh])=>{s+=rect(fx+2.4,fy+2.4,fw,fh,'#000',.18)+rect(fx,fy,fw,1.2,'#fff',.6)+path(`M${fx+3} ${fy+fh-3} L${fx+fw*.45} ${fy+3} L${fx+fw*.6} ${fy+3} L${fx+fw*.18} ${fy+fh-3}Z`,'#fff',.22)});
  s+=line('M222 36 q8 -6 14 0 M216 48 q10 -5 22 1','#fff',1.2,.4);
  /* tapete */
  s+=ell(160,152,120,16,'none',null,' stroke="#fff" stroke-opacity=".35" stroke-width="1.2" stroke-dasharray="2 2"')+ell(160,152,86,10,'none',null,' stroke="#000" stroke-opacity=".18" stroke-width="1.2"')+ell(160,152,50,6,'#fff',.1);
  /* sofá: volume, costuras, almofadas */
  s+=ell(155,141,92,3.4,'#000',.3)+rect(70,104,170,36,'url(#'+p+'sf)')+rect(62,98,22,42,'url(#'+p+'sf)')+rect(226,98,22,42,'url(#'+p+'sf)')+rect(82,96,70,16,'url(#'+p+'sf)')+rect(158,96,70,16,'url(#'+p+'sf)');
  s+=line('M82 112 H152 M158 112 H228','#000',1,.3)+line('M117 96 V112 M193 96 V112','#000',.8,.2)+rect(62,98,22,1.5,'#fff',.3)+rect(226,98,22,1.5,'#fff',.3)+rect(70,104,170,1.4,'#fff',.3);
  s+=rect(66,140,3,5,'#3d281b')+rect(238,140,3,5,'#3d281b');
  s+=circ(110,102,8,'none',null,' stroke="#fff" stroke-opacity=".4" stroke-width=".8"')+path('M104 99 q6 -4 12 0','none',' stroke="#000" stroke-opacity=".2" fill="none"')+circ(196,102,8,'none',null,' stroke="#fff" stroke-opacity=".35" stroke-width=".8"')+line('M190 104 L202 100 M190 101 L202 97','#fff',.8,.4);
  /* luminária: abajur aceso */
  const on=c.T.lit>.2;
  s+=rect(268.4,70,1.2,68,'#fff',.25)+path('M256 66 L282 66 L276 48 L262 48Z','#fff',.18)+path('M262 48 L276 48 L277 52 L261 52Z','#fff',.25)+ell(269,70,24,12,WARM,on?.35:.12)+ell(269,140,12,2,'#000',.25)+ell(269,139,6,1.4,'#222');
  /* planta: folhas */
  s+=pot(28,118,16,20,'#9a5a3a')+leaves(28,118,9,26,'#2E7D4F',R)+leaves(28,118,5,20,'#4CB07A',R,15)+ell(28,139,10,1.6,'#000',.25);
  /* cortina junto à janela */
  if(c.win&&!lite){const cx=c.win.x,cw=c.win.w;s+=rect(cx-9,12,10,76,'#F3E6D2',.55)+rect(cx+cw-1,12,10,76,'#F3E6D2',.55);for(let i=0;i<4;i++)s+=rect(cx-9+i*2.6,12,.8,76,'#000',.1)+rect(cx+cw-1+i*2.6,12,.8,76,'#000',.1);s+=rect(cx-12,10,cw+24,2,'#7a4a2a')}
  return {d,s};
};
IN.office=function(c,p,R){
  let d='',s='';const lite=c.lite;
  d+=lg(p+'scr',0,0,1,1,[[0,'#9CC4FF'],[1,'#3E6FD0']]);
  s+=shelfShade(214,22,80,2).replace(/SHD/g,p+'ao')+rect(214,22,80,36,'url(#'+p+'bd)',1,' opacity=".5"');
  d+=lg(p+'bd',0,0,0,1,[[0,'#fff',.12],[1,'#000',.28]]);
  /* tampo de madeira */
  s+=rect(40,104,160,1.2,'#fff',.45)+rect(40,105.2,160,2.8,'#000',.12)+line('M46 106 H190 M52 108 H196','#000',.4,.2)+ell(120,113,86,2,'#000',.22)+rect(46,112,6,34,'#000',.18)+rect(190,112,6,34,'#000',.2);
  /* monitor com brilho e conteúdo */
  s+=rect(98,80,40,22,'url(#'+p+'scr)',1,' opacity=".7"')+rect(101,84,16,2,'#fff',.6)+rect(101,88,26,1.4,'#fff',.4)+rect(101,92,20,1.4,'#fff',.4)+rect(122,84,12,10,'#fff',.3)+path('M98 102 L124 80 L132 80 L106 102Z','#fff',.16)+rect(96,78,44,1,'#fff',.3)+rect(114,106,8,2,'#555')+rect(104,108,28,2.6,'#2a2f45')+rect(105,108,26,.8,'#fff',.35);
  s+=ell(118,92,40,30,'#8FB8FF',.08*(1+c.T.lit));
  /* caneca, planta, abajur de mesa */
  s+=rect(80,96,10,8,'#E8795A')+rect(80,96,2,8,'#fff',.35)+rect(80,96,10,1.2,'#fff',.4)+path('M90 98 q4 .5 3.4 4 q-1 2 -3.4 2','none',' stroke="#c9604a" stroke-width="1.3" fill="none"')+steam(p,85,95,2,lite,.8);
  s+=pot(165,104,12,8,'#B9784F')+leaves(165,104,7,12,'#3E9A63',R);
  s+=rect(58,96,1.4,9,'#2a2f45')+path('M52 92 L66 92 L62 86 L56 86Z','#2a2f45')+path('M54 93 L64 93 L76 106 L42 106Z',WARM,c.T.lit>.4?.22:.07);
  /* livros no móvel */
  s+=rect(212,92,26,2,'#fff',.35)+rect(212,114,26,2,'#000',.25);
  return {d,s};
};
IN.classroom=function(c,p,R){
  let d='',s='';const lite=c.lite;
  d+=lg(p+'bd',0,0,0,1,[[0,'#fff',.1],[1,'#000',.28]]);
  /* lousa: giz e manchas */
  s+=rect(122,26,146,56,'url(#'+p+'bd)',1,' opacity=".6"')+rect(120,24,150,1.6,'#fff',.3)+rect(120,86,150,1.6,'#000',.3)+rect(122,81,40,1.8,'#E8DCC4')+rect(168,81,10,1.8,'#fff')+rect(182,81,8,1.8,'#E8795A');
  s+=`<text x="130" y="42" font-family="'Plus Jakarta Sans',system-ui,sans-serif" font-weight="800" font-size="9" fill="#fff" fill-opacity=".85" letter-spacing="1">A B C 1 2 3</text>`+line('M130 50 h70 M130 58 h50','#fff',1.2,.4)+ell(232,50,18,8,'#fff',.05)+ell(160,70,22,6,'#fff',.06);
  /* mesas: reflexos no tampo */
  for(let r=0;r<2;r++)for(let q=0;q<4;q++){const dx=36+q*66-(r?0:10),dy=116+r*26;s+=rect(dx,dy,44,1,'#fff',.5)+rect(dx,dy+5,44,1,'#000',.2)+ell(dx+22,dy+20,24,2,'#000',.16)}
  /* globo: continentes e brilho */
  s+=path('M283 88 q4 -4 8 -1 q3 3 -1 6 q-3 3 -6 -1Z','#3E9A63')+path('M292 98 q4 -2 5 2 q-1 4 -4 2Z','#3E9A63')+circ(286,88,5,'#fff',.2)+path('M277 94 a13 13 0 0 0 26 0','none',' stroke="#000" stroke-opacity=".22" stroke-width="3" fill="none"')+rect(289.6,104,1.6,12,'#C9CED9')+ell(290.5,116,6,1.4,'#444');
  return {d,s};
};
IN.library=function(c,p,R){
  let d='',s='';const lite=c.lite;
  d+=lg(p+'bd',0,0,0,1,[[0,'#fff',.1],[1,'#000',.3]]);
  [[10,96],[112,96],[214,96]].forEach(([x,w])=>{s+=shelfShade(x,6,w,5).replace(/SHD/g,p+'ao')+rect(x,6,w,88,'url(#'+p+'bd)',1,' opacity=".55"');
    if(!lite)for(let r=0;r<5;r++)for(let k=0;k<7;k++)s+=rect(x+4+k*13+(r%2)*3,6+r*17+4,.8,8,'#FFD98A',.55)});
  s+=rect(60,128,200,1.2,'#fff',.45)+ell(160,134,100,2,'#000',.2)+rect(150,119,24,1,'#fff',.4)+rect(176,121,18,1,'#fff',.4);
  s+=rect(214,114,12,10,'#222',.5)+path('M208 112 L232 112 L226 100 L214 100Z','#2a6b4a')+ell(220,126,28,10,WARM,.3+c.T.lit*.3)+rect(219.4,114,1.2,12,'#C9A24B');
  return {d,s};
};
IN.shop=function(c,p,R){
  let d='',s='';const lite=c.lite;
  d+=lg(p+'bd',0,0,0,1,[[0,'#fff',.1],[1,'#000',.28]]);
  [[14,120],[186,120]].forEach(([x,w])=>{s+=shelfShade(x,20,w,4).replace(/SHD/g,p+'ao')+rect(x,20,w,70,'url(#'+p+'bd)',1,' opacity=".5"');if(!lite)for(let i=0;i<14;i++)s+=rect(x+6+i*8,26+(i%4)*17,5,2.4,'#fff',.8)});
  s+=rect(0,124,W,1.4,'#fff',.45)+rect(0,131,W,2,'#000',.22)+ell(160,148,160,2,'#000',.12);
  s+=rect(40,108,26,2,'#fff',.4)+rect(250,106,30,1.4,'#fff',.4)+path('M130 0 L190 0 L184 14 L136 14Z','#fff',.1)+path('M140 3 L146 3 L142 12 L137 12Z','#fff',.2);
  return {d,s};
};
IN.hall=function(c,p,R){
  let d='',s='';const lite=c.lite;
  d+=lg(p+'col',0,0,1,0,[[0,'#000',.2],[.3,'#fff',.22],[.7,'#000',0],[1,'#000',.3]]);
  [[24],[90],[230],[296]].forEach(([cx])=>{s+=rect(cx-8,0,16,c.horizon,'url(#'+p+'col)')+ell(cx,c.horizon-4,11,2,'#000',.3)+rect(cx-9.5,c.horizon-12,19,2,'#fff',.4)+rect(cx-9.5,0,19,6,'#000',.12);
  });
  s+=rect(90,122,140,1.4,'#fff',.5)+rect(90,128,140,26,'#000',.12)+rect(0,c.horizon,W,3,'url(#'+p+'ao)');
  s+=pot(52,118,12,8,'#9a5a3a')+leaves(52,106,7,14,'#2E7D4F',R)+pot(272,118,12,8,'#9a5a3a')+leaves(272,106,7,14,'#2E7D4F',R);
  return {d,s};
};
IN.clinic=function(c,p,R){
  let d='',s='';
  s+=rect(197,27,38,38,'#fff',.3)+ell(216,46,34,24,'#fff',.07)+rect(40,100,100,1.6,'#fff',.7)+ell(90,134,50,3,'#000',.15)+rect(0,c.horizon,W,H-c.horizon,'url(#'+p+'ao2)')+path('M0 112 H320 V116 H0Z','url(#'+p+'ao)');
  d+=lg(p+'ao2',0,0,0,1,[[0,'#fff',.2],[1,'#000',.12]]);
  if(!c.lite)for(let i=0;i<5;i++)s+=rect(0,130+i*8,W,.6,'#000',.1);
  return {d,s};
};
IN.gym=function(c,p,R){let s='';s+=rect(0,c.horizon,W,H-c.horizon,'url(#'+p+'ao2)');for(let i=0;i<5;i++){const x=30+i*50;s+=ell(x+6,126,22,1.4,'#000',.2)+rect(x-6,117,22,1,'#fff',.4)}return {d:lg(p+'ao2',0,0,0,1,[[0,'#fff',.14],[1,'#000',.18]]),s}};
IN.ballroom=function(c,p,R){let s='',d='';d+=rg(p+'bk',[[0,'#fff',.45],[.8,'#fff',.3],[1,'#fff',0]]);for(let i=0;i<(c.lite?7:14);i++){const r=3+R()*6;s+=circ(R()*W,R()*100,r,'url(#'+p+'bk)',.5)}
  s+=path('M160 24 L40 172 L120 172Z','#FFE9A8',.07)+path('M160 24 L200 172 L290 172Z','#FFE9A8',.06);return {d,s}};
IN.cinema=function(c,p,R){let s='',d='';d+=lg(p+'bm',0,0,1,0,[[0,'#BFD4FF',.3],[1,'#BFD4FF',0]]);s+=path('M158 8 L50 60 L50 100 L270 100 L270 60Z','#DDE8FF',.12)+rect(158,6,4,4,'#fff',.9);
  if(!c.lite)for(let i=0;i<26;i++)s+=circ(70+R()*180,16+R()*70,.6,'#fff',.6);return {d,s}};
IN.museum=function(c,p,R){let s='',d='';[[30,26,60,44],[120,22,76,54],[228,28,56,42]].forEach(([fx,fy,fw,fh])=>{s+=rect(fx+3,fy+fh+4,fw,3,'#000',.18)+path(`M${fx} ${fy+fh} L${fx+fw*.4} ${fy} L${fx+fw*.55} ${fy} L${fx+fw*.15} ${fy+fh}Z`,'#fff',.16)+path(`M${fx-8} 0 L${fx+fw+8} 0 L${fx+fw*.9} ${fy-4} L${fx+fw*.1} ${fy-4}Z`,'#FFE9B8',.1)+rect(fx+fw/2-6,fy+fh+8,12,3,'#fff',.35)});
  s+=rect(0,c.horizon,W,H-c.horizon,'url(#'+p+'ao2)')+ell(166,134,60,3,'#000',.18);d+=lg(p+'ao2',0,0,0,1,[[0,'#fff',.2],[1,'#000',.16]]);return {d,s}};
IN.subwaycar=function(c,p,R){let s='';for(let i=0;i<3;i++){const x=14+i*104;s+=path(`M${x+6} 82 L${x+36} 40 L${x+46} 40 L${x+16} 82Z`,'#fff',.14);for(let k=0;k<8;k++)s+=rect(x+6,44+k*5,76,.8,'#FFD98A',.16)}
  s+=rect(0,100,W,70,'url(#'+p+'ao2)')+rect(100,0,1,172,'#fff',.6)+rect(210,0,1,172,'#fff',.6);return {d:lg(p+'ao2',0,0,0,1,[[0,'#fff',.2],[1,'#000',.2]]),s}};

function interiorPre(c){
  const p=c.id+'x',R=rng(hash(c.seed+'pr')),lite=c.lite,tm=c.tm,hz=c.horizon||112,win=c.win,v=c.cl.v,key=KEY[tm]||'#fff',I=INT[tm]||.5;
  c.key=key;c.I=I;
  let d='',s='';
  d+=lg(p+'ao',0,0,0,1,[[0,'#000',.3],[1,'#000',0]])+lg(p+'wa',0,0,1,0,[[0,'#000',.26],[.2,'#000',0],[.8,'#000',0],[1,'#000',.3]])+lg(p+'ce',0,0,0,1,[[0,'#000',.3],[.4,'#000',0]])+lg(p+'sh',0,1,.6,0,[[0,'#fff',.34],[1,'#fff',0]])+lg(p+'hz',0,0,0,1,[[0,c.T.b,0],[1,c.T.b,.45]])+lg(p+'ds',0,0,0,1,[[0,'#000',.32],[1,'#000',0]])+lg(p+'wb',0,0,0,1,[[0,'#000',.3],[1,'#000',0]]);
  const fb=FB[v]||H;
  s+=rect(0,0,W,hz,'url(#'+p+'wa)')+rect(0,0,W,hz*.5,'url(#'+p+'ce)');
  if(!lite){d+=`<pattern id="${p}chk" width="9" height="9" patternUnits="userSpaceOnUse"><circle cx="2" cy="3" r=".5" fill="#fff" fill-opacity=".08"/><circle cx="6.5" cy="7" r=".4" fill="#fff" fill-opacity=".06"/></pattern>`;s+=rect(0,0,W,hz,'url(#'+p+'chk)')}
  if(win){
    const wx=win.x,wy=win.y,ww=win.w,wh=win.h,dx=-c.ld;
    d+=`<clipPath id="${p}wk"><rect x="${wx}" y="${wy}" width="${ww}" height="${wh}"/></clipPath><clipPath id="${p}fk"><rect x="0" y="${hz}" width="${W}" height="${fb-hz}"/></clipPath>`+lg(p+'fp',0,0,0,1,[[0,key,.46*I+.06],[1,key,.1*I]]);
    s+=`<g clip-path="url(#${p}wk)">${rect(wx,wy+wh*.6,ww,wh*.4,'url(#'+p+'hz)',.6)}<path d="M${wx-4} ${wy+wh} L${wx+ww*.32} ${wy} L${wx+ww*.5} ${wy} L${wx+ww*.1} ${wy+wh}Z" fill="url(#${p}sh)"/><path d="M${wx+ww*.58} ${wy+wh} L${wx+ww*.82} ${wy} L${wx+ww*.9} ${wy} L${wx+ww*.66} ${wy+wh}Z" fill="#fff" fill-opacity=".1"/>${rect(wx,wy,ww,6,'url(#'+p+'wb)')}${rect(wx,wy,5,wh,'url(#'+p+'wb)',1,' opacity=".6"')}</g>`;
    s+=line(`M${wx-4.8} ${wy+wh+4.6} V${wy-4.6} H${wx+ww+4.8}`,'#fff',.8,.7)+line(`M${wx+ww+4.8} ${wy-4.6} V${wy+wh+4.6} H${wx-4.8}`,'#000',.8,.2)+rect(wx-5,wy+wh+6,ww+10,9,'url(#'+p+'ds)',1,' opacity=".7"');
    s+=ell(wx+ww/2,wy+wh/2,ww*1.05,wh*1.1,key,.07*I+.02);
    const x0=wx+ww*.04+dx*22,x1=wx+ww*.96+dx*22,b0=wx-ww*.15+dx*80,b1=wx+ww*1.15+dx*110;
    s+=`<g clip-path="url(#${p}fk)">`+path(`M${n1(x0)} ${hz+3} L${n1(x1)} ${hz+3} L${n1(b1)} ${fb+10} L${n1(b0)} ${fb+10}Z`,'url(#'+p+'fp)')+path(`M${n1((x0+x1)/2-1)} ${hz+3} L${n1((x0+x1)/2+1)} ${hz+3} L${n1((b0+b1)/2+5)} ${fb+10} L${n1((b0+b1)/2-5)} ${fb+10}Z`,'#000',.1)+`</g>`;
    if(!lite){for(let i=0;i<14;i++){const t=R(),u=R(),px=wx+ww*.1+t*ww*.8+dx*u*70,py=wy+wh+u*(hz-wy-wh+36);if(py<hz+2)s+=circ(px,py,.4+R()*.5,'#fff',.4,` class="${p}dm"`)}}
  }
  s+=rect(0,hz-1,W,9,'url(#'+p+'ao)')+rect(0,hz+7,W,2,'#fff',.05);
  if(c.T.lit>.3&&!win)s+=ell(160,20,150,60,WARM,.08);
  const css=lite?'':`<style>@media (prefers-reduced-motion:no-preference){.${p}st{animation:${p}up 4.2s ease-in-out infinite;transform-box:fill-box}.${p}dm{animation:${p}dr 9s ease-in-out infinite alternate}}@keyframes ${p}up{0%{opacity:0;transform:translateY(3px)}40%{opacity:1}100%{opacity:0;transform:translateY(-5px)}}@keyframes ${p}dr{from{transform:translate(0,0)}to{transform:translate(3px,5px)}}</style>`;
  return css+`<defs>${d}</defs>`+s;
}
function interiorBack(c,p,R){
  const lite=c.lite,hz=c.horizon,v=c.cl.v;
  let d='',s='';
  const f=IN[v];
  if(f){const r=f(c,p,R);d+=r.d;s+=r.s}
  const fb=FB[v]||H;
  if(!lite&&fb>=H-1&&v!=='hall'){for(let i=0;i<8;i++){const y=hz+8+i*i*.9+i*3;s+=rect(0,y,W,.6,'#000',.09)}}
  return `<defs>${d}</defs>${s}`;
}

/* ================== EXTERIORES ================== */
const CITY=new Set('street plaza madrid paris lisboa sampa brasilia pelourinho market'.split(' '));
function exteriorBack(c,p,R){
  const lite=c.lite,tm=c.tm,T=c.T,key=c.key,I=c.I,v=c.cl.v,hz=c.horizon||108,sun=c.sun||{x:200,y:40},ld=c.ld;
  let d='',s='';
  d+=lg(p+'hz',0,0,0,1,[[0,T.b,0],[.5,T.b,.5],[1,T.b,0]])+rg(p+'sb',[[0,key,.5*I+.1],[1,key,0]])+lg(p+'ao',0,0,0,1,[[0,'#000',.3],[1,'#000',0]])+lg(p+'rf',0,0,0,1,[[0,WARM,.5],[1,WARM,0]])+lg(p+'sd',0,0,0,1,[[0,'#0a0e2a',.34],[1,'#0a0e2a',.04]]);
  /* névoa de profundidade no horizonte */
  s+=rect(0,hz-30,W,50,'url(#'+p+'hz)',tm==='night'?.4:.6);
  /* brilho do sol/lua sobre a cena */
  s+=circ(sun.x,sun.y+(tm==='day'?0:14),150,'url(#'+p+'sb)',tm==='night'?.5:1);
  const city=CITY.has(v);
  if(city){
    /* sombras projetadas atravessando a rua (direção oposta ao sol) */
    if(tm!=='night'){const a=tm==='day'?.16:.3,sk=-ld*(tm==='day'?28:70);
      for(let i=0;i<3;i++){const x=40+i*86+R()*20,wd=26+R()*24;s+=path(`M${n1(x)} ${hz+11} L${n1(x+wd)} ${hz+11} L${n1(x+wd*2.6+sk)} ${H} L${n1(x*1.6-110+sk)} ${H}Z`,'url(#'+p+'sd)',1,` opacity="${a*3}"`)}}
    /* faixa de pedestres e meio-fio */
    s+=path(`M70 ${H-7} L250 ${H-7} L262 ${H-1} L58 ${H-1}Z`,'#fff',.0);
    for(let i=0;i<7;i++){const x=22+i*40;s+=path(`M${x} ${H-14} L${x+20} ${H-14} L${x+26} ${H-2} L${x-6} ${H-2}Z`,'#fff',.3)}
    /* cabos e luzinhas entre os postes */
    s+=line(`M52 ${H-64} Q160 ${H-44} 268 ${H-64}`,'#10142a',.7,.55);
    const nl=(v==='plaza'||v==='lisboa'||v==='pelourinho'||v==='market')?9:5;
    for(let i=1;i<=nl;i++){const t=i/(nl+1),x=52+t*216,y=(H-64)*(1-t)*(1-t)*0+((1-t)*(1-t)*(H-64)+2*t*(1-t)*(H-44)+t*t*(H-64));
      if(nl>5&&tm!=='night'&&tm!=='dusk')s+=path(`M${n1(x-3)} ${n1(y)} L${n1(x+3)} ${n1(y)} L${n1(x)} ${n1(y+7)}Z`,['#E8795A','#F4C26B','#4C7FD6','#9CCB86','#C99BD6'][i%5]);
      else s+=circ(x,y+1.4,1.3,'#FFE6A8',.95)+(lite?'':circ(x,y+1.4,5,'#FFE6A8',.3))}
    /* reflexos na rua molhada / vitrines (noite, entardecer) */
    if(T.lit>.4){[52,268,110,210].forEach((x,i)=>{s+=rect(x-6,hz+16,12,H-hz-16,'url(#'+p+'rf)',i<2?.55:.3)});s+=rect(0,hz+12,W,H-hz-12,'#fff',.03)}
    if(!lite)for(let i=0;i<24;i++)s+=circ(R()*W,hz+16+R()*(H-hz-20),.5,'#fff',.14);
  }else if(v==='park'||v==='amazonia'||v==='snowy'||v==='sertao'){
    /* feixes de luz entre as árvores, névoa em camadas */
    if(tm!=='night'&&v!=='snowy')for(let i=0;i<3;i++){const x=sun.x-40+i*34;s+=path(`M${n1(sun.x)} ${Math.max(0,sun.y-4)} L${n1(x+10)} ${H} L${n1(x+34)} ${H}Z`,key,.08*I*2+.02)}
    s+=rect(0,hz+4,W,16,'url(#'+p+'hz)',.7);
    /* capim e flores no primeiro plano */
    const gc=v==='snowy'?'#CFE3F2':v==='sertao'?'#B9923A':'#2F7A48';
    for(let i=0;i<(lite?14:34);i++){const x=R()*W,y=H-R()*16-1,h2=6+R()*12,lean=(R()-.5)*7;s+=line(`M${n1(x)} ${n1(y)} q${n1(lean*.4)} ${-h2*.5} ${n1(lean)} ${-h2}`,mix(gc,i%3?'#000':'#fff',.2),1.1,.9)}
    if(v==='park'||v==='amazonia')for(let i=0;i<7;i++){const x=R()*W,y=H-3-R()*9;s+=circ(x,y,1.4,['#fff','#F4C26B','#E8795A','#C99BD6'][i%4],.95)}
  }else if(v==='beach'||v==='ipanema'||v==='harbor'){
    /* trilha de brilho do sol na água, espuma */
    const wy=hz+2;
    for(let i=0;i<(lite?9:16);i++){const t=i/16,y=wy+4+t*(v==='harbor'?H-wy-30:40),wd=4+t*26;s+=rect(sun.x-wd/2+(R()-.5)*8,y,wd,1+t,tm==='night'?'#cfd8ff':key,.55-t*.3)}
    s+=rect(0,wy,W,6,'url(#'+p+'hz)',.8);
    if(v!=='harbor'){const sy=H-44;s+=path(`M0 ${sy+6} Q80 ${sy-2} 170 ${sy+4} T${W} ${sy} L${W} ${sy+4} Q250 ${sy+8} 170 ${sy+8} T0 ${sy+10}Z`,'#fff',.55)+line(`M0 ${sy+9} Q80 ${sy+3} 170 ${sy+9} T${W} ${sy+4}`,'#fff',.7,.6);
      s+=rect(0,sy+10,W,H-sy-10,'#000',.0)+rect(0,H-60,W,60,'url(#'+p+'ao)',1,' transform="rotate(180 160 142)" opacity=".5"')}
    else{s+=rect(0,H-26,W,3,'#fff',.35)+rect(0,H-23,W,2,'#000',.2)}
  }else if(v==='station'||v==='airport'){
    s+=rect(0,hz+10,W,H-hz-10,'url(#'+p+'rf)',.18);
    for(let i=0;i<7;i++){const x=i*50-10;s+=path(`M${x} ${H} L${n1(x+22)} ${H} L${n1(160+(x-160)*.3+4)} ${hz+20} L${n1(160+(x-160)*.3)} ${hz+20}Z`,'#fff',.06)}
    s+=rect(0,H-18,W,2,'#F4C26B',.8)+rect(0,H-14,W,5,'#000',.12);
    if(v==='airport')for(let i=0;i<9;i++){const t=i/9;s+=circ(160+(i-4)*(8+t*22),hz+26+t*30,1.2+t*1.6,'#FFE6A8',.9)}
  }else if(v==='stadium'){
    for(let i=0;i<2;i++){const x=50+i*220;s+=circ(x,hz-30,18,'url(#'+p+'sb)',1)+circ(x,hz-30,2.4,'#fff')}
    s+=path(`M0 ${H} L${W} ${H} L${W} ${H-30} L0 ${H-30}Z`,'url(#'+p+'ao)',.4)
  }
  /* bokeh: luzes desfocadas ao fundo (entardecer/noite) */
  if(T.lit>.4){d+=rg(p+'bk',[[0,'#FFE6A8',.5],[.8,'#FFD98A',.4],[1,'#FFD98A',0]]);const n=lite?5:10;for(let i=0;i<n;i++){const r=3+R()*6;s+=circ(R()*W,hz-26+R()*34,r,'url(#'+p+'bk)',.5)}}
  return `<defs>${d}</defs>${s}`;
}

/* ================== API ================== */
function prep(c){
  c.key=KEY[c.tm]||'#fff';c.I=INT[c.tm]||.5;
  c.horizon=c.horizon||(c.cl.mode==='in'?112:108);
  return 'sc'+hash(c.seed+'fx')+'_';
}
function back(c){
  if(!c||!c.cl)return '';
  c.key=KEY[c.tm]||'#fff';c.I=INT[c.tm]||.5;
  const p=c.id+'x',R=rng(hash(c.seed+'fx'));
  return c.cl.mode==='in'?interiorBack(c,p,R):exteriorBack(c,p,R);
}
function front(c){
  if(!c)return '';
  const p=c.id+'x',tm=c.tm,lite=c.lite,R=rng(hash(c.seed+'ft'));
  let d='',s='';
  const g=GRADE[tm];
  if(g)s+=rect(0,0,W,H,g[0],g[1]);
  /* luz quente de entrada vinda da janela / sol sobre tudo */
  const sx=c.win?c.win.x+c.win.w/2:(c.sun?c.sun.x:60),key=KEY[tm]||'#fff',I=INT[tm]||.5;
  d+=rg(p+'lg',[[0,key,.3*I],[1,key,0]]);
  s+=ell(sx,c.cl.mode==='in'?30:(c.sun?c.sun.y:30),190,120,'url(#'+p+'lg)');
  /* folhagem desfocada em primeiro plano (profundidade de campo), só no canto superior */
  const showLeaf=(hash(c.seed)>>3)%3!==0,leafSide=(hash(c.seed)&1)?1:0,lx=leafSide?W+4:-4,dir=leafSide?-1:1,col=c.cl.mode==='in'?'#2c5a3a':'#1d4a2c';
  d+=rg(p+'lf',[[0,mix(col,'#fff',.2),.95],[1,col,.9]]);
  let lv='';for(let i=0;i<(lite?3:6);i++){const r=14+R()*14;lv+=ell(lx+dir*(8+i*7),-2+i*3.4+R()*3,r,r*.3,'url(#'+p+'lf)',1,` transform="rotate(${n1(dir*(28+i*9))} ${n1(lx+dir*(8+i*7))} ${n1(-2+i*3.4)})"`)}
  if(!showLeaf){}
  else if(lite)s+=`<g opacity=".55">${lv}</g>`;
  else{d+=`<filter id="${p}bl" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="2.6"/></filter>`;s+=`<g filter="url(#${p}bl)" opacity=".75">${lv}</g>`}
  /* grão de filme (só versão completa) */
  if(!lite){d+=`<filter id="${p}gr" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="${hash(c.seed)%97}"/><feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .9 -.4"/></filter>`;s+=`<rect width="${W}" height="${H}" filter="url(#${p}gr)" opacity=".1"/>`}
  /* brilho nas bordas (halation) para noite/entardecer */
  if(tm==='night'||tm==='dusk')s+=rect(0,H-40,W,40,'#000',.12);
  return `<defs>${d}</defs>${s}`;
}
/* mão segurando a caneca (café, restaurante, cozinha, loja), com antebraço saindo da borda inferior */
function hands(c){
  if(!c||!c.chars||!c.chars.length||c.cl.mode!=='in'||!/^(cafe|restaurant|kitchen|shop)$/.test(c.cl.v))return '';
  const ch=c.chars[c.chars.length-1],o=ch.o||{},k=ch.k,p=c.id+'x';
  const sk=o.skinOut||'#E2B08A',sd=mix(sk,'#4a1f12',.42),sl=mix(sk,'#fff',.2),sh=o.shirtOut||'#4C7FD6';
  const side=(hash(c.seed)&1)?1:-1,cx=ch.x+50*ch.k+side*24*ch.k,cy=H-25;
  const mug=['#E8795A','#2E8B7A','#E3A93B','#4C7FD6','#C0392B'][hash(c.seed+'m')%5],md=mix(mug,'#000',.3);
  let s=`<defs>${lg(p+'hc',0,0,1,0,[[0,mix(mug,'#fff',.3)],[.45,mug],[1,md]])}</defs><g transform="translate(${n1(cx)} ${cy})">`;
  s+=path(`M${side*2} 34 L${side*4} 8 Q${side*10} 5 ${side*15} 9 L${side*18} 34Z`,sh)+path(`M${side*4} 8 Q${side*10} 5 ${side*15} 9 L${side*15} 13 Q${side*10} 10 ${side*4} 12Z`,mix(sh,'#000',.3),.5)+path(`M${side*2} 34 L${side*4} 8 L${side*7} 9 L${side*6} 34Z`,'#fff',.14);
  s+=ell(0,13,13,2.6,'#000',.25)+path('M-9 -10 L9 -10 L7.6 12 Q0 14.6 -7.6 12Z','url(#'+p+'hc)')+ell(0,-10,9,2.5,mix(mug,'#fff',.55))+ell(0,-10,7.6,1.9,'#3a1d0e')+ell(-1.8,-10.4,3.4,.7,'#b07a48',.8)+rect(-7,-8,1.5,17,'#fff',.4);
  s+=path('M8.4 -6 q6.4 .6 5.6 6.4 q-.8 4.4 -6.6 4.4','none',' stroke="'+md+'" stroke-width="2.2" fill="none" stroke-linecap="round"');
  for(let i=0;i<4;i++){const y=-3+i*4.6,x=-side*(.4+i*.4);s+=`<ellipse cx="${n1(x)}" cy="${n1(y)}" rx="9.2" ry="2.8" fill="${sk}" transform="rotate(${-side*6} ${n1(x)} ${n1(y)})"/><path d="M${n1(x-8)} ${n1(y-1.3)} Q${n1(x)} ${n1(y-2.8)} ${n1(x+8)} ${n1(y-1.3)}" stroke="${sl}" stroke-opacity=".8" stroke-width=".9" fill="none" stroke-linecap="round"/><path d="M${n1(x-7)} ${n1(y+2)} Q${n1(x)} ${n1(y+3.4)} ${n1(x+7)} ${n1(y+2)}" stroke="${sd}" stroke-opacity=".7" stroke-width=".8" fill="none" stroke-linecap="round"/><ellipse cx="${n1(x+side*7.4)}" cy="${n1(y-.6)}" rx="1.6" ry="1.9" fill="${sk}"/><ellipse cx="${n1(x+side*8)}" cy="${n1(y-.9)}" rx=".9" ry="1" fill="${sl}"/>`}
  s+=path(`M${-side*9.6} 7 Q${-side*13.4} -1 ${-side*10.6} -10 Q${-side*6.5} -7 ${-side*8} 3Z`,sk)+path(`M${-side*10.6} -10 Q${-side*9} -8 ${-side*8.4} -5`,'none',' stroke="'+sd+'" stroke-opacity=".6" stroke-width=".8"');
  s+=`</g>`;
  if(o.grade){const G=o.grade,cache={};s=s.replace(/#[0-9a-fA-F]{6}\b/g,m=>cache[m]||(cache[m]=mix(m,G.c,G.k)))}
  return s+(c.lite?'':steam(p,cx,cy-12,3,false,1.2));
}
w.PogSceneFX={pre:function(c){return c&&c.cl&&c.cl.mode==='in'?interiorPre(c):''},back,front,hands,version:1};
})(window);
