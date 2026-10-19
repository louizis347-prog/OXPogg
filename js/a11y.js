/* Pogglot · acessibilidade: tamanho do texto, alto contraste e menos movimento. Aplica antes da pintura. */
(function(){
'use strict';
var KEY='pogglot:a11y',root=document.documentElement,D={zoom:100,contrast:false,motion:false};
function get(){try{var v=JSON.parse(localStorage.getItem(KEY)||'null');return Object.assign({},D,v||{})}catch(e){return Object.assign({},D)}}
function apply(s){s=s||get();var z=Math.max(90,Math.min(150,+s.zoom||100));
  root.style.setProperty('--pg-zoom',z/100);root.toggleAttribute('data-zoomed',z!==100);
  root.setAttribute('data-contrast',s.contrast?'high':'normal');
  root.setAttribute('data-motion',s.motion?'reduce':'normal')}
function set(p){var s=Object.assign(get(),p);try{localStorage.setItem(KEY,JSON.stringify(s))}catch(e){}apply(s);return s}
apply();
window.PogA11y={get:get,set:set,apply:apply,reset:function(){return set(D)}};
})();
