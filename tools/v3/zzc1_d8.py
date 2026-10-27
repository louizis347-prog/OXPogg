# Lote C do A1, dados 8 (n 7080322 … 7080330). Ver zzc1_lib.py para o formato.
from v3.zzc1_lib import parse

N = []
N.append(parse("""
N 7080322
C Mafalda,Felipe | polly,tommy | A Mafalda e o Felipe descrevem a cidade: o parque tranquilo, a rua movimentada e a feira lotada.
F Mafalda | 💬 Tirinha | 1964 | uma tirinha do argentino Quino sobre Mafalda, uma menina curiosa que se preocupa com o mundo, e os amigos, como Felipe e Manolito. | descrever lugares: quiet, busy e crowded | street | 🌍,🏙️,🌳
V 🤫|quiet|tranquilo|KUÁI-et
V 🚗|busy|movimentado|BÍ-zi
V 👥|crowded|lotado|KRÁU-did
V 💧|clean|limpo|KLÍIN
V 🗑️|dirty|sujo|DÂR-ti
V 🏙️|city|cidade|SÍ-ti
L Felipe, the park is quiet.|Felipe, o parque é tranquilo.
L The street is busy.|A rua é movimentada.
L The market is crowded.|A feira está lotada.
L The lake is clean.|O lago é limpo.
L The corner is dirty.|A esquina é suja.
L I love this city.|Eu amo esta cidade.
L Me too, but I like the quiet park.|Eu também, mas gosto do parque tranquilo.
L Let’s go to the park!|Vamos ao parque!
H 0,1,2,3,4
Q Which place is quiet?|Que lugar é tranquilo?|0|🌳 The park|🚗 The street|🛒 The market
Q Which place is crowded?|Que lugar está lotado?|2|🛒 The market|🌳 The park|🏞️ The lake
Q Where do they go?|Aonde eles vão?|7|🌳 To the park|🛒 To the market|🏠 Home
B visit|🚶|visitar|the park|Mafalda visits the park.|A Mafalda visita o parque.
B prefer|💚|preferir|quiet places|Felipe prefers quiet places.|O Felipe prefere lugares tranquilos.
B go|🚌|ir|to the market|They go to the market.|Eles vão à feira.
B breathe|🌬️|respirar|fresh air|Mafalda breathes fresh air.|A Mafalda respira ar fresco.
LAB qu|Em quiet, ie soa ái-et; em busy, u soa i.|Quiet e quite têm sons diferentes.
W quiet|KUÁI-et|tranquilo|ie = ái-et|quite|KUÁIT
W busy|BÍ-zi|movimentado|u = i|bus|BÂS
W dirty|DÂR-ti|sujo|ir = âr|dart|DÁRT
G 0|quiet|quite|quit
G 1|busy|bus|busily
G 2|crowded|crowd|crowds
G 4|dirty|dirt|dirtily
X 🙌|Me too.|Eu também.|Concorda.|Me too. I like the park.|Eu também. Eu gosto do parque.
X 🚀|Let’s go!|Vamos lá!|Chama para ir.|Let’s go! The park is near.|Vamos lá! O parque é perto.
X 🤩|What a city!|Que cidade!|Reage à cidade.|What a city! It is big.|Que cidade! Ela é grande.
X 🤫|Shh!|Silêncio!|Pede silêncio.|Shh! It is a quiet place.|Silêncio! É um lugar tranquilo.
"""))

