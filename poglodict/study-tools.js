const interfaceText=new Map([
  ['Seu estudo','Your study dashboard','Tu panel de estudio'],
  ['Continuar lição','Continue lesson','Continuar lección'],
  ['Revisar palavras','Review words','Repasar palabras'],
  ['Estudar','Study','Estudiar'],['Dicionário','Dictionary','Diccionario'],['Favoritos','Favorites','Favoritos'],
  ['Escolha seu idioma','Choose your language','Elige tu idioma'],['Estudo diário','Daily study','Estudio diario'],
  ['Inglês','English','Inglés'],['Espanhol','Spanish','Español'],['Italiano','Italian','Italiano'],['Alemão','German','Alemán'],
  ['Árabe','Arabic','Árabe'],['Japonês','Japanese','Japonés'],['Português brasileiro','Brazilian Portuguese','Portugués brasileño'],
  ['Idioma de apoio','Support language','Idioma de apoyo'],['Lição','Lesson','Lección'],['de','of','de'],
  ['lições concluídas','lessons completed','lecciones completadas'],['Lição de abertura','Opening lesson','Lección inicial'],
  ['Prática guiada','Guided practice','Práctica guiada'],['Anterior','Previous','Anterior'],['Próxima','Next','Siguiente'],
  ['Ir à lição','Go to lesson','Ir a la lección'],['Ir','Go','Ir'],['Lição concluída','Lesson complete','Lección completada'],
  ['Marcar como estudada','Mark as studied','Marcar como estudiada'],['Escolher próxima lição de estudo','Choose next lesson','Elegir la siguiente lección'],
  ['Praticar tradução','Practice translation','Practicar traducción'],['Praticar compreensão','Practice comprehension','Practicar comprensión'],
  ['Mostrar resposta','Show answer','Mostrar respuesta'],['Como você diria em português?','How would you say it in Portuguese?','¿Cómo lo dirías en portugués?'],
  ['Leia o exemplo abaixo e explique em português o que acontece.','Read the example and explain what happens.','Lee el ejemplo y explica lo que ocurre.'],
  ['Sentido do termo','Meaning of the term','Significado del término'],
  ['Ouvir exemplo','Listen to example','Escuchar ejemplo'],['Ouvir','Listen','Escuchar'],['Gramática','Grammar','Gramática'],
  ['Observe a construção','Notice the structure','Observa la estructura'],['Exemplo','Example','Ejemplo'],
  ['Exemplos por acepção','Examples by sense','Ejemplos por acepción'],['Revisto editorialmente','Editorially reviewed','Revisión editorial'],
  ['Exemplos do acervo','Corpus examples','Ejemplos del corpus'],
  ['Exemplos de uso em revisão.','Usage examples under review.','Ejemplos de uso en revisión.'],
  ['Segundo exemplo de uso em revisão.','Second usage example under review.','Segundo ejemplo de uso en revisión.'],
  ['Mais uma expressão','Another expression','Otra expresión'],['Expressão para praticar','Expression to practice','Expresión para practicar'],
  ['Palavra relacionada','Related word','Palabra relacionada'],['Expressão relacionada','Related expression','Expresión relacionada'],
  ['Vocabulário da leitura e do diálogo','Reading and dialogue vocabulary','Vocabulario de la lectura y el diálogo'],
  ['Consultar verbete','Open entry','Consultar entrada'],['Leitura','Reading','Lectura'],['Diálogo','Dialogue','Diálogo'],
  ['Original e tradução','Original and translation','Original y traducción'],['Seis falas com tradução','Six turns with translation','Seis intervenciones con traducción'],
  ['Palavra do dia','Word of the day','Palabra del día'],['Ver verbete','Open entry','Ver entrada'],
  ['Café','Coffee shop','Cafetería'],['Direções','Directions','Indicaciones'],['Viagem','Travel','Viajes'],
  ['Conversas','Conversations','Conversaciones'],['Argumentação','Argumentation','Argumentación'],['Nuances','Nuance','Matices'],
  ['Comida e bebida','Food and drink','Comida y bebida'],['Viagem e transporte','Travel and transportation','Viajes y transporte'],
  ['Casa e cidade','Home and city','Casa y ciudad'],['Pessoas e relações','People and relationships','Personas y relaciones'],
  ['Trabalho e estudo','Work and study','Trabajo y estudio'],['Natureza','Nature','Naturaleza'],['Corpo e saúde','Body and health','Cuerpo y salud'],
  ['Vocabulário geral','General vocabulary','Vocabulario general'],['Tema','Topic','Tema'],['Tipo','Type','Tipo'],['Todos','All','Todos'],
  ['Todos os temas','All topics','Todos los temas'],['Verbos','Verbs','Verbos'],['Substantivos','Nouns','Sustantivos'],['Adjetivos','Adjectives','Adjetivos'],
  ['Advérbios','Adverbs','Adverbios'],['Expressões','Expressions','Expresiones'],['Gírias e coloquialismos','Slang and colloquialisms','Jerga y coloquialismos'],
  ['Nome próprio','Proper name','Nombre propio'],['Contração','Contraction','Contracción'],['Verbo','Verb','Verbo'],['Substantivo','Noun','Sustantivo'],
  ['Adjetivo','Adjective','Adjetivo'],['Advérbio','Adverb','Adverbio'],['Expressão','Expression','Expresión'],
  ['Provérbio','Proverb','Proverbio'],['Interjeição','Interjection','Interjección'],['Pronome','Pronoun','Pronombre'],
  ['Preposição','Preposition','Preposición'],['Conjunção','Conjunction','Conjunción'],['Numeral','Numeral','Numeral'],['Determinante','Determiner','Determinante'],
  ['Partícula','Particle','Partícula'],['Gíria / coloquial','Slang / colloquial','Jerga / coloquial'],
  ['Buscar no dicionário','Search the dictionary','Buscar en el diccionario'],
  ['Palavra desta lição','Word from this lesson','Palabra de esta lección'],
  ['Busque uma palavra ou expressão','Search for a word or expression','Busca una palabra o expresión'],
  ['resultado','result','resultado'],['resultados','results','resultados'],['na lista','shown','en la lista'],
  ['Nenhum verbete encontrado.','No entries found.','No se encontraron entradas.'],
  ['Mostrar mais','Show more','Mostrar más'],['Mini-história da lição','Short story for lesson','Minicuento de la lección'],
  ['Mostrar tradução','Show translation','Mostrar traducción'],['Ocultar tradução','Hide translation','Ocultar traducción'],
  ['Leitura curta','Short reading','Lectura corta'],['Narrativa com contexto','Narrative with context','Narración con contexto'],
  ['Narrativa e nuances','Narrative and nuance','Narración y matices'],
  ['Palavras salvas entram na fila de revisão.','Saved words go into your review queue.','Las palabras guardadas se añaden a la cola de repaso.'],
  ['Nenhuma palavra vence agora.','No words are due for review right now.','No hay palabras pendientes de repaso ahora.'],
  ['Palavras para revisar agora','Words due for review','Palabras pendientes de repaso'],
  ['Carregando o acervo…','Loading the dictionary…','Cargando el diccionario…'],
  ['Errei','Missed it','No acerté'],['Difícil','Hard','Difícil'],['Fácil','Easy','Fácil'],['Lembrei','Got it','Lo recordé'],
  ['Complete a lacuna.','Fill in the blank.','Completa el espacio en blanco.'],
  ['Tente lembrar a palavra ou expressão.','Try to recall the word or expression.','Intenta recordar la palabra o expresión.'],
  ['Como os níveis foram organizados?','How are the levels organized?','¿Cómo se organizaron los niveles?'],
  ['8 idiomas para estudar no seu ritmo.','8 languages to learn at your own pace.','8 idiomas para estudiar a tu ritmo.'],
  ['Mandarim','Mandarin Chinese','Chino mandarín'],['Exemplos adicionais em revisão.','Additional examples under review.','Ejemplos adicionales en revisión.'],
  ['Um mundo de palavras.','A world of words.','Un mundo de palabras.']
].map(([pt,en,es])=>[pt,[en,es]]));
function supportLocale(){return lang!=='por'?'pt':support==='spa'?'spa':'eng';}
function supportTag(){return {pt:'pt-BR',eng:'en-US',spa:'es'}[supportLocale()];}
function ui(text){
  if(lang!=='por')return text;
  return interfaceText.get(text)?.[support==='spa'?1:0]||text;
}
function companionText(text){
  if(lang==='por'&&support==='spa')return supportSpanish.get(text)||portugueseSupport.definitions?.[text]||text;
  return text;
}
function exampleTranslation(example){
  if(lang==='cmn')return {text:example.translation||mandarinSupport.examples?.[example.text],locale:'pt-BR'};
  if(lang!=='por')return {text:example.translation,locale:example.english?'en':'pt-BR'};
  const original=example.translation;
  const text=support==='spa'
    ?supportSpanish.get(original)||portugueseSupport.spanish?.[example.text]
    :original||portugueseSupport.english?.[example.text];
  return {text,locale:supportTag()};
}
function refreshInterface(){
  if(!focusedLessonPanel){
    $('dailyFocusToolbar').innerHTML=lessonFocusToolbar();
    $('dailyFocusPreview').innerHTML=lessonPreviewActions(ui('Palavra desta lição'));
  }
  const clearLabel=routeLabel('Limpar busca','Clear search','Borrar búsqueda');
  $('clearQuery').setAttribute('aria-label',clearLabel);
  $('clearQuery').title=clearLabel;
  for(const node of document.querySelectorAll('[data-ui]'))node.textContent=ui(node.dataset.ui);
  const field=$('query');
  field.placeholder=ui('Busque uma palavra ou expressão');
  $('supportControl').hidden=lang!=='por';
  $('portugueseRoutes').hidden=true;
  $('supportLanguage').value=support;
  document.documentElement.lang=supportTag();
}
let reviewOpen=false;
function dueReviews(){
  return (cache[lang]||[]).filter(item=>saved.has(item.key)&&(reviews[item.key]?.due||0)<=Date.now())
    .sort((a,b)=>(reviews[a.key]?.due||0)-(reviews[b.key]?.due||0));
}
function drawStudyHome(){
  const count=dueReviews().length;
  $('homeProgress').textContent=ui(languages[lang][1])+' · '+levels[level]+' · '+ui('Lição')+' '+(unit+1)+' '+ui('de')+' '+lessonCount();
  $('reviewCount').textContent=count?num(count)+' · '+ui('Palavras para revisar agora'):ui('Nenhuma palavra vence agora.');
}
function clozeExample(item){
  const word=item.row[0].replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  const apostrophes=word.replace(/['’]/g,"['’]");
  const pattern=lang==='jpn'?apostrophes:'(?<![\\p{L}\\p{N}])'+apostrophes+'(?![\\p{L}\\p{N}])';
  const expression=new RegExp(pattern,'iu');
  for(const example of examplePair(item)){
    if(expression.test(example.text))return {example,cloze:example.text.replace(expression,'_____')};
  }
  return null;
}
function renderReview(){
  drawStudyHome();
  const day=dateKey();
  const clock=new Intl.DateTimeFormat('sv-SE',{timeZone:'America/Sao_Paulo',year:'numeric',month:'2-digit',day:'2-digit'});
  const today=(cache[lang]||[]).filter(item=>saved.has(item.key)&&
    (!reviews[item.key]?.due||clock.format(new Date(reviews[item.key].due))<=day)).length;
  $('reviewToday').textContent=today+' '+(today===1?'palavra para revisar hoje':'palavras para revisar hoje')+'.';
  const selection=dueReviews();
  const target=$('reviewCard');
  const current=selection[0];
  if(!current){
    const existing=cache[lang]?.some(item=>saved.has(item.key));
    const next=Math.min(...(cache[lang]||[]).filter(item=>saved.has(item.key)).map(item=>reviews[item.key]?.due||Infinity));
    target.innerHTML='<p>'+clean(!cache[lang]?ui('Carregando o acervo…'):existing?ui('Nenhuma palavra vence agora.'):ui('Palavras salvas entram na fila de revisão.'))+'</p>';
    if(existing&&Number.isFinite(next))target.innerHTML+='<p>Próxima revisão: '+clean(new Date(next).toLocaleString(supportTag()))+'</p>';
    return;
  }
  const prompt=clozeExample(current);
  const answer=reviewOpen?'<div class="review-answer">'+nativeText(current.row[0],'h3')+
    (prompt?renderExample(prompt.example,1):'')+'</div>':'';
  const rates=reviewOpen?'<div class="controls review-rates">'+
    [['again','Errei'],['hard','Difícil'],['good','Fácil']].map(([key,label])=>'<button type="button" data-grade="'+key+'">'+clean(ui(label))+'</button>').join('')+'</div>':
    '<button type="button" id="reviewReveal">'+clean(ui('Mostrar resposta'))+'</button>';
  target.innerHTML='<p class="meta">'+clean(ui('Palavras para revisar agora'))+' · '+num(selection.length)+'</p><h3>'+clean(ui(prompt?'Complete a lacuna.':'Tente lembrar a palavra ou expressão.'))+'</h3>'+
    '<p>'+clean(companionText(current.row[10]||current.row[1]))+'</p>'+(prompt?nativeText(prompt.cloze,'p'):'')+answer+rates;
}
function rateReview(item,grade){
  const day=86400000;
  const previous=reviews[item.key]?.days||0;
  const days=grade==='again'?0:grade==='hard'?Math.max(1,Math.ceil(previous*1.3)):Math.max(3,Math.ceil(previous*2.2));
  const delay=grade==='again'?600000:days*day;
  reviews[item.key]={days,due:Date.now()+delay};
  write('review-schedule',reviews);
}
