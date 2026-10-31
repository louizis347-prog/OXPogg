/* Kit de ilustrações do Painel do Professor: ícones de objetos, bandeiras, rostos de humor, cenas por hora do dia, dados, árvore genealógica. */
(function(){
'use strict';
var K='#1f2a44',S='stroke="'+K+'" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"';
function svg(vb,inner,cls){return '<svg viewBox="'+vb+'" class="vis '+(cls||'')+'" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'+inner+'</svg>'}
function P(d,f,x){return '<path d="'+d+'" fill="'+(f||'none')+'" '+S+(x||'')+'/>'}
function R(x,y,w,h,f,r){return '<rect x="'+x+'" y="'+y+'" width="'+w+'" height="'+h+'" rx="'+(r||0)+'" fill="'+f+'" '+S+'/>'}
function C(x,y,r,f){return '<circle cx="'+x+'" cy="'+y+'" r="'+r+'" fill="'+f+'" '+S+'/>'}
function L(x1,y1,x2,y2,w){return '<path d="M'+x1+' '+y1+'L'+x2+' '+y2+'" '+S+(w?' stroke-width="'+w+'"':'')+' fill="none"/>'}
function T(x,y,t,sz,f){return '<text x="'+x+'" y="'+y+'" text-anchor="middle" font-family="system-ui,Arial" font-weight="800" font-size="'+sz+'" fill="'+(f||K)+'">'+t+'</text>'}
var COL={red:'#e8473b',blue:'#3b82e8',green:'#3fae5a',yellow:'#f5c542',orange:'#f08a2b',pink:'#ee7fa8',purple:'#8f5bd6',brown:'#9b6a43',black:'#2b2b36',white:'#ffffff',gray:'#9aa3b5'};
function col(c){return COL[c]||c||'#cfd8ff'}
/* ---------- objetos (viewBox 100x100) ---------- */
var OBJ={
book:function(c){return P('M14 24h30q6 0 6 6v50q0-6-6-6H14z',col(c||'blue'))+P('M86 24H56q-6 0-6 6v50q0-6 6-6h30z',col(c||'blue'))+L(24,38,40,38)+L(24,48,40,48)+L(60,38,76,38)+L(60,48,76,48)},
pen:function(c){return P('M70 12l18 18-46 46-24 6 6-24z',col(c||'blue'))+P('M62 20l18 18')+P('M18 82l8-8',' #f2d7a8')},
pencil:function(c){return P('M72 10l18 18-52 52-24 6 6-24z',col(c||'yellow'))+P('M66 16l18 18')+P('M14 86l6-18 12 12z','#f2d7a8')+P('M14 86l3-9 6 6z',K)},
bag:function(c){return P('M30 34q0-18 20-18t20 18',null)+R(18,32,64,54,col(c||'orange'),10)+R(30,50,40,20,'rgba(255,255,255,.35)',6)+L(50,50,50,70)},
desk:function(c){return R(10,34,80,12,col(c||'#c98a52'),3)+L(18,46,18,86)+L(82,46,82,86)+R(56,46,26,22,'#e0b484',2)+L(61,57,77,57)},
chair:function(c){return P('M30 14h34l-4 36H34z',col(c||'#c98a52'))+R(26,50,46,10,col(c||'#c98a52'),3)+L(32,60,28,88)+L(66,60,70,88)},
board:function(c){return R(8,14,84,56,'#2f7d5b',4)+R(8,14,84,56,'none',4)+L(30,34,58,34)+L(30,46,70,46)+L(30,58,48,58)+L(34,70,30,88)+L(66,70,70,88)+R(40,66,20,4,'#fff',1)},
window:function(){return R(14,12,72,76,'#bfe3ff',4)+L(50,12,50,88)+L(14,50,86,50)+P('M24 36l12-10','none',' stroke="#fff"')+R(10,86,80,6,'#d9d2c3',2)},
door:function(c){return R(26,8,48,84,col(c||'#b7794a'),4)+R(34,18,32,26,'rgba(255,255,255,.3)',3)+R(34,52,32,28,'rgba(255,255,255,.3)',3)+C(64,54,3.5,'#f5c542')},
clock:function(){return C(50,50,38,'#fff')+L(50,50,50,26)+L(50,50,68,58)+C(50,50,4,K)+L(50,16,50,22)+L(50,78,50,84)+L(16,50,22,50)+L(78,50,84,50)},
ruler:function(){return P('M10 60L60 10l30 30L40 90z','#f5c542')+L(26,60,34,52)+L(38,48,46,40)+L(50,36,58,28)+L(62,24,70,16)},
eraser:function(){return P('M20 58l30-30 32 32-30 30z','#ee7fa8')+P('M20 58l32 32')+P('M44 34l32 32','none')},
car:function(c){return P('M10 62q0-14 10-16l12-18h34l14 18q10 2 10 16v10H10z',col(c||'red'))+P('M38 32l-8 14h16V32z M52 32v14h24L66 32z','#cfeaff')+C(30,74,10,'#444')+C(72,74,10,'#444')+C(30,74,4,'#bbb')+C(72,74,4,'#bbb')},
ball:function(c){return C(50,50,38,col(c||'blue'))+P('M12 50q38-18 76 0','none')+P('M50 12q-22 38 0 76','none')+P('M50 12q22 38 0 76','none')},
hat:function(c){return P('M10 70h80q-4 8-40 8T10 70z',col(c||'purple'))+P('M26 70q0-40 24-40t24 40',col(c||'purple'))+R(26,56,48,8,'#f5c542',2)},
apple:function(c){return P('M50 30q-30-14-36 14t14 38q12 8 22 2 10 6 22-2 20-12 14-38T50 30z',col(c||'red'))+P('M50 30q2-12 12-16','none')+P('M54 22q12-6 18 2-8 8-18-2z','#3fae5a')},
orange:function(){return C(50,56,34,'#f08a2b')+P('M50 22q2-10 10-12','none')+P('M52 20q10-8 18 0-8 8-18 0z','#3fae5a')},
banana:function(){return P('M16 28q6 50 60 54 12 0 14-6-36-4-50-54z','#f5c542')+P('M16 28l6-8')},
balloon:function(c){return P('M50 10q30 0 30 30t-30 40q-30-10-30-40t30-30z',col(c||'red'))+P('M46 80l4 6 4-6z',col(c||'red'))+P('M50 86q-8 6 0 12','none')+P('M34 28q4-10 12-12','none',' stroke="#fff"')},
flower:function(c){return [0,72,144,216,288].map(function(a){return '<g transform="rotate('+a+' 50 44)">'+'<ellipse cx="50" cy="22" rx="12" ry="16" fill="'+col(c||'pink')+'" '+S+'/></g>'}).join('')+C(50,44,10,'#f5c542')+L(50,54,50,92)+P('M50 74q16-4 20-18-16 0-20 18z','#3fae5a')},
coin:function(){return C(50,50,36,'#f5c542')+C(50,50,26,'#f8d96a')+T(50,60,'$',30,'#b8860b')},
cup:function(c){return P('M16 30h56v32q0 20-28 20T16 62z',col(c||'#fff'))+P('M72 38h8q10 0 10 10t-12 12h-6','none')+P('M30 14q-6 6 0 10M44 12q-6 6 0 12M58 14q-6 6 0 10','none',' stroke-width="2.5"')},
bread:function(){return P('M12 54q0-26 38-26t38 26q0 20-12 22H24q-12-2-12-22z','#e0a25d')+P('M34 40l6 10M50 36l6 12M66 40l6 10','none')},
cake:function(){return R(16,46,68,36,'#f1c27d',6)+P('M16 60q8 8 17 0t17 0 17 0 17 0','none')+R(16,38,68,12,'#ee7fa8',6)+L(50,38,50,22)+P('M50 22q-6-6 0-12 6 6 0 12z','#f5c542')},
heart:function(c){return P('M50 86C10 56 8 26 28 20q16-4 22 14 6-18 22-14 20 6 22 36-14 22-44 30z',col(c||'red'))},
star:function(c){return P('M50 8l12 28 30 3-23 20 7 30-26-16-26 16 7-30L8 39l30-3z',col(c||'yellow'))},
sun:function(){return C(50,50,20,'#f5c542')+[0,45,90,135,180,225,270,315].map(function(a){return '<g transform="rotate('+a+' 50 50)">'+L(50,18,50,6)+'</g>'}).join('')},
moon:function(){return P('M64 10q-34 6-34 40t34 40q-40 4-52-30T64 10z','#f5e08a')},
cloud:function(){return P('M24 70q-14 0-14-14t16-14q2-16 20-16t22 16q22-2 22 16t-18 12z','#fff')},
house:function(c){return P('M10 48L50 14l40 34v38H10z',col(c||'#f08a2b'))+P('M4 52L50 10l46 42','none')+R(40,60,20,26,'#7a4a2a',2)+R(18,56,14,14,'#bfe3ff',2)+R(68,56,14,14,'#bfe3ff',2)},
wave:function(){return P('M34 86q-18-14-14-40l4-22q2-8 8-6t4 8l-2 14 4-30q2-8 8-6t4 8l-2 24 4-24q2-8 8-6t4 8l-2 28 4-18q2-8 8-6t2 10q-2 26-12 48z','#ffd7b5')+P('M80 24q8-6 12 0M84 14q8-4 12 4','none')},
nametag:function(c){return R(10,20,80,60,'#fff',8)+R(10,20,80,22,col(c||'#e8473b'),8)+T(50,38,'HELLO',13,'#fff')+T(50,60,'my name is',9)+L(22,68,78,68)},
speech:function(c){return P('M14 18h72q6 0 6 6v38q0 6-6 6H52l-18 18V68H14q-6 0-6-6V24q0-6 6-6z',col(c||'#fff'))+L(24,34,74,34)+L(24,46,60,46)},
suitcase:function(c){return R(12,30,76,52,col(c||'#3b82e8'),8)+P('M36 30V20q0-6 6-6h16q6 0 6 6v10','none')+L(12,52,88,52)+R(44,48,12,10,'#f5c542',2)},
globe:function(){return C(50,50,38,'#7fc4ff')+P('M30 28q14 6 8 18t10 14-4 22M62 24q-6 12 8 16t14 4','#6dbb6a')+P('M12 50h76M50 12q-22 38 0 76M50 12q22 38 0 76','none',' stroke-width="2"')},
plane:function(){return P('M10 54l30-6-14-26h8l26 24 28-6q10 0 10 6t-10 6l-28-4-24 26h-8l12-26-30-4z','#fff')},
pin:function(){return P('M50 92Q22 58 22 38a28 28 0 0156 0q0 20-28 54z','#e8473b')+C(50,38,10,'#fff')},
key:function(){return C(30,40,18,'#f5c542')+C(30,40,6,'#fff')+P('M44 50l40 36M70 70l8-8M60 60l8-8','none')},
phone:function(){return R(28,8,44,84,'#2b3350',8)+R(33,18,34,56,'#7fc4ff',3)+C(50,83,4,'#fff')},
envelope:function(){return R(10,22,80,56,'#fff',6)+P('M10 28l40 30 40-30','none')},
magnifier:function(){return C(42,42,26,'#cfeaff')+L(62,62,88,88)},
bell:function(){return P('M50 12q26 0 26 30v18l10 12H14l10-12V42q0-30 26-30z','#f5c542')+C(50,86,6,'#f5c542')},
trophy:function(){return P('M28 12h44v28q0 22-22 22T28 40z','#f5c542')+P('M28 20H12q0 22 18 24M72 20h16q0 22-18 24','none')+R(42,62,16,14,'#f5c542',2)+R(30,76,40,10,'#b8860b',3)},
dice:function(){return R(14,14,72,72,'#fff',12)+C(34,34,6,K)+C(66,34,6,K)+C(50,50,6,K)+C(34,66,6,K)+C(66,66,6,K)},
lamp:function(){return P('M26 14h48l10 40H16z','#f5c542')+L(50,54,50,78)+R(32,78,36,10,'#8a6a2a',3)},
umbrella:function(c){return P('M8 52q0-38 42-38t42 38q-10-10-21 0-10-10-21 0-11-10-21 0-11-10-21 0z',col(c||'#e8473b'))+P('M50 52v30q0 10-10 8','none')},
tree:function(){return R(44,54,12,36,'#9b6a43',2)+C(50,34,28,'#4ea45a')+C(32,44,16,'#4ea45a')+C(68,44,16,'#4ea45a')},
cat:function(){return P('M20 40l6-24 16 14h16l16-14 6 24q4 40-30 44T20 40z','#f0a24a')+C(40,52,3,K)+C(60,52,3,K)+P('M46 62l4 4 4-4','none')+L(14,58,32,60,2)+L(14,66,32,64,2)+L(86,58,68,60,2)+L(86,66,68,64,2)},
dog:function(){return P('M22 40q-10 0-12 18t14 8q4 14 26 14t26-14q16 10 14-8t-12-18q-4-22-28-22T22 40z','#d9a066')+C(40,48,4,K)+C(60,48,4,K)+C(50,62,6,K)+P('M50 68v6','none')}
};

/* ---------- adereços do curso regular (mesmo traço dos personagens) ---------- */
var PMAP={book:['book','#2f6fe0'],pencil:['pencil'],clock:['clock'],apple:['apple'],bread:['bread'],cake:['cake'],cup:['cup'],balloon:['balloon',null,.72,26],ball:['ball'],car:['car'],flower:['flower'],heart:['heart'],star:['star'],sun:['sun'],moon:['moon'],house:['house'],tree:['tree',null,.8,8],suitcase:['suitcase'],bell:['bell'],trophy:['trophy'],envelope:['envelope'],phone:['telephone'],key:['key'],lamp:['lamp',null,1.1,6],umbrella:['umbrella'],magnifier:['magnifier'],plane:['airplane'],cloud:['cloud'],dice:['dice'],hat:['tophat'],tea:['cup','#bfe2f6'],map:['map'],gift:['gift'],camera:['camera'],bicycle:['bicycle'],bus:['bus'],train:['train'],pizza:['pizza'],cheese:['cheese'],egg:['egg'],carrot:['carrot'],guitar:['guitar'],piano:['piano'],mailbox:['mailbox'],computer:['computer'],flag:['flag']};
function propIcon(id,c,cls,sc,dy){var Lb=window.PogFichaLib;if(!Lb||!Lb.PROP[id])return '';var inner='';try{inner=Lb.PROP[id](c)}catch(e){return ''}
 return svg('-72 -72 144 144','<defs><radialGradient id="pg'+id+'" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#fff" stop-opacity=".9"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient></defs><circle r="66" fill="url(#pg'+id+')"/><ellipse cx="0" cy="54" rx="42" ry="7" fill="rgba(31,42,68,.14)"/><g transform="translate(0 '+(dy||0)+') scale('+(sc||1)+')">'+inner+'</g>',cls)}
function obj(name,color,cls){var m=PMAP[name];if(m&&!(color&&PMAPSKIP[name])){var r=propIcon(m[0],color&&color.charAt(0)==='#'?color:(color?col(color):m[1]||undefined),cls,m[2],m[3]);if(r)return r}var f=OBJ[name];return f?svg('0 0 100 100',f(color),cls):''}
var PMAPSKIP={car:0};
/* ---------- bandeiras (viewBox 90x60) ---------- */
function fr(x,y,w,h,f){return '<rect x="'+x+'" y="'+y+'" width="'+w+'" height="'+h+'" fill="'+f+'"/>'}
var FLAG={
br:function(){return fr(0,0,90,60,'#2e9e4f')+'<path d="M45 8L82 30 45 52 8 30z" fill="#f5d93a"/><circle cx="45" cy="30" r="12" fill="#2a4fa0"/><path d="M34 28q11-4 22 4" stroke="#fff" stroke-width="2" fill="none"/>'},
jp:function(){return fr(0,0,90,60,'#fff')+'<circle cx="45" cy="30" r="15" fill="#d6283c"/>'},
eg:function(){return fr(0,0,90,20,'#c8102e')+fr(0,20,90,20,'#fff')+fr(0,40,90,20,'#111')+'<path d="M40 24h10v12H40z" fill="#c8a137"/>'},
gb:function(){return fr(0,0,90,60,'#1d3f8f')+'<path d="M0 0L90 60M90 0L0 60" stroke="#fff" stroke-width="12"/><path d="M0 0L90 60M90 0L0 60" stroke="#cf142b" stroke-width="4"/><path d="M45 0v60M0 30h90" stroke="#fff" stroke-width="18"/><path d="M45 0v60M0 30h90" stroke="#cf142b" stroke-width="10"/>'},
mx:function(){return fr(0,0,30,60,'#0a7a3d')+fr(30,0,30,60,'#fff')+fr(60,0,30,60,'#ce1126')+'<circle cx="45" cy="30" r="8" fill="#9b6a43"/>'},
in:function(){return fr(0,0,90,20,'#f59a23')+fr(0,20,90,20,'#fff')+fr(0,40,90,20,'#138808')+'<circle cx="45" cy="30" r="8" fill="none" stroke="#1d3f8f" stroke-width="2"/><path d="M45 22v16M37 30h16" stroke="#1d3f8f" stroke-width="1.5"/>'},
us:function(){var s='';for(var i=0;i<7;i++)s+=fr(0,i*60/7*2,90,60/13,'#b22234');s=fr(0,0,90,60,'#fff')+Array.apply(null,Array(7)).map(function(_,i){return fr(0,i*60/6.5,90,60/13,'#b22234')}).join('');return s+fr(0,0,38,32,'#3c3b6e')+'<g fill="#fff">'+[8,18,28].map(function(x){return [6,14,22].map(function(y){return '<circle cx="'+x+'" cy="'+y+'" r="1.6"/>'}).join('')}).join('')+'</g>'},
fr:function(){return fr(0,0,30,60,'#0055a4')+fr(30,0,30,60,'#fff')+fr(60,0,30,60,'#ef4135')},
it:function(){return fr(0,0,30,60,'#009246')+fr(30,0,30,60,'#fff')+fr(60,0,30,60,'#ce2b37')},
es:function(){return fr(0,0,90,15,'#aa151b')+fr(0,15,90,30,'#f1bf00')+fr(0,45,90,15,'#aa151b')},
de:function(){return fr(0,0,90,20,'#111')+fr(0,20,90,20,'#dd0000')+fr(0,40,90,20,'#ffce00')},
cn:function(){return fr(0,0,90,60,'#de2910')+'<path d="M16 8l3 9h9l-7 5 3 9-8-6-8 6 3-9-7-5h9z" fill="#ffde00"/>'},
kr:function(){return fr(0,0,90,60,'#fff')+'<circle cx="45" cy="30" r="13" fill="#cd2e3a"/><path d="M32 30a13 13 0 0026 0 6.5 6.5 0 01-13 0 6.5 6.5 0 00-13 0z" fill="#0047a0"/><g stroke="#111" stroke-width="3"><path d="M10 12l8-4M12 18l8-4M72 46l8-4M70 52l8-4M72 8l8 4M70 14l8 4M10 42l8 4M12 48l8 4"/></g>'},
ca:function(){return fr(0,0,90,60,'#fff')+fr(0,0,22,60,'#d52b1e')+fr(68,0,22,60,'#d52b1e')+'<path d="M45 12l5 10 8-4-3 14 6-2-4 8-8 0v8h-8v-8l-8 0-4-8 6 2-3-14 8 4z" fill="#d52b1e"/>'},
au:function(){return fr(0,0,90,60,'#00247d')+'<path d="M0 0l40 26M40 0L0 26" stroke="#fff" stroke-width="5"/><path d="M20 0v26M0 13h40" stroke="#fff" stroke-width="8"/><path d="M20 0v26M0 13h40" stroke="#cf142b" stroke-width="4"/><g fill="#fff"><circle cx="20" cy="44" r="3.5"/><circle cx="62" cy="14" r="2.5"/><circle cx="74" cy="26" r="2.5"/><circle cx="62" cy="42" r="2.5"/><circle cx="54" cy="28" r="2.5"/></g>'},
ar:function(){return fr(0,0,90,20,'#74acdf')+fr(0,20,90,20,'#fff')+fr(0,40,90,20,'#74acdf')+'<circle cx="45" cy="30" r="5" fill="#f6b40e"/>'},
pt:function(){return fr(0,0,36,60,'#046a38')+fr(36,0,54,60,'#da291c')+'<circle cx="36" cy="30" r="10" fill="#ffe000"/>'},
ie:function(){return fr(0,0,30,60,'#169b62')+fr(30,0,30,60,'#fff')+fr(60,0,30,60,'#ff883e')},
ng:function(){return fr(0,0,30,60,'#008751')+fr(30,0,30,60,'#fff')+fr(60,0,30,60,'#008751')},
tr:function(){return fr(0,0,90,60,'#e30a17')+'<circle cx="38" cy="30" r="14" fill="#fff"/><circle cx="43" cy="30" r="11" fill="#e30a17"/><path d="M56 30l7-2-4 6 0-8 4 6z" fill="#fff"/>'},
ru:function(){return fr(0,0,90,20,'#fff')+fr(0,20,90,20,'#0039a6')+fr(0,40,90,20,'#d52b1e')}
};
function flag(code,cls){var f=FLAG[code];return f?'<svg viewBox="0 0 90 60" class="vis flag '+(cls||'')+'" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><defs><clipPath id="fc'+code+'"><rect width="90" height="60" rx="6"/></clipPath></defs><g clip-path="url(#fc'+code+')">'+f()+'</g><rect width="90" height="60" rx="6" fill="none" stroke="'+K+'" stroke-width="3"/></svg>':''}
/* ---------- humor (rostos) ---------- */
var MOOD={great:['#7bd88f','M30 58q20 20 40 0'],fine:['#b6e36e','M32 60q18 12 36 0'],ok:['#ffd35c','M32 64h36'],tired:['#f4b36a','M32 68q18-10 36 0'],sad:['#9ec5f4','M32 70q18-16 36 0'],angry:['#f28b82','M32 70q18-12 36 0']};
function mood(k,cls){var m=MOOD[k]||MOOD.ok;var eyes=k==='tired'?L(30,44,42,44)+L(58,44,70,44):C(36,44,5,K)+C(64,44,5,K);var brows=k==='angry'?L(28,34,44,40)+L(72,34,56,40):'';return svg('0 0 100 100',C(50,50,40,m[0])+eyes+brows+P(m[1],'none')+(k==='sad'?'<path d="M74 54q4 10-2 12q-6-2-2-12z" fill="#7fc4ff"/>':''),cls)}
/* ---------- hora do dia ---------- */
var TOD={dawn:['#ffd9b3','#ffb199','#f5c542',50,64],day:['#9edcff','#d6f0ff','#f5c542',50,34],dusk:['#ff9966','#ffcc99','#ff7a3d',50,64],night:['#1d2a5c','#3b4a8a',null,0,0]};
function tod(k,cls){var t=TOD[k]||TOD.day,id='tg'+k;var body='<defs><linearGradient id="'+id+'" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="'+t[0]+'"/><stop offset="1" stop-color="'+t[1]+'"/></linearGradient><clipPath id="tc'+k+'"><rect width="100" height="100" rx="14"/></clipPath></defs><g clip-path="url(#tc'+k+')"><rect width="100" height="100" fill="url(#'+id+')"/>';
 if(k==='night'){body+='<circle cx="70" cy="30" r="14" fill="#f5e08a"/><circle cx="76" cy="26" r="12" fill="#2a3870"/>'+[[18,20],[34,12],[50,28],[24,40],[84,52],[60,14]].map(function(p){return '<circle cx="'+p[0]+'" cy="'+p[1]+'" r="1.8" fill="#fff"/>'}).join('')}
 else body+='<circle cx="'+(k==='day'?50:30)+'" cy="'+t[4]+'" r="14" fill="'+t[2]+'"/>'+(k==='day'?[0,45,90,135,180,225,270,315].map(function(a){return '<g transform="rotate('+a+' 50 34)"><path d="M50 14v-6" stroke="'+t[2]+'" stroke-width="3"/></g>'}).join(''):'');
 body+='<path d="M0 78q25-18 50-6t50-6v34H0z" fill="'+(k==='night'?'#1c2f54':'#5aa85f')+'"/><path d="M0 88q30-10 60-2t40-4v18H0z" fill="'+(k==='night'?'#14233f':'#4a9650')+'"/></g><rect width="100" height="100" rx="14" fill="none" stroke="'+K+'" stroke-width="3"/>';
 return svg('0 0 100 100',body,cls)}
/* ---------- números: dados, ten-frame ---------- */
function dots(n,cls){var cols=5,rows=Math.max(1,Math.ceil(Math.min(n,20)/5)),o='';for(var i=0;i<Math.min(n,20);i++){o+=C(14+(i%cols)*18,16+Math.floor(i/cols)*18,6.5,i<10?'#3b82e8':'#f08a2b')}return svg('0 0 100 '+(10+rows*18+6),o,cls)}
function numBlob(n,c,cls){return svg('0 0 100 100',C(50,50,42,col(c||'#7a5cf0'))+T(50,(String(n).length>2?60:66),String(n),(String(n).length>1?40:52),'#fff'),cls)}
function swatch(c,cls){return svg('0 0 100 100','<rect x="10" y="10" width="80" height="80" rx="16" fill="'+col(c)+'" '+S+'/><path d="M22 28q12-10 30-10" stroke="rgba(255,255,255,.7)" stroke-width="5" fill="none" stroke-linecap="round"/>',cls)}
function crayon(c,cls){return svg('0 0 100 100','<g transform="rotate(35 50 50)">'+R(38,8,24,66,col(c),4)+P('M38 74h24l-12 20z','#f2d7a8')+P('M44 85h12l-6 9z',col(c))+R(38,26,24,14,'rgba(255,255,255,.45)',0)+'</g>',cls)}
/* ---------- tile de letra ---------- */
function letter(ch,c,cls){return svg('0 0 100 100',R(8,8,84,84,col(c||'#fff'),16)+T(50,68,ch+ch.toLowerCase(),38,K),cls)}
/* ---------- árvore genealógica (usa faces via callback) ---------- */
function famTree(nodes,faceFn){var w=620,h=372,out='',byId={};nodes.list.forEach(function(n){byId[n.id]=n});
 (nodes.couples||[]).forEach(function(c){var A=byId[c.a],B=byId[c.b],mx=(A.x+B.x)/2,y=A.y;out+='<path d="M'+(A.x+36)+' '+y+'H'+(B.x-36)+'" stroke="#e8438f" stroke-width="4" fill="none"/><path d="M'+(mx-9)+' '+(y-3)+'q9-12 18 0q-9 14-18 0z" fill="#e8438f"/>';
  var kids=(c.kids||[]).map(function(k){return byId[k]});if(!kids.length)return;var by=y+64;out+='<path d="M'+mx+' '+y+'V'+by+'" stroke="#8a93b8" stroke-width="3" fill="none"/>';
  var xs=kids.map(function(k){return k.x}).concat([mx]);out+='<path d="M'+Math.min.apply(null,xs)+' '+by+'H'+Math.max.apply(null,xs)+'" stroke="#8a93b8" stroke-width="3" fill="none"/>';
  kids.forEach(function(k){out+='<path d="M'+k.x+' '+by+'V'+(k.y-38)+'" stroke="#8a93b8" stroke-width="3" fill="none"/>'})});
 nodes.list.forEach(function(n){var f=faceFn?faceFn(n.face):'';out+='<g transform="translate('+(n.x-36)+' '+(n.y-36)+')"><circle cx="36" cy="36" r="36" fill="#fff" stroke="'+K+'" stroke-width="3"/><foreignObject x="3" y="3" width="66" height="66"><div xmlns="http://www.w3.org/1999/xhtml" style="width:66px;height:66px;border-radius:50%;overflow:hidden">'+f+'</div></foreignObject></g><text x="'+n.x+'" y="'+(n.y+56)+'" text-anchor="middle" font-family="system-ui" font-weight="800" font-size="16" fill="'+K+'">'+n.label+'</text>'});
 return svg('0 0 '+w+' '+h,out,'tree')}
window.Vis={svg:svg,obj:obj,flag:flag,mood:mood,tod:tod,dots:dots,num:numBlob,swatch:swatch,crayon:crayon,letter:letter,famTree:famTree,OBJ:OBJ,FLAG:FLAG,
 /* spec "tipo:arg[:cor]" */
 by:function(spec,cls){if(!spec)return '';var p=spec.split(':'),k=p[0],a=p[1],c=p[2];
  if(k==='obj')return obj(a,c,cls);if(k==='prop')return propIcon(a,c?col(c):undefined,cls);if(k==='flag')return flag(a,cls);if(k==='mood')return mood(a,cls);if(k==='tod')return tod(a,cls);if(k==='dots')return dots(+a,cls);if(k==='num')return numBlob(a,c,cls);if(k==='swatch')return swatch(a,cls);if(k==='crayon')return crayon(a,cls);if(k==='letter')return letter(a,c,cls);return ''}};
})();
