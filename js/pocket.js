/* Pocket · inglês · episódios de 5 quadros: pkhero (Cena), pkdlg (Diálogo), pkbuild (Monte a frase), pkspeak (Fale), wrap (Mochila).
   Usa os mesmos helpers globais do Neighbors (FXR, say, cta, fxSay, fxKindBar, PogCover, PogFace, PogVoice). */
(function(){
if(typeof FXR==='undefined'||typeof FX_KIND==='undefined')return;
const L={pkhero:'Cena',pkdlg:'Diálogo',pkvoc:'Vocabulário',pkread:'Leitura',pkbuild:'Monte a frase',pkspeak:'Fale'};
Object.keys(L).forEach(k=>{FX_KIND[k]=k==='pkspeak'?'speak':(k==='pkhero'||k==='pkread'||k==='pkvoc')?'story':'practice';FX_LABEL[k]=L[k]});
const q=(s,r)=>(r||document).querySelector(s);
const H=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));

const sfx2=n=>{try{sfx(n)}catch(e){}};
const lock=()=>{P.fx.done=false;P.fx.cta=()=>!P.fx.done};
const th=f=>'style="--g1:'+(f.g||['#FF8A5B'])[0]+';--g2:'+(f.g||[0,'#FFC857'])[1]+'"';
const av=(em,name,col)=>{try{return window.NBF?NBF.avatar(em,name,col):(window.PogFace?PogFace.avatar(em,name,col):em)}catch(e){return em}};

/* personagem de corpo inteiro (cabeça/ombros refinados do PogFace + corpo proporcional), sem zoom no rosto */
const TONEM={'\u{1F3FB}':0,'\u{1F3FC}':1,'\u{1F3FD}':2,'\u{1F3FE}':3,'\u{1F3FF}':3};
const SH=['#3b6ea5','#b5543c','#4d8f6b','#7a5fa8','#c58a2f','#2f7f86'];
function fullBody(face,name,gender){
  try{const F=window.PogFace;if(!F||!F.bust)return '';
    let h=7;for(const c of String(name))h=(h*31+c.charCodeAt(0))>>>0;
    const tm=String(face).match(/[\u{1F3FB}-\u{1F3FF}]/u),g=gender==='f'?'f':'m';
    const col=SH[h%SH.length],hair=['#4a3228','#2b211c','#7a4a2b','#5b3a29'][h%4];
    const bo={g,tone:tm?TONEM[tm[0]]:h%4,style:(g==='f'?['long','wavy','bob','bun']:['short','side','short','curly'])[(h>>3)%4],hair,shirt:col,seed:h,refined:true,natural:true,rich:2,mood:'grin',glasses:false,beard:false};
    const k=.2,by=-17-120*k,pants=['#2f3550','#4a3b32','#3b4a63','#35384a'][h%4],pd='#20263a',sk='#d9a07a';
    const face2='<svg x="'+(-46*k).toFixed(2)+'" y="'+by.toFixed(2)+'" width="'+(92*k).toFixed(2)+'" height="'+(120*k).toFixed(2)+'" viewBox="4 6 92 120" overflow="hidden">'+F.bust(bo)+'</svg>';
    const arm=(sx,c)=>'<path d="M'+(sx*7.4)+' '+(by+88*k).toFixed(2)+' Q'+(sx*9.3)+' -20 '+(sx*8.7)+' -12.5" stroke="'+c+'" stroke-width="2.4" fill="none" stroke-linecap="round"/><ellipse cx="'+(sx*8.7)+'" cy="-10.8" rx="1.25" ry="1.6" fill="#e6b896"/>';
    return '<svg class="pk-fig" viewBox="-14 -48 28 50" preserveAspectRatio="xMidYMax meet" aria-hidden="true"><ellipse cx="0" cy=".2" rx="11" ry="1.9" fill="#000" fill-opacity=".3"/>'+
     '<path d="M-6.2 -17.5 L-5.6 -2.4 L-.6 -2.4 L-.4 -17.5Z" fill="'+pants+'"/><path d="M.4 -17.5 L.6 -2.4 L5.6 -2.4 L6.2 -17.5Z" fill="'+pd+'"/>'+
     '<path d="M-6.4 -3 Q-3.4 -4.4 -.5 -3 L-.5 -1.2 L-6.8 -1.2Z M.5 -3 Q3.4 -4.4 6.4 -3 L6.8 -1.2 L.5 -1.2Z" fill="#15151c"/>'+face2+arm(-1,col)+arm(1,'#00000033')+'</svg>';
  }catch(x){return ''}}
const bg=v=>{try{const e=P.e,h=e.fr.find(x=>x.k==='pkhero');return '<div class="pk-bg b'+v+'" aria-hidden="true">'+coverOf(e,h,true)+'</div>'}catch(x){return ''}};
const strip=()=>{try{const e=P.e,h=e.fr.find(x=>x.k==='pkhero');return '<div class="pk-strip">'+coverOf(e,h,true)+'</div>'}catch(x){return ''}};
const coverOf=(e,f,noc)=>{try{return PogCover.svg({n:e.n,t:e.t,sc:e.sc,fr:[{k:'nbhero',face:f.face,name:f.name,city:f.city,num:f.num}]},{full:true,noChar:!!noc})}catch(x){return ''}};


