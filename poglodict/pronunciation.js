const pronunciationTopics={
  eng:[
    ['/iː/','Mantenha a língua alta e à frente, com os lábios relaxados.',['see','green','meet','street','please']],
    ['/ɪ/','Relaxe a língua um pouco em relação ao som de “ee” em see.',['sit','fish','milk','ticket','visit']],
    ['/æ/','Abra a mandíbula e mantenha a língua na frente da boca.',['cat','map','bag','plan','back']],
    ['/θ/','Encoste a ponta da língua de leve entre os dentes e deixe o ar passar sem vibrar a garganta.',['think','three','thank','bath','both']],
    ['/ʃ/','Deixe escapar um fluxo contínuo de ar. O som começa como o “ch” de chuva.',['shop','ship','she','short','wash']],
    ['[ɾ] · t americano','Entre a vogal tônica e uma vogal átona, o t destas palavras costuma sair como um toque rápido da língua no inglês americano.',['city','water','better','later','pretty']]
  ],
  spa:[
    ['/ɲ/ · ñ','Levante o meio da língua contra o céu da boca e deixe o ar passar pelo nariz, como no “nh” português.',['año','baño','niño','mañana','señal']],
    ['/ɾ/ · r breve','Dê um toque rápido com a ponta da língua atrás dos dentes superiores.',['pero','caro','cero','cara','mira']],
    ['/r/ · r vibrante','Deixe a ponta da língua solta para vibrar atrás dos dentes superiores.',['perro','carro','torre','rojo','ropa']],
    ['j / x','Na pronúncia com [x], deixe a parte de trás da língua se aproximar do céu da boca. Em muitas regiões, o som é mais suave, próximo de [h].',['jamón','jardín','joven','caja','ojo']],
    ['/tʃ/ · ch','Bloqueie o ar por um instante e solte-o com um chiado, como em “tchau”.',['chico','chica','chocolate','leche','noche']],
    ['Acento na última sílaba','Diga a última sílaba com mais destaque. Nestas palavras, a marca escrita indica onde cai o acento.',['café','sofá','menú','limón','canción']]
  ],
  ita:[
    ['/tʃ/ · c antes de e ou i','Comece com uma breve oclusão e solte o ar com um chiado, como em “tchau”.',['cena','cinema','certo','centro','cibo']],
    ['/k/ · ch','Faça o som de “c” em casa. Em italiano, o h mantém esse som antes de e ou i.',['che','chi','chiesa','chiave','chiedere']],
    ['/ɲ/ · gn','Una o meio da língua ao céu da boca, como no “nh” de manhã.',['bagno','sogno','legno','ragno','gnocchi']],
    ['/ʃ/ · sc antes de e ou i','O ar sai continuamente, como no “ch” de chuva.',['scena','scelta','scimmia','scendere','scienza']],
    ['/tː/ · tt','Segure por um instante o contato da língua antes de soltar o t.',['notte','latte','gatto','tutto','otto']],
    ['/ʎ/ · gli','Levante o meio da língua e deixe o ar sair pelas laterais, como no “lh” de milho.',['figlio','figlia','foglia','moglie','meglio']]
  ],
  deu:[
    ['/ç/ · ch de ich','Aproxime o meio da língua do palato e solte ar sem usar a voz.',['ich','mich','dich','Licht','Milch']],
    ['/x/ · ch de Bach','Aproxime a parte de trás da língua do palato mole e deixe o ar raspar de leve.',['Bach','Buch','Dach','Nacht','auch']],
    ['/aɪ̯/ · ei','Passe de um som aberto para um som próximo de i dentro de uma só sílaba.',['ein','Eis','mein','Zeit','klein']],
    ['/ɔʏ̯/ · eu, äu','Comece com os lábios arredondados e deslize para um som mais fechado, mantendo-os arredondados.',['neu','heute','Leute','Freund','Häuser']],
    ['/yː/ · ü','Posicione a língua como num i e arredonde os lábios como num u.',['Tür','grün','müde','üben','süß']],
    ['/ʃ/ · sch','Faça um chiado contínuo, como o “ch” em chuva.',['Schule','Schuh','Schiff','Fisch','Tisch']]
  ],
  ara:[
    ['/ħ/ · ح','Deixe o ar passar de modo contínuo, estreitando levemente a garganta sem pôr voz.',[['حَلِيب','ḥalīb'],['حُبّ','ḥubb'],['حِصَان','ḥiṣān'],['مِفْتَاح','miftāḥ'],['بَحْر','baḥr']]],
    ['/x/ · خ','Aproxime o dorso da língua do palato mole. Deixe o ar passar com atrito.',[['خُبْز','khubz'],['خَمْسَة','khamsa'],['خَرِيف','kharīf'],['أَخ','akh'],['مَطْبَخ','maṭbakh']]],
    ['/ʕ/ · ع','Use a voz e faça uma leve constrição na garganta. Evite forçar.',[['عَيْن','ʿayn'],['عِنَب','ʿinab'],['عَسَل','ʿasal'],['عَلَم','ʿalam'],['عَرَبِيّ','ʿarabiyy']]],
    ['/q/ · ق','Toque a parte de trás do céu da boca com o dorso da língua e solte. Este é o som de referência no árabe padrão.',[['قَلَم','qalam'],['قَمَر','qamar'],['قَلْب','qalb'],['قِطَار','qiṭār'],['وَرَق','waraq']]],
    ['/ʃ/ · ش','Solte um chiado contínuo, como o “ch” de chuva.',[['شَمْس','shams'],['شَجَرَة','shajara'],['شَاي','shāy'],['شَارِع','shāriʿ'],['مِشْمِش','mishmish']]],
    ['/aː/ · ا','Sustente a vogal a por mais tempo onde aparecer o alif longo.',[['بَاب','bāb'],['نَار','nār'],['مَال','māl'],['كِتَاب','kitāb'],['سَاعَة','sāʿa']]]
  ],
  jpn:[
    ['Vogal longa · ー','No katakana, ー estende a vogal anterior por uma batida a mais.',[['ケーキ','kēki'],['コーヒー','kōhī'],['チーズ','chīzu'],['ジュース','jūsu'],['スープ','sūpu']]],
    ['Consoante dupla · っ','Segure a consoante seguinte por uma batida antes de soltá-la.',[['きって','kitte'],['きっぷ','kippu'],['がっこう','gakkō'],['ざっし','zasshi'],['にっき','nikki']]],
    ['Som nasal · ん','Dê uma batida própria a ん. A posição da língua pode mudar com o som seguinte.',[['ほん','hon'],['パン','pan'],['りんご','ringo'],['てんき','tenki'],['さんぽ','sanpo']]],
    ['[ɾ] · série de ら','Dê um toque breve com a língua na região logo atrás dos dentes superiores.',[['さくら','sakura'],['そら','sora'],['りす','risu'],['くるま','kuruma'],['れきし','rekishi']]],
    ['[ɸ] · ふ','Aproxime os dois lábios e sopre suavemente por entre eles.',[['ふね','fune'],['ふゆ','fuyu'],['ふく','fuku'],['ふた','futa'],['ふろ','furo']]],
    ['[ɕ] · し','Faça um chiado com a lâmina da língua alta e os lábios pouco arredondados.',[['しお','shio'],['した','shita'],['しろ','shiro'],['ほし','hoshi'],['すし','sushi']]]
  ],
  cmn:[
    ['1º tom · alto e estável','Sustente a nota no alto, sem subir ou descer no meio da sílaba.',[['猫','māo'],['书','shū'],['天','tiān'],['杯','bēi'],['山','shān']]],
    ['2º tom · ascendente','Comece numa altura média e suba até o fim da sílaba.',[['茶','chá'],['人','rén'],['门','mén'],['鱼','yú'],['糖','táng']]],
    ['3º tom · baixo','Na fala corrida, mantenha a nota baixa. Isolado, o tom pode descer e depois subir.',[['马','mǎ'],['水','shuǐ'],['手','shǒu'],['纸','zhǐ'],['米','mǐ']]],
    ['4º tom · descendente','Comece numa nota alta e faça uma queda firme na mesma sílaba.',[['饭','fàn'],['店','diàn'],['路','lù'],['票','piào'],['树','shù']]],
    ['q · [tɕʰ]','Com a língua perto do palato, solte a consoante com um sopro perceptível.',[['七','qī'],['气','qì'],['请','qǐng'],['球','qiú'],['前','qián']]],
    ['x · [ɕ]','Eleve a frente da língua e faça o ar passar com um chiado fino.',[['西','xī'],['小','xiǎo'],['鞋','xié'],['新','xīn'],['下','xià']]]
  ],
  por:[
    ['nh · /ɲ/','Aproxime o meio da língua do céu da boca e deixe o ar sair pelo nariz.',['banho','manhã','sonho','vinho','linha']],
    ['lh · /ʎ/','Levante o meio da língua e faça o ar passar pelas laterais.',['filho','folha','olho','milho','melhor']],
    ['-ão · /ɐ̃w̃/','Comece com a vogal nasal e feche os lábios gradualmente num deslize.',['pão','mão','chão','avião','coração']],
    ['r breve · [ɾ]','Dê um toque rápido com a língua atrás dos dentes de cima.',['caro','muro','pera','arara','barato']],
    ['j · /ʒ/','Faça um chiado contínuo e mantenha a vibração da voz.',['jogo','janela','jantar','ajuda','loja']],
    ['ch · /ʃ/','Deixe o ar chiar com a voz desligada.',['chá','chave','chuva','chão','chato']]
  ]
};

