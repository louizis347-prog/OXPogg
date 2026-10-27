# Lote C do A1, dados 5 (n 7080309 … 7080317). Ver zzc1_lib.py para o formato.
from v3.zzc1_lib import parse

N = []
N.append(parse("""
N 7080309
C Epimetheus,Prometheus | tom,tommy | O titã Prometeu conta ao irmão o que pegou e o que deu aos humanos.
F Prometheus | 🏛️ Mito grego | Grécia antiga | um mito grego sobre o titã Prometeu, que pegou o fogo dos deuses e o deu aos humanos para eles não passarem frio. | contar o passado com took e gave | lake | 🔥,⛰️,🎁
V 🔥|fire|fogo|FÁI-er
V 🔦|torch|tocha|TÓRTCH
V ⛰️|mountain|montanha|MÁUN-tin
V 🎁|gift|presente|GÍFT
V 👥|people|pessoas|PÍI-pol
V 🌟|hope|esperança|HÔUP
L Brother, you took the fire!|Irmão, você pegou o fogo!
L Yes. I took a torch from the gods.|Sim. Eu peguei uma tocha dos deuses.
L You went up the mountain alone.|Você subiu a montanha sozinho.
L Yes. I gave the people a gift.|Sim. Eu dei um presente às pessoas.
L What gift?|Que presente?
L Fire. The people were cold.|Fogo. As pessoas estavam com frio.
L Zeus is angry with you.|Zeus está zangado com você.
L I took a risk, but I gave them hope.|Eu corri um risco, mas dei esperança a elas.
H 0,1,2,3,5
Q What did Prometheus take?|O que o Prometeu pegou?|1|🔥 A torch of fire|🍎 An apple|📷 A camera
Q Where did he go?|Aonde ele foi?|2|⛰️ Up the mountain|🌊 To the sea|🏠 Home
Q What did he give the people?|O que ele deu às pessoas?|5|🔥 Fire|🍞 Bread|💰 Gold
B take|🔥|pegar|the fire|Prometheus takes the fire.|O Prometeu pega o fogo.
B give|🎁|dar|a gift|He gives a gift.|Ele dá um presente.
B climb|🧗|escalar|the mountain|Prometheus climbs the mountain.|O Prometeu escala a montanha.
B carry|🔦|carregar|a torch|He carries a torch.|Ele carrega uma tocha.
LAB oo|Em took, oo soa ú; em gave, a soa êi.|Gave e give têm sons diferentes.
W took|TÚK|pegou|oo = ú|tuck|TÂK
W gave|GÊIV|deu|a = êi|give|GÍV
W fire|FÁI-er|fogo|ire = ái-er|fear|FÍ-er
G 0|took|take|taken
G 1|from|to|at
G 2|went|go|goes
G 3|gave|give|given
X ⚠️|Be careful.|Tenha cuidado.|Alerta alguém.|Be careful. The mountain is high.|Tenha cuidado. A montanha é alta.
X 🙏|Thank you, brother.|Obrigado, irmão.|Agradece ao irmão.|Thank you, brother. It is warm now.|Obrigado, irmão. Agora está quente.
X 🎁|What a gift!|Que presente!|Elogia um presente.|What a gift! Fire is great.|Que presente! O fogo é ótimo.
X 😱|Oh no!|Ai, não!|Mostra susto.|Oh no! The gods are angry.|Ai, não! Os deuses estão zangados.
"""))

