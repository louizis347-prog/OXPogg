# Lote B (cinema), dados 5: episódios A1 7910024 .. 7910025. Formato: ver zz_b_lib.py.
from v3.zz_b_lib import add

add('''
N: 7910024
C: Westley,Buttercup | tom,polly | No jardim do castelo, Westley e Buttercup dizem o que precisam e o que não precisam fazer: have to, don’t have to.
S: obrigação com have to e don’t have to: I have to find a horse. You don’t have to wear a dress
Y: Hoje você aprende a falar de obrigação: have to (precisar) e don’t have to (não precisar). I have to find a horse. You don’t have to wear a dress.
F: The Princess Bride | 🎬 Filme | 1987 | um filme dirigido por Rob Reiner, sobre um jovem que enfrenta muitos perigos para reencontrar a mulher que ama | dizer o que se precisa e o que não se precisa fazer | castle | ⚔️,🐴,🏰
V: 🐴|horse|cavalo|RÓRS
V: 👗|dress|vestido|DRÉS
V: ⚔️|sword|espada|SÓRD
V: 🏰|castle|castelo|KÉ-sol
V: 🌹|rose|rosa|RÔUZ
V: 🛡️|shield|escudo|SHÍLD
H: I have to find a horse.|Eu preciso achar um cavalo.
H: You don’t have to wear a dress.|Você não precisa usar um vestido.
H: I have to take my sword.|Eu preciso levar minha espada.
H: We have to go to the castle.|Nós precisamos ir ao castelo.
H: You don’t have to bring a rose.|Você não precisa trazer uma rosa.
L: Buttercup, I have to find a horse.|Buttercup, eu preciso achar um cavalo.
L: Why, Westley? We have to go to the castle.|Por quê, Westley? Nós precisamos ir ao castelo.
L: Yes. I have to take my sword.|Sim. Eu preciso levar minha espada.
L: You don’t have to wear a dress.|Você não precisa usar um vestido.
L: Good. I wear my old boots.|Bom. Eu uso minhas botas velhas.
L: You don’t have to bring a rose.|Você não precisa trazer uma rosa.
L: But I want to. It is for the castle.|Mas eu quero. É para o castelo.
L: Take the shield, too. Let’s go!|Leve o escudo também. Vamos!
Q: What does Westley have to find?|O que o Westley precisa achar?|0|🐴 A horse|🏰 A castle|🌹 A rose
Q: What doesn’t Buttercup have to wear?|O que a Buttercup não precisa usar?|3|👗 A dress|⚔️ A sword|🛡️ A shield
Q: What doesn’t she have to bring?|O que ela não precisa trazer?|5|🌹 A rose|🐴 A horse|⚔️ A sword
B: ride|🐴|cavalgar|I ride a horse.|He rides a horse.|She rode all day.|Ela cavalgou o dia todo.
B: fight|⚔️|lutar|I fight with a sword.|He fights with a sword.|They fought bravely.|Eles lutaram com bravura.
B: climb|🧗|escalar|I climb the wall.|He climbs the wall.|She climbed the tower.|Ela escalou a torre.
B: save|🛟|salvar|I save my friend.|He saves his friend.|They saved the day.|Eles salvaram o dia.
LAB: ho|Laboratório de sons: horse, sword e castle|Horse soa “RÓRS”, com h soprado. Em sword, o w é mudo: “SÓRD”. Em castle, o t é mudo: “KÉ-sol”.|Em sword, o w não se fala: SÓRD.
W: horse|RÓRS|cavalo|h soprado|hose|RÔUZ
W: sword|SÓRD|espada|w mudo|sore|SÓR
W: castle|KÉ-sol|castelo|t mudo|cattle|KÉ-dol
G: 0|have|has|having
G: 1|don’t|doesn’t|not
G: 2|to|for|of
G: 4|don’t|doesn’t|not
X: 😅|As you wish|Como quiser|aceitar|As you wish, Buttercup.|Como quiser, Buttercup.
X: 💪|Be brave|Seja corajosa|animar|Be brave, we can do it.|Seja corajosa, nós conseguimos.
X: 😮|Look out|Cuidado|avisar|Look out, a sword!|Cuidado, uma espada!
X: 🙂|Don’t worry|Não se preocupe|acalmar|Don’t worry, I am here.|Não se preocupe, eu estou aqui.

N: 80197
C: Duchess,O’Malley | polly,tom | Nos telhados de Paris, Duchess e O’Malley contam onde e com quem moram: live in, live with.
S: dizer onde e com quem mora: I live in a mansion. I live with my kittens
Y: Hoje você aprende a dizer onde e com quem mora: live in (morar em) e live with (morar com). I live in Paris. I live with my kittens.
F: The Aristocats | 🎬 Animação | 1970 | uma animação da Disney sobre uma gata elegante e seus filhotes que se perdem em Paris e ganham a ajuda de um gato de rua | dizer onde e com quem se mora | viaduct | 🐱,🎹,🗼
V: 🏠|mansion|mansão|MÉN-shan
V: 🏙️|city|cidade|SÍ-ti
V: 🐱|kittens|gatinhos|KÍ-tnz
V: 🏚️|roof|telhado|RÚF
V: 🎹|piano|piano|pi-Á-nô
V: 🐈|cat|gato|KÉT
H: I live in a big mansion.|Eu moro numa mansão grande.
H: I live in Paris, a big city.|Eu moro em Paris, uma cidade grande.
H: I live with my kittens.|Eu moro com os meus gatinhos.
H: He lives on a roof.|Ele mora num telhado.
H: We live with a piano!|Nós moramos com um piano!
L: O’Malley, where do you live?|O’Malley, onde você mora?
L: I live on a roof, Duchess. And you?|Eu moro num telhado, Duchess. E você?
L: I live in a big mansion.|Eu moro numa mansão grande.
L: Is it in Paris, a big city?|Fica em Paris, uma cidade grande?
L: Yes. I live with my kittens.|Sim. Eu moro com os meus gatinhos.
L: Do you live with a cat, too?|Você mora com um gato também?
L: No, but we live with a piano!|Não, mas nós moramos com um piano!
L: Then I visit you. Is the roof open?|Então eu visito vocês. O telhado está aberto?
Q: Where does O’Malley live?|Onde o O’Malley mora?|1|🏚️ On a roof|🏠 In a mansion|🎹 In a piano
Q: Who does Duchess live with?|Com quem a Duchess mora?|4|🐱 Her kittens|🐈 O’Malley|🎹 A dog
Q: What do they live with?|Com o que eles moram?|6|🎹 A piano|🐱 A bird|🏚️ A roof
B: live|🏠|morar|I live in Paris.|She lives in Paris.|He lived on a roof.|Ele morou num telhado.
B: purr|😸|ronronar|I purr on the piano.|She purrs on the piano.|The kittens purred.|Os gatinhos ronronaram.
B: jump|🦘|pular|I jump on the roof.|He jumps on the roof.|They jumped down.|Eles pularam para baixo.
B: meow|🐱|miar|I meow at night.|She meows at night.|The kittens meowed.|Os gatinhos miaram.
LAB: ki|Laboratório de sons: kittens, roof e piano|Kittens soa “KÍ-tnz”, com tt curto. Roof tem u longo, “RÚF”. Piano tem a força no meio, “pi-Á-nô”.|Em roof, alongue o u: RÚÚF.
W: kittens|KÍ-tnz|gatinhos|tt curto|mittens|MÍ-tnz
W: roof|RÚF|telhado|oo = ú|rough|RÂF
W: piano|pi-Á-nô|piano|força no meio|panel|PÉ-nol
G: 0|in|on|at
G: 2|with|in|at
G: 3|lives|live|living
G: 4|with|at|in
X: 😍|How lovely|Que lindo|admirar|How lovely, Paris!|Que lindo, Paris!
X: 😊|Come in|Entre|convidar|Come in, O’Malley.|Entre, O’Malley.
X: 🎶|Play for us|Toque para nós|pedir|Play for us, please.|Toque para nós, por favor.
X: 😸|Meow|Miau|imitar|Meow, I am hungry.|Miau, eu estou com fome.

N: 7080197
C: Emmet,Wyldstyle | tommy,polly | Na cidade de peças, Emmet e Wyldstyle dizem do que cada coisa é feita: made of.
S: dizer de que material é feito: It is made of plastic
Y: Hoje você aprende made of + material: The brick is made of plastic. The door is made of wood. What is the tower made of?
F: The Lego Movie | 🎬 Animação | 2014 | uma animação dirigida por Phil Lord e Christopher Miller, sobre um operário de peças de montar que vira herói de um mundo inteiro feito de blocos | dizer de que material as coisas são feitas | toyshop | 🧱,🏗️,🔩
V: 🧱|brick|bloco|BRÍK
V: 🪵|wood|madeira|UÚD
V: 🔩|metal|metal|MÉ-dol
V: 🪟|glass|vidro|GLÉS
V: 🧊|plastic|plástico|PLÉS-tik
V: 🏗️|tower|torre|TÁU-er
H: The brick is made of plastic.|O bloco é feito de plástico.
H: The door is made of wood.|A porta é feita de madeira.
H: My sword is made of metal.|Minha espada é feita de metal.
H: The window is made of glass.|A janela é feita de vidro.
H: What is the tower made of?|De que é feita a torre?
L: Wyldstyle, look at this brick.|Wyldstyle, olhe este bloco.
L: The brick is made of plastic, Emmet.|O bloco é feito de plástico, Emmet.
L: And the door? It is made of wood.|E a porta? Ela é feita de madeira.
L: My sword is made of metal.|Minha espada é feita de metal.
L: Careful! The window is made of glass.|Cuidado! A janela é feita de vidro.
L: What is the tower made of?|De que é feita a torre?
L: It is made of bricks, of course!|Ela é feita de blocos, claro!
L: Then let’s snap one more on top.|Então vamos encaixar mais um em cima.
Q: What is the brick made of?|De que é feito o bloco?|1|🧊 Plastic|🪵 Wood|🔩 Metal
Q: What is the sword made of?|De que é feita a espada?|3|🔩 Metal|🪟 Glass|🪵 Wood
Q: What is the tower made of?|De que é feita a torre?|6|🧱 Bricks|🪟 Glass|🪵 Wood
B: snap|🔗|encaixar|I snap the brick.|He snaps the brick.|She snapped two pieces.|Ela encaixou duas peças.
B: stack|🧱|empilhar|I stack the bricks.|He stacks the bricks.|They stacked a tower.|Eles empilharam uma torre.
B: break|💥|quebrar|I break the glass.|He breaks the glass.|The window broke.|A janela quebrou.
B: find|🔎|achar|I find a red brick.|She finds a red brick.|We found the door.|Nós achamos a porta.
LAB: pl|Laboratório de sons: plastic, metal e glass|Plastic começa com pl junto, “PLÉS-tik”. Metal tem tt rápido, “MÉ-dol”. Glass soa “GLÉS”.|Em metal, o t vira um d suave: MÉ-dol.
W: plastic|PLÉS-tik|plástico|pl junto|plate|PLÊIT
W: metal|MÉ-dol|metal|t = d suave|medal|MÉ-dol
W: glass|GLÉS|vidro|a = é|class|KLÉS
G: 0|made|make|making
G: 1|of|in|at
G: 2|made|make|making
G: 4|What|Where|When
X: 😮|Awesome|Demais|elogiar|Awesome, a tall tower!|Demais, uma torre alta!
X: 🧱|Everything is awesome|Tudo é demais|comemorar|Everything is awesome today.|Tudo é demais hoje.
X: 😅|Be careful|Tenha cuidado|avisar|Be careful with the glass.|Tenha cuidado com o vidro.
X: 🤝|Let’s build|Vamos montar|propor|Let’s build it together.|Vamos montar juntos.

N: 80198
C: Christian,Satine | tom,polly | No grande salão, Christian e Satine dão opinião: beautiful, amazing, wonderful, terrible, ugly.
S: dar opinião com beautiful, amazing, wonderful e terrible: The dress is beautiful
Y: Hoje você aprende a dar opinião: beautiful (lindo), amazing (incrível), wonderful (maravilhoso), terrible (terrível), ugly (feio).
F: Moulin Rouge! | 🎬 Musical | 2001 | um filme musical dirigido por Baz Luhrmann, sobre um poeta que se apaixona por uma cantora famosa num cabaré de Paris | dar opinião sobre o que se vê | castle | 💃,💎,🎭
V: 👗|dress|vestido|DRÉS
V: 💎|diamond|diamante|DÁI-mand
V: 🎭|show|espetáculo|SHÔU
V: 🎵|song|canção|SÓNG
V: 🌹|flower|flor|FLÁU-er
V: 🎡|windmill|moinho|UÍND-mil
H: The dress is beautiful!|O vestido é lindo!
H: The diamond is amazing.|O diamante é incrível.
H: The show is wonderful.|O espetáculo é maravilhoso.
H: This song is terrible.|Esta canção é terrível.
H: The old flower is ugly.|A flor velha é feia.
L: Satine, the dress is beautiful!|Satine, o vestido é lindo!
L: Thank you, Christian. The diamond is amazing, too.|Obrigada, Christian. O diamante também é incrível.
L: And the show is wonderful.|E o espetáculo é maravilhoso.
L: Not everything. This song is terrible.|Nem tudo. Esta canção é terrível.
L: Really? I love it!|Sério? Eu adoro!
L: Look at the old flower. It is ugly.|Olhe a flor velha. Ela é feia.
L: But the windmill is lovely at night.|Mas o moinho é lindo à noite.
L: How beautiful! Let’s sing together.|Que lindo! Vamos cantar juntos.
Q: How is the dress?|Como é o vestido?|0|👗 Beautiful|👗 Terrible|👗 Ugly
Q: How is the song?|Como é a canção?|3|🎵 Terrible|🎵 Wonderful|🎵 Amazing
Q: How is the old flower?|Como é a flor velha?|5|🌹 Ugly|🌹 Beautiful|🌹 Amazing
B: look|👀|olhar|I look at the dress.|She looks at the dress.|He looked at the show.|Ele olhou o espetáculo.
B: sing|🎤|cantar|I sing a love song.|She sings a love song.|They sang together.|Eles cantaram juntos.
B: love|❤️|amar|I love this show.|He loves this show.|She loved the song.|Ela amou a canção.
B: think|🤔|achar, pensar|I think it is amazing.|She thinks it is amazing.|We thought it was great.|Nós achamos que era ótimo.
LAB: be|Laboratório de sons: beautiful, wonderful e terrible|Beautiful soa “BIÚ-ti-ful”. Wonderful soa “UÂN-der-ful”. Terrible soa “TÉ-ri-bol”.|Em beautiful, comece com biú: BIÚ-ti-ful.
W: beautiful|BIÚ-ti-ful|lindo|eau = iú|bottle|BÓ-tol
W: wonderful|UÂN-der-ful|maravilhoso|o = â|wander|UÓN-der
W: terrible|TÉ-ri-bol|terrível|força no começo|terror|TÉ-rer
G: 0|beautiful|beauty|beautifully
G: 1|amazing|amaze|amazed
G: 2|wonderful|wonder|wonderfully
G: 3|terrible|terror|terribly
X: 😍|I love it|Eu adoro|elogiar|I love it, it is so pretty.|Eu adoro, é tão bonito.
X: 😮|What a night|Que noite|se surpreender|What a night, Satine!|Que noite, Satine!
X: 😬|Not really|Não muito|discordar|Not really, I don’t like it.|Não muito, eu não gosto.
X: 🎭|Bravo|Bravo|elogiar|Bravo, what a show!|Bravo, que espetáculo!

N: 7080198
C: Merida,Elinor | polly,misshoney | No pátio do castelo, Merida e Elinor reforçam as qualidades com so: so funny, so brave.
S: reforçar adjetivos com so: You are so brave. The bear is so big
Y: Hoje você aprende so + adjetivo: You are so brave! The bear is so big! My horse is so fast!
F: Brave | 🎬 Animação | 2012 | uma animação dirigida por Mark Andrews e Brenda Chapman, sobre uma princesa escocesa que quer decidir seu próprio destino | reforçar as qualidades com so | castle | 🏹,🐻,🐴
V: 🏹|bow|arco|BÔU
V: 🐻|bear|urso|BÉR
V: 🐴|horse|cavalo|RÓRS
V: 🏰|castle|castelo|KÉ-sol
V: 👑|crown|coroa|KRÁUN
V: 🧶|tapestry|tapeçaria|TÉ-pes-tri
H: You are so brave!|Você é tão corajosa!
H: The bear is so big!|O urso é tão grande!
H: My horse is so fast!|Meu cavalo é tão rápido!
H: The castle is so old.|O castelo é tão velho.
H: The crown is so heavy!|A coroa é tão pesada!
L: Mom, look at my bow!|Mãe, olhe o meu arco!
L: You are so brave, Merida!|Você é tão corajosa, Merida!
L: The bear is so big!|O urso é tão grande!
L: Don’t be afraid. My horse is so fast!|Não tenha medo. Meu cavalo é tão rápido!
L: The castle is so old, but I love it.|O castelo é tão velho, mas eu o amo.
L: The crown is so heavy!|A coroa é tão pesada!
L: You look so funny with it.|Você fica tão engraçada com ela.
L: Mom, you are so funny, too!|Mãe, você também é tão engraçada!
Q: What is so brave?|Quem é tão corajosa?|1|🏹 Merida|👑 The queen|🐴 The horse
Q: What is so fast?|O que é tão rápido?|3|🐴 The horse|🐻 The bear|🏰 The castle
Q: What is so heavy?|O que é tão pesado?|5|👑 The crown|🏹 The bow|🏰 The castle
B: shoot|🏹|atirar (flecha)|I shoot an arrow.|She shoots an arrow.|He shot twice.|Ele atirou duas vezes.
B: laugh|😂|rir|I laugh with Mom.|She laughs with Mom.|We laughed a lot.|Nós rimos muito.
B: ride|🐴|cavalgar|I ride my horse.|She rides her horse.|They rode in the forest.|Eles cavalgaram na floresta.
B: hold|🤝|segurar|I hold the bow.|She holds the bow.|He held the crown.|Ele segurou a coroa.
LAB: bo|Laboratório de sons: bow, bear e crown|Bow soa “BÔU”, como em boat. Bear soa “BÉR”. Crown soa “KRÁUN”.|Em crown, o ow soa áu: KRÁUN.
W: bow|BÔU|arco|ow = ôu|boat|BÔUT
W: bear|BÉR|urso|ea = é|beer|BÍR
W: crown|KRÁUN|coroa|ow = áu|clown|KLÁUN
G: 0|so|such|much
G: 1|so|such|much
G: 2|so|such|much
G: 3|so|such|much
X: 😲|Wow|Uau|se surpreender|Wow, you are so strong!|Uau, você é tão forte!
X: 😂|That’s funny|Que engraçado|rir|That’s funny, Mom.|Que engraçado, mãe.
X: 🤗|I’m proud|Tenho orgulho|elogiar|I’m proud of you.|Tenho orgulho de você.
X: 💪|Be brave|Seja corajosa|animar|Be brave, Merida.|Seja corajosa, Merida.

N: 7080200
C: Sabine,Bean | misshoney,tom | Numa estrada da França, Sabine e Bean dizem como vão para o mar: on foot, by car, by train.
S: como se locomove: on foot, by car, by train
Y: Hoje você aprende como ir a um lugar: on foot (a pé) e by + veículo: by car, by train, by bus, by bike.
F: Mr. Bean’s Holiday | 🎬 Filme | 2007 | uma comédia dirigida por Steve Bendelack, sobre um homem atrapalhado que viaja pela França para chegar à praia | dizer como se vai de um lugar a outro | viaduct | 🚗,🚆,🏖️
V: 🚗|car|carro|KÁR
V: 🚶|foot|pé|FÚT
V: 🚆|train|trem|TRÊIN
V: 🚌|bus|ônibus|BÂS
V: 🚲|bike|bicicleta|BÁIK
V: 🏖️|beach|praia|BÍTCH
H: I go by car.|Eu vou de carro.
H: I go on foot.|Eu vou a pé.
H: We go by train.|Nós vamos de trem.
H: You go by bus.|Você vai de ônibus.
H: She goes by bike.|Ela vai de bicicleta.
L: Bean, how do you go to the beach?|Bean, como você vai para a praia?
L: I go by car. Beep, beep!|Eu vou de carro. Bip, bip!
L: I go on foot. It is fun.|Eu vou a pé. É divertido.
L: We go by train. It is fast.|Nós vamos de trem. É rápido.
L: You go by bus, don’t you?|Você vai de ônibus, não é?
L: No, I go by bike.|Não, eu vou de bicicleta.
L: She goes by bike? Very funny!|Ela vai de bicicleta? Muito engraçado!
L: See you at the beach, Bean.|Até a praia, Bean.
Q: How does Bean go first?|Como o Bean vai primeiro?|1|🚗 By car|🚶 On foot|🚆 By train
Q: How do they go together?|Como eles vão juntos?|3|🚆 By train|🚌 By bus|🚲 By bike
Q: How does Bean go in the end?|Como o Bean vai no fim?|5|🚲 By bike|🚗 By car|🚌 By bus
B: go|➡️|ir|I go by train.|She goes by train.|He went on foot.|Ele foi a pé.
B: drive|🚗|dirigir|I drive a car.|He drives a car.|She drove to the beach.|Ela dirigiu até a praia.
B: ride|🚲|andar de|I ride a bike.|She rides a bike.|They rode to the sea.|Eles foram de bicicleta ao mar.
B: walk|🚶|andar a pé|I walk to the station.|He walks to the station.|We walked a mile.|Nós andamos uma milha.
LAB: ca|Laboratório de sons: car, train e beach|Car soa “KÁR”, com a aberto. Train soa “TRÊIN”. Beach termina em tch, “BÍTCH”.|Em train, o ai soa êi: TRÊIN.
W: car|KÁR|carro|a aberto|core|KÓR
W: train|TRÊIN|trem|ai = êi|tray|TRÊI
W: beach|BÍTCH|praia|ch = tch|peach|PÍTCH
G: 0|by|in|on
G: 1|on|by|in
G: 2|by|in|on
G: 4|by|in|on
X: 😆|Beep beep|Bip bip|imitar|Beep beep, here I come.|Bip bip, aí vou eu.
X: 🏖️|Have fun|Divirta-se|desejar|Have fun at the beach.|Divirta-se na praia.
X: 😮|Hurry up|Ande rápido|apressar|Hurry up, the train leaves.|Ande rápido, o trem vai sair.
X: 👋|Bye bye|Tchau|despedir-se|Bye bye, Sabine.|Tchau, Sabine.

N: 80202
C: Max,Duke | tom,tommy | No parque, Max e Duke escolhem entre duas coisas: Which do you prefer?
S: escolher entre duas coisas com Which do you prefer? e I prefer…
Y: Hoje você aprende a escolher: Which do you prefer, the park or the couch? I prefer the couch.
F: The Secret Life of Pets | 🎬 Animação | 2016 | uma animação dirigida por Chris Renaud, sobre cachorros e outros bichos que fazem o que querem quando os donos saem | escolher entre duas coisas | jungle | 🐕,🛋️,🌳
V: 🌳|park|parque|PÁRK
V: 🛋️|couch|sofá|KÁUTCH
V: 🛁|bath|banho|BÉF
V: 🦴|bone|osso|BÔUN
V: ⚽|ball|bola|BÓL
V: 🦮|leash|coleira|LÍTCH
H: Which do you prefer, the park or the couch?|Qual você prefere, o parque ou o sofá?
H: I prefer the couch.|Eu prefiro o sofá.
H: I prefer a short bath.|Eu prefiro um banho curto.
H: Which do you prefer, a bone or a ball?|Qual você prefere, um osso ou uma bola?
H: I prefer the red ball.|Eu prefiro a bola vermelha.
L: Duke, which do you prefer, the park or the couch?|Duke, qual você prefere, o parque ou o sofá?
L: I prefer the couch, Max.|Eu prefiro o sofá, Max.
L: And a bath? Which do you prefer, long or short?|E um banho? Qual você prefere, longo ou curto?
L: I prefer a short bath.|Eu prefiro um banho curto.
L: Which do you prefer, a bone or a ball?|Qual você prefere, um osso ou uma bola?
L: I prefer the red ball.|Eu prefiro a bola vermelha.
L: Good choice. Take your leash. We go to the park!|Boa escolha. Pegue sua coleira. Nós vamos ao parque!
L: Okay, I prefer that, too.|Certo, eu também prefiro isso.
Q: What does Duke prefer first?|O que o Duke prefere primeiro?|1|🛋️ The couch|🌳 The park|🛁 A bath
Q: What kind of bath does Duke prefer?|Que tipo de banho o Duke prefere?|3|🛁 A short bath|🛁 A long bath|🚿 No bath
Q: What does Duke prefer to play with?|Com o que o Duke prefere brincar?|5|⚽ The red ball|🦴 A bone|🦮 A leash
B: prefer|⭐|preferir|I prefer the couch.|He prefers the couch.|She preferred the park.|Ela preferiu o parque.
B: choose|☑️|escolher|I choose the ball.|He chooses the ball.|They chose a bone.|Eles escolheram um osso.
B: fetch|🎾|buscar|I fetch the ball.|He fetches the ball.|The dog fetched a bone.|O cachorro buscou um osso.
B: sniff|👃|farejar|I sniff the park.|He sniffs the park.|They sniffed the bone.|Eles farejaram o osso.
LAB: co|Laboratório de sons: couch, bath e leash|Couch soa “KÁUTCH”, com ou = áu. Bath termina em th, “BÉF”. Leash soa “LÍTCH”, com ea = í.|Em bath, o th final é soprado: BÉF, com a língua entre os dentes.
W: couch|KÁUTCH|sofá|ou = áu|coach|KÔUTCH
W: bath|BÉF|banho|th soprado|bat|BÉT
W: leash|LÍTCH|coleira|ea = í|lease|LÍS
G: 0|Which|What|Who
G: 1|prefer|prefers|preferring
G: 3|Which|What|Who
G: 4|prefer|prefers|preferring
X: 🤔|Let me think|Deixe-me pensar|pensar|Let me think, the park.|Deixe-me pensar, o parque.
X: 😊|Good choice|Boa escolha|elogiar|Good choice, Duke.|Boa escolha, Duke.
X: 🐕|Let’s go|Vamos|animar|Let’s go to the park.|Vamos ao parque.
X: 😴|I’m sleepy|Estou com sono|reclamar|I’m sleepy, I prefer the couch.|Estou com sono, eu prefiro o sofá.

N: 7080202
C: Dumbo,Timothy | tom,tommy | No circo, Dumbo e o ratinho Timothy comparam tamanhos com as … as.
S: comparar com as … as: My ears are as big as a blanket. The feather is as light as air
Y: Hoje você aprende a comparar com as + adjetivo + as: as big as, as small as, as light as e not as small as.
F: Dumbo | 🎬 Animação | 1941 | uma animação clássica da Disney sobre um elefantinho de orelhas enormes que aprende a voar num circo | comparar tamanhos | toyshop | 🐘,🎪,🪶
V: 👂|ears|orelhas|ÍRZ
V: 🐘|elephant|elefante|É-le-fant
V: 🐭|mouse|ratinho|MÁUS
V: 🪶|feather|pena|FÉ-der
V: 🎪|tent|tenda|TÉNT
V: 🥜|peanut|amendoim|PÍ-nât
H: My ears are as big as a blanket.|Minhas orelhas são tão grandes quanto um cobertor.
H: The elephant is as big as a bus.|O elefante é tão grande quanto um ônibus.
H: Timothy is as small as a peanut.|O Timothy é tão pequeno quanto um amendoim.
H: The feather is as light as air.|A pena é tão leve quanto o ar.
H: The tent is not as small as a house.|A tenda não é tão pequena quanto uma casa.
L: Timothy, my ears are as big as a blanket.|Timothy, minhas orelhas são tão grandes quanto um cobertor.
L: Yes, Dumbo! The elephant is as big as a bus.|Sim, Dumbo! O elefante é tão grande quanto um ônibus.
L: And you are as small as a peanut, Timothy.|E você é tão pequeno quanto um amendoim, Timothy.
L: True, but I am as brave as a lion.|Verdade, mas eu sou tão corajoso quanto um leão.
L: Take the feather. It is as light as air.|Pegue a pena. Ela é tão leve quanto o ar.
L: With the feather I feel brave.|Com a pena eu me sinto corajoso.
L: The tent is not as small as a house.|A tenda não é tão pequena quanto uma casa.
L: Now fly with your big ears, Dumbo!|Agora voe com as suas orelhas grandes, Dumbo!
Q: How big are Dumbo’s ears?|Quão grandes são as orelhas do Dumbo?|0|👂 As big as a blanket|👂 As small as a peanut|👂 As light as air
Q: How small is Timothy?|Quão pequeno é o Timothy?|2|🥜 As small as a peanut|🐘 As big as a bus|🎪 As big as a house
Q: How light is the feather?|Quão leve é a pena?|4|🪶 As light as air|🪶 As heavy as a bus|🪶 As big as a tent
B: fly|🐘|voar|I fly with my ears.|He flies with his ears.|They flew over the tent.|Eles voaram sobre a tenda.
B: flap|👂|bater (as orelhas)|I flap my ears.|He flaps his ears.|She flapped them fast.|Ela as bateu rápido.
B: jump|🦘|pular|I jump on the tent.|He jumps on the tent.|They jumped high.|Eles pularam alto.
B: laugh|😂|rir|I laugh with Timothy.|He laughs with Timothy.|We laughed a lot.|Nós rimos muito.
LAB: ea|Laboratório de sons: ears, mouse e feather|Ears soa “ÍRZ”, com ea = í. Mouse soa “MÁUS”, com ou = áu. Feather soa “FÉ-der”, com th suave.|Em mouse, o ou soa áu: MÁUS.
W: ears|ÍRZ|orelhas|ea = í|airs|ÉRZ
W: mouse|MÁUS|ratinho|ou = áu|moose|MÚS
W: feather|FÉ-der|pena|th suave|father|FÁ-der
G: 0|as|so|like
G: 1|as|so|like
G: 3|as|so|like
G: 4|not as|no as|not like
X: 😲|Look at me|Olhe para mim|chamar atenção|Look at me, I fly!|Olhe para mim, eu voo!
X: 🐭|Squeak|Quiu|imitar|Squeak, squeak, I am here.|Quiu, quiu, eu estou aqui.
X: 😊|I believe|Eu acredito|animar|I believe in you, Dumbo.|Eu acredito em você, Dumbo.
X: 🤝|Good team|Bom time|elogiar|Good team, Timothy.|Bom time, Timothy.

N: 80204
C: Sosuke,Ponyo | tommy,polly | Na beira do mar, Sosuke e Ponyo contam seus passatempos: collect, knit, fish.
S: falar de passatempos manuais: I collect shells. I knit with yarn. I fish with a rod
Y: Hoje você aprende a falar de passatempos: collect (colecionar), knit (tricotar), fish (pescar).
F: Ponyo | 🎬 Animação | 2008 | uma animação do estúdio japonês Ghibli, dirigida por Hayao Miyazaki, sobre um peixinho que vira menina e faz amizade com um menino à beira do mar | falar de passatempos | lighthouse | 🐟,🌊,🐚
V: 🐚|shells|conchas|SHÉLZ
V: 🧶|yarn|lã|IÁRN
V: 🎣|rod|vara de pescar|RÓD
V: 🪨|stones|pedras|STÔUNZ
V: 🐟|fish|peixe|FÍSH
V: 🌊|sea|mar|SÍ
H: I collect shells.|Eu coleciono conchas.
H: I knit with yarn.|Eu tricoto com lã.
H: I fish with a rod.|Eu pesco com uma vara.
H: We collect stones, too.|Nós também colecionamos pedras.
H: The fish live in the sea.|Os peixes vivem no mar.
L: Ponyo, what is your hobby?|Ponyo, qual é o seu passatempo?
L: I collect shells, Sosuke.|Eu coleciono conchas, Sosuke.
L: I knit with yarn. Look at my scarf.|Eu tricoto com lã. Olhe o meu cachecol.
L: Nice! I fish with a rod.|Legal! Eu pesco com uma vara.
L: We collect stones, too.|Nós também colecionamos pedras.
L: Can I fish with you?|Posso pescar com você?
L: Yes. The fish live in the sea.|Sim. Os peixes vivem no mar.
L: Let’s go to the sea together.|Vamos ao mar juntos.
Q: What does Ponyo collect?|O que a Ponyo coleciona?|1|🐚 Shells|🪨 Stones|🎣 Rods
Q: What does Ponyo knit with?|Com o que a Ponyo tricota?|2|🧶 Yarn|🎣 A rod|🐚 Shells
Q: What does Sosuke fish with?|Com o que o Sosuke pesca?|3|🎣 A rod|🧶 Yarn|🪨 A stone
B: collect|🐚|colecionar|I collect shells.|He collects shells.|She collected stones.|Ela colecionou pedras.
B: knit|🧶|tricotar|I knit a scarf.|She knits a scarf.|He knitted socks.|Ele tricotou meias.
B: fish|🎣|pescar|I fish in the sea.|He fishes in the sea.|They fished all day.|Eles pescaram o dia todo.
B: swim|🏊|nadar|I swim with the fish.|She swims with the fish.|We swam at the beach.|Nós nadamos na praia.
LAB: sh|Laboratório de sons: shells, yarn e fish|Shells começa com sh, “SHÉLZ”. Yarn começa com i, “IÁRN”. Fish termina em sh, “FÍSH”.|Em yarn, o y soa como i: IÁRN.
W: shells|SHÉLZ|conchas|sh|sells|SÉLZ
W: yarn|IÁRN|lã|y = i|barn|BÁRN
W: fish|FÍSH|peixe|sh final|fist|FÍST
G: 0|collect|collects|collecting
G: 1|knit|knits|knitting
G: 2|fish|fishes|fishing
G: 3|collect|collects|collecting
X: 😍|How pretty|Que lindo|admirar|How pretty, a blue shell!|Que lindo, uma concha azul!
X: 🌊|Look at the sea|Olhe o mar|chamar atenção|Look at the sea, Ponyo!|Olhe o mar, Ponyo!
X: 😊|Me too|Eu também|concordar|Me too, I love fish.|Eu também, eu amo peixes.
X: 🙌|Let’s play|Vamos brincar|propor|Let’s play at the beach.|Vamos brincar na praia.

N: 7080204
C: Mia,Sebastian | polly,tom | No bar de jazz, Mia e Sebastian contam o que fazem no tempo livre: in my free time, on weekends.
S: dizer o que faz no tempo livre: In my free time, I play the piano. I listen to jazz on weekends
Y: Hoje você aprende a falar do tempo livre: in my free time (no meu tempo livre) e on weekends (nos fins de semana).
F: La La Land | 🎬 Musical | 2016 | um filme musical dirigido por Damien Chazelle, sobre uma atriz e um pianista que sonham com a carreira em Los Angeles | falar do que se faz no tempo livre | rainycafe | 🎹,🎶,🌅
V: 🎹|piano|piano|pi-Á-nô
V: 🎶|jazz|jazz|DJÉZ
V: ☕|coffee|café|KÓ-fi
V: 🌅|sunset|pôr do sol|SÂN-sét
V: 💃|dance|dança|DÉNS
V: 🎬|movie|filme|MÚ-vi
H: In my free time, I play the piano.|No meu tempo livre, eu toco piano.
H: I listen to jazz on weekends.|Eu ouço jazz nos fins de semana.
H: We have coffee on weekends.|Nós tomamos café nos fins de semana.
H: I watch the sunset on weekends.|Eu vejo o pôr do sol nos fins de semana.
H: In my free time, I dance.|No meu tempo livre, eu danço.
L: Sebastian, what do you do in your free time?|Sebastian, o que você faz no seu tempo livre?
L: In my free time, I play the piano.|No meu tempo livre, eu toco piano.
L: Nice! I listen to jazz on weekends.|Legal! Eu ouço jazz nos fins de semana.
L: We have coffee on weekends, too.|Nós também tomamos café nos fins de semana.
L: I watch the sunset on weekends.|Eu vejo o pôr do sol nos fins de semana.
L: And you, Mia? What do you like?|E você, Mia? Do que você gosta?
L: In my free time, I dance. And I watch a movie.|No meu tempo livre, eu danço. E vejo um filme.
L: Then let’s dance this weekend.|Então vamos dançar neste fim de semana.
Q: What does Sebastian play in his free time?|O que o Sebastian toca no tempo livre?|1|🎹 The piano|🎺 The trumpet|🎻 The violin
Q: When do they have coffee?|Quando eles tomam café?|3|☕ On weekends|☕ At night|☕ In school
Q: What does Mia do in her free time?|O que a Mia faz no tempo livre?|6|💃 She dances|🎹 She plays|🌅 She sleeps
B: play|🎹|tocar|I play the piano.|He plays the piano.|She played jazz.|Ela tocou jazz.
B: listen|👂|ouvir|I listen to jazz.|He listens to jazz.|We listened all night.|Nós ouvimos a noite toda.
B: watch|👀|assistir|I watch a movie.|She watches a movie.|They watched the sunset.|Eles viram o pôr do sol.
B: dance|💃|dançar|I dance on weekends.|She dances on weekends.|We danced in the street.|Nós dançamos na rua.
LAB: ja|Laboratório de sons: jazz, sunset e movie|Jazz começa com dj, “DJÉZ”. Sunset tem a força no começo, “SÂN-sét”. Movie soa “MÚ-vi”.|Em jazz, o j soa dj: DJÉZ.
W: jazz|DJÉZ|jazz|j = dj|has|RÉZ
W: sunset|SÂN-sét|pôr do sol|força no começo|sunrise|SÂN-ráiz
W: movie|MÚ-vi|filme|oo = ú|move|MÚV
G: 0|In my free time|On my free time|At my free time
G: 1|on|in|at
G: 2|on|in|at
G: 4|In my free time|On my free time|At my free time
X: 😍|I love jazz|Eu amo jazz|elogiar|I love jazz, it is great.|Eu amo jazz, é ótimo.
X: 🌅|What a view|Que vista|admirar|What a view, the sunset!|Que vista, o pôr do sol!
X: 🎶|Play it again|Toque de novo|pedir|Play it again, please.|Toque de novo, por favor.
X: 🤗|Same here|Igualmente|concordar|Same here, I dance a lot.|Igualmente, eu danço muito.

N: 7910025
C: WALL-E,EVE | tommy,polly | Num mundo cheio de lixo, WALL-E e EVE decidem o que guardar e o que jogar fora: put away, throw away.
S: guardar ou jogar fora: Put away the box. Throw away the trash
Y: Hoje você aprende put away (guardar) e throw away (jogar fora). Put away the box. Throw away the old trash.
F: WALL-E | 🎬 Animação | 2008 | uma animação da Pixar, dirigida por Andrew Stanton, sobre um robô que limpa o lixo da Terra e encontra uma nova amiga | decidir o que guardar e o que jogar fora | cave | 🤖,🗑️,🌱
V: 🗑️|trash|lixo|TRÉSH
V: 📦|box|caixa|BÓKS
V: 🌱|plant|planta|PLÉNT
V: ♻️|bin|lixeira|BÍN
V: 🔧|tools|ferramentas|TÚLZ
V: 🤖|robot|robô|RÔU-bót
H: Throw away the old trash.|Jogue fora o lixo velho.
H: Put away the box.|Guarde a caixa.
H: Put the plant away.|Guarde a planta.
H: Throw it away in the bin.|Jogue fora na lixeira.
H: Put your tools away.|Guarde suas ferramentas.
L: EVE, look at this old trash.|EVE, olhe este lixo velho.
L: Throw away the old trash, WALL-E.|Jogue fora o lixo velho, WALL-E.
L: Okay. Put away the box.|Certo. Guarde a caixa.
L: Wait! Put the plant away. It is special.|Espere! Guarde a planta. Ela é especial.
L: Yes. Throw it away in the bin.|Sim. Jogue isso fora na lixeira.
L: Put your tools away, too.|Guarde suas ferramentas também.
L: Done. The robot house is clean.|Pronto. A casa do robô está limpa.
L: Thank you, EVE. Beep!|Obrigado, EVE. Bip!
Q: What does EVE throw away?|O que a EVE joga fora?|1|🗑️ The old trash|🌱 The plant|🔧 The tools
Q: What is special?|O que é especial?|3|🌱 The plant|📦 The box|🗑️ The trash
Q: Where does the trash go?|Para onde vai o lixo?|4|♻️ In the bin|📦 In the box|🌱 In the plant
B: put away|📦|guardar|I put away the box.|He puts away the box.|She put away her tools.|Ela guardou suas ferramentas.
B: throw away|🗑️|jogar fora|I throw away the trash.|He throws away the trash.|They threw it away.|Eles jogaram fora.
B: recycle|♻️|reciclar|I recycle the box.|He recycles the box.|She recycled a bottle.|Ela reciclou uma garrafa.
B: keep|🔒|guardar, manter|I keep the plant.|He keeps the plant.|We kept the old tools.|Nós guardamos as ferramentas velhas.
LAB: tr|Laboratório de sons: trash, plant e robot|Trash soa “TRÉSH”. Plant começa com pl junto, “PLÉNT”. Robot soa “RÔU-bót”, com a força no começo.|Em robot, o primeiro o soa ôu: RÔU-bót.
W: trash|TRÉSH|lixo|a = é|trace|TRÊIS
W: plant|PLÉNT|planta|pl junto|plan|PLÉN
W: robot|RÔU-bót|robô|força no começo|rabbit|RÉ-bit
G: 0|Throw away|Throw up|Throw in
G: 1|Put away|Put up|Put off
G: 2|away|at|on
G: 3|away|to|in
X: 😊|Good job|Bom trabalho|elogiar|Good job, WALL-E.|Bom trabalho, WALL-E.
X: 🌱|Look at this|Olhe isto|chamar atenção|Look at this little plant!|Olhe esta plantinha!
X: 🤖|Beep beep|Bip bip|imitar|Beep beep, I am done.|Bip bip, terminei.
X: 😍|So cool|Tão legal|elogiar|So cool, a green plant.|Tão legal, uma planta verde.
''')
