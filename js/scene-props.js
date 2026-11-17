/* Objetos de cena por aula + clima + "briefing" (descrição/prompt) de cada aula.
   O briefing é calculado a partir da obra, do título e do vocabulário: tema, horário, clima e objetos.
   Os objetos são desenhados em SVG sobre o cenário pintado (img/scenes), nos pontos livres do piso. */
(function(){
'use strict';
var U=0;
function G(stops,x1,y1,x2,y2){var id='sp'+(++U);return {id:id,def:'<linearGradient id="'+id+'" x1="'+(x1||0)+'" y1="'+(y1||0)+'" x2="'+(x2||0)+'" y2="'+(y2==null?1:y2)+'">'+stops.map(function(s,i){return '<stop offset="'+s[0]+'" stop-color="'+s[1]+'"'+(s[2]!=null?' stop-opacity="'+s[2]+'"':'')+'/>'}).join('')+'</linearGradient>'}}
function sh(w){return '<ellipse cx="0" cy="3" rx="'+w+'" ry="'+(w*.14)+'" fill="#000" opacity=".28" filter="url(#spb)"/>'}
function R(x,y,w,h,f,rx,o){return '<rect x="'+x+'" y="'+y+'" width="'+w+'" height="'+h+'" rx="'+(rx||0)+'" fill="'+f+'"'+(o!=null?' opacity="'+o+'"':'')+'/>'}
function E(cx,cy,rx,ry,f,o){return '<ellipse cx="'+cx+'" cy="'+cy+'" rx="'+rx+'" ry="'+ry+'" fill="'+f+'"'+(o!=null?' opacity="'+o+'"':'')+'/>'}
function P(d,f,o,ex){return '<path d="'+d+'" fill="'+f+'"'+(o!=null?' opacity="'+o+'"':'')+' '+(ex||'')+'/>'}
function L(d,c,w,ex){return '<path d="'+d+'" fill="none" stroke="'+c+'" stroke-width="'+w+'" stroke-linecap="round" '+(ex||'')+'/>'}
/* cada sprite: função (defs[]) -> string desenhada com a base em (0,0), altura ~100 */
var S={
 coffee:function(d){var g=G([[0,'#d9a06a'],[1,'#8a5a36']]);d.push(g.def);return sh(40)+R(-34,-62,68,7,'url(#'+g.id+')',3)+R(-3,-55,6,52,'#5a3a26')+E(0,-2,22,4,'#3a2616')+E(-10,-66,15,3.5,'#f6efe4')+R(-18,-82,16,16,'#fbfaf5',3)+R(-18,-82,5,16,'#000',3,.08)+E(-10,-82,8,2.6,'#6a4228')+L('M-1 -80 q6 0 6 6 q0 6 -6 6','#fbfaf5',2.6)+L('M-14 -86 q-3 -8 2 -14 M-8 -86 q-3 -8 2 -14','#fff',1.6,'opacity=".5"')+E(16,-67,12,4,'#e8b36a')+P('M6 -68 q10 -9 22 0 q-10 5 -22 0Z','#d99a50')+R(-30,-62,60,2,'#fff',0,.25)},
 books:function(d){var c=['#b5453a','#3d7fb8','#4a9b6a','#d9b44a','#8c5aa8'];return sh(34)+c.map(function(k,i){return R(-28+i%2*3,-12*(i+1),56-i*5,12,k,2)+R(-28+i%2*3,-12*(i+1),56-i*5,3,'#fff',0,.18)+R(-26+i%2*3+8,-12*(i+1)+4,30-i*3,3,'#f0d890',0,.7)}).join('')+E(-4,-64,0,0,'none')},
 laptop:function(d){var g=G([[0,'#7a5a3a'],[1,'#4a2f1c']]);d.push(g.def);return sh(48)+R(-48,-52,96,8,'url(#'+g.id+')',3)+R(-42,-44,6,44,'#3a2616')+R(36,-44,6,44,'#3a2616')+P('M-26 -52 L-20 -86 L20 -86 L26 -52Z','#2b2f3a')+P('M-22 -55 L-17 -82 L17 -82 L22 -55Z','#6fb6f0')+P('M-22 -55 L-17 -82 L0 -82 L-6 -55Z','#fff',.18)+R(-30,-54,60,3,'#aab2c0',1)+R(14,-60,12,8,'#e9edf4',2)},
 pizza:function(d){return sh(44)+R(-42,-60,84,6,'#a97c50',3)+R(-3,-54,6,50,'#6a4a2c')+E(0,-3,20,4,'#3a2a1a')+R(-26,-76,52,16,'#d9b06a',2)+E(0,-77,24,6,'#f2c27a')+E(-8,-77,5,2,'#c0453a')+E(8,-76,5,2,'#c0453a')+E(0,-79,4,1.6,'#4a9b6a')+R(-26,-64,52,3,'#000',0,.15)},
 flowers:function(d){var o='';[['#e0525a',-14,-96],['#f2c24a',0,-104],['#e888b8',14,-94],['#fff',-6,-88],['#e0525a',8,-86]].forEach(function(f){o+=L('M0 -50 Q'+(f[1]/2)+' -70 '+f[1]+' '+(f[2]+8),'#3f8a4f',2.4)+E(f[1],f[2],9,9,f[0])+E(f[1],f[2],3.5,3.5,'#f7e08a')});return sh(26)+o+P('M-18 -52 L18 -52 L13 -2 L-13 -2Z','#5a8aa8')+R(-20,-56,40,6,'#7aa6c2',2)+P('M4 -52 L18 -52 L13 -2 L2 -2Z','#000',.14)},
 tv:function(d){return sh(46)+R(-40,-50,80,6,'#3a2c22',2)+R(-34,-44,6,42,'#2a1e16')+R(28,-44,6,42,'#2a1e16')+R(-38,-98,76,50,'#14161c',5)+R(-34,-94,68,42,'#4a7fc0',2)+P('M-34 -94 L-6 -94 L-34 -60Z','#fff',.16)+E(0,-72,10,10,'#f4c24a',.9)+R(-6,-47,12,2,'#888')},
 bicycle:function(d){return sh(50)+E(-30,-22,22,22,'none')+'<circle cx="-30" cy="-22" r="21" fill="none" stroke="#2a2f3a" stroke-width="3.4"/><circle cx="30" cy="-22" r="21" fill="none" stroke="#2a2f3a" stroke-width="3.4"/>'+L('M-30 -22 L-8 -22 L10 -52 L28 -22 M-8 -22 L-14 -54 L10 -52','#c0453a',3.4)+L('M-18 -56 L-6 -56 M24 -58 L34 -58 L30 -22','#2a2f3a',3)+E(-30,-22,3,3,'#888')+E(30,-22,3,3,'#888')+R(-18,-60,16,4,'#2a2f3a',2)},
 car:function(d){var g=G([[0,'#e05a4a'],[1,'#a02f28']]);d.push(g.def);return sh(66)+R(-62,-34,124,26,'url(#'+g.id+')',8)+P('M-36 -34 Q-28 -58 -6 -58 L24 -58 Q40 -56 48 -34Z','url(#'+g.id+')')+P('M-28 -36 Q-22 -54 -6 -54 L2 -54 L2 -36Z','#bfe6ff')+P('M8 -36 L8 -54 L22 -54 Q34 -52 40 -36Z','#bfe6ff')+'<circle cx="-36" cy="-8" r="12" fill="#1a1c22"/><circle cx="36" cy="-8" r="12" fill="#1a1c22"/><circle cx="-36" cy="-8" r="5" fill="#9aa3ac"/><circle cx="36" cy="-8" r="5" fill="#9aa3ac"/>'+E(58,-22,5,4,'#ffe9a8')+R(-62,-22,5,8,'#f2c24a',2)+R(-60,-34,120,2,'#fff',0,.3)},
 suitcase:function(d){return sh(40)+R(-34,-52,68,52,'#2f6aa8',7)+R(-34,-52,68,6,'#fff',3,.25)+R(-22,-64,44,12,'none',6)+L('M-12 -52 q0 -12 12 -12 q12 0 12 12','#1d3f6a',4)+R(-34,-30,68,3,'#000',0,.2)+R(-6,-40,12,8,'#c9a24a',2)+R(10,-98,46,38,'#c0453a',6)+R(14,-98,38,5,'#fff',2,.25)+L('M24 -98 q0 -9 9 -9 q9 0 9 9','#7a2a22',3)},
 umbrella:function(d){return sh(30)+L('M0 -4 L0 -78','#5a4030',3.4)+P('M-46 -78 Q0 -122 46 -78 Q34 -84 23 -78 Q12 -84 0 -78 Q-12 -84 -23 -78 Q-34 -84 -46 -78Z','#e05a6a')+P('M-23 -78 Q-6 -110 0 -118 Q6 -110 23 -78 Q12 -84 0 -78 Q-12 -84 -23 -78Z','#f2c24a')+L('M0 -8 q8 0 8 -8','#5a4030',3.4)},
 dog:function(d){return sh(36)+E(0,-26,28,16,'#c98a4a')+E(-24,-40,13,12,'#c98a4a')+P('M-30 -50 Q-40 -40 -34 -30 Q-28 -38 -26 -48Z','#8a5a2a')+E(-28,-42,2.4,2.4,'#222')+E(-36,-38,3,2.4,'#222')+R(-16,-14,8,14,'#c98a4a',3)+R(8,-14,8,14,'#c98a4a',3)+R(-26,-14,8,14,'#b07a3a',3)+R(18,-14,8,14,'#b07a3a',3)+P('M26 -34 Q42 -48 38 -26 Q34 -34 26 -28Z','#c98a4a')+E(0,-20,22,8,'#e8c496',.7)},
 cat:function(d){return sh(26)+E(0,-22,20,18,'#8a8f9a')+E(0,-46,13,12,'#8a8f9a')+P('M-12 -52 L-12 -64 L-4 -56Z','#8a8f9a')+P('M12 -52 L12 -64 L4 -56Z','#8a8f9a')+E(-5,-47,2,3,'#7ad07a')+E(5,-47,2,3,'#7ad07a')+P('M18 -14 Q40 -10 34 -34','#8a8f9a',1,'stroke="#8a8f9a" stroke-width="6" stroke-linecap="round" fill="none"')+E(0,-12,16,6,'#b9bfc9',.7)},
 guitar:function(d){return sh(30)+R(-20,-8,40,8,'#3a2616',3)+E(0,-40,24,22,'#c98a4a')+E(0,-60,17,16,'#c98a4a')+E(0,-40,8,8,'#2a1a10')+R(-4,-120,8,60,'#6a4426')+R(-8,-128,16,12,'#3a2616',3)+L('M-2 -118 L-2 -42 M2 -118 L2 -42','#e9e4d4',.8)+R(-14,-30,28,5,'#6a4426',2)},
 piano:function(d){return sh(54)+R(-52,-96,104,92,'#1c1f28',4)+R(-52,-98,104,6,'#2a2e3a',3)+R(-46,-66,92,26,'#f4f1e8',1)+[].concat(Array(11)).map(function(_,i){return R(-46+i*8.4+5,-66,4,16,'#14161c',1)}).join('')+R(-46,-92,92,22,'#2a2e3a',2)+R(-50,-4,100,4,'#0a0b10')+R(-48,-40,6,36,'#14161c')+R(42,-40,6,36,'#14161c')},
 globe:function(d){var g=G([[0,'#6fb6f0'],[1,'#2a5a9a']],.2,0,.8,1);d.push(g.def);return sh(26)+R(-3,-30,6,28,'#6a4a2a')+E(0,-3,16,4,'#4a3220')+'<circle cx="0" cy="-62" r="30" fill="url(#'+g.id+')"/>'+P('M-18 -72 Q-6 -84 4 -76 Q-2 -64 -14 -62 Q-22 -64 -18 -72Z','#4aa860')+P('M8 -58 Q20 -66 26 -54 Q18 -44 8 -50Z','#4aa860')+L('M-30 -62 Q0 -50 30 -62','#fff',1,'opacity=".4"')+L('M-24 -42 A30 30 0 0 0 24 -42','#c9a24a',3)},
 backpack:function(d){return sh(30)+P('M-26 -8 Q-30 -60 -14 -74 Q0 -80 14 -74 Q30 -60 26 -8Z','#d9694a')+R(-16,-40,32,26,'#b5493a',5)+R(-12,-34,24,3,'#f4c24a')+L('M-14 -74 q0 -16 14 -16 q14 0 14 16','#8a3a2a',4)+R(-24,-30,6,16,'#8a3a2a',3)+R(18,-30,6,16,'#8a3a2a',3)},
 trophy:function(d){var g=G([[0,'#ffe27a'],[1,'#c9922a']],0,0,1,0);d.push(g.def);return sh(26)+R(-20,-14,40,14,'#3a2a1a',3)+R(-5,-34,10,22,'url(#'+g.id+')')+P('M-24 -92 Q-24 -52 0 -48 Q24 -52 24 -92Z','url(#'+g.id+')')+L('M-24 -86 q-14 0 -12 14 q2 10 14 10 M24 -86 q14 0 12 14 q-2 10 -14 10','#c9922a',4)+P('M-14 -88 Q-14 -64 -6 -58','#fff',.5,'stroke="#fff" stroke-width="3" fill="none" opacity=".5"')},
 balloons:function(d){var c=['#e0525a','#f2c24a','#3d9ad8','#58b868','#a85aa8'],o='';c.forEach(function(k,i){var x=-26+i*14,y=-120-(i%2)*14;o+=L('M'+(x*.2)+' -4 Q'+(x*.5)+' -50 '+x+' '+(y+22),'#ccc',1)+E(x,y,13,16,k)+E(x-4,y-5,3.4,5,'#fff',.4)+P('M'+x+' '+(y+16)+' l-3 5 h6Z',k)});return sh(10)+o},
 clock:function(d){return sh(24)+R(-18,-150,36,146,'#6a4426',5)+R(-22,-156,44,12,'#4a2f1a',3)+E(0,-128,15,15,'#f6efe4')+L('M0 -128 L0 -138 M0 -128 L8 -124','#2a2a2a',2)+R(-12,-104,24,66,'#3a2616',3)+E(0,-66,7,7,'#d9b44a')},
 bench:function(d){return sh(54)+R(-52,-44,104,8,'#a97c50',3)+R(-52,-30,104,8,'#a97c50',3)+R(-52,-60,104,8,'#a97c50',3)+R(-48,-22,6,22,'#3a2c22')+R(42,-22,6,22,'#3a2c22')+R(-52,-60,4,40,'#3a2c22')+R(48,-60,4,40,'#3a2c22')},
 camera:function(d){return sh(30)+L('M0 -62 L-26 -2 M0 -62 L26 -2 M0 -62 L0 -2','#3a3f4a',3.4)+R(-24,-92,48,32,'#2b2f3a',6)+E(0,-76,11,11,'#14161c')+E(0,-76,6,6,'#3d7fb8')+E(-3,-79,2,2,'#fff',.8)+R(14,-98,10,6,'#c0453a',2)+R(-18,-98,14,6,'#2b2f3a',2)},
 microphone:function(d){return sh(24)+R(-14,-6,28,6,'#2b2f3a',3)+R(-2,-86,4,80,'#8a929c')+E(0,-100,12,16,'#2b2f3a')+E(0,-100,9,13,'#6a727c')+L('M-8 -104 h16 M-8 -98 h16 M-8 -92 h16','#2b2f3a',1.2)},
 easel:function(d){return sh(36)+L('M-24 -2 L-8 -118 M24 -2 L8 -118 M0 -2 L0 -110','#8a5a2a',4)+R(-30,-96,60,42,'#f4efe4',2)+P('M-30 -54 L-12 -78 L0 -64 L14 -86 L30 -54Z','#4a9b6a',.9)+E(10,-84,6,6,'#f2c24a')+R(-24,-40,48,4,'#8a5a2a')+E(-10,-46,3,3,'#e0525a')+E(0,-46,3,3,'#3d7fb8')+E(10,-46,3,3,'#f2c24a')},
 telescope:function(d){return sh(30)+L('M0 -2 L-20 -44 M0 -2 L20 -44 M0 -2 L0 -46','#3a3f4a',3.4)+P('M-30 -56 L24 -78 L30 -64 L-24 -42Z','#c9d0dc')+P('M-30 -56 L-24 -42 L-36 -40 L-42 -54Z','#7a8294')+E(-36,-47,5,8,'#bfe6ff',.7)},
 cake:function(d){return sh(40)+R(-38,-50,76,6,'#a97c50',3)+R(-3,-44,6,42,'#6a4a2c')+R(-24,-70,48,20,'#f2c2a8',4)+P('M-24 -70 q6 8 12 0 q6 8 12 0 q6 8 12 0 q6 8 12 0 L24 -74 L-24 -74Z','#fff')+R(-1,-86,2,16,'#e0525a')+E(0,-90,3,5,'#ffd24a')+E(-12,-62,3,3,'#e0525a')+E(0,-60,3,3,'#e0525a')+E(12,-62,3,3,'#e0525a')},
 basket:function(d){return sh(34)+P('M-30 -4 L-24 -34 L24 -34 L30 -4Z','#b98a52')+L('M-26 -26 h52 M-27 -18 h54 M-28 -10 h56','#8a6032',1.6)+L('M-22 -34 Q0 -76 22 -34','#8a6032',3.4)+E(-10,-40,8,6,'#d9473a')+E(6,-41,8,6,'#f2c24a')+E(18,-39,6,5,'#6ab04c')+R(-30,-36,60,4,'#a97c3a',2)},
 campfire:function(d){return sh(30)+L('M-26 -6 L22 -16 M26 -6 L-22 -16','#5a3a22',7)+P('M-14 -16 Q-18 -44 -4 -58 Q0 -42 8 -52 Q22 -34 14 -16Z','#f08a2a')+P('M-8 -16 Q-10 -34 0 -44 Q10 -32 6 -16Z','#ffd860')+E(0,-14,22,5,'#14100c',.5)},
 ball:function(d){return sh(20)+'<circle cx="0" cy="-24" r="22" fill="#f4f4f2"/>'+P('M0 -36 l10 7 -4 12 h-12 l-4 -12Z','#2a2a2a')+L('M-22 -24 q6 -10 12 -12 M22 -24 q-6 -10 -12 -12 M-10 -9 q-8 2 -10 -6 M10 -9 q8 2 10 -6','#2a2a2a',1.2)+P('M-22 -30 A22 22 0 0 1 4 -46','#fff',.6,'stroke="#fff" stroke-width="3" fill="none"')},
 plantpot:function(d){return sh(24)+P('M-16 -34 L16 -34 L12 -2 L-12 -2Z','#c06a40')+R(-18,-38,36,6,'#d98a56',2)+[-3,-2,-1,0,1,2,3].map(function(a){return L('M0 -38 Q'+(a*10)+' -64 '+(a*14)+' '+(-70+Math.abs(a)*5),'#2f7a46',3)+E(a*14,-72+Math.abs(a)*5,6,13,'#3d9a56')}).join('')}
};
var PROPS=[
 ['coffee',/coffee|tea\b|caf[eé]|breakfast|latte|barista|drink|brunch/],['books',/\bbooks?\b|read|library|novel|author|story|diary|poem|literature|writer|letter/],
 ['laptop',/laptop|computer|e-?mail|online|internet|office|\bwork\b|project|deadline|software|screen|website|\bapp\b|password/],['pizza',/pizza|dinner|lunch|menu|\beat\b|food|restaurant|order|hungry|meal|pasta|burger/],
 ['flowers',/flower|garden|\brose\b|wedding|\blove\b|bouquet|spring|bloom|valentine|date\b/],['tv',/\btv\b|television|show|series|channel|news|sitcom|episode|program|remote/],
 ['bicycle',/bike|bicycle|cycling|\bride\b/],['car',/\bcar\b|drive|driver|taxi|traffic|highway|road|garage|speed/],
 ['suitcase',/suitcase|luggage|travel|trip|passport|journey|airport|vacation|holiday|hotel|tourist|baggage/],['umbrella',/umbrella|\brain|storm|weather|drizzle|forecast/],
 ['dog',/\bdog|puppy|\bpet\b|bark|leash|walk the/],['cat',/\bcat\b|kitten|meow/],['guitar',/guitar|\bsong|\bband\b|sing|rock\b|music|lyrics|concert|album/],['piano',/piano|opera|melody|orchestra|musical|classical/],
 ['globe',/globe|world|country|\bmap\b|geography|abroad|culture|international/],['backpack',/backpack|school|student|class|study|homework|exam|teacher|university/],
 ['trophy',/trophy|champion|prize|award|medal|\bwin\b|winner|race\b|contest|victory/],['balloons',/balloon|party|birthday|celebrat|festival|congrat|surprise|anniversary|carnival/],
 ['clock',/\bclock|\btime\b|\blate\b|\bhour|schedule|\bago\b|watch\b|punctual|midnight|alarm/],['bench',/\bbench|\bpark\b|\bsit\b|\bwait|picnic|sunday/],
 ['camera',/camera|photo|picture|film|movie|photograph|cinema|selfie|tourist/],['microphone',/microphone|speech|interview|podcast|\btalk\b|radio|presentation|announce|opinion|debate/],
 ['easel',/easel|paint|\bart\b|painting|artist|draw|museum|gallery|canvas|color/],['telescope',/telescope|space|\bstar|galaxy|planet|moon|astronaut|universe/],
 ['cake',/\bcake|bakery|dessert|sugar|\bbake|cookie|sweet|candy|chocolate/],['basket',/basket|fruit|market|shopping|grocery|vegetable|apple|harvest/],
 ['campfire',/campfire|\bcamp\b|\bfire\b|cabin|fireplace|marshmallow|warm/],['ball',/\bball\b|soccer|football|basketball|sport|\bgame\b|\bteam\b|goal\b|match|coach|player/],
 ['plantpot',/plant|green|leaf|tree|nature|fresh|grow/]
];
var PLACE={cafe:'a cozy modern coffee shop',library:'a warm old library full of books',kitchen:'a bright home kitchen',living:'a comfortable living room',office:'a modern office',classroom:'a school classroom',street:'a lively city street',park:'a green city park',forest:'an enchanted forest',lake:'a mountain lake',lobby:'a hotel lobby',shop:'a small shop',bedroom:'a cozy bedroom',studio:'a recording studio',bakery:'a neighborhood bakery',museum:'an art museum',hospital:'a hospital room',courtroom:'a courtroom',restaurant:'an elegant restaurant',harbor:'a harbor with boats',farm:'a countryside farm',village:'a european old town',castle:'a castle on a hill',beach:'a sunny beach',snow:'a snowy winter landscape',airport:'an airport terminal',station:'a train station platform',theater:'a theater stage',desert:'a desert highway',gym:'a modern gym',cinema:'a movie theater',subway:'a subway platform',bridge:'a city bridge over the river',temple:'a japanese temple garden',cabin:'a cabin with a fireplace',rain:'a rainy night street',skyline:'a city skyline',rooftop:'a city rooftop',space:'a space station',airport2:''};
var TODTXT={day:'bright daylight',gold:'warm golden hour light',night:'night, with soft artificial lights'};
var SL={interior:[[.09,.80],[.91,.80],[.23,.82],[.79,.82]],exterior:[[.08,.82],[.92,.82],[.22,.84],[.80,.84]]};
var EXT={street:1,skyline:1,village:1,desert:1,lake:1,forest:1,castle:1,harbor:1,beach:1,farm:1,snow:1,space:1,station:1,airport:0,park:1,rooftop:1,bridge:1,temple:1,rain:1};
function hash(s){var h=7;s=String(s);for(var i=0;i<s.length;i++)h=(h*31+s.charCodeAt(i))>>>0;return h}
function words(e){var v=(e&&e.v)||[],o=[];for(var i=0;i<v.length;i++){var w=v[i];o.push(Array.isArray(w)?w[0]:(w&&w.w)||w)}return o.join(' ')}
function brief(e,rs){
  if(!e||!window.PogPaint)return null;
  var pk=PogPaint.pick(rs||'street',e);if(!pk)return null;
  var a=e.a||{},strong=(String(e.t||'')+' '+String(a.w||'')).toLowerCase(),weak=words(e).toLowerCase(),hay=strong+' '+weak,p=[],i;
  for(i=0;i<PROPS.length&&p.length<3;i++)if(PROPS[i][1].test(strong))p.push(PROPS[i][0]);
  for(i=0;i<PROPS.length&&p.length<3;i++)if(p.indexOf(PROPS[i][0])<0&&PROPS[i][1].test(weak))p.push(PROPS[i][0]);
  var h=hash((e.uid||e.n||e.t)+'p');if(!p.length)p.push(['plantpot','bench','books','coffee','clock','ball'][h%6]);
  var w=/\brain|storm|drizzle|umbrella|thunder/.test(strong)?'rain':/snow|blizzard|winter|frozen|christmas/.test(strong)?'snow':/fog|mist|ghost|haunt|spook|eerie|mystery|creep/.test(hay)?'fog':'';
  var th=pk.theme,place=PLACE[th]||th;
  var prompt='Cinematic realistic digital painting of '+place+', '+TODTXT[pk.name.split('-').pop()]+(w?', '+({rain:'rainy weather with wet reflections',snow:'falling snow',fog:'soft atmospheric fog'}[w]):'')+', with '+p.join(', ').replace(/plantpot/,'a potted plant')+' in the scene, inspired by the story "'+(a.w||e.t||'')+'" (lesson: '+(e.t||'')+'), detailed, soft natural light, depth of field, no text, 16:9';
  return {theme:th,image:pk.name,flip:pk.flip,hue:pk.hue,tod:pk.name.split('-').pop(),weather:w,props:p,place:place,prompt:prompt,ext:!!EXT[th]};
}
function layer(b,seed){
  var d=[],o='',slots=(b.ext?SL.exterior:SL.interior).slice(),h=hash(seed||b.image);
  if(h&1)slots.reverse();
  var tint=b.tod==='night'?'brightness(.62) saturate(.85)':b.tod==='gold'?'sepia(.18) saturate(1.1) brightness(.97)':'none';
  b.props.forEach(function(k,i){var f=S[k];if(!f||!slots[i])return;var def=[],g=f(def);var s=(k==='clock'?.95:k==='car'?.9:1)*(.95+(hash(k+seed)%20)/100);var x=slots[i][0]*800,y=slots[i][1]*450;d=d.concat(def);o+='<g transform="translate('+x.toFixed(0)+' '+y.toFixed(0)+') scale('+s.toFixed(2)+')">'+g+'</g>'});
  var wx='';
  if(b.weather==='rain'){for(var j=0;j<70;j++){var rx=(hash('r'+j+seed)%800),ry=(hash('q'+j+seed)%450);wx+='<line x1="'+rx+'" y1="'+ry+'" x2="'+(rx-5)+'" y2="'+(ry+20)+'" stroke="#dbe8ff" stroke-opacity=".38" stroke-width="1.2"/>'}wx='<g class="ps-rain">'+wx+'</g>'}
  else if(b.weather==='snow'){for(var j2=0;j2<60;j2++){wx+='<circle cx="'+(hash('s'+j2+seed)%800)+'" cy="'+(hash('t'+j2+seed)%450)+'" r="'+(1+(j2%3)*.7)+'" fill="#fff" opacity=".8"/>'}wx='<g class="ps-snow">'+wx+'</g>'}
  else if(b.weather==='fog'){wx='<rect y="200" width="800" height="250" fill="url(#spfog)"/>'}
  var fog='<linearGradient id="spfog" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".6" stop-color="#dfe8f4" stop-opacity=".38"/><stop offset="1" stop-color="#fff" stop-opacity=".12"/></linearGradient>';
  return '<svg class="ps-props" viewBox="0 0 800 450" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><defs><filter id="spb" x="-30%" y="-100%" width="160%" height="300%"><feGaussianBlur stdDeviation="3"/></filter>'+fog+d.join('')+'</defs><g style="filter:'+tint+'">'+o+'</g>'+wx+'</svg>';
}
window.PogProps={brief:brief,layer:layer,sprites:S,list:Object.keys(S)};
})();
