/* Pogglot · capas ilustradas (cenas em camadas): céu, luz, prédios, ambientes e pessoas, geradas em SVG a partir do cenário do episódio.
   Substitui as miniaturas de ícones: PogCover.svg (capa larga) e PogCover.work (pôster vertical) passam a usar estas cenas. */
(function(){
'use strict';
const W=320,H=172;
const hash=s=>{let h=2166136261;s=String(s);for(let i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619)}return h>>>0};
const rng=seed=>{let a=seed>>>0||1;return()=>{a^=a<<13;a>>>=0;a^=a>>>17;a^=a<<5;a>>>=0;return a/4294967296}};
const hx=h=>{if(h.length===4)h='#'+h[1]+h[1]+h[2]+h[2]+h[3]+h[3];return [parseInt(h.slice(1,3),16),parseInt(h.slice(3,5),16),parseInt(h.slice(5,7),16)]};
const mix=(a,b,k)=>{const x=hx(a),y=hx(b);return '#'+x.map((v,i)=>Math.round(v+(y[i]-v)*k).toString(16).padStart(2,'0')).join('')};
const n1=v=>(Math.round(v*10)/10);
const pick=(R,a)=>a[Math.floor(R()*a.length)%a.length];
const esc=s=>String(s==null?'':s).replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]));
let UID=0;
const rect=(x,y,w,h,f,x2)=>`<rect x="${n1(x)}" y="${n1(y)}" width="${n1(w)}" height="${n1(h)}" fill="${f}"${x2||''}/>`;
const circ=(x,y,r,f,x2)=>`<circle cx="${n1(x)}" cy="${n1(y)}" r="${n1(r)}" fill="${f}"${x2||''}/>`;
const ell=(x,y,rx,ry,f,x2)=>`<ellipse cx="${n1(x)}" cy="${n1(y)}" rx="${n1(rx)}" ry="${n1(ry)}" fill="${f}"${x2||''}/>`;
const path=(d,f,x2)=>`<path d="${d}" fill="${f}"${x2||''}/>`;

/* ---------- horários do dia ---------- */
const TM={
 dawn:{t:'#5D70D8',m:'#F2A7C3',b:'#FFE2B8',sun:'#FFF3CE',amb:'#FFB38C',far:'#8E86BE',near:'#6A5F9C',lit:.2,wall:.0},
 day:{t:'#3B8BE0',m:'#8CC6F4',b:'#E3F3FF',sun:'#FFFFFF',amb:'#FFF6DD',far:'#A9BCD8',near:'#7F98BC',lit:0,wall:.0},
 golden:{t:'#3A58A4',m:'#F3A368',b:'#FFDB93',sun:'#FFF2C2',amb:'#FFB45A',far:'#A98AA6',near:'#7C5D86',lit:.25,wall:.08},
 dusk:{t:'#252965',m:'#C2507A',b:'#FFB078',sun:'#FFD6A4',amb:'#FF8E6B',far:'#6B5590',near:'#463A72',lit:.65,wall:.18},
 night:{t:'#060C2C',m:'#1A2966',b:'#44579C',sun:'#F6F3DC',amb:'#7FA0FF',far:'#34437C',near:'#222C5C',lit:1,wall:.35}
};
const DAYPICK=['day','day','golden','dawn','golden','day','dusk'];
const NIGHTY={party:1,ballroom:1,boteco:1,cinema:1,carnaval:'dusk',junina:'dusk',diner:'golden',stadium:'golden'};
/* ---------- classificação do cenário ---------- */
const INT=new Set('cafe counter diner restaurant boteco pizzeria kitchen cocina living home bedroom bath vecindad office studio classroom school library clinic hospital hall lobby ballroom party gym shop cinema museum subwaycar'.split(' '));
const ALIAS={counter:'cafe',pizzeria:'restaurant',diner:'restaurant',boteco:'restaurant',cocina:'kitchen',home:'living',vecindad:'living',bedroom:'living',bath:'living',studio:'office',school:'classroom',hospital:'clinic',lobby:'hall',party:'ballroom'};
const EXTV=new Set('plaza street city sampa brasilia rioantigo pelourinho lisboa madrid paris station railway airport bridge rainycity stadium road yard market harbor beach ipanema carnaval outdoors park sitio sertao amazonia snowy junina vila'.split(' '));
const EXALIAS={city:'street',rainycity:'street',road:'street',yard:'plaza',bridge:'harbor',railway:'station',outdoors:'park',sitio:'park',vila:'plaza',carnaval:'plaza',junina:'plaza',rioantigo:'pelourinho'};
function classify(sc,R){
  sc=String(sc||'').toLowerCase();
  if(INT.has(sc))return{mode:'in',v:ALIAS[sc]||sc,raw:sc};
  if(EXTV.has(sc))return{mode:'ex',v:EXALIAS[sc]||sc,raw:sc};
  return R()<.5?{mode:'in',v:'cafe',raw:''}:{mode:'ex',v:'plaza',raw:''};
}
/* ---------- peças ---------- */
function stars(R,n){let s='';for(let i=0;i<n;i++)s+=circ(R()*W,R()*70,.4+R()*.8,'#fff',` fill-opacity="${n1(.4+R()*.6)}"`);return s}
function cloud(x,y,sc,col,op){return `<g fill="${col}" fill-opacity="${op}" transform="translate(${n1(x)} ${n1(y)}) scale(${sc})"><ellipse cx="0" cy="0" rx="26" ry="7"/><ellipse cx="-12" cy="-6" rx="14" ry="9"/><ellipse cx="8" cy="-9" rx="16" ry="11"/></g>`}
function windowsGrid(R,x,y,w,h,lit,cols,rows,warm){
  let s='';const cw=w/cols,ch=h/rows;
  for(let i=0;i<cols;i++)for(let j=0;j<rows;j++){
    const on=R()<lit,fx=x+i*cw+cw*.2,fy=y+j*ch+ch*.2;
    s+=rect(fx,fy,cw*.55,ch*.55,on?warm:'#000',on?'':' fill-opacity=".16"');
  }
  return s;
}
function building(R,x,y,w,h,col,T,o){
  o=o||{};const dark=mix(col,'#000',.28),light=mix(col,'#fff',.14);
  let s=rect(x,y,w,h,col)+rect(x+w*.72,y,w*.28,h,dark,' fill-opacity=".55"')+rect(x,y,w*.08,h,light,' fill-opacity=".5"');
  const roof=o.roof==null?Math.floor(R()*4):o.roof;
  if(roof===1)s+=path(`M${n1(x-1)} ${n1(y)}L${n1(x+w/2)} ${n1(y-w*.32)}L${n1(x+w+1)} ${n1(y)}Z`,o.roofCol||mix(col,'#7a2d1e',.55));
  else if(roof===2){s+=rect(x+w*.35,y-h*.1,w*.3,h*.1,dark)+rect(x+w*.47,y-h*.18,w*.06,h*.08,dark)}
  else if(roof===3)s+=rect(x-1,y-2.2,w+2,2.4,mix(col,'#000',.35));
  const cols=Math.max(2,Math.floor(w/9)),rows=Math.max(2,Math.floor(h/12));
  if(!o.nowin)s+=windowsGrid(R,x+w*.08,y+h*.08,w*.78,h*.78,Math.max(.12,T.lit*.85),cols,rows,'#FFD98A');
  return s;
}
function skylineRow(R,y,minH,maxH,minW,maxW,cols,T,o){
  let s='',x=-6;
  while(x<W+6){const w=minW+R()*(maxW-minW),h=minH+R()*(maxH-minH),c=cols[Math.floor(R()*cols.length)];s+=building(R,x,y-h,w,h+2,c,T,o);x+=w+(o&&o.gap!=null?o.gap:R()*3)}
  return s;
}
function tree(R,x,y,s,col,T){const d=mix(col,'#000',.3);return `<g transform="translate(${n1(x)} ${n1(y)}) scale(${s})">${rect(-1.6,-12,3.2,13,'#5b3d2a')}${circ(0,-20,11,d)}${circ(-7,-15,8,col)}${circ(7,-15,8,col)}${circ(0,-24,9,mix(col,'#fff',.1))}</g>`}
function palm(R,x,y,s,T){let f='';for(let i=0;i<7;i++){const a=-160+i*50,c=Math.cos(a*Math.PI/180),sn=Math.sin(a*Math.PI/180);f+=`<path d="M0 -34 Q ${n1(c*16)} ${n1(-34+sn*12-8)} ${n1(c*30)} ${n1(-34+sn*18+6)}" stroke="#2E7D4F" stroke-width="3.4" fill="none" stroke-linecap="round"/>`}
  return `<g transform="translate(${n1(x)} ${n1(y)}) scale(${s})"><path d="M-1.5 0 Q 3 -18 0 -34 L2.5 -34 Q 6 -18 2 0Z" fill="#7a5638"/>${f}${circ(0,-33,2.4,'#6b4a2f')}</g>`}
