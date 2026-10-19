/* Episódio enxuto: "Mais treino", recompensas, métrica de abandono por tela */
(function(){
if(typeof render!=='function'||typeof play!=='function'||typeof closePlayer!=='function')return;
const $$=(s,r)=>(r||document).querySelector(s);
const MK='pg_drop';
const ld=()=>{try{return JSON.parse(localStorage.getItem(MK)||'{}')}catch(e){return{}}};
const sv=o=>{try{localStorage.setItem(MK,JSON.stringify(o))}catch(e){}};
/* --- métrica: última tela vista; se fechar antes do fim, conta abandono --- */
function track(){
  if(!P||!P.e||!P.e.fr||P.isTest)return;
  const s=P.steps[P.i];if(s==='done')return;
  const f=P.e.fr[P.i];P.lastK=(f&&f.k)||s;P.lastI=P.i;
}
function logExit(){
  if(!P||!P.e||!P.e.fr||P.isTest)return;
  const done=P.steps[P.i]==='done',m=ld(),k=P.cid+(P.e.ex?':x':'');
  const r=m[k]||(m[k]={n:0,fin:0,at:{}});r.n++;
  if(done)r.fin++;else{const a=(P.lastK||'?')+'@'+(P.lastI||0);r.at[a]=(r.at[a]||0)+1}
  sv(m);
  try{if(window.PogCloud&&PogCloud.logEpisode)PogCloud.logEpisode(done?'finish':'drop',P.cid,P.e.n,P.lastI||0)}catch(e){}
}
window.pogDropStats=()=>ld();
const _c=window.closePlayer;
window.closePlayer=function(){logExit();const x=P&&P.extraPop;const r=_c.apply(this,arguments);if(x)x();return r};
/* --- Mais treino --- */
const companion=(cid,n)=>((typeof EPX!=='undefined'&&EPX[cid])||[]).find(x=>x.xof===n);
function playExtra(cid,x){
  const arr=EP[cid];arr.push(x);const idx=arr.length-1;
  const pop=()=>{const i=arr.indexOf(x);if(i>=0)arr.splice(i,1)};
  try{play(cid,idx)}catch(e){pop();throw e}
  if(P)P.extraPop=pop;else pop();
}
window.playExtra=playExtra;
function addDone(){
  if(!P||!P.e||P.isTest||P.steps[P.i]!=='done'||P.e.ex)return;
  const st=$$('#pstage .step');if(!st||st.querySelector('.lean-more'))return;
  const x=companion(P.cid,P.e.n);if(!x)return;
  const b=document.createElement('button');b.type='button';b.className='lean-more';
  b.innerHTML='<span class="lm-ic">🎯</span><span><b>Mais treino</b><small>Sons, expressões e uma 2ª cena · ~4 min</small></span>';
  b.onclick=()=>{const cid=P.cid;closePlayer();setTimeout(()=>playExtra(cid,x),60)};
  st.appendChild(b);
}
/* --- recompensas: sequência de acertos, estrelas, mascote --- */
function pop(txt){
  const p=$$('#player');if(!p)return;
  const d=document.createElement('div');d.className='lean-pop';d.textContent=txt;p.appendChild(d);setTimeout(()=>d.remove(),1300);
}
function stars(){
  const p=$$('#player');if(!p)return;
  for(let i=0;i<7;i++){const s=document.createElement('i');s.className='lean-star';s.textContent='★';
    s.style.setProperty('--dx',(Math.random()*160-80)+'px');s.style.setProperty('--dy',(-60-Math.random()*90)+'px');
    s.style.animationDelay=(i*40)+'ms';p.appendChild(s);setTimeout(()=>s.remove(),1400)}
}
function chip(){
  const h=$$('#player .p-head');if(!h)return;let c=$$('#lean-streak');
  const n=(P&&P.streak)||0;
  if(n<2){if(c)c.remove();return}
  if(!c){c=document.createElement('span');c.id='lean-streak';c.className='lean-streak';h.appendChild(c)}
  c.textContent='🔥 '+n;c.classList.remove('bump');void c.offsetWidth;c.classList.add('bump');
}
const _g=window.fxGrade;
if(_g)window.fxGrade=function(ok){
  const r=_g.apply(this,arguments);
  try{
    const n=P.streak||0;chip();
    const dock=$$('#pdock');if(dock){dock.classList.remove('lean-jump','lean-oops');void dock.offsetWidth;dock.classList.add(ok?'lean-jump':'lean-oops')}
    if(ok){stars();if(n===3)pop('Sequência de 3! 🔥');else if(n===5)pop('Imparável! ⚡');else if(n>=8&&n%4===0)pop(n+' seguidas! 🏆')}
  }catch(e){}
  return r;
};
/* --- render --- */
const _r=window.render;
window.render=function(){
  const out=_r.apply(this,arguments);
  try{
    track();addDone();
    if(P&&P.e&&P.e.fr&&!P.isTest){
      const stp=$$('#pstage .step');
      if(stp){
        const f=P.e.fr[P.i];stp.dataset.fk=(f&&f.k)||'';
        stp.classList.add('lean');
        const w=(stp.innerText||'').trim().split(/\s+/).length;
        if(w>46)stp.classList.add('lean-dense');
      }
      chip();
    }
  }catch(e){}
  return out;
};
/* --- "Mais treino" nos itens do mapa --- */
function decorate(){
  document.querySelectorAll('button.node[data-ep]').forEach(b=>{
    if(b.querySelector('.lean-more-tag'))return;
    const [cid,i]=b.dataset.ep.split(':');const e=(EP[cid]||[])[+i];
    if(!e||!e.xn||!companion(cid,e.n))return;
    const t=document.createElement('span');t.className='lean-more-tag';t.textContent='＋ treino';t.setAttribute('role','button');
    t.onclick=ev=>{ev.stopPropagation();ev.preventDefault();playExtra(cid,companion(cid,e.n))};
    (b.querySelector('.info small')||b).appendChild(t);
  });
}
new MutationObserver(()=>{clearTimeout(decorate.t);decorate.t=setTimeout(decorate,80)}).observe(document.body,{childList:true,subtree:true});
})();
