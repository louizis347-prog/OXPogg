/* Aula Quest · ponte português → inglês: apresenta o vocabulário novo antes de ele aparecer, de forma lúdica */
(function(){'use strict';
var V=window.L1VIS,D=window.L1DECOR;if(!V||!D)return;
var H=V.H,$=V.$,$$=V.$$;
function heroInto(host,art){var h=$('.q1v-hero',host);if(h)h.innerHTML=V.stage(art&&art.pair?art.pair[1]:art,'scene')}
function shell(b,art){b.innerHTML='<div class="q1v-split"><div class="q1v-hero"></div><div class="q1v-main"></div></div>';heroInto(b,art);return $('.q1v-main',b)}
function shuffle(a){a=a.slice();for(var i=a.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1)),t=a[i];a[i]=a[j];a[j]=t}return a}
function sp(t){try{window.L1SPEAK.speak(t,'en-US')}catch(e){}}
D.bridge=function(p,b,art,A){var ws=p.words||[],m=shell(b,art),sel=-1,done=0;
  var pt=shuffle(ws.map(function(w,i){return i})),en=shuffle(ws.map(function(w,i){return i}));
  m.innerHTML='<div class="q1-card q1v-bridge"><span class="q1-eyebrow">Ponte · como dizemos isso?</span><p class="q1v-bhint">Estas palavras vão aparecer na aula. Ligue o que você diz em <b>português</b> ao que se diz em <b>inglês</b>.</p><div class="q1v-bcols"><div class="q1v-bcol">'+pt.map(function(i){return '<button type="button" class="q1v-bc pt" data-i="'+i+'"><span class="q1v-be">'+H(ws[i].e)+'</span><span>'+H(ws[i].pt)+'</span></button>'}).join('')+'</div><div class="q1v-bcol">'+en.map(function(i){return '<button type="button" class="q1v-bc en" data-i="'+i+'"><span>'+H(ws[i].w)+'</span><small>🔊</small></button>'}).join('')+'</div></div><div class="q1v-bnote" aria-live="polite">Toque numa palavra em português e depois na correspondente em inglês.</div></div>';
  var note=$('.q1v-bnote',m);
  $$(m,'.q1v-bc.pt').forEach(function(x){x.onclick=function(){if(x.classList.contains('ok'))return;$$(m,'.q1v-bc.pt').forEach(function(y){y.classList.remove('sel')});x.classList.add('sel');sel=+x.dataset.i}});
  $$(m,'.q1v-bc.en').forEach(function(x){x.onclick=function(e){var i=+x.dataset.i;if(x.classList.contains('ok'))return;sp(ws[i].w);
    if(sel<0){note.textContent='Primeiro escolha uma palavra em português.';return}
    if(sel===i){var ptb=$('.q1v-bc.pt[data-i="'+i+'"]',m);ptb.classList.remove('sel');ptb.classList.add('ok');x.classList.add('ok');sel=-1;done++;
      note.innerHTML='✅ <b>'+H(ws[i].pt)+'</b> = <b>'+H(ws[i].w)+'</b>'+(ws[i].ex?' · “'+H(ws[i].ex)+'”':'');try{A.gain(4,true,e)}catch(z){}
      if(done>=ws.length){try{A.mark()}catch(z){}note.innerHTML='🎉 Pronto! Agora estas palavras já são suas. Vamos vê-las em ação.'}}
    else{x.classList.add('no');setTimeout(function(){x.classList.remove('no')},450);note.textContent='Quase! Tente outra combinação.';try{A.gain(0,false,e)}catch(z){}}}})};
D.bridge2=function(p,b,art,A){var its=p.items||[],m=shell(b,art),seen=0;
  m.innerHTML='<div class="q1-card q1v-bridge2"><span class="q1-eyebrow">Ponte · português ↔ inglês</span><p class="q1v-bhint">Quando traduzimos palavra por palavra, o inglês sai “torto”. Toque em cada cartão para ver como se diz de verdade.</p>'+its.map(function(it,i){return '<div class="q1v-flip" data-i="'+i+'" tabindex="0" role="button"><div class="q1v-fl no"><small>Muita gente diz ✗</small><b>'+H(it.wrong)+'</b></div><div class="q1v-fl yes"><small>Em inglês se diz ✓</small><b>'+H(it.fix)+'</b><em>'+H(it.why)+'</em></div></div>'}).join('')+'</div>';
  $$(m,'.q1v-flip').forEach(function(x){function go(){if(!x.classList.contains('on')){x.classList.add('on');seen++;var it=its[+x.dataset.i];sp(it.fix);try{A.gain(3,true)}catch(z){}if(seen>=its.length){try{A.mark()}catch(z){}}}}
    x.onclick=go;x.onkeydown=function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();go()}}})};
})();
