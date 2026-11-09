/* Pogglot · quadro "etiqueta de bagagem" (pgtag).
   start: o aluno diz o próprio nome logo no começo (primeira vitória em um minuto).
   end:   o aluno monta a própria etiqueta (nome, país, como está), ouve, fala, guarda e compartilha. */
(function(){
'use strict';
if(typeof FXR==='undefined'||typeof FX_KIND==='undefined'||!window.PogStage)return;
const S=window.PogStage;
const H=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const q=(s,r)=>(r||document).querySelector(s);
const qa=(s,r)=>[...(r||document).querySelectorAll(s)];
const tts=(t,slow)=>{try{fxSay(String(t),null,slow)}catch(e){}};
const KEY='pg_tag',AW='pg_tag_coins';
const get=()=>{try{return JSON.parse(localStorage.getItem(KEY)||'{}')||{}}catch(e){return {}}};
const put=o=>{try{localStorage.setItem(KEY,JSON.stringify(Object.assign(get(),o)))}catch(e){}};
const awarded=k=>{try{return (JSON.parse(localStorage.getItem(AW)||'{}')||{})[k]}catch(e){return false}};
const award=(k,n)=>{if(awarded(k))return false;try{const o=JSON.parse(localStorage.getItem(AW)||'{}')||{};o[k]=1;localStorage.setItem(AW,JSON.stringify(o))}catch(e){}try{window.PogCoins&&PogCoins.add(n)}catch(e){}return true};
const clean=v=>String(v||'').replace(/[^\p{L}\p{M}' -]/gu,'').replace(/\s+/g,' ').trim().slice(0,20);
const pop=(host,txt)=>{const b=document.createElement('div');b.className='tg-pop';b.textContent=txt;host.appendChild(b);setTimeout(()=>b.remove(),1600)};
const lang=()=>(typeof P!=='undefined'&&P.c&&P.c.tts)||'en-US';
function mic(host,target,onDone){
  if(!window.PogVoice){host.innerHTML='<p class="tg-note">Este navegador não reconhece voz: diga a frase em voz alta e toque em “Já falei”.</p>';return false}
  host.hidden=false;host.innerHTML='';
  try{const v=PogVoice.mount(host,{force:true,target,lang:lang(),onDone:r=>onDone&&onDone(r)});if(v&&v.start)v.start();return true}catch(e){return false}
}

FX_LABEL.pgtag='Etiqueta';
FX_KIND.pgtag='speak';

FXR.pgtag=function(f,st,n){
  const mode=f.mode||'start',saved=get();
  const scene=S.stage({rs:f.rs||'station',chars:f.chars||[['bear',36,0,1],['mrs',68,1,1]]});
  if(mode==='start'){
    st.innerHTML=`<div class="step fx tg">
      <div class="tg-story"><span>📖</span><p><b>Paddington está perdido na estação.</b> A Sra. Brown se aproxima.</p></div>
      <div class="tg-scene">${scene}</div>
      <div class="tg-bub"><small>MRS. BROWN</small><b>Hello! What’s your name?</b><span>Olá! Qual é o seu nome?</span><button type="button" class="tg-hear" data-say="Hello! What's your name?">🔊</button></div>
      <label class="tg-lab">Escreva o seu nome<input id="tgName" type="text" maxlength="20" autocomplete="given-name" placeholder="Luiz" value="${H(saved.name||'')}"></label>
      <div class="tg-tag" id="tgTag" aria-live="polite"><span class="tg-hole"></span><div><small>Sua primeira frase</small><b id="tgLine">I’m …</b></div></div>
      <div class="tg-acts"><button type="button" class="ps-btn main" id="tgHear">🔊 Ouvir</button><button type="button" class="ps-btn rec" id="tgSay">🎤 Dizer “I’m …”</button></div>
      <div class="pv-host tg-mic" id="tgMic" hidden></div></div>`;
    const inp=q('#tgName',st),line=q('#tgLine',st),tag=q('#tgTag',st);
    const sentence=()=>{const nm=clean(inp.value);return nm?`I'm ${nm}.`:''};
    const paint=()=>{const s=sentence();line.textContent=s?s.replace("'",'’'):'I’m …'};
    let done=false;
    const finish=()=>{if(done)return;done=true;put({name:clean(inp.value)});tag.classList.add('ok');
      if(award('start',10))pop(st.querySelector('.tg'),'+10 🪙');
      P.fx.cta=null;cta('Continuar: ajudar o Paddington',true,true);
      say(`Muito bem, ${clean(inp.value)}! Você se apresentou!`)};
    inp.oninput=paint;paint();
    qa('[data-say]',st).forEach(b=>b.onclick=()=>tts(b.dataset.say));
    q('#tgHear',st).onclick=()=>{const s=sentence();if(!s){inp.focus();return}tts(s)};
    q('#tgSay',st).onclick=()=>{const s=sentence();if(!s){inp.focus();say('Escreva o seu nome primeiro.');return}
      const host=q('#tgMic',st);
      if(!mic(host,s,r=>{finish()}))finish();
      if(!host.querySelector('.tg-skip')){const b=document.createElement('button');b.type='button';b.className='ps-btn tg-skip';b.textContent='✓ Já falei (sem microfone)';b.onclick=finish;host.appendChild(b)}};
    P.fx.cta=null;cta('Diga o seu nome para continuar',false);
    say('Diga o seu nome em inglês!');
    return;
  }
  /* mode: end */
  const COUNTRIES=['Brazil','Portugal','Angola','Mozambique','Cape Verde','Spain','Argentina','Other'];
  const FEEL=[['happy','😄','feliz'],['tired','😴','cansado'],['hungry','🍞','com fome']];
  const st0=Object.assign({name:'',from:'Brazil',feel:'happy'},saved);
  st.innerHTML=`<div class="step fx tg tg-end">
    <div class="tg-story"><span>🏠</span><p><b>A família Brown leva o Paddington para casa.</b> Agora falta a sua etiqueta, a que vai para o seu álbum.</p></div>
    <div class="tg-form">
      <label class="tg-lab">Nome<input id="tgN" type="text" maxlength="20" value="${H(st0.name)}" placeholder="Luiz"></label>
      <label class="tg-lab">País<select id="tgF">${COUNTRIES.map(c=>`<option${c===st0.from?' selected':''}>${c}</option>`).join('')}</select></label>
      <label class="tg-lab" id="tgOW" hidden>Qual país? (em inglês)<input id="tgO" type="text" maxlength="24" placeholder="Italy"></label>
      <div class="tg-lab">Como você está?<div class="tg-chips" id="tgC">${FEEL.map(x=>`<button type="button" data-v="${x[0]}" class="${x[0]===st0.feel?'on':''}"><span>${x[1]}</span>${x[0]}<small>${x[2]}</small></button>`).join('')}</div></div>
    </div>
    <div class="tg-card" id="tgCard"><span class="tg-hole"></span><small>PLEASE LOOK AFTER THIS PERSON</small><b id="tgL1"></b><b id="tgL2"></b><b id="tgL3"></b><em id="tgSig"></em></div>
    <div class="tg-acts"><button type="button" class="ps-btn main" id="tgP">🔊 Ouvir</button><button type="button" class="ps-btn rec" id="tgM">🎤 Falar a etiqueta</button><button type="button" class="ps-btn" id="tgS">📤 Compartilhar</button></div>
    <div class="pv-host tg-mic" id="tgMic" hidden></div></div>`;
  const nameI=q('#tgN',st),fromS=q('#tgF',st),otherW=q('#tgOW',st),otherI=q('#tgO',st);
  let feel=st0.feel;
  const parts=()=>{const nm=clean(nameI.value)||'…',fr=fromS.value==='Other'?(clean(otherI.value)||'…'):fromS.value;
    return {l1:`I'm ${nm}.`,l2:`I'm from ${fr}.`,l3:`I'm ${feel==='hungry'?'a little hungry':feel}.`,nm,fr}};
  const paint=()=>{otherW.hidden=fromS.value!=='Other';const p=parts();
    q('#tgL1',st).textContent=p.l1.replace("'",'’');q('#tgL2',st).textContent=p.l2.replace("'",'’');q('#tgL3',st).textContent=p.l3.replace("'",'’');
    q('#tgSig',st).textContent='— '+(p.nm==='…'?'you':p.nm)};
  const full=()=>{const p=parts();return `${p.l1} ${p.l2} ${p.l3}`};
  const ready=()=>clean(nameI.value)&&(fromS.value!=='Other'||clean(otherI.value));
  let finished=false;
  const finish=()=>{if(finished)return;finished=true;const p=parts();put({name:p.nm,from:p.fr,feel});q('#tgCard',st).classList.add('ok');
    if(award('end',20))pop(st.querySelector('.tg'),'+20 🪙');
    try{if(window.PogStickers&&PogStickers.add)PogStickers.add({id:'tag-ep1',title:'Minha etiqueta',sub:full()})}catch(e){}
    P.fx.cta=null;cta('Continuar',true,true);say(`Etiqueta guardada, ${p.nm}! 🎉`)};
  nameI.oninput=paint;fromS.onchange=paint;otherI.oninput=paint;
  qa('#tgC button',st).forEach(b=>b.onclick=()=>{feel=b.dataset.v;qa('#tgC button',st).forEach(x=>x.classList.toggle('on',x===b));paint();tts(parts().l3)});
  q('#tgP',st).onclick=()=>{if(!ready()){nameI.focus();return}tts(full())};
  q('#tgM',st).onclick=()=>{if(!ready()){nameI.focus();say('Preencha o nome (e o país) primeiro.');return}
    const host=q('#tgMic',st);if(!mic(host,full(),r=>finish()))finish();
    if(!host.querySelector('.tg-skip')){const b=document.createElement('button');b.type='button';b.className='ps-btn tg-skip';b.textContent='✓ Já falei (sem microfone)';b.onclick=finish;host.appendChild(b)}};
  q('#tgS',st).onclick=()=>{if(!ready()){nameI.focus();return}const txt=`${full()} — Pogglot`;
    try{if(navigator.share){navigator.share({title:'Minha etiqueta no Pogglot',text:txt,url:location.origin}).catch(()=>{});return}}catch(e){}
    try{navigator.clipboard.writeText(txt+' '+location.origin);say('Copiei a sua etiqueta. É só colar onde quiser!')}catch(e){say(txt)}};
  paint();
  P.fx.cta=null;cta('Fale a etiqueta para guardar',false);
  say('Monte a sua etiqueta e fale em voz alta!');
};
})();
