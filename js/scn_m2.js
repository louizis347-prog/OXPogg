/* scn_m2.js - cenários pintados (mesma identidade do "Welcome to New York"): nyc, flags, cafe2, airport2, lobby1, lobby2 */
(function(){
window.RS=window.RS||{};
function rng(s){return function(){s=(s*16807)%2147483647;return (s-1)/2147483646;};}
function f(n){return Math.round(n*10)/10;}
var HEAD='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 270" width="100%" height="100%" style="width:100%;height:100%;display:block" preserveAspectRatio="xMidYMid slice" role="img" aria-hidden="true">';
function fin(u,b){return b.replace(/@/g,u+'-');}
var COM='<linearGradient id="@sk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5c7db0"/><stop offset=".3" stop-color="#a9a6c6"/><stop offset=".62" stop-color="#f0b58b"/><stop offset="1" stop-color="#fcd8a0"/></linearGradient>'
+'<radialGradient id="@sn"><stop offset="0" stop-color="#fffbe2"/><stop offset=".2" stop-color="#ffe6a0" stop-opacity=".85"/><stop offset=".55" stop-color="#ffbf80" stop-opacity=".3"/><stop offset="1" stop-color="#ffbf80" stop-opacity="0"/></radialGradient>'
+'<radialGradient id="@lg"><stop offset="0" stop-color="#fff3c4" stop-opacity=".95"/><stop offset=".4" stop-color="#ffd37a" stop-opacity=".45"/><stop offset="1" stop-color="#ffb347" stop-opacity="0"/></radialGradient>'
+'<linearGradient id="@cl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff2dc"/><stop offset="1" stop-color="#e79a8a"/></linearGradient>'
+'<radialGradient id="@vg" cx=".5" cy=".55" r=".8"><stop offset=".6" stop-color="#0c1220" stop-opacity="0"/><stop offset="1" stop-color="#0c1220" stop-opacity=".42"/></radialGradient>'
+'<filter id="@b" x="-20%" y="-40%" width="140%" height="180%"><feGaussianBlur stdDeviation="1.5"/></filter>'
+'<filter id="@b2" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="3.2"/></filter>'
+'<filter id="@n" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".03 .8" numOctaves="2" seed="6"/><feColorMatrix values="0 0 0 0 .12 0 0 0 0 .07 0 0 0 0 .03 1.5 0 0 0 -.55"/></filter>';
var CLOUDS='<g filter="url(#@b)"><ellipse cx="300" cy="40" rx="110" ry="6" fill="#8d8fb8" opacity=".5"/><ellipse cx="80" cy="30" rx="80" ry="5" fill="#8d8fb8" opacity=".45"/><ellipse cx="320" cy="76" rx="90" ry="9" fill="url(#@cl)"/><ellipse cx="370" cy="68" rx="50" ry="7" fill="url(#@cl)"/><ellipse cx="140" cy="86" rx="100" ry="8" fill="url(#@cl)"/><ellipse cx="60" cy="68" rx="60" ry="6" fill="url(#@cl)"/><ellipse cx="220" cy="106" rx="120" ry="6" fill="#f4a876" opacity=".8"/><ellipse cx="400" cy="108" rx="80" ry="5" fill="#f5b184" opacity=".8"/></g>';
var FIN='<rect width="480" height="270" fill="url(#@vg)"/><rect width="480" height="270" filter="url(#@n)" opacity=".06"/>';
function bokeh(r,n,y0,y1,cols){var s='<g filter="url(#@b)">';for(var i=0;i<n;i++){s+='<circle cx="'+f(r()*480)+'" cy="'+f(y0+r()*(y1-y0))+'" r="'+f(2+r()*3.5)+'" fill="'+cols[i%cols.length]+'" opacity="'+f(.35+r()*.4)+'"/>';}return s+'</g>';}
function lamp(x,y,s){return '<circle cx="'+x+'" cy="'+y+'" r="'+f(26*s)+'" fill="url(#@lg)"/><circle cx="'+x+'" cy="'+y+'" r="'+f(3.2*s)+'" fill="#fffbe6"/>';}
function person(x,y,s,c,h){return '<g filter="url(#@b)" opacity=".9"><ellipse cx="'+x+'" cy="'+f(y-34*s)+'" rx="'+f(5*s)+'" ry="'+f(5.5*s)+'" fill="'+h+'"/><path d="M'+f(x-9*s)+' '+y+'Q'+x+' '+f(y-44*s)+' '+f(x+9*s)+' '+y+'Z" fill="'+c+'"/></g>';}

/* ============ NYC: Brooklyn ao entardecer, ponte, skyline, táxi ============ */
RS.nyc=function(u){
  var r=rng(5),sky='',win='',wat='',sun='';
  var bl=[[0,22,38],[22,18,52],[40,14,34],[54,20,60],[74,16,44],[90,22,70],[112,14,48],[126,18,86],[144,12,54],[156,20,40],[176,14,62],[190,20,48],[210,12,76],[222,16,58],[238,14,100],[252,16,66],[268,12,52],[280,18,80],[298,14,60],[312,18,44],[330,12,70],[342,20,56],[362,14,90],[376,18,48],[394,12,64],[406,20,50],[426,14,72],[440,22,44],[462,18,58]];
  var far='',near='';
  for(var i=0;i<bl.length;i++){var b=bl[i];far+='<rect x="'+b[0]+'" y="'+(148-b[2]*.85)+'" width="'+b[1]+'" height="'+(b[2]*.85+4)+'" fill="#a798b6"/>';
    if(i%2===0)near+='<rect x="'+(b[0]+3)+'" y="'+(148-b[2]*.62)+'" width="'+(b[1]-2)+'" height="'+(b[2]*.62+4)+'" fill="#6f6a92"/>';}
  for(var j=0;j<90;j++){win+='<rect x="'+f(r()*470)+'" y="'+f(104+r()*42)+'" width="1.6" height="2" fill="#ffe7a8" opacity="'+f(.4+r()*.5)+'"/>';}
  /* Empire State */
  var es='<g><path d="M290 148V92h18v56Z" fill="#7f7aa0"/><path d="M293 92V74h12v18Z" fill="#7f7aa0"/><path d="M296 74V60h6v14Z" fill="#7f7aa0"/><rect x="298" y="40" width="2" height="21" fill="#7f7aa0"/><rect x="297" y="60" width="4" height="3" fill="#ffe2a0"/></g>';
  var bridge='<g stroke="#4b4468" fill="none" stroke-width="1.1" opacity=".92"><path d="M40 168C90 150 130 150 160 150" /><path d="M0 172H300" stroke-width="2.4"/>'
   +'<path d="M-10 164C30 190 70 190 110 164" opacity="0"/>'
   +'</g>';
  var tw='<g fill="#5a5278"><rect x="108" y="108" width="9" height="66"/><rect x="214" y="108" width="9" height="66"/></g><g fill="#2c2742"><path d="M108 124q4.5-12 9 0v50h-9Z" opacity=".35"/><path d="M214 124q4.5-12 9 0v50h-9Z" opacity=".35"/></g>'
   +'<g stroke="#5a5278" fill="none" stroke-width=".9"><path d="M-10 160Q54 166 112 112"/><path d="M112 112Q164 168 218 112"/><path d="M218 112Q300 168 500 176"/>'
   +'<path d="M20 163L22 172M40 164L42 172M60 162L62 172M80 156L82 172M96 138L98 172M130 130L132 172M148 142L150 172M164 148L166 172M180 148L182 172M196 140L198 172M234 134L236 172M254 146L256 172M274 154L276 172M294 160L296 172M314 164L316 172"/></g>'
   +'<rect x="-10" y="170" width="500" height="4" fill="#4f4870"/><rect x="-10" y="170" width="500" height="1.2" fill="#ffd9a0" opacity=".6"/>';
  var statue='<g transform="translate(418 128)" filter="url(#@b)"><path d="M-3 20V6h6v14Z" fill="#7a9a8f"/><path d="M-2 6L-3 -6Q0 -10 3 -6L2 6Z" fill="#8bb0a2"/><rect x="2.5" y="-14" width="1.5" height="9" fill="#8bb0a2"/><circle cx="3.3" cy="-16" r="2" fill="#ffd36a"/><rect x="-7" y="20" width="14" height="6" fill="#a89a96"/></g>';
  for(var k=0;k<22;k++){var yy=152+k*2.6,w=10+k*1.8+r()*6;sun+='<path d="M'+f(330-w)+' '+f(yy)+'H'+f(330+w)+'" stroke-opacity="'+f(.7-k*.028)+'"/>';}
  for(var q=0;q<50;q++){var y2=152+Math.pow(r(),1.6)*46;wat+='<path d="M'+f(r()*480)+' '+f(y2)+'h'+f(4+r()*10)+'" stroke-width="'+f(.4+(y2-150)/120)+'"/>';}
  /* grade e calçada */
  var posts='';for(var p=0;p<9;p++){var px=20+p*58;posts+='<rect x="'+px+'" y="186" width="3.2" height="22" fill="#2b2430"/>';}
  var taxi='<g transform="translate(232 232)"><ellipse cx="0" cy="22" rx="62" ry="6" fill="#2a1a10" opacity=".32" filter="url(#@b)"/>'
   +'<path d="M-58 14V0Q-58 -6-50 -8L-30 -10L-20 -26Q-17 -30-10 -30H22Q30 -30 34 -24L44 -10L54 -7Q60 -5 60 2V14Q60 18 56 18H-54Q-58 18-58 14Z" fill="#ffc21a"/>'
   +'<path d="M-18 -9L-10 -24H22L32 -9Z" fill="#9fc2d8"/><path d="M-18 -9L-10 -24H0L-4 -9Z" fill="#fff" opacity=".35"/><rect x="-6" y="-35" width="22" height="6" rx="2" fill="#2b2430"/><text x="5" y="-30.4" font-size="5" font-family="Arial" font-weight="800" fill="#ffd34a" text-anchor="middle">TAXI</text>'
   +'<path d="M-58 4H60" stroke="#d99a00" stroke-width="1.6"/><rect x="-6" y="2" width="12" height="4" fill="#2b2430" opacity=".25"/>'
   +'<circle cx="-34" cy="18" r="9" fill="#1d1a24"/><circle cx="-34" cy="18" r="4" fill="#9d98a8"/><circle cx="34" cy="18" r="9" fill="#1d1a24"/><circle cx="34" cy="18" r="4" fill="#9d98a8"/>'
   +'<rect x="54" y="-1" width="6" height="5" rx="1.5" fill="#fff4b8"/><circle cx="62" cy="2" r="14" fill="url(#@lg)" opacity=".6"/></g>';
  var b=HEAD+'<defs>'+COM+'</defs>'
   +'<rect width="480" height="152" fill="url(#@sk)"/><circle cx="330" cy="148" r="118" fill="url(#@sn)"/><circle cx="330" cy="148" r="9" fill="#fffbe6"/>'+CLOUDS
   +'<g filter="url(#@b)">'+far+es+'</g><g filter="url(#@b)" opacity=".98">'+near+'</g><g>'+win+'</g>'+statue
   +'<rect y="148" width="480" height="60" fill="#8f94b0"/><rect y="148" width="480" height="60" fill="url(#@sk)" opacity=".0"/>'
   +'<linearGradient id="@wa" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f6cd9b"/><stop offset=".3" stop-color="#b8a0a6"/><stop offset="1" stop-color="#5b7192"/></linearGradient><rect y="148" width="480" height="62" fill="url(#@wa)"/>'
   +'<ellipse cx="330" cy="154" rx="110" ry="14" fill="#ffe3a8" opacity=".55" filter="url(#@b)"/><g stroke="#fff3c6" stroke-width="1" fill="none">'+sun+'</g><g stroke="#fff0d6" stroke-opacity=".38" fill="none">'+wat+'</g>'
   +bridge+tw
   +'<linearGradient id="@pv" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c9a98b"/><stop offset="1" stop-color="#7d6150"/></linearGradient><rect y="196" width="480" height="76" fill="url(#@pv)"/>'
   +'<rect y="196" width="480" height="3" fill="#ffe6bd" opacity=".55"/><g>'+posts+'</g><path d="M0 188H480M0 194H480" stroke="#2b2430" stroke-width="1.6" opacity=".85"/>'
   +'<linearGradient id="@rd" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5d5668"/><stop offset="1" stop-color="#3a3444"/></linearGradient><rect y="214" width="480" height="60" fill="url(#@rd)"/>'
   +'<path d="M0 213H480" stroke="#e8d7b8" stroke-width="2" opacity=".7"/><g stroke="#f4e3a6" stroke-width="2" stroke-dasharray="26 22" opacity=".6"><path d="M0 262H480"/></g>'
   +'<rect y="214" width="480" height="60" fill="#ffb86b" opacity=".12"/>'+lamp(70,176,1.2)+lamp(405,176,1.2)+'<rect x="68.8" y="176" width="2.4" height="34" fill="#2b2430"/><rect x="403.8" y="176" width="2.4" height="34" fill="#2b2430"/>'
   +taxi+bokeh(r,16,150,205,['#ffe0a0','#ffb86b','#fff'])+FIN+'</svg>';
  return fin(u,b);
};

/* ============ Dia Internacional: praça com bandeiras ============ */
RS.flags=function(u){
  var r=rng(9),cols=[['#d62828','#fff','#d62828'],['#1d3a8a','#fff','#c62828'],['#1f9d55','#ffd23f','#1d3a8a'],['#fff','#d62828','#fff'],['#74acdf','#fff','#74acdf'],['#c8102e','#fff','#002868'],['#009739','#fedd00','#009739'],['#ff9933','#fff','#138808'],['#ce1126','#fcd116','#006b3f'],['#000','#d00','#fc0']];
  var bunt='';
  function row(y0,sag,n,x0,x1){var s='<path d="M'+x0+' '+y0+'Q'+f((x0+x1)/2)+' '+(y0+sag)+' '+x1+' '+y0+'" stroke="#3a3040" stroke-width="1" fill="none"/>';
    for(var i=0;i<n;i++){var t=(i+.5)/n,x=x0+(x1-x0)*t,y=y0+2*sag*t*(1-t)*1,c=cols[(i*3+Math.floor(r()*4))%cols.length],w=11,hgt=14;
      s+='<g transform="translate('+f(x)+' '+f(y)+') rotate('+f((t-.5)*34)+')"><path d="M-'+(w/2)+' 0H'+(w/2)+'L0 '+hgt+'Z" fill="'+c[0]+'"/><path d="M-'+(w/2-2)+' 2H'+(w/2-2)+'L0 '+(hgt-3)+'Z" fill="'+c[1]+'"/><circle cx="0" cy="5" r="1.6" fill="'+c[2]+'"/></g>';}
    return s;}
  bunt=row(24,22,15,-10,490)+row(46,28,16,-10,490);
  var lights='';for(var i=0;i<26;i++){var t=i/25,x=-5+t*490,y=70+2*30*t*(1-t);lights+='<circle cx="'+f(x)+'" cy="'+f(y)+'" r="2" fill="#fff3c4"/><circle cx="'+f(x)+'" cy="'+f(y)+'" r="8" fill="url(#@lg)" opacity=".7"/>';}
  var bl='';[[0,40,92],[44,34,70],[380,40,84],[426,60,100]].forEach(function(b,i){bl+='<rect x="'+b[0]+'" y="'+(150-b[2])+'" width="'+b[1]+'" height="'+b[2]+'" fill="'+(i%2?'#8d86a8':'#9b8fae')+'"/>';for(var k=0;k<14;k++)bl+='<rect x="'+f(b[0]+4+r()*(b[1]-9))+'" y="'+f(150-b[2]+8+r()*(b[2]-20))+'" width="3" height="4" fill="#ffe3a0" opacity="'+f(.4+r()*.5)+'"/>';});
  var tr='';[[70,148,30],[420,148,34],[110,150,22]].forEach(function(t,i){tr+='<rect x="'+(t[0]-2)+'" y="'+(t[1]-14)+'" width="4" height="16" fill="#4a3a2e"/><circle cx="'+t[0]+'" cy="'+(t[1]-26)+'" r="'+t[2]*.7+'" fill="#5f8b57"/><circle cx="'+(t[0]-6)+'" cy="'+(t[1]-30)+'" r="'+t[2]*.45+'" fill="#7aa86a" opacity=".8"/>';});
  var stage='<g><rect x="150" y="142" width="180" height="26" fill="#7a5638"/><rect x="150" y="142" width="180" height="4" fill="#c79a66"/><rect x="150" y="146" width="180" height="22" fill="url(#@st)"/><path d="M150 168H330" stroke="#2a1a10" stroke-width="1.5" opacity=".5"/>'
   +'<rect x="168" y="96" width="144" height="34" rx="4" fill="#fffaf0"/><rect x="168" y="96" width="144" height="34" rx="4" fill="none" stroke="#c9553d" stroke-width="2.4"/>'
   +'<text x="240" y="111" font-size="10.5" font-family="Arial,sans-serif" font-weight="800" fill="#c9553d" text-anchor="middle">INTERNATIONAL</text><text x="240" y="124" font-size="10.5" font-family="Arial,sans-serif" font-weight="800" fill="#1d3a8a" text-anchor="middle">DAY</text>'
   +'<rect x="170" y="130" width="3" height="14" fill="#3a2a1e"/><rect x="307" y="130" width="3" height="14" fill="#3a2a1e"/></g>';
  var stalls='';[[8,'#d62828'],[388,'#1f9d55']].forEach(function(s){stalls+='<g><rect x="'+s[0]+'" y="140" width="84" height="30" fill="#6b4a32"/><path d="M'+(s[0]-4)+' 134H'+(s[0]+88)+'L'+(s[0]+82)+' 150H'+(s[0]+2)+'Z" fill="'+s[1]+'"/>';for(var k=0;k<6;k++)stalls+='<path d="M'+(s[0]-4+k*15.3)+' 134h7.6l-.8 16h-6z" fill="#fff" opacity=".85"/>';stalls+='</g>';});
  var crowd='';var cc=['#4a3d6b','#c2571f','#2f6f73','#8a3b5c','#355c8a','#a2791f'];for(var i=0;i<16;i++){crowd+=person(110+i*17+r()*8,176+r()*10,.95+r()*.3,cc[i%cc.length],'#3a2a1e');}
  var b=HEAD+'<defs>'+COM+'<linearGradient id="@st" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#b78556"/><stop offset="1" stop-color="#6a4a30"/></linearGradient><linearGradient id="@gr" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d3b58c"/><stop offset="1" stop-color="#7a6350"/></linearGradient></defs>'
   +'<rect width="480" height="152" fill="url(#@sk)"/><circle cx="250" cy="140" r="130" fill="url(#@sn)"/>'+CLOUDS
   +'<g filter="url(#@b)">'+bl+tr+'</g>'+stalls+stage
   +'<rect y="166" width="480" height="108" fill="url(#@gr)"/><rect y="166" width="480" height="3" fill="#ffe6bd" opacity=".6"/>'
   +'<g stroke="#5a4636" stroke-opacity=".25" fill="none">'+(function(){var s='';for(var i=0;i<9;i++){s+='<path d="M0 '+(172+i*12)+'H480"/>';}for(var j=0;j<16;j++){s+='<path d="M'+(j*34)+' 170L'+(240+(j*34-240)*1.7)+' 274"/>';}return s;})()+'</g>'
   +'<rect y="166" width="480" height="108" fill="#ffb86b" opacity=".12"/>'
   +crowd+'<g>'+bunt+'</g>'+lights+bokeh(r,14,60,170,['#ffe0a0','#ff9aa2','#a0d8ff'])+FIN+'</svg>';
  return fin(u,b);
};

/* ============ Café aconchegante (hora dourada) ============ */
RS.cafe2=function(u){
  var r=rng(14),pend='';[[96,48],[240,40],[384,48]].forEach(function(p){pend+='<path d="M'+p[0]+' 0V'+p[1]+'" stroke="#2a1a10" stroke-width="1.4"/><path d="M'+(p[0]-12)+' '+(p[1]+11)+'Q'+p[0]+' '+(p[1]-6)+' '+(p[0]+12)+' '+(p[1]+11)+'Z" fill="#d9a441"/>'+lamp(p[0],p[1]+10,1.5);});
  var cb='';for(var i=0;i<14;i++){cb+='<rect x="'+(40+i*26)+'" y="'+(82+(i%3)*0)+'" width="1.4" height="44" fill="#fff" opacity=".0"/>';}
  var sk='';
  var win='<g><rect x="132" y="36" width="216" height="104" fill="url(#@sk)"/><circle cx="260" cy="120" r="70" fill="url(#@sn)"/><g filter="url(#@b)"><ellipse cx="190" cy="66" rx="40" ry="5" fill="url(#@cl)"/><ellipse cx="300" cy="84" rx="44" ry="5" fill="url(#@cl)"/></g>'
   +'<g filter="url(#@b)" fill="#8d82a8"><rect x="134" y="104" width="20" height="40"/><rect x="156" y="92" width="16" height="52"/><rect x="176" y="108" width="24" height="36"/><rect x="204" y="86" width="14" height="58"/><rect x="224" y="100" width="26" height="44"/><rect x="254" y="94" width="18" height="50"/><rect x="278" y="106" width="22" height="38"/><rect x="304" y="90" width="16" height="54"/><rect x="324" y="102" width="22" height="42"/></g>'
   +'<g stroke="#3a2418" stroke-width="5"><path d="M132 36H348M132 140H348M132 36V140M348 36V140"/></g><g stroke="#3a2418" stroke-width="2.5"><path d="M204 36V140M276 36V140M132 88H348"/></g>'
   +'<path d="M136 38L190 138" stroke="#fff" stroke-opacity=".12" stroke-width="22"/></g>';
  var shelf='<g><rect x="20" y="62" width="92" height="4" fill="#3a2418"/><rect x="20" y="92" width="92" height="4" fill="#3a2418"/>';
  for(var k=0;k<7;k++){shelf+='<rect x="'+(26+k*12)+'" y="'+(50+(k%2)*2)+'" width="8" height="12" rx="1.5" fill="'+['#f4e3c8','#c9553d','#e8b04a','#8fb3a6'][k%4]+'"/><rect x="'+(26+k*12)+'" y="'+(80+(k%3))+'" width="8" height="12" rx="1.5" fill="'+['#fff','#d9a441','#c9553d'][k%3]+'"/>';}
  shelf+='</g>';
  var plant='<g transform="translate(446 150)"><path d="M-12 0H12L9 -24H-9Z" fill="#9c5a3c"/><g fill="#4f8a55"><ellipse cx="-8" cy="-38" rx="6" ry="16" transform="rotate(-24 -8 -38)"/><ellipse cx="8" cy="-40" rx="6" ry="17" transform="rotate(22 8 -40)"/><ellipse cx="0" cy="-46" rx="6" ry="19"/></g></g>';
  function table(x,y,s){return '<g transform="translate('+x+' '+y+') scale('+s+')"><ellipse cx="0" cy="40" rx="42" ry="7" fill="#1a0f08" opacity=".35" filter="url(#@b)"/><rect x="-3" y="4" width="6" height="36" fill="#2a1a10"/><ellipse cx="0" cy="2" rx="40" ry="10" fill="#d1a672"/><ellipse cx="0" cy="0" rx="40" ry="9.5" fill="#e6c08a"/>'
   +'<g transform="translate(-14 -6)"><path d="M-7 0H7L5 10H-5Z" fill="#fff"/><ellipse cx="0" cy="0" rx="7" ry="2" fill="#6b3a1e"/><path d="M5 2q5 0 4 4" stroke="#fff" fill="none" stroke-width="1.5"/></g>'
   +'<g transform="translate(14 -4)"><path d="M-7 0H7L5 10H-5Z" fill="#f4d9b0"/><ellipse cx="0" cy="0" rx="7" ry="2" fill="#6b3a1e"/></g><g opacity=".5" stroke="#fff" fill="none" stroke-width="1.2"><path d="M-14 -12q-3-6 0-10M14 -10q-3-6 0-10"/></g>'
   +'<g fill="#7a4a2c"><rect x="-58" y="14" width="16" height="3" rx="1"/><rect x="-56" y="17" width="2.4" height="26"/><rect x="-46" y="17" width="2.4" height="26"/></g></g>';}
  var b=HEAD+'<defs>'+COM+'<linearGradient id="@wl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6b3f27"/><stop offset="1" stop-color="#b87a4c"/></linearGradient><linearGradient id="@fl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9a6238"/><stop offset="1" stop-color="#4b2a17"/></linearGradient></defs>'
   +'<rect width="480" height="160" fill="url(#@wl)"/><g stroke="#3a2418" stroke-opacity=".25">'+(function(){var s='';for(var i=0;i<16;i++)s+='<path d="M'+(i*30)+' 0V160"/>';return s})()+'</g>'
   +win+shelf
   +'<rect x="0" y="136" width="480" height="134" fill="url(#@fl)"/><g stroke="#2a150a" stroke-opacity=".38" fill="none">'+(function(){var s='';for(var i=0;i<8;i++){s+='<path d="M0 '+(146+i*16)+'H480"/>';}for(var j=0;j<18;j++){s+='<path d="M'+(j*30-10)+' 136L'+(240+(j*30-250)*2.2)+' 274"/>';}return s})()+'</g>'
   +'<ellipse cx="260" cy="160" rx="150" ry="20" fill="#ffd49a" opacity=".28" filter="url(#@b2)"/>'
   +'<g filter="url(#@b)"><rect x="0" y="130" width="110" height="26" fill="#4a2a18"/><rect x="0" y="126" width="110" height="5" fill="#d1a672"/><rect x="14" y="112" width="26" height="16" fill="#9fa3a8"/><rect x="48" y="116" width="14" height="12" fill="#c9553d"/></g>'
   +plant+table(250,196,1)+table(380,226,.92)+pend+bokeh(r,12,60,180,['#ffe0a0','#ffb86b'])+FIN+'</svg>';
  return fin(u,b);
};

/* ============ Aeroporto: chegadas ao pôr do sol ============ */
RS.airport2=function(u){
  var r=rng(21),panels='';for(var i=0;i<7;i++){panels+='<rect x="'+(20+i*66)+'" y="6" width="44" height="7" rx="2" fill="#fff6dc"/><ellipse cx="'+(42+i*66)+'" cy="14" rx="30" ry="6" fill="url(#@lg)" opacity=".5"/>';}
  var plane='<g transform="translate(332 126)" filter="url(#@b)"><path d="M-70 0Q-70 -9-56 -10H48Q64 -10 70 -2L74 4Q60 8 46 8H-60Q-70 8-70 0Z" fill="#f5f2ee"/><path d="M-56 -8L-76 -34 -62 -34 -34 -9Z" fill="#e8e3df"/><path d="M-70 -2H70" stroke="#2f6fb5" stroke-width="2.4"/><path d="M-20 4L-44 24 -28 24 0 6Z" fill="#dcd6d2"/><g fill="#6a89a8">'+(function(){var s='';for(var k=0;k<14;k++)s+='<circle cx="'+(-40+k*7.5)+'" cy="-4" r="1.3"/>';return s})()+'</g></g>';
  var bags='';[[104,'#c9553d'],[132,'#2f6fb5'],[408,'#3a8a6a'],[434,'#d9a441']].forEach(function(b,i){var y=i<2?214:224;bags+='<g transform="translate('+b[0]+' '+y+')"><rect x="-12" y="-28" width="24" height="28" rx="4" fill="'+b[1]+'"/><rect x="-6" y="-34" width="12" height="7" rx="2" fill="none" stroke="#2a2430" stroke-width="2"/><rect x="-12" y="-16" width="24" height="2" fill="#fff" opacity=".35"/><circle cx="-7" cy="2" r="2" fill="#1d1a24"/><circle cx="7" cy="2" r="2" fill="#1d1a24"/></g>';});
  var cart='<g transform="translate(262 232)"><path d="M-26 -24H22L18 -2H-22Z" fill="none" stroke="#9fa7b0" stroke-width="2"/><path d="M-22 -14H20M-24 -24L-30 -34H-36" stroke="#9fa7b0" stroke-width="2" fill="none"/><circle cx="-18" cy="2" r="3" fill="#2a2430"/><circle cx="16" cy="2" r="3" fill="#2a2430"/></g>';
  var b=HEAD+'<defs>'+COM+'<linearGradient id="@fl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#b9b7c4"/><stop offset=".4" stop-color="#8f8ea6"/><stop offset="1" stop-color="#55546e"/></linearGradient><linearGradient id="@cei" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3b3a55"/><stop offset="1" stop-color="#6e6a8c"/></linearGradient></defs>'
   +'<rect width="480" height="170" fill="url(#@cei)"/>'
   +'<g><rect x="30" y="26" width="420" height="112" fill="url(#@sk)"/><circle cx="130" cy="130" r="100" fill="url(#@sn)"/><g filter="url(#@b)"><ellipse cx="320" cy="60" rx="80" ry="5" fill="url(#@cl)"/><ellipse cx="160" cy="76" rx="70" ry="5" fill="url(#@cl)"/></g>'
   +'<rect x="30" y="124" width="420" height="14" fill="#6b6a86"/><g stroke="#f4e08a" stroke-width="1.4" stroke-dasharray="14 10"><path d="M30 131H450"/></g>'
   +'<g filter="url(#@b)" fill="#e9a064"><rect x="40" y="116" width="46" height="9"/><rect x="380" y="112" width="40" height="13"/></g>'+plane
   +'<g stroke="#2a2840" stroke-width="3"><path d="M30 26H450M30 138H450M30 26V138M450 26V138M170 26V138M310 26V138"/></g></g>'
   +'<g filter="url(#@b)" fill="#3e3c5c"><rect x="0" y="0" width="30" height="170"/><rect x="450" y="0" width="30" height="170"/></g>'+panels
   +'<g transform="translate(240 36)"><rect x="-58" y="0" width="116" height="26" rx="4" fill="#232a44"/><rect x="-58" y="0" width="116" height="26" rx="4" fill="none" stroke="#ffd34a" stroke-width="1.4"/><text x="-8" y="18" font-size="13" font-family="Arial,sans-serif" font-weight="800" fill="#ffd34a" text-anchor="middle">ARRIVALS</text><path d="M30 13H46M40 7L46 13L40 19" stroke="#ffd34a" stroke-width="2.4" fill="none"/><path d="M-30 -36V0M30 -36V0" stroke="#232a44" stroke-width="1.5"/></g>'
   +'<rect y="138" width="480" height="136" fill="url(#@fl)"/><g stroke="#fff" stroke-opacity=".12" fill="none">'+(function(){var s='';for(var i=0;i<7;i++){s+='<path d="M0 '+(148+i*18)+'H480"/>';}for(var j=0;j<14;j++){s+='<path d="M'+(j*40-20)+' 138L'+(240+(j*40-220)*2.4)+' 274"/>';}return s})()+'</g>'
   +'<g opacity=".38" filter="url(#@b)"><g transform="translate(0 290) scale(1 -1)"><rect x="30" y="26" width="420" height="112" fill="url(#@sk)"/></g></g><ellipse cx="150" cy="170" rx="130" ry="14" fill="#ffd9a0" opacity=".4" filter="url(#@b2)"/>'
   +bags+cart+bokeh(r,10,30,200,['#fff','#ffd9a0'])+FIN+'</svg>';
  return fin(u,b);
};

/* ============ Hotel: recepção (variante 1 = nomes e dados, 2 = chave e quarto 305) ============ */
function hotel(u,v){
  var r=rng(30+v),chand='';for(var i=0;i<5;i++){var x=150+i*45;chand+='<path d="M'+x+' 0V'+(18+(i%2)*6)+'" stroke="#8a6a3a" stroke-width="1.2"/><circle cx="'+x+'" cy="'+(24+(i%2)*6)+'" r="4" fill="#fff3c4"/>'+lamp(x,24+(i%2)*6,1.4);}
  var keys='<g><rect x="168" y="52" width="144" height="70" rx="5" fill="#3a2418"/><rect x="172" y="56" width="136" height="62" rx="3" fill="#5a3822"/>';
  for(var a=0;a<3;a++)for(var c=0;c<8;c++){var kx=180+c*16,ky=66+a*18,hot=(v===2&&a===1&&c===3);keys+='<circle cx="'+kx+'" cy="'+ky+'" r="1.3" fill="#d9b25a"/><path d="M'+kx+' '+ky+'V'+(ky+9)+'" stroke="'+(hot?'#ffe27a':'#c9a24a')+'" stroke-width="1.4"/><circle cx="'+kx+'" cy="'+(ky+11)+'" r="3.1" fill="'+(hot?'#ffe27a':'#e6c46a')+'"/>'+(hot?'<circle cx="'+kx+'" cy="'+(ky+11)+'" r="14" fill="url(#@lg)"/>':'');}
  keys+='</g>';
  var sign=v===1?'<g transform="translate(240 38)"><rect x="-56" y="-12" width="112" height="22" rx="4" fill="#1f2a3d"/><rect x="-56" y="-12" width="112" height="22" rx="4" fill="none" stroke="#d9b25a" stroke-width="1.4"/><text x="0" y="4" font-size="11" font-family="Georgia,serif" font-weight="700" fill="#e6c46a" text-anchor="middle" letter-spacing="1.4">HOTEL PLAZA</text></g>':'<g transform="translate(240 38)"><rect x="-56" y="-12" width="112" height="22" rx="4" fill="#1f2a3d"/><rect x="-56" y="-12" width="112" height="22" rx="4" fill="none" stroke="#d9b25a" stroke-width="1.4"/><text x="0" y="4" font-size="10" font-family="Georgia,serif" font-weight="700" fill="#e6c46a" text-anchor="middle" letter-spacing="1">WELCOME · ROOM 305</text></g>';
  var lift='<g transform="translate(60 40)"><rect x="-26" y="0" width="52" height="96" rx="3" fill="#2a2840"/><rect x="-22" y="6" width="21" height="90" fill="#c4c8d4"/><rect x="1" y="6" width="21" height="90" fill="#b0b5c4"/><path d="M-1 6V96" stroke="#6b6f84"/><rect x="-14" y="-12" width="28" height="10" rx="2" fill="#111a2a"/><text x="0" y="-4" font-size="8" font-family="Arial" font-weight="800" fill="#ff9a3c" text-anchor="middle">'+(v===2?'3':'1')+' ▲</text><rect x="-22" y="6" width="9" height="90" fill="#fff" opacity=".18"/></g>';
  var desk='<g><ellipse cx="240" cy="204" rx="130" ry="10" fill="#1a0f08" opacity=".35" filter="url(#@b)"/><rect x="118" y="146" width="244" height="58" rx="4" fill="url(#@dk)"/><rect x="112" y="140" width="256" height="9" rx="3" fill="#d9a870"/><rect x="112" y="140" width="256" height="2.4" fill="#fff" opacity=".35"/>'
   +'<g stroke="#e6c46a" stroke-width="1.4" opacity=".7"><path d="M126 160H354M126 188H354"/></g>'
   +'<g transform="translate(300 134)"><path d="M-8 0Q0-10 8 0Z" fill="#d9b25a"/><rect x="-1" y="-10" width="2" height="4" fill="#d9b25a"/></g>'
   +'<g transform="translate(150 134)"><rect x="-1" y="-22" width="2" height="22" fill="#4a3a2e"/><path d="M-10 -22Q0 -38 10 -22Z" fill="#f2d28a"/>'+lamp(0,-24,1.3)+'</g><g transform="translate(196 140)"><rect x="-14" y="-10" width="28" height="10" rx="1" fill="#fff"/><rect x="-14" y="-10" width="28" height="3" fill="#2f6fb5"/></g></g>';
  var plant='<g transform="translate(436 190)"><path d="M-14 0H14L10 -26H-10Z" fill="#8a5a3c"/><g fill="#4f8a55"><ellipse cx="-9" cy="-40" rx="7" ry="18" transform="rotate(-26 -9 -40)"/><ellipse cx="9" cy="-42" rx="7" ry="19" transform="rotate(24 9 -42)"/><ellipse cx="0" cy="-50" rx="7" ry="21"/></g></g>';
  var b=HEAD+'<defs>'+COM+'<linearGradient id="@wl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4a3a5a"/><stop offset="1" stop-color="#8a6a62"/></linearGradient><linearGradient id="@dk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8a5a34"/><stop offset="1" stop-color="#4b2a17"/></linearGradient><linearGradient id="@fl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d9cdb8"/><stop offset=".4" stop-color="#b3a58f"/><stop offset="1" stop-color="#6e6352"/></linearGradient></defs>'
   +'<rect width="480" height="150" fill="url(#@wl)"/><g stroke="#2a1a24" stroke-opacity=".25" fill="none">'+(function(){var s='';for(var i=0;i<10;i++)s+='<path d="M'+(i*52)+' 0V150"/>';return s})()+'</g><rect y="120" width="480" height="30" fill="#2a1a24" opacity=".25"/>'
   +'<ellipse cx="240" cy="70" rx="200" ry="80" fill="#ffd49a" opacity=".18" filter="url(#@b2)"/>'
   +keys+sign+lift+'<g>'+chand+'</g>'
   +'<rect y="146" width="480" height="128" fill="url(#@fl)"/><g stroke="#4a3f33" stroke-opacity=".22" fill="none">'+(function(){var s='';for(var i=0;i<7;i++){s+='<path d="M0 '+(154+i*18)+'H480"/>';}for(var j=0;j<14;j++){s+='<path d="M'+(j*38-14)+' 146L'+(240+(j*38-250)*2.3)+' 274"/>';}return s})()+'</g>'
   +'<ellipse cx="240" cy="190" rx="170" ry="26" fill="#ffd9a0" opacity=".35" filter="url(#@b2)"/>'+desk+plant+bokeh(r,10,40,200,['#ffe0a0','#ffb86b'])+FIN+'</svg>';
  return fin(u,b);
}
RS.lobby1=function(u){return hotel(u,1)};
RS.lobby2=function(u){return hotel(u,2)};

/* ============ v49: novos cenários pintados ============ */
function room(w1,w2,f1,f2,hy,ex){return '<defs>'+COM+'<linearGradient id="@wl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="'+w1+'"/><stop offset="1" stop-color="'+w2+'"/></linearGradient><linearGradient id="@fl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="'+f1+'"/><stop offset="1" stop-color="'+f2+'"/></linearGradient>'+(ex||'')+'</defs><rect width="480" height="'+hy+'" fill="url(#@wl)"/><rect y="'+hy+'" width="480" height="'+(270-hy)+'" fill="url(#@fl)"/>';}
function persp(hy,col,n){var s='<g stroke="'+col+'" stroke-opacity=".3" fill="none">';for(var i=0;i<6;i++)s+='<path d="M0 '+f(hy+10+i*i*3.6+i*8)+'H480"/>';for(var j=0;j<n;j++)s+='<path d="M'+f(j*480/(n-1)*0.55+108)+' '+hy+'L'+f((j-(n-1)/2)*150+240)+' 274"/>';return s+'</g>';}
function winv(x,y,w,h,sk){var s='<g><rect x="'+x+'" y="'+y+'" width="'+w+'" height="'+h+'" fill="url(#@sk)"/><circle cx="'+f(x+w*.6)+'" cy="'+f(y+h*.8)+'" r="'+f(h*.7)+'" fill="url(#@sn)"/><g filter="url(#@b)" fill="#8d82a8">';var r=rng(w+h);for(var i=0;i<8;i++){var bw=w/8,bh=h*(.25+r()*.4);s+='<rect x="'+f(x+i*bw)+'" y="'+f(y+h-bh)+'" width="'+f(bw-1)+'" height="'+f(bh)+'"/>';}return s+'</g><g stroke="#3a2418" stroke-width="4" fill="none"><rect x="'+x+'" y="'+y+'" width="'+w+'" height="'+h+'"/><path d="M'+f(x+w/2)+' '+y+'V'+(y+h)+'M'+x+' '+f(y+h*.5)+'H'+(x+w)+'"/></g></g>';}
function shad(x,y,rx){return '<ellipse cx="'+x+'" cy="'+y+'" rx="'+rx+'" ry="'+f(rx*.16)+'" fill="#120a14" opacity=".35" filter="url(#@b)"/>';}
function crowd(list){var s='';list.forEach(function(p){s+=person(p[0],p[1],p[2],p[3],p[4]||'#3a2a3a');});return s;}

RS.sub2=function(u){var r=rng(31),x,i;
  var b=HEAD+room('#1d2742','#3f5478','#7a7686','#3a3846',150)
   +'<g stroke="#e8e2cf" stroke-opacity=".18">'+(function(){var s='';for(i=0;i<12;i++)s+='<path d="M0 '+(80+i*6)+'H480"/>';for(i=0;i<40;i++)s+='<path d="M'+(i*12)+' 80V150"/>';return s})()+'</g>'
   +'<g><rect x="240" y="60" width="260" height="92" rx="6" fill="#cfd5df"/><rect x="240" y="104" width="260" height="8" fill="#e8742c"/>'+(function(){var s='';for(i=0;i<5;i++)s+='<rect x="'+(256+i*50)+'" y="72" width="34" height="26" rx="3" fill="#ffe7a8"/><rect x="'+(256+i*50)+'" y="72" width="34" height="26" rx="3" fill="url(#@lg)" opacity=".6"/>';return s})()+'<rect x="240" y="148" width="260" height="6" fill="#2a2a38"/></g>'
   +'<g fill="#2d3550"><rect x="64" y="0" width="22" height="270"/><rect x="190" y="0" width="22" height="270"/></g><g fill="#f2c94c"><rect x="64" y="0" width="3" height="270"/><rect x="190" y="0" width="3" height="270"/></g>'
   +(function(){var s='';[[75,70,'5'],[201,70,'2'],[330,34,'7']].forEach(function(c){s+='<circle cx="'+c[0]+'" cy="'+c[1]+'" r="13" fill="#2a8f4f" stroke="#fff" stroke-width="2"/><text x="'+c[0]+'" y="'+(c[1]+6)+'" text-anchor="middle" font-family="Arial,sans-serif" font-weight="700" font-size="17" fill="#fff">'+c[2]+'</text>';});return s})()
   +persp(150,'#16161f',9)+'<rect x="0" y="176" width="480" height="7" fill="#f2c94c" opacity=".85"/><rect x="0" y="183" width="480" height="3" fill="#1b1b24" opacity=".35"/>'
   +[60,200,340,450].map(function(x){return lamp(x,16,1.4)}).join('')
   +shad(130,246,38)+shad(380,252,44)+crowd([[130,246,1.5,'#7C4DFF'],[168,238,1.3,'#e85d75'],[380,252,1.7,'#12B3A8'],[300,232,1.2,'#f0b429']])
   +bokeh(r,12,40,150,['#ffe7a8','#9fd3ff'])+FIN+'</svg>';
  return fin(u,b);};

RS.tick=function(u){var r=rng(41),i,s='';
  var b=HEAD+room('#f0dcb8','#cfa376','#e8d8c0','#9a7e62',150)
   +[40,150,270,380].map(function(x){return '<g><path d="M'+x+' 120V60Q'+(x+30)+' 20 '+(x+60)+' 60V120Z" fill="url(#@sk)"/><circle cx="'+(x+40)+'" cy="100" r="34" fill="url(#@sn)"/><path d="M'+x+' 120V60Q'+(x+30)+' 20 '+(x+60)+' 60V120Z" fill="none" stroke="#7a5030" stroke-width="5"/></g>'}).join('')
   +'<g><rect x="168" y="28" width="144" height="44" rx="5" fill="#1d1a24"/>'+(function(){for(var k=0;k<4;k++)s+='<rect x="178" y="'+(35+k*9)+'" width="'+(70+(k*17)%40)+'" height="3" fill="#ffc857"/><rect x="274" y="'+(35+k*9)+'" width="26" height="3" fill="#7be07b"/>';return s})()+'</g>'
   +'<g><circle cx="240" cy="92" r="0"/></g>'
   +'<rect x="0" y="122" width="480" height="34" fill="#7a4a2c"/><rect x="0" y="118" width="480" height="6" fill="#d9a441"/>'
   +[30,185,340].map(function(x){return '<g><rect x="'+x+'" y="82" width="100" height="42" rx="3" fill="#bfe0f0" opacity=".55"/><rect x="'+x+'" y="82" width="100" height="42" rx="3" fill="none" stroke="#3a2418" stroke-width="3"/><rect x="'+(x+12)+'" y="124" width="76" height="4" fill="#1d1208"/></g>'}).join('')
   +'<g filter="url(#@b)"><ellipse cx="235" cy="100" rx="9" ry="10" fill="#3a2a3a"/><path d="M220 124Q235 78 250 124Z" fill="#0c7a78"/></g>'
   +persp(150,'#5a4030',9)
   +(function(){var t='';for(var k=0;k<8;k++)t+='<rect x="'+(k*60)+'" y="160" width="30" height="110" fill="#fff" opacity="'+(k%2?.0:.06)+'"/>';return t})()
   +lamp(100,20,1.6)+lamp(240,14,1.6)+lamp(380,20,1.6)
   +shad(110,248,40)+shad(380,244,40)+crowd([[110,250,1.6,'#7C4DFF'],[146,244,1.4,'#e85d75'],[200,240,1.2,'#12B3A8'],[380,244,1.5,'#f0b429'],[340,236,1.2,'#FF6F59']])
   +'<g transform="translate(430 232)"><rect x="-8" y="-20" width="26" height="20" rx="3" fill="#9a5a3c"/><rect x="-4" y="-26" width="18" height="6" rx="2" fill="#6b3a1e"/></g>'
   +bokeh(r,12,30,150,['#ffe0a0','#ffb86b'])+FIN+'</svg>';
  return fin(u,b);};

RS.cafe3=function(u){var r=rng(51),i,s='';
  var b=HEAD+room('#5e3722','#9a6238','#a8703e','#4b2a17',150)
   +'<g><rect x="140" y="18" width="200" height="86" rx="4" fill="#24352f" stroke="#a8703e" stroke-width="6"/>'+(function(){for(var k=0;k<5;k++)s+='<rect x="'+(156+(k%2)*6)+'" y="'+(32+k*14)+'" width="'+(70+(k*23)%60)+'" height="3" rx="1" fill="#f4efe6" opacity=".8"/><rect x="'+(268+(k%3)*4)+'" y="'+(32+k*14)+'" width="'+(30+(k*11)%24)+'" height="3" rx="1" fill="#ffc857" opacity=".8"/>';return s})()+'<text x="240" y="30" text-anchor="middle" font-family="Georgia,serif" font-size="12" fill="#fff" opacity=".9">MENU</text></g>'
   +'<g><rect x="14" y="40" width="96" height="4" fill="#2a1a10"/><rect x="14" y="76" width="96" height="4" fill="#2a1a10"/>'+(function(){var t='';for(var k=0;k<7;k++)t+='<rect x="'+(20+k*13)+'" y="'+(26+(k%2)*2)+'" width="9" height="14" rx="2" fill="'+['#f4e3c8','#c9553d','#e8b04a','#8fb3a6'][k%4]+'"/><rect x="'+(20+k*13)+'" y="'+(62+(k%3))+'" width="9" height="14" rx="2" fill="'+['#fff','#d9a441','#c9553d'][k%3]+'"/>';return t})()+'</g>'
   +'<g filter="url(#@b)"><ellipse cx="400" cy="92" rx="13" ry="14" fill="#2a1a24"/><path d="M380 150Q400 70 420 150Z" fill="#f4efe6"/></g>'
   +'<rect x="0" y="146" width="480" height="124" fill="url(#@fl)"/><rect x="0" y="146" width="480" height="8" fill="#e6c08a"/>'
   +'<g><rect x="30" y="156" width="120" height="70" rx="6" fill="#cfe9f2" opacity=".5" stroke="#3a2418" stroke-width="3"/>'+(function(){var t='';for(var k=0;k<6;k++)t+='<ellipse cx="'+(50+(k%3)*36)+'" cy="'+(180+Math.floor(k/3)*28)+'" rx="13" ry="7" fill="'+['#e8b04a','#c9553d','#f4d9b0'][k%3]+'"/>';return t})()+'</g>'
   +'<g transform="translate(360 172)"><rect x="-44" y="-8" width="88" height="46" rx="8" fill="#9fa3a8"/><rect x="-40" y="-14" width="80" height="10" rx="4" fill="#c9ced6"/><circle cx="-18" cy="14" r="8" fill="#2a2d32"/><circle cx="18" cy="14" r="8" fill="#2a2d32"/><rect x="-16" y="36" width="32" height="14" fill="#fff"/></g>'
   +'<g>'+[0,1,2].map(function(k){return '<g transform="translate('+(190+k*34)+' 206)"><path d="M-9 0H9L7 14H-7Z" fill="#fff"/><ellipse cx="0" cy="0" rx="9" ry="2.4" fill="#6b3a1e"/></g>'}).join('')+'</g>'
   +[90,240,390].map(function(x){return '<path d="M'+x+' 0V28" stroke="#2a1a10" stroke-width="1.4"/><path d="M'+(x-12)+' 40Q'+x+' 22 '+(x+12)+' 40Z" fill="#d9a441"/>'+lamp(x,38,1.5)}).join('')
   +'<ellipse cx="240" cy="180" rx="190" ry="22" fill="#ffd49a" opacity=".22" filter="url(#@b2)"/>'
   +bokeh(r,12,50,200,['#ffe0a0','#ffb86b'])+FIN+'</svg>';
  return fin(u,b);};

RS.diner=function(u){var r=rng(61),i;
  var b=HEAD+room('#2c6e72','#17454c','#e8e2d4','#6a2f2a',150,'<linearGradient id="@ng" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1a1d3a"/><stop offset="1" stop-color="#5a3a6a"/></linearGradient>')
   +'<g><rect x="30" y="30" width="190" height="96" fill="url(#@ng)"/>'+(function(){var s='';for(var k=0;k<14;k++)s+='<rect x="'+(34+k*13)+'" y="'+(70+(k*17)%40)+'" width="10" height="'+(56-(k*17)%40)+'" fill="#2a2a50"/>';for(k=0;k<30;k++)s+='<rect x="'+f(36+r()*180)+'" y="'+f(70+r()*52)+'" width="1.6" height="2" fill="#ffe7a8" opacity=".8"/>';return s})()+'<rect x="30" y="30" width="190" height="96" fill="none" stroke="#d9d4c4" stroke-width="5"/><path d="M125 30V126" stroke="#d9d4c4" stroke-width="4"/></g>'
   +'<g><rect x="258" y="38" width="150" height="40" rx="8" fill="#1a0f1c"/><text x="333" y="66" text-anchor="middle" font-family="Arial,sans-serif" font-weight="800" font-size="26" fill="#ff5d8f" letter-spacing="4">OPEN</text><rect x="258" y="38" width="150" height="40" rx="8" fill="none" stroke="#ff5d8f" stroke-width="2.5"/><circle cx="333" cy="58" r="70" fill="url(#@lg)" opacity=".35"/></g>'
   +'<g fill="#7a1f2a"><rect x="0" y="128" width="480" height="8"/></g>'
   +(function(){var s='';for(var j=0;j<6;j++)for(var k=0;k<16;k++)s+='<rect x="'+(k*30+(j%2)*15-15)+'" y="'+(150+j*j*4+j*4)+'" width="30" height="'+(10+j*3)+'" fill="'+((j+k)%2?'#e8e2d4':'#b84a44')+'" opacity=".55"/>';return s})()
   +'<g><rect x="60" y="150" width="190" height="82" rx="14" fill="#b32f3c"/><rect x="60" y="150" width="190" height="14" rx="7" fill="#d9525e"/></g>'
   +'<g><rect x="90" y="196" width="130" height="10" rx="3" fill="#e8e2d4"/><rect x="150" y="206" width="10" height="40" fill="#9aa0a8"/>'+'<g transform="translate(110 192)"><path d="M-8 0H8L6 -22H-6Z" fill="#c9553d" opacity=".9"/><ellipse cx="0" cy="-22" rx="8" ry="2.4" fill="#fff"/></g><g transform="translate(170 194)"><path d="M-16 0H16L12 -9H-12Z" fill="#f4d9b0"/><ellipse cx="0" cy="-9" rx="14" ry="3" fill="#e8b04a"/></g><g transform="translate(205 196)"><rect x="-10" y="-8" width="20" height="9" fill="#fff"/><rect x="-6" y="-6" width="12" height="2" fill="#bbb"/></g></g>'
   +'<g transform="translate(400 150)"><rect x="-34" y="-8" width="68" height="110" rx="14" fill="#7a1f2a"/><rect x="-26" y="0" width="52" height="40" rx="8" fill="#ffc857" opacity=".9"/><circle cx="0" cy="62" r="14" fill="#2a1a24"/><rect x="-26" y="84" width="52" height="8" fill="#ff5d8f"/></g>'
   +lamp(120,18,1.6)+lamp(330,18,1.6)+shad(150,252,70)+crowd([[300,246,1.5,'#12B3A8'],[90,236,1.5,'#7C4DFF']])
   +bokeh(r,14,30,160,['#ff7aa8','#ffe7a8','#9fd3ff'])+FIN+'</svg>';
  return fin(u,b);};

RS.home1=function(u){var r=rng(71);
  var b=HEAD+room('#ecd0a8','#c79a68','#8a5a38','#4a2a18',166)
   +winv(300,32,130,100)
   +'<g>'+[[60,40,40,50],[110,30,34,44],[154,44,46,56],[200,34,36,46]].map(function(p,k){return '<rect x="'+p[0]+'" y="'+p[1]+'" width="'+p[2]+'" height="'+p[3]+'" fill="#f4efe6" stroke="#6b3f27" stroke-width="3"/><rect x="'+(p[0]+5)+'" y="'+(p[1]+5)+'" width="'+(p[2]-10)+'" height="'+(p[3]-10)+'" fill="'+['#e8a07a','#8fb3a6','#e8c46a','#b79ad8'][k]+'"/><ellipse cx="'+(p[0]+p[2]/2)+'" cy="'+(p[1]+p[3]/2)+'" rx="7" ry="9" fill="#5a3a2a" opacity=".6"/>'}).join('')+'</g>'
   +'<ellipse cx="200" cy="232" rx="170" ry="26" fill="#c9553d" opacity=".55"/><ellipse cx="200" cy="232" rx="140" ry="18" fill="#e8b04a" opacity=".35"/>'
   +'<g><rect x="30" y="140" width="250" height="70" rx="22" fill="#4f7a8a"/><rect x="30" y="118" width="250" height="40" rx="18" fill="#5f8ea0"/><rect x="18" y="136" width="30" height="72" rx="14" fill="#4f7a8a"/><rect x="262" y="136" width="30" height="72" rx="14" fill="#4f7a8a"/><ellipse cx="80" cy="150" rx="22" ry="16" fill="#e8a07a"/><ellipse cx="226" cy="150" rx="22" ry="16" fill="#e8c46a"/><rect x="40" y="206" width="12" height="14" fill="#2a1a10"/><rect x="258" y="206" width="12" height="14" fill="#2a1a10"/></g>'
   +'<g transform="translate(390 170)"><rect x="-20" y="0" width="40" height="46" rx="4" fill="#7a4a2c"/><rect x="-16" y="-62" width="4" height="62" fill="#3a2418"/><path d="M-34 -62H6L-2 -92H-26Z" fill="#f4d9b0"/>'+lamp(-14,-66,2.4)+'</g>'
   +'<g transform="translate(330 214)" filter="url(#@b)"><ellipse cx="0" cy="-10" rx="12" ry="10" fill="#8a5a38"/><ellipse cx="-8" cy="-26" rx="8" ry="8" fill="#8a5a38"/><path d="M-12 -32l-4 -8l8 4Z" fill="#6b3f27"/><path d="M-8 -32l4 -8l4 8Z" fill="#6b3f27"/><rect x="6" y="-12" width="16" height="6" rx="3" fill="#8a5a38"/></g>'
   +'<g transform="translate(446 150)"><path d="M-12 0H12L9 -24H-9Z" fill="#9c5a3c"/><g fill="#4f8a55"><ellipse cx="-8" cy="-38" rx="6" ry="16" transform="rotate(-24 -8 -38)"/><ellipse cx="8" cy="-40" rx="6" ry="17" transform="rotate(22 8 -40)"/><ellipse cx="0" cy="-46" rx="6" ry="19"/></g></g>'
   +'<ellipse cx="240" cy="196" rx="200" ry="26" fill="#ffd49a" opacity=".2" filter="url(#@b2)"/>'
   +bokeh(r,10,40,180,['#ffe0a0','#ffb86b'])+FIN+'</svg>';
  return fin(u,b);};

RS.yard=function(u){var r=rng(81),i;
  var b=HEAD+'<defs>'+COM+'</defs><rect width="480" height="270" fill="url(#@sk)"/><circle cx="360" cy="150" r="130" fill="url(#@sn)"/>'
   +'<g filter="url(#@b)"><ellipse cx="300" cy="50" rx="110" ry="6" fill="url(#@cl)"/><ellipse cx="90" cy="68" rx="80" ry="5" fill="url(#@cl)"/></g>'
   +'<path d="M0 150Q80 118 170 142T340 138T480 146V270H0Z" fill="#5d7a58"/><path d="M0 168Q120 150 240 164T480 160V270H0Z" fill="#6f9060"/>'
   +[[50,120,36],[130,128,30],[420,116,40],[360,126,28]].map(function(t){return '<g filter="url(#@b)"><rect x="'+(t[0]-3)+'" y="'+t[1]+'" width="6" height="'+(40)+'" fill="#4a3a2a"/><ellipse cx="'+t[0]+'" cy="'+(t[1]-6)+'" rx="'+t[2]+'" ry="'+(t[2]*.9)+'" fill="#3f6a48"/></g>'}).join('')
   +'<g stroke="#4a3a2a" stroke-width="1.4" fill="none"><path d="M0 70Q120 110 240 80T480 90"/></g>'+(function(){var s='';for(i=0;i<14;i++){var x=i*36+6,y=78+Math.sin(i*.6)*14+(i*6)%12;s+='<circle cx="'+x+'" cy="'+f(y)+'" r="10" fill="url(#@lg)"/><circle cx="'+x+'" cy="'+f(y)+'" r="2.4" fill="#fffbe6"/>';}return s})()
   +'<g><rect x="70" y="190" width="260" height="14" rx="3" fill="#a8703e"/><rect x="82" y="204" width="8" height="38" fill="#6b3f27"/><rect x="310" y="204" width="8" height="38" fill="#6b3f27"/>'+(function(){var s='';[110,170,230,290].forEach(function(x,k){s+='<ellipse cx="'+x+'" cy="188" rx="14" ry="4" fill="'+['#f4efe6','#e8b04a','#c9553d','#8fb3a6'][k]+'"/><rect x="'+(x-3)+'" y="170" width="6" height="18" fill="'+['#c9553d','#fff','#e8b04a','#fff'][k]+'" opacity=".0"/>';});return s})()+'</g>'
   +'<g transform="translate(400 200)"><rect x="-22" y="-20" width="44" height="22" rx="8" fill="#2a2d32"/><rect x="-3" y="0" width="6" height="40" fill="#2a2d32"/><g opacity=".4" filter="url(#@b)"><ellipse cx="0" cy="-40" rx="8" ry="16" fill="#fff"/></g></g>'
   +shad(110,244,80)+crowd([[96,236,1.7,'#7C4DFF'],[134,236,1.45,'#e85d75'],[176,236,1.1,'#12B3A8'],[300,240,1.8,'#f0b429'],[340,240,1.4,'#FF6F59'],[250,238,.9,'#b79ad8']])
   +bokeh(r,14,60,200,['#ffe0a0','#ffb86b','#fff'])+FIN+'</svg>';
  return fin(u,b);};

RS.park2=function(u){var r=rng(91),i;
  var b=HEAD+'<defs>'+COM+'</defs><rect width="480" height="270" fill="url(#@sk)"/><circle cx="110" cy="150" r="140" fill="url(#@sn)"/>'
   +'<g filter="url(#@b)"><ellipse cx="320" cy="44" rx="110" ry="6" fill="url(#@cl)"/><ellipse cx="380" cy="76" rx="60" ry="7" fill="url(#@cl)"/></g>'
   +'<g filter="url(#@b)" fill="#8d82a8"><rect x="300" y="110" width="22" height="46"/><rect x="326" y="96" width="18" height="60"/><rect x="348" y="116" width="26" height="40"/><rect x="378" y="100" width="16" height="56"/><rect x="398" y="120" width="30" height="36"/></g>'
   +'<path d="M0 152Q100 128 200 148T400 142T480 150V270H0Z" fill="#6f9a5a"/><path d="M0 180Q140 160 280 178T480 172V270H0Z" fill="#7fae68"/><path d="M180 270Q220 200 260 176T330 164L350 168Q300 190 280 270Z" fill="#e0cfa0" opacity=".9"/>'
   +[[40,116,32],[96,126,26],[440,112,34]].map(function(t){return '<g filter="url(#@b)"><rect x="'+(t[0]-4)+'" y="'+t[1]+'" width="8" height="44" fill="#4a3a2a"/><ellipse cx="'+t[0]+'" cy="'+(t[1]-8)+'" rx="'+t[2]+'" ry="'+(t[2]*.95)+'" fill="#4f8a55"/></g>'}).join('')
   +'<g transform="translate(150 190)"><path d="M-30 0H30" stroke="#6b3f27" stroke-width="6"/><path d="M-26 0V-24H26V0" stroke="#6b3f27" stroke-width="5" fill="none"/><rect x="-28" y="-26" width="56" height="6" fill="#a8703e"/><rect x="-28" y="-14" width="56" height="6" fill="#a8703e"/></g>'
   +'<g><path d="M380 70Q372 90 390 96Q408 90 400 70Z" fill="#e85d75"/><path d="M390 96Q392 130 384 150" stroke="#fff" fill="none" stroke-width="1"/></g>'
   +shad(250,252,80)+crowd([[230,248,2.0,'#7C4DFF'],[272,248,1.2,'#e85d75'],[330,244,1.6,'#12B3A8'],[366,244,2.3,'#f0b429'],[100,236,1.0,'#FF6F59']])
   +bokeh(r,10,40,170,['#fff6c8','#ffe0a0'])+FIN+'</svg>';
  return fin(u,b);};

RS.school=function(u){var r=rng(101),i;
  var b=HEAD+room('#cfe3d4','#a5c4b0','#b98a5a','#6a4528',156)
   +'<g><rect x="120" y="22" width="240" height="106" rx="4" fill="#24493a" stroke="#a8703e" stroke-width="7"/>'+(function(){var s='';s+='<circle cx="170" cy="70" r="16" fill="none" stroke="#f4efe6" stroke-width="2" opacity=".85"/><path d="M162 76q8 8 16 0M162 66h2M176 66h2" stroke="#f4efe6" fill="none" stroke-width="2" opacity=".85"/>';for(var k=0;k<4;k++)s+='<rect x="'+(216+(k%2)*8)+'" y="'+(40+k*18)+'" width="'+(70+(k*19)%50)+'" height="3" rx="1" fill="#f4efe6" opacity=".8"/>';return s})()+'<rect x="130" y="118" width="220" height="5" fill="#8a5a38"/></g>'
   +winv(14,36,92,84)+winv(374,36,92,84)
   +'<g transform="translate(240 160)"><path d="M-6 0V-28" stroke="#6b3f27" stroke-width="3"/><circle cx="0" cy="-42" r="16" fill="#2a6fa8"/><path d="M-16 -42Q0 -34 16 -42M-4 -58Q4 -42 -4 -26" stroke="#8fd08f" stroke-width="3" fill="none"/></g>'
   +persp(156,'#3a2418',9)
   +(function(){var s='';[[60,210,1.1],[180,214,1.1],[300,210,1.1],[420,214,1.1],[110,244,1.4],[260,248,1.4],[390,244,1.4]].forEach(function(d){var x=d[0],y=d[1],k=d[2];s+='<g transform="translate('+x+' '+y+') scale('+k+')"><ellipse cx="0" cy="22" rx="30" ry="5" fill="#120a14" opacity=".3" filter="url(#@b)"/><rect x="-30" y="0" width="60" height="8" rx="2" fill="#d9a441"/><rect x="-26" y="8" width="4" height="16" fill="#6b3f27"/><rect x="22" y="8" width="4" height="16" fill="#6b3f27"/><rect x="-12" y="-6" width="22" height="7" fill="#c9553d"/><rect x="-8" y="-12" width="22" height="6" fill="#4a7ac8"/></g>';});return s})()
   +'<g filter="url(#@b)"><ellipse cx="410" cy="132" rx="9" ry="10" fill="#3a2a3a"/><path d="M396 158Q410 112 424 158Z" fill="#e85d75"/></g>'
   +lamp(240,10,1.6)+bokeh(r,10,30,150,['#fff6c8','#ffe0a0'])+FIN+'</svg>';
  return fin(u,b);};

RS.shop=function(u){var r=rng(111),i;
  var cols=['#e34a5f','#f7c948','#3f8fe0','#5cb85c','#2a2d32','#f4efe6'];
  var b=HEAD+room('#7a4a6a','#4a2a45','#b98a5a','#5a3a22',146)
   +(function(){var s='';for(var row=0;row<3;row++){s+='<rect x="30" y="'+(28+row*38+30)+'" width="420" height="5" fill="#2a1a24"/>';for(var k=0;k<12;k++){var c=cols[(k+row*2)%6];s+='<rect x="'+(38+k*34)+'" y="'+(28+row*38+8)+'" width="26" height="'+(24+(k*7+row*5)%6)+'" rx="3" fill="'+c+'"/><rect x="'+(38+k*34)+'" y="'+(28+row*38+8)+'" width="26" height="6" rx="3" fill="#fff" opacity=".25"/>';}}return s})()
   +'<rect x="0" y="146" width="480" height="124" fill="url(#@fl)"/><rect x="0" y="146" width="480" height="8" fill="#d9a441"/>'
   +'<g><rect x="260" y="168" width="200" height="60" rx="6" fill="#8a5a38"/><rect x="254" y="162" width="212" height="10" rx="4" fill="#d9a441"/>'+cols.map(function(c,k){return '<rect x="'+(274+k*30)+'" y="144" width="22" height="18" rx="3" fill="'+c+'"/>'}).join('')+'</g>'
   +'<g transform="translate(110 190)">'+cols.map(function(c,k){return '<ellipse cx="'+((k%3)*34-34)+'" cy="'+(Math.floor(k/3)*-26+6)+'" rx="14" ry="13" fill="'+c+'"/><ellipse cx="'+((k%3)*34-38)+'" cy="'+(Math.floor(k/3)*-26)+'" rx="4" ry="3" fill="#fff" opacity=".4"/>'}).join('')+'</g>'
   +[100,240,380].map(function(x){return '<path d="M'+x+' 0V10" stroke="#2a1a10"/><path d="M'+(x-14)+' 24Q'+x+' 6 '+(x+14)+' 24Z" fill="#ffc857"/>'+lamp(x,24,1.5)}).join('')
   +shad(180,250,60)+crowd([[180,250,1.7,'#7C4DFF'],[210,242,1.3,'#12B3A8']])
   +'<g filter="url(#@b)"><ellipse cx="370" cy="136" rx="10" ry="11" fill="#3a2a3a"/><path d="M356 176Q370 124 384 176Z" fill="#f4efe6"/></g>'
   +bokeh(r,12,40,200,['#ffe0a0','#ff9ac0','#9fd3ff'])+FIN+'</svg>';
  return fin(u,b);};


/* ===== cenários extras (Neighbors): office, clinic, kitchen, bedroom, bath, counter, gym, hall, street ===== */
function rect(x,y,w,h,c,rx,o){return '<rect x="'+x+'" y="'+y+'" width="'+w+'" height="'+h+'" fill="'+c+'"'+(rx?' rx="'+rx+'"':'')+(o?' opacity="'+o+'"':'')+'/>';}
function plantP(x,y,s){return '<g transform="translate('+x+' '+y+') scale('+s+')"><path d="M-12 0H12L9 -24H-9Z" fill="#9c5a3c"/><g fill="#4f8a55"><ellipse cx="-8" cy="-38" rx="6" ry="16" transform="rotate(-24 -8 -38)"/><ellipse cx="8" cy="-40" rx="6" ry="17" transform="rotate(22 8 -40)"/><ellipse cx="0" cy="-46" rx="6" ry="19"/></g></g>';}
function ceilLamps(xs){return xs.map(function(x){return rect(x-18,0,36,5,'#e9e4d8',2)+lamp(x,8,1.7)}).join('');}

RS.office=function(u){var r=rng(121),i;
  var b=HEAD+room('#dfe6ee','#b8c4d2','#8d8f98','#4d4f5c',160)
   +winv(30,28,150,104)+winv(300,28,150,104)
   +'<g>'+rect(190,36,100,70,'#f4f5f7',3)+'<rect x="190" y="36" width="100" height="70" fill="none" stroke="#9aa3b0" stroke-width="4" rx="3"/><path d="M204 88L226 62L246 76L274 48" stroke="#2a8f4f" stroke-width="3" fill="none"/>'+rect(204,92,20,4,'#c9553d')+rect(232,92,30,4,'#2e6f95')+'</g>'
   +persp(160,'#2a2a34',9)
   +'<g>'+rect(40,176,190,12,'#b98a5a',3)+rect(48,188,10,52,'#6b4a2e')+rect(212,188,10,52,'#6b4a2e')+rect(86,148,58,28,'#22252c',3)+rect(100,176,30,6,'#22252c')+rect(88,150,54,22,'#8fd0f0',2,'.85')+rect(166,162,34,14,'#f4efe6',2)+rect(172,156,22,6,'#c9553d',2)+'</g>'
   +'<g>'+rect(258,176,190,12,'#b98a5a',3)+rect(266,188,10,52,'#6b4a2e')+rect(430,188,10,52,'#6b4a2e')+rect(310,148,58,28,'#22252c',3)+rect(324,176,30,6,'#22252c')+rect(312,150,54,22,'#a8d8ff',2,'.85')+'</g>'
   +'<g transform="translate(150 214)"><rect x="-20" y="-6" width="40" height="30" rx="10" fill="#2e4a6a"/><rect x="-16" y="-34" width="32" height="32" rx="8" fill="#3a5c82"/><rect x="-2" y="22" width="4" height="22" fill="#222"/><ellipse cx="0" cy="46" rx="20" ry="4" fill="#222"/></g>'
   +plantP(456,176,1.1)+ceilLamps([100,240,380])
   +shad(330,250,50)+crowd([[330,248,1.9,'#e85d75'],[390,246,1.5,'#12B3A8']])
   +bokeh(r,8,40,160,['#fff6c8','#cfe6ff'])+FIN+'</svg>';
  return fin(u,b);};

RS.clinic=function(u){var r=rng(131),i;
  var b=HEAD+room('#e4f1f0','#bcd9d6','#d8dcd8','#a4aaa6',158)
   +'<g>'+rect(180,26,120,54,'#fff',4)+'<rect x="180" y="26" width="120" height="54" rx="4" fill="none" stroke="#8fb8b4" stroke-width="3"/><rect x="226" y="34" width="28" height="38" rx="3" fill="#d9534f" opacity=".0"/><path d="M233 40h14v10h10v14h-10v10h-14v-10h-10V50h10z" fill="#d9534f"/></g>'
   +winv(30,34,110,84)
   +'<g>'+rect(330,40,100,70,'#f7fbfb',3)+'<path d="M346 62q12-16 24 0t24 0" stroke="#5aa6a0" stroke-width="3" fill="none"/>'+rect(346,82,60,4,'#9db8b6')+rect(346,92,44,4,'#9db8b6')+'</g>'
   +persp(158,'#4a5552',9)
   +'<g>'+rect(190,170,160,52,'#f2f5f5',8)+rect(184,164,172,12,'#e0a74a',5)+rect(204,150,36,14,'#3a5c82',3)+rect(262,140,52,24,'#22252c',3)+rect(266,143,44,18,'#8fd0f0',2,'.8')+'</g>'
   +'<g transform="translate(70 220)">'+rect(-50,-20,100,16,'#4f9a96',8)+rect(-50,-6,100,12,'#f2f5f5',4)+rect(-46,6,6,26,'#8a9290')+rect(40,6,6,26,'#8a9290')+rect(30,-40,22,22,'#fff',6)+'</g>'
   +'<g transform="translate(420 226)">'+[0,36].map(function(x){return rect(-60+x,-34,30,34,'#4f9a96',6)+rect(-60+x,0,30,6,'#2f6a66')}).join('')+'</g>'
   +plantP(32,168,1)+ceilLamps([110,250,380])
   +shad(250,252,50)+crowd([[250,252,1.9,'#fff','#3a2a3a'],[300,246,1.5,'#7C4DFF']])
   +bokeh(r,8,40,150,['#fff','#cfeeea'])+FIN+'</svg>';
  return fin(u,b);};

RS.kitchen=function(u){var r=rng(141),i;
  var b=HEAD+room('#f1e3c0','#dcc592','#b58a5a','#6a4528',172)
   +(function(){var s='';for(var y=96;y<172;y+=19)for(var x=0;x<480;x+=24)s+='<rect x="'+(x+(((y-96)/19)%2?12:0))+'" y="'+y+'" width="22" height="17" fill="#fff7e6" opacity=".6" rx="1"/>';return s})()
   +'<g>'+[[10,18],[130,18],[330,18]].map(function(p){return rect(p[0],p[1],108,60,'#6aa6a0',3)+rect(p[0]+4,p[1]+4,48,52,'#7fbab4',2)+rect(p[0]+56,p[1]+4,48,52,'#7fbab4',2)+rect(p[0]+46,p[1]+26,4,10,'#e8d8b0')+rect(p[0]+58,p[1]+26,4,10,'#e8d8b0')}).join('')+'</g>'
   +winv(250,34,70,56)
   +rect(0,150,480,10,'#e8d8b0')+rect(0,160,480,62,'#4f8a86')+rect(0,160,480,4,'#2f6a66')
   +'<g transform="translate(76 156)"><rect x="-44" y="-10" width="88" height="14" fill="#2a2d32" rx="3"/><ellipse cx="-20" cy="-12" rx="16" ry="4" fill="#555"/><ellipse cx="20" cy="-12" rx="16" ry="4" fill="#555"/><path d="M-34 -14h28l-3 -20h-22z" fill="#c9553d"/><rect x="-14" y="-38" width="8" height="5" fill="#222"/><g filter="url(#@b)" opacity=".5"><ellipse cx="-20" cy="-48" rx="6" ry="10" fill="#fff"/></g></g>'
   +'<g transform="translate(400 70)"><rect x="-30" y="0" width="60" height="150" rx="6" fill="#e9eef2"/><rect x="-30" y="56" width="60" height="4" fill="#9aa6b0"/><rect x="22" y="14" width="4" height="26" fill="#9aa6b0"/><rect x="22" y="70" width="4" height="30" fill="#9aa6b0"/></g>'
   +'<g>'+[0,1,2].map(function(k){return rect(190+k*22,138,16,18,['#e34a5f','#f7c948','#3f8fe0'][k],3)}).join('')+'<rect x="150" y="146" width="30" height="4" fill="#fff" opacity=".4"/></g>'
   +'<g stroke="#2a2d32" stroke-width="2">'+[[170,0,98],[210,0,92]].map(function(p){return '<path d="M'+p[0]+' 0V'+p[2]}).join('')+'</g>'+'<circle cx="170" cy="108" r="14" fill="#444"/><circle cx="210" cy="100" r="11" fill="#666"/>'
   +'<ellipse cx="240" cy="232" rx="150" ry="22" fill="#c9553d" opacity=".4"/>'
   +lamp(250,16,1.6)+shad(300,250,50)+crowd([[300,252,2.0,'#7C4DFF']])
   +bokeh(r,8,40,150,['#ffe0a0','#ffb86b'])+FIN+'</svg>';
  return fin(u,b);};

RS.bedroom=function(u){var r=rng(151),i;
  var b=HEAD+room('#d6cfe8','#a79cc8','#b98a5a','#6a4528',170)
   +'<g>'+rect(30,28,56,40,'#f4efe6',2)+rect(36,34,44,28,'#e8a07a')+rect(100,36,40,52,'#f4efe6',2)+rect(105,41,30,42,'#8fb3a6')+'</g>'
   +'<g><rect x="310" y="26" width="120" height="96" fill="#1c2d5c"/><circle cx="380" cy="60" r="16" fill="#f7f1dc"/><circle cx="388" cy="56" r="14" fill="#1c2d5c"/>'+[[330,44],[350,90],[410,100],[420,50],[336,100]].map(function(p){return '<circle cx="'+p[0]+'" cy="'+p[1]+'" r="1.6" fill="#fff"/>'}).join('')+'<rect x="310" y="26" width="120" height="96" fill="none" stroke="#f4efe6" stroke-width="6"/><path d="M370 26V122M310 74H430" stroke="#f4efe6" stroke-width="4"/><path d="M300 20Q320 80 306 130M440 20Q420 80 434 130" stroke="#c9553d" stroke-width="14" fill="none" opacity=".75"/></g>'
   +'<ellipse cx="190" cy="236" rx="150" ry="22" fill="#4f7a8a" opacity=".5"/>'
   +'<g>'+rect(20,134,260,86,'#8a5a38',8)+rect(24,100,252,50,'#f4efe6',8)+rect(24,140,252,70,'#5f8ea0',10)+rect(24,140,252,16,'#7fb0c4',8)+rect(40,108,70,32,'#fff',12)+rect(120,108,70,32,'#fff',12)+rect(26,192,248,6,'#fff',2,'.35')+rect(14,100,10,120,'#6b3f27',4)+'</g>'
   +'<g transform="translate(330 176)">'+rect(-24,0,48,50,'#7a4a2c',4)+rect(-20,10,40,4,'#3a2418')+rect(-18,-48,4,48,'#3a2418')+'<path d="M-32 -48H4L-2 -78H-26Z" fill="#f4d9b0"/>'+lamp(-14,-52,2.6)+rect(8,-12,16,12,'#e8c46a',2)+'</g>'
   +bokeh(r,10,40,180,['#ffe0a0','#c9a8ff'])+FIN+'</svg>';
  return fin(u,b);};

RS.bath=function(u){var r=rng(161),i;
  var b=HEAD+room('#d4ecef','#a7d1d8','#e8e2d4','#b0a890',176)
   +(function(){var s='';for(var y=0;y<176;y+=22)for(var x=0;x<480;x+=22)s+='<rect x="'+x+'" y="'+y+'" width="21" height="21" fill="#fff" opacity=".28"/>';return s})()
   +'<g>'+rect(150,34,96,86,'#e6f2f6',6)+'<rect x="150" y="34" width="96" height="86" rx="6" fill="none" stroke="#c6d4d8" stroke-width="5"/><path d="M162 50L196 110" stroke="#fff" stroke-width="5" opacity=".7"/>'+'</g>'
   +'<g>'+rect(130,122,136,12,'#f6f6f2',6)+rect(168,134,60,40,'#f0efe8',4)+'<ellipse cx="198" cy="124" rx="30" ry="6" fill="#cfe0e4"/><path d="M198 98v22" stroke="#9aa6b0" stroke-width="4"/><path d="M198 98h12" stroke="#9aa6b0" stroke-width="4"/></g>'
   +'<g>'+rect(310,20,164,160,'#eef7f8')+rect(322,32,10,120,'#fff',5,'.0')+'<path d="M310 20Q340 60 330 120M310 20H474" stroke="#8fb3b6" stroke-width="3" fill="none"/>'+[0,1,2,3,4,5,6].map(function(k){return '<circle cx="'+(322+k*22)+'" cy="28" r="4" fill="#9aa6b0"/><path d="M'+(322+k*22)+' 32Q'+(328+k*22)+' 100 '+(322+k*22)+' 178" stroke="#8fd0e0" stroke-width="10" opacity=".35" fill="none"/>'}).join('')+rect(300,140,14,14,'#9aa6b0',7)+'</g>'
   +'<g transform="translate(60 170)">'+rect(-6,0,4,4,'#fff',0,0)+'<path d="M-30 -6H30" stroke="#b9a37a" stroke-width="4"/><path d="M-24 -6V30H24V-6Z" fill="#e85d75"/><path d="M-24 0H24" stroke="#fff" opacity=".4" stroke-width="3"/>'+'<g transform="translate(0 -70)"><rect x="-30" y="-14" width="60" height="4" fill="#b9a37a"/><path d="M-24 -10V40H-4V-10Z" fill="#7fb0c4"/><path d="M4 -10V40H24V-10Z" fill="#f4efe6"/></g></g>'
   +'<g transform="translate(262 206)"><ellipse cx="0" cy="12" rx="30" ry="6" fill="#120a14" opacity=".25"/>'+rect(-14,-52,28,28,'#f6f6f2',8)+rect(-18,-26,36,32,'#f0efe8',12)+'</g>'
   +'<ellipse cx="240" cy="236" rx="160" ry="20" fill="#7fb0c4" opacity=".35"/>'
   +lamp(240,12,1.6)+bokeh(r,8,40,170,['#fff','#cfeeea'])+FIN+'</svg>';
  return fin(u,b);};

RS.counter=function(u){var r=rng(171),i;
  var b=HEAD+room('#dde6dc','#b6c6b4','#c9c4b6','#8d8878',156)
   +'<g>'+rect(170,20,140,40,'#1d2a3a',4)+'<rect x="170" y="20" width="140" height="40" rx="4" fill="none" stroke="#8a95a4" stroke-width="3"/><text x="240" y="48" text-anchor="middle" font-family="Arial,sans-serif" font-weight="700" font-size="24" fill="#ffc857">A 27</text></g>'
   +'<g>'+rect(30,28,100,66,'#f4f5f7',3)+rect(40,40,60,5,'#2e6f95')+rect(40,52,76,4,'#9aa3b0')+rect(40,62,50,4,'#9aa3b0')+rect(40,72,66,4,'#9aa3b0')+'</g>'
   +'<g>'+rect(340,24,110,60,'#2e4a6a',4)+'<text x="395" y="62" text-anchor="middle" font-family="Arial,sans-serif" font-weight="700" font-size="22" fill="#fff">INFO</text></g>'
   +persp(156,'#3a3a34',9)
   +'<g>'+rect(40,150,400,10,'#8a5a38',3)+rect(40,160,400,70,'#a8703e',4)+[1,2,3].map(function(k){return rect(40+k*100,106,4,46,'#cfe6ff',0,'.5')}).join('')+rect(40,104,400,4,'#8a95a4')+[0,1,2].map(function(k){return rect(64+k*130,118,74,30,'#cfe6ff',3,'.35')+rect(84+k*130,140,34,6,'#f4efe6',2)}).join('')+'</g>'
   +'<g transform="translate(390 216)">'+rect(-18,-40,36,60,'#2a2d32',5)+rect(-14,-34,28,22,'#8fd0f0',2)+rect(-10,-6,20,4,'#c9553d')+'</g>'
   +'<g stroke="#c9553d" stroke-width="3"><path d="M30 252H150M200 252H320"/></g>'+[30,150,200,320].map(function(x){return rect(x-2,236,4,18,'#c9a43a')}).join('')
   +ceilLamps([90,240,390])
   +shad(250,200,36)+crowd([[250,150,1.9,'#12B3A8'],[110,252,1.6,'#7C4DFF'],[300,250,1.4,'#e85d75']])
   +bokeh(r,8,40,150,['#fff6c8','#cfe6ff'])+FIN+'</svg>';
  return fin(u,b);};

RS.gym=function(u){var r=rng(181),i;
  var b=HEAD+room('#2b3347','#1d2236','#5a4a3a','#2c241c',170)
   +'<g>'+rect(20,26,440,112,'#a9c4d8',4,'.28')+'<path d="M80 26L40 138M200 26L160 138M320 26L280 138" stroke="#fff" stroke-width="10" opacity=".08"/><rect x="20" y="26" width="440" height="112" fill="none" stroke="#6a7288" stroke-width="4"/></g>'
   +'<g>'+rect(30,150,160,8,'#3a2418',2)+[0,1,2,3,4].map(function(k){return '<g transform="translate('+(46+k*30)+' 144)">'+rect(-9,-6,18,6,'#222',3)+rect(-3,-12,6,6,'#888')+rect(-9,-18,18,6,'#222',3)+'</g>'}).join('')+rect(30,158,160,40,'#2a2d32',3)+'</g>'
   +'<g transform="translate(330 200)">'+rect(-60,-8,130,8,'#222',3)+'<path d="M-50 -8L-30 -62H20L40 -8" stroke="#777" stroke-width="6" fill="none"/>'+rect(-36,-70,60,12,'#444',4)+rect(-30,-62,48,8,'#3fa7d6',2)+'</g>'
   +'<g transform="translate(110 236)">'+rect(-60,-4,120,8,'#5a8a5a',3)+rect(-80,6,160,5,'#3a6a3a',2)+'</g>'
   +'<g transform="translate(430 140)"><ellipse cx="0" cy="40" rx="18" ry="30" fill="#c9553d"/><path d="M0 10V-14" stroke="#555" stroke-width="3"/></g>'
   +'<g>'+rect(210,32,60,28,'#111',3)+'<text x="240" y="54" text-anchor="middle" font-family="Arial,sans-serif" font-weight="700" font-size="20" fill="#7be07b">06:30</text></g>'
   +ceilLamps([80,240,400])
   +shad(250,248,50)+crowd([[250,248,1.9,'#e85d75'],[200,244,1.6,'#12B3A8']])
   +bokeh(r,8,40,160,['#9fd3ff','#ff9ac0'])+FIN+'</svg>';
  return fin(u,b);};

RS.hall=function(u){var r=rng(191),i;
  var b=HEAD+room('#e9d9c0','#c7ae88','#8a3d3a','#4d1f20',150)
   +'<g>'+rect(150,50,180,100,'#8d939c',3)+rect(155,55,84,90,'#c5ccd6')+rect(241,55,84,90,'#c5ccd6')+rect(238,55,4,90,'#555')+'<path d="M225 36l15 -12l15 12z" fill="#ffc857"/><rect x="190" y="26" width="100" height="18" rx="3" fill="#1d1a24"/><text x="240" y="40" text-anchor="middle" font-family="Arial,sans-serif" font-weight="700" font-size="13" fill="#ffc857">3</text></g>'
   +'<g>'+[18,356].map(function(x,k){return rect(x,62,60,88,'#6b3f27',3)+rect(x+6,68,48,76,'#8a5a38',2)+'<circle cx="'+(x+50)+'" cy="108" r="3" fill="#e0c060"/>'+rect(x+16,48,28,12,'#d9a441',2)+'<text x="'+(x+30)+'" y="58" text-anchor="middle" font-family="Arial,sans-serif" font-weight="700" font-size="10" fill="#3a2418">'+(k?'3B':'3A')+'</text>'}).join('')+'</g>'
   +'<g>'+rect(420,66,52,70,'#9aa6b0',3)+[0,1,2,3].map(function(k){return rect(426+(k%2)*22,72+Math.floor(k/2)*32,20,26,'#cfd8e0',2)+rect(430+(k%2)*22,92+Math.floor(k/2)*32,12,3,'#555')}).join('')+'</g>'
   +'<path d="M120 270L210 150H270L360 270Z" fill="#a83a3a" opacity=".9"/><path d="M120 270L210 150" stroke="#e0c060" stroke-width="3"/><path d="M360 270L270 150" stroke="#e0c060" stroke-width="3"/>'
   +plantP(90,170,1.2)+ceilLamps([110,240,370])
   +'<g transform="translate(120 220)">'+rect(-20,-20,40,40,'#c9a46a',3)+rect(-20,-6,40,4,'#a8803a')+'</g>'
   +shad(300,246,40)+crowd([[300,246,1.8,'#12B3A8'],[340,238,1.3,'#7C4DFF']])
   +bokeh(r,8,40,150,['#ffe0a0','#fff'])+FIN+'</svg>';
  return fin(u,b);};

RS.street=function(u){var r=rng(201),i;
  var b=HEAD+'<defs>'+COM+'</defs><rect width="480" height="270" fill="url(#@sk)"/><circle cx="360" cy="140" r="140" fill="url(#@sn)"/>'
   +'<g filter="url(#@b)"><ellipse cx="120" cy="44" rx="100" ry="6" fill="url(#@cl)"/><ellipse cx="380" cy="64" rx="70" ry="6" fill="url(#@cl)"/></g>'
   +(function(){var s='',cols=['#c9553d','#e8b04a','#4f7a8a','#8a5a8a','#5a8a5a','#d98a6a'];for(i=0;i<5;i++){var x=i*100-10,h=110+((i*37)%40),c=cols[i%6];s+='<rect x="'+x+'" y="'+(160-h)+'" width="98" height="'+h+'" fill="'+c+'"/><rect x="'+x+'" y="'+(160-h)+'" width="98" height="8" fill="#000" opacity=".15"/>';for(var wy=0;wy<2;wy++)for(var wx=0;wx<3;wx++)s+='<rect x="'+(x+10+wx*28)+'" y="'+(160-h+18+wy*32)+'" width="18" height="22" fill="'+((wx+wy+i)%3?'#2a3346':'#ffd98a')+'"/>';s+='<path d="M'+(x+2)+' 122h94l-8 14h-78z" fill="'+['#fff','#d9534f','#fff','#2e6f95','#fff'][i]+'"/><path d="M'+(x+10)+' 122l-4 14M'+(x+30)+' 122l-4 14M'+(x+50)+' 122l-4 14M'+(x+70)+' 122l-4 14" stroke="#0003" stroke-width="2"/><rect x="'+(x+14)+'" y="138" width="70" height="22" fill="#2a2d32" opacity=".55"/><rect x="'+(x+14)+'" y="138" width="70" height="22" fill="#ffe0a0" opacity=".35"/>';}return s})()
   +'<rect x="0" y="160" width="480" height="28" fill="#cfc7b8"/><rect x="0" y="186" width="480" height="84" fill="#4a4a54"/><rect x="0" y="186" width="480" height="4" fill="#9a9488"/>'
   +'<g fill="#fff" opacity=".85">'+[0,1,2,3,4,5].map(function(k){return '<rect x="'+(20+k*82)+'" y="226" width="44" height="6" rx="2"/>'}).join('')+'</g>'
   +'<g transform="translate(60 160)"><rect x="-2" y="-84" width="4" height="84" fill="#2a2d32"/><rect x="-16" y="-110" width="32" height="30" rx="4" fill="#2e6f95"/><text x="0" y="-92" text-anchor="middle" font-family="Arial,sans-serif" font-weight="700" font-size="14" fill="#fff">BUS</text></g>'
   +'<g transform="translate(400 240)"><path d="M-60 0q4-30 36-32l16-16h50l18 16q30 2 34 32v8h-154z" fill="#e8b04a"/><rect x="-16" y="-44" width="22" height="14" fill="#bfe0f2"/><rect x="12" y="-44" width="22" height="14" fill="#bfe0f2"/><circle cx="-34" cy="8" r="12" fill="#222"/><circle cx="34" cy="8" r="12" fill="#222"/></g>'
   +'<g>'+[150,300].map(function(x){return '<rect x="'+(x-2)+'" y="86" width="4" height="76" fill="#1B2230"/><path d="M'+(x-9)+' 86h18l-4-14h-10z" fill="#1B2230"/>'+lamp(x,80,1.8)}).join('')+'</g>'
   +shad(210,176,50)+crowd([[210,178,1.9,'#e85d75'],[250,176,1.5,'#12B3A8'],[130,174,1.4,'#7C4DFF']])
   +bokeh(r,10,50,170,['#ffe0a0','#ffb86b'])+FIN+'</svg>';
  return fin(u,b);};

})();
