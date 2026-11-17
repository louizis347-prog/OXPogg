/* Cenários Quest adicionais (dentista, oculista, ferragens, tinturaria, lava-rápido, caixa eletrônico, celulares, shopping, roupas, sapatos, salão).
   Mesma API de scn_pro.js (SF helpers, 480×270). */
(function(){
if(!window.SF||!window.RS)return;
var SF=window.SF,RS=window.RS,rng=SF.rng,LG=SF.LG,RG=SF.RG,R=SF.R,RR=SF.RR,E=SF.E,C=SF.C,L=SF.L,P=SF.P,D=SF.D,S=SF.S,G=SF.G,INK=SF.INK,WRAP=SF.WRAP,vig=SF.vig,T=SF.T;
var SANS='Trebuchet MS,Arial,sans-serif';
function tile(y0,a,b,sz){var s='',i,j;for(j=0;y0+j*sz*.5<270;j++)for(i=0;i<480/sz+1;i++)s+=R(i*sz,y0+j*sz*.5,sz,sz*.5,(i+j)%2?a:b);return s}
function planks(y0,c1,c2,seed){var r=rng(seed),b=R(0,y0,480,270-y0,c1),i;for(i=0;i<14;i++)b+=L(0,y0+i*(270-y0)/14,480,y0+i*(270-y0)/14+(r()-.5)*2,c2,.8,' opacity=".35"');for(i=0;i<20;i++){var x=r()*480,y=y0+r()*(270-y0);b+=L(x,y,x+(r()-.5)*40,y+2,c2,.6,' opacity=".25"')}return b}
function sign(x,y,w,h,txt,bg,fg,sz){return RR(x,y,w,h,4,bg,INK)+T(x+w/2,y+h/2+(sz||12)*.35,txt,sz||12,fg||'#fff',{a:'middle',w:700,f:SANS})}
function base(u,wa,wb,fy,fl,lc){return LG(u,'w',0,0,0,fy,[[0,wa],[1,wb]])+LG(u,'f',0,fy,0,270,[[0,fl[0]],[1,fl[1]]])+RG(u,'lt',240,60,300,[[0,lc||'#fff0c8',.5],[1,lc||'#fff0c8',0]])+vig(u)}
function skirt(fy,c){return R(0,fy-5,480,6,c,INK)}
function lamps(xs,y,c){return xs.map(function(x){return L(x,0,x,y,'#222',1)+D('M'+(x-22)+' '+y+'h44l-8 14h-28z',c||'#3a3f46',INK)+C(x,y+16,28,'#ffe8b0',' opacity=".2"')}).join('')}
function plant(x,y,s){s=s||1;var b='',k;b+=P((x-9*s)+','+y+' '+(x+9*s)+','+y+' '+(x+6*s)+','+(y+22*s)+' '+(x-6*s)+','+(y+22*s),'#a8552f',INK);for(k=0;k<7;k++){var a=-2.6+k*.45;var ex=x+Math.cos(a)*34*s,ey=y+Math.sin(a)*40*s;b+=D('M'+x+' '+y+'Q'+(x+Math.cos(a-.5)*22*s)+' '+(y+Math.sin(a-.5)*28*s)+' '+ex+' '+ey+'Q'+(x+Math.cos(a+.5)*22*s)+' '+(y+Math.sin(a+.5)*28*s)+' '+x+' '+y+'z',k%2?'#3f7f3f':'#52a050',INK)}return b}
/* ---------- DENTISTA ---------- */
RS.dentist=function(u){var d,b='',i;
  d=base(u,'#e6f1ef','#cfe3e0',170,['#dfe6e8','#b8c3c6'],'#f4fbff');
  b+=R(0,0,480,170,'url(#'+u+'-w)')+tile(170,'#e2e8ea','#c9d3d6',30)+R(0,170,480,100,'url(#'+u+'-f)',' opacity=".3"')+skirt(170,'#9fb0b4')+R(0,0,480,170,'url(#'+u+'-lt)');
  b+=R(0,100,480,70,'#c8dcda')+R(0,98,480,4,'#fff',INK);
  /* janela com persiana */
  b+=R(14,24,96,70,'#e8eef0',INK)+R(18,28,88,62,'#a8d0e8');for(i=0;i<9;i++)b+=R(18,28+i*7,88,4,'#f4f6f6',' opacity=".85"');
  /* pôster de dentes e placa */
  b+=sign(130,18,120,24,'DENTAL CLINIC','#2a8aa8','#fff',12);
  b+=R(140,52,100,38,'#fff',INK)+T(190,66,'Brush twice a day',8,'#2a6a80',{a:'middle',w:700,f:SANS})+D('M168 74q-6-10 4-12q6 2 12 0q10-2 6 10q-2 8-5 8q-3-4-6-4q-4 0-6 4q-3 0-5-6z','#fff',INK)+D('M198 74q-6-10 4-12q6 2 12 0q10-2 6 10q-2 8-5 8q-3-4-6-4q-4 0-6 4q-3 0-5-6z','#fff',INK);
  /* diploma e raio-x */
  b+=R(262,34,38,28,'#f4ead4',INK)+L(268,44,294,44,'#a8884a',1)+L(268,50,290,50,'#a8884a',1)+C(281,57,3,'#c9302c');
  b+=R(312,28,60,44,'#1a2630',INK)+R(316,32,52,36,'#0c1a24')+[0,1,2,3,4,5,6].map(function(k){return D('M'+(320+k*7)+' 52q0-10 3-10t3 10q0 8-3 12q-3-4-3-12z','#dff0f8',' opacity=".85"')}).join('');
  /* armário com instrumentos (direita) */
  b+=R(390,60,86,110,'#f2f4f4',INK)+R(396,66,74,50,'#bfe0ec',INK)+L(433,66,433,116,'#fff',2)+R(396,124,74,40,'#e2e8ea',INK)+RR(430,138,6,14,2,'#777')
  +RR(402,98,10,18,2,'#2a8aa8',INK)+RR(416,92,8,24,2,'#e8503a',INK)+RR(444,96,10,20,2,'#f4f6f6',INK)+RR(458,100,8,16,2,'#2a8aa8',INK)+R(396,116,74,3,'#9aa0aa');
  /* luz de dentista (braço articulado) */
  b+=R(236,0,8,20,'#9aa0aa',INK)+L(240,18,300,48,'#aeb6bc',6)+L(300,48,330,34,'#aeb6bc',5)+C(300,48,6,'#8a929a',INK)+E(342,36,32,13,'#e8edf0',INK)+E(342,40,26,8,'#fff6c0')+E(342,70,70,34,'#fff6c0',' opacity=".18"')+E(342,40,12,5,'#fff');
  /* cadeira odontológica (esquerda) */
  b+=E(88,250,64,9,'#000',' opacity=".22"')+R(82,226,12,22,'#7a828a',INK)+E(88,250,38,7,'#5a626a',INK)
  +D('M30 206q-4-10 8-12l82 4q14 0 14 12l-2 8q-50 6-100 2z','#2a6a80',INK)+D('M26 206q-10-40 4-84q4-8 12-6l12 6q-8 40-4 84z','#2f7a92',INK)+R(30,130,18,60,'#fff',' opacity=".08"')
  +RR(110,190,56,8,3,'#2a6a80',INK)+R(160,196,6,22,'#7a828a')+RR(20,196,24,14,5,'#235a6e',INK)+RR(36,112,22,12,5,'#2f7a92',INK);
  /* unidade com cuspideira e bandeja */
  b+=R(160,102,5,60,'#9aa0aa',INK)+RR(152,96,34,10,3,'#e2e8ea',INK)+RR(158,84,22,12,3,'#fff',INK)+C(168,90,4,'#2a8aa8')+RR(172,112,8,24,3,'#cfd4dc',INK)+L(170,106,196,150,'#555',1.5)+C(198,152,3,'#e8503a')+RR(380,170,70,8,2,'#cfd4dc',INK)+[0,1,2,3,4].map(function(k){return L(388+k*12,170,390+k*12,158,'#9aa0aa',2)}).join('');
  b+=sign(398,182,60,14,'SMILE BRIGHT','#fff','#2a8aa8',8);
  b+=plant(462,226,.7);
  return WRAP(u,d,b)};
/* ---------- OCULISTA ---------- */
RS.eyedoctor=function(u){var d,b='',i,j,r=rng(7);
  d=base(u,'#efe9dc','#d9cfba',170,['#9a7a5a','#6d5238']);
  b+=R(0,0,480,170,'url(#'+u+'-w)')+planks(170,'#9a7a5a','#5a4028',3)+R(0,0,480,170,'url(#'+u+'-lt)')+skirt(170,'#4a3420');
  b+=R(0,118,480,52,'#3f6f6a')+R(0,116,480,4,'#c9b79a',INK);
  /* tabela de letras Snellen */
  b+=RR(190,16,100,128,4,'#fdfdf6',INK)+[['E',34,'#111'],['F P',22,'#111'],['T O Z',16,'#111'],['L P E D',12,'#111'],['P E C F D',9,'#111'],['E D F C Z P',7,'#111'],['F E L O P Z D',5.5,'#111']].reduce(function(a,t,k){var y=[40,64,82,98,110,121,130][k];return a+T(240,y,t[0],t[1],t[2],{a:'middle',w:700,f:'Georgia,serif',ls:t[1]>12?t[1]/3:2})},'');
  b+=sign(180,150,120,16,'EYE EXAM','#2f7f8f','#fff',10);
  /* prateleira de armações (esquerda) */
  b+=R(10,26,150,112,'#6b4a34',INK)+R(14,30,142,104,'#4a3020');
  for(j=0;j<4;j++){var y=36+j*26;b+=R(14,y+20,142,3,'#c9b79a',INK);for(i=0;i<5;i++){var x=24+i*27,c=['#222','#8a4a2a','#2f6a9a','#c9302c','#caa24a'][(i+j)%5];b+=C(x,y+10,6,'#cfe8f4',' stroke="'+c+'" stroke-width="2" opacity=".9"')+C(x+13,y+10,6,'#cfe8f4',' stroke="'+c+'" stroke-width="2" opacity=".9"')+L(x+6,y+9,x+7,y+9,c,2)}}
  /* mostruário direita + espelho */
  b+=R(318,26,150,70,'#c8dcda',INK)+R(322,30,142,62,'#e8f2f0')+P('322,92 360,30 392,30 354,92','#fff',' opacity=".35"');
  b+=R(306,100,166,10,'#3a2418',INK)+R(310,110,158,60,'#6b4a34',INK)+[0,1,2,3,4,5].map(function(k){return R(316+k*26,114,22,2,'#c9b79a')}).join('')+[0,1,2,3,4,5].map(function(k){var x=324+k*26;return C(x-4,106,4,'#cfe8f4',' stroke="#222" stroke-width="1.5"')+C(x+5,106,4,'#cfe8f4',' stroke="#222" stroke-width="1.5"')}).join('');
  b+=sign(332,6,100,18,'OPTICAL SHOP','#222','#e8c860',10);
  /* foróptero no braço (direita-baixo) e lupa */
  b+=R(436,150,6,40,'#555',INK)+RR(422,132,36,22,5,'#2a2f36',INK)+C(433,143,6,'#7fd0e0',INK)+C(447,143,6,'#7fd0e0',INK)+R(404,196,70,8,'#3a2418',INK)+R(412,204,6,40,'#3a2418')+R(462,204,6,40,'#3a2418');
  b+=C(46,196,18,'none',' stroke="#caa24a" stroke-width="4"')+C(46,196,15,'#cfe8f4',' opacity=".5"')+L(60,208,76,228,'#caa24a',5);
  b+=plant(24,226,.8);
  return WRAP(u,d,b)};
/* ---------- FERRAGENS ---------- */
RS.hardware=function(u){var d,b='',i,j,r=rng(11);
  d=base(u,'#d9cdb4','#b8a888',172,['#9a9a94','#6e6e68'],'#fff0c8');
  b+=R(0,0,480,172,'url(#'+u+'-w)')+R(0,172,480,98,'url(#'+u+'-f)')+skirt(172,'#4a4a46');
  for(i=0;i<8;i++)b+=L(0,176+i*12,480,176+i*12+4,'#4a4a46',.6,' opacity=".3"');
  b+=R(0,0,480,16,'#444a50')+lamps([60,200,340,440],16,'#cfd3d8');
  b+=sign(150,22,180,26,'HARDWARE STORE','#c9302c','#fff',16);
  /* painel de ferramentas (esquerda) */
  b+=R(10,56,150,110,'#8a6a44',INK);for(i=0;i<14;i++)for(j=0;j<8;j++)b+=C(16+i*10.5,62+j*13,.8,'#4a3420');
  b+=R(20,64,5,40,'#8a929a',INK)+RR(16,60,13,10,2,'#c9302c',INK)+D('M44 62h22v6h-22zM52 68h6v36h-6z','#8a929a',INK)+RR(78,64,10,34,3,'#caa24a',INK)+R(80,98,6,16,'#6a6a70')+D('M100 62q14-6 24 4l-4 6q-8-4-16 0z','#8a929a',INK)+R(106,70,6,40,'#a8552f',INK)+L(24,124,150,124,'#8a929a',1.5)+[0,1,2,3,4].map(function(k){return R(22+k*24,124,5,36-k*3,'#e8c860',INK)}).join('')+R(136,76,14,40,'#2f6a9a',INK)+C(143,84,4,'#cfe8f4');
  /* prateleiras com caixas e latas de tinta (direita) */
  b+=R(330,56,146,114,'#5a5a60',INK);for(j=0;j<3;j++){var y=62+j*36;b+=R(334,y+30,138,4,'#8a8a90',INK);for(i=0;i<8;i++){var h=20+Math.floor(r()*8),col=['#c9302c','#e8c860','#2f6a9a','#4f9a52','#fff','#e08a3f'][Math.floor(r()*6)];b+=R(338+i*17,y+30-h,14,h,j==0?col:'#d9c9a8',INK)+R(338+i*17,y+30-h+4,14,5,'#fff',' opacity=".5"')}}
  b+=sign(370,38,66,14,'PAINT','#2f6a9a','#fff',9);
  /* escadas de alumínio encostadas */
  b+=P('268,60 276,60 244,176 234,176','#b8bec6',INK)+P('290,60 298,60 276,176 266,176','#b8bec6',INK)+[0,1,2,3,4,5,6].map(function(k){var t=k/7;return L(272-t*38+6,66+k*15,292-t*22,66+k*15,'#8a929a',3)}).join('');
  /* rolos de corda / fios e baldes */
  b+=E(176,166,18,6,'#caa24a',INK)+R(158,150,36,16,'#caa24a',INK)+L(158,156,194,156,'#8a6a2a',1)+L(158,162,194,162,'#8a6a2a',1)+RR(204,140,16,26,2,'#e8c860',INK)+RR(224,148,14,18,2,'#c9302c',INK);
  b+=D('M18 200h46l-5 34h-36z','#e08a3f',INK)+E(41,200,23,5,'#c9702f',INK)+S('M20 198q21-24 42 0','#555',2)+D('M72 206h38l-4 28h-30z','#2f6a9a',INK)+E(91,206,19,4,'#2a5a8a',INK)+R(416,210,50,26,'#b98a52',INK)+R(416,210,50,5,'#d9aa6a')+T(441,229,'NAILS',9,'#6a4a2a',{a:'middle',w:700,f:SANS});
  return WRAP(u,d,b)};
/* ---------- TINTURARIA ---------- */
RS.drycleaner=function(u){var d,b='',i,r=rng(21);
  d=base(u,'#eef0f0','#d6dcdc',170,['#cfd4d4','#a6adad'],'#fff');
  b+=R(0,0,480,170,'url(#'+u+'-w)')+tile(170,'#d6dada','#bcc2c2',30)+skirt(170,'#8a9494')+R(0,0,480,170,'url(#'+u+'-lt)');
  b+=sign(136,12,208,30,'DRY CLEANERS','#1f5f8f','#fff',18)+T(240,56,'Same-day service · Wash & Fold',9,'#1f5f8f',{a:'middle',w:700,f:SANS});
  /* trilho de roupas em plásticos (esquerda e direita) */
  [[8,170],[320,160]].forEach(function(rl,ri){var x0=rl[0],w=rl[1];b+=L(x0,72,x0+w,72,'#8a929a',3)+L(x0,72,x0,170,'#8a929a',2)+L(x0+w,72,x0+w,170,'#8a929a',2);for(i=0;i<(ri?6:7);i++){var x=x0+14+i*(w-20)/(ri?6:7),c=['#2a3a5a','#8a4a3a','#e8e4da','#3a5a4a','#6a3a5a','#4a4a52','#c9b79a'][(i+ri*3)%7];b+=L(x,72,x,80,'#555',1)+S('M'+(x-8)+' 80q8-6 16 0','#9aa0aa',1.5)+D('M'+(x-12)+' 82l12-4l12 4l-2 8l-4-1v66h-12v-66l-4 1z',c,INK)+D('M'+(x-14)+' 80q14-6 28 0l4 90q-18 6-36 0z','#e8f4fa',' opacity=".42" stroke="#fff" stroke-opacity=".7" stroke-width=".8"')+L(x-8,90,x-7,150,'#fff',1.4,' opacity=".6"')}});
  /* prateleira com ferros e produtos */
  b+=R(180,74,120,5,'#9aa0aa',INK)+RR(188,60,26,14,3,'#cfd4dc',INK)+RR(220,56,18,18,2,'#e8c860',INK)+RR(244,60,14,14,2,'#2f8fb8',INK)+RR(264,56,18,18,2,'#fff',INK);
  /* balcão */
  b+=R(150,150,220,10,'#3a4650',INK)+R(150,160,220,48,'#5a6a78',INK)+R(158,168,204,34,'#4a5a68')+[0,1,2].map(function(k){return L(158+k*68,168,158+k*68,202,'#3a4650',1.4)}).join('')+RR(176,132,40,18,3,'#2a2f36',INK)+R(180,136,32,9,'#7fd0e0',' opacity=".85"')+C(300,142,8,'#e8c860',INK)+RR(316,138,28,12,2,'#fff',INK)+T(330,147,'TICKET',5,'#555',{a:'middle',w:700,f:SANS});
  /* cabides e sacos de lavanderia (direita-baixo) */
  b+=D('M420 214q8-8 24-6q12 4 14 20l-4 12h-36z','#e8e4da',INK)+S('M436 208q2-8 8-6','#8a929a',2)+T(438,236,'LAUNDRY',6,'#1f5f8f',{a:'middle',w:700,f:SANS})+RR(20,200,56,52,4,'#c9d4dc',INK)+C(48,226,16,'#e8f4fa',INK)+C(48,226,11,'#7fb0d0',' opacity=".6"')+R(26,206,44,4,'#8a929a');
  return WRAP(u,d,b)};
/* ---------- LAVA-RÁPIDO ---------- */
RS.carwash=function(u){var d,b='',i,r=rng(31);
  d=LG(u,'w',0,0,0,160,[[0,'#6fa0c0'],[1,'#c8dcea']])+LG(u,'f',0,160,0,270,[[0,'#8a8e92'],[1,'#5a5e62']])+RG(u,'lt',240,40,280,[[0,'#fff6d8',.5],[1,'#fff6d8',0]])+vig(u);
  b+=R(0,0,480,160,'url(#'+u+'-w)')+R(0,160,480,110,'url(#'+u+'-f)');
  /* prédio do túnel */
  b+=R(60,36,360,126,'#c8ccd0',INK)+R(60,36,360,10,'#8a929a',INK)+sign(150,12,180,26,'CAR WASH','#1f5f9f','#fff',18)+T(240,32,'',1,'#fff');
  b+=P('96,160 96,76 150,56 330,56 384,76 384,160','#2a2f36',INK)+P('112,160 112,84 156,66 324,66 368,84 368,160','#12161a')+RG(u,'x',240,120,120,[[0,'#7fd0e0',.5],[1,'#7fd0e0',0]]).replace(/^.*$/,'');
  /* escovas e luzes dentro do túnel */
  b+=R(150,78,6,80,'#e8503a',INK)+R(324,78,6,80,'#e8503a',INK)+[0,1,2,3,4,5].map(function(k){return R(158+k*28,70,18,4,'#e8c860',' opacity=".85"')}).join('')+E(240,120,70,34,'#7fd0e0',' opacity=".08"');
  /* semáforo + setas */
  b+=R(404,70,8,50,'#444',INK)+RR(398,40,20,34,4,'#222',INK)+C(408,50,5,'#c9302c')+C(408,64,5,'#4f4f4f')+sign(384,126,60,16,'WAIT','#c9302c','#fff',9);
  /* espuma (bolhas) */
  for(i=0;i<46;i++){var x=r()<.5?r()*100+4:380+r()*96,y=150+r()*80,rr=3+r()*8;b+=C(x,y,rr,'#fff',' opacity=".85" stroke="#9fc4dc" stroke-width=".6"')+C(x-rr*.3,y-rr*.3,rr*.28,'#fff',' opacity=".9"')}
  b+=E(40,168,52,14,'#fff',' opacity=".8"')+E(440,168,52,14,'#fff',' opacity=".8"')+[0,1,2,3,4,5,6].map(function(k){return C(14+k*14,160+(k%3)*3,9,'#fff',' opacity=".9" stroke="#9fc4dc" stroke-width=".6"')}).join('');
  /* esteira (trilhos) e poça */
  b+=P('150,266 190,172 290,172 330,266','#4a4e52',' opacity=".55"')+L(190,172,150,266,'#e8c860',2,' opacity=".6"')+L(290,172,330,266,'#e8c860',2,' opacity=".6"');
  /* mangueira + balde + cone + preços */
  b+=S('M30 262q-14-30 18-34q30-4 40-22','#2a2f36',5)+RR(86,196,12,10,2,'#e8c860',INK)+D('M426 236h26l4 22h-34z','#e08a3f',INK)+P('439,214 450,238 428,238','#e08a3f',INK)+R(430,226,18,4,'#fff')
  +R(20,60,34,52,'#fff',INK)+T(37,74,'WASH',8,'#1f5f9f',{a:'middle',w:700,f:SANS})+T(37,88,'$10',12,'#c9302c',{a:'middle',w:700,f:SANS})+T(37,104,'WAX $5',7,'#555',{a:'middle',w:700,f:SANS})+R(35,112,4,48,'#555');
  return WRAP(u,d,b)};
/* ---------- RUA COM CAIXA ELETRÔNICO ---------- */
RS.atmstreet=function(u){var d,b='',i,j,r=rng(33);
  d=LG(u,'w',0,0,0,170,[[0,'#d9b88a'],[1,'#b8946a']])+LG(u,'f',0,170,0,270,[[0,'#8e8a84'],[1,'#5e5a56']])+RG(u,'lt',130,40,280,[[0,'#ffe0a8',.5],[1,'#ffe0a8',0]])+vig(u);
  b+=R(0,0,480,170,'url(#'+u+'-w)')+R(0,170,480,100,'url(#'+u+'-f)');
  for(i=0;i<5;i++)for(j=0;j<12;j++)b+=R(j*40+(i%2)*20,176+i*18,38,16,'none',' stroke="#4a4642" stroke-width=".6" opacity=".4"');
  b+=R(0,170,480,6,'#aaa49a',INK);
  /* fachada do banco */
  b+=R(0,0,300,170,'#e8dcc4',INK)+R(0,0,300,14,'#7a5a3a',INK)+sign(70,20,160,28,'FIRST NATIONAL BANK','#1f3f6f','#e8c860',11)+[0,1,2,3,4,5].map(function(k){return R(8+k*50,56,6,114,'#f4ecda',INK)}).join('')+[0,1,2,3,4,5].map(function(k){return R(6+k*50,52,10,6,'#d8cca8',INK)}).join('');
  b+=R(18,68,100,84,'#1a2f4a',INK)+R(22,72,92,76,'#6a9ac0')+L(68,72,68,148,'#dfe6ec',2)+P('22,148 60,72 84,72 46,148','#fff',' opacity=".25"')+T(68,138,'OPEN',9,'#e8c860',{a:'middle',w:700,f:SANS});
  /* porta */
  b+=R(222,86,64,84,'#3a2a1a',INK)+R(228,92,52,78,'#6a9ac0')+L(254,92,254,170,'#dfe6ec',2)+RR(246,128,4,12,2,'#e8c860')+RR(258,128,4,12,2,'#e8c860');
  /* caixa eletrônico na parede */
  b+=RR(138,70,70,96,5,'#2a2f36',INK)+RR(146,78,54,34,3,'#0c2a3a',INK)+R(150,82,46,26,'#2f8fb8')+T(173,92,'ATM',9,'#fff',{a:'middle',w:700,f:SANS})+T(173,103,'WELCOME',5,'#cfe8f4',{a:'middle',f:SANS})+RR(146,118,54,22,2,'#555',INK)+[0,1,2,3].map(function(k){return [0,1,2].map(function(m){return RR(150+m*16,121+k*0,12,4,1,'#9aa0aa')}).join('')}).join('')+[0,1,2].map(function(m){return RR(150+m*16,128,12,4,1,'#9aa0aa')+RR(150+m*16,134,12,4,1,'#9aa0aa')}).join('')+RR(150,146,34,8,1,'#0c0c0c',INK)+R(152,149,30,2,'#e8c860')+RR(188,146,12,8,1,'#4f9a52')+sign(142,52,62,14,'24h CASH','#4f9a52','#fff',8);
  /* poste, lixeira, hidrante */
  b+=R(330,40,6,130,'#2a2f36',INK)+L(333,44,360,40,'#2a2f36',3)+E(366,42,14,5,'#444',INK)+E(366,50,28,18,'#ffe8b0',' opacity=".2"')+R(380,100,54,40,'#fff',INK)+T(407,122,'BUS',10,'#c9302c',{a:'middle',w:700,f:SANS})+R(404,140,6,30,'#555');
  b+=R(444,150,26,20,'#1f5f9f',INK)+T(457,164,'P',12,'#fff',{a:'middle',w:700,f:SANS})+RR(444,170,24,40,3,'#3a6a4a',INK)+R(442,168,28,6,'#2a4a34',INK)+RR(14,198,16,34,4,'#c9302c',INK)+R(16,192,12,8,'#8a1a1a',INK);
  b+=E(80,262,70,5,'#000',' opacity=".15"')+R(0,264,480,6,'#4a4642')+L(0,267,480,267,'#e8c860',1.4,' stroke-dasharray="14 10"');
  return WRAP(u,d,b)};
/* ---------- LOJA DE CELULARES ---------- */
RS.phonestore=function(u){var d,b='',i,j,r=rng(41);
  d=base(u,'#f4f6f8','#dfe4e8',172,['#e6e8ea','#b8bcc0'],'#ffffff');
  b+=R(0,0,480,172,'url(#'+u+'-w)')+tile(172,'#e6e8ea','#cfd2d6',34)+skirt(172,'#9aa0a6')+R(0,0,480,172,'url(#'+u+'-lt)');
  b+=R(0,0,480,12,'#2a2f36')+[50,170,290,410].map(function(x){return R(x,8,50,5,'#fff',' opacity=".9"')}).join('');
  b+=sign(150,18,180,28,'MOBILE WORLD','#1f1f24','#fff',16)+C(142,32,5,'#2f8fb8');
  /* parede de celulares (esquerda) */
  b+=R(10,56,150,114,'#1a1f26',INK);for(j=0;j<3;j++)for(i=0;i<6;i++){var x=18+i*24,y=62+j*34;b+=RR(x,y,16,28,3,'#0c0c10',INK)+R(x+1.5,y+3,13,20,['#2f8fb8','#e8503a','#4f9a52','#b05cc0','#e8c860','#7fd0e0'][(i+j*2)%6])}
  b+=R(10,158,150,12,'#444a52');
  /* vitrines/balcões de vidro */
  b+=R(330,100,146,70,'#cfd8e0',INK)+R(334,104,138,62,'#e8f2f8',' opacity=".8"')+[0,1,2,3,4].map(function(k){return RR(342+k*26,128,14,24,3,'#0c0c10',INK)+R(344+k*26,131,10,16,['#2f8fb8','#e8503a','#4f9a52','#b05cc0','#e8c860'][k])}).join('')+P('334,104 380,104 346,166 334,166','#fff',' opacity=".3"')+R(330,92,146,8,'#2a2f36',INK);
  /* tablets em mostruário */
  b+=R(332,56,140,30,'#2a2f36',INK)+[0,1,2].map(function(k){return RR(340+k*46,60,38,22,3,'#0c0c10',INK)+R(343+k*46,63,32,16,['#7fd0e0','#e8c860','#b05cc0'][k])}).join('');
  /* acessórios pendurados no centro-fundo */
  b+=R(184,60,112,100,'#fff',INK)+T(240,74,'ACCESSORIES',8,'#555',{a:'middle',w:700,f:SANS});
  for(j=0;j<3;j++)for(i=0;i<6;i++){var ax=192+i*17,ay=82+j*26;b+=L(ax+5,ay-2,ax+5,ay,'#999',1)+RR(ax,ay,10,18,1.5,['#2f8fb8','#e8503a','#222','#4f9a52','#e8c860','#b05cc0'][(i+j)%6],INK)+(j==2?S('M'+(ax+5)+' '+(ay+18)+'q-6 10 -2 14','#555',1.2):'')}
  /* carregador de balcão, cabos e caixas (esquerda-baixo) */
  b+=R(14,200,64,30,'#fff',INK)+RR(18,204,26,22,2,'#2f8fb8',INK)+T(31,218,'5G',9,'#fff',{a:'middle',w:700,f:SANS})+RR(48,206,26,20,2,'#e8503a',INK)+R(14,230,64,4,'#cfd2d6')+R(424,206,44,34,'#fff',INK)+sign(428,210,36,12,'SALE','#c9302c','#fff',8)+plant(450,258,.01);
  return WRAP(u,d,b)};
/* ---------- SHOPPING ---------- */
RS.mall=function(u){var d,b='',i,r=rng(51);
  d=LG(u,'w',0,0,0,168,[[0,'#f4ecda'],[1,'#e2d4b8']])+LG(u,'f',0,168,0,270,[[0,'#e6dcc6'],[1,'#c4b698']])+RG(u,'lt',240,10,300,[[0,'#fff6d8',.6],[1,'#fff6d8',0]])+vig(u);
  b+=R(0,0,480,168,'url(#'+u+'-w)')+tile(168,'#eae0ca','#d2c6a8',36)+R(0,168,480,102,'url(#'+u+'-f)',' opacity=".3"');
  /* claraboia */
  b+=P('60,0 420,0 380,18 100,18','#bcdcf0',INK)+[0,1,2,3,4,5,6,7].map(function(k){return L(60+k*45-k*5,0,100+k*35,18,'#8a929a',1.5)}).join('')+P('60,0 420,0 380,18 100,18','#fff',' opacity=".2"');
  /* lojas laterais */
  b+=R(0,24,150,144,'#d9c9a8',INK)+R(8,70,134,96,'#1a1f26',INK)+R(12,74,126,88,'#f4d9a0')+sign(10,34,130,26,'FASHION','#222','#e8c860',14)+[0,1,2].map(function(k){return D('M'+(28+k*38)+' 100l8-6l8 6l-3 8l-2-1v34h-6v-34l-2 1z',['#c9302c','#2f6a9a','#3a5a4a'][k],INK)+C(36+k*38,88,5,'#e8c4a0',INK)}).join('')+R(12,150,126,12,'#a8884a');
  b+=R(330,24,150,144,'#c9d4dc',INK)+R(338,70,134,96,'#1a1f26',INK)+R(342,74,126,88,'#e0f0f8')+sign(340,34,130,26,'BOOKS & COFFEE','#3a2418','#f4ead4',11)+[0,1,2,3].map(function(k){return R(350,82+k*18,110,3,'#8a6a4a')+[0,1,2,3,4,5,6].map(function(m){return R(352+m*15,70+k*18+0,10,12,['#c9302c','#2f6a9a','#4f9a52','#e8c860','#8a4a2a','#b05cc0','#222'][(m+k)%7],INK)}).join('')}).join('');
  /* placa centro-fundo (directory) */
  b+=sign(186,38,108,22,'FOOD COURT ↑','#2f7f5f','#fff',11)+L(206,24,206,38,'#555',1.2)+L(274,24,274,38,'#555',1.2)+R(186,66,108,70,'#c8d0d8',INK)+R(190,70,100,62,'#e8f0f4')+T(240,86,'STORE DIRECTORY',7,'#2a2f36',{a:'middle',w:700,f:SANS})+[0,1,2,3].map(function(k){return L(198,96+k*10,282,96+k*10,'#8a929a',1)+C(204,92+k*10,2,['#c9302c','#2f6a9a','#4f9a52','#e8c860'][k])}).join('');
  /* corrimão de vidro no 2º andar */
  b+=R(150,138,180,4,'#2a2f36',INK)+R(150,142,180,26,'#bcdcf0',' opacity=".4" stroke="#8a929a" stroke-width=".8"')+[0,1,2,3,4,5,6,7].map(function(k){return R(150+k*25,138,4,30,'#8a929a',INK)}).join('')+R(150,166,180,6,'#a8a090',INK);
  /* plantas grandes e bancos */
  b+=plant(30,212,1.4)+plant(450,212,1.4)+RR(70,228,76,10,3,'#8a5a34',INK)+R(76,238,6,18,'#3a2418')+R(134,238,6,18,'#3a2418')+RR(70,214,76,6,3,'#a8703f',INK)+RR(340,228,76,10,3,'#8a5a34',INK)+R(346,238,6,18,'#3a2418')+R(404,238,6,18,'#3a2418')+RR(340,214,76,6,3,'#a8703f',INK);
  b+=RR(166,244,148,3,1.5,'#fff',' opacity=".0"');
  return WRAP(u,d,b)};
/* ---------- LOJA DE ROUPAS ---------- */
RS.clothesstore=function(u){var d,b='',i,r=rng(61);
  d=base(u,'#efe6dc','#d9cab8',170,['#a8825a','#6d4e30'],'#ffe8c0');
  b+=R(0,0,480,170,'url(#'+u+'-w)')+planks(170,'#a8825a','#5a3e24',5)+R(0,0,480,170,'url(#'+u+'-lt)')+skirt(170,'#3a2418');
  b+=lamps([100,380],14,'#222')+sign(160,14,160,26,'BOUTIQUE','#222','#e8c860',16);
  /* araras com roupas (esquerda e direita) */
  [[8,150],[326,148]].forEach(function(rl,ri){var x0=rl[0],w=rl[1];b+=L(x0+6,84,x0+w-6,84,'#caa24a',3)+L(x0+10,84,x0+10,170,'#caa24a',3)+L(x0+w-10,84,x0+w-10,170,'#caa24a',3)+E(x0+10,172,10,3,'#caa24a')+E(x0+w-10,172,10,3,'#caa24a');for(i=0;i<9;i++){var x=x0+20+i*(w-40)/8,c=['#c9302c','#2f4a8a','#e8e4da','#3a6a4a','#8a4a8a','#222','#e8c860','#7a4a2a','#4a8a9a'][(i+ri*4)%9];b+=S('M'+x+' 84q0-6 4-6','#555',1.4)+D('M'+(x-8)+' 88l8-5l8 5l4 8l-5 3l-2-4v50q-5 3-10 0v-50l-2 4l-5-3z',c,INK)+L(x-2,98,x-2,138,'#fff',.8,' opacity=".25"')}});
  /* prateleira de dobrados */
  b+=R(166,104,148,5,'#8a6a44',INK)+[0,1,2,3,4].map(function(k){return R(172+k*28,92,24,12,['#2f4a8a','#e8e4da','#c9302c','#3a6a4a','#e8c860'][k],INK)+R(172+k*28,84,24,8,['#e8e4da','#2f4a8a','#e8c860','#c9302c','#222'][k],INK)}).join('')+R(166,134,148,5,'#8a6a44',INK)+[0,1,2,3,4].map(function(k){return R(172+k*28,122,24,12,['#8a4a8a','#222','#4a8a9a','#e8e4da','#7a4a2a'][k],INK)+R(172+k*28,114,24,8,['#222','#e8c860','#e8e4da','#8a4a8a','#3a6a4a'][k],INK)}).join('');
  /* provador com cortina */
  b+=R(204,150,72,20,'#5a3e24',INK).replace(/.*/,'');
  b+=R(196,40,0,0,'none');
  b+=R(150,140,0,0,'none');
  /* espelho de pé e provador (fundo-centro alto) */
  b+=R(196,34,88,2,'#222')+sign(206,40,68,16,'FITTING ROOM','#3a2418','#f4ead4',8)+R(204,58,72,0,'none');
  /* manequins */
  [[120,'#c9302c'],[360,'#2f4a8a']].forEach(function(m){var x=m[0];b+=D('M'+(x-16)+' 110q16-10 32 0l4 34q-20 6-40 0z',m[1],INK)+R(x-3,100,6,12,'#e8d9bd',INK)+E(x,96,6,8,'#e8d9bd',INK)+R(x-1.5,144,3,28,'#444')+E(x,172,14,3,'#444')});
  /* caixa/balcão */
  b+=R(420,206,52,34,'#3a2418',INK)+R(416,202,60,6,'#c9b79a',INK)+RR(430,186,24,16,2,'#2a2f36',INK)+R(433,189,18,8,'#7fd0e0')+sign(24,206,52,14,'SALE 50%','#c9302c','#fff',8)+D('M24 220h52l-3 30h-46z','#e8c860',INK)+[0,1,2].map(function(k){return D('M'+(34+k*14)+' 226l3-4l3 4v14h-6z',['#c9302c','#2f4a8a','#222'][k],INK)}).join('');
  return WRAP(u,d,b)};
/* ---------- LOJA DE SAPATOS ---------- */
RS.shoestore=function(u){var d,b='',i,j,r=rng(71);
  d=base(u,'#e9e0d2','#cdbfa8',170,['#b89a72','#7a5e3c'],'#ffe8c0');
  b+=R(0,0,480,170,'url(#'+u+'-w)')+planks(170,'#b89a72','#5a4228',8)+R(0,0,480,170,'url(#'+u+'-lt)')+skirt(170,'#3a2418');
  b+=lamps([120,360],14,'#222')+sign(150,14,180,26,'SHOE STORE','#7a2a1a','#f4ead4',16);
  /* prateleiras de sapatos esquerda e direita */
  [[8,170],[302,170]].forEach(function(sh,si){var x0=sh[0],w=sh[1];b+=R(x0,50,w,120,'#6b4a34',INK)+R(x0+4,54,w-8,112,'#3a2418');for(j=0;j<4;j++){var y=58+j*28;b+=R(x0+4,y+22,w-8,4,'#c9b79a',INK);for(i=0;i<4;i++){var x=x0+12+i*(w-20)/4,c=['#222','#8a4a2a','#c9302c','#e8e4da','#2f4a8a','#caa24a','#4a2a1a','#3a6a4a'][(i*2+j+si*3)%8];b+=D('M'+x+' '+(y+22)+'v-10q8-4 12 2l4 4q12 0 14 4v4z',c,INK)+L(x,y+22,x+30,y+22,'#111',1.4)+R(x+1,y+14,5,6,'#fff',' opacity=".2"')}}});
  /* espelho baixo e banquinho medidor */
  b+=R(196,70,88,76,'#c8dcda',INK)+R(200,74,80,68,'#e8f2f0')+P('200,142 232,74 252,74 220,142','#fff',' opacity=".4"')+R(186,146,108,6,'#6b4a34',INK);
  b+=sign(206,50,68,14,'NEW ARRIVALS','#222','#e8c860',7);
  /* bancos de provar (cantos) e caixas */
  b+=RR(20,206,70,18,5,'#7a2a1a',INK)+R(30,224,6,26,'#3a2418')+R(76,224,6,26,'#3a2418')+RR(392,206,70,18,5,'#2f4a8a',INK)+R(402,224,6,26,'#3a2418')+R(448,224,6,26,'#3a2418');
  b+=R(30,184,30,20,'#d9b87a',INK)+R(30,184,30,5,'#c99a5a')+R(36,172,30,20,'#e8e4da',INK)+R(36,172,30,5,'#c9302c')+D('M402 204v-10q8-4 12 2l4 4q12 0 14 4v4z','#c9302c',INK)+R(450,196,0,0,'none');
  /* medidor Brannock no chão (direita) */
  b+=D('M400 254h56l-4 8h-52z','#8a929a',INK)+L(410,256,410,262,'#222',1)+L(422,256,422,262,'#222',1)+L(434,256,434,262,'#222',1);
  return WRAP(u,d,b)};
/* ---------- SALÃO DE CABELEIREIRO ---------- */
RS.hairsalon=function(u){var d,b='',i,j,r=rng(81);
  d=base(u,'#f0e0e4','#d8b8c4',170,['#2a2a30','#16161a'],'#fff0f4');
  b+=R(0,0,480,170,'url(#'+u+'-w)')+tile(170,'#2c2c32','#18181c',30)+skirt(170,'#222');
  b+=R(0,0,480,170,'url(#'+u+'-lt)')+sign(150,10,180,26,'HAIR STUDIO','#222','#e8c8d0',16);
  /* três espelhos com moldura e lâmpadas */
  [[24],[176],[328]].forEach(function(m){var x=m[0];b+=RR(x,44,128,96,6,'#c8a24a',INK)+RR(x+6,50,116,84,4,'#dff0f6',INK)+P((x+6)+',134 '+(x+50)+',50 '+(x+74)+',50 '+(x+30)+',134','#fff',' opacity=".5"')+P((x+80)+',134 '+(x+104)+',50 '+(x+114)+',50 '+(x+90)+',134','#fff',' opacity=".25"');for(i=0;i<8;i++)b+=C(x+10+i*15,44,3,'#fff6c0',INK)+C(x+10+i*15,44,7,'#ffe8a0',' opacity=".25"')});
  /* bancadas com produtos */
  [[24],[176],[328]].forEach(function(m,k){var x=m[0];b+=R(x,138,128,6,'#e8e4da',INK)+R(x+4,144,120,26,'#3a3a42',INK)+RR(x+10,118,10,20,3,['#c9302c','#2f8fb8','#e8c860'][k],INK)+RR(x+26,122,8,16,2,'#fff',INK)+D('M'+(x+44)+' 138l4-20h6l4 20z','#b05cc0',INK)+R(x+70,128,24,10,'#111',INK)+L(x+72,128,x+94,120,'#222',2)+L(x+100,138,x+112,116,'#9aa0aa',2)+L(x+104,138,x+116,116,'#9aa0aa',2)});
  /* cadeiras de salão (extremos) */
  [[22,208],[420,208]].forEach(function(c){var x=c[0],y=c[1];b+=E(x+20,y+50,30,6,'#000',' opacity=".3"')+R(x+16,y+30,8,18,'#9aa0aa',INK)+E(x+20,y+50,22,5,'#555',INK)+RR(x-6,y+12,52,20,8,'#c9302c',INK)+D('M'+(x-4)+' '+(y+14)+'q-4-40 6-48q22-6 38 0q8 8 4 48z','#b02a26',INK)+RR(x-12,y+4,10,16,3,'#222',INK)+RR(x+42,y+4,10,16,3,'#222',INK)+RR(x+8,y+36,24,5,2,'#9aa0aa',INK)});
  /* secadores de capacete (centro-alto, parede dir/centro) */
  b+=L(150,10,150,26,'#555',2).replace(/.*/,'');
  [[98],[382]].forEach(function(h){var x=h[0];b+=R(x-2,18,4,30,'#9aa0aa',INK)});
  /* carrinho de produtos e lavatório */
  b+=RR(84,196,34,44,3,'#e8e4da',INK)+R(84,206,34,3,'#9aa0aa')+RR(90,184,8,14,2,'#2f8fb8',INK)+RR(102,186,8,12,2,'#c9302c',INK)+E(101,244,16,3,'#555')+C(90,248,3,'#222')+C(112,248,3,'#222')+R(344,198,0,0,'none');
  b+=D('M370 226q14-14 32 0v10q-16 8-32 0z','#e8e4da',INK)+R(384,196,4,30,'#9aa0aa')+S('M386 196q10-10 20 0','#9aa0aa',3)+[0,1,2].map(function(k){return L(126+k*5,200,126+k*5,214,'#555',1)}).join('');
  return WRAP(u,d,b)};
})();
