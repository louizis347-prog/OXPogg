# Lote C do A1, dados 4 (n 7080301 … 7080317). Ver zzc1_lib.py para o formato.
from v3.zzc1_lib import parse

N = []
N.append(parse("""
N 7080301
C Usagi,Luna | polly,misshoney | A Usagi conta à gata Luna que chorou ontem, mas tentou de novo.
F Sailor Moon | 💬 Mangá | 1991 | um mangá de Naoko Takeuchi sobre Usagi, uma garota desastrada que vira guerreira, e a gata falante Luna, que a orienta. | contar o passado com verbos que terminam em y | living | 🌙,🐱,✨
V 😢|cried|chorou|KRÁID
V 🔁|tried|tentou|TRÁID
V 📖|studied|estudou|STÂ-did
V 👜|carried|carregou|KÉ-rid
V 🤗|hug|abraço|HÂG
V 💧|tear|lágrima|TÍR
L I cried yesterday, Luna.|Eu chorei ontem, Luna.
L Oh dear. Why?|Ai, que pena. Por quê?
L I tried again, but the test was hard.|Eu tentei de novo, mas a prova era difícil.
L Ami studied hard. She is smart.|A Ami estudou muito. Ela é inteligente.
L Mamoru carried my bag home.|O Mamoru carregou a minha bolsa até em casa.
L That was kind. Dry the tear on your face.|Que gentil. Seque a lágrima do seu rosto.
L Give me a hug, Luna.|Me dê um abraço, Luna.
L Of course. Now study with Ami!|Claro. Agora estude com a Ami!
H 0,2,3,4,6
Q What did Usagi do yesterday?|O que a Usagi fez ontem?|0|😢 She cried|😄 She laughed|😴 She slept
Q Who studied hard?|Quem estudou muito?|3|👩 Ami|👩 Usagi|🐱 Luna
Q Who carried the bag?|Quem carregou a bolsa?|4|🧑 Mamoru|👩 Ami|🐱 Luna
B cry|😢|chorar|at night|Usagi cries at night.|A Usagi chora à noite.
B try|🔁|tentar|again|She tries again.|Ela tenta de novo.
B study|📖|estudar|hard|Ami studies hard.|A Ami estuda muito.
B carry|👜|carregar|a bag|Mamoru carries a bag.|O Mamoru carrega uma bolsa.
LAB ie|Em cried e tried, ie soa ái; em hug, u soa â.|Cried e creed têm sons diferentes.
W cried|KRÁID|chorou|ie = ái|creed|KRÍID
W tried|TRÁID|tentou|ie = ái|tread|TRÉD
W hug|HÂG|abraço|u = â|hog|HÓG
G 0|cried|cry|crying
G 1|tried|try|tries
G 2|studied|studyed|studies
G 3|carried|carryed|carries
X 😢|Don’t cry.|Não chore.|Consola alguém.|Don’t cry. You can try again.|Não chore. Você pode tentar de novo.
X 💪|Cheer up!|Anime-se!|Anima alguém.|Cheer up! The test is over.|Anime-se! A prova acabou.
X 🙂|It’s okay.|Tudo bem.|Acalma alguém.|It’s okay. I am here.|Tudo bem. Eu estou aqui.
X 🙏|Thank you, Luna.|Obrigada, Luna.|Agradece a ajuda.|Thank you, Luna. You are kind.|Obrigada, Luna. Você é gentil.
"""))

