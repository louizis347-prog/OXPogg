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
let UID=0,LITE=false,CTX=null;
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
const NIGHTY={party:1,ballroom:1,boteco:1,cinema:1,carnaval:'dusk',junina:'dusk',diner:'golden',stadium:'golden',paris:'golden',japan:'golden',seoul:'dusk'};
/* ---------- classificação do cenário ---------- */
const INT=new Set('cafe counter diner restaurant boteco pizzeria kitchen cocina living home bedroom bath vecindad office studio classroom school library clinic hospital hall lobby ballroom party gym shop cinema museum subwaycar'.split(' '));
const ALIAS={counter:'cafe',pizzeria:'restaurant',diner:'restaurant',boteco:'restaurant',cocina:'kitchen',home:'living',vecindad:'living',bedroom:'living',bath:'living',studio:'office',school:'classroom',hospital:'clinic',lobby:'hall',party:'ballroom'};
const EXTV=new Set('plaza street city sampa brasilia rioantigo pelourinho lisboa madrid paris japan seoul station railway airport bridge rainycity stadium road yard market harbor beach ipanema carnaval outdoors park sitio sertao amazonia snowy junina vila'.split(' '));
const EXALIAS={city:'street',rainycity:'street',road:'street',yard:'plaza',bridge:'harbor',railway:'station',outdoors:'park',sitio:'park',vila:'plaza',carnaval:'plaza',junina:'plaza',rioantigo:'pelourinho'};
function classify(sc,R){
  sc=String(sc||'').toLowerCase();
  if(INT.has(sc))return{mode:'in',v:ALIAS[sc]||sc,raw:sc};
  if(EXTV.has(sc))return{mode:'ex',v:EXALIAS[sc]||sc,raw:sc};
  return R()<.5?{mode:'in',v:'cafe',raw:''}:{mode:'ex',v:'plaza',raw:''};
}
/* ---------- peças ---------- */
function stars(R,n){let s='';for(let i=0;i<n;i++){const c=circ(R()*W,R()*70,.4+R()*.8,'#fff',` fill-opacity="${n1(.4+R()*.6)}"`);if(!LITE||i%2)s+=c}return s}
function cloud(x,y,sc,col,op){
  const g=`<g fill="${col}" fill-opacity="${op}" transform="translate(${n1(x)} ${n1(y)}) scale(${sc})">`;
  if(LITE)return g+`<ellipse cx="0" cy="0" rx="26" ry="7"/><ellipse cx="-12" cy="-6" rx="14" ry="9"/><ellipse cx="8" cy="-9" rx="16" ry="11"/></g>`;
  const T=CTX&&CTX.T,sh=T?mix(col,T.near,.55):'#8896b8',hi=T?mix(col,T.sun,.5):'#fff';
  return g+`<ellipse cx="0" cy="0" rx="26" ry="7"/><ellipse cx="-12" cy="-6" rx="14" ry="9"/><ellipse cx="8" cy="-9" rx="16" ry="11"/><ellipse cx="-18" cy="-1" rx="10" ry="5"/><ellipse cx="20" cy="-3" rx="9" ry="5"/><ellipse cx="-2" cy="3" rx="22" ry="3.6" fill="${sh}" fill-opacity=".45"/><ellipse cx="4" cy="-12" rx="9" ry="5" fill="${hi}" fill-opacity=".6"/><ellipse cx="-14" cy="-9" rx="6" ry="3.4" fill="${hi}" fill-opacity=".45"/></g>`}
