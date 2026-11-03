/* Cenários mais detalhados para o painel do professor (supermercado, restaurante, cozinha, academia).
   Mesma identidade de scn_new.js (SF helpers, 480×270, pintura quente, vinheta). Só substitui RS.* quando carregado depois. */
(function(){
if(!window.SF||!window.RS)return;
var SF=window.SF,RS=window.RS,rng=SF.rng,LG=SF.LG,RG=SF.RG,R=SF.R,RR=SF.RR,E=SF.E,C=SF.C,L=SF.L,P=SF.P,D=SF.D,S=SF.S,G=SF.G,INK=SF.INK,WRAP=SF.WRAP,vig=SF.vig,T=SF.T;
var SANS='Trebuchet MS,Arial,sans-serif';
function tile(y0,a,b,sz){var s='',i,j;for(j=0;y0+j*sz*.5<270;j++)for(i=0;i<480/sz+1;i++)s+=R(i*sz,y0+j*sz*.5,sz,sz*.5,(i+j)%2?a:b);return s}
function planks(y0,c1,c2,seed){var r=rng(seed),b=R(0,y0,480,270-y0,c1),i;for(i=0;i<14;i++)b+=L(0,y0+i*(270-y0)/14,480,y0+i*(270-y0)/14+(r()-.5)*2,c2,.8,' opacity=".35"');for(i=0;i<20;i++){var x=r()*480,y=y0+r()*(270-y0);b+=L(x,y,x+(r()-.5)*40,y+2,c2,.6,' opacity=".25"')}return b}
/* ---------- SUPERMERCADO ---------- */
RS.supermarket=function(u){var r=rng(41),d='',b='',i,j;
  d+=LG(u,'w',0,0,0,170,[[0,'#f6f3ea'],[1,'#e3dfcf']])+LG(u,'f',0,170,0,270,[[0,'#e6e2d4'],[1,'#c3bda8']])+RG(u,'lt',240,40,300,[[0,'#ffffff',.55],[1,'#ffffff',0]])+vig(u);
  b+=R(0,0,480,170,'url(#'+u+'-w)')+tile(170,'#e9e5d6','#d2ccb8',30)+R(0,170,480,100,'url(#'+u+'-f)',' opacity=".35"');
  /* teto com luminárias */
  b+=R(0,0,480,18,'#cfd3d8')+[40,150,270,380].map(function(x){return R(x,5,64,8,'#fff',INK)+R(x-6,13,76,3,'#fff',' opacity=".5"')}).join('');
  /* placas penduradas dos corredores */
  [[62,'PRODUCE','#3f9a4a'],[240,'DAIRY','#2f7fc0'],[418,'BAKERY','#d98a3a']].forEach(function(s){var x=s[0];b+=L(x-26,18,x-26,34,'#777',1)+L(x+26,18,x+26,34,'#777',1)+RR(x-34,32,68,20,4,s[2],INK)+T(x,47,'',12,'#fff',{a:'middle',w:700,f:SANS}).replace('></text>','>'+s[1]+'</text>')});
  /* hortifrúti (esquerda): caixotes inclinados com frutas e verduras */
  b+=R(14,70,128,6,'#b98a52',INK);
  [[18,'#e8503a','tomatoes'],[58,'#f4c430','lemons'],[98,'#7cc06a','greens']].forEach(function(c,k){var x=c[0];b+=D('M'+x+' 110l4 34h30l4-34z','#c9965a',INK)+R(x+2,110,38,5,'#a8763a');for(var q=0;q<9;q++){var cx=x+7+(q%5)*7+(q>4?3:0),cy=106-(q>4?7:0);b+=C(cx,cy,5.4,c[1],INK)+C(cx-1.6,cy-1.8,1.5,'#fff',' opacity=".55"')}});
  b+=RR(14,84,128,18,3,'#fff',INK)+T(78,98,'',9,'#3f7a3a',{a:'middle',w:700,f:SANS}).replace('></text>','>FRESH · LOCAL</text>');
  /* geladeiras de laticínios (centro) */
  b+=RR(166,62,148,96,4,'#dfe9ef',INK)+[0,1,2].map(function(k){var x=172+k*47;return RR(x,68,43,84,2,'#bfe0f0',INK)+R(x+3,74,37,74,'#e9f6fb',' opacity=".9"')+[0,1,2].map(function(s){var y=82+s*22;return R(x+4,y+14,35,2,'#9aa0aa')+[0,1,2,3].map(function(m){return R(x+7+m*8.5,y,6.5,14,m%2?'#fff':'#e8f2fa',INK)+R(x+7+m*8.5,y+3,6.5,4,m%3?'#2f7fc0':'#e8a43a')}).join('')}).join('')+L(x+43,100,x+43,120,'#777',1.4)}).join('');
  /* prateleiras (direita): caixas e latas */
  b+=R(332,60,138,100,'#8a6a4a',INK);for(j=0;j<4;j++){var sy=66+j*24;b+=R(336,sy+17,130,3,'#c9b79a',INK);for(i=0;i<10;i++){var h=11+Math.floor(r()*5),w=10+Math.floor(r()*3),col=['#e8503a','#f4c430','#2f8fb8','#4f9a52','#b05cc0','#fff','#e08a3f'][Math.floor(r()*7)];b+=R(338+i*12.6,sy+17-h,w,h,col,INK)+R(340+i*12.6,sy+19-h,w-4,3,'#fff',' opacity=".55"')}}
  /* corredor central: gôndolas em perspectiva */
  b+=P('150,172 330,172 360,206 120,206','#cfc9b6',INK)+R(120,206,240,6,'#a39d88',INK);
  [[132,'#e8503a'],[182,'#f4c430'],[232,'#2f8fb8'],[282,'#4f9a52']].forEach(function(c){b+=R(c[0],180,38,22,c[1],INK)+R(c[0]+3,183,32,5,'#fff',' opacity=".5"')});
  /* checkout à direita */
  b+=D('M372 214h96v22h-96z','#9aa0aa',INK)+R(372,206,96,10,'#3c4650',INK)+RR(384,176,40,30,3,'#2a2f36',INK)+R(388,180,32,18,'#7fd0e0',' opacity=".85"')+RR(430,190,26,16,2,'#e8503a',INK)+T(443,202,'',7,'#fff',{a:'middle',w:700,f:SANS}).replace('></text>','>3</text>')+C(406,222,3,'#f4c430')+C(420,222,3,'#4f9a52')+R(438,224,16,8,'#2f8fb8');
  /* carrinhos e cestas */
  b+=D('M18 214h70l-8 34h-54z','#cfd4dc',INK)+S('M18 214l-10-18h-14','#555',3)+C(36,254,5.5,'#2a2a2a')+C(70,254,5.5,'#2a2a2a')+[28,42,58,72].map(function(x){return L(x,222,x-2,244,'#999',.8)}).join('')+C(44,208,8,'#e8503a',INK)+R(56,200,13,13,'#f4c430',INK);
  b+=RR(96,224,36,22,3,'#e8503a',INK)+RR(100,230,28,12,2,'#c03a2a')+S('M98 226q16-14 32 0','#a8301f',2);
  return WRAP(u,d,b)};
/* ---------- RESTAURANTE ---------- */
RS.restaurant=function(u){var r=rng(52),d='',b='',i;
  d+=LG(u,'w',0,0,0,170,[[0,'#6b2a26'],[1,'#a24a3a']])+RG(u,'lt',240,60,280,[[0,'#ffd8a0',.55],[1,'#ffd8a0',0]])+vig(u);
  b+=R(0,0,480,170,'url(#'+u+'-w)')+planks(170,'#8a5a34','#4a2e18',6)+R(0,0,480,170,'url(#'+u+'-lt)');
  /* lambri e papel de parede */
  b+=R(0,110,480,60,'#5a3a24')+R(0,108,480,4,'#c9965a')+[0,1,2,3,4,5,6,7,8,9,10,11].map(function(k){return R(k*40+4,116,32,48,'none',' stroke="#7a5236" stroke-width="1.4"')}).join('');
  for(i=0;i<16;i++)b+=R(i*30+8,10,2,96,'#fff',' opacity=".05"');
  /* janela + quadros */
  b+=R(24,28,92,76,'#2a3a52',INK)+R(28,32,84,68,'#8fb4d4')+L(70,32,70,100,'#f4ead4',3)+L(28,66,112,66,'#f4ead4',3)+R(18,24,104,6,'#3a2418')+P('28,32 70,32 28,76','#fff',' opacity=".25"')+[0,1].map(function(k){return R(36+k*50,52,16,14,'#e8c860',' opacity=".75"')}).join('');
  b+=R(340,34,50,40,'#c9965a',INK)+R(344,38,42,32,'#7aa0b8')+C(365,52,9,'#e8c860')+R(398,40,44,34,'#c9965a',INK)+R(402,44,36,26,'#a8c0a0');
  /* luminárias */
  [[160,'#e8c860'],[260,'#e8c860'],[360,'#e8c860']].forEach(function(l){var x=l[0];b+=L(x,0,x,22,'#222',1)+D('M'+(x-26)+' 22h52l-9 17h-34z',l[1],INK)+C(x,40,30,'#ffe3a0',' opacity=".22"')});
  /* balcão/bar com banquetas ao fundo */
  b+=R(186,118,150,10,'#3a2418',INK)+R(186,128,150,38,'#6b4a34',INK)+R(192,134,138,26,'#52371f')+[0,1,2,3,4,5,6].map(function(k){return RR(194+k*20,96,8,22,3,['#2f8fb8','#4f9a52','#e8503a','#f4c430','#b05cc0','#2f8fb8','#e8503a'][k],INK)}).join('')+[0,1,2,3].map(function(k){return R(206+k*30,168,4,22,'#222')+E(208+k*30,166,10,3,'#a8301f',INK)}).join('');
  /* mesas postas em primeiro plano */
  [[84,214,'#f6f0e2'],[336,220,'#f1e6d0']].forEach(function(t){var x=t[0],y=t[1];b+=E(x+34,y+34,52,6,'#000',' opacity=".2"')+R(x+31,y+4,6,30,'#4a2e18')+E(x+34,y+36,18,3,'#3a2418')+E(x+34,y+2,54,13,t[2],INK)+D('M'+(x-20)+' '+(y+2)+'q54 24 108 0l-6 12q-48 18-96 0z',t[2],INK)+E(x+16,y+0,9,3,'#fff',INK)+E(x+52,y+0,9,3,'#fff',INK)+C(x+34,y-2,3.4,'#e8503a',INK)+S('M'+(x+34)+' '+(y-5)+'v-5','#f4c430',1.4)+RR(x+25,y-9,18,5,1.5,'#fff',INK)+RR(x+60,y-6,5,8,1.5,'#cfe8f0',INK)});
  /* cadeiras */
  [[40,216],[188,222],[298,222],[446,218]].forEach(function(c){b+=R(c[0],c[1],4,30,'#4a2e18')+R(c[0]+22,c[1],4,30,'#4a2e18')+RR(c[0]-2,c[1]-4,30,8,3,'#8a4a2a',INK)+RR(c[0]-2,c[1]-40,5,38,2,'#6b3a22',INK)});
  /* lousa do cardápio */
  b+=R(10,134,70,36,'#2a2f2a',INK)+T(45,148,'',8,'#f4ead4',{a:'middle',w:700,f:'Georgia,serif'}).replace('></text>','>TODAY</text>')+L(18,154,70,154,'#c9b79a',1)+L(18,160,62,160,'#c9b79a',1)+L(18,166,66,166,'#c9b79a',1);
  return WRAP(u,d,b)};
/* ---------- COZINHA DE CASA ---------- */
RS.kitchen=function(u){var r=rng(63),d='',b='',i;
  d+=LG(u,'w',0,0,0,170,[[0,'#f4ead4'],[1,'#e6d8bb']])+RG(u,'lt',130,60,260,[[0,'#fff0c4',.5],[1,'#fff0c4',0]])+vig(u);
  b+=R(0,0,480,170,'url(#'+u+'-w)')+planks(170,'#b88a5a','#7a5a38',9)+R(0,0,480,170,'url(#'+u+'-lt)');
  /* azulejos */
  b+=R(0,84,480,48,'#f8f6ee')+[0,1,2,3].map(function(j){return L(0,84+j*12,480,84+j*12,'#d9d2c0',.8)}).join('')+Array.apply(null,{length:24}).map(function(_,k){return L(k*20,84,k*20,132,'#d9d2c0',.8)}).join('');
  /* armários altos */
  [[10,'#5a9a98'],[170,'#5a9a98'],[330,'#5a9a98']].forEach(function(a){var x=a[0];b+=R(x,16,140,60,a[1],INK)+L(x+70,16,x+70,76,'#2d5e5c',1.6)+RR(x+62,40,5,12,2,'#e8c860',INK)+RR(x+73,40,5,12,2,'#e8c860',INK)+R(x+6,22,58,48,'#fff',' opacity=".07"')});
  /* janela */
  b+=R(150,22,0,0,'none');
  /* fogão com coifa */
  b+=D('M196 70h88l-10-20h-68z','#cfd4dc',INK)+R(226,16,28,34,'#9aa0aa',INK)+R(186,132,108,36,'#9aa0aa',INK)+R(190,136,100,28,'#dfe3e8',INK)+[0,1,2,3].map(function(k){return E(210+k*24,132,10,3.2,'#2a2a2a',INK)}).join('')+RR(200,142,32,20,2,'#2a2f36',INK)+R(204,146,24,12,'#7aa0b8',' opacity=".6"')+RR(246,150,6,6,3,'#777')+RR(262,150,6,6,3,'#777');
  b+=E(220,126,22,8,'#2a2a2a',INK)+R(240,122,30,4,'#555')+D('M208 122q12-18 24 0','#fff',' opacity=".75"')+E(264,124,18,7,'#c9553d',INK)+D('M256 120q4-14 8 0','#fff',' opacity=".7"');
  /* bancada */
  b+=R(0,132,180,8,'#d9c9a8',INK)+R(0,140,180,30,'#6a4a3a',INK)+R(298,132,182,8,'#d9c9a8',INK)+R(298,140,182,30,'#6a4a3a',INK)+[0,1,2,3].map(function(k){return RR(10+k*42,148,34,16,2,'#7a5a48',INK)}).join('')+[0,1,2,3].map(function(k){return RR(308+k*44,148,36,16,2,'#7a5a48',INK)}).join('');
  /* tábua, frutas, utensílios */
  b+=RR(18,124,56,6,2,'#c9965a',INK)+C(40,119,7,'#e8503a',INK)+C(52,120,6,'#f4a430',INK)+R(60,108,4,22,'#555')+D('M58 108h8v-8h-8z','#cfd4dc',INK)+E(106,124,22,9,'#cfa05a',INK)+C(98,120,6,'#7cc06a',INK)+C(112,120,6,'#f4c430',INK)+C(105,115,5,'#e8503a',INK);
  b+=R(350,118,16,14,'#f6f0e2',INK)+R(370,112,12,20,'#2f8fb8',INK)+R(386,116,12,16,'#e8503a',INK)+R(440,92,28,40,'#cfd4dc',INK)+R(446,98,16,10,'#f4c430',INK);
  /* geladeira */
  b+=RR(392,66,76,104,4,'#e9eef2',INK)+L(392,112,468,112,'#9aa0aa',1.6)+RR(398,84,4,22,2,'#777')+RR(398,122,4,26,2,'#777')+R(412,86,22,16,'#f4c430',INK)+R(438,92,18,12,'#e8503a',INK);
  /* piso: tapete */
  b+=D('M150 224q90 12 180 0l16 22q-106 14 -212 0z','#c9553d',INK)+L(190,230,170,246,'#a8301f',1,' opacity=".6"')+L(330,230,350,246,'#a8301f',1,' opacity=".6"');
  return WRAP(u,d,b)};
})();