N.append(parse("""
N 80302
C Thomas,Percy | tom,tommy | O Thomas e o Percy, dois trenzinhos, contam o que pararam, planejaram e deixaram cair.
F Thomas and Friends | 📺 Série infantil | 1984 | um seriado infantil inglês sobre a locomotiva azul Thomas e seus amigos, como Percy, baseado nos livros do reverendo W. Awdry. | contar o passado com verbos de consoante dobrada | school | 🚂,🛤️,🚉
V 🛑|stopped|parou|STÓPT
V 🗓️|planned|planejou|PLÉND
V 🐇|hopped|pulou|HÓPT
V ⬇️|dropped|deixou cair|DRÓPT
V 👏|clapped|aplaudiu|KLÉPT
V 👣|step|passo|STÉP
L The train stopped at the station.|O trem parou na estação.
L We planned a trip to the sea.|Nós planejamos uma viagem ao mar.
L A little rabbit hopped on the track.|Um coelhinho pulou nos trilhos.
L I dropped my red cap!|Eu deixei cair o meu boné vermelho!
L Don’t worry. Everyone clapped for us.|Não se preocupe. Todos aplaudiram para nós.
L Step in, friends. The trip starts!|Entrem, amigos. A viagem começa!
L We stopped at a bridge and waved.|Nós paramos numa ponte e acenamos.
L It was a fun day.|Foi um dia divertido.
H 0,1,2,3,4
Q Where did the train stop?|Onde o trem parou?|0|🚉 At the station|🌉 At a bridge|🏖️ At the sea
Q What did the rabbit do?|O que o coelho fez?|2|🐇 It hopped|💤 It slept|🏃 It ran
Q What did Percy drop?|O que o Percy deixou cair?|3|🧢 His cap|🔑 His key|🎒 His bag
B stop|🛑|parar|at the station|The train stops at the station.|O trem para na estação.
B plan|🗓️|planejar|a trip|Percy plans a trip.|O Percy planeja uma viagem.
B drop|⬇️|deixar cair|a cap|Percy drops a cap.|O Percy deixa cair um boné.
B clap|👏|bater palmas|for the train|The friends clap for the train.|Os amigos batem palmas para o trem.
LAB ed|Depois de p, o -ed soa t: stopped soa STÓPT; planned soa PLÉND.|Planned e plant têm sons diferentes.
W stopped|STÓPT|parou|ed = t|stop|STÓP
W planned|PLÉND|planejou|ed = d|plant|PLÉNT
W clapped|KLÉPT|aplaudiu|ed = t|clap|KLÉP
G 0|stopped|stoped|stopping
G 1|planned|planed|planning
G 2|hopped|hoped|hopping
G 3|dropped|droped|dropping
X 🚂|All aboard!|Todos a bordo!|Chama os passageiros.|All aboard! The train leaves now.|Todos a bordo! O trem sai agora.
X 👏|Well done!|Muito bem!|Elogia.|Well done, Thomas!|Muito bem, Thomas!
X 😮|What a surprise!|Que surpresa!|Reage a uma surpresa.|What a surprise! A rabbit!|Que surpresa! Um coelho!
X 🎉|Hooray!|Hurra!|Comemora.|Hooray! We are at the sea.|Hurra! Nós estamos no mar.
"""))

