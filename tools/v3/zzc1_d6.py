# Lote C do A1, dados 6 (n 80288 … 7080295). Ver zzc1_lib.py para o formato.
from v3.zzc1_lib import parse

N = []
N.append(parse("""
N 80288
C Dilbert,Alice | tom,polly | O Dilbert e a Alice decidem o que imprimir, copiar e digitalizar no escritório.
F Dilbert | 💬 Tirinha | 1989 | uma tirinha de Scott Adams sobre Dilbert, um engenheiro de escritório, e colegas como Alice e Wally, em empresas cheias de máquinas e reuniões. | usar a impressora, a copiadora e o scanner | office | 🖨️,💻,☕
V 🖨️|printer|impressora|PRÍN-ter
V 📠|copier|copiadora|KÓ-pi-er
V 🔍|scanner|scanner|SKÉ-ner
V 🖋️|ink|tinta|ÍNK
V 📄|document|documento|DÓ-kiu-ment
V 📃|page|página|PÊIDJ
L Alice, should I print this document?|Alice, eu devo imprimir este documento?
L The printer is busy.|A impressora está ocupada.
L Then I use the copier.|Então eu uso a copiadora.
L Good. Scan it on the scanner first.|Bom. Digitalize primeiro no scanner.
L Oh no! There is no ink.|Ai, não! Não tem tinta.
L Wally has ink. Ask Wally.|O Wally tem tinta. Pergunte ao Wally.
L Wally is on a break.|O Wally está no intervalo.
L Print one page and copy it.|Imprima uma página e copie.
H 1,2,3,4,0
Q What is busy?|O que está ocupado?|1|🖨️ The printer|📠 The copier|🔍 The scanner
Q What is missing?|O que está faltando?|4|🖋️ Ink|📄 Paper|🔌 A plug
Q Who is on a break?|Quem está no intervalo?|6|👨 Wally|👩 Alice|🤓 Dilbert
B print|🖨️|imprimir|a document|Dilbert prints a document.|O Dilbert imprime um documento.
B copy|📠|copiar|a page|Alice copies a page.|A Alice copia uma página.
B scan|🔍|digitalizar|a letter|Dilbert scans a letter.|O Dilbert digitaliza uma carta.
B send|📤|enviar|the file|Alice sends the file.|A Alice envia o arquivo.
LAB pr|Em printer, i soa í; em page, a soa êi.|Printer e painter têm sons diferentes.
W printer|PRÍN-ter|impressora|i = í|painter|PÊIN-ter
W ink|ÍNK|tinta|i = í|inch|ÍNTCH
W page|PÊIDJ|página|a = êi|pig|PÍG
G 4|print|prints|printed
G 1|use|uses|using
G 2|Scan|Scans|Scanning
G 3|no|any|not
X ⏳|Just a minute.|Só um minuto.|Pede um tempo.|Just a minute. I scan it now.|Só um minuto. Eu digitalizo agora.
X 😌|No problem.|Sem problema.|Responde a um pedido.|No problem. I copy it.|Sem problema. Eu copio.
X 💡|Good idea.|Boa ideia.|Aprova uma sugestão.|Good idea. Let’s print two pages.|Boa ideia. Vamos imprimir duas páginas.
X 🙏|Thank you, Alice.|Obrigado, Alice.|Agradece a ajuda.|Thank you, Alice. You are kind.|Obrigado, Alice. Você é gentil.
"""))

