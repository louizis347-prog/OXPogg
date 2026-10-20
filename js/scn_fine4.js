/* scn_fine4.js - interiores refinados: loja, lanchonete e cafés. Usa window.SF de scn_fine.js. */
(function(){
if(!window.SF||!window.RS)return;
var SF=window.SF;
var rng=SF.rng,r1=SF.r1,LG=SF.LG,RG=SF.RG,R=SF.R,RR=SF.RR,E=SF.E,C=SF.C,L=SF.L,P=SF.P,D=SF.D,S=SF.S,T=SF.T,G=SF.G,INK=SF.INK,WRAP=SF.WRAP,vig=SF.vig,reg=SF.reg;

/* piso xadrez em perspectiva */
function checkerFloor(u,y0,vy,c1,c2,size,line){
  var b='',n=14,rows=[y0,y0+7,y0+17,y0+31,y0+51,y0+80,y0+118,270].filter(function(y,i,a){return y<=270}),i,j;
  b+=R(0,y0,480,270-y0,c1);
  for(j=0;j<rows.length-1;j++){
    var yA=rows[j],yB=rows[j+1],kA=(yA-vy)/(270-vy),kB=(yB-vy)/(270-vy);
    for(i=-n;i<n;i++){if(((i+j)&1)===0)continue;
      b+=P(r1(240+i*size*kA)+','+yA+' '+r1(240+(i+1)*size*kA)+','+yA+' '+r1(240+(i+1)*size*kB)+','+yB+' '+r1(240+i*size*kB)+','+yB,c2);}
  }
  for(i=-n;i<=n;i++)b+=L(r1(240+i*size*((y0-vy)/(270-vy))),y0,r1(240+i*size),270,line,.6,' opacity=".28"');
  rows.forEach(function(y){b+=L(0,y,480,y,line,.6,' opacity=".28"');});
  return b;
}

/* prateleira com mercadorias: potes, caixas, garrafas e latas */
function goods(x,y,w,h,seed){
  var r=rng(seed),b='',s,rows=Math.max(1,Math.floor(h/24)),sh=h/rows;
  b+=R(x,y,w,h,'#4a3322',INK)+R(x+2,y+2,w-4,h-4,'#2a1c12');
  var cols=['#d94f3d','#e8b948','#2f8fb8','#79b06a','#8c6aa6','#f08aa0','#f4f0e6','#e58a3f','#3f9a8a'];
  for(s=0;s<rows;s++){
    var by=y+2+(s+1)*sh-3,bx=x+4;
    while(bx<x+w-10){
      var kind=Math.floor(r()*4),c=cols[Math.floor(r()*cols.length)];
      if(kind===0){var bw=7+r()*3,bh=11+r()*6;b+=RR(bx,by-bh,bw,bh,2,c,INK)+R(bx,by-bh,bw,2.4,'#fff',' opacity=".5"')+R(bx+1,by-bh*.6,bw-2,bh*.28,'#fff',' opacity=".8"');bx+=bw+1.4;}
      else if(kind===1){var bw2=9+r()*4,bh2=13+r()*8;b+=R(bx,by-bh2,bw2,bh2,c,INK)+R(bx+1,by-bh2+2,bw2-2,3,'#fff',' opacity=".6"')+C(bx+bw2/2,by-bh2*.45,2.2,'#fff',' opacity=".8"');bx+=bw2+1.2;}
      else if(kind===2){var bh3=15+r()*6;b+=RR(bx+1.4,by-bh3,4.6,bh3*.7,1.4,c,INK)+R(bx+2.6,by-bh3-5,2.2,5.4,c,INK)+R(bx+2.4,by-bh3-6,2.6,1.6,'#e6c35c')+R(bx+1.4,by-bh3*.6,4.6,3,'#fff',' opacity=".7"');bx+=8.4;}
      else {var bh4=9+r()*3;b+=RR(bx,by-bh4,7.4,bh4,1.4,c,INK)+R(bx,by-bh4*.62,7.4,2,'#fff',' opacity=".7"')+R(bx,by-bh4*.34,7.4,.8,'#000',' opacity=".25"');bx+=8.6;}
    }
    b+=R(x+2,y+2+(s+1)*sh-3,w-4,3,'#a87444',INK)+R(x+2,y+2+(s+1)*sh-3,w-4,.8,'#e0b784',' opacity=".7"');
  }
  return b;
}

/* xícara com vapor */
function cup(x,y,s,col){
  return E(x,y+1,6*s,1.6*s,'#000',' opacity=".22"')+E(x,y,6*s,1.6*s,'#fff',INK)+D('M'+r1(x-4.6*s)+' '+r1(y-5*s)+'h'+r1(9.2*s)+'l'+r1(-1.2*s)+' '+r1(5*s)+'h'+r1(-6.8*s)+'Z',col||'#f4f0e6',INK)+E(x,y-5*s,4.6*s,1.2*s,'#6a3f1c')+S('M'+r1(x+4.6*s)+' '+r1(y-4*s)+'q'+r1(3.4*s)+' 0 '+r1(3.4*s)+' '+r1(2.4*s)+'t'+r1(-3*s)+' '+r1(2.4*s),'#f4f0e6',1.2*s)+
    S('M'+r1(x-1.4*s)+' '+r1(y-8*s)+'q-2-3 0-5t0-5','#fff',.8,' opacity=".5"')+S('M'+r1(x+1.8*s)+' '+r1(y-8*s)+'q-2-3 0-5t0-5','#fff',.8,' opacity=".4"');
}

/* mesa redonda de café com banquinhos */
function cafeTable(u,x,y,s){
  var b='';
  b+=E(x,y+13*s,22*s,4*s,'#000',' opacity=".26"');
  b+=R(x-1.6*s,y,3.2*s,13*s,'#3a2a1a')+E(x,y+13*s,8*s,1.6*s,'#3a2a1a')+E(x,y,20*s,5*s,'#8a5c38',INK)+E(x,y-1*s,20*s,4.4*s,'#a87448')+S('M'+r1(x-16*s)+' '+r1(y-1*s)+'Q'+x+' '+r1(y+2*s)+' '+r1(x+16*s)+' '+r1(y-2*s),'#6d4a30',.5,' opacity=".5"');
  b+=cup(x-7*s,y-1*s,.9*s,'#f4f0e6')+cup(x+8*s,y-2*s,.9*s,'#e8b4a0');
  b+=E(x-1*s,y-5*s,5*s,1.4*s,'#fff',INK)+C(x-1*s,y-6.6*s,2*s,'#d9a441',INK);
  [[-26,18],[26,18]].forEach(function(p){b+=E(x+p[0]*s,y+p[1]*s+10*s,10*s,2.4*s,'#000',' opacity=".22"')+R(x+p[0]*s-1.6*s,y+p[1]*s,3.2*s,10*s,'#3a2a1a')+E(x+p[0]*s,y+p[1]*s,10*s,3.2*s,'#b8423a',INK)+E(x+p[0]*s,y+p[1]*s-1*s,9*s,2.6*s,'#d9564a');});
  return b;
}

/* ---------- SHOP: mercadinho ---------- */
reg('shop',function(u){
  var r=rng(6606),d='',b='',i;
  d+=LG(u,'wl',0,0,0,150,[[0,'#f0d9b0'],[1,'#e2bf8a']]);
  d+=RG(u,'gl',240,70,260,[[0,'#fff0c0',.5],[1,'#fff0c0',0]]);
  d+=vig(u);
  var fl=checkerFloor(u,154,112,'#f1e4cc','#c9794a',44,'#7a4a2a');
  var wall=R(0,0,480,154,'url(#'+u+'-wl)');
  for(i=0;i<480;i+=20)wall+=R(i,26,9,128,'#fff',' opacity=".05"');
  wall+=R(0,0,480,28,'#7a4a2a')+R(0,24,480,5,'#caa05a',INK)+R(0,28,480,3,'#000',' opacity=".18"');
  for(i=0;i<480;i+=40)wall+=R(i+3,4,34,16,'none',' stroke="#caa05a" stroke-width=".7" opacity=".6"');
  wall+=R(0,150,480,8,'#6a4224',INK)+R(0,150,480,1.4,'#e0b784',' opacity=".7"');
  /* letreiro */
  b+=R(166,32,148,22,'#2a1c14',INK)+R(168,34,144,18,'none',' stroke="#e6c35c" stroke-width=".8"')+T(240,48,'GENERAL STORE',11,'#f1d88c',{a:'middle',w:'bold',ls:'1.6'});
  b+=L(180,24,180,32,'#333',1)+L(300,24,300,32,'#333',1);
  /* prateleiras */
  b+=goods(20,60,128,88,1)+goods(332,60,128,88,2);
  b+=goods(166,62,148,28,3);
  /* balcão central */
  b+=E(240,176,112,6,'#000',' opacity=".3"');
  b+=P('140,128 340,128 350,138 130,138','#e6cfa6',INK)+R(130,138,220,36,'#7a4a2a',INK);
  for(i=134;i<346;i+=14)b+=R(i,142,11,26,'none',' stroke="#caa05a" stroke-width=".6" opacity=".55"')+R(i,142,11,26,'#000',' opacity=".1"');
  b+=R(130,138,220,1.6,'#e0b784',' opacity=".7"')+R(130,170,220,4,'#2a1c12')+R(130,138,220,2,'#000',' opacity=".18"');
  /* caixa registradora + balança + sacola + sino */
  b+=RR(272,110,40,24,3,'#3a4a5a',INK)+R(276,114,32,9,'#0d2a20',INK)+T(292,121,'$ 4.50',6,'#8affb0',{a:'middle',w:'bold',f:'Arial'})+R(276,126,32,6,'#c9d2da',INK);
  for(i=0;i<5;i++)b+=R(279+i*6,127.4,4,3.2,'#6a7a8a');
  b+=R(244,122,22,6,'#caa05a',INK)+C(255,118,10,'#f4f0e6',INK)+S('M255 118l5-5','#d94f3d',1)+RR(150,112,24,18,3,'#d9b98a',INK)+S('M154 112q8-8 16 0','#a8895a',1.4)+E(200,128,6,1.6,'#a37d30')+D('M194 127.8q0-8 6-8t6 8Z','#e0b74e',INK);
  /* cestas de frutas e flores */
  [[60,166,'#d94f3d','#79b06a'],[420,166,'#e8b948','#e58a3f']].forEach(function(c,k){
    b+=E(c[0],c[1]+12,26,4,'#000',' opacity=".25"')+D('M'+(c[0]-22)+' '+c[1]+'h44l-4 18h-36Z','#a8723f',INK);
    for(i=0;i<5;i++)b+=L(c[0]-20+i*10,c[1]+1,c[0]-17+i*9,c[1]+17,'#6a4624',.6,' opacity=".6"');
    for(i=0;i<7;i++)b+=C(c[0]-16+i*5.4,c[1]-3-((i*5)%5),5,i%2?c[2]:c[3],INK)+C(c[0]-17.6+i*5.4,c[1]-5-((i*5)%5),1.6,'#fff',' opacity=".5"');
  });
  /* plantas, placas e lâmpadas */
  b+=SF.plantFull(u,24,164,.8,4,['#c9824f','#a8683c']);
  [[92,0],[388,0]].forEach(function(p,k){var pd=SF.pendant(u,'pd'+k,p[0],28,46,'#ffd88a');d+=pd.d;b+=pd.b;});
  b+=R(40,30,40,18,'#f6efdc',INK)+T(60,43,'SALE',9,'#d94f3d',{a:'middle',w:'bold',f:'Arial'})+R(400,30,40,18,'#f6efdc',INK)+T(420,43,'OPEN',9,'#2f8f5a',{a:'middle',w:'bold',f:'Arial'});
  b+=R(0,0,480,154,'url(#'+u+'-gl)')+SF.motes(r,16,0,30,480,150);
  return WRAP(u,d,fl+wall+b);
});

/* ---------- DINER: lanchonete retrô à noite ---------- */
reg('diner',function(u){
  var r=rng(7707),d='',b='',i;
  d+=LG(u,'wl',0,0,0,150,[[0,'#1f6f78'],[1,'#17525a']]);
  d+=LG(u,'ns',0,40,0,124,[[0,'#0d1a40'],[1,'#26356a']]);
  d+=RG(u,'ne',380,46,120,[[0,'#ff4a5a',.55],[0.5,'#ff4a5a',.16],[1,'#ff4a5a',0]]);
  d+=RG(u,'nb',130,60,110,[[0,'#4ad8ff',.4],[1,'#4ad8ff',0]]);
  d+=vig(u);
  var fl=checkerFloor(u,156,114,'#f1ece0','#1e2430',42,'#000');
  var wall=R(0,0,480,156,'url(#'+u+'-wl)');
  for(i=0;i<480;i+=16)wall+=R(i,0,.8,156,'#000',' opacity=".14"');
  wall+=R(0,104,480,6,'#d33a46',INK)+R(0,110,480,46,'#e8e2d2')+R(0,104,480,1.4,'#ff8a92',' opacity=".8"');
  for(i=0;i<480;i+=18)wall+=R(i,111,9,44,'#fff',' opacity=".28"')+L(i,111,i,155,'#9a9484',.4,' opacity=".4"');
  wall+=R(0,152,480,6,'#c0c4cc',INK)+R(0,152,480,1.4,'#fff',' opacity=".9"');
  /* janela com a cidade à noite */
  b+=R(40,28,170,70,'#c8ccd4',INK)+R(44,32,162,62,'url(#'+u+'-ns)');
  for(i=0;i<14;i++){var bh=14+r()*38,bw=10+r()*10,bx=44+i*12;b+=R(bx,94-bh,bw,bh,'#1a2450',' opacity=".95"');for(var q=0;q<Math.floor(bh/6);q++)for(var m=0;m<2;m++)if(r()>.42)b+=R(bx+2+m*5,94-bh+3+q*6,2.4,2.8,'#ffd47a',' opacity="'+r1(.5+r()*.5)+'"');}
  b+=C(190,48,6,'#fff6d0',' opacity=".9"')+C(190,48,12,'#fff6d0',' opacity=".2"');
  b+=R(124,32,3,62,'#c8ccd4',INK)+R(44,62,162,3,'#c8ccd4',INK)+P('44,32 90,32 66,94 44,94','#fff',' opacity=".12"');
  b+=T(125,80,'DINER',13,'#4ad8ff',{a:'middle',w:'bold',ls:'3',f:'Arial Black,Arial,sans-serif'});
  b+=T(125,80,'DINER',13,'#bff3ff',{a:'middle',w:'bold',ls:'3',f:'Arial Black,Arial,sans-serif'}).replace('fill="#bff3ff"','fill="none" stroke="#fff" stroke-width=".6"');
  b+=R(0,0,480,156,'url(#'+u+'-nb)');
  /* neon OPEN + moldura */
  b+=R(300,30,134,50,'#0e0e16',INK)+R(304,34,126,42,'none',' stroke="#ff4a5a" stroke-width="2.4"')+R(304,34,126,42,'none',' stroke="#fff" stroke-width=".6" opacity=".6"')+
     T(367,66,'OPEN',26,'#ff5a68',{a:'middle',w:'bold',ls:'4',f:'Arial Black,Arial,sans-serif'})+T(367,66,'OPEN',26,'#ffd0d4',{a:'middle',w:'bold',ls:'4',f:'Arial Black,Arial,sans-serif'}).replace('fill="#ffd0d4"','fill="none" stroke="#fff" stroke-width=".7"');
  b+=R(0,0,480,156,'url(#'+u+'-ne)');
  /* relógio e quadro de cardápio */
  b+=SF.clock(u,260,50,12,6,25);
  b+=R(224,74,104,24,'#17120e',INK);for(i=0;i<3;i++)b+=T(232,84+i*6.4,['Burger ....... $5','Milkshake .... $3','Apple Pie .... $2'][i],4.6,'#f1e7c8',{f:'Arial',w:'bold'});
  /* jukebox */
  b+=E(448,162,20,3,'#000',' opacity=".3"')+D('M430 160V104Q430 86 448 86T466 104V160Z','#d9564a',INK)+D('M434 160V106Q434 92 448 92T462 106V160Z','#ffd47a',' opacity=".9"')+R(436,112,24,16,'#1a1a22',INK)+R(438,114,20,5,'#4ad8ff',' opacity=".8"')+R(438,122,20,4,'#ff4a5a',' opacity=".7"')+R(436,134,24,20,'#c8ccd4',INK)+C(448,144,6,'#222',INK)+C(448,144,2,'#c8ccd4');
  /* balcão com banquetas cromadas */
  b+=E(176,206,118,6,'#000',' opacity=".26"');
  b+=R(60,170,232,5,'#e8e2d2',INK)+R(60,175,232,26,'#d33a46',INK)+R(60,175,232,2,'#ff8a92',' opacity=".8"')+R(60,196,232,5,'#b8bcc4',INK);
  for(i=64;i<288;i+=16)b+=R(i,178,1,18,'#000',' opacity=".14"');
  [[84],[132],[180],[228]].forEach(function(p){var x=p[0];b+=E(x,214,9,2,'#000',' opacity=".25"')+R(x-1.4,196,2.8,18,'#b8bcc4',INK)+E(x,214,8,2,'#b8bcc4',INK)+E(x,193,12,4,'#d33a46',INK)+E(x,191.6,11,3.2,'#ef5a66')+R(x-12,193,24,3,'#b53040',INK);});
  /* sobre o balcão: torta, milkshake, hambúrguer */
  b+=E(110,170,16,3,'#f4f0e6',INK)+D('M96 170q14-20 28 0Z','#d9a050',INK)+S('M100 166l10-6l8 6','#8a5a2a',.8)+
     D('M190 170l4-22h10l4 22Z','#f6efe0',INK)+E(199,148,6,2,'#f08aa0')+C(199,144,3,'#e8503a',INK)+S('M203 144l6-8','#fff',1)+
     E(244,170,16,3.4,'#fff',INK)+E(244,166,10,4,'#d9a050',INK)+E(244,162,10,3,'#79b06a')+E(244,159,10,3,'#8a3a2a')+E(244,156,10,3.4,'#d9a050',INK);
  b+=SF.motes(r,14,0,20,480,160);
  return WRAP(u,d,fl+wall+b);
});

/* ---------- CAFE2: café ao entardecer com janela ---------- */
reg('cafe2',function(u){
  var r=rng(8808),d='',b='',i;
  d+=LG(u,'wl',0,0,0,150,[[0,'#7a4a30'],[1,'#5a3422']]);
  d+=LG(u,'sk',0,34,0,108,[[0,'#6a82b8'],[0.4,'#b79ac0'],[0.75,'#f1b48a'],[1,'#fcd8a0']]);
  d+=RG(u,'wg',200,80,200,[[0,'#ffcf94',.55],[1,'#ffb066',0]]);
  d+=vig(u);
  var pq=(function(){var s='',n=26,k=(158-114)/(270-114),j;s+=R(0,158,480,112,'#a8723f');for(j=-n;j<n;j++){s+=P(r1(240+j*34*k)+',158 '+r1(240+(j+1)*34*k)+',158 '+r1(240+(j+1)*34)+',270 '+r1(240+j*34)+',270',['#b9824f','#a8723f','#c8915e','#9a6638'][((j%4)+4)%4],' opacity=".85"')+L(r1(240+j*34*k),158,r1(240+j*34),270,'#5a3a1e',.7,' opacity=".4"');}return s;})();
  var wall=R(0,0,480,158,'url(#'+u+'-wl)');
  for(i=0;i<480;i+=11)wall+=R(i,0,5,158,'#000',' opacity=".06"')+R(i+5,0,1,158,'#fff',' opacity=".05"');
  /* tijolinhos baixos */
  for(var rr=0;rr<5;rr++)for(i=0;i<480;i+=24)wall+=R(i+(rr%2)*12,118+rr*7,22,5.4,'#7a4a34',' opacity=".5"');
  wall+=R(0,150,480,8,'#2a1c12',INK)+R(0,150,480,1.4,'#8a6444',' opacity=".7"');
  /* janelão com a cidade */
  b+=R(120,28,240,86,'#2a1c12',INK)+R(126,34,228,74,'url(#'+u+'-sk)');
  for(i=0;i<20;i++){var bh=14+r()*40,bw=9+r()*8,bx=126+i*11.6;b+=R(bx,108-bh,bw,bh,'rgb('+(86+Math.floor(r()*26))+','+(86+Math.floor(r()*22))+','+(122+Math.floor(r()*26))+')',' opacity=".9"');for(var q=0;q<Math.floor(bh/6);q++)for(var m=0;m<2;m++)if(r()>.5)b+=R(bx+2+m*4,108-bh+3+q*6,2,2.6,'#ffd97a',' opacity="'+r1(.5+r()*.5)+'"');}
  b+=C(300,76,9,'#fff0c0',' opacity=".8"')+C(300,76,20,'#fff0c0',' opacity=".2"');
  for(i=0;i<3;i++)b+=R(126+(i+1)*57-1.4,34,2.8,74,'#2a1c12',INK);
  b+=R(126,70,228,2.8,'#2a1c12',INK)+P('126,34 186,34 154,108 126,108','#fff',' opacity=".13"');
  b+=R(114,114,252,6,'#6d4a30',INK)+R(114,114,252,1.4,'#e0b784',' opacity=".6"');
  b+=R(0,0,480,158,'url(#'+u+'-wg)');
  /* prateleira de xícaras e quadros */
  b+=R(18,64,84,4,'#6d4a30',INK);for(i=0;i<7;i++)b+=cup(26+i*11,64,.7,['#f4f0e6','#e8b4a0','#a8c8d8'][i%3]).replace(/<path d="M[^"]*" fill="none"[^>]*stroke-width="[^"]*"[^>]*opacity="\.[45]"\/>/g,'');
  b+=R(18,92,84,4,'#6d4a30',INK);for(i=0;i<5;i++)b+=RR(24+i*15,76,10,16,2,['#d94f3d','#e8b948','#2f8fb8','#79b06a','#8c6aa6'][i],INK)+R(24+i*15,78,10,2,'#fff',' opacity=".5"');
  b+=SF.frame(u,388,50,40,50,'abs',4)+SF.frame(u,388+0,108,40,0.1,'abs',5).replace(/.*/,'');
  /* balcão à direita */
  b+=E(422,176,56,5,'#000',' opacity=".28"')+R(376,134,92,6,'#e6cfa6',INK)+R(376,140,92,34,'#5a3422',INK);
  for(i=380;i<466;i+=11)b+=R(i,144,8,26,'none',' stroke="#caa05a" stroke-width=".6" opacity=".5"');
  b+=RR(398,112,38,22,3,'#9aa3ac',INK)+R(402,116,12,6,'#222')+C(424,126,4,'#e8503a')+R(402,128,30,3,'#2a2f35')+RR(440,118,16,16,2,'#f4f0e6',INK);
  /* mesas e pendentes */
  b+=cafeTable(u,160,176,1.05)+cafeTable(u,300,196,1.25);
  [[110],[240],[360]].forEach(function(p,k){var pd=SF.pendant(u,'pd'+k,p[0],0,38+(k%2)*6,'#ffd88a');d+=pd.d;b+=pd.b;});
  b+=SF.plantFull(u,40,164,.85,8,['#c9824f','#a8683c']);
  b+=SF.motes(r,18,0,20,480,160);
  return WRAP(u,d,pq+wall+b);
});

/* ---------- CAFE3: balcão do café, cardápio e vitrine ---------- */
reg('cafe3',function(u){
  var r=rng(9909),d='',b='',i;
  d+=LG(u,'wl',0,0,0,150,[[0,'#6a4430'],[1,'#4a2c1e']]);
  d+=RG(u,'lg',240,80,240,[[0,'#ffd88a',.45],[1,'#ffd88a',0]]);
  d+=vig(u);
  var wall=R(0,0,480,270,'url(#'+u+'-wl)');
  for(i=0;i<480;i+=11)wall+=R(i,0,5,270,'#000',' opacity=".06"');
  /* cardápio de giz */
  b+=R(150,22,180,92,'#5a3a24',INK)+R(155,27,170,82,'#1d2b26')+R(155,27,170,3,'#000',' opacity=".3"')+P('155,27 210,27 188,109 155,109','#fff',' opacity=".05"');
  b+=T(240,44,'MENU',11,'#f6efd8',{a:'middle',w:'bold',ls:'3',f:'Segoe Script,cursive'})+S('M178 50h124','#f6efd8',.8,' opacity=".6"');
  [['Coffee','$2'],['Latte','$3'],['Tea','$2'],['Cake','$4'],['Juice','$3']].forEach(function(it,k){b+=T(170,64+k*9,it[0],6.6,'#fbe9a0',{f:'Segoe Script,cursive'})+T(310,64+k*9,it[1],6.6,'#cfe9f3',{a:'end',f:'Segoe Script,cursive'})+S('M196 '+(63+k*9)+'h96','#f6efd8',.4,' opacity=".25" stroke-dasharray="1 2"');});
  b+=C(300,38,5,'none',' stroke="#fbe9a0" stroke-width="1"')+S('M297 39q3 3 6 0','#fbe9a0',.8);
  /* prateleiras laterais com xícaras e garrafas */
  [[20,70],[372,70]].forEach(function(p,k){var x=p[0],y=p[1];b+=R(x,y,88,4,'#7a5230',INK)+R(x,y+30,88,4,'#7a5230',INK)+R(x,y+60,88,4,'#7a5230',INK);
    for(i=0;i<6;i++)b+=cup(x+8+i*14,y+0,.72,['#f4f0e6','#e8b4a0','#a8c8d8'][(i+k)%3]).replace(/<path d="M[^"]*" fill="none"[^>]*stroke-width="[^"]*"[^>]*opacity="\.[45]"\/>/g,'');
    for(i=0;i<5;i++)b+=RR(x+8+i*16,y+8,9,22,2,['#8a4a2a','#d9a441','#4f8a5b','#7a3a2a','#2f6f8f'][(i+k)%5],INK)+R(x+10+i*16,y-3+8,5,6,'#d9d2c0',INK)+R(x+9+i*16,y+16,7,6,'#f4efe0',' opacity=".8"');
    for(i=0;i<6;i++)b+=RR(x+6+i*13,y+40,9,20,2,['#d94f3d','#e8b948','#f4f0e6'][(i+k)%3],INK)+R(x+6+i*13,y+44,9,3,'#fff',' opacity=".5"');
  });
  /* máquina de espresso */
  b+=E(240,168,70,5,'#000',' opacity=".3"')+RR(190,118,100,50,5,'#b8bec6',INK)+RR(194,122,92,16,3,'#2a2f35',INK)+R(198,126,84,8,'#3a424a')+C(212,130,3,'#e8503a')+C(224,130,3,'#79b06a')+R(240,125,40,10,'#1a1d22')+T(260,132.4,'ESPRESSO',5,'#ffcf6a',{a:'middle',w:'bold',f:'Arial'})+
     R(210,142,6,20,'#6a727a',INK)+R(264,142,6,20,'#6a727a',INK)+cup(213,166,.9,'#f4f0e6')+cup(267,166,.9,'#f4f0e6')+R(194,122,92,3,'#fff',' opacity=".35"');
  /* vitrine de doces */
  b+=R(20,150,440,6,'#e6cfa6',INK)+R(20,156,440,56,'#5a3422',INK);
  for(i=24;i<456;i+=16)b+=R(i,160,12,46,'none',' stroke="#caa05a" stroke-width=".6" opacity=".5"');
  b+=RR(40,126,128,26,3,'#cfe9f3',INK)+R(40,126,128,3,'#fff',' opacity=".6"')+P('44,128 80,128 62,150 44,150','#fff',' opacity=".25"');
  [[56,'#e0a45a'],[84,'#f08aa0'],[112,'#8a4a2a'],[140,'#f4d79a']].forEach(function(c,k){b+=E(c[0],146,11,3.4,'#f4f0e6',INK)+D('M'+(c[0]-9)+' 146q9-'+(10+(k%2)*3)+' 18 0Z',c[1],INK)+C(c[0],138-(k%2)*2,1.8,k%2?'#d94f3d':'#fff',INK)+S('M'+(c[0]-5)+' 144q5-4 10 0','#fff',.6,' opacity=".5"');});
  b+=RR(330,128,100,24,3,'#cfe9f3',INK)+R(330,128,100,3,'#fff',' opacity=".6"');
  [[346,'#d9a050'],[370,'#c98a58'],[394,'#e8c07a'],[418,'#d9a050']].forEach(function(c,k){b+=D('M'+(c[0]-8)+' 150q-4-14 8-16q12 2 8 16Z',c[1],INK)+S('M'+(c[0]-3)+' 143q3-2 6 0','#8a5a2a',.8)+S('M'+(c[0]-5)+' 147q5-3 10 0','#8a5a2a',.8);});
  /* caixa registradora, sino e pote de gorjetas */
  b+=RR(300,160,40,22,3,'#3a4a5a',INK)+R(304,164,32,8,'#0d2a20',INK)+T(320,170.4,'OPEN',5.6,'#8affb0',{a:'middle',w:'bold',f:'Arial'})+E(360,182,7,1.8,'#a37d30')+D('M353 181.8q0-8 7-8t7 8Z','#e0b74e',INK)+RR(392,166,14,16,2,'#cfe9f3',INK)+C(398,172,2.2,'#e6c35c')+C(401,175,2.2,'#e6c35c');
  [[70],[410]].forEach(function(p,k){var pd=SF.pendant(u,'pd'+k,p[0],0,40,'#ffd88a');d+=pd.d;b+=pd.b;});
  b+=R(0,0,480,270,'url(#'+u+'-lg)');
  b+=R(0,212,480,58,'#2a1a10')+R(0,212,480,2,'#caa05a',' opacity=".7"');
  for(i=0;i<480;i+=40)b+=R(i,214,1,56,'#000',' opacity=".3"');
  b+=SF.motes(r,16,0,20,480,200);
  return WRAP(u,d,wall+b);
});
})();
