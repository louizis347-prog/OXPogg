# Lote C do A1, dados 10 (n 7910042 … 7910047). Ver zzc1_lib.py para o formato.
from v3.zzc1_lib import parse

N = []
N.append(parse("""
N 7910042
C Richie,Fonzie | tommy,tom | O Richie começa um emprego novo e o Fonzie lhe deseja o melhor com um cartão.
F Happy Days | 📺 Série | 1974 | uma comédia americana sobre Richie Cunningham, sua família e o amigo descolado Fonzie, nos anos 1950. | desejar o melhor a alguém | office | 🎸,🎶,🏍️
V ⭐|wish|desejo|UÍSH
V 🔮|future|futuro|FIÚ-tcher
V ❤️‍🩹|health|saúde|HÉLTH
V 😊|happiness|felicidade|HÉ-pi-nes
V 🍀|luck|sorte|LÂK
V 💌|card|cartão|KÁRD
L Fonzie, make a wish.|Fonzie, faça um desejo.
L Best wishes for your new job, Richie!|Os melhores votos pelo seu emprego novo, Richie!
L The future is bright.|O futuro é brilhante.
L Health is important. All the best!|Saúde é importante. Tudo de bom!
L I wish you happiness.|Eu desejo felicidade a você.
L And I wish you luck.|E eu desejo sorte a você.
L Here is a card for you.|Aqui está um cartão para você.
L Aaay! All the best, my friend.|Aaay! Tudo de bom, meu amigo.
H 0,2,3,4,5
Q Who has a new job?|Quem tem um emprego novo?|1|👦 Richie|🧑 Fonzie|👧 Joanie
Q What is important?|O que é importante?|3|❤️‍🩹 Health|💰 Money|🚗 Cars
Q What is the gift?|Qual é o presente?|6|💌 A card|🎂 A cake|🚗 A car
B wish|⭐|desejar|you luck|Fonzie wishes Richie luck.|O Fonzie deseja sorte ao Richie.
B sign|✍️|assinar|the card|Richie signs the card.|O Richie assina o cartão.
B start|🚀|começar|a new job|Richie starts a new job.|O Richie começa um emprego novo.
B follow|👣|seguir|a dream|Richie follows a dream.|O Richie segue um sonho.
LAB wi|Em wish, i soa í; em luck, u soa â.|Wish e which têm sons diferentes.
W wish|UÍSH|desejo|i = í|which|UÍTCH
W luck|LÂK|sorte|u = â|lock|LÓK
W card|KÁRD|cartão|ar = ár|cord|KÓRD
G 0|make|makes|making
G 1|is|are|am
G 2|best|good|better
G 3|wish|wishes|wished
X 😎|Aaay!|Aaay!|Exclamação de alegria do Fonzie.|Aaay! You did it.|Aaay! Você conseguiu.
X 🎉|Congratulations!|Parabéns!|Parabeniza.|Congratulations on the new job!|Parabéns pelo emprego novo!
X 🍀|Good luck!|Boa sorte!|Deseja sorte.|Good luck, Richie!|Boa sorte, Richie!
X 🙏|Thank you!|Obrigado!|Agradece.|Thank you for the card!|Obrigado pelo cartão!
"""))