N.append(parse("""
N 7080288
C Felipe,Manny | tommy,tom | O Felipe oferece ajuda ao Manny com perguntas simples e o Manny responde: sim ou “eu dou conta”.
F Handy Manny | 📺 Série infantil | 2006 | um seriado infantil da Disney sobre Manny, um consertador gentil, e seu ajudante Felipe, que consertam coisas com ferramentas falantes. | oferecer ajuda e responder “I can manage” | office | 🔨,🪜,🧰
V 🔨|hammer|martelo|HÉ-mer
V 🪜|ladder|escada|LÉ-der
V 📍|nail|prego|NÊIL
V 🧱|wall|parede|UÓL
V 🧰|toolbox|caixa de ferramentas|TÚL-box
V 🧒|helper|ajudante|HÉL-per
L Manny, do you need help?|Manny, você precisa de ajuda?
L Yes, please. Pass me the hammer.|Sim, por favor. Me passe o martelo.
L Here is the hammer. Where is the ladder?|Aqui está o martelo. Cadê a escada?
L No, thanks. I can manage the ladder.|Não, obrigado. Eu dou conta da escada.
L Do you need a nail?|Você precisa de um prego?
L Yes, I need a nail for the wall.|Sim, eu preciso de um prego para a parede.
L Here is the toolbox.|Aqui está a caixa de ferramentas.
L Thanks, helper! We can fix it.|Obrigado, ajudante! Nós podemos consertar.
H 1,3,4,5,6
Q What does Manny need first?|Do que o Manny precisa primeiro?|1|🔨 The hammer|🪜 The ladder|🧰 The toolbox
Q Who can manage the ladder?|Quem dá conta da escada?|3|🧑‍🔧 Manny|🧒 Felipe|🤷 Nobody
Q What does Felipe bring?|O que o Felipe traz?|6|🧰 The toolbox|🔨 The hammer|🪜 The ladder
B need|🆘|precisar de|help|Manny needs help.|O Manny precisa de ajuda.
B help|🤝|ajudar|Manny|Felipe helps Manny.|O Felipe ajuda o Manny.
B manage|💪|dar conta de|the work|Manny manages the work.|O Manny dá conta do trabalho.
B call|📞|chamar|a helper|Manny calls a helper.|O Manny chama um ajudante.
LAB ha|Em hammer, a soa é; em wall, a soa ó.|Hammer e hamper têm sons diferentes.
W hammer|HÉ-mer|martelo|a = é|hamper|HÉM-per
W ladder|LÉ-der|escada|a = é|leader|LÍI-der
W wall|UÓL|parede|a = ó|well|UÉL
G 1|manage|manages|managed
G 2|Do|Does|Are
G 0|Pass|Passes|Passing
G 3|need|needs|needed
X 🙏|Yes, please.|Sim, por favor.|Aceita ajuda.|Yes, please. I need a hand.|Sim, por favor. Eu preciso de uma mão.
X 🙅|No, thanks.|Não, obrigado.|Recusa ajuda com educação.|No, thanks. I can do it.|Não, obrigado. Eu consigo.
X 😄|Thanks a lot!|Muito obrigado!|Agradece com vontade.|Thanks a lot! The wall is done.|Muito obrigado! A parede está pronta.
X 💪|Can do!|Dá para fazer!|Mostra disposição.|Can do! I fix it fast.|Dá para fazer! Eu conserto rápido.
"""))

