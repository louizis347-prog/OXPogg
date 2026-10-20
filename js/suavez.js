/* Pogglot · "Sua vez" v2: camada final sobre o motor existente (rework/m2/talk/ai).
   Mantém correção por IA, voz, estrelas, XP e resposta do personagem; só reorganiza a embalagem
   numa cena de chat compacta: missão, objetivos em pílulas, dica sob demanda, caixa de resposta. */
(function(){
'use strict';
if(typeof FXR==='undefined'||typeof FXR.produce!=='function')return;
const prev=FXR.produce;
const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const cap=s=>s?s.charAt(0).toUpperCase()+s.slice(1):s;

FXR.produce=function(f,st,n){
  prev.apply(this,arguments);
  try{reskin(f,st)}catch(e){console.warn('suavez',e)}
};

/* "Cumprimente, pergunte como vai e diga que é a sua primeira vez." -> 3 rótulos curtos */
function labels(f,count){
  const bold=(String(f.prompt||'').match(/\*\*(.+?)\*\*/)||[])[1]||'';
  const parts=bold.replace(/[.!?]+$/,'').split(/,\s*|\s+e\s+(?=[a-zà-ú])/i).map(s=>s.trim()).filter(Boolean);
  if(parts.length===count)return parts.map(cap);
  return (f.check||[]).map(c=>cap(String(c).replace(/\?+$/,'')));
}

function reskin(f,st){
  const step=st.querySelector('.step');
  if(!step||step.classList.contains('sv2')||!step.querySelector('#fxta'))return;
  step.classList.add('sv2');
  const ta=step.querySelector('#fxta'),ul=step.querySelector('.rw-goals');

  /* personagem da missão */
  const ic=step.querySelector('.rw-sit-ic');
  if(ic&&f.reply&&f.reply[3])ic.textContent=f.reply[3];

  /* objetivos: rótulos curtos no imperativo */
  if(ul){
    const labs=labels(f,ul.children.length);
    [...ul.children].forEach((li,i)=>{
      const t=[...li.children].find(c=>c.tagName==='SPAN'&&!c.classList.contains('rw-box'));
      if(t&&labs[i])t.textContent=labs[i];
    });
  }

  /* convite curto no lugar do texto longo do Poggie */
  /* a bolha do Poggie só aparece quando há reação (objetivo cumprido), sem texto de convite longo */
  const bubBox=step.querySelector('.tp-bub'),bub=bubBox&&bubBox.querySelector('p');
  if(bub){
    bub.textContent='';bubBox.classList.add('idle');
    new MutationObserver(()=>{if(bub.textContent.trim())bubBox.classList.remove('idle')}).observe(bub,{childList:true,characterData:true,subtree:true});
  }

  ta.rows=2;
  if(!f.ph)ta.placeholder='Responda como numa conversa…';

  /* ajuda sob demanda: 3 jeitos de dizer o próximo objetivo */
  const bar=step.querySelector('.rw-bar');
  const hints=f.gp||f.tips;
  if(hints&&ul&&bar){
    const help=document.createElement('button');
    help.type='button';help.className='pill light sv-help';help.textContent='💡 Ajuda';
    bar.prepend(help);
    const panel=document.createElement('div');panel.className='sv-hint';panel.hidden=true;
    ta.before(panel);
    const next=()=>[...ul.children].findIndex(li=>!li.classList.contains('done'));
    const draw=()=>{
      const i=next();
      if(i<0){panel.hidden=true;help.hidden=true;return}
      const labs=[...ul.children].map(li=>li.textContent.replace(/\s+/g,' ').trim());
      panel.innerHTML=`<small>3 jeitos de dizer: <b>${esc(ul.children[i].dataset.lab||'')}</b></small>`
        +(hints[i]||[]).map((p,k)=>`<div class="sv-way"><button type="button" class="sv-use" data-i="${i}" data-k="${k}"><span>${esc(p[0])}</span><em>${esc(p[1])}</em></button><button type="button" class="sv-hear" data-i="${i}" data-k="${k}" aria-label="Ouvir">🔊</button></div>`).join('');
    };
    [...ul.children].forEach(li=>{li.dataset.lab=li.querySelector('span:not(.rw-box)')?li.querySelector('span:not(.rw-box)').textContent:''});
    help.onclick=()=>{
      if(panel.hidden){draw();panel.hidden=false;help.textContent='Esconder ajuda'}
      else{panel.hidden=true;help.textContent='💡 Ajuda'}
      try{sfx('pop')}catch(e){}
    };
    panel.onclick=e=>{
      const hear=e.target.closest('.sv-hear'),use=e.target.closest('.sv-use');
      if(hear){try{sfx('pop');fxSay(hints[+hear.dataset.i][+hear.dataset.k][0])}catch(x){}return}
      if(use){const t=hints[+use.dataset.i][+use.dataset.k][0];
        ta.value+=(ta.value&&!/\s$/.test(ta.value)?' ':'')+t;ta.dispatchEvent(new Event('input'));ta.focus();
        try{sfx('key');fxSay(t)}catch(x){}}
    };
    new MutationObserver(()=>{ if(!panel.hidden)draw();
      if(next()<0){help.hidden=true;panel.hidden=true} }).observe(ul,{attributes:true,subtree:true,attributeFilter:['class']});
  }

  /* IA + modelo lado a lado */
  const ai=step.querySelector('.ai-box'),mb=step.querySelector('#fxm');
  if(ai||mb){
    const row=document.createElement('div');row.className='sv-acts';
    const anchor=ai||mb;anchor.before(row);
    if(ai)row.appendChild(ai);
    if(mb){mb.textContent='👀 Ver modelo';row.appendChild(mb)}
  }

  /* sem gp (palavras-chave): o personagem também reage e responde quando todos os objetivos acendem */
  if(!f.gp&&ul&&ul.children.length)freeMode(f,step,ul);
}

const OK_DEF=['Boa! ⭐','Isso mesmo! 🎯','Perfeito! 🚀','Muito bem! 👏'];
function freeMode(f,step,ul){
  const lis=[...ul.children],reacted=new Set();
  let box=step.querySelector('.tp-bub');
  if(!box){
    box=document.createElement('div');box.className='tp-bub idle';box.innerHTML='<span>🦫</span><p></p>';
    ul.after(box);
  }
  const bp=box.querySelector('p');
  const say2=m=>{bp.textContent=m;box.classList.remove('idle','pop');void box.offsetWidth;box.classList.add('pop')};
  const plain=t=>String(t||'').replace(/\*\*/g,'');
  let rep=null;
  const r=f.reply||[plain(f.model),'', 'Poggie · um jeito de dizer','🦫'];
  new MutationObserver(()=>{
    let newly=-1;
    lis.forEach((li,i)=>{const d=li.classList.contains('done');
      if(d&&!reacted.has(i)){reacted.add(i);newly=i}else if(!d&&reacted.has(i))reacted.delete(i)});
    if(newly>=0)say2((f.ok&&f.ok[newly])||OK_DEF[newly%OK_DEF.length]);
    const all=reacted.size===lis.length;
    if(all&&!rep){
      rep=document.createElement('div');rep.className='tp-rep';
      rep.innerHTML=`<span>${esc(r[3]||'🧑')}</span><div><small>${esc(f.reply?(r[2]||'Seu amigo')+' responde:':(r[2]||'Poggie'))}</small><b>${esc(r[0])}</b>${r[1]?`<small>${esc(r[1])}</small>`:''}</div><button type="button" aria-label="Ouvir">🔊</button>`;
      rep.querySelector('button').onclick=()=>{try{sfx('pop');fxSay(r[0])}catch(x){}};
      ul.after(rep);
      setTimeout(()=>{try{fxSay(r[0])}catch(x){}},900);
    }else if(!all&&rep){rep.remove();rep=null}
  }).observe(ul,{attributes:true,subtree:true,attributeFilter:['class']});
}
})();
