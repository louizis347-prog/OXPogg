# Lote C do A1, dados 9 (n 910041 … 7080337). Ver zzc1_lib.py para o formato.
from v3.zzc1_lib import parse

N = []
N.append(parse("""
N 910041
C Lilly,Miley | polly,tommy | A Lilly deixa escapar o segredo da festa-surpresa: “let the cat out of the bag”.
F Hannah Montana | 📺 Série | 2006 | um seriado da Disney sobre Miley, uma garota que tem uma vida secreta como a cantora Hannah Montana, e os amigos Lilly e Oliver. | falar de segredos com expressões | living | 🎤,🎉,🤫
V 🤫|secret|segredo|SÍI-kret
V 🎉|party|festa|PÁR-ti
V 🐱|cat|gato|KÉT
V 👜|bag|bolsa|BÉG
V 🫘|beans|feijões|BÍINZ
V 🎁|surprise|surpresa|sâr-PRÁIZ
L Miley, it is a secret.|Miley, é um segredo.
L A surprise party for Oliver!|Uma festa-surpresa para o Oliver!
L Don’t let the cat out of the bag.|Não deixe o gato sair da bolsa.
L I won’t. Don’t spill the beans!|Eu não vou. Não derrame os feijões!
L Oops! The cat is out of the bag.|Ops! O gato saiu da bolsa.
L Lilly! You spill the beans.|Lilly! Você derrama os feijões.
L Sorry. I am bad at secrets.|Desculpe. Eu sou ruim com segredos.
L Shh! Oliver is here!|Psiu! O Oliver está aqui!
H 0,1,4,2,3
Q Whose party is it?|De quem é a festa?|1|🎉 Oliver’s|👩 Lilly’s|🧑 Robbie’s
Q Who spills the beans?|Quem derrama os feijões?|5|👩 Lilly|👧 Miley|🧑 Oliver
Q Who is here at the end?|Quem chega no fim?|7|🧑 Oliver|👨 Robbie Ray|🐱 A cat
B spill|🫘|derramar|the beans|Lilly spills the beans.|A Lilly derrama os feijões.
B tell|🗣️|contar|a secret|Miley tells a secret.|A Miley conta um segredo.
B promise|🤞|prometer|a secret|Miley promises a secret.|A Miley promete um segredo.
B keep|🔒|guardar|a secret|Lilly keeps a secret.|A Lilly guarda um segredo.
LAB se|Em secret, e soa íi; em beans, ea soa íi.|Beans e bins têm sons diferentes.
W secret|SÍI-kret|segredo|e = íi|second|SÉ-kond
W beans|BÍINZ|feijões|ea = íi|bins|BÍNZ
W surprise|sâr-PRÁIZ|surpresa|i = ái|sunrise|SÂN-ráiz
G 0|secret|second|secrete
G 2|out|in|on
G 3|let|lets|letting
G 4|spill|spills|spilled
X 😳|Oops!|Ops!|Reage a uma gafe.|Oops! I spill the beans.|Ops! Eu derramei os feijões.
X 🤫|Shh!|Psiu!|Pede silêncio.|Shh! It is a secret.|Psiu! É um segredo.
X 🙏|Sorry!|Desculpe!|Pede desculpa.|Sorry! I am bad at secrets.|Desculpe! Eu sou ruim com segredos.
X 😱|Oh no!|Ai, não!|Mostra susto.|Oh no! He is here.|Ai, não! Ele está aqui.
"""))

