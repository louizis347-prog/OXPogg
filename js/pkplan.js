/* Pocket · plano de estudo, exames a cada 20 episódios e relatório de desempenho com prognóstico.
   Tudo é calculado no aparelho (localStorage 'pkp:*'): plano por ritmo, exame gerado a partir do vocabulário e dos padrões
   (nunca das falas do diálogo), relatório com habilidades, palavras fracas e previsão de conclusão. */
(function(){
'use strict';
if(typeof EP==='undefined'||typeof ST==='undefined'||typeof COURSES==='undefined')return;
const H=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const KEY='pkp:';
const get=(k,d)=>{try{const v=localStorage.getItem(KEY+k);return v==null?d:JSON.parse(v)}catch(e){return d}};
const put=(k,v)=>{try{localStorage.setItem(KEY+k,JSON.stringify(v))}catch(e){}};
const shuf=a=>{a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a};
const rnd=a=>a[Math.floor(Math.random()*a.length)];
const clamp=(x,a,b)=>Math.max(a,Math.min(b,x));
const avg=a=>a.length?a.reduce((x,y)=>x+y,0)/a.length:0;
const DAY=86400000,DN=['dom','seg','ter','qua','qui','sex','sáb'];
const iso=d=>{const x=new Date(d);return x.getFullYear()+'-'+String(x.getMonth()+1).padStart(2,'0')+'-'+String(x.getDate()).padStart(2,'0')};
const fromIso=s=>{const [y,m,d]=s.split('-').map(Number);return new Date(y,m-1,d)};
const today=()=>{const d=new Date();return new Date(d.getFullYear(),d.getMonth(),d.getDate())};
const fdate=d=>String(d.getDate()).padStart(2,'0')+'/'+String(d.getMonth()+1).padStart(2,'0');
const fdateL=d=>d.toLocaleDateString('pt-BR',{day:'numeric',month:'long',year:'numeric'});
const courses=()=>Object.keys(COURSES).filter(k=>/^pk-/.test(k)&&EP[k]&&EP[k].length);
const avail=cid=>(EP[cid]||[]).filter(e=>!(typeof isPlannedEpisode==='function'&&isPlannedEpisode(e)));
const isDone=(cid,e)=>!!ST.done[cid+'-'+e.n];
const cname=cid=>{try{return COURSES[cid].name[COURSES[cid].ui]}catch(x){return cid}};
const lvlOf=cid=>String(cid).split('-')[1].toUpperCase();
const block=(cid,k)=>avail(cid).slice(k*20,k*20+20);
const nBlocks=cid=>{const n=avail(cid).length;return Math.floor(n/20)+(n%20>=10?1:0)};
const blockDone=(cid,k)=>{const b=block(cid,k);return b.length>=10&&b.every(e=>isDone(cid,e))};

/* ───────── estatísticas por episódio ───────── */
const epStats=cid=>get('stats:'+cid,{});
function recordEpisode(){
  try{const e=P.e,cid=P.cid,c=(window.PKS&&PKS.cur)||{};
    const all=epStats(cid);if(all[e.n])return;
    all[e.n]={ts:Date.now(),sec:Math.max(5,((Date.now()-P.t0)/1000)|0),voc:(c.voc||[]).length,vt:c.vt||0,b:c.b||0,bt:c.bt||0,sp:c.sp||0,sk:c.sk||0,dl:c.dl||0};
    put('stats:'+cid,all)}catch(x){}}
const avgMin=cid=>{const v=Object.values(epStats(cid)).map(s=>s.sec).filter(s=>s>=60&&s<=3600);return v.length>=3?clamp(Math.round(avg(v)/60),6,25):12};

/* ───────── plano ───────── */
const PRESETS=[
  {id:'leve',n:'Leve',d:'3 episódios por semana',per:1,days:[1,3,6]},
  {id:'regular',n:'Regular',d:'5 episódios por semana',per:1,days:[1,2,3,4,5]},
  {id:'intenso',n:'Intenso',d:'10 episódios por semana',per:2,days:[1,2,3,4,5]},
  {id:'custom',n:'Personalizado',d:'você escolhe minutos e dias',per:1,days:[1,2,3,4,5]}];
const getPlan=cid=>get('plan:'+cid,null);
function buildSessions(cid,plan,from){
  const eps=avail(cid),total=eps.length;let next=eps.filter(e=>isDone(cid,e)).length;const out=[];
  let d=new Date(from||today()),g=0;
  while(next<total&&g++<3000){
    if(plan.days.includes(d.getDay())){
      let to=Math.min(total,next+plan.per);const bnd=Math.floor(next/20)*20+20;if(to>bnd)to=bnd;
      const ex=(to%20===0||(to===total&&total%20>=10))?Math.ceil(to/20)-1:null;
      out.push({date:new Date(d),from:next+1,to,exam:ex});next=to}
    d=new Date(d.getTime()+DAY)}
  return out}
const weeklyEps=p=>p.per*p.days.length;
function weekStart(d){const x=new Date(d);const k=(x.getDay()+6)%7;x.setDate(x.getDate()-k);return x}
function planStatus(cid){
  const pl=getPlan(cid);if(!pl)return null;
  const eps=avail(cid),done=eps.filter(e=>isDone(cid,e)).length,st=fromIso(pl.start);
  let sessions=0;for(let d=new Date(st);d<=today();d=new Date(d.getTime()+DAY))if(pl.days.includes(d.getDay()))sessions++;
  const expected=Math.min(eps.length,(pl.done0||0)+sessions*pl.per);
  return {done,expected,diff:done-expected,pl}}

/* ───────── exame (vocabulário e padrões; nunca as falas do diálogo) ───────── */
function poolOf(eps){
  const V=new Map(),B=[];
  eps.forEach(e=>{(e.v||[]).forEach(v=>{const k=String(v[0]).toLowerCase();if(!V.has(k))V.set(k,{w:v[0],pt:v[1]})});
    const bf=(e.fr||[]).find(f=>f.k==='pkbuild');if(bf)(bf.items||[]).forEach(b=>B.push(b))});
  return {V:[...V.values()],B}}
const fill=(t,o)=>t.replace('{0}',o)
function distract(V,t,n,key){const seen=new Set([t[key].toLowerCase()]),out=[];
  for(const x of shuf(V)){const v=x[key].toLowerCase();if(x.w.toLowerCase()===t.w.toLowerCase()||x.pt===t.pt||seen.has(v))continue;seen.add(v);out.push(x);if(out.length>=n)break}
  return out}
function itemVoc(p,used,target){
  const t=target||rnd(p.V.filter(v=>!used.has(v.w)));if(!t)return null;const d=distract(p.V,t,3,'pt');if(d.length<3)return null;used.add(t.w);
  return {k:'mc',skill:'vocab',q:'O que significa “'+t.w+'”?',say:t.w,opts:shuf([t.pt].concat(d.map(x=>x.pt))),ans:t.pt,word:t}}
function itemRev(p,used,target){
  const t=target||rnd(p.V.filter(v=>!used.has('r'+v.w)));if(!t)return null;const d=distract(p.V,t,3,'w');if(d.length<3)return null;used.add('r'+t.w);
  return {k:'mc',skill:'vocab',q:'Como se diz “'+t.pt+'” em inglês?',opts:shuf([t.w].concat(d.map(x=>x.w))),ans:t.w,word:t}}
const pickB=(p,used)=>{const c=p.B.filter(b=>b.opts.length>=3&&!used.has(b.en));if(!c.length)return null;const b=rnd(c);used.add(b.en);return b};
function itemGap(p,used){const b=pickB(p,used);if(!b)return null;const o=rnd(b.opts.slice(1));
  return {k:'mc',skill:'pat',q:'Complete a frase em inglês:',sub:fill(b.pt,o[1]),en:b.en.replace('{0}','＿＿＿'),opts:shuf(b.opts.map(x=>x[0])),ans:o[0],pat:b.en}}
function itemListen(p,used){const b=pickB(p,used);if(!b)return null;const o=rnd(b.opts.slice(1));
  const os=shuf(b.opts).slice(0,3);if(!os.some(x=>x[0]===o[0]))os[0]=o;
  return {k:'mc',skill:'listen',q:'Ouça e escolha o que a frase quer dizer.',say:fill(b.en,o[0]),opts:shuf(os.map(x=>fill(b.pt,x[1]))),ans:fill(b.pt,o[1]),pat:b.en}}
function itemOrder(p,used){for(let i=0;i<8;i++){const b=pickB(p,used);if(!b)return null;const o=rnd(b.opts.slice(1));const s=fill(b.en,o[0]);const tk=s.split(/\s+/);
    if(tk.length>=3&&tk.length<=9)return {k:'order',skill:'pat',q:'Monte a frase na ordem certa.',sub:fill(b.pt,o[1]),say:null,toks:shuf(tk),ans:s,pat:b.en}}return null}
function makeExam(cid,k,weakOnly){
  const eps=weakOnly?avail(cid).filter(e=>isDone(cid,e)):block(cid,k),p=poolOf(eps),used=new Set(),items=[];
  if(weakOnly){const wk=Object.values(get('weak',{})).filter(x=>x.cid===cid);
    shuf(wk).slice(0,8).forEach(w=>{const t=p.V.find(v=>v.w.toLowerCase()===w.w.toLowerCase())||{w:w.w,pt:w.pt};
      const a=itemVoc(p,used,t);if(a)items.push(a);const b=itemRev(p,used,t);if(b&&items.length<12)items.push(b)});
    return items}
  const plan=[['voc',5],['rev',3],['gap',3],['listen',3],['order',2]];
  plan.forEach(([t,n])=>{for(let i=0;i<n;i++){const it=t==='voc'?itemVoc(p,used):t==='rev'?itemRev(p,used):t==='gap'?itemGap(p,used):t==='listen'?itemListen(p,used):itemOrder(p,used);if(it)items.push(it)}});
  return shuf(items)}
const SK={vocab:'Vocabulário',pat:'Padrões de frase',listen:'Compreensão auditiva'};
const getExams=cid=>get('exams',[]).filter(e=>e.cid===cid);
function saveExam(cid,k,res,weakOnly){
  const weak=get('weak',{});
  res.forEach(r=>{if(!r.word)return;const key=cid+'|'+r.word.w.toLowerCase();
    if(r.ok){if(weak[key]){weak[key].c--;if(weak[key].c<=0)delete weak[key]}}
    else{weak[key]=weak[key]||{cid,w:r.word.w,pt:r.word.pt,c:0};weak[key].c=Math.min(5,weak[key].c+1)}});
  put('weak',weak);
  const by={};res.forEach(r=>{const s=by[r.skill]=by[r.skill]||[0,0];s[1]++;if(r.ok)s[0]++});
  const rec={cid,block:k,ts:Date.now(),ok:res.filter(r=>r.ok).length,tot:res.length,by,weakOnly:!!weakOnly,pats:res.filter(r=>!r.ok&&r.pat).map(r=>r.pat)};
  if(!weakOnly){const all=get('exams',[]);all.push(rec);put('exams',all)}
  return rec}

/* ───────── métricas e prognóstico ───────── */
function metrics(cid){
  const eps=avail(cid),total=eps.length,done=eps.filter(e=>isDone(cid,e)).length,progress=total?done/total:0;
  const stats=epStats(cid),sv=Object.values(stats).sort((a,b)=>a.ts-b.ts);
  const exams=getExams(cid).sort((a,b)=>a.ts-b.ts),last=exams.slice(-3);
  const score=e=>e.ok/e.tot;
  const acc=last.length?avg(last.map(score)):null;
  const slope=last.length>=2?(score(last[last.length-1])-score(last[0]))/(last.length-1):0;
  const projNext=acc==null?null:Math.round(clamp(score(last[last.length-1])+slope*0.6,0,1)*100);
  const skills={};exams.slice(-3).forEach(e=>Object.entries(e.by).forEach(([s,v])=>{const x=skills[s]=skills[s]||[0,0];x[0]+=v[0];x[1]+=v[1]}));
  const eng={voc:avg(sv.filter(s=>s.vt).map(s=>s.voc/s.vt)),build:avg(sv.filter(s=>s.bt).map(s=>s.b/s.bt)),dl:avg(sv.map(s=>clamp(s.dl/6,0,1))),
    speakOk:sv.reduce((a,s)=>a+s.sp,0),speakSkip:sv.reduce((a,s)=>a+s.sk,0)};
  const now=Date.now(),rec14=sv.filter(s=>now-s.ts<=14*DAY).length;
  const pl=getPlan(cid),planPace=pl?weeklyEps(pl):null;
  const pace=rec14>=2?rec14/2:(planPace||null),remaining=total-done;
  const daysSince=sv.length?Math.floor((now-sv[sv.length-1].ts)/DAY):null;
  const eta=(wk)=>wk&&remaining>0?new Date(today().getTime()+Math.ceil(remaining/wk*7)*DAY):null;
  const readiness=Math.round(100*(0.55*progress+0.45*(acc==null?progress*0.8:acc)));
  return {eps,total,done,progress,exams,acc,slope,projNext,skills,eng,pace,planPace,remaining,daysSince,eta,readiness,rec14,hasStats:sv.length>0}}
const readLabel=r=>r<40?'Construindo a base':r<70?'Em consolidação':r<85?'Quase lá':'Pronto para o próximo nível';
function advice(cid,m){
  const out=[],pc=x=>Math.round(x*100);
  const sk=Object.entries(m.skills).filter(([,v])=>v[1]>=3).map(([s,v])=>[s,v[0]/v[1]]).sort((a,b)=>a[1]-b[1]);
  if(!m.exams.length)out.push('Faça o primeiro exame assim que concluir os 20 primeiros episódios: ele calibra o seu prognóstico.');
  if(sk.length&&sk[0][1]<0.7)out.push('Ponto mais fraco: '+SK[sk[0][0]].toLowerCase()+' ('+pc(sk[0][1])+'%). Revise os episódios do bloco e use a revisão espaçada antes do próximo exame.');
  if(sk.length&&sk[sk.length-1][1]>=0.85)out.push('Ponto forte: '+SK[sk[sk.length-1][0]].toLowerCase()+' ('+pc(sk[sk.length-1][1])+'%). Continue assim.');
  const wk=Object.values(get('weak',{})).filter(x=>x.cid===cid);
  if(wk.length>=3)out.push('Você tem '+wk.length+' palavras para reforçar. Faça o treino rápido de palavras fracas (abaixo) antes de seguir.');
  const sp=m.eng.speakOk+m.eng.speakSkip;
  if(sp>=4&&m.eng.speakSkip/sp>0.4)out.push('Você pulou '+pc(m.eng.speakSkip/sp)+'% das atividades de fala. Falar em voz alta é o que mais acelera a fluência: tente não pular.');
  if(m.hasStats&&m.eng.voc<0.7)out.push('Você abre só '+pc(m.eng.voc)+'% das figuras do vocabulário. Tocar em todas ajuda a fixar as palavras.');
  if(m.daysSince!=null&&m.daysSince>=4)out.push('Faz '+m.daysSince+' dias desde o último episódio. Estudar um pouco todo dia vale mais do que muito de uma vez.');
  const ps=planStatus(cid);if(ps&&ps.diff<=-2)out.push('Você está '+(-ps.diff)+' episódios atrás do plano. Considere um ritmo mais leve para manter a constância.');
  if(ps&&ps.diff>=2)out.push('Você está '+ps.diff+' episódios à frente do plano. Que tal subir o ritmo?');
  if(!out.length)out.push('Tudo certo por aqui. Continue no seu ritmo e faça o próximo exame no fim do bloco.');
  return out}

/* ───────── interface ───────── */
let root=null,cur={cid:null,tab:'plan'};
function ensureRoot(){if(root&&document.body.contains(root))return root;root=document.createElement('div');root.id='pkp';root.setAttribute('role','dialog');root.setAttribute('aria-label','Plano e desempenho');document.body.appendChild(root);document.body.style.overflow='hidden';return root}
function close(){try{if(typeof fxStopAudio==='function')fxStopAudio()}catch(e){}if(root){root.remove();root=null}document.body.style.overflow=''}
const speakTxt=t=>{try{if(typeof fxStopAudio==='function')fxStopAudio();if(typeof fxSay==='function')fxSay(t)}catch(e){}};
function head(cid,tab){
  const cs=courses();
  return '<header class="pkp-h"><button type="button" class="pkp-x" data-act="close" aria-label="Fechar">✕</button><div><small>🎒 Pocket</small><h2>Plano e desempenho</h2></div>'+
   (cs.length>1?'<select id="pkp-c" aria-label="Curso">'+cs.map(c=>'<option value="'+c+'"'+(c===cid?' selected':'')+'>'+H(cname(c))+'</option>').join('')+'</select>':'')+'</header>'+
   '<nav class="pkp-t">'+[['plan','🗓️ Plano'],['exams','📝 Exames'],['report','📊 Relatório']].map(([k,l])=>'<button type="button" data-tab="'+k+'"'+(k===tab?' class="on"':'')+'>'+l+'</button>').join('')+'</nav>'}
function paint(html){const r=ensureRoot();r.innerHTML=html;r.scrollTop=0;
  r.querySelectorAll('[data-act="close"]').forEach(b=>b.onclick=close);
  const sel=r.querySelector('#pkp-c');if(sel)sel.onchange=()=>open(sel.value,cur.tab);
  r.querySelectorAll('[data-tab]').forEach(b=>b.onclick=()=>open(cur.cid,b.dataset.tab))}
function open(cid,tab){
  const cs=courses();cid=cid&&cs.includes(cid)?cid:(cs.includes(cur.cid)?cur.cid:(cs[0]||null));if(!cid)return;
  cur={cid,tab:tab||'plan'};
  const go=()=>{const body=cur.tab==='exams'?examsTab(cid):cur.tab==='report'?reportTab(cid):planTab(cid);paint('<div class="pkp-box">'+head(cid,cur.tab)+'<div class="pkp-b">'+body.html+'</div></div>');body.bind&&body.bind(root)};
  if(typeof ensureLangLoaded==='function'&&(!EP[cid]||!EP[cid].length))ensureLangLoaded(cid).then(go);else go()}

/* — plano — */
let draft=null;
function planTab(cid){
  const pl=getPlan(cid),m=metrics(cid);
  if(!draft||draft.cid!==cid){draft=pl?{cid,pace:pl.pace,days:pl.days.slice(),min:pl.min||20}:{cid,pace:'regular',days:[1,2,3,4,5],min:20}}
  const am=avgMin(cid);
  const cfg=()=>{const pr=PRESETS.find(x=>x.id===draft.pace);const days=draft.pace==='custom'?(draft.days.length?draft.days:[1]):pr.days;
    const per=draft.pace==='custom'?Math.max(1,Math.round(draft.min/am)):pr.per;return {pace:draft.pace,days,per,min:draft.min}};
  const render=()=>{const c=cfg(),ss=buildSessions(cid,c),last=ss[ss.length-1],wk=weeklyEps(c);
    const weeks=new Map();ss.forEach(s=>{const k=iso(weekStart(s.date));(weeks.get(k)||weeks.set(k,[]).get(k)).push(s)});
    const wl=[...weeks.entries()],show=wl.slice(0,6);
    const ps=planStatus(cid);
    return '<section class="pkp-card">'+(m.remaining===0?'<p class="pkp-ok">🎉 Você concluiu todos os episódios disponíveis deste curso.</p>':
     '<h3>Escolha o seu ritmo</h3><div class="pkp-pace">'+PRESETS.map(p=>'<button type="button" data-pace="'+p.id+'" class="'+(draft.pace===p.id?'on':'')+'"><b>'+p.n+'</b><small>'+p.d+'</small></button>').join('')+'</div>'+
     '<div class="pkp-days"><span>Dias de estudo</span>'+DN.map((n,i)=>{const on=(draft.pace==='custom'?draft.days:PRESETS.find(x=>x.id===draft.pace).days).includes(i);return '<button type="button" data-day="'+i+'" class="'+(on?'on':'')+'"'+(draft.pace==='custom'?'':' disabled')+'>'+n+'</button>'}).join('')+'</div>'+
     (draft.pace==='custom'?'<label class="pkp-min">Minutos por dia: <b id="pkp-mv">'+draft.min+'</b><input type="range" id="pkp-m" min="10" max="90" step="5" value="'+draft.min+'"></label><p class="pkp-n">Seu episódio leva em média '+am+' min'+(Object.keys(epStats(cid)).length>=3?' (medido)':' (estimado)')+'. Isso dá '+c.per+' episódio'+(c.per>1?'s':'')+' por dia de estudo.</p>':'')+
     '<div class="pkp-sum"><div><b>'+wk+'</b><small>episódios/semana</small></div><div><b>'+(wk*am/60).toFixed(1).replace('.',',')+' h</b><small>por semana</small></div><div><b>'+(last?fdate(last.date):'—')+'</b><small>previsão de término</small></div><div><b>'+ss.filter(s=>s.exam!=null).length+'</b><small>exames no caminho</small></div></div>'+
     (last?'<p class="pkp-n">Terminando '+m.remaining+' episódios restantes em cerca de <b>'+Math.ceil(ss.length/c.days.length)+' semanas</b>, até '+fdateL(last.date)+'.</p>':'')+
     '<button type="button" class="pkp-go" id="pkp-save">'+(pl?'Atualizar meu plano':'Começar com este plano')+'</button>')+'</section>'+
     (ps?'<section class="pkp-card"><h3>Seu plano hoje</h3><div class="pkp-st '+(ps.diff<0?'late':ps.diff>0?'ahead':'ok')+'"><b>'+(ps.diff===0?'No ritmo':ps.diff>0?ps.diff+' à frente':(-ps.diff)+' atrás')+'</b><span>'+ps.done+' concluídos · esperado até hoje: '+ps.expected+'</span></div></section>':'')+
     '<section class="pkp-card"><h3>Calendário</h3>'+(show.length?show.map(([k,arr],wi)=>'<div class="pkp-wk"><b>Semana '+(wi+1)+' · '+fdate(fromIso(k))+'</b>'+arr.map(s=>'<div class="pkp-ss"><span>'+DN[s.date.getDay()]+' '+fdate(s.date)+'</span><span>ep. '+(s.from===s.to?s.from:s.from+'–'+s.to)+'</span>'+(s.exam!=null?'<em>📝 Exame '+(s.exam+1)+'</em>':'')+'</div>').join('')+'</div>').join('')+(wl.length>show.length?'<p class="pkp-n">+ '+(wl.length-show.length)+' semanas seguintes no mesmo ritmo.</p>':''):'<p class="pkp-n">Nada pendente.</p>')+'</section>'};
  return {html:'<div id="pkp-plan">'+render()+'</div>',bind:r=>{
    const re=()=>{r.querySelector('#pkp-plan').innerHTML=render();wire()};
    const wire=()=>{
      r.querySelectorAll('[data-pace]').forEach(b=>b.onclick=()=>{draft.pace=b.dataset.pace;re()});
      r.querySelectorAll('[data-day]').forEach(b=>b.onclick=()=>{const d=+b.dataset.day,i=draft.days.indexOf(d);if(i<0)draft.days.push(d);else if(draft.days.length>1)draft.days.splice(i,1);re()});
      const m=r.querySelector('#pkp-m');if(m)m.oninput=()=>{draft.min=+m.value;r.querySelector('#pkp-mv').textContent=m.value};if(m)m.onchange=re;
      const sv=r.querySelector('#pkp-save');if(sv)sv.onclick=()=>{const c=cfg(),n=avail(cid).filter(e=>isDone(cid,e)).length;
        put('plan:'+cid,{pace:c.pace,days:c.days,per:c.per,min:c.min,start:iso(today()),done0:n});re();try{sfx('win')}catch(e){}}};
    wire()}}}

/* — exames — */
function examsTab(cid){
  const nb=nBlocks(cid),ex=getExams(cid),m=metrics(cid);
  let rows='';
  for(let k=0;k<nb;k++){
    const b=block(cid,k),dn=b.filter(e=>isDone(cid,e)).length,ok=blockDone(cid,k),tries=ex.filter(e=>e.block===k),best=tries.length?Math.max(...tries.map(e=>Math.round(100*e.ok/e.tot))):null;
    rows+='<div class="pkp-ex '+(ok?'open':'lock')+'"><div><b>Exame '+(k+1)+'</b><small>episódios '+(k*20+1)+'–'+(k*20+b.length)+(ok?'':' · '+dn+'/'+b.length+' concluídos')+'</small></div>'+
     (best!=null?'<span class="pkp-bd '+(best>=75?'g':best>=55?'y':'r')+'">'+best+'%</span>':'')+
     '<button type="button" '+(ok?'data-exam="'+k+'"':'disabled')+'>'+(ok?(tries.length?'Refazer':'Fazer exame'):'🔒')+'</button></div>'}
  const wk=Object.values(get('weak',{})).filter(x=>x.cid===cid);
  return {html:'<section class="pkp-card"><h3>Exames de 20 em 20</h3><p class="pkp-n">Cada exame tem cerca de 16 questões sobre o vocabulário e os padrões do bloco, em situações novas: nunca repete as falas dos diálogos. Cada refação traz questões diferentes. Ele alimenta o seu relatório e o seu prognóstico.</p>'+rows+'</section>'+
    '<section class="pkp-card"><h3>Treino de palavras fracas</h3>'+(wk.length>=4?'<p class="pkp-n">'+wk.length+' palavras precisam de reforço.</p><button type="button" class="pkp-go" data-weak="1">Treinar agora</button>':'<p class="pkp-n">Quando o exame mostrar palavras para reforçar, elas aparecem aqui para um treino rápido.</p>')+'</section>',
    bind:r=>{r.querySelectorAll('[data-exam]').forEach(b=>b.onclick=()=>run(cid,+b.dataset.exam,false));const w=r.querySelector('[data-weak]');if(w)w.onclick=()=>run(cid,0,true)}}}

function run(cid,k,weakOnly){
  const items=makeExam(cid,k,weakOnly);
  if(items.length<5){paint('<div class="pkp-box">'+head(cid,'exams')+'<div class="pkp-b"><section class="pkp-card"><p class="pkp-n">Ainda não há conteúdo suficiente para montar este exame.</p></section></div></div>');return}
  const res=[];let i=0;
  const step=()=>{
    if(i>=items.length)return finish();
    const it=items[i];
    paint('<div class="pkp-box pkp-run"><header class="pkp-h"><button type="button" class="pkp-x" data-act="close" aria-label="Sair">✕</button><div><small>'+(weakOnly?'Treino de palavras fracas':'Exame '+(k+1))+'</small><h2>Questão '+(i+1)+' de '+items.length+'</h2></div></header><div class="pkp-prog"><i style="width:'+Math.round(i/items.length*100)+'%"></i></div>'+
     '<div class="pkp-b"><section class="pkp-card pkp-q"><small class="pkp-sk">'+SK[it.skill]+'</small><h3>'+H(it.q)+'</h3>'+(it.sub?'<p class="pkp-sub">'+H(it.sub)+'</p>':'')+(it.en?'<p class="pkp-en">'+H(it.en)+'</p>':'')+
     (it.say?'<button type="button" class="pkp-say" id="pkp-s">🔊 Ouvir</button>':'')+
     (it.k==='mc'?'<div class="pkp-o">'+it.opts.map((o,j)=>'<button type="button" data-o="'+j+'">'+H(o)+'</button>').join('')+'</div>':
      '<div class="pkp-ans" id="pkp-a"></div><div class="pkp-tk" id="pkp-t">'+it.toks.map((t,j)=>'<button type="button" data-t="'+j+'">'+H(t)+'</button>').join('')+'</div><div class="pkp-ctl"><button type="button" id="pkp-u">↩ Desfazer</button><button type="button" id="pkp-ok" class="pkp-go">Conferir</button></div>')+
     '<div id="pkp-fb"></div></section></div></div>');
    const r=root,done=(ok,show)=>{res.push({ok,skill:it.skill,word:it.word,pat:it.pat});
      r.querySelector('#pkp-fb').innerHTML='<div class="pkp-fb '+(ok?'g':'r')+'"><b>'+(ok?'✔ Certo!':'✖ Não foi dessa vez')+'</b>'+(ok?'':'<span>Resposta: '+H(show)+'</span>')+'</div><button type="button" class="pkp-go" id="pkp-n">'+(i+1<items.length?'Próxima':'Ver resultado')+'</button>';
      r.querySelector('#pkp-n').onclick=()=>{i++;step()};try{sfx(ok?'step':'pop')}catch(e){}};
    const sb=r.querySelector('#pkp-s');if(sb){sb.onclick=()=>speakTxt(it.say);setTimeout(()=>speakTxt(it.say),350)}
    if(it.k==='mc'){r.querySelectorAll('[data-o]').forEach(b=>b.onclick=()=>{const v=it.opts[+b.dataset.o],ok=v===it.ans;
      r.querySelectorAll('[data-o]').forEach(x=>{x.disabled=true;if(it.opts[+x.dataset.o]===it.ans)x.classList.add('ok')});if(!ok)b.classList.add('bad');done(ok,it.ans)})}
    else{const pick=[];const aEl=r.querySelector('#pkp-a');
      const draw=()=>{aEl.innerHTML=pick.map(j=>'<span>'+H(it.toks[j])+'</span>').join('');r.querySelectorAll('[data-t]').forEach(b=>b.disabled=pick.includes(+b.dataset.t))};
      r.querySelectorAll('[data-t]').forEach(b=>b.onclick=()=>{pick.push(+b.dataset.t);draw()});
      r.querySelector('#pkp-u').onclick=()=>{pick.pop();draw()};
      r.querySelector('#pkp-ok').onclick=()=>{if(pick.length<it.toks.length)return;const s=pick.map(j=>it.toks[j]).join(' '),ok=s===it.ans;
        r.querySelectorAll('.pkp-tk button,.pkp-ctl button').forEach(x=>x.disabled=true);done(ok,it.ans)}}};
  const finish=()=>{const rec=saveExam(cid,k,res,weakOnly),pct=Math.round(100*rec.ok/rec.tot);
    const bars=Object.entries(rec.by).map(([s,v])=>{const p=Math.round(100*v[0]/v[1]);return '<div class="pkp-bar"><span>'+SK[s]+'</span><div><i class="'+(p>=75?'g':p>=55?'y':'r')+'" style="width:'+p+'%"></i></div><b>'+p+'%</b></div>'}).join('');
    const wrong=res.filter(r=>!r.ok&&r.word).map(r=>r.word);
    paint('<div class="pkp-box">'+head(cid,'exams')+'<div class="pkp-b"><section class="pkp-card pkp-res"><div class="pkp-big '+(pct>=75?'g':pct>=55?'y':'r')+'">'+pct+'%</div><h3>'+(pct>=85?'Excelente!':pct>=75?'Muito bem!':pct>=55?'Bom caminho':'Vale reforçar o bloco')+'</h3><p class="pkp-n">'+rec.ok+' de '+rec.tot+' questões certas.</p>'+bars+
     (wrong.length?'<h4>Palavras para reforçar</h4><div class="pkp-chips">'+[...new Map(wrong.map(w=>[w.w,w])).values()].map(w=>'<span>'+H(w.w)+' · '+H(w.pt)+'</span>').join('')+'</div>':'')+
     '<div class="pkp-ctl"><button type="button" class="pkp-go" id="pkp-rep">📊 Ver relatório</button><button type="button" id="pkp-bk">Voltar aos exames</button></div></section></div></div>');
    root.querySelector('#pkp-rep').onclick=()=>open(cid,'report');root.querySelector('#pkp-bk').onclick=()=>open(cid,'exams');
    if(pct>=75&&!weakOnly){try{if(window.confetti)confetti(70)}catch(e){}}};
  step()}

/* — relatório — */
function spark(vals){if(vals.length<2)return '';const w=240,h=56,p=6;
  const pts=vals.map((v,i)=>[p+i*(w-2*p)/(vals.length-1),h-p-v*(h-2*p)/100]);
  return '<svg class="pkp-sp" viewBox="0 0 '+w+' '+h+'" role="img" aria-label="Evolução nos exames"><polyline fill="none" stroke="currentColor" stroke-width="2.5" points="'+pts.map(x=>x.join(',')).join(' ')+'"/>'+pts.map(x=>'<circle cx="'+x[0]+'" cy="'+x[1]+'" r="3.5" fill="currentColor"/>').join('')+'</svg>'}
function reportTab(cid){
  const m=metrics(cid),ps=planStatus(cid),pc=x=>Math.round(x*100);
  const circ=2*Math.PI*34,off=circ*(1-m.readiness/100);
  const skills=Object.entries(m.skills).filter(([,v])=>v[1]).map(([s,v])=>{const p=pc(v[0]/v[1]);return '<div class="pkp-bar"><span>'+SK[s]+'</span><div><i class="'+(p>=75?'g':p>=55?'y':'r')+'" style="width:'+p+'%"></i></div><b>'+p+'%</b></div>'}).join('');
  const sp=m.eng.speakOk+m.eng.speakSkip;
  const eng=m.hasStats?'<div class="pkp-bar"><span>Vocabulário explorado</span><div><i class="b" style="width:'+pc(m.eng.voc)+'%"></i></div><b>'+pc(m.eng.voc)+'%</b></div><div class="pkp-bar"><span>Frases montadas</span><div><i class="b" style="width:'+pc(m.eng.build)+'%"></i></div><b>'+pc(m.eng.build)+'%</b></div><div class="pkp-bar"><span>Fala (sem pular)</span><div><i class="b" style="width:'+(sp?pc(m.eng.speakOk/sp):0)+'%"></i></div><b>'+(sp?pc(m.eng.speakOk/sp)+'%':'—')+'</b></div>':'<p class="pkp-n">Conclua alguns episódios para ver seu engajamento.</p>';
  const scen=[];
  if(m.remaining>0){
    const mk=(n,wk)=>{const d=m.eta(wk);if(d)scen.push('<div class="pkp-sc"><span>'+n+'</span><b>'+(wk%1?wk.toFixed(1):wk)+' ep./semana</b><em>'+fdateL(d)+'</em></div>')};
    if(m.pace)mk('No seu ritmo atual',m.pace);if(m.planPace&&m.planPace!==m.pace)mk('Seguindo o plano',m.planPace);if(m.pace)mk('Com +2 episódios por semana',m.pace+2)}
  const ready=m.progress>=0.9&&m.acc!=null&&m.acc>=0.75;
  const prog=[];
  if(m.remaining===0)prog.push(m.acc==null?'Você concluiu o nível. Faça os exames para confirmar a sua prontidão.':(m.acc>=0.75?'Você concluiu o nível com bom desempenho: está pronto para avançar.':'Você concluiu o nível, mas o desempenho nos exames pede reforço antes de avançar.'));
  else if(m.pace){const d=m.eta(m.pace);prog.push('Mantendo cerca de '+(m.pace%1?m.pace.toFixed(1):m.pace)+' episódios por semana, você conclui o '+lvlOf(cid)+' por volta de '+fdateL(d)+'.')}
  else prog.push('Estude alguns dias seguidos ou monte o seu plano para eu estimar a data de conclusão.');
  if(m.projNext!=null)prog.push('Projeção para o próximo exame: cerca de '+clamp(m.projNext-5,0,100)+'–'+clamp(m.projNext+5,0,100)+'%'+(m.slope>0.02?' (tendência de alta).':m.slope<-0.02?' (tendência de queda: vale reforçar).':' (estável).'));
  prog.push('Prontidão para o próximo nível: '+m.readiness+'% · '+readLabel(m.readiness)+(ready?' ✔':'')+'.');
  const wk=Object.values(get('weak',{})).filter(x=>x.cid===cid).sort((a,b)=>b.c-a.c).slice(0,10);
  const ex=m.exams.map(e=>Math.round(100*e.ok/e.tot));
  return {html:'<section class="pkp-card pkp-top"><svg class="pkp-ring" viewBox="0 0 80 80"><circle cx="40" cy="40" r="34" fill="none" stroke="rgba(0,0,0,.1)" stroke-width="8"/><circle cx="40" cy="40" r="34" fill="none" stroke="currentColor" stroke-width="8" stroke-linecap="round" stroke-dasharray="'+circ.toFixed(1)+'" stroke-dashoffset="'+off.toFixed(1)+'" transform="rotate(-90 40 40)"/><text x="40" y="46" text-anchor="middle" font-size="19" font-weight="800" fill="currentColor">'+m.readiness+'%</text></svg><div><h3>'+readLabel(m.readiness)+'</h3><p class="pkp-n">'+m.done+' de '+m.total+' episódios do '+lvlOf(cid)+' concluídos ('+pc(m.progress)+'%).'+(m.acc!=null?' Média recente nos exames: '+pc(m.acc)+'%.':'')+'</p></div></section>'+
    '<section class="pkp-card"><h3>Habilidades</h3>'+(skills||'<p class="pkp-n">Os exames medem vocabulário, padrões de frase e compreensão auditiva. Faça o primeiro para ver seu perfil.</p>')+'<h4>Engajamento nos episódios</h4>'+eng+'</section>'+
    (ex.length?'<section class="pkp-card"><h3>Evolução nos exames</h3>'+(ex.length>1?'<div class="pkp-spw">'+spark(ex)+'</div>':'')+'<p class="pkp-n">'+ex.map((v,i)=>'#'+(i+1)+': '+v+'%').join(' · ')+'</p></section>':'')+
    '<section class="pkp-card"><h3>Prognóstico</h3>'+prog.map(t=>'<p class="pkp-pg">'+H(t)+'</p>').join('')+(scen.length?'<h4>Cenários de conclusão</h4>'+scen.join(''):'')+'</section>'+
    '<section class="pkp-card"><h3>Feedback do seu desempenho</h3><ul class="pkp-adv">'+advice(cid,m).map(t=>'<li>'+H(t)+'</li>').join('')+'</ul></section>'+
    (wk.length?'<section class="pkp-card"><h3>Palavras para reforçar</h3><div class="pkp-chips">'+wk.map(w=>'<button type="button" data-say="'+H(w.w)+'">🔊 '+H(w.w)+' · '+H(w.pt)+'</button>').join('')+'</div></section>':''),
    bind:r=>r.querySelectorAll('[data-say]').forEach(b=>b.onclick=()=>speakTxt(b.dataset.say))}}

/* ───────── entradas no app ───────── */
function bannerHTML(cid){
  const nb=nBlocks(cid);let nextEx=-1;for(let k=0;k<nb;k++){const t=getExams(cid).filter(e=>e.block===k);if(blockDone(cid,k)&&!t.length){nextEx=k;break}}
  const ps=planStatus(cid),m=metrics(cid);
  const line=nextEx>=0?'📝 O Exame '+(nextEx+1)+' está liberado!':ps?(ps.diff===0?'Você está no ritmo do seu plano.':ps.diff>0?'Você está '+ps.diff+' episódio(s) à frente do plano.':'Você está '+(-ps.diff)+' episódio(s) atrás do plano.'):'Escolha seu ritmo e receba um plano, exames e relatório.';
  return '<section class="srs-banner pkp-banner"><div><b>🧭 Plano e desempenho</b><p>'+H(line)+(m.exams.length?' Prontidão: '+m.readiness+'%.':'')+'</p></div><button class="pill light" data-pkplan="'+cid+'" data-pktab="'+(nextEx>=0?'exams':'plan')+'">Abrir</button></section>'}
const _course=window.course;
if(typeof _course==='function')window.course=function(id){const r=_course.apply(this,arguments);
  try{if(id&&/^pk-/.test(String(id))&&EP[id]&&EP[id].length){document.querySelectorAll('.pkp-banner').forEach(x=>x.remove());
    const at=document.querySelector('.p2tools')||document.querySelector('.ep-search');
    if(at)at.insertAdjacentHTML('beforebegin',bannerHTML(id))}}catch(e){}
  return r};
document.addEventListener('click',e=>{const b=e.target.closest&&e.target.closest('[data-pkplan]');if(b){e.preventDefault();open(b.dataset.pkplan,b.dataset.pktab||'plan')}});

/* tela de resultado do episódio: grava estatísticas e oferece o exame quando o bloco fecha */
setInterval(()=>{
  try{if(typeof P==='undefined'||!P||!/^pk-/.test(String(P.cid))||P.pkdone)return;
    const dn=document.querySelector('#pstage .step.done');if(!dn)return;P.pkdone=true;recordEpisode();
    const cid=P.cid,eps=avail(cid),idx=eps.findIndex(e=>e.n===P.e.n),k=Math.floor(idx/20),nb=nBlocks(cid);
    let html;
    if(k<nb&&blockDone(cid,k)&&!getExams(cid).some(e=>e.block===k))html='<section class="pkp-dn"><b>📝 Exame '+(k+1)+' liberado!</b><span>Você concluiu os episódios '+(k*20+1)+'–'+Math.min(eps.length,k*20+20)+'. Hora de testar o que aprendeu.</span><button type="button" class="pkp-dnb" data-pkplan="'+cid+'" data-pktab="exams">Fazer o exame</button></section>';
    else{const left=Math.min(20-((idx+1)%20||20),eps.length-idx-1);html='<section class="pkp-dn"><b>🧭 '+(left>0?'Faltam '+left+' para o próximo exame':'Plano e desempenho')+'</b><span>Veja seu plano, seu relatório e o prognóstico.</span><button type="button" class="pkp-dnb" data-pkplan="'+cid+'" data-pktab="report">Ver relatório</button></section>'}
    const row=dn.querySelector('.row')||dn.querySelector('.big');if(row)row.insertAdjacentHTML('afterend',html)}catch(x){}},600);

window.PKPlan={open,close,metrics,makeExam,buildSessions,_get:get,_put:put};
})();
