/* Pogglot · Quizzes de revisão (fora dos episódios)
   Cada episódio tem um quiz próprio, com práticas variadas que misturam vocabulário, expressões e estruturas:
   ver e escolher · ouvir e tocar · combinar · palavra em contexto · reagir à situação · completar o diálogo ·
   ordenar a conversa · completar a frase · montar a frase · achar o erro · digitar · verdadeiro ou falso.
   Dados em data/quiz_<curso>.json. */
(function(){
'use strict';
const store={get(k,d){try{const v=localStorage.getItem('pogglot:'+k);return v?JSON.parse(v):d}catch(e){return d}},set(k,v){try{localStorage.setItem('pogglot:'+k,JSON.stringify(v))}catch(e){}}};
const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const bold=s=>esc(s).replace(/\*\*(.+?)\*\*/g,'<b>$1</b>');
const shuf=a=>{a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a};
const HL=()=>(typeof ST!=='undefined'&&ST.homeLang)||'pt';
const TX={
 pt:{sec:'Quizzes de revisão',secSub:'Teste o que você aprendeu sem voltar aos episódios.',start:'Começar',again:'Refazer',best:'Melhor',quick:'Rápido',full:'Completo',qs:'perguntas',choose:'Como você quer treinar?',quickD:'Uma amostra variada para revisar em poucos minutos.',fullD:'Todas as práticas do episódio.',
  check:'Verificar',cont:'Continuar',skip:'Pular',ok:['Isso aí!','Perfeito!','Mandou bem!','Muito bem!'],no:['Quase!','Vamos ajustar.','Sem problemas.'],right:'Resposta certa',vocab:'Vocabulário',expr:'Expressões',gram:'Gramática',cult:'Cultura',
  res:'Resultado',acc:'de acerto',stars:'estrelas',xp:'XP ganhos',rev:'Para revisar',redo:'Refazer só os erros',close:'Fechar',perfect:'Sem erros! Você dominou este episódio.',great:'Ótimo resultado!',fair:'Bom começo: revise e tente de novo.',low:'Vale rever o episódio e voltar aqui.',
  hear:'Ouça e toque na imagem certa',see:'Que palavra é esta?',match:'Combine cada palavra com a imagem',ctxT:'Palavra no contexto',reactT:'O que você responde?',dialogT:'Complete a conversa',orderT:'Coloque a conversa em ordem',fillT:'Complete a frase',buildT:'Monte a frase',fixT:'Toque no erro',fixT2:'Qual é a correção?',typeT:'Escreva a palavra',tfT:'Verdadeiro ou falso?',askT:'Escolha a resposta',multiT:'Marque todas as corretas',readT:'Leia e responda',dictT:'Ouça e escreva',tapAll:'Pode haver mais de uma',
  tru:'Verdadeiro',fal:'Falso',slow:'Devagar',listen:'Ouvir',type:'Digite aqui',hintT:'dica',sentSaid:'Ele(a) diz',combo:'Sequência',exit:'Sair do quiz?',exitD:'Seu progresso nesta rodada será perdido.',stay:'Continuar quiz',leave:'Sair',noQuiz:'Em breve, quizzes para este curso.',done:'Concluído',tapEach:'Toque na ordem certa',yourTurn:'Sua vez',ep:'Episódio'},
 es:{sec:'Quizzes de repaso',secSub:'Pon a prueba lo aprendido sin volver a los episodios.',start:'Empezar',again:'Repetir',best:'Mejor',quick:'Rápido',full:'Completo',qs:'preguntas',choose:'¿Cómo quieres practicar?',quickD:'Una muestra variada para repasar en pocos minutos.',fullD:'Todas las prácticas del episodio.',
  check:'Comprobar',cont:'Continuar',skip:'Saltar',ok:['¡Eso es!','¡Perfecto!','¡Bien hecho!'],no:['¡Casi!','Vamos a ajustar.','No pasa nada.'],right:'Respuesta correcta',vocab:'Vocabulario',expr:'Expresiones',gram:'Gramática',cult:'Cultura',
  res:'Resultado',acc:'de acierto',stars:'estrellas',xp:'XP ganados',rev:'Para repasar',redo:'Repetir solo los errores',close:'Cerrar',perfect:'¡Sin errores! Dominaste este episodio.',great:'¡Gran resultado!',fair:'Buen comienzo: repasa e inténtalo de nuevo.',low:'Vale la pena repasar el episodio y volver.',
  hear:'Escucha y toca la imagen correcta',see:'¿Qué palabra es esta?',match:'Une cada palabra con su imagen',ctxT:'Palabra en contexto',reactT:'¿Qué respondes?',dialogT:'Completa la conversación',orderT:'Ordena la conversación',fillT:'Completa la frase',buildT:'Arma la frase',fixT:'Toca el error',fixT2:'¿Cuál es la corrección?',typeT:'Escribe la palabra',tfT:'¿Verdadero o falso?',askT:'Elige la respuesta',multiT:'Marca todas las correctas',readT:'Lee y responde',dictT:'Escucha y escribe',tapAll:'Puede haber más de una',
  tru:'Verdadero',fal:'Falso',slow:'Despacio',listen:'Escuchar',type:'Escribe aquí',hintT:'pista',sentSaid:'Dice',combo:'Racha',exit:'¿Salir del quiz?',exitD:'Perderás el progreso de esta ronda.',stay:'Seguir',leave:'Salir',noQuiz:'Pronto habrá quizzes para este curso.',done:'Completado',tapEach:'Toca en el orden correcto',yourTurn:'Tu turno',ep:'Episodio'}
};
const k=key=>{const t=TX[HL()]||TX.pt;return t[key]!=null?t[key]:TX.pt[key]};
const SK={c:{n:'cult',c:'#D6336C',bg:'#FFE3EE',ic:'🎬'},v:{n:'vocab',c:'#7C4DFF',bg:'#F1EBFF',ic:'🧩'},e:{n:'expr',c:'#0FA79B',bg:'#DFF6F3',ic:'💬'},g:{n:'gram',c:'#F2711C',bg:'#FFEBDD',ic:'🧱'}};
const LANGOF=cid=>(typeof COURSES!=='undefined'&&COURSES[cid]&&COURSES[cid].tts)||'en-US';
const ic=(a,px)=>{px=px||56;if(typeof a==='string'&&a.startsWith('flag:')&&typeof fxIcon==='function')return fxIcon(a,Math.round(px*1.1));return `<span class="qz-em" style="font-size:${px}px">${esc(a)}</span>`};
const say=(t,lang,slow,who)=>{try{if(typeof speak==='function')speak(String(t).replace(/\*\*/g,''),lang||'en-US',null,who||null,!!slow)}catch(e){}};
const DATA={};
async function load(cid){
  if(DATA[cid]!==undefined)return DATA[cid];
  try{const r=await fetch('data/quiz_'+cid+'.json');if(!r.ok)throw 0;const j=await r.json();DATA[cid]=j.quizzes||[]}catch(e){DATA[cid]=null}
  return DATA[cid];
}
const prog=()=>store.get('quiz',{});
const keyQ=(cid,n)=>cid+'-'+n;

/* ---------- cenas pequenas ---------- */
const BG={
 street:`<rect width="300" height="120" fill="#CDEBFF"/><circle cx="244" cy="26" r="14" fill="#FFE9A0"/><g fill="#B8D6F2"><rect x="10" y="40" width="44" height="80"/><rect x="60" y="22" width="38" height="98"/><rect x="104" y="48" width="50" height="72"/><rect x="190" y="34" width="46" height="86"/><rect x="242" y="52" width="48" height="68"/></g><g fill="#fff" opacity=".7"><rect x="18" y="50" width="6" height="8"/><rect x="30" y="50" width="6" height="8"/><rect x="68" y="34" width="6" height="8"/><rect x="80" y="34" width="6" height="8"/><rect x="198" y="46" width="6" height="8"/></g><rect y="98" width="300" height="22" fill="#8FA3BD"/><path d="M0 108 H300" stroke="#fff" stroke-width="2" stroke-dasharray="14 12" opacity=".7"/>`,
 cafe:`<rect width="300" height="120" fill="#FFE8D2"/><rect x="20" y="14" width="260" height="60" rx="8" fill="#FFF7EC" stroke="#F0C9A0" stroke-width="3"/><path d="M20 14 h260 v14 h-260z" fill="#F2711C"/>${[0,1,2,3,4,5,6,7,8].map(i=>`<path d="M${20+i*29} 28 q14.5 12 29 0z" fill="${i%2?'#fff':'#F2711C'}"/>`).join('')}<rect y="96" width="300" height="24" fill="#E7B98F"/><circle cx="250" cy="52" r="10" fill="#C9884A" opacity=".4"/>`,
 subway:`<rect width="300" height="120" fill="#D8F3EE"/><g fill="#BFE6DE">${[0,1,2,3,4,5,6,7].map(i=>`<rect x="${i*40}" y="0" width="38" height="70"/>`).join('')}</g><rect x="0" y="60" width="300" height="16" fill="#0FA79B" opacity=".5"/><rect x="40" y="82" width="220" height="16" rx="8" fill="#F6C945"/><rect y="98" width="300" height="22" fill="#9FB8B3"/><path d="M0 98 H300" stroke="#F6C945" stroke-width="3"/>`,
 hotel:`<rect width="300" height="120" fill="#EDE5FF"/><rect x="26" y="16" width="52" height="70" rx="26" fill="#fff" stroke="#CDBCF5" stroke-width="3"/><rect x="224" y="16" width="52" height="70" rx="26" fill="#fff" stroke="#CDBCF5" stroke-width="3"/><rect x="100" y="52" width="100" height="40" rx="6" fill="#7C4DFF" opacity=".85"/><rect x="108" y="60" width="84" height="6" rx="3" fill="#fff" opacity=".6"/><rect y="98" width="300" height="22" fill="#CFC0F2"/>`,
 airport:`<rect width="300" height="120" fill="#D6EEFF"/><g fill="#fff" opacity=".9"><ellipse cx="60" cy="30" rx="34" ry="9"/><ellipse cx="86" cy="24" rx="22" ry="8"/><ellipse cx="230" cy="40" rx="38" ry="10"/></g><path d="M180 70 L260 56 L272 60 L196 78Z" fill="#fff" stroke="#B9D9F2"/><rect y="98" width="300" height="22" fill="#A9B8C9"/><path d="M0 108 H300" stroke="#fff" stroke-width="2" stroke-dasharray="16 12" opacity=".7"/>`,
 lobby:`<rect width="300" height="120" fill="#FFF0E0"/><rect x="0" y="0" width="300" height="14" fill="#F2A65A" opacity=".5"/><rect x="30" y="22" width="70" height="52" rx="6" fill="#fff" stroke="#F0D2AE" stroke-width="3"/><rect x="38" y="30" width="54" height="8" rx="3" fill="#F2711C" opacity=".35"/><rect x="38" y="44" width="38" height="6" rx="3" fill="#F0D2AE"/><rect x="200" y="22" width="70" height="60" rx="6" fill="#E6F3FF" stroke="#BBD9F3" stroke-width="3"/><path d="M235 22v60M200 52h70" stroke="#BBD9F3" stroke-width="3"/><rect y="98" width="300" height="22" fill="#E8C9A0"/>`,
 station:`<rect width="300" height="120" fill="#E3EAF5"/><g fill="#CBD6E8">${[0,1,2,3,4,5].map(i=>`<rect x="${i*52+6}" y="16" width="14" height="82"/>`).join('')}</g><rect x="0" y="52" width="300" height="12" fill="#4F7CFF" opacity=".35"/><rect x="200" y="40" width="46" height="58" rx="6" fill="#fff" stroke="#9FB4D8" stroke-width="3"/><path d="M212 98V60M234 98V60" stroke="#9FB4D8" stroke-width="3"/><rect y="98" width="300" height="22" fill="#A9B8CF"/>`,
 park:`<rect width="300" height="120" fill="#DDF5E3"/><circle cx="40" cy="26" r="12" fill="#FFE9A0"/><g fill="#7FCB93"><circle cx="210" cy="56" r="26"/><circle cx="244" cy="62" r="22"/></g><rect x="206" y="70" width="8" height="30" fill="#8B6B4A"/><rect y="96" width="300" height="24" fill="#9CD9A8"/>`
};
function scene(bg,cast,pt){
  const back=BG[bg]||BG.street;
  const c=(cast||[]).filter(Boolean);
  const chars=c.slice(0,2),props=[];
  const pos=[['18%','bottom:8px'],['72%','bottom:8px']];
  let html=`<div class="qz-scene"><svg viewBox="0 0 300 120" preserveAspectRatio="xMidYMid slice" aria-hidden="true">${back}</svg>`;
  chars.forEach((a,i)=>{const big=/^[\u{1F300}-\u{1FAFF}]|^flag:/u.test(a)&&!/\u{200D}/u.test(a)&&i===1&&chars.length===2&&props.length===0;html+=`<div class="qz-cast c${i}">${ic(a,i===0?54:48)}</div>`});
  props.forEach((a,i)=>{html+=`<div class="qz-prop p${i}">${ic(a,36)}</div>`});
  return html+`</div>`;
}

/* ---------- sessão ---------- */
let S=null;
function el(){return document.getElementById('qzx')}
function pickRapid(items,n){
  if(items.length<=n)return items.slice();
  const out=[];const step=items.length/n;for(let i=0;i<n;i++)out.push(items[Math.floor(i*step)]);return out;
}
async function openHub(cid){
  cid=cid||'en-a1';
  const qs=await load(cid);
  const root=shell();
  const p=prog();
  root.innerHTML=`<div class="qz-top"><button class="qz-x" aria-label="${esc(k('close'))}">×</button><div class="qz-title"><b>🧠 ${esc(k('sec'))}</b><small>${esc(k('secSub'))}</small></div></div>
   <div class="qz-hub">${qs&&qs.length?qs.map(q=>cardHTML(cid,q,p)).join(''):`<p class="qz-empty">${esc(k('noQuiz'))}</p>`}</div>`;
  root.querySelector('.qz-x').onclick=closeAll;
  root.querySelectorAll('[data-qz]').forEach(b=>b.onclick=()=>choose(cid,+b.dataset.qz));
}
function cardHTML(cid,q,p){
  const r=p[keyQ(cid,q.n)],st=r?r.stars:0;
  return `<button class="qz-card" data-qz="${q.n}"><span class="qz-ico">${ic(q.icon,34)}</span><span class="qz-info"><small>${esc(k('ep'))} ${(q.n-9800)}</small><b>${esc(q.title)}</b><span class="qz-tags">${q.tags.map((t,i)=>`<i class="t${i}">${esc(t)}</i>`).join('')}</span></span><span class="qz-stars" aria-label="${st} ${esc(k('stars'))}">${[1,2,3].map(i=>`<s class="${i<=st?'on':''}">★</s>`).join('')}${r?`<small>${esc(k('best'))} ${r.best}%</small>`:''}</span></button>`;
}
function shell(){
  closeAll();
  const root=document.createElement('div');root.id='qzx';root.className='qzx';root.setAttribute('role','dialog');root.setAttribute('aria-modal','true');
  document.body.appendChild(root);document.body.classList.add('pgs-open');return root;
}
function closeAll(){const e=el();if(e)e.remove();document.body.classList.remove('pgs-open');try{speechSynthesis.cancel()}catch(x){}S=null}
async function choose(cid,n){
  const qs=await load(cid),q=(qs||[]).find(x=>x.n===n);if(!q)return;
  const root=shell();
  root.innerHTML=`<div class="qz-top"><button class="qz-x" aria-label="${esc(k('close'))}">×</button><div class="qz-title"><b>${esc(q.title)}</b><small>${esc(k('ep'))} ${n-9800}</small></div></div>
  <div class="qz-pre"><div class="qz-hero">${ic(q.icon,64)}</div><h2>${esc(k('choose'))}</h2>
   <button class="qz-mode" data-m="quick"><b>⚡ ${esc(k('quick'))} · 10 ${esc(k('qs'))}</b><small>${esc(k('quickD'))}</small></button>
   <button class="qz-mode" data-m="full"><b>🎯 ${esc(k('full'))} · ${q.items.length} ${esc(k('qs'))}</b><small>${esc(k('fullD'))}</small></button>
   <div class="qz-tags big">${q.tags.map((t,i)=>`<i class="t${i}">${esc(t)}</i>`).join('')}</div></div>`;
  root.querySelector('.qz-x').onclick=()=>openHub(cid);
  root.querySelectorAll('[data-m]').forEach(b=>b.onclick=()=>start(cid,q,b.dataset.m==='quick'?pickRapid(q.items,10):q.items.slice()));
}
function start(cid,q,items,retry){
  const root=shell();
  S={cid,q,items,i:0,ok:0,streak:0,maxStreak:0,xp:0,sk:{v:[0,0],e:[0,0],g:[0,0],c:[0,0]},missed:[],retry:!!retry,lang:LANGOF(cid)};
  root.innerHTML=`<div class="qz-top"><button class="qz-x" aria-label="${esc(k('close'))}">×</button><div class="qz-bar"><i id="qzbar"></i></div><span class="qz-streak" id="qzst">🔥 0</span></div>
   <div class="qz-body" id="qzbody"></div><div class="qz-foot" id="qzfoot"></div>`;
  root.querySelector('.qz-x').onclick=confirmExit;
  next();
}
function confirmExit(){
  const root=el();if(!root||root.querySelector('.qz-modal'))return;
  const m=document.createElement('div');m.className='qz-modal';m.innerHTML=`<div class="qz-mcard"><b>${esc(k('exit'))}</b><p>${esc(k('exitD'))}</p><button class="qz-btn" id="qzstay">${esc(k('stay'))}</button><button class="qz-btn ghost" id="qzleave">${esc(k('leave'))}</button></div>`;
  root.appendChild(m);m.querySelector('#qzstay').onclick=()=>m.remove();m.querySelector('#qzleave').onclick=()=>openHub(S&&S.cid);
}
function next(){
  if(!S)return;
  const it=S.items[S.i];
  if(!it){return finish()}
  const body=document.getElementById('qzbody'),foot=document.getElementById('qzfoot');
  document.getElementById('qzbar').style.width=Math.round(S.i/S.items.length*100)+'%';
  document.getElementById('qzst').textContent='🔥 '+S.streak;
  foot.innerHTML='';foot.className='qz-foot';
  body.scrollTop=0;
  const s=SK[it.sk]||SK.v;
  body.innerHTML=`<div class="qz-q" style="--sk:${s.c};--skb:${s.bg}"><div class="qz-chip"><span>${s.ic}</span>${esc(k(s.n))}</div><div class="qz-h">${esc(promptOf(it))}</div><div class="qz-stage" id="qzstage"></div></div>`;
  const stage=document.getElementById('qzstage');
  R[it.t](it,stage);
}
function promptOf(it){return {see:it.q||k('see'),hear:k('hear'),match:k('match'),ctx:k('ctxT'),react:k('reactT'),dialog:k('dialogT'),order:k('orderT'),fill:k('fillT'),build:k('buildT'),fix:k('fixT'),type:it.hint||(it.art?k('typeT'):k('dictT')),tf:k('tfT'),ask:it.title||k('askT'),multi:k('multiT'),read:k('readT')}[it.t]}

/* resposta + painel de feedback */
function answer(it,ok,right,opt){
  opt=opt||{};
  const s=SK[it.sk]||SK.v;S.sk[it.sk][1]++;if(ok){S.sk[it.sk][0]++;S.ok++;S.streak++;S.maxStreak=Math.max(S.maxStreak,S.streak);S.xp+=2+(S.streak>=3?1:0)}else{S.streak=0;S.missed.push(it);logMiss(it)}
  try{if(typeof beep==='function')beep(ok);if(ok&&typeof confetti==='function'&&S.streak>=3)confetti(24)}catch(e){}
  document.getElementById('qzst').textContent='🔥 '+S.streak;
  const foot=document.getElementById('qzfoot');foot.className='qz-foot fb '+(ok?'ok':'no');
  const msg=ok?(k('ok')[Math.floor(Math.random()*k('ok').length)]):(k('no')[Math.floor(Math.random()*k('no').length)]);
  foot.innerHTML=`<div class="qz-fb"><div class="qz-fbh"><span class="qz-fbi">${ok?'✓':'✕'}</span><b>${esc(msg)}</b>${opt.audio?`<button class="qz-ear" id="qzear" aria-label="${esc(k('listen'))}">🔊</button>`:''}</div>${!ok&&right?`<div class="qz-right"><small>${esc(k('right'))}</small><span>${bold(right)}</span></div>`:''}<p>${bold(it.why||'')}</p><button class="qz-btn ${ok?'':'red'}" id="qznext">${esc(k('cont'))}</button></div>`;
  const ear=document.getElementById('qzear');if(ear)ear.onclick=()=>say(opt.audio,S.lang);
  document.getElementById('qznext').onclick=()=>{S.i++;next()};
  if(opt.audio&&ok)say(opt.audio,S.lang);
  document.getElementById('qznext').focus();
}
function logMiss(it){
  try{if(!window.PogPath||!S)return;
    if(['ctx','react','dialog','fill','ask','read'].includes(it.t)){
      const q=it.t==='ctx'?it.bubble:it.t==='react'?it.line:it.t==='dialog'?it.turns[it.turns.length-1][1]:(it.t==='ask'||it.t==='read')?it.q:it.s;
      const opts=it.opts.map(o=>typeof o==='string'?o:o.w);
      PogPath.miss({kind:'choose',cid:S.cid,n:S.q.n,q,opts,a:opts[it.a],ai:it.a,why:it.why,lang:S.lang});
    }
  }catch(e){}
}
function disableAll(root,sel){root.querySelectorAll(sel).forEach(b=>b.disabled=true)}
const L=o=>typeof o==='string'?o:o.w;

/* ---------- renderizadores ---------- */
const R={};
/* escolhas: embaralha opções mantendo o gabarito */
function shuffled(it){const idx=shuf(it.opts.map((_,i)=>i));return idx.map(i=>({o:it.opts[i],i}))}
function pickBtns(stage,it,mk,cls){
  const sh=shuffled(it);
  const grid=document.createElement('div');grid.className='qz-opts '+(cls||'');
  grid.innerHTML=sh.map((x,j)=>mk(x.o,j,x.i)).join('');
  stage.appendChild(grid);
  return {grid,sh};
}
R.see=(it,stage)=>{
  stage.innerHTML=`<div class="qz-big">${ic(it.art,92)}</div>`;
  const {grid}=pickBtns(stage,it,(o,j,i)=>`<button class="qz-o" data-i="${i}">${esc(o)}</button>`,'two');
  grid.querySelectorAll('.qz-o').forEach(b=>b.onclick=()=>{
    const i=+b.dataset.i,ok=i===it.a;disableAll(grid,'.qz-o');
    grid.querySelectorAll('.qz-o').forEach(x=>{if(+x.dataset.i===it.a)x.classList.add('ok');else if(x===b)x.classList.add('no')});
    answer(it,ok,it.opts[it.a],{audio:it.say})});
};
R.hear=(it,stage)=>{
  stage.innerHTML=`<div class="qz-listen"><button class="qz-spk" id="qzsp" aria-label="${esc(k('listen'))}">🔊</button><button class="qz-slow" id="qzsl">🐢 ${esc(k('slow'))}</button></div>`;
  const {grid}=pickBtns(stage,it,(o,j,i)=>`<button class="qz-o img" data-i="${i}">${ic(o,64)}</button>`,'two');
  const p=()=>say(it.say,S.lang);stage.querySelector('#qzsp').onclick=p;stage.querySelector('#qzsl').onclick=()=>say(it.say,S.lang,true);setTimeout(p,350);
  grid.querySelectorAll('.qz-o').forEach(b=>b.onclick=()=>{
    const i=+b.dataset.i,ok=i===it.a;disableAll(grid,'.qz-o');
    grid.querySelectorAll('.qz-o').forEach(x=>{if(+x.dataset.i===it.a)x.classList.add('ok');else if(x===b)x.classList.add('no')});
    answer(it,ok,it.say)});
};
R.ctx=(it,stage)=>{
  const parts=it.bubble.split('___');
  stage.innerHTML=`${scene(it.bg,it.cast)}<div class="qz-bub">${esc(parts[0])}<span class="qz-gap" id="qzgap">?</span>${esc(parts[1]||'')}<button class="qz-ear sm" id="qzbs" aria-label="${esc(k('listen'))}">🔊</button></div><div class="qz-pt">${esc(it.pt||'')}</div>`;
  const {grid}=pickBtns(stage,it,(o,j,i)=>`<button class="qz-o" data-i="${i}">${esc(L(o))}</button>`,'three');
  stage.querySelector('#qzbs').onclick=()=>say(it.bubble.replace('___',L(it.opts[it.a])),S.lang);
  grid.querySelectorAll('.qz-o').forEach(b=>b.onclick=()=>{
    const i=+b.dataset.i,ok=i===it.a;disableAll(grid,'.qz-o');
    const gap=document.getElementById('qzgap');gap.textContent=L(it.opts[i]);gap.classList.add(ok?'ok':'no');
    grid.querySelectorAll('.qz-o').forEach(x=>{if(+x.dataset.i===it.a)x.classList.add('ok');else if(x===b)x.classList.add('no')});
    if(!ok)setTimeout(()=>{gap.textContent=L(it.opts[it.a]);gap.classList.remove('no');gap.classList.add('ok')},650);
    answer(it,ok,it.bubble.replace('___','**'+L(it.opts[it.a])+'**'),{audio:it.bubble.replace('___',L(it.opts[it.a]))})});
};
R.react=(it,stage)=>{
  stage.innerHTML=`${scene(it.bg,it.cast)}<div class="qz-bub said"><small>${esc(k('sentSaid'))}</small>“${esc(it.line)}”<button class="qz-ear sm" id="qzbs" aria-label="${esc(k('listen'))}">🔊</button></div><div class="qz-pt">${esc(it.pt||'')}</div>`;
  const {grid}=pickBtns(stage,it,(o,j,i)=>`<button class="qz-o long" data-i="${i}">${esc(o)}</button>`,'col');
  const p=()=>say(it.line,S.lang);stage.querySelector('#qzbs').onclick=p;setTimeout(p,400);
  grid.querySelectorAll('.qz-o').forEach(b=>b.onclick=()=>{
    const i=+b.dataset.i,ok=i===it.a;disableAll(grid,'.qz-o');
    grid.querySelectorAll('.qz-o').forEach(x=>{if(+x.dataset.i===it.a)x.classList.add('ok');else if(x===b)x.classList.add('no')});
    answer(it,ok,it.opts[it.a],{audio:it.opts[it.a]})});
};
R.dialog=(it,stage)=>{
  const names=[...new Set(it.turns.map(t=>t[0]))];
  const av=['🧑🏽','🧑🏻‍🦱','🧑🏿','👩🏼'];
  const rows=it.turns.map((t,j)=>{const me=names.indexOf(t[0])%2===1,parts=t[1].split('___');
    return `<div class="qz-msg ${me?'me':''}"><span class="qz-av">${av[names.indexOf(t[0])%4]}</span><div class="qz-m"><small>${esc(t[0])}</small><div>${esc(parts[0])}${parts.length>1?`<span class="qz-gap" id="qzgap">?</span>${esc(parts[1])}`:''}</div></div></div>`}).join('');
  stage.innerHTML=`<div class="qz-chat">${rows}</div>${it.pt?`<div class="qz-pt">${esc(it.pt)}</div>`:''}`;
  const {grid}=pickBtns(stage,it,(o,j,i)=>`<button class="qz-o" data-i="${i}">${esc(o)}</button>`,'col');
  const full=o=>it.turns.map(t=>t[1].replace('___',o)).join(' ');
  grid.querySelectorAll('.qz-o').forEach(b=>b.onclick=()=>{
    const i=+b.dataset.i,ok=i===it.a;disableAll(grid,'.qz-o');
    const gap=document.getElementById('qzgap');gap.textContent=it.opts[i];gap.classList.add(ok?'ok':'no');
    grid.querySelectorAll('.qz-o').forEach(x=>{if(+x.dataset.i===it.a)x.classList.add('ok');else if(x===b)x.classList.add('no')});
    if(!ok)setTimeout(()=>{gap.textContent=it.opts[it.a];gap.classList.remove('no');gap.classList.add('ok')},650);
    const last=it.turns[it.turns.length-1][1].replace('___',it.opts[it.a]);
    answer(it,ok,'**'+it.opts[it.a]+'**',{audio:last})});
};
R.fill=(it,stage)=>{
  const parts=it.s.split('___');
  stage.innerHTML=`<div class="qz-fillcard">${it.art?`<div class="qz-fa">${ic(it.art,58)}</div>`:''}<div class="qz-fs">${esc(parts[0])}<span class="qz-gap" id="qzgap">?</span>${esc(parts[1]||'')}</div><div class="qz-pt">${esc(it.pt||'')}</div></div>`;
  const {grid}=pickBtns(stage,it,(o,j,i)=>`<button class="qz-o" data-i="${i}">${esc(o)}</button>`,'three');
  grid.querySelectorAll('.qz-o').forEach(b=>b.onclick=()=>{
    const i=+b.dataset.i,ok=i===it.a;disableAll(grid,'.qz-o');
    const gap=document.getElementById('qzgap');gap.textContent=it.opts[i];gap.classList.add(ok?'ok':'no');
    grid.querySelectorAll('.qz-o').forEach(x=>{if(+x.dataset.i===it.a)x.classList.add('ok');else if(x===b)x.classList.add('no')});
    if(!ok)setTimeout(()=>{gap.textContent=it.opts[it.a];gap.classList.remove('no');gap.classList.add('ok')},650);
    answer(it,ok,it.s.replace('___','**'+it.opts[it.a]+'**'),{audio:it.s.replace('___',it.opts[it.a])})});
};
R.tf=(it,stage)=>{
  stage.innerHTML=`${it.art?`<div class="qz-big">${ic(it.art,92)}</div>`:''}<div class="qz-stmt">${esc(it.stmt)}<button class="qz-ear sm" id="qzbs" aria-label="${esc(k('listen'))}">🔊</button></div><div class="qz-opts two"><button class="qz-o tf t" data-v="1">✓ ${esc(k('tru'))}</button><button class="qz-o tf f" data-v="0">✕ ${esc(k('fal'))}</button></div>`;
  stage.querySelector('#qzbs').onclick=()=>say(it.stmt,S.lang);
  stage.querySelectorAll('.tf').forEach(b=>b.onclick=()=>{
    const v=b.dataset.v==='1',ok=v===it.a;disableAll(stage,'.tf');
    stage.querySelectorAll('.tf').forEach(x=>{if((x.dataset.v==='1')===it.a)x.classList.add('ok');else if(x===b)x.classList.add('no')});
    answer(it,ok,it.a?k('tru'):k('fal'),{audio:it.stmt})});
};
R.match=(it,stage)=>{
  const L1=shuf(it.pairs.map((p,i)=>({w:p[0],i}))),R1=shuf(it.pairs.map((p,i)=>({a:p[1],i})));
  stage.innerHTML=`<div class="qz-match"><div class="col">${L1.map(x=>`<button class="qz-mw" data-i="${x.i}">${esc(x.w)}</button>`).join('')}</div><div class="col">${R1.map(x=>`<button class="qz-ma" data-i="${x.i}">${ic(x.a,40)}</button>`).join('')}</div></div>`;
  let sel=null,done=0,err=0;const total=it.pairs.length;
  stage.querySelectorAll('.qz-mw,.qz-ma').forEach(b=>b.onclick=()=>{
    if(b.classList.contains('lock'))return;
    if(b.classList.contains('qz-mw'))say(it.pairs[+b.dataset.i][0],S.lang);
    if(!sel||sel.className!==b.className&&false){}
    if(sel&&sel!==b&&sel.className.split(' ')[0]!==b.className.split(' ')[0]){
      const a=sel,c=b;sel.classList.remove('sel');sel=null;
      if(a.dataset.i===c.dataset.i){[a,c].forEach(x=>{x.classList.add('lock');x.classList.add('ok')});done++;if(done===total){const ok=err<=1;answer(it,ok,it.pairs.map(p=>p[0]).join(' · '))}}
      else{err++;[a,c].forEach(x=>x.classList.add('shake'));setTimeout(()=>[a,c].forEach(x=>x.classList.remove('shake')),420)}
      return}
    if(sel)sel.classList.remove('sel');sel=b;b.classList.add('sel')});
  const foot=document.getElementById('qzfoot');foot.innerHTML='';
};
R.order=(it,stage)=>{
  const items=it.lines.map((l,i)=>({who:l[0],t:l[1],i}));const bank=shuf(items);const placed=[];
  const draw=()=>{
    stage.innerHTML=`<div class="qz-ord"><div class="qz-ordl" id="qzo">${placed.length?placed.map((x,j)=>`<button class="qz-ol placed" data-j="${j}"><em>${j+1}</em><span><small>${esc(x.who)}</small>${esc(x.t)}</span></button>`).join(''):`<div class="qz-hint">${esc(k('tapEach'))}</div>`}</div>
     <div class="qz-bank">${bank.filter(x=>!placed.includes(x)).map(x=>`<button class="qz-ol" data-b="${x.i}"><span><small>${esc(x.who)}</small>${esc(x.t)}</span></button>`).join('')}</div></div>`;
    stage.querySelectorAll('[data-b]').forEach(b=>b.onclick=()=>{const x=items[+b.dataset.b];placed.push(x);say(x.t,S.lang,false,x.who);draw()});
    stage.querySelectorAll('[data-j]').forEach(b=>b.onclick=()=>{placed.splice(+b.dataset.j,1);draw()});
    const foot=document.getElementById('qzfoot');
    foot.className='qz-foot';foot.innerHTML=`<button class="qz-btn" id="qzck" ${placed.length===items.length?'':'disabled'}>${esc(k('check'))}</button>`;
    document.getElementById('qzck').onclick=()=>{
      const ok=placed.every((x,j)=>x.i===j);
      stage.querySelectorAll('.qz-ol.placed').forEach((b,j)=>b.classList.add(placed[j].i===j?'ok':'no'));
      answer(it,ok,it.lines.map(l=>l[0]+': '+l[1]).join('  ›  '),{audio:null})};
  };
  draw();
};
R.build=(it,stage)=>{
  const words=it.ans.split(' ');const bank=shuf([...words,...(it.extra||[])].map((w,i)=>({w,i,u:false})));const slots=[];
  const draw=()=>{
    stage.innerHTML=`<div class="qz-pt top">${esc(it.pt||'')}<button class="qz-ear sm" id="qzbs" aria-label="${esc(k('listen'))}">🔊</button></div><div class="qz-slots" id="qzsl">${slots.length?slots.map((x,j)=>`<button class="qz-w in" data-j="${j}">${esc(x.w)}</button>`).join(''):''}</div><div class="qz-bank w">${bank.map(x=>`<button class="qz-w ${x.u?'used':''}" data-i="${x.i}" ${x.u?'disabled':''}>${esc(x.w)}</button>`).join('')}</div>`;
    stage.querySelector('#qzbs').onclick=()=>say(it.ans,S.lang);
    stage.querySelectorAll('.qz-w[data-i]').forEach(b=>b.onclick=()=>{const x=bank.find(y=>y.i===+b.dataset.i);x.u=true;slots.push(x);draw()});
    stage.querySelectorAll('.qz-w[data-j]').forEach(b=>b.onclick=()=>{const x=slots.splice(+b.dataset.j,1)[0];x.u=false;draw()});
    const foot=document.getElementById('qzfoot');foot.className='qz-foot';foot.innerHTML=`<button class="qz-btn" id="qzck" ${slots.length?'':'disabled'}>${esc(k('check'))}</button>`;
    document.getElementById('qzck').onclick=()=>{
      const got=slots.map(x=>x.w).join(' '),ok=got===it.ans;
      stage.querySelectorAll('.qz-w.in').forEach(b=>b.classList.add(ok?'ok':'no'));
      stage.querySelectorAll('.qz-w').forEach(b=>b.disabled=true);
      answer(it,ok,it.ans,{audio:it.ans})};
  };
  draw();
};
R.fix=(it,stage)=>{
  const toks=it.text.split(' ');let step=1,chosen=-1;
  const draw=()=>{
    stage.innerHTML=`<div class="qz-fixcard">${it.pt?`<div class="qz-pt top">${esc(it.pt)}</div>`:''}<div class="qz-toks">${toks.map((w,j)=>`<button class="qz-tk ${chosen===j?(j===it.wrong?'bad':'no'):''}" data-j="${j}" ${step===2?'disabled':''}>${esc(w)}</button>`).join('')}</div></div>${step===2?`<div class="qz-h2">${esc(k('fixT2'))}</div>`:''}<div id="qzfo"></div>`;
    if(step===1){stage.querySelectorAll('.qz-tk').forEach(b=>b.onclick=()=>{
        const j=+b.dataset.j;chosen=j;
        if(j===it.wrong){step=2;draw();opts()}
        else{stage.querySelectorAll('.qz-tk').forEach(x=>x.disabled=true);b.classList.add('no');stage.querySelectorAll('.qz-tk')[it.wrong].classList.add('bad');answer(it,false,it.text.split(' ').map((w,jj)=>jj===it.wrong?'**'+it.opts[it.a]+'**':w).join(' '),{audio:it.text.split(' ').map((w,jj)=>jj===it.wrong?it.opts[it.a]:w).join(' ')})}})}
  };
  const opts=()=>{
    const host=stage.querySelector('#qzfo');const sh=shuffled(it);
    host.innerHTML=`<div class="qz-opts three">${sh.map(x=>`<button class="qz-o" data-i="${x.i}">${esc(x.o)}</button>`).join('')}</div>`;
    host.querySelectorAll('.qz-o').forEach(b=>b.onclick=()=>{
      const i=+b.dataset.i,ok=i===it.a;disableAll(host,'.qz-o');
      host.querySelectorAll('.qz-o').forEach(x=>{if(+x.dataset.i===it.a)x.classList.add('ok');else if(x===b)x.classList.add('no')});
      const fixed=toks.map((w,jj)=>jj===it.wrong?it.opts[it.a]:w).join(' ');
      answer(it,ok,toks.map((w,jj)=>jj===it.wrong?'**'+it.opts[it.a]+'**':w).join(' '),{audio:fixed})});
  };
  draw();
};

R.ask=(it,stage)=>{
  stage.innerHTML=`<div class="qz-stmt qz-ask">${bold(it.q)}${it.say?`<button class="qz-ear sm" id="qzbs" aria-label="${esc(k('listen'))}">🔊</button>`:''}</div>${it.pt?`<div class="qz-pt">${esc(it.pt)}</div>`:''}`;
  const cls=it.opts.some(o=>String(L(o)).length>16)?'col':'two';
  const {grid}=pickBtns(stage,it,(o,j,i)=>`<button class="qz-o ${cls==='col'?'long':''}" data-i="${i}">${esc(L(o))}</button>`,cls);
  const b=stage.querySelector('#qzbs');if(b)b.onclick=()=>say(it.say,S.lang);
  grid.querySelectorAll('.qz-o').forEach(b=>b.onclick=()=>{
    const i=+b.dataset.i,ok=i===it.a;disableAll(grid,'.qz-o');
    grid.querySelectorAll('.qz-o').forEach(x=>{if(+x.dataset.i===it.a)x.classList.add('ok');else if(x===b)x.classList.add('no')});
    answer(it,ok,L(it.opts[it.a]),{audio:it.say||null})});
};
R.read=(it,stage)=>{
  stage.innerHTML=`<div class="qz-passage">${it.lines.map(l=>`<p>${bold(l)}</p>`).join('')}<button class="qz-ear sm" id="qzbs" aria-label="${esc(k('listen'))}">🔊 </button></div><div class="qz-stmt qz-ask">${bold(it.q)}</div>`;
  stage.querySelector('#qzbs').onclick=()=>say(it.lines.join(' ').replace(/\*\*/g,''),S.lang);
  const cls=it.opts.some(o=>String(o).length>16)?'col':'two';
  const {grid}=pickBtns(stage,it,(o,j,i)=>`<button class="qz-o ${cls==='col'?'long':''}" data-i="${i}">${esc(o)}</button>`,cls);
  grid.querySelectorAll('.qz-o').forEach(b=>b.onclick=()=>{
    const i=+b.dataset.i,ok=i===it.a;disableAll(grid,'.qz-o');
    grid.querySelectorAll('.qz-o').forEach(x=>{if(+x.dataset.i===it.a)x.classList.add('ok');else if(x===b)x.classList.add('no')});
    answer(it,ok,it.opts[it.a])});
};
R.multi=(it,stage)=>{
  const sh=shuffled(it);const sel=new Set();
  stage.innerHTML=`<div class="qz-stmt qz-ask">${bold(it.q)}</div><div class="qz-hint" style="padding:0">${esc(k('tapAll'))}</div><div class="qz-opts col" id="qzmo">${sh.map(x=>`<button class="qz-o long chk" data-i="${x.i}"><span class="bx"></span>${esc(L(x.o))}</button>`).join('')}</div>`;
  const foot=document.getElementById('qzfoot');foot.className='qz-foot';foot.innerHTML=`<button class="qz-btn" id="qzck" disabled>${esc(k('check'))}</button>`;
  const ck=document.getElementById('qzck');
  stage.querySelectorAll('.chk').forEach(b=>b.onclick=()=>{const i=+b.dataset.i;if(sel.has(i)){sel.delete(i);b.classList.remove('sel')}else{sel.add(i);b.classList.add('sel')}ck.disabled=!sel.size});
  ck.onclick=()=>{
    const want=new Set(it.a);let ok=sel.size===want.size&&[...sel].every(i=>want.has(i));
    stage.querySelectorAll('.chk').forEach(b=>{const i=+b.dataset.i;b.disabled=true;if(want.has(i))b.classList.add('ok');else if(sel.has(i))b.classList.add('no')});
    answer(it,ok,it.a.map(i=>L(it.opts[i])).join(' · '))};
};
const norm=s=>String(s||'').toLowerCase().replace(/[^a-z0-9’' ]/g,'').replace(/’/g,"'").replace(/\s+/g,' ').trim();
R.type=(it,stage)=>{
  stage.innerHTML=`${it.art?`<div class="qz-big">${ic(it.art,92)}</div>`:`<div class="qz-listen"><button class="qz-spk" id="qzsp" aria-label="${esc(k('listen'))}">🔊</button><button class="qz-slow" id="qzsl">🐢 ${esc(k('slow'))}</button></div>`}<div class="qz-blanks">${it.ans.split('').filter(c=>/[A-Za-z0-9]/.test(c)||c===' ').map(c=>c===' '?'<span class="sp"></span>':'<i></i>').join('')}</div><input class="qz-in" id="qzin" type="text" autocomplete="off" autocapitalize="none" spellcheck="false" placeholder="${esc(k('type'))}" aria-label="${esc(k('type'))}"><button class="qz-ear" id="qzbs" style="margin:6px auto 0" aria-label="${esc(k('listen'))}">🔊</button>`;
  const inp=stage.querySelector('#qzin');const sp=stage.querySelector('#qzsp'),sl=stage.querySelector('#qzsl');if(sp){sp.onclick=()=>say(it.ans,S.lang);sl.onclick=()=>say(it.ans,S.lang,true);setTimeout(()=>say(it.ans,S.lang),350);stage.querySelector('#qzbs').style.display='none'}else stage.querySelector('#qzbs').onclick=()=>say(it.ans,S.lang);
  const foot=document.getElementById('qzfoot');foot.className='qz-foot';foot.innerHTML=`<button class="qz-btn" id="qzck" disabled>${esc(k('check'))}</button>`;
  const ck=document.getElementById('qzck');
  inp.oninput=()=>{ck.disabled=!inp.value.trim();const v=norm(inp.value);stage.querySelectorAll('.qz-blanks i').forEach((x,j)=>{x.textContent=(v.replace(/ /g,'')[j]||'').toUpperCase()})};
  const go=()=>{if(ck.disabled)return;const v=norm(inp.value),ok=[it.ans,...(it.alts||[])].some(a=>norm(a)===v);inp.disabled=true;inp.classList.add(ok?'ok':'no');answer(it,ok,it.ans,{audio:it.ans})};
  ck.onclick=go;inp.onkeydown=e=>{if(e.key==='Enter')go()};setTimeout(()=>{try{inp.focus()}catch(e){}},300);
};

/* ---------- resultado ---------- */
function finish(){
  const root=el();if(!root)return;
  const tot=S.items.length,pct=Math.round(S.ok/tot*100),stars=pct>=90?3:pct>=70?2:pct>=40?1:0;
  const bonus=5+(stars===3?5:0);const xp=S.xp+bonus;
  if(!S.retry){
    const p=prog(),key=keyQ(S.cid,S.q.n),old=p[key]||{};
    p[key]={best:Math.max(old.best||0,pct),stars:Math.max(old.stars||0,stars),last:pct,n:(old.n||0)+1,date:Date.now(),sk:S.sk};store.set('quiz',p);
  }
  try{ST.xp+=xp;save()}catch(e){}
  try{if(stars>=2&&typeof confetti==='function')confetti(110);if(typeof sfx==='function')sfx('cheer')}catch(e){}
  const bar=(id)=>{const [a,b]=S.sk[id];if(!b)return '';const s=SK[id],pp=Math.round(a/b*100);return `<div class="qz-sk"><span>${s.ic} ${esc(k(s.n))}</span><div class="t"><i style="width:${pp}%;background:${s.c}"></i></div><b>${a}/${b}</b></div>`};
  const msg=S.missed.length===0?k('perfect'):pct>=70?k('great'):pct>=40?k('fair'):k('low');
  root.innerHTML=`<div class="qz-top"><button class="qz-x" aria-label="${esc(k('close'))}">×</button><div class="qz-title"><b>${esc(S.q.title)}</b><small>${esc(k('res'))}</small></div></div>
   <div class="qz-res"><div class="qz-stars big">${[1,2,3].map(i=>`<s class="${i<=stars?'on':''}" style="--d:${i*.18}s">★</s>`).join('')}</div>
   <div class="qz-ring" style="--p:${pct}"><div><b>${pct}%</b><small>${esc(k('acc'))}</small></div></div>
   <p class="qz-msg2">${esc(msg)}</p>
   <div class="qz-chips"><span>+${xp} ${esc(k('xp'))}</span><span>🔥 ${S.maxStreak}</span></div>
   <div class="qz-sks">${bar('v')}${bar('e')}${bar('g')}${bar('c')}</div>
   ${S.missed.length?`<div class="qz-rev"><h3>${esc(k('rev'))}</h3>${S.missed.slice(0,8).map(m=>`<div class="qz-ri">${ic(revArt(m),26)}<span>${bold(revText(m))}</span></div>`).join('')}</div>`:''}
   <div class="qz-acts">${S.missed.length?`<button class="qz-btn" id="qzredo">${esc(k('redo'))}</button>`:''}<button class="qz-btn ${S.missed.length?'ghost':''}" id="qzagain">${esc(k('again'))}</button><button class="qz-btn ghost" id="qzhub">${esc(k('close'))}</button></div></div>`;
  root.querySelector('.qz-x').onclick=()=>{const c=S.cid;openHub(c);refreshHost()};
  const redo=root.querySelector('#qzredo');if(redo)redo.onclick=()=>start(S.cid,S.q,S.missed.slice(),true);
  root.querySelector('#qzagain').onclick=()=>choose(S.cid,S.q.n);
  root.querySelector('#qzhub').onclick=()=>{closeAll();refreshHost()};
}
function revArt(m){return (m.t==='tf'||m.t==='ask'||m.t==='read'||m.t==='multi')?'📝':m.art||(m.cast&&m.cast[m.cast.length-1])||(m.pairs&&m.pairs[0][1])||'📝'}
function revText(m){
  const w=o=>typeof o==='string'?o:o.w;
  if(m.t==='see'||m.t==='hear'||m.t==='type')return '**'+(m.say||m.ans||w(m.opts[m.a]))+'** — '+(m.why||'').replace(/\*\*/g,'');
  if(m.t==='match')return m.pairs.map(p=>p[0]).join(' · ');
  if(m.t==='ctx')return m.bubble.replace('___','**'+w(m.opts[m.a])+'**');
  if(m.t==='react')return '“'+m.line+'” → **'+m.opts[m.a]+'**';
  if(m.t==='dialog')return m.turns[m.turns.length-1][1].replace('___','**'+m.opts[m.a]+'**');
  if(m.t==='fill')return m.s.replace('___','**'+m.opts[m.a]+'**');
  if(m.t==='build')return '**'+m.ans+'**';
  if(m.t==='fix')return m.text.split(' ').map((x,i)=>i===m.wrong?'**'+m.opts[m.a]+'**':x).join(' ');
  if(m.t==='order')return m.lines.map(l=>l[1]).join(' › ');
  if(m.t==='ask'||m.t==='read')return m.q.replace(/\*\*/g,'')+' → **'+w(m.opts[m.a])+'**';
  if(m.t==='multi')return m.a.map(i=>w(m.opts[i])).join(' · ');
  if(m.t==='tf')return m.stmt+' → '+(m.a?k('tru'):k('fal'));
  return m.why||'';
}
function refreshHost(){try{if(typeof P!=='undefined'&&P)return;const h=document.querySelector('.qz-sec');if(h)renderSection(h)}catch(e){}}

/* ---------- entrada na página do curso e na home ---------- */
async function renderSection(host){
  const cid=host.dataset.cid,qs=await load(cid);
  if(!qs||!qs.length){host.remove();return}
  const p=prog();
  host.innerHTML=`<div class="qz-sec-h"><div><h2>🧠 ${esc(k('sec'))}</h2><p>${esc(k('secSub'))}</p></div></div><div class="qz-strip">${qs.map(q=>{const r=p[keyQ(cid,q.n)];return `<button class="qz-mini" data-qz="${q.n}"><span class="qz-ico">${ic(q.icon,30)}</span><b>${esc(q.title)}</b><small>${esc(k('ep'))} ${q.n-9800}${r?' · '+r.best+'%':''}</small><span class="qz-stars sm">${[1,2,3].map(i=>`<s class="${r&&i<=r.stars?'on':''}">★</s>`).join('')}</span></button>`}).join('')}</div>`;
  host.querySelectorAll('[data-qz]').forEach(b=>b.onclick=()=>choose(cid,+b.dataset.qz));
}
{const _course=window.course;if(_course)window.course=function(id){const r=_course.apply(this,arguments);
  try{if(typeof P==='undefined'||!P){const road=document.querySelector('#app .road');if(road&&!document.querySelector('.qz-sec')){const s=document.createElement('section');s.className='qz-sec';s.dataset.cid=id;road.insertAdjacentElement('afterend',s);renderSection(s)}}}catch(e){}
  return r}}
window.PogQuiz={open:openHub,start:choose,load,close:closeAll};
})();
