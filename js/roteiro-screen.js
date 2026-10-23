/* Pré-episódio: roteiro do episódio (gramática, vocabulário, 4 verbos, expressões e gírias).
   Inglês: data/skel/<curso>.json · demais cursos: data/plan/<curso>.json. Sem roteiro do episódio, a tela é pulada. */
(function(){
'use strict';
const cache={};
const L={pt:{eye:'Pré-episódio · Roteiro do episódio',gram:'Estrutura gramatical',voc:'Vocabulário',vb:'4 verbos',ex:'Expressões comuns',gir:'Gírias e coloquiais',obra:'Obra',go:'Começar o episódio',load:'Carregando…',say:'Este é o roteiro do episódio: o que vai aparecer nele.'},
         es:{eye:'Pre-episodio · Guion del episodio',gram:'Estructura gramatical',voc:'Vocabulario',vb:'4 verbos',ex:'Expresiones comunes',gir:'Jerga y coloquial',obra:'Obra',go:'Empezar el episodio',load:'Cargando…',say:'Este es el guion del episodio: lo que aparecerá en él.'}};
function load(cid){
 if(!cache[cid]){
  const en=/^en-/.test(cid);
  cache[cid]=fetch((en?'data/skel/':'data/plan/')+cid+'.json?v=3').then(r=>r.ok?r.json():(en?[]:{})).then(a=>{
   if(!en)return a;
   const m={};a.forEach(x=>{if(x.status==='roteiro')m[x.n]={t:x.titulo,tema:x.tema,gram:(x.gramatica||{}).estrutura||x.tema,vocab:(x.vocabulario_pt&&x.vocabulario_pt.length?x.vocabulario_pt:(x.vocabulario||[]).map(w=>[w,''])),verbos:x.verbos,exp:x.expressoes,gir:x.girias,obra:x.obra}});
   return m;}).catch(()=>({}));
 }
 return cache[cid];
}
function row(ico,title,body){return '<div class="rt-row"><span class="rt-ic">'+ico+'</span><div><b>'+title+'</b>'+body+'</div></div>';}
function pairs(list){return '<ul class="rt-ul">'+(list||[]).map(p=>'<li>'+esc(p[0])+(p[1]?' <small>— '+esc(p[1])+'</small>':'')+'</li>').join('')+'</ul>';}
window.renderRoteiro=function(st){
 const n=P.e.n,cid=P.cid,idx=P.i,t=L[(P.c&&P.c.ui)==='es'?'es':'pt'];
 st.innerHTML='<div class="step rt"><span class="eyebrow">'+t.eye+'</span><p>'+t.load+'</p></div>';
 cta(t.go,false,true);
 load(cid).then(m=>{
  if(!P||P.steps[P.i]!=='roteiro'||P.i!==idx)return;
  const s=m[n];
  if(!s){P.i++;render();return;}
  let h='<div class="step rt"><span class="eyebrow">'+t.eye+'</span><h2>'+esc(s.t)+'</h2>';
  if(s.tema)h+='<p class="rt-sub">'+esc(s.tema)+'</p>';
  h+=row('🧩',t.gram,'<p>'+esc(s.gram||'—')+'</p>');
  h+=row('📚',t.voc,pairs(s.vocab));
  h+=row('🏃',t.vb,pairs(s.verbos));
  h+=row('💬',t.ex,pairs(s.exp));
  if(s.gir&&s.gir.length)h+=row('😎',t.gir,pairs(s.gir));
  if(s.obra)h+=row('🎬',t.obra,'<p>'+esc(s.obra)+'</p>');
  st.innerHTML=h+'</div>';
  say(t.say);cta(t.go,true,true);
 });
};
})();
