# Lote B (cinema), dados 7: episódios A1 7080219 .. 7080228. Formato: ver zz_b_lib.py.
from v3.zz_b_lib import add

add('''
N: 7080219
C: Kris,Susan | tommy,polly | Numa rua de Nova York, Kris e Susan dizem onde fica cada loja: up the street, down the street.
S: dizer para onde na rua: The shop is up the street. The bakery is down the street
Y: Hoje você aprende a situar na rua: up the street (adiante, subindo) e down the street (mais adiante, descendo). The shop is up the street.
F: Miracle on 34th Street | 🎬 Filme | 1947 | um filme dirigido por George Seaton, sobre um senhor que diz ser o Papai Noel e conquista uma menina numa loja de departamentos | dizer onde as coisas ficam na rua | viaduct | 🏪,🎄,🚦
V: 🏪|shop|loja|SHÓP
V: 🥖|bakery|padaria|BÊI-ke-ri
V: 🏫|school|escola|SKÚL
V: ⛰️|hill|ladeira|RÍL
V: 🚦|light|semáforo|LÁIT
V: 🎄|tree|árvore|TRÍ
H: The shop is up the street.|A loja fica rua acima.
H: The bakery is down the street.|A padaria fica rua abaixo.
H: The school is over there.|A escola fica ali.
H: Walk up the hill.|Suba a ladeira.
H: Turn left, then go down the street.|Vire à esquerda e desça a rua.
L: Susan, where is the shop?|Susan, onde fica a loja?
L: The shop is up the street, Kris.|A loja fica rua acima, Kris.
L: And the bakery?|E a padaria?
L: The bakery is down the street.|A padaria fica rua abaixo.
L: Is the school near?|A escola fica perto?
L: The school is over there. Walk up the hill.|A escola fica ali. Suba a ladeira.
L: Stop at the light. Then go down the street.|Pare no semáforo. Depois desça a rua.
L: Thank you. I see a big tree there!|Obrigado. Eu vejo uma árvore grande ali!
Q: Where is the shop?|Onde fica a loja?|1|🏪 Up the street|🥖 Down the street|🏫 Over there
Q: Where is the bakery?|Onde fica a padaria?|3|🥖 Down the street|🏪 Up the street|⛰️ On the hill
Q: Where do they stop?|Onde eles param?|6|🚦 At the light|🏫 At the school|🎄 At the tree
B: look|👀|olhar|I look up the street.|She looks up the street.|He looked at the shop.|Ele olhou a loja.
B: wait|⏳|esperar|I wait at the light.|She waits at the light.|We waited a minute.|Nós esperamos um minuto.
B: point|👉|apontar|I point at the shop.|She points at the shop.|He pointed down the street.|Ele apontou rua abaixo.
B: turn|↩️|virar|I turn left.|She turns left.|They turned at the school.|Eles viraram na escola.
LAB: sh|Laboratório de sons: shop, bakery e light|Shop soa “SHÓP”. Bakery soa “BÊI-ke-ri”. Light termina em t, “LÁIT”, com gh mudo.|Em light, o gh não se fala: LÁIT.
W: shop|SHÓP|loja|sh|ship|SHÍP
W: bakery|BÊI-ke-ri|padaria|a = êi|bacon|BÊI-kon
W: light|LÁIT|semáforo|gh mudo|late|LÊIT
G: 0|up|down|under
G: 1|down|up|under
G: 2|over there|over here|under there
G: 4|down|up|under
X: 😊|Over here|Por aqui|chamar|Over here, Susan!|Por aqui, Susan!
X: 🎄|Merry Christmas|Feliz Natal|desejar|Merry Christmas, Kris.|Feliz Natal, Kris.
X: 👍|Thanks a lot|Muito obrigado|agradecer|Thanks a lot, Susan.|Muito obrigado, Susan.
X: 🚶|Not far|Não é longe|tranquilizar|Not far, just walk.|Não é longe, é só andar.

N: 80220
C: Tony,Maria | tom,polly | Numa praça de Nova York, Tony e Maria combinam onde se encontrar: on the corner, by the fountain.
S: combinar o ponto de encontro: I am on the corner. Meet me by the fountain
Y: Hoje você aprende a combinar o encontro: on the corner (na esquina) e by the fountain (junto da fonte). Meet me by the fountain.
F: West Side Story | 🎬 Musical | 1961 | um filme musical dirigido por Robert Wise e Jerome Robbins, sobre dois jovens que se apaixonam em Nova York | combinar onde se encontrar | rainycafe | ⛲,🌹,🎶
V: 📍|corner|esquina|KÓR-ner
V: ⛲|fountain|fonte|FÁUN-tn
V: 🪑|bench|banco|BÉNTCH
V: 🌉|bridge|ponte|BRÍDJ
V: 🌹|flower|flor|FLÁU-er
V: 🎶|song|canção|SÓNG
H: I am on the corner.|Eu estou na esquina.
H: Meet me by the fountain.|Encontre-me junto da fonte.
H: Wait on the bench.|Espere no banco.
H: See you by the bridge.|Até a ponte.
H: I bring a flower and a song.|Eu levo uma flor e uma canção.
L: Maria, I am on the corner.|Maria, eu estou na esquina.
L: Meet me by the fountain, Tony.|Encontre-me junto da fonte, Tony.
L: Okay. Where do I wait?|Certo. Onde eu espero?
L: Wait on the bench.|Espere no banco.
L: And tomorrow? See you by the bridge.|E amanhã? Até a ponte.
L: Good. I bring a flower and a song.|Bom. Eu levo uma flor e uma canção.
L: Sing it for me by the fountain.|Cante para mim junto da fonte.
L: With pleasure. Tonight!|Com prazer. Hoje à noite!
Q: Where is Tony first?|Onde o Tony está primeiro?|0|📍 On the corner|⛲ By the fountain|🌉 By the bridge
Q: Where does Tony wait?|Onde o Tony espera?|3|🪑 On the bench|⛲ In the fountain|🌉 On the bridge
Q: What does Tony bring?|O que o Tony leva?|5|🌹 A flower and a song|🪑 A bench|⛲ A fountain
B: sing|🎤|cantar|I sing a song.|He sings a song.|She sang by the fountain.|Ela cantou junto da fonte.
B: dance|💃|dançar|I dance on the corner.|He dances on the corner.|They danced all night.|Eles dançaram a noite toda.
B: wave|👋|acenar|I wave at Maria.|He waves at Maria.|She waved from the bridge.|Ela acenou da ponte.
B: hurry|🏃|apressar-se|I hurry to the bridge.|He hurries to the bridge.|We hurried home.|Nós corremos para casa.
LAB: co|Laboratório de sons: corner, fountain e bench|Corner soa “KÓR-ner”. Fountain soa “FÁUN-tn”. Bench termina em tch, “BÉNTCH”.|Em fountain, ou soa áu: FÁUN-tn.
W: corner|KÓR-ner|esquina|or = ór|corn|KÓRN
W: fountain|FÁUN-tn|fonte|ou = áu|mountain|MÁUN-tn
W: bench|BÉNTCH|banco|ch = tch|bunch|BÂNTCH
G: 0|on|in|at
G: 1|by|in|to
G: 2|on|in|by
G: 3|by|in|to
X: 😍|My love|Meu amor|carinho|My love, I am here.|Meu amor, estou aqui.
X: 🎶|Sing for me|Cante para mim|pedir|Sing for me, Tony.|Cante para mim, Tony.
X: 🌙|Tonight|Hoje à noite|marcar|Tonight, by the fountain.|Hoje à noite, junto da fonte.
X: 😊|See you soon|Até logo|despedir-se|See you soon, Maria.|Até logo, Maria.

N: 7080220
C: Baxter,Fran | tom,misshoney | Num prédio de escritórios, Baxter e Fran dizem em que andar fica cada coisa: upstairs, downstairs.
S: dizer em que andar: Go upstairs. The elevator is downstairs. It is on the second floor
Y: Hoje você aprende upstairs (lá em cima), downstairs (lá embaixo) e on the first/second floor (no primeiro/segundo andar).
F: The Apartment | 🎬 Filme | 1960 | um filme dirigido por Billy Wilder, sobre um funcionário de uma empresa grande e uma ascensorista que se tornam amigos | dizer em que andar fica cada coisa | library | 🏢,🛗,🔑
V: 🪜|stairs|escada|STÉRZ
V: 🛗|elevator|elevador|ÉL-e-vei-ter
V: 🚪|door|porta|DÓR
V: 🏢|building|prédio|BÍL-ding
V: 🔑|key|chave|KÍ
V: 🍸|party|festa|PÁR-ti
H: Take the stairs upstairs.|Pegue a escada para cima.
H: The elevator is downstairs.|O elevador está lá embaixo.
H: My door is on the second floor.|Minha porta fica no segundo andar.
H: The party is on the first floor.|A festa é no primeiro andar.
H: Go downstairs with the key.|Desça com a chave.
L: Fran, where is your office?|Fran, onde fica o seu escritório?
L: It is upstairs. Take the stairs upstairs.|Fica lá em cima. Pegue a escada para cima.
L: Where is the elevator?|Onde fica o elevador?
L: The elevator is downstairs.|O elevador está lá embaixo.
L: And your door, Baxter?|E a sua porta, Baxter?
L: My door is on the second floor.|Minha porta fica no segundo andar.
L: The party is on the first floor.|A festa é no primeiro andar.
L: Then go downstairs with the key.|Então desça com a chave.
Q: Where is Fran’s office?|Onde fica o escritório da Fran?|1|🪜 Upstairs|🛗 Downstairs|🍸 On the first floor
Q: Where is the elevator?|Onde fica o elevador?|3|🛗 Downstairs|🪜 Upstairs|🚪 On the second floor
Q: Where is the party?|Onde é a festa?|6|🍸 On the first floor|🚪 On the second floor|🛗 Upstairs
B: climb|🧗|subir|I climb the stairs.|She climbs the stairs.|He climbed to the office.|Ele subiu até o escritório.
B: press|🔘|apertar|I press the button.|She presses the button.|They pressed floor two.|Eles apertaram o andar dois.
B: knock|✊|bater à porta|I knock on the door.|He knocks on the door.|She knocked twice.|Ela bateu duas vezes.
B: carry|💪|carregar|I carry the key.|He carries the key.|She carried a box.|Ela carregou uma caixa.
LAB: st|Laboratório de sons: stairs, building e party|Stairs soa “STÉRZ”. Building tem u mudo, “BÍL-ding”. Party soa “PÁR-ti”.|Em building, o u não se fala: BÍL-ding.
W: stairs|STÉRZ|escada|ai = é|stars|STÁRZ
W: building|BÍL-ding|prédio|u mudo|billing|BÍ-ling
W: party|PÁR-ti|festa|a aberto|pretty|PRÍ-ti
G: 0|upstairs|up stairs|upstair
G: 1|downstairs|down stairs|downstair
G: 2|on|in|at
G: 3|on|in|at
X: 😊|After you|Depois de você|ceder a vez|After you, Fran.|Depois de você, Fran.
X: 🛗|Going up|Subindo|avisar|Going up, please.|Subindo, por favor.
X: 😮|Watch your step|Cuidado com o degrau|avisar|Watch your step, the stairs!|Cuidado com o degrau, a escada!
X: 🍸|Cheers|Saúde|brindar|Cheers, Baxter!|Saúde, Baxter!

N: 7910027
C: Gordie,Chris | tommy,tom | Numa noite de acampamento, Gordie e Chris combinam dormir juntos: come over, stay over.
S: convidar para ir à casa e dormir lá: Come over tonight. Can you stay over
Y: Hoje você aprende come over (aparecer na casa de alguém) e stay over (dormir lá). Come over tonight. Can you stay over?
F: Stand by Me | 🎬 Filme | 1986 | um filme dirigido por Rob Reiner, sobre quatro amigos que fazem uma caminhada de um fim de semana | convidar um amigo para ir e dormir em casa | cave | ⛺,🔦,🌙
V: ⛺|tent|barraca|TÉNT
V: 🔦|flashlight|lanterna|FLÉSH-láit
V: 🛏️|sleeping bag|saco de dormir|SLÍ-ping-bég
V: 🍫|snacks|lanches|SNÉKS
V: 📖|story|história|STÓ-ri
V: 🌙|night|noite|NÁIT
H: Come over tonight.|Venha aqui hoje à noite.
H: Can you stay over?|Você pode dormir aqui?
H: Come over with your sleeping bag.|Venha com o seu saco de dormir.
H: Stay over and bring snacks.|Durma aqui e traga lanches.
H: We tell a story when you stay over.|Nós contamos uma história quando você dorme aqui.
L: Chris, come over tonight.|Chris, venha aqui hoje à noite.
L: Cool. Can I stay over?|Legal. Posso dormir aí?
L: Sure. Come over with your sleeping bag.|Claro. Venha com o seu saco de dormir.
L: Okay. I bring a flashlight, too.|Certo. Eu levo uma lanterna também.
L: Stay over and bring snacks.|Durma aqui e traga lanches.
L: Deal. We sleep in the tent.|Fechado. Nós dormimos na barraca.
L: We tell a story when you stay over.|Nós contamos uma história quando você dorme aqui.
L: The best night ever, Gordie.|A melhor noite de todas, Gordie.
Q: What does Gordie ask Chris to do?|O que o Gordie pede ao Chris?|0|🌙 Come over tonight|⛺ Go to school|🍫 Cook dinner
Q: What does Chris bring?|O que o Chris leva?|3|🔦 A flashlight|📖 A book|🍫 A pizza
Q: Where do they sleep?|Onde eles dormem?|5|⛺ In the tent|🏠 In the kitchen|🌳 On a tree
B: invite|💌|convidar|I invite Chris.|He invites Chris.|She invited us.|Ela nos convidou.
B: bring|🎒|trazer|I bring snacks.|He brings snacks.|They brought a tent.|Eles trouxeram uma barraca.
B: tell|🗣️|contar|I tell a story.|He tells a story.|She told us a joke.|Ela nos contou uma piada.
B: sleep|😴|dormir|I sleep in the tent.|He sleeps in the tent.|We slept late.|Nós dormimos até tarde.
LAB: te|Laboratório de sons: tent, snacks e night|Tent soa “TÉNT”. Snacks soa “SNÉKS”. Night termina em t, “NÁIT”.|Em night, o gh não se fala: NÁIT.
W: tent|TÉNT|barraca|e aberto|tint|TÍNT
W: snacks|SNÉKS|lanches|sn junto|snakes|SNÊIKS
W: night|NÁIT|noite|gh mudo|nine|NÁIN
G: 0|Come over|Come on|Come out
G: 1|stay over|stay on|stay out
G: 2|Come over|Come on|Come out
G: 3|Stay over|Stay on|Stay out
X: 😄|Awesome|Demais|elogiar|Awesome, a night in a tent!|Demais, uma noite na barraca!
X: 🤫|Shh|Shh|pedir silêncio|Shh, Mom is asleep.|Shh, a mamãe está dormindo.
X: 🤝|Best friends|Melhores amigos|carinho|Best friends forever.|Melhores amigos para sempre.
X: 🔦|Turn it off|Apague|pedir|Turn it off, it is late.|Apague, está tarde.

N: 7080223
C: Jack,Annie | misshoney,tommy | No ônibus em alta velocidade, Jack e Annie avisam: hold on, stand up.
S: segurar-se e dar lugar com hold on e stand up: Hold on to the pole. Stand up
Y: Hoje você aprende hold on (segurar firme) e stand up (levantar-se). Hold on to the pole! Stand up and give her the seat.
F: Speed | 🎬 Filme | 1994 | um filme de ação dirigido por Jan de Bont, sobre um ônibus que não pode diminuir a velocidade | avisar para segurar firme e levantar | street | 🚌,🛑,🛣️
V: 🚌|bus|ônibus|BÂS
V: 🧍|pole|barra|PÔUL
V: 🧳|bag|bolsa|BÉG
V: 💺|seat|assento|SÍT
V: 🛑|brake|freio|BRÊIK
V: 🛣️|highway|rodovia|RÁI-uêi
H: Hold on, the bus is fast!|Segure firme, o ônibus está rápido!
H: Hold on to the pole.|Segure-se na barra.
H: Stand up and take your bag.|Levante-se e pegue sua bolsa.
H: Stand up, give her the seat.|Levante-se, dê o assento a ela.
H: Hold on, we hit the brake!|Segure firme, vamos frear!
L: Annie, hold on, the bus is fast!|Annie, segure firme, o ônibus está rápido!
L: I hold on to the pole, Jack.|Eu me seguro na barra, Jack.
L: Good. Now stand up and take your bag.|Bom. Agora levante-se e pegue sua bolsa.
L: Stand up, give her the seat.|Levante-se, dê o assento a ela.
L: Okay. The road is long.|Certo. A estrada é longa.
L: Hold on, we hit the brake!|Segure firme, vamos frear!
L: Stop! Everybody, hold on!|Pare! Pessoal, segurem firme!
L: We did it. The bus stops now.|Conseguimos. O ônibus para agora.
Q: What does Annie hold on to?|Em que a Annie se segura?|1|🧍 The pole|🧳 The bag|💺 The seat
Q: What does Jack say to do with the seat?|O que o Jack diz fazer com o assento?|3|💺 Give it to her|🛑 Sit on it|🧳 Break it
Q: What do they hit?|O que eles acionam?|5|🛑 The brake|🛣️ The road|🧍 The pole
B: drive|🚌|dirigir|I drive the bus.|He drives the bus.|She drove fast.|Ela dirigiu rápido.
B: steer|🛞|dirigir (o volante)|I steer left.|She steers left.|He steered the bus.|Ele conduziu o ônibus.
B: jump|🦘|pular|I jump off the bus.|He jumps off the bus.|They jumped out.|Eles pularam para fora.
B: shout|📣|gritar|I shout, “Hold on!”|She shouts, “Hold on!”|We shouted together.|Nós gritamos juntos.
LAB: bu|Laboratório de sons: bus, pole e brake|Bus soa “BÂS”, com u = â. Pole soa “PÔUL”. Brake soa “BRÊIK”, com a = êi.|Em bus, o u soa â: BÂS.
W: bus|BÂS|ônibus|u = â|boss|BÓS
W: pole|PÔUL|barra|o = ôu|poll|PÔUL
W: brake|BRÊIK|freio|a = êi|break|BRÊIK
G: 0|Hold on|Hold up|Hold in
G: 1|Hold on|Hold up|Hold in
G: 2|Stand up|Stand on|Stand in
G: 3|Stand up|Stand on|Stand in
X: 😱|Look out|Cuidado|avisar|Look out, a car!|Cuidado, um carro!
X: 💪|Keep going|Continue|animar|Keep going, Jack.|Continue, Jack.
X: 😅|That was close|Foi por pouco|reagir|That was close, Annie.|Foi por pouco, Annie.
X: 🙌|We did it|Conseguimos|comemorar|We did it, the bus stops!|Conseguimos, o ônibus para!

N: 7080225
C: Alex,Marty | tommy,tom | Numa viagem de caixote, Alex e Marty perguntam se falta muito: Are we there yet? Almost there.
S: perguntar se falta muito: Are we there yet? Almost there
Y: Hoje você aprende a perguntar se já chegou: Are we there yet? e a responder Almost there! (quase lá).
F: Madagascar | 🎬 Animação | 2005 | uma animação dirigida por Eric Darnell e Tom McGrath, sobre animais do zoológico que vão parar numa ilha | perguntar se já chegaram | lighthouse | 🦁,🦓,🏝️
V: 🦁|lion|leão|LÁI-on
V: 🦓|zebra|zebra|ZÍ-bra
V: 📦|crate|caixote|KRÊIT
V: 🏝️|island|ilha|ÁI-land
V: 🍌|banana|banana|ba-NÉ-na
V: 🌴|palm tree|palmeira|PÁM-trí
H: Are we there yet?|Já chegamos?
H: Almost there, Alex.|Quase lá, Alex.
H: Are we there yet? I am in a crate.|Já chegamos? Eu estou num caixote.
H: Almost there, I see the island.|Quase lá, eu vejo a ilha.
H: Are we there yet? I want a banana.|Já chegamos? Eu quero uma banana.
L: Marty, are we there yet?|Marty, já chegamos?
L: Almost there, Alex.|Quase lá, Alex.
L: Are we there yet? I am in a crate.|Já chegamos? Eu estou num caixote.
L: Almost there, I see the island.|Quase lá, eu vejo a ilha.
L: Are we there yet? I want a banana.|Já chegamos? Eu quero uma banana.
L: Here, take mine. Look, a palm tree!|Tome a minha. Olhe, uma palmeira!
L: Almost there. The beach is next.|Quase lá. A praia é a próxima.
L: We are here! Open the crate.|Chegamos! Abra o caixote.
Q: What does Alex ask?|O que o Alex pergunta?|0|🦁 Are we there yet?|🦓 Where is the zoo?|🍌 Where is the banana?
Q: What does Marty see?|O que o Marty vê?|3|🏝️ The island|🦁 A lion|🍌 A banana
Q: What does Alex want?|O que o Alex quer?|4|🍌 A banana|🏝️ An island|🌴 A palm tree
B: travel|🧳|viajar|I travel by ship.|He travels by ship.|They traveled a week.|Eles viajaram uma semana.
B: ask|❓|perguntar|I ask, “Are we there?”|He asks, “Are we there?”|She asked twice.|Ela perguntou duas vezes.
B: wait|⏳|esperar|I wait in the crate.|He waits in the crate.|We waited all day.|Nós esperamos o dia todo.
B: sleep|😴|dormir|I sleep on the road.|He sleeps on the road.|They slept in the crate.|Eles dormiram no caixote.
LAB: li|Laboratório de sons: lion, crate e banana|Lion soa “LÁI-on”. Crate soa “KRÊIT”, com a = êi. Banana tem a força no meio, “ba-NÉ-na”.|Em banana, a força cai na segunda sílaba: ba-NÉ-na.
W: lion|LÁI-on|leão|i = ái|line|LÁIN
W: crate|KRÊIT|caixote|a = êi|cray|KRÊI
W: banana|ba-NÉ-na|banana|força no meio|bandana|ban-DÉ-na
G: 0|Are we|Is we|Do we
G: 1|Almost|Most|Also
G: 2|there|here|where
G: 3|Almost|Most|Also
X: 😩|So long|Tão longe|reclamar|So long, I am tired.|Tão longe, estou cansado.
X: 😮|Look there|Olhe ali|chamar atenção|Look there, an island!|Olhe ali, uma ilha!
X: 🎉|We made it|Nós conseguimos|comemorar|We made it, Marty!|Nós conseguimos, Marty!
X: 🍌|Take mine|Pegue a minha|oferecer|Take mine, I have two.|Pegue a minha, eu tenho duas.

N: 80228
C: Fox,Badger | tom,tommy | Na toca, o senhor Raposa e o Texugo pedem e oferecem coisas: borrow, lend.
S: pedir e emprestar com borrow e lend: Can I borrow your ladder? I can lend you a shovel
Y: Hoje você aprende borrow (pegar emprestado) e lend (emprestar). Can I borrow your ladder? I can lend you a shovel.
F: Fantastic Mr. Fox | 🎬 Animação | 2009 | uma animação dirigida por Wes Anderson, sobre uma raposa esperta que faz planos para roubar comida de fazendeiros | pedir e oferecer coisas emprestadas | cave | 🦊,🪜,⛏️
V: 🪜|ladder|escada|LÉ-der
V: ⛏️|shovel|pá|SHÂ-vol
V: 🔦|lamp|lampião|LÉMP
V: 👜|bag|sacola|BÉG
V: 🍎|cider|sidra|SÁI-der
V: 🕳️|tunnel|túnel|TÂ-nol
H: Can I borrow your ladder?|Posso pegar sua escada emprestada?
H: I can lend you a shovel.|Eu posso emprestar uma pá a você.
H: Please lend me your lamp.|Por favor, empreste-me o seu lampião.
H: Can I borrow your bag?|Posso pegar sua sacola emprestada?
H: I can lend you some cider.|Eu posso emprestar sidra a você.
L: Badger, can I borrow your ladder?|Texugo, posso pegar sua escada emprestada?
L: Yes. I can lend you a shovel, too.|Sim. Eu posso emprestar uma pá também.
L: Thank you. Please lend me your lamp.|Obrigado. Por favor, empreste-me o seu lampião.
L: Of course. Can I borrow your bag?|Claro. Posso pegar sua sacola emprestada?
L: Sure. The tunnel is long.|Claro. O túnel é longo.
L: I can lend you some cider for the trip.|Eu posso emprestar sidra a você para a viagem.
L: Great. I return everything tomorrow.|Ótimo. Eu devolvo tudo amanhã.
L: Good luck, Mister Fox.|Boa sorte, senhor Raposa.
Q: What does Fox want to borrow first?|O que o Raposa quer pegar emprestado primeiro?|0|🪜 A ladder|⛏️ A shovel|🍎 Cider
Q: What does Badger want to borrow?|O que o Texugo quer pegar emprestado?|3|👜 A bag|🔦 A lamp|🪜 A ladder
Q: When does Fox return everything?|Quando o Raposa devolve tudo?|6|📅 Tomorrow|📅 Today|📅 Never
B: borrow|🙏|pegar emprestado|I borrow a ladder.|He borrows a ladder.|She borrowed a lamp.|Ela pegou um lampião emprestado.
B: lend|🤲|emprestar|I lend a shovel.|He lends a shovel.|They lent me a bag.|Eles me emprestaram uma sacola.
B: return|↩️|devolver|I return the lamp.|He returns the lamp.|She returned the bag.|Ela devolveu a sacola.
B: dig|⛏️|cavar|I dig a tunnel.|He digs a tunnel.|They dug all night.|Eles cavaram a noite toda.
LAB: la|Laboratório de sons: ladder, shovel e cider|Ladder tem dd rápido, “LÉ-der”. Shovel soa “SHÂ-vol”, com o = â. Cider soa “SÁI-der”.|Em shovel, o o soa como â: SHÂ-vol.
W: ladder|LÉ-der|escada|dd = d suave|latter|LÉ-der
W: shovel|SHÂ-vol|pá|o = â|shuffle|SHÂ-fol
W: cider|SÁI-der|sidra|i = ái|spider|SPÁI-der
G: 0|borrow|lend|borrowing
G: 1|lend|borrow|lending
G: 2|lend|borrow|lending
G: 3|borrow|lend|borrowing
X: 🙏|Thanks a lot|Muito obrigado|agradecer|Thanks a lot, Badger.|Muito obrigado, Texugo.
X: 🤝|No problem|Sem problema|responder|No problem, my friend.|Sem problema, meu amigo.
X: 🍀|Good luck|Boa sorte|desejar|Good luck, Mister Fox.|Boa sorte, senhor Raposa.
X: 😉|Be careful|Tenha cuidado|avisar|Be careful in the tunnel.|Tenha cuidado no túnel.

N: 7080228
C: Ralph,Vanellope | tom,polly | No fliperama, Ralph e Vanellope pedem o carregador: for a minute, for a while.
S: pedir por quanto tempo: Can I use your charger for a minute? Wait for a while
Y: Hoje você aprende for a minute (por um minutinho) e for a while (por um tempo). Can I use your charger for a minute?
F: Wreck-It Ralph | 🎬 Animação | 2012 | uma animação da Disney, dirigida por Rich Moore, sobre um vilão de videogame que sai do seu jogo em busca de mudança | pedir algo por um tempo | toyshop | 🕹️,🏎️,🔌
V: 🔌|charger|carregador|TCHÁR-djer
V: 🔋|battery|bateria|BÉ-te-ri
V: 📞|phone|celular|FÔUN
V: 🕹️|game|jogo|GUÊIM
V: 🏎️|race car|carro de corrida|RÊIS-kár
V: 🏆|prize|prêmio|PRÁIZ
H: Can I use your charger for a minute?|Posso usar seu carregador por um minutinho?
H: Wait for a while, the battery is low.|Espere um tempo, a bateria está fraca.
H: Can I use the phone for an hour?|Posso usar o celular por uma hora?
H: Play the game for a while.|Jogue por um tempo.
H: Drive the race car for a minute.|Dirija o carro de corrida por um minutinho.
L: Vanellope, can I use your charger for a minute?|Vanellope, posso usar seu carregador por um minutinho?
L: Wait for a while, the battery is low.|Espere um tempo, a bateria está fraca.
L: Okay. Can I use the phone for an hour?|Certo. Posso usar o celular por uma hora?
L: No, just for a minute. Then play the game.|Não, só por um minutinho. Depois jogue.
L: Play the game for a while.|Jogue por um tempo.
L: Fine. Can I drive the race car, too?|Certo. Posso dirigir o carro de corrida também?
L: Drive the race car for a minute.|Dirija o carro de corrida por um minutinho.
L: Thanks! I win the prize!|Obrigado! Eu ganho o prêmio!
Q: What does Ralph want for a minute?|O que o Ralph quer por um minutinho?|0|🔌 The charger|📞 The phone|🏆 The prize
Q: How long can Ralph use the phone?|Por quanto tempo o Ralph pode usar o celular?|3|⏱️ Just for a minute|⏱️ For an hour|⏱️ For a day
Q: What does Ralph drive?|O que o Ralph dirige?|6|🏎️ The race car|🔌 The charger|🕹️ The game
B: charge|🔌|carregar|I charge my phone.|He charges his phone.|She charged the battery.|Ela carregou a bateria.
B: call|📞|ligar|I call a friend.|He calls a friend.|They called Ralph.|Eles ligaram para o Ralph.
B: win|🏆|ganhar|I win the prize.|He wins the prize.|She won the race.|Ela ganhou a corrida.
B: fix|🔧|consertar|I fix the game.|He fixes the game.|They fixed the car.|Eles consertaram o carro.
LAB: ch|Laboratório de sons: charger, battery e prize|Charger começa com tch, “TCHÁR-djer”. Battery tem tt rápido, “BÉ-te-ri”. Prize termina em z, “PRÁIZ”.|Em charger, o ch soa tch e o g soa dj: TCHÁR-djer.
W: charger|TCHÁR-djer|carregador|ch = tch|char|TCHÁR
W: battery|BÉ-te-ri|bateria|força no começo|butter|BÂ-der
W: prize|PRÁIZ|prêmio|i = ái|price|PRÁIS
G: 0|for a minute|in a minute|on a minute
G: 1|for a while|on a while|to a while
G: 3|for a while|on a while|to a while
G: 4|for a minute|in a minute|on a minute
X: 🙏|Please|Por favor|pedir|Please, just a minute.|Por favor, só um minutinho.
X: 😅|Hurry up|Ande logo|apressar|Hurry up, the battery!|Ande logo, a bateria!
X: 🏆|Hooray|Eba|comemorar|Hooray, I win!|Eba, eu ganhei!
X: 🤝|Sure thing|Claro|aceitar|Sure thing, Ralph.|Claro, Ralph.
''')
