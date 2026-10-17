/* Pogglot · diversão: reações com áudio + dois quadros lúdicos de ordenar frases (Poggie protagonista)
   Tudo entra por cima do app (monkeypatch), sem tocar nos dados dos episódios. */
(function(){
'use strict';
window.PGK=window.PGK||['pbridge','pballoon'];
const q=s=>document.querySelector(s);
const rnd=n=>Math.random()*n|0;
const ui=()=>{try{if(typeof P!=='undefined'&&P&&P.c&&P.c.ui&&P.e&&document.querySelector('#pstage'))return P.c.ui==='es'?'es':'pt'}catch(e){}return (typeof ST!=='undefined'&&ST.homeLang)==='es'?'es':'pt'};
const tgtLang=()=>{const t=(typeof P!=='undefined'&&P&&P.c&&P.c.tts)||'';return t.slice(0,2)};

/* ================= REAÇÕES ================= */
const POOL={
 pt:{
  ok:['Ornitorrincamente perfeito!','Quack-tástico!','Bico de ouro!','Cravou!','Mandou bem demais!','Que ouvido!','Acertou na veia!','Olha só quem sabe!','Gol de placa!','Sem erro, craque!','Fez bonito!','Essa foi limpa!','É isso aí!','Tá voando!','De primeira!','Nem precisou pensar!','Show de bola!','Aprendeu rápido, hein?','Arrasou!','Tá de parabéns!','Isso é nível Poggie!','Mais uma pra conta!','Bem na mosca!','Que sangue frio!','Uau!'],
  s3:['Três seguidas! Tá esquentando!','Trio de ouro!','Não para mais!','Embalou!','Sequência boa, hein!'],
  s5:['Cinco seguidas! Pegando fogo!','Ninguém te segura!','Poggie tá chocado!','Que sequência!'],
  s8:['Lenda! Oito seguidas!','Isso já é show!','Impossível errar hoje!','Você é uma máquina!'],
  back:['Agora sim! Errar faz parte.','Voltou com tudo!','Essa foi a virada!','Aprendeu com o erro, boa!','Redenção!','Levantou e acertou!'],
  no:['Quase!','Ixi, escapou por pouco!','Opa, essa pegou.','Calma, acontece!','Hmm, não foi dessa vez.','Essa era traiçoeira!','Quase lá!','Faz parte, vamos de novo.']
 },
 es:{
  ok:['¡Ornitorrincamente perfecto!','¡Cuac-tástico!','¡Pico de oro!','¡Lo clavaste!','¡Qué oído!','¡Justo en el blanco!','¡Golazo!','¡Sin errores!','¡Muy bien hecho!','¡Qué rápido aprendes!','¡Eso es nivel Poggie!','¡Una más!','¡Wow!'],
  s3:['¡Tres seguidas! ¡Se calienta!','¡Trío de oro!','¡Ya no paras!'],
  s5:['¡Cinco seguidas! ¡Ardiendo!','¡Nadie te frena!','¡Qué racha!'],
  s8:['¡Leyenda! ¡Ocho seguidas!','¡Eres una máquina!'],
  back:['¡Ahora sí! Equivocarse es parte.','¡Volviste con todo!','¡Esa fue la remontada!'],
  no:['¡Casi!','¡Uy, por poco!','¡Calma, pasa!','Hmm, esta vez no.','¡Casi lo logras!']
 }
};
const TGT={ /* exclamações na língua que o aluno estuda: [texto, tradução pt, tradução es] */
 en:[['Nailed it!','Mandou bem!','¡Lo clavaste!'],['Spot on!','Na mosca!','¡Justo!'],['You got it!','Você pegou!','¡Lo lograste!'],['Boom!','Boom!','¡Boom!'],['Well done!','Muito bem!','¡Bien hecho!'],['Bingo!','Bingo!','¡Bingo!'],['Right on!','Isso aí!','¡Eso!'],['Awesome!','Demais!','¡Genial!'],['Nice one!','Boa!','¡Buena!'],['Crushed it!','Arrasou!','¡Arrasaste!'],['Look at you!','Olha só você!','¡Mírate!'],['Brilliant!','Brilhante!','¡Brillante!'],['That’s the way!','É assim!','¡Así se hace!'],['Perfect!','Perfeito!','¡Perfecto!']],
 es:[['¡Olé!','Olé!','¡Olé!'],['¡Bravo!','Bravo!','¡Bravo!'],['¡Qué bien!','Que bom!','¡Qué bien!'],['¡Así se hace!','É assim que se faz!','¡Así se hace!'],['¡Eso es!','É isso!','¡Eso es!'],['¡Genial!','Genial!','¡Genial!'],['¡Chévere!','Legal!','¡Chévere!'],['¡Qué crack!','Que craque!','¡Qué crack!'],['¡De diez!','Nota dez!','¡De diez!'],['¡Muy bien!','Muito bem!','¡Muy bien!']],
 fr:[['Bravo !','Bravo!','¡Bravo!'],['Parfait !','Perfeito!','¡Perfecto!'],['Bien joué !','Bem jogado!','¡Bien jugado!'],['Super !','Super!','¡Súper!'],['Génial !','Genial!','¡Genial!']],
 de:[['Super!','Super!','¡Súper!'],['Stark!','Forte!','¡Fuerte!'],['Genau!','Exato!','¡Exacto!'],['Prima!','Ótimo!','¡Estupendo!'],['Bravo!','Bravo!','¡Bravo!']],
 it:[['Bravo!','Bravo!','¡Bravo!'],['Perfetto!','Perfeito!','¡Perfecto!'],['Grande!','Grande!','¡Grande!'],['Che bello!','Que lindo!','¡Qué lindo!'],['Evviva!','Viva!','¡Viva!']],
 pt:[['Boa!','Boa!','¡Buena!'],['Mandou bem!','Mandou bem!','¡Muy bien!'],['Show!','Show!','¡Genial!'],['Isso aí!','Isso aí!','¡Eso!'],['Perfeito!','Perfeito!','¡Perfecto!']]
};
const EMO={ok:['🎉','✨','🌟','👏','🙌','💫','🎯','🔥','🥳','🦆'],s3:['🔥','⚡','🚀'],s5:['🔥','🚀','🌋'],s8:['👑','🏆','🌈'],back:['💪','🔄','🌱'],no:['🤔','😅','🙈','🫣','😬']};
const SFX={ok:['cheer','sparkle','clap','ding','bell','boing'],s3:['tada','sparkle'],s5:['fire','tada'],s8:['fire','tada','cheer'],back:['sparkle','ding']};
const ANIMS=['a1','a2','a3','a4','a5'];
const ENTER={
 scene:['🎬 Luz, câmera, ação!','👂 Orelhas abertas!','🍿 Cena começando!'],
 chunk:['🧩 Peça-chave chegando!','📌 Guarde essa frase!','✨ Frase de ouro!'],
 grammar:['🧠 Regrinha rápida!','💡 Esse truque ajuda muito!','🔍 Olha o padrão!'],
 dictate:['🎧 Capricha no ouvido!','✍️ Hora de escrever!'],
 trap:['🕵️ Detetive em ação!','🪤 Cuidado com as pegadinhas!'],
 convo:['💬 Bora conversar!','🗣️ Sua vez de falar!'],
 order:['🔀 Quebra-cabeça de frases!','🧱 Arrume a conversa!'],
 produce:['🎤 Agora é com você!','🚀 Hora de produzir!'],
 match:['⚡ Jogo relâmpago!','🃏 Combine rápido!'],
 build:['🏗️ Montando frases!','🧩 Frase em obras!'],
 pbridge:['🌉 Ponte em construção!','🦆 Poggie precisa de você!'],
 pballoon:['🎈 Balões no ar!','🎧 Escute e estoure!']
};
const ENTER_ES={scene:['🎬 ¡Luces, cámara, acción!'],chunk:['✨ ¡Frase de oro!'],grammar:['💡 ¡Mira el patrón!'],dictate:['🎧 ¡Ojo al oído!'],trap:['🕵️ ¡Ojo con las trampas!'],convo:['💬 ¡A conversar!'],order:['🔀 ¡Ordena la charla!'],produce:['🚀 ¡Ahora tú!'],match:['⚡ ¡Juego relámpago!'],build:['🧩 ¡Armando frases!'],pbridge:['🌉 ¡Puente en obra!'],pballoon:['🎈 ¡Globos al aire!']};

const Rx=window.Rx={cur:null,recent:{},st:{pid:0,half:false,late:false,wrongBefore:false,lastEnter:-9}};
function pick(list,key){
  const r=Rx.recent[key]=Rx.recent[key]||[];
  let c=list.filter((_,i)=>!r.includes(i));if(!c.length){r.length=0;c=list.slice()}
  const item=c[rnd(c.length)];r.push(list.indexOf(item));if(r.length>Math.min(10,list.length-2))r.shift();return item;
}
function sync(){if(typeof P==='undefined'||!P)return;if(Rx.st.pid!==P.t0){Rx.st={pid:P.t0,half:false,late:false,wrongBefore:false,lastEnter:-9};Rx.cur=null}}
function popEl(R,small){
  const pl=q('#player');if(!pl)return;
  const old=q('.rx-pop');if(old)old.remove();
  const d=document.createElement('div');
  d.className='rx-pop '+(small?'sm ':'')+(R.ok===false?'no ':'')+'rx-'+(R.anim||'a1');
  d.innerHTML=`<span class="rx-em">${R.emoji}</span><span class="rx-tx">${R.text}${R.tr?`<small>${R.tr}</small>`:''}</span>`;
  pl.appendChild(d);setTimeout(()=>{try{d.classList.add('out')}catch(e){}},small?1300:1650);setTimeout(()=>{try{d.remove()}catch(e){}},small?1700:2050);
}
Rx.fire=function(ok,silent){
  sync();const L=ui();const pool=POOL[L]||POOL.pt;const st=(typeof P!=='undefined'&&P&&P.streak)||0;
  let R;
  if(ok){
    const tier=st>=8?'s8':st>=5?'s5':st>=3?'s3':(Rx.st.wrongBefore?'back':'ok');
    const tl=tgtLang(),useTgt=TGT[tl]&&tl!==L&&Math.random()<(tier==='ok'?.38:.22);
    if(useTgt){const x=pick(TGT[tl],'t'+tl);R={ok:true,text:x[0],tr:L==='es'?x[2]:x[1],lang:(P.c&&P.c.tts)||null}}
    else R={ok:true,text:pick(pool[tier]||pool.ok,'o'+tier)};
    R.emoji=pick(EMO[tier],'e'+tier);R.sfx=pick(SFX[tier],'s'+tier);R.tier=tier;Rx.st.wrongBefore=false;
  }else{
    R={ok:false,text:pick(pool.no,'no'),emoji:pick(EMO.no,'eno')};Rx.st.wrongBefore=true;
  }
  R.anim=ANIMS[rnd(ANIMS.length)];R.t=Date.now();R.say=true;Rx.cur=R;
  if(!silent){
    popEl(R,!ok);
    if(ok){setTimeout(()=>{try{sfx(R.sfx)}catch(e){}},80);try{if(window.PogHero)PogHero.react(true)}catch(e){}}
    else{try{if(window.PogHero)PogHero.react(false)}catch(e){}}
  }
  return R;
};
const fresh=()=>Rx.cur&&Date.now()-Rx.cur.t<2500;
Rx.enter=function(kind,n){
  sync();if(typeof P==='undefined'||!P||!P.steps)return;
  const L=ui(),prog=P.i/Math.max(1,P.steps.length-1);let R=null;
  if(!Rx.st.half&&prog>=.5){Rx.st.half=true;R={emoji:'🚀',text:L==='es'?'¡Mitad del camino!':'Metade do caminho!',sfx:'tada'}}
  else if(!Rx.st.late&&prog>=.85){Rx.st.late=true;R={emoji:'🏁',text:L==='es'?'¡Recta final!':'Reta final!',sfx:'fire'}}
  else if(n>=3&&P.i-Rx.st.lastEnter>=3&&Math.random()<.34){
    const arr=(L==='es'?ENTER_ES[kind]:ENTER[kind])||ENTER[kind];
    if(arr){const t=pick(arr,'en'+kind);const m=/^(\S+)\s+(.*)$/.exec(t);R={emoji:m?m[1]:'✨',text:m?m[2]:t,sfx:Math.random()<.4?'quack':'pop'}}
  }
  if(!R)return;Rx.st.lastEnter=P.i;R.anim=ANIMS[rnd(ANIMS.length)];R.ok=true;
  setTimeout(()=>{if(!q('#player'))return;popEl(R,true);try{sfx(R.sfx)}catch(e){}},420);
};

/* ---- ganchos nas funções existentes ---- */
const _beep=window.beep;
window.beep=function(ok){try{_beep(ok)}catch(e){}try{Rx.fire(!!ok)}catch(e){}};
const _pick=window.pickRight;
window.pickRight=function(t){try{if(fresh()&&Rx.cur.ok)return Rx.cur.text;if(typeof P!=='undefined'&&P&&q('#player')){return Rx.fire(true,true).text}}catch(e){}return _pick(t)};
['pt','es'].forEach(l=>{try{const T0=T[l];if(!T0)return;const base=T0.wrong;Object.defineProperty(T0,'wrong',{configurable:true,get(){try{if(fresh()&&Rx.cur.ok===false)return Rx.cur.text}catch(e){}return base}})}catch(e){}});
const _say=window.say;
window.say=function(txt,mood){
  try{const c=Rx.cur;if(c&&c.ok&&c.lang&&fresh()&&typeof txt==='string'&&txt.indexOf(c.text)===0){Rx.sayText=c.text;Rx.sayLang=c.lang}}catch(e){}
  return _say(txt,mood)};
const _speak=window.speak;
window.speak=function(text,lang,btn,speaker,slow){
  if(Rx.sayText&&typeof text==='string'&&text.indexOf(Rx.sayText)===0&&Rx.sayLang){const t=Rx.sayText,l=Rx.sayLang;Rx.sayText=null;return _speak(t,l,btn,speaker,slow)}
  Rx.sayText=null;return _speak(text,lang,btn,speaker,slow)};

/* ---- novos efeitos sonoros ---- */
const _sfx=window.sfx;
function ctx(){try{AC=AC||new (window.AudioContext||window.webkitAudioContext)();return AC}catch(e){return null}}
function tone(f,d,type,v,at,f2){const a=ctx();if(!a)return;const t=a.currentTime+(at||0),o=a.createOscillator(),g=a.createGain();o.type=type||'sine';o.frequency.setValueAtTime(f,t);if(f2)o.frequency.exponentialRampToValueAtTime(f2,t+d);g.gain.setValueAtTime(0,t);g.gain.linearRampToValueAtTime(v||.1,t+.012);g.gain.exponentialRampToValueAtTime(.001,t+d);o.connect(g).connect(a.destination);o.start(t);o.stop(t+d+.05)}
function noise(d,fr,Q,v,at){const a=ctx();if(!a)return;const t=a.currentTime+(at||0),n=a.sampleRate*d,b=a.createBuffer(1,n,a.sampleRate),c=b.getChannelData(0);for(let i=0;i<n;i++)c[i]=Math.random()*2-1;const s=a.createBufferSource();s.buffer=b;const f=a.createBiquadFilter();f.type='bandpass';f.frequency.value=fr;f.Q.value=Q||1;const g=a.createGain();g.gain.setValueAtTime(v||.12,t);g.gain.exponentialRampToValueAtTime(.001,t+d);s.connect(f).connect(g).connect(a.destination);s.start(t)}
const EX={
 tada(){[523,659,784].forEach((f,i)=>tone(f,.16,'triangle',.1,i*.09));tone(1046,.55,'triangle',.11,.28);noise(.4,3600,.8,.05,.3)},
 fire(){tone(220,.6,'sawtooth',.05,0,880);noise(.7,1400,.6,.07,0);[784,988,1175].forEach((f,i)=>tone(f,.2,'square',.04,.32+i*.07))},
 oops(){tone(392,.18,'triangle',.09,0,330);tone(311,.3,'triangle',.09,.17,220)},
 quack(){tone(420,.09,'sawtooth',.07,0,300);tone(360,.13,'sawtooth',.06,.1,240);noise(.16,1100,2,.04,.02)},
 boing(){tone(180,.34,'sine',.12,0,620);tone(620,.22,'triangle',.05,.1,300)},
 splash(){noise(.45,1800,.5,.12,0);tone(500,.2,'sine',.05,0,160)},
 hop(){tone(330,.14,'sine',.1,0,660)},
 plank(){noise(.07,300,2,.14,0);tone(160,.1,'triangle',.08,0,110)},
 burst(){noise(.14,2600,1.2,.14,0);tone(900,.1,'triangle',.07,0,1500)}
};
window.sfx=function(name){if(EX[name]){try{EX[name]()}catch(e){}return}return _sfx(name)};

/* ================= QUADROS NOVOS ================= */
const norm=s=>String(s||'').toLowerCase().replace(/[^a-z0-9áéíóúàâêôãõçñüöäß ]/g,'').replace(/\s+/g,' ').trim();
const plainS=s=>(typeof plain==='function'?plain(s):String(s||'').replace(/\*\*/g,''));
function sentences(e){
  const fr=e.fr||[],seen=new Set(),out=[];
  const add=(t,pt,pri)=>{t=plainS(t).trim();pt=plainS(pt).trim();const w=t.split(/\s+/);if(w.length<3||w.length>9||!pt)return;const k=norm(t);if(seen.has(k))return;seen.add(k);out.push({t,pt,w:w.length,pri:pri||0})};
  const bi=new Set();fr.forEach(f=>{if(f.k==='build')(f.items||[]).forEach(b=>bi.add(norm(plainS(b[0]))))});
  const sc=fr.find(f=>f.k==='scene');(sc&&sc.lines||[]).forEach(l=>{if(l[0]!=='Poggie'&&!bi.has(norm(plainS(l[1]))))add(l[1],l[2],1)});
  const ch=fr.find(f=>f.k==='chunk');if(ch){if(ch.blocks&&ch.pt)add(ch.blocks.map(b=>b[0]).join(' '),ch.pt,2);(ch.variants||[]).forEach(v=>{if(!bi.has(norm(plainS(v[0]))))add(v[0],v[1],1)})}
  if(out.length<4)fr.forEach(f=>{if(f.k==='build')(f.items||[]).forEach(b=>add(b[0],b[1],0))});
  return out.sort((a,b)=>a.w-b.w);
}
window.fxPoggie=function(e){
  try{
    if(!e||!e.fr||e._pg||e.baked)return;e._pg=1;
    if(!e.fr.some(f=>f.k==='cover')||e.fr.some(f=>f.k==='pbridge'))return;
    const S=sentences(e);if(S.length<2)return;
    const h=Math.ceil(S.length/2),A=S.slice(0,Math.min(2,h)),B=S.slice(h,h+2).length?S.slice(h,h+2):S.slice(0,1);
    const ci=e.fr.findIndex(f=>f.k==='chunk'),bi=e.fr.findIndex(f=>f.k==='build'),gi=e.fr.findIndex(f=>f.k==='gap');
    const fb={k:'pballoon',rounds:B};
    const ia=ci>=0?ci+1:Math.max(1,e.fr.findIndex(f=>f.k==='scene')+1);
    e.fr.splice(ia,0,{k:'pbridge',rounds:A});
    const ib=(bi>=0?bi:gi>=0?gi:e.fr.length-4)+(bi>=0?2:1);
    e.fr.splice(Math.min(ib,e.fr.length-1),0,fb);
  }catch(err){}
};
const _fxb=window.fxBridge;window.fxBridge=function(e){try{_fxb(e)}catch(x){}window.fxPoggie(e)};
FX_KIND.pbridge=FX_KIND.pballoon='practice';
FX_LABEL.pbridge='Ponte do Poggie';FX_LABEL.pballoon='Balões do Poggie';
const _ft=window.fxTotal;window.fxTotal=function(e){let n=_ft(e);(e.fr||[]).forEach(f=>{if(f.k==='pbridge'||f.k==='pballoon')n+=f.rounds.length});return n};
const _rf=window.renderFx;
window.renderFx=function(n,st,lang){
  const f=P.e.fr[n],pl=q('#player');if(pl)pl.classList.toggle('pgmode',window.PGK.includes(f.k));
  window.PogHero=null;
  _rf(n,st,lang);try{Rx.enter(f.k,n)}catch(e){}
};

const POGMSG={
 pt:{start:['Me ajuda?','Bora!','Chegou a hora!','Vamos nessa!'],ok:['Isso!','Boa!','Aí sim!','Segue!','Uhul!'],no:['Hm…','Opa!','Essa não!','Eita!'],end:['Cheguei!','Consegui!','Uhuuu!','Missão cumprida!']},
 es:{start:['¿Me ayudas?','¡Vamos!','¡A ello!'],ok:['¡Eso!','¡Bien!','¡Sigue!'],no:['Hm…','¡Uy!','¡Esa no!'],end:['¡Llegué!','¡Lo logré!','¡Misión cumplida!']}
};
const pm=(k)=>{const L=POGMSG[ui()]||POGMSG.pt;return L[k][rnd(L[k].length)]};
const tokens=t=>plainS(t).trim().split(/\s+/);
const spkIc=()=>(typeof spk!=='undefined'?spk:'🔊');
const FX_SAY=(t,who,slow)=>{try{fxSay(t,who,slow)}catch(e){}};
function setMood(root,cls){const p=root&&root.querySelector('.pog');if(!p)return;p.classList.remove('happy','happy2','happy3','sad');void p.offsetWidth;if(cls)p.classList.add(cls)}
function grade(mist,r){
  if(mist===0){fxGrade(true,null,r.t);return}
  P.streak=0;try{beep(true)}catch(e){}
  const fb=q('#fb');if(fb)fb.innerHTML=`<div class="feedback ok"><div><b>${mist===1?'Quase perfeito!':'Chegou lá!'}</b>Você tropeçou ${mist}x, mas terminou a frase. Ouça de novo e tente sem erros da próxima vez.</div></div>`;
}
function resultCard(r){return `<div class="pgx-win"><button class="pgx-win-b" id="pgw"><span class="say2">${spkIc()}</span><div><b>${esc(r.t)}</b><em>${esc(r.pt)}</em></div></button></div>`}
const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const hue=i=>[12,36,152,190,262,330,48,205][i%8];

/* ---------- Ponte do Poggie: leitura + tradução, ordem das palavras ---------- */
FXR.pbridge=function(f,st,n){
  const R=f.rounds;let ri=0,done=false;
  const draw=()=>{
    const r=R[ri],tk=tokens(r.t),words=fxShuffle(tk.map((w,i)=>({w,i})));let pos=0,mist=0,stepMist=0;done=false;
    st.innerHTML=`<div class="step fx fx-pg">${fxKindBar(f,n)}
     <h2 class="fx-h">Ponte do Poggie${R.length>1?` <small>${ri+1}/${R.length}</small>`:''}</h2>
     <div class="pgx-ask"><span>Poggie quer dizer</span><b>“${esc(r.pt)}”</b></div>
     <div class="pgx-scene pgb" id="pgs"><div class="pgx-sky"><i class="pgx-sun"></i><i class="pgx-cloud c1"></i><i class="pgx-cloud c2"></i></div>
      <div class="pgb-water"><i></i><i></i><i></i></div>
      <div class="pgb-bank l"></div><div class="pgb-bank r"><span class="pgb-flag">🏁</span></div>
      <div class="pgb-stones" id="pgst">${tk.map(()=>'<i class="pgb-st"></i>').join('')}</div>
      <div class="pgx-hero" id="pgh"><div class="pgx-bub" id="pgbub">${esc(pm('start'))}</div>${poggie({scarf:P.c.scarf})}</div></div>
     <div class="pgx-sign" id="pgsign"><span class="pgx-sign-h">Frase</span></div>
     <div class="bank pgx-bank" id="bank">${words.map(o=>`<button class="tile pgx-t" data-w="${esc(o.w)}" data-k="${o.i}">${esc(o.w)}</button>`).join('')}</div><div id="fb"></div></div>`;
    const sc=q('#pgs'),hero=q('#pgh'),bub=q('#pgbub'),stones=[...q('#pgst').children],sign=q('#pgsign');
    const heroX=idx=>{const sr=sc.getBoundingClientRect();let cx;if(idx<0){const b=sc.querySelector('.pgb-bank.l').getBoundingClientRect();cx=b.left+b.width*.5}else if(idx>=tk.length){const b=sc.querySelector('.pgb-bank.r').getBoundingClientRect();cx=b.left+b.width*.45}else{const b=stones[idx].getBoundingClientRect();cx=b.left+b.width/2}return cx-sr.left};
    const place=(idx,anim)=>{const w=hero.offsetWidth||110,sw=sc.getBoundingClientRect().width;let x=heroX(idx);x=Math.max(w/2+4,Math.min(sw-w/2-4,x));hero.style.transform=`translateX(${(x-w/2).toFixed(1)}px)`;if(anim){hero.classList.remove('hop');void hero.offsetWidth;hero.classList.add('hop');sfx('hop')}};
    hero.style.transition='none';place(-1,false);requestAnimationFrame(()=>{hero.style.transition='';});
    const hint=()=>{const t=q(`.pgx-t:not(.used)[data-w="${CSS.escape(tk[pos])}"]`);if(t)t.classList.add('hint')};
    const finish=()=>{
      done=true;const ok=mist===0;if(ok)P.score++;
      place(tk.length,true);setMood(hero,'happy2');bub.textContent=pm('end');q('#pgs').classList.add('won');
      setTimeout(()=>{sfx('tada');try{confetti(60)}catch(e){}},420);
      grade(mist,r);setTimeout(()=>{if(q('#player'))FX_SAY(r.t,'Poggie')},1500);
      q('#fb').insertAdjacentHTML('beforeend',resultCard(r));const w=q('#pgw');if(w)w.onclick=()=>FX_SAY(r.t,'Poggie');
      cta(ri<R.length-1?'Próxima ponte ▶':'Continuar',true,true)};
    document.querySelectorAll('.pgx-t').forEach(b=>b.onclick=()=>{
      if(done||b.classList.contains('used'))return;
      if(b.dataset.w===tk[pos]){
        b.classList.add('used');q('#bank').querySelectorAll('.hint').forEach(x=>x.classList.remove('hint'));
        stones[pos].classList.add('on');stones[pos].textContent=b.dataset.w;sfx('plank');
        const sp=document.createElement('span');sp.className='pgx-w';sp.textContent=b.dataset.w;sign.appendChild(sp);
        place(pos,true);bub.textContent=b.dataset.w;setMood(hero,'happy');FX_SAY(b.dataset.w,'Poggie');
        pos++;stepMist=0;
        if(pos>=tk.length)setTimeout(finish,520);
      }else{
        mist++;stepMist++;b.classList.remove('shake');void b.offsetWidth;b.classList.add('shake');
        sfx('splash');bub.textContent=pm('no');setMood(hero,'sad');hero.classList.add('wob');setTimeout(()=>hero.classList.remove('wob'),500);
        try{Rx.fire(false)}catch(e){}
        if(stepMist>=2)hint();
      }});
    cta('Monte a frase na ponte',false);say(ri===0?'Toque nas palavras na ordem e o Poggie atravessa a ponte.':'Mais uma ponte!');
  };
  P.fx.cta=()=>{if(!done)return true;if(ri<R.length-1){ri++;draw();return true}return false};
  draw();
};

/* ---------- Balões do Poggie: ouvir e estourar na ordem ---------- */
FXR.pballoon=function(f,st,n){
  const R=f.rounds;let ri=0,done=false;
  const draw=()=>{
    const r=R[ri],tk=tokens(r.t),words=fxShuffle(tk.map((w,i)=>({w,i})));let pos=0,mist=0,stepMist=0,tr=false;done=false;
    st.innerHTML=`<div class="step fx fx-pg">${fxKindBar(f,n)}
     <h2 class="fx-h">Balões do Poggie${R.length>1?` <small>${ri+1}/${R.length}</small>`:''}</h2>
     <div class="pgx-ctl"><button class="pill light" id="pgp">${spkIc()} Ouvir</button><button class="pill light" id="pgsl">🐢 Devagar</button><button class="pill light" id="pgtr">💡 Dica</button></div>
     <div class="pgx-tr" id="pgtrl" hidden>“${esc(r.pt)}”</div>
     <div class="pgx-scene pgl" id="pgs"><div class="pgx-sky"><i class="pgx-sun"></i><i class="pgx-cloud c1"></i><i class="pgx-cloud c2"></i></div>
      <div class="pgl-air" id="pgair">${words.map((o,j)=>`<button class="pgl-b" data-w="${esc(o.w)}" style="--h:${hue(o.i*3+j)};--d:${(j*-.55).toFixed(2)}s;--r:${(rnd(9)-4)}deg;--y:${rnd(14)}px"><span>${esc(o.w)}</span></button>`).join('')}</div>
      <div class="pgl-row"><div class="pgx-hero st" id="pgh">${poggie({scarf:P.c.scarf})}</div><div class="pgl-say" id="pgsay"><small>Poggie disse…</small><div id="pgwords"></div></div></div></div><div id="fb"></div></div>`;
    const hero=q('#pgh'),box=q('#pgwords');
    window.PogHero={react(ok){setMood(hero,ok?'happy3':'sad')}};
    const play=slow=>{hero.querySelector('.pog').classList.add('talk');FX_SAY(r.t,'Poggie',slow);clearTimeout(play.t);play.t=setTimeout(()=>{try{hero.querySelector('.pog').classList.remove('talk')}catch(e){}},Math.max(1200,r.t.length*95*(slow?1.7:1)))};
    q('#pgp').onclick=()=>play(false);q('#pgsl').onclick=()=>play(true);
    q('#pgtr').onclick=()=>{tr=!tr;q('#pgtrl').hidden=!tr};
    setTimeout(()=>play(false),500);
    const finish=()=>{
      done=true;const ok=mist===0;if(ok)P.score++;
      setMood(hero,'happy2');q('#pgs').classList.add('won');q('#pgtrl').hidden=false;
      setTimeout(()=>{sfx('tada');try{confetti(60)}catch(e){}},260);
      grade(mist,r);setTimeout(()=>{if(q('#player'))FX_SAY(r.t,'Poggie')},1500);
      q('#fb').insertAdjacentHTML('beforeend',resultCard(r));const w=q('#pgw');if(w)w.onclick=()=>FX_SAY(r.t,'Poggie');
      cta(ri<R.length-1?'Próximos balões ▶':'Continuar',true,true)};
    document.querySelectorAll('.pgl-b').forEach(b=>b.onclick=()=>{
      if(done||b.classList.contains('gone'))return;
      if(b.dataset.w===tk[pos]){
        b.classList.add('pop');sfx('burst');setTimeout(()=>b.classList.add('gone'),260);
        document.querySelectorAll('.pgl-b.hint').forEach(x=>x.classList.remove('hint'));
        const sp=document.createElement('span');sp.className='pgx-w';sp.textContent=b.dataset.w;box.appendChild(sp);
        setMood(hero,'happy');pos++;stepMist=0;if(pos>=tk.length)setTimeout(finish,420);
      }else{
        mist++;stepMist++;b.classList.remove('shake');void b.offsetWidth;b.classList.add('shake');sfx('boing');
        setMood(hero,'sad');try{Rx.fire(false)}catch(e){}
        if(stepMist>=2){const t=q(`.pgl-b:not(.gone)[data-w="${CSS.escape(tk[pos])}"]`);if(t)t.classList.add('hint')}
      }});
    cta('Estoure os balões na ordem',false);say(ri===0?'Ouça o Poggie e estoure os balões na ordem em que ele falou.':'Mais uma! Ouça com atenção.');
  };
  P.fx.cta=()=>{if(!done)return true;if(ri<R.length-1){ri++;draw();return true}return false};
  draw();
};
window.PGX={q,rnd,esc,hue,pm,tokens,setMood,grade,resultCard,spkIc,FX_SAY,plainS,sentences};
})();
