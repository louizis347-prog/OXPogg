/* Pogglot · Acentos e ortografia (espanhol, francês, italiano, português): ouça a palavra e escolha a grafia correta
   (acentos, ñ, ç, tremas), com dica de regra depois de cada resposta. */
(function(){
if(typeof FXR==='undefined'||typeof FX_KIND==='undefined')return;
FX_KIND.nbacc='practice';FX_LABEL.nbacc='Acentos';
const q=(s,r)=>(r||document).querySelector(s);
const H=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const say2=(t,slow)=>{try{fxSay(String(t),null,slow)}catch(e){}};
const shuf=a=>a.slice().sort(()=>Math.random()-.5);
const css=document.createElement('style');css.textContent=`
.kc{--g1:#E67E22;--g2:#F6C26B;padding-bottom:12px}
.kc-st{display:flex;gap:6px;justify-content:center;margin:6px 0}.kc-st i{width:30px;height:8px;border-radius:6px;background:#f3e6d6}.kc-st i.on{background:linear-gradient(90deg,#E67E22,#F6C26B)}
.kc-w{text-align:center;margin:12px 0 4px}.kc-w b{display:block;font:900 36px system-ui;color:#23383C;letter-spacing:.01em}.kc-w small{display:block;font:600 15px system-ui;color:#68848E;margin-top:2px}
.kc-hint{text-align:center;font:700 13px system-ui;color:#8a6a3a;margin:2px 0 6px}
.kc-tools{display:flex;gap:8px;justify-content:center;margin:8px 0}
.kc-opts{display:grid;gap:10px;margin:10px 0}.kc-opts button{border:0;border-radius:18px;background:#fff;box-shadow:0 6px 16px rgba(37,77,83,.12);min-height:58px;padding:10px;font:900 26px system-ui;color:#23383C}
.kc-opts button.ok{background:#d9f8e5;outline:3px solid #2cc673}.kc-opts button.no{background:#ffe0e0;outline:3px solid #ff6b6b;opacity:.8}
.kc-fb{min-height:44px;text-align:center;font:800 15px/1.4 system-ui;color:#23383C}.kc-fb.ok{color:#1f9d5c}.kc-fb.no{color:#d9480f}
.kc-tip{margin:8px 0;padding:10px 12px;border-radius:14px;background:#FFF6EA;font:600 13.5px/1.4 system-ui;color:#6b4a1d;text-align:center}
html[data-theme="dark"] .kc-opts button{background:#1C373B;color:#EDFCFB}html[data-theme="dark"] .kc-w b{color:#EDFCFB}
`;document.head.appendChild(css);
FXR.nbacc=function(f,st,n){
  const items=f.items||[];let i=0,hits=0;P.fx.done=false;P.fx.cta=()=>!P.fx.done;
  const render=()=>{const it=items[i],opts=shuf([it.w].concat(it.alts));
    st.innerHTML=`<div class="step fx nbx kc">${fxKindBar(f,n)}<h2 class="fx-h">${H(f.title||'Acentos e ortografia')}</h2>
    <div class="kc-st">${items.map((_,k)=>`<i class="${k<i?'on':''}"></i>`).join('')}</div>
    <div class="kc-w"><b>${H(it.s)}</b><small>${H(it.pt)}</small></div><div class="kc-hint">Qual é a grafia correta?</div>
    <div class="kc-tools" style="justify-content:center"><button class="nb-chip" id="kcs">🔊 Ouvir</button><button class="nb-chip" id="kcsl">🐢 Devagar</button></div>
    <div class="kc-opts">${opts.map(o=>`<button data-o="${H(o)}">${H(o)}</button>`).join('')}</div>
    <div class="kc-fb" id="kcfb"></div><div id="kct"></div></div>`;
    q('#kcs',st).onclick=()=>say2(it.w);q('#kcsl',st).onclick=()=>say2(it.w,true);
    let lk=false;const fb=q('#kcfb',st);
    st.querySelectorAll('.kc-opts button').forEach(b=>b.onclick=()=>{if(lk)return;
      if(b.dataset.o===it.w){lk=true;hits++;b.classList.add('ok');try{sfx('burst')}catch(e){}fb.className='kc-fb ok';fb.textContent='Certo!';if(it.tip)q('#kct',st).innerHTML=`<div class="kc-tip">💡 ${H(it.tip)}</div>`;say2(it.w);cta(i<items.length-1?'Próxima ▶':'Concluir',true,true);P.fx.cta=()=>{i++;if(i<items.length)render();else finish();return true}}
      else{b.classList.add('no');b.disabled=true;try{sfx('oops')}catch(e){}fb.className='kc-fb no';fb.textContent='Ainda não. Ouça de novo e tente outra grafia.'}});
    cta('Escolha a grafia',false);P.fx.cta=()=>!P.fx.done;setTimeout(()=>say2(it.w),350);
    say(i===0?'Ouça a palavra e escolha a grafia correta.':'Próxima palavra.')};
  const finish=()=>{P.fx.done=true;P.score++;try{sfx('tada');confetti(60)}catch(e){}
    st.innerHTML=`<div class="step fx nbx kc">${fxKindBar(f,n)}<h2 class="fx-h">${H(f.title||'Acentos e ortografia')}</h2><div class="kc-tip"><b>Palavras revisadas:</b><br>${items.map(x=>H(x.w)).join(' · ')}</div><div class="kc-tip">Dica: o acento faz parte da palavra. Escreva sempre com ele, como em ${H(items[0].w)}.</div></div>`;
    cta('Continuar',true,true);P.fx.cta=null};
  render()};
})();
