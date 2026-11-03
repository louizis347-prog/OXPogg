/* Aula Quest 1: passos legíveis sem rolagem, com conteúdo igual nos modos solo e grupo. */
(function(){
'use strict';
var previous=window.RL_REGISTER;
window.RL_REGISTER=function(R,A){
 if(previous)previous(R,A);
 A.SEC.q1=['open','Aula em ação'];
 var H=A.esc, $=function(selector,root){return root.querySelector(selector)},
  all=function(root,selector){return Array.from(root.querySelectorAll(selector))};
 function rich(s){return H(s||'').replace(/\*\*(.+?)\*\*/g,'<strong>$1</strong>')}
 function say(root){all(root,'[data-say1]').forEach(function(button){button.onclick=function(){A.say(button.dataset.say1)}})}
 function speak(text){return '<button type="button" class="q1-audio" data-say1="'+H(text)+'" aria-label="Ouvir em inglês">'+
  '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 9v6h4l5 4V5L7 9H3zM16 9a5 5 0 010 6m2-9a9 9 0 010 12"/></svg></button>'}
 function illustration(){return '<div class="q1-art" aria-hidden="true"><svg viewBox="0 0 800 450" role="img" aria-label="Cafeteria em Chicago" xmlns="http://www.w3.org/2000/svg">'+
  '<defs><linearGradient id="q1win" x2="0" y2="1"><stop stop-color="#9ccee0"/><stop offset="1" stop-color="#e4eff0"/></linearGradient><linearGradient id="q1wall" x2="1" y2="1"><stop stop-color="#f6eee4"/><stop offset="1" stop-color="#e9dbc9"/></linearGradient><pattern id="q1grain" width="8" height="8" patternUnits="userSpaceOnUse"><circle cx="1" cy="2" r=".5" fill="#986f5e" opacity=".22"/></pattern></defs>'+
  '<rect width="800" height="450" fill="url(#q1wall)"/><rect width="800" height="450" fill="url(#q1grain)" opacity=".5"/><path d="M0 328H800v122H0z" fill="#c6a78a"/><path d="M0 331H800" stroke="#2b1d3a" stroke-width="6"/>'+
  '<rect x="24" y="30" width="270" height="225" rx="8" fill="#f5faf5" stroke="#2b1d3a" stroke-width="7"/><rect x="36" y="42" width="246" height="202" fill="url(#q1win)"/>'+
  '<path d="M43 230h233M86 40v206M175 40v206" stroke="#2b1d3a" stroke-width="6"/><path d="M42 210l22-36 18 16 29-51 26 28 22-41 17 14 31-45 24 31 29-25" fill="none" stroke="#698e9d" stroke-width="8"/>'+
  '<path d="M65 229v-68h22v68m32 0v-94h28v94m49 0v-50h25v50m19 0v-81h24v81" fill="#70859a" opacity=".7"/>'+
  '<rect x="330" y="40" width="430" height="120" rx="10" fill="#223b3f" stroke="#2b1d3a" stroke-width="7"/><text x="360" y="80" fill="#f8e9c8" font-size="29" font-family="Georgia,serif">CAFÉ · MENU</text><path d="M360 94h360" stroke="#b5ad96" stroke-width="3"/><text x="360" y="122" fill="#f3e5d1" font-size="21" font-family="Arial,sans-serif">Coffee  $3   ·   Tea  $2.50</text><text x="360" y="145" fill="#f3e5d1" font-size="18" font-family="Arial,sans-serif">Oat milk  +$0.75</text>'+
  '<path d="M311 305h489v145H311z" fill="#a76c58" stroke="#2b1d3a" stroke-width="7"/><path d="M312 305h487v26H312z" fill="#d6aa82" stroke="#2b1d3a" stroke-width="6"/>'+
  '<path d="M535 306v-86q0-36 42-36t42 36v86" fill="#2e6b6a" stroke="#2b1d3a" stroke-width="6"/><circle cx="579" cy="179" r="37" fill="#b77a59" stroke="#2b1d3a" stroke-width="6"/><path d="M543 176q8-53 48-37 26 8 22 33-24-20-70 4" fill="#30282a" stroke="#2b1d3a" stroke-width="5"/><path d="M563 188h4m27 0h4" stroke="#2b1d3a" stroke-width="5" stroke-linecap="round"/><path d="M571 204q12 9 22 0" fill="none" stroke="#2b1d3a" stroke-width="4"/>'+
  '<path d="M118 342v-101q0-42 48-42t48 42v101" fill="#d46d60" stroke="#2b1d3a" stroke-width="7"/><circle cx="167" cy="182" r="42" fill="#dca37d" stroke="#2b1d3a" stroke-width="6"/><path d="M125 174q-9-52 39-51 53-1 48 49-27-21-49-14-22 8-38 16" fill="#30282a" stroke="#2b1d3a" stroke-width="6"/><path d="M152 189h3m26 0h3" stroke="#2b1d3a" stroke-width="5" stroke-linecap="round"/><path d="M158 207q11 7 20 0" fill="none" stroke="#2b1d3a" stroke-width="4"/>'+
  '<path d="M211 263q44 3 75 35" fill="none" stroke="#dca37d" stroke-width="17" stroke-linecap="round"/><path d="M450 304q-65-36-126-13" fill="none" stroke="#b77a59" stroke-width="16" stroke-linecap="round"/>'+
  '<path d="M288 261h41l-5 47h-31z" fill="#faf8ed" stroke="#2b1d3a" stroke-width="5"/><path d="M294 259h29" stroke="#cf8261" stroke-width="7"/><path d="M300 278h18" stroke="#a67260" stroke-width="3"/><text x="470" y="390" fill="#f9eee0" font-size="23" font-family="Arial,sans-serif">ORDER HERE  →</text>'+
  '<path d="M0 0h800v450H0z" fill="none" stroke="#2b1d3a" stroke-width="12"/></svg></div>'}
 function intro(text){return '<p class="q1-intro">'+H(text||'')+'</p>'}
 function card(inner,extra){return '<div class="q1-card '+(extra||'')+'">'+inner+'</div>'}
 function vocabIcon(word){var shapes={
  coffee:'<path d="M10 24h23l-3 18H13z" fill="#b7775e"/><path d="M10 24h23"/><path d="M18 18c-5-6 5-7 0-13m9 13c-5-6 5-7 0-13"/>',
  tea:'<path d="M9 22h24l-2 18H11z" fill="#eacb89"/><path d="M33 27c12-2 11 9-1 9"/><path d="M17 14q7-9 15-4-5 8-15 4" fill="#8cb69b"/>',
  milk:'<path d="M12 15h23v29H12z" fill="#edf5f3"/><path d="M12 15l5-8h13l5 8M17 7v8m13-8v8"/><path d="M17 25h13l-4 12h-5z" fill="#8bc4ce"/>',
  cup:'<path d="M13 12h22l-3 30H16z" fill="#f3e9dc"/><path d="M11 12h26M16 26h16"/><path d="M22 32q3-4 5 0-2 4-5 0" fill="#c78263"/>',
  counter:'<path d="M5 25h38v6H5zM9 31v12m30-12v12" fill="#bb8d71"/><path d="M18 13h17v12H18z" fill="#bddddd"/><path d="M23 18h7"/>',
  tray:'<path d="M6 34h36l-4 6H10z" fill="#c59b73"/><path d="M16 31q0-13 8-13t8 13z" fill="#eed8a5"/><path d="M13 32h22"/>'};
  return '<svg viewBox="0 0 48 48" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"><g stroke="#2b1d3a" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">'+(shapes[word]||shapes.cup)+'</g></svg>'}
 function quiz(root,items){var index=0,correct=0;
  function draw(){if(index>=items.length){root.innerHTML=card('<b class="q1-complete">'+correct+' / '+items.length+' · concluído</b><p>Explique uma resposta com suas próprias palavras.</p>');A.mark();return}
   var q=items[index];root.innerHTML='<div class="q1-progress">Pergunta '+(index+1)+' de '+items.length+'</div>'+card('<h3>'+H(q.q||q.s)+'</h3><div class="q1-options">'+
    q.opts.map(function(o,i){return '<button type="button" data-answer="'+i+'">'+H(o)+'</button>'}).join('')+'</div><p class="q1-feedback" role="status"></p><button type="button" class="q1-next-item" hidden>Próxima pergunta →</button>');
   all(root,'[data-answer]').forEach(function(btn){btn.onclick=function(e){var ok=+btn.dataset.answer===q.ans;if(ok)correct++;A.gain(ok?8:0,ok,e);
    all(root,'[data-answer]').forEach(function(x){x.disabled=true;x.classList.toggle('right',+x.dataset.answer===q.ans)});
    btn.classList.add(ok?'right':'wrong');$('.q1-feedback',root).textContent=(ok?'Correto. ':'Tente explicar a forma correta. ')+(q.why||'');
    $('.q1-next-item',root).hidden=false}});
   $('.q1-next-item',root).onclick=function(){index++;draw()}
  }draw()}
 function status(root,text){var s=$('.q1-feedback',root);if(s)s.textContent=text}
 R.q1=function(p,b){var kind=p.kind,bg=A.lesson().visual||'cafe2';b.className='pb q1-body';
  if(kind==='cover'){
   b.innerHTML='<div class="q1-cover"><div>'+intro(p.kicker||'A1 · Aula 1 · Particular ou grupo')+'<h1>'+H(p.heading||'A coffee to go in Chicago')+'</h1>'+card('<b>Missão</b><p>'+H(p.goal)+'</p>','q1-mission')+
    '<div class="q1-lines">'+p.can.map(function(x){return '<div>'+speak(x)+'<span>'+H(x)+'</span></div>'}).join('')+'</div><p class="q1-note">'+H(p.note)+'</p></div>'+illustration(bg)+'</div>'}
  else if(kind==='work'){
   b.innerHTML='<div class="q1-two">'+card('<span class="q1-eyebrow">Obra cultural · '+H(p.work.year)+'</span><h3>'+H(p.work.title)+'</h3><p>'+H(p.work.note)+'</p><div class="q1-prompt">'+H(p.question)+'</div>')+
    illustration(bg)+'</div>'}
  else if(kind==='facts'){
   b.innerHTML='<div class="q1-facts">'+p.facts.map(function(f){return card('<b>'+H(f.big)+'</b><strong>'+H(f.label)+'</strong><span>'+H(f.sub)+'</span>')}).join('')+'</div>'+
    (p.compare?'<details class="q1-details"><summary>Compare Brasil e Estados Unidos</summary><p><b>Brasil:</b> '+H(p.compare.br)+'</p><p><b>EUA:</b> '+H(p.compare.us)+'</p><p>'+H(p.compare.tip)+'</p></details>':'')}
  else if(kind==='compare'){
   b.innerHTML='<div class="q1-facts">'+card('<span class="q1-eyebrow">Brasil</span><p>'+H(p.compare.br)+'</p>')+
    card('<span class="q1-eyebrow">Estados Unidos</span><p>'+H(p.compare.us)+'</p>')+
    card('<span class="q1-eyebrow">Ponte de uso</span><p>'+H(p.compare.tip)+'</p>')+'</div>'+card('<div class="q1-prompt">'+H(p.compare.ask)+'</div>')}
  else if(kind==='artifact'){
   var w=p.artifact;b.innerHTML='<div class="q1-two">'+card('<span class="q1-eyebrow">Texto do cotidiano · '+H(w.kind)+'</span><div class="q1-sign">'+w.lines.map(function(l){return '<div>'+rich(l)+'</div>'}).join('')+'</div>')+
    card('<h3>'+H(w.decode.q)+'</h3><div class="q1-options">'+w.decode.opts.map(function(o,i){return '<button type="button" data-art-answer="'+i+'">'+H(o)+'</button>'}).join('')+'</div><p class="q1-feedback" role="status"></p>')+'</div>';
   all(b,'[data-art-answer]').forEach(function(x){x.onclick=function(e){var ok=+x.dataset.artAnswer===w.decode.ans;A.gain(ok?8:0,ok,e);all(b,'[data-art-answer]').forEach(function(v){v.disabled=true;v.classList.toggle('right',+v.dataset.artAnswer===w.decode.ans)});status(b,w.decode.why)}})}
  else if(kind==='quiz'){
   b.innerHTML=intro(p.instruction)+'<div class="q1-quiz"></div>';
   var items=p.items.map(function(it){return it.opts?it:{q:it.s,opts:['Fato','Mito'],ans:it.ans?0:1,why:it.why}});quiz($('.q1-quiz',b),items)}
  else if(kind==='reading'){
   var words=(p.paragraphs||[]).join(' ').replace(/\*\*/g,'').split(/\s+/).length;
   var gloss=p.glossary.slice((p.part-1)*3,p.part*3).map(function(g){return '<button type="button" data-word="'+H(g.w)+'"><b>'+H(g.w)+'</b><span>'+H(g.pt)+'</span></button>'}).join('');
   b.innerHTML='<div class="q1-reading">'+card('<span class="q1-eyebrow">História · Parte '+p.part+' de 3 · '+words+' palavras</span>'+p.paragraphs.map(function(t){return '<p>'+rich(t)+'</p>'}).join('')+
    '<div class="q1-actions"><button type="button" id="q1-hear">Ouvir este trecho</button><button type="button" id="q1-slow">Ouvir devagar</button></div><details class="q1-gloss-mobile"><summary>Palavras deste trecho</summary><div class="q1-gloss">'+gloss+'</div></details>','q1-text')+
    card('<b>Encontre na história</b><p>'+H(p.prompt)+'</p><div class="q1-gloss">'+gloss+'</div>','q1-reading-side')+'</div>';
   $('#q1-hear',b).onclick=function(){A.say(p.paragraphs.join(' ').replace(/\*\*/g,''))};$('#q1-slow',b).onclick=function(){A.sayP(p.paragraphs.join(' ').replace(/\*\*/g,''),.72)};
   all(b,'[data-word]').forEach(function(x){x.onclick=function(){A.say(x.dataset.word)}})}
  else if(kind==='dialog'){
   b.innerHTML=intro(p.instruction)+'<div class="q1-dialog">'+p.lines.map(function(line){var who=line[0];return card('<b>'+H(who)+'</b><span>'+H(line[1])+'</span>'+speak(line[1])+'<small>'+H(line[2])+'</small>',who==='Evan'?'evan':'ana')}).join('')+'</div>'}
  else if(kind==='choice'){
   var t=p.turn;var face=A.face(p.npcface||p.npc||'Evan');b.innerHTML='<div class="q1-choice"><div class="q1-person">'+face+'</div>'+card('<span class="q1-eyebrow">'+H(p.npc||'Evan')+' · fala '+p.position+' de '+(p.total||6)+'</span><h3>'+H(t.npc)+'</h3><p>'+H(t.pt)+'</p>'+speak(t.npc))+'</div><div class="q1-options">'+t.opts.map(function(o,i){return '<button type="button" data-choice="'+i+'"><strong>'+H(o.en)+'</strong><span>'+H(o.pt)+'</span></button>'}).join('')+'</div><p class="q1-feedback" role="status"></p>';
   all(b,'[data-choice]').forEach(function(x){x.onclick=function(e){var o=t.opts[+x.dataset.choice];A.gain(o.ok?10:0,!!o.ok,e);all(b,'[data-choice]').forEach(function(v){v.disabled=true;v.classList.toggle('right',t.opts[+v.dataset.choice].ok)});x.classList.add(o.ok?'right':'wrong');status(b,o.fb+' '+(o.ok?p.outcome:''));if(o.ok)A.say(o.en)}})}
  else if(kind==='vocab'){
   b.innerHTML=intro(p.prompt)+'<div class="q1-vocab">'+p.words.map(function(item){return card('<div class="q1-vocab-head"><span class="q1-vocab-icon">'+vocabIcon(item[0])+'</span><div><strong>'+H(item[0])+'</strong><span>'+H(item[1])+'</span></div>'+speak(item[0])+'</div><button type="button" class="q1-variant" data-say1="'+H(item[2])+'">'+H(item[2])+'</button><button type="button" class="q1-variant" data-say1="'+H(item[3])+'">'+H(item[3])+'</button>')}).join('')+'</div>'}
  else if(kind==='pattern'){
   b.innerHTML='<div class="q1-two">'+card('<span class="q1-eyebrow">Molde que muda</span><div class="q1-result" aria-live="polite"></div><div class="q1-slots">'+p.slots.map(function(s){return '<label>'+H(s.key)+'<select data-slot="'+H(s.key)+'">'+s.opts.map(function(o){return '<option>'+H(o)+'</option>'}).join('')+'</select></label>'}).join('')+'</div><button type="button" class="q1-main" id="q1-say">Ouvir minha frase</button>')+
    card('<b>Compare e produza</b><p>'+H(p.model)+'</p><p>'+H(p.note)+'</p><div class="q1-prompt">Troque duas opções. Depois faça a pergunta ou responda sem ler.</div>')+'</div>';
   function update(){var phrase=p.frame;all(b,'[data-slot]').forEach(function(s){phrase=phrase.replace('{'+s.dataset.slot+'}',s.value)});$('.q1-result',b).textContent=phrase;return phrase}
   all(b,'select').forEach(function(s){s.onchange=update});$('#q1-say',b).onclick=function(){A.say(update())};update()}
  else if(kind==='sound'){
   b.innerHTML=intro(p.prompt)+'<div class="q1-facts">'+p.pairs.map(function(pair){return card('<span class="q1-eyebrow">Som: '+H(pair[1])+'</span><h3>'+H(pair[0])+' '+speak(pair[0])+'</h3><p>'+H(pair[2])+'</p>')}).join('')+'</div>'}
  else if(kind==='role'){
   var group=A.mode()==='group';b.innerHTML=card('<span class="q1-eyebrow">'+'Missão ao vivo'+'</span><h3>'+H(p.solo)+'</h3><div class="q1-roles">'+p.prompts.map(function(x){return '<button type="button" data-say1="'+H(x)+'">'+H(x)+'</button>'}).join('')+'</div>')+
    card('<b>Mude a condição a cada rodada</b><ol>'+p.change.map(function(x){return '<li>'+H(x)+'</li>'}).join('')+'</ol><p class="q1-note">'+(group?'Observador: anote uma fala clara e uma reformulação.':'Professor: dê uma pista só quando necessário; peça uma segunda tentativa.')+'</p>')}
  else if(kind==='writing'){
   b.innerHTML=card('<span class="q1-eyebrow">Agora escreva</span><p>'+H(p.task)+'</p><textarea aria-label="Sua mensagem em inglês" placeholder="'+H(p.placeholder||'Hi! Could I get…?')+'"></textarea><div class="q1-check">'+p.checks.map(function(c){return '<label><input type="checkbox">'+H(c)+'</label>'}).join('')+'</div>')}
  else if(kind==='exit'){
   b.innerHTML=card('<b>Sem consultar, diga em voz alta</b><ol>'+p.prompts.map(function(x){return '<li>'+H(x)+'</li>'}).join('')+'</ol><p class="q1-note">Professor: registre um acerto e uma próxima meta.</p>')+
    card('<b>Mochila de revisão</b><ul>'+p.spaced.map(function(x){return '<li>'+H(x)+'</li>'}).join('')+'</ul>')}
  else if(kind==='finish'){
   b.innerHTML='<div class="q1-two">'+card('<span class="q1-eyebrow">Missão cumprida</span><h3>'+H(p.badge.name)+'</h3><p>'+H(p.badge.desc)+'</p><p>'+H(p.homework)+'</p><div class="q1-prompt">'+H(p.next)+'</div>')+illustration(bg)+'</div>'}
  else b.innerHTML=card('Etapa indisponível.');
  say(b);if(kind==='writing')all(b,'[data-var]').forEach(function(x){x.onclick=function(){var v=x.dataset.var.split(' / ');$('textarea',b).value='Hi! Could I get a '+v[0]+' to go at '+v[1]+'? Do you have oat milk? Thanks, Ana.'}});
  A.mark()
 }
};
})();
