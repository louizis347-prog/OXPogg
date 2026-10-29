/* Pogglot · telas compostas: junta quadros vizinhos em uma só tela (abas ou lado a lado), em tempo de execução.
   Os dados dos episódios não mudam. POG_COMBO=false desliga; POG_COMBO_MAX = quantos episódios por curso (padrão: todos). */
(function(){
'use strict';
if(typeof FXR==='undefined'||typeof FX_KIND==='undefined')return;
const H=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
FX_KIND.combo='practice';FX_LABEL.combo='Prática';

/* ---- agrupamento ---- */
function group(e){
  const fr=e.fr,out=[];let i=0,scenes=0;
  const K=j=>fr[j]&&fr[j].k;
  const mk=(tabs,parts,layout)=>({k:'combo',tabs,parts,layout:layout||'tabs',rs:parts[0].rs,chars:parts[0].chars});
  while(i<fr.length){
    const k=K(i);
    if(k==='review'&&K(i+1)==='hotscene'){out.push(mk(['🎒 Mochila','🔎 Cenário'],[fr[i],fr[i+1]]));i+=2;continue}
    if(k==='pgscene'&&scenes===0&&K(i+1)==='pgsheet'){scenes++;out.push(mk(['💬 A cena','❓ Perguntas'],[fr[i],fr[i+1]],'split'));i+=2;continue}
    if(k==='pgrule'&&K(i+1)==='pgmold'){out.push(mk(['🧩 O padrão','🎲 Monte frases'],[fr[i],fr[i+1]],'split'));i+=2;continue}
    if(k==='verbs'&&K(i+1)==='vplay'){out.push(mk(['🏃 Verbos','🎮 Jogo dos verbos'],[fr[i],fr[i+1]],'split'));i+=2;continue}
    if(k==='pgscene'&&scenes>=1&&K(i+1)==='pgsheet'){
      scenes++;const parts=[fr[i]],tabs=['💬 A cena'];let j=i+1;
      while(K(j)==='pgsheet'){const lac=(fr[j].items||[]).some(t=>t.text&&/___/.test(t.text));tabs.push(lac?'✏️ Complete':'🎧 Escute');parts.push(fr[j]);j++}
      out.push(mk(tabs,parts));i=j;continue}
    if(k==='pglab'&&K(i+1)==='pgspeak'){out.push(mk(['🔊 Sons','🎤 Fale'],[fr[i],fr[i+1]],'split'));i+=2;continue}
    if(k==='pgscene')scenes++;
    out.push(fr[i]);i++;
  }
  return out;
}
const on=(cid,idx,e)=>window.POG_COMBO!==false&&/^en-/.test(cid)&&e&&e.fr&&e.presentation==='regular-pilot-v1'&&idx<(window.POG_COMBO_MAX==null?10:window.POG_COMBO_MAX);

/* play() joga o episódio já agrupado; o dado original fica intacto (revisão, auditoria etc.) */
const _play=window.play;
window.play=function(cid,idx){
  let e=null;try{e=EP[cid]&&EP[cid][idx]}catch(x){}
  if(!on(cid,idx,e))return _play.apply(this,arguments);
  const g=Object.assign({},e,{fr:group(e),__orig:e});
  EP[cid][idx]=g;
  try{return _play.apply(this,arguments)}finally{EP[cid][idx]=e}
};

/* ---- renderizador ---- */
FXR.combo=function(f,st,n){
  const parts=f.parts,split=f.layout==='split',state=[];let cur=0;
  st.innerHTML=`<div class="step fx cb ${split?'split':''}"><div class="cb-tabs" role="tablist">${f.tabs.map((t,i)=>`<button type="button" role="tab" class="cb-t" data-i="${i}">${H(t)}</button>`).join('')}</div><div class="cb-body">${parts.map((_,i)=>`<div class="cb-pane" data-i="${i}" hidden></div>`).join('')}</div></div>`;
  const root=st.querySelector('.cb'),panes=[...st.querySelectorAll('.cb-pane')],tabs=[...st.querySelectorAll('.cb-t')];
  const renderPart=i=>{
    const p=parts[i],fn=FXR[p.k];if(!fn)return;
    const rec={label:null,en:true,amber:false,inner:null};
    const realCta=window.cta;window.cta=function(l,en,am){rec.label=l;rec.en=en;rec.amber=am;return realCta.apply(this,arguments)};
    P.fx={n,cta:null};
    try{fn(p,panes[i],n)}catch(x){panes[i].innerHTML='<p>Quadro indisponível.</p>';try{console.warn('combo',x)}catch(_){}}
    finally{window.cta=realCta}
    if(p.k==='pgscene'&&!split){const stp=panes[i].querySelector('.step');if(stp)stp.classList.add('ps-2col')}
    rec.inner=P.fx&&P.fx.cta;state[i]=rec;
  };
  const apply=i=>{
    const rec=state[i];if(!rec)return;
    const next=()=>{for(let j=i+1;j<parts.length;j++)return j;return null};
    P.fx={n,cta:()=>{if(rec.inner&&rec.inner())return true;const nx=next();if(nx!=null){show(nx);return true}return false}};
    if(rec.label!=null)cta(rec.label,rec.en,rec.amber);
    try{PogStage.footLine(parts[i].bubble)}catch(_){}
  };
  function show(i){
    cur=i;tabs.forEach((b,k)=>b.classList.toggle('on',k===i));
    panes.forEach((p,k)=>{p.hidden=split&&window.innerWidth>=1000?false:k!==i});
    if(!state[i])renderPart(i);
    apply(i);
    const bd=document.getElementById('pbody');if(bd)bd.scrollTop=0;
  }
  if(split&&window.innerWidth>=1000){parts.forEach((_,i)=>renderPart(i));show(parts.length-1);tabs.forEach(b=>b.hidden=true)}
  else show(0);
  tabs.forEach(b=>b.onclick=()=>show(+b.dataset.i));
};

const _ft=window.fxTotal;
window.fxTotal=function(e){
  if(e&&e.fr&&e.fr.some(f=>f.k==='combo'))return _ft(Object.assign({},e,{fr:e.fr.flatMap(f=>f.k==='combo'?f.parts:[f])}));
  return _ft(e)};
const _render=window.render;
if(typeof _render==='function')window.render=function(){try{if(window.PogStage&&PogStage.footLine)PogStage.footLine(null)}catch(_){}return _render.apply(this,arguments)};
})();