const pronunciationMoreTopics={
  eng:[
    ['/v/','Encoste os dentes superiores no lábio inferior e mantenha a voz enquanto o ar passa.',['van','voice','visit','leave','move']],
    ['/ŋ/ · ng','Feche a passagem na parte de trás da boca e deixe o ar sair pelo nariz, sem acrescentar um g final.',['sing','ring','long','song','bring']],
    ['/dʒ/','Bloqueie o ar rapidamente e solte a consoante com um chiado sonoro.',['job','jam','June','age','page']],
    ['/eɪ/','Deslize de uma vogal média em direção a i sem dividir o som em duas sílabas.',['day','name','cake','train','rain']],
    ['-ed · /t/','Nestas formas do passado, o -ed soa como t e não acrescenta sílaba.',['worked','walked','watched','helped','washed']],
    ['-ed · /ɪd/','Depois de t ou d, o -ed acrescenta uma sílaba nestes exemplos.',['wanted','needed','started','ended','waited']]
  ],
  spa:[
    ['h muda','Comece pela vogal. O h escrito fica sem som nestas palavras.',['hola','hora','hilo','huevo','humo']],
    ['/k/ · qu','Antes de e ou i, qu representa o som de casa. O u fica mudo.',['queso','quince','quitar','equipo','paquete']],
    ['/ɡ/ inicial','Feche brevemente a passagem do ar com o dorso da língua ao iniciar estas palavras isoladas.',['gato','goma','gusto','gota','gorro']],
    ['Acento na antepenúltima','Conte três sílabas do fim para o começo e dê destaque à terceira.',['sábado','música','pájaro','rápido','médico']],
    ['Duas sílabas · hiato','Dê uma batida a cada vogal no encontro com í tônico.',['país','maíz','raíz','río','día']],
    ['Ditongo · ie','Passe rapidamente do som de i para e no mesmo impulso.',['pie','bien','miel','piel','cielo']]
  ],
  ita:[
    ['/dʒ/ · g antes de e ou i','Comece com um breve bloqueio de ar e termine com um chiado sonoro.',['gente','giro','gelato','gesto','gesso']],
    ['/ɡ/ · gh','O h mantém o som de g de gato antes de e ou i.',['ghetto','ghiro','spaghetti','aghi','laghi']],
    ['/pː/ · pp','Mantenha os lábios fechados por um instante a mais antes de soltar o ar.',['troppo','doppio','zuppa','coppa','tappo']],
    ['/lː/ · ll','Demore um pouco mais no contato da língua antes de passar à vogal seguinte.',['bello','quello','sella','colla','palla']],
    ['Acento final','Dê mais destaque à última vogal, que vem marcada com acento escrito.',['città','caffè','perché','virtù','così']],
    ['/f/','Deixe o ar passar entre os dentes de cima e o lábio de baixo, sem vibrar a garganta.',['fare','foto','festa','fame','fiume']]
  ],
  deu:[
    ['/ʃt/ · st inicial','Quando estas palavras começam com st, faça um breve chiado antes do t.',['Stadt','Stein','still','Stuhl','Straße']],
    ['/ʃp/ · sp inicial','Faça um breve som de “ch” antes do p nestes começos de palavra.',['Spiel','Sport','spät','Spaß','Spiegel']],
    ['/ts/ · z','Solte t e s em sequência rápida, como uma só consoante.',['Zeit','Zahl','Zug','Zahn','Zimmer']],
    ['/aʊ̯/ · au','Comece com a boca aberta e deslize para uma vogal próxima de u.',['Haus','Maus','Baum','laut','blau']],
    ['/f/ · v inicial','Neste conjunto de palavras alemãs, o v soa como f.',['Vater','Vogel','Volk','viel','voll']],
    ['/p/ no final','Nestas palavras isoladas, o b final perde a vibração e soa como p.',['Dieb','Lob','gelb','Korb','Kalb']]
  ],
  ara:[
    ['/θ/ · ث','Ponha a ponta da língua perto da borda dos dentes e deixe passar ar sem voz.',[['ثَلَاثَة','thalātha'],['ثَلْج','thalj'],['ثَوْب','thawb'],['ثَمَر','thamar'],['ثَقِيل','thaqīl']]],
    ['/ð/ · ذ','Aproxime a ponta da língua dos dentes e mantenha a vibração de voz.',[['ذَهَب','dhahab'],['ذِرَاع','dhirāʿ'],['ذِئْب','dhiʾb'],['ذُبَاب','dhubāb'],['ذَنْب','dhanb']]],
    ['/sˤ/ · ص','Faça um s com a parte de trás da língua recuada. Observe como isso muda a vogal vizinha.',[['صَبَاح','ṣabāḥ'],['صَوْت','ṣawt'],['صُورَة','ṣūra'],['صَغِير','ṣaghīr'],['صَيْف','ṣayf']]],
    ['/ɣ/ · غ','Faça o ar passar com atrito na parte de trás da boca, mantendo a voz.',[['غُرْفَة','ghurfa'],['غُرَاب','ghurāb'],['غَابَة','ghāba'],['غَيْم','ghaym'],['غَد','ghad']]],
    ['/iː/ · ي longa','Sustente o i um pouco mais nestes exemplos, mantendo a língua alta e à frente.',[['كَبِير','kabīr'],['جَمِيل','jamīl'],['قَرِيب','qarīb'],['جَدِيد','jadīd'],['بَعِيد','baʿīd']]],
    ['/uː/ · و longa','Sustente o u na sílaba que contém و longa. Mantenha os lábios arredondados.',[['نُور','nūr'],['سُوق','sūq'],['فُول','fūl'],['حُوت','ḥūt'],['نُجُوم','nujūm']]]
  ],
  jpn:[
    ['きゃ · uma batida','Combine k e y antes de a num único impulso. O ゃ pequeno não ganha uma batida própria.',[['きゃく','kyaku'],['きゃべつ','kyabetsu'],['キャラ','kyara'],['キャンプ','kyanpu'],['キャップ','kyappu']]],
    ['じゅ · uma batida','Passe da consoante sonora diretamente a u na mesma batida.',[['じゅう','jū'],['じゅぎょう','jugyō'],['じゅんび','junbi'],['じゅんばん','junban'],['じゅうしょ','jūsho']]],
    ['つ · [tsɯ]','Solte t e s como um movimento só e passe a um u com pouco arredondamento.',[['つき','tsuki'],['つち','tsuchi'],['つくえ','tsukue'],['なつ','natsu'],['みつ','mitsu']]],
    ['ち · [tɕi]','Solte a consoante com um chiado curto e passe direto a i.',[['ちず','chizu'],['ちか','chika'],['ちから','chikara'],['くち','kuchi'],['まち','machi']]],
    ['う · [ɯ]','Eleve o dorso da língua e mantenha os lábios pouco arredondados, especialmente no início destes exemplos.',[['うみ','umi'],['うし','ushi'],['うえ','ue'],['うた','uta'],['うま','uma']]],
    ['にゃ, にゅ, にょ','Mantenha o som nasal e encaixe o y e a vogal na mesma batida do kana inicial.',[['にゃあ','nyā'],['にゅうがく','nyūgaku'],['にゅういん','nyūin'],['にょう','nyō'],['にょろにょろ','nyoronyoro']]]
  ],
  cmn:[
    ['ch · [ʈʂʰ]','Leve a ponta da língua um pouco para trás e solte a consoante com ar perceptível.',[['车','chē'],['吃','chī'],['茶','chá'],['春','chūn'],['船','chuán']]],
    ['sh · [ʂ]','Leve a ponta da língua para trás antes de soltar o chiado, sem bloquear o ar.',[['书','shū'],['上','shàng'],['手','shǒu'],['水','shuǐ'],['山','shān']]],
    ['z · [ts]','Una t e s numa consoante breve, com pouco sopro na soltura.',[['早','zǎo'],['字','zì'],['在','zài'],['坐','zuò'],['走','zǒu']]],
    ['c · [tsʰ]','Una t e s e solte com um sopro claro. Encoste a mão perto da boca para sentir o ar.',[['菜','cài'],['草','cǎo'],['词','cí'],['从','cóng'],['才','cái']]],
    ['ü · [y]','Faça a posição de i com a língua e arredonde os lábios. Depois de j ou q, esse som é escrito com u.',[['女','nǚ'],['绿','lǜ'],['鱼','yú'],['句','jù'],['去','qù']]],
    ['Final -ng','Deixe o ar sair pelo nariz com o dorso da língua levantado. Termine sem acrescentar g.',[['灯','dēng'],['冰','bīng'],['糖','táng'],['房','fáng'],['风','fēng']]]
  ],
  por:[
    ['-ou','Em boa parte do Brasil, o ditongo final -ou costuma soar próximo de um o simples.',['falou','andou','voltou','chegou','achou']],
    ['rr · r forte','Em muitas regiões, o rr produz atrito na parte de trás da boca, sem vibrar a ponta da língua.',['carro','terra','garrafa','correr','cachorro']],
    ['s entre vogais · /z/','Mantenha a vibração da voz ao fazer o s destas palavras.',['casa','mesa','rosa','vaso','visita']],
    ['qu · /k/','Nestas palavras, o u em qu fica mudo. Comece com o som de c de casa.',['queijo','quilo','quente','queda','quero']],
    ['e final átono','Em muitas regiões, o e final sem acento soa próximo de i nestas palavras.',['nome','tarde','noite','verde','doce']],
    ['o final átono','Em muitas regiões, o o final sem acento soa próximo de u nestas palavras.',['livro','gato','carro','copo','banco']]
  ]
};

