# Lote C do A1, dados 2 (n 7080255 … 7910033). Ver zzc1_lib.py para o formato.
from v3.zzc1_lib import parse

N = []
N.append(parse("""
N 7080255
C Baloo,Kit | tom,tommy | O piloto Baloo e o Kit embarcam, decolam, voam acima das nuvens e pousam.
F TaleSpin | 📺 Série animada | 1990 | um seriado animado da Disney sobre o urso Baloo, piloto de um avião de carga, e o menino Kit Cloudkicker, seu navegador. | falar das etapas de um voo | pier | ✈️,☁️,🐻
V ✈️|plane|avião|PLÊIN
V 🧑‍✈️|pilot|piloto|PÁI-lot
V 🛫|runway|pista|RÂN-uêi
V ☁️|clouds|nuvens|KLÁUDZ
V 🌪️|turbulence|turbulência|TÂR-biu-lens
V 💺|seat belt|cinto de segurança|SÍIT-bélt
L Kit, we board the plane at nine.|Kit, nós embarcamos no avião às nove.
L Look! The pilot says hello.|Olhe! O piloto diz olá.
L The plane takes off from the runway now.|O avião decola da pista agora.
L We fly above the clouds. Wow!|Nós voamos acima das nuvens. Uau!
L There is some turbulence. Hold on!|Há um pouco de turbulência. Segure firme!
L Where is my seat belt?|Cadê o meu cinto de segurança?
L Put on your seat belt. We land at noon.|Coloque o cinto. Nós pousamos ao meio-dia.
L I see the city. Let’s land, Baloo!|Eu vejo a cidade. Vamos pousar, Baloo!
H 0,1,2,3,4
Q When do they board the plane?|Quando eles embarcam no avião?|0|🕘 At nine|🕙 At ten|🕛 At noon
Q What do they fly above?|Sobre o que eles voam?|3|☁️ The clouds|🌊 The sea|🏔️ The mountains
Q When do they land?|Quando eles pousam?|6|🕛 At noon|🕘 At nine|🌙 At night
B board|🛫|embarcar|the plane|Baloo boards the plane.|O Baloo embarca no avião.
B take off|🛫|decolar|from the runway|The plane takes off.|O avião decola.
B fly|✈️|voar|above the clouds|Kit flies above the clouds.|O Kit voa acima das nuvens.
B land|🛬|pousar|at noon|They land at noon.|Eles pousam ao meio-dia.
LAB pl|Em plane, a soa êi; em clouds, ou soa áu.|Plane e plan têm sons diferentes.
W plane|PLÊIN|avião|a = êi|plan|PLÉN
W pilot|PÁI-lot|piloto|i = ái|pill|PÍL
W clouds|KLÁUDZ|nuvens|ou = áu|clues|KLÚZ
G 0|board|boards|boarding
G 1|says|say|saying
G 2|takes|take|taking
G 3|fly|flies|flying
X 🤩|Wow!|Uau!|Mostra admiração.|Wow! The sky is blue.|Uau! O céu é azul.
X ✋|Hold on!|Segure firme!|Avisa de um sacolejo.|Hold on! The plane moves.|Segure firme! O avião balança.
X 👋|Welcome aboard.|Bem-vindo a bordo.|Recebe os passageiros.|Welcome aboard. Take a seat.|Bem-vindo a bordo. Sente-se.
X 👀|Look!|Olhe!|Chama a atenção.|Look! I see the airport.|Olhe! Eu vejo o aeroporto.
"""))

