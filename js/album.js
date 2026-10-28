/* Álbum de vizinhos: cada episódio do Neighbors concluído vira uma figurinha (nome, cidade e curiosidade do lugar). */
(function(){
const K='pogglot:stickers';
const load=()=>{try{return JSON.parse(localStorage.getItem(K)||'{}')}catch(e){return {}}};
const save=s=>{try{localStorage.setItem(K,JSON.stringify(s))}catch(e){}};
const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const FLAG={nb:'🇺🇸',nbeng:'🇺🇸',nbes:'🇪🇸',nbfr:'🇫🇷',nbde:'🇩🇪',nbja:'🇯🇵',nbit:'🇮🇹',nbpt:'🇧🇷',nbpten:'🇧🇷'};
const isNb=cid=>/^nb/.test(cid||'');
const fam=cid=>(String(cid).match(/^(nb[a-z]*)/)||[])[1]||'nb';
function who(e){
  const p=(e.p||'')+'';
  const m=p.match(/(?:conhece|conoces a)\s+([^,.]+?),\s*de\s+([^.]+?)\./);
  if(m)return {name:m[1].trim(),city:m[2].trim()};
  const m2=p.match(/(?:conhece|conoces a)\s+([^,.]+?)(?:,|\.)/);
  if(m2)return {name:m2[1].trim(),city:(e.a&&e.a.w)||''};
  return null;
}
function earn(){
  try{
    if(typeof P==='undefined'||!P||P.isTest||!isNb(P.cid)||!P.e)return null;
    const w=who(P.e);if(!w)return null;
    const key=P.cid+'-'+P.e.n,all=load();
    if(all[key])return {sticker:all[key],fresh:false};
    const st={name:w.name,city:w.city||'',fam:fam(P.cid),title:P.e.t||'',fact:(P.e.a&&P.e.a.d)||'',cid:P.cid,t:Date.now()};
    all[key]=st;save(all);return {sticker:st,fresh:true};
  }catch(e){return null}
}
function card(s,big){
  return `<article class="alb-c ${big?'big':''}"><span class="fl">${FLAG[s.fam]||'🏘️'}</span><b>${esc(s.name)}</b><small>${esc(s.city)}</small>${big&&s.fact?`<p>${esc(s.fact.length>150?s.fact.slice(0,147)+'…':s.fact)}</p>`:''}<em>${esc(s.title)}</em></article>`;
}
const css=`.alb-c{position:relative;display:flex;flex-direction:column;gap:2px;padding:12px 12px 10px;border-radius:16px;background:linear-gradient(160deg,#fff,#F1FCFC);border:2px solid #DAF8F7;box-shadow:0 3px 0 #CDF3F2;color:#204146;text-align:left;min-width:0}
.alb-c .fl{font-size:22px}.alb-c b{font-size:15px;line-height:1.15}.alb-c small{color:#68838D;font-size:12px}
.alb-c em{font-style:normal;font-size:11px;color:#87A0A9;margin-top:4px;line-height:1.25}
.alb-c p{margin:6px 0 0;font-size:12.5px;line-height:1.35;color:#3A575B}
.alb-new{margin:10px 0;display:flex;gap:10px;align-items:center;padding:10px 12px;border-radius:18px;background:#FFF7E0;border:2px solid #FFD36B;animation:albp .6s ease}
.alb-new>span{font-size:26px}.alb-new div{flex:1;min-width:0}.alb-new small{display:block;font-size:11px;font-weight:800;letter-spacing:.06em;color:#9A6A00}.alb-new b{font-size:15px;color:#204146}.alb-new i{font-style:normal;display:block;font-size:12px;color:#68838D}
@keyframes albp{from{transform:scale(.92);opacity:0}to{transform:none;opacity:1}}
#alb{position:fixed;inset:0;z-index:2147483000;background:rgba(25,59,65,.55);backdrop-filter:blur(6px);display:flex;align-items:center;justify-content:center;padding:14px}
#alb .box{width:min(720px,100%);max-height:100%;overflow:auto;background:#fff;border-radius:24px;padding:18px 16px 16px;box-shadow:0 24px 60px rgba(25,59,65,.35)}
#alb h2{margin:0;font-size:22px;color:#204146}#alb .sub{margin:2px 0 12px;color:#68838D;font-size:13px}
#alb .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:10px}
#alb .x{float:right;border:0;background:#EDFCFB;border-radius:12px;width:38px;height:38px;font-size:18px;cursor:pointer}
#alb .empty{padding:26px 8px;text-align:center;color:#68838D}
.alb-btn{display:inline-flex;align-items:center;gap:8px;margin:10px 0;padding:11px 16px;border:2px solid #DAF8F7;border-radius:16px;background:#fff;color:#204146;font:inherit;font-weight:800;cursor:pointer}`;
const st=document.createElement('style');st.textContent=css;document.head.appendChild(st);
function open(){
  const all=load(),list=Object.values(all).sort((a,b)=>b.t-a.t);
  const d=document.createElement('div');d.id='alb';
  d.innerHTML=`<div class="box" role="dialog" aria-label="Álbum de vizinhos"><button class="x" aria-label="Fechar">✕</button><h2>🏘️ Álbum de vizinhos</h2><p class="sub">${list.length?list.length+' vizinho'+(list.length>1?'s':'')+' conhecido'+(list.length>1?'s':'')+'. Conclua episódios do Neighbors para ganhar novas figurinhas.':'Cada episódio do Neighbors concluído ganha uma figurinha aqui.'}</p>${list.length?`<div class="grid">${list.map(s=>card(s,true)).join('')}</div>`:'<div class="empty">Seu álbum está vazio. Complete um episódio do Neighbors para ganhar a primeira figurinha.</div>'}</div>`;
  d.onclick=e=>{if(e.target===d||e.target.closest('.x'))d.remove()};
  document.body.appendChild(d);
}
/* quadro final: avisa a figurinha nova */
const _render=window.render;
if(typeof _render==='function')window.render=function(){
  const r=_render.apply(this,arguments);
  try{
    if(typeof P!=='undefined'&&P&&P.steps&&P.steps[P.i]==='done'&&isNb(P.cid)){
      const g=earn();
      if(g&&g.fresh){
        setTimeout(()=>{
          const host=document.querySelector('#pbody .step.done');if(!host||host.querySelector('.alb-new'))return;
          const n=document.createElement('div');n.className='alb-new';n.innerHTML=`<span>🎴</span><div><small>NOVA FIGURINHA</small><b>${esc(g.sticker.name)}</b><i>${esc(g.sticker.city)} · ${Object.keys(load()).length} no álbum</i></div>`;
          host.insertBefore(n,host.children[1]||null);
        },500);
      }
    }
  }catch(e){}
  return r;
};
/* atalho na página de cada curso Neighbors */
const _hub=window.hub;
if(typeof _hub==='function')window.hub=function(id){
  const r=_hub.apply(this,arguments);
  try{
    if(isNb(id)){
      setTimeout(()=>{
        const host=document.querySelector('.p2lhead')||document.querySelector('.wrap');if(!host||document.querySelector('.alb-btn'))return;
        const b=document.createElement('button');b.className='alb-btn';b.type='button';
        b.innerHTML=`🎴 Meu álbum de vizinhos <small>(${Object.keys(load()).length})</small>`;b.onclick=open;
        host.insertAdjacentElement('afterend',b);
      },60);
    }
  }catch(e){}
  return r;
};
window.POG_ALBUM={open,load,earn};
})();
