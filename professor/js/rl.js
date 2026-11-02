/* Aulas Real-Life (aula3.html): tipos de tela "rl_*", linha do tempo de 60 min e roteiro do professor.
   O deck2.js chama window.RL_REGISTER(R, API) uma vez e window.RL_ONDRAW(p, i, pages) a cada tela. */
(function(){
'use strict';
var A=null,T0=Date.now();
var H=function(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})};
var hb=function(t){return H(t).replace(/\*\*(.+?)\*\*/g,'<b>$1</b>')};
var norm=function(s){return String(s||'').toLowerCase().replace(/[“”]/g,'"').replace(/[’‘]/g,"'").replace(/[^a-z0-9' ]/g,' ').replace(/\s+/g,' ').trim()};
var $q=function(r,s){return r.querySelector(s)},$a=function(r,s){return Array.prototype.slice.call(r.querySelectorAll(s))};
var S=function(sfx){return A.key()+'-rl-'+sfx};
var isSolo=function(){return A.mode()==='solo'};
/* ---------- fala (TTS) com vozes diferentes por personagem ---------- */
var TOK=0,VOICES=[];
function loadVoices(){try{VOICES=(speechSynthesis.getVoices()||[]).filter(function(v){return /^en/i.test(v.lang)})}catch(e){}}
try{loadVoices();speechSynthesis.onvoiceschanged=loadVoices}catch(e){}
function speakLine(text,who,rate){return new Promise(function(res){try{var u=new SpeechSynthesisUtterance(String(text).replace(/\*\*/g,''));u.lang='en-US';u.rate=rate||.92;u.pitch=who===1?.82:1.12;
  if(VOICES.length>1){var us=VOICES.filter(function(v){return /US/i.test(v.lang)});var pool=us.length>1?us:VOICES;u.voice=pool[who===1?1%pool.length:0]}
  u.onend=res;u.onerror=res;speechSynthesis.speak(u);setTimeout(res,12000)}catch(e){res()}})}
function stopAll(){TOK++;try{speechSynthesis.cancel()}catch(e){}}
async function playLines(lines,spk,rate,onLine){var my=++TOK;try{speechSynthesis.cancel()}catch(e){}
  for(var i=0;i<lines.length;i++){if(my!==TOK)return false;if(onLine)onLine(i);await speakLine(lines[i].en,spk.indexOf(lines[i].who)<=0?0:1,rate)}
  if(onLine)onLine(-1);return my===TOK}
function dlg(){return (A.lesson()||{}).dialog||{speakers:{},lines:[]}}
function faceOf(who){var d=dlg(),sp=(d.speakers||{})[who];var nm=sp&&sp.name||who;try{return A.V('face:'+nm)}catch(e){return ''}}
var uid=function(){return 'x'+Math.random().toString(36).slice(2,7)};
/* ---------- roteiro padrão por tipo de tela (usado quando a aula não traz p.teach) ---------- */
var DEF={
 rl_open:{solo:['Leia o objetivo comunicativo em voz alta e peça que o estudante diga, com as próprias palavras, o que acha que vai fazer hoje.','Mostre a cena e faça a pergunta "Think about it" antes de abrir qualquer regra.'],group:['Peça que cada estudante diga uma palavra que associa à situação.','Mostre os critérios de sucesso: o grupo precisa realizar a missão final, não só falar certo.']},
 rl_warm:{solo:['Conversa espontânea: não corrija ainda; anote lacunas para usar depois.','Retome 2 itens da aula anterior em contexto novo.'],group:['Rodada rápida: cada estudante responde a uma pergunta diferente.','Use "Who goes next?" para sortear; peça uma pergunta de volta para o colega.']},
 rl_culture:{solo:['Mostre os cartões e peça hipóteses antes de explicar.','Discuta a comparação com o Brasil e peça um exemplo pessoal.'],group:['Discussão coletiva: cada estudante escolhe um cartão e explica por quê.','Peça comparações entre colegas ("Do you agree?").']},
 rl_listen:{solo:['1ª escuta sem texto: só a ideia principal.','2ª escuta: 3 informações específicas. Só depois mostre o texto.'],group:['Escuta coletiva; respostas em duplas antes de revelar.','Compare as respostas entre duplas e só então mostre o texto.']},
 rl_dialog:{solo:['Peça ao estudante para ler o papel do cliente; você lê o do atendente.','Peça que reconte a conversa no nível que conseguir.'],group:['Leitura em duplas e troca de papéis.','Reconto em cadeia: cada estudante diz uma frase.']},
 rl_chunks:{solo:['Escolha 3–5 expressões prioritárias (estrelas) para usar repetidamente; as outras são repertório de compreensão.','Peça que o estudante descubra quando cada expressão é usada.'],group:['Cada estudante escolhe a expressão que mais usaria e explica quando.','Compare equivalentes formais e informais.']},
 rl_patterns:{solo:['Mostre o padrão dentro do diálogo, não como regra isolada.','Use a troca de palavras: o estudante diz a frase com cada combinação.'],group:['Troca de palavras em cadeia: cada estudante muda uma peça da frase.','Em pares: um escolhe as peças, o outro fala a frase.']},
 rl_pron:{solo:['Trabalhe UM fenômeno só. Modele, peça repetição de ritmo e depois uso livre.','Não busque eliminar sotaque: busque compreensão e naturalidade.'],group:['Coro, depois duplas; circule ouvindo.','Cada estudante cria uma pergunta própria usando a ligação.']},
 rl_challenge:{solo:['Do controlado ao guiado: peça justificativa nas respostas.','Se acertar fácil, peça a versão mais educada ou mais informal.'],group:['Resolvam em duplas e comparem antes de revelar.','Equipes: ponto por resposta justificada.']},
 rl_lab:{solo:['—'],group:['Rodízio de pares: troque parceiros a cada rodada para repetir a função com informações novas.','Information gap: ninguém olha o cartão do outro.']},
 rl_role:{solo:['Você assume o atendente e introduz uma complicação inesperada.','Repita 3 vezes com cada vez menos apoio.'],group:['—']},
 rl_mission:{solo:['—'],group:['Cada grupo recebe papel, restrição e missão. O objetivo é resolver, não só falar certo.','Observe e anote 2–3 correções prioritárias para a devolutiva.']},
 rl_write:{solo:['Peça a mensagem curta; corrija só 2–3 pontos prioritários e mostre uma forma mais natural.'],group:['Produção individual, depois troca de textos entre colegas para comparar e corrigir em duplas.']},
 rl_feedback:{solo:['Preencha a rubrica com o estudante: ele se autoavalia primeiro, depois você.','Termine com os 3 blocos: What you did well · What to improve · Your next challenge.'],group:['Cada estudante recebe um comentário em cada critério.','Peça que cada um escolha o próximo desafio.']},
 rl_exit:{solo:['Sem consultar as anotações: construir uma pergunta, responder a uma situação e usar uma expressão nova.'],group:['Cada estudante faz o exit ticket individualmente; compare com o colega.']},
 rl_levels:{solo:['Mostre onde o estudante está e a próxima etapa.'],group:['Peça que cada um escolha a frase do próprio nível e a do próximo.']}
};
/* ---------- registro dos tipos de tela ---------- */
window.RL_REGISTER=function(R,API){A=API;var SEC=A.SEC,COLS=A.COLS,esc=A.esc,say=A.say,gain=A.gain,mark=A.mark,shuf=A.shuf,LS=A.LS,V=A.V,ex=A.ex;
 SEC.rl_open=['open','Mission & objectives'];SEC.rl_warm=['look','Connection & warm-up'];SEC.rl_culture=['read','Cultural snapshot'];SEC.rl_listen=['listen','Scene & listening'];SEC.rl_dialog=['photo','Dialogue & comprehension'];
 SEC.rl_chunks=['vocab','Useful expressions'];SEC.rl_patterns=['gram','Grammar & patterns'];SEC.rl_pron=['pron','Pronunciation lab'];SEC.rl_challenge=['game','Guided challenges'];SEC.rl_lab=['speak','Communication lab'];
 SEC.rl_role=['speak','Personalized roleplay'];SEC.rl_mission=['speak','Group mission'];SEC.rl_write=['write','Writing'];SEC.rl_feedback=['review','Feedback & review'];SEC.rl_exit=['review','Exit ticket & homework'];SEC.rl_levels=['open','Level up'];
 var lvColor={A1:'#e5484d',A2:'#f08a2b',B1:'#f2b01e',B2:'#2da44e',C1:'#2f6fe0',C2:'#7a3fe0'};
 /* utilitários de UI */
 function sayBtn(t,cls){return '<button class="say '+(cls||'')+'" data-sy="'+H(t)+'" title="Ouvir">🔊</button>'}
 function wireSay(root){$a(root,'[data-sy]').forEach(function(x){x.onclick=function(e){e.stopPropagation();stopAll();say(x.dataset.sy.replace(/\*\*/g,''))}})}
 function saved(key,def){return LS.get(S(key),def)}
 function save(key,v){LS.set(S(key),v)}
 function textArea(key,ph,min){var v=saved(key,'');return '<textarea class="rl-ta" data-k="'+key+'" placeholder="'+H(ph||'')+'" style="min-height:'+(min||110)+'px">'+H(v)+'</textarea>'}
 function wireTA(root){$a(root,'.rl-ta,[data-save]').forEach(function(t){t.oninput=function(){save(t.dataset.k||t.dataset.save,t.value)}})}
 function timer(el,secs,onEnd){var left=secs,iv=null,run=false;function fmt(){var m=Math.floor(left/60),s=left%60;el.textContent=m+':'+String(s).padStart(2,'0');el.classList.toggle('low',left<=15)}
  fmt();return {toggle:function(){if(run){clearInterval(iv);run=false;return false}run=true;iv=setInterval(function(){left--;fmt();if(left<=0){clearInterval(iv);run=false;if(onEnd)onEnd()}},1000);return true},reset:function(s){clearInterval(iv);run=false;left=s||secs;fmt()},stop:function(){clearInterval(iv);run=false}}}

 /* 1 · Mission & objectives */
 R.rl_open=function(p,b){var s=p.situation||{},u=p.unit||{};b.className='pb c';
  var map=(u.map||[]).map(function(n,i){return '<span class="'+(i+1===u.k?'on':'')+'">'+(i+1)+' · '+esc(n)+'</span>'}).join('');
  b.innerHTML='<div class="rl-hero"><div style="display:grid;gap:12px"><div class="rl-kick"><span class="k">Unit '+esc(u.n)+'</span><span class="k o">Lesson '+esc(u.k)+' / '+esc(u.of)+'</span><span class="k o">'+esc(p.level||'')+'</span><span class="k o">60 min</span></div>'+
   '<h1 class="rl-h1">'+esc(p.title)+'</h1>'+(p.pt?'<p class="rl-sub">'+esc(p.pt)+'</p>':'')+
   '<div class="rl-sit"><b>Real-life situation</b>'+esc(s.text||'')+'</div>'+
   '<div class="bx soft"><div class="bxh">Communicative goal</div><div class="bxb"><p style="margin:0 0 6px;font-weight:700">'+esc(p.goal||'')+'</p>'+(p.canDo||[]).map(function(g){return '<div class="rl-goal"><i>✓</i><span>'+esc(g)+'</span></div>'}).join('')+'</div></div>'+
   (p.success&&p.success.length?'<div class="rl-crit">'+p.success.map(function(g,i){return '<div><i>'+(i+1)+'</i><span>'+esc(g)+'</span></div>'}).join('')+'</div>':'')+
   (p.think?'<div class="rl-tip">💭 <span><b>Think about it:</b> '+esc(p.think)+'</span></div>':'')+(map?'<div class="rl-umap">'+map+'</div>':'')+'</div>'+
   '<div class="rl-sc"><div class="frame">'+A.scene(s.scene||'park',s.tod||'day',s.cast||[],'cover')+'</div></div></div>';mark()};

 /* 2 · Connection & warm-up */
 R.rl_warm=function(p,b){var N=saved('who-n',4);
  var qs=(p.qs||[]).map(function(q,i){return '<div class="rl-qi"><span class="n">'+(i+1)+'</span><div style="flex:1">'+esc(q.q)+' '+sayBtn(q.q)+'<small class="ptx" style="display:none">'+esc(q.pt||'')+'</small>'+((q.sup&&q.sup.length)?'<div class="chips" style="margin-top:6px">'+q.sup.map(function(c){return '<button class="cp" data-sy="'+H(c)+'">'+esc(c)+'</button>'}).join('')+'</div>':'')+'</div></div>'}).join('');
  b.innerHTML='<div class="sec-row"><p class="lead" style="flex:1"><b>'+(isSolo()?'One-to-one.':'Group round.')+'</b> '+esc((p.intro||{})[isSolo()?'solo':'group']||'')+'</p><button class="btn sec" id="pt">PT</button></div>'+
   (p.recall?'<div class="rl-tip">🔁 <span><b>Last class:</b> '+esc(p.recall)+'</span></div>':'')+'<div class="rl-q">'+qs+'</div>'+
   (isSolo()?'':'<div class="rl-in2"><button class="btn" id="who">🎲 Who goes next?</button><label class="lead">Students <input id="wn" type="number" min="2" max="12" value="'+N+'" style="width:64px;padding:4px 8px;border:2px solid var(--line);border-radius:10px;font:inherit;background:var(--paper);color:var(--ink)"></label><span class="chip" id="wr">—</span></div>')+
   (p.tip?'<div class="rl-tip">💡 <span>'+esc(p.tip)+'</span></div>':'');
  var pt=false;$q(b,'#pt').onclick=function(){pt=!pt;$a(b,'.ptx').forEach(function(x){x.style.display=pt?'block':'none'})};wireSay(b);
  if(!isSolo()){var last=0;$q(b,'#who').onclick=function(e){var n=Math.max(2,+$q(b,'#wn').value||4);save('who-n',n);var k;do{k=1+Math.floor(Math.random()*n)}while(k===last&&n>1);last=k;$q(b,'#wr').textContent='Student '+k;gain(0,true,e)}}
  mark()};

 /* 3 · Cultural snapshot */
 R.rl_culture=function(p,b){var lv=saved('culv','A2');
  var cards=(p.cards||[]).map(function(c){return '<div class="rl-card"><div class="pic">'+(c.vis?V(c.vis):'')+'</div><div class="tx"><b>'+esc(c.en)+' '+sayBtn(c.en)+'</b><small>'+esc(c.pt||'')+'</small>'+(c.note?'<p>'+esc(c.note)+'</p>':'')+'</div></div>'}).join('');
  var qs=(p.qs||[]).map(function(q,i){return '<div class="rl-qi" data-q="'+i+'"><span class="n">'+(i+1)+'</span><div style="flex:1">'+esc(q.q)+' '+sayBtn(q.q)+'<small>'+esc(q.pt||'')+'</small><div class="rl-ans" data-a="'+i+'"></div></div></div>'}).join('');
  var lvs=['A1','A2','B1','B2'];
  b.innerHTML='<p class="lead" style="margin:0">'+esc(p.intro||'')+'</p><div class="rl-cards">'+cards+'</div>'+
   '<div class="sec-row"><b>Ask in English</b><span style="flex:1"></span><span class="lead">Model answers by level:</span><div class="rl-lv" id="lv">'+lvs.map(function(x){return '<button data-l="'+x+'" class="'+(x===lv?'on':'')+'">'+x+'</button>'}).join('')+'</div></div><div class="rl-q">'+qs+'</div>'+
   (p.compare?'<div class="rl-cmp"><b>🇧🇷 Compare:</b> '+esc(p.compare)+'</div>':'');
  function showAns(){$a(b,'.rl-ans').forEach(function(a){var q=p.qs[+a.dataset.a],m=(q.levels||{})[lv];a.textContent=m?'Model ('+lv+'): '+m:'';a.classList.toggle('on',!!m&&a.dataset.open==='1')})}
  $a(b,'.rl-qi').forEach(function(q){q.onclick=function(e){if(e.target.closest('[data-sy]'))return;var a=$q(q,'.rl-ans');a.dataset.open=a.dataset.open==='1'?'0':'1';showAns()}});
  $a(b,'#lv button').forEach(function(x){x.onclick=function(){lv=x.dataset.l;save('culv',lv);$a(b,'#lv button').forEach(function(y){y.classList.toggle('on',y===x)});showAns()}});
  showAns();wireSay(b);mark()};

 /* 4 · Scene & listening */
 R.rl_listen=function(p,b){var d=dlg(),sp=Object.keys(d.speakers||{}),lines=d.lines||[],rate=.92,shown=false;
  var sc=p.scene||{};var p1=p.pass1||{},tasks=(p.pass2||{}).tasks||[];
  b.innerHTML='<div class="rl-two"><div style="display:grid;gap:12px"><div class="rl-sc"><div class="frame">'+A.scene(sc.scene||'park',sc.tod||'day',sc.cast||[],'cover')+'</div></div>'+
   '<div class="rl-bar"><button class="btn" id="play">▶ Play the dialogue</button><button class="btn sec" id="slow">🐢 Slow</button><button class="btn sec" id="stop">■ Stop</button><button class="btn sec" id="show">👁 Show text</button></div>'+
   '<div class="rl-bub rl-blur" id="tx">'+lines.map(function(l,i){var sI=sp.indexOf(l.who);return '<div class="rl-ln '+(sI>0?'b':'')+'" data-i="'+i+'"><div class="av">'+faceOf(l.who)+'</div><div class="tb"><div class="wo">'+esc(l.who)+'</div><div class="en">'+hb(l.en)+'</div></div></div>'}).join('')+'</div></div>'+
   '<div style="display:grid;gap:12px;align-content:start"><div class="rl-pass"><h4><i>1</i> First listen — main idea</h4><div class="q" style="font-size:16px">'+esc(p1.q||'')+'</div><small class="lead">'+esc(p1.pt||'')+'</small><div class="opts" id="p1">'+(p1.opts||[]).map(function(o,i){return '<button class="opt" data-i="'+i+'">'+esc(o)+'</button>'}).join('')+'</div></div>'+
   '<div class="rl-pass"><h4><i>2</i> Second listen — find the details</h4><div class="rl-slots">'+tasks.map(function(t,i){return '<div class="rl-slot"><label>'+esc(t.label)+'</label><input data-i="'+i+'" placeholder="…" autocomplete="off"><button class="btn sec" data-rv="'+i+'" style="padding:5px 10px">✔</button></div>'}).join('')+'</div></div></div></div>';
  var mark1=function(i){$a(b,'.rl-ln').forEach(function(x,j){x.classList.toggle('on',j===i)})};
  $q(b,'#play').onclick=function(){playLines(lines,sp,rate,mark1)};$q(b,'#slow').onclick=function(){rate=rate===.92?.7:.92;this.classList.toggle('on',rate!==.92);this.textContent=rate===.92?'🐢 Slow':'🐇 Normal'};
  $q(b,'#stop').onclick=function(){stopAll();mark1(-1)};$q(b,'#show').onclick=function(){shown=!shown;$q(b,'#tx').classList.toggle('rl-show',shown);this.textContent=shown?'🙈 Hide text':'👁 Show text'};
  $a(b,'.rl-ln').forEach(function(x){x.onclick=function(){stopAll();var l=lines[+x.dataset.i];mark1(+x.dataset.i);speakLine(l.en,sp.indexOf(l.who)<=0?0:1,rate)}});
  $a(b,'#p1 .opt').forEach(function(o){o.onclick=function(e){var r=+o.dataset.i===p1.ans;$a(b,'#p1 .opt').forEach(function(x){x.disabled=true});o.classList.add(r?'ok':'bad');if(!r)$a(b,'#p1 .opt')[p1.ans].classList.add('ok');gain(r?10:0,r,e)}});
  $a(b,'[data-rv]').forEach(function(btn){btn.onclick=function(e){var i=+btn.dataset.rv,t=tasks[i],inp=$q(b,'input[data-i="'+i+'"]'),ok=[t.ans].concat(t.alt||[]).some(function(a){return norm(inp.value)===norm(a)||(norm(inp.value)&&norm(a).indexOf(norm(inp.value))>=0&&norm(inp.value).length>=3)});inp.classList.remove('ok','bad');inp.classList.add(ok?'ok':'bad');if(!ok)inp.placeholder='Answer: '+t.ans;if(ok)gain(10,true,e)}});
  mark()};

 /* 5 · Dialogue & comprehension */
 R.rl_dialog=function(p,b){var d=dlg(),sp=Object.keys(d.speakers||{}),lines=d.lines||[],pt=false;
  b.innerHTML='<div class="rl-two"><div style="display:grid;gap:10px"><div class="rl-bar"><button class="btn" id="play">▶ Play</button><button class="btn sec" id="stop">■</button><button class="btn sec" id="pt">PT</button><span class="lead">Tap a line to hear it · <b style="background:linear-gradient(transparent 55%,rgba(242,176,30,.5) 55%)">highlighted</b> = useful chunks</span></div>'+
   '<div class="rl-bub" id="tx">'+lines.map(function(l,i){var sI=sp.indexOf(l.who);return '<div class="rl-ln '+(sI>0?'b':'')+'" data-i="'+i+'"><div class="av">'+faceOf(l.who)+'</div><div class="tb"><div class="wo">'+esc(l.who)+'</div><div class="en">'+hb(l.en)+'</div><div class="pt">'+esc(l.pt||'')+'</div></div></div>'}).join('')+'</div></div>'+
   '<div style="display:grid;gap:12px;align-content:start"><div class="bx soft"><div class="bxh">Check your understanding</div><div class="bxb" id="qq"></div></div>'+
   (p.retell?'<div class="bx soft"><div class="bxh">Retell it</div><div class="bxb"><p style="margin:0 0 6px;font-weight:800">'+esc(p.retell.prompt)+'</p><div class="chips">'+(p.retell.starters||[]).map(function(s){return '<button class="cp" data-sy="'+H(s)+'">'+esc(s)+'</button>'}).join('')+'</div></div></div>':'')+'</div></div>';
  var mk=function(i){$a(b,'.rl-ln').forEach(function(x,j){x.classList.toggle('on',j===i)})};
  $q(b,'#play').onclick=function(){playLines(lines,sp,.92,mk)};$q(b,'#stop').onclick=function(){stopAll();mk(-1)};
  $q(b,'#pt').onclick=function(){pt=!pt;$q(b,'#tx').parentNode.classList.toggle('rl-pt',pt)};
  $a(b,'.rl-ln').forEach(function(x){x.onclick=function(){stopAll();var l=lines[+x.dataset.i];mk(+x.dataset.i);speakLine(l.en,sp.indexOf(l.who)<=0?0:1,.92)}});
  A.mcqBlock($q(b,'#qq'),(p.qs||[]).map(function(q){return {q:q.q,opts:q.opts,ans:q.ans,say:q.say||''}}),function(){mark()});wireSay(b);mark()};

 /* 6 · Useful expressions */
 R.rl_chunks=function(p,b){var items=p.items||[],dc=p.discover;
  var rows=items.map(function(it,i){return '<div class="rl-ch'+(it.pri?' pri':'')+'" data-i="'+i+'"><span class="st">'+(it.pri?'★':(i+1))+'</span><div><div class="en">'+esc(it.en)+(it.reg?'<span class="fm">'+esc(it.reg)+'</span>':'')+'</div><div class="us">'+esc(it.use||'')+'</div>'+(it.alt?'<div class="rl-alt">'+hb(it.alt)+'</div>':'')+'</div><div class="pt">'+esc(it.pt||'')+'</div></div>'}).join('');
  b.innerHTML='<div class="sec-row"><p class="lead" style="flex:1"><b>★ = prioridade:</b> use 3–5 destas expressões repetidamente. As outras são repertório de compreensão. <span style="opacity:.8">Toque para ouvir.</span></p><button class="btn sec" id="all">▶ Listen to all</button></div><div style="display:grid;gap:10px">'+rows+'</div>'+
   (dc?'<div class="bx soft"><div class="bxh">Discover: when do you say it?</div><div class="bxb" style="display:grid;gap:8px">'+(dc.items||[]).map(function(x,i){return '<div class="rl-fn"><b style="min-width:200px">“'+esc(x.en)+'”</b><select data-i="'+i+'"><option value="">— choose —</option>'+(dc.fns||[]).map(function(f){return '<option>'+esc(f)+'</option>'}).join('')+'</select></div>'}).join('')+'</div></div>':'')+(p.note?'<div class="rl-tip">💡 <span>'+hb(p.note)+'</span></div>':'');
  $a(b,'.rl-ch').forEach(function(r){r.onclick=function(){stopAll();say(items[+r.dataset.i].en)}});
  $q(b,'#all').onclick=async function(){var my=++TOK;for(var i=0;i<items.length;i++){if(my!==TOK)return;var r=$a(b,'.rl-ch')[i];r.style.borderColor='var(--acc)';await speakLine(items[i].en,0,.9);r.style.borderColor=''}};
  if(dc)$a(b,'.rl-fn select').forEach(function(s){s.onchange=function(e){var ok=s.value===dc.items[+s.dataset.i].fn;s.classList.remove('ok','bad');s.classList.add(ok?'ok':'bad');if(ok)gain(5,true,e)}});
  mark()};

 /* 7 · Grammar & patterns (com troca de palavras) */
 R.rl_patterns=function(p,b){var sw=p.swap,st={},reg=p.register;
  var pats=(p.patterns||[]).map(function(x,i){return '<div class="rl-pat"><div class="h"><span>Pattern '+String(i+1).padStart(2,'0')+' — '+esc(x.name)+'</span>'+(x.main?'<em>main focus</em>':'<em>expansion</em>')+'</div><div class="f">'+hb(x.formula).replace(/<b>/g,'<span class="c">').replace(/<\/b>/g,'</span>')+'</div><ul>'+(x.ex||[]).map(function(e){return '<li data-sy="'+H(e)+'">'+esc(e)+' 🔊</li>'}).join('')+'</ul></div>'}).join('');
  var swap='';if(sw){(sw.slots||[]).forEach(function(s){st[s.k]=0});swap='<div class="rl-swap"><div class="sec-row"><b style="flex:1">🔁 Swap the words — say it with every combination</b><button class="btn" id="shuf">🎰 Shuffle</button><button class="btn sec" id="sayit">🔊 Say it</button></div><div class="sf" id="sf"></div><div class="mean" id="mean"></div><div class="opts2" id="o2"></div></div>'}
  b.innerHTML='<div class="rl-two" style="align-items:start"><div style="display:grid;gap:12px">'+pats+'</div><div style="display:grid;gap:12px">'+swap+(reg?'<div class="rl-reg"><div class="hd">'+esc((reg.head||[])[0]||'Spoken')+'</div><div class="hd" style="border-left:2px solid rgba(255,255,255,.4)">'+esc((reg.head||[])[1]||'Written')+'</div>'+(reg.rows||[]).map(function(r){return '<div class="c">'+esc(r[0])+'</div><div class="c">'+esc(r[1])+'</div>'}).join('')+'</div>'+(reg.note?'<div class="rl-tip">ℹ️ <span>'+esc(reg.note)+'</span></div>':''):'')+'</div></div>';
  if(sw){var cur=null;
   var frame=function(){return sw.frame.replace(/\{(\w+)\}/g,function(_,k){var s=sw.slots.filter(function(x){return x.k===k})[0];return s?s.opts[st[k]].en:k})};
   var meaning=function(){return (sw.tpt||'').replace(/\{(\w+)\}/g,function(_,k){var s=sw.slots.filter(function(x){return x.k===k})[0];return s?(s.opts[st[k]].pt||s.opts[st[k]].en):k})};
   var draw=function(pop){var h=sw.frame.split(/(\{\w+\})/).map(function(tok){var m=/^\{(\w+)\}$/.exec(tok);if(!m)return esc(tok);var s=sw.slots.filter(function(x){return x.k===m[1]})[0];return '<button class="sw'+(pop===m[1]?' pop':'')+'" data-k="'+s.k+'">'+esc(s.opts[st[s.k]].en)+'</button>'}).join('');$q(b,'#sf').innerHTML=h;$q(b,'#mean').textContent=meaning();
    $a(b,'#sf .sw').forEach(function(x){x.onclick=function(){cur=x.dataset.k;var s=sw.slots.filter(function(y){return y.k===cur})[0];st[cur]=(st[cur]+1)%s.opts.length;draw(cur);speakLine(frame(),0,.95);opts()}});opts()};
   var opts=function(){var k=cur||sw.slots[0].k,s=sw.slots.filter(function(y){return y.k===k})[0];$q(b,'#o2').innerHTML='<span class="lead"><b>'+esc(s.label)+':</b></span>'+s.opts.map(function(o,i){return '<button data-i="'+i+'" class="'+(i===st[k]?'on':'')+'">'+esc(o.en)+'</button>'}).join('');$a(b,'#o2 button').forEach(function(x){x.onclick=function(){st[k]=+x.dataset.i;draw(k);speakLine(frame(),0,.95)}})};
   $q(b,'#shuf').onclick=function(e){sw.slots.forEach(function(s){st[s.k]=Math.floor(Math.random()*s.opts.length)});cur=null;draw(sw.slots[0].k);speakLine(frame(),0,.95);gain(2,true,e)};
   $q(b,'#sayit').onclick=function(){speakLine(frame(),0,.95)};draw();}
  wireSay(b);mark()};

 /* 8 · Pronunciation lab */
 R.rl_pron=function(p,b){var tab=0,items=p.items||[];
  var head='<div class="rl-sit"><b>Focus · '+esc(p.focus||'')+'</b>'+esc(p.tip||'')+'</div><div class="rl-tabs" id="tb"><button data-t="0" class="on"><i>1</i> Listen & identify</button><button data-t="1"><i>2</i> Repeat the rhythm</button><button data-t="2"><i>3</i> Use it</button></div><div id="pn" style="display:grid;gap:12px"></div>';
  b.innerHTML=head;var pn=$q(b,'#pn');
  var views=[function(){
    pn.innerHTML=items.map(function(it,i){return '<div class="rl-pr"><div class="tx">'+esc(it.say)+'</div>'+(it.linked?'<div class="lk">'+esc(it.linked)+'</div>':'')+(it.ipa?'<div class="ip">'+esc(it.ipa)+'</div>':'')+'<div class="rl-bar"><button class="btn" data-n="'+i+'">🔊 Normal</button><button class="btn sec" data-s="'+i+'">🐢 Slow</button></div></div>'}).join('')+
     ((p.identify&&p.identify.length)?'<div class="bx soft"><div class="bxh">Which one do you hear?</div><div class="bxb" id="idn"></div></div>':'');
    $a(pn,'[data-n]').forEach(function(x){x.onclick=function(){stopAll();speakLine(items[+x.dataset.n].say,0,.95)}});$a(pn,'[data-s]').forEach(function(x){x.onclick=function(){stopAll();speakLine(items[+x.dataset.s].say,0,.65)}});
    if(p.identify&&p.identify.length)A.mcqBlock($q(pn,'#idn'),p.identify.map(function(q){return {q:q.q||'Which one do you hear?',opts:q.opts,ans:q.ans,say:q.say,auto:1}}),function(){mark()})},
   function(){pn.innerHTML=items.map(function(it,i){var r=(it.rhythm||'oOoO').split('');return '<div class="rl-pr"><div class="tx">'+esc(it.say)+'</div><div class="rl-dots" data-d="'+i+'">'+r.map(function(c){return '<i class="'+(c==='O'?'big':'sm')+'"></i>'}).join('')+'</div><div class="rl-bar"><button class="btn" data-p="'+i+'">▶ Follow the rhythm</button><span class="lead">Big dot = stressed. Clap or tap with each dot.</span></div></div>'}).join('');
    $a(pn,'[data-p]').forEach(function(x){x.onclick=async function(){var i=+x.dataset.p,ds=$a(pn,'[data-d="'+i+'"] i'),it=items[i],my=++TOK;var pr=speakLine(it.say,0,.85);for(var k=0;k<ds.length;k++){if(my!==TOK)return;ds.forEach(function(d){d.classList.remove('hit')});ds[k].classList.add('hit');await new Promise(function(r){setTimeout(r,Math.max(230,Math.round(1300/ds.length)))})}ds.forEach(function(d){d.classList.remove('hit')});await pr;gain(2,true,{target:x})}})},
   function(){var o=p.own||{};pn.innerHTML='<div class="bx soft"><div class="bxh">Your turn</div><div class="bxb" style="display:grid;gap:8px"><p style="margin:0;font-weight:800">'+esc(o.prompt||'Make your own question using the same sound pattern.')+'</p><div class="rl-in"><input id="ow" placeholder="Type your sentence…" value="'+H(saved('pron-own',''))+'"><button class="btn" id="ows">🔊 Say it</button></div><div class="rl-tip">🎯 <span>'+esc(o.criteria||'Listen to yourself: did the words connect smoothly?')+'</span></div></div></div>';
    $q(pn,'#ow').oninput=function(e){save('pron-own',e.target.value)};$q(pn,'#ows').onclick=function(e){var v=$q(pn,'#ow').value;if(v){speakLine(v,0,.9);gain(5,true,e)}}}];
  function show(t){tab=t;$a(b,'#tb button').forEach(function(x){x.classList.toggle('on',+x.dataset.t===t)});views[t]();wireSay(b)}
  $a(b,'#tb button').forEach(function(x){x.onclick=function(){show(+x.dataset.t)}});show(0);mark()};

 /* 9 · Guided challenges */
 R.rl_challenge=function(p,b){var levels=p.levels||[],total=0,okN=0,doneN=0;levels.forEach(function(l){total+=(l.items||[]).length});
  var body=levels.map(function(l,li){return '<div class="rl-lvh">'+esc(l.h)+'</div>'+(l.items||[]).map(function(it,ii){return '<div class="rl-it" data-l="'+li+'" data-i="'+ii+'"></div>'}).join('')}).join('');
  b.innerHTML='<div class="rl-sc2"><b>Quick Language Challenge</b><div class="bar"><i id="bar"></i></div><span class="chip" id="sc">0 / '+total+'</span></div>'+body;
  function fin(box,ok,e){box.classList.add('done',ok?'ok':'bad');doneN++;if(ok){okN++;gain(10,true,e)}else gain(0,false,e);$q(b,'#sc').textContent=okN+' / '+total;$q(b,'#bar').style.width=(doneN/total*100)+'%';if(doneN===total){mark();if(okN===total)A.confetti()}}
  $a(b,'.rl-it').forEach(function(box){var it=levels[+box.dataset.l].items[+box.dataset.i],ty=it.type||'mcq';
   var why=function(){return '<div class="why">'+(it.why?esc(it.why):'')+(it.model?' <b>Model:</b> '+esc(it.model):'')+'</div>'};
   if(ty==='mcq'||ty==='reply'){box.innerHTML=(ty==='reply'?'<div class="npc">'+esc(it.npc)+' '+sayBtn(it.npc)+'</div>':'')+'<div class="pq">'+esc(it.q||'Choose the best reply.')+'</div><div class="opts">'+it.opts.map(function(o,i){return '<button class="opt" data-o="'+i+'">'+esc(o)+'</button>'}).join('')+'</div>'+why();
    $a(box,'.opt').forEach(function(o){o.onclick=function(e){if(box.classList.contains('done'))return;var r=+o.dataset.o===it.ans;$a(box,'.opt').forEach(function(x){x.disabled=true});o.classList.add(r?'ok':'bad');if(!r)$a(box,'.opt')[it.ans].classList.add('ok');fin(box,r,e)}})}
   else if(ty==='gap'||ty==='swap'){var gapAns=ty==='gap'?[it.ans||''].concat(it.alt||[]):it.ans;var prompt=ty==='gap'?it.text:it.instr+'  “'+it.from+'”';
    box.innerHTML='<div class="pq">'+esc(prompt)+(it.say?' '+sayBtn(it.say):'')+'</div>'+(it.bank?'<div class="chips">'+it.bank.map(function(w){return '<button class="cp" data-w="'+H(w)+'">'+esc(w)+'</button>'}).join('')+'</div>':'')+'<div class="rl-in"><input placeholder="Type your answer…" autocomplete="off"><button class="btn" data-ck="1">Check</button></div>'+why();
    var inp=$q(box,'input');$a(box,'[data-w]').forEach(function(w){w.onclick=function(){inp.value=w.dataset.w;inp.focus()}});
    $q(box,'[data-ck]').onclick=function(e){if(box.classList.contains('done'))return;var v=norm(inp.value);if(!v)return;var r=(gapAns||[]).some(function(a){return norm(a)===v});box.classList.remove('bad');if(!r&&!box.dataset.try){box.dataset.try='1';box.classList.add('bad');inp.focus();return}if(!r)inp.value=gapAns[0];inp.disabled=true;fin(box,r,e)}}
   wireSay(box)});
  mark()};

 /* 10a · Communication lab (grupo): rodízio + information gap */
 R.rl_lab=function(p,b){var N=saved('lab-n',4),rd=0,tm;
  function rotations(n){var m=n%2?n+1:n,rounds=[],ring=[];for(var i=1;i<m;i++)ring.push(i);var R2=Math.min(m-1,Math.max(1,(p.rounds||[]).length-1))+0;
   for(var r=0;r<m-1;r++){var pairs=[[0,ring[r]]];for(var k=1;k<m/2;k++){pairs.push([ring[(r+k)%(m-1)],ring[(r-k+(m-1)*2)%(m-1)]])}
    rounds.push(pairs.filter(function(x){return x[0]<n&&x[1]<n}))}return rounds}
  function pname(i){return String.fromCharCode(65+i)}
  function draw(){var rots=rotations(N);b.innerHTML='<div class="sec-row"><p class="lead" style="flex:1"><b>Conversation rotations.</b> Pairs change every round: same function, new information. Individual accountability: each student asks ≥1 question and answers ≥1.</p><label class="lead">Students <input id="ln" type="number" min="2" max="8" value="'+N+'" style="width:60px;padding:4px 8px;border:2px solid var(--line);border-radius:10px;font:inherit;background:var(--paper);color:var(--ink)"></label></div>'+
   '<div class="rl-rnd">'+(p.rounds||[]).map(function(r,i){var pr=rots[i%rots.length]||[];return '<div class="rl-r'+(i===rd?' cur':'')+'" data-r="'+i+'"><div class="t"><i>'+(i+1)+'</i>'+esc(r.title)+'<span style="margin-left:auto" class="lead">'+(r.min||3)+' min</span></div><div class="rl-pair">'+(r.whole?'<span>👥 Whole group</span>':pr.map(function(x){return '<span>'+pname(x[0])+' ⇄ '+pname(x[1])+'</span>'}).join(''))+'</div><div>'+esc(r.task||'')+'</div>'+(r.hint?'<small class="lead">'+esc(r.hint)+'</small>':'')+'</div>'}).join('')+'</div>'+
   '<div class="sec-row"><span class="rl-tm" id="tm">3:00</span><button class="btn" id="go">▶ Start round</button><button class="btn sec" id="nx">Next round →</button></div>'+
   (p.infogap?infogap():'');
   tm=timer($q(b,'#tm'),((p.rounds||[])[rd]||{min:3}).min*60||180,function(){gain(0,true,{target:b});$q(b,'#go').textContent='▶ Start round'});
   $q(b,'#go').onclick=function(){var run=tm.toggle();this.textContent=run?'⏸ Pause':'▶ Resume'};$q(b,'#nx').onclick=function(){rd=(rd+1)%((p.rounds||[]).length||1);draw();mark()};$q(b,'#ln').onchange=function(){N=Math.max(2,Math.min(8,+this.value||4));save('lab-n',N);rd=0;draw()};
   var rv=false;if(p.infogap){$a(b,'[data-ig]').forEach(function(x){x.onclick=function(){x.classList.toggle('on')}})}}
  function infogap(){var g=p.infogap,card=function(c,k){return '<div class="rl-card2"><div class="h">Card '+k+'<em>'+esc(c.title||'')+'</em></div><div class="cbd"><p><b>'+esc(c.task||'')+'</b></p>'+(c.rows||[]).map(function(r){return '<p><span style="color:var(--mut)">'+esc(r.k)+':</span> '+(r.v?'<b>'+esc(r.v)+'</b>':'<span style="letter-spacing:.2em">______</span>')+'</p>'}).join('')+'</div></div>'};return '<div class="bx soft"><div class="bxh">Information gap · '+esc(g.title||'')+'</div><div class="bxb" style="display:grid;gap:10px"><p style="margin:0;font-weight:800">'+esc(g.instr||'')+'</p><div class="grid g2">'+card(g.a,'A')+card(g.b,'B')+'</div></div></div>'}
  draw();mark()};

 /* 10b · Personalized roleplay (particular) */
 R.rl_role=function(p,b){var rd=0,br=p.brief||{},rounds=p.rounds||[];
  var chk=saved('role-chk',{});
  b.innerHTML='<div class="rl-two" style="align-items:start"><div style="display:grid;gap:12px"><div class="rl-card2"><div class="h">🎭 Roles<em>1-to-1</em></div><div class="cbd"><p><b>Teacher:</b> '+esc(br.teacher||'')+'</p><p><b>Student:</b> '+esc(br.student||'')+'</p></div></div>'+
   '<div class="rl-prog" id="rp">'+rounds.map(function(r,i){return '<button data-r="'+i+'" class="'+(i===0?'on':'')+'">Round '+(i+1)+' · '+esc(r.label)+'<small>'+esc(r.desc||'')+'</small></button>'}).join('')+'</div><div id="help"></div>'+
   '<div class="rl-bar"><button class="btn" id="d1">🎴 Draw an order</button><button class="btn" id="d2" style="background:var(--c-speak)">⚡ Draw a complication</button></div><div class="rl-draw" id="dr"><span>Draw cards to start the roleplay<small>The teacher plays the staff and changes the plan on the spot.</small></span></div></div>'+
   '<div style="display:grid;gap:12px"><div class="bx soft"><div class="bxh">Success criteria</div><div class="bxb rl-chk" id="sc">'+(p.success||[]).map(function(s,i){return '<label class="'+(chk[i]?'on':'')+'"><input type="checkbox" data-i="'+i+'" '+(chk[i]?'checked':'')+'><span>'+esc(s)+'</span></label>'}).join('')+'</div></div><div class="rl-tip">⏱ <span>Talk-time goal: the student speaks about 60–70% of the time.</span></div></div></div>';
  function help(){var r=rounds[rd]||{};$q(b,'#help').innerHTML=r.help&&r.help.length?'<div class="rl-help'+(r.kw?' kw':'')+'">'+r.help.map(function(h){return '<button class="cp" data-sy="'+H(h)+'">'+esc(h)+'</button>'}).join('')+'</div>':'<div class="rl-tip">🚫 <span>No help on screen. Use what you remember.</span></div>';wireSay($q(b,'#help'))}
  $a(b,'#rp button').forEach(function(x){x.onclick=function(){rd=+x.dataset.r;$a(b,'#rp button').forEach(function(y){y.classList.toggle('on',y===x)});help()}});help();
  var draw=function(list,label){var v=list[Math.floor(Math.random()*list.length)];$q(b,'#dr').innerHTML='<span>'+esc(v)+'<small>'+label+'</small></span>'};
  $q(b,'#d1').onclick=function(){draw(p.orders||['—'],'Customer order')};$q(b,'#d2').onclick=function(){draw(p.complications||['—'],'Unexpected problem')};
  $a(b,'#sc input').forEach(function(x){x.onchange=function(e){chk[x.dataset.i]=x.checked;save('role-chk',chk);x.parentNode.classList.toggle('on',x.checked);if(x.checked)gain(5,true,e);if($a(b,'#sc input').every(function(y){return y.checked})){A.confetti();mark()}}});mark()};

 /* 11 · Group mission */
 R.rl_mission=function(p,b){var tm;var ms=p.missions||[];
  b.innerHTML='<div class="rl-sit"><b>Mission</b>'+esc(p.goal||'')+'</div><div class="rl-cards">'+ms.map(function(m){return '<div class="rl-card2"><div class="h">Group '+esc(m.who)+'<em>'+esc(m.role||'')+'</em></div><div class="cbd"><p><b>Your mission:</b> '+esc(m.mission)+'</p><p><b>Constraint:</b> '+esc(m.constraint||'—')+'</p><p style="color:var(--mut)"><b>Start with:</b> “'+esc(m.start||'')+'” '+(m.start?sayBtn(m.start):'')+'</p></div></div>'}).join('')+'</div>'+
   '<div class="bx soft"><div class="bxh">Success criteria</div><div class="bxb rl-chk">'+(p.success||[]).map(function(s,i){return '<label><input type="checkbox"><span>'+esc(s)+'</span></label>'}).join('')+'</div></div>'+
   '<div class="sec-row"><span class="rl-tm" id="tm">11:00</span><button class="btn" id="go">▶ Start mission</button><button class="btn sec" id="cp">📋 Copy mission to class chat</button></div>';
  tm=timer($q(b,'#tm'),(p.min||11)*60);$q(b,'#go').onclick=function(){var r=tm.toggle();this.textContent=r?'⏸ Pause':'▶ Resume'};
  $q(b,'#cp').onclick=function(){var t='MISSION — '+(p.goal||'')+'\n'+ms.map(function(m){return 'Group '+m.who+' ('+m.role+'): '+m.mission+' | Constraint: '+m.constraint}).join('\n');try{navigator.clipboard.writeText(t);this.textContent='✔ Copied'}catch(e){this.textContent='Copy failed'}};
  $a(b,'.rl-chk input').forEach(function(x){x.onchange=function(e){x.parentNode.classList.toggle('on',x.checked);if(x.checked)gain(5,true,e);if($a(b,'.rl-chk input').every(function(y){return y.checked})){A.confetti();mark()}}});wireSay(b);mark()};

 /* 12 · Writing */
 R.rl_write=function(p,b){var fx=saved('fix',[]),n=p.fix&&p.fix.n||3;
  b.innerHTML='<div class="rl-two" style="align-items:start"><div style="display:grid;gap:12px"><div class="rl-sit"><b>Writing task</b>'+esc(p.task||'')+'</div><div class="rl-steps">'+(p.steps||[]).map(function(s){return '<span>'+esc(s)+'</span>'}).join('')+'</div>'+
   '<div class="rl-model"><b style="font-size:12px;letter-spacing:.07em;text-transform:uppercase;color:var(--ok)">Model</b><br>'+hb(p.model||'')+' '+sayBtn((p.model||'').replace(/\*\*/g,''))+'</div>'+textArea('write','Write your own message here…',140)+
   '<div class="rl-chk">'+(p.checklist||[]).map(function(c,i){return '<label><input type="checkbox" data-c="'+i+'"><span>'+esc(c)+'</span></label>'}).join('')+'</div></div>'+
   '<div style="display:grid;gap:12px"><div class="bx soft"><div class="bxh">Feedback · fix 2–3 priorities</div><div class="bxb" style="display:grid;gap:8px"><p class="lead" style="margin:0">Write what the student wrote and a more natural way to say it.</p>'+[...Array(n)].map(function(_,i){return '<div class="rl-fixr"><input data-f="'+i+'a" placeholder="Student wrote…" value="'+H((fx[i]||{}).a||'')+'"><input data-f="'+i+'b" placeholder="More natural…" value="'+H((fx[i]||{}).b||'')+'"></div>'}).join('')+'</div></div>'+(p.tip?'<div class="rl-tip">💡 <span>'+esc(p.tip)+'</span></div>':'')+'</div></div>';
  wireTA(b);wireSay(b);$a(b,'[data-f]').forEach(function(x){x.oninput=function(){var i=parseInt(x.dataset.f,10),k=x.dataset.f.slice(-1);fx[i]=fx[i]||{};fx[i][k]=x.value;save('fix',fx)}});
  $a(b,'.rl-chk input').forEach(function(x){x.onchange=function(e){x.parentNode.classList.toggle('on',x.checked);if(x.checked)gain(3,true,e)}});mark()};

 /* 13 · Feedback & review (rubrica) */
 R.rl_feedback=function(p,b){var sc=saved('rub',{}),cr=p.criteria||[];
  b.innerHTML='<div class="rl-two" style="align-items:start"><div class="rl-rub"><div class="sec-row"><b style="flex:1">Speaking Performance Check</b><span class="lead">1–5 per criterion · internal tracking, not a CEFR certificate</span></div>'+cr.map(function(c){return '<div class="rl-cr"><div><b>'+esc(c.name)+'</b><small>'+esc(c.desc||'')+'</small></div><div class="rl-sc5" data-k="'+c.k+'">'+[1,2,3,4,5].map(function(n){return '<button data-n="'+n+'" class="'+(sc[c.k]===n?'on':'')+'">'+n+'</button>'}).join('')+'</div><div class="v" data-v="'+c.k+'">'+(sc[c.k]||'–')+'</div></div>'}).join('')+'<div class="rl-tot"><span class="n" id="tot">0</span><span style="font-size:20px;font-weight:900">/ '+(cr.length*5)+'</span><p id="int"></p></div></div>'+
   '<div class="rl-3" style="grid-template-columns:1fr">'+[['well','What you did well','✅'],['improve','What to improve','🔧'],['next','Your next challenge','🚀']].map(function(x){return '<div class="bx"><div class="bxh">'+x[2]+' '+x[1]+'</div><textarea data-save="fb-'+x[0]+'" data-k="fb-'+x[0]+'" placeholder="'+H(((p.prompts||{})[x[0]])||'')+'">'+H(saved('fb-'+x[0],''))+'</textarea></div>'}).join('')+'<button class="btn sec" id="cpy">📋 Copy summary</button></div></div>';
  function recalc(){var t=0,n=0;cr.forEach(function(c){if(sc[c.k]){t+=sc[c.k];n++}});$q(b,'#tot').textContent=t;var txt='Mark the criteria to see the interpretation.';if(n===cr.length){var map=p.interpret||[];txt=(map.filter(function(m){return t<=m.max})[0]||map[map.length-1]||{text:''}).text}$q(b,'#int').textContent=txt}
  $a(b,'.rl-sc5').forEach(function(g){$a(g,'button').forEach(function(x){x.onclick=function(){sc[g.dataset.k]=+x.dataset.n;save('rub',sc);$a(g,'button').forEach(function(y){y.classList.toggle('on',y===x)});$q(b,'[data-v="'+g.dataset.k+'"]').textContent=x.dataset.n;recalc()}})});
  wireTA(b);$q(b,'#cpy').onclick=function(){var t='Speaking Performance Check\n'+cr.map(function(c){return c.name+': '+(sc[c.k]||'-')+'/5'}).join('\n')+'\nWhat you did well: '+saved('fb-well','')+'\nWhat to improve: '+saved('fb-improve','')+'\nYour next challenge: '+saved('fb-next','');try{navigator.clipboard.writeText(t);this.textContent='✔ Copied'}catch(e){this.textContent='Copy failed'}};
  recalc();mark()};

 /* 14 · Exit ticket & homework */
 R.rl_exit=function(p,b){var st=saved('exit',{}),hw=saved('hw',{}),h=p.homework||{},sp=p.spaced||{};
  b.innerHTML='<div class="rl-two" style="align-items:start"><div style="display:grid;gap:12px"><div class="rl-sit"><b>Exit ticket · no notes</b>Show three skills without looking at your notes.</div><div class="rl-ex">'+(p.tasks||[]).map(function(t,i){return '<div class="it'+(st[i]?' on':'')+'" data-i="'+i+'"><div class="ic">'+esc(t.ic||'✔')+'</div><div><b>'+esc(t.name)+'</b><small>'+esc(t.prompt)+'</small><small class="mdl" style="display:none;color:var(--ok);font-weight:800">Model: '+esc(t.model||'')+'</small></div><div style="display:grid;gap:6px"><button class="tg" data-t="'+i+'">'+(st[i]?'✔ Done':'Mark done')+'</button><button class="tg" data-m="'+i+'" style="font-size:12px">Model</button></div></div>'}).join('')+'</div></div>'+
   '<div style="display:grid;gap:12px"><div class="bx soft"><div class="bxh">🎒 '+esc(h.h||'Your real-life English mission')+'</div><div class="bxb rl-hw"><div class="rl-hwp"><span>≈ '+esc(h.min||'10–15')+' min</span><div class="bar"><i id="hb"></i></div><span id="hc">0 / '+((h.items||[]).length)+'</span></div><div class="rl-chk">'+(h.items||[]).map(function(x,i){return '<label class="'+(hw[i]?'on':'')+'"><input type="checkbox" data-i="'+i+'" '+(hw[i]?'checked':'')+'><span>'+esc(x)+'</span></label>'}).join('')+'</div></div></div>'+
   '<div class="bx soft"><div class="bxh">🔁 Spaced review</div><div class="bxb rl-spaced"><div><b>Next class</b>'+esc((sp.next||[]).join(' · '))+'</div><div><b>In one week</b>'+esc((sp.week||[]).join(' · '))+'</div><div><b>Unit mission</b>'+esc((sp.unit||[]).join(' · '))+'</div></div></div></div></div>';
  $a(b,'[data-t]').forEach(function(x){x.onclick=function(e){var i=+x.dataset.t;st[i]=!st[i];save('exit',st);x.parentNode.parentNode.classList.toggle('on',!!st[i]);x.textContent=st[i]?'✔ Done':'Mark done';if(st[i])gain(10,true,e);if((p.tasks||[]).every(function(_,k){return st[k]})){A.confetti();mark()}}});
  $a(b,'[data-m]').forEach(function(x){x.onclick=function(){var m=$q(x.parentNode.parentNode,'.mdl');m.style.display=m.style.display==='none'?'block':'none'}});
  function hwp(){var n=0;(h.items||[]).forEach(function(_,i){if(hw[i])n++});$q(b,'#hc').textContent=n+' / '+(h.items||[]).length;$q(b,'#hb').style.width=((h.items||[]).length?n/(h.items||[]).length*100:0)+'%'}
  $a(b,'.rl-hw input').forEach(function(x){x.onchange=function(e){hw[x.dataset.i]=x.checked;save('hw',hw);x.parentNode.classList.toggle('on',x.checked);if(x.checked)gain(3,true,e);hwp()}});hwp();mark()};

 /* 15 · Level up: a mesma situação do A1 ao C2 */
 R.rl_levels=function(p,b){
  b.innerHTML='<p class="lead" style="margin:0">'+esc(p.intro||'Same situation, growing complexity. The structure stays; the autonomy and nuance evolve.')+'</p><div class="rl-lad">'+(p.ladder||[]).map(function(r){return '<div class="rl-rung'+(r.lv===p.you?' you':'')+'" style="--c:'+(lvColor[r.lv]||'#2f6fe0')+'" data-sy="'+H(r.say)+'"><div class="lv">'+esc(r.lv)+'</div><div><div class="t">“'+esc(r.say)+'”</div><small>'+esc(r.goal||'')+'</small></div>'+(r.lv===p.you?'<span class="yb">YOU ARE HERE</span>':'<span>🔊</span>')+'</div>'}).join('')+'</div>'+(p.note?'<div class="rl-tip">ℹ️ <span>'+esc(p.note)+'</span></div>':'');
  $a(b,'.rl-rung').forEach(function(x){x.onclick=function(){stopAll();say(x.dataset.sy)}});mark()};
};

/* ---------- linha do tempo + roteiro do professor ---------- */
var tpOpen=false,tpMode=null;
function fmt2(n){return String(n).padStart(2,'0')}
function planOf(L,mode){var pl=(L.plan||{})[mode]||[];var t=0;return pl.map(function(s){var o={id:s.id,name:s.name,min:s.min,from:t,to:t+s.min,c:s.c,desc:s.desc,ic:s.ic};t+=s.min;return o})}
function renderTimeline(p,i,pages){var L=A.lesson(),mode=A.mode(),plan=planOf(L,mode),tl=document.getElementById('tl');if(!tl)return;var cur=(p.stage&&typeof p.stage==='object')?p.stage[mode]:p.stage;
  var total=plan.length?plan[plan.length-1].to:60,curIdx=plan.findIndex(function(s){return s.id===cur});
  tl.innerHTML=plan.map(function(s,k){return '<button class="st '+(k===curIdx?'cur':(k<curIdx?'past':''))+'" style="--c:'+(s.c||'#2f6fe0')+';flex:'+Math.max(1,s.min)+' 1 0" data-s="'+s.id+'" title="'+H(s.desc||'')+'"><em>'+(s.ic?s.ic+' ':'')+fmt2(s.from)+'–'+fmt2(s.to)+'</em><b>'+H(s.name)+'</b></button>'}).join('')+'<span class="tm0" id="tm0">⏱ 00:00 / '+total+':00</span>';
  Array.prototype.forEach.call(tl.querySelectorAll('.st'),function(x){x.onclick=function(){var id=x.dataset.s,j=A.pages().findIndex(function(q){return ((q.stage&&typeof q.stage==='object')?q.stage[A.mode()]:q.stage)===id});var rb=document.querySelectorAll('#rail .sg')[j];if(rb)rb.click()}})}
setInterval(function(){var el=document.getElementById('tm0');if(!el||!A)return;var L=A.lesson(),pl=planOf(L,A.mode()),total=pl.length?pl[pl.length-1].to:60,s=Math.floor((Date.now()-T0)/1000);el.firstChild&&(el.textContent='⏱ '+fmt2(Math.floor(s/60))+':'+fmt2(s%60)+' / '+total+':00');el.classList.toggle('over',s/60>total)},1000);
function renderTeacher(p){var tp=document.getElementById('tp');if(!tp)return;if(!tpOpen){tp.hidden=true;return}tp.hidden=false;
  var L=A.lesson(),mode=tpMode||A.mode(),plan=planOf(L,A.mode()),st=plan.filter(function(s){return s.id===((p.stage&&typeof p.stage==='object')?p.stage[A.mode()]:p.stage)})[0]||{},t=p.teach||{},def=DEF[p.t]||{};
  var steps=t[mode]||def[mode]||[];var ul=function(a,cls){return a&&a.length?'<ul>'+a.map(function(x){return '<li class="'+(cls||'')+'">'+H(x)+'</li>'}).join('')+'</ul>':''};
  var ans=t.answers;var ansH=Array.isArray(ans)?ul(ans):(ans?'<p style="margin:0">'+H(ans)+'</p>':'');
  var errs=t.errors&&t.errors.length?'<ul>'+t.errors.map(function(e){return '<li><span class="wr">'+H(e.w)+'</span> → <span class="rt">'+H(e.r)+'</span></li>'}).join('')+'</ul>':'';
  tp.style.setProperty('--acc',st.c||'#2f6fe0');
  tp.innerHTML='<h3>📋 Roteiro do professor <small>'+(st.name?H(st.name)+' · '+fmt2(st.from)+'–'+fmt2(st.to)+' min':'')+'</small><button class="tpx" id="tpx" aria-label="Fechar">×</button></h3>'+
   '<div class="sg2"><button data-m="solo" class="'+(mode==='solo'?'on':'')+'">Particular</button><button data-m="group" class="'+(mode==='group'?'on':'')+'">Grupo</button></div>'+
   (t.goal?'<div class="blk"><b>Objetivo da tela</b>'+H(t.goal)+'</div>':'')+
   '<div class="blk"><b>Como conduzir ('+(mode==='solo'?'1 professor + 1 estudante':'4 a 6 estudantes')+')</b>'+ul(steps)+'</div>'+
   (ansH?'<div class="blk"><b>Respostas</b>'+ansH+'</div>':'')+
   (t.extra&&t.extra.length?'<div class="blk"><b>Perguntas extras</b>'+ul(t.extra)+'</div>':'')+
   (errs?'<div class="blk"><b>Correções frequentes</b>'+errs+'</div>':'')+
   (t.support&&t.support.length?'<div class="blk"><b>Mais apoio</b>'+ul(t.support)+'</div>':'')+
   (t.stretch&&t.stretch.length?'<div class="blk"><b>Para ir além</b>'+ul(t.stretch)+'</div>':'')+
   (st.desc?'<div class="blk"><b>Etapa da aula</b>'+H(st.desc)+'</div>':'');
  var x=document.getElementById('tpx');if(x)x.onclick=function(){tpOpen=false;tp.hidden=true};
  Array.prototype.forEach.call(tp.querySelectorAll('.sg2 button'),function(bn){bn.onclick=function(){tpMode=bn.dataset.m;renderTeacher(p)}})}
window.RL_ONDRAW=function(p,i,pages){if(!A)return;tpMode=null;renderTimeline(p,i,pages);renderTeacher(p)};
document.addEventListener('DOMContentLoaded',function(){var bt=document.getElementById('tpb');if(bt)bt.onclick=function(){tpOpen=!tpOpen;var h=document.getElementById('hudp');if(h)h.hidden=true;var p=A&&A.pages()[A.idx()];if(p)renderTeacher(p)};
  document.addEventListener('keydown',function(e){if(/INPUT|TEXTAREA|SELECT/.test(e.target.tagName))return;if(e.key==='t'||e.key==='T'){tpOpen=!tpOpen;var p=A&&A.pages()[A.idx()];if(p)renderTeacher(p)}});
  document.addEventListener('click',function(e){if(e.target&&e.target.id==='nb'){}});});
})();