/* ===== áudio em fila: cada fala espera a anterior terminar; nada se atropela nem pula palavras ===== */
const PKA={tok:0,
  stop(){this.tok++;try{fxStopAudio()}catch(e){}},
  say(text,who,slow){const my=this.tok,t0=Date.now(),txt=String(text||'');
    return new Promise(res=>{let end=false;
      const est=Math.max(1400,txt.length*(slow?125:80)+800),minMs=Math.min(est*.5,txt.length*34+300);
      const fin=ok=>{if(end)return;end=true;clearInterval(tm);if(window.__speakEnd===cb)window.__speakEnd=null;
        const rest=ok?Math.max(0,minMs-(Date.now()-t0)):0;setTimeout(()=>res(ok&&my===PKA.tok),rest)};
      const cb=()=>fin(true),busy=()=>{try{return !!(speechSynthesis.speaking||speechSynthesis.pending)}catch(e){return false}};
      /* só desiste se o aparelho já não está falando (voz ausente/travada); se ainda fala, espera o fim */
      const tm=setInterval(()=>{const el=Date.now()-t0;if((el>est*1.15&&!busy())||el>est*3+3000)fin(true)},400);
      window.__speakEnd=cb;
      try{fxSay(txt,who||null,slow?(typeof slow==='number'?slow:.72):undefined)}catch(e){fin(false)}})},
  wait:ms=>new Promise(r=>setTimeout(r,ms))};
const say2=(t,w,slow)=>{PKA.stop();return PKA.say(t,w,slow)};
const alive=fx=>{try{return !!(P&&P.fx===fx)}catch(e){return false}};
const coach=t=>{try{const b=document.getElementById('pbub');if(b)b.textContent=t||''}catch(e){}};
const store={get(k,d){try{const v=localStorage.getItem('pk:'+k);return v==null?d:JSON.parse(v)}catch(e){return d}},set(k,v){try{localStorage.setItem('pk:'+k,JSON.stringify(v))}catch(e){}}};
const rx=w=>String(w).replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
/* texto -> blocos [{t,v}] : v = índice do vocabulário quando a trecho é palavra marcada */
function units(text,voc){
  const out=[];const list=voc.map((v,i)=>[String(v[0]),i]).sort((a,b)=>b[0].length-a[0].length);
  const re=list.length?new RegExp('\\b('+list.map(x=>rx(x[0])).join('|')+')\\b','gi'):null;
  const push=(seg,vi)=>{if(vi!=null){out.push({t:seg,v:vi});return}seg.split(/(\s+)/).forEach(p=>{if(!p)return;if(/^\s+$/.test(p))out.push({s:p});else out.push({t:p})})};
  let last=0,m;
  if(re){while((m=re.exec(text))){if(m.index>last)push(text.slice(last,m.index));const vi=list.find(x=>x[0].toLowerCase()===m[0].toLowerCase());push(m[0],vi?vi[1]:null);last=m.index+m[0].length}}
  if(last<text.length)push(text.slice(last));return out}
const unitsHTML=(text,voc,cls)=>units(text,voc).map(u=>u.s!=null?H(u.s):'<span class="pk-wd'+(u.v!=null?' pk-w':'')+(cls?' '+cls:'')+'"'+(u.v!=null?' data-v="'+u.v+'"':'')+'>'+H(u.t)+'</span>').join('');
/* destaque palavra a palavra, no ritmo da fala (estimado); termina quando a fala termina */
function karaoke(els,text,slow,speakP){
  const total=Math.max(900,String(text).length*(slow?120:72)),w=els.map(u=>u.textContent.length+1),S=w.reduce((a,b)=>a+b,0)||1,t0=Date.now();
  const cur=k=>els.forEach((u,j)=>{u.classList.toggle('past',j<k);u.classList.toggle('cur',j===k)});
  const tick=setInterval(()=>{const el=(Date.now()-t0)/total*S;let a=0,k=0;while(k<els.length&&a+w[k]<=el){a+=w[k];k++}cur(Math.min(k,els.length-1))},60);
  return speakP.then(ok=>{clearInterval(tick);els.forEach(u=>{u.classList.remove('cur');u.classList.add('past')});return ok})}
