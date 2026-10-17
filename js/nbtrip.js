/* Neighbors — abertura das revisões: "Passaporte do arco" (carimbe cada parada) */
(function(){
if(typeof FXR==='undefined'||typeof FX_KIND==='undefined')return;
FX_KIND.nbtrip='practice';FX_LABEL.nbtrip='Passaporte do arco';
const q=(s,r)=>(r||document).querySelector(s);
const H=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const say2=(t,who,slow)=>{try{fxSay(String(t),who,slow)}catch(e){}};
const av=(em,nm,col)=>{try{return window.PogFace?PogFace.avatar(em,nm,col):em}catch(e){return em}};
const css=document.createElement('style');css.textContent=`
.nbt-top{display:flex;gap:10px;align-items:center;background:#fff;border-radius:22px;padding:12px 14px;margin:8px 0;box-shadow:0 8px 22px rgba(40,30,90,.12)}
.nbt-top .pg{flex:none;width:44px;height:44px;border-radius:50%;display:grid;place-items:center;font-size:24px;background:linear-gradient(135deg,var(--g1),var(--g2))}
.nbt-top p{margin:0;font-weight:700;font-size:14.5px;line-height:1.35;color:#25203f}
.nbt-bar{height:10px;border-radius:99px;background:#e6e1fa;overflow:hidden;margin:10px 2px 4px}.nbt-bar i{display:block;height:100%;width:0;border-radius:99px;background:linear-gradient(90deg,#ffb703,#ff7aa8);transition:width .5s}
.nbt-cnt{text-align:right;font:800 12px system-ui;opacity:.65;margin:0 4px 6px}
.nbt-path{list-style:none;margin:6px 0 0;padding:0 0 0 22px;position:relative}
.nbt-path:before{content:"";position:absolute;left:11px;top:14px;bottom:30px;border-left:3px dashed #c9c1f0}
.nbt-st{position:relative;margin:0 0 14px}
.nbt-pin{position:absolute;left:-22px;top:18px;width:24px;height:24px;border-radius:50%;background:#fff;border:3px solid #c9c1f0;display:grid;place-items:center;font:900 11px system-ui;color:#5b4fc9;z-index:1;transition:.3s}
.nbt-st.on .nbt-pin{background:#2fb87a;border-color:#2fb87a;color:#fff;transform:scale(1.15)}
.nbt-card{display:block;width:100%;text-align:left;border:0;padding:0;border-radius:24px;background:#fff;box-shadow:0 8px 22px rgba(40,30,90,.12);overflow:hidden;cursor:pointer;color:#25203f;font-family:system-ui}
.nbt-ph{position:relative;height:84px;overflow:hidden;background:linear-gradient(135deg,var(--g1),var(--g2))}
.nbt-ph svg{position:absolute;inset:0;width:100%;height:100%}
.nbt-ph:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 35%,rgba(10,8,30,.62))}
.nbt-ph .ct{position:absolute;left:14px;bottom:8px;z-index:1;color:#fff;font:900 17px/1.1 system-ui;text-shadow:0 2px 8px rgba(0,0,0,.4)}
.nbt-ph .ct small{display:block;font:700 11.5px system-ui;opacity:.9;margin-top:2px}
.nbt-ph .fa{position:absolute;right:12px;bottom:-14px;z-index:2;width:52px;height:52px;border-radius:50%;background:#fff;display:grid;place-items:center;font-size:30px;box-shadow:0 5px 14px rgba(0,0,0,.28);overflow:hidden}
.nbt-bd{padding:12px 14px 14px}
.nbt-q{font:800 16px/1.3 system-ui;margin:0 56px 4px 0}
.nbt-q b{font-size:14px;margin-right:4px}
.nbt-tr{font:600 12.5px/1.35 system-ui;opacity:.75;display:none}
.nbt-st.on .nbt-tr{display:block}
.nbt-w{display:flex;gap:6px;flex-wrap:wrap;margin-top:8px}
.nbt-w span{background:#f1eeff;border-radius:99px;padding:5px 10px;font:800 12.5px system-ui;color:#4a3fb0}
.nbt-w span em{font-style:normal;opacity:.6;font-weight:700;margin-left:3px}
.nbt-tap{font:800 11px system-ui;letter-spacing:.06em;color:#7a4a00;background:#fff1d6;border-radius:99px;padding:4px 10px;display:inline-block;margin-top:8px}
.nbt-st.on .nbt-tap{display:none}
.nbt-stamp{position:absolute;right:12px;top:14px;z-index:3;width:60px;height:60px;border-radius:50%;border:3px solid #e24b5a;color:#e24b5a;display:grid;place-items:center;font:900 9px/1.1 system-ui;letter-spacing:.06em;text-align:center;transform:rotate(-16deg) scale(2);opacity:0;pointer-events:none;background:rgba(255,255,255,.88)}
.nbt-st.on .nbt-stamp{animation:nbtst .45s cubic-bezier(.2,1.4,.4,1) forwards}
@keyframes nbtst{to{opacity:1;transform:rotate(-16deg) scale(1)}}
`;document.head.appendChild(css);
const theme=f=>`style="--g1:${(f.g||['#6C5CE7','#FF7AA8'])[0]};--g2:${(f.g||['#6C5CE7','#FF7AA8'])[1]}"`;
FXR.nbtrip=function(f,st,n){
  const S=f.stops||[];const seen=new Set();
  const cover=s=>{try{if(window.PogCover&&PogCover.svg)return PogCover.svg({n:s.num,t:s.t,sc:s.sc,fr:[{k:'nbhero',face:s.fc,name:s.nm,city:s.c,num:s.num}]})}catch(e){}return ''};
  st.innerHTML=`<div class="step fx nbx" ${theme(f)}>${fxKindBar(f,n)}<h2 class="fx-h">${H(f.title||'Passaporte do arco')}</h2>
  <div class="nbt-top"><span class="pg">🧭</span><p>${H(f.intro||'Visite cada parada: toque no cartão para ouvir a frase e carimbar seu passaporte.')}</p></div>
  <div class="nbt-bar"><i id="nbtb"></i></div><div class="nbt-cnt" id="nbtc"></div>
  <ol class="nbt-path">${S.map((s,i)=>`<li class="nbt-st" data-i="${i}"><span class="nbt-pin">${i+1}</span><button class="nbt-card" type="button"><div class="nbt-ph">${cover(s)}<div class="ct">${H(s.c)}<small>${H(s.t)}</small></div><span class="fa">${av(s.fc,s.nm,'#8F5400')}</span></div><div class="nbt-bd"><p class="nbt-q"><b>🔊</b>${H(s.ln[0])}</p><div class="nbt-tr">${H(s.ln[1])}</div><div class="nbt-w">${(s.w||[]).map((w,j)=>`<span data-j="${j}">${H(w[0])}<em>${H(w[1])}</em></span>`).join('')}</div><span class="nbt-tap">TOQUE PARA CARIMBAR</span></div></button><span class="nbt-stamp">VISITADO<br>✓</span></li>`).join('')}</ol></div>`;
  const upd=()=>{q('#nbtb',st).style.width=Math.round(seen.size/S.length*100)+'%';q('#nbtc',st).textContent=seen.size+' de '+S.length+' paradas';};
  upd();
  P.fx.done=false;P.fx.cta=()=>!P.fx.done;cta('Visite as paradas',false);
  st.querySelectorAll('.nbt-st').forEach(li=>{const i=+li.dataset.i,s=S[i];
    li.querySelector('.nbt-card').onclick=e=>{
      const wd=e.target.closest&&e.target.closest('.nbt-w span');
      if(wd){say2(s.w[+wd.dataset.j][0],s.nm);return}
      say2(s.ln[0],s.nm);
      if(!seen.has(i)){seen.add(i);li.classList.add('on');try{sfx('burst')}catch(x){}upd();
        if(seen.size>=S.length){P.fx.done=true;P.score++;try{sfx('tada');confetti(60)}catch(x){}cta('Continuar',true,true)}}};
  });
  say('Vamos passear pelos lugares que você já conhece!')};
})();
