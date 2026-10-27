# Lote B (cinema), dados 4: episódios A1 80186 .. 910024. Formato: ver zz_b_lib.py.
from v3.zz_b_lib import add

add('''
N: 80186
C: Dewey,Summer | polly,tom | Na escola de música, Dewey e Summer dizem onde cada coisa está: at home, at school, at work.
S: lugares sem the: at home, at school, at work
Y: Hoje você aprende que alguns lugares não levam the: at home, at school, at work. Dewey is at school. Mom is at work.
F: School of Rock | 🎬 Filme | 2003 | uma comédia dirigida por Richard Linklater, sobre um músico que vira professor substituto e forma uma banda com os alunos | dizer onde as pessoas e as coisas estão | library | 🎸,🏫,🥁
V: 🏫|school|escola|SKÚL
V: 🏠|home|casa|RÔUM
V: 💼|work|trabalho|UÂRK
V: 🎸|guitar|guitarra|gui-TÁR
V: 🥁|drums|bateria|DRÂMZ
V: 🎒|classroom|sala de aula|KLÉS-rum
H: Dewey is at school.|O Dewey está na escola.
H: The kids are not at home.|As crianças não estão em casa.
H: Mom is at work.|A mãe está no trabalho.
H: The guitar is at home today.|A guitarra está em casa hoje.
H: We play drums at school.|Nós tocamos bateria na escola.
L: Summer, where is Dewey?|Summer, onde está o Dewey?
L: Dewey is at school.|O Dewey está na escola.
L: Where are the kids?|Onde estão as crianças?
L: The kids are not at home. They are in the classroom.|As crianças não estão em casa. Elas estão na sala de aula.
L: And your mom? Is she at home?|E a sua mãe? Ela está em casa?
L: No. Mom is at work.|Não. A mãe está no trabalho.
L: The guitar is at home today.|A guitarra está em casa hoje.
L: We play drums at school. Come on!|Nós tocamos bateria na escola. Vamos lá!
Q: Where is Dewey?|Onde está o Dewey?|1|🏫 At school|🏠 At home|💼 At work
Q: Where is Summer’s mom?|Onde está a mãe da Summer?|5|💼 At work|🏠 At home|🏫 At school
Q: Where is the guitar today?|Onde está a guitarra hoje?|6|🏠 At home|🏫 At school|💼 At work
B: teach|👨‍🏫|ensinar|I teach music.|He teaches music.|She taught the class.|Ela ensinou a turma.
B: play|🎸|tocar|I play the guitar.|He plays the guitar.|They played drums.|Eles tocaram bateria.
B: sing|🎤|cantar|I sing at school.|She sings at school.|We sang together.|Nós cantamos juntos.
B: practice|🥁|praticar|I practice the drums.|She practices the drums.|They practiced all day.|Eles praticaram o dia todo.
LAB: sc|Laboratório de sons: school, work e guitar|School começa com sk, “SKÚL”. Work soa “UÂRK”. Guitar tem a força no fim, “gui-TÁR”.|Em school, o ch soa como k: SKÚL.
W: school|SKÚL|escola|ch = k|skill|SKÍL
W: work|UÂRK|trabalho|or = âr|walk|UÓK
W: guitar|gui-TÁR|guitarra|força no fim|guard|GÁRD
G: 0|at|in|on
G: 1|at|in|to
G: 2|at|in|on
G: 4|at|in|on
X: 🎸|Let’s rock|Vamos tocar|animar|Let’s rock, kids!|Vamos tocar, crianças!
X: 🙌|Good job|Bom trabalho|elogiar|Good job, Summer.|Bom trabalho, Summer.
X: 👏|One more time|Mais uma vez|pedir repetição|One more time, please.|Mais uma vez, por favor.
X: 😊|See you tomorrow|Até amanhã|despedir-se|See you tomorrow at school.|Até amanhã na escola.

N: 7080186
C: Amélie,Nino | polly,tom | Nas ruas de Paris, Amélie e Nino contam o que fazem em cada parte do dia: in the morning, at night.
S: partes do dia: in the morning, in the afternoon, in the evening, at night
Y: Hoje você aprende as partes do dia: in the morning, in the afternoon, in the evening, mas at night.
F: Amélie | 🎬 Filme | 2001 | um filme dirigido por Jean-Pierre Jeunet, sobre uma jovem de Paris que gosta de fazer pequenas gentilezas para os vizinhos | falar do que se faz em cada parte do dia | rainycafe | 🚲,☕,🗼
V: ☀️|morning|manhã|MÓR-ning
V: 🌤️|afternoon|tarde|é-fter-NÚN
V: 🌆|evening|fim de tarde|ÍV-ning
V: 🌙|night|noite|NÁIT
V: ☕|coffee|café|KÓ-fi
V: 🚲|bike|bicicleta|BÁIK
H: I walk in the morning.|Eu ando de manhã.
H: I read in the afternoon.|Eu leio à tarde.
H: I cook in the evening.|Eu cozinho no fim da tarde.
H: I sleep at night.|Eu durmo à noite.
H: We have coffee in the morning.|Nós tomamos café de manhã.
L: Nino, what do you do in the morning?|Nino, o que você faz de manhã?
L: I walk in the morning. I ride my bike.|Eu ando de manhã. Eu ando de bicicleta.
L: And in the afternoon?|E à tarde?
L: I read in the afternoon.|Eu leio à tarde.
L: I cook in the evening.|Eu cozinho no fim da tarde.
L: What about at night?|E à noite?
L: I sleep at night. Good night, Nino.|Eu durmo à noite. Boa noite, Nino.
L: We have coffee in the morning. See you!|Nós tomamos café de manhã. Até lá!
Q: When does Nino walk?|Quando o Nino anda?|1|☀️ In the morning|🌙 At night|🌆 In the evening
Q: What does he do in the afternoon?|O que ele faz à tarde?|3|📖 He reads|🍳 He cooks|😴 He sleeps
Q: When does Amélie sleep?|Quando a Amélie dorme?|6|🌙 At night|☀️ In the morning|🌤️ In the afternoon
B: ride|🚲|andar de (bicicleta)|I ride my bike.|He rides his bike.|She rode to the park.|Ela foi de bicicleta ao parque.
B: cook|🍳|cozinhar|I cook dinner.|She cooks dinner.|He cooked at home.|Ele cozinhou em casa.
B: sleep|😴|dormir|I sleep eight hours.|He sleeps eight hours.|They slept well.|Eles dormiram bem.
B: smile|😊|sorrir|I smile at people.|She smiles at people.|He smiled in the morning.|Ele sorriu de manhã.
LAB: mo|Laboratório de sons: morning, afternoon e night|Morning soa “MÓR-ning”. Afternoon tem a força no fim, “é-fter-NÚN”. Night termina em t, “NÁIT”, com o gh mudo.|Em night, o gh não se fala: NÁIT.
W: morning|MÓR-ning|manhã|or = ór|mourning|MÓR-ning
W: afternoon|é-fter-NÚN|tarde|força no fim|after|É-fter
W: night|NÁIT|noite|gh mudo|knight|NÁIT
G: 0|in|at|on
G: 1|in|at|on
G: 3|at|in|on
G: 4|in|at|on
X: 😍|How lovely|Que lindo|admirar|How lovely, the morning.|Que lindo, a manhã.
X: 🌙|Good night|Boa noite|despedir-se|Good night, Nino.|Boa noite, Nino.
X: 😊|See you soon|Até logo|despedir-se|See you soon, Amélie.|Até logo, Amélie.
X: ☕|Every day|Todo dia|dizer a rotina|Every day I ride my bike.|Todo dia eu ando de bicicleta.

N: 80187
T: Thirteen puppies
C: Pongo,Perdita | tom,polly | Na casa dos dálmatas, Pongo e Perdita contam os filhotes: thirteen, fourteen, fifteen… nineteen.
S: números de 13 a 19: thirteen, fourteen, fifteen… nineteen
Y: Hoje você aprende os números de 13 a 19: thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen. Todos terminam em -teen.
F: One Hundred and One Dalmatians | 🎬 Animação | 1961 | uma animação clássica da Disney sobre dois cães dálmatas que cuidam de uma ninhada enorme de filhotes | contar de treze a dezenove | toyshop | 🐶,⚫,🦴
V: 🐶|puppy|filhote|PÂ-pi
V: ⚫|spot|mancha|SPÓT
V: 🕐|clock|relógio|KLÓK
V: 🦴|bone|osso|BÔUN
V: 🏠|house|casa|RÁUS
V: 🍼|bottle|mamadeira|BÓ-tol
H: I count thirteen puppies.|Eu conto treze filhotes.
H: There are fourteen spots.|Há quatorze manchas.
H: It is fifteen minutes past one.|São quinze minutos depois da uma.
H: I have sixteen bones.|Eu tenho dezesseis ossos.
H: Nineteen puppies are in the house.|Dezenove filhotes estão na casa.
L: Perdita, I count thirteen puppies.|Perdita, eu conto treze filhotes.
L: Thirteen? I count fourteen spots.|Treze? Eu conto quatorze manchas.
L: Look at the clock. It is fifteen minutes past one.|Olhe o relógio. São quinze minutos depois da uma.
L: Time for the bottle!|Hora da mamadeira!
L: I have sixteen bones in the box.|Eu tenho dezesseis ossos na caixa.
L: Seventeen, eighteen, nineteen...|Dezessete, dezoito, dezenove...
L: Nineteen puppies are in the house.|Dezenove filhotes estão na casa.
L: Then we need a bigger house, Pongo!|Então precisamos de uma casa maior, Pongo!
Q: How many puppies does Pongo count first?|Quantos filhotes o Pongo conta primeiro?|0|🐶 Thirteen|🐶 Fourteen|🐶 Fifteen
Q: What time is it?|Que horas são?|2|🕐 Fifteen minutes past one|🕐 Fifty minutes past one|🕐 Five minutes past one
Q: How many puppies are in the house?|Quantos filhotes estão na casa?|6|🏠 Nineteen|🏠 Ninety|🏠 Nine
B: count|🔢|contar|I count the puppies.|He counts the puppies.|She counted fifteen.|Ela contou quinze.
B: bark|🐕|latir|I bark at the door.|He barks at the door.|They barked all night.|Eles latiram a noite toda.
B: sniff|👃|farejar|I sniff the bone.|He sniffs the bone.|She sniffed the bottle.|Ela farejou a mamadeira.
B: hide|🙈|esconder|I hide the bone.|He hides the bone.|The puppy hid under the bed.|O filhote se escondeu embaixo da cama.
LAB: te|Laboratório de sons: thirteen, fifteen e nineteen|Os números de 13 a 19 terminam em -teen, com í longo: “thâr-TÍN”, “fif-TÍN”, “náin-TÍN”. A força cai no -teen.|Em thirteen, a força cai no final: thâr-TÍN.
W: thirteen|thâr-TÍN|treze|força no final|thirty|THÂR-di
W: fifteen|fif-TÍN|quinze|força no final|fifty|FÍF-ti
W: nineteen|náin-TÍN|dezenove|força no final|ninety|NÁIN-ti
G: 0|thirteen|thirty|third
G: 1|fourteen|forty|fourth
G: 2|fifteen|fifty|fifth
G: 4|Nineteen|Ninety|Ninth
X: 😮|So many|Tantos|se surpreender|So many puppies!|Tantos filhotes!
X: 🕐|Time for|Hora de|marcar hora|Time for the bottle!|Hora da mamadeira!
X: 🐶|Come here|Venham aqui|chamar|Come here, puppies.|Venham aqui, filhotes.
X: 😅|Oh dear|Ai, meu Deus|se preocupar|Oh dear, nineteen puppies.|Ai, meu Deus, dezenove filhotes.

N: 7080187
C: Kermit,Fozzie | tommy,tom | No teatro, Kermit e Fozzie dizem as horas com minutos: past e to.
S: hora com minutos: five past, twenty past, ten to, twenty to
Y: Hoje você aprende a dizer as horas: past é depois (five past twelve) e to é para (ten to one).
F: The Muppet Movie | 🎬 Filme | 1979 | um filme dirigido por James Frawley, sobre um sapo e seus amigos bonecos que viajam para fazer um grande show | dizer as horas com minutos | toyshop | 🐸,🎭,🕒
V: ⌚|watch|relógio de pulso|UÓTCH
V: ⏱️|minute|minuto|MÍ-nit
V: 🚌|bus|ônibus|BÂS
V: 🎬|show|espetáculo|SHÔU
V: 🎭|stage|palco|STÊIJ
V: 🐸|frog|sapo|FRÓG
H: It is five past twelve.|São doze e cinco.
H: Just a minute, Fozzie!|Só um minuto, Fozzie!
H: The bus leaves at ten to one.|O ônibus sai às dez para a uma.
H: The show starts at twenty past three.|O show começa às três e vinte.
H: It is twenty to four.|São vinte para as quatro.
L: Kermit, what time is it?|Kermit, que horas são?
L: It is five past twelve, Fozzie.|São doze e cinco, Fozzie.
L: Just a minute! I need my hat.|Só um minuto! Eu preciso do meu chapéu.
L: The bus leaves at ten to one.|O ônibus sai às dez para a uma.
L: Then hurry. The show starts at twenty past three.|Então ande rápido. O show começa às três e vinte.
L: What time is it now?|Que horas são agora?
L: It is twenty to four. We are late!|São vinte para as quatro. Estamos atrasados!
L: Run to the stage, Fozzie!|Corra para o palco, Fozzie!
Q: What time is it first?|Que horas são primeiro?|1|🕒 Five past twelve|🕒 Ten to one|🕒 Twenty to four
Q: When does the bus leave?|Quando o ônibus sai?|3|🚌 At ten to one|🚌 At five past twelve|🚌 At twenty to four
Q: When does the show start?|Quando o show começa?|4|🎬 At twenty past three|🎬 At ten to one|🎬 At five past twelve
B: wait|⏳|esperar|I wait for the bus.|He waits for the bus.|They waited ten minutes.|Eles esperaram dez minutos.
B: hurry|🏃|apressar-se|I hurry to the stage.|He hurries to the stage.|We hurried inside.|Nós corremos para dentro.
B: start|▶️|começar|The show starts now.|The show starts now.|It started at three.|Começou às três.
B: leave|🚪|sair|I leave at one.|He leaves at one.|The bus left early.|O ônibus saiu cedo.
LAB: mi|Laboratório de sons: minute, stage e frog|Minute soa “MÍ-nit”, com força no começo. Stage soa “STÊIJ”. Frog soa “FRÓG”, com o aberto.|Em stage, o a soa êi e o g soa dj: STÊIJ.
W: minute|MÍ-nit|minuto|força no começo|mini|MÍ-ni
W: stage|STÊIJ|palco|a = êi|stay|STÊI
W: frog|FRÓG|sapo|o aberto|flag|FLÉG
G: 0|past|to|at
G: 2|to|past|at
G: 3|past|to|in
G: 4|to|past|in
X: 😅|Hurry up|Ande rápido|apressar|Hurry up, Fozzie!|Ande rápido, Fozzie!
X: 😮|We’re late|Estamos atrasados|reagir|We’re late, run!|Estamos atrasados, corra!
X: 🎭|Show time|Hora do show|anunciar|Show time, everyone!|Hora do show, pessoal!
X: 🕒|Right on time|Bem na hora|comemorar|Right on time, Kermit.|Bem na hora, Kermit.

N: 80188
T: A million dollars
C: Annie,Warbucks | polly,tom | Na mansão, Annie e o senhor Warbucks contam valores grandes: hundred, thousand, million.
S: números grandes: hundred, thousand, million
Y: Hoje você aprende os números grandes: one hundred (100), a thousand (1.000), a million (1.000.000).
F: Annie | 🎬 Musical | 1982 | um filme musical dirigido por John Huston, sobre uma menina órfã que vai morar na mansão de um milionário | falar de números grandes e dinheiro | castle | 🏰,💵,🐕
V: 💵|dollar|dólar|DÓ-ler
V: 🏦|bank|banco|BÉNK
V: 🏰|mansion|mansão|MÉN-shan
V: 🌟|star|estrela|STÁR
V: 🐕|dog|cachorro|DÓG
V: 🎁|gift|presente|GUÍFT
H: I have one hundred dollars.|Eu tenho cem dólares.
H: The bank has a thousand dollars.|O banco tem mil dólares.
H: The mansion costs a million dollars.|A mansão custa um milhão de dólares.
H: I see a thousand stars.|Eu vejo mil estrelas.
H: The dog has one hundred bones.|O cachorro tem cem ossos.
L: Mister Warbucks, I have one hundred dollars.|Senhor Warbucks, eu tenho cem dólares.
L: Ha! The bank has a thousand dollars.|Ha! O banco tem mil dólares.
L: And the mansion?|E a mansão?
L: The mansion costs a million dollars.|A mansão custa um milhão de dólares.
L: Wow! I see a thousand stars from my window.|Uau! Eu vejo mil estrelas da minha janela.
L: The stars cost nothing, Annie.|As estrelas não custam nada, Annie.
L: My dog has one hundred bones. A big gift!|Meu cachorro tem cem ossos. Um grande presente!
L: You are a rich girl, Annie.|Você é uma menina rica, Annie.
Q: How many dollars does Annie have?|Quantos dólares a Annie tem?|0|💵 One hundred|💵 One thousand|💵 One million
Q: How much does the mansion cost?|Quanto custa a mansão?|3|🏰 A million dollars|🏰 A thousand dollars|🏰 One hundred dollars
Q: How many bones does the dog have?|Quantos ossos o cachorro tem?|6|🦴 One hundred|🦴 One thousand|🦴 One million
B: count|🔢|contar|I count the dollars.|He counts the dollars.|She counted a thousand.|Ela contou mil.
B: sing|🎤|cantar|I sing a happy song.|She sings a happy song.|They sang in the rain.|Eles cantaram na chuva.
B: smile|😊|sorrir|I smile at the dog.|She smiles at the dog.|We smiled all day.|Nós sorrimos o dia todo.
B: give|🎁|dar|I give a gift.|He gives a gift.|She gave me a dollar.|Ela me deu um dólar.
LAB: hu|Laboratório de sons: hundred, thousand e million|Hundred soa “RÂN-dred”. Thousand soa “THÁU-zend”, com th soprado. Million soa “MÍ-lien”.|Em thousand, coloque a língua entre os dentes no th: THÁU-zend.
W: hundred|RÂN-dred|cem|h soprado|hunter|RÂN-ter
W: thousand|THÁU-zend|mil|th surdo|south|SÁUTH
W: million|MÍ-lien|milhão|ll = li|mill|MÍL
G: 0|hundred|hundreds|hundredth
G: 1|thousand|thousands|thousandth
G: 2|million|millions|millionth
G: 4|hundred|hundreds|hundredth
X: 😲|Wow|Uau|se surpreender|Wow, a million dollars!|Uau, um milhão de dólares!
X: 😊|Tomorrow|Amanhã|esperança|Tomorrow will be better.|Amanhã vai ser melhor.
X: 🎁|For you|Para você|dar|For you, Annie.|Para você, Annie.
X: 😄|Thank you so much|Muito obrigada|agradecer|Thank you so much, sir.|Muito obrigada, senhor.

N: 7080188
T: It’s thirty degrees
C: Mumble,Gloria | tom,polly | No gelo, Mumble e Gloria leem o termômetro: thirty, forty, sixty, ninety degrees.
S: temperatura em graus: thirty, forty, sixty, ninety degrees
Y: Hoje você aprende a dizer a temperatura: It’s thirty degrees. It’s forty degrees. Os números de dezena terminam em -ty.
F: Happy Feet | 🎬 Animação | 2006 | uma animação dirigida por George Miller, sobre um pinguim que não sabe cantar mas dança muito bem no gelo | dizer a temperatura em graus | lighthouse | 🐧,🧊,🌡️
V: 🌡️|thermometer|termômetro|ther-MÓ-mi-ter
V: 🐧|penguin|pinguim|PÉN-guin
V: 🧊|ice|gelo|ÁIS
V: 🌊|ocean|oceano|ÔU-shen
V: ☀️|sun|sol|SÂN
V: 🌬️|wind|vento|UÍND
H: It’s thirty degrees.|Faz trinta graus.
H: It’s forty degrees today.|Hoje faz quarenta graus.
H: It’s sixty degrees in the sun.|Faz sessenta graus no sol.
H: The ocean is seventy degrees.|O oceano está a setenta graus.
H: It’s ninety degrees in summer.|Faz noventa graus no verão.
L: Gloria, look at the thermometer.|Gloria, olhe o termômetro.
L: It’s thirty degrees, Mumble.|Faz trinta graus, Mumble.
L: Thirty? It’s forty degrees today.|Trinta? Hoje faz quarenta graus.
L: It’s sixty degrees in the sun.|Faz sessenta graus no sol.
L: The ocean is seventy degrees.|O oceano está a setenta graus.
L: Too warm for a penguin!|Quente demais para um pinguim!
L: In summer it’s ninety degrees.|No verão faz noventa graus.
L: Then let’s dance on the ice now.|Então vamos dançar no gelo agora.
Q: How many degrees is it first?|Quantos graus faz primeiro?|1|🌡️ Thirty|🌡️ Thirteen|🌡️ Third
Q: How warm is the ocean?|Quão quente está o oceano?|4|🌊 Seventy degrees|🌊 Seventeen degrees|🌊 Sixty degrees
Q: What do they do on the ice?|O que eles fazem no gelo?|7|💃 They dance|🏊 They swim|🍽️ They eat
B: dance|💃|dançar|I dance on the ice.|She dances on the ice.|They danced all day.|Eles dançaram o dia todo.
B: slide|🛝|deslizar|I slide on my belly.|He slides on his belly.|She slid across the ice.|Ela deslizou pelo gelo.
B: swim|🏊|nadar|I swim in the ocean.|She swims in the ocean.|We swam to the shore.|Nós nadamos até a costa.
B: shiver|🥶|tremer de frio|I shiver in the wind.|He shivers in the wind.|They shivered all night.|Eles tremeram a noite toda.
LAB: ty|Laboratório de sons: thirty, ninety e degrees|Thirty e ninety terminam em -ty curto: “THÂR-di”, “NÁIN-di”. Degrees soa “di-GRÍZ”, com força no fim.|Em thirty, a força cai no começo: THÂR-di, diferente de thirteen.
W: thirty|THÂR-di|trinta|força no começo|thirteen|thâr-TÍN
W: ninety|NÁIN-di|noventa|força no começo|nineteen|náin-TÍN
W: degrees|di-GRÍZ|graus|força no fim|agrees|a-GRÍZ
G: 0|thirty|thirteen|third
G: 1|forty|fourteen|fourth
G: 2|sixty|sixteen|sixth
G: 4|ninety|nineteen|ninth
X: 🥶|Brrr|Brrr, que frio|reclamar|Brrr, it is so cold.|Brrr, está tão frio.
X: 😎|Nice and warm|Quentinho|elogiar|Nice and warm in the sun.|Quentinho no sol.
X: 💃|Let’s dance|Vamos dançar|animar|Let’s dance, Gloria!|Vamos dançar, Gloria!
X: 😲|Look at that|Olhe aquilo|chamar atenção|Look at that, seventy degrees!|Olhe aquilo, setenta graus!

N: 910023
C: Bastian,Atreyu | misshoney,tom | No sótão da escola, Bastian lê e escreve uma história: read a…, write a…
S: falar do que lê e escreve: I read a book. I write a story
Y: Hoje você aprende a dizer o que lê e o que escreve: read a book, write a story, write a note.
F: The NeverEnding Story | 🎬 Filme | 1984 | um filme dirigido por Wolfgang Petersen, sobre um menino que lê um livro mágico e entra na história | falar do que se lê e se escreve | library | 📖,🐉,✍️
V: 📖|book|livro|BÚK
V: ✍️|story|história|STÓ-ri
V: 📝|note|bilhete|NÔUT
V: 🐉|dragon|dragão|DRÉ-gon
V: 🕯️|candle|vela|KÉN-dol
V: 🪟|attic|sótão|É-tik
H: I read a book in the attic.|Eu leio um livro no sótão.
H: I write a story every night.|Eu escrevo uma história toda noite.
H: Let me write a note for you.|Deixe-me escrever um bilhete para você.
H: Read a story about a dragon.|Leia uma história sobre um dragão.
H: The candle is small, but I read.|A vela é pequena, mas eu leio.
L: Atreyu, I read a book in the attic.|Atreyu, eu leio um livro no sótão.
L: What is the book about, Bastian?|Sobre o que é o livro, Bastian?
L: A dragon! Read a story about a dragon.|Um dragão! Leia uma história sobre um dragão.
L: I write a story every night, too.|Eu escrevo uma história toda noite também.
L: Let me write a note for you.|Deixe-me escrever um bilhete para você.
L: Thank you. What does it say?|Obrigado. O que ele diz?
L: “Be brave.” The candle is small, but I read.|“Seja corajoso.” A vela é pequena, mas eu leio.
L: Then keep reading, Bastian.|Então continue lendo, Bastian.
Q: Where does Bastian read?|Onde o Bastian lê?|0|🪟 In the attic|🏫 In class|🏠 In the kitchen
Q: What is the story about?|Sobre o que é a história?|2|🐉 A dragon|🐕 A dog|🚀 A rocket
Q: What does Bastian write for Atreyu?|O que o Bastian escreve para o Atreyu?|4|📝 A note|📖 A book|✍️ A story
B: read|📖|ler|I read a book.|He reads a book.|She read a story.|Ela leu uma história.
B: write|✍️|escrever|I write a note.|He writes a note.|They wrote a story.|Eles escreveram uma história.
B: turn|🔄|virar|I turn the page.|He turns the page.|She turned it slowly.|Ela a virou devagar.
B: imagine|💭|imaginar|I imagine a dragon.|He imagines a dragon.|We imagined a castle.|Nós imaginamos um castelo.
LAB: bo|Laboratório de sons: book, story e dragon|Book tem o u curto, “BÚK”. Story soa “STÓ-ri”. Dragon soa “DRÉ-gon”.|Em book, o oo é curto: BÚK, diferente de food.
W: book|BÚK|livro|oo curto|buck|BÂK
W: story|STÓ-ri|história|or = ór|stir|STÂR
W: dragon|DRÉ-gon|dragão|a = é|drag|DRÉG
G: 0|read|reads|reading
G: 1|write|writes|writing
G: 2|write|writes|writing
G: 3|Read|Reads|Reading
X: 📖|Once upon a time|Era uma vez|começar história|Once upon a time, a dragon.|Era uma vez, um dragão.
X: 😲|What happens next|O que acontece depois|perguntar|What happens next, Bastian?|O que acontece depois, Bastian?
X: 🤫|Shh|Shh|pedir silêncio|Shh, I read now.|Shh, eu leio agora.
X: 👍|Keep going|Continue|animar|Keep going, the story is good.|Continue, a história está boa.

N: 7910023
C: David,Jennifer | tommy,polly | Diante do computador, David e Jennifer digitam, mandam mensagem e anotam: type, text, write down.
S: tecnologia simples: type, text e write down: I type the code. Write down the password
Y: Hoje você aprende type (digitar), text (mandar mensagem) e write down (anotar). I type on the keyboard. Write down the password.
F: WarGames | 🎬 Filme | 1983 | um filme dirigido por John Badham, sobre um jovem curioso que entra por engano num sistema de computador e precisa corrigir o erro | falar de digitar, mandar mensagem e anotar | viaduct | ⌨️,💻,📱
V: ⌨️|keyboard|teclado|KÍ-bórd
V: 📱|phone|celular|FÔUN
V: 🔐|password|senha|PÉS-uârd
V: 💻|code|código|KÔUD
V: 📝|paper|papel|PÊI-per
V: 🖥️|screen|tela|SKRÍN
H: I type on the keyboard.|Eu digito no teclado.
H: I text Jennifer on the phone.|Eu mando mensagem para a Jennifer pelo celular.
H: Write down the password.|Anote a senha.
H: Type the code, please.|Digite o código, por favor.
H: Write it down on paper.|Anote no papel.
L: Jennifer, I type on the keyboard.|Jennifer, eu digito no teclado.
L: Look at the screen, David.|Olhe a tela, David.
L: Wait. I text my friend on the phone.|Espere. Eu mando mensagem para o meu amigo pelo celular.
L: Good. Now write down the password.|Bom. Agora anote a senha.
L: Write it down on paper.|Anote no papel.
L: Type the code, please.|Digite o código, por favor.
L: Done. The screen says “Yes”.|Pronto. A tela diz “Sim”.
L: Great! Text me the result later.|Ótimo! Mande-me o resultado depois.
Q: Where does David type?|Onde o David digita?|0|⌨️ On the keyboard|📱 On the phone|📝 On paper
Q: What must David write down?|O que o David deve anotar?|3|🔐 The password|📱 The phone|🖥️ The screen
Q: What does Jennifer ask David to do later?|O que a Jennifer pede ao David depois?|7|📱 Text her|⌨️ Type again|📝 Write a letter
B: type|⌨️|digitar|I type the code.|He types the code.|She typed a word.|Ela digitou uma palavra.
B: click|🖱️|clicar|I click on the icon.|He clicks on the icon.|They clicked twice.|Eles clicaram duas vezes.
B: save|💾|salvar|I save the file.|He saves the file.|She saved her work.|Ela salvou o trabalho dela.
B: print|🖨️|imprimir|I print the page.|He prints the page.|We printed two copies.|Nós imprimimos duas cópias.
LAB: ke|Laboratório de sons: keyboard, password e screen|Keyboard tem a força no começo, “KÍ-bórd”. Password soa “PÉS-uârd”. Screen começa com skr junto, “SKRÍN”.|Em screen, junte s, k e r: SKRÍN.
W: keyboard|KÍ-bórd|teclado|ey = í|keyword|KÍ-uârd
W: password|PÉS-uârd|senha|a = é|passport|PÉS-pórt
W: screen|SKRÍN|tela|skr junto|scream|SKRÍM
G: 0|type|types|typing
G: 1|text|texts|texting
G: 2|Write down|Write up|Writes down
G: 3|Type|Types|Typing
X: 😅|Oops|Ops|se desculpar|Oops, wrong code.|Ops, código errado.
X: 👍|It works|Funciona|comemorar|It works, David!|Funciona, David!
X: 🤔|Let me check|Deixe-me conferir|conferir|Let me check the screen.|Deixe-me conferir a tela.
X: 🙂|Be careful|Tenha cuidado|avisar|Be careful with the code.|Tenha cuidado com o código.

N: 7080193
C: Babe,Fly | polly,tommy | Na cozinha da fazenda, Babe e Fly falam do que só comem: only, just.
S: limitar com only e just: I only eat vegetables, I just eat corn
Y: Hoje você aprende only e just (só, apenas): I only eat vegetables. I just eat corn and peas.
F: Babe | 🎬 Filme | 1995 | um filme dirigido por Chris Noonan, sobre um porquinho que vive numa fazenda e aprende a pastorear ovelhas | dizer o que se come apenas | jungle | 🐷,🌽,🥕
V: 🥕|carrots|cenouras|KÉ-rots
V: 🌽|corn|milho|KÓRN
V: 🥔|potatoes|batatas|po-TÊI-tôz
V: 🌱|grass|grama|GRÉS
V: 🥬|cabbage|repolho|KÉ-bidj
V: 🐷|pig|porquinho|PÍG
H: I only eat vegetables.|Eu só como vegetais.
H: I just eat corn and peas.|Eu só como milho e ervilhas.
H: Fly only likes potatoes.|A Fly só gosta de batatas.
H: I just like the grass.|Eu só gosto da grama.
H: We only grow cabbage.|Nós só cultivamos repolho.
L: Fly, what do you eat?|Fly, o que você come?
L: I only eat vegetables, Babe.|Eu só como vegetais, Babe.
L: I just eat corn and peas.|Eu só como milho e ervilhas.
L: Do you eat carrots?|Você come cenouras?
L: Yes, but Fly only likes potatoes.|Sim, mas a Fly só gosta de batatas.
L: I just like the grass.|Eu só gosto da grama.
L: And the farmer? We only grow cabbage.|E o fazendeiro? Nós só cultivamos repolho.
L: Then dinner is easy for a pig!|Então o jantar é fácil para um porquinho!
Q: What does Fly eat?|O que a Fly come?|1|🥬 Only vegetables|🍖 Only meat|🍰 Only cake
Q: What does Babe just eat?|O que o Babe só come?|2|🌽 Corn and peas|🥔 Potatoes|🥬 Cabbage
Q: What does the farm only grow?|O que a fazenda só cultiva?|6|🥬 Cabbage|🌽 Corn|🥕 Carrots
B: feed|🍽️|alimentar|I feed the pig.|She feeds the pig.|He fed the sheep.|Ele alimentou as ovelhas.
B: grow|🌱|cultivar|I grow cabbage.|He grows cabbage.|They grew corn.|Eles cultivaram milho.
B: chew|😋|mastigar|I chew the grass.|He chews the grass.|The pig chewed slowly.|O porquinho mastigou devagar.
B: share|🤝|dividir|I share my corn.|She shares her corn.|They shared the carrots.|Eles dividiram as cenouras.
LAB: ca|Laboratório de sons: carrots, corn e cabbage|Carrots soa “KÉ-rots”. Corn soa “KÓRN”, com o aberto. Cabbage soa “KÉ-bidj”.|Em cabbage, o age final soa idj: KÉ-bidj.
W: carrots|KÉ-rots|cenouras|a = é|carats|KÉ-rots
W: corn|KÓRN|milho|o aberto|coin|KÓIN
W: cabbage|KÉ-bidj|repolho|age = idj|cabin|KÉ-bin
G: 0|only|alone|lonely
G: 1|just|right|much
G: 2|only|alone|lonely
G: 3|just|right|much
X: 😋|Yummy|Que delícia|elogiar|Yummy, fresh corn.|Que delícia, milho fresco.
X: 🤢|Not for me|Não é para mim|recusar|Not for me, thank you.|Não é para mim, obrigado.
X: 🐷|Oink|Oinc|imitar|Oink, oink, I am hungry.|Oinc, oinc, estou com fome.
X: 😊|That’s all|É só isso|encerrar|That’s all I eat.|É só isso que eu como.

N: 7080195
C: Buster,Rosita | tom,polly | No palco do teatro, Buster e Rosita descrevem os sons: loud, soft, quiet, too loud.
S: descrever sons com loud, soft e quiet: The drum is too loud
Y: Hoje você aprende a descrever sons: loud (alto), soft (suave), quiet (baixinho). The drum is too loud. The bell is soft.
F: Sing | 🎬 Animação | 2016 | uma animação dirigida por Garth Jennings, sobre um empresário que organiza um concurso de canto num teatro | descrever sons e música | rainycafe | 🎤,🥁,🎺
V: 🥁|drum|tambor|DRÂM
V: 🎺|trumpet|trombeta|TRÂM-pit
V: 🔔|bell|sino|BÉL
V: 🎻|violin|violino|vai-o-LÍN
V: 🎼|song|canção|SÓNG
V: 🎭|theater|teatro|THÍ-e-ter
H: The drum is too loud.|O tambor está alto demais.
H: Your trumpet is too loud!|Sua trombeta está alta demais!
H: The bell is soft.|O sino é suave.
H: The violin is quiet.|O violino está baixinho.
H: Sing a soft song.|Cante uma canção suave.
L: Rosita, the drum is too loud.|Rosita, o tambor está alto demais.
L: Sorry, Buster. Your trumpet is too loud!|Desculpe, Buster. Sua trombeta está alta demais!
L: Listen to the bell. The bell is soft.|Ouça o sino. O sino é suave.
L: Nice. And the violin is quiet.|Legal. E o violino está baixinho.
L: Then play it a little louder.|Então toque um pouco mais alto.
L: Now sing a soft song, Rosita.|Agora cante uma canção suave, Rosita.
L: Like this? La, la, la...|Assim? Lá, lá, lá...
L: Perfect. The theater loves it!|Perfeito. O teatro adora!
Q: What is too loud?|O que está alto demais?|0|🥁 The drum|🔔 The bell|🎻 The violin
Q: How is the bell?|Como é o sino?|2|🔔 Soft|🔔 Too loud|🔔 Broken
Q: What does Buster ask Rosita to sing?|O que o Buster pede para a Rosita cantar?|5|🎼 A soft song|🎼 A loud song|🎼 No song
B: play|🎺|tocar|I play the trumpet.|She plays the trumpet.|He played a song.|Ele tocou uma canção.
B: listen|👂|ouvir|I listen to the bell.|She listens to the bell.|We listened to the violin.|Nós ouvimos o violino.
B: whisper|🤫|sussurrar|I whisper a song.|She whispers a song.|He whispered softly.|Ele sussurrou baixinho.
B: tune|🎼|afinar|I tune the violin.|She tunes the violin.|They tuned the drum.|Eles afinaram o tambor.
LAB: dr|Laboratório de sons: drum, trumpet e violin|Drum soa “DRÂM”. Trumpet soa “TRÂM-pit”. Violin tem a força no fim, “vai-o-LÍN”.|Em trumpet, o u soa como â: TRÂM-pit.
W: drum|DRÂM|tambor|u = â|dram|DRÉM
W: trumpet|TRÂM-pit|trombeta|u = â|trumpets|TRÂM-pits
W: violin|vai-o-LÍN|violino|força no fim|violent|VÁI-o-lent
G: 0|loud|loudly|louder
G: 1|too|to|two
G: 2|soft|softly|soften
G: 3|quiet|quite|quietly
X: 🤫|Shh|Shh|pedir silêncio|Shh, the show starts.|Shh, o show vai começar.
X: 👏|Bravo|Bravo|elogiar|Bravo, Rosita!|Bravo, Rosita!
X: 🎶|Turn it down|Abaixe o volume|pedir|Turn it down, please.|Abaixe o volume, por favor.
X: 😊|Not bad|Nada mal|opinar|Not bad, try again.|Nada mal, tente de novo.

N: 910024
C: Tom,Kate | tom,polly | Na cozinha de uma casa cheia, Tom e Kate dividem as tarefas: take out the trash, clean the floor, cook dinner.
S: tarefas de casa: Take out the trash. Clean the floor. Cook dinner
Y: Hoje você aprende as tarefas de casa: take out the trash (levar o lixo para fora), clean the floor (limpar o chão), cook dinner (fazer o jantar).
F: Cheaper by the Dozen | 🎬 Filme | 2003 | uma comédia de família dirigida por Shawn Levy, sobre pais que cuidam de doze filhos numa casa bem movimentada | dividir as tarefas de casa | bakery | 🏠,🧹,🍝
V: 🗑️|trash|lixo|TRÉSH
V: 🧹|broom|vassoura|BRÚM
V: 🍝|dinner|jantar|DÍ-ner
V: 🍽️|dishes|louça|DÍ-shiz
V: 🪣|bucket|balde|BÂ-kit
V: 🛏️|beds|camas|BÉDZ
H: Take out the trash.|Leve o lixo para fora.
H: Clean the floor with the broom.|Limpe o chão com a vassoura.
H: Cook dinner in the big pan.|Faça o jantar na panela grande.
H: Wash the dishes after dinner.|Lave a louça depois do jantar.
H: Fill the bucket with water.|Encha o balde com água.
L: Kate, we have a lot to do today.|Kate, temos muito o que fazer hoje.
L: Tom, take out the trash.|Tom, leve o lixo para fora.
L: Okay. Then I clean the floor with the broom.|Certo. Depois eu limpo o chão com a vassoura.
L: Good. I cook dinner in the big pan.|Bom. Eu faço o jantar na panela grande.
L: Kids, wash the dishes after dinner.|Crianças, lavem a louça depois do jantar.
L: Fill the bucket with water first.|Encham o balde com água primeiro.
L: And make the beds, please.|E arrumem as camas, por favor.
L: Great team! Dinner is ready.|Ótimo time! O jantar está pronto.
Q: Who takes out the trash?|Quem leva o lixo para fora?|1|🗑️ Tom|🍝 Kate|🧹 The kids
Q: Who cooks dinner?|Quem faz o jantar?|3|🍝 Kate|🗑️ Tom|🪣 The kids
Q: What do the kids do after dinner?|O que as crianças fazem depois do jantar?|4|🍽️ Wash the dishes|🧹 Clean the floor|🗑️ Take out the trash
B: sweep|🧹|varrer|I sweep the floor.|She sweeps the floor.|He swept the kitchen.|Ele varreu a cozinha.
B: wipe|🧽|limpar com pano|I wipe the table.|She wipes the table.|They wiped the dishes.|Eles enxugaram a louça.
B: carry|💪|carregar|I carry the bucket.|He carries the bucket.|She carried the bags.|Ela carregou as sacolas.
B: tidy|🛏️|arrumar|I tidy my bed.|She tidies her bed.|We tidied the room.|Nós arrumamos o quarto.
LAB: tr|Laboratório de sons: trash, broom e bucket|Trash soa “TRÉSH”. Broom tem u longo, “BRÚM”. Bucket soa “BÂ-kit”.|Em trash, o a soa é: TRÉSH.
W: trash|TRÉSH|lixo|a = é|trace|TRÊIS
W: broom|BRÚM|vassoura|oo = ú|bloom|BLÚM
W: bucket|BÂ-kit|balde|u = â|bracket|BRÉ-kit
G: 0|Take out|Take off|Take in
G: 1|Clean|Cleans|Cleaning
G: 2|Cook|Cooks|Cooking
G: 3|Wash|Washes|Washing
X: 💪|Let’s go|Vamos|animar|Let’s go, team!|Vamos, time!
X: 😅|Almost done|Quase pronto|avisar|Almost done, kids.|Quase pronto, crianças.
X: 👍|Good job|Bom trabalho|elogiar|Good job, everyone.|Bom trabalho, pessoal.
X: 🙏|Thanks for help|Obrigado pela ajuda|agradecer|Thanks for help, Tom.|Obrigada pela ajuda, Tom.
''')
