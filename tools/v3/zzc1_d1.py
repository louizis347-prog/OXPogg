# Lote C do A1, dados 1 (n 80245 … 80254). Ver zzc1_lib.py para o formato.
from v3.zzc1_lib import parse

N = []
N.append(parse("""
N 80245
C Gadget,Penny | tom,polly | O Inspector Gadget e a sobrinha Penny acham a cozinha cheia de coisas que não funcionam.
F Inspector Gadget | 📺 Série animada | 1983 | um seriado animado sobre um detetive atrapalhado, cheio de aparelhos no corpo, e a sobrinha esperta, Penny, que resolve os casos por ele. | avisar o que não funciona e o que está quebrado | kitchen | 🔧,🐶,🕵️
V 🔥|oven|forno|Á-vên
V 💡|bulb|lâmpada|BÂLB
V 🚰|faucet|torneira|FÓ-set
V ⚡|fuse|fusível|FIÚZ
V 🛠️|repair|conserto|ri-PÉR
V 🤖|gadget|aparelho|GÉ-djet
L Penny, the oven is not working.|Penny, o forno não está funcionando.
L Oh no! The bulb is broken too, Uncle.|Ai, não! A lâmpada também está quebrada, tio.
L The faucet is not working. No water!|A torneira não está funcionando. Sem água!
L Look at the fuse. It is broken.|Olhe o fusível. Está quebrado.
L I need a repair. Where is my gadget?|Eu preciso de um conserto. Cadê o meu aparelho?
L Uncle, your gadget is not working!|Tio, o seu aparelho não está funcionando!
L Don’t worry. Brain can fix the oven.|Não se preocupe. O Brain pode consertar o forno.
L Great! The oven works now.|Ótimo! O forno funciona agora.
H 0,1,2,3,4
Q What is not working first?|O que não está funcionando primeiro?|0|🔥 The oven|💡 The bulb|🚰 The faucet
Q What is broken?|O que está quebrado?|3|⚡ The fuse|🛠️ The repair|🔥 The oven
Q Who can fix the oven?|Quem pode consertar o forno?|6|🐶 Brain|🕵️ Gadget|👧 Penny
B fix|🔧|consertar|the oven|Brain fixes the oven.|O Brain conserta o forno.
B break|💥|quebrar|a cup|The cup breaks.|O copo quebra.
B change|🔄|trocar|the bulb|Penny changes the bulb.|A Penny troca a lâmpada.
B press|🔘|apertar|the button|Gadget presses the button.|O Gadget aperta o botão.
LAB ov|Em oven, o soa como á; em bulb, u soa como â.|Oven e over têm sons diferentes.
W oven|Á-vên|forno|o = á|over|ÔU-ver
W bulb|BÂLB|lâmpada|u = â|bull|BÚL
W fuse|FIÚZ|fusível|u = iú|fuss|FÂS
G 0|working|work|works
G 1|broken|break|breaking
G 2|not|no|never
G 3|is|are|am
X 😱|Oh no!|Ai, não!|Mostra susto com um defeito.|Oh no! The radio is broken.|Ai, não! O rádio está quebrado.
X 😌|Don’t worry.|Não se preocupe.|Acalma alguém.|Don’t worry. It is easy to fix.|Não se preocupe. É fácil consertar.
X 🔎|Look at|Olhe para|Chama a atenção para algo.|Look at the lamp. It is not working.|Olhe a lâmpada. Ela não está funcionando.
X 🎉|Great!|Ótimo!|Comemora quando funciona.|Great! The lamp works now.|Ótimo! A lâmpada funciona agora.
"""))