N.append(parse("""
N 7080340
C John-Boy,Grandpa | tommy,tom | O John-Boy e o vovô veem a mesa da família com bastante comida, mas faltam pratos.
F The Waltons | 📺 Série | 1972 | uma série americana sobre a família Walton, que vive nas montanhas da Virgínia durante a Grande Depressão, com o filho John-Boy e os avós. | falar de quantidade: plenty of e enough | diner | 🏡,🍞,🥔
V 🥔|potatoes|batatas|po-TÊI-touz
V 🌽|corn|milho|KÓRN
V 🍞|bread|pão|BRÉD
V 🥣|gravy|molho|GRÊI-vi
V 🫐|cranberries|oxicocos|KRÉN-bé-riz
V 🍽️|plate|prato|PLÊIT
L Grandpa, we have plenty of potatoes.|Vovô, temos bastante batata.
L Is there enough corn?|Tem milho suficiente?
L Yes. There is plenty of bread.|Sim. Tem bastante pão.
L I need more gravy.|Eu preciso de mais molho.
L Are there enough cranberries?|Tem oxicocos suficientes?
L There are not enough plates.|Não tem pratos suficientes.
L I have ten plates in the kitchen.|Eu tenho dez pratos na cozinha.
L Good! We have plenty of food.|Bom! Temos bastante comida.
H 0,1,2,3,4
Q What do they have plenty of?|De que eles têm bastante?|0|🥔 Potatoes|🐟 Fish|🍚 Rice
Q What does Grandpa need?|Do que o vovô precisa?|3|🥣 Gravy|🌽 Corn|🍞 Bread
Q What is missing?|O que está faltando?|5|🍽️ Plates|🍞 Bread|🌽 Corn
B have|🍽️|ter|plenty of food|They have plenty of food.|Eles têm bastante comida.
B need|🆘|precisar de|more gravy|Grandpa needs more gravy.|O vovô precisa de mais molho.
B take|🥄|pegar|a plate|John-Boy takes a plate.|O John-Boy pega um prato.
B eat|😋|comer|bread|Grandpa eats bread.|O vovô come pão.
LAB pl|Em plenty, e soa é; em plate, a soa êi.|Plenty e twenty têm sons diferentes.
W plenty|PLÉN-ti|bastante|e = é|twenty|TUÉN-ti
W bread|BRÉD|pão|ea = é|bride|BRÁID
W plate|PLÊIT|prato|a = êi|plot|PLÓT
G 0|plenty|twenty|plentiful
G 1|Is|Are|Be
G 2|of|for|at
G 4|Are|Is|Do
X 🍽️|Dig in!|Podem comer!|Convida para comer.|Dig in! There is plenty.|Podem comer! Tem bastante.
X 🙏|Thank you!|Obrigado!|Agradece.|Thank you for the food!|Obrigado pela comida!
X 🥖|Pass the bread.|Passe o pão.|Pede o pão.|Pass the bread, please.|Passe o pão, por favor.
X 😋|Yum!|Hum, que bom!|Mostra que gostou.|Yum! The gravy is great.|Hum, que bom! O molho é ótimo.
"""))

