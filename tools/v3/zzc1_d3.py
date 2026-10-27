# Lote C do A1, dados 3 (n 80271 … 7910035). Ver zzc1_lib.py para o formato.
from v3.zzc1_lib import parse

N = []
N.append(parse("""
N 80271
C Jughead,Archie | tom,tommy | O Jughead chama o Archie para jogar xadrez, e os dois contam no que são ruins.
F Archie | 💬 Quadrinhos | 1941 | uma série de quadrinhos americana sobre o adolescente Archie Andrews, seus amigos Jughead, Betty, Veronica e Reggie e a vida na cidade de Riverdale. | falar do que você faz mal | living | 🍔,📚,🎸
V ♟️|chess|xadrez|TCHÉS
V 🎤|singing|cantar|SÍN-guin
V ✏️|drawing|desenho|DRÓ-in
V ⚽|football|futebol|FÚT-bol
V 🍳|cooking|cozinhar|KÚ-kin
V 🏋️|practice|treino|PRÉK-tis
L Let’s play chess, Archie.|Vamos jogar xadrez, Archie.
L I’m bad at chess.|Eu sou ruim em xadrez.
L Then sing a song with Betty.|Então cante uma música com a Betty.
L I’m terrible at singing!|Eu sou péssimo em cantar!
L Draw a picture then.|Então desenhe um quadro.
L I’m bad at drawing.|Eu sou ruim em desenhar.
L Reggie is bad at football.|O Reggie é ruim em futebol.
L And Veronica is terrible at cooking. We need practice!|E a Veronica é péssima em cozinhar. Nós precisamos de treino!
H 1,3,5,6,7
Q What is Archie bad at?|Em que o Archie é ruim?|1|♟️ Chess|⚽ Football|🍳 Cooking
Q What is Archie terrible at?|Em que o Archie é péssimo?|3|🎤 Singing|🎨 Drawing|♟️ Chess
Q Who is bad at football?|Quem é ruim em futebol?|6|👦 Reggie|👩 Veronica|👱 Betty
B play|♟️|jogar|chess|Jughead plays chess.|O Jughead joga xadrez.
B sing|🎤|cantar|a song|Betty sings a song.|A Betty canta uma música.
B draw|✏️|desenhar|a picture|Archie draws a picture.|O Archie desenha um quadro.
B cook|🍳|cozinhar|dinner|Veronica cooks dinner.|A Veronica cozinha o jantar.
LAB ch|Em chess, ch soa tch; em cooking, oo soa ú.|Chess e chase têm sons diferentes.
W chess|TCHÉS|xadrez|ch = tch|chase|TCHÊIS
W terrible|TÉ-ri-bol|péssimo|e = é|terrific|te-RÍ-fik
W cooking|KÚ-kin|cozinhar|oo = ú|looking|LÚ-kin
G 0|at|in|on
G 1|terrible|terribly|terror
G 2|bad|badly|worse
G 3|is|are|am
X 🙌|Me neither!|Eu também não!|Concorda com uma frase negativa.|Me neither! I’m bad at football too.|Eu também não! Eu também sou ruim em futebol.
X 💪|Come on!|Vamos lá!|Incentiva alguém.|Come on! Try again.|Vamos lá! Tente de novo.
X 🤷|Why not?|Por que não?|Pergunta o motivo.|Why not? It is fun.|Por que não? É divertido.
X 😌|It’s okay.|Tudo bem.|Acalma alguém.|It’s okay. Practice is good.|Tudo bem. Treinar faz bem.
"""))

N.append(parse("""
N 7080271
C Dolly,Horace | polly,tom | A Dolly convida o Horace para o fim de semana e ele aceita com “I’d love to”.
F Hello, Dolly! | 🎭 Musical | 1964 | um musical da Broadway sobre Dolly Levi, uma casamenteira animada, e o rico e rabugento Horace Vandergelder. | aceitar convites com educação | living | 💃,🎩,🎶
V 🗓️|weekend|fim de semana|UÍIK-énd
V 🎶|concert|show|KÓN-sert
V 🚣|boat ride|passeio de barco|BÔUT RÁID
V 🍽️|dinner|jantar|DÍ-ner
V 📋|plans|planos|PLÉNZ
V 🆓|free|livre|FRÍI
L Horace, are you free this weekend?|Horace, você está livre neste fim de semana?
L Yes, I am free. Do you have plans?|Sim, estou livre. Você tem planos?
L Would you like a boat ride?|Você gostaria de um passeio de barco?
L I’d love to!|Eu adoraria!
L And I’d like to have dinner at eight.|E eu gostaria de jantar às oito.
L Dinner? I’d love to.|Jantar? Eu adoraria.
L Then we go to the concert after dinner.|Então vamos ao show depois do jantar.
L I’d love to go to the concert!|Eu adoraria ir ao show!
H 0,7,2,4,1
Q What does Dolly offer first?|O que a Dolly oferece primeiro?|2|🚣 A boat ride|🎶 A concert|🍽️ Dinner
Q What time is dinner?|A que horas é o jantar?|4|🕗 At eight|🕖 At seven|🕘 At nine
Q Where do they go after dinner?|Aonde eles vão depois do jantar?|6|🎶 To the concert|🎬 To the cinema|🏠 Home
B invite|💌|convidar|Horace|Dolly invites Horace.|A Dolly convida o Horace.
B accept|✅|aceitar|the invitation|Horace accepts the invitation.|O Horace aceita o convite.
B plan|🗓️|planejar|the weekend|They plan the weekend.|Eles planejam o fim de semana.
B meet|🤝|encontrar|at eight|Dolly meets Horace at eight.|A Dolly encontra o Horace às oito.
LAB co|Em concert, o soa ó; em love, o soa â.|Love e live têm sons diferentes.
W concert|KÓN-sert|show|con = kón|concern|kon-SÂRN
W dinner|DÍ-ner|jantar|i = í|diner|DÁI-ner
W love|LÂV|adorar|o = â|live|LÍV
G 0|this|that|these
G 1|to|for|at
G 2|Would|Do|Are
G 3|like|likes|liking
X 😍|Sounds great.|Parece ótimo.|Reage bem a um plano.|Sounds great. I’m free on Saturday.|Parece ótimo. Eu estou livre no sábado.
X 👋|See you then.|Até lá.|Combina o encontro.|See you then, Dolly.|Até lá, Dolly.
X 💡|What a nice idea!|Que boa ideia!|Elogia uma sugestão.|What a nice idea! A boat ride!|Que boa ideia! Um passeio de barco!
X 🙂|I’m free.|Estou livre.|Diz que tem tempo.|I’m free on Sunday.|Estou livre no domingo.
"""))

