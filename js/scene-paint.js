/* Cenários pintados por tema da aula: escolhe uma das imagens de img/scenes (tema × hora do dia) a partir da obra, do título e do vocabulário.
   Substitui o fundo desenhado dos quadros; mesma imagem em todos os quadros do episódio (consistência) e variação entre episódios. */
(function(){
'use strict';
var R=[ /* [tema, regex] em ordem de prioridade; testado primeiro na obra/título, depois no vocabulário */
 ['temple',/japan|tokyo|kyoto|temple|samurai|korea|seoul|china|chinese|asian|sakura|ghibli|spirited|anime|ninja|k-?pop/],
 ['gym',/\bgym\b|workout|exercise|fitness|training|muscle|boxing|rocky|yoga|stretch|sweat|trainer|warm up/],
 ['bakery',/bakery|\bbread\b|\bcake\b|pastry|donut|cookie|dessert|croissant|cupcake|muffin/],
 ['cinema',/cinema|movie theat|premiere|popcorn|film studio|screening|projector|blockbuster/],
 ['subway',/subway|metro\b|underground|\btube\b|tram\b|commuter|rush hour/],
 ['bridge',/\bbridge|golden gate|river crossing|overpass/],
 ['cabin',/cabin|fireplace|cozy|hearth|chimney|cottage|christmas carol|log fire|wood stove/],
 ['rain',/\brain|storm|umbrella|drizzle|thunder|downpour/],
 ['space',/star trek|star wars|alien\b|space|galaxy|planet|martian|gravity|astronaut|moon landing|rocket|telescope|interstellar|tomorrowland|terminator|sci-?fi|spaceship|mars\b/],
 ['desert',/mad max|desert|sahara|dune|route 66|road trip|western|cowboy|wild west|duel|outlaw|canyon/],
 ['castle',/lord of the rings|hobbit|castle|princess|knight|fairy|macbeth|hamlet|cinderella|beowulf|throne|dragon|harry potter|game of thrones|camelot|medieval|witch|wizard|pinocchio|shrek|rapunzel|sleeping beauty/],
 ['forest',/alice|wonderland|robin hood|forest|woods|hansel|snow white|goldilocks|wizard of oz|peter pan|neverland|jungle|bambi|red riding|mushroom|enchanted|fox\b|wolf|bear\b|goat/],
 ['snow',/snow|winter|frozen|christmas|santa|polar|arctic|shackleton|blizzard|north pole/],
 ['harbor',/\bship\b|titanic|pirate|\bsea\b|ocean|sailor|\bboat|moby|harbor|harbour|treasure|odyssey|voyage|lighthouse|navigat|captain|whale|shark|cruise|canal/],
 ['beach',/beach|surf|tropical|hawaii|ipanema|island|castaway|swim|summer|coast/],
 ['lake',/mountain|lake\b|climb|everest|walden|alps|heidi|sound of music|hiking|trail|camp|river|waterfall|canyon|wild\b|nature|summit/],
 ['farm',/farm|barn|animal farm|charlotte|\bbabe\b|harvest|wheat|little house|countryside|cow\b|chicken|rural|garden/],
 ['airport',/airport|flight|\bplane|pilot|passport|top gun|terminal|boarding|luggage|customs|wright brothers|airline|check in|jet lag/],
 ['station',/train|station|railway|orient express|subway|platform|commute|brief encounter|ticket|bus stop|timetable/],
 ['rooftop',/rooftop|noir|blade runner|detective|sherlock|mystery|night city|spy|heist|crime|thriller/],
 ['skyline',/new york|manhattan|brooklyn|gatsby|sex and the city|batman|spider|superman|wall street|skyline|chicago|city life|metropolis|nyc/],
 ['village',/paris|italy|rome\b|venice|tuscan|village|europe|amelie|spain|portugal|lisbon|marseille|french|italian|spanish|madrid|barcelona|london|england|british|old town/],
 ['park',/park\b|picnic|bench|central park|jogging|football|soccer|baseball|basketball|olympic|sport|race\b|running|playground|dog\b|pet\b|outdoor/],
 ['courtroom',/court|judge|trial|lawyer|jury|verdict|legal|witness|lawsuit|objection|prosecutor|contract|clause/],
 ['hospital',/hospital|doctor|nurse|health|medic|patient|sick|pharmacy|surgeon|symptom|cold\b|cough|fever|headache|allerg|clinic/],
 ['theater',/theat(er|re)|stage|opera|musical|\bplay\b|actor|broadway|ballet|phantom|hamilton|performance|audition|dance|concert|curtain|cinema|movie|film\b|drama/],
 ['museum',/museum|painting|gallery|exhibit|monet|van gogh|mona lisa|louvre|statue|sculpture|ancient|egypt|artist|canvas|history/],
 ['studio',/podcast|radio|album|record\b|\bband\b|singer|guitar|\bdj\b|studio|beatles|news\b|journal|talk show|broadcast|microphone|song|music\b|headline|interview/],
 ['classroom',/school|class\b|classroom|teacher|student|exam|homework|university|college|lesson|dead poets|matilda|professor|study|quiz|grade/],
 ['library',/library|bookshop|novel|\bbooks?\b|author|writer|poem|literature|shakespeare|dickens|austen|reading|read\b|diary|letter|manuscript|story/],
 ['restaurant',/restaurant|menu|waiter|wine\b|dinner|order food|bistro|reservation|chef\b|tasting|banquet|feast/],
 ['kitchen',/kitchen|cook|recipe|bake|baking|ratatouille|masterchef|pasta|soup|sugar|flour|oven|ingredient|stir\b|whisk|simmer/],
 ['cafe',/caf[eé]|coffee|\btea\b|diner|brunch|bakery|breakfast|friends\b|barista|sandwich|latte/],
 ['shop',/shop|store|market|\bbuy|mall|supermarket|\bsale\b|clothes|fashion|price|customer|grocery|refund|receipt|discount|shopping/],
 ['office',/office|\bjob\b|\bwork\b|boss|meeting|e-?mail|business|career|devil wears prada|the office|suits|manager|colleague|deadline|presentation|startup|resume|salary|project/],
 ['lobby',/hotel|lobby|reception|check-?in|apartment|building|grand budapest|bank\b|elevator|concierge|front desk/],
 ['bedroom',/\bbed\b|sleep|bedroom|dream|pajama|insomnia|morning routine|wake up|night\b|alarm/],
 ['living',/home\b|house|family|living room|\bsofa|\btv\b|sitcom|roommate|neighbo|furniture|friends and|chores/]
];
var NV={cafe:2,library:2,kitchen:2,living:2,office:2,classroom:2,street:2,park:2,forest:1,lake:1,lobby:2,shop:1,bedroom:1,studio:1,bakery:1,museum:1,hospital:1,courtroom:1,restaurant:1,harbor:1,farm:1,village:1,castle:1,beach:1,snow:1,airport:1,station:1,theater:1,desert:1,gym:1,cinema:1,subway:1};
var BYRS={cafe:'cafe',cafe2:'cafe',cafe3:'cafe',diner:'cafe',pizzeria:'cafe',library:'library',lake:'lake',forest:'forest',kitchen:'kitchen',street:'street',city:'street',plaza:'street',office:'office',meetingroom:'office',living:'living',home1:'living',home2:'living',lobby1:'lobby',hall:'lobby',school:'classroom',yard:'park',park:'park',park2:'park',garden:'park',shop:'shop',market:'shop',bookshop:'library',bedroom:'bedroom',pier:'harbor',harbor:'harbor',coast:'harbor',museum:'museum',mountain:'lake',station:'station',castlehall:'castle',musicroom:'studio',nightcity:'skyline',restaurant:'restaurant',stage:'theater',outdoors:'park',workshop:'office'};
var WEAK={library:1,kitchen:1,cafe:1,shop:1,office:1,classroom:1,hospital:1,courtroom:1,restaurant:1,bakery:1,gym:1,living:1,bedroom:1,lobby:1,museum:1,studio:1,airport:1,station:1,park:1};
var POOL=['street','cafe','park','living','office','library','shop','kitchen','classroom','lobby','bedroom','restaurant','village','bakery','museum','studio','lake','forest','harbor','farm'];
var TOD=['day','gold','day','night','gold','day'];
function hash(s){var h=7;s=String(s);for(var i=0;i<s.length;i++)h=(h*31+s.charCodeAt(i))>>>0;return h}
function words(e){var v=(e&&e.v)||[],o=[];for(var i=0;i<v.length;i++){var w=v[i];o.push(Array.isArray(w)?w[0]:(w&&w.w)||w)}return o.join(' ')}
function themeOf(e,rs){
  if(!e)return BYRS[rs]||'street';
  if(e._pt)return e._pt;
  var a=e.a||{},strong=(String(e.t||'')+' '+String(a.w||'')+' '+String(a.k||'')).toLowerCase(),weak=words(e).toLowerCase(),t=null,i;
  for(i=0;i<R.length&&!t;i++)if(R[i][1].test(strong))t=R[i][0];
  var base=BYRS[rs];
  if(!t&&base&&base!=='street')t=base;
  for(i=0;i<R.length&&!t;i++)if(WEAK[R[i][0]]&&R[i][1].test(weak))t=R[i][0];
  if(!t)t=POOL[hash(e.uid||e.n||e.t)%POOL.length];
  try{e._pt=t}catch(x){}
  return t;
}
var OK=null;
function themes(){return OK}
function pick(rs,ep){
  var e=ep||(typeof P!=='undefined'&&P&&P.e)||null;if(!e&&!BYRS[rs])return null;
  var t=themeOf(e,rs),h=hash((e&&(e.uid||e.n||e.t))||rs),tod=TOD[h%TOD.length];
  if(t==='skyline'||t==='rooftop'||t==='studio'||t==='theater'||t==='space')tod=(h&1)?'night':'gold';
  if(t==='studio'||t==='theater'||t==='space'||t==='cinema'||t==='gym')tod='night';
  if(t==='cabin'||t==='rain'||t==='subway')tod=t==='subway'?'day':'night';
  var nv=NV[t]||0,v=nv?((h>>7)%(nv+1)):0;
  return {name:t+(v?'-v'+v:'')+'-'+tod,flip:(h>>3)&1,hue:((h>>5)%5-2)*6,theme:t};
}
window.PogPaint={
  theme:themeOf,pick:pick,
  bg:function(rs,ep){
    try{
      var e=ep||(typeof P!=='undefined'&&P&&P.e)||null;if(!e&&!BYRS[rs])return '';
      var t=themeOf(e,rs),h=hash((e&&(e.uid||e.n||e.t))||rs),tod=TOD[h%TOD.length];
      if(t==='skyline'||t==='rooftop'||t==='studio'||t==='theater'||t==='space')tod=(h&1)?'night':'gold';
      if(t==='studio'||t==='theater'||t==='space'||t==='cinema'||t==='gym')tod='night';if(t==='cabin'||t==='rain'||t==='subway')tod=t==='subway'?'day':'night';
      var flip=(h>>3)&1,hue=((h>>5)%5-2)*6;
      var nv=NV[t]||0,v=nv?((h>>7)%(nv+1)):0,nm=t+(v?'-v'+v:'')+'-'+tod;
      return '<img class="ps-paint" src="img/scenes/'+nm+'.webp" width="1024" height="576" alt="" decoding="async" draggable="false" style="'+(flip?'transform:scaleX(-1);':'')+'filter:hue-rotate('+hue+'deg) saturate(1.04)">';
    }catch(x){return ''}
  }
};

function patchCovers(){
  var C=window.PogCover;if(!C||C._pp)return;C._pp=1;var og=C.svg;
  C.svg=function(e,o){
    try{
      o=o||{};if(!e||o.noPaint||!e.fr||!e.a)return og.apply(this,arguments);
      var k=pick((e.stage&&e.stage.rs)||'street',e);if(!k)return og.apply(this,arguments);
      var num=(o.num!=null&&!o.noNum)?'<g transform="translate(14 14)"><rect width="46" height="30" rx="15" fill="rgba(10,16,30,.62)"/><text x="23" y="21" text-anchor="middle" font-family="Plus Jakarta Sans,system-ui,sans-serif" font-weight="800" font-size="16" fill="#fff">'+String(o.num).replace(/[<>&]/g,'')+'</text></g>':'';
      return '<svg viewBox="0 0 400 225" preserveAspectRatio="xMidYMid slice" role="img" aria-label="'+String(e.t||'').replace(/[<>&"]/g,'')+'"><g'+(k.flip?' transform="translate(400 0) scale(-1 1)"':'')+'><image href="img/scenes/'+k.name+'.webp" width="400" height="225" preserveAspectRatio="xMidYMid slice" style="filter:hue-rotate('+k.hue+'deg) saturate(1.04)"/></g>'+num+'</svg>';
    }catch(x){return og.apply(this,arguments)}
  };
}
patchCovers();document.addEventListener('DOMContentLoaded',patchCovers);setTimeout(patchCovers,0);setTimeout(patchCovers,800);
})();