N.append(parse("""
N 7080302
C Tom,Jerry | tom,tommy | O gato Tom e o ratinho Jerry contam o que queriam, precisavam e esperavam.
F Tom and Jerry | 📺 Série animada | 1940 | um desenho animado clássico de Hanna e Barbera sobre o gato Tom, que tenta pegar o ratinho Jerry, mas sempre acaba em confusão. | ouvir o som id em wanted e needed | kitchen | 🐱,🐭,🧀
V 🙏|wanted|queria|UÓN-tid
V 🆘|needed|precisava|NÍI-did
V 🖌️|painted|pintou|PÊIN-tid
V ⏳|waited|esperou|UÊI-tid
V 🏁|started|começou|STÁR-tid
V 🧀|cheese|queijo|TCHÍIZ
L I wanted a little mouse.|Eu queria um ratinho.
L I needed some cheese.|Eu precisava de queijo.
L I painted a trap. It is red.|Eu pintei uma armadilha. Ela é vermelha.
L I waited behind the door.|Eu esperei atrás da porta.
L The chase started again!|A perseguição começou de novo!
L You wanted me. You needed a plan.|Você me queria. Você precisava de um plano.
L I wanted cheese too!|Eu também queria queijo!
L Okay, friend. Let’s share the cheese.|Tudo bem, amigo. Vamos dividir o queijo.
H 0,1,2,3,4
Q What did Tom want?|O que o Tom queria?|0|🐭 A mouse|🧀 Cheese|🐟 A fish
Q What did Tom paint?|O que o Tom pintou?|2|🪤 A trap|🏠 A house|🚪 A door
Q What do they share?|O que eles dividem?|7|🧀 Cheese|🐟 Fish|🥛 Milk
B want|🙏|querer|cheese|Jerry wants cheese.|O Jerry quer queijo.
B need|🆘|precisar de|a plan|Tom needs a plan.|O Tom precisa de um plano.
B paint|🖌️|pintar|a trap|Tom paints a trap.|O Tom pinta uma armadilha.
B wait|⏳|esperar|at the door|Jerry waits at the door.|O Jerry espera na porta.
LAB id|Depois de t ou d, o -ed soa id: wanted soa UÓN-tid.|Wanted e wonder têm sons diferentes.
W wanted|UÓN-tid|queria|ed = id|wonder|UÂN-der
W needed|NÍI-did|precisava|ed = id|noted|NÔU-tid
W painted|PÊIN-tid|pintou|ed = id|printed|PRÍN-tid
G 0|wanted|want|wants
G 1|needed|need|needs
G 2|painted|paint|paints
G 3|waited|wait|waits
X 🏃|Look out!|Cuidado!|Avisa de perigo.|Look out! Here comes the cat.|Cuidado! Lá vem o gato.
X 🎉|Hooray!|Hurra!|Comemora.|Hooray! I have the cheese.|Hurra! Eu tenho o queijo.
X 🤝|Let’s share.|Vamos dividir.|Propõe dividir.|Let’s share the milk.|Vamos dividir o leite.
X 😄|Okay, friend.|Tudo bem, amigo.|Faz as pazes.|Okay, friend. No more chase.|Tudo bem, amigo. Chega de perseguição.
"""))

N.append(parse("""
N 7080305
C Gena,Axel | polly,tom | A Gena corre de táxi para não chegar atrasada e o Axel avisa da multa por atraso.
F Crazy Taxi | 🎮 Videogame | 1999 | um jogo de corrida da Sega em que motoristas de táxi, como Axel e Gena, levam clientes depressa para ganhar dinheiro. | falar de atraso e de chegar na hora | hall | 🚕,⏰,🏙️
V ⏰|late|atrasado|LÊIT
V ✅|on time|na hora|ON TÁIM
V 💸|fee|taxa|FÍI
V 📅|deadline|prazo|DÉD-láin
V 🏃|hurry|pressa|HÂ-ri
V 🙇|excuse|desculpa|iks-KIÚS
L Axel, I am late!|Axel, estou atrasada!
L Hurry up! The customer waits.|Depressa! O cliente espera.
L Look! Now I am on time.|Olhe! Agora estou na hora.
L Good. If you are late, there is a late fee.|Bom. Se você chega atrasada, tem multa por atraso.
L The deadline is five o’clock.|O prazo é às cinco horas.
L No excuse, Gena. Be on time.|Sem desculpa, Gena. Chegue na hora.
L I know. I run to the taxi.|Eu sei. Eu corro até o táxi.
L Drive fast! We are on time!|Dirija rápido! Estamos na hora!
H 0,2,3,4,1
Q Is Gena late first?|A Gena está atrasada no começo?|0|✅ Yes, she is late|❌ No, she is on time|🤷 Maybe
Q What happens if you are late?|O que acontece se você chega atrasado?|3|💸 There is a late fee|🎁 There is a gift|🍕 There is a pizza
Q Is she on time at the end?|Ela está na hora no fim?|7|✅ Yes|❌ No|🤷 Maybe
B hurry|🏃|apressar-se|to the taxi|Gena hurries to the taxi.|A Gena se apressa até o táxi.
B drive|🚕|dirigir|fast|Axel drives fast.|O Axel dirige rápido.
B pay|💵|pagar|the fee|The customer pays the fee.|O cliente paga a taxa.
B forget|🤦|esquecer|the time|Gena forgets the time.|A Gena esquece a hora.
LAB la|Em late, a soa êi; em hurry, u soa â.|Late e let têm sons diferentes.
W late|LÊIT|atrasado|a = êi|let|LÉT
W fee|FÍI|taxa|ee = íi|few|FIÚ
W hurry|HÂ-ri|pressa|u = â|hairy|HÉ-ri
G 0|late|later|lately
G 1|on|in|at
G 2|fee|free|feet
G 4|Hurry|Hurries|Hurried
X ✋|Hold on!|Segure firme!|Avisa de uma curva.|Hold on! The taxi is fast.|Segure firme! O táxi é rápido.
X 🙅|No excuse.|Sem desculpa.|Não aceita uma desculpa.|No excuse. The clock is right.|Sem desculpa. O relógio está certo.
X 😅|Just in time.|Bem na hora.|Diz que chegou a tempo.|Just in time! The customer smiles.|Bem na hora! O cliente sorri.
X 🙏|Sorry!|Desculpe!|Pede desculpa.|Sorry! I am late again.|Desculpe! Estou atrasada de novo.
"""))

