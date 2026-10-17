/* scn_c.js - cenas ilustradas: subway, park, pier (SVG semi-realista, deterministico) */
(function(){
window.RS = window.RS || {};
function rng(s){return function(){s=(s*16807)%2147483647;return (s-1)/2147483646;};}
function f(n){return Math.round(n*10)/10;}
var HEAD='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 270" width="100%" height="100%" style="width:100%;height:100%;display:block" preserveAspectRatio="xMidYMid slice" role="img" aria-hidden="true">';
function fin(u,b){return b.replace(/@/g,u+'-');}
function blobs(r,n,cx,cy,rx,ry,rmin,rmax,fill,a0,a1){
  var s='<g fill="'+fill+'">';
  for(var i=0;i<n;i++){var a=a0+(a1-a0)*r(),d=Math.sqrt(r());
    s+='<circle cx="'+f(cx+rx*d*Math.cos(a))+'" cy="'+f(cy+ry*d*Math.sin(a))+'" r="'+f(rmin+(rmax-rmin)*r())+'"/>';}
  return s+'</g>';
}
function tree(r,cx,cy,rx,ry,n,rmin,rmax,c1,c2,c3){
  return '<g filter="url(#@b)" opacity=".96">'+blobs(r,n,cx,cy,rx,ry,rmin,rmax,c1,0,6.28)+'</g>'
    +blobs(r,(n*1.1)|0,cx+rx*.03,cy-ry*.06,rx*.93,ry*.9,rmin*.6,rmax*.6,c2,-2.8,1.0)
    +'<g opacity=".85">'+blobs(r,(n*1.5)|0,cx+rx*.08,cy-ry*.1,rx*.97,ry*.97,rmin*.28,rmax*.36,c3,-1.9,0.5)+'</g>';
}
/* ============================ SUBWAY ============================ */
RS.subway=function(u){
  var ties='';
  for(var i=0;i<30;i++){var y=112+12*Math.pow(1.17,i);if(y>177)break;
    var hw=142*(y-112)/66+14,h=.8+(y-112)/66*3.4;
    ties+='<rect x="'+f(240-hw)+'" y="'+f(y)+'" width="'+f(hw*2)+'" height="'+f(h)+'"/>';}
  var seams='';
  for(var x=-300;x<=780;x+=60)seams+='M240 112L'+x+' 270';
  var tun='';
  for(var k=0;k<5;k++){tun+='<circle cx="'+(193+k*2)+'" cy="'+(78+k*5)+'" r="'+f(1.6-k*.2)+'"/><circle cx="'+(287-k*2)+'" cy="'+(78+k*5)+'" r="'+f(1.6-k*.2)+'"/>';}
  var b=HEAD+`<defs>
<pattern id="@tl" width="16" height="8" patternUnits="userSpaceOnUse"><rect width="16" height="8" fill="#eceee9"/><path d="M0 0H16M0 4H16M0 0V4M8 4V8" stroke="#aeb5b0" stroke-width=".55" fill="none"/><path d="M0 .6H16M0 4.6H16" stroke="#fff" stroke-width=".4" opacity=".7"/></pattern>
<pattern id="@dt" width="3" height="3" patternUnits="userSpaceOnUse"><rect width="3" height="3" fill="#d6ac28"/><circle cx="1.5" cy="1.5" r=".8" fill="#9a7a14"/></pattern>
<linearGradient id="@wl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0d1519" stop-opacity=".62"/><stop offset=".45" stop-color="#cfe6e8" stop-opacity=".08"/><stop offset="1" stop-color="#1a2326" stop-opacity=".3"/></linearGradient>
<linearGradient id="@wh" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#0a1013" stop-opacity=".5"/><stop offset=".25" stop-color="#000" stop-opacity="0"/><stop offset=".75" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#0a1013" stop-opacity=".5"/></linearGradient>
<radialGradient id="@tn" cx=".5" cy=".62" r=".6"><stop offset="0" stop-color="#05070a"/><stop offset=".6" stop-color="#0b1015"/><stop offset="1" stop-color="#1b232a"/></radialGradient>
<linearGradient id="@pit" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#14120f"/><stop offset="1" stop-color="#37322b"/></linearGradient>
<linearGradient id="@fl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8a9096"/><stop offset=".5" stop-color="#737980"/><stop offset="1" stop-color="#5f656c"/></linearGradient>
<linearGradient id="@co" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#2f383d"/><stop offset=".3" stop-color="#a3b0b5"/><stop offset=".62" stop-color="#6e7a80"/><stop offset="1" stop-color="#262e33"/></linearGradient>
<linearGradient id="@tr" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7b8388"/><stop offset=".35" stop-color="#c3c9cc"/><stop offset=".7" stop-color="#9aa2a7"/><stop offset="1" stop-color="#6c7378"/></linearGradient>
<linearGradient id="@gl" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2a3a48"/><stop offset=".5" stop-color="#0b1219"/><stop offset="1" stop-color="#16212b"/></linearGradient>
<linearGradient id="@hl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff4cf" stop-opacity=".6"/><stop offset="1" stop-color="#fff4cf" stop-opacity="0"/></linearGradient>
<linearGradient id="@mc" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#2f66b0"/><stop offset="1" stop-color="#1a3d70"/></linearGradient>
<linearGradient id="@st" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7d868b"/><stop offset=".4" stop-color="#e0e5e7"/><stop offset="1" stop-color="#6b7479"/></linearGradient>
<radialGradient id="@hg"><stop offset="0" stop-color="#fffbe6" stop-opacity=".95"/><stop offset=".35" stop-color="#fff0b8" stop-opacity=".45"/><stop offset="1" stop-color="#fff0b8" stop-opacity="0"/></radialGradient>
<radialGradient id="@vg" cx=".5" cy=".5" r=".75"><stop offset=".55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".5"/></radialGradient>
<filter id="@b" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="2.2"/></filter>
<filter id="@n" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" seed="4"/><feColorMatrix values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 .55 -.12"/></filter>
<clipPath id="@fc"><rect x="0" y="185" width="480" height="85"/></clipPath>
<clipPath id="@pc"><rect x="0" y="123" width="480" height="56"/></clipPath>
</defs>
<rect width="480" height="270" fill="#1b2227"/>
<rect y="0" width="480" height="124" fill="url(#@tl)"/>
<rect y="0" width="480" height="124" fill="url(#@wl)"/>
<rect y="0" width="480" height="22" fill="#232a30"/>
<path d="M0 22H480" stroke="#3b454c" stroke-width="2"/>
<rect y="56" width="480" height="6" fill="#1d7c47"/><rect y="56" width="480" height="1.2" fill="#49b374"/><rect y="62" width="480" height="1.4" fill="#0e4527"/>
<rect y="108" width="480" height="10" fill="#c9cfcb" opacity=".55"/><rect y="108" width="480" height="1" fill="#8d9692"/>
<g font-family="Helvetica,Arial,sans-serif" font-weight="bold">
<rect x="86" y="72" width="68" height="20" rx="1.5" fill="#15191c" stroke="#9aa3a8" stroke-width=".7"/>
<circle cx="99" cy="82" r="5.5" fill="#d93b30"/><text x="99" y="84.6" font-size="7" fill="#fff" text-anchor="middle">2</text>
<text x="127" y="86" font-size="11" fill="#fff" text-anchor="middle">14 St</text>
<rect x="326" y="72" width="68" height="20" rx="1.5" fill="#15191c" stroke="#9aa3a8" stroke-width=".7"/>
<text x="360" y="85" font-size="6.6" fill="#fff" text-anchor="middle">14 St - Union Sq</text>
</g>
<rect y="0" width="480" height="124" fill="url(#@wh)"/>
<rect y="117" width="480" height="7" fill="#868b91"/><rect y="122.4" width="480" height="1.6" fill="#c9a227"/>
<path d="M172 123V62Q172 20 240 20Q308 20 308 62V123Z" fill="#6b7277"/>
<path d="M172 123V62Q172 20 240 20Q308 20 308 62" fill="none" stroke="#9aa2a7" stroke-width="1.2" opacity=".6"/>
<path d="M181 123V62Q181 30 240 30Q299 30 299 62V123Z" fill="url(#@tn)"/>
<g fill="#cfe27a" opacity=".7">`+tun+`</g>
<path d="M211 122V56Q211 44 223 44H257Q269 44 269 56V122Z" fill="url(#@tr)"/>
<rect x="215" y="52" width="50" height="27" rx="3" fill="url(#@gl)"/>
<path d="M219 54L232 54L222 77L219 77Z" fill="#fff" opacity=".12"/>
<rect x="232" y="46.4" width="16" height="4" rx=".8" fill="#fff6d0"/><circle cx="240" cy="48.4" r="1.8" fill="#d93b30"/>
<rect x="214" y="104" width="52" height="14" fill="#3a4045"/><rect x="214" y="104" width="52" height="1.2" fill="#d5dadc" opacity=".6"/>
<path d="M240 79V104" stroke="#555e63" stroke-width="1"/>
<circle cx="221" cy="96" r="12" fill="url(#@hg)"/><circle cx="259" cy="96" r="12" fill="url(#@hg)"/>
<circle cx="221" cy="96" r="3.4" fill="#fffef2"/><circle cx="259" cy="96" r="3.4" fill="#fffef2"/>
<circle cx="230" cy="110" r="1.3" fill="#e6382d"/><circle cx="250" cy="110" r="1.3" fill="#e6382d"/>
<circle cx="240" cy="98" r="62" fill="url(#@hg)" opacity=".4"/>
<rect y="124" width="480" height="55" fill="url(#@pit)"/>
<g fill="#2b2622" opacity=".95">`+ties+`</g>
<g clip-path="url(#@pc)"><rect y="123" width="480" height="56" filter="url(#@n)" opacity=".8"/></g>
<path d="M98 179L216.7 123M382 179L263.3 123" stroke="#43474b" stroke-width="3.6"/>
<path d="M99.5 178L217 123M380.5 178L263 123" stroke="#cfd4d7" stroke-width=".9" opacity=".8"/>
<path d="M60 179L204 123M420 179L276 123" stroke="#2b2e31" stroke-width="2.4"/>
<path d="M222 123L258 123L440 179L40 179Z" fill="url(#@hl)" opacity=".75"/>
<path d="M0 178.5H480" stroke="#07090a" stroke-width="1.6"/>
<rect y="179" width="480" height="6.4" fill="url(#@dt)"/><rect y="179" width="480" height="1.4" fill="#f0cf5c" opacity=".7"/>
<rect y="185" width="480" height="85" fill="url(#@fl)"/>
<g clip-path="url(#@fc)">
<path d="`+seams+`" stroke="#12181c" stroke-opacity=".15" stroke-width=".6" fill="none"/>
<path d="M0 198H480M0 220H480M0 252H480" stroke="#12181c" stroke-opacity=".1" stroke-width=".6"/>
<ellipse cx="240" cy="226" rx="16" ry="38" fill="#e8f4ff" opacity=".1" filter="url(#@b)"/>
<ellipse cx="120" cy="222" rx="12" ry="34" fill="#e8f4ff" opacity=".09" filter="url(#@b)"/>
<ellipse cx="362" cy="222" rx="12" ry="34" fill="#e8f4ff" opacity=".09" filter="url(#@b)"/>
<rect y="185" width="480" height="85" filter="url(#@n)" opacity=".5"/>
<rect y="185" width="480" height="14" fill="#000" opacity=".12"/>
</g>
<ellipse cx="122" cy="206" rx="28" ry="4.5" fill="#000" opacity=".4" filter="url(#@b)"/>
<rect x="108" y="141" width="4" height="63" fill="#0e2243"/>
<rect x="104" y="140" width="34" height="63" rx="2" fill="url(#@mc)"/>
<rect x="104" y="140" width="34" height="9" rx="2" fill="#f1c230"/>
<text x="121" y="147" font-family="Helvetica,Arial,sans-serif" font-weight="bold" font-size="5.6" fill="#1a1a1a" text-anchor="middle">MetroCard</text>
<rect x="109" y="153" width="24" height="17" rx="1" fill="#09222f" stroke="#0a1620" stroke-width=".8"/>
<rect x="110.5" y="154.5" width="21" height="14" fill="#4fb6d8" opacity=".75"/><rect x="110.5" y="154.5" width="21" height="5" fill="#bdeeff" opacity=".45"/>
<g fill="#cfd6da"><rect x="110" y="175" width="4" height="3"/><rect x="116" y="175" width="4" height="3"/><rect x="122" y="175" width="4" height="3"/><rect x="110" y="180" width="4" height="3"/><rect x="116" y="180" width="4" height="3"/><rect x="122" y="180" width="4" height="3"/></g>
<rect x="128" y="175" width="6" height="8" fill="#e5c13a"/>
<rect x="110" y="188" width="22" height="3" fill="#06090c"/><rect x="110" y="194" width="22" height="5" rx="1" fill="#10161b"/>
<rect x="104" y="140" width="3" height="63" fill="#fff" opacity=".13"/>
<ellipse cx="366" cy="204" rx="34" ry="4" fill="#000" opacity=".4" filter="url(#@b)"/>
<g>
<rect x="342" y="172" width="9" height="32" rx="2" fill="url(#@st)"/><rect x="364" y="172" width="9" height="32" rx="2" fill="url(#@st)"/><rect x="386" y="172" width="9" height="32" rx="2" fill="url(#@st)"/>
<rect x="344.5" y="176" width="4" height="3" fill="#3ddc84"/><rect x="366.5" y="176" width="4" height="3" fill="#e44"/><rect x="388.5" y="176" width="4" height="3" fill="#3ddc84"/>
<path d="M351 186L364 191M373 186L386 191" stroke="#aeb7bb" stroke-width="1.4"/><path d="M351 186L364 181M373 186L386 181" stroke="#8f989d" stroke-width="1.2"/>
</g>
<g><ellipse cx="70" cy="207" rx="22" ry="4" fill="#000" opacity=".45" filter="url(#@b)"/><rect x="62" y="-4" width="16" height="210" fill="url(#@co)"/>
<rect x="59" y="198" width="22" height="8" fill="#1d2428"/><rect x="62" y="110" width="16" height="2" fill="#1b2227" opacity=".5"/><rect x="62" y="190" width="16" height="2" fill="#1b2227" opacity=".4"/>
<ellipse cx="410" cy="207" rx="22" ry="4" fill="#000" opacity=".45" filter="url(#@b)"/><rect x="402" y="-4" width="16" height="210" fill="url(#@co)"/>
<rect x="399" y="198" width="22" height="8" fill="#1d2428"/><rect x="402" y="110" width="16" height="2" fill="#1b2227" opacity=".5"/><rect x="402" y="190" width="16" height="2" fill="#1b2227" opacity=".4"/></g>
<g fill="#f2fbff">
<rect x="96" y="6" width="68" height="4" rx="1"/><rect x="316" y="6" width="68" height="4" rx="1"/>
<rect x="150" y="15" width="42" height="3" rx="1"/><rect x="288" y="15" width="42" height="3" rx="1"/><rect x="218" y="21" width="44" height="2" rx="1"/></g>
<g fill="#d8f2ff" opacity=".5" filter="url(#@b)"><rect x="96" y="6" width="68" height="6"/><rect x="316" y="6" width="68" height="6"/><rect x="150" y="14" width="42" height="5"/><rect x="288" y="14" width="42" height="5"/></g>
<path d="M326 22V34M384 22V34" stroke="#2a3136" stroke-width="1.2"/>
<rect x="316" y="34" width="80" height="26" rx="1.5" fill="#0a0c0e" stroke="#4a5258" stroke-width=".8"/>
<rect x="318" y="36" width="76" height="22" fill="#ffa81f" opacity=".16" filter="url(#@b)"/>
<g font-family="Helvetica,Arial,sans-serif" font-weight="bold"><circle cx="327" cy="42.5" r="4.4" fill="#d93b30"/><text x="327" y="45" font-size="6" fill="#fff" text-anchor="middle">2</text>
<text x="336" y="45.4" font-size="8" fill="#ffb02e">Uptown</text><text x="322" y="56" font-size="8" fill="#ffb02e">2 min</text></g>
<rect width="480" height="270" fill="url(#@vg)"/>
</svg>`;
  return fin(u,b);
};

/* ============================ PARK ============================ */
RS.park=function(u){
  var r=rng(7),r2=rng(31),r3=rng(53);
  var bld='',bs=[[128,14,30],[142,18,46],[160,12,36],[172,20,58],[192,14,40],[206,22,30],[230,16,52],[246,12,66],[262,18,40],[280,22,50],[302,12,34],[316,18,28],[110,16,26],[334,16,24]];
  for(var i=0;i<bs.length;i++)bld+='<rect x="'+bs[i][0]+'" y="'+(114-bs[i][2])+'" width="'+bs[i][1]+'" height="'+bs[i][2]+'"/>';
  bld+='<rect x="174" y="48" width="4" height="10"/><rect x="248" y="42" width="3" height="26"/>';
  var farT=blobs(r,64,240,108,270,7,5,10,'#6c7c52',0,6.28)+blobs(r,34,240,106,260,5,3,7,'#8c9a58',0,6.28);
  var glint='';
  for(var g=0;g<16;g++){var y=117+g*3.5,cx=334+Math.sin(g*2.3)*9,w=7+g*1.7;
    glint+='<path d="M'+f(cx-w)+' '+f(y)+'H'+f(cx+w)+'" stroke-opacity="'+f(.85-g*.045)+'"/>';}
  var rip='';
  for(var q=0;q<46;q++){var y2=118+Math.pow(r2(),1.3)*50,x2=r2()*520-20,l=6+r2()*16;
    rip+='<path d="M'+f(x2)+' '+f(y2)+'h'+f(l)+'"/>';}
  var dap='';
  for(var d=0;d<22;d++){dap+='<ellipse cx="'+f(120+r3()*340)+'" cy="'+f(200+r3()*60)+'" rx="'+f(5+r3()*10)+'" ry="'+f(1.5+r3()*2.5)+'"/>';}
  var reeds='';
  for(var e=0;e<26;e++){var x3=20+e*17+r3()*8,yb=168+Math.sin(x3*.02)*2;reeds+='<path d="M'+f(x3)+' '+f(yb+1)+'q'+f(r3()*3-1.5)+' -'+f(4+r3()*5)+' '+f(r3()*4-2)+' -'+f(7+r3()*5)+'"/>';}
  var b=HEAD+`<defs>
<linearGradient id="@sk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7f9db7"/><stop offset=".5" stop-color="#f0d5a6"/><stop offset="1" stop-color="#f6b66d"/></linearGradient>
<radialGradient id="@sn"><stop offset="0" stop-color="#fff7d6"/><stop offset=".25" stop-color="#ffe7a0" stop-opacity=".8"/><stop offset=".6" stop-color="#ffc878" stop-opacity=".3"/><stop offset="1" stop-color="#ffc878" stop-opacity="0"/></radialGradient>
<linearGradient id="@hz" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f6c58a" stop-opacity="0"/><stop offset="1" stop-color="#f6c58a" stop-opacity=".8"/></linearGradient>
<linearGradient id="@bd" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c7a99d"/><stop offset="1" stop-color="#d9b99d"/></linearGradient>
<linearGradient id="@lk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f4c486"/><stop offset=".35" stop-color="#d5bd8f"/><stop offset=".75" stop-color="#8f9d7c"/><stop offset="1" stop-color="#5f7662"/></linearGradient>
<linearGradient id="@gr" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#b9ab55"/><stop offset=".4" stop-color="#8a9944"/><stop offset="1" stop-color="#5e7c37"/></linearGradient>
<linearGradient id="@pt" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d4be98"/><stop offset=".5" stop-color="#c3ad88"/><stop offset="1" stop-color="#ad9877"/></linearGradient>
<linearGradient id="@tk" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#2a211b"/><stop offset=".6" stop-color="#4a3a2c"/><stop offset="1" stop-color="#9a7544"/></linearGradient>
<linearGradient id="@ry" gradientUnits="userSpaceOnUse" x1="332" y1="100" x2="210" y2="250"><stop offset="0" stop-color="#fff0b4" stop-opacity=".5"/><stop offset="1" stop-color="#fff0b4" stop-opacity="0"/></linearGradient>
<radialGradient id="@lm"><stop offset="0" stop-color="#ffe9a0" stop-opacity=".85"/><stop offset="1" stop-color="#ffe9a0" stop-opacity="0"/></radialGradient>
<radialGradient id="@vg" cx=".5" cy=".5" r=".78"><stop offset=".6" stop-color="#1a1608" stop-opacity="0"/><stop offset="1" stop-color="#1a1608" stop-opacity=".42"/></radialGradient>
<filter id="@b" x="-20%" y="-30%" width="140%" height="160%"><feGaussianBlur stdDeviation="1.6"/></filter>
<filter id="@n" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="9"/><feColorMatrix values="0 0 0 0 .2 0 0 0 0 .15 0 0 0 0 .08 0 0 0 .7 -.18"/></filter>
<g id="@ft">`+farT+`</g>
<g id="@bg" fill="url(#@bd)">`+bld+`</g>
<clipPath id="@pc"><path d="M150 270C165 232 260 205 350 190C400 178 450 174 490 172L490 190C450 192 410 205 390 222C370 240 355 255 345 270Z"/></clipPath>
<clipPath id="@lc"><rect x="0" y="114" width="480" height="60"/></clipPath>
</defs>
<rect width="480" height="130" fill="url(#@sk)"/>
<ellipse cx="270" cy="30" rx="150" ry="5" fill="#fff0cf" opacity=".5" filter="url(#@b)"/><ellipse cx="110" cy="52" rx="90" ry="4" fill="#fff0cf" opacity=".4" filter="url(#@b)"/>
<circle cx="332" cy="102" r="120" fill="url(#@sn)"/><circle cx="332" cy="102" r="8" fill="#fffbe6"/>
<g filter="url(#@b)" opacity=".92"><use href="#@bg"/></g>
<rect y="60" width="480" height="54" fill="url(#@hz)"/>
<g filter="url(#@b)"><use href="#@ft"/></g>
<rect y="106" width="480" height="9" fill="#74835a"/>
<rect y="114" width="480" height="62" fill="url(#@lk)"/>
<g clip-path="url(#@lc)">
<g transform="translate(0 228) scale(1 -1)" filter="url(#@b)" opacity=".5"><use href="#@ft"/></g>
<g transform="translate(0 228) scale(1 -1)" filter="url(#@b)" opacity=".28"><use href="#@bg"/></g>
<ellipse cx="334" cy="124" rx="70" ry="14" fill="#ffe7a8" opacity=".5" filter="url(#@b)"/>
<g stroke="#fff3c4" stroke-width="1.1" fill="none">`+glint+`</g>
<g stroke="#fff6dc" stroke-opacity=".3" stroke-width=".6">`+rip+`</g>
<rect y="150" width="480" height="26" fill="#2e4a3a" opacity=".22"/>
</g>
<path d="M-10 177C70 166 150 164 240 168S400 168 490 174L490 270L-10 270Z" fill="url(#@gr)"/>
<path d="M-10 177C70 166 150 164 240 168S400 168 490 174" fill="none" stroke="#4c5a34" stroke-width="2.2" opacity=".8"/>
<g stroke="#7c8b3e" stroke-width=".9" fill="none" opacity=".85">`+reeds+`</g>
<rect y="176" width="480" height="94" filter="url(#@n)" opacity=".45"/>
<ellipse cx="90" cy="188" rx="86" ry="7" fill="#1d3a1c" opacity=".42" filter="url(#@b)"/>
<ellipse cx="400" cy="186" rx="80" ry="6" fill="#1d3a1c" opacity=".38" filter="url(#@b)"/>
<ellipse cx="190" cy="176" rx="30" ry="3" fill="#1d3a1c" opacity=".35" filter="url(#@b)"/>
<path d="M186 168L188 142L192 130L195 144L197 169Z" fill="url(#@tk)"/>
`+tree(r,190,128,30,24,30,5,9,'#35502d','#53723a','#a8b650')+`
<path d="M110 180L113 118L119 92L125 118L130 181Z" fill="url(#@tk)"/>
`+tree(r,114,80,62,50,70,7,14,'#2a4427','#486a2e','#a9b84a')+`
<path d="M393 178L396 120L402 96L408 120L412 177Z" fill="url(#@tk)"/>
`+tree(r,408,68,72,56,76,7,14,'#294326','#486a2c','#b3c04c')+`
<path d="M150 270C165 232 260 205 350 190C400 178 450 174 490 172L490 190C450 192 410 205 390 222C370 240 355 255 345 270Z" fill="url(#@pt)"/>
<g clip-path="url(#@pc)"><rect y="170" width="480" height="100" filter="url(#@n)" opacity=".7"/>
<path d="M205 270C215 238 290 210 360 196C410 186 450 182 490 180" stroke="#8b7753" stroke-opacity=".22" stroke-width="1" fill="none"/>
<path d="M270 270C282 245 330 222 380 208C420 198 450 192 490 190" stroke="#8b7753" stroke-opacity=".18" stroke-width="1" fill="none"/>
<g fill="#fff0a8" opacity=".3">`+dap+`</g></g>
<path d="M150 270C165 232 260 205 350 190C400 178 450 174 490 172" fill="none" stroke="#8d7c5b" stroke-width="2.4"/>
<path d="M150 270C165 232 260 205 350 190C400 178 450 174 490 172" fill="none" stroke="#ecdcb6" stroke-width=".8" opacity=".7" transform="translate(0 -1.5)"/>
<path d="M490 190C450 192 410 205 390 222C370 240 355 255 345 270" fill="none" stroke="#8d7c5b" stroke-width="2"/>
<ellipse cx="318" cy="197" rx="34" ry="4" fill="#2a2210" opacity=".4" filter="url(#@b)"/>
<g id="@bn"><path d="M292 196V184M346 196V184M296 196V184M342 196V184" stroke="#26372c" stroke-width="2.4"/>
<rect x="291" y="168" width="58" height="3" rx="1" fill="#a9763a"/><rect x="291" y="173" width="58" height="3" rx="1" fill="#9a6a33"/><rect x="291" y="178" width="58" height="3" rx="1" fill="#a9763a"/>
<rect x="290" y="183" width="60" height="3.6" rx="1" fill="#b5803f"/><rect x="290" y="183" width="60" height="1" fill="#e0b777" opacity=".7"/>
<rect x="289" y="166" width="3" height="19" fill="#26372c"/><rect x="348" y="166" width="3" height="19" fill="#26372c"/>
<rect x="289" y="175" width="62" height="2" fill="#26372c" opacity=".0"/>
<rect x="291" y="168" width="58" height="1" fill="#f0c98a" opacity=".6"/></g>
<g><ellipse cx="364" cy="193" rx="9" ry="2" fill="#2a2210" opacity=".4"/>
<path d="M362.4 192L363 104H365L365.6 192Z" fill="#1c2420"/><rect x="359" y="186" width="10" height="7" rx="1" fill="#1c2420"/>
<circle cx="364" cy="100" r="15" fill="url(#@lm)"/><path d="M360 106L359 94L364 89L369 94L368 106Z" fill="#ffe9a0" stroke="#1c2420" stroke-width="1.6"/><path d="M358 90L364 84L370 90Z" fill="#1c2420"/>
<ellipse cx="156" cy="182" rx="6" ry="1.5" fill="#2a2210" opacity=".4"/>
<path d="M155.2 181L155.6 116H157.2L157.6 181Z" fill="#1c2420"/><circle cx="156.4" cy="113" r="11" fill="url(#@lm)"/><path d="M153.5 118L153 109L156.4 105L160 109L159.3 118Z" fill="#ffe9a0" stroke="#1c2420" stroke-width="1.2"/><path d="M152.5 106L156.4 101L160.5 106Z" fill="#1c2420"/></g>
<g><path d="M-30 -10L-30 40Q20 60 70 40Q110 24 150 -10Z" fill="#1d3220"/></g>
`+tree(r,10,-8,150,70,64,9,16,'#1a2c1d','#2c4727','#8a9b3a')+tree(r,470,-10,130,78,60,9,16,'#1b2f1e','#2f4d28','#a0b03e')+`
<path d="M-12 44Q40 70 100 44" fill="none"/>
<path d="M332 100L128 270L216 270Z" fill="url(#@ry)" opacity=".5"/>
<path d="M332 100L228 270L292 270Z" fill="url(#@ry)" opacity=".4"/>
<path d="M332 100L300 270L372 270Z" fill="url(#@ry)" opacity=".28"/>
<path d="M332 100L24 250L60 270Z" fill="url(#@ry)" opacity=".4"/>
<rect width="480" height="270" fill="url(#@vg)"/>
</svg>`;
  return fin(u,b);
};

/* ============================ PIER ============================ */
RS.pier=function(u){
  var r=rng(11),r2=rng(23);
  function hw(y){return .857*(y-148);}
  var K=350,A='',B='',C='',gaps='';
  var prev=null;
  for(var k=0;k<48;k++){var Z=2.7+k*.4,y=148+K/Z;
    if(prev!==null){var yb=prev,ya=y;
      var q='M'+f(240-hw(yb))+' '+f(yb)+'L'+f(240+hw(yb))+' '+f(yb)+'L'+f(240+hw(ya))+' '+f(ya)+'L'+f(240-hw(ya))+' '+f(ya)+'Z';
      if(k%3===0)A+=q;else if(k%3===1)B+=q;else C+=q;
      gaps+='M'+f(240-hw(ya))+' '+f(ya)+'L'+f(240+hw(ya))+' '+f(ya);}
    prev=y;}
  var rip='',rip2='';
  for(var i=0;i<64;i++){var y2=150+Math.pow(r(),1.7)*118,x2=r()*500-10,l=3+(y2-148)*.12+r()*5,sw=f(.45+(y2-148)/190);
    var s='<path d="M'+f(x2)+' '+f(y2)+'h'+f(l)+'" stroke-width="'+sw+'"/>';
    if(i%2)rip+=s;else rip2+=s;}
  var sun='';
  for(var j=0;j<24;j++){var yy=150+j*2.8,w=8+j*1.4+r2()*6,cx=172+Math.sin(j*1.9)*6;
    sun+='<path d="M'+f(cx-w)+' '+f(yy)+'H'+f(cx+w)+'" stroke-opacity="'+f(.8-j*.028)+'"/>';}
  var fs=blobs(r,70,240,141,270,6,3,7,'#4a5a4c',0,6.28)+blobs(r,30,240,138,250,4,2.5,5,'#5f6f55',0,6.28)
    +blobs(r,16,92,138,22,6,4,8,'#3f4f43',0,6.28)+blobs(r,18,396,138,26,6,4,9,'#3f4f43',0,6.28);
  var hs=[[96,9,5],[110,8,4.4],[270,9,5],[286,10,5.5],[302,7,4.5],[352,9,5],[368,8,4.6],[388,9,5]],hh='';
  for(var h=0;h<hs.length;h++){var x=hs[h][0],w=hs[h][1],t=hs[h][2];
    hh+='<rect x="'+x+'" y="'+f(144-t)+'" width="'+w+'" height="'+t+'" fill="'+(h%2?'#f1dfc8':'#e7ccb0')+'"/><path d="M'+(x-1)+' '+f(144-t)+'L'+f(x+w/2)+' '+f(144-t-4)+'L'+(x+w+1)+' '+f(144-t)+'Z" fill="'+(h%3?'#8a5b52':'#6a5560')+'"/><rect x="'+f(x+w/2-1)+'" y="'+f(145-t*.7)+'" width="1.6" height="1.6" fill="#ffd27a"/>';}
  var posts=[[5,218,60,50,10],[8,191.8,37.6,31,6.2],[12,177.2,25,20.8,4.2],[17,168.6,17.6,14.7,2.9]];
  var postsS='',ropeL='',ropeR='';
  for(var p=0;p<posts.length;p++){var P=posts[p],yb2=P[1],ph=P[3],pw=P[4],hx=P[2];
    for(var sd=-1;sd<=1;sd+=2){var px=240+sd*hx;
      postsS+='<path d="M'+f(px)+' '+f(yb2)+'l'+f(pw*2.4+sd*0)+' '+f(pw*.9)+'l'+f(pw*.9)+' '+f(-pw*.2)+'l'+f(-pw*.5)+' '+f(-pw*.8)+'Z" fill="#2a1b10" opacity=".28"/>'
      +'<rect x="'+f(px-pw/2)+'" y="'+f(yb2-ph)+'" width="'+pw+'" height="'+ph+'" rx="'+f(pw*.4)+'" fill="url(#@pl)"/>'
      +'<ellipse cx="'+px+'" cy="'+f(yb2-ph)+'" rx="'+f(pw/2)+'" ry="'+f(pw*.22)+'" fill="#9b7b55"/>'
      +'<ellipse cx="'+px+'" cy="'+f(yb2-ph*.82)+'" rx="'+f(pw*.62)+'" ry="'+f(pw*.2)+'" fill="none" stroke="#d6bf92" stroke-width="'+f(Math.max(.7,pw*.2))+'"/>';}
    if(p<posts.length-1){var N=posts[p+1];
      for(var sd2=-1;sd2<=1;sd2+=2){var x1=240+sd2*P[2],y1=P[1]-P[3]*.82,x2b=240+sd2*N[2],y2b=N[1]-N[3]*.82,sag=f(P[3]*.28);
        var d='M'+f(x1)+' '+f(y1)+'Q'+f((x1+x2b)/2)+' '+f((y1+y2b)/2+ +sag)+' '+f(x2b)+' '+f(y2b);
        ropeL+='<path d="'+d+'" stroke-width="'+f(Math.max(.8,P[4]*.3))+'"/>';}}}
  var b=HEAD+`<defs>
<linearGradient id="@sk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5c7db0"/><stop offset=".3" stop-color="#a9a6c6"/><stop offset=".62" stop-color="#f0b58b"/><stop offset="1" stop-color="#fcd8a0"/></linearGradient>
<radialGradient id="@sn"><stop offset="0" stop-color="#fffbe2"/><stop offset=".2" stop-color="#ffe6a0" stop-opacity=".85"/><stop offset=".55" stop-color="#ffbf80" stop-opacity=".3"/><stop offset="1" stop-color="#ffbf80" stop-opacity="0"/></radialGradient>
<linearGradient id="@cl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff2dc"/><stop offset="1" stop-color="#e79a8a"/></linearGradient>
<linearGradient id="@wt" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f6cd9b"/><stop offset=".2" stop-color="#e0ab93"/><stop offset=".45" stop-color="#a595a8"/><stop offset=".75" stop-color="#627998"/><stop offset="1" stop-color="#425b7a"/></linearGradient>
<linearGradient id="@pl" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#b08a5e"/><stop offset=".5" stop-color="#7a5b3b"/><stop offset="1" stop-color="#3f2c1c"/></linearGradient>
<linearGradient id="@dk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffd9a0" stop-opacity=".55"/><stop offset=".5" stop-color="#ffc58a" stop-opacity=".12"/><stop offset="1" stop-color="#2a1a10" stop-opacity=".18"/></linearGradient>
<linearGradient id="@hl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9a97b2" stop-opacity=".9"/><stop offset="1" stop-color="#b3a2a8" stop-opacity=".6"/></linearGradient>
<radialGradient id="@vg" cx=".5" cy=".55" r=".8"><stop offset=".6" stop-color="#0c1220" stop-opacity="0"/><stop offset="1" stop-color="#0c1220" stop-opacity=".4"/></radialGradient>
<filter id="@b" x="-20%" y="-40%" width="140%" height="180%"><feGaussianBlur stdDeviation="1.5"/></filter>
<filter id="@n" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".03 .8" numOctaves="2" seed="6"/><feColorMatrix values="0 0 0 0 .12 0 0 0 0 .07 0 0 0 0 .03 1.5 0 0 0 -.55"/></filter>
<g id="@fs"><path d="M-10 146C60 130 110 138 170 134S260 128 330 136S440 128 490 140V148H-10Z" fill="url(#@hl)"/>`+hh+fs+`<rect x="-10" y="143" width="500" height="5" fill="#3b4a40"/></g>
<clipPath id="@dc"><path d="M`+f(240-hw(165))+` 165L`+f(240+hw(165))+` 165L`+f(240+hw(280))+` 280L`+f(240-hw(280))+` 280Z"/></clipPath>
</defs>
<rect width="480" height="150" fill="url(#@sk)"/>
<circle cx="172" cy="136" r="110" fill="url(#@sn)"/><circle cx="172" cy="137" r="9" fill="#fffbe6"/>
<g filter="url(#@b)">
<ellipse cx="300" cy="40" rx="110" ry="6" fill="#8d8fb8" opacity=".5"/><ellipse cx="80" cy="30" rx="80" ry="5" fill="#8d8fb8" opacity=".45"/>
<ellipse cx="320" cy="76" rx="90" ry="9" fill="url(#@cl)"/><ellipse cx="370" cy="68" rx="50" ry="7" fill="url(#@cl)"/><ellipse cx="140" cy="86" rx="100" ry="8" fill="url(#@cl)"/>
<ellipse cx="60" cy="68" rx="60" ry="6" fill="url(#@cl)"/><ellipse cx="220" cy="106" rx="120" ry="6" fill="#f4a876" opacity=".8"/><ellipse cx="400" cy="108" rx="80" ry="5" fill="#f5b184" opacity=".8"/>
<ellipse cx="240" cy="54" rx="70" ry="5" fill="url(#@cl)" opacity=".8"/><ellipse cx="430" cy="48" rx="50" ry="5" fill="url(#@cl)" opacity=".8"/>
<ellipse cx="200" cy="120" rx="60" ry="4" fill="#ffd9a0" opacity=".8"/></g>
<use href="#@fs"/>
<rect y="148" width="480" height="122" fill="url(#@wt)"/>
<g clip-path="url(#@dc)" opacity="0"></g>
<g filter="url(#@b)" opacity=".42"><g transform="translate(0 295) scale(1 -1)"><use href="#@fs"/></g></g>
<rect y="148" width="480" height="3" fill="#fbe0b3" opacity=".6" filter="url(#@b)"/>
<ellipse cx="172" cy="152" rx="100" ry="22" fill="#ffe3a8" opacity=".5" filter="url(#@b)"/>
<g stroke="#fff3c6" stroke-width="1.1" fill="none">`+sun+`</g>
<g stroke="#fff0d6" stroke-opacity=".42" fill="none">`+rip+`</g><g stroke="#2d3f66" stroke-opacity=".28" fill="none">`+rip2+`</g>
<path d="M341 149.6H347L346 151.4H342Z" fill="#3a3a44"/><path d="M344 149.2V135.5L352 148.6Z" fill="#fff0dc"/><path d="M343 149V138L336 148.4Z" fill="#f6d9bd"/><path d="M335 152.4H352" stroke="#fff0dc" stroke-opacity=".4" stroke-width="1.2"/>
<path d="M`+f(240-hw(165)-3)+` 165L135 280M`+f(240+hw(165)+3)+` 165L345 280" stroke="#142238" stroke-width="5" opacity=".42" filter="url(#@b)"/>
<path d="M`+f(240-hw(165))+` 165L`+f(240+hw(165))+` 165L`+f(240+hw(280))+` 280L`+f(240-hw(280))+` 280Z" fill="#6f5338"/>
<g clip-path="url(#@dc)">
<path d="`+A+`" fill="#8f7050"/><path d="`+B+`" fill="#826346"/><path d="`+C+`" fill="#997b5a"/>
<path d="`+gaps+`" stroke="#24160c" stroke-opacity=".5" stroke-width=".7" fill="none"/>
<rect y="150" width="480" height="130" filter="url(#@n)" opacity=".55"/>
<rect y="160" width="480" height="120" fill="url(#@dk)"/>
<path d="M`+f(240-hw(165))+` 165L135 280M`+f(240+hw(165))+` 165L345 280" stroke="#f1d3a0" stroke-opacity=".5" stroke-width="2" fill="none"/>
</g>
<g>`+postsS+`</g>
<g fill="none" stroke="#5a4630" stroke-opacity=".6">`+ropeL+`</g>
<g fill="none" stroke="#d9c496">`+ropeL+`</g>
<g transform="translate(277.6 173.5)"><circle r="5.2" fill="none" stroke="#f3efe6" stroke-width="3.2"/><circle r="5.2" fill="none" stroke="#d63a2e" stroke-width="3.2" stroke-dasharray="4.1 4.1"/></g>
<rect width="480" height="270" fill="url(#@vg)"/>
</svg>`;
  return fin(u,b);
};

/* ============================ LAKE ============================ */
RS.lake=function(u){
  var r=rng(41),r2=rng(77);
  var H=110,rip='',rip2='';
  for(var i=0;i<90;i++){var t=Math.pow(r(),1.6),y=H+3+t*157,x=r()*540-30,l=3+t*34+r()*6,sw=f(.4+t*1.1);
    var q='<path d="M'+f(x)+' '+f(y)+'h'+f(l)+'" stroke-width="'+sw+'"/>';
    if(i%2)rip+=q;else rip2+=q;}
  var sun='';
  for(var j=0;j<26;j++){var yy=H+2+j*2.6,w=7+j*1.5+r2()*6,cx=300+Math.sin(j*1.9)*7;
    sun+='<path d="M'+f(cx-w)+' '+f(yy)+'H'+f(cx+w)+'" stroke-opacity="'+f(.8-j*.028)+'"/>';}
  var fs=blobs(r,70,240,104,270,6,3,7,'#4a5a4c',0,6.28)+blobs(r,30,240,101,250,4,2.5,5,'#5f6f55',0,6.28)
    +blobs(r,18,60,100,40,8,4,9,'#3f4f43',0,6.28)+blobs(r,18,420,100,40,8,4,9,'#3f4f43',0,6.28);
  var hs=[[150,9,5],[164,8,4.4],[212,9,5],[226,10,5.5],[360,9,5],[374,8,4.6],[392,9,5]],hh='';
  for(var h=0;h<hs.length;h++){var x=hs[h][0],w=hs[h][1],t=hs[h][2];
    hh+='<rect x="'+x+'" y="'+f(106-t)+'" width="'+w+'" height="'+t+'" fill="'+(h%2?'#f1dfc8':'#e7ccb0')+'"/><path d="M'+(x-1)+' '+f(106-t)+'L'+f(x+w/2)+' '+f(106-t-4)+'L'+(x+w+1)+' '+f(106-t)+'Z" fill="'+(h%3?'#8a5b52':'#6a5560')+'"/><rect x="'+f(x+w/2-1)+'" y="'+f(107-t*.7)+'" width="1.6" height="1.6" fill="#ffd27a"/>';}
  var planks='';
  for(var k=0;k<9;k++){var yk=124+k*3.1;planks+='M-10 '+f(yk)+'L'+f(108+k*.5)+' '+f(yk+k*.35);}
  var reeds='';
  for(var e=0;e<44;e++){var left=e<22,xr=left?(-6+e*3.2+r2()*3):(448+(e-22)*2.9+r2()*3),yb=left?268:270,hgt=26+r2()*30,lean=(r2()-.5)*10;
    reeds+='<path d="M'+f(xr)+' '+yb+'q'+f(lean*.3)+' -'+f(hgt*.5)+' '+f(lean)+' -'+f(hgt)+'" stroke="'+(e%3?'#4f5d2c':'#6d7a38')+'"/>';}
  var stones='';
  var st=[[18,262,16,6],[40,266,10,4],[438,264,18,6],[462,262,12,5],[420,268,9,3.5]];
  for(var m=0;m<st.length;m++)stones+='<ellipse cx="'+st[m][0]+'" cy="'+st[m][1]+'" rx="'+st[m][2]+'" ry="'+st[m][3]+'"/>';
  var b=HEAD+`<defs>
<linearGradient id="@sk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5c7db0"/><stop offset=".3" stop-color="#a9a6c6"/><stop offset=".62" stop-color="#f0b58b"/><stop offset="1" stop-color="#fcd8a0"/></linearGradient>
<radialGradient id="@sn"><stop offset="0" stop-color="#fffbe2"/><stop offset=".2" stop-color="#ffe6a0" stop-opacity=".85"/><stop offset=".55" stop-color="#ffbf80" stop-opacity=".3"/><stop offset="1" stop-color="#ffbf80" stop-opacity="0"/></radialGradient>
<linearGradient id="@cl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff2dc"/><stop offset="1" stop-color="#e79a8a"/></linearGradient>
<linearGradient id="@wt" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f6cd9b"/><stop offset=".18" stop-color="#e0ab93"/><stop offset=".42" stop-color="#a595a8"/><stop offset=".75" stop-color="#627998"/><stop offset="1" stop-color="#4a6482"/></linearGradient>
<linearGradient id="@hl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7f809c" stop-opacity=".95"/><stop offset="1" stop-color="#98899c" stop-opacity=".8"/></linearGradient>
<linearGradient id="@dk" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8d6e4c"/><stop offset="1" stop-color="#a98559"/></linearGradient>
<linearGradient id="@pl" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#b08a5e"/><stop offset=".5" stop-color="#7a5b3b"/><stop offset="1" stop-color="#3f2c1c"/></linearGradient>
<radialGradient id="@vg" cx=".5" cy=".55" r=".8"><stop offset=".6" stop-color="#0c1220" stop-opacity="0"/><stop offset="1" stop-color="#0c1220" stop-opacity=".38"/></radialGradient>
<filter id="@b" x="-20%" y="-40%" width="140%" height="180%"><feGaussianBlur stdDeviation="1.5"/></filter>
<g id="@fs"><path d="M-10 108C60 94 110 102 170 98S260 92 330 100S440 92 490 104V112H-10Z" fill="url(#@hl)"/>`+hh+fs+`<rect x="-10" y="107" width="500" height="5" fill="#3b4a40"/></g>
</defs>
<rect width="480" height="114" fill="url(#@sk)"/>
<circle cx="300" cy="100" r="105" fill="url(#@sn)"/><circle cx="300" cy="101" r="9" fill="#fffbe6"/>
<g filter="url(#@b)">
<ellipse cx="300" cy="30" rx="110" ry="6" fill="#8d8fb8" opacity=".5"/><ellipse cx="90" cy="24" rx="80" ry="5" fill="#8d8fb8" opacity=".45"/>
<ellipse cx="150" cy="56" rx="100" ry="8" fill="url(#@cl)"/><ellipse cx="370" cy="48" rx="70" ry="7" fill="url(#@cl)"/><ellipse cx="60" cy="48" rx="60" ry="6" fill="url(#@cl)"/>
<ellipse cx="220" cy="82" rx="120" ry="5" fill="#f4a876" opacity=".8"/><ellipse cx="420" cy="86" rx="70" ry="5" fill="#f5b184" opacity=".8"/></g>
<use href="#@fs"/>
<rect y="112" width="480" height="158" fill="url(#@wt)"/>
<g filter="url(#@b)" opacity=".42"><g transform="translate(0 224) scale(1 -1)"><use href="#@fs"/></g></g>
<rect y="112" width="480" height="3" fill="#fbe0b3" opacity=".6" filter="url(#@b)"/>
<ellipse cx="300" cy="116" rx="110" ry="20" fill="#ffe3a8" opacity=".5" filter="url(#@b)"/>
<g stroke="#fff3c6" stroke-width="1.1" fill="none">`+sun+`</g>
<g stroke="#fff0d6" stroke-opacity=".4" fill="none">`+rip+`</g><g stroke="#2d3f66" stroke-opacity=".26" fill="none">`+rip2+`</g>
<path d="M-10 154L112 150L116 160L-10 164Z" fill="#142238" opacity=".4" filter="url(#@b)"/>
<path d="M92 152V176M30 156V182" stroke="#3a2a1c" stroke-width="5"/>
<path d="M-10 146L110 144L112 152L-10 156Z" fill="#5e452e"/>
<path d="M-10 124L108 128L112 146L-10 148Z" fill="url(#@dk)"/>
<path d="`+planks+`" stroke="#3a2614" stroke-opacity=".5" stroke-width=".7" fill="none"/>
<path d="M-10 124L108 128L112 146" fill="none" stroke="#f1d3a0" stroke-opacity=".5" stroke-width="1.4"/>
<rect x="100" y="112" width="6" height="22" rx="2" fill="url(#@pl)"/><ellipse cx="103" cy="112" rx="3" ry="1.3" fill="#9b7b55"/>
<path d="M104 118Q76 124 52 122" fill="none" stroke="#d9c496" stroke-width="1.3"/>
<g fill="none" stroke-width="1.3" stroke-linecap="round">`+reeds+`</g>
<g fill="#5d6068">`+stones+`</g><g fill="#a3a6ac" opacity=".5" transform="translate(-1.5 -1.5)">`+stones+`</g>
<rect width="480" height="270" fill="url(#@vg)"/>
</svg>`;
  return fin(u,b);
};
})();