N.append(parse("""
N 7080275
C Courage,Muriel | tommy,misshoney | O cachorro Courage conta à Muriel que tem medo do escuro, de aranhas e de trovão.
F Courage the Cowardly Dog | 📺 Série animada | 1999 | um seriado animado sobre Courage, um cachorro medroso que protege seus donos, Muriel e Eustace, de monstros numa casa no meio do nada. | falar dos medos | bedroom | 🐶,🌙,🏚️
V 🌑|dark|escuro|DÁRK
V 🕷️|spider|aranha|SPÁI-der
V ⚡|thunder|trovão|THÂN-der
V 🐕|dog|cachorro|DÓG
V 🔦|nightlight|luz de noite|NÁIT-láit
V 💪|brave|corajoso|BRÊIV
L Muriel, I’m afraid of the dark.|Muriel, eu tenho medo do escuro.
L Here is a nightlight. Don’t be scared.|Aqui está uma luz de noite. Não fique com medo.
L Thank you. I’m scared of spiders too.|Obrigado. Eu também tenho medo de aranhas.
L Eustace is afraid of thunder.|O Eustace tem medo de trovão.
L I’m scared of big dogs!|Eu tenho medo de cachorros grandes!
L But you are a dog, Courage!|Mas você é um cachorro, Courage!
L Yes, but I’m a small dog.|Sim, mas eu sou um cachorro pequeno.
L Be brave. I am here with you.|Seja corajoso. Eu estou aqui com você.
H 0,2,3,4,1
Q What is Courage afraid of?|Do que o Courage tem medo?|0|🌑 The dark|🕷️ Cookies|🌞 The sun
Q Who is afraid of thunder?|Quem tem medo de trovão?|3|🧓 Eustace|👵 Muriel|🐶 Courage
Q What does Muriel give Courage?|O que a Muriel dá ao Courage?|1|🔦 A nightlight|🍪 A cookie|🛏️ A bed
B hug|🤗|abraçar|the dog|Muriel hugs the dog.|A Muriel abraça o cachorro.
B calm|😌|acalmar|Courage|Muriel calms Courage.|A Muriel acalma o Courage.
B protect|🛡️|proteger|the house|Courage protects the house.|O Courage protege a casa.
B hide|🙈|esconder-se|under the bed|Courage hides under the bed.|O Courage se esconde embaixo da cama.
LAB da|Em dark, ar soa ár; em spider, i soa ái.|Dark e duck têm sons diferentes.
W dark|DÁRK|escuro|ar = ár|duck|DÂK
W thunder|THÂN-der|trovão|th = língua entre os dentes|under|ÂN-der
W spider|SPÁI-der|aranha|i = ái|spinner|SPÍ-ner
G 0|of|from|at
G 1|scared|scare|scaring
G 2|afraid|fear|afraidly
G 4|Don’t|Not|No
X 😌|Don’t worry.|Não se preocupe.|Acalma alguém.|Don’t worry. I am here.|Não se preocupe. Eu estou aqui.
X 🫂|I’m here.|Eu estou aqui.|Mostra que está por perto.|I’m here. You are safe.|Eu estou aqui. Você está seguro.
X 💪|Be brave.|Seja corajoso.|Incentiva alguém.|Be brave. The dark is only a room.|Seja corajoso. O escuro é só um quarto.
X 😱|Oh no!|Ai, não!|Mostra susto.|Oh no! A big spider!|Ai, não! Uma aranha grande!
"""))

