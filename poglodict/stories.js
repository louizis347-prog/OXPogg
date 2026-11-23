const storyCache=new Map();
const storyInFlight=new Map();
function storyData(language){
  if(!storyInFlight.has(language)){
    const request=loadJson('stories-'+language+'.json').then(data=>{storyCache.set(language,data);return data;}).catch(error=>{
      storyInFlight.delete(language);throw error;
    });
    storyInFlight.set(language,request);
  }
  return storyInFlight.get(language);
}
function storyLines(data,chapter,episode){
  const entry=data.episodes[episode],arc=data.arcs[chapter];
  const simpler=data.simple?.[episode];
  const opening=chapter===0&&simpler?simpler:chapter===1&&simpler?[...simpler.slice(0,3),entry[4]]:entry.slice(1,5);
  return [...opening,...arc.slice(0,2),entry[5+chapter],...arc.slice(2)];
}
function storyHtml(language,chapter,episode){
  const source=storyCache.get(language==='por'?'pt':language),pt=storyCache.get('pt');
  const supportData=storyCache.get(supportLocale());
  const target=storyLines(source,chapter,episode),translation=storyLines(supportData,chapter,episode);
  const companionTitle=supportData.episodes[episode][0];
  const note=chapter<2?'Leitura curta':chapter<4?'Narrativa com contexto':'Narrativa e nuances';
  const theme=({station:'ticket',cafe:'cup',library:'notebook',river:'park',clinic:'health'})[pt.scenes[episode]]||pt.scenes[episode];
  return '<div data-playback-block>'+lessonPhotoFrame(photoForMoment(theme,episode,'story',pt.episodes[episode][0]),'lesson-story-photo')+'<div class="term-heading"><h3>'+nativeText(source.episodes[episode][0])+'</h3>'+
    lessonPlayButton(source.episodes[episode][0],{compact:true})+'</div>'+
    '<p class="meta">'+clean(ui(note))+'</p><p id="storyHeadingTranslation" class="lesson-pt" hidden lang="'+supportTag()+'">'+clean(companionTitle)+'</p>'+
    '<div class="controls">'+sectionPlayButton('story',routeLabel('Ouvir a mini-história','Play the short story','Escuchar el minicuento'))+
    '<button type="button" class="translation-toggle" id="storyTranslation" aria-expanded="false" aria-controls="storyLines">'+clean(ui('Mostrar tradução'))+'</button></div>'+
    lessonCoach(routeLabel('Encontre a virada','Find the turning point','Encuentra el giro'),
      routeLabel('Escolha a frase em que o plano muda ou surge um problema. Depois conte em uma frase o que aconteceu no fim.','Find the line where the plan changes or a problem appears. Then say in one sentence what happened at the end.','Busca la frase en la que cambia el plan o aparece un problema. Luego cuenta en una frase qué pasó al final.'))+
    lessonLinesMarkup(target.map((text,i)=>({text,pt:translation[i]})),'story',{id:'storyLines',hideTranslation:true,theme})+'</div>';
}
function storySection(lessonNumber,used){
  if(lessonNumber%10!==0)return '';
  const authored=renderCompletedEnglishStory();
  if(authored)return lessonPanel('story','Narrativa ligada ao tema da lição',authored,{id:'lessonStory',used});
  return lessonPanel('story',routeLabel('Narrativa com áudio e tradução','Story with audio and translation','Narración con audio y traducción'),
    '<div class="story-content" id="storyContent" aria-live="polite"></div>',{id:'lessonStory',used});
}
function connectStory(){
  const details=$('lessonStory');
  const content=$('storyContent');
  if(!details||!content)return;
  const selected=lang,chapter=level,episode=(unit+1)/10-1;
  const toRead=selected==='por'?'pt':selected,translation=supportLocale();
  content.addEventListener('click',event=>{
    if(event.target.id!=='storyTranslation')return;
    const button=event.target;
    const active=button.getAttribute('aria-expanded')==='true';
    button.setAttribute('aria-expanded',String(!active));
    button.textContent=ui(active?'Mostrar tradução':'Ocultar tradução');
    for(const line of content.querySelectorAll('.lesson-pt'))line.hidden=active;
  });
  const render=()=>{
    if([toRead,translation,'pt'].every(key=>storyCache.has(key))){
      content.innerHTML=storyHtml(selected,chapter,episode);
      return;
    }
    content.textContent='Carregando a mini-história…';
    Promise.all([storyData('pt'),storyData(toRead),storyData(translation)]).then(()=>{
      if(content.isConnected)content.innerHTML=storyHtml(selected,chapter,episode);
    }).catch(()=>{
      if(!content.isConnected)return;
      content.innerHTML='<p>A mini-história não carregou. <button type="button">Tentar novamente</button></p>';
      content.querySelector('button').addEventListener('click',render,{once:true});
    });
  };
  if(details.open)render();
  details.addEventListener('toggle',()=>{
    if(details.open&&!content.hasChildNodes())render();
  });
}
