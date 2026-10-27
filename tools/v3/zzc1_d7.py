# Lote C do A1, dados 7 (n 80298 … 7910037). Ver zzc1_lib.py para o formato.
from v3.zzc1_lib import parse

N = []
N.append(parse("""
N 80298
C Matt,Coach | tommy,tom | O Matt e o Coach Taylor perguntam se a torcida está vibrando no jogo de futebol americano.
F Friday Night Lights | 📺 Série | 2006 | um seriado americano sobre um time de futebol americano de uma cidade pequena do Texas, o técnico Taylor e os jogadores, como Matt Saracen. | falar da torcida: cheer, clap e shout | park2 | 🏈,📣,🏟️
V 👥|crowd|torcida|KRÁUD
V 🏈|team|time|TÍIM
V ⚾|ball|bola|BÓL
V 🎉|touchdown|touchdown|TÂTCH-dáun
V 📣|cheer|torcida (vibração)|TCHÍIR
V 👏|clap|bater palmas|KLÉP
L Coach, are they cheering?|Coach, eles estão torcendo?
L Yes, the crowd is cheering.|Sim, a torcida está vibrando.
L The fans clap for the team.|Os torcedores batem palmas para o time.
L Listen to the cheer!|Escute a vibração!
L I throw the ball to Smash.|Eu jogo a bola para o Smash.
L Touchdown! Everybody shouts.|Touchdown! Todo mundo grita.
L They clap and cheer.|Eles batem palmas e vibram.
L Don’t shout at the referee!|Não grite com o juiz!
H 1,2,4,5,3
Q Is the crowd cheering?|A torcida está vibrando?|1|✅ Yes|❌ No|🤷 Maybe
Q Who claps for the team?|Quem bate palmas para o time?|2|👥 The fans|🧑‍🏫 The coach|🧑‍⚖️ The referee
Q What does the coach say at the end?|O que o coach diz no fim?|7|✋ Don’t shout at the referee|🎉 Shout more|🏃 Run fast
B cheer|📣|torcer|for the team|The fans cheer for the team.|Os torcedores torcem pelo time.
B clap|👏|bater palmas|for Matt|The crowd claps for Matt.|A torcida bate palmas para o Matt.
B shout|🗣️|gritar|at the field|Everybody shouts at the field.|Todo mundo grita para o campo.
B throw|🏈|jogar|the ball|Matt throws the ball.|O Matt joga a bola.
LAB ch|Em cheer, ch soa tch; em shout, sh soa ch e ou soa áu.|Cheer e chair têm sons diferentes.
W cheer|TCHÍIR|torcer|ch = tch|chair|TCHÉR
W clap|KLÉP|bater palmas|a = é|clip|KLÍP
W shout|XÁUT|gritar|sh = ch; ou = áu|shot|XÓT
G 0|is|are|am
G 1|clap|claps|clapping
G 3|shouts|shout|shouting
G 4|to|at|for
X 🏈|Go team!|Vai, time!|Incentiva o time.|Go team! We can win.|Vai, time! Nós podemos vencer.
X 💪|Come on!|Vamos lá!|Incentiva.|Come on! One more touchdown.|Vamos lá! Mais um touchdown.
X 👍|Nice throw!|Belo lançamento!|Elogia uma jogada.|Nice throw, Matt!|Belo lançamento, Matt!
X 🤩|What a game!|Que jogo!|Reage a um bom jogo.|What a game! The crowd is happy.|Que jogo! A torcida está feliz.
"""))

