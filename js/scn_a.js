/* Pogglot - realistic illustrated scenes A: cafe, living, market (deterministic SVG) */
(function(){
window.RS = window.RS || {};
var R = function(v){ return Math.round(v*10)/10; };

function wrap(u, defs, body){
  return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 270" width="100%" height="100%" style="width:100%;height:100%;display:block" preserveAspectRatio="xMidYMid slice" role="img" aria-hidden="true"><defs>' +
    '<filter id="'+u+'-bl" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="3"/></filter>' +
    '<filter id="'+u+'-nz" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" seed="4"/><feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .9 -.35"/></filter>' +
    '<radialGradient id="'+u+'-vg" cx=".5" cy=".5" r=".75"><stop offset=".6" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#1a0d05" stop-opacity=".35"/></radialGradient>' +
    defs + '</defs>' + body +
    '<rect width="480" height="270" filter="url(#'+u+'-nz)" opacity=".07"/>' +
    '<rect width="480" height="270" fill="url(#'+u+'-vg)"/></svg>';
}
function lg(id, stops, x1, y1, x2, y2){
  var s = '<linearGradient id="'+id+'" x1="'+(x1||0)+'" y1="'+(y1||0)+'" x2="'+(x2===undefined?0:x2)+'" y2="'+(y2===undefined?1:y2)+'">';
  for (var i=0;i<stops.length;i++) s += '<stop offset="'+stops[i][0]+'" stop-color="'+stops[i][1]+'"'+(stops[i][2]!==undefined?' stop-opacity="'+stops[i][2]+'"':'')+'/>';
  return s + '</linearGradient>';
}
function rg(id, c1, c2, cx, cy, r){
  return '<radialGradient id="'+id+'" cx="'+(cx||.35)+'" cy="'+(cy||.3)+'" r="'+(r||.8)+'"><stop offset="0" stop-color="'+c1+'"/><stop offset="1" stop-color="'+c2+'"/></radialGradient>';
}
function rect(x,y,w,h,f,x2){ return '<rect x="'+x+'" y="'+y+'" width="'+w+'" height="'+h+'" fill="'+f+'"'+(x2||'')+'/>'; }
function ell(cx,cy,rx,ry,f,x2){ return '<ellipse cx="'+cx+'" cy="'+cy+'" rx="'+rx+'" ry="'+ry+'" fill="'+f+'"'+(x2||'')+'/>'; }
function shadow(u,cx,cy,rx,ry,o){ return ell(cx,cy,rx,ry,'#1b0e06',' opacity="'+(o||.35)+'" filter="url(#'+u+'-bl)"'); }
function awning(x0,x1,ya,yb,c1,c2,n){
  var s='', w=(x1-x0)/n, ins=10, tw=(x1-x0-2*ins)/n;
  for (var i=0;i<n;i++){
    var f=(i%2)?c2:c1, a=x0+ins+i*tw, b=a+tw, c=x0+i*w, d=c+w;
    s += '<path d="M'+R(a)+' '+ya+'L'+R(b)+' '+ya+'L'+R(d)+' '+yb+'L'+R(c)+' '+yb+'Z" fill="'+f+'"/>' +
         '<path d="M'+R(c)+' '+yb+'Q'+R(c+w/2)+' '+(yb+10)+' '+R(d)+' '+yb+'Z" fill="'+f+'"/>';
  }
  return s;
}
function heap(cx,cy,w,rows,fills,r){
  var s='', k=0;
  for (var j=0;j<rows;j++){
    var cnt = Math.max(3, Math.floor((w - j*r*1.7)/(r*1.8)));
    var y = cy - j*r*1.45, x0 = cx - (cnt-1)*r*0.92;
    for (var i=0;i<cnt;i++){
      s += '<circle cx="'+R(x0+i*r*1.84 + ((j*3+i*5)%3-1)*.5)+'" cy="'+R(y + ((i*7+j)%3-1)*.6)+'" r="'+r+'" fill="url(#'+fills[(k++)%fills.length]+')"/>';
    }
  }
  return s;
}
function crate(x,y,w,h,c1,c2){
  var s = rect(x,y,w,h,c1) + rect(x,y,w,2.2,'#e0b987',' opacity=".55"');
  for (var yy=y+h/3; yy<y+h-1; yy+=h/3) s += rect(x,R(yy),w,.9,'#2b1a0d',' opacity=".55"');
  s += rect(x,y,2.5,h,c2) + rect(x+w-2.5,y,2.5,h,c2);
  return s;
}

/* ================= CAFE ================= */
RS.cafe = function(u){
  var d =
    lg(u+'-wall',[[0,'#5b3b2b'],[1,'#8a6046']]) +
    lg(u+'-floor',[[0,'#6e4c34'],[.35,'#a47c58'],[1,'#c19a72']]) +
    lg(u+'-sky',[[0,'#bcd3e4'],[.6,'#eadfc9'],[1,'#f2d9ab']]) +
    lg(u+'-ctr',[[0,'#7a4a2c'],[1,'#4e2d1a']]) +
    lg(u+'-top',[[0,'#d9a66e'],[1,'#a86f3f']]) +
    lg(u+'-steel',[[0,'#7b838a'],[.3,'#eef1f2'],[.55,'#a4acb2'],[1,'#6c747b']],0,0,1,0) +
    lg(u+'-gl',[[0,'#fff',.45],[1,'#fff',0]],0,0,1,1) +
    lg(u+'-beam',[[0,'#ffe3a8',.38],[1,'#ffe3a8',0]],0,0,.3,1) +
    lg(u+'-case',[[0,'#d8c9b4'],[1,'#9d8a74']]) +
    lg(u+'-brd',[[0,'#26302c'],[1,'#161d1a']]) +
    rg(u+'-lamp','#ffd990','#ffd990',.5,.5,.5).replace('stop-color="#ffd990"/></radial','stop-color="#ffd990" stop-opacity="0"/></radial') +
    rg(u+'-cr','#e8a95a','#b36c27') + rg(u+'-dn','#f0b8c4','#c9798c') + rg(u+'-mf','#d09a5e','#8d5a2b') +
    '<pattern id="'+u+'-brk" width="22" height="9" patternUnits="userSpaceOnUse"><rect width="22" height="9" fill="#7a4a36"/><rect y="4.2" width="22" height=".8" fill="#2d1a10" opacity=".5"/><rect y="8.6" width="22" height=".8" fill="#2d1a10" opacity=".5"/><rect x="5" width=".8" height="4.4" fill="#2d1a10" opacity=".5"/><rect x="16" y="4.6" width=".8" height="4.4" fill="#2d1a10" opacity=".5"/></pattern>' +
    '<clipPath id="'+u+'-win"><rect x="72" y="42" width="154" height="102"/></clipPath>';

  var b = '';
  // wall + brick
  b += rect(0,0,480,170,'url(#'+u+'-wall)');
  b += rect(0,0,480,170,'url(#'+u+'-brk)',' opacity=".38"');
  // floor with plank lines
  b += rect(0,165,480,105,'url(#'+u+'-floor)');
  for (var i=-8;i<=16;i++){ b += '<line x1="'+R(240+i*20)+'" y1="165" x2="'+R(240+i*58)+'" y2="270" stroke="#4a2f1c" stroke-opacity=".22" stroke-width=".7"/>'; }
  b += rect(0,162,480,4,'#3c2517',' opacity=".8"');
  // street seen through window (blurred)
  b += '<g clip-path="url(#'+u+'-win)"><g filter="url(#'+u+'-bl)">' +
    rect(60,30,180,125,'url(#'+u+'-sky)') +
    rect(70,66,26,80,'#8d8478') + rect(96,52,34,94,'#a9715a') + rect(130,74,30,70,'#78818c') + rect(160,58,38,88,'#b99a76') + rect(198,70,34,76,'#7f7a74') +
    '<g fill="#ffd27a" opacity=".85">' + rect(102,62,5,5,'#ffd27a') + rect(114,74,5,5,'#ffd27a') + rect(102,90,5,5,'#ffd27a') + rect(168,70,5,5,'#ffd27a') + rect(182,86,5,5,'#ffd27a') + rect(140,90,4,5,'#ffd27a') + '</g>' +
    ell(88,112,20,22,'#5f7a4a') + ell(212,116,18,20,'#617c4d') +
    rect(60,128,180,20,'#8b8a86') + rect(60,126,180,3,'#b7b3aa') +
    rect(138,118,46,13,'#e6b52f') + rect(150,111,24,9,'#d9a424') + rect(142,129,8,6,'#222') + rect(172,129,8,6,'#222') +
    ell(110,120,3,3,'#ff9a5a') + ell(196,122,3.5,3.5,'#ffe2a0') + ell(124,124,2.5,2.5,'#fff0c4') +
    '</g></g>';
  // window frame, mullions, glass reflections
  b += rect(72,42,154,102,'url(#'+u+'-gl)',' opacity=".55"');
  b += '<path d="M72 42L120 42L72 100Z" fill="#fff" opacity=".12"/><path d="M150 144L212 42L226 42L226 60L176 144Z" fill="#fff" opacity=".1"/>';
  b += '<path d="M66 36H232V150H66ZM72 42V144H226V42Z" fill="#1f1a17" fill-rule="evenodd"/>';
  b += rect(122,42,3.5,102,'#1f1a17') + rect(174,42,3.5,102,'#1f1a17') + rect(72,100,154,3,'#1f1a17');
  b += rect(72,42,154,1.5,'#000',' opacity=".25"');
  b += rect(61,148,178,5,'#b98a57') + rect(61,148,178,1.4,'#e5bf8c') + rect(61,153,178,2,'#2e1c10',' opacity=".4"');
  // plant on sill
  b += '<path d="M205 148l2.5-12h10l2.5 12z" fill="#b5654a"/>' +
    '<path d="M212 136c-8-8-14-4-16-12 8 0 14 4 16 12zM212 136c0-10 4-16 10-20 2 8-2 16-10 20zM212 136c6-4 14-4 18-10-8-2-16 2-18 10z" fill="#4d7a3d"/>' +
    '<path d="M212 136c-3-5-6-8-10-10" stroke="#355c2c" stroke-width=".8" fill="none"/>';
  // light beam on floor + wall
  b += '<path d="M72 144L226 144L330 262L96 262Z" fill="url(#'+u+'-beam)" opacity=".4"/>';
  b += '<path d="M90 168L214 168L292 262L128 262Z" fill="#ffe0a0" opacity=".12"/>';

  // back shelf & counter back
  b += rect(256,100,230,3,'#3e2616') + rect(256,103,230,2,'#000',' opacity=".25"');
  var cups = [[264,'#e9e2d3'],[276,'#c7523f'],[288,'#e9e2d3'],[432,'#e9e2d3'],[444,'#4a7c8c'],[456,'#e9e2d3']];
  for (i=0;i<cups.length;i++) b += '<path d="M'+cups[i][0]+' 100l1.5-8h8l1.5 8z" fill="'+cups[i][1]+'"/>';
  b += '<rect x="418" y="86" width="10" height="14" rx="2" fill="#d7c9a8" opacity=".8"/><rect x="418" y="86" width="10" height="3" rx="1.5" fill="#3b2a1d"/>';
  // chalkboard menu
  b += rect(296,40,108,52,'#3a2415') + rect(299,43,102,46,'url(#'+u+'-brd)') +
    '<g font-family="Georgia,serif" fill="#efe8d8" opacity=".9"><text x="350" y="54" font-size="8" text-anchor="middle" font-weight="bold">COFFEE</text>' +
    '<text x="305" y="64" font-size="5.6">Espresso</text><text x="395" y="64" font-size="5.6" text-anchor="end">$3</text>' +
    '<text x="305" y="72" font-size="5.6">Latte</text><text x="395" y="72" font-size="5.6" text-anchor="end">$4.5</text>' +
    '<text x="305" y="80" font-size="5.6">Croissant</text><text x="395" y="80" font-size="5.6" text-anchor="end">$3.5</text></g>' +
    '<path d="M304 57H396" stroke="#efe8d8" stroke-width=".5" opacity=".5"/>';

  // pendant lamps
  var lamps=[150,290,400];
  for (i=0;i<lamps.length;i++){
    var x=lamps[i];
    b += '<circle cx="'+x+'" cy="40" r="42" fill="url(#'+u+'-lamp)" opacity=".5"/>';
    b += '<line x1="'+x+'" y1="0" x2="'+x+'" y2="24" stroke="#1a1411" stroke-width="1"/>';
    b += '<path d="M'+(x-13)+' 38Q'+(x-12)+' 24 '+x+' 22Q'+(x+12)+' 24 '+(x+13)+' 38Z" fill="#26211d"/>';
    b += '<path d="M'+(x-13)+' 38Q'+x+' 42 '+(x+13)+' 38Q'+x+' 35 '+(x-13)+' 38Z" fill="#ffe2a0"/>';
  }

  // pastry case
  b += shadow(u,300,148,40,3,.3);
  b += rect(262,116,78,32,'url(#'+u+'-case)') + rect(264,118,74,28,'#3a2a1f');
  b += rect(264,118,74,28,'#ffcf86',' opacity=".25"');
  b += rect(264,132,74,1.6,'#e6d6bd',' opacity=".8"');
  for (i=0;i<4;i++){
    var cx=273+i*17;
    b += '<ellipse cx="'+cx+'" cy="130" rx="6.5" ry="3.4" fill="url(#'+u+'-cr)" transform="rotate('+(i%2?-8:6)+' '+cx+' 130)"/>' +
      '<path d="M'+(cx-3)+' 127.8q1.6 2.5 0 4.5M'+(cx+1)+' 127.4q1.6 2.8 0 5" stroke="#8a4d18" stroke-width=".7" fill="none"/>';
    b += '<circle cx="'+(cx+2)+'" cy="143" r="4.6" fill="url(#'+u+'-dn)"/><circle cx="'+(cx+2)+'" cy="143" r="1.3" fill="#3a2a1f"/>';
  }
  b += '<path d="M324 147l2-6h7l2 6z" fill="#b97b3c"/><path d="M323 141q6-8 13 0z" fill="url(#'+u+'-mf)"/>';
  b += '<path d="M262 116H340L322 148H262Z" fill="#fff" opacity=".13"/>' + rect(262,115,78,2,'#e4ddd1') + rect(262,146,78,2,'#6b5a49');
  b += '<rect x="302" y="140" width="10" height="6" fill="#f3ead2" transform="rotate(-4 307 143)"/><text x="307" y="145" font-family="Arial,sans-serif" font-size="4.4" text-anchor="middle" fill="#7a2b1c" transform="rotate(-4 307 143)">$3</text>';

  // espresso machine
  b += '<g transform="translate(-8 0)">';
  b += shadow(u,386,148,34,3,.35);
  b += rect(352,108,68,4,'url(#'+u+'-steel)') + '<path d="M356 108l1-5h8l1 5zM370 108l1-5h8l1 5z" fill="#efe8dc"/>';
  b += '<rect x="352" y="112" width="68" height="31" rx="3" fill="url(#'+u+'-steel)"/>';
  b += rect(352,112,68,3,'#1b1e20',' opacity=".25"');
  b += '<circle cx="386" cy="122" r="5" fill="#f2f2ee" stroke="#555b60" stroke-width="1.2"/><path d="M386 122l2.5-2.5" stroke="#b22" stroke-width=".8"/>';
  b += rect(364,128,14,5,'#272b2d') + rect(394,128,14,5,'#272b2d');
  b += '<path d="M360 133h16v3h-16zM392 133h16v3h-16z" fill="#1b1e20"/><path d="M362 135l-14 3" stroke="#251a12" stroke-width="2.6" stroke-linecap="round"/><path d="M410 135l12 3" stroke="#251a12" stroke-width="2.6" stroke-linecap="round"/>';
  b += rect(358,140,56,4,'#2c3033') + rect(358,140,56,1,'#8a9298');
  b += '<path d="M424 118v20" stroke="#9aa2a8" stroke-width="1.6"/><path d="M424 138q4 0 4 4" stroke="#9aa2a8" stroke-width="1.6" fill="none"/>';
  b += '<rect x="352" y="112" width="12" height="31" rx="3" fill="#fff" opacity=".18"/>';
  b += '</g>';

  // counter
  b += shadow(u,360,201,120,4,.45);
  b += rect(250,153,240,46,'url(#'+u+'-ctr)');
  for (i=0;i<14;i++) b += rect(256+i*17,156,.9,36,'#000',' opacity=".25"') + rect(257+i*17,156,.6,36,'#d9a066',' opacity=".12"');
  b += rect(250,191,240,8,'#241610') + rect(250,153,240,3,'#2b1a0f',' opacity=".5"');
  b += rect(246,145,244,8,'url(#'+u+'-top)') + rect(246,145,244,1.4,'#f2cf9c') + rect(246,152,244,1.4,'#3c2412',' opacity=".6"');
  b += '<rect x="246" y="145" width="244" height="8" fill="#ffe7b0" opacity=".12"/>';

  // table & stools (front of window)
  b += shadow(u,142,203,34,4,.5);
  b += rect(139,162,5,38,'#1d1a18') + ell(141.5,200,15,3.4,'#1d1a18');
  b += ell(141.5,164,30,7.5,'#2a1d14') + ell(141.5,162,30,7.5,'#d0a574') + ell(141.5,161.4,26,5.8,'#e2bd8e',' opacity=".55"');
  b += '<ellipse cx="141.5" cy="162" rx="30" ry="7.5" fill="none" stroke="#7a4f2d" stroke-width=".8"/>';
  b += '<path d="M131 159l1.2-6h8l1.2 6z" fill="#f4efe6"/><ellipse cx="135.2" cy="153" rx="4" ry="1.1" fill="#4a2a18"/><path d="M140.6 155.5q4 0 0 3" stroke="#f4efe6" stroke-width="1" fill="none"/>' +
    ell(135.5,160.4,6,1.5,'#f4efe6',' opacity=".95"') + '<rect x="148" y="158" width="10" height="2" fill="#e8dcc0" transform="rotate(8 150 159)"/>';
  var st=[[98,196],[186,198]];
  for (i=0;i<2;i++){
    var sx=st[i][0], sy=st[i][1];
    b += shadow(u,sx+2,sy+2,15,3,.45);
    b += '<path d="M'+(sx-9)+' '+(sy-28)+'L'+(sx-13)+' '+sy+'M'+(sx+9)+' '+(sy-28)+'L'+(sx+13)+' '+sy+'M'+(sx-3)+' '+(sy-28)+'L'+(sx-5)+' '+(sy+1)+'M'+(sx+4)+' '+(sy-28)+'L'+(sx+6)+' '+(sy+1)+'" stroke="#1d1a18" stroke-width="2" stroke-linecap="round"/>';
    b += ell(sx,sy-12,10.5,2.2,'none',' stroke="#1d1a18" stroke-width="1"');
    b += ell(sx,sy-27,12,3.6,'#3b2416') + ell(sx,sy-29,12,3.6,'#a4623a') + ell(sx-2,sy-29.6,7,2,'#c98355',' opacity=".6"');
  }
  return wrap(u, d, b);
};

/* ================= LIVING ROOM ================= */
RS.living = function(u){
  var d =
    lg(u+'-wall',[[0,'#e6dcc6'],[1,'#d3c4a6']]) +
    lg(u+'-floor',[[0,'#8e6540'],[.3,'#b58a5c'],[1,'#cfa876']]) +
    lg(u+'-sky',[[0,'#a9cfe8'],[.7,'#e7f0ef'],[1,'#f6efd4']]) +
    lg(u+'-sofa',[[0,'#6f9094'],[1,'#4b6a6f']]) +
    lg(u+'-sofat',[[0,'#86a6a9'],[1,'#5c7d82']]) +
    lg(u+'-curt',[[0,'#efe4cd'],[.5,'#d8c9a8'],[1,'#efe4cd']],0,0,1,0) +
    lg(u+'-beam',[[0,'#fff1c4',.55],[1,'#fff1c4',0]],0,0,.35,1) +
    lg(u+'-shelf',[[0,'#6a4228'],[1,'#4a2c18']],0,0,1,0) +
    lg(u+'-rug',[[0,'#b86a4c'],[1,'#a35a40']]) +
    lg(u+'-gl',[[0,'#fff',.4],[1,'#fff',0]],0,0,1,1) +
    rg(u+'-lamp','#ffe2a0','#ffe2a0',.5,.5,.5).replace('stop-color="#ffe2a0"/></radial','stop-color="#ffe2a0" stop-opacity="0"/></radial') +
    '<clipPath id="'+u+'-win"><rect x="152" y="60" width="94" height="88"/></clipPath>';

  var b = '';
  b += rect(0,0,480,174,'url(#'+u+'-wall)');
  b += rect(0,0,480,6,'#f2ebdb') ;
  // wainscot panel subtle
  b += rect(0,130,480,44,'#efe7d4',' opacity=".35"') + rect(0,130,480,1.2,'#bfae8c',' opacity=".6"');
  // floor
  b += rect(0,172,480,98,'url(#'+u+'-floor)');
  for (var i=-10;i<=18;i++) b += '<line x1="'+R(240+i*22)+'" y1="173" x2="'+R(240+i*64)+'" y2="270" stroke="#5a3a22" stroke-opacity=".2" stroke-width=".7"/>';
  b += rect(0,167,480,7,'#f6f1e4') + rect(0,173.4,480,1.6,'#3c2a1b',' opacity=".35"');

  // window outdoor
  b += '<g clip-path="url(#'+u+'-win)"><g filter="url(#'+u+'-bl)">' +
    rect(140,50,120,110,'url(#'+u+'-sky)') +
    ell(170,84,16,8,'#fff',' opacity=".8"') + ell(220,76,20,7,'#fff',' opacity=".7"') +
    rect(176,104,50,24,'#c98d6b') + '<path d="M170 106L201 88L232 106Z" fill="#8c4f3b"/>' +
    ell(160,118,22,30,'#4f8a45') + ell(238,114,24,34,'#5b9a4c') + ell(200,142,70,16,'#6aa955') + ell(186,124,14,18,'#3f7a3c') +
    '<circle cx="190" cy="136" r="3" fill="#f7d0e0"/><circle cx="216" cy="138" r="3" fill="#fff0a8"/><circle cx="204" cy="140" r="2.6" fill="#f7a6b8"/>' +
    '</g></g>';
  b += rect(152,60,94,88,'url(#'+u+'-gl)',' opacity=".5"');
  b += '<path d="M146 54H252V154H146ZM152 60V148H246V60Z" fill="#fbf7ee" fill-rule="evenodd"/>' +
    rect(197,60,3,88,'#fbf7ee') + rect(152,102,94,3,'#fbf7ee') +
    rect(140,150,118,5,'#fbf7ee') + rect(140,155,118,2,'#7a6a52',' opacity=".35"') + rect(146,54,106,1.2,'#bfae8c',' opacity=".6"');
  // curtains
  b += rect(128,44,144,3,'#6a4a2e') + ell(128,45.5,3,3,'#6a4a2e') + ell(272,45.5,3,3,'#6a4a2e');
  b += '<path d="M134 47Q146 90 140 168H166Q160 100 162 47Z" fill="url(#'+u+'-curt)"/>' +
    '<path d="M262 47Q250 90 256 168H232Q238 100 236 47Z" fill="url(#'+u+'-curt)"/>' +
    '<path d="M140 50Q150 100 146 166M150 50Q158 100 156 166M258 50Q248 100 252 166M248 50Q240 100 242 166" stroke="#a89674" stroke-width=".7" fill="none" opacity=".7"/>';
  // sunlight patch on floor and wall
  b += '<path d="M152 150L246 150L340 266L196 266Z" fill="url(#'+u+'-beam)" opacity=".5"/>';
  b += '<path d="M168 180L236 180L306 262L214 262Z" fill="#fff4cc" opacity=".16"/>';

  // bookshelf
  b += shadow(u,100,177,38,4,.4);
  b += rect(68,84,62,92,'#4a2c18') + rect(71,87,56,86,'#2f1b0f');
  var ys=[87,110,133,156];
  var cols=['#9c3f35','#3f6b88','#d6b24a','#4f7a52','#e6dccb','#7d4a8a','#c86f3a','#2f4a68','#b5a58a','#a84a5a'];
  for (var s=0;s<4;s++){
    var y0=ys[s], x=73, k=s*3;
    while (x<122){
      var w=2.6+((k*7)%4)*.9, h=15+((k*5)%4)*2.2;
      if (s==1 && x>96 && x<112){ x+=4; k++; continue; }
      if (s==2 && k%7==3){ b += '<path d="M'+x+' '+(y0+22)+'l'+(h*.5)+' -'+(h)+'" stroke="'+cols[k%10]+'" stroke-width="'+w+'"/>'; x+=h*.5+1; k++; continue; }
      b += rect(R(x),R(y0+22.3-h),R(w),R(h),cols[k%10]) + rect(R(x),R(y0+22.3-h),.7,R(h),'#fff',' opacity=".18"');
      x+=w+.4; k++;
    }
    b += rect(70,y0+22,58,2.2,'#6b4228');
  }
  // decor on shelf 2: small vase + frame
  b += '<path d="M103 132q-3-6 0-10h6q3 4 0 10z" fill="#c9d9d6"/><path d="M106 122q-5-8 0-12M106 122q6-6 4-12" stroke="#4d7a3d" stroke-width="1" fill="none"/><rect x="114" y="116" width="9" height="12" fill="#e9d8a8" stroke="#5a3a22" stroke-width="1"/>';
  b += rect(68,82,62,3,'#6b4228');

  // paintings
  b += '<rect x="291" y="62" width="56" height="36" fill="#000" opacity=".18" filter="url(#'+u+'-bl)" transform="translate(2 3)"/>';
  b += rect(290,60,56,36,'#5a3a22') + rect(293,63,50,30,'#f2ead6') +
    rect(296,66,44,24,'#9cc3dc') + '<path d="M296 82L310 72L322 80L331 74L340 82V90H296Z" fill="#6f8f67"/><path d="M296 84Q318 80 340 85V90H296Z" fill="#4f7a52"/><circle cx="329" cy="71" r="3.4" fill="#f3d06a"/>';
  b += '<rect x="357" y="64" width="26" height="32" fill="#000" opacity=".18" filter="url(#'+u+'-bl)" transform="translate(2 3)"/>';
  b += rect(356,62,26,32,'#e9dfc6') + rect(358,64,22,28,'#f6f0e2') + ell(369,80,7,9,'#d98e4a') + '<path d="M363 92Q369 76 375 92Z" fill="#4f7a8a"/><rect x="356" y="62" width="26" height="32" fill="none" stroke="#2c211a" stroke-width="1.6"/>';

  // sofa
  b += shadow(u,320,177,76,5,.5);
  b += rect(254,174,8,4,'#2c1d12') + rect(378,174,8,4,'#2c1d12');
  b += '<rect x="256" y="120" width="132" height="40" rx="9" fill="url(#'+u+'-sofa)"/>';          // back
  b += '<rect x="250" y="138" width="16" height="36" rx="7" fill="#527479"/><rect x="378" y="138" width="16" height="36" rx="7" fill="#527479"/>'; // arms
  b += '<rect x="266" y="150" width="112" height="22" rx="4" fill="#4b6c71"/>';                   // base
  b += '<rect x="267" y="136" width="55" height="20" rx="6" fill="url(#'+u+'-sofat)"/><rect x="322" y="136" width="55" height="20" rx="6" fill="url(#'+u+'-sofat)"/>';
  b += '<rect x="267" y="150" width="55" height="14" rx="4" fill="#6d8f93"/><rect x="322" y="150" width="55" height="14" rx="4" fill="#6a8b8f"/>';
  b += '<path d="M322 150V164" stroke="#3e5c60" stroke-width="1"/>';
  b += '<rect x="250" y="138" width="16" height="3" rx="1.5" fill="#fff" opacity=".18"/><rect x="378" y="138" width="16" height="3" rx="1.5" fill="#fff" opacity=".18"/>';
  // cushions
  b += '<path d="M272 134L292 132L296 152L275 154Z" fill="#d9a43f"/><path d="M272 134L292 132L293 137L273 139Z" fill="#fff" opacity=".2"/>' +
    '<path d="M360 136L378 138L376 156L358 154Z" fill="#c4694a"/><path d="M360 136L378 138L377 142L359 140Z" fill="#fff" opacity=".18"/>' +
    '<path d="M330 140L350 140L350 156L330 156Z" fill="#e9dcc2" transform="rotate(-6 340 148)"/>';
  b += '<path d="M296 148Q312 140 330 150L326 170 296 168Z" fill="#b8a07a" opacity=".0"/>';

  // floor lamp
  b += shadow(u,404,178,12,2.6,.45);
  b += '<circle cx="404" cy="96" r="34" fill="url(#'+u+'-lamp)" opacity=".8"/>';
  b += ell(404,177,8,2,'#2c241d') + rect(403,102,2,75,'#3a2f27');
  b += '<path d="M392 108L396 88H412L416 108Z" fill="#f7e8bf"/><path d="M392 108L396 88H400L398 108Z" fill="#fff" opacity=".4"/><ellipse cx="404" cy="108" rx="12" ry="2" fill="#ffd57a"/>';

  // rug
  b += '<path d="M126 190L392 190L424 252L96 252Z" fill="#000" opacity=".16" filter="url(#'+u+'-bl)" transform="translate(0 3)"/>';
  b += '<path d="M130 188L388 188L420 250L100 250Z" fill="url(#'+u+'-rug)"/>';
  b += '<path d="M138 194L380 194L408 244L112 244Z" fill="none" stroke="#efe0c0" stroke-width="2.2" opacity=".85"/>';
  b += '<path d="M150 200L368 200L392 238L126 238Z" fill="none" stroke="#7e3c29" stroke-width="1" opacity=".6"/>';

  // coffee table
  b += shadow(u,177,201,38,4,.5);
  b += '<path d="M146 182v16M208 182v16M154 186v14M200 186v14" stroke="#4b2f1a" stroke-width="2.6" stroke-linecap="round"/>';
  b += '<ellipse cx="177" cy="183" rx="37" ry="8" fill="#3d2515"/><ellipse cx="177" cy="180.6" rx="37" ry="8" fill="#b98456"/><ellipse cx="174" cy="179.6" rx="28" ry="5.4" fill="#d6a574" opacity=".55"/>' +
    '<ellipse cx="177" cy="180.6" rx="37" ry="8" fill="none" stroke="#6f4627" stroke-width=".8"/>';
  b += rect(150,174,17,3.4,'#3f6b88') + rect(151,171,15,3.2,'#d6b24a') + rect(152,168.2,13,3,'#9c3f35');
  b += '<path d="M185 178l1.2-7h7l1.2 7z" fill="#f4efe6"/><ellipse cx="189.5" cy="171" rx="3.5" ry="1" fill="#5a3320"/><path d="M194 173q3.4 0 0 3" stroke="#f4efe6" stroke-width="1" fill="none"/>';
  b += '<path d="M203 179q-3-5 0-9h5q3 4 0 9z" fill="#d9e6e2"/><path d="M205.5 170q-6-8 0-13M205.5 170q7-5 5-12" stroke="#4d7a3d" stroke-width="1" fill="none"/><circle cx="199.8" cy="159" r="2.6" fill="#f3b4c4"/><circle cx="211" cy="158" r="2.6" fill="#f6d36a"/><circle cx="205" cy="156" r="2.6" fill="#fff"/>';
  return wrap(u, d, b);
};

/* ================= MARKET ================= */
RS.market = function(u){
  var d =
    lg(u+'-sky',[[0,'#8fc0e6'],[.65,'#d6e8f0'],[1,'#f6ecd2']]) +
    lg(u+'-gnd',[[0,'#a9a291'],[.3,'#c8c0ae'],[1,'#d6cfbd']]) +
    lg(u+'-cloth',[[0,'#2a2018',.45],[1,'#2a2018',0]]) +
    lg(u+'-tbl',[[0,'#c9965c'],[1,'#8a5a30']]) +
    lg(u+'-awn',[[0,'#000',0],[1,'#000',.28]]) +
    lg(u+'-sun',[[0,'#fff3c4',.5],[1,'#fff3c4',0]],0,0,.5,1) +
    rg(u+'-ap','#f0594a','#a31f1f') + rg(u+'-ag','#bfe05a','#5f9a28') + rg(u+'-tm','#ff6a4a','#b82812') +
    rg(u+'-or','#ffb347','#d6700f') + rg(u+'-lm','#fff07a','#e0b800') + rg(u+'-gr','#7cc063','#2f7a2e') +
    '<clipPath id="'+u+'-sk"><rect x="0" y="0" width="480" height="150"/></clipPath>';

  var b = '';
  b += rect(0,0,480,160,'url(#'+u+'-sky)');
  // blurred skyline
  b += '<g filter="url(#'+u+'-bl)" clip-path="url(#'+u+'-sk)">' +
    ell(100,34,40,9,'#fff',' opacity=".75"') + ell(330,26,50,8,'#fff',' opacity=".65"') +
    rect(-10,60,60,100,'#b98a74') + rect(50,40,50,120,'#c9b79a') + rect(100,70,56,90,'#9fa7b0') + rect(156,50,44,110,'#c98f6c') +
    rect(200,76,60,84,'#d9cdb2') + rect(260,44,48,116,'#a88a78') + rect(308,66,56,94,'#b3bcc4') + rect(364,36,52,124,'#c4a07e') + rect(416,60,80,100,'#a7978a') +
    '<g fill="#e7f1f7" opacity=".8">' + rect(58,52,6,8,'#e7f1f7') + rect(72,52,6,8,'#e7f1f7') + rect(58,70,6,8,'#e7f1f7') + rect(72,70,6,8,'#e7f1f7') + rect(166,62,6,8,'#e7f1f7') + rect(180,62,6,8,'#e7f1f7') + rect(272,56,6,8,'#e7f1f7') + rect(286,56,6,8,'#e7f1f7') + rect(376,50,6,8,'#e7f1f7') + rect(392,50,6,8,'#e7f1f7') + rect(272,76,6,8,'#e7f1f7') + rect(376,70,6,8,'#e7f1f7') + '</g>' +
    ell(130,98,26,24,'#6a9a55') + ell(248,100,22,22,'#6fa05a') + ell(344,104,24,24,'#5f904e') +
    rect(-10,126,500,30,'#b8b3a6') +
    '</g>';
  // ground
  b += rect(0,150,480,120,'url(#'+u+'-gnd)');
  for (var i=-6;i<=14;i++) b += '<line x1="'+R(240+i*26)+'" y1="152" x2="'+R(240+i*78)+'" y2="270" stroke="#8a8372" stroke-opacity=".18" stroke-width=".8"/>';
  b += rect(0,154,480,1.2,'#8d8676',' opacity=".35"') + rect(0,163,480,.8,'#8d8676',' opacity=".25"') + rect(0,178,480,.8,'#8d8676',' opacity=".2"');

  b += '<g transform="translate(16.8 12.3) scale(.93)">';
  // ===== stall A (apples) x 64..190
  b += rect(66,82,122,62,'#6d5a46') + rect(66,82,122,62,'url(#'+u+'-cloth)');
  b += rect(68,84,3,92,'#5b4129') + rect(183,84,3,92,'#5b4129');
  b += awning(60,194,58,84,'#c8352f','#f3ead6',8) + rect(60,56,134,28,'url(#'+u+'-awn)',' opacity=".55"');
  b += rect(70,52,114,5,'#8a2b24') ;
  // sign
  b += '<line x1="94" y1="86" x2="94" y2="92" stroke="#3a2a1a" stroke-width=".8"/><line x1="146" y1="86" x2="146" y2="92" stroke="#3a2a1a" stroke-width=".8"/>';
  b += rect(86,91,68,17,'#2a3a30') + rect(84,89,72,2.4,'#6a4a2c') +
    '<text x="120" y="98.5" text-anchor="middle" font-family="Georgia,serif" font-size="6.4" fill="#f6f0dc" font-weight="bold">Apples</text><text x="120" y="105.5" text-anchor="middle" font-family="Georgia,serif" font-size="6.4" fill="#ffd96a">$2/lb</text>';
  // table & crates
  b += shadow(u,128,178,70,3,.35);
  b += rect(66,140,120,5,'url(#'+u+'-tbl)') + rect(66,140,120,1.2,'#ecc790');
  b += crate(70,148,52,28,'#a9743f','#7b4d27') + crate(126,148,56,28,'#a9743f','#7b4d27');
  b += '<path d="M70 146H122M126 146H182" stroke="#6a4326" stroke-width="1.4"/>';
  b += heap(96,144,48,4,[u+'-ap',u+'-ap',u+'-ag'],5.2) + heap(154,144,52,4,[u+'-ag',u+'-ap',u+'-ap'],5.2);
  b += shadow(u,128,146,56,2,.22);
  // scale on table (stall A)
  b += '<rect x="109" y="132" width="18" height="8" rx="1.5" fill="#2e3336"/><circle cx="118" cy="127" r="7" fill="#f4f1e8" stroke="#2e3336" stroke-width="1.6"/><path d="M118 127l3-3.5" stroke="#b22" stroke-width=".9"/><rect x="113" y="140" width="10" height="1.4" fill="#aeb4b8"/>';

  // ===== stall B (tomatoes / greens) x 198..324
  b += rect(200,82,122,62,'#5e6f56') + rect(200,82,122,62,'url(#'+u+'-cloth)');
  b += rect(202,84,3,92,'#5b4129') + rect(317,84,3,92,'#5b4129');
  b += awning(194,328,56,84,'#2f7a47','#f3ead6',8) + rect(194,54,134,30,'url(#'+u+'-awn)',' opacity=".55"');
  b += rect(204,50,114,5,'#215a34');
  b += '<line x1="226" y1="86" x2="226" y2="92" stroke="#3a2a1a" stroke-width=".8"/><line x1="296" y1="86" x2="296" y2="92" stroke="#3a2a1a" stroke-width=".8"/>';
  b += rect(214,91,92,17,'#f1e3b8') + rect(212,89,96,2.4,'#6a4a2c') +
    '<text x="260" y="98.8" text-anchor="middle" font-family="Georgia,serif" font-size="6.4" fill="#3a2418" font-weight="bold">Tomatoes $3/lb</text><text x="260" y="105.6" text-anchor="middle" font-family="Georgia,serif" font-size="5.6" fill="#2f7a47">Fresh Greens $2</text>';
  b += shadow(u,262,178,70,3,.35);
  b += rect(200,140,120,5,'url(#'+u+'-tbl)') + rect(200,140,120,1.2,'#ecc790');
  b += crate(204,148,54,28,'#a9743f','#7b4d27') + crate(262,148,54,28,'#a9743f','#7b4d27');
  b += heap(231,144,48,4,[u+'-tm'],5.2);
  // leafy greens in second crate
  var g='';
  for (i=0;i<9;i++){
    var gx=270+i*5.6, gy=143-((i*5)%3)*2.2;
    g += '<path d="M'+R(gx)+' '+R(gy+3)+'q-6 -6 -3 -13q4 3 4 6q3 -5 6 -4q1 7 -2 11z" fill="'+(i%2?'#4f9a3a':'#6fb04a')+'"/>';
  }
  b += g + '<path d="M268 146H314" stroke="#3f7a2c" stroke-width="2.2"/>';
  // carrots
  b += '<g transform="translate(300 129)"><path d="M0 12L3 -3L6 12Z" fill="#e8772a"/><path d="M5 12L8 -2L11 12Z" fill="#f08a36"/><path d="M-4 12L-1 -2L2 12Z" fill="#d96a20"/><path d="M0 -3l-2-6M3 -3l1-7M8 -2l3-6M6 -3l-1-6" stroke="#4f9a3a" stroke-width="1.6"/></g>';
  // hanging scale at stall B
  b += '<line x1="236" y1="86" x2="236" y2="108" stroke="#2e3336" stroke-width=".8" opacity="0"/>';

  // ===== stall C (citrus) x 332..432
  b += rect(334,82,96,62,'#7a6a46') + rect(334,82,96,62,'url(#'+u+'-cloth)');
  b += rect(336,84,3,92,'#5b4129') + rect(425,84,3,92,'#5b4129');
  b += awning(328,436,58,84,'#e0a92b','#f3ead6',6) + rect(328,56,108,28,'url(#'+u+'-awn)',ric());
  b += rect(338,52,90,5,'#a8791c');
  b += rect(350,91,64,17,'#2a3a30') + rect(348,89,68,2.4,'#6a4a2c') +
    '<text x="382" y="98.6" text-anchor="middle" font-family="Georgia,serif" font-size="6.2" fill="#ffd96a" font-weight="bold">Lemons</text><text x="382" y="105.6" text-anchor="middle" font-family="Georgia,serif" font-size="6" fill="#f6f0dc">3 for $1</text>';
  b += shadow(u,384,178,56,3,.35);
  b += rect(334,140,96,5,'url(#'+u+'-tbl)') + rect(334,140,96,1.2,'#ecc790');
  b += crate(338,148,44,28,'#a9743f','#7b4d27') + crate(386,148,40,28,'#a9743f','#7b4d27');
  b += heap(360,144,38,4,[u+'-lm'],5) + heap(406,144,34,4,[u+'-or'],5);
  // wicker basket with bread? keep produce only: basket of pears near front-left of stall C
  b += '<path d="M310 176l3-12h18l3 12z" fill="#b98a4e"/><path d="M311 170h22M312 165h20" stroke="#8a5f2c" stroke-width=".8"/>' +
    '<circle cx="317" cy="162" r="4.4" fill="url(#'+u+'-ag)"/><circle cx="325" cy="162" r="4.4" fill="url(#'+u+'-ap)"/><circle cx="321" cy="157.6" r="4.4" fill="url(#'+u+'-ag)"/>';
  b += '</g>';
  // sun haze
  return wrap(u, d, b);
  function ric(){ return ' opacity=".55"'; }
};
})();
