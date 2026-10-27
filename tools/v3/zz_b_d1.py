# Lote B (cinema), dados 1: episódios A1 7030033 .. 7010179. Formato: ver zz_b_lib.py.
from v3.zz_b_lib import add

add('''
N: 7030033
C: Mike,Sulley | tommy,tom | Presos no elevador, Mike e Sulley pedem ajuda com calma: Can you…? Call for help.
S: pedir ajuda com calma: Can you press the button? Call for help
Y: Hoje você aprende a pedir ajuda com calma: Can you press the button? Can you open the door? Call for help!
F: Monsters, Inc. | 🎬 Animação | 2001 | uma animação da Pixar, dirigida por Pete Docter, sobre dois monstros amigos que trabalham juntos numa grande fábrica | pedir ajuda com Can you…? e chamar ajuda | toyshop | 🚪,👾,🔔
V: 🛗|elevator|elevador|ÉL-e-vei-ter
V: 🔘|button|botão|BÂ-tn
V: 📞|phone|telefone|FÔUN
V: 🚪|door|porta|DÓR
V: 🆘|help|ajuda|RÉLP
V: 🔦|light|luz|LÁIT
H: Can you hear the elevator?|Você consegue ouvir o elevador?
H: Can you press the button?|Você consegue apertar o botão?
H: Call for help on the phone.|Peça ajuda pelo telefone.
H: Can you open the door?|Você consegue abrir a porta?
H: Please call for help!|Por favor, peça ajuda!
L: The elevator stopped, Sulley.|O elevador parou, Sulley.
L: Can you press the button, Mike?|Você consegue apertar o botão, Mike?
L: I press it. Nothing happens.|Eu aperto. Nada acontece.
L: Can you open the door?|Você consegue abrir a porta?
L: No, the door is stuck. The light is off.|Não, a porta está presa. A luz está apagada.
L: Call for help on the phone.|Peça ajuda pelo telefone.
L: Good idea. Can you hear me? Help, please!|Boa ideia. Você consegue me ouvir? Ajuda, por favor!
L: Stay calm. Somebody is coming.|Fique calmo. Alguém está vindo.
Q: What stopped?|O que parou?|0|🛗 The elevator|🚪 The door|🔦 The light
Q: What can Mike press?|O que o Mike aperta?|1|🔘 The button|📞 The phone|🆘 A sign
Q: How do they call for help?|Como eles pedem ajuda?|5|📞 On the phone|🚪 At the door|🔦 With a light
B: press|🔘|apertar|I press the button.|He presses the button.|She pressed it twice.|Ela apertou duas vezes.
B: call|📞|chamar, ligar|I call for help.|He calls for help.|They called the guard.|Eles chamaram o guarda.
B: shout|📣|gritar|I shout, “Help!”|He shouts, “Help!”|We shouted together.|Nós gritamos juntos.
B: wait|⏳|esperar|I wait here.|He waits here.|They waited a long time.|Eles esperaram muito tempo.
LAB: el|Laboratório de sons: elevator, button e help|Elevator tem a força no começo: ÉL-e-vei-ter. Button termina em som mudo, “bâ-tn”. Help começa com “r” suave.|Em button, o tt vira um toque rápido: BÂ-tn.
W: elevator|ÉL-e-vei-ter|elevador|força no começo|alligator|É-li-guei-ter
W: button|BÂ-tn|botão|tt rápido|butter|BÂ-der
W: help|RÉLP|ajuda|l final suave|held|RÉLD
G: 0|Can|Do|Are
G: 1|press|pressed|pressing
G: 2|for|to|of
G: 3|open|opens|opening
X: 😌|Stay calm|Fique calmo|acalmar|Stay calm and wait.|Fique calmo e espere.
X: 🙏|Hang on|Aguente firme|encorajar|Hang on, help is here.|Aguente firme, a ajuda chegou.
X: 😮|Oh no|Ai, não|reagir|Oh no, the light is off.|Ai, não, a luz apagou.
X: 👍|Good idea|Boa ideia|concordar|Good idea, call the guard.|Boa ideia, chame o guarda.

N: 30034
C: Moana,Maui | polly,tom | Na tempestade, Moana e Maui dizem o que há ao redor e o que precisam fazer: There is…, need to…
S: dizer o que há e o que precisa fazer: There is a storm. We need to hurry
Y: Hoje você aprende a falar do que há ao redor e do que precisa fazer: There is thunder. We need to hurry.
F: Moana | 🎬 Animação | 2016 | uma animação da Disney, dirigida por Ron Clements e John Musker, sobre uma jovem que atravessa o oceano num barco | falar do tempo no mar e do que é preciso fazer | ship | 🌊,⛵,🌩️
V: 🌩️|thunder|trovão|TÂN-der
V: 🌊|wave|onda|UÊIV
V: 💨|wind|vento|UÍND
V: ⛵|boat|barco|BÔUT
V: 🌧️|rain|chuva|RÊIN
V: 🪢|rope|corda|RÔUP
H: There is thunder in the sky.|Há trovão no céu.
H: There are big waves.|Há ondas grandes.
H: We need to hurry.|Precisamos nos apressar.
H: We need to turn the boat.|Precisamos virar o barco.
H: There is rain on the boat.|Há chuva no barco.
L: Maui, there is a storm.|Maui, há uma tempestade.
L: There is thunder in the sky.|Há trovão no céu.
L: There are big waves too.|Há ondas grandes também.
L: We need to hurry, Moana.|Precisamos nos apressar, Moana.
L: We need to turn the boat.|Precisamos virar o barco.
L: Hold the rope. There is a lot of wind.|Segure a corda. Há muito vento.
L: There is rain on the boat.|Há chuva no barco.
L: Stay low. The storm is almost over.|Fique abaixada. A tempestade está quase no fim.
Q: What is in the sky?|O que há no céu?|1|🌩️ Thunder|🌈 A rainbow|☀️ The sun
Q: What do they need to do?|O que eles precisam fazer?|3|🏃 Hurry|😴 Sleep|🍽️ Eat
Q: What does Moana hold?|O que a Moana segura?|5|🪢 The rope|🌩️ The thunder|🌧️ The rain
B: sail|⛵|navegar|I sail the boat.|He sails the boat.|They sailed all night.|Eles navegaram a noite toda.
B: hold|🤝|segurar|I hold the rope.|She holds the rope.|He held the boat.|Ele segurou o barco.
B: hurry|🏃|apressar-se|I hurry to the shore.|He hurries to the shore.|We hurried home.|Nós corremos para casa.
B: pull|💪|puxar|I pull the rope.|She pulls the rope.|He pulled the sail.|Ele puxou a vela.
LAB: th|Laboratório de sons: thunder, wave e wind|Thunder começa com th surdo: coloque a língua entre os dentes. Wave e wind começam com w, som de u.|Em thunder, o th é soprado: TÂN-der, com a língua entre os dentes.
W: thunder|TÂN-der|trovão|th surdo|under|ÂN-der
W: wave|UÊIV|onda|w = u|save|SÊIV
W: wind|UÍND|vento|w = u|wine|UÁIN
G: 0|is|are|am
G: 1|are|is|be
G: 2|need|needs|needing
G: 3|to|for|in
X: 😟|Look out|Cuidado|avisar|Look out, a big wave!|Cuidado, uma onda grande!
X: 💪|Let’s go|Vamos|animar|Let’s go, we can do it.|Vamos, nós conseguimos.
X: 😮|Hold on|Segure firme|pedir firmeza|Hold on, the wind is strong.|Segure firme, o vento está forte.
X: 😌|It’s okay|Está tudo bem|acalmar|It’s okay, we are safe.|Está tudo bem, estamos seguros.

N: 7010175
C: Carl,Russell | tom,tommy | Olhando o céu, Carl e Russell dizem o que as coisas do alto não fazem: doesn’t + verbo.
S: negar com doesn’t: The moon doesn’t sleep
Y: Hoje você aprende a negar com doesn’t + verbo: The moon doesn’t sleep. A star doesn’t move.
F: Up | 🎬 Animação | 2009 | uma animação da Pixar, dirigida por Pete Docter, sobre um senhor e um menino que viajam numa casa levada por balões | falar do céu e do que ele não faz | castle | 🎈,☁️,🌙
V: 🎈|balloon|balão|ba-LUM
V: ☁️|cloud|nuvem|KLÁUD
V: 🌙|moon|lua|MÚN
V: ⭐|star|estrela|STÁR
V: 🌈|rainbow|arco-íris|RÊIN-bou
V: 🌬️|breeze|brisa|BRÍZ
H: A balloon doesn’t fall.|Um balão não cai.
H: A cloud doesn’t stay still.|Uma nuvem não fica parada.
H: The moon doesn’t sleep.|A lua não dorme.
H: A star doesn’t move.|Uma estrela não se mexe.
H: A rainbow doesn’t last long.|Um arco-íris não dura muito.
L: Look at the sky, Russell.|Olhe para o céu, Russell.
L: The balloon doesn’t fall, Carl.|O balão não cai, Carl.
L: No, it doesn’t. It goes up.|Não, não cai. Ele sobe.
L: A cloud doesn’t stay still.|Uma nuvem não fica parada.
L: The moon doesn’t sleep.|A lua não dorme.
L: And a star doesn’t move.|E uma estrela não se mexe.
L: A rainbow doesn’t last long.|Um arco-íris não dura muito.
L: Let’s look at the stars tonight.|Vamos olhar as estrelas hoje à noite.
Q: What doesn’t fall?|O que não cai?|1|🎈 The balloon|🌙 The moon|⭐ A star
Q: What doesn’t stay still?|O que não fica parado?|3|☁️ A cloud|⭐ A star|🌈 A rainbow
Q: What doesn’t move?|O que não se mexe?|5|⭐ A star|☁️ A cloud|🎈 The balloon
B: float|🎈|flutuar|I float in the air.|It floats in the air.|The house floated away.|A casa flutuou para longe.
B: point|👉|apontar|I point at the sky.|He points at the sky.|She pointed at the moon.|Ela apontou para a lua.
B: watch|👀|observar|I watch the clouds.|He watches the clouds.|We watched the stars.|Nós observamos as estrelas.
B: wave|👋|acenar|I wave at the balloon.|He waves at the balloon.|They waved goodbye.|Eles acenaram em despedida.
LAB: ou|Laboratório de sons: cloud, moon e star|Cloud tem o ditongo ou, “káud”. Moon tem o u longo, “mún”. Star abre bem a boca: “stár”.|Em moon, alongue o u: MÚÚN. Em cloud, a boca vai de á para u.
W: cloud|KLÁUD|nuvem|ou = áu|loud|LÁUD
W: moon|MÚN|lua|u longo|moan|MÔUN
W: star|STÁR|estrela|a aberto|stir|STÂR
G: 0|doesn’t|don’t|isn’t
G: 1|stay|stays|staying
G: 2|sleep|sleeps|sleeping
G: 3|move|moves|moving
X: 😮|Look up|Olhe para cima|chamar atenção|Look up, a big cloud!|Olhe para cima, uma nuvem grande!
X: 😍|How pretty|Que lindo|admirar|How pretty, a rainbow!|Que lindo, um arco-íris!
X: 🤩|Wow|Uau|se surpreender|Wow, so many stars.|Uau, tantas estrelas.
X: 🌙|Good night|Boa noite|despedir-se|Good night, moon.|Boa noite, lua.

N: 7070070
C: Satsuki,Mei | polly,misshoney | No jardim de casa, Satsuki e Mei dizem onde ficam as coisas: between, in front of, opposite.
S: situar no espaço com between, in front of e opposite: The tree is between the houses
Y: Hoje você aprende a situar as coisas: The tree is between the houses. The bench is in front of the tree. The stop is opposite the tree.
F: My Neighbor Totoro | 🎬 Animação | 1988 | uma animação do estúdio japonês Ghibli, dirigida por Hayao Miyazaki, sobre duas irmãs que vão morar no campo e fazem amizade com um espírito da floresta | dizer onde ficam as coisas | jungle | 🌳,☂️,🏡
V: 🌳|tree|árvore|TRÍ
V: 🚏|bus stop|ponto de ônibus|BÂS-stóp
V: ☂️|umbrella|guarda-chuva|am-BRÉ-la
V: 🏡|house|casa|RÁUS
V: 🌰|acorn|bolota|ÊI-kórn
V: 🪑|bench|banco|BÉNTCH
H: The tree is between the two houses.|A árvore fica entre as duas casas.
H: The bus stop is opposite the tree.|O ponto de ônibus fica em frente à árvore, do outro lado.
H: My umbrella is in front of the bench.|Meu guarda-chuva está na frente do banco.
H: Our house is between the tree and the hill.|Nossa casa fica entre a árvore e o morro.
H: The acorn is in front of the door.|A bolota está na frente da porta.
L: Mei, where is the bus stop?|Mei, onde fica o ponto de ônibus?
L: It is opposite the big tree.|Fica em frente à árvore grande, do outro lado.
L: And where is my umbrella?|E onde está o meu guarda-chuva?
L: It is in front of the bench.|Está na frente do banco.
L: Look! The tree is between the two houses.|Olhe! A árvore fica entre as duas casas.
L: Our house is between the tree and the hill.|Nossa casa fica entre a árvore e o morro.
L: The acorn is in front of the door.|A bolota está na frente da porta.
L: Let’s sit on the bench and wait.|Vamos sentar no banco e esperar.
Q: Where is the bus stop?|Onde fica o ponto de ônibus?|1|🌳 Opposite the tree|🏡 In the house|🪑 On the bench
Q: Where is the umbrella?|Onde está o guarda-chuva?|3|🪑 In front of the bench|🌳 Between the trees|🏡 Inside the house
Q: What is in front of the door?|O que está na frente da porta?|6|🌰 The acorn|☂️ The umbrella|🚏 The bus stop
B: sit|🪑|sentar|I sit on the bench.|She sits on the bench.|They sat together.|Eles sentaram juntos.
B: wait|⏳|esperar|I wait at the stop.|She waits at the stop.|We waited for the bus.|Nós esperamos o ônibus.
B: look|👀|olhar|I look at the tree.|She looks at the tree.|He looked at the hill.|Ele olhou para o morro.
B: stand|🧍|ficar de pé|I stand under the tree.|She stands under the tree.|They stood in the rain.|Eles ficaram de pé na chuva.
LAB: br|Laboratório de sons: umbrella, bench e acorn|Umbrella tem a força em -BRÉ-: am-BRÉ-la. Bench termina em tch. Acorn começa com ÊI.|Em bench, termine com um tch suave: BÉNTCH.
W: umbrella|am-BRÉ-la|guarda-chuva|força no meio|umpire|ÂM-páir
W: bench|BÉNTCH|banco|ch final|bunch|BÂNTCH
W: acorn|ÊI-kórn|bolota|a = êi|corn|KÓRN
G: 0|between|in|on
G: 1|opposite|in|at
G: 2|in front of|behind|beside
G: 3|between|on|at
X: 😮|Over there|Ali adiante|apontar|Over there, the red bus stop.|Ali adiante, o ponto de ônibus vermelho.
X: 🙋|Right here|Bem aqui|indicar|Right here, on the bench.|Bem aqui, no banco.
X: 👀|Look at that|Olhe aquilo|chamar atenção|Look at that, a huge tree!|Olhe aquilo, uma árvore enorme!
X: 😊|That’s funny|Que engraçado|reagir|That’s funny, my umbrella is small.|Que engraçado, meu guarda-chuva é pequeno.

N: 7910017
C: Julie,Julia | tom,polly | Na cozinha, Julie e Julia cozinham passo a passo: after that, later, at last.
S: encadear ações com after that, later e at last: Melt the butter. After that, add the onions
Y: Hoje você aprende a ligar passos de uma receita: After that, Later, At last. Melt the butter. After that, add onions.
F: Julie and Julia | 🎬 Filme | 2009 | um filme escrito e dirigido por Nora Ephron, sobre duas mulheres que aprendem a cozinhar por receitas, em épocas diferentes | contar os passos de uma receita | bakery | 🧈,🍳,🥘
V: 🧈|butter|manteiga|BÂ-der
V: 🥚|egg|ovo|ÉG
V: 🍳|pan|frigideira|PÉN
V: 🔪|knife|faca|NÁIF
V: 🧂|salt|sal|SÓLT
V: 🥘|stew|ensopado|STIÚ
H: Melt the butter. After that, add onions.|Derreta a manteiga. Depois disso, ponha cebolas.
H: Break the egg. Later, add milk.|Quebre o ovo. Mais tarde, ponha leite.
H: Cook for ten minutes. At last, it is ready.|Cozinhe por dez minutos. Por fim, está pronto.
H: Cut the onion. After that, stir the pan.|Corte a cebola. Depois disso, mexa a frigideira.
H: Add salt. Later, taste the stew.|Ponha sal. Mais tarde, prove o ensopado.
L: Julia, how do I start the stew?|Julia, como eu começo o ensopado?
L: Melt the butter. After that, add onions.|Derreta a manteiga. Depois disso, ponha cebolas.
L: I cut the onion with the knife.|Eu corto a cebola com a faca.
L: Good. After that, stir the pan.|Bom. Depois disso, mexa a frigideira.
L: Should I add an egg?|Devo pôr um ovo?
L: Yes. Break the egg. Later, add milk.|Sim. Quebre o ovo. Mais tarde, ponha leite.
L: Cook for ten minutes. At last, it is ready.|Cozinhe por dez minutos. Por fim, está pronto.
L: Add salt. Later, taste the stew.|Ponha sal. Mais tarde, prove o ensopado.
Q: What does Julie melt first?|O que a Julie derrete primeiro?|1|🧈 The butter|🥚 The egg|🧂 The salt
Q: What does Julie cut?|O que a Julie corta?|2|🧅 The onion|🥚 The egg|🧈 The butter
Q: When is the stew ready?|Quando o ensopado fica pronto?|6|🍳 At last, after ten minutes|🥚 Before the egg|🔪 After the knife
B: melt|🧈|derreter|I melt the butter.|She melts the butter.|He melted the cheese.|Ele derreteu o queijo.
B: stir|🥄|mexer|I stir the pan.|She stirs the pan.|We stirred the stew.|Nós mexemos o ensopado.
B: cut|🔪|cortar|I cut the onion.|She cuts the onion.|He cut the bread.|Ele cortou o pão.
B: serve|🍽️|servir|I serve the stew.|She serves the stew.|They served dinner.|Eles serviram o jantar.
LAB: bu|Laboratório de sons: butter, egg e stew|Butter tem tt rápido, “bâ-der”. Egg tem e aberto, “ég”. Stew soa como “stiú”.|Em butter, o tt vira um d suave: BÂ-der.
W: butter|BÂ-der|manteiga|tt = d suave|better|BÉ-der
W: egg|ÉG|ovo|e aberto|ink|ÍNK
W: stew|STIÚ|ensopado|ew = iú|stay|STÊI
G: 0|After that|Before|Always
G: 1|Later|Early|Late
G: 2|At last|At night|At first
G: 4|Later|Early|Never
X: 😋|Yummy|Que delícia|elogiar|Yummy, the stew is great.|Que delícia, o ensopado está ótimo.
X: 😅|Oops|Ops|se desculpar|Oops, I dropped the egg.|Ops, derrubei o ovo.
X: 👩‍🍳|Be careful|Tenha cuidado|avisar|Be careful, the pan is hot.|Tenha cuidado, a frigideira está quente.
X: 👏|Well done|Muito bem|elogiar|Well done, Julie.|Muito bem, Julie.

N: 7010176
C: Bambi,Thumper | tommy,rabbit | No bosque, Bambi e Thumper contam como são os meses de janeiro a junho, sempre com letra maiúscula.
S: meses de janeiro a junho com maiúscula: January is cold, March is windy
Y: Hoje você aprende os meses de janeiro a junho: January, February, March, April, May, June. Em inglês, mês começa com letra maiúscula.
F: Bambi | 🎬 Animação | 1942 | uma animação clássica da Disney sobre um filhote de cervo que cresce na floresta, com a amizade de um coelho e o passar das estações | falar dos meses e do tempo | jungle | 🦌,🌸,❄️
V: ❄️|snow|neve|SNÔU
V: 🌬️|breeze|brisa|BRÍZ
V: 🌧️|rain|chuva|RÊIN
V: 🌷|tulip|tulipa|TIÚ-lip
V: 🐇|bunny|coelhinho|BÂ-ni
V: 🦌|deer|cervo|DÍR
H: January is cold and white.|Janeiro é frio e branco.
H: March is windy, but flowers grow.|Março tem vento, mas as flores crescem.
H: April has a lot of rain.|Abril tem muita chuva.
H: May is warm, and tulips bloom.|Maio é quente, e as tulipas florescem.
H: June is hot, and bunnies play.|Junho é quente, e os coelhinhos brincam.
L: Look, Thumper! January is cold and white.|Olhe, Thumper! Janeiro é frio e branco.
L: February is short, Bambi.|Fevereiro é curto, Bambi.
L: March is windy, but flowers grow.|Março tem vento, mas as flores crescem.
L: April has a lot of rain.|Abril tem muita chuva.
L: May is warm, and tulips bloom.|Maio é quente, e as tulipas florescem.
L: June is hot, and bunnies play.|Junho é quente, e os coelhinhos brincam.
L: I love June. The days are long.|Eu amo junho. Os dias são longos.
L: Me too! Let’s play in the sun.|Eu também! Vamos brincar no sol.
Q: What is January like?|Como é janeiro?|0|❄️ Cold and white|☀️ Hot|🌧️ Rainy
Q: What does April have?|O que abril tem?|3|🌧️ A lot of rain|❄️ Snow|🌷 Tulips
Q: Which month is hot?|Qual mês é quente?|5|☀️ June|❄️ January|🌬️ March
B: hop|🐇|pular|I hop in the grass.|He hops in the grass.|The bunny hopped away.|O coelhinho saiu pulando.
B: melt|💧|derreter|The snow melts.|The snow melts.|The ice melted in May.|O gelo derreteu em maio.
B: sniff|👃|cheirar|I sniff the flowers.|He sniffs the flowers.|She sniffed the tulips.|Ela cheirou as tulipas.
B: slide|🛝|escorregar|I slide on the snow.|He slides on the snow.|We slid down the hill.|Nós escorregamos o morro.
LAB: mo|Laboratório de sons: January, tulip e deer|January tem a força no começo, “JÉ-niu-é-ri”. Tulip soa “TIÚ-lip”. Deer termina com r suave.|Nos meses, a primeira letra é sempre maiúscula: January, March, June.
W: January|JÉ-niu-é-ri|janeiro|força no começo|Janet|JÉ-nit
W: tulip|TIÚ-lip|tulipa|tu = tiú|tulle|TIÚL
W: deer|DÍR|cervo|ee = í|dear|DÍR
G: 0|January|january|Jenuary
G: 1|March|march|Marsh
G: 2|April|april|Abril
G: 4|June|june|Jun
X: 😊|Look at that|Olhe aquilo|chamar atenção|Look at that, a tiny bunny!|Olhe aquilo, um coelhinho!
X: 😍|So pretty|Tão lindo|admirar|So pretty, the tulips in May.|Tão lindas, as tulipas em maio.
X: 🏃|Come on|Vamos lá|animar|Come on, let’s play.|Vamos lá, vamos brincar.
X: 🥶|It’s cold|Está frio|dizer o tempo|It’s cold, but I like snow.|Está frio, mas eu gosto de neve.

N: 7070071
C: Gil,Adriana | polly,tommy | Numa Paris de épocas misturadas, Gil e Adriana dizem em que ano as coisas aconteceram: in + ano.
S: dizer o ano com in + ano: He lived in Paris in 1925
Y: Hoje você aprende a dizer o ano com in: I was born in 1995. We moved here in 2010. He lived in Paris in 1925.
F: Midnight in Paris | 🎬 Filme | 2011 | um filme escrito e dirigido por Woody Allen, sobre um escritor que viaja no tempo à meia-noite pelas ruas de Paris | dizer em que ano algo aconteceu | library | 🗼,🕛,🚕
V: 🎨|painter|pintor|PÊIN-ter
V: ✍️|writer|escritor|RÁI-ter
V: 🚕|taxi|táxi|TÉK-si
V: 🕛|midnight|meia-noite|MÍD-nait
V: 🗼|tower|torre|TÁU-er
V: 📅|year|ano|IÍR
H: He lived in Paris in 1925.|Ele morou em Paris em 1925.
H: I was born in 1995.|Eu nasci em 1995.
H: We took a taxi in 2011.|Nós pegamos um táxi em 2011.
H: It happened in 1920.|Aconteceu em 1920.
H: The tower opened in 1889.|A torre abriu em 1889.
L: Adriana, which year is it?|Adriana, que ano é?
L: It is 1925, Gil. He lived in Paris in 1925.|É 1925, Gil. Ele morou em Paris em 1925.
L: I am a writer. I was born in 1995.|Sou escritor. Eu nasci em 1995.
L: Really? We took a taxi in 2011.|Sério? Nós pegamos um táxi em 2011.
L: It is midnight. Where are we?|É meia-noite. Onde estamos?
L: It happened in 1920, I think.|Aconteceu em 1920, eu acho.
L: Look at the tower. It opened in 1889.|Olhe a torre. Ela abriu em 1889.
L: Paris is beautiful in every year.|Paris é linda em todos os anos.
Q: When did the painter live in Paris?|Quando o pintor morou em Paris?|1|📅 In 1925|📅 In 1995|📅 In 2011
Q: When was Gil born?|Quando o Gil nasceu?|2|📅 In 1995|📅 In 1889|📅 In 1920
Q: When did the tower open?|Quando a torre abriu?|6|🗼 In 1889|🗼 In 1925|🗼 In 2011
B: draw|✏️|desenhar|I draw a tower.|He draws a tower.|She drew a taxi.|Ela desenhou um táxi.
B: dream|💭|sonhar|I dream of Paris.|He dreams of Paris.|We dreamed all night.|Nós sonhamos a noite toda.
B: walk|🚶|andar|I walk by the river.|He walks by the river.|They walked home.|Eles andaram para casa.
B: travel|🧳|viajar|I travel by train.|She travels by train.|He traveled in 2011.|Ele viajou em 2011.
LAB: mi|Laboratório de sons: midnight, tower e year|Midnight tem a força no começo, “MÍD-nait”. Tower soa “TÁU-er”. Year começa com um i curto, “iír”.|Em year, comece com um i curto: IÍR.
W: midnight|MÍD-nait|meia-noite|força no começo|mid-air|MÍD-éar
W: tower|TÁU-er|torre|ow = áu|tire|TÁI-er
W: year|IÍR|ano|y = i curto|ear|ÍR
G: 0|in|on|at
G: 1|in|at|of
G: 2|in|on|to
G: 4|in|at|by
X: 😮|No way|Não pode ser|se surpreender|No way, it is 1925!|Não pode ser, é 1925!
X: 🤔|Let me see|Deixe-me ver|pensar|Let me see, it is 2011.|Deixe-me ver, é 2011.
X: 😍|I love it|Eu amo|elogiar|I love it, Paris is great.|Eu amo, Paris é ótima.
X: 🕛|It’s late|Está tarde|dizer a hora|It’s late, it is midnight.|Está tarde, é meia-noite.

N: 7030036
C: Harry,Sally | tom,polly | Num café de Nova York, Harry e Sally falam de datas: in + mês e in + estação.
S: dizer o mês e a estação com in: The fair is in autumn. It is in October
Y: Hoje você aprende a dizer quando algo acontece: The fair is in autumn. It is in October. We meet in November.
F: When Harry Met Sally | 🎬 Filme | 1989 | uma comédia romântica dirigida por Rob Reiner, sobre um homem e uma mulher que se encontram várias vezes ao longo dos anos em Nova York | dizer em que mês e estação algo acontece | rainycafe | 🍂,☕,🍁
V: 🍂|autumn|outono|Ó-tam
V: 📅|October|outubro|ok-TÔU-ber
V: 🍁|leaf|folha|LÍF
V: 🎡|fair|feira|FÉR
V: ☕|coffee|café|KÓ-fi
V: 🧣|scarf|cachecol|SKÁRF
H: The fair is in autumn.|A feira é no outono.
H: It is in October.|É em outubro.
H: The leaves fall in September.|As folhas caem em setembro.
H: We meet in November.|Nós nos encontramos em novembro.
H: We have coffee in autumn.|Nós tomamos café no outono.
L: Sally, when is the fair?|Sally, quando é a feira?
L: The fair is in autumn.|A feira é no outono.
L: Which month? It is in October.|Que mês? É em outubro.
L: The leaves fall in September.|As folhas caem em setembro.
L: And I wear a scarf in winter.|E eu uso cachecol no inverno.
L: Let’s meet again. We meet in November.|Vamos nos ver de novo. Nós nos encontramos em novembro.
L: Great. We have coffee in autumn.|Ótimo. Nós tomamos café no outono.
L: See you at the fair, Harry.|Até a feira, Harry.
Q: When is the fair?|Quando é a feira?|1|🍂 In autumn|🌸 In spring|❄️ In winter
Q: Which month is the fair?|Em que mês é a feira?|2|📅 In October|📅 In January|📅 In June
Q: What do they have in autumn?|O que eles tomam no outono?|6|☕ Coffee|🧣 A scarf|🍁 A leaf
B: meet|🤝|encontrar|I meet Sally.|He meets Sally.|They met in 1989.|Eles se encontraram em 1989.
B: walk|🚶|andar|I walk in the park.|She walks in the park.|We walked in autumn.|Nós andamos no outono.
B: order|🧾|pedir|I order a coffee.|He orders a coffee.|She ordered a pie.|Ela pediu uma torta.
B: talk|💬|conversar|I talk to Harry.|She talks to Harry.|We talked for hours.|Nós conversamos por horas.
LAB: au|Laboratório de sons: autumn, October e scarf|Autumn tem o m final mudo, “Ó-tam”. October tem a força em -TÔU-. Scarf abre bem o a: “SKÁRF”.|Em autumn, o n final é mudo: Ó-tam.
W: autumn|Ó-tam|outono|n final mudo|atom|É-tam
W: October|ok-TÔU-ber|outubro|força no meio|over|ÔU-ver
W: scarf|SKÁRF|cachecol|a aberto|scar|SKÁR
G: 0|in|on|at
G: 1|in|at|of
G: 2|in|on|to
G: 4|in|at|by
X: 🍂|Nice weather|Tempo bom|comentar|Nice weather in autumn.|Tempo bom no outono.
X: 😊|See you soon|Até logo|despedir-se|See you soon, Sally.|Até logo, Sally.
X: 🤗|Me too|Eu também|concordar|Me too, I love autumn.|Eu também, eu amo o outono.
X: 📅|Mark the date|Marque a data|lembrar|Mark the date, it is October.|Marque a data, é outubro.

N: 7910018
C: Beca,Chloe | polly,misshoney | Ensaiando no palco, Beca e Chloe concordam com Me too e Me neither.
S: concordar com Me too e Me neither: I like singing. Me too
Y: Hoje você aprende a concordar: depois de uma frase positiva use Me too; depois de uma negativa use Me neither.
F: Pitch Perfect | 🎬 Filme | 2012 | uma comédia musical dirigida por Jason Moore, sobre um grupo de jovens que canta sem instrumentos num coral de universidade | concordar com Me too e Me neither | toyshop | 🎤,🎵,🎶
V: 🎤|microphone|microfone|MÁI-kro-fôun
V: 🎵|song|música|SÓNG
V: 🎧|headphones|fones de ouvido|RÉD-fônz
V: 🥁|drum|bateria|DRÂM
V: 🎹|piano|piano|pi-Á-nô
V: 🎶|choir|coral|KUÁI-er
H: I like singing. — Me too.|Eu gosto de cantar. — Eu também.
H: I don’t like loud music. — Me neither.|Eu não gosto de música alta. — Eu também não.
H: I love this song. — Me too.|Eu amo esta música. — Eu também.
H: I can’t sing high. — Me neither.|Eu não consigo cantar agudo. — Eu também não.
H: I want to win. — Me too.|Eu quero ganhar. — Eu também.
L: I like singing, Chloe.|Eu gosto de cantar, Chloe.
L: Me too! I love this song.|Eu também! Eu amo esta música.
L: Me too. I want to win.|Eu também. Eu quero ganhar.
L: I don’t like loud music.|Eu não gosto de música alta.
L: Me neither. It hurts my ears.|Eu também não. Machuca meus ouvidos.
L: I can’t sing high.|Eu não consigo cantar agudo.
L: Me neither. Let’s practice with the piano.|Eu também não. Vamos praticar com o piano.
L: Good idea. Me too!|Boa ideia. Eu também!
Q: What do they both like?|De que as duas gostam?|0|🎤 Singing|🥁 Loud drums|🎧 Silence
Q: Who does not like loud music?|Quem não gosta de música alta?|3|🎶 Both of them|🎤 Only Beca|🥁 Nobody
Q: What do they practice with?|Com o que elas praticam?|6|🎹 The piano|🥁 The drum|🎤 A microphone
B: agree|🤝|concordar|I agree with you.|She agrees with you.|They agreed on a song.|Elas concordaram numa música.
B: sing|🎤|cantar|I sing every day.|She sings every day.|We sang together.|Nós cantamos juntas.
B: clap|👏|bater palmas|I clap my hands.|She claps her hands.|They clapped loudly.|Elas bateram palmas alto.
B: practice|🎹|praticar|I practice the song.|She practices the song.|We practiced at night.|Nós praticamos à noite.
LAB: mi|Laboratório de sons: microphone, headphones e choir|Microphone tem a força no começo, “MÁI-kro-fôun”. Headphones soa “RÉD-fônz”. Choir soa “KUÁI-er”.|Em choir, o ch soa como k: KUÁI-er.
W: microphone|MÁI-kro-fôun|microfone|força no começo|microwave|MÁI-kro-uêiv
W: headphones|RÉD-fônz|fones|h soprado|head|RÉD
W: choir|KUÁI-er|coral|ch = k|quiet|KUÁI-et
G: 0|Me too|Me neither|Me not
G: 1|Me neither|Me too|Me no
G: 3|Me neither|Me too|Me not
G: 4|Me too|Me neither|Me yes
X: 😄|Same here|Igualmente|concordar|Same here, I love music.|Igualmente, eu amo música.
X: 👏|Nice job|Bom trabalho|elogiar|Nice job, Beca.|Bom trabalho, Beca.
X: 🙌|Let’s go|Vamos|animar|Let’s go, we can win.|Vamos, nós podemos ganhar.
X: 😬|Not bad|Nada mal|opinar|Not bad, but try again.|Nada mal, mas tente de novo.

N: 7010178
C: George,Mary | tom,polly | No banco da cidade, George e Mary falam de dinheiro: earn, save e spend.
S: falar de dinheiro com earn, save e spend: I earn money. I save ten dollars
Y: Hoje você aprende a falar de dinheiro: earn é ganhar, save é guardar e spend é gastar. I earn money. I save ten dollars.
F: It’s a Wonderful Life | 🎬 Filme | 1946 | um clássico dirigido por Frank Capra, sobre um homem que ajuda os vizinhos de uma cidade pequena a guardar dinheiro e comprar casas | falar de dinheiro | castle | 🏦,💵,🏠
V: 🏦|bank|banco|BÉNK
V: 💵|dollar|dólar|DÓ-ler
V: 🐷|piggy bank|cofrinho|PÍ-gui-bénk
V: 🏠|house|casa|RÁUS
V: 💼|job|emprego|DJÓB
V: 🪙|coin|moeda|KÓIN
H: I work at the bank. I earn money.|Eu trabalho no banco. Eu ganho dinheiro.
H: I save ten dollars a week.|Eu guardo dez dólares por semana.
H: I spend twenty dollars on food.|Eu gasto vinte dólares em comida.
H: We save money for a house.|Nós guardamos dinheiro para uma casa.
H: I like my job.|Eu gosto do meu emprego.
L: George, what do you do at the bank?|George, o que você faz no banco?
L: I work at the bank. I earn money.|Eu trabalho no banco. Eu ganho dinheiro.
L: Do you save money, Mary?|Você guarda dinheiro, Mary?
L: Yes, I save ten dollars a week.|Sim, eu guardo dez dólares por semana.
L: And I spend twenty dollars on food.|E eu gasto vinte dólares em comida.
L: We save money for a house.|Nós guardamos dinheiro para uma casa.
L: Put every coin in the piggy bank.|Ponha cada moeda no cofrinho.
L: I like my job. It is a good life.|Eu gosto do meu emprego. É uma boa vida.
Q: Where does George work?|Onde o George trabalha?|1|🏦 At the bank|🏠 At a house|💼 At home
Q: How much does Mary save a week?|Quanto a Mary guarda por semana?|3|💵 Ten dollars|💵 Twenty dollars|💵 One dollar
Q: What do they save money for?|Para que eles guardam dinheiro?|5|🏠 A house|🍽️ Food|💼 A job
B: lend|🤲|emprestar|I lend a dollar.|He lends a dollar.|She lent me ten dollars.|Ela me emprestou dez dólares.
B: work|💼|trabalhar|I work at the bank.|He works at the bank.|They worked all day.|Eles trabalharam o dia todo.
B: give|🎁|dar|I give a coin.|He gives a coin.|She gave me a dollar.|Ela me deu um dólar.
B: buy|🛒|comprar|I buy bread.|He buys bread.|We bought a house.|Nós compramos uma casa.
LAB: da|Laboratório de sons: dollar, bank e coin|Dollar tem a força no começo, “DÓ-ler”. Bank termina em nk, “BÉNK”. Coin tem o ditongo oi, “KÓIN”.|Em dollar, o ar final vira um er curto: DÓ-ler.
W: dollar|DÓ-ler|dólar|força no começo|dolly|DÓ-li
W: bank|BÉNK|banco|nk final|bake|BÊIK
W: coin|KÓIN|moeda|oi = ói|corn|KÓRN
G: 0|earn|earns|earning
G: 1|save|saves|saving
G: 2|spend|spends|spending
G: 3|for|to|of
X: 💰|Not bad|Nada mau|opinar|Not bad, fifty dollars a day.|Nada mau, cinquenta dólares por dia.
X: 😊|Good job|Bom trabalho|elogiar|Good job, you save a lot.|Bom trabalho, você guarda muito.
X: 🤔|Let’s see|Vamos ver|calcular|Let’s see, ten and ten is twenty.|Vamos ver, dez e dez são vinte.
X: 😄|Thanks a lot|Muito obrigado|agradecer|Thanks a lot, George.|Muito obrigado, George.

N: 7010179
C: Wonka,Charlie | willywonka,tommy | Na fábrica de doces, Wonka e Charlie dividem as porções: a slice of, a piece of.
S: porções de comida: a slice of cake, a piece of chocolate
Y: Hoje você aprende a falar de porções: a slice of cake (fatia), a piece of chocolate (pedaço).
F: Willy Wonka and the Chocolate Factory | 🎬 Filme | 1971 | um filme musical dirigido por Mel Stuart, sobre um menino que visita uma fábrica de chocolate cheia de surpresas | pedir porções de comida | bakery | 🍫,🍰,🍬
V: 🍰|cake|bolo|KÊIK
V: 🥧|pie|torta|PÁI
V: 🍫|chocolate|chocolate|TCHÓK-lit
V: 🍬|candy|bala|KÉN-di
V: 🍞|toast|torrada|TÔUST
V: 🔪|knife|faca|NÁIF
H: A slice of cake, please.|Uma fatia de bolo, por favor.
H: A slice of pie is warm.|Uma fatia de torta está quente.
H: A piece of chocolate is sweet.|Um pedaço de chocolate é doce.
H: A piece of candy for you.|Um pedaço de bala para você.
H: A slice of toast with jam.|Uma fatia de torrada com geleia.
L: Mister Wonka, a slice of cake, please.|Senhor Wonka, uma fatia de bolo, por favor.
L: Here you are, Charlie. Use the knife.|Aqui está, Charlie. Use a faca.
L: A slice of pie is warm. Do you want it?|Uma fatia de torta está quente. Você quer?
L: Yes, please. And a piece of chocolate.|Sim, por favor. E um pedaço de chocolate.
L: A piece of chocolate is sweet.|Um pedaço de chocolate é doce.
L: A piece of candy for you, too.|Um pedaço de bala para você também.
L: A slice of toast with jam for Grandpa.|Uma fatia de torrada com geleia para o vovô.
L: Thank you, Mister Wonka. It is delicious!|Obrigado, senhor Wonka. Está delicioso!
Q: What does Charlie ask for first?|O que o Charlie pede primeiro?|0|🍰 A slice of cake|🍫 A piece of candy|🥧 A slice of pie
Q: What is sweet?|O que é doce?|4|🍫 A piece of chocolate|🍞 A slice of toast|🔪 The knife
Q: What is for Grandpa?|O que é para o vovô?|6|🍞 A slice of toast|🍰 A slice of cake|🍬 A piece of candy
B: cut|🔪|cortar|I cut the cake.|He cuts the cake.|She cut the pie.|Ela cortou a torta.
B: break|🍫|quebrar|I break the chocolate.|He breaks the chocolate.|They broke a candy.|Eles quebraram uma bala.
B: pass|🤲|passar|I pass the plate.|He passes the plate.|She passed the knife.|Ela passou a faca.
B: smell|👃|cheirar|I smell the pie.|He smells the pie.|We smelled the bread.|Nós sentimos o cheiro do pão.
LAB: ch|Laboratório de sons: chocolate, candy e knife|Chocolate tem três sílabas ditas como duas: “TCHÓK-lit”. Candy soa “KÉN-di”. Em knife, o k é mudo: “NÁIF”.|Em knife, o k não se fala: NÁIF.
W: chocolate|TCHÓK-lit|chocolate|duas sílabas|chalk|TCHÓK
W: candy|KÉN-di|bala|a = é|handy|RÉN-di
W: knife|NÁIF|faca|k mudo|night|NÁIT
G: 0|slice|glass|cup
G: 1|slice|bottle|cup
G: 2|piece|glass|cup
G: 3|piece|bottle|box
X: 😋|Yummy|Que delícia|elogiar|Yummy, this cake is great.|Que delícia, este bolo é ótimo.
X: 🙏|Here you are|Aqui está|oferecer|Here you are, a slice of pie.|Aqui está, uma fatia de torta.
X: 🎉|Help yourself|Sirva-se|oferecer|Help yourself to the candy.|Sirva-se da bala.
X: 😊|My pleasure|Com prazer|responder|My pleasure, Charlie.|Com prazer, Charlie.
''')
