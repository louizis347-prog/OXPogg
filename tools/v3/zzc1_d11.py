# Lote C do A1, dados 11 (n 910049 … 7080350). Ver zzc1_lib.py para o formato.
from v3.zzc1_lib import parse

N = []
N.append(parse("""
N 910049
C Rose,Dorothy | polly,misshoney | A Rose e a Dorothy combinam de manter contato com e-mail, carta e telefone.
F The Golden Girls | 📺 Série | 1985 | uma comédia americana sobre quatro amigas mais velhas, Dorothy, Rose, Blanche e Sophia, que moram juntas em Miami. | manter contato com amigos | cafe2 | 👵,🍰,💌
V 🤝|touch|contato|TÂTCH
V 📧|email|e-mail|Í-mêil
V 📞|phone number|número de telefone|FÔUN NÂM-ber
V ✉️|letter|carta|LÉ-ter
V 💬|message|mensagem|MÉ-sidj
V 🧑‍🤝‍🧑|pen pal|amigo por correspondência|PÉN PÉL
L Dorothy, let us keep in touch.|Dorothy, vamos manter contato.
L Sure. Send me an email.|Claro. Mande-me um e-mail.
L Here is my phone number.|Aqui está o meu número de telefone.
L Write me a letter too.|Escreva-me uma carta também.
L Sophia has a pen pal in Italy.|A Sophia tem um amigo por correspondência na Itália.
L Send her a message. We stay in contact.|Mande uma mensagem a ela. Nós mantemos contato.
L I miss my friends already.|Eu já sinto saudade dos meus amigos.
L Don’t worry. We keep in touch!|Não se preocupe. Nós mantemos contato!
H 0,1,2,3,5
Q What do they want to keep?|O que elas querem manter?|0|🤝 Touch|🤫 A secret|🐱 A cat
Q Who has a pen pal?|Quem tem um amigo por correspondência?|4|👵 Sophia|👩 Rose|👩‍🦳 Dorothy
Q What does Rose miss?|Do que a Rose sente saudade?|6|🧑‍🤝‍🧑 Her friends|🏠 Her house|🐶 Her dog
B keep|🤝|manter|in touch|Rose keeps in touch.|A Rose mantém contato.
B send|📤|enviar|an email|Dorothy sends an email.|A Dorothy envia um e-mail.
B write|✍️|escrever|a letter|Rose writes a letter.|A Rose escreve uma carta.
B stay|📞|ficar|in contact|They stay in contact.|Elas ficam em contato.
LAB tou|Em touch, ou soa â; em letter, e soa é.|Touch e teach têm sons diferentes.
W touch|TÂTCH|contato|ou = â|teach|TÍITCH
W letter|LÉ-ter|carta|e = é|later|LÊI-ter
W message|MÉ-sidj|mensagem|age = idj|massage|ma-SÁJ
G 0|touch|tough|teach
G 1|Send|Sends|Sending
G 3|Write|Writes|Wrote
G 4|stay|stays|staying
X 👋|Take care.|Se cuide.|Despede-se com carinho.|Take care, Dorothy.|Se cuide, Dorothy.
X 😢|Miss you!|Sinto sua falta!|Diz que sente saudade.|Miss you! Write soon.|Sinto sua falta! Escreva logo.
X 👍|Of course.|Claro.|Aceita um pedido.|Of course. I write every week.|Claro. Eu escrevo toda semana.
X 👋|Goodbye!|Tchau!|Despede-se.|Goodbye! See you soon.|Tchau! Até logo.
"""))