N.append(parse("""
N 910043
C Johnny,David | tom,tommy | O Johnny pergunta ao filho David como ele está de verdade, e o David responde: não muito bem.
F Schitt’s Creek | 📺 Série | 2015 | uma comédia canadense sobre uma família rica, os Rose, que perde tudo e vai morar numa cidade pequena e simples. | perguntar e responder como você está de verdade | cafe2 | 🏨,💛,🧶
V 😴|tired|cansado|TÁI-erd
V 😰|stressed|estressado|STRÉST
V 😢|sad|triste|SÉD
V 🆗|fine|bem|FÁIN
V 🤗|hug|abraço|HÂG
V 😟|worried|preocupado|UÂ-rid
L David, how are you, really?|David, como você está, de verdade?
L Not so good. I am tired.|Não muito bem. Eu estou cansado.
L Are you stressed?|Você está estressado?
L Yes. I feel stressed about the store.|Sim. Eu me sinto estressado com a loja.
L Are you sad?|Você está triste?
L I am a little sad. And worried.|Estou um pouco triste. E preocupado.
L Give me a hug. I am fine.|Me dê um abraço. Eu estou bem.
L Thanks, Dad. Now I am fine.|Obrigado, pai. Agora eu estou bem.
H 1,3,5,7,6
Q How is David?|Como o David está?|1|😴 Tired|😄 Happy|😠 Angry
Q What is he stressed about?|Com o que ele está estressado?|3|🏪 The store|🌦️ The weather|✈️ A trip
Q How is David at the end?|Como o David está no fim?|7|🆗 Fine|😢 Sad|🤒 Sick
B seem|🤔|parecer|tired|David seems tired.|O David parece cansado.
B look|👀|parecer|sad|David looks sad.|O David parece triste.
B worry|😰|preocupar-se|about the store|David worries about the store.|O David se preocupa com a loja.
B ask|❓|perguntar|a question|Johnny asks a question.|O Johnny faz uma pergunta.
LAB ti|Em tired, i soa ái; em worried, or soa âr.|Tired e tried têm sons diferentes.
W tired|TÁI-erd|cansado|i = ái|tried|TRÁID
W worried|UÂ-rid|preocupado|or = âr|weary|UÍ-ri
W hug|HÂG|abraço|u = â|hog|HÓG
G 0|Not|No|Nothing
G 1|feel|feels|feeling
G 2|little|less|lot
G 4|Give|Gives|Giving
X 🤗|I’m here for you.|Estou aqui por você.|Oferece apoio.|I’m here for you, David.|Estou aqui por você, David.
X 😌|It’s okay.|Tudo bem.|Acalma alguém.|It’s okay. Rest a little.|Tudo bem. Descanse um pouco.
X 🙏|Thanks, Dad.|Obrigado, pai.|Agradece ao pai.|Thanks, Dad. I feel better.|Obrigado, pai. Eu me sinto melhor.
X 👋|Take care.|Se cuide.|Despede-se com carinho.|Take care, David.|Se cuide, David.
"""))

N.append(parse("""
N 7910043
C Carol,Carter | misshoney,tom | A enfermeira Carol pergunta ao Dr. Carter como ele se sente e os dois falam de quem está melhor, doente ou calmo.
F ER | 📺 Série | 1994 | uma série americana de drama passada no pronto-socorro de um hospital, com médicos como John Carter e enfermeiras como Carol Hathaway. | descrever como você se sente com feel + adjetivo | bedroom | 🏥,🩺,💊
V 😊|better|melhor|BÉ-ter
V 🤒|sick|doente|SÍK
V 😠|angry|bravo|ÉN-gri
V 😔|lonely|sozinho|LÔUN-li
V 😌|calm|calmo|KÁM
V 🩺|doctor|médico|DÓK-ter
L Doctor Carter, how do you feel?|Doutor Carter, como o senhor se sente?
L I feel better, thanks.|Eu me sinto melhor, obrigado.
L The patient feels sick.|O paciente se sente doente.
L He feels angry too.|Ele também se sente bravo.
L She feels lonely here.|Ela se sente sozinha aqui.
L I feel calm. Let’s help them.|Eu me sinto calmo. Vamos ajudá-los.
L The doctor can help. Drink water and rest.|O médico pode ajudar. Beba água e descanse.
L Rest is good. Then you feel better.|Descansar faz bem. Depois você se sente melhor.
H 1,2,3,4,5
Q How does Carter feel?|Como o Carter se sente?|1|😊 Better|🤒 Sick|😠 Angry
Q Who feels lonely?|Quem se sente sozinha?|4|👩 The patient|👨 Carter|👩‍⚕️ Carol
Q What do they say to do?|O que dizem para fazer?|6|🥤 Drink water and rest|🏃 Run fast|🍕 Eat pizza
B feel|😌|sentir-se|better|Carter feels better.|O Carter se sente melhor.
B drink|🥤|beber|water|The patient drinks water.|O paciente bebe água.
B rest|🛌|descansar|a lot|Carol rests a lot.|A Carol descansa muito.
B sleep|😴|dormir|well|She sleeps well.|Ela dorme bem.
LAB be|Em better, e soa é; em calm, o l não soa.|Better e butter têm sons diferentes.
W better|BÉ-ter|melhor|e = é|butter|BÂ-ter
W sick|SÍK|doente|i = í|sock|SÓK
W calm|KÁM|calmo|l mudo|come|KÂM
G 0|feel|feels|feeling
G 1|feels|feel|feeling
G 2|angry|angrily|anger
G 4|calm|calmly|calms
X 💐|Get well soon.|Melhoras!|Deseja melhoras.|Get well soon, Carter.|Melhoras, Carter.
X 😌|Take it easy.|Vá com calma.|Aconselha descanso.|Take it easy today.|Vá com calma hoje.
X 🙏|Thank you, doctor.|Obrigada, doutor.|Agradece ao médico.|Thank you, doctor. I feel better.|Obrigada, doutor. Eu me sinto melhor.
X 😌|Don’t worry.|Não se preocupe.|Acalma alguém.|Don’t worry. You are safe here.|Não se preocupe. Você está seguro aqui.
"""))