N.append(parse("""
N 7080245
C Arnold,Gerald | tommy,tom | Arnold e Gerald conversam na escola sobre a matéria favorita de cada um.
F Hey Arnold! | 📺 Série animada | 1996 | um seriado animado criado por Craig Bartlett sobre Arnold, um menino de cabeça quadrada, e o melhor amigo Gerald, na escola e no bairro. | falar das matérias da escola e da favorita | school | 🏫,📚,🎨
V 🔢|math|matemática|MÉTH
V 🧪|science|ciência|SÁI-êns
V 📜|history|história|RÍS-tri
V 🎨|art|arte|ÁRT
V ⭐|favorite|favorito|FÊI-vo-rit
V 📝|project|trabalho|PRÓ-djékt
L What is your favorite subject, Gerald?|Qual é a sua matéria favorita, Gerald?
L I like math. Numbers are easy.|Eu gosto de matemática. Números são fáceis.
L Science is fun. We have a project.|Ciências é divertido. Temos um trabalho.
L History is my favorite.|História é a minha favorita.
L We have art on Friday with Mr. Simmons.|Temos arte na sexta com o Sr. Simmons.
L Do you like art, Arnold?|Você gosta de arte, Arnold?
L Yes! I like art and music.|Sim! Eu gosto de arte e de música.
L My project is about history.|O meu trabalho é sobre história.
H 1,2,3,4,0
Q What does Gerald like?|Do que o Gerald gosta?|1|🔢 Math|🧪 Science|🎨 Art
Q When do they have art?|Quando eles têm arte?|4|📅 On Friday|📅 On Monday|📅 On Sunday
Q What is the project about?|Sobre o que é o trabalho?|7|📜 History|🔢 Math|🎨 Art
B like|👍|gostar de|math|Gerald likes math.|O Gerald gosta de matemática.
B love|❤️|amar|art class|Arnold loves art class.|O Arnold ama a aula de arte.
B study|📖|estudar|history|They study history.|Eles estudam história.
B paint|🖌️|pintar|a picture|Helga paints a picture.|A Helga pinta um quadro.
LAB th|Em math, o th é a língua entre os dentes; em art, ar soa ár.|Math e mass têm sons diferentes.
W math|MÉTH|matemática|th = língua entre os dentes|mass|MÉS
W science|SÁI-êns|ciência|sci = sái|silence|SÁI-lens
W art|ÁRT|arte|ar = ár|arm|ÁRM
G 0|like|likes|liking
G 1|is|are|am
G 2|my|me|mine
G 4|your|you|yours
X 😮|Really?|Sério?|Mostra surpresa.|Really? I like art too.|Sério? Eu também gosto de arte.
X 🙌|Me too!|Eu também!|Concorda com o outro.|Me too! I love science.|Eu também! Eu amo ciências.
X 😎|Cool!|Legal!|Reage com gosto.|Cool! Your project is great.|Legal! O seu trabalho é ótimo.
X 🤔|Let’s see.|Vamos ver.|Pensa antes de responder.|Let’s see. I like history and math.|Vamos ver. Eu gosto de história e de matemática.
"""))

N.append(parse("""
N 7080246
C Cory,Topanga | tommy,polly | O Cory conta à Topanga o resultado da prova e os dois falam de passar e de reprovar.
F Boy Meets World | 📺 Série | 1993 | um seriado americano sobre Cory, um menino que cresce com a ajuda do professor Mr. Feeny, da amiga Topanga e da família. | falar de provas: passar e reprovar | home1 | 📝,🏫,⭐
V 📝|test|prova|TÉST
V 🅰️|grade|nota|GRÊID
V 📋|result|resultado|ri-ZÂLT
V 🗒️|notes|anotações|NÔUTS
V 🥰|proud|orgulhoso|PRÁUD
V 📚|study|estudar|STÂ-di
L Topanga, I pass the test!|Topanga, eu passei na prova!
L Wow! What is the grade?|Uau! Qual é a nota?
L I got a good grade. Look!|Eu tirei uma boa nota. Olhe!
L The result is here. Mr. Feeny is happy.|O resultado está aqui. O Sr. Feeny está feliz.
L I study my notes every night.|Eu estudo as minhas anotações toda noite.
L Good! If you do not study, you fail the test.|Bom! Se você não estuda, reprova na prova.
L I was nervous, but I pass!|Eu estava nervoso, mas passei!
L I am proud of you, Cory.|Eu tenho orgulho de você, Cory.
H 0,2,3,4,7
Q Does Cory pass the test?|O Cory passa na prova?|0|✅ Yes, he does|❌ No, he fails|🤷 We do not know
Q Who is happy with the result?|Quem está feliz com o resultado?|3|👨‍🏫 Mr. Feeny|👧 Topanga|👩 Mom
Q What does Cory study every night?|O que o Cory estuda toda noite?|4|🗒️ His notes|🍕 Pizza|🎸 A guitar
B study|📖|estudar|my notes|Cory studies every night.|O Cory estuda toda noite.
B pass|✅|passar|the test|Topanga passes the test.|A Topanga passa na prova.
B fail|❌|reprovar em|the test|He fails the test.|Ele reprova na prova.
B get|🎁|tirar|a good grade|Cory gets a good grade.|O Cory tira uma boa nota.
LAB pa|Em pass, a soa é; em grade, a soa êi.|Pass e pace têm sons diferentes.
W pass|PÉS|passar|a = é|pace|PÊIS
W test|TÉST|prova|e = é|taste|TÊIST
W proud|PRÁUD|orgulhoso|ou = áu|prod|PRÓD
G 0|pass|passed|passing
G 1|good|well|goodly
G 2|here|hear|there
G 4|of|for|at
X 🥳|Congratulations!|Parabéns!|Parabeniza quem passou.|Congratulations! You pass the test.|Parabéns! Você passou na prova.
X 😅|Phew!|Ufa!|Mostra alívio.|Phew! The test is over.|Ufa! A prova acabou.
X 💪|Keep it up!|Continue assim!|Incentiva a continuar.|Keep it up! Your grades are good.|Continue assim! As suas notas são boas.
X 😬|Good luck|Boa sorte|Deseja sorte antes da prova.|Good luck on the test!|Boa sorte na prova!
"""))

