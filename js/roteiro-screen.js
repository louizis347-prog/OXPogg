/* Pré-episódio: tela de roteiro (verbos, expressões, gírias, gramática, vocabulário) lida de data/skel/<curso>.json */
(function(){
'use strict';
const cache={};
function load(cid){
 if(!cache[cid])cache[cid]=fetch('data/skel/'+cid+'.json?v=1').then(r=>r.ok?r.json():[]).then(a=>{const m={};a.forEach(x=>{m[x.n]=x});return m}).catch(()=>({}));
 return cache[cid];
}
function row(ico,title,body){return '<div class="rt-row"><span class="rt-ic">'+ico+'</span><div><b>'+title+'</b>'+body+'</div></div>';}
function pairs(list){return '<ul class="rt-ul">'+list.map(p=>'<li>'+esc(p[0])+(p[1]?' <small>— '+esc(p[1])+'</small>':'')+'</li>').join('')+'</ul>';}
window.renderRoteiro=function(st){
 const n=P.e.n,cid=P.cid,idx=P.i;
 st.innerHTML='<div class="step rt"><span class="eyebrow">Pré-episódio · Roteiro</span><p>Carregando…</p></div>';
 cta('Começar o episódio',false,true);
 load(cid).then(m=>{
  if(!P||P.steps[P.i]!=='roteiro'||P.i!==idx)return;
  const s=m[n];
  if(!s||s.status!=='roteiro'){P.i++;render();return;}
  const g=s.gramatica||{};
  let h='<div class="step rt"><span class="eyebrow">Pré-episódio · Roteiro do episódio</span><h2>'+esc(s.titulo)+'</h2>';
  if(s.tema)h+='<p class="rt-sub">'+esc(s.tema)+'</p>';
  h+=row('🧩','Estrutura gramatical','<p>'+esc(g.estrutura||s.tema||'—')+(g.funcao?' <small>— '+esc(g.funcao)+'</small>':'')+'</p>');
  h+=row('📚','Vocabulário',pairs(s.vocabulario_pt&&s.vocabulario_pt.length?s.vocabulario_pt:(s.vocabulario||[]).map(x=>[x,''])));
  h+=row('🏃','4 verbos',pairs(s.verbos||[]));
  h+=row('💬','Expressões comuns',pairs(s.expressoes||[]));
  if(s.girias&&s.girias.length)h+=row('😎','Gírias',pairs(s.girias));
  if(s.obra)h+=row('🎬','Obra',  '<p>'+esc(s.obra)+'</p>');
  h+='</div>';
  st.innerHTML=h;
  say('Este é o roteiro do episódio: o que vai aparecer nele.');cta('Começar o episódio',true,true);
 });
};
})();
