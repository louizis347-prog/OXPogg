/* scn_fine2.js - mais cenários refinados (sala, sala de aula, rua, parque, quintal, loja, lanchonete, café).
   Usa a biblioteca window.SF de scn_fine.js. */
(function(){
if(!window.SF||!window.RS)return;
var SF=window.SF,RS=window.RS;
var rng=SF.rng,r1=SF.r1,LG=SF.LG,RG=SF.RG,R=SF.R,RR=SF.RR,E=SF.E,C=SF.C,L=SF.L,P=SF.P,D=SF.D,S=SF.S,T=SF.T,G=SF.G,F=SF.F,INK=SF.INK,WRAP=SF.WRAP,vig=SF.vig,reg=SF.reg;

/* ---------- peças ---------- */

/* piso de tábuas em perspectiva: cada tábua com tom próprio, veios e emendas alternadas */
function parquet(u,y0,vy,seed,tones,line){
  var r=rng(seed),b='',i,j,n=27,k=(y0-vy)/(270-vy);
  b+=R(0,y0,480,270-y0,tones[0]);
  for(i=-n;i<n;i++){
    var xb1=240+i*34,xb2=240+(i+1)*34,xt1=240+i*34*k,xt2=240+(i+1)*34*k;
    b+=P(r1(xt1)+','+y0+' '+r1(xt2)+','+y0+' '+r1(xb2)+',270 '+r1(xb1)+',270',tones[Math.floor(r()*tones.length)],' opacity="'+r1(.55+r()*.4)+'"');
    /* veios */
    for(j=0;j<2;j++){var f=.25+r()*.5,xa=xt1+(xt2-xt1)*f,xz=xb1+(xb2-xb1)*f;b+=L(r1(xa),y0,r1(xz+(r()-.5)*3),270,line,.4,' opacity="'+r1(.1+r()*.12)+'"');}
  }
  for(i=-n;i<=n;i++)b+=L(r1(240+i*34*k),y0,r1(240+i*34),270,line,.7,' opacity=".42"');
  /* emendas (curtas, alternadas) em linhas de perspectiva */
  var rows=[y0+4,y0+9,y0+16,y0+26,y0+40,y0+60,y0+88];
  rows.forEach(function(y,m){
    var kk=(y-vy)/(270-vy);
    for(i=-n;i<n;i++)if(((i+m)&1)===0){var xa=240+i*34*kk,xb=240+(i+1)*34*kk;b+=L(r1(xa),y,r1(xb),y,line,.6,' opacity=".4"');}
  });
  return b;
}

/* janela ao entardecer: skyline com janelas acesas, caixilho, reflexo, cortina e varão */
function windowDusk(u,id,x,y,w,h,seed,curtain){
  var r=rng(seed),d='',b='',i;
  d+=LG(u,id,x,y,x,y+h,[[0,'#4f6fa8'],[0.35,'#9a96c4'],[0.7,'#f1b48a'],[1,'#fcd8a0']]);
  b+=R(x-5,y-5,w+10,h+10,'#f2ead8',INK)+R(x,y,w,h,'url(#'+u+'-'+id+')');
  b+=E(x+w*.74,y+h*.62,w*.18,w*.18,'#ffe7a8',' opacity=".55"')+C(x+w*.74,y+h*.62,w*.05,'#fff6d0');
  for(i=0;i<9;i++){var bw=w/9+2,bh=h*(.22+r()*.34),bx=x+i*(w/9)-1;b+=R(bx,y+h-bh,bw,bh,'rgb('+(70+Math.floor(r()*30))+','+(70+Math.floor(r()*24))+','+(104+Math.floor(r()*30))+')',' opacity=".92"');
    for(var q=0;q<Math.floor(bh/6);q++)for(var m=0;m<2;m++)if(r()>.5)b+=R(bx+2+m*(bw/2-1),y+h-bh+3+q*6,2,2.6,'#ffd97a',' opacity="'+r1(.5+r()*.5)+'"');}
  b+=D('M'+(x)+' '+(y+h)+'L'+(x)+' '+(y+h*.78)+'L'+(x+w*.55)+' '+(y+h)+'Z','#fff',' opacity=".1"');
  /* caixilho */
  b+=R(x+w/2-1.6,y,3.2,h,'#f2ead8',INK)+R(x,y+h/2-1.6,w,3.2,'#f2ead8',INK)+R(x-6,y+h+2,w+12,5,'#e4d8bd',INK)+R(x-6,y+h+2,w+12,1.2,'#fff',' opacity=".8"');
  b+=P(x+','+y+' '+(x+w*.34)+','+y+' '+(x+w*.12)+','+(y+h)+' '+x+','+(y+h),'#fff',' opacity=".16"');
  if(curtain){
    var cw=w*.3;
    [[x-cw-4,'#c9856a'],[x+w+4,'#c9856a']].forEach(function(c,k){
      var cx=c[0];
      b+=R(cx,y-8,cw,h+22,c[1],INK);
      for(var f=0;f<7;f++)b+=L(r1(cx+f*cw/7+2),y-8,r1(cx+f*cw/7+(k?-1:1)*2),y+h+14,'#000',.7,' opacity=".16"')+L(r1(cx+f*cw/7+3.2),y-8,r1(cx+f*cw/7+3.2),y+h+14,'#fff',.5,' opacity=".1"');
      b+=D('M'+cx+' '+(y+h+14)+'Q'+r1(cx+cw/2)+' '+(y+h+19)+' '+r1(cx+cw)+' '+(y+h+14)+'V'+(y+h+14)+'Z',c[1]);
    });
    b+=R(x-cw-12,y-14,w+2*cw+24,3.4,'#3b2a1a',INK)+C(x-cw-13,y-12.4,3,'#b8923f',INK)+C(x+w+cw+13,y-12.4,3,'#b8923f',INK);
    for(i=0;i<9;i++)b+=C(x-cw+i*((w+2*cw)/8),y-8,1.6,'#b8923f');
  }
  return {d:d,b:b};
}

/* estante com livros de alturas, cores e inclinações variadas, mais objetos de decoração */
function bookshelf(u,x,y,w,h,seed){
  var r=rng(seed),b='',s,i,rows=Math.floor(h/26),sh=h/rows;
  b+=E(x+w/2,y+h+1,w*.62,2.6,'#000',' opacity=".24"')+R(x,y,w,h,'#5a3a24',INK)+R(x+3,y+3,w-6,h-6,'#2c1c12');
  var cols=['#c4513a','#2f6f8f','#e0b24a','#4f8a5b','#7a4f9a','#d9d2c0','#b83a52','#35567a','#e08a3f'];
  for(s=0;s<rows;s++){
    var by=y+3+s*sh,bx=x+5,top=by+sh-3;
    while(bx<x+w-9){
      var bw=3+r()*4.4,bh=sh*(.55+r()*.38),c=cols[Math.floor(r()*cols.length)],lean=r()>.92;
      if(r()>.9){ // objeto
        var kind=Math.floor(r()*3);
        if(kind===0)b+=D('M'+r1(bx)+' '+top+'l1.6-9h4l1.6 9Z','#d8e6ea',INK)+S('M'+r1(bx+3.6)+' '+r1(top-9)+'q-3-6 1-9','#4f8a5b',.9);
        else if(kind===1)b+=RR(bx,top-8,9,8,1,'#e0b24a',INK)+R(bx+1.4,top-6,6,1,'#fff',' opacity=".5"');
        else b+=C(bx+4,top-5,4.5,'#4f8f94',INK)+S('M'+r1(bx-.5)+' '+r1(top-5)+'h9','#fff',.5,' opacity=".6"');
        bx+=11;continue;
      }
      b+=(lean?G('rotate(-10 '+r1(bx+bw)+' '+top+')',R(bx,top-bh,bw,bh,c,INK)):R(bx,top-bh,bw,bh,c,INK))+R(bx+.7,top-bh+2,bw-1.4,1,'#fff',' opacity=".3"')+R(bx+.7,top-bh*.4,bw-1.4,.8,'#fff',' opacity=".25"');
      bx+=bw+.7;
    }
    b+=R(x+3,y+3+(s+1)*sh-3,w-6,3,'#6d4a30')+R(x+3,y+3+(s+1)*sh-3,w-6,.8,'#e0b784',' opacity=".6"');
  }
  b+=R(x-2,y-3,w+4,4,'#6d4a30',INK)+R(x-2,y-3,w+4,1,'#e0b784',' opacity=".7"');
  return b;
}

/* sofá com almofadas, costuras e manta */
function sofa(u,x,y,w,c1,c2,pillow){
  var b='',n=2,cw=(w-44)/n,i;
  b+=E(x+w/2,y+2,w*.58,5,'#000',' opacity=".28"');
  b+=R(x+10,y-2,6,8,'#3a2415')+R(x+w-16,y-2,6,8,'#3a2415');
  b+=RR(x+8,y-50,w-16,42,12,c1,INK)+RR(x+10,y-48,w-20,12,10,'#fff',' opacity=".08"');
  for(i=0;i<n;i++){var cx=x+22+i*cw;b+=RR(cx,y-40,cw-2,32,8,c2,INK)+RR(cx+3,y-38,cw-8,10,6,'#fff',' opacity=".1"')+L(cx+cw/2,y-39,cx+cw/2,y-12,'#000',.6,' opacity=".2"');}
  b+=RR(x-4,y-36,26,34,11,c1,INK)+RR(x+w-22,y-36,26,34,11,c1,INK)+RR(x-2,y-34,10,10,5,'#fff',' opacity=".09"')+RR(x+w-8,y-34,10,10,5,'#fff',' opacity=".09"');
  b+=RR(x+6,y-14,w-12,14,6,c1,INK)+S('M'+(x+14)+' '+(y-7)+'H'+(x+w-14),'#000',.6,' opacity=".22"');
  pillow.forEach(function(p,k){var px=x+(k?w-62:34),py=y-52;
    b+=G('rotate('+(k?10:-8)+' '+(px+12)+' '+(py+14)+')',RR(px,py,26,26,6,p[0],INK)+RR(px+3,py+3,20,20,4,'none',' stroke="'+p[1]+'" stroke-width="1"')+C(px+13,py+13,3.4,p[1])+L(px+1,py+13,px+25,py+13,p[1],.5,' opacity=".6"'));});
  return b;
}

/* mesa de centro com xícara, livros e vaso */
function coffeeTable(u,x,y,w){
  var b='';
  b+=E(x+w/2,y+9,w*.55,4,'#000',' opacity=".25"');
  b+=R(x+6,y,3,10,'#4a2e1a')+R(x+w-9,y,3,10,'#4a2e1a')+R(x+w*.5-1.5,y,3,9,'#4a2e1a');
  b+=E(x+w/2,y,w/2,6,'#8a5c38',INK)+E(x+w/2,y-1,w/2-2,5,'#a87448')+S('M'+(x+8)+' '+(y-1)+'Q'+(x+w/2)+' '+(y+2)+' '+(x+w-8)+' '+(y-2),'#6d4a30',.5,' opacity=".5"');
  /* itens */
  b+=R(x+w*.18,y-6,22,4,'#2f6f8f',INK)+R(x+w*.18+2,y-9,19,3.4,'#e0b24a',INK)+R(x+w*.18+4,y-11.4,15,2.6,'#c4513a',INK);
  b+=D('M'+(x+w*.62)+' '+(y-2)+'h8l-1 -6h-6Z','#f6efe0',INK)+E(x+w*.62+4,y-8,4,1,'#6a3f1c')+S('M'+(x+w*.62+8)+' '+(y-6)+'q3 0 3 2t-3 2','#f6efe0',1);
  b+=D('M'+(x+w*.8)+' '+(y-1)+'h7l-1.4 -10h-4.2Z','#9ec3d3',INK)+S('M'+(x+w*.8+3.5)+' '+(y-11)+'q-3-8 -5-9M'+(x+w*.8+3.5)+' '+(y-11)+'q2-8 5-8','#4f8a5b',.9)+C(x+w*.8-1,y-20,2.2,'#f0a0b8')+C(x+w*.8+6,y-19,2.2,'#fff3d8');
  return b;
}

/* gato dormindo */
function cat(x,y,s,c1,c2){
  var b='';
  b+=E(x,y,16*s,8*s,c1,INK)+E(x-12*s,y-4*s,7*s,6*s,c1,INK)+D('M'+r1(x-17*s)+' '+r1(y-9*s)+'l2-5l4 3Z',c1,INK)+D('M'+r1(x-9*s)+' '+r1(y-9*s)+'l1-5l4 2Z',c1,INK)+
    S('M'+r1(x-15*s)+' '+r1(y-4*s)+'q2 1.6 4 0M'+r1(x-11*s)+' '+r1(y-4*s)+'q2 1.6 4 0','#2a1608',.7)+D('M'+r1(x-10*s)+' '+r1(y-1.5*s)+'l1.4 1.4l-2.4 0Z','#e58a8a')+
    S('M'+r1(x+13*s)+' '+r1(y+2*s)+'q8 2 8-5t-6-6',c1,2.4*s,' stroke-linecap="round"')+E(x+2*s,y-2*s,9*s,3*s,c2,' opacity=".6"');
  return b;
}

/* mesa-escrivaninha/carteira de sala de aula */
function schoolDesk(u,x,y,s,seed){
  var r=rng(seed),b='';
  b+=E(x+14*s,y+14*s,20*s,3*s,'#000',' opacity=".25"');
  b+=L(x+2*s,y+6*s,x,y+14*s,'#555',1.3*s)+L(x+26*s,y+6*s,x+28*s,y+14*s,'#555',1.3*s);
  b+=P(r1(x-2*s)+','+r1(y+2*s)+' '+r1(x+4*s)+','+r1(y-3*s)+' '+r1(x+26*s)+','+r1(y-3*s)+' '+r1(x+31*s)+','+r1(y+2*s),'#d0a06a',INK)+R(x-2*s,y+2*s,33*s,3.4*s,'#a87444',INK)+R(x-2*s,y+2*s,33*s,.8*s,'#f0cf9c',' opacity=".7"');
  b+=R(x+3*s,y-6*s,10*s,3*s,['#c4513a','#2f6f8f','#4f8a5b'][Math.floor(r()*3)],INK)+R(x+15*s,y-4*s,12*s,1.6*s,'#f6efe0',INK)+L(x+17*s,y-3.2*s,x+25*s,y-3.2*s,'#8aa',.5);
  return b;
}
function chair(x,y,s,col){
  return R(x+2*s,y-12*s,16*s,3*s,col,INK)+R(x+3*s,y-9*s,14*s,2*s,'#000',' opacity=".18"')+R(x+4*s,y-9*s,2*s,13*s,'#555')+R(x+14*s,y-9*s,2*s,13*s,'#555')+RR(x+1*s,y-6*s,18*s,3.4*s,1,col,INK);
}

/* ---------- HOME1: sala de estar ao entardecer ---------- */
reg('home1',function(u){
  var r=rng(1101),d='',b='',i;
  d+=LG(u,'wl',0,0,0,160,[[0,'#f3dcb4'],[1,'#e7c392']]);
  d+=LG(u,'ce',0,0,0,24,[[0,'#f7ead2'],[1,'#e6d3ac']]);
  d+=LG(u,'sg',0,0,0,1,[[0,'#fff',.5],[1,'#fff',0]]);
  d+=RG(u,'wg',350,92,150,[[0,'#ffcf94',.6],[1,'#ffb066',0]]);
  d+=RG(u,'lg',284,110,64,[[0,'#ffe6a8',.7],[0.5,'#ffd28a',.22],[1,'#ffd28a',0]]);
  d+=vig(u);
  /* piso de madeira + parede */
  var pq=parquet(u,160,114,5,['#b9824f','#a8723f','#c8915e','#9a6638'],'#5a3a1e');
  var wall=R(0,24,480,136,'url(#'+u+'-wl)');
  for(i=0;i<480;i+=24)wall+=R(i,24,10,136,'#fff',' opacity=".03"');
  /* teto + sanca + rodapé */
  wall+=R(0,0,480,26,'url(#'+u+'-ce)')+R(0,22,480,6,'#efe0bc',INK)+R(0,26,480,2,'#000',' opacity=".14"')+R(0,22,480,1,'#fff',' opacity=".8"');
  for(i=0;i<480;i+=7)wall+=R(i,23.4,3.4,2.4,'#d3b97d',' opacity=".7"');
  wall+=R(0,150,480,10,'#fff6e0',INK)+R(0,150,480,1.4,'#fff',' opacity=".9"')+R(0,158,480,2.4,'#000',' opacity=".2"');
  /* friso (boiserie) */
  for(i=-4;i<490;i+=64)wall+=R(i+6,108,52,36,'none',' stroke="#c9ab74" stroke-width="1" opacity=".7"')+R(i+9,111,46,30,'none',' stroke="#c9ab74" stroke-width=".5" opacity=".5"');
  wall+=R(0,104,480,4,'#fff3d4',INK)+R(0,104,480,1,'#fff',' opacity=".9"');
  /* estante */
  b+=bookshelf(u,28,36,74,114,3);
  /* quadros */
  b+=SF.frame(u,126,44,34,42,'abs',1)+SF.frame(u,166,38,44,34,'land',2)+SF.frame(u,166,78,24,30,'portrait',3)+SF.frame(u,196,78,32,26,'abs',4);
  /* janela + cortina */
  var wd=windowDusk(u,'wk',338,34,84,74,7,true);d+=wd.d;b+=wd.b;
  b+=R(0,24,480,136,'url(#'+u+'-wg)');
  /* sofá, mesa, tapete */
  var rg='';
  rg+=P('112,212 292,212 322,246 82,246','#8a4a3a',INK)+P('120,215 284,215 308,240 96,240','#a85a46')+P('130,218 274,218 292,236 112,236','none',' stroke="#e8cf98" stroke-width="1.2" opacity=".9"');
  for(i=0;i<14;i++)rg+=C(140+i*9.6,226,1.5,'#e8cf98',' opacity=".7"');
  for(i=0;i<22;i++)rg+=L(r1(112+i*8.2),212,r1(82+i*10.9),246,'#efe3c4',.4,' opacity=".35"');
  b+=rg;
  b+=sofa(u,112,176,176,'#4e7f94','#6a9bb0',[['#e2825f','#fde0b0'],['#e8b948','#fff1c6']]);
  b+=cat(168,148,1,'#c98a58','#f1d7b0');
  b+=coffeeTable(u,160,218,84);
  /* luminária de pé e planta */
  b+=R(283.2,98,1.6,62,'#3a2a14')+D('M270 98L276 78H292L298 98Z','#f6e3b2',INK)+E(284,98,14,2.2,'#ffe9b0',' opacity=".9"')+E(284,160,9,2,'#2a1c0e')+C(284,110,64,'url(#'+u+'-lg)');
  b+=SF.plantFull(u,462,164,.9,6,['#c9824f','#a8683c']);
  /* reflexo do piso e poeira */
  b+=E(350,176,64,6,'#ffd28a',' opacity=".18"')+SF.motes(r,22,0,30,480,150);
  return WRAP(u,d,pq+wall+b);
});

/* ---------- SCHOOL: sala de aula ---------- */
reg('school',function(u){
  var r=rng(2202),d='',b='',i,j;
  d+=LG(u,'wl',0,0,0,150,[[0,'#cfe0d8'],[1,'#b7cfc4']]);
  d+=LG(u,'bd',0,38,0,112,[[0,'#2f5a46'],[1,'#264a3a']]);
  d+=LG(u,'ce',0,0,0,22,[[0,'#f4efe3'],[1,'#ddd3bd']]);
  d+=RG(u,'sun',90,90,160,[[0,'#fff1c8',.55],[1,'#fff1c8',0]]);
  d+=vig(u);
  var pq=parquet(u,156,110,12,['#cfa070','#c28f5e','#d8ae80','#b98353'],'#7a5230');
  var wall=R(0,22,480,134,'url(#'+u+'-wl)');
  wall+=R(0,0,480,24,'url(#'+u+'-ce)')+R(0,22,480,4,'#efe9d8',INK)+R(0,24,480,2,'#000',' opacity=".12"');
  for(i=0;i<480;i+=60)wall+=R(i,0,2,22,'#fff',' opacity=".5"');
  /* friso verde + rodapé */
  wall+=R(0,112,480,44,'#8aa99a')+R(0,112,480,3,'#f2eadb',INK);
  for(i=0;i<480;i+=12)wall+=R(i,115,.7,38,'#000',' opacity=".12"');
  wall+=R(0,150,480,6,'#e9dfc8',INK)+R(0,154,480,2.4,'#000',' opacity=".2"');
  /* lousa grande com giz */
  b+=R(150,34,184,84,'#7a5230',INK)+R(154,38,176,76,'url(#'+u+'-bd)')+R(154,38,176,3,'#000',' opacity=".25"');
  b+=P('154,38 214,38 190,114 154,114','#fff',' opacity=".05"');
  b+=T(164,56,'Welcome!',10,'#f4f1e6',{f:'"Comic Sans MS",Segoe Script,cursive',w:'bold'});
  b+=T(164,72,'A  B  C  D  E',7.4,'#fbe9a0',{f:'Segoe Script,cursive'})+T(164,84,'1 + 1 = 2',6.8,'#cfe9f3',{f:'Segoe Script,cursive'});
  b+=S('M262 52q10-8 20 0t20 0','#f3a6b0',1.2)+C(296,76,8,'none',' stroke="#fbe9a0" stroke-width="1"')+S('M290 78q6 6 12 0','#fbe9a0',1)+C(293,74,.9,'#fbe9a0')+C(299,74,.9,'#fbe9a0');
  b+=S('M236 96h86M236 102h60','#f4f1e6',.9,' opacity=".55"');
  b+=R(150,114,184,5,'#5a3a24',INK)+R(158,112,24,2.6,'#f4f1e6')+R(190,112,12,2.6,'#e0a2a8')+R(208,112,10,2.6,'#fbe9a0');
  /* relógio, bandeiras, globo */
  b+=SF.clock(u,360,52,13,9,10);
  b+=L(372,70,372,72,'#333',.1);
  /* janela com luz do dia */
  var wx=22,wy=40,ww=100,wh=70;
  b+=R(wx-4,wy-4,ww+8,wh+8,'#f2ead8',INK)+R(wx,wy,ww,wh,'#bfe0f2')+E(wx+22,wy+14,16,6,'#fff',' opacity=".85"')+E(wx+58,wy+22,22,7,'#fff',' opacity=".7"')+
    D('M'+wx+' '+(wy+wh)+'L'+wx+' '+(wy+wh*.55)+'Q'+(wx+30)+' '+(wy+wh*.4)+' '+(wx+ww)+' '+(wy+wh*.62)+'V'+(wy+wh)+'Z','#8fbf7a')+D('M'+wx+' '+(wy+wh)+'L'+wx+' '+(wy+wh*.8)+'Q'+(wx+50)+' '+(wy+wh*.66)+' '+(wx+ww)+' '+(wy+wh*.82)+'V'+(wy+wh)+'Z','#5f9a58');
  for(i=0;i<5;i++)b+=C(wx+14+i*16,wy+wh*.7+((i*7)%9),5+((i*3)%4),'#4f8a4a',' opacity=".8"');
  b+=R(wx+ww/2-1.4,wy,2.8,wh,'#f2ead8',INK)+R(wx,wy+wh/2-1.4,ww,2.8,'#f2ead8',INK)+R(wx-5,wy+wh+3,ww+10,5,'#e4d8bd',INK)+P(wx+','+wy+' '+(wx+34)+','+wy+' '+(wx+10)+','+(wy+wh)+' '+wx+','+(wy+wh),'#fff',' opacity=".2"');
  b+=P((wx+ww)+',112 '+(wx+ww+170)+',150 '+(wx+ww+170)+',156 '+(wx+ww)+',116','#fff6cc',' opacity=".0"');
  b+=R(0,0,480,160,'url(#'+u+'-sun)');
  /* cartazes e mural */
  b+=R(352,74,64,30,'#f6efdc',INK);for(i=0;i<8;i++)b+=R(356+i*7.4,78,6,6,['#c4513a','#2f6f8f','#e0b24a','#4f8a5b'][i%4],' opacity=".9"')+R(356+i*7.4,87,6,6,['#e0b24a','#4f8a5b','#c4513a','#2f6f8f'][i%4],' opacity=".9"');
  b+=L(356,98,412,98,'#8aa',.5);
  /* mesa do professor + maçã */
  b+=E(398,142,26,3,'#000',' opacity=".2"')+R(378,126,40,5,'#b98353',INK)+R(380,131,36,20,'#9a6a40',INK)+R(384,134,12,14,'none',' stroke="#e0b784" stroke-width=".6"')+C(386,122,3.4,'#d9473a',INK)+S('M386 118.6q1-3 3-3','#4f8a4a',.8)+R(402,118,10,8,'#2f6f8f',INK);
  /* globo */
  b+=R(98,140,2,10,'#6d4a30')+C(99,132,9,'#4f8fb8',INK)+D('M92 130q4-6 8-2t3 6q-4 4-8 2t-3-6Z','#79b06a')+S('M90 132q9 4 18 0','#fff',.4,' opacity=".5"');
  /* carteiras em perspectiva (3 fileiras) */
  var rows=[[168,.8,[110,178,246,314]],[196,1.05,[88,174,260,346]],[232,1.4,[56,170,284,398]]];
  rows.forEach(function(row,k){var y=row[0],s=row[1];row[2].forEach(function(x,j){b+=chair(x+4*s,y+14*s,s,['#c4513a','#2f6f8f','#e0b24a','#4f8a5b'][(j+k)%4])+schoolDesk(u,x,y,s,j+k*7);});});
  /* mochilas no chão */
  b+=RR(76,236,18,22,6,'#2f6f8f',INK)+R(79,240,12,6,'#e0b24a',INK)+RR(420,250,18,20,6,'#c4513a',INK)+R(423,254,12,5,'#f6efdc',INK);
  b+=SF.motes(r,20,0,40,480,150);
  return WRAP(u,d,pq+wall+b);
});
})();