N.append(parse("""
N 7080250
C Leslie,Ron | polly,tom | Na Prefeitura, a Leslie escreve um e-mail e o Ron aprende a anexar e a responder.
F Parks and Recreation | 📺 Série | 2009 | um seriado de comédia sobre Leslie Knope, uma funcionária animada da prefeitura de uma cidade pequena, e os colegas, como o sério Ron Swanson. | usar e-mail: enviar, anexar e responder | office | 💻,📧,🌳
V 📧|email|e-mail|Í-mêil
V 📎|attachment|anexo|a-TÉTCH-ment
V 🏷️|subject|assunto|SÂB-djekt
V 📥|inbox|caixa de entrada|ÍN-box
V ↩️|reply|resposta|ri-PLÁI
V 💬|message|mensagem|MÉ-sidj
L Ron, I send an email to the park team.|Ron, eu envio um e-mail para a equipe do parque.
L Open the attachment first, Leslie.|Abra primeiro o anexo, Leslie.
L Write a subject line. It is short.|Escreva uma linha de assunto. Ela é curta.
L Check your inbox. I have a message.|Veja a sua caixa de entrada. Eu tenho uma mensagem.
L Please reply to my email today.|Por favor, responda ao meu e-mail hoje.
L I attach the photo of the park.|Eu anexo a foto do parque.
L Good. Now click send.|Bom. Agora clique em enviar.
L Done! Ron, you can reply now.|Pronto! Ron, você pode responder agora.
H 0,1,2,3,4
Q Who sends an email?|Quem envia o e-mail?|0|👩 Leslie|👨 Ron|👮 Ben
Q What does Leslie attach?|O que a Leslie anexa?|5|📸 A photo of the park|🍔 A burger|📅 A calendar
Q What can Ron do at the end?|O que o Ron pode fazer no fim?|7|↩️ Reply|🚪 Leave|🍳 Cook
B send|📤|enviar|an email|Leslie sends an email.|A Leslie envia um e-mail.
B attach|📎|anexar|a photo|Leslie attaches a photo.|A Leslie anexa uma foto.
B reply|↩️|responder|to Leslie|Ron replies to Leslie.|O Ron responde à Leslie.
B write|✍️|escrever|a subject line|He writes a subject line.|Ele escreve uma linha de assunto.
LAB em|Em email, e soa í e ai soa êi; em reply, y final soa ái.|Reply e ripe têm sons diferentes.
W email|Í-mêil|e-mail|e = í|mail|MÊIL
W reply|ri-PLÁI|resposta|y = ái|ripe|RÁIP
W inbox|ÍN-box|caixa de entrada|in = ín|ink|ÍNK
G 0|send|sent|sending
G 1|attachment|attach|attached
G 4|reply|replay|repeat
G 3|inbox|input|outbox
X 😊|Thanks!|Obrigada!|Agradece uma ajuda.|Thanks! I can send it now.|Obrigada! Já posso enviar.
X 🤨|Not yet.|Ainda não.|Diz que algo não está pronto.|Not yet. I have no subject line.|Ainda não. Eu não tenho assunto.
X 👍|Sounds good.|Combinado.|Aceita um plano.|Sounds good. I reply today.|Combinado. Eu respondo hoje.
X 😮‍💨|Finally!|Finalmente!|Mostra alívio.|Finally! The email is gone.|Finalmente! O e-mail foi embora.
"""))