N.append(parse("""
N 7080343
C Bitzer,Shaun | tom,tommy | O cão Bitzer pergunta ao Shaun o que os bichos estão fazendo: dançando, cantando, comendo e pintando.
F Shaun the Sheep | 📺 Série animada | 2007 | um desenho animado inglês da Aardman sobre Shaun, uma ovelha esperta, o cão Bitzer e o resto do rebanho numa fazenda, quase sem falas. | perguntar o que estão fazendo agora | park | 🐑,🐕,🚜
V 💃|dancing|dançando|DÉN-sin
V 🎤|singing|cantando|SÍN-guin
V 🍎|eating|comendo|Í-tin
V 🎨|painting|pintando|PÊIN-tin
V ⛺|tent|barraca|TÉNT
V 👨‍🌾|farmer|fazendeiro|FÁR-mer
L Shaun, are they dancing?|Shaun, eles estão dançando?
L Yes, they are dancing.|Sim, eles estão dançando.
L Are the sheep singing?|As ovelhas estão cantando?
L Yes, they are singing.|Sim, elas estão cantando.
L Is the pig eating?|O porco está comendo?
L No, he is not eating. He is painting.|Não, ele não está comendo. Ele está pintando.
L Are they in the tent?|Eles estão na barraca?
L Yes, and the farmer is sleeping!|Sim, e o fazendeiro está dormindo!
H 1,3,4,5,6
Q Are the sheep dancing?|As ovelhas estão dançando?|1|✅ Yes|❌ No|🤷 Maybe
Q Who is painting?|Quem está pintando?|5|🐖 The pig|🐑 Shaun|👨‍🌾 The farmer
Q Who is sleeping?|Quem está dormindo?|7|👨‍🌾 The farmer|🐕 Bitzer|🐑 The sheep
B dance|💃|dançar|in the field|The sheep dance in the field.|As ovelhas dançam no campo.
B sing|🎤|cantar|a song|Shaun sings a song.|O Shaun canta uma música.
B eat|🍎|comer|grass|The pig eats grass.|O porco come grama.
B paint|🎨|pintar|the tent|The pig paints the tent.|O porco pinta a barraca.
LAB da|Em dancing, a soa é; em tent, e soa é.|Tent e tint têm sons diferentes.
W dancing|DÉN-sin|dançando|a = é|dozing|DÔU-zin
W singing|SÍN-guin|cantando|ng soa nasal|sinking|SÍN-kin
W tent|TÉNT|barraca|e = é|tint|TÍNT
G 0|are|is|am
G 1|singing|sing|sings
G 2|Is|Are|Do
G 3|painting|paint|paints
X 👀|Look!|Olhe!|Chama a atenção.|Look! They are dancing.|Olhe! Eles estão dançando.
X 🤫|Shh!|Psiu!|Pede silêncio.|Shh! The farmer is sleeping.|Psiu! O fazendeiro está dormindo.
X 🐑|Baa!|Bé!|Som da ovelha.|Baa! I am Shaun.|Bé! Eu sou o Shaun.
X 😱|Oh no!|Ai, não!|Mostra susto.|Oh no! The farmer is up.|Ai, não! O fazendeiro acordou.
"""))