N.append(parse("""
N 80289
C Liz,Kenneth | polly,tom | A Liz pede o ramal e o Kenneth transfere a ligação na central telefônica.
F 30 Rock | 📺 Série | 2006 | uma comédia americana sobre Liz Lemon, roteirista de um programa de TV, e os colegas de trabalho, como o ajudante Kenneth. | transferir ligações e pedir o ramal | lobby1 | 📞,📺,🏢
V 🔢|extension|ramal|ik-STÉN-xân
V 📞|line|linha|LÁIN
V 🧑‍💼|operator|telefonista|Ó-pe-rei-ter
V ⏸️|hold|espera|HÔULD
V 🏢|department|departamento|di-PÁRT-ment
V 🎛️|switchboard|central telefônica|SUÍTCH-bórd
L Kenneth, dial extension twelve.|Kenneth, disque o ramal doze.
L The line is busy, Liz.|A linha está ocupada, Liz.
L Ask the operator.|Pergunte à telefonista.
L Please hold.|Aguarde, por favor.
L Transfer me to the sales department.|Transfira-me para o departamento de vendas.
L I put you through on the switchboard.|Eu completo a ligação na central.
L Thank you. Which extension is it?|Obrigada. Qual é o ramal?
L It is extension twelve. Have a nice day!|É o ramal doze. Tenha um bom dia!
H 0,1,2,3,4
Q Which extension does Liz dial?|Qual ramal a Liz disca?|0|1️⃣2️⃣ Twelve|1️⃣ One|5️⃣ Five
Q What is busy?|O que está ocupado?|1|📞 The line|🏢 The department|🧑‍💼 The operator
Q Where does Liz want to go?|Para onde a Liz quer ir?|4|🛒 To the sales department|🏦 To the bank|🍕 To the kitchen
B transfer|🔁|transferir|the call|Kenneth transfers the call.|O Kenneth transfere a ligação.
B hold|⏸️|aguardar|the line|Liz holds the line.|A Liz aguarda na linha.
B dial|☎️|discar|a number|Kenneth dials a number.|O Kenneth disca um número.
B put through|📞|completar a ligação de|the call|Kenneth puts through the call.|O Kenneth completa a ligação.
LAB ex|Em extension, ex soa iks; em line, i soa ái.|Line e lane têm sons diferentes.
W extension|ik-STÉN-xân|ramal|ex = iks|expansion|iks-PÉN-xân
W hold|HÔULD|aguardar|o = ôu|held|HÉLD
W line|LÁIN|linha|i = ái|lane|LÊIN
G 0|dial|dials|dialed
G 1|busy|bus|busily
G 3|hold|holds|holding
G 4|to|at|in
X 🙂|One moment, please.|Um momento, por favor.|Pede para esperar.|One moment, please. I check.|Um momento, por favor. Eu verifico.
X 🌞|Have a nice day!|Tenha um bom dia!|Despede-se com carinho.|Have a nice day, Liz!|Tenha um bom dia, Liz!
X 📞|Hello?|Alô?|Atende o telefone.|Hello? This is Kenneth.|Alô? Aqui é o Kenneth.
X 🙏|Thank you.|Obrigada.|Agradece.|Thank you. You put me through.|Obrigada. Você completou a ligação.
"""))

N.append(parse("""
N 7080289
C Lou,Mary | tom,misshoney | O Lou liga e a Mary atende: “Aqui é a Mary falando. Um momento, por favor.”
F The Mary Tyler Moore Show | 📺 Série | 1970 | uma comédia americana sobre Mary Richards, que trabalha numa redação de TV e tem como chefe o rabugento Lou Grant. | atender e pedir alguém ao telefone | office | ☎️,📺,🧣
V 🗣️|speaking|falando|SPÍI-kin
V 🚫|available|disponível|a-VÊI-la-bol
V 👔|manager|gerente|MÉ-ni-djer
V ⏳|moment|momento|MÔU-ment
V 🤝|reach|alcançar|RÍITCH
V 💬|message|recado|MÉ-sidj
L Hello. Can I speak to the manager?|Alô. Posso falar com o gerente?
L This is Mary speaking.|Aqui é a Mary falando.
L I want the manager, please.|Eu quero o gerente, por favor.
L One moment, please.|Um momento, por favor.
L How can I reach him?|Como posso falar com ele?
L He is not available. Call back at three.|Ele não está disponível. Ligue de volta às três.
L Can I leave a message?|Posso deixar um recado?
L Of course. I write the message now.|Claro. Eu escrevo o recado agora.
H 1,5,2,3,4
Q Who does Lou want?|Quem o Lou quer?|2|👔 The manager|👩 Mary|🧑 A friend
Q Is the manager available?|O gerente está disponível?|5|❌ No, he is not|✅ Yes, he is|🤷 Maybe
Q What does Lou leave?|O que o Lou deixa?|6|💬 A message|🎁 A gift|📦 A box
B speak|🗣️|falar|to the manager|Lou speaks to the manager.|O Lou fala com o gerente.
B call|📞|ligar|at three|Lou calls at three.|O Lou liga às três.
B leave|💬|deixar|a message|Lou leaves a message.|O Lou deixa um recado.
B reach|🤝|encontrar|him|Mary reaches him.|A Mary encontra ele.
LAB ma|Em manager, a soa é e g soa dj; em moment, o soa ôu.|Moment e movement têm sons diferentes.
W manager|MÉ-ni-djer|gerente|a = é; g = dj|manner|MÉ-ner
W moment|MÔU-ment|momento|o = ôu|movement|MÚV-ment
W message|MÉ-sidj|recado|age = idj|massage|ma-SÁJ
G 0|speaking|speak|speaks
G 1|not|no|nor
G 2|want|wants|wanting
G 4|How|What|Who
X 📞|Hello?|Alô?|Atende o telefone.|Hello? This is Mary.|Alô? Aqui é a Mary.
X 👍|Of course.|Claro.|Aceita um pedido.|Of course. I write it down.|Claro. Eu anoto.
X 🙏|Thank you.|Obrigado.|Agradece.|Thank you. Goodbye.|Obrigado. Tchau.
X ✋|Hold on.|Espere um pouco.|Pede para esperar.|Hold on. I call him.|Espere um pouco. Eu chamo ele.
"""))

