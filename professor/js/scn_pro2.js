/* Cenários extras para as aulas Quest (lavanderia, bike, aeroporto, bagagem, prédio, quarto, jantar, posto, garagem, sala de aula).
   Mesma API de scn_pro.js. Centro-baixo livre para os personagens. */
(function(){
if(!window.SF||!window.RS)return;
var SF=window.SF,RS=window.RS,rng=SF.rng,LG=SF.LG,RG=SF.RG,R=SF.R,RR=SF.RR,E=SF.E,C=SF.C,L=SF.L,P=SF.P,D=SF.D,S=SF.S,G=SF.G,INK=SF.INK,WRAP=SF.WRAP,vig=SF.vig,T=SF.T;
var SANS='Trebuchet MS,Arial,sans-serif';
function tx(x,y,s,sz,c,a){return T(x,y,'',sz,c||'#fff',{a:a||'middle',w:700,f:SANS}).replace('></text>','>'+s+'</text>')}
function tile(y0,a,b,sz){var s='',i,j;for(j=0;y0+j*sz*.5<270;j++)for(i=0;i<480/sz+1;i++)s+=R(i*sz,y0+j*sz*.5,sz,sz*.5,(i+j)%2?a:b);return s}
function planks(y0,c1,c2,seed){var r=rng(seed),b=R(0,y0,480,270-y0,c1),i;for(i=0;i<14;i++)b+=L(0,y0+i*(270-y0)/14,480,y0+i*(270-y0)/14+(r()-.5)*2,c2,.8,' opacity=".35"');for(i=0;i<20;i++){var x=r()*480,y=y0+r()*(270-y0);b+=L(x,y,x+(r()-.5)*40,y+2,c2,.6,' opacity=".25"')}return b}
function sign(x,y,w,s,bg,fg){return RR(x,y,w,16,3,bg,INK)+tx(x+w/2,y+12,s,10,fg)}
function lampc(x,y,w,col){return R(x,y,w,6,col||'#fff',INK)+R(x-4,y+6,w+8,3,'#fff',' opacity=".45"')}
function suitcase(x,y,w,h,c,h2){return RR(x,y,w,h,4,c,INK)+R(x+w*.3,y-4,w*.4,4,'#222')+L(x+w*.3,y+3,x+w*.3,y+h-3,h2||'#000',1,' opacity=".3"')+L(x+w*.7,y+3,x+w*.7,y+h-3,h2||'#000',1,' opacity=".3"')+C(x+5,y+h+2,2.2,'#222')+C(x+w-5,y+h+2,2.2,'#222')}
function plant(x,y,s){return D('M'+(x-8*s)+' '+y+'l2-14h12l2 14z','#a8643a',INK)+[-1,0,1].map(function(k){return D('M'+x+' '+(y-14*s)+'q'+(k*14*s)+' '+(-22*s)+' '+(k*18*s)+' '+(-30*s)+'q-4 16 '+(-k*2)+' 30z','#3f8a4a',INK)}).join('')}

/* ---------- LAVANDERIA ---------- */
RS.laundry=function(u){var d='',b='',i,k;
  d+=LG(u,'w',0,0,0,170,[[0,'#cfe0e0'],[1,'#a8c4c4']])+RG(u,'lt',240,40,300,[[0,'#fff',.5],[1,'#fff',0]])+vig(u);
  b+=R(0,0,480,170,'url(#'+u+'-w)')+tile(170,'#e4e6e2','#c3c8c4',30)+R(0,0,480,170,'url(#'+u+'-lt)');
  for(i=0;i<16;i++)b+=L(i*30,0,i*30,120,'#fff',.8,' opacity=".25"');
  b+=R(0,0,480,14,'#e9eef0')+[50,190,330].map(function(x){return lampc(x,6,70)}).join('');
  b+=sign(168,22,144,'SELF-SERVICE LAUNDRY','#1f6f9a','#fff');
  /* fileira de máquinas esquerda e direita */
  function mach(x,y,col){var s=RR(x,y,64,92,4,'#eef1f3',INK)+R(x,y,64,14,'#c9d0d6',INK)+RR(x+6,y+3,22,8,2,'#2a2f36')+C(x+50,y+7,2.5,'#e8503a')+C(x+57,y+7,2.5,'#4f9a52')+C(x+32,y+53,24,'#9aa0aa',INK)+C(x+32,y+53,19,'#2a3a52',INK)+C(x+32,y+53,15,col,' opacity=".55"')+P((x+20)+','+(y+44)+' '+(x+30)+','+(y+40)+' '+(x+24)+','+(y+52),'#fff',' opacity=".3"')+R(x+4,y+84,56,4,'#9aa0aa');return s}
  [[8,'#7fb8d8'],[78,'#e8a07a'],[348,'#a8c8e8'],[418,'#c8a0d8']].forEach(function(m,j){b+=mach(m[0],80,m[1])+(j==0||j==2?'':'')});
  /* secadoras empilhadas ao fundo */
  b+=[0,1].map(function(k){return RR(152+k*0,50+k*0,0,0,0,'none')}).join('');
  [[150,'#e0e4e8'],[266,'#e0e4e8']].forEach(function(m){var x=m[0];b+=RR(x,44,64,60,4,m[1],INK)+C(x+32,76,19,'#9aa0aa',INK)+C(x+32,76,14,'#2a3a52')+RR(x+6,48,22,6,2,'#2a2f36')+RR(x,108,0,0,0,'none')});
  /* bancada de dobrar + cestos */
  b+=R(150,112,180,7,'#c9965a',INK)+R(154,119,6,44,'#7a5a3a')+R(320,119,6,44,'#7a5a3a')+RR(176,100,36,12,2,'#e8503a',INK)+RR(214,102,30,10,2,'#f4ead4',INK)+RR(250,98,40,14,2,'#2f8fb8',INK)+L(250,103,290,103,'#fff',1,' opacity=".4"');
  b+=D('M12 224h54l-5 30h-44z','#e8a43a',INK)+[0,1,2,3].map(function(k){return L(20+k*11,228,20+k*11,250,'#b87a1a',1)}).join('')+D('M16 224q10-14 22-6q10-8 20 4z','#fff',INK)+D('M414 224h54l-5 30h-44z','#4f9a52',INK)+D('M418 224q14-12 26-4q8-6 18 4z','#7fb8d8',INK);
  /* placas e relógio de parede, máquina de moedas, varal */
  b+=C(100,38,13,'#fff',INK)+L(100,38,100,29,INK,1.4)+L(100,38,107,40,INK,1.4)+RR(386,34,60,28,3,'#fff',INK)+tx(416,46,'COINS ONLY',7,'#1f6f9a')+tx(416,57,'$2.50 / WASH',7,'#c0392b')+L(20,24,150,28,'#888',1)+D('M40 25l12 0l-2 18h-8z','#e8503a',INK)+D('M84 26l12 0l-2 16h-8z','#f4c430',INK);
  b+=RR(72,170,0,0,0,'none');
  return WRAP(u,d,b)};

/* ---------- LOCAÇÃO DE BICICLETAS ---------- */
RS.bikeshop=function(u){var d='',b='',i;
  d+=LG(u,'w',0,0,0,170,[[0,'#3c5a58'],[1,'#5d7a6e']])+RG(u,'lt',240,50,300,[[0,'#ffe0a0',.5],[1,'#ffe0a0',0]])+vig(u);
  b+=R(0,0,480,170,'url(#'+u+'-w)')+R(0,170,480,100,'#8c8478',INK)+[0,1,2,3,4].map(function(k){return L(0,180+k*18,480,180+k*18,'#6c665a',1,' opacity=".6"')}).join('')+R(0,0,480,170,'url(#'+u+'-lt)');
  for(i=0;i<24;i++)b+=R(i*20,0,1.5,100,'#000',' opacity=".08"');
  function bike(x,y,col,s){s=s||1;var w1=C(x,y,20*s,'none',' stroke="#222" stroke-width="3"')+C(x+56*s,y,20*s,'none',' stroke="#222" stroke-width="3"')+C(x,y,3,'#999')+C(x+56*s,y,3,'#999');
    return w1+S('M'+x+' '+y+'L'+(x+22*s)+' '+(y-26*s)+'L'+(x+50*s)+' '+(y-26*s)+'L'+(x+56*s)+' '+y+'M'+(x+22*s)+' '+(y-26*s)+'L'+(x+26*s)+' '+y+'L'+(x+50*s)+' '+(y-26*s),col,3.2)+S('M'+(x+50*s)+' '+(y-26*s)+'L'+(x+46*s)+' '+(y-36*s)+'M'+(x+40*s)+' '+(y-36*s)+'h12',  '#222',2.6)+S('M'+(x+22*s)+' '+(y-26*s)+'L'+(x+20*s)+' '+(y-34*s)+'M'+(x+14*s)+' '+(y-34*s)+'h12','#222',2.6)+C(x+26*s,y,5,'none',' stroke="#555" stroke-width="2"')}
  /* parede de capacetes */
  b+=R(14,40,150,70,'#2e3e3c',INK);[0,1,2].forEach(function(k){b+=R(18,66+k*0,0,0,0,'none')});
  [['#e8503a',0,0],['#2f8fb8',1,0],['#f4c430',2,0],['#4f9a52',3,0],['#fff',0,1],['#b05cc0',1,1],['#222',2,1],['#e8503a',3,1]].forEach(function(h){var x=26+h[1]*34,y=52+h[2]*28;b+=D('M'+x+' '+(y+16)+'q0-18 14-18q14 0 14 18z',h[0],INK)+L(x+4,y+8,x+24,y+8,'#fff',1,' opacity=".5"')+R(x+2,y+16,24,2,'#222')});
  b+=L(14,82,164,82,'#7a8a86',2);
  b+=sign(20,14,138,'HELMETS · $3 / DAY','#c0392b','#fff');
  /* balcão de locação + letreiro */
  b+=R(300,100,166,12,'#c9965a',INK)+R(300,112,166,58,'#4a3a2a',INK)+[0,1,2].map(function(k){return R(308+k*54,118,46,46,'#5a4634',INK)}).join('')+RR(338,60,100,22,4,'#1f4f5a',INK)+tx(388,76,'BIKE RENTAL',14,'#ffe9a8')+RR(344,86,88,12,2,'#f4ead4',INK)+tx(388,95,'$12 / hour',9,'#2a2a2a')+RR(310,86,22,14,2,'#f4ead4',INK)+tx(321,96,'MAP',7,'#3a2a1a')+R(440,74,20,26,'#f4ead4',INK)+L(444,80,456,80,'#aaa',1)+L(444,86,456,86,'#aaa',1)+L(444,92,456,92,'#aaa',1);
  /* rack de bikes ao fundo */
  b+=R(176,120,120,4,'#444',INK)+bike(184,116,'#e8503a',.9)+bike(238,116,'#2f8fb8',.85);
  /* bikes à frente nas laterais */
  b+=E(60,258,56,6,'#000',' opacity=".2"')+bike(20,240,'#4f9a52')+E(430,258,44,6,'#000',' opacity=".2"')+C(430,0,0,'none')+bike(388,240,'#f4c430',.9);
  b+=RR(176,22,128,18,3,'#fff',INK)+tx(240,35,'RENT · RIDE · RETURN',10,'#1f4f5a')+plant(180,172,.9);
  return WRAP(u,d,b)};

/* ---------- SEGURANÇA DO AEROPORTO ---------- */
RS.airportsecurity=function(u){var d='',b='',i;
  d+=LG(u,'w',0,0,0,170,[[0,'#d8dde4'],[1,'#b8c0cc']])+RG(u,'lt',240,30,320,[[0,'#fff',.55],[1,'#fff',0]])+vig(u);
  b+=R(0,0,480,170,'url(#'+u+'-w)')+tile(170,'#c8cdd2','#aeb5bc',40)+R(0,0,480,170,'url(#'+u+'-lt)');
  b+=R(0,0,480,16,'#aab2bc')+[40,170,300,420].map(function(x){return R(x,6,50,6,'#fff',INK)}).join('');
  b+=RR(120,22,240,34,4,'#1f3a5a',INK)+tx(240,45,'SECURITY CHECK',20,'#fff')+RR(128,60,100,16,3,'#f4c430',INK)+tx(178,72,'LAPTOPS OUT',9,'#222')+RR(236,60,116,16,3,'#e8503a',INK)+tx(294,72,'NO LIQUIDS > 100ml',8,'#fff');
  /* janelas vidro ao fundo */
  b+=R(10,30,100,100,'#9ec5dc',INK)+L(60,30,60,130,'#fff',2,' opacity=".6"')+P('10,30 50,30 10,90','#fff',' opacity=".3"')+R(370,30,100,100,'#9ec5dc',INK)+L(420,30,420,130,'#fff',2,' opacity=".6"');
  b+=D('M300 112l36-22l22 6l-36 22z','#fff',' opacity=".6"')+D('M40 108l34-12l12 4l-24 14z','#fff',' opacity=".6"');
  /* esteira raio-X (direita) */
  b+=RR(318,112,150,56,5,'#2f3a46',INK)+R(318,112,150,10,'#46545f')+RR(340,86,106,34,6,'#3c4a58',INK)+RR(350,92,86,22,3,'#0e1418',INK)+R(354,96,78,14,'#2a6a58',' opacity=".8"')+RR(372,98,32,8,2,'#e8c850',' opacity=".8"')+D('M296 150h24v20h-24z','#9aa0aa',INK)+R(312,142,60,8,'#1c2229',INK)+[0,1,2,3,4,5].map(function(k){return L(318+k*8,146,318+k*8,150,'#555',1)}).join('')+RR(304,128,34,12,2,'#d8d8d8',INK)+RR(420,130,32,14,2,'#2f8fb8',INK)+tx(394,164,'X-RAY',9,'#fff');
  b+=RR(392,148,56,8,2,'#6a7480',INK);
  /* bandejas */
  [[250,100],[256,92]].forEach(function(t){b+=RR(t[0],t[1]+20,0,0,0,'none')});
  [[246,138,'#d4d9de'],[246,134,'#c4cad0'],[246,130,'#d4d9de']].forEach(function(t){b+=RR(t[0],t[1],56,8,2,t[2],INK)});
  b+=RR(286,122,22,6,2,'#222')+C(270,126,4,'#4a4a4a',INK)+RR(256,118,20,12,2,'#7a5236',INK);
  b+=RR(18,150,60,12,2,'#d4d9de',INK)+RR(18,138,60,12,2,'#c4cad0',INK)+RR(22,128,50,10,2,'#2a3a52',INK)+R(30,124,0,0,'none');
  /* pórtico detector de metais */
  b+=R(110,92,12,80,'#e6e9ec',INK)+R(214,92,12,80,'#e6e9ec',INK)+R(106,86,124,10,'#e6e9ec',INK)+C(168,91,3,'#4f9a52')+C(180,91,3,'#e8503a');
  /* cordões de fila */
  [[90,'#c0392b'],[330,'#c0392b']].forEach(function(p){});
  [24,66,108].forEach(function(x){b+=R(x-2,176,4,30,'#555')+E(x,208,7,2.5,'#333',INK)+C(x,176,3,'#c9a84a')});
  b+=S('M24 180q21 8 42 0','#c0392b',3)+S('M66 180q21 8 42 0','#c0392b',3)+RR(14,150,0,0,0,'none');
  [440,396].forEach(function(x){b+=R(x-2,206,4,30,'#555')+E(x,238,7,2.5,'#333',INK)+C(x,206,3,'#c9a84a')});
  b+=S('M396 210q22 8 44 0','#c0392b',3)+sign(392,176,60,'LINE →','#222','#f4c430');
  return WRAP(u,d,b)};

/* ---------- ESTEIRA DE BAGAGEM ---------- */
RS.baggageclaim=function(u){var d='',b='',i;
  d+=LG(u,'w',0,0,0,170,[[0,'#cdd3da'],[1,'#a9b2bc']])+RG(u,'lt',240,30,320,[[0,'#fff',.5],[1,'#fff',0]])+vig(u);
  b+=R(0,0,480,170,'url(#'+u+'-w)')+tile(170,'#c2c6ca','#a8adb3',40)+R(0,0,480,170,'url(#'+u+'-lt)');
  b+=R(0,0,480,14,'#9aa4b0')+[60,200,340].map(function(x){return R(x,5,60,5,'#fff',INK)}).join('');
  b+=RR(170,18,140,36,4,'#1f3a5a',INK)+tx(240,36,'BAGGAGE CLAIM',16,'#fff')+RR(204,40,72,12,2,'#f4c430',INK)+tx(240,50,'CAROUSEL 3',9,'#222');
  b+=RR(20,22,110,40,3,'#16202a',INK)+tx(75,36,'ARRIVALS',9,'#f4c430')+tx(75,48,'AA 214  NEW YORK',7,'#7fe0a0')+tx(75,58,'BA 078  LONDON',7,'#7fe0a0');
  b+=RR(350,22,110,40,3,'#16202a',INK)+tx(405,36,'FLIGHT  BELT',9,'#f4c430')+tx(405,48,'AA 214 → 3',7,'#7fe0a0')+tx(405,58,'LH 456 → 4',7,'#7fe0a0');
  /* abertura da esteira ao fundo */
  b+=R(150,70,180,50,'#2a3038',INK)+[0,1,2,3,4,5,6].map(function(k){return R(154+k*25,70,22,50,'#3a424c')}).join('')+R(150,64,180,8,'#c0392b',INK);
  b+=suitcase(176,96,34,24,'#2f8fb8')+suitcase(262,92,40,28,'#7a2f2f');
  /* carrossel oval (laterais com malas) */
  b+=D('M0 150q0-22 70-24h340q70 2 70 24v16q0 22-70 24h-340q-70-2-70-24z','#7a838e',INK)+D('M14 152q0-16 56-18h340q56 2 56 18v10q0 16-56 18h-340q-56-2-56-18z','#2a2f36',INK);
  for(i=0;i<22;i++)b+=L(30+i*20,134,30+i*20,180,'#1a1e24',2,' opacity=".6"');
  b+=suitcase(24,126,36,26,'#c0392b')+suitcase(78,116,30,22,'#4f9a52')+RR(112,118,34,22,3,'#222',INK)+suitcase(390,120,34,26,'#f4c430')+suitcase(432,114,32,28,'#5a3a8a')+R(350,128,26,18,'#9a6a3a',INK)+L(350,137,376,137,'#6a4a2a',1.6)+L(363,128,363,146,'#6a4a2a',1.6);
  b+=R(0,190,480,3,'#f4c430',' opacity=".55"')+D('M0 192h480v6h-480z','#000',' opacity=".08"');
  /* carrinhos de bagagem */
  b+=S('M20 214h50l-6 30h-38z','#8a929c',2)+R(8,206,0,0,'none')+S('M20 214l-10-22','#8a929c',3)+C(32,252,4,'#222')+C(60,252,4,'#222')+[28,40,52].map(function(x){return L(x,216,x-2,242,'#8a929c',1)}).join('')+suitcase(30,200,22,14,'#2f8fb8');
  b+=S('M416 214h50l-6 30h-38z','#8a929c',2)+S('M466 214l10-22','#8a929c',3)+C(430,252,4,'#222')+C(456,252,4,'#222')+RR(432,198,26,16,3,'#e8503a',INK)+plant(110,208,.9);
  return WRAP(u,d,b)};

/* ---------- CORREDOR DE APARTAMENTO ---------- */
RS.apartmenthall=function(u){var d='',b='',i;
  d+=LG(u,'w',0,0,0,170,[[0,'#d8cdb8'],[1,'#b8a888']])+RG(u,'lt',240,40,300,[[0,'#ffe8b0',.55],[1,'#ffe8b0',0]])+vig(u);
  b+=R(0,0,480,170,'url(#'+u+'-w)')+planks(170,'#7a5236','#3e2614',9)+R(0,0,480,170,'url(#'+u+'-lt)');
  b+=R(0,120,480,50,'#8a6a4a')+R(0,118,480,4,'#c9a870')+[0,1,2,3,4,5,6,7,8,9,10,11].map(function(k){return R(k*40+4,126,32,38,'none',' stroke="#6a4a30" stroke-width="1.2"')}).join('');
  function door(x,n,col){return R(x,40,56,100,'#5a3a24',INK)+R(x+5,46,46,92,col,INK)+R(x+10,54,15,28,'none',' stroke="#00000044" stroke-width="1.4"')+R(x+31,54,15,28,'none',' stroke="#00000044" stroke-width="1.4"')+R(x+10,90,36,40,'none',' stroke="#00000044" stroke-width="1.4"')+C(x+44,94,3,'#e8c860',INK)+RR(x+17,26,22,13,2,'#e8c860',INK)+tx(x+28,37,n,10,'#3a2a10')+C(x+28,68,3,'#222')+C(x+28,68,1.3,'#9aa')}
  door(30,'2A','#3f6a8a')+'';b+=door(30,'2A','#3f6a8a')+door(118,'2B','#8a3f3f');
  b+=door(300,'3A','#3f7a58')+door(390,'3B','#7a5a8a');
  /* centro: porta no fundo + tapete */
  b+=R(188,56,104,84,'#4a2e1c',INK)+R(194,62,92,78,'#6a4630')+tx(240,52,'→',10,'#e8c860')+RR(200,20,80,20,3,'#1f3a5a',INK)+tx(240,34,'STAIRS · EXIT',10,'#fff');
  b+=P('196,140 284,140 300,172 180,172','#6a2f2f',' opacity=".55"');
  /* caixas de correio (parede esquerda) */
  b+=RR(14,150,0,0,0,'none');
  /* arandelas */
  [[96,70],[276,70]].forEach(function(p){b+=D('M'+p[0]+' 66h10l-2 14h-6z','#e8c860',INK)+C(p[0]+5,72,16,'#ffe3a0',' opacity=".25"')});
  b+=D('M170 70h10l-2 14h-6z','#e8c860',INK)+C(175,76,16,'#ffe3a0',' opacity=".22"')+D('M368 70h10l-2 14h-6z','#e8c860',INK)+C(373,76,16,'#ffe3a0',' opacity=".22"');
  /* bloco de caixas de correio à direita baixo */
  b+=RR(380,160,90,64,3,'#8a929c',INK)+tx(425,156,'MAILBOXES',8,'#3a2a10');
  for(i=0;i<8;i++){var mx=386+(i%4)*21,my=166+Math.floor(i/4)*26;b+=RR(mx,my,18,22,2,'#b8c0c8',INK)+R(mx+3,my+4,12,3,'#222')+RR(mx+4,my+12,10,6,1,'#fff')+tx(mx+9,my+17.5,(i+1)+'',5,'#222')}
  b+=RR(10,170,56,56,3,'#8a929c',INK)+[0,1,2,3].map(function(i){return RR(16+(i%2)*24,178+Math.floor(i/2)*24,20,20,2,'#b8c0c8',INK)+R(19+(i%2)*24,184+Math.floor(i/2)*24,14,3,'#222')}).join('')+tx(38,166,'MAIL',8,'#3a2a10')+plant(112,246,1)+D('M72 228h10v16h-10z','#c9965a',INK);
  return WRAP(u,d,b)};

/* ---------- QUARTO DE CRIANÇA/ESTUDO ---------- */
RS.kidsroom=function(u){var d='',b='',i;
  d+=LG(u,'w',0,0,0,170,[[0,'#8fa8c4'],[1,'#b0c0d4']])+RG(u,'lt',240,60,300,[[0,'#ffe8b8',.5],[1,'#ffe8b8',0]])+vig(u);
  b+=R(0,0,480,170,'url(#'+u+'-w)')+planks(170,'#b8885a','#7a5230',11)+R(0,0,480,170,'url(#'+u+'-lt)');
  b+=R(0,160,480,10,'#f4efe4',INK);
  /* janela */
  b+=R(180,30,100,76,'#2a3a52',INK)+R(184,34,92,68,'#8fc4e4')+P('184,34 230,34 184,84','#fff',' opacity=".3"')+L(230,34,230,102,'#f4ead4',3)+L(184,68,276,68,'#f4ead4',3)+D('M170 28h120v8h-120z','#fff',INK)+D('M170 30q8 40 2 80h-6q4-40-2-80z','#c9553d')+D('M290 30q-8 40 -2 80h6q-4-40 2-80z','#c9553d')+C(250,52,6,'#fff',' opacity=".7"');
  /* cama (esquerda) */
  b+=R(10,108,130,56,'#8a5a34',INK)+R(10,98,10,66,'#6a4224',INK)+RR(18,100,118,26,6,'#fff',INK)+RR(20,118,118,38,4,'#3f7a9a',INK)+L(20,132,138,132,'#2e5a74',1.4)+RR(22,102,42,20,6,'#f4ead4',INK)+RR(100,116,30,34,4,'#e8a43a',INK)+C(116,130,5,'#fff',' opacity=".5"');
  b+=R(14,164,6,10,'#6a4224')+R(130,164,6,10,'#6a4224');
  /* prateleira na parede + livros + globo */
  b+=R(300,60,160,6,'#8a5a34',INK)+R(300,110,160,6,'#8a5a34',INK);
  [[306,'#c0392b',30],[314,'#2f8fb8',34],[322,'#f4c430',28],[330,'#4f9a52',32],[338,'#7a3f8a',30]].forEach(function(k){b+=R(k[0],60-k[2],7,k[2],k[1],INK)});
  b+=C(380,44,14,'#4a90c0',INK)+S('M366 44q14 6 28 0','#4f9a52',2)+R(378,58,4,2,'#555')+RR(410,42,40,18,2,'#f4ead4',INK)+RR(412,30,0,0,0,'none');
  b+=[0,1,2,3,4].map(function(k){return R(308+k*8,110-24-k%2*4,7,24+k%2*4,['#e8503a','#2f8fb8','#4f9a52','#f4c430','#b05cc0'][k],INK)}).join('')+D('M360 110v-22h26v22z','#f4ead4',INK)+RR(398,94,44,16,2,'#e8a43a',INK)+C(430,100,0,'none');
  /* mesa de estudo (direita) */
  b+=R(318,134,142,8,'#c9965a',INK)+R(324,142,6,52,'#7a5a3a')+R(450,142,6,52,'#7a5a3a')+RR(336,142,70,34,2,'#a87a4a',INK)+R(340,148,62,10,'#8a5a34')+R(340,162,62,10,'#8a5a34')+C(371,153,2,'#e8c860')+C(371,167,2,'#e8c860');
  b+=RR(346,128,32,6,1,'#fff',INK)+RR(346,122,32,6,1,'#2f8fb8',INK)+R(420,100,0,0,'none')+D('M424 134l8-34l14-4l-4 6l-10 32z','#3a3d48',INK)+D('M414 92h30l-6 12h-18z','#e8c860',INK)+C(432,108,22,'#ffe9a8',' opacity=".25"');
  b+=RR(392,126,22,8,1,'#c0392b',INK)+R(440,124,2,12,'#2f8fb8')+R(444,122,2,14,'#e8503a')+R(448,125,2,11,'#f4c430');
  b+=E(80,268,70,0,'none')+D('M150 232q90 12 180 0l16 22q-106 14 -212 0z','#7a5a8a',INK)+D('M164 234q76 8 152 0','none',' stroke="#a888b8" stroke-width="1.4"')+RR(60,30,50,36,2,'#c9965a',INK)+R(64,34,42,28,'#f4c8a0')+P('64,62 80,46 96,60 106,52 106,62','#4f9a52')+C(94,42,4,'#ffd860');
  return WRAP(u,d,b)};

/* ---------- SALA DE JANTAR ---------- */
RS.diningroom=function(u){var d='',b='',i;
  d+=LG(u,'w',0,0,0,170,[[0,'#7a3a34'],[1,'#a05a48']])+RG(u,'lt',240,70,280,[[0,'#ffd8a0',.6],[1,'#ffd8a0',0]])+vig(u);
  b+=R(0,0,480,170,'url(#'+u+'-w)')+planks(170,'#8a5a34','#4a2e18',14)+R(0,0,480,170,'url(#'+u+'-lt)');
  b+=R(0,114,480,56,'#5a3a24')+R(0,112,480,4,'#c9965a')+[0,1,2,3,4,5,6,7,8,9,10,11].map(function(k){return R(k*40+4,122,32,42,'none',' stroke="#7a5236" stroke-width="1.4"')}).join('');
  /* lustre */
  b+=L(240,0,240,20,'#222',1.4)+D('M214 28h52l-8 12h-36z','#e8c860',INK)+[-22,-11,0,11,22].map(function(x){return C(240+x,36+Math.abs(x)*.15,3,'#fff3c0')}).join('')+C(240,36,50,'#ffe3a0',' opacity=".2"');
  /* aparador esquerdo com quadro */
  b+=R(14,110,120,50,'#3a2418',INK)+R(14,106,120,6,'#5a3a24',INK)+R(52,116,0,0,'none')+RR(22,118,46,36,2,'#4a2e1c',INK)+RR(78,118,46,36,2,'#4a2e1c',INK)+C(66,136,2,'#e8c860')+C(80,136,2,'#e8c860')+RR(28,34,92,56,2,'#c9965a',INK)+R(33,39,82,46,'#a8c0a0')+P('33,85 60,56 82,76 100,60 115,85','#5f7a58')+C(98,52,6,'#f6e6a0')+D('M92 106q-6-14 0-22q6 8 0 22z','#2f8fb8',INK)+RR(100,92,12,14,2,'#e8503a',INK)+C(48,100,0,'none')+D('M48 106q0-14 8-14q8 0 8 14z','#cfd4dc',INK);
  /* vitrine/armário direito */
  b+=R(346,40,118,120,'#4a2e1c',INK)+R(352,46,106,108,'#2c1c12')+[0,1,2].map(function(k){var y=52+k*34;return R(352,y+30,106,4,'#8a5a34')+[0,1,2,3,4].map(function(j){return E(364+j*20,y+22,7,4,'#e8eef4',INK)+(k==1?D('M'+(360+j*20)+' '+(y+24)+'l2-14h10l2 14z','#cfe4f0',' opacity=".8"'):'')}).join('')}).join('')+L(405,46,405,154,'#c9965a',1.4)+RR(398,96,3,14,1,'#e8c860')+RR(410,96,3,14,1,'#e8c860');
  /* mesa posta ao fundo (centro-alto, personagens à frente) */
  b+=E(240,168,100,8,'#000',' opacity=".18"')+D('M130 128h220l14 24h-248z','#f4efe4',INK)+R(124,152,232,8,'#8a5a34',INK)+R(140,160,8,26,'#6a4224')+R(332,160,8,26,'#6a4224');
  b+=D('M130 128h220','none',' stroke="#c0392b" stroke-width="1.4"');
  [[160,'#e8503a'],[210,'#fff'],[270,'#fff'],[320,'#e8503a']].forEach(function(p,k){var x=p[0];b+=E(x,142,18,5,'#fff',INK)+E(x,141,11,3,'#e8eef4')+L(x-24,138,x-24,146,'#aaa',1.4)+L(x+24,138,x+24,146,'#aaa',1.4)+D('M'+(x+16)+' 130q-2 -12 0 -12q8 0 8 6q0 6 -8 6z','#cfe4f0',' opacity=".8"')});
  b+=D('M222 126q18-18 36 0z','#c9965a',INK)+E(240,128,26,5,'#a8763a',INK)+D('M232 122q8-12 16 0','#f4c430',INK)+RR(184,116,10,14,2,'#7a2f2f',INK)+D('M188 112l2 4','none',INK)+R(290,114,3,16,'#f4ead4',INK)+C(291.5,112,2.5,'#ffb040')+C(291.5,112,10,'#ffd878',' opacity=".3"')+R(176,116,3,14,'#f4ead4',INK)+C(177.5,114,2.5,'#ffb040');
  b+=plant(450,250,1.1);
  return WRAP(u,d,b)};

/* ---------- POSTO DE GASOLINA ---------- */
RS.gasstation=function(u){var d='',b='',i;
  d+=LG(u,'sk',0,0,0,140,[[0,'#6aa8d8'],[1,'#d8ecf4']])+LG(u,'rd',0,150,0,270,[[0,'#6a6e74'],[1,'#44484e']])+RG(u,'lt',380,20,240,[[0,'#fff3c0',.6],[1,'#fff3c0',0]])+vig(u);
  b+=R(0,0,480,150,'url(#'+u+'-sk)')+[[60,30],[300,20]].map(function(p){return E(p[0],p[1],34,7,'#fff',' opacity=".8"')+E(p[0]+14,p[1]-6,20,7,'#fff',' opacity=".8"')}).join('');
  b+=P('0,138 70,108 140,126 220,100 300,122 400,104 480,120 480,150 0,150','#7a9a8a',' opacity=".6"');
  b+=R(0,150,480,120,'url(#'+u+'-rd)')+R(0,148,480,6,'#aaa',INK);
  [[40,198],[130,206],[360,196],[440,204]].forEach(function(p){b+=L(p[0],p[1],p[0]+40,p[1],'#f4c430',2,' opacity=".6"')});
  /* loja de conveniência (direita) */
  b+=R(340,76,140,76,'#e8e2d2',INK)+R(340,70,140,10,'#c0392b',INK)+R(350,92,60,44,'#9ec5dc',INK)+L(380,92,380,136,'#fff',1.4)+P('350,92 376,92 350,120','#fff',' opacity=".3"')+R(420,92,44,60,'#3a424c',INK)+R(424,96,36,52,'#9ec5dc')+tx(380,86,'MINI MART',9,'#222')+RR(352,138,0,0,0,'none')+RR(352,104,0,0,0,'none');
  b+=RR(352,100,0,0,0,'none')+R(356,126,50,8,'#e8a43a',' opacity=".6"')+R(356,112,0,0,0,'none');
  /* cobertura com placa */
  b+=R(40,28,300,16,'#e8e2d2',INK)+R(40,44,300,5,'#c0392b',INK)+R(40,49,300,3,'#f4c430',INK)+R(60,52,12,98,'#cfd4dc',INK)+R(308,52,12,98,'#cfd4dc',INK)+RR(110,14,160,24,4,'#1f3a5a',INK)+tx(190,32,'GAS STATION',16,'#ffd860')+[110,170,230,290].map(function(x){return C(x,50,0,'none')}).join('')+[100,160,220,280].map(function(x){return R(x,50,22,2,'#fff',' opacity=".8"')}).join('');
  /* pedestal de preços */
  b+=R(12,40,10,116,'#555',INK)+RR(2,20,70,66,4,'#1f3a5a',INK)+tx(37,34,'GAS',10,'#ffd860')+[['REG','3.49','#4f9a52'],['PLUS','3.79','#f4c430'],['DIESEL','3.99','#e8503a']].map(function(p,k){return RR(6,40+k*14,62,12,2,'#10161c')+tx(18,50+k*14,p[0],6,p[2])+tx(52,50+k*14,'$'+p[1],8,'#7fe0a0')}).join('');
  /* bombas */
  function pump(x,col){return E(x+22,154,30,4,'#000',' opacity=".25"')+RR(x,92,44,62,4,'#e8e8ea',INK)+R(x,92,44,10,col,INK)+RR(x+6,106,32,18,2,'#10161c',INK)+tx(x+22,119,'12.80',10,'#7fe0a0')+RR(x+6,128,14,12,2,col,INK)+RR(x+24,128,14,12,2,'#555',INK)+R(x+4,144,36,8,'#555',INK)+S('M'+(x+44)+' 108q16 6 14 30','#222',3)+R(x+54,136,8,16,'#333',INK)}
  b+=pump(104,'#e8503a')+pump(206,'#2f8fb8');
  b+=D('M286 150l8-18h18l8 18z','#e8503a',INK)+RR(290,140,0,0,0,'none')+RR(300,136,12,14,2,'#f4c430',INK)+tx(306,147,'OIL',5,'#222');
  b+=R(250,150,2,0,'none')+[40,84].map(function(x){return D('M'+x+' 150l4-18h12l4 18z','#f4c430',INK)}).join('');
  return WRAP(u,d,b)};

/* ---------- ESTACIONAMENTO / GARAGEM ---------- */
RS.parking=function(u){var d='',b='',i;
  d+=LG(u,'w',0,0,0,170,[[0,'#6a6e76'],[1,'#8a8e94']])+RG(u,'lt',240,30,320,[[0,'#fff6d0',.35],[1,'#fff6d0',0]])+vig(u);
  b+=R(0,0,480,170,'url(#'+u+'-w)')+R(0,170,480,100,'#4a4d54')+R(0,0,480,170,'url(#'+u+'-lt)');
  b+=R(0,0,480,22,'#4a4e56')+[70,200,330,430].map(function(x){return R(x,22,60,5,'#fff',INK)+C(x+30,30,28,'#fff6d0',' opacity=".12"')}).join('');
  [0,1,2,3,4].forEach(function(k){b+=R(k*100+12,22,14,100,'#7a7e86',INK)});
  b+=RR(172,34,136,26,4,'#1f3a5a',INK)+tx(240,53,'PARKING · LEVEL 2',13,'#fff')+RR(20,34,70,22,3,'#f4c430',INK)+tx(55,50,'EXIT →',11,'#222')+RR(390,34,70,22,3,'#2f8fb8',INK)+tx(425,50,'P  LEVEL 2',9,'#fff');
  /* vagas numeradas no chão: linhas em perspectiva */
  for(i=0;i<=7;i++){var x0=20+i*60,x1=-40+i*80;b+=L(x0,176,x1,270,'#f4f0e0',2.4,' opacity=".85"')}
  [['A1',50],['A2',110],['A3',170],['A4',230],['A5',290],['A6',350],['A7',410]].forEach(function(s,k){b+=tx(40+k*60,190+0,s[0],10,'#f4f0e0')});
  b+=R(0,172,480,3,'#f4f0e0',' opacity=".7"');
  /* carros de fundo nas vagas das laterais (traseira) */
  function car(x,y,col){return E(x+30,y+34,34,4,'#000',' opacity=".3"')+RR(x,y,60,32,8,col,INK)+RR(x+8,y-12,44,16,6,col,INK)+R(x+12,y-9,36,11,'#2a3a52')+RR(x+3,y+18,10,6,2,'#c0392b')+RR(x+47,y+18,10,6,2,'#c0392b')+R(x+22,y+22,16,6,'#f4efe4')+R(x+4,y+30,10,5,'#222')+R(x+46,y+30,10,5,'#222')}
  b+=car(14,130,'#2f8fb8')+car(90,132,'#b8bcc4')+car(344,130,'#8a2f2f');
  b+=R(0,118,0,0,0,'none');
  /* máquina de pagamento */
  b+=R(448,150,10,44,'#555',INK)+RR(426,100,54,64,4,'#f4c430',INK)+tx(453,112,'PAY',9,'#222')+RR(432,116,42,18,2,'#10161c',INK)+tx(453,129,'$4.00',9,'#7fe0a0')+RR(432,138,18,10,1,'#555')+RR(454,138,18,10,1,'#555')+R(434,152,38,3,'#222')+tx(453,176,'TICKET',6,'#222');
  b+=R(448,164,12,6,'#666');
  /* cone e extintor + placas de bloco */
  b+=D('M18 250l6-26l6 26z','#e86a1a',INK)+R(15,250,18,4,'#222')+R(20,236,8,3,'#fff')+R(130,196,0,0,0,'none')+RR(60,214,28,36,2,'#c0392b',INK)+tx(74,230,'FIRE',6,'#fff')+RR(70,236,8,10,1,'#222');
  b+=R(0,160,0,0,0,'none')+RR(22,66,0,0,0,'none');
  return WRAP(u,d,b)};

/* ---------- SALA DE AULA ---------- */
RS.classroom=function(u){var d='',b='',i;
  d+=LG(u,'w',0,0,0,170,[[0,'#d8d0b4'],[1,'#c0b690']])+RG(u,'lt',240,40,320,[[0,'#fff6d0',.5],[1,'#fff6d0',0]])+vig(u);
  b+=R(0,0,480,170,'url(#'+u+'-w)')+planks(170,'#b8885a','#7a5230',21)+R(0,0,480,170,'url(#'+u+'-lt)')+R(0,160,480,10,'#8a6a4a',INK);
  /* quadro verde */
  b+=RR(104,28,206,92,3,'#7a5a3a',INK)+R(110,34,194,80,'#2f5a48')+P('110,34 170,34 110,70','#fff',' opacity=".08"')+tx(150,56,'Today:',12,'#f4f0e0')+tx(206,76,'Present Simple',12,'#f4f0e0')+L(120,90,230,90,'#f4f0e0',1.4,' opacity=".6"')+tx(160,104,'I am · you are',9,'#d8e8d0')+C(278,100,0,'none')+R(120,108,60,3,'#f4f0e0',' opacity=".4"')+R(114,114,194,3,'#8a6a4a')+R(130,112,16,4,'#fff')+R(150,112,10,4,'#e8c860')+RR(272,108,24,6,1,'#c9a878');
  b+=tx(250,50,'A  B  C',10,'#f4c430');
  /* mapa-múndi na parede direita */
  b+=RR(334,34,136,86,2,'#8a6a4a',INK)+R(338,38,128,78,'#8fc4e4')+D('M350 56q10-10 24-6q6 10-4 20q-10 6-18 0z','#7aa85a')+D('M360 82q10-4 14 8q-2 14-10 18q-8-8-4-26z','#7aa85a')+D('M392 52q18-8 38 2q10 10-2 16q-14-2-20 10q-12-2-16-12z','#8ab868')+D('M408 82q14 0 18 10q-6 10-16 8q-8-8-2-18z','#7aa85a')+D('M440 96q10-2 14 4q-6 6-14 4z','#7aa85a')+tx(380,129,'WORLD MAP',6,'#fff')+L(338,77,466,77,'#fff',.8,' opacity=".4"')+L(402,38,402,116,'#fff',.8,' opacity=".4"');
  /* janela esquerda */
  b+=R(16,34,76,82,'#2a3a52',INK)+R(20,38,68,74,'#a8d4ec')+L(54,38,54,112,'#f4ead4',3)+L(20,75,88,75,'#f4ead4',3)+P('20,38 50,38 20,66','#fff',' opacity=".3"');
  /* relógio e alfabeto */
  b+=C(207,16,10,'#fff',INK)+L(207,16,207,9,INK,1.4)+L(207,16,212,18,INK,1.4);
  ['A','B','C','D','E','F','G'].forEach(function(c,k){b+=RR(20+k*26+(k>3?242:0),128,0,0,0,'none')});
  /* mesa do professor (direita) e globo */
  b+=R(350,150,100,6,'#c9965a',INK)+R(356,156,6,34,'#7a5a3a')+R(438,156,6,34,'#7a5a3a')+RR(364,138,30,12,1,'#2f8fb8',INK)+RR(366,130,26,8,1,'#c0392b',INK)+C(424,132,13,'#4a90c0',INK)+D('M414 130q8-6 14 2q-2 8-10 6z','#7aa85a')+R(422,144,4,6,'#555');
  /* carteiras laterais (esquerda e direita baixo) */
  function desk(x,y){return R(x+4,y+14,3,34,'#6a6e76')+R(x+36,y+14,3,34,'#6a6e76')+D('M'+x+' '+(y+14)+'h44l4-12h-44z','#c9965a',INK)+R(x,y+14,44,4,'#a8763a',INK)+RR(x+8,y+28,28,4,1,'#8a929c')+R(x+14,y+36,16,3,'#6a6e76')+RR(x+8,y+4,12,3,1,'#fff')}
  b+=desk(14,172)+desk(66,176)+desk(380,172)+desk(430,176)+desk(14,222)+desk(430,226);
  b+=RR(14,150,58,16,2,'#fff',INK)+tx(43,162,'Be quiet!',8,'#c0392b')+RR(150,130,0,0,0,'none');
  return WRAP(u,d,b)};
})();
