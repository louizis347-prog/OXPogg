/* Quest 2 · palco com cenas do curso + pessoas de corpo inteiro (estilo Pocket), história em páginas, mini-diálogo com palavras que trocam, fala com microfone */
(function(){'use strict';
var H=function(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})};
var hb=function(s){return H(s).replace(/\*\*(.+?)\*\*/g,'<b class="hl">$1</b>')};
var $q=function(r,s){return r.querySelector(s)},$a=function(r,s){return Array.prototype.slice.call(r.querySelectorAll(s))};
var A=null,UID=0;
/* ---------- pessoa de corpo inteiro (PogFace.bust + corpo), com papel ---------- */
var TONEM={'\u{1F3FB}':0,'\u{1F3FC}':1,'\u{1F3FD}':2,'\u{1F3FE}':3,'\u{1F3FF}':3};
var SH=['#3b6ea5','#b5543c','#4d8f6b','#7a5fa8','#c58a2f','#2f7f86'];
var ROLE={barista:{apron:'#7a4a2b',prop:'cup',shirt:'#f2efe6'},customer:{},cook:{apron:'#f4f4f4',shirt:'#e8e8e8'},cashier:{apron:'#2f7f86',shirt:'#f2efe6'},teacher:{shirt:'#4d8f6b'},friend:{}};
function person(c){
  var F=window.PogFace;if(!F||!F.bust)return '';var name=c.n||'x';
  var h=7;for(var i=0;i<name.length;i++)h=(h*31+name.charCodeAt(i))>>>0;
  var g=c.g==='f'?'f':'m',R=ROLE[c.role]||{};
  var col=c.shirt||R.shirt||SH[h%SH.length],hair=c.hair||['#4a3228','#2b211c','#7a4a2b','#5b3a29'][h%4];
  var bo={g:g,tone:c.tone!=null?c.tone:h%4,style:(g==='f'?['long','wavy','bob','bun']:['short','side','short','curly'])[(h>>3)%4],hair:hair,shirt:col,seed:h,refined:true,natural:true,rich:2,mood:c.mood||'grin',glasses:!!c.glasses,beard:false};
  var k=.2,by=-17-120*k,pants=c.pants||['#2f3550','#4a3b32','#3b4a63','#35384a'][h%4],pd='#20263a';
  var face='<svg x="'+(-46*k).toFixed(2)+'" y="'+by.toFixed(2)+'" width="'+(92*k).toFixed(2)+'" height="'+(120*k).toFixed(2)+'" viewBox="4 6 92 120" overflow="hidden">'+F.bust(bo)+'</svg>';
  var arm=function(sx,cl){return '<path d="M'+(sx*7.4)+' '+(by+88*k).toFixed(2)+' Q'+(sx*9.3)+' -20 '+(sx*8.7)+' -12.5" stroke="'+cl+'" stroke-width="2.4" fill="none" stroke-linecap="round"/><ellipse cx="'+(sx*8.7)+'" cy="-10.8" rx="1.25" ry="1.6" fill="#e6b896"/>'};
  var apron=R.apron?'<path d="M-4.7 -27.5 L4.7 -27.5 L5.6 -17.2 L-5.6 -17.2Z" fill="'+R.apron+'"/><path d="M-4 -27.5 L-2.2 -31 M4 -27.5 L2.2 -31" stroke="'+R.apron+'" stroke-width=".7"/>':'';
  var prop=(c.prop||R.prop)==='cup'?'<g transform="translate(9.6 -13)"><path d="M-1.9 -1.6 L1.9 -1.6 L1.4 2.4 L-1.4 2.4Z" fill="#f6f1e6" stroke="#bda98a" stroke-width=".25"/><rect x="-2.1" y="-2.1" width="4.2" height=".8" fill="#7a4a2b"/></g>':(c.prop==='bag'?'<g transform="translate(9.4 -12)"><rect x="-2.4" y="-2" width="4.8" height="5" rx=".6" fill="#c58a2f"/><path d="M-1.4 -2 Q0 -4 1.4 -2" stroke="#8a5f1e" fill="none" stroke-width=".4"/></g>':'');
  return '<svg class="qp-fig" viewBox="-14 -48 28 50" preserveAspectRatio="xMidYMax meet" aria-hidden="true"><ellipse cx="0" cy=".2" rx="11" ry="1.9" fill="#000" fill-opacity=".3"/>'+
   '<path d="M-6.2 -17.5 L-5.6 -2.4 L-.6 -2.4 L-.4 -17.5Z" fill="'+pants+'"/><path d="M.4 -17.5 L.6 -2.4 L5.6 -2.4 L6.2 -17.5Z" fill="'+pd+'"/>'+
   '<path d="M-6.4 -3 Q-3.4 -4.4 -.5 -3 L-.5 -1.2 L-6.8 -1.2Z M.5 -3 Q3.4 -4.4 6.4 -3 L6.8 -1.2 L.5 -1.2Z" fill="#15151c"/>'+face+arm(-1,col)+arm(1,'#00000033')+apron+prop+'</svg>'}
