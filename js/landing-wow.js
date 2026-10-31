/* Pog interativo da landing: entra pulando, fala em vários idiomas e faz sons. */
(function(){
var G=[['Hello! I\'m Pog.','Olá! Eu sou o Pog.','en-US'],['¡Hola! Soy Pog.','Olá! Eu sou o Pog.','es-ES'],['Bonjour ! Moi, c\'est Pog.','Olá! Eu sou o Pog.','fr-FR'],['Ciao! Sono Pog.','Olá! Eu sou o Pog.','it-IT'],['Hallo! Ich bin Pog.','Olá! Eu sou o Pog.','de-DE'],['こんにちは！ポグです。','Olá! Eu sou o Pog.','ja-JP'],['안녕하세요! 포그예요.','Olá! Eu sou o Pog.','ko-KR'],['Olá! Eu sou o Pog.','Vamos aprender juntos?','pt-BR']];
var ctx,muted=false,i=0;try{muted=localStorage.getItem('pg_pog_mute')==='1'}catch(e){}
function ac(){try{ctx=ctx||new (window.AudioContext||window.webkitAudioContext)();if(ctx.state==='suspended')ctx.resume();return ctx}catch(e){return null}}
function tone(f,t,d,type,v){var c=ac();if(!c)return;var o=c.createOscillator(),g=c.createGain();o.type=type||'sine';o.frequency.setValueAtTime(f,c.currentTime+t);g.gain.setValueAtTime(0,c.currentTime+t);g.gain.linearRampToValueAtTime(v||.12,c.currentTime+t+.02);g.gain.exponentialRampToValueAtTime(.0001,c.currentTime+t+d);o.connect(g).connect(c.destination);o.start(c.currentTime+t);o.stop(c.currentTime+t+d+.05)}
function chirp(){var c=ac();if(!c)return;var o=c.createOscillator(),g=c.createGain();o.type='triangle';o.frequency.setValueAtTime(420,c.currentTime);o.frequency.exponentialRampToValueAtTime(980,c.currentTime+.12);o.frequency.exponentialRampToValueAtTime(620,c.currentTime+.2);g.gain.setValueAtTime(.14,c.currentTime);g.gain.exponentialRampToValueAtTime(.0001,c.currentTime+.24);o.connect(g).connect(c.destination);o.start();o.stop(c.currentTime+.26);[784,988,1175].forEach(function(f,k){tone(f,.12+k*.07,.16,'sine',.07)})}
function say(txt,lang){if(muted||!window.speechSynthesis)return;try{speechSynthesis.cancel();var u=new SpeechSynthesisUtterance(txt);u.lang=lang;u.rate=.92;u.pitch=1.2;var v=speechSynthesis.getVoices().filter(function(x){return x.lang&&x.lang.replace('_','-').toLowerCase().indexOf(lang.slice(0,2).toLowerCase())===0})[0];if(v)u.voice=v;speechSynthesis.speak(u)}catch(e){}}
function init(){var pog=document.querySelector('.hero2 .hero-pog'),st=document.querySelector('.hero2 .stage');if(!pog||!st)return false;if(pog.dataset.wow)return true;pog.dataset.wow=1;
 pog.setAttribute('role','button');pog.setAttribute('tabindex','0');pog.setAttribute('aria-label','Pog: toque para ouvir uma saudação');pog.removeAttribute('aria-hidden');
 var b=document.createElement('div');b.className='pog-say';b.setAttribute('aria-live','polite');st.appendChild(b);
 var sb=document.createElement('button');sb.type='button';sb.className='pog-snd';sb.setAttribute('aria-label','Som do Pog');sb.textContent=muted?'🔇':'🔊';st.appendChild(sb);
 function bubble(a,c,hold){b.innerHTML=a+'<small>'+c+'</small>';b.classList.add('on');clearTimeout(bubble.t);bubble.t=setTimeout(function(){b.classList.remove('on')},hold||4200)}
 function sparks(){var r=pog.getBoundingClientRect(),s=st.getBoundingClientRect();['✨','⭐','💛','✦','🎵'].forEach(function(e,k){var el=document.createElement('i');el.className='pog-spark';el.textContent=e;el.style.left=(r.left-s.left+r.width/2)+'px';el.style.top=(r.top-s.top+10)+'px';el.style.setProperty('--x',((k-2)*34)+'px');el.style.setProperty('--y',(-50-Math.random()*50)+'px');st.appendChild(el);setTimeout(function(){el.remove()},1100)})}
 function hi(){var g=G[i++%G.length];pog.classList.remove('talk');void pog.offsetWidth;pog.classList.add('talk');chirp();sparks();bubble(g[0],g[1]);setTimeout(function(){say(g[0].replace(/[!¡]/g,''),g[2])},260)}
 pog.addEventListener('click',hi);pog.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();hi()}});
 sb.addEventListener('click',function(){muted=!muted;sb.textContent=muted?'🔇':'🔊';try{localStorage.setItem('pg_pog_mute',muted?'1':'0');if(muted)speechSynthesis.cancel()}catch(e){}if(!muted)chirp()});
 setTimeout(function(){bubble('Oi! Eu sou o Pog 👋','Toque em mim para ouvir como se diz “olá”.',6000)},2200);
 return true}
var n=0,t=setInterval(function(){if(init()||++n>40)clearInterval(t)},150);
})();