N.append(parse("""
N 7080344
C Estragon,Vladimir | tommy,tom | O Estragon pergunta “What do you mean?” e o Vladimir explica que eles esperam o Godot.
F Waiting for Godot | 🎭 Peça de teatro | 1953 | uma peça de Samuel Beckett sobre dois homens, Vladimir e Estragon, que esperam em uma estrada, perto de uma árvore, por alguém chamado Godot. | pedir esclarecimento: What do you mean? | school | 🌳,🛤️,⏳
V 💬|mean|querer dizer|MÍIN
V 📋|example|exemplo|ig-ZÉM-pol
V 🗣️|explain|explicar|iks-PLÊIN
V 💡|idea|ideia|ai-DÍ-a
V ✨|clear|claro|KLÍR
V ❓|question|pergunta|KUÉS-tchân
L Let’s go, Vladimir.|Vamos embora, Vladimir.
L We cannot. We wait for Godot.|Não podemos. Nós esperamos o Godot.
L What do you mean?|O que você quer dizer?
L I mean we wait here.|Eu quero dizer que esperamos aqui.
L Give me an example.|Dê-me um exemplo.
L I have an idea. Wait by the tree.|Eu tenho uma ideia. Espere perto da árvore.
L Can you explain? I have a question.|Você pode explicar? Eu tenho uma pergunta.
L Is it clear now?|Está claro agora?
H 3,4,6,5,7
Q Who are they waiting for?|Quem eles esperam?|1|🧑 Godot|👩 A friend|🚌 A bus
Q Where do they wait?|Onde eles esperam?|5|🌳 By the tree|🏠 At home|🏪 In a shop
Q What does Estragon have?|O que o Estragon tem?|6|❓ A question|🌳 A tree|🚗 A car
B mean|💬|querer dizer|it|Vladimir means it.|O Vladimir quer dizer isso.
B explain|🗣️|explicar|the idea|Vladimir explains the idea.|O Vladimir explica a ideia.
B give|🎁|dar|an example|Estragon gives an example.|O Estragon dá um exemplo.
B understand|🧠|entender|the question|Estragon understands the question.|O Estragon entende a pergunta.
LAB me|Em mean, ea soa íi; em idea, i soa ái.|Mean e men têm sons diferentes.
W mean|MÍIN|querer dizer|ea = íi|men|MÉN
W idea|ai-DÍ-a|ideia|i = ái|ideal|ai-DÍIL
W clear|KLÍR|claro|ea = í|clean|KLÍIN
G 0|mean|means|meaning
G 1|Give|Gives|Giving
G 2|explain|explains|explained
G 4|Is|Are|Do
X 🚶|Let’s go.|Vamos embora.|Propõe ir embora.|Let’s go. It is late.|Vamos embora. Está tarde.
X 🤷|Never mind.|Deixa pra lá.|Deixa o assunto.|Never mind. Wait here.|Deixa pra lá. Espere aqui.
X 😮|Really?|Sério?|Mostra surpresa.|Really? We wait again?|Sério? Esperamos de novo?
X 👍|I see.|Entendi.|Mostra que entendeu.|I see. It is clear now.|Entendi. Agora está claro.
"""))

