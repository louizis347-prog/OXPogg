# Lote B (cinema), dados 2: episódios A1 7030039 .. 7009814. Formato: ver zz_b_lib.py.
from v3.zz_b_lib import add

add('''
N: 7030039
C: Po,Mr. Ping | tommy,tom | Na cozinha do restaurante, Po e o pai pedem licença com May I…? e respondem Yes, you may.
S: pedir licença com May I…? e responder Yes, you may: May I add a carrot?
Y: Hoje você aprende a pedir licença com educação: May I help with the soup? Yes, you may. May I have some noodles?
F: Kung Fu Panda | 🎬 Animação | 2008 | uma animação dirigida por Mark Osborne e John Stevenson, sobre um panda atrapalhado que sonha em aprender kung fu e ajuda o pai a servir sopa de macarrão | pedir licença com educação | bakery | 🍜,🥢,🐼
V: 🥣|broth|caldo|BRÓF
V: 🍜|noodles|macarrão|NÚ-dolz
V: 🥢|chopsticks|hashis|TCHÓP-stiks
V: 🧅|onion|cebola|Â-nion
V: 🥕|carrot|cenoura|KÉ-rot
V: 🥄|ladle|concha|LÊI-dol
H: May I stir the broth?|Posso mexer o caldo?
H: May I have some noodles?|Posso pegar um pouco de macarrão?
H: Yes, you may use the chopsticks.|Sim, você pode usar os hashis.
H: May I add an onion?|Posso pôr uma cebola?
H: Yes, you may add a carrot.|Sim, você pode pôr uma cenoura.
L: Dad, may I help with the soup?|Pai, posso ajudar com a sopa?
L: Yes, you may. Add a carrot.|Sim, pode. Ponha uma cenoura.
L: May I add an onion too?|Posso pôr uma cebola também?
L: Yes, you may. Cut it first.|Sim, pode. Corte antes.
L: May I have some noodles?|Posso pegar um pouco de macarrão?
L: Yes, you may. Use the chopsticks.|Sim, pode. Use os hashis.
L: May I taste the broth?|Posso provar o caldo?
L: Yes, you may. Use the ladle.|Sim, pode. Use a concha.
Q: What does Po want to help with?|Com o que o Po quer ajudar?|0|🥣 The soup|🍜 The bowl|🥕 The garden
Q: What may Po add after the carrot?|O que o Po pode pôr depois?|2|🧅 An onion|🥄 A spoon|🍜 A noodle
Q: What may Po use for the noodles?|O que o Po pode usar no macarrão?|5|🥢 The chopsticks|🥄 The spoon|🔪 The knife
B: add|➕|pôr, juntar|I add a carrot.|He adds a carrot.|She added salt.|Ela pôs sal.
B: slurp|😋|sorver|I slurp the noodles.|He slurps the noodles.|They slurped the soup.|Eles sorveram a sopa.
B: pour|🫗|despejar|I pour the broth.|He pours the broth.|She poured some water.|Ela despejou água.
B: cook|🍲|cozinhar|I cook the noodles.|He cooks the noodles.|We cooked all day.|Nós cozinhamos o dia todo.
LAB: br|Laboratório de sons: broth, noodles e ladle|Broth termina com th suave, “BRÓF”. Noodles tem u longo, “NÚ-dolz”. Ladle soa “LÊI-dol”.|Em broth, o th final é soprado: BRÓF, com a língua entre os dentes.
W: broth|BRÓF|caldo|th soprado|brother|BRÂ-der
W: noodles|NÚ-dolz|macarrão|u longo|needles|NÍ-dolz
W: ladle|LÊI-dol|concha|a = êi|label|LÊI-bol
G: 0|May|Do|Am
G: 1|have|has|having
G: 2|may|are|do
G: 4|may|is|does
X: 🙏|Thank you|Obrigado|agradecer|Thank you, Dad.|Obrigado, pai.
X: 😋|Yummy|Que delícia|elogiar|Yummy, this soup is great.|Que delícia, esta sopa é ótima.
X: 🍜|Be careful|Tenha cuidado|avisar|Be careful, it is hot.|Tenha cuidado, está quente.
X: 😊|Of course|Claro|concordar|Of course, Po.|Claro, Po.

N: 7070078
C: Frank,Carl | tommy,tom | Numa loja, Frank e Carl falam de como pagar: pay by card, pay in cash.
S: formas de pagar: pay by card, pay in cash
Y: Hoje você aprende a falar de pagamento: pay by card (com cartão) e pay in cash (em dinheiro).
F: Catch Me If You Can | 🎬 Filme | 2002 | um filme dirigido por Steven Spielberg, sobre um jovem esperto e um agente que corre atrás dele | falar de como se paga | viaduct | 💳,💵,🧾
V: 💳|card|cartão|KÁRD
V: 💵|cash|dinheiro vivo|KÉSH
V: 🧾|receipt|recibo|ri-SÍT
V: 🪙|coin|moeda|KÓIN
V: 🧑‍💼|cashier|caixa|ka-SHÍR
V: 🛍️|bag|sacola|BÉG
H: I pay by card.|Eu pago com cartão.
H: I pay in cash.|Eu pago em dinheiro.
H: Can I have a receipt, please?|Posso receber o recibo, por favor?
H: I have some coins in my bag.|Eu tenho umas moedas na minha sacola.
H: Do you pay by card or in cash?|Você paga com cartão ou em dinheiro?
L: Hello. How do you pay, Frank?|Olá. Como você paga, Frank?
L: Do you pay by card or in cash?|Você paga com cartão ou em dinheiro?
L: I pay in cash. I have some coins.|Eu pago em dinheiro. Eu tenho umas moedas.
L: Good. The cashier takes cash.|Bom. O caixa aceita dinheiro.
L: Here you are. Can I have a receipt, please?|Aqui está. Posso receber o recibo, por favor?
L: Sure. Do you need a bag?|Claro. Você precisa de uma sacola?
L: Yes, please. I pay by card next time.|Sim, por favor. Eu pago com cartão da próxima vez.
L: See you then. Have a nice day!|Até lá. Tenha um bom dia!
Q: How does Frank pay?|Como o Frank paga?|2|💵 In cash|💳 By card|🪙 With a bag
Q: What does Frank ask for?|O que o Frank pede?|4|🧾 A receipt|🛍️ A card|🪙 A coin
Q: How does Frank pay next time?|Como o Frank paga da próxima vez?|6|💳 By card|💵 In cash|🪙 With coins
B: pay|💳|pagar|I pay in cash.|He pays in cash.|She paid by card.|Ela pagou com cartão.
B: hand|🤲|entregar|I hand over the card.|He hands over the card.|She handed me a bag.|Ela me entregou uma sacola.
B: count|🔢|contar|I count the coins.|He counts the coins.|They counted the cash.|Eles contaram o dinheiro.
B: sign|✍️|assinar|I sign the receipt.|He signs the receipt.|She signed her name.|Ela assinou o nome.
LAB: ca|Laboratório de sons: card, cash e receipt|Card tem o a aberto, “KÁRD”. Cash termina em sh, “KÉSH”. Em receipt, o p é mudo: “ri-SÍT”.|Em receipt, o p não se fala: ri-SÍT.
W: card|KÁRD|cartão|a aberto|cord|KÓRD
W: cash|KÉSH|dinheiro vivo|sh final|cat|KÉT
W: receipt|ri-SÍT|recibo|p mudo|recipe|RÉ-si-pi
G: 0|by|in|on
G: 1|in|by|on
G: 2|have|has|having
G: 4|or|and|but
X: 🙏|Here you are|Aqui está|entregar|Here you are, ten dollars.|Aqui está, dez dólares.
X: 😊|No problem|Sem problema|responder|No problem, take your time.|Sem problema, com calma.
X: 🤔|Let me see|Deixe-me ver|pensar|Let me see, I have cash.|Deixe-me ver, eu tenho dinheiro.
X: 👋|Have a nice day|Tenha um bom dia|despedir-se|Have a nice day, Carl.|Tenha um bom dia, Carl.

N: 7910019
C: Gru,Agnes | tom,polly | No quintal, Gru e Agnes descrevem coisas com very, really e a little.
S: intensidade com very, really e a little: The rocket is very big
Y: Hoje você aprende a reforçar ou suavizar: very e really aumentam, a little suaviza. The rocket is very big. The speaker is a little loud.
F: Despicable Me | 🎬 Animação | 2010 | uma animação dirigida por Pierre Coffin e Chris Renaud, sobre um vilão rabugento que adota três meninas | descrever o tamanho e a força das coisas | toyshop | 🚀,🦄,🍪
V: 🚀|rocket|foguete|RÓ-kit
V: 🦄|unicorn|unicórnio|IÚ-ni-kórn
V: 🍪|cookie|biscoito|KÚ-ki
V: 🔊|speaker|caixa de som|SPÍ-ker
V: 🎈|balloon|balão|ba-LÚN
V: 🥽|goggles|óculos de proteção|GÓ-golz
H: The rocket is very big.|O foguete é muito grande.
H: The unicorn is really soft.|O unicórnio é muito macio.
H: The cookie is a little sweet.|O biscoito é um pouco doce.
H: The speaker is a little loud.|A caixa de som é um pouco alta.
H: The balloon is really big.|O balão é bem grande.
L: Gru, your rocket is very big!|Gru, seu foguete é muito grande!
L: Yes, it is. It is really fast.|Sim, é. Ele é muito rápido.
L: My unicorn is really soft.|Meu unicórnio é muito macio.
L: It is. The speaker is a little loud.|É. A caixa de som é um pouco alta.
L: Turn it down. The balloon is really big.|Abaixe. O balão é bem grande.
L: Have a cookie, Gru.|Pegue um biscoito, Gru.
L: Thank you. It is a little sweet.|Obrigado. Ele é um pouco doce.
L: Put on your goggles. We fly now!|Ponha seus óculos. Nós voamos agora!
Q: How big is the rocket?|Quão grande é o foguete?|0|🚀 Very big|🚀 A little small|🚀 Not big
Q: How is the speaker?|Como é a caixa de som?|3|🔊 A little loud|🔊 Very quiet|🔊 Really soft
Q: How is the cookie?|Como é o biscoito?|6|🍪 A little sweet|🍪 Very salty|🍪 Really hot
B: fly|✈️|voar|I fly the rocket.|He flies the rocket.|They flew to the moon.|Eles voaram para a lua.
B: laugh|😂|rir|I laugh a lot.|She laughs a lot.|We laughed together.|Nós rimos juntos.
B: hug|🤗|abraçar|I hug my unicorn.|She hugs her unicorn.|He hugged Agnes.|Ele abraçou a Agnes.
B: jump|🦘|pular|I jump on the bed.|She jumps on the bed.|They jumped up and down.|Eles pularam para cima e para baixo.
LAB: ro|Laboratório de sons: rocket, unicorn e goggles|Rocket começa com r suave, “RÓ-kit”. Unicorn começa com iú, “IÚ-ni-kórn”. Goggles soa “GÓ-golz”.|Em unicorn, o u soa como iú: IÚ-ni-kórn.
W: rocket|RÓ-kit|foguete|força no começo|pocket|PÓ-kit
W: unicorn|IÚ-ni-kórn|unicórnio|u = iú|uniform|IÚ-ni-fórm
W: goggles|GÓ-golz|óculos|g duro|giggles|GUÍ-golz
G: 0|very|much|many
G: 1|really|real|rarely
G: 2|a little|a few|a lot
G: 3|a little|a few|a lot
X: 😲|Wow|Uau|se surpreender|Wow, the rocket is huge.|Uau, o foguete é enorme.
X: 😆|So funny|Tão engraçado|rir|So funny, Gru!|Tão engraçado, Gru!
X: 🙌|Hooray|Eba|comemorar|Hooray, we fly today.|Eba, nós voamos hoje.
X: 🤗|Come here|Venha cá|chamar|Come here, Agnes.|Venha cá, Agnes.

N: 7010180
C: Mirabel,Isabela | polly,misshoney | Na casa da família, Mirabel e Isabela comparam idades: older, younger, oldest, youngest.
S: idades relativas: older, younger, oldest, youngest
Y: Hoje você aprende a comparar idades: older (mais velha), younger (mais nova), oldest (a mais velha de todas), youngest (a mais nova de todas).
F: Encanto | 🎬 Animação | 2021 | uma animação da Disney, dirigida por Byron Howard e Jared Bush, sobre uma família colombiana numa casa mágica, em que cada pessoa tem um dom | comparar a idade das pessoas da família | castle | 🏡,👵,👧
V: 👧|sister|irmã|SÍS-ter
V: 👦|brother|irmão|BRÂ-der
V: 👵|grandmother|avó|GRÉN-má-der
V: 👶|baby|bebê|BÊI-bi
V: 🖼️|photo|foto|FÔU-tô
V: 🧑‍🤝‍🧑|friends|amigos|FRÉNDZ
H: I have an older sister.|Eu tenho uma irmã mais velha.
H: My brother is younger than me.|Meu irmão é mais novo que eu.
H: Grandma is the oldest.|A vovó é a mais velha.
H: The baby is the youngest.|O bebê é o mais novo.
H: Look at the photo of the family.|Olhe a foto da família.
L: Isabela, you are my older sister.|Isabela, você é minha irmã mais velha.
L: And you are the younger one, Mirabel.|E você é a mais nova, Mirabel.
L: My brother is younger than me.|Meu irmão é mais novo que eu.
L: Grandma is the oldest in the family.|A vovó é a mais velha da família.
L: Yes, she is. The baby is the youngest.|Sim, é. O bebê é o mais novo.
L: Look at the photo of the family.|Olhe a foto da família.
L: Everyone is in it. We look happy.|Todos estão nela. Nós parecemos felizes.
L: Let’s hang it on the wall.|Vamos pendurá-la na parede.
Q: Who is the older sister?|Quem é a irmã mais velha?|0|👧 Isabela|👶 The baby|👦 The brother
Q: Who is the oldest in the family?|Quem é a mais velha da família?|3|👵 Grandma|👶 The baby|👦 The brother
Q: Who is the youngest?|Quem é o mais novo?|4|👶 The baby|👵 Grandma|👧 Isabela
B: hug|🤗|abraçar|I hug my sister.|She hugs her sister.|He hugged the baby.|Ele abraçou o bebê.
B: smile|😊|sorrir|I smile in the photo.|She smiles in the photo.|They smiled together.|Eles sorriram juntos.
B: draw|✏️|desenhar|I draw my family.|She draws her family.|He drew a house.|Ele desenhou uma casa.
B: hang|🖼️|pendurar|I hang the photo.|She hangs the photo.|We hung it on the wall.|Nós a penduramos na parede.
LAB: gr|Laboratório de sons: grandmother, brother e baby|Grandmother tem th suave no meio, “GRÉN-má-der”. Brother soa “BRÂ-der”. Baby soa “BÊI-bi”.|Em brother, o o soa como â: BRÂ-der.
W: grandmother|GRÉN-má-der|avó|th suave|grandfather|GRÉN-fá-der
W: brother|BRÂ-der|irmão|o = â|bother|BÓ-der
W: baby|BÊI-bi|bebê|a = êi|bobby|BÓ-bi
G: 0|older|oldest|more old
G: 1|younger|youngest|more young
G: 2|oldest|older|most old
G: 3|youngest|younger|most young
X: 😍|How cute|Que fofo|elogiar|How cute, the baby!|Que fofo, o bebê!
X: 👨‍👩‍👧|All together|Todos juntos|reunir|All together for the photo.|Todos juntos para a foto.
X: 😊|Say cheese|Diga xis|fotografar|Say cheese, everyone!|Diga xis, pessoal!
X: 🥰|I love you|Eu amo você|carinho|I love you, Grandma.|Eu amo você, vovó.

N: 7070079
C: Lilo,Nani | polly,tommy | Na sala de casa, Lilo e Nani perguntam como estão as pessoas: How is…? How are…?
S: perguntar como alguém está: How is Grandma? How are the neighbors
Y: Hoje você aprende a perguntar como estão as pessoas: How is Grandma? (uma pessoa) e How are the neighbors? (várias pessoas).
F: Lilo and Stitch | 🎬 Animação | 2002 | uma animação da Disney, dirigida por Chris Sanders e Dean DeBlois, sobre uma menina havaiana e um alienígena que vira seu melhor amigo | perguntar como as pessoas estão | lighthouse | 🌺,🍍,🏝️
V: 👵|grandma|vovó|GRÉN-má
V: 🏘️|neighbors|vizinhos|NÊI-berz
V: 🤒|sick|doente|SÍK
V: 😊|fine|bem|FÁIN
V: 🌺|flowers|flores|FLÁU-erz
V: 🍍|pineapple|abacaxi|PÁI-nê-pol
H: How is Grandma today?|Como está a vovó hoje?
H: How are the neighbors?|Como estão os vizinhos?
H: My brother is sick.|Meu irmão está doente.
H: She is fine, thank you.|Ela está bem, obrigada.
H: How are the flowers?|Como estão as flores?
L: Nani, how is Grandma today?|Nani, como está a vovó hoje?
L: She is fine, thank you.|Ela está bem, obrigada.
L: And how are the neighbors?|E como estão os vizinhos?
L: They are fine. My brother is sick.|Eles estão bem. Meu irmão está doente.
L: Oh no! How is he now?|Ai, não! Como ele está agora?
L: He is better. How are the flowers?|Ele está melhor. Como estão as flores?
L: They are fine. Take a pineapple to Grandma.|Elas estão bem. Leve um abacaxi para a vovó.
L: Good idea. She loves pineapple.|Boa ideia. Ela ama abacaxi.
Q: How is Grandma?|Como está a vovó?|1|😊 She is fine|🤒 She is sick|😴 She is asleep
Q: Who is sick?|Quem está doente?|3|🤒 Lilo’s brother|👵 Grandma|🏘️ The neighbors
Q: What is for Grandma?|O que é para a vovó?|6|🍍 A pineapple|🌺 A flower|🏘️ A house
B: feel|😊|sentir-se|I feel fine.|She feels fine.|He felt sick.|Ele se sentiu doente.
B: bring|🎁|trazer|I bring a pineapple.|She brings a pineapple.|He brought flowers.|Ele trouxe flores.
B: ask|❓|perguntar|I ask about Grandma.|She asks about Grandma.|They asked how we are.|Eles perguntaram como estamos.
B: listen|👂|ouvir|I listen to Nani.|She listens to Nani.|We listened carefully.|Nós ouvimos com atenção.
LAB: ne|Laboratório de sons: neighbors, flowers e pineapple|Neighbors soa “NÊI-berz”, com êi. Flowers soa “FLÁU-erz”. Pineapple soa “PÁI-nê-pol”.|Em neighbors, o gh não se fala: NÊI-berz.
W: neighbors|NÊI-berz|vizinhos|gh mudo|labors|LÊI-berz
W: flowers|FLÁU-erz|flores|ow = áu|floors|FLÓRZ
W: pineapple|PÁI-nê-pol|abacaxi|ai = ái|pine|PÁIN
G: 0|is|are|am
G: 1|are|is|am
G: 3|is|are|am
G: 4|are|is|be
X: 😟|Oh dear|Ai, meu Deus|se preocupar|Oh dear, he is sick.|Ai, meu Deus, ele está doente.
X: 😌|That’s good|Que bom|ficar aliviado|That’s good, she is fine.|Que bom, ela está bem.
X: 🤗|Give her a hug|Dê um abraço nela|carinho|Give her a hug from me.|Dê um abraço nela por mim.
X: 🌺|Aloha|Aloha|cumprimentar|Aloha, Grandma!|Aloha, vovó!

N: 7009811
C: Cady,Gretchen | polly,misshoney | No corredor da escola, Cady e Gretchen escolhem o que usar e levar: wear, bring, stay.
S: escolher o que usar e levar conforme o tempo: Wear a jacket. Bring a cap
Y: Hoje você aprende a decidir o que vestir e levar: wear (usar), bring (levar), stay (ficar). Wear a jacket. Bring your backpack.
F: Mean Girls | 🎬 Filme | 2004 | uma comédia dirigida por Mark Waters, sobre uma jovem que chega a uma nova escola e aprende as regras dos grupos de amigas | escolher o que vestir e levar | rainycafe | 🧥,🎒,☔
V: 🧥|jacket|jaqueta|DJÉ-kit
V: 👢|boots|botas|BÚTS
V: 🧢|cap|boné|KÉP
V: 🎒|backpack|mochila|BÉK-pék
V: 🧤|gloves|luvas|GLÂVZ
V: 👖|jeans|calça jeans|DJÍNZ
H: Wear a jacket today.|Use uma jaqueta hoje.
H: Wear boots in the rain.|Use botas na chuva.
H: Bring a cap for the sun.|Leve um boné para o sol.
H: Bring your backpack.|Leve sua mochila.
H: Stay warm. Wear gloves.|Fique aquecida. Use luvas.
L: Gretchen, what do I wear today?|Gretchen, o que eu uso hoje?
L: Wear a jacket today, Cady.|Use uma jaqueta hoje, Cady.
L: Is it raining?|Está chovendo?
L: Yes. Wear boots in the rain.|Sim. Use botas na chuva.
L: Should I bring a cap?|Devo levar um boné?
L: Bring a cap for the sun later.|Leve um boné para o sol mais tarde.
L: And bring your backpack.|E leve sua mochila.
L: Stay warm. Wear gloves too.|Fique aquecida. Use luvas também.
Q: What does Cady wear today?|O que a Cady usa hoje?|1|🧥 A jacket|🧢 A cap|🧤 Gloves
Q: What do they wear in the rain?|O que elas usam na chuva?|3|👢 Boots|👖 Jeans|🧢 A cap
Q: What does Cady bring?|O que a Cady leva?|6|🎒 Her backpack|🧥 Her jacket|👢 Her boots
B: choose|👕|escolher|I choose a jacket.|She chooses a jacket.|He chose boots.|Ele escolheu botas.
B: carry|🎒|carregar|I carry my backpack.|She carries her backpack.|They carried umbrellas.|Eles carregaram guarda-chuvas.
B: zip|🤐|fechar o zíper|I zip my jacket.|She zips her jacket.|He zipped his bag.|Ele fechou o zíper da bolsa.
B: check|☑️|conferir|I check the weather.|She checks the weather.|We checked the sky.|Nós conferimos o céu.
LAB: ja|Laboratório de sons: jacket, boots e gloves|Jacket começa com dj, “DJÉ-kit”. Boots tem u longo, “BÚTS”. Gloves soa “GLÂVZ”.|Em gloves, o o soa como â: GLÂVZ.
W: jacket|DJÉ-kit|jaqueta|j = dj|packet|PÉ-kit
W: boots|BÚTS|botas|oo = ú|bits|BÍTS
W: gloves|GLÂVZ|luvas|o = â|loves|LÂVZ
G: 0|Wear|Wears|Wearing
G: 1|in|on|at
G: 2|Bring|Brings|Bringing
G: 4|Stay|Stays|Staying
X: 😮|Look out|Cuidado|avisar|Look out, it is raining.|Cuidado, está chovendo.
X: 😅|Good idea|Boa ideia|concordar|Good idea, take a cap.|Boa ideia, leve um boné.
X: 😊|Don’t forget|Não esqueça|lembrar|Don’t forget your gloves.|Não esqueça suas luvas.
X: 👍|See you later|Até mais tarde|despedir-se|See you later, Gretchen.|Até mais tarde, Gretchen.

N: 7910020
C: Hallie,Annie | polly,misshoney | Na sala do chalé, Hallie e Annie comparam o que têm igual e diferente: both, the same, different.
S: comparar duas pessoas com both, the same e different: We both have a big smile
Y: Hoje você aprende a comparar duas pessoas: both (as duas), the same (igual), different (diferente).
F: The Parent Trap | 🎬 Filme | 1998 | uma comédia dirigida por Nancy Meyers, sobre duas meninas gêmeas que se conhecem num acampamento e trocam de lugar | comparar o que é igual e o que é diferente | castle | 👭,💇,😀
V: 😀|smile|sorriso|SMÁIL
V: 💇|hair|cabelo|RÉR
V: 👀|eyes|olhos|ÁIZ
V: 👗|dresses|vestidos|DRÉ-siz
V: 🍕|pizza|pizza|PÍT-sa
V: 👭|twins|gêmeas|TUÍNZ
H: We both have a big smile.|Nós duas temos um sorriso grande.
H: Our hair is different.|Nosso cabelo é diferente.
H: We have the same eyes.|Nós temos os mesmos olhos.
H: Our dresses are the same.|Nossos vestidos são iguais.
H: We both like pizza.|Nós duas gostamos de pizza.
L: Look, Annie! We both have a big smile.|Olhe, Annie! Nós duas temos um sorriso grande.
L: And we have the same eyes.|E nós temos os mesmos olhos.
L: But our hair is different.|Mas nosso cabelo é diferente.
L: Yes. Mine is long, yours is short.|Sim. O meu é longo, o seu é curto.
L: Our dresses are the same!|Nossos vestidos são iguais!
L: We are twins. What else is the same?|Somos gêmeas. O que mais é igual?
L: We both like pizza.|Nós duas gostamos de pizza.
L: Then let’s eat some together.|Então vamos comer um pouco juntas.
Q: What do they both have?|O que as duas têm?|0|😀 A big smile|💇 Short hair|👗 A red dress
Q: What is different?|O que é diferente?|2|💇 Their hair|👀 Their eyes|😀 Their smile
Q: What do they both like?|Do que as duas gostam?|6|🍕 Pizza|👗 Dresses|💇 Hair
B: share|🤝|dividir|I share my pizza.|She shares her pizza.|They shared a room.|Elas dividiram um quarto.
B: swap|🔄|trocar|I swap dresses.|She swaps dresses.|We swapped places.|Nós trocamos de lugar.
B: compare|⚖️|comparar|I compare our eyes.|She compares our eyes.|They compared their hair.|Elas compararam o cabelo.
B: giggle|🤭|dar risadinhas|I giggle with Annie.|She giggles with Annie.|We giggled all night.|Nós demos risadinhas a noite toda.
LAB: tw|Laboratório de sons: twins, eyes e smile|Twins começa com tu, “TUÍNZ”. Eyes soa “ÁIZ”. Smile começa com sm, “SMÁIL”.|Em eyes, o e inicial é mudo: ÁIZ.
W: twins|TUÍNZ|gêmeas|tw = tu|tins|TÍNZ
W: eyes|ÁIZ|olhos|e mudo|ice|ÁIS
W: smile|SMÁIL|sorriso|sm junto|small|SMÓL
G: 0|both|all|each
G: 1|different|difference|differ
G: 2|same|alike|equal
G: 3|same|alike|equal
X: 😮|No way|Não pode ser|se surpreender|No way, we are the same!|Não pode ser, somos iguais!
X: 😆|Me too|Eu também|concordar|Me too, I love pizza.|Eu também, eu amo pizza.
X: 🤩|That’s cool|Que legal|elogiar|That’s cool, we are twins.|Que legal, somos gêmeas.
X: 👭|Best friends|Melhores amigas|carinho|Best friends forever.|Melhores amigas para sempre.

N: 7030042
C: Viktor,Amelia | tom,polly | No saguão do aeroporto, Viktor e Amelia dizem um e-mail em voz alta: at, dot, dash.
S: dizer um e-mail em voz alta: amelia at mail dot com
Y: Hoje você aprende a dizer um e-mail: at (arroba), dot (ponto) e dash (traço). My email is amelia at mail dot com.
F: The Terminal | 🎬 Filme | 2004 | um filme dirigido por Steven Spielberg, sobre um viajante que fica morando num aeroporto e faz amigos | soletrar nomes e e-mails | viaduct | ✈️,📧,🛄
V: 📍|address|endereço|a-DRÉS
V: ⌨️|keyboard|teclado|KÍ-bórd
V: 🪪|name|nome|NÊIM
V: ✈️|airport|aeroporto|ÉR-pórt
V: 📝|paper|papel|PÊI-per
V: 🛄|suitcase|mala|SÚT-keis
H: My email address is amelia at mail dot com.|Meu endereço de e-mail é amelia arroba mail ponto com.
H: Type mail dot com.|Digite mail ponto com.
H: My name has a dash.|Meu nome tem um traço.
H: I wait at the airport.|Eu espero no aeroporto.
H: Write it down on paper: viktor at mail dot com.|Escreva no papel: viktor arroba mail ponto com.
L: Amelia, what is your email?|Amelia, qual é o seu e-mail?
L: My email is amelia at mail dot com.|Meu e-mail é amelia arroba mail ponto com.
L: Is there a dash?|Tem um traço?
L: No dash. Type mail dot com.|Sem traço. Digite mail ponto com.
L: My name has a dash. Say each letter slowly.|Meu nome tem um traço. Diga cada letra devagar.
L: V, I, K, T, O, R.|V, I, K, T, O, R.
L: Write it down: viktor at mail dot com.|Escreva: viktor arroba mail ponto com.
L: Perfect. I send you the ticket now.|Perfeito. Eu envio a passagem agora.
Q: What is Amelia’s email?|Qual é o e-mail da Amelia?|1|📧 Amelia at mail dot com|📧 Viktor at mail dot com|📧 Amelia dash mail
Q: Is there a dash in the email?|Tem um traço no e-mail?|3|❌ No dash|✅ Yes, one dash|✅ Yes, two dashes
Q: What does Amelia send?|O que a Amelia envia?|7|🎫 The ticket|🛄 The suitcase|⌨️ The keyboard
B: type|⌨️|digitar|I type my email.|She types her email.|He typed the name.|Ele digitou o nome.
B: spell|🔤|soletrar|I spell my name.|She spells her name.|We spelled it twice.|Nós soletramos duas vezes.
B: repeat|🔁|repetir|I repeat the letters.|She repeats the letters.|He repeated his email.|Ele repetiu o e-mail dele.
B: show|👀|mostrar|I show my ticket.|She shows her ticket.|He showed his name.|Ele mostrou o nome dele.
LAB: em|Laboratório de sons: address, name e suitcase|Address tem a força no fim, “a-DRÉS”. Name soa “NÊIM”, com a = êi. Suitcase soa “SÚT-keis”.|Em address, a força cai na segunda sílaba: a-DRÉS.
W: address|a-DRÉS|endereço|força no fim|dress|DRÉS
W: name|NÊIM|nome|a = êi|nine|NÁIN
W: suitcase|SÚT-keis|mala|ui = ú|suit|SÚT
G: 0|at|dot|dash
G: 1|dot|at|dash
G: 2|dash|dot|at
G: 4|dot|at|dash
X: 🙏|Once more|Mais uma vez|pedir repetição|Once more, please.|Mais uma vez, por favor.
X: 😊|Got it|Entendi|confirmar|Got it, thank you.|Entendi, obrigado.
X: 🐢|Slowly, please|Devagar, por favor|pedir calma|Slowly, please, I write it down.|Devagar, por favor, eu escrevo.
X: 👍|Perfect|Perfeito|elogiar|Perfect, that is right.|Perfeito, está certo.

N: 7009813
C: Ren,Ariel | tom,polly | Na loja de sapatos, Ren e Ariel provam pares para dançar: fit, match, comfortable.
S: falar do caimento: Do the shoes fit? They match my jacket
Y: Hoje você aprende a falar de caimento: Do the shoes fit? (servir), They match my jacket (combinar), comfortable (confortável).
F: Footloose | 🎬 Filme | 1984 | um filme musical dirigido por Herbert Ross, sobre um jovem que chega a uma cidade onde dançar é proibido | falar de sapatos que servem e combinam | toyshop | 👟,💃,🎀
V: 👡|sandals|sandálias|SÉN-dolz
V: 👟|sneakers|tênis|SNÍ-kerz
V: 🧦|socks|meias|SÓKS
V: 👠|heels|saltos|RÍLZ
V: 📏|size|tamanho|SÁIZ
V: 🎀|laces|cadarços|LÊI-siz
H: Do the sandals fit?|As sandálias servem?
H: They match my jacket.|Eles combinam com a minha jaqueta.
H: These socks are comfortable.|Estas meias são confortáveis.
H: The heels are too tight.|Os saltos estão muito apertados.
H: They fit my size.|Eles servem no meu tamanho.
L: Ariel, do the sandals fit?|Ariel, as sandálias servem?
L: Yes. They fit my size.|Sim. Eles servem no meu tamanho.
L: And do the sneakers match your jacket?|E o tênis combina com a sua jaqueta?
L: Yes, they match my jacket.|Sim, combinam com a minha jaqueta.
L: Try the socks. They are comfortable.|Experimente as meias. Elas são confortáveis.
L: They are! But the heels are too tight.|São! Mas os saltos estão muito apertados.
L: Then tie the laces and dance.|Então amarre os cadarços e dance.
L: Great. These shoes are for dancing!|Ótimo. Estes sapatos são para dançar!
Q: Do the sandals fit Ariel?|As sandálias servem na Ariel?|1|👡 Yes, they fit|👡 No, they are small|👡 No, they are big
Q: What matches the jacket?|O que combina com a jaqueta?|3|👟 The sneakers|👠 The heels|🧦 The socks
Q: What is too tight?|O que está muito apertado?|5|👠 The heels|🧦 The socks|👟 The sneakers
B: try|👟|experimentar|I try the shoes.|She tries the shoes.|He tried the sneakers.|Ele experimentou o tênis.
B: dance|💃|dançar|I dance in the shoes.|She dances in the shoes.|We danced all night.|Nós dançamos a noite toda.
B: tie|🎀|amarrar|I tie the laces.|She ties the laces.|He tied his shoes.|Ele amarrou os sapatos.
B: jump|🦘|pular|I jump in the sneakers.|She jumps in the sneakers.|They jumped on the floor.|Eles pularam no chão.
LAB: sh|Laboratório de sons: sandals, socks e size|Sandals tem a força no começo, “SÉN-dolz”. Socks soa “SÓKS”. Size soa “SÁIZ”.|Em sandals, o a soa é: SÉN-dolz.
W: sandals|SÉN-dolz|sandálias|a = é|sandwiches|SÉN-uí-tchiz
W: socks|SÓKS|meias|o aberto|sacks|SÉKS
W: size|SÁIZ|tamanho|i = ái|seas|SÍZ
G: 0|Do|Are|Is
G: 1|match|matches|matching
G: 2|comfortable|comfort|comfortably
G: 4|fit|fits|fitting
X: 😍|I love them|Eu amei|elogiar|I love them, they are cool.|Eu amei, eles são legais.
X: 😊|Just right|No ponto certo|aprovar|Just right, they fit well.|No ponto certo, eles servem bem.
X: 🙁|Too small|Pequeno demais|reclamar|Too small, try a bigger size.|Pequeno demais, tente um tamanho maior.
X: 💃|Let’s dance|Vamos dançar|animar|Let’s dance, Ariel!|Vamos dançar, Ariel!

N: 7030043
C: Lady,Tramp | polly,tommy | No quintal, Lady e Tramp contam o que amam, odeiam e preferem comer: love, hate, prefer.
S: expressar preferências com love, hate e prefer: I love spaghetti. I prefer cheese
Y: Hoje você aprende a falar de gosto: love (amar), hate (odiar), prefer (preferir). I love spaghetti. I hate onions. I prefer cheese.
F: Lady and the Tramp | 🎬 Animação | 1955 | uma animação clássica da Disney sobre uma cadela elegante e um vira-lata que dividem um prato de espaguete | falar do que se ama, odeia e prefere | bakery | 🍝,🐕,🍖
V: 🍝|spaghetti|espaguete|spa-GUÉ-ti
V: 🍖|bone|osso|BÔUN
V: 🧀|cheese|queijo|TCHÍZ
V: 🥩|meat|carne|MÍT
V: 🍅|tomato|tomate|ta-MÊI-tô
V: 🧅|onion|cebola|Â-nion
H: I love spaghetti.|Eu amo espaguete.
H: I hate cold bones.|Eu odeio ossos frios.
H: I prefer cheese.|Eu prefiro queijo.
H: I love meat.|Eu amo carne.
H: I hate tomatoes.|Eu odeio tomates.
L: Tramp, I love spaghetti.|Tramp, eu amo espaguete.
L: Me too, Lady. I hate cold bones.|Eu também, Lady. Eu odeio ossos frios.
L: I prefer cheese. Do you like cheese?|Eu prefiro queijo. Você gosta de queijo?
L: I love cheese. I love meat, too.|Eu amo queijo. Eu amo carne também.
L: Do you like tomatoes?|Você gosta de tomates?
L: No, I hate tomatoes. And onions?|Não, eu odeio tomates. E cebolas?
L: I hate onions, too. Spaghetti is best.|Eu odeio cebolas também. Espaguete é o melhor.
L: Then let’s share one plate.|Então vamos dividir um prato.
Q: What does Lady love?|O que a Lady ama?|0|🍝 Spaghetti|🍖 Cold bones|🍅 Tomatoes
Q: What does Lady prefer?|O que a Lady prefere?|2|🧀 Cheese|🥩 Meat|🧅 Onions
Q: What do they hate?|O que eles odeiam?|5|🍅 Tomatoes|🍝 Spaghetti|🧀 Cheese
B: lick|👅|lamber|I lick the plate.|She licks the plate.|He licked the cheese.|Ele lambeu o queijo.
B: share|🤝|dividir|I share my plate.|She shares her plate.|He shared the bone.|Ele dividiu o osso.
B: sniff|👃|farejar|I sniff the meat.|She sniffs the meat.|He sniffed the cheese.|Ele farejou o queijo.
B: bark|🐕|latir|I bark at the door.|She barks at the door.|They barked loudly.|Eles latiram alto.
LAB: sp|Laboratório de sons: spaghetti, cheese e tomato|Spaghetti tem a força no -GUÉ-: spa-GUÉ-ti. Cheese começa com tch, “TCHÍZ”. Tomato soa “ta-MÊI-tô”.|Em spaghetti, o gh soa como g duro: spa-GUÉ-ti.
W: spaghetti|spa-GUÉ-ti|espaguete|gh = g|spa|SPÁ
W: cheese|TCHÍZ|queijo|ch = tch|these|DÍZ
W: tomato|ta-MÊI-tô|tomate|a = êi|tornado|tor-NÊI-dô
G: 0|love|loves|loving
G: 1|hate|hates|hating
G: 2|prefer|prefers|preferring
G: 3|love|loves|loving
X: 😋|Yummy|Que delícia|elogiar|Yummy, this is my favorite.|Que delícia, este é o meu favorito.
X: 🤢|Yuck|Eca|reclamar|Yuck, I hate onions.|Eca, eu odeio cebolas.
X: 😍|My favorite|Meu favorito|elogiar|My favorite is spaghetti.|O meu favorito é espaguete.
X: 🐕|Let’s share|Vamos dividir|propor|Let’s share this plate.|Vamos dividir este prato.

N: 7009814
C: Jenna,Dawn | polly,misshoney | Na cozinha de casa, Jenna e Dawn conferem a receita: How much? How many?
S: quantidades numa receita com How much e How many: How many eggs? How much milk
Y: Hoje você aprende a perguntar quantidades: How many para o que se conta (eggs) e How much para o que não se conta (milk).
F: Waitress | 🎬 Filme | 2007 | um filme escrito e dirigido por Adrienne Shelly, sobre uma garçonete que faz tortas deliciosas numa pequena lanchonete | perguntar quantidades numa receita | bakery | 🥧,🥚,🍎
V: 🥚|eggs|ovos|ÉGZ
V: 🍚|sugar|açúcar|SHÚ-ger
V: 🌾|flour|farinha|FLÁU-er
V: 🍎|apples|maçãs|É-polz
V: 🍇|raisins|uvas-passas|RÊI-zinz
V: 🥧|pie|torta|PÁI
H: How many eggs do I need?|Quantos ovos eu preciso?
H: How much sugar do I need?|Quanto açúcar eu preciso?
H: How much flour do I need?|Quanta farinha eu preciso?
H: How many apples do I need?|Quantas maçãs eu preciso?
H: A handful of raisins, please.|Um punhado de uvas-passas, por favor.
L: Dawn, how many eggs do I need?|Dawn, quantos ovos eu preciso?
L: Two eggs, Jenna.|Dois ovos, Jenna.
L: How much sugar do I need?|Quanto açúcar eu preciso?
L: One cup of sugar.|Uma xícara de açúcar.
L: And how much flour?|E quanta farinha?
L: Two cups. How many apples do we have?|Duas xícaras. Quantas maçãs nós temos?
L: We have five apples. Add a handful of raisins.|Nós temos cinco maçãs. Ponha um punhado de uvas-passas.
L: Great. The pie is ready to bake!|Ótimo. A torta está pronta para assar!
Q: How many eggs does Jenna need?|Quantos ovos a Jenna precisa?|1|🥚 Two eggs|🥚 Five eggs|🥚 One egg
Q: How much sugar does she need?|Quanto açúcar ela precisa?|3|🍚 One cup|🍚 Two cups|🍚 Five cups
Q: How many apples do they have?|Quantas maçãs eles têm?|6|🍎 Five apples|🍎 Two apples|🍎 One apple
B: whisk|🥄|bater (na colher)|I whisk the batter.|She whisks the batter.|He whisked the eggs.|Ele bateu os ovos.
B: bake|🥧|assar|I bake a pie.|She bakes a pie.|We baked it for an hour.|Nós a assamos por uma hora.
B: pour|🫗|despejar|I pour the batter.|She pours the batter.|He poured the sugar.|Ele despejou o açúcar.
B: crack|🥚|quebrar (ovo)|I crack the eggs.|She cracks the eggs.|They cracked two eggs.|Eles quebraram dois ovos.
LAB: fl|Laboratório de sons: eggs, flour e raisins|Eggs tem e aberto, “ÉGZ”. Flour soa como flower, “FLÁU-er”. Raisins soa “RÊI-zinz”.|Em flour, o our soa áu-er: FLÁU-er.
W: eggs|ÉGZ|ovos|e aberto|aches|ÊIKS
W: flour|FLÁU-er|farinha|our = áu-er|floor|FLÓR
W: raisins|RÊI-zinz|uvas-passas|ai = êi|raising|RÊI-zing
G: 0|many|much|more
G: 1|much|many|more
G: 2|much|many|long
G: 3|many|much|more
X: 🥧|Smells good|Que cheiro bom|elogiar|Smells good, the pie.|Que cheiro bom, a torta.
X: 😊|A little more|Um pouco mais|pedir|A little more honey, please.|Um pouco mais de mel, por favor.
X: 🤔|Let me check|Deixe-me conferir|conferir|Let me check the recipe.|Deixe-me conferir a receita.
X: 🙌|All done|Tudo pronto|terminar|All done, let’s bake.|Tudo pronto, vamos assar.
''')
