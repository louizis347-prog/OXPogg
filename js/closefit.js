/* Pogglot · fechamento do episódio em UMA tela (sem "Ver mais").
   Cobre: "Seu resultado" (.step.done) e o quadro de fechamento (.m2-wrap Neighbors / wrap com .wr-hero + .fx-recap).
   1) organiza o quadro em duas colunas (PC) ou uma coluna compacta (celular), sem tirar nenhum conteúdo/botão;
   2) acrescenta troféu, estrelas e (se houver) sequência em destaque, calculados de P.score/P.total;
   3) se ainda sobrar altura, reduz proporcionalmente (zoom) até caber, para o paginador nunca dividir o quadro.
   Estilos em css/closefit.css (escopados a .step.clf). */
(function(){
if(window.POG_CLOSEFIT===false)return;
const MIN=.56;
const $=(s,r)=>(r||document).querySelector(s);
function kindOf(st){
  if(typeof P!=='undefined'&&P&&(P.isTest||(P.e&&P.e.pilot)))return '';
  if(st.classList.contains('done'))return 'done';
  if(st.classList.contains('m2-wrap'))return 'm2';
  if(st.querySelector(':scope>.fx-recap,:scope>.clf-cols .fx-recap'))return 'wr';
  return '';
}
const LEFT_DONE=['pgbig','eyebrow','big','row','clf-hero'];
const LEFT_WRAP=['m2-fin','wr-hero','fx-h','eyebrow','fx-next','fx-kind','fx-bar'];
const has=(el,list)=>list.some(c=>el.classList&&el.classList.contains(c));
function stars(){
  const tot=(P&&P.total)||0,sc=Math.max(0,(P&&P.score)||0),r=tot?Math.min(1,sc/tot):0;
  const n=r>=.9?3:r>=.6?2:r>0?1:0;
  const tro=r>=.9?'🏆':r>=.6?'🏅':'🌱';
  return {n,tro,r};
}
function buildDone(st){
  let cols=st.querySelector(':scope>.clf-cols');
  if(!cols){
    const pg=st.querySelector(':scope>.pgbig'),ey=st.querySelector(':scope>.eyebrow'),big=st.querySelector(':scope>.big'),row=st.querySelector(':scope>.row');
    if(!pg||!big)return false;
    const s=stars(),hero=document.createElement('div');hero.className='clf-hero';
    const ht=document.createElement('div');ht.className='clf-ht';
    let strk='';try{const n=ST&&ST.streak&&ST.streak.n;if(n>=2)strk=`<span class="clf-streak" title="Sequência de dias">🔥 ${n}</span>`}catch(e){}
    const stHtml=`<div class="clf-stars" role="img" aria-label="${s.n} de 3 estrelas">${[0,1,2].map(i=>`<i class="${i<s.n?'on':''}" style="--k:${i}">★</i>`).join('')}</div>`;
    pg.classList.add('clf-pg');
    const tro=document.createElement('span');tro.className='clf-tro';tro.textContent=s.tro;tro.setAttribute('aria-hidden','true');pg.appendChild(tro);
    if(ey)ht.appendChild(ey);ht.appendChild(big);ht.insertAdjacentHTML('beforeend',`<div class="clf-sr">${stHtml}${strk}</div>`);
    hero.appendChild(pg);hero.appendChild(ht);
    cols=document.createElement('div');cols.className='clf-cols';
    const l=document.createElement('div'),r=document.createElement('div');l.className='clf-l';r.className='clf-r';
    cols.appendChild(l);cols.appendChild(r);
    st.insertBefore(cols,st.firstChild);
    l.appendChild(hero);if(row){row.classList.add('clf-stats');l.appendChild(row);const f=row.firstElementChild;if(f)f.classList.add('clf-xp')}
  }
  const l=cols.querySelector(':scope>.clf-l'),r=cols.querySelector(':scope>.clf-r');
  [...st.children].forEach(k=>{if(k===cols)return;r.appendChild(k)});
  cols.dataset.n=r.children.length;
  return true;
}
function buildWrap(st){
  let cols=st.querySelector(':scope>.clf-cols');
  if(!cols){
    cols=document.createElement('div');cols.className='clf-cols';
    const l=document.createElement('div'),r=document.createElement('div');l.className='clf-l';r.className='clf-r';
    cols.appendChild(l);cols.appendChild(r);st.insertBefore(cols,st.firstChild);
  }
  const l=cols.querySelector(':scope>.clf-l'),r=cols.querySelector(':scope>.clf-r');
  [...st.children].forEach(k=>{
    if(k===cols)return;
    (has(k,LEFT_WRAP)?l:r).appendChild(k);
  });
  const n=r.querySelectorAll('.fx-rc').length;st.dataset.cfn=n>4?'many':'few';
  return true;
}
function fit(st){
  if(!st||!st.isConnected)return;
  const b=document.getElementById('pbody');if(!b)return;
  st.style.zoom='';st.style.width='';let z=1;
  const setz=(v)=>{st.style.zoom=v===1?'':v.toFixed(3);st.style.width=v===1?'':(100/v).toFixed(3)+'%'};
  const sg=document.getElementById('pstage');
  const used=()=>Math.max(b.scrollHeight>b.clientHeight+1?b.scrollHeight:0,sg?sg.getBoundingClientRect().bottom-b.getBoundingClientRect().top+b.scrollTop:0);
  const ok=(m)=>used()<=b.clientHeight-(m||0)+1&&b.scrollWidth<=b.clientWidth+1;
  if(!ok(0)){
    for(let i=0;i<7;i++){
      const sh=b.scrollHeight,ch=b.clientHeight;
      if(sh<=ch+1)break;
      z=Math.max(MIN,z*Math.min(.985,(ch-1)/sh));
      setz(z);
      if(z<=MIN)break;
    }
  }else{
    /* sobrou altura (telas grandes/altas): amplia um pouco para o quadro ficar bem preenchido, sem rolagem */
    for(const g of [1.1,1.2,1.3,1.4,1.5]){
      setz(g);
      if(ok(14))z=g;else break;
    }
    setz(z);
  }
  st.dataset.cfz=z.toFixed(2);
}
let cur=null,obs=null,tm=[];
function run(st){
  const k=kindOf(st);if(!k)return;
  try{
    if(!st.classList.contains('clf')){st.classList.add('clf','clf-'+k)}
    if(k==='done')buildDone(st);else buildWrap(st);
    fit(st);
  }catch(e){console.warn('closefit',e)}
}
function arm(st){
  tm.forEach(clearTimeout);tm=[];
  if(obs){obs.disconnect();obs=null}
  cur=st;if(!st)return;
  run(st);
  [90,350,900,1800].forEach(ms=>tm.push(setTimeout(()=>{if(cur===st)run(st)},ms)));
  obs=new MutationObserver(()=>{if(cur!==st)return;clearTimeout(arm._t);arm._t=setTimeout(()=>{if(cur===st)run(st)},30)});
  obs.observe(st,{childList:true});
}
function watch(){
  const stg=document.getElementById('pstage');if(!stg||stg._cf)return;stg._cf=1;
  const chk=()=>{const s=stg.querySelector('.step');if(s===cur)return;if(s&&!s.classList.contains('out'))arm(s);else if(!s)arm(null)};
  new MutationObserver(chk).observe(stg,{childList:true});chk();
}
new MutationObserver(()=>{if(document.getElementById('pstage'))watch()}).observe(document.body,{childList:true});
window.addEventListener('resize',()=>{if(cur)setTimeout(()=>run(cur),60)});
window.addEventListener('orientationchange',()=>{if(cur)setTimeout(()=>run(cur),300)});
if(document.fonts&&document.fonts.ready)document.fonts.ready.then(()=>{if(cur)run(cur)});
window.POG_CLOSEFIT_RUN=run;
watch();
})();
