/* Aula Quest · mochila ampliada, verbos em peças coloridas, aplicação em situação, expressões comuns (tudo com tradução) */
(function(){'use strict';
var V=window.L1VIS,D=window.L1DECOR;if(!V||!D)return;
var H=V.H,$=V.$,$$=V.$$,stage=V.stage,toast=V.toast;
function heroInto(host,art){var h=$('.q1v-hero',host);if(h)h.innerHTML=stage(art&&art.pair?art.pair[1]:art,'scene')}
function shell(b,art){b.innerHTML='<div class="q1v-split"><div class="q1v-hero"></div><div class="q1v-main"></div></div>';heroInto(b,art);return $('.q1v-main',b)}
function esc(s){return String(s==null?'':s).replace(/[.*+?^${}()|[\]\\]/g,'\\$&')}
function mark(en,form){return H(en).replace(new RegExp('\\b('+esc(form)+')\\b','i'),'<mark>$1</mark>')}
/* ---- mochila: palavras ---- */
D.reviewwords=function(p,b,art,A){var n=0,ws=p.words||[],m=shell(b,art);
  m.innerHTML='<div class="q1-card q1v-bag"><span class="q1-eyebrow">🎒 Mochila · palavras</span><p>Veja a figura, lembre a palavra em inglês e toque para conferir o significado.</p><div class="q1v-wgrid">'+ws.map(function(w,i){return '<button type="button" class="q1v-wc" data-i="'+i+'"><span class="q1v-be">'+H(w.e)+'</span><b>'+H(w.w)+'</b><small>toque para ver</small></button>'}).join('')+'</div></div>';
  $$(b,'.q1v-wc').forEach(function(x){x.onclick=function(e){var w=ws[+x.dataset.i];A.say(w.w);if(!x.classList.contains('on')){x.classList.add('on');$('small',x).textContent=w.pt;n++;try{A.gain(3,true,e)}catch(z){}if(n>=ws.length){A.mark();toast('🎒 Palavras revisadas!')}}}})};
/* ---- mochila: fale ---- */
D.reviewsay=function(p,b,art,A){var its=p.items||[],m=shell(b,art);
  m.innerHTML='<div class="q1-card q1v-bag"><span class="q1-eyebrow">🎒 Mochila · fale</span><p>Ouça, repita em voz alta e veja sua nota.</p>'+its.map(function(it,i){return '<div class="q1v-sayrow"><div class="q1v-sayt"><b>'+H(it.en)+'</b><small>'+H(it.pt)+'</small></div><button type="button" class="q1v-spk" data-i="'+i+'" aria-label="Ouvir">🔊</button><div class="q1v-sayc" data-i="'+i+'"></div></div>'}).join('')+'</div>';
  $$(b,'.q1v-spk').forEach(function(x){x.onclick=function(){A.say(its[+x.dataset.i].en)}});
  $$(b,'.q1v-sayc').forEach(function(h){var it=its[+h.dataset.i];try{if(window.PogVoice)PogVoice.mount(h,{target:it.en,lang:'en-US',onDone:function(r){if(r.score>=70){try{A.gain(10,true)}catch(z){}toast('🎤 '+r.score+'%')}}})}catch(z){}});A.mark()};
/* ---- verbos em peças coloridas (formas + exemplo traduzido) ---- */
D.verbs=function(p,b,art,A){var vs=p.verbs||[],m=shell(b,art),seen=0;
  m.innerHTML=vs.map(function(v,vi){return '<div class="q1-card q1v-verb" data-v="'+vi+'"><div class="q1v-vh"><span class="q1v-vic">'+H(v.ic)+'</span><b class="q1v-vv">'+H(v.v)+'</b><span class="q1v-vpt">'+H(v.pt)+'</span></div><div class="q1v-vfs">'+v.forms.map(function(f,i){return '<button type="button" class="q1v-vf f'+i+(i===0?' on':'')+'" data-i="'+i+'"><small>'+H(f.k)+'</small><b>'+H(f.en)+'</b></button>'}).join('')+'</div><div class="q1v-vex"></div><div class="q1v-vn">💡 '+H(v.note)+'</div></div>'}).join('');
  function show(card,i){var v=vs[+card.dataset.v],f=v.forms[i];$$(card,'.q1v-vf').forEach(function(x,j){x.classList.toggle('on',j===i)});$('.q1v-vex',card).innerHTML='<span class="q1v-ven">'+mark(f.ex,f.en)+'</span><small class="q1v-vpt2">'+H(f.pt)+'</small>'}
  $$(b,'.q1v-verb').forEach(function(card){show(card,0);$$(card,'.q1v-vf').forEach(function(x){x.onclick=function(e){var i=+x.dataset.i,v=vs[+card.dataset.v];show(card,i);A.say(v.forms[i].ex);if(!card.dataset.s){card.dataset.s='1';seen++;try{A.gain(5,true,e)}catch(z){}if(seen>=vs.length)A.mark()}}})});A.mark()};
/* ---- aplique os verbos: situação com lacuna ---- */
D.verbplay=function(p,b,art,A){var its=p.items||[],k=0,ok=0,m=shell(b,art);
  function draw(){if(k>=its.length){m.innerHTML='<div class="q1-card q1v-vp"><span class="q1-eyebrow">Aplique os verbos</span><h3>🎉 '+ok+' de '+its.length+' na primeira tentativa!</h3><p>Releia as formas dos verbos e volte aqui amanhã.</p></div>';try{A.confetti();A.mark()}catch(z){}return}
    var it=its[k],first=true;m.innerHTML='<div class="q1-card q1v-vp"><span class="q1-eyebrow">Aplique os verbos · '+(k+1)+'/'+its.length+'</span><p class="q1v-scene">🎬 '+H(it.scene)+'</p><h3 class="q1v-gap">'+H(it.en).replace('___','<span class="q1v-blank">___</span>')+'</h3><div class="q1v-vopts">'+it.opts.map(function(o,i){return '<button type="button" class="q1v-vo c'+i+'" data-i="'+i+'">'+H(o)+'</button>'}).join('')+'</div><p class="q1-feedback"></p></div>';
    $$(m,'.q1v-vo').forEach(function(x){x.onclick=function(e){var i=+x.dataset.i,good=i===it.ans;if(good){$('.q1v-blank',m).textContent=it.opts[i];$('.q1v-blank',m).classList.add('ok');$$(m,'.q1v-vo').forEach(function(y){y.disabled=true});x.classList.add('right');var full=it.en.replace('___',it.opts[i]);$('.q1-feedback',m).innerHTML='✅ '+H(full)+'<br><b>'+H(it.pt)+'</b> · '+H(it.why);A.say(full);try{A.gain(first?12:4,true,e)}catch(z){}if(first)ok++;setTimeout(function(){k++;draw()},2400)}else{x.classList.add('wrong');x.disabled=true;first=false;$('.q1-feedback',m).textContent='🔁 Quase! Pense na pessoa e no tempo da frase.';try{A.gain(0,false,e)}catch(z){}}}})}
  draw()};
/* ---- expressões comuns ---- */
D.exprs=function(p,b,art,A){var its=p.items||[],m=shell(b,art),n=0;
  m.innerHTML='<div class="q1-card q1v-ex"><span class="q1-eyebrow">Expressões comuns · toque para ouvir</span><div class="q1v-exg">'+its.map(function(x,i){return '<button type="button" class="q1v-exc c-'+H(x.c)+'" data-i="'+i+'"><b>'+H(x.en)+'</b><span>'+H(x.pt)+'</span><small>'+H(x.ex)+'</small><em>'+H(x.exp)+'</em></button>'}).join('')+'</div></div>';
  $$(b,'.q1v-exc').forEach(function(x){x.onclick=function(e){var it=its[+x.dataset.i];A.say(it.en);if(!x.classList.contains('on')){x.classList.add('on');n++;try{A.gain(3,true,e)}catch(z){}if(n>=its.length)A.mark()}}});A.mark()};
D.exprplay=function(p,b,art,A){var its=p.items||[],k=0,m=shell(b,art);
  function draw(){if(k>=its.length){m.innerHTML='<div class="q1-card q1v-vp"><span class="q1-eyebrow">Qual expressão usar?</span><h3>🎉 Você escolheu a expressão certa para cada situação!</h3></div>';try{A.confetti();A.mark()}catch(z){}return}
    var it=its[k];m.innerHTML='<div class="q1-card q1v-vp"><span class="q1-eyebrow">Qual expressão usar? · '+(k+1)+'/'+its.length+'</span><h3>'+H(it.cue)+'</h3><div class="q1-options">'+it.opts.map(function(o,i){return '<button type="button" data-answer="'+i+'">'+H(o)+'</button>'}).join('')+'</div><p class="q1-feedback"></p></div>';
    $$(m,'[data-answer]').forEach(function(x){x.onclick=function(e){var i=+x.dataset.answer,good=i===it.ans;$$(m,'[data-answer]').forEach(function(y){y.disabled=true;if(+y.dataset.answer===it.ans)y.classList.add('right')});if(!good)x.classList.add('wrong');$('.q1-feedback',m).textContent=(good?'✅ ':'💡 ')+it.why;try{A.gain(good?10:0,good,e);A.say(it.opts[it.ans])}catch(z){}setTimeout(function(){k++;draw()},2000)}})}
  draw()};
})();
