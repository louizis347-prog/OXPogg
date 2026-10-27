# Lote B (cinema), dados 6: episódios A1 7080205 .. 7080218. Formato: ver zz_b_lib.py.
from v3.zz_b_lib import add

add('''
N: 7080205
T: Too much cream
C: Bugsy,Blousey | polly,misshoney | Na festa das tortas, Bugsy e Blousey dizem que algo é demais: too much, too many.
S: dizer que algo é demais com too much e too many: Too much cream. Too many cookies
Y: Hoje você aprende too much (demais, para o que não se conta) e too many (demais, para o que se conta). Too much cream. Too many cookies.
F: Bugsy Malone | 🎬 Musical | 1976 | um filme musical dirigido por Alan Parker, em que crianças fazem papel de gângsteres e brigam com tortas de creme | dizer que algo é demais | bakery | 🥧,🍦,🍪
V: 🥧|pie|torta|PÁI
V: 🍦|cream|creme|KRÍM
V: 🍬|candies|balas|KÉN-diz
V: 🥤|soda|refrigerante|SÔU-da
V: 🍪|cookies|biscoitos|KÚ-kiz
V: 🤢|stomachache|dor de barriga|STÂ-mak-êik
H: There is too much cream on the pie.|Tem creme demais na torta.
H: I put too much cream here.|Eu pus creme demais aqui.
H: You eat too many candies.|Você come balas demais.
H: That is too much soda.|Isso é refrigerante demais.
H: Too many cookies make a stomachache.|Biscoitos demais dão dor de barriga.
L: Blousey, there is too much cream on the pie.|Blousey, tem creme demais na torta.
L: Oh no! I put too much cream here.|Ai, não! Eu pus creme demais aqui.
L: And you eat too many candies, Bugsy.|E você come balas demais, Bugsy.
L: That is too much soda, too.|Isso também é refrigerante demais.
L: Too many cookies make a stomachache.|Biscoitos demais dão dor de barriga.
L: My stomach is full. I stop now.|Minha barriga está cheia. Eu paro agora.
L: Good. Let’s share the pie with friends.|Bom. Vamos dividir a torta com os amigos.
L: Great idea. Not too much for me!|Ótima ideia. Não demais para mim!
Q: What is on the pie?|O que está na torta?|0|🍦 Too much cream|🍪 Too many cookies|🥤 Too much soda
Q: What does Bugsy eat too many of?|De que o Bugsy come demais?|2|🍬 Candies|🥧 Pies|🥤 Sodas
Q: What do too many cookies make?|O que biscoitos demais causam?|4|🤢 A stomachache|😴 Sleep|🎉 A party
B: taste|😋|provar|I taste a cookie.|He tastes a cookie.|She tasted the candies.|Ela provou as balas.
B: throw|🥧|jogar|I throw the pie.|He throws the pie.|They threw cream.|Eles jogaram creme.
B: splash|💦|respingar|I splash the soda.|She splashes the soda.|He splashed the cream.|Ele respingou o creme.
B: stop|🛑|parar|I stop eating.|He stops eating.|We stopped the game.|Nós paramos o jogo.
LAB: cr|Laboratório de sons: cream, soda e cookies|Cream soa “KRÍM”, com ea = í. Soda soa “SÔU-da”. Cookies soa “KÚ-kiz”, com oo curto.|Em cream, o ea soa í: KRÍM.
W: cream|KRÍM|creme|ea = í|crime|KRÁIM
W: soda|SÔU-da|refrigerante|o = ôu|sofa|SÔU-fa
W: cookies|KÚ-kiz|biscoitos|oo curto|cooks|KÚKS
G: 0|much|many|more
G: 2|many|much|more
G: 3|much|many|long
G: 4|many|much|more
X: 😮|That’s a lot|É muita coisa|se surpreender|That’s a lot of cream!|É muito creme!
X: 😅|Oops|Ops|se desculpar|Oops, too much soda.|Ops, refrigerante demais.
X: 🛑|Stop it|Pare|pedir|Stop it, Bugsy.|Pare com isso, Bugsy.
X: 🤝|Let’s share|Vamos dividir|propor|Let’s share this pie.|Vamos dividir esta torta.

N: 7080206
C: Scotty,Benny | tom,tommy | Num dia de verão, Scotty e Benny fazem sugestões: Why don’t we…? How about…?
S: fazer sugestões com Why don’t we…? e How about…?: Why don’t we play baseball
Y: Hoje você aprende a sugerir: Why don’t we + verbo? (Por que não…?) e How about + coisa? (Que tal…?).
F: The Sandlot | 🎬 Filme | 1993 | um filme dirigido por David Mickey Evans, sobre um grupo de meninos que passa o verão jogando beisebol num terreno | sugerir o que fazer | park | ⚾,🧤,🍦
V: ⚾|baseball|beisebol|BÊIS-bol
V: 🧤|glove|luva|GLÂV
V: 🏊|pool|piscina|PÚL
V: 🍦|ice cream|sorvete|ÁIS-krím
V: 🎆|fireworks|fogos|FÁI-er-uârks
V: 🌞|summer|verão|SÂ-mer
H: Why don’t we play baseball?|Por que não jogamos beisebol?
H: How about my glove?|Que tal a minha luva?
H: Why don’t we go to the pool?|Por que não vamos à piscina?
H: How about ice cream?|Que tal um sorvete?
H: Why don’t we watch the fireworks?|Por que não vemos os fogos?
L: Benny, why don’t we play baseball?|Benny, por que não jogamos beisebol?
L: Good idea. How about my glove?|Boa ideia. Que tal a minha luva?
L: Great. It is hot. Why don’t we go to the pool?|Ótimo. Está quente. Por que não vamos à piscina?
L: Sure. And after that, how about ice cream?|Claro. E depois, que tal um sorvete?
L: Yes! Ice cream in the summer is the best.|Sim! Sorvete no verão é o melhor.
L: Tonight, why don’t we watch the fireworks?|Hoje à noite, por que não vemos os fogos?
L: Perfect. Let’s meet at the sandlot.|Perfeito. Vamos nos encontrar no terreno.
L: See you there, Scotty!|Até lá, Scotty!
Q: What does Scotty suggest first?|O que o Scotty sugere primeiro?|0|⚾ Baseball|🏊 The pool|🎆 Fireworks
Q: What do they have after the pool?|O que eles tomam depois da piscina?|3|🍦 Ice cream|🧤 A glove|🎆 Fireworks
Q: What do they watch tonight?|O que eles veem hoje à noite?|5|🎆 Fireworks|⚾ Baseball|🏊 The pool
B: play|⚾|jogar|I play baseball.|He plays baseball.|They played all day.|Eles jogaram o dia todo.
B: hit|🏏|bater|I hit the ball.|He hits the ball.|She hit it far.|Ela a bateu longe.
B: catch|🧤|pegar|I catch the ball.|He catches the ball.|They caught it twice.|Eles a pegaram duas vezes.
B: meet|🤝|encontrar|I meet Benny.|He meets Benny.|We met at noon.|Nós nos encontramos ao meio-dia.
LAB: gl|Laboratório de sons: glove, pool e fireworks|Glove soa “GLÂV”, com o = â. Pool tem u longo, “PÚL”. Fireworks soa “FÁI-er-uârks”.|Em glove, o o soa como â: GLÂV.
W: glove|GLÂV|luva|o = â|love|LÂV
W: pool|PÚL|piscina|oo = ú|pull|PÚL
W: fireworks|FÁI-er-uârks|fogos|fire + works|firewood|FÁI-er-uúd
G: 0|Why don’t we|Why we don’t|Why not we
G: 1|How about|How for|How with
G: 2|Why don’t we|Why we don’t|Why not we
G: 3|How about|How for|How with
X: 😄|Sounds good|Parece bom|aceitar|Sounds good, let’s go!|Parece bom, vamos!
X: 🙌|Why not|Por que não|aceitar|Why not, I love baseball.|Por que não, eu amo beisebol.
X: 😎|Great idea|Ótima ideia|elogiar|Great idea, Benny.|Ótima ideia, Benny.
X: ⏰|See you there|Até lá|despedir-se|See you there at six.|Até lá às seis.

N: 7080208
C: Katherine,Dorothy | polly,tommy | Numa sala da equipe, Katherine e Dorothy contam quantos fizeram a tarefa: all, most, none.
S: dizer quantos: All of the numbers are right. Most of the team is here
Y: Hoje você aprende all (todos), most (a maioria) e none (nenhum). All of the numbers are right. None of the reports are late.
F: Hidden Figures | 🎬 Filme | 2016 | um filme dirigido por Theodore Melfi, sobre mulheres matemáticas que fizeram cálculos importantes para a Nasa | dizer quantos fizeram algo | library | 🧮,🚀,📋
V: 🧮|numbers|números|NÂM-berz
V: ✏️|pencils|lápis|PÉN-solz
V: 📋|reports|relatórios|ri-PÓRTS
V: 🧑‍🔬|team|equipe|TÍM
V: 🚀|rockets|foguetes|RÓ-kits
V: 📐|ruler|régua|RÚ-ler
H: All of the numbers are right.|Todos os números estão certos.
H: Most of the pencils are new.|A maioria dos lápis é nova.
H: None of the reports are late.|Nenhum dos relatórios está atrasado.
H: All of the team is here.|Toda a equipe está aqui.
H: Most of the rockets work.|A maioria dos foguetes funciona.
L: Dorothy, are the numbers right?|Dorothy, os números estão certos?
L: All of the numbers are right, Katherine.|Todos os números estão certos, Katherine.
L: Good. Do we have pencils?|Bom. Temos lápis?
L: Most of the pencils are new.|A maioria dos lápis é nova.
L: And the reports? None of the reports are late.|E os relatórios? Nenhum dos relatórios está atrasado.
L: Is the team here?|A equipe está aqui?
L: All of the team is here. Most of the rockets work.|Toda a equipe está aqui. A maioria dos foguetes funciona.
L: Then let’s vote and start the work.|Então vamos votar e começar o trabalho.
Q: How are the numbers?|Como estão os números?|1|🧮 All are right|🧮 Most are right|🧮 None are right
Q: How many pencils are new?|Quantos lápis são novos?|3|✏️ Most of them|✏️ All of them|✏️ None of them
Q: How many reports are late?|Quantos relatórios estão atrasados?|4|📋 None of them|📋 All of them|📋 Most of them
B: count|🔢|contar|I count the numbers.|She counts the numbers.|He counted the pencils.|Ele contou os lápis.
B: calculate|🧮|calcular|I calculate the numbers.|She calculates the numbers.|They calculated all day.|Eles calcularam o dia todo.
B: vote|🗳️|votar|I vote for the plan.|She votes for the plan.|We voted together.|Nós votamos juntos.
B: finish|🏁|terminar|I finish the report.|She finishes the report.|They finished early.|Eles terminaram cedo.
LAB: nu|Laboratório de sons: numbers, pencils e reports|Numbers soa “NÂM-berz”. Pencils soa “PÉN-solz”. Reports tem a força no fim, “ri-PÓRTS”.|Em reports, a força cai na segunda sílaba: ri-PÓRTS.
W: numbers|NÂM-berz|números|u = â|members|MÉM-berz
W: pencils|PÉN-solz|lápis|c = s|pencil case|PÉN-sol-kêis
W: reports|ri-PÓRTS|relatórios|força no fim|sports|SPÓRTS
G: 0|All|Every|Both
G: 1|Most|Much|More
G: 2|None|No|Not
G: 3|All|Every|Both
X: 👏|Well done|Muito bem|elogiar|Well done, team.|Muito bem, equipe.
X: 😊|Thank you all|Obrigada a todos|agradecer|Thank you all for the work.|Obrigada a todos pelo trabalho.
X: 🙋|Raise your hand|Levante a mão|pedir|Raise your hand to vote.|Levante a mão para votar.
X: 🚀|Ready to go|Pronto para ir|avisar|Ready to go, Katherine.|Pronto para ir, Katherine.

N: 7080209
C: Shaun,Bitzer | tom,tommy | No piquenique da fazenda, Shaun e Bitzer contam o que sobrou e pedem mais: left, another, one more.
S: pedir outro e contar o que resta: Can I have another cookie? One more apple
Y: Hoje você aprende left (restante), another (outro) e one more (mais um). Can I have another cookie? There is one more apple left.
F: Shaun the Sheep Movie | 🎬 Animação | 2015 | uma animação dirigida por Mark Burton e Richard Starzak, sobre uma ovelha esperta que vai à cidade grande atrás do fazendeiro | pedir mais e contar o que sobrou | park | 🐑,🍪,🧺
V: 🍪|cookie|biscoito|KÚ-ki
V: 🧺|basket|cesta|BÉS-ket
V: 🍎|apple|maçã|É-pol
V: 🥛|milk|leite|MÍLK
V: 🐑|sheep|ovelha|SHÍP
V: ⛰️|hill|morro|RÍL
H: Can I have another cookie?|Posso pegar outro biscoito?
H: How many cookies are left?|Quantos biscoitos restam?
H: One more apple, please.|Mais uma maçã, por favor.
H: Is there any milk left?|Ainda tem leite?
H: Another sheep is here.|Outra ovelha está aqui.
L: Bitzer, can I have another cookie?|Bitzer, posso pegar outro biscoito?
L: How many cookies are left in the basket?|Quantos biscoitos restam na cesta?
L: Three. One more apple, please.|Três. Mais uma maçã, por favor.
L: Here you are, Shaun.|Aqui está, Shaun.
L: Is there any milk left?|Ainda tem leite?
L: Yes, a little. Another sheep is here.|Sim, um pouco. Outra ovelha está aqui.
L: Welcome! Share the picnic on the hill.|Bem-vinda! Divida o piquenique no morro.
L: Baa! One more cookie for my friend.|Mé! Mais um biscoito para a minha amiga.
Q: What does Shaun want?|O que o Shaun quer?|0|🍪 Another cookie|🍎 Another hill|🥛 Another basket
Q: What does Shaun ask for after the cookie?|O que o Shaun pede depois?|2|🍎 One more apple|🥛 Some milk|🧺 A basket
Q: Who is here?|Quem chegou?|5|🐑 Another sheep|🐕 Another dog|🐷 A pig
B: share|🤝|dividir|I share the cookies.|He shares the cookies.|They shared the apple.|Eles dividiram a maçã.
B: bring|🎁|trazer|I bring the basket.|He brings the basket.|She brought milk.|Ela trouxe leite.
B: spill|💦|derramar|I spill the milk.|He spills the milk.|The sheep spilled it.|A ovelha o derramou.
B: wipe|🧽|limpar|I wipe the table.|He wipes the table.|We wiped the milk.|Nós limpamos o leite.
LAB: co|Laboratório de sons: cookie, basket e sheep|Cookie soa “KÚ-ki”, com oo curto. Basket soa “BÉS-ket”. Sheep soa “SHÍP”, com ee = í.|Em sheep, alongue o í: SHÍÍP, diferente de ship.
W: cookie|KÚ-ki|biscoito|oo curto|rookie|RÚ-ki
W: basket|BÉS-ket|cesta|a = é|biscuit|BÍS-kit
W: sheep|SHÍP|ovelha|ee = í longo|ship|SHÍP
G: 0|another|other|others
G: 1|left|leave|leaves
G: 2|One more|One most|One many
G: 4|Another|Other|Others
X: 🐑|Baa|Mé|imitar|Baa, I want more.|Mé, eu quero mais.
X: 😋|Yummy|Que delícia|elogiar|Yummy, one more cookie.|Que delícia, mais um biscoito.
X: 🙏|Help yourself|Sirva-se|oferecer|Help yourself to the apples.|Sirva-se das maçãs.
X: 🎉|What a picnic|Que piquenique|comemorar|What a picnic, Bitzer!|Que piquenique, Bitzer!

N: 7080210
C: Coraline,Wybie | misshoney,tommy | No jardim da casa, Coraline e Wybie dizem onde as coisas estão: inside, outside, out of.
S: dizer onde algo está: inside, outside e out of: Take the key out of the box
Y: Hoje você aprende inside (dentro), outside (fora) e out of (para fora de). Take the key out of the box. The cat is inside the house.
F: Coraline | 🎬 Animação | 2009 | uma animação dirigida por Henry Selick, sobre uma menina que descobre uma portinha secreta na casa nova | dizer onde as coisas estão | cave | 🔑,🚪,🐈
V: 🔑|key|chave|KÍ
V: 🐈|cat|gato|KÉT
V: 🏠|house|casa|RÁUS
V: 🚪|door|porta|DÓR
V: 📦|box|caixa|BÓKS
V: 🕳️|tunnel|túnel|TÂ-nol
H: Take the key out of the box.|Tire a chave da caixa.
H: It is cold, so the cat is inside the house.|Está frio, então o gato está dentro da casa.
H: Wybie is outside, in the yard.|O Wybie está fora, no quintal.
H: Come out of the little door.|Saia pela portinha.
H: Look inside the box.|Olhe dentro da caixa.
L: Wybie, take the key out of the box.|Wybie, tire a chave da caixa.
L: Here it is. Look inside the box, too.|Aqui está. Olhe dentro da caixa também.
L: Where is the cat?|Onde está o gato?
L: It is cold, so the cat is inside the house.|Está frio, então o gato está dentro da casa.
L: And where are you?|E onde você está?
L: I am outside, in the yard.|Eu estou fora, no quintal.
L: Come out of the little door, Coraline.|Saia pela portinha, Coraline.
L: Okay. Close the tunnel behind me.|Certo. Feche o túnel atrás de mim.
Q: What does Wybie take out of the box?|O que o Wybie tira da caixa?|0|🔑 The key|🐈 The cat|🏠 The house
Q: Where is the cat?|Onde está o gato?|3|🏠 Inside the house|🏡 In the yard|🕳️ In the tunnel
Q: Where is Wybie?|Onde está o Wybie?|5|🌳 Outside, in the yard|🏠 Inside the house|📦 Inside the box
B: open|📦|abrir|I open the box.|She opens the box.|He opened the door.|Ele abriu a porta.
B: close|🚪|fechar|I close the door.|She closes the door.|They closed the tunnel.|Eles fecharam o túnel.
B: hide|🙈|esconder|I hide the key.|He hides the key.|She hid in the box.|Ela se escondeu na caixa.
B: crawl|🐛|rastejar|I crawl in the tunnel.|She crawls in the tunnel.|They crawled out.|Eles saíram rastejando.
LAB: ke|Laboratório de sons: key, house e tunnel|Key soa “KÍ”, com ey = í. House soa “RÁUS”. Tunnel soa “TÂ-nol”.|Em key, o ey soa í: KÍ.
W: key|KÍ|chave|ey = í|quay|KÍ
W: house|RÁUS|casa|ou = áu|horse|RÓRS
W: tunnel|TÂ-nol|túnel|u = â|tonal|TÔU-nol
G: 0|out of|out from|outside
G: 1|inside|outside|out of
G: 2|outside|inside|out of
G: 3|out of|out from|outside
X: 😮|Look out|Cuidado|avisar|Look out, a little door!|Cuidado, uma portinha!
X: 🤫|Be quiet|Fique quieta|pedir silêncio|Be quiet, someone is inside.|Fique quieta, tem alguém dentro.
X: 😨|It’s dark|Está escuro|reclamar|It’s dark in the tunnel.|Está escuro no túnel.
X: 🔑|Got it|Peguei|confirmar|Got it, the key!|Peguei, a chave!

N: 80212
C: Daisy,Jojo | polly,misshoney | Na pizzaria, Daisy e Jojo pedem a pizza com ou sem ingredientes: with, without.
S: pedir com ou sem ingrediente: A pizza with mushrooms. Without onions, please
Y: Hoje você aprende with (com) e without (sem): A pizza with mushrooms, please. Without onions, please.
F: Mystic Pizza | 🎬 Filme | 1988 | um filme dirigido por Donald Petrie, sobre três amigas que trabalham numa pizzaria de uma cidade à beira-mar | pedir comida com ou sem ingredientes | bakery | 🍕,🍄,🧅
V: 🍕|pizza|pizza|PÍT-sa
V: 🍄|mushrooms|cogumelos|MÂSH-rumz
V: 🧅|onions|cebolas|Â-nions
V: 🧀|cheese|queijo|TCHÍZ
V: 🌶️|peppers|pimentões|PÉ-perz
V: 🥤|lemonade|limonada|lé-mo-NÊID
H: A pizza with mushrooms, please.|Uma pizza com cogumelos, por favor.
H: I hate onions. Without onions, please.|Eu odeio cebolas. Sem cebolas, por favor.
H: I love onions. With onions, please.|Eu amo cebolas. Com cebolas, por favor.
H: With mushrooms and cheese.|Com cogumelos e queijo.
H: Without peppers, please. I don’t like them.|Sem pimentões, por favor. Eu não gosto deles.
L: Jojo, what pizza do you want?|Jojo, que pizza você quer?
L: A pizza with mushrooms, please.|Uma pizza com cogumelos, por favor.
L: Hmm, I hate onions. Without onions, please.|Hmm, eu odeio cebolas. Sem cebolas, por favor.
L: Really? I love onions. With onions, please.|Sério? Eu amo cebolas. Com cebolas, por favor.
L: Then half and half. With mushrooms and cheese.|Então metade e metade. Com cogumelos e queijo.
L: Without peppers, please. I don’t like them.|Sem pimentões, por favor. Eu não gosto deles.
L: And a lemonade? With or without ice?|E uma limonada? Com ou sem gelo?
L: Without ice, please. Thank you!|Sem gelo, por favor. Obrigada!
Q: What does Jojo want on the pizza?|O que a Jojo quer na pizza?|1|🍄 Mushrooms|🧅 Onions|🌶️ Peppers
Q: Who loves onions?|Quem ama cebolas?|3|🧅 Jojo|🍄 Daisy|🌶️ The cook
Q: What is the lemonade like?|Como é a limonada?|7|🥤 Without ice|🥤 With ice|🥤 With peppers
B: order|🧾|pedir|I order a pizza.|She orders a pizza.|He ordered lemonade.|Ele pediu limonada.
B: add|➕|adicionar|I add cheese.|She adds cheese.|They added mushrooms.|Eles adicionaram cogumelos.
B: remove|➖|tirar|I remove the onions.|She removes the onions.|He removed the peppers.|Ele tirou os pimentões.
B: share|🤝|dividir|I share the pizza.|She shares the pizza.|We shared a slice.|Nós dividimos uma fatia.
LAB: pi|Laboratório de sons: pizza, mushrooms e lemonade|Pizza soa “PÍT-sa”, com zz = ts. Mushrooms soa “MÂSH-rumz”. Lemonade tem a força no fim, “lé-mo-NÊID”.|Em pizza, o zz soa ts: PÍT-sa.
W: pizza|PÍT-sa|pizza|zz = ts|piece|PÍS
W: mushrooms|MÂSH-rumz|cogumelos|u = â|rooms|RÚMZ
W: lemonade|lé-mo-NÊID|limonada|força no fim|lemon|LÉ-mon
G: 0|with|to|at
G: 1|Without|With|Not
G: 2|With|Without|To
G: 4|Without|With|Not
X: 😋|Sounds good|Parece bom|aceitar|Sounds good, I’m hungry.|Parece bom, estou com fome.
X: 🍕|Coming up|Já vai sair|responder|Coming up, two pizzas.|Já vai sair, duas pizzas.
X: 🙏|No problem|Sem problema|responder|No problem, no onions.|Sem problema, sem cebolas.
X: 😊|Enjoy|Aproveite|desejar|Enjoy your pizza!|Aproveite a sua pizza!

N: 7080212
C: Sarah,Hoggle | polly,tom | Num quarto cheio de brinquedos, Sarah e Hoggle propõem outra coisa: instead of, I’d rather.
S: propor outra coisa com instead of e I’d rather: Let’s play instead of watching TV
Y: Hoje você aprende a propor outra coisa: instead of (em vez de) e I’d rather (eu prefiro). Let’s play instead of watching TV. I’d rather play a board game.
F: Labyrinth | 🎬 Filme | 1986 | um filme dirigido por Jim Henson, sobre uma jovem que atravessa um labirinto cheio de criaturas para salvar o irmão | propor outra coisa no lugar | toyshop | 🧩,🎲,🧸
V: 📺|TV|televisão|TI-VÍ
V: 🎲|board game|jogo de tabuleiro|BÓRD-guêim
V: 🍿|popcorn|pipoca|PÓP-kórn
V: 🍎|fruit|fruta|FRÚT
V: 📚|book|livro|BÚK
V: 🧸|toy|brinquedo|TÓI
H: Let’s play instead of watching TV.|Vamos brincar em vez de ver TV.
H: I’d rather play a board game.|Eu prefiro jogar um jogo de tabuleiro.
H: Popcorn instead of candy.|Pipoca em vez de bala.
H: I’d rather have fruit.|Eu prefiro comer fruta.
H: I’d rather read a book.|Eu prefiro ler um livro.
L: Hoggle, let’s play instead of watching TV.|Hoggle, vamos brincar em vez de ver TV.
L: Good idea. I’d rather play a board game.|Boa ideia. Eu prefiro jogar um jogo de tabuleiro.
L: Do you want candy?|Você quer bala?
L: Popcorn instead of candy, please.|Pipoca em vez de bala, por favor.
L: And I’d rather have fruit.|E eu prefiro comer fruta.
L: Later, I’d rather read a book.|Mais tarde, eu prefiro ler um livro.
L: Fine. First the game, then the book.|Certo. Primeiro o jogo, depois o livro.
L: Deal! Roll the dice, Sarah.|Fechado! Jogue o dado, Sarah.
Q: What do they play instead of watching TV?|O que eles jogam em vez de ver TV?|1|🎲 A board game|📺 A video game|🧸 A toy
Q: What do they eat instead of candy?|O que eles comem em vez de bala?|3|🍿 Popcorn|🍬 Candy|🍎 Pizza
Q: What does Sarah read later?|O que a Sarah lê mais tarde?|5|📚 A book|📺 A TV guide|🎲 A game
B: play|🎲|jogar|I play a board game.|She plays a board game.|They played all day.|Eles jogaram o dia todo.
B: roll|🎲|rolar|I roll the dice.|She rolls the dice.|He rolled a six.|Ele tirou um seis.
B: read|📖|ler|I read a book.|She reads a book.|We read a story.|Nós lemos uma história.
B: decide|🤔|decidir|I decide to play.|She decides to play.|They decided on a game.|Eles decidiram por um jogo.
LAB: bo|Laboratório de sons: board game, popcorn e fruit|Board game soa “BÓRD-guêim”. Popcorn junta pop e corn, “PÓP-kórn”. Fruit tem u longo, “FRÚT”.|Em fruit, o ui soa ú: FRÚT.
W: board game|BÓRD-guêim|jogo de tabuleiro|oa = ó|bored|BÓRD
W: popcorn|PÓP-kórn|pipoca|pop + corn|pop|PÓP
W: fruit|FRÚT|fruta|ui = ú|fruity|FRÚ-ti
G: 0|instead of|instead|instead for
G: 1|rather|better|more
G: 2|instead of|instead|instead for
G: 4|rather|better|more
X: 😊|Deal|Fechado|aceitar|Deal, one more round.|Fechado, mais uma rodada.
X: 🤔|Let me think|Deixe-me pensar|pensar|Let me think, a game.|Deixe-me pensar, um jogo.
X: 😄|That’s better|Assim é melhor|opinar|That’s better, let’s play.|Assim é melhor, vamos jogar.
X: 🎲|Your turn|Sua vez|indicar|Your turn, Hoggle.|Sua vez, Hoggle.

N: 7910026
C: Toto,Alfredo | tommy,tom | No cinema da vila, Toto e Alfredo falam do que fazem enquanto esperam: while, during.
S: dizer o que faz enquanto: I read while I wait. Don’t talk during the movie
Y: Hoje você aprende while + frase (enquanto) e during + substantivo (durante). I read while I wait. Don’t talk during the movie.
F: Cinema Paradiso | 🎬 Filme | 1988 | um filme dirigido por Giuseppe Tornatore, sobre um menino siciliano que cresce dentro do cinema da vila com o projecionista | dizer o que se faz enquanto e durante | lighthouse | 🎞️,🎟️,🍿
V: 🎬|movie|filme|MÚ-vi
V: 🎟️|ticket|ingresso|TÍ-kit
V: 🎞️|film|película|FÍLM
V: 🔦|projector|projetor|pro-DJÉK-ter
V: 🪑|seat|poltrona|SÍT
V: 🥤|soda|refrigerante|SÔU-da
H: Don’t talk during the movie.|Não converse durante o filme.
H: I read while I wait.|Eu leio enquanto espero.
H: Be quiet during the film.|Fique quieto durante a película.
H: Alfredo cleans the projector while we wait.|O Alfredo limpa o projetor enquanto esperamos.
H: Stay in your seat during the show.|Fique na sua poltrona durante a sessão.
L: Alfredo, I buy a ticket while I wait.|Alfredo, eu compro um ingresso enquanto espero.
L: Good. Don’t talk during the movie.|Bom. Não converse durante o filme.
L: I read while I wait.|Eu leio enquanto espero.
L: Be quiet during the film, Toto.|Fique quieto durante a película, Toto.
L: I clean the projector while we wait.|Eu limpo o projetor enquanto esperamos.
L: Can I have a soda during the show?|Posso tomar um refrigerante durante a sessão?
L: Yes, but stay in your seat during the show.|Sim, mas fique na sua poltrona durante a sessão.
L: The lights go down. Shh, the film starts.|As luzes se apagam. Shh, a película começa.
Q: What does Toto do while he waits?|O que o Toto faz enquanto espera?|2|📖 He reads|🥤 He drinks|🎬 He talks
Q: What does Alfredo clean?|O que o Alfredo limpa?|4|🔦 The projector|🪑 The seat|🎟️ The ticket
Q: Where must Toto stay during the show?|Onde o Toto deve ficar durante a sessão?|6|🪑 In his seat|🚪 At the door|🔦 Near the projector
B: wait|⏳|esperar|I wait for the show.|He waits for the show.|They waited an hour.|Eles esperaram uma hora.
B: clean|🧽|limpar|I clean the projector.|He cleans the projector.|She cleaned the seat.|Ela limpou a poltrona.
B: watch|👀|assistir|I watch the film.|He watches the film.|We watched a movie.|Nós assistimos a um filme.
B: whisper|🤫|sussurrar|I whisper to Toto.|He whispers to Toto.|They whispered softly.|Eles sussurraram baixinho.
LAB: mo|Laboratório de sons: movie, projector e seat|Movie soa “MÚ-vi”. Projector tem a força no meio, “pro-DJÉK-ter”. Seat soa “SÍT”, com ea = í.|Em projector, a força cai na segunda sílaba: pro-DJÉK-ter.
W: movie|MÚ-vi|filme|oo = ú|mooey|MÚ-i
W: projector|pro-DJÉK-ter|projetor|j = dj|protector|pro-TÉK-ter
W: seat|SÍT|poltrona|ea = í|sit|SÍT
G: 0|during|while|when
G: 1|while|during|for
G: 3|while|during|for
G: 4|during|while|when
X: 🤫|Shh|Shh|pedir silêncio|Shh, the film starts.|Shh, a película começa.
X: 🎬|Lights out|Apaguem as luzes|anunciar|Lights out, Alfredo!|Apaguem as luzes, Alfredo!
X: 🍿|Enjoy the show|Aproveite a sessão|desejar|Enjoy the show, Toto.|Aproveite a sessão, Toto.
X: 😊|Good job|Bom trabalho|elogiar|Good job, my friend.|Bom trabalho, meu amigo.

N: 7080217
C: Jack,Elizabeth | captain,polly | No navio, Jack e Elizabeth pedem ajuda com o mapa: Show me… Tell me…
S: pedir ajuda com show me e tell me: Show me on the map. Tell me the way
Y: Hoje você aprende a pedir ajuda: Show me (Mostre-me) e Tell me (Diga-me). Show me on the map, please. Tell me the way to the island.
F: Pirates of the Caribbean | 🎬 Filme | 2003 | um filme dirigido por Gore Verbinski, sobre um pirata esperto e uma jovem que vão atrás de um tesouro no mar | pedir que mostrem ou digam o caminho | ship | 🏴‍☠️,🗺️,🏝️
V: 🗺️|map|mapa|MÉP
V: 🧭|compass|bússola|KÂM-pas
V: 🏴‍☠️|flag|bandeira|FLÉG
V: ⚓|anchor|âncora|ÉN-kor
V: 💰|treasure|tesouro|TRÉ-jer
V: 🏝️|island|ilha|ÁI-land
H: Show me on the map, please.|Mostre-me no mapa, por favor.
H: Tell me the way to the island.|Diga-me o caminho para a ilha.
H: Show me the flag.|Mostre-me a bandeira.
H: Tell me where the anchor is.|Diga-me onde está a âncora.
H: Tell me the way to the treasure.|Diga-me o caminho para o tesouro.
L: Jack, show me on the map, please.|Jack, mostre-me no mapa, por favor.
L: Here it is, Elizabeth. This is the island.|Aqui está, Elizabeth. Esta é a ilha.
L: Tell me the way to the island.|Diga-me o caminho para a ilha.
L: Follow the compass. Show me the flag.|Siga a bússola. Mostre-me a bandeira.
L: It is up there. Tell me where the anchor is.|Está lá em cima. Diga-me onde está a âncora.
L: Down in the water. Tell me the way to the treasure.|Lá embaixo, na água. Diga-me o caminho para o tesouro.
L: The treasure is on the island, mate.|O tesouro está na ilha, camarada.
L: Then raise the anchor and let’s go!|Então levante a âncora e vamos!
Q: What does Elizabeth want to see?|O que a Elizabeth quer ver?|0|🗺️ The map|🏴‍☠️ The flag|💰 The treasure
Q: What does Jack tell her to follow?|O que o Jack manda ela seguir?|3|🧭 The compass|⚓ The anchor|🏝️ The island
Q: Where is the treasure?|Onde está o tesouro?|6|🏝️ On the island|⚓ In the anchor|🏴‍☠️ On the flag
B: show|👀|mostrar|I show the map.|He shows the map.|She showed the flag.|Ela mostrou a bandeira.
B: tell|🗣️|dizer|I tell the way.|He tells the way.|They told me a secret.|Eles me contaram um segredo.
B: sail|⛵|navegar|I sail the ship.|He sails the ship.|We sailed to the island.|Nós navegamos até a ilha.
B: raise|⬆️|levantar|I raise the anchor.|He raises the anchor.|They raised the flag.|Eles levantaram a bandeira.
LAB: ma|Laboratório de sons: map, compass e treasure|Map soa “MÉP”. Compass soa “KÂM-pas”, com o = â. Treasure soa “TRÉ-jer”, com s = j suave.|Em treasure, o s soa como j suave: TRÉ-jer.
W: map|MÉP|mapa|a aberto|mop|MÓP
W: compass|KÂM-pas|bússola|o = â|compare|kom-PÉR
W: treasure|TRÉ-jer|tesouro|s = j suave|pleasure|PLÉ-jer
G: 0|Show me|Show to me|Shows me
G: 1|Tell me|Tell to me|Say me
G: 2|Show me|Show to me|Shows me
G: 4|Tell me|Tell to me|Say me
X: ⚓|Aye aye|Sim, senhor|responder|Aye aye, captain!|Sim, senhor, capitão!
X: 🧭|This way|Por aqui|indicar|This way, follow me.|Por aqui, siga-me.
X: 😮|Look there|Olhe ali|chamar atenção|Look there, an island!|Olhe ali, uma ilha!
X: 🙏|Thank you|Obrigada|agradecer|Thank you, Jack.|Obrigada, Jack.

N: 80218
C: Frodo,Sam | frodo,sam | Numa trilha da Terra Média, Frodo e Sam perguntam o rumo: Which way is…? This way, that way.
S: perguntar o rumo: Which way is the forest? This way, that way
Y: Hoje você aprende a perguntar e indicar o rumo: Which way is the forest? This way! (por aqui) The bridge is that way. (por ali)
F: The Fellowship of the Ring | 🎬 Filme | 2001 | o primeiro filme da trilogia O Senhor dos Anéis, dirigido por Peter Jackson, sobre um hobbit que sai numa longa viagem para destruir um anel | perguntar e indicar o caminho | jungle | 🌲,🌉,🪧
V: 🌲|forest|floresta|FÓ-rest
V: 🪧|sign|placa|SÁIN
V: 🌉|bridge|ponte|BRÍDJ
V: 🛤️|path|trilha|PÉF
V: 🏞️|stream|riacho|STRÍM
V: 🛖|inn|estalagem|ÍN
H: Which way is the forest?|Qual é o caminho para a floresta?
H: Look at the sign. This way!|Olhe a placa. Por aqui!
H: The bridge is that way.|A ponte fica por ali.
H: Which path goes to the inn?|Qual trilha vai para a estalagem?
H: The stream is this way.|O riacho fica por aqui.
L: Sam, which way is the forest?|Sam, qual é o caminho para a floresta?
L: Look at the sign, Mister Frodo. This way!|Olhe a placa, senhor Frodo. Por aqui!
L: And the bridge? Which way is the bridge?|E a ponte? Qual é o caminho para a ponte?
L: The bridge is that way.|A ponte fica por ali.
L: Which path goes to the inn?|Qual trilha vai para a estalagem?
L: The left path. The stream is this way.|A trilha da esquerda. O riacho fica por aqui.
L: Good. Stay close, Sam.|Bom. Fique perto, Sam.
L: Always, Mister Frodo.|Sempre, senhor Frodo.
Q: What does the sign say?|O que a placa diz?|1|🪧 This way|🪧 That way|🪧 No way
Q: Where is the bridge?|Onde fica a ponte?|3|🌉 That way|🌉 This way|🌉 In the forest
Q: Where is the stream?|Onde fica o riacho?|5|🏞️ This way|🏞️ That way|🏞️ Behind the inn
B: walk|🚶|andar|I walk on the path.|He walks on the path.|We walked all day.|Nós andamos o dia todo.
B: cross|🌉|atravessar|I cross the bridge.|He crosses the bridge.|They crossed the stream.|Eles atravessaram o riacho.
B: climb|🧗|subir|I climb the hill.|He climbs the hill.|She climbed the path.|Ela subiu a trilha.
B: turn|↩️|virar|I turn left.|He turns left.|We turned at the sign.|Nós viramos na placa.
LAB: fo|Laboratóriacho de sons: forest, bridge e path|Forest tem a força no começo, “FÓ-rest”. Bridge termina em dj, “BRÍDJ”. Path termina com th soprado, “PÉF”.|Em path, o th final é soprado: PÉF.
W: forest|FÓ-rest|floresta|força no começo|forced|FÓRST
W: bridge|BRÍDJ|ponte|dge = dj|brick|BRÍK
W: path|PÉF|trilha|th soprado|pat|PÉT
G: 0|Which way|What way|Where way
G: 1|This way|These way|Them way
G: 2|that|those|there
G: 4|this|these|those
X: 😊|Follow me|Siga-me|chamar|Follow me, Sam.|Siga-me, Sam.
X: 🌲|Stay close|Fique perto|avisar|Stay close, it is dark.|Fique perto, está escuro.
X: 😮|Look there|Olhe ali|chamar atenção|Look there, the bridge!|Olhe ali, a ponte!
X: 💪|Let’s go|Vamos|animar|Let’s go, Mister Frodo.|Vamos, senhor Frodo.

N: 7080218
C: Charlie,Rose | tom,polly | Num barco no rio, Charlie e Rose descrevem o trajeto: along, at the end of.
S: descrever o trajeto: along the river, at the end of the road
Y: Hoje você aprende along (ao longo de) e at the end of (no fim de). The boat goes along the river. The lake is at the end of the river.
F: The African Queen | 🎬 Filme | 1951 | um filme dirigido por John Huston, sobre um capitão de barco e uma missionária que descem um rio juntos | descrever o trajeto ao longo do rio | jungle | 🛶,🌴,🏞️
V: 🛶|boat|barco|BÔUT
V: 🏞️|river|rio|RÍ-ver
V: 🌴|trees|árvores|TRÍZ
V: 🏘️|village|vila|VÍ-lidj
V: 🛤️|road|estrada|RÔUD
V: 🪷|lake|lago|LÊIK
H: The boat goes along the river.|O barco vai ao longo do rio.
H: We walk along the river.|Nós andamos ao longo do rio.
H: The trees are along the bank.|As árvores ficam ao longo da margem.
H: The village is at the end of the road.|A vila fica no fim da estrada.
H: The lake is at the end of the river.|O lago fica no fim do rio.
L: Rose, the boat goes along the river.|Rose, o barco vai ao longo do rio.
L: Yes, Charlie. We walk along the river, too.|Sim, Charlie. Nós também andamos ao longo do rio.
L: Look! The trees are along the bank.|Olhe! As árvores ficam ao longo da margem.
L: Where is the village?|Onde fica a vila?
L: The village is at the end of the road.|A vila fica no fim da estrada.
L: And the lake?|E o lago?
L: The lake is at the end of the river.|O lago fica no fim do rio.
L: Then keep the boat steady, Charlie.|Então mantenha o barco firme, Charlie.
Q: Where does the boat go?|Por onde o barco vai?|0|🏞️ Along the river|🛤️ Along the road|🏘️ In the village
Q: Where are the trees?|Onde ficam as árvores?|2|🌴 Along the bank|🌴 At the lake|🌴 In the boat
Q: Where is the lake?|Onde fica o lago?|6|🏞️ At the end of the river|🛤️ At the end of the road|🏘️ In the village
B: steer|🛶|conduzir|I steer the boat.|He steers the boat.|She steered it well.|Ela o conduziu bem.
B: paddle|🚣|remar|I paddle along the river.|He paddles along the river.|They paddled all day.|Eles remaram o dia todo.
B: drift|🛶|ir à deriva|I drift on the river.|He drifts on the river.|The boat drifted slowly.|O barco foi à deriva devagar.
B: stop|🛑|parar|I stop at the village.|He stops at the village.|The boat stopped.|O barco parou.
LAB: bo|Laboratório de sons: boat, village e lake|Boat soa “BÔUT”, com oa = ôu. Village termina em idj, “VÍ-lidj”. Lake soa “LÊIK”, com a = êi.|Em lake, o a soa êi: LÊIK.
W: boat|BÔUT|barco|oa = ôu|bat|BÉT
W: village|VÍ-lidj|vila|age = idj|villain|VÍ-len
W: lake|LÊIK|lago|a = êi|like|LÁIK
G: 0|along|among|alone
G: 1|along|among|alone
G: 3|at the end of|at end of|in the end of
G: 4|at the end of|at end of|in the end of
X: 😊|Nice and calm|Calmo e tranquilo|comentar|Nice and calm, this river.|Calmo e tranquilo, este rio.
X: 🛶|Row harder|Reme mais forte|animar|Row harder, Charlie!|Reme mais forte, Charlie!
X: 😮|Look at that|Olhe aquilo|chamar atenção|Look at that, a village!|Olhe aquilo, uma vila!
X: 🙂|Almost there|Quase lá|avisar|Almost there, Rose.|Quase lá, Rose.
''')