N.append(parse("""
N 7910041
C Bob,Tina | tom,polly | O Bob e a Tina descobrem que fazer uma torta é “easy as pie” e “a piece of cake”.
F Bob’s Burgers | 📺 Série animada | 2011 | um desenho animado americano sobre Bob, dono de uma lanchonete, e sua família, a esposa Linda e os filhos Tina, Gene e Louise. | dizer que algo é muito fácil | kitchen | 🍔,🥧,🍰
V 🥧|pie|torta|PÁI
V 🍰|cake|bolo|KÊIK
V 👍|easy|fácil|Í-zi
V 🧪|test|teste|TÉST
V 🏆|win|vencer|UÍN
V ⚡|quick|rápido|KUÍK
L Tina, bake a pie for the shop.|Tina, asse uma torta para a lanchonete.
L It’s as easy as pie, Dad.|É fácil como torta, pai.
L And a cake? That is a piece of cake.|E um bolo? Isso é moleza.
L The recipe is easy and quick.|A receita é fácil e rápida.
L Taste the pie. It is a good test.|Prove a torta. É um bom teste.
L We win the contest!|Nós vencemos o concurso!
L Louise says it is not easy.|A Louise diz que não é fácil.
L A piece of cake! Let’s win.|Moleza! Vamos vencer.
H 1,2,3,4,5
Q What does Bob want?|O que o Bob quer?|0|🥧 A pie|🍔 A burger|🍟 Fries
Q Is the recipe easy?|A receita é fácil?|3|✅ Yes, and quick|❌ No|🤷 Maybe
Q Who says it is not easy?|Quem diz que não é fácil?|6|👧 Louise|👦 Gene|👨 Teddy
B bake|🥧|assar|a pie|Tina bakes a pie.|A Tina assa uma torta.
B mix|🥣|misturar|the cake|Bob mixes the cake.|O Bob mistura o bolo.
B add|➕|adicionar|sugar|Tina adds sugar.|A Tina adiciona açúcar.
B win|🏆|ganhar|the contest|They win the contest.|Eles ganham o concurso.
LAB pi|Em pie, ie soa ái; em easy, ea soa íi.|Pie e pea têm sons diferentes.
W pie|PÁI|torta|ie = ái|pea|PÍI
W piece|PÍIS|pedaço|ie = íi|peas|PÍIZ
W easy|Í-zi|fácil|ea = íi|busy|BÍ-zi
G 0|as|like|so
G 1|piece|peace|pie
G 2|is|are|am
G 4|win|wins|won
X 🍰|Piece of cake!|Moleza!|Diz que é fácil.|Piece of cake! I bake it.|Moleza! Eu asso.
X 👏|Great job!|Ótimo trabalho!|Elogia.|Great job, Tina!|Ótimo trabalho, Tina!
X 😋|Yum!|Hum, que bom!|Mostra que gostou.|Yum! The pie is sweet.|Hum, que bom! A torta é doce.
X 💪|Come on!|Vamos lá!|Incentiva.|Come on! One more pie.|Vamos lá! Mais uma torta.
"""))

N.append(parse("""
N 7080333
C King,Prince | tom,tommy | O Rei do Cosmos e o Príncipe rolam uma bola que cresce de minúscula a gigante.
F Katamari Damacy | 🎮 Videogame | 2004 | um jogo da Namco em que o pequeno Príncipe rola uma bola pegajosa que cresce ao juntar coisas, a pedido do enorme Rei de Todo o Cosmos. | descrever tamanhos: huge, tiny e giant | park | 🔵,👑,⭐
V 🔵|ball|bola|BÓL
V 🐜|ant|formiga|ÉNT
V 🐘|elephant|elefante|É-le-fant
V ⛰️|mountain|montanha|MÁUN-tin
V ⭐|star|estrela|STÁR
V 📏|size|tamanho|SÁIZ
L Prince, the ball is tiny.|Príncipe, a bola é minúscula.
L Now it is bigger. I roll an ant.|Agora ela é maior. Eu rolo uma formiga.
L The elephant is huge!|O elefante é enorme!
L I roll the elephant too.|Eu rolo o elefante também.
L The ball is giant now.|A bola é gigante agora.
L Look! A huge mountain.|Olhe! Uma montanha enorme.
L Roll the mountain. Make a giant star.|Role a montanha. Faça uma estrela gigante.
L The star is huge. Hooray!|A estrela é enorme. Hurra!
H 0,1,2,5,7
Q How is the ball first?|Como a bola é no começo?|0|🔹 Tiny|🔵 Giant|🔴 Huge
Q What is huge?|O que é enorme?|2|🐘 The elephant|🐜 The ant|⭐ The ball
Q What does the Prince make?|O que o Príncipe faz?|6|⭐ A giant star|🏔️ A mountain|🐘 An elephant
B roll|🔵|rolar|the ball|The Prince rolls the ball.|O Príncipe rola a bola.
B grow|🌱|crescer|bigger|The ball grows bigger.|A bola cresce mais.
B look|👀|olhar|at the mountain|The King looks at the mountain.|O Rei olha para a montanha.
B measure|📏|medir|the size|The King measures the size.|O Rei mede o tamanho.
LAB hu|Em huge, u soa iú; em giant, g soa dj e i soa ái.|Huge e hug têm sons diferentes.
W huge|HIÚDJ|enorme|u = iú|hug|HÂG
W tiny|TÁI-ni|minúsculo|i = ái|tinny|TÍ-ni
W giant|DJÁI-ant|gigante|g = dj|gent|DJÉNT
G 0|tiny|tin|tinny
G 2|huge|hug|hugely
G 3|Look|Looks|Looking
G 4|is|are|am
X 🤩|Wow!|Uau!|Mostra admiração.|Wow! It is a giant ball.|Uau! É uma bola gigante.
X 🔵|Roll, roll!|Role, role!|Incentiva a rolar.|Roll, roll! The ball grows.|Role, role! A bola cresce.
X 🎉|Hooray!|Hurra!|Comemora.|Hooray! A huge star!|Hurra! Uma estrela enorme!
X 👀|Look!|Olhe!|Chama a atenção.|Look! A tiny ant.|Olhe! Uma formiga minúscula.
"""))