N.append(parse("""
N 80276
C Joe,Sam | tommy,polly | O Joe e a Sam escolhem um livro na biblioteca: capa mole ou capa dura?
F Wishbone | 📺 Série infantil | 1995 | um seriado americano em que um cachorrinho curioso, o Wishbone, imagina que vive as histórias dos livros que o amigo Joe lê. | falar das partes de um livro | school | 📚,🐶,📖
V ✍️|author|autor|Ó-thor
V 🏷️|title|título|TÁI-tol
V 🔖|chapter|capítulo|TCHÉP-ter
V 📘|paperback|livro de capa mole|PÊI-per-bék
V 📕|hardcover|livro de capa dura|HÁRD-kâ-ver
V 📄|page|página|PÊIDJ
L Who is the author, Sam?|Quem é o autor, Sam?
L Look at the cover. What is the title?|Olhe a capa. Qual é o título?
L The title is big. Read chapter one.|O título é grande. Leia o capítulo um.
L I prefer a paperback. It is light.|Eu prefiro um livro de capa mole. É leve.
L The hardcover is heavy.|O livro de capa dura é pesado.
L But the hardcover looks nice.|Mas o livro de capa dura é bonito.
L Wishbone likes the last page.|O Wishbone gosta da última página.
L Let’s borrow the paperback.|Vamos pegar emprestado o livro de capa mole.
H 0,1,2,3,4
Q What does Sam prefer?|O que a Sam prefere?|3|📘 A paperback|📕 A hardcover|📱 A phone
Q What is heavy?|O que é pesado?|4|📕 The hardcover|📘 The paperback|📄 The page
Q What do they borrow?|O que eles pegam emprestado?|7|📘 The paperback|📕 The hardcover|🎧 A CD
B read|📖|ler|chapter one|Joe reads chapter one.|O Joe lê o capítulo um.
B write|✍️|escrever|a book|The author writes a book.|O autor escreve um livro.
B choose|👆|escolher|a book|Sam chooses a book.|A Sam escolhe um livro.
B borrow|📚|pegar emprestado|a book|They borrow a book.|Eles pegam um livro emprestado.
LAB au|Em author, au soa ó e th soa t; em chapter, ch soa tch.|Author e offer têm sons diferentes.
W author|Ó-thor|autor|au = ó|offer|Ó-fer
W chapter|TCHÉP-ter|capítulo|ch = tch|catcher|KÉ-tcher
W paperback|PÊI-per-bék|livro de capa mole|pa = pêi|pepper|PÉ-per
G 0|Who|What|Where
G 2|Read|Reads|Reading
G 3|prefer|prefers|preferring
G 4|is|are|am
X 🤔|Let me see.|Deixe-me ver.|Pede um momento.|Let me see the cover.|Deixe-me ver a capa.
X 💡|Good idea.|Boa ideia.|Aprova uma sugestão.|Good idea. Let’s read it.|Boa ideia. Vamos ler.
X 😍|What a nice cover!|Que capa bonita!|Elogia um livro.|What a nice cover! It is blue.|Que capa bonita! Ela é azul.
X 🙋|Me too.|Eu também.|Concorda com o outro.|Me too. I like paperbacks.|Eu também. Eu gosto de livros de capa mole.
"""))

N.append(parse("""
N 7080276
C Cleo,Theo | polly,tommy | A Cleo conta ao Theo do que trata a história que ela leu na biblioteca dos leões.
F Between the Lions | 📺 Série infantil | 2000 | um seriado infantil americano passado numa biblioteca onde uma família de leões, como os filhotes Cleo e Theo, ama ler histórias. | resumir uma história | park2 | 🦁,📚,🎭
V 📖|story|história|STÓ-ri
V 🗺️|plot|enredo|PLÓT
V 🎭|character|personagem|KÉ-rek-ter
V 🏁|ending|final|ÉN-din
V 🦁|lion|leão|LÁI-on
V 🧭|adventure|aventura|ad-VÉN-tcher
L It is a great story, Theo.|É uma ótima história, Theo.
L What’s it about?|Sobre o que é?
L It’s about a brave lion.|É sobre um leão corajoso.
L The main character is a lion?|O personagem principal é um leão?
L Yes! The plot is simple.|Sim! O enredo é simples.
L Is it an adventure?|É uma aventura?
L Yes! I love the ending.|Sim! Eu amo o final.
L I want to read it now.|Eu quero ler agora.
H 0,4,3,6,2
Q What is the story about?|Sobre o que é a história?|2|🦁 A brave lion|🐋 A white whale|🐱 A little cat
Q Is the plot simple?|O enredo é simples?|4|✅ Yes, it is|❌ No, it is not|🤷 Maybe
Q What does Cleo love?|O que a Cleo ama?|6|🏁 The ending|🎬 The title|📖 The page
B tell|🗣️|contar|a story|Cleo tells a story.|A Cleo conta uma história.
B love|❤️|amar|the ending|Cleo loves the ending.|A Cleo ama o final.
B end|🏁|terminar|well|The story ends well.|A história termina bem.
B recommend|👍|recomendar|the book|Cleo recommends the book.|A Cleo recomenda o livro.
LAB st|Em story, o soa ó; em lion, i soa ái.|Story e store têm sons diferentes.
W story|STÓ-ri|história|o = ó|store|STÓR
W plot|PLÓT|enredo|o = ó|plate|PLÊIT
W lion|LÁI-on|leão|i = ái|lying|LÁI-in
G 4|about|at|of
G 0|is|are|am
G 3|love|loves|loving
G 2|main|man|many
X 😲|No way!|Não acredito!|Mostra surpresa.|No way! A lion in a book!|Não acredito! Um leão num livro!
X 🗣️|Tell me more.|Conte mais.|Pede mais detalhes.|Tell me more about the plot.|Conte mais sobre o enredo.
X 😄|Sounds fun!|Parece divertido!|Reage bem a uma história.|Sounds fun! I want to read it.|Parece divertido! Eu quero ler.
X ❤️|I love it.|Eu amo.|Diz que gostou muito.|I love it. The ending is good.|Eu amo. O final é bom.
"""))

