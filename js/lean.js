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
  const done=P.steps[P.i]==='done',m=ld(),k=P.cid+('');
  const r=m[k]||(m[k]={n:0,fin:0,at:{}});r.n++;
  if(done)r.fin++;else{const a=(P.lastK||'?')+'@'+(P.lastI||0);r.at[a]=(r.at[a]||0)+1}
  sv(m);
  try{if(window.PogCloud&&PogCloud.logEpisode)PogCloud.logEpisode(done?'finish':'drop',P.cid,P.e.n,P.lastI||0)}catch(e){}
}
window.pogDropStats=()=>ld();
const _c=window.closePlayer;
window.closePlayer=function(){logExit();return _c.apply(this,arguments)};
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
    track();
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
})();
