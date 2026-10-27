# Lote B (cinema), dados 8: episódios A1 7910028 .. 7910030. Formato: ver zz_b_lib.py.
from v3.zz_b_lib import add

add('''
N: 7910028
C: Dennis,Mr. Wilson | tommy,tom | Na casa do vizinho, Dennis explica o que quebrou: by mistake, on purpose.
S: explicar um erro com by mistake e on purpose: I broke the vase by mistake. I did not do it on purpose
Y: Hoje você aprende by mistake (sem querer) e on purpose (de propósito). I broke the vase by mistake. I did not do it on purpose.
F: Dennis the Menace | 🎬 Filme | 1993 | uma comédia dirigida por Nick Castle, sobre um menino travesso que apronta na casa do vizinho | explicar que algo foi sem querer ou de propósito | castle | 🏺,⚽,🪟
V: 🏺|vase|vaso|VÊIS
V: ⚽|ball|bola|BÓL
V: 🪟|window|janela|UÍN-dô
V: 🐕|dog|cachorro|DÓG
V: 🌸|flowers|flores|FLÁU-erz
V: 🌷|garden|jardim|GÁR-dn
H: I broke the vase by mistake.|Eu quebrei o vaso sem querer.
H: The ball hit the window by mistake.|A bola bateu na janela sem querer.
H: I did not do it on purpose.|Eu não fiz isso de propósito.
H: The dog ran away by mistake.|O cachorro fugiu sem querer.
H: I picked the flowers on purpose.|Eu colhi as flores de propósito.
L: Mister Wilson, I broke the vase by mistake.|Senhor Wilson, eu quebrei o vaso sem querer.
L: By mistake, Dennis? Again?|Sem querer, Dennis? De novo?
L: The ball hit the window by mistake, too.|A bola bateu na janela sem querer também.
L: I did not do it on purpose.|Eu não fiz isso de propósito.
L: And the dog ran away by mistake.|E o cachorro fugiu sem querer.
L: Did you pick my flowers?|Você colheu as minhas flores?
L: Yes, on purpose. They are for you!|Sim, de propósito. Elas são para o senhor!
L: Then thank you. Now go to the garden.|Então obrigado. Agora vá ao jardim.
Q: What did Dennis break?|O que o Dennis quebrou?|0|🏺 The vase|🪟 The window|⚽ The ball
Q: What ran away by mistake?|O que fugiu sem querer?|4|🐕 The dog|🏺 The vase|⚽ The ball
Q: Why did Dennis pick the flowers?|Por que o Dennis colheu as flores?|6|🌸 On purpose, for Mister Wilson|🏺 By mistake|🐕 For the dog
B: drop|🫳|derrubar|I drop the vase.|He drops the vase.|She dropped the ball.|Ela derrubou a bola.
B: throw|🥎|jogar|I throw the ball.|He throws the ball.|She threw it far.|Ela o jogou longe.
B: promise|🤞|prometer|I promise to be good.|He promises to be good.|She promised twice.|Ela prometeu duas vezes.
B: wave|👋|acenar|I wave at Mister Wilson.|He waves at Mister Wilson.|They waved goodbye.|Eles acenaram em despedida.
LAB: va|Laboratório de sons: vase, window e garden|Vase soa “VÊIS”. Window soa “UÍN-dô”. Garden soa “GÁR-dn”, com a aberto.|Em window, o w soa u: UÍN-dô.
W: vase|VÊIS|vaso|a = êi|face|FÊIS
W: window|UÍN-dô|janela|w = u|widow|UÍ-dô
W: garden|GÁR-dn|jardim|a aberto|guard|GÁRD
G: 0|by mistake|by error|in mistake
G: 1|by mistake|by error|in mistake
G: 2|on purpose|in purpose|by purpose
G: 4|on purpose|in purpose|by purpose
X: 😅|Sorry|Desculpe|se desculpar|Sorry, Mister Wilson.|Desculpe, senhor Wilson.
X: 😬|Oops|Ops|reagir|Oops, the vase!|Ops, o vaso!
X: 🙏|I promise|Eu prometo|prometer|I promise, no more mess.|Eu prometo, chega de bagunça.
X: 😊|It’s okay|Tudo bem|perdoar|It’s okay, Dennis.|Tudo bem, Dennis.

N: 80230
C: Rebecca,Luke | tom,polly | Numa loja de roupas, Rebecca e Luke pedem para provar: try on, changing room.
S: provar roupa com try on e changing room: Could I try it on? Where is the changing room
Y: Hoje você aprende try on (provar) e changing room (provador). Could I try it on? Where is the changing room?
F: Confessions of a Shopaholic | 🎬 Filme | 2009 | uma comédia dirigida por P. J. Hogan, sobre uma jovem que adora fazer compras e se enrola com as contas | provar roupas numa loja | toyshop | 🛍️,👗,🪞
V: 🧥|jacket|jaqueta|DJÉ-kit
V: 🪞|mirror|espelho|MÍ-rer
V: 👗|skirt|saia|SKÂRT
V: 🏷️|price tag|etiqueta|PRÁIS-tég
V: 👜|handbag|bolsa|RÉND-bég
V: 💳|card|cartão|KÁRD
H: Could I try it on?|Posso provar?
H: Is there a mirror in the changing room?|Tem um espelho no provador?
H: I want to try on this skirt.|Eu quero provar esta saia.
H: Where is the changing room?|Onde fica o provador?
H: Look at the price tag first.|Olhe a etiqueta de preço primeiro.
L: Excuse me, I like this jacket. Could I try it on?|Com licença, eu gosto desta jaqueta. Posso provar?
L: Of course, Rebecca. The changing room is there.|Claro, Rebecca. O provador fica ali.
L: Is there a mirror in the changing room?|Tem um espelho no provador?
L: Yes. I want to try on this skirt, too.|Sim. Eu quero provar esta saia também.
L: Where is the changing room for skirts?|Onde fica o provador das saias?
L: It is next to the handbags.|Fica ao lado das bolsas.
L: Look at the price tag first, Rebecca.|Olhe a etiqueta de preço primeiro, Rebecca.
L: Oh no! Maybe I just look today.|Ai, não! Talvez eu só olhe hoje.
Q: What does Rebecca want to try?|O que a Rebecca quer provar?|0|🧥 A jacket|👜 A handbag|💳 A card
Q: What is in the changing room?|O que há no provador?|2|🪞 A mirror|👗 A skirt|💳 A card
Q: What should Rebecca look at first?|O que a Rebecca deve olhar primeiro?|6|🏷️ The price tag|🪞 The mirror|👜 The handbag
B: try|👗|experimentar|I try the jacket.|She tries the jacket.|He tried a skirt.|Ele experimentou uma saia.
B: pick|☑️|escolher|I pick a skirt.|She picks a skirt.|They picked two jackets.|Eles escolheram dois casacos.
B: hold|🤲|segurar|I hold the handbag.|She holds the handbag.|He held the card.|Ele segurou o cartão.
B: smile|😊|sorrir|I smile at the mirror.|She smiles at the mirror.|We smiled together.|Nós sorrimos juntos.
LAB: ja|Laboratório de sons: jacket, mirror e skirt|Jacket começa com dj, “DJÉ-kit”. Mirror soa “MÍ-rer”. Skirt soa “SKÂRT”, com ir = âr.|Em skirt, o ir soa âr: SKÂRT.
W: jacket|DJÉ-kit|jaqueta|j = dj|packet|PÉ-kit
W: mirror|MÍ-rer|espelho|ir = ír|minor|MÁI-ner
W: skirt|SKÂRT|saia|ir = âr|shirt|SHÂRT
G: 0|try it on|try on it|try in it
G: 1|changing room|change room|changed room
G: 2|try on|try in|try at
G: 3|changing room|change room|changed room
X: 😍|It’s perfect|É perfeito|elogiar|It’s perfect, I love it.|É perfeito, eu amei.
X: 🙁|Too tight|Apertado demais|reclamar|Too tight, try a bigger size.|Apertado demais, tente um tamanho maior.
X: 💳|Maybe later|Talvez depois|adiar|Maybe later, I look first.|Talvez depois, eu olho primeiro.
X: 😊|Take your time|Fique à vontade|acalmar|Take your time, Rebecca.|Fique à vontade, Rebecca.

N: 7080230
C: Edna,Helen | misshoney,polly | No ateliê, Edna e Helen escolhem uniformes: the red one, the big ones.
S: escolher com one e ones: I like the red one. The big ones are heavy
Y: Hoje você aprende a não repetir a palavra: the red one (o vermelho) e the big ones (os grandes). I like the red one.
F: The Incredibles | 🎬 Animação | 2004 | uma animação da Pixar, dirigida por Brad Bird, sobre uma família de super-heróis que tenta viver uma vida normal | escolher entre várias coisas sem repetir a palavra | bakery | 🦸,🎭,🧵
V: 🦸|suit|uniforme|SÚT
V: 🧣|cape|capa|KÊIP
V: 🎭|mask|máscara|MÉSK
V: 🥋|belt|cinto|BÉLT
V: 👟|sneakers|tênis|SNÍ-kerz
V: 🧵|thread|linha|THRÉD
H: I like the red one.|Eu gosto do vermelho.
H: No cape! I like the big ones.|Sem capa! Eu gosto dos grandes.
H: The black one, please.|O preto, por favor.
H: The small ones are too tight.|Os pequenos estão apertados demais.
H: The white ones are comfortable.|Os brancos são confortáveis.
L: Helen, which suit do you like?|Helen, de qual uniforme você gosta?
L: I like the red one, Edna.|Eu gosto do vermelho, Edna.
L: No cape! Do you like the big ones?|Sem capa! Você gosta das grandes?
L: Yes, I like the big ones. What about the mask?|Sim, eu gosto das grandes. E a máscara?
L: The black one, please.|A preta, por favor.
L: And the belts? The small ones are too tight.|E os cintos? Os pequenos estão apertados demais.
L: Then take the sneakers. The white ones are comfortable.|Então leve os tênis. Os brancos são confortáveis.
L: Perfect. I sew the thread today.|Perfeito. Eu costuro com a linha hoje.
Q: Which suit does Helen like?|De qual uniforme a Helen gosta?|1|🦸 The red one|🦸 The black one|🦸 The white one
Q: Which mask does Helen want?|Qual máscara a Helen quer?|4|🎭 The black one|🎭 The red one|🎭 The big one
Q: Which sneakers are comfortable?|Quais tênis são confortáveis?|6|👟 The white ones|👟 The small ones|👟 The red ones
B: choose|☑️|escolher|I choose the red one.|She chooses the red one.|He chose the black one.|Ele escolheu o preto.
B: design|✏️|desenhar (projetar)|I design a suit.|She designs a suit.|They designed a mask.|Eles projetaram uma máscara.
B: sew|🧵|costurar|I sew the cape.|She sews the cape.|He sewed the belt.|Ele costurou o cinto.
B: fit|📏|servir|The suit fits me.|The suit fits her.|The mask fit well.|A máscara serviu bem.
LAB: su|Laboratório de sons: suit, cape e thread|Suit soa “SÚT”, com ui = ú. Cape soa “KÊIP”. Thread começa com th soprado, “THRÉD”.|Em thread, o th inicial é soprado: THRÉD.
W: suit|SÚT|uniforme|ui = ú|soot|SÚT
W: cape|KÊIP|capa|a = êi|cap|KÉP
W: thread|THRÉD|linha|th soprado|dread|DRÉD
G: 0|one|ones|once
G: 1|ones|one|once
G: 2|one|ones|once
G: 3|ones|one|once
X: 😎|No capes|Sem capas|opinar|No capes, darling!|Sem capas, querida!
X: 😍|Perfect|Perfeito|elogiar|Perfect, it fits you.|Perfeito, serve em você.
X: 🤔|Let me see|Deixe-me ver|pensar|Let me see the black one.|Deixe-me ver o preto.
X: 👍|Good choice|Boa escolha|elogiar|Good choice, Helen.|Boa escolha, Helen.

N: 7080233
C: Kiki,Osono | misshoney,tommy | No quarto da padaria, Kiki e Osono cuidam da roupa: do the laundry, fold, iron.
S: cuidar da roupa lavada: Do the laundry. Fold the shirt. Iron it
Y: Hoje você aprende a cuidar da roupa: do the laundry (lavar a roupa), fold (dobrar), iron (passar).
F: Kiki’s Delivery Service | 🎬 Animação | 1989 | uma animação do estúdio japonês Ghibli, dirigida por Hayao Miyazaki, sobre uma jovem bruxa que faz entregas de vassoura numa cidade | cuidar da roupa e das tarefas | bakery | 🧹,🧺,🥖
V: 🧺|laundry|roupa lavada|LÓN-dri
V: 👕|shirt|camisa|SHÂRT
V: 🧼|soap|sabão|SÔUP
V: 🌬️|clothesline|varal|KLÔUZ-láin
V: 🧸|apron|avental|ÊI-pron
V: 🧹|broom|vassoura|BRÚM
H: I do the laundry on Sunday.|Eu lavo a roupa no domingo.
H: Fold the shirt.|Dobre a camisa.
H: Iron the shirt after you wash it.|Passe a camisa depois de lavá-la.
H: Hang it on the clothesline.|Pendure no varal.
H: Put the apron in the basket.|Ponha o avental na cesta.
L: Osono, I do the laundry on Sunday.|Osono, eu lavo a roupa no domingo.
L: Good. Fold the shirt, Kiki.|Bom. Dobre a camisa, Kiki.
L: Okay. Do I use soap?|Certo. Eu uso sabão?
L: Yes, soap first. Hang it on the clothesline.|Sim, sabão primeiro. Pendure no varal.
L: Then iron the shirt after you wash it.|Depois passe a camisa depois de lavá-la.
L: Careful with the iron!|Cuidado com o ferro!
L: Put the apron in the basket.|Ponha o avental na cesta.
L: Done. Now I fly with my broom.|Pronto. Agora eu voo com a minha vassoura.
Q: When does Kiki do the laundry?|Quando a Kiki lava a roupa?|0|📅 On Sunday|📅 On Monday|📅 At night
Q: Where does Kiki hang the clothes?|Onde a Kiki pendura a roupa?|3|🌬️ On the clothesline|🧺 In the basket|🧹 On the broom
Q: What goes in the basket?|O que vai na cesta?|6|🧸 The apron|🧼 The soap|🌬️ The clothesline
B: wash|🧼|lavar|I wash the shirt.|She washes the shirt.|He washed the apron.|Ele lavou o avental.
B: hang|🌬️|pendurar|I hang the shirt.|She hangs the shirt.|They hung the laundry.|Eles penduraram a roupa.
B: dry|☀️|secar|I dry the apron.|She dries the apron.|It dried in the sun.|Secou ao sol.
B: carry|💪|carregar|I carry the basket.|She carries the basket.|He carried the laundry.|Ele carregou a roupa.
LAB: la|Laboratório de sons: laundry, shirt e soap|Laundry soa “LÓN-dri”. Shirt soa “SHÂRT”, com ir = âr. Soap soa “SÔUP”, com oa = ôu.|Em laundry, aun soa ón: LÓN-dri.
W: laundry|LÓN-dri|roupa lavada|aun = ón|laundromat|LÓN-dro-mét
W: shirt|SHÂRT|camisa|ir = âr|short|SHÓRT
W: soap|SÔUP|sabão|oa = ôu|soup|SÚP
G: 0|do the laundry|make the laundry|take the laundry
G: 1|Fold|Folds|Folding
G: 2|Iron|Irons|Ironing
G: 3|Hang|Hangs|Hanging
X: 😊|All clean|Tudo limpo|comemorar|All clean, Osono.|Tudo limpo, Osono.
X: 🔥|Be careful|Tenha cuidado|avisar|Be careful, the iron is hot.|Tenha cuidado, o ferro está quente.
X: 👍|Good job|Bom trabalho|elogiar|Good job, Kiki.|Bom trabalho, Kiki.
X: 🧹|Time to fly|Hora de voar|anunciar|Time to fly, Jiji!|Hora de voar, Jiji!

N: 7080235
C: Amir,Hassan | polly,tom | Numa colina ventosa, Amir e Hassan propõem empinar pipa: Shall we…? Why not?
S: propor um programa com Shall we…? e responder Why not?: Shall we fly a kite
Y: Hoje você aprende a propor com Shall we…? (Vamos…?) e a aceitar com Why not? (Por que não?). Shall we fly a kite?
F: The Kite Runner | 🎬 Filme | 2007 | um filme dirigido por Marc Forster, sobre dois meninos amigos que adoram empinar pipas | propor um passeio e aceitar | park | 🪁,🌬️,⛰️
V: 🪁|kite|pipa|KÁIT
V: 🌬️|wind|vento|UÍND
V: 🧵|string|linha|STRÍNG
V: ⛰️|hill|colina|RÍL
V: 🍉|picnic|piquenique|PÍK-nik
V: 🏃|race|corrida|RÊIS
H: Shall we fly a kite?|Vamos empinar uma pipa?
H: Why not? The wind is good.|Por que não? O vento está bom.
H: Shall we hold the string?|Vamos segurar a linha?
H: Shall we go up the hill?|Vamos subir a colina?
H: Shall we have a picnic?|Vamos fazer um piquenique?
L: Hassan, shall we fly a kite?|Hassan, vamos empinar uma pipa?
L: Why not? The wind is good.|Por que não? O vento está bom.
L: Shall we hold the string together?|Vamos segurar a linha juntos?
L: Why not? You hold it, I run.|Por que não? Você segura, eu corro.
L: Shall we go up the hill?|Vamos subir a colina?
L: Why not? There is more wind there.|Por que não? Tem mais vento lá.
L: Shall we have a picnic after the race?|Vamos fazer um piquenique depois da corrida?
L: Why not? I bring the watermelon.|Por que não? Eu levo a melancia.
Q: What do they want to fly?|O que eles querem empinar?|0|🪁 A kite|✈️ A plane|🎈 A balloon
Q: Where do they go?|Para onde eles vão?|4|⛰️ Up the hill|🏖️ To the beach|🏫 To school
Q: What do they have after the race?|O que eles fazem depois da corrida?|6|🍉 A picnic|📖 A lesson|🛌 A nap
B: fly|🪁|empinar|I fly a kite.|He flies a kite.|They flew it high.|Eles a empinaram alto.
B: run|🏃|correr|I run on the hill.|He runs on the hill.|She ran fast.|Ela correu rápido.
B: hold|🤲|segurar|I hold the string.|He holds the string.|We held it tight.|Nós a seguramos firme.
B: laugh|😂|rir|I laugh with Hassan.|He laughs with Amir.|They laughed a lot.|Eles riram muito.
LAB: ki|Laboratório de sons: kite, string e picnic|Kite soa “KÁIT”, com i = ái. String começa com str junto, “STRÍNG”. Picnic soa “PÍK-nik”.|Em kite, o i soa ái: KÁIT.
W: kite|KÁIT|pipa|i = ái|kit|KÍT
W: string|STRÍNG|linha|str junto|sing|SÍNG
W: picnic|PÍK-nik|piquenique|força no começo|panic|PÉ-nik
G: 0|Shall we|Do we|Are we
G: 1|Why not|Why no|What not
G: 2|Shall we|Do we|Are we
G: 3|Shall we|Do we|Are we
X: 😄|Let’s go|Vamos|animar|Let’s go, Hassan!|Vamos, Hassan!
X: 🪁|Look at it fly|Olhe como voa|admirar|Look at it fly, so high!|Olhe como voa, tão alto!
X: 🙌|For you|Para você|prometer|For you, a thousand times.|Para você, mil vezes.
X: 🌬️|What a wind|Que vento|comentar|What a wind today!|Que vento hoje!

N: 7080236
C: Manny,Sid | tom,tommy | Na geleira, Manny e Sid perguntam o que é permitido: allowed to, not allowed.
S: perguntar o que é permitido com allowed e not allowed: Are we allowed on the ice
Y: Hoje você aprende allowed (permitido) e not allowed (não permitido). Are we allowed on the ice? You are not allowed on the tree.
F: Ice Age | 🎬 Animação | 2002 | uma animação dirigida por Chris Wedge, sobre um mamute, uma preguiça e um tigre que levam um bebê pela era do gelo | perguntar o que se pode ou não fazer | lighthouse | 🧊,🦣,🦥
V: 🧊|ice|gelo|ÁIS
V: 🌳|tree|árvore|TRÍ
V: 🕳️|cave|caverna|KÊIV
V: ❄️|snow|neve|SNÔU
V: 🦣|mammoth|mamute|MÉ-mof
V: 👶|baby|bebê|BÊI-bi
H: Are we allowed on the ice?|Nós podemos ir no gelo?
H: You are not allowed on the tree.|Você não pode subir na árvore.
H: We are allowed in the cave.|Nós podemos ficar na caverna.
H: We are not allowed to slide on the snow.|Nós não podemos escorregar na neve.
H: Are we allowed to touch the mammoth?|Nós podemos tocar no mamute?
L: Manny, are we allowed on the ice?|Manny, nós podemos ir no gelo?
L: No, Sid. You are not allowed on the tree.|Não, Sid. Você não pode subir na árvore.
L: Then where are we allowed?|Então onde nós podemos?
L: We are allowed in the cave.|Nós podemos ficar na caverna.
L: And the snow? We are not allowed to slide on the snow.|E a neve? Nós não podemos escorregar na neve.
L: Are we allowed to touch the mammoth?|Nós podemos tocar no mamute?
L: No. Be gentle with the baby.|Não. Seja gentil com o bebê.
L: Okay. I just watch.|Certo. Eu só olho.
Q: Are they allowed on the ice?|Eles podem ir no gelo?|1|🧊 No, they aren’t|🧊 Yes, they are|🧊 Only Sid
Q: Where are they allowed?|Onde eles podem ficar?|3|🕳️ In the cave|🌳 On the tree|🧊 On the ice
Q: Who must they be gentle with?|Com quem eles devem ser gentis?|6|👶 The baby|🦣 The ice|🌳 The tree
B: slide|🛝|escorregar|I slide on the snow.|He slides on the snow.|They slid down.|Eles escorregaram.
B: climb|🧗|subir|I climb the tree.|He climbs the tree.|She climbed it fast.|Ela subiu rápido.
B: touch|✋|tocar|I touch the ice.|He touches the ice.|She touched the baby.|Ela tocou o bebê.
B: ask|❓|perguntar|I ask Manny.|He asks Manny.|They asked first.|Eles perguntaram primeiro.
LAB: ic|Laboratório de sons: ice, cave e mammoth|Ice soa “ÁIS”, com i = ái. Cave soa “KÊIV”. Mammoth termina com th soprado, “MÉ-mof”.|Em cave, o a soa êi: KÊIV.
W: ice|ÁIS|gelo|i = ái|ace|ÊIS
W: cave|KÊIV|caverna|a = êi|calf|KÉF
W: mammoth|MÉ-mof|mamute|th soprado|mammal|MÉ-mol
G: 0|allowed|allow|allows
G: 1|not allowed|no allowed|not allow
G: 2|allowed|allow|allows
G: 4|Are we|Do we|Is we
X: 😟|Careful|Cuidado|avisar|Careful, the ice is thin.|Cuidado, o gelo é fino.
X: 🙂|That’s the rule|Essa é a regra|explicar|That’s the rule, Sid.|Essa é a regra, Sid.
X: 😮|No way|De jeito nenhum|recusar|No way, it is cold.|De jeito nenhum, está frio.
X: 🤝|Stay together|Fiquem juntos|pedir|Stay together, everyone.|Fiquem juntos, pessoal.

N: 7910029
C: Hiro,Baymax | tom,tommy | Na oficina, Hiro e Baymax falam de dor: My … hurts. Where does it hurt?
S: dizer onde dói com My … hurts e Where does it hurt?: My knee hurts
Y: Hoje você aprende a dizer onde dói: My knee hurts. e a perguntar Where does it hurt?
F: Big Hero 6 | 🎬 Animação | 2014 | uma animação da Disney, dirigida por Don Hall e Chris Williams, sobre um menino e um robô enfermeiro que formam uma equipe de heróis | dizer onde dói | viaduct | 🤖,🩹,🦵
V: 🦵|knee|joelho|NÍ
V: 💪|elbow|cotovelo|ÉL-bô
V: 🦶|ankle|tornozelo|ÉN-kol
V: 🤕|head|cabeça|RÉD
V: 🩹|bandage|curativo|BÉN-didj
V: 🤖|nurse robot|robô enfermeiro|NÂRS-RÔU-bót
H: My knee hurts.|Meu joelho dói.
H: Where does it hurt?|Onde dói?
H: My ankle hurts a lot.|Meu tornozelo dói muito.
H: My head hurts.|Minha cabeça dói.
H: A bandage, and it hurts less.|Um curativo, e dói menos.
L: Baymax, my knee hurts.|Baymax, meu joelho dói.
L: Where does it hurt, Hiro?|Onde dói, Hiro?
L: My ankle hurts a lot, too.|Meu tornozelo dói muito também.
L: Does your head hurt?|Sua cabeça dói?
L: Yes, my head hurts.|Sim, minha cabeça dói.
L: I scan you. Take a bandage.|Eu escaneio você. Pegue um curativo.
L: A bandage, and it hurts less.|Um curativo, e dói menos.
L: I am satisfied with your care.|Estou satisfeito com o seu cuidado.
Q: What hurts first?|O que dói primeiro?|0|🦵 His knee|💪 His elbow|🤕 His head
Q: Does Hiro’s head hurt?|A cabeça do Hiro dói?|4|✅ Yes, it does|❌ No, it doesn’t|🤷 Maybe
Q: What helps?|O que ajuda?|6|🩹 A bandage|🦵 A knee|💪 An elbow
B: scan|🔍|escanear|I scan my knee.|He scans my knee.|It scanned my head.|Ele escaneou minha cabeça.
B: heal|💚|curar|I heal slowly.|He heals slowly.|The knee healed.|O joelho sarou.
B: hug|🤗|abraçar|I hug Baymax.|He hugs Hiro.|They hugged twice.|Eles se abraçaram duas vezes.
B: wait|⏳|esperar|I wait for Baymax.|He waits for Baymax.|She waited a minute.|Ela esperou um minuto.
LAB: kn|Laboratório de sons: knee, ankle e bandage|Em knee, o k é mudo: “NÍ”. Ankle soa “ÉN-kol”. Bandage termina em idj, “BÉN-didj”.|Em knee, o k não se fala: NÍ.
W: knee|NÍ|joelho|k mudo|key|KÍ
W: ankle|ÉN-kol|tornozelo|força no começo|uncle|ÂN-kol
W: bandage|BÉN-didj|curativo|age = idj|bondage|BÓN-didj
G: 0|hurts|hurt|hurting
G: 1|Where|What|Who
G: 2|hurts|hurt|hurting
G: 3|hurts|hurt|hurting
X: 😢|Ouch|Ai|reagir|Ouch, my knee!|Ai, meu joelho!
X: 🤖|Hello|Olá|cumprimentar|Hello, I am Baymax.|Olá, eu sou o Baymax.
X: 😊|I’m fine|Estou bem|tranquilizar|I’m fine, thank you.|Estou bem, obrigado.
X: 🩹|Feel better|Melhore|desejar|Feel better, Hiro.|Melhore, Hiro.

N: 7080238
C: Patch,Carin | tom,polly | Na farmácia, Patch e Carin leem a receita: once, twice, three times a day.
S: dizer quantas vezes com once, twice e three times a day: Take one tablet twice a day
Y: Hoje você aprende once (uma vez), twice (duas vezes) e three times (três vezes). Take one tablet twice a day.
F: Patch Adams | 🎬 Filme | 1998 | um filme dirigido por Tom Shadyac, sobre um estudante de medicina que usa humor para cuidar dos pacientes | ler a receita e dizer quantas vezes tomar | rainycafe | 💊,🩺,🧴
V: 💊|tablet|comprimido|TÉ-blit
V: 🧴|syrup|xarope|SÍ-rop
V: 📋|prescription|receita|pris-KRÍP-shan
V: 🧃|juice|água|DJÚS
V: 🩺|doctor|médico|DÓK-ter
V: 🏥|clinic|clínica|KLÍ-nik
H: Take one tablet twice a day.|Tome um comprimido duas vezes por dia.
H: Take the syrup three times a day.|Tome o xarope três vezes por dia.
H: Use the cream once a day.|Use o creme uma vez por dia.
H: Drink juice three times a day.|Beba água três vezes por dia.
H: See the doctor twice a year.|Veja o médico duas vezes por ano.
L: Carin, I go to the pharmacy.|Carin, eu vou à farmácia.
L: Here is the prescription, Patch.|Aqui está a receita, Patch.
L: Take one tablet twice a day.|Tome um comprimido duas vezes por dia.
L: And the syrup? Take the syrup three times a day.|E o xarope? Tome o xarope três vezes por dia.
L: Use the cream once a day.|Use o creme uma vez por dia.
L: Drink juice three times a day.|Beba água três vezes por dia.
L: See the doctor twice a year.|Veja o médico duas vezes por ano.
L: Thank you. I feel better already.|Obrigado. Eu já me sinto melhor.
Q: How often is the tablet?|Quantas vezes é o comprimido?|2|💊 Twice a day|💊 Once a day|💊 Three times a day
Q: How often is the syrup?|Quantas vezes é o xarope?|3|🧴 Three times a day|🧴 Once a day|🧴 Twice a day
Q: How often does Patch see the doctor?|Quantas vezes o Patch vê o médico?|6|🩺 Twice a year|🩺 Once a day|🩺 Three times a day
B: swallow|💊|engolir|I swallow a tablet.|He swallows a tablet.|She swallowed the syrup.|Ela engoliu o xarope.
B: count|🔢|contar|I count the tablets.|He counts the tablets.|They counted ten.|Eles contaram dez.
B: read|📖|ler|I read the prescription.|She reads the prescription.|He read it twice.|Ele a leu duas vezes.
B: ask|❓|perguntar|I ask the doctor.|He asks the doctor.|She asked about the tablet.|Ela perguntou sobre o comprimido.
LAB: pi|Laboratório de sons: tablet, syrup e prescription|Tablet soa “TÉ-blit”. Syrup soa “SÍ-rop”. Prescription tem a força no meio, “pris-KRÍP-shan”.|Em prescription, a força cai na segunda sílaba: pris-KRÍP-shan.
W: tablet|TÉ-blit|comprimido|a = é|table|TÊI-bol
W: syrup|SÍ-rop|xarope|y = í|sir|SÂR
W: prescription|pris-KRÍP-shan|receita|força no meio|description|dis-KRÍP-shan
G: 0|twice|two|second
G: 1|three times|three time|three timing
G: 2|once|one|first
G: 3|three times|three time|three timing
X: 😷|Get well|Melhore|desejar|Get well, Patch.|Melhore, Patch.
X: 😂|Laugh|Ria|animar|Laugh, it helps!|Ria, isso ajuda!
X: 🙏|Thank you|Obrigado|agradecer|Thank you, Carin.|Obrigado, Carin.
X: ⏰|Don’t forget|Não esqueça|lembrar|Don’t forget the tablet.|Não esqueça o comprimido.

N: 7080239
C: Auggie,Via | tommy,polly | No quarto, Auggie e Via desejam melhoras: get well soon, feel better.
S: desejar melhoras: Get well soon! Feel better
Y: Hoje você aprende a desejar melhoras: Get well soon! (Melhoras!) e Feel better! (Sinta-se melhor!). I made a card for you.
F: Wonder | 🎬 Filme | 2017 | um filme dirigido por Stephen Chbosky, sobre um menino que começa numa escola nova e conquista os colegas | desejar melhoras a quem está doente | bakery | 💌,💐,🧸
V: 💌|card|cartão|KÁRD
V: 💐|flowers|flores|FLÁU-erz
V: 🍲|soup|sopa|SÚP
V: 🧸|teddy bear|urso de pelúcia|TÉ-di-bér
V: 🛏️|bed|cama|BÉD
V: 🤒|fever|febre|FÍ-ver
H: I made a card. Get well soon!|Eu fiz um cartão. Melhoras!
H: These flowers are for you. Feel better!|Estas flores são para você. Melhoras!
H: I brought you soup. Get well soon!|Eu trouxe sopa para você. Melhoras!
H: Hug the teddy bear and feel better.|Abrace o urso de pelúcia e melhore.
H: Rest in bed. Get well soon!|Descanse na cama. Melhoras!
L: Via, I made a card. Get well soon!|Via, eu fiz um cartão. Melhoras!
L: Thank you, Auggie. It is so nice.|Obrigada, Auggie. É tão bonito.
L: These flowers are for you. Feel better!|Estas flores são para você. Melhoras!
L: I brought you soup. Get well soon!|Eu trouxe sopa para você. Melhoras!
L: Hug the teddy bear and feel better.|Abrace o urso de pelúcia e melhore.
L: Rest in bed. Your fever is high.|Descanse na cama. Sua febre está alta.
L: Rest in bed. Get well soon!|Descanse na cama. Melhoras!
L: I feel better already. Thank you.|Eu já me sinto melhor. Obrigada.
Q: What does Auggie make?|O que o Auggie faz?|0|💌 A card|💐 Flowers|🍲 Soup
Q: What does Auggie bring?|O que o Auggie traz?|3|🍲 Soup|🛏️ A bed|🤒 A fever
Q: Where does Via rest?|Onde a Via descansa?|6|🛏️ In bed|🍲 In the soup|💐 In the flowers
B: make|✂️|fazer|I make a card.|He makes a card.|She made a drawing.|Ela fez um desenho.
B: bring|🎁|trazer|I bring soup.|He brings soup.|They brought flowers.|Eles trouxeram flores.
B: wish|🌟|desejar|I wish you well.|He wishes you well.|She wished me luck.|Ela me desejou sorte.
B: hug|🤗|abraçar|I hug the teddy bear.|He hugs the teddy bear.|They hugged Via.|Eles abraçaram a Via.
LAB: ca|Laboratório de sons: card, soup e fever|Card soa “KÁRD”. Soup tem u longo, “SÚP”. Fever soa “FÍ-ver”, com e = í.|Em fever, o e soa í: FÍ-ver.
W: card|KÁRD|cartão|a aberto|cord|KÓRD
W: soup|SÚP|sopa|ou = ú|soap|SÔUP
W: fever|FÍ-ver|febre|e = í|fiver|FÁI-ver
G: 0|Get well soon|Get good soon|Be well soon
G: 1|Feel better|Feel more good|Feel best
G: 2|Get well soon|Get good soon|Be well soon
G: 3|feel better|feel more good|feel best
X: 🤗|Take care|Cuide-se|despedir-se|Take care, Via.|Cuide-se, Via.
X: 💪|You can do it|Você consegue|animar|You can do it, Via.|Você consegue, Via.
X: 😊|I miss you|Sinto sua falta|carinho|I miss you at school.|Sinto sua falta na escola.
X: 🌟|See you soon|Até logo|despedir-se|See you soon, Via.|Até logo, Via.

N: 7080240
C: Miss Price,Charlie | misshoney,tommy | Numa casa de campo, a Srta. Price e Charlie distinguem doenças: a cold, the flu, a fever.
S: diferenciar doenças com a cold, the flu e a fever: It is a cold. It looks like the flu
Y: Hoje você aprende a falar de doenças: a cold (um resfriado), the flu (a gripe), a fever (uma febre).
F: Bedknobs and Broomsticks | 🎬 Filme | 1971 | um filme musical dirigido por Robert Stevenson, sobre uma aprendiz de bruxa que cuida de três crianças numa casa de campo | falar de resfriado, gripe e febre | castle | 🛏️,🧹,🤧
V: 🤧|cold|resfriado|KÔULD
V: 🤒|flu|gripe|FLÚ
V: 🌡️|fever|febre|FÍ-ver
V: 🍵|tea|chá|TÍ
V: 🛌|blanket|cobertor|BLÉN-kit
V: 🧣|scarf|cachecol|SKÁRF
H: It is only a cold.|É só um resfriado.
H: It looks like the flu.|Parece gripe.
H: He has a fever.|Ele está com febre.
H: Drink hot tea. It is a cold.|Beba chá quente. É um resfriado.
H: Stay in bed under the blanket.|Fique na cama debaixo do cobertor.
L: Miss Price, Charlie is sick.|Srta. Price, o Charlie está doente.
L: Is it a cold or the flu?|É um resfriado ou gripe?
L: It is only a cold.|É só um resfriado.
L: No. It looks like the flu.|Não. Parece gripe.
L: He has a fever, too.|Ele está com febre também.
L: Drink hot tea. Use a scarf.|Beba chá quente. Use um cachecol.
L: Stay in bed under the blanket.|Fique na cama debaixo do cobertor.
L: Thank you. I feel better soon.|Obrigado. Eu me sinto melhor logo.
Q: What is it first?|O que é, a princípio?|2|🤧 A cold|🤒 The flu|🌡️ A fever
Q: What does it look like later?|Com o que se parece depois?|3|🤒 The flu|🤧 A cold|🍵 Tea
Q: What does Charlie drink?|O que o Charlie bebe?|5|🍵 Hot tea|🤧 Milk|🌡️ Water
B: measure|📏|medir|I measure the fever.|She measures the fever.|He measured it twice.|Ele a mediu duas vezes.
B: shiver|🥶|tremer|I shiver in bed.|He shivers in bed.|She shivered all night.|Ela tremeu a noite toda.
B: rest|🛌|descansar|I rest in bed.|He rests in bed.|They rested all day.|Eles descansaram o dia todo.
B: drink|🥤|beber|I drink hot tea.|He drinks hot tea.|They drank a lot.|Eles beberam muito.
LAB: co|Laboratório de sons: cold, flu e fever|Cold soa “KÔULD”, com o = ôu. Flu soa “FLÚ”. Fever soa “FÍ-ver”.|Em cold, o o soa ôu: KÔULD.
W: cold|KÔULD|resfriado|o = ôu|called|KÓLD
W: flu|FLÚ|gripe|u = ú|flew|FLÚ
W: fever|FÍ-ver|febre|e = í|feather|FÉ-der
G: 0|a cold|the cold|an cold
G: 1|the flu|a flu|the flus
G: 2|a fever|the fever|an fever
G: 3|a cold|the cold|an cold
X: 😷|Poor Charlie|Pobre Charlie|ter pena|Poor Charlie, he is sick.|Pobre Charlie, ele está doente.
X: 🍵|Drink up|Beba tudo|pedir|Drink up, it is good.|Beba tudo, faz bem.
X: 😴|Get some rest|Descanse um pouco|aconselhar|Get some rest, Charlie.|Descanse um pouco, Charlie.
X: 🌟|Magic words|Palavras mágicas|brincar|Magic words, and you feel fine.|Palavras mágicas, e você fica bem.

N: 7080241
C: Seymour,Audrey | tom,polly | No consultório, Seymour e Audrey vão ao dentista: a toothache, open wide.
S: ir ao dentista com a toothache e open wide: I have a toothache. Open wide
Y: Hoje você aprende a falar do dentista: a toothache (dor de dente) e Open wide (abra bem a boca).
F: Little Shop of Horrors | 🎬 Musical | 1986 | um filme musical dirigido por Frank Oz, sobre um florista tímido e sua planta que cresce demais | falar de dor de dente e dentista | cave | 🦷,🌱,🪥
V: 🦷|tooth|dente|TÚF
V: 🧑‍⚕️|dentist|dentista|DÉN-tist
V: 👄|mouth|boca|MÁUF
V: 🪥|toothbrush|escova de dente|TÚF-brâsh
V: 🌱|plant|planta|PLÉNT
V: 💺|chair|cadeira|TCHÉR
H: I have a toothache.|Eu estou com dor de dente.
H: Open wide, please.|Abra bem a boca, por favor.
H: Open your mouth wide.|Abra bem a sua boca.
H: Brush your teeth after dinner.|Escove os dentes depois do jantar.
H: The plant is hungry. Open wide!|A planta está com fome. Abra bem!
L: Audrey, I have a toothache.|Audrey, eu estou com dor de dente.
L: Sit in the chair, Seymour.|Sente na cadeira, Seymour.
L: The dentist says: open wide, please.|O dentista diz: abra bem a boca, por favor.
L: Open your mouth wide.|Abra bem a sua boca.
L: Ah! It hurts. Is the tooth bad?|Ah! Dói. O dente está ruim?
L: Brush your teeth after dinner.|Escove os dentes depois do jantar.
L: Yes. Use a good toothbrush.|Sim. Use uma boa escova de dente.
L: The plant is hungry. Open wide!|A planta está com fome. Abra bem!
Q: What does Seymour have?|O que o Seymour tem?|0|🦷 A toothache|🌱 A plant|🪥 A brush
Q: What does the dentist say?|O que o dentista diz?|2|👄 Open wide|🪥 Brush more|🌱 Feed me
Q: When must he brush his teeth?|Quando ele deve escovar os dentes?|5|🍽️ After dinner|🌅 Never|🌙 Before school
B: open|👄|abrir|I open my mouth.|He opens his mouth.|She opened wide.|Ela abriu bem.
B: brush|🪥|escovar|I brush my teeth.|He brushes his teeth.|They brushed twice.|Eles escovaram duas vezes.
B: sit|🪑|sentar|I sit in the chair.|He sits in the chair.|She sat down.|Ela sentou.
B: rinse|💧|enxaguar|I rinse my mouth.|He rinses his mouth.|We rinsed with water.|Nós enxaguamos com água.
LAB: to|Laboratório de sons: tooth, mouth e chair|Tooth e mouth terminam em th soprado, “TÚF” e “MÁUF”. Chair começa com tch, “TCHÉR”.|Em tooth, o th final é soprado: TÚF.
W: tooth|TÚF|dente|th soprado|toot|TÚT
W: mouth|MÁUF|boca|th soprado|mouse|MÁUS
W: chair|TCHÉR|cadeira|ch = tch|share|SHÉR
G: 0|a toothache|an toothache|toothaches
G: 1|Open wide|Open big|Open wild
G: 2|wide|wild|width
G: 3|Brush|Brushes|Brushing
X: 😖|Ouch|Ai|reagir|Ouch, my tooth!|Ai, meu dente!
X: 😬|Don’t worry|Não se preocupe|acalmar|Don’t worry, it is quick.|Não se preocupe, é rápido.
X: 😊|All done|Tudo pronto|terminar|All done, Seymour.|Tudo pronto, Seymour.
X: 🌱|Feed me|Alimente-me|imitar|Feed me, said the plant.|Alimente-me, disse a planta.

N: 80243
C: Luca,Alberto | tom,tommy | Na vila à beira-mar, Luca e Alberto organizam a mudança: move in, move out, pack.
S: falar de mudança com move in, move out e pack: Pack the boxes. We move in tomorrow
Y: Hoje você aprende a falar de mudança: pack (arrumar as malas), move out (sair da casa) e move in (entrar na casa).
F: Luca | 🎬 Animação | 2021 | uma animação da Pixar, dirigida por Enrico Casarosa, sobre dois amigos que passam o verão numa vila italiana à beira-mar | falar de mudança | lighthouse | 📦,🛵,🏠
V: 📦|boxes|caixas|BÓK-siz
V: 🚚|truck|caminhão|TRÂK
V: 🏠|house|casa|RÁUS
V: 📎|tape|fita|TÊIP
V: 🛵|scooter|lambreta|SKÚ-ter
V: 🌊|sea|mar|SÍ
H: Pack the boxes.|Arrume as caixas.
H: We move out today.|Nós saímos da casa hoje.
H: We move in tomorrow.|Nós entramos na casa amanhã.
H: Pack the tape in the box.|Ponha a fita na caixa.
H: Pack my scooter, too.|Guarde minha lambreta também.
L: Alberto, pack the boxes.|Alberto, arrume as caixas.
L: Okay, Luca. We move out today.|Certo, Luca. Nós saímos da casa hoje.
L: The truck is here. Where do we go?|O caminhão está aqui. Para onde vamos?
L: We move in tomorrow. The house is by the sea.|Nós entramos na casa amanhã. A casa é perto do mar.
L: Pack the tape in the box.|Ponha a fita na caixa.
L: Pack my scooter, too.|Guarde minha lambreta também.
L: Done. Load the truck, Alberto.|Pronto. Carregue o caminhão, Alberto.
L: Ready! Our new house, here we come.|Pronto! Nossa casa nova, aí vamos nós.
Q: What do they pack?|O que eles arrumam?|0|📦 The boxes|🌊 The sea|🏠 The house
Q: When do they move in?|Quando eles entram na casa?|3|📅 Tomorrow|📅 Today|📅 Yesterday
Q: What do they pack last?|O que eles guardam por último?|5|🛵 The scooter|📎 The tape|📦 The boxes
B: carry|💪|carregar|I carry the boxes.|He carries the boxes.|They carried the scooter.|Eles carregaram a lambreta.
B: load|🚚|carregar (veículo)|I load the truck.|He loads the truck.|We loaded it fast.|Nós o carregamos rápido.
B: tape|📎|colar com fita|I tape the box.|He tapes the box.|She taped it twice.|Ela o colou com fita duas vezes.
B: close|🚪|fechar|I close the door.|He closes the door.|They closed the box.|Eles fecharam a caixa.
LAB: bo|Laboratório de sons: boxes, truck e scooter|Boxes soa “BÓK-siz”. Truck soa “TRÂK”, com u = â. Scooter tem u longo, “SKÚ-ter”.|Em truck, o u soa â: TRÂK.
W: boxes|BÓK-siz|caixas|es = iz|bosses|BÓ-siz
W: truck|TRÂK|caminhão|u = â|track|TRÉK
W: scooter|SKÚ-ter|lambreta|oo = ú|skater|SKÊI-der
G: 0|Pack|Packs|Packing
G: 1|move out|move off|move up
G: 2|move in|move on|move up
G: 3|Pack|Packs|Packing
X: 🎉|Let’s go|Vamos|animar|Let’s go, Alberto!|Vamos, Alberto!
X: 😊|New home|Casa nova|comemorar|New home, new friends.|Casa nova, amigos novos.
X: 😮|So many boxes|Tantas caixas|comentar|So many boxes today!|Tantas caixas hoje!
X: 🙌|All set|Tudo pronto|avisar|All set, Luca.|Tudo pronto, Luca.

N: 7080243
C: Hercules,Phil | tommy,tom | No pátio de treino, Hercules e Phil levantam e carregam coisas: lift, carry, drop.
S: mover coisas pesadas com lift, carry e drop: I can lift the rock. Don’t drop the vase
Y: Hoje você aprende lift (levantar), carry (carregar) e drop (deixar cair). I can lift the rock. Don’t drop the vase!
F: Hercules | 🎬 Animação | 1997 | uma animação da Disney, dirigida por Ron Clements e John Musker, sobre um jovem muito forte que treina para ser um herói | falar de levantar e carregar coisas pesadas | castle | 💪,🏛️,🪨
V: 🪨|rock|pedra|RÓK
V: 🪑|chair|cadeira|TCHÉR
V: 🏺|vase|vaso|VÊIS
V: 🏋️|weight|peso|UÊIT
V: 🗿|statue|estátua|STÉ-tchu
V: 🪢|rope|corda|RÔUP
H: I can lift the rock.|Eu consigo levantar a pedra.
H: We carry the chair.|Nós carregamos a cadeira.
H: Don’t drop the vase!|Não deixe o vaso cair!
H: Lift it together.|Levantem juntos.
H: Carry the statue with the rope.|Carregue a estátua com a corda.
L: Phil, I can lift the rock.|Phil, eu consigo levantar a pedra.
L: Good. Now we carry the chair.|Bom. Agora nós carregamos a cadeira.
L: Easy. What about the vase?|Fácil. E o vaso?
L: Don’t drop the vase!|Não deixe o vaso cair!
L: Okay. The weight is heavy.|Certo. O peso é pesado.
L: Lift it together, Hercules.|Levantem juntos, Hércules.
L: Carry the statue with the rope.|Carregue a estátua com a corda.
L: Done. You are a real hero.|Pronto. Você é um herói de verdade.
Q: What can Hercules lift?|O que o Hércules consegue levantar?|0|🪨 The rock|🏺 The vase|🗿 The statue
Q: What must he not drop?|O que ele não deve deixar cair?|3|🏺 The vase|🪑 The chair|🪨 The rock
Q: What do they carry with the rope?|O que eles carregam com a corda?|6|🗿 The statue|🪑 The chair|🏋️ The weight
B: lift|🏋️|levantar|I lift the rock.|He lifts the rock.|She lifted the chair.|Ela levantou a cadeira.
B: drag|🪢|arrastar|I drag the rope.|He drags the rope.|They dragged the statue.|Eles arrastaram a estátua.
B: push|➡️|empurrar|I push the rock.|He pushes the rock.|We pushed it together.|Nós o empurramos juntos.
B: train|🏃|treinar|I train every day.|He trains every day.|They trained all week.|Eles treinaram a semana toda.
LAB: ro|Laboratório de sons: rock, weight e statue|Rock soa “RÓK”. Weight soa “UÊIT”, com eigh = êi. Statue soa “STÉ-tchu”.|Em weight, o gh não se fala: UÊIT.
W: rock|RÓK|pedra|o aberto|rack|RÉK
W: weight|UÊIT|peso|eigh = êi|wait|UÊIT
W: statue|STÉ-tchu|estátua|tu = tchu|state|STÊIT
G: 0|lift|lifts|lifting
G: 1|carry|carries|carrying
G: 2|drop|drops|dropping
G: 3|Lift|Lifts|Lifting
X: 💪|So strong|Tão forte|elogiar|So strong, Hercules!|Tão forte, Hércules!
X: 😮|Careful|Cuidado|avisar|Careful, it is heavy.|Cuidado, é pesado.
X: 🤝|Together|Juntos|animar|Together, on three.|Juntos, no três.
X: 🏆|Hero|Herói|elogiar|Hero of the day!|Herói do dia!

N: 7910030
C: Tarzan,Jane | tom,polly | Na selva, Tarzan e Jane montam a casa da árvore: put together, set up.
S: montar com put together e set up: We put together the treehouse. We set up the bed
Y: Hoje você aprende put together (montar) e set up (armar). We put together the treehouse. We set up the bed.
F: Tarzan | 🎬 Animação | 1999 | uma animação da Disney, dirigida por Chris Buck e Kevin Lima, sobre um homem criado na selva que conhece uma exploradora | montar e armar coisas | jungle | 🌴,🔨,🏠
V: 🏠|treehouse|casa da árvore|TRÍ-ráus
V: 🪵|wood|madeira|UÚD
V: 🔨|hammer|martelo|RÉ-mer
V: 🔩|screws|parafusos|SKRÚZ
V: 📖|plan|plano|PLÉN
V: 🪢|vines|cipós|VÁINZ
H: We put together the treehouse.|Nós montamos a casa da árvore.
H: We set up the wood here.|Nós arrumamos a madeira aqui.
H: Where is the hammer?|Onde está o martelo?
H: Where are the screws?|Onde estão os parafusos?
H: Read the plan, then put it together.|Leia o plano e depois monte.
L: Jane, we put together the treehouse.|Jane, nós montamos a casa da árvore.
L: Good. We set up the wood here.|Bom. Nós arrumamos a madeira aqui.
L: Where is the hammer?|Onde está o martelo?
L: It is on the branch. Where are the screws?|Está no galho. Onde estão os parafusos?
L: In the bag. Read the plan, then put it together.|Na sacola. Leia o plano e depois monte.
L: Use the vines to tie the wood.|Use os cipós para amarrar a madeira.
L: Perfect. We set up the bed next.|Perfeito. Nós armamos a cama depois.
L: Our treehouse is ready, Jane.|Nossa casa da árvore está pronta, Jane.
Q: What do they put together?|O que eles montam?|0|🏠 The treehouse|🔨 The hammer|📖 The plan
Q: Where is the hammer?|Onde está o martelo?|3|🌿 On the branch|🎒 In the bag|🏠 In the house
Q: What do they use to tie the wood?|O que eles usam para amarrar a madeira?|5|🪢 The vines|🔩 The screws|📖 The plan
B: build|🏗️|construir|I build a treehouse.|He builds a treehouse.|They built a bed.|Eles construíram uma cama.
B: tie|🪢|amarrar|I tie the wood.|She ties the wood.|He tied the vines.|Ele amarrou os cipós.
B: swing|🌿|balançar|I swing on a vine.|He swings on a vine.|We swung together.|Nós nos balançamos juntos.
B: read|📖|ler|I read the plan.|She reads the plan.|They read it twice.|Eles o leram duas vezes.
LAB: tr|Laboratório de sons: treehouse, hammer e screws|Treehouse junta tree e house, “TRÍ-ráus”. Hammer soa “RÉ-mer”, com h soprado. Screws começa com skr, “SKRÚZ”.|Em screws, junte s, k e r: SKRÚZ.
W: treehouse|TRÍ-ráus|casa da árvore|tree + house|three|THRÍ
W: hammer|RÉ-mer|martelo|h soprado|hamster|RÉM-ster
W: screws|SKRÚZ|parafusos|skr junto|screens|SKRÍNZ
G: 0|put together|put up|put in
G: 1|set up|set on|set in
G: 2|Where|What|Who
G: 4|put it together|put together it|put up it
X: 😄|Well done|Muito bem|elogiar|Well done, Tarzan.|Muito bem, Tarzan.
X: 🌴|Hold on|Segure firme|avisar|Hold on to the vine.|Segure firme no cipó.
X: 🙌|Almost ready|Quase pronto|avisar|Almost ready, Jane.|Quase pronto, Jane.
X: 😊|Come and see|Venha ver|chamar|Come and see our house.|Venha ver a nossa casa.
''')