N.append(parse("""
N 7080256
C Julie,Gopher | polly,tom | No navio, a Julie pede serviço de quarto e o Gopher cuida do cartão-chave e do despertar.
F The Love Boat | 📺 Série | 1977 | um seriado americano de comédia que se passa num navio de cruzeiro, com o capitão, o comissário Gopher e a diretora de cruzeiro Julie. | pedir serviços de hotel e de quarto | hall | 🚢,🛎️,🍽️
V 🛎️|room service|serviço de quarto|RÚM SÂR-vis
V 🔑|key card|cartão-chave|KÍI KÁRD
V ⏰|wake-up call|despertar|UÊIK-âp KÓL
V 🍽️|tray|bandeja|TRÊI
V 🧊|minibar|frigobar|MÍ-ni-bar
V 🥐|breakfast|café da manhã|BRÉK-fast
L Room service, please.|Serviço de quarto, por favor.
L Yes, Julie. What do you want?|Sim, Julie. O que você quer?
L A wake-up call at seven, please.|Um despertar às sete, por favor.
L Sure. And your key card?|Claro. E o seu cartão-chave?
L My key card doesn’t work.|O meu cartão-chave não funciona.
L Here is a new one. Put the tray outside.|Aqui está um novo. Ponha a bandeja do lado de fora.
L Thank you. The minibar is empty.|Obrigada. O frigobar está vazio.
L I bring breakfast to your room.|Eu levo o café da manhã ao seu quarto.
H 0,4,2,5,6
Q What time is the wake-up call?|A que horas é o despertar?|2|🕖 At seven|🕕 At six|🕗 At eight
Q What does not work?|O que não funciona?|4|🔑 The key card|🍽️ The tray|🧊 The minibar
Q What is empty?|O que está vazio?|6|🧊 The minibar|🍽️ The tray|🛏️ The bed
B order|🛎️|pedir|breakfast|Julie orders breakfast.|A Julie pede o café da manhã.
B serve|🍽️|servir|breakfast|Gopher serves breakfast.|O Gopher serve o café da manhã.
B wake|⏰|acordar|the guest|The call wakes the guest.|O despertar acorda a hóspede.
B leave|🚪|deixar|the tray outside|Julie leaves the tray outside.|A Julie deixa a bandeja do lado de fora.
LAB tr|Em tray, ay soa êi; em card, ar soa ár.|Tray e tree têm sons diferentes.
W tray|TRÊI|bandeja|ay = êi|tree|TRÍI
W card|KÁRD|cartão|ar = ár|cord|KÓRD
W service|SÂR-vis|serviço|ser = sâr|surface|SÂR-fis
G 0|service|serve|servant
G 1|doesn’t|don’t|isn’t
G 2|at|on|in
G 3|Put|Puts|Putting
X 🙂|At your service.|Às suas ordens.|Oferece ajuda com educação.|At your service. Anything else?|Às suas ordens. Mais alguma coisa?
X 🏃|Right away.|Agora mesmo.|Promete rapidez.|Right away. I bring the tray.|Agora mesmo. Eu levo a bandeja.
X 🙏|Thank you.|Obrigada.|Agradece o serviço.|Thank you. The breakfast is great.|Obrigada. O café da manhã está ótimo.
X 🤷|No problem.|Sem problema.|Responde a um pedido.|No problem. I fix the key card.|Sem problema. Eu arrumo o cartão-chave.
"""))