const saved=()=>store.get('saved',[]);
/* estatísticas do episódio atual (lidas por js/pkplan.js ao concluir) */
const PKS=window.PKS={cur:null,init(){const n=P&&P.e&&P.e.n;if(!this.cur||this.cur.n!==n)this.cur={n,voc:[],vt:0,b:0,bt:0,bd:{},sp:0,sk:0,st:0,dl:0};return this.cur}};
const tipH=(ic,t)=>'<div class="pk-tip" id="pktip"><i>'+ic+'</i><span>'+t+'</span></div>';
/* ícones SVG (Noto) carregados sob demanda de data/pk-icons.json; enquanto não chegam, mostra o emoji */
const PKI={m:null,p:null,
  load(){if(this.p)return this.p;this.p=fetch('data/pk-icons.json').then(r=>r.json()).then(j=>{this.m=j;return j}).catch(()=>{this.m={};return this.m});return this.p},
  svg(e){return this.m&&this.m[e]||''},
  html(e,cls){const sv=this.svg(e);return '<span class="pk-ico'+(cls?' '+cls:'')+'" data-e="'+H(e)+'">'+(sv||'<b class="pk-eg">'+H(e)+'</b>')+'</span>'},
  paint(root){this.load().then(()=>{root.querySelectorAll('.pk-ico[data-e]').forEach(el=>{if(el.querySelector('svg'))return;const sv=this.svg(el.dataset.e);if(sv)el.innerHTML=sv})})}};
/* 1 · Cena */
FXR.pkhero=function(f,st,n){
  const e=P.e,fx=P.fx;PKA.stop();PKS.cur=null;PKS.init();
  st.innerHTML='<div class="step fx pk pk-hero" '+th(f)+'>'+fxKindBar(f,n)+
   '<div class="pk-poster"><div class="pk-scene">'+coverOf(e,f,true)+fullBody(f.face,f.name,(e.character||{}).gender)+'<span class="pk-badge">'+(f.boss?'⭐ DESAFIO DO ARCO':'EPISÓDIO '+f.num)+' · '+H(f.lvl)+'</span></div>'+
   '<div class="pk-info"><span class="pk-face">'+av(f.face,f.name,f.g[0])+'</span><h2>'+H(e.t)+'</h2><p class="pk-sub">'+H(f.name)+' · '+H(f.city)+'</p>'+
   '<div class="pk-mis"><small>SUA MISSÃO</small>'+H(f.mission)+'</div>'+
   '<button class="pk-key" id="pkk" type="button">🔊 <b>“'+H(f.hook[0])+'”</b><em>'+H(f.hook[1])+'</em></button></div></div></div>';
  q('#pkk',st).onclick=()=>{sfx2('pop');say2(f.hook[0],f.name)};
  setTimeout(()=>{if(alive(fx))PKA.say(f.hook[0],f.name)},500);
  cta(f.boss?'Aceitar o desafio':'Vamos lá',true,true);coach('Hoje a missão é rápida: sete quadros!')};

