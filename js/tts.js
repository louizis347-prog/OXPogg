/* Pogglot · áudio de qualidade
   1) escolhe a melhor voz instalada (neurais/premium primeiro) e respeita sotaque, voz e velocidade do aluno;
   2) guarda o áudio de uma voz neural em nuvem (config.js › tts) no cache do aparelho, para uso offline;
   3) deixa o aluno baixar o áudio de um episódio inteiro. */
(function(){
'use strict';
const store={get(k,d){try{const v=localStorage.getItem('pogglot:'+k);return v?JSON.parse(v):d}catch(e){return d}},set(k,v){try{localStorage.setItem('pogglot:'+k,JSON.stringify(v))}catch(e){}}};
const GM=()=>typeof GENDER_MAP!=='undefined'?GENDER_MAP:{};
const YN=()=>typeof YOU_NAMES!=='undefined'?YOU_NAMES:[];
const CFG=()=>((window.POGGLOT_CONFIG&&POGGLOT_CONFIG.tts)||null);
const ACCENTS={
 en:[['US','en-US','Americano'],['GB','en-GB','Britânico'],['AU','en-AU','Australiano'],['CA','en-CA','Canadense'],['IN','en-IN','Indiano'],['IE','en-IE','Irlandês'],['MIX','','Variado (um sotaque por personagem)']],
 es:[['ES','es-ES','Espanha'],['MX','es-MX','México'],['AR','es-AR','Argentina'],['US','es-US','Estados Unidos'],['CO','es-CO','Colômbia']],
 pt:[['BR','pt-BR','Brasil'],['PT','pt-PT','Portugal']],
 fr:[['FR','fr-FR','França'],['CA','fr-CA','Canadá']],
 de:[['DE','de-DE','Alemanha'],['AT','de-AT','Áustria']],
 it:[['IT','it-IT','Itália']],
 ja:[['JP','ja-JP','Japão']]
};
const DEF={accent:{en:'US',es:'ES',pt:'BR',fr:'FR',de:'DE',it:'IT',ja:'JP'},voice:{},rate:1,cloud:true};
let S=Object.assign({},DEF,store.get('tts',{}));S.accent=Object.assign({},DEF.accent,S.accent||{});S.voice=S.voice||{};
const save=()=>store.set('tts',S);

/* ---------- qualidade das vozes do aparelho ---------- */
const BAD=/compact|espeak|festival|novelty|fred\b|ralph|zarvox|trinoids|whisper|bells|hysterical|cellos|good news|bad news|organ|bubbles|boing|albert|jester|junior|kathy|princess|superstar|wobble|bahh|deranged|pipe organ/i;
function quality(v){
  const n=(v.name||'')+' '+(v.voiceURI||'');let q=0;
  if(/neural|natural|premium|enhanced|wavenet|studio|multilingual/i.test(n))q+=4;
  if(/siri/i.test(n))q+=3;
  if(/google/i.test(n))q+=2;
  if(/microsoft/i.test(n)&&/online/i.test(n))q+=3;
  if(/online/i.test(n)&&/natural/i.test(n))q+=3;
  if(/kyoko|otoya|hattori|o-ren|kanji|nanami|keita|google 日本語|google italiano|google deutsch|google français|google português/i.test(n))q+=1;
  if(v.localService)q+=1;
  if(BAD.test(n))q-=6;
  return q;
}
function qualityLabel(v){const q=quality(v);return q>=4?'Alta':q>=2?'Boa':q>=0?'Básica':'Evitar'}
const lc=v=>String(v.lang||'').replace('_','-');
const lp=l=>String(l||'').slice(0,2).toLowerCase();
function voicesFor(lang){const all=(window.speechSynthesis&&speechSynthesis.getVoices())||[];return all.filter(v=>lc(v).toLowerCase().startsWith(lp(lang)))}
function accentCode(l){const p=lp(l),code=S.accent[p],row=(ACCENTS[p]||[]).find(a=>a[0]===code);return row&&row[1]||''}
function hash(s){let h=0;for(const c of String(s))h=(h*31+c.charCodeAt(0))>>>0;return h}

/* Chamado de dentro de speak(): devolve a voz e a velocidade a usar */
function pick(o){
  try{
    const p=lp(o.lang),all=voicesFor(o.lang);if(!all.length)return null;
    const sp=o.speaker;
    let acc=accentCode(o.lang);
    if(S.accent[p]==='MIX'){const opts=['en-US','en-GB','en-AU'].filter(a=>all.some(v=>lc(v)===a));
      acc=sp&&sp!=='Poggie'&&opts.length?opts[hash(sp)%opts.length]:'en-US'}
    let pool=acc?all.filter(v=>lc(v)===acc):[];
    if(!pool.length)pool=all.filter(v=>lc(v).toLowerCase().startsWith(acc.toLowerCase().slice(0,2)));
    if(sp==='Poggie'&&/^es-(MX|US|419)$/.test(o.lang||'')){/* Poggie em espanhol: sotaque latino-americano (México › EUA › qualquer não-Espanha) */
      const lat=[o.lang,'es-MX','es-US','es-419'].map(c=>all.filter(v=>lc(v)===c)).find(a=>a.length)||all.filter(v=>!/^es-ES$/i.test(lc(v)));
      if(lat.length)pool=lat}
    if(!pool.length)pool=all;
    pool=pool.slice().sort((a,b)=>quality(b)-quality(a));
    const usePref=!sp||YN().includes(sp);
    const pref=S.voice[p];
    let voice=null;
    if(usePref&&pref){voice=all.find(v=>v.voiceURI===pref||v.name===pref)||null}
    if(!voice){
      const top=quality(pool[0]);const best=pool.filter(v=>quality(v)>=top-1);
      if(o.gender&&o.guess){const same=best.filter(v=>o.guess(v)===o.gender);voice=(same.length?same:best)[(o.gidx||0)%(same.length||best.length)]}
      else if(sp==='Poggie'){const m=best.filter(v=>o.guess&&o.guess(v)==='m');voice=(m.length?m:best)[0]}
      else voice=best[0];
    }
    return{voice,rate:(o.rate||.9)*(S.rate||1)};
  }catch(e){return null}
}

/* ---------- voz neural em nuvem (opcional) ---------- */
let AUD=null;
function stop(){try{if(AUD){AUD.pause();AUD.src='';AUD=null}}catch(e){}document.querySelectorAll('.playing').forEach(b=>{if(b.__cloud)b.classList.remove('playing')})}
function cloudReady(){const c=CFG();return !!(c&&c.url&&S.cloud!==false)}
function voiceFor(lang,speaker,gender){
  const c=CFG()||{},v=c.voices&&(c.voices[lang]||c.voices[lp(lang)]);if(!v)return '';
  if(typeof v==='string')return v;
  if(gender&&v[gender]&&v[gender].length)return v[gender][hash(speaker||'')%v[gender].length];
  return v.default||(v.f&&v.f[0])||(v.m&&v.m[0])||'';
}
const keyOf=(text,lang,voice,rate)=>'https://pogglot-tts.local/'+hash(lang+'|'+voice+'|'+rate+'|'+text).toString(36)+'-'+text.length;
async function cache(){return window.caches?caches.open('pogglot-audio-v1'):null}
async function fetchAudio(text,lang,voice,rate){
  const c=CFG(),ca=await cache(),k=keyOf(text,lang,voice,rate);
  if(ca){const hit=await ca.match(k);if(hit)return hit.blob()}
  let req;
  if(typeof c.request==='function')req=c.request({text,lang,voice,rate});
  else req={url:c.url,init:{method:c.method||'POST',headers:Object.assign({'Content-Type':'application/json'},c.headers||{}),body:JSON.stringify({text,lang,voice,rate})}};
  const r=await fetch(req.url,req.init);
  if(!r.ok)throw new Error('tts '+r.status);
  const blob=await r.blob();
  if(!/^audio\//.test(blob.type||'')&&!/audio/.test(r.headers.get('content-type')||''))throw new Error('tts: resposta não é áudio');
  if(ca)try{await ca.put(k,new Response(blob,{headers:{'content-type':blob.type||'audio/mpeg'}}))}catch(e){}
  return blob;
}
function cloudSpeak(text,lang,btn,speaker,slow,fallback){
  const endCb=window.__speakEnd;window.__speakEnd=null;
  const plainT=String(text).replace(/\*\*/g,'');
  const gender=(speaker&&GM()[speaker])?GM()[speaker][0]:(speaker==='Poggie'?'m':null);
  const voice=voiceFor(lang,speaker,gender),rate=Math.round((typeof slow==='number'?(slow<1?.6:1):(slow?.72:1))*(S.rate||1)*100)/100;
  stop();if(btn){btn.classList.add('playing');btn.__cloud=1}
  fetchAudio((window.ttsFix?ttsFix(plainT,lang):plainT),lang,voice,rate).then(blob=>{
    const a=new Audio(URL.createObjectURL(blob));AUD=a;a.playbackRate=1;
    a.onended=a.onerror=()=>{if(btn)btn.classList.remove('playing');if(AUD===a)AUD=null;try{URL.revokeObjectURL(a.src)}catch(e){}if(endCb)setTimeout(endCb,0)};
    return a.play();
  }).catch(()=>{if(btn)btn.classList.remove('playing');window.__speakEnd=endCb;fallback&&fallback()});
}

/* ---------- baixar o áudio de um episódio (uso offline) ---------- */
function episodeTexts(e){
  const out=[],add=(t,sp)=>{t=String(t||'').replace(/\*\*/g,'').trim();if(t&&t.length<400)out.push({text:t,speaker:sp||null})};
  (e.fr||[]).forEach(f=>{
    if(f.k==='scene')(f.lines||[]).forEach(l=>add(l[1],l[0]));
    if(f.k==='words'||f.k==='cwords')(f.items||[]).forEach(w=>add(w[0]));
    if(f.k==='cult1')(f.lines||[]).forEach(l=>add(l[0]));
    if(f.k==='chunk'){add((f.blocks||[]).map(b=>b[0]).join(' '));(f.variants||[]).forEach(v=>add(v[0]))}
    if(f.k==='soundlab'){(f.ex||[]).forEach(x=>add(x[0]));(f.pairs||[]).forEach(p=>{add(p[0]);add(p[1])});if(f.phrase)add(f.phrase[0]);(f.rounds||[]).forEach(r=>add(r.say))}
    if(f.k==='tapimg'||f.k==='sound'||f.k==='vquiz')(f.rounds||[]).forEach(r=>add(r.say));
    if(f.k==='ctx')(f.items||[]).forEach(it=>{let k=0;const L=it.lines.map(l=>[l[0],l[1].replace(/___/g,()=>it.ans[k++])]);L.forEach(l=>add(l[1],l[0]||null))});
    if(f.k==='dictate')(f.lines||[]).forEach(l=>add(l[0]));
    if(f.k==='order')(f.lines||[]).forEach(l=>add(l[1],l[0]));
    if(f.k==='order')(f.extra||[]).forEach(l=>add(l[1],l[0]));
    if(f.k==='scene'&&f.full)f.full.forEach(l=>add(l[1],l[0]));
    if(f.k==='wrap')(f.recap||[]).forEach(r=>add(r[0]));
    if(f.k==='convo')(f.turns||[]).forEach(t=>add(t.npc&&t.npc[0]));
  });
  const seen=new Set();return out.filter(x=>{const k=x.text+'|'+(x.speaker||'');if(seen.has(k))return false;seen.add(k);return true});
}
async function prefetch(items,lang,onProgress){
  if(!cloudReady())throw new Error('sem voz em nuvem');
  let done=0,fail=0;const q=items.slice();
  const worker=async()=>{while(q.length){const it=q.shift();
    const gender=(it.speaker&&GM()[it.speaker])?GM()[it.speaker][0]:null;
    const voice=voiceFor(lang,it.speaker,gender);
    for(const slow of [false,true]){try{await fetchAudio((window.ttsFix?ttsFix(it.text,lang):it.text),lang,voice,Math.round((slow?.72:1)*(S.rate||1)*100)/100)}catch(e){fail++}}
    done++;onProgress&&onProgress(done,items.length,fail)}};
  await Promise.all([worker(),worker(),worker()]);
  return{done,fail};
}
async function clearCache(){try{await caches.delete('pogglot-audio-v1')}catch(e){}}
async function cacheCount(){try{const c=await cache();return c?(await c.keys()).length:0}catch(e){return 0}}

window.PogTTS={
  settings:()=>S,set(patch){Object.assign(S,patch);S.accent=Object.assign({},S.accent);save()},
  setAccent(l,code){S.accent[l]=code;delete S.voice[l];save()},setVoice(l,uri){if(uri)S.voice[l]=uri;else delete S.voice[l];save()},setRate(r){S.rate=Math.max(.6,Math.min(1.25,+r||1));save()},
  ACCENTS,quality,qualityLabel,voicesFor,pick,stop,cloudReady,cloudSpeak,episodeTexts,prefetch,clearCache,cacheCount,
  cloud:()=>!!(CFG()&&CFG().url)
};
})();