N.append(parse("""
N 7080323
C Yogi,Boo-Boo | tom,tommy | O urso Yogi manda o Boo-Boo trazer e levar a cesta de piquenique.
F Yogi Bear | 📺 Série animada | 1958 | um desenho animado da Hanna-Barbera sobre o urso Yogi e o amiguinho Boo-Boo, que roubam cestas de piquenique no Parque Jellystone, para raiva do guarda Smith. | distinguir bring (trazer) e take (levar) | living | 🧺,🐻,🌲
V 🧺|basket|cesta|BÉS-ket
V 🪑|table|mesa|TÊI-bol
V 🍯|honey|mel|HÂ-ni
V 🥪|sandwich|sanduíche|SÉN-uitch
V 🍎|apple|maçã|Á-pol
V 👮|ranger|guarda|RÊIN-djer
L Boo-Boo, bring me the picnic basket.|Boo-Boo, traga-me a cesta de piquenique.
L Take it to the table, Yogi.|Leve para a mesa, Yogi.
L Bring some honey too.|Traga um pouco de mel também.
L I bring a sandwich from the camp.|Eu trago um sanduíche do acampamento.
L Take this apple to Ranger Smith.|Leve esta maçã para o guarda Smith.
L No! Ranger Smith is angry.|Não! O guarda Smith está zangado.
L Then bring the basket back.|Então traga a cesta de volta.
L I take the basket home. Bye!|Eu levo a cesta para casa. Tchau!
H 0,1,2,3,4
Q What does Yogi want?|O que o Yogi quer?|0|🧺 The picnic basket|🍯 Honey|🍎 An apple
Q Where does Boo-Boo take it?|Para onde o Boo-Boo leva?|1|🪑 To the table|🏠 Home|🌲 To the forest
Q Who is angry?|Quem está zangado?|5|👮 Ranger Smith|🐻 Yogi|🐻 Boo-Boo
B carry|🧺|carregar|a basket|Boo-Boo carries a basket.|O Boo-Boo carrega uma cesta.
B take|🚶|levar|the apple|Yogi takes the apple.|O Yogi leva a maçã.
B pick up|🍯|pegar|the honey|Yogi picks up the honey.|O Yogi pega o mel.
B open|📦|abrir|the basket|Boo-Boo opens the basket.|O Boo-Boo abre a cesta.
LAB ba|Em basket, a soa é; em honey, o soa â.|Basket e biscuit têm sons diferentes.
W basket|BÉS-ket|cesta|a = é|biscuit|BÍS-kit
W honey|HÂ-ni|mel|o = â|funny|FÂ-ni
W sandwich|SÉN-uitch|sanduíche|a = é|sandal|SÉN-dal
G 0|bring|brings|bringing
G 1|Take|Takes|Taking
G 2|Bring|Brings|Brought
G 3|bring|brings|bringing
X 🐻|Hey, Boo-Boo!|Ei, Boo-Boo!|Chama o amigo.|Hey, Boo-Boo! Look at that basket.|Ei, Boo-Boo! Olhe aquela cesta.
X ⚠️|Be careful.|Tenha cuidado.|Alerta alguém.|Be careful. The ranger is near.|Tenha cuidado. O guarda está perto.
X 😋|Yum!|Hum, que bom!|Mostra que gostou.|Yum! The honey is sweet.|Hum, que bom! O mel é doce.
X 😱|Oh no!|Ai, não!|Mostra susto.|Oh no! Here comes the ranger.|Ai, não! Lá vem o guarda.
"""))