/* ---------- palco: cenário pintado do curso (RS) + personagens (PogChars) + pessoas (cast) ---------- */
function stage(a,h){if(!a||!a.rs)return '';var bk='';try{bk=window.RS&&RS[a.rs]?RS[a.rs]('pq'+(++UID)):''}catch(e){}
  var cs=(a.chars||[]).map(function(c){var x=c[1]==null?50:c[1];return '<span class="ps-c'+(c[2]?' fl':'')+'" data-c="'+c[0]+'" style="left:'+x+'%;--s:'+(c[3]||1)+'">'+(window.PogChars?PogChars.svg(c[0]):'')+'</span>'}).join('');
  var pp=(a.cast||[]).map(function(c){return '<span class="qp'+(c.flip?' fl':'')+'" style="left:'+(c.x==null?50:c.x)+'%;--s:'+(c.s||1)+'">'+person(c)+'</span>'}).join('');
  return '<div class="ps-stage '+(h||'strip')+'"><div class="ps-stage-bk">'+bk+'</div><div class="ps-chars">'+cs+pp+'</div>'+(a.over||'')+'</div>'}
window.QSTAGE=stage;
/* ---------- util ---------- */
function toast(t){var el=document.createElement('div');el.className='qtoast';el.textContent=t;document.body.appendChild(el);setTimeout(function(){el.classList.add('out')},1800);setTimeout(function(){el.remove()},2300)}
/* "{a|b|c}" nas falas: palavras que trocam ao toque; pt acompanha pelo mesmo índice */
function parseSw(en,pt){var re=/\{([^{}]+)\}/g,out=[],ptp=(pt||'').split(/\{([^{}]+)\}/),m,last=0,i=0;en=en||'';var enp=en.split(/\{([^{}]+)\}/);
  for(var k=0;k<enp.length;k++){if(k%2===0)out.push({t:enp[k],p:ptp[k]!=null?ptp[k]:''});else out.push({sw:enp[k].split('|'),pw:(ptp[k]||'').split('|'),i:0})}return out}
function lineHtml(parts,li){return parts.map(function(p,k){if(p.t!=null)return hb(p.t);return '<button type="button" class="qsw" data-l="'+li+'" data-k="'+k+'">'+H(p.sw[p.i])+'</button>'}).join('')}
function lineText(parts){return parts.map(function(p){return p.t!=null?p.t:p.sw[p.i]}).join('').replace(/\*\*/g,'')}
function linePt(parts){return parts.map(function(p){return p.t!=null?p.p:(p.pw[p.i]||p.pw[0]||'')}).join('')}
function ptOnly(en,pt){var e=parseSw(en,pt);return e}
function swapBox(host,lines,cfg){ /* lines:[{who,en,pt}] ; cfg:{faces, onAll} */
  var P=lines.map(function(l){var parts=parseSw(l.en,l.pt);return{who:l.who,parts:parts,ptParts:parseSw(l.pt||'',l.pt||''),raw:l}});
  var touched={},total=0;P.forEach(function(l){l.parts.forEach(function(p){if(p.sw)total++})});
  var showPt=false;
  function draw(){host.innerHTML=P.map(function(l,i){return '<div class="qd-ln '+(l.who===cfg.me?'b':'')+'" data-i="'+i+'"><div class="av">'+(cfg.face?cfg.face(l.who):'')+'</div><div class="tb"><div class="wo">'+H(l.who)+'</div><div class="en">'+lineHtml(l.parts,i)+'</div><div class="pt" '+(showPt?'':'hidden')+'>'+H(linePt(l.parts))+'</div></div><button class="say" data-sy="'+i+'" title="Ouvir">🔊</button></div>'}).join('');
    $a(host,'.qsw').forEach(function(b){b.onclick=function(e){var l=P[+b.dataset.l],p=l.parts[+b.dataset.k];p.i=(p.i+1)%p.sw.length;var key=b.dataset.l+'-'+b.dataset.k;if(!touched[key]){touched[key]=1;try{A.gain(5,true,e)}catch(x){}if(cfg.onProgress)cfg.onProgress(Object.keys(touched).length,total)}draw();say(lineText(l.parts))}});
    $a(host,'[data-sy]').forEach(function(b){b.onclick=function(){say(lineText(P[+b.dataset.sy].parts))}})}
  function say(t){try{A.say(t)}catch(e){}}
  draw();
  return{pt:function(on){showPt=on;draw()},shuffle:function(){P.forEach(function(l){l.parts.forEach(function(p){if(p.sw)p.i=Math.floor(Math.random()*p.sw.length)})});draw()},
   play:async function(){var my=++PLAYTOK;for(var i=0;i<P.length;i++){if(my!==PLAYTOK)return;$a(host,'.qd-ln').forEach(function(x,j){x.classList.toggle('on',j===i)});await A.sayP(lineText(P[i].parts))}$a(host,'.qd-ln').forEach(function(x){x.classList.remove('on')})},
   stop:function(){PLAYTOK++;try{speechSynthesis.cancel()}catch(e){}},total:total}}
