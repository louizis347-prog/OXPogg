/* Tema Azulejo + aquarela/nanquim + esqueleto único (Capa·Obra·Ponte·Prática·Fechamento) */
(function(){
const AZ=window.AZ={
  on(e){return !!e&&Array.isArray(e.fr)},
  first(e){return !!e&&(e.th==='az'||(e.n>=9801&&e.n<=9810)||(e.n>=30001&&e.n<=30010))},
  STAGES:[['capa','Capa'],['obra','Obra'],['ponte','Ponte'],['pratica','Prática'],['fim','Fechamento']],
  stageOf(k,e){if(k==='hook')return AZ.stageOf('cover',e);if(e&&e.mdl===2)return k==='cover'||k==='review'?0:k==='read'?1:k==='wrap'?4:/^(words|wsent|verbs|vplay|pat|scene|dquiz|xpr|grammar)$/.test(k)?2:3;return k==='cover'?((e&&e.fr&&e.fr.findIndex(f=>f.k==='cover')>0)?2:0):(k==='cult1'||k==='cwords'||k==='cquiz')?1:k==='bridge'?2:k==='wrap'?4:3},
  TYPE:{regular:'Regular',extra:'Extra',revisao:'Revisão',teste:'Teste'}
};
/* esqueleto: capa primeiro, ponte entre obra e lição */
const _fb=window.fxBridge;
window.fxBridge=function(e){if(e&&e.baked)return;_fb(e);try{
  if(!AZ.first(e)||e._azo)return;e._azo=1;
  const i=e.fr.findIndex(f=>f.k==='cover');
  if(i>0){const c=e.fr.splice(i,1)[0];e.fr.unshift(c)}
}catch(x){}};
/* paletas por episódio (sem roxo): [cor1, cor2, escura, clara] */
const PAL=[['#1FAE9B','#52C98F','#0F6E62','#E3F6F0'],['#25B5A8','#4FC4D9','#0F6A67','#E2F6F5'],['#2DB87C','#7AD08A','#17714A','#E6F7EC'],['#1BA79A','#6FCB8E','#0E655B','#E1F5EF'],['#3BBF8A','#38B6C4','#146E57','#E4F7F0']];
/* identidade por idioma (sem roxo): [cor1, cor2, escura, clara] × 4 variações que alternam de episódio em episódio */
const PALS={
 en:[['#2F6FED','#5B9BFF','#1B4DB3','#E7F0FF'],['#1E88C9','#4FB3E6','#0F5E8F','#E3F3FC'],['#3B5BDB','#6C8CFF','#2740A8','#E8EDFF'],['#0E7490','#38B2C9','#0B4F63','#E0F3F7']],
 es:[['#E4572E','#FF8A5B','#A93A18','#FFEDE6'],['#D9483B','#F28B6B','#9C2F25','#FDECE8'],['#E07A1F','#F5A84F','#99510B','#FFF1DE'],['#C94C6E','#EE8BA3','#8E2C48','#FCE9EF']],
 fr:[['#B02A4B','#DD6A87','#7E1932','#FBE9EE'],['#C0392B','#E4806F','#85241A','#FCEAE7'],['#A63D6F','#D683A8','#6F2347','#F9E8F1'],['#BF4A2B','#E88A62','#80301A','#FDECE4']],
 de:[['#E8A317','#F7C948','#8F6208','#FFF6DA'],['#D98324','#F5B365','#8A4F0F','#FFF0DD'],['#B8860B','#E0B84D','#6F500A','#FBF3D9'],['#C2410C','#F28A55','#7C2A07','#FFEDE3']],
 ja:[['#EC5F94','#FF9CC0','#B02E63','#FFE9F2'],['#E64980','#F78FB3','#A61E4D','#FFEAF2'],['#F06595','#FFA8C5','#B02A5C','#FFEBF3'],['#E8588A','#FF9BB9','#A82A55','#FFE8F0']],
 it:PAL.slice(0,4),pt:PAL.slice(0,4)
};
const GROUP={nb:'en',nbeng:'en',nbes:'es',nbfr:'fr',nbde:'de',nbja:'ja',nbit:'it',nbpt:'pt',enes:'es',eng:'en'};
function palFor(){const cid=String((P&&P.cid)||'');let g=(P&&P.c&&P.c.group)||cid.split('-')[0];g=GROUP[g]||g;const set=PALS[g]||PALS.en;return set[((((P.e&&P.e.o)||1)-1)>>1)%set.length]}
const ICO=['🎟️','🎬','🌉','🎮','🏁'];
function rail(f,n){
  const e=P.e,fr=e.fr,st=fr.map(x=>AZ.stageOf(x.k,e)),cnt=[0,0,0,0,0];st.forEach(s=>cnt[s]++);
  const cur=st[n],before=st.slice(0,n).filter(s=>s===cur).length;
  const es=typeof fxEsOn==='function'&&fxEsOn();const names=es?['Portada','Obra','Puente','Práctica','Final']:['Capa','Obra','Ponte','Prática','Final'];
  const seg=names.map((nm,i)=>{if(!cnt[i])return '';const fill=i<cur?100:i>cur?0:Math.round((before+1)/cnt[i]*100);
    return `<div class="az-s ${i<cur?'done':i===cur?'on':''}" title="${nm}" style="flex:${cnt[i]>3?11:5}"><i style="width:${fill}%"></i></div>`}).join('');
  return `<div class="az-seg" role="progressbar" aria-label="${es?'Etapas del episodio':'Etapas do episódio'}" aria-valuemin="1" aria-valuemax="${fr.length}" aria-valuenow="${n+1}">${seg}</div><span class="az-pos"><b>${names[cur]}</b> ${n+1}/${fr.length}</span>`;
}
AZ.rail=rail;
function emojis(e){
  const ws=e.fr.find(f=>f.k==='words'),out=[];
  (ws&&ws.items||[]).forEach(i=>{const x=String(i[1]||'').trim();if(x&&!out.includes(x))out.push(x)});
  return out.slice(0,6);
}
const POS=[[8,18],[72,6],[84,48],[66,82],[10,70],[40,-2]];
function hero(f,e,st){
  const step=st.querySelector('.step'),old=step.querySelector('.fx-hero'),tb=step.querySelector('.fx-titleblock');if(!old||!tb)return;
  const em=emojis(e);
  const bubs=em.map((m,i)=>`<span class="az-bub" style="left:${POS[i][0]}%;top:${POS[i][1]}%;animation-delay:-${i*.8}s">${/^(flag|svg):/.test(m)&&typeof fxIcon==='function'?fxIcon(m,34):esc(m)}</span>`).join('');
  const h=document.createElement('section');h.className='az-hero';
  const art=(()=>{try{if(window.PogCover)return `<div class="az-scene">${PogCover.svg(e)}</div>`}catch(x){}return ''})();
  h.innerHTML=`${art||`<div class="az-orbit"><div class="az-blob"></div><div class="az-pg">${poggie({cls:'',scarf:'#FFE58A'})}</div>${bubs}</div>`}
   <span class="az-ep">${esc((tb.querySelector('.fx-ep')||{}).textContent||'')}</span><h1>${esc(e.t)}</h1><p>${esc(f.sub||'')}</p>`;
  old.replaceWith(h);tb.remove();
}

const ILL={read:{tag:'📖'},gap:{tag:'✏️',pen:1},choose:{tag:'💬'},trap:{tag:'🔍',lens:1},order:{tag:'🔀'}};
function castOf(e){
  const out=[];const add=(n,em,c)=>{if(n&&em&&!out.some(x=>x.n===n))out.push({n,em,c})};
  e.fr.forEach(f=>{
    if(f.k==='scene'&&f.cast)Object.entries(f.cast).forEach(([n,v])=>add(n,v[0],v[1]));
    if(f.k==='convo'&&f.cast){const c=f.cast;if(c.npc)add(c.npc[2],c.npc[0],c.npc[1]);if(c.you)add(c.you[2],c.you[0],c.you[1])}
  });
  return out.slice(0,2);
}
function illus(step,f){
  try{
    const e=P.e,I=ILL[f.k],cast=f.k==='read'?(f.props||[]).slice(0,3).map(em=>({n:'',em,c:'#2BB3A6'})):castOf(e);
    const key=f.rs||AZ.scn(e,'scene');let bk='';
    if(key&&window.RS&&RS[key])bk=`<div class="az-ill-bk">${AZ.svg(key)}</div>`;
    const av=cast.map((c,i)=>`<span class="az-av ${i?'r':'l'}" style="--c:${c.c||'#2BB3A6'}"><b>${/^(flag|svg):/.test(c.em)&&typeof fxIcon==='function'?fxIcon(c.em,34):c.em}</b></span>`).join('');
    const d=document.createElement('div');d.className='az-ill';
    d.innerHTML=`${bk}${av}<div class="az-ill-pg">${poggie({scarf:(P.c&&P.c.scarf)||'#FFE58A',lens:I.lens,pen:I.pen})}</div><span class="az-ill-tag">${I.tag}</span>`;
    const anchor=step.querySelector('.fx-h')||step.firstElementChild;
    if(anchor&&anchor.parentNode===step)anchor.before(d);else step.prepend(d);
  }catch(x){console.warn('ill',x)}
}
const TWO={read:'.az-ill',gap:'.az-ill',choose:'.az-ill',trap:'.az-ill',order:'.az-ill',cover:'.az-hero',cult1:'.cu-poster',scene:'.fx-stagewrap',convo:'.fx-stagewrap',pbridge:'.pgx-scene',pballoon:'.pgx-scene',pfish:'.pgx-scene'};
function twoCol(step,f){
  const sel=TWO[f.k];if(!sel)return;
  const m=[...step.children].find(c=>c.matches(sel));if(!m)return;
  m.classList.add('az-media');step.classList.add('az-two');
}
const _rf=window.renderFx;
window.renderFx=function(n,st,lang){
  _rf(n,st,lang);
  try{
    const pl=document.getElementById('player');if(!pl)return;
    const on=AZ.on(P.e);pl.classList.toggle('az',on);
    if(!on)return;
    const pal=palFor()||PAL[0];
    pl.style.setProperty('--az1',pal[0]);pl.style.setProperty('--az2',pal[1]);pl.style.setProperty('--azd',pal[2]);pl.style.setProperty('--azl',pal[3]);
    const step=st.querySelector('.step');if(!step)return;
    const f=P.e.fr[n];
    step.querySelectorAll('.fx-cul,.fx-banner,.fx-mini').forEach(x=>x.remove());
    if(ILL[f.k]&&!step.querySelector('.az-ill'))illus(step,f);
    st._azn=n;
    if(!st._azo){st._azo=new MutationObserver(()=>{try{
      const fr=P.e&&P.e.fr&&P.e.fr[st._azn];if(!fr||!ILL[fr.k]||!AZ.on(P.e))return;
      const sp=st.querySelector('.step');if(!sp||sp.querySelector('.az-ill'))return;
      sp.querySelectorAll('.eyebrow,.fx-cul,.fx-banner,.fx-mini').forEach(x=>x.remove());
      illus(sp,fr);twoCol(sp,fr);
    }catch(x){}});st._azo.observe(st,{childList:true})}
    if(f.k==='cover'){const h=step.querySelector('.az-hero');if(h&&!h.querySelector('.az-meta')){const nf=P.e.fr.length;h.insertAdjacentHTML('beforeend',`<div class="az-meta"><span>🎬 ${nf} quadros</span><span>⏱ ~${Math.max(8,Math.round(nf*.75))} min</span><span>⭐ ${esc(f.badge||'A1')}</span></div>`)}}
    if(f.k==='soundlab'&&!step.querySelector('.sl-hero')){
      const h2=step.querySelector('.fx-h');
      if(h2){const hero=document.createElement('div');hero.className='sl-hero';
        hero.innerHTML=`<span class="sl-ic">🔬</span><div><small>Laboratório de sons</small><b>${esc(f.short||String(f.title||'').replace(/^Laborat[^:]*:\s*/,''))}</b></div><span class="sl-wave"><i></i><i></i><i></i><i></i><i></i></span>`;
        h2.replaceWith(hero)}
      const secs=[...step.querySelectorAll(':scope>.sl-sec')];
      if(secs.length){const grid=document.createElement('div');grid.className='sl-grid';secs[0].before(grid);secs.forEach((x,i)=>{x.classList.add('s'+i);grid.appendChild(x)})}
    }
    if(f.k==='wrap'&&!step.querySelector('.wr-hero')){
      const h2=step.querySelector('.fx-h');
      if(h2){const hero=document.createElement('div');hero.className='wr-hero';hero.innerHTML=`<span class="wr-ic">🎒</span><div><small>Fim do episódio</small><b>${esc(f.title||'Para levar na mochila')}</b></div>`;h2.replaceWith(hero)}
      step.querySelectorAll('.fx-rc').forEach((b,i)=>b.insertAdjacentHTML('afterbegin',`<i class="wr-n">${i+1}</i>`));
      try{const tz=f.teaser;const nx=step.querySelector('.fx-next');
        if(tz&&nx&&!nx.querySelector('.wr-nx')){
          const L=(typeof EP!=='undefined'&&EP[P.cid])||[];let ne=L.find(x=>x.t===tz.t&&x.n!==P.e.n)||L[(P.idx||0)+1];
          const key=ne&&AZ.scn(ne,'scene');const art=nx.querySelector('.fx-next-art');
          if(key&&window.RS&&RS[key]){const d=document.createElement('div');d.className='wr-nx';d.innerHTML=`<div class="wr-nx-bk">${AZ.svg(key)}</div><span class="wr-nx-pg">${poggie({scarf:(P.c&&P.c.scarf)||'#FFE58A'})}</span>`;
            if(art)art.replaceWith(d);else nx.prepend(d)}
        }}catch(x){console.warn('nx',x)}
    }
    if(f.k==='scene'||f.k==='convo'||f.k==='order'){const k=(f.rs&&window.RS&&RS[f.rs])?f.rs:AZ.scn(P.e,f.k==='order'?'scene':f.k),w=step.querySelector('.fx-stagewrap');if(k&&w){const old=w.querySelector('svg.fx-art');if(old){const d=document.createElement('div');d.className='az-scn';d.innerHTML=AZ.svg(k);old.replaceWith(d)}}}
    step.querySelectorAll('.eyebrow').forEach(x=>x.remove());
    twoCol(step,f);
    if(f.k==='cover')hero(f,P.e,st);
    let bar=document.getElementById('azbar');if(!bar){bar=document.createElement('div');bar.id='azbar';bar.className='az-bar';const pr=pl.querySelector('.p-head .prog');pr&&pr.after(bar)}
    bar.innerHTML=rail(f,n);
  }catch(x){console.warn('az',x)}
};
/* cenário do episódio atrás das atividades do Poggie */
const BYN={9801:'cafe',9802:'airport',9803:'lobby',9804:'subway',9805:'cafe',9806:'living',9807:'park',9808:'market',9809:'lobby',9810:'station'};
const BYK={cafe:'cafe',airport:'airport',lobby:'lobby',station:'station',living:'living',park:'park',market:'market',harbor:'pier',subwaycar:'subway',pier:'pier'};
let UID=0;
AZ.scn=function(e,kind){
  if(!window.RS)return null;
  if(kind==='pfish')return RS.lake?'lake':(RS.pier?'pier':null);
  if(kind!=='scene'&&kind!=='convo')return null;
  if(e.rs&&RS[e.rs])return e.rs;
  let k=BYN[e.n>=30001&&e.n<=30010?e.n-20200:e.n];
  if(!k){const sc=e.fr.find(f=>f.k==='scene'),cv=e.fr.find(f=>f.k==='cover');const s=(sc&&sc.art&&sc.art.s)||(cv&&cv.art&&cv.art.s);k=BYK[s]}
  return k&&RS[k]?k:null;
};
AZ.svg=k=>RS[k]('az'+(++UID));
function addBk(){
  try{
    if(typeof P==='undefined'||!P||!P.e||!AZ.on(P.e))return;
    const sc=document.querySelector('#pstage .pgx-scene');if(!sc||sc.querySelector('.pgx-bk'))return;
    const f=P.e.fr[P.fx&&P.fx.n]||{};const key=AZ.scn(P.e,f.k);
    if(!key){sc.classList.add('nobk');return}
    const d=document.createElement('div');d.className='pgx-bk';d.innerHTML=AZ.svg(key);sc.prepend(d);
    sc.classList.add('has-bk');sc.dataset.bk=key;
  }catch(x){console.warn('bk',x)}
}
const _rf2=window.renderFx;
window.renderFx=function(n,st,lang){
  _rf2(n,st,lang);
  try{
    const f=P.e.fr[n];
    if(window.PGK.includes(f.k)&&AZ.on(P.e)){
      addBk();
      if(st._azmo)st._azmo.disconnect();
      st._azmo=new MutationObserver(()=>{if(!st.querySelector('.pgx-bk'))addBk()});
      st._azmo.observe(st,{childList:true});
    }else if(st._azmo){st._azmo.disconnect();st._azmo=null}
  }catch(x){}
};
/* ao fechar o player, limpa a classe */
const _cl=window.closePlayer;
if(typeof _cl==='function')window.closePlayer=function(){try{const pl=document.getElementById('player');pl&&pl.classList.remove('az')}catch(x){}return _cl.apply(this,arguments)};
})();