N.append(parse("""
N 7080334
C Mary Jane,Peter | polly,tommy | A Mary Jane pergunta ao Peter o que ele é capaz de fazer: escalar, pular e fazer teia.
F Spider-Man | 💬 Quadrinhos | 1962 | uma série de quadrinhos da Marvel sobre Peter Parker, um estudante que ganha poderes de aranha e usa a força, a velocidade e as teias para ajudar a cidade. | falar do que você é capaz de fazer | park | 🕷️,🕸️,🏙️
V 🧱|wall|parede|UÓL
V 💪|strong|forte|STRÓNG
V ⭐|skill|habilidade|SKÍL
V 🕸️|web|teia|UÉB
V 🏋️|practice|treino|PRÉK-tis
V ⚡|fast|rápido|FÉST
L Peter, are you able to climb the wall?|Peter, você é capaz de escalar a parede?
L Yes, I am able to climb it.|Sim, eu sou capaz de escalá-la.
L Are you able to jump high?|Você é capaz de pular alto?
L Yes. I am strong and fast.|Sim. Eu sou forte e rápido.
L What is your skill?|Qual é a sua habilidade?
L I am able to make a web.|Eu sou capaz de fazer uma teia.
L Practice every day, Peter.|Treine todo dia, Peter.
L I was not able to swing before, but now I can.|Antes eu não era capaz de me balançar, mas agora consigo.
H 0,3,4,5,6
Q Can Peter climb the wall?|O Peter consegue escalar a parede?|1|✅ Yes|❌ No|🤷 Maybe
Q What is Peter?|Como o Peter é?|3|💪 Strong and fast|🐢 Slow|😴 Sleepy
Q What can Peter make?|O que o Peter consegue fazer?|5|🕸️ A web|🪁 A kite|🏠 A house
B run|🏃|correr|fast|Peter runs fast.|O Peter corre rápido.
B jump|🦘|pular|high|He jumps high.|Ele pula alto.
B swing|🕸️|balançar|in the city|Peter swings in the city.|O Peter se balança na cidade.
B practice|🏋️|treinar|every day|Peter practices every day.|O Peter treina todo dia.
LAB ab|Em able, a soa êi; em strong, o soa ó.|Able e apple têm sons diferentes.
W able|ÊI-bol|capaz|a = êi|apple|Á-pol
W strong|STRÓNG|forte|o = ó|string|STRÍNG
W web|UÉB|teia|e = é|wed|UÉD
G 0|able|ability|enable
G 1|am|is|are
G 2|skill|skills|killed
G 3|to|for|at
X 🤩|Wow!|Uau!|Mostra admiração.|Wow! You are fast.|Uau! Você é rápido.
X 👍|Nice!|Legal!|Elogia.|Nice! That is a good skill.|Legal! Essa é uma boa habilidade.
X ⚠️|Be careful.|Tenha cuidado.|Alerta alguém.|Be careful. The wall is high.|Tenha cuidado. A parede é alta.
X 👋|See you!|Até logo!|Despede-se.|See you! I swing home.|Até logo! Eu me balanço para casa.
"""))