N.append(parse("""
N 7910034
C Layton,Luke | tom,tommy | O Professor Layton e o Luke resolvem um enigma: a resposta está certa ou errada?
F Professor Layton | 🎮 Videogame | 2007 | uma série de jogos de enigmas em que o professor Hershel Layton e o jovem aprendiz Luke resolvem mistérios com quebra-cabeças. | dizer se uma resposta está certa ou errada | school | 🧩,🎩,🔎
V ✅|right|certo|RÁIT
V ❌|wrong|errado|RÓNG
V ☑️|correct|correto|ko-RÉKT
V 🤔|guess|palpite|GUÉS
V ⭐|point|ponto|PÓINT
V 🧩|puzzle|enigma|PÂ-zol
L Luke, solve this puzzle. What is the answer?|Luke, resolva este enigma. Qual é a resposta?
L It is just a guess. Is it five?|É só um palpite. É cinco?
L That is wrong. Try again.|Isso está errado. Tente de novo.
L Then it is six, Professor.|Então é seis, professor.
L You are right, Luke!|Você está certo, Luke!
L Is the answer correct? Do I get a point?|A resposta está correta? Eu ganho um ponto?
L Yes, it is correct. You get one point.|Sim, está correta. Você ganha um ponto.
L Thank you! I love a good puzzle.|Obrigado! Eu amo um bom enigma.
H 4,2,5,1,6
Q What is Luke’s first answer?|Qual é a primeira resposta do Luke?|1|5️⃣ Five|6️⃣ Six|2️⃣ Two
Q Is five right?|Cinco está certo?|2|❌ No, it is wrong|✅ Yes, it is right|🤷 Maybe
Q How many points does Luke get?|Quantos pontos o Luke ganha?|6|1️⃣ One|2️⃣ Two|0️⃣ None
B guess|🤔|adivinhar|the answer|Luke guesses the answer.|O Luke adivinha a resposta.
B solve|🧩|resolver|the puzzle|Layton solves the puzzle.|O Layton resolve o enigma.
B correct|✏️|corrigir|the mistake|Layton corrects the mistake.|O Layton corrige o erro.
B get|🎯|ganhar|a point|Luke gets a point.|O Luke ganha um ponto.
LAB wr|Em wrong, wr soa r; em guess, gu soa g.|Wrong e long têm sons diferentes.
W right|RÁIT|certo|igh = ái|rate|RÊIT
W wrong|RÓNG|errado|wr = r|long|LÓNG
W guess|GUÉS|palpite|gu = g|guest|GUÉST
G 0|right|left|light
G 1|is|are|am
G 3|guess|guest|guests
G 4|get|gets|getting
X 🔁|Try again.|Tente de novo.|Pede outra tentativa.|Try again. Think about it.|Tente de novo. Pense nisso.
X 👏|Well done!|Muito bem!|Elogia uma resposta certa.|Well done! The answer is six.|Muito bem! A resposta é seis.
X 🤏|Not quite.|Quase.|Diz que a resposta ainda não está certa.|Not quite. It is close.|Quase. Está perto.
X 🌟|Excellent!|Excelente!|Elogia com entusiasmo.|Excellent! You are a good student.|Excelente! Você é um bom aluno.
"""))