const pronunciationPractice=[
  [
    ['Ouça {a}, pause e imite. Faça o mesmo com {b}.','Listen to {a}, pause and imitate it. Do the same with {b}.','Escucha {a}, haz una pausa e imita. Haz lo mismo con {b}.'],
    ['Comece por {a} no modo lento. Depois ouça e repita {b} em velocidade normal.','Start with {a} at slow speed. Then listen to and repeat {b} at normal speed.','Empieza con {a} en modo lento. Luego escucha y repite {b} a velocidad normal.'],
    ['Ouça as duas. Confirme em {b} o som que você percebeu em {a}.','Listen to both. Find the sound you heard in {a} again in {b}.','Escucha las dos. Busca en {b} el sonido que oíste en {a}.']
  ],
  [
    ['Alterne {a} e {b} em voz alta, com uma pequena pausa entre elas.','Alternate {a} and {b} aloud with a short pause between them.','Alterna {a} y {b} en voz alta, con una pequeña pausa.'],
    ['Ouça {a} duas vezes. Tente dizer {b} antes de tocar o áudio dela.','Hear {a} twice. Try saying {b} before playing its audio.','Escucha {a} dos veces. Intenta decir {b} antes de reproducir su audio.'],
    ['Articule {a} e {b} sem voz. Depois repita em voz alta e compare com o áudio.','Mouth {a} and {b}, then say them aloud and compare with the audio.','Articula {a} y {b} sin voz. Luego dilas en voz alta y compara con el audio.']
  ],
  [
    ['Repita {a} e {b} numa única expiração, preservando o som-alvo em cada palavra.','Repeat {a} and {b} in a single breath, keeping the target sound in both.','Repite {a} y {b} en una sola exhalación, conservando el sonido en ambas.'],
    ['Ouça {a} e {b}. Marque o ritmo natural de cada palavra com toques leves do dedo.','Listen to {a} and {b}. Tap out the natural rhythm of each word.','Escucha {a} y {b}. Marca el ritmo natural de cada palabra con el dedo.'],
    ['Diga {a}, depois {b}, primeiro devagar e depois numa conversa imaginária.','Say {a}, then {b}, first slowly and then as if you were in a conversation.','Di {a} y luego {b}, primero despacio y después como en una conversación.']
  ],
  [
    ['Insira {a} e {b} em duas frases curtas. Preserve o som-alvo em velocidade normal.','Use {a} and {b} in two short sentences. Keep the target sound at normal speed.','Usa {a} y {b} en dos frases cortas. Conserva el sonido a velocidad normal.'],
    ['Imagine que alguém ouviu mal {a}. Repita devagar e faça o mesmo com {b}.','Imagine someone misheard {a}. Repeat it slowly, then do the same with {b}.','Imagina que alguien oyó mal {a}. Repítela despacio y haz lo mismo con {b}.'],
    ['Ouça {a} e {b} uma vez. Espere cinco segundos e tente repetir de memória.','Listen once to {a} and {b}. Wait five seconds, then repeat from memory.','Escucha {a} y {b} una vez. Espera cinco segundos y repite de memoria.']
  ],
  [
    ['Diga uma frase com {a} e outra com {b}. Faça a primeira como pergunta e a segunda como resposta.','Say a sentence with {a} and one with {b}. Make the first a question and the second a reply.','Di una frase con {a} y otra con {b}. Haz la primera como pregunta y la segunda como respuesta.'],
    ['Compare {a} com {b}. Observe o que a língua e os lábios fazem no trecho que elas têm em comum.','Compare {a} with {b}. Notice what your tongue and lips do at the sound they share.','Compara {a} con {b}. Observa qué hacen la lengua y los labios en el sonido que comparten.'],
    ['Repita {a} e {b}, primeiro dirigindo-se a uma pessoa próxima, depois a alguém do outro lado da sala.','Say {a} and {b} first to someone nearby, then to someone across the room.','Di {a} y {b}, primero a alguien cercano y luego a alguien al otro lado de la sala.']
  ],
  [
    ['Invente um diálogo de duas falas com {a} e {b}. Preserve o som mesmo ao mudar a intenção.','Improvise a two-line dialogue with {a} and {b}. Keep the sound when you change your intention.','Improvisa dos intervenciones con {a} y {b}. Conserva el sonido aunque cambies de intención.'],
    ['Diga {a} e {b} em ritmo espontâneo. Identifique o que precisa ajustar ao ouvir os modelos de novo.','Say {a} and {b} at a natural pace. Listen again and identify what to adjust.','Di {a} y {b} con ritmo espontáneo. Escucha de nuevo e identifica qué debes ajustar.'],
    ['Diga uma frase com {a}, faça uma pausa natural e complete a ideia com outra frase que inclua {b}.','Say a sentence with {a}, pause naturally, then add a sentence using {b}.','Di una frase con {a}, haz una pausa natural y añade otra oración con {b}.']
  ]
];