N.append(parse("""
N 7080335
C Sunflower,Dave | polly,tommy | O Crazy Dave e a Girassol cuidam do jardim: dar de beber, dar sol e olhar a folha.
F Plants vs. Zombies | 🎮 Videogame | 2009 | um jogo de defesa da PopCap em que o jardineiro Crazy Dave e suas plantas, como a Girassol, protegem a casa de zumbis. | falar de cuidar de plantas | yard | 🌻,🪴,🧟
V 🪴|plant|planta|PLÉNT
V 🍃|leaf|folha|LÍIF
V 🌱|root|raiz|RÚT
V ☀️|sun|sol|SÂN
V 🌹|rose|rosa|RÔUZ
V 🌳|garden|jardim|GÁR-den
L Dave, take care of the plant.|Dave, cuide da planta.
L I look after it every day.|Eu cuido dela todo dia.
L The leaf is green.|A folha é verde.
L The root is long. I give it a drink.|A raiz é longa. Eu dou de beber a ela.
L It needs the sun.|Ela precisa de sol.
L Look at the big rose!|Olhe a rosa grande!
L Take care of it, Dave.|Cuide dela, Dave.
L I look after the garden. It is great!|Eu cuido do jardim. Ele é ótimo!
H 0,2,3,4,5
Q What is green?|O que é verde?|2|🍃 The leaf|🌸 The flower|🪨 The soil
Q What is long?|O que é longo?|3|🌱 The root|🍃 The leaf|🌹 The rose
Q What does the plant need?|De que a planta precisa?|4|☀️ The sun|❄️ The snow|🌙 The moon
B take care of|🪴|cuidar de|the plant|Dave takes care of the plant.|O Dave cuida da planta.
B look after|👀|cuidar de|the garden|Dave looks after the garden.|O Dave cuida do jardim.
B feed|🍽️|alimentar|the plant|Sunflower feeds the plant.|A Girassol alimenta a planta.
B cut|✂️|cortar|the leaf|Dave cuts the leaf.|O Dave corta a folha.
LAB le|Em leaf, ea soa íi; em root, oo soa ú; em rose, o soa ôu.|Leaf e life têm sons diferentes.
W leaf|LÍIF|folha|ea = íi|life|LÁIF
W root|RÚT|raiz|oo = ú|rot|RÓT
W rose|RÔUZ|rosa|o = ôu|rise|RÁIZ
G 0|of|for|at
G 2|give|gives|giving
G 3|needs|need|needing
G 4|at|on|to
X ⚠️|Be careful.|Tenha cuidado.|Alerta alguém.|Be careful. The plant is big.|Tenha cuidado. A planta é grande.
X 👀|Look!|Olhe!|Chama a atenção.|Look! A new leaf!|Olhe! Uma folha nova!
X 👏|Good job!|Bom trabalho!|Elogia.|Good job, Dave!|Bom trabalho, Dave!
X 😱|Oh no!|Ai, não!|Mostra susto.|Oh no! The garden is dry.|Ai, não! O jardim está seco.
"""))

N.append(parse("""
N 7080337
C Susanna,Figaro | polly,tom | A Susanna e o Fígaro escrevem os convites da cerimônia e convidam os amigos.
F The Marriage of Figaro | 🎭 Ópera | 1786 | uma ópera cômica de Mozart sobre o criado Fígaro e a noiva Susanna, que se preparam para o casamento no meio de várias confusões. | convidar alguém para um evento | school | 💌,💍,🎶
V 💌|invitation|convite|ín-vi-TÊI-xân
V 💍|ceremony|cerimônia|SÉ-re-mô-ni
V 📍|address|endereço|a-DRÉS
V ⏰|time|hora|TÁIM
V 🧑‍🤝‍🧑|friend|amigo|FRÉND
V 🎉|party|festa|PÁR-ti
L Figaro, here is an invitation.|Fígaro, aqui está um convite.
L I invite Cherubino to the ceremony.|Eu convido o Cherubino para a cerimônia.
L Write the address on it.|Escreva o endereço nele.
L The time is four o’clock.|A hora é quatro horas.
L Invite a friend to dinner too.|Convide um amigo para o jantar também.
L Come to the party, friends!|Venham à festa, amigos!
L Can you come to the ceremony?|Você pode vir à cerimônia?
L I invite everyone. You are invited!|Eu convido todos. Vocês estão convidados!
H 0,1,2,3,4
Q Who does Figaro invite?|Quem o Fígaro convida?|1|🧑 Cherubino|👨 The Count|👩 Marcellina
Q What time is the ceremony?|A que horas é a cerimônia?|3|4️⃣ At four|3️⃣ At three|5️⃣ At five
Q Who is invited at the end?|Quem está convidado no fim?|7|👥 Everyone|🧑 Only Figaro|🙅 Nobody
B invite|💌|convidar|a friend|Figaro invites a friend.|O Fígaro convida um amigo.
B come|🚶|vir|to the ceremony|Friends come to the ceremony.|Os amigos vêm à cerimônia.
B write|✍️|escrever|the address|Susanna writes the address.|A Susanna escreve o endereço.
B confirm|✅|confirmar|the time|Figaro confirms the time.|O Fígaro confirma a hora.
LAB ce|Em ceremony, c soa s; em friend, ie soa é.|Address e dress têm sons diferentes.
W ceremony|SÉ-re-mô-ni|cerimônia|c = s|sermon|SÂR-mon
W friend|FRÉND|amigo|ie = é|fiend|FÍIND
W address|a-DRÉS|endereço|dd = d|dress|DRÉS
G 0|an|a|the
G 1|to|at|in
G 2|Write|Writes|Writing
G 4|Invite|Invites|Inviting
X 👍|Of course.|Claro.|Aceita um pedido.|Of course. I come to the ceremony.|Claro. Eu vou à cerimônia.
X 🙏|Thank you!|Obrigada!|Agradece.|Thank you! What a nice invitation!|Obrigada! Que convite bonito!
X 👋|See you there.|Até lá.|Combina o encontro.|See you there, Figaro.|Até lá, Fígaro.
X 💌|What a nice invitation!|Que convite bonito!|Elogia um convite.|What a nice invitation! It is blue.|Que convite bonito! Ele é azul.
"""))