N.append(parse("""
N 7080324
C Nobita,Doraemon | tommy,tom | O Nobita conta seus planos para amanhã e para a semana que vem com a ajuda do Doraemon.
F Doraemon | 💬 Mangá | 1969 | um mangá de Fujiko F. Fujio sobre Nobita, um menino sonhador, e Doraemon, um gato-robô do futuro que tira gadgets mágicos do bolso. | falar de planos com be going to | street | 🤖,⏳,🏛️
V 🗓️|plan|plano|PLÉN
V 📅|tomorrow|amanhã|tu-MÓ-rou
V 🏛️|museum|museu|miu-ZÍ-um
V 🚆|train|trem|TRÊIN
V ⏳|time machine|máquina do tempo|TÁIM ma-XÍIN
V 🗓️|next week|semana que vem|NÉKST UÍIK
L Doraemon, I have a plan.|Doraemon, eu tenho um plano.
L What are you going to do?|O que você vai fazer?
L Tomorrow I am going to visit the museum.|Amanhã eu vou visitar o museu.
L Are you going to take a train?|Você vai pegar um trem?
L No. I am going to use the time machine.|Não. Eu vou usar a máquina do tempo.
L Next week we are going to travel to Paris.|Semana que vem nós vamos viajar para Paris.
L The museum is big. It is going to be fun.|O museu é grande. Vai ser divertido.
L What are you going to eat? Dorayaki!|O que você vai comer? Dorayaki!
H 0,2,6,3,4
Q What is Nobita going to visit?|O que o Nobita vai visitar?|2|🏛️ The museum|🏰 A castle|🏫 School
Q What is he going to use?|O que ele vai usar?|4|⏳ The time machine|🚆 A train|🚲 A bike
Q Where are they going next week?|Aonde eles vão na semana que vem?|5|🗼 To Paris|🗽 To New York|🏯 To Tokyo
B visit|🏛️|visitar|the museum|Nobita visits the museum.|O Nobita visita o museu.
B take|🚆|pegar|a train|Doraemon takes a train.|O Doraemon pega um trem.
B travel|✈️|viajar|to Paris|They travel to Paris.|Eles viajam para Paris.
B pack|🎒|arrumar|a bag|Nobita packs a bag.|O Nobita arruma uma mala.
LAB mu|Em museum, u soa iú; em train, ai soa êi.|Museum e music começam parecido, mas terminam diferente.
W museum|miu-ZÍ-um|museu|u = iú|music|MIÚ-zik
W train|TRÊIN|trem|ai = êi|tin|TÍN
W tomorrow|tu-MÓ-rou|amanhã|o = ó|tomato|to-MÊI-tou
G 1|going|go|goes
G 3|Are|Is|Do
G 2|is|are|am
G 4|am|is|are
X 🚀|Let’s go!|Vamos lá!|Chama para ir.|Let’s go! The time machine is ready.|Vamos lá! A máquina do tempo está pronta.
X 🎉|Great!|Ótimo!|Comemora um plano.|Great! A trip to Paris!|Ótimo! Uma viagem a Paris!
X 😱|Oh no!|Ai, não!|Mostra susto.|Oh no! I forgot my bag.|Ai, não! Eu esqueci a mala.
X 🥞|Dorayaki!|Dorayaki!|Diz o doce favorito do Doraemon.|Dorayaki! I love it.|Dorayaki! Eu amo.
"""))