N.append(parse("""
N 7910049
C DJ,Stephanie | polly,tommy | A DJ e a Stephanie combinam de se falar: mande uma linha, me ligue, mande uma mensagem.
F Full House | 📺 Série | 1987 | uma comédia americana sobre um pai viúvo, Danny, o cunhado Jesse e o amigo Joey, que criam juntos as filhas DJ, Stephanie e Michelle. | combinar contato: drop me a line e give me a call | lobby1 | 🏠,📞,👭
V ✍️|line|bilhete|LÁIN
V 📞|call|ligação|KÓL
V 🔢|number|número|NÂM-ber
V 💬|text|mensagem de texto|TÉKST
V ⏰|today|hoje|tu-DÊI
V 📅|week|semana|UÍIK
L Stephanie, drop me a line.|Stephanie, mande-me uma linha.
L Okay. Give me a call.|Certo. Me dê uma ligação.
L Here is my number.|Aqui está o meu número.
L Send me a text.|Mande-me uma mensagem de texto.
L Call me today.|Ligue para mim hoje.
L I call you next week.|Eu ligo para você na semana que vem.
L Write to me too.|Escreva para mim também.
L Deal! See you soon.|Combinado! Até logo.
H 0,1,2,3,4
Q What does DJ say first?|O que a DJ diz primeiro?|0|✍️ Drop me a line|🏠 Go home|🍕 Eat now
Q What does DJ give?|O que a DJ dá?|2|🔢 Her number|📚 Her book|🎒 Her bag
Q When does Stephanie call?|Quando a Stephanie liga?|5|📅 Next week|⏪ Yesterday|🌙 Tonight
B drop|✉️|mandar|a line|DJ drops a line.|A DJ manda uma linha.
B give|📞|dar|a call|Stephanie gives a call.|A Stephanie liga.
B text|💬|mandar mensagem a|a friend|DJ texts a friend.|A DJ manda mensagem a uma amiga.
B call|📱|ligar|today|Stephanie calls today.|A Stephanie liga hoje.
LAB li|Em line, i soa ái; em call, a soa ó.|Line e lane têm sons diferentes.
W line|LÁIN|linha|i = ái|lane|LÊIN
W call|KÓL|ligar|a = ó|coal|KÔUL
W text|TÉKST|mensagem|e = é|test|TÉST
G 0|drop|drops|dropped
G 1|Give|Gives|Giving
G 2|my|me|mine
G 3|Send|Sends|Sending
X 🤝|Deal!|Combinado!|Fecha um acordo.|Deal! I call you.|Combinado! Eu ligo para você.
X 👋|See you soon.|Até logo.|Despede-se.|See you soon, DJ.|Até logo, DJ.
X 💬|Talk soon.|Falamos em breve.|Combina de falar.|Talk soon, Stephanie.|Falamos em breve, Stephanie.
X 👍|Okay.|Certo.|Concorda.|Okay. I send a text.|Certo. Eu mando uma mensagem.
"""))

