/* Pogglot - PogIllus: cenas em SVG inline (sem imagens externas, sem rede).
   PogIllus.scene(kind,{mood,seed,motion,label}) -> string SVG (viewBox 960x540, 16:9)
   PogIllus.pick(textoOuTags) -> kind ; PogIllus.frame(kind,opts) -> <figure> com moldura/legenda */
(function(w){
'use strict';
var W=960,H=540;
function rng(s){s=(s>>>0)||1;return function(){s=(Math.imul(s,1664525)+1013904223)>>>0;return s/4294967296}}
function hs(t){var h=2166136261;for(var i=0;i<t.length;i++){h^=t.charCodeAt(i);h=Math.imul(h,16777619)}return h>>>0}
function P3(h){h=h.replace('#','');if(h.length==3)h=h.replace(/./g,'$&$&');return[parseInt(h.substr(0,2),16),parseInt(h.substr(2,2),16),parseInt(h.substr(4,2),16)]}
function H3(a){return'#'+a.map(function(v){v=Math.max(0,Math.min(255,Math.round(v)));return(v<16?'0':'')+v.toString(16)}).join('')}
function mix(a,b,t){a=P3(a);b=P3(b);return H3([a[0]+(b[0]-a[0])*t,a[1]+(b[1]-a[1])*t,a[2]+(b[2]-a[2])*t])}
function n1(v){return Math.round(v*10)/10}
function ii(v){return Math.round(v)}
function R(x,y,w,h,f,x2){return'<rect x="'+n1(x)+'" y="'+n1(y)+'" width="'+n1(w)+'" height="'+n1(h)+'" fill="'+f+'"'+(x2||'')+'/>'}
function Pa(d,f,x2){return'<path d="'+d+'" fill="'+f+'"'+(x2||'')+'/>'}
function Ci(x,y,r,f,x2){return'<circle cx="'+n1(x)+'" cy="'+n1(y)+'" r="'+n1(r)+'" fill="'+f+'"'+(x2||'')+'/>'}
function El(x,y,rx,ry,f,x2){return'<ellipse cx="'+n1(x)+'" cy="'+n1(y)+'" rx="'+n1(rx)+'" ry="'+n1(ry)+'" fill="'+f+'"'+(x2||'')+'/>'}
function Ln(d,s,sw,x2){return'<path d="'+d+'" fill="none" stroke="'+s+'" stroke-width="'+sw+'"'+(x2||'')+'/>'}
var SCR=' style="mix-blend-mode:screen"',MUL=' style="mix-blend-mode:multiply"';

var MO={
 day:{sk:['#3f86cc','#86bde9','#d9ebf4'],g:[1,1,1],gi:[1,1,1],fog:'#cbdde8',sun:'#fff4d2',sx:.7,sy:.17,cl:'#ffffff',cs:'#a9b9cf',lamp:.05,sl:1,key:'#fff2cf',sea:['#2a7fa8','#8fd0d8'],lit:0},
 dawn:{sk:['#33437a','#cf86a2','#ffcf9e'],g:[1,.85,.82],gi:[1,.9,.86],fog:'#e9b9b6',sun:'#ffd9ac',sx:.27,sy:.56,cl:'#ffd2c6',cs:'#85688e',lamp:.45,sl:.7,key:'#ffcda0',sea:['#4b5d8d','#f0b6a4'],lit:.3},
 sunset:{sk:['#28356f','#dc6d5c','#ffbb68'],g:[1,.74,.58],gi:[1,.83,.68],fog:'#e59f84',sun:'#ffab52',sx:.74,sy:.58,cl:'#ffaa84',cs:'#6a4678',lamp:.6,sl:.9,key:'#ffa24f',sea:['#43457f','#f3a171'],lit:.55},
 night:{sk:['#03060f','#0b1736','#2a3d70'],g:[.25,.33,.6],gi:[.52,.52,.64],fog:'#1b2a55',sun:'#dbe6ff',sx:.8,sy:.17,cl:'#33447a',cs:'#0e1636',lamp:1,sl:.22,key:'#86a2ff',sea:['#050b1e','#1f3363'],lit:1}
};
function moodOf(x,kind){
 var s=String(x||'').toLowerCase().normalize?String(x||'').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,''):String(x||'').toLowerCase();
 if(/amanhec|dawn|sunrise|alvorada|manha|morning/.test(s))return'dawn';
 if(/por.?do.?sol|sunset|dusk|entardec|golden|crepusc/.test(s))return'sunset';
 if(/noite|night|dark|escur/.test(s))return'night';
 if(/dia|day|tarde|noon|afternoon/.test(s))return'day';
 return kind==='night-skyline'?'night':'day';
}

/* contexto de uma chamada */
function ctx(kind,o){
 var mk=moodOf(o.mood,kind),m=MO[mk],id='pi'+Math.random().toString(36).slice(2,6),n=0,D=[],memo={},used={},c={};
 c.m=m;c.mk=mk;c.o=o;c.r=rng(o.seed!=null?+o.seed:hs(kind));c.int=false;
 c.id=function(){return id+(n++).toString(36)};
 c.rn=function(a,b){return a+c.r()*(b-a)};
 c.pk=function(a){return a[Math.floor(c.r()*a.length)]};
 c.C=function(col,d){var a=P3(col),g=c.int?m.gi:m.g;var s=H3([a[0]*g[0],a[1]*g[1],a[2]*g[2]]);return d?mix(s,m.fog,d):s};
 c.lg=function(st,dir){var k='l'+dir+JSON.stringify(st);if(memo[k])return memo[k];var i=c.id();
  var d=dir==='h'?'':(dir==='v'?' x2="0" y2="1"':' '+dir);
  D.push('<linearGradient id="'+i+'"'+d+'>'+st.map(function(s){return'<stop offset="'+s[0]+'" stop-color="'+s[1]+'"'+(s[2]!=null&&s[2]<1?' stop-opacity="'+s[2]+'"':'')+'/>'}).join('')+'</linearGradient>');
  return memo[k]='url(#'+i+')'};
 c.rg=function(col,op){op=op==null?1:op;var k='r'+col+op;if(memo[k])return memo[k];var i=c.id();
  D.push('<radialGradient id="'+i+'"><stop offset="0" stop-color="'+col+'" stop-opacity="'+op+'"/><stop offset=".45" stop-color="'+col+'" stop-opacity="'+n1(op*.3)/1+'"/><stop offset="1" stop-color="'+col+'" stop-opacity="0"/></radialGradient>');
  return memo[k]='url(#'+i+')'};
 c.bl=function(s){var k='b'+s;if(memo[k])return memo[k];var i=c.id();
  D.push('<filter id="'+i+'" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="'+s+'"/></filter>');
  return memo[k]=' filter="url(#'+i+')"'};
 c.fol=function(sc){var k='f'+sc;if(memo[k])return memo[k];var i=c.id();D.push('<filter id="'+i+'" x="-15%" y="-15%" width="130%" height="130%"><feTurbulence type="fractalNoise" baseFrequency=".06" numOctaves="3" seed="4"/><feDisplacementMap in="SourceGraphic" scale="'+(sc||22)+'"/></filter>');return memo[k]=' filter="url(#'+i+')"'};
 c.clip=function(inner){var i=c.id();D.push('<clipPath id="'+i+'">'+inner+'</clipPath>');return' clip-path="url(#'+i+')"'};
 c.pat=function(w,h,inner,extra){var i=c.id();D.push('<pattern id="'+i+'" width="'+w+'" height="'+h+'" patternUnits="userSpaceOnUse"'+(extra||'')+'>'+inner+'</pattern>');return'url(#'+i+')'};
 c.def=function(inner){var i=c.id();D.push('<g id="'+i+'">'+inner+'</g>');return'#'+i};
 c.glow=function(x,y,r,col,op,x2){return Ci(x,y,r,c.rg(col,op),SCR+(x2||''))};
 c.shadow=function(x,y,rx,ry,op){return El(x,y,rx,ry,c.rg('#000',op==null?.5:op))};
 c.fog=function(y,h,op,col){col=col||m.fog;return R(0,y,W,h,c.lg([[0,col,0],[.5,col,op],[1,col,0]],'v'))};
 c.fogTo=function(y,h,op,col){col=col||m.fog;return R(0,y,W,h,c.lg([[0,col,0],[1,col,op]],'v'))};

 /* pessoas: simbolos reutilizaveis, cores por variaveis CSS */
 var TOP=['#2f4858','#7b3f4a','#3d6b5e','#b9873b','#4b4e6d','#a85a44','#d8d2c4','#1f2937','#5a6b8c','#8a9a5b'],
  LEG=['#1d232c','#2b2f3a','#3a3326','#222a3f','#4a4339','#38404f'],
  SK=['#e0ac86','#c68a62','#8d5a3c','#f1c9a5','#6b4328'],
  HR=['#1b1411','#3a2418','#6b4a2b','#a88b5a','#2a2a2e','#b9b9b4'];
 var SYM={
  Mt:'M-4,-87L4,-87L11,-84Q15,-82 15,-76L16,-48L12,-47L11,-66L10,-46L-10,-46L-11,-66L-12,-47L-16,-48L-15,-76Q-15,-82 -11,-84Z',
  Ml:'M-10,-47L10,-47L9,-1L11,0L1,0L.6,-40L-.6,-40L-1,0L-11,0L-9,-1Z',
  Kl:'M-10,-47L10,-47L15,-2L7,0L1,-35L-6,-1L-15,-3Z',
  Wt:'M-3.5,-87L3.5,-87L9,-84Q12,-82 12,-76L13,-52L10,-51L9,-68L9,-42L-9,-42L-9,-68L-10,-51L-13,-52L-12,-76Q-12,-82 -9,-84Z',
  Wl:'M-9,-44L9,-44L14,-20L-14,-20ZM-6,-20L6,-20L5,-1L7,0L1,0L.5,-18L-.5,-18L-1,0L-7,0L-5,-1Z',
  St:'M-4,-59L4,-59L11,-56Q14,-54 14,-48L13,-30L-13,-30L-14,-48Q-14,-54 -11,-56Z',
  Sl:'M-12,-32L12,-32L14,-22L11,-2L4,-1L3,-20L-3,-20L-4,-1L-11,-2L-14,-22Z'};
 c.p=function(x,y,h,t,o2){
  o2=o2||{};var s=h/100,d=o2.d||0,pt=t==='W'?'W':t==='S'?'S':'M',lt=t==='K'?'K':pt;
  if(!used[pt+'t']){used[pt+'t']=1;D.push('<path id="'+id+pt+'t" d="'+SYM[pt+'t']+'"/>')}
  if(!used[lt+'l']){used[lt+'l']=1;D.push('<path id="'+id+lt+'l" d="'+SYM[lt+'l']+'"/>')}
  if(!used.hd){used.hd=1;D.push('<g id="'+id+'hd"><rect x="-2.5" y="-90" width="5" height="5" style="fill:var(--s)"/><ellipse cy="-94" rx="5.3" ry="6.3" style="fill:var(--s)"/><path d="M-5.7,-95Q-5.2,-102 0,-101.6Q5.4,-102 5.7,-95Q3,-98.4 0,-98Q-3,-98.4 -5.7,-95Z" style="fill:var(--h)"/></g>');
   D.push('<linearGradient id="'+id+'sg" gradientUnits="userSpaceOnUse" x1="0" y1="-100" x2="0" y2="0"><stop offset="0" stop-color="#fff" stop-opacity=".1"/><stop offset="1" stop-color="#000" stop-opacity=".38"/></linearGradient>')}
  var gid=id+'p'+pt+lt;
  if(!used[gid]){used[gid]=1;var hy=pt==='S'?' transform="translate(0 28)"':'',hair=pt==='W'?'<path d="M-6,-95Q-6,-103 0,-103Q6,-103 6,-95L7,-83L4.6,-85L4.8,-92Q0,-96 -4.8,-92L-4.6,-85L-7,-83Z" style="fill:var(--h)" transform="'+(pt==='S'?'translate(0 28)':'')+'"/>':'';
   D.push('<g id="'+gid+'"><use href="#'+id+pt+'t" style="fill:var(--t)"/><use href="#'+id+lt+'l" style="fill:var(--l)"/><use href="#'+id+'hd"'+hy+'/>'+hair+'<use href="#'+id+pt+'t" fill="url(#'+id+'sg)"/><use href="#'+id+lt+'l" fill="url(#'+id+'sg)"/></g>')}
  var a=function(k,col){return o2[k]||col};
  var st='--t:'+c.C(a('t',c.pk(TOP)),d)+';--l:'+c.C(a('l',c.pk(LEG)),d)+';--s:'+c.C(a('s',c.pk(SK)),d)+';--h:'+c.C(a('h',c.pk(HR)),d);
  var sx=o2.flip?-s:s;
  return(o2.noshadow?'':El(x+h*.1,y,h*.26,h*.05,c.rg('#000',.5)))+'<use href="#'+gid+'" transform="translate('+n1(x)+' '+n1(y)+') scale('+n1(sx)+' '+n1(s)+')" style="'+st+'"/>'};

 /* ceu + sol/lua + nuvens */
 c.sky=function(hy,sx,sy,noclouds){
  var s=R(0,0,W,hy+70,c.lg([[0,m.sk[0]],[.55,m.sk[1]],[.85,m.sk[2]],[1,m.sk[2]]],'v'));
  sx=sx==null?m.sx*W:sx;sy=sy==null?m.sy*H:sy;c.sun=[sx,sy];
  if(mk==='night'){
   var st='';for(var i=0;i<9;i++)st+=Ci(c.rn(4,196),c.rn(4,116),c.rn(.5,1.2),'#fff',' opacity="'+n1(c.rn(.3,.9))+'"');
   s+=R(0,0,W,hy*.85,c.pat(200,120,st));
   s+=Ci(sx,sy,150,c.rg('#9fb8ff',.35))+Ci(sx,sy,19,'#eef3ff')+Ci(sx-5,sy-4,5,'#d3dcf0',' opacity=".6"')+Ci(sx+6,sy+5,3.5,'#d3dcf0',' opacity=".5"')
  }else{
   var big=mk==='day'?280:380;
   s+=Ci(sx,sy,big,c.rg(m.sun,mk==='day'?.55:.9))+Ci(sx,sy,big*.28,c.rg('#fff',.8))+Ci(sx,sy,mk==='day'?16:24,mk==='day'?'#fffbe8':'#fff1d2',' opacity=".95"'+c.bl(1.5))
  }
  if(!noclouds){
   var cs=c.bl(7),k,j,x,y,g;
   for(k=0;k<3;k++){x=c.rn(100,W-100);y=c.rn(40,hy*.6);g='<g'+cs+'>';
    for(j=0;j<3;j++)g+=El(x+c.rn(-60,60),y+c.rn(-6,8),c.rn(44,84),c.rn(11,20),m.cl,' opacity="'+n1(c.rn(.5,.85))+'"');
    g+=El(x,y+13,90,8,m.cs,' opacity=".35"')+'</g>';s+=g}
   s+='<g'+c.bl(12)+' opacity=".4">'+El(W*.3,hy*.5,260,7,m.cl)+El(W*.7,hy*.7,300,8,m.cl)+'</g>'
  }
  return s};

 /* predios (silhuetas em camadas, janelas por padrao) */
 c.wpat=function(){var k='wp';if(memo[k])return memo[k];var wc=mk==='night'?'#ffd58a':mix(m.fog,'#fff',.5),t='';
  for(var y=0;y<3;y++)for(var x=0;x<3;x++){var a=mk==='night'?(c.r()<.55?c.rn(.5,1):.12):c.rn(.12,.4);t+=R(x*7+1,y*9+2,4,5,wc,' opacity="'+n1(a)+'"')}
  return memo[k]=c.pat(21,27,t)};
 c.bld=function(x0,x1,base,hmin,hmax,col,depth,o2){
  o2=o2||{};var x=x0,hh,w1,d=['','',''],k=0,cl=c.C(col,depth),all='',top=base;
  while(x<x1){w1=c.rn(o2.wmin||34,o2.wmax||80);hh=c.rn(hmin,hmax);
   var seg='M'+ii(x)+' '+ii(base+2)+'V'+ii(base-hh)+'h'+ii(w1)+'V'+ii(base+2)+'Z';d[k%3]+=seg;all+=seg;top=Math.min(top,base-hh);
   if(c.r()<.25)d[(k+1)%3]+='M'+ii(x+w1*.45)+' '+ii(base-hh)+'v-'+ii(c.rn(8,20))+'h2v'+ii(c.rn(8,20))+'Z';
   x+=w1+c.rn(-4,6);k++}
  var s=Pa(d[0],mix(cl,'#fff',.05))+Pa(d[1],cl)+Pa(d[2],mix(cl,'#000',.1));
  if(!o2.nowin){var cp=c.clip('<path d="'+all+'"/>');s+='<g'+cp+'>'+R(x0,top,x1-x0,base-top,c.wpat(),' opacity="'+n1(.5+depth*.3)+'"')+R(x0,top,x1-x0,base-top,c.lg([[0,'#fff',.1],[1,'#000',.22]],'v'))+'</g>'}
  return s};
 c.trees=function(x0,x1,base,hmin,hmax,col,depth,dens){
  var s='',x=x0,hh,r,cc=c.C(col,depth);
  while(x<x1){hh=c.rn(hmin,hmax);r=hh*c.rn(.34,.5);
   s+=El(x,base-hh*.55,r,hh*.5,c.lg([[0,mix(cc,m.sun,.12)],[1,mix(cc,'#000',.25)]],'v'));
   x+=r*c.rn(.9,1.5)*(dens||1)}
  return'<g'+c.fol(hmax*.35)+'>'+s+'</g>'};
 c.ridge=function(base,amp,col,depth,seedx){
  var d='M0 '+H,x,y,k=0;for(x=0;x<=W+40;x+=40){y=base-amp*(Math.sin(x*.011+seedx)+.6*Math.sin(x*.027+seedx*2)+.3*Math.sin(x*.063+seedx*3));d+='L'+x+' '+ii(y)}
  return Pa(d+'L'+W+' '+H+'Z',c.C(col,depth))};
 c.bokeh=function(x0,y0,x1,y1,n,cols){var s='<g'+SCR+c.bl(2)+'>';for(var i=0;i<n;i++)s+=Ci(c.rn(x0,x1),c.rn(y0,y1),c.rn(4,16),c.pk(cols),' opacity="'+n1(c.rn(.15,.55))+'"');return s+'</g>'};
 /* janela com vista */
 c.outside=function(x,y,w,h,mode){
  var s=R(x,y,w,h,c.lg([[0,m.sk[0]],[.6,m.sk[1]],[1,m.sk[2]]],'v'));
  s+=Ci(x+w*.7,y+h*.2,w*.4,c.rg(m.sun,.7));
  var b=y+h*.85,g='<g'+c.bl(1.6)+'>'+c.bld(x-10,x+w+10,b,h*.2,h*.7,'#8fa3b8',.5,{wmin:26,wmax:60})+c.bld(x-10,x+w+10,b+8,h*.1,h*.4,'#6c7f95',.25,{wmin:30,wmax:70})+'</g>';
  if(mode==='trees')g='<g'+c.bl(2.5)+'>'+c.trees(x-10,x+w+10,b+10,h*.35,h*.6,'#4f7a4a',.3)+'</g>';
  s+=g+R(x,b,w,y+h-b,c.lg([[0,mix(m.fog,'#444',.3)],[1,'#2b3036']],'v'));
  if(mk==='night'||mk==='sunset')s+=c.bokeh(x,y+h*.5,x+w,y+h*.95,14,['#ffd28a','#ff9a6a','#9ed0ff','#fff0b8']);
  return s};
 c.winFrame=function(x,y,w,h,cols,rows,mode,fc){
  var cp=c.clip(R(x,y,w,h,'#000')),s='<g'+cp+'>'+c.outside(x,y,w,h,mode);
  s+=Pa('M'+x+' '+(y+h)+'L'+x+' '+(y+h*.45)+'L'+(x+w*.5)+' '+y+'L'+(x+w*.62)+' '+y+'L'+(x+w*.1)+' '+(y+h)+'Z','#fff',' opacity=".09"')+'</g>';
  fc=fc||c.C('#e9e3d8');var k;
  for(k=0;k<=cols;k++)s+=R(x+k*(w-5)/cols,y,5,h,fc);
  for(k=0;k<=rows;k++)s+=R(x,y+k*(h-5)/rows,w,5,fc);
  return s};
 /* feixe de luz (janela -> chao) */
 c.beam=function(x,y,w,h,dx,dy,op){
  var sl=m.sl;if(sl<.1)return'';op=(op==null?.2:op)*sl;var yb=y+h;
  return'<g'+SCR+c.bl(5)+'>'+Pa('M'+x+' '+y+'L'+(x+w)+' '+y+'L'+(x+w+dx)+' '+(yb+dy)+'L'+(x+dx*.9)+' '+(yb+dy)+'Z',c.lg([[0,m.key,op*1.1],[1,m.key,op*.3]],'v'))+'</g>'};
 c.patch=function(pts,op){var sl=m.sl;return'<g'+SCR+c.bl(3)+'>'+Pa(pts,m.key,' opacity="'+n1((op||.35)*sl)+'"')+'</g>'};
 c.lamp=function(x,y,r,col,op){return c.glow(x,y,r,col||'#ffcf8a',(op==null?.6:op)*Math.max(m.lamp,.12))};
 c.fin=function(){
  var sx=c.sun?c.sun[0]:W*.7,sy=c.sun?c.sun[1]:80,s='';
  if(!c.int&&mk!=='night')s+=Ci(sx,sy,520,c.rg(m.sun,mk==='day'?.16:.28),SCR);
  s+=R(0,0,W,H,c.lg([[0,'#000',.0],[1,'#000',.32]],'v'),' opacity=".7"');
  s+=R(0,0,W,H,'#000',' filter="url(#'+id+'mt)" opacity="'+(mk==='night'?.1:.08)+'" style="mix-blend-mode:multiply"');
  s+=R(0,0,W,H,'url(#'+id+'vg)');
  s+=R(0,0,W,H,'#808080',' filter="url(#'+id+'gr)" opacity="'+(mk==='night'?.1:.085)+'" style="mix-blend-mode:overlay"');
  return s};
 c.assemble=function(body,label){
  var mo=o.motion?'<style>@media (prefers-reduced-motion:no-preference){.'+id+'a{animation:'+id+'d 14s ease-in-out infinite alternate}.'+id+'b{animation:'+id+'s 7s ease-in-out infinite alternate}}@keyframes '+id+'d{to{transform:translateX(-9px)}}@keyframes '+id+'s{from{opacity:.55}to{opacity:1}}</style>':'';
  var defs='<defs>'+D.join('')+'<radialGradient id="'+id+'vg" cx=".5" cy=".5" r=".75"><stop offset=".55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".5"/></radialGradient><filter id="'+id+'mt" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".035 .05" numOctaves="3" seed="'+(hs(kind)%50+3)+'"/><feColorMatrix values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1.7 -.5"/></filter><filter id="'+id+'gr" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" seed="'+(hs(kind)%90)+'" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter></defs>';
  body=body.split(SCR).join(' class="s"').split(MUL).join(' class="u"');
  return'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 '+W+' '+H+'" preserveAspectRatio="xMidYMid slice" class="pogillus" role="img" aria-label="'+(label||'').replace(/"/g,'')+'" style="display:block;width:100%;height:auto;aspect-ratio:16/9">'+mo+defs+body+'</svg>'};
 return c}

var S={};/* cenas */
/* ---------- exterior: rua ---------- */
function car(c,x,gy,sc,col,front){
 var m=c.m,s='<g transform="translate('+ii(x)+' '+ii(gy)+') scale('+n1(sc)+')">',dk=c.C('#10151d');
 s+=El(0,0,62,6,c.rg('#000',.6));
 s+=Pa('M-50,-12Q-52,-30 -46,-40L-36,-42L-30,-72Q-28,-76 -22,-76L22,-76Q28,-76 30,-72L36,-42L46,-40Q52,-30 50,-12Z',c.lg([[0,mix(c.C(col),'#fff',.18)],[.5,c.C(col)],[1,mix(c.C(col),'#000',.45)]],'v'));
 s+=Pa('M-26,-70L26,-70L31,-45L-31,-45Z',c.lg([[0,mix(m.sk[1],'#102',.5)],[1,dk]],'v'),' opacity=".92"');
 s+=Pa('M-24,-69L-8,-69L-14,-46L-28,-46Z','#fff',' opacity=".12"');
 s+=R(-50,-14,100,6,dk)+R(-46,-12,12,12,'#0b0e13')+R(34,-12,12,12,'#0b0e13');
 if(front){
  s+=R(-40,-30,16,7,'#fffbe8')+R(24,-30,16,7,'#fffbe8')+Ci(-32,-26,34,c.rg('#fff6c8',.5*Math.max(m.lamp,.25)),SCR)+Ci(32,-26,34,c.rg('#fff6c8',.5*Math.max(m.lamp,.25)),SCR);
  s+=R(-14,-24,28,9,dk,' opacity=".7"')
 }else{
  s+=R(-46,-34,18,7,'#e23b3b')+R(28,-34,18,7,'#e23b3b')+Ci(-38,-30,30,c.rg('#ff3b30',.55),SCR)+Ci(38,-30,30,c.rg('#ff3b30',.55),SCR);
  s+=R(-12,-26,24,8,'#d9d6cc')
 }
 s+=Ln('M-48,-38L-36,-42L-30,-72',mix(c.C(col),'#fff',.5),1.2,' opacity=".5"');
 return s+'</g>'}

S['city-street']=function(c,m){
 var VX=480,VY=262,s='',mk=c.mk,r=c.r,k,i,j;
 function pr(X,Y,z){return[ii(VX+X/z),ii(VY+Y/z)]}
 function q(X,z1,z2,Y1,Y2){return'M'+pr(X,Y1,z1)+'L'+pr(X,Y1,z2)+'L'+pr(X,Y2,z2)+'L'+pr(X,Y2,z1)+'Z'}
 function gq(X1,X2,z1,z2){return'M'+pr(X1,200,z1)+'L'+pr(X2,200,z1)+'L'+pr(X2,200,z2)+'L'+pr(X1,200,z2)+'Z'}
 var day=mk==='day';
 s+=c.sky(VY+40,day?700:VX,day?80:VY-40);
 /* skyline distante */
 s+='<g'+c.bl(.8)+'>'+c.bld(300,520,VY+8,30,120,'#9db1c6',.78,{wmin:18,wmax:34})+c.bld(380,700,VY+8,18,70,'#93a7bc',.7,{wmin:20,wmax:40})+'</g>';
 s+=R(0,VY,W,H-VY,c.C('#575b63'));
 /* calcada e rua */
 s+=Pa(gq(-430,-250,.4,40),c.lg([[0,mix(c.C('#8e8f91'),m.fog,.7)],[1,c.C('#a3a39f')]],'v'));
 s+=Pa(gq(250,430,.4,40),c.lg([[0,mix(c.C('#8e8f91'),m.fog,.7)],[1,c.C('#a3a39f')]],'v'));
 s+=Pa(gq(-250,250,.4,40),c.lg([[0,mix(c.C('#4a4d54'),m.fog,.78)],[.35,c.C('#43464d')],[1,c.C('#2e3036')]],'v'));
 s+=Pa(gq(-262,-250,.4,40),c.C('#c9c6bd'))+Pa(gq(250,262,.4,40),c.C('#c9c6bd'));
 /* faixa e marcas */
 var dd='';for(k=0;k<12;k++)dd+=gq(-5,5,.55+k*.75,.55+k*.75+.38);
 s+=Pa(dd,c.C('#e9d27a'),' opacity=".85"');
 dd='';for(k=-6;k<6;k++)dd+=gq(k*40+6,k*40+34,1.25,1.72);
 s+=Pa(dd,c.C('#e8e6df'),' opacity=".9"');
 if(m.lamp>.3)s+='<g'+SCR+c.bl(6)+'>'+El(VX,430,70,150,c.rg(m.sun,.5))+El(VX-120,470,30,70,c.rg('#ff6a4a',.3))+El(VX+110,450,26,60,c.rg('#fff1c8',.3))+'</g>';
 /* sombras projetadas */
 if(mk!=='night'){var sh=day?gq(-430,-60,.4,40):gq(-430,-150,.4,40)+gq(170,430,.4,40);s+='<g'+c.bl(4)+MUL+'>'+Pa(sh,mix(m.sk[0],'#000',.55),' opacity=".4"')+'</g>'}
 /* predios */
 var COLS=['#bba993','#8f939c','#a8604b','#cfc1a8','#7a8a99','#b49a7d','#9a8f86'],lw=[.4,1.6,3.3,5.6,9.6],rw=[.4,2.4,3.4,5,7.4,9.6],walls='',wn;
 function wall(X,z1,z2,Ytop,col,lit,side){
  var base=c.C(mix(col,lit?'#fff':'#000',lit?.1:.2)),far=mix(base,m.fog,Math.min(.85,.08+z1*.07));
  var o=side<0?[[0,base],[1,far]]:[[0,far],[1,base]];
  var out=Pa(q(X,z1,z2,Ytop,200),c.lg(o,'h'));
  /* andares */
  var dk='',l1='',l2='',zz,f,y1,y2,wz,nz=Math.min(z2,3.4),yy;
  for(f=1;f<9;f++){
   y1=-125*f+75-95;y2=-125*f+75-35;
   if(y1<Ytop+20)break;
   yy=VY+y2/z1;if(yy<-30)continue;
   if(VY+y1/z2>545)continue;
   for(zz=z1+.12;zz<nz-.2;zz+=.9){
    wz=.42;dk+=q(X,zz,zz+wz,y1,y2);
    var rr=r();if(rr<m.lit*.55)l1+=q(X,zz,zz+wz,y1,y2);}
   if(z2>3.4){dk+=q(X,Math.max(z1,3.4),z2,y1,y2)}
  }
  var gl=mk==='night'?'#141b2c':mix(c.C('#3d5169'),m.fog,Math.min(.6,z1*.05));
  out+=Pa(dk,c.lg([[0,mix(m.sk[1],'#fff',.1)],[.6,mk==='night'?'#141b2c':c.C('#33475f')],[1,mk==='night'?'#141b2c':c.C('#26333f')]],'v'),' opacity=".92"');
  if(l1)out+=Pa(l1,'#ffd78e');
  /* vitrines */
  var zz2=z1+.1,aw='',gw='';
  while(zz2<Math.min(z2,4.4)-.4){
   var wl=r()*.5+.55,zb=Math.min(zz2+wl,z2-.05);
   aw+='<path d="'+q(X,zz2,zb,30,92)+'" fill="'+c.C(c.pk(['#a3342f','#2f5d46','#223a63','#c08a2b','#6b2f55']))+'"/>';
   gw+=q(X,zz2+.04,zb-.04,92,196);zz2=zb+.15}
  out+=Pa(gw,mk==='night'||mk==='sunset'||mk==='dawn'?'#ffcf86':mix(c.C('#566a80'),'#fff',.1),' opacity="'+(mk==='day'?.75:.95)+'"')+aw;
  /* vigas e cornija */
  var ln='';for(f=0;f<9;f++){y1=-125*f+75;ln+='M'+pr(X,y1,z1)+'L'+pr(X,y1,z2)}
  out+=Ln(ln,'#000',1.2,' opacity=".18"')+Ln('M'+pr(X,Ytop,z1)+'L'+pr(X,Ytop,z2),mix(base,m.sun,.5),2,' opacity=".6"');
  out+=Ln('M'+pr(X,Ytop,z1)+'L'+pr(X,200,z1),'#000',2,' opacity=".25"');
  return out}
 for(i=lw.length-2;i>=0;i--)s+=wall(-430,lw[i],lw[i+1],-620-i*160+r()*200,COLS[(i*3+1)%COLS.length],day,-1);
 for(i=rw.length-2;i>=0;i--){if(i===1){continue}s+=wall(430,rw[i],rw[i+1],-650-i*130+r()*180,COLS[(i*2+3)%COLS.length],!day,1)}
 /* arvores de rua */
 function tree(X,z,sz){var p=pr(X,200,z),sc=1/z,cx=p[0],cy=p[1],g=mix('#4d7a45',mk==='night'?'#1c3040':'#4d7a45',0);
  var t=Ln('M'+cx+' '+cy+'L'+cx+' '+ii(cy-150*sc),c.C('#4a3a2c'),ii(9*sc+2))+'<g'+c.fol(Math.max(4,22*sc))+'>'+El(cx,cy-205*sc,95*sc*sz,80*sc*sz,c.lg([[0,c.C('#6a9a54')],[1,c.C('#2f5a30')]],'v'))+El(cx-60*sc,cy-185*sc,45*sc*sz,40*sc*sz,c.C('#4f7e44'))+El(cx+58*sc,cy-190*sc,42*sc*sz,38*sc*sz,c.C('#3b6a38'))+El(cx-20*sc,cy-235*sc,60*sc*sz,36*sc*sz,c.C('#9fc873'),' opacity=".45"')+'</g>';
  return t+El(cx,cy,60*sc,6*sc,c.rg('#000',.4))}
 s+=tree(-330,1.15,1)+tree(335,1.85,1)+tree(-330,3.2,1)+tree(335,5.2,1);
 /* postes */
 function lamp(X,z){var p=pr(X,200,z),sc=1/z,t=Ln('M'+p[0]+' '+p[1]+'L'+p[0]+' '+ii(p[1]-285*sc),c.C('#2a2f37'),n1(7*sc+1))+Ln('M'+p[0]+' '+ii(p[1]-285*sc)+'Q'+p[0]+' '+ii(p[1]-310*sc)+' '+ii(p[0]-Math.sign(X)*70*sc)+' '+ii(p[1]-305*sc),c.C('#2a2f37'),n1(5*sc+.8));
  var hx=p[0]-Math.sign(X)*70*sc,hy=p[1]-300*sc;t+=El(hx,hy,16*sc+2,5*sc+1,c.C('#20252c'));
  if(m.lamp>.1)t+=Ci(hx,hy+4,110*sc,c.rg('#ffd9a0',.75*m.lamp),SCR)+Ci(hx,hy+3,5*sc+1,'#fff4d6');
  return t}
 s+=lamp(-262,.95)+lamp(262,1.8)+lamp(-262,3.3)+lamp(262,5.6)+lamp(-262,8);
 /* semaforo */
 var tp=pr(240,200,3.1),tz=1/3.1;
 s+=Ln('M'+tp[0]+' '+tp[1]+'L'+tp[0]+' '+ii(tp[1]-330*tz),c.C('#1f242b'),n1(6*tz+1))+R(tp[0]-9*tz,tp[1]-380*tz,18*tz+2,58*tz,c.C('#14181d'))+Ci(tp[0],tp[1]-372*tz,5*tz+1,'#ff3b30')+Ci(tp[0],tp[1]-372*tz,26*tz,c.rg('#ff3b30',.7),SCR)+Ci(tp[0],tp[1]-350*tz,5*tz+1,'#14301c');
 /* carros */
 var cp=pr(-120,200,2.1);s+=car(c,cp[0],cp[1],1.35/2.1,'#c9c4b8',false);
 cp=pr(120,200,3.6);s+=car(c,cp[0],cp[1],1.35/3.6,'#a6322d',true);
 cp=pr(-120,200,5.3);s+=car(c,cp[0],cp[1],1.35/5.3,'#1f3b5c',false);
 /* pessoas */
 var pp=[[-340,1.05,'W'],[-292,1.25,'M'],[338,1.4,'K'],[312,1.9,'W'],[-330,2.5,'K'],[300,2.8,'M'],[320,4.4,'K']],pt;
 for(i=0;i<pp.length;i++){pt=pr(pp[i][0],200,pp[i][1]);s+=c.p(pt[0],pt[1],128/pp[i][1],pp[i][2],{d:Math.min(.5,(pp[i][1]-1)*.07),flip:i%2})}
 /* atmosfera */
 s+=Ci(VX,VY-10,320,c.rg(m.fog,mk==='day'?.6:.85))+c.fog(VY-60,120,.5);
 if(mk==='sunset'||mk==='dawn'){s+='<g'+SCR+c.bl(9)+' opacity=".5">';for(k=0;k<6;k++)s+=Pa('M'+VX+' '+(VY-30)+'L'+ii(VX+(k-2.5)*220)+' 0L'+ii(VX+(k-2.5)*220+60)+' 0Z',m.sun,' opacity=".25"');s+='</g>'}
 return s};

/* ---------- exteriores (1) ---------- */
function pines(c,y0,h,col,depth,sz){
 return c.pat(sz,h,Pa('M'+sz*.5+' 0L'+sz*.84+' '+h*.52+'H'+sz*.66+'L'+sz*.96+' '+h*.92+'H'+sz*.04+'L'+sz*.34+' '+h*.52+'H'+sz*.16+'Z',c.C(col,depth)))}

S['night-skyline']=function(c,m){
 var s='',mk=c.mk,hy=360,i,x,k;
 s+=c.sky(hy+10,mk==='night'?720:null,mk==='night'?95:null);
 /* skyline em camadas */
 var far=c.bld(-20,980,hy,50,170,'#7d90a8',.7,{wmin:22,wmax:46})+c.bld(-20,980,hy,40,120,'#6a7d96',.55,{wmin:26,wmax:50});
 var near=c.bld(-30,990,hy,90,250,'#4a5a72',.25,{wmin:36,wmax:74});
 /* torres de destaque */
 var tw='',tx=[170,420,640,820];
 for(i=0;i<4;i++){var tw0=46+i%2*18,th=230+((i*53)%90);
  tw+=R(tx[i],hy-th,tw0,th,c.lg([[0,c.C('#5d6e86',.1)],[.5,c.C('#7d8fa8',.05)],[1,c.C('#3a4659',.12)]],'h'))+R(tx[i]+3,hy-th+6,tw0-6,th-8,c.wpat(),' opacity=".9"')+R(tx[i]+tw0/2-1,hy-th-34,2,34,c.C('#5d6e86'))+Ci(tx[i]+tw0/2,hy-th-34,2.5,'#ff3b3b')+Ci(tx[i]+tw0/2,hy-th-34,14,c.rg('#ff3b3b',.8*(mk==='night'?1:.2)),SCR)}
 tw+=Pa('M590 '+hy+'V150L606 120L614 40L622 120L638 150V'+hy+'Z',c.lg([[0,c.C('#6f819a')],[1,c.C('#3c4a5e')]],'h'));
 var sk=c.def('<g'+c.bl(.7)+'>'+far+'</g>'+near+tw);
 s+='<use href="'+sk+'"/>';
 s+=c.fog(hy-90,100,.5);
 /* agua */
 s+=R(0,hy,W,H-hy,c.lg([[0,m.sea[1]],[1,m.sea[0]]],'v'));
 s+='<use href="'+sk+'" transform="translate(0 '+(2*hy)+') scale(1 -1)" opacity=".32"'+c.bl(2.2)+'/>';
 s+=R(0,hy,W,H-hy,c.lg([[0,m.sea[1],.0],[1,'#000',.35]],'v'));
 var rip='';for(i=0;i<46;i++)rip+='M'+ii(c.rn(0,W))+' '+ii(hy+8+c.r()*c.r()*170)+'h'+ii(c.rn(14,60));
 s+=Ln(rip,mk==='night'?'#cfe0ff':'#fff',1.3,' opacity=".35"'+c.bl(.4));
 if(mk==='night')for(i=0;i<5;i++){x=c.rn(120,860);s+=El(x,hy+60,10,70,c.rg('#ffd58a',.45),SCR)}
 /* ponte e margem */
 s+=Pa('M0 458Q240 410 480 458T960 458V470H0Z',c.C('#2a323f'))+Ln('M0 458Q240 410 480 458T960 458',c.C('#58657a'),2)
 for(i=0;i<16;i++){x=i*64;s+=Ln('M'+x+' 458V'+ii(443+Math.abs(Math.sin(x*.0065))*-10),c.C('#58657a'),1)+(m.lamp>.2?Ci(x,434-Math.abs(Math.sin(x*.0065))*-8,3,'#fff1c8')+Ci(x,436,16,c.rg('#ffd58a',.6*m.lamp),SCR):'')}
 s+=R(0,470,W,70,c.lg([[0,c.C('#1d232d')],[1,c.C('#090c12')]],'v'))+R(0,470,W,3,c.C('#6f7f95'),' opacity=".6"');
 s+=Ln('M0 488H960',c.C('#3a4658'),3)+Ln(function(){var d='';for(var j=0;j<20;j++)d+='M'+(j*52)+' 488V532';return d}(),c.C('#2a323f'),2);
 s+=c.p(300,500,170,'M',{noshadow:1,t:'#0c0f15',l:'#0c0f15',s:'#1b1410',h:'#0c0f15'})+c.p(335,500,160,'W',{noshadow:1,t:'#0c0f15',l:'#0c0f15',s:'#1b1410',h:'#0c0f15'});
 s+=Ln('M700 540V380',c.C('#1a1f27'),6)+Ci(700,376,8,'#fff1c8')+c.glow(700,376,150,'#ffd58a',.7*Math.max(m.lamp,.3));
 return s};

S['park']=function(c,m){
 var s='',mk=c.mk,i,x,hy=300;
 s+=c.sky(hy,null,null);
 s+='<g'+c.bl(2)+'>'+c.bld(-20,980,hy-20,20,60,'#8da1b5',.7,{wmin:30,wmax:60})+'</g>';
 s+='<g'+c.bl(2.5)+'>'+c.trees(-30,990,hy+16,70,130,'#5d8a55',.55,.8)+'</g>'+c.trees(-30,990,hy+26,90,170,'#4a7a48',.38,1.1);
 /* gramado */
 s+=R(0,hy,W,H-hy,c.lg([[0,c.C('#8fb66a',.35)],[.4,c.C('#6f9e4a')],[1,c.C('#3f6a30')]],'v'));
 var st='';for(i=-8;i<9;i++)st+='M'+ii(480+i*14)+' '+hy+'L'+ii(480+i*180)+' '+H+'L'+ii(480+i*180+90)+' '+H+'L'+ii(480+i*14+7)+' '+hy+'Z';
 s+=Pa(st,'#fff',' opacity=".05"');
 /* caminho */
 s+=Pa('M455 '+hy+'L505 '+hy+'Q530 400 760 540H120Q440 420 455 '+hy+'Z',c.lg([[0,c.C('#d6c7a4',.4)],[1,c.C('#b6a47c')]],'v'));
 s+=Pa('M455 '+hy+'Q440 420 120 540H60Q420 430 450 '+hy+'Z',c.C('#2f5a2a'),' opacity=".35"');
 /* sombras de arvores no chao */
 if(mk!=='night')s+='<g'+c.bl(6)+MUL+'>'+El(250,400,200,26,mix(m.sk[0],'#000',.6),' opacity=".4"')+El(720,360,190,20,mix(m.sk[0],'#000',.6),' opacity=".35"')+'</g>';
 /* arvores medias */
 function tr(x,y,sz){return Pa('M'+(x-sz*.06)+' '+y+'L'+(x-sz*.04)+' '+ii(y-sz*.6)+'L'+(x+sz*.04)+' '+ii(y-sz*.6)+'L'+(x+sz*.06)+' '+y+'Z',c.C('#4a3a2c'))+'<g'+c.fol(sz*.1)+'>'+El(x,y-sz*.9,sz*.55,sz*.42,c.lg([[0,c.C('#7fae5c')],[1,c.C('#2f5a30')]],'v'))+El(x-sz*.34,y-sz*.78,sz*.28,sz*.24,c.C('#4f8a46'))+El(x+sz*.32,y-sz*.82,sz*.26,sz*.22,c.C('#3f7a3c'))+El(x-sz*.15,y-sz*1.05,sz*.3,sz*.18,c.C('#a3cf72'),' opacity=".5"')+'</g>'}
 s+=tr(150,420,200)+tr(840,400,220)+tr(300,350,100)+tr(660,340,90);
 /* poste e banco */
 s+=Ln('M610 372V290',c.C('#2a2f37'),3)+Ci(610,286,5,'#fff1c8')+c.glow(610,286,70,'#ffd9a0',.6*Math.max(m.lamp,.1));
 s+=R(600,356,70,5,c.C('#6b4a2a'))+R(600,336,70,14,c.C('#7f5a36'))+R(604,361,4,16,c.C('#222'))+R(662,361,4,16,c.C('#222'))+El(635,380,44,5,c.rg('#000',.4));
 /* pessoas */
 s+=c.p(300,430,120,'K',{d:.05})+c.p(335,428,114,'W',{d:.05,flip:1})+c.p(590,356,62,'K',{d:.2})+c.p(560,350,52,'M',{d:.25});
 /* cachorro */
 s+=Pa('M366 438Q372 428 386 430L396 424L398 432L390 438L388 446H384L383 440H372L371 446H367Z',c.C('#6b4a2a'));
 /* raios de sol */
 if(mk!=='night'){s+='<g'+SCR+c.bl(8)+'>';for(i=0;i<5;i++)s+=Pa('M'+ii(c.sun[0]+i*14)+' '+ii(c.sun[1])+'L'+ii(120+i*190)+' 540L'+ii(200+i*190)+' 540Z',m.sun,' opacity=".1"');s+='</g>'}
 /* primeiro plano desfocado */
 s+='<g'+c.bl(5)+'>'+Pa('M-20 540Q0 380 40 330Q60 440 100 540Z',c.C('#1f3a1c'))+El(930,540,70,26,c.C('#3f7a34'))+'</g>';
 s+=c.fog(hy-30,110,.35);
 return s};

S['beach']=function(c,m){
 var s='',mk=c.mk,hy=235,i,x,y;
 var sx=mk==='day'?640:mk==='dawn'?300:620;
 s+=c.sky(hy,sx,hy-(mk==='day'?160:mk==='night'?130:10));
 s+=R(0,hy,W,200,c.lg([[0,m.sea[1]],[1,m.sea[0]]],'v'));
 s+=El(c.sun[0],hy+4,230,8,c.rg(m.sun,.7),SCR);
 /* glitter */
 var gl='';for(i=0;i<34;i++){y=hy+4+i*i*.14+i*2;gl+='M'+ii(c.sun[0]-22-i*1.4+c.rn(-14,14))+' '+ii(y)+'h'+ii(c.rn(8,30)+i*.9)}
 s+=Ln(gl,mk==='night'?'#cfe0ff':'#fff7de',1.6,' opacity=".6"'+c.bl(.4));
 /* ondas */
 for(i=0;i<5;i++){y=hy+36+i*i*9;s+=Pa('M0 '+y+'Q240 '+(y-6-i*2)+' 480 '+y+'T960 '+(y-2)+'V'+(y+3+i*1.5)+'Q720 '+(y+8)+' 480 '+(y+3+i)+'T0 '+(y+6+i)+'Z','#fff',' opacity="'+n1(.1+i*.06)+'"'+c.bl(.6+i*.2))}
 /* velejador e navio */
 s+=Pa('M420 '+(hy-2)+'L442 '+(hy-30)+'L444 '+(hy-2)+'Z',c.C('#f4efe4',.4))+Pa('M446 '+(hy-2)+'L446 '+(hy-24)+'L462 '+(hy-2)+'Z',c.C('#f4efe4',.4))+R(414,hy-2,52,3,c.C('#2a3140',.4));
 /* areia */
 s+=Pa('M0 400Q200 365 480 380T960 360V540H0Z',c.lg([[0,c.C('#dcc79b')],[1,c.C('#b9a073')]],'v'));
 s+=Pa('M0 400Q200 365 480 380T960 360V368Q720 392 480 388T0 410Z','#fff',' opacity=".55"'+c.bl(.8))+Pa('M0 410Q200 376 480 392T960 372V392Q720 410 480 404T0 428Z',c.C('#8a7a58'),' opacity=".35"');
 s+=Ln('M0 455Q300 430 960 450',c.C('#a58b5e'),1,' opacity=".4"');
 /* guarda-sol e cadeiras */
 s+=Ln('M180 500L196 372',c.C('#e8e0cf'),3)+Pa('M120 380Q196 330 276 380Q196 372 120 380Z',c.C('#d9483b'))+Pa('M196 350L120 380Q150 364 196 350ZM196 350L276 380Q240 362 196 350Z','#fff',' opacity=".25"')+El(190,505,70,8,c.rg('#000',.4));
 s+=Pa('M236 500L300 470L316 482L252 512Z',c.C('#2f6b8a'));
 /* palmeira */
 var px=860;s+=Pa('M'+px+' 540Q'+(px-20)+' 380 '+(px-70)+' 250Q'+(px-60)+' 380 '+(px+10)+' 540Z',c.C('#3a2f26'))
 for(i=0;i<7;i++){var a=-170+i*30,ex=px-70+Math.cos(a*Math.PI/180)*150,ey=250+Math.sin(a*Math.PI/180)*90+40;s+=Pa('M'+(px-70)+' 250Q'+ii((px-70+ex)/2)+' '+ii(Math.min(250,ey)-50)+' '+ii(ex)+' '+ii(ey)+'Q'+ii((px-70+ex)/2)+' '+ii(Math.min(250,ey)-20)+' '+(px-70)+' 252Z',c.C(i%2?'#2f6a3a':'#3b7d45'))}
 /* pessoas */
 s+=c.p(430,430,100,'K',{d:.1})+c.p(466,430,95,'W',{d:.1})+c.p(640,402,58,'M',{d:.25})+c.p(300,418,70,'W',{d:.18,flip:1});
 s+=Pa('M0 540Q60 470 140 540Z',c.C('#8a7a58'),c.bl(5));
 s+=c.fog(hy-20,80,.4);
 return s};

S['mountain-trail']=function(c,m){
 var s='',mk=c.mk,hy=300,i;
 s+=c.sky(hy,null,null);
 /* cumes com neve */
 function peak(x,top,w,col,d){var b=hy+60;return Pa('M'+(x-w)+' '+b+'L'+(x-w*.42)+' '+ii(top+(b-top)*.35)+'L'+(x-w*.18)+' '+ii(top+(b-top)*.28)+'L'+x+' '+top+'L'+(x+w*.22)+' '+ii(top+(b-top)*.3)+'L'+(x+w*.5)+' '+ii(top+(b-top)*.4)+'L'+(x+w)+' '+b+'Z',c.lg([[0,mix(c.C(col,d),'#fff',.1)],[1,c.C(col,d+.08)]],'v'))+Pa('M'+x+' '+top+'L'+(x-w*.18)+' '+ii(top+(b-top)*.28)+'L'+(x-w*.08)+' '+ii(top+(b-top)*.34)+'L'+(x+w*.02)+' '+ii(top+(b-top)*.26)+'L'+(x+w*.1)+' '+ii(top+(b-top)*.34)+'L'+(x+w*.22)+' '+ii(top+(b-top)*.3)+'Z',c.C('#f4f7fb',d*.8),' opacity=".92"')+Pa('M'+x+' '+top+'L'+(x+w*.22)+' '+ii(top+(b-top)*.3)+'L'+(x+w*.5)+' '+ii(top+(b-top)*.4)+'L'+(x+w)+' '+b+'L'+(x+w*.3)+' '+b+'Z','#12213a',' opacity=".25"')}
 s+='<g'+c.bl(.6)+'>'+peak(300,70,300,'#7f92ab',.5)+peak(700,40,360,'#6f829b',.42)+peak(930,110,200,'#7a8da6',.5)+'</g>';
 s+=c.fog(hy-40,120,.55);
 s+=c.ridge(hy+30,26,'#58708a',.35,1.7);
 /* florestas em faixas (padrao de pinheiros) */
 s+=R(0,hy-8,W,70,pines(c,0,56,'#3f6b57',.35,34))+c.fog(hy+14,50,.4);
 s+=c.ridge(hy+78,16,'#41655a',.2,4)
 s+=R(0,hy+34,W,96,pines(c,0,86,'#2d5844',.2,52));
 s+=R(0,hy+95,W,H-hy-95,c.lg([[0,c.C('#5d7f45')],[1,c.C('#2f4a2a')]],'v'));
 /* lago */
 s+=El(330,hy+112,210,12,c.lg([[0,m.sk[1]],[1,m.sk[2]]],'h'),' opacity=".85"')+El(330,hy+114,200,3,'#fff',' opacity=".35"');
 /* trilha */
 s+=Pa('M520 '+(hy+100)+'Q640 380 470 440Q330 490 380 540H760Q690 470 600 440Q530 400 560 '+(hy+100)+'Z',c.lg([[0,c.C('#c9b48a',.35)],[1,c.C('#a8916a')]],'v'));
 s+=Ln('M545 '+(hy+104)+'Q640 380 480 438',c.C('#e6d6b0'),2,' opacity=".5"');
 /* pedras e flores */
 for(i=0;i<9;i++)s+=El(60+i*100+c.rn(-30,30),c.rn(440,520),c.rn(14,32),c.rn(8,16),c.C('#7d7f80'),' opacity=".95"')
 for(i=0;i<40;i++)s+=Ci(c.rn(0,W),c.rn(420,530),c.rn(1.5,3),c.pk(['#f2d34a','#fff','#c24ac2','#f58a3a']),' opacity=".85"');
 /* trilheiro */
 s+=c.p(540,432,86,'K',{d:.05,t:'#c9482f',l:'#2a3140'})+Pa('M522 380L538 376L540 404L524 408Z',c.C('#2f5d62'));
 /* pinheiros primeiro plano */
 var fg=pines(c,0,230,'#18351f',0,96);
 s+='<g'+c.bl(3)+'>'+R(-10,240,190,300,fg)+R(800,230,170,310,fg)+'</g>';
 if(mk!=='night'){s+='<g'+SCR+c.bl(9)+'>';for(i=0;i<4;i++)s+=Pa('M'+ii(c.sun[0]+i*10)+' '+ii(c.sun[1])+'L'+(200+i*180)+' 540L'+(290+i*180)+' 540Z',m.sun,' opacity=".1"');s+='</g>'}
 return s};

S['countryside']=function(c,m){
 var s='',mk=c.mk,hy=240,i,x;
 s+=c.sky(hy,null,null);
 s+=c.ridge(hy+14,18,'#7d94a8',.55,2.2)+c.ridge(hy+30,22,'#6b8a6a',.4,.4);
 /* campos em faixas */
 var fc=['#d2b24a','#7da34a','#b9894a','#9bb556'],yy=hy+26,k;
 for(i=0;i<4;i++){var y2=hy+26+(i+1)*(i+1)*13;s+=R(0,yy-1,W,y2-yy+2,c.lg([[0,c.C(fc[i],.25-i*.05)],[1,c.C(fc[i])]],'v'));yy=y2}
 s+=R(0,yy-1,W,H-yy+1,c.lg([[0,c.C('#7da34a')],[1,c.C('#3f6a2f')]],'v'));
 var rows='';for(i=-12;i<13;i++)rows+='M'+ii(520+i*10)+' '+(hy+26)+'L'+ii(520+i*95)+' '+H;
 s+=Ln(rows,'#000',1.4,' opacity=".12"');
 s+=Ln(function(){var d='',j;for(j=-12;j<13;j+=2)d+='M'+ii(520+j*10+5)+' '+(hy+26)+'L'+ii(520+j*95+48)+' '+H;return d}(),'#fff',2,' opacity=".07"');
 /* estrada */
 s+=Pa('M430 '+(hy+28)+'L450 '+(hy+28)+'Q470 360 700 540H270Q440 400 430 '+(hy+28)+'Z',c.lg([[0,c.C('#c8b08a',.35)],[1,c.C('#a48a64')]],'v'));
 /* fazenda */
 var fx=620,fy=hy+34;
 s+=R(fx,fy-26,46,26,c.C('#b8402f'))+Pa('M'+(fx-4)+' '+(fy-26)+'L'+(fx+23)+' '+(fy-44)+'L'+(fx+50)+' '+(fy-26)+'Z',c.C('#5a3a2c'))+R(fx+14,fy-14,18,14,c.C('#f4efe4'))+R(fx+50,fy-30,34,30,c.C('#efe7d6'))+Pa('M'+(fx+46)+' '+(fy-30)+'L'+(fx+67)+' '+(fy-46)+'L'+(fx+88)+' '+(fy-30)+'Z',c.C('#7a3f2c'))+Pa('M'+(fx-4)+' '+(fy-26)+'L'+(fx+23)+' '+(fy-44)+'L'+(fx+23)+' '+(fy-26)+'Z','#000',' opacity=".15"');
 s+=c.trees(fx-60,fx-10,fy+3,34,56,'#3f6a3a',.3,1)+c.trees(fx+96,fx+150,fy+3,30,52,'#3f6a3a',.3,1);
 /* cerca */
 var fd='';for(i=0;i<22;i++){x=60+i*i*1.4+i*20;fd+='M'+ii(x)+' '+(hy+210+i*.5)+'v'+ii(-18-i*.5)}
 /* arvores grandes e feno */
 function oak(x,y,sz){return Pa('M'+(x-sz*.05)+' '+y+'L'+(x-sz*.03)+' '+ii(y-sz*.7)+'L'+(x+sz*.03)+' '+ii(y-sz*.7)+'L'+(x+sz*.05)+' '+y+'Z',c.C('#4a3a2c'))+'<g'+c.fol(sz*.12)+'>'+El(x,y-sz*.95,sz*.55,sz*.38,c.lg([[0,c.C('#86b05a')],[1,c.C('#2f5a30')]],'v'))+El(x-sz*.38,y-sz*.8,sz*.26,sz*.2,c.C('#4f8a46'))+El(x+sz*.36,y-sz*.82,sz*.24,sz*.2,c.C('#3f7a3c'))+El(x-sz*.18,y-sz*1.08,sz*.28,sz*.16,c.C('#b5d97c'),' opacity=".45"')+'</g>'+El(x,y,sz*.5,sz*.05,c.rg('#000',.4))}
 s+=oak(180,330,170)+oak(780,310,120);
 s+=El(120,470,46,34,c.lg([[0,c.C('#e2c565')],[1,c.C('#a8883a')]],'v'))+El(215,500,52,38,c.lg([[0,c.C('#e2c565')],[1,c.C('#a8883a')]],'v'));
 /* sombras de nuvens */
 s+='<g'+c.bl(18)+MUL+'>'+El(300,330,220,26,mix(m.sk[0],'#000',.5),' opacity=".3"')+El(740,290,160,16,mix(m.sk[0],'#000',.5),' opacity=".25"')+'</g>';
 /* capim em primeiro plano */
 var gr='';for(i=0;i<46;i++){x=c.rn(0,W);gr+='M'+ii(x)+' 545Q'+ii(x+c.rn(-14,14))+' '+ii(c.rn(450,500))+' '+ii(x+c.rn(-30,30))+' '+ii(c.rn(420,480))}
 s+='<g'+c.bl(1.6)+'>'+Ln(gr,c.C('#4f7a2a'),2.2)+'</g>';
 for(i=0;i<18;i++)s+=Ci(c.rn(0,W),c.rn(470,530),c.rn(2,4),c.pk(['#d9382f','#f5f0e4']),' opacity=".9"'+c.bl(1));
 s+=c.fog(hy-10,70,.3);
 return s};

/* ---------- exteriores (2): pracas, templo, feira ---------- */
function palm(c,px,py,h,lean){
 var s=Pa('M'+px+' '+py+'Q'+(px+lean*.2)+' '+(py-h*.5)+' '+(px+lean)+' '+(py-h)+'Q'+(px+lean*.3+7)+' '+(py-h*.5)+' '+(px+9)+' '+py+'Z',c.lg([[0,c.C('#7a6248')],[1,c.C('#3e2f22')]],'h')),i,tx=px+lean,ty=py-h,L=h*.55,g='';
 for(i=0;i<8;i++){var a=(-165+i*330/7)*Math.PI/180,ex=tx+Math.cos(a)*L,ey=ty+Math.sin(a)*L*.55+L*.35;
  g+=Pa('M'+ii(tx)+' '+ii(ty)+'Q'+ii((tx+ex)/2)+' '+ii(Math.min(ty,ey)-L*.28)+' '+ii(ex)+' '+ii(ey)+'Q'+ii((tx+ex)/2)+' '+ii(Math.min(ty,ey)-L*.05)+' '+ii(tx)+' '+(ii(ty)+2)+'Z',c.C(i%2?'#2f6a3a':'#4a8a46'))}
 return s+'<g'+c.fol(6)+'>'+g+'</g>'}
function wpt(c,x,y,tw,th,gl,fr,arch){
 var t=Pa(arch?'M'+(tw*.25)+' '+(th*.62)+'V'+(th*.3)+'Q'+(tw*.5)+' '+(th*.08)+' '+(tw*.75)+' '+(th*.3)+'V'+(th*.62)+'Z':'M'+(tw*.25)+' '+(th*.2)+'H'+(tw*.75)+'V'+(th*.68)+'H'+(tw*.25)+'Z',gl)+R(tw*.2,th*.68,tw*.6,th*.05,fr);
 return c.pat(tw,th,t,' patternTransform="translate('+ii(x)+' '+ii(y)+')"')}
function slate(c,x,y,w,h,col){return Pa('M'+(x-8)+' '+y+'L'+(x+12)+' '+(y-h)+'L'+(x+w-12)+' '+(y-h)+'L'+(x+w+8)+' '+y+'Z',c.lg([[0,mix(c.C(col),'#fff',.12)],[1,c.C(col)]],'v'))}

S['plaza-europe']=function(c,m){
 var s='',mk=c.mk,i,x,hy=330;
 s+=c.sky(hy,null,null);
 var cols=['#e6d3b0','#d9a96a','#cdd6d9','#e2b6a8','#efe3c8','#c9b79a'],bx=-10,k=0,fac='';
 while(bx<960){var w1=110+(k*37%50),h1=150+((k*61)%60);
  var col=c.C(cols[k%6],.12);
  fac+=R(bx,hy-h1,w1,h1,c.lg([[0,mix(col,'#fff',.08)],[1,mix(col,'#000',.12)]],'h'))+R(bx,hy-h1+16,w1,h1-62,wpt(c,bx,hy-h1+16,30,46,mk==='night'?'#ffcf86':c.C('#34475a'),c.C('#f3ead8'),k%2))+slate(c,bx,hy-h1,w1,46,'#4a5560')+R(bx+w1*.3,hy-h1-60,10,26,c.C('#7a5a4a'))+R(bx,hy-h1,w1,3,c.C('#fff'),' opacity=".4"')+Ln('M'+ii(bx+w1)+' '+(hy-h1-40)+'V'+hy,'#000',1.5,' opacity=".2"');
  bx+=w1;k++}
 s+='<g'+c.bl(.5)+'>'+fac+'</g>';
 /* torre da igreja */
 s+=R(130,70,64,260,c.lg([[0,c.C('#d9c9a6')],[1,c.C('#a8946e')]],'h'))+Pa('M122 74L162 -20L202 74Z',c.C('#5a6b6a'))+Ci(162,118,16,c.C('#f4efe2'))+Ln('M162 118V108M162 118L170 122','#222',2)+Pa('M146 190V160Q162 140 178 160V190Z',c.C('#2a2d33'))+Pa('M146 260V230Q162 210 178 230V260Z',c.C('#2a2d33'));
 /* arcada terrea e chao */
 s+=R(0,hy-40,W,40,c.lg([[0,c.C('#2b2f36')],[1,c.C('#5a4a3a')]],'v'),' opacity=".8"');
 s+=R(0,hy,W,H-hy,c.lg([[0,c.C('#b9ab94',.3)],[1,c.C('#8d806b')]],'v'));
 var cb=c.pat(18,9,Ci(5,3,3.4,'#fff',' opacity=".07"')+Ci(14,6,3.2,'#000',' opacity=".07"'));
 s+=R(0,hy,W,H-hy,cb)+c.fog(hy,40,.4);
 if(mk!=='night')s+='<g'+c.bl(5)+MUL+'>'+Pa('M0 '+hy+'L560 '+hy+'L360 440L-80 440Z',mix(m.sk[0],'#000',.55),' opacity=".32"')+'</g>';
 /* fonte */
 var fx=500,fy=420;
 s+=El(fx,fy+16,150,34,c.lg([[0,c.C('#cfc8b8')],[1,c.C('#8d8676')]],'v'))+El(fx,fy+8,138,28,c.lg([[0,m.sk[1]],[1,m.sk[2]]],'v'))+El(fx,fy+8,138,28,'none',' stroke="#f4efe2" stroke-width="3"')
 s+=R(fx-9,fy-70,18,76,c.lg([[0,c.C('#d9d2c0')],[1,c.C('#8d8676')]],'h'))+El(fx,fy-70,48,10,c.C('#cfc8b8'))+R(fx-5,fy-110,10,42,c.C('#bdb6a4'))+El(fx,fy-112,26,6,c.C('#cfc8b8'));
 s+='<g'+c.bl(.9)+'>'+Ln('M'+fx+' '+(fy-118)+'Q'+(fx-50)+' '+(fy-140)+' '+(fx-70)+' '+(fy-72)+'M'+fx+' '+(fy-118)+'Q'+(fx+50)+' '+(fy-140)+' '+(fx+70)+' '+(fy-72)+'M'+fx+' '+(fy-118)+'V'+(fy-160),'#fff',3,' opacity=".75"')+El(fx-62,fy+4,16,5,'#fff',' opacity=".55"')+El(fx+64,fy+4,16,5,'#fff',' opacity=".55"')+'</g>';
 /* arvores */
 function plane(x,y,sz){return Pa('M'+(x-5)+' '+y+'L'+(x-3)+' '+(y-sz*.7)+'L'+(x+3)+' '+(y-sz*.7)+'L'+(x+5)+' '+y+'Z',c.C('#6a5a48'))+'<g'+c.fol(18)+'>'+El(x,y-sz*.95,sz*.5,sz*.32,c.lg([[0,c.C('#7fa65a')],[1,c.C('#35603a')]],'v'))+El(x-sz*.34,y-sz*.82,sz*.22,sz*.2,c.C('#4f7e44'))+El(x+sz*.34,y-sz*.84,sz*.22,sz*.2,c.C('#406e3c'))+'</g>'}
 s+=plane(60,362,190)+plane(900,372,210)+plane(280,350,120);
 /* mesas */
 function sun(x,y,w,col){return Ln('M'+x+' '+y+'V'+(y+90),c.C('#3a3a3a'),3)+Pa('M'+(x-w)+' '+(y+4)+'Q'+x+' '+(y-34)+' '+(x+w)+' '+(y+4)+'Q'+x+' '+(y+12)+' '+(x-w)+' '+(y+4)+'Z',c.C(col))+Pa('M'+x+' '+(y-14)+'L'+(x-w*.3)+' '+(y+8)+'M'+x+' '+(y-14)+'L'+(x+w*.3)+' '+(y+8),'none',' stroke="#fff" stroke-opacity=".3" stroke-width="1.5"')}
 s+=c.p(720,478,118,'S',{noshadow:1,t:'#a85a44'})+c.p(790,480,112,'S',{noshadow:1,flip:1,t:'#4b4e6d'})+sun(752,382,70,'#f0e6cf')+El(756,486,44,9,c.C('#2f2f33'))+R(752,486,3,34,c.C('#2f2f33'));
 s+=c.p(300,460,125,'W',{d:.05})+c.p(335,462,120,'M',{d:.05,flip:1})+c.p(150,420,96,'K',{d:.15})+c.p(610,400,80,'M',{d:.2});
 for(i=0;i<7;i++)s+=El(c.rn(360,640),c.rn(430,520),4.5,2.6,c.C('#6f6f78'));
 s+=Ln('M880 380V300',c.C('#222'),4)+Ci(880,296,7,'#fff1c8')+c.glow(880,296,100,'#ffd9a0',.5*Math.max(m.lamp,.15));
 s+=c.fog(hy-30,90,.35);
 return s};

S['plaza-latin']=function(c,m){
 var s='',mk=c.mk,i,x,hy=345;
 s+=c.sky(hy,null,null);
 /* fachadas coloridas */
 var pal=['#e0a84a','#c4553a','#2f8f8a','#d97a8a','#f0c94a','#d9733a'],bx=-20,k=0;
 function col(x0,x1,h,cl){var w1=x1-x0,o='';
  o+=R(x0,hy-h,w1,h,c.lg([[0,mix(c.C(cl),'#fff',.1)],[1,mix(c.C(cl),'#000',.18)]],'h'));
  o+=R(x0+6,hy-h+30,w1-12,h-82,wpt(c,x0+6,hy-h+30,38,52,c.C('#2a3038'),c.C('#f4efe2'),1));
  o+=Pa('M'+(x0-6)+' '+(hy-h)+'H'+(x1+6)+'V'+(hy-h-14)+'H'+(x0-6)+'Z',c.C('#b5472f'))+R(x0,hy-h+22,w1,6,c.C('#fff'),' opacity=".4"');
  o+=R(x0,hy-52,w1,52,c.C('#3a2b22'),' opacity=".55"');
  var d='';for(var j=x0+14;j<x1-24;j+=44)d+='M'+j+' '+(hy-52)+'v-6h26v6';
  return o+Ln(d,'#1a1a1a',2)+R(x0,hy-h+60,w1,3,c.C('#1a1a1a'),' opacity=".35"')}
 s+=col(-10,150,200,pal[0])+col(150,300,170,pal[2])+col(660,810,180,pal[1])+col(810,970,210,pal[3]);
 s+=R(300,hy-170,60,170,c.C('#e8dcc4'))+R(600,hy-170,60,170,c.C('#e8dcc4'));
 /* igreja */
 var cx=480;
 s+=R(cx-130,hy-200,260,200,c.lg([[0,c.C('#f0e6cf')],[1,c.C('#cdbf9f')]],'h'))+R(cx-170,hy-260,84,260,c.lg([[0,c.C('#efe3c8')],[1,c.C('#c4b594')]],'h'))+R(cx+86,hy-260,84,260,c.lg([[0,c.C('#efe3c8')],[1,c.C('#c4b594')]],'h'));
 s+=Pa('M'+(cx-176)+' '+(hy-260)+'Q'+(cx-128)+' '+(hy-350)+' '+(cx-80)+' '+(hy-260)+'Z',c.lg([[0,c.C('#4a8fa8')],[1,c.C('#2a5f78')]],'v'))+Pa('M'+(cx+80)+' '+(hy-260)+'Q'+(cx+128)+' '+(hy-350)+' '+(cx+176)+' '+(hy-260)+'Z',c.lg([[0,c.C('#4a8fa8')],[1,c.C('#2a5f78')]],'v'));
 s+=Ln('M'+(cx-128)+' '+(hy-338)+'V'+(hy-366)+'M'+(cx-138)+' '+(hy-356)+'H'+(cx-118)+'M'+(cx+128)+' '+(hy-338)+'V'+(hy-366)+'M'+(cx+118)+' '+(hy-356)+'H'+(cx+138),c.C('#d9b45a'),3);
 s+=Pa('M'+(cx-136)+' '+(hy-220)+'V'+(hy-190)+'Q'+(cx-128)+' '+(hy-206)+' '+(cx-120)+' '+(hy-190)+'V'+(hy-220)+'Q'+(cx-128)+' '+(hy-236)+' '+(cx-136)+' '+(hy-220)+'ZM'+(cx+120)+' '+(hy-220)+'V'+(hy-190)+'Q'+(cx+128)+' '+(hy-206)+' '+(cx+136)+' '+(hy-190)+'V'+(hy-220)+'Q'+(cx+128)+' '+(hy-236)+' '+(cx+120)+' '+(hy-220)+'Z',c.C('#2a2d33'))+Ci(cx,hy-150,26,c.C('#c9b99a'))+Ci(cx,hy-150,19,c.lg([[0,c.C('#4a8fa8')],[1,c.C('#e8c35a')]],'v'))+Pa('M'+(cx-34)+' '+hy+'V'+(hy-70)+'Q'+cx+' '+(hy-112)+' '+(cx+34)+' '+(hy-70)+'V'+hy+'Z',c.C('#4a3224'))+Pa('M'+(cx-130)+' '+(hy-200)+'L'+cx+' '+(hy-250)+'L'+(cx+130)+' '+(hy-200)+'Z',c.C('#cdbf9f'));
 s+=Ln('M'+(cx-130)+' '+(hy-200)+'H'+(cx+130),'#000',2,' opacity=".2"');
 s+=c.fog(hy-100,90,.25)
 /* bandeirinhas */
 var bp='M-10 120Q240 190 480 130T970 150',fl=['#e23d3d','#f2c230','#2f8f8a','#e86aa0'];
 for(i=0;i<4;i++)s+=Ln(bp,fl[i],14,' stroke-dasharray="9 27" stroke-dashoffset="'+(-i*9)+'"');
 s+=Ln(bp,'#2a2a2a',1);
 /* chao */
 s+=R(0,hy,W,H-hy,c.lg([[0,c.C('#d9c7a6',.2)],[1,c.C('#a8906c')]],'v'));
 var tl=c.pat(46,24,Pa('M23 0L46 12L23 24L0 12Z',c.C('#e9d8b4'),' opacity=".5"')+Pa('M23 0L46 12L23 24L0 12Z','none',' stroke="'+c.C('#8a7254')+'" stroke-width="1.4" opacity=".5"'));
 s+=R(0,hy,W,H-hy,tl)+R(0,hy,W,H-hy,c.lg([[0,m.fog,.8],[.5,m.fog,0]],'v'));
 if(mk!=='night')s+='<g'+c.bl(5)+MUL+'>'+Pa('M0 '+hy+'L500 '+hy+'L300 470L-100 470Z',mix(m.sk[0],'#000',.5),' opacity=".3"')+'</g>';
 s+=palm(c,120,400,230,-25)+palm(c,860,390,250,30);
 /* quiosque / carrinho */
 s+=R(650,420,90,34,c.C('#2f8f8a'))+Pa('M640 420L690 384L750 420Z',c.lg([[0,c.C('#f2c230')],[1,c.C('#e23d3d')]],'h'))+R(654,454,6,24,c.C('#222'))+R(730,454,6,24,c.C('#222'))+El(695,482,50,6,c.rg('#000',.4));
 s+=c.p(570,470,128,'W',{t:'#e23d3d',d:.02})+c.p(610,472,122,'M',{t:'#f4efe2',flip:1})+c.p(400,440,96,'K',{d:.12,t:'#2f8f8a'})+c.p(300,452,104,'W',{t:'#f2c230',d:.08,flip:1})+c.p(700,452,96,'M',{noshadow:1,t:'#d9d2c4'});
 for(i=0;i<6;i++)s+=El(c.rn(380,560),c.rn(480,525),4.6,2.6,c.C('#6f6f78'));
 return s};

S['temple-asia']=function(c,m){
 var s='',mk=c.mk,i,hy=300,cx=480;
 s+=c.sky(hy,null,null);
 s+=c.ridge(hy-40,60,'#7d8fa5',.6,.7)+c.fog(hy-120,130,.6)+c.ridge(hy+10,44,'#6a8294',.45,2.4)+c.fog(hy-50,120,.5)+c.ridge(hy+50,30,'#4f6e70',.3,5);
 s+='<g'+c.bl(1)+'>'+R(0,hy+10,W,70,pines(c,0,52,'#355b4a',.3,30))+'</g>'+c.fog(hy+10,70,.4);
 /* patio e escadaria */
 s+=R(0,hy+60,W,H-hy-60,c.lg([[0,c.C('#b9b2a2',.3)],[1,c.C('#8a8374')]],'v'));
 /* pagode */
 var rc=c.C('#2d2a33'),bc=c.C('#b0332c'),t,y,w1;
 for(t=0;t<5;t++){w1=130-t*20;y=420-t*66;
  s+=R(cx-w1+14,y-34,2*w1-28,34,c.lg([[0,mix(bc,'#fff',.1)],[1,mix(bc,'#000',.25)]],'v'))+R(cx-w1+14,y-34,2*w1-28,4,c.C('#e6c25a'))
  s+=Pa('M'+(cx-w1-34)+' '+(y-34+12)+'Q'+(cx-w1*.6)+' '+(y-34+14)+' '+(cx-w1*.32)+' '+(y-60)+'L'+cx+' '+(y-70-t*2)+'L'+(cx+w1*.32)+' '+(y-60)+'Q'+(cx+w1*.6)+' '+(y-34+14)+' '+(cx+w1+34)+' '+(y-34+12)+'Q'+(cx+w1*.7)+' '+(y-34+22)+' '+cx+' '+(y-34+20)+'Q'+(cx-w1*.7)+' '+(y-34+22)+' '+(cx-w1-34)+' '+(y-34+12)+'Z',c.lg([[0,mix(rc,'#fff',.14)],[1,rc]],'v'));
  s+=Ln('M'+(cx-w1-34)+' '+(y-22)+'Q'+(cx-w1*.6)+' '+(y-20)+' '+(cx-w1*.32)+' '+(y-60),mix(rc,m.sun,.5),1.6,' opacity=".6"')+Ci(cx-w1-34,y-22,2.4,c.C('#e6c25a'))+Ci(cx+w1+34,y-22,2.4,c.C('#e6c25a'));
  var d='';for(var j=-3;j<=3;j+=2)d+='M'+(cx+j*w1/5)+' '+(y-30)+'v26';
  s+=Ln(d,'#1a0c0c',3,' opacity=".5"')}
 s+=Ln('M'+cx+' 78V20',c.C('#e6c25a'),3)+El(cx,50,6,10,c.C('#e6c25a'));
 s+=c.fog(300,160,.3);
 /* degraus */
 var st='';for(i=0;i<9;i++)st+=Pa('M'+(cx-120-i*14)+' '+(430+i*13)+'H'+(cx+120+i*14)+'V'+(443+i*13)+'H'+(cx-120-i*14)+'Z',c.lg([[0,c.C('#cfc8b8')],[1,c.C('#8f887a')]],'v'),' stroke="#000" stroke-opacity=".12"');
 s+=st;
 /* lanternas de pedra */
 function sl(x,y,sz){return R(x-sz*.08,y-sz*.6,sz*.16,sz*.6,c.C('#8f887a'))+R(x-sz*.22,y-sz*.82,sz*.44,sz*.24,c.C('#a39c8c'))+R(x-sz*.12,y-sz*.76,sz*.24,sz*.12,'#ffd9a0',' opacity="'+(.25+m.lamp*.7)+'"')+Pa('M'+(x-sz*.34)+' '+(y-sz*.82)+'L'+x+' '+(y-sz*1.06)+'L'+(x+sz*.34)+' '+(y-sz*.82)+'Z',c.C('#6f695c'))+c.glow(x,y-sz*.7,sz*.5,'#ffd9a0',.4*Math.max(m.lamp,.15))}
 s+=sl(190,480,120)+sl(770,480,120);
 /* torii */
 var tr=c.C('#c0392b');
 s+=R(300,230,24,310,c.lg([[0,mix(tr,'#fff',.1)],[1,mix(tr,'#000',.3)]],'h'))+R(636,230,24,310,c.lg([[0,mix(tr,'#fff',.1)],[1,mix(tr,'#000',.3)]],'h'))+R(296,300,368,16,tr)+Pa('M250 232Q480 252 710 232L720 214Q480 236 240 214Z',c.C('#17141a'))+R(290,244,380,14,tr)+R(300,520,24,20,c.C('#17141a'))+R(636,520,24,20,c.C('#17141a'));
 /* lanternas penduradas */
 for(i=0;i<5;i++){var lx=360+i*60;s+=Ln('M'+lx+' 316V'+(332+(i%2)*6),'#222',1)+El(lx,350+(i%2)*6,10,15,c.lg([[0,'#ff7a5a'],[1,'#c0392b']],'v'))+c.glow(lx,350+(i%2)*6,50,'#ff9a6a',.55*Math.max(m.lamp,.3))}
 /* sakura */
 var bg='<g'+c.bl(1.4)+'>';
 for(i=0;i<46;i++)bg+=Ci(c.rn(520,960)-c.r()*c.r()*140,c.rn(0,150)+c.r()*c.r()*80,c.rn(8,24),c.rg(c.pk(['#ffc6d9','#ffadc8','#fff0f5']),.9));
 s+=Ln('M960 40Q820 60 740 120Q690 160 650 150',c.C('#3a2a2a'),9)+Ln('M840 70Q800 40 740 40',c.C('#3a2a2a'),5)+bg+'</g>';
 for(i=0;i<22;i++)s+=El(c.rn(0,W),c.rn(120,520),3.2,1.8,'#ffc6d9',' opacity="'+n1(c.rn(.4,.9))+'"');
 s+=c.p(430,500,120,'W',{t:'#d9488a',l:'#f4efe2',d:0})+c.p(470,500,118,'M',{t:'#2f4858',d:0,flip:1});
 s+=c.fog(hy-10,60,.25);
 return s};

S['market']=function(c,m){
 var s='',mk=c.mk,i,x,hy=330;
 s+=c.sky(hy,null,null);
 s+='<g'+c.bl(2.2)+'>'+c.bld(-20,980,hy+6,150,250,'#c9b79a',.4,{wmin:60,wmax:110})+'</g>'+c.fog(hy-100,110,.4);
 s+=R(0,hy,W,H-hy,c.lg([[0,c.C('#b5a78f',.3)],[1,c.C('#8a7c64')]],'v'));
 s+=R(0,hy,W,H-hy,c.pat(18,9,Ci(5,3,3.4,'#fff',' opacity=".07"')+Ci(14,6,3.2,'#000',' opacity=".07"')));
 var pr=[c.pat(16,13,Ci(4,4,4,c.C('#d9382f'))+Ci(12,8,4,c.C('#d9382f'))+Ci(3,11,2,'#fff',' opacity=".3"')),c.pat(16,13,Ci(4,4,4.2,c.C('#f08a24'))+Ci(12,8,4.2,c.C('#f5a63a'))),c.pat(16,13,Ci(4,4,4.5,c.C('#4f9a3a'))+Ci(12,8,4.5,c.C('#79b84a'))+Ci(8,2,3,c.C('#2f6a2a'))),c.pat(16,13,Ci(4,4,4,c.C('#f2d33a'))+Ci(12,8,4,c.C('#e8c22a')))];
 var aw=c.pat(36,10,R(0,0,18,10,c.C('#f4efe2'))+R(18,0,18,10,c.C('#d9382f')),' patternTransform="translate(0 0)"');
 var sc=[[20,300,'#d9382f'],[340,300,'#2f7a8a'],[660,280,'#e0a82a']];
 for(i=0;i<3;i++){var sx=sc[i][0],sw=sc[i][1];
  s+=R(sx+10,230,6,200,c.C('#5a4632'))+R(sx+sw-16,230,6,200,c.C('#5a4632'));
  s+=R(sx+16,250,sw-32,170,c.lg([[0,c.C('#2a2420')],[1,c.C('#5a4a3a')]],'v'),' opacity=".7"');
  s+=c.p(sx+sw*.5,380,150,i%2?'M':'W',{noshadow:1,t:['#e8e0cf','#8a3a3a','#2f5d62'][i],d:.02});
  s+=R(sx,372,sw,16,c.lg([[0,c.C('#a8794a')],[1,c.C('#6b4a2a')]],'v'));
  s+=R(sx+8,388,sw-16,48,c.C('#5a3c24'),' opacity=".9"');
  var n=Math.floor((sw-30)/70);for(var j=0;j<n;j++)s+=R(sx+18+j*70+(sw-30-n*70)/2,346,62,30,pr[(i+j)%4])+R(sx+18+j*70+(sw-30-n*70)/2,372,62,16,c.C('#b08a52'));
  s+=Pa('M'+(sx-8)+' 190H'+(sx+sw+8)+'L'+(sx+sw+16)+' 252H'+(sx-16)+'Z',aw)+Pa('M'+(sx-16)+' 252'+function(){var d='',q;for(q=0;q<sw/20;q++)d+='q10 14 20 0';return d}()+'V240H'+(sx-16)+'Z',aw)+Pa('M'+(sx-8)+' 190H'+(sx+sw+8)+'L'+(sx+sw+16)+' 252H'+(sx-16)+'Z',c.lg([[0,'#fff',.25],[1,'#000',.3]],'v'))}
 /* luzes */
 var d='M0 160Q240 210 480 150T960 170';s+=Ln(d,'#2a2a2a',1);
 for(i=0;i<22;i++){x=i*44+10;var y=160+Math.sin(x*.0065+1)*26+ (x>480?0:0);s+=Ci(x,y+6,3,'#fff1c8')+Ci(x,y+6,18,c.rg('#ffd58a',.55*Math.max(m.lamp,.35)),SCR)}
 /* clientes */
 s+=c.p(150,470,168,'W',{d:0,t:'#d9482f'})+c.p(205,478,176,'M',{d:0,flip:1,t:'#2f4858'})+c.p(820,486,184,'W',{d:0,t:'#2f6b4f',flip:1})+c.p(500,440,128,'K',{d:.05,t:'#b9873b'});
 s+=Pa('M140 400Q150 440 175 400Z',c.C('#c9a45a'));
 s+=El(480,500,420,28,c.rg('#000',.18));
 if(mk!=='night'){s+='<g'+SCR+c.bl(8)+'>';for(i=0;i<5;i++)s+=Pa('M'+ii(c.sun[0]+i*10)+' '+ii(c.sun[1])+'L'+(120+i*200)+' 540L'+(190+i*200)+' 540Z',m.sun,' opacity=".1"');s+='</g>'}
 return s};

/* ---------- interiores (1) ---------- */
function floorP(c,y0,a,b,vx,n,lc){
 var s=R(0,y0,W,H-y0,c.lg([[0,c.C(a)],[1,c.C(b)]],'v')),d='',i;
 for(i=-n;i<=n;i++)d+='M'+ii(vx+i*30)+' '+y0+'L'+ii(vx+i*190)+' '+H;
 return s+Ln(d,lc||'#000',1,' opacity=".13"')}
function pend(c,x,len,col,r){
 var m=c.m,s=Ln('M'+x+' 0V'+len,c.C('#222'),1.5)+Pa('M'+(x-r)+' '+(len+r*.55)+'Q'+x+' '+(len-r*.4)+' '+(x+r)+' '+(len+r*.55)+'Z',c.C(col));
 s+=Ci(x,len+r*.5,r*.5,c.rg('#fff1c8',.9),' opacity="'+(.25+m.lamp*.75)+'"'+SCR)+c.glow(x,len+r*.9,r*3.2,'#ffcf8a',.5*Math.max(m.lamp,.2));
 return s+Pa('M'+(x-r*.6)+' '+(len+r*.6)+'L'+(x-r*2.4)+' '+(len+r*5)+'L'+(x+r*2.4)+' '+(len+r*5)+'L'+(x+r*.6)+' '+(len+r*.6)+'Z',c.lg([[0,'#ffd9a0',.28*m.lamp+.04],[1,'#ffd9a0',0]],'v'),SCR)}
function plant(c,x,y,h,leaf){
 var s=Pa('M'+(x-h*.13)+' '+y+'L'+(x-h*.17)+' '+ii(y-h*.2)+'L'+(x+h*.17)+' '+ii(y-h*.2)+'L'+(x+h*.13)+' '+y+'Z',c.C('#8b5a3c')),i,g=c.lg([[0,c.C('#6f9a4e')],[1,c.C('#2c5530')]],'v');
 for(i=0;i<7;i++)s+=El(0,-h*.34,h*.07,h*.34,g,' transform="translate('+ii(x)+' '+ii(y-h*.18)+') rotate('+ii(-70+i*23)+')"');
 return s}
function bookP(c,w,h,rows){
 var t='',x=0,cs=['#8a3b3b','#2f4f6f','#d8c9a8','#4f6b45','#a9743a','#5c3b5e','#e2dccd','#27384a','#b5523b','#6f7f5e'],bw,bh;
 while(x<w){bw=c.rn(5,12);bh=c.rn(h*.6,h*.95);t+=R(x,h-bh,bw-.6,bh,c.C(c.pk(cs)));x+=bw}
 return c.pat(w,h,t)}

S['cafe-interior']=function(c,m){
 c.int=true;var s='',mk=c.mk,i,wl=c.lg([[0,c.C('#d9c3a3')],[1,c.C('#a78a68')]],'v');
 s+=R(0,0,W,360,wl);
 /* tijolo */
 var br=c.pat(30,13,R(0,0,30,13,c.C('#8a4a38'))+R(0,0,30,1.4,c.C('#c9b9a3'))+R(0,6.5,30,1.4,c.C('#c9b9a3'))+R(0,0,1.4,6.5,c.C('#c9b9a3'))+R(15,6.5,1.4,6.5,c.C('#c9b9a3')));
 s+=R(0,0,430,360,br)+R(0,0,430,360,c.lg([[0,'#000',.35],[1,'#000',0]],'h'));
 s+=floorP(c,350,'#6b4a30','#3d2a1c',480,9);
 /* vitrine */
 s+=c.winFrame(510,60,410,290,4,2,'street',c.C('#2a2f33'));
 s+=c.beam(510,60,410,290,-140,180,.3)+c.patch('M560 360L890 360L800 470L420 470Z',.28);
 /* quadro-menu e prateleiras */
 s+=R(170,48,170,84,c.C('#23272b'))+R(166,44,178,6,c.C('#6b4a32'));
 for(i=0;i<6;i++)s+=R(182,64+i*11,60+(i*37%70),2,'#e8e4d8',' opacity=".7"')+R(300,64+i*11,24,2,'#e8e4d8',' opacity=".5"');
 s+=R(30,150,130,6,c.C('#5a3d28'))+R(30,205,130,6,c.C('#5a3d28'));
 for(i=0;i<9;i++)s+=R(36+i*14,128+(i%3)*2,10,22-(i%3)*2,c.C(['#c9a24a','#7f9f6b','#d8d2c4'][i%3]),' opacity=".9"')+R(36+i*14,184,10,21,c.C(['#8a5a3a','#d8d2c4','#a3495a'][i%3]));
 /* balcao */
 s+=R(10,250,400,170,c.lg([[0,c.C('#7a5338')],[1,c.C('#4b3223')]],'v'));
 for(i=0;i<20;i++)s+=R(16+i*20,258,1.5,158,'#000',' opacity=".18"');
 s+=R(0,238,420,14,c.lg([[0,c.C('#e9e0d0')],[1,c.C('#b9ad98')]],'v'))+R(0,238,420,2,'#fff',' opacity=".5"');
 s+=R(30,185,95,53,c.lg([[0,c.C('#d7dade')],[1,c.C('#7f868f')]],'v'))+R(36,193,36,20,c.C('#2b2f33'))+R(95,170,24,16,c.C('#b8bcc2'))+Ci(60,200,5,'#fff',' opacity=".5"')+R(42,224,8,14,c.C('#222'));
 s+=Pa('M215 238Q215 190 265 190Q315 190 315 238Z',c.lg([[0,'#fff',.35],[1,'#fff',.08]],'v'))+El(265,236,52,6,c.C('#e8e0d0'))+El(245,222,14,8,c.C('#c8854a'))+El(285,223,14,8,c.C('#e3b878'))+El(265,212,10,6,c.C('#8a3a2c'));
 s+=Ci(355,232,7,c.C('#f2efe6'))+Ci(375,233,6,c.C('#f2efe6'));
 s+=c.p(215,420,150,'M',{t:'#e8e4da',l:'#2a2d33',d:.05});
 s+=Pa('M10 250H420V270H10Z','#000',' opacity=".25"'+c.bl(6));
 /* lampadas */
 s+=pend(c,95,70,'#2a2f33',24)+pend(c,320,90,'#2a2f33',20)+pend(c,600,80,'#2a2f33',24)+pend(c,780,95,'#2a2f33',22);
 /* mesas e pessoas */
 var tx=620,ty=468;
 s+=c.shadow(tx,ty+30,120,22,.5)+R(tx-112,ty-72,60,70,c.C('#2b2d31'))+R(tx+82,ty-72,60,70,c.C('#2b2d31'))+c.p(tx-80,ty-8,138,'S',{noshadow:1,t:'#7b3f4a',d:0})+c.p(tx+90,ty-8,142,'S',{flip:1,noshadow:1,t:'#3d6b5e'});
 s+=Pa('M'+(tx-6)+' '+(ty+4)+'H'+(tx+6)+'L'+(tx+8)+' '+(ty+62)+'H'+(tx-8)+'Z',c.C('#25272b'))+El(tx,ty+62,42,7,c.C('#25272b'))+El(tx,ty,92,17,c.lg([[0,c.C('#c19a6b')],[1,c.C('#8a6a45')]],'v'))+El(tx,ty-3,90,14,'#fff',' opacity=".12"');
 s+=Ci(tx-34,ty-6,9,c.C('#f4f1ea'))+El(tx-34,ty-8,6,2,'#4a2c1a')+Ci(tx+30,ty-3,9,c.C('#f4f1ea'))+El(tx+30,ty-5,6,2,'#4a2c1a')+R(tx-8,ty-9,16,7,c.C('#e8d9b8'));
 s+=c.p(820,540,160,'M',{flip:1,t:'#1f2937',d:0,noshadow:1});
 s+=Ln('M120 360V470',c.C('#2a2c30'),0)+plant(c,40,520,160);
 s+='<g'+c.bl(5)+' opacity=".95">'+plant(c,925,560,210)+'</g>';
 s+=c.bokeh(520,70,900,340,10,['#fff0c8','#9ed0ff','#ffd28a'])
 return s};

S['kitchen']=function(c,m){
 c.int=true;var s='',mk=c.mk,i,tile=c.pat(26,13,R(0,0,26,13,c.C('#ece7de'))+R(0,0,26,1,c.C('#bdb6a8'))+R(0,0,1,6.5,c.C('#bdb6a8'))+R(13,6.5,1,6.5,c.C('#bdb6a8')));
 s+=R(0,0,W,350,c.lg([[0,c.C('#e4dccd')],[1,c.C('#cfc4b0')]],'v'))+R(0,190,W,150,tile);
 s+=floorP(c,470,'#a37b55','#6b4a30',480,9);
 s+=c.winFrame(350,50,220,200,2,2,'trees',c.C('#f2efe8'))+R(340,248,240,10,c.C('#efe9dc'))+c.beam(350,50,220,200,-60,300,.3)+c.patch('M360 480L560 480L480 540L250 540Z',.3);
 /* armarios altos */
 var cab=c.lg([[0,c.C('#7b9a85')],[1,c.C('#587a66')]],'v');
 for(i=0;i<3;i++)s+=R(10+i*112,40,108,150,cab)+R(16+i*112,46,96,138,'none',' stroke="'+c.C('#47634f')+'" stroke-width="1.5"')+R(86+i*112,150,3,26,c.C('#d7c28a'));
 s+=R(600,40,80,150,cab)+R(690,40,100,150,cab);
 s+=Pa('M770 190L850 40L960 40L960 190Z',c.lg([[0,c.C('#cfd3d6')],[1,c.C('#8a9097')]],'v'));
 for(i=0;i<5;i++)s+=R(845+i*20,60,10,10,'#fff',' opacity=".15"');
 /* bancada e armarios baixos */
 s+=R(0,330,W,16,c.lg([[0,c.C('#efe9de')],[1,c.C('#bdb3a0')]],'v'))+R(0,330,W,2,'#fff',' opacity=".6"');
 s+=R(0,346,W,128,c.lg([[0,c.C('#5f8069')],[1,c.C('#3f5a49')]],'v'));
 for(i=0;i<8;i++)s+=R(8+i*120,354,112,110,'none',' stroke="'+c.C('#34493c')+'" stroke-width="1.6"')+R(52+i*120,358,4,22,c.C('#d7c28a'));
 s+=Pa('M0 474H960L960 480H0Z','#000',' opacity=".3"');
 /* fogao */
 s+=R(640,322,160,150,c.lg([[0,c.C('#c9ccd0')],[1,c.C('#7e848c')]],'v'))+R(652,372,136,80,c.C('#23272c'))+R(660,380,120,60,'#fff',' opacity=".1"');
 s+=El(690,326,28,5,c.C('#2a2d31'))+El(752,326,28,5,c.C('#2a2d31'));
 s+=R(678,296,26,30,c.C('#9ea3aa'))+R(732,300,40,26,c.C('#b45a3a'))+'<g'+c.bl(5)+' opacity=".5">'+El(692,276,14,22,'#fff')+El(700,248,18,24,'#fff')+El(752,280,16,20,'#fff')+'</g>';
 /* ilha */
 s+=c.shadow(480,540,420,26,.5)+R(150,420,660,120,c.lg([[0,c.C('#5f8069')],[1,c.C('#344b3c')]],'v'))+Pa('M120 420H840L880 396H80Z',c.lg([[0,c.C('#d9b383')],[1,c.C('#b58b5c')]],'v'))+R(120,420,720,3,'#000',' opacity=".3"')+Pa('M80 396H880L860 392H100Z','#fff',' opacity=".35"');
 s+=El(470,402,70,11,c.C('#f1ece1'))+El(470,398,62,9,c.C('#cfc6b4'));
 var fc=['#d9482f','#e8a13a','#8fb04a','#d9482f','#e8a13a'];
 for(i=0;i<5;i++)s+=Ci(440+i*16,392-(i%2)*7,9,c.C(fc[i]))+Ci(437+i*16,388-(i%2)*7,3,'#fff',' opacity=".35"');
 s+=Ci(620,400,12,c.C('#f6f2ea'))+R(250,404,70,4,'#000',' opacity=".25"');
 s+=pend(c,300,90,'#d9c28a',26)+pend(c,480,110,'#d9c28a',26)+pend(c,660,90,'#d9c28a',26);
 s+=c.p(120,468,168,'W',{t:'#d9d2c4',l:'#3a3e4b',h:'#5a3a24',d:.03});
 s+=plant(c,610,250,50);
 return s};

S['office']=function(c,m){
 c.int=true;var s='',mk=c.mk,i;
 s+=R(0,0,W,340,c.lg([[0,c.C('#cfd5dc')],[1,c.C('#aab3bd')]],'v'));
 s+=c.outside(30,36,900,290,'city');
 s+=Pa('M30 326L30 36L560 36L330 326Z','#fff',' opacity=".07"');
 for(i=0;i<=7;i++)s+=R(30+i*128,36,7,290,c.C('#2b3139'));
 s+=R(30,36,900,6,c.C('#2b3139'))+R(30,320,900,10,c.C('#2b3139'));
 s+=R(0,0,W,36,c.lg([[0,c.C('#e9ecef')],[1,c.C('#bfc5cc')]],'v'));
 for(i=0;i<5;i++)s+=R(80+i*180,10,110,10,'#fff',' opacity="'+(.5+m.lamp*.5)+'"')+c.glow(135+i*180,20,90,'#fff6e0',.35);
 s+=floorP(c,330,'#58616d','#2c323b',480,9,'#fff');
 s+=c.beam(30,36,900,290,-300,200,.2)+c.patch('M120 340L880 340L960 470L0 470Z',.26);
 /* mesas */
 function desk(x,y,w,sc,person){
  var o='',h=60*sc,mx=x+w*.5-26*sc+(x>480?-40:40)*sc;
  if(person)o+=c.p(x+w*.5,y+34*sc,h*2.6,'S',{noshadow:1,d:.1,t:person,l:'#232833'});
  o+=c.shadow(x+w/2,y+h+20*sc,w*.55,12*sc,.45)+Pa('M'+x+' '+y+'L'+(x+w)+' '+y+'L'+(x+w+18*sc)+' '+ii(y+16*sc)+'L'+(x-18*sc)+' '+ii(y+16*sc)+'Z',c.lg([[0,c.C('#d6c3a2')],[1,c.C('#a88c64')]],'v'));
  o+=R(x-14*sc,y+16*sc,w+28*sc,5*sc,c.C('#7f6a4a'))+R(x-10*sc,y+21*sc,5*sc,h,c.C('#2a2d33'))+R(x+w+5*sc,y+21*sc,5*sc,h,c.C('#2a2d33'));
  o+=R(mx,y-44*sc,52*sc,34*sc,c.C('#14181d'))+R(mx+3*sc,y-41*sc,46*sc,28*sc,c.lg([[0,'#7fb4e6'],[1,'#3d6aa8']],'v'),' opacity="'+(.55+m.lamp*.45)+'"')+R(mx+22*sc,y-10*sc,8*sc,10*sc,c.C('#14181d'));
  return o+c.glow(mx+26*sc,y-30*sc,60*sc,'#9cc8ff',.25)}
 s+=desk(80,380,200,1.1,'#7b3f4a')+desk(360,372,200,1,'#2f5d62')+desk(650,380,200,1.1,'#b9873b');
 s+=desk(190,330,130,.62,'#4b4e6d')+desk(560,330,130,.62);
 s+=c.p(150,335,120,'M',{t:'#111',l:'#111',s:'#2a1c14',h:'#111',noshadow:1,d:0,flip:1})+c.p(840,330,114,'W',{t:'#15181d',l:'#15181d',s:'#2a1c14',h:'#111',noshadow:1,d:0});
 s+=plant(c,36,470,230)+plant(c,930,420,170);
 s+=c.bokeh(30,40,930,320,8,['#fff6e0','#cfe4ff'])
 return s};

S['apartment-living-room']=function(c,m){
 c.int=true;var s='',mk=c.mk,i;
 s+=R(0,0,W,380,c.lg([[0,c.C('#e8dfd0')],[1,c.C('#d1c3ab')]],'v'));
 s+=floorP(c,380,'#b08d63','#6f5035',480,9);
  s+=c.winFrame(560,66,350,270,3,2,'city',c.C('#f4f1ea'));
 /* cortinas */
 s+=Pa('M520 52H590L575 360H520Z',c.lg([[0,c.C('#efe7d8')],[1,c.C('#cbbf9f')]],'h'),' opacity=".9"')+Pa('M880 52H940V360H890Z',c.lg([[0,c.C('#cbbf9f')],[1,c.C('#efe7d8')]],'h'),' opacity=".9"')+R(500,46,460,6,c.C('#3a3226'));
 s+=c.beam(560,66,350,270,-200,150,.28)+c.patch('M470 400L840 400L700 470L330 470Z',.28);
 /* estante */
 s+=R(20,90,140,300,c.C('#4d3a2b'));
 for(i=0;i<4;i++)s+=R(26,98+i*72,128,62,bookP(c,128,62))+R(20,160+i*72,140,5,c.C('#2d2218'));
 /* quadros */
 s+=R(220,110,92,120,c.C('#2b2f33'))+R(226,116,80,108,c.lg([[0,c.C('#e8a65a')],[1,c.C('#a24a3a')]],'v'))+Ci(266,164,22,c.C('#f5e6c8'),' opacity=".85"')
 s+=R(330,130,96,70,c.C('#d9d2c4'))+R(336,136,84,58,c.lg([[0,c.C('#6f8fa6')],[1,c.C('#2f4f6b')]],'v'))+R(346,164,64,30,c.C('#233a52'),' opacity=".7"');
 /* tapete */
 s+=El(370,470,300,52,c.lg([[0,c.C('#c9b39a')],[1,c.C('#8d765f')]],'v'))+El(370,470,270,42,'none',' stroke="'+c.C('#efe3cf')+'" stroke-width="2" opacity=".5"');
 /* sofa */
 s+=c.shadow(330,484,250,24,.55)+Pa('M100 360Q100 330 130 328H520Q550 330 550 360V450H100Z',c.lg([[0,c.C('#6f7f8f')],[1,c.C('#46525f')]],'v'))+Pa('M60 400Q60 372 90 376Q112 380 112 410V470Q70 470 60 450Z',c.lg([[0,c.C('#7d8d9d')],[1,c.C('#4a5764')]],'h'))+Pa('M590 400Q590 372 560 376Q538 380 538 410V470Q580 470 590 450Z',c.lg([[0,c.C('#4a5764')],[1,c.C('#7d8d9d')]],'h'));
 s+=Pa('M112 396Q112 380 140 380H300V470H112Z',c.lg([[0,c.C('#7d8d9d')],[1,c.C('#576572')]],'v'))+Pa('M300 380H510Q538 380 538 396V470H300Z',c.lg([[0,c.C('#78889a')],[1,c.C('#526070')]],'v'))+R(112,466,426,6,'#000',' opacity=".25"');
 s+=Pa('M150 372L220 366L226 432L158 440Z',c.C('#c9873f'))+Pa('M470 368L520 372L514 438L462 432Z',c.C('#e6d9bd'));
 /* mesa de centro */
 s+=El(430,520,112,16,c.rg('#000',.4))+El(430,500,100,20,c.lg([[0,c.C('#e0c9a3')],[1,c.C('#8a6d49')]],'v'))+R(332,505,6,34,c.C('#3d2f22'))+R(520,505,6,34,c.C('#3d2f22'))+Ci(400,494,9,c.C('#f4f1ea'))+R(448,490,40,4,c.C('#8a3a3a'));
 /* luminaria e planta */
 s+=Ln('M690 340V470',c.C('#2a2c30'),3)+Pa('M670 340L710 340L722 300L658 300Z',c.C('#f0e2bd'))+c.lamp(690,330,140,'#ffcf8a',.8)+El(690,474,22,5,c.C('#25272b'));
 s+=plant(c,900,490,210)+plant(c,30,500,90);
 return s};

S['library']=function(c,m){
 c.int=true;var s='',mk=c.mk,i,j;
 s+=R(0,0,W,360,c.lg([[0,c.C('#6b4a32')],[1,c.C('#3b281b')]],'v'));
 var bp=bookP(c,150,40);
 for(i=0;i<6;i++){s+=R(0,52+i*50,W,5,c.C('#2d1d12'));s+=R(0,12+i*50+(i?0:0),W,40,bp,' opacity="'+(.85+(i%2)*.1)+'"')}
 s+=R(0,0,W,7,c.C('#2d1d12'))+R(0,350,W,14,c.C('#2d1d12'));
 /* arcos e janelas centrais */
 s+=Pa('M330 360V150Q330 40 480 40Q630 40 630 150V360Z',c.lg([[0,m.sk[0]],[1,m.sk[2]]],'v'))+Ci(560,110,150,c.rg(m.sun,.8),' clip-path="none"')
 s+=Pa('M330 360V150Q330 40 480 40Q630 40 630 150V360ZM480 40V360M330 200H630','none',' stroke="'+c.C('#2d1d12')+'" stroke-width="8"')+Pa('M320 365V150Q320 30 480 30Q640 30 640 150V365','none',' stroke="'+c.C('#4a3324')+'" stroke-width="14"');
 s+=c.beam(340,60,280,300,-220,160,.32);
 s+=floorP(c,364,'#7a5a3c','#2f2016',480,9);
 s+=c.patch('M390 372L570 372L640 470L260 470Z',.32);
 /* mesa longa com luminarias */
 s+=c.p(330,452,150,'S',{noshadow:1,t:'#4b4e6d',l:'#222'})+c.p(740,456,150,'S',{noshadow:1,flip:1,t:'#a85a44',l:'#222'})+c.shadow(480,540,420,30,.5)+Pa('M120 430L840 430L930 470L30 470Z',c.lg([[0,c.C('#9a6b3f')],[1,c.C('#6e4a2a')]],'v'))+R(30,470,900,12,c.C('#4a301b'))+R(60,482,12,58,c.C('#3a2615'))+R(888,482,12,58,c.C('#3a2615'));
 for(i=0;i<3;i++){var x=240+i*240;s+=Pa('M'+(x-26)+' 410Q'+x+' 380 '+(x+26)+' 410Z',c.C('#2f6b4b'))+R(x-2,410,4,22,c.C('#c9a24a'))+c.lamp(x,415,110,'#ffd98a',.9)+Pa('M'+(x-90)+' 440L'+(x+90)+' 440L'+(x+60)+' 458L'+(x-60)+' 458Z','#ffd98a',' opacity="'+(.15+m.lamp*.25)+'"'+c.bl(4)+SCR)}
 s+=Pa('M'+210+' 400L250 392L260 428L220 432Z',c.C('#c9b99a'))+Pa('M690 402L730 396L738 430L698 434Z',c.C('#a3495a'));
  s+=R(0,0,W,H,c.lg([[0,'#000',.5],[.3,'#000',0],[.7,'#000',0],[1,'#000',.5]],'h'));
 return s};

/* ---------- interiores (2) ---------- */
function persp(vx,vy){
 var P=function(X,Y,z){return[ii(vx+X/z),ii(vy+Y/z)]};
 return{P:P,
  q:function(X,z1,z2,Y1,Y2){return'M'+P(X,Y1,z1)+'L'+P(X,Y1,z2)+'L'+P(X,Y2,z2)+'L'+P(X,Y2,z1)+'Z'},
  g:function(X1,X2,z1,z2,Y){return'M'+P(X1,Y,z1)+'L'+P(X2,Y,z1)+'L'+P(X2,Y,z2)+'L'+P(X1,Y,z2)+'Z'},
  f:function(Z,X1,X2,Y1,Y2){return'M'+P(X1,Y1,Z)+'L'+P(X2,Y1,Z)+'L'+P(X2,Y2,Z)+'L'+P(X1,Y2,Z)+'Z'}}}

S['subway']=function(c,m){
 c.int=true;var s='',mk=c.mk,i,VX=480,VY=255,p=persp(VX,VY),P=p.P;
 s+=R(0,0,W,H,c.C('#1b1f26'));
 /* parede esquerda azulejada */
 s+=Pa(p.q(-720,.18,16,-330,210),c.lg([[0,c.C('#e8e4d8')],[1,mix(c.C('#c9c4b4'),m.fog,.5)]],'h'));
 var ln='';for(i=0;i<9;i++)ln+='M'+P(-720,-330+i*60,.18)+'L'+P(-720,-330+i*60,16);for(i=0;i<22;i++){var zz=.2+i*i*.04+i*.1;ln+='M'+P(-720,-330,zz)+'L'+P(-720,210,zz)}
 s+=Ln(ln,'#000',1,' opacity=".1"')+Pa(p.q(-720,.18,16,-90,-40),c.C('#2f6aa8'))+Pa(p.q(-720,.18,16,-36,-30),c.C('#e8c23a'));
 /* teto */
 s+=Pa(p.g(-720,720,.18,16,-330),c.lg([[0,c.C('#20252d')],[1,mix(c.C('#2a303a'),m.fog,.3)]],'v'));
 var lt='';for(i=0;i<9;i++){var z1=.4+i*i*.12+i*.4;lt+=p.g(-340,-250,z1,z1+.5,-330)+p.g(250,340,z1,z1+.5,-330)+p.g(-45,45,z1,z1+.5,-330)}
 s+=Pa(lt,'#fff',' opacity="'+(.55+m.lamp*.45)+'"')+Pa(lt,'#fff',' opacity=".5"'+c.bl(4)+SCR);
 /* plataforma, faixa, trilhos */
 s+=Pa(p.g(-720,-190,.18,16,210),c.lg([[0,mix(c.C('#8a8c8f'),m.fog,.6)],[1,c.C('#a5a6a6')]],'v'))+Pa(p.g(-196,-170,.18,16,210),c.C('#e6c23a'))+Pa(p.g(-170,170,.18,16,300),c.lg([[0,'#0b0d10'],[1,c.C('#2a2c30')]],'v'))+Pa(p.q(-170,.18,16,210,300),c.C('#3a3d42'));
 var rl='';for(i=-1;i<=1;i+=2)rl+='M'+P(i*70,300,.18)+'L'+P(i*70,300,16);s+=Ln(rl,c.C('#9aa0a8'),2.2);
 var sl='';for(i=0;i<16;i++){var z2=.25+i*i*.09+i*.25;sl+=p.g(-120,120,z2,z2+.08,300)}s+=Pa(sl,'#17120e',' opacity=".8"');
 s+=c.patch('M-30 540L300 330L480 330L400 540Z',.12);
 /* trem */
 var tx=190;
 s+=Pa(p.q(tx,.3,12,-130,290),c.lg([[0,mix(c.C('#d9dde2'),m.fog,.5)],[1,c.C('#a3a9b1')]],'h'))+Pa(p.q(tx,.3,12,90,130),c.C('#2f6aa8'))+Pa(p.q(tx,.3,12,270,290),c.C('#12151a'));
 var wn='',dr='';for(i=0;i<8;i++){var a=1+i*i*.12+i*.9,b=a+.55;if(a>9)break;if(i%2===0)dr+=p.q(tx,a,b+.1,-90,230);else wn+=p.q(tx,a+.05,b+.45,-80,40)}
 s+=Pa(wn,c.lg([[0,'#fff3d2'],[1,'#d9c08a']],'v'))+Pa(dr,c.lg([[0,'#fff6dc'],[1,'#e8d2a0']],'v'))+Pa(dr,'#ffd98a',' opacity=".4"'+c.bl(6)+SCR);
 s+=Ci(VX+8,VY+8,14,c.rg('#fff6dc',.9),SCR);
 /* pilares */
 var zs=[.9,1.9,3.5,6];
 for(i=0;i<4;i++){var z=zs[i];s+=Pa(p.q(-430,z,z+.12,-330,210),c.lg([[0,c.C('#d9d4c4')],[1,c.C('#a29c8a')]],'h'))+Pa(p.f(z,-430,-390,-330,210),c.lg([[0,c.C('#efeadb')],[1,c.C('#b9b3a1')]],'h'))}
 /* placa suspensa */
 s+=Ln('M'+P(-300,-330,2.4)+'V'+P(-300,-190,2.4)[1],'#222',1.5)+R(P(-380,0,2.4)[0],P(-380,-190,2.4)[1],86,36,c.C('#14181d'))+R(P(-380,0,2.4)[0]+6,P(-380,-190,2.4)[1]+8,54,3,'#ffd98a')+R(P(-380,0,2.4)[0]+6,P(-380,-190,2.4)[1]+17,40,3,'#9ed0ff')+Ci(P(-380,0,2.4)[0]+70,P(-380,-190,2.4)[1]+18,6,'#e8c23a');
 /* pessoas */
 var pp=[[-330,1.1,'M','K'],[-470,1.5,'W'],[-300,2.2,'K'],[-420,3.0,'M'],[-330,4.2,'W']];
 for(i=0;i<pp.length;i++){var pt=P(pp[i][0],210,pp[i][1]);s+=c.p(pt[0],pt[1],150/pp[i][1],pp[i][2],{d:Math.min(.4,pp[i][1]*.05),flip:i%2})}
 var sp=P(-300,210,1.1);s+=R(sp[0]+30,sp[1]-40,28,40,c.C('#2a3140'))+Ln('M'+(sp[0]+44)+' '+(sp[1]-40)+'v-14',c.C('#111'),2);
 s+=c.fog(190,130,.35)+Ci(VX,VY,200,c.rg(m.fog,.4),SCR);
 return s};

S['airport']=function(c,m){
 c.int=true;var s='',mk=c.mk,i;
 /* vista externa: ceu, pista e aviao */
 var wy=96,wh=240;
 s+=R(0,0,W,H,c.C('#2c3138'));
 s+=R(0,wy,W,wh,c.lg([[0,m.sk[0]],[.6,m.sk[1]],[1,m.sk[2]]],'v'))+Ci(m.sx*W,wy+60,300,c.rg(m.sun,.8));
 s+=R(0,wy+wh-70,W,70,c.lg([[0,c.C('#6e747c',.4)],[1,c.C('#3a3f46')]],'v'));
 s+='<g'+c.bl(1.4)+'>'+c.bld(0,960,wy+wh-66,10,30,'#9aa6b4',.6,{nowin:1,wmin:40,wmax:100})+'</g>';
 /* aviao */
 var ax=300,ay=wy+wh-50;
 s+=Pa('M'+(ax-190)+' '+ay+'Q'+(ax-210)+' '+(ay-38)+' '+(ax-150)+' '+(ay-52)+'L'+(ax+170)+' '+(ay-56)+'Q'+(ax+240)+' '+(ay-40)+' '+(ax+250)+' '+(ay-6)+'Q'+(ax+160)+' '+(ay+8)+' '+(ax-60)+' '+(ay+8)+'Z',c.lg([[0,c.C('#f4f6f8')],[.6,c.C('#cfd5dc')],[1,c.C('#8d96a1')]],'v'))+Pa('M'+(ax+160)+' '+(ay-52)+'L'+(ax+210)+' '+(ay-120)+'L'+(ax+240)+' '+(ay-120)+'L'+(ax+230)+' '+(ay-40)+'Z',c.C('#2f6aa8'))+Pa('M'+(ax-30)+' '+(ay-6)+'L'+(ax+90)+' '+(ay-20)+'L'+(ax+30)+' '+(ay+30)+'Z',c.C('#b9c0c9'));
 var ws='';for(i=0;i<22;i++)ws+=Ci(ax-100+i*14,ay-36,2.4,c.C('#2a3140'));
 s+=ws+Pa('M'+(ax-150)+' '+(ay-52)+'L'+(ax-96)+' '+(ay-60)+'L'+(ax-100)+' '+(ay-42)+'L'+(ax-160)+' '+(ay-38)+'Z',c.C('#1b2533'));
 s+=R(ax+300,ay-60,180,10,c.C('#8e949c'))+R(ax+470,ay-62,14,64,c.C('#7a8088'));
 /* vidro e montantes */
 s+=Pa('M0 '+(wy+wh)+'L0 '+(wy+90)+'L420 '+wy+'L560 '+wy+'L100 '+(wy+wh)+'Z','#fff',' opacity=".08"');
 for(i=0;i<=8;i++)s+=R(i*120-4,wy,8,wh,c.C('#3a4048'));
 s+=R(0,wy+wh,W,6,c.C('#3a4048'));
 /* teto com trelica */
 s+=R(0,0,W,wy,c.lg([[0,c.C('#d9dde1')],[1,c.C('#b3b9bf')]],'v'));
 var tl='';for(i=0;i<20;i++)tl+='M'+(i*60)+' 0L'+(i*60+30)+' '+wy+'L'+(i*60+60)+' 0';
 s+=Ln(tl,c.C('#6e757d'),2,' opacity=".6"')+R(0,wy-6,W,8,c.C('#5b626a'));
 for(i=0;i<6;i++)s+=R(90+i*150,wy-16,60,5,'#fff',' opacity="'+(.5+m.lamp*.5)+'"')+c.glow(120+i*150,wy-10,60,'#fff6e0',.3);
 /* piso brilhante */
 var fy=wy+wh+6;
 s+=R(0,fy,W,H-fy,c.lg([[0,c.C('#9da3aa')],[1,c.C('#555b63')]],'v'));
 s+=R(0,fy,W,60,c.lg([[0,m.sk[1],.45],[1,m.sk[1],0]],'v'))+El(300,fy+50,240,26,c.rg(m.sun,.6),SCR);
 var fl='';for(i=-8;i<9;i++)fl+='M'+(480+i*40)+' '+fy+'L'+(480+i*170)+' '+H;s+=Ln(fl,'#000',1,' opacity=".1"')+Ln('M0 '+(fy+34)+'H960M0 '+(fy+86)+'H960M0 '+(fy+160)+'H960','#000',1,' opacity=".08"');
 s+=c.beam(60,wy,440,wh,-120,190,.18);
 /* painel de voos */
 s+=Ln('M440 '+(wy-6)+'V30M520 '+(wy-6)+'V30',c.C('#2a2f36'),2)+R(360,30,240,92,c.C('#101419'))+R(360,30,240,92,'none',' stroke="'+c.C('#3a4048')+'" stroke-width="3"');
 for(i=0;i<5;i++){var yy=42+i*16;s+=R(370,yy,70,4,'#ffc233')+R(450,yy,64,4,'#ffc233',' opacity=".7"')+R(530,yy,22,4,i===2?'#ff5a4a':'#4ade80')+R(560,yy,28,4,'#ffc233',' opacity=".5"')}
 s+=c.glow(480,76,220,'#ffc233',.18);
 /* cadeiras */
 var chr='';for(i=0;i<5;i++){var cx=60+i*62;chr+=R(cx,430,46,34,c.C('#2f5d8f'))+R(cx,396,46,30,c.C('#3b6fa5'))+R(cx+20,464,6,22,c.C('#1c1f24'))}
 s+=El(190,492,190,14,c.rg('#000',.4))+chr;
 s+=c.p(120,468,120,'S',{noshadow:1,t:'#d9482f',d:0});
 /* viajantes */
 function bag(x,y,w,h,col){return R(x,y-h,w,h,c.lg([[0,c.C(col)],[1,mix(c.C(col),'#000',.35)]],'v'))+R(x+w*.3,y-h-8,w*.4,8,'none',' stroke="#222" stroke-width="2"')+R(x+2,y,5,4,'#111')+R(x+w-7,y,5,4,'#111')}
 s+=c.p(640,470,196,'M',{d:0,t:'#2f4858',flip:1})+bag(666,492,42,60,'#c0392b')+c.p(740,456,170,'W',{d:0,t:'#d8d2c4'})+bag(720,478,34,46,'#2f6aa8')+c.p(560,420,100,'K',{d:.15})+c.p(860,440,160,'M',{d:.05,t:'#8a3a3a'});
 s+=R(0,0,W,H,c.lg([[0,'#000',.25],[.2,'#000',0],[.8,'#000',0],[1,'#000',.25]],'h'));
 return s};

S['classroom']=function(c,m){
 c.int=true;var s='',mk=c.mk,i,j;
 s+=R(0,0,W,350,c.lg([[0,c.C('#e9e3d4')],[1,c.C('#cfc6b2')]],'v'))+R(0,0,W,8,c.C('#f4f1ea'));
 s+=R(0,250,W,100,c.lg([[0,c.C('#7a9a8a')],[1,c.C('#587a6a')]],'v'),' opacity=".9"')+R(0,246,W,5,c.C('#d9cfb8'));
 s+=floorP(c,350,'#b9946a','#6f5238',480,9);
 /* quadro-branco */
 s+=R(228,66,470,186,c.C('#9aa3a8'))+R(236,74,454,170,c.lg([[0,c.C('#fbfbf8')],[1,c.C('#e0e3e3')]],'v'))+R(236,74,454,170,'#fff',' opacity=".25"');
 var wr='';for(i=0;i<7;i++)wr+='M256 '+(100+i*18)+'q'+ii(40+i*20)+' -8 '+ii(110+(i*53%90))+' 0';s+=Ln(wr,'#244a7a',2.4,' opacity=".85"')+Ln('M520 98q30 -10 60 0t60 0M520 132h120M520 150h90','#c0392b',2.4)+Ci(600,200,18,'none',' stroke="#2f7a4a" stroke-width="2.4"')+R(560,186,40,26,'none',' stroke="#2f6aa8" stroke-width="2.4"');
 s+=R(236,244,454,8,c.C('#7a8186'))+R(300,240,22,5,'#fff')+R(330,240,16,5,'#e8c23a');
 /* relogio e mapa */
 s+=Ci(770,92,26,c.C('#f4f1ea'))+Ci(770,92,26,'none',' stroke="#2a2d33" stroke-width="4"')+Ln('M770 92V74M770 92L784 98','#222',2.4)+R(738,150,132,86,c.lg([[0,c.C('#6fa8c9')],[1,c.C('#3f7ea3')]],'v'))+Pa('M752 170Q770 160 788 172Q800 182 790 198Q770 210 756 194Z',c.C('#8aae6a'))+Pa('M810 176Q830 170 846 184Q840 204 818 204Z',c.C('#8aae6a'));
 /* janelas */
 s+=c.winFrame(30,60,170,200,2,2,'trees',c.C('#efe9dc'))+c.beam(30,60,170,200,260,200,.3)+c.patch('M250 360L560 360L640 460L300 480Z',.3);
 /* professora */
 s+=c.p(150,360,178,'W',{t:'#a85a44',l:'#2a2d33',h:'#3a2418',d:0});
 /* carteiras e alunos de costas */
 function desk(x,y,sc,stu,col){
  var o='',w1=116*sc;
  o+=c.shadow(x,y+40*sc,w1*.62,10*sc,.4);
  if(stu)o+=c.p(x,y+4*sc,168*sc,'S',{noshadow:1,t:col,l:'#232833',s:stu,h:stu,d:.04});
  o+=R(x-w1*.5,y-6*sc,w1,6*sc,c.C('#c9a672'))+Pa('M'+(x-w1*.5)+' '+y+'L'+(x+w1*.5)+' '+y+'L'+(x+w1*.55)+' '+(y+10*sc)+'L'+(x-w1*.55)+' '+(y+10*sc)+'Z',c.lg([[0,c.C('#d9b685')],[1,c.C('#9a7a4a')]],'v'))+R(x-w1*.45,y+10*sc,4*sc,32*sc,c.C('#2a2d33'))+R(x+w1*.45-4*sc,y+10*sc,4*sc,32*sc,c.C('#2a2d33'))+R(x-14*sc,y-10*sc,26*sc,4*sc,c.C('#f4f1ea'))+R(x+20*sc,y-9*sc,16*sc,3*sc,c.C('#2f6aa8'));
  return o}
 var cols=['#2f4858','#7b3f4a','#3d6b5e','#b9873b','#4b4e6d','#a85a44'],hr=['#1b1411','#3a2418','#6b4a2b','#a88b5a','#2a2a2e','#1b1411'];
 for(j=0;j<3;j++)for(i=0;i<3;i++){var sc=.55+j*.22,y=392+j*58;s+=desk(190+i*290-(j%2)*40+j*30,y,sc,hr[(i+j*3)%6],cols[(i*2+j)%6])}
 s+=plant(c,920,350,120);
 s+=Pa('M0 0H960V30H0Z','#000',' opacity=".1"')+pend(c,300,40,'#2a2f33',16)+pend(c,640,40,'#2a2f33',16);
 return s};

S['hotel-lobby']=function(c,m){
 c.int=true;var s='',mk=c.mk,i,hy=340;
 s+=R(0,0,W,hy,c.lg([[0,c.C('#6b5238')],[1,c.C('#3e2f20')]],'v'));
 var pn='';for(i=0;i<16;i++)pn+='M'+(i*64)+' 0V'+hy;s+=Ln(pn,'#000',1.5,' opacity=".28"')+R(0,hy-14,W,14,c.C('#2a1f14'));
 /* quadro grande */
 s+=R(330,60,300,150,c.C('#c9a24a'))+R(338,68,284,134,c.lg([[0,c.C('#3c5f7a')],[.5,c.C('#d9a65a')],[1,c.C('#7a3a3a')]],'h'))+Pa('M338 170Q420 120 480 160T622 140V202H338Z',c.C('#1f3a4a'),' opacity=".7"')+Ci(540,106,22,c.C('#f5e6c8'),' opacity=".85"');
 s+=c.glow(480,40,220,'#ffd9a0',.35);
 /* piso marmore e reflexo */
 s+=R(0,hy,W,H-hy,c.lg([[0,c.C('#d9d2c4')],[1,c.C('#a29a89')]],'v'));
 var mb='';for(i=-8;i<9;i++)mb+='M'+(480+i*40)+' '+hy+'L'+(480+i*180)+' '+H;s+=Ln(mb,'#000',1,' opacity=".13"')+Ln('M0 380H960M0 430H960M0 500H960','#000',1,' opacity=".1"');
 s+=Ln('M80 350Q200 440 120 540M830 360Q700 450 840 540M400 345Q520 400 430 470','#fff',2,' opacity=".25"'+c.bl(1));
 /* balcao */
 s+=c.shadow(480,444,260,18,.5)+R(250,300,460,140,c.lg([[0,c.C('#7a5538')],[1,c.C('#4a3220')]],'v'));
 for(i=0;i<9;i++)s+=R(262+i*50,312,34,116,'none',' stroke="'+c.C('#2f1f13')+'" stroke-width="1.6"');
 s+=R(236,288,488,16,c.lg([[0,c.C('#e9e0d0')],[1,c.C('#a89c86')]],'v'))+R(236,288,488,2,'#fff',' opacity=".6"')+c.glow(480,300,260,'#ffd9a0',.3*Math.max(m.lamp,.3));
 s+=c.p(480,300,128,'W',{t:'#1f2a44',l:'#1f2a44',noshadow:1,h:'#2a1c14',d:0})+Ci(300,284,7,c.C('#f2efe6'))+R(640,278,28,10,c.C('#d9a45a'))+Pa('M610 288Q620 262 640 288Z',c.C('#2f6b4b'))+c.lamp(610,272,60,'#ffd98a',.6);
 /* colunas */
 function col(x,wd){return R(x-wd/2-6,hy-20,wd+12,18,c.C('#d9c28a'))+R(x-wd/2,0,wd,hy-20,c.lg([[0,c.C('#e2dacb')],[.35,c.C('#fbf7ee')],[1,c.C('#8f8574')]],'h'))+R(x-wd/2-6,0,wd+12,16,c.C('#d9c28a'))+R(x-wd/2-6,hy,wd+12,8,c.C('#d9c28a'))}
 s+=col(120,60)+col(840,60);
 /* lustre */
 s+=Ln('M480 0V70',c.C('#3a3226'),2)+c.glow(480,100,230,'#ffd9a0',.7*Math.max(m.lamp,.35))+Pa('M450 60H510L540 92H420Z',c.C('#d9b45a'));
 for(i=0;i<24;i++){var a=i/24*6.283;s+=Ci(480+Math.cos(a)*(40+i%3*14),92+Math.sin(a)*14+i%4*8,2.6,'#fff7e0',SCR+' opacity=".95"')}
 s+=Ln('M440 92Q480 130 520 92','#fff',1,' opacity=".6"');
 /* sofas */
 s+=Pa('M30 430Q30 400 60 398H190Q220 400 220 430V480H30Z',c.lg([[0,c.C('#7a2f3a')],[1,c.C('#4a1c26')]],'v'))+Pa('M20 440Q20 420 40 424V490H20Z',c.C('#5a2230'))+Pa('M230 440Q230 420 210 424V490H230Z',c.C('#5a2230'))+El(125,500,110,12,c.rg('#000',.4))+El(280,505,56,10,c.lg([[0,c.C('#e8d9b8')],[1,c.C('#a8946a')]],'v'))+R(276,505,5,24,c.C('#2a1f14'));
 /* carrinho de malas */
 s+=Ln('M740 330V500M860 330V500M740 330H860M740 500H860','#d9b45a',3)+R(748,440,100,60,c.C('#c0392b'))+R(756,390,80,50,c.C('#2f4858'))+Ln('M756 390v-8h80v8','none',2)+R(800,350,0,0,'#000');
 s+=c.p(640,480,176,'M',{d:0,t:'#d8d2c4',flip:0})+c.p(690,482,168,'W',{d:0,t:'#2f6aa8'});
 s+=plant(c,935,500,200)+plant(c,25,350,90);
 return s};

S['museum-gallery']=function(c,m){
 c.int=true;var s='',mk=c.mk,i,j,VX=480,VY=250,p=persp(VX,VY),P=p.P;
 s+=R(0,0,W,H,c.C('#cfc9bd'));
 /* parede do fundo e sala seguinte */
 s+=Pa(p.f(10,-400,400,-300,200),c.C('#efe9dc'))+Pa(p.f(10,-90,90,-80,200),c.lg([[0,'#fffaf0'],[1,c.C('#e8e0d0')]],'v'))+Pa(p.f(10,-60,60,-60,0),c.lg([[0,c.C('#3c5f7a')],[1,c.C('#d9a65a')]],'h'))+Ci(VX,VY+12,160,c.rg('#fff6dc',.5),SCR);
 /* paredes laterais */
 var wl=c.lg([[0,c.C('#cfc7b8')],[1,mix(c.C('#e6dfd0'),m.fog,.4)]],'h'),wr=c.lg([[0,mix(c.C('#e6dfd0'),m.fog,.4)],[1,c.C('#b9b1a1')]],'h');
 s+=Pa(p.q(-400,.35,10,-300,200),wl)+Pa(p.q(400,.35,10,-300,200),wr);
 /* teto e claraboias */
 s+=Pa(p.g(-400,400,.35,10,-300),c.lg([[0,c.C('#d9d4c8')],[1,'#fff']],'v'));
 var sk='';for(i=0;i<5;i++){var z1=.7+i*i*.45+i*.5;sk+=p.g(-250,250,z1,z1+.9+i*.3,-300)}
 s+=Pa(sk,mk==='night'?'#2a3a66':'#fffaf0',' opacity=".9"')+Pa(sk,m.key,' opacity="'+(.6*m.sl)+'"'+c.bl(5)+SCR);
 /* piso */
 s+=Pa(p.g(-400,400,.35,10,200),c.lg([[0,c.C('#8a6a48')],[.6,c.C('#a8865c')],[1,c.C('#c8a67a')]],'v'));
 var fl='';for(i=-8;i<9;i++)fl+='M'+P(i*50,200,10)+'L'+P(i*50,200,.35);s+=Ln(fl,'#000',1,' opacity=".14"');
 s+=Pa(p.g(-250,250,.7,12,200),m.key,' opacity="'+(.22*m.sl)+'"'+c.bl(8)+SCR);
 /* quadros */
 var art=[['#3c5f7a','#d9a65a'],['#7a3a3a','#e8d9b8'],['#2f4a3a','#c9b44a'],['#1f2a44','#d97a8a'],['#d9a65a','#5a3a2a']];
 var zz=[.55,1.5,2.6,4.2,6.4],k;
 for(i=0;i<5;i++){var a=zz[i],b=a+(.5+i*.08)*(1+i*.12);
  for(j=-1;j<=1;j+=2){var X=j*400,ac=art[(i+(j>0?2:0))%5];
   s+=Pa(p.q(X,a-.03,b+.03,-110,60),c.C('#2b2318'))+Pa(p.q(X,a+.02,b-.02,-104,54),c.lg([[0,c.C(ac[0])],[1,c.C(ac[1])]],'h'))+Pa(p.q(X,a+(b-a)*.3,b-(b-a)*.2,-70,22),c.C(ac[1]),' opacity=".55"')+Pa(p.q(X,a,b,70,76),'#000',' opacity=".25"'+c.bl(1.5))+Ci(P(X,-170,(a+b)/2)[0],P(X,-170,(a+b)/2)[1],18/((a+b)/2)+3,c.rg(m.key,.7),SCR)}}
 /* banco e escultura */
 var bz=P(0,200,2.1);s+=El(bz[0],bz[1]+4,100,10,c.rg('#000',.4))+R(bz[0]-90,bz[1]-34,180,10,c.C('#2a2220'))+R(bz[0]-84,bz[1]-24,8,24,c.C('#1a1a1a'))+R(bz[0]+76,bz[1]-24,8,24,c.C('#1a1a1a'));
 var sz=P(-90,200,3.3);s+=R(sz[0]-12,sz[1]-48,24,48,c.C('#f4f1ea'))+Ci(sz[0],sz[1]-68,13,c.lg([[0,c.C('#fffdf8')],[1,c.C('#c9c2b0')]],'v'))+Pa('M'+(sz[0]-12)+' '+(sz[1]-56)+'Q'+sz[0]+' '+(sz[1]-46)+' '+(sz[0]+12)+' '+(sz[1]-56)+'L'+(sz[0]+14)+' '+(sz[1]-48)+'H'+(sz[0]-14)+'Z',c.C('#efe9dc'));
 /* visitantes */
 var pp=[[-170,1.3,'W',1],[140,1.9,'M',0],[-40,3.1,'K',1],[260,4.6,'W',0],[-260,2.5,'M',0]];
 for(i=0;i<pp.length;i++){var pt=P(pp[i][0],200,pp[i][1]);s+=c.p(pt[0],pt[1],145/pp[i][1],pp[i][2],{d:Math.min(.4,pp[i][1]*.05),flip:pp[i][3],t:['#1f2937','#8a3a3a','#2f4858','#d8d2c4','#4b4e6d'][i],l:'#1f232b'})}
 s+=c.fog(200,120,.25)+R(0,0,W,H,c.lg([[0,'#000',.3],[.25,'#000',0],[.75,'#000',0],[1,'#000',.3]],'h'));
 return s};



var KINDS=['city-street','cafe-interior','kitchen','office','subway','airport','market','park','beach','mountain-trail','museum-gallery','library','classroom','hotel-lobby','apartment-living-room','night-skyline','countryside','plaza-europe','plaza-latin','temple-asia'];
var LABEL={'city-street':'Rua de cidade','cafe-interior':'Interior de cafeteria','kitchen':'Cozinha','office':'Escritorio','subway':'Estacao de metro','airport':'Aeroporto','market':'Feira ao ar livre','park':'Parque','beach':'Praia','mountain-trail':'Trilha na montanha','museum-gallery':'Galeria de museu','library':'Biblioteca','classroom':'Sala de aula','hotel-lobby':'Saguao de hotel','apartment-living-room':'Sala de apartamento','night-skyline':'Skyline noturno','countryside':'Campo','plaza-europe':'Praca europeia','plaza-latin':'Praca latina','temple-asia':'Templo asiatico'};

function scene(kind,o){
 o=o||{};kind=String(kind||'');
 var fn=S[kind],c=ctx(fn?kind:'fallback',o),body;
 if(fn){try{body=fn(c,c.m)}catch(e){body=null}}
 if(!body){c.int=false;body=c.sky(H)+c.ridge(430,30,'#3a4a60',.2,1)+c.ridge(480,24,'#26324a',.1,2)}
 return c.assemble(body+c.fin(),o.label||LABEL[kind]||'Ilustracao')}

/* escolha automatica por cidade/lugar/tema */
function norm(t){t=String(t||'').toLowerCase();try{t=t.normalize('NFD').replace(/[̀-ͯ]/g,'')}catch(e){}return t}
var RULES=[
 [/museu|museum|galeri|gallery|louvre|moma|exposic|exhibit|arte\b|\bart\b|painting|quadro|pintura/,'museum-gallery'],
 [/bibliotec|library|\blivro|\bbook|leitura|reading/,'library'],
 [/aeroport|airport|\bvoo\b|flight|embarque|boarding|\bgate\b|passport|passaporte|\bjfk\b|heathrow|bagagem|luggage|suitcase|mala\b/,'airport'],
 [/subwaycar|\bmetro\b|subway|estacao|station|\btrem\b|train|underground|\btube\b|platform|plataforma|bilhete|ticket/,'subway'],
 [/classroom|escola|school|sala de aula|\baula|student|aluno|teacher|professor|homework|lesson|university|universidade|campus/,'classroom'],
 [/hotel|lobby|reception|recepcao|check-?in|hostel|resort|concierge|room key|quarto|enjoy your stay|\bstay\b|hospedagem|elevator|elevador|luggage/,'hotel-lobby'],
 [/kitchen|cozinha|cook|cozinhar|recipe|receita|\bbaking|forno|stove|dinner|jantar|lunch|almoco/,'kitchen'],
 [/cafe|coffee|latte|starbucks|bakery|padaria|diner|breakfast|cafe da manha|pizzeria|pizza|restaurant|restaurante|\bbar\b|bagel|waiter|garcom/,'cafe-interior'],
 [/office|escritorio|\bwork|trabalho|meeting|reuniao|studio|estudio|job|emprego|career|business|negocio|telefone|phone call/,'office'],
 [/market|feira|mercado|\bshop|loja|store|supermarket|\bmall\b|compras|shopping|buy|comprar|price|preco|cheap/,'market'],
 [/beach|praia|surf|\bsea\b|ocean|oceano|harbor|harbour|porto\b|pier|swim|nadar|holiday|ferias|miami|san diego|honolulu|hawaii|tampa|salvador|copacabana/,'beach'],
 [/mountain|montanha|trail|hike|hiking|trilha|camping|acampar|yellowstone|boulder|flagstaff|colorado|alps|alpes|rocky|nature|natureza|forest|floresta|duluth/,'mountain-trail'],
 [/park|parque|garden|jardim|picnic|dog walk|jogging|run\b|correr|bench|banco da praca/,'park'],
 [/countryside|farm|fazenda|\bcampo\b|rural|village|vila\b|route 66|road trip|estrada|barn|harvest|colheita|boise|fargo|des moines|omaha|santa fe/,'countryside'],
 [/living|sala de estar|apartamento|apartment|\bhome\b|\bcasa\b|family|familia|party|festa|sofa|sofa|bath|banheiro|bedroom|quarto de dormir|neighbor|vizinh|\btv\b|weekend em casa/,'apartment-living-room'],
 [/skyline|noite|night|\bbar\b|rooftop|fireworks|new year/,'night-skyline']
];
var EUR=/london|londres|paris|rome|roma|madrid|berlin|lisbon|lisboa|barcelona|praga|prague|amsterd|vienna|viena|florenc|florence|venice|veneza|milan|munich|dublin|brussels|bruxelas|athens|atenas|porto|edinburgh|europ|italy|italia|france|franca|spain|espanha|germany|alemanha|portugal|england|inglaterra|uk\b|bruges|salzburg|oxford|cambridge|copenhagen|stockholm|oslo/,
 LAT=/mexico|cdmx|oaxaca|bogota|buenos aires|lima\b|santiago|cartagena|havana|habana|quito|cusco|guadalajara|montevideo|san juan|latin|latina|argentina|colombia|peru|chile|cuba|rio\b|brasil|brazil|sao paulo|recife|olinda|ouro preto|puebla|antigua|san antonio|tucson|albuquerque|el paso|laredo|sevilla|seville|andaluz/,
 ASIA=/tokyo|toquio|kyoto|osaka|japan|japao|china|beijing|pequim|shanghai|seoul|korea|coreia|bangkok|thai|vietnam|hanoi|asia|temple|templo|shrine|santuario|pagoda|india|delhi|mumbai|singapore|hong kong|taipei|bali|nara|sushi/;
var SC={cafe:'cafe-interior',diner:'cafe-interior',pizzeria:'cafe-interior',living:'apartment-living-room',party:'apartment-living-room',bath:'apartment-living-room',lobby:'hotel-lobby',shop:'market',market:'market',airport:'airport',station:'subway',subwaycar:'subway',classroom:'classroom',studio:'office',beach:'beach',harbor:'beach',park:'park',kitchen:'kitchen',office:'office',library:'library',museum:'museum-gallery'},
 MTN=/yellowstone|boulder|flagstaff|duluth|colorado|aspen|denver|salt lake|alps/,
 HIST=/boston|philadelphia|charleston|savannah|salem|washington|new orleans|albany|baltimore|cincinnati/;
function pick(x){
 var t,sc='',city='';
 if(x==null)t='';
 else if(typeof x==='string')t=x;
 else if(Array.isArray(x))t=x.join(' ');
 else{sc=norm(x.sc||x.scene||'');city=norm(x.city||x.place||'');t=[x.t,x.title,x.sub,x.s,x.city,x.place,x.theme,x.tags&&[].concat(x.tags).join(' '),x.emo&&[].concat(x.emo).join(' ')].filter(Boolean).join(' ')}
 t=norm(t);
 if(KINDS.indexOf(t.trim())>=0)return t.trim();
 if(sc&&(SC[sc]||sc==='plaza')){
  var k=SC[sc];
  if(sc==='plaza'){
   if(ASIA.test(city))return'temple-asia';
   if(LAT.test(city)||/miami|salvador|san antonio|tucson|santa fe|albuquerque|houston|el paso/.test(city))return'plaza-latin';
   if(EUR.test(city)||HIST.test(city))return'plaza-europe';
   if(/honolulu|san diego/.test(city))return'beach';
   if(MTN.test(city))return'mountain-trail';
   return'city-street'}
  if(sc==='park'&&MTN.test(city))return'mountain-trail';
  if(sc==='park'&&/honolulu|san diego|miami|tampa/.test(city))return'beach';
  if(sc==='lobby'&&/las vegas|miami|new york/.test(city))return'hotel-lobby';
  return k}
 var emj=[[/☕|🥐|🥯|🍕/,'cafe-interior'],[/✈|🧳|🛫/,'airport'],[/🏖|🌊|🏄|🌴/,'beach'],[/🚇|🚆|🚉/,'subway'],[/🏛|🖼|🎨/,'museum-gallery'],[/📚/,'library'],[/🏔|⛰|🥾/,'mountain-trail'],[/🛒|🍎|🥕/,'market'],[/🌳|🌲/,'park'],[/🏨|🛎/,'hotel-lobby'],[/🍳|🔪/,'kitchen'],[/🌃|🌙/,'night-skyline'],[/🛕|⛩|🏯/,'temple-asia']],tt=String(typeof x==='string'?x:(x&&x.emo?[].concat(x.emo).join(''):'')),i;
 for(i=0;i<RULES.length;i++)if(RULES[i][0].test(t))return RULES[i][1];
 for(i=0;i<emj.length;i++)if(emj[i][0].test(tt))return emj[i][1];
 if(ASIA.test(t))return'temple-asia';
 if(LAT.test(t))return'plaza-latin';
 if(EUR.test(t))return'plaza-europe';
 if(MTN.test(t))return'mountain-trail';
 return'city-street'}

function frame(kind,o){
 o=o||{};var k=(KINDS.indexOf(kind)>=0||kind==='fallback')?kind:pick(kind),cap=o.caption!=null?o.caption:'',r=o.radius!=null?o.radius:16;
 return'<figure class="pogillus-frame" style="margin:0;position:relative;border-radius:'+r+'px;overflow:hidden;background:#0b1020;box-shadow:0 1px 0 rgba(255,255,255,.08) inset,0 10px 30px -10px rgba(0,0,0,.55),0 2px 6px rgba(0,0,0,.3);border:1px solid rgba(255,255,255,.1)'+(o.style?';'+o.style:'')+'">'+scene(k,o)+
  '<span style="position:absolute;inset:0;border-radius:'+r+'px;box-shadow:inset 0 0 0 1px rgba(255,255,255,.06),inset 0 -60px 70px -40px rgba(0,0,0,.45);pointer-events:none"></span>'+
  (cap?'<figcaption style="position:absolute;left:0;right:0;bottom:0;padding:26px 16px 12px;font:600 13px/1.3 system-ui,-apple-system,Segoe UI,sans-serif;color:#fff;letter-spacing:.01em;background:linear-gradient(to top,rgba(0,0,0,.62),rgba(0,0,0,0));text-shadow:0 1px 3px rgba(0,0,0,.6)">'+String(cap).replace(/</g,'&lt;')+'</figcaption>':'')+'</figure>'}

w.PogIllus={scene:scene,pick:pick,frame:frame,kinds:KINDS.slice(),auto:function(t,o){return scene(pick(t),o)},moods:['dawn','day','sunset','night'],_S:S};
})(window);