const portuguesePronunciationSupport=[
  ['Place the middle of your tongue against your hard palate and let air flow through your nose.','Acerca el centro de la lengua al paladar y deja salir el aire por la nariz.'],
  ['Raise the middle of your tongue and let air escape around its sides.','Eleva el centro de la lengua y deja que el aire salga por los lados.'],
  ['Start with the nasal vowel and gradually close your lips into a glide.','Empieza con la vocal nasal y cierra los labios gradualmente en un deslizamiento.'],
  ['Tap the ridge behind your upper teeth with your tongue tip.','Da un toque rápido con la lengua detrás de los dientes superiores.'],
  ['Keep your voice vibrating while you make a continuous sh-like sound.','Mantén la vibración de la voz al hacer un sonido continuo parecido a sh.'],
  ['Let air make a continuous sh sound, with no vocal vibration.','Deja salir el aire con un sonido sh continuo, sin vibración de la voz.'],
  ['In much of Brazil, this final diphthong often sounds like a single o.','En gran parte de Brasil, este diptongo final suele sonar como una sola o.'],
  ['In many regions, rr comes from friction at the back of the mouth, without a tongue-tip trill.','En muchas regiones, rr se hace con fricción en la parte posterior de la boca, sin vibrar la punta de la lengua.'],
  ['Keep your voice vibrating on the s in these words.','Mantén la vibración de la voz al pronunciar la s de estas palabras.'],
  ['The u in qu is silent in these words. Start with a k sound.','La u de qu es muda en estas palabras. Empieza con un sonido k.'],
  ['In many regions, an unstressed final e sounds close to i in these words.','En muchas regiones, la e final átona suena cercana a i en estas palabras.'],
  ['In many regions, an unstressed final o sounds close to u in these words.','En muchas regiones, la o final átona suena cercana a u en estas palabras.']
];