N.append(parse("""
N 7910031
C Richard,Dinesh | tom,tommy | Richard e Dinesh baixam arquivos e enviam fotos no computador da empresa.
F Silicon Valley | 📺 Série | 2014 | um seriado de comédia sobre jovens programadores que tentam criar uma empresa de tecnologia no Vale do Silício. | baixar e enviar arquivos | office | 💻,📁,📶
V 📄|file|arquivo|FÁIL
V 📁|folder|pasta|FÔUL-der
V 📸|photo|foto|FÔU-tou
V 📱|app|aplicativo|ÉP
V 📶|wifi|wi-fi|UÁI-fái
V 💾|storage|armazenamento|STÓ-ridj
L I download the file.|Eu baixo o arquivo.
L Save it in a folder.|Salve na pasta.
L I upload a photo of the team.|Eu envio uma foto da equipe.
L Download the app too.|Baixe também o aplicativo.
L The wifi is slow today.|O wi-fi está lento hoje.
L Is the storage full?|O armazenamento está cheio?
L Yes. I delete old files.|Sim. Eu apago arquivos antigos.
L Now upload the photo. Good.|Agora envie a foto. Bom.
H 0,1,2,3,4
Q What does Richard download?|O que o Richard baixa?|0|📄 A file|📸 A photo|📱 A song
Q What is slow today?|O que está lento hoje?|4|📶 The wifi|💻 The laptop|📱 The phone
Q What does Richard delete?|O que o Richard apaga?|6|🗑️ Old files|📸 New photos|📱 The app
B download|⬇️|baixar|a file|Richard downloads a file.|O Richard baixa um arquivo.
B upload|⬆️|enviar|a photo|Dinesh uploads a photo.|O Dinesh envia uma foto.
B save|💾|salvar|the file|They save the file.|Eles salvam o arquivo.
B share|🔗|compartilhar|the folder|Richard shares the folder.|O Richard compartilha a pasta.
LAB ph|Em photo, ph soa f; em file, i soa ái.|File e feel têm sons diferentes.
W file|FÁIL|arquivo|i = ái|feel|FÍIL
W photo|FÔU-tou|foto|ph = f|foot|FÚT
W app|ÉP|aplicativo|a = é|up|ÂP
G 0|download|downloads|downloading
G 2|upload|uploads|uploaded
G 3|app|up|apple
G 4|slow|slows|slowly
X ⏳|Hold on.|Espere um pouco.|Pede para esperar.|Hold on. The file is big.|Espere um pouco. O arquivo é grande.
X 🙂|Almost done.|Quase pronto.|Diz que falta pouco.|Almost done. I upload the photo.|Quase pronto. Eu envio a foto.
X 🔁|Try again.|Tente de novo.|Incentiva a tentar outra vez.|Try again. The wifi is better.|Tente de novo. O wi-fi está melhor.
X 👍|No problem.|Sem problema.|Responde a um agradecimento.|No problem. I share the folder.|Sem problema. Eu compartilho a pasta.
"""))

N.append(parse("""
N 80254
C Laura,Maggie | polly,tommy | A Maggie faz o check-in no balcão do aeroporto com a ajuda da Laura.
F Pan Am | 📺 Série | 2011 | um seriado americano sobre comissárias de bordo e pilotos de uma grande companhia aérea nos anos 1960. | fazer o check-in no aeroporto | lobby1 | ✈️,🧳,🎫
V ✅|check in|fazer check-in|TCHÉK-ín
V 🧳|suitcase|mala|SUT-kêis
V 🎫|boarding pass|cartão de embarque|BÓR-din PÉS
V 🪟|window seat|assento na janela|UÍN-dou SÍIT
V ✈️|flight|voo|FLÁIT
V 🛄|counter|balcão|KÁUN-ter
L Good morning! Go to the check-in counter.|Bom dia! Vá ao balcão de check-in.
L Hello! I want to check in, please.|Olá! Eu quero fazer o check-in, por favor.
L Put your suitcase here.|Ponha a sua mala aqui.
L Can I have a window seat?|Posso ficar com um assento na janela?
L Yes. Here is your boarding pass.|Sim. Aqui está o seu cartão de embarque.
L What is my seat number?|Qual é o número do meu assento?
L Row twelve, window. Your flight is at ten.|Fileira doze, janela. O seu voo é às dez.
L Thank you! See you in Paris.|Obrigada! Até logo em Paris.
H 1,2,4,3,6
Q What does Maggie want?|O que a Maggie quer?|3|🪟 A window seat|🚪 An aisle seat|🪑 A back seat
Q What does Laura give her?|O que a Laura dá a ela?|4|🎫 A boarding pass|🛂 A passport|🧳 A suitcase
Q When is the flight?|Quando é o voo?|6|🔟 At ten|9️⃣ At nine|1️⃣2️⃣ At twelve
B check in|✅|fazer check-in|at the counter|Maggie checks in at the counter.|A Maggie faz o check-in no balcão.
B board|🛫|embarcar|the plane|They board the plane.|Elas embarcam no avião.
B wait|⏳|esperar|at the gate|Laura waits at the gate.|A Laura espera no portão.
B carry|🧳|carregar|a suitcase|Maggie carries a suitcase.|A Maggie carrega uma mala.
LAB ou|Em counter, ou soa áu; em flight, igh soa ái.|Counter e country têm sons diferentes.
W counter|KÁUN-ter|balcão|ou = áu|country|KÂN-tri
W flight|FLÁIT|voo|igh = ái|fright|FRÁIT
W seat|SÍIT|assento|ea = íi|sit|SÍT
G 0|check in|check on|check out
G 1|Put|Puts|Putting
G 2|boarding|board|boarded
G 4|at|on|in
X 🛫|Have a nice flight!|Boa viagem!|Deseja uma boa viagem.|Have a nice flight! Say hello to Paris.|Boa viagem! Dê um oi a Paris.
X 🙏|Thank you so much!|Muito obrigada!|Agradece com vontade.|Thank you so much! You are kind.|Muito obrigada! Você é gentil.
X 🙋|Excuse me.|Com licença.|Chama a atenção com educação.|Excuse me. Where is gate five?|Com licença. Onde fica o portão cinco?
X 👌|No problem.|Sem problema.|Responde a um pedido.|No problem. Wait here, please.|Sem problema. Espere aqui, por favor.
"""))

