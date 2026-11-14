/* Jogue agora — mini episódio gamificado (Alice no País das Maravilhas) */
(function(){
var root=document.getElementById('pgRoot');if(!root)return;
var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
var R=[
 {t:'Ouça e toque',h:'O que a Alice perguntou?',k:'listen',say:'Are you in a hurry?',opts:['Você está com pressa?','Você está com fome?','Você está cansado?'],a:0,ok:'Isso! “Are you…?” é como se pergunta.'},
 {t:'Monte a frase',h:'Monte: “Você é novo aqui?”',k:'build',tiles:['you','Are','here','new','?'],ans:['Are','you','new','here','?'],ok:'Frase montada! Agora é só trocar as peças.'},
 {t:'Entenda a cena',h:'Quem está atrasado?',k:'pick',opts:['😺 The Cat','🐰 The Rabbit','👧 Alice'],a:1,ok:'Certo! “I’m late!” disse o Coelho Branco.'},
 {t:'Pares',h:'Una cada palavra ao seu significado',k:'pairs',pairs:[['late','atrasado'],['hurry','pressa'],['new','novo']]},
 {t:'Complete a fala',h:'Yes, I ___ late!',k:'pick',opts:['am','is','are'],a:0,ok:'Perfeito! “I am” → I’m.'}
];
var S;function init(){S={r:0,xp:0,coins:0,combo:0,best:0,miss:0}}
var snd;function beep(f,d){if(reduce)return;try{snd=snd||new (window.AudioContext||window.webkitAudioContext)();var o=snd.createOscillator(),g=snd.createGain();o.frequency.value=f;o.type='triangle';g.gain.value=.06;o.connect(g);g.connect(snd.destination);o.start();g.gain.exponentialRampToValueAtTime(.0001,snd.currentTime+d);o.stop(snd.currentTime+d)}catch(e){}}
function say(t){try{speechSynthesis.cancel();var u=new SpeechSynthesisUtterance(t);u.lang='en-US';u.rate=.85;speechSynthesis.speak(u)}catch(e){}}
function vib(n){try{navigator.vibrate&&navigator.vibrate(n)}catch(e){}}
function el(h){var d=document.createElement('div');d.innerHTML=h;return d.firstElementChild}
function hud(){return '<div class="pg-hud"><div class="pg-pog" id="pgPog">🐰</div><div class="pg-xp" aria-label="Progresso"><i id="pgXp"></i></div><div class="pg-chip fire" id="pgCombo">🔥 ×0</div><div class="pg-chip" id="pgCoins">🪙 0</div></div>'}
function upd(){var x=document.getElementById('pgXp');if(x)x.style.width=Math.round(S.r/R.length*100)+'%';
 var c=document.getElementById('pgCoins'),f=document.getElementById('pgCombo');if(c)c.textContent='🪙 '+S.coins;if(f)f.textContent='🔥 ×'+S.combo}
function bump(id){var e=document.getElementById(id);if(!e)return;e.classList.remove('bump');void e.offsetWidth;e.classList.add('bump')}
function float(txt,node){var p=root.querySelector('.pg');var r=node.getBoundingClientRect(),q=p.getBoundingClientRect();var f=el('<span class="pg-float">'+txt+'</span>');f.style.left=(r.left-q.left+r.width/2-20)+'px';f.style.top=(r.top-q.top)+'px';p.appendChild(f);setTimeout(function(){f.remove()},1000)}
function confetti(){if(reduce)return;var p=root.querySelector('.pg'),cols=['#16B58F','#3E7BE0','#FFB627','#E0647E','#FF7A45'];
 for(var i=0;i<46;i++){var c=el('<i class="pg-conf"></i>');c.style.left=Math.random()*100+'%';c.style.background=cols[i%5];c.style.animationDelay=Math.random()*.5+'s';p.appendChild(c);setTimeout(function(c){return function(){c.remove()}}(c),2400)}}
function good(node,msg){S.combo++;S.best=Math.max(S.best,S.combo);var g=10+5*Math.min(S.combo-1,4);S.coins+=g;S.xp+=g;upd();bump('pgCoins');bump('pgCombo');float('+'+g+' 🪙',node);beep(660,.14);setTimeout(function(){beep(880,.18)},110);vib(15);
 var pog=document.getElementById('pgPog');pog.classList.remove('hop');void pog.offsetWidth;pog.classList.add('hop');var fb=document.getElementById('pgFb');if(fb){fb.className='pg-fb ok';fb.textContent=(S.combo>=3?'🔥 Sequência! ':'✓ ')+(msg||'Muito bem!')}}
function bad(node){S.combo=0;S.miss++;upd();bump('pgCombo');beep(220,.25);vib([40,40,40]);node.classList.add('no');setTimeout(function(){node.classList.remove('no')},450);var fb=document.getElementById('pgFb');if(fb){fb.className='pg-fb no';fb.textContent='Quase! Tente de novo.'}}
function next(){S.r++;upd();setTimeout(function(){S.r>=R.length?end():render()},900)}
function shell(q,body){root.innerHTML='<div class="pg">'+hud()+'<div class="pg-q">'+(S.r+1)+'/'+R.length+' · '+q.t+'</div><h3 class="pg-h">'+q.h+'</h3><div class="pg-stage" id="pgSt">'+body+'<div class="pg-fb" id="pgFb" role="status" aria-live="polite"></div></div></div>';upd()}
function render(){var q=R[S.r];
 if(q.k==='listen'||q.k==='pick'){
  var o=q.opts.map(function(t,i){return '<button class="pg-opt" data-i="'+i+'">'+t+'</button>'}).join('');
  var top=q.k==='listen'?'<button class="pg-say" id="pgSay"><span>🔊</span>Toque para ouvir</button>':'';
  shell(q,top+o);if(q.k==='listen'){var b=document.getElementById('pgSay');b.onclick=function(){say(q.say)};setTimeout(function(){say(q.say)},350)}
  var done=false;root.querySelectorAll('.pg-opt').forEach(function(b){b.onclick=function(){if(done)return;if(+b.dataset.i===q.a){done=true;b.classList.add('ok');root.querySelectorAll('.pg-opt').forEach(function(x){x.disabled=true});good(b,q.ok);next()}else bad(b)}})}
 else if(q.k==='build'){
  shell(q,'<div class="pg-built" id="pgB" aria-label="Sua frase"></div><div class="pg-pool" id="pgP">'+q.tiles.map(function(t,i){return '<button class="pg-tile" data-i="'+i+'">'+t+'</button>'}).join('')+'</div>');
  var cur=0,B=document.getElementById('pgB');root.querySelectorAll('.pg-tile').forEach(function(b){b.onclick=function(){var t=q.tiles[+b.dataset.i];if(t===q.ans[cur]){cur++;b.classList.add('used');B.appendChild(el('<span class="pg-tile set">'+t+'</span>'));beep(520+cur*80,.1);if(cur===q.ans.length){say('Are you new here?');good(B,q.ok);next()}}else bad(b)}})}
 else if(q.k==='pairs'){
  var L=q.pairs.map(function(p,i){return {t:p[0],i:i}}),Rr=q.pairs.map(function(p,i){return {t:p[1],i:i}}).reverse();
  shell(q,'<div class="pg-pairs">'+L.map(function(x){return '<button class="pg-opt" data-s="l" data-i="'+x.i+'">'+x.t+'</button>'}).join('')+Rr.map(function(x){return '<button class="pg-opt" data-s="r" data-i="'+x.i+'">'+x.t+'</button>'}).join('')+'</div>');
  var sel=null,left=q.pairs.length;root.querySelectorAll('.pg-opt').forEach(function(b){b.onclick=function(){
   if(!sel||sel.dataset.s===b.dataset.s){if(sel)sel.classList.remove('sel');sel=b;b.classList.add('sel');if(b.dataset.s==='l')say(b.textContent);return}
   if(sel.dataset.i===b.dataset.i){sel.classList.remove('sel');sel.classList.add('done');b.classList.add('done');good(b,'Par certo!');sel=null;if(--left===0){document.getElementById('pgFb').textContent='✓ Todos os pares!';next()}}
   else{bad(b);sel.classList.remove('sel');sel=null}}})}
}
function end(){var m=S.miss===0?['🥇','Medalha de ouro']:S.miss<=2?['🥈','Medalha de prata']:['🥉','Medalha de bronze'];S.r=R.length;
 root.innerHTML='<div class="pg">'+hud()+'<div class="pg-end"><div class="pg-medal">'+m[0]+'</div><h3 class="pg-h" style="margin:0">'+m[1]+'!</h3><div class="pg-fb ok">🪙 +'+S.coins+' Pogcoins · 🔥 melhor sequência ×'+S.best+'</div><div class="pg-card" id="pgCard" tabindex="0" role="button" aria-label="Virar a figurinha"><div><div class="f"><b>🎴</b>Toque para virar<br>sua figurinha</div><div class="b"><em>🐇</em><b>Alice’s Adventures in Wonderland</b><small>FIGURINHA Nº 002</small></div></div></div><div class="pg-btns"><a class="pg-btn" href="app.html">Jogar o episódio completo →</a><button class="pg-btn alt" id="pgAgain">Jogar de novo</button></div></div></div>';
 upd();document.getElementById('pgXp').style.width='100%';confetti();beep(784,.2);setTimeout(function(){beep(988,.3)},180);
 var c=document.getElementById('pgCard'),fl=function(){c.classList.toggle('flip');if(c.classList.contains('flip')){confetti();beep(1040,.25)}};c.onclick=fl;c.onkeydown=function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();fl()}};
 setTimeout(function(){c.classList.add('flip')},1100);document.getElementById('pgAgain').onclick=function(){init();render()}}
function start(){init();root.innerHTML='<div class="pg">'+hud()+'<div class="pg-end" style="min-height:250px;justify-content:center"><div class="pg-medal" style="animation:none">🐰</div><h3 class="pg-h" style="margin:0">Episódio relâmpago</h3><p style="margin:0;color:#5B6E73;font-weight:600">5 desafios, moedas, sequência e uma figurinha no final. Toque para ouvir os sons.</p><button class="pg-btn" id="pgGo">Começar a jogar ▶</button></div></div>';upd();document.getElementById('pgGo').onclick=function(){beep(600,.1);render()}}
start();
})();
