/* Trilhas em páginas separadas: Regular, Neighbors e Pocket. Usa os mesmos data-hub / data-course do app. */
(function(){
var FAM={
 regular:{n:'Cursos Regulares',em:'📚',a:'#0B7C88',b:'#16B58F',d:'A trilha completa, do A1 ao C2, com gramática em contexto, leitura, escrita e cultura.',how:['Do A1 ao C2','Cultura de verdade','Prova e certificado de nível']},
 neighbors:{n:'Neighbors',em:'🏘️',a:'#E0703A',b:'#FFB627',d:'Aprenda conversando: personagens, cidades e situações reais para treinar respostas naturais e escuta.',how:['Conversas do dia a dia','Personagens e cidades','Escuta e fala']},
 pocket:{n:'Pocket',em:'⚡',a:'#7A4FD0',b:'#E0647E',d:'Inglês de bolso: episódios curtos de poucos minutos, com situações reais, fala primeiro e jogos.',how:['Poucos minutos por dia','Fala primeiro','Plano de estudo e testes']}};
function famOf(id){return /^pk/.test(id)?'pocket':/^nb/.test(id)?'neighbors':'regular'}
function avail(c){var ids=c.hub&&GROUPS[c.id]?GROUPS[c.id].sub:[c.id],t=0;ids.forEach(function(x){var a=EP_AVAILABLE&&EP_AVAILABLE[x];t+=a&&typeof a==='object'?(a.available||0):(EP_COUNT[x]||0)});return t}
function cards(f){return Object.keys(GROUPS).filter(function(k){return famOf(k)===f&&GROUPS[k].sub&&GROUPS[k].sub.some(function(x){return COURSES[x]})}).map(function(k){var g=GROUPS[k],c={id:k,hub:true,scene:g.scene,flag:g.flag,name:g.name,desc:g.desc};
 c.n=g.sub.reduce(function(a,x){return a+(EP_COUNT[x]||0)},0);c.d=g.sub.reduce(function(a,x){return a+doneCountFor(x)},0);c.av=avail(c);return c}).sort(function(x,y){return(y.av>0)-(x.av>0)||(y.n-x.n)})}
function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(m){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[m]})}
function card(c,i){var L=ST.homeLang,pc=(c.av||c.n)?Math.min(100,c.d/(c.av||c.n)*100):0;
 return '<button class="cg-card" '+(c.hub?'data-hub':'data-course')+'="'+c.id+'" style="animation-delay:'+(i*.05)+'s"><div class="th">'+SC.get(c.scene)+'<span class="fl">'+flagPair(c.flag)+'</span>'+(c.av?'':'<span class="soon">Em breve</span>')+'</div><div class="bd"><h3>'+esc(c.name[L]||c.name.pt)+'</h3><p>'+esc((c.desc[L]||c.desc.pt))+'</p><div class="mt"><span>'+c.d+' de '+(c.av||c.n)+' episódios</span><span>'+(c.av?'':'')+'</span></div><div class="br"><i style="width:'+pc+'%"></i></div></div></button>'}
window.catalog=function(f){f=FAM[f]?f:'regular';var m=FAM[f],L=ST.homeLang,list=cards(f);
 app.innerHTML=topbar(L)+'<main class="wrap cg cg-page" style="--a:'+m.a+';--b:'+m.b+'"><button class="back" data-go="home">← Voltar</button><section class="cg-hero"><span class="em">'+m.em+'</span><h1>'+m.n+'</h1><p>'+m.d+'</p><div class="cg-how">'+m.how.map(function(x){return'<span>'+x+'</span>'}).join('')+'</div></section><div class="cg-tabs" role="group" aria-label="Trilhas">'+Object.keys(FAM).map(function(k){return'<button type="button" data-fam="'+k+'" aria-pressed="'+(k===f)+'">'+FAM[k].em+' '+FAM[k].n+'</button>'}).join('')+'</div><section class="cg-grid">'+list.map(card).join('')+'</section></main>';
 scrollTo(0,0)};
function famCards(){return '<div class="cg-fams cg">'+Object.keys(FAM).map(function(k){var m=FAM[k],n=cards(k).reduce(function(a,c){return a+c.av},0);
 return '<button class="cg-fam" data-fam="'+k+'" style="--a:'+m.a+';--b:'+m.b+'"><span class="em">'+m.em+'</span><b>'+m.n+'</b><span class="d">'+m.d+'</span><span class="go">'+n.toLocaleString('pt-BR')+' episódios · Abrir →</span></button>'}).join('')+'</div>'}
function patch(){var l=document.querySelector('.px-sec .px-langs');if(!l||document.querySelector('.cg-fams'))return;
 try{var s=l.closest('.px-sec'),h=s.querySelector('h2'),p=s.querySelector('.p2sh p'),b=s.querySelector('.p2link');
  if(h)h.textContent='Escolha sua trilha';if(p)p.textContent='Três jeitos de aprender. Cada um tem a sua página.';if(b)b.style.display='none';
  l.insertAdjacentHTML('afterend',famCards());l.style.display='none'}catch(e){}}
document.addEventListener('click',function(ev){var b=ev.target.closest('[data-fam]');if(b&&!(typeof P!=="undefined"&&P)){ev.preventDefault();ev.stopPropagation();catalog(b.dataset.fam);return}
 var g=ev.target.closest('[data-go="courses"]');if(g&&!(typeof P!=="undefined"&&P)){ev.preventDefault();ev.stopPropagation();catalog('regular')}},true);
var t;new MutationObserver(function(){clearTimeout(t);t=setTimeout(patch,30)}).observe(document.getElementById('app')||document.body,{childList:true,subtree:true});patch();
})();
