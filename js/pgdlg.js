/* Pogglot · "Diálogo relâmpago" (pgdlg): diálogo curto em que o aluno troca as peças coloridas.
   Texto: {a|b|c} = peça trocável (a é a inicial); o português usa a mesma ordem de peças. */
(function(){
'use strict';
if(typeof FXR==='undefined'||typeof FX_KIND==='undefined'||!window.PogStage)return;
const H=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const q=(s,r)=>(r||document).querySelector(s);
const qa=(s,r)=>[...(r||document).querySelectorAll(s)];
FX_KIND.pgdlg='practice';FX_LABEL.pgdlg='Diálogo relâmpago';
const CC=['c0','c1','c2','c3'];
const parse=s=>{const parts=[];let last=0;String(s).replace(/\{([^}]*)\}/g,(m,g,i)=>{if(i>last)parts.push({t:s.slice(last,i)});parts.push({o:g.split('|')});last=i+m.length;return m});if(last<s.length)parts.push({t:s.slice(last)});return parts};
FXR.pgdlg=function(f,st,n){
  const L=(f.lines||[]).map(l=>({who:l[0],en:parse(l[1]),pt:parse(l[2]||''),i:0}));
  const state=L.map(()=>({}));            /* por fala: índice de cada peça */
  let slotN=0;L.forEach((l,li)=>{l.en.forEach((p,pi)=>{if(p.o){p.id=slotN++;p.c=CC[p.id%4];state[li][pi]=0}})});
  /* o PT segue a mesma ordem de peças do EN */
  const enSlots=L.map(l=>l.en.map((p,i)=>p.o?i:-1).filter(i=>i>=0));
  const ptTxt=li=>{let j=0;return L[li].pt.map(p=>p.o?p.o[state[li][enSlots[li][j++]]||0]:p.t).join('')};
  const enTxt=li=>L[li].en.map((p,i)=>p.o?p.o[state[li][i]||0]:p.t).join('');
  const names=[...new Set(L.map(l=>l.who))];
  const html=li=>{const l=L[li],side=names.indexOf(l.who)%2?'r':'';
    return `<div class="dl-l ${side}" data-i="${li}"><span class="dl-who">${H(l.who)}</span><div class="dl-b"><p class="dl-en">${l.en.map((p,i)=>p.o?`<button type="button" class="dl-p ${p.c}" data-p="${i}">${H(p.o[0])}<i>⟳</i></button>`:H(p.t)).join('')}</p><small class="dl-pt">${H(ptTxt(li))}</small></div><button type="button" class="dl-s" aria-label="Ouvir">🔊</button></div>`};
  st.innerHTML=`<div class="step fx ps-dl">${fxKindBar(f,n)}<div class="ps-sh-h"><h2 class="fx-h">${H(f.title||'Diálogo relâmpago')}</h2><span class="ps-count" id="dlc">toque nas peças</span></div>
   <p class="ps-note">As peças coloridas mudam. Toque nelas para criar outra conversa — e ouça o resultado.</p>
   <div class="dl-tools"><button type="button" class="ps-btn main" id="dlp">▶ Ouvir o diálogo</button><button type="button" class="ps-btn" id="dlr">🎲 Sortear tudo</button><button type="button" class="ps-btn tog" id="dlt" aria-pressed="true">🇧🇷 Tradução</button></div>
   <div class="dl-list">${L.map((_,i)=>html(i)).join('')}</div></div>`;
  let moves=0;
  const refresh=li=>{const el=q(`.dl-l[data-i="${li}"]`,st);
    qa('.dl-p',el).forEach(b=>{const p=L[li].en[+b.dataset.p];b.firstChild.nodeValue=p.o[state[li][+b.dataset.p]||0]});
    q('.dl-pt',el).textContent=ptTxt(li)};
  const say1=(li,cb)=>{window.__speakEnd=cb||null;fxSay(enTxt(li),null,false)};
  qa('.dl-l',st).forEach(el=>{const li=+el.dataset.i;
    qa('.dl-p',el).forEach(b=>b.onclick=()=>{const pi=+b.dataset.p,p=L[li].en[pi];state[li][pi]=((state[li][pi]||0)+1)%p.o.length;
      b.classList.remove('dlf');void b.offsetWidth;b.classList.add('dlf');refresh(li);moves++;q('#dlc',st).textContent=moves+' trocas';say1(li)});
    q('.dl-s',el).onclick=()=>say1(li)});
  q('#dlr',st).onclick=()=>{L.forEach((l,li)=>l.en.forEach((p,pi)=>{if(p.o)state[li][pi]=Math.floor(Math.random()*p.o.length)}));L.forEach((_,li)=>refresh(li));moves++;q('#dlc',st).textContent=moves+' trocas'};
  q('#dlt',st).onclick=e=>{const on=e.currentTarget.getAttribute('aria-pressed')!=='true';e.currentTarget.setAttribute('aria-pressed',on);st.classList.toggle('dl-nopt',!on)};
  q('#dlp',st).onclick=()=>{let li=0;const next=()=>{if(li>=L.length){window.__speakEnd=null;return}
      qa('.dl-l',st).forEach((e,k)=>e.classList.toggle('now',k===li));const cur=li++;say1(cur,next)};next()};
  P.fx.cta=null;cta('Continuar',true,true);
  say(f.say||'Troque as peças e ouça a conversa mudar!');
};
})();
