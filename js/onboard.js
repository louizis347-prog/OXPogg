/* Primeira experiência: 3 perguntas (idioma, nível, meta) e o primeiro episódio já aberto.
   Só aparece para quem ainda não tem nenhum progresso e nunca viu esta tela. */
(function(){
const K='pogglot:onb';
const seen=()=>{try{return !!localStorage.getItem(K)}catch(e){return true}};
const mark=()=>{try{localStorage.setItem(K,'1')}catch(e){}};
const LANGS=[
 ['en','🇺🇸','Inglês','en-a1','en-a2'],
 ['es','🇪🇸','Espanhol','es-a1','es-a2'],
 ['fr','🇫🇷','Francês','fr','fr'],
 ['de','🇩🇪','Alemão','de','de'],
 ['it','🇮🇹','Italiano','it','it'],
 ['ja','🇯🇵','Japonês','nbja-a1','nbja-a2']];
const LEVELS=[['zero','🌱','Do zero','Nunca estudei ou quase nada'],['pouco','🌿','Já sei um pouco','Entendo frases simples']];
const GOALS=[[10,'☕','5 min por dia','Leve, para criar o hábito'],[20,'🚶','10 min por dia','Um episódio por dia'],[40,'🏃','20 min por dia','Ritmo de quem quer fluência']];
const OBJECTIVES=[['💬','Conversar','Quero me virar em situações reais'],['🧭','Viajar','Quero viajar com mais confiança'],['🎓','Estudar ou trabalhar','Quero alcançar uma meta acadêmica ou profissional'],['🎬','Cultura','Quero aprender por filmes, livros e histórias']];
const STYLES=[['🗣️','Conversação','Priorize o curso Neighbors'],['📚','Estrutura','Priorize o curso Regular'],['🌎','Uma combinação','Comece pelo Regular e experimente o Neighbors']];
const css=`#onb{position:fixed;inset:0;z-index:2147483000;display:flex;align-items:center;justify-content:center;padding:16px;background:rgba(30,20,70,.55);backdrop-filter:blur(6px);font-family:var(--f-body,system-ui,sans-serif)}
#onb .ob{width:min(460px,100%);max-height:100%;overflow:auto;background:#fff;border-radius:24px;padding:22px 20px 18px;box-shadow:0 24px 60px rgba(30,20,70,.35);text-align:center}
#onb .ob-dots{display:flex;justify-content:center;gap:6px;margin-bottom:12px}
#onb .ob-dots i{width:26px;height:5px;border-radius:5px;background:#E6E1F5}
#onb .ob-dots i.on{background:var(--river,#7C4DFF)}
#onb h2{font-family:var(--f-display,inherit);font-size:22px;margin:0 0 4px;color:#241B4B}
#onb p{margin:0 0 14px;color:#6B6590;font-size:14px}
#onb .ob-opts{display:grid;gap:8px}
#onb .ob-opts.two{grid-template-columns:1fr 1fr}
#onb .ob-opt{display:flex;align-items:center;gap:12px;text-align:left;border:2px solid #E6E1F5;background:#fff;border-radius:16px;padding:12px 14px;font:inherit;cursor:pointer;color:#241B4B;min-height:56px}
#onb .ob-opt:hover,#onb .ob-opt:focus-visible{border-color:var(--river,#7C4DFF);background:var(--river-l,#F0EAFF);outline:0}
#onb .ob-opt i{font-style:normal;font-size:26px}
#onb .ob-opt b{display:block;font-size:15px}
#onb .ob-opt small{display:block;color:#6B6590;font-size:12px;margin-top:2px}
#onb .ob-opts.two .ob-opt{flex-direction:column;text-align:center;gap:4px;padding:14px 8px}
#onb .ob-skip{margin-top:12px;background:none;border:0;color:#8A84AC;font:inherit;font-size:13px;cursor:pointer;text-decoration:underline}
#onb .ob-go{width:100%;margin-top:6px;border:0;border-radius:16px;padding:15px;background:var(--river,#7C4DFF);color:#fff;font:inherit;font-weight:800;font-size:16px;cursor:pointer}`;
function run(){
  if(document.getElementById('onb'))return;
  const pick={};const root=document.createElement('div');root.id='onb';
  const st=document.createElement('style');st.textContent=css;root.appendChild(st);
  const box=document.createElement('div');box.className='ob';root.appendChild(box);
  document.body.appendChild(root);
  const dots=n=>`<div class="ob-dots">${[1,2,3,4,5].map(i=>`<i class="${i<=n?'on':''}"></i>`).join('')}</div>`;
  const skip='<button class="ob-skip" data-skip>Agora não, quero explorar sozinho</button>';
  const close=()=>{mark();root.remove()};
  const bind=fn=>{box.querySelectorAll('[data-i]').forEach(b=>b.onclick=()=>fn(+b.dataset.i));const s=box.querySelector('[data-skip]');if(s)s.onclick=close};
  function s1(){box.innerHTML=dots(1)+'<h2>O que você quer aprender?</h2><p>Você pode mudar quando quiser.</p><div class="ob-opts two">'+LANGS.map((l,i)=>`<button class="ob-opt" data-i="${i}"><i>${l[1]}</i><b>${l[2]}</b></button>`).join('')+'</div>'+skip;bind(i=>{pick.l=LANGS[i];s2()})}
  function s2(){box.innerHTML=dots(2)+`<h2>Qual é o seu nível em ${pick.l[2]}?</h2><p>Sem prova. É só para começar no ponto certo.</p><div class="ob-opts">`+LEVELS.map((l,i)=>`<button class="ob-opt" data-i="${i}"><i>${l[1]}</i><span><b>${l[2]}</b><small>${l[3]}</small></span></button>`).join('')+'</div>'+skip;bind(i=>{pick.v=i;s3()})}
  function s3(){box.innerHTML=dots(3)+'<h2>Qual é o seu objetivo?</h2><p>Isso ajusta as recomendações da sua trilha.</p><div class="ob-opts">'+OBJECTIVES.map((g,i)=>`<button class="ob-opt" data-i="${i}"><i>${g[0]}</i><span><b>${g[1]}</b><small>${g[2]}</small></span></button>`).join('')+'</div>'+skip;bind(i=>{pick.o=OBJECTIVES[i];s4()})}
  function s4(){box.innerHTML=dots(4)+'<h2>Quanto tempo por dia?</h2><p>Combinamos uma meta realista para começar.</p><div class="ob-opts">'+GOALS.map((g,i)=>`<button class="ob-opt" data-i="${i}"><i>${g[1]}</i><span><b>${g[2]}</b><small>${g[3]}</small></span></button>`).join('')+'</div>'+skip;bind(i=>{pick.g=GOALS[i];s5()})}
  function s5(){box.innerHTML=dots(5)+'<h2>Como você prefere aprender?</h2><p>Você poderá mudar essa escolha depois.</p><div class="ob-opts">'+STYLES.map((g,i)=>`<button class="ob-opt" data-i="${i}"><i>${g[0]}</i><span><b>${g[1]}</b><small>${g[2]}</small></span></button>`).join('')+'</div>'+skip;bind(i=>{pick.f=STYLES[i];start()})}
  function start(){
    try{localStorage.setItem('pogglot:goal',JSON.stringify({xp:pick.g[0]}));localStorage.setItem('pogglot:learningProfile',JSON.stringify({language:pick.l[0],level:pick.v?'A2':'A1',objective:pick.o[1],dailyMinutes:pick.g[0]===10?5:pick.g[0],preference:pick.f[1]}))}catch(e){}
    const cid=pick.v?pick.l[4]:pick.l[3];
    box.innerHTML=dots(3)+'<h2>Tudo pronto! 🎉</h2><p>Seu primeiro episódio é curto e já conta para a sua sequência.</p><button class="ob-go" data-go1>Começar agora</button>';
    box.querySelector('[data-go1]').onclick=async()=>{
      close();
      try{
        const c=COURSES[cid]?cid:pick.l[3];
        await ensureLangLoaded(c);
        const idx=Math.max(0,(EP[c]||[]).findIndex(e=>!e.pl&&!(e.fr&&e.fr.length===0)));
        play(c,idx);
      }catch(e){}
    };
  }
  s1();
}
function should(){
  try{
    if(seen())return false;
    if(typeof ST==='undefined')return false;
    return !(ST.xp>0)&&!Object.keys(ST.done||{}).length&&!ST.lastCourse;
  }catch(e){return false}
}
function boot(){setTimeout(()=>{if(should())run()},1200)}
if(document.readyState==='complete')boot();else addEventListener('load',boot);
window.POG_ONBOARD={run,reset(){try{localStorage.removeItem(K)}catch(e){}}};
})();
