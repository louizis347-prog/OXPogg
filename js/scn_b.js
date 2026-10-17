/* Pogglot - scenes B: airport, lobby, station (illustrated SVG, deterministic) */
(function(){
window.RS = window.RS || {};
function LG(u,id,x1,y1,x2,y2,st){var s='<linearGradient id="'+u+'-'+id+'" gradientUnits="userSpaceOnUse" x1="'+x1+'" y1="'+y1+'" x2="'+x2+'" y2="'+y2+'">';for(var i=0;i<st.length;i++)s+='<stop offset="'+st[i][0]+'" stop-color="'+st[i][1]+'"'+(st[i][2]!=null?' stop-opacity="'+st[i][2]+'"':'')+'/>';return s+'</linearGradient>';}
function RG(u,id,cx,cy,r,st){var s='<radialGradient id="'+u+'-'+id+'" gradientUnits="userSpaceOnUse" cx="'+cx+'" cy="'+cy+'" r="'+r+'">';for(var i=0;i<st.length;i++)s+='<stop offset="'+st[i][0]+'" stop-color="'+st[i][1]+'"'+(st[i][2]!=null?' stop-opacity="'+st[i][2]+'"':'')+'/>';return s+'</radialGradient>';}
function F(u,id){return 'url(#'+u+'-'+id+')';}
function R(x,y,w,h,fill,ex){return '<rect x="'+x+'" y="'+y+'" width="'+w+'" height="'+h+'" fill="'+fill+'"'+(ex||'')+'/>';}
function P(pts,fill,ex){return '<polygon points="'+pts+'" fill="'+fill+'"'+(ex||'')+'/>';}
function L(x1,y1,x2,y2,st,w,ex){return '<line x1="'+x1+'" y1="'+y1+'" x2="'+x2+'" y2="'+y2+'" stroke="'+st+'" stroke-width="'+w+'"'+(ex||'')+'/>';}
function E(cx,cy,rx,ry,fill,ex){return '<ellipse cx="'+cx+'" cy="'+cy+'" rx="'+rx+'" ry="'+ry+'" fill="'+fill+'"'+(ex||'')+'/>';}
function T(x,y,s,sz,fill,o){o=o||{};return '<text x="'+x+'" y="'+y+'" font-family="'+(o.f||'Arial,Helvetica,sans-serif')+'" font-size="'+sz+'" fill="'+fill+'"'+(o.w?' font-weight="'+o.w+'"':'')+(o.a?' text-anchor="'+o.a+'"':'')+(o.ls?' letter-spacing="'+o.ls+'"':'')+'>'+s+'</text>';}
function r1(n){return Math.round(n*10)/10;}
function WRAP(u,defs,body){
  return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 270" width="100%" height="100%" preserveAspectRatio="xMidYMid slice" role="img" aria-hidden="true" style="width:100%;height:100%;display:block"><defs>'+defs+
  '<filter id="'+u+'-nz" filterUnits="userSpaceOnUse" x="0" y="0" width="480" height="270"><feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" seed="7"/><feColorMatrix values="0 0 0 0 0.25 0 0 0 0 0.22 0 0 0 0 0.2 1.4 0 0 0 -0.45"/></filter>'+
  '<filter id="'+u+'-bl" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="1.3"/></filter>'+
  '</defs>'+body+'</svg>';
}
function vignette(u){return RG(u,'vg',240,125,300,[[0.55,'#000',0],[1,'#1a1208',0.32]]);}

/* ============================ AIRPORT ============================ */
RS.airport = function(u){
  var d='', b='', i, x;
  d+=LG(u,'sky',0,28,0,116,[[0,'#6fa6d4'],[0.6,'#b9d6ea'],[1,'#eef3f2']]);
  d+=LG(u,'ap',0,112,0,152,[[0,'#9aa0a5'],[1,'#7d8286']]);
  d+=LG(u,'fl',0,150,0,270,[[0,'#ecebe6'],[0.25,'#dedbd3'],[1,'#cfccc3']]);
  d+=LG(u,'ce',0,0,0,30,[[0,'#2b323a'],[1,'#4a525c']]);
  d+=LG(u,'wl',0,0,40,0,[[0,'#6b737b'],[1,'#8c939a']]);
  d+=LG(u,'wr',440,0,480,0,[[0,'#8c939a'],[1,'#6b737b']]);
  d+=LG(u,'gl',0,0,1,1,[[0,'#fff',0.4],[1,'#fff',0]]);
  d+=LG(u,'bd',0,38,0,98,[[0,'#10264a'],[1,'#0a1830']]);
  d+=LG(u,'fu',0,95,0,114,[[0,'#ffffff'],[1,'#c6cfd6']]);
  d+=LG(u,'dk',0,153,0,172,[[0,'#f4f5f6'],[1,'#c9ced4']]);
  d+=LG(u,'rf',0,150,0,205,[[0,'#fff',0.55],[1,'#fff',0]]);
  d+=LG(u,'bw',352,0,440,0,[[0,'#b3b9be'],[1,'#98a0a7']]);
  d+=LG(u,'cy',0,134,0,152,[[0,'#cfd9e2'],[1,'#aeb9c4']]);
  d+=LG(u,'cl',0,170,0,215,[[0,'#d3d0c8',0],[0.45,'#d3d0c8',0.9],[1,'#d3d0c8',1]]);
  d+=RG(u,'sh',0,0,1,[[0,'#2a2a2a',0.35],[1,'#2a2a2a',0]]);
  d+=RG(u,'lt',0,0,1,[[0,'#fff6dc',0.9],[1,'#fff6dc',0]]);
  d+=vignette(u);
  // base
  b+=R(0,0,480,270,'#d6d3cb');
  // sky + far scene
  b+=R(40,28,400,88,F(u,'sky'));
  b+='<g filter="url(#'+u+'-bl)">';
  b+=E(120,56,30,5,'#fff','opacity=".7"')+E(150,60,24,4,'#fff','opacity=".6"')+E(330,48,34,5,'#fff','opacity=".55"')+E(398,64,22,4,'#fff','opacity=".5"');
  b+=P('40,110 40,100 70,100 70,95 105,95 105,100 150,100 150,97 190,97 190,102 230,102 230,110','#a9b8c4');
  b+=R(96,76,3,24,'#9fb0bd')+P('90,76 105,76 103,70 92,70','#8fa2b1')+R(92,70,11,6,'#c4d3de');
  b+=P('300,110 300,103 345,103 345,99 380,99 380,106 440,106 440,110','#a9b8c4');
  b+=R(40,108,400,9,'#8aa174');
  b+=R(40,116,400,36,F(u,'ap'));
  b+=L(40,141,440,141,'#c8a93a',0.8,' stroke-dasharray="10 7" opacity=".85"');
  b+=L(40,127,440,127,'#b9bdc0',0.5,' opacity=".6"');
  // baggage cart train
  b+=R(150,125,13,4,'#d96b2b')+R(165,125,13,4,'#b8bcc0')+R(180,125,13,4,'#b8bcc0')+R(195,125,13,4,'#b8bcc0');
  b+=R(150,119,12,6,'#e8e0c8')+E(153,130,1.4,1.4,'#222')+E(160,130,1.4,1.4,'#222')+E(170,130,1.4,1.4,'#222')+E(200,130,1.4,1.4,'#222');
  // cones
  b+=P('252,138 255,138 253.5,132','#e5702a')+P('300,140 303,140 301.5,134','#e5702a');
  // aircraft
  b+=E(292,124,64,3.4,'#4f5a52','opacity=".35"');
  b+='<path d="M228 103C228 96 240 95 262 95L322 95C342 95 352 101 356 106C352 111 338 113 322 113L244 113C232 113 228 110 228 103Z" fill="'+F(u,'fu')+'"/>';
  b+='<path d="M232 98L225 76L240 76L264 96Z" fill="#fff"/><path d="M226 78L238 78L242 85L228 85Z" fill="#1f4e8c"/>';
  b+='<path d="M282 107L308 107L274 121L262 121Z" fill="#dce3e8"/><path d="M270 107L296 107L264 118L256 118Z" fill="#c9d1d8" opacity=".8"/>';
  b+=L(232,108,352,108,'#1f4e8c',1.4);
  for(i=0;i<19;i++)b+='<circle cx="'+(252+i*4.5)+'" cy="101.5" r=".9" fill="#2d3b4a"/>';
  b+='<path d="M342 99.5L350 102L346 103.5L341 103Z" fill="#1d2a38"/>';
  b+=E(291,114,9,4.2,'#c5ccd2')+E(284.5,114,2.2,3.6,'#3a424a');
  b+=L(270,113,270,121,'#555',1)+E(270,122,2.3,2.3,'#1a1a1a')+L(340,112,340,121,'#555',1)+E(340,122,2.1,2.1,'#1a1a1a');
  b+='</g>';
  // glass reflections
  b+=P('60,28 110,28 70,150 40,150',F(u,'gl'))+P('150,28 175,28 120,150 98,150',F(u,'gl'))+P('300,28 335,28 290,150 262,150',F(u,'gl'),' opacity=".7"');
  // right wall panel + baggage opening
  b+=R(352,28,88,124,F(u,'bw'));
  for(x=364;x<440;x+=22)b+=L(x,28,x,152,'#7f878e',0.6,' opacity=".6"');
  b+=L(352,62,440,62,'#7f878e',0.6,' opacity=".5"');
  b+='<g transform="translate(-10 0)">';
  b+=R(372,126,48,26,'#14171b');
  for(x=373;x<420;x+=3.4)b+='<path d="M'+x+' 126Q'+(x+0.8)+' 140 '+(x+0.2)+' 152" stroke="#2b3036" stroke-width="2.4" fill="none"/>';
  b+=R(370,103,52,17,'#101418')+T(396,110,'BAGGAGE CLAIM',4.3,'#e9eef3',{a:'middle',w:'bold',ls:'.3'})+T(381,118.5,'Belt',4,'#aeb7c0',{a:'middle'})+T(412,118.5,'4',8,'#f2c230',{a:'middle',w:'bold'});
  b+=L(371,120,371,126,'#444',1)+L(421,120,421,126,'#444',1);
  b+='</g>';
  // mullions
  for(i=0;i<9;i++){x=40+i*50;if(x>=352&&x<440)continue;b+=R(x-1.6,28,3.2,124,'#3a4149')+R(x-0.4,28,0.8,124,'#6d767e');}
  b+=R(40,60.5,312,1.6,'#3a4149')+R(40,148,400,5,'#4d555d')+R(40,28,400,3,'#2c333a');
  // walls & ceiling
  b+=P('0,13.6 40,28 40,152 0,162',F(u,'wl'))+P('480,13.6 440,28 440,152 480,162',F(u,'wr'));
  for(i=1;i<6;i++){var yy=28+i*20;b+=L(40,yy,0,yy+(yy-100)*0.2,'#4a5159',0.6,' opacity=".5"');b+=L(440,yy,480,yy+(yy-100)*0.2,'#4a5159',0.6,' opacity=".5"');}
  b+=P('0,0 480,0 480,13.6 440,28 40,28 0,13.6',F(u,'ce'));
  [[24,1.06],[12,1.22],[1,1.4]].forEach(function(r){[-150,-50,50,150].forEach(function(xw){var w=34*r[1],cx=240+xw*r[1];b+=R(r1(cx-w/2),r[0],r1(w),2.2,'#fff4d6','opacity=".9"');b+=E(cx,r[0]+3,w*0.7,3.5,F(u,'lt'),'opacity=".35"');});});
  b+=L(40,28,0,13.6,'#1e242a',1)+L(440,28,480,13.6,'#1e242a',1);
  // floor
  b+=P('0,162 40,152 440,152 480,162 480,270 0,270',F(u,'fl'));
  b+=P('40,152 440,152 470,208 10,208',F(u,'rf'));
  for(i=0;i<9;i++){x=40+i*50;b+=P(x+1+','+152+' '+(x+49)+',152 '+(240+(x+24-240)*1.5)+',210 '+(240+(x+24-240)*1.5-14)+',210','#fff','opacity=".14"');}
  for(i=-4;i<=12;i++){var xb=i*70-60;b+=L(r1(240+(xb-240)*50/170),152,xb,270,'#b4b1a8',0.6,' opacity=".4"');}
  [158,166,178,196,224,260].forEach(function(y){b+=L(0,y,480,y,'#b4b1a8',0.6,' opacity=".32"');});
  // sign reflections on floor
  b+=R(72,156,104,26,'#2b5da8','opacity=".07"')+R(258,156,76,10,'#f2c230','opacity=".1"');
  // arrivals sign
  b+=L(272,28,272,38,'#222',1.2)+L(322,28,322,38,'#222',1.2);
  b+=R(262,34,72,20,'#f2c230')+R(262,34,72,2,'#fbe28a')+R(262,52,72,2,'#c79a14');
  b+=T(268,48,'Arrivals',11,'#16181a',{w:'bold'});
  b+='<path d="M321 40h6v6h3l-6 6-6-6h3z" fill="#16181a"/>';
  b+=R(264,54,68,3,'#000','opacity=".15"');
  // board
  b+=L(90,28,90,40,'#222',1.2)+L(160,28,160,40,'#222',1.2);
  b+=R(70,38,108,62,'#1a2026')+R(72,40,104,58,F(u,'bd'));
  var rowsA=[['14:20','LONDON','LANDED','#7ee2a0'],['14:35','TOKYO','ON TIME','#e8f0ff'],['14:50','MADRID','DELAYED','#ff8a6a']];
  var rowsD=[['16:05','ROME','B12','#e8f0ff'],['16:20','SEOUL','B07','#e8f0ff'],['16:45','SYDNEY','C03','#e8f0ff']];
  b+=R(72,41,104,7,'#e9a91c')+T(76,46.6,'ARRIVALS',4.8,'#14181c',{w:'bold',f:'Arial,sans-serif'})+T(172,46.6,'STATUS',3.8,'#14181c',{a:'end',w:'bold'});
  rowsA.forEach(function(r,k){var y=54+k*6;b+=T(76,y,r[0],4.5,'#ffd25a',{f:'monospace'})+T(98,y,r[1],4.5,'#e8f0ff',{f:'monospace'})+T(172,y,r[2],4,r[3],{a:'end',f:'monospace'});});
  b+=R(72,70,104,7,'#e9a91c')+T(76,75.6,'DEPARTURES',4.8,'#14181c',{w:'bold'})+T(172,75.6,'GATE',3.8,'#14181c',{a:'end',w:'bold'});
  rowsD.forEach(function(r,k){var y=83+k*5.8;b+=T(76,y,r[0],4.5,'#ffd25a',{f:'monospace'})+T(98,y,r[1],4.5,'#e8f0ff',{f:'monospace'})+T(172,y,r[2],4.4,'#e8f0ff',{a:'end',f:'monospace'});});
  b+=P('72,40 120,40 96,98 72,98','#fff','opacity=".05"');
  // check-in bank
  b+=R(192,126,68,22,F(u,'cy'))+R(192,126,68,2,'#e9edf1')+T(226,138,'CHECK-IN',6,'#17386a',{a:'middle',w:'bold',ls:'.4'})+T(226,145.5,'A   B   C',4.4,'#4a5f7c',{a:'middle'});
  b+=R(194,148,64,10,'#e7eaee')+R(194,148,64,1.6,'#2d3238')+R(194,155,64,3,'#b6bcc3');
  b+=R(200,143,6,5,'#23282e')+R(222,143,6,5,'#23282e')+R(244,143,6,5,'#23282e');
  b+=E(226,159.5,36,2.2,F(u,'sh'),'');
  // info desk
  b+=R(80,126,88,24,'#1f4e8c')+R(80,126,88,1.6,'#4a7cc0')+'<circle cx="94" cy="138" r="6" fill="#fff"/>'+T(94,141,'i',8.5,'#1f4e8c',{a:'middle',w:'bold',f:'Georgia,serif'})+T(130,141,'Information',8,'#fff',{a:'middle',w:'bold'});
  b+=R(82,150,3,4,'#444')+R(163,150,3,4,'#444');
  b+=P('80,153 168,153 173,159 75,159','#2b3036');
  b+=R(75,159,98,14,F(u,'dk'));
  b+=R(75,159,98,2,'#fff','opacity=".6"')+R(75,166,98,2.2,'#2a6fbd','opacity=".75"')+R(75,171,98,2,'#8f969d');
  b+=R(96,147,12,6,'#20262c')+R(98,148,8,4,'#7aa7d8','opacity=".5"')+R(138,147,12,6,'#20262c')+R(140,148,8,4,'#7aa7d8','opacity=".5"');
  b+=E(124,176,56,4.5,F(u,'sh'),'');
  // carousel
  var cx=362,cy=161;
  b+=E(cx+1,cy+4,50,9,'#2c3035')+E(cx,cy+2.5,49.5,8.6,'#3c4147')+E(cx,cy,49.5,8.6,'#8a9097')+E(cx,cy,43,6.6,'#2e3237')+E(cx,cy,36,4.8,'#555c63')+E(cx,cy-0.5,34,3.6,'#6c747b');
  b+='<path d="M'+(cx-49)+' '+cy+'A49.5 8.6 0 0 1 '+(cx+49)+' '+cy+'" fill="none" stroke="#fff" stroke-width=".8" opacity=".5"/>';
  var bags=[[215,'#7a2d34'],[262,'#25282c'],[320,'#b38a58'],[40,'#264a7a'],[105,'#2d6f6a'],[150,'#8a3a3a']];
  bags.forEach(function(g){var a=g[0]*Math.PI/180,sc=Math.sin(a)<0?0.85:1.05,px=cx+39.5*Math.cos(a),py=cy+5.7*Math.sin(a),w=11*sc,h=8*sc;
    b+='<path d="M'+r1(px-w*0.2)+' '+r1(py-h)+'v-2.4h'+r1(w*0.4)+'v2.4" stroke="#222" stroke-width=".9" fill="none"/>';
    b+='<rect x="'+r1(px-w/2)+'" y="'+r1(py-h)+'" width="'+r1(w)+'" height="'+r1(h)+'" rx="1.6" fill="'+g[1]+'"/><rect x="'+r1(px-w/2)+'" y="'+r1(py-h)+'" width="'+r1(w)+'" height="1.6" rx=".8" fill="#fff" opacity=".22"/>'+L(r1(px-w*0.2),r1(py-h+1.5),r1(px-w*0.2),r1(py-0.5),'#000',0.5,' opacity=".3"')+L(r1(px+w*0.2),r1(py-h+1.5),r1(px+w*0.2),r1(py-0.5),'#000',0.5,' opacity=".3"');});
  // trolleys
  [[174,189],[181,188],[188,187]].forEach(function(t,k){var bx=t[0],by=t[1];
    b+=E(bx+16,by+1,18,2.4,F(u,'sh'),'');
    b+=E(bx+5,by,1.6,1.6,'#1a1c1f')+E(bx+25,by,1.6,1.6,'#1a1c1f')+L(bx+3,by-2.6,bx+27,by-2.6,'#8d959d',1.2);
    var s='<path d="M'+(bx+5)+' '+(by-4)+'L'+(bx+2)+' '+(by-17)+'H'+(bx+27)+'L'+(bx+24)+' '+(by-4)+'Z" fill="#dfe3e7" fill-opacity=".12" stroke="#9aa2aa" stroke-width=".8"/>';
    for(var q=1;q<5;q++)s+=L(r1(bx+5-3*(1-q/5)*0+ (q*4.5)),by-4,r1(bx+2+q*5),by-17,'#9aa2aa',0.45);
    s+=L(bx+4,by-10.5,bx+25,by-10.5,'#9aa2aa',0.45)+'<path d="M'+(bx+25)+' '+(by-17)+'L'+(bx+29)+' '+(by-24)+'H'+(bx+35)+'" stroke="#4a5158" stroke-width="1.5" fill="none" stroke-linecap="round"/>'+L(bx+30,by-24,bx+35,by-24,'#2a6fbd',1.8);
    b+=s;});
  // calm floor + overlays
  b+=R(0,170,480,100,F(u,'cl'));
  b+=R(0,0,480,270,'#000','filter="url(#'+u+'-nz)" opacity=".18"');
  b+=R(0,0,480,270,F(u,'vg'));
  return WRAP(u,d,b);
};

/* ============================ LOBBY ============================ */
RS.lobby = function(u){
  var d='', b='', i, j, x;
  d+=LG(u,'wa',0,28,0,155,[[0,'#d9c6a3'],[1,'#c7ad84']]);
  d+=LG(u,'ce',0,0,0,30,[[0,'#f1e8d4'],[1,'#e2d4b6']]);
  d+=LG(u,'wd',0,38,0,125,[[0,'#6a452c'],[1,'#4a2e1c']]);
  d+=LG(u,'cf',0,128,0,155,[[0,'#9a6338'],[1,'#6c4426']]);
  d+=LG(u,'ct',0,122,0,128,[[0,'#c78d58'],[1,'#a06a3c']]);
  d+=LG(u,'fl',0,155,0,270,[[0,'#efe8da'],[0.3,'#e0d7c5'],[1,'#d4cab6']]);
  d+=LG(u,'br',0,0,1,0,[[0,'#8a6a2c'],[0.5,'#f0d27a'],[1,'#a67f33']]);
  d+=LG(u,'dr',0,52,0,155,[[0,'#d6ebf7'],[0.6,'#f4f1e0'],[1,'#e8e3cc']]);
  d+=LG(u,'sf',0,140,0,170,[[0,'#2f7c7c'],[1,'#1e5b5d']]);
  d+=LG(u,'ar',0,144,0,172,[[0,'#dcc9a3'],[1,'#bfa87c']]);
  d+=LG(u,'lf',0,0,0,1,[[0,'#2f6a34'],[1,'#1f4a26']]);
  d+=LG(u,'sp',0,155,0,215,[[0,'#fffbe8',0.6],[1,'#fffbe8',0]]);
  d+=LG(u,'rf',0,155,0,175,[[0,'#4a2e1c',0.35],[1,'#4a2e1c',0]]);
  d+=LG(u,'cl',0,172,0,215,[[0,'#d8cfbc',0],[0.5,'#d8cfbc',0.85],[1,'#d8cfbc',1]]);
  d+=RG(u,'ch',240,38,95,[[0,'#ffe3a0',0.55],[1,'#ffe3a0',0]]);
  d+=RG(u,'lp',150,106,40,[[0,'#ffd88a',0.65],[1,'#ffd88a',0]]);
  d+=RG(u,'sh',0,0,1,[[0,'#2a1c10',0.4],[1,'#2a1c10',0]]);
  d+='<pattern id="'+u+'-st" width="9" height="10" patternUnits="userSpaceOnUse"><rect width="4" height="10" fill="#7a5a2a" opacity=".07"/></pattern>';
  d+=vignette(u);
  b+=R(0,0,480,270,'#d4cab6');
  b+=R(0,28,480,127,F(u,'wa'))+R(0,28,480,127,F(u,'st'));
  b+=R(0,0,480,30,F(u,'ce'))+R(0,26,480,5,'#f6eedb')+R(0,31,480,2,'#a88f63','opacity=".5"');
  // wainscot
  b+=R(0,114,480,41,'#b79c71');
  for(x=-6;x<480;x+=38)b+=R(x+4,118,30,30,'none',' stroke="#e2cfa6" stroke-width=".9" opacity=".7"')+R(x+4,118,30,30,'#000','opacity=".05"');
  b+=R(0,112,480,3,'#e5d3ab')+R(0,151,480,4,'#5a3b25')+R(0,151,480,1,'#8a6444');
  // feature wall behind desk
  b+=R(118,36,196,92,F(u,'wd'));
  for(x=122;x<314;x+=8)b+=R(x,36,1,92,'#000','opacity=".22"')+R(x+1,36,0.8,92,'#fff','opacity=".05"');
  b+=R(116,34,200,3,'#caa05a')+R(116,34,200,1,'#f0d48a');
  b+=R(118,36,196,92,F(u,'wd'),' opacity=".0"');
  // reception plate
  b+=R(150,43,64,11,'#2a1a10')+R(150.5,43.5,63,10,'none',' stroke="#e0bd6a" stroke-width=".7"')+T(182,51.2,'RECEPTION',6,'#efd48a',{a:'middle',w:'bold',ls:'.9',f:'Georgia,serif'});
  // keys
  b+=R(125,58,82,56,'#5a3a24')+R(125,58,82,56,'none',' stroke="#caa05a" stroke-width=".8"');
  var kc=['#e6c35c','#d9d9d9','#e6c35c','#cf9a45'],tg=['#f3ead2','#b8402f','#f3ead2','#f3ead2'];
  for(j=0;j<4;j++)for(i=0;i<8;i++){var kx=132+i*9.6,ky=66+j*12;
    b+='<circle cx="'+kx+'" cy="'+ky+'" r=".9" fill="#caa05a"/>'+L(kx,ky+1,kx,ky+6.4,kc[(i+j)%4],0.8)+'<circle cx="'+kx+'" cy="'+(ky+7.6)+'" r="1.5" fill="none" stroke="'+kc[(i+j)%4]+'" stroke-width=".8"/>'+R(r1(kx-1.6),ky+3.3,3.2,3.4,tg[(i*2+j)%4],' rx=".5" opacity=".95"');}
  // painting
  b+=R(286,60,22,30,'#caa05a')+R(288,62,18,26,'#a9c3c9')+'<path d="M288 80Q294 70 300 78T306 74V88H288Z" fill="#6f8f5a"/><path d="M288 84Q296 78 306 84V88H288Z" fill="#41603f"/>'+E(298,68,3,3,'#f5e7b8');
  // clock
  var ccx=250,ccy=82;
  b+='<circle cx="'+(ccx+1.5)+'" cy="'+(ccy+2.2)+'" r="16" fill="#000" opacity=".25"/><circle cx="'+ccx+'" cy="'+ccy+'" r="16" fill="#b58a3a"/><circle cx="'+ccx+'" cy="'+ccy+'" r="14.3" fill="#f6efd9"/><circle cx="'+ccx+'" cy="'+ccy+'" r="14.3" fill="none" stroke="#7a5a22" stroke-width=".7"/>';
  for(i=0;i<12;i++){var an=i*Math.PI/6;b+=L(r1(ccx+11.6*Math.sin(an)),r1(ccy-11.6*Math.cos(an)),r1(ccx+13.4*Math.sin(an)),r1(ccy-13.4*Math.cos(an)),'#3a2a14',i%3==0?1.2:0.6);}
  var ha=(3+40/60)*30*Math.PI/180,ma=240*Math.PI/180;
  b+=L(ccx,ccy,r1(ccx+7*Math.sin(ha)),r1(ccy-7*Math.cos(ha)),'#2a1c0e',1.5,' stroke-linecap="round"')+L(ccx,ccy,r1(ccx+11*Math.sin(ma)),r1(ccy-11*Math.cos(ma)),'#2a1c0e',1,' stroke-linecap="round"')+'<circle cx="'+ccx+'" cy="'+ccy+'" r="1.1" fill="#b58a3a"/>';
  // restroom sign
  b+=R(68,58,46,11,'#2a1a10')+R(68.5,58.5,45,10,'none',' stroke="#e0bd6a" stroke-width=".6"')+'<path d="M73 63.5h8M73 63.5l2.6-2.4M73 63.5l2.6 2.4" stroke="#efd48a" stroke-width="1.1" fill="none" stroke-linecap="round"/>'+T(98,66.6,'Restrooms',5.4,'#efd48a',{a:'middle',f:'Georgia,serif'});
  // glow from chandelier on wall
  b+=R(0,28,480,127,F(u,'ch'));
  // revolving door
  b+=R(330,48,86,107,'#2c2218');
  b+=R(334,52,78,103,F(u,'dr'));
  b+='<g filter="url(#'+u+'-bl)">'+E(352,116,14,16,'#9db88a','opacity=".45"')+E(397,110,16,20,'#8fae80','opacity=".4"')+R(342,128,66,16,'#b9c3c0','opacity=".6"')+R(360,100,22,40,'#c9c6b8','opacity=".5"')+'</g>';
  b+=P('334,52 412,52 340,155 334,155','#fff','opacity=".22"');
  b+=R(334,52,78,5,'#3a2c1e')+R(334,76,78,2,'#3a2c1e')+L(346,78,346,155,'#3a2c1e',2)+L(400,78,400,155,'#3a2c1e',2);
  b+='<path d="M348 78H398V152H348Z" fill="#e8f4fa" fill-opacity=".25"/>';
  b+=E(373,152,25,5,'#5a4a36')+E(373,151,23,4,'#2a2018')+E(373,150.5,19,3,'#a9a08e');
  b+=P('349,80 372,84 372,148 349,150','#fff','opacity=".18"',)+P('397,80 374,84 374,148 397,150','#fff','opacity=".1"');
  b+=L(373,80,373,150,'#3a2c1e',2.6)+L(349,80,349,150,'#8a6a42',1.2)+L(397,80,397,150,'#8a6a42',1.2);
  b+=R(348,78,50,3.4,'#4a382a')+R(348,147,50,3,'#4a382a');
  b+=R(355,112,2,12,'#e6c35c','opacity=".85"')+R(389,112,2,12,'#e6c35c','opacity=".85"');
  b+=R(330,48,86,4,'#2c2218');
  // floor
  b+=R(0,155,480,115,F(u,'fl'));
  for(i=-5;i<=13;i++){var xb=i*62-20;b+=L(r1(240+(xb-240)*40/155),155,xb,270,'#b3a78f',0.7,' opacity=".32"');}
  [158,164,173,187,208,240].forEach(function(y){b+=L(0,y,480,y,'#b3a78f',0.7,' opacity=".3"');});
  b+='<path d="M20 190Q90 176 140 196T260 188M300 215Q360 200 420 218M60 230Q130 215 200 238" stroke="#a89c85" stroke-width=".6" fill="none" opacity=".25"/>';
  b+=P('335,155 412,155 452,215 300,215',F(u,'sp'));
  b+=R(120,155,190,22,F(u,'rf'));
  b+='<ellipse cx="240" cy="205" rx="150" ry="20" fill="#fff0c0" opacity=".1"/>';
  // rug
  b+=E(150,182,82,14,'#8d4630','opacity=".92"')+E(150,182,76,11.5,'none',' stroke="#e3cfa0" stroke-width="1.2"')+E(150,182,66,9,'#a4553d')+E(150,182,57,6.5,'none',' stroke="#e9d9b2" stroke-width=".8" stroke-dasharray="3 2.5"');
  // counter
  b+=E(215,157,100,4,F(u,'sh'),' opacity=".8"');
  b+=P('130,122 300,122 306,128 124,128',F(u,'ct'));
  b+=R(124,128,182,27,F(u,'cf'));
  for(x=128;x<304;x+=22)b+=R(x,132,18,17,'#000','opacity=".14"')+R(x+0.8,132.8,16.4,15.4,'none',' stroke="#c28a56" stroke-width=".6" opacity=".6"');
  b+=R(124,128,182,1.6,'#e0a870','opacity=".7"')+R(124,149,182,1.6,F(u,'br'))+R(124,151,182,4,'#2e1d12');
  b+=R(124,128,182,27,'#000','opacity=".0"');
  b+=P('124,128 130,122 130,128','#000','opacity=".12"');
  // lamp
  b+='<circle cx="150" cy="106" r="40" fill="'+F(u,'lp')+'"/>';
  b+=R(148.4,112,3.2,10,'#b58a3a')+E(150,122.5,6,1.8,'#b58a3a')+'<path d="M141 98H159L163 112H137Z" fill="#f4e2b4"/><path d="M141 98H159L163 112H137Z" fill="#ffd88a" opacity=".6"/>'+L(141,98,159,98,'#caa66a',0.8);
  b+=E(150,123.5,8,2,F(u,'sh'),'');
  // bell
  b+=E(215,123.6,7,1.8,'#a37d30')+'<path d="M209 123.4Q209 115.6 215 115.6T221 123.4Z" fill="#d9b04a"/><path d="M211 122Q211 117.4 214 116.8" stroke="#fff4c8" stroke-width=".9" fill="none" opacity=".8"/>'+R(214,113.6,2,2.2,'#a37d30')+E(215,113.4,1.6,1,'#e6c35c');
  // monitor back
  b+=R(262,104,24,15,'#2b2e33')+R(262,104,24,1.2,'#4a4e55')+R(272,119,4,3,'#202328')+E(274,123,7,1.4,'#202328')+'<circle cx="274" cy="111.5" r="1.2" fill="#6a6e75"/>';
  // brochure holder + pen cup
  b+=P('232,124 244,124 243,113 233,113','#e6e0d0','opacity=".95"')+R(233,116,10,1,'#b8402f')+R(233,119.4,10,1,'#2f7c7c');
  b+=R(190,118,5,6,'#1f3a5c')+L(191.5,118,190.5,113,'#222',0.7)+L(193.5,118,194.6,114,'#b8402f',0.7);
  // chandelier
  b+=L(240,0,240,26,'#8a6a2c',1.2)+E(240,38,92,26,F(u,'ch'),'');
  b+=R(238,24,4,16,'#c49a46')+E(240,26,5,2.4,'#d9b04a');
  var tiers=[[34,32,5],[43,21,4]];
  tiers.forEach(function(t,k){var yy=t[0],rr=t[1],n=t[2]*2;
    b+='<path d="M'+(240-rr)+' '+yy+'Q240 '+(yy+9)+' '+(240+rr)+' '+yy+'" stroke="#c49a46" stroke-width="1.3" fill="none"/>';
    for(i=0;i<=n;i++){var px=240-rr+i*(2*rr/n),py=yy+9*2*(i/n)*(1-i/n)*0.0+ (yy+ 4.5*(1-Math.pow((px-240)/rr,2))-yy)*1;
      var by=yy+ (1-Math.pow((px-240)/rr,2))*4.5*1;
      b+='<circle cx="'+r1(px)+'" cy="'+r1(by-3.2)+'" r="1.6" fill="#fff0c0"/><circle cx="'+r1(px)+'" cy="'+r1(by-3.2)+'" r="3.4" fill="#ffe7a8" opacity=".35"/>'+L(r1(px),r1(by-1.6),r1(px),r1(by+0.5),'#c49a46',0.9)+'<path d="M'+r1(px)+' '+r1(by+1)+'l-1.1 3.2l1.1 1.6l1.1 -1.6z" fill="#e8f2f6" opacity=".85"/>';}});
  [-22,-14,-6,6,14,22].forEach(function(o){b+='<path d="M'+(240+o)+' 46l-0.9 4l0.9 2.4l0.9-2.4z" fill="#e8f2f6" opacity=".85"/>';});
  b+=E(240,52,7,3.4,'#c49a46')+'<path d="M240 55l-2 5h4z" fill="#e8f2f6"/>';
  // left palm/plant big
  b+=E(80,163,19,3.4,F(u,'sh'),'');
  b+='<path d="M69 142H93L90 162Q81 164 72 162Z" fill="#e6e1d6"/><path d="M69 142H93L92 146H70Z" fill="#c9c3b6"/><path d="M69 142H93L90 162Q81 164 72 162Z" fill="#000" opacity=".1"/>';
  b+='<path d="M81 142Q80 120 83 96" stroke="#6a4a2c" stroke-width="2" fill="none"/>';
  var lv=[[-34,26,12,0],[30,28,12,0],[-14,32,13,1],[16,34,13,1],[-48,16,10,2],[46,18,10,2],[2,34,14,2],[-26,30,12,3],[22,20,11,3]];
  lv.forEach(function(l,k){var a=l[0],len=l[1],w=l[2],ly=[142,128,112,98][l[3]],bx=81-(l[3]*0.6);
    b+='<g transform="translate('+bx+' '+ly+') rotate('+a+')"><ellipse cx="0" cy="-'+(len/2+2)+'" rx="'+(w/2)+'" ry="'+(len/2)+'" fill="'+(k%2?'#2c5a2f':'#38723a')+'"/><line x1="0" y1="-2" x2="0" y2="-'+(len+1)+'" stroke="#9cc58a" stroke-width=".5" opacity=".6"/></g>';});
  // sofa
  b+=E(134,172.5,48,4.4,F(u,'sh'),'');
  b+=R(100,170,3,4,'#2a1a10')+R(165,170,3,4,'#2a1a10');
  b+='<rect x="98" y="141" width="72" height="22" rx="6" fill="#256a6a"/><rect x="98" y="141" width="72" height="3" rx="1.5" fill="#4a9a96" opacity=".7"/>';
  [[102,22],[125,22],[148,18]].forEach(function(c){b+='<rect x="'+c[0]+'" y="144" width="'+c[1]+'" height="19" rx="4" fill="'+F(u,'sf')+'"/><rect x="'+c[0]+'" y="144" width="'+c[1]+'" height="2" rx="1" fill="#6bb3ad" opacity=".5"/>';});
  b+='<rect x="96" y="150" width="10" height="21" rx="4" fill="#1f5b5d"/><rect x="162" y="150" width="10" height="21" rx="4" fill="#1f5b5d"/><rect x="96" y="150" width="10" height="3" rx="1.5" fill="#4a9a96" opacity=".6"/><rect x="162" y="150" width="10" height="3" rx="1.5" fill="#4a9a96" opacity=".6"/>';
  b+='<rect x="105" y="159" width="62" height="11" rx="3" fill="#2d7b7a"/><rect x="105" y="159" width="30" height="11" rx="3" fill="#3a8c88"/><rect x="105" y="159" width="62" height="1.5" fill="#7cc4bc" opacity=".5"/>'+L(135,160,135,170,'#1b4c4e',0.7);
  b+='<rect x="108" y="147" width="14" height="14" rx="3" transform="rotate(-8 115 154)" fill="#d6a033"/><rect x="108" y="147" width="14" height="3" rx="1.5" transform="rotate(-8 115 154)" fill="#f0c968" opacity=".6"/>';
  // armchair
  b+=E(194,172.5,20,3.6,F(u,'sh'),'');
  b+=R(179,169,2.6,5,'#2a1a10')+R(205,169,2.6,5,'#2a1a10');
  b+='<rect x="178" y="146" width="30" height="24" rx="7" fill="#c4ac80"/><rect x="178" y="146" width="30" height="3" rx="1.5" fill="#efe0be" opacity=".7"/><rect x="183" y="150" width="20" height="12" rx="4" fill="'+F(u,'ar')+'"/><rect x="175.5" y="156" width="8" height="15" rx="3.5" fill="#b49c70"/><rect x="202.5" y="156" width="8" height="15" rx="3.5" fill="#b49c70"/><rect x="183" y="162" width="20" height="8" rx="3" fill="#dcc9a3"/><rect x="183" y="162" width="20" height="1.4" fill="#fff" opacity=".4"/>';
  // coffee table
  b+=E(135,187,28,3.4,F(u,'sh'),'')+E(135,181,24,4.6,'#4a2e1c')+E(135,180,24,4.6,'#7a4e2c')+E(135,179.6,22,3.8,'#a06a3c')+L(118,182,118,188,'#2a1a10',1.4)+L(152,182,152,188,'#2a1a10',1.4);
  b+=R(124,176,12,2.4,'#1f3a5c')+R(125,174,10,2.2,'#b8402f')+'<path d="M147 178h5l-0.8-6h-3.4z" fill="#e6e1d6"/><path d="M149.5 172Q148 166 151 163M149.5 172Q152 167 154 166" stroke="#4a8a44" stroke-width="1" fill="none"/><ellipse cx="151" cy="163" rx="2" ry="1.4" fill="#d96b4a"/>';
  // right palm
  b+=E(321,163,13,3,F(u,'sh'),'');
  b+='<path d="M311 146H331L329 162Q321 164 313 162Z" fill="#3a3530"/><path d="M311 146H331L330 149H312Z" fill="#5a544c"/>';
  [[-52,40],[-32,50],[-14,56],[4,58],[22,52],[40,44],[58,34]].forEach(function(l,k){var a=l[0]*Math.PI/180,len=l[1],ex=321+len*Math.sin(a)*0.6,ey=146-len*Math.cos(a)*0.92;
    b+='<path d="M321 146Q'+r1(321+len*Math.sin(a)*0.15)+' '+r1(146-len*0.6)+' '+r1(ex)+' '+r1(ey)+'" stroke="#3d7a3a" stroke-width="1.6" fill="none"/>';
    for(var q=1;q<=6;q++){var t=q/7,px=321+(ex-321)*t*(0.9)+len*Math.sin(a)*0.15*t*(1-t)*2*0,py=146+(ey-146)*t;
      b+='<ellipse cx="'+r1(px-3.2)+'" cy="'+r1(py+1)+'" rx="4.2" ry="1.2" transform="rotate(-25 '+r1(px-3.2)+' '+r1(py+1)+')" fill="'+(k%2?'#2e6a30':'#3d7a3a')+'"/><ellipse cx="'+r1(px+3.2)+'" cy="'+r1(py+1)+'" rx="4.2" ry="1.2" transform="rotate(25 '+r1(px+3.2)+' '+r1(py+1)+')" fill="'+(k%2?'#3d7a3a':'#2e6a30')+'"/>';}});
  // calm floor + overlays
  b+=R(0,172,480,98,F(u,'cl'),'');
  b+=R(0,155,480,115,'#000','filter="url(#'+u+'-nz)" opacity=".14"');
  b+=R(0,0,480,270,F(u,'vg'));
  return WRAP(u,d,b);
};

/* ============================ STATION ============================ */
RS.station = function(u){
  var d='', b='', i, j, x, VX=240, VY=105;
  function tp(px,py,k){return [r1(VX+k*(px-VX)),r1(VY+k*(py-VY))];}
  function qb(t,p0,c,p2){return [(1-t)*(1-t)*p0[0]+2*t*(1-t)*c[0]+t*t*p2[0],(1-t)*(1-t)*p0[1]+2*t*(1-t)*c[1]+t*t*p2[1]];}
  d+=LG(u,'wl',0,0,60,0,[[0,'#7d7364'],[1,'#a39887']]);
  d+=LG(u,'wr',420,0,480,0,[[0,'#a39887'],[1,'#7d7364']]);
  d+=LG(u,'ew',0,30,0,155,[[0,'#c8bda8'],[1,'#b3a78f']]);
  d+=LG(u,'fl',0,155,0,270,[[0,'#d9d3c6'],[0.3,'#cbc4b5'],[1,'#bfb8a8']]);
  d+=LG(u,'sk',0,54,0,120,[[0,'#cfe0ea'],[0.7,'#f1efe2'],[1,'#fbf4dc']]);
  d+=LG(u,'cn',0,60,0,100,[[0,'#4b545c'],[1,'#6a737b']]);
  d+=LG(u,'tr',0,86,0,128,[[0,'#f2f4f6'],[0.45,'#dfe4e8'],[0.46,'#1f4a88'],[1,'#173a6e']]);
  d+=LG(u,'pf',0,105,0,155,[[0,'#cfcdc6'],[1,'#e2dfd6']]);
  d+=LG(u,'bg',0,105,0,155,[[0,'#4a4640'],[1,'#6a655c']]);
  d+=LG(u,'tk',0,100,0,150,[[0,'#7a4a2c'],[1,'#a56a3c']]);
  d+=LG(u,'ob',0,116,0,160,[[0,'#6a4a30'],[1,'#4a301c']]);
  d+=LG(u,'ts',0,0,0,1,[[0,'#fff',0.55],[1,'#fff',0]]);
  d+=LG(u,'sf',0,155,0,215,[[0,'#fff6dc',0.55],[1,'#fff6dc',0]]);
  d+=LG(u,'cl',0,172,0,215,[[0,'#c9c3b5',0],[0.5,'#c9c3b5',0.85],[1,'#c9c3b5',1]]);
  d+=RG(u,'sh',0,0,1,[[0,'#2a2418',0.38],[1,'#2a2418',0]]);
  d+=RG(u,'hg',240,125,70,[[0,'#fff8dc',0.75],[1,'#fff8dc',0]]);
  d+='<clipPath id="'+u+'-op"><path d="M160 156V104Q240 4 320 104V156Z"/></clipPath>';
  d+=vignette(u);
  var ARCH='M60 92Q240 -14 420 92';
  var ks=[2.4,1.8,1.45,1.2,1];
  var roofC=['#59616a','#6d767e','#8a949c','#b2bec7','#d2e0e8'];
  b+=R(0,0,480,270,'#a09583');
  // roof bands
  ks.forEach(function(k,n){b+='<path d="'+ARCH+'Z" transform="translate('+VX+' '+VY+') scale('+k+') translate(-'+VX+' -'+VY+')" fill="'+roofC[n]+'"/>';});
  // truss lattice between ribs
  var ptsA=[];for(i=0;i<=16;i++)ptsA.push(qb(i/16,[60,92],[240,-14],[420,92]));
  for(n=0;n<ks.length-1;n++){var ka=ks[n],kb=ks[n+1],s='';
    for(i=0;i<=16;i++){var pa=tp(ptsA[i][0],ptsA[i][1],ka),pb=tp(ptsA[i][0],ptsA[i][1],kb);s+='M'+pa[0]+' '+pa[1]+'L'+pb[0]+' '+pb[1];
      if(i<16){var pc=tp(ptsA[i+1][0],ptsA[i+1][1],kb);s+='M'+pa[0]+' '+pa[1]+'L'+pc[0]+' '+pc[1];}}
    b+='<path d="'+s+'" stroke="#3a4249" stroke-width=".7" fill="none" opacity=".55"/>';}
  var n;
  ks.slice(0,4).forEach(function(k){b+='<path d="'+ARCH+'" transform="translate('+VX+' '+VY+') scale('+k+') translate(-'+VX+' -'+VY+')" fill="none" stroke="#2f363c" stroke-width="2.6" vector-effect="non-scaling-stroke"/>';});
  // skylight sun
  b+=P('150,30 300,30 250,150 160,150',F(u,'ts'),' opacity=".25"');
  // side walls
  b+=P('60,92 60,156 -192,226 -192,83',F(u,'wl'))+P('420,92 420,156 672,226 672,83',F(u,'wr'));
  [[1.04,1.13],[1.2,1.31]].forEach(function(w){[1,-1].forEach(function(sg){
    var a=tp(240+sg*180,105-13,w[0]),bq=tp(240+sg*180,105-13,w[1]);
    var yt=function(k){return r1(VY+k*(-9));},yb=function(k){return r1(VY+k*34);};
    var x1=r1(VX+sg*180*w[0]),x2=r1(VX+sg*180*w[1]);
    b+=P(x1+','+yt(w[0])+' '+x2+','+yt(w[1])+' '+x2+','+yb(w[1])+' '+x1+','+yb(w[0]),'#e9f0f2','opacity=".9"')+P(x1+','+yt(w[0])+' '+x2+','+yt(w[1])+' '+x2+','+yb(w[1])+' '+x1+','+yb(w[0]),'none',' stroke="#4a4a42" stroke-width="1.2"');
  });});
  b+=L(60,92,-192,83,'#5a5346',1,' opacity=".6"');
  // end wall
  b+='<path d="M60 156V92Q240 -14 420 92V156Z" fill="'+F(u,'ew')+'"/>';
  for(i=0;i<16;i++)b+=L(60,40+i*7.5,420,40+i*7.5,'#7a6f5c',0.4,' opacity=".28"');
  b+='<path d="M60 92Q240 -14 420 92" fill="none" stroke="#2f363c" stroke-width="3.4"/><path d="M62 94Q240 -8 418 94" fill="none" stroke="#e6dcc5" stroke-width="1" opacity=".6"/>';
  // arch opening with platform
  b+='<g clip-path="url(#'+u+'-op)">';
  b+=R(150,50,180,110,F(u,'sk'));
  b+='<g filter="url(#'+u+'-bl)">'+P('160,106 160,98 185,98 185,92 200,92 200,100 215,100 215,96 235,96 235,106','#b9c4c9')+P('245,106 245,97 262,97 262,93 285,93 285,100 305,100 305,95 320,95 320,106','#b9c4c9')+'</g>';
  b+=R(150,105,180,52,'#8f8a7e');
  b+=P('150,66 224,93 224,97 150,76',F(u,'cn'))+P('330,66 256,93 256,97 330,76',F(u,'cn'));
  for(i=0;i<3;i++){var cxk=1+i*0.45,lx=r1(VX-80/(cxk)*0.99),rx=r1(VX+80/(cxk)*0.99);}
  [[168,76,105],[188,84,105],[206,91,105]].forEach(function(c){b+=L(c[0],c[1],c[0],c[2],'#4b545c',1.2);b+=L(660-c[0]-180,c[1],660-c[0]-180,c[2],'#4b545c',1.2);});
  b+=P('150,160 150,105 240,105 205,160',F(u,'pf'))+P('330,160 330,105 240,105 275,160',F(u,'pf'));
  b+=P('205,160 240,105 275,160',F(u,'bg'));
  b+=L(212,160,240,105,'#d9b72d',1.1)+L(268,160,240,105,'#d9b72d',1.1);
  b+=L(205,160,240,105,'#6f6a60',1.2)+L(275,160,240,105,'#6f6a60',1.2);
  [108,110.5,114,118.5,125,134,146,160].forEach(function(y){var h=(y-105)*0.7;b+=L(r1(VX-h),y,r1(VX+h),y,'#6e4a2d',1.4+(y-105)*0.04,' opacity=".85"');});
  [-1,1].forEach(function(sg){b+=L(r1(VX+sg*9*1),128,r1(VX+sg*(160-105)*0.0+sg*22),160,'#c3c9ce',1.1);});
  b+=L(r1(VX-14),128,r1(VX-24),160,'#d8dde1',1.1)+L(r1(VX+14),128,r1(VX+24),160,'#d8dde1',1.1);
  b+=L(VX-14,128,VX,105,'#9aa1a7',0.6)+L(VX+14,128,VX,105,'#9aa1a7',0.6);
  // train front
  b+=E(240,129,17,2.2,F(u,'sh'),'');
  b+='<path d="M225 128V94Q225 86 233 86H247Q255 86 255 94V128Z" fill="'+F(u,'tr')+'"/>';
  b+='<path d="M227.5 93Q227.5 90 231 90H249Q252.5 90 252.5 93V104H227.5Z" fill="#17222d"/><path d="M228 91L238 91L231 104H228Z" fill="#fff" opacity=".18"/>'+L(240,90,240,104,'#2a3844',1)+R(231,87.4,18,2.2,'#ffb02e');
  b+=R(231,108,18,5,'#0f2a52')+R(226,115,28,1,'#ffffff','opacity=".5"');
  b+='<circle cx="230" cy="119.5" r="2.1" fill="#fffbe8"/><circle cx="250" cy="119.5" r="2.1" fill="#fffbe8"/><circle cx="230" cy="119.5" r="5.5" fill="#fff6c8" opacity=".35"/><circle cx="250" cy="119.5" r="5.5" fill="#fff6c8" opacity=".35"/>';
  b+=R(236,122,8,4.5,'#2a2f35')+R(225,126,30,2,'#1a2330')+R(225,86,2,42,'#000','opacity=".12"')+R(253,86,2,42,'#000','opacity=".18"');
  b+=R(150,50,180,110,F(u,'hg'),' opacity=".3"');
  b+='</g>';
  b+='<path d="M160 156V104Q240 4 320 104V156" fill="none" stroke="#3a4249" stroke-width="3.2"/><path d="M164 156V104Q240 10 316 104V156" fill="none" stroke="#e6dcc5" stroke-width=".8" opacity=".6"/>';
  // floor
  b+='<path d="M60 156H420L480 171.7V270H0V171.7Z" fill="'+F(u,'fl')+'"/>';
  b+=P('160,156 320,156 306,210 176,210',F(u,'sf'));
  b+=P('96,156 150,156 126,214 40,214','#fff','opacity=".07"');
  for(i=-6;i<=14;i++){var xb=i*66-60;b+=L(r1(VX+(xb-VX)*51/165),156,xb,270,'#9b9484',0.7,' opacity=".4"');}
  [160,167,178,196,224,262].forEach(function(y){b+=L(0,y,480,y,'#9b9484',0.7,' opacity=".32"');});
  b+=L(60,156,420,156,'#7a7262',1.2,' opacity=".5"');
  // clock
  var cx=106,cy=72,rr=20;
  b+='<circle cx="'+(cx+2)+'" cy="'+(cy+3)+'" r="'+(rr+3)+'" fill="#000" opacity=".25"/><circle cx="'+cx+'" cy="'+cy+'" r="'+(rr+3)+'" fill="#23262a"/><circle cx="'+cx+'" cy="'+cy+'" r="'+(rr+2)+'" fill="none" stroke="#6d7379" stroke-width=".6"/><circle cx="'+cx+'" cy="'+cy+'" r="'+rr+'" fill="#f6f2e6"/>';
  for(i=0;i<60;i++){var an=i*Math.PI/30,big=i%5==0;b+=L(r1(cx+(rr-(big?4.4:2))*Math.sin(an)),r1(cy-(rr-(big?4.4:2))*Math.cos(an)),r1(cx+(rr-0.8)*Math.sin(an)),r1(cy-(rr-0.8)*Math.cos(an)),'#1c1c1c',big?1.5:0.5);}
  var ha=(10+10/60)*30*Math.PI/180,ma=10*6*Math.PI/180;
  b+=L(cx,cy,r1(cx+11*Math.sin(ha)),r1(cy-11*Math.cos(ha)),'#151515',2.6,' stroke-linecap="round"')+L(cx,cy,r1(cx+16.5*Math.sin(ma)),r1(cy-16.5*Math.cos(ma)),'#151515',1.8,' stroke-linecap="round"');
  var sa=33*6*Math.PI/180;
  b+=L(r1(cx-4*Math.sin(sa)),r1(cy+4*Math.cos(sa)),r1(cx+15*Math.sin(sa)),r1(cy-15*Math.cos(sa)),'#d1342c',0.8)+'<circle cx="'+cx+'" cy="'+cy+'" r="1.6" fill="#d1342c"/>';
  b+='<path d="M'+(cx-17)+' '+(cy-9)+'Q'+cx+' '+(cy-26)+' '+(cx+17)+' '+(cy-9)+'" fill="none" stroke="#fff" stroke-width="1" opacity=".35"/>';
  // departure board
  b+=R(338,52,76,50,'#1a2026')+R(340,54,72,46,'#0b1d3a')+R(340,54,72,8,'#e9a91c')+T(344,60.2,'DEPARTURES',5,'#14181c',{w:'bold'})+T(409,60.2,'PL.',4,'#14181c',{a:'end',w:'bold'});
  [['10:18','LEEDS','4'],['10:25','YORK','2'],['10:40','BATH','7'],['10:52','DOVER','3'],['11:05','DERBY','6']].forEach(function(r,k){var y=68.4+k*7.4;b+=T(344,y,r[0],4.7,'#ffd25a',{f:'monospace'})+T(364,y,r[1],4.7,'#e8f0ff',{f:'monospace'})+T(408,y,r[2],4.7,'#e8f0ff',{a:'end',f:'monospace'})+L(341,y+2.2,411,y+2.2,'#fff',0.3,' opacity=".18"');});
  b+=P('340,54 372,54 356,106 340,106','#fff','opacity=".05"');
  // ticket office
  b+=P('336,116 326,114.9 326,154.3 336,160','#3a2a1c')+P('336,116 326,114.9 326,121 336,121','#000','opacity=".15"');
  b+=R(336,116,80,44,F(u,'ob'));
  b+=R(334,108,84,9,'#241a12')+R(334,108,84,1.2,'#caa05a')+T(376,115,'TICKETS',6.6,'#efd48a',{a:'middle',w:'bold',ls:'1.2',f:'Georgia,serif'});
  [0,1,2].forEach(function(k){var wx=340+k*25;
    b+=R(wx,123,21,22,'#2a2218')+R(wx+1,124,19,20,'#ffd9a0')+R(wx+1,124,19,20,'#fff4d8','opacity=".35"')+P((wx+1)+',124 '+(wx+10)+',124 '+(wx+4)+',144 '+(wx+1)+',144','#fff','opacity=".25"')+R(wx+8,128,5,6,'#6a4a30','opacity=".55"')+R(wx+3,139,15,1.6,'#a3763e','opacity=".5"')+R(wx-1,145,23,3,'#9a6338')+R(wx-1,145,23,1,'#d9a46a')+T(wx+10.5,121,String(k+1),4.4,'#efd48a',{a:'middle',w:'bold'});});
  b+=R(336,150,80,10,'#2e2016')+R(336,150,80,1,'#8a6444');
  b+=E(376,161,46,3,F(u,'sh'),'');
  // benches
  [[72,172,1],[150,164,0.74]].forEach(function(bn){var bx=bn[0],by=bn[1],s=bn[2],w=58*s;
    b+=E(bx+w/2,by+1,w*0.58,3*s,F(u,'sh'),'');
    b+=R(bx+3*s,by-8*s,2.4*s,9*s,'#25282c')+R(bx+w-5.4*s,by-8*s,2.4*s,9*s,'#25282c')+R(bx+w/2-1.2*s,by-8*s,2.4*s,9*s,'#25282c');
    b+=R(bx,by-9*s,w,4.2*s,'#9a6a3a')+R(bx,by-9*s,w,1.1*s,'#c89358')+R(bx,by-4.4*s,w,3.8*s,'#7f5530')+R(bx,by-4.4*s,w,1*s,'#b07c48');
    b+=R(bx,by-22*s,w,3.8*s,'#8a5c32')+R(bx,by-22*s,w,1*s,'#bb8650')+R(bx,by-17*s,w,3.8*s,'#7f5530')+R(bx,by-17*s,w,1*s,'#b07c48')+R(bx+3*s,by-23*s,2*s,15*s,'#2a2d31')+R(bx+w-5*s,by-23*s,2*s,15*s,'#2a2d31');});
  // calm floor + overlays
  b+=R(0,172,480,98,F(u,'cl'));
  b+=R(0,155,480,115,'#000','filter="url(#'+u+'-nz)" opacity=".16"');
  b+=R(0,0,480,270,F(u,'vg'));
  return WRAP(u,d,b);
};
})();
