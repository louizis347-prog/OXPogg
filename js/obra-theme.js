/* Tema por obra (piloto: 10 primeiros episódios do inglês A1): cor própria no episódio, faixa com a cena da obra,
   personagem que reage às respostas e textos mais calorosos. Mantém a base clara e limpa do player. */
(function(){
'use strict';
const TH={
 paddington:{c:['#2F5FB8','#6C97E6','#1F4584','#E8F0FC'],who:'paddington',title:'A Bear Called Paddington',
  ok:['Que ótimo! Isso merece um sanduíche de geleia.','Certo! Você está se saindo muito bem.'],no:['Ops! Acontece até com ursos. Veja a dica.','Quase! Respire e leia a dica com calma.']},
 alice:{c:['#1FA39A','#6ED0C8','#127068','#E5F6F4'],who:'alice',title:"Alice's Adventures in Wonderland",
  ok:['Curiosíssimo… e certo!','Que resposta maravilhosa!'],no:['Hmm, a toca é mais funda. Veja a dica.','Quase! Nem tudo é o que parece aqui.']},
 oz:{c:['#2FAE6C','#7BD26B','#17703F','#E6F7EE'],who:'dorothy',title:'The Wizard of Oz',
  ok:['Acertou! Siga a estrada amarela.','Não há lugar como o lar… e você acertou!'],no:['Quase! A dica mostra o caminho.','Tudo bem, até o Espantalho erra. Veja a dica.']},
 peterpan:{c:['#4A5BC4','#8E9CF0','#2A3580','#ECEEFB'],who:'peter',title:'Peter Pan',
  ok:['Maravilha! Você está voando alto!','Isso! Pensamentos felizes funcionam.'],no:['Pense em algo feliz e leia a dica.','Quase! A Terra do Nunca ensina com calma.']},
 toystory:{c:['#E5A11C','#F6CB62','#A56E0A','#FDF4DE'],who:'woody',title:'Toy Story',
  ok:['Boa, parceiro!','Isso aí! Até o infinito e além.'],no:['Calma, xerife. Dá para aprender com essa.','Quase! Veja a dica e tente o próximo.']},
 snow:{c:['#B83A6B','#E687A8','#7E234A','#FBE9F0'],who:'snowwhite',title:'Snow-White and Rose-Red',
  ok:['Que flor de resposta!','Certo! Florescendo como a roseira.'],no:['Quase! Toda rosa tem seu espinho.','Sem pressa. A dica ajuda.']},
 around:{c:['#7B4CC2','#A98AE8','#4A2A86','#F0EAFB'],who:'fogg',title:'Around the World in 80 Days',
  ok:['Pontual e correto!','Excelente! Estamos no horário.'],no:['Um pequeno atraso. Veja a dica.','Quase! Ajuste a rota e siga.']},
 kim:{c:['#E07B2A','#F5B05C','#9A4E14','#FDEFE2'],who:'kim',title:'Kim',
  ok:['Esperto como o Kim!','Certo! O caminho está ficando claro.'],no:['Sem pressa, o caminho ensina.','Quase! Olhe a dica e siga em frente.']},
 nights:{c:['#B5832A','#E0B25A','#7A5512','#FBF3E2'],who:'scheherazade',title:'One Thousand and One Nights',
  ok:['Mais uma história bem contada!','Certo! Vamos para a próxima noite.'],no:['Há outra versão da história. Veja a dica.','Quase! Toda noite tem uma segunda chance.']},
 madeline:{c:['#E0707A','#F4A3A8','#A0414B','#FDEBEC'],who:'madeline',title:'Madeline',
  ok:['Sem medo de nada!','Muito bem! Em fila e acertando.'],no:['Tudo bem errar. Veja a dica.','Quase! Pas de problème.']}
};
const WARM=[
 [/^Responda todas as perguntas\.?$/,'Bora responder? Uma de cada vez.'],
 [/^Tudo certo! Muito bem!$/,'Mandou bem! Tudo certo por aqui.'],
 [/^Bom trabalho! Revise o que errou\.$/,'Boa! Dê uma olhada no que errou e fixe com calma.'],
 [/^Ouça a cena e leia junto\.$/,'Ouça a cena e vá lendo junto. Sem pressa.'],
 [/^Toque nas peças para trocar as palavras\.$/,'Brinque com as peças e invente frases novas.'],
 [/^Toque para ouvir cada expressão\.$/,'Toque para ouvir. Quanto mais ouvir, mais natural fica.'],
 [/^Você fechou mais um episódio!$/,'Mais um episódio no bolso! Que orgulho.']
];
const STRIP_OK=/^(pgsheet|pgrule|pgmold|verbs|vplay|pgexp|pglab|pgspeak|pgmission)$/;
const th=()=>{try{if(typeof P==='undefined'||!P||!P.e||P.isTest||!window.PogObra)return null;return TH[PogObra.key(P.e)]||null}catch(e){return null}};
const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const calm=()=>{try{return matchMedia('(prefers-reduced-motion:reduce)').matches||localStorage.getItem('pogglot:fxoff')==='1'}catch(e){return false}};

function paint(){
  const pl=document.getElementById('player');if(!pl)return;
  const t=th();pl.classList.toggle('ot-on',!!t);if(!t)return;
  [...pl.classList].filter(c=>c.indexOf('ot-k-')===0).forEach(c=>pl.classList.remove(c));pl.classList.add('ot-k-'+PogObra.key(P.e));
}
function strip(n,st){
  const t=th();if(!t)return;
  const f=P.e.fr&&P.e.fr[n];if(!f||!STRIP_OK.test(f.k))return;
  const step=st.querySelector('.step');if(!step||step.querySelector('.ot-strip'))return;
  const d=document.createElement('div');d.className='ot-strip';d.setAttribute('aria-hidden','true');
  d.innerHTML=`${PogObra.svg(P.e,'strip')}<span class="ot-cap">📖 ${esc(t.title)}</span>`;
  step.prepend(d);
}
/* o personagem da obra reage às respostas */
function react(ok){
  const t=th();if(!t||calm())return;
  const pl=document.getElementById('player');if(!pl)return;
  let r=document.getElementById('otreact');if(r)r.remove();
  r=document.createElement('div');r.id='otreact';r.className='ot-react '+(ok?'ok':'no');
  const lines=ok?t.ok:t.no;
  r.innerHTML=`<span class="ot-face">${PogObra.face(t.who)}</span><span class="ot-say">${esc(lines[Math.random()*lines.length|0])}</span>`;
  pl.appendChild(r);setTimeout(()=>{if(r.parentNode)r.remove()},2400);
}
const prevR=window.renderFx;
if(typeof prevR==='function')window.renderFx=function(n,st,lang){
  const r=prevR.apply(this,arguments);
  try{paint();strip(n,st)}catch(e){}
  return r;
};
/* textos do Poggie e do botão, mais calorosos */
const prevSay=window.say;
if(typeof prevSay==='function')window.say=function(txt,mood){
  if(th()&&typeof txt==='string'){for(const [re,to] of WARM){if(re.test(txt)){txt=to;break}}}
  return prevSay.call(this,txt,mood);
};
const prevCta=window.cta;
if(typeof prevCta==='function')window.cta=function(label,en,amber){
  if(th()&&typeof label==='string'){
    label=label.replace(/^Faltam (\d+)$/,'Faltam $1 · você consegue').replace(/^Responda tudo: (\d+) perguntas$/,'Responda as $1 perguntas');
  }
  return prevCta.call(this,label,en,amber);
};
window.PogTheme={react,theme:th};
})();
