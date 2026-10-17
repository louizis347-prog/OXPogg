/* Menu moderno do curso: hero com progresso, Continuar, níveis, arcos recolhíveis */
(function(){
const _course=window.course;
window.course=function(id){
  _course.apply(this,arguments);
  try{cmBuild(id)}catch(e){console.warn('menu',e)}
};
function cmBuild(id){
  const c=COURSES[id],eps=EP[id]||[],real=eps.filter(e=>!e.pl),
    done=real.filter(e=>ST.done[id+'-'+e.n]).length,total=real.length,all=eps.length;
  const pct=total?Math.round(done/total*100):0;
  const nextI=eps.findIndex(e=>!e.pl&&!ST.done[id+'-'+e.n]);
  const nxt=nextI>=0?eps[nextI]:null;
  const es=c.ui==='es';
  const tx={cont:es?'Continuar':'Continuar',start:es?'Empezar':'Começar',
    ep:es?'Episodio':'Episódio',done:es?'completos':'concluídos',soon:es?'próximamente':'em breve',
    avail:es?'disponibles':'disponíveis',lv:es?'Nivel':'Nível',all:es?'Todos los niveles':'Todos os níveis',
    fin:es?'¡Nivel completo!':'Nível completo!',arcs:es?'Arcos':'Arcos'};
  const R=34,CIR=2*Math.PI*R;
  const g=c.group&&GROUPS[c.group];
  const chips=g&&g.sub?`<div class="cm-lv">${g.sub.map(cid=>{const lv=(cl(cid)||cid.split('-')[1]||'').toUpperCase();const d=doneCountFor?doneCountFor(cid):0,n=(EP_COUNT||{})[cid]||0;
    return `<button class="cm-chip ${cid===id?'on':''}" data-course="${cid}" aria-label="${tx.lv} ${lv}"><b>${lv}</b><i style="--p:${n?Math.min(100,d/n*100):0}%"></i></button>`}).join('')}</div>`:'';
  const cta=nxt?`<button class="cm-cta" data-ep="${id}:${nextI}"><span class="cm-play">▶</span><span class="cm-ct"><small>${done?tx.cont:tx.start}</small><b>${tx.ep} ${nxt.en||nextI+1} · ${esc(nxt.t)}</b></span><span class="cm-go">→</span></button>`
    :`<div class="cm-cta cm-fin">🏆 ${tx.fin}</div>`;
  const hero=document.createElement('section');hero.className='cm-hero';
  hero.innerHTML=`<div class="cm-row"><div class="cm-ring"><svg viewBox="0 0 80 80"><circle cx="40" cy="40" r="${R}" class="bg"/><circle cx="40" cy="40" r="${R}" class="fg" stroke-dasharray="${CIR.toFixed(1)}" stroke-dashoffset="${(CIR*(1-pct/100)).toFixed(1)}"/></svg><b>${pct}%</b></div>
    <div class="cm-stats"><div><b>${done}</b><span>${tx.done}</span></div><div><b>${total}</b><span>${tx.avail}</span></div><div><b>${Math.max(0,all-total)}</b><span>${tx.soon}</span></div></div></div>
    ${cta}${chips}`;
  const road=document.querySelector('#app .road');
  if(road)road.parentNode.insertBefore(hero,road);
  if(road)road.classList.add('cm-oldroad');
  /* arcos recolhíveis */
  const tr=document.getElementById('trail');if(!tr)return;
  const kids=[...tr.children].filter(k=>!k.matches('svg'));
  const groups=[];let cur=null;
  kids.forEach(k=>{if(k.classList.contains('arc')){cur={head:k,items:[]};groups.push(cur)}else if(cur)cur.items.push(k)});
  const curEp=nxt&&nxt.n;
  let openIdx=groups.findIndex(gr=>gr.items.some(it=>nxt&&it.dataset&&it.dataset.ep===id+':'+nextI));
  if(openIdx<0)openIdx=0;
  groups.forEach((gr,gi)=>{
    const nodes=gr.items.filter(i=>i.classList.contains('node')),
      d=nodes.filter(n=>n.classList.contains('done')).length,
      pl=nodes.filter(n=>n.classList.contains('locked')).length,tt=nodes.length-pl;
    gr.head.classList.add('cm-arch');
    const bar=document.createElement('em');bar.className='cm-ab';bar.innerHTML=`<i style="width:${tt?d/tt*100:0}%"></i>`;
    const cnt=document.createElement('span');cnt.className='cm-ac';cnt.textContent=tt?`${d}/${tt}`:(es?'próximamente':'em breve');
    const chev=document.createElement('span');chev.className='cm-chev';chev.textContent='›';
    gr.head.append(cnt,chev);gr.head.appendChild(bar);
    gr.head.setAttribute('role','button');gr.head.tabIndex=0;
    const set=open=>{gr.head.classList.toggle('open',open);gr.items.forEach(i=>i.classList.toggle('cm-hide',!open));gr.head.setAttribute('aria-expanded',open)};
    gr.set=set;set(gi===openIdx);
    const tog=()=>set(!gr.head.classList.contains('open'));
    gr.head.onclick=tog;gr.head.onkeydown=e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();tog()}};
  });
  const s=document.getElementById('epsearch');
  if(s){const prev=s.oninput;s.oninput=ev=>{const q=ev.target.value.trim();
    if(q){tr.classList.add('cm-search');tr.querySelectorAll('.cm-hide').forEach(x=>x.classList.remove('cm-hide'))}
    else{tr.classList.remove('cm-search');groups.forEach(gr=>gr.set(gr.head.classList.contains('open')))}
    prev.call(s,ev)}}
  const ob=document.querySelector('#trail .node.next');
  if(ob)setTimeout(()=>{},0);
}
})();