var PLAYTOK=0;
function mcq(box,it,done){box.innerHTML='<div class="qq">'+H(it.q)+'</div><div class="qopts">'+it.opts.map(function(o,i){return '<button class="opt" data-i="'+i+'">'+H(o)+'</button>'}).join('')+'</div><div class="qfb"></div>';
  $a(box,'.opt').forEach(function(b){b.onclick=function(e){var ok=+b.dataset.i===it.ans;try{A.gain(ok?10:0,ok,e)}catch(x){}b.classList.add(ok?'ok':'bad');$q(box,'.qfb').innerHTML=(ok?'✅ ':'❌ ')+H(it.why||'');if(ok){$a(box,'.opt').forEach(function(x){x.disabled=true});setTimeout(function(){done&&done()},900)}else setTimeout(function(){b.classList.remove('bad')},500)}})}
function seq(box,items,done){var k=0;(function nx(){if(k>=items.length){done&&done();return}var w=document.createElement('div');w.className='qmc';box.innerHTML='';box.appendChild(w);var it=items[k];var n=document.createElement('div');n.className='qn';n.textContent=(k+1)+'/'+items.length;w.appendChild(n);var m=document.createElement('div');w.appendChild(m);mcq(m,it,function(){k++;nx()})})()}
function faceFor(name,face){try{return A.V('face:'+(face&&face[name]||name))}catch(e){return ''}}