N.append(parse("""
N 7080292
C Jonah,Amy | tommy,polly | O Jonah e a Amy fazem uma pausa para o café na copa da loja.
F Superstore | 📺 Série | 2015 | uma comédia americana passada numa grande loja, com funcionários como Amy e Jonah, que conversam e fazem pausas na copa. | falar da copa e da pausa para o café | office | 🛒,☕,🏪
V 🚪|break room|copa|BRÊIK RÚM
V ☕|coffee|café|KÓ-fi
V 🔥|microwave|micro-ondas|MÁI-kro-uêiv
V 🥤|vending machine|máquina de lanches|VÉN-din ma-XÍIN
V 🫖|kettle|chaleira|KÉ-tol
V 🍱|lunch|almoço|LÂNTCH
L Let’s go to the break room, Amy.|Vamos para a copa, Amy.
L Good. I need a drink.|Bom. Eu preciso de uma bebida.
L Use the microwave for lunch.|Use o micro-ondas para o almoço.
L The vending machine has snacks.|A máquina de lanches tem petiscos.
L The kettle is hot.|A chaleira está quente.
L Let’s take a coffee break.|Vamos fazer uma pausa para o café.
L I have a lunch break at noon.|Eu tenho o intervalo de almoço ao meio-dia.
L Our break is short. Come on!|O nosso intervalo é curto. Vamos!
H 0,5,2,3,4
Q What does Amy suggest?|O que a Amy sugere?|5|☕ A coffee break|🍔 Lunch|🏠 Going home
Q What has snacks?|O que tem petiscos?|3|🥤 The vending machine|🔥 The microwave|🫖 The kettle
Q When is Jonah’s lunch break?|Quando é o intervalo de almoço do Jonah?|6|🕛 At noon|🕙 At ten|🕒 At three
B take|☕|fazer|a break|Amy takes a break.|A Amy faz uma pausa.
B drink|🥤|beber|coffee|Jonah drinks coffee.|O Jonah bebe café.
B warm|🔥|esquentar|lunch|Amy warms lunch.|A Amy esquenta o almoço.
B chat|💬|conversar|with Amy|Jonah chats with Amy.|O Jonah conversa com a Amy.
LAB co|Em coffee, o soa ó; em microwave, i soa ái.|Coffee e copy têm sons diferentes.
W coffee|KÓ-fi|café|o = ó|copy|KÓ-pi
W microwave|MÁI-kro-uêiv|micro-ondas|i = ái|microphone|MÁI-kro-fôun
W kettle|KÉ-tol|chaleira|e = é|kennel|KÉ-nol
G 0|break|brake|breaks
G 1|take|takes|taking
G 2|Use|Uses|Using
G 3|has|have|having
X 🏃|Come on!|Vamos lá!|Chama alguém.|Come on! The break is short.|Vamos lá! O intervalo é curto.
X ⏳|Just a minute.|Só um minuto.|Pede um tempo.|Just a minute. The coffee is hot.|Só um minuto. O café está quente.
X 💡|Good idea.|Boa ideia.|Aprova uma sugestão.|Good idea. Let’s eat lunch.|Boa ideia. Vamos almoçar.
X 👋|See you later.|Até mais tarde.|Despede-se.|See you later, Amy.|Até mais tarde, Amy.
"""))