N.append(parse("""
N 7080298
C Dedede,Kirby | tom,tommy | O rei Dedede acha a cidade barulhenta e o Kirby leva a conversa para o prado tranquilo.
F Kirby | 🎮 Videogame | 1992 | uma série de jogos da Nintendo sobre Kirby, uma bolinha rosa que mora em Dream Land e enfrenta o rei Dedede. | descrever lugares barulhentos e tranquilos | park | 🌸,🌾,☁️
V 🏘️|town|cidade|TÁUN
V 🌾|meadow|prado|MÉ-dou
V 🤫|silence|silêncio|SÁI-lens
V 🐦|birds|pássaros|BÂRDZ
V 🥁|drums|tambores|DRÂMZ
V ☁️|cloud|nuvem|KLÁUD
L Kirby, the town is noisy.|Kirby, a cidade é barulhenta.
L The meadow is peaceful.|O prado é tranquilo.
L I love the silence.|Eu amo o silêncio.
L The birds sing softly.|Os pássaros cantam baixinho.
L The drums are loud in my castle.|Os tambores são altos no meu castelo.
L Stay calm, King Dedede.|Fique calmo, rei Dedede.
L It is calm here.|Aqui é calmo.
L Poyo! Let’s take a nap on a cloud.|Poyo! Vamos tirar uma soneca numa nuvem.
H 0,1,2,3,4
Q What is noisy?|O que é barulhento?|0|🏘️ The town|🌾 The meadow|☁️ The cloud
Q What do the birds do?|O que os pássaros fazem?|3|🐦 They sing softly|🥁 They play drums|😴 They sleep
Q What do they take at the end?|O que eles fazem no fim?|7|😴 A nap|🍰 A cake|🎮 A game
B hear|👂|ouvir|the birds|Kirby hears the birds.|O Kirby ouve os pássaros.
B love|❤️|amar|the silence|Dedede loves the silence.|O Dedede ama o silêncio.
B visit|🚶|visitar|the meadow|Kirby visits the meadow.|O Kirby visita o prado.
B stay|🧘|ficar|calm|Dedede stays calm.|O Dedede fica calmo.
LAB no|Em noisy, oi soa ói; em calm, o l não soa.|Noisy e nose têm sons diferentes.
W noisy|NÓI-zi|barulhento|oi = ói|nose|NÔUZ
W peaceful|PÍIS-ful|tranquilo|ea = íi|pace|PÊIS
W calm|KÁM|calmo|l mudo|come|KÂM
G 0|noisy|noise|noisily
G 1|peaceful|peace|peacefully
G 3|sing|sings|singing
G 4|are|is|am
X 🤫|Shh!|Silêncio!|Pede silêncio.|Shh! The birds sleep.|Silêncio! Os pássaros dormem.
X 😌|Relax.|Relaxe.|Pede calma.|Relax. The meadow is nice.|Relaxe. O prado é agradável.
X 🧘|Stay calm.|Fique calmo.|Acalma alguém.|Stay calm. It is only a drum.|Fique calmo. É só um tambor.
X 😄|Poyo!|Poyo!|Grito alegre do Kirby.|Poyo! I love the cloud.|Poyo! Eu amo a nuvem.
"""))

