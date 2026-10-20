/* scn_fine.js - cenários refinados (mesma identidade dos cenários detalhados: pintura quente, grão, vinheta),
   com mais detalhe e traço: papel de parede, molduras, mármore em perspectiva, plantas folha a folha,
   móveis com costura e sombra de contato. Substitui os cenários simples; se algo falhar, cai no antigo.
   Cada função RS[chave](uid) devolve um SVG 480x270 com ids prefixados por uid. */
(function(){
window.RS = window.RS || {};
var RS = window.RS;

/* ---------- utilitários ---------- */
function rng(s){return function(){s=(s*16807)%2147483647;return (s-1)/2147483646;};}
function r1(n){return Math.round(n*10)/10;}
function LG(u,id,x1,y1,x2,y2,st){var s='<linearGradient id="'+u+'-'+id+'" gradientUnits="userSpaceOnUse" x1="'+x1+'" y1="'+y1+'" x2="'+x2+'" y2="'+y2+'">';for(var i=0;i<st.length;i++)s+='<stop offset="'+st[i][0]+'" stop-color="'+st[i][1]+'"'+(st[i][2]!=null?' stop-opacity="'+st[i][2]+'"':'')+'/>';return s+'</linearGradient>';}
function RG(u,id,cx,cy,r,st){var s='<radialGradient id="'+u+'-'+id+'" gradientUnits="userSpaceOnUse" cx="'+cx+'" cy="'+cy+'" r="'+r+'">';for(var i=0;i<st.length;i++)s+='<stop offset="'+st[i][0]+'" stop-color="'+st[i][1]+'"'+(st[i][2]!=null?' stop-opacity="'+st[i][2]+'"':'')+'/>';return s+'</radialGradient>';}
function R(x,y,w,h,fill,ex){return '<rect x="'+r1(x)+'" y="'+r1(y)+'" width="'+r1(w)+'" height="'+r1(h)+'" fill="'+fill+'"'+(ex||'')+'/>';}
function RR(x,y,w,h,rad,fill,ex){return '<rect x="'+r1(x)+'" y="'+r1(y)+'" width="'+r1(w)+'" height="'+r1(h)+'" rx="'+rad+'" fill="'+fill+'"'+(ex||'')+'/>';}
function E(cx,cy,rx,ry,fill,ex){return '<ellipse cx="'+r1(cx)+'" cy="'+r1(cy)+'" rx="'+r1(rx)+'" ry="'+r1(ry)+'" fill="'+fill+'"'+(ex||'')+'/>';}
function C(cx,cy,r,fill,ex){return '<circle cx="'+r1(cx)+'" cy="'+r1(cy)+'" r="'+r1(r)+'" fill="'+fill+'"'+(ex||'')+'/>';}
function L(x1,y1,x2,y2,st,w,ex){return '<line x1="'+r1(x1)+'" y1="'+r1(y1)+'" x2="'+r1(x2)+'" y2="'+r1(y2)+'" stroke="'+st+'" stroke-width="'+w+'"'+(ex||'')+'/>';}
function P(pts,fill,ex){return '<polygon points="'+pts+'" fill="'+fill+'"'+(ex||'')+'/>';}
function D(d,fill,ex){return '<path d="'+d+'" fill="'+fill+'"'+(ex||'')+'/>';}
function S(d,st,w,ex){return '<path d="'+d+'" fill="none" stroke="'+st+'" stroke-width="'+w+'"'+(ex||'')+'/>';}
function T(x,y,s,sz,fill,o){o=o||{};return '<text x="'+x+'" y="'+y+'" font-family="'+(o.f||'Georgia,serif')+'" font-size="'+sz+'" fill="'+fill+'"'+(o.w?' font-weight="'+o.w+'"':'')+(o.a?' text-anchor="'+o.a+'"':'')+(o.ls?' letter-spacing="'+o.ls+'"':'')+'>'+s+'</text>';}
function F(u,id){return 'url(#'+u+'-'+id+')';}
function G(tr,inner,ex){return '<g transform="'+tr+'"'+(ex||'')+'>'+inner+'</g>';}

/* "traço": contorno fino e quente em volta dos objetos, dá o ar de desenho */
var INK=' stroke="#2a1608" stroke-opacity=".38" stroke-width=".55" stroke-linejoin="round"';

/* base do SVG com grão de pintura e desfoque leve */
function WRAP(u,defs,body){
  return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 270" width="100%" height="100%" preserveAspectRatio="xMidYMid slice" role="img" aria-hidden="true" style="width:100%;height:100%;display:block"><defs>'+defs+
  '<filter id="'+u+'-nz" filterUnits="userSpaceOnUse" x="0" y="0" width="480" height="270"><feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" seed="7"/><feColorMatrix values="0 0 0 0 0.25 0 0 0 0 0.22 0 0 0 0 0.2 1.4 0 0 0 -0.45"/></filter>'+
  '<filter id="'+u+'-br" filterUnits="userSpaceOnUse" x="0" y="0" width="480" height="270"><feTurbulence type="fractalNoise" baseFrequency="0.012 0.18" numOctaves="3" seed="3"/><feColorMatrix values="0 0 0 0 0.3 0 0 0 0 0.2 0 0 0 0 0.12 0 0 0 0.9 -0.35"/></filter>'+
  '<filter id="'+u+'-bl" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="1.2"/></filter>'+
  '<filter id="'+u+'-b2" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="3"/></filter>'+
  '</defs>'+body+
  /* acabamento: pinceladas largas + grão fino + vinheta */
  '<rect width="480" height="270" filter="url(#'+u+'-br)" opacity=".10"/><rect width="480" height="270" filter="url(#'+u+'-nz)" opacity=".07"/>'+
  '<rect width="480" height="270" fill="url(#'+u+'-vg)"/></svg>';
}
function vig(u){return RG(u,'vg',240,130,310,[[0.5,'#000',0],[1,'#160c04',0.36]]);}

/* ---------- peças reutilizáveis (cada uma devolve {d,b}) ---------- */

/* piso de mármore em perspectiva, com juntas, veios e reflexos das luzes */
function marbleFloor(u,y0,vy,seed,tint,lights){
  var r=rng(seed),d='',b='',i,j;
  d+=LG(u,'mf',0,y0,0,270,[[0,tint[0]],[0.35,tint[1]],[1,tint[2]]]);
  b+=R(0,y0,480,270-y0,'url(#'+u+'-mf)');
  var rows=[y0,y0+6,y0+15,y0+29,y0+50,y0+82,y0+118];
  /* veios dentro de cada ladrilho */
  for(j=0;j<rows.length-1;j++){
    var ya=rows[j],yb=rows[j+1],k=(yb-vy)/(270-vy);
    for(i=-9;i<=9;i++){
      var xa=240+(i*70-240+240)*0+ (i*70)*k, xb2=240+((i+1)*70)*k;
      if(xb2<-30||xa>510)continue;
      var cx=(xa+xb2)/2,cy=(ya+yb)/2;
      if(r()<.8)b+=S('M'+r1(xa+(xb2-xa)*r()*.4)+' '+r1(ya)+'Q'+r1(cx+(r()-.5)*10*k)+' '+r1(cy)+' '+r1(xa+(xb2-xa)*(.5+r()*.5))+' '+r1(yb),tint[3],.5,' opacity="'+r1(.16+r()*.16)+'"');
      if(r()<.35)b+=S('M'+r1(xa+(xb2-xa)*.15)+' '+r1(yb)+'Q'+r1(cx)+' '+r1(cy+2)+' '+r1(xb2-(xb2-xa)*.1)+' '+r1(ya+1),tint[3],.35,' opacity=".2"');
      b+=R(xa+1,ya+.6,(xb2-xa)-2,(yb-ya)-1.2,'#fff',' opacity="'+r1(.02+r()*.05)+'"');
    }
  }
  /* juntas */
  for(i=-9;i<=10;i++){var xb=240+(i*70-0)*1;b+=L(r1(240+(i*70)*((y0-vy)/(270-vy))),y0,r1(240+i*70),270,tint[3],.7,' opacity=".34"');}
  rows.forEach(function(y,k){b+=L(0,y,480,y,tint[3],.7,' opacity="'+(k?'.3':'.5')+'"')+L(0,y+.9,480,y+.9,'#fff',.5,' opacity=".28"');});
  /* reflexos das luzes (elipses alongadas) */
  lights.forEach(function(l){
    d+=RG(u,'rf'+l[0],l[0],l[1],l[2],[[0,l[3],0.55],[0.5,l[3],0.18],[1,l[3],0]]);
    b+=E(l[0],l[1],l[2],l[2]*.26,'url(#'+u+'-rf'+l[0]+')');
  });
  return {d:d,b:b};
}

/* papel de parede com treliça dourada e luz suave */
function wallpaper(u,y0,y1,base,line,glowC){
  var d='',b='';
  d+=LG(u,'wp',0,y0,0,y1,[[0,base[0]],[1,base[1]]]);
  d+='<pattern id="'+u+'-wpat" width="26" height="30" patternUnits="userSpaceOnUse"><path d="M13 2L24 15L13 28L2 15Z" fill="none" stroke="'+line+'" stroke-width=".6" opacity=".34"/><path d="M13 9L18 15L13 21L8 15Z" fill="'+line+'" opacity=".16"/><circle cx="13" cy="15" r="1.1" fill="'+line+'" opacity=".4"/><path d="M0 0L26 30M26 0L0 30" stroke="'+line+'" stroke-width=".3" opacity=".12"/></pattern>';
  b+=R(0,y0,480,y1-y0,'url(#'+u+'-wp)')+R(0,y0,480,y1-y0,'url(#'+u+'-wpat)');
  return {d:d,b:b};
}

/* planta tipo monstera, folhas desenhadas uma a uma com nervuras */
function plant(u,x,y,s,seed,pot){
  var r=rng(seed),b='',i;
  b+=E(x,y+1,22*s,4*s,'#000',' opacity=".22"');
  b+=D('M'+r1(x-13*s)+' '+r1(y-24*s)+'L'+r1(x+13*s)+' '+r1(y-24*s)+'L'+r1(x+10*s)+' '+r1(y)+'Q'+x+' '+r1(y+3*s)+' '+r1(x-10*s)+' '+r1(y)+'Z',pot[0],INK);
  b+=D('M'+r1(x-13*s)+' '+r1(y-24*s)+'L'+r1(x+13*s)+' '+r1(y-24*s)+'L'+r1(x+12.4*s)+' '+r1(y-20*s)+'L'+r1(x-12.4*s)+' '+r1(y-20*s)+'Z',pot[1]);
  b+=D('M'+r1(x-13*s)+' '+r1(y-24*s)+'L'+r1(x-9*s)+' '+r1(y-24*s)+'L'+r1(x-7*s)+' '+r1(y)+'L'+r1(x-10*s)+' '+r1(y)+'Z','#fff',' opacity=".16"');
  b+=E(x,y-24*s,13*s,2.6*s,'#3b2814');
  var n=11,stems='',leaves='';
  for(i=0;i<n;i++){
    var a=(-62+i*(124/(n-1)))+(r()-.5)*10,len=(34+r()*38)*s,ang=a*Math.PI/180;
    var tx=x+Math.sin(ang)*len*.9,ty=y-24*s-Math.cos(ang)*len*1.25;
    var cx=x+Math.sin(ang)*len*.3,cy=y-24*s-len*.55;
    stems+=S('M'+r1(x+(r()-.5)*4*s)+' '+r1(y-24*s)+'Q'+r1(cx)+' '+r1(cy)+' '+r1(tx)+' '+r1(ty),'#3d5d2c',1.1*s);
    var lw=(11+r()*6)*s,lh=(15+r()*7)*s,rot=a*.9+(r()-.5)*24;
    var shade=['#2f6f3a','#3b8445','#4f9a50','#2a5f33'][i%4];
    leaves+=G('translate('+r1(tx)+' '+r1(ty)+') rotate('+r1(rot)+')',
      D('M0 '+r1(lh*.45)+'C'+r1(-lw*1.1)+' '+r1(lh*.1)+' '+r1(-lw*.9)+' '+r1(-lh*.8)+' 0 '+r1(-lh)+'C'+r1(lw*.9)+' '+r1(-lh*.8)+' '+r1(lw*1.1)+' '+r1(lh*.1)+' 0 '+r1(lh*.45)+'Z',shade,INK)+
      D('M0 '+r1(lh*.45)+'C'+r1(lw*.5)+' '+r1(lh*.1)+' '+r1(lw*.6)+' '+r1(-lh*.6)+' 0 '+r1(-lh)+'C'+r1(lw*.9)+' '+r1(-lh*.8)+' '+r1(lw*1.1)+' '+r1(lh*.1)+' 0 '+r1(lh*.45)+'Z','#fff',' opacity=".12"')+
      S('M0 '+r1(lh*.45)+'L0 '+r1(-lh*.92),'#173d20',.6,' opacity=".7"')+
      S('M0 '+r1(lh*.2)+'L'+r1(-lw*.62)+' '+r1(-lh*.05)+'M0 '+r1(-lh*.1)+'L'+r1(-lw*.6)+' '+r1(-lh*.38)+'M0 '+r1(-lh*.4)+'L'+r1(-lw*.45)+' '+r1(-lh*.62)+'M0 '+r1(lh*.2)+'L'+r1(lw*.62)+' '+r1(-lh*.05)+'M0 '+r1(-lh*.1)+'L'+r1(lw*.6)+' '+r1(-lh*.38)+'M0 '+r1(-lh*.4)+'L'+r1(lw*.45)+' '+r1(-lh*.62),'#173d20',.4,' opacity=".5"'));
  }
  return stems+leaves+b.replace('','');
}
/* o vaso vem antes das folhas na ordem de desenho */
function plantFull(u,x,y,s,seed,pot){
  var all=plant(u,x,y,s,seed,pot);
  /* separa: sombra+vaso (b) ficam no fim da string; reordena pondo vaso primeiro */
  var idx=all.indexOf('<ellipse');
  return all.slice(idx)+all.slice(0,idx);
}

/* luminária com cúpula, haste e halo de luz */
function lamp(u,id,x,y,s,warm){
  var d=RG(u,id,x,y-26*s,46*s,[[0,warm,0.7],[0.45,warm,0.22],[1,warm,0]]),b='';
  b+=C(x,y-26*s,46*s,'url(#'+u+'-'+id+')');
  b+=E(x,y,9*s,2*s,'#000',' opacity=".25"')+E(x,y-1,7*s,1.8*s,'#9a7a38')+R(x-1*s,y-26*s,2*s,25*s,'#b8923f')+
     D('M'+r1(x-10*s)+' '+r1(y-26*s)+'L'+r1(x-6*s)+' '+r1(y-40*s)+'L'+r1(x+6*s)+' '+r1(y-40*s)+'L'+r1(x+10*s)+' '+r1(y-26*s)+'Z','#f6e3b2',INK)+
     D('M'+r1(x-10*s)+' '+r1(y-26*s)+'L'+r1(x-6*s)+' '+r1(y-40*s)+'L'+r1(x+6*s)+' '+r1(y-40*s)+'L'+r1(x+10*s)+' '+r1(y-26*s)+'Z',warm,' opacity=".55"')+
     E(x,y-26*s,10*s,1.6*s,'#ffe9b0',' opacity=".85"')+L(x-3*s,y-39*s,x-5.4*s,y-27*s,'#fff',.8,' opacity=".5"');
  return {d:d,b:b};
}

/* moldura com arte (paisagem, retrato abstrato) */
function frame(u,x,y,w,h,kind,seed){
  var r=rng(seed),b='',m=3;
  b+=R(x+1.5,y+2.5,w,h,'#000',' opacity=".22"')+R(x,y,w,h,'#b8923f',INK)+R(x+1,y+1,w-2,h-2,'#e2c071',' opacity=".8"')+R(x+m,y+m,w-2*m,h-2*m,'#f4ecd6');
  var ix=x+m+2,iy=y+m+2,iw=w-2*m-4,ih=h-2*m-4;
  if(kind==='land'){
    b+=R(ix,iy,iw,ih,'#bcd4de')+E(ix+iw*.72,iy+ih*.28,ih*.12,ih*.12,'#fbe8b0')+
       D('M'+ix+' '+r1(iy+ih*.75)+'Q'+r1(ix+iw*.3)+' '+r1(iy+ih*.45)+' '+r1(ix+iw*.55)+' '+r1(iy+ih*.7)+'T'+r1(ix+iw)+' '+r1(iy+ih*.6)+'V'+r1(iy+ih)+'H'+ix+'Z','#6f946a')+
       D('M'+ix+' '+r1(iy+ih*.88)+'Q'+r1(ix+iw*.4)+' '+r1(iy+ih*.66)+' '+r1(ix+iw)+' '+r1(iy+ih*.82)+'V'+r1(iy+ih)+'H'+ix+'Z','#41683f');
  }else if(kind==='abs'){
    var cs=['#e58a64','#4f8f94','#e6b94e','#8b6fc0'];var c=cs[Math.floor(r()*4)];
    b+=R(ix,iy,iw,ih,'#f3e2c4')+E(ix+iw/2,iy+ih*.52,iw*.32,ih*.34,c)+E(ix+iw*.56,iy+ih*.44,iw*.14,ih*.14,'#fff',' opacity=".55"')+D('M'+ix+' '+r1(iy+ih)+'Q'+r1(ix+iw/2)+' '+r1(iy+ih*.7)+' '+r1(ix+iw)+' '+r1(iy+ih)+'Z',cs[(cs.indexOf(c)+1)%4],' opacity=".85"');
  }else{
    b+=R(ix,iy,iw,ih,'#dfe9ee')+E(ix+iw/2,iy+ih*.42,iw*.2,iw*.2,'#c98a62')+D('M'+r1(ix+iw*.12)+' '+r1(iy+ih)+'Q'+r1(ix+iw/2)+' '+r1(iy+ih*.45)+' '+r1(ix+iw*.88)+' '+r1(iy+ih)+'Z','#506e86');
  }
  b+=R(x+m,y+m,w-2*m,2,'#000',' opacity=".12"')+L(x+1,y+1,x+w-1,y+1,'#fff3c8',.5,' opacity=".6"');
  return b;
}

/* relógio redondo de parede */
function clock(u,x,y,rad,hh,mm){
  var b='';
  b+=C(x+1.5,y+2.2,rad,'#000',' opacity=".25"')+C(x,y,rad,'#b58a3a',INK)+C(x,y,rad*.88,'#f6efd9')+C(x,y,rad*.88,'none',' stroke="#7a5a22" stroke-width=".7"');
  for(var i=0;i<12;i++){var an=i*Math.PI/6,a1=rad*.7,a2=rad*.82;b+=L(r1(x+a1*Math.sin(an)),r1(y-a1*Math.cos(an)),r1(x+a2*Math.sin(an)),r1(y-a2*Math.cos(an)),'#3a2a14',i%3===0?1.2:.6);}
  var ha=(hh+mm/60)*30*Math.PI/180,ma=mm*6*Math.PI/180;
  b+=L(x,y,r1(x+rad*.46*Math.sin(ha)),r1(y-rad*.46*Math.cos(ha)),'#2a1c0e',1.5,' stroke-linecap="round"')+L(x,y,r1(x+rad*.7*Math.sin(ma)),r1(y-rad*.7*Math.cos(ma)),'#2a1c0e',1,' stroke-linecap="round"')+C(x,y,1.2,'#b58a3a');
  return b;
}

/* pendente de teto com halo */
function pendant(u,id,x,y0,y1,warm){
  var d=RG(u,id,x,y1,40,[[0,warm,0.55],[0.5,warm,0.16],[1,warm,0]]),b='';
  b+=C(x,y1,40,'url(#'+u+'-'+id+')')+L(x,y0,x,y1-5,'#3a2a14',.9)+D('M'+r1(x-7)+' '+r1(y1)+'Q'+x+' '+r1(y1-12)+' '+r1(x+7)+' '+r1(y1)+'Z','#c49a46',INK)+E(x,y1,7,1.6,'#ffeeb8')+C(x,y1+.8,2.6,'#fffbe6');
  return {d:d,b:b};
}

/* poeira de luz: pontinhos pequenos e suaves (em vez de bolhas gigantes) */
function motes(r,n,x0,y0,x1,y1){
  var s='';for(var i=0;i<n;i++)s+=C(x0+r()*(x1-x0),y0+r()*(y1-y0),.5+r()*1.2,'#fff3d0',' opacity="'+r1(.25+r()*.45)+'"');
  return s;
}

/* mala de viagem */
function suitcase(x,y,w,h,col,col2){
  var b='';
  b+=E(x+w/2,y+h+1,w*.6,2.4,'#000',' opacity=".25"')+RR(x,y,w,h,3,col,INK)+RR(x,y,w,h*.18,3,'#fff',' opacity=".14"')+
     L(x+w*.3,y+1,x+w*.3,y+h-1,col2,.7,' opacity=".6"')+L(x+w*.7,y+1,x+w*.7,y+h-1,col2,.7,' opacity=".6"')+
     RR(x+w*.38,y-5,w*.24,5,1.4,'none',' stroke="#2a1608" stroke-width="1.2"')+C(x+3,y+h+1.4,1.3,'#222')+C(x+w-3,y+h+1.4,1.3,'#222')+
     R(x+w*.1,y+h*.55,w*.8,1.6,col2,' opacity=".55"');
  return b;
}

/* poltrona */
function armchair(u,x,y,s,col,col2){
  var b='';
  b+=E(x+30*s,y+2,36*s,4*s,'#000',' opacity=".24"');
  b+=R(x+5*s,y-2*s,3*s,5*s,'#4a2e1a')+R(x+52*s,y-2*s,3*s,5*s,'#4a2e1a');
  b+=RR(x,y-34*s,60*s,32*s,9*s,col,INK)+RR(x+5*s,y-30*s,50*s,18*s,7*s,col2,INK)+RR(x-6*s,y-26*s,14*s,26*s,6*s,col,INK)+RR(x+52*s,y-26*s,14*s,26*s,6*s,col,INK);
  b+=S('M'+r1(x+8*s)+' '+r1(y-22*s)+'H'+r1(x+52*s),'#fff',.6,' opacity=".25"')+S('M'+r1(x+30*s)+' '+r1(y-29*s)+'V'+r1(y-13*s),'#000',.6,' opacity=".25"');
  b+=RR(x+8*s,y-22*s,44*s,12*s,5*s,'#fff',' opacity=".07"');
  return b;
}


/* tapete oval com bordado, franja e sombra */
function rug(u,cx,cy,rx,ry,c1,c2,c3){
  var b='',i;
  b+=E(cx,cy+2,rx+3,ry+2,'#000',' opacity=".18"')+E(cx,cy,rx,ry,c1,INK)+E(cx,cy,rx*.93,ry*.9,'none',' stroke="'+c3+'" stroke-width="1.4" opacity=".9"')+E(cx,cy,rx*.86,ry*.8,c2)+E(cx,cy,rx*.79,ry*.72,'none',' stroke="'+c3+'" stroke-width=".8" opacity=".8"');
  for(i=0;i<16;i++){var a=i*Math.PI/8,x1=cx+Math.cos(a)*rx*.5,y1=cy+Math.sin(a)*ry*.5,x2=cx+Math.cos(a)*rx*.74,y2=cy+Math.sin(a)*ry*.68;
    b+=L(r1(x1),r1(y1),r1(x2),r1(y2),c3,.7,' opacity=".6"')+C(cx+Math.cos(a)*rx*.62,cy+Math.sin(a)*ry*.6,1.1,c3,' opacity=".75"');}
  b+=E(cx,cy,rx*.3,ry*.28,c1,' opacity=".9"')+E(cx,cy,rx*.2,ry*.18,c3,' opacity=".55"')+E(cx,cy,rx*.08,ry*.07,c1);
  for(i=0;i<46;i++){var a2=i*Math.PI*2/46;b+=L(r1(cx+Math.cos(a2)*rx),r1(cy+Math.sin(a2)*ry),r1(cx+Math.cos(a2)*(rx+3.2)),r1(cy+Math.sin(a2)*(ry+1.3)),'#efe3c4',.6,' opacity=".7"');}
  b+=E(cx,cy-ry*.25,rx*.8,ry*.35,'#fff',' opacity=".06"');
  return b;
}

/* ---------- LOBBY: saguão do hotel ---------- */
/* v=1: vista ampla com elevador e sofá; v=2: balcão em primeiro plano e corredor */
function hotel(u,v){
  var r=rng(v*7919),d='',b='',i,j,k;
  var floorY=152,vy=112;
  d+=LG(u,'ce',0,0,0,32,[[0,'#f0e4cb'],[1,'#dccaa0']]);
  d+=LG(u,'wd',0,38,0,128,[[0,'#6d462c'],[1,'#432816']]);
  d+=LG(u,'br',0,0,1,0,[[0,'#8a6a2c'],[0.5,'#f2d680'],[1,'#a67f33']]);
  d+=LG(u,'ct',0,126,0,134,[[0,'#f1e6d0'],[1,'#cdbd9d']]);
  d+=LG(u,'cf',0,132,0,170,[[0,'#7a4d2c'],[1,'#4e3019']]);
  d+=LG(u,'ev',0,52,0,152,[[0,'#cfd5d8'],[0.5,'#a9b2b7'],[1,'#8a949a']]);
  d+=LG(u,'dsk',0,0,0,1,[[0,'#fff',0.55],[1,'#fff',0]]);
  d+=RG(u,'wl',240,86,210,[[0,'#ffd9a0',0.5],[0.6,'#ffc27a',0.14],[1,'#ffb066',0]]);
  d+=RG(u,'fs',240,170,240,[[0,'#ffe4b0',0.34],[1,'#ffe4b0',0]]);
  d+=vig(u);

  /* paredes */
  var wp=wallpaper(u,30,floorY,['#6c4458','#523345'],'#e2bf72');d+=wp.d;b+=wp.b;
  /* friso e rodapé em painéis */
  b+=R(0,112,480,40,'#3d2a22')+R(0,112,480,40,'#000',' opacity=".12"');
  for(i=-4;i<490;i+=40){b+=R(i+4,117,32,28,'#4a3228',INK)+R(i+6,119,28,24,'none',' stroke="#a78458" stroke-width=".6" opacity=".6"')+R(i+4,117,32,3,'#fff',' opacity=".06"');}
  b+=R(0,109,480,4,'#c9a35a')+R(0,109,480,1.2,'#f6dd96')+R(0,112.4,480,1.4,'#000',' opacity=".3"')+R(0,148,480,5,'#2c1b12')+R(0,148,480,1.2,'#8a6444')+R(0,152,480,2,'#000',' opacity=".25"');
  /* teto com caixotões e sanca */
  b+=R(0,0,480,32,F(u,'ce'));
  for(i=0;i<6;i++){var cxx=i*86-8;b+=R(cxx+4,4,76,20,'#e9dcc0',INK)+R(cxx+8,7,68,14,'#f5ecd7')+R(cxx+8,7,68,2,'#000',' opacity=".07"');}
  b+=R(0,26,480,6,'#e6d6b0')+R(0,30,480,1.4,'#b99a5e')+R(0,31.4,480,3,'#000',' opacity=".18"')+R(0,26,480,1,'#fff8e0',' opacity=".8"');
  for(i=0;i<480;i+=9)b+=R(i,27.4,4.6,2.4,'#cdb27a',' opacity=".7"');
  /* luz quente nas paredes */
  b+=R(0,32,480,120,'url(#'+u+'-wl)');

  var lights=[],fg='';
  /* ---- composição ---- */
  if(v===1){
    /* elevador */
    b+=elevatorBlock(u,d,28,48);d=d+elevatorDefs;
    /* parede da recepção */
    b+=keyWall(u,150,34,176,94,'HOTEL PLAZA',r);
    b+=clock(u,352,70,14,3,48);
    b+=frame(u,384,46,40,50,'land',5);
    /* balcão */
    b+=deskBlock(u,112,126,254);
    /* área de estar (sofá + luminária + planta) */
    b+=armchair(u,380,152,.95,'#7a3f3a','#9a5248');
    var lp=lamp(u,'l1',446,152,.95,'#ffd88a');d+=lp.d;b+=lp.b;
    b+=plantFull(u,470,153,1.0,9,['#d8d0bf','#b9ae98']);
    b+=pendantRow(u,d,[118,346]);d=d+pendantDefs;
    lights=[[118,160,56,'#fff0c0'],[346,160,56,'#fff0c0'],[446,164,26,'#ffd88a'],[240,170,120,'#ffe4a8']];
    fg+=rug(u,300,224,112,18,'#8a3a36','#a64a42','#e8cf98');
    fg+=cartBlock(u,104,228);
  }else{
    /* balcão à esquerda em primeiro plano + corredor à direita */
    b+=keyWall(u,40,34,176,94,'WELCOME · ROOM 305',r);
    /* corredor com portas numeradas */
    b+=corridor(u,276,34,r);
    b+=deskBlock(u,8,126,252);
    b+=plantFull(u,268,153,.9,21,['#d8d0bf','#b9ae98']);
    b+=pendantRow(u,d,[246,372]);d=d+pendantDefs;
    lights=[[246,160,56,'#fff0c0'],[372,160,60,'#fff0c0'],[130,170,100,'#ffe4a8']];
    fg+=rug(u,200,224,112,18,'#2f5d6e','#3d7184','#e8cf98');
    fg+=cartBlock(u,334,230);
  }
  /* piso (depois dos móveis na lista, mas inserido antes na pilha) */
  var fl=marbleFloor(u,floorY,vy,v*131,['#efe6d6','#e2d6c0','#d2c3a8','#a79677'],lights);
  d+=fl.d;
  var floorPieces=fl.b+R(0,floorY,480,118,'url(#'+u+'-fs)');
  /* poeira de luz */
  b+=motes(r,26,0,34,480,150);

  /* ordem final: fundo (b até o piso) -> piso -> móveis. como b já mistura, o piso fica atrás via inserção */
  return WRAP(u,d,floorLayer(u,floorY)+floorPieces+b+fg);
}
function floorLayer(u,y){return R(0,y,480,270-y,'#d9ccb2');}

/* ---- blocos do saguão ---- */
var elevatorDefs='',pendantDefs='';
function elevatorBlock(u,d,x,y){
  elevatorDefs='';
  var b='',w=66,h=104;
  b+=R(x-5,y-4,w+10,h+6,'#b8923f',INK)+R(x-3,y-2,w+6,h+4,'#7a5a22');
  b+=R(x,y,w,h,'url(#'+u+'-ev)');
  b+=R(x+w/2-.7,y,1.4,h,'#4a5258')+R(x+w/2-.7,y,.5,h,'#fff',' opacity=".5"');
  for(var i=0;i<6;i++){b+=R(x+3+i*5,y,2.2,h,'#fff',' opacity="'+r1(.07+(i%2)*.06)+'"')+R(x+w/2+3+i*5,y,1.6,h,'#fff',' opacity="'+r1(.05+(i%2)*.05)+'"');}
  b+=P((x)+','+(y)+' '+(x+22)+','+(y)+' '+(x+8)+','+(y+h)+' '+x+','+(y+h),'#fff',' opacity=".13"');
  b+=R(x,y+h-4,w,4,'#6a747a')+R(x,y+h-1,w,1,'#000',' opacity=".3"');
  /* indicador */
  b+=R(x+w/2-18,y-17,36,12,'#17110c',INK)+R(x+w/2-17,y-16,34,10,'none',' stroke="#c9a35a" stroke-width=".6"')+T(x+w/2-6,y-7.5,'1',8.2,'#ffa23a',{f:'Arial,sans-serif',w:'bold'})+D('M'+(x+w/2+4)+' '+(y-7)+'L'+(x+w/2+8)+' '+(y-14)+'L'+(x+w/2+12)+' '+(y-7)+'Z','#ffa23a');
  /* botão */
  b+=RR(x+w+9,y+44,8,14,2,'#c9a35a',INK)+C(x+w+13,y+49,2.1,'#ffb84a')+C(x+w+13,y+49,4.2,'#ffb84a',' opacity=".25"')+C(x+w+13,y+54,1.6,'#e2e2e2');
  /* reflexo no piso */
  b+=E(x+w/2,y+h+6,w*.55,5,'#ffe9bd',' opacity=".12"');
  return b;
}
function keyWall(u,x,y,w,h,sign,r){
  var b='',i,j;
  b+=R(x-6,y-2,w+12,h+6,'#2a1a10',INK)+R(x,y,w,h,'url(#'+u+'-wd)');
  for(i=x+3;i<x+w;i+=7){b+=R(i,y,.9,h,'#000',' opacity=".26"')+R(i+1,y,.6,h,'#fff',' opacity=".05"');}
  b+=R(x-6,y-2,w+12,3,'#caa05a')+R(x-6,y-2,w+12,1,'#f4dc92');
  /* placa com nome */
  var sw=Math.min(w-26,(sign.length*6.4)+30);
  b+=R(x+w/2-sw/2,y+5,sw,13,'#1c120a',INK)+R(x+w/2-sw/2+1,y+6,sw-2,11,'none',' stroke="#e0bd6a" stroke-width=".7"')+T(x+w/2,y+14.6,sign,7.2,'#f1d88c',{a:'middle',w:'bold',ls:'1.1'});
  /* escaninhos com chaves */
  var cols=Math.floor((w-14)/13),rows=5,sx=x+7,sy=y+26;
  b+=R(sx-2,sy-2,cols*13+4,rows*11.4+4,'#2a1a10',' stroke="#caa05a" stroke-width=".8"');
  for(j=0;j<rows;j++)for(i=0;i<cols;i++){
    var cx=sx+i*13,cy=sy+j*11.4;
    b+=R(cx+.6,cy+.6,12,10.4,'#1b110a')+R(cx+.6,cy+.6,12,1.4,'#000',' opacity=".5"')+R(cx+.6,cy+10,12,.8,'#caa05a',' opacity=".55"');
    var occupied=r()>.35;
    if(occupied){
      var kc=['#e6c35c','#dcdcdc','#cf9a45'][(i+j)%3];
      b+=L(cx+6.2,cy+1.4,cx+6.2,cy+6,kc,.8)+C(cx+6.2,cy+7.4,1.8,'none',' stroke="'+kc+'" stroke-width=".8"')+R(cx+4.2,cy+3.6,4,3.4,['#f3ead2','#b8402f','#f3ead2','#2f7c7c'][(i*2+j)%4],' rx=".5"');
      b+=T(cx+6.2,cy+6.2,String(((i+j*cols)*7%9)+1),2.4,'#222',{a:'middle',f:'Arial',w:'bold'});
    }else if(r()>.6){b+=R(cx+2,cy+4,9,5,'#efe4c8',' opacity=".9"')+D('M'+(cx+2)+' '+(cy+4)+'L'+(cx+6.5)+' '+(cy+7)+'L'+(cx+11)+' '+(cy+4)+'Z','#d9cba8');}
  }
  return b;
}
function deskBlock(u,x,y,w){
  var b='',i;
  b+=E(x+w/2,y+46,w*.56,5.4,'#000',' opacity=".28"');
  /* tampo de mármore */
  b+=P((x-4)+','+(y+7)+' '+(x+8)+','+y+' '+(x+w-8)+','+y+' '+(x+w+4)+','+(y+7),'#f3ebd9',INK)+R(x-4,y+7,w+8,4,'#e1d5bb',INK)+R(x-4,y+7,w+8,1,'#fff',' opacity=".7"');
  b+=S('M'+(x+30)+' '+(y+3)+'Q'+(x+60)+' '+(y+6)+' '+(x+90)+' '+(y+2),'#b9a98a',.4,' opacity=".5"')+S('M'+(x+150)+' '+(y+5)+'Q'+(x+190)+' '+(y+2)+' '+(x+230)+' '+(y+6),'#b9a98a',.4,' opacity=".4"');
  /* frente em madeira canelada */
  b+=R(x,y+11,w,34,'url(#'+u+'-cf)',INK);
  for(i=x+5;i<x+w-3;i+=5.2){b+=R(i,y+13,1.3,30,'#000',' opacity=".26"')+R(i+1.4,y+13,.6,30,'#fff',' opacity=".08"');}
  /* painéis e filete latão */
  for(i=0;i<4;i++){var px=x+8+i*((w-16)/4);b+=R(px+3,y+16,(w-16)/4-9,22,'none',' stroke="#caa05a" stroke-width=".7" opacity=".55"');}
  b+=R(x,y+11,w,1.6,'#e0a870',' opacity=".7"')+R(x,y+38,w,1.6,'url(#'+u+'-br)')+R(x,y+40,w,5,'#2e1d12')+R(x,y+40,w,1,'#8a6444',' opacity=".6"');
  /* sobre o tampo */
  /* sino */
  b+=E(x+w*.45,y+2.6,7,1.8,'#a37d30')+D('M'+(x+w*.45-6)+' '+(y+2.4)+'Q'+(x+w*.45-6)+' '+(y-5)+' '+(x+w*.45)+' '+(y-5)+'T'+(x+w*.45+6)+' '+(y+2.4)+'Z','#e0b74e',INK)+C(x+w*.45,y-6,1.2,'#a37d30')+S('M'+(x+w*.45-3.4)+' '+(y+1)+'Q'+(x+w*.45-3.4)+' '+(y-3)+' '+(x+w*.45-1)+' '+(y-3.8),'#fff6cc',.8,' opacity=".8"');
  /* monitor visto por trás */
  var mx=x+w*.62;
  b+=R(mx,y-18,28,17,'#2b2e33',INK)+R(mx,y-18,28,1.4,'#555a62')+C(mx+14,y-9,1.2,'#8a8f98')+R(mx+12,y-1,4,2.6,'#202328')+E(mx+14,y+2.6,8,1.4,'#202328');
  /* porta-folhetos */
  var fx=x+w*.3;
  b+=P((fx)+','+(y+1)+' '+(fx+13)+','+(y+1)+' '+(fx+12)+','+(y-11)+' '+(fx+1)+','+(y-11),'#ece5d3',INK)+R(fx+1,y-7,11,1.2,'#b8402f')+R(fx+1,y-3.6,11,1.2,'#2f7c7c');
  /* cartões de chave */
  b+=RR(x+w*.2,y+1,8,2,.6,'#f1f1f1',INK)+RR(x+w*.2+3,y,8,2,.6,'#d9a441',INK);
  /* arranjo de orquídeas */
  var ox=x+w-26;
  b+=D('M'+(ox-5)+' '+(y+1)+'L'+(ox+5)+' '+(y+1)+'L'+(ox+4)+' '+(y-9)+'L'+(ox-4)+' '+(y-9)+'Z','#9aa7ad',INK)+S('M'+ox+' '+(y-9)+'Q'+(ox+2)+' '+(y-22)+' '+(ox+8)+' '+(y-28),'#4b6a3a',1)+S('M'+ox+' '+(y-9)+'Q'+(ox-2)+' '+(y-20)+' '+(ox-8)+' '+(y-25),'#4b6a3a',1);
  [[8,-28],[4,-24],[-8,-25],[-4,-20]].forEach(function(p){b+=C(ox+p[0],y+p[1],2.8,'#fff7f0',INK)+C(ox+p[0],y+p[1],1,'#e9a0c0');});
  /* luminária de mesa */
  var lamx=x+16;
  b+=R(lamx-.8,y-14,1.6,14,'#b8923f')+D('M'+(lamx-8)+' '+(y-14)+'L'+(lamx-4)+' '+(y-26)+'L'+(lamx+4)+' '+(y-26)+'L'+(lamx+8)+' '+(y-14)+'Z','#f1dfae',INK)+E(lamx,y+1,6,1.4,'#a37d30');
  b+=E(lamx,y-14,9,1.6,'#ffe6a8',' opacity=".8"');
  return b;
}
function cartBlock(u,x,y){
  var b='';
  b+=E(x+26,y+14,34,3.4,'#000',' opacity=".25"');
  b+=S('M'+x+' '+(y-34)+'V'+(y+10)+'M'+(x+52)+' '+(y-34)+'V'+(y+10)+'M'+(x-4)+' '+(y-34)+'H'+(x+56),'#d4a94c',1.5,' stroke-linecap="round"');
  b+=S('M'+x+' '+(y-34)+'V'+(y+10),'#fff0b8',.5,' opacity=".7"');
  b+=R(x-2,y+2,56,2.4,'#b8923f',INK)+C(x+4,y+12,2.8,'#2a2a2a')+C(x+48,y+12,2.8,'#2a2a2a')+C(x+4,y+12,1,'#888')+C(x+48,y+12,1,'#888');
  b+=suitcase(x+4,y-14,28,16,'#8b3d3a','#e6c35c')+suitcase(x+30,y-24,22,26,'#2f5d6e','#e6c35c')+suitcase(x+8,y-30,22,15,'#c98a48','#6b3f1c');
  return b;
}
function pendantRow(u,d,xs){
  var b='';pendantDefs='';
  xs.forEach(function(x,i){var p=pendant(u,'pd'+i,x,26,40+(i%2)*4,'#ffd88a');pendantDefs+=p.d;b+=p.b;});
  return b;
}
function corridor(u,x,y,r){
  var b='',i;
  var w=170,h=120;
  b+=R(x,y,w,h,'#2d1f20',INK);
  /* fuga de perspectiva do corredor */
  b+=P(x+','+y+' '+(x+w)+','+y+' '+(x+w-34)+','+(y+26)+' '+(x+34)+','+(y+26),'#3a2a28');
  b+=P(x+','+(y+h)+' '+(x+34)+','+(y+h-26)+' '+(x+w-34)+','+(y+h-26)+' '+(x+w)+','+(y+h),'#6f5a44');
  b+=P(x+','+y+' '+(x+34)+','+(y+26)+' '+(x+34)+','+(y+h-26)+' '+x+','+(y+h),'#4a3231');
  b+=P((x+w)+','+y+' '+(x+w-34)+','+(y+26)+' '+(x+w-34)+','+(y+h-26)+' '+(x+w)+','+(y+h),'#3d2a2a');
  b+=R(x+34,y+26,w-68,h-52,'#caa98a');
  /* portas do fundo */
  for(i=0;i<3;i++){var dx=x+46+i*34;b+=R(dx,y+40,22,h-66,'#6a4630',INK)+R(dx+3,y+44,16,h-74,'none',' stroke="#caa05a" stroke-width=".5" opacity=".6"')+C(dx+18,y+h*.52,1,'#e6c35c')+R(dx+5,y+47,12,5,'#e6c35c',' opacity=".85"')+T(dx+11,y+51,String(301+i*2),3.6,'#2a1a10',{a:'middle',f:'Arial',w:'bold'});}
  /* luzes do corredor */
  for(i=0;i<4;i++){var lxx=x+24+i*40;b+=E(lxx+(i*3),y+8+i*4,10-i*1.6,2.4,'#fff1c8',' opacity=".9"')+E(lxx+(i*3),y+9+i*4,16-i*2,4,'#ffe29a',' opacity=".2"');}
  /* tapete vermelho */
  b+=P((x+54)+','+(y+h)+' '+(x+w-54)+','+(y+h)+' '+(x+w-72)+','+(y+h-26)+' '+(x+72)+','+(y+h-26),'#9b3a35');
  b+=L(x+60,y+h,x+76,y+h-26,'#e6c35c',.8,' opacity=".8"')+L(x+w-60,y+h,x+w-76,y+h-26,'#e6c35c',.8,' opacity=".8"');
  /* moldura do vão */
  b+=R(x-4,y-3,w+8,4,'#c9a35a')+R(x-4,y-3,4,h+3,'#c9a35a')+R(x+w,y-3,4,h+3,'#c9a35a')+R(x-4,y-3,w+8,1,'#f6dd96');
  return b;
}

/* ---------- registro: cai no cenário antigo se algo falhar ---------- */
function reg(key,fn){
  var old=RS[key];
  RS[key]=function(u){try{return fn(u)}catch(e){if(window.console)console.warn('scn_fine '+key,e);return old?old(u):''}};
}
/* biblioteca compartilhada com scn_fine2.js */
window.SF={rng:rng,r1:r1,LG:LG,RG:RG,R:R,RR:RR,E:E,C:C,L:L,P:P,D:D,S:S,T:T,G:G,F:F,INK:INK,WRAP:WRAP,vig:vig,marbleFloor:marbleFloor,wallpaper:wallpaper,plantFull:plantFull,lamp:lamp,frame:frame,clock:clock,pendant:pendant,motes:motes,suitcase:suitcase,armchair:armchair,rug:rug,reg:reg};
reg('lobby1',function(u){return hotel(u,1)});
reg('lobby2',function(u){return hotel(u,2)});
})();
