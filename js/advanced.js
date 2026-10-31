/* Pogglot · prática avançada (C1/C2): "Quase iguais", "Tom certo", "Diga de outro jeito" e "Resumo em uma frase".
   Tudo é montado em tempo de execução a partir do que já existe no episódio (expressões, exemplos, cenas, vocabulário). */
(function(){
'use strict';
if(typeof FXR==='undefined'||typeof FX_KIND==='undefined')return;
const H=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const q=(s,r)=>(r||document).querySelector(s),qa=(s,r)=>[...(r||document).querySelectorAll(s)];
const plain=s=>String(s==null?'':s).replace(/\*\*/g,'');
const norm=s=>String(s||'').toLowerCase().replace(/[’‘]/g,"'").replace(/[^\p{L}\p{N}' ]+/gu,' ').replace(/\s+/g,' ').trim();
const STOP=new Set('the a an and or but of to in on at for with from by about into over after before is are was were be been being am do does did have has had will would can could should must may might i you he she it we they him her us them my your his its our their this that these those there here what when where who why how which not yes if then than so as just very too also only all some any one more most much many every each other another again now'.split(' '));
FX_KIND.pgnuance='practice';FX_LABEL.pgnuance='Quase iguais';
FX_KIND.pgrewrite='practice';FX_LABEL.pgrewrite='Diga de outro jeito';
FX_KIND.pgsum='practice';FX_LABEL.pgsum='Resumo em uma frase';
const hash=s=>{let h=7;for(const c of String(s))h=(h*31+c.charCodeAt(0))>>>0;return h};
const shuffle=(a,seed)=>{a=a.slice();let h=seed>>>0||1;for(let i=a.length-1;i>0;i--){h=(h*1103515245+12345)>>>0;const j=h%(i+1);[a[i],a[j]]=[a[j],a[i]]}return a};

/* ---- banco de registro: informal → formal ---- */
const REG=[
['ask for','request','We need to ask for more time.','We need to request an extension.','pedir'],['find out','ascertain','Let’s find out what happened.','Let us ascertain what occurred.','descobrir'],
['start','commence','The meeting will start at nine.','The meeting will commence at nine.','começar'],['help','assist','Can you help me with this?','Could you assist me with this matter?','ajudar'],
['buy','purchase','We bought the tickets online.','We purchased the tickets online.','comprar'],['need','require','You need a visa to enter.','A visa is required for entry.','precisar'],
['show','demonstrate','The data shows a clear trend.','The data demonstrates a clear trend.','mostrar'],['enough','sufficient','We don’t have enough time.','We do not have sufficient time.','suficiente'],
['but','however','It’s cheap, but it’s slow.','It is inexpensive; however, it is slow.','mas'],['so','therefore','The road was closed, so we turned back.','The road was closed; therefore, we turned back.','então'],
['about','approximately','It costs about ten pounds.','It costs approximately ten pounds.','cerca de'],['think about','consider','I’ll think about your offer.','I will consider your offer.','pensar em'],
['look into','investigate','We’ll look into the problem.','We will investigate the problem.','investigar'],['put up with','tolerate','I can’t put up with this noise.','I cannot tolerate this noise.','tolerar'],
['turn down','decline','She turned down the job.','She declined the position.','recusar'],['go up','increase','Prices went up last year.','Prices increased last year.','aumentar'],
['set up','establish','They set up a new company.','They established a new company.','criar'],['sort out','resolve','Let’s sort out the budget.','Let us resolve the budgetary issue.','resolver'],
['bring up','raise','He brought up a good point.','He raised a valid point.','levantar um assunto'],['carry out','conduct','We carried out a survey.','We conducted a survey.','realizar'],
['come up with','devise','She came up with a plan.','She devised a plan.','bolar'],['deal with','address','We have to deal with this fast.','We must address this promptly.','lidar com'],
['get rid of','eliminate','They got rid of the old rules.','They eliminated the outdated rules.','eliminar'],['make up for','compensate for','Nothing can make up for the loss.','Nothing can compensate for the loss.','compensar'],
['point out','indicate','The report points out several risks.','The report indicates several risks.','indicar'],['give up','abandon','He gave up the project.','He abandoned the project.','abandonar'],
['keep up','maintain','Keep up the good work.','Maintain the high standard.','manter'],['go on','continue','The talks went on for hours.','The negotiations continued for hours.','continuar'],
['talk about','discuss','We talked about the plan.','We discussed the plan.','discutir'],['get','obtain','How did you get that permit?','How did you obtain that permit?','conseguir'],
['try','attempt','They tried to leave early.','They attempted to leave early.','tentar'],['end','terminate','They ended the contract.','They terminated the contract.','encerrar'],
['get in touch with','contact','Get in touch with me soon.','Please contact me at your earliest convenience.','entrar em contato'],['tell','inform','Tell me when you’re ready.','Please inform me when you are ready.','informar'],
['let','permit','They don’t let you park here.','Parking is not permitted here.','permitir'],['say sorry','apologise','He said sorry for the delay.','He apologised for the delay.','pedir desculpas'],
['hurry up','expedite','Can you hurry up the order?','Could you expedite the order?','agilizar'],['boss','supervisor','Ask your boss first.','Consult your supervisor first.','chefe'],
['kids','children','The kids need more space.','The children require more space.','crianças'],['a lot of','numerous','A lot of people complained.','Numerous people complained.','muitos'],
['big','substantial','It’s a big problem.','It is a substantial problem.','grande'],['happen','occur','When did it happen?','When did it occur?','acontecer'],
['check','verify','Check the numbers again.','Verify the figures again.','conferir'],['build','construct','They’re building a bridge.','They are constructing a bridge.','construir'],
['give','provide','We’ll give you the details.','We will provide you with the details.','fornecer'],['stop','cease','The noise stopped at midnight.','The noise ceased at midnight.','parar'],
['use','utilise','We use new methods.','We utilise new methods.','usar'],['look at','examine','The doctor looked at the scan.','The doctor examined the scan.','examinar'],
['make sure','ensure','Make sure the door is locked.','Ensure that the door is secured.','garantir'],['find','locate','I can’t find my keys.','I am unable to locate my keys.','encontrar'],
['leave','depart','The train leaves at six.','The train departs at six.','partir'],['fix','rectify','We’ll fix the error.','We will rectify the error.','corrigir'],
['go against','contravene','That goes against the rules.','That contravenes the regulations.','violar'],['take part in','participate in','Everyone took part in the game.','All members participated in the exercise.','participar'],
['pay back','reimburse','I’ll pay you back tomorrow.','You will be reimbursed tomorrow.','reembolsar'],['wait for','await','We’re waiting for the results.','We are awaiting the results.','aguardar'],
['free','complimentary','The coffee is free.','Coffee is complimentary.','gratuito'],['so that','in order to','We left early so that we could avoid the traffic.','We left early in order to avoid the traffic.','para que'],
['ask','enquire','Ask at the front desk.','Enquire at the front desk.','perguntar'],['wrong','incorrect','That answer is wrong.','That answer is incorrect.','errado'],
['rich','affluent','It’s a rich neighbourhood.','It is an affluent neighbourhood.','rico'],['get better','improve','Things got better after May.','Conditions improved after May.','melhorar'],
['seem','appear','It seems he’s lost.','It appears that he is lost.','parecer'],['enough money','adequate funds','We don’t have enough money.','We lack adequate funds.','recursos suficientes'],
['in the end','ultimately','In the end, it didn’t matter.','Ultimately, it was of no consequence.','no fim'],['mostly','predominantly','The crowd was mostly young.','The crowd was predominantly young.','principalmente'],
['sad','distressing','It was a sad story.','It was a distressing account.','triste'],['hard','arduous','It was a hard journey.','It was an arduous journey.','difícil'],
['want','wish','I want to speak to the manager.','I wish to speak to the manager.','querer'],['start up','launch','They started up a new service.','They launched a new service.','lançar'],
['end up','result in','The plan ended up costing more.','The plan resulted in higher costs.','acabar resultando em'],['look after','care for','She looks after her mother.','She cares for her mother.','cuidar de'],
['come back','return','He came back in May.','He returned in May.','voltar'],['go in','enter','Please go in through the side door.','Please enter through the side door.','entrar'],
['show up','attend','Only ten people showed up.','Only ten people attended.','comparecer'],['put off','postpone','They put off the vote.','They postponed the vote.','adiar'],
['call off','cancel','We called off the trip.','We cancelled the trip.','cancelar'],['hold up','delay','The storm held up the flights.','The storm delayed the flights.','atrasar'],
['think','believe','I think he is right.','I believe he is correct.','acreditar'],['lots of','a great deal of','There’s lots of work to do.','There is a great deal of work to be done.','muito']
];
const UP=s=>s.charAt(0).toUpperCase()+s.slice(1);

/* ---- construção dos exercícios a partir do episódio ---- */
function exps(e){const out=[];(e.fr||[]).forEach(f=>{if(f&&f.k==='pgexp')(f.items||[]).forEach(i=>{const en=plain(i.en||i.x||'').trim();if(en&&i.ex&&i.ex[0]&&i.ex[1])out.push({en,pt:plain(i.pt||''),ex:plain(i.ex[0]),exPt:plain(i.ex[1])})})});return out}
function toks(en){return norm(en).split(' ').filter(t=>t.length>2&&!/^(someone|something|one's|your|their|his|her)$/.test(t))}
function has(text,en){const t=norm(text);return toks(en).every(w=>t.indexOf(w.slice(0,Math.max(3,w.length-3)))>=0)}
function build(e){
  const X=exps(e);if(X.length<3)return null;const seed=hash(String(e.n));const parts=[];
  /* 1) quase iguais: a tradução da frase → qual expressão do mesmo tema */
  const items=X.slice(0,4).map((x,i)=>{
    const sib=X.filter(y=>y.en!==x.en);const opts=shuffle([x].concat(shuffle(sib,seed+i).slice(0,2)),seed+i*7);
    return {stem:x.exPt,opts:opts.map(o=>o.en),a:opts.indexOf(x),why:opts.map(o=>[o.en,o.pt]),say:x.ex}});
  /* tom certo: dois pares do banco, escolhidos por episódio */
  const r0=REG[seed%REG.length],r1=REG[(seed*7+13)%REG.length];
  const tom=[r0,r1].map((r,i)=>{const ask=i%2===0?'formal':'informal';const good=ask==='formal'?3:2,bad=ask==='formal'?2:3;
    const other=REG[(seed+i*17+5)%REG.length];
    const opts=shuffle([r[good],r[bad],ask==='formal'?other[2]:other[3]],seed+i);
    return {stem:ask==='formal'?'Numa carta ou e-mail formal, qual versão você usa?':'Numa conversa entre amigos, qual versão soa mais natural?',opts:opts,a:opts.indexOf(r[good]),why:[[r[2],'informal · '+r[0]+' = '+r[4]],[r[3],'formal · '+r[1]]],say:r[good]}});
  parts.push({k:'pgnuance',title:'Qual expressão encaixa melhor?',items:items.concat(tom)});
  /* 2) diga de outro jeito */
  const rw=[0,1].map(i=>{const base=X[i%X.length],tg=X[(i+1)%X.length];return {base:base.ex,basePt:base.exPt,target:tg.en,hint:tg.pt,model:tg.ex}});
  parts.push({k:'pgrewrite',title:'Diga de outro jeito',items:rw});
  /* 3) resumo */
  const sc=(e.fr||[]).filter(f=>f&&f.k==='pgscene');const L=(sc[1]||sc[0]||{}).lines||[];
  const cnt={};sc.forEach(s=>(s.lines||[]).forEach(l=>norm(l[1]).split(' ').forEach(w=>{if(w.length>=5&&!STOP.has(w))cnt[w]=(cnt[w]||0)+1})));
  const keys=new Set(Object.keys(cnt).filter(w=>cnt[w]>=1).slice(0,60));X.forEach(x=>toks(x.en).forEach(w=>keys.add(w.slice(0,Math.max(3,w.length-3)))));
  (e.v||[]).forEach(v=>{if(v&&v[0])keys.add(norm(v[0]).slice(0,Math.max(3,norm(v[0]).length-2)))});
  if(L.length>=3)parts.push({k:'pgsum',title:'Resumo em uma frase',lines:L.slice(0,9).map(l=>[l[0],plain(l[1]),plain(l[2]||'')]),keys:[...keys],idea:[plain(L[0][2]||''),plain(L[L.length-1][2]||'')],model:plain(L[0][1])});
  return parts}
window.PogAdv={build,REG};

/* ---- renderizadores ---- */
FXR.pgnuance=function(f,st,n){
  const it=f.items||[];let answered=0;
  st.innerHTML=`<div class="step fx ps-nu">${fxKindBar(f,n)}<div class="ps-sh-h"><h2 class="fx-h">${H(f.title)}</h2><span class="ps-count" id="nuc">0/${it.length}</span></div>
   <p class="ps-note">As três opções parecem servir. Pense no <b>sentido exato</b> e no <b>tom</b>: depois do clique, você vê por que cada uma serve ou não.</p>
   <div class="nu-list">${it.map((x,i)=>`<section class="ps-sec nu-q" data-i="${i}"><b class="nu-s">${H(x.stem)}</b><div class="ps-opts">${x.opts.map((o,j)=>`<button type="button" class="ps-o" data-j="${j}">${H(o)}</button>`).join('')}</div><div class="nu-why" hidden></div></section>`).join('')}</div></div>`;
  qa('.nu-q',st).forEach(sec=>{const x=it[+sec.dataset.i];qa('.ps-o',sec).forEach(b=>b.onclick=()=>{
    if(sec.dataset.done)return;sec.dataset.done=1;const j=+b.dataset.j,ok=j===x.a;
    qa('.ps-o',sec).forEach((o,k)=>{o.disabled=true;if(k===x.a)o.classList.add('ok');else if(k===j)o.classList.add('no')});
    const w=q('.nu-why',sec);w.hidden=false;w.innerHTML=`<p>${ok?'✅ Isso!':'❌ Quase.'} <b>${H(x.opts[x.a])}</b>.</p><ul>${x.why.map(p=>`<li><b>${H(p[0])}</b> — ${H(p[1])}</li>`).join('')}</ul>`;
    if(ok)P.score++;try{beep(ok)}catch(e){}try{fxSay(x.say,null,false)}catch(e){}
    answered++;q('#nuc',st).textContent=answered+'/'+it.length;
    if(answered===it.length)cta('Continuar',true,true);else cta('Faltam '+(it.length-answered),false)})});
  P.fx.cta=null;cta('Responda: '+it.length+' perguntas',false);say('Todas parecem servir. Escolha a que encaixa melhor!');
};
FXR.pgrewrite=function(f,st,n){
  const it=f.items||[];let done=0;
  st.innerHTML=`<div class="step fx ps-rw">${fxKindBar(f,n)}<div class="ps-sh-h"><h2 class="fx-h">${H(f.title)}</h2><span class="ps-count" id="rwc">0/${it.length}</span></div>
   <p class="ps-note">Reescreva a frase com a expressão pedida. Não precisa ser igual ao modelo: precisa <b>fazer sentido</b> e usar a expressão.</p>
   <div class="nu-list">${it.map((x,i)=>`<section class="ps-sec rw-q" data-i="${i}"><small>Frase original</small><b class="nu-s">${H(x.base)}</b><small>${H(x.basePt)}</small>
    <p class="rw-t">Agora use: <mark>${H(x.target)}</mark> <em>(${H(x.hint)})</em></p>
    <textarea class="rw-in" rows="2" placeholder="Escreva em inglês…" spellcheck="false"></textarea>
    <div class="rw-act"><button type="button" class="ps-btn main rw-ok">Conferir</button></div><div class="nu-why" hidden></div></section>`).join('')}</div></div>`;
  qa('.rw-q',st).forEach(sec=>{const x=it[+sec.dataset.i];q('.rw-ok',sec).onclick=()=>{
    if(sec.dataset.done)return;const v=q('.rw-in',sec).value.trim();const words=v.split(/\s+/).filter(Boolean).length;
    const w=q('.nu-why',sec);w.hidden=false;
    if(words<3){w.innerHTML='<p>Escreva uma frase completa (pelo menos 3 palavras).</p>';return}
    sec.dataset.done=1;const ok=has(v,x.target);q('.rw-in',sec).disabled=true;q('.rw-ok',sec).disabled=true;
    w.innerHTML=`<p>${ok?'✅ Usou a expressão!':'❌ Faltou usar <b>'+H(x.target)+'</b>.'}</p><p>Modelo: <b>${H(x.model)}</b></p>`;
    if(ok)P.score++;try{beep(ok)}catch(e){}try{fxSay(x.model,null,false)}catch(e){}
    done++;q('#rwc',st).textContent=done+'/'+it.length;if(done===it.length)cta('Continuar',true,true)}});
  P.fx.cta=null;cta('Escreva as '+it.length+' frases',false);say('Use a expressão nova numa frase sua.');
};
FXR.pgsum=function(f,st,n){
  st.innerHTML=`<div class="step fx ps-sm">${fxKindBar(f,n)}<div class="ps-sh-h"><h2 class="fx-h">${H(f.title)}</h2></div>
   <p class="ps-note">Releia a cena e resuma em <b>uma frase</b>, em inglês, com as suas palavras.</p>
   <div class="sm-lines">${f.lines.map(l=>`<p><b>${H(l[0])}:</b> ${H(l[1])} <small>${H(l[2])}</small></p>`).join('')}</div>
   <textarea class="rw-in" id="smin" rows="3" placeholder="In one sentence…" spellcheck="false"></textarea>
   <div class="rw-act"><button type="button" class="ps-btn main" id="smok">Conferir</button></div><div class="nu-why" id="smwhy" hidden></div></div>`;
  let done=false;q('#smok',st).onclick=()=>{
    if(done)return;const v=q('#smin',st).value.trim(),w=q('#smwhy',st);w.hidden=false;
    if(v.split(/\s+/).filter(Boolean).length<5){w.innerHTML='<p>Escreva uma frase com pelo menos 5 palavras.</p>';return}
    done=true;const t=norm(v),hit=[...new Set(f.keys.filter(k=>t.indexOf(k)>=0))];const ok=hit.length>=2;
    q('#smin',st).disabled=true;q('#smok',st).disabled=true;
    w.innerHTML=`<p>${ok?'✅ Bom resumo!':'🤔 Seu resumo ainda não retoma as ideias da cena.'} ${hit.length?`Você usou: <b>${H(hit.slice(0,5).join(', '))}</b>.`:''}</p><p>Ideia central: ${H(f.idea[0])} … ${H(f.idea[1])}</p><p>Uma forma de começar: <b>${H(f.model)}</b></p>`;
    if(ok)P.score++;try{beep(ok)}catch(e){}cta('Continuar',true,true)};
  P.fx.cta=null;cta('Escreva seu resumo',false);say('Uma frase basta. Foque na ideia principal.');
};
const _ft=window.fxTotal;
window.fxTotal=function(e){let n=_ft(e);const fr=(e.fr||[]).flatMap(f=>f.k==='combo'?f.parts:[f]);fr.forEach(f=>{if(f.k==='pgnuance'||f.k==='pgrewrite')n+=(f.items||[]).length;else if(f.k==='pgsum')n+=1});return n};
})();
