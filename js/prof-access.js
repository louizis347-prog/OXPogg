/* Botão "Painel do Professor" na home e no menu do app (o acesso é protegido por código dentro de /professor/). */
(function(){
'use strict';
var URL_='professor/';
var ICON='<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4M7 9h5M7 12h8"/></svg>';
function add(nav){
 if(!nav||nav.querySelector('[data-prof]'))return;
 var b=document.createElement('button');b.type='button';b.setAttribute('data-prof','1');b.innerHTML=ICON+'<span>Painel do Professor</span>';
 b.addEventListener('click',function(e){e.stopPropagation();location.href=URL_});
 nav.appendChild(b);
}
function sync(){add(document.getElementById('pgnav'));add(document.querySelector('.bnav'))}
function pill(){if(document.getElementById('profPill'))return;var a=document.createElement('a');a.id='profPill';a.href=URL_;a.setAttribute('aria-label','Painel do Professor');a.innerHTML=ICON+'<span>Professor</span>';
 a.style.cssText='position:fixed;left:12px;bottom:calc(12px + env(safe-area-inset-bottom));z-index:60;display:flex;align-items:center;gap:6px;padding:8px 13px;border-radius:99px;background:#14263a;color:#fff;font:800 13px system-ui,sans-serif;text-decoration:none;box-shadow:0 6px 18px rgba(0,0,0,.28);opacity:.92';
 a.querySelector('svg').setAttribute('width','16');a.querySelector('svg').setAttribute('height','16');document.body.appendChild(a)}
function init(){sync();pill();new MutationObserver(sync).observe(document.body,{childList:true,subtree:true})}
if(document.body)init();else document.addEventListener('DOMContentLoaded',init);
})();
