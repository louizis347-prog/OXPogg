/* Pogglot · tema claro/escuro/automático. Aplica antes da pintura (script no <head>) e liga o botão da barra. */
(function(){
'use strict';
var KEY='pogglot:theme',root=document.documentElement;
function get(){try{return localStorage.getItem(KEY)||'auto'}catch(e){return 'auto'}}
function eff(m){return m==='auto'?(window.matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'):m}
function apply(m){var t=eff(m||get());root.setAttribute('data-theme',t);
  var mt=document.querySelector('meta[name=theme-color]');if(mt)mt.setAttribute('content',t==='dark'?'#0C1B1D':'#F4FDFC');
  document.querySelectorAll('[data-act="theme"]').forEach(function(b){b.textContent=t==='dark'?'🌙':'☀️';b.setAttribute('aria-label',t==='dark'?'Tema escuro':'Tema claro')})}
function set(m){try{localStorage.setItem(KEY,m)}catch(e){}apply(m)}
function toggle(){set(eff(get())==='dark'?'light':'dark')}
apply();
try{matchMedia('(prefers-color-scheme: dark)').addEventListener('change',function(){if(get()==='auto')apply()})}catch(e){}
document.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('[data-act="theme"]');if(b){e.preventDefault();e.stopPropagation();toggle()}},true);
window.PogTheme={get:get,set:set,toggle:toggle,apply:apply,eff:function(){return eff(get())}};
})();
