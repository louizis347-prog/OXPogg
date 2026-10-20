/* scn_fine3.js - cenários externos refinados: rua, parque e quintal. Usa window.SF de scn_fine.js. */
(function(){
if(!window.SF||!window.RS)return;
var SF=window.SF;
var rng=SF.rng,r1=SF.r1,LG=SF.LG,RG=SF.RG,R=SF.R,RR=SF.RR,E=SF.E,C=SF.C,L=SF.L,P=SF.P,D=SF.D,S=SF.S,T=SF.T,G=SF.G,INK=SF.INK,WRAP=SF.WRAP,vig=SF.vig,reg=SF.reg;

/* ---------- peças ---------- */

/* copa de árvore em camadas: sombra, massa escura, tufos médios e luzes, com tronco e galhos */
function tree(u,x,y,s,seed,pal){
  var r=rng(seed),b='',i,n=34;
  b+=E(x,y+2,30*s,5*s,'#000',' opacity=".2"');
  b+=D('M'+r1(x-5*s)+' '+y+'Q'+r1(x-3*s)+' '+r1(y-26*s)+' '+r1(x-2*s)+' '+r1(y-46*s)+'L'+r1(x+3*s)+' '+r1(y-46*s)+'Q'+r1(x+4*s)+' '+r1(y-24*s)+' '+r1(x+6*s)+' '+y+'Z','#5a3a24',INK)+
    S('M'+x+' '+r1(y-30*s)+'Q'+r1(x-14*s)+' '+r1(y-42*s)+' '+r1(x-22*s)+' '+r1(y-58*s),'#5a3a24',2.2*s)+S('M'+x+' '+r1(y-36*s)+'Q'+r1(x+14*s)+' '+r1(y-48*s)+' '+r1(x+22*s)+' '+r1(y-62*s),'#5a3a24',2*s)+
    S('M'+r1(x-1*s)+' '+r1(y-2*s)+'Q'+r1(x-1*s)+' '+r1(y-22*s)+' '+r1(x)+' '+r1(y-44*s),'#2a1608',.6,' opacity=".4"');
  var cx=x,cy=y-66*s;
  for(i=0;i<n;i++){var a=r()*Math.PI*2,d=Math.sqrt(r()),rx=cx+Math.cos(a)*d*34*s,ry=cy+Math.sin(a)*d*24*s,rad=(8+r()*10)*s;b+=C(rx,ry,rad,pal[0]);}
  for(i=0;i<n;i++){var a2=r()*Math.PI*2,d2=Math.sqrt(r()),rx2=cx+Math.cos(a2)*d2*30*s-2*s,ry2=cy+Math.sin(a2)*d2*20*s-3*s,rad2=(5+r()*8)*s;b+=C(rx2,ry2,rad2,pal[1],' opacity=".9"');}
  for(i=0;i<22;i++){var a3=r()*Math.PI*2,d3=Math.sqrt(r()),rx3=cx+Math.cos(a3)*d3*24*s-6*s,ry3=cy+Math.sin(a3)*d3*15*s-8*s,rad3=(3+r()*5)*s;b+=C(rx3,ry3,rad3,pal[2],' opacity=".85"');}
  for(i=0;i<16;i++){b+=C(cx+(r()-.5)*58*s,cy+(r()-.5)*40*s,.9+r()*1.2,pal[3],' opacity=".8"');}
  b+=E(cx-8*s,cy-12*s,18*s,9*s,'#fff',' opacity=".05"');
  return b;
}

/* poste de rua com luminária e halo */
function lampPost(u,id,x,y,s,warm,on){
  var d=RG(u,id,x,y-64*s,40*s,[[0,warm,on?.7:.0],[0.5,warm,on?.2:0],[1,warm,0]]),b='';
  b+=E(x,y+1,7*s,1.6*s,'#000',' opacity=".25"');
  b+=C(x,y-64*s,40*s,'url(#'+u+'-'+id+')');
  b+=R(x-2*s,y-60*s,4*s,60*s,'#2e3a3a',INK)+R(x-4*s,y-6*s,8*s,6*s,'#2e3a3a',INK)+R(x-3*s,y-12*s,6*s,2*s,'#4f5f5f')+
     S('M'+r1(x)+' '+r1(y-60*s)+'q0-8 '+r1(8*s)+'-8','#2e3a3a',2.4*s)+
     D('M'+r1(x+4*s)+' '+r1(y-70*s)+'h'+r1(11*s)+'l'+r1(-2*s)+' '+r1(8*s)+'h'+r1(-7*s)+'Z','#2e3a3a',INK)+C(x+9.5*s,y-62*s,3*s,on?'#fff3c8':'#cfd8d8',INK);
  return {d:d,b:b};
}

/* toldo listrado com festão */
function awning(x,y,w,c1,c2){
  var b='',n=Math.round(w/9),sw=w/n,i;
  b+=R(x,y,w,13,'#fff')+P(r1(x-2)+','+y+' '+r1(x+w+2)+','+y+' '+r1(x+w+5)+','+r1(y+13)+' '+r1(x-5)+','+r1(y+13),c1,INK);
  for(i=0;i<n;i+=2)b+=P(r1(x+i*sw)+','+y+' '+r1(x+(i+1)*sw)+','+y+' '+r1(x+(i+1)*sw+1)+','+r1(y+13)+' '+r1(x+i*sw-1)+','+r1(y+13),c2);
  for(i=0;i<n;i++)b+=D('M'+r1(x-5+i*(w+10)/n)+' '+r1(y+13)+'q'+r1((w+10)/n/2)+' 6 '+r1((w+10)/n)+' 0',i%2?c1:c2,INK);
  b+=R(x-2,y,w+4,2,'#fff',' opacity=".35"');
  return b;
}

/* fachada com janelas, parapeito e detalhes; devolve markup */
function facade(u,x,y,w,h,base,trim,seed,lit){
  var r=rng(seed),b='',i,j;
  b+=R(x,y,w,h,base,INK)+R(x,y,w,5,trim,INK)+R(x,y+5,w,2,'#000',' opacity=".14"')+R(x-2,y-3,w+4,4,trim,INK)+R(x-2,y-3,w+4,1,'#fff',' opacity=".5"');
  for(i=0;i<Math.floor(h/14);i++)b+=L(x,y+10+i*14,x+w,y+10+i*14,'#000',.4,' opacity=".07"');
  var cols=Math.max(1,Math.floor((w-10)/22)),rows=Math.max(1,Math.floor((h-48)/30)),gx=(w-cols*14)/(cols+1);
  for(j=0;j<rows;j++)for(i=0;i<cols;i++){
    var wx=x+gx+i*(14+gx),wy=y+14+j*30,on=lit&&r()>.45;
    b+=R(wx-2,wy-2,18,24,trim,INK)+R(wx,wy,14,20,on?'#ffd47a':'#7d9db4')+(on?R(wx,wy,14,20,'#fff',' opacity=".12"'):D('M'+wx+' '+(wy+20)+'L'+wx+' '+(wy+8)+'L'+(wx+8)+' '+wy+'L'+(wx+14)+' '+wy+'L'+(wx+14)+' '+(wy+6)+'L'+(wx+6)+' '+(wy+20)+'Z','#fff',' opacity=".2"'))+
       R(wx+6.4,wy,1.2,20,trim)+R(wx,wy+9.4,14,1.2,trim)+R(wx-3,wy+20,20,3,trim,INK)+R(wx-3,wy+20,20,.8,'#fff',' opacity=".6"');
    if(r()>.7)b+=R(wx+1,wy+1,6,19,['#c98a6a','#e8d4a8','#a8b8d4'][Math.floor(r()*3)],' opacity=".7"');
    if(r()>.78)b+=R(wx-1,wy+23,16,3.4,'#6d4a30',INK)+C(wx+3,wy+22,2.4,'#4f8a5b')+C(wx+8,wy+21,2.6,'#e2825f')+C(wx+12,wy+22,2.2,'#4f8a5b');
  }
  return b;
}

/* pedestre de silhueta refinada */
function walker(x,y,s,coat,pants,hair,skin,flip){
  var b='',f=flip?-1:1;
  b+=E(x,y+1,9*s,2*s,'#000',' opacity=".24"');
  b+=R(x-4*s,y-18*s,3.4*s,18*s,pants,INK)+R(x+.8*s,y-18*s,3.4*s,18*s,pants,INK)+R(x-4.6*s,y-2*s,4.6*s,2.4*s,'#2a1c14')+R(x+.4*s,y-2*s,4.6*s,2.4*s,'#2a1c14');
  b+=RR(x-6*s,y-38*s,12*s,22*s,4*s,coat,INK)+RR(x-5*s,y-37*s,4*s,18*s,2*s,'#fff',' opacity=".14"');
  b+=R(x-8.2*s,y-36*s,3*s,15*s,coat,INK)+R(x+5.2*s,y-36*s,3*s,15*s,coat,INK)+C(x-6.6*s,y-20.4*s,1.8*s,skin)+C(x+6.6*s,y-20.4*s,1.8*s,skin);
  b+=R(x-1.6*s,y-41*s,3.2*s,4*s,skin)+C(x,y-46*s,5.4*s,skin,INK)+D('M'+r1(x-5.8*s)+' '+r1(y-46*s)+'q0-8 '+r1(5.8*s)+'-8t'+r1(5.8*s)+' 8q-'+r1(2*s)+' -4 -'+r1(5.8*s)+' -3t-'+r1(5.8*s)+' 3Z',hair,INK);
  return b;
}

/* ---------- STREET ---------- */
reg('street',function(u){
  var r=rng(3303),d='',b='',i;
  d+=LG(u,'sk',0,0,0,150,[[0,'#7fb2dc'],[0.55,'#cfe4ee'],[1,'#fbe6c2']]);
  d+=LG(u,'sw',0,176,0,206,[[0,'#d8cfbd'],[1,'#c4b9a4']]);
  d+=LG(u,'rd',0,206,0,270,[[0,'#59606b'],[1,'#454b55']]);
  d+=RG(u,'sn',380,48,170,[[0,'#fff5cf',.8],[1,'#fff5cf',0]]);
  d+=vig(u);
  /* céu, nuvens e prédios distantes */
  b+=R(0,0,480,176,'url(#'+u+'-sk)')+R(0,0,480,176,'url(#'+u+'-sn)');
  b+=E(90,34,48,7,'#fff',' opacity=".85"')+E(120,28,30,6,'#fff',' opacity=".9"')+E(300,52,60,8,'#fff',' opacity=".7"')+E(330,46,34,6,'#fff',' opacity=".8"');
  for(i=0;i<14;i++){var bh=40+r()*50,bw=22+r()*20,bx=i*36-8;b+=R(bx,150-bh,bw,bh,'#a6b4c8',' opacity=".55"')+R(bx,150-bh,bw,3,'#fff',' opacity=".25"');}
  /* fachadas */
  var fa=[[6,40,96,114,'#e0a15a','#fff1d6'],[104,26,90,128,'#c4513a','#f3e6cf'],[196,48,100,106,'#5d8a9c','#eaf1f0'],[298,30,88,124,'#e5c66a','#fff6df'],[388,44,98,110,'#8c6aa6','#f1e7f5']];
  fa.forEach(function(f,k){b+=facade(u,f[0],f[1],f[2],f[3],f[4],f[5],k+11,true);});
  /* lojas no térreo: vitrines, portas, toldos, placas */
  var sh=[[10,'CAFÉ','#d94f3d','#fff4de'],[108,'BOOKS','#2f6f8f','#fff4de'],[200,'BAKERY','#e8a23a','#fff4de'],[302,'FLOWERS','#4f8a5b','#fff4de'],[392,'MARKET','#8c4a7a','#fff4de']];
  sh.forEach(function(s,k){
    var sx=s[0],sy=118;
    b+=R(sx,sy,86,36,'#3a2a22',INK)+R(sx+4,sy+4,50,28,'#cfe6ee')+P(r1(sx+4)+','+r1(sy+4)+' '+r1(sx+22)+','+r1(sy+4)+' '+r1(sx+10)+','+r1(sy+32)+' '+r1(sx+4)+','+r1(sy+32),'#fff',' opacity=".25"');
    b+=R(sx+60,sy+6,20,30,'#5a3a24',INK)+R(sx+63,sy+10,14,12,'#cfe6ee')+C(sx+77,sy+24,1.2,'#e6c35c');
    b+=R(sx+8,sy+22,42,10,'#000',' opacity=".12"');
    if(k===0)b+=R(sx+10,sy+18,10,8,'#fff',INK)+R(sx+24,sy+18,10,8,'#fff',INK)+C(sx+15,sy+16,2,'#8a4a2a')+C(sx+29,sy+16,2,'#8a4a2a');
    if(k===1){for(i=0;i<6;i++)b+=R(sx+8+i*6.6,sy+12+(i%2)*2,5,18-(i%2)*2,['#c4513a','#e0b24a','#4f8a5b','#7a4f9a','#2f6f8f','#d9d2c0'][i],INK);}
    if(k===2)b+=E(sx+22,sy+26,14,4,'#e8c07a',INK)+E(sx+22,sy+24,12,3,'#f4d79a')+E(sx+38,sy+27,6,3,'#d99a52',INK);
    if(k===3){for(i=0;i<5;i++)b+=S('M'+r1(sx+10+i*8)+' '+(sy+30)+'v-8','#4f8a5b',1)+C(sx+10+i*8,sy+20,3.2,['#f0a0b8','#e8b948','#fff','#e2825f','#b085d9'][i],INK);}
    if(k===4){for(i=0;i<4;i++)b+=C(sx+12+i*10,sy+26,4,['#d94f3d','#e8b948','#79b06a','#e58a3f'][i],INK);}
    b+=awning(sx-1,sy-8,88,s[2],'#fff4de');
    b+=R(sx+16,sy-26,54,13,'#2a1c14',INK)+R(sx+17,sy-25,52,11,'none',' stroke="#e6c35c" stroke-width=".6"')+T(sx+43,sy-16.2,s[1],8,'#f1d88c',{a:'middle',w:'bold',ls:'1.2'});
  });
  /* calçada em perspectiva + meio-fio */
  b+=R(0,154,480,52,'url(#'+u+'-sw)')+R(0,154,480,2,'#000',' opacity=".15"');
  for(i=-4;i<14;i++)b+=L(r1(240+(i*70-240)*.55),156,r1(i*70-20),206,'#a89c85',.6,' opacity=".4"');
  [160,168,180,194,206].forEach(function(y){b+=L(0,y,480,y,'#a89c85',.6,' opacity=".35"');});
  b+=R(0,204,480,5,'#e8e0d0',INK)+R(0,208,480,2,'#000',' opacity=".2"');
  /* rua + faixas */
  b+=R(0,209,480,61,'url(#'+u+'-rd)');
  for(i=0;i<8;i++)b+=P(r1(i*66+14)+',236 '+r1(i*66+52)+',236 '+r1(i*66+56)+',241 '+r1(i*66+10)+',241','#f1e9cf',' opacity=".9"');
  for(i=0;i<12;i++)b+=L(r1(i*44),217,r1(i*44+20),217,'#d9cf9e',.9,' opacity=".6"');
  b+=R(0,250,480,20,'#000',' opacity=".12"');
  /* árvores em canteiros, postes, placa de ônibus */
  var pal=['#3f7d3d','#58a050','#7cc06a','#cfe9a0'];
  b+=tree(u,38,196,.8,31,pal)+tree(u,462,196,.8,32,pal);
  var lp1=lampPost(u,'lpa',172,206,1,'#ffd88a',false),lp2=lampPost(u,'lpb',358,206,1,'#ffd88a',false);d+=lp1.d+lp2.d;b+=lp1.b+lp2.b;
  b+=R(238,172,2.4,34,'#555',INK)+RR(228,160,22,14,3,'#2f6f8f',INK)+T(239,170.2,'BUS',7,'#fff',{a:'middle',w:'bold',f:'Arial'})+R(228,160,22,2,'#fff',' opacity=".3"');
  /* hidrante e caixa de correio */
  b+=R(206,194,7,12,'#d94f3d',INK)+RR(205,192,9,4,2,'#d94f3d',INK)+R(204,200,11,2,'#b53a2d')+RR(326,184,14,22,3,'#2f6f8f',INK)+R(328,190,10,2,'#0a2a3a')+R(328,196,10,5,'#fff',' opacity=".25"');
  /* pessoas */
  b+=walker(130,200,.95,'#c4513a','#2f4a6a','#2a1c14','#e0ac84')+walker(150,200,.85,'#4f8a5b','#3a3a4a','#7a3a1a','#f0c8a4')+walker(398,202,1,'#e0b24a','#3a3a4a','#1a1208','#b87a54',true)+walker(318,200,.9,'#2f6f8f','#5a3a2a','#c98a58','#e8b890');
  /* táxi */
  b+=taxi(u,262,254,.95);
  b+=SF.motes(r,14,0,20,480,170);
  return WRAP(u,d,b);
});

/* táxi amarelo visto de lado, com faróis, rodas e luz de teto */
function taxi(u,x,y,s){
  var b='';
  b+=E(x,y+2,66*s,6*s,'#000',' opacity=".3"');
  b+=RR(x-62*s,y-24*s,124*s,22*s,6*s,'#f4c430',INK)+D('M'+r1(x-34*s)+' '+r1(y-24*s)+'L'+r1(x-24*s)+' '+r1(y-42*s)+'H'+r1(x+26*s)+'L'+r1(x+38*s)+' '+r1(y-24*s)+'Z','#f4c430',INK);
  b+=D('M'+r1(x-30*s)+' '+r1(y-26*s)+'L'+r1(x-22*s)+' '+r1(y-39*s)+'H'+r1(x-2*s)+'V'+r1(y-26*s)+'Z','#bfe0ee',INK)+D('M'+r1(x+2*s)+' '+r1(y-26*s)+'V'+r1(y-39*s)+'H'+r1(x+24*s)+'L'+r1(x+34*s)+' '+r1(y-26*s)+'Z','#bfe0ee',INK)+
    P(r1(x-30*s)+','+r1(y-26*s)+' '+r1(x-22*s)+','+r1(y-39*s)+' '+r1(x-14*s)+','+r1(y-39*s)+' '+r1(x-22*s)+','+r1(y-26*s),'#fff',' opacity=".35"');
  b+=RR(x-10*s,y-48*s,20*s,7*s,2*s,'#fff7d6',INK)+T(x,y-42.6*s,'TAXI',5.4*s,'#3a2a14',{a:'middle',w:'bold',f:'Arial'});
  b+=R(x-62*s,y-14*s,124*s,2.4*s,'#222',' opacity=".5"')+R(x-60*s,y-24*s,120*s,3*s,'#fff',' opacity=".3"')+L(x+3*s,y-26*s,x+3*s,y-4*s,'#c99a10',.8);
  b+=R(x-60*s,y-8*s,10*s,4*s,'#fff3c8',INK)+R(x+50*s,y-9*s,11*s,5*s,'#e8503a',INK)+RR(x-24*s,y-12*s,10*s,2.4*s,1,'#8a6a10');
  [[-38,0],[40,0]].forEach(function(w){b+=C(x+w[0]*s,y+1*s,10*s,'#1c1c1c',INK)+C(x+w[0]*s,y+1*s,5.4*s,'#b8bec6')+C(x+w[0]*s,y+1*s,1.8*s,'#555');});
  return b;
}

/* ---------- PARK2 ---------- */
reg('park2',function(u){
  var r=rng(4404),d='',b='',i;
  d+=LG(u,'sk',0,0,0,130,[[0,'#6c9fd2'],[0.5,'#c9d9ec'],[0.85,'#f6d9b6'],[1,'#fbe0b0']]);
  d+=LG(u,'g1',0,128,0,270,[[0,'#7fb86a'],[0.5,'#5f9f55'],[1,'#3f7d3f']]);
  d+=LG(u,'pa',0,150,0,270,[[0,'#e6d3ac'],[1,'#c9b387']]);
  d+=RG(u,'sn',70,70,170,[[0,'#fff3c4',.8],[1,'#fff3c4',0]]);
  d+=vig(u);
  b+=R(0,0,480,140,'url(#'+u+'-sk)')+R(0,0,480,140,'url(#'+u+'-sn)');
  b+=E(330,34,60,7,'#fff',' opacity=".85"')+E(364,28,34,6,'#fff',' opacity=".9"')+E(120,58,50,6,'#fff',' opacity=".7"');
  /* skyline distante em névoa */
  for(i=0;i<16;i++){var bh=18+r()*40,bw=14+r()*14,bx=i*30-4;b+=R(bx,130-bh,bw,bh,'#a8b6cc',' opacity=".5"')+R(bx,130-bh,bw,2,'#fff',' opacity=".3"');}
  /* colinas em camadas */
  b+=D('M0 140Q70 112 150 132T300 128T480 136V270H0Z','#8ec27a',INK)+D('M0 152Q90 130 190 148T380 142T480 150V270H0Z','url(#'+u+'-g1)');
  /* grama: tufos finos */
  for(i=0;i<150;i++){var gx=r()*480,gy=150+r()*120;b+=S('M'+r1(gx)+' '+r1(gy)+'q-1-4 -3-6M'+r1(gx)+' '+r1(gy)+'q0-5 1-7','#3f7d3f',.5,' opacity="'+r1(.25+r()*.4)+'"');}
  /* caminho em perspectiva com pavers */
  b+=D('M200 150Q236 170 218 200T180 270H430Q330 230 290 190T262 150Z','url(#'+u+'-pa)',INK);
  b+=S('M232 160Q252 180 238 204T214 270','#fff',1.2,' opacity=".25"');
  for(i=0;i<9;i++){var py=162+i*12;b+=S('M'+r1(214-i*(i>4?1:0)*.5)+' '+py+'q'+r1(36+i*7)+' -3 '+r1(60+i*14)+' 0','#b8a278',.6,' opacity=".5"');}
  /* flores */
  var fc=['#f0a0b8','#fff3d8','#e8b948','#b085d9','#e2825f'];
  for(i=0;i<60;i++){var fx=r()*480,fy=162+r()*100;if(fx>190&&fx<430&&fy<200)continue;b+=S('M'+r1(fx)+' '+r1(fy)+'v5','#4f8a5b',.6)+C(fx,fy,1.5+r()*1.2,fc[Math.floor(r()*5)],' opacity=".95"');}
  /* árvores */
  var pal=['#3f7d3d','#58a050','#7cc06a','#d6efa6'],pal2=['#4a8a3a','#6cb15a','#9ad27a','#e3f3b4'];
  b+=tree(u,60,190,1.25,41,pal)+tree(u,400,176,1.0,42,pal2)+tree(u,452,208,1.4,43,pal)+tree(u,150,168,.7,44,pal2);
  /* banco */
  b+=E(318,206,30,4,'#000',' opacity=".24"')+R(290,184,56,4,'#8a5a34',INK)+R(290,190,56,4,'#8a5a34',INK)+R(290,196,56,4,'#9a6a40',INK)+R(294,200,4,8,'#3a2a1a')+R(338,200,4,8,'#3a2a1a')+R(292,176,52,3,'#8a5a34',INK)+R(292,180,52,3,'#8a5a34',INK)+R(294,176,3,24,'#3a2a1a')+R(340,176,3,24,'#3a2a1a');
  b+=R(290,184,56,1,'#f0cf9c',' opacity=".6"');
  /* poste de luz */
  var lp=lampPost(u,'lpk',250,186,.9,'#ffe2a0',false);d+=lp.d;b+=lp.b;
  /* pipa e balões */
  b+=S('M110 40Q130 70 118 120','#fff',.7,' opacity=".7"')+P('110,22 124,40 110,58 96,40','#e8503a',INK)+L(110,22,110,58,'#fff',.6,' opacity=".6"')+L(96,40,124,40,'#fff',.6,' opacity=".6"')+S('M110 58q-6 8 0 14t0 12','#e8503a',1);
  [[384,64,'#e8503a'],[398,54,'#f4c430'],[392,78,'#2f8fb8']].forEach(function(bl){b+=E(bl[0],bl[1],7,9,bl[2],INK)+E(bl[0]-2.4,bl[1]-3,2,3,'#fff',' opacity=".5"')+S('M'+bl[0]+' '+(bl[1]+9)+'Q'+(bl[0]-4)+' '+(bl[1]+30)+' 372 '+(bl[1]+70),'#555',.6,' opacity=".6"');});
  /* pássaros */
  b+=S('M180 50q4-4 8 0q4-4 8 0','#2a2a3a',1,' stroke-linecap="round"')+S('M210 38q3-3 6 0q3-3 6 0','#2a2a3a',.9,' stroke-linecap="round"');
  b+=SF.motes(r,16,0,20,480,160);
  return WRAP(u,d,b);
});

/* ---------- YARD: quintal com festa ao entardecer ---------- */
reg('yard',function(u){
  var r=rng(5505),d='',b='',i;
  d+=LG(u,'sk',0,0,0,130,[[0,'#3a4f86'],[0.35,'#8a78b0'],[0.7,'#f0a888'],[1,'#fcd09a']]);
  d+=LG(u,'gr',0,140,0,270,[[0,'#5a9a52'],[1,'#35703a']]);
  d+=LG(u,'fn',0,64,0,150,[[0,'#a87444'],[1,'#7a5230']]);
  d+=RG(u,'gl',240,150,200,[[0,'#ffd88a',.4],[1,'#ffd88a',0]]);
  d+=vig(u);
  b+=R(0,0,480,140,'url(#'+u+'-sk)');
  b+=E(380,92,36,36,'#ffd08a',' opacity=".35"')+C(380,92,13,'#fff0c0',' opacity=".9"');
  for(i=0;i<22;i++)b+=C(r()*480,r()*60,.7+r()*.8,'#fff',' opacity="'+r1(.4+r()*.5)+'"');
  /* casa ao fundo */
  b+=R(300,56,150,96,'#d9b98a',INK)+P('290,58 375,22 460,58','#a8553a',INK)+R(318,78,38,40,'#ffd47a',INK)+R(318,78,38,40,'#fff',' opacity=".1"')+R(336.4,78,1.6,40,'#fff')+R(318,97.4,38,1.6,'#fff')+R(310,118,54,4,'#e8dcc0',INK)+R(374,92,34,60,'#6d4a30',INK)+R(378,96,26,52,'none',' stroke="#e0b784" stroke-width=".6"')+C(400,126,1.5,'#e6c35c')+R(330,40,8,18,'#8a4a3a',INK);
  b+=D('M318 78l19 12l19-12v-0Z','#fff',' opacity=".0"');
  /* cerca de tábuas */
  b+=R(0,92,480,60,'url(#'+u+'-fn)',INK);
  for(i=0;i<480;i+=14){b+=R(i,86+((i*7)%5),12,66,'#b98353',INK)+R(i+1,88,2,62,'#fff',' opacity=".14"')+L(i+6,92,i+6,150,'#000',.4,' opacity=".18"')+P(i+','+(86+((i*7)%5))+' '+(i+6)+','+(80+((i*7)%5))+' '+(i+12)+','+(86+((i*7)%5)),'#b98353',INK);}
  b+=R(0,104,480,3,'#6a4624',INK)+R(0,136,480,3,'#6a4624',INK);
  /* gramado */
  b+=R(0,150,480,120,'url(#'+u+'-gr)');
  for(i=0;i<220;i++){var gx=r()*480,gy=152+r()*118;b+=S('M'+r1(gx)+' '+r1(gy)+'q-1-4 -3-7M'+r1(gx)+' '+r1(gy)+'q0-5 1-8','#2d6a33',.55,' opacity="'+r1(.3+r()*.4)+'"');}
  /* árvores laterais */
  var pal=['#2f6a35','#4a8a45','#6cae5c','#c6e59a'];
  b+=tree(u,40,176,1.15,51,pal)+tree(u,214,160,.62,52,['#3a7440','#5a9a4e','#80be68','#d3ecaa']);
  /* varal de luzes */
  var xs=[0,60,120,180,240,300,360,420,480],pts=[];
  b+=S('M0 70Q60 96 120 74T240 76T360 72T480 74','#2a1c14',.9,' opacity=".85"');
  for(i=0;i<22;i++){var t=i/21,bx=t*480,by=74+Math.sin(t*Math.PI*6)*7+ (Math.sin(t*3.1)*4);
    b+=C(bx,by+4,9,'#ffd88a',' opacity=".18"')+C(bx,by+4,3.4,'#ffe9b0',INK)+C(bx,by+3.4,1.2,'#fff');}
  /* mesa de piquenique */
  b+=E(250,214,92,8,'#000',' opacity=".25"')+R(160,180,176,6,'#a8723f',INK)+R(160,180,176,1.4,'#e0b784',' opacity=".7"')+R(172,186,6,24,'#6a4624',INK)+R(318,186,6,24,'#6a4624',INK);
  b+=P('172,186 322,186 340,204 154,204','#c4513a',INK)+P('172,186 322,186 330,194 164,194','#fff',' opacity=".12"');
  for(i=0;i<9;i++)b+=L(r1(176+i*18),186,r1(162+i*22),204,'#fff',.7,' opacity=".5"');
  /* comida: prato, bolo, frutas, copos */
  b+=E(200,178,12,3,'#f4f0e6',INK)+E(200,176,9,5,'#e8c07a',INK)+E(200,174,7,3,'#f4d79a')+C(200,170,2,'#d94f3d')+
     E(250,178,16,3.4,'#fff',INK)+C(244,175,4.4,'#d94f3d',INK)+C(252,175,4.4,'#e8b948',INK)+C(258,176,4,'#79b06a',INK)+
     RR(284,168,8,12,2,'#e8503a',INK)+RR(296,170,8,10,2,'#2f8fb8',INK)+RR(308,168,8,12,2,'#f4c430',INK)+
     D('M224 180l4-12h8l4 12Z','#cfe9f3',INK)+C(232,168,5,'#f08aa0',INK);
  /* banquinhos */
  [[150,212],[344,212]].forEach(function(p){b+=E(p[0],p[1]+10,14,3,'#000',' opacity=".22"')+R(p[0]-12,p[1],24,5,'#8a5a34',INK)+R(p[0]-10,p[1]+5,3,10,'#3a2a1a')+R(p[0]+7,p[1]+5,3,10,'#3a2a1a');});
  /* churrasqueira com fumaça */
  b+=E(436,226,22,4,'#000',' opacity=".26"')+C(436,204,17,'#2a2a30',INK)+D('M419 204h34q0 10-8 14h-18q-8-4-8-14Z','#3a3a42',INK)+R(424,202,24,3,'#e8503a',' opacity=".8"')+R(430,198,5,3,'#ffb84a')+L(424,218,420,236,'#444',1.6)+L(448,218,452,236,'#444',1.6)+L(436,218,436,236,'#444',1.6);
  b+='<g filter="url(#'+u+'-b2)" opacity=".5"><ellipse cx="436" cy="178" rx="8" ry="12" fill="#e8e8f0"/><ellipse cx="444" cy="152" rx="10" ry="14" fill="#e8e8f0"/><ellipse cx="452" cy="124" rx="13" ry="14" fill="#e8e8f0"/></g>';
  /* balões amarrados */
  [[110,150,'#e8503a'],[124,138,'#f4c430'],[100,136,'#2f8fb8'],[116,124,'#8c6aa6']].forEach(function(bl){b+=S('M'+bl[0]+' '+(bl[1]+9)+'Q'+(bl[0]+6)+' '+(bl[1]+38)+' 118 190','#666',.6,' opacity=".7"')+E(bl[0],bl[1],7,9,bl[2],INK)+E(bl[0]-2.4,bl[1]-3,2,3,'#fff',' opacity=".5"');});
  b+=R(0,0,480,270,'url(#'+u+'-gl)');
  b+=SF.motes(r,22,0,60,480,200);
  return WRAP(u,d,b);
});
})();