function q2(R,API){A=API;var SEC=A.SEC;
 SEC.q_story=['listen','Story time'];SEC.q_phrase=['photo','Situation & phrase'];SEC.q_dialog=['photo','Dialogue'];SEC.q_say=['speak','Say it'];SEC.q_mold=['gram','Word mold'];SEC.q_sound=['pron','Sound lab'];SEC.q_role=['speak','Boss mission'];SEC.q_free=['write','Free production'];
 /* ===== História em páginas: o cenário muda a cada passo ===== */
 R.q_story=function(p,b){var steps=p.steps||[],k=0,pt=false;
  b.innerHTML='<div class="qsty"><div class="qsty-st" id="sst"></div><div class="qsty-cap"><div class="qsty-tx" id="stx"></div><div class="qsty-bar"><button class="btn sec" id="spt">PT</button><button class="btn sec" id="sli">🔊 Listen</button><span class="qdots" id="sdt"></span><button class="btn sec" id="spv">‹</button><button class="btn" id="snx">Next ›</button></div></div></div>';
  function show(i){k=i;var s=steps[i],box=$q(b,'#sst');box.classList.remove('in');box.innerHTML=stage(s.art,'scene');void box.offsetWidth;box.classList.add('in');
   $q(b,'#stx').innerHTML='<p>'+hb(s.en)+'</p>'+(pt?'<small>'+H(s.pt||'')+'</small>':'');
   $q(b,'#sdt').innerHTML=steps.map(function(_,j){return '<i class="'+(j===i?'on':j<i?'dn':'')+'"></i>'}).join('');
   $q(b,'#spv').disabled=i===0;$q(b,'#snx').textContent=i===steps.length-1?'Finish ✓':'Next ›';try{A.say(s.en.replace(/\*\*/g,''))}catch(e){}}
  $q(b,'#spt').onclick=function(){pt=!pt;show(k)};$q(b,'#sli').onclick=function(){try{A.say(steps[k].en.replace(/\*\*/g,''))}catch(e){}};
  $q(b,'#spv').onclick=function(){if(k>0)show(k-1)};$q(b,'#snx').onclick=function(e){if(k<steps.length-1)show(k+1);else{try{A.gain(15,true,e);A.confetti()}catch(x){}A.mark();toast('📖 Story complete!')}};
  if(steps.length===1){$q(b,'#spv').style.display='none';$q(b,'#snx').style.display='none';$q(b,'#sdt').style.display='none';A.mark()}show(0)};
 /* ===== Situação + molde: contexto + mini-diálogo de 4 falas com palavras que trocam ===== */
 R.q_phrase=function(p,b){var ex=p.expr||{};
  b.innerHTML='<div class="qph"><div class="qph-l">'+stage(p.art,'scene')+'<div class="qph-ctx"><div class="qph-chip"><button class="say" data-sy="'+H(ex.en||'')+'">🔊</button><b>'+H(ex.en||'')+'</b><span>'+H(ex.pt||'')+'</span></div><p>'+H(ex.note||'')+'</p></div></div><div class="qph-r"><h3 class="qph-h">'+H(p.hint2||'Tap the colored words — they change!')+'</h3><div class="qd-box" id="qdb"></div><div class="rl-bar"><button class="btn" id="qpl">▶ Play</button><button class="btn sec" id="qsh">🔀 Shuffle words</button><button class="btn sec" id="qpt">PT</button></div><div class="qph-prog" id="qpg"></div></div></div>';
  var done=false,box=swapBox($q(b,'#qdb'),p.lines||[],{me:p.me,face:function(w){return faceFor(w,p.faces)},onProgress:function(n,t){$q(b,'#qpg').innerHTML='🎨 <b>'+n+'/'+t+'</b> words explored';if(n>=t&&!done){done=true;try{A.confetti()}catch(e){}A.mark();toast('✨ You explored every word!')}}});
  $q(b,'#qpg').innerHTML='🎨 <b>0/'+box.total+'</b> words explored';
  var pton=false;$q(b,'#qpt').onclick=function(){pton=!pton;box.pt(pton)};$q(b,'#qsh').onclick=function(){box.shuffle()};$q(b,'#qpl').onclick=function(){box.play()};
  $q(b,'[data-sy="'+H(ex.en||'')+'"]').onclick=function(){try{A.say(ex.en)}catch(e){}}};
 /* ===== Diálogo com cena e palavras que trocam + compreensão ===== */
 R.q_dialog=function(p,b){
  if(p.qonly){b.innerHTML='<div class="qph"><div class="qph-l">'+stage(p.art,'scene')+'</div><div class="qph-r"><div class="qph-h">Check your understanding</div><div class="qph-q" id="qq"></div></div></div>';seq($q(b,'#qq'),p.qs||[],function(){A.mark()});return}
  b.innerHTML='<div class="qph"><div class="qph-l">'+stage(p.art,'scene')+'<div class="qph-q" id="qq"></div></div><div class="qph-r"><h3 class="qph-h">Tap a colored word to hear new vocabulary</h3><div class="qd-box" id="qdb"></div><div class="rl-bar"><button class="btn" id="qpl">▶ Play</button><button class="btn sec" id="qst">■</button><button class="btn sec" id="qsh">🔀 Shuffle</button><button class="btn sec" id="qpt">PT</button></div></div></div>';
  var box=swapBox($q(b,'#qdb'),p.lines||[],{me:p.me,face:function(w){return faceFor(w,p.faces)}});
  var pton=false;$q(b,'#qpt').onclick=function(){pton=!pton;box.pt(pton)};$q(b,'#qsh').onclick=function(){box.shuffle()};$q(b,'#qpl').onclick=function(){box.play()};$q(b,'#qst').onclick=function(){box.stop()};
  if(!(p.qs||[]).length){$q(b,'#qq').style.display='none';A.mark()}else seq($q(b,'#qq'),p.qs,function(){A.mark()})};
 /* ===== Toque, ouça e diga uma frase sua com cada palavra (microfone) ===== */
 R.q_say=function(p,b){var items=p.items||[],okN=0;
  b.innerHTML='<div class="qsay"><div class="qsay-l">'+stage(p.art,'scene')+'<p class="qsay-help">'+H(p.help||'Tap a word, listen, then say your own sentence with it.')+'</p><div class="qsay-pg" id="qsg">0/'+items.length+'</div></div><div class="qsay-r" id="qsr"></div></div>';
  var sup=!!(window.PogVoice&&PogVoice.supported&&PogVoice.supported());
  var r=$q(b,'#qsr');r.innerHTML=items.map(function(it,i){return '<div class="qsw-c" data-i="'+i+'"><button class="qsw-w" data-w="'+i+'"><span class="qsw-v">'+(it.vis?A.V(it.vis):(it.e||''))+'</span><b>'+H(it.w)+'</b><small>'+H(it.pt||'')+'</small></button><div class="qsw-a"><div class="qsw-mic" data-m="'+i+'"></div>'+(sup?'':'<input class="qsw-in" data-t="'+i+'" placeholder="Type your sentence…"><button class="btn sec" data-ok="'+i+'">✓</button>')+'<div class="qsw-fb" data-f="'+i+'">'+(it.ex?'<em>e.g. “'+H(it.ex)+'”</em>':'')+'</div></div></div>'}).join('');
  function check(i,text,e){var it=items[i],t=String(text||'').toLowerCase(),n=t.split(/\s+/).filter(Boolean).length,hit=t.indexOf(String(it.w).toLowerCase())>=0;var fb=$q(r,'[data-f="'+i+'"]'),card=$q(r,'.qsw-c[data-i="'+i+'"]');
   if(hit&&n>=3){if(!card.classList.contains('ok')){card.classList.add('ok');okN++;try{A.gain(15,true,e)}catch(x){}toast('🎤 Great sentence!');$q(b,'#qsg').textContent=okN+'/'+items.length;if(okN>=items.length){try{A.confetti()}catch(x){}A.mark()}}fb.innerHTML='✅ “'+H(text)+'”'}
   else fb.innerHTML='🔁 '+(hit?'Say a full sentence (3+ words).':'Use the word “'+H(it.w)+'” in your sentence.')+(text?' <small>I heard: “'+H(text)+'”</small>':'')}
  $a(r,'[data-w]').forEach(function(bt){bt.onclick=function(){try{A.say(items[+bt.dataset.w].w)}catch(e){}}});
  if(sup)$a(r,'[data-m]').forEach(function(host){var i=+host.dataset.m;host.innerHTML='<button type="button" class="qmic" aria-label="Speak">🎤 <span>Say it</span><i class="qwv"><b></b><b></b><b></b><b></b></i></button>';var mb=$q(host,'.qmic'),h=null;
   mb.onclick=function(e){if(h){h.stop();h=null;mb.classList.remove('on');return}try{speechSynthesis.cancel()}catch(x){}mb.classList.add('on');
    h=PogVoice.listen({lang:'en-US',onInterim:function(t){$q(r,'[data-f="'+i+'"]').textContent='“'+t+'”'},onDone:function(res){h=null;mb.classList.remove('on');if(res.error){$q(r,'[data-f="'+i+'"]').textContent=res.error==='not-allowed'?'🎙️ Allow the microphone in your browser.':'🔁 I did not hear anything. Try again.';return}check(i,(res.alts||[''])[0],e);(res.alts||[]).slice(1).some(function(a){var ok=a.toLowerCase().indexOf(String(items[i].w).toLowerCase())>=0&&a.split(/\s+/).length>=3;if(ok&&!$q(r,'.qsw-c[data-i="'+i+'"]').classList.contains('ok'))check(i,a,e);return ok})}})}});
  else $a(r,'[data-ok]').forEach(function(bt){bt.onclick=function(e){var i=+bt.dataset.ok;check(i,$q(r,'[data-t="'+i+'"]').value,e)}})};
 /* ===== Molde que muda (moderno): cena + frase com espaços; toque nas opções, ouça, fale ===== */
 R.q_mold=function(p,b){var fr=p.frames||[],cur=0,sel={},used={},gm=0;
  b.innerHTML='<div class="qph"><div class="qph-l">'+stage(p.art,'scene')+'<div class="qph-ctx"><p><b>'+H(p.intro||'Build real sentences. Pick the pieces, listen, then say them!')+'</b></p></div></div><div class="qph-r"><div class="qtabs" id="mt"></div><div class="qml" id="ml"></div><div class="qml-say" id="mv"></div><div class="qph-prog" id="mp"></div></div></div>';
  function sentence(f){var en=f.frame,pt=f.tpt||'';f.slots.forEach(function(sl){var o=sl.opts[sel[sl.k]||0];en=en.replace('{'+sl.k+'}','\u0001'+sl.k+'\u0002'+o.en+'\u0003');pt=pt.replace('{'+sl.k+'}',o.pt)});return{en:en,pt:pt}}
  function plain(t){return t.replace(/[\u0001\u0002\u0003]/g,'').replace(/[a-z0-9_]+(?=[A-Za-z’'])/,function(m){return m})}
  function draw(){var f=fr[cur];$q(b,'#mt').innerHTML=fr.length<2?'':fr.map(function(x,i){return '<button class="'+(i===cur?'on':'')+'" data-t="'+i+'">'+H(x.title)+'</button>'}).join('');
   f.slots.forEach(function(sl){if(sel[sl.k]==null)sel[sl.k]=0});
   var sent=f.frame,disp=f.frame;f.slots.forEach(function(sl){disp=disp.replace('{'+sl.k+'}','<mark class="qmk" data-s="'+sl.k+'">'+H(sl.opts[sel[sl.k]].en)+'</mark>')});
   var spoken=f.frame,ptx=f.tpt||'';f.slots.forEach(function(sl){spoken=spoken.replace('{'+sl.k+'}',sl.opts[sel[sl.k]].en);ptx=ptx.replace('{'+sl.k+'}',sl.opts[sel[sl.k]].pt)});
   $q(b,'#ml').innerHTML='<div class="qml-s">'+disp+'</div><div class="qml-p">'+H(ptx)+'</div>'+f.slots.map(function(sl){return '<div class="qml-r"><label>'+H(sl.label)+'</label><div class="chips">'+sl.opts.map(function(o,i){return '<button class="cp'+(sel[sl.k]===i?' on':'')+'" data-k="'+sl.k+'" data-i="'+i+'">'+(o.e?o.e+' ':'')+H(o.en)+'</button>'}).join('')+'</div></div>'}).join('')+'<div class="rl-bar"><button class="btn" id="msay">🔊 Listen</button><button class="btn sec" id="mshuf">🔀 Surprise me</button></div>';
   $q(b,'#mv').innerHTML='';try{if(window.PogVoice)PogVoice.mount($q(b,'#mv'),{target:spoken,lang:'en-US',onDone:function(r){if(r.score>=70){try{A.gain(15,true)}catch(e){}toast('🎤 '+r.score+'% — nice!')}}})}catch(e){}
   $a(b,'#mt button').forEach(function(x){x.onclick=function(){cur=+x.dataset.t;draw()}});
   $a(b,'#ml .cp').forEach(function(x){x.onclick=function(e){sel[x.dataset.k]=+x.dataset.i;var key=cur+x.dataset.k+x.dataset.i;if(!used[key]){used[key]=1;try{A.gain(5,true,e)}catch(z){}}draw();var f2=fr[cur],sp=f2.frame;f2.slots.forEach(function(sl){sp=sp.replace('{'+sl.k+'}',sl.opts[sel[sl.k]].en)});try{A.say(sp)}catch(z){}$q(b,'#mp').innerHTML='🎨 <b>'+Object.keys(used).length+'</b> combinations tried';if(Object.keys(used).length>=8)A.mark()}});
   $q(b,'#msay').onclick=function(){try{A.say(spoken)}catch(e){}};
   $q(b,'#mshuf').onclick=function(){f.slots.forEach(function(sl){sel[sl.k]=Math.floor(Math.random()*sl.opts.length)});draw();var sp=f.frame;f.slots.forEach(function(sl){sp=sp.replace('{'+sl.k+'}',sl.opts[sel[sl.k]].en)});try{A.say(sp)}catch(e){}}}
  draw()};
 /* ===== Laboratório de sons (moderno): ritmo/ligação + microfone com nota por palavra ===== */
 R.q_sound=function(p,b){var items=p.items||[],cur=0,ide=p.identify||[];
  b.innerHTML='<div class="qph"><div class="qph-l">'+stage(p.art,'scene')+'<div class="qph-ctx"><div class="qph-chip"><b>'+H(p.focus||'')+'</b></div><p>'+H(p.tip||'')+'</p></div></div><div class="qph-r"><div class="qtabs" id="st"><button class="on" data-v="0">🎧 Listen & copy</button><button data-v="1">👂 Which do you hear?</button></div><div id="sv"></div></div></div>';
  function v0(){var it=items[cur];$q(b,'#sv').innerHTML='<div class="qsn-nav">'+items.map(function(_,i){return '<button class="cp'+(i===cur?' on':'')+'" data-i="'+i+'">'+(i+1)+'</button>'}).join('')+'</div><div class="qsn-c"><div class="qsn-t">'+H(it.say)+'</div><div class="qsn-l">'+H(it.linked||'')+'</div><p>'+H(it.note||'')+'</p><div class="rl-bar"><button class="btn" id="sn">🔊 Normal</button><button class="btn sec" id="ss">🐢 Slow</button></div><div id="smic"></div></div>';
   $a(b,'.qsn-nav .cp').forEach(function(x){x.onclick=function(){cur=+x.dataset.i;v0()}});$q(b,'#sn').onclick=function(){A.say(it.say)};$q(b,'#ss').onclick=function(){A.say(it.say,.6)};
   try{if(window.PogVoice)PogVoice.mount($q(b,'#smic'),{target:it.say,lang:'en-US',onDone:function(r){if(r.score>=70){try{A.gain(15,true)}catch(e){}toast('🎤 '+r.score+'%')}}})}catch(e){}}
  function v1(){$q(b,'#sv').innerHTML='';seq($q(b,'#sv'),ide.map(function(x){return {q:'🎧 Press play, then choose: '+x.q,opts:x.opts,ans:x.ans,why:'You heard: “'+x.say+'”',say:x.say}}),function(){A.mark()});$a(b,'#sv .qmc').forEach(function(){});
   var pl=document.createElement('div');pl.className='rl-bar';pl.innerHTML='<button class="btn" id="spl">🔊 Play sound</button>';$q(b,'#sv').insertBefore(pl,$q(b,'#sv').firstChild);var k=0;$q(b,'#spl').onclick=function(){var n=$q(b,'#sv .qn');var i=n?(+n.textContent.split('/')[0]-1):0;A.say((ide[i]||ide[0]).say)};setTimeout(function(){try{A.say(ide[0].say)}catch(e){}},300)}
  if(!items.length||!ide.length)$q(b,'#st').style.display='none';
  $a(b,'#st button').forEach(function(x){x.onclick=function(){$a(b,'#st button').forEach(function(y){y.classList.toggle('on',y===x)});+x.dataset.v?v1():v0()}});(items.length?v0:v1)();A.mark()};
 /* ===== Roleplay dinâmico: escolha entre respostas que fazem sentido e o mini-diálogo é montado ===== */
 R.q_role=function(p,b){var turns=p.turns||[],k=0,log=[];
  b.innerHTML='<div class="qph"><div class="qph-l">'+stage(p.art,'scene')+'<div class="qph-ctx"><p><b>'+H(p.scenario||'')+'</b></p></div></div><div class="qph-r"><div class="qrl" id="rl"></div><div id="ro"></div></div></div>';
  function bub(who,en,pt,me){return '<div class="qd-ln '+(me?'b':'')+'"><div class="av">'+faceFor(who,p.faces)+'</div><div class="tb"><div class="wo">'+H(who)+'</div><div class="en">'+hb(en)+'</div><div class="pt">'+H(pt||'')+'</div></div><button class="say" data-sy="'+H(en.replace(/\*\*/g,''))+'">🔊</button></div>'}
  function draw(){var h=log.map(function(x){return bub(x.who,x.en,x.pt,x.me)}).join('');$q(b,'#rl').innerHTML=h;$a(b,'#rl [data-sy]').forEach(function(x){x.onclick=function(){A.say(x.dataset.sy)}});var box=$q(b,'#ro');
   if(k>=turns.length){box.innerHTML='<div class="qph-ctx"><b>🎉 Your own version of the conversation!</b><p>Play it, or start again with different choices.</p></div><div class="rl-bar"><button class="btn" id="rpl">▶ Play all</button><button class="btn sec" id="rre">↺ Try different choices</button></div>';try{A.confetti();A.gain(20,true)}catch(e){}A.mark();$q(b,'#rpl').onclick=async function(){for(var i=0;i<log.length;i++){await A.sayP(log[i].en.replace(/\*\*/g,''))}};$q(b,'#rre').onclick=function(){k=0;log=[];start()};return}
   var t=turns[k];box.innerHTML='<div class="qq">Your turn — choose what you want to say:</div><div class="qopts">'+t.opts.map(function(o,i){return '<button class="opt" data-i="'+i+'">'+H(o.en)+'<small>'+H(o.pt||'')+'</small></button>'}).join('')+'</div>';
   $a(box,'.opt').forEach(function(x){x.onclick=function(e){var o=t.opts[+x.dataset.i];log.push({who:p.me,en:o.en,pt:o.pt,me:true});try{A.gain(10,true,e);A.say(o.en)}catch(z){}if(o.reply){log.push({who:p.npc,en:o.reply,pt:o.rpt});k++;if(k<turns.length&&turns[k].lead)log[log.length-1].en+=' '+turns[k].lead;draw();setTimeout(function(){try{A.say(log[log.length-1].en)}catch(z){}},500)}else{k++;draw()}}})}
  function start(){log=[{who:p.npc,en:turns[0].npc,pt:turns[0].pt}];draw();setTimeout(function(){try{A.say(turns[0].npc)}catch(z){}},400)}
  start()};
 /* ===== Produção livre (moderna): fale ou escreva, receba feedback do que usou ===== */
 R.q_free=function(p,b){var tg=p.targets||[],mic=!!(window.PogVoice&&PogVoice.supported&&PogVoice.supported());
  b.innerHTML='<div class="qph"><div class="qph-l">'+stage(p.art,'scene')+'<div class="qph-q"><b>'+H(p.prompt||'')+'</b><div class="chips" style="margin-top:8px">'+(p.chips||[]).map(function(c){return '<button class="cp" data-sy="'+H(c)+'">'+H(c)+'</button>'}).join('')+'</div></div></div><div class="qph-r"><div class="qfree-in"><textarea id="fx" placeholder="Speak with the microphone or write here…"></textarea><div class="rl-bar">'+(mic?'<button class="qmic" id="fmic">🎤 <span>Speak</span><i class="qwv"><b></b><b></b><b></b><b></b></i></button>':'')+'<button class="btn" id="fck">✓ Check</button><button class="btn sec" id="fmd">👀 See a model</button></div></div><div class="qfree-fb" id="ff"></div></div></div>';
  var h=null;function check(e){var t=$q(b,'#fx').value.toLowerCase();var n=t.split(/\s+/).filter(Boolean).length;var hit=tg.filter(function(x){return t.indexOf(x.toLowerCase())>=0});var stars=Math.min(3,(n>=12?1:0)+(hit.length>=2?1:0)+(hit.length>=4||n>=18?1:0));
   $q(b,'#ff').innerHTML='<div class="qfree-st">'+'★'.repeat(stars)+'☆'.repeat(3-stars)+'</div><p>'+(n<3?'Say or write at least one full sentence.':'You used <b>'+hit.length+'</b> useful expression'+(hit.length===1?'':'s')+(hit.length?': '+hit.map(function(x){return '<mark>'+H(x)+'</mark>'}).join(', '):'')+'.')+'</p><p style="color:#566">'+(hit.length<2?'Try adding: '+tg.filter(function(x){return hit.indexOf(x)<0}).slice(0,3).map(H).join(' · '):'Great! Now make it longer with one more detail.')+'</p>';
   if(n>=3&&stars>=1){try{A.gain(10+stars*10,true,e)}catch(z){}if(stars>=2){try{A.confetti()}catch(z){}A.mark();toast('⭐ Nice work!')}}}
  $q(b,'#fck').onclick=check;$q(b,'#fmd').onclick=function(){$q(b,'#ff').innerHTML='<div class="qph-ctx"><b>Model answer</b><p>'+hb(p.model||'')+' <button class="say" data-sy="'+H((p.model||'').replace(/\*\*/g,''))+'">🔊</button></p></div>';$q(b,'#ff .say').onclick=function(){A.say((p.model||'').replace(/\*\*/g,''))}};
  if(mic){var mb=$q(b,'#fmic');mb.onclick=function(e){if(h){h.stop();h=null;mb.classList.remove('on');return}mb.classList.add('on');h=PogVoice.listen({lang:'en-US',maxMs:15000,onInterim:function(t){$q(b,'#fx').value=t},onDone:function(r){h=null;mb.classList.remove('on');if(r.error){$q(b,'#ff').innerHTML='<p>'+(r.error==='not-allowed'?'🎙️ Allow the microphone in your browser.':'🔁 I did not hear anything. Try again.')+'</p>';return}$q(b,'#fx').value=(r.alts||[''])[0];check(e)}})}}
  $a(b,'[data-sy]').forEach(function(x){x.onclick=function(){A.say(x.dataset.sy)}})};

}

/* ---------- ajuste automático: o quadro nunca rola (cena encolhe, depois espaçamento compacto) ---------- */
function fit(){var st=document.getElementById('stage');if(!st)return;var pg0=st.querySelector('.pg');if(pg0)pg0.style.animation='none';var steps=document.fullscreenElement?[46,40,34,30,26,22,18,15,12,9]:[38,34,30,26,22,18,15,12,9];
  document.body.classList.remove('qtight','qtight2');
  function over(){return st.scrollHeight-st.clientHeight>2}
  var i=0;st.style.setProperty('--qh',steps[0]);
  for(i=0;i<steps.length&&over();i++){st.style.setProperty('--qh',steps[i])}
  if(over()){document.body.classList.add('qtight');for(i=0;i<steps.length&&over();i++){st.style.setProperty('--qh',steps[i])}}
  if(over()){document.body.classList.add('qtight2');for(i=0;i<steps.length&&over();i++){st.style.setProperty('--qh',steps[i])}}
  st.scrollTop=0}

/* ---------- barra de partes + XP: minimizada no topo, aparece ao passar o mouse ---------- */
function dockTop(){var tl=document.getElementById('tl');if(!tl)return;var top=document.getElementById('qtop');
  if(!top){top=document.createElement('div');top.id='qtop';top.innerHTML='<div class="qtop-in" id="qtin"></div><button type="button" class="qtop-h" id="qth" aria-label="Mapa da aula">▾ Mapa da aula · XP</button>';document.body.appendChild(top);
    $q(top,'#qth').onclick=function(){top.classList.toggle('open')};document.addEventListener('click',function(e){if(top.classList.contains('open')&&!top.contains(e.target))top.classList.remove('open')})}
  var inn=$q(top,'#qtin'),bar=document.getElementById('qbar');if(bar&&bar.parentNode!==inn)inn.appendChild(bar);if(tl.parentNode!==inn)inn.appendChild(tl)}
document.addEventListener('fullscreenchange',function(){try{document.body.classList.toggle('qfs',!!document.fullscreenElement);fit();setTimeout(fit,200)}catch(e){}});
window.QFIT=fit;
var prevD=window.RL_ONDRAW;window.RL_ONDRAW=function(p,i,pg){if(prevD)prevD(p,i,pg);try{dockTop();fit();setTimeout(fit,120);setTimeout(fit,500)}catch(e){console.error(e)}};
var prev=window.RL_REGISTER;window.RL_REGISTER=function(R,API){if(prev)prev(R,API);q2(R,API)};
})();