N.append(parse("""
N 7080260
C Ruby,Max | polly,tommy | É aniversário do Max: a Ruby ajuda a cortar o bolo, soprar as velas e fazer um desejo.
F Max and Ruby | 📺 Série animada | 2002 | um seriado infantil sobre dois irmãos coelhos, a mandona Ruby e o travesso Max, baseado nos livros de Rosemary Wells. | celebrar um aniversário | kitchen | 🎂,🎈,🐰
V 🎂|cake|bolo|KÊIK
V 🕯️|candles|velas|KÉN-dolz
V ⭐|wish|desejo|UÍSH
V 🎈|balloon|balão|ba-LÚN
V 🎶|song|canção|SÓNG
V 🔪|knife|faca|NÁIF
L Max, it is your birthday! We cut the cake.|Max, é o seu aniversário! Nós cortamos o bolo.
L Yummy! I see the candles.|Que delícia! Eu vejo as velas.
L Blow out the candles, Max.|Sopre as velas, Max.
L Wait, Ruby. I need a wish.|Espere, Ruby. Eu preciso de um desejo.
L Make a wish!|Faça um desejo!
L I wish for a red balloon.|Eu desejo um balão vermelho.
L Look! Pop the balloon, Max!|Olhe! Estoure o balão, Max!
L Now sing the birthday song!|Agora cante a canção de aniversário!
H 0,2,4,6,7
Q Whose birthday is it?|De quem é o aniversário?|0|👦 Max’s|👧 Ruby’s|👵 Grandma’s
Q What does Max need?|Do que o Max precisa?|3|⭐ A wish|🎈 A balloon|🔪 A knife
Q What do they sing?|O que eles cantam?|7|🎂 The birthday song|🌙 A lullaby|🎸 A rock song
B blow|💨|soprar|out the candles|Max blows out the candles.|O Max sopra as velas.
B make|⭐|fazer|a wish|Ruby makes a wish.|A Ruby faz um desejo.
B cut|🔪|cortar|the cake|Ruby cuts the cake.|A Ruby corta o bolo.
B sing|🎤|cantar|the birthday song|They sing the song.|Eles cantam a canção.
LAB ak|Em cake, a soa êi; em balloon, oo soa ú.|Cake e cook têm sons diferentes.
W cake|KÊIK|bolo|a = êi|cook|KÚK
W wish|UÍSH|desejo|i = í|which|UÍTCH
W balloon|ba-LÚN|balão|oo = ú|ballot|BÉ-lot
G 0|cut|cuts|cutting
G 1|Blow|Blows|Blowing
G 2|Make|Makes|Making
G 4|sing|sings|singing
X 🎉|Happy birthday|Feliz aniversário|Dá os parabéns.|Happy birthday, Max!|Feliz aniversário, Max!
X 😋|Yummy!|Que delícia!|Mostra que gostou da comida.|Yummy! I love this cake.|Que delícia! Eu amo este bolo.
X 🥳|Hooray!|Hurra!|Comemora.|Hooray! The party starts.|Hurra! A festa começa.
X 🙏|Thank you, Grandma.|Obrigado, vovó.|Agradece um presente.|Thank you, Grandma. It is great.|Obrigado, vovó. É ótimo.
"""))

N.append(parse("""
N 7910032
C Scrooge,Huey | tom,tommy | O Tio Patinhas leva o sobrinho Huey ao banco para abrir uma conta.
F Uncle Scrooge | 💬 Quadrinhos | 1952 | uma série de quadrinhos criada por Carl Barks sobre Scrooge McDuck, um pato riquíssimo e econômico, e os sobrinhos. | usar o banco: depositar, sacar e ver o saldo | office | 💰,🏦,🦆
V 🏦|bank|banco|BÉNK
V 📒|account|conta|a-KÁUNT
V 💵|deposit|depósito|di-PÓ-zit
V 🏧|withdraw|sacar|uidh-DRÓ
V 🧮|balance|saldo|BÉ-lans
V 🧑‍💼|teller|caixa|TÉ-ler
L Huey, we go to the bank today.|Huey, nós vamos ao banco hoje.
L I open an account, Uncle.|Eu abro uma conta, tio.
L Good! I deposit fifty dollars for you.|Bom! Eu deposito cinquenta dólares para você.
L Thank you! I withdraw twenty dollars.|Obrigado! Eu saco vinte dólares.
L Careful, Huey. What is your balance?|Cuidado, Huey. Qual é o seu saldo?
L Let me ask the teller.|Deixe-me perguntar ao caixa.
L The teller says: thirty dollars.|O caixa diz: trinta dólares.
L Great! Money in my account.|Ótimo! Dinheiro na minha conta.
H 0,1,2,3,4
Q What does Huey open?|O que o Huey abre?|1|📒 An account|🛍️ A shop|📬 A mailbox
Q How much does Huey withdraw?|Quanto o Huey saca?|3|2️⃣0️⃣ Twenty dollars|5️⃣0️⃣ Fifty dollars|3️⃣0️⃣ Thirty dollars
Q What is the balance?|Qual é o saldo?|6|3️⃣0️⃣ Thirty dollars|2️⃣0️⃣ Twenty dollars|5️⃣0️⃣ Fifty dollars
B open|🔓|abrir|an account|Huey opens an account.|O Huey abre uma conta.
B deposit|💵|depositar|fifty dollars|Scrooge deposits fifty dollars.|O Scrooge deposita cinquenta dólares.
B withdraw|🏧|sacar|twenty dollars|Huey withdraws twenty dollars.|O Huey saca vinte dólares.
B check|✅|conferir|the balance|The teller checks the balance.|O caixa confere o saldo.
LAB ac|Em account, ou soa áu; em bank, a soa é.|Bank e bunk têm sons diferentes.
W bank|BÉNK|banco|a = é|bunk|BÂNK
W account|a-KÁUNT|conta|ou = áu|amount|a-MÁUNT
W balance|BÉ-lans|saldo|a = é|silence|SÁI-lens
G 0|bank|bunk|bag
G 1|an|a|the
G 2|deposit|deposits|depositing
G 3|withdraw|withdraws|withdrawn
X 😟|Careful.|Cuidado.|Alerta alguém.|Careful. The money is not a toy.|Cuidado. O dinheiro não é brinquedo.
X 🙏|Thank you very much.|Muito obrigado.|Agradece com vontade.|Thank you very much, Uncle.|Muito obrigado, tio.
X 🙋|Let me ask.|Deixe-me perguntar.|Pede um tempo para perguntar.|Let me ask the teller.|Deixe-me perguntar ao caixa.
X 🎉|Great!|Ótimo!|Comemora uma boa notícia.|Great! I have money in the bank.|Ótimo! Eu tenho dinheiro no banco.
"""))

