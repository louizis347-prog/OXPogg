function lessonText(language,index,levelIndex,vocabulary){
  if(vocabulary.sceneSource){
    return alignLessonText(vocabulary.sceneSource.slice(6).join('\n'),vocabulary.sceneTranslation.slice(6).join('\n'));
  }
  const locale=language==='por'?'pt':language;
  const companion=language==='por'?supportLocale():'pt';
  if(index===0&&levelIndex===0){
    return language==='por'?alignLessonText(portugueseCafe.por,portugueseCafe[companion]):
      alignLessonText(cafeScenes[language],cafeScenes.pt[language]);
  }
  const frame=(index+levelIndex)%readingFrames.pt.length;
  const {word,expression,wordExample,expressionExample}=vocabulary;
  const render=(locale,isTranslation)=>{
    const [example,reply,noExample,noReply]=readingConnectors[locale];
    const quotation=(template,fallback,sample)=>{
      if(!sample?.text||!sample?.pt)return fallback;
      const text=(isTranslation?sample.pt:sample.text).replace(/\s+/g,' ').trim();
      return template.replace('{line}',()=>locale==='jpn'?text.replace(/[。？！]$/u,''):text);
    };
    const slots={
      word,expression,
      example:quotation(example,noExample,expressionExample?.pt?expressionExample:wordExample),
      reply:quotation(reply,noReply,wordExample)
    };
    return readingFrames[locale][frame].replace(/\{(word|expression|example|reply)\}/g,(_,slot)=>slots[slot]);
  };
  return alignLessonText(render(locale,false),render(companion,true));
}
function alignLessonText(native,portuguese){
  const translations=portuguese.split('\n');
  const pairs=native.split('\n').map((text,i)=>({text:lessonLevelText(text),pt:translations[i]}));
  return {reading:pairs.slice(0,5),dialogue:pairs.slice(5)};
}
function portugueseSample(item){
  if(!item)return null;
  const examples=exampleList(item);
  for(const example of examples){
    const translation=exampleTranslation(example);
    if(translation.text&&(!example.english||lang==='por')&&!example.context)return {text:example.text,pt:translation.text};
  }
  return null;
}
function renderLessonText(content,previewPhotos){
  const used=new Set();
  const reprise=currentLesson.reviewScene?'<p class="scene-reuse-note">'+routeLabel('Cena de revisão compartilhada por outras lições deste tema.','Review scene shared by other lessons on this theme.','Escena de repaso compartida con otras lecciones del tema.')+'</p>':'';
  const answer=line=>nativeText(line.text,'p')+'<p lang="'+supportTag()+'">'+clean(line.pt)+'</p>'+lessonPlayButton(line.text,{compact:true});
  const readCoach=lessonCoach(routeLabel('Leia com um objetivo','Read with a goal','Lee con un objetivo'),
    routeLabel('Antes de ler a tradução, descubra onde a cena começa ou quem aparece primeiro.','Before checking the translation, find where the scene starts or who appears first.','Antes de mirar la traducción, descubre dónde empieza la escena o quién aparece primero.'),
    answer(content.reading[0]));
  const replyCoach=lessonCoach(routeLabel('Escute e antecipe','Listen and predict','Escucha y anticipa'),
    routeLabel('Ouça a primeira fala, faça uma pausa e imagine a resposta. Compare com a segunda fala.','Listen to the first line, pause, and imagine the reply. Compare it with the second line.','Escucha la primera intervención, haz una pausa e imagina la respuesta. Compárala con la segunda.'),
    answer(content.dialogue[1]||content.dialogue[0]));
  return lessonPanel('reading',routeLabel('Leitura com áudio e tradução','Reading with audio and translation','Lectura con audio y traducción'),
    '<section class="lesson-card" data-playback-block aria-labelledby="readingTitle"><h3 id="readingTitle">'+ui('Leitura')+'</h3>'+
    sectionPlayButton('reading',routeLabel('Ouvir a leitura','Play the reading','Escuchar la lectura'))+reprise+readCoach+lessonLinesMarkup(content.reading,'reading',{used})+'</section>',{extraClass:'lesson-texts',used:previewPhotos})+
    lessonPanel('dialogue',englishLessonPlan()?'Oito falas com áudio e tradução':routeLabel('Seis falas com áudio e tradução','Six lines with audio and translation','Seis intervenciones con audio y traducción'),
    '<section class="lesson-card" data-playback-block aria-labelledby="dialogueTitle"><h3 id="dialogueTitle">'+ui('Diálogo')+'</h3>'+
    sectionPlayButton('dialogue',routeLabel('Ouvir o diálogo completo','Play the full dialogue','Escuchar el diálogo completo'))+
    reprise+replyCoach+lessonLinesMarkup(content.dialogue,'dialogue',{used})+'</section>',{extraClass:'lesson-texts',used:previewPhotos});
}