N.append(parse("""
N 7080312
C Henry,Emma | tommy,polly | O Henry lê para a Emma um livro de contos que começa com “Once upon a time”.
F Once Upon a Time | 📺 Série | 2011 | um seriado americano em que personagens de contos de fadas, como Branca de Neve, vivem numa cidade onde a Emma e o menino Henry descobrem a verdade. | abrir uma história com “Once upon a time” | living | 📖,🏰,🐉
V 🤴|king|rei|KÍN
V 🏰|castle|castelo|KÉ-sol
V 🐉|dragon|dragão|DRÉ-gon
V 🌲|forest|floresta|FÓ-rest
V 📖|tale|conto|TÊIL
V ✨|magic|magia|MÉ-djik
L Emma, listen! Once upon a time, there was a king.|Emma, escute! Era uma vez um rei.
L A king? Where was his home?|Um rei? Onde era a casa dele?
L He lived in a castle.|Ele morava num castelo.
L And then?|E depois?
L One day, a dragon came.|Um dia, um dragão veio.
L Wow! Was the forest dark?|Uau! A floresta era escura?
L Yes. The forest was dark, but the queen had magic.|Sim. A floresta era escura, mas a rainha tinha magia.
L What a nice tale, Henry!|Que conto bonito, Henry!
H 0,2,4,5,7
Q Who was in the story?|Quem estava na história?|0|🤴 A king|🐉 A dragon|🧙 A witch
Q Where did the king live?|Onde o rei morava?|2|🏰 In a castle|🌲 In a forest|🏠 In a house
Q What came one day?|O que veio um dia?|4|🐉 A dragon|🧚 A fairy|🐺 A wolf
B live|🏰|morar|in a castle|The king lives in a castle.|O rei mora num castelo.
B come|🐉|vir|to the castle|A dragon comes to the castle.|Um dragão vem ao castelo.
B use|✨|usar|magic|The queen uses magic.|A rainha usa magia.
B read|📖|ler|a tale|Henry reads a tale.|O Henry lê um conto.
LAB ki|Em king, i soa í; em castle, o t não soa.|King e keen têm sons diferentes.
W king|KÍNG|rei|i = í|keen|KÍIN
W castle|KÉ-sol|castelo|t mudo|cattle|KÉ-tol
W dragon|DRÉ-gon|dragão|a = é|drag|DRÉG
G 0|Once|One|Ones
G 1|lived|live|living
G 2|day|days|dayly
G 3|Was|Were|Be
X 👂|Listen!|Escute!|Chama a atenção para ouvir.|Listen! This tale is good.|Escute! Este conto é bom.
X ❓|And then?|E depois?|Pede para continuar.|And then? Tell me more.|E depois? Conte mais.
X 🔚|The end.|Fim.|Termina a história.|The end. Good night.|Fim. Boa noite.
X 🤩|Wow!|Uau!|Mostra admiração.|Wow! A real dragon!|Uau! Um dragão de verdade!
"""))

N.append(parse("""
N 80313
C Sandy,Danny | polly,tom | A Sandy e o Danny lembram do verão passado, da praia e das músicas do ano passado.
F Grease | 🎭 Musical | 1971 | um musical de Jim Jacobs e Warren Casey sobre Danny e Sandy, que se conheceram no verão e se reencontram na escola. | falar do verão passado e do ano passado | lake | 🎵,🚗,🏖️
V ☀️|summer|verão|SÂ-mer
V 🏖️|beach|praia|BÍITCH
V 🌞|sun|sol|SÂN
V 🚗|car|carro|KÁR
V 🎵|song|canção|SÓNG
V 💃|dance|dançar|DÉNS
L Danny, last summer was great.|Danny, o verão passado foi ótimo.
L Yes! We went to the beach.|Sim! Nós fomos à praia.
L The sun was hot.|O sol estava quente.
L I had a car last year.|Eu tive um carro no ano passado.
L We sang a song in your car.|Nós cantamos uma música no seu carro.
L And we danced, Sandy.|E nós dançamos, Sandy.
L Last year I was far away.|No ano passado eu estava longe.
L Now you are here. Let’s dance!|Agora você está aqui. Vamos dançar!
H 0,1,2,3,4
Q Where did they go last summer?|Aonde eles foram no verão passado?|1|🏖️ To the beach|🏔️ To the mountains|🏙️ To the city
Q What did Danny have last year?|O que o Danny teve no ano passado?|3|🚗 A car|🚲 A bike|🏍️ A motorcycle
Q What did they sing?|O que eles cantaram?|4|🎵 A song|📖 A story|🎹 A piano
B go|🏖️|ir|to the beach|Sandy goes to the beach.|A Sandy vai à praia.
B sing|🎤|cantar|a song|Danny sings a song.|O Danny canta uma música.
B dance|💃|dançar|with Sandy|Danny dances with Sandy.|O Danny dança com a Sandy.
B drive|🚗|dirigir|a car|Danny drives a car.|O Danny dirige um carro.
LAB su|Em summer e sun, u soa â; em beach, ea soa íi.|Beach e peach têm sons diferentes.
W summer|SÂ-mer|verão|u = â|simmer|SÍ-mer
W beach|BÍITCH|praia|ea = íi|peach|PÍITCH
W sun|SÂN|sol|u = â|sin|SÍN
G 0|last|past|next
G 1|went|go|goes
G 3|year|years|yearly
G 4|sang|sing|sung
X 🧠|Remember?|Lembra?|Puxa uma lembrança.|Remember? It was a nice day.|Lembra? Foi um dia bonito.
X 🙌|Yes!|Sim!|Concorda com entusiasmo.|Yes! I remember the beach.|Sim! Eu me lembro da praia.
X 💃|Let’s dance!|Vamos dançar!|Chama alguém para dançar.|Let’s dance! The song is great.|Vamos dançar! A música é ótima.
X 🤩|Wow!|Uau!|Mostra admiração.|Wow! You are here!|Uau! Você está aqui!
"""))