N.append(parse("""
N 80277
C Frasquita,Carmen | polly,misshoney | A Frasquita e a Carmen embaralham, distribuem e escolhem cartas à mesa.
F Carmen | 🎭 Ópera | 1875 | uma ópera de Georges Bizet sobre Carmen, uma mulher livre e corajosa na Espanha, que lê o futuro nas cartas com as amigas. | jogar baralho | living | 🃏,🎭,🌹
V 🃏|deck|baralho|DÉK
V 🂡|card|carta|KÁRD
V ♥️|hearts|copas|HÁRTS
V ♠️|spades|espadas|SPÊIDZ
V 🤡|joker|coringa|DJÔU-ker
V 🪑|table|mesa|TÊI-bol
L Carmen, shuffle the deck.|Carmen, embaralhe o baralho.
L Okay. Pick a card, Frasquita.|Certo. Escolha uma carta, Frasquita.
L I have the queen of hearts.|Eu tenho a dama de copas.
L I deal five cards. The ace of spades wins.|Eu distribuo cinco cartas. O ás de espadas ganha.
L Oh no! I have a joker.|Ai, não! Eu tenho um coringa.
L Put the cards on the table.|Ponha as cartas na mesa.
L Deal again, Carmen.|Distribua de novo, Carmen.
L Look at the cards. Love is a game!|Olhe as cartas. O amor é um jogo!
H 0,1,2,3,4
Q Who has the queen of hearts?|Quem tem a dama de copas?|2|👩 Frasquita|👩‍🦰 Carmen|🤴 Don José
Q Which card wins?|Qual carta ganha?|3|♠️ The ace of spades|♥️ The queen of hearts|🃏 The joker
Q What does Frasquita have?|O que a Frasquita tem?|4|🃏 A joker|♠️ A spade|👑 A king
B shuffle|🔀|embaralhar|the deck|Carmen shuffles the deck.|A Carmen embaralha o baralho.
B deal|🃏|distribuir|the cards|Carmen deals the cards.|A Carmen distribui as cartas.
B pick|👆|escolher|a card|Frasquita picks a card.|A Frasquita escolhe uma carta.
B win|🏆|ganhar|the game|The ace wins the game.|O ás ganha o jogo.
LAB de|Em deck, e soa é; em hearts, ear soa ár.|Deck e dock têm sons diferentes.
W deck|DÉK|baralho|e = é|dock|DÓK
W hearts|HÁRTS|copas|ear = ár|hurts|HÂRTS
W joker|DJÔU-ker|coringa|j = dj|joke|DJÔUK
G 0|shuffle|shuffles|shuffled
G 1|Pick|Picks|Picking
G 3|deal|deals|dealing
G 2|have|has|having
X 😱|Oh no!|Ai, não!|Mostra susto.|Oh no! The joker again!|Ai, não! O coringa de novo!
X 👀|Look!|Olhe!|Chama a atenção.|Look! I have the ace.|Olhe! Eu tenho o ás.
X 🔁|Again!|De novo!|Pede mais uma rodada.|Again! I want to play.|De novo! Eu quero jogar.
X 🍀|Good luck.|Boa sorte.|Deseja sorte.|Good luck with the cards.|Boa sorte com as cartas.
"""))

N.append(parse("""
N 7080277
C Luigi,Mario | tommy,tom | O Luigi e o Mario jogam num tabuleiro e combinam de quem é a vez.
F Mario Party | 🎮 Videogame | 1998 | um jogo de tabuleiro para vários jogadores da Nintendo, em que Mario, Luigi e amigos rolam dados e disputam minijogos para ganhar estrelas. | combinar de quem é a vez | living | 🎲,⭐,🍄
V 🔁|turn|vez|TÂRN
V 🎲|dice|dado|DÁIS
V 🧩|board|tabuleiro|BÓRD
V 🪙|coins|moedas|KÓINZ
V ⭐|star|estrela|STÁR
V 📜|rules|regras|RÚLZ
L Whose turn is it, Mario?|De quem é a vez, Mario?
L It is my turn!|É a minha vez!
L Roll the dice, then.|Então jogue o dado.
L A six! I move on the board.|Um seis! Eu ando no tabuleiro.
L Now it is my turn. I have ten coins.|Agora é a minha vez. Eu tenho dez moedas.
L Look! A star is on the board.|Olhe! Tem uma estrela no tabuleiro.
L The rules say: the star wins.|As regras dizem: a estrela vence.
L Your turn again, Luigi. Good luck!|Sua vez de novo, Luigi. Boa sorte!
H 0,2,3,4,5
Q What does Mario have?|O que o Mario tira?|3|6️⃣ A six|5️⃣ A five|1️⃣ A one
Q How many coins does Luigi have?|Quantas moedas o Luigi tem?|4|🔟 Ten|5️⃣ Five|2️⃣ Two
Q What is on the board?|O que tem no tabuleiro?|5|⭐ A star|🍄 A mushroom|🏁 A flag
B play|🎮|jogar|a game|Mario plays a game.|O Mario joga um jogo.
B roll|🎲|rolar|the dice|Mario rolls the dice.|O Mario rola o dado.
B move|🚶|andar|on the board|Luigi moves on the board.|O Luigi anda no tabuleiro.
B take|🪙|pegar|a coin|Luigi takes a coin.|O Luigi pega uma moeda.
LAB tu|Em turn, ur soa âr; em dice, i soa ái.|Dice e dose têm sons diferentes.
W turn|TÂRN|vez|ur = âr|torn|TÓRN
W dice|DÁIS|dado|i = ái|dose|DÔUS
W coins|KÓINZ|moedas|oi = ói|cones|KÔUNZ
G 0|Whose|Who|Who’s
G 1|Roll|Rolls|Rolling
G 2|move|moves|moving
G 3|my|me|mine
X 🍀|Good luck!|Boa sorte!|Deseja sorte.|Good luck, Mario!|Boa sorte, Mario!
X 🚀|Let’s go!|Vamos lá!|Anima o jogo.|Let’s go! I roll the dice.|Vamos lá! Eu jogo o dado.
X 🤩|Wow!|Uau!|Mostra admiração.|Wow! A big star!|Uau! Uma estrela grande!
X 😤|Not fair!|Não vale!|Reclama de uma jogada.|Not fair! You have more coins.|Não vale! Você tem mais moedas.
"""))