function pronunciationTip(language,tier,index){
  const topics=[...pronunciationTopics[language],...pronunciationMoreTopics[language]];
  const position=index%topics.length;
  // Put the American flap on the early city lesson that teaches the word "city".
  const topic=language==='eng'&&position===11?5:language==='eng'&&position===5?11:position;
  const [sound,advice,examples]=topics[topic];
  // Twenty ordered pairs per topic. Each level supplies three different listening or speaking tasks.
  const slot=Math.floor(index/topics.length);
  const pairCount=examples.length*(examples.length-1);
  const pair=(slot*7)%pairCount;
  const first=Math.floor(pair/(examples.length-1));
  const offset=pair%(examples.length-1);
  const second=offset>=first?offset+1:offset;
  const words=[examples[first],examples[second]].map(example=>Array.isArray(example)?example:[example,'']);
  return {sound,advice,topic,words,task:pronunciationPractice[tier][slot%pronunciationPractice[tier].length]};
}

const portugueseSoundLabels={
  3:['Tapped r · [ɾ]','r simple · [ɾ]'],
  7:['rr · strong r','rr · r fuerte'],
  8:['s between vowels · /z/','s entre vocales · /z/'],
  10:['Unstressed final e','e final átona'],
  11:['Unstressed final o','o final átona']
};

