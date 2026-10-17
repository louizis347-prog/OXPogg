/* Pogglot · mais quadros dinâmicos com o Poggie: Portas, Cartas e Pesca */
(function(){
'use strict';
const X=window.PGX;if(!X)return;
const {q,rnd,esc,hue,pm,setMood,grade,spkIc,FX_SAY}=X;
['pdoor','pcards'].forEach(k=>{window.PGK.push(k);FX_KIND[k]='practice'});
FX_LABEL.pdoor='Portas do Poggie';FX_LABEL.pcards='Memória do Poggie';FX_LABEL.pfish='Pesca do Poggie';
const plain=s=>X.plainS(s);
/* ---------- inserção nos episódios ---------- */
const _fp=window.fxPoggie;
window.fxPoggie=function(e){
  _fp(e);
  try{
    if(!e||!e.fr||e._pg2||e.baked)return;e._pg2=1;
    if(!e.fr.some(f=>f.k==='pbridge'))return;
    const fr=e.fr,at=(k,after)=>{const i=fr.findIndex(f=>f.k===k);return i<0?-1:i+(after?1:0)};
    const ws=fr.find(f=>f.k==='words'),items=(ws&&ws.items||[]).filter(i=>i[0]&&i[1]);
    const gp=fr.find(f=>f.k==='gap');
    if(items.length>=4){
      const ci=at('match',false);
      fr.splice(ci>=0?ci:Math.max(1,fr.length-4),0,{k:'pcards',items:items.slice(0,4)});
    }
    if(gp&&gp.rounds&&gp.rounds.length>=2&&gp.rounds.every(r=>r.opts&&r.opts.length>=2)){
      const gi=fr.findIndex(f=>f.k==='choose');const pos=gi>=0?gi+1:fr.findIndex(f=>f.k==='gap')+1;
      fr.splice(pos,0,{k:'pdoor',rounds:gp.rounds.slice(0,3)});
    }
  }catch(x){console.warn('fun2',x)}
};
const _ft=window.fxTotal;
window.fxTotal=function(e){let n=_ft(e);(e.fr||[]).forEach(f=>{if(f.k==='pdoor'||f.k==='pfish')n+=f.rounds.length;else if(f.k==='pcards')n+=1});return n};
const fill=(t,w)=>plain(t).replace(/_{2,}/g,w);
const mood=(el,c)=>setMood(el,c);
const stageHead=(f,n,title,sub,i,N)=>`${fxKindBar(f,n)}<h2 class="fx-h">${title}${N>1?` <small>${i+1}/${N}</small>`:''}</h2>${sub?`<div class="pgx-ask"><span>${sub[0]}</span><b>${sub[1]}</b></div>`:''}`;

/* ---------- Portas do Poggie: completar a frase escolhendo a porta ---------- */
FXR.pdoor=function(f,st,n){
  const R=f.rounds;let ri=0,done=false;
  const draw=()=>{
    const r=R[ri],ci=r.a,right=r.opts[ci];let mist=0;done=false;
    const q0=plain(r.q),parts=q0.split(/_{2,}/);
    const fin=['walnut','teal','wine'];
    st.innerHTML=`<div class="step fx fx-pg">${stageHead(f,n,'Portas do Poggie',['Poggie quer dizer',`“${esc(r.pt||'')}”`],ri,R.length)}
     <div class="pgx-scene pgd" id="pgs">
      <div class="pgd-sent" id="pgsent">${esc(parts[0]||'')}<span class="pgd-gap" id="pgd-gap">?</span>${esc(parts[1]||'')}</div>
      <div class="pgd-row" id="pgdoors">${r.opts.map((o,i)=>`<div class="pgd-slot"><span class="pgd-plate">${esc(o)}</span><button class="pgd-door ${fin[i%3]}" data-i="${i}" aria-label="${esc(o)}"><span class="pgd-frame"><span class="pgd-in"></span><span class="pgd-leaf"><i class="p1"></i><i class="p2"></i><i class="p3"></i><i class="p4"></i><b class="pgd-knob"></b></span></span></button></div>`).join('')}</div>
      <div class="pgd-floor" id="pgfl"><div class="pgx-hero pgd-hero" id="pgh"><div class="pgx-bub" id="pgbub">${esc(pm('start'))}</div>${poggie({scarf:P.c.scarf})}</div></div></div><div id="fb"></div></div>`;
    const hero=q('#pgh'),bub=q('#pgbub'),sc=q('#pgs'),fl=q('#pgfl');
    const toDoor=btn=>{const sr=fl.getBoundingClientRect(),b=btn.getBoundingClientRect(),w=hero.offsetWidth||80;hero.style.transform=`translateX(${(b.left-sr.left+b.width/2-w/2).toFixed(1)}px)`;hero.classList.remove('hop');void hero.offsetWidth;hero.classList.add('hop')};
    hero.style.transition='none';hero.style.transform=`translateX(${(fl.getBoundingClientRect().width/2-40).toFixed(1)}px)`;requestAnimationFrame(()=>hero.style.transition='');
    document.querySelectorAll('.pgd-door').forEach(b=>b.onclick=()=>{
      if(done||b.classList.contains('shut'))return;
      const i=+b.dataset.i;
      if(i===ci){
        done=true;b.classList.add('open');toDoor(b);sfx('boing');
        q('#pgd-gap').textContent=right;q('#pgd-gap').classList.add('ok');
        setMood(hero,'happy2');bub.textContent=pm('end');sc.classList.add('won');
        if(mist===0)P.score++;
        setTimeout(()=>{sfx('tada');try{confetti(50)}catch(e){}},350);
        const full=fill(r.q,right);
        const fb=q('#fb');
        if(mist===0)fxGrade(true,r.why,right);else grade(mist,{t:full});
        setTimeout(()=>{if(q('#player'))FX_SAY(full,'Poggie')},1400);
        cta(ri<R.length-1?'Próxima porta ▶':'Continuar',true,true);
      }else{
        mist++;b.classList.add('shut','shake');setTimeout(()=>b.classList.remove('shake'),450);
        sfx('oops');bub.textContent=pm('no');mood(hero,'sad');hero.classList.add('wob');setTimeout(()=>hero.classList.remove('wob'),500);
        try{Rx.fire(false)}catch(e){}
      }});
    cta('Escolha a porta certa',false);say(ri===0?'Qual palavra completa a frase? Escolha a porta e o Poggie passa.':'Mais uma porta!');
  };
  P.fx.cta=()=>{if(!done)return true;if(ri<R.length-1){ri++;draw();return true}return false};
  draw();
};

/* ---------- Memória do Poggie: decore as cartas e ache a que o Poggie pedir ---------- */
FXR.pcards=function(f,st,n){
  const all=f.items.filter(x=>x&&x[0]&&x[1]);
  const set=fxShuffle(all).slice(0,Math.min(4,all.length));
  const order=fxShuffle(set.map((_,i)=>i));
  let phase='look',qi=0,mist=0,tries=0,done=false,lock=false,tm=null;
  const mood=(el,m)=>{try{setMood(el,m)}catch(e){}};
  st.innerHTML=`<div class="step fx fx-pg">${stageHead(f,n,'Memória do Poggie',['Memória','Decore as cartas e ache a que o Poggie pedir'],0,1)}
   <div class="pgx-scene pgm" id="pgs"><div class="pgm-top"><div class="pgx-hero pgm-hero" id="pgh"><div class="pgx-bub" id="pgbub">Decore!</div>${poggie({scarf:P.c.scarf})}</div>
     <div class="pgm-say" id="pgsay"><span class="pgm-lab" id="pglab">Você tem alguns segundos</span><div class="pgm-time"><i id="pgti"></i></div></div></div>
    <div class="pgm-grid n${set.length}">${set.map((x,i)=>`<button class="pgm-card look" data-i="${i}" aria-label="Carta ${i+1}"><span class="pgm-in"><span class="pgm-back">?</span><span class="pgm-front"><b>${fxIcon(x[1],54)}</b><em>${esc(plain(x[0]))}</em></span></span></button>`).join('')}</div>
    <div class="pgm-act"><button class="pill light" id="pgok">Já decorei ▶</button><button class="pill light" id="pgpl" hidden>${spkIc()} Ouvir de novo</button></div></div><div id="fb"></div></div>`;
  const hero=q('#pgh'),bub=q('#pgbub'),cards=[...document.querySelectorAll('.pgm-card')],lab=q('#pglab'),ti=q('#pgti');
  const target=()=>set[order[qi]];
  const ask=()=>{const t=target();lab.textContent='Onde está a carta que o Poggie falou?';bub.textContent='Escute!';FX_SAY(plain(t[0]),'Poggie')};
  const hide=()=>{phase='find';cards.forEach(c=>c.classList.remove('look'));q('#pgok').hidden=true;q('#pgpl').hidden=false;ti.parentNode.style.visibility='hidden';
    cta('Toque na carta certa',false);say('As cartas viraram. Ouça e toque na carta que você viu.');setTimeout(ask,550)};
  q('#pgpl').onclick=()=>{if(phase==='find'&&!done)FX_SAY(plain(target()[0]),'Poggie')};
  q('#pgok').onclick=()=>{clearTimeout(tm);hide()};
  /* contagem para decorar */
  const T=Math.max(6000,set.length*2000);ti.style.transition=`width ${T}ms linear`;requestAnimationFrame(()=>requestAnimationFrame(()=>{ti.style.width='0%'}));
  tm=setTimeout(()=>{if(q('#pgs')&&phase==='look')hide()},T);
  cards.forEach((b,i)=>b.onclick=()=>{
    if(phase!=='find'||done||lock||b.classList.contains('hit'))return;
    if(i===order[qi]){
      b.classList.add('hit','look');sfx('burst');mood(hero,'happy');bub.textContent=pm('end');if(tries===0)try{Rx.fire(true)}catch(e){}
      qi++;tries=0;
      if(qi>=set.length){done=true;if(mist<=1)P.score++;mood(hero,'happy2');q('#pgs').classList.add('won');lab.textContent='Memória de elefante!';setTimeout(()=>{sfx('tada');try{confetti(50)}catch(e){}},250);
        grade(mist,{t:''});cta('Continuar',true,true)}
      else{lock=true;setTimeout(()=>{lock=false;ask()},900)}
    }else{
      mist++;tries++;lock=true;b.classList.add('look','wrong');sfx('oops');mood(hero,'sad');bub.textContent='Quase!';try{Rx.fire(false)}catch(e){}
      setTimeout(()=>{b.classList.remove('look','wrong');lock=false},1100);
    }});
  cta('Decore as cartas',false);say('Olhe bem as cartas: elas vão virar.');
};
/* ---------- Pesca do Poggie: ouvir a palavra e pescar o peixe certo ---------- */
FXR.pfish=function(f,st,n){
  const R=f.rounds;let ri=0,done=false;
  const draw=()=>{
    const r=R[ri];let mist=0;done=false;const opts=fxShuffle(r.opts);
    st.innerHTML=`<div class="step fx fx-pg">${stageHead(f,n,'Pesca do Poggie',null,ri,R.length)}
     <div class="pgx-ctl"><button class="pill light" id="pgp">${spkIc()} Ouvir</button><button class="pill light" id="pgsl">🐢 Devagar</button></div>
     <div class="pgx-scene pgf" id="pgs"><div class="pgx-sky"><i class="pgx-sun"></i><i class="pgx-cloud c1"></i></div>
      <div class="pgf-pier"></div><div class="pgx-hero pgf-hero" id="pgh"><div class="pgx-bub" id="pgbub">${esc(pm('start'))}</div>${poggie({scarf:P.c.scarf,rod:1})}</div>
      <div class="pgf-sea">${opts.map((o,i)=>`<button class="pgf-fish" data-w="${esc(plain(o[0]))}" style="--y:${i*25+4}%;--d:${(-i*2.2).toFixed(1)}s;--s:${(7+i*1.3).toFixed(1)}s;--h:${hue(i*3)}" aria-label="peixe ${i+1}"><span class="pgf-body"><em>${fxIcon(o[1],30)}</em></span></button>`).join('')}</div></div><div id="fb"></div></div>`;
    const hero=q('#pgh'),bub=q('#pgbub');
    const play=slow=>FX_SAY(r.w,'Poggie',slow);
    q('#pgp').onclick=()=>play(false);q('#pgsl').onclick=()=>play(true);setTimeout(()=>play(false),500);
    document.querySelectorAll('.pgf-fish').forEach(b=>b.onclick=()=>{
      if(done||b.classList.contains('gone'))return;
      if(b.dataset.w===plain(r.w)){
        done=true;b.classList.add('caught');sfx('splash');mood(hero,'happy2');bub.textContent=pm('end');q('#pgs').classList.add('won');
        if(mist===0)P.score++;setTimeout(()=>{sfx('tada');try{confetti(40)}catch(e){}},300);
        const fb=q('#fb');
        if(mist===0)fxGrade(true,r.pt?`${r.w} = ${r.pt}`:null,r.w);else grade(mist,{t:r.w});
        setTimeout(()=>{if(q('#player'))FX_SAY(r.w,'Poggie')},1300);
        cta(ri<R.length-1?'Próximo peixe ▶':'Continuar',true,true);
      }else{
        mist++;b.classList.add('gone');sfx('boing');mood(hero,'sad');try{Rx.fire(false)}catch(e){}
        if(mist>=3){const t=q(`.pgf-fish[data-w="${CSS.escape(plain(r.w))}"]`);if(t)t.classList.add('hint')}
      }});
    cta('Pesque o peixe da palavra',false);say(ri===0?'Ouça a palavra e pesque o peixe com a imagem certa.':'Mais um peixe!');
  };
  P.fx.cta=()=>{if(!done)return true;if(ri<R.length-1){ri++;draw();return true}return false};
  draw();
};
})();