/* Poggie pescador: vara no lugar do livro */
(function(){const _p=window.poggie;if(!_p)return;
window.poggie=function(o){let h=_p(o);if(o&&o.rod){
  h=h.replace(/<rect x="148" y="72"[^>]*\/><rect x="150" y="74"[^>]*\/>/,'<line x1="154" y1="96" x2="214" y2="14" stroke="#8A5A2B" stroke-width="4" stroke-linecap="round"/><line x1="154" y1="96" x2="214" y2="14" stroke="#C99A5B" stroke-width="1.4" stroke-linecap="round"/><circle cx="157" cy="93" r="5" fill="#B8384F"/><line x1="214" y1="14" x2="214" y2="196" stroke="#fff" stroke-width="1.6" opacity=".9" class="pgf-lineS"/><circle cx="214" cy="198" r="4" fill="#E85D75"/>');
  h=h.replace('<svg class="pog','<svg style="overflow:visible" class="pog');}
  if(o&&(o.lens||o.pen)){const prop=o.lens?'<circle cx="171" cy="74" r="17" fill="rgba(190,235,255,.6)" stroke="#4B5C70" stroke-width="5"/><line x1="159" y1="88" x2="150" y2="100" stroke="#4B5C70" stroke-width="6" stroke-linecap="round"/>':'<line x1="154" y1="100" x2="190" y2="58" stroke="#F6C445" stroke-width="8" stroke-linecap="round"/><path d="M186 62 l8 -8 l5 5 l-8 8z" fill="#F2A7B0"/><path d="M152 102 l-3 8 l8 -3z" fill="#3D2517"/>';
    h=h.replace(/<rect x="148" y="72"[^>]*\/><rect x="150" y="74"[^>]*\/>/,prop);h=h.replace('<svg class="pog','<svg style="overflow:visible" class="pog');}
  return h};})();

