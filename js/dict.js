/* Pogglot · Ditado (cursos com alfabeto latino): ouvir a frase e escrever. Compara palavra por palavra, avisa quando só os acentos
   falham e oferece teclas de acento no celular. Estatísticas em localStorage (pogglot:dict). */
(function(){
if(typeof FXR==='undefined'||typeof FX_KIND==='undefined')return;
FX_KIND.nbdict='practice';FX_LABEL.nbdict='Ditado';
const q=(s,r)=>(r||document).querySelector(s);
const H=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const say2=(t,slow)=>{try{fxSay(String(t),null,slow)}catch(e){}};
const store=(k,v)=>{try{if(v===undefined)return JSON.parse(localStorage.getItem('pogglot:'+k)||'null');localStorage.setItem('pogglot:'+k,JSON.stringify(v))}catch(e){return null}};
const KEYS={es:'á é í ó ú ñ ü ¿ ¡',fr:'é è ê à â ç ô î û ù ë ï œ',de:'ä ö ü ß',it:'à è é ì ò ù',pt:'á à â ã é ê í ó ô õ ú ç',en:''};
const css=document.createElement('style');css.textContent=`
.kd{--g1:#0984E3;--g2:#74B9FF;padding-bottom:12px}
.kd-st{display:flex;gap:6px;justify-content:center;margin:6px 0}.kd-st i{width:34px;height:8px;border-radius:6px;background:#dfe9f7}.kd-st i.on{background:linear-gradient(90deg,var(--g1),var(--g2))}
.kd-tools{display:flex;gap:8px;justify-content:center;margin:10px 0}
.kd-pt{text-align:center;font:600 14px system-ui;color:#586D75;margin:4px 0}
.kd-in{width:100%;box-sizing:border-box;min-height:96px;border-radius:18px;border:2px solid #dbe6f7;background:#fff;padding:12px 14px;font:700 20px/1.35 system-ui;color:#23383C;resize:none}
.kd-in:focus{outline:none;border-color:#0984E3}
.kd-keys{display:flex;flex-wrap:wrap;gap:6px;justify-content:center;margin:8px 0}.kd-keys button{min-width:44px;min-height:44px;border:0;border-radius:12px;background:#EAF3FF;color:#0b5cad;font:800 20px system-ui}
.kd-fb{min-height:44px;margin:8px 0;text-align:center;font:800 15px/1.4 system-ui;color:#23383C}
.kd-fb.ok{color:#1f9d5c}.kd-fb.no{color:#d9480f}
.kd-ans{margin:8px 0;padding:12px;border-radius:16px;background:#F3F8FF;font:700 18px/1.7 system-ui;color:#23383C;text-align:center}
.kd-ans .w{display:inline-block;margin:0 3px;padding:0 4px;border-radius:6px}.kd-ans .g{background:#D9F8E5}.kd-ans .b{background:#FFE0E0}.kd-ans .a{background:#FFF1C9}
.kd-ans small{display:block;font:600 13px system-ui;color:#68848E}
.kd-stars{font-size:24px;letter-spacing:4px;color:#f5a524}
html[data-theme="dark"] .kd-in{background:#1C373B;border-color:#2D545A;color:#EDFCFB}
html[data-theme="dark"] .kd-ans{background:#1C373B;color:#EDFCFB}
`;document.head.appendChild(css);
const strip=s=>s.normalize('NFD').replace(/[̀-ͯ]/g,'');
const norm=s=>String(s).replace(/[’‘`´]/g,"'").replace(/[“”«»]/g,'"').replace(/[.,;:!?¿¡"()…—–-]/g,' ').replace(/\s+/g,' ').trim().toLowerCase();
const toks=s=>norm(s).split(' ').filter(Boolean);
function lcs(a,b,eq){const m=a.length,n=b.length,t=Array.from({length:m+1},()=>new Array(n+1).fill(0));
  for(let i=m-1;i>=0;i--)for(let j=n-1;j>=0;j--)t[i][j]=eq(a[i],b[j])?t[i+1][j+1]+1:Math.max(t[i+1][j],t[i][j+1]);
  const pairs=[];let i=0,j=0;while(i<m&&j<n){if(eq(a[i],b[j])){pairs.push([i,j]);i++;j++}else if(t[i+1][j]>=t[i][j+1])i++;else j++}return pairs}
function check(user,target){
  const U=toks(user),T=toks(target);
  if(!U.length)return{stars:0,exact:false,marks:T.map(w=>({w,k:'b'})),acc:0};
  if(U.join(' ')===T.join(' '))return{stars:3,exact:true,marks:T.map(w=>({w,k:'g'})),acc:1};
  if(U.map(strip).join(' ')===T.map(strip).join(' '))return{stars:2,exact:false,accentOnly:true,marks:T.map((w,i)=>({w,k:U[i]===w?'g':'a'})),acc:.95};
  const pr=lcs(U,T,(a,b)=>strip(a)===strip(b)),hit=new Map(pr.map(p=>[p[1],p[0]]));
  const marks=T.map((w,j)=>hit.has(j)?{w,k:U[hit.get(j)]===w?'g':'a'}:{w,k:'b'});
  const acc=pr.length/Math.max(T.length,U.length);
  return{stars:acc>=.85?2:acc>=.5?1:0,exact:false,marks,acc}}
const langOf=()=>{const t=(P&&P.c&&P.c.tts)||'en-US';return t.slice(0,2)};
FXR.nbdict=function(f,st,n){
  const items=f.items||[];let i=0,tries=0,perfect=0;P.fx.done=false;P.fx.cta=()=>!P.fx.done;
  const render=()=>{
    const it=items[i],lg=langOf(),keys=(KEYS[lg]||'').split(' ').filter(Boolean);tries=0;
    st.innerHTML=`<div class="step fx nbx kd" style="--g1:${(f.g||['#0984E3','#74B9FF'])[0]};--g2:${(f.g||['#0984E3','#74B9FF'])[1]}">${fxKindBar(f,n)}<h2 class="fx-h">${H(f.title||'Ditado')}</h2>
    <div class="kd-st">${items.map((_,k)=>`<i class="${k<i?'on':''}"></i>`).join('')}</div>
    <div class="kd-pt">Ouça e escreva o que ouviu (frase ${i+1} de ${items.length}).</div>
    <div class="kd-tools"><button class="nb-chip" id="kds">🔊 Ouvir</button><button class="nb-chip" id="kdsl">🐢 Devagar</button><button class="nb-chip" id="kdh">💡 Dica</button></div>
    <textarea class="kd-in" id="kdi" rows="3" autocomplete="off" autocapitalize="off" autocorrect="off" spellcheck="false" placeholder="Escreva aqui…"></textarea>
    ${keys.length?`<div class="kd-keys">${keys.map(k=>`<button type="button" data-k="${H(k)}">${H(k)}</button>`).join('')}</div>`:''}
    <div class="kd-fb" id="kdfb"></div><div id="kdans"></div></div>`;
    const inp=q('#kdi',st),fb=q('#kdfb',st);
    q('#kds',st).onclick=()=>say2(it.t);q('#kdsl',st).onclick=()=>say2(it.t,true);
    q('#kdh',st).onclick=()=>{fb.className='kd-fb';fb.textContent='Dica: '+it.t.split(/\s+/).map(w=>w.replace(/[^\p{L}\p{N}'’]/gu,'').slice(0,1)+'…').join('  ')};
    st.querySelectorAll('.kd-keys button').forEach(b=>b.onclick=()=>{const s=inp.selectionStart||inp.value.length,e=inp.selectionEnd||s;inp.value=inp.value.slice(0,s)+b.dataset.k+inp.value.slice(e);inp.focus();inp.selectionStart=inp.selectionEnd=s+b.dataset.k.length;cta('Verificar',true,true)});
    inp.oninput=()=>cta('Verificar',inp.value.trim().length>0,inp.value.trim().length>0);
    P.fx.cta=()=>{if(P.fx.done)return false;return verify()};cta('Escreva o que ouviu',false);
    setTimeout(()=>say2(it.t),400);say('Ouça a frase e escreva. Use os botões de acento se precisar.')};
  let revealed=false;
  const verify=()=>{
    if(revealed){revealed=false;i++;if(i>=items.length)finish();else render();return true}
    const it=items[i],inp=q('#kdi',st),fb=q('#kdfb',st),r=check(inp.value,it.t);tries++;
    if(r.exact||tries>=2){
      revealed=true;inp.disabled=true;if(r.stars===3)perfect++;
      const dd=store('dict')||{total:0,perfect:0};dd.total++;if(r.stars===3)dd.perfect++;store('dict',dd);
      try{sfx(r.stars>0?'burst':'oops')}catch(e){}
      fb.className='kd-fb '+(r.stars>=2?'ok':'no');
      fb.innerHTML=`<div class="kd-stars">${'★'.repeat(r.stars)}${'☆'.repeat(3-r.stars)}</div>`+(r.exact?'Perfeito!':r.accentOnly?'Quase! Só os acentos ou letras especiais falharam.':r.stars>=1?'Bom! Veja a frase correta:':'Veja a frase correta e ouça de novo:');
      q('#kdans',st).innerHTML=`<div class="kd-ans">${r.marks.map(m=>`<span class="w ${m.k}">${H(m.w)}</span>`).join(' ')}<small>${H(it.pt||'')}</small></div>`;
      say2(it.t);cta(i<items.length-1?'Próxima frase ▶':'Concluir',true,true);return true}
    fb.className='kd-fb no';const wrong=r.marks.filter(m=>m.k==='b').length;
    fb.textContent=r.accentOnly?'Quase! Confira os acentos e as letras especiais.':wrong?`${wrong} palavra(s) não bateram. Ouça de novo (🐢 Devagar) e corrija.`:'Confira as palavras e os acentos.';
    cta('Verificar de novo',true,true);return true};
  const finish=()=>{P.fx.done=true;P.score++;try{sfx('tada');confetti(60)}catch(e){}
    st.innerHTML=`<div class="step fx nbx kd">${fxKindBar(f,n)}<h2 class="fx-h">${H(f.title||'Ditado')}</h2><div class="kd-ans"><b>${perfect}/${items.length} frases perfeitas</b><small>Ouvir e escrever treina ouvido, ortografia e acentos ao mesmo tempo.</small></div></div>`;
    cta('Continuar',true,true);P.fx.cta=null};
  render()};
})();
