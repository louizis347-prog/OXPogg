/* Pogglot · modo ouvir (estilo podcast): toca os diálogos dos episódios em sequência, com velocidade e avanço automático */
(function(){
'use strict';
const HL=()=>(ST.homeLang==='es'?'es':'pt');
const T={pt:{t:'Modo ouvir',now:'Tocando agora',next:'A seguir',spd:'Velocidade',tr:'Tradução',none:'Nenhum episódio com áudio neste curso.',load:'Carregando…',close:'Fechar',pick:'Escolha um curso para ouvir.',ep:'Episódio'},
 es:{t:'Modo escuchar',now:'Sonando ahora',next:'A continuación',spd:'Velocidad',tr:'Traducción',none:'Ningún episodio con audio en este curso.',load:'Cargando…',close:'Cerrar',pick:'Elige un curso para escuchar.',ep:'Episodio'}};
const k=x=>(T[HL()]||T.pt)[x];
const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const clean=s=>String(s||'').replace(/\{\{|\}\}/g,'').replace(/\*\*/g,'');
const S={cid:null,idx:0,line:0,lines:[],playing:false,rate:1,tok:0,showTr:true,eps:[]};
let el=null;
function linesOf(e){
  const fr=e.fr||[];
  const chat=fr.find(f=>f&&f.k==='nbchat'&&Array.isArray(f.lines)&&f.lines.length);
  if(chat)return chat.lines.map(l=>({who:l[0],text:clean(l[1]),tr:clean(l[2])}));
  const st=fr.find(f=>f&&Array.isArray(f.s)&&f.s.length&&Array.isArray(f.s[0]));
  if(st)return st.s.map((p,i)=>({who:i%2?'B':'A',text:clean(p[0]),tr:clean(p[1])}));
  if(e.h&&e.h.l)return [{who:'A',text:clean(e.h.l),tr:clean(e.h.tr)}];
  return [];
}
function playable(cid){return (EP[cid]||[]).map((e,i)=>({e,i})).filter(x=>!x.isPlannedEpisode(e)&&linesOf(x.e).length)}
function voice(lang){
  try{const vs=speechSynthesis.getVoices()||[],p=String(lang||'en').slice(0,2).toLowerCase(),
    c=vs.filter(v=>String(v.lang).toLowerCase().startsWith(p)),good=c.filter(v=>!/compact|espeak/i.test(v.name));
    return (good.find(v=>v.lang.toLowerCase()===String(lang).toLowerCase())||good[0]||c[0])||null}catch(e){return null}
}
function say(text,who,done){
  const my=S.tok;
  try{
    speechSynthesis.cancel();
    const u=new SpeechSynthesisUtterance(text),lang=(COURSES[S.cid]&&COURSES[S.cid].tts)||'en-US';
    u.lang=lang;
    /* O modo ouvir usa a mesma escalação do player: gênero e índice do personagem. */
    let v=voice(lang), rate=S.rate, pitch=(String(who).toLowerCase()==='you'||who==='B')?1.12:.92;
    try{
      const gm=(typeof GENDER_MAP!=='undefined')?GENDER_MAP:{}; const meta=gm[who];
      if(window.PogTTS){const picked=PogTTS.pick({lang,speaker:who,gender:meta&&meta[0],gidx:meta?meta[1]:0,guess:window.voiceGenderGuess});if(picked){if(picked.voice)v=picked.voice;if(picked.rate)rate=picked.rate;if(meta)pitch=meta[0]==='f'?1.06:.94}}
    }catch(_e){}
    if(v)u.voice=v;u.rate=rate;u.pitch=pitch;
    let fin=false;const end=()=>{if(fin)return;fin=true;if(my===S.tok)setTimeout(()=>{if(my===S.tok)done()},320)};
    u.onend=end;u.onerror=end;speechSynthesis.speak(u);
    /* segurança: alguns navegadores não disparam onend */
    setTimeout(end,Math.max(2500,text.length*130/S.rate+1500));
  }catch(e){setTimeout(()=>{if(my===S.tok)done()},1200)}
}
function step(){
  if(!S.playing)return;
  const l=S.lines[S.line];
  if(!l){return nextEp(true)}
  render();
  say(l.text,l.who,()=>{S.line++;step()});
}
function nextEp(auto){
  const p=S.eps;const pos=p.findIndex(x=>x.i===S.idx);const n=p[pos+1];
  if(!n){S.playing=false;S.tok++;render();return}
  loadEp(n.i);if(auto||S.playing)step();
}
function prevEp(){const p=S.eps,pos=p.findIndex(x=>x.i===S.idx);const n=p[Math.max(0,pos-1)];S.tok++;loadEp(n.i);if(S.playing)step();else render()}
function loadEp(i){S.idx=i;S.line=0;S.lines=linesOf(EP[S.cid][i]);media();}
function media(){try{if('mediaSession' in navigator){const e=EP[S.cid][S.idx];navigator.mediaSession.metadata=new MediaMetadata({title:e.t,artist:'Pogglot',album:(COURSES[S.cid].name||{})[HL()]||''});
  navigator.mediaSession.setActionHandler('play',()=>toggle(true));navigator.mediaSession.setActionHandler('pause',()=>toggle(false));navigator.mediaSession.setActionHandler('nexttrack',()=>{S.tok++;nextEp(false)});navigator.mediaSession.setActionHandler('previoustrack',prevEp)}}catch(x){}}
function toggle(on){
  S.playing=on==null?!S.playing:on;S.tok++;
  if(S.playing)step();else{try{speechSynthesis.cancel()}catch(e){}render()}
}
function seekLine(n){S.line=Math.max(0,Math.min(S.lines.length-1,n));S.tok++;if(S.playing)step();else render()}
function render(){
  if(!el)return;const e=EP[S.cid][S.idx],l=S.lines[S.line]||S.lines[S.lines.length-1]||{},pc=S.lines.length?S.line/S.lines.length:0;
  const nxt=S.eps.slice(S.eps.findIndex(x=>x.i===S.idx)+1,S.eps.findIndex(x=>x.i===S.idx)+5);
  const L=(window.PogUI&&PogUI.LANG)?null:null;
  el.querySelector('.sheet').innerHTML=`<div class="top"><button class="x" data-lx aria-label="${esc(k('close'))}">⌄</button><span>${esc(k('now'))}</span><span></span></div>
   <div class="art ${S.playing?'pl':''}">${PogCover.svg(e,{num:e.en||S.idx+1})}</div>
   <div class="meta"><h2>${esc(e.t)}</h2><p>${esc(((COURSES[S.cid].name||{})[HL()])||'')} · ${esc(k('ep'))} ${String(e.en||S.idx+1).padStart(2,'0')}</p></div>
   <div class="lyr"><small>${esc(l.who||'')}</small><b>${esc(l.text||'')}</b>${S.showTr&&l.tr?`<em>${esc(l.tr)}</em>`:''}</div>
   <div class="seek" data-seek><div class="bar"><i style="width:${(pc*100).toFixed(1)}%"></i></div><div class="lab"><span>${S.line+1}</span><span>${S.lines.length}</span></div></div>
   <div class="ctl"><button data-la="prev" aria-label="Anterior">⏮</button><button data-la="back" aria-label="−">↺</button><button class="pp" data-la="pp" aria-label="Play/Pause">${S.playing?'⏸':'▶'}</button><button data-la="fwd" aria-label="+">↻</button><button data-la="next" aria-label="Próximo">⏭</button></div>
   <div class="lopt"><div class="spd"><small>${esc(k('spd'))}</small>${[.75,1,1.25,1.5].map(r=>`<button data-lr="${r}" aria-pressed="${S.rate===r}">${r}×</button>`).join('')}</div><button class="trb" data-la="tr" aria-pressed="${S.showTr}">${esc(k('tr'))}</button></div>
   ${nxt.length?`<div class="q"><h3>${esc(k('next'))}</h3>${nxt.map(x=>`<button data-lq="${x.i}"><span class="n">${x.i+1}</span><b>${esc(x.e.t)}</b></button>`).join('')}</div>`:''}`;
}
async function open(cid){
  cid=cid||ST.lastCourse||Object.keys(COURSES)[0];
  if(!COURSES[cid]){return}
  document.getElementById('px-listen')?.remove();
  el=document.createElement('div');el.id='px-listen';el.className='px-listen';el.innerHTML=`<div class="bg" data-lx></div><div class="sheet"><p class="ld">${esc(k('load'))}</p></div>`;
  document.body.appendChild(el);document.body.classList.add('px-lockscroll');requestAnimationFrame(()=>el.classList.add('on'));
  try{await ensureLangLoaded(cid)}catch(e){}
  S.cid=cid;S.eps=playable(cid);
  if(!S.eps.length){el.querySelector('.sheet').innerHTML=`<div class="top"><button class="x" data-lx>⌄</button><span></span><span></span></div><p class="ld">${esc(k('none'))}</p>`;return}
  /* começa do próximo episódio não concluído */
  let start=S.eps.find(x=>!ST.done[cid+"-"+x.e.n])||S.eps[0];
  loadEp(start.i);S.playing=false;render();
}
function close(){S.tok++;S.playing=false;try{speechSynthesis.cancel()}catch(e){}if(el){const d=el;d.classList.remove('on');document.body.classList.remove('px-lockscroll');setTimeout(()=>d.remove(),260);el=null}}
document.addEventListener('click',e=>{
  const o=e.target.closest&&e.target.closest('[data-listen]');if(o){e.preventDefault();open(o.dataset.listen||null);return}
  if(!el||!el.contains(e.target))return;
  if(e.target.closest('[data-lx]')){close();return}
  const sk=e.target.closest('[data-seek]');if(sk){const r=sk.getBoundingClientRect();seekLine(Math.floor(((e.clientX-r.left)/r.width)*S.lines.length));return}
  const q=e.target.closest('[data-lq]');if(q){S.tok++;loadEp(+q.dataset.lq);S.playing=true;step();return}
  const rt=e.target.closest('[data-lr]');if(rt){S.rate=+rt.dataset.lr;if(S.playing){S.tok++;step()}else render();return}
  const a=e.target.closest('[data-la]');if(!a)return;
  switch(a.dataset.la){
    case 'pp':toggle();break;
    case 'back':seekLine(S.line-1);break;
    case 'fwd':seekLine(S.line+1);break;
    case 'next':S.tok++;nextEp(false);if(!S.playing)render();break;
    case 'prev':prevEp();break;
    case 'tr':S.showTr=!S.showTr;render();break;
  }
});
window.PogListen={open,close,state:S};
})();
