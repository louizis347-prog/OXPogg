const lessonsPerLevel=350;
const activitySteps=[
  'Depois leia a frase em voz alta.',
  'Depois tente recuperá-la de memória.',
  'Depois mude um detalhe de tempo ou lugar.',
  'Depois formule uma pergunta que a frase possa responder.',
  'Depois acrescente uma frase de continuação.'
];
const corpusExamples={};
const thirdExamples={};
const curriculum={};
const wordIndex={};
const starterKey=(level,index)=>lang+'-'+level+(index?'-'+index:'');
const focusTerms=text=>[...new Set(text.toLowerCase().match(/[a-z]{4,}/g)||[])].filter(t=>!['that','with','from','used','when','which','this','someone','something','person','form','word','usually','other','certain','into','some','such','than','their','especially','referring'].includes(t));
function isExpression(item){
  const [word,,part,flag]=item.row;
  return part==='phrase'||part==='proverb'||flag===1&&part!=='intj'||word.trim().includes(' ');
}
function lessonItems(list){
  const themesOrder=[...themes.map(t=>t[0]),'Vocabulário geral'];
  const lexical=list.filter(item=>!isExpression(item)&&item.row[3]!==2&&['noun','verb','adj','adv'].includes(item.row[2]));
  const groups=themesOrder.map(theme=>lexical.filter(item=>item.theme===theme)
    .sort((a,b)=>(b.row[16]??6)-(a.row[16]??6)||(b.row[11]||0)-(a.row[11]||0)));
  const selected=[];
  // Round-robin interleaving keeps the seven practical themes in each level.
  const offsets=groups.map(()=>0);
  const target=(lessonsPerLevel-1)*levels.length;
  for(let cursor=0;selected.length<target;cursor++){
    const slot=cursor%groups.length;
    if (!groups.some((g,i)=>offsets[i]<g.length)) break;
    const item=groups[slot][offsets[slot]++];
    if(item)selected.push(item);
  }
  return levels.map((_,level)=>selected.slice(level*(lessonsPerLevel-1),(level+1)*(lessonsPerLevel-1)));
}
function makeIndex(list){
  const make=items=>{
    const byTheme=new Map();
    const byTerm=new Map();
    for(const item of items){
      if(!byTheme.has(item.theme))byTheme.set(item.theme,[]);
      byTheme.get(item.theme).push(item);
      for(const t of item.terms){
        if(!byTerm.has(t))byTerm.set(t,[]);
        byTerm.get(t).push(item);
      }
    }
    return {items,byTheme,byTerm};
  };
  const phrases=list.filter(isExpression);
  const words=list.filter(item=>!isExpression(item)&&item.row[3]!==2);
  return {phrases:make(phrases),words:make(words),lookup:new Map(list.map(item=>[item.row[0],item]))};
}
function related(item,pool){
  const strength=new Map();
  for(const token of item.terms){
    const group=pool.byTerm.get(token)||[];
    const weight=group.length?4/(1+Math.log2(group.length)):0;
    for(const candidate of group.slice(0,70))strength.set(candidate,(strength.get(candidate)||0)+weight);
  }
  const options=pool.byTheme.get(item.theme)||[];
  const salt=[...item.row[0]].reduce((total,c)=>total+c.codePointAt(0),0);
  for(let n=0;n<Math.min(12,options.length);n++){
    const candidate=options[(salt+n)%options.length];
    if(!strength.has(candidate))strength.set(candidate,0);
  }
  let best=null;
  let high=-Infinity;
  for(const [candidate,value] of strength){
    if(candidate.key===item.key)continue;
    const score=value+(candidate.theme===item.theme&&item.theme!=='Vocabulário geral'?1.2:0);
    if(score>high){best=candidate;high=score;}
  }
  return best||pool.items.filter(x=>x.key!==item.key)[salt%Math.max(1,pool.items.length-1)];
}
function examplePair(item){
  if(item.reviewed)return item.reviewed.examples;
  const [word,,,,first,en,sid,pt,,roman,,,author]=item.row;
  const source=corpusExamples[lang];
  const second=source&&Object.hasOwn(source,word)?source[word]:null;
  const normalized=value=>normalize(value).replace(/[^\p{L}\p{N}]/gu,'');
  const authored= item.lessonEntry?.second||authoredSeconds[lang].get(word);
  const firstExample={text:first,translation:pt||en,english:!pt&&Boolean(en),roman,source:sid,author};
  if(authored)return [firstExample,authored];
  const review=auditedExamples(item);
  if(review)return review;
  const companion=second&&normalized(second[0])!==normalized(first)
    ?{text:second[0],translation:second[1],english:Boolean(second[1]),source:second[2],roman:second[3]}:null;
  return [firstExample,companion].filter(Boolean);
}
function exampleList(item){
  const examples=[...examplePair(item)];
  const source=thirdExamples[lang];
  const extra=source&&Object.hasOwn(source,item.row[0])?source[item.row[0]]:null;
  const next=item.lessonEntry?.third||editorialThird[lang]?.get(item.row[0])||(!item.reviewed&&extra?{text:extra[0],source:extra[1],roman:extra[2]}:null);
  const signature=text=>normalize(text).replace(/[^\p{L}\p{N}]/gu,'');
  if(next&&examples.every(example=>signature(example.text)!==signature(next.text)))examples.push(next);
  return examples;
}
function examplesHtml(item,art){
  const examples=exampleList(item);
  const rendered=examples.map((example,n)=>renderExample(example,n+1,art)+(art===undefined?'':exampleAudio(example.text))).join('');
  const status=examples.length<3?'Exemplos adicionais em revisão.':'';
  return rendered+(status?'<p class="meta example-review">'+ui(status)+'</p>':'');
}
function sourceLink(source,author){
  if(!source)return '';
  if(source.startsWith('https://'))return '<a href="'+clean(source)+'" target="_blank" rel="noopener">Fonte da frase</a>';
  if(!/^\d+$/.test(source))return '';
  return '<a href="https://tatoeba.org/en/sentences/show/'+source+'" target="_blank" rel="noopener">Tatoeba · frase '+source+'</a>';
}
function renderExample(example,n,illustration,usedPhotos){
  if(!example?.text)return '';
  const translation=exampleTranslation(example);
  return '<div class="example lex-example">'+(screen==='licao'||illustration===undefined?'':scene(illustration))+
    '<p class="example-label">'+ui('Exemplo')+' '+n+(example.context?' · termo citado':'')+'</p>'+
    nativeText(example.text,'p')+
    (example.roman?'<p class="meta"'+(lang==='cmn'?' lang="zh-Latn"':'')+'>'+clean(example.roman)+'</p>':pinyinLine(example.text))+
    (translation.text?'<p class="translation" lang="'+translation.locale+'">'+clean(translation.text)+'</p>':'')+
    (example.source?'<p class="meta">'+sourceLink(example.source,example.author)+(example.translationId?' · '+sourceLink(example.translationId,example.translationAuthor):'')+'</p>':'')+
    (screen==='licao'?illustratedExampleControls(example.text,n-1,translation.text,usedPhotos):'')+'</div>';
}
function wordHash(word){return '#verbete/'+lang+'/'+encodeURIComponent(word);}
function linkTo(item,label){
  if(!item)return '';
  const word=item.row[0];
  return '<a class="word-link" href="'+clean(wordHash(word))+'">'+(label?'<span>'+clean(ui(label))+'</span>':'')+nativeText(word)+'</a>';
}
function connections(item){
  const index=wordIndex[lang];
  if(!index||!item)return '';
  return '<div class="related-block"><p class="meta">Relacionados</p><div class="connections">'+linkTo(related(item,index.words),'')+
    linkTo(related(item,index.phrases),'')+'</div></div>';
}
function illustration(item){
  return ({cup:0,pin:1,plane:2,heart:3,book:4,sun:5})[item.icon]??4;
}
function buildPractice(index,lesson){
  const [word,gloss]=lesson.row;
  const sample=exampleList(lesson)[0];
  const [strategy,instructions]=variedPractice[level][index%variedPractice[level].length].map(ui);
  const expression=related(lesson,wordIndex[lang].phrases);
  const expressionSection=expression?'<details open><summary>'+ui('Expressão para praticar')+'</summary><h3>'+nativeText(expression.row[0])+'</h3><p lang="'+(lang==='por'?supportTag():expression.reviewed?'pt-BR':'en')+'">'+clean(companionText(expression.row[1]))+'</p>'+
    examplesHtml(expression,3)+connections(expression)+'</details>':'';
  const section='<article class="lesson-card">'+scene(illustration(lesson))+'<span class="tag">'+icon(lesson.icon||'book')+' '+clean(ui(lesson.theme))+'</span>'+
    '<h3>'+nativeText(word)+'</h3><p>'+(lesson.row[10]?'<strong>'+clean(companionText(lesson.row[10]))+'</strong> · ':'')+(!lesson.reviewed?'<span lang="'+(lang==='por'?supportTag():'en')+'">'+clean(lang==='cmn'?mandarinSupport.definitions?.[gloss]||gloss:companionText(gloss))+'</span>':'')+'</p>'+
    examplesHtml(lesson)+
    (sample?'<div class="controls"><button data-say="word">'+icon('speaker')+' '+ui('Ouvir exemplo')+'</button></div>':'')+connections(lesson)+expressionSection+'</article>';
  const guided=Boolean(index%2);
  const topic=guided?grammarPractice[lang][level]:study[lang][level].slice(4);
  const audio={word:sample?.text};
  const tipSection='<article class="lesson-card">'+lessonSectionPhoto(lessonVisualTheme(),'grammar')+'<span class="tag">'+icon('book')+' '+ui('Gramática')+' · '+levels[level]+'</span>'+
    grammarPanel(lang,level,guided,topic,audio)+'<h4>'+clean(strategy)+'</h4><p>'+clean(instructions)+' '+
    clean(ui(activitySteps[Math.floor(index/5)%activitySteps.length]))+'</p></article>';
  return {cards:section+tipSection, cue:ui('Leia o exemplo abaixo e explique em português o que acontece.'), clue:sample?.text||topic[2], answer:sample?exampleTranslation(sample).text||ui('Sentido do termo')+': '+companionText(gloss):companionText(topic[3]),
    audio,vocabulary:{word,expression:expression.row[0],
      wordExample:portugueseSample(lesson),expressionExample:portugueseSample(expression)}};
}