/* 2 · Diálogo: conversa que se conta sozinha, uma fala por vez, com áudio em ordem */
FXR.pkdlg=function(f,st,n){
  const Ls=f.lines,cast=f.cast||{},voc=f.vocab||[],fx=P.fx;PKA.stop();lock();
  const hook=(P.e.fr.find(x=>x.k==='pkhero')||{}).hook||['',''];
  let runTok=0,playing=false,slow=false,pt=store.get('pt',true);const heard=new Set();
  st.innerHTML='<div class="step fx pk pk-dlg" '+th(f)+'>'+bg(1)+
   '<div class="pk-tools"><b class="pk-tt">Diálogo</b><button type="button" class="pk-btn'+(pt?' on':'')+'" id="pkpt">🇧🇷 PT</button><button type="button" class="pk-btn" id="pkslow">🐢 Lento</button><button type="button" class="pk-btn" id="pkal">⏸ Pausar</button></div>'+
   '<div class="pk-key2">🔑 <b>“'+H(hook[0])+'”</b><span>'+H(hook[1])+'</span></div>'+
   tipH('👆','Toque nas <mark>palavras amarelas</mark> para ver o significado')+
   '<div class="pk-chat'+(pt?' pt':'')+'" id="pkc">'+Ls.map((l,i)=>{const c=cast[l[0]]||['🙂','#999'],me=l[0]==='You';
     return '<div class="pk-row pend'+(me?' me':'')+'" data-l="'+i+'"><span class="pk-av">'+av(c[0],l[0],c[1])+'</span><div class="pk-b"><b>'+H(me?'VOCÊ':l[0])+'</b><span class="pk-en">'+unitsHTML(l[1],voc)+'</span><small class="pk-pt">'+H(l[2])+'</small>'+(me?'<button type="button" class="pk-mic" title="Repetir esta fala">🎤</button>':'')+'<i class="pk-ok">✓</i></div></div>'}).join('')+'</div>'+
   '<div class="pk-card2" id="pkcard" hidden></div></div>';
  const chat=q('#pkc',st),rows=[...st.querySelectorAll('.pk-row')],card=q('#pkcard',st),tip=q('#pktip',st),bAl=q('#pkal',st);
  const first=q('.pk-w',st);if(first)first.classList.add('pulse');
  const reveal=i=>{const r=rows[i];if(!r||!r.classList.contains('pend'))return;r.classList.remove('pend');r.classList.add('in');chat.scrollTo({top:chat.scrollHeight,behavior:'smooth'})};
  const revealAll=()=>rows.forEach((_,i)=>reveal(i));
  const setNow=i=>rows.forEach((r,j)=>r.classList.toggle('now',j===i));
  let unlocked=false;
  const unlock=()=>{if(unlocked)return;unlocked=true;try{PKS.init().dl=heard.size}catch(e){}P.fx.done=true;P.fx.cta=()=>false;cta('Continuar',true,true);coach('Muito bem! Toque nas palavras ou siga em frente.')};
  const mark=i=>{rows[i].classList.add('heard');heard.add(i);if(heard.size>=Math.min(3,Ls.length))unlock()};
  const label=()=>{bAl.textContent=playing?'⏸ Pausar':'▶ Ouvir'};
  const speakLine=(i)=>{const l=Ls[i];return PKA.say(l[1],l[0]==='You'?null:l[0],slow)};
  const run=async from=>{const my=++runTok;PKA.stop();playing=true;label();
    for(let i=from;i<Ls.length;i++){
      if(!alive(fx)||my!==runTok)return;
      reveal(i);setNow(i);
      const ok=await speakLine(i);
      if(!alive(fx)||my!==runTok||!ok)return;
      mark(i);await PKA.wait(320)}
    if(my===runTok){setNow(-1);playing=false;label();unlock()}};
  const pause=()=>{runTok++;PKA.stop();playing=false;setNow(-1);label();revealAll()};
  bAl.onclick=()=>{if(playing){pause();return}const nx=rows.findIndex((r,i)=>!heard.has(i));run(nx<0?0:nx)};
  q('#pkpt',st).onclick=ev=>{pt=!pt;store.set('pt',pt);chat.classList.toggle('pt',pt);ev.currentTarget.classList.toggle('on',pt)};
  q('#pkslow',st).onclick=ev=>{slow=!slow;ev.currentTarget.classList.toggle('on',slow);coach(slow?'Velocidade lenta ligada.':'Velocidade normal.')};
  const closeCard=()=>{card.hidden=true;card.innerHTML=''};
  const openWord=b=>{const v=voc[+b.dataset.v],w=b.textContent;pause();sfx2('pop');b.classList.add('seen');b.classList.remove('pulse');tip.hidden=true;
    const has=saved().some(x=>x[0]===v[0]);
    card.innerHTML='<div class="pkc-w"><b>'+H(w)+'</b><span>'+H(v[1])+'</span></div><div class="pkc-a"><button type="button" id="pkc-h">🔊 Ouvir</button><button type="button" id="pkc-s">🐢 Devagar</button><button type="button" id="pkc-b"'+(has?' class="on"':'')+'>'+(has?'✓ Guardada':'＋ Guardar na mochila')+'</button><button type="button" id="pkc-x" aria-label="Fechar">✕</button></div>';
    card.hidden=false;PKI.paint(card);
    q('#pkc-h',card).onclick=()=>say2(w);q('#pkc-s',card).onclick=()=>say2(w,null,true);q('#pkc-x',card).onclick=closeCard;
    q('#pkc-b',card).onclick=ev=>{const a=saved(),k=a.findIndex(x=>x[0]===v[0]);if(k<0){a.push([v[0],v[1]]);store.set('saved',a);ev.currentTarget.textContent='✓ Guardada';ev.currentTarget.classList.add('on');sfx2('step')}else{a.splice(k,1);store.set('saved',a);ev.currentTarget.textContent='＋ Guardar na mochila';ev.currentTarget.classList.remove('on')}};
    say2(w)};
  const openMic=i=>{pause();const l=Ls[i];
    card.innerHTML='<div class="pkc-w"><b>'+H(l[1])+'</b><span>'+H(l[2])+'</span></div><div id="pkcm"></div><div class="pkc-a"><button type="button" id="pkc-h">🔊 Ouvir</button><button type="button" id="pkc-x" aria-label="Fechar">✕</button></div>';card.hidden=false;
    q('#pkc-h',card).onclick=()=>say2(l[1]);q('#pkc-x',card).onclick=closeCard;
    const done=()=>{sfx2('step');mark(i);const m=q('#pkcm',card);if(m)m.innerHTML='<div class="pkc-ok">Muito bem! ✔</div>'};
    const fb=()=>{const m=q('#pkcm',card);if(!m)return;m.innerHTML='<button type="button" class="pk-btn" id="pkok">Eu falei ✔</button>';q('#pkok',card).onclick=done};
    if(window.PogVoice&&PogVoice.supported())PogVoice.mount(q('#pkcm',card),{target:l[1],onDone:done,onFail:c=>{if(c==='unsupported')fb()}});else fb()};
  chat.addEventListener('click',ev=>{
    const w=ev.target.closest('.pk-w');if(w){ev.stopPropagation();openWord(w);return}
    const mic=ev.target.closest('.pk-mic');if(mic){ev.stopPropagation();openMic(+mic.closest('.pk-row').dataset.l);return}
    const r=ev.target.closest('.pk-row');if(!r||r.classList.contains('pend'))return;
    const i=+r.dataset.l;closeCard();runTok++;PKA.stop();playing=false;label();setNow(i);
    speakLine(i).then(ok=>{if(ok){mark(i)}setNow(-1)})});
  cta('Ouvindo o diálogo…',false);coach('Ouça o diálogo. Toque numa fala para repetir.');
  setTimeout(()=>{if(alive(fx))run(0)},450)};

