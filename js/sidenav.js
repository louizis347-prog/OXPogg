// Botão flutuante lateral que abre o menu (antes ficava preso embaixo da tela)
(function(){
 function on(){return document.getElementById('pgnav')||document.querySelector('.bnav')}
 var fab=document.createElement('button');fab.id='sdfab';fab.type='button';fab.setAttribute('aria-label','Abrir menu');fab.setAttribute('aria-expanded','false');fab.textContent='☰';
 function set(o){document.body.classList.toggle('sd-open',o);fab.setAttribute('aria-expanded',o?'true':'false');fab.textContent=o?'✕':'☰';fab.setAttribute('aria-label',o?'Fechar menu':'Abrir menu')}
 fab.addEventListener('click',function(e){e.stopPropagation();set(!document.body.classList.contains('sd-open'))});
 document.addEventListener('click',function(e){if(!document.body.classList.contains('sd-open'))return;if(e.target.closest('.pgnav,.bnav'))setTimeout(function(){set(false)},60);else if(e.target!==fab)set(false)},true);
 document.addEventListener('keydown',function(e){if(e.key==='Escape')set(false)});
 function sync(){if(!document.body.contains(fab))document.body.appendChild(fab);fab.style.display=on()?'':'none'}
 function init(){document.body.appendChild(fab);sync();new MutationObserver(sync).observe(document.body,{childList:true})}
 if(document.body)init();else document.addEventListener('DOMContentLoaded',init);
})();
