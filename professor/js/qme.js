/* Quest · quadros "Sobre você" (início e fim), "Cena da obra" e fundo pintado em tom médio. */
(function(){'use strict';
var previous=window.RL_REGISTER;
window.RL_REGISTER=function(R,A){if(previous)previous(R,A);var orig=R.q1;if(!orig)return;
 var H=function(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})};
 var $=function(s,r){return(r||document).querySelector(s)},$$=function(s,r){return[].slice.call((r||document).querySelectorAll(s))};
 var LSg=function(k){try{return JSON.parse(localStorage.getItem(k)||'{}')||{}}catch(e){return{}}},LSs=function(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}};
 var N=function(){try{return A.lesson().n}catch(e){return 0}};
 function paint(){var st=$('#stage'),L=A.lesson&&A.lesson();if(!st||!L||!L.paint)return;var d=$('.qp-bg',st);var u='../img/scenes/'+L.paint.name+'.webp';
  if(!d){d=document.createElement('div');d.className='qp-bg';d.innerHTML='<img alt="" decoding="async">';st.insertBefore(d,st.firstChild)}
  var im=$('img',d);if(im.getAttribute('src')!==u)im.src=u;im.style.transform=L.paint.flip?'scaleX(-1)':'';im.style.filter='hue-rotate('+(L.paint.hue||0)+'deg) saturate(1.45) contrast(1.05) brightness(1.1)'}
 function build(frame,vals){return String(frame||'').replace(/\{(\w+)\}/g,function(m,k){return vals[k]||'…'})}
 function slotHtml(fid,s){var o=s.opts.map(function(x){return'<option>'+H(x)+'</option>'}).join('');return'<label class="qm-slot"><span>'+H(s.key)+'</span><select data-f="'+fid+'" data-k="'+H(s.key)+'">'+o+'<option value="__o">Outro…</option></select><input data-f="'+fid+'" data-o="'+H(s.key)+'" type="text" maxlength="24" placeholder="escreva" hidden></label>'}
 function wire(root,frames,onChange){function vals(fid){var v={};$$('select[data-f="'+fid+'"]',root).forEach(function(s){var k=s.dataset.k;if(s.value==='__o'){var i=$('input[data-f="'+fid+'"][data-o="'+k+'"]',root);i.hidden=false;v[k]=i.value.trim()}else{var i2=$('input[data-f="'+fid+'"][data-o="'+k+'"]',root);if(i2)i2.hidden=true;v[k]=s.value}});return v}
  function upd(){frames.forEach(function(f,i){var t=build(f.frame,vals(i)),el=$('[data-line="'+i+'"]',root);if(el)el.textContent=t});onChange&&onChange(frames.map(function(f,i){return build(f.frame,vals(i))}))}
  $$('select,input[data-o]',root).forEach(function(x){x.addEventListener('input',upd);x.addEventListener('change',upd)});upd()}
 function meStart(p,b){var key='pgx-me-'+N()+'-start',saved=LSg(key),frames=[{frame:p.frame,slots:p.slots}];
  b.innerHTML='<div class="qm"><div class="qm-card"><span class="qm-eye">Antes de começar · fale de você</span><h3>Diga algo sobre você, agora</h3><p class="qm-model">Modelo: <b>'+H(p.model)+'</b> <button type="button" class="qm-say" data-t="'+H(p.model)+'" aria-label="Ouvir">🔊</button></p>'+
   (p.slots.length?'<div class="qm-slots">'+p.slots.map(function(s){return slotHtml(0,s)}).join('')+'</div><div class="qm-line" aria-live="polite"><small>Sua frase</small><b data-line="0"></b></div><div class="qm-acts"><button type="button" class="qm-btn main" id="qmHear">🔊 Ouvir minha frase</button><button type="button" class="qm-btn" id="qmDone">✔ Já falei em voz alta</button></div>':'<p>Diga o modelo em voz alta.</p><div class="qm-acts"><button type="button" class="qm-btn" id="qmDone">✔ Já falei em voz alta</button></div>')+'<p class="qm-fine">Sem certo ou errado: é a sua primeira vitória da aula.</p></div></div>';
  var cur=[];wire(b,frames,function(a){cur=a});
  $$('.qm-say',b).forEach(function(x){x.onclick=function(){A.say(x.dataset.t)}});
  var h=$('#qmHear',b);if(h)h.onclick=function(){A.say(cur[0])};
  $('#qmDone',b).onclick=function(e){var s=LSg(key);if(!s.ok){LSs(key,{ok:1,line:cur[0]||p.model});A.gain(10,true,e)}this.textContent='✔ Muito bem!';this.disabled=true}}
 function meEnd(p,b){var key='pgx-me-'+N()+'-end',fr=p.frames||[];
  b.innerHTML='<div class="qm"><div class="qm-card"><span class="qm-eye">Para fechar · monte a sua versão</span><h3>Agora sobre você, com o que aprendeu</h3>'+
   fr.map(function(f,i){return'<div class="qm-row"><div class="qm-slots">'+f.slots.map(function(s){return slotHtml(i,s)}).join('')+'</div><div class="qm-line"><small>Frase '+(i+1)+'</small><b data-line="'+i+'"></b><button type="button" class="qm-say2" data-i="'+i+'" aria-label="Ouvir">🔊</button></div></div>'}).join('')+
   '<div class="qm-acts"><button type="button" class="qm-btn main" id="qmAll">🔊 Ouvir tudo</button><button type="button" class="qm-btn" id="qmCopy">📋 Copiar</button><button type="button" class="qm-btn" id="qmSave">⭐ Guardar</button></div><p class="qm-fine">Mostre para o professor ou para um colega e converse sobre as suas frases.</p></div></div>';
  var cur=[];wire(b,fr,function(a){cur=a});
  $$('.qm-say2',b).forEach(function(x){x.onclick=function(){A.say(cur[+x.dataset.i])}});
  $('#qmAll',b).onclick=function(){A.say(cur.join(' '))};
  $('#qmCopy',b).onclick=function(){var t=cur.join('\n');try{navigator.clipboard.writeText(t);this.textContent='Copiado ✓'}catch(e){}};
  $('#qmSave',b).onclick=function(e){if(!LSg(key).ok)A.gain(15,true,e);LSs(key,{ok:1,lines:cur});this.textContent='⭐ Guardado';this.disabled=true}}
 function story(p,b){var L=A.lesson&&A.lesson(),pi=(L&&L.paint)?'../img/scenes/'+L.paint.name+'.webp':'';
  var lines=(p.lines||[]).map(function(l,i){var f='';try{f=A.face(l.name)}catch(e){}return'<div class="qs-b'+(i%2?' r':'')+'"><span class="qs-f">'+f+'</span><div><b>'+H(l.name)+'</b><p>'+H(l.en)+' <button type="button" class="qm-say" data-t="'+H(l.en)+'" aria-label="Ouvir">🔊</button></p><small>'+H(l.pt)+'</small></div></div>'}).join('');
  b.innerHTML='<div class="qs"><div class="qs-scene">'+(window.L1HERO&&p.art?window.L1HERO(p.art,'cover').outerHTML:'')+'<div class="qs-cap"><small>Cena da obra · '+H(p.work.year)+'</small><b>'+H(p.work.title)+'</b></div></div><div class="qs-side"><p class="qs-narr">'+H(p.narr)+'</p><div class="qs-lines">'+lines+'</div><button type="button" class="qm-btn main" id="qsAll">🔊 Ouvir a cena</button></div></div>';
  $$('.qm-say',b).forEach(function(x){x.onclick=function(){A.say(x.dataset.t)}});
  $('#qsAll',b).onclick=function(){A.say((p.lines||[]).map(function(l){return l.en}).join(' '))}}
 R.q1=function(p,b){
  if(p.kind==='me'||p.kind==='story'){try{b.scrollTop=0}catch(z){}b.className='pb q1-body q1v qm-body';if(p.kind==='story')story(p,b);else if(p.mode==='end')meEnd(p,b);else meStart(p,b);try{A.mark()}catch(e){}paint();return}
  orig(p,b);paint()}};
})();