N.append(parse("""
N 7080261
C Steve,Mailbox | tom,polly | O Steve usa a Caixa de Correio para mandar uma carta, um pacote e um cartão-postal.
F Blue’s Clues | 📺 Série infantil | 1996 | um seriado infantil americano em que o apresentador e a cachorrinha azul Blue seguem pistas, com a ajuda de amigos como a Caixa de Correio. | usar o correio: carta, selo e pacote | lobby1 | 📬,🐶,✉️
V ✉️|letter|carta|LÉ-ter
V 📨|envelope|envelope|ÉN-ve-lôup
V 📦|package|pacote|PÉ-kidj
V 🖼️|postcard|cartão-postal|PÔUST-kard
V ⚖️|scale|balança|SKÊIL
V 🏷️|stamp|selo|STÉMP
L Hello, Mailbox! I send a letter.|Olá, Caixa de Correio! Eu envio uma carta.
L Put it in an envelope, Steve.|Ponha num envelope, Steve.
L Done! Now I need a stamp.|Pronto! Agora eu preciso de um selo.
L Put a stamp on the envelope.|Ponha um selo no envelope.
L I send a package too.|Eu envio um pacote também.
L Put it on the scale.|Ponha na balança.
L Look! A postcard from the lake.|Olhe! Um cartão-postal do lago.
L Blue sends a postcard to you!|A Blue manda um cartão-postal para você!
H 0,1,4,6,5
Q What does Steve send first?|O que o Steve envia primeiro?|0|✉️ A letter|📦 A package|🖼️ A postcard
Q Where does Steve put the package?|Onde o Steve põe o pacote?|5|⚖️ On the scale|📪 In the box|🪑 On the chair
Q Who sends a postcard?|Quem manda um cartão-postal?|7|🐶 Blue|🧑 Joe|📬 Mailbox
B send|📤|enviar|a letter|Steve sends a letter.|O Steve envia uma carta.
B stamp|🏷️|selar|the envelope|Mailbox stamps the envelope.|A Caixa de Correio sela o envelope.
B weigh|⚖️|pesar|the package|Steve weighs the package.|O Steve pesa o pacote.
B mail|📬|postar|a postcard|Blue mails a postcard.|A Blue posta um cartão-postal.
LAB le|Em letter, e soa é; em stamp, a soa é.|Letter e later têm sons diferentes.
W letter|LÉ-ter|carta|e = é|later|LÊI-ter
W stamp|STÉMP|selo|a = é|stomp|STÓMP
W package|PÉ-kidj|pacote|age = idj|passage|PÉ-sidj
G 0|send|sends|sent
G 1|Put|Puts|Putting
G 2|package|packet|page
G 3|from|to|at
X 🙌|Done!|Pronto!|Avisa que terminou.|Done! The letter is ready.|Pronto! A carta está pronta.
X ⏳|Wait a minute.|Espere um minuto.|Pede para esperar.|Wait a minute. I need a stamp.|Espere um minuto. Eu preciso de um selo.
X 🎶|Mail time!|Hora da correspondência!|Anuncia que chegou correspondência.|Mail time! I have a letter.|Hora da correspondência! Eu tenho uma carta.
X 🙏|Thanks for the help.|Obrigado pela ajuda.|Agradece a ajuda.|Thanks for the help, Mailbox.|Obrigado pela ajuda, Caixa de Correio.
"""))