N.append(parse("""
N 7910040
C Eliza,Higgins | polly,tom | A Eliza pede ao professor Higgins que fale devagar e mais alto.
F Pygmalion | 🎭 Peça de teatro | 1913 | uma peça de George Bernard Shaw sobre o professor Higgins, que ensina a florista Eliza a falar com clareza e sem sotaque forte. | pedir que falem devagar e mais alto | shop | 🗣️,🌹,🎩
V 🐢|slowly|devagar|SLÔU-li
V ⚡|fast|rápido|FÉST
V 📣|louder|mais alto|LÁU-der
V 🔊|clearly|com clareza|KLÍR-li
V 🌍|accent|sotaque|ÉK-sent
V 🔤|word|palavra|UÂRD
L Professor, please speak slowly.|Professor, por favor fale devagar.
L You speak fast, Eliza.|Você fala rápido, Eliza.
L Can you speak louder?|Você pode falar mais alto?
L Speak clearly. Say each word.|Fale com clareza. Diga cada palavra.
L I have an accent.|Eu tenho sotaque.
L Your accent is nice. Speak up!|O seu sotaque é bonito. Fale mais alto!
L I speak slowly now.|Agora eu falo devagar.
L Good! You speak clearly.|Bom! Você fala com clareza.
H 0,1,2,3,4
Q What does Eliza ask?|O que a Eliza pede?|0|🐢 Speak slowly|📣 Speak louder|🤐 Be quiet
Q Who has an accent?|Quem tem sotaque?|4|👩 Eliza|👨 Higgins|🧑 Pickering
Q What does Higgins say at the end?|O que o Higgins diz no fim?|7|👏 You speak clearly|🙅 You speak badly|🤷 I do not know
B speak|🗣️|falar|slowly|Eliza speaks slowly.|A Eliza fala devagar.
B spell|🔤|soletrar|a word|Higgins spells a word.|O Higgins soletra uma palavra.
B repeat|🔁|repetir|the word|Eliza repeats the word.|A Eliza repete a palavra.
B understand|🧠|entender|the accent|Higgins understands the accent.|O Higgins entende o sotaque.
LAB lo|Em louder, ou soa áu; em accent, a soa é.|Accent e accept têm sons diferentes.
W louder|LÁU-der|mais alto|ou = áu|loader|LÔU-der
W accent|ÉK-sent|sotaque|a = é|accept|ak-SÉPT
W word|UÂRD|palavra|or = âr|ward|UÓRD
G 0|slowly|slow|slows
G 1|fast|fastly|fasting
G 2|louder|loudest|loudy
G 4|an|a|the
X 🙋|Pardon?|Como?|Pede para repetir.|Pardon? Say it again.|Como? Diga de novo.
X 🔁|Say it again.|Diga de novo.|Pede repetição.|Say it again, please. Slowly.|Diga de novo, por favor. Devagar.
X 👏|Well done!|Muito bem!|Elogia.|Well done, Eliza!|Muito bem, Eliza!
X 🐢|Slow down.|Mais devagar.|Pede calma ao falar.|Slow down. I cannot follow.|Mais devagar. Eu não consigo acompanhar.
"""))

N.append(parse("""
N 7080326
C Ariadne,Theseus | polly,tom | A Ariadne guia o Teseu pelo labirinto com um fio e pede: siga-me e fiquem juntos.
F Theseus and the Minotaur | 🏛️ Mito grego | Grécia antiga | um mito grego em que o herói Teseu entra num labirinto, ajudado por Ariadne, que lhe dá um fio para achar o caminho de volta. | guiar um grupo: follow me e stay together | park2 | 🧵,🏛️,🐂
V ➡️|follow|seguir|FÓ-lou
V 🛤️|path|caminho|PÉTH
V 🤝|together|juntos|tu-GUÉ-dher
V 🧵|thread|fio|THRÉD
V 🔥|torch|tocha|TÓRTCH
V 🌀|maze|labirinto|MÊIZ
L Follow me, Theseus.|Siga-me, Teseu.
L Where is the path?|Onde fica o caminho?
L Look at the thread. Take the path.|Olhe o fio. Pegue o caminho.
L Stay together with me.|Fique junto comigo.
L I hold the thread. It is the way out.|Eu seguro o fio. É a saída.
L I have a torch. The maze is dark.|Eu tenho uma tocha. O labirinto é escuro.
L Follow the thread. Stay together!|Siga o fio. Fiquem juntos!
L We are out! Thank you, Ariadne.|Estamos fora! Obrigado, Ariadne.
H 0,2,3,4,5
Q What does Ariadne say first?|O que a Ariadne diz primeiro?|0|➡️ Follow me|⏳ Wait here|🏃 Run
Q What does Ariadne hold?|O que a Ariadne segura?|4|🧵 The thread|🔦 A torch|🗝️ A key
Q What does Theseus have?|O que o Teseu tem?|5|🔥 A torch|🗺️ A map|⛵ A boat
B follow|➡️|seguir|the thread|Theseus follows the thread.|O Teseu segue o fio.
B stay|🤝|ficar|together|They stay together.|Eles ficam juntos.
B lead|🧭|guiar|the way|Ariadne leads the way.|A Ariadne guia o caminho.
B hold|🧵|segurar|the thread|Ariadne holds the thread.|A Ariadne segura o fio.
LAB th|Em thread e path, th é a língua entre os dentes (thread tem th + r).|Path e pass têm sons diferentes.
W thread|THRÉD|fio|th + r|bread|BRÉD
W path|PÉTH|caminho|th = língua entre os dentes|pass|PÉS
W maze|MÊIZ|labirinto|a = êi|mess|MÉS
G 0|Follow|Follows|Following
G 1|Take|Takes|Taking
G 2|with|to|at
G 4|have|has|having
X ➡️|This way!|Por aqui!|Mostra o caminho.|This way! The thread is here.|Por aqui! O fio está aqui.
X ⚠️|Be careful.|Tenha cuidado.|Alerta alguém.|Be careful. The maze is dark.|Tenha cuidado. O labirinto é escuro.
X 🏃|Hurry!|Depressa!|Apressa alguém.|Hurry! Stay together.|Depressa! Fiquem juntos.
X 🎉|We did it!|Nós conseguimos!|Comemora.|We did it! We are out.|Nós conseguimos! Estamos fora.
"""))

