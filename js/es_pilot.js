/* Pogglot · rótulos fixos do modelo "padrão do dia" (episódios pilot) traduzidos para hispanohablantes (cursos com ui 'es'). */
(function(){
'use strict';
if(typeof FXES_MAP==='undefined'||typeof window.fxEs!=='function')return;
Object.assign(FXES_MAP,{
'Explore a cena':'Explora la escena','Toque nos objetos brilhantes!':'¡Toca los objetos brillantes!','Toque nos objetos da cena':'Toca los objetos de la escena',
'▶ Ouvir a cena':'▶ Escuchar la escena','🐢 Devagar':'🐢 Despacio','🇧🇷 Tradução':'🇪🇸 Traducción','Ouvir a cena':'Escuchar la escena',
'Padrão do dia':'Patrón del día','🧩 Como funciona':'🧩 Cómo funciona','💬 Quando usar':'💬 Cuándo usar','📌 Regra':'📌 Regla','🎯 Teste rápido':'🎯 Prueba rápida',
'Molde de frases':'Moldes de frases','toque nas peças':'toca las piezas',
'Cada peça colorida pode ser trocada. Toque nela e veja (e ouça) uma frase nova. O 🎲 sorteia tudo de uma vez.':'Cada pieza de color se puede cambiar. Tócala y mira (y escucha) una frase nueva. El 🎲 sortea todo de una vez.',
'Palavras da cena':'Palabras de la escena','Qual é a palavra?':'¿Cuál es la palabra?','ele/ela':'él/ella','eu':'yo',
'Passo 1: leia a frase e escolha o verbo que completa.':'Paso 1: lee la frase y elige el verbo que la completa.',
'Expressões e gírias':'Expresiones y jergas','Expressões e gírias não se traduzem palavra por palavra. Aprenda cada uma como um':'Las expresiones y jergas no se traducen palabra por palabra. Aprende cada una como un','bloco inteiro':'bloque entero',
'Expressão':'Expresión','Gíria':'Jerga','🎯 Qual expressão usar?':'🎯 ¿Qué expresión usar?','Na conversa de verdade':'En la conversación de verdad',
'Complete as falas':'Completa las frases','Qual está certa?':'¿Cuál es la correcta?','Qual frase está certa?':'¿Qué frase es la correcta?',
'🎧 O som':'🎧 El sonido','vira':'se vuelve','👄 Como fazer':'👄 Cómo hacerlo','🇧🇷 Comparando com o português':'🇪🇸 Comparando con el español',
'↔️ Ouça a diferença':'↔️ Escucha la diferencia','🗣️ Frase de treino':'🗣️ Frase de práctica','👂 Treino do ouvido':'👂 Entrenamiento del oído',
'Ouça e toque na palavra.':'Escucha y toca la palabra.','Ouça e toque na figura.':'Escucha y toca la figura.','🎤 Falar':'🎤 Hablar',
'Missão: sua vez!':'Misión: ¡tu turno!','Escolha':'Elige','uma':'una','missão e use o que você aprendeu. Cada uma pede algo diferente!':'misión y usa lo que aprendiste. ¡Cada una pide algo diferente!',
'Cena da obra':'Escena de la obra','Fale como os personagens.':'Habla como los personajes.','EPISÓDIO CONCLUÍDO':'EPISODIO COMPLETADO',
'Verbos':'Verbos','Frases para levar':'Frases para llevar','Fim do episódio':'Fin del episodio','Para levar':'Para llevar','Figurinha desbloqueada':'Cromo desbloqueado',
'Episódio concluído!':'¡Episodio completado!','Pontos':'Puntos','Acertos':'Aciertos','Tempo':'Tiempo','Você levou deste episódio':'Te llevas de este episodio',
'Referências culturais deste episódio':'Referencias culturales de este episodio','💬 Dúvidas e comentários deste episódio':'💬 Dudas y comentarios de este episodio',
'MOCHILA DO EPISÓDIO ANTERIOR':'MOCHILA DEL EPISODIO ANTERIOR','Abra cada bolso da mochila e relembre o episódio anterior!':'¡Abre cada bolsillo de la mochila y recuerda el episodio anterior!',
'Padrão':'Patrón','Palavras':'Palabras','Sons':'Sonidos','👆 Toque num bolso para abrir':'👆 Toca un bolsillo para abrir','🎯 Hoje:':'🎯 Hoy:',
'📌 Padrão':'📌 Patrón','🔤 Palavras':'🔤 Palabras','🏃 Verbos':'🏃 Verbos','💬 Expressões':'💬 Expresiones','🎧 Sons':'🎧 Sonidos',
'Informal':'Informal','Com':'Con','começo':'comienzo','fim':'fin','verbo':'verbo','quem':'quién','Ouvir':'Escuchar','🔊 Ouvir':'🔊 Escuchar'
});
const _fx=window.fxEs;
window.fxEs=function(s){
  if(typeof s!=='string')return s;const t=s.trim();if(!t)return s;let m,r;
  if(m=/^🔒 Descubra os (\d+) objetos para abrir a obra do dia$/.exec(t))r='🔒 Descubre los '+m[1]+' objetos para abrir la obra del día';
  else if(m=/^(\d+) para levar$/.exec(t))r=m[1]+' para llevar';
  else if(m=/^⭐ (\d+) acertos de primeira · 🎒 mochila cheia$/.exec(t))r='⭐ '+m[1]+' aciertos a la primera · 🎒 mochila llena';
  else if(m=/^🔁 \+(\d+) palavras no seu baralho de revisão espaçada\.$/.exec(t))r='🔁 +'+m[1]+' palabras en tu mazo de repaso espaciado.';
  else if(m=/^🔁 Estas frases voltam para você em$/.exec(t))r='🔁 Estas frases vuelven a ti en';
  else if(m=/^1, 3, 7 e 21 dias$/.exec(t))r='1, 3, 7 y 21 días';
  else if(m=/^na revisão espaçada\.$/.exec(t))r='en el repaso espaciado.';
  else if(m=/^⚡ (\d+) verbos para usar hoje$/.exec(t))r='⚡ '+m[1]+' verbos para usar hoy';
  if(r)return s.replace(t,r);
  return _fx(s);
};
})();