/* 2b · Leitura: o mesmo episódio contado como narração, com destaque palavra a palavra */
/* 2b · Vocabulário: figura por palavra, toque para ver exemplos */
const STC=[['#E85D75','#7B2350'],['#3E8FD8','#1B4585'],['#F29B34','#9A4E14'],['#9B6AD8','#4A2A86'],['#2FB0A0','#166057'],['#2FAE6C','#0F5A37']];
const TILE=['#ff8a5b','#2ec4b6','#b388ff','#43d17a','#ff7a7a','#3a86ff'];
FXR.pkvoc=function(f,st,n){
  const fx=P.fx,C=f.cards||[];PKA.stop();lock();const seen=new Set();let cur=-1;
  const pic=(c,i)=>c[2]?PKI.html(c[2],'pkv-em'):'<span class="pkv-em tile" style="background:'+TILE[i%TILE.length]+'">'+H(String(c[0]).charAt(0).toUpperCase())+'</span>';
  st.innerHTML='<div class="step fx pk pk-voc" '+th(f)+'>'+bg(1)+
   '<div class="pk-tools"><b class="pk-tt">Vocabulário</b><span class="pk-cnt" id="pkvc"></span></div>'+
   tipH('👆','Toque em cada <mark>figura</mark> para ver e ouvir a palavra')+
   '<div class="pkv-grid">'+C.map((c,i)=>'<button type="button" class="pkv-c" data-i="'+i+'">'+pic(c,i)+'<b>'+H(c[0])+'</b><i class="pk-ok">✓</i></button>').join('')+'</div>'+(f.notes||[]).map(m=>'<div class="pk-note pkv-note"><b>“'+H(m.en)+'”</b> '+H(m.txt)+'</div>').join('')+
   '<div class="pk-card2 pkv-card" id="pkcard" hidden></div></div>';
  const card=q('#pkcard',st),cnt=q('#pkvc',st),tip=q('#pktip',st),cells=[...st.querySelectorAll('.pkv-c')];PKI.paint(st);
  const need=Math.min(C.length,5);let unlocked=false;
  const upd=()=>{cnt.textContent=seen.size+'/'+C.length;
    if(!unlocked&&seen.size>=need){unlocked=true;P.fx.done=true;P.fx.cta=()=>false;cta('Continuar',true,true);coach('Ótimo! Agora vamos ler um texto com essas palavras.')}};
  const close=()=>{card.hidden=true;card.innerHTML='';cur=-1};
  const open=i=>{const c=C[i],has=saved().some(x=>x[0]===c[0]);cur=i;seen.add(i);try{const c0=PKS.init();c0.vt=C.length;if(c0.voc.indexOf(i)<0)c0.voc.push(i)}catch(e){}cells[i].classList.add('seen');tip.hidden=true;sfx2('pop');
    card.innerHTML='<div class="pkv-big">'+pic(c,i)+'</div><div class="pkc-w"><b>'+H(c[0])+'</b><span>'+H(c[1])+'</span></div>'+
     (c[3]?'<div class="pkv-ex"><p>“'+H(c[3])+'”</p><small>'+H(c[4])+'</small></div>':'')+
     '<div class="pkc-a"><button type="button" id="pkc-h">🔊 Ouvir</button><button type="button" id="pkc-s">🐢 Devagar</button><button type="button" id="pkc-e">🔊 Exemplo</button><button type="button" id="pkc-b"'+(has?' class="on"':'')+'>'+(has?'✓ Guardada':'＋ Guardar')+'</button><button type="button" id="pkc-n">Próxima ▶</button><button type="button" id="pkc-x" aria-label="Fechar">✕</button></div>';
    card.hidden=false;
    q('#pkc-h',card).onclick=()=>say2(c[0]);q('#pkc-s',card).onclick=()=>say2(c[0],null,true);
    const ex=q('#pkc-e',card);if(c[3])ex.onclick=()=>say2(c[3]);else ex.hidden=true;
    q('#pkc-x',card).onclick=close;q('#pkc-n',card).onclick=()=>open((i+1)%C.length);
    q('#pkc-b',card).onclick=e2=>{const a=saved(),k=a.findIndex(x=>x[0]===c[0]);if(k<0){a.push([c[0],c[1]]);store.set('saved',a);e2.currentTarget.textContent='✓ Guardada';e2.currentTarget.classList.add('on');sfx2('step')}else{a.splice(k,1);store.set('saved',a);e2.currentTarget.textContent='＋ Guardar';e2.currentTarget.classList.remove('on')}};
    say2(c[0]).then(ok=>{if(ok&&alive(fx)&&cur===i&&c[3])return PKA.wait(250).then(()=>cur===i&&alive(fx)?PKA.say(c[3]):0)});upd()};
  cells.forEach(b=>b.onclick=()=>open(+b.dataset.i));
  upd();cta('Toque nas figuras…',false);coach('Toque em cada figura: veja, ouça e guarde as palavras.')};

