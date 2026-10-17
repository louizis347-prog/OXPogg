/* Pogglot · fala com feedback (reconhecimento de voz + nota palavra por palavra)
   Usa a Web Speech API (SpeechRecognition): Chrome, Edge e Safari. Sem suporte, o aluno pode pular. */
(function(){
'use strict';
const SR=()=>window.SpeechRecognition||window.webkitSpeechRecognition;
const store={get(k,d){try{const v=localStorage.getItem('pogglot:'+k);return v?JSON.parse(v):d}catch(e){return d}},set(k,v){try{localStorage.setItem('pogglot:'+k,JSON.stringify(v))}catch(e){}}};
const ui=()=>{try{if(window.P&&P.c&&P.c.ui&&P.e&&document.querySelector('#pstage'))return P.c.ui==='es'?'es':'pt'}catch(e){}return (window.ST&&ST.homeLang)==='es'?'es':'pt'};
const TXT={
 pt:{tap:'Toque no microfone e fale',listen:'Ouvindo… fale agora',proc:'Analisando…',again:'Tentar de novo',model:'Ouvir modelo',slow:'Devagar',skip:'Pular',
  great:'Excelente! Pronúncia clara.',good:'Muito bom! Falta pouco.',ok:'Quase lá. Ouça o modelo e repita.',low:'Vamos de novo, devagar. Ouça o modelo primeiro.',
  heard:'Eu ouvi',nosp:'Não ouvi nada. Chegue mais perto e fale logo depois de tocar.',deny:'O microfone foi bloqueado. Libere a permissão do microfone para este site e tente de novo. Dentro de uma página incorporada (como uma prévia), o navegador pode bloquear: abra o app direto na página.',
  uns:'Este navegador não reconhece voz. Use o Chrome, o Edge ou o Safari. Você pode pular este exercício.',net:'O reconhecimento de voz precisa de internet. Tente de novo quando estiver conectado.',err:'Não consegui ouvir. Tente de novo.',
  legend:'verde: certo · amarelo: quase · vermelho: ouça de novo',priv:'O navegador pode enviar o áudio ao serviço de reconhecimento de voz dele.',tryw:'Toque numa palavra para ouvir'},
 es:{tap:'Toca el micrófono y habla',listen:'Escuchando… habla ahora',proc:'Analizando…',again:'Intentar de nuevo',model:'Escuchar modelo',slow:'Despacio',skip:'Saltar',
  great:'¡Excelente! Pronunciación clara.',good:'¡Muy bien! Falta poco.',ok:'Casi. Escucha el modelo y repite.',low:'Otra vez, despacio. Escucha primero el modelo.',
  heard:'Escuché',nosp:'No escuché nada. Acércate y habla justo después de tocar.',deny:'El micrófono está bloqueado. Permite el micrófono para este sitio e inténtalo de nuevo. En una página incrustada (como una vista previa) el navegador puede bloquearlo: abre la app directamente.',
  uns:'Este navegador no reconoce voz. Usa Chrome, Edge o Safari. Puedes saltar este ejercicio.',net:'El reconocimiento de voz necesita internet. Inténtalo con conexión.',err:'No pude escuchar. Inténtalo de nuevo.',
  legend:'verde: correcto · amarillo: casi · rojo: escucha otra vez',priv:'El navegador puede enviar el audio a su servicio de reconocimiento de voz.',tryw:'Toca una palabra para escucharla'}
};
const T=k=>TXT[ui()][k];
const esc=s=>String(s==null?'':s).replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]));