N.append(parse("""
N 7080254
C Nigel,Eliza | tom,polly | O Nigel e a Eliza passam pelo controle de passaportes com a bagagem da família.
F The Wild Thornberrys | 📺 Série animada | 1998 | um seriado animado sobre uma família que viaja pelo mundo num trailer, filmando animais, e a filha Eliza, que fala com eles. | passar pelo controle de passaportes | hall | 🛂,🌍,🐒
V 🛂|passport|passaporte|PÉS-pórt
V 🧳|luggage|bagagem|LÂ-gidj
V 🛃|customs|alfândega|KÂS-tâmz
V 📑|visa|visto|VÍI-za
V 🖋️|stamp|carimbo|STÉMP
V 📋|declare|declarar|di-KLÉR
L Eliza, show your passport.|Eliza, mostre o seu passaporte.
L Here it is, Dad. Is this your luggage?|Aqui está, pai. Esta é a sua bagagem?
L Yes, it is. We go through customs now.|Sim, é. Agora passamos pela alfândega.
L Do you have a visa for this country?|Você tem visto para este país?
L Yes. The officer stamps it.|Sim. O oficial carimba.
L How much luggage do we have?|Quanta bagagem nós temos?
L Four bags. Darwin is in the small bag!|Quatro malas. O Darwin está na mala pequena!
L Shh, Dad! Do not declare Darwin!|Psiu, pai! Não declare o Darwin!
H 0,1,2,3,4
Q What does Nigel ask for?|O que o Nigel pede?|0|🛂 A passport|🎫 A ticket|🍎 An apple
Q How many bags do they have?|Quantas malas eles têm?|6|4️⃣ Four|2️⃣ Two|3️⃣ Three
Q Where is Darwin?|Onde está o Darwin?|6|🧳 In the small bag|🚗 In the car|🛂 At the desk
B show|🛂|mostrar|the passport|Eliza shows the passport.|A Eliza mostra o passaporte.
B declare|📋|declarar|a gift|Nigel declares a gift.|O Nigel declara um presente.
B stamp|🖋️|carimbar|the page|The officer stamps the page.|O oficial carimba a página.
B open|📂|abrir|the bag|Nigel opens the bag.|O Nigel abre a mala.
LAB gg|Em luggage, u soa â e gg soa g; age soa idj.|Luggage e language têm sons diferentes.
W passport|PÉS-pórt|passaporte|a = é|passage|PÉ-sidj
W luggage|LÂ-gidj|bagagem|u = â|language|LÉN-guidj
W customs|KÂS-tâmz|alfândega|u = â|costumes|KÓS-tiumz
G 0|passport|passage|passion
G 1|luggage|language|lunch
G 2|customs|custom|costume
G 3|have|has|having
X 🛬|Welcome to|Bem-vindo a|Dá boas-vindas ao país.|Welcome to our country!|Bem-vindo ao nosso país!
X 📭|Nothing to declare|Nada a declarar|Diz que não leva nada.|I have nothing to declare.|Não tenho nada a declarar.
X 👍|All set|Tudo certo|Diz que está liberado.|You are all set. Enjoy!|Está tudo certo. Aproveite!
X ➡️|This way|Por aqui|Mostra o caminho.|This way, please.|Por aqui, por favor.
"""))