function renderPronunciation(){
  const lab=a1PronunciationLabRow();
  if(lab)return renderA1Pronunciation(lab);
  const authored=plannedEnglishContent()?.pronunciation;
  const tip=authored?{sound:authored[0],advice:authored[1],topic:0,words:authored[2].map(word=>[word,'']),
    task:['Ouça {a} e {b}. Repita e tente perceber o detalhe descrito acima.']}:pronunciationTip(lang,level,unit);
  const {sound,advice,topic,words,task}=tip;
  const support=portuguesePronunciationSupport[topic];
  const guide=lang==='por'?routeLabel(advice,...support):advice;
  const soundSupport=lang==='por'&&portugueseSoundLabels[topic];
  const label=soundSupport?routeLabel(sound,...soundSupport):sound;
  const practice=routeLabel(...task).replace(/\{([ab])\}/g,(_,key)=>nativeText(words[key==='a'?0:1][0]));
  return '<section class="lesson-card pronunciation-card" id="pronunciationSection" aria-labelledby="pronunciationTitle" data-playback-block>'+
    lessonPhotoFrame(photoForMoment(lessonVisualTheme(),topic,'example'),'lesson-pronunciation-photo')+'<div><h3 id="pronunciationTitle">'+routeLabel('Dica de pronúncia','Pronunciation tip','Consejo de pronunciación')+'</h3>'+
    '<p class="pronunciation-sound" dir="auto">'+clean(label)+'</p><p>'+clean(guide)+'</p>'+
    '<ul class="pronunciation-words">'+words.map(([word,reading])=>'<li data-audio-line>'+nativeText(word)+(reading?'<span class="pinyin" lang="'+languages[lang][2].split('-')[0]+'-Latn">'+clean(reading)+'</span>':'')+
      lessonPlayButton(word,{compact:true,line:true})+'</li>').join('')+'</ul>'+
    sectionPlayButton('pronunciation',routeLabel('Ouvir as duas palavras','Play both words','Escuchar las dos palabras'))+
    '<p class="pronunciation-task">'+practice+'</p>'+
    lessonCoach(routeLabel('Repita sem ler','Repeat from memory','Repite sin leer'),
      routeLabel('Ouça as palavras, desvie os olhos do texto e repita. Depois compare com o áudio lento.','Listen to the words, look away, and repeat. Then compare with the slow audio.','Escucha las palabras, aparta la vista y repite. Luego compara con el audio lento.'))+'</div></section>';
}