/* balões do Poggie sempre inteiros: mantém a fala dentro da cena */
setInterval(()=>{try{
  document.querySelectorAll('#player .pgx-bub').forEach(b=>{
    const sc=b.closest('.pgx-scene');if(!sc)return;
    b.style.setProperty('--bs','0px');
    const r=b.getBoundingClientRect(),s=sc.getBoundingClientRect();if(!r.width)return;
    let d=0;if(r.left<s.left+8)d=s.left+8-r.left;else if(r.right>s.right-8)d=s.right-8-r.right;
    if(d)b.style.setProperty('--bs',d.toFixed(1)+'px');
    const need=(b.closest('.pgx-hero')||b).getBoundingClientRect().top-s.top;
    b.classList.toggle('below',need<r.height+10);
  });
}catch(e){}},140);

/* ===== Pogglot · quadros "Verbos em ação" (verbs) e "Palavras que andam juntas" (xpr) =====
   verbs: lista de verbos com ícone, formas do nível (eu / ele-ela / não / passado…) e frase dita por um personagem.
   xpr:   expressões, colocações, verbo + preposição e phrasal verbs, com blocos que se encaixam ao toque.
   Também mantém a numeração dos episódios do A1 sempre sequencial (campo "en"), sem alterar os arquivos originais. */