N.append(parse("""
N 7910044
C Fry,Leela | tommy,polly | O Fry começa um assunto, desiste com “never mind” e a Leela diz para esquecer.
F Futurama | 📺 Série animada | 1999 | um desenho animado de Matt Groening sobre Fry, um entregador de pizza que acorda no futuro, e os amigos Leela e Bender. | deixar um assunto pra lá | yard | 🚀,🤖,🍕
V 🧠|mind|mente|MÁIND
V 🙅|forget|esquecer|for-GUÉT
V ⏰|later|depois|LÊI-ter
V ⏭️|skip|pular|SKÍP
V 💬|topic|assunto|TÓ-pik
V 😂|joke|piada|DJÔUK
L Leela, never mind.|Leela, deixa pra lá.
L What is it, Fry?|O que foi, Fry?
L Forget it. It is not important.|Esqueça. Não é importante.
L Tell me later, then.|Então me conte depois.
L Skip that. Let’s change the topic.|Pule isso. Vamos mudar de assunto.
L Okay. What is the topic?|Certo. Qual é o assunto?
L Bender told a joke. Never mind!|O Bender contou uma piada. Deixa pra lá!
L Forget it. Bender always jokes.|Esqueça. O Bender sempre faz piada.
H 0,2,3,4,5
Q What does Fry say first?|O que o Fry diz primeiro?|0|🙅 Never mind|👋 Hello|🌙 Good night
Q What do they change?|O que eles mudam?|4|💬 The topic|🏠 The room|🚀 The ship
Q Who told a joke?|Quem contou uma piada?|6|🤖 Bender|👨 Fry|👩 Leela
B forget|🙅|esquecer|it|Fry forgets it.|O Fry esquece isso.
B skip|⏭️|pular|that|Leela skips that.|A Leela pula isso.
B change|🔄|mudar|the topic|They change the topic.|Eles mudam de assunto.
B remember|🧠|lembrar de|the joke|Bender remembers the joke.|O Bender lembra da piada.
LAB mi|Em mind, i soa ái; em later, a soa êi.|Mind e mend têm sons diferentes.
W mind|MÁIND|mente|i = ái|mend|MÉND
W later|LÊI-ter|depois|a = êi|letter|LÉ-ter
W topic|TÓ-pik|assunto|o = ó|tropic|TRÓ-pik
G 0|mind|mine|mild
G 1|Forget|Forgets|Forgot
G 2|later|late|latter
G 3|change|changes|changing
X 😌|No worries.|Sem problemas.|Responde com leveza.|No worries. It is okay.|Sem problemas. Tudo bem.
X 👍|Okay.|Certo.|Concorda.|Okay. Tell me later.|Certo. Conte-me depois.
X 😉|Sure.|Claro.|Concorda.|Sure. Let’s skip it.|Claro. Vamos pular.
X 🤷|Fine!|Tudo bem!|Cede.|Fine! Forget it.|Tudo bem! Esqueça.
"""))

N.append(parse("""
N 7910045
C Hannibal,Face | tom,tommy | O Hannibal apresenta o plano da missão e o Face responde “Sounds good”.
F The A-Team | 📺 Série | 1983 | uma série americana de ação sobre quatro ex-soldados, Hannibal, Face, B.A. e Murdock, que ajudam pessoas com planos ousados e uma van preta. | aceitar planos: Sounds good e Sounds like a plan | park | 🚐,📋,🤝
V 🗓️|plan|plano|PLÉN
V 💡|idea|ideia|ai-DÍ-a
V 🎯|mission|missão|MÍ-xân
V 🚐|van|van|VÉN
V 🤩|great|ótimo|GRÊIT
V 🌙|tonight|esta noite|tu-NÁIT
L Face, I have a plan.|Face, eu tenho um plano.
L Sounds like a plan!|Parece um bom plano!
L That is a good idea, right?|É uma boa ideia, certo?
L Yes. Tonight is the mission.|Sim. Esta noite é a missão.
L We take the van.|Nós pegamos a van.
L Sounds good. B.A. drives.|Parece bom. O B.A. dirige.
L Sounds great. We are a team.|Parece ótimo. Nós somos uma equipe.
L We love it when a plan works.|Nós adoramos quando um plano funciona.
H 0,2,3,4,6
Q What does Hannibal have?|O que o Hannibal tem?|0|🗓️ A plan|🚐 A van|🎯 A mission
Q When is the mission?|Quando é a missão?|3|🌙 Tonight|🌅 Tomorrow|☀️ Today
Q Who drives?|Quem dirige?|5|🧑 B.A.|😎 Face|🧓 Hannibal
B sound|👂|parecer|good|The plan sounds good.|O plano parece bom.
B plan|🗓️|planejar|a mission|Hannibal plans a mission.|O Hannibal planeja uma missão.
B take|🚐|pegar|the van|Face takes the van.|O Face pega a van.
B drive|🚗|dirigir|the van|B.A. drives the van.|O B.A. dirige a van.
LAB pl|Em plan, a soa é; em van, a soa é.|Plan e plane têm sons diferentes.
W plan|PLÉN|plano|a = é|plane|PLÊIN
W van|VÉN|van|a = é|ban|BÉN
W mission|MÍ-xân|missão|ss = x|mansion|MÉN-xân
G 0|have|has|having
G 1|good|well|goods
G 2|is|are|am
G 4|Sounds|Sound|Sounding
X 🚀|Let’s go!|Vamos lá!|Chama para a ação.|Let’s go! The van is ready.|Vamos lá! A van está pronta.
X 💡|Good idea.|Boa ideia.|Aprova uma sugestão.|Good idea. I like the plan.|Boa ideia. Eu gosto do plano.
X 🤩|Great!|Ótimo!|Comemora.|Great! We have a team.|Ótimo! Nós temos uma equipe.
X 👋|See you tonight.|Até esta noite.|Combina o encontro.|See you tonight, Face.|Até esta noite, Face.
"""))

