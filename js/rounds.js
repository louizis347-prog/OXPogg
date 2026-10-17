/* Episódio em 3 rodadas (Entender · Treinar · Usar) — por enquanto só no A1 */
(function(){
if(typeof render!=='function'||typeof play!=='function')return;
const NAMES=[['Entender','🧭','história, palavras e verbos'],['Treinar','🎯','padrões, jogos e sons'],['Usar','🗣️','cenas, diálogo e produção']];
const act=()=>P&&!P.isTest&&(P.cid==='en-a1'||P.cid==='en-a2'||P.cid==='en-b1'||P.cid==='en-b2'||P.cid==='en-c1'||P.cid==='en-c2'||P.cid==='es-a1')&&P.e&&P.e.fr&&P.e.fr.length>12&&P.e.fr.some(f=>f.k==='pat')&&P.e.fr.some(f=>f.k==='cexp');
const starts=e=>{const k=e.fr.map(f=>f.k);return [0,k.indexOf('pat'),k.indexOf('cexp')]};
const roundOf=i=>{const s=starts(P.e);return i>=s[2]?2:i>=s[1]?1:0};
const sizes=()=>{const s=starts(P.e),n=P.e.fr.length;return [s[1]-s[0],s[2]-s[1],n-s[2]]};
const mins=n=>Math.max(3,Math.round(n*1.1));
const key=()=>'pg_rd_'+P.e.n;
const sv=(v)=>{try{v==null?localStorage.removeItem(key()):localStorage.setItem(key(),String(v))}catch(e){}};
const ld=()=>{try{return +localStorage.getItem(key())||0}catch(e){return 0}};
function strip(){
  const el=document.getElementById('rdstrip');if(!el)return;
  const done=P.steps[P.i]==='done',r=done?3:roundOf(P.i);
  el.innerHTML=NAMES.map((n,i)=>`<span class="rd-chip ${i<r?'ok':i===r?'on':''}"><b>${i<r?'✓':i+1}</b>${n[0]}</span>`).join('');
}
function gate(i){
  const r=roundOf(i),prev=r-1,st=document.getElementById('pstage'),sz=sizes();
  P.answered=false;try{setProg()}catch(e){}
  st.innerHTML=`<div class="step rd-gate"><div class="rd-big">✅</div><h2>Rodada ${prev+1} concluída!</h2><p class="rd-sub">Você terminou <b>${NAMES[prev][0]}</b>. Seu progresso está guardado.</p>
  <div class="rd-next"><span class="rd-ic">${NAMES[r][1]}</span><div><small>PRÓXIMA · RODADA ${r+1} DE 3</small><b>${NAMES[r][0]}</b><span>${NAMES[r][2]} · cerca de ${mins(sz[r])} min</span></div></div>
  <button type="button" class="rd-later" id="rdlater">Continuar depois</button></div>`;
  const b=document.getElementById('pcta');b.textContent=`Começar a rodada ${r+1}`;b.disabled=false;b.classList.add('amber');
  b.onclick=()=>{P.rd.seen[i]=true;b.onclick=ctaClick;sv(null);render()};
  document.getElementById('rdlater').onclick=()=>{sv(i);P.rd.seen[i]=true;closePlayer()};
  try{say('Rodada '+(prev+1)+' completa! Quer seguir ou continuar depois?')}catch(e){}
  try{chime('step')}catch(e){}
  strip();
}
const _r=window.render;
window.render=function(){
  if(act()&&P.rd){
    const i=P.i,s=starts(P.e);
    if(P.steps[i]!=='done'&&i>0&&(i===s[1]||i===s[2])&&!P.rd.seen[i]){return gate(i)}
    if(P.steps[i]==='done')sv(null);
  }
  const out=_r.apply(this,arguments);
  if(act()&&P.rd){strip();
    if(P.i===0){const stp=document.querySelector('#pstage .step');if(stp&&!stp.querySelector('.rd-plan')){const sz=sizes();
      const d=document.createElement('div');d.className='rd-plan';
      d.innerHTML=`<b>Este episódio tem 3 rodadas curtas</b>`+NAMES.map((n,k)=>`<div class="rd-row"><span class="rd-n">${k+1}</span><span><b>${n[0]}</b> · ${n[2]}</span><em>~${mins(sz[k])} min</em></div>`).join('')+`<small>Pare quando quiser: o progresso fica guardado.</small>`;
      stp.appendChild(d)}}}
  return out;
};
const _p=window.play;
window.play=function(cid,idx){
  const out=_p.apply(this,arguments);
  if(act()){
    P.rd={seen:{}};
    const h=document.querySelector('#player .p-head');
    if(h&&!document.getElementById('rdstrip')){const d=document.createElement('div');d.id='rdstrip';d.className='rd-strip';h.after(d)}
    const s=ld();
    if(s>0&&s<P.steps.length-1){const st=starts(P.e);for(const x of st)if(x<=s)P.rd.seen[x]=true;P.i=s;render()}
    else strip();
  }
  return out;
};
})();