N.append(parse("""
N 7080307
C Pac-Man,Blinky | tommy,tom | O Pac-Man e o fantasma Blinky contam o que viram e o que comeram no labirinto.
F Pac-Man | 🎮 Videogame | 1980 | um jogo de fliperama da Namco em que o amarelo Pac-Man come bolinhas num labirinto e foge de fantasmas como Blinky e Pinky. | contar o passado com saw e ate | lake | 🟡,👻,🍒
V 👻|ghost|fantasma|GÔUST
V 🍒|cherry|cereja|TCHÉ-ri
V 🔵|dots|bolinhas|DÓTS
V 🍎|apple|maçã|Á-pol
V 🍓|strawberry|morango|STRÓ-bé-ri
V 🌀|maze|labirinto|MÊIZ
L I saw a ghost in the maze.|Eu vi um fantasma no labirinto.
L Boo! I saw a cherry.|Bu! Eu vi uma cereja.
L I ate the cherry. Yum!|Eu comi a cereja. Hum!
L We ate dots in the maze.|Nós comemos bolinhas no labirinto.
L I saw an apple too.|Eu vi uma maçã também.
L Pinky ate a strawberry.|A Pinky comeu um morango.
L I ate the apple. It is sweet.|Eu comi a maçã. Ela é doce.
L I saw you, Pac-Man. Wait for me!|Eu vi você, Pac-Man. Espere por mim!
H 0,2,3,4,5
Q What did Pac-Man see in the maze?|O que o Pac-Man viu no labirinto?|0|👻 A ghost|🍒 A cherry|🍎 An apple
Q What did Pac-Man eat first?|O que o Pac-Man comeu primeiro?|2|🍒 The cherry|🍓 A strawberry|🍎 An apple
Q Who ate a strawberry?|Quem comeu um morango?|5|👻 Pinky|🟡 Pac-Man|🔴 Blinky
B see|👀|ver|a ghost|Pac-Man sees a ghost.|O Pac-Man vê um fantasma.
B eat|🍒|comer|a cherry|He eats a cherry.|Ele come uma cereja.
B find|🔎|achar|a fruit|Blinky finds a fruit.|O Blinky acha uma fruta.
B chase|🏃|perseguir|the ghost|Pac-Man chases the ghost.|O Pac-Man persegue o fantasma.
LAB sa|Em saw, aw soa ó; em ate, a soa êi.|Ate e eat têm sons diferentes.
W saw|SÓ|viu|aw = ó|sew|SÔU
W ate|ÊIT|comeu|a = êi|eat|ÍIT
W cherry|TCHÉ-ri|cereja|ch = tch|sherry|XÉ-ri
G 0|saw|seen|seed
G 1|ate|eaten|eated
G 2|dots|dot|dogs
G 3|an|a|am
X 😋|Yum!|Hum, que bom!|Mostra que gostou.|Yum! The cherry is sweet.|Hum, que bom! A cereja é doce.
X 👻|Boo!|Bu!|Assusta de brincadeira.|Boo! I am a ghost.|Bu! Eu sou um fantasma.
X ⏳|Wait for me!|Espere por mim!|Pede para esperar.|Wait for me! I am slow.|Espere por mim! Eu sou lento.
X ⚠️|Look out!|Cuidado!|Avisa de perigo.|Look out! A ghost is here.|Cuidado! Tem um fantasma aqui.
"""))

