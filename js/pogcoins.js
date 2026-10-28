/* Pogcoins: a moeda do Pogglot (antes chamada de gemas 💎 nas missões). Substitui a chama de ofensiva nos contadores da home e da barra do topo.
   Saldo guardado em store 'wallet'.gems (compatível com missões e loja de proteção). Episódio novo concluído rende moedas. */
(function(){
'use strict';
let UID=0;
function icon(size){
  const id='pc'+(++UID);size=size||20;
  return `<svg class="pc-coin" width="${size}" height="${size}" viewBox="0 0 32 32" aria-hidden="true" focusable="false"><defs><linearGradient id="${id}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFE27A"/><stop offset=".55" stop-color="#FFB627"/><stop offset="1" stop-color="#E58E10"/></linearGradient></defs><circle cx="16" cy="16" r="14" fill="url(#${id})" stroke="#9A5A00" stroke-width="2"/><circle cx="16" cy="16" r="10.2" fill="none" stroke="#FFF1B8" stroke-width="1.6" opacity=".9"/><path d="M12.6,22.5 L12.6,9.8 L17.6,9.8 Q22,9.8 22,14 Q22,18.2 17.6,18.2 L12.6,18.2" fill="none" stroke="#9A5A00" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M8,8 Q10,5.5 13,5" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" opacity=".7"/></svg>`;
}
const wallet=()=>{try{const w=store.get('wallet',{gems:0,freeze:0});return (w&&typeof w==='object')?w:{gems:0,freeze:0}}catch(e){return {gems:0,freeze:0}}};
const balance=()=>Math.max(0,Math.floor(+wallet().gems||0));
function add(n){try{const w=wallet();w.gems=(+w.gems||0)+n;store.set('wallet',w)}catch(e){}refresh()}
function upgrade(){document.querySelectorAll('.pgstat.coin').forEach(c=>{if(c.querySelector('.pc-coin'))return;const n=[...c.childNodes].find(x=>x.nodeType===3&&/🪙/.test(x.textContent));if(n){const w=document.createElement('span');w.innerHTML=icon(20);n.replaceWith(w.firstChild)}})}
function refresh(){document.querySelectorAll('[data-pgcoins]').forEach(e=>{e.textContent=balance()});upgrade()}
/* moedas pelo episódio concluído pela primeira vez: 5 + até 10 pela precisão de primeira */
function earnHTML(first){
  try{
    if(!first||typeof P==='undefined'||!P)return '';
    const t=P.prTries||0,acc=t?(P.prHits||0)/t:Math.min(1,(P.score||0)/Math.max(1,P.total||1));
    const n=5+Math.round(acc*10);add(n);
    return `<div class="pc-earn" role="status"><span class="pc-ico">${icon(34)}</span><div><b>+${n} Pogcoins</b><small>por concluir o episódio</small></div></div>`;
  }catch(e){return ''}
}
window.PogCoins={icon,balance,add,refresh,earnHTML};
document.addEventListener('visibilitychange',refresh);
try{new MutationObserver(()=>{if(document.querySelector('.pgstat.coin:not(:has(.pc-coin))'))refresh()}).observe(document.body,{childList:true,subtree:true})}catch(e){}
refresh();
})();
