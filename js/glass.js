/* Pogglot · player "glass": liga a camada visual (css/glass.css) nos episódios do inglês regular e troca os emojis de interface por ícones SVG.
   Não altera dados nem a lógica dos quadros. window.POG_GLASS=false desliga. */
(function(){
'use strict';
/* telas compostas (js/combo.js) em todos os episódios do inglês regular; window.POG_COMBO_MAX=10 volta ao piloto */
if(window.POG_COMBO_MAX==null)window.POG_COMBO_MAX=1e9;
const pl=()=>document.getElementById('player');
const active=cid=>window.POG_GLASS!==false&&/^en-/.test(String(cid||''));

/* liga/desliga a classe quando um episódio abre */
const _play=window.play;
if(typeof _play==='function')window.play=function(cid,idx){
  let e=null;try{e=EP[cid]&&EP[cid][idx]}catch(_){}
  const on=active(cid)&&e&&e.presentation==='regular-pilot-v1';
  const r=_play.apply(this,arguments);
  const p=pl();if(p)p.classList.toggle('gl',!!on);
  return r;
};
/* ao fechar, limpa */
const _close=window.closePlayer;
if(typeof _close==='function')window.closePlayer=function(){const p=pl();if(p)p.classList.remove('gl');return _close.apply(this,arguments)};

/* ---------- ícones SVG de linha (no lugar de emojis de interface) ---------- */
const S=(d,extra)=>`<svg class="gl-i" viewBox="0 0 24 24" width="1.15em" height="1.15em" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"${extra||''}>${d}</svg>`;
const ICON={
 '🔊':S('<path d="M3.5 9.5v5h3.8L12.5 19V5L7.3 9.5z" fill="currentColor" stroke="currentColor"/><path d="M15.6 8.8a4.6 4.6 0 0 1 0 6.4" stroke="var(--gl-acc,currentColor)"/><path d="M18.3 6.2a8.4 8.4 0 0 1 0 11.6" stroke="var(--gl-acc,currentColor)"/>'),
 '🔉':S('<path d="M4 9.5v5h3.5L12 18.5v-13L7.5 9.5z"/><path d="M15.5 9a4.2 4.2 0 0 1 0 6"/>'),
 '▶':S('<path d="M8 5.5v13l11-6.5z" fill="currentColor"/>'),
 '▶️':S('<path d="M8 5.5v13l11-6.5z" fill="currentColor"/>'),
 '❓':S('<circle cx="12" cy="12" r="9.2" fill="currentColor" fill-opacity=".14"/><path d="M9.5 9.6a2.6 2.6 0 1 1 3.7 2.3c-.8.5-1.2 1-1.2 1.9"/><circle cx="12" cy="17.2" r=".9" fill="var(--gl-acc,currentColor)" stroke="none"/>'),
 '💬':S('<path d="M20.5 12a8 8 0 0 1-11.6 7.1L3.8 20.5l1.4-4.3A8 8 0 1 1 20.5 12z" fill="currentColor" fill-opacity=".18"/><path d="M8.5 11h7M8.5 14h4.2" stroke="var(--gl-acc,currentColor)"/>'),
 '🧩':S('<path d="M10 4.5a2 2 0 1 1 4 0V6h3.5a1 1 0 0 1 1 1v3.5H20a2 2 0 1 1 0 4h-1.5V18a1 1 0 0 1-1 1H14v-1.5a2 2 0 1 0-4 0V19H6.5a1 1 0 0 1-1-1v-3.5H4a2 2 0 1 1 0-4h1.5V7a1 1 0 0 1 1-1H10z"/>'),
 '🎲':S('<rect x="4" y="4" width="16" height="16" rx="4"/><path d="M8.5 8.5h.01M15.5 8.5h.01M12 12h.01M8.5 15.5h.01M15.5 15.5h.01"/>'),
 '🏃':S('<circle cx="14.5" cy="5" r="1.8"/><path d="M9 21l2.4-5.6L9 13l2.2-4.4 3.3 1.8 2.5 2M7 12.5l2.2-3.4M15 15l2.5 5.5"/>'),
 '🎮':S('<rect x="3" y="7" width="18" height="11" rx="5"/><path d="M8 10.5v4M6 12.5h4M15.5 11.5h.01M17.5 13.5h.01"/>'),
 '🎧':S('<path d="M4 15v-3a8 8 0 0 1 16 0v3"/><rect x="3.2" y="13.6" width="4.6" height="7" rx="2" fill="currentColor"/><rect x="16.2" y="13.6" width="4.6" height="7" rx="2" fill="currentColor"/><path d="M10 12.5v3M12 10.5v7M14 12.5v3" stroke="var(--gl-acc,currentColor)"/>'),
 '✏️':S('<path d="M4 20l1-4L16.5 4.5a2 2 0 0 1 2.8 0l.2.2a2 2 0 0 1 0 2.8L8 19z"/><path d="M14.5 6.5l3 3"/>'),
 '🎤':S('<rect x="8.8" y="3" width="6.4" height="11.5" rx="3.2" fill="currentColor"/><path d="M5.5 11.5a6.5 6.5 0 0 0 13 0M12 18.2V21" /><path d="M10.9 7h2.2" stroke="var(--gl-acc,#fff)"/>'),
 '🎒':S('<path d="M7 20.5h10a2 2 0 0 0 2-2V10a5 5 0 0 0-5-5h-4a5 5 0 0 0-5 5v8.5a2 2 0 0 0 2 2z"/><path d="M9 5V3.5h6V5M8 13h8M10 16.5h4"/>'),
 '🔎':S('<circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5L20 20"/>'),
 '🐢':S('<path d="M5 15a7 6 0 0 1 14 0z"/><path d="M19 13.5l2.5-1.2M5 15l-2 1.5M8 15v2.5M16 15v2.5M10 9.5l1.5 2.5M14 9.5L12.5 12"/>'),
 '🇧🇷':S('<circle cx="12" cy="12" r="9"/><path d="M3.5 12h17M12 3a13 13 0 0 1 0 18M12 3a13 13 0 0 0 0 18"/>'),
 '✨':S('<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8zM18.5 16l.8 2.2 2.2.8-2.2.8-.8 2.2-.8-2.2-2.2-.8 2.2-.8z"/>'),
 '⚡':S('<path d="M13 3L5 13.5h6L10 21l8-10.5h-6z" fill="currentColor" stroke="none"/>'),
 '🎯':S('<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r="1" fill="currentColor"/>'),
 '🔥':S('<path d="M12 3c.5 3-1.7 4.3-3 6.3A5.8 5.8 0 0 0 8 13a4.5 4.5 0 0 0 9 0c0-2.2-1-3.5-2-4.7.2 1.6-.6 2.4-1.5 2.9C13.6 8.4 13.6 5.4 12 3z"/>'),
 '✅':S('<circle cx="12" cy="12" r="9"/><path d="M8 12.5l2.8 2.8L16.5 9"/>'),
 '⭐':S('<path d="M12 3.5l2.6 5.4 5.9.8-4.3 4.1 1 5.9L12 16.9 6.8 19.7l1-5.9L3.5 9.7l5.9-.8z" fill="currentColor" stroke="none"/>'),
 '🌟':S('<path d="M12 3.5l2.6 5.4 5.9.8-4.3 4.1 1 5.9L12 16.9 6.8 19.7l1-5.9L3.5 9.7l5.9-.8z"/>'),
 '📖':S('<path d="M12 6.5C10 5 7.3 4.5 4 5v13c3.3-.5 6 0 8 1.5 2-1.5 4.7-2 8-1.5V5c-3.3-.5-6 0-8 1.5zM12 6.5v13"/>'),
 '📚':S('<path d="M5 4.5h5v15H5zM12 4.5h3l4 15h-3.5zM5 8h5"/>'),
 '🗣️':S('<circle cx="8.5" cy="8" r="3.6" fill="currentColor"/><path d="M2.8 20.5a5.7 5.7 0 0 1 11.4 0z" fill="currentColor"/><path d="M15.8 6.6a4.6 4.6 0 0 1 0 6.8" stroke="var(--gl-acc,currentColor)"/><path d="M18.6 4a8.4 8.4 0 0 1 0 12" stroke="var(--gl-acc,currentColor)"/>'),
 '🎬':S('<rect x="3.5" y="7.5" width="17" height="12" rx="2"/><path d="M3.5 7.5l2-4 3.5 4 3.5-4 3.5 4 3.5-4M3.5 11.5h17"/>'),
 '🎵':S('<path d="M9 18V6l10-2v12"/><circle cx="6.5" cy="18" r="2.5"/><circle cx="16.5" cy="16" r="2.5"/>'),
 '💡':S('<path d="M9 17.5h6M10 20.5h4M12 3.5a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2h5c0-.8.4-1.5 1-2A6 6 0 0 0 12 3.5z"/>'),
 '👄':S('<path d="M3.5 12c2.5-3.2 5-4.2 8.5-2.6 3.5-1.6 6-.6 8.5 2.6-2.5 3.8-5 5-8.5 5s-6-1.2-8.5-5zM3.5 12h17"/>'),
 '🙋':S('<circle cx="12" cy="8" r="3.4"/><path d="M5 21a7 7 0 0 1 14 0M18.5 4l1.5-2M20.5 8h2"/>'),
 '🔁':S('<path d="M4 12a7 7 0 0 1 11.8-5l2.2 2.2M20 12a7 7 0 0 1-11.8 5L6 14.8M18 4.5v4.7h-4.7M6 19.5v-4.7h4.7"/>'),
};
const KEYS=Object.keys(ICON).sort((a,b)=>b.length-a.length);
const RX=new RegExp(KEYS.map(k=>k.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')).join('|'),'g');
/* onde o emoji é conteúdo (figura da cena, banco de palavras, medalhas) NÃO se troca */
const SKIP='.ps-stage,.ps-hot,.ps-hb,.ps-hot-bank,.ps-hot-info,.pr-star,.pr-chip,.pg-fig,.ps-ico,.verb-ic,[data-keep-emoji],svg,script,style,textarea,input';
function swap(root){
  if(!root||!root.querySelectorAll)return;
  const w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT,{acceptNode:n=>RX.test(n.nodeValue)?(RX.lastIndex=0,n.parentElement&&!n.parentElement.closest(SKIP)?NodeFilter.FILTER_ACCEPT:NodeFilter.FILTER_REJECT):(RX.lastIndex=0,NodeFilter.FILTER_REJECT)});
  const nodes=[];while(w.nextNode())nodes.push(w.currentNode);
  for(const n of nodes){
    const html=n.nodeValue.replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c])).replace(RX,m=>ICON[m]||m);
    const sp=document.createElement('span');sp.className='gl-ic';sp.innerHTML=html;n.replaceWith(...sp.childNodes);
  }
}
window.PogGlass={swap,ICON};
function art(){
  const p=pl();if(!p||!window.PogGlassArt)return;
  /* escutar: o azulejo de fones substitui o desenho simples */
  p.querySelectorAll('.ps-q .ps-fig:not([data-gl])').forEach(b=>{
    b.dataset.gl='1';const q=b.closest('.ps-q'),a=q&&q.querySelector('.ps-q-a'),t=a?a.textContent:'';
    const hasSvg=!!b.querySelector('span svg'),hasEmoji=/[\u{1F300}-\u{1FAFF}\u2600-\u27BF]/u.test((b.querySelector('span')||{}).textContent||'');
    if(hasSvg&&!hasEmoji&&/^(Ou[cç]a|Listen)/i.test(t.trim())){b.classList.add('gl-fig');b.innerHTML='<span class="gl-figart">'+PogGlassArt.tile('listen')+'</span><i class="gl-play" aria-hidden="true"><svg viewBox="0 0 24 24" width="12" height="12"><path d="M8 5.5v13l11-6.5z" fill="currentColor"/></svg></i>'}
  });
  /* missões */
  p.querySelectorAll('.ps-mc .ps-ico.big:not([data-gl])').forEach(i=>{i.dataset.gl='1';if(/🙋|🎤|💬/.test(i.textContent))i.innerHTML=PogGlassArt.tile('mission')});
}
/* palavras com hífen (meio-dia, heavy-handed) não se partem entre linhas */
const HY=/[A-Za-zÀ-ÿ0-9]+(?:[-‑][A-Za-zÀ-ÿ0-9]+)+/g;
function nobreak(root){
  const w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT,{acceptNode:n=>{HY.lastIndex=0;return HY.test(n.nodeValue)&&n.parentElement&&!n.parentElement.closest('svg,script,style,textarea,input,.gl-nb')?NodeFilter.FILTER_ACCEPT:NodeFilter.FILTER_REJECT}});
  const nodes=[];while(w.nextNode())nodes.push(w.currentNode);
  for(const n of nodes){const t=n.nodeValue.replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));const sp=document.createElement('span');sp.innerHTML=t.replace(HY,m=>'<span class="gl-nb">'+m+'</span>');n.replaceWith(...sp.childNodes)}
}
let timer=0;
function schedule(){if(timer)return;timer=setTimeout(()=>{timer=0;const p=pl();if(p&&p.classList.contains('gl')){swap(p);art();const st=p.querySelector('#pstage');if(st)nobreak(st)}},60)}
const start=()=>{if(window._glObs)return;window._glObs=new MutationObserver(m=>{const p=pl();if(p&&p.classList.contains('gl')&&m.some(x=>p.contains(x.target)))schedule()});window._glObs.observe(document.body,{childList:true,subtree:true,characterData:true});};
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',start);else start();

/* altura do rodapé (para o corpo nunca ficar escondido atrás dele) */
if(window.ResizeObserver){const ro=new ResizeObserver(()=>{const f=document.querySelector('#player .p-foot'),p=pl();if(f&&p)p.style.setProperty('--gl-foot',Math.ceil(f.getBoundingClientRect().height)+'px')});
  const hook=()=>{const f=document.querySelector('#player .p-foot');if(f&&!f._glRo){f._glRo=1;ro.observe(f)}};setInterval(hook,800);}
})();