N.append(parse("""
N 7080328
C Cheer,Tenderheart | misshoney,tommy | A Cheer Bear e o Tenderheart descrevem o que é peludo, fofinho e fofo no Reino do Cuidado.
F Care Bears | 🧸 Desenho e brinquedos | 1981 | uma turma de ursinhos coloridos, como Cheer Bear e Tenderheart Bear, que moram em nuvens e ajudam as pessoas a cuidar dos sentimentos. | descrever bichinhos: furry, fluffy e cute | living | 🧸,☁️,🌈
V 🐻|furry|peludo|FÂ-ri
V ☁️|fluffy|fofinho|FLÂ-fi
V 😍|cute|fofo|KIÚT
V 🧶|soft|macio|SÓFT
V 🐱|tiny|minúsculo|TÁI-ni
V 🐾|paw|patinha|PÓ
L Tenderheart, the bear is furry.|Tenderheart, o urso é peludo.
L The cloud is fluffy.|A nuvem é fofinha.
L What a cute cub!|Que filhote fofo!
L Its fur is soft.|O pelo dele é macio.
L The kitten is tiny.|O gatinho é minúsculo.
L Look at its paw.|Olhe a patinha dele.
L I love soft and fluffy things.|Eu amo coisas macias e fofinhas.
L Care Bears are cute!|Os Ursinhos Carinhosos são fofos!
H 0,1,2,3,4
Q What is furry?|O que é peludo?|0|🐻 The bear|☁️ The cloud|🐱 The kitten
Q What is fluffy?|O que é fofinho?|1|☁️ The cloud|🐻 The bear|🐾 The paw
Q What is tiny?|O que é minúsculo?|4|🐱 The kitten|🐻 The bear|☁️ The cloud
B look|👀|olhar|at the kitten|Cheer looks at the kitten.|A Cheer olha o gatinho.
B adore|😍|adorar|soft things|Tenderheart adores soft things.|O Tenderheart adora coisas macias.
B hug|🤗|abraçar|the bear|Cheer hugs the bear.|A Cheer abraça o urso.
B sleep|😴|dormir|on a cloud|Tenderheart sleeps on a cloud.|O Tenderheart dorme numa nuvem.
LAB fu|Em furry e fluffy, u soa â; em cute, u soa iú.|Furry e ferry têm sons diferentes.
W furry|FÂ-ri|peludo|u = â|ferry|FÉ-ri
W soft|SÓFT|macio|o = ó|sift|SÍFT
W cute|KIÚT|fofo|u = iú|cut|KÂT
G 0|furry|fury|funny
G 1|fluffy|fluff|fluffily
G 2|cute|cut|cure
G 3|soft|sofa|sort
X 🥰|Aww!|Ai, que fofo!|Reage a algo fofo.|Aww! A tiny kitten!|Ai, que fofo! Um gatinho minúsculo!
X 😍|So cute!|Tão fofo!|Elogia.|So cute! I love it.|Tão fofo! Eu amo.
X 🤗|Big hug!|Abraço grande!|Convida para abraçar.|Big hug! We are friends.|Abraço grande! Nós somos amigos.
X 🌈|Care a lot!|Cuide muito!|Incentiva o cuidado.|Care a lot, my friend.|Cuide muito, meu amigo.
"""))

