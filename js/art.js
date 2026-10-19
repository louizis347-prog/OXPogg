/* Pogglot · Artigos em alemão (der / die / das): exercício por episódio com cores por gênero e dicas de terminações. */
(function(){
if(typeof FXR==='undefined'||typeof FX_KIND==='undefined')return;
FX_KIND.nbart='practice';FX_LABEL.nbart='Der · Die · Das';
const q=(s,r)=>(r||document).querySelector(s);
const H=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const say2=(t,slow)=>{try{fxSay(String(t),null,slow)}catch(e){}};
const COL={der:'#2F80ED',die:'#E5484D',das:'#2CB67D'};
const css=document.createElement('style');css.textContent=`
.ka{--g1:#2F80ED;--g2:#74B9FF;padding-bottom:12px}
.ka-st{display:flex;gap:6px;justify-content:center;margin:6px 0}.ka-st i{width:30px;height:8px;border-radius:6px;background:#dfe9f7}.ka-st i.on{background:linear-gradient(90deg,#2F80ED,#2CB67D)}
.ka-w{display:flex;flex-wrap:wrap;justify-content:center;align-items:baseline;gap:6px;margin:14px 0 6px;text-align:center}.ka-w .art{display:inline-block;min-width:64px;border-bottom:4px dashed #c9d3e6;color:transparent;font:900 34px system-ui}
.ka-w .art.show{border-color:transparent}.ka-w b{font:900 38px system-ui;color:#25203f;}.ka-w small{flex-basis:100%;display:block;font:600 15px system-ui;color:#6b6591;margin-top:2px}
.ka-opts{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:14px 0}.ka-opts button{border:0;border-radius:18px;min-height:64px;font:900 24px system-ui;color:#fff;box-shadow:0 8px 18px -10px rgba(0,0,0,.45)}
.ka-opts button[data-a=der]{background:#2F80ED}.ka-opts button[data-a=die]{background:#E5484D}.ka-opts button[data-a=das]{background:#2CB67D}
.ka-opts button.dim{opacity:.35}
.ka-fb{min-height:48px;text-align:center;font:800 15px/1.4 system-ui;color:#25203f}.ka-fb.ok{color:#1f9d5c}.ka-fb.no{color:#d9480f}
.ka-tip{margin:8px 0;padding:10px 12px;border-radius:14px;background:#F3F8FF;font:600 13.5px/1.4 system-ui;color:#3a4a6b;text-align:center}
.ka-leg{display:flex;gap:8px;justify-content:center;margin-top:8px;font:800 12px system-ui}.ka-leg span{white-space:nowrap;padding:4px 8px;border-radius:999px;color:#fff}
`;document.head.appendChild(css);
const RULES=[[/(ung|heit|keit|schaft|tion|ität|ie|ik|ur|ei)$/i,'die','Terminações como -ung, -heit, -keit, -schaft, -tion, -ität, -ie, -ik, -ei geralmente são “die”.'],
 [/(chen|lein|ment|um)$/i,'das','Terminações -chen e -lein (diminutivos), -ment e -um geralmente são “das”.'],
 [/(ling|ismus|ant|ist)$/i,'der','Terminações -ling, -ismus, -ant e -ist geralmente são “der”.'],
 [/^(Montag|Dienstag|Mittwoch|Donnerstag|Freitag|Samstag|Sonntag|Januar|Februar|März|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember|Morgen|Abend|Frühling|Sommer|Herbst|Winter)$/,'der','Dias da semana, meses e estações do ano são sempre “der”.']];
const tipFor=(noun,art)=>{for(const r of RULES)if(r[0].test(noun)&&r[1]===art)return r[2];return /e$/.test(noun)&&art==='die'?'Substantivos terminados em -e costumam ser “die”.':''};
FXR.nbart=function(f,st,n){
  const base=f.items||[];let queue=base.map(x=>x.slice()),i=0,hits=0,retried=false,wrong=[];P.fx.done=false;P.fx.cta=()=>!P.fx.done;
  const render=()=>{const it=queue[i],total=queue.length;
    st.innerHTML=`<div class="step fx nbx ka">${fxKindBar(f,n)}<h2 class="fx-h">${H(f.title||'Der · Die · Das')}</h2>
    <div class="ka-st">${queue.map((_,k)=>`<i class="${k<i?'on':''}"></i>`).join('')}</div>
    <div class="ka-w"><span class="art" id="kaa">${H(it[0])}</span><b>${H(it[1])}</b><small>${H(it[2])}</small></div>
    <div class="ka-opts">${['der','die','das'].map(a=>`<button data-a="${a}">${a}</button>`).join('')}</div>
    <div class="ka-fb" id="kafb">Escolha o artigo certo. Memorize sempre junto com a palavra.</div><div id="kat"></div>
    <div class="ka-leg"><span style="background:#2F80ED">der · masc.</span><span style="background:#E5484D">die · fem.</span><span style="background:#2CB67D">das · neutro</span></div></div>`;
    let lk=false;const fb=q('#kafb',st);
    st.querySelectorAll('.ka-opts button').forEach(b=>b.onclick=()=>{if(lk)return;const a=b.dataset.a;
      if(a===it[0]){lk=true;hits++;const e=q('#kaa',st);e.classList.add('show');e.style.color=COL[a];try{sfx('burst')}catch(e2){}fb.className='ka-fb ok';fb.textContent='Certo! '+it[0]+' '+it[1];
        const tp=tipFor(it[1],a);if(tp)q('#kat',st).innerHTML=`<div class="ka-tip">💡 ${H(tp)}</div>`;say2(it[0]+' '+it[1]);cta(i<queue.length-1?'Próxima ▶':'Concluir',true,true);P.fx.cta=()=>{next();return true}}
      else{b.classList.add('dim');b.disabled=true;if(!wrong.includes(it))wrong.push(it);try{sfx('oops')}catch(e2){}fb.className='ka-fb no';fb.textContent='Ainda não. Tente outro artigo.'}});
    cta('Escolha o artigo',false);P.fx.cta=()=>!P.fx.done;
    say(i===0?'Qual é o artigo? der, die ou das?':'Próxima palavra.')};
  const next=()=>{i++;if(i<queue.length)return render();
    if(!retried&&wrong.length){retried=true;queue=queue.concat(wrong.map(x=>x.slice()));wrong=[];return render()}
    finish()};
  const finish=()=>{P.fx.done=true;P.score++;try{sfx('tada');confetti(60)}catch(e){}
    st.innerHTML=`<div class="step fx nbx ka">${fxKindBar(f,n)}<h2 class="fx-h">${H(f.title||'Der · Die · Das')}</h2><div class="ka-tip"><b>Artigos treinados!</b><br>${base.map(x=>`<span style="color:${COL[x[0]]};font-weight:900">${H(x[0])}</span> ${H(x[1])}`).join(' · ')}</div><div class="ka-tip">Dica: escreva sempre o artigo junto com o substantivo no seu caderno. Assim você memoriza o gênero junto com a palavra.</div></div>`;
    cta('Continuar',true,true);P.fx.cta=null};
  render()};
})();
