/* Botão para minimizar a barra de dicas do Pog no player (estado guardado no aparelho). */
(function(){
var K='pg_dockmin';function get(){try{return localStorage.getItem(K)==='1'}catch(e){return false}}
function apply(m){document.body.classList.toggle('pg-dockmin',m);document.querySelectorAll('.dock-tog').forEach(function(b){b.setAttribute('aria-expanded',m?'false':'true');b.firstElementChild.nextSibling.textContent=m?' Mostrar dica':' Esconder dica'})}
function add(){document.querySelectorAll('#player .p-foot').forEach(function(f){if(f.querySelector('.dock-tog')||!f.querySelector('#pbub'))return;
 var b=document.createElement('button');b.type='button';b.className='dock-tog';b.innerHTML='<i>▾</i> Esconder dica';b.onclick=function(e){e.stopPropagation();var m=!document.body.classList.contains('pg-dockmin');try{localStorage.setItem(K,m?'1':'0')}catch(x){}apply(m)};f.appendChild(b);apply(get())})}
var t;new MutationObserver(function(){clearTimeout(t);t=setTimeout(add,40)}).observe(document.body,{childList:true,subtree:true});add();
})();