/* ---------- normalização e nota ---------- */
const CONTR={"i'm":'i am',"you're":'you are',"he's":'he is',"she's":'she is',"it's":'it is',"we're":'we are',"they're":'they are',"that's":'that is',"there's":'there is',"what's":'what is',"where's":'where is',"who's":'who is',"don't":'do not',"doesn't":'does not',"didn't":'did not',"can't":'can not',"cannot":'can not',"won't":'will not',"isn't":'is not',"aren't":'are not',"wasn't":'was not',"weren't":'were not',"haven't":'have not',"hasn't":'has not',"i've":'i have',"i'll":'i will',"i'd":'i would',"let's":'let us',"gonna":'going to',"wanna":'want to'};
function words(s,lang){
  let t=String(s).replace(/\*\*/g,'').replace(/[’‘`´]/g,"'").toLowerCase();
  if(/^en/.test(lang||'en'))t=t.replace(/[a-z]+'[a-z]+|gonna|wanna|cannot/g,m=>CONTR[m]||m);
  t=t.normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/[^a-z0-9' ]+/g,' ').replace(/'/g,'');
  return t.split(/\s+/).filter(Boolean);
}
function lev(a,b){const m=a.length,n=b.length;if(!m)return n;if(!n)return m;let p=Array.from({length:n+1},(_,j)=>j);
  for(let i=1;i<=m;i++){const c=[i];for(let j=1;j<=n;j++)c[j]=Math.min(p[j]+1,c[j-1]+1,p[j-1]+(a[i-1]===b[j-1]?0:1));p=c}return p[n]}
function sim(a,b){if(a===b)return 1;const L=Math.max(a.length,b.length);return L?1-lev(a,b)/L:0}
function cmpWord(a,b){const s=sim(a,b);if(s===1)return 'ok';if(a.length>=4&&s>=.72)return 'close';if(a.length>=3&&b.length>=3&&(a.startsWith(b)||b.startsWith(a))&&Math.abs(a.length-b.length)<=2)return 'close';return 'miss'}
/* alinha as palavras da frase alvo com o que foi ouvido */
function align(T0,H0){
  const n=T0.length,m=H0.length,D=Array.from({length:n+1},()=>new Array(m+1).fill(0)),B=Array.from({length:n+1},()=>new Array(m+1).fill(0));
  for(let i=1;i<=n;i++){D[i][0]=i;B[i][0]=1}for(let j=1;j<=m;j++){D[0][j]=j*.7;B[0][j]=2}
  for(let i=1;i<=n;i++)for(let j=1;j<=m;j++){
    const c=cmpWord(T0[i-1],H0[j-1]),sub=D[i-1][j-1]+(c==='ok'?0:c==='close'?.35:1.1);
    let best=sub,b=0;
    if(D[i-1][j]+1<best){best=D[i-1][j]+1;b=1}
    if(D[i][j-1]+.7<best){best=D[i][j-1]+.7;b=2}
    D[i][j]=best;B[i][j]=b}
  const out=new Array(n).fill(null);let i=n,j=m;
  while(i>0||j>0){
    if(i>0&&j>0&&B[i][j]===0){out[i-1]={w:T0[i-1],st:cmpWord(T0[i-1],H0[j-1]),heard:H0[j-1]};i--;j--}
    else if(i>0&&(j===0||B[i][j]===1)){out[i-1]={w:T0[i-1],st:'miss',heard:''};i--}
    else j--;
  }
  return out;
}
function score(target,alts,lang){
  const T0=words(target,lang);if(!T0.length)return{score:0,words:[],heard:''};
  let best=null;
  for(const a of alts){const H0=words(a,lang);const al=align(T0,H0);
    let ok=0,close=0;al.forEach(x=>{if(x.st==='ok')ok++;else if(x.st==='close')close++});
    const extra=Math.max(0,H0.length-T0.length)*.04;
    const sc=Math.max(0,Math.round((ok+.6*close)/T0.length*100-extra*100));
    if(!best||sc>best.score)best={score:sc,words:al,heard:a}}
  return best||{score:0,words:T0.map(w=>({w,st:'miss',heard:''})),heard:''};
}
function tier(sc){return sc>=85?'great':sc>=65?'good':sc>=40?'ok':'low'}

/* ---------- escuta ---------- */
let cur=null;
function stop(){try{if(cur)cur.abort()}catch(e){}cur=null}
function listen(o){
  const Rec=SR();if(!Rec){o.onDone({error:'unsupported'});return null}
  stop();
  const r=new Rec();cur=r;r.lang=o.lang||'en-US';r.interimResults=true;r.maxAlternatives=5;r.continuous=false;
  let alts=null,last='',err='',fin=false,timer=0;
  const finish=()=>{if(fin)return;fin=true;clearTimeout(timer);if(cur===r)cur=null;
    o.onDone(alts&&alts.length?{alts}:last?{alts:[last]}:{error:err||'no-speech'})};
  r.onstart=()=>{o.onStart&&o.onStart()};
  r.onresult=ev=>{const res=ev.results[ev.results.length-1];last=res[0].transcript;
    if(res.isFinal)alts=Array.from(res).map(a=>a.transcript);else o.onInterim&&o.onInterim(last)};
  r.onerror=ev=>{err=ev.error||'error'};
  r.onend=finish;
  timer=setTimeout(()=>{try{r.stop()}catch(e){}},o.maxMs||9000);
  try{r.start()}catch(e){err='start';finish()}
  return{stop(){try{r.stop()}catch(e){}}};
}
function say(t,lang,slow){try{if(typeof fxSay==='function'&&!lang)fxSay(t,null,slow);else if(typeof speak==='function')speak(t,lang||((window.P&&P.c&&P.c.tts)||'en-US'),null,null,slow)}catch(e){}}
function record(sc,target,lang){
  const s=store.get('speak',{n:0,sum:0,great:0,best:0,day:{}});s.n++;s.sum+=sc;if(sc>=85)s.great++;s.best=Math.max(s.best||0,sc);
  const d=new Date().toISOString().slice(0,10);s.day=s.day||{};s.day[d]=(s.day[d]||0)+1;
  const keys=Object.keys(s.day).sort();while(keys.length>30)delete s.day[keys.shift()];
  store.set('speak',s);
  try{document.dispatchEvent(new CustomEvent('pogglot:speak',{detail:{score:sc,target,lang}}))}catch(e){}
  try{if(window.PogUI&&PogUI.syncNow)PogUI.syncNow()}catch(e){}
}

/* ---------- widget ---------- */
function mount(host,o){
  const lang=o.lang||((window.P&&P.c&&P.c.tts)||'en-US'),target=String(o.target).replace(/\*\*/g,'');
  host.innerHTML=`<div class="pv" data-state="idle"><div class="pv-row"><button type="button" class="pv-mic" aria-label="${esc(T('tap'))}"><span class="pv-ic">🎤</span><i class="pv-wave"><b></b><b></b><b></b><b></b><b></b></i></button><div class="pv-st" aria-live="polite">${esc(T('tap'))}</div></div><div class="pv-res" hidden></div></div>`;
  const root=host.querySelector('.pv'),mic=root.querySelector('.pv-mic'),st=root.querySelector('.pv-st'),res=root.querySelector('.pv-res');
  const setState=(s,msg)=>{root.dataset.state=s;if(msg!=null)st.textContent=msg};
  let h=null;
  const show=r=>{
    const pills=r.words.map((x,i)=>`<button type="button" class="pv-w ${x.st}" data-w="${esc(x.w)}" title="${esc(T('tryw'))}">${esc(x.w)}</button>`).join(' ');
    const tr=tier(r.score);
    res.hidden=false;
    res.innerHTML=`<div class="pv-score ${tr}"><b>${r.score}%</b><span>${esc(T(tr==='great'?'great':tr==='good'?'good':tr==='ok'?'ok':'low'))}</span></div>
     <div class="pv-words">${pills}</div><small class="pv-leg">${esc(T('legend'))}</small>
     ${r.heard?`<small class="pv-heard">${esc(T('heard'))}: “${esc(r.heard)}”</small>`:''}
     <div class="pv-btns"><button type="button" class="pv-b" data-a="model">🔊 ${esc(T('model'))}</button><button type="button" class="pv-b" data-a="slow">🐢 ${esc(T('slow'))}</button><button type="button" class="pv-b main" data-a="again">🎤 ${esc(T('again'))}</button></div>`;
    res.querySelectorAll('.pv-w').forEach(b=>b.onclick=()=>say(b.dataset.w,lang,true));
    res.querySelector('[data-a=model]').onclick=()=>say(target,lang,false);
    res.querySelector('[data-a=slow]').onclick=()=>say(target,lang,true);
    res.querySelector('[data-a=again]').onclick=()=>start();
  };
  const fail=code=>{
    const m=code==='unsupported'?T('uns'):(code==='not-allowed'||code==='service-not-allowed')?T('deny'):code==='network'?T('net'):(code==='no-speech'||code==='aborted')?T('nosp'):T('err');
    setState('idle',m);if(o.onFail)o.onFail(code);
  };
  const start=()=>{
    if(h){h.stop();h=null;setState('idle',T('tap'));return}
    try{if(typeof speechSynthesis!=='undefined')speechSynthesis.cancel()}catch(e){}
    res.hidden=true;setState('listen',T('listen'));
    h=listen({lang,onStart:()=>setState('listen',T('listen')),onInterim:t=>{st.textContent='“'+t+'”'},
      onDone:r=>{h=null;
        if(r.error){fail(r.error);return}
        setState('proc',T('proc'));
        const sc=score(target,r.alts,lang);setState('done',T('tap'));
        show(sc);record(sc.score,target,lang);
        if(o.onDone)o.onDone(sc);
      }});
    if(!h&&!SR())fail('unsupported');
  };
  mic.onclick=start;
  return{start,destroy(){stop()}};
}
const PogVoice=window.PogVoice={supported:()=>!!SR(),mount,score,listen,stop,words,stats:()=>store.get('speak',{n:0,sum:0,great:0,best:0,day:{}}),T};

/* testes rápidos de nota (usados na verificação) */
PogVoice._selfTest=()=>{
  const a=score('I like coffee',['i like coffee'],'en-US').score,b=score('I like coffee',['i like toffee'],'en-US').score,c=score('I like coffee',['hello'],'en-US').score,d=score("I'm Mia",['i am mia'],'en-US').score;
  return{a,b,c,d};
};
})();
