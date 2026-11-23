const sceneVocabulary=Object.fromEntries(Object.entries({
eng:`tea|noun|chá|I ordered a coffee and a tea.|Pedi um café e um chá.|Would you like some tea?|Você gostaria de um pouco de chá?
to go|phrase|para viagem|Is the tea for here or to go?|O chá é para tomar aqui ou para viagem?|Two sandwiches to go, please.|Dois sanduíches para viagem, por favor.
card|noun|cartão|Did you bring today’s card?|Você trouxe o cartão de hoje?|Write one word on each card.|Escreva uma palavra em cada cartão.
voice message|phrase|mensagem de voz|Before class, I got a voice message.|Antes da aula, recebi uma mensagem de voz.|I sent her a voice message.|Mandei uma mensagem de voz para ela.
notes|noun|anotações|Which part of the notes do you want to review?|Qual parte das anotações você quer rever?|I shared my notes with the class.|Compartilhei minhas anotações com a turma.`,
spa:`bocadillo|noun|sanduíche (Espanha)|También pedí un bocadillo para llevar.|Pedi também um sanduíche para viagem.|¿Quieres un bocadillo de queso?|Você quer um sanduíche de queijo?
café con leche|phrase|café com leite|Pedí un café con leche.|Pedi um café com leite.|Me tomo un café con leche al desayunar.|Tomo café com leite no café da manhã.
tarjeta|noun|cartão|¿Trajiste la tarjeta de hoy?|Você trouxe o cartão de hoje?|Escribe la respuesta en la tarjeta.|Escreva a resposta no cartão.
mensaje de voz|phrase|mensagem de voz|Antes de clase recibí un mensaje de voz.|Antes da aula, recebi uma mensagem de voz.|Te dejé un mensaje de voz anoche.|Deixei uma mensagem de voz para você ontem à noite.
apuntes|noun|anotações|¿Qué parte de los apuntes quieres repasar?|Qual parte das anotações você quer rever?|Perdí los apuntes de la última clase.|Perdi as anotações da última aula.`,
ita:`panino|noun|sanduíche|Ho chiesto anche un panino da portare via.|Pedi também um sanduíche para viagem.|Mangio un panino durante la pausa.|Como um sanduíche no intervalo.
sacchetto di carta|phrase|saco de papel|Il panino era in un sacchetto di carta.|O sanduíche veio num saco de papel.|Ho messo il pane in un sacchetto di carta.|Coloquei o pão num saco de papel.
cartoncino|noun|cartão, pedaço de cartolina|Hai portato il cartoncino di oggi?|Você trouxe o cartão de hoje?|Scrivi il tuo nome sul cartoncino.|Escreva seu nome no cartão.
messaggio vocale|phrase|mensagem de voz|Prima della lezione ho ricevuto un messaggio vocale.|Antes da aula, recebi uma mensagem de voz.|Ti mando un messaggio vocale dopo cena.|Vou mandar uma mensagem de voz para você depois do jantar.
appunti|noun|anotações|Quale parte degli appunti vuoi ripassare?|Qual parte das anotações você quer rever?|Ho dimenticato gli appunti a casa.|Esqueci as anotações em casa.`,
deu:`Brötchen|noun|pãozinho; pãezinhos|Dazu habe ich zwei Brötchen bestellt.|Também pedi dois pãezinhos.|Ich esse morgens ein Brötchen.|Como um pãozinho de manhã.
Bäckerei|noun|padaria|Am Morgen bin ich in eine Bäckerei gegangen.|De manhã, parei numa padaria.|Die Bäckerei öffnet um sieben.|A padaria abre às sete.
Karte|noun|cartão, ficha|Hast du die Karte für heute mitgebracht?|Você trouxe o cartão de hoje?|Schreib das Beispiel auf die Karte.|Escreva o exemplo no cartão.
Sprachnachricht|noun|mensagem de voz|Vor dem Unterricht habe ich eine Sprachnachricht bekommen.|Antes da aula, recebi uma mensagem de voz.|Kannst du mir eine Sprachnachricht schicken?|Você pode me mandar uma mensagem de voz?
Notizen|noun|anotações|Welchen Teil der Notizen möchtest du wiederholen?|Qual parte das anotações você quer rever?|Sie hat ihre Notizen mitgebracht.|Ela trouxe as anotações dela.`,
ara:`نَقْدًا|adv|em dinheiro|دَفَعْتُ نَقْدًا وَعُدْتُ إِلَى البَيْتِ.|Paguei em dinheiro e voltei para casa.|سَأَدْفَعُ نَقْدًا.|Vou pagar em dinheiro.
بِالبِطَاقَةِ|phrase|com cartão|هَلْ تُرِيدُ الدَّفْعَ نَقْدًا أَمْ بِالبِطَاقَةِ؟|Você quer pagar em dinheiro ou com cartão?|دَفَعْتُ بِالبِطَاقَةِ فِي المَتْجَرِ.|Paguei com cartão na loja.
بِطَاقَة|noun|cartão, ficha|هَلْ أَحْضَرْتَ بِطَاقَةَ اليَوْمِ؟|Você trouxe o cartão de hoje?|كَتَبْتُ الكَلِمَةَ عَلَى بِطَاقَةٍ.|Escrevi a palavra em um cartão.
رِسَالَة صَوْتِيَّة|phrase|mensagem de voz|تَلَقَّيْتُ رِسَالَةً صَوْتِيَّةً قَبْلَ الدَّرْسِ.|Antes da aula, recebi uma mensagem de voz.|أَرْسَلْتُ رِسَالَةً صَوْتِيَّةً إِلَى صَدِيقِي.|Mandei uma mensagem de voz para meu amigo.
مُلَاحَظَات|noun|anotações|سَنُقَارِنُ مُلَاحَظَاتِنَا فِي الدَّرْسِ القَادِمِ.|Vamos comparar as anotações na próxima aula.|دَوَّنْتُ مُلَاحَظَاتٍ أَثْنَاءَ الدَّرْسِ.|Fiz anotações durante a aula.`,
jpn:`注文する|verb|pedir, fazer um pedido|コーヒーを注文しました。|Pedi um café.|オンラインで本を注文しました。|Pedi um livro pela internet.
店員|noun|atendente, funcionário de loja|店員がふた付きのカップにコーヒーを入れてくれました。|A atendente colocou o café num copo com tampa.|店員に値段を聞きました。|Perguntei o preço ao atendente.
カード|noun|cartão, ficha|今日のカードを持ってきた？|Você trouxe o cartão de hoje?|カードに名前を書いてください。|Escreva seu nome no cartão, por favor.
ボイスメッセージ|noun|mensagem de voz|授業の前にボイスメッセージが届いた。|Antes da aula, recebi uma mensagem de voz.|友達にボイスメッセージを送りました。|Mandei uma mensagem de voz para um amigo.
メモ|noun|anotação|先週のノートに二つのメモを見つけた。|Encontrei duas anotações no caderno da semana passada.|大事なことをメモに書きました。|Escrevi uma informação importante numa anotação.`
}).map(([language,rows])=>[language,rows.split('\n').map(line=>line.split('|'))]));
function lessonLexicon(language){
  const openingThemes=['Comida e bebida','Casa e cidade','Viagem e transporte','Pessoas e relações','Trabalho e estudo','Vocabulário geral'];
  const records=new Map();
  const put=(word,part,gloss,first,firstPt,second,secondPt,theme,flag=part==='phrase'?1:0)=>{
    records.set(word,{theme,row:[word,gloss,part,flag,first,'','',firstPt,'','',gloss,0,'','','','lesson'],
      second:{text:second,translation:secondPt}});
  };
  study[language].forEach((entry,i)=>{
    const [,rawWord,first,firstPt]=entry;
    const [phrase,phrasePt,pFirst,pFirstPt]=phrases[language][i];
    const [second,secondPt,pSecond,pSecondPt]=coreSeconds[language][i];
    const [third,thirdPt,pThird,pThirdPt]=extraOpening[language][i];
    const parts={
      eng:['noun','phrase','verb','phrase','verb','phrase'],
      spa:['noun','phrase','phrase','adj','phrase','phrase'],
      ita:['noun','phrase','phrase','intj','phrase','phrase'],
      deu:['noun','phrase','phrase','adj','phrase','phrase'],
      ara:['noun','phrase','verb','intj','phrase','phrase'],
      jpn:['noun','phrase','verb','adj','phrase','phrase'],
      por:['noun','noun','verb','verb','noun','noun'], cmn:['noun','noun','verb','verb','noun','verb']
    };
    const part=parts[language][i];
    const pPart=i===3&&['spa','ara'].includes(language)?'adj':i===2&&language==='deu'?'verb':'phrase';
    put(rawWord.split(' (')[0],part,glosses[language][i],first,firstPt,second,secondPt,openingThemes[i],i===3?2:undefined);
    put(phrase,pPart,phrasePt,pFirst,pFirstPt,pSecond,pSecondPt,openingThemes[i],i===3?2:undefined);
    records.get(rawWord.split(' (')[0]).third={text:third,translation:thirdPt};
    records.get(phrase).third={text:pThird,translation:pThirdPt};
  });
  sceneVocabulary[language].forEach(([word,part,gloss,first,firstPt,second,secondPt],i)=>
    put(word,part,gloss,first,firstPt,second,secondPt,i<2?'Comida e bebida':'Trabalho e estudo'));
  return records;
}