N.append(parse("""
N 7910038
C Gordo,Lizzie | tom,polly | O Gordo e a Lizzie pegam o ônibus da escola e perguntam se o lugar está livre.
F Lizzie McGuire | 📺 Série | 2001 | um seriado americano sobre Lizzie, uma garota do ensino fundamental, e os melhores amigos Gordo e Miranda. | perguntar se o lugar está ocupado | street | 🚌,🎒,🏫
V 🚌|bus|ônibus|BÂS
V 💺|seat|lugar|SÍIT
V 🎒|backpack|mochila|BÉK-pék
V 🪟|window|janela|UÍN-dou
V 🚶|aisle|corredor|ÁIL
V 🧑‍✈️|driver|motorista|DRÁI-ver
L Lizzie, the bus is here!|Lizzie, o ônibus chegou!
L Is this seat taken?|Este lugar está ocupado?
L No, it’s free. Move my backpack.|Não, está livre. Tire a minha mochila.
L Thanks. I like the window.|Obrigada. Eu gosto da janela.
L I sit in the aisle.|Eu sento no corredor.
L The driver is nice today.|O motorista está simpático hoje.
L Yes. He says hello.|Sim. Ele diz olá.
L Look! Our school is next.|Olhe! A nossa escola é a próxima.
H 0,1,2,3,4
Q What does Lizzie ask?|O que a Lizzie pergunta?|1|💺 If the seat is taken|🚌 If the bus is late|🎒 If the bag is heavy
Q Where does Gordo sit?|Onde o Gordo senta?|4|🚶 In the aisle|🪟 At the window|🪑 At the back
Q Who is nice today?|Quem está simpático hoje?|5|🧑‍✈️ The driver|👩 Lizzie|🏫 The school
B sit|💺|sentar-se|at the window|Lizzie sits at the window.|A Lizzie senta na janela.
B take|🚌|pegar|the bus|Gordo takes the bus.|O Gordo pega o ônibus.
B move|🎒|tirar do lugar|the backpack|Gordo moves the backpack.|O Gordo tira a mochila do lugar.
B ask|❓|perguntar|a question|Lizzie asks a question.|A Lizzie faz uma pergunta.
LAB se|Em seat, ea soa íi; em aisle, o s não soa.|Seat e sit têm sons diferentes.
W seat|SÍIT|lugar|ea = íi|sit|SÍT
W aisle|ÁIL|corredor|s mudo|ill|ÍL
W window|UÍN-dou|janela|ow = ôu|winter|UÍN-ter
G 1|taken|take|taking
G 2|free|fee|three
G 0|is|are|am
G 3|like|likes|liking
X 🙋|Excuse me.|Com licença.|Chama a atenção com educação.|Excuse me. Is this seat free?|Com licença. Este lugar está livre?
X 🙏|Thanks!|Obrigada!|Agradece.|Thanks! You are kind.|Obrigada! Você é gentil.
X 🤷|No problem.|Sem problema.|Responde a um agradecimento.|No problem. Sit down.|Sem problema. Sente-se.
X 👍|Of course.|Claro.|Aceita um pedido.|Of course. Sit here.|Claro. Sente aqui.
"""))
