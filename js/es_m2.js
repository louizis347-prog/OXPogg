/* Pogglot · Inglés para hispanohablantes: rótulos del modelo 2 (traducción de la interfaz PT → ES) */
(function(){
'use strict';
if(typeof FXES_MAP==='undefined'||typeof fxEs!=='function')return;
const ENES=()=>!!(typeof P!=='undefined'&&P&&P.c&&/^enes/.test(P.c.id||''));
Object.assign(FXES_MAP,{
'🇧🇷 Ver tradução':'🌎 Ver traducción','🇧🇷 Esconder tradução':'🌎 Ocultar traducción',
'Toque em cada verbo: veja as formas e ouça a frase.':'Toca cada verbo: mira las formas y escucha la frase.',
'Faça o passo para continuar':'Haz el paso para continuar',
'Troque 2 peças para continuar':'Cambia 2 piezas para continuar',
'🔁 Troque a peça tracejada por:':'🔁 Cambia la pieza punteada por:',
'Descubra todas as expressões':'Descubre todas las expresiones',
'🔊 Ouça os exemplos':'🔊 Escucha los ejemplos','👂 Ouça a diferença':'👂 Escucha la diferencia',
'Abra os cartões e ouça os exemplos':'Abre las tarjetas y escucha los ejemplos',
'Ouça e toque na palavra que você escutou.':'Escucha y toca la palabra que oíste.','Ouça e escolha':'Escucha y elige',
'Toque em cada expressão: ouça e veja quando usar.':'Toca cada expresión: escucha y mira cuándo usarla.',
'💡 Aprenda cada uma como um bloco: não traduza palavra por palavra.':'💡 Aprende cada una como un bloque: no traduzas palabra por palabra.',
'Da obra para a lição':'De la obra a la lección','Contextos em áudio':'Contextos en audio','Leia':'Lee','Ouça':'Escucha','Repita':'Repite','Converse':'Conversa','Desafio':'Desafío',
'Monte a frase na ponte':'Arma la frase en el puente','Balões do Poggie':'Globos de Poggie','Portas do Poggie':'Puertas de Poggie','Memória do Poggie':'Memoria de Poggie','Pesca do Poggie':'Pesca de Poggie',
'Verbos em ação':'Verbos en acción','Expressões e colocações':'Expresiones y combinaciones','Contextos variados':'Contextos variados','Escolha a peça':'Elige la pieza','Pratique os verbos':'Practica los verbos','Pratique as combinações':'Practica las combinaciones',
'Treino dos verbos':'Entrenamiento de verbos','Treino das combinações':'Entrenamiento de combinaciones','Treino dos sons':'Entrenamiento de sonidos','Reading':'Lectura','Palavras em frases':'Palabras en frases','Estrutura da frase':'Estructura de la frase',
'Common Expressions':'Expresiones comunes','Revisão':'Repaso','Complete o diálogo':'Completa el diálogo','Você entendeu?':'¿Entendiste?','Missão dos verbos':'Misión de los verbos','Caça-sons':'Caza-sonidos',
'Muito bem! Pode trocar mais peças ou seguir. 🎉':'¡Muy bien! Puedes cambiar más piezas o seguir. 🎉','Tradução:':'Traducción:','Expressões':'Expresiones','Peças-fala':'Piezas-frase','Ouça e toque na figura da palavra.':'Escucha y toca la figura de la palabra.',
'Comparando com o português':'Comparando con el español','O som':'El sonido','Como fazer':'Cómo hacerlo',
'Passo 1: veja a cena e escolha o verbo certo.':'Paso 1: mira la escena y elige el verbo correcto.'
});
const _fx=window.fxEs;
window.fxEs=function(s){
  if(typeof s!=='string')return s;const t=s.trim();if(!t)return s;let m,r;
  if(ENES()&&t==='🇧🇷')return s.replace(t,'🌎');
  if(m=/^SITUAÇÃO (\d+)\/(\d+)$/.exec(t))r='SITUACIÓN '+m[1]+'/'+m[2];
  else if(m=/^🔁 \+(\d+) palavras no seu baralho de revisão espaçada\.$/.exec(t))r='🔁 +'+m[1]+' palabras en tu mazo de repaso espaciado.';
  else if(m=/^Troque pelo menos (\d+) peças \((\d+)\/(\d+)\)\.$/.exec(t))r='Cambia al menos '+m[1]+' piezas ('+m[2]+'/'+m[3]+').';
  else if(m=/^💬 (\d+) expressões comuns$/.exec(t))r='💬 '+m[1]+' expresiones comunes';
  else if(m=/^Abra os (\d+) cartões e ouça os exemplos\.$/.exec(t))r='Abre las '+m[1]+' tarjetas y escucha los ejemplos.';
  else if(m=/^⚡ (\d+) verbos para usar hoje$/.exec(t))r='⚡ '+m[1]+' verbos para usar hoy';
  else if(m=/^🃏 (\d+) expressões coringa$/.exec(t))r='🃏 '+m[1]+' expresiones comodín';
  else if(m=/^Troque (\d+) peças? para continuar$/.exec(t))r='Cambia '+m[1]+(m[1]==='1'?' pieza':' piezas')+' para continuar';
  else if(m=/^🔊 Fala (\d+): ouça e escolha a peça$/.exec(t))r='🔊 Frase '+m[1]+': escucha y elige la pieza';
  if(r)return s.replace(t,r);
  return _fx(s);
};
})();