N.append(parse("""
N 7080330
C Bia,Curupira | polly,tom | A Bia se perde na floresta e o Curupira, de pés virados para trás, a ajuda a achar o caminho.
F Curupira | 🏛️ Lenda brasileira | Folclore | uma lenda do folclore brasileiro sobre o Curupira, protetor da floresta, que tem os pés virados para trás e confunde quem se perde na mata. | falar de se perder e achar o caminho | park | 🌲,🦶,🗺️
V 🌲|lost|perdido|LÓST
V 🗺️|map|mapa|MÉP
V 🧭|way|caminho|UÊI
V 🥾|trail|trilha|TRÊIL
V 🦶|feet|pés|FÍIT
V 🐦|bird|pássaro|BÂRD
L Curupira, I got lost in the forest.|Curupira, eu me perdi na floresta.
L Check the map, Bia.|Veja o mapa, Bia.
L The map is old. I cannot find the way.|O mapa é velho. Eu não consigo achar o caminho.
L Follow the trail. It is near.|Siga a trilha. Ela é perto.
L Your feet point back! You are tricky.|Os seus pés apontam para trás! Você é esperto.
L Ha ha! I protect every bird.|Ha ha! Eu protejo cada pássaro.
L Please help me find the way home.|Por favor, ajude-me a achar o caminho de casa.
L Follow me. Do not get lost again.|Siga-me. Não se perca de novo.
H 0,1,2,3,4
Q Where is Bia lost?|Onde a Bia está perdida?|0|🌲 In the forest|🏖️ At the beach|🏙️ In the city
Q Is the map new?|O mapa é novo?|2|❌ No, it is old|✅ Yes, it is new|🤷 Maybe
Q What is tricky about Curupira?|O que tem de esperto no Curupira?|4|🦶 His feet point back|👁️ He has one eye|🐍 He has a snake
B get lost|🌲|se perder|in the forest|Bia gets lost in the forest.|A Bia se perde na floresta.
B find|🧭|achar|the way|Bia finds the way.|A Bia acha o caminho.
B check|🗺️|conferir|the map|Bia checks the map.|A Bia confere o mapa.
B ask|🙋|pedir ajuda a|Curupira|Bia asks Curupira.|A Bia pede ajuda ao Curupira.
LAB lo|Em lost, o soa ó; em trail, ai soa êi.|Lost e last têm sons diferentes.
W lost|LÓST|perdido|o = ó|last|LÉST
W trail|TRÊIL|trilha|ai = êi|trial|TRÁI-al
W feet|FÍIT|pés|ee = íi|fit|FÍT
G 0|got|get|gets
G 1|Check|Checks|Checking
G 2|find|finds|found
G 3|Follow|Follows|Following
X 🆘|Help!|Socorro!|Pede ajuda.|Help! I am lost.|Socorro! Estou perdida.
X 😌|Don’t worry.|Não se preocupe.|Acalma alguém.|Don’t worry. I know the way.|Não se preocupe. Eu conheço o caminho.
X ➡️|Follow me.|Siga-me.|Chama para seguir.|Follow me. The trail is here.|Siga-me. A trilha é aqui.
X 😄|Ha ha!|Ha ha!|Ri.|Ha ha! You are funny.|Ha ha! Você é engraçada.
"""))
