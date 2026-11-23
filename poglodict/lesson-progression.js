const contractionMilestones={
  be:[0,50],negative:[1,0],future:[1,50],suggestion:[1,100],perfect:[2,50],conditional:[3,50]
};
function lessonHasContractions(kind,tier=level,index=unit){
  const [firstTier,firstUnit]=contractionMilestones[kind];
  return tier>firstTier||(tier===firstTier&&index>=firstUnit);
}
function expandEnglishLesson(text,tier,index){
  const allowed=kind=>lessonHasContractions(kind,tier,index);
  const matchCase=(source,target)=>source===source.toUpperCase()?target.toUpperCase():
    /^[A-Z]/.test(source)?target[0].toUpperCase()+target.slice(1):target;
  const negatives={
    "aren't":'are not',"isn't":'is not',"wasn't":'was not',"weren't":'were not',
    "don't":'do not',"doesn't":'does not',"didn't":'did not',"haven't":'have not',"hasn't":'has not',
    "hadn't":'had not',"can't":'cannot',"couldn't":'could not',"won't":'will not',"wouldn't":'would not',
    "shouldn't":'should not',"shan't":'shall not',"mustn't":'must not',"needn't":'need not',"mightn't":'might not'
  };
  let result=text;
  if(!allowed('negative'))result=result.replace(/\b[A-Za-z]+n['’]t\b/gi,match=>{
    const full=negatives[match.toLowerCase().replace('’',"'")];
    return full?matchCase(match,full):match;
  });
  if(!allowed('suggestion'))result=result.replace(/\blet['’]s\b/gi,match=>matchCase(match,'let us'));
  const suffixes={m:['be','am'],re:['be','are'],ve:['perfect','have'],ll:['future','will'],d:['conditional','would']};
  result=result.replace(/\b(I|you|he|she|it|we|they|there|here|that|what|when|where|who|how|why)['’](m|re|ve|ll|d|s)\b/gi,
    (match,subject,ending,offset,source)=>{
      const suffix=ending.toLowerCase();
      let [family,full]=suffixes[suffix]||['be','is'];
      const after=source.slice(offset+match.length);
      if(suffix==='d'&&/^\s+(?:better|been|had|already (?:seen|gone)|seen|gone|done|left)\b/i.test(after))full='had';
      if(suffix==='s'&&/^\s+(?:been|gone|done|had|already (?:seen|gone|left))\b/i.test(after)){family='perfect';full='has';}
      if(allowed(family))return match;
      return subject+' '+(ending===ending.toUpperCase()?full.toUpperCase():full);
    });
  return result;
}
function lessonLevelText(text,language=lang,tier=level,index=unit){
  if(typeof text!=='string')return text;
  if(language==='eng')return expandEnglishLesson(text,tier,index);
  if(language==='por'&&tier<2)return text.replace(/\b(pra|pras|pro|pros|tá|tô|tava|cê|cês)\b/gi,match=>{
    const full={pra:'para',pras:'para as',pro:'para o',pros:'para os',tá:'está',tô:'estou',tava:'estava',cê:'você',cês:'vocês'}[match.toLowerCase()];
    return /^[A-Z]/.test(match)?full[0].toUpperCase()+full.slice(1):full;
  });
  if(language==='deu'&&tier<2)return text.replace(/\bgeht['’]s\b/gi,match=>match[0]==='G'?'Geht es':'geht es');
  if(language==='jpn'&&tier<2)return text.replace(/住んでる/g,'住んでいる');
  return text;
}
const contractionMiniLessons=[
  ['be','Afirmativas com be','Junte o pronome ao verbo be em conversas. O apóstrofo fica no lugar da letra que saiu. Em perguntas, coloque o verbo antes do sujeito, como em Are you ready? Use a forma completa em respostas curtas afirmativas: Yes, I am.','I am ready.','I’m ready.','Estou pronto.'],
  ['negative','Negativas no dia a dia','Em muitas negativas, not se junta ao auxiliar. Compare do not com don’t e is not com isn’t. O verbo principal continua igual. A forma completa cannot costuma ser escrita numa palavra e vira can’t na forma reduzida.','I do not have a ticket.','I don’t have a ticket.','Não tenho uma passagem.'],
  ['future','Planos e promessas com will','A terminação ’ll substitui will depois do sujeito. Ela aparece em conversas quando você decide ou promete algo. Na forma completa, will pode receber ênfase.','I will call you later.','I’ll call you later.','Vou ligar para você mais tarde.'],
  ['suggestion','Sugestões com let’s','Use let’s mais o verbo na forma base para sugerir algo que vocês podem fazer juntos. Let us tem as mesmas palavras na origem, mas pode soar mais formal.','Let us meet at nine.','Let’s meet at nine.','Vamos nos encontrar às nove.'],
  ['perfect','Auxiliar have em frases reduzidas','Antes de um particípio, ’ve pode representar have, e ’s pode representar has. Compare She’s arrived com She’s here. O particípio arrived pede has. Here acompanha is.','We have already eaten.','We’ve already eaten.','Já comemos.'],
  ['conditional','O sentido de ’d depende do que vem depois','Antes da forma base, ’d pode ser would. Antes de um particípio, pode ser had. Compare I’d leave com I’d left. Em I’d better go, a construção fixa é had better.','I would wait here.','I’d wait here.','Eu esperaria aqui.']
];
function shortFormsGuide(){
  if(lang!=='eng'){
    const forms={
      spa:['Preposição e artigo','Em espanhol, a + el vira al e de + el vira del. Use Voy al parque, mas Voy a la plaza. Essa junção faz parte da escrita padrão.'],
      ita:['Elisão na escrita italiana','Em l’amica e un’amica, o apóstrofo indica a vogal omitida antes de outra vogal. Compare un’amica com un amico. O masculino un não leva apóstrofo. Em c’è, a expressão ci è perde a vogal de ci. Em all’entrata, a preposição e o artigo aparecem juntos antes da vogal.'],
      deu:['Preposição e artigo','Em alemão, zum é zu + dem, zur é zu + der e im é in + dem. Observe o gênero e o caso do substantivo.'],
      por:[routeLabel('Preposição e artigo','Prepositions and articles','Preposiciones y artículos'),
        routeLabel('Em português, de + o vira do e em + a vira na. Em + uma pode formar numa. Formas informais como pra, tô e tá aparecem a partir do B1.','In Portuguese, de + o becomes do and em + a becomes na. Em + uma can become numa. Informal forms such as pra, tô and tá appear from B1.','En portugués, de + o se convierte en do y em + a en na. Em + uma puede convertirse en numa. Las formas informales como pra, tô y tá aparecen a partir de B1.')]
    };
    const casual={
      deu:['A forma informal geht’s','Na fala, geht’s pode substituir geht es, como em Wie geht’s? O apóstrofo assinala a letra omitida. Use a forma completa se quiser manter um registro mais neutro.'],
      jpn:['Encurtamentos na fala japonesa','Na conversa casual, 住んでいる (sunde iru, morar) pode virar 住んでる (sunderu). O い desaparece. Em situações formais, pratique 住んでいます (sunde imasu).']
    };
    const guide=level===0?forms[lang]:level===2?(casual[lang]|| (lang==='por'?forms.por:null)):null;
    if(!guide)return '';
    const [title,note]=guide;
    return '<details class="grammar-usage"><summary>'+clean(title)+'</summary><p>'+clean(note)+'</p>'+
      (lang==='por'&&level>=2?'<p>'+nativeText('para → pra · estou → tô · está → tá')+'</p>':'')+'</details>';
  }
  const reached=contractionMiniLessons.filter(([kind])=>lessonHasContractions(kind));
  const current=reached.at(-1);
  const intro='<p>Nas primeiras lições, pratique as formas completas. Um apóstrofo também pode indicar posse, como em <bdi lang="en">Lia’s notebook</bdi> (o caderno de Lia), ou fazer parte da expressão <bdi lang="en">o’clock</bdi> para horas exatas.</p>';
  if(!current)return '<details class="grammar-usage"><summary>Como ler o apóstrofo</summary>'+intro+'</details>';
  const [kind]=current;
  const [tier,index]=contractionMilestones[kind];
  const open=level===tier&&unit===index?' open':'';
  return '<details class="grammar-usage"'+open+'><summary>'+clean(current[1])+'</summary>'+
    reached.map(([,title,note,full,short,translation])=>'<div class="contraction-explainer"><strong>'+clean(title)+'</strong><p>'+clean(note)+'</p>'+
      '<p>'+nativeText(full)+lessonPlayButton(full,{compact:true})+'</p><p>'+nativeText(short)+lessonPlayButton(short,{compact:true})+'</p>'+
      '<p class="meta" lang="pt-BR">'+clean(translation)+'</p></div>').join('')+'</details>';
}
