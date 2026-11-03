/* Aulas Quest (aula4.html): tipos de tela gamificados q_* + camada de jogo (mapa de missões, XP, combo, medalha, figurinha).
   Reaproveita as telas rl_* (chunks, padrões, pronúncia, desafios, roleplay/lab/missão, escrita, feedback, exit). */
(function(){
'use strict';
var A=null;
var H=function(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})};
var hb=function(t){return H(t).replace(/\*\*(.+?)\*\*/g,'<b>$1</b>')};
var norm=function(s){return String(s||'').toLowerCase().replace(/[’‘]/g,"'").replace(/[^a-z0-9' ]/g,' ').replace(/\s+/g,' ').trim()};
var $q=function(r,s){return r.querySelector(s)},$a=function(r,s){return Array.prototype.slice.call(r.querySelectorAll(s))};
var STAT={ok:0,tot:0,combo:0,best:0};
/* ---------- fala ---------- */
var TOKQ=0,VOICES=[];
function lv(){try{VOICES=(speechSynthesis.getVoices()||[]).filter(function(v){return /^en/i.test(v.lang)})}catch(e){}}try{lv();speechSynthesis.onvoiceschanged=lv}catch(e){}
function speak(t,who,rate){return new Promise(function(res){try{var u=new SpeechSynthesisUtterance(String(t).replace(/\*\*/g,''));u.lang='en-US';u.rate=rate||.92;u.pitch=who===1?.82:1.12;if(VOICES.length>1){var us=VOICES.filter(function(v){return /US/i.test(v.lang)});var pool=us.length>1?us:VOICES;u.voice=pool[who===1?1%pool.length:0]}u.onend=res;u.onerror=res;speechSynthesis.speak(u);setTimeout(res,15000)}catch(e){res()}})}
function stop(){TOKQ++;try{speechSynthesis.cancel()}catch(e){}}
/* ---------- mascote ---------- */
function poggie(opts){
  opts=opts||{};
  const scarf=opts.scarf||'#0C7A78', id='pg'+(poggie.n=(poggie.n||0)+1);
  return `<svg class="pog ${opts.cls||''}" viewBox="0 0 200 200" role="img" aria-label="Poggie, o ornitorrinco">
  <defs>
    <radialGradient id="${id}f" cx="45%" cy="35%" r="70%"><stop offset="0" stop-color="#A9744E"/><stop offset="1" stop-color="#6E4429"/></radialGradient>
    <linearGradient id="${id}b" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFB85C"/><stop offset="1" stop-color="#E08421"/></linearGradient>
    <linearGradient id="${id}t" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#5B3721"/><stop offset="1" stop-color="#7C4F32"/></linearGradient>
  </defs>
  <ellipse cx="100" cy="186" rx="58" ry="8" fill="rgba(0,0,0,.18)"/>
  <g class="whole">
    <g class="tail"><path d="M58 150 C20 150 8 132 12 118 C18 104 44 110 64 128 Z" fill="url(#${id}t)"/>
      <path d="M22 122 l30 16 M20 132 l32 10 M30 116 l24 18" stroke="#4A2C19" stroke-width="2" opacity=".5"/></g>
    <path d="M64 180 q-4 6 -14 6 q6 -2 4 -8 z M136 180 q4 6 14 6 q-6 -2 -4 -8 z" fill="#F08F2A"/>
    <ellipse cx="100" cy="126" rx="50" ry="56" fill="url(#${id}f)"/>
    <ellipse cx="100" cy="140" rx="31" ry="36" fill="#C99A72"/>
    <path d="M78 176 q-6 8 -18 8 q8 -8 6 -12 z M122 176 q6 8 18 8 q-8 -8 -6 -12 z" fill="#F29B34"/>
    <path d="M60 110 q40 26 80 0 l2 12 q-42 26 -84 0 z" fill="${scarf}"/>
    <path d="M122 118 q10 18 2 34 l-12 -4 q6 -14 -2 -26 z" fill="${scarf}" class="swayT" style="animation-duration:2.2s"/>
    <path d="M70 110 q6 22 44 32" stroke="#3D2517" stroke-width="3" fill="none" opacity=".55"/>
    <g class="arm"><path d="M138 126 q20 -10 22 -30 q2 -8 -6 -6 q-6 12 -22 22 z" fill="#7C4F32"/>
      <rect x="148" y="72" width="22" height="28" rx="2" fill="#E85D75" transform="rotate(12 159 86)"/><rect x="150" y="74" width="4" height="24" fill="#B8384F" transform="rotate(12 159 86)"/></g>
    <path d="M62 132 q-14 10 -10 24 q8 2 14 -10 z" fill="#7C4F32"/>
    <circle cx="80" cy="84" r="13" fill="#fff"/><circle cx="120" cy="84" r="13" fill="#fff"/>
    <g class="blink"><circle cx="82" cy="86" r="7" fill="#15233B"/><circle cx="118" cy="86" r="7" fill="#15233B"/>
      <circle cx="85" cy="83" r="2.4" fill="#fff"/><circle cx="121" cy="83" r="2.4" fill="#fff"/></g>
    <ellipse cx="66" cy="98" rx="7" ry="4" fill="#E88B8B" opacity=".55"/><ellipse cx="134" cy="98" rx="7" ry="4" fill="#E88B8B" opacity=".55"/>
    <path d="M70 96 C70 92 130 92 130 96 C150 98 160 108 150 116 C140 122 60 122 50 116 C40 108 50 98 70 96 Z" fill="url(#${id}b)"/>
    <ellipse cx="90" cy="102" rx="3" ry="2" fill="#9A5A12"/><ellipse cx="110" cy="102" rx="3" ry="2" fill="#9A5A12"/>
    <path class="bill-low" d="M56 116 C80 124 120 124 144 116 C140 126 60 126 56 116 Z" fill="#C9741A"/>
    <path d="M72 58 q28 -18 56 0 q-10 -6 -28 -6 q-18 0 -28 6z" fill="#5F3C25" opacity=".6"/>
  </g></svg>`;
}
/* ---- small illustrated character avatars for dialog lines: gendered on purpose, so a
   student can tell characters apart at a glance the same way they read the big scenes ---- */
/* ---------- capítulos (mapa de missões) ---------- */
var CHAP={q_cover:'mission',rl_warm:'mission',q_culture:'culture',q_read:'read',rl_listen:'talk',rl_dialog:'talk',q_choose:'talk',rl_chunks:'lab',rl_patterns:'lab',rl_pron:'lab',rl_challenge:'arcade',q_arcade:'arcade',rl_role:'boss',rl_lab:'boss',rl_mission:'boss',rl_write:'write',rl_feedback:'write',rl_exit:'wrap',q_wrap:'wrap'};
var HINT={q_cover:'Leia a missão e escolha: o que você quer conseguir fazer hoje?',rl_warm:'Responda com sinceridade, em inglês. Pode ser curto!',q_culture:'Descubra como as pessoas realmente fazem isso. Toque nas abas!',q_read:'Leia uma vez rápido, depois volte para os detalhes. Toque nas palavras sublinhadas.',rl_listen:'Primeiro só ouça. Depois leia o texto.',rl_dialog:'Toque numa fala para ouvir. Os trechos grifados são seus chunks!',q_choose:'Escolha a resposta mais natural. Não existe pressa.',rl_chunks:'As ★ são suas armas de hoje. Use-as várias vezes.',rl_patterns:'Troque as palavras e diga a frase inteira em voz alta.',rl_pron:'Ouça, repita o ritmo e depois crie a sua frase.',rl_challenge:'Do guiado ao livre: justifique cada resposta.',q_arcade:'Faça combos! Acertos seguidos valem mais pontos.',rl_role:'Chefe da fase! Resolva o problema sem sair do inglês.',rl_lab:'Troquem de parceiro a cada rodada.',rl_mission:'Missão em equipe: resolver é mais importante do que ser perfeito.',rl_write:'Uma mensagem curta, mas de verdade.',rl_feedback:'Uma nota é só um mapa para a próxima fase.',rl_exit:'Sem consultar: mostre o que você já faz sozinho.',q_wrap:'Missão cumprida! Veja o que você ganhou.'};
function chapOf(p){return (p&&(p.stage&&typeof p.stage==='object'?p.stage[A.mode()]:p.stage))||CHAP[p.t]}
/* ---------- placar e combo ---------- */
window.RL_ONGAIN=function(n,ok,xp,streak){if(n>0||!ok){STAT.tot++;if(ok&&n>0){STAT.ok++;STAT.combo++;if(STAT.combo>STAT.best)STAT.best=STAT.combo}else STAT.combo=0}
  var c=document.getElementById('qcombo');if(c){c.textContent=STAT.combo>=2?'🔥 combo ×'+STAT.combo:'';c.classList.toggle('on',STAT.combo>=2);if(STAT.combo>=2){c.classList.remove('pulse');void c.offsetWidth;c.classList.add('pulse')}}
  var a=document.getElementById('qacc');if(a)a.textContent=STAT.tot?Math.round(STAT.ok/STAT.tot*100)+'%':'—'};
function medal(){var acc=STAT.tot?STAT.ok/STAT.tot:1;return acc>=.9?{k:'gold',ic:'🥇',n:'Medalha de ouro',r:'Dourada'}:acc>=.7?{k:'silver',ic:'🥈',n:'Medalha de prata',r:'Rara'}:{k:'bronze',ic:'🥉',n:'Medalha de bronze',r:'Comum'}}
/* ---------- poggie flutuante com dica ---------- */
function drawHint(p){var el=document.getElementById('qh');if(!el){el=document.createElement('div');el.id='qh';el.className='qh';document.body.appendChild(el)}
  var t=(p&&p.hint)||HINT[p&&p.t]||'';el.innerHTML='<div class="qhp">'+poggie({scarf:'#0C7A78'})+'</div><div class="qhb"><b>Poggie</b>'+H(t)+'</div>';el.style.display=t?'flex':'none';el.classList.remove('hide');clearTimeout(drawHint.t);drawHint.t=setTimeout(function(){el.classList.add('hide')},6000)}
function drawGameBar(p){var bar=document.getElementById('qbar');if(!bar){bar=document.createElement('div');bar.id='qbar';bar.className='qbar';var tl=document.getElementById('tl');tl.parentNode.insertBefore(bar,tl)}
  var L=A.lesson(),med=L.badge||{};bar.innerHTML='<span class="qchip lvl">'+(L.level||'')+' · Lesson '+L.n+'</span><span class="qchip">⭐ XP <b>'+A.xp()+'</b></span><span class="qchip">🎯 <b id="qacc">'+(STAT.tot?Math.round(STAT.ok/STAT.tot*100)+'%':'—')+'</b></span><span class="qchip combo" id="qcombo"></span><span class="qgoal">'+(med.icon||'🏆')+' <b>'+H(med.name||'Badge da missão')+'</b> · '+H(med.desc||'')+'</span>'}

var _U=0;function stg(a,h){if(!a||!a.rs)return '';var bk='';try{bk=window.RS&&RS[a.rs]?RS[a.rs]('pq'+(++_U)):''}catch(e){}
  var cs=(a.chars||[]).map(function(c){var x=c[1]==null?50:c[1];return '<span class="ps-c'+(c[2]?' fl':'')+'" data-c="'+c[0]+'" style="left:'+x+'%;--s:'+(c[3]||1)+'">'+(window.PogChars?PogChars.svg(c[0]):'')+'</span>'}).join('');
  return '<div class="ps-stage '+(h||'strip')+'"><div class="ps-stage-bk">'+bk+'</div><div class="ps-chars">'+cs+'</div>'+(a.over||'')+'</div>'}
var PREV_ONDRAW=null;
function quest(R,API){A=API;var SEC=A.SEC,esc=A.esc,gain=A.gain,mark=A.mark,LS=A.LS,V=A.V;
 SEC.q_cover=['open','Mission briefing'];SEC.q_culture=['read','Cultural spotlight'];SEC.q_read=['listen','Reading quest'];SEC.q_choose=['photo','Choose your reply'];SEC.q_arcade=['game','Practice arcade'];SEC.q_wrap=['review','Mission complete'];
 var S=function(k){return A.key()+'-q-'+k},sv=function(k,v){A.LS.set(S(k),v)},ld=function(k,d){return A.LS.get(S(k),d)};
 function sayBtn(t){return '<button class="say" data-sy="'+H(t)+'" title="Ouvir">🔊</button>'}
 function wire(r){$a(r,'[data-sy]').forEach(function(x){x.onclick=function(e){e.stopPropagation();stop();A.say(x.dataset.sy.replace(/\*\*/g,''))}})}
 function tabs(box,list,draw,start){var cur=start||0;var h='<div class="qtabs">'+list.map(function(t,i){return '<button data-t="'+i+'"><i>'+t.ic+'</i>'+H(t.n)+'</button>'}).join('')+'</div><div class="qview"></div>';box.innerHTML=h;var view=$q(box,'.qview');
  function show(i){cur=i;$a(box,'.qtabs button').forEach(function(b,j){b.classList.toggle('on',j===i)});view.innerHTML='';draw(i,view);wire(view)}
  $a(box,'.qtabs button').forEach(function(b){b.onclick=function(){show(+b.dataset.t)}});show(cur);return show}
 function mcq(box,q,onDone){var ans=q.ans;box.innerHTML='<div class="qq">'+H(q.q||q.s||'')+(q.say?' '+sayBtn(q.say):'')+'</div><div class="opts">'+q.opts.map(function(o,i){return '<button class="opt" data-i="'+i+'">'+H(o)+'</button>'}).join('')+'</div><div class="qfb"></div>';wire(box);
  $a(box,'.opt').forEach(function(b){b.onclick=function(e){var ok=+b.dataset.i===ans;$a(box,'.opt').forEach(function(x){x.disabled=true});b.classList.add(ok?'ok':'bad');if(!ok)$a(box,'.opt')[ans].classList.add('ok');$q(box,'.qfb').innerHTML=(ok?'✅ ':'💡 ')+H(q.why||'');gain(ok?10:0,ok,e);if(onDone)onDone(ok)}})}
 function seq(box,items,drawOne,onEnd){var k=0,okN=0;function go(){if(k>=items.length){box.innerHTML='<div class="qdone">'+okN+' / '+items.length+' ✔</div>';if(onEnd)onEnd(okN);return}var w=document.createElement('div');w.className='qstep';box.innerHTML='<div class="qcount">'+(k+1)+' / '+items.length+'</div>';box.appendChild(w);drawOne(items[k],w,function(ok){if(ok)okN++;var nx=document.createElement('button');nx.className='btn';nx.textContent=k+1<items.length?'Next →':'Finish ✔';nx.onclick=function(){k++;go()};w.appendChild(nx)})}go()}

 /* ===== 1 · Mission briefing ===== */
 R.q_cover=function(p,b){var s=p.situation||{},u=p.unit||{},L=A.lesson(),bd=L.badge||{};b.className='pb c';
  var chaps=(L.plan&&L.plan[A.mode()]||[]).map(function(c,i){return '<div class="qnode" style="--c:'+c.c+'"><span class="qi">'+(c.ic||'')+'</span><b>'+H(c.name)+'</b><small>'+c.min+' min</small></div>'}).join('<span class="qlink"></span>');
  b.innerHTML='<div class="qhero"><div class="qh-l"><div class="rl-kick"><span class="k">Unit '+esc(u.n)+'</span><span class="k o">Lesson '+esc(u.k)+' / '+esc(u.of)+'</span><span class="k o">'+esc(p.level||'')+'</span><span class="k o">60 min</span></div>'+
   '<h1 class="rl-h1">'+esc(p.title)+'</h1>'+(p.pt?'<p class="rl-sub">'+esc(p.pt)+'</p>':'')+
   '<div class="qmission"><b>🎬 Mission</b>'+esc(s.text||'')+'</div>'+
   '<div class="qcando"><b>By the end you can…</b>'+(p.canDo||[]).map(function(g){return '<div><i>✓</i><span>'+esc(g)+'</span></div>'}).join('')+'</div>'+
   '<div class="qrew"><div class="qbadge"><span>'+(bd.icon||'🏆')+'</span><b>'+esc(bd.name||'Mission badge')+'</b><small>'+esc(bd.desc||'Complete the boss mission')+'</small></div><div class="qbadge"><span>🎴</span><b>Collectible sticker</b><small>Unlock it at the end</small></div><div class="qbadge"><span>⭐</span><b>XP + medal</b><small>Bronze · Silver · Gold</small></div></div></div>'+
   '<div class="qh-r"><div class="frame">'+(p.art&&p.art.rs&&window.RS?stg(p.art,'cover'):A.scene(s.scene||'park',s.tod||'day',s.cast||[],'cover'))+'</div>'+(p.think?'<div class="rl-tip" style="margin-top:12px">💭 <span><b>Think about it:</b> '+esc(p.think)+'</span></div>':'')+'</div></div><div class="qmap"><b>Quest map</b><div class="qpath">'+chaps+'</div></div>';mark()};

 /* ===== 3 · Cultural spotlight (aprofundado) ===== */
 R.q_culture=function(p,b){var tabsL=[{ic:'🌍',n:'Fact file'},{ic:'🧐',n:'Myth or fact?'},{ic:'👀',n:'In the wild'},{ic:'🇧🇷',n:'Compare'},{ic:'🎯',n:'Quiz'}];if(p.hot&&p.art)tabsL.unshift({ic:'🔎',n:'Explore the scene'});
  b.innerHTML='<p class="lead" style="margin:0">'+esc(p.hook||'')+'</p><div class="qbox"></div>';
  tabs($q(b,'.qbox'),tabsL,function(i,v){
   if(p.hot&&p.art){if(i===0){var seen={},H0=p.hot;v.innerHTML='<div class="qhs">'+stg(Object.assign({},p.art,{over:H0.map(function(o,k){return '<button type="button" class="ps-hot" data-k="'+k+'" style="left:'+o.x+'%;top:'+o.y+'%" aria-label="'+H(o.en)+'"><span>'+o.e+'</span><i class="ps-ping"></i></button>'}).join('')}),'hot')+'<div class="qhsi" id="qhsi"><b>Tap the glowing objects to hear them.</b></div><div class="qhsc" id="qhsc">0/'+H0.length+' found</div></div>';
     $a(v,'.ps-hot').forEach(function(x){x.onclick=function(){var o=H0[+x.dataset.k];seen[x.dataset.k]=1;x.classList.add('seen');$q(v,'#qhsi').innerHTML='<b>'+H(o.en)+'</b> · '+H(o.pt)+(o.say?'<br><span style="font-weight:700">“'+H(o.say)+'”</span> <small>'+H(o.sayPt||'')+'</small>':'');$q(v,'#qhsc').textContent=Object.keys(seen).length+'/'+H0.length+' found';if(o.say)A.say(o.say);try{A.gain(1,true)}catch(e){}}});return}i--}
   if(i===0){v.innerHTML='<div class="qfacts">'+(p.facts||[]).map(function(f){return '<div class="qfact"><div class="fi">'+(f.vis?V(f.vis):'')+'</div><div class="fb">'+H(f.big||'')+'</div><div class="fl">'+H(f.label||'')+'</div><div class="fs">'+H(f.sub||'')+'</div></div>'}).join('')+'</div>'+(p.polite?'<div class="rl-tip">💬 <span>'+hb(p.polite)+'</span></div>':'')}
   if(i===1){var mf=p.mythfact||[];seq(v,mf,function(it,w,done){w.innerHTML='<div class="qq">“'+H(it.s)+'”</div><div class="rl-bar"><button class="btn" data-a="1">✅ Fact</button><button class="btn" data-a="0" style="background:#d9444f">❌ Myth</button></div><div class="qfb"></div>';$a(w,'[data-a]').forEach(function(bt){bt.onclick=function(e){var ok=(+bt.dataset.a===1)===!!it.ans;$a(w,'[data-a]').forEach(function(x){x.disabled=true});$q(w,'.qfb').innerHTML=(ok?'✅ ':'💡 ')+H(it.why||'');gain(ok?10:0,ok,e);done(ok)}})},function(){mark()})}
   if(i===2){v.innerHTML=(p.wild||[]).map(function(w,k){return '<div class="qwild"><div class="qw-t">'+H(w.kind||'Real life')+'</div><div class="qw-card k-'+H((w.kind||'').toLowerCase().split(' ')[0])+'">'+(w.lines||[]).map(function(l){return '<div>'+hb(l)+'</div>'}).join('')+'</div><div class="qw-q" data-k="'+k+'"></div></div>'}).join('');
    (p.wild||[]).forEach(function(w,k){var box=$q(v,'.qw-q[data-k="'+k+'"]');mcq(box,w.decode,function(){})})}
   if(i===3){var c=p.compare||{};v.innerHTML='<div class="qcmp"><div class="br"><b>🇧🇷 In Brazil</b><p>'+H(c.br||'')+'</p></div><div class="us"><b>🌎 In English-speaking places</b><p>'+H(c.us||'')+'</p></div></div>'+(c.tip?'<div class="rl-tip">💡 <span>'+H(c.tip)+'</span></div>':'')+(c.ask?'<div class="rl-cmp"><b>Your turn:</b> '+H(c.ask)+'</div>':'')}
   if(i===4){seq(v,p.quiz||[],function(it,w,done){mcq(w,it,done)},function(){mark()})}
  });mark()};

 /* ===== 4 · Reading quest (densidade) ===== */
 R.q_read=function(p,b){var gl={};(p.glossary||[]).forEach(function(g){gl[g.w.toLowerCase()]=g.pt});var rate=.9;
  function body(){return (p.text||[]).map(function(par,i){var t=hb(par);Object.keys(gl).sort(function(a,c){return c.length-a.length}).forEach(function(w){t=t.replace(new RegExp('(^|[^A-Za-z>])('+w.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+')(?![A-Za-z])','i'),function(_,pre,m){return pre+'<u class="gw" data-w="'+H(w)+'">'+m+'</u>'})});return '<p data-p="'+i+'">'+t+'</p>'}).join('')}
  var words=(p.text||[]).join(' ').split(/\s+/).length;
  b.innerHTML='<div class="rl-two" style="align-items:start"><div class="qread"><div class="qr-h"><span class="qtag">'+H(p.genre||'Reading')+'</span><b>'+H(p.title||'')+'</b><small>'+words+' words</small></div><div class="qr-b">'+body()+'</div><div class="rl-bar"><button class="btn" id="rp">▶ Listen</button><button class="btn sec" id="rs">🐢 Slow</button><button class="btn sec" id="rx">■</button><span class="lead">Tap the underlined words.</span></div><div class="qgl" id="gl"></div></div><div class="qbox"></div></div>';
  var tl=[{ic:'⚡',n:'Skim'},{ic:'🔎',n:'Scan'},{ic:'✔',n:'True / False'},{ic:'🔢',n:'Order'},{ic:'🧩',n:'In context'},{ic:'💬',n:'Talk about it'}];
  tabs($q(b,'.qbox'),tl,function(i,v){
   if(i===0){mcq(v,p.fast||{q:'What is this text about?',opts:['—','—','—'],ans:0},function(){})}
   if(i===1){v.innerHTML='<p class="lead">Find the information. Look at the text again.</p>'+(p.scan||[]).map(function(q,k){return '<div class="rl-slot"><label>'+H(q.q)+'</label><input data-k="'+k+'" placeholder="…" autocomplete="off"><button class="btn sec" data-c="'+k+'" style="padding:5px 10px">✔</button></div>'}).join('');
    $a(v,'[data-c]').forEach(function(bt){bt.onclick=function(e){var k=+bt.dataset.c,q=p.scan[k],inp=$q(v,'input[data-k="'+k+'"]'),val=norm(inp.value);var ok=val&&[q.ans].concat(q.alt||[]).some(function(a){var n2=norm(a);return n2===val||(val.length>=3&&n2.indexOf(val)>=0)});inp.classList.remove('ok','bad');inp.classList.add(ok?'ok':'bad');if(!ok)inp.placeholder='Answer: '+q.ans;gain(ok?10:0,!!ok,e)}})}
   if(i===2){seq(v,p.tf||[],function(it,w,done){w.innerHTML='<div class="qq">“'+H(it.s)+'”</div><div class="rl-bar"><button class="btn" data-a="1">✅ True</button><button class="btn" data-a="0" style="background:#d9444f">❌ False</button></div><div class="qfb"></div>';$a(w,'[data-a]').forEach(function(bt){bt.onclick=function(e){var ok=(+bt.dataset.a===1)===!!it.ans;$a(w,'[data-a]').forEach(function(x){x.disabled=true});$q(w,'.qfb').innerHTML=(ok?'✅ ':'💡 ')+H(it.why||'');gain(ok?10:0,ok,e);done(ok)}})},function(){mark()})}
   if(i===3){var ev=p.order||[];var sh=A.shuf(ev.map(function(t,k){return {t:t,k:k}}),7),picked=[];v.innerHTML='<p class="lead">Put the events in order. Tap them one by one.</p><div class="qord"></div><div class="qord-r"></div><div class="rl-bar"><button class="btn sec" id="rs2">↺ Reset</button></div>';
    function dr(){var pool=$q(v,'.qord'),res=$q(v,'.qord-r');pool.innerHTML=sh.filter(function(x){return picked.indexOf(x.k)<0}).map(function(x){return '<button class="opt" data-k="'+x.k+'">'+H(x.t)+'</button>'}).join('');res.innerHTML=picked.map(function(k,j){return '<div class="qrow '+(k===j?'ok':'bad')+'"><i>'+(j+1)+'</i>'+H(ev[k])+'</div>'}).join('');
     $a(pool,'.opt').forEach(function(o){o.onclick=function(e){var k=+o.dataset.k;picked.push(k);var ok=k===picked.length-1;gain(ok?10:0,ok,e);if(!ok){picked.pop();o.classList.add('bad');setTimeout(function(){o.classList.remove('bad')},500);return}dr();if(picked.length===ev.length){A.confetti();mark()}}})}
    $q(v,'#rs2').onclick=function(){picked=[];dr()};dr()}
   if(i===4){seq(v,p.ctx||[],function(it,w,done){mcq(w,{q:'In “'+it.sent+'”, “'+it.w+'” means…',opts:it.opts,ans:it.ans,why:it.why},done)},function(){mark()})}
   if(i===5){v.innerHTML='<div class="rl-sit"><b>Talk about it</b>'+H(p.think||'What do you think?')+'</div><div class="chips">'+(p.chunkHunt||[]).map(function(c){return '<button class="cp" data-sy="'+H(c)+'">'+H(c)+'</button>'}).join('')+'</div><p class="lead">Find these chunks in the text and use one in your answer.</p>'}
  });
  $a(b,'.gw').forEach(function(u){u.onclick=function(){var w=u.dataset.w.toLowerCase();$q(b,'#gl').innerHTML='<b>'+H(u.textContent)+'</b> — '+H(gl[w]||'')+' '+sayBtn(u.textContent);wire(b);A.say(u.textContent)}});
  var running=false;$q(b,'#rs').onclick=function(){rate=rate===.9?.7:.9;this.textContent=rate===.9?'🐢 Slow':'🐇 Normal'};$q(b,'#rx').onclick=function(){stop();$a(b,'.qr-b p').forEach(function(x){x.classList.remove('on')})};
  $q(b,'#rp').onclick=async function(){var my=++TOKQ;try{speechSynthesis.cancel()}catch(e){}var ps=$a(b,'.qr-b p');for(var i=0;i<(p.text||[]).length;i++){if(my!==TOKQ)return;ps.forEach(function(x){x.classList.remove('on')});ps[i].classList.add('on');await speak(p.text[i],0,rate)}ps.forEach(function(x){x.classList.remove('on')})};
  mark()};

 /* ===== 7 · Choose your reply (conversa ramificada) ===== */
 R.q_choose=function(p,b){var turns=p.turns||[],k=0,okN=0,log=[];var npc=(p.npc&&p.npc.name)||'Neighbor';var face='';try{face=V('face:'+npc)}catch(e){}
  function go(){if(k>=turns.length){b.innerHTML='<div class="qdone">'+okN+' / '+turns.length+' natural replies ✔</div><div class="qlog">'+log.map(function(l){return '<div>'+H(l)+'</div>'}).join('')+'</div>'+(p.story?'<div class="rl-tip">📖 <span>'+H(p.story)+'</span></div>':'')+'<div class="rl-bar"><button class="btn" id="rep">↺ Play again</button></div>';mark();$q(b,'#rep').onclick=function(){k=0;okN=0;log=[];go()};return}
   var t=turns[k];var order=A.shuf(t.opts.map(function(o,i){return {o:o,i:i}}),k+3);
   b.innerHTML='<div class="qchat"><div class="qcn"><div class="av">'+face+'</div><div class="qbub npc"><div class="wo">'+H(npc)+'</div><div class="en">'+H(t.npc)+' '+sayBtn(t.npc)+'</div><div class="pt">'+H(t.pt||'')+'</div></div></div>'+
    '<div class="qyou">'+order.map(function(x){return '<button class="opt" data-i="'+x.o.i+'">'+H(x.o.en)+'<small>'+H(x.o.pt||'')+'</small></button>'}).join('')+'</div><div class="qfb"></div></div><div class="qcount">Turn '+(k+1)+' / '+turns.length+'</div>';wire(b);A.say(t.npc);
   $a(b,'.qyou .opt').forEach(function(bt){bt.onclick=function(e){var o=t.opts[+bt.dataset.i];$a(b,'.qyou .opt').forEach(function(x){x.disabled=true});bt.classList.add(o.ok?'ok':'bad');if(!o.ok){var good=$a(b,'.qyou .opt').filter(function(x){return t.opts[+x.dataset.i].ok})[0];if(good)good.classList.add('ok')}
     $q(b,'.qfb').innerHTML=(o.ok?'✅ ':'💡 ')+H(o.fb||'');gain(o.ok?15:0,!!o.ok,e);if(o.ok)okN++;log.push(npc+': '+t.npc+' → You: '+(o.en));var nx=document.createElement('button');nx.className='btn';nx.textContent=k+1<turns.length?'Next →':'Finish ✔';nx.onclick=function(){k++;go()};$q(b,'.qchat').appendChild(nx);A.say(o.en)}})}
  b.innerHTML='';go()};

 /* ===== 11 · Practice arcade (mini-jogos) ===== */
 R.q_arcade=function(p,b){var games=[];var g=p.games||{};
  if(g.pairs&&g.pairs.length)games.push({id:'pairs',ic:'🃏',n:'Memory match'});if(g.unscramble&&g.unscramble.length)games.push({id:'uns',ic:'🔀',n:'Unscramble'});if(g.errors&&g.errors.length)games.push({id:'err',ic:'🕵️',n:'Error hunt'});if(g.speed&&g.speed.length)games.push({id:'spd',ic:'⚡',n:'Speed round'});if(g.dict&&g.dict.length)games.push({id:'dic',ic:'🎧',n:'Dictation'});
  var done=ld('arc',{});
  b.innerHTML='<div class="qarc">'+games.map(function(x){return '<button class="qg'+(done[x.id]?' on':'')+'" data-g="'+x.id+'"><span>'+x.ic+'</span><b>'+x.n+'</b><small>'+(done[x.id]?'✔ done':'play')+'</small></button>'}).join('')+'</div><div class="qgv"></div>';
  var view=$q(b,'.qgv');
  function finish(id){done[id]=1;sv('arc',done);var btn=$q(b,'[data-g="'+id+'"]');if(btn){btn.classList.add('on');$q(btn,'small').textContent='✔ done'}if(games.every(function(x){return done[x.id]})){mark();A.confetti()}}
  function play(id){view.innerHTML='';
   if(id==='pairs'){var pr=g.pairs,cards=A.shuf(pr.map(function(x,i){return {t:x.en,i:i,l:'en'}}).concat(pr.map(function(x,i){return {t:x.pt,i:i,l:'pt'}})),11),sel=null,found=0;view.innerHTML='<div class="qmem">'+cards.map(function(c,k){return '<button class="mc" data-k="'+k+'">'+H(c.t)+'</button>'}).join('')+'</div>';
    $a(view,'.mc').forEach(function(bt){bt.onclick=function(e){if(bt.classList.contains('ok'))return;var c=cards[+bt.dataset.k];if(c.l==='en')A.say(c.t);if(!sel){sel=bt;bt.classList.add('sel');return}if(sel===bt){bt.classList.remove('sel');sel=null;return}var c0=cards[+sel.dataset.k];if(c0.i===c.i&&c0.l!==c.l){sel.classList.remove('sel');sel.classList.add('ok');bt.classList.add('ok');found++;gain(8,true,e);sel=null;if(found===pr.length)finish('pairs')}else{gain(0,false,e);bt.classList.add('bad');var s0=sel;setTimeout(function(){bt.classList.remove('bad');s0.classList.remove('sel')},500);sel=null}}})}
   if(id==='uns'){seq(view,g.unscramble,function(it,w,dn){var words=A.shuf(it.words.map(function(t,i){return {t:t,i:i}}),it.words.length+3),picked=[];w.innerHTML='<div class="qq">Put the words in order'+(it.pt?' — <small>'+H(it.pt)+'</small>':'')+'</div><div class="qsent"></div><div class="qpool"></div><div class="qfb"></div>';
    function dr(){$q(w,'.qsent').innerHTML=picked.map(function(x){return '<button class="cp on" data-r="'+x.i+'">'+H(x.t)+'</button>'}).join('')||'<span class="lead">…</span>';$q(w,'.qpool').innerHTML=words.filter(function(x){return !picked.some(function(y){return y.i===x.i})}).map(function(x){return '<button class="cp" data-a="'+x.i+'">'+H(x.t)+'</button>'}).join('');
     $a(w,'.qpool .cp').forEach(function(c){c.onclick=function(){picked.push(words.filter(function(x){return x.i===+c.dataset.a})[0]);dr();if(picked.length===it.words.length){var ok=norm(picked.map(function(x){return x.t}).join(' '))===norm(it.ans||it.words.join(' '));$q(w,'.qfb').innerHTML=ok?'✅ '+H(it.ans||it.words.join(' ')):'💡 '+H(it.ans||it.words.join(' '));gain(ok?12:0,ok,{target:c});if(ok)A.say(it.ans||it.words.join(' '));dn(ok)}}});$a(w,'.qsent .cp').forEach(function(c){c.onclick=function(){picked=picked.filter(function(x){return x.i!==+c.dataset.r});dr()}})}dr()},function(){finish('uns')})}
   if(id==='err'){seq(view,g.errors,function(it,w,dn){var opts=A.shuf([it.fix,it.wrong,it.alt||'—'].filter(function(x,i,a){return a.indexOf(x)===i}),5);mcq(w,{q:'Find the correct sentence.',opts:opts,ans:opts.indexOf(it.fix),why:it.why},dn)},function(){finish('err')})}
   if(id==='spd'){var items=g.speed,k=0,sc=0,left=45,iv=null;view.innerHTML='<div class="rl-bar"><span class="rl-tm" id="stm">0:45</span><button class="btn" id="sgo">▶ Start</button><span class="chip">Score <b id="ssc">0</b></span></div><div class="qsp"></div>';
    var box=$q(view,'.qsp');function q(){if(k>=items.length||left<=0){clearInterval(iv);box.innerHTML='<div class="qdone">'+sc+' / '+items.length+' ⚡</div>';finish('spd');return}mcq(box,items[k],function(ok){if(ok)sc++;$q(view,'#ssc').textContent=sc;setTimeout(function(){k++;q()},700)})}
    $q(view,'#sgo').onclick=function(){this.disabled=true;q();iv=setInterval(function(){left--;var t=$q(view,'#stm');if(t){t.textContent='0:'+String(Math.max(0,left)).padStart(2,'0');t.classList.toggle('low',left<=10)}if(left<=0){clearInterval(iv);box.innerHTML='<div class="qdone">Time! '+sc+' ⚡</div>';finish('spd')}},1000)}}
   if(id==='dic'){seq(view,g.dict,function(it,w,dn){w.innerHTML='<div class="qq">Listen and type what you hear '+sayBtn(it.say)+'</div><div class="rl-in"><input placeholder="Type here…" autocomplete="off"><button class="btn" data-ck="1">Check</button></div><div class="qfb"></div>';wire(w);setTimeout(function(){A.say(it.say)},300);
    $q(w,'[data-ck]').onclick=function(e){var v=norm($q(w,'input').value);if(!v)return;var ok=v===norm(it.say);$q(w,'.qfb').innerHTML=(ok?'✅ ':'💡 ')+H(it.say);gain(ok?12:0,ok,e);dn(ok)}},function(){finish('dic')})}}
  $a(b,'.qg').forEach(function(x){x.onclick=function(){play(x.dataset.g)}});mark()};

 /* ===== 17 · Mission complete: medalha, XP, figurinha e próxima parada ===== */
 R.q_wrap=function(p,b){var L=A.lesson(),m=medal(),bd=L.badge||{},st=L.sticker||{},xp=A.xp();var cast=(L.cast||[]);
  var rec=A.LS.get('pgq-prog',{});rec[L.n]={xp:xp,acc:STAT.tot?Math.round(STAT.ok/STAT.tot*100):100,medal:m.k,at:Date.now()};
  var prev=rec[L.n];A.LS.set('pgq-prog',rec);
  var lad=(A.lesson().pages.filter(function(x){return x.t==='rl_levels'})[0]||{});
  b.innerHTML='<div class="qwrap"><div class="qw-l"><div class="qmedal '+m.k+'"><span>'+m.ic+'</span><b>'+m.n+'</b></div><div class="qstats"><div><b>'+xp+'</b><small>XP</small></div><div><b>'+(STAT.tot?Math.round(STAT.ok/STAT.tot*100)+'%':'—')+'</b><small>accuracy</small></div><div><b>'+STAT.best+'</b><small>best combo</small></div></div>'+
   '<div class="qbadge big"><span>'+(bd.icon||'🏆')+'</span><b>'+H(bd.name||'Mission badge')+'</b><small>'+H(bd.desc||'')+'</small></div>'+
   (p.homework?'<div class="bx soft"><div class="bxh">🎒 Streak mission</div><div class="bxb">'+H(p.homework)+'</div></div>':'')+'</div>'+
   '<div class="qw-r"><div class="qstk '+m.k+'"><div class="qs-h"><span>'+H(st.cat||'Cultural sticker')+'</span><em>Nº '+String(L.n).padStart(3,'0')+'</em></div><div class="frame">'+(st.art&&st.art.rs&&window.RS?stg(st.art,'cover'):A.scene(L.scene||'park',L.tod||'day',cast,'cover'))+'</div><div class="qs-t"><b>'+H(st.title||L.title)+'</b><small>'+H(st.sub||'')+'</small></div><div class="qs-r">'+m.r+'</div></div>'+
   (p.next?'<div class="qnext"><b>🚏 Next stop</b><span>'+H(p.next.title||'')+'</span><small>'+H(p.next.teaser||'')+'</small></div>':'')+'</div></div>';
  A.confetti();mark()};
}
var prevReg=window.RL_REGISTER;window.RL_REGISTER=function(R,API){if(prevReg)prevReg(R,API);quest(R,API)};
function addStrip(p){if(!p||!p.art||!p.art.rs||!window.RS||/^(q_cover|q_wrap)$/.test(p.t))return;var b=document.querySelector('.pg .pb');if(!b||b.querySelector('.qstrip'))return;var d=document.createElement('div');d.className='qstrip';d.innerHTML=stg(p.art,'strip');b.insertBefore(d,b.firstChild)}
var prevDraw=window.RL_ONDRAW;window.RL_ONDRAW=function(p,i,pages){if(prevDraw)prevDraw(p,i,pages);try{drawGameBar(p);drawHint(p);addStrip(p)}catch(e){console.error(e)}};
})();