N.append(parse("""
N 7910050
C Bugs,Daffy | tommy,tom | O Pernalonga e o Patolino se despedem com carinho: se cuide e até a próxima.
F Looney Tunes | 📺 Série animada | 1930 | uma série de desenhos animados clássicos da Warner, com personagens como Bugs Bunny e Daffy Duck, que sempre terminam com “That’s all, folks!”. | se despedir com carinho | hall | 🐰,🦆,🥕
V 💛|care|cuidado|KÉR
V 🛡️|safe|seguro|SÊIF
V 🤗|hug|abraço|HÂG
V ⏳|time|vez|TÁIM
V 🍵|tea|chá|TÍI
V 👋|wave|aceno|UÊIV
L Take care, Daffy.|Se cuide, Patolino.
L Stay safe, Bugs.|Fique seguro, Pernalonga.
L Give me a hug.|Me dê um abraço.
L Until next time!|Até a próxima!
L Have some tea first.|Tome um chá primeiro.
L Wave to the friends.|Acene para os amigos.
L That’s all, folks!|É tudo, pessoal!
L Take care, everybody.|Se cuidem, pessoal.
H 0,1,2,3,4
Q What does Bugs say first?|O que o Pernalonga diz primeiro?|0|💛 Take care|👋 Hello|🌙 Good night
Q What do they give?|O que eles dão?|2|🤗 A hug|🎁 A gift|✉️ A letter
Q What does Bugs offer?|O que o Pernalonga oferece?|4|🍵 Tea|🍰 Cake|💧 Water
B take|💛|tomar|care|Bugs takes care.|O Pernalonga se cuida.
B give|🤲|dar|a hug|Daffy gives a hug.|O Patolino dá um abraço.
B stay|🛡️|ficar|safe|They stay safe.|Eles ficam seguros.
B wave|👋|acenar|to the friends|Bugs waves to the friends.|O Pernalonga acena para os amigos.
LAB ca|Em care, are soa ér; em tea, ea soa íi.|Care e car têm sons diferentes.
W care|KÉR|cuidado|are = ér|car|KÁR
W safe|SÊIF|seguro|a = êi|save|SÊIV
W tea|TÍI|chá|ea = íi|tie|TÁI
G 0|Take|Takes|Taking
G 1|safe|save|safely
G 2|hug|hog|hung
G 3|next|last|near
X 👋|That’s all, folks!|É tudo, pessoal!|Despedida clássica.|That’s all, folks! Bye-bye.|É tudo, pessoal! Tchau, tchau.
X 👋|Goodbye!|Tchau!|Despede-se.|Goodbye, Bugs!|Tchau, Pernalonga!
X 👀|See you!|Até logo!|Despede-se.|See you, Daffy!|Até logo, Patolino!
X 🐰|Bye-bye!|Tchau, tchau!|Despede-se com alegria.|Bye-bye! Take care.|Tchau, tchau! Se cuide.
"""))

N.append(parse("""
N 80350
C Violetta,Alfredo | polly,tom | A Violetta e o Alfredo erguem as taças e brindam: Cheers to A1!
F La Traviata | 🎭 Ópera | 1853 | uma ópera de Giuseppe Verdi sobre Violetta e Alfredo, que se conhecem numa festa em Paris e cantam um famoso brinde. | fazer um brinde | cafe2 | 🥂,🌹,🎶
V 🥂|cheers|saúde (brinde)|TCHÍIRZ
V 📈|level|nível|LÉ-vol
V 🛤️|journey|jornada|DJÂR-ni
V 🧑‍🤝‍🧑|friends|amigos|FRÉNDZ
V 🏆|success|sucesso|sak-SÉS
V 🍷|toast|brinde|TÔUST
L Cheers, everyone!|Saúde, pessoal!
L Cheers to this level!|Um brinde a este nível!
L Here’s to the journey!|Um brinde à jornada!
L Here’s to our friends!|Um brinde aos nossos amigos!
L Cheers to success!|Um brinde ao sucesso!
L Raise your glass for the toast.|Levante a taça para o brinde.
L To A1 and to learning!|Ao A1 e ao aprendizado!
L We finish this level. Cheers!|Nós terminamos este nível. Saúde!
H 0,1,2,3,4
Q Who says Cheers first?|Quem diz Cheers primeiro?|0|👩 Violetta|👨 Alfredo|🙅 Nobody
Q What do they toast to?|A que eles brindam?|4|🏆 Success|💰 Money|🌧️ Rain
Q What do they finish?|O que eles terminam?|7|📈 This level|🎂 A cake|📖 A book
B end|🔚|acabar|this level|They end this level.|Eles acabam este nível.
B propose|🥂|propor|a toast|Violetta proposes a toast.|A Violetta propõe um brinde.
B raise|🥂|erguer|your glass|Alfredo raises his glass.|O Alfredo ergue a taça.
B celebrate|🎉|comemorar|success|They celebrate success.|Eles comemoram o sucesso.
LAB ch|Em cheers, ch soa tch; em journey, j soa dj.|Cheers e chairs têm sons diferentes.
W cheers|TCHÍIRZ|saúde|ch = tch|chairs|TCHÉRZ
W journey|DJÂR-ni|jornada|j = dj|tourney|TÓR-ni
W success|sak-SÉS|sucesso|cc = ks|excess|ik-SÉS
G 0|Cheers|Cheer|Cheering
G 1|to|at|of
G 3|friends|friend|friendly
G 4|success|succeed|successful
X 🎉|Congratulations!|Parabéns!|Parabeniza.|Congratulations on the new level!|Parabéns pelo nível novo!
X 👏|Well done!|Muito bem!|Elogia.|Well done, everyone!|Muito bem, pessoal!
X 🥂|To us!|A nós!|Brinda ao grupo.|To us and our friends!|A nós e aos nossos amigos!
X 🎭|Bravo!|Bravo!|Aplaude.|Bravo! What a toast!|Bravo! Que brinde!
"""))