N.append(parse("""
N 7080278
C GLaDOS,Chell | polly,tom | A Chell descobre sozinha como resolver o enigma do cubo, do botão e da porta.
F Portal | 🎮 Videogame | 2007 | um jogo de enigmas da Valve em que a personagem Chell usa uma arma de portais para fugir de um laboratório controlado pela voz de GLaDOS. | descobrir e resolver enigmas | office | 🔵,🟠,🧊
V 🧩|puzzle|enigma|PÂ-zol
V 🧊|cube|cubo|KIÚB
V 🔘|button|botão|BÂ-ton
V 🚪|door|porta|DÓR
V 💡|solution|solução|so-LÚ-xân
V 🌀|portal|portal|PÓR-tal
L Chell, solve the puzzle.|Chell, resolva o enigma.
L I can figure out the door.|Eu consigo descobrir a porta.
L Pick up the cube.|Pegue o cubo.
L I put the cube on the button.|Eu ponho o cubo no botão.
L The door opens. Work out the portal.|A porta abre. Descubra o portal.
L I work out the portal. It is easy.|Eu descubro o portal. É fácil.
L Here is the solution.|Aqui está a solução.
L No, thanks. I figure it out.|Não, obrigada. Eu descubro sozinha.
H 0,2,3,1,6
Q What does Chell put on the button?|O que a Chell põe no botão?|3|🧊 The cube|🌀 The portal|🔑 A key
Q What opens?|O que abre?|4|🚪 The door|📦 The cube|🔘 The button
Q Does Chell want the solution?|A Chell quer a solução?|7|❌ No, she figures it out|✅ Yes, please|🤷 Maybe
B solve|🧩|resolver|the puzzle|Chell solves the puzzle.|A Chell resolve o enigma.
B figure out|💡|descobrir|the door|She figures out the door.|Ela descobre a porta.
B work out|🧠|descobrir|the portal|Chell works out the portal.|A Chell descobre o portal.
B pick up|📦|pegar|the cube|Chell picks up the cube.|A Chell pega o cubo.
LAB cu|Em cube, u soa iú; em button, u soa â.|Cube e cob têm sons diferentes.
W cube|KIÚB|cubo|u = iú|cob|KÓB
W button|BÂ-ton|botão|u = â|baton|ba-TÓN
W door|DÓR|porta|oo = ó|dare|DÉR
G 0|solve|solves|solved
G 3|figure|figures|figuring
G 1|cube|cup|cute
G 4|solution|solve|solving
X 👏|Well done.|Muito bem.|Elogia quem conseguiu.|Well done. The door is open.|Muito bem. A porta está aberta.
X 👌|Not bad.|Nada mal.|Elogia sem exagero.|Not bad. That is a hard puzzle.|Nada mal. Esse enigma é difícil.
X ✋|Let me try.|Deixe-me tentar.|Pede para tentar.|Let me try the button.|Deixe-me tentar o botão.
X 😎|Easy!|Fácil!|Diz que foi fácil.|Easy! I solve it fast.|Fácil! Eu resolvo rápido.
"""))

N.append(parse("""
N 7080280
C Dick,Muttley | tom,tommy | O Dick Dastardly está na frente na corrida, mas a rival vem logo atrás.
F Wacky Races | 📺 Série animada | 1968 | um seriado animado da Hanna-Barbera sobre uma corrida maluca de carros, em que o vilão Dick Dastardly e o cachorro Muttley tentam trapacear. | narrar quem está na frente e quem está atrás | street | 🏎️,🏁,🏆
V 🏁|lead|liderança|LÍID
V 👥|crowd|multidão|KRÁUD
V 🏆|trophy|troféu|TRÔU-fi
V 🏎️|rival|rival|RÁI-val
V 💨|sprint|arrancada|SPRÍNT
V ⛰️|hill|ladeira|HÍL
L Muttley, I am in the lead!|Muttley, eu estou na frente!
L The crowd cheers for you, boss.|A multidão torce por você, chefe.
L I want the trophy!|Eu quero o troféu!
L Your rival Penelope is behind us.|Sua rival Penelope está atrás de nós.
L She tries to catch up. Start the sprint!|Ela tenta nos alcançar. Comece a arrancada!
L Up the hill, boss. Faster!|Subindo a ladeira, chefe. Mais rápido!
L Now we are far in the lead.|Agora estamos bem na frente.
L We win! Hee, hee, hee!|Nós vencemos! Hi, hi, hi!
H 0,1,2,3,4
Q Who is in the lead?|Quem está na frente?|0|😈 Dick|👩 Penelope|🐶 Muttley
Q Who is behind them?|Quem está atrás deles?|3|👩 Penelope|🐶 The dog|👥 The crowd
Q Who wins?|Quem vence?|7|😈 Dick and Muttley|👩 Penelope|🚗 Nobody
B lead|🏁|liderar|the race|Dick leads the race.|O Dick lidera a corrida.
B follow|🚗|seguir|the car|Penelope follows the car.|A Penelope segue o carro.
B catch up|🏃|alcançar|the rival|She catches up with the rival.|Ela alcança o rival.
B win|🏆|ganhar|the trophy|Muttley wins the trophy.|O Muttley ganha o troféu.
LAB le|Em lead, ea soa íi; em hill, i soa í.|Lead e lid têm sons diferentes.
W lead|LÍID|liderar|ea = íi|lid|LÍD
W hill|HÍL|ladeira|i = í|heel|HÍIL
W sprint|SPRÍNT|arrancada|spr + int|print|PRÍNT
G 0|lead|led|load
G 1|cheers|cheer|cheering
G 3|behind|before|beside
G 4|catch|catches|catching
X 🚀|Faster!|Mais rápido!|Pede velocidade.|Faster! The rival is near.|Mais rápido! A rival está perto.
X 🎉|We win!|Nós vencemos!|Comemora a vitória.|We win! The trophy is mine.|Nós vencemos! O troféu é meu.
X 👀|Look!|Olhe!|Chama a atenção.|Look! A big hill!|Olhe! Uma ladeira grande!
X 😤|Not fair!|Não vale!|Reclama de uma jogada.|Not fair! She is fast.|Não vale! Ela é rápida.
"""))