N.append(parse("""
N 7080262
C Rosina,Figaro | polly,tom | A Rosina e o Fígaro combinam o teatro e perguntam a que horas tudo começa.
F The Barber of Seville | 🎭 Ópera | 1816 | uma ópera cômica de Rossini sobre Fígaro, um barbeiro esperto que ajuda o Conde Almaviva a conquistar Rosina. | perguntar a que horas algo começa | lobby1 | 🎭,💈,🎶
V 🕖|start|começo|STÁRT
V 🎟️|tickets|ingressos|TÍ-kets
V 💺|row|fileira|RÔU
V 🎭|curtain|cortina|KÂR-tin
V ☕|intermission|intervalo|ín-ter-MÍ-xân
V 🪑|seat|assento|SÍIT
L What time does it start, Figaro?|A que horas começa, Fígaro?
L It starts at seven thirty.|Começa às sete e meia.
L Do you have the tickets?|Você tem os ingressos?
L Yes. Two tickets, row ten.|Sim. Dois ingressos, fileira dez.
L What time does the curtain open?|A que horas a cortina abre?
L The curtain opens at eight.|A cortina abre às oito.
L And the intermission?|E o intervalo?
L The intermission starts at nine.|O intervalo começa às nove.
H 0,2,3,5,7
Q What time does the show start?|A que horas o espetáculo começa?|1|🕢 At seven thirty|🕗 At eight|🕘 At nine
Q Where are their seats?|Onde ficam os assentos deles?|3|🎟️ Row ten|🎟️ Row two|🎟️ Row five
Q When is the intermission?|Quando é o intervalo?|7|🕘 At nine|🕗 At eight|🕖 At seven
B start|🕖|começar|at seven thirty|The show starts at seven thirty.|O espetáculo começa às sete e meia.
B open|🎭|abrir|at eight|The curtain opens at eight.|A cortina abre às oito.
B sit|💺|sentar-se|in row ten|They sit in row ten.|Eles se sentam na fileira dez.
B buy|🎟️|comprar|two tickets|Figaro buys two tickets.|O Fígaro compra dois ingressos.
LAB tk|Em ticket, i soa í; em curtain, ur soa âr.|Curtain e carton têm sons diferentes.
W ticket|TÍ-ket|ingresso|i = í|thicket|THÍ-ket
W curtain|KÂR-tin|cortina|ur = âr|carton|KÁR-ton
W row|RÔU|fileira|ow = ôu|raw|RÓ
G 0|does|do|is
G 4|starts|start|starting
G 3|at|on|in
G 1|have|has|having
X ⏰|Hurry up!|Depressa!|Apressa alguém.|Hurry up! The show starts soon.|Depressa! O espetáculo começa logo.
X 😅|Just in time.|Bem na hora.|Diz que chegou a tempo.|Just in time. The curtain opens now.|Bem na hora. A cortina abre agora.
X 🙂|Not yet.|Ainda não.|Diz que ainda não começou.|Not yet. It starts at eight.|Ainda não. Começa às oito.
X 🎶|Enjoy the show!|Aproveite o espetáculo!|Deseja um bom espetáculo.|Enjoy the show, Rosina!|Aproveite o espetáculo, Rosina!
"""))