function windowsGrid(R,x,y,w,h,lit,cols,rows,warm){
  let s='';const cw=w/cols,ch=h/rows,sx=cw*.55,sy=ch*.55;
  for(let i=0;i<cols;i++)for(let j=0;j<rows;j++){
    const on=R()<lit,fx=x+i*cw+cw*.2,fy=y+j*ch+ch*.2;
    if(LITE){if(on)s+=rect(fx,fy,sx,sy,warm)}
    else s+=`<use href="#${on?'wso':'wsn'}" transform="translate(${n1(fx)} ${n1(fy)}) scale(${n1(sx)} ${n1(sy)})"/>`;
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
  if(!LITE){s+=rect(x,y,w,h,'url(#bg1)')+rect(x,y,w,h,'url(#brk)')+rect(x-.8,y-.2,w+1.6,1.7,light,' fill-opacity=".75"')+rect(x,y+1.5,w,.9,'#000',' fill-opacity=".2"')+rect(x,y+h-3.5,w,3.5,dark,' fill-opacity=".6"')}
  const cols=Math.max(2,Math.floor(w/9)),rows=Math.max(2,Math.floor(h/12));
  if(!o.nowin)s+=windowsGrid(R,x+w*.08,y+h*.08,w*.78,h*.78,Math.max(.12,T.lit*.85),cols,rows,'#FFD98A');
  return s;
}
function skylineRow(R,y,minH,maxH,minW,maxW,cols,T,o){
  let s='',x=-6;
  while(x<W+6){const w=minW+R()*(maxW-minW),h=minH+R()*(maxH-minH),c=cols[Math.floor(R()*cols.length)];s+=building(R,x,y-h,w,h+2,c,T,o);x+=w+(o&&o.gap!=null?o.gap:R()*3)}
  return s;
}
function tree(R,x,y,s,col,T){
  const d=mix(col,'#000',.3),l=mix(col,'#fff',.24);
  let q=`<g transform="translate(${n1(x)} ${n1(y)}) scale(${s})">`;
  if(LITE)return q+rect(-1.6,-12,3.2,13,'#5b3d2a')+circ(0,-20,11,d)+circ(-7,-15,8,col)+circ(7,-15,8,col)+circ(0,-24,9,mix(col,'#fff',.1))+'</g>';
  const ld=CTX&&CTX.ld||-1;
  q+=ell(-ld*4,1,13,2.6,'#000',' fill-opacity=".26"')+rect(-1.8,-13,3.6,14,'#5b3d2a')+rect(-ld*.2,-13,1.5,14,'#2e1d12',' fill-opacity=".45"')+path('M0 -9 Q-5 -13 -8 -16M0 -10 Q5 -14 7 -18','none',' stroke="#4a3022" stroke-width="1.2" stroke-linecap="round"')+circ(0,-20,11,d)+circ(-7,-15,8,mix(col,'#000',.12))+circ(7,-15,8,mix(col,'#000',.12))+circ(0,-24,9,col);
  q+=circ(ld*3,-27,6.5,l,' fill-opacity=".5"')+circ(ld*8,-19,4.6,l,' fill-opacity=".42"')+circ(ld*-3,-14,5,d,' fill-opacity=".5"');
  for(let k=0;k<9;k++){const a=k*2.4+x*.13,r=3+k%4*2.6;q+=circ(Math.cos(a)*r*1.7+ld*2,-20+Math.sin(a)*r*1.4,1.1+(k%3)*.4,k%2?l:d,' fill-opacity=".7"')}
  return q+'</g>';
}
function palm(R,x,y,s,T){let f='';for(let i=0;i<7;i++){const a=-160+i*50,c=Math.cos(a*Math.PI/180),sn=Math.sin(a*Math.PI/180);f+=`<path d="M0 -34 Q ${n1(c*16)} ${n1(-34+sn*12-8)} ${n1(c*30)} ${n1(-34+sn*18+6)}" stroke="#2E7D4F" stroke-width="3.4" fill="none" stroke-linecap="round"/>`}
  return `<g transform="translate(${n1(x)} ${n1(y)}) scale(${s})"><path d="M-1.5 0 Q 3 -18 0 -34 L2.5 -34 Q 6 -18 2 0Z" fill="#7a5638"/>${f}${circ(0,-33,2.4,'#6b4a2f')}</g>`}
function person(R,x,y,s,col,T){
  const skin=pick(R,['#F2C4A0','#D9A07A','#B9784F','#8D5A3B','#F6D2B4']),hair=pick(R,['#2B1B14','#4A2E1B','#1A1A22','#7B4A25','#C69552']);
  if(LITE)return `<g transform="translate(${n1(x)} ${n1(y)}) scale(${s})">${ell(0,0,7,1.6,'#000',' fill-opacity=".22"')}${path('M-3.6 -2 L-3.2 -17 L-.3 -17 L-.2 -2Z M.2 -2 L.3 -17 L3.2 -17 L3.6 -2Z',mix(col,'#000',.5))}${path('M-5 -17 Q0 -23 5 -17 L5.8 -29 Q0 -32 -5.8 -29Z',col)}${circ(0,-35,4.6,skin)}${path('M-4.8 -36 Q0 -43 4.8 -36 Q3 -39 0 -39 Q-3 -39 -4.8 -36Z',hair)}</g>`;
  const ld=CTX&&CTX.ld||-1,h=hash(x*7+y*3),pants=['#2f3550','#4a3b32','#3b4a63','#5a4a3e','#35384a'][h%5];
  const sk=mix(skin,'#3a1a10',.35),cd=mix(col,'#000',.34),cl=mix(col,'#fff',.2),hl=mix(hair,'#fff',.3);
  const shade=ld>0?'M0 -29.5 L-5.8 -29 L-5 -17 L0 -17Z':'M0 -29.5 L5.8 -29 L5 -17 L0 -17Z';
  return `<g transform="translate(${n1(x)} ${n1(y)}) scale(${s})">${ell(-ld*3.5,.2,9,1.8,'#000',' fill-opacity=".3"')}`+
   path('M-3.8 -2 L-3.3 -17.5 L-.2 -17.5 L-.4 -2Z',pants)+path('M.4 -2 L.2 -17.5 L3.3 -17.5 L3.8 -2Z',mix(pants,'#000',.18))+
   ell(-2.4,-1,2.9,1.3,'#15151c')+ell(2.6,-1,2.9,1.3,'#15151c')+
   path('M-5.3 -17 Q0 -22 5.3 -17 L6.2 -29.4 Q0 -32.4 -6.2 -29.4Z',col)+path(shade,cd,' fill-opacity=".42"')+`<path d="M-5 -29 Q0 -31 5 -29" fill="none" stroke="${cl}" stroke-opacity=".55" stroke-width=".8"/>`+
   `<path d="M-6 -28.5 L-6.8 -18" stroke="${col}" stroke-width="2.7" stroke-linecap="round"/><path d="M6 -28.5 L6.8 -18" stroke="${cd}" stroke-width="2.7" stroke-linecap="round"/>`+circ(-6.9,-16.6,1.5,skin)+circ(6.9,-16.6,1.5,sk)+
   rect(-1.3,-33,2.6,4,sk)+circ(0,-35.2,4.7,skin)+path(`M0 -39.9 A4.7 4.7 0 0 ${ld>0?0:1} 0 -30.5Z`,sk,' fill-opacity=".3"')+circ(-4.5,-35,.9,skin)+circ(4.5,-35,.9,sk)+circ(-1.9,-35.2,.55,'#2a1810',' fill-opacity=".75"')+circ(1.9,-35.2,.55,'#2a1810',' fill-opacity=".75"')+path('M-1.3 -32.6 Q0 -32 1.3 -32.6','none',' stroke="#7a3a2a" stroke-opacity=".6" stroke-width=".5"')+
   path('M-5 -36.2 Q-4.6 -43.4 0 -43.4 Q4.8 -43.4 5 -36.2 Q3.4 -39.6 0 -39.6 Q-3.4 -39.6 -5 -36.2Z',hair)+path(`M${-ld*3.2} -41.6 Q${ld*1} -43 ${ld*3} -40.6`,'none',' stroke="'+hl+'" stroke-opacity=".6" stroke-width=".8" stroke-linecap="round"')+
   `</g>`;
}
function lamp(x,y,h,T,R){const on=T.lit>.3;
  let q=rect(x-.8,y-h,1.6,h,'#2a2f45')+rect(x-4,y-h-1.5,8,2.4,'#2a2f45');
  if(!LITE)q=ell(x,y,4,1,'#000',' fill-opacity=".3"')+rect(x-1.5,y-5,3,5,'#1c2033')+rect(x-.8,y-h,1.6,h,'#2a2f45')+rect(x-.2,y-h,.7,h,'#fff',' fill-opacity=".18"')+path(`M${x-4.4} ${n1(y-h-1)}L${x+4.4} ${n1(y-h-1)}L${x+3} ${n1(y-h-6)}L${x-3} ${n1(y-h-6)}Z`,'#232840')+rect(x-3,y-h-1.4,6,1.6,on?'#FFE6A8':'#9aa0b5',on?'':' fill-opacity=".5"');
  return q+(on?`<ellipse cx="${n1(x)}" cy="${n1(y-h+1)}" rx="${LITE?12:16}" ry="${LITE?9:12}" fill="url(#gl)"/>`:'')}
/* ---------- céu ---------- */
function skyBlock(R,T,tm,id,horizon){
  let s=`<rect width="${W}" height="${H}" fill="url(#${id}s)"/>`;
  const sx=40+R()*240,sy=horizon*(.22+R()*.3);if(CTX){CTX.sun={x:sx,y:sy,night:tm==='night'};CTX.T=T;CTX.ld=sx<160?-1:1}
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
  <linearGradient id="bg1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".12"/><stop offset=".55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".22"/></linearGradient>
  <pattern id="brk" width="5" height="3.2" patternUnits="userSpaceOnUse"><rect width="5" height="3.2" fill="none"/><rect y="2.6" width="5" height=".6" fill="#000" fill-opacity=".09"/><rect x="2" width=".5" height="2.6" fill="#fff" fill-opacity=".04"/></pattern>
  <linearGradient id="wgo" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFEBB8"/><stop offset="1" stop-color="#FFAE55"/></linearGradient>
  <linearGradient id="wgn" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${mix(T.m,'#fff',.25)}"/><stop offset="1" stop-color="${mix(T.near,'#000',.5)}"/></linearGradient>
  <g id="wso"><rect width="1" height="1" fill="#3d2a14" fill-opacity=".55"/><rect x=".08" y=".08" width=".84" height=".84" fill="url(#wgo)"/><path d="M.5 .08V.92M.08 .5H.92" stroke="#5a3d1a" stroke-width=".07" stroke-opacity=".55"/><rect x="-.1" y="1" width="1.2" height=".14" fill="#fff" fill-opacity=".45"/></g>
  <g id="wsn"><rect width="1" height="1" fill="#0b1030" fill-opacity=".4"/><rect x=".08" y=".08" width=".84" height=".84" fill="url(#wgn)" fill-opacity=".82"/><path d="M.08 .92L.5 .08H.72L.3 .92Z" fill="#fff" fill-opacity=".2"/><path d="M.5 .08V.92" stroke="#0b1030" stroke-width=".06" stroke-opacity=".4"/><rect x="-.1" y="1" width="1.2" height=".14" fill="#fff" fill-opacity=".35"/></g>
  <linearGradient id="gnd" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${mix(T.near,'#2b2f45',.5)}"/><stop offset="1" stop-color="${mix(T.near,'#12142a',.7)}"/></linearGradient></defs>`;
}
/* ---------- EXTERIORES ---------- */
const PASTEL=['#F4C26B','#E8795A','#6FB7C9','#E9A0B4','#9CCB86','#F0DFA2','#C99BD6'];
const CREAM=['#E8D9B9','#D9C49B','#EBDDC7','#C9B188','#E2CDA6'];
const COOL=['#9AA9C6','#8294B6','#B4BED6','#7487AD'];
function exterior(v,raw,R,T,tm,hint){
  const horizon=v==='beach'||v==='harbor'||v==='ipanema'?96:(v==='paris'?90:(v==='japan'?100:108));
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
  }else if(v==='paris'){ /* Paris: Torre Eiffel, Sena com reflexo, ponte de pedra, cais com bouquinistes e café */
    const uidp='pr'+Math.floor(R()*1e6)+'_',cx=214,yb=horizon+14,y1=horizon-17,y2=horizon-46,y3=horizon-70,qy=H-32;
    const iron=mix('#5b4636',T.far,.42),ironHi=mix(iron,'#ffffff',.3),stone=mix('#CDBA97',T.near,.3+T.wall),stoneSh=mix('#8f7f68',T.near,.35+T.wall);
    s+=`<defs><radialGradient id="${uidp}g" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="${T.sun}" stop-opacity=".85"/><stop offset=".55" stop-color="${T.amb}" stop-opacity=".3"/><stop offset="1" stop-color="${T.amb}" stop-opacity="0"/></radialGradient><linearGradient id="${uidp}w" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${mix(T.b,'#6d8fb0',.35)}"/><stop offset=".55" stop-color="${mix(T.m,'#2f5f88',.5)}"/><stop offset="1" stop-color="${mix(T.near,'#1c3552',.45)}"/></linearGradient><clipPath id="${uidp}c"><rect x="0" y="${horizon+9}" width="${W}" height="${qy-horizon-9}"/></clipPath></defs>`;
    s+=circ(cx-6,horizon-26,58,`url(#${uidp}g)`);
    /* margem distante: telhados de mansarda */
    s+=skylineRow(R,horizon-2,16,34,9,20,cols.map(c=>mix(c,T.far,.62)),T,{nowin:true,roof:1,roofCol:mix('#5b6b86',T.far,.35)});
    /* Torre Eiffel */
    let tw='';
    tw+=path(`M${cx-33} ${yb} L${cx-22} ${yb} Q${cx-14} ${yb-20} ${cx-8} ${y1} L${cx-14} ${y1} Q${cx-24} ${yb-22} ${cx-33} ${yb}Z`,iron);
    tw+=path(`M${cx+33} ${yb} L${cx+22} ${yb} Q${cx+14} ${yb-20} ${cx+8} ${y1} L${cx+14} ${y1} Q${cx+24} ${yb-22} ${cx+33} ${yb}Z`,iron);
    tw+=path(`M${cx-21} ${yb} Q${cx} ${yb-30} ${cx+21} ${yb} L${cx+21} ${yb-2.2} Q${cx} ${yb-32} ${cx-21} ${yb-2.2}Z`,iron);
    tw+=rect(cx-16,y1-3,32,3.4,iron)+rect(cx-17,y1-4.4,34,1.4,ironHi,' fill-opacity=".55"');
    tw+=path(`M${cx-11} ${y1-3} L${cx-4.6} ${y2} L${cx+4.6} ${y2} L${cx+11} ${y1-3}Z`,iron);
    tw+=rect(cx-7,y2-2.4,14,2.6,iron)+rect(cx-7.6,y2-3.4,15.2,1,ironHi,' fill-opacity=".5"');
    tw+=path(`M${cx-4} ${y2-2.4} L${cx-1.1} ${y3} L${cx+1.1} ${y3} L${cx+4} ${y2-2.4}Z`,iron)+rect(cx-.4,y3-9,.8,9,iron);
    let lat='';
    for(let i=1;i<=4;i++){const yy=y1-3-(y1-3-y2)*i/5,hw=11-(11-4.6)*i/5;lat+=`M${n1(cx-hw)} ${n1(yy)}L${n1(cx+hw)} ${n1(yy)}`}
    for(let i=0;i<5;i++){const ya=y1-3-(y1-3-y2)*i/5,yc=y1-3-(y1-3-y2)*(i+1)/5,ha=11-(11-4.6)*i/5,hc=11-(11-4.6)*(i+1)/5;lat+=`M${n1(cx-ha)} ${n1(ya)}L${n1(cx+hc)} ${n1(yc)}M${n1(cx+ha)} ${n1(ya)}L${n1(cx-hc)} ${n1(yc)}`}
    lat+=`M${cx-9} ${y1-3}L${cx-1} ${yb-14}M${cx+9} ${y1-3}L${cx+1} ${yb-14}M${cx-27} ${yb-3}L${cx-12} ${yb-18}M${cx+27} ${yb-3}L${cx+12} ${yb-18}`;
    tw+=`<path d="${lat}" stroke="${ironHi}" stroke-width=".55" stroke-opacity=".8" fill="none"/>`;
    s+=tw;
    /* margem próxima: edifícios haussmannianos */
    s+=skylineRow(R,horizon+8,24,40,16,30,cols.map(c=>mix(c,T.far,.18)),T,{roof:1,roofCol:mix('#5b6b86',T.near,.3)});
    /* Sena */
    const wy=horizon+9,wh=qy-wy;
    s+=rect(0,wy,W,wh,`url(#${uidp}w)`);
    s+=`<g clip-path="url(#${uidp}c)" opacity=".2" transform="translate(0 ${n1(2*yb+10)}) scale(1 -1)">${tw}</g>`;
    for(let i=0;i<16;i++)s+=rect(R()*W,wy+4+R()*(wh-8),10+R()*26,.9,T.sun,` fill-opacity="${n1(.25+R()*.4)}"`);
    for(let i=0;i<6;i++)s+=rect(R()*W,wy+3+R()*(wh-6),14+R()*30,.7,'#ffffff',' fill-opacity=".18"');
    /* bateau-mouche */
    const bx=176,by=wy+17;
    s+=path(`M${bx} ${by} L${bx+54} ${by} L${bx+48} ${by+8} L${bx+7} ${by+8}Z`,mix('#F3EFE6',T.near,.18))+rect(bx+6,by-6,40,6,mix('#BFD6E6',T.near,.1),' fill-opacity=".9"')+rect(bx+4,by-7.5,44,1.6,mix('#F3EFE6',T.near,.15));
    for(let i=0;i<7;i++)s+=rect(bx+9+i*5.2,by-5,3,3.4,T.lit>.2?'#FFD98A':mix('#7FA3BE',T.near,.1));
    s+=rect(bx,by+8,54,1.2,'#000',' fill-opacity=".18"');
    /* ponte de pedra (Pont Neuf) */
    const by2=horizon+8;
    s+=rect(-10,by2,172,20,stone)+rect(-10,by2,172,2.6,mix(stone,'#ffffff',.25))+rect(-10,by2+2.6,172,1.2,'#000',' fill-opacity=".18"');
    for(let i=0;i<4;i++){const ax=18+i*44;s+=path(`M${ax-17} ${by2+20} L${ax-17} ${by2+11} Q${ax} ${by2+1} ${ax+17} ${by2+11} L${ax+17} ${by2+20}Z`,stoneSh)+ell(ax,by2+20,17,3,mix('#2f5f88',T.near,.2),' fill-opacity=".6"')}
    for(let i=0;i<7;i++)s+=rect(-6+i*26,by2-1.6,1.6,1.6,mix(stoneSh,'#000',.25));
    s+=lamp(30,by2+2,22,T,R)+lamp(120,by2+2,22,T,R);
    /* cais: calçada, mureta e bouquinistes */
    s+=rect(0,qy,W,H-qy,mix('#B9AA8C',T.near,.3+T.wall))+rect(0,qy,W,3.4,mix(stone,'#ffffff',.2))+rect(0,qy+3.4,W,1.2,'#000',' fill-opacity=".2"');
    for(let i=0;i<9;i++)s+=rect(i*36+R()*8,qy+10+R()*20,16+R()*10,.8,'#000',' fill-opacity=".07"');
    [[14,0],[48,1],[82,0]].forEach(([bxx,k])=>{const gc=mix(k?'#2F6B4A':'#3B7A55',T.near,.18);s+=rect(bxx,qy-9,28,9,gc)+rect(bxx-1,qy-11,30,2.6,mix(gc,'#ffffff',.18))+rect(bxx+2,qy-7,24,1.4,'#000',' fill-opacity=".25"');for(let j=0;j<5;j++)s+=rect(bxx+3+j*4.6,qy-11-3-R()*3,3.4,3.4+R()*3,pick(R,['#E8795A','#F4C26B','#4C7FD6','#E9A0B4']))});
    /* café com mesas e cadeiras */
    [[252,H-14],[286,H-10]].forEach(([tx,ty])=>{s+=ell(tx,ty+11,13,2.4,'#000',' fill-opacity=".2"')+rect(tx-.8,ty-1,1.6,12,'#2a2f45')+ell(tx,ty-1,9,2.6,mix('#F3EFE6',T.near,.2))+rect(tx-14,ty+2,5,9,'#3a3f55')+rect(tx+9,ty+2,5,9,'#3a3f55')});
    s+=person(R,242,H-12,1.05,'#E8795A',T)+person(R,196,H-9,1,'#4C7FD6',T)+person(R,166,H-8,.95,'#F4C26B',T)+tree(R,22,H-8,1.15,'#4E8F4A',T)+tree(R,306,H-6,1.3,'#4E8F4A',T)+lamp(180,H-4,46,T,R)+lamp(278,H-4,46,T,R);
  }else if(v==='japan'){ /* Japão: Monte Fuji nevado, lago com reflexo, torii, pagode e cerejeiras em flor */
    const fx=206,fy=horizon-58,fb=horizon+2,uidj='jp'+Math.floor(R()*1e6)+'_';
    const mtn=mix('#5d6a9a',T.far,.4),snow=mix('#ffffff',T.sun,.18),lake=mix('#7fa9c4',T.amb,.35),red=mix('#d8392b',T.near,.12),dark=mix('#2e2a52',T.far,.25);
    s+=`<defs><radialGradient id="${uidj}g" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="${T.sun}" stop-opacity=".85"/><stop offset="1" stop-color="${T.amb}" stop-opacity="0"/></radialGradient><linearGradient id="${uidj}w" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${mix(lake,T.sun,.4)}"/><stop offset="1" stop-color="${mix(lake,T.far,.5)}"/></linearGradient></defs>`;
    s+=circ(236,horizon-36,52,`url(#${uidj}g)`);
    s+=hills(horizon-4,10,mix(mtn,T.far,.5));
    s+=path(`M${fx-118} ${fb} L${fx-14} ${fy+6} Q${fx} ${fy-6} ${fx+14} ${fy+6} L${fx+118} ${fb}Z`,mtn);
    s+=path(`M${fx-22} ${fy+14} L${fx-14} ${fy+6} Q${fx} ${fy-6} ${fx+14} ${fy+6} L${fx+22} ${fy+14} L${fx+15} ${fy+10} L${fx+9} ${fy+18} L${fx+2} ${fy+9} L${fx-5} ${fy+19} L${fx-11} ${fy+10}Z`,snow);
    s+=rect(0,horizon,W,H-horizon,`url(#${uidj}w)`);
    s+=`<g opacity=".22" transform="translate(0 ${2*horizon}) scale(1 -1)">${path(`M${fx-118} ${fb} L${fx-14} ${fy+6} Q${fx} ${fy-6} ${fx+14} ${fy+6} L${fx+118} ${fb}Z`,mtn)}</g>`;
    for(let i=0;i<10;i++)s+=rect(14+i*32+R()*8,horizon+8+(i%4)*9,16+R()*14,.8,'#ffffff',' fill-opacity=".35"');
    /* pagode */
    const px=52,py=horizon+2;let pg='';
    for(let i=0;i<4;i++){const w2=26-i*4.4,yy=py-i*11;pg+=rect(px-w2/2+2,yy-8,w2-4,8,mix('#7a2e3a',T.near,.15))+path(`M${px-w2/2-5} ${yy-8} Q${px} ${yy-13} ${px+w2/2+5} ${yy-8} L${px+w2/2+2} ${yy-5} H${px-w2/2-2}Z`,dark)}
    s+=pg+rect(px-.7,py-58,1.4,10,dark);
    /* torii no lago */
    const tx=262,ty=horizon+22;
    s+=ell(tx,ty+19,26,2.6,'#000',' fill-opacity=".16"')+rect(tx-17,ty-14,3.2,32,red)+rect(tx+14,ty-14,3.2,32,red)+path(`M${tx-26} ${ty-14} Q${tx} ${ty-24} ${tx+26} ${ty-14} L${tx+24} ${ty-9} Q${tx} ${ty-18} ${tx-24} ${ty-9}Z`,red)+rect(tx-20,ty-6,40,2.6,red);
    /* margem e cerejeiras */
    s+=path(`M0 ${H-24} Q70 ${H-34} 150 ${H-22} T320 ${H-26} V${H} H0Z`,mix('#8fb06a',T.near,.45));
    const sak=(x,y,k)=>{let t=path(`M${x} ${y} q-2 -16 ${3*k} -28 M${x} ${y-14} q9 -5 14 -14`,'none',` stroke="${mix('#4a2f3f',T.near,.2)}" stroke-width="${(2.4*k).toFixed(1)}" stroke-linecap="round"`);for(let i=0;i<12;i++){const a=R()*6.28,d=R()*16*k;t+=circ(x+4+Math.cos(a)*d,y-30*k+Math.sin(a)*d*.7,5.6*k+R()*3,i%3?mix('#f7b8cb',T.near,.15):mix('#ffdce6',T.near,.1),' fill-opacity=".92"')}return t};
    s+=sak(30,H-6,1.3)+sak(292,H-4,1.15)+sak(158,H+2,.9);
    for(let i=0;i<22;i++)s+=ell(R()*W,R()*H,1.6,.9,mix('#ffd5e1',T.sun,.2),` fill-opacity="${(.45+R()*.5).toFixed(2)}"`);
  }else if(v==='seoul'){ /* Seul: Torre Namsan, skyline, telhados de hanok e lanternas */
    const uids='sl'+Math.floor(R()*1e6)+'_',nx=232,nb=horizon-4;
    const mtn=mix('#5d6a9a',T.far,.45),tw=mix('#3a3f6a',T.far,.3),ro=mix('#2e2a52',T.near,.2),wall=mix('#8a4a44',T.near,.25);
    s+=`<defs><radialGradient id="${uids}g" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="${T.sun}" stop-opacity=".85"/><stop offset="1" stop-color="${T.amb}" stop-opacity="0"/></radialGradient></defs>`;
    s+=circ(250,horizon-34,48,`url(#${uids}g)`);
    s+=hills(horizon-6,18,mtn);
    s+=path(`M${nx-3} ${nb-6} L${nx-1.6} ${nb-62} L${nx+1.6} ${nb-62} L${nx+3} ${nb-6}Z`,tw)+ell(nx,nb-46,7,3,tw)+ell(nx,nb-46,7,3,T.sun,' fill-opacity=".4"')+rect(nx-.5,nb-76,1,14,tw);
    s+=skylineRow(R,horizon+8,18,52,12,24,[mix('#4a5a86',T.far,.4),mix('#3d4c78',T.far,.4),mix('#5a6a96',T.far,.4)],T,{});
    s+=rect(0,horizon+14,W,H-horizon-14,mix('#4a3a6a',T.near,.45));
    const hk=(cx,y,w)=>rect(cx-w*.38,y,w*.76,16,wall)+rect(cx-w*.38,y+3,w*.76,2,mix('#d8a860',T.near,.2))+path(`M${cx-w/2-7} ${y+1} Q${cx-w*.3} ${y-1} ${cx} ${y-10} Q${cx+w*.3} ${y-1} ${cx+w/2+7} ${y+1} Q${cx+w*.36} ${y+5} ${cx} ${y+2} Q${cx-w*.36} ${y+5} ${cx-w/2-7} ${y+1}Z`,ro);
    s+=hk(62,horizon+16,90)+hk(190,horizon+22,104)+hk(292,horizon+14,70);
    [[28,12],[112,18],[160,10],[250,16],[300,20]].forEach(([x,y],i)=>{const c=i%2?'#f25c54':'#ffb347';s+=rect(x-.3,0,.6,y-6,'#4a3a6a')+ell(x,y,4,5,c)+ell(x,y,9,10,'#ffb347',' fill-opacity=".16"')});
    s+=person(R,126,H-10,1,'#E8795A',T)+person(R,214,H-8,1.05,'#4C7FD6',T);
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
  if(CTX){CTX.T=T;CTX.horizon=horizon;CTX.wall=wc;if(hasWin){CTX.win={x:wx,y:wy,w:ww,h:wh};CTX.ld=(wx+ww/2)<160?-1:1}else CTX.ld=-1}
  if(hasWin){
    s+=`<defs>${winSky}<clipPath id="wc"><rect x="${wx}" y="${wy}" width="${ww}" height="${wh}"/></clipPath></defs><g clip-path="url(#wc)">${rect(wx,wy,ww,wh,'url(#ws)')}${tm==='night'?stars(R,12).replace(/cx="([\d.]+)"/g,(m,a)=>`cx="${n1(wx+(+a%ww))}"`):''}${circ(wx+ww*.7,wy+14,7,tm==='night'?'#F6F3DC':T.sun)}${skylineRow(R,wy+wh,10,34,8,16,[T.far,mix(T.far,'#000',.12)],T)}${tree(R,wx+16,wy+wh+2,.8,'#3E8F4E',T)}</g>`;
    s+=rect(wx-3,wy-3,ww+6,wh+6,'none',` stroke="#fff" stroke-opacity=".92" stroke-width="3.4"`)+rect(wx+ww/2-1,wy,2,wh,'#fff',' fill-opacity=".9"')+rect(wx,wy+wh/2-1,ww,2,'#fff',' fill-opacity=".9"')+rect(wx-5,wy+wh+3,ww+10,3,'#fff',' fill-opacity=".9"');
    s+=path(`M${wx} ${wy+wh} L${wx+ww} ${wy+wh} L${wx+ww+86} ${H} L${wx-30} ${H}Z`,'url(#ray)',' opacity=".8"');
  }
  {const FX=window.PogSceneFX;if(FX&&FX.pre&&CTX){try{s+=FX.pre(CTX)}catch(err){if(window.console)console.warn('PogSceneFX.pre',err)}}}
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

/* ---------- elenco da história (cursos regulares) ---------- */
const FEM=new Set(('mia ana anna ann marta lia rosa zoe mary mei lily liz alice rita nina eve emma lucia lucía grace sofia sofía maria maría julia laura carla elena clara paula lola sara sarah emily olivia lucy kate katie amy jane anne eva lena lea lara chloe camille léa manon jeanne marie sophie claire inès ines giulia chiara francesca martina elisa luisa beatriz bia carol camila fernanda joana helena isabel isabela nora ida mila vera hana yuki mika sakura aiko lisa jenny anita carmen pilar mercedes rocío rocio silvia susana teresa tere monica mónica andrea paola valentina gabriela daniela natalia noemi irene ingrid greta heidi katja anja petra monika sabine laila lina amelie charlotte alina nadia lucie mathilde yasmin fatima aisha leila').split(' '));
const MAL=new Set(('tom sam leo ben max dan kai kenji diego jack joe peter mark paul john david james mike jim bob tim luke pedro juan carlos luis luís miguel jorge pablo mario marco luca matteo paolo giovanni jean pierre louis hugo lucas nico nick andré andre antonio antónio joão joao josé jose rafael rui felipe gabriel bruno ricardo hans jan lukas felix klaus karl tobias ryo taro hiro ken tomás tomas diogo thiago tiago eduardo fernando manuel alberto enrique ramón ramon sergio javier óscar oscar hector héctor alejandro daniel adrián adrian dani paco pepe ahmed omar ali youssef mohamed').split(' '));
const STOP=new Set(('the this what you she can how let yes every there monday where mom please that and friday her each but saturday dad they could may good your look take don new some our are his sunday not who have york june london would many excuse paris these one give maybe read put here when which welcome listen then rome why boss today sorry everything just july thank choose turn street spain make first qué english italian american french portuguese spanish german japan tokyo france earth sarcasm people never state find all life shall come sure keep tuesday wednesday thursday el la los las un una le les des der die das ein eine il lo gli o os as um uma hoy ayer mañana hola bonjour bonsoir hallo ciao olá oi buenos buenas bom boa guten gute salut').split(' '));
const OLD=/\b(grandma|grandpa|grandmother|grandfather|abuela|abuelo|avó|avô|nonna|nonno|oma|opa|grand-mère|grand-père|mamie|papy)\b/i;
const PRON_F=/\b(she|her|hers|ella|elle|sie|lei|ela|dela)\b/gi,PRON_M=/\b(he|his|him|él|il|er|lui|ele|dele)\b/gi;
const AB={sam:1};
function storyTexts(e){
  const fr=(e&&e.fr)||[],st=fr.find&&fr.find(f=>f&&Array.isArray(f.s)&&f.s.length&&Array.isArray(f.s[0]));
  const sents=st?st.s.slice(0,10).map(x=>String(x[0]||'')):[];
  return {sents,all:sents.join(' ')+' '+((e&&e.p)||'')+' '+((e&&e.s)||'')};
}
function castOf(e){
  const {sents,all}=storyTexts(e),found=[],seen={};
  const toks=all.match(/[A-ZÀ-Ý][a-zà-ÿ]{1,}/g)||[];
  const freq={};toks.forEach(t=>{freq[t]=(freq[t]||0)+1});
  toks.forEach(t=>{const l=t.toLowerCase();if(seen[l])return;
    if(FEM.has(l)||MAL.has(l)||(freq[t]>=3&&!STOP.has(l)&&l.length>2&&/^[A-ZÀ-Ý]/.test(t)&&!/^(A[sn]|In|On|At|To|It|Is|If|We|Do|My|No|So|Up|Of|Or|By|Be)$/.test(t))){seen[l]=1;found.push(t)}});
  const f=(all.match(PRON_F)||[]).length,m=(all.match(PRON_M)||[]).length;
  const gender=n=>{const l=n.toLowerCase();if(FEM.has(l))return 'f';if(MAL.has(l))return 'm';if(f>m)return 'f';if(m>f)return 'm';return /[ai]$/.test(l)?'f':'m'};
  const out=found.slice(0,2).map(n=>({name:n,g:gender(n)}));
  if(!out.length){const fr=(e&&e.fr)||[],props=((fr.find&&fr.find(x=>x&&Array.isArray(x.props)))||{}).props||[];
    const em=props.join('');if(/[👩👧👵]/u.test(em))out.push({name:'',g:'f'});else if(/[👨👦👴]/u.test(em))out.push({name:'',g:'m'});
    else if(f||m)out.push({name:'',g:f>=m?'f':'m'})}
  out.old=OLD.test(all);
  return out;
}
const ASIAN=new Set('kenji mei kai yuki hiro taro ryo mika aiko ken lee kim sakura hana'.split(' '));
function faceFor(name,g,seed,old){
  const R=rng(hash(name||('x'+seed)));
  const o={g,seed:hash((name||'x'+seed)+'f'),age:old?'old':'adult'};
  const l=(name||'').toLowerCase();
  o.tone=ASIAN.has(l)?1:[0,1,1,2,2,3,4][Math.floor(R()*7)];
  if(ASIAN.has(l))o.hair='#14100E';
  return o;
}
/* ---------- personagem principal (retrato) ---------- */
const TINT={night:'0.56 0 0 0 0  0 0.62 0 0 0  0 0 0.92 0 0  0 0 0 1 0',dusk:'0.98 0 0 0 0  0 0.78 0 0 0  0 0 0.74 0 0  0 0 0 1 0',golden:'1 0 0 0 0  0 0.9 0 0 0  0 0 0.74 0 0  0 0 0 1 0',dawn:'0.97 0 0 0 0  0 0.9 0 0 0  0 0 0.96 0 0  0 0 0 1 0'};
function charList(e){
  const hero=(e&&e.fr||[]).find&&(e.fr||[]).find(f=>f&&f.k==='nbhero');
  if(hero&&hero.face&&window.PogFace){
    const o=PogFace.fromEmoji(hero.face);o.seed=hash((e&&e.t||'')+(hero.name||'')+(hero.city||''));
    if(hero.g&&hero.g[0]&&/^#[0-9a-f]{6}$/i.test(hero.g[0]))o.shirt=hero.g[0];
    if(o.age==='kid')o.age='adult';
    return [o];
  }
  const cast=castOf(e),seed=hash((e&&e.t||'')+(e&&e.n||''));
  if(!cast.length)return [{seed}];
  return cast.map((c,i)=>{const o=faceFor(c.name,c.g,seed+i,cast.old&&i===0);o.shirt=window.PogFace?PogFace.SHIRTS[hash(c.name||('s'+seed+i))%PogFace.SHIRTS.length]:undefined;return o});
}
const GRADE={night:{c:'#3d4fa8',k:.34},dusk:{c:'#ff8a66',k:.2},golden:{c:'#ffb062',k:.14},dawn:{c:'#ff9fae',k:.1}};
function character(e,tm,id,sc,xPos,yBase,ctx){
  if(!window.PogFace)return '';
  const list=charList(e),R=rng(hash((e&&e.t)||'')+7),s0=sc||1,lite=!!(ctx&&ctx.lite);
  const src=ctx&&ctx.win?ctx.win.x+ctx.win.w/2:(ctx&&ctx.sun?ctx.sun.x:0);
  const kc=ctx&&ctx.cl&&ctx.cl.mode==='in'&&ctx.cl.v!=='cinema'?(tm==='night'?'#FFC477':ctx.T.sun):(ctx&&ctx.T?ctx.T.sun:'#fff');
  let out=`<defs><radialGradient id="${id}cs"><stop offset="0" stop-color="#000" stop-opacity=".5"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient></defs>`;
  const put=(o,x,y,k)=>{
    o.rich=lite?1:2;o.grade=GRADE[tm];o.light={d:(src<x+50*k)?-1:1,c:kc,k:tm==='night'?.5:.8};
    if(ctx){(ctx.chars=ctx.chars||[]).push({x,y,k,o})}
    out+=`<ellipse cx="${n1(x+50*k)}" cy="${H-2}" rx="${n1(62*k)}" ry="${n1(12*k)}" fill="url(#${id}cs)"/><g transform="translate(${n1(x)} ${n1(y)}) scale(${k})">${PogFace.bust(o)}</g>`};
  if(list.length===2){const k=s0*.86;put(list[1],W-14-100*k,H-117*k,k);put(list[0],12,H-117*k+6,k)}
  else{const left=R()<.5,x=xPos!=null?xPos:(left?18:W-18-100*s0),y=yBase!=null?yBase:H-117*s0;put(list[0],x,y,s0)}
  return out;
}
/* ---------- montagem ---------- */
function timeOf(R,cl){
  const f=NIGHTY[cl.raw];
  if(f===1)return 'night';if(typeof f==='string')return f;
  return DAYPICK[Math.floor(R()*DAYPICK.length)];
}
function sceneBody(e,seedExtra,lite){
  const sc=e&&e.sc,a=(e&&e.a)||{},seed=hash((e&&e.t||'')+(a.w||'')+(e&&e.n||'')+(seedExtra||''));
  const R=rng(seed),cl=classify(sc,R),tm=timeOf(R,cl),T=TM[tm],id='sc'+(++UID)+'_';
  const tx=((a.d||'')+' '+(a.w||'')+' '+(e&&e.t||'')).toLowerCase();
  const hint={mount:/montanh|andes|serra|cordilheir|vulc|cume|alto|altitude/.test(tx),volcano:/vulc/.test(tx),sea:/praia|costa|porto|ilha|caribe|mar\b|litoral|baía|baia/.test(tx)};
  LITE=!!lite;CTX={T,ld:-1,lite:!!lite,tm,cl,id,seed};
  const r=cl.mode==='in'?interior(cl.v,cl.raw,R,T,tm):exterior(cl.v,cl.raw,R,T,tm,hint);
  const ctx=CTX;ctx.tm=tm;ctx.cl=cl;ctx.id=id;ctx.seed=seed;ctx.horizon=r.horizon||ctx.horizon||108;ctx.W=W;ctx.H=H;
  let body=r.svg;
  const FX=window.PogSceneFX;
  if(FX&&FX.back){try{body+=FX.back(ctx)}catch(err){if(window.console)console.warn('PogSceneFX.back',err)}}
  return{body,T,tm,cl,id,seed,ctx};
}
/* ids únicos por capa: reescreve os ids dos gradientes */
function uniq(svg,pre){
  const ids=['as','sunglow','moonglow','gl','vg','vr','ray','gnd','wl','fl','ws','wc','sea','bg1','brk','wgo','wgn','wso','wsn'];
  ids.forEach(i=>{svg=svg.split('id="'+i+'"').join('id="'+pre+i+'"').split('url(#'+i+')').join('url(#'+pre+i+')').split('href="#'+i+'"').join('href="#'+pre+i+'"')});
  svg=svg.split('id="as"').join('id="'+pre+'as"');
  return svg;
}
/* versão leve: arredonda coordenadas (>=4) para inteiros para encolher o SVG */
function squeeze(s){return s.replace(/ (x|y|cx|cy|r|rx|ry|width|height|x1|y1|x2|y2|d)="([^"]*)"/g,(m,a,v)=>` ${a}="${v.replace(/-?\d+\.\d+/g,x=>Math.abs(+x)<4?x:String(Math.round(+x)||0))}"`)}
const isLite=o=>!(o&&(o.full||o.lite===false));
function wide(e,o){
  o=o||{};const lite=isLite(o);
  const sb=sceneBody(e,'',lite),pal=window.PogCover&&PogCover.palette?PogCover.palette(((e&&e.a&&e.a.w)||(e&&e.t)||'x')):{c1:'#7C4DFF'};
  const T=sb.T,horizon=sb.cl.mode==='ex'?108:112,FX=window.PogSceneFX;
  const dfs=defs('a',T,sb.tm,horizon,pal);
  let front='';if(FX&&FX.front){try{front=FX.front(sb.ctx)}catch(err){if(window.console)console.warn('PogSceneFX.front',err)}}
  let ch='';if(!o.noChar)ch=character(e,sb.tm,sb.id,.98,null,null,sb.ctx);
  if(ch&&FX&&FX.hands){try{ch+=FX.hands(sb.ctx)}catch(err){}}
  let inner=dfs+sb.body+ch+front+`<rect width="${W}" height="${H}" fill="${pal.c1}" opacity=".16" style="mix-blend-mode:soft-light"/>`+`<rect width="${W}" height="${H}" fill="url(#vg)"/><rect width="${W}" height="${H}" fill="url(#vr)"/>`;
  let svg=`<svg viewBox="0 0 ${W} ${H}" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="${esc('Capa: '+((e&&e.t)||''))}">${inner}</svg>`;
  svg=uniq(svg,sb.id);
  return lite?squeeze(svg):svg;
}
function wrapLines(t,max){const w=String(t||'').split(/\s+/).filter(Boolean),out=[];let c='';w.forEach(x=>{if((c+' '+x).trim().length>max&&c){out.push(c);c=x}else c=(c+' '+x).trim()});if(c)out.push(c);return out.slice(0,4)}
function poster(e,o){
  const a=(e&&e.a)||{},title=a.w||e.t||'',k=String(a.k||'').toLowerCase();
  const fake={sc:(/filme|serie|série|pe[cç]a/.test(k)?'cinema':/livro|romance|poema|conto/.test(k)?['library','living','office','cafe'][hash(title)%4]:/can[cç][aã]o|m[uú]sica/.test(k)?'ballroom':/cidade|lugar|edif|institu/.test(k)?'plaza':/tradi/.test(k)?'plaza':/arte|pintura/.test(k)?'museum':/esporte/.test(k)?'stadium':''),t:title,a:{w:title},n:0};
  const sb=sceneBody(fake,'poster',isLite(o)),T=sb.T,pal=window.PogCover&&PogCover.palette?PogCover.palette(title+'|p'):{c1:'#7C4DFF',c2:'#4B26B8'};
  const pw=240,ph=320,dfs=defs('a',T,sb.tm,108,pal);
  const lines=wrapLines(title.toUpperCase(),13),fs=lines.length>2?22:26,y0=ph-34-(lines.length-1)*(fs+4);
  const txt=lines.map((l,i)=>`<text x="${pw/2}" y="${y0+i*(fs+4)}" text-anchor="middle" font-family="'Plus Jakarta Sans','Plus Jakarta Sans',Georgia,serif" font-weight="800" font-size="${fs}" letter-spacing="1" fill="#fff" stroke="rgba(0,0,0,.28)" stroke-width="3" paint-order="stroke">${esc(l)}</text>`).join('');
  const au=a.au?`<text x="${pw/2}" y="${ph-14}" text-anchor="middle" font-family="'Plus Jakarta Sans',system-ui,sans-serif" font-weight="700" font-size="10" letter-spacing="2" fill="#fff" fill-opacity=".8">${esc(String(a.au).toUpperCase())}</text>`:'';
  const svg=`<svg viewBox="0 0 ${pw} ${ph}" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="${esc(title)}">${dfs}<svg x="${-(30+sb.seed%130)}" y="0" width="${ph/H*W}" height="${ph}" viewBox="0 0 ${W} ${H}" preserveAspectRatio="xMidYMid slice">${sb.body}</svg>
   <rect width="${pw}" height="${ph}" fill="${pal.c1}" opacity=".22" style="mix-blend-mode:soft-light"/><rect width="${pw}" height="${ph}" fill="url(#vr)"/>
   <rect y="${ph*.42}" width="${pw}" height="${ph*.58}" fill="url(#pf)"/><linearGradient id="pf" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#05030f" stop-opacity="0"/><stop offset=".7" stop-color="#05030f" stop-opacity=".78"/><stop offset="1" stop-color="#05030f" stop-opacity=".92"/></linearGradient>
   <rect x="8" y="8" width="${pw-16}" height="${ph-16}" rx="4" fill="none" stroke="#fff" stroke-opacity=".38" stroke-width="1"/>${txt}${au}</svg>`;
  return uniq(svg.replace(/id="pf"/g,'id="PFx"').replace(/url\(#pf\)/g,'url(#PFx)'),sb.id).replace(/PFx/g,sb.id+'pf');
}
function lockedScene(e,o){
  const sb=sceneBody(e,'',true),T=sb.T,pal={c1:'#9aa0b5'};
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
