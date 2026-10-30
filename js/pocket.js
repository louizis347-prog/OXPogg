/* Pocket · inglês · episódios de 5 quadros: pkhero (Cena), pkdlg (Diálogo), pkbuild (Monte a frase), pkspeak (Fale), wrap (Mochila).
   Usa os mesmos helpers globais do Neighbors (FXR, say, cta, fxSay, fxKindBar, PogCover, PogFace, PogVoice). */
(function(){
if(typeof FXR==='undefined'||typeof FX_KIND==='undefined')return;
const L={pkhero:'Cena',pkdlg:'Diálogo',pkbuild:'Monte a frase',pkspeak:'Fale'};
Object.keys(L).forEach(k=>{FX_KIND[k]=k==='pkspeak'?'speak':k==='pkhero'?'story':'practice';FX_LABEL[k]=L[k]});
const q=(s,r)=>(r||document).querySelector(s);
const H=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const say2=(t,w,slow)=>{try{fxSay(String(t),w,slow)}catch(e){}};
const sfx2=n=>{try{sfx(n)}catch(e){}};
const lock=()=>{P.fx.done=false;P.fx.cta=()=>!P.fx.done};
const th=f=>'style="--g1:'+(f.g||['#FF8A5B'])[0]+';--g2:'+(f.g||[0,'#FFC857'])[1]+'"';
const av=(em,name,col)=>{try{return window.NBF?NBF.avatar(em,name,col):(window.PogFace?PogFace.avatar(em,name,col):em)}catch(e){return em}};
const strip=()=>{try{const e=P.e,h=e.fr.find(x=>x.k==='pkhero');return '<div class="pk-strip">'+coverOf(e,h,true)+'</div>'}catch(x){return ''}};
const coverOf=(e,f,noc)=>{try{return PogCover.svg({n:e.n,t:e.t,sc:e.sc,fr:[{k:'nbhero',face:f.face,name:f.name,city:f.city,num:f.num}]},{full:true,noChar:!!noc})}catch(x){return ''}};

/* 1 · Cena */
FXR.pkhero=function(f,st,n){
  const e=P.e;
  st.innerHTML='<div class="step fx pk pk-hero" '+th(f)+'>'+fxKindBar(f,n)+
   '<div class="pk-poster"><div class="pk-scene">'+coverOf(e,f)+'<span class="pk-badge">'+(f.boss?'⭐ DESAFIO DO ARCO':'EPISÓDIO '+f.num)+' · '+H(f.lvl)+'</span></div>'+
   '<div class="pk-info"><span class="pk-face">'+av(f.face,f.name,f.g[0])+'</span><h2>'+H(e.t)+'</h2><p class="pk-sub">'+H(f.name)+' · '+H(f.city)+'</p>'+
   '<div class="pk-mis"><small>SUA MISSÃO</small>'+H(f.mission)+'</div>'+
   '<button class="pk-key" id="pkk" type="button">🔊 <b>“'+H(f.hook[0])+'”</b><em>'+H(f.hook[1])+'</em></button></div></div></div>';
  q('#pkk',st).onclick=()=>{sfx2('pop');say2(f.hook[0],f.name)};
  setTimeout(()=>say2(f.hook[0],f.name),450);
  cta(f.boss?'Aceitar o desafio':'Vamos lá',true,true);say('Hoje a missão é rápida: cinco quadros!')};

/* 2 · Diálogo */
FXR.pkdlg=function(f,st,n){
  const Ls=f.lines,cast=f.cast||{},voc=f.vocab||[];let seq=0;
  const mark=t=>{let h=H(t);voc.forEach((v,i)=>{const w=String(v[0]).replace(/[.*+?^${}()|[\]\\]/g,'\\$&');h=h.replace(new RegExp('\\b('+w+')\\b','i'),'<button type="button" class="pk-w" data-v="'+i+'">$1</button>')});return h};
  st.innerHTML='<div class="step fx pk pk-dlg" '+th(f)+'>'+fxKindBar(f,n)+
   '<div class="pk-tools"><b class="pk-tt">Diálogo</b><button type="button" class="pk-btn" id="pkpt">🇧🇷 Tradução</button><button type="button" class="pk-btn" id="pkal">🔊 Ouvir tudo</button></div>'+
   '<div class="pk-chat" id="pkc">'+Ls.map((l,i)=>{const c=cast[l[0]]||['🙂','#999'],me=l[0]==='You';
     return '<div class="pk-row'+(me?' me':'')+'" data-l="'+i+'"><span class="pk-av">'+av(c[0],l[0],c[1])+'</span><div class="pk-b"><b>'+H(me?'VOCÊ':l[0])+'</b><span class="pk-en">'+mark(l[1])+'</span><small class="pk-pt">'+H(l[2])+'</small></div></div>'}).join('')+'</div>'+
   '<div class="pk-hint">Toque numa fala para ouvir · toque nas palavras marcadas para ver o significado</div><div class="pk-pop" id="pkpop" hidden></div></div>';
  const pop=q('#pkpop',st),root=q('.pk',st);
  st.querySelectorAll('.pk-w').forEach(b=>b.onclick=ev=>{ev.stopPropagation();const v=voc[+b.dataset.v];say2(b.textContent);sfx2('pop');pop.innerHTML='<b>'+H(b.textContent)+'</b> '+H(v[1]);pop.hidden=false;
    const rb=root.getBoundingClientRect(),br=b.getBoundingClientRect(),pw=Math.min(pop.offsetWidth,rb.width-16);let x=Math.max(8,Math.min(br.left-rb.left+br.width/2-pw/2,rb.width-pw-8)),y=br.top-rb.top-pop.offsetHeight-8;if(y<4)y=br.bottom-rb.top+8;pop.style.left=x+'px';pop.style.top=y+'px';b.classList.add('seen')});
  st.querySelectorAll('.pk-row').forEach(r=>r.onclick=ev=>{if(ev.target.closest('.pk-w'))return;pop.hidden=true;const l=Ls[+r.dataset.l];say2(l[1],l[0])});
  root.addEventListener('click',ev=>{if(!ev.target.closest('.pk-w'))pop.hidden=true});
  q('#pkpt',st).onclick=ev=>{q('#pkc',st).classList.toggle('pt');ev.currentTarget.classList.toggle('on')};
  q('#pkal',st).onclick=()=>{const s=++seq;(async()=>{for(let i=0;i<Ls.length&&s===seq;i++){st.querySelectorAll('.pk-row').forEach((r,j)=>r.classList.toggle('now',j===i));say2(Ls[i][1],Ls[i][0]);await new Promise(r=>setTimeout(r,1100+Ls[i][1].length*62))}st.querySelectorAll('.pk-row').forEach(r=>r.classList.remove('now'))})()};
  cta('Continuar',true,true);say('Leia o diálogo e toque para ouvir.')};

/* 3 · Monte a frase */
FXR.pkbuild=function(f,st,n){
  const R=f.items;let ri=0;lock();
  const draw=()=>{const it=R[ri];let pick=0;const tried=new Set([0]);
    const render=()=>{const o=it.opts[pick];
      st.querySelector('.pk-sent').innerHTML=H(it.en).replace('{0}','<mark>'+H(o[0])+'</mark>');
      st.querySelector('.pk-sentpt').innerHTML=H(it.pt).replace('{0}','<mark>'+H(o[1])+'</mark>')};
    st.innerHTML='<div class="step fx pk pk-build" '+th(f)+'>'+strip()+'<div class="pk-prog">'+R.map((_,i)=>'<i class="'+(i<ri?'on':'')+'"></i>').join('')+'</div>'+
     '<div class="pk-card"><div class="pk-sent"></div><div class="pk-sentpt"></div><button class="pk-btn" id="pkhear" type="button">🔊 Ouvir</button></div>'+
     '<div class="pk-hint">Toque numa peça para trocar a palavra. Experimente todas!</div>'+
     '<div class="pk-opts">'+it.opts.map((o,i)=>'<button type="button" class="pk-opt'+(i===0?' on':'')+'" data-i="'+i+'"><b>'+H(o[0])+'</b><small>'+H(o[1])+'</small></button>').join('')+'</div></div>';
    render();
    const speak=()=>{const o=it.opts[pick];say2(it.en.replace('{0}',o[0]))};
    q('#pkhear',st).onclick=speak;
    st.querySelectorAll('.pk-opt').forEach(b=>b.onclick=()=>{pick=+b.dataset.i;tried.add(pick);sfx2('step');st.querySelectorAll('.pk-opt').forEach(x=>x.classList.toggle('on',x===b));b.classList.add('seen');render();speak();
      if(tried.size>=it.opts.length){P.fx.cta=()=>{ri++;if(ri<R.length)draw();else{P.fx.done=true;return false}return true};cta(ri<R.length-1?'Próxima ▶':'Continuar',true,true)}});
    P.fx.cta=()=>true;cta('Troque as peças',false)};
  draw();say('Troque as palavras e ouça como a frase muda.')};

/* 4 · Fale */
FXR.pkspeak=function(f,st,n){
  const R=f.items,cast=(P.e.fr.find(x=>x.k==='pkdlg')||{}).cast||{};let ri=0;lock();
  const draw=()=>{const it=R[ri],c=cast[it.who]||['🙂','#999'];
    st.innerHTML='<div class="step fx pk pk-speak" '+th(f)+'>'+strip()+'<div class="pk-prog">'+R.map((_,i)=>'<i class="'+(i<ri?'on':'')+'"></i>').join('')+'</div>'+
     '<div class="pk-row"><span class="pk-av">'+av(c[0],it.who,c[1])+'</span><div class="pk-b"><b>'+H(it.who)+'</b><span class="pk-en">'+H(it.line[0])+'</span><small style="display:block">'+H(it.line[1])+'</small></div></div>'+
     '<div class="pk-card pk-say"><small>SUA VEZ · diga em inglês</small><div class="pk-sent">'+H(it.target)+'</div><div class="pk-sentpt">'+H(it.pt)+'</div>'+
     '<div class="pk-tools"><button type="button" class="pk-btn" id="pkl">🔊 Ouvir</button><button type="button" class="pk-btn" id="pks">🐢 Devagar</button></div><div id="pkm"></div></div>'+
     '<div class="pk-tools"><button type="button" class="pk-btn" id="pksk">Pular</button></div></div>';
    q('#pkl',st).onclick=()=>say2(it.target);q('#pks',st).onclick=()=>say2(it.target,null,true);
    setTimeout(()=>say2(it.line[0],it.who),350);
    const adv=()=>{ri++;if(ri<R.length)draw();else{P.fx.done=true;P.fx.cta=()=>false;cta('Continuar',true,true)}};
    const fin=()=>{sfx2('step');P.fx.cta=()=>{adv();return true};cta(ri<R.length-1?'Próxima ▶':'Concluir',true,true)};
    P.fx.cta=()=>true;cta('Fale a frase 🎤',false);
    if(window.PogVoice&&PogVoice.supported())PogVoice.mount(q('#pkm',st),{target:it.target,onDone:()=>fin(),onFail:c=>{if(c==='unsupported')q('#pkm',st).innerHTML='<div class="pk-tools"><button type="button" class="pk-btn" id="pkok">Eu falei ✔</button></div>',q('#pkok',st).onclick=fin}});
    else{q('#pkm',st).innerHTML='<div class="pk-tools"><button type="button" class="pk-btn" id="pkok">Eu falei ✔</button></div>';q('#pkok',st).onclick=fin}
    q('#pksk',st).onclick=adv};
  draw();say('Agora é você! Fale a frase em voz alta.')};

/* 5 · Mochila: reaproveita o fechamento padrão e acrescenta cartões */
const w0=FXR.wrap;
FXR.wrap=function(f,st,n){
  if(!(P.e&&P.e.pocket)||!w0)return w0&&w0.apply(this,arguments);
  const e=P.e,s=f.sticker||{};
  st.innerHTML='<div class="step fx pk pk-wrap" '+th(f)+'>'+fxKindBar({k:'wrap'},n)+
   '<div class="pk-fin"><div class="pk-stk'+(s.boss?' boss':'')+'"><span class="pk-face">'+av(s.face,s.name,(f.g||['#FF8A5B'])[0])+'</span><small>'+(s.boss?'FIGURINHA RARA':'FIGURINHA')+'</small><b>'+H(s.name)+'</b><i>'+H(s.role)+' · '+H(s.city)+'</i></div>'+
   '<div class="pk-bag"><h3>🎒 Frases para levar</h3>'+(f.recap||[]).map(r=>'<button type="button" class="pk-cc" data-t="'+H(r[0])+'"><b>'+H(r[0])+'</b><small>'+H(r[1])+'</small></button>').join('')+'</div>'+
   '<div class="pk-bag"><h3>💬 Expressão</h3><button type="button" class="pk-cc" data-t="'+H((f.expr||[''])[0])+'"><b>'+H((f.expr||['',''])[0])+'</b><small>'+H((f.expr||['',''])[1])+'</small></button></div>'+
   '<div class="pk-cult">🌎 '+H(f.culture||'')+'</div><div class="pk-next">'+H((f.teaser||{}).t||'')+'</div></div></div>';
  st.querySelectorAll('.pk-cc').forEach(b=>b.onclick=()=>{sfx2('pop');say2(b.dataset.t)});
  try{sfx2('win');if(window.confetti)confetti(70)}catch(x){}
  cta('Concluir episódio',true,true);say('Episódio concluído!')};
})();