N.append(parse("""
N 7080282
C Will,Carlton | tommy,tom | O Will chega novo na escola e o Carlton mostra o corredor, a cantina e o ginásio.
F The Fresh Prince of Bel-Air | 📺 Série | 1990 | um seriado americano de comédia sobre Will, um jovem da Filadélfia que vai morar com os tios ricos em Bel-Air e entra numa escola nova. | se apresentar como novo e pedir ajuda | school | 🏫,🎒,🏀
V 🛤️|hallway|corredor|HÓL-uêi
V 🍽️|cafeteria|cantina|ké-fe-TÍ-ri-a
V 🏀|gym|ginásio|DJÍM
V 🧑‍🏫|principal|diretor|PRÍN-si-pal
V 🆕|new student|aluno novo|NIÚ STIÚ-dent
V 🧭|lost|perdido|LÓST
L Hi, I’m new here. I am a new student.|Oi, sou novo aqui. Sou um aluno novo.
L Welcome to Bel-Air Academy!|Bem-vindo à Bel-Air Academy!
L Can you show me around?|Você pode me mostrar o lugar?
L Sure. The hallway is long.|Claro. O corredor é longo.
L Where is the cafeteria?|Onde fica a cantina?
L The cafeteria is downstairs.|A cantina fica no andar de baixo.
L Where is the gym? I am lost.|Onde fica o ginásio? Estou perdido.
L The principal is nice. Follow me!|O diretor é simpático. Siga-me!
H 3,4,6,7,0
Q Who is new?|Quem é o novo?|0|👨 Will|🧑 Carlton|🧑‍🏫 The principal
Q Where is the cafeteria?|Onde fica a cantina?|5|⬇️ Downstairs|⬆️ Upstairs|🚪 Outside
Q Is the principal nice?|O diretor é simpático?|7|✅ Yes|❌ No|🤷 Maybe
B show|👉|mostrar|the school|Carlton shows the school.|O Carlton mostra a escola.
B find|🔎|achar|the gym|Will finds the gym.|O Will acha o ginásio.
B ask|❓|perguntar|the principal|Will asks the principal.|O Will pergunta ao diretor.
B walk|🚶|andar|in the hallway|They walk in the hallway.|Eles andam no corredor.
LAB gy|Em gym, g soa dj e y soa i; em lost, o soa ó.|Gym e gem têm sons diferentes.
W gym|DJÍM|ginásio|g = dj|gem|DJÉM
W lost|LÓST|perdido|o = ó|last|LÉST
W new|NIÚ|novo|ew = iú|now|NÁU
G 0|is|are|am
G 1|Where|What|When
G 3|Follow|Follows|Following
G 4|new|now|news
X 👋|Welcome!|Bem-vindo!|Recebe alguém.|Welcome! This is our school.|Bem-vindo! Esta é a nossa escola.
X ➡️|Follow me!|Siga-me!|Chama alguém para ir junto.|Follow me! The gym is here.|Siga-me! O ginásio é aqui.
X 😌|Don’t worry.|Não se preocupe.|Acalma o novato.|Don’t worry. You are not lost.|Não se preocupe. Você não está perdido.
X 🙂|No problem.|Sem problema.|Responde a um agradecimento.|No problem. I like new friends.|Sem problema. Eu gosto de amigos novos.
"""))