N.append(parse("""
N 7080299
C Peso,Barnacles | tom,tommy | O médico Peso manda o Capitão Barnacles pegar a toalha para não ficar molhado e ficar seco.
F Octonauts | 📺 Série infantil | 2010 | um seriado infantil sobre uma equipe de bichinhos exploradores do mar, como o capitão urso Barnacles e o médico pinguim Peso. | falar de molhado e seco | hall | 🐙,🌊,🧻
V 🧻|towel|toalha|TÁU-el
V 🧥|raincoat|capa de chuva|RÊIN-kout
V 🥾|boots|botas|BÚTS
V 💦|wet|molhado|UÉT
V 🌬️|dry|seco|DRÁI
V 🐻|fur|pelo|FÂR
L Captain, get a towel.|Capitão, pegue uma toalha.
L Why, Peso?|Por quê, Peso?
L Put on a raincoat. It is raining.|Vista uma capa de chuva. Está chovendo.
L My boots are wet.|As minhas botas estão molhadas.
L Your fur is wet too.|O seu pelo também está molhado.
L I do not want to get wet.|Eu não quero me molhar.
L Let it get dry. The towel is dry.|Deixe secar. A toalha está seca.
L Thank you. Now I am dry!|Obrigado. Agora estou seco!
H 0,2,3,4,6
Q What does Peso say to get?|O que o Peso manda pegar?|0|🧻 A towel|🧥 A coat|🥾 Boots
Q What is wet?|O que está molhado?|3|🥾 The boots|🧥 The raincoat|🧻 The towel
Q How is Barnacles at the end?|Como o Barnacles está no fim?|7|😊 Dry|💦 Wet|😴 Asleep
B get|🧻|pegar|a towel|Barnacles gets a towel.|O Barnacles pega uma toalha.
B dry|🌬️|secar|the fur|Peso dries the fur.|O Peso seca o pelo.
B put on|🧥|vestir|a raincoat|Barnacles puts on a raincoat.|O Barnacles veste uma capa de chuva.
B take off|🥾|tirar|the boots|Peso takes off the boots.|O Peso tira as botas.
LAB tw|Em towel, ow soa áu; em boots, oo soa ú.|Boots e boats têm sons diferentes.
W towel|TÁU-el|toalha|ow = áu|tower|TÁU-er
W boots|BÚTS|botas|oo = ú|boats|BÔUTS
W wet|UÉT|molhado|e = é|wit|UÍT
G 0|get|gets|getting
G 1|Put|Puts|Putting
G 2|are|is|am
G 4|dry|dries|drying
X 🏃|Hurry up!|Depressa!|Apressa alguém.|Hurry up! The rain is strong.|Depressa! A chuva está forte.
X 🙏|Thank you.|Obrigado.|Agradece.|Thank you for the towel.|Obrigado pela toalha.
X 😌|Don’t worry.|Não se preocupe.|Acalma alguém.|Don’t worry. It is only water.|Não se preocupe. É só água.
X ⚠️|Be careful.|Tenha cuidado.|Alerta alguém.|Be careful. The floor is wet.|Tenha cuidado. O chão está molhado.
"""))

N.append(parse("""
N 80300
C Wilma,Fred | misshoney,tom | A Wilma e o Fred contam o que fazem aos domingos e todo domingo em casa.
F The Flintstones | 📺 Série animada | 1960 | um desenho animado da Hanna-Barbera sobre a família da Idade da Pedra: Fred, Wilma, a filha Pebbles e os vizinhos Barney e Betty. | falar da rotina de domingo | living | 🦖,🪨,🏠
V 🎬|movie|filme|MÚ-vi
V 🍽️|dinner|jantar|DÍ-ner
V 🎂|cake|bolo|KÊIK
V 😴|nap|soneca|NÉP
V 👨‍👩‍👧|family|família|FÉ-mi-li
V 📅|Sunday|domingo|SÂN-dei
L Fred, we rest on Sundays.|Fred, nós descansamos aos domingos.
L Yes. We watch a movie every Sunday.|Sim. Nós assistimos a um filme todo domingo.
L Dinner is at six with Barney.|O jantar é às seis com o Barney.
L Betty bakes a cake every Sunday.|A Betty assa um bolo todo domingo.
L Pebbles takes a nap on Sundays.|A Pebbles tira uma soneca aos domingos.
L My family is here. Yabba dabba doo!|A minha família está aqui. Yabba dabba doo!
L Let’s eat dinner and cake.|Vamos comer o jantar e o bolo.
L Sunday at home is the best.|O domingo em casa é o melhor.
H 1,2,3,4,5
Q What do they watch every Sunday?|O que eles assistem todo domingo?|1|🎬 A movie|📺 The news|⚽ A game
Q Who bakes a cake?|Quem assa um bolo?|3|👩 Betty|👩 Wilma|👨 Fred
Q Who takes a nap?|Quem tira uma soneca?|4|👶 Pebbles|👨 Barney|🦖 Dino
B rest|😌|descansar|at home|Wilma rests at home.|A Wilma descansa em casa.
B bake|🎂|assar|a cake|Betty bakes a cake.|A Betty assa um bolo.
B watch|📺|assistir|a movie|Fred watches a movie.|O Fred assiste a um filme.
B visit|🤝|visitar|Barney|Fred visits Barney.|O Fred visita o Barney.
LAB mo|Em movie, ie soa i; em nap, a soa é.|Movie e money têm sons diferentes.
W movie|MÚ-vi|filme|ie = i|money|MÂ-ni
W nap|NÉP|soneca|a = é|nip|NÍP
W cake|KÊIK|bolo|a = êi|cook|KÚK
G 0|Sunday|Sundays|Mondays
G 1|at|on|in
G 2|bakes|bake|baking
G 3|on|in|at
X 🎉|Yabba dabba doo!|Yabba dabba doo!|Grito alegre do Fred.|Yabba dabba doo! It is Sunday.|Yabba dabba doo! É domingo.
X 😌|Relax.|Relaxe.|Pede calma.|Relax. It is Sunday.|Relaxe. É domingo.
X 💡|Good idea.|Boa ideia.|Aprova uma sugestão.|Good idea. Let’s watch a movie.|Boa ideia. Vamos assistir a um filme.
X 😋|Yum!|Hum, que bom!|Mostra que gostou.|Yum! The cake is sweet.|Hum, que bom! O bolo é doce.
"""))