N.append(parse("""
N 7080313
C Sherman,Peabody | tommy,tom | O Sherman e o Sr. Peabody falam de meses e anos na máquina do tempo.
F Peabody’s Improbable History | 📺 Série animada | 1959 | uma série de curtas animados em que o cachorro genial Mr. Peabody e o menino Sherman viajam no tempo para visitar fatos da história. | dizer quando: in + mês e in + ano | kitchen | ⏳,🐶,📅
V 📆|month|mês|MÂNTH
V 📅|June|junho|DJÚN
V 🗓️|year|ano|IÍR
V ❄️|December|dezembro|di-SÉM-ber
V 🍂|season|estação|SÍI-zon
V 🏖️|vacation|férias|vei-KÊI-xân
L Mr. Peabody, which month is it?|Sr. Peabody, que mês é este?
L It is June, Sherman.|É junho, Sherman.
L Great! My birthday is in June.|Ótimo! O meu aniversário é em junho.
L Good. The year is 2020.|Bom. O ano é 2020.
L Where do we go in December?|Aonde nós vamos em dezembro?
L To a snowy vacation.|A férias na neve.
L Which season is that?|Que estação é essa?
L Winter. It is a cold season.|Inverno. É uma estação fria.
H 0,2,3,4,7
Q Which month is it?|Que mês é?|1|📅 June|❄️ December|🍂 October
Q Which year is it?|Que ano é?|3|2️⃣0️⃣2️⃣0️⃣ 2020|2️⃣0️⃣1️⃣0️⃣ 2010|1️⃣9️⃣9️⃣0️⃣ 1990
Q What is winter?|O que é o inverno?|7|❄️ A cold season|☀️ A hot season|🌸 A spring month
B travel|⏳|viajar|in time|Peabody travels in time.|O Peabody viaja no tempo.
B celebrate|🎂|comemorar|my birthday|Sherman celebrates his birthday.|O Sherman comemora o aniversário.
B visit|🏛️|visitar|the past|They visit the past.|Eles visitam o passado.
B ask|❓|perguntar|the date|Sherman asks the date.|O Sherman pergunta a data.
LAB ju|Em June, u soa ú; em year, ea soa íi.|June e gene têm sons diferentes.
W June|DJÚN|junho|u = ú|gene|DJÍIN
W year|IÍR|ano|ea = íi|ear|ÍR
W December|di-SÉM-ber|dezembro|c = s|decimal|DÉ-si-mal
G 0|which|who|whose
G 1|in|on|at
G 3|in|on|at
G 2|is|are|am
X 🏃|Hurry up!|Depressa!|Apressa alguém.|Hurry up! The machine is ready.|Depressa! A máquina está pronta.
X 💡|Good idea.|Boa ideia.|Aprova uma sugestão.|Good idea. Let’s go to June.|Boa ideia. Vamos para junho.
X 🚀|Let’s go!|Vamos lá!|Anima o passeio.|Let’s go! The year is new.|Vamos lá! O ano é novo.
X 🤔|Really?|Sério?|Mostra surpresa.|Really? It is December?|Sério? É dezembro?
"""))

