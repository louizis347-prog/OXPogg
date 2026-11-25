// Photo sequences follow the actions in the recurring lesson scenes.
const photoSceneTargets={
  cup:{
    reading:['bakery','bread','takeout','counter','payment'],
    dialogue:['counter','bread','cup','takeout','coffeeTable','bakery'],
    continuation:['cup','takeout','water']
  },
  ticket:{
    reading:['ticket','railpass','ticketdesk','board','train'],
    dialogue:['railpass','ticketdesk','square','roundtrip','ticket','board'],
    continuation:['ticket','train','stationSign']
  },
  city:{
    reading:['coast','square','walk','bakery','cup'],
    dialogue:['street','coast','lake','stationPark','walk','coffeeTable'],
    continuation:['bakery','street','walk']
  },
  chat:{
    reading:['friends','message','clock','dinner','restaurant'],
    dialogue:['calendar','clock','dinner','diningRoom','restaurant','friends'],
    continuation:['clock','dinner','restaurant']
  },
  notebook:{
    reading:['classroom','study','deskStudy','pen','paper'],
    dialogue:['notebook','bag','study','book','pen','deskStudy'],
    continuation:['notebook','study','pen']
  },
  park:{
    reading:['walk','park','lake','dusk','street'],
    dialogue:['walk','park','lake','entrance','parkPath','dusk'],
    continuation:['parkPath','walk','water']
  },
  health:{
    reading:['calendar','phone','clinic','pen','hospital'],
    dialogue:['clinic','exam','health','calendar','clock','hospital'],
    continuation:['clinic','calendar','health']
  },
  map:{
    reading:['desk','bread','note','phone','message'],
    dialogue:['map','bakery','note','paper','phone','desk'],
    continuation:['desk','door','luggage']
  }
};
const photoFallBacks={
  bakery:['bread','counter','cup'],bread:['bakery','counter','cup'],takeout:['counter','coffeeTable','cup'],
  water:['coffeeTable','cup'],counter:['coffeeTable','cup'],payment:['counter','cup'],
  roundtrip:['railpass','ticketdesk'],stationSign:['board','ticket'],stationPark:['park','ticket'],
  square:['street','city'],coast:['city','street'],street:['city','square'],
  walk:['parkPath','park','street'],lake:['park','parkPath'],dusk:['parkPath','park'],entrance:['parkPath','park'],
  parkPath:['park'],friends:['dinner','chat'],dinner:['restaurant','chat'],diningRoom:['restaurant','chat'],
  restaurant:['dinner','chat'],calendar:['clock','notebook'],clock:['calendar','notebook'],
  bag:['classroom','notebook'],pen:['deskStudy','notebook'],paper:['note','deskStudy','notebook'],deskStudy:['notebook'],
  classroom:['study','notebook'],study:['classroom','notebook'],book:['deskStudy','notebook'],
  clinic:['health','hospital'],exam:['health','clinic'],hospital:['health','clinic'],
  message:['phone','note'],note:['pen','notebook'],phone:['message','notebook'],
  desk:['map'],door:['desk','map'],luggage:['desk','map'],coffeeTable:['cup']
};
const photoKeywords=[
  ['bakery',/padaria|panadería|bakery/i],['railpass',/passagem|billete|train ticket/i],
  ['takeout',/para viagem|para llevar|to go|takeaway/i],['payment',/\bpag(?:a|ou|ar)\b|paid|payment/i],
  ['bread',/pão|pães|bread|pan\b/i],['cup',/café|coffee|xícara|cup/i],
  ['calendar',/horário|horario|appointment|calend|consulta/i],['hospital',/clínica|clinic|hospital/i],
  ['lake',/lago|pond|lake/i],['dusk',/escurec|anoitec|atardec|sunset|dusk/i],
  ['park',/parque|\bpark\b/i],['coast',/mar\b|coast|sea\b/i],['street',/rua|street|calle/i],
  ['board',/painel|tablero|board\b/i],['train',/trem|tren|train|plataforma|platform/i],
  ['note',/recado|nota\b|note\b/i],['message',/mensage|mensaje|message/i],['phone',/liga(?:r|ção|da)|telefone|teléfono|phone/i],
  ['pen',/escrev|escrib|\bwrite|anot/i],['notebook',/caderno|cuaderno|notebook/i],
  ['book',/leitura|livro|libro|book|página|page/i],['bag',/mochila|backpack/i],
  ['dinner',/jantar|cena\b|dinner/i],['friends',/amig|friend/i],['door',/elevador|elevator|ascensor/i]
];
const relatedPhotoThemes={
  cup:['chat','city'],ticket:['city','map'],city:['park','cup'],chat:['cup','notebook'],
  notebook:['map','chat'],park:['city','chat'],health:['notebook','map'],map:['ticket','notebook']
};
function photoForMoment(theme,index,kind,text='',used){
  if(mangaPilot())return mangaMoment(index,kind);
  const scenes=photoSceneTargets[theme]||photoSceneTargets.map;
  const sequence=scenes[kind]||scenes.reading;
  const keyword=photoKeywords.find(([,pattern])=>pattern.test(text))?.[0];
  const plan=englishLessonPlan();
  if(plan&&!plan.file)return null;
  if(plan){
    const cover=englishPlanPhoto(plan);
    const related=[...new Set(Object.values(scenes).flat())].filter(key=>!['coast','walk','lake','parkPath','stationPark','dusk','street','bakery','cup','coffeeTable','square'].includes(key)||['city','park','cup'].includes(theme));
    if(unit===4)related.splice(0,related.length,'book','deskStudy','pen','paper');
    const photos=[cover,...related.flatMap(key=>[...(lessonPhotoPool[key]||[]),lessonPhotos[key]].filter(Boolean))];
    const position=keyword&&related.includes(keyword)?photos.findIndex(photo=>lessonPhotoPool[keyword]?.some(candidate=>candidate.file===photo.file)):-1;
    const preferred=position>=0?photos[position]:photos[index%photos.length];
    const available=used?.has(preferred.file)?photos.find(photo=>!used.has(photo.file))||preferred:preferred;
    used?.add(available.file);
    return available;
  }
  const arranged=sequence[index%sequence.length];
  const topical=['continuation','reading','dialogue'].includes(kind);
  const primary=topical&&(unit!==0||kind==='continuation')?arranged:keyword||arranged;
  const candidates=[primary,keyword,...(photoFallBacks[primary]||[]),...sequence,theme];
  if(used&&(kind==='example'||kind==='grammar'||kind==='section'||kind==='preview')){
    const related=(relatedPhotoThemes[theme]||relatedPhotoThemes.map).map(key=>photoSceneTargets[key]);
    candidates.push(...Object.values(scenes).flat(),...related.flatMap(scene=>Object.values(scene).flat()));
  }
  const photos=candidates.flatMap(key=>{
    if(!key)return [];
    const bank=[...(lessonPhotoPool[key]||[]),lessonPhotos[key]].filter(Boolean);
    if(!bank.length||topical)return bank;
    const offset=index%bank.length;
    return [...bank.slice(offset),...bank.slice(0,offset)];
  });
  if(!photos.length)return lessonPhotos.map;
  const available=photos.find(photo=>!used?.has(photo.file))||photos[0];
  used?.add(available.file);
  return available;
}
function lessonPhotoFrame(photo,className,priority=false){
  if(mangaPilot())return mangaFigure(photo?.manga?photo:mangaMoment(0,className==='lesson-hero-photo'?'scene':'thumb'),className,priority);
  if(!photo)return '';
  const alt=routeLabel(...photo.alt);
  return '<figure class="'+className+'"><img src="'+clean(photo.file)+'" alt="'+clean(alt)+'" width="'+photo.width+
    '" height="'+photo.height+'" decoding="async"'+(priority?' fetchpriority="high"':' loading="lazy"')+'></figure>';
}
function lessonSectionPhoto(theme,kind,used){
  return lessonPhotoFrame(photoForMoment(theme,kind==='grammar'?2:0,kind,'',used),'lesson-section-photo');
}