N.append(parse("""
N 7910036
C Abigail,Sebastian | polly,tommy | A Abigail, que acorda cedo, e o Sebastian, que dorme tarde, comparam seus hábitos na fazenda.
F Stardew Valley | 🎮 Videogame | 2016 | um jogo de fazenda criado por ConcernedApe em que o jogador cuida de uma roça e faz amizade com os moradores, como Abigail e Sebastian. | falar de quem acorda cedo e de quem dorme tarde | bedroom | 🌾,🌙,🦉
V 🦉|owl|coruja|ÁUL
V 🐦|early bird|quem acorda cedo|ÂR-li BÂRD
V 🌙|midnight|meia-noite|MÍD-náit
V 🌅|sunrise|nascer do sol|SÂN-ráiz
V ⏰|alarm|despertador|a-LÁRM
V 🌾|farm|fazenda|FÁRM
L Sebastian, are you a night owl?|Sebastian, você é uma coruja da noite?
L Yes, I am a night owl.|Sim, eu sou uma coruja da noite.
L I am an early bird.|Eu sou do tipo que acorda cedo.
L I sleep after midnight.|Eu durmo depois da meia-noite.
L I watch the sunrise on the farm.|Eu vejo o nascer do sol na fazenda.
L My alarm is loud at six.|O meu despertador é alto às seis.
L The farmer is an early bird too.|O fazendeiro também acorda cedo.
L Good morning, Abigail.|Bom dia, Abigail.
H 1,2,3,4,5
Q Is Sebastian a night owl?|O Sebastian é uma coruja da noite?|1|✅ Yes|❌ No|🤷 Maybe
Q What is Abigail?|O que a Abigail é?|2|🐦 An early bird|🦉 A night owl|🐔 A hen
Q When does Sebastian sleep?|Quando o Sebastian dorme?|3|🌙 After midnight|🌅 At sunrise|☀️ At noon
B wake up|⏰|acordar|at six|Abigail wakes up at six.|A Abigail acorda às seis.
B go to bed|🛏️|ir dormir|late|Sebastian goes to bed late.|O Sebastian vai dormir tarde.
B work|🧑‍🌾|trabalhar|on the farm|The farmer works on the farm.|O fazendeiro trabalha na fazenda.
B sleep|😴|dormir|a lot|Sebastian sleeps a lot.|O Sebastian dorme muito.
LAB ow|Em owl, ow soa áu; em farm, ar soa ár.|Owl e oil têm sons diferentes.
W owl|ÁUL|coruja|ow = áu|oil|ÓIL
W sunrise|SÂN-ráiz|nascer do sol|u = â|sunset|SÂN-sét
W farm|FÁRM|fazenda|ar = ár|form|FÓRM
G 0|owl|bird|cow
G 1|an|a|the
G 2|after|in|on
G 3|watch|watches|watching
X 🌞|Good morning!|Bom dia!|Cumprimenta de manhã.|Good morning! The sun is up.|Bom dia! O sol nasceu.
X 🌙|Good night!|Boa noite!|Despede-se à noite.|Good night! I sleep now.|Boa noite! Eu vou dormir.
X 🙌|Me too!|Eu também!|Concorda com o outro.|Me too! I love the night.|Eu também! Eu amo a noite.
X 😮|Really?|Sério?|Mostra surpresa.|Really? You sleep late?|Sério? Você dorme tarde?
"""))