(function(){
'use strict';
if(typeof FXR==='undefined'||typeof FX_KIND==='undefined')return;
FX_KIND.verbs='vocab';FX_KIND.xpr='vocab';
FX_LABEL.verbs='Verbos em ação';FX_LABEL.xpr='Expressões e colocações';
const BC=['#6D5BE8','#12A59B','#F26B52','#D6428E','#2F86D6','#E39A12'];
const XT={col:['🧩','Colocação'],exp:['💬','Expressão'],prep:['🔗','Verbo + preposição'],phr:['🧲','Phrasal verb'],wild:['🃏','Expressão coringa'],cexp:['💬','Expressão comum']};
const ANIM=['vb-bob','vb-wig','vb-hop'];
const cast=()=>{const sc=((P&&P.e&&P.e.fr)||[]).find(f=>f.k==='scene');const c=(sc&&sc.cast)||{};return Object.keys(c).slice(0,2).map(n=>({n,em:c[n][0],c:c[n][1]}))};
const avatar=c=>c?`<span class="vb-av" style="--c:${c.c}"><b>${c.em}</b></span>`:'';
const later=(fn,ms)=>{clearTimeout(fxSeq.t);fxSeq.t=setTimeout(()=>{if(document.getElementById('player'))fn()},ms)};
const dur=t=>Math.max(900,String(t).length*80+450);
const pogMini=()=>`<span class="vb-pg" aria-hidden="true">${poggie({scarf:(P.c&&P.c.scarf)||'#FFE58A'})}</span>`;
const hl=s=>mk(s);

/* ---------- Verbos em ação ---------- */
FXR.verbs=function(f,st,n){
  const C=cast(),seen=new Set(),R=f.items;
  const card=(it,i)=>{
    const who=C[(it.who!=null?it.who:i)%Math.max(1,C.length)]||null;
    const words=String(it.v).split(' ');
    return `<div class="vb-card" data-i="${i}" style="--i:${i};--k:${BC[i%BC.length]}">
      <button class="vb-top" type="button" aria-expanded="false"><span class="vb-ic ${ANIM[i%3]}"><span>${fxIcon(it.ic,40)}</span></span>
        <span class="vb-main"><b class="vb-v">${words.map((w,j)=>`<i style="--b:${BC[(i+j)%BC.length]}">${esc(w)}</i>`).join('')}</b><small class="vb-pt">${esc(it.pt)}</small></span>
        <span class="say2" aria-hidden="true">${spk}</span></button>
      <div class="vb-more">
        <div class="vb-forms">${(it.f||[]).map(x=>`<button class="vb-form" type="button" data-s="${esc(plain(x[1]))}"><small>${esc(x[0])}</small><span>${hl(x[1])}</span></button>`).join('')}</div>
        <button class="vb-say" type="button" data-s="${esc(plain(it.ex[0]))}" data-w="${who?esc(who.n):''}">${avatar(who)}<span class="vb-bub"><b>${who?esc(who.n):''}</b><p>${hl(it.ex[0])}</p><small>${esc(it.ex[1])}</small></span><span class="say2" aria-hidden="true">${spk}</span></button>
        ${it.note?`<div class="vb-note"><span>⚠️</span><p>${hl(it.note)}</p></div>`:''}
      </div></div>`};
  st.innerHTML=`<div class="step fx fx-vb">${fxKindBar(f,n)}
    <div class="vb-head"><div><small class="vb-kicker">⚡ ${R.length} verbos para usar hoje</small><h2 class="fx-h">${esc(f.title||'Verbos em ação')}</h2></div>${pogMini()}</div>
    ${f.intro?`<p class="vb-intro">${hl(f.intro)}</p>`:''}
    <div class="vb-list">${R.map(card).join('')}</div>
    <p class="fx-hint" id="fxhint">Toque em cada verbo: veja as formas e ouça a frase.</p>
    ${f.tip?`<div class="fx-tip">💡 ${hl(f.tip)}</div>`:''}</div>`;
  const cards=[...st.querySelectorAll('.vb-card')];
  cards.forEach(c=>{
    const i=+c.dataset.i,it=R[i];
    c.querySelector('.vb-top').onclick=()=>{
      const first=!c.classList.contains('open');
      c.classList.add('open');c.querySelector('.vb-top').setAttribute('aria-expanded','true');seen.add(i);sfx('pop');
      fxSay(plain(it.v));
      later(()=>fxSay(plain(it.ex[0]),(cast()[(it.who!=null?it.who:i)%Math.max(1,cast().length)]||{}).n),dur(it.v)+250);
      if(first)setTimeout(()=>{try{c.scrollIntoView({behavior:'smooth',block:'nearest'})}catch(e){}},120);
      if(seen.size>=R.length){cta('Continuar',true,true);const h=document.getElementById('fxhint');if(h)h.textContent='Todos descobertos! 🎉'}
      else{const h=document.getElementById('fxhint');if(h)h.textContent=`${seen.size}/${R.length} verbos descobertos`}
    };
    c.querySelectorAll('.vb-form').forEach(b=>b.onclick=ev=>{ev.stopPropagation();clearTimeout(fxSeq.t);sfx('pop');fxSay(b.dataset.s)});
    const sy=c.querySelector('.vb-say');sy.onclick=ev=>{ev.stopPropagation();clearTimeout(fxSeq.t);sfx('pop');fxSay(sy.dataset.s,sy.dataset.w||undefined)};
  });
  cta('Descubra todos os verbos',false);say(f.say||'Verbo é ação! Toque em cada um para ver as formas.');
};

/* ---------- Expressões e colocações ---------- */
/* palavra trocável de um item coringa: o texto da peça sem o final fixo (?, please…) */
function xprWord(it){const t=it.tail||'',x=it.b[it.slot][0];return t&&x.endsWith(t)?x.slice(0,x.length-t.length):x}
FXR.xpr=function(f,st,n){
  const C=cast(),seen=new Set(),R=f.items;
  FX_LABEL.xpr=R.some(x=>x.t==='wild')?'Expressões coringa':'Expressões e colocações';
  const tile=(it,i)=>{
    const t=XT[it.t]||XT.col,who=C[(it.who!=null?it.who:i+1)%Math.max(1,C.length)]||null;
    const bl=(it.b||[]).map((b,j)=>`<i class="${j?'b':'a'}${it.slot===j?' sl':''}" data-j="${j}" style="--b:${b[1]||BC[(i+j)%BC.length]}">${esc(b[0])}</i>`).join('');
    return `<div class="xp-tile t-${it.t||'col'}" data-i="${i}" style="--i:${i}">
      <button class="xp-top" type="button" aria-expanded="false">
        <span class="xp-type"><em>${t[0]}</em>${t[1]}</span>
        <span class="xp-ic">${fxIcon(it.ic,40)}</span>
        <span class="xp-blocks">${bl}</span>
        <small class="xp-pt">${esc(it.pt)}</small></button>
      <div class="xp-more">
        ${it.no?`<div class="xp-vs"><s>${esc(it.no)}</s><span>→</span><b>${esc(plain((it.b||[]).map(b=>b[0]).join(' ')))}</b></div>`:''}
        <button class="xp-say" type="button" data-s="${esc(plain(it.ex[0]))}" data-w="${who?esc(who.n):''}">${avatar(who)}<span class="vb-bub"><b>${who?esc(who.n):''}</b><p>${hl(it.ex[0])}</p><small>${esc(it.ex[1])}</small></span><span class="say2" aria-hidden="true">${spk}</span></button>
        ${it.sw?`<div class="xp-sw"><small>🔁 Troque a peça tracejada por:</small><div class="xp-chips">${[[xprWord(it),it.pt]].concat(it.sw).map((q,j)=>`<button type="button" class="xp-chip${j?'':' on'}" data-j="${j}">${esc(q[0])}</button>`).join('')}</div><div class="xp-swl"><b>${esc(plain(it.b.map(b=>b[0]).join(' ')))}</b><small>${esc(it.pt)}</small></div></div>`:''}
        ${it.cult?`<div class="vb-note"><span>🌎</span><p>${hl(it.cult)}</p></div>`:''}
        ${it.note?`<div class="vb-note"><span>💡</span><p>${hl(it.note)}</p></div>`:''}
      </div></div>`};
  st.innerHTML=`<div class="step fx fx-xp">${fxKindBar(f,n)}
    <div class="vb-head"><div><small class="vb-kicker">${f.kicker||('🧲 '+R.length+' combinações naturais')}</small><h2 class="fx-h">${esc(f.title||'Palavras que andam juntas')}</h2></div>${pogMini()}</div>
    ${f.intro?`<p class="vb-intro">${hl(f.intro)}</p>`:''}
    <div class="xp-grid">${R.map(tile).join('')}</div>
    <p class="fx-hint" id="fxhint">${esc(f.hint||'Toque em cada par: veja os blocos se encaixarem e ouça a frase.')}</p>
    ${f.tip?`<div class="fx-tip">💡 ${hl(f.tip)}</div>`:''}</div>`;
  [...st.querySelectorAll('.xp-tile')].forEach(c=>{
    const i=+c.dataset.i,it=R[i];
    c.querySelector('.xp-top').onclick=()=>{
      c.classList.add('open');c.querySelector('.xp-top').setAttribute('aria-expanded','true');seen.add(i);sfx('key');
      const whole=plain((it.b||[]).map(b=>b[0]).join(' '));
      setTimeout(()=>sfx('pop'),260);
      fxSay(whole);
      later(()=>fxSay(plain(it.ex[0]),(cast()[(it.who!=null?it.who:i+1)%Math.max(1,cast().length)]||{}).n),dur(whole)+250);
      setTimeout(()=>{try{c.scrollIntoView({behavior:'smooth',block:'nearest'})}catch(e){}},120);
      const h=document.getElementById('fxhint');
      if(seen.size>=R.length){cta('Continuar',true,true);if(h)h.textContent='Todas descobertas! 🎉'}
      else if(h)h.textContent=`${seen.size}/${R.length} descobertas`;
    };
    const sy=c.querySelector('.xp-say');sy.onclick=ev=>{ev.stopPropagation();clearTimeout(fxSeq.t);sfx('pop');fxSay(sy.dataset.s,sy.dataset.w||undefined)};
    c.querySelectorAll('.xp-chip').forEach(ch=>ch.onclick=ev=>{
      ev.stopPropagation();clearTimeout(fxSeq.t);sfx('key');
      const j=+ch.dataset.j,all=[[xprWord(it),it.pt]].concat(it.sw),q=all[j];
      c.querySelectorAll('.xp-chip').forEach(x=>x.classList.toggle('on',x===ch));
      const ws=it.b.map(b=>b[0]);ws[it.slot]=q[0]+(j?(it.tail||''):'');if(!j)ws[it.slot]=it.b[it.slot][0];
      const sl=c.querySelector('.xp-blocks i.sl');if(sl){sl.textContent=ws[it.slot];sl.classList.remove('pop');void sl.offsetWidth;sl.classList.add('pop')}
      const ph=plain(ws.join(' '));
      c.querySelector('.xp-swl').innerHTML=`<b>${esc(ph)}</b><small>${esc(q[1])}</small>`;
      fxSay(ph);
    });
  });
  cta(f.cta||(R.some(x=>x.t==='wild')?'Descubra todas as expressões':'Descubra todas as combinações'),false);say(f.say||'Algumas palavras são amigas: andam sempre juntas. Toque para juntar!');
};

/* ---------- numeração sequencial do A1 (campo "en") ---------- */
function renumber(cid){
  try{
    const L=EP&&EP[cid];if(!L||!L.length||L._rn===L.length)return;
    let k=0;L.forEach(e=>{if(typeof e.en==='number'||e.en==null){if(!e.mv&&!e.pl&&!(e.sp)&&!(e.n>20000&&e.n<21000)){k++;e.en=k}}});
    L._rn=L.length;
  }catch(x){}
}
if(typeof window.ensureLangLoaded==='function'){
  const _el=window.ensureLangLoaded;
  window.ensureLangLoaded=async function(lang){const r=await _el.apply(this,arguments);if(lang==='en-a1'||lang==='en-a2')renumber(lang);return r};
}
})();
