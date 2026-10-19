/* Pogglot · service worker: app offline, dados e áudio em cache */
const V='pogglot-shell-v42',DATA='pogglot-data-v31';
const SHELL=['./','index.html','css/modern.css','config.js','js/cloud.js','js/voice.js','js/tts.js','js/a11y.js','js/exams.js','js/sync.js','css/a11y.css','js/ui.js','js/know.js','js/community.js','js/hello.js','js/missions.js','js/listen.js','js/recap.js','js/theme.js','css/dark.css','css/premium.css','js/forum.js','js/extras.js','js/billing.js','css/forum.css','css/community2.css','js/settings.js','js/path.js','js/ai.js','manifest.webmanifest','icons/icon-192.png'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(V).then(c=>Promise.all(SHELL.map(u=>c.add(u).catch(()=>0)))).then(()=>self.skipWaiting()))});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>(k.startsWith('pogglot-shell-')&&k!==V)||k.startsWith('pogglot-data-')).map(k=>caches.delete(k)))).then(()=>self.clients.claim()))});
self.addEventListener('fetch',e=>{
  const r=e.request;if(r.method!=='GET')return;
  const u=new URL(r.url);
  if(u.hostname==='pogglot-tts.local'){e.respondWith(caches.match(r).then(h=>h||fetch(r)));return}
  if(u.origin!==location.origin){
    if(/fonts\.(googleapis|gstatic)\.com$/.test(u.hostname))e.respondWith(caches.open(V).then(c=>c.match(r).then(h=>h||fetch(r).then(n=>{c.put(r,n.clone());return n}).catch(()=>h))));
    return}
  if(u.pathname.includes('/data/')){ /* dados: rede primeiro (conteúdo novo aparece na hora); sem rede, usa a cópia guardada */
    e.respondWith(caches.open(DATA).then(c=>fetch(r,{cache:'no-cache'}).then(x=>{if(x.ok)c.put(r,x.clone());return x}).catch(()=>c.match(r))));return}
  e.respondWith(fetch(r).then(n=>{if(n.ok)caches.open(V).then(c=>c.put(r,n.clone()));return n}).catch(()=>caches.match(r).then(h=>h||caches.match('index.html'))));
});
self.addEventListener('notificationclick',e=>{e.notification.close();e.waitUntil(self.clients.matchAll({type:'window'}).then(cs=>{for(const c of cs){if('focus' in c)return c.focus()}return self.clients.openWindow('./index.html')}))});