N.append(parse("""
N 7080293
C Morticia,Gomez | misshoney,tom | A Morticia e o Gomez leem os avisos da casa: proibido fumar, correr, comer e nadar.
F The Addams Family | 📺 Série | 1964 | uma comédia americana sobre a família Addams, esquisita e simpática, com Gomez, Morticia, Wednesday, Pugsley e o tio Fester, baseada em cartuns de Charles Addams. | ler avisos de proibição com No + -ing | lobby1 | 🏚️,🕷️,🪦
V 🚭|smoking|fumar|SMÓU-kin
V 🏃|running|correr|RÂ-nin
V 🍔|eating|comer|Í-tin
V 🏊|swimming|nadar|SUÍ-min
V 📢|shouting|gritar|XÁU-tin
V 🪧|sign|placa|SÁIN
L Gomez, read the sign. No smoking here.|Gomez, leia a placa. Proibido fumar aqui.
L Yes, my dear. No smoking!|Sim, minha querida. Proibido fumar!
L There is also a sign: No running inside.|Também tem uma placa: Proibido correr aqui dentro.
L Fester runs in the hall!|O Fester corre no corredor!
L No eating in the library, please.|Proibido comer na biblioteca, por favor.
L And no swimming in the pond today.|E proibido nadar no lago hoje.
L There is a “No shouting” sign too.|Tem uma placa “Proibido gritar” também.
L What a long list of signs!|Que lista longa de placas!
H 0,2,4,5,6
Q What is the first sign?|Qual é a primeira placa?|0|🚭 No smoking|🏃 No running|🍔 No eating
Q Where is “No eating”?|Onde é o “Proibido comer”?|4|📚 In the library|🛁 In the bath|🛏️ In bed
Q Where is no swimming?|Onde é proibido nadar?|5|🏊 In the pond|🛁 In the bath|🏖️ At the beach
B obey|✅|obedecer|the sign|Morticia obeys the sign.|A Morticia obedece à placa.
B smoke|🚬|fumar|a cigar|Gomez smokes a cigar.|O Gomez fuma um charuto.
B run|🏃|correr|in the hall|Fester runs in the hall.|O Fester corre no corredor.
B swim|🏊|nadar|in the pond|Pugsley swims in the pond.|O Pugsley nada no lago.
LAB sg|Em sign, o g não soa; em running, u soa â.|Sign e sin têm sons diferentes.
W sign|SÁIN|placa|g mudo|sin|SÍN
W swimming|SUÍ-min|nadar|w + i|swinging|SUÍN-guin
W running|RÂ-nin|correr|u = â|ranging|RÊIN-djin
G 0|No|Not|Non
G 1|running|run|runs
G 2|eating|eat|eats
G 3|swimming|swim|swims
X 💕|My dear.|Minha querida.|Chama alguém com carinho.|My dear, read the list.|Minha querida, leia a lista.
X 📜|What a list!|Que lista!|Reage a uma lista longa.|What a list! Ten signs!|Que lista! Dez placas!
X 👍|Of course.|Claro.|Concorda.|Of course. No running.|Claro. Proibido correr.
X 🤫|Be quiet!|Fique quieto!|Pede silêncio.|Be quiet! No shouting here.|Fique quieto! Proibido gritar aqui.
"""))

