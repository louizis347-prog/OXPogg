/* Aula Quest · Poggie que fala, elogios variados que somem ao trocar de quadro, áudio nas referências culturais
   (português com voz pt-BR, inglês com voz en-US), "toque para saber mais" em mini-páginas e textos do cotidiano ilustrados */
(function(){'use strict';
var V=window.L1VIS;if(!V)return;
var H=V.H,$=V.$,$$=V.$$;
function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function rich(s){return esc(s).replace(/\*\*(.+?)\*\*/g,'<b>$1</b>')}
function plain(s){return String(s==null?'':s).replace(/\*\*/g,'')}
/* ================= fala (voz certa para cada idioma) ================= */
var VOICES=[];function loadV(){try{VOICES=speechSynthesis.getVoices()||[]}catch(e){}}
loadV();try{speechSynthesis.addEventListener('voiceschanged',loadV)}catch(e){}
function pickVoice(lang){var l=lang.toLowerCase(),p=l.slice(0,2),c=VOICES.filter(function(v){return String(v.lang).replace('_','-').toLowerCase().indexOf(l)===0});
  if(!c.length)c=VOICES.filter(function(v){return String(v.lang).toLowerCase().indexOf(p)===0});if(!c.length)return null;
  function q(v){var n=v.name||'',s=0;if(/google|natural|neural|premium|enhanced/i.test(n))s+=3;if(/luciana|francisca|samantha|aria|jenny|joana/i.test(n))s+=2;if(v.localService===false)s+=1;return s}
  return c.sort(function(a,b){return q(b)-q(a)})[0]}
function isPT(t){return /[ãõçáéíóúâêôà]/i.test(t)||/(^|[^a-z])(que|de|para|com|uma?|não|você|em|os|as|é|se|na|no|são|mas|muito|também|quando|como|sua|seu|nos|dos|das|pelo|aos|isso|ao|ou|há|foi|ser|tem|por)([^a-z]|$)/i.test(t)}
function segments(text){var out=[],re=/[“"]([^”"]+)[”"]/g,last=0,m,t=String(text||'');
  function pushOut(s){s=s.replace(/\s+/g,' ').trim();if(s.replace(/[^A-Za-zÀ-ú]/g,'').length<2)return;out.push({t:s,l:isPT(s)?'pt-BR':'en-US'})}
  while((m=re.exec(t))){pushOut(t.slice(last,m.index));var q=m[1].trim();if(q)out.push({t:q,l:isPT(q)&&!/^[A-Za-z' ,.!?’-]+$/.test(q)?'pt-BR':'en-US'});last=re.lastIndex}
  pushOut(t.slice(last));return out}
var token=0;
function stop(){token++;try{speechSynthesis.cancel()}catch(e){}$$(document,'.q1v-narr.on').forEach(function(b){b.classList.remove('on');b.firstChild.textContent='🔊 '})}
function speakSegs(segs,done){stop();var my=token;var i=0;
  function next(){if(my!==token)return;if(i>=segs.length){if(done)done();return}var s=segs[i++],u=new SpeechSynthesisUtterance(s.t);u.lang=s.l;var v=pickVoice(s.l);if(v)u.voice=v;u.rate=s.l==='en-US'?.9:.98;u.onend=next;u.onerror=next;try{speechSynthesis.speak(u)}catch(e){next()}}
  next()}
window.L1SPEAK={segments:segments,speak:function(t,l){speakSegs([{t:t,l:l||(isPT(t)?'pt-BR':'en-US')}])},speakText:function(t,done){speakSegs(segments(t),done)},stop:stop};
/* ================= elogios variados ================= */
var PRAISE=['Isso aí!','Mandou bem!','Na mosca!','Resposta de quem sabe!','Boa, continue assim!','Show de bola!','Exatamente!','Você pegou o jeito!','Caprichou!','Essa foi rápida!','Ouvido afiado!','Perfeito, sem erro!','Gostei dessa!','Agora sim!','Você já fala assim!','Certeira!','Que memória!','Muito bem pensado!','Dessa vez foi de primeira!','Sem tropeçar!','Pronunciou como gente de lá!','Foi quase automático!'];
var OOPS=['Quase! Veja o porquê.','Boa tentativa, olhe a dica.','Tudo bem errar: leia a explicação.','Ainda não, mas está perto.','Vamos entender essa juntos.'];
var lastPraise=-1,bag=[];
function nextPraise(){if(!bag.length){bag=PRAISE.map(function(_,i){return i}).sort(function(){return Math.random()-.5});if(bag[bag.length-1]===lastPraise)bag.reverse()}lastPraise=bag.pop();return PRAISE[lastPraise]}
var oopsI=0;function nextOops(){return OOPS[(oopsI++)%OOPS.length]}
/* ================= Poggie (coach) ================= */
var coach,coachTimer,coachRun=0;
function ensureCoach(){if(coach&&coach.isConnected)return coach;coach=document.createElement('div');coach.className='q1v-coach';coach.setAttribute('aria-live','polite');
  var m='';try{if(window.HomeArt&&HomeArt.mascot)m=HomeArt.mascot({scarf:'#2b6fe6'})}catch(e){}
  coach.innerHTML='<div class="q1v-cm">'+(m||'🦦')+'</div><div class="q1v-cb"><span class="q1v-ct"></span></div>';document.body.appendChild(coach);return coach}
function say(msg,ms,tone){var c=ensureCoach();clearTimeout(coachTimer);$('.q1v-ct',c).textContent=msg;c.classList.remove('ok','no');if(tone)c.classList.add(tone);c.classList.add('on');
  coachTimer=setTimeout(function(){c.classList.remove('on')},ms||5200)}
function hideCoach(){clearTimeout(coachTimer);if(coach)coach.classList.remove('on','ok','no')}
var KIND_MSG={
 cover:['Oi! Eu sou o Poggie. Hoje a aula é sobre “{t}”. Vamos?','Pronto para “{t}”? Eu acompanho você até o fim.','Hoje vamos aprender a se virar em “{t}”.'],
 review:['Antes de começar, uma revisão rápida do que já vimos.','Aquecendo a memória com as aulas anteriores.'],
 reviewwords:['Toque em cada figura e tente lembrar a palavra antes de ver.','Se lembrar sem ajuda, é sinal de que ficou.'],
 reviewsay:['Agora é a sua voz! Ouça e repita.','Sem pressa: ouça primeiro, depois fale.'],
 quiz:['Escolha com calma. A dica aparece depois.','Pense na situação, não na tradução palavra por palavra.','Responda pela situação: o que uma pessoa diria de verdade?'],
 work:['Este é o seu desafio de hoje.','Olhe a missão: ao final você consegue fazer isso sozinho.'],
 facts:['Curiosidade do dia a dia: toque nos cartões para saber mais.','Um detalhe que muda a conversa: leia e, se quiser, ouça.','Cultura de verdade: toque no cartão para abrir.'],
 compare:['Brasil e Estados Unidos lado a lado. Toque em cada um!','Repare no que muda de um país para o outro.'],
 artifact:['Textos como este aparecem o tempo todo. Leia e responda.','Você vai ver isso na vida real. Qual é a informação-chave?'],
 reading:['Passe o mouse (ou toque) nas frases para ver a tradução.','Leia uma vez para entender e outra para ouvir.'],
 dialog:['Clique nas palavras coloridas: elas trocam e a frase muda.','Brinque com as trocas até soar natural.'],
 vocab:['Toque, ouça e fale cada palavra.','Fale em voz alta, o microfone dá a sua nota.'],
 pattern:['Aqui você monta frases com moldes: troque as peças.','Escolha as peças e veja a frase nascer.'],
 sound:['Cuidado com este som: ouça devagar e repita.','Sons difíceis ficam fáceis com repetição.'],
 soundlab:['Laboratório de sons: olhe como a boca se mexe.','Dica de boca e de ar: experimente agora.'],
 verbs:['Veja como o verbo muda para cada pessoa e tempo.','Toque nas peças coloridas para ver o verbo mudar.'],
 verbplay:['Agora aplique o verbo na situação.','Qual forma encaixa nesta cena?'],
 exprs:['Frases prontas que você vai usar muito.','Guarde estas expressões: elas salvam a conversa.'],
 exprplay:['Qual expressão serve para esta situação?','Escolha a frase que uma pessoa diria aqui.'],
 role:['Hora de conversar! Você é o personagem principal.','Escolha as respostas e acompanhe a conversa.'],
 writing:['Agora escreva com as suas palavras.','Uma frase sua vale mais que dez copiadas.'],
 exit:['Quase lá! Monte as frases sem consultar.','Sem espiar: o que ficou na memória?'],
 finish:['Aula concluída! Veja o que você levou daqui.','Missão cumprida. Até a próxima!']};
var kindUse={};
function frameCoach(p,b){if(!p)return;var arr=KIND_MSG[p.kind];if(!arr)return;var k=p.kind;kindUse[k]=((kindUse[k]||0)+1);var msg=arr[(kindUse[k]-1)%arr.length];
  var L=window.__LESSON||{};msg=msg.replace('{t}',(L.topic||L.title||'esta situação'));var run=++coachRun;
  setTimeout(function(){if(run===coachRun)say(msg,5600)},650)}
/* ================= limpeza ao trocar de quadro ================= */
function clearTransient(){$$(document,'.q1v-toast,.xpop').forEach(function(e){e.remove()});hideCoach();stop()}
/* reação às respostas: Poggie fala uma frase diferente a cada acerto; some no próximo quadro */
(function(){var prev=window.RL_ONGAIN;window.RL_ONGAIN=function(n,ok,xp,streak){if(prev){try{prev.apply(this,arguments)}catch(e){}}
  if(n>0&&ok){say(nextPraise(),2600,'ok');var hero=$('.pb .q1v-react');if(hero)hero.textContent='✨ '+nextPraise()}
  else if(!ok){say(nextOops(),3000,'no')}}})();
/* ================= mini-páginas (toque para saber mais) ================= */
var modal;
function closeMini(){if(modal){modal.classList.remove('on');setTimeout(function(){if(modal){modal.remove();modal=null}},180)}stop()}
document.addEventListener('keydown',function(e){if(e.key==='Escape')closeMini()});
function openMini(o){closeMini();modal=document.createElement('div');modal.className='q1v-mini';modal.setAttribute('role','dialog');modal.setAttribute('aria-modal','true');
  var body=(o.body||[]).map(function(t){return '<p>'+rich(t)+'</p>'}).join('');
  var quotes=[];(o.body||[]).join(' ').replace(/[“"]([^”"]{3,90})[”"]/g,function(_,q){if(!isPT(q)||/^[A-Za-z' ,.!?’-]+$/.test(q))quotes.push(q)});
  quotes=quotes.filter(function(q,i){return quotes.indexOf(q)===i}).slice(0,4);
  modal.innerHTML='<div class="q1v-mc"><button type="button" class="q1v-mx" aria-label="Fechar">✕</button><div class="q1v-mh" style="--h:'+(o.hue||210)+'"><span class="q1v-mi">'+esc(o.icon||'📖')+'</span><div><small>'+esc(o.kicker||'Saiba mais')+'</small><h3>'+esc(o.title||'')+'</h3></div></div><div class="q1v-mb">'+body+(quotes.length?'<div class="q1v-mq"><b>Para falar:</b>'+quotes.map(function(q,i){return '<button type="button" data-q="'+i+'">🔊 '+esc(q)+'</button>'}).join('')+'</div>':'')+'</div><div class="q1v-mf"><button type="button" class="q1v-narr q1v-mlisten"><span>🔊 </span>Ouvir esta página</button></div></div>';
  document.body.appendChild(modal);requestAnimationFrame(function(){modal.classList.add('on')});
  modal.addEventListener('click',function(e){if(e.target===modal||e.target.closest('.q1v-mx'))closeMini()});
  $$(modal,'[data-q]').forEach(function(x){x.onclick=function(){window.L1SPEAK.speak(quotes[+x.dataset.q],'en-US')}});
  var nb=$('.q1v-mlisten',modal);nb.onclick=function(){if(nb.classList.contains('on')){stop();return}stop();nb.classList.add('on');nb.firstChild.textContent='⏹ ';speakSegs(segments([o.title].concat(o.body||[]).map(plain).join('. ')),function(){nb.classList.remove('on');nb.firstChild.textContent='🔊 '})};
  var mx=$('.q1v-mx',modal);if(mx)mx.focus()}
window.L1MINI=openMini;
function hueOf(s){var h=0;String(s).split('').forEach(function(c){h=(h*31+c.charCodeAt(0))%360});return h}
/* ================= botão de áudio nas referências culturais ================= */
var NARR={facts:1,compare:1,artifact:1};
function addNarrate(b,p){var main=$('.q1v-main',b)||b;if($('.q1v-narr',b))return;
  var btn=document.createElement('button');btn.type='button';btn.className='q1v-narr q1v-nbtn';btn.innerHTML='<span>🔊 </span>Ouvir';main.insertBefore(btn,main.firstChild);
  btn.onclick=function(){if(btn.classList.contains('on')){stop();return}var clone=main.cloneNode(true);$$(clone,'.q1v-narr,button,.q1v-hero,svg,.ps-stage').forEach(function(e){e.remove()});
    var text=(clone.innerText||clone.textContent||'').replace(/\n+/g,'. ');stop();btn.classList.add('on');btn.firstChild.textContent='⏹ ';speakSegs(segments(text),function(){btn.classList.remove('on');btn.firstChild.textContent='🔊 '})}}
/* ================= cartões clicáveis ================= */
function findCard(b,txt){var els=$$(b,'h3,b,strong,.q1v-sbig');txt=String(txt).slice(0,40);for(var i=0;i<els.length;i++){if(els[i].textContent.indexOf(txt)===0){return els[i].closest('.q1-card,.q1v-sit,.q1v-fact,.q1v-sitgrid>div,li')||els[i].parentNode}}return null}
function wireFacts(b,p){(p.facts||[]).forEach(function(f){var c=findCard(b,f.big);if(!c||c.dataset.more)return;c.dataset.more='1';c.classList.add('q1v-more');c.setAttribute('tabindex','0');c.setAttribute('role','button');
  var go=function(){openMini({icon:f.icon||'💡',kicker:f.label||'Cultura',title:f.big,body:[f.sub].concat(f.more?[].concat(f.more):[]),hue:hueOf(f.big)})};
  c.addEventListener('click',function(e){if(e.target.closest('button,a,input'))return;go()});c.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();go()}})})}
function wireCompare(b,p){var cp=p.compare;if(!cp)return;var cols=$$(b,'.q1v-pairrow>div');var data=[['🇧🇷','No Brasil',cp.br,'#2e9e5b'],['🇺🇸','Nos Estados Unidos',cp.us,'#3b6fe0']];
  cols.forEach(function(c,i){var d=data[i];if(!d||c.dataset.more)return;c.dataset.more='1';c.classList.add('q1v-more');c.setAttribute('tabindex','0');c.setAttribute('role','button');
    var go=function(){var body=[d[2]];if(cp.tip)body.push('Dica para falar: '+cp.tip);if(cp.ask)body.push('Sua vez: '+cp.ask);openMini({icon:d[0],kicker:'Compare',title:d[1],body:body,hue:i?220:140})};
    c.addEventListener('click',go);c.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();go()}})});
  $$(b,'.q1-card').forEach(function(c){if(c.dataset.more)return;var t=c.textContent;[['tip','Dica'],['ask','Sua vez']].forEach(function(k){var v=cp[k[0]];if(v&&t.indexOf(String(v).slice(0,25))>=0){c.dataset.more='1';c.classList.add('q1v-more');c.setAttribute('tabindex','0');c.setAttribute('role','button');c.addEventListener('click',function(){openMini({icon:k[0]==='tip'?'💡':'🎤',kicker:'Para usar hoje',title:k[1],body:[v],hue:hueOf(v)})})}})})}
/* ================= textos do cotidiano ilustrados ================= */
function lines(w){return (w.lines||[]).map(function(l){return rich(l)})}
function kindOf(k){k=String(k||'').toLowerCase();
  if(/receipt/.test(k))return'receipt';if(/ticket|boarding pass|pass$/.test(k))return'ticket';
  if(/text|message|chat|sms|voicemail|reminder|thank-you/.test(k))return'phone';
  if(/weather|app|screen|alarm|calendar|order/.test(k))return'app';
  if(/menu|price board|price sign|price tag|barbecue|rental board|ticket window|ticket board|price/.test(k))return'menu';
  if(/note|fridge|hanger|recipe/.test(k))return'note';
  if(/invitation|card|invite/.test(k))return'card';
  if(/flyer|poster|rule|tip/.test(k))return'poster';
  if(/name tag|label|tag/.test(k))return'label';
  if(/schedule|directory|board|timetable/.test(k))return'board';
  if(/sign|notice/.test(k))return'sign';return'paper'}
var ART={
 phone:function(w){var L=lines(w);return '<div class="q1a-phone"><div class="q1a-notch"></div><div class="q1a-bar"><span>‹</span><b>'+esc(w.kind.replace(/^.*?(message|text)/i,'$1')||'Mensagem')+'</b><span>⋯</span></div><div class="q1a-chat">'+L.map(function(l,i){return '<div class="q1a-b '+(i%2?'me':'')+'">'+l+'</div>'}).join('')+'</div></div>'},
 receipt:function(w){var L=lines(w);return '<div class="q1a-receipt"><div class="q1a-rh">★ RECEIPT ★</div>'+L.map(function(l){var m=l.replace(/<[^>]+>/g,'').match(/^(.*?)(\$?\d+[\d.,]*)\s*$/);return m&&/\d/.test(m[2])?'<div class="q1a-row"><span>'+esc(m[1].trim())+'</span><b>'+esc(m[2])+'</b></div>':'<div class="q1a-row"><span>'+l+'</span></div>'}).join('')+'<div class="q1a-bar2"></div><div class="q1a-thx">THANK YOU!</div></div>'},
 ticket:function(w){var L=lines(w);return '<div class="q1a-ticket"><div class="q1a-tm"><small>'+esc(w.kind.toUpperCase())+'</small>'+L.map(function(l,i){return i===0?'<h4>'+l+'</h4>':'<p>'+l+'</p>'}).join('')+'</div><div class="q1a-ts"><span>ADMIT<br>ONE</span><i></i></div></div>'},
 menu:function(w){var L=lines(w);return '<div class="q1a-menu"><div class="q1a-mh">'+esc(w.kind)+'</div>'+L.map(function(l){var m=l.replace(/<[^>]+>/g,'').match(/^(.*?)(\$\s?\d+[\d.,]*)\s*$/);return m?'<div class="q1a-mi"><span>'+esc(m[1].replace(/[:\-–]\s*$/,'').trim())+'</span><i></i><b>'+esc(m[2])+'</b></div>':'<div class="q1a-mn">'+l+'</div>'}).join('')+'</div>'},
 sign:function(w){var L=lines(w);return '<div class="q1a-sign"><span class="q1a-sc"></span><span class="q1a-sc r"></span>'+L.map(function(l,i){return '<div class="'+(i===0?'big':'')+'">'+l+'</div>'}).join('')+'</div>'},
 note:function(w){var L=lines(w);return '<div class="q1a-note"><span class="q1a-tape"></span>'+L.map(function(l){return '<div>'+l+'</div>'}).join('')+'</div>'},
 card:function(w){var L=lines(w);return '<div class="q1a-card"><div class="q1a-cf">🎉</div>'+L.map(function(l,i){return '<div class="'+(i===0?'big':'')+'">'+l+'</div>'}).join('')+'<div class="q1a-cf2">✦ ✦ ✦</div></div>'},
 poster:function(w){var L=lines(w);return '<div class="q1a-poster"><div class="q1a-ph">'+esc(w.kind)+'</div>'+L.map(function(l,i){return '<div class="'+(i===0?'big':'')+'">'+l+'</div>'}).join('')+'</div>'},
 label:function(w){var L=lines(w);return '<div class="q1a-label"><span class="q1a-hole"></span>'+L.map(function(l,i){return '<div class="'+(i===0?'big':'')+'">'+l+'</div>'}).join('')+'</div>'},
 board:function(w){var L=lines(w);return '<div class="q1a-board"><div class="q1a-bh">'+esc(w.kind)+'</div>'+L.map(function(l){return '<div class="q1a-br">'+l+'</div>'}).join('')+'</div>'},
 app:function(w){var L=lines(w);return '<div class="q1a-app"><div class="q1a-ah"><span>9:41</span><b>'+esc(w.kind)+'</b></div>'+L.map(function(l,i){return '<div class="q1a-ar '+(i===0?'big':'')+'">'+l+'</div>'}).join('')+'</div>'},
 paper:function(w){var L=lines(w);return '<div class="q1a-paper"><span class="q1a-tape"></span>'+L.map(function(l,i){return '<div class="'+(i===0?'big':'')+'">'+l+'</div>'}).join('')+'</div>'}};
function illustrateArtifact(b,p){var w=p.artifact;if(!w||!w.lines)return;var box=$('.q1-sign',b);if(!box||box.dataset.ill)return;var k=kindOf(w.kind);var fn=ART[k]||ART.paper;
  var wrap=document.createElement('div');wrap.className='q1a-wrap q1a-'+k+'-w';wrap.innerHTML=fn(w);wrap.dataset.ill='1';box.parentNode.replaceChild(wrap,box)}
/* ================= ligação ================= */
var previous=window.RL_REGISTER;
window.RL_REGISTER=function(R,A){if(previous)previous(R,A);var orig=R.q1;if(!orig)return;
  R.q1=function(p,b){try{window.__LESSON=A.lesson&&A.lesson()}catch(z){}clearTransient();orig(p,b);
    try{if(p.kind==='artifact')illustrateArtifact(b,p);if(NARR[p.kind])addNarrate(b,p);if(p.kind==='facts')wireFacts(b,p);if(p.kind==='compare')wireCompare(b,p);frameCoach(p,b)}catch(err){try{console.error(err)}catch(z){}}}};
})();
