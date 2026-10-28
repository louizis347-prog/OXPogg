/* Home do app (novo visual): paisagem ilustrada com o Poggie, cartão "continuar" com a capa do episódio e abertura animada.
   Lê os dados do herói antigo (mesmos botões data-ep / data-course / data-go), então a navegação continua a mesma. */
(function(){
'use strict';
const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const q=(s,r)=>(r||document).querySelector(s);
function epOf(ref){try{const [cid,i]=ref.split(':');return {cid,idx:+i,e:(EP[cid]||[])[+i]}}catch(e){return null}}
function progress(cid){try{const n=(EP[cid]||[]).length;const d=typeof doneCountFor==='function'?doneCountFor(cid):0;return n?{d,n,p:Math.round(d/n*100)}:null}catch(e){return null}}

const QI=HomeArt.QI,QT=HomeArt.QT;
function quick(){
  const row=q('.px-quick');if(!row||row.dataset.hn)return;row.dataset.hn='1';
  row.querySelectorAll('button').forEach(b=>{
    const k=b.dataset.listen!=null?'listen':(b.dataset.go||'');const ic=QI[k]||(k==='comm'?QI.comm:null);if(!ic)return;
    const i=b.querySelector('i');if(!i)return;const em=i.querySelector('em');
    i.innerHTML=`<svg viewBox="0 0 48 48" width="40" height="40" aria-hidden="true">${ic}</svg>`+(em?em.outerHTML:'');
    const t=QT[k]||QT.profile;i.style.setProperty('--t1',t[0]);i.style.setProperty('--t2',t[1]);b.classList.add('qk-'+k);
  });
}
function enhance(){
  const hero=q('.px-hero');if(!hero||hero.dataset.hn||!window.HomeArt)return;hero.dataset.hn='1';
  const txt=s=>{const n=q(s,hero);return n?n.textContent.trim():''};
  const cta=q('.px-cta',hero),ghost=q('.px-ghost',hero),cover=q('.px-cover',hero);
  const ref=cta&&cta.dataset.ep,course=cta&&cta.dataset.course,eyebrow=txt('.px-eyebrow');
  const title=txt('h1'),sub=txt('.px-hl p');
  const pills=[...hero.querySelectorAll('.px-pill')].map(x=>({ic:(x.querySelector('i')||{}).textContent||'',v:(x.querySelector('b')||{}).textContent||'',l:(x.querySelector('small')||{}).textContent||''}));
  const goal=q('.px-goal span',hero);
  let art='';
  const ep=ref?epOf(ref):null;
  if(ep&&ep.e&&window.PogObra&&PogObra.has(ep.e))art=PogObra.svg(ep.e,'obra-cover');
  else if(cover){const s=cover.querySelector('svg');art=s?s.outerHTML:cover.innerHTML}
  const pr=ep?progress(ep.cid):null;
  const hi=ref?{h:'Que bom te ver de volta',s:'Seu próximo passo está pronto. Vamos continuar a história?'}:{h:'Aprenda idiomas <em>pela cultura</em>',s:sub};
  const html=`<section class="hn-hero hn-in${ref?' rs':''}" aria-label="Boas-vindas">
    <div class="hn-bg">${HomeArt.scene()}</div>
    <div class="hn-copy">
      <span class="hn-chip">${esc(eyebrow||'Episódios de 10 minutos')}</span>
      <h1 class="hn-h1">${ref?esc(hi.h):hi.h}</h1>
      <p class="hn-sub">${esc(hi.s)}</p>
      ${ref?'':`<div class="hn-acts"><button class="hn-btn sun" ${course?`data-course="${esc(course)}"`:'data-go="courses"'}>${esc(cta?cta.textContent.trim():'Começar')} <i>→</i></button>${ghost?`<button class="hn-btn glass" data-go="courses">${esc(ghost.textContent.trim())}</button>`:''}</div>`}
    </div>
    <div class="hn-mascot" aria-hidden="true">${HomeArt.mascot({scarf:'#FF7A45'})}</div>
  </section>
  ${ref?`<section class="hn-continue hn-in" aria-label="Continuar">
    <button class="hn-cover" data-ep="${esc(ref)}" aria-label="Continuar episódio">${art}<span class="hn-play">▶</span></button>
    <div class="hn-ct"><small>Continue de onde parou</small><b>${esc(title)}</b><span>${esc(sub)}</span>
      ${pr?`<div class="hn-prog" aria-label="Progresso no curso"><i style="width:${Math.max(3,pr.p)}%"></i></div><em>${pr.d} de ${pr.n} episódios · ${pr.p}%</em>`:''}
      <button class="hn-btn sun" data-ep="${esc(ref)}">${esc(cta?cta.textContent.trim():'Continuar')} <i>→</i></button></div>
  </section>`:''}
  <section class="hn-stats hn-in" aria-label="Seu progresso">${pills.map(p=>`<span><i>${p.ic==='🪙'&&window.PogCoins?PogCoins.icon(20):esc(p.ic)}</i><b>${esc(p.v)}</b><small>${esc(p.l)}</small></span>`).join('')}${goal?`<span class="g"><i>🎯</i><b>${esc(goal.textContent)}</b><small>meta de hoje</small></span>`:''}</section>`;
  hero.outerHTML=html;
  quick();
}
const _h=window.home;
if(typeof _h==='function')window.home=function(){const r=_h.apply(this,arguments);try{enhance()}catch(e){console.warn('home-new',e)}return r};
/* a primeira renderização pode ter acontecido antes deste script: observa o herói antigo e troca quando aparecer */
try{enhance();quick();new MutationObserver(()=>{if(q('.px-hero:not([data-hn])'))enhance();if(q('.px-quick:not([data-hn])'))quick()}).observe(document.body,{childList:true,subtree:true})}catch(e){}
/* abertura animada na primeira entrada da sessão */
if(window.HomeArt)HomeArt.splash();
window.PogHomeNew={enhance};
})();
