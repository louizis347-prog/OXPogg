/* Pogglot · Paradas Culturais
   Episódio especial de 5 páginas: 1 Leia · 2 Ouça · 3 Repita (fala) · 4 Converse (fala) · 5 Desafio (ler + ouvir + falar).
   Usa o mesmo reconhecimento de voz (PogVoice) dos primeiros episódios. Dados: episódios com `sp:1` e quadros sp_read, sp_listen, sp_repeat, sp_talk, sp_final. */
(function(){
'use strict';
if(typeof FXR==='undefined'||typeof FX_KIND==='undefined')return;

/* ---------- utilidades ---------- */
const H=s=>esc(s).replace(/\*\*(.+?)\*\*/g,'<mark class="sp-k">$1</mark>');
const hash=s=>{let h=0;for(const c of String(s))h=(h*31+c.charCodeAt(0))>>>0;return h};
const lang=()=>(P&&P.c&&P.c.tts)||'en-US';
const sayEn=(t,who,slow)=>{try{fxSay(plain(t),who||null,!!slow)}catch(e){}};
const voiceOK=()=>!!(window.PogVoice&&PogVoice.supported());
const AVF=['👩🏻','👩🏽','👩🏿','👩🏼','👩🏾','👩🏻‍🦱','👩🏽‍🦰'],AVM=['👨🏻','👨🏽','👨🏿','👨🏼','👨🏾','👨🏻‍🦱','👨🏽‍🦲'];
const av=(n,g)=>{const a=g==='m'?AVM:AVF;return a[hash(n)%a.length]};
function reg(name,g){try{if(name&&typeof GENDER_MAP!=='undefined'&&!GENDER_MAP[name])GENDER_MAP[name]=[g==='m'?'m':'f',hash(name)%3]}catch(e){}}
function quiet(txt,mood){const b=$('#pbub'),pg=$('#pdock .pog');if(!b)return;clearInterval(say.t);b.textContent=txt;if(pg){pg.classList.remove('happy','happy2','happy3','sad','talk');if(mood)pg.classList.add(mood)}}
function grade(ok,why,right){
  P.streak=ok?(P.streak||0)+1:0;beep(ok);if(ok)confetti(P.streak>=3?80:28);
  const fb=$('#fb');if(fb)fb.innerHTML=`<div class="feedback ${ok?'ok':'no'}"><div><b>${ok?pickRight(P.t):P.t.wrong}</b>${ok||!right?'':`${P.t.correctIs} <i>${esc(right)}</i><br>`}${why?mk(why):''}</div></div>`;
  quiet(ok?pickRight(P.t):P.t.wrong,pickMood(ok));
  setTimeout(()=>{const f=$('#fb');if(f)f.scrollIntoView({behavior:'smooth',block:'nearest'})},60);
}
const tier=s=>s>=85?'great':s>=65?'good':s>=40?'ok':'low';
const avg=a=>{a=a.filter(x=>typeof x==='number');return a.length?Math.round(a.reduce((x,y)=>x+y,0)/a.length):null};
/* sequência de falas com destaque; só continua enquanto o quadro atual é o mesmo */
function seq(lines,my,o){
  o=o||{};let i=0;clearTimeout(my.tm);
  const go=()=>{
    if(!P||P.fx!==my)return;
    if(i>=lines.length){o.onEnd&&o.onEnd();return}
    const L=lines[i];o.onLine&&o.onLine(i);sayEn(L[1],L[0],o.slow);
    const est=Math.max(1400,plain(L[1]).length*(o.slow?150:88)+500);i++;const t0=Date.now();
    const wait=()=>{if(!P||P.fx!==my)return;const spk=window.speechSynthesis&&speechSynthesis.speaking,dt=Date.now()-t0;
      if(dt<est*.6||(spk&&dt<est*2.4))my.tm=setTimeout(wait,160);else go()};
    my.tm=setTimeout(wait,160);
  };
  go();
}
function pre(n){
  try{speechSynthesis.cancel()}catch(e){}
  try{window.PogVoice&&PogVoice.stop()}catch(e){}
  P.sp=P.sp||{};P.fx.n=n;
}
const ICON=['📖','🎧','🗣️','💬','⭐'],LAB=['Leia','Ouça','Repita','Converse','Desafio'];
function top(n){return `<div class="sp-top"><span class="eyebrow">PÁGINA ${n+1}/5 · ${LAB[n].toUpperCase()}</span><div class="sp-dots">${ICON.map((x,i)=>(i?'<u></u>':'')+`<i class="${i<n?'done':i===n?'now':''}">${x}</i>`).join('')}</div></div>`}

/* ---------- mini-ilustrações (SVG leve, nada cortado, sem texto sobre a imagem) ---------- */
const SKY={sky:['#7fd0ff','#e6f7ff'],dawn:['#ffd0a6','#fff0d4'],dusk:['#ff9a76','#6b5bbf'],night:['#1b2559','#5a46a8'],warm:['#ffe3a6','#ffc27a'],sea:['#7fe0ea','#d6f6ff'],snow:['#cfe6ff','#f6fbff'],rose:['#ffc6dd','#fff0f6'],lime:['#c8f0a0','#f2ffd9'],lav:['#cdb8ff','#f0e9ff'],fire:['#ff8a5c','#ffd36e'],mint:['#a8f0d8','#eafff7']};
const GND={grass:['#7ac36a','#5aa650'],sand:['#f0cf8a','#e0b768'],snow:['#ffffff','#e3eefc'],sea:['#3aa6c9','#2688b0'],stone:['#b8b2c4','#9a93aa'],dirt:['#c98f5a','#a8703f'],city:['#6f6a8f','#59547a'],none:null};
const LAY=[
 [[160,62,60],[68,80,38],[252,80,38],[112,28,24]],
 [[88,66,54],[170,74,44],[244,80,36],[130,26,22]],
 [[84,62,64],[204,44,40],[252,84,40],[160,92,24]],
 [[240,62,64],[100,44,40],[58,84,40],[160,84,24]]];
let SPID=0;
function spArt(a){
  a=a||{};const sk=SKY[a.s]||SKY.sky,gn=GND[a.g==null?'grass':a.g],id='spg'+(++SPID),rnd=(()=>{let h=hash((a.e||[]).join('')+(a.d||''))||7;return()=>{h=(h*1103515245+12345)>>>0;return(h%10000)/10000}})();
  const lay=LAY[(a.l||0)%4],D=String(a.d||'sun').split('+'),night=/night|dusk/.test(a.s||'');
  let o=`<svg viewBox="0 0 320 120" role="img" aria-hidden="true"><defs><linearGradient id="${id}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${sk[0]}"/><stop offset="1" stop-color="${sk[1]}"/></linearGradient></defs><rect width="320" height="120" fill="url(#${id})"/>`;
  const sunX=lay[0][0]>200?40:284;
  if(D.includes('sun'))o+=`<circle cx="${sunX}" cy="26" r="24" fill="#ffd23f" opacity=".3"/><circle cx="${sunX}" cy="26" r="15" fill="#ffd23f"/>`;
  if(D.includes('moon'))o+=`<circle cx="${sunX}" cy="28" r="15" fill="#fff3c4"/><circle cx="${sunX+7}" cy="23" r="13" fill="${sk[0]}"/>`;
  if(D.includes('stars'))for(let i=0;i<12;i++)o+=`<circle class="sp-tw" style="animation-delay:-${(i%5)*.45}s" cx="${(14+rnd()*292).toFixed(0)}" cy="${(8+rnd()*46).toFixed(0)}" r="${(1+rnd()*1.3).toFixed(1)}" fill="#fff"/>`;
  if(D.includes('clouds'))o+=`<g fill="#fff" opacity=".85"><ellipse cx="${sunX>100?70:250}" cy="22" rx="26" ry="8"/><ellipse cx="${sunX>100?92:272}" cy="17" rx="16" ry="7"/></g><g fill="#fff" opacity=".6"><ellipse cx="${sunX>100?170:150}" cy="40" rx="20" ry="6"/></g>`;
  if(D.includes('snow'))for(let i=0;i<22;i++)o+=`<circle cx="${(8+rnd()*304).toFixed(0)}" cy="${(6+rnd()*100).toFixed(0)}" r="${(1.2+rnd()*1.6).toFixed(1)}" fill="#fff" opacity=".9"/>`;
  if(D.includes('confetti')){const C=['#ff6f59','#ffd23f','#2fbf9b','#7c4dff','#f0508b'];for(let i=0;i<22;i++)o+=`<rect x="${(8+rnd()*300).toFixed(0)}" y="${(6+rnd()*70).toFixed(0)}" width="5" height="3" rx="1" fill="${C[i%5]}" transform="rotate(${(rnd()*180).toFixed(0)} ${(8+rnd()*300).toFixed(0)} 20)" opacity=".9"/>`}
  if(D.includes('bunting')){const C=['#ff6f59','#ffd23f','#2fbf9b','#7c4dff','#f0508b'];o+=`<path d="M0 6 Q160 28 320 6" fill="none" stroke="#7a5a3a" stroke-width="1.5"/>`;for(let i=0;i<12;i++){const t=(i+.5)/12,x=t*320,y=6+Math.sin(Math.PI*t)*17;o+=`<path d="M${(x-9).toFixed(0)} ${(y-1).toFixed(0)} L${(x+9).toFixed(0)} ${(y-1).toFixed(0)} L${x.toFixed(0)} ${(y+15).toFixed(0)}Z" fill="${C[i%5]}"/>`}}
  if(D.includes('leaves')){const C=['#e8741c','#c8412b','#f0b030'];for(let i=0;i<9;i++)o+=`<ellipse cx="${(10+rnd()*300).toFixed(0)}" cy="${(8+rnd()*80).toFixed(0)}" rx="5" ry="2.6" fill="${C[i%3]}" transform="rotate(${(rnd()*180).toFixed(0)} ${(10+rnd()*300).toFixed(0)} 40)" opacity=".85"/>`}
  if(D.includes('sparkle'))for(let i=0;i<6;i++)o+=`<text class="sp-tw" style="animation-delay:-${i*.4}s" x="${(16+rnd()*288).toFixed(0)}" y="${(14+rnd()*50).toFixed(0)}" font-size="${(9+rnd()*7).toFixed(0)}" fill="#fff" text-anchor="middle">✦</text>`;
  if(gn){
    if(a.g==='sea'){o+=`<rect y="88" width="320" height="32" fill="${gn[0]}"/><path d="M0 92 Q20 84 40 92 T80 92 T120 92 T160 92 T200 92 T240 92 T280 92 T320 92 V120 H0Z" fill="${gn[1]}" opacity=".8"/>`}
    else o+=`<path d="M0 98 Q80 84 160 96 T320 90 V120 H0Z" fill="${gn[0]}"/><path d="M0 110 Q100 100 200 108 T320 106 V120 H0Z" fill="${gn[1]}" opacity=".6"/>`;
  }
  if(D.includes('waves')&&a.g!=='sea')o+=`<path d="M0 104 Q20 96 40 104 T80 104 T120 104 T160 104 T200 104 T240 104 T280 104 T320 104 V120 H0Z" fill="#ffffff" opacity=".45"/>`;
  (a.e||[]).slice(0,4).forEach((em,i)=>{const p=lay[i];if(!p||!em)return;o+=`<text class="sp-em e${i}" x="${p[0]}" y="${p[1]}" font-size="${p[2]}" text-anchor="middle" dominant-baseline="central">${em}</text>`});
  return o+'</svg>';
}
const art=(a,sm)=>`<div class="sp-art${sm?' sm':''}">${spArt(a)}</div>`;

/* ======================= PÁGINA 1 · LEIA ======================= */
FXR.sp_read=function(f,st,n){
  pre(n);const my=P.fx,e=P.e,L=f.lines;
  st.innerHTML=`<div class="step fx sp sp-read">${top(n)}${art(f.art)}
  <h1 class="sp-title">${esc(e.t)}</h1><p class="sp-sub">${esc(e.s)}</p>
  <div class="sp-chips"><span class="badge-pill">${esc(f.topic||'🌏 Cultura')}</span>${f.place?`<span class="badge-pill">📍 ${esc(f.place)}</span>`:''}</div>
  <div class="sp-goal"><span class="g1">📖 Ler</span><span class="g2">🎧 Ouvir</span><span class="g3">🗣️ Falar</span></div>
  <div class="sp-card sp-text" id="sptext"><div class="sp-card-h"><b>${esc(f.title||'Leia')}</b><span><button class="pill light" id="spall" type="button">▶ Ouvir tudo</button> <button class="pill light" id="sptr" type="button">🌐 Tradução</button></span></div>
  ${L.map((l,i)=>`<div class="sp-l" data-i="${i}" style="--i:${i}"><button class="say2" type="button" aria-label="Ouvir">${spk}</button><div><p>${H(l[0])}</p><small>${esc(l[1])}</small></div></div>`).join('')}</div>
  <div class="sp-words">${f.words.map((w,i)=>`<button class="sp-w" data-i="${i}" type="button"><span>${w[1]}</span><b>${esc(w[0])}</b><small>${esc(w[2])}</small></button>`).join('')}</div>
  <div class="sp-fact"><span>💡</span><div><b>Você sabia?</b> ${H(f.fact)}</div></div></div>`;
  const rows=[...st.querySelectorAll('.sp-l')],box=$('#sptext');
  rows.forEach((r,i)=>r.onclick=()=>{clearTimeout(my.tm);rows.forEach(x=>x.classList.remove('on'));r.classList.add('on');r.classList.add('tr');sayEn(L[i][0])});
  $('#sptr').onclick=()=>{box.classList.toggle('alltr');sfx('pop')};
  $('#spall').onclick=()=>{clearTimeout(my.tm);try{speechSynthesis.cancel()}catch(e){}seq(L.map(l=>[null,l[0]]),my,{onLine:i=>{rows.forEach((x,j)=>x.classList.toggle('on',j===i));if(rows[i])rows[i].scrollIntoView({behavior:'smooth',block:'nearest'})},onEnd:()=>rows.forEach(x=>x.classList.remove('on'))})};
  st.querySelectorAll('.sp-w').forEach(b=>b.onclick=()=>{sfx('pop');sayEn(f.words[+b.dataset.i][0])});
  P.fx.cta=null;cta('Continuar',true,true);say(f.say||'Leia com calma. Toque numa frase para ouvir e ver a tradução.');
};

/* ======================= PÁGINA 2 · OUÇA ======================= */
FXR.sp_listen=function(f,st,n){
  pre(n);const my=P.fx,Q=f.qs,cast=f.cast||{};Object.keys(cast).forEach(k=>reg(k,cast[k]));
  let qi=0,okc=0,answered=false,shown=false;P.sp.listen=0;
  const lines=f.lines.map(l=>[l[0],l[1]]);
  st.innerHTML=`<div class="step fx sp sp-listen">${top(n)}${art(f.art,1)}
  <div class="sp-card"><div class="sp-audio" id="spa"><button class="sp-bigplay" id="spp" type="button" aria-label="Ouvir">${spk}</button><div class="sp-wave"><i></i><i></i><i></i><i></i><i></i></div><div class="t"><b>${esc(f.title||'Ouça a conversa')}</b><small>Ouça sem ler. Repita quantas vezes quiser.</small></div><button class="pill light" id="spslow" type="button">🐢 Devagar</button></div></div>
  <div id="spq"></div><div id="fb"></div><div class="sp-card sp-script" id="spsc" hidden></div></div>`;
  const aud=$('#spa');
  const play=slow=>{clearTimeout(my.tm);try{speechSynthesis.cancel()}catch(e){}aud.classList.add('playing');seq(lines,my,{slow,onEnd:()=>{const a=$('#spa');if(a)a.classList.remove('playing')}})};
  $('#spp').onclick=()=>play(false);$('#spslow').onclick=()=>play(true);
  const draw=()=>{const q=Q[qi];answered=false;
    $('#spq').innerHTML=`<div class="sp-card"><span class="sp-qn">Pergunta ${qi+1}/${Q.length}</span><div class="sp-ask">${esc(q.q)}</div>${q.h?`<small>${esc(q.h)}</small>`:''}<div class="fx-opts">${q.o.map((o,i)=>`<button class="fx-o" data-i="${i}" type="button">${esc(o)}</button>`).join('')}</div></div>`;
    $('#fb').innerHTML='';
    $('#spq').querySelectorAll('.fx-o').forEach(b=>b.onclick=()=>{if(answered)return;answered=true;const i=+b.dataset.i,ok=i===q.a;
      $('#spq').querySelectorAll('.fx-o').forEach((x,j)=>{x.disabled=true;if(j===q.a)x.classList.add('ok');else if(j===i)x.classList.add('no')});
      if(ok){okc++;P.score++;P.sp.listen=okc}
      grade(ok,q.w||'',q.o[q.a]);cta(qi<Q.length-1?'Próxima ▶':'Ver o texto',true,true)});
    cta('Escolha uma resposta',false)};
  const reveal=()=>{const sc=$('#spsc');sc.hidden=false;
    sc.innerHTML=`<div class="sp-card-h"><b>📝 O texto da conversa</b><span class="sp-qn">${okc}/${Q.length} certas</span></div>`+f.lines.map((l,i)=>{const g=cast[l[0]]||'f';return `<div class="sp-bub ${i%2?'me':''}" style="animation-delay:${i*.07}s"><div class="sp-av">${av(l[0],g)}</div><div class="sp-msg" data-i="${i}"><span class="sp-who">${esc(l[0])}</span>${H(l[1])}<small>${esc(l[2]||'')}</small></div></div>`}).join('');
    sc.querySelectorAll('.sp-msg').forEach(m=>m.onclick=()=>{m.classList.add('tr');const l=f.lines[+m.dataset.i];sayEn(l[1],l[0])});
    sc.scrollIntoView({behavior:'smooth',block:'nearest'})};
  P.fx.cta=()=>{if(!answered)return true;
    if(qi<Q.length-1){qi++;draw();return true}
    if(!shown){shown=true;reveal();cta('Continuar',true,true);return true}
    return false};
  draw();say(f.say||'Aperte o play e ouça a conversa sem ler. Depois responda.');
};

/* ======================= PÁGINA 3 · REPITA (fala) ======================= */
FXR.sp_repeat=function(f,st,n){
  pre(n);const my=P.fx,items=f.items;let i=0;const best=[];P.sp.say=best;
  const hostHTML=()=>voiceOK()?'<div id="spmic" class="pv-host"></div>':'<div class="sp-note">Este navegador não reconhece voz. Use o Chrome, o Edge ou o Safari. Por enquanto, repita em voz alta e toque em “Já falei”.</div>';
  const end=()=>{
    const a=avg(best),ok=best.filter(x=>x>=65).length;
    st.innerHTML=`<div class="step fx sp sp-repeat">${top(n)}${art(f.art,1)}<div class="sp-card"><div class="sp-card-h"><b>Resultado da repetição</b></div>
    <div class="pv-score ${a==null?'ok':tier(a)} big"><b>${a==null?'—':a+'%'}</b><span>${a==null?'Você pulou a fala. Volte quando puder usar o microfone.':`${ok} de ${items.length} frases acima de 65%`}</span></div>
    ${items.map((it,k)=>`<button class="sp-key" data-k="${k}" type="button" style="margin-top:6px"><span class="say2">${spk}</span><div><b>${H(it[0])}</b><em>${typeof best[k]==='number'?best[k]+'%':'—'}</em></div></button>`).join('')}</div></div>`;
    st.querySelectorAll('.sp-key').forEach(b=>b.onclick=()=>sayEn(items[+b.dataset.k][0]));
    P.fx.cta=null;cta('Continuar',true,true);say(a==null?'Quando puder, treine a fala em voz alta.':'Falar em voz alta faz toda a diferença!');
  };
  const draw=()=>{
    if(i>=items.length)return end();
    const it=items[i],last=i===items.length-1;
    st.innerHTML=`<div class="step fx sp sp-repeat">${top(n)}${art(f.art,1)}
    <div class="sp-card"><div class="sp-card-h"><b>Repita em voz alta</b><span class="sp-qn">${i+1}/${items.length}</span></div>
    <div class="sp-turn" id="spturn" style="border-style:solid;margin-top:4px"><div class="sl-target"><button class="fx-play" id="spt" type="button">${spk}</button><div><b>${H(it[0])}</b><small>${esc(it[1])}</small></div></div>
    <div class="sp-tools"><button class="pill light" id="spsl" type="button">🐢 Devagar</button><button class="pill light" id="sphide" type="button">🙈 Esconder</button></div>${hostHTML()}</div>
    <button class="pill light" id="spskip" type="button" style="margin-top:10px">${voiceOK()?'Pular':'Já falei ✓'}</button></div></div>`;
    const target=plain(it[0]);
    $('#spt').onclick=()=>sayEn(target);$('#spsl').onclick=()=>sayEn(target,null,true);
    $('#sphide').onclick=()=>$('#spturn').classList.toggle('sp-blur');
    const nxt=()=>{i++;draw()};
    $('#spskip').onclick=()=>{try{window.PogVoice&&PogVoice.stop()}catch(e){}nxt()};
    P.fx.cta=()=>{if(best[i]===undefined)return true;nxt();return true};
    if(voiceOK()){
      PogVoice.mount($('#spmic'),{target,lang:lang(),onDone:r=>{const first=best[i]===undefined;best[i]=Math.max(best[i]||0,r.score);if(first&&r.score>=65)P.score++;
        quiet(r.score>=85?'Pronúncia ótima!':r.score>=65?'Muito bem! Quer tentar melhorar?':'Ouça o modelo e tente de novo.',pickMood(r.score>=65));cta(last?'Ver resultado':'Próxima ▶',true,true)},
        onFail:c=>{if(c==='unsupported'){best[i]=null;cta(last?'Ver resultado':'Próxima ▶',true,true)}}});
      cta('Fale e veja sua nota',false);
    }else{cta('Fale em voz alta',false);const sk=$('#spskip');sk.onclick=()=>{best[i]=null;cta(last?'Ver resultado':'Próxima ▶',true,true);sk.disabled=true}}
    if(i===0)say(f.say||'Ouça o modelo, toque no microfone e repita a frase.');
  };
  draw();
};

/* ======================= PÁGINA 4 · CONVERSE (fala) ======================= */
FXR.sp_talk=function(f,st,n){
  pre(n);const my=P.fx,T=f.turns,npc=f.npc[0],ng=f.npc[1];reg(npc,ng);let ti=0;const best=[];P.sp.talk=best;
  st.innerHTML=`<div class="step fx sp sp-talk">${top(n)}${art(f.art,1)}
  <div class="sp-card"><div class="sp-card-h"><b>${esc(f.title||'Converse')}</b><span class="sp-av" style="width:34px;height:34px;font-size:20px">${av(npc,ng)}</span></div><p class="sp-sub" style="margin-bottom:4px">${esc(f.intro)}</p>
  <div id="spchat"></div><div id="spturn"></div></div></div>`;
  const chat=$('#spchat');
  const bub=(who,text,pt,me,extra)=>{const d=document.createElement('div');d.className='sp-bub'+(me?' me':'');
    d.innerHTML=`<div class="sp-av">${me?'🙋':av(who,ng)}</div><div class="sp-msg"><span class="sp-who">${esc(me?'Você':who)}${extra||''}</span>${H(text)}<small>${esc(pt||'')}</small></div>`;
    d.querySelector('.sp-msg').onclick=function(){this.classList.add('tr');sayEn(text,me?null:who)};chat.appendChild(d);d.scrollIntoView({behavior:'smooth',block:'nearest'});return d};
  const npcTurn=()=>{
    const t=T[ti];$('#spturn').innerHTML='';
    const ty=document.createElement('div');ty.className='sp-bub';ty.innerHTML=`<div class="sp-av">${av(npc,ng)}</div><div class="sp-msg"><span class="sp-typing"><i></i><i></i><i></i></span></div>`;chat.appendChild(ty);
    cta('…',false);
    setTimeout(()=>{if(!P||P.fx!==my)return;ty.remove();bub(npc,t.npc[0],t.npc[1],false);sayEn(t.npc[0],npc);userTurn()},650);
  };
  const userTurn=()=>{
    const t=T[ti],last=ti===T.length-1,target=plain(t.you[0]);
    $('#spturn').innerHTML=`<div class="sp-turn" id="spt0"><div class="lbl"><span>🎤 Sua vez · ${ti+1}/${T.length}</span></div><div class="sl-target"><button class="fx-play" id="spm" type="button">${spk}</button><div><b>${H(t.you[0])}</b><small>${esc(t.you[1])}</small></div></div>
    <div class="sp-tools"><button class="pill light" id="sphide" type="button">🙈 Esconder</button><button class="pill light" id="spskip" type="button">${voiceOK()?'Pular':'Já falei ✓'}</button></div>${voiceOK()?'<div id="spmic" class="pv-host"></div>':'<div class="sp-note">Sem reconhecimento de voz neste navegador. Fale em voz alta e toque em “Já falei”.</div>'}</div>`;
    $('#spturn').scrollIntoView({behavior:'smooth',block:'nearest'});
    $('#spm').onclick=()=>sayEn(target);$('#sphide').onclick=()=>$('#spt0').classList.toggle('sp-blur');
    const finish=score=>{
      const sc=typeof score==='number'?`<span class="sp-sc ${tier(score)}">${score}%</span>`:'';
      $('#spturn').innerHTML='';bub('',t.you[0],t.you[1],true,sc);
      if(last&&f.end){setTimeout(()=>{if(!P||P.fx!==my)return;bub(npc,f.end[0],f.end[1],false);sayEn(f.end[0],npc)},500)}
      if(last){cta('Continuar',true,true);P.fx.cta=null}
      else{ti++;npcTurn()}
    };
    P.fx.cta=()=>true;
    $('#spskip').onclick=()=>{try{window.PogVoice&&PogVoice.stop()}catch(e){}best[ti]=voiceOK()?undefined:null;finish(null)};
    if(voiceOK()){
      let done=false;
      PogVoice.mount($('#spmic'),{target,lang:lang(),onDone:r=>{best[ti]=Math.max(best[ti]||0,r.score);if(!done){done=true;if(r.score>=65)P.score++}
        quiet(r.score>=65?'Muito bem! Pode seguir.':'Ouça o modelo e tente de novo, ou siga em frente.',pickMood(r.score>=65));
        const cs=$('#spskip');if(cs)cs.textContent='Continuar ▶';
        cta(last?'Continuar':'Próxima ▶',true,true);P.fx.cta=()=>{finish(best[ti]);return true}},
        onFail:c=>{if(c==='unsupported'){best[ti]=null;finish(null)}}});
      cta('Fale e veja sua nota',false);
    }else cta('Fale em voz alta',false);
  };
  npcTurn();say(f.say||'Agora é uma conversa de verdade: eu falo, você responde em voz alta.');
};

/* ======================= PÁGINA 5 · DESAFIO (ler + ouvir + falar) ======================= */
FXR.sp_final=function(f,st,n){
  pre(n);const my=P.fx;let r=0;const res={hear:null,gap:null,say:null};
  const R=['🎧 Ouça','📖 Leia','🗣️ Fale'];
  const wrap=inner=>`<div class="step fx sp sp-final">${top(n)}<div class="sp-rounds">${R.map((x,i)=>`<span class="${i<r?'done':i===r?'now':''}">${x}</span>`).join('')}</div>${inner}</div>`;
  const opts=(o,sel)=>`<div class="fx-opts">${o.map((x,i)=>`<button class="fx-o" data-i="${i}" type="button">${esc(x)}</button>`).join('')}</div>`;
  const choose=(q,onPick)=>{let done=false;st.querySelectorAll('.fx-opts .fx-o').forEach(b=>b.onclick=()=>{if(done)return;done=true;const i=+b.dataset.i,ok=i===q.a;
    st.querySelectorAll('.fx-opts .fx-o').forEach((x,j)=>{x.disabled=true;if(j===q.a)x.classList.add('ok');else if(j===i)x.classList.add('no')});onPick(ok,i)})};
  const next=label=>{cta(label,true,true);P.fx.cta=()=>{r++;draw();return true}};
  const draw=()=>{
    if(r===0){const q=f.hear;
      st.innerHTML=wrap(`<div class="sp-card"><div class="fx-q"><button class="fx-play" id="fxp" type="button">${spk}</button><span>Ouça e escolha a frase que você ouviu.</span></div>${opts(q.o)}<div id="fb"></div></div>`);
      $('#fxp').onclick=()=>sayEn(q.say);
      choose(q,ok=>{res.hear=ok;if(ok)P.score++;grade(ok,q.w||'',q.o[q.a]);sayEn(q.say);next('Próximo desafio ▶')});
      cta('Escolha uma resposta',false);P.fx.cta=()=>true;say('Primeiro, o ouvido: aperte o play e escolha a frase certa.');
    }else if(r===1){const q=f.gap;
      st.innerHTML=wrap(`<div class="sp-card"><div class="fx-q gapq"><div>${H(q.q).replace('___','<span class="hole" id="fxh">&nbsp;?&nbsp;</span>')}<small>${esc(q.pt||'')}</small></div></div>${opts(q.o)}<div id="fb"></div></div>`);
      choose(q,ok=>{res.gap=ok;if(ok)P.score++;const h=$('#fxh');if(h){h.textContent=q.o[q.a];h.classList.add(ok?'ok':'no')}grade(ok,q.w||'',q.o[q.a]);sayEn(q.q.replace('___',q.o[q.a]));next('Último desafio ▶')});
      cta('Escolha uma resposta',false);P.fx.cta=()=>true;say('Agora a leitura: complete a frase.');
    }else if(r===2){const k=f.key,target=plain(k[0]);
      st.innerHTML=wrap(`<div class="sp-card"><div class="sp-card-h"><b>Frase para levar</b></div><div class="sp-turn" id="spturn" style="border-style:solid"><div class="sl-target"><button class="fx-play" id="spm" type="button">${spk}</button><div><b>${H(k[0])}</b><small>${esc(k[1])}</small></div></div><div class="sp-tools"><button class="pill light" id="spsl" type="button">🐢 Devagar</button><button class="pill light" id="sphide" type="button">🙈 Esconder</button></div>${voiceOK()?'<div id="spmic" class="pv-host"></div>':'<div class="sp-note">Sem reconhecimento de voz neste navegador. Fale em voz alta e toque em “Já falei”.</div>'}</div><button class="pill light" id="spskip" type="button" style="margin-top:10px">${voiceOK()?'Pular':'Já falei ✓'}</button></div>`);
      $('#spm').onclick=()=>sayEn(target);$('#spsl').onclick=()=>sayEn(target,null,true);$('#sphide').onclick=()=>$('#spturn').classList.toggle('sp-blur');
      const go=()=>{r++;draw()};
      $('#spskip').onclick=()=>{try{window.PogVoice&&PogVoice.stop()}catch(e){}go()};
      if(voiceOK()){
        let counted=false;P.fx.cta=()=>{if(res.say==null)return true;go();return true};
        PogVoice.mount($('#spmic'),{target,lang:lang(),onDone:x=>{res.say=Math.max(res.say||0,x.score);if(!counted&&x.score>=65){counted=true;P.score++}
          quiet(x.score>=65?'Essa frase é sua agora!':'Ouça o modelo e tente de novo.',pickMood(x.score>=65));cta('Ver meu resultado',true,true)},
          onFail:c=>{if(c==='unsupported'){res.say=null;go()}}});
        cta('Fale e veja sua nota',false);
      }else{P.fx.cta=null;cta('Fale em voz alta',false);$('#spskip').onclick=()=>{cta('Ver meu resultado',true,true);P.fx.cta=()=>{go();return true}}}
      say('Para fechar, diga a frase para levar.');
    }else summary();
  };
  const summary=()=>{
    const L=P.sp.listen||0,nQ=(P.e.fr[1].qs||[]).length||3;
    const pts=[];for(let k=0;k<nQ;k++)pts.push(k<L?100:0);
    (P.sp.say||[]).forEach(x=>{if(typeof x==='number')pts.push(x)});(P.sp.talk||[]).forEach(x=>{if(typeof x==='number')pts.push(x)});
    if(res.hear!=null)pts.push(res.hear?100:0);if(res.gap!=null)pts.push(res.gap?100:0);if(typeof res.say==='number')pts.push(res.say);
    const pct=pts.length?Math.round(pts.reduce((a,b)=>a+b,0)/pts.length):0,stars=pct>=80?3:pct>=55?2:1;
    const sp=avg([].concat(P.sp.say||[],P.sp.talk||[],[res.say]));
    P.sp.pct=pct;P.sp.stars=stars;
    st.innerHTML=`<div class="step fx sp sp-final">${top(n)}${art(f.art,1)}<div class="sp-card" style="text-align:center"><div class="sp-card-h" style="justify-content:center"><b>Parada concluída!</b></div>
    <div class="sp-stars">${[1,2,3].map(s=>`<i class="${s<=stars?'on':''}" style="transition-delay:${s*.25}s">⭐</i>`).join('')}</div>
    <div class="sp-res"><div><b>${L}/${nQ}</b><small>🎧 Escuta</small></div><div><b>${sp==null?'—':sp+'%'}</b><small>🗣️ Fala</small></div><div><b>${pct}%</b><small>⭐ Geral</small></div></div>
    <button class="sp-key" id="spkey" type="button"><span class="say2">${spk}</span><div style="text-align:left"><small>Frase para levar</small><b>${H(f.key[0])}</b><em>${esc(f.key[1])}</em></div></button></div></div>`;
    setTimeout(()=>st.querySelectorAll('.sp-stars i').forEach(i=>i.classList.add('on')),0);
    $('#spkey').onclick=()=>sayEn(f.key[0]);
    sfx('cheer');confetti(stars>=3?140:60);P.fx.cta=null;cta('Ver meu resultado',true,true);
    say(stars>=3?'Parada perfeita! Três estrelas!':'Boa parada! Volte para treinar a fala quando quiser.');
  };
  draw();
};

/* ---------- integração com o app ---------- */
Object.assign(FX_KIND,{sp_read:'reading',sp_listen:'dialog',sp_repeat:'speak',sp_talk:'speak',sp_final:'practice'});
Object.assign(FX_LABEL,{sp_read:'Leia',sp_listen:'Ouça',sp_repeat:'Repita',sp_talk:'Converse',sp_final:'Desafio'});
if(typeof fxTotal==='function'){const _ft=fxTotal;fxTotal=function(e){return e&&e.sp?12:_ft(e)}}
if(window.PogTTS&&PogTTS.episodeTexts){const _et=PogTTS.episodeTexts;PogTTS.episodeTexts=function(e){
  const base=_et(e);if(!e||!e.sp)return base;
  const out=[],add=(t,sp)=>{t=String(t||'').replace(/\*\*/g,'').trim();if(t&&t.length<400)out.push({text:t,speaker:sp||null})};
  (e.fr||[]).forEach(f=>{
    if(f.k==='sp_read'){(f.lines||[]).forEach(l=>add(l[0]));(f.words||[]).forEach(w=>add(w[0]))}
    if(f.k==='sp_listen')(f.lines||[]).forEach(l=>add(l[1],l[0]));
    if(f.k==='sp_repeat')(f.items||[]).forEach(l=>add(l[0]));
    if(f.k==='sp_talk'){(f.turns||[]).forEach(t=>{add(t.npc[0],f.npc[0]);add(t.you[0])});if(f.end)add(f.end[0],f.npc[0])}
    if(f.k==='sp_final'){add(f.hear&&f.hear.say);add(f.key&&f.key[0])}});
  const seen=new Set();return out.filter(x=>{const k=x.text+'|'+(x.speaker||'');if(seen.has(k))return false;seen.add(k);return true})}}
/* na trilha: paradas culturais ganham visual próprio */
function decorate(){try{document.querySelectorAll('#trail .node[data-ep]').forEach(nd=>{const p=nd.dataset.ep.split(':'),e=(EP[p[0]]||[])[+p[1]];if(e&&e.sp)nd.classList.add('sp-node')})}catch(e){}}
if(typeof course==='function'){const _c=course;course=function(){const r=_c.apply(this,arguments);decorate();return r}}
window.PogSpecial={art:spArt,decorate};
})();