N.append(parse("""
N 7080350
C Light,Mega | polly,tom | O Dr. Light tem orgulho do Mega Man: “I did it” e “We made it”.
F Mega Man | 🎮 Videogame | 1987 | um jogo da Capcom em que o robô azul Mega Man, criado pelo Dr. Light, enfrenta chefes e o malvado Dr. Wily fase após fase. | celebrar uma conquista | school | 🤖,🏆,🎮
V 🥰|proud|orgulhoso|PRÁUD
V 👾|boss|chefe (do jogo)|BÓS
V 👣|step|passo|STÉP
V 🔮|future|futuro|FIÚ-tcher
V 🏁|finish|terminar|FÍ-nix
V 🏅|medal|medalha|MÉ-dol
L Mega Man, I am proud of you.|Mega Man, eu tenho orgulho de você.
L I did it! I beat the boss.|Eu consegui! Eu venci o chefe.
L One step at a time.|Um passo de cada vez.
L We made it! The future is bright.|Nós conseguimos! O futuro é brilhante.
L Here is the last level. I finish it.|Aqui está a última fase. Eu termino.
L Here is your medal.|Aqui está a sua medalha.
L Thank you, Doctor!|Obrigado, Doutor!
L We made it! I am so happy.|Nós conseguimos! Eu estou tão feliz.
H 0,1,2,3,4
Q Who is proud?|Quem tem orgulho?|0|🧑‍🔬 Dr. Light|👾 The boss|🤖 Roll
Q What does Mega Man beat?|O que o Mega Man vence?|1|👾 The boss|🚗 A car|🚪 A door
Q What does Dr. Light give?|O que o Dr. Light dá?|5|🏅 A medal|🚗 A car|🔑 A key
B do|💪|fazer|it|Mega Man does it.|O Mega Man consegue.
B make|🎉|conseguir|it|They make it.|Eles conseguem.
B finish|🏁|terminar|the level|Mega Man finishes the level.|O Mega Man termina a fase.
B win|🏆|ganhar|a medal|He wins a medal.|Ele ganha uma medalha.
LAB pr|Em proud, ou soa áu; em boss, o soa ó.|Proud e prod têm sons diferentes.
W proud|PRÁUD|orgulhoso|ou = áu|prod|PRÓD
W boss|BÓS|chefe|o = ó|bus|BÂS
W medal|MÉ-dol|medalha|e = é|metal|MÉ-tol
G 0|of|for|at
G 1|did|do|done
G 3|made|make|makes
G 2|at|on|in
X 🎉|Congratulations!|Parabéns!|Parabeniza.|Congratulations, Mega Man!|Parabéns, Mega Man!
X 👏|Well done!|Muito bem!|Elogia.|Well done! The level is over.|Muito bem! A fase acabou.
X 🥳|Hooray!|Hurra!|Comemora.|Hooray! We made it.|Hurra! Nós conseguimos.
X 🙏|Thank you!|Obrigado!|Agradece.|Thank you, Doctor!|Obrigado, Doutor!
"""))