N.append(parse("""
N 7080284
C Helga,Hagar | misshoney,tom | A Helga pergunta ao Hagar, o viking, se vão ao mar, e a resposta é sempre: depende.
F Hägar the Horrible | 💬 Tirinha | 1973 | uma tirinha criada por Dik Browne sobre Hagar, um viking atrapalhado, e a esposa Helga, que cuidam de casa e de aventuras no mar. | responder “depende” | home1 | ⛵,🪓,🏡
V ☀️|weather|tempo (clima)|UÉ-dher
V 💰|money|dinheiro|MÂ-ni
V 😊|mood|humor|MÚD
V ✌️|option|opção|ÓP-xân
V ⚖️|decision|decisão|di-SÍ-jân
V 🗓️|plan|plano|PLÉN
L Hagar, do we go to the sea?|Hagar, nós vamos ao mar?
L It depends on the weather.|Depende do tempo.
L Do you want a feast?|Você quer um banquete?
L It depends on the money.|Depende do dinheiro.
L Do you want a nap?|Você quer uma soneca?
L It depends on my mood, Helga.|Depende do meu humor, Helga.
L We have two options: the sea or the farm.|Nós temos duas opções: o mar ou a fazenda.
L It is a big decision. Let’s make a plan.|É uma grande decisão. Vamos fazer um plano.
H 1,3,5,6,7
Q What does it depend on first?|Do que depende primeiro?|1|☀️ The weather|💰 The money|😊 The mood
Q What are the two options?|Quais são as duas opções?|6|⛵ The sea or the farm|🍕 Pizza or pasta|🏠 Home or school
Q What do they need at the end?|Do que eles precisam no fim?|7|🗓️ A plan|🎁 A gift|🚌 A bus
B depend|🤷|depender|on the weather|It depends on the weather.|Depende do tempo.
B decide|✅|decidir|a plan|They decide a plan.|Eles decidem um plano.
B choose|👆|escolher|a place|Hagar chooses a place.|O Hagar escolhe um lugar.
B wait|⏳|esperar|for the sun|Helga waits for the sun.|A Helga espera o sol.
LAB we|Em weather, th soa dh; em mood, oo soa ú.|Mood e mud têm sons diferentes.
W weather|UÉ-dher|tempo (clima)|th = dh|wetter|UÉ-ter
W mood|MÚD|humor|oo = ú|mud|MÂD
W plan|PLÉN|plano|a = é|plane|PLÊIN
G 0|depends|depend|depending
G 1|on|in|at
G 2|my|me|mine
G 3|have|has|having
X 🤷|We’ll see.|Vamos ver.|Adia a resposta.|We’ll see. Ask me later.|Vamos ver. Pergunte mais tarde.
X 🙂|Maybe.|Talvez.|Responde sem certeza.|Maybe. It depends.|Talvez. Depende.
X 🤔|Let me think.|Deixe-me pensar.|Pede tempo.|Let me think about the plan.|Deixe-me pensar no plano.
X 💡|Good idea.|Boa ideia.|Aprova uma sugestão.|Good idea. Let’s go to the farm.|Boa ideia. Vamos à fazenda.
"""))

N.append(parse("""
N 7910035
C Madeline,Theo | polly,tom | A Madeline sobe a montanha e o Theo a anima a não desistir, a continuar e a tentar de novo.
F Celeste | 🎮 Videogame | 2018 | um jogo de plataforma em que a jovem Madeline sobe uma montanha difícil e aprende a continuar tentando, com a ajuda do amigo Theo. | persistir e não desistir | park | ⛰️,🍓,❄️
V ⛰️|challenge|desafio|TCHÉ-lendj
V 💪|effort|esforço|É-fort
V 📈|progress|progresso|PRÓ-gres
V 🎯|goal|meta|GÔUL
V 🦾|strength|força|STRÉNGTH
V 🏔️|mountain|montanha|MÁUN-tin
L Madeline, the mountain is a big challenge.|Madeline, a montanha é um grande desafio.
L I make an effort. I never give up.|Eu faço um esforço. Eu nunca desisto.
L You make progress. Keep going!|Você faz progresso. Continue!
L I fall. I try again. My goal is the top.|Eu caio. Eu tento de novo. A minha meta é o topo.
L You have strength. Never give up!|Você tem força. Nunca desista!
L I keep going. I climb the mountain.|Eu continuo. Eu escalo a montanha.
L One more step. You can do it!|Mais um passo. Você consegue!
L Look! I am at the top!|Olhe! Eu estou no topo!
H 0,1,2,3,4
Q What is the challenge?|Qual é o desafio?|0|⛰️ The mountain|🌊 The sea|🏰 The castle
Q What is Madeline’s goal?|Qual é a meta da Madeline?|3|🏔️ The top|🏠 Home|🍓 A strawberry
Q Is Madeline at the top at the end?|A Madeline está no topo no fim?|7|✅ Yes|❌ No|🤷 Maybe
B fall|⬇️|cair|on the ice|Madeline falls on the ice.|A Madeline cai no gelo.
B try|🔁|tentar|again|She tries again.|Ela tenta de novo.
B keep|➡️|continuar|going|Madeline keeps going.|A Madeline continua.
B climb|🧗|escalar|the mountain|They climb the mountain.|Eles escalam a montanha.
LAB mo|Em mountain, ou soa áu; em strength, ng+th soam juntos.|Mountain e mounting têm sons diferentes.
W mountain|MÁUN-tin|montanha|ou = áu|mounting|MÁUN-tin
W effort|É-fort|esforço|e = é|afford|a-FÓRD
W strength|STRÉNGTH|força|ng + th|string|STRÍNG
G 1|give|gives|giving
G 2|going|go|goes
G 3|try|tries|trying
G 4|Never|Ever|Not
X 💪|You can do it!|Você consegue!|Incentiva alguém.|You can do it! One more try.|Você consegue! Mais uma tentativa.
X ☝️|One more try.|Mais uma tentativa.|Pede outra chance.|One more try. I am ready.|Mais uma tentativa. Eu estou pronta.
X 🚫|Don’t stop!|Não pare!|Pede para continuar.|Don’t stop! The top is near.|Não pare! O topo está perto.
X 👏|Well done!|Muito bem!|Elogia o esforço.|Well done! You are strong.|Muito bem! Você é forte.
"""))