N.append(parse("""
N 7080300
C Mom,Daniel | misshoney,tommy | A mamãe Tigre e o Daniel contam o que fizeram ontem: assistiram, cozinharam, limparam e brincaram.
F Daniel Tiger’s Neighborhood | 📺 Série infantil | 2012 | um seriado infantil da PBS sobre o tigrinho Daniel e a família dele, que aprendem pequenas lições do dia a dia no bairro. | contar o passado com verbos terminados em -ed | kitchen | 🐯,🏘️,🦉
V 📅|yesterday|ontem|IÉS-ter-dêi
V 📺|watched|assistiu|UÓTCHT
V 🍳|cooked|cozinhou|KÚKT
V 🧹|cleaned|limpou|KLÍIND
V 🎲|played|brincou|PLÊID
V 🏡|visited|visitou|VÍ-zi-tid
L Daniel, yesterday was fun.|Daniel, ontem foi divertido.
L Yes! I watched a movie.|Sim! Eu assisti a um filme.
L I cooked dinner.|Eu cozinhei o jantar.
L I cleaned my room.|Eu limpei o meu quarto.
L We played a game.|Nós brincamos de um jogo.
L We visited O the Owl.|Nós visitamos o Coruja O.
L I love our neighborhood.|Eu amo o nosso bairro.
L Today is fun too!|Hoje também é divertido!
H 0,1,2,3,4
Q What did Daniel watch?|O que o Daniel assistiu?|1|🎬 A movie|📚 A book|🎵 A song
Q Who cooked dinner?|Quem cozinhou o jantar?|2|👩 Mom|👦 Daniel|🦉 O the Owl
Q Who did they visit?|Quem eles visitaram?|5|🦉 O the Owl|👴 Grandpere|🐱 Katerina
B enjoy|😊|curtir|a movie|Daniel enjoys a movie.|O Daniel curte um filme.
B cook|🍳|cozinhar|dinner|Mom cooks dinner.|A mamãe cozinha o jantar.
B clean|🧹|limpar|my room|Daniel cleans his room.|O Daniel limpa o quarto dele.
B play|🎲|brincar de|a game|They play a game.|Eles brincam de um jogo.
LAB ed|Depois de som surdo, -ed soa t (watched, cooked); depois de som sonoro, soa d (cleaned).|Cooked e cook têm sons diferentes.
W watched|UÓTCHT|assistiu|ed = t|watch|UÓTCH
W cooked|KÚKT|cozinhou|ed = t|cook|KÚK
W cleaned|KLÍIND|limpou|ed = d|clean|KLÍIN
G 1|watched|watch|watching
G 2|cooked|cook|cooks
G 3|cleaned|clean|cleans
G 4|played|play|plays
X 🎉|Hooray!|Hurra!|Comemora.|Hooray! We cleaned the house.|Hurra! Nós limpamos a casa.
X 😊|It was fun.|Foi divertido.|Diz que gostou.|It was fun. I played all day.|Foi divertido. Eu brinquei o dia todo.
X 💕|I love you.|Eu te amo.|Mostra carinho.|I love you, Mom.|Eu te amo, mamãe.
X 🙌|Me too!|Eu também!|Concorda.|Me too! I loved it.|Eu também! Eu adorei.
"""))