N.append(parse("""
N 7080316
C Alfred,Batman | tom,tommy | O Alfredo lembra ao Batman o que ele precisa e tem que fazer antes de sair.
F Batman | 💬 Quadrinhos | 1939 | uma série de quadrinhos da DC Comics sobre Bruce Wayne, que vira o herói Batman para proteger a cidade de Gotham, ajudado pelo mordomo Alfred. | falar de obrigações com need to e have to | kitchen | 🦇,🏙️,🚗
V 🍽️|dinner|jantar|DÍ-ner
V 🏙️|city|cidade|SÍ-ti
V 🧽|dishes|pratos|DÍ-xiz
V 🦇|cape|capa|KÊIP
V 🎭|mask|máscara|MÉSK
V 🚗|car|carro|KÁR
L Bruce, you have to eat dinner.|Bruce, você tem que jantar.
L I need to save the city tonight.|Eu preciso salvar a cidade esta noite.
L Then you need to wash the dishes.|Então você precisa lavar os pratos.
L Alfred, I have to wear my cape.|Alfred, eu tenho que vestir a minha capa.
L And you have to wear the mask too.|E você também tem que usar a máscara.
L I need to take the car.|Eu preciso pegar o carro.
L Be careful. Robin has to help you.|Tenha cuidado. O Robin tem que ajudar você.
L I have to go now. See you!|Eu tenho que ir agora. Até logo!
H 0,1,2,3,4
Q What does Alfred say first?|O que o Alfred diz primeiro?|0|🍽️ You have to eat dinner|🦇 You have to fly|🚗 You have to drive
Q What does Batman need to save?|O que o Batman precisa salvar?|1|🏙️ The city|🏠 His house|🐶 A dog
Q Who has to help Batman?|Quem tem que ajudar o Batman?|6|🐦 Robin|🤡 The Joker|🐱 Catwoman
B wash|🧽|lavar|the dishes|Alfred washes the dishes.|O Alfred lava os pratos.
B wear|🦇|vestir|a mask|Batman wears a mask.|O Batman veste uma máscara.
B save|🛟|salvar|the city|Batman saves the city.|O Batman salva a cidade.
B eat|🍽️|comer|dinner|Bruce eats dinner.|O Bruce janta.
LAB ca|Em cape, a soa êi; em mask, a soa é.|Cape e cap têm sons diferentes.
W cape|KÊIP|capa|a = êi|cap|KÉP
W mask|MÉSK|máscara|a = é|mark|MÁRK
W dinner|DÍ-ner|jantar|i = í|diner|DÁI-ner
G 0|have|has|having
G 1|to|for|at
G 2|need|needs|needing
G 4|wear|wears|wearing
X ⚠️|Be careful.|Tenha cuidado.|Alerta alguém.|Be careful. The city is dark.|Tenha cuidado. A cidade está escura.
X 👋|See you!|Até logo!|Despede-se.|See you! I go to work.|Até logo! Eu vou trabalhar.
X 🏃|Right away.|Agora mesmo.|Promete rapidez.|Right away, sir.|Agora mesmo, senhor.
X 🙂|Of course.|Claro.|Aceita um pedido.|Of course. I help you.|Claro. Eu ajudo você.
"""))

N.append(parse("""
N 7910039
C Rodolfo,Mimi | tom,polly | O Rodolfo espera o resultado do concurso de poemas e a Mimi cruza os dedos por ele.
F La Bohème | 🎭 Ópera | 1896 | uma ópera de Giacomo Puccini sobre os jovens artistas pobres Rodolfo, um poeta, e Mimi, que vivem e se amam em Paris. | torcer por alguém: fingers crossed e I hope so | school | 🍀,📜,🎶
V 🍀|luck|sorte|LÂK
V 🌟|hope|esperança|HÔUP
V 🤞|fingers|dedos|FÍN-gerz
V 📋|result|resultado|ri-ZÂLT
V 🏆|win|vencer|UÍN
V 📜|poem|poema|PÔU-em
L Mimi, I need luck today.|Mimi, eu preciso de sorte hoje.
L Why? Is it the poem contest?|Por quê? É o concurso de poemas?
L Yes. The result is today.|Sim. O resultado sai hoje.
L Will you win? Fingers crossed!|Você vai vencer? Dedos cruzados!
L I have hope. I hope so.|Eu tenho esperança. Espero que sim.
L Cross your fingers, Rodolfo. I cross mine.|Cruze os dedos, Rodolfo. Eu cruzo os meus.
L Look! The poem is on the list.|Olhe! O poema está na lista.
L You win! I hope you are happy.|Você venceu! Espero que esteja feliz.
H 0,4,5,2,7
Q What does Rodolfo need?|Do que o Rodolfo precisa?|0|🍀 Luck|💰 Money|🔑 A key
Q What is today?|O que acontece hoje?|2|📋 The result|🎂 A birthday|🚆 A train
Q Does Rodolfo win?|O Rodolfo vence?|7|✅ Yes|❌ No|🤷 Maybe
B hope|🤞|ter esperança|so|Rodolfo hopes so.|O Rodolfo espera que sim.
B cross|✋|cruzar|your fingers|Mimi crosses her fingers.|A Mimi cruza os dedos.
B win|🏆|vencer|the contest|Rodolfo wins the contest.|O Rodolfo vence o concurso.
B wait|⏳|esperar|for the result|They wait for the result.|Eles esperam o resultado.
LAB lu|Em luck, u soa â; em hope, o soa ôu.|Luck e lock têm sons diferentes.
W luck|LÂK|sorte|u = â|lock|LÓK
W hope|HÔUP|esperança|o = ôu|hop|HÓP
W fingers|FÍN-gerz|dedos|ng + g|singers|SÍN-gerz
G 0|need|needs|needed
G 1|hope|hopes|hoped
G 2|Cross|Crosses|Crossed
G 4|win|wins|won
X 🍀|Good luck!|Boa sorte!|Deseja sorte.|Good luck, Rodolfo!|Boa sorte, Rodolfo!
X 😮|Wow!|Uau!|Mostra surpresa.|Wow! I am on the list!|Uau! Eu estou na lista!
X 🤞|I hope so.|Espero que sim.|Responde com esperança.|I hope so. The result is good.|Espero que sim. O resultado é bom.
X 😌|Don’t worry.|Não se preocupe.|Acalma alguém.|Don’t worry. Your poem is great.|Não se preocupe. O seu poema é ótimo.
"""))

