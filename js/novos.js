/* Quadros novos por nível: scenebuild, follow (A1) · docread, form (A2) · mystery, paraphrase (B1)
   · voices, chain (B2) · upgrade, rhetoric (C1) · editor, ctxword (C2) */
(function(){
if(typeof FXR==='undefined'||typeof FX_KIND==='undefined')return;
const L={scenebuild:'Monte a cena',follow:'Siga as ordens',puzzle:'Quebra-cabeça',balloons:'Estoure os balões',lexpack:'Mala lexical',docread:'Papel da vida real',form:'Preencha o formulário',mystery:'Caso para resolver',paraphrase:'Mesmo sentido',voices:'Quem pensa o quê?',chain:'Cadeia de causas',upgrade:'Melhore o rascunho',rhetoric:'Marque a retórica',editor:'Você é o editor',ctxword:'Adivinhe pelo contexto'};
Object.keys(L).forEach(k=>{FX_KIND[k]='practice';FX_LABEL[k]=L[k]});
const q=(s,r)=>(r||document).querySelector(s);
const H=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const B=s=>H(s).replace(/\*\*(.+?)\*\*/g,'<b>$1</b>');
const say2=(t,who,slow)=>{try{fxSay(String(t).replace(/\*\*/g,''),who,slow)}catch(e){}};
const shk=el=>{if(!el)return;el.classList.remove('no');void el.offsetWidth;el.classList.add('no')};
const wait=(st,f)=>{P.fx.done=false;P.fx.cta=()=>{if(!P.fx.done)return true;return false}};
const finish=(label)=>{P.fx.done=true;cta(label||'Continuar',true,true);try{sfx('cheer')}catch(e){}};
const fb=(ok,why,right)=>fxGrade(ok,why,right);
const TONE={balloons:['#d9f3ff','#ffe0f1'],puzzle:['#ffe9b8','#ffd0e0'],mystery:['#d9d4ff','#ffe3b8'],paraphrase:['#c9f1ff','#e6f9d8'],voices:['#ffd9c9','#e3d4ff'],chain:['#cdf3e6','#d7e6ff'],upgrade:['#fff0b8','#ffd6d6'],rhetoric:['#d9e4ff','#ffe0f1'],editor:['#e6dcff','#fff0c9'],ctxword:['#d2f5ea','#fff2c2'],form:['#ffe9b8','#d9f3ff']};
const ban=f=>f.ban&&f.ban.length?`<div class="nv-ban" style="--a:${(TONE[f.k]||['#d9f3ff','#fff'])[0]};--b:${(TONE[f.k]||['#d9f3ff','#fff'])[1]}">${f.ban.map((e,i)=>`<span style="--i:${i}">${e}</span>`).join('')}</div>`:'';
const pt=t=>t?`<small class="nv-pt">🇧🇷 ${H(t)}</small>`:'';
const shell=(f,n,cls,head,body)=>`<div class="step fx nv ${cls}">${fxKindBar(f,n)}<h2 class="fx-h">${H(f.title||L[f.k])}${head||''}</h2>${ban(f)}${body}<div id="fb"></div></div>`;
const listenBar=()=>`<div class="nv-bar"><button type="button" class="pill light" id="nvl">🔊 Ouvir</button><button type="button" class="pill light" id="nvs">🐢 Devagar</button></div>`;

/* ---------- A1 · Monte a cena ---------- */
FXR.scenebuild=function(f,st,n){
  const R=f.rounds;let ri=0,score=0;
  const draw=()=>{
    const r=R[ri];let si=0,sel=null,miss=0;const used=new Set();
    const items=fxShuffle(r.items||[...new Set(r.steps.map(s=>s[0]))]),spots=r.spots||f.spots.map((_,i)=>i);
    st.innerHTML=shell(f,n,'nv-sb',` <small>${ri+1}/${R.length}</small>`,
      fxEn('🎧','OUÇA E MONTE',H(f.intro||'Ouça as ordens e coloque cada objeto no lugar certo.'))+listenBar()+
      `<div class="nv-tiles" id="nvi">${items.map(i=>`<button type="button" class="nv-tile" data-i="${i}">${f.items[i][0]}<small>${H(f.items[i][1])}</small></button>`).join('')}</div>
       <div class="nv-tiles" id="nvp">${spots.map(i=>`<button type="button" class="nv-tile nv-spot" data-s="${i}"><span class="pl">${f.spots[i][0]}</span><span class="put" style="font-size:44px">&nbsp;</span><small>${H(f.spots[i][1])}</small></button>`).join('')}</div>
       <div id="nvt"></div>`);
    const text=r.say.join(' ');const play=slow=>say2(text,null,slow);
    q('#nvl',st).onclick=()=>play(false);q('#nvs',st).onclick=()=>play(true);setTimeout(()=>play(false),500);
    st.querySelectorAll('#nvi .nv-tile').forEach(b=>b.onclick=()=>{
      if(b.classList.contains('ok')||P.fx.done)return;
      st.querySelectorAll('#nvi .nv-tile').forEach(x=>x.classList.remove('on'));b.classList.add('on');sel=+b.dataset.i});
    st.querySelectorAll('#nvp .nv-tile').forEach(b=>b.onclick=()=>{
      if(P.fx.done||sel==null)return;const s=+b.dataset.s,need=r.steps[si];
      if(sel===need[0]&&s===need[1]){
        const it=q(`#nvi [data-i="${sel}"]`,st);it.classList.remove('on');it.classList.add('ok');it.disabled=true;
        b.classList.add('ok');q('.put',b).textContent=f.items[sel][0];sel=null;si++;sfx('key');
        q('#nvt',st).insertAdjacentHTML('beforeend',`<div class="nv-sent">${H(r.say[si-1])}${r.pt&&r.pt[si-1]?`<small>${H(r.pt[si-1])}</small>`:''}</div>`);
        if(si>=r.steps.length){if(!miss){score++;P.score++}fb(true,r.why||'Cena montada!');cta(ri<R.length-1?'Próxima cena ▶':'Continuar',true,true);P.fx.cta=()=>{if(ri<R.length-1){ri++;draw();return true}return false};}
      }else{miss++;const w=sel===need[0]?b:q(`#nvi [data-i="${sel}"]`,st);shk(w);beep(false);
        if(miss>=2){const h=q(`#nvi [data-i="${need[0]}"]`,st);if(h)h.classList.add('hint')}}
    });
    P.fx.done=false;cta('Ouça e monte a cena',false);
  };
  wait();draw();say(f.say||'Abra bem os ouvidos e monte a cena!');
};

/* ---------- A1 · Siga as ordens ---------- */
FXR.follow=function(f,st,n){
  const R=f.rounds,V=f.verb||'Touch';let ri=0;
  const nm=i=>f.tiles[i][1];
  const speak=r=>V+' '+(f.det!=null?f.det:'the ')+r.map(nm).join(f.sep||', then the ')+'.';
  const draw=()=>{
    const r=R[ri];let pos=0,miss=0;
    st.innerHTML=shell(f,n,'nv-fo',` <small>${ri+1}/${R.length}</small>`,
      fxEn('🎧','OUÇA E FAÇA NA ORDEM',H(f.intro||'Ouça as ordens e toque nas figuras na mesma ordem.'))+listenBar()+
      `<div class="nv-seq">${r.map(()=>'<i></i>').join('')}</div>
       <div class="nv-tiles">${f.tiles.map((t,i)=>`<button type="button" class="nv-tile" data-i="${i}">${t[0]}<small>${H(t[1])}</small></button>`).join('')}</div><div id="nvt"></div>`);
    const play=slow=>say2(speak(r),null,slow);
    q('#nvl',st).onclick=()=>play(false);q('#nvs',st).onclick=()=>play(true);setTimeout(()=>play(false),500);
    st.querySelectorAll('.nv-tile').forEach(b=>b.onclick=()=>{
      if(P.fx.done)return;const i=+b.dataset.i;
      if(i===r[pos]){b.classList.add('ok');sfx('key');st.querySelectorAll('.nv-seq i')[pos].classList.add('ok');pos++;
        if(pos>=r.length){if(!miss)P.score++;fb(true,'**'+speak(r)+'**');q('#nvt',st).innerHTML=`<div class="nv-sent">${H(speak(r))}</div>`;
          P.fx.done=false;cta(ri<R.length-1?'Próxima ordem ▶':'Continuar',true,true);P.fx.cta=()=>{if(ri<R.length-1){ri++;draw();return true}return false}}}
      else{miss++;beep(false);shk(b);pos=0;st.querySelectorAll('.nv-tile').forEach(x=>x.classList.remove('ok'));st.querySelectorAll('.nv-seq i').forEach(x=>x.classList.remove('ok'));
        if(miss>=2)q(`.nv-tile[data-i="${r[0]}"]`,st).classList.add('hint')}
    });
    P.fx.done=false;cta('Ouça e toque na ordem',false);
  };
  wait();draw();say(f.say||'Ouça com atenção e toque na ordem certa!');
};

/* ---------- motor de perguntas (caso, mesmo sentido) ---------- */
const oT=o=>typeof o==='string'?o:o.t, oP=o=>typeof o==='string'?'':(o.pt||''), oI=o=>typeof o==='string'?'':(o.ic||'');
function qa(f,st,n,cfg){
  const Q=f.items;let qi=0;
  const draw=()=>{
    const it=Q[qi];let tries=0;
    st.innerHTML=shell(f,n,'nv-qa',` <small>${qi+1}/${Q.length}</small>`,
      (qi===0||cfg.sticky?(cfg.top?cfg.top(f):''):'')+(cfg.head?cfg.head(it):'')+
      fxEn('❓',cfg.label||'PERGUNTA',H(it.q||cfg.q||'')+(it.qpt?`<br><small class="nv-pt on">🇧🇷 ${H(it.qpt)}</small>`:(cfg.qpt?`<br><small class="nv-pt on">🇧🇷 ${H(cfg.qpt)}</small>`:'')),1)+
      `<div class="nv-opts">${it.opts.map((o,i)=>`<button type="button" class="fx-o nv-oi" data-i="${i}">${oI(o)?`<span class="ic">${oI(o)}</span>`:''}<span class="tx"><b>${B(oT(o))}</b>${pt(oP(o))}</span></button>`).join('')}</div>`);
    const fxp=q('#fxp',st);if(fxp)fxp.onclick=()=>say2(cfg.speak?cfg.speak(it):it.q);
    st.querySelectorAll('[data-say]').forEach(b=>b.onclick=()=>say2(b.dataset.say));
    st.querySelectorAll('.fx-o').forEach(b=>b.onclick=()=>{
      if(P.fx.done)return;const i=+b.dataset.i;
      if(i!==it.a){tries++;b.disabled=true;b.classList.add('no');beep(false);fb(false,tries>1&&it.hint?it.hint:'Leia com calma e tente de novo.',null);return}
      st.querySelectorAll('.fx-o').forEach((x,j)=>{x.disabled=true;if(j===it.a)x.classList.add('ok')});
      if(!tries)P.score++;fb(true,it.why||'',null);
      P.fx.done=false;cta(qi<Q.length-1?'Próxima ▶':'Continuar',true,true);P.fx.cta=()=>{if(qi<Q.length-1){qi++;draw();return true}return false};
    });
    P.fx.done=false;cta('Escolha a resposta',false);
  };
  wait();draw();say(f.say||'Leia com atenção e escolha.');
}
FXR.docread=function(f,st,n){
  const d=f.doc;
  qa(f,st,n,{label:'PERGUNTA',sticky:true,
    top:()=>`<div class="nv-paper"><h3><span>${d.ic||'📄'}</span>${H(d.title)}</h3>${(d.rows||[]).map(r=>`<div class="row"><span>${B(r[0])}</span><b>${B(r[1]||'')}</b></div>`).join('')}${(d.text||[]).map(t=>`<p>${B(t)}</p>`).join('')}</div>`,
    speak:it=>it.q});
};
const cl=c=>typeof c==='string'?{en:c}:c;
FXR.mystery=function(f,st,n){
  qa(f,st,n,{label:'DETETIVE · RESPONDA',sticky:true,
    top:()=>`<div class="nv-sent">${B(f.intro)}${pt(f.introPt)}</div><ul class="nv-clues">${f.clues.map(cl).map((c,i)=>`<li data-say="${H(c.en.replace(/\*\*/g,''))}"><span class="ic">${c.ic||'🔍'}</span><span class="tx"><b>${i+1}.</b> ${B(c.en)}${pt(c.pt)}</span></li>`).join('')}</ul>`,
    speak:it=>it.q});
};
FXR.paraphrase=function(f,st,n){
  qa(f,st,n,{label:'QUAL TEM O MESMO SENTIDO?',q:'Which sentence means the same?',qpt:'Qual frase tem o mesmo sentido?',
    head:it=>`<div class="nv-quote" data-say="${H(it.src)}"><span class="ic">${it.ic||'💬'}</span><span>🔊 ${H(it.src)}${pt(it.srcpt)}</span></div>`,
    speak:it=>it.src});
};

/* ---------- A2 · Estoure os balões (ouça a pista, estoure a palavra) ---------- */
FXR.balloons=function(f,st,n){
  const K=f.clues,N=K.length;let ci=0,miss=0;const COL=['#ff8fab','#ffb703','#8ecae6','#95d5b2','#c8b6ff','#ffd6a5'];
  const order=fxShuffle(f.balloons.map((_,i)=>i));
  const draw=()=>{
    const c=K[ci];let tries=0,shown=false;
    st.innerHTML=shell(f,n,'nv-bl',` <small>${ci+1}/${N}</small>`,
      fxEn('🎧','OUÇA A PISTA E ESTOURE',H(f.intro||'Ouça a pista e estoure o balão com a palavra certa.')+`<br><small class="nv-pt on">🇧🇷 ${H(f.introPt||'Ouça a pista e estoure o balão com a palavra certa.')}</small>`)+
      `<div class="nv-talk"><button type="button" class="nv-bubble" id="nvbub"><span class="spk">🔊</span><span id="nvtx">Toque para ouvir a pista</span></button></div>
       <div class="nv-bar"><button type="button" class="pill light" id="nvl">🔊 Ouvir</button><button type="button" class="pill light" id="nvs">🐢 Devagar</button><button type="button" class="pill light" id="nvtt">👁️ Ver texto</button></div>
       <div class="nv-sky">${order.map((i,j)=>{const g=f.balloons[i];return `<button type="button" class="nv-bln ${i<ci?'pop gone':''}" data-i="${i}" style="--c:${COL[j%COL.length]};--d:${(j*.37%1.8).toFixed(2)}s"><span class="b"><i>${g[0]}</i><b>${H(g[1])}</b></span></button>`}).join('')}</div>`);
    const play=slow=>say2(c.en,null,slow);
    const showT=()=>{shown=true;q('#nvtx',st).innerHTML=`${B(c.en)}${pt(c.pt)}`};
    q('#nvl',st).onclick=()=>play(false);q('#nvs',st).onclick=()=>play(true);q('#nvbub',st).onclick=()=>play(false);q('#nvtt',st).onclick=showT;
    setTimeout(()=>play(false),450);
    st.querySelectorAll('.nv-bln').forEach(b=>b.onclick=()=>{
      if(P.fx.done||b.disabled)return;const i=+b.dataset.i;say2(f.balloons[i][1]);
      if(i!==c.a){miss++;tries++;beep(false);shk(b);b.classList.add('wrong');if(tries>=2&&!shown)showT();fb(false,tries>1?(c.hint||'Leia a pista de novo.'):'Ouça a pista de novo e tente outro balão.',null);return}
      b.disabled=true;b.classList.add('pop');sfx('key');showT();
      order.splice(0,0);
      if(ci>=N-1){if(!miss)P.score++;fb(true,c.why||'Muito bem! 🎉',null);P.fx.done=true;cta('Continuar',true,true);return}
      fb(true,c.why||'Isso!',null);
      P.fx.done=false;cta('Próxima pista ▶',true,true);P.fx.cta=()=>{ci++;draw();return true}});
    P.fx.done=false;cta('Estoure o balão certo',false);
  };
  wait();draw();say(f.say||'Ouça a pista e estoure a palavra certa.');
};

/* ---------- A2 · Preencha o formulário ---------- */
FXR.form=function(f,st,n){
  const c=f.card;const ans=f.fields.map(()=>null);
  st.innerHTML=shell(f,n,'nv-fm','',
    fxEn('📝','PREENCHA',H(f.intro||'Use os dados do cartão para preencher o formulário.'))+
    `<div class="nv-card"><div class="av">${c.ic}</div><div><b>${H(c.name)}</b><ul>${c.facts.map(x=>`<li>${B(x)}</li>`).join('')}</ul></div></div>
     <div class="nv-form"><h3 style="margin:10px 0 0">${H(f.formTitle||'Form')}</h3>${f.fields.map((fl,i)=>`<div class="nv-field"><label>${H(fl.label)}</label><div class="opts">${fl.opts.map((o,j)=>`<button type="button" class="nv-pill" data-f="${i}" data-o="${j}">${H(o)}</button>`).join('')}</div></div>`).join('')}</div>`);
  let checked=false;
  st.querySelectorAll('.nv-pill').forEach(b=>b.onclick=()=>{
    if(checked)return;const i=+b.dataset.f;ans[i]=+b.dataset.o;
    st.querySelectorAll(`.nv-pill[data-f="${i}"]`).forEach(x=>x.classList.toggle('on',x===b));
    cta('Conferir',ans.every(a=>a!=null),true)});
  wait();P.fx.cta=()=>{
    if(!checked){checked=true;let bad=0;
      f.fields.forEach((fl,i)=>{const bs=st.querySelectorAll(`.nv-pill[data-f="${i}"]`);bs.forEach((x,j)=>{x.classList.remove('on');if(j===fl.a)x.classList.add('ok');else if(j===ans[i])x.classList.add('no')});if(ans[i]!==fl.a)bad++});
      if(!bad)P.score++;fb(!bad,bad?f.fields.filter((fl,i)=>ans[i]!==fl.a).map(fl=>fl.why).filter(Boolean).join(' '):(f.ok||'Formulário perfeito!'),null);
      P.fx.done=true;cta('Continuar',true,true);return true}
    return false};
  cta('Preencha todos os campos',false);say(f.say||'Leia o cartão e preencha cada campo.');
};

/* ---------- B2 · Quem pensa o quê? (uma pessoa por vez, rostos) ---------- */
FXR.voices=function(f,st,n){
  const S=f.speakers,N=S.length;let ri=0,score=0;
  const draw=()=>{
    const s=S[ri];let miss=0,shown=false;
    st.innerHTML=shell(f,n,'nv-vo',` <small>${ri+1}/${N}</small>`,
      fxEn('🎧','OUÇA E DESCUBRA',H(f.intro||'Ouça a pessoa. Como ela se sente sobre o assunto? Escolha o rosto.')+(f.introPt?`<br><small class="nv-pt on">🇧🇷 ${H(f.introPt)}</small>`:''))+
      `<div class="nv-sent">📌 ${H(f.topic)}${pt(f.topicPt)}</div>
       <div class="nv-people-row">${S.map((x,i)=>`<span class="nv-dot ${i<ri?'ok':i===ri?'on':''}">${x.ic}</span>`).join('')}</div>
       <div class="nv-talk"><div class="av" id="nvav">${s.ic}<b>${H(s.n)}</b></div><button type="button" class="nv-bubble" id="nvbub"><span class="spk">🔊</span><span id="nvtx">Toque para ouvir ${H(s.n)}</span></button></div>
       <div class="nv-bar"><button type="button" class="pill light" id="nvl">🔊 Ouvir</button><button type="button" class="pill light" id="nvs">🐢 Devagar</button><button type="button" class="pill light" id="nvtt">👁️ Ver texto</button></div>
       <div class="nv-faces">${f.stances.map((x,i)=>`<button type="button" class="nv-face" data-i="${i}"><span class="fc">${x[0]}</span><b>${H(x[1])}</b><small>${H(x[2]||'')}</small></button>`).join('')}</div>`);
    const play=slow=>{const a=q('#nvav',st);if(!a)return;a.classList.add('talk');setTimeout(()=>a.classList.remove('talk'),Math.max(2200,s.line.length*90));say2(s.line,s.n,slow)};
    q('#nvl',st).onclick=()=>play(false);q('#nvs',st).onclick=()=>play(true);q('#nvbub',st).onclick=()=>play(false);
    const showT=()=>{shown=true;q('#nvtx',st).innerHTML=`${H(s.line)}${pt(s.pt)}`};
    q('#nvtt',st).onclick=showT;setTimeout(()=>play(false),500);
    st.querySelectorAll('.nv-face').forEach(b=>b.onclick=()=>{
      if(P.fx.done)return;const i=+b.dataset.i;
      if(i!==s.a){miss++;b.disabled=true;b.classList.add('no');beep(false);fb(false,miss>1?'Dica: '+(s.hint||'ouça o tom da voz e as palavras-chave.'):'Ouça de novo: o tom da voz mostra o que a pessoa sente.',null);return}
      st.querySelectorAll('.nv-face').forEach((x,j)=>{x.disabled=true;if(j===s.a)x.classList.add('ok')});showT();
      if(!miss){score++;P.score++}fb(true,s.why||'',null);
      P.fx.done=false;cta(ri<N-1?'Próxima pessoa ▶':'Continuar',true,true);P.fx.cta=()=>{if(ri<N-1){ri++;draw();return true}return false}});
    P.fx.done=false;cta('Escolha o rosto',false);
  };
  wait();draw();say(f.say||'Ouça cada pessoa e descubra como ela se sente.');
};

/* ---------- B2 · Cadeia de causas (trilha numerada) ---------- */
FXR.chain=function(f,st,n){
  const K=f.links.map(cl),N=K.length;let pos=0,miss=0;
  st.innerHTML=shell(f,n,'nv-ch','',
    fxEn('🔗','MONTE A TRILHA',H(f.intro||'Coloque as cartas na ordem: o que acontece primeiro, depois, depois…')+`<br><small class="nv-pt on">🇧🇷 ${H(f.introPt||'Toque na carta que vem primeiro; depois na seguinte, até o final.')}</small>`)+
    `<div class="nv-sent">❓ ${H(f.topic)}${pt(f.topicPt)}</div>
     <div class="nv-track" id="nvc">${K.map((_,i)=>`<div class="nv-slotn" data-p="${i}"><i>${i+1}</i><span class="em">${i===0?'Começo':i===N-1?'Resultado':'Depois'}</span></div>${i<N-1?`<span class="cn">↓ ${H((f.conn||[])[i]||'')}</span>`:''}`).join('')}</div>
     <h3 class="nv-h3">Cartas</h3>
     <div class="nv-opts">${fxShuffle(K.map((_,i)=>i)).map(i=>`<button type="button" class="fx-o nv-oi" data-i="${i}"><span class="ic">${K[i].ic||'🔹'}</span><span class="tx"><b>${H(K[i].en)}</b>${pt(K[i].pt)}</span></button>`).join('')}</div>`);
  st.querySelectorAll('.fx-o').forEach(b=>b.onclick=()=>{
    if(P.fx.done||b.disabled)return;const i=+b.dataset.i;
    if(i===pos){b.disabled=true;b.classList.add('ok');b.style.display='none';
      const sl=q(`.nv-slotn[data-p="${pos}"]`,st);sl.classList.add('ok');sl.innerHTML=`<i>${pos+1}</i><span class="ic">${K[i].ic||'🔹'}</span><span class="tx"><b>${H(K[i].en)}</b>${pt(K[i].pt)}</span>`;
      say2(K[i].en);pos++;sfx('key');
      if(pos>=N){if(!miss)P.score++;fb(true,f.why||'Trilha completa!',null);P.fx.done=true;cta('Continuar',true,true)}}
    else{miss++;beep(false);shk(b);if(miss>=2){const h=q(`.fx-o[data-i="${pos}"]`,st);if(h)h.classList.add('hint')}}});
  wait();cta('Monte a trilha',false);say(f.say||'Qual coisa vem primeiro? E qual é a consequência?');
};

/* ---------- C1 · Melhore o rascunho ---------- */
FXR.upgrade=function(f,st,n){
  const parts=f.parts;const weak=parts.map((p,i)=>typeof p==='object'?i:-1).filter(i=>i>=0);let fixed=0,miss=new Set();
  const txt=()=>parts.map((p,i)=>typeof p==='string'?H(p):`<button type="button" class="nv-weak ${p.done?'fixed':''}" data-i="${i}">${H(p.done?p.opts[p.a]:p.w)}</button>`).join('');
  st.innerHTML=shell(f,n,'nv-up','',
    fxEn('✍️','MELHORE',H(f.intro||'Toque nos trechos amarelos e escolha a versão mais precisa.'))+
    `<div class="nv-draft" id="nvd">${txt()}</div><div class="nv-bar"><button type="button" class="pill light" id="nvl">🔊 Ouvir o parágrafo</button></div><div id="nvo"></div>`);
  const full=()=>parts.map(p=>typeof p==='string'?p:(p.done?p.opts[p.a]:p.w)).join('');
  const redraw=()=>{q('#nvd',st).innerHTML=txt();bind()};
  q('#nvl',st).onclick=()=>say2(full());
  const bind=()=>st.querySelectorAll('.nv-weak').forEach(b=>b.onclick=()=>{
    const i=+b.dataset.i,p=parts[i];if(p.done)return;
    st.querySelectorAll('.nv-weak').forEach(x=>x.classList.toggle('on',x===b));
    const o=q('#nvo',st);o.innerHTML=`<div class="nv-opts">${p.opts.map((x,j)=>`<button type="button" class="fx-o" data-j="${j}"><b>${H(x)}</b></button>`).join('')}</div>`;
    o.querySelectorAll('.fx-o').forEach(bb=>bb.onclick=()=>{
      const j=+bb.dataset.j;
      if(j!==p.a){bb.disabled=true;bb.classList.add('no');beep(false);miss.add(i);fb(false,p.hints&&p.hints[j]?p.hints[j]:'Essa versão não encaixa tão bem. Pense no tom e na precisão.',null);return}
      p.done=true;fixed++;o.innerHTML='';fb(true,p.why,null);redraw();
      if(fixed>=weak.length){if(!miss.size)P.score++;P.fx.done=true;say2(full());cta('Continuar',true,true)}});
  });
  bind();wait();cta('Melhore todos os trechos',false);say(f.say||'Quais palavras podem ficar mais precisas?');
};

/* ---------- C1 · Marque a retórica (uma frase por vez, ícones) ---------- */
FXR.rhetoric=function(f,st,n){
  const T=f.tags;const items=[];f.paras.forEach(p=>p.s.forEach(s=>items.push({who:p.who,ic:p.ic||'💬',t:s[0],pt:s[3]||'',a:s[1],why:s[2]})));
  const N=items.length;let ri=0;
  const draw=()=>{
    const it=items[ri];let miss=0;
    st.innerHTML=shell(f,n,'nv-rh',` <small>${ri+1}/${N}</small>`,
      fxEn('🔎','QUAL É O RECURSO?',H(f.intro||'Leia a frase e toque no ícone do recurso que o autor usa.')+(f.introPt?`<br><small class="nv-pt on">🇧🇷 ${H(f.introPt)}</small>`:''))+
      `<div class="nv-sent">📌 ${H(f.topic)}${pt(f.topicPt)}</div>
       <div class="nv-people-row">${items.map((x,i)=>`<span class="nv-dot ${i<ri?'ok':i===ri?'on':''}">${i<ri?'✔':i+1}</span>`).join('')}</div>
       <button type="button" class="nv-bubble big" id="nvbub"><span class="spk">${it.ic}</span><span><b class="who">${H(it.who)}</b>${H(it.t)}${pt(it.pt)}</span></button>
       <div class="nv-faces">${T.map((x,i)=>`<button type="button" class="nv-face" data-i="${i}"><span class="fc">${x[0]}</span><b>${H(x[1])}</b><small>${H(x[2]||'')}</small></button>`).join('')}</div>`);
    q('#nvbub',st).onclick=()=>say2(it.t);setTimeout(()=>say2(it.t),400);
    st.querySelectorAll('.nv-face').forEach(b=>b.onclick=()=>{
      if(P.fx.done)return;const i=+b.dataset.i;
      if(i!==it.a){miss++;b.disabled=true;b.classList.add('no');beep(false);fb(false,miss>1?'Dica: procure a palavra-chave da frase (número, emoção, “always”, “perhaps”…).':'Quase! Releia a frase e pense no efeito que ela causa.',null);return}
      st.querySelectorAll('.nv-face').forEach((x,j)=>{x.disabled=true;if(j===it.a)x.classList.add('ok')});
      if(!miss)P.score++;fb(true,it.why,null);
      P.fx.done=false;cta(ri<N-1?'Próxima frase ▶':'Continuar',true,true);P.fx.cta=()=>{if(ri<N-1){ri++;draw();return true}return false}});
    P.fx.done=false;cta('Escolha o recurso',false);
  };
  wait();draw();say(f.say||'Que recurso o autor usa em cada frase?');
};

/* ---------- C2 · Você é o editor ---------- */
FXR.editor=function(f,st,n){
  const S=f.sents;const bad=S.map((s,i)=>s.d!=null?i:-1).filter(i=>i>=0);let flag=new Set(),stage=1,cls=0,miss=0;
  st.innerHTML=shell(f,n,'nv-ed','',
    fxEn('🕵️','ETAPA 1 · FAREJE OS DEFEITOS',H(f.intro||'Este parágrafo esconde 3 frases que um editor mudaria. Toque nelas.'))+
    `<div id="nvs">${S.map((s,i)=>`<div class="nv-sn" data-i="${i}"><i>${i+1}</i><span>${H(s.t)}</span></div>`).join('')}</div><div id="nvo"></div>`);
  const rows=()=>st.querySelectorAll('.nv-sn');
  rows().forEach(r=>r.onclick=()=>{
    if(stage!==1)return;const i=+r.dataset.i;flag.has(i)?flag.delete(i):flag.add(i);r.classList.toggle('flag',flag.has(i));
    cta('Conferir marcações',flag.size>0,true)});
  const stage2=()=>{
    stage=2;const todo=bad.slice();
    q('.fx-en-t small',st).textContent='ETAPA 2 · QUE MONSTRINHO É ESTE?';q('.fx-en-t p',st).textContent='Cada defeito tem um monstrinho. Descubra qual deles atacou a frase.';
    const o=q('#nvo',st);
    const show=()=>{
      const i=todo[cls];if(i==null)return;rows().forEach(r=>r.classList.toggle('flag',+r.dataset.i===i&&!r.classList.contains('ok')));
      o.innerHTML=`<div class="nv-sent">${H(S[i].t)}</div><div class="nv-faces">${f.types.map((t,j)=>`<button type="button" class="nv-face" data-j="${j}"><span class="fc">${t[0]}</span><b>${H(t[1])}</b><small>${H(t[2]||'')}</small></button>`).join('')}</div>`;
      o.querySelectorAll('.nv-face').forEach(b=>b.onclick=()=>{
        const j=+b.dataset.j;if(j!==S[i].d){miss++;b.disabled=true;b.classList.add('no');beep(false);fb(false,'Hmm, não foi esse monstrinho! Leia de novo e veja o que incomoda na frase.',null);return}
        const r=q(`.nv-sn[data-i="${i}"]`,st);r.classList.remove('flag');r.classList.add('ok');q('span',r).innerHTML=`<s style="opacity:.55">${H(S[i].t)}</s><br><b>✨ ${H(S[i].fix)}</b>`;
        fb(true,S[i].why,null);cls++;
        if(cls>=todo.length){if(!miss)P.score++;o.innerHTML='';fb(true,'🎉 Parágrafo salvo! Os 3 monstrinhos foram derrotados e o texto ganhou voz própria.',null);P.fx.done=true;cta('Continuar',true,true)}else show()})};
    show()};
  wait();P.fx.cta=()=>{
    if(stage===1&&!P.fx.done){
      let hit=0,fp=0;rows().forEach(r=>{const i=+r.dataset.i,isBad=bad.includes(i),fl=flag.has(i);r.classList.remove('flag');
        if(isBad&&fl){hit++;r.classList.add('ok')}else if(isBad){r.classList.add('no')}else if(fl){fp++;r.classList.add('no')}});
      miss+=Math.abs(bad.length-hit)+fp;
      fb(hit===bad.length&&!fp,hit===bad.length&&!fp?'🕵️ Faro perfeito! Você achou os 3.':'Você achou '+hit+' de '+bad.length+(fp?' e marcou '+fp+' frase boa':'')+'. As frases com defeito foram destacadas.',null);
      rows().forEach(r=>{r.classList.remove('no','ok');if(bad.includes(+r.dataset.i))r.classList.add('flag')});
      cta('Etapa 2: caçar os monstrinhos',true,true);stage=1.5;return true}
    if(stage===1.5){stage2();cta('Escolha o monstrinho',false);return true}
    return P.fx.done?false:true};
  cta('Marque as frases com defeito',false);say(f.say||'Você é o editor. Quais frases melhorariam?');
};

/* ---------- C2 · Adivinhe pelo contexto ---------- */
FXR.ctxword=function(f,st,n){
  const W=f.words;let wi=0;
  const draw=()=>{
    const w=W[wi];let shown=1,stage=1,tries=0,usetries=0;
    const render=()=>{
      st.innerHTML=shell(f,n,'nv-cw',` <small>${wi+1}/${W.length}</small>`,
        fxEn('🧩','DEDUZA O SENTIDO',H(f.intro||'Leia as pistas. Adivinhe o sentido antes de ver a resposta.'))+
        `<div class="nv-w"><span class="big">${w.ic||'🔎'}</span>${H(w.w)}<small>${H(w.pron||'')}</small></div>`+
        w.ctx.slice(0,shown).map(c=>`<div class="nv-ctx" data-say="${H(c.replace(/\*\*/g,''))}">🔊 ${B(c)}</div>`).join('')+
        (stage===1?`<div class="nv-bar">${shown<w.ctx.length?'<button type="button" class="pill light" id="nvm">➕ Mais uma pista</button>':''}</div>
          <div class="nv-opts">${w.opts.map((o,i)=>`<button type="button" class="fx-o" data-i="${i}"><b>${H(o)}</b></button>`).join('')}</div>`
        :`<div class="nv-sent">${B(w.df)}</div>${fxEn('✅','USE A PALAVRA','Qual frase usa <b>'+H(w.w)+'</b> corretamente?')}<div class="nv-opts">${w.use.map((o,i)=>`<button type="button" class="fx-o" data-u="${i}"><b>${H(o)}</b></button>`).join('')}</div>`));
      st.querySelectorAll('[data-say]').forEach(b=>b.onclick=()=>say2(b.dataset.say));
      const m=q('#nvm',st);if(m)m.onclick=()=>{shown++;render()};
      st.querySelectorAll('.fx-o[data-i]').forEach(b=>b.onclick=()=>{
        const i=+b.dataset.i;if(i!==w.a){tries++;b.disabled=true;b.classList.add('no');beep(false);return}
        stage=2;shown=w.ctx.length;sfx('key');render()});
      st.querySelectorAll('.fx-o[data-u]').forEach(b=>b.onclick=()=>{
        const i=+b.dataset.u;if(i!==w.ua){usetries++;b.disabled=true;b.classList.add('no');beep(false);return}
        st.querySelectorAll('.fx-o[data-u]').forEach((x,j)=>{x.disabled=true;if(j===w.ua)x.classList.add('ok')});
        if(!tries&&!usetries)P.score++;fb(true,w.why,null);say2(w.use[w.ua]);
        P.fx.done=false;cta(wi<W.length-1?'Próxima palavra ▶':'Continuar',true,true);P.fx.cta=()=>{if(wi<W.length-1){wi++;draw();return true}return false}});
      P.fx.done=false;if(stage===1)cta('Escolha o sentido',false);else cta('Escolha a frase correta',false)};
    render()};
  wait();draw();say(f.say||'Deduza o sentido pelas pistas, como um leitor experiente.');
};

/* ---------- Mala lexical (episódios novos): estudo + quiz de sentido ---------- */
const LXT={pv:['🔗','Phrasal verb'],id:['💡','Idiom'],sl:['😎','Gíria'],co:['🧩','Collocation'],cn:['🔀','Conector'],w:['📘','Palavra'],fx:['💬','Expressão']};
FXR.lexpack=function(f,st,n){
  const I=f.items;
  st.innerHTML=shell(f,n,'nv-lx','',
    fxEn('🎒','MALA LEXICAL',H(f.intro||'Mais blocos úteis para levar deste episódio. Toque em cada cartão para ouvir.'))+
    `<div class="nv-lxl">${I.map((x,i)=>{const t=LXT[x.t]||LXT.w;return `<button type="button" class="nv-lxc" data-i="${i}"><span class="ic">${x.ic||t[0]}</span><span class="tx"><b>${H(x.en)}</b><em>${t[0]} ${t[1]}</em><small class="pt">🇧🇷 ${H(x.pt)}</small>${x.ex?`<small class="ex">“${H(x.ex)}”</small>`:''}</span></button>`}).join('')}</div>`);
  st.querySelectorAll('.nv-lxc').forEach(b=>b.onclick=()=>{const x=I[+b.dataset.i];say2(x.ex||x.en);b.classList.add('on')});
  wait();P.fx.done=false;
  P.fx.cta=()=>{
    const pool=I.map(x=>x.pt);
    const items=I.slice(0,Math.min(5,I.length)).map((x,k)=>{
      const others=fxShuffle(pool.filter(p=>p!==x.pt)).slice(0,2);const opts=fxShuffle([x.pt,...others]);
      return {q:x.en,qpt:'',opts:opts,a:opts.indexOf(x.pt),why:'**'+x.en+'** = '+x.pt+(x.ex?'. Ex.: “'+x.ex+'”':'.'),hint:'Releia o cartão: '+(x.ex||x.en)}});
    qa({k:f.k,title:f.title,items:items,say:'O que cada bloco significa?'},st,n,{label:'O QUE SIGNIFICA?',speak:it=>it.q});
    return true};
  cta('Praticar',true,true);say(f.say||'Vamos conhecer mais blocos úteis.');
};

/* ---------- total de pontos e áudio pré-gerado ---------- */
const _ft=window.fxTotal;
window.fxTotal=function(e){let t=_ft.apply(this,arguments);try{(e.fr||[]).forEach(f=>{
  if(f.k==='scenebuild'||f.k==='follow')t+=(f.rounds||[]).length;
  else if(['mystery','paraphrase','docread'].includes(f.k))t+=(f.items||[]).length;
  else if(f.k==='voices')t+=(f.speakers||[]).length;
  else if(f.k==='rhetoric')t+=f.paras.reduce((a,p)=>a+p.s.length,0);
  else if(['form','puzzle','balloons','chain','upgrade','editor'].includes(f.k))t+=1;
  else if(f.k==='lexpack')t+=Math.min(5,(f.items||[]).length);
  else if(f.k==='ctxword')t+=(f.words||[]).length})}catch(x){}return t};
if(window.PogTTS&&PogTTS.episodeTexts){
  const o=PogTTS.episodeTexts;
  PogTTS.episodeTexts=function(e){
    const out=o.apply(this,arguments),seen=new Set(out.map(x=>x.text+'|'+(x.speaker||'')));
    const add=(t,s)=>{t=String(t||'').replace(/\*\*/g,'').trim();const k=t+'|'+(s||'');if(t&&t.length<400&&!seen.has(k)){seen.add(k);out.push({text:t,speaker:s||null})}};
    (e.fr||[]).forEach(f=>{
      if(f.k==='scenebuild')(f.rounds||[]).forEach(r=>add(r.say.join(' ')));
      if(f.k==='follow')(f.rounds||[]).forEach(r=>add((f.verb||'Touch')+' '+(f.det!=null?f.det:'the ')+r.map(i=>f.tiles[i][1]).join(f.sep||', then the ')+'.'));
      if(f.k==='docread')(f.items||[]).forEach(i=>add(i.q));
      if(f.k==='mystery'){(f.items||[]).forEach(i=>add(i.q));(f.clues||[]).forEach(c=>add(cl(c).en))}
      if(f.k==='paraphrase')(f.items||[]).forEach(i=>add(i.src));
      if(f.k==='lexpack')(f.items||[]).forEach(x=>{add(x.en);add(x.ex)});
      if(f.k==='balloons'){(f.clues||[]).forEach(c=>add(c.en));(f.balloons||[]).forEach(g=>add(g[1]))}
      if(f.k==='puzzle'){(f.clues||[]).forEach(c=>add(c[0]));(f.items||[]).forEach(i=>add(i[1]))}
      if(f.k==='voices')(f.speakers||[]).forEach(s=>add(s.line,s.n));
      if(f.k==='chain')(f.links||[]).forEach(l=>add(cl(l).en));
      if(f.k==='upgrade')add((f.parts||[]).map(p=>typeof p==='string'?p:p.opts[p.a]).join(''));
      if(f.k==='rhetoric')(f.paras||[]).forEach(p=>p.s.forEach(s=>add(s[0])));
      if(f.k==='ctxword')(f.words||[]).forEach(w=>{(w.ctx||[]).forEach(c=>add(c));add(w.use[w.ua])});
    });
    return out;
  };
}
})();
