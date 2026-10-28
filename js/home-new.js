/* Home do app (novo visual): paisagem ilustrada com o Poggie, cartão "continuar" com a capa do episódio e abertura animada.
   Lê os dados do herói antigo (mesmos botões data-ep / data-course / data-go), então a navegação continua a mesma. */
(function(){
'use strict';
const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const q=(s,r)=>(r||document).querySelector(s);
function epOf(ref){try{const [cid,i]=ref.split(':');return {cid,idx:+i,e:(EP[cid]||[])[+i]}}catch(e){return null}}
function progress(cid){try{const n=(EP[cid]||[]).length;const d=typeof doneCountFor==='function'?doneCountFor(cid):0;return n?{d,n,p:Math.round(d/n*100)}:null}catch(e){return null}}

const INK='#0E2F3A';
const S=(w)=>`stroke="${INK}" stroke-width="${w||2.4}" stroke-linejoin="round" stroke-linecap="round"`;
const QI={
 listen:`<path d="M9,30 Q9,10 24,10 Q39,10 39,30" fill="none" ${S(3)}/><rect x="6" y="28" width="9" height="13" rx="4" fill="#FF7A45" ${S()}/><rect x="33" y="28" width="9" height="13" rx="4" fill="#FF7A45" ${S()}/><path d="M20,24 Q24,20 28,24 M18,28 Q24,22 30,28" fill="none" stroke="#0B7C88" stroke-width="2.4" stroke-linecap="round" class="qi-w"/>`,
 review:`<path d="M12,22 A12,12 0 0 1 34,15" fill="none" stroke="#0B7C88" stroke-width="4.4" stroke-linecap="round"/><path d="M36,26 A12,12 0 0 1 14,33" fill="none" stroke="#FFB627" stroke-width="4.4" stroke-linecap="round"/><path d="M34,8 L36,17 L27,16Z" fill="#0B7C88" ${S(1.6)}/><path d="M14,40 L12,31 L21,32Z" fill="#FFB627" ${S(1.6)}/><rect x="19" y="19" width="10" height="10" rx="2.4" fill="#fff" ${S(2)} class="qi-c"/>`,
 shelf:`<rect x="7" y="14" width="9" height="26" rx="2" fill="#0B7C88" ${S()}/><rect x="17" y="10" width="9" height="30" rx="2" fill="#FFB627" ${S()}/><path d="M28,18 L36,15 L42,38 L34,41Z" fill="#FF7A45" ${S()}/><path d="M10,20 L13,20 M20,16 L23,16" stroke="#fff" stroke-width="2" stroke-linecap="round"/>`,
 comm:`<path d="M6,10 H30 Q34,10 34,14 V24 Q34,28 30,28 H17 L10,34 V28 H10 Q6,28 6,24Z" fill="#fff" ${S()}/><path d="M20,20 H38 Q42,20 42,24 V33 Q42,37 38,37 H38 V42 L32,37 H26 Q22,37 22,33Z" fill="#FFB627" ${S()}/><circle cx="13" cy="19" r="1.8" fill="${INK}"/><circle cx="20" cy="19" r="1.8" fill="${INK}"/><circle cx="27" cy="19" r="1.8" fill="${INK}"/>`,
 rank:`<path d="M14,8 H34 V20 Q34,31 24,31 Q14,31 14,20Z" fill="#FFB627" ${S()}/><path d="M14,12 H8 Q8,22 15,24 M34,12 H40 Q40,22 33,24" fill="none" ${S()}/><rect x="21" y="31" width="6" height="6" fill="#E58E10" ${S(2)}/><rect x="15" y="37" width="18" height="5" rx="2" fill="#0B7C88" ${S(2)}/><path d="M24,13 L26,18 L31,18 L27,21 L29,26 L24,23 L19,26 L21,21 L17,18 L22,18Z" fill="#fff6c8" stroke="none"/>`,
 ach:`<path d="M15,6 L22,22 L26,22 L33,6Z" fill="#FF7A45" ${S()}/><circle cx="24" cy="30" r="12" fill="#FFB627" ${S()}/><circle cx="24" cy="30" r="7.6" fill="none" stroke="#fff3b8" stroke-width="2"/><path d="M24,24 L26,28.4 L30.8,28.8 L27.2,32 L28.3,36.6 L24,34.2 L19.7,36.6 L20.8,32 L17.2,28.8 L22,28.4Z" fill="#fff" stroke="${INK}" stroke-width="1.6" stroke-linejoin="round"/>`,
 profile:`<circle cx="24" cy="17" r="9" fill="#FFD9B5" ${S()}/><path d="M6,42 Q8,28 24,28 Q40,28 42,42Z" fill="#0B7C88" ${S()}/><path d="M16,15 Q18,7 24,8 Q31,7 33,15 Q28,11 24,12 Q19,11 16,15Z" fill="#6B3F22" ${S(1.8)}/><circle cx="20.5" cy="17" r="1.4" fill="${INK}"/><circle cx="27.5" cy="17" r="1.4" fill="${INK}"/><path d="M21,21 Q24,23.4 27,21" fill="none" stroke="${INK}" stroke-width="1.8" stroke-linecap="round"/>`
};
const QT={listen:['#FFE3D6','#FFC9B0'],review:['#DDF3EF','#B7E6DE'],shelf:['#FFF0C9','#FFE08A'],comm:['#FFE6EA','#FFC8D2'],rank:['#FFF2CC','#FFDD83'],ach:['#FFE7D9','#FFC6A6'],profile:['#DFF1F6','#BDE3EE']};
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
