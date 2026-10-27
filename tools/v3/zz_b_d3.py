# Lote B (cinema), dados 3: episódios A1 7030044 .. 7080185. Formato: ver zz_b_lib.py.
from v3.zz_b_lib import add

add('''
N: 7030044
C: Eddie,Boogie | tom,polly | Na lanchonete, Eddie e Boogie escolhem comer ali ou levar: for here, to go.
S: pedir para comer no local ou levar: Is it for here or to go?
Y: Hoje você aprende a pedir na lanchonete: for here (para comer aqui) e to go (para levar). Is it for here or to go?
F: Diner | 🎬 Filme | 1982 | um filme escrito e dirigido por Barry Levinson, sobre amigos que se encontram numa lanchonete de Baltimore | pedir para comer ali ou levar | rainycafe | 🍔,🥤,🍟
V: 🍔|burger|hambúrguer|BÂR-ger
V: 🍟|fries|batata frita|FRÁIZ
V: 🥤|milkshake|milk-shake|MÍLK-shêik
V: 🥡|takeout box|marmita|TÊIK-áut-bóks
V: 🍴|fork|garfo|FÓRK
V: 🧾|bill|conta|BÍL
H: Is it for here or to go?|É para comer aqui ou para levar?
H: Fries to go, please.|Batata frita para levar, por favor.
H: A milkshake for here, please.|Um milk-shake para comer aqui, por favor.
H: The takeout box is to go.|A marmita é para levar.
H: Do you want a fork?|Você quer um garfo?
L: Boogie, is it for here or to go?|Boogie, é para comer aqui ou para levar?
L: Burger for here, please.|Hambúrguer para comer aqui, por favor.
L: And the fries?|E a batata frita?
L: Fries to go, please.|Batata frita para levar, por favor.
L: A milkshake for here, too.|Um milk-shake para comer aqui também.
L: The takeout box is to go. Do you want a fork?|A marmita é para levar. Você quer um garfo?
L: Yes, please. Can I have the bill?|Sim, por favor. Posso pegar a conta?
L: Sure. Thanks, Eddie!|Claro. Obrigado, Eddie!
Q: What is for here?|O que é para comer aqui?|1|🍔 The burger|🍟 The fries|🥡 The box
Q: What are the fries?|Como é a batata frita?|3|🍟 To go|🍟 For here|🍟 Cold
Q: What does Boogie ask for at the end?|O que o Boogie pede no fim?|6|🧾 The bill|🍴 A fork|🥤 A milkshake
B: order|🧾|pedir|I order a burger.|He orders a burger.|She ordered fries.|Ela pediu batata frita.
B: wrap|🎁|embrulhar|I wrap the burger.|He wraps the burger.|They wrapped the fries.|Eles embrulharam a batata.
B: sit|🪑|sentar|I sit at the counter.|He sits at the counter.|We sat by the window.|Nós sentamos perto da janela.
B: ask|❓|perguntar|I ask for a fork.|He asks for a fork.|She asked for the bill.|Ela pediu a conta.
LAB: bu|Laboratório de sons: burger, fries e fork|Burger tem a força no começo, “BÂR-ger”. Fries soa “FRÁIZ”. Fork soa “FÓRK”, com o aberto.|Em burger, o u soa como â: BÂR-ger.
W: burger|BÂR-ger|hambúrguer|u = â|bugger|BÂ-ger
W: fries|FRÁIZ|batata frita|ie = ái|freeze|FRÍZ
W: fork|FÓRK|garfo|o aberto|folk|FÔUK
G: 0|for here|for there|to here
G: 1|to go|to went|for go
G: 2|for here|in here|at here
G: 3|to go|to goes|for going
X: 😊|Here you go|Aqui está|entregar|Here you go, your burger.|Aqui está, o seu hambúrguer.
X: 🙏|Thanks a lot|Muito obrigado|agradecer|Thanks a lot, Eddie.|Muito obrigado, Eddie.
X: 👌|That’s all|É só isso|encerrar o pedido|That’s all, thank you.|É só isso, obrigado.
X: 😋|Sounds good|Parece bom|aceitar|Sounds good, I am hungry.|Parece bom, estou com fome.

N: 7009815
C: John,Jenny | tom,polly | Em casa, John e Jenny veem a tigela do cachorro e dizem: empty, full, enough.
S: dizer se algo está vazio, cheio ou é suficiente: The bowl is empty. There isn’t enough food
Y: Hoje você aprende empty (vazio), full (cheio) e enough (suficiente). The bowl is empty. There isn’t enough food.
F: Marley and Me | 🎬 Filme | 2008 | um filme dirigido por David Frankel, sobre um casal e seu cachorro grande e bagunceiro | dizer se a tigela está vazia ou cheia | toyshop | 🐕,🥣,🍖
V: 🥣|bowl|tigela|BÔUL
V: 🍖|food|comida|FÚD
V: 🥫|can|lata|KÉN
V: 💧|water|água|UÓ-der
V: 🐕|dog|cachorro|DÓG
V: 🛍️|bag|saco|BÉG
H: The bowl is empty. He is hungry.|A tigela está vazia. Ele está com fome.
H: There isn’t enough food.|Não tem comida suficiente.
H: The can is full of food.|A lata está cheia de comida.
H: There is enough water.|Tem água suficiente.
H: The bag is empty. Let’s buy more.|O saco está vazio. Vamos comprar mais.
L: Jenny, the bowl is empty.|Jenny, a tigela está vazia.
L: Poor dog! He is hungry.|Pobre cachorro! Ele está com fome.
L: There isn’t enough food in the house.|Não tem comida suficiente em casa.
L: The can is full of food.|A lata está cheia de comida.
L: Good. Is there enough water?|Bom. Tem água suficiente?
L: Yes, there is enough water.|Sim, tem água suficiente.
L: The bag is empty. Let’s buy more.|O saco está vazio. Vamos comprar mais.
L: Okay. The bowl is full now. Eat, boy!|Certo. A tigela está cheia agora. Coma, garoto!
Q: How is the bowl at first?|Como está a tigela no início?|0|🥣 Empty|🥣 Full|🥣 Hot
Q: What is full of food?|O que está cheio de comida?|3|🥫 The can|🛍️ The bag|🥣 The bowl
Q: What do they buy?|O que eles compram?|6|🛍️ More food|💧 More water|🐕 A dog
B: fill|🥣|encher|I fill the bowl.|She fills the bowl.|He filled the can.|Ele encheu a lata.
B: buy|🛒|comprar|I buy dog food.|She buys dog food.|They bought a bag.|Eles compraram um saco.
B: feed|🍖|alimentar|I feed the dog.|She feeds the dog.|He fed the dog twice.|Ele alimentou o cachorro duas vezes.
B: wag|🐕|abanar|I wag my hand.|The dog wags his tail.|He wagged it fast.|Ele a abanou rápido.
LAB: bo|Laboratório de sons: bowl, food e water|Bowl soa “BÔUL”. Food tem u longo, “FÚD”. Water soa “UÓ-der”, com tt rápido.|Em food, alongue o u: FÚÚD.
W: bowl|BÔUL|tigela|ow = ôu|ball|BÓL
W: food|FÚD|comida|oo = ú longo|foot|FÚT
W: water|UÓ-der|água|t = d suave|waiter|UÊI-der
G: 0|empty|full|enough
G: 1|enough|empty|full
G: 2|full|empty|enough
G: 4|empty|full|enough
X: 😢|Poor dog|Pobre cachorro|ter pena|Poor dog, he is hungry.|Pobre cachorro, ele está com fome.
X: 🛒|Let’s buy more|Vamos comprar mais|propor|Let’s buy more food.|Vamos comprar mais comida.
X: 😊|Good boy|Bom garoto|elogiar|Good boy, eat your food.|Bom garoto, coma sua comida.
X: 😅|Oh no|Ai, não|reagir|Oh no, the bag is empty.|Ai, não, o saco está vazio.

N: 7030045
C: Hassan,Marguerite | tommy,polly | No restaurante, Hassan e Marguerite pedem uma recomendação: What do you recommend? I’d like…
S: pedir uma recomendação e fazer o pedido: What do you recommend? I’d like the steak
Y: Hoje você aprende a pedir uma recomendação (What do you recommend?) e a fazer o pedido (I’d like…).
F: The Hundred-Foot Journey | 🎬 Filme | 2014 | um filme dirigido por Lasse Hallström, sobre duas famílias que têm restaurantes vizinhos e aprendem a cozinhar juntas | pedir uma recomendação e fazer o pedido | bakery | 🍽️,🐟,🥩
V: 🧑‍🍳|waiter|garçom|UÊI-der
V: 🐟|fish|peixe|FÍSH
V: 🥩|steak|bife|STÊIK
V: 🍗|chicken|frango|TCHÍ-kin
V: 🥗|salad|salada|SÉ-lad
V: 🍰|dessert|sobremesa|di-ZÂRT
H: What do you recommend?|O que você recomenda?
H: I recommend the fish.|Eu recomendo o peixe.
H: I’d like the steak, please.|Eu gostaria do bife, por favor.
H: What about chicken?|Que tal frango?
H: I’d like a salad, too.|Eu gostaria de uma salada também.
L: Good evening. Here is the menu.|Boa noite. Aqui está o cardápio.
L: What do you recommend, Hassan?|O que você recomenda, Hassan?
L: I recommend the fish. It is fresh today.|Eu recomendo o peixe. Ele está fresco hoje.
L: Hmm. What about chicken?|Hmm. Que tal frango?
L: The chicken is good, too.|O frango também é bom.
L: I’d like the steak, please.|Eu gostaria do bife, por favor.
L: Of course. I’d like a salad, too.|Claro. Eu gostaria de uma salada também.
L: And dessert? I recommend the cake.|E sobremesa? Eu recomendo o bolo.
Q: What does Hassan recommend?|O que o Hassan recomenda?|2|🐟 The fish|🍗 The chicken|🥩 The steak
Q: What does Marguerite order?|O que a Marguerite pede?|5|🥩 The steak|🐟 The fish|🍗 The chicken
Q: What does Hassan recommend for dessert?|O que o Hassan recomenda de sobremesa?|7|🍰 The cake|🥗 The salad|🍽️ The menu
B: order|🧾|pedir|I order the steak.|She orders the steak.|He ordered fish.|Ele pediu peixe.
B: recommend|👍|recomendar|I recommend the fish.|He recommends the fish.|She recommended dessert.|Ela recomendou sobremesa.
B: choose|☑️|escolher|I choose the salad.|She chooses the salad.|They chose chicken.|Eles escolheram frango.
B: serve|🍽️|servir|I serve the fish.|He serves the fish.|They served dinner.|Eles serviram o jantar.
LAB: me|Laboratório de sons: waiter, steak e dessert|Waiter soa “UÊI-der”, com tt rápido. Steak tem o ditongo êi, “STÊIK”. Dessert tem a força no fim, “di-ZÂRT”.|Em steak, ea soa êi: STÊIK, como em break.
W: waiter|UÊI-der|garçom|tt = d suave|water|UÓ-der
W: steak|STÊIK|bife|ea = êi|stick|STÍK
W: dessert|di-ZÂRT|sobremesa|força no fim|desert|DÉ-zert
G: 0|recommend|recommends|recommending
G: 2|like|likes|liking
G: 3|about|for|with
G: 4|I’d|I|Me
X: 😋|Sounds great|Parece ótimo|aceitar|Sounds great, I’d like it.|Parece ótimo, eu gostaria.
X: 🙏|Thank you|Obrigado|agradecer|Thank you, Hassan.|Obrigado, Hassan.
X: 😊|Good choice|Boa escolha|elogiar|Good choice, the fish.|Boa escolha, o peixe.
X: 🍽️|Enjoy your meal|Bom apetite|desejar|Enjoy your meal, Marguerite.|Bom apetite, Marguerite.

N: 7009817
C: Mark,Lewis | tommy,tom | Numa nave, Mark e Lewis calculam quanto tempo leva cada coisa: It takes…
S: falar de duração com It takes…: It takes two days to fix the rocket
Y: Hoje você aprende a falar de duração com It takes…: It takes two days to fix the rocket. How long does it take?
F: The Martian | 🎬 Filme | 2015 | um filme dirigido por Ridley Scott, sobre um astronauta que fica sozinho em Marte e precisa se virar até ser resgatado | falar de quanto tempo as coisas levam | ship | 🚀,🪐,🥔
V: 🚀|rocket|foguete|RÓ-kit
V: 🪐|planet|planeta|PLÉ-net
V: 📅|day|dia|DÊI
V: 🥔|potato|batata|po-TÊI-tô
V: 📡|radio|rádio|RÊI-di-ô
V: 🧑‍🚀|astronaut|astronauta|É-stro-nót
H: It takes two days to fix the rocket.|Leva dois dias para consertar o foguete.
H: It takes a long time to reach the planet.|Leva muito tempo para chegar ao planeta.
H: It takes one day to cook.|Leva um dia para cozinhar.
H: It takes weeks to grow a potato.|Leva semanas para cultivar uma batata.
H: How long does it take?|Quanto tempo leva?
L: Commander, the rocket is broken.|Comandante, o foguete está quebrado.
L: How long does it take to fix it?|Quanto tempo leva para consertá-la?
L: It takes two days to fix the rocket.|Leva dois dias para consertar o foguete.
L: And the planet? It takes a long time to reach it.|E o planeta? Leva muito tempo para chegar lá.
L: We need food. It takes weeks to grow a potato.|Precisamos de comida. Leva semanas para cultivar uma batata.
L: Call Earth on the radio.|Chame a Terra pelo rádio.
L: How long does it take for the answer?|Quanto tempo leva para a resposta?
L: It takes one day. Be patient, Mark.|Leva um dia. Tenha paciência, Mark.
Q: How long does it take to fix the rocket?|Quanto tempo leva para consertar o foguete?|2|📅 Two days|📅 One day|📅 Two weeks
Q: What takes weeks to grow?|O que leva semanas para crescer?|4|🥔 A potato|🚀 The rocket|📡 The radio
Q: How long does the answer take?|Quanto tempo leva a resposta?|7|📅 One day|📅 Two days|📅 Weeks
B: fix|🔧|consertar|I fix the rocket.|He fixes the rocket.|They fixed the radio.|Eles consertaram o rádio.
B: grow|🌱|cultivar|I grow a potato.|He grows a potato.|She grew food.|Ela cultivou comida.
B: wait|⏳|esperar|I wait for Earth.|He waits for Earth.|We waited a day.|Nós esperamos um dia.
B: reach|🪐|chegar a|I reach the planet.|He reaches the planet.|They reached it in a month.|Eles chegaram lá em um mês.
LAB: pl|Laboratório de sons: planet, potato e astronaut|Planet tem a força no começo, “PLÉ-net”. Potato tem a força em -TÊI-, “po-TÊI-tô”. Astronaut soa “É-stro-nót”.|Em potato, a força cai na segunda sílaba: po-TÊI-tô.
W: planet|PLÉ-net|planeta|força no começo|plant|PLÉNT
W: potato|po-TÊI-tô|batata|força no meio|pot|PÓT
W: astronaut|É-stro-nót|astronauta|força no começo|asteroid|É-ste-róid
G: 0|takes|take|taking
G: 1|takes|take|taking
G: 2|to|for|at
G: 4|does|do|is
X: 😅|Be patient|Tenha paciência|acalmar|Be patient, it takes time.|Tenha paciência, leva tempo.
X: 💪|Keep going|Continue|animar|Keep going, Mark.|Continue, Mark.
X: 😮|That’s long|É muito tempo|reagir|That’s long, two weeks.|É muito tempo, duas semanas.
X: 🙂|No rush|Sem pressa|acalmar|No rush, we have time.|Sem pressa, temos tempo.

N: 7030047
C: Hilts,Hendley | polly,tom | No campo na Alemanha, Hilts e Hendley estudam alemão: learn, study, practice.
S: falar de aprendizado com learn, study e practice: I study German. I practice every day
Y: Hoje você aprende learn (aprender), study (estudar) e practice (praticar). I study German grammar. I practice every day.
F: The Great Escape | 🎬 Filme | 1963 | um filme dirigido por John Sturges, sobre prisioneiros de guerra num campo na Alemanha que planejam fugir juntos | falar de aprender e praticar uma língua | cave | 🇩🇪,📖,✏️
V: 🗣️|accent|sotaque|ÉK-sent
V: 📚|grammar|gramática|GRÉ-mar
V: ❌|mistake|erro|mis-TÊIK
V: 📖|dictionary|dicionário|DÍK-sho-né-ri
V: 📓|notebook|caderno|NÔUT-búk
V: 👩‍🏫|teacher|professora|TÍ-tcher
H: I practice with a strange accent.|Eu pratico com um sotaque estranho.
H: I study German grammar.|Eu estudo a gramática do alemão.
H: I learn from my mistakes.|Eu aprendo com os meus erros.
H: I learn new words with a dictionary.|Eu aprendo palavras novas com um dicionário.
H: We study in a notebook.|Nós estudamos num caderno.
L: Hendley, I learn German now.|Hendley, eu aprendo alemão agora.
L: Good. I study German grammar.|Bom. Eu estudo a gramática do alemão.
L: I practice with a strange accent.|Eu pratico com um sotaque estranho.
L: That is fine. I make a lot of mistakes.|Tudo bem. Eu cometo muitos erros.
L: We all learn from our mistakes.|Todos nós aprendemos com os nossos erros.
L: I learn new words with a dictionary.|Eu aprendo palavras novas com um dicionário.
L: Let’s study in a notebook together.|Vamos estudar juntos num caderno.
L: Good idea. I practice every day.|Boa ideia. Eu pratico todo dia.
Q: What does Hendley study?|O que o Hendley estuda?|1|📚 German grammar|📖 A story|🗣️ Music
Q: What do they learn from?|Com o que eles aprendem?|4|❌ Their mistakes|🗣️ Their accent|📓 Their notebook
Q: How often does Hendley practice?|Com que frequência o Hendley pratica?|7|📅 Every day|📅 Once a week|📅 Never
B: learn|💡|aprender|I learn German.|He learns German.|She learned ten words.|Ela aprendeu dez palavras.
B: study|📚|estudar|I study grammar.|He studies grammar.|We studied for an hour.|Nós estudamos por uma hora.
B: practice|🗣️|praticar|I practice every day.|He practices every day.|They practiced a lot.|Eles praticaram muito.
B: repeat|🔁|repetir|I repeat the word.|He repeats the word.|She repeated it twice.|Ela a repetiu duas vezes.
LAB: ac|Laboratório de sons: accent, mistake e teacher|Accent tem a força no começo, “ÉK-sent”. Mistake tem a força no fim, “mis-TÊIK”. Teacher soa “TÍ-tcher”.|Em teacher, ea soa í e ch soa tch: TÍ-tcher.
W: accent|ÉK-sent|sotaque|força no começo|ascent|a-SÉNT
W: mistake|mis-TÊIK|erro|força no fim|mist|MÍST
W: teacher|TÍ-tcher|professora|ea = í|teaser|TÍ-zer
G: 0|practice|practices|practicing
G: 1|study|studies|studying
G: 2|learn|learns|learning
G: 4|study|studies|studying
X: 😅|Don’t worry|Não se preocupe|acalmar|Don’t worry, you learn fast.|Não se preocupe, você aprende rápido.
X: 💪|Try again|Tente de novo|animar|Try again, Hilts.|Tente de novo, Hilts.
X: 👍|Well done|Muito bem|elogiar|Well done, your accent is good.|Muito bem, seu sotaque está bom.
X: 🤔|Say it again|Diga de novo|pedir repetição|Say it again, slowly.|Diga de novo, devagar.

N: 7009818
C: Walter,Cheryl | polly,tom | No quintal, Walter e Cheryl dizem o que querem fazer: want to + verbo.
S: dizer o que quer fazer com want to + verbo: I want to see the world
Y: Hoje você aprende a dizer o que quer fazer: want to + verbo. I want to see the world. Do you want to fly?
F: The Secret Life of Walter Mitty | 🎬 Filme | 2013 | um filme dirigido e estrelado por Ben Stiller, sobre um homem tímido que sonha acordado e depois vive uma grande aventura | dizer o que se quer fazer | cave | 🗺️,📷,🏔️
V: 🗺️|map|mapa|MÉP
V: 📷|camera|câmera|KÉ-me-ra
V: ✈️|plane|avião|PLÊIN
V: 🏔️|mountain|montanha|MÁUN-tn
V: 🎒|backpack|mochila|BÉK-pék
V: 🌍|world|mundo|UÂRLD
H: I want to see the world.|Eu quero ver o mundo.
H: I want to take a photo.|Eu quero tirar uma foto.
H: Do you want to fly?|Você quer voar?
H: Cheryl wants to climb the mountain.|A Cheryl quer escalar a montanha.
H: We want to go now.|Nós queremos ir agora.
L: Cheryl, I want to try something new.|Cheryl, eu quero tentar algo novo.
L: What do you want to do, Walter?|O que você quer fazer, Walter?
L: I want to see the world. Look at the map.|Eu quero ver o mundo. Olhe o mapa.
L: I want to take a photo of the mountain.|Eu quero tirar uma foto da montanha.
L: Do you want to fly?|Você quer voar?
L: Yes! And you want to climb, right?|Sim! E você quer escalar, certo?
L: Cheryl wants to climb the mountain too.|A Cheryl também quer escalar a montanha.
L: Take your backpack. We want to go now.|Pegue sua mochila. Nós queremos ir agora.
Q: What does Walter want to see?|O que o Walter quer ver?|2|🌍 The world|🗺️ A map|✈️ A plane
Q: What does Walter want to photograph?|O que o Walter quer fotografar?|3|🏔️ The mountain|🌍 The world|✈️ A plane
Q: What do they take?|O que eles levam?|7|🎒 A backpack|🗺️ A map|📷 A phone
B: want|⭐|querer|I want to travel.|He wants to travel.|She wanted a camera.|Ela queria uma câmera.
B: climb|🧗|escalar|I climb the mountain.|She climbs the mountain.|He climbed a hill.|Ele escalou um morro.
B: fly|✈️|voar|I fly to the north.|He flies to the north.|We flew all night.|Nós voamos a noite toda.
B: dream|💭|sonhar|I dream of a trip.|He dreams of a trip.|She dreamed of snow.|Ela sonhou com neve.
LAB: ma|Laboratório de sons: map, camera e mountain|Map soa “MÉP”. Camera tem três sílabas, “KÉ-me-ra”. Mountain termina em som mudo, “MÁUN-tn”.|Em mountain, o final é um n curto: MÁUN-tn.
W: map|MÉP|mapa|a aberto|mop|MÓP
W: camera|KÉ-me-ra|câmera|força no começo|came|KÊIM
W: mountain|MÁUN-tn|montanha|ou = áu|fountain|FÁUN-tn
G: 0|want|wants|wanting
G: 1|to|for|in
G: 2|Do|Does|Are
G: 3|wants|want|wanting
X: 🤩|Great idea|Ótima ideia|elogiar|Great idea, let’s go!|Ótima ideia, vamos!
X: 😮|Look at that|Olhe aquilo|chamar atenção|Look at that, a huge mountain!|Olhe aquilo, uma montanha enorme!
X: 💪|Let’s try|Vamos tentar|animar|Let’s try something new.|Vamos tentar algo novo.
X: 🌍|Why not|Por que não|aceitar|Why not, I want to fly.|Por que não, eu quero voar.

N: 7080181
T: Does the fox have big ears?
C: Judy,Nick | rabbit,wolf | Na delegacia, Judy e Nick descrevem alguém com Does he…? Yes, he does.
S: perguntar sobre ele ou ela com Does he…? Yes, he does: Does he have a long nose
Y: Hoje você aprende a perguntar sobre uma pessoa: Does he have big ears? Yes, he does. Does she have a badge? Yes, she does.
F: Zootopia | 🎬 Animação | 2016 | uma animação da Disney, dirigida por Byron Howard e Rich Moore, sobre uma coelha policial e uma raposa esperta que resolvem um caso juntos | perguntar como é uma pessoa | castle | 🐰,🦊,🚔
V: 🐰|rabbit|coelha|RÉ-bit
V: 🦊|fox|raposa|FÓKS
V: 👂|ears|orelhas|ÍRZ
V: 👃|nose|nariz|NÔUZ
V: 🚔|police car|viatura|po-LÍS-kár
V: 🎖️|badge|distintivo|BÉDJ
H: Does she have big ears?|Ela tem orelhas grandes?
H: Yes, he does.|Sim, ele tem.
H: She has big ears.|Ela tem orelhas grandes.
H: Does he have a long nose?|Ele tem um nariz comprido?
H: Does she drive a police car?|Ela dirige uma viatura?
L: Nick, who is the thief?|Nick, quem é o ladrão?
L: Does he have big ears?|Ele tem orelhas grandes?
L: No, he doesn’t. He has a long nose.|Não, não tem. Ele tem um nariz comprido.
L: Does she have a badge, Judy?|Ela tem um distintivo, Judy?
L: Yes, she does. She has big ears.|Sim, tem. Ela tem orelhas grandes.
L: Does she drive a police car?|Ela dirige uma viatura?
L: Yes, she does. It is the blue one.|Sim, dirige. É a azul.
L: Let’s go. I drive today!|Vamos. Eu dirijo hoje!
Q: What does the thief have?|O que o ladrão tem?|2|👃 A long nose|👂 Big ears|🎖️ A badge
Q: Does Judy have a badge?|A Judy tem um distintivo?|4|✅ Yes, she does|❌ No, she doesn’t|🤷 Maybe
Q: What does Judy drive?|O que a Judy dirige?|6|🚔 A police car|🚌 A bus|🚲 A bike
B: have|✋|ter|I have a badge.|She has a badge.|He had big ears.|Ele tinha orelhas grandes.
B: drive|🚔|dirigir|I drive a car.|She drives a car.|They drove all day.|Eles dirigiram o dia todo.
B: look|👀|olhar|I look at the map.|He looks at the map.|She looked at the thief.|Ela olhou para o ladrão.
B: catch|🤲|pegar|I catch the thief.|She catches the thief.|He caught the fox.|Ele pegou a raposa.
LAB: ea|Laboratório de sons: ears, nose e badge|Ears soa “ÍRZ”. Nose soa “NÔUZ”, com o final em z. Badge termina em dj, “BÉDJ”.|Em badge, termine com dj: BÉDJ.
W: ears|ÍRZ|orelhas|ea = í|airs|ÉRZ
W: nose|NÔUZ|nariz|o = ôu|nods|NÓDZ
W: badge|BÉDJ|distintivo|dg = dj|bad|BÉD
G: 0|Does|Do|Is
G: 1|does|do|is
G: 2|has|have|having
G: 3|have|has|having
X: 😮|No way|Não pode ser|se surpreender|No way, he has big ears!|Não pode ser, ele tem orelhas grandes!
X: 🕵️|Good job|Bom trabalho|elogiar|Good job, Judy.|Bom trabalho, Judy.
X: 🤔|Let me see|Deixe-me ver|pensar|Let me see the badge.|Deixe-me ver o distintivo.
X: 🚔|Follow me|Siga-me|chamar|Follow me, Nick.|Siga-me, Nick.

N: 80182
C: Derice,Sanka | tommy,polly | Na pista de gelo, Derice e Sanka dizem o que sempre e nunca fazem: always, never + verbo.
S: dizer o que sempre e nunca faz com always e never: We always push the sled. I never stop
Y: Hoje você aprende always (sempre) e never (nunca): vêm antes do verbo. We always push the sled. I never stop in a race.
F: Cool Runnings | 🎬 Filme | 1993 | uma comédia dirigida por Jon Turteltaub, sobre uma equipe de bobsled que sai do clima quente para competir na neve | falar do que sempre e nunca se faz | lighthouse | 🛷,🏁,🥇
V: 🛷|sled|trenó|SLÉD
V: 🏁|race|corrida|RÊIS
V: 🥇|medal|medalha|MÉ-dol
V: 🧊|ice|gelo|ÁIS
V: ⛑️|helmet|capacete|RÉL-mit
V: ❄️|snow|neve|SNÔU
H: We always push the sled.|Nós sempre empurramos o trenó.
H: I never stop in a race.|Eu nunca paro numa corrida.
H: We always want a medal.|Nós sempre queremos uma medalha.
H: The ice is never soft.|O gelo nunca é macio.
H: I always wear a helmet.|Eu sempre uso capacete.
L: Sanka, we always push the sled.|Sanka, nós sempre empurramos o trenó.
L: Yes. And I never stop in a race.|Sim. E eu nunca paro numa corrida.
L: We always want a medal.|Nós sempre queremos uma medalha.
L: The ice is never soft, Derice.|O gelo nunca é macio, Derice.
L: I always wear a helmet.|Eu sempre uso capacete.
L: Good. I never forget mine.|Bom. Eu nunca esqueço o meu.
L: We are always fast, never slow!|Nós somos sempre rápidos, nunca lentos!
L: Ready? Let’s race in the snow.|Pronto? Vamos correr na neve.
Q: What do they always push?|O que eles sempre empurram?|0|🛷 The sled|🥇 A medal|🧊 The ice
Q: How is the ice?|Como é o gelo?|3|🧊 Never soft|🧊 Always soft|🧊 Warm
Q: What does Derice always wear?|O que o Derice sempre usa?|4|⛑️ A helmet|🥇 A medal|🛷 A sled
B: push|💪|empurrar|I push the sled.|He pushes the sled.|They pushed it fast.|Eles o empurraram rápido.
B: race|🏁|correr (disputa)|I race on the ice.|He races on the ice.|We raced in the snow.|Nós corremos na neve.
B: slide|🛝|deslizar|I slide on the ice.|He slides on the ice.|It slid down the hill.|Ele deslizou pelo morro.
B: win|🥇|ganhar|I win a medal.|He wins a medal.|They won the race.|Eles ganharam a corrida.
LAB: sl|Laboratório de sons: sled, medal e helmet|Sled começa com sl junto, “SLÉD”. Medal tem a força no começo, “MÉ-dol”. Helmet soa “RÉL-mit”.|Em sled, junte s e l: SLÉD.
W: sled|SLÉD|trenó|sl junto|slid|SLÍD
W: medal|MÉ-dol|medalha|força no começo|metal|MÉ-dol
W: helmet|RÉL-mit|capacete|h soprado|hello|re-LÔU
G: 0|always|every|ever
G: 1|never|ever|no
G: 2|always|every|ever
G: 3|never|ever|no
X: 🏁|Ready, set, go|Já, preparar, vai|largar|Ready, set, go!|Já, preparar, vai!
X: 💪|Push harder|Empurre mais forte|animar|Push harder, Sanka!|Empurre mais forte, Sanka!
X: 🥇|We did it|Nós conseguimos|comemorar|We did it, a medal!|Nós conseguimos, uma medalha!
X: 😮|Watch out|Cuidado|avisar|Watch out, the ice!|Cuidado, o gelo!

N: 7080182
C: Claire,Bender | polly,tom | Na biblioteca da escola, Claire e Bender falam do que fazem com often e rarely.
S: falar de rotina com often e rarely: I often study. I rarely check the clock
Y: Hoje você aprende often (muitas vezes) e rarely (raramente): vêm antes do verbo. I often study here. I rarely check the clock.
F: The Breakfast Club | 🎬 Filme | 1985 | um filme escrito e dirigido por John Hughes, sobre cinco alunos diferentes que passam um sábado juntos na biblioteca da escola | falar do que se faz muitas vezes e raramente | library | 📚,🕘,🍔
V: 📚|library|biblioteca|LÁI-bré-ri
V: 🕘|clock|relógio|KLÓK
V: 🍔|lunch|almoço|LÂNTCH
V: 🧑‍🏫|teacher|professor|TÍ-tcher
V: 🎒|bag|bolsa|BÉG
V: 📝|note|bilhete|NÔUT
H: I often study in the library.|Eu estudo muitas vezes na biblioteca.
H: I rarely check the clock.|Eu raramente olho o relógio.
H: I often eat lunch alone.|Eu como sozinho muitas vezes.
H: The teacher is rarely late.|O professor raramente se atrasa.
H: I often forget my bag.|Eu esqueço a minha bolsa muitas vezes.
L: Bender, I often study in the library.|Bender, eu estudo muitas vezes na biblioteca.
L: I rarely check the clock.|Eu raramente olho o relógio.
L: Really? I often check it. It is eight.|Sério? Eu olho muitas vezes. São oito horas.
L: I often eat lunch alone, Claire.|Eu como sozinho muitas vezes, Claire.
L: Not today. We eat together.|Hoje não. Nós comemos juntos.
L: The teacher is rarely late.|O professor raramente se atrasa.
L: I am often early and rarely late.|Eu estou muitas vezes cedo e raramente atrasado.
L: I often forget my bag. Write me a note.|Eu esqueço a minha bolsa muitas vezes. Escreva-me um bilhete.
Q: Where does Claire often study?|Onde a Claire estuda muitas vezes?|0|📚 In the library|🍔 At lunch|🕘 At home
Q: What does Claire rarely do?|O que a Claire raramente faz?|1|🕘 Check the clock|📚 Study|🍔 Eat lunch
Q: What does Bender often forget?|O que o Bender esquece muitas vezes?|7|🎒 His bag|📝 His lunch|🕘 His clock
B: study|📚|estudar|I study in the library.|She studies in the library.|He studied late.|Ele estudou até tarde.
B: check|☑️|conferir|I check the clock.|She checks the clock.|They checked the time.|Eles conferiram a hora.
B: forget|🤦|esquecer|I forget my bag.|He forgets his bag.|She forgot a note.|Ela esqueceu um bilhete.
B: write|✍️|escrever|I write a note.|She writes a note.|He wrote a letter.|Ele escreveu uma carta.
LAB: li|Laboratório de sons: library, lunch e teacher|Library tem a força no começo, “LÁI-bré-ri”. Lunch termina em tch, “LÂNTCH”. Teacher soa “TÍ-tcher”.|Em teacher, ea soa í e ch soa tch: TÍ-tcher.
W: library|LÁI-bré-ri|biblioteca|força no começo|liberty|LÍ-ber-ti
W: lunch|LÂNTCH|almoço|u = â|launch|LÓNTCH
W: teacher|TÍ-tcher|professor|ea = í|tuner|TIÚ-ner
G: 0|often|much|ever
G: 1|rarely|rare|rarity
G: 2|often|much|ever
G: 3|rarely|rare|rarity
X: 😴|Not again|De novo não|reclamar|Not again, I forget my bag.|De novo não, esqueci minha bolsa.
X: 😊|Good morning|Bom dia|cumprimentar|Good morning, Claire.|Bom dia, Claire.
X: 😏|Whatever|Tanto faz|reagir|Whatever, I am early today.|Tanto faz, estou cedo hoje.
X: 🤝|See you|Até logo|despedir-se|See you tomorrow, Bender.|Até amanhã, Bender.

N: 7080183
C: Rudy,Fortune | tom,tommy | No ginásio, Rudy e Fortune contam quantas vezes treinam: once, twice, three times a week.
S: contar as vezes com once, twice e three times a week: I train twice a week
Y: Hoje você aprende a contar as vezes: once (uma vez), twice (duas vezes), three times (três vezes). I go to the gym twice a week.
F: Rudy | 🎬 Filme | 1993 | um filme dirigido por David Anspaugh, sobre um jovem que treina muito para jogar futebol americano na universidade | falar de quantas vezes se treina | castle | 🏈,🏋️,🏟️
V: 🏈|football|futebol americano|FÚT-bol
V: 🏋️|gym|academia|DJÍM
V: 🏃|field|campo|FÍLD
V: 🥤|bottle|garrafa|BÓ-tol
V: 🌳|park|parque|PÁRK
V: 📅|week|semana|UÍK
H: I play football once a week.|Eu jogo futebol americano uma vez por semana.
H: I go to the gym twice a week.|Eu vou à academia duas vezes por semana.
H: I run on the field three times a week.|Eu corro no campo três vezes por semana.
H: I drink water twice a day.|Eu bebo água duas vezes por dia.
H: We train at the park three times a week.|Nós treinamos no parque três vezes por semana.
L: Fortune, how often do you train?|Fortune, com que frequência você treina?
L: I play football once a week.|Eu jogo futebol americano uma vez por semana.
L: I go to the gym twice a week.|Eu vou à academia duas vezes por semana.
L: I run on the field three times a week.|Eu corro no campo três vezes por semana.
L: Drink water. I drink water twice a day.|Beba água. Eu bebo água duas vezes por dia.
L: Take your bottle to the park.|Leve sua garrafa para o parque.
L: We train there three times a week.|Nós treinamos lá três vezes por semana.
L: Good. See you on the field, Rudy!|Bom. Até o campo, Rudy!
Q: How often does Fortune play football?|Com que frequência o Fortune joga?|1|🏈 Once a week|🏈 Twice a week|🏈 Every day
Q: How often does Rudy go to the gym?|Com que frequência o Rudy vai à academia?|2|🏋️ Twice a week|🏋️ Once a week|🏋️ Never
Q: How often do they train at the park?|Com que frequência eles treinam no parque?|6|🌳 Three times a week|🌳 Once a week|🌳 Twice a week
B: train|🏋️|treinar|I train at the gym.|He trains at the gym.|We trained all week.|Nós treinamos a semana toda.
B: run|🏃|correr|I run on the field.|He runs on the field.|They ran two laps.|Eles correram duas voltas.
B: stretch|🤸|alongar|I stretch my legs.|He stretches his legs.|She stretched her arms.|Ela alongou os braços.
B: throw|🏈|arremessar|I throw the ball.|He throws the ball.|She threw it far.|Ela o arremessou longe.
LAB: fo|Laboratório de sons: football, gym e park|Football junta foot e ball, “FÚT-bol”. Gym começa com dj, “DJÍM”. Park termina em k, “PÁRK”.|Em gym, o g soa dj: DJÍM.
W: football|FÚT-bol|futebol americano|foot + ball|foot|FÚT
W: gym|DJÍM|academia|g = dj|jam|DJÉM
W: park|PÁRK|parque|a aberto|pork|PÓRK
G: 0|once|one|first
G: 1|twice|two|second
G: 2|three times|three time|three timing
G: 4|three times|three time|three timing
X: 💪|Keep it up|Continue assim|animar|Keep it up, Rudy.|Continue assim, Rudy.
X: 😅|I’m tired|Estou cansado|reclamar|I’m tired, but I train.|Estou cansado, mas eu treino.
X: 🏆|Never give up|Nunca desista|animar|Never give up, Rudy.|Nunca desista, Rudy.
X: 🤝|Good game|Bom jogo|elogiar|Good game, Fortune.|Bom jogo, Fortune.

N: 7080185
C: Buddy,Jovie | tom,polly | No Polo Norte, Buddy e Jovie pedem com educação para não fazer algo: Please don’t + verbo.
S: pedir para não fazer algo com Please don’t + verbo: Please don’t open the gift
Y: Hoje você aprende a pedir para não fazer algo: Please don’t + verbo. Please don’t open the gift. Please don’t touch the tree.
F: Elf | 🎬 Filme | 2003 | uma comédia de Natal dirigida por Jon Favreau, sobre um homem criado por elfos que vai conhecer a cidade de Nova York | pedir com educação para não fazer algo | castle | 🎄,🎁,🎅
V: 🎁|gift|presente|GUÍFT
V: 🎄|tree|árvore|TRÍ
V: 🍬|candy|bala|KÉN-di
V: 🛷|sleigh|trenó|SLÊI
V: 🎅|Santa|Papai Noel|SÉN-ta
V: ❄️|snow|neve|SNÔU
H: Please don’t open the gift.|Por favor, não abra o presente.
H: Please don’t touch the tree.|Por favor, não toque na árvore.
H: Please don’t eat all the candy.|Por favor, não coma toda a bala.
H: Please don’t sit on the sleigh.|Por favor, não sente no trenó.
H: Please don’t wake Santa.|Por favor, não acorde o Papai Noel.
L: Jovie, please don’t open the gift.|Jovie, por favor, não abra o presente.
L: Okay. Please don’t touch the tree, Buddy.|Certo. Por favor, não toque na árvore, Buddy.
L: Sorry! Please don’t eat all the candy.|Desculpe! Por favor, não coma toda a bala.
L: I don’t. I eat only two.|Eu não como. Eu como só duas.
L: Please don’t sit on the sleigh.|Por favor, não sente no trenó.
L: Why? It is so cool.|Por quê? Ele é tão legal.
L: Shh. Please don’t wake Santa.|Shh. Por favor, não acorde o Papai Noel.
L: Okay. Let’s play in the snow instead.|Certo. Vamos brincar na neve em vez disso.
Q: What can’t Jovie open?|O que a Jovie não pode abrir?|0|🎁 The gift|🎄 The tree|🛷 The sleigh
Q: What can’t Buddy sit on?|Em que o Buddy não pode sentar?|4|🛷 The sleigh|🎄 The tree|🎁 The gift
Q: Who is asleep?|Quem está dormindo?|6|🎅 Santa|🎄 The tree|🍬 The candy
B: touch|✋|tocar|I touch the tree.|He touches the tree.|She touched the gift.|Ela tocou o presente.
B: open|📦|abrir|I open the gift.|He opens the gift.|They opened the box.|Eles abriram a caixa.
B: wake|⏰|acordar|I wake Santa.|He wakes Santa.|She woke the elf.|Ela acordou o elfo.
B: sit|🪑|sentar|I sit on the sleigh.|He sits on the sleigh.|We sat in the snow.|Nós sentamos na neve.
LAB: gi|Laboratório de sons: gift, sleigh e Santa|Gift começa com g duro, “GUÍFT”. Sleigh soa “SLÊI”, com o gh mudo. Santa soa “SÉN-ta”.|Em sleigh, o gh não se fala: SLÊI.
W: gift|GUÍFT|presente|g duro|give|GUÍV
W: sleigh|SLÊI|trenó|eigh = êi|sly|SLÁI
W: Santa|SÉN-ta|Papai Noel|a = é|sander|SÉN-der
G: 0|don’t|doesn’t|not
G: 1|touch|touching|touches
G: 2|eat|ate|eating
G: 4|wake|wakes|waking
X: 😅|Sorry|Desculpe|se desculpar|Sorry, Jovie.|Desculpe, Jovie.
X: 🤫|Be quiet|Fique quieto|pedir silêncio|Be quiet, Santa is asleep.|Fique quieto, o Papai Noel está dormindo.
X: 🎄|Merry Christmas|Feliz Natal|desejar|Merry Christmas, Buddy!|Feliz Natal, Buddy!
X: 😄|So cool|Tão legal|elogiar|So cool, the sleigh!|Tão legal, o trenó!
''')