N.append(parse("""
N 7080317
C Gadd,Luigi | tom,tommy | O Professor Gadd dá ordens curtas ao Luigi na mansão: dê um passo, espere aqui, por aqui.
F Luigi’s Mansion | 🎮 Videogame | 2001 | um jogo da Nintendo em que o Luigi explora uma mansão cheia de fantasmas com a ajuda do Professor E. Gadd e de uma lanterna especial. | seguir ordens de lugar: step forward, wait here, this way | lobby1 | 👻,🔦,🏚️
V 🚪|door|porta|DÓR
V 🏛️|hall|corredor|HÓL
V ➡️|way|caminho|UÊI
V 🔦|flashlight|lanterna|FLÉSH-láit
V 🔑|key|chave|KÍI
V 👻|ghost|fantasma|GÔUST
L Step forward to the door, Luigi.|Dê um passo à frente até a porta, Luigi.
L The door is big and old.|A porta é grande e velha.
L Wait here. I check the hall.|Espere aqui. Eu vejo o corredor.
L I have a flashlight.|Eu tenho uma lanterna.
L Good. This way, please.|Bom. Por aqui, por favor.
L Is there a ghost in this room?|Tem um fantasma neste quarto?
L Wait here. Take the key.|Espere aqui. Pegue a chave.
L I have the key. Let’s go!|Eu tenho a chave. Vamos!
H 0,2,4,3,6
Q Where does Gadd say to step?|Para onde o Gadd diz para dar um passo?|0|🚪 To the door|🏛️ To the hall|🔑 To the key
Q What does Luigi have?|O que o Luigi tem?|3|🔦 A flashlight|🔑 A key|👻 A ghost
Q What does Luigi take?|O que o Luigi pega?|6|🔑 The key|🔦 The flashlight|🚪 The door
B step|👣|dar um passo|forward|Luigi steps forward.|O Luigi dá um passo à frente.
B wait|⏳|esperar|here|Gadd waits here.|O Gadd espera aqui.
B stand|🧍|ficar de pé|in the hall|Luigi stands in the hall.|O Luigi fica no corredor.
B show|👉|mostrar|the way|Gadd shows the way.|O Gadd mostra o caminho.
LAB do|Em door, oo soa ó; em ghost, o h não soa.|Door e dare têm sons diferentes.
W door|DÓR|porta|oo = ó|dare|DÉR
W hall|HÓL|corredor|a = ó|hull|HÂL
W ghost|GÔUST|fantasma|h mudo|goat|GÔUT
G 0|Step|Steps|Stepping
G 1|Wait|Waits|Waiting
G 2|way|where|what
G 3|have|has|having
X ⚠️|Be careful.|Tenha cuidado.|Alerta alguém.|Be careful. The hall is dark.|Tenha cuidado. O corredor está escuro.
X 🚀|Let’s go!|Vamos lá!|Chama para ir.|Let’s go! The door is open.|Vamos lá! A porta está aberta.
X 👉|Over here.|Aqui.|Mostra onde está algo.|Over here. I have the key.|Aqui. Eu tenho a chave.
X 👏|Good job!|Bom trabalho!|Elogia.|Good job, Luigi!|Bom trabalho, Luigi!
"""))