N.append(parse("""
N 7910037
C London,Moseby | polly,tom | A London faz o check-in no hotel: tem reserva, mostra o passaporte e paga a conta.
F The Suite Life of Zack and Cody | 📺 Série | 2005 | um seriado de comédia da Disney sobre os gêmeos Zack e Cody, que moram num hotel chique de Boston com a herdeira London e o gerente Sr. Moseby. | fazer e confirmar uma reserva de hotel | lobby1 | 🏨,🛎️,🔑
V 📋|reservation|reserva|ré-zer-VÊI-xân
V 🛂|passport|passaporte|PÉS-pórt
V 🌙|night|noite|NÁIT
V 💳|credit card|cartão de crédito|KRÉ-dit KÁRD
V 🌆|view|vista|VIÚ
V 🧾|bill|conta|BÍL
L Good evening. Do you have a reservation?|Boa noite. Você tem reserva?
L Yes, I have a reservation.|Sim, eu tenho reserva.
L Show your passport, please.|Mostre o seu passaporte, por favor.
L Here it is. We stay one night.|Aqui está. Nós ficamos uma noite.
L The room has a view of the city.|O quarto tem vista para a cidade.
L How do I pay? I pay by credit card.|Como eu pago? Eu pago com cartão de crédito.
L Sorry, we are fully booked tomorrow.|Desculpe, estamos lotados amanhã.
L Okay. The bill, please.|Tudo bem. A conta, por favor.
H 1,2,3,5,4
Q Does London have a reservation?|A London tem reserva?|1|✅ Yes|❌ No|🤷 Maybe
Q How long do they stay?|Quanto tempo eles ficam?|3|🌙 One night|📅 One week|☀️ One day
Q How does London pay?|Como a London paga?|5|💳 By credit card|💵 By cash|🪙 By coin
B have|📋|ter|a reservation|London has a reservation.|A London tem uma reserva.
B show|🛂|mostrar|your passport|Moseby shows the desk.|O Moseby mostra o balcão.
B pay|💳|pagar|the bill|London pays the bill.|A London paga a conta.
B book|📅|reservar|a room|Moseby books a room.|O Moseby reserva um quarto.
LAB vi|Em view, ie soa iú; em night, igh soa ái.|View e few têm sons diferentes.
W view|VIÚ|vista|ie = iú|few|FIÚ
W night|NÁIT|noite|igh = ái|nut|NÂT
W bill|BÍL|conta|i = í|bell|BÉL
G 0|have|has|having
G 1|Show|Shows|Showing
G 2|stay|stays|staying
G 3|by|in|on
X 🌆|Good evening.|Boa noite (ao chegar).|Cumprimenta à noite.|Good evening. Welcome to the hotel.|Boa noite. Bem-vinda ao hotel.
X ⏳|One moment, please.|Um momento, por favor.|Pede para esperar.|One moment, please. I check.|Um momento, por favor. Eu verifico.
X 🙏|Sorry!|Desculpe!|Pede desculpa.|Sorry! The hotel is full.|Desculpe! O hotel está lotado.
X 👋|Welcome!|Bem-vinda!|Recebe alguém.|Welcome! Your room is ready.|Bem-vinda! O seu quarto está pronto.
"""))
