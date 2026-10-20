/* Pogglot · vida do player: Poggie de volta ao rodapé (com balão e reações) + mais sons.
   Tudo leve e opcional: nada aqui bloqueia o fluxo do episódio. */
(function(){
const q=s=>document.querySelector(s);
const es=()=>{try{return typeof fxEsOn==='function'&&fxEsOn()}catch(e){return false}};
const T=t=>{try{return es()&&typeof fxEs==='function'?fxEs(t):t}catch(e){return t}};
const rnd=a=>a[Math.floor(Math.random()*a.length)];
/* ---------------- sons extras (sintetizados) ---------------- */
const _sfx=window.sfx;let AC2=null;
const ctx=()=>{try{AC2=AC2||new (window.AudioContext||window.webkitAudioContext)();if(AC2.state==='suspended')AC2.resume();return AC2}catch(e){return null}};
function tone(f,d,type,v,at,f2){const a=ctx();if(!a)return;const t=a.currentTime+(at||0),o=a.createOscillator(),g=a.createGain();o.type=type||'sine';o.frequency.setValueAtTime(f,t);if(f2)o.frequency.exponentialRampToValueAtTime(f2,t+d);g.gain.setValueAtTime(0,t);g.gain.linearRampToValueAtTime(v||.08,t+.015);g.gain.exponentialRampToValueAtTime(.0001,t+d);o.connect(g).connect(a.destination);o.start(t);o.stop(t+d+.05)}
function noise(d,fr,Q,v,at){const a=ctx();if(!a)return;const t=a.currentTime+(at||0),n=Math.floor(a.sampleRate*d),b=a.createBuffer(1,n,a.sampleRate),c=b.getChannelData(0);for(let i=0;i<n;i++)c[i]=Math.random()*2-1;const s=a.createBufferSource();s.buffer=b;const f=a.createBiquadFilter();f.type='bandpass';f.frequency.value=fr;f.Q.value=Q||1;const g=a.createGain();g.gain.setValueAtTime(v||.08,t);g.gain.exponentialRampToValueAtTime(.0001,t+d);s.connect(f).connect(g).connect(a.destination);s.start(t)}
const EX={
 page(){noise(.22,2200,.7,.06,0);tone(520,.1,'sine',.04,.02,760)},
 reveal(){[659,880,1175,1568].forEach((f,i)=>tone(f,.2,'sine',.05,i*.06))},
 film(){for(let i=0;i<5;i++)noise(.03,3000,3,.05,i*.05);[392,494,587].forEach((f,i)=>tone(f,.5,'triangle',.05,.28+i*.02))},
 book(){noise(.3,1400,.6,.07,0);tone(262,.35,'sine',.05,.1);tone(392,.4,'sine',.04,.18)},
 music(){[523,659,784,659,880].forEach((f,i)=>tone(f,.18,'triangle',.06,i*.11))},
 tv(){tone(880,.07,'square',.03,0);tone(1320,.12,'square',.03,.09);noise(.1,5000,2,.03,.2)},
 win(){[523,659,784,1046,1319].forEach((f,i)=>tone(f,.22,'triangle',.07,i*.08));noise(.4,3600,.8,.04,.3)},
 tick(){tone(1500,.04,'square',.025,0)},
 coin(){tone(988,.08,'square',.05,0);tone(1319,.3,'square',.05,.08)},
 cheer2(){[523,659,784,1046].forEach((f,i)=>tone(f,.25,'triangle',.08,i*.07));noise(.5,3200,.8,.05,.1);tone(1568,.4,'sine',.05,.3)}
};
window.sfx=function(name){if(EX[name]){try{EX[name]()}catch(e){}return}return _sfx(name)};
const kindOfWork=f=>{const s=[f&&f.tag,f&&(f.chips||[]).join(' '),f&&f.kind,f&&f.work].join(' ').toLowerCase();
  if(/filme|film|cine/.test(s))return'film';if(/série|serie|tv/.test(s))return'tv';if(/can[çc][aã]o|cantiga|música|musica|álbum|album|song|poema/.test(s))return'music';if(/livro|romance|conto|novela|peça|fábula|fabula|book|ensaio/.test(s))return'book';return null};
/* ---------------- Poggie: balão + reações ---------------- */
let hideT=0,lastMsg='',idleT=0,nudges=0;
const POOL={
 story:['Olha só essa cena!','Já imaginou estar aí?','Vamos entrar na história!'],
 dialog:['Escuta com atenção!','Repara como eles falam.','Toque nas falas para ouvir!'],
 vocab:['Palavra nova chegando!','Essa vai grudar, confia!','Repete em voz alta!'],
 reading:['Lê sem pressa.','Toque nas frases para ouvir.','Sublinhei o que importa!'],
 grammar:['Só repare no padrão!','Não decore: perceba.'],
 speak:['Fala em voz alta, vale muito!','Pode errar, eu estou aqui.'],
 practice:['Sua vez! Você consegue.','Pensa um pouquinho e escolhe.','Sem pressa, tá?','Eu acredito em você!'],
 reward:['Que orgulho!','Mais um episódio no bolso!']
};
const TURN=['Já vem mais!','Continua, tem mais!','Boa! Segue comigo.'];
const IDLE=['Travou? Toque em mim!','Quer uma ajudinha? Sou eu!','Respira e tenta de novo.'];
function quiet(txt,mood){
  const b=q('#pbub'),pg=q('#pdock .pog');if(!b||!pg||!txt)return;txt=T(txt);if(txt===lastMsg)return;lastMsg=txt;
  b.textContent=txt;pg.classList.remove('happy','happy2','happy3','sad','talk');void pg.offsetWidth;if(mood)pg.classList.add(mood);pg.classList.add('talk');setTimeout(()=>{try{pg.classList.remove('talk')}catch(e){}},1300)}
function bindDock(){
  const b=q('#pbub'),d=q('#pdock');if(!b||b._l)return;b._l=1;
  new MutationObserver(()=>{const on=!!b.textContent.trim();b.classList.toggle('p2on',on);clearTimeout(hideT);if(on)hideT=setTimeout(()=>{b.classList.remove('p2on');lastMsg=''},5600)}).observe(b,{childList:true,characterData:true,subtree:true});
  if(d){d.setAttribute('role','button');d.setAttribute('aria-label','Poggie');d.onclick=()=>{try{EX.coin()}catch(e){}quiet(rnd(POOL.practice.concat(['Bora! Um passo de cada vez.','Você está indo muito bem!'])),'happy2')}}
}
new MutationObserver(()=>{if(q('#pbub'))bindDock()}).observe(document.body,{childList:true});
/* ao entrar em cada quadro: som temático + (às vezes) fala do Poggie */
const _render=window.render;
if(typeof _render==='function')window.render=function(){
  const r=_render.apply(this,arguments);
  try{
    clearTimeout(idleT);bindDock();
    if(typeof P==='undefined'||!P||P.isTest)return r;
    const s=P.steps[P.i];if(!s)return r;
    const f=/^fx\d+$/.test(s)?P.e.fr[+s.slice(2)]:null;
    const kind=typeof stepKind==='function'?stepKind(s):'story';
    if(f){
      if(f.k==='cover')setTimeout(()=>EX.reveal(),250);
      else if(/^(cultob|cultx|cultcena|cult1)$/.test(f.k)){const w=kindOfWork(f);if(w)setTimeout(()=>EX[w](),300)}
      else if(f.k==='culttl')setTimeout(()=>EX.reveal(),250);
    }
    if(s==='done'){
      setTimeout(()=>EX.win(),300);
      /* fechamento único: se o episódio já teve a tela de fim (wrap) com as frases para levar, a tela de resultado não repete a mochila */
      if(P.e.fr.some(x=>x.k==='wrap'||x.k==='cult1'&&false)){
        setTimeout(()=>{try{
          const st=q('#pstage .step.done');if(!st||st._dd)return;st._dd=1;
          st.querySelectorAll('.recap').forEach(r=>{if(/Você levou|Vocé llevaste|Te llevas/i.test(r.textContent))r.remove()});
          const big=st.querySelector('.big');if(big&&/conclu/i.test(big.textContent))big.textContent='Seu resultado';
          if(typeof window.POG_PAGER_DEBUG!=='undefined')window.dispatchEvent(new Event('resize'));
        }catch(e){}},120)}
    }
    /* fala do Poggie: nos primeiros quadros sempre, depois em ~45% */
    nudges++;const go=P.i<=1||Math.random()<.45;
    if(go&&s!=='done'){const pool=POOL[kind]||POOL.practice;setTimeout(()=>{if(typeof P!=='undefined'&&P&&P.steps[P.i]===s)quiet(rnd(pool),kind==='practice'?'happy':undefined)},900)}
    /* parado numa prática: oferece ajuda */
    if(kind==='practice'||kind==='speak')idleT=setTimeout(()=>{const c=q('#pcta');if(c&&c.disabled&&typeof P!=='undefined'&&P&&P.steps[P.i]===s)quiet(rnd(IDLE),'sad')},16000);
  }catch(e){}
  return r};
/* virar de parte dentro do quadro (paginador) */
window.POG_LIFE={turn(){try{EX.page();quiet(rnd(TURN),'happy')}catch(e){}},quiet,sfx:n=>EX[n]&&EX[n]()};
})();
