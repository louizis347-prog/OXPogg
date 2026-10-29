/* Pogglot · ilustrações SVG dos exercícios (azulejos duotone petróleo/sol/coral). Usado por js/glass.js. */
(function(){
'use strict';
let uid=0;
const wrap=(inner,g)=>{const id='gla'+(++uid);return `<svg class="gl-art" viewBox="0 0 96 96" role="img" aria-hidden="true"><defs><linearGradient id="${id}" x1="0" y1="0" x2="1" y2="1">${g}</linearGradient><radialGradient id="${id}h" cx=".25" cy=".15" r=".8"><stop offset="0" stop-color="#fff" stop-opacity=".38"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient></defs><rect x="2" y="2" width="92" height="92" rx="27" fill="url(#${id})"/><rect x="2" y="2" width="92" height="92" rx="27" fill="url(#${id}h)"/>${inner}</svg>`};
const TEAL='<stop offset="0" stop-color="#17a2ad"/><stop offset="1" stop-color="#0a6270"/>';
const CORAL='<stop offset="0" stop-color="#ff9a62"/><stop offset="1" stop-color="#e0562a"/>';
const SUN='<stop offset="0" stop-color="#ffd266"/><stop offset="1" stop-color="#f29a0a"/>';
const BLUE='<stop offset="0" stop-color="#5b8cf5"/><stop offset="1" stop-color="#2456c9"/>';
const ART={
 /* escutar: fones + equalizador */
 listen:()=>wrap(`<path d="M25 52a23 23 0 0 1 46 0" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round"/>
  <rect x="17" y="48" width="14" height="27" rx="7" fill="#fff"/><rect x="65" y="48" width="14" height="27" rx="7" fill="#fff"/>
  <rect x="21" y="55" width="6" height="13" rx="3" fill="#ffb627"/><rect x="69" y="55" width="6" height="13" rx="3" fill="#ffb627"/>
  <g fill="#ffd266"><rect x="38" y="58" width="4.6" height="13" rx="2.3"/><rect x="45.7" y="50" width="4.6" height="21" rx="2.3"/><rect x="53.4" y="55" width="4.6" height="16" rx="2.3"/></g>
  <circle cx="75" cy="22" r="3" fill="#fff" opacity=".7"/><circle cx="20" cy="26" r="2" fill="#fff" opacity=".6"/>`,TEAL),
 /* falar: microfone + ondas */
 speak:()=>wrap(`<rect x="38" y="16" width="20" height="38" rx="10" fill="#fff"/><rect x="43" y="22" width="10" height="9" rx="4.5" fill="#ffb627"/>
  <path d="M28 46a20 20 0 0 0 40 0M48 66v13M39 79h18" fill="none" stroke="#fff" stroke-width="5.5" stroke-linecap="round"/>
  <path d="M18 38a14 14 0 0 0 0 16M78 38a14 14 0 0 1 0 16M11 33a22 22 0 0 0 0 26M85 33a22 22 0 0 1 0 26" fill="none" stroke="#ffe1a0" stroke-width="3.2" stroke-linecap="round" opacity=".85"/>`,CORAL),
 /* missão: balão de fala + estrela */
 mission:()=>wrap(`<path d="M20 26a10 10 0 0 1 10-10h36a10 10 0 0 1 10 10v26a10 10 0 0 1-10 10H46L32 76V62h-2a10 10 0 0 1-10-10z" fill="#fff"/>
  <path d="M48 27l3.7 7.6 8.3 1.2-6 5.9 1.4 8.3L48 46l-7.4 3.9 1.4-8.3-6-5.9 8.3-1.2z" fill="#ffb627"/>
  <circle cx="78" cy="20" r="3.4" fill="#fff" opacity=".75"/><circle cx="17" cy="78" r="2.4" fill="#fff" opacity=".6"/>`,BLUE),
 /* som: alto-falante com ondas */
 sound:()=>wrap(`<path d="M22 40v16h13l16 14V26L35 40z" fill="#fff"/><path d="M60 38a14 14 0 0 1 0 20M68 30a26 26 0 0 1 0 36" fill="none" stroke="#ffe1a0" stroke-width="5" stroke-linecap="round"/>`,SUN),
 /* leitura: livro aberto */
 read:()=>wrap(`<path d="M48 30C41 24 31 22 20 23v44c11-1 21 1 28 7 7-6 17-8 28-7V23c-11-1-21 1-28 7z" fill="#fff"/><path d="M48 30v44" stroke="#17a2ad" stroke-width="3.2"/><path d="M27 34c5 0 10 1 15 4M27 44c5 0 10 1 15 4M69 34c-5 0-10 1-15 4M69 44c-5 0-10 1-15 4" fill="none" stroke="#ffb627" stroke-width="3.4" stroke-linecap="round"/>`,TEAL),
};
window.PogGlassArt={tile:k=>(ART[k]||ART.listen)(),kinds:Object.keys(ART)};
})();
