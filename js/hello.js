/* Pogglot · extras estilo HelloTalk: tradução de mensagem, reações e "digitando…".
   Supabase: usa as tabelas de backend/hellotalk.sql (se não existirem, o recurso se esconde sozinho).
   Demo: tudo local e com um parceiro fictício que reage e "digita".
   Tradução: config.js › translate:{url} (POST {text,from,to} → {text}); sem isso usa o serviço gratuito MyMemory. */
(function(){
'use strict';
const C=()=>window.PogCloud,me=()=>C()&&C().user(),sb=()=>C()&&C().mode==='supabase';
const off={react:false,typing:false};
const ls={get(k,d){try{const v=localStorage.getItem(k);return v==null?d:JSON.parse(v)}catch(e){return d}},set(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}}};
const enc=encodeURIComponent;
const RX=['👍','❤️','😂','😮','😢','🙏'];
const missing=e=>{if(e&&(e.code==='setup'||e.code==='forbidden'||/not found|setup|42P01|PGRST/i.test(e.message||'')))return true;return false};

/* ---------- reações: {msgId:{emoji:[uid,...]}} ---------- */
async function reactions(ids){
  ids=ids.filter(x=>x!=null);if(!ids.length||off.react)return {};
  const out={};
  const add=(id,e,u)=>{((out[id]=out[id]||{})[e]=out[id][e]||[]).push(u)};
  if(!sb()){const st=ls.get('pogglot:rx',{});ids.forEach(id=>{(st[id]||[]).forEach(r=>add(id,r.e,r.u))});return out}
  try{
    const rows=await C().rest('GET','/rest/v1/reactions?select=msg_id,uid,emoji&msg_id=in.('+ids.slice(-120).map(Number).filter(Number.isFinite).join(',')+')');
    rows.forEach(r=>add(r.msg_id,r.emoji,r.uid));
  }catch(e){if(missing(e))off.react=true}
  return out;
}
async function react(msgId,emoji,mineNow){
  const u=me();if(!u||off.react)return;
  if(!sb()){const st=ls.get('pogglot:rx',{}),l=(st[msgId]||[]).filter(r=>r.u!==u.id);if(mineNow!==emoji)l.push({e:emoji,u:u.id});st[msgId]=l;ls.set('pogglot:rx',st);return}
  try{
    if(mineNow===emoji)await C().rest('DELETE','/rest/v1/reactions?msg_id=eq.'+enc(msgId)+'&uid=eq.'+enc(u.id),{headers:{Prefer:'return=minimal'}});
    else await C().rest('POST','/rest/v1/reactions?on_conflict=msg_id,uid',{headers:{Prefer:'resolution=merge-duplicates,return=minimal'},body:{msg_id:msgId,uid:u.id,emoji}});
  }catch(e){if(missing(e))off.react=true;throw e}
}
/* demo: depois de uma mensagem sua, o parceiro fictício reage */
function demoBotReact(msg,uid){
  if(sb()||!msg||!msg.id)return;
  setTimeout(()=>{const st=ls.get('pogglot:rx',{}),l=st[msg.id]||[];if(l.some(r=>r.u===uid))return;l.push({e:['❤️','👍','😂','🙏'][msg.id%4],u:uid});st[msg.id]=l;ls.set('pogglot:rx',st)},3500);
}

/* ---------- digitando… ---------- */
let lastPing=0;
async function ping(room){
  const u=me();if(!u||off.typing||!sb())return;
  const n=Date.now();if(n-lastPing<2500)return;lastPing=n;
  try{await C().rest('POST','/rest/v1/typing?on_conflict=room,uid',{headers:{Prefer:'resolution=merge-duplicates,return=minimal'},body:{room,uid:u.id,ts:new Date().toISOString()}})}
  catch(e){if(missing(e))off.typing=true}
}
async function typers(room){
  const u=me();if(!u||off.typing)return [];
  if(!sb()){const t=ls.get('pogglot:typing:'+room,0);return Date.now()<t?[{uid:'demo',name:null}]:[]}
  try{
    const since=new Date(Date.now()-6000).toISOString();
    const rows=await C().rest('GET','/rest/v1/typing?select=uid&room=eq.'+enc(room)+'&uid=neq.'+enc(u.id)+'&ts=gt.'+enc(since)+'&limit=5');
    return rows.map(r=>({uid:r.uid}));
  }catch(e){if(missing(e))off.typing=true;return []}
}
function demoTyping(room,ms){if(!sb())ls.set('pogglot:typing:'+room,Date.now()+(ms||2200))}

/* ---------- tradução ---------- */
const LC={pt:'pt-BR',es:'es',en:'en',fr:'fr',de:'de',it:'it'};
async function translate(text,from,to){
  text=String(text||'').trim().slice(0,480);if(!text)return '';
  const key='pogglot:tr:'+to+':'+text,hit=ls.get(key,null);if(hit)return hit;
  const cfg=(window.POGGLOT_CONFIG&&POGGLOT_CONFIG.translate)||{};let out='';
  if(cfg.url){
    const r=await fetch(cfg.url,{method:'POST',headers:Object.assign({'Content-Type':'application/json'},cfg.headers||{}),body:JSON.stringify({text,from:from||'auto',to})});
    if(!r.ok)throw new Error('translate');const d=await r.json();out=d.text||d.translation||d.translatedText||'';
  }else{
    const pair=(from&&LC[from]?LC[from]:'Autodetect')+'|'+(LC[to]||to);
    const r=await fetch('https://api.mymemory.translated.net/get?q='+enc(text)+'&langpair='+enc(pair));
    if(!r.ok)throw new Error('translate');const d=await r.json();
    out=(d.responseData&&d.responseData.translatedText)||'';
    if(d.responseStatus&&Number(d.responseStatus)!==200)throw new Error(d.responseDetails||'translate');
  }
  out=String(out).replace(/&#39;/g,"'").replace(/&quot;/g,'"').replace(/&amp;/g,'&').trim();
  if(!out)throw new Error('translate');
  ls.set(key,out);return out;
}
window.PogHello={RX,reactions,react,demoBotReact,ping,typers,demoTyping,translate,state:off};
})();