/* 3 · Leitura: texto com o vocabulário */
FXR.pkread=function(f,st,n){
  const fx=P.fx,voc=f.vocab||[],P_=f.pars||[];PKA.stop();lock();
  let runTok=0,playing=false,slow=false,pt=store.get('pt',true);const heard=new Set();
  st.innerHTML='<div class="step fx pk pk-read" '+th(f)+'>'+bg(1)+
   '<div class="pk-tools"><b class="pk-tt">Leitura</b><button type="button" class="pk-btn'+(pt?' on':'')+'" id="pkpt">🇧🇷 PT</button><button type="button" class="pk-btn" id="pkslow">🐢 Lento</button><button type="button" class="pk-btn" id="pkal">⏸ Pausar</button></div>'+
   tipH('📖','Acompanhe a leitura. Toque nas <mark>palavras amarelas</mark>')+
   '<div class="pk-story'+(pt?' pt':'')+'" id="pks">'+P_.map((p,i)=>
     '<div class="pk-par" data-p="'+i+'">'+(p.ic?PKI.html(p.ic,'pk-pic'):'')+'<div class="pk-ptx"><p class="pk-line"><span class="pk-lead">'+unitsHTML(p.lead[0],voc)+'</span>'+(p.q[0]?' <span class="pk-q">“'+unitsHTML(p.q[0],voc)+'”</span>':'')+'</p><small class="pk-ptp">'+H(p.lead[1]+(p.q[0]?' “'+p.q[1]+'”':''))+'</small></div><i class="pk-ok">✓</i></div>').join('')+'</div>'+
   '<div class="pk-card2" id="pkcard" hidden></div></div>';PKI.paint(st);
  const box=q('#pks',st),pars=[...st.querySelectorAll('.pk-par')],card=q('#pkcard',st),tip=q('#pktip',st),bAl=q('#pkal',st);
  const first=q('.pk-w',st);if(first)first.classList.add('pulse');
  const setNow=i=>pars.forEach((r,j)=>{r.classList.toggle('now',j===i);if(j!==i)r.querySelectorAll('.cur').forEach(x=>x.classList.remove('cur'))});
  const reset=()=>st.querySelectorAll('.past,.cur').forEach(x=>x.classList.remove('past','cur'));
  let unlocked=false;
  const unlock=()=>{if(unlocked)return;unlocked=true;P.fx.done=true;P.fx.cta=()=>false;cta('Continuar',true,true);coach('Muito bem! Agora vamos montar frases.')};
  const label=()=>{bAl.textContent=playing?'⏸ Pausar':'▶ Ler'};
  const part=(el,text,who)=>karaoke([...el.querySelectorAll('.pk-wd')],text,slow,PKA.say(text,who,slow));
  const readPar=async i=>{const p=P_[i],r=pars[i];setNow(i);reset();r.scrollIntoView({block:'center',behavior:'smooth'});
    let ok=await part(r.querySelector('.pk-lead'),p.lead[0],null);if(!ok)return false;
    await PKA.wait(150);
    if(!p.q[0])return true;
    ok=await part(r.querySelector('.pk-q'),p.q[0],p.who==='You'?null:p.who);return ok};
  const run=async from=>{const my=++runTok;PKA.stop();playing=true;label();
    for(let i=from;i<P_.length;i++){
      if(!alive(fx)||my!==runTok)return;
      const ok=await readPar(i);if(!alive(fx)||my!==runTok||!ok)return;
      pars[i].classList.add('heard');heard.add(i);if(heard.size>=Math.min(3,P_.length))unlock();await PKA.wait(380)}
    if(my===runTok){setNow(-1);playing=false;label();unlock()}};
  const pause=()=>{runTok++;PKA.stop();playing=false;setNow(-1);reset();label()};
  bAl.onclick=()=>{if(playing){pause();return}const nx=pars.findIndex((r,i)=>!heard.has(i));run(nx<0?0:nx)};
  q('#pkpt',st).onclick=ev=>{pt=!pt;store.set('pt',pt);box.classList.toggle('pt',pt);ev.currentTarget.classList.toggle('on',pt)};
  q('#pkslow',st).onclick=ev=>{slow=!slow;ev.currentTarget.classList.toggle('on',slow)};
  const closeCard=()=>{card.hidden=true;card.innerHTML=''};
  box.addEventListener('click',ev=>{
    const w=ev.target.closest('.pk-w');
    if(w){ev.stopPropagation();const v=voc[+w.dataset.v],t=w.textContent;pause();sfx2('pop');w.classList.add('seen');w.classList.remove('pulse');tip.hidden=true;
      const has=saved().some(x=>x[0]===v[0]);
      card.innerHTML='<div class="pkc-w"><b>'+H(t)+'</b><span>'+H(v[1])+'</span></div><div class="pkc-a"><button type="button" id="pkc-h">🔊 Ouvir</button><button type="button" id="pkc-s">🐢 Devagar</button><button type="button" id="pkc-b"'+(has?' class="on"':'')+'>'+(has?'✓ Guardada':'＋ Guardar na mochila')+'</button><button type="button" id="pkc-x" aria-label="Fechar">✕</button></div>';card.hidden=false;
      q('#pkc-h',card).onclick=()=>say2(t);q('#pkc-s',card).onclick=()=>say2(t,null,true);q('#pkc-x',card).onclick=closeCard;
      q('#pkc-b',card).onclick=e2=>{const a=saved(),k=a.findIndex(x=>x[0]===v[0]);if(k<0){a.push([v[0],v[1]]);store.set('saved',a);e2.currentTarget.textContent='✓ Guardada';e2.currentTarget.classList.add('on');sfx2('step')}else{a.splice(k,1);store.set('saved',a);e2.currentTarget.textContent='＋ Guardar na mochila';e2.currentTarget.classList.remove('on')}};
      say2(t);return}
    const r=ev.target.closest('.pk-par');if(r){closeCard();run(+r.dataset.p)}});
  cta('Ouvindo a leitura…',false);coach('Leia e ouça. Toque num parágrafo para ler dali.');
  setTimeout(()=>{if(alive(fx))run(0)},450)};