N.append(parse("""
N 7080264
C Tsubasa,Genzo | tommy,tom | O Tsubasa e o Genzo acompanham o jogo no estádio e dizem o placar.
F Captain Tsubasa | 💬 Mangá | 1981 | um mangá de Yoichi Takahashi sobre Tsubasa Ozora, um menino apaixonado por futebol, e o goleiro Genzo Wakabayashi. | dizer o placar de um jogo | park | ⚽,🏟️,📣
V ⚽|score|placar|SKÓR
V ⏸️|halftime|intervalo do jogo|HÉF-táim
V 🧑‍⚖️|referee|juiz|ré-fe-RÍI
V 🏟️|stadium|estádio|STÊI-di-um
V 📣|fans|torcedores|FÉNZ
V 🔔|whistle|apito|UÍ-sol
L What is the score, Genzo?|Qual é o placar, Genzo?
L The score is two to one.|O placar é dois a um.
L It is halftime now.|É o intervalo agora.
L The referee blows the whistle.|O juiz apita.
L The stadium is full of fans.|O estádio está cheio de torcedores.
L Our team scores! It is three to one.|O nosso time marca! É três a um.
L What a shot! Three to one!|Que chute! Três a um!
L The fans cheer. We win!|Os torcedores vibram. Nós vencemos!
H 1,2,3,4,7
Q What is the score first?|Qual é o placar no começo?|1|2️⃣ Two to one|3️⃣ Three to one|1️⃣ One to one
Q Who blows the whistle?|Quem apita?|3|🧑‍⚖️ The referee|🥅 The goalkeeper|📣 The fans
Q What is the score at the end?|Qual é o placar no fim?|6|3️⃣ Three to one|2️⃣ Two to two|1️⃣ One to zero
B kick|🦵|chutar|the ball|Tsubasa kicks the ball.|O Tsubasa chuta a bola.
B blow|💨|soprar|the whistle|The referee blows the whistle.|O juiz apita.
B clap|👏|aplaudir|for the team|The fans clap for the team.|Os torcedores aplaudem o time.
B watch|👀|assistir|the game|Genzo watches the game.|O Genzo assiste ao jogo.
LAB sc|Em score, or soa ór; em whistle, o t não soa.|Score e scar têm sons diferentes.
W score|SKÓR|placar|or = ór|scar|SKÁR
W whistle|UÍ-sol|apito|t mudo|wrist|RÍST
W stadium|STÊI-di-um|estádio|a = êi|stand|STÉND
G 0|to|at|of
G 1|is|are|am
G 2|blows|blow|blowing
G 4|cheer|cheers|cheered
X 🤩|What a shot!|Que chute!|Elogia uma jogada.|What a shot! It is a goal.|Que chute! É gol.
X 🎉|We win!|Nós vencemos!|Comemora a vitória.|We win! The score is four to two.|Nós vencemos! O placar é quatro a dois.
X 👏|Nice one!|Boa!|Elogia uma boa jogada.|Nice one, Tsubasa!|Boa, Tsubasa!
X 🔥|Come on!|Vamos lá!|Incentiva o time.|Come on! One more goal.|Vamos lá! Mais um gol.
"""))

