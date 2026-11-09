/* Aula Quest 1 · atividades modernas: mini-diálogo com palavras que trocam, escolha com cena, vocabulário/sons com microfone, molde, roleplay dinâmico, escrita */
(function(){'use strict';
var V=window.L1VIS;if(!V)return;var H=V.H,$=V.$,$$=V.$$,stage=V.stage,ANA=V.ANA,EV=V.EV,toast=V.toast,split=window.L1SPLIT,heroEl=window.L1HERO;
var DECOR=window.L1DECOR;
function sup(){return !!(window.PogVoice&&PogVoice.supported&&PogVoice.supported())}
/* ---- linhas com palavras que trocam: {a|b|c}; o pt acompanha pelo mesmo índice ---- */
function parse(en,pt){var e=String(en).split(/\{([^{}]+)\}/),q=String(pt||'').split(/\{([^{}]+)\}/),o=[];var stat=String(pt||'').indexOf('{')<0?String(pt||''):null;for(var k=0;k<e.length;k++){if(k%2===0)o.push({t:e[k],p:q[k]!=null?q[k]:''});else o.push({sw:e[k].split('|'),pw:(q[k]||'').split('|'),i:0})}o.ptStatic=stat;return o}
function txt(parts){return parts.map(function(p){return p.t!=null?p.t:p.sw[p.i]}).join('')}
function ptxt(parts){if(parts.ptStatic!=null)return parts.ptStatic;return parts.map(function(p){return p.t!=null?p.p:(p.pw[p.i]||p.pw[0]||'')}).join('')}
var FACES={};function swapBox(host,lines,A,o){o=o||{};var P=lines.map(function(l){return{who:l.who,parts:parse(l.en,l.pt)}}),touched={},total=0,showPt=false,tok=0;P.forEach(function(l){l.parts.forEach(function(p){if(p.sw)total++})});
  function face(w){try{return A.face(FACES[w]||w)}catch(e){return ''}}
  function draw(){host.innerHTML=P.map(function(l,i){return '<div class="q1v-ln'+(l.who===o.me?' me':'')+'" data-i="'+i+'"><span class="q1v-av">'+face(l.who)+'</span><div class="q1v-tb"><b>'+H(l.who)+'</b><span>'+l.parts.map(function(p,k){return p.t!=null?H(p.t):'<button type="button" class="q1sw" data-l="'+i+'" data-k="'+k+'">'+H(p.sw[p.i])+'</button>'}).join('')+'</span>'+(showPt?'<small>'+H(ptxt(l.parts))+'</small>':'')+'</div><button type="button" class="q1v-spk" data-s="'+i+'" aria-label="Ouvir">🔊</button></div>'}).join('');
   $$(host,'.q1sw').forEach(function(b){b.onclick=function(e){var l=P[+b.dataset.l],p=l.parts[+b.dataset.k];p.i=(p.i+1)%p.sw.length;var key=b.dataset.l+'-'+b.dataset.k;if(!touched[key]){touched[key]=1;try{A.gain(4,true,e)}catch(x){}if(o.onProgress)o.onProgress(Object.keys(touched).length,total)}draw();A.say(txt(l.parts))}});
   $$(host,'[data-s]').forEach(function(b){b.onclick=function(){A.say(txt(P[+b.dataset.s].parts))}})}
  draw();
  return{total:total,pt:function(on){showPt=on;draw()},shuffle:function(){P.forEach(function(l){l.parts.forEach(function(p){if(p.sw)p.i=Math.floor(Math.random()*p.sw.length)})});draw()},
    play:async function(){var my=++tok;for(var i=0;i<P.length;i++){if(my!==tok)return;$$(host,'.q1v-ln').forEach(function(x,j){x.classList.toggle('on',j===i)});await A.sayP(txt(P[i].parts))}$$(host,'.q1v-ln').forEach(function(x){x.classList.remove('on')})}}}
function bar(buttons){return '<div class="q1v-bar">'+buttons.map(function(x){return '<button type="button" class="q1v-b" data-a="'+x[0]+'">'+x[1]+'</button>'}).join('')+'<span class="q1v-prog"></span></div>'}
/* ---- reconhecimento de fala simples: reconhece frase própria com a palavra ---- */
function micSay(host,word,A,done){host.innerHTML='';var okd=false;
  if(sup()){host.innerHTML='<button type="button" class="q1v-mic">🎤 <span>Frase sua com “'+H(word)+'”</span><i class="q1v-wv"><b></b><b></b><b></b><b></b></i></button><div class="q1v-heard" role="status"></div>';
    var mb=$('.q1v-mic',host),hd=$('.q1v-heard',host),h=null;
    function evalT(t,e){var low=String(t||'').toLowerCase(),n=low.split(/\s+/).filter(Boolean).length,hit=low.indexOf(String(word).toLowerCase())>=0;
      if(hit&&n>=3){hd.innerHTML='✅ “'+H(t)+'”';if(!okd){okd=true;try{A.gain(15,true,e)}catch(x){}toast('🎤 Ótimo! Frase com “'+word+'”');done&&done()}return true}
      hd.innerHTML='🔁 '+(hit?'Faça uma frase completa (3 palavras ou mais).':'Use a palavra “'+H(word)+'” na sua frase.')+(t?' <small>Ouvi: “'+H(t)+'”</small>':'');return false}
    mb.onclick=function(e){if(h){h.stop();h=null;mb.classList.remove('on');return}try{speechSynthesis.cancel()}catch(x){}mb.classList.add('on');
      h=PogVoice.listen({lang:'en-US',onInterim:function(t){hd.textContent='“'+t+'”'},onDone:function(r){h=null;mb.classList.remove('on');
        if(r.error){hd.textContent=r.error==='not-allowed'?'🎙️ Permita o microfone no navegador.':'🔁 Não ouvi nada. Tente de novo.';return}
        var alts=r.alts||[''];if(!evalT(alts[0],e)){for(var i=1;i<alts.length;i++){var l=alts[i].toLowerCase();if(l.indexOf(String(word).toLowerCase())>=0&&l.split(/\s+/).length>=3){evalT(alts[i],e);break}}}}})}}
  else{host.innerHTML='<div class="q1v-type"><input placeholder="Escreva uma frase com '+H(word)+'…" aria-label="Sua frase"><button type="button" class="q1v-b">✓</button></div><div class="q1v-heard"></div>';
    $('button',host).onclick=function(e){var t=$('input',host).value,low=t.toLowerCase(),ok=low.indexOf(word.toLowerCase())>=0&&low.split(/\s+/).filter(Boolean).length>=3;$('.q1v-heard',host).textContent=ok?'✅ Boa!':'🔁 Use “'+word+'” numa frase de 3 palavras ou mais.';if(ok&&!okd){okd=true;try{A.gain(15,true,e)}catch(x){}toast('✍️ Boa frase!');done&&done()}}}}
/* ===== 3 · For here / to go: situação contextualizada + mini-diálogo de 4 falas ===== */
var MINI=[{who:'Evan',en:'Hi! What can I get for you {today|this morning|this afternoon}?',pt:'Oi! O que posso preparar para você {hoje|esta manhã|esta tarde}?'},
 {who:'Ana',en:'Can I get a {small|medium|large} {coffee|tea|latte}, please?',pt:'Posso pedir um {pequeno|médio|grande} {café|chá|latte}, por favor?'},
 {who:'Evan',en:'Sure! {For here or to go?|Is that for here or to go?|Will that be for here or to go?}',pt:'Claro! {Para ficar ou levar?|É para ficar ou levar?|Vai ficar ou levar?}'},
 {who:'Ana',en:'{To go, please.|For here, please.|To go, thanks.}',pt:'{Para levar, por favor.|Para ficar, por favor.|Para levar, obrigada.}'}];
DECOR.facts=function(p,b,art,A){var first=p.facts&&p.facts[0];FACES=p.faces||FACES;(function(){var cs=$$(b,'.q1-facts .q1-card');cs.forEach(function(c,i){var f=p.facts&&p.facts[i];if(f&&f.icon&&i>0)c.insertAdjacentHTML('afterbegin','<span class="q1v-ic">'+H(f.icon)+'</span>')})})();var mini=p.mini||(first&&/For here/.test(first.big)?MINI:null);
  if(mini){var cards=$$(b,'.q1-facts .q1-card'),sit=document.createElement('div');sit.className='q1-card q1v-sit';
    sit.innerHTML='<span class="q1-eyebrow">Situação no balcão</span><h3>'+H(first.big)+' <small>· '+H(first.label)+'</small></h3><p>'+H(first.sub)+'</p><div class="q1v-sitgrid"><div class="q1v-sitst">'+stage(p.miniart||{rs:'cafe',cast:[ANA(28),EV(72,1,{prop:'cup'})]},'scene')+'</div><div class="q1v-sitdlg"></div></div>'+bar([['play','▶ Ouvir'],['shuf','🔀 Trocar palavras'],['pt','PT']]);
    cards[0].replaceWith(sit);var grid=$('.q1-facts',b);grid.classList.add('q1v-facts2');
    var box=swapBox($('.q1v-sitdlg',sit),mini,A,{me:p.me||'Ana',onProgress:function(n,t){$('.q1v-prog',sit).textContent='🎨 '+n+'/'+t+' palavras exploradas';if(n>=t){A.confetti();toast('✨ Você explorou todas as palavras!')}}});
    $('.q1v-prog',sit).textContent='🎨 0/'+box.total+' palavras exploradas';var on=false;
    $('[data-a=play]',sit).onclick=function(){box.play()};$('[data-a=shuf]',sit).onclick=function(){box.shuffle()};$('[data-a=pt]',sit).onclick=function(){on=!on;box.pt(on)};return}
  split(b,art)};
/* ===== 17–18 · diálogos com cena e palavras que trocam ===== */
var DLG={'Conversa · o pedido':[
 {who:'Evan',en:'Hi! {What can I get for you?|How can I help you?|What would you like?}',pt:'Oi! {O que vai ser?|Como posso ajudar?|O que você gostaria?}'},
 {who:'Ana',en:'Can I get a {small coffee|large tea|medium latte}, please?',pt:'Pode ser {um café pequeno|um chá grande|um latte médio}, por favor?'},
 {who:'Evan',en:'{For here or to go?|Is that for here or to go?}',pt:'{Para ficar ou levar?|É para ficar ou levar?}'},
 {who:'Ana',en:'{To go|For here}, please. Do you have {oat milk|almond milk|soy milk}?',pt:'{Para levar|Para ficar}, por favor. Tem {leite de aveia|leite de amêndoas|leite de soja}?'},
 {who:'Evan',en:'Sorry, not today. We have {regular milk|whole milk|skim milk}.',pt:'Desculpe, hoje não. Temos {leite comum|leite integral|leite desnatado}.'},
 {who:'Ana',en:'{Regular milk is fine, thanks.|That’s fine, thanks.|OK, regular milk, please.}',pt:'{Leite comum serve, obrigada.|Tudo bem, obrigada.|Certo, leite comum, por favor.}'}],
 'Conversa · a retirada':[
 {who:'Evan',en:'{Anything else?|Would you like anything else?}',pt:'{Mais alguma coisa?|Você gostaria de mais alguma coisa?}'},
 {who:'Ana',en:'No, that’s all. How much is it?',pt:'Não, é só isso. Quanto custa?'},
 {who:'Evan',en:'{Three|Four|Five} dollars. Your order number is {12|27|8}.',pt:'{Três|Quatro|Cinco} dólares. O número do pedido é {12|27|8}.'},
 {who:'Ana',en:'Here you go. Where is the pickup counter?',pt:'Aqui está. Onde fica o balcão de retirada?'},
 {who:'Evan',en:'{On the left|On the right|Over there}, near the {window|door|menu}.',pt:'{À esquerda|À direita|Ali}, perto da {janela|porta|cardápio}.'},
 {who:'Ana',en:'Got it. {Thank you!|Thanks a lot!|Perfect, thanks!}',pt:'Entendi. {Obrigada!|Muito obrigada!|Perfeito, obrigada!}'}]};
DECOR.dialog=function(p,b,art,A){FACES=p.faces||FACES;var data=p.swaps||DLG[p.title];if(!data){split(b,art);return}
  var intro=$('.q1-intro',b),old=$('.q1-dialog',b);var wrap=document.createElement('div');wrap.className='q1v-dlgwrap';wrap.innerHTML=bar([['play','▶ Ouvir tudo'],['shuf','🔀 Trocar palavras'],['pt','PT']]);var host=document.createElement('div');host.className='q1v-dlg';wrap.insertBefore(host,wrap.firstChild);old.replaceWith(wrap);
  var sp=split(b,art);
  var box=swapBox(host,data,A,{me:p.me||'Ana',onProgress:function(n,t){$('.q1v-prog',wrap).textContent='🎨 '+n+'/'+t+' palavras exploradas'}});$('.q1v-prog',wrap).textContent='🎨 0/'+box.total+' palavras exploradas';var on=false;
  $('[data-a=play]',wrap).onclick=function(){box.play()};$('[data-a=shuf]',wrap).onclick=function(){box.shuffle()};$('[data-a=pt]',wrap).onclick=function(){on=!on;box.pt(on)}};
/* ===== 19–24 · escolha da fala: o Evan e a Ana aparecem na cena ===== */
DECOR.choice=function(p,b,art,A){split(b,art)};
function topRow(b,art){var intro=$('.q1-intro',b),row=document.createElement('div');row.className='q1v-top';var t=document.createElement('div');t.className='q1v-topt';if(intro)t.appendChild(intro);row.appendChild(t);row.appendChild(heroEl(art));b.insertBefore(row,b.firstChild)}
/* ===== 25–26 · toque, ouça e diga uma frase sua (microfone) ===== */
DECOR.vocab=function(p,b,art,A){var cards=$$(b,'.q1-vocab .q1-card'),n=0;cards.forEach(function(c,i){var w=p.words[i];if(w&&w[5]){var ic=$('.q1-vocab-icon:not(.q1-vph)',c);if(ic)ic.innerHTML='<span style="font-size:30px;line-height:1">'+H(w[5])+'</span>'}});
  cards.forEach(function(c,i){var w=(p.words[i]||[])[0];if(!w)return;var h=document.createElement('div');h.className='q1v-say';c.appendChild(h);micSay(h,w,A,function(){c.classList.add('done');n++;if(n>=cards.length){A.confetti();A.mark()}})});
  topRow(b,art)};
/* ===== 27, 28, 33 · molde que muda: cena + palavras que trocam + ouvir + falar ===== */
DECOR.pattern=function(p,b,art,A){var sel={};p.slots.forEach(function(s){sel[s.key]=0});var used={};
  b.innerHTML='<div class="q1v-split"><div class="q1v-hero"></div><div class="q1v-main"><div class="q1-card q1v-mold"><span class="q1-eyebrow">Molde que muda · toque nas palavras</span><div class="q1v-sent"></div><div class="q1v-slots"></div><div class="q1v-bar"><button type="button" class="q1v-b" data-a="say">🔊 Ouvir</button><button type="button" class="q1v-b" data-a="shuf">🔀 Surpreenda-me</button><span class="q1v-prog"></span></div><div class="q1v-micwrap"></div></div><div class="q1-card"><b>Compare e produza</b><p>'+H(p.model)+'</p><p>'+H(p.note)+'</p></div></div></div>';
  var hero=$('.q1v-hero',b);hero.innerHTML=stage(art.pair?art.pair[1]:art,'scene');
  function cur(){var f=p.frame;p.slots.forEach(function(s){f=f.replace('{'+s.key+'}',s.opts[sel[s.key]])});return f}
  function draw(){var f=H(p.frame);p.slots.forEach(function(s){f=f.replace('{'+s.key+'}','<mark class="q1sw2">'+H(s.opts[sel[s.key]])+'</mark>')});$('.q1v-sent',b).innerHTML=f;
   $('.q1v-slots',b).innerHTML=p.slots.map(function(s){return '<div class="q1v-row"><label>'+H(s.key)+'</label><div class="q1v-chips">'+s.opts.map(function(o,i){return '<button type="button" class="q1v-chip'+(sel[s.key]===i?' on':'')+'" data-k="'+s.key+'" data-i="'+i+'">'+H(o)+'</button>'}).join('')+'</div></div>'}).join('');
   $$(b,'.q1v-chip').forEach(function(x){x.onclick=function(e){sel[x.dataset.k]=+x.dataset.i;var key=x.dataset.k+x.dataset.i;if(!used[key]){used[key]=1;try{A.gain(4,true,e)}catch(z){}}draw();A.say(cur());$('.q1v-prog',b).textContent='🎨 '+Object.keys(used).length+' combinações'+(Object.keys(used).length>=6?' ✓':'')}});
   var mw=$('.q1v-micwrap',b);mw.innerHTML='';try{if(window.PogVoice)PogVoice.mount(mw,{target:cur(),lang:'en-US',onDone:function(r){if(r.score>=70){try{A.gain(15,true)}catch(e){}toast('🎤 '+r.score+'% — muito bom!')}}})}catch(e){}}
  $('[data-a=say]',b).onclick=function(){A.say(cur())};$('[data-a=shuf]',b).onclick=function(){p.slots.forEach(function(s){sel[s.key]=Math.floor(Math.random()*s.opts.length)});draw();A.say(cur())};draw();A.mark()};
/* ===== 29 · laboratório de sons: ouvir, repetir e receber nota ===== */
DECOR.sound=function(p,b,art,A){var cards=$$(b,'.q1-facts .q1-card');
  cards.forEach(function(c,i){var pair=p.pairs[i];if(!pair)return;var h=document.createElement('div');h.className='q1v-soundmic';c.appendChild(h);try{if(window.PogVoice)PogVoice.mount(h,{target:pair[0],lang:'en-US',onDone:function(r){if(r.score>=70){try{A.gain(12,true)}catch(e){}toast('🎤 '+r.score+'% — '+pair[0])}}})}catch(e){}});
  topRow(b,art)};
/* ===== 32 · roleplay dinâmico: alternativas que se encaixam e o mini-diálogo se recria ===== */
var ROLE=[{npc:'Hi! What can I get for you?',opts:[['Can I get a large latte, please?','Posso pedir um latte grande, por favor?','Sure! One large latte. For here or to go?'],['Can I get a small tea, please?','Posso pedir um chá pequeno, por favor?','Sure! One small tea. For here or to go?'],['Hi! A medium coffee, please.','Oi! Um café médio, por favor.','Great! One medium coffee. For here or to go?']]},
 {npc:null,opts:[['To go, please.','Para levar, por favor.','No problem. Anything else?'],['For here, please.','Para ficar, por favor.','Nice! Take a seat anywhere. Anything else?'],['Can I have it to go, please?','Posso levar, por favor?','Of course! Anything else?']]},
 {npc:null,opts:[['No, that’s all. How much is it?','Não, é só isso. Quanto custa?','That’s four dollars.'],['Do you have oat milk?','Vocês têm leite de aveia?','Sorry, not today. We have regular milk. That’s four dollars.'],['Yes, a muffin, please.','Sim, um muffin, por favor.','Sure! That’s six dollars.']]},
 {npc:null,opts:[['Here you go. Thanks!','Aqui está. Obrigada!','Thank you! Your number is 12. Pick it up on the left.'],['Can I pay by card?','Posso pagar com cartão?','Sure! Tap your card here. Your number is 12. Pick it up on the left.'],['Here’s ten dollars.','Aqui estão dez dólares.','Thanks! Here’s your change. Your number is 12. Pick it up on the left.']]}];
DECOR.role=function(p,b,art,A){FACES=p.faces||FACES;if(!p.turns&&p.solo&&p.t&&p.stage&&A.lesson().n!==1){split(b,art);return}var ROLE_=p.turns||ROLE,ME=p.me||'Ana',NPC=p.npcname||'Evan';var group=false,k=0,log=[];var compl=p.change[Math.floor(Math.random()*p.change.length)];
  b.innerHTML='<div class="q1v-split"><div class="q1v-hero"></div><div class="q1v-main"><div class="q1-card q1v-role"><span class="q1-eyebrow">'+'Missão ao vivo · roleplay'+'</span><p class="q1v-compl">⚡ Complicação possível: <b>'+H(compl)+'</b></p><div class="q1v-log"></div><div class="q1v-opts"></div></div></div></div>';
  $('.q1v-hero',b).innerHTML=stage(art,'scene');var log$=$('.q1v-log',b),opts$=$('.q1v-opts',b);
  function bub(who,t,me){var f='';try{f=A.face(who)}catch(e){}return '<div class="q1v-ln'+(me?' me':'')+'"><span class="q1v-av">'+f+'</span><div class="q1v-tb"><b>'+who+'</b><span>'+H(t)+'</span></div><button type="button" class="q1v-spk" data-t="'+H(t)+'">🔊</button></div>'}
  function draw(){var h=log.slice(-4).map(function(x){return bub(x.who,x.en,x.me)}).join('');log$.innerHTML=h;$$(log$,'[data-t]').forEach(function(x){x.onclick=function(){A.say(x.dataset.t)}});
   if(k>=ROLE_.length){opts$.innerHTML='<div class="q1v-bar"><button class="q1v-b" data-a="all">▶ Ouvir a conversa</button><button class="q1v-b" data-a="again">↺ Outra versão</button></div><p class="q1-note">'+'Professor ou colega: registre uma fala clara e uma reformulação.'+'</p>';try{A.confetti();A.gain(20,true);A.mark()}catch(e){}$('[data-a=all]',opts$).onclick=async function(){for(var i=0;i<log.length;i++){await A.sayP(log[i].en)}};$('[data-a=again]',opts$).onclick=function(){k=0;start()};return}
   var t=ROLE_[k];opts$.innerHTML='<div class="q1v-q">Sua vez, '+H(ME)+' — escolha o que dizer:</div>'+t.opts.map(function(o,i){return '<button type="button" class="q1v-opt" data-i="'+i+'">'+H(o[0])+'<small>'+H(o[1])+'</small></button>'}).join('');
   $$(opts$,'.q1v-opt').forEach(function(x){x.onclick=function(e){var o=t.opts[+x.dataset.i];log.push({who:ME,en:o[0],me:true});try{A.gain(8,true,e);A.say(o[0])}catch(z){}log.push({who:NPC,en:o[2]});k++;draw();setTimeout(function(){A.say(o[2])},600)}})}
  function start(){log=[{who:NPC,en:ROLE_[0].npc}];draw();setTimeout(function(){A.say(ROLE_[0].npc)},400)}start()};
/* ===== 34 · escrita lúdica: fale ou escreva, confira sozinho ===== */
DECOR.writing=function(p,b,art,A){var ta=$('textarea',b),checks=$$(b,'.q1-check input');
  var tools=document.createElement('div');tools.className='q1v-tools';tools.innerHTML=(sup()?'<button type="button" class="q1v-mic" id="q1fm">🎤 <span>Falar</span><i class="q1v-wv"><b></b><b></b><b></b><b></b></i></button>':'')+'<button type="button" class="q1v-b" id="q1fc">✓ Conferir</button><button type="button" class="q1v-b" id="q1fv">👀 Ver modelo</button><div class="q1v-fb" role="status"></div>';
  ta.parentNode.insertBefore(tools,ta.nextSibling);
  function check(e){var t=ta.value.toLowerCase(),n=t.split(/\s+/).filter(Boolean).length;var kw=(p.kw||[]),c1=kw.length?kw.filter(function(w){return t.indexOf(w)>=0}).length>=2:(/(coffee|tea|latte)/.test(t)&&/(small|medium|large)/.test(t)),c2=/\?/.test(t),c3=/(thanks|thank you|bye|see you)/.test(t);
   [c1,c2,c3].forEach(function(v,i){if(checks[i])checks[i].checked=!!v});var stars=(c1?1:0)+(c2?1:0)+(c3?1:0);
   $('.q1v-fb',tools).innerHTML='<span class="q1v-st">'+'★'.repeat(stars)+'☆'.repeat(3-stars)+'</span> '+(n<4?'Escreva ou diga pelo menos uma frase completa.':stars===3?'Excelente! Agora faça uma segunda versão mudando bebida, tamanho e horário.':'Quase! '+(!c1?'Inclua bebida e tamanho. ':'')+(!c2?'Faça uma pergunta. ':'')+(!c3?'Termine com uma despedida natural.':''));
   if(n>=4&&stars>=1){try{A.gain(8+stars*8,true,e)}catch(z){}if(stars===3){try{A.confetti()}catch(z){}toast('⭐ Missão cumprida!')}}}
  $('#q1fc',tools).onclick=check;$('#q1fv',tools).onclick=function(){ta.value=p.model;check()};
  var mb=$('#q1fm',tools);if(mb){var h=null;mb.onclick=function(e){if(h){h.stop();h=null;mb.classList.remove('on');return}mb.classList.add('on');h=PogVoice.listen({lang:'en-US',maxMs:15000,onInterim:function(t){ta.value=t},onDone:function(r){h=null;mb.classList.remove('on');if(r.error){$('.q1v-fb',tools).textContent=r.error==='not-allowed'?'🎙️ Permita o microfone no navegador.':'🔁 Não ouvi nada. Tente de novo.';return}ta.value=(r.alts||[''])[0];check(e)}})}}
  split(b,art)};
/* ===== helpers ===== */
function rich(s){return H(s).replace(/\*\*(.+?)\*\*/g,'<strong>$1</strong>')}
function shuffleArr(a,seed){a=a.slice();var s=seed||7;function rnd(){s=(s*9301+49297)%233280;return s/233280}for(var i=a.length-1;i>0;i--){var j=Math.floor(rnd()*(i+1)),t=a[i];a[i]=a[j];a[j]=t}return a}
function heroInto(host,art){var h=$('.q1v-hero',host);if(h)h.innerHTML=stage(art&&art.pair?art.pair[1]:art,'scene')}
var TIP=null;function tip(){if(!TIP){TIP=document.createElement('div');TIP.className='q1v-tip';TIP.hidden=true;document.body.appendChild(TIP)}return TIP}
/* ===== leitura guiada: passe o mouse e veja a tradução ===== */
DECOR.reading=function(p,b,art,A){tip().hidden=true;var card=$('.q1-text',b),side=$('.q1-reading-side',b);
  if(side){var col=document.createElement('div');col.className='q1v-col';side.replaceWith(col);col.appendChild(heroEl(art));col.appendChild(side)}
  if(!(p.sentences&&card))return;
  $$(card,':scope > p').forEach(function(el,i){var ss=p.sentences[i];if(!ss)return;el.innerHTML=ss.map(function(s,k){return '<span class="q1v-sn" tabindex="0" data-i="'+i+'" data-k="'+k+'">'+rich(s.en)+'</span>'}).join(' ')});
  var bar=document.createElement('div');bar.className='q1v-trans';bar.innerHTML='<span>🔤</span><div><b>Leitura guiada.</b> Passe o mouse (ou toque) em uma frase para ver a tradução; clique para ouvir.<div class="q1v-trline"></div></div>';card.insertBefore(bar,$('.q1-actions',card));
  function show(el,pin){var s=p.sentences[+el.dataset.i][+el.dataset.k],t=tip();t.textContent=String(s.pt).replace(/\*\*/g,'');t.hidden=false;var r=el.getBoundingClientRect();t.style.left=Math.max(8,Math.min(innerWidth-t.offsetWidth-8,r.left+r.width/2-t.offsetWidth/2))+'px';t.style.top=Math.max(8,r.top-t.offsetHeight-8)+'px';if(pin)$('.q1v-trline',bar).textContent=String(s.pt).replace(/\*\*/g,'')}
  $$(card,'.q1v-sn').forEach(function(el){el.onmouseenter=function(){show(el,false)};el.onmouseleave=function(){tip().hidden=true};el.onfocus=function(){show(el,true)};el.onblur=function(){tip().hidden=true};el.onclick=function(){show(el,true);A.say(String(p.sentences[+el.dataset.i][+el.dataset.k].en).replace(/\*\*/g,''))}})};
/* ===== mochila de revisão (começo da aula) ===== */
DECOR.review=function(p,b,art,A){var n=0,items=p.items||[];
  b.innerHTML='<div class="q1v-split"><div class="q1v-hero"></div><div class="q1v-main"><div class="q1-card q1v-bag"><span class="q1-eyebrow">🎒 Mochila de revisão</span><p>Antes de começar, lembre o que você já sabe. Toque no cartão: pense, diga em voz alta e confira a tradução.</p><div class="q1v-bagrid">'+items.map(function(it,i){return '<button type="button" class="q1v-bc" data-i="'+i+'"><span class="q1v-be">'+H(it.e)+'</span><b>'+H(it.en)+'</b><small>toque para ver</small></button>'}).join('')+'</div></div></div></div>';heroInto(b,art);
  $$(b,'.q1v-bc').forEach(function(x){x.onclick=function(e){var it=items[+x.dataset.i];A.say(it.en);if(!x.classList.contains('on')){x.classList.add('on');$('small',x).textContent=it.pt;n++;try{A.gain(4,true,e)}catch(z){}if(n>=items.length){A.mark();toast('🎒 Mochila revisada!')}}}})};
/* ===== laboratório de sons completo (3 quadros) ===== */
DECOR.soundlab=function(p,b,art,A){var part=p.part;
  if(part===1){b.innerHTML='<div class="q1v-split"><div class="q1v-hero"></div><div class="q1v-main"><div class="q1-card q1v-sl"><span class="q1-eyebrow">Laboratório de sons · '+H(p.focus)+'</span><div class="q1v-slrow"><span class="q1v-slic">👂</span><div><b>O que é</b><p>'+H(p.what)+'</p></div></div><div class="q1v-slrow"><span class="q1v-slic">👄</span><div><b>Como fazer</b><p>'+H(p.how)+'</p></div></div><div class="q1v-slwords">'+p.words.map(function(w,i){return '<button type="button" class="q1v-slw" data-i="'+i+'"><b>'+H(w.w)+'</b><small>'+H(w.pt)+'</small><span>🔊</span></button>'}).join('')+'</div><div class="q1v-sltip">💡 '+H(p.tip)+'</div></div></div></div>';heroInto(b,art);
    $$(b,'.q1v-slw').forEach(function(x){x.onclick=function(){A.say(p.words[+x.dataset.i].w)}});A.mark();return}
  if(part===2){var k=0,ok=0,pairs=p.pairs;b.innerHTML='<div class="q1v-split"><div class="q1v-hero"></div><div class="q1v-main"><div class="q1-card q1v-sl"><span class="q1-eyebrow">Ouça e escolha · <span class="q1v-slc"></span></span><h3>Qual você ouviu?</h3><div class="rl-bar"><button type="button" class="q1v-b" data-a="play">🔊 Ouvir</button><button type="button" class="q1v-b" data-a="slow">🐢 Devagar</button></div><div class="q1v-slopts"></div><p class="q1-feedback"></p></div></div></div>';heroInto(b,art);
    function round(){var pr=pairs[k],first=shuffleArr([0,1],k+3)[0],target=first?pr.b:pr.a;$('.q1v-slc',b).textContent=(k+1)+'/'+pairs.length;var opts=shuffleArr([pr.a,pr.b],k+9);$('.q1v-slopts',b).innerHTML=opts.map(function(o){return '<button type="button" class="q1v-slo" data-o="'+H(o)+'">'+H(o)+'</button>'}).join('');$('.q1-feedback',b).textContent='';
      $('[data-a=play]',b).onclick=function(){A.say(target)};$('[data-a=slow]',b).onclick=function(){A.say(target,.6)};setTimeout(function(){A.say(target)},350);
      $$(b,'.q1v-slo').forEach(function(x){x.onclick=function(e){var good=x.dataset.o===target;x.classList.add(good?'right':'wrong');$$(b,'.q1v-slo').forEach(function(y){y.disabled=true});try{A.gain(good?10:0,good,e)}catch(z){}if(good)ok++;$('.q1-feedback',b).textContent=good?'✅ Isso! Você ouviu “'+target+'”.':'🔁 Ouça de novo: era “'+target+'”.';setTimeout(function(){k++;if(k<pairs.length)round();else{$('.q1v-slopts',b).innerHTML='<div class="q1v-sldone">🎧 '+ok+' de '+pairs.length+' — ótimo ouvido!</div>';A.mark()}},1300)}})}
    round();return}
  b.innerHTML='<div class="q1v-split"><div class="q1v-hero"></div><div class="q1v-main"><div class="q1-card q1v-sl"><span class="q1-eyebrow">Agora diga você</span><h3>'+H(p.phrase.en)+'</h3><p class="q1-note">'+H(p.phrase.pt)+'</p><div class="rl-bar"><button type="button" class="q1v-b" data-a="n">🔊 Normal</button><button type="button" class="q1v-b" data-a="s">🐢 Devagar</button></div><div class="q1v-micwrap"></div><div class="q1v-sltip">💡 '+H(p.tip)+'</div></div></div></div>';heroInto(b,art);
  $('[data-a=n]',b).onclick=function(){A.say(p.phrase.en)};$('[data-a=s]',b).onclick=function(){A.say(p.phrase.en,.6)};
  try{if(window.PogVoice)PogVoice.mount($('.q1v-micwrap',b),{target:p.phrase.en,lang:'en-US',onDone:function(r){if(r.score>=70){try{A.gain(15,true);A.mark()}catch(e){}toast('🎤 '+r.score+'% — muito bem!')}}})}catch(e){}A.mark()};
/* ===== sem consultar: monte a frase com as palavras e diga em voz alta ===== */
DECOR.exit=function(p,b,art,A){var items=p.items||[],k=0;
  b.innerHTML='<div class="q1v-split"><div class="q1v-hero"></div><div class="q1v-main"><div class="q1-card q1v-game"></div></div></div>';heroInto(b,art);var box=$('.q1v-game',b);
  function nz(s){return String(s).toLowerCase().replace(/[^a-z0-9’' ]/g,'').replace(/\s+/g,' ').trim()}
  function draw(){if(k>=items.length){box.innerHTML='<span class="q1-eyebrow">Sem consultar</span><h3>🎉 Você montou e disse as '+items.length+' frases sozinho!</h3><p>Volte a este jogo amanhã, sem olhar a aula.</p>';try{A.confetti();A.mark()}catch(e){}return}
    var it=items[k],words=shuffleArr(it.target.split(/\s+/),k*5+3),picked=[];
    box.innerHTML='<span class="q1-eyebrow">Sem consultar · '+(k+1)+'/'+items.length+'</span><h3>'+H(it.cue)+'</h3><div class="q1v-built" aria-live="polite"></div><div class="q1v-bank"></div><p class="q1-feedback"></p><div class="q1v-micwrap"></div><button type="button" class="q1v-b q1v-nx" hidden>Próxima ›</button>';
    function paint(){$('.q1v-built',box).innerHTML=picked.map(function(w,i){return '<button type="button" class="q1v-chip on" data-r="'+i+'">'+H(words[w])+'</button>'}).join('')||'<span class="q1-note">Toque nas palavras na ordem certa…</span>';
      $('.q1v-bank',box).innerHTML=words.map(function(w,i){return picked.indexOf(i)>=0?'':'<button type="button" class="q1v-chip" data-a="'+i+'">'+H(w)+'</button>'}).join('');
      $$(box,'.q1v-bank .q1v-chip').forEach(function(x){x.onclick=function(e){picked.push(+x.dataset.a);paint();if(picked.length===words.length)check(e)}});
      $$(box,'.q1v-built .q1v-chip').forEach(function(x){x.onclick=function(){picked.splice(+x.dataset.r,1);paint()}})}
    function check(e){var s=picked.map(function(i){return words[i]}).join(' ');if(nz(s)===nz(it.target)){$('.q1-feedback',box).textContent='✅ Isso! Agora diga em voz alta.';try{A.gain(12,true,e)}catch(z){}A.say(it.target);$$(box,'.q1v-chip').forEach(function(c){c.disabled=true});var mw=$('.q1v-micwrap',box);try{if(window.PogVoice)PogVoice.mount(mw,{target:it.target,lang:'en-US',onDone:function(r){if(r.score>=70){try{A.gain(10,true)}catch(z){}toast('🎤 '+r.score+'%')}}})}catch(z){}$('.q1v-nx',box).hidden=false;$('.q1v-nx',box).onclick=function(){k++;draw()}}
      else{$('.q1-feedback',box).textContent='🔁 Quase! Toque numa palavra para tirar e tente outra ordem.';try{A.gain(0,false,e)}catch(z){}}}
    paint()}
  draw()};
})();