N.append(parse("""
N 7910046
C Kelly,Zack | polly,tom | A Kelly e o Zack conversam de um jeito informal: kinda, sorta e gimme.
F Saved by the Bell | 📺 Série | 1989 | uma comédia americana sobre Zack Morris e os amigos Kelly, Screech, Slater e Jessie no colégio, com o diretor Mr. Belding. | entender formas faladas como kinda, sorta e gimme | park | 🏫,📞,🎒
V 🥶|kinda|meio (kind of)|KÁIN-da
V 🙂|sorta|meio (sort of)|SÓR-ta
V 🤲|gimme|me dá (give me)|GUÍ-mi
V 🤏|bit|um pouco|BÍT
V 💬|word|palavra|UÂRD
V 🧊|cold|frio|KÔULD
L It’s kinda cold today, Zack.|Está meio frio hoje, Zack.
L It’s sorta fun.|É meio divertido.
L Gimme the ball, please.|Me dá a bola, por favor.
L I’m a bit tired.|Estou um pouco cansado.
L That is a funny word, Zack.|Essa é uma palavra engraçada, Zack.
L Kinda? Sorta? It is how we talk.|Meio? Meio que? É como a gente fala.
L Gimme a break!|Me dá um tempo!
L OK, OK. I’m kinda sorry.|Tá bom, tá bom. Eu estou meio arrependido.
H 0,1,2,3,4
Q How is the day?|Como está o dia?|0|🧊 Kinda cold|🔥 Very hot|🌧️ Rainy
Q What does Kelly want?|O que a Kelly quer?|2|⚽ The ball|📚 A book|🍕 Pizza
Q Who is a bit tired?|Quem está um pouco cansado?|3|👦 Zack|👧 Kelly|🤓 Screech
B talk|🗣️|falar|with funny words|Zack talks with funny words.|O Zack fala com palavras engraçadas.
B sound|👂|soar|fun|It sounds fun.|Soa divertido.
B feel|😴|sentir-se|tired|Zack feels tired.|O Zack se sente cansado.
B say|💬|dizer|a word|Kelly says a word.|A Kelly diz uma palavra.
LAB ki|Em kinda, i soa ái; em gimme, gi soa gui.|Kinda e kinder têm sons diferentes.
W kinda|KÁIN-da|meio|i = ái|kinder|KÁIN-der
W sorta|SÓR-ta|meio que|or = ór|sore|SÓR
W gimme|GUÍ-mi|me dá|gi = gui|gym|DJÍM
G 0|kinda|kind|kindly
G 1|sorta|sort|sorts
G 2|Gimme|Give|Gives
G 3|bit|bite|beat
X 😮|No way!|Nem pensar!|Mostra surpresa.|No way! It is kinda cold.|Nem pensar! Está meio frio.
X 😎|Cool!|Legal!|Reage com gosto.|Cool! That is a fun word.|Legal! Essa é uma palavra divertida.
X 🙄|Whatever.|Tanto faz.|Mostra indiferença.|Whatever. I am sorta busy.|Tanto faz. Eu estou meio ocupado.
X 🛑|Gimme a break!|Me dá um tempo!|Pede paz.|Gimme a break! I am tired.|Me dá um tempo! Estou cansado.
"""))

