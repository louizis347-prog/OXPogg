const cacheName='pogolo-dict-2026-11-25-v32';
const allowed=['eng','spa','ita','deu','ara','jpn','por','cmn'];
const shell=[
 './','index.html','style.css','platypus.svg','icon-192.png','icon-512.png','manifest.webmanifest',
 'lessons.js','practice-data.js','curriculum.js','reading-data.js','lesson-reading.js',
 'grammar-examples.js','grammar-panel.js','lesson-vocabulary.js','stories.js','lexicon-review.js',
 'portuguese-course.js','sense-notes.js','study-tools.js','practice-ui.js','mandarin-course.js',
 'mandarin-pinyin.js','more-opening.js','more-grammar.js','extra-reviewed.js','writing.js','data-loader.js',
 'theme-scenes.js','theme-lesson.js','professional.js','lesson-screens.js','lesson-photos.js','placement-data.js','placement.js','lesson-audio.js','lesson-media.js','scene-photo-pool.js','scene-photography.js','pronunciation.js','scene-extension.js','scene-dialogue-practice.js','roleplay-writing.js','lesson-progression.js','lesson-focus.js','word-use.js','distinct-lesson.js','english-a1-plan.js','english-a1-content.js','english-a1-extra.js','english-a2.js','english-a2-extra.js','english-b1.js','english-extra-words.js','a1-pronunciation-data.js','a1-pronunciation-lab.js','plano-ingles-a1-01-50.csv','app.js',
 'lesson-cup.webp','lesson-ticket.webp','lesson-city.webp','lesson-chat.webp','lesson-notebook.webp','lesson-park.webp','lesson-health.webp','lesson-map.webp',
 'photo-bakery-1.webp','photo-bakery-2.webp','photo-bread-1.webp','photo-takeout-1.webp','photo-takeout-2.webp',
 'photo-counter-1.webp','photo-counter-2.webp','photo-payment-1.webp','photo-train-1.webp','photo-train-2.webp',
 'photo-ticketdesk-1.webp','photo-ticketdesk-2.webp','photo-railpass-1.webp','photo-railpass-2.webp','photo-board-1.webp',
 'photo-board-2.webp','photo-coast-1.webp','photo-coast-2.webp','photo-square-1.webp','photo-lake-1.webp',
 'photo-lake-2.webp','photo-walk-1.webp','photo-dusk-1.webp','photo-dusk2-1.webp','photo-entrance-1.webp',
 'photo-friends-1.webp','photo-message-1.webp','photo-clock-1.webp','photo-dinner-1.webp','photo-dinner-2.webp',
 'photo-restaurant-1.webp','photo-restaurant-2.webp','photo-classroom-1.webp','photo-classroom-2.webp','photo-study-1.webp',
 'photo-pen-1.webp','photo-pen-2.webp','photo-bag-1.webp','photo-phone-1.webp','photo-calendar-1.webp',
 'photo-hospital-1.webp','photo-hospital-2.webp','photo-note-1.webp','photo-door-1.webp','photo-luggage-1.webp',
 'photo-water-1.webp','photo-coffeeTable-1.webp','photo-street-1.webp','photo-parkPath-1.webp','photo-deskStudy-1.webp',
 'photo-clinic-1.webp','photo-desk-1.webp','photo-stationSign-1.webp','photo-stationPark-1.webp','photo-roundtrip-1.webp',
 'photo-paper-1.webp','photo-book-1.webp'
];
const a1AudioFiles=Array.from({length:126},(_,i)=>'a1-audio/'+String(i+1).padStart(3,'0')+'.mp3');
shell.push(...a1AudioFiles);
shell.push('manga-art.js');
const mangaFiles=Array.from({length:20},(_,i)=>'manga/a1-'+String(i+1).padStart(2,'0')+'.webp');
const mangaThumbs=Array.from({length:20},(_,i)=>'manga/thumbs/a1-'+String(i+1).padStart(2,'0')+'.webp');
const a1AudioPaths=new Set(a1AudioFiles.map(file=>new URL(file,self.registration.scope).pathname));
const urls=new Set([...shell,...mangaFiles,...mangaThumbs].map(file=>new URL(file,self.registration.scope).pathname));
function isData(path){
  return /^\/(eng|spa|ita|deu|ara|jpn|por|cmn)(-(examples|third|audit|support|forms))?\.json$/.test(path)||
    /^\/stories-(pt|eng|spa|ita|deu|ara|jpn|cmn)\.json$/.test(path);
}
function valid(response,path){
  if(!response||!response.ok||response.redirected)return false;
  const content=response.headers.get('content-type')||'';
  return !path.endsWith('.json')||content.includes('json');
}
async function cachedAudioRange(response,header){
  if(!header)return response;
  const range=/^bytes=(\d+)-(\d*)$/.exec(header);
  if(!range)return response;
  const bytes=await response.arrayBuffer();
  const start=Number(range[1]);
  const end=range[2]?Math.min(Number(range[2]),bytes.byteLength-1):bytes.byteLength-1;
  if(start>end)return new Response(null,{status:416,headers:{'Content-Range':'bytes */'+bytes.byteLength}});
  return new Response(bytes.slice(start,end+1),{status:206,headers:{
    'Content-Type':'audio/mpeg','Accept-Ranges':'bytes',
    'Content-Range':'bytes '+start+'-'+end+'/'+bytes.byteLength,
    'Content-Length':String(end-start+1)
  }});
}
self.addEventListener('install',event=>event.waitUntil((async()=>{
  const cache=await caches.open(cacheName);
  await cache.addAll(shell);
  await self.skipWaiting();
})()));
self.addEventListener('activate',event=>event.waitUntil((async()=>{
  for(const key of await caches.keys())if((key.startsWith('pogglodict-')||key.startsWith('pogolo-dict-'))&&key!==cacheName)await caches.delete(key);
  await self.clients.claim();
})()));
self.addEventListener('fetch',event=>{
  const req=event.request,url=new URL(req.url);
  if(req.method!=='GET'||url.origin!==self.location.origin)return;
  if(!urls.has(url.pathname)&&!isData(url.pathname)&&req.mode!=='navigate')return;
  if(req.mode==='navigate'&&!['/','/index.html'].includes(url.pathname))return;
  event.respondWith((async()=>{
    const cache=await caches.open(cacheName);
    if(a1AudioPaths.has(url.pathname)){
      const cached=await cache.match(req,{ignoreSearch:true});
      if(cached)return cachedAudioRange(cached,req.headers?.get('range'));
      return fetch(req);
    }
    try{
      const response=await fetch(req);
      if(valid(response,url.pathname))await cache.put(req,response.clone());
      return response;
    }catch{
      return await cache.match(req,{ignoreSearch:true})|| (req.mode==='navigate'?await cache.match('./'):null)||Response.error();
    }
  })());
});
self.addEventListener('message',event=>{
  const {type,language}=event.data||{};
  if(type!=='cache-course'||!allowed.includes(language))return;
  event.waitUntil((async()=>{
    try{
      const cache=await caches.open(cacheName);
      const files=['','-examples','-third','-audit',...(language==='cmn'?['-support']:language==='por'?['-support','-forms']:['-forms'])].map(s=>language+s+'.json');
      files.push('stories-pt.json');
      if(language==='por')files.push('stories-eng.json','stories-spa.json');
      else files.push('stories-'+language+'.json');
      await Promise.all(files.map(async file=>{
        const response=await fetch(file);
        if(!valid(response,file))throw Error(file);
        await cache.put(file,response);
      }));
      event.ports[0]?.postMessage(true);
    }catch{event.ports[0]?.postMessage(false);}
  })());
});
