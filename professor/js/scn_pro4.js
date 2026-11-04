/* Cenários Quest 4 (cinema, show, beisebol, camping, trilha, drive-thru, festa, casamento, boliche, minigolfe, elevador).
   Mesma identidade de scn_pro.js (SF helpers, 480×270, pintura quente, vinheta). Sem pessoas. */
(function(){
if(!window.SF||!window.RS)return;
var SF=window.SF,RS=window.RS,rng=SF.rng,LG=SF.LG,RG=SF.RG,R=SF.R,RR=SF.RR,E=SF.E,C=SF.C,L=SF.L,P=SF.P,D=SF.D,S=SF.S,G=SF.G,INK=SF.INK,WRAP=SF.WRAP,vig=SF.vig,T=SF.T;
var SANS='Trebuchet MS,Arial,sans-serif';
function tx(x,y,s,sz,fill,a,w){return T(x,y,'',sz,fill,{a:a||'middle',w:w||700,f:SANS}).replace('></text>','>'+s+'</text>')}
function planks(y0,c1,c2,seed){var r=rng(seed),b=R(0,y0,480,270-y0,c1),i;for(i=0;i<14;i++)b+=L(0,y0+i*(270-y0)/14,480,y0+i*(270-y0)/14+(r()-.5)*2,c2,.8,' opacity=".35"');for(i=0;i<20;i++){var x=r()*480,y=y0+r()*(270-y0);b+=L(x,y,x+(r()-.5)*40,y+2,c2,.6,' opacity=".25"')}return b}
function tree(x,y,h,c1,c2){return R(x-3,y-h*.35,6,h*.35,'#4a3020')+C(x,y-h*.55,h*.3,c1)+C(x-h*.15,y-h*.4,h*.22,c2)+C(x+h*.17,y-h*.45,h*.2,c2)}
function pine(x,y,h,c){return R(x-2,y-8,4,8,'#4a3020')+P((x-h*.28)+','+(y-8)+' '+(x+h*.28)+','+(y-8)+' '+x+','+(y-h),c)+P((x-h*.22)+','+(y-h*.4)+' '+(x+h*.22)+','+(y-h*.4)+' '+x+','+(y-h),'#fff',' opacity=".06"')}
function stars(r,n,y1){var s='',i;for(i=0;i<n;i++)s+=C(r()*480,r()*y1,.5+r()*.7,'#fff',' opacity="'+(.3+r()*.5).toFixed(2)+'"');return s}

/* ---------- CINEMA ---------- */
RS.cinema=function(u){var r=rng(71),d='',b='',i;
  d+=LG(u,'w',0,0,0,180,[[0,'#2a0f1c'],[1,'#5a2234']])+RG(u,'lt',240,20,300,[[0,'#ffcf80',.4],[1,'#ffcf80',0]])+vig(u);
  b+=R(0,0,480,180,'url(#'+u+'-w)')+R(0,176,480,94,'#3a1520')+R(0,0,480,180,'url(#'+u+'-lt)');
  /* carpete com padrão */
  for(i=0;i<30;i++)b+=P((i*18-40)+',270 '+(i*18-20)+',270 '+(i*18+10)+',180 '+(i*18+4)+',180',i%2?'#6b1f2e':'#4a1422',' opacity=".55"');
  b+=R(0,176,480,5,'#c9965a',INK);
  /* marquise de lâmpadas */
  b+=R(0,0,480,22,'#1c0a12')+Array.apply(null,{length:40}).map(function(_,k){return C(6+k*12,11,2.6,k%2?'#ffe08a':'#fff4c8')+C(6+k*12,11,6,'#ffd070',' opacity=".18"')}).join('');
  b+=RR(170,26,140,26,4,'#12080c',INK)+tx(240,46,'CINEMA',20,'#ff5a4a',null,900)+S('M172 28h136','#ffcf70',1);
  /* cartazes com moldura iluminada */
  [[16,'#2a4a7a','#e8a43a','NOW SHOWING'],[96,'#7a2a2a','#f4d890','COMING SOON'],[336,'#2a5a4a','#f4c430','NEW RELEASE'],[416,'#4a2a6a','#e8503a','MIDNIGHT']].forEach(function(p,k){var x=p[0];b+=R(x-3,62,62,94,'#c9965a',INK)+R(x,65,56,88,p[1])+RG(u,'p'+k,x+28,100,40,[[0,p[2],.7],[1,p[2],0]])+R(x,65,56,88,'url(#'+u+'-p'+k+')')+P((x+8)+',150 '+(x+28)+',100 '+(x+48)+',150','#12080c',' opacity=".55"')+C(x+28,92,9,'#12080c',' opacity=".5"')+tx(x+28,78,p[3].split(' ')[0],7,p[2])+tx(x+28,86,p[3].split(' ')[1],5,'#fff')+R(x+6,142,44,5,'#fff',' opacity=".5"')+L(x+28,156,x+28,162,'#ffe08a',1)});
  /* bilheteria */
  b+=R(150,64,180,90,'#1c0e14',INK)+R(158,86,164,50,'#e8d4a8',INK)+R(158,86,164,50,'#ffe9b0',' opacity=".25"')+L(240,86,240,136,'#8a6a4a',2)+RR(172,128,40,5,2,'#3a2418')+RR(268,128,40,5,2,'#3a2418')+R(150,136,180,18,'#3a2418',INK)+tx(240,80,'TICKETS',10,'#ffd070',null,900)+[0,1].map(function(k){return RR(172+k*96,92,64,22,2,'#12080c',INK)+tx(204+k*96,107,k?'SHOW TIMES':'BOX OFFICE',6,'#7fd0e0')}).join('');
  /* banner da pipoca (esquerda) */
  b+=RR(14,176,70,76,4,'#8a1a22',INK)+R(14,192,70,4,'#fff',' opacity=".8"')+tx(49,186,'POPCORN',8,'#fff')+D('M20 196h58l-6 52h-46z','#fff',INK)+[0,1,2,3,4].map(function(k){return R(26+k*11,196,5,52,'#d8323a',' opacity=".85"')}).join('')+[0,1,2,3,4,5,6,7].map(function(k){return C(26+k*7,192-(k%3)*3,5,k%2?'#fff4c8':'#f6dc8a',INK)}).join('')+tx(49,244,'LARGE',7,'#8a1a22');
  /* máquina de pipoca (direita) */
  b+=R(398,214,64,38,'#a8301f',INK)+R(402,150,56,64,'#fff4d8',' opacity=".35"'+INK)+R(398,144,64,8,'#ffcf40',INK)+R(396,208,68,8,'#ffcf40',INK)+Array.apply(null,{length:16}).map(function(){return C(406+r()*46,162+r()*44,5.5,r()>.5?'#fff4c8':'#f6dc8a',INK)}).join('')+tx(430,236,'FRESH',8,'#fff')+C(430,138,7,'#ffe08a',' opacity=".4"');
  b+=RR(364,196,26,56,3,'#12080c',INK)+R(368,202,18,12,'#7fd0e0',' opacity=".6"')+tx(377,230,'SODA',6,'#fff')+tx(377,240,'$5',7,'#ffd070');
  /* corda de veludo */
  [112,364].forEach(function(x){b+=R(x-2,224,4,28,'#c9965a',INK)+C(x,222,4,'#c9965a',INK)+E(x,252,8,3,'#8a6a3a')});
  b+=S('M112 224q126 24 252 0','#8a1a22',3);
  return WRAP(u,d,b)};

/* ---------- SHOW / PALCO ---------- */
RS.concert=function(u){var r=rng(83),d='',b='',i;
  d+=LG(u,'w',0,0,0,170,[[0,'#0a0618'],[1,'#2a1448']])+RG(u,'lt',240,60,260,[[0,'#ff7ac8',.35],[1,'#ff7ac8',0]])+vig(u);
  b+=R(0,0,480,170,'url(#'+u+'-w)')+R(0,0,480,170,'url(#'+u+'-lt)');
  /* feixes de luz */
  [[60,'#ff4a8a',-30],[150,'#4ac8ff',-12],[330,'#ffd04a',14],[420,'#8a5aff',34]].forEach(function(l){b+=P(l[0]+',16 '+(l[0]+l[2]-22)+',200 '+(l[0]+l[2]+22)+',200',l[1],' opacity=".13"')});
  /* treliça de luz */
  b+=R(0,0,480,10,'#1a1a22',INK)+R(30,14,420,6,'#2a2a34',INK)+Array.apply(null,{length:35}).map(function(_,k){return L(30+k*12,14,42+k*12,20,'#555',.8)}).join('');
  [40,100,160,220,280,340,400].forEach(function(x,k){var c=['#ff4a8a','#4ac8ff','#ffd04a','#8a5aff','#ff7a3a','#4aff9a','#ff4a8a'][k];b+=RR(x-8,20,16,14,3,'#1a1a22',INK)+C(x,38,6,c)+C(x,38,14,c,' opacity=".28"')});
  /* painel LED */
  b+=R(150,48,180,70,'#06040e',INK)+R(154,52,172,62,'#2a1450')+RG(u,'led',240,84,90,[[0,'#ff5ab0',.8],[1,'#4a2aa0',.2]])+R(154,52,172,62,'url(#'+u+'-led)')+tx(240,92,'LIVE',24,'#fff',null,900)+tx(240,106,'WORLD TOUR',8,'#ffd04a');
  /* palco */
  b+=R(0,150,480,22,'#2a2230',INK)+R(0,172,480,6,'#12101a')+R(0,178,480,92,'#14101c');
  b+=R(0,150,480,3,'#ff7ac8',' opacity=".5"');
  /* caixas de som empilhadas */
  [[8,'L'],[408,'R']].forEach(function(s){var x=s[0];for(i=0;i<3;i++){b+=R(x,64+i*30,64,30,'#14141a',INK)+C(x+32,79+i*30,11,'#2a2a32',INK)+C(x+32,79+i*30,5,'#06060a')+C(x+14,69+i*30,3,'#2a2a32')+C(x+50,69+i*30,3,'#2a2a32')}b+=R(x,154,64,16,'#14141a',INK)+tx(x+32,166,'PA',7,'#888')});
  /* retorno de palco */
  [[96],[360]].forEach(function(m){b+=P(m[0]+',176 '+(m[0]+30)+',176 '+(m[0]+24)+',164 '+(m[0]+6)+',164','#1a1a22',INK)});
  /* bateria ao fundo */
  b+=R(210,128,60,22,'#2a2230',INK)+E(240,138,18,12,'#c0302a',INK)+E(240,138,18,3,'#fff',' opacity=".3"')+E(212,126,12,3,'#e8c860',INK)+E(268,124,12,3,'#e8c860',INK)+E(262,142,10,8,'#2a4a8a',INK)+E(218,142,10,8,'#2a4a8a',INK)+L(212,126,212,150,'#888',1)+L(268,124,268,150,'#888',1);
  /* mic stands e amps */
  b+=L(120,176,124,140,'#aaa',1.6)+E(124,138,3,4,'#222')+L(356,176,352,140,'#aaa',1.6)+E(352,138,3,4,'#222');
  b+=R(70,150,26,22,'#14141a',INK)+R(384,150,26,22,'#14141a',INK)+C(83,161,6,'#2a2a32')+C(397,161,6,'#2a2a32');
  /* plateia como luzes: pulseiras e celulares */
  for(i=0;i<34;i++){var x=r()*480,y=222+r()*44,col=['#ffd04a','#ff4a8a','#4ac8ff','#4aff9a','#fff'][Math.floor(r()*5)];if(x>130&&x<350&&y<248)continue;b+=C(x,y,3.2,col,' opacity=".85"')+C(x,y,8,col,' opacity=".16"')}
  for(i=0;i<8;i++){var px=20+i*62+r()*20;b+=RR(px,196+r()*10,5,8,1,'#cfeaff',' opacity=".8"')+C(px+2.5,200,9,'#cfeaff',' opacity=".12"')}
  b+=R(0,206,480,6,'#3a3a44',INK)+[0,1,2,3,4,5,6,7,8,9,10,11].map(function(k){return R(k*40+2,206,36,6,'#4a4a56',' opacity=".6"')}).join('');
  return WRAP(u,d,b)};

/* ---------- BEISEBOL ---------- */
RS.ballpark=function(u){var r=rng(97),d='',b='',i;
  d+=LG(u,'s',0,0,0,100,[[0,'#7fb8e0'],[1,'#f4e8c8']])+LG(u,'g',0,100,0,270,[[0,'#4f9a42'],[1,'#2f7a32']])+RG(u,'lt',380,20,260,[[0,'#fff4c0',.55],[1,'#fff4c0',0]])+vig(u);
  b+=R(0,0,480,110,'url(#'+u+'-s)')+R(0,0,480,110,'url(#'+u+'-lt)')+E(100,30,50,10,'#fff',' opacity=".6"')+E(330,50,60,9,'#fff',' opacity=".5"');
  /* arquibancada ao fundo */
  b+=P('0,102 0,56 480,56 480,102','#8a8f9a',INK)+[0,1,2,3].map(function(k){return R(0,62+k*10,480,8,k%2?'#6a707c':'#7a808c')}).join('')+Array.apply(null,{length:60}).map(function(_,k){var row=Math.floor(k/15);return R(4+(k%15)*32+row*6,60+row*10,6,3,['#e8503a','#f4c430','#2f8fb8','#fff'][(k+row)%4],' opacity=".55"')}).join('');
  b+=R(0,100,480,10,'#2a5a3a',INK)+Array.apply(null,{length:24}).map(function(_,k){return R(k*20+2,102,16,6,k%3?'#3a6a4a':'#e8c860',' opacity=".6"')}).join('');
  /* placar */
  b+=R(150,18,180,78,'#1f3a2a',INK)+R(154,22,172,70,'#2a4a38')+R(154,22,172,14,'#0e1a12')+tx(240,33,'HOME  vs  VISITORS',8,'#ffd04a')+[0,1].map(function(k){return tx(168,56+k*18,k?'VIS':'HOME',8,'#fff','start')+[0,1,2,3,4,5,6,7,8].map(function(n){return RR(200+n*14,46+k*18,11,13,1,'#06100a')+tx(205.5+n*14,56+k*18,String((n*3+k*2)%4),8,'#ffd04a')}).join('')}).join('')+R(184,92,6,22,'#555')+R(290,92,6,22,'#555');
  b+=RR(166,76,60,12,2,'#0e1a12')+tx(196,85,'BALL 2  STR 1',6,'#4aff7a')+RR(254,76,60,12,2,'#0e1a12')+tx(284,85,'OUT 1  INN 7',6,'#ff6a4a');
  /* refletores */
  [60,430].forEach(function(x){b+=R(x-2,40,4,66,'#555')+R(x-16,26,32,16,'#2a2e36',INK)+Array.apply(null,{length:8}).map(function(_,k){return C(x-12+(k%4)*8,30+Math.floor(k/4)*7,2.6,'#fff8d0')}).join('')+C(x,32,24,'#fff8d0',' opacity=".18"')});
  /* campo */
  for(i=0;i<8;i++)b+=P((i*60-40)+',270 '+(i*60+20)+',270 '+(i*60+20)+',110 '+(i*60-10)+',110',i%2?'#4a9a40':'#3f8a38',' opacity=".25"');
  b+=R(0,110,480,4,'#2a1a10',INK)+P('240,114 440,200 240,266 40,200','#b8845a',INK)+P('240,130 410,200 240,252 70,200','#3f8a38')+E(240,200,24,10,'#b8845a')+R(232,198,16,3,'#fff')+P('240,258 232,266 248,266','#fff',INK);
  b+=P('0,270 40,200 0,200','#fff',' opacity=".0"')+L(240,266,40,200,'#fff',1.8,' opacity=".85"')+L(240,266,440,200,'#fff',1.8,' opacity=".85"');
  [[240,134],[70,200],[410,200]].forEach(function(p){b+=P((p[0]-6)+','+p[1]+' '+p[0]+','+(p[1]-5)+' '+(p[0]+6)+','+p[1]+' '+p[0]+','+(p[1]+5),'#fff',INK)});
  /* banco de reservas (esquerda) e bola/bastões (direita) */
  b+=R(8,208,100,34,'#2a3a5a',INK)+R(8,200,100,10,'#c9965a',INK)+R(12,226,92,4,'#a8763a')+[0,1,2,3,4].map(function(k){return R(14+k*19,222,3,16,'#555')}).join('')+tx(58,238,'HOME',7,'#fff');
  b+=L(400,246,424,214,'#c9965a',4)+L(414,248,432,222,'#a8763a',4)+C(448,246,6,'#fff',INK)+S('M443 244q5 4 10 0','#d8323a',1)+RR(380,236,28,10,3,'#8a5a30',INK);
  return WRAP(u,d,b)};

/* ---------- ACAMPAMENTO ---------- */
RS.campsite=function(u){var r=rng(103),d='',b='',i;
  d+=LG(u,'s',0,0,0,150,[[0,'#2a3a6a'],[.5,'#c4627a'],[1,'#f4a860']])+LG(u,'g',0,170,0,270,[[0,'#3a5a2a'],[1,'#1f3a1c']])+RG(u,'fire',330,225,150,[[0,'#ff9a3a',.5],[1,'#ff9a3a',0]])+vig(u);
  b+=R(0,0,480,170,'url(#'+u+'-s)')+stars(r,24,70)+C(380,136,26,'#ffd890',' opacity=".5"')+C(380,136,14,'#fff0c0');
  b+=D('M0 150l60-44 50 30 70-56 70 50 60-34 80 52 90-40v60h-480z','#4a3a58')+D('M0 160l90-30 70 24 80-34 100 40 70-26 70 24v50h-480z','#3a2a48');
  /* árvores laterais */
  [[20,180,130],[64,186,100],[420,184,120],[462,186,100],[150,182,70],[330,182,60]].forEach(function(t){b+=pine(t[0],t[1],t[2],'#1f4a2a')+pine(t[0]+2,t[1]-6,t[2]*.8,'#2a5a30')});
  b+=R(0,170,480,100,'url(#'+u+'-g)')+Array.apply(null,{length:40}).map(function(){var x=r()*480,y=176+r()*90;return L(x,y,x+(r()-.5)*5,y-5,'#4f7a38',.8,' opacity=".6"')}).join('');
  /* barraca */
  b+=P('30,230 100,150 170,230','#e8803a',INK)+P('100,150 170,230 128,230','#c9602a')+P('100,150 100,230 62,230','#f0a060',' opacity=".5"')+P('84,230 100,180 116,230','#2a1a10',INK)+P('100,180 116,230 100,230','#4a2a18')+L(100,150,100,140,'#555',2)+L(30,232,12,246,'#c9b080',1)+L(170,232,190,246,'#c9b080',1)+C(12,246,2,'#555')+C(190,246,2,'#555');
  /* lanterna pendurada */
  b+=L(130,150,130,160,'#555',1)+RR(125,160,10,14,2,'#c9965a',INK)+C(130,167,14,'#ffd070',' opacity=".25"')+R(127,164,6,8,'#ffe9a0');
  /* fogueira */
  b+=E(330,238,36,10,'#12080a',' opacity=".5"')+[0,1,2,3,4,5,6,7].map(function(k){var a=k*.785;return C(330+Math.cos(a)*28,234+Math.sin(a)*8,5,k%2?'#6a6a72':'#8a8a92',INK)}).join('');
  b+=L(310,236,350,222,'#4a2a18',5)+L(350,236,310,222,'#5a3418',5)+L(318,238,342,238,'#3a2010',4);
  b+=D('M330 196q-14 18-12 30t12 6 12-8-12-28z','#e8503a')+D('M330 204q-8 14-6 22t6 4 7-8-7-18z','#ffa030')+D('M330 214q-4 8-3 12t3 2 4-4-4-10z','#ffe070')+C(330,214,34,'#ff8a2a',' opacity=".12"');
  for(i=0;i<8;i++)b+=C(322+r()*20,180+r()*34,.9,'#ffc060',' opacity=".8"');
  /* tronco-banco, mochila, lenha, panela */
  b+=RR(220,246,70,14,6,'#5a3a22',INK)+E(220,253,6,7,'#c9965a',INK)+E(290,253,6,7,'#c9965a',INK);
  b+=RR(420,214,36,40,10,'#3a6a8a',INK)+RR(426,232,24,16,4,'#2a5470',INK)+S('M424 218q14-12 28 0','#2a2a2a',2)+R(430,222,16,3,'#e8c860');
  b+=[0,1,2].map(function(k){return RR(380,236+k*7,34,6,3,'#7a4a2a',INK)+E(380,239+k*7,3,3,'#c9965a')}).join('')+RR(176,248,14,10,2,'#cfd4dc',INK)+L(176,250,168,246,'#777',1.4);
  b+=L(118,200,118,236,'#6a4a2a',2)+P('100,226 100,236 118,236','#fff',' opacity="0"');
  return WRAP(u,d,b)};

/* ---------- TRILHA ---------- */
RS.hiketrail=function(u){var r=rng(111),d='',b='',i;
  d+=LG(u,'s',0,0,0,130,[[0,'#6fa8d8'],[1,'#e8f0f4']])+LG(u,'g',0,160,0,270,[[0,'#6a7a3a'],[1,'#3f4a24']])+RG(u,'lt',360,30,260,[[0,'#fff8d0',.55],[1,'#fff8d0',0]])+vig(u);
  b+=R(0,0,480,170,'url(#'+u+'-s)')+R(0,0,480,170,'url(#'+u+'-lt)')+C(400,36,16,'#fffbe8')+E(120,40,60,8,'#fff',' opacity=".7"')+E(300,64,50,7,'#fff',' opacity=".6"');
  b+=D('M0 150l70-90 40 40 60-70 70 80 50-40 80 70 60-50 50 40v70h-480z','#8a9ab0')+D('M170 30l-24 26 12-4 10 10 8-8 10 6z','#fff')+D('M70 60l-18 20 10-2 8 8 6-6z','#fff');
  b+=D('M0 170l100-50 80 40 90-46 100 54 110-30v60h-480z','#5a7a4a')+D('M0 190l120-40 100 30 120-34 140 44v50h-480z','#4a6a3a');
  [[30,190,70],[70,196,90],[430,194,80],[460,190,100],[400,198,60]].forEach(function(t){b+=pine(t[0],t[1],t[2],'#2a5a34')});
  b+=R(0,196,480,74,'url(#'+u+'-g)');
  /* trilha de terra em perspectiva */
  b+=D('M200 170q30-4 50 0l110 100h-290z','#b89460',INK)+D('M215 172q16-2 30 0l70 98h-170z','#c9a874',' opacity=".6"')+Array.apply(null,{length:26}).map(function(){var y=176+r()*90,t=(y-170)/100,x=225+(r()-.5)*(80+t*240);return C(x,y,1+t*2.5,r()>.5?'#8a6a40':'#d8c090',' opacity=".7"')}).join('');
  b+=L(236,174,230,270,'#8a6a40',1,' opacity=".25"');
  /* pedras e arbustos */
  [[60,236,14],[104,252,10],[380,242,16],[430,256,12]].forEach(function(s){b+=E(s[0],s[1],s[2],s[2]*.6,'#8a8a90',INK)+E(s[0]-3,s[1]-3,s[2]*.5,s[2]*.25,'#b0b0b8',' opacity=".6"')});
  [[150,214,26],[340,216,22],[20,246,24],[470,236,22]].forEach(function(s){b+=C(s[0],s[1],s[2],'#3a6a30')+C(s[0]-6,s[1]-4,s[2]*.6,'#4f8a40')});
  /* placa de madeira */
  b+=R(398,128,8,110,'#6a4a2a',INK)+R(400,128,3,110,'#8a6a42',' opacity=".6"');
  b+=P('330,140 388,140 400,152 388,164 330,164','#c9965a',INK)+P('330,168 410,168 422,180 410,192 330,192','#b8844a',INK)+[0,1,2].map(function(k){return L(334,146+k*6,382,146+k*6,'#8a6a3a',.6,' opacity=".6"')}).join('')+tx(358,157,'SUMMIT 3 mi',8,'#2a1608','middle',700)+tx(372,184,'LAKE 1.5 mi',8,'#2a1608','middle',700)+C(338,152,1.6,'#555')+C(338,180,1.6,'#555');
  b+=RR(14,150,52,34,3,'#3a6a3a',INK)+tx(40,164,'TRAIL',8,'#fff')+tx(40,177,'#12  EASY',7,'#ffd070');
  b+=L(40,184,40,230,'#6a4a2a',3);
  return WRAP(u,d,b)};

/* ---------- DRIVE-THRU ---------- */
RS.drivethru=function(u){var r=rng(127),d='',b='',i;
  d+=LG(u,'s',0,0,0,130,[[0,'#1a2040'],[1,'#e87a4a']])+LG(u,'g',0,200,0,270,[[0,'#3a3a40'],[1,'#22222a']])+RG(u,'lt',110,150,200,[[0,'#ffd070',.5],[1,'#ffd070',0]])+vig(u);
  b+=R(0,0,480,200,'url(#'+u+'-s)')+stars(r,14,50);
  b+=R(0,120,480,50,'#1a1a28')+Array.apply(null,{length:22}).map(function(_,k){var w=14+r()*18,h=20+r()*30;return R(k*22,170-h,w,h,'#2a2438')+R(k*22+3,170-h+4,3,3,'#ffd070',' opacity=".7"')}).join('');
  /* asfalto e faixas */
  b+=R(0,196,480,74,'url(#'+u+'-g)')+R(0,196,480,3,'#555')+Array.apply(null,{length:6}).map(function(_,k){return R(10+k*80,258,44,4,'#e8c860',' opacity=".8"')}).join('');
  b+=R(0,196,480,5,'#8a8a90',INK)+R(0,200,480,2,'#444');
  /* prédio do restaurante */
  b+=R(0,40,330,160,'#e8d8b8',INK)+R(0,40,330,24,'#c8302a',INK)+R(0,64,330,5,'#fff')+tx(70,58,'BURGER HUT',14,'#fff',null,900)+R(140,36,6,4,'#555')+C(280,52,16,'#ffd04a',INK)+tx(280,57,'24h',11,'#c8302a');
  b+=R(0,130,330,6,'#c8302a')+Array.apply(null,{length:11}).map(function(_,k){return R(k*30,130,15,6,'#fff')}).join('');
  /* janela de atendimento */
  b+=R(14,76,140,70,'#2a1a14',INK)+R(18,80,132,62,'#ffd890')+R(18,80,132,62,'#fff',' opacity=".12"')+R(10,144,148,8,'#9a7a54',INK)+R(10,152,148,44,'#b89870',INK)+tx(84,92,'PICK UP',9,'#c8302a')+R(40,106,20,36,'#a8763a',' opacity=".5"')+R(110,104,28,20,'#cfd4dc',' opacity=".6"')+C(100,128,6,'#e8503a',INK)+RR(128,132,14,10,2,'#f4c430',INK);
  b+=R(176,76,2,60,'#555');
  /* cardápio luminoso */
  b+=R(338,62,128,138,'#12121a',INK)+R(342,66,120,24,'#c8302a')+tx(402,84,'WELCOME',12,'#fff',null,900)+R(342,94,120,102,'#1a1a26');
  [['Burger','5.99'],['Cheeseburger','6.49'],['Fries','2.99'],['Chicken Nuggets','4.99'],['Milkshake','3.99'],['Soda','1.99'],['Combo Meal','8.99']].forEach(function(m,k){var y=108+k*13;b+=tx(348,y,m[0],8,'#fff','start',600)+tx(456,y,'$'+m[1],8,'#ffd04a','end')+L(348,y+3,456,y+3,'#fff',.4,' opacity=".25"')});
  b+=C(402,130,60,'#ffd070',' opacity=".05"');
  /* poste e cones */
  b+=R(472,90,4,110,'#555')+[[340,246],[460,250]].forEach?'':'';
  [[346,244],[458,248]].forEach(function(c){b+=P((c[0]-6)+','+c[1]+' '+(c[0]+6)+','+c[1]+' '+c[0]+','+(c[1]-18),'#ff7a2a',INK)+R(c[0]-4,c[1]-9,8,3,'#fff')+R(c[0]-8,c[1],16,3,'#c9602a')});
  b+=P('190,196 210,196 210,170 190,170','#555',' opacity="0"');
  return WRAP(u,d,b)};

/* ---------- SALA DE FESTA ---------- */
RS.partyroom=function(u){var r=rng(139),d='',b='',i;
  d+=LG(u,'w',0,0,0,170,[[0,'#f0d8c8'],[1,'#e0b8a4']])+RG(u,'lt',240,40,300,[[0,'#fff4d0',.55],[1,'#fff4d0',0]])+vig(u);
  b+=R(0,0,480,170,'url(#'+u+'-w)')+planks(170,'#b88a5a','#7a5a38',12)+R(0,0,480,170,'url(#'+u+'-lt)');
  b+=R(0,164,480,6,'#fff',INK);
  /* janela com cortina */
  b+=R(376,34,80,90,'#2a3a52',INK)+R(380,38,72,82,'#8a6aa0')+L(416,38,416,120,'#f4ead4',3)+D('M368 28q16 40 8 100h-10z','#c8607a')+D('M464 28q-16 40-8 100h10z','#c8607a')+R(364,26,100,5,'#6a4a2a');
  /* faixa */
  b+=S('M20 30q220 56 440 0','#e8c860',2)+Array.apply(null,{length:9}).map(function(_,k){var x=44+k*48,y=30+Math.sin((x-20)/440*Math.PI)*28;return P((x-14)+','+y+' '+(x+14)+','+y+' '+x+','+(y+22),['#e8503a','#2f8fb8','#f4c430','#4f9a52','#b05cc0'][k%5],INK)}).join('');
  b+=RR(130,56,220,34,4,'#c8307a',INK)+tx(240,80,'HAPPY BIRTHDAY!',18,'#fff',null,900)+C(130,60,3,'#e8c860')+C(350,60,3,'#e8c860');
  /* bandeirinhas e confete */
  for(i=0;i<40;i++)b+=R(r()*480,r()*160,4,2,['#e8503a','#2f8fb8','#f4c430','#4f9a52','#b05cc0'][i%5],' opacity=".7" transform="rotate('+Math.floor(r()*180)+')" ');
  /* balões */
  [[26,150,'#e8503a'],[52,120,'#f4c430'],[40,86,'#2f8fb8'],[76,150,'#4f9a52'],[440,148,'#b05cc0'],[464,112,'#e8503a'],[420,100,'#f4c430'],[100,100,'#c8307a'],[352,130,'#2f8fb8']].forEach(function(bl){var x=bl[0],y=bl[1];b+=S('M'+x+' '+(y+20)+'q-6 40 '+(x>240?-4:4)+' '+(172-y),'#888',.7)+E(x,y,15,19,bl[2],INK)+P((x-3)+','+(y+19)+' '+(x+3)+','+(y+19)+' '+x+','+(y+24),bl[2])+E(x-5,y-7,4,7,'#fff',' opacity=".45"')});
  /* mesa do bolo */
  b+=R(150,150,180,8,'#fff',INK)+P('150,158 330,158 340,170 140,170','#c8307a',INK)+R(158,170,6,12,'#6a4a2a')+R(316,170,6,12,'#6a4a2a')+R(150,170,180,3,'#a8205a');
  /* bolo em camadas */
  b+=E(240,150,40,6,'#e8d8c8',INK)+R(206,124,68,26,'#f4e0d0',INK)+R(206,124,68,8,'#e8708a')+R(206,138,68,4,'#e8708a')+R(222,102,36,22,'#f8ecd8',INK)+R(222,102,36,6,'#e8708a')+[0,1,2,3,4].map(function(k){return R(228+k*6,92,2.4,10,['#2f8fb8','#f4c430','#e8503a','#4f9a52','#b05cc0'][k])+D('M'+(229.2+k*6)+' 88q-2 3 0 5q2-2 0-5z','#ffb030')}).join('')+[0,1,2,3,4,5].map(function(k){return C(210+k*11,124,2.6,'#e83a4a',INK)}).join('')+tx(240,142,'ANA',7,'#c8307a');
  /* pratos, copos e presentes */
  b+=[0,1,2].map(function(k){return E(176+k*0,152,0,0,'#fff')}).join('')+RR(164,138,22,12,2,'#fff',INK)+RR(294,138,22,12,2,'#fff',INK)+C(300,142,3,'#e8503a')+C(172,142,3,'#2f8fb8')+[0,1,2].map(function(k){return D('M'+(188+k*8)+' 150l-1-10h6l-1 10z','#e8503a',INK)}).join('');
  b+=R(26,216,40,32,'#2f8fb8',INK)+R(42,216,8,32,'#f4c430')+R(26,228,40,6,'#f4c430')+S('M46 216q-10-14-16-6M46 216q10-14 16-6','#f4c430',2.4);
  b+=R(80,232,30,22,'#e8503a',INK)+R(92,232,6,22,'#fff')+R(80,240,30,5,'#fff')+R(400,222,44,34,'#b05cc0',INK)+R(418,222,8,34,'#f4c430')+R(400,236,44,6,'#f4c430')+S('M422 222q-10-14-16-6M422 222q10-14 16-6','#f4c430',2.4);
  return WRAP(u,d,b)};

/* ---------- SALÃO DE CASAMENTO ---------- */
RS.weddinghall=function(u){var r=rng(151),d='',b='',i;
  d+=LG(u,'w',0,0,0,170,[[0,'#f6ecdc'],[1,'#e0d0b4']])+RG(u,'lt',240,70,260,[[0,'#fff4d0',.6],[1,'#fff4d0',0]])+vig(u);
  b+=R(0,0,480,170,'url(#'+u+'-w)')+R(0,170,480,100,'#a07a52')+R(0,0,480,170,'url(#'+u+'-lt)');
  for(i=0;i<14;i++)b+=L(0,170+i*7,480,170+i*7,'#7a5a38',.7,' opacity=".35"');
  /* janelas altas */
  [14,92,350,426].forEach(function(x){b+=D('M'+x+' 160v-100q20-34 40 0v100z','#8fb4d4',INK)+L(x+20,40,x+20,160,'#f4ead4',2)+L(x,100,x+40,100,'#f4ead4',2)+D('M'+x+' 160v-100q20-34 40 0v100z','#fff',' opacity=".15"')});
  /* cortinas */
  [[8,'l'],[470,'r']].forEach(function(c){});
  /* lustres */
  [[110,22],[240,14],[370,22]].forEach(function(l){var x=l[0],y=l[1];b+=L(x,0,x,y,'#8a6a3a',1)+D('M'+(x-22)+' '+y+'q22 16 44 0l-6 12h-32z','#e8c860',INK)+Array.apply(null,{length:7}).map(function(_,k){return C(x-18+k*6,y+16,1.6,'#fff4c8')+L(x-18+k*6,y+12,x-18+k*6,y+22,'#fff4c8',.6,' opacity=".6"')}).join('')+C(x,y+14,30,'#ffe9a0',' opacity=".2"')});
  /* arco de flores */
  b+=R(172,60,6,110,'#e8e0d0',INK)+R(302,60,6,110,'#e8e0d0',INK)+S('M174 64q66-64 132 0','#e8e0d0',6)+S('M174 64q66-64 132 0','#6a9a4a',9,' opacity=".85"');
  var fl=['#fff','#f4a0b0','#e8708a','#fff4c8','#f8c8d8'];
  for(i=0;i<34;i++){var a=Math.PI*(i/33),fx=240-66*Math.cos(a),fy=64-48*Math.sin(a)+Math.sin(i*2)*3;b+=C(fx,fy,4+r()*2.5,fl[i%5],INK)+C(fx,fy,1.4,'#e8c860')+C(fx+4,fy+3,2.6,'#4f8a40')}
  for(i=0;i<12;i++){b+=C(174+r()*10-5,70+i*8,4,fl[i%5],INK)+C(306+r()*10-5,70+i*8,4,fl[(i+2)%5],INK)}
  b+=S('M200 52q-6 30-4 60M280 52q6 30 4 60','#fff',1.4,' opacity=".6"');
  /* vasos de flores no altar */
  [[140,'#e8708a'],[340,'#f4a0b0']].forEach(function(v){var x=v[0];b+=D('M'+(x-10)+' 156h20l-4 14h-12z','#e8e0d0',INK)+[0,1,2,3,4].map(function(k){return C(x-9+k*4.5,148-(k%2)*5,5,k%2?'#fff':v[1],INK)}).join('')});
  /* tapete corredor central é deixado livre; cadeiras laterais em fileiras */
  [[0,-1],[1,1]].forEach(function(sd){for(i=0;i<4;i++){var y=198+i*17,s=1+i*.14,x0=sd[1]<0?20-i*6:460+i*6;for(var j=0;j<3;j++){var xx=sd[1]<0?x0+j*30*s:x0-j*30*s;b+=R(xx-8*s,y-14*s,16*s,15*s,'#fff',INK)+R(xx-9*s,y,18*s,5*s,'#e8dcc4',INK)+R(xx-7*s,y+5*s,2,8*s,'#c9b080')+R(xx+5*s,y+5*s,2,8*s,'#c9b080')+S('M'+(xx-6*s)+' '+(y-14*s)+'h'+(12*s),'#e8c860',1)}}});
  /* laços nos corredores */
  b+=D('M118 214q-6-8 0-10l6 6 6-6q6 2 0 10l-6-4z','#f4a0b0',INK);
  /* pétalas no chão ao centro (sutil) */
  for(i=0;i<16;i++)b+=E(200+r()*80,226+r()*36,2.4,1.2,i%2?'#f8c8d8':'#fff',' opacity=".6"');
  return WRAP(u,d,b)};

/* ---------- BOLICHE ---------- */
RS.bowling=function(u){var r=rng(163),d='',b='',i;
  d+=LG(u,'w',0,0,0,110,[[0,'#14102a'],[1,'#2a1a4a']])+LG(u,'ln',0,110,0,270,[[0,'#e0b070'],[1,'#c08a48']])+RG(u,'lt',240,130,240,[[0,'#ffd890',.35],[1,'#ffd890',0]])+vig(u);
  b+=R(0,0,480,110,'url(#'+u+'-w)')+R(0,110,480,160,'#1c1430');
  /* luz neon */
  b+=R(0,0,480,6,'#ff3aa0',' opacity=".8"')+R(0,0,480,16,'#ff3aa0',' opacity=".1"')+R(0,104,480,3,'#3ad0ff',' opacity=".9"');
  /* placar suspenso */
  b+=R(170,14,140,50,'#0c0818',INK)+R(174,18,132,42,'#14283a')+tx(240,32,'LANE 7',10,'#ffd04a',null,900)+[0,1,2,3,4,5,6,7,8,9].map(function(k){return R(180+k*12,38,11,10,'#0c1a28',' stroke="#3ad0ff" stroke-width=".4"')+tx(185.5+k*12,46,['X','7','/','9','8','X','6','/','8','X'][k],7,'#4aff9a')}).join('')+tx(240,57,'ANA 187   LEO 164',6,'#fff');
  /* pinos ao fundo */
  b+=R(150,76,180,34,'#0c0818',INK)+R(150,76,180,6,'#2a1a3a');
  [[240,98],[228,92],[252,92],[216,86],[240,86],[264,86],[204,80],[228,80],[252,80],[276,80]].forEach(function(p,k){var x=p[0],y=p[1]+6;b+=E(x,y+2,3,1,'#000',' opacity=".3"')+D('M'+(x-2)+' '+y+'q-3-5 0-9q-2-3 0-5h4q2 2 0 5q3 4 0 9z','#fff',INK)+R(x-2,y-8,4,1.2,'#d8323a')});
  /* pistas em perspectiva */
  b+=P('140,110 340,110 470,270 10,270','url(#'+u+'-ln)',INK)+P('140,110 340,110 470,270 10,270','#fff',' opacity=".06"');
  for(i=0;i<22;i++)b+=L(150+i*8.6,110,32+i*20.5,270,'#8a5a28',.8,' opacity=".35"');
  b+=P('140,110 150,110 40,270 10,270','#3a2418')+P('340,110 330,110 440,270 470,270','#3a2418');
  /* setas de mira */
  [0,1,2,3,4,5,6].forEach(function(k){var t=Math.abs(k-3),y=150+t*4,x=240+(k-3)*(26-t*0);b+=P((240+(k-3)*24)+','+(y-8)+' '+(240+(k-3)*24-4)+','+(y+2)+' '+(240+(k-3)*24+4)+','+(y+2),'#5a3418',' opacity=".7"')});
  b+=R(0,196,480,3,'#ff3aa0',' opacity=".0"');
  /* retorno de bolas (laterais) */
  b+=RR(6,200,90,34,8,'#3a3a44',INK)+RR(384,200,90,34,8,'#3a3a44',INK)+R(8,206,86,6,'#555');
  [['#d8323a',24],['#2f6fd0',46],['#3aa05a',68]].forEach(function(c){b+=C(c[1],198,10,c[0],INK)+C(c[1]-3,194,1.4,'#111')+C(c[1]+1,193,1.4,'#111')+C(c[1]-2,198,1.4,'#111')+C(c[1]-4,193,3,'#fff',' opacity=".4"')});
  [['#e8a43a',404],['#b05cc0',426],['#2fb8b8',448]].forEach(function(c){b+=C(c[1],198,10,c[0],INK)+C(c[1]-3,194,1.4,'#111')+C(c[1]+1,193,1.4,'#111')+C(c[1]-2,198,1.4,'#111')+C(c[1]-4,193,3,'#fff',' opacity=".4"')});
  /* sapatos */
  b+=RR(10,248,34,14,5,'#d8323a',INK)+R(10,255,34,6,'#f4ead4')+RR(52,250,30,12,5,'#2f6fd0',INK)+R(52,256,30,5,'#f4ead4')+tx(98,258,'SHOES',7,'#ffd04a','start');
  b+=RR(396,244,70,20,3,'#2a2a34',INK)+tx(431,258,'LANE 7',9,'#3ad0ff');
  return WRAP(u,d,b)};

/* ---------- MINIGOLFE ---------- */
RS.minigolf=function(u){var r=rng(173),d='',b='',i;
  d+=LG(u,'s',0,0,0,120,[[0,'#7fc0e8'],[1,'#fff0d0']])+LG(u,'g',0,130,0,270,[[0,'#4fb04a'],[1,'#2f8a38']])+RG(u,'lt',100,20,260,[[0,'#fff8c0',.55],[1,'#fff8c0',0]])+vig(u);
  b+=R(0,0,480,140,'url(#'+u+'-s)')+R(0,0,480,140,'url(#'+u+'-lt)')+E(330,34,54,9,'#fff',' opacity=".7"')+E(120,60,44,7,'#fff',' opacity=".6"');
  b+=D('M0 124q60-30 130-6t160-6 190 10v30h-480z','#3a8a46')+[40,150,300,440].map(function(x){return tree(x,132,60,'#2f7a38','#3f9a48')}).join('');
  b+=R(0,128,480,142,'url(#'+u+'-g)');
  /* grama listrada */
  for(i=0;i<10;i++)b+=P((i*60-80)+',270 '+(i*60-20)+',270 '+(i*60+20)+',130 '+(i*60-10)+',130',i%2?'#3fa040':'#4fb04a',' opacity=".3"');
  /* moinho de vento */
  b+=P('382,116 436,116 430,50 388,50','#f4ead4',INK)+P('382,116 400,116 396,50 388,50','#c8b898',' opacity=".5"')+P('380,50 438,50 409,22','#c8302a',INK)+RR(400,92,18,24,9,'#6a3a24',INK)+R(396,66,10,10,'#5a8ab0',INK)+R(412,66,10,10,'#5a8ab0',INK)+C(409,44,4,'#6a4a2a',INK);
  b+=G('translate(409 44)',[0,1,2,3].map(function(k){return G('rotate('+(k*90+18)+')',R(-2,-36,4,36,'#8a6a3a',INK)+R(1,-36,12,24,'#f4ead4',INK)+R(1,-36,12,24,'#c8302a',' opacity=".35"'))}).join(''))+C(409,44,5,'#c9965a',INK);
  b+=R(372,116,76,6,'#8a8a90',INK);
  /* pista de feltro com borda de madeira */
  b+=P('40,262 440,262 410,170 70,170','#2f9a4a',INK)+P('40,262 440,262 410,170 70,170','#fff',' opacity=".05"');
  b+=S('M70 170L40 262','#8a5a30',6)+S('M410 170L440 262','#8a5a30',6)+S('M70 170H410','#8a5a30',5)+S('M40 262H440','#a8763a',6);
  /* obstáculos ficam à beira para deixar o centro livre */
  b+=P('86,214 130,214 124,200 92,200','#8a8a90',INK)+D('M86 214q22-34 44 0z','#6a6a72',INK)+R(94,206,28,8,'#12121a');
  b+=R(352,196,40,10,'#c9965a',INK)+P('352,196 392,196 372,176','#d8323a',INK);
  /* buraco, bandeira e bolas */
  b+=E(310,196,7,3,'#12121a',INK)+L(310,196,310,166,'#ddd',1.4)+P('310,166 328,172 310,178','#e8503a',INK)+tx(319,173,'7',4,'#fff');
  b+=C(96,244,4.6,'#fff',INK)+C(94.6,242.6,1.4,'#fff')+C(420,240,4.6,'#2f8fb8',INK)+C(360,232,4.6,'#f4c430',INK);
  /* tacos e placar */
  b+=L(46,230,70,266,'#cfd4dc',2.4)+R(40,226,8,5,'#d8323a')+L(30,222,52,262,'#cfd4dc',2.4);
  b+=R(18,86,64,42,'#fff',INK)+R(18,86,64,12,'#3f8a38')+tx(50,96,'HOLE 7',8,'#fff')+tx(50,112,'PAR 3',10,'#2a1608')+R(46,128,6,20,'#6a4a2a')+tx(50,123,'MINI GOLF',6,'#3f8a38');
  return WRAP(u,d,b)};

/* ---------- ELEVADOR ---------- */
RS.elevator=function(u){var r=rng(181),d='',b='',i;
  d+=LG(u,'w',0,0,0,270,[[0,'#8a8f98'],[1,'#5a5f68']])+RG(u,'lt',240,20,260,[[0,'#fff8e0',.6],[1,'#fff8e0',0]])+LG(u,'m',0,0,480,0,[[0,'#cfd8e0'],[.5,'#f0f6fa'],[1,'#b0bcc8']])+vig(u);
  /* parede de fundo em aço escovado */
  b+=R(0,0,480,270,'url(#'+u+'-w)');
  for(i=0;i<32;i++)b+=R(i*15,22,.8,200,'#fff',' opacity="'+(.05+r()*.12).toFixed(2)+'"');
  /* painéis laterais */
  b+=R(0,22,60,200,'#6a6f78',INK)+R(420,22,60,200,'#6a6f78',INK)+R(8,34,44,176,'#7a808a')+R(428,34,44,176,'#7a808a')+R(0,22,60,200,'#fff',' opacity=".04"');
  /* teto com luminária */
  b+=R(0,0,480,22,'#cfd3d8',INK)+R(120,6,240,10,'#fff8e0',INK)+R(120,6,240,10,'#fff',' opacity=".6"')+C(240,16,60,'#fff8e0',' opacity=".15"');
  [40,80,400,440].forEach(function(x){b+=C(x,12,4,'#fff8e0',INK)});
  /* espelho no fundo */
  b+=R(76,40,328,150,'#3a3f48',INK)+R(80,44,320,142,'url(#'+u+'-m)')+P('80,44 180,44 120,186 80,186','#fff',' opacity=".25"')+P('220,44 250,44 190,186 160,186','#fff',' opacity=".12"');
  b+=R(80,170,320,16,'#9aa6b4',' opacity=".4"');
  /* corrimão */
  b+=RR(64,196,352,8,4,'#b0b6c0',INK)+R(64,197,352,2,'#fff',' opacity=".7"')+R(70,203,6,8,'#777')+R(404,203,6,8,'#777');
  /* painel de botões (direita) */
  b+=RR(430,56,40,140,4,'#2a2e36',INK)+RR(434,60,32,132,3,'#c8ced6')+RR(438,64,24,14,2,'#0c0c10')+tx(450,75,'7',11,'#ff5a3a',null,900)+P('446,66 450,63 454,66','#ff5a3a');
  for(i=0;i<8;i++){var by=86+Math.floor(i/2)*22,bx=444+(i%2)*14;b+=C(bx,by,5.4,'#e8ecf0',INK)+C(bx,by,5.4,i==6?'#ffd070':'none',' opacity=".5"')+tx(bx,by+2.5,String(8-i),6.5,'#2a2a30')}
  b+=C(444,176,5.4,'#e8ecf0',INK)+tx(444,178.5,'<>',5,'#2a2a30')+C(458,176,5.4,'#e8ecf0',INK)+tx(458,178.5,'><',5,'#2a2a30')+C(451,188,0,'#fff');
  b+=RR(434,186,32,0,0,'none');
  /* indicador de andar acima e placas */
  b+=RR(210,28,60,0,0,'none');
  b+=R(436,200,28,14,'#e8ecf0',INK)+tx(450,210,'ALARM',5,'#d8323a')+R(14,60,32,40,'#e8ecf0',INK)+tx(30,72,'MAX',6,'#2a2a30')+tx(30,82,'12 PERSONS',5,'#2a2a30')+tx(30,92,'2,100 lbs',5,'#2a2a30')+R(14,108,32,12,'#2f6fd0',INK)+tx(30,117,'HELP',6,'#fff');
  /* portas fechando no fundo? piso */
  b+=R(0,222,480,48,'#4a4e56',INK)+Array.apply(null,{length:12}).map(function(_,k){return L(k*40,222,k*40-20,270,'#3a3e46',.8,' opacity=".6"')}).join('')+R(0,222,480,3,'#9aa0aa')+RG(u,'fl',240,236,200,[[0,'#fff8e0',.3],[1,'#fff8e0',0]])+R(0,222,480,48,'url(#'+u+'-fl)');
  b+=R(0,258,480,12,'#2a2e36',INK)+E(60,246,20,4,'#2a2e36',' opacity=".5"');
  return WRAP(u,d,b)};
})();
