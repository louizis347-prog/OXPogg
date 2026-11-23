const lessonSource = {
eng:`Café|coffee|Where can I get a coffee?|Onde posso comprar um café?|Usar can em perguntas|Coloque can antes do sujeito para perguntar sobre possibilidade.|Can I sit here?|Posso sentar aqui?
Direções|around the corner|The station is around the corner.|A estação fica logo na esquina.|Dar direções no imperativo|Comece pelo verbo para indicar o caminho.|Turn left at the bridge.|Vire à esquerda na ponte.
Viagem|put off|We put off the trip until June.|Adiamos a viagem até junho.|Falar de experiências|Use have ou has com particípio para experiências sem data definida.|Have you ever been to Scotland?|Você já esteve na Escócia?
Conversas|no big deal|It's no big deal if we start late.|Tudo bem se começarmos tarde.|Imaginar consequências|Use if + passado e would + verbo para situações hipotéticas no presente.|If I had more time, I would learn German.|Se eu tivesse mais tempo, aprenderia alemão.
Argumentação|come down to|It comes down to whether we can afford it.|A questão é se podemos pagar por isso.|Fazer concessões|Use much as para admitir um ponto antes de defender outro.|Much as I like the plan, it needs more work.|Por mais que eu goste do plano, ele precisa de mais trabalho.
Nuances|a far cry from|The result is a far cry from what we expected.|O resultado está bem longe do que esperávamos.|Inversão enfática|Depois de not until no início da frase, inverta auxiliar e sujeito na oração principal.|Not until she spoke did I understand.|Só entendi quando ela falou.`,
spa:`Café|el café|Quiero un café con leche.|Quero um café com leite.|Pedir com querer|Use quiero + substantivo ou infinitivo para expressar o que você quer.|Quiero pedir la cuenta.|Quero pedir a conta.
Direções|a la vuelta de la esquina|La farmacia está a la vuelta de la esquina.|A farmácia fica logo na esquina.|Localizar com estar|Use estar para dizer onde fica um lugar específico.|El museo está enfrente del parque.|O museu fica em frente ao parque.
Viagem|hacer las maletas|Mañana hacemos las maletas.|Amanhã fazemos as malas.|Contar fatos e descrever o cenário|Use o pretérito indefinido para o evento e o imperfeito para o pano de fundo.|Cuando llegué, llovía.|Quando cheguei, estava chovendo.
Conversas|guay (Espanha, informal)|¡Qué guay que hayas venido!|Que legal que você veio!|Reagir com o subjuntivo|Use o subjuntivo depois de expressões de emoção com que.|Me alegra que estés aquí.|Fico feliz que você esteja aqui.
Argumentação|poner en tela de juicio|El estudio pone en tela de juicio esa conclusión.|O estudo põe essa conclusão em dúvida.|Conceder com aunque|Use aunque + subjuntivo ao tratar o fato como hipótese ou como secundário ao argumento.|Aunque resulte caro, merece la pena.|Mesmo que saia caro, vale a pena.
Nuances|ni mucho menos|El asunto no está resuelto, ni mucho menos.|A questão está longe de estar resolvida.|Hipótese contrária no passado|Combine si + mais-que-perfeito do subjuntivo com o condicional composto.|Si lo hubiera sabido, habría llamado.|Se eu soubesse, teria ligado.`,
ita:`Café|il caffè|Prendo un caffè, per favore.|Vou querer um café, por favor.|Pedir com vorrei|Use vorrei + substantivo ou infinitivo para fazer um pedido cortês.|Vorrei un bicchiere d’acqua.|Eu gostaria de um copo de água.
Direções|dietro l’angolo|La farmacia è dietro l’angolo.|A farmácia fica logo na esquina.|Preposições de lugar|Use a com cidades e in com países na maioria dos casos.|Abito a Roma, in Italia.|Moro em Roma, na Itália.
Viagem|fare le valigie|Stasera devo fare le valigie.|Hoje à noite preciso fazer as malas.|Contrastar ação e cenário|Use o passato prossimo para o acontecimento e o imperfetto para descrever a situação.|Quando sono uscito, pioveva.|Quando saí, estava chovendo.
Conversas|boh (informal)|Boh, forse è già a casa.|Sei lá, talvez já esteja em casa.|Expressar opinião|Use o congiuntivo depois de penso che no italiano padrão.|Penso che sia a casa.|Acho que está em casa.
Argumentação|mettere in discussione|I dati mettono in discussione questa teoria.|Os dados põem essa teoria em questão.|Fazer concessões com benché|Use benché com o congiuntivo para admitir um obstáculo.|Benché fosse tardi, abbiamo continuato.|Embora fosse tarde, continuamos.
Nuances|a conti fatti|A conti fatti, ne è valsa la pena.|No fim das contas, valeu a pena.|Imaginar um passado diferente|Use se + congiuntivo trapassato na condição e condizionale passato no resultado.|Se l’avessi saputo, ti avrei chiamato.|Se eu soubesse, teria te ligado.`,
deu:`Café|der Kaffee|Ich hätte gern einen Kaffee.|Eu gostaria de um café.|Pedir com hätte gern|Combine ich hätte gern com um substantivo no acusativo.|Ich hätte gern einen Tee.|Eu gostaria de um chá.
Direções|um die Ecke|Die Apotheke ist gleich um die Ecke.|A farmácia fica logo na esquina.|Indicar movimento e posição|Com in, use acusativo para destino e dativo para localização.|Ich gehe in den Park. Ich bin im Park.|Vou ao parque. Estou no parque.
Viagem|Koffer packen|Heute Abend packe ich meinen Koffer.|Hoje à noite faço a mala.|Passado na conversa|Use o Perfekt com auxiliar conjugado e particípio no fim.|Wir haben die Fahrkarten gekauft.|Compramos as passagens.
Conversas|krass (informal)|Das war echt krass!|Isso foi muito intenso!|Hipóteses com Konjunktiv II|Use hätte e würde para formular uma condição imaginária e seu resultado.|Wenn ich mehr Zeit hätte, würde ich öfter reisen.|Se tivesse mais tempo, viajaria mais.
Argumentação|in Frage stellen|Die Ergebnisse stellen die These in Frage.|Os resultados colocam a tese em dúvida.|Relatar falas no Konjunktiv I|Em textos jornalísticos, use formas como sei para atribuir uma declaração a alguém.|Sie sagte, der Termin sei abgesagt.|Ela disse que o compromisso foi cancelado.
Nuances|geschweige denn|Er hat keine Zeit zum Lesen, geschweige denn zum Schreiben.|Ele não tem tempo para ler, muito menos para escrever.|Concessão sem conjunção inicial|Com so + adjetivo + auch, você pode destacar uma ressalva antes da oração principal.|So überzeugend das klingt, es bleiben Fragen offen.|Por mais convincente que pareça, ainda há questões em aberto.`,
ara:`Café|قَهْوَة|أُرِيدُ قَهْوَةً، مِنْ فَضْلِكَ.|Quero um café, por favor.|Pedir com أريد|Use أريد antes do que você quer. مِنْ فَضْلِكَ se dirige a um homem e مِنْ فَضْلِكِ a uma mulher.|أُرِيدُ كُوبَ شَايٍ.|Quero uma xícara de chá.
Direções|بِالْقُرْبِ مِنْ|الصَّيْدَلِيَّةُ بِالْقُرْبِ مِنَ الْمَحَطَّةِ.|A farmácia fica perto da estação.|Localizar em uma frase nominal|No presente, uma frase como المتحف قريب geralmente dispensa um verbo equivalente a estar.|الْمَتْحَفُ قَرِيبٌ.|O museu fica perto.
Viagem|حَجَزَ|حَجَزْتُ غُرْفَةً لِلَيْلَتَيْنِ.|Reservei um quarto para duas noites.|Contar no passado|Em verbos regulares, o sufixo ـتُ indica a primeira pessoa do singular do passado.|وَصَلْتُ أَمْسِ.|Cheguei ontem.
Conversas|ماشي (egípcio, informal)|ماشي، أشوفك بكرة.|Beleza, te vejo amanhã.|Expressar uma hipótese com لو|Use لو para introduzir uma condição hipotética e لَ na resposta afirmativa em construções formais como esta.|لَوْ كَانَ لَدَيَّ وَقْتٌ لَسَافَرْتُ.|Se eu tivesse tempo, viajaria.
Argumentação|وَضَعَ مَوْضِعَ الشَّكِّ|وَضَعَ التَّقْرِيرُ النَّتَائِجَ مَوْضِعَ الشَّكِّ.|O relatório pôs os resultados em dúvida.|Conceder com رغم أن|Use رغم أنَّ para introduzir um fato que poderia contrariar o que se afirma em seguida.|رَغْمَ أَنَّ الطَّرِيقَ طَوِيلٌ، سَنَذْهَبُ سَيْرًا.|Embora o caminho seja longo, iremos a pé.
Nuances|نَاهِيكَ عَنْ|الْمَشْرُوعُ مُكْلِفٌ، نَاهِيكَ عَنْ صُعُوبَةِ تَنْفِيذِهِ.|O projeto é caro, sem falar na dificuldade de executá-lo.|Limitar uma afirmação com إنما|Use إنما para introduzir uma restrição ou enquadrar o único ponto em foco.|إِنَّمَا الْمَقْصُودُ تَوْضِيحُ الْفِكْرَةِ.|O objetivo é apenas esclarecer a ideia.`,
jpn:`Café|コーヒー (kōhī)|コーヒーをください。|Um café, por favor.|Pedir com をください|Use objeto + をください para pedir algo de forma cortês.|水をください。|Água, por favor.
Direções|角を曲がる (kado o magaru)|次の角を右に曲がってください。|Vire à direita na próxima esquina.|Formular um pedido com てください|Acrescente ください à forma て do verbo para pedir uma ação.|ここで待ってください。|Espere aqui, por favor.
Viagem|予約する (yoyaku suru)|ホテルを予約しました。|Reservei um hotel.|Falar de experiências com たことがある|Use a forma た seguida de ことがある para dizer que já fez algo.|京都に行ったことがあります。|Já fui a Quioto.
Conversas|やばい (yabai, informal)|このケーキ、やばいくらいおいしい。|Esse bolo é absurdamente gostoso.|Expressar contraste com のに|Use のに quando o resultado contraria uma expectativa.|たくさん勉強したのに、緊張した。|Mesmo tendo estudado muito, fiquei nervoso.
Argumentação|疑問を呈する (gimon o tei suru)|専門家はその結論に疑問を呈した。|Especialistas questionaram essa conclusão.|Conceder com とはいえ|Use とはいえ para reconhecer um ponto e, em seguida, introduzir uma ressalva.|便利だとはいえ、料金は高い。|Embora seja conveniente, a tarifa é alta.
Nuances|言うまでもない (iu made mo nai)|準備が大切なのは言うまでもない。|Nem é preciso dizer que a preparação é importante.|Dar destaque com こそ|Use こそ para destacar com ênfase o elemento apresentado como decisivo.|今こそ決断すべきだ。|É justamente agora que devemos tomar uma decisão.`
};
const study=Object.fromEntries(Object.entries(lessonSource).map(([key,list])=>[key,list.split('\n').map(x=>x.split('|'))]));
const glosses={
  eng:['café','logo na esquina','adiar','nada de mais','se resumir a','bem distante de'],
  spa:['café','logo na esquina','fazer as malas','legal, bacana','pôr em dúvida','nem de longe'],
  ita:['café','logo na esquina','fazer as malas','sei lá','questionar','no fim das contas'],
  deu:['café','logo na esquina','fazer as malas','intenso, impressionante','pôr em dúvida','muito menos'],
  ara:['café','perto de','reservar','beleza, combinado','pôr em dúvida','sem falar em'],
  jpn:['café','virar na esquina','reservar','absurdo, impressionante','questionar','nem é preciso dizer']
};
const phrases={
  eng:[
    ['for here','para consumir aqui','A tea for here, please.','Um chá para tomar aqui, por favor.'],
    ['How do I get to…?','Como chego a…?','How do I get to the city center?','Como chego ao centro da cidade?'],
    ['check in','fazer o check-in','Can we check in before noon?','Podemos fazer o check-in antes do meio-dia?'],
    ['I’m down','eu topo (informal)','Pizza tonight? I’m down.','Pizza hoje à noite? Eu topo.'],
    ['on balance','considerando os prós e contras','On balance, the benefits outweigh the costs.','Considerando os prós e contras, os benefícios superam os custos.'],
    ['for all its flaws','apesar de todos os seus defeitos','For all its flaws, the proposal sparked a useful debate.','Apesar de todos os seus defeitos, a proposta abriu um debate produtivo.']
  ],
  spa:[
    ['para llevar','para viagem','Un café para llevar, por favor.','Um café para viagem, por favor.'],
    ['¿Queda lejos?','Fica longe?','¿Queda lejos la estación?','A estação fica longe?'],
    ['el billete de ida y vuelta','a passagem de ida e volta','Compré un billete de ida y vuelta.','Comprei uma passagem de ida e volta.'],
    ['chévere','legal, bacana (em vários países da América Latina)','¡Qué chévere quedó el mural!','Que legal que ficou o mural!'],
    ['a grandes rasgos','em linhas gerais','Voy a explicar el proyecto a grandes rasgos.','Vou explicar o projeto em linhas gerais.'],
    ['huelga decir','nem é preciso dizer (formal)','Huelga decir que los datos son confidenciales.','Nem é preciso dizer que os dados são confidenciais.']
  ],
  ita:[
    ['da portare via','para viagem','Un panino da portare via, per favore.','Um sanduíche para viagem, por favor.'],
    ['a piedi','a pé','Il museo è a dieci minuti a piedi.','O museu fica a dez minutos a pé.'],
    ['andata e ritorno','ida e volta','Vorrei un biglietto di andata e ritorno.','Gostaria de uma passagem de ida e volta.'],
    ['dai','ah, vai / vamos lá (informal)','Dai, vieni anche tu!','Ah, vai, vem você também!'],
    ['in linea di massima','em princípio, em linhas gerais','In linea di massima sono d’accordo.','Em princípio, estou de acordo.'],
    ['per quanto mi consta','até onde sei (formal)','Per quanto mi consta, non ci sono novità.','Até onde sei, não há novidades.']
  ],
  deu:[
    ['zum Mitnehmen','para viagem','Einen Kaffee zum Mitnehmen, bitte.','Um café para viagem, por favor.'],
    ['zu Fuß','a pé','Wir gehen zu Fuß zum Bahnhof.','Vamos a pé até a estação.'],
    ['umsteigen','fazer baldeação','Müssen wir in Köln umsteigen?','Precisamos fazer baldeação em Colônia?'],
    ['Bock haben','estar a fim (informal)','Hast du Bock auf Kino?','Está a fim de ir ao cinema?'],
    ['unter dem Strich','no fim das contas','Unter dem Strich hat sich der Aufwand gelohnt.','No fim das contas, o esforço valeu a pena.'],
    ['es sei denn','a menos que','Wir treffen uns draußen, es sei denn, es regnet.','Vamos nos encontrar ao ar livre, a menos que chova.']
  ],
  ara:[
    ['الحِسَابُ، مِنْ فَضْلِكَ','A conta, por favor (dirigido a um homem)','الحِسَابُ، مِنْ فَضْلِكَ. سَأَدْفَعُ نَقْدًا.','A conta, por favor. Vou pagar em dinheiro.'],
    ['عَلَى الأَقْدَامِ','a pé','ذَهَبْنَا إِلَى السُّوقِ عَلَى الأَقْدَامِ.','Fomos a pé ao mercado.'],
    ['ذَهَابًا وَإِيَابًا','ida e volta','أُرِيدُ تَذْكِرَةً ذَهَابًا وَإِيَابًا.','Quero uma passagem de ida e volta.'],
    ['جامد','muito bom, incrível (egípcio, informal)','الفيلم ده جامد أوي!','Esse filme é incrível!'],
    ['مِنْ حَيْثُ المَبْدَأِ','em princípio','أُوَافِقُ عَلَى الفِكْرَةِ مِنْ حَيْثُ المَبْدَأِ.','Em princípio, concordo com a ideia.'],
    ['خَيْرُ دَلِيلٍ عَلَى ذَلِكَ','a melhor prova disso','وَخَيْرُ دَلِيلٍ عَلَى ذَلِكَ نَتَائِجُ التَّجْرِبَةِ.','E a melhor prova disso são os resultados do experimento.']
  ],
  jpn:[
    ['持ち帰りで','para viagem (mochikaeri de)','持ち帰りでお願いします。','Para viagem, por favor.'],
    ['歩いて','a pé (aruite)','駅まで歩いて十分です。','Até a estação são dez minutos a pé.'],
    ['乗り換える','trocar de linha ou veículo (norikaeru)','新宿で電車を乗り換えます。','Vou trocar de trem em Shinjuku.'],
    ['マジで','sério, de verdade (maji de, informal)','マジで知らなかった。','Eu não sabia, sério.'],
    ['一概には言えない','não dá para generalizar (ichigai ni wa ienai)','どちらが正しいかは一概には言えない。','Não dá para dizer de forma geral qual dos dois está certo.'],
    ['あえて','deliberadamente, por escolha (aete)','あえて難しい道を選んだ。','Escolhi deliberadamente o caminho mais difícil.']
  ]
};
const starterEntries={
eng:`be|verb|to be; to exist or have a quality|ser, estar|I am ready.|Estou pronto.
the|det|the definite article|o, a, os, as|The door is open.|A porta está aberta.
to|prep|in the direction of|para, a|We’re going to the library.|Vamos à biblioteca.
one|num|the number 1|um, uma|I have one ticket.|Tenho uma passagem.
first|adj|coming before all others|primeiro|This is my first lesson.|Esta é minha primeira lição.
I|pron|the first-person singular subject pronoun|eu|I live near the station.|Eu moro perto da estação.
a|det|the indefinite article before a consonant sound|um, uma|I’d like a coffee.|Eu gostaria de um café.
you|pron|the person or people addressed|você, vocês|Are you ready?|Você está pronto?
and|conj|connects words or clauses|e|I bought bread and cheese.|Comprei pão e queijo.
have|verb|to possess|ter|I have two brothers.|Tenho dois irmãos.
go|verb|to move from one place to another|ir|I go to work by bus.|Vou ao trabalho de ônibus.
coffee|noun|a drink made from roasted coffee beans|café|I drink coffee in the morning.|Tomo café de manhã.`,
spa:`ser|verb|expresses identity or characteristics|ser|Soy de Brasil.|Sou do Brasil.
de|prep|indicates origin or possession|de|Ella es de Perú.|Ela é do Peru.
la|det|feminine singular definite article|a|La puerta está abierta.|A porta está aberta.
que|conj|introduces a subordinate clause|que|Creo que viene mañana.|Acho que vem amanhã.
no|adv|expresses negation|não|No entiendo la pregunta.|Não entendo a pergunta.
a|prep|indicates direction or destination|a, para|Voy a la biblioteca.|Vou à biblioteca.
en|prep|indicates location or means of transport|em, de|Viajo en autobús.|Viajo de ônibus.
estar|verb|to be in a place or state|estar|Estamos en casa.|Estamos em casa.
haber|verb|exists as hay in impersonal use|haver, ter|Hay una farmacia cerca.|Tem uma farmácia perto.
se|pron|a reflexive pronoun|se|Ana se lava las manos.|Ana lava as mãos.
tener|verb|to possess|ter|Tengo dos hermanas.|Tenho duas irmãs.
ir|verb|to move toward a place|ir|Vamos al cine.|Vamos ao cinema.`,
ita:`non|adv|expresses negation|não|Non ho fame.|Não estou com fome.
a|prep|indicates direction or location|a, em|Domani vado a Roma.|Amanhã vou a Roma.
essere|verb|to be|ser, estar|Sono a casa.|Estou em casa.
di|prep|indicates origin or possession|de|Sono di Bologna.|Sou de Bolonha.
che|conj|introduces a subordinate clause|que|So che sei qui.|Sei que você está aqui.
in|prep|indicates location or direction|em, para|Vivo in Italia.|Moro na Itália.
la|det|feminine singular definite article|a|La farmacia è aperta.|A farmácia está aberta.
avere|verb|to have or possess|ter|Abbiamo due biglietti.|Temos dois ingressos.
per|prep|indicates purpose or beneficiary|para|Ho un regalo per te.|Tenho um presente para você.
io|pron|the first-person singular subject pronoun|eu|Io parlo portoghese.|Eu falo português.
le|det|feminine plural definite article|as|Le finestre sono aperte.|As janelas estão abertas.
mi|pron|unstressed first-person object pronoun|me|Mi senti bene?|Você me ouve bem?`,
deu:`sein|verb|to be|ser, estar|Ich bin zu Hause.|Estou em casa.
ich|pron|the first-person singular subject pronoun|eu|Ich lerne Deutsch.|Eu estudo alemão.
haben|verb|to have|ter|Wir haben Zeit.|Temos tempo.
einen|det|masculine accusative form of the indefinite article|um|Ich hätte gern einen Kaffee.|Eu gostaria de um café.
nicht|adv|negates a verb or phrase|não|Ich verstehe das nicht.|Eu não entendo isso.
sie|pron|third-person pronoun for she or they|ela, eles, elas|Sie wohnt in Berlin.|Ela mora em Berlim.
das|det|neuter singular definite article|o, a|Das Fenster ist offen.|A janela está aberta.
der|det|masculine nominative definite article|o|Der Zug kommt gleich.|O trem chega já.
werden|verb|to become; also used as a future auxiliary|tornar-se, ficar|Es wird kalt.|Está ficando frio.
zu|prep|toward a destination or person|a, para|Wir gehen zum Bahnhof.|Vamos à estação.
du|pron|informal singular you|você, tu|Kommst du morgen?|Você vem amanhã?
gehen|verb|to go; to walk|ir, andar|Wir gehen zu Fuß.|Vamos a pé.`,
ara:`في|prep|in, at|em|أَنَا فِي البَيْتِ.|Estou em casa.|fī
من|prep|from|de, a partir de|أَنَا مِنَ البَرَازِيلِ.|Sou do Brasil.|min
أن|conj|that, introducing a subordinate clause in this example|que|أُرِيدُ أَنْ أَذْهَبَ.|Quero ir.|ʾan
لا|particle|negates the present tense in this example|não|لَا أَفْهَمُ السُّؤَالَ.|Não entendo a pergunta.|lā
كان|verb|to be in the past|ser, estar no passado|كَانَ الجَوُّ بَارِدًا.|O tempo estava frio.|kāna
هل|particle|introduces a yes–no question|partícula interrogativa|هَلْ أَنْتَ جَاهِزٌ؟|Você está pronto?|hal
لم|particle|negates a past action with a jussive verb|não, em ação passada|لَمْ أَذْهَبْ إِلَى السُّوقِ.|Não fui ao mercado.|lam
على|prep|on, upon|sobre, em cima de|الكِتَابُ عَلَى الطَّاوِلَةِ.|O livro está sobre a mesa.|ʿalā
إلى|prep|to, toward|a, para|ذَهَبْتُ إِلَى الطَّبِيبِ.|Fui ao médico.|ʾilā
هذا|pron|this, for a masculine singular referent|este, isto|هَذَا كِتَابٌ جَدِيدٌ.|Este é um livro novo.|hādhā
ما|pron|what, when used as an interrogative|o que, qual|مَا اسْمُكَ؟|Qual é o seu nome?|mā
أنا|pron|first-person singular pronoun|eu|أَنَا أَتَعَلَّمُ العَرَبِيَّةَ.|Estou aprendendo árabe.|ʾanā`,
jpn:`彼|pron|he; him|ele|彼は先生です。|Ele é professor.|かれ · kare
私|pron|I; me|eu|私はブラジル人です。|Sou do Brasil.|わたし · watashi
彼女|pron|she; her|ela|彼女は東京に住んでいます。|Ela mora em Tóquio.|かのじょ · kanojo
人|noun|person; human being|pessoa|あの人は誰ですか。|Quem é aquela pessoa?|ひと · hito
何|pron|what|o que|何を食べますか。|O que você vai comer?|なに · nani
君|pron|you, often used among peers or toward juniors|você, tu|君も行く？|Você também vai?|きみ · kimi
話|noun|talk; story|conversa, história|面白い話を聞きました。|Ouvi uma história interessante.|はなし · hanashi
行く|verb|to go|ir|明日、京都に行きます。|Amanhã vou a Quioto.|いく · iku
見る|verb|to see; to watch|ver, assistir|映画を見ます。|Vou assistir a um filme.|みる · miru
食べる|verb|to eat|comer|朝ご飯を食べます。|Tomo café da manhã.|たべる · taberu
水|noun|water|água|水をください。|Água, por favor.|みず · mizu
本|noun|book|livro|この本は面白いです。|Este livro é interessante.|ほん · hon`
};
function localizedEntries(language,rows){
  const edited=new Map();
  const key=w=>w.normalize('NFC').toLowerCase();
  for(const line of starterEntries[language].split('\n')){
    const [word,part,definition,ptWord,example,pt,reading]=line.split('|');
    edited.set(key(word),[word,definition,part,0,example,'','',pt,reading||'','',ptWord,0,'','','','original']);
  }
  const rest=rows.filter(row=>!edited.has(key(row[0])));
  return [...edited.values(),...rest].slice(0,rows.length);
}