N.append(parse("""
N 80294
C Dipper,Mabel | tommy,polly | O Dipper e a Mabel dizem o que cada um está fazendo agora na Cabana do Mistério.
F Gravity Falls | 📺 Série animada | 2012 | um seriado animado da Disney criado por Alex Hirsch sobre os irmãos gêmeos Dipper e Mabel, que passam as férias numa cidade cheia de mistérios. | dizer o que você está fazendo agora | living | 🏚️,📓,🧶
V 🧶|sweater|suéter|SUÉ-ter
V ⏱️|moment|momento|MÔU-ment
V 📓|journal|diário|DJÂR-nal
V 🏚️|shack|cabana|XÉK
V 🍪|snack|lanche|SNÉK
V 👹|monster|monstro|MÓN-ster
L Mabel, what are you doing right now?|Mabel, o que você está fazendo agora?
L I am making a sweater right now.|Eu estou fazendo um suéter agora.
L I am busy at the moment.|Eu estou ocupado neste momento.
L Are you reading the journal?|Você está lendo o diário?
L Yes. Soos is fixing the shack.|Sim. O Soos está consertando a cabana.
L And Grunkle Stan is eating a snack.|E o tio Stan está comendo um lanche.
L Look! A monster is running in the forest!|Olhe! Um monstro está correndo na floresta!
L It is running to the shack. Oh no!|Ele está correndo para a cabana. Ai, não!
H 1,2,3,4,5
Q What is Mabel making?|O que a Mabel está fazendo?|1|🧶 A sweater|🍰 A cake|🎨 A picture
Q Who is fixing the shack?|Quem está consertando a cabana?|4|👷 Soos|👴 Stan|👦 Dipper
Q Where is the monster running?|Para onde o monstro está correndo?|7|🏚️ To the shack|🌲 To the forest|🏫 To school
B make|🧶|fazer|a sweater|Mabel makes a sweater.|A Mabel faz um suéter.
B read|📖|ler|the journal|Dipper reads the journal.|O Dipper lê o diário.
B fix|🔧|consertar|the shack|Soos fixes the shack.|O Soos conserta a cabana.
B eat|🍪|comer|a snack|Stan eats a snack.|O Stan come um lanche.
LAB sw|Em sweater, ea soa é; em monster, o soa ó.|Sweater e sweeter têm sons diferentes.
W sweater|SUÉ-ter|suéter|ea = é|sweeter|SUÍI-ter
W snack|SNÉK|lanche|a = é|snake|SNÊIK
W monster|MÓN-ster|monstro|o = ó|master|MÉS-ter
G 0|making|make|makes
G 1|at|on|in
G 2|Are|Is|Do
G 3|fixing|fix|fixes
X 👀|Look!|Olhe!|Chama a atenção.|Look! The monster is big.|Olhe! O monstro é grande.
X 😱|Oh no!|Ai, não!|Mostra susto.|Oh no! He is here.|Ai, não! Ele está aqui.
X 🏃|Hurry!|Depressa!|Apressa alguém.|Hurry! Close the door.|Depressa! Feche a porta.
X 🤩|Wow!|Uau!|Mostra admiração.|Wow! What a big monster!|Uau! Que monstro grande!
"""))

N.append(parse("""
N 7080294
C Po,Dipsy | polly,tom | O Po e o Dipsy olham o céu, veem um arco-íris e assistem à tela na barriga.
F Teletubbies | 📺 Série infantil | 1997 | um seriado infantil da BBC sobre quatro bonecos coloridos, como Po e Dipsy, que vivem numa colina e têm uma tela na barriga. | diferenciar look at, watch e see | park | 🌈,📺,🌞
V ☁️|sky|céu|SKÁI
V 🌈|rainbow|arco-íris|RÊIN-bou
V 🐦|bird|pássaro|BÂRD
V 📺|screen|tela|SKRÍIN
V 🌞|sun|sol|SÂN
V ⛰️|hill|colina|HÍL
L Dipsy, look at the sky.|Dipsy, olhe para o céu.
L I see a rainbow!|Eu vejo um arco-íris!
L Look at the rainbow. It is big.|Olhe para o arco-íris. Ele é grande.
L I see a bird too.|Eu vejo um pássaro também.
L Watch the bird. It flies.|Observe o pássaro. Ele voa.
L Watch the screen on my tummy.|Assista à tela na minha barriga.
L I see the sun on the hill.|Eu vejo o sol na colina.
L Look, watch, see. Fun!|Olhar, assistir, ver. Divertido!
H 0,1,4,5,6
Q What does Dipsy see?|O que o Dipsy vê?|1|🌈 A rainbow|🌞 The sun|🐦 A bird
Q What do they watch?|O que eles observam?|4|🐦 The bird|🌈 The rainbow|📺 The sky
Q Where is the sun?|Onde está o sol?|6|⛰️ On the hill|☁️ In a cloud|🏠 At home
B look|👀|olhar|at the sky|Po looks at the sky.|O Po olha para o céu.
B watch|📺|assistir|the screen|Dipsy watches the screen.|O Dipsy assiste à tela.
B see|🌈|ver|a rainbow|Po sees a rainbow.|O Po vê um arco-íris.
B notice|👁️|reparar em|a bird|Dipsy notices a bird.|O Dipsy repara num pássaro.
LAB sk|Em sky e screen, sk soa sk; em rainbow, ai soa êi.|Sky e ski têm sons diferentes.
W sky|SKÁI|céu|y = ái|ski|SKÍI
W rainbow|RÊIN-bou|arco-íris|ai = êi|raincoat|RÊIN-kout
W screen|SKRÍIN|tela|ee = íi|scream|SKRÍIM
G 0|at|on|to
G 1|see|look|watch
G 2|Watch|Watchs|Watching
G 4|see|look|looks
X 🔁|Again!|De novo!|Pede para repetir.|Again! I see the bird.|De novo! Eu vejo o pássaro.
X 👋|Hello!|Olá!|Cumprimenta.|Hello! I am Po.|Olá! Eu sou o Po.
X 👀|Look!|Olhe!|Chama a atenção.|Look! A big sun!|Olhe! Um sol grande!
X 🤗|Big hug!|Abraço grande!|Convida para um abraço.|Big hug! We are friends.|Abraço grande! Nós somos amigos.
"""))