N.append(parse("""
N 7910047
C Annie,Abed | polly,tommy | A Annie estuda de última hora para a prova e o Abed espera tirar nota máxima.
F Community | 📺 Série | 2009 | uma comédia americana sobre um grupo de estudantes de uma faculdade comunitária, como Annie e Abed, que estudam juntos. | estudar de última hora e tirar nota máxima | school | 📚,🏫,✏️
V 📚|cram|estudar às pressas|KRÉM
V 💯|ace|tirar nota máxima|ÊIS
V 🅰️|grade|nota|GRÊID
V 📝|quiz|prova rápida|KUÍZ
V 🧑‍🏫|tutor|professor particular|TIÚ-ter
V 🕒|clock|relógio|KLÓK
L Abed, I cram for the test.|Abed, eu estudo às pressas para a prova.
L I hope to ace it.|Eu espero tirar nota máxima.
L I get a good grade.|Eu tiro uma boa nota.
L We have a quiz today.|Nós temos uma prova rápida hoje.
L I have a tutor, Troy.|Eu tenho um professor particular, o Troy.
L The clock is fast. Cool.|O relógio está rápido. Legal.
L Cram, cram, cram! No sleep.|Estude, estude, estude! Sem dormir.
L Ace it, Annie.|Tire nota máxima, Annie.
H 0,1,2,3,4
Q What does Annie do for the test?|O que a Annie faz para a prova?|0|📚 Cram|😴 Sleep|🎮 Play
Q What do they have today?|O que eles têm hoje?|3|📝 A quiz|🎉 A party|🧳 A trip
Q What does Abed say at the end?|O que o Abed diz no fim?|7|💯 Ace it|😴 Sleep now|🏠 Go home
B cram|📚|estudar às pressas|for the test|Annie crams for the test.|A Annie estuda às pressas para a prova.
B ace|💯|tirar nota máxima em|the quiz|Abed aces the quiz.|O Abed tira nota máxima na prova.
B pass|✅|passar em|the test|Troy passes the test.|O Troy passa na prova.
B fail|❌|reprovar em|a quiz|He fails a quiz.|Ele reprova numa prova rápida.
LAB cr|Em cram, a soa é; em ace, a soa êi.|Cram e cream têm sons diferentes.
W cram|KRÉM|estudar às pressas|a = é|cream|KRÍIM
W ace|ÊIS|nota máxima|a = êi|ice|ÁIS
W quiz|KUÍZ|prova rápida|qu = ku|quit|KUÍT
G 0|cram|crams|crammed
G 1|ace|aces|aced
G 2|get|gets|getting
G 3|have|has|having
X 🍀|Good luck!|Boa sorte!|Deseja sorte.|Good luck on the quiz!|Boa sorte na prova rápida!
X 😎|Cool!|Legal!|Reage com gosto.|Cool! I ace it.|Legal! Eu tiro nota máxima.
X 💪|Come on!|Vamos lá!|Incentiva.|Come on! One more page.|Vamos lá! Mais uma página.
X 😴|No sleep.|Sem dormir.|Diz que não vai dormir.|No sleep tonight. I cram.|Sem dormir esta noite. Eu estudo.
"""))