function person(R,x,y,s,col,T){
  const skin=pick(R,['#F2C4A0','#D9A07A','#B9784F','#8D5A3B','#F6D2B4']),hair=pick(R,['#2B1B14','#4A2E1B','#1A1A22','#7B4A25','#C69552']);
  return `<g transform="translate(${n1(x)} ${n1(y)}) scale(${s})">${ell(0,0,7,1.6,'#000',' fill-opacity=".22"')}${path('M-3.6 -2 L-3 -17 L3 -17 L3.6 -2Z',mix(col,'#000',.5))}${path('M-5 -17 Q0 -23 5 -17 L5.8 -29 Q0 -32 -5.8 -29Z',col)}${circ(0,-35,4.6,skin)}${path('M-4.8 -36 Q0 -43 4.8 -36 Q3 -39 0 -39 Q-3 -39 -4.8 -36Z',hair)}</g>`;
}
function lamp(x,y,h,T,R){const on=T.lit>.3;return rect(x-.8,y-h,1.6,h,'#2a2f45')+rect(x-4,y-h-1.5,8,2.4,'#2a2f45')+(on?`<ellipse cx="${n1(x)}" cy="${n1(y-h+1)}" rx="12" ry="9" fill="url(#gl)"/>`:'')}
/* ---------- céu ---------- */
function skyBlock(R,T,tm,id,horizon){
  let s=`<rect width="${W}" height="${H}" fill="url(#${id}s)"/>`;
  const sx=40+R()*240,sy=horizon*(.22+R()*.3);
  if(tm==='night'){s+=stars(R,38)+circ(sx,sy+6,9,'#F6F3DC')+circ(sx+3,sy+4,8,'#d8d3b8',' fill-opacity=".35"')+circ(sx,sy+6,26,'url(#moonglow)')}
  else{const lowy=(tm==='golden'||tm==='dusk'||tm==='dawn')?horizon-26-R()*10:sy;s+=circ(sx,lowy,34,'url(#sunglow)')+circ(sx,lowy,(tm==='day'?9:13),T.sun)}
  if(tm!=='night'||R()<.4)for(let i=0;i<3;i++)s+=cloud(R()*W,14+R()*(horizon*.45),.7+R()*.9,tm==='night'?'#7b8cc8':(tm==='day'?'#fff':'#fff4e6'),tm==='night'?.25:.7);
  return s;
}
function defs(id,T,tm,horizon,pal){
  return `<defs><linearGradient id="${id}s" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${T.t}"/><stop offset=".55" stop-color="${T.m}"/><stop offset="1" stop-color="${T.b}"/></linearGradient>
  <radialGradient id="sunglow"><stop offset="0" stop-color="${T.sun}" stop-opacity=".9"/><stop offset="1" stop-color="${T.sun}" stop-opacity="0"/></radialGradient>
  <radialGradient id="moonglow"><stop offset="0" stop-color="#cfd8ff" stop-opacity=".5"/><stop offset="1" stop-color="#cfd8ff" stop-opacity="0"/></radialGradient>
  <radialGradient id="gl"><stop offset="0" stop-color="#FFE6A8" stop-opacity=".9"/><stop offset="1" stop-color="#FFE6A8" stop-opacity="0"/></radialGradient>
  <linearGradient id="vg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#000" stop-opacity=".18"/><stop offset=".35" stop-color="#000" stop-opacity="0"/><stop offset=".62" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".5"/></linearGradient>
  <radialGradient id="vr" cx=".5" cy=".5" r=".75"><stop offset=".55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".32"/></radialGradient>
  <linearGradient id="ray" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="${T.amb}" stop-opacity=".42"/><stop offset="1" stop-color="${T.amb}" stop-opacity="0"/></linearGradient>
  <linearGradient id="gnd" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${mix(T.near,'#2b2f45',.5)}"/><stop offset="1" stop-color="${mix(T.near,'#12142a',.7)}"/></linearGradient></defs>`;
}
/* ---------- EXTERIORES ---------- */
const PASTEL=['#F4C26B','#E8795A','#6FB7C9','#E9A0B4','#9CCB86','#F0DFA2','#C99BD6'];
const CREAM=['#E8D9B9','#D9C49B','#EBDDC7','#C9B188','#E2CDA6'];
const COOL=['#9AA9C6','#8294B6','#B4BED6','#7487AD'];
function exterior(v,raw,R,T,tm,hint){
  const horizon=v==='beach'||v==='harbor'||v==='ipanema'?96:108;
  let s=skyBlock(R,T,tm,'a',horizon);
  const far=T.far,near=T.near;
  const hills=(y,amp,col,op)=>{let d=`M0 ${H} L0 ${y}`;for(let x=0;x<=W;x+=20)d+=` L${x} ${n1(y-Math.abs(Math.sin(x*.03+R()*2))*amp-R()*amp*.3)}`;return path(d+` L${W} ${H}Z`,col,op?` fill-opacity="${op}"`:'')};
  const mountains=(y,col,hmax)=>{let d=`M-10 ${y+20}`,x=-10;while(x<W+20){const pw=40+R()*60,ph=hmax*(.5+R()*.5);d+=` L${n1(x+pw/2)} ${n1(y-ph)} L${n1(x+pw)} ${y+10}`;x+=pw}return path(d+` L${W+20} ${H}L-10 ${H}Z`,col)};
  let ground='',mid='';
  const ALT=pick(R,[PASTEL,CREAM,COOL,['#E9B97C','#CF6A4E','#D9A441','#B5623F']]);
  const palStreet=v==='pelourinho'?PASTEL:(v==='lisboa'?PASTEL:v==='plaza'||v==='market'?ALT:(v==='madrid'||v==='paris'?CREAM:(v==='sampa'||v==='brasilia'||v==='station'||v==='street'||v==='airport'?COOL:CREAM)));
  const tint=c=>mix(c,T.near,.32+T.wall);
  const cols=palStreet.map(tint);
  if(v==='beach'||v==='ipanema'||v==='harbor'){
    s+=mountains(horizon-4,mix(far,'#000',.1),v==='ipanema'?50:30);
    if(v==='ipanema')s+=path(`M200 ${horizon+4} Q215 ${horizon-46} 232 ${horizon-44} Q250 ${horizon-30} 262 ${horizon+4}Z`,mix(far,'#000',.25));
    const wy=horizon+2;
    s+=rect(0,wy,W,H-wy,'url(#sea)')+`<linearGradient id="sea" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${mix(T.m,'#1E7FB8',.5)}"/><stop offset="1" stop-color="${mix(T.b,'#0E5C8C',.55)}"/></linearGradient>`;
    for(let i=0;i<9;i++)s+=rect(R()*W,wy+6+R()*40,18+R()*30,1.2,'#fff',' fill-opacity=".35"');
    if(v==='harbor'){
      for(let i=0;i<3;i++){const bx=40+i*105+R()*20,by=wy+24+R()*18;s+=path(`M${bx} ${by} L${bx+46} ${by} L${bx+38} ${by+9} L${bx+8} ${by+9}Z`,pick(R,['#F3F0EA','#E8795A','#F4C26B']))+rect(bx+22,by-26,1.6,26,'#3a3f55')+path(`M${bx+23.5} ${by-26} L${bx+23.5} ${by-4} L${bx+40} ${by-4}Z`,'#fff',' fill-opacity=".92"')}
      s+=rect(0,H-26,W,26,'url(#gnd)')+rect(0,H-26,W,3,'#8a8aa0',' fill-opacity=".6"');
      for(let i=0;i<6;i++)s+=rect(20+i*55,H-34,3,10,'#3a3a4f');
      s+=person(R,230,H-4,.95,pick(R,['#E8795A','#4C7FD6']),T)+person(R,252,H-3,.9,pick(R,['#F4C26B','#6FB7C9']),T);
    }else{
      const sy=H-44;s+=path(`M0 ${sy} Q80 ${sy-8} 170 ${sy-2} T${W} ${sy-6} L${W} ${H} L0 ${H}Z`,mix('#F0D9A8',T.near,.2+T.wall*.6));
      s+=palm(R,38,sy+16,1.1,T)+palm(R,284,sy+10,1.25,T)+palm(R,300,sy+22,.9,T);
      [[90,sy+14],[170,sy+22],[225,sy+12]].forEach(([ux,uy])=>{s+=path(`M${ux-14} ${uy} Q${ux} ${uy-17} ${ux+14} ${uy}Z`,pick(R,['#E8795A','#F4C26B','#4C7FD6','#fff']))+rect(ux-.7,uy,1.4,12,'#5a4a3a')});
      s+=person(R,128,H-8,1.05,'#E8795A',T)+person(R,196,H-6,.95,'#4C7FD6',T);
    }
  }else if(v==='park'||v==='amazonia'||v==='snowy'||v==='sertao'){
    const g=v==='snowy'?'#EAF2FA':v==='sertao'?'#C9A06A':'#4E9B5C';
    s+=mountains(horizon-2,mix(far,'#000',.08),v==='snowy'?56:36);
    if(v==='snowy')s+=mountains(horizon+4,'#fff',.5?28:20).replace(/fill="#fff"/,'fill="#fff" fill-opacity=".9"');
    s+=hills(horizon+6,10,mix(g,T.far,.45))+hills(horizon+26,14,mix(g,T.near,.35+T.wall*.5))+rect(0,H-40,W,40,mix(g,'#10241a',.25+T.wall*.4));
    const tcol=v==='snowy'?'#CFE3F2':v==='sertao'?'#9BA85B':'#2F7A48';
    for(let i=0;i<(v==='amazonia'?14:8);i++){const tx=R()*W,ty=horizon+22+R()*38;s+=v==='sertao'?`<g transform="translate(${n1(tx)} ${n1(ty)})">${rect(-2,-22,4,22,'#5B8A4B')}${rect(-8,-14,3,7,'#5B8A4B')}${rect(5,-17,3,8,'#5B8A4B')}</g>`:tree(R,tx,ty,.8+R()*.9,tcol,T)}
    s+=path(`M${130} ${H} Q ${160} ${H-30} ${190} ${horizon+34} L ${200} ${horizon+34} Q ${200} ${H-30} ${250} ${H}Z`,mix('#D9C39A',T.near,.3+T.wall*.5),' fill-opacity=".9"');
    s+=person(R,166,H-18,.8,'#E8795A',T)+person(R,180,H-16,.75,'#4C7FD6',T);
    if(v==='amazonia')s+=rect(0,horizon,W,H-horizon,'#0f3d2a',' fill-opacity=".18"');
  }else if(v==='station'||v==='airport'){
    s+=skylineRow(R,horizon,26,70,14,32,cols.map(c=>mix(c,T.far,.45)),T,{nowin:true});
    s+=rect(0,horizon,W,H-horizon,'url(#gnd)')+rect(0,horizon+26,W,3,'#e8e8f0',' fill-opacity=".5"');
    if(v==='station'){
      s+=rect(30,horizon-32,250,40,mix('#8d95ad',T.near,.2))+rect(30,horizon-32,250,5,'#2a2f45');
      for(let i=0;i<6;i++)s+=rect(44+i*40,horizon-22,28,18,'#FFD98A',` fill-opacity="${n1(.35+T.lit*.55)}"`)+rect(70+i*40,horizon+8,2,40,'#2a2f45');
      s+=path(`M0 ${H-18} L${W} ${H-18} L${W} ${H} L0 ${H}Z`,'#3b3f55')+rect(0,H-18,W,2,'#c9ced9',' fill-opacity=".7"');
    }else{
      s+=path(`M70 ${horizon+14} Q120 ${horizon+8} 200 ${horizon+14} L226 ${horizon+10} L200 ${horizon+20} Q130 ${horizon+26} 70 ${horizon+22}Z`,'#F4F6FA')+path(`M130 ${horizon+14} L100 ${horizon-8} L116 ${horizon-8} L156 ${horizon+14}Z`,'#DDE3EE')+rect(190,horizon-4,2.4,16,'#E8795A');
    }
    s+=person(R,60,H-10,1.1,'#E8795A',T)+person(R,92,H-8,1,'#4C7FD6',T)+lamp(250,H-4,48,T,R);
  }else if(v==='stadium'){
    s+=path(`M-10 ${horizon+6} L40 ${horizon-30} L280 ${horizon-30} L330 ${horizon+6}Z`,mix(far,'#000',.1));
    for(let i=0;i<40;i++)s+=rect(50+R()*220,horizon-28+R()*30,3,3,pick(R,['#E8795A','#F4C26B','#fff','#4C7FD6']),' fill-opacity=".8"');
    s+=rect(0,horizon+6,W,H-horizon,'#3E8F4E');for(let i=0;i<8;i++)s+=rect(0,horizon+6+i*10,W,5,'#fff',' fill-opacity=".05"');
    s+=rect(W/2-1,horizon+6,2,H-horizon,'#fff',' fill-opacity=".6"')+ell(W/2,H-50,24,10,'none',' stroke="#fff" stroke-opacity=".6" stroke-width="1.5"')+person(R,120,H-30,1,'#E8795A',T)+person(R,200,H-26,1,'#4C7FD6',T);
  }else{ /* cidade: plaza, street, madrid, paris, lisboa, sampa, brasília, pelourinho, market */
    const tall=v==='sampa'||v==='brasilia'||v==='street';
    if(hint&&hint.mount)s+=mountains(horizon-6,mix(far,'#000',.12),58)+(hint.volcano?path(`M180 ${horizon} L214 ${horizon-70} L222 ${horizon-70} L256 ${horizon}Z`,mix(far,'#000',.2)):'');
    if(hint&&hint.sea)s+=rect(0,horizon-8,W,16,mix(T.m,'#1E7FB8',.55))+rect(0,horizon-8,W,2,'#fff',' fill-opacity=".5"');
    s+=skylineRow(R,horizon-4,tall?40:22,tall?95:48,12,tall?30:24,cols.map(c=>mix(c,T.far,.55)),T,{nowin:!tall});
    if(v==='paris')s+=path(`M236 ${horizon-2} L246 ${horizon-70} L250 ${horizon-70} L260 ${horizon-2}Z`,mix(far,'#000',.35))+rect(240,horizon-40,16,2,mix(far,'#000',.35))+rect(246.5,horizon-86,3,16,mix(far,'#000',.35));
    if(v==='brasilia')s+=path(`M120 ${horizon} Q160 ${horizon-46} 200 ${horizon}Z`,mix('#fff',T.near,.2+T.wall*.5))+rect(150,horizon-30,12,30,mix('#fff',T.near,.2+T.wall*.5));
    if(v==='lisboa'||v==='plaza'||v==='pelourinho'||v==='market')s+=rect(228,horizon-60,22,60,mix('#E9D2A5',T.near,.25+T.wall))+path(`M226 ${horizon-60} L239 ${horizon-84} L252 ${horizon-60}Z`,mix('#B8523A',T.near,.25))+rect(235,horizon-52,8,14,'#000',' fill-opacity=".35"');
    s+=skylineRow(R,horizon+10,34,66,22,40,cols,T,{roof:v==='madrid'||v==='paris'?1:undefined,roofCol:mix('#5b6b86',T.near,.3)});
    s+=rect(0,horizon+10,W,H-horizon-10,'url(#gnd)');
    s+=path(`M120 ${horizon+10} L200 ${horizon+10} L${W+40} ${H} L-40 ${H}Z`,mix('#565b72',T.near,.25+T.wall*.5))+path(`M-40 ${H} L120 ${horizon+10} L112 ${horizon+10} L-60 ${H}Z`,mix('#9aa0b5',T.near,.25),' fill-opacity=".85"')+path(`M${W+40} ${H} L200 ${horizon+10} L208 ${horizon+10} L${W+60} ${H}Z`,mix('#9aa0b5',T.near,.25),' fill-opacity=".85"');
    for(let i=0;i<4;i++){const y=horizon+16+i*i*5+i*4;s+=rect(158-i*1.5,y,4+i*3,1.2+i*.7,'#fff',' fill-opacity=".55"')}
    if(v==='plaza'||v==='lisboa'||v==='pelourinho'||v==='market'){
      s+=ell(160,H-26,26,6,mix('#9aa0b5',T.near,.2))+rect(158,H-48,4,22,mix('#c9ced9',T.near,.2))+ell(160,H-48,14,3.5,mix('#c9ced9',T.near,.2),' fill-opacity=".8"')+path(`M160 ${H-52} Q150 ${H-60} 146 ${H-46} M160 ${H-52} Q170 ${H-60} 174 ${H-46}`,'none',' stroke="#bfe8ff" stroke-opacity=".8" stroke-width="1.6" stroke-linecap="round"');
      if(v==='market')[[40],[108],[214],[272]].forEach(([mx])=>{const mc=pick(R,['#E8795A','#F4C26B','#4C7FD6','#6FB7C9']);s+=path(`M${mx-22} ${H-34} L${mx+22} ${H-34} L${mx+18} ${H-46} L${mx-18} ${H-46}Z`,mc)+rect(mx-20,H-34,40,18,mix('#7a5638',T.near,.1))+[0,1,2,3].map(j=>circ(mx-14+j*9,H-37,3,pick(R,['#E8795A','#9CCB86','#F4C26B','#C99BD6']))).join('')});
    }
    s+=lamp(52,H-6,58,T,R)+lamp(268,H-6,58,T,R)+tree(R,22,H-8,1.1,'#3E8F4E',T)+tree(R,300,H-8,1.2,'#3E8F4E',T)+person(R,98,H-12,1.05,'#E8795A',T)+person(R,121,H-10,.98,'#4C7FD6',T)+person(R,204,H-14,1.02,'#F4C26B',T);
    if(v==='street'||v==='sampa'||v==='madrid'||v==='paris')s+=`<g transform="translate(${n1(150+R()*20)} ${H-8})">${rect(-14,-9,28,8,pick(R,['#E8795A','#F4C26B','#4C7FD6']))}${rect(-9,-15,18,7,mix('#9bb8d8',T.near,.1))}${circ(-8,-1,3,'#111')}${circ(8,-1,3,'#111')}${T.lit>.3?ell(16,-4,10,4,'url(#gl)'):''}</g>`;
  }
  if(tm==='dusk'||tm==='night')s=s.replace(/<\/?$/,'');
  return{svg:s,horizon};
}
/* ---------- INTERIORES ---------- */
const WALLS=[['#EBD8B8','#C99A6B'],['#DCE6D4','#9AB88F'],['#F3D4CE','#CF8F8C'],['#D3DDEE','#8FA6CC'],['#F1DFAE','#C9A24B'],['#E3D3EE','#A98BC4']];
function interior(v,raw,R,T,tm){
  const wc=pick(R,WALLS),horizon=112;
  const wallTop=mix(wc[0],T.near,T.wall*.9),wallBot=mix(wc[1],T.near,T.wall*.9);
  let s=`<defs><linearGradient id="wl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${wallTop}"/><stop offset="1" stop-color="${wallBot}"/></linearGradient>
   <linearGradient id="fl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${mix('#B07A4C',T.near,T.wall)}"/><stop offset="1" stop-color="${mix('#6B4527',T.near,T.wall+.1)}"/></linearGradient></defs>`;
  s+=rect(0,0,W,H,'url(#wl)')+rect(0,horizon,W,H-horizon,'url(#fl)');
  for(let i=-4;i<=12;i++)s+=`<line x1="${n1(i*28+10)}" y1="${horizon}" x2="${n1(160+(i*28+10-160)*2.4)}" y2="${H}" stroke="#000" stroke-opacity=".08"/>`;
  s+=rect(0,horizon-2,W,3,'#000',' fill-opacity=".18"');
  /* janela com vista */
  const wx=24+R()*160,wy=18,ww=76+R()*30,wh=62;
  const winSky=`<linearGradient id="ws" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${T.t}"/><stop offset=".6" stop-color="${T.m}"/><stop offset="1" stop-color="${T.b}"/></linearGradient>`;
  const hasWin=!['cinema','subwaycar','library','museum'].includes(v);
  if(hasWin){
    s+=`<defs>${winSky}<clipPath id="wc"><rect x="${wx}" y="${wy}" width="${ww}" height="${wh}"/></clipPath></defs><g clip-path="url(#wc)">${rect(wx,wy,ww,wh,'url(#ws)')}${tm==='night'?stars(R,12).replace(/cx="([\d.]+)"/g,(m,a)=>`cx="${n1(wx+(+a%ww))}"`):''}${circ(wx+ww*.7,wy+14,7,tm==='night'?'#F6F3DC':T.sun)}${skylineRow(R,wy+wh,10,34,8,16,[T.far,mix(T.far,'#000',.12)],T)}${tree(R,wx+16,wy+wh+2,.8,'#3E8F4E',T)}</g>`;
    s+=rect(wx-3,wy-3,ww+6,wh+6,'none',` stroke="#fff" stroke-opacity=".92" stroke-width="3.4"`)+rect(wx+ww/2-1,wy,2,wh,'#fff',' fill-opacity=".9"')+rect(wx,wy+wh/2-1,ww,2,'#fff',' fill-opacity=".9"')+rect(wx-5,wy+wh+3,ww+10,3,'#fff',' fill-opacity=".9"');
    s+=path(`M${wx} ${wy+wh} L${wx+ww} ${wy+wh} L${wx+ww+86} ${H} L${wx-30} ${H}Z`,'url(#ray)',' opacity=".8"');
  }
  const wood='#7a4a2a',dwood=mix(wood,'#000',.35);
  const pend=(x,y,l,c)=>rect(x-.6,y,1.2,l,'#222')+path(`M${x-9} ${y+l+7} Q${x} ${y+l-6} ${x+9} ${y+l+7}Z`,c)+ell(x,y+l+8,13,6,'url(#gl)',` opacity="${n1(.35+T.lit*.6)}"`);
  const shelf=(x,y,w,rows,cols2)=>{let q='';for(let r=0;r<rows;r++){q+=rect(x,y+r*17+13,w,2.4,wood);let bx=x+3;while(bx<x+w-6){const bw=3+R()*4,bh=8+R()*5;q+=rect(bx,y+r*17+13-bh,bw,bh,pick(R,cols2));bx+=bw+.8}}return q+rect(x-1.6,y,2.4,rows*17+16,dwood)+rect(x+w-.8,y,2.4,rows*17+16,dwood)};
  const BOOKS=['#C0392B','#2F6BE8','#E3A93B','#2E8B57','#8E44AD','#E8795A','#16A085'];
  if(v==='cafe'){
    s+=shelf(210,24,84,2,['#F3F0EA','#E8795A','#6FB7C9','#F4C26B']);
    s+=pend(70,0,14,'#2a2f45')+pend(150,0,26,'#2a2f45')+pend(240,0,18,'#2a2f45');
    s+=rect(18,24,52,36,'#2a3a34')+rect(18,24,52,36,'none',' stroke="#7a4a2a" stroke-width="2.4"')+path('M26 36h30M26 44h38M26 52h22','none',' stroke="#fff" stroke-opacity=".7" stroke-width="1.6" stroke-linecap="round"');
    s+=person(R,132,horizon+14,1.35,'#E8795A',T);
    s+=rect(0,132,W,40,dwood)+rect(0,128,W,6,mix(wood,'#fff',.2))+rect(0,134,W,2,'#000',' fill-opacity=".3"');
    s+=rect(212,102,34,26,'#C9CED9')+rect(212,102,34,5,'#8a90a3')+rect(220,108,6,10,'#555')+circ(236,112,4,'#2a2f45')+rect(246,118,18,9,'#E8DCC4');
    [[60],[90],[180],[290]].forEach(([cx])=>{s+=path(`M${cx-5} ${126} L${cx+5} ${126} L${cx+4} ${116} L${cx-4} ${116}Z`,'#F3F0EA')+ell(cx,116,4,1.4,'#6b3a1e')+`<path d="M${cx} ${112} q-3 -6 0 -10" stroke="#fff" stroke-opacity=".6" stroke-width="1.2" fill="none"/>`});
    s+=ell(130,122,16,6,'#E8DCC4')+path('M118 122 Q130 106 142 122Z','#fff',' fill-opacity=".35"');
  }else if(v==='restaurant'){
    s+=pend(60,0,22,'#2a2f45')+pend(160,0,34,'#2a2f45')+pend(262,0,22,'#2a2f45');
    [[70,132,1],[170,144,1.15],[262,132,1]].forEach(([tx,ty,sc2])=>{s+=`<g transform="translate(${tx} ${ty}) scale(${sc2})">${rect(-24,-2,48,3,'#fff')}${path('M-24 1 L24 1 L20 9 L-20 9Z',pick(R,['#C0392B','#2F6BE8']),' fill-opacity=".9"')}${rect(-1.6,9,3.2,22,dwood)}${circ(-10,-6,4,'#F3F0EA')}${circ(10,-6,4,'#F3F0EA')}${rect(-18,-14,3,16,dwood)}${rect(15,-14,3,16,dwood)}</g>`});
    s+=person(R,118,horizon+12,1.2,'#4C7FD6',T)+person(R,214,horizon+12,1.2,'#E8795A',T);
    s+=rect(210,70,40,28,'#fff',' fill-opacity=".1"')+path('M222 74h18M222 82h14M222 90h20','none',' stroke="#fff" stroke-opacity=".6" stroke-width="2"');
  }else if(v==='kitchen'){
    s+=rect(0,58,W,24,mix('#fff',wc[0],.3),' fill-opacity=".92"')+[0,1,2,3,4,5,6,7].map(i=>rect(i*40+2,60,36,20,mix(wc[1],'#fff',.3))+circ(i*40+32,72,1.4,'#fff')).join('');
    s+=rect(120,30,70,30,'#7a8195')+path('M120 30 L190 30 L180 20 L130 20Z','#9aa0b5');
    [[60],[100],[230],[262]].forEach(([px])=>{s+=rect(px-.6,60,1.2,16,'#222')+path(`M${px-8} ${76} L${px+8} ${76} L${px+6} ${90} L${px-6} ${90}Z`,pick(R,['#9aa0b5','#C9CED9']))});
    s+=rect(0,120,W,52,dwood)+rect(0,116,W,6,'#E8DCC4')+rect(130,124,60,30,'#9aa0b5')+circ(150,134,6,'#333')+circ(172,134,6,'#333')+ell(215,114,18,5,'#7a5638')+circ(196,112,7,'#9CCB86')+circ(206,111,6,'#E8795A')+person(R,78,horizon+16,1.4,'#C99BD6',T);
  }else if(v==='living'){
    s+=rect(0,0,W,3,'#000',' fill-opacity=".06"');
    [[210,26,36,28],[258,36,30,22]].forEach(([fx,fy,fw,fh])=>{s+=rect(fx,fy,fw,fh,'#fff')+rect(fx+3,fy+3,fw-6,fh-6,pick(R,['#6FB7C9','#E8795A','#9CCB86','#F4C26B']))});
    s+=rect(20,128,W-40,3,'#000',' fill-opacity=".1"')+ell(160,152,120,16,mix('#C0392B',T.near,.2),' fill-opacity=".45"');
    s+=rect(70,104,170,36,mix('#5A6FA8',T.near,.1))+rect(62,98,22,42,mix('#4C5E90',T.near,.1))+rect(226,98,22,42,mix('#4C5E90',T.near,.1))+rect(82,96,70,16,mix('#6B80BA',T.near,.1))+rect(158,96,70,16,mix('#6B80BA',T.near,.1))+circ(110,102,8,'#F4C26B')+circ(196,102,8,'#E8795A');
    s+=rect(268,66,2,72,'#333')+path('M256 66 L282 66 L276 48 L262 48Z','#F4C26B')+ell(269,70,20,10,'url(#gl)',` opacity="${n1(.3+T.lit*.6)}"`);
    s+=rect(20,100,16,38,'#7a4a2a')+circ(28,90,16,'#2E7D4F')+circ(20,98,10,'#3E9A63')+circ(36,98,10,'#3E9A63')+person(R,150,horizon+30,1.3,'#E8795A',T);
  }else if(v==='office'){
    s+=rect(0,0,W,3,'#000',' fill-opacity=".06"')+shelf(214,22,80,2,BOOKS);
    s+=rect(40,104,160,8,mix('#B9895A',T.near,.1))+rect(46,112,6,34,dwood)+rect(190,112,6,34,dwood)+rect(96,78,44,28,'#1d2433')+rect(98,80,40,22,mix('#6FA8FF',T.near,.0),' fill-opacity=".85"')+rect(114,106,8,4,'#333')+rect(80,96,10,8,'#E8795A')+circ(165,98,8,'#9CCB86')+rect(163,100,4,6,'#7a4a2a');
    s+=person(R,130,horizon+38,1.5,'#4C7FD6',T)+rect(212,92,26,22,'#444',' fill-opacity=".4"');
  }else if(v==='classroom'){
    s+=rect(120,24,150,60,'#24433A')+rect(120,24,150,60,'none',' stroke="#B9895A" stroke-width="3"')+path('M132 40h60M132 52h90M132 64h40M210 70l16-14','none',' stroke="#fff" stroke-opacity=".75" stroke-width="2" stroke-linecap="round"')+rect(120,84,150,3,'#B9895A');
    for(let r=0;r<2;r++)for(let c=0;c<4;c++){const dx=36+c*66-(r?0:10),dy=116+r*26;s+=rect(dx,dy,44,5,mix('#B9895A',T.near,.1))+rect(dx+4,dy+5,3,15,dwood)+rect(dx+36,dy+5,3,15,dwood)+rect(dx+14,dy-6,16,6,pick(R,['#C0392B','#2F6BE8','#fff']))}
    s+=person(R,76,horizon+4,1.2,'#E8795A',T)+circ(290,92,13,mix('#2F6BE8',T.near,.2))+rect(288,104,4,12,'#333');
  }else if(v==='library'){
    s+=shelf(10,6,96,5,BOOKS)+shelf(112,6,96,5,BOOKS)+shelf(214,6,96,5,BOOKS);
    s+=rect(0,112,W,60,'url(#fl)')+rect(60,128,200,6,mix('#B9895A',T.near,.1))+rect(70,134,5,24,dwood)+rect(245,134,5,24,dwood)+rect(150,118,24,10,'#E8795A')+rect(176,121,18,7,'#2F6BE8')+person(R,110,horizon+34,1.3,'#9CCB86',T)+ell(220,124,10,5,'url(#gl)',' opacity=".8"');
  }else if(v==='clinic'){
    s+=rect(0,0,W,H,'#EAF3F5')+rect(0,horizon,W,H-horizon,'#C9D6DB')+rect(196,26,40,40,'#fff')+rect(213,32,6,28,'#E8493A')+rect(203,43,26,6,'#E8493A');
    s+=rect(40,100,100,30,'#F6F8FA')+rect(34,92,12,40,'#C9D6DB')+rect(40,96,100,6,'#fff')+rect(190,70,8,60,'#aab5bd')+rect(170,128,60,3,'#aab5bd')+person(R,246,horizon+30,1.4,'#fff',T)+path('M262 92 q10 10 4 20','none',' stroke="#555" stroke-width="1.6"');
  }else if(v==='hall'){
    [[24],[90],[230],[296]].forEach(([cx])=>{s+=rect(cx-8,0,16,horizon,mix('#E8DCC4',T.near,.15))+rect(cx-10,horizon-8,20,8,mix('#E8DCC4',T.near,.3))+rect(cx-6,0,4,horizon,'#fff',' fill-opacity=".3"')});
    s+=rect(0,horizon,W,H-horizon,'url(#fl)')+rect(90,126,140,30,mix('#7a4a2a',T.near,.05))+rect(90,122,140,6,mix('#B9895A',T.near,.1))+person(R,160,horizon+10,1.3,'#4C7FD6',T)+circ(52,92,14,'#2E7D4F')+circ(272,92,14,'#2E7D4F')+rect(50,100,4,24,'#7a4a2a')+rect(270,100,4,24,'#7a4a2a');
  }else if(v==='ballroom'){
    s+=rect(0,0,W,H,mix('#2A1C4A',T.near,.4))+rect(0,horizon,W,H-horizon,mix('#8A5A3A',T.near,.5));
    s+=`<g>${[0,1,2,3,4].map(i=>circ(30+i*65,12+(i%2)*6,2.4,'#FFE6A8')+circ(30+i*65,12+(i%2)*6,10,'url(#gl)')).join('')}</g>`;
    s+=rect(158,0,2,22,'#bbb')+path('M130 26 Q160 14 190 26 L184 38 L136 38Z','#FFD98A')+circ(160,44,24,'url(#gl)');
    [[60,'#E8795A'],[110,'#4C7FD6'],[200,'#F4C26B'],[250,'#C99BD6']].forEach(([px,c],i)=>{s+=person(R,px,horizon+22+(i%2)*8,1.5,c,T)});
    ['#E8795A','#F4C26B','#4C7FD6','#9CCB86'].forEach((c,i)=>{s+=ell(20+i*92,52+(i%2)*10,8,10,c)+`<path d="M${20+i*92} ${62+(i%2)*10} L${20+i*92} ${96}" stroke="#fff" stroke-opacity=".5"/>`});
  }else if(v==='gym'){
    s+=rect(20,24,130,70,'#fff',' fill-opacity=".14"')+rect(170,24,130,70,'#fff',' fill-opacity=".14"')+rect(0,horizon,W,H-horizon,'#34506B');
    for(let i=0;i<5;i++)s+=rect(30+i*50,120,10+i*2,6,'#222')+circ(30+i*50,123,6,'#555')+circ(40+i*50+i*2,123,6,'#555');
    s+=person(R,130,horizon+22,1.4,'#E8795A',T)+person(R,220,horizon+26,1.3,'#4C7FD6',T);
  }else if(v==='shop'){
    s+=shelf(14,20,120,4,['#E8795A','#F4C26B','#6FB7C9','#9CCB86','#C99BD6'])+shelf(186,20,120,4,['#E8795A','#F4C26B','#6FB7C9','#9CCB86','#C99BD6']);
    s+=path('M130 0 L190 0 L184 14 L136 14Z',pick(R,['#C0392B','#2F6BE8']),' fill-opacity=".95"')+rect(0,128,W,44,dwood)+rect(0,124,W,6,mix('#B9895A',T.near,.1))+person(R,160,horizon+20,1.4,'#9CCB86',T)+rect(40,108,26,16,'#F4C26B')+rect(70,112,20,12,'#E8795A')+rect(250,106,30,18,'#fff')+path('M262 106 q4 -10 8 0','none',' stroke="#333" stroke-width="2"');
  }else if(v==='cinema'){
    s+=rect(0,0,W,H,'#1A1230')+rect(60,20,200,76,'#BFD4FF',' fill-opacity=".9"')+path('M60 20 L260 20 L320 0 L0 0Z','#000',' fill-opacity=".3"')+circ(160,58,70,'url(#gl)',' opacity=".35"');
    for(let r=0;r<4;r++)for(let c=0;c<9;c++){const sx=10+c*36+r*6,sy=110+r*14;s+=rect(sx,sy,24,14,mix('#7a1f2e',T.near,.2))+circ(sx+12,sy-6,5,'#05040c')+rect(sx+7,sy,10,9,'#05040c')}
  }else if(v==='museum'){
    [[30,26,60,44],[120,22,76,54],[228,28,56,42]].forEach(([fx,fy,fw,fh])=>{s+=rect(fx-4,fy-4,fw+8,fh+8,'#B9895A')+rect(fx,fy,fw,fh,pick(R,['#6FB7C9','#E8795A','#9CCB86','#C99BD6']))+circ(fx+fw/2,fy+fh/2,fh*.28,'#fff',' fill-opacity=".35"')});
    s+=rect(0,horizon,W,H-horizon,mix('#B9A58A',T.near,.2))+rect(130,120,70,8,'#6B4527')+rect(136,128,4,16,'#6B4527')+rect(190,128,4,16,'#6B4527')+person(R,230,horizon+22,1.4,'#4C7FD6',T);
  }else if(v==='subwaycar'){
    s+=rect(0,0,W,H,'#D9DEE8')+rect(0,0,W,24,'#B8BFCE');
    for(let i=0;i<3;i++)s+=rect(14+i*104,34,88,54,'#0f1530')+rect(20+i*104,40,76,42,'#223',' fill-opacity=".7"')+`<path d="M${20+i*104} 60h76" stroke="#FFD98A" stroke-width="2" stroke-dasharray="6 10"/>`;
    s+=rect(0,100,W,72,'#8A92A8')+rect(0,98,W,6,'#E8795A')+rect(100,0,3,172,'#C9CED9')+rect(210,0,3,172,'#C9CED9')+person(R,140,H-6,1.5,'#E8795A',T)+person(R,260,H-6,1.5,'#4C7FD6',T);
  }
  return{svg:s,horizon};
}