/* 3 · Monte a frase */
FXR.pkbuild=function(f,st,n){
  const R=f.items;let ri=0;lock();
  const draw=()=>{const it=R[ri];let pick=0;const tried=new Set([0]);
    const render=()=>{const o=it.opts[pick];
      st.querySelector('.pk-sent').innerHTML=H(it.en).replace('{0}','<mark>'+H(o[0])+'</mark>');
      st.querySelector('.pk-sentpt').innerHTML=H(it.pt).replace('{0}','<mark>'+H(o[1])+'</mark>')};
    st.innerHTML='<div class="step fx pk pk-build" '+th(f)+'>'+bg(2)+'<div class="pk-prog">'+R.map((_,i)=>'<i class="'+(i<ri?'on':'')+'"></i>').join('')+'</div>'+
     '<div class="pk-card"><div class="pk-sent"></div><div class="pk-sentpt"></div><button class="pk-btn" id="pkhear" type="button">🔊 Ouvir</button></div>'+(it.note?'<div class="pk-note">'+H(it.note)+'</div>':'')+
     '<div class="pk-hint">Toque numa peça para trocar a palavra. Experimente todas!</div>'+
     '<div class="pk-opts">'+it.opts.map((o,i)=>'<button type="button" class="pk-opt'+(i===0?' on':'')+'" data-i="'+i+'"><b>'+H(o[0])+'</b><small>'+H(o[1])+'</small></button>').join('')+'</div></div>';
    render();
    const speak=()=>{const o=it.opts[pick];say2(it.en.replace('{0}',o[0]))};
    q('#pkhear',st).onclick=speak;
    st.querySelectorAll('.pk-opt').forEach(b=>b.onclick=()=>{pick=+b.dataset.i;tried.add(pick);sfx2('step');st.querySelectorAll('.pk-opt').forEach(x=>x.classList.toggle('on',x===b));b.classList.add('seen');render();speak();
      if(tried.size>=it.opts.length){try{const c0=PKS.init();c0.bt=R.length;c0.bd[ri]=1;c0.b=Object.keys(c0.bd).length}catch(e){}P.fx.cta=()=>{ri++;if(ri<R.length)draw();else{P.fx.done=true;return false}return true};cta(ri<R.length-1?'Próxima ▶':'Continuar',true,true)}});
    P.fx.cta=()=>true;cta('Troque as peças',false)};
  draw();coach('Troque as palavras e ouça como a frase muda.')};

