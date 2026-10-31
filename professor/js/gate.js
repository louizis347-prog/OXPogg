/* Portão do Painel do Professor: pede o código antes de mostrar a página. (Proteção do lado do navegador: separa professor e aluno, não é segurança de servidor.) */
(function(){
'use strict';
var KEY='pg_prof_ok',TTL=12*3600e3,SALT='pogglot-prof:';
var H_SHA='ebaa74a1090afa77cee9bff4b8dc1b2e79b46cb9b81442c5299c15040a058c86',H_FNV='76923dbc';
function fnv(s){var h=0x811c9dc5;for(var i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,0x01000193)>>>0}return h.toString(16)}
function sha(s){if(!(window.crypto&&crypto.subtle))return Promise.resolve(null);return crypto.subtle.digest('SHA-256',new TextEncoder().encode(s)).then(function(b){return Array.prototype.map.call(new Uint8Array(b),function(x){return('0'+x.toString(16)).slice(-2)}).join('')})}
function ok(){try{var t=+localStorage.getItem(KEY);return t&&Date.now()-t<TTL}catch(e){return false}}
function pass(){try{localStorage.setItem(KEY,String(Date.now()))}catch(e){}}
if(ok())return;
var css=document.createElement('style');css.textContent='html.pgate body>*:not(#pgate){visibility:hidden!important}#pgate{position:fixed;inset:0;z-index:99999;display:grid;place-items:center;padding:20px;background:radial-gradient(900px 600px at 10% 0,rgba(122,92,240,.35),transparent),linear-gradient(160deg,#eef3ff,#f6efff);font:16px system-ui,sans-serif;color:#1d2540}#pgate form{width:min(360px,100%);background:rgba(255,255,255,.78);backdrop-filter:blur(14px);border:1px solid rgba(60,80,160,.18);border-radius:24px;padding:26px;display:grid;gap:12px;text-align:center;box-shadow:0 20px 50px rgba(40,50,120,.18)}#pgate h1{margin:0;font-size:22px}#pgate p{margin:0;color:#5b6585;font-size:14px}#pgate input{font:700 28px system-ui;letter-spacing:.5em;text-align:center;border-radius:14px;border:1px solid rgba(60,80,160,.25);padding:10px;background:#fff;color:#1d2540;width:100%}#pgate button{border:0;border-radius:14px;padding:12px;font:800 16px system-ui;background:linear-gradient(135deg,#4a5fe0,#7a5cf0);color:#fff;cursor:pointer}#pgate button:disabled{opacity:.5}#pgate .e{min-height:1.3em;color:#d9444f;font-weight:700;font-size:14px}#pgate a{color:#4a5fe0;font-size:14px}@media(prefers-color-scheme:dark){#pgate{background:linear-gradient(160deg,#10162e,#1b1436);color:#eef1ff}#pgate form{background:rgba(30,38,78,.78)}#pgate p{color:#a5afd4}}';
document.head.appendChild(css);document.documentElement.classList.add('pgate');
var d=document.createElement('div');d.id='pgate';
d.innerHTML='<form autocomplete="off"><h1>👩‍🏫 Painel do Professor</h1><p>Digite o código de acesso.</p><input id="pgc" type="password" inputmode="numeric" maxlength="8" aria-label="Código" autofocus><div class="e" id="pge" role="alert"></div><button type="submit">Entrar</button><a href="../app.html">← Voltar ao app</a></form>';
function mount(){document.body.appendChild(d);var i=d.querySelector('input');i&&i.focus()}
if(document.body)mount();else document.addEventListener('DOMContentLoaded',mount);
var tries=0,lock=0;
d.addEventListener('submit',function(e){e.preventDefault();var inp=d.querySelector('#pgc'),er=d.querySelector('#pge'),b=d.querySelector('button');
 if(Date.now()<lock){er.textContent='Aguarde alguns segundos.';return}
 var v=inp.value.trim(),s=SALT+v;
 sha(s).then(function(h){var good=h?h===H_SHA:fnv(s)===H_FNV;
  if(good){pass();document.documentElement.classList.remove('pgate');d.remove();location.reload();return}
  tries++;inp.value='';er.textContent='Código incorreto.';if(tries>=5){lock=Date.now()+30000;tries=0;b.disabled=true;er.textContent='Muitas tentativas. Aguarde 30 s.';setTimeout(function(){b.disabled=false;er.textContent=''},30000)}})});
})();