N.append(parse("""
N 7080295
C Marle,Crono | polly,tommy | A Marle e o Crono falam de há quanto tempo viveram numa vila e visitaram o castelo.
F Chrono Trigger | 🎮 Videogame | 1995 | um jogo de aventura da Square sobre Crono, Marle e Lucca, que viajam no tempo por um portal e visitam o passado e o futuro. | datar o passado com ago | living | ⏳,🏰,🌀
V 🏡|village|vila|VÍ-lidj
V 🏰|castle|castelo|KÉ-sol
V 🕰️|past|passado|PÉST
V 🗓️|years|anos|IÍRZ
V 🔮|future|futuro|FIÚ-tcher
V 🌀|gate|portal|GÊIT
L Crono, I lived in a village two years ago.|Crono, eu morei numa vila há dois anos.
L I came to the castle two days ago.|Eu vim ao castelo há dois dias.
L A minute ago, we were in the past.|Há um minuto, estávamos no passado.
L Ten years ago, this place was a forest.|Há dez anos, este lugar era uma floresta.
L Look at the time gate. It is magic.|Olhe o portal do tempo. É mágico.
L The future is far, but the past is near.|O futuro é longe, mas o passado é perto.
L Three years ago, I was a princess.|Há três anos, eu era uma princesa.
L Now we are friends. Let’s go!|Agora somos amigos. Vamos!
H 0,1,2,3,5
Q When did Marle live in a village?|Quando a Marle morou numa vila?|0|2️⃣ Two years ago|1️⃣0️⃣ Ten years ago|🕐 A minute ago
Q When did Crono come to the castle?|Quando o Crono veio ao castelo?|1|📅 Two days ago|🗓️ Ten years ago|⏱️ A minute ago
Q What was this place ten years ago?|O que era este lugar há dez anos?|3|🌲 A forest|🏰 A castle|🏙️ A city
B live|🏡|morar|in a village|Marle lives in a village.|A Marle mora numa vila.
B come|🚶|vir|to the castle|Crono comes to the castle.|O Crono vem ao castelo.
B remember|🧠|lembrar de|the past|Marle remembers the past.|A Marle lembra do passado.
B travel|⏳|viajar|in time|They travel in time.|Eles viajam no tempo.
LAB ag|Em ago, o soa ôu; em years, ea soa íi.|Years e yours têm sons diferentes.
W ago|a-GÔU|atrás (tempo)|o = ôu|ego|Í-gou
W years|IÍRZ|anos|ea = íi|yours|IÓRZ
W gate|GÊIT|portal|a = êi|get|GÉT
G 0|ago|before|after
G 1|came|come|comes
G 2|were|was|are
G 3|years|year|yearly
X 🤩|Wow!|Uau!|Mostra admiração.|Wow! We are in the past.|Uau! Nós estamos no passado.
X 🚀|Let’s go!|Vamos lá!|Chama para ir.|Let’s go! The gate is open.|Vamos lá! O portal está aberto.
X 😱|Oh no!|Ai, não!|Mostra susto.|Oh no! We are lost in time.|Ai, não! Nós estamos perdidos no tempo.
X 🧓|Long ago.|Há muito tempo.|Fala de um passado distante.|Long ago, this was a village.|Há muito tempo, isto era uma vila.
"""))