/* 4 · Fale */
FXR.pkspeak=function(f,st,n){
  const R=f.items,cast=(P.e.fr.find(x=>x.k==='pkdlg')||{}).cast||{},fx=P.fx;let ri=0;lock();PKA.stop();
  const draw=()=>{const it=R[ri],c=cast[it.who]||['🙂','#999'];PKA.stop();
    st.innerHTML='<div class="step fx pk pk-speak" '+th(f)+'>'+bg(3)+'<div class="pk-prog">'+R.map((_,i)=>'<i class="'+(i<ri?'on':'')+'"></i>').join('')+'</div>'+
     '<div class="pk-row"><span class="pk-av">'+av(c[0],it.who,c[1])+'</span><div class="pk-b"><b>'+H(it.who)+'</b><span class="pk-en">'+H(it.line[0])+'</span><small style="display:block">'+H(it.line[1])+'</small></div></div>'+
     '<div class="pk-card pk-say"><small>SUA VEZ · diga em inglês</small><div class="pk-sent">'+H(it.target)+'</div><div class="pk-sentpt">'+H(it.pt)+'</div>'+
     '<div class="pk-tools"><button type="button" class="pk-btn" id="pkl">🔊 Ouvir</button><button type="button" class="pk-btn" id="pks">🐢 Devagar</button></div><div id="pkm"></div></div>'+
     '<div class="pk-tools"><button type="button" class="pk-btn" id="pksk">Pular</button></div></div>';
    q('#pkl',st).onclick=()=>say2(it.target);q('#pks',st).onclick=()=>say2(it.target,null,true);
    setTimeout(()=>{if(alive(fx))PKA.say(it.line[0],it.who===it.who?it.who:null)},350);
    const adv=()=>{ri++;if(ri<R.length)draw();else{P.fx.done=true;P.fx.cta=()=>false;cta('Continuar',true,true)}};
    const fin=()=>{try{const c0=PKS.init();c0.st=R.length;c0.sp++}catch(e){}sfx2('step');P.fx.cta=()=>{adv();return true};cta(ri<R.length-1?'Próxima ▶':'Concluir',true,true)};
    P.fx.cta=()=>true;cta('Fale a frase 🎤',false);
    if(window.PogVoice&&PogVoice.supported())PogVoice.mount(q('#pkm',st),{target:it.target,onDone:()=>fin(),onFail:c=>{if(c==='unsupported')q('#pkm',st).innerHTML='<div class="pk-tools"><button type="button" class="pk-btn" id="pkok">Eu falei ✔</button></div>',q('#pkok',st).onclick=fin}});
    else{q('#pkm',st).innerHTML='<div class="pk-tools"><button type="button" class="pk-btn" id="pkok">Eu falei ✔</button></div>';q('#pkok',st).onclick=fin}
    q('#pksk',st).onclick=()=>{try{const c0=PKS.init();c0.st=R.length;c0.sk++}catch(e){}adv()}};
  draw();coach('Agora é você! Fale a frase em voz alta.')};

/* 5 · Mochila: reaproveita o fechamento padrão e acrescenta cartões */
const w0=FXR.wrap;
FXR.wrap=function(f,st,n){
  if(!(P.e&&P.e.pocket)||!w0)return w0&&w0.apply(this,arguments);
  const e=P.e,s=f.sticker||{},STK=f.stickers||[];PKA.stop();
  const own=store.get('stk',[]);
  try{store.set('stk',[...new Set(own.concat(STK.map(c=>c[0].toLowerCase())))])}catch(x){}
  st.innerHTML='<div class="step fx pk pk-wrap" '+th(f)+'>'+bg(4)+
   '<div class="pk-fin"><div class="pk-vsw"><h3>🏷️ Figurinhas do vocabulário</h3><div class="pk-vs-grid">'+STK.map((c,i)=>{const nw=!own.includes(c[0].toLowerCase());return '<button type="button" class="pk-vs'+(s.boss?' gold':'')+'" data-t="'+H(c[0])+'" style="--c1:'+STC[i%STC.length][0]+';--c2:'+STC[i%STC.length][1]+';--r:'+(((i%3)-1)*1.6)+'deg"><span class="pk-vs-shine"></span>'+(nw?'<em class="pk-vs-new">NOVA</em>':'')+'<span class="pk-vs-top">'+(s.boss?'★★★':'★')+'</span><span class="pk-vs-win">'+(c[2]?PKI.html(c[2],'pk-vs-ic'):'<b class="pk-vs-l">'+H(String(c[0]).charAt(0).toUpperCase())+'</b>')+'</span><b class="pk-vs-w">'+H(c[0])+'</b><small>'+H(c[1])+'</small></button>'}).join('')+'</div></div>'+
   '<div class="pk-bag"><h3>🎒 Frases para levar</h3>'+(f.recap||[]).map(r=>'<button type="button" class="pk-cc" data-t="'+H(r[0])+'"><b>'+H(r[0])+'</b><small>'+H(r[1])+'</small></button>').join('')+'</div>'+
   '<div class="pk-bag"><h3>💬 Expressão</h3><button type="button" class="pk-cc" data-t="'+H((f.expr||[''])[0])+'"><b>'+H((f.expr||['',''])[0])+'</b><small>'+H((f.expr||['',''])[1])+'</small></button></div>'+
   '<div class="pk-cult">🌎 '+H(f.culture||'')+'</div><div class="pk-next">'+H((f.teaser||{}).t||'')+'</div></div></div>';
  st.querySelectorAll('.pk-cc,.pk-vs').forEach(b=>b.onclick=()=>{sfx2('pop');say2(b.dataset.t)});PKI.paint(st);
  try{sfx2('win');if(window.confetti)confetti(70)}catch(x){}
  cta('Concluir episódio',true,true);coach('Episódio concluído!')};
})();