N.append(parse("""
N 7080266
C Jessica,Seth | misshoney,tom | A Jessica e o Dr. Seth conversam sobre o que fizeram ontem, ontem à noite e na semana passada.
F Murder, She Wrote | 📺 Série | 1984 | um seriado americano sobre Jessica Fletcher, uma escritora de livros de mistério que resolve crimes de verdade com a ajuda do amigo Dr. Seth Hazlitt. | contar o que aconteceu no passado recente | home1 | 🔎,📓,🖋️
V 📅|yesterday|ontem|IÉS-ter-dêi
V 🌙|last night|ontem à noite|LÉST NÁIT
V 🗓️|last week|semana passada|LÉST UÍIK
V 📓|diary|diário|DÁI-a-ri
V 🧳|trip|viagem|TRÍP
V 🧠|memory|memória|MÉ-mo-ri
L Jessica, what did you do yesterday?|Jessica, o que você fez ontem?
L Yesterday I was at the library.|Ontem eu estive na biblioteca.
L And what did you do last night?|E o que você fez ontem à noite?
L Last night I watched a movie.|Ontem à noite eu assisti a um filme.
L Last week we went to the lake.|Na semana passada nós fomos ao lago.
L I know. I write it in my diary.|Eu sei. Eu escrevo isso no meu diário.
L You have a great memory!|Você tem uma ótima memória!
L Thank you. The trip was great.|Obrigada. A viagem foi ótima.
H 1,3,4,5,7
Q Where was Jessica yesterday?|Onde a Jessica esteve ontem?|1|📚 At the library|🏖️ At the beach|🏫 At school
Q What did Jessica watch last night?|O que a Jessica assistiu ontem à noite?|3|🎬 A movie|📺 The news|📖 A book
Q Where did they go last week?|Aonde eles foram na semana passada?|4|🏞️ To the lake|🏙️ To the city|🏫 To school
B visit|🏛️|visitar|the library|Jessica visited the library.|A Jessica visitou a biblioteca.
B watch|🎬|assistir|a movie|Seth watched a movie.|O Seth assistiu a um filme.
B write|✍️|escrever|in my diary|Jessica wrote in her diary.|A Jessica escreveu no diário dela.
B go|🚶|ir|to the lake|They went to the lake.|Eles foram ao lago.
LAB ni|Em night, igh soa ái; em diary, i soa ái.|Night e net têm sons diferentes.
W night|NÁIT|noite|igh = ái|net|NÉT
W diary|DÁI-a-ri|diário|i = ái|dairy|DÉ-ri
W memory|MÉ-mo-ri|memória|e = é|many|MÉ-ni
G 0|Yesterday|Tomorrow|Today
G 1|watched|watch|watching
G 2|went|go|goes
G 4|was|is|were
X 🤔|Let me think.|Deixe-me pensar.|Pede um tempo para lembrar.|Let me think. I was at home.|Deixe-me pensar. Eu estava em casa.
X 👍|Of course.|Claro.|Concorda sem dúvida.|Of course. I remember the trip.|Claro. Eu me lembro da viagem.
X 🧐|Are you sure?|Você tem certeza?|Duvida com educação.|Are you sure? It was last week.|Você tem certeza? Foi na semana passada.
X 💭|I remember.|Eu me lembro.|Diz que lembra de algo.|I remember. It was a nice day.|Eu me lembro. Foi um dia bonito.
"""))

N.append(parse("""
N 7080267
C Leo,Mikey | tom,tommy | O Leo e o Mikey pedem uma pizza online com entrega grátis.
F Teenage Mutant Ninja Turtles | 💬 Quadrinhos | 1984 | uma série de quadrinhos criada por Kevin Eastman e Peter Laird sobre quatro tartarugas ninja que vivem no esgoto e adoram pizza. | pedir online com entrega | shop | 🐢,🍕,🥷
V 🚚|delivery|entrega|di-LÍ-ve-ri
V 💲|shipping|frete|XÍ-ping
V 🛒|order|pedido|ÓR-der
V 📦|parcel|encomenda|PÁR-sol
V 📍|tracking|rastreio|TRÉ-king
V 🚪|doorstep|porta de casa|DÓR-step
L The delivery is free over twenty dollars.|A entrega é grátis acima de vinte dólares.
L Great! I order a pizza online.|Ótimo! Eu peço uma pizza online.
L Shipping is five dollars for a parcel.|O frete é cinco dólares por encomenda.
L I make an order for the team.|Eu faço um pedido para o time.
L Check the tracking. Is it near?|Veja o rastreio. Está perto?
L Yes! The parcel arrives soon.|Sim! A encomenda chega logo.
L They deliver to our door. Wait on the doorstep.|Eles entregam na nossa porta. Espere na porta de casa.
L Pizza is here! Thank you!|A pizza chegou! Obrigado!
H 0,2,3,5,4
Q What does Mikey order?|O que o Mikey pede?|1|🍕 A pizza|🍔 A burger|🥗 A salad
Q How much is shipping?|Quanto é o frete?|2|5️⃣ Five dollars|🔟 Ten dollars|🆓 It is free
Q Where do they wait?|Onde eles esperam?|6|🚪 On the doorstep|🛋️ On the sofa|🚗 In the car
B order|🛒|pedir|a pizza|Mikey orders a pizza.|O Mikey pede uma pizza.
B deliver|🚚|entregar|the parcel|They deliver the parcel.|Eles entregam a encomenda.
B ship|📦|enviar|the box|The shop ships the box.|A loja envia a caixa.
B track|📍|rastrear|the order|Leo tracks the order.|O Leo rastreia o pedido.
LAB or|Em order, or soa ór; em shipping, sh soa ch.|Shipping e sipping têm sons diferentes.
W order|ÓR-der|pedido|or = ór|odor|ÔU-der
W shipping|XÍ-ping|frete|sh = ch|sipping|SÍ-ping
W free|FRÍI|grátis|ee = íi|fray|FRÊI
G 0|free|fee|tree
G 1|is|are|am
G 2|make|makes|making
G 3|arrives|arrive|arriving
X 🙌|Awesome!|Demais!|Mostra empolgação.|Awesome! The pizza is hot.|Demais! A pizza está quente.
X 🕑|Right on time.|Bem na hora.|Elogia a pontualidade.|Right on time. The box is here.|Bem na hora. A caixa chegou.
X 🙄|No way!|Não acredito!|Mostra surpresa.|No way! The delivery is free.|Não acredito! A entrega é grátis.
X 🍕|Dig in!|Podem comer!|Convida para comer.|Dig in! There is a lot of pizza.|Podem comer! Tem muita pizza.
"""))

