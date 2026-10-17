/* Pogglot · correção do "Sua vez"
   Ordem: 1) seu servidor (config.js › ai.endpoint)  2) Claude dentro do artefato (capacidade "sample")  3) conferência básica no aparelho.
   Para correção humana, o aluno pode enviar o texto ao professor pelo endpoint (config.js › ai.teacher). */
(function(){
'use strict';
const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const HL=()=>(typeof ST!=='undefined'&&ST.homeLang)||'pt';
const CFG=()=>((window.POGGLOT_CONFIG&&POGGLOT_CONFIG.ai)||{});
const TX={
 pt:{btn:'🤖 Corrigir meu texto',busy:'Lendo seu texto…',title:'Correção',score:'Nota',fixed:'Versão corrigida',issues:'O que ajustar',praise:'O que ficou bom',none:'Nenhum erro encontrado. Muito bem!',listen:'Ouvir',
  ai:'Correção por IA',basic:'Conferência básica (sem IA). Conecte a IA em Ajustes ou no config.js para uma correção completa.',endp:'Correção do seu servidor',short:'Escreva uma frase um pouco maior para eu corrigir.',err:'Não consegui corrigir agora. Tente de novo.',retry:'Corrigir de novo',
  teacher:'👩‍🏫 Enviar ao professor',sent:'Enviado! Você receberá a correção em breve.',limit:'Muitas correções seguidas. Espere um instante.'},
 es:{btn:'🤖 Corregir mi texto',busy:'Leyendo tu texto…',title:'Corrección',score:'Nota',fixed:'Versión corregida',issues:'Qué ajustar',praise:'Qué quedó bien',none:'No encontré errores. ¡Muy bien!',listen:'Escuchar',
  ai:'Corrección con IA',basic:'Revisión básica (sin IA). Conecta la IA en Ajustes o en config.js para una corrección completa.',endp:'Corrección de tu servidor',short:'Escribe una frase un poco más larga para corregirla.',err:'No pude corregir ahora. Inténtalo de nuevo.',retry:'Corregir de nuevo',
  teacher:'👩‍🏫 Enviar al profesor',sent:'¡Enviado! Recibirás la corrección pronto.',limit:'Demasiadas correcciones seguidas. Espera un momento.'}
};
const k=key=>{const t=TX[HL()]||TX.pt;return t[key]!=null?t[key]:TX.pt[key]};
const LNAME={en:'English',es:'Spanish',pt:'Portuguese',fr:'French',de:'German',it:'Italian'};

/* ---------- 3) conferência local ---------- */
const PT_WORDS=/\b(você|voce|não|nao|que|é|uma|muito|obrigado|também|tambem|para|com|mas|isso|está|esta)\b/gi;
const ES_WORDS=/\b(usted|qué|que|muy|gracias|también|pero|está|esta|con|una|para)\b/gi;
const EN_FIX=[[/\bi\b(?!['’])/g,'I','Use “I” sempre em maiúscula.'],[/\bdont\b/gi,"don't",'Faltou o apóstrofo: don’t.'],[/\bcant\b/gi,"can't",'Faltou o apóstrofo: can’t.'],[/\bim\b/gi,"I'm",'Escreva I’m (I am).'],[/\bive\b/gi,"I've",'Escreva I’ve (I have).'],[/\bdoesnt\b/gi,"doesn't",'Faltou o apóstrofo: doesn’t.'],[/\bisnt\b/gi,"isn't",'Faltou o apóstrofo: isn’t.'],[/\bthank you very much\b/gi,null,null],[/\bI am agree\b/gi,'I agree','Em inglês não se usa “am” com agree.'],[/\bI have (\d+) years\b/gi,'I am $1 years old','Idade em inglês: I am … years old.'],[/\bpeoples\b/gi,'people','People já é plural.'],[/\bmore better\b/gi,'better','Não use “more” com better.']];
function localCheck(o){
  const text=String(o.text||'').trim(),lang=String(o.lang||'en').slice(0,2),issues=[],praise=[];
  let fixed=text,score=70;
  const words=text.split(/\s+/).filter(Boolean);
  if(lang==='en'){
    EN_FIX.forEach(([re,rep,why])=>{if(!rep)return;const g=new RegExp(re.source,re.flags.includes('g')?re.flags:re.flags+'g');let m;const found=[];
      fixed=fixed.replace(g,(x,a1)=>{const r=rep.replace('$1',a1||'');found.push([x,r]);return r});
      found.slice(0,1).forEach(([x,r])=>{issues.push({wrong:x,fix:r,why});score-=8})});
    if((text.match(PT_WORDS)||[]).length>=2){issues.push({wrong:'—',fix:'—',why:'Parece haver palavras em português. Tente escrever tudo em inglês.'});score-=20}
  }else if(lang==='pt'||lang==='es'){
    const other=lang==='pt'?ES_WORDS:PT_WORDS;
    if((text.match(other)||[]).length>=3){issues.push({wrong:'—',fix:'—',why:'Parece haver palavras de outro idioma na frase.'});score-=15}
  }
  if(/^[a-zà-ú]/.test(fixed)){fixed=fixed.charAt(0).toUpperCase()+fixed.slice(1);issues.push({wrong:text.slice(0,12),fix:fixed.slice(0,12),why:'Comece a frase com letra maiúscula.'});score-=5}
  if(!/[.!?…]["”']?$/.test(fixed)){fixed+='.';issues.push({wrong:'…',fix:'.',why:'Termine a frase com ponto, exclamação ou interrogação.'});score-=4}
  const dup=text.match(/\b(\w{2,})\s+\1\b/i);if(dup){issues.push({wrong:dup[0],fix:dup[1],why:'Palavra repetida.'});fixed=fixed.replace(/\b(\w{2,})\s+\1\b/i,'$1');score-=6}
  const chips=(o.chips||[]).filter(c=>c&&c.length>1),used=chips.filter(c=>text.toLowerCase().includes(String(c).toLowerCase()));
  if(chips.length){if(used.length===chips.length){praise.push('Você usou todas as expressões pedidas.');score+=15}else if(used.length){praise.push('Você usou '+used.length+' de '+chips.length+' expressões.');const miss=chips.filter(c=>!used.includes(c));issues.push({wrong:'—',fix:miss.join(' · '),why:'Tente incluir também estas expressões.'});score-=6*miss.length}else{issues.push({wrong:'—',fix:chips.join(' · '),why:'Tente usar as expressões do desafio.'});score-=15}}
  if(words.length>=6)praise.push('Boa extensão: '+words.length+' palavras.');
  if(words.length<3){score-=15}
  score=Math.max(20,Math.min(96,Math.round(score)));
  return{corrected:fixed,score,summary:'',issues:issues.filter(i=>i.why),praise,source:'local'};
}

/* ---------- 2) Claude via capacidade sample ---------- */
async function viaSample(o){
  if(!(window.claude&&claude.use))return null;
  const sample=await claude.use('sample');if(!sample)return null;
  const ui=(o.uiLang||'pt')==='es'?'Spanish':'Brazilian Portuguese';
  const input=`You are a kind, precise language teacher. A student at level ${o.level||'A1-B1'} is learning ${LNAME[String(o.lang).slice(0,2)]||o.lang}. 
Task given to the student: ${o.prompt}
Expressions they should use: ${(o.chips||[]).join(' | ')||'—'}
Model answer (for reference only): ${o.model||'—'}
Student's text: """${o.text}"""

Correct the text. Keep the student's meaning and voice; fix only what is wrong, and keep it at the student's level. Explain in ${ui}, in short sentences. Reply with JSON only, exactly in this shape:
{"corrected":"<corrected text in the target language>","score":<0-100 integer>,"issues":[{"wrong":"<excerpt>","fix":"<fix>","why":"<one short reason in ${ui}>"}],"praise":["<one thing done well, in ${ui}>"]}
If there are no errors, "issues" is an empty array and "corrected" equals the student's text.`;
  const j=await sample.json(input,{modelTier:'quick',cache:false});
  if(!j||typeof j.corrected!=='string')return null;
  return{corrected:j.corrected,score:Math.max(0,Math.min(100,Math.round(+j.score||0))),summary:'',issues:Array.isArray(j.issues)?j.issues.slice(0,8):[],praise:Array.isArray(j.praise)?j.praise.slice(0,3):[],source:'ai'};
}
/* ---------- 1) seu servidor ---------- */
async function viaEndpoint(o){
  const c=CFG();if(!c.endpoint)return null;
  const r=await fetch(c.endpoint,{method:'POST',headers:Object.assign({'Content-Type':'application/json'},c.headers||{}),body:JSON.stringify(o)});
  if(!r.ok)throw new Error('ai '+r.status);
  const j=await r.json();if(!j||typeof j.corrected!=='string')throw new Error('ai: formato');
  return{corrected:j.corrected,score:Math.max(0,Math.min(100,Math.round(+j.score||0))),summary:j.summary||'',issues:Array.isArray(j.issues)?j.issues:[],praise:Array.isArray(j.praise)?j.praise:[],source:'endpoint'};
}
let last=0;
async function correct(o){
  if(Date.now()-last<1500){const e=new Error('limit');e.code='limit';throw e}
  last=Date.now();
  for(const fn of [viaEndpoint,viaSample]){try{const r=await fn(o);if(r)return r}catch(e){if(e&&e.code==='not_granted'||e&&e.code==='cancelled')break}}
  return localCheck(o);
}

/* ---------- interface no quadro "Sua vez" ---------- */
function mount(f,st){
  const ta=st.querySelector('#fxta');if(!ta||st.querySelector('#aibtn'))return;
  const box=document.createElement('div');box.className='ai-box';
  box.innerHTML=`<button class="pill ai-btn" id="aibtn" type="button">${esc(k('btn'))}</button>${CFG().teacher?`<button class="pill light ai-btn" id="aiteach" type="button">${esc(k('teacher'))}</button>`:''}<div id="airs" aria-live="polite"></div>`;
  ta.insertAdjacentElement('afterend',box);
  const out=box.querySelector('#airs'),btn=box.querySelector('#aibtn');
  const lang=(typeof P!=='undefined'&&P&&P.c&&P.c.tts)||'en-US',cid=(typeof P!=='undefined'&&P&&P.cid)||'';
  const level=(String(cid).match(/-([a-c][12])$/i)||[])[1]||'';
  const payload=()=>({lang,uiLang:HL(),prompt:String(f.prompt||'').replace(/\*\*/g,''),chips:f.chips||[],model:String(f.model||'').replace(/\*\*/g,''),criteria:f.check||[],level:level.toUpperCase(),text:ta.value.trim()});
  btn.onclick=async()=>{
    const p=payload();
    if(p.text.length<4){out.innerHTML=`<p class="ai-note">${esc(k('short'))}</p>`;return}
    btn.disabled=true;out.innerHTML=`<p class="ai-note"><span class="ai-dot"></span> ${esc(k('busy'))}</p>`;
    try{
      const r=await correct(p);
      const tag=r.source==='ai'?k('ai'):r.source==='endpoint'?k('endp'):k('basic');
      const cls=r.score>=85?'great':r.score>=65?'good':r.score>=40?'ok':'low';
      out.innerHTML=`<div class="ai-card ${r.source}"><div class="ai-top"><div class="ai-score ${cls}"><b>${r.score}</b><small>${esc(k('score'))}</small></div><div><b>${esc(k('title'))}</b><small class="ai-src">${esc(tag)}</small></div></div>
        <div class="ai-fixed"><small>${esc(k('fixed'))}</small><div class="ai-fx"><span>${esc(r.corrected)}</span><button class="say2" id="aiplay" aria-label="${esc(k('listen'))}" type="button">🔊</button></div></div>
        ${r.issues.length?`<div class="ai-list"><small>${esc(k('issues'))}</small><ul>${r.issues.map(i=>`<li>${i.wrong&&i.wrong!=='—'?`<s>${esc(i.wrong)}</s> → <b>${esc(i.fix)}</b><br>`:(i.fix&&i.fix!=='—'?`<b>${esc(i.fix)}</b><br>`:'')}<span>${esc(i.why||'')}</span></li>`).join('')}</ul></div>`:`<p class="ai-ok">✅ ${esc(k('none'))}</p>`}
        ${r.praise.length?`<div class="ai-list good"><small>${esc(k('praise'))}</small><ul>${r.praise.map(x=>`<li>${esc(x)}</li>`).join('')}</ul></div>`:''}</div>`;
      const pl=out.querySelector('#aiplay');if(pl)pl.onclick=()=>{try{speak(r.corrected,lang)}catch(e){}};
      try{ST.xp+=r.score>=65?2:1;save()}catch(e){}
    }catch(e){out.innerHTML=`<p class="ai-note warn">${esc(e&&e.code==='limit'?k('limit'):k('err'))}</p>`}
    btn.disabled=false;btn.textContent='🔄 '+k('retry');
  };
  const tb=box.querySelector('#aiteach');
  if(tb)tb.onclick=async()=>{const p=payload();if(p.text.length<4){out.innerHTML=`<p class="ai-note">${esc(k('short'))}</p>`;return}
    try{const c=CFG();const r=await fetch(c.teacher,{method:'POST',headers:Object.assign({'Content-Type':'application/json'},c.headers||{}),body:JSON.stringify(p)});if(!r.ok)throw 0;out.innerHTML=`<p class="ai-note ok">${esc(k('sent'))}</p>`}catch(e){out.innerHTML=`<p class="ai-note warn">${esc(k('err'))}</p>`}};
}
if(typeof FXR!=='undefined'&&FXR.produce){const o=FXR.produce;FXR.produce=function(f,st,n){const r=o.call(this,f,st,n);try{mount(f,st)}catch(e){}return r}}
window.PogAI={correct,localCheck};
})();
