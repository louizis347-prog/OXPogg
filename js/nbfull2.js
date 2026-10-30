/* Neighbors (inglês A1, episódios 1–10): avatares ilustrados, quadro "Diálogo" completo (no lugar da "Leitura")
   e quadro "Expressões". Só age quando #player.nb-full está ligado (ver nbfull.js). */
(function(){
if(typeof FXR==='undefined')return;
const full=()=>{const p=document.getElementById('player');return !!(p&&p.classList.contains('nb-full'))};
const q=(s,r)=>(r||document).querySelector(s);
const H=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const hash=s=>{let h=7;for(const c of String(s))h=(h*31+c.charCodeAt(0))>>>0;return h};
try{FX_LABEL.nbopen2='Diálogo';FX_LABEL.nbfluency='Expressões'}catch(e){}

/* ---------- avatar ilustrado (gênero do personagem vem do cadastro, não do emoji) ---------- */
const TONE={'🏻':0,'🏼':1,'🏽':2,'🏾':3,'🏿':3};
const HAIR=['#2b211c','#4a3228','#7a4a2b','#1f1a17','#5b3a29','#8a5a33'];
const STYLE_M=['short','side','curly','short'],STYLE_F=['long','wavy','bob','bun'];
function avatar(em,name,color){
  const F=window.PogFace;if(!F||!F.bust)return em;
  const e=(typeof P!=='undefined'&&P&&P.e)||{};const ch=e.character||{};
  const o=F.fromEmoji?F.fromEmoji(em):{};const h=hash(name||em);
  let g=o.g;
  if(name&&ch.name===name&&(ch.gender==='m'||ch.gender==='f'))g=ch.gender;
  if(/^(you|voc)/i.test(String(name)))g='m';
  if(g!=='m'&&g!=='f')g=(h%2?'m':'f');
  const tm=String(em).match(/[\u{1F3FB}-\u{1F3FF}]/u);
  Object.assign(o,{g,seed:h,refined:true,rich:2,mood:'soft'});
  if(tm)o.tone=TONE[tm[0]];else if(o.tone==null)o.tone=h%4;
  if(!o.style||o.style==='bald')o.style=(g==='f'?STYLE_F:STYLE_M)[h%4];
  if(!o.hair)o.hair=HAIR[h%HAIR.length];
  if(/^#[0-9a-f]{6}$/i.test(color||''))o.shirt=color;
  if(g==='f')o.beard=false;
  return '<svg viewBox="16 8 68 68" width="100%" height="100%" aria-hidden="true">'+F.bust(o)+'</svg>';
}
function patch(){const F=window.PogFace;if(!F||F._nbf)return;const orig=F.avatar;F._nbf=1;
  F.avatar=function(em,name,color){if(full()){try{return avatar(em,name,color)}catch(x){}}return orig.apply(this,arguments)}}
patch();setInterval(patch,400);
window.NBF={avatar};
/* TODA figura do Neighbors (capa, fundo de cena, chat) usa o desenho refinado e natural */
function patchBust(){const F=window.PogFace;if(!F||F._nbb||!F.bust)return;const ob=F.bust;F._nbb=1;
  F.bust=function(o){try{const c=(typeof P!=='undefined'&&P&&String(P.cid||''))||'';
    if(/^nb/.test(c)&&o&&typeof o==='object'){o.refined=true;o.natural=true;if(!o.mood)o.mood='soft';if(!o.rich||o.rich<2)o.rich=2;if(o.age==='kid')o.age='adult'}}catch(x){}
    return ob.apply(this,arguments)}}
patchBust();setInterval(patchBust,400);

/* ---------- Diálogo (substitui a "Leitura") ---------- */
const origOpen2=FXR.nbopen2;
FXR.nbopen2=function(f,st,n){
  if(!full()||!origOpen2)return origOpen2&&origOpen2.apply(this,arguments);
  const e=P.e,chat=(e.fr||[]).find(x=>x.k==='nbchat'&&x.lines&&x.lines.length>2);
  if(!chat)return origOpen2.apply(this,arguments);
  const L=chat.lines,cast=chat.cast||{};
  const me=l=>l[0]==='You';
  const vocab=(f.vocab||[]).filter(v=>v&&v[0]);
  const mark=txt=>{let html=H(txt);vocab.forEach((v,i)=>{const w=String(v[0]).replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
    html=html.replace(new RegExp('\\b('+w+')\\b','i'),'<button type="button" class="nbd-w" data-v="'+i+'">$1</button>')});return html};
  const bub=L.map((l,i)=>{const c=cast[l[0]]||['🙂','#999'];
    return '<div class="nbd-row'+(me(l)?' me':'')+'" data-l="'+i+'"><span class="nbd-av">'+avatar(c[0],l[0],c[1])+'</span>'+
    '<div class="nbd-b"><b class="nbd-who">'+H(l[0]==='You'?'VOCÊ':l[0])+'</b><span class="nbd-en">'+mark(l[1])+'</span><small class="nbd-pt">'+H(l[2]||'')+'</small></div></div>'}).join('');
  const key=(f.hook&&f.hook[0])||L[0][1];
  st.innerHTML='<div class="step fx nbo nbd" style="--g1:'+(f.g||['#00B894'])[0]+';--g2:'+(f.g||[0,'#0984E3'])[1]+'">'+fxKindBar(f,n)+
   '<div class="nbd-grid"><aside class="nbd-side"><div class="nbd-art">'+(window.PogCover?PogCover.svg(e,{full:true}):'')+'</div>'+
   '<div class="nbd-key"><small>Frase do dia</small><b>“'+H(key)+'”</b></div></aside>'+
   '<section class="nbd-main"><div class="nbd-tools"><span class="nbd-tt">Diálogo · '+H(f.topic||e.s||'')+'</span>'+
   '<button type="button" class="nbd-btn" id="nbdpt">🇧🇷 Tradução</button><button type="button" class="nbd-btn" id="nbdal">🔊 Ouvir tudo</button></div>'+
   '<div class="nbd-chat" id="nbdchat">'+bub+'</div><div class="nbd-hint">Toque numa fala para ouvir. Toque nas palavras marcadas para ver o significado.</div></section>'+
   '<div class="nbd-pop" id="nbdpop" hidden></div></div></div>';
  const root=q('.nbd',st),pop=q('#nbdpop',st),chatEl=q('#nbdchat',st);let seq=0;
  const say2=(t,w)=>{try{fxSay(String(t),w)}catch(x){}};
  st.querySelectorAll('.nbd-w').forEach(b=>b.onclick=ev=>{ev.stopPropagation();const v=vocab[+b.dataset.v];say2(b.textContent,null);
    pop.innerHTML='<b>'+H(b.textContent)+'</b><span>'+H(v[1]||'')+'</span>'+(v[2]?'<small>'+H(v[2])+'</small>':'');pop.hidden=false;
    const rb=root.getBoundingClientRect(),br=b.getBoundingClientRect();const pw=Math.min(pop.offsetWidth,rb.width-16);
    let x=br.left-rb.left+br.width/2-pw/2;x=Math.max(8,Math.min(x,rb.width-pw-8));let y=br.top-rb.top-pop.offsetHeight-8;if(y<4)y=br.bottom-rb.top+8;
    pop.style.left=x+'px';pop.style.top=y+'px';b.classList.add('seen')});
  st.querySelectorAll('.nbd-row').forEach(r=>r.addEventListener('click',ev=>{if(ev.target.closest('.nbd-w'))return;pop.hidden=true;const l=L[+r.dataset.l];say2(l[1],l[0])}));
  root.addEventListener('click',ev=>{if(!ev.target.closest('.nbd-w'))pop.hidden=true});
  q('#nbdpt',st).onclick=ev=>{chatEl.classList.toggle('pt');ev.currentTarget.classList.toggle('on')};
  q('#nbdal',st).onclick=()=>{const s=++seq;(async()=>{for(let i=0;i<L.length&&s===seq;i++){
    st.querySelectorAll('.nbd-row').forEach((r,j)=>r.classList.toggle('now',j===i));say2(L[i][1],L[i][0]);await new Promise(r=>setTimeout(r,1100+L[i][1].length*62))}
    st.querySelectorAll('.nbd-row').forEach(r=>r.classList.remove('now'))})()};
  cta('Continuar',true,true);say('Leia o diálogo inteiro. Toque numa fala para ouvir.');
};

/* ---------- Expressões (no lugar de "Linguagem natural") ---------- */
const origFl=FXR.nbfluency;
FXR.nbfluency=function(f,st,n){
  if(!full()||!origFl)return origFl&&origFl.apply(this,arguments);
  const e=P.e,items=[];
  const chat=(e.fr||[]).find(x=>x.k==='nbchat'&&x.lines),allL=[].concat(...(e.fr||[]).filter(x=>x.k==='nbchat'&&x.lines).map(x=>x.lines));
  const find=en=>{const k=String(en).replace(/…|\.\.\.|\?/g,'').trim().toLowerCase();const l=allL.find(l=>l[1].toLowerCase().includes(k));return l||null};
  const key=e.g&&e.g.t;
  if(key){const l=find(key);items.push({tag:'Frase-chave',en:key,pt:'',ex:l?l[1].replace(/\*\*/g,''):'',exPt:l?l[2]:''})}
  const sl=(e.fr||[]).find(x=>x.k==='nbslang');
  if(sl){const gl=sl.gl||{};Object.keys(gl).forEach(k=>{const l=sl.lines.find(l=>l[1].replace(/\*\*/g,'').includes(k));
    items.push({tag:'Gíria',en:k,pt:gl[k],ex:l?l[1].replace(/\*\*/g,''):'',exPt:l?l[2]:''})});
    const prov=sl.lines.map(l=>(l[1].match(/\*\*([^*]*!)\*\*/)||[])[1]).filter(Boolean)[0];
    if(prov&&!items.some(i=>i.en===prov)){const l=sl.lines.find(l=>l[1].includes(prov));items.push({tag:'Ditado',en:prov,pt:l?l[2].replace(/!.*$/,'!'):'',ex:'',exPt:''})}}
  (f.chunks||[]).slice(0,3).forEach(c=>{if(!items.some(i=>i.en===c[0]))items.push({tag:'Bloco',en:c[0],pt:c[1],ex:(find(c[0])||[])[1]||'',exPt:(find(c[0])||[])[2]||''})});
  const shown=items.slice(0,6);
  st.innerHTML='<div class="step fx nbo nbfluency nbe" style="--g1:'+(f.g||['#00B894'])[0]+';--g2:'+(f.g||[0,'#0984E3'])[1]+'">'+fxKindBar(f,n)+
   '<div class="nbe-head"><h2>Expressões do episódio</h2><p>'+H(f.scene||'')+' · toque num cartão para ouvir.</p></div>'+
   '<div class="nbe-grid">'+shown.map((x,i)=>'<button type="button" class="nbe-card" data-i="'+i+'"><span class="nbe-tag">'+H(x.tag)+'</span><b>'+H(x.en)+'</b>'+(x.pt?'<em>'+H(x.pt)+'</em>':'')+
     (x.ex?'<small>“'+H(x.ex)+'”'+(x.exPt?'<i>'+H(x.exPt)+'</i>':'')+'</small>':'')+'<span class="nbe-ear">🔊</span></button>').join('')+'</div>'+
   '<div class="nbe-repair"><span>Se não entender, peça de novo</span><b>“'+H(f.repair||'Sorry, could you say that again?')+'”</b><button type="button" class="nbd-btn" id="nberp">🔊 Ouvir</button></div></div>';
  const say2=t=>{try{fxSay(String(t))}catch(x){}};
  st.querySelectorAll('.nbe-card').forEach(b=>b.onclick=()=>{const x=shown[+b.dataset.i];say2(x.en);b.classList.add('seen')});
  q('#nberp',st).onclick=()=>say2(f.repair||'Sorry, could you say that again?');
  cta('Continuar',true,true);say('Essas são as expressões de hoje. Toque para ouvir cada uma.');
};
})();