N.append(parse("""
N 7910033
C Roz,Frasier | polly,tom | A Roz tem uma ligação perdida e o Frasier ensina a deixar um recado.
F Frasier | 📺 Série | 1993 | uma comédia americana sobre Frasier Crane, um psiquiatra que faz um programa de rádio em Seattle, e sua família e colegas. | retornar ligações e deixar recados | hall | 📞,🎙️,📻
V 📬|voicemail|caixa postal|VÓIS-mêil
V 🔢|number|número|NÂM-ber
V 🚫|busy|ocupado|BÍ-zi
V 🔔|beep|bipe|BÍIP
V 📵|missed call|ligação perdida|MÍST KÓL
V 💬|message|recado|MÉ-sidj
L Frasier, I have a missed call.|Frasier, eu tenho uma ligação perdida.
L What is the number?|Qual é o número?
L It is Niles. The line is busy.|É o Niles. A linha está ocupada.
L Leave a voicemail, Roz.|Deixe uma mensagem de voz, Roz.
L I speak after the beep. Hi, Niles!|Eu falo depois do bipe. Oi, Niles!
L Say: “Please call me back.”|Diga: “Por favor, me ligue de volta.”
L Okay. I leave a message now.|Certo. Eu deixo um recado agora.
L Good. He calls back later.|Bom. Ele liga de volta depois.
H 3,1,2,4,0
Q Who has a missed call?|Quem tem uma ligação perdida?|0|👩 Roz|👨 Frasier|👴 Martin
Q Who is on the phone?|Quem está ao telefone?|2|🧔 Niles|👴 Martin|🐶 Eddie
Q What does Roz leave?|O que a Roz deixa?|6|💬 A message|🎁 A gift|🔑 A key
B call back|📞|ligar de volta|later|Roz calls back later.|A Roz liga de volta depois.
B leave|💬|deixar|a message|Roz leaves a message.|A Roz deixa um recado.
B listen|👂|ouvir|to the voicemail|Frasier listens to the voicemail.|O Frasier ouve a caixa postal.
B hang up|📴|desligar|the phone|Niles hangs up the phone.|O Niles desliga o telefone.
LAB bp|Em beep, ee soa íi; em busy, u soa i.|Busy e bus têm sons diferentes.
W beep|BÍIP|bipe|ee = íi|big|BÍG
W busy|BÍ-zi|ocupado|u = i|bus|BÂS
W message|MÉ-sidj|recado|age = idj|massage|ma-SÁJ
G 0|Leave|Leaves|Left
G 1|number|name|numb
G 2|busy|bus|buzzy
G 3|speak|speaks|speaking
X ⏳|Hold on.|Espere um pouco.|Pede para esperar.|Hold on. The line is busy.|Espere um pouco. A linha está ocupada.
X 👍|Of course.|Claro.|Aceita um pedido.|Of course. I call you back.|Claro. Eu ligo de volta para você.
X 👋|Talk to you later.|Falo com você depois.|Despede-se de quem está na linha.|Talk to you later, Roz.|Falo com você depois, Roz.
X 📞|Hello?|Alô?|Atende o telefone.|Hello? Who is it?|Alô? Quem é?
"""))