/* ---------- personagem principal (retrato) ---------- */
const TINT={night:'0.56 0 0 0 0  0 0.62 0 0 0  0 0 0.92 0 0  0 0 0 1 0',dusk:'0.98 0 0 0 0  0 0.78 0 0 0  0 0 0.74 0 0  0 0 0 1 0',golden:'1 0 0 0 0  0 0.9 0 0 0  0 0 0.74 0 0  0 0 0 1 0',dawn:'0.97 0 0 0 0  0 0.9 0 0 0  0 0 0.96 0 0  0 0 0 1 0'};
function charOpts(e){
  const hero=(e&&e.fr||[]).find&&(e.fr||[]).find(f=>f&&f.k==='nbhero');
  const o=hero&&hero.face&&window.PogFace?PogFace.fromEmoji(hero.face):{};
  o.seed=hash((e&&e.t||'')+(hero&&hero.name||'')+(hero&&hero.city||''));
  if(hero&&hero.g&&hero.g[0]&&/^#[0-9a-f]{6}$/i.test(hero.g[0]))o.shirt=hero.g[0];
  if(o.age==='kid')o.age='adult';
  return o;
}
function character(e,tm,id,sc,xPos,yBase){
  if(!window.PogFace)return '';
  const o=charOpts(e),R=rng(o.seed+7);
  const left=R()<.5,s0=sc||1,x=xPos!=null?xPos:(left?18:W-18-100*s0),y=yBase!=null?yBase:H-117*s0;
  const mt=TINT[tm];
  const flt=mt?`<filter id="${id}ct" x="0" y="0" width="1" height="1"><feColorMatrix type="matrix" values="${mt}"/></filter>`:'';
  const cx=x+50*s0;
  return `<defs>${flt}<radialGradient id="${id}cs"><stop offset="0" stop-color="#000" stop-opacity=".5"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient></defs>
   <ellipse cx="${n1(cx)}" cy="${H-2}" rx="${n1(62*s0)}" ry="${n1(12*s0)}" fill="url(#${id}cs)"/>
   <g transform="translate(${n1(x)} ${n1(y)}) scale(${s0})"${mt?` filter="url(#${id}ct)"`:''}>${PogFace.bust(o)}</g>`;
}
/* ---------- montagem ---------- */
function timeOf(R,cl){
  const f=NIGHTY[cl.raw];
  if(f===1)return 'night';if(typeof f==='string')return f;
  return DAYPICK[Math.floor(R()*DAYPICK.length)];
}
function sceneBody(e,seedExtra){
  const sc=e&&e.sc,a=(e&&e.a)||{},seed=hash((e&&e.t||'')+(a.w||'')+(e&&e.n||'')+(seedExtra||''));
  const R=rng(seed),cl=classify(sc,R),tm=timeOf(R,cl),T=TM[tm],id='sc'+(++UID)+'_';
  const tx=((a.d||'')+' '+(a.w||'')+' '+(e&&e.t||'')).toLowerCase();
  const hint={mount:/montanh|andes|serra|cordilheir|vulc|cume|alto|altitude/.test(tx),volcano:/vulc/.test(tx),sea:/praia|costa|porto|ilha|caribe|mar\b|litoral|baía|baia/.test(tx)};
  const r=cl.mode==='in'?interior(cl.v,cl.raw,R,T,tm):exterior(cl.v,cl.raw,R,T,tm,hint);
  const body=cl.mode==='ex'?r.svg:r.svg;
  const idPrefix=s=>s.replace(/id="(a|wl|fl|ws|wc|gl|sea|gnd|ray|vg|vr|sunglow|moonglow|as)s?"/g,m=>m).replace(/(id|url\(#|href="#)(as|a s)/g,'$1$2');
  return{body,T,tm,cl,id,seed};
}
/* ids únicos por capa: reescreve os ids dos gradientes */
function uniq(svg,pre){
  const ids=['as','sunglow','moonglow','gl','vg','vr','ray','gnd','wl','fl','ws','wc','sea'];
  ids.forEach(i=>{svg=svg.split('id="'+i+'"').join('id="'+pre+i+'"').split('url(#'+i+')').join('url(#'+pre+i+')')});
  svg=svg.split('id="as"').join('id="'+pre+'as"');
  return svg;
}
function wide(e,o){
  const sb=sceneBody(e),pal=window.PogCover&&PogCover.palette?PogCover.palette(((e&&e.a&&e.a.w)||(e&&e.t)||'x')):{c1:'#7C4DFF'};
  const T=sb.T,horizon=sb.cl.mode==='ex'?108:112;
  const dfs=defs('a',T,sb.tm,horizon,pal);
  let inner=dfs+sb.body+((o&&o.noChar)?'':character(e,sb.tm,sb.id,.98))+`<rect width="${W}" height="${H}" fill="${pal.c1}" opacity=".16" style="mix-blend-mode:soft-light"/>`+`<rect width="${W}" height="${H}" fill="url(#vg)"/><rect width="${W}" height="${H}" fill="url(#vr)"/>`;
  let svg=`<svg viewBox="0 0 ${W} ${H}" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="${esc('Capa: '+((e&&e.t)||''))}">${inner}</svg>`;
  return uniq(svg.replace('id="as"','id="as"'),sb.id);
}
function wrapLines(t,max){const w=String(t||'').split(/\s+/).filter(Boolean),out=[];let c='';w.forEach(x=>{if((c+' '+x).trim().length>max&&c){out.push(c);c=x}else c=(c+' '+x).trim()});if(c)out.push(c);return out.slice(0,4)}
function poster(e,o){
  const a=(e&&e.a)||{},title=a.w||e.t||'',k=String(a.k||'').toLowerCase();
  const fake={sc:(/filme|serie|série|pe[cç]a/.test(k)?'cinema':/livro|romance|poema|conto/.test(k)?['library','living','office','cafe'][hash(title)%4]:/can[cç][aã]o|m[uú]sica/.test(k)?'ballroom':/cidade|lugar|edif|institu/.test(k)?'plaza':/tradi/.test(k)?'plaza':/arte|pintura/.test(k)?'museum':/esporte/.test(k)?'stadium':''),t:title,a:{w:title},n:0};
  const sb=sceneBody(fake,'poster'),T=sb.T,pal=window.PogCover&&PogCover.palette?PogCover.palette(title+'|p'):{c1:'#7C4DFF',c2:'#4B26B8'};
  const pw=240,ph=320,dfs=defs('a',T,sb.tm,108,pal);
  const lines=wrapLines(title.toUpperCase(),13),fs=lines.length>2?22:26,y0=ph-34-(lines.length-1)*(fs+4);
  const txt=lines.map((l,i)=>`<text x="${pw/2}" y="${y0+i*(fs+4)}" text-anchor="middle" font-family="'Bricolage Grotesque','Plus Jakarta Sans',Georgia,serif" font-weight="800" font-size="${fs}" letter-spacing="1" fill="#fff" stroke="rgba(0,0,0,.28)" stroke-width="3" paint-order="stroke">${esc(l)}</text>`).join('');
  const au=a.au?`<text x="${pw/2}" y="${ph-14}" text-anchor="middle" font-family="'Plus Jakarta Sans',system-ui,sans-serif" font-weight="700" font-size="10" letter-spacing="2" fill="#fff" fill-opacity=".8">${esc(String(a.au).toUpperCase())}</text>`:'';
  const svg=`<svg viewBox="0 0 ${pw} ${ph}" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="${esc(title)}">${dfs}<svg x="${-(30+sb.seed%130)}" y="0" width="${ph/H*W}" height="${ph}" viewBox="0 0 ${W} ${H}" preserveAspectRatio="xMidYMid slice">${sb.body}</svg>
   <rect width="${pw}" height="${ph}" fill="${pal.c1}" opacity=".22" style="mix-blend-mode:soft-light"/><rect width="${pw}" height="${ph}" fill="url(#vr)"/>
   <rect y="${ph*.42}" width="${pw}" height="${ph*.58}" fill="url(#pf)"/><linearGradient id="pf" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#05030f" stop-opacity="0"/><stop offset=".7" stop-color="#05030f" stop-opacity=".78"/><stop offset="1" stop-color="#05030f" stop-opacity=".92"/></linearGradient>
   <rect x="8" y="8" width="${pw-16}" height="${ph-16}" rx="4" fill="none" stroke="#fff" stroke-opacity=".38" stroke-width="1"/>${txt}${au}</svg>`;
  return uniq(svg.replace(/id="pf"/g,'id="PFx"').replace(/url\(#pf\)/g,'url(#PFx)'),sb.id).replace(/PFx/g,sb.id+'pf');
}
function lockedScene(e,o){
  const sb=sceneBody(e),T=sb.T,pal={c1:'#9aa0b5'};
  const svg=`<svg viewBox="0 0 ${W} ${H}" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Em breve">${defs('a',T,sb.tm,108,pal)}<g style="filter:grayscale(1) brightness(.55) blur(1.2px)">${sb.body}</g><rect width="${W}" height="${H}" fill="#0b0a1f" opacity=".35"/><g transform="translate(160 86)"><circle r="22" fill="#fff" fill-opacity=".16" stroke="#fff" stroke-opacity=".5"/><rect x="-9" y="-3" width="18" height="14" rx="3" fill="#fff"/><path d="M-5 -3 V-8 a5 5 0 0 1 10 0 V-3" fill="none" stroke="#fff" stroke-width="2.4"/></g></svg>`;
  return uniq(svg,sb.id);
}
function install(){
  if(!window.PogCover||PogCover._scene)return;
  const o=PogCover,svg0=o.svg,work0=o.work,lock0=o.locked;
  o.svg=function(e,x){try{return wide(e,x)}catch(err){return svg0(e,x)}};
  o.work=function(e,x){try{return poster(e,x)}catch(err){return work0(e,x)}};
  o.locked=function(e,x){try{return lockedScene(e,x)}catch(err){return lock0(e,x)}};
  o._scene=true;
}
install();
window.PogScene={wide,poster,locked:lockedScene,install,classify};
})();
