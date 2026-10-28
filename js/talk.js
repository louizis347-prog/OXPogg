/* Pogglot · conversa: "Molde de conversa" (personagens + variações) e "Converse com o Poggie" (2 diálogos de 8 falas) */
(function(){
'use strict';
if(typeof FXR==='undefined')return;
const lang=()=>(typeof P!=='undefined'&&P&&P.c&&P.c.tts)||'en-US';
const E=s=>esc(String(s==null?'':s));
const safe=(f)=>{try{return f()}catch(e){}};
FX_KIND.tmold='grammar';FX_LABEL.tmold='Molde de conversa';
FX_KIND.tchat='practice';FX_LABEL.tchat='Converse com o Poggie';

if(!document.getElementById('tk-css')){const s=document.createElement('style');s.id='tk-css';s.textContent=`
.tk-cast{display:flex;gap:10px;justify-content:center;margin:6px 0 10px}
.tk-av{display:flex;align-items:center;gap:6px;padding:4px 12px 4px 6px;border-radius:99px;background:color-mix(in srgb,var(--c) 16%,transparent);font-weight:700;font-size:.9rem}
.tk-av i{font-style:normal;font-size:1.5rem}
.tk-chat{display:flex;flex-direction:column;gap:8px;margin:8px 0}
.tk-b{max-width:86%;padding:8px 12px;border-radius:16px;background:color-mix(in srgb,var(--c) 14%,transparent);border:2px solid color-mix(in srgb,var(--c) 45%,transparent);cursor:pointer;text-align:left;font:inherit;color:inherit;display:block}
.tk-b.r{align-self:flex-end;border-bottom-right-radius:4px}.tk-b.l{align-self:flex-start;border-bottom-left-radius:4px}
.tk-b small{display:block;opacity:.65;font-size:.78rem;margin-top:2px}
.tk-b u{text-decoration:none;background:color-mix(in srgb,var(--c) 38%,transparent);border-radius:6px;padding:0 4px;font-weight:700}
.tk-b b.nm{display:block;font-size:.72rem;opacity:.7;margin-bottom:2px}
.tk-b.pop{animation:tkpop .35s}@keyframes tkpop{40%{transform:scale(1.05)}}
.tk-sl{margin:10px 0}.tk-sl h4{margin:0 0 4px;font-size:.85rem;opacity:.8}
.tk-ch{display:flex;flex-wrap:wrap;gap:6px}
.tk-c{padding:7px 12px;border-radius:99px;border:2px solid #7C4DFF55;background:transparent;color:inherit;font:inherit;cursor:pointer}
.tk-c.on{background:#6DDFDB;color:#fff;border-color:#6DDFDB}.tk-c.sw{outline:2px solid #12B3A8}
.tk-ops{display:flex;flex-direction:column;gap:8px;margin:10px 0}
.tk-o{padding:10px 12px;border-radius:14px;border:2px solid #7C4DFF55;background:transparent;color:inherit;font:inherit;text-align:left;cursor:pointer}
.tk-o small{display:block;opacity:.65}.tk-o.bad{border-color:#e5484d;animation:tkshake .4s}.tk-o.hint{border-color:#12B3A8;box-shadow:0 0 0 3px #12B3A855}
@keyframes tkshake{25%{transform:translateX(-6px)}75%{transform:translateX(6px)}}
.tk-mic{margin-top:4px;padding:3px 10px;border-radius:99px;border:1px solid currentColor;background:transparent;color:inherit;font:inherit;font-size:.78rem;cursor:pointer;opacity:.85}
.tk-prog{display:flex;gap:4px;margin:6px 0}.tk-prog i{flex:1;height:6px;border-radius:4px;background:#8884}.tk-prog i.on{background:#12B3A8}
.tk-end{text-align:center;font-weight:700;margin:8px 0}.tk-gap{display:inline-block;min-width:3.2em;border-bottom:2px dashed currentColor;opacity:.55;text-align:center}.tk-pieces{margin-top:6px;display:flex;flex-direction:column;gap:6px}.tk-pk{display:flex;flex-wrap:wrap;gap:6px}.tk-c.bad{background:#e5484d33;border-color:#e5484d;animation:tkshake .4s}`;document.head.appendChild(s)}

const fill=(tpl,idx,slots,hl)=>tpl.replace(/\{(\w+)\}/g,(m,k)=>{const sl=slots[k];if(!sl)return m;const v=(sl[idx[k]||0]||sl[0]);return hl?'\u0001'+v+'\u0002':v});
const mark=(s)=>E(s).replace(/\u0001/g,'<u>').replace(/\u0002/g,'</u>');
const plainT=(s)=>String(s).replace(/[\u0001\u0002]/g,'');

/* ---------- 1) Molde de conversa ---------- */
FXR.tmold=function(f,st,n){
  const cast=f.cast,slots={},ids=Object.keys(f.slots);
  ids.forEach(k=>slots[k]=f.slots[k]);
  const idx={},swapped=new Set();ids.forEach(k=>idx[k]=0);
  const NEED=Math.min(2,ids.length);
  const slotIdx=(k)=>{ /* slot "x2" acompanha o slot "x" */ return idx[k]};
  const val=(k,j)=>{const b=k.length>1&&/2$/.test(k)&&slots[k.slice(0,-1)]?k.slice(0,-1):null;return b?slots[k][idx[b]]:slots[k][idx[k]]};
  const render=(tpl,li)=>tpl.replace(/\{(\w+)\}/g,(m,k)=>{if(!slots[k])return m;return '\u0001'+(val(k)[li])+'\u0002'});
  const linkIds=ids.filter(k=>!(k.length>1&&/2$/.test(k)&&slots[k.slice(0,-1)]));
  const draw=(only)=>{
    const chat=st.querySelector('.tk-chat');
    chat.innerHTML=f.lines.map((l,i)=>{const c=cast[l[0]];const en=render(l[1],0),pt=render(l[2],1);
      return `<button type="button" class="tk-b ${l[0]?'r':'l'}" data-i="${i}" style="--c:${c[1]}"><b class="nm">${c[0]} ${E(c[2])}</b>${mark(en)}<small>${mark(pt)}</small></button>`}).join('');
    chat.querySelectorAll('.tk-b').forEach(b=>b.onclick=()=>{sfx('pop');fxSay(plainT(render(f.lines[+b.dataset.i][1],0)))});
  };
  const upd=()=>{
    const c=swapped.size;
    if(c>=NEED)cta('Continuar',true,true);else cta(`Troque ${NEED-c} peça${NEED-c>1?'s':''} para continuar`,false);
    const m=st.querySelector('.tk-msg');if(m)m.textContent=c>=NEED?'🎉 Você montou uma conversa nova! Toque nos balões e repita em voz alta.':'Toque nas peças abaixo e veja a conversa mudar.';
  };
  st.innerHTML=`<div class="step fx m2-sb5">${fxKindBar(f,n)}
   <div class="m2-wh"><h2 class="fx-h">${E(f.title||'Molde de conversa')}</h2></div>
   <div class="m2-vpb"><span>🦫</span><p>${E(f.sub||'Troque as peças e monte novas conversas!')}</p></div>
   <div class="tk-cast">${cast.map(c=>`<span class="tk-av" style="--c:${c[1]}"><i>${c[0]}</i>${E(c[2])}</span>`).join('')}</div>
   <div class="tk-chat"></div>
   ${linkIds.map((k,qi)=>`<div class="tk-sl" data-k="${k}"><h4>${E(f.labels&&f.labels[k]||('Peça '+(qi+1)+' · toque para trocar'))}</h4><div class="tk-ch">${slots[k].map((o,j)=>`<button type="button" class="tk-c${j===0?' on':''}" data-j="${j}">${E(o[0])}</button>`).join('')}</div></div>`).join('')}
   <p class="tk-end tk-msg"></p></div>`;
  draw();
  st.querySelectorAll('.tk-sl').forEach(box=>{const k=box.dataset.k;
    box.querySelectorAll('.tk-c').forEach(b=>b.onclick=()=>{
      const j=+b.dataset.j;idx[k]=j;
      ids.forEach(x=>{if(x!==k&&x.length>1&&/2$/.test(x)&&x.slice(0,-1)===k)idx[x]=j});
      box.querySelectorAll('.tk-c').forEach(x=>x.classList.toggle('on',x===b));
      if(j!==0&&!swapped.has(k)){swapped.add(k);b.classList.add('sw')}
      sfx('pop');draw();
      const hit=f.lines.findIndex(l=>l[1].indexOf('{'+k+'}')>=0);
      const el=st.querySelector(`.tk-b[data-i="${hit}"]`);if(el){el.classList.add('pop');fxSay(plainT(render(f.lines[hit][1],0)))}
      if(swapped.size===NEED&&!st.dataset.won){st.dataset.won='1';safe(()=>burst(st.querySelector('.tk-chat')));safe(()=>sfx('key'))}
      upd();
    })});
  P.fx.cta=()=>false;
  upd();
  say(f.say||'Molde de conversa: troque as peças e invente novas conversas!');
};

/* ---------- 2) Converse com o Poggie ---------- */
const hash=s=>{let h=7;for(const c of s)h=(h*31+c.charCodeAt(0))>>>0;return h};
const norm=s=>String(s).toLowerCase().replace(/[^a-z' ]/g,' ').split(/\s+/).filter(Boolean);
FXR.tchat=function(f,st,n){
  const R=f.rounds,N=R.length;let ri=0,score=0;
  const draw=()=>{
    const r=R[ri],T=r.turns;let ti=0,mist=0;P.answered=false;
    st.innerHTML=`<div class="step fx m2-sb5">${fxKindBar(f,n)}
     <div class="m2-wh"><h2 class="fx-h">${E(f.title||'Converse com o Poggie')} <small>${ri+1}/${N}</small></h2><span class="m2-stars">⭐ ${score}</span></div>
     <div class="m2-vpb"><span>🦫</span><p>${E(r.intro)}</p></div>
     <div class="tk-prog">${[...Array(T.length*2)].map(()=>'<i></i>').join('')}</div>
     <div class="tk-chat"></div><div class="tk-ops"></div><p class="tk-end"></p></div>`;
    const chat=st.querySelector('.tk-chat'),ops=st.querySelector('.tk-ops'),end=st.querySelector('.tk-end'),prog=[...st.querySelectorAll('.tk-prog i')];
    const bub=(who,en,pt,mic)=>{const b=document.createElement('div');b.className='tk-b '+(who?'r':'l')+' pop';b.style.setProperty('--c',who?'#6DDFDB':'#12B3A8');
      b.innerHTML=`<b class="nm">${who?'👤 Você':'🦫 Poggie'}</b>${E(en)}<small>${E(pt)}</small>`;
      b.onclick=()=>{sfx('pop');fxSay(en)};chat.appendChild(b);
      if(who&&mic&&window.PogVoice&&PogVoice.supported&&PogVoice.supported()){const m=document.createElement('button');m.type='button';m.className='tk-mic';m.textContent='🎤 Repetir em voz alta';
        m.onclick=(ev)=>{ev.stopPropagation();if(m.dataset.on)return;m.dataset.on='1';m.textContent='🎤 Ouvindo…';
          PogVoice.listen({lang:lang(),maxMs:8000,onInterim:()=>{},onDone:res=>{m.dataset.on='';const a=norm((res&&res.alts&&res.alts[0])||''),t=norm(en);
            if(!a.length){m.textContent='🎤 Não ouvi. Tentar de novo';return}
            const ok=t.filter(w=>a.indexOf(w)>=0).length/Math.max(1,t.length);
            m.textContent=ok>=.6?'✅ Muito bem!':'🔁 Quase! Tente de novo';if(ok>=.6){sfx('key')}}})};
        b.appendChild(m)}
      chat.scrollIntoView&&b.scrollIntoView({block:'nearest',behavior:'smooth'});return b};
    const turn=()=>{
      const t=T[ti];prog[ti*2].classList.add('on');
      bub(0,t.p[0],t.p[1]);fxSay(t.p[0]);
      const arr=t.o.map((o,i)=>({o,i}));arr.sort((a,b)=>hash(r.intro+ti+a.o[0])-hash(r.intro+ti+b.o[0]));
      ops.innerHTML=arr.map(x=>`<button type="button" class="tk-o" data-i="${x.i}">${E(x.o[0])}<small>${E(x.o[1])}</small></button>`).join('');
      cta('Responda o Poggie para continuar',false);
      ops.querySelectorAll('.tk-o').forEach(b=>b.onclick=()=>{
        if(P.answered||b.dataset.done)return;
        if(+b.dataset.i===t.a){
          ops.innerHTML='';prog[ti*2+1].classList.add('on');sfx('pop');
          bub(1,t.o[t.a][0],t.o[t.a][1],true);fxSay(t.o[t.a][0]);ti++;mist=0;
          if(ti<T.length)setTimeout(turn,1100);
          else{P.answered=true;if(!r.__m){score++;P.score++}
            st.querySelector('.m2-stars').textContent='⭐ '+score;end.textContent='🎉 Diálogo completo! Você conversou com o Poggie.';
            safe(()=>burst(chat));sfx('tada');cta(ri<N-1?'Próximo diálogo ▶':'Continuar',true,true)}
        }else{
          r.__m=true;mist++;b.classList.remove('bad');void b.offsetWidth;b.classList.add('bad');beep(false);
          if(mist>=2){const h=ops.querySelector(`.tk-o[data-i="${t.a}"]`);if(h)h.classList.add('hint')}
        }});
    };
    turn();
  };
  P.fx.cta=()=>{if(!P.answered)return true;if(ri<N-1){ri++;draw();return true}return false};
  draw();
  say(f.say||'Vamos conversar! Escolha a resposta certa para cada fala do Poggie.');
};

/* ---------- 3) Complete o diálogo com o Poggie (lacunas + peças) ---------- */
FX_KIND.tfill='practice';FX_LABEL.tfill='Monte o diálogo com o Poggie';
FXR.tfill=function(f,st,n){
  const R=f.rounds,N=R.length;let ri=0,score=0;
  const draw=()=>{
    const r=R[ri],L=r.lines;let li=0,mist=0;P.answered=false;const chosen={};
    st.innerHTML=`<div class="step fx m2-sb5">${fxKindBar(f,n)}
     <div class="m2-wh"><h2 class="fx-h">${E(f.title||'Monte o diálogo com o Poggie')} <small>${ri+1}/${N}</small></h2><span class="m2-stars">⭐ ${score}</span></div>
     <div class="m2-vpb"><span>🦫</span><p>${E(r.intro)} Complete as lacunas com as peças certas.</p></div>
     <div class="tk-prog">${L.map(()=>'<i></i>').join('')}</div>
     <div class="tk-chat"></div><p class="tk-end"></p></div>`;
    const chat=st.querySelector('.tk-chat'),end=st.querySelector('.tk-end'),prog=[...st.querySelectorAll('.tk-prog i')];
    const sub=(s)=>s.replace(/\{@(\d+)\}/g,(m,k)=>chosen[k]?chosen[k][s===undefined?0:0]:'…');
    const subL=(s,x)=>s.replace(/\{@(\d+)\}/g,(m,k)=>chosen[k]?chosen[k][x]:'…');
    const step=()=>{
      if(li>=L.length){P.answered=true;if(!r.__m){score++;P.score++}
        st.querySelector('.m2-stars').textContent='⭐ '+score;end.textContent='🎉 Diálogo completo! Você conversou do começo ao fim.';
        safe(()=>burst(chat));sfx('tada');cta(ri<N-1?'Próximo diálogo ▶':'Continuar',true,true);return}
      const l=L[li];prog[li].classList.add('on');
      if(l[0]==='p'){
        const en=subL(l[1],0),pt=subL(l[2],1);
        const b=document.createElement('div');b.className='tk-b l pop';b.style.setProperty('--c','#12B3A8');
        b.innerHTML=`<b class="nm">🦫 Poggie</b>${E(en)}<small>${E(pt)}</small>`;b.onclick=()=>{sfx('pop');fxSay(en)};chat.appendChild(b);
        fxSay(en);li++;setTimeout(step,900);return;
      }
      const bl=l[3],vals=bl.map(()=>null);mist=0;
      const b=document.createElement('div');b.className='tk-b r pop';b.style.setProperty('--c','#6DDFDB');
      const parts=l[1].split(/(\{\d+\})/);
      const lineHtml=()=>parts.map(p=>{const m=p.match(/^\{(\d+)\}$/);if(!m)return E(p);const k=+m[1];return vals[k]?`<u>${E(vals[k][0])}</u>`:'<span class="tk-gap">＿＿＿</span>'}).join('');
      const ptHtml=()=>l[2].replace(/\{(\d+)\}/g,(m,k)=>vals[+k]?vals[+k][1]:'…');
      const draw2=()=>{
        b.innerHTML=`<b class="nm">👤 Você</b><span class="tk-ln">${lineHtml()}</span><small class="tk-pt"></small><div class="tk-pieces">${bl.map((bk,k)=>vals[k]?'':`<div class="tk-pk" data-k="${k}">${bk[0].map((o,i)=>({o,i})).sort((a,b2)=>hash(l[1]+k+a.o[0])-hash(l[1]+k+b2.o[0])).map(x=>`<button type="button" class="tk-c" data-k="${k}" data-i="${x.i}">${E(x.o[0])}</button>`).join('')}</div>`).join('')}</div>`;
        b.querySelectorAll('.tk-c').forEach(c=>c.onclick=(ev)=>{ev.stopPropagation();
          const k=+c.dataset.k,i=+c.dataset.i;
          if(bl[k][1].indexOf(i)>=0){vals[k]=bl[k][0][i];sfx('pop');
            if(bl[0]&&vals.every(Boolean)){
              chosen[li]=vals[0];const en=l[1].replace(/\{(\d+)\}/g,(m,q)=>vals[+q][0]);
              b.innerHTML=`<b class="nm">👤 Você</b>${E(en)}<small>${E(ptHtml())}</small>`;
              b.onclick=()=>{sfx('pop');fxSay(en)};fxSay(en);
              if(window.PogVoice&&PogVoice.supported&&PogVoice.supported()){const m=document.createElement('button');m.type='button';m.className='tk-mic';m.textContent='🎤 Repetir em voz alta';
                m.onclick=(e2)=>{e2.stopPropagation();if(m.dataset.on)return;m.dataset.on='1';m.textContent='🎤 Ouvindo…';
                  PogVoice.listen({lang:lang(),maxMs:8000,onInterim:()=>{},onDone:res=>{m.dataset.on='';const a=norm((res&&res.alts&&res.alts[0])||''),t=norm(en);
                    if(!a.length){m.textContent='🎤 Não ouvi. Tentar de novo';return}
                    const ok=t.filter(w=>a.indexOf(w)>=0).length/Math.max(1,t.length);m.textContent=ok>=.6?'✅ Muito bem!':'🔁 Quase! Tente de novo';if(ok>=.6)sfx('key')}})};
                b.appendChild(m)}
              li++;setTimeout(step,1300);
            }else draw2();
          }else{r.__m=true;mist++;c.classList.add('bad');beep(false);setTimeout(()=>c.classList.remove('bad'),500);
            if(mist>=2){const h=b.querySelector(`.tk-c[data-k="${k}"][data-i="${bl[k][1][0]}"]`);if(h)h.classList.add('sw')}}
        });
      };
      chat.appendChild(b);draw2();cta('Complete a sua fala para continuar',false);
      b.scrollIntoView&&b.scrollIntoView({block:'nearest',behavior:'smooth'});
    };
    step();
  };
  P.fx.cta=()=>{if(!P.answered)return true;if(ri<N-1){ri++;draw();return true}return false};
  draw();
  say(f.say||'Monte a conversa com o Poggie: escolha as peças que completam cada fala sua.');
};


/* ---------- 4) Converse com o Poggie: diálogo de 10 falas, ouvindo e escolhendo ---------- */
FX_KIND.tdlg='practice';FX_LABEL.tdlg='Converse com o Poggie';
if(!document.getElementById('td-css')){const s=document.createElement('style');s.id='td-css';s.textContent=`
.td-coach{display:flex;gap:10px;align-items:flex-start;padding:10px 12px;border-radius:16px;background:color-mix(in srgb,#12B3A8 14%,transparent);border:2px solid #12B3A855;margin:6px 0}
.td-coach>span{font-size:2rem;line-height:1}.td-coach p{margin:0;font-size:.95rem}.td-coach label{display:inline-flex;align-items:center;gap:6px;margin-top:6px;font-size:.82rem;opacity:.85;cursor:pointer}
.td-dots{display:flex;gap:5px;margin:8px 0}.td-dots i{flex:1;height:6px;border-radius:4px;background:#8884}.td-dots i.on{background:#12B3A8}
.td-hist{display:flex;flex-direction:column;gap:6px;margin:6px 0;max-height:34vh;overflow:auto}
.td-h{display:flex;gap:6px;align-items:center;font-size:.86rem;padding:6px 10px;border-radius:12px;background:color-mix(in srgb,var(--c) 12%,transparent);max-width:92%}
.td-h.r{align-self:flex-end;background:color-mix(in srgb,var(--c) 18%,transparent)}.td-h small{display:block;opacity:.6}
.td-h button{border:0;background:transparent;color:inherit;cursor:pointer;font-size:1rem;padding:0 2px}
.td-now{display:flex;gap:12px;align-items:center;padding:14px;border-radius:18px;border:2px solid color-mix(in srgb,var(--c) 60%,transparent);background:color-mix(in srgb,var(--c) 10%,transparent);margin:10px 0}
.td-av{font-size:2rem}.td-play{flex:none;width:54px;height:54px;border-radius:50%;border:0;background:var(--c);color:#fff;font-size:1.4rem;cursor:pointer;box-shadow:0 3px 0 #0003}
.td-play.go{animation:tkpop .6s infinite}.td-tx{flex:1;min-width:0}.td-tx b{display:block;font-size:1.05rem;line-height:1.35}.td-tx small{display:block;opacity:.7;margin-top:4px}
.td-tx button{margin-top:6px;border:1px solid currentColor;background:transparent;color:inherit;border-radius:99px;font:inherit;font-size:.78rem;padding:2px 10px;cursor:pointer;opacity:.8}
.td-hide .td-tx b{filter:blur(7px);cursor:pointer}
.td-q{font-size:.85rem;opacity:.8;margin:8px 0 4px}
.td-ops{display:flex;flex-direction:column;gap:10px;margin:6px 0 14px}
.td-o{display:flex;gap:10px;align-items:center;padding:10px 12px;border-radius:14px;border:2px solid #7C4DFF55;background:transparent;color:inherit;font:inherit;text-align:left;cursor:pointer;width:100%}
.td-o i{font-style:normal;flex:none;width:26px;height:26px;border-radius:50%;background:#6DDFDB;color:#fff;display:grid;place-items:center;font-size:.8rem;font-weight:700}
.td-o span{flex:1}.td-o em{font-style:normal;flex:none;border:1px solid #8886;border-radius:99px;padding:3px 9px;font-size:.95rem}
.td-o.bad{border-color:#e5484d;animation:tkshake .4s}.td-o.hint{border-color:#12B3A8;box-shadow:0 0 0 3px #12B3A855}`;document.head.appendChild(s)}
FXR.tdlg=function(f,st,n){
  const T=f.turns,NT=T.length,npc=f.cast.npc,you=f.cast.you;let ti=0,mist=0,allClean=true,listenOnly=false;P.answered=false;
  st.innerHTML=`<div class="step fx m2-sb5">${fxKindBar(f,n)}
   <div class="m2-wh"><h2 class="fx-h">${E(f.title||'Converse com o Poggie')}</h2></div>
   <div class="td-coach"><span>🦫</span><div><p>${E(f.intro)}</p><label><input type="checkbox" id="tdlo"> 🎧 Só ouvir (esconder o texto de ${E(npc[2])})</label></div></div>
   <div class="td-dots">${T.map(()=>'<i></i>').join('')}</div>
   <div class="td-hist"></div><div class="td-slot"></div><p class="tk-end"></p></div>`;
  const hist=st.querySelector('.td-hist'),slot=st.querySelector('.td-slot'),end=st.querySelector('.tk-end'),dots=[...st.querySelectorAll('.td-dots i')];
  st.querySelector('#tdlo').onchange=e=>{listenOnly=e.target.checked;const w=slot.querySelector('.td-now');if(w)w.classList.toggle('td-hide',listenOnly)};
  const addH=(who,en,pt)=>{const c=who?you:npc;const d=document.createElement('div');d.className='td-h'+(who?' r':'');d.style.setProperty('--c',c[1]);
    d.innerHTML=`<span>${c[0]}</span><div>${E(en)}<small>${E(pt||'')}</small></div><button type="button" aria-label="Ouvir">🔊</button>`;
    d.querySelector('button').onclick=()=>{sfx('pop');fxSay(en)};hist.appendChild(d);hist.scrollTop=hist.scrollHeight};
  const turn=()=>{
    const t=T[ti];mist=0;dots[ti].classList.add('on');
    const arr=t.o.map((o,i)=>({o,i})).sort((a,b)=>hash(t.n[0]+a.o[0])-hash(t.n[0]+b.o[0]));
    slot.innerHTML=`<div class="td-now${listenOnly?' td-hide':''}" style="--c:${npc[1]}"><span class="td-av">${npc[0]}</span>
      <div class="td-tx"><b>${E(t.n[0])}</b><small class="td-ptx" hidden>${E(t.n[1])}</small><button type="button" class="td-pt">🇧🇷 Ver tradução</button></div>
      <button type="button" class="td-play go" aria-label="Ouvir ${E(npc[2])}">🔊</button></div>
      <p class="td-q">Fala ${ti*2+1} de ${NT*2} · Agora responda como <b>${E(you[2])}</b>:${t.q?` <b>${E(String(t.q).replace(/\*\*/g,''))}</b>`:''}</p>
      <div class="td-ops">${arr.map((x,k)=>`<div class="td-o" role="button" tabindex="0" data-i="${x.i}"><i>${'ABC'[k]}</i><span>${E(x.o[0])}</span><em data-s="1" title="Ouvir">🔊</em></div>`).join('')}</div>`;
    const now=slot.querySelector('.td-now');
    slot.querySelector('.td-play').onclick=()=>{sfx('pop');slot.querySelector('.td-play').classList.remove('go');fxSay(t.n[0])};
    slot.querySelector('.td-pt').onclick=(e)=>{const p=slot.querySelector('.td-ptx');p.hidden=!p.hidden;e.target.textContent=p.hidden?'🇧🇷 Ver tradução':'🇧🇷 Esconder tradução'};
    slot.querySelector('.td-tx b').onclick=()=>now.classList.remove('td-hide');
    setTimeout(()=>fxSay(t.n[0]),300);
    cta('Escolha a resposta para continuar',false);
    slot.querySelectorAll('.td-o').forEach(o=>{
      o.querySelector('em').onclick=(e)=>{e.stopPropagation();sfx('pop');fxSay(t.o[+o.dataset.i][0])};
      o.onclick=()=>{
        const i=+o.dataset.i;
        if(i===t.a){
          sfx('key');addH(0,t.n[0],t.n[1]);addH(1,t.o[i][0],t.o[i][1]);fxSay(t.o[i][0]);ti++;slot.innerHTML='';
          if(ti<NT)setTimeout(turn,1300);
          else{P.answered=true;if(allClean)P.score++;dots.forEach(d=>d.classList.add('on'));end.textContent='🎉 Conversa completa! Você falou com '+npc[2]+' do começo ao fim.';
            safe(()=>burst(hist));sfx('tada');cta('Continuar',true,true)}
        }else{
          allClean=false;mist++;o.classList.remove('bad');void o.offsetWidth;o.classList.add('bad');beep(false);
          if(mist===1)fxSay(t.n[0]);
          if(mist>=2){const h=slot.querySelector(`.td-o[data-i="${t.a}"]`);if(h)h.classList.add('hint')}
        }};
    });
  };
  P.fx.cta=()=>false;
  turn();
  say(f.say||'Conversa com áudio: ouça cada fala e escolha a melhor resposta.');
};


/* ---------- 5) "Sua vez" dinâmico: objetivos que acendem sozinhos + gabarito oculto + resposta do amigo ---------- */
if(!document.getElementById('tp-css')){const s=document.createElement('style');s.id='tp-css';s.textContent=`
.tp-bub{display:flex;gap:10px;align-items:flex-start;padding:10px 12px;border-radius:16px;background:color-mix(in srgb,#12B3A8 14%,transparent);border:2px solid #12B3A855;margin:8px 0}
.tp-bub.pop{animation:tkpop .45s}.tp-bub>span{font-size:1.8rem;line-height:1}.tp-bub p{margin:0;font-size:.95rem}
.rw-goals li.tp-g{display:block}.rw-goals li.tp-g.done{background:color-mix(in srgb,#12B3A8 20%,transparent);border-radius:12px;transition:background .4s}
.tp-key{display:none;margin:6px 0 4px 28px;padding:8px 10px;border-radius:12px;border:1px dashed #12B3A8aa}
.tp-reveal .tp-key{display:block;animation:tkpop .5s}.tp-key small{display:block;opacity:.7;margin-bottom:4px}
.tp-key div{display:flex;gap:8px;align-items:center;padding:3px 0}.tp-key div span{flex:1}.tp-key em{font-style:normal;display:block;opacity:.6;font-size:.82rem}
.tp-key button{border:0;background:transparent;color:inherit;cursor:pointer;font-size:1rem}
.tp-rep{display:flex;gap:10px;align-items:center;padding:12px;border-radius:16px;border:2px solid #FF6F59;background:color-mix(in srgb,#FF6F59 12%,transparent);margin:10px 0;animation:tkpop .5s}
.tp-rep>span{font-size:1.9rem}.tp-rep b{display:block}.tp-rep small{display:block;opacity:.7}.tp-rep button{margin-left:auto;border:0;background:#FF6F59;color:#fff;border-radius:50%;width:42px;height:42px;font-size:1.1rem;cursor:pointer}`;document.head.appendChild(s)}
const TP_STOP=new Set('a an the is are am be to of my your his her our their it its i me we you he she they in on at for and or with this that these those do does did please so very just would can could will may like get have'.split(' '));
function tpNorm(s){return String(s).toLowerCase().replace(/[’]/g,"'").replace(/\b(it|he|she|that|there|what|who|here|how)'s\b/g,'$1 is').replace(/\bi'm\b/g,'i am').replace(/\b(you|we|they)'re\b/g,'$1 are').replace(/n't\b/g,' not').replace(/'ll\b/g,' will').replace(/'ve\b/g,' have').replace(/'d\b/g,' would').replace(/[^a-z0-9$ ]/g,' ').split(/\s+/).filter(Boolean)}
function tpSame(a,b){return a===b||(a.length>=4&&b.length>=4&&a.slice(0,4)===b.slice(0,4)&&Math.abs(a.length-b.length)<=3)}
function tpScore(user,ans){const u=tpNorm(user),w=tpNorm(ans).filter(x=>!TP_STOP.has(x));if(!w.length)return u.join(' ')===tpNorm(ans).join(' ')?1:0;
  let hit=0;w.forEach(x=>{if(u.some(y=>tpSame(x,y)))hit++});return hit/w.length}
window.TPfuzzy=function(user,answers){return Math.max.apply(null,answers.map(a=>tpScore(user,a[0])))>=0.66};
const _prod=FXR.produce;
FXR.produce=function(f,st,n){
  _prod.apply(this,arguments);
  if(f.gp)try{dynProduce(f,st)}catch(e){console.warn('dynProduce',e)}
};
function dynProduce(f,st){
  const step=st.querySelector('.step'),ta=step&&step.querySelector('#fxta'),ul=step&&step.querySelector('.rw-goals');
  if(!ta||!ul||step.querySelector('.tp-bub'))return;
  const ch=step.querySelector('.fx-chips');if(ch){const l=ch.previousElementSibling;if(l&&l.classList.contains('rw-lab'))l.remove();ch.remove()}
  const sit=step.querySelector('.rw-sit');
  const bub=document.createElement('div');bub.className='tp-bub';bub.innerHTML='<span>🦫</span><p></p>';(sit||ta).after(bub);
  const say2=(m)=>{bub.querySelector('p').textContent=m;bub.classList.remove('pop');void bub.offsetWidth;bub.classList.add('pop')};
  const START='Escreva (ou fale) com as suas palavras. Cada objetivo fica verde sozinho quando você o cumpre!';
  say2(START);
  const lis=[...ul.children],done=new Set();let rep=null,revealed=false;
  const lb=step.querySelector('.rw-lab');if(lb&&/Objetivos/.test(lb.textContent))lb.textContent='Objetivos (ficam verdes sozinhos enquanto você escreve ou fala)';
  lis.forEach((li,i)=>{
    li.classList.remove('manual');li.classList.add('auto','tp-g');
    const key=document.createElement('div');key.className='tp-key';
    key.innerHTML='<small>✅ 3 jeitos de cumprir este objetivo:</small>'+(f.gp[i]||[]).map(p=>`<div><span>${E(p[0])}<em>${E(p[1])}</em></span><button type="button" aria-label="Ouvir">🔊</button></div>`).join('');
    key.querySelectorAll('button').forEach((b,k)=>b.onclick=()=>{sfx('pop');fxSay(f.gp[i][k][0])});
    li.appendChild(key);
  });
  const reveal=()=>{if(revealed)return;revealed=true;step.classList.add('tp-reveal')};
  const check=()=>{
    const v=ta.value;let newly=-1;
    lis.forEach((li,i)=>{const ok=window.TPfuzzy(v,f.gp[i]||[]);li.classList.toggle('done',ok);
      if(ok&&!done.has(i)){done.add(i);newly=i}else if(!ok&&done.has(i))done.delete(i)});
    const cnt=step.querySelector('#rwcnt');if(cnt)cnt.textContent=`${done.size}/${lis.length} objetivos`;
    if(newly>=0){sfx('key');say2((f.ok&&f.ok[newly])||'Muito bem!')}
    if(done.size===lis.length&&!rep){
      const r=f.reply,c=r[3]||'🧑';rep=document.createElement('div');rep.className='tp-rep';
      rep.innerHTML=`<span>${c}</span><div><small>${E(r[2]||'Seu amigo')} responde:</small><b>${E(r[0])}</b><small>${E(r[1])}</small></div><button type="button" aria-label="Ouvir">🔊</button>`;
      rep.querySelector('button').onclick=()=>{sfx('pop');fxSay(r[0])};ul.after(rep);
      reveal();say2('🏆 Todos os objetivos cumpridos! Veja outros jeitos de dizer e como a conversa continua.');setTimeout(()=>fxSay(r[0]),900);
    }else if(done.size<lis.length&&rep){rep.remove();rep=null;if(newly<0)say2(START)}
  };
  ta.addEventListener('input',check);
  const mb=step.querySelector('#fxm');if(mb)mb.addEventListener('click',reveal);
  check();
}
(function(){const o=window.fxTotal;window.fxTotal=function(e){let t=o.apply(this,arguments);try{(e.fr||[]).forEach(f=>{if(f.k==='tchat'||f.k==='tfill')t+=(f.rounds||[]).length})}catch(x){}return t}})();
})();
