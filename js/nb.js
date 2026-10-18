/* Neighbors — quadros próprios (visual moderno + jogos): nbhero, nbchat, nbtap, nbswap, nbmatch, nbreply, nbshadow */
(function(){
if(typeof FXR==='undefined'||typeof FX_KIND==='undefined')return;
const L={nbhero:'Seu vizinho',nbchat:'Papo no chat',nbtap:'Ouça e toque',nbswap:'Caça-níveis de frases',nbmatch:'Memória de palavras',nbreply:'Resposta rápida',nbshadow:'Fale em voz alta',nbslang:'Chat de gírias',nbctx:'Em que contexto?',nbvocab:'Soletrando',nbfind:'Caça-palavras'};
Object.keys(L).forEach(k=>{FX_KIND[k]='practice';FX_LABEL[k]=L[k]});
const q=(s,r)=>(r||document).querySelector(s);
const H=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const RJ=()=>{try{return localStorage.getItem('pogglot:romaji')!=='0'}catch(e){return true}};
const rjh=l=>l&&l[3]?`<em class="nb-rj">${H(l[3])}</em>`:'';
const isJa=()=>{try{return /japon/.test(fxLang())}catch(e){return false}};
const rjInit=(st,L)=>{const root=q('.nbx',st);if(root)root.classList.toggle('nb-nor',!RJ());const b=q('#nbrj',st);if(b){b.classList.toggle('on',RJ());b.onclick=()=>{const on=!RJ();try{localStorage.setItem('pogglot:romaji',on?'1':'0')}catch(_){}root.classList.toggle('nb-nor',!on);b.classList.toggle('on',on)}}};
const say2=(t,who,slow)=>{try{fxSay(String(t),who,slow)}catch(e){}};
const win=(label)=>{P.fx.done=true;P.score++;try{sfx('tada');confetti(60)}catch(e){}cta(label||'Continuar',true,true)};
const lock=()=>{P.fx.done=false;P.fx.cta=()=>!P.fx.done};
const css=document.createElement('style');css.textContent=`
.nbx{--g1:#6C5CE7;--g2:#FF7AA8;padding-bottom:12px}
.nbx .nb-card{border-radius:26px;background:#fff;box-shadow:0 10px 30px rgba(40,30,90,.12);padding:16px;margin:10px 0}
.nb-poster{position:relative;overflow:hidden;border-radius:30px;color:#fff;padding:26px 20px 20px;min-height:340px;background:linear-gradient(155deg,var(--g1),var(--g2));box-shadow:0 18px 40px rgba(60,40,120,.28)}
.nb-poster:before{content:"";position:absolute;inset:-40% -30% auto auto;width:300px;height:300px;border-radius:50%;background:rgba(255,255,255,.16)}
.nb-poster .nb-no{display:inline-block;font:800 11px/1 system-ui;letter-spacing:.14em;background:rgba(255,255,255,.22);border-radius:99px;padding:7px 11px}
.nb-poster .nb-big{font-size:92px;line-height:1;margin:14px 0 4px;filter:drop-shadow(0 8px 12px rgba(0,0,0,.25));animation:nbf 3s ease-in-out infinite}
.nb-poster h2{margin:0;font:900 34px/1.05 system-ui;color:#fff}.nb-poster p{margin:6px 0 0;opacity:.92;font-weight:600}
.nb-float{position:absolute;z-index:0;pointer-events:none;font-size:28px;opacity:.9;animation:nbf 3.4s ease-in-out infinite}
.nb-mis{position:relative;z-index:1;margin-top:16px;background:rgba(255,255,255,.2);backdrop-filter:blur(6px);border-radius:18px;padding:12px 14px;font-weight:700;font-size:14.5px}
.nb-mis small{display:block;opacity:.8;font-weight:800;letter-spacing:.1em;margin-bottom:3px;font-size:10.5px}
.nb-hook{position:relative;z-index:1;margin-top:12px;width:100%;border:0;border-radius:99px;padding:13px;background:#fff;color:#3b2f8f;font:800 15px system-ui;box-shadow:0 8px 18px rgba(0,0,0,.18)}
@keyframes nbf{50%{transform:translateY(-9px) rotate(3deg)}}
.nb-chat{display:flex;flex-direction:column;gap:10px;margin:12px 0}
.nb-row{display:flex;gap:8px;align-items:flex-end;animation:nbin .35s ease both}.nb-row.me{flex-direction:row-reverse}
.nb-av{flex:none;width:36px;height:36px;border-radius:50%;display:grid;place-items:center;font-size:20px;box-shadow:0 3px 8px rgba(0,0,0,.15)}
.nb-b{max-width:78%;border-radius:20px 20px 20px 6px;padding:10px 13px;background:#fff;box-shadow:0 4px 14px rgba(40,30,90,.1);cursor:pointer;font-weight:700;font-size:16px;line-height:1.35;color:#25203f}
.nb-row.me .nb-b{border-radius:20px 20px 6px 20px;background:linear-gradient(135deg,var(--g1),var(--g2));color:#fff}
.nb-rj{display:block;font:600 12px system-ui;opacity:.75;font-style:normal;margin-top:2px;letter-spacing:.02em}.nb-nor .nb-rj{display:none}.nb-rj2{display:block;font:600 14px system-ui;opacity:.7;font-style:normal;margin-top:4px}.nb-nor .nb-rj2{display:none}
.nb-b small{display:none;margin-top:4px;font-weight:600;opacity:.85;font-size:12.5px}.nb-pt .nb-b small{display:block}
.nb-b .nb-who{display:block;font:800 10px system-ui;letter-spacing:.08em;opacity:.6;margin-bottom:2px}
@keyframes nbin{from{opacity:0;transform:translateY(10px) scale(.96)}}
.nb-tools{display:flex;gap:8px;flex-wrap:wrap}.nb-chip{border:0;border-radius:99px;padding:9px 14px;background:#fff;box-shadow:0 3px 10px rgba(40,30,90,.12);font:800 13px system-ui;color:#4a3fb0}
.nb-chip.on{background:#4a3fb0;color:#fff}
.nb-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:12px 0}
.nb-opt{border:0;border-radius:22px;background:#fff;box-shadow:0 6px 16px rgba(40,30,90,.12);padding:14px 6px;font:800 14px system-ui;color:#25203f;transition:.2s}
.nb-opt b{display:block;font-size:38px;margin-bottom:4px}.nb-opt.ok{background:#c9f5dc;transform:scale(1.05)}.nb-opt.no{background:#ffd9de;animation:nbs .35s}
@keyframes nbs{25%{transform:translateX(-6px)}75%{transform:translateX(6px)}}
.nb-big-line{font:900 22px/1.25 system-ui;color:#25203f;text-align:center;margin:12px 6px 4px;min-height:58px}
.nb-big-line em{display:block;font:600 13px system-ui;opacity:.6;margin-top:4px}
.nb-reel{display:flex;gap:8px;overflow-x:auto;padding:4px 2px 8px;scrollbar-width:none}.nb-reel::-webkit-scrollbar{display:none}
.nb-reel button{flex:none;border:0;border-radius:16px;padding:11px 14px;background:#fff;box-shadow:0 4px 12px rgba(40,30,90,.12);font:800 14px system-ui;color:#25203f}
.nb-reel button.on{background:linear-gradient(135deg,var(--g1),var(--g2));color:#fff}
.nb-prog{display:flex;gap:6px;justify-content:center;margin:6px 0}.nb-prog i{width:14px;height:14px;border-radius:50%;background:#ddd7f5}.nb-prog i.on{background:#ffb703;transform:scale(1.2)}
.nb-mem{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:12px 0}
.nb-mc{aspect-ratio:1/1.05;border:0;border-radius:20px;font:900 15px system-ui;background:linear-gradient(135deg,var(--g1),var(--g2));color:#fff;box-shadow:0 6px 16px rgba(40,30,90,.2);perspective:600px;transition:transform .25s}
.nb-mc.up{background:#fff;color:#25203f}.nb-mc.up b{font-size:40px;display:block}.nb-mc.done{background:#c9f5dc;color:#17613a}
.nb-streak{text-align:center;font:900 18px system-ui;color:#ff7a00;min-height:26px}
.nb-mic{display:grid;place-items:center;margin:8px auto;width:92px;height:92px;border-radius:50%;border:0;font-size:40px;background:linear-gradient(135deg,var(--g1),var(--g2));color:#fff;box-shadow:0 0 0 8px rgba(108,92,231,.15);animation:nbp 2s infinite}
@keyframes nbp{50%{box-shadow:0 0 0 16px rgba(108,92,231,.05)}}
.nb-rate{display:flex;gap:10px;justify-content:center;margin:10px 0}.nb-rate button{border:0;background:#fff;border-radius:20px;padding:10px 14px;font-size:30px;box-shadow:0 4px 12px rgba(40,30,90,.12)}
.nb-b mark{background:#ffe27a;color:#3b2f00;border-radius:7px;padding:0 4px;font-weight:900;border-bottom:2px solid #ffb703}.nb-row.me .nb-b mark{background:#ffe27a;color:#3b2f00}
.nb-gl{background:#fff8dc;border-radius:18px;padding:10px 13px;margin:8px 0;font-weight:700;font-size:14px;color:#4a3a00;box-shadow:0 4px 12px rgba(255,183,3,.2)}
.nb-sit{font:800 18px/1.3 system-ui;color:#25203f;text-align:center;margin:8px 4px}.nb-sit b{display:block;font-size:56px}
.nb-lt{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin:12px 0}.nb-lt button{width:46px;height:52px;border:0;border-radius:14px;background:#fff;box-shadow:0 4px 12px rgba(40,30,90,.15);font:900 22px system-ui;text-transform:uppercase;color:#25203f}.nb-lt button.used{opacity:.25}
.nb-sl{display:flex;gap:6px;justify-content:center;flex-wrap:wrap;margin:10px 0}.nb-sl span{width:42px;height:50px;border-radius:12px;background:#ece9ff;display:grid;place-items:center;font:900 22px system-ui;text-transform:uppercase;color:#25203f}.nb-sl.ok span{background:#c9f5dc}.nb-sl.no span{background:#ffd9de}
.nb-ws{display:grid;gap:4px;margin:10px auto;max-width:340px;touch-action:manipulation}.nb-ws button{aspect-ratio:1;border:0;border-radius:9px;background:#fff;box-shadow:0 2px 6px rgba(40,30,90,.14);font:900 17px system-ui;text-transform:uppercase;color:#25203f;padding:0}.nb-ws button.sel{background:#ffe27a}.nb-ws button.fd{background:#c9f5dc;color:#17613a}
.nb-clues{display:flex;gap:8px;flex-wrap:wrap;justify-content:center}.nb-clues span{background:#fff;border-radius:14px;padding:7px 11px;font-weight:800;font-size:13.5px;box-shadow:0 3px 9px rgba(40,30,90,.1)}.nb-clues span.fd{background:#c9f5dc;text-decoration:none}
.nb-hint{text-align:center;font-weight:700;opacity:.7;font-size:13px}
.nbx mark.x,.nbx mark.e{display:inline!important;width:auto!important;height:auto!important;min-width:0!important;border-radius:7px!important;transition:none!important;font-size:inherit!important;line-height:inherit!important;place-items:normal!important;border-width:0 0 2px!important;white-space:normal!important}.nbx .nb-tag.x,.nbx .nb-tag.e{display:inline-block!important;width:auto!important;height:auto!important;border-radius:99px!important;font-size:11px!important;transition:none!important}.nb-b mark.x{background:#dff1ff;border-bottom-color:#5aa9e6;color:#0b3a5e}.nb-tag{display:inline-block;border-radius:99px;padding:2px 9px;font:800 11px system-ui;margin-right:6px}.nb-tag.e{background:#ffe27a;color:#5a4200}.nb-tag.x{background:#dff1ff;color:#0b3a5e}
.nb-real{background:#fff;border-radius:22px;padding:12px 14px;margin:8px 0;box-shadow:0 6px 16px rgba(40,30,90,.1);text-align:center}.nb-real .w{font:700 15px system-ui;opacity:.65;text-decoration:line-through}.nb-real .s{font:900 22px system-ui;color:#4a3fb0;margin:4px 0}.nb-real small{display:block;font:600 12.5px system-ui;opacity:.75}
.nb-sp{background:#fff;border-radius:22px;padding:10px 12px;margin:8px 0;box-shadow:0 6px 16px rgba(40,30,90,.12)}
.nb-rep{display:inline-block;background:#fff1d6;color:#7a4a00;border-radius:99px;padding:3px 10px;font:800 11px system-ui;margin-bottom:4px}
`;document.head.appendChild(css);
const av=(em,nm,col)=>{try{return window.PogFace?PogFace.avatar(em,nm,col):em}catch(e){return em}};
const theme=f=>`style="--g1:${(f.g||['#6C5CE7','#FF7AA8'])[0]};--g2:${(f.g||['#6C5CE7','#FF7AA8'])[1]}"`;
const head=(f,n,t)=>`${fxKindBar(f,n)}<h2 class="fx-h">${H(f.title||t)}</h2>`;

/* 1 · pôster do vizinho */
FXR.nbhero=function(f,st,n){
  const fl=(f.emo||[]).map((e,i)=>`<span class="nb-float" style="top:${14+i*32}px;right:${14+(i%2)*40}px;animation-delay:${i*.5}s">${e}</span>`).join('');
  st.innerHTML=`<div class="step fx nbx" ${theme(f)}>${fxKindBar(f,n)}<div class="nb-poster">${fl}<span class="nb-no">VIZINHO Nº ${f.num} · ${H(f.lvl)}</span>${(()=>{try{const e=(typeof P!=='undefined'&&P)?P.e:null;if(e&&window.PogCover)return `<div class="nb-scene">${PogCover.svg(e)}</div>`}catch(x){}return `<div class="nb-big">${f.face}</div>`})()}<h2>${H(f.name)}</h2><p>${H(f.city)} · ${H(f.sub)}</p><div class="nb-mis"><small>SUA MISSÃO</small>${H(f.mission)}</div><button class="nb-hook" id="nbh">🔊 “${H(f.hook[0])}”</button></div><div class="nb-hint">${H(f.hook[1])}</div></div>`;
  q('#nbh',st).onclick=()=>say2(f.hook[0],f.name);
  cta('Conhecer o vizinho',true);say('Esse é seu novo vizinho!')};

/* 2/5 · diálogo em bolhas de chat */
FXR.nbchat=function(f,st,n){
  const cast=f.cast,L=f.lines;let k=0,pt=false,role=!!f.role&&!!(window.PogVoice);
  const isMe=l=>l[0]==='You'||l[0]===f.me;
  st.innerHTML=`<div class="step fx nbx" ${theme(f)}>${head(f,n,'Papo no chat')}<div class="nb-tools"><button class="nb-chip" id="nbpt">🇧🇷 Tradução</button><button class="nb-chip" id="nbal">🔊 Ouvir tudo</button>${L.some(l=>l[3])?'<button class="nb-chip on" id="nbrj">あ/a Romaji</button>':''}${f.role?'<button class="nb-chip on" id="nbrl">🎭 Eu falo minhas falas</button>':''}<button class="nb-chip" id="nbrp">🚩 Algo errado?</button></div><div class="nb-chat" id="nbc"></div><div id="nbsp"></div><div class="nb-hint" id="nbhn">${H(f.intro||'Toque em “Próxima fala” para abrir cada mensagem.')}</div></div>`;
  const box=q('#nbc',st);let seq=0;rjInit(st,L);
  const add=(i,speak)=>{const l=L[i],me=isMe(l),c=cast[l[0]]||['🙂','#999'];
    const r=document.createElement('div');r.className='nb-row'+(me?' me':'');
    r.innerHTML=`<span class="nb-av" style="background:${c[1]}22">${av(c[0],l[0],c[1])}</span><div class="nb-b"><span class="nb-who">${H(l[0]==='You'?'VOCÊ':l[0])}</span>${H(l[1])}${rjh(l)}<small>${H(l[2])}</small></div>`;
    r.querySelector('.nb-b').onclick=()=>say2(l[1],l[0]);box.appendChild(r);r.scrollIntoView({block:'nearest',behavior:'smooth'});if(speak)say2(l[1],l[0])};
  const after=()=>{if(k>=L.length){cta('Continuar',true,true);q('#nbhn',st).textContent='Toque em qualquer bolha para ouvir de novo.'}else cta('Próxima fala ▶',true)};
  const reveal=i=>{q('#nbsp',st).innerHTML='';add(i,true);k=i+1;P.fx.cta=()=>{if(k<L.length){next();return true}return false};after()};
  const speakTurn=i=>{const l=L[i],w=l[1].split(' ');
    q('#nbsp',st).innerHTML=`<div class="nb-sp"><div class="nb-hint">🎭 Sua vez! Diga em ${fxLang()}:</div><div class="nb-big-line" style="min-height:0">${H(l[2])}<em>Começa com: “${H(w.slice(0,2).join(' '))}…”</em></div><div id="nbmic"></div><div class="nb-tools" style="justify-content:center"><button class="nb-chip" id="nbshow">👀 Ver a frase</button></div></div>`;
    q('#nbhn',st).textContent='';P.fx.cta=()=>true;cta('Fale sua parte 🎤',false);
    q('#nbshow',st).onclick=()=>reveal(i);
    if(PogVoice.supported())PogVoice.mount(q('#nbmic',st),{target:l[1],onDone:r=>{if(r.score>=50){setTimeout(()=>reveal(i),900)}},onFail:c=>{if(c==='unsupported'){role=false;q('#nbmic',st).innerHTML='<div class="nb-hint">Seu navegador não tem microfone: diga em voz alta e toque em “Ver a frase”.</div>'}}});
    else q('#nbmic',st).innerHTML='<div class="nb-hint">Diga em voz alta e toque em “Ver a frase”.</div>'};
  const next=()=>{if(k<L.length){if(role&&isMe(L[k])){speakTurn(k);return}add(k,true);k++;after()}};
  q('#nbpt',st).onclick=e=>{pt=!pt;box.classList.toggle('nb-pt',pt);e.currentTarget.classList.toggle('on',pt)};
  q('#nbal',st).onclick=()=>{const s=++seq;(async()=>{for(let i=0;i<k&&s===seq;i++){say2(L[i][1],L[i][0]);await new Promise(r=>setTimeout(r,1000+L[i][1].length*62))}})()};
  const rl=q('#nbrl',st);if(rl)rl.onclick=e=>{role=!role;e.currentTarget.classList.toggle('on',role);if(!role&&q('#nbsp',st).innerHTML){const i=k;q('#nbsp',st).innerHTML='';reveal(i)}};
  q('#nbrp',st).onclick=()=>reportErr(f,n,L[Math.max(0,k-1)]);
  P.fx.cta=()=>{if(k<L.length){next();return true}return false};
  next()};
const reportErr=(f,n,l)=>{try{const it={ep:(window.P&&P.e&&P.e.n)||n,t:(window.P&&P.e&&P.e.t)||'',frame:f.k,en:l&&l[1],pt:l&&l[2],at:new Date().toISOString()};const msg=prompt('O que está estranho nessa fala? (opcional)','');if(msg===null)return;it.note=msg;let a=[];try{a=JSON.parse(localStorage.getItem('nb_reports')||'[]')}catch(e){}a.push(it);try{localStorage.setItem('nb_reports',JSON.stringify(a))}catch(e){}
  try{navigator.clipboard.writeText(JSON.stringify(it))}catch(e){}alert('Anotado neste aparelho ('+a.length+' no total). Também copiei os dados para você colar numa mensagem.')}catch(e){}};

/* 3 · ouça e toque */
FXR.nbtap=function(f,st,n){
  const R=f.items;let ri=0,hits=0;lock();
  const draw=()=>{const it=R[ri],ln=it.ln||f.lines[it.line];
    st.innerHTML=`<div class="step fx nbx" ${theme(f)}>${head(f,n,'Ouça e toque')}<div class="nb-prog">${R.map((_,i)=>`<i class="${i<ri?'on':''}"></i>`).join('')}</div>
    <div class="nb-big-line">${it.rv?'<span class="nb-rep">🔁 revisão</span><br>':''}${H(it.pt)}<em>Ouça a cena e toque na resposta certa</em></div><div class="nb-tools" style="justify-content:center"><button class="nb-chip" id="nbl">🔊 Ouvir a fala</button><button class="nb-chip" id="nbs">🐢 Devagar</button></div>
    <div class="nb-grid">${it.opts.map((o,i)=>`<button class="nb-opt" data-i="${i}"><b>${o[0]}</b>${H(o[1])}</button>`).join('')}</div><div id="fb"></div></div>`;
    const play=s=>say2(ln[1],ln[0],s);q('#nbl',st).onclick=()=>play(false);q('#nbs',st).onclick=()=>play(true);setTimeout(()=>play(false),400);
    let lk=false;st.querySelectorAll('.nb-opt').forEach(b=>b.onclick=()=>{if(lk)return;const ok=+b.dataset.i===it.a;
      if(ok){lk=true;b.classList.add('ok');sfx('burst');hits++;setTimeout(()=>{ri++;if(ri<R.length)draw();else win()},700)}else{b.classList.add('no');sfx('oops')}})};
  draw();cta('Ouça e toque',false);say('Escute a fala e escolha o que combina.')};

/* 4 · caça-níveis de frases (troque as peças) */
const ptj=(a,b,end)=>{let t=(a+' '+b+(end||'')).replace(/\s+([?.!,])/g,'$1');
  const M=[[/\bem (o|a|os|as|um|uma|este|esta|estes|estas|esse|essa|aquele|aquela)\b/gi,(m,x)=>({o:'no',a:'na',os:'nos',as:'nas',um:'num',uma:'numa',este:'neste',esta:'nesta',estes:'nestes',estas:'nestas',esse:'nesse',essa:'nessa',aquele:'naquele',aquela:'naquela'}[x.toLowerCase()])],
   [/\bde (o|a|os|as|este|esta|estes|estas|esse|essa|aquele|aquela)\b/gi,(m,x)=>({o:'do',a:'da',os:'dos',as:'das',este:'deste',esta:'desta',estes:'destes',estas:'destas',esse:'desse',essa:'dessa',aquele:'daquele',aquela:'daquela'}[x.toLowerCase()])],
   [/\bpor (o|a|os|as)\b/gi,(m,x)=>({o:'pelo',a:'pela',os:'pelos',as:'pelas'}[x.toLowerCase()])],
   [/\ba (o|os|as)\b/gi,(m,x)=>({o:'ao',os:'aos',as:'às'}[x.toLowerCase()])],[/\ba a\b/gi,'à']];
  M.forEach(r=>{t=t.replace(r[0],r[1])});return t.charAt(0).toUpperCase()+t.slice(1)};
FXR.nbswap=function(f,st,n){
  const P_=f.pages;let pi=0,a=0,b=0;const heard=new Set();const GOAL=f.goal||4;lock();
  const draw=()=>{const p=P_[pi];
    st.innerHTML=`<div class="step fx nbx" ${theme(f)}>${head(f,n,'Troque as peças')}<div class="nb-tools">${P_.map((x,i)=>`<button class="nb-chip ${i===pi?'on':''}" data-p="${i}">${H(x.label)}</button>`).join('')}</div>
    <div class="nb-card"><div class="nb-big-line" id="nbsent"></div></div>
    <div class="nb-hint">1 · escolha o começo</div><div class="nb-reel" id="r1">${p.S.map((s,i)=>`<button data-i="${i}" class="${i===a?'on':''}">${H(s[0])}</button>`).join('')}</div>
    <div class="nb-hint">2 · escolha o final</div><div class="nb-reel" id="r2">${p.E.map((s,i)=>`<button data-i="${i}" class="${i===b?'on':''}">${H(s[0])}</button>`).join('')}</div>
    <div class="nb-tools" style="justify-content:center"><button class="nb-chip" id="nbr">🎲 Sortear</button><button class="nb-chip" id="nbpl">🔊 Ouvir</button></div>
    <div class="nb-hint">${H(p.tip||f.tip||'')}</div><div class="nb-prog" id="nbpr"></div></div>`;
    const sync=(speak)=>{const s=p.S[a],e=p.E[b],en=(s[0]+' '+e[0]+(p.end||'')).replace(/\s+([?.!,])/g,'$1');
      q('#nbsent',st).innerHTML=`${H(en)}<em>${H(ptj(s[1],e[1],p.end))}</em>`;
      st.querySelectorAll('#r1 button').forEach((x,i)=>x.classList.toggle('on',i===a));st.querySelectorAll('#r2 button').forEach((x,i)=>x.classList.toggle('on',i===b));
      if(speak){say2(en,null);sfx('key');heard.add(pi+'|'+a+'|'+b)}
      q('#nbpr',st).innerHTML=Array.from({length:GOAL},(_,i)=>`<i class="${i<heard.size?'on':''}"></i>`).join('');
      if(speak&&heard.size>=GOAL&&!P.fx.done){setTimeout(()=>win(),500)}else if(!P.fx.done)cta(`Monte ${Math.max(0,GOAL-heard.size)} frase(s) diferentes`,false)};
    st.querySelectorAll('#r1 button').forEach(x=>x.onclick=()=>{a=+x.dataset.i;sync(true)});st.querySelectorAll('#r2 button').forEach(x=>x.onclick=()=>{b=+x.dataset.i;sync(true)});
    q('#nbr',st).onclick=()=>{a=Math.random()*p.S.length|0;b=Math.random()*p.E.length|0;sync(true)};q('#nbpl',st).onclick=()=>sync(false)||say2(q('#nbsent',st).firstChild.textContent);
    st.querySelectorAll('[data-p]').forEach(x=>x.onclick=()=>{pi=+x.dataset.p;a=0;b=0;draw()});sync(false)};
  draw();say('Troque as peças e ouça cada frase nova.')};

/* 6 · memória de palavras */
FXR.nbmatch=function(f,st,n){
  const W=f.items.slice(0,6);lock();let cards=[];W.forEach((w,i)=>{cards.push({i,t:'e',h:`<b>${w[1]}</b>${H(w[2])}`,s:w[0]});cards.push({i,t:'w',h:`<b>🔊</b>${H(w[0])}`,s:w[0]})});cards=fxShuffle(cards);
  let open=[],found=0,tries=0,lk=false;
  st.innerHTML=`<div class="step fx nbx" ${theme(f)}>${head(f,n,'Memória de palavras')}<div class="nb-hint">Ache o par: figura em português + palavra em ${fxLang()}. Toque para ouvir.</div><div class="nb-mem">${cards.map((c,i)=>`<button class="nb-mc" data-i="${i}">?</button>`).join('')}</div><div class="nb-streak" id="nbst"></div></div>`;
  const bs=[...st.querySelectorAll('.nb-mc')];
  bs.forEach((b,i)=>b.onclick=()=>{if(lk||b.classList.contains('up')||b.classList.contains('done'))return;const c=cards[i];b.classList.add('up');b.innerHTML=c.h;say2(c.s,null);open.push(i);
    if(open.length===2){tries++;const[x,y]=open;if(cards[x].i===cards[y].i&&cards[x].t!==cards[y].t){bs[x].classList.add('done');bs[y].classList.add('done');found++;sfx('burst');open=[];q('#nbst',st).textContent=found>=W.length?`Perfeito em ${tries} jogadas!`:'🔥 Par!';if(found>=W.length)setTimeout(()=>win(),600)}
      else{lk=true;setTimeout(()=>{[x,y].forEach(j=>{bs[j].classList.remove('up');bs[j].textContent='?'});open=[];lk=false},900)}}});
  cta('Ache os pares',false);say('Vire as cartas e junte figura e palavra.')};

/* 7 · resposta rápida */
FXR.nbreply=function(f,st,n){
  const T=f.turns;let ti=0,combo=0;lock();
  const draw=()=>{const t=T[ti];
    st.innerHTML=`<div class="step fx nbx" ${theme(f)}>${head(f,n,'Resposta rápida')}<div class="nb-streak">${combo>1?'🔥 combo x'+combo:' '}</div>
    <div class="nb-chat"><div class="nb-row"><span class="nb-av" style="background:${f.npc[1]}22">${av(f.npc[0],f.npc[2],f.npc[1])}</span><div class="nb-b" id="nbn"><span class="nb-who">${H(f.npc[2])}</span>${H(t.n[0])}<small>${H(t.n[1])}</small></div></div></div>
    <div class="nb-hint">Como você responde?</div><div class="nb-chat" id="nbo">${t.o.map((o,i)=>`<div class="nb-row me"><div class="nb-b" data-i="${i}">${H(o[0])}</div></div>`).join('')}</div></div>`;
    q('#nbn',st).onclick=()=>say2(t.n[0],f.npc[2]);setTimeout(()=>say2(t.n[0],f.npc[2]),400);let lk=false;
    st.querySelectorAll('#nbo .nb-b').forEach(b=>b.onclick=()=>{if(lk)return;const i=+b.dataset.i;say2(t.o[i][0],'You');
      if(i===t.a){lk=true;combo++;b.style.background='#c9f5dc';b.style.color='#17613a';sfx('burst');setTimeout(()=>{ti++;if(ti<T.length)draw();else win()},1100)}else{combo=0;b.style.opacity=.45;sfx('oops')}})};
  draw();cta('Escolha a resposta',false);say('Responda como um local!')};

/* 8 · fale em voz alta: repita -> complete -> lembre; + "como falam de verdade" */
FXR.nbshadow=function(f,st,n){
  const R=f.items.map((it,i)=>({t:it[0],p:it[1],r:it[2],tier:['repeat','cloze','recall'][Math.min(i,2)]}));
  if(f.real)R.push({t:f.real[0],p:f.real[2],tier:'real',sp:f.real[1]});
  let ri=0;lock();
  const jmask=t=>{const a=[...t],k=Math.max(2,Math.ceil(a.length/3));return a.slice(0,Math.max(1,a.length-k-1)).join('')+'＿'.repeat(k)+(/[。！？!?]/.test(a[a.length-1])?a[a.length-1]:'')};
  const mask=t=>{if(isJa())return jmask(t);const w=t.split(' ');const sc=w.map((x,i)=>[x.replace(/[^A-Za-z']/g,'').length,i]).sort((a,b)=>b[0]-a[0]).slice(0,Math.max(1,Math.round(w.length/3))).map(x=>x[1]);return w.map((x,i)=>sc.includes(i)?x.replace(/[A-Za-z']+/,m=>'_'.repeat(Math.min(7,m.length))):x).join(' ')};
  const draw=()=>{const it=R[ri],fw=isJa()?[...it.t].slice(0,3).join(''):it.t.split(' ').slice(0,2).join(' ');
    const lab={repeat:'1 · Ouça e repita',cloze:'2 · Complete e fale a frase inteira',recall:'3 · Sem olhar: diga em '+fxLang(),real:'🗣️ Como falam de verdade'}[it.tier];
    let body;
    if(it.tier==='repeat')body=`<div class="nb-big-line">${H(it.t)}${it.r?`<em class="nb-rj2">${H(it.r)}</em>`:''}<em>${H(it.p)}</em></div>`;
    else if(it.tier==='cloze')body=`<div class="nb-big-line">${H(mask(it.t))}<em>${H(it.p)}</em></div>`;
    else if(it.tier==='recall')body=`<div class="nb-big-line">${H(it.p)}<em>Começa com: “${H(fw)}…”</em></div>`;
    else body=`<div class="nb-real"><div class="w">${H(it.t)}</div><div class="s">${H(it.sp)}</div><small>${H(it.p)}</small></div>`;
    st.innerHTML=`<div class="step fx nbx" ${theme(f)}>${head(f,n,'Fale em voz alta')}<div class="nb-prog">${R.map((_,i)=>`<i class="${i<ri?'on':''}"></i>`).join('')}</div><div class="nb-hint" style="font-weight:900;opacity:.85">${lab}</div>${body}
    <div class="nb-tools" style="justify-content:center"><button class="nb-chip" id="nbl">🔊 ${it.tier==='real'?'Escrito':'Ouvir'}</button>${it.tier==='real'?'<button class="nb-chip" id="nbf">🔊 Rápido (real)</button>':''}<button class="nb-chip" id="nbs">🐢 Devagar</button></div>
    <div id="nbmh"></div><div id="nbrv"></div><div class="nb-hint" id="nbh2"></div></div>`;
    const play=sl=>say2(it.t,null,sl);
    q('#nbl',st).onclick=()=>play(false);q('#nbs',st).onclick=()=>play(true);if(q('#nbf',st))q('#nbf',st).onclick=()=>say2(it.sp,null);
    if(it.tier!=='recall')setTimeout(()=>play(false),350);
    const adv=()=>{ri++;if(ri<R.length)draw();else win()};
    const done=()=>{if(it.tier==='recall')q('#nbrv',st).innerHTML=`<div class="nb-gl">✅ ${H(it.t)}</div>`;P.fx.cta=()=>{adv();return true};cta(ri<R.length-1?'Próxima ▶':'Concluir',true,true)};
    const fb=()=>{q('#nbmh',st).innerHTML=`<button class="nb-mic" id="nbm" aria-label="Falar">🎤</button><div class="nb-rate" id="nbrt"><button data-v="1">😬</button><button data-v="2">🙂</button><button data-v="3">🤩</button></div><div class="nb-hint">Fale em voz alta e se avalie.</div>`;
      q('#nbm',st).onclick=()=>play(false);st.querySelectorAll('#nbrt button').forEach(b=>b.onclick=()=>{sfx('step');done()})};
    P.fx.cta=()=>true;cta('Fale a frase 🎤',false);
    if(window.PogVoice&&PogVoice.supported())PogVoice.mount(q('#nbmh',st),{target:it.t,onDone:r=>{sfx('step');done()},onFail:c=>{if(c==='unsupported')fb()}});else fb();
    const sk=document.createElement('div');sk.className='nb-tools';sk.style.justifyContent='center';sk.innerHTML='<button class="nb-chip" id="nbsk">Pular</button>';q('#nbh2',st).after(sk);q('#nbsk',st).onclick=adv};
  draw();say('Repita, complete e depois lembre sem olhar!')};
/* 6 · chat de gírias, expressões e ditados */
FXR.nbslang=function(f,st,n){
  const cast=f.cast,L=f.lines,GL=f.gl;let k=0,pt=false;
  st.innerHTML=`<div class="step fx nbx" ${theme(f)}>${head(f,n,'Chat de gírias')}<div class="nb-tools"><button class="nb-chip" id="nbpt">🇧🇷 Tradução</button>${L.some(l=>l[3])?'<button class="nb-chip on" id="nbrj">あ/a Romaji</button>':''}</div><div class="nb-chat" id="nbc"></div><div id="nbg"></div><div class="nb-hint" id="nbhn">Toque nas palavras coloridas: <b>amarelo = essencial ⭐</b>, azul = curiosidade 🎈.</div></div>`;
  const box=q('#nbc',st),gbox=q('#nbg',st);const seen=new Set();rjInit(st,L);
  const ES=new Set((f.ess||[]).map(x=>x.toLowerCase()));const tg=a=>ES.has(a.toLowerCase())?'e':'x';
  const mk=t=>H(t).replace(/\*\*(.+?)\*\*/g,(m,a)=>`<mark class="${tg(a)}" data-k="${a}">${a}</mark>`);
  const plain=t=>t.replace(/\*\*/g,'');
  const add=i=>{const l=L[i],me=l[0]==='You',c=cast[l[0]]||['🙂','#999'];const r=document.createElement('div');r.className='nb-row'+(me?' me':'');
    r.innerHTML=`<span class="nb-av" style="background:${c[1]}22">${av(c[0],l[0],c[1])}</span><div class="nb-b"><span class="nb-who">${H(me?'VOCÊ':l[0])}</span>${mk(l[1])}${rjh(l)}<small>${H(l[2])}</small></div>`;
    r.querySelector('.nb-b').onclick=ev=>{const m=ev.target.closest('mark');if(m){const key=m.dataset.k;seen.add(key);gbox.innerHTML=`<div class="nb-gl"><span class="nb-tag ${tg(key)}">${tg(key)==='e'?'⭐ Essencial':'🎈 Curiosidade'}</span>💡 <b>${H(key)}</b> = ${H(GL[key]||'')} <button class="nb-chip" style="margin-left:6px">🔊</button></div>`;gbox.querySelector('button').onclick=()=>say2(key,null);say2(key,null)}else say2(plain(l[1]),l[0])};
    box.appendChild(r);r.scrollIntoView({block:'nearest',behavior:'smooth'});say2(plain(l[1]),l[0])};
  const next=()=>{if(k<L.length){add(k);k++;if(k>=L.length){cta('Continuar',true,true);q('#nbhn',st).innerHTML='Revise: <b>'+Object.keys(GL).map(k=>(ES.has(k.toLowerCase())?'⭐ ':'')+H(k)).join(' · ')+'</b>'}else cta('Próxima mensagem ▶',true)}};
  q('#nbpt',st).onclick=e=>{pt=!pt;box.classList.toggle('nb-pt',pt);e.currentTarget.classList.toggle('on',pt)};
  P.fx.cta=()=>{if(k<L.length){next();return true}return false};next()};

/* 7 · em que contexto? (aplicar o que viu no chat) */
FXR.nbctx=function(f,st,n){
  const R=f.items;let ri=0;lock();
  const draw=()=>{const it=R[ri];
    st.innerHTML=`<div class="step fx nbx" ${theme(f)}>${head(f,n,'Em que contexto?')}<div class="nb-prog">${R.map((_,i)=>`<i class="${i<ri?'on':''}"></i>`).join('')}</div>
    <div class="nb-card"><div class="nb-sit"><b>${it.ic}</b>${H(it.sit)}</div></div><div class="nb-hint">O que você diria?</div>
    <div class="nb-chat" id="nbo">${it.opts.map((o,i)=>`<div class="nb-row me"><div class="nb-b" data-i="${i}">${H(o)}</div></div>`).join('')}</div><div id="nbw"></div></div>`;
    let lk=false;st.querySelectorAll('#nbo .nb-b').forEach(b=>b.onclick=()=>{if(lk)return;const i=+b.dataset.i;say2(it.opts[i],'You');
      if(i===it.a){lk=true;b.style.background='#c9f5dc';b.style.color='#17613a';sfx('burst');q('#nbw',st).innerHTML=`<div class="nb-gl">✅ ${H(it.why)}</div>`;setTimeout(()=>{ri++;if(ri<R.length)draw();else win()},1900)}else{b.style.opacity=.4;sfx('oops')}})};
  draw();cta('Escolha a melhor frase',false);say('Use o que você viu no chat.')};

/* 8 · soletrando (construção de vocabulário) */
FXR.nbvocab=function(f,st,n){
  const R=f.items;let ri=0;lock();
  const draw=()=>{const it=R[ri],w=it[0].toLowerCase(),letters=fxShuffle(w.split('').map((c,i)=>({c,i})));let cur=[];
    st.innerHTML=`<div class="step fx nbx" ${theme(f)}>${head(f,n,'Soletrando')}<div class="nb-prog">${R.map((_,i)=>`<i class="${i<ri?'on':''}"></i>`).join('')}</div>
    <div class="nb-card"><div class="nb-sit"><b>${it[1]}</b>${H(it[2])}</div></div><div class="nb-tools" style="justify-content:center"><button class="nb-chip" id="nbl">🔊 Ouvir</button><button class="nb-chip" id="nbd">💡 Dica</button><button class="nb-chip" id="nbc2">↩︎ Apagar</button></div>
    <div class="nb-sl" id="nbs">${w.split('').map(()=>'<span></span>').join('')}</div><div class="nb-lt" id="nblt">${letters.map((l,j)=>`<button data-j="${j}">${l.c}</button>`).join('')}</div></div>`;
    const slots=()=>[...st.querySelectorAll('#nbs span')],btns=()=>[...st.querySelectorAll('#nblt button')];
    const paint=()=>{slots().forEach((s,i)=>s.textContent=cur[i]?cur[i].c:'');btns().forEach((b,j)=>b.classList.toggle('used',cur.some(x=>x.j===j)))};
    q('#nbl',st).onclick=()=>say2(it[0],null);setTimeout(()=>say2(it[0],null),350);
    q('#nbd',st).onclick=()=>{const t=q('#nbs',st);t.firstElementChild.textContent=w[0];};
    q('#nbc2',st).onclick=()=>{cur.pop();paint()};
    btns().forEach((b,j)=>b.onclick=()=>{if(cur.some(x=>x.j===j)||cur.length>=w.length)return;cur.push({c:letters[j].c,j});sfx('key');paint();
      if(cur.length===w.length){const ok=cur.map(x=>x.c).join('')===w,box=q('#nbs',st);box.classList.add(ok?'ok':'no');
        if(ok){sfx('burst');say2(it[0],null);setTimeout(()=>{ri++;if(ri<R.length)draw();else win()},1100)}else{sfx('oops');setTimeout(()=>{box.classList.remove('no');cur=[];paint()},700)}}})};
  draw();cta('Monte as palavras',false);say('Ouça a palavra e toque nas letras.')};
/* 9 · caça-palavras (vocabulário em inglês a partir de pistas em português) */
FXR.nbfind=function(f,st,n){
  const W_len=()=>f.items.map(x=>x[0]).filter(w=>w.length<=10).slice(0,5).map(w=>w.length);
  const W=f.items.map(x=>({w:x[0].toLowerCase(),e:x[1],pt:x[2]})).filter(x=>x.w.length<=10).slice(0,5);const N=Math.max(8,...W_len());lock();
  let G,place;
  for(let tries=0;tries<80;tries++){G=Array.from({length:N},()=>Array(N).fill(''));place=[];let ok=true;
    for(const it of W){let done=false;for(let a=0;a<60&&!done;a++){const d=[[0,1],[1,0],[1,1]][Math.random()*3|0],r=Math.random()*N|0,c=Math.random()*N|0,er=r+d[0]*(it.w.length-1),ec=c+d[1]*(it.w.length-1);if(er>=N||ec>=N)continue;
      const cells=[...it.w].map((ch,i)=>[r+d[0]*i,c+d[1]*i,ch]);if(cells.every(x=>!G[x[0]][x[1]]||G[x[0]][x[1]]===x[2])){cells.forEach(x=>G[x[0]][x[1]]=x[2]);place.push({it,cells});done=true}}
      if(!done){ok=false;break}}
    if(ok)break}
  const JAW=W.some(x=>/[\u3040-\u30ff]/.test(x.w)),AB=[...(JAW?'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわん':'abcdefghijklmnopqrstuvwxyz')];G.forEach(r=>r.forEach((v,i)=>{if(!v)r[i]=AB[Math.random()*AB.length|0]}));
  st.innerHTML=`<div class="step fx nbx" ${theme(f)}>${head(f,n,'Caça-palavras')}<div class="nb-hint">Ache em ${fxLang()}: toque na primeira e na última letra de cada palavra.</div>
  <div class="nb-clues" id="nbcl">${W.map((x,i)=>`<span data-i="${i}">${x.e} ${H(x.pt)}</span>`).join('')}</div>
  <div class="nb-ws" id="nbw" style="grid-template-columns:repeat(${N},1fr)">${G.map((r,i)=>r.map((v,j)=>`<button data-r="${i}" data-c="${j}">${v}</button>`).join('')).join('')}</div></div>`;
  const cell=(r,c)=>q(`#nbw [data-r="${r}"][data-c="${c}"]`,st);let a=null,found=0;
  st.querySelectorAll('#nbw button').forEach(b=>b.onclick=()=>{const r=+b.dataset.r,c=+b.dataset.c;
    if(!a){a=[r,c];b.classList.add('sel');return}
    const [r0,c0]=a;st.querySelectorAll('#nbw .sel').forEach(x=>x.classList.remove('sel'));a=null;
    const dr=Math.sign(r-r0),dc=Math.sign(c-c0),len=Math.max(Math.abs(r-r0),Math.abs(c-c0))+1;
    if(!((r===r0)||(c===c0)||Math.abs(r-r0)===Math.abs(c-c0))||len<2){sfx('oops');return}
    const cells=Array.from({length:len},(_,i)=>[r0+dr*i,c0+dc*i]),str=cells.map(x=>G[x[0]][x[1]]).join(''),rev=[...str].reverse().join('');
    const hit=W.findIndex(x=>(x.w===str||x.w===rev)&&!x.fd);
    if(hit>=0){W[hit].fd=true;found++;cells.forEach(x=>cell(x[0],x[1]).classList.add('fd'));q(`#nbcl [data-i="${hit}"]`,st).classList.add('fd');sfx('burst');say2(W[hit].w,null);if(found>=W.length)setTimeout(()=>win(),900)}else sfx('oops')});
  cta('Ache as palavras',false);say('Procure as palavras em '+fxLang()+' na grade.')};
})();
/* textos fixos do Neighbors → espanhol (cursos com ui:'es') */
if(typeof FXES_MAP!=='undefined')Object.assign(FXES_MAP,{
'Caça-níveis de frases':'Niveles de frases','Memória de palavras':'Memoria de palabras','Resposta rápida':'Respuesta rápida','Chat de gírias':'Chat de jergas','Caça-palavras':'Sopa de letras',
'SUA MISSÃO':'TU MISIÓN','Esse é seu novo vizinho!':'¡Este es tu nuevo vecino!','Conhecer o vizinho':'Conocer al vecino','🇧🇷 Tradução':'🇪🇸 Traducción','🎭 Eu falo minhas falas':'🎭 Yo digo mis líneas','🚩 Algo errado?':'🚩 ¿Algo mal?',
'Toque em “Próxima fala” para abrir cada mensagem.':'Toca «Siguiente frase» para abrir cada mensaje.','VOCÊ':'TÚ','Próxima fala ▶':'Siguiente frase ▶','Fale sua parte 🎤':'Di tu parte 🎤',
'Seu navegador não tem microfone: diga em voz alta e toque em “Ver a frase”.':'Tu navegador no tiene micrófono: dilo en voz alta y toca «Ver la frase».','Diga em voz alta e toque em “Ver a frase”.':'Dilo en voz alta y toca «Ver la frase».',
'O que está estranho nessa fala? (opcional)':'¿Qué hay de raro en esta frase? (opcional)','🔁 revisão':'🔁 repaso','Ouça a cena e toque na resposta certa':'Escucha la escena y toca la respuesta correcta','Escute a fala e escolha o que combina.':'Escucha la frase y elige la que encaja.',
'Troque as peças':'Cambia las piezas','1 · escolha o começo':'1 · elige el comienzo','Troque as peças e ouça cada frase nova.':'Cambia las piezas y escucha cada frase nueva.',
'Ache os pares':'Encuentra los pares','Vire as cartas e junte figura e palavra.':'Voltea las cartas y une imagen y palabra.','Como você responde?':'¿Cómo respondes?','Responda como um local!':'¡Responde como un local!','Escolha a resposta':'Elige la respuesta',
'1 · Ouça e repita':'1 · Escucha y repite','🗣️ Como falam de verdade':'🗣️ Cómo se habla de verdad','🔊 Rápido (real)':'🔊 Rápido (real)','Próxima ▶':'Siguiente ▶','Fale em voz alta e se avalie.':'Dilo en voz alta y evalúate.','Fale a frase 🎤':'Di la frase 🎤',
'Repita, complete e depois lembre sem olhar!':'¡Repite, completa y luego recuerda sin mirar!','Pular':'Saltar','Toque nas palavras coloridas:':'Toca las palabras de color:','amarelo = essencial ⭐':'amarillo = esencial ⭐','⭐ Essencial':'⭐ Esencial','Próxima mensagem ▶':'Siguiente mensaje ▶',
'O que você diria?':'¿Qué dirías?','Escolha a melhor frase':'Elige la mejor frase','Use o que você viu no chat.':'Usa lo que viste en el chat.','💡 Dica':'💡 Pista','↩︎ Apagar':'↩︎ Borrar','Monte as palavras':'Arma las palabras','Ouça a palavra e toque nas letras.':'Escucha la palabra y toca las letras.',
'Ache as palavras':'Encuentra las palabras','Visite as paradas':'Visita las paradas','Visite cada parada: toque no cartão para ouvir a frase e carimbar seu passaporte.':'Visita cada parada: toca la tarjeta para escuchar la frase y sellar tu pasaporte.','Vamos passear pelos lugares que você já conhece!':'¡Vamos a pasear por los lugares que ya conoces!',
'🔊 Ouvir tudo':'🔊 Escuchar todo','🔊 Ouvir a fala':'🔊 Escuchar la frase','🔊 Ouvir':'🔊 Escuchar',
'Passaporte do arco':'Pasaporte del arco','Para levar na mochila':'Para llevar en la mochila'
});
