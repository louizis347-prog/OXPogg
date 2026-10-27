# Reescrita dos episódios B1 141–172 (ver ovrb1.py).
from v3.ovrb1 import OVR, L

# ---------------------------------------------------------------- 141–145
OVR[82090] = dict(fill=[['I will read the contract tonight.', 'Vou ler o contrato esta noite.'], ['Read every line, including the small print.', 'Leia cada linha, inclusive as letras miúdas.'],
                        ['Then we sign tomorrow morning.', 'Então assinamos amanhã de manhã.'], ['Fine. See you at nine.', 'Combinado. Até as nove.']])

OVR[7082090] = dict(
    names=('Wizard', 'Dorothy'), ids=['wizardoz', 'dorothy'], rs='hall',
    hot4=('🧹', 'broomstick', 'vassoura', 'Bring me the broomstick.', 'Traga-me a vassoura.'),
    cv='Na Cidade das Esmeraldas, Dorothy e o Mágico negociam uma troca.',
    obra=('Supposing I help, what do I get?', 'Supondo que eu ajude, o que ganho?'),
    vocab=[('🧹', 'broomstick', 'vassoura', 'Soa como “BRÚM-stik”.'), ('💚', 'emerald', 'esmeralda', 'Soa como “É-me-rald”.'), ('👠', 'slippers', 'sapatinhos', 'Soa como “SLÍ-perz”.'),
           ('🌪️', 'tornado', 'tornado', 'Soa como “tor-NÊI-dou”.'), ('🎭', 'curtain', 'cortina', 'Soa como “KÉR-ten”.'), ('🧙‍♀️', 'witch', 'bruxa', 'Soa como “UÍTCH”.')],
    verbs=[('ask', '🙋', 'pedir', 'In return, I ask for a favour.', 'In return, I ask a favour.', 'I asked.', 'Pedi.', 'ask **for**.'),
           ('give', '🎁', 'dar', 'I give you my thanks.', 'I give to you my thanks.', 'I gave.', 'Dei.', 'give → **gave**.'),
           ('bring', '🧹', 'trazer', 'Bring me the broomstick.', 'Bring to me the broomstick.', 'I brought it.', 'Trouxe.', 'bring → **brought**.'),
           ('exchange', '🔁', 'trocar', 'We exchange favours.', 'We exchange of favours.', 'We exchanged.', 'Trocamos.', 'exchange **+ objeto**.')],
    lines=[['Dorothy', 'Can you help me go home?', 'Pode me ajudar a voltar para casa?'],
           ['Wizard', 'Supposing I help, what do I get?', 'Supondo que eu ajude, o que ganho?'],
           ['Dorothy', 'In exchange for help, I give you my thanks.', 'Em troca de ajuda, dou meus agradecimentos.'],
           ['Wizard', 'In return, I ask for a favour too.', 'Em troca, também peço um favor.'],
           ['Dorothy', 'What favour?', 'Que favor?'],
           ['Wizard', 'Bring me the witch’s broomstick.', 'Traga-me a vassoura da bruxa.'],
           ['Dorothy', 'If you agree to send me home, I bring it.', 'Se você concordar em me mandar para casa, eu trago.'],
           ['Wizard', 'We have a deal.', 'Temos um acordo.']],
    quiz=[('What does Dorothy offer?', 'O que Dorothy oferece?', [('🙏', 'Her thanks'), ('💰', 'Money'), ('🍕', 'Pizza')], 0, 2, 'Dorothy diz: “I give you my thanks.”'),
          ('What favour does the Wizard ask for?', 'Que favor o Mágico pede?', [('🧹', 'The witch’s broomstick'), ('📚', 'A book'), ('🍽️', 'Dinner')], 0, 5, 'Wizard diz: “Bring me the witch’s broomstick.”'),
          ('How does it end?', 'Como termina?', [('🤝', 'They have a deal'), ('😡', 'They argue'), ('🏃', 'She runs')], 0, 7, 'Wizard diz: “We have a deal.”')],
    fill=[['Do you accept my terms, little girl?', 'Você aceita meus termos, menina?'], ['I do, if I can bring my friends.', 'Aceito, se eu puder levar meus amigos.'],
          ['Then go, and return before sunset.', 'Então vá, e volte antes do pôr do sol.'], ['We will. Thank you, sir.', 'Voltaremos. Obrigada, senhor.']])

OVR[82091] = dict(fill=[['Which year would you visit first?', 'Qual ano você visitaria primeiro?'], ['Maybe one hundred years ago.', 'Talvez cem anos atrás.'],
                        ['What if you could not come back?', 'E se você não pudesse voltar?'], ['Then I would write a book there.', 'Então eu escreveria um livro lá.']])

OVR[7082091] = dict(
    names=('Guinevere', 'Arthur'), ids=['polly', 'arthur'], rs='hall',
    cv='No castelo de Camelot, Guinevere e Arthur imaginam uma história diferente.',
    obra=('What if the king had died?', 'E se o rei tivesse morrido?'),
    vocab=[('🏰', 'kingdom', 'reino', 'Soa como “KÍNG-dom”.'), ('🛡️', 'knight', 'cavaleiro', 'Soa como “NÁIT”.'), ('⚔️', 'battle', 'batalha', 'Soa como “BÉ-tol”.'),
           ('👑', 'throne', 'trono', 'Soa como “THRÔUN”.'), ('⭕', 'round table', 'távola redonda', 'Soa como “RÁUND TÊI-bol”.'), ('📜', 'legend', 'lenda', 'Soa como “LÉ-djend”.')],
    hot4=('🏰', 'kingdom', 'reino', 'The kingdom would have fallen.', 'O reino teria caído.'),
    lines=[['Arthur', 'What would have happened if they had not won?', 'O que teria acontecido se eles não tivessem vencido?'],
           ['Guinevere', 'The outcome would have been different.', 'O resultado teria sido diferente.'],
           ['Arthur', 'What if the king had died?', 'E se o rei tivesse morrido?'],
           ['Guinevere', 'Then the kingdom would have changed.', 'Então o reino teria mudado.'],
           ['Arthur', 'If he had not left, nothing would have changed.', 'Se ele não tivesse partido, nada teria mudado.'],
           ['Guinevere', 'A legend is fun to imagine.', 'Uma lenda é divertida de imaginar.'],
           ['Arthur', 'Is it possible to know?', 'É possível saber?'],
           ['Guinevere', 'No, only imagine.', 'Não, só imaginar.']],
    quiz=[('What would the outcome have been?', 'Qual teria sido o resultado?', [('🔀', 'Different'), ('🔁', 'The same'), ('❌', 'Unknown')], 0, 1, 'Guinevere diz: “would have been different.”'),
          ('What if the king had died?', 'E se o rei tivesse morrido?', [('🏰', 'The kingdom would have changed'), ('😴', 'Nothing'), ('🎉', 'A party')], 0, 3, 'Guinevere diz: “the kingdom would have changed.”'),
          ('Is it possible to know?', 'É possível saber?', [('🙅', 'No, only imagine'), ('✅', 'Yes'), ('🤷', 'Maybe')], 0, 7, 'Guinevere diz: “No, only imagine.”')],
    fill=[['The knights are waiting at the round table.', 'Os cavaleiros esperam na távola redonda.'], ['Tell them I will come soon.', 'Diga que irei em breve.'],
          ['They want to hear another legend.', 'Eles querem ouvir outra lenda.'], ['Then I will tell them the true one.', 'Então contarei a verdadeira.']])

OVR[82092] = dict(fill=[['The footprints stop at the river.', 'As pegadas param no rio.'], ['Then the thief crossed by boat.', 'Então o ladrão atravessou de barco.'],
                        ['Check the pier for a ticket.', 'Confira o cais atrás de um bilhete.'], ['I will go there at once.', 'Vou lá agora mesmo.']])

# ---------------------------------------------------------------- 146–150
OVR[7082092] = dict(
    names=('Mustard', 'Scarlet'), ids=['tom', 'polly'], rs='hall',
    cv='Numa mansão, Mustard e Scarlet combinam as regras de um jogo de detetive.',
    obra=('If you find a clue, you can keep it.', 'Se você achar uma pista, pode ficar com ela.'),
    vocab=[('🕯️', 'candlestick', 'castiçal', 'Soa como “KÉN-dol-stik”.'), ('🔪', 'weapon', 'arma', 'Soa como “UÉ-pon”.'), ('🏰', 'mansion', 'mansão', 'Soa como “MÉN-shon”.'),
           ('🎲', 'dice', 'dados', 'Soa como “DÁIS”.'), ('🕵️', 'suspect', 'suspeito', 'Soa como “SÂS-pekt”.'), ('🤵', 'butler', 'mordomo', 'Soa como “BÂT-ler”.')],
    hot4=('🕯️', 'candlestick', 'castiçal', 'You can keep the candlestick.', 'Você pode ficar com o castiçal.'),
    verbs=[('keep', '🔍', 'ficar com', 'You can keep it.', 'You can to keep it.', 'I kept it.', 'Fiquei com ele.', 'can + **keep**.'),
           ('rain', '🌧️', 'chover', 'If it rains, we may stay.', 'If it will rain, we may stay.', 'It rained.', 'Choveu.', 'if + **rains**.'),
           ('rest', '😴', 'descansar', 'You should rest.', 'You should to rest.', 'I rested.', 'Descansei.', 'should + **rest**.'),
           ('stop', '🛑', 'parar', 'You must stop.', 'You must to stop.', 'I stopped.', 'Parei.', 'must + **stop**.')],
    fill=[['Roll the dice and move your piece.', 'Role os dados e mova sua peça.'], ['I land in the library. May I guess?', 'Caí na biblioteca. Posso dar um palpite?'],
          ['Yes, if you name the weapon too.', 'Sim, se disser a arma também.'], ['The candlestick, then. In the hall.', 'O castiçal, então. No salão.']])

OVR[930020] = dict(fill=[['Is the roof in good condition?', 'O telhado está em bom estado?'], ['The survey says it needs repairs.', 'A vistoria diz que precisa de reparos.'],
                         ['Then I want a second quote.', 'Então quero um segundo orçamento.'], ['Fair. I will call the builder.', 'Justo. Ligo para o construtor.']])

OVR[7930020] = dict(
    names=('Goldilocks', 'Baby Bear'), ids=['polly', 'bear'], rs='living',
    cv='Na casinha da floresta, Goldilocks e o Ursinho relaxam depois do almoço.',
    obra=('Let us have a chat.', 'Vamos bater um papo.'),
    vocab=[('🍲', 'porridge', 'mingau', 'Soa como “PÓ-ridj”.'), ('🪑', 'chair', 'cadeira', 'Soa como “TCHÉR”.'), ('🛏️', 'bed', 'cama', 'Soa como “BÉD”.'),
           ('🏡', 'cottage', 'casinha', 'Soa como “KÓ-tidj”.'), ('🌲', 'forest', 'floresta', 'Soa como “FÓ-rist”.'), ('🥣', 'bowl', 'tigela', 'Soa como “BÔUL”.')],
    verbs=[('try', '🧩', 'tentar', 'Try this puzzle!', 'Try to this puzzle!', 'I tried.', 'Tentei.', 'try **+ objeto**.'),
           ('sleep', '😴', 'dormir', 'I need to sleep.', 'I need to sleeping.', 'I slept.', 'Dormi.', 'need to + **sleep**.'),
           ('chat', '💬', 'bater papo', 'We chat after lunch.', 'We chats after lunch.', 'We chatted.', 'Batemos papo.', 'we **chat**.'),
           ('rest', '☕', 'descansar', 'Let us rest.', 'Let us to rest.', 'I rested.', 'Descansei.', 'let us **rest**.')],
    fill=[['Your porridge is delicious.', 'Seu mingau está delicioso.'], ['Thank you. There is more in the pot.', 'Obrigado. Tem mais na panela.'],
          ['Then I will take another bowl.', 'Então pego outra tigela.'], ['Slowly, or you will need another nap.', 'Devagar, ou vai precisar de outra soneca.']])

OVR[930021] = dict(fill=[['Would you like some tea?', 'Aceita um chá?'], ['Yes. Thank you for staying with me.', 'Sim. Obrigada por ficar comigo.'],
                         ['The family is welcome to call anytime.', 'A família pode ligar a qualquer hora.'], ['That means a lot to us.', 'Isso significa muito para nós.']])

OVR[7930021] = dict(
    names=('Dumbledore', 'Harry'), ids=['dumbledore', 'harry'], rs='hall',
    cv='No castelo de Hogwarts, Dumbledore acolhe Harry num momento difícil.',
    obra=('I am here for you. Take your time.', 'Estou aqui por você. Leve o tempo que precisar.'),
    vocab=[('🕯️', 'candle', 'vela', 'Soa como “KÉN-dol”.'), ('🧪', 'potion', 'poção', 'Soa como “PÔU-shon”.'), ('📖', 'spell', 'feitiço', 'Soa como “SPÉL”.'),
           ('🧙', 'headmaster', 'diretor da escola', 'Soa como “HÉD-más-ter”.'), ('🫂', 'friend', 'amigo', 'Soa como “FRÉND”.'), ('🪄', 'wand', 'varinha', 'Soa como “UÓND”.')],
    hot4=('🕯️', 'candle', 'vela', 'I will light a candle for you.', 'Vou acender uma vela por você.'),
    verbs=[('take', '⏳', 'levar (tempo)', 'Take your time.', 'Take your times.', 'I took it.', 'Levei.', 'take → **took**.'),
           ('get', '📈', 'ficar', 'It will get better.', 'It will gets better.', 'It got better.', 'Melhorou.', 'will + **get**.'),
           ('listen', '👂', 'ouvir', 'I will listen.', 'I will to listen.', 'I listened.', 'Ouvi.', 'will + **listen**.'),
           ('count', '🤝', 'contar com', 'You can count on me.', 'You can count in me.', 'I counted.', 'Contei.', 'count **on**.')],
    lines=[['Harry', 'I failed the test and I feel awful.', 'Reprovei na prova e me sinto péssimo.'],
           ['Dumbledore', 'I am here for you.', 'Estou aqui por você.'],
           ['Harry', 'I do not know what to do.', 'Não sei o que fazer.'],
           ['Dumbledore', 'Take your time. I will listen.', 'Leve o tempo que precisar. Eu ouço você.'],
           ['Harry', 'It is hard.', 'É difícil.'],
           ['Dumbledore', 'It will get better. You are not alone.', 'Vai melhorar. Você não está sozinho.'],
           ['Harry', 'Thank you, Professor.', 'Obrigado, professor.'],
           ['Dumbledore', 'Anytime.', 'Sempre.']],
    quiz=[('What happened to Harry?', 'O que aconteceu com Harry?', [('📝', 'He failed the test'), ('🏥', 'He got sick'), ('✈️', 'He moved')], 0, 0, 'Harry diz: “I failed the test.”'),
          ('What does Dumbledore offer?', 'O que Dumbledore oferece?', [('👂', 'To listen'), ('💰', 'Money'), ('🍕', 'Pizza')], 0, 3, 'Dumbledore diz: “I will listen.”'),
          ('What does he tell Harry?', 'O que ele diz a Harry?', [('🫂', 'He is not alone'), ('😡', 'He is wrong'), ('🏃', 'To run')], 0, 5, 'Dumbledore diz: “You are not alone.”')],
    fill=[['Would you like some tea and a biscuit?', 'Aceita um chá e um biscoito?'], ['Yes, please. Thank you, Professor.', 'Sim, por favor. Obrigado, professor.'],
          ['Then sit by the fire and rest.', 'Então sente perto da lareira e descanse.'], ['I feel a little better already.', 'Já me sinto um pouco melhor.']])

# ---------------------------------------------------------------- 151–155
OVR[82098] = dict(fill=[['Would you like it gift wrapped?', 'Quer embrulhado para presente?'], ['Yes, and put it in a strong bag.', 'Sim, e coloque numa sacola resistente.'],
                        ['That will be a small extra charge.', 'Haverá uma pequena taxa extra.'], ['Fine. Here is my card.', 'Tudo bem. Aqui está meu cartão.']])

OVR[7082098] = dict(
    names=('Toula', 'Gus'), ids=['polly', 'tom'], rs='diner',
    cv='Num restaurante, Toula e Gus discutem o preço do buffet do casamento.',
    obra=('Could you lower the price?', 'Você poderia baixar o preço?'),
    vocab=[('💒', 'wedding', 'casamento', 'Soa como “UÉ-ding”.'), ('🍽️', 'caterer', 'bufê', 'Soa como “KÊI-te-rer”.'), ('🍖', 'lamb', 'cordeiro', 'Soa como “LÉM”.'),
           ('💐', 'bouquet', 'buquê', 'Soa como “bu-KÊI”.'), ('🎂', 'cake', 'bolo', 'Soa como “KÊIK”.'), ('🧑‍🤝‍🧑', 'guests', 'convidados', 'Soa como “GÉSTS”.')],
    hot4=('🎂', 'cake', 'bolo', 'Could you lower the price of the cake?', 'Poderia baixar o preço do bolo?'),
    lines=[['Gus', 'The catering costs two hundred.', 'O buffet custa duzentos.'],
           ['Toula', 'Could you lower the price?', 'Você poderia baixar o preço?'],
           ['Gus', 'Is it a bigger group?', 'É um grupo maior?'],
           ['Toula', 'Yes, the whole family comes. Can you do better?', 'Sim, a família toda vem. Você pode melhorar?'],
           ['Gus', 'One hundred and eighty. That is my final offer.', 'Cento e oitenta. Esta é minha oferta final.'],
           ['Toula', 'Hmm. The wedding is big, though.', 'Hmm. O casamento é grande, mesmo assim.'],
           ['Gus', 'Take it or leave it.', 'É pegar ou largar.'],
           ['Toula', 'I take it.', 'Eu pego.']],
    quiz=[('How much was the first price?', 'Quanto era o primeiro preço?', [('2️⃣', 'Two hundred'), ('1️⃣', 'One hundred'), ('3️⃣', 'Three hundred')], 0, 0, 'Gus diz: “two hundred.”'),
          ('What is his final offer?', 'Qual é a oferta final dele?', [('8️⃣', 'One hundred and eighty'), ('2️⃣', 'Two hundred'), ('1️⃣', 'One hundred')], 0, 4, 'Gus diz: “One hundred and eighty.”'),
          ('What does she decide?', 'O que ela decide?', [('✅', 'She takes it'), ('🚫', 'She leaves it'), ('🤷', 'She waits')], 0, 7, 'Toula diz: “I take it.”')],
    fill=[['Will the cake be ready on Friday?', 'O bolo estará pronto na sexta?'], ['Yes, with white flowers on top.', 'Sim, com flores brancas em cima.'],
          ['And a table for the guests, please.', 'E uma mesa para os convidados, por favor.'], ['Everything is arranged.', 'Está tudo combinado.']])

OVR[82099] = dict(fill=[['The power may go out tonight.', 'A energia pode cair esta noite.'], ['Then the fence will not work.', 'Então a cerca não vai funcionar.'],
                        ['Stay inside the car until morning.', 'Fique dentro do carro até de manhã.'], ['I will not move an inch.', 'Não me mexo um centímetro.']])

OVR[7082099] = dict(
    names=('Marion', 'Indy'), ids=['polly', 'tom'], rs='street',
    cv='Numa estrada de aventura, Marion e Indy se protegem do perigo.',
    obra=('Watch out! A car is coming.', 'Cuidado! Vem um carro.'),
    vocab=[('🐍', 'snake', 'cobra', 'Soa como “SNÊIK”.'), ('🛕', 'temple', 'templo', 'Soa como “TÉM-pol”.'), ('🪤', 'trap', 'armadilha', 'Soa como “TRÉP”.'),
           ('🤠', 'whip', 'chicote', 'Soa como “UÍP”.'), ('🪨', 'boulder', 'pedregulho', 'Soa como “BÔUL-der”.'), ('⛰️', 'cliff', 'penhasco', 'Soa como “KLÍF”.')],
    hot4=('🐍', 'snake', 'cobra', 'Watch out for the snake!', 'Cuidado com a cobra!'),
    fill=[['Hold the rope and do not look down.', 'Segure a corda e não olhe para baixo.'], ['The cliff is higher than I thought.', 'O penhasco é mais alto do que pensei.'],
          ['Mind the loose stones on the left.', 'Cuidado com as pedras soltas à esquerda.'], ['I see them. Keep going.', 'Estou vendo. Continue.']])

OVR[82101] = dict(fill=[['The muddy shoes belong to the gardener.', 'Os sapatos sujos são do jardineiro.'], ['Then he was in the garden at night.', 'Então ele esteve no jardim à noite.'],
                        ['Ask him about the broken window.', 'Pergunte a ele sobre a janela quebrada.'], ['I will do it first thing.', 'Faço isso logo cedo.']])

# ---------------------------------------------------------------- 156–160
OVR[7082101] = dict(
    names=('Inspector', 'Miss Marple'), ids=['tom', 'mrs'], rs='hall',
    cv='No saguão de uma casa de campo, o inspetor e Miss Marple investigam o desaparecimento de um vaso.',
    obra=('The vase is missing!', 'O vaso sumiu!'),
    vocab=[('🏺', 'vase', 'vaso', 'Soa como “VÊIZ”.'), ('🌿', 'gardener', 'jardineiro', 'Soa como “GÁR-dner”.'), ('🧹', 'maid', 'empregada', 'Soa como “MÊID”.'),
           ('👞', 'muddy', 'enlameado', 'Soa como “MÂ-di”.'), ('🔒', 'lock', 'trancar', 'Soa como “LÓK”.'), ('🏘️', 'vicarage', 'casa paroquial', 'Soa como “VÍ-ke-ridj”.')],
    hot4=('🏺', 'vase', 'vaso', 'The vase is missing.', 'O vaso sumiu.'),
    verbs=[('leave', '🚪', 'sair', 'He must have left.', 'He must have leave.', 'He left.', 'Ele saiu.', 'must have + **left**.'),
           ('see', '👀', 'ver', 'She cannot have seen it.', 'She cannot have see it.', 'She saw it.', 'Ela viu.', 'cannot have + **seen**.'),
           ('forget', '🧠', 'esquecer', 'They might have forgotten.', 'They might have forget.', 'They forgot.', 'Esqueceram.', 'might have + **forgotten**.'),
           ('lock', '🔒', 'trancar', 'She locked the door.', 'She lock the door.', 'She has locked it.', 'Ela trancou.', 'lock → **locked**.')],
    lab=L('mg2', 'Laboratório de sons: maid, seen e forgotten', 'ai soa êi; ee soa í longo; o soa ó.', 'Em maid, o ai soa êi.',
          [('maid', 'MÊID', 'empregada', 'ai = êi', 'mad', 'MÉD'), ('seen', 'SÍIN', 'visto', 'ee = í longo', 'sin', 'SÍN'), ('forgotten', 'for-GÓ-ten', 'esquecido', 'o = ó', 'forgiven', 'for-GUÍ-ven')]),
    fill=[['Who cleans this room every morning?', 'Quem limpa este cômodo toda manhã?'], ['The maid, before nine o clock.', 'A empregada, antes das nove.'],
          ['Then ask her about the muddy shoes.', 'Então pergunte a ela sobre os sapatos enlameados.'], ['I will, as soon as she is back.', 'Perguntarei, assim que ela voltar.']])

OVR[930022] = dict(fill=[['The ship is leaning to one side.', 'O navio está inclinando para um lado.'], ['Then we must move to the upper deck.', 'Então precisamos subir ao convés superior.'],
                         ['Stay together and keep calm.', 'Fiquem juntos e mantenham a calma.'], ['I will find a lifejacket for you.', 'Vou achar um colete para você.']])

OVR[7930022] = dict(
    names=('Pi', 'Father'), ids=['tommy', 'tom'], rs='pier',
    cv='No convés, Pi e o pai se seguram à corda e esperam o resgate.',
    obra=('Hold on to the rope!', 'Agarre-se à corda!'),
    vocab=[('🐅', 'tiger', 'tigre', 'Soa como “TÁI-ger”.'), ('🌊', 'ocean', 'oceano', 'Soa como “ÔU-shon”.'), ('🛶', 'raft', 'jangada', 'Soa como “RÁFT”.'),
           ('🏝️', 'island', 'ilha', 'Soa como “ÁI-lend”.'), ('⛈️', 'storm', 'tempestade', 'Soa como “STÓRM”.'), ('🌟', 'survivor', 'sobrevivente', 'Soa como “sur-VÁI-vor”.')],
    hot4=('🌊', 'ocean', 'oceano', 'The ocean is huge.', 'O oceano é enorme.'),
    verbs=[('grab', '🪢', 'agarrar', 'Grab the rope!', 'Grab to the rope!', 'I grabbed it.', 'Agarrei.', 'grab **+ objeto**.'),
           ('rain', '🌧️', 'chover', 'The rain held off.', 'The rain held of.', 'It rained.', 'Choveu.', 'rain → **rained**.'),
           ('wait', '⏳', 'esperar', 'We wait for the rescue.', 'We wait to the rescue.', 'We waited.', 'Esperamos.', 'wait **for**.'),
           ('survive', '🌟', 'sobreviver', 'We can survive.', 'We can to survive.', 'We survived.', 'Sobrevivemos.', 'can + **survive**.')],
    lines=[['Father', 'Hold on to the rope!', 'Agarre-se à corda!'],
           ['Pi', 'I am holding on to it.', 'Estou agarrado a ela.'],
           ['Father', 'The rain held off, luckily.', 'A chuva deu uma trégua, por sorte.'],
           ['Pi', 'Does the rescue plan hold together?', 'O plano de resgate se sustenta?'],
           ['Father', 'Yes. The captain holds down the radio.', 'Sim. O capitão cuida do rádio.'],
           ['Pi', 'And the lifeboat?', 'E o bote salva-vidas?'],
           ['Father', 'It is ready.', 'Está pronto.'],
           ['Pi', 'Then let us go.', 'Então vamos.']],
    quiz=[('What must Pi hold on to?', 'Em que Pi deve se segurar?', [('🪢', 'The rope'), ('🚣', 'The boat'), ('🛟', 'The buoy')], 0, 0, 'Father diz: “Hold on to the rope!”'),
          ('What held off?', 'O que deu trégua?', [('🌧️', 'The rain'), ('💨', 'The wind'), ('🌊', 'The waves')], 0, 2, 'Father diz: “The rain held off.”'),
          ('Is the lifeboat ready?', 'O bote está pronto?', [('✅', 'Yes'), ('❌', 'No'), ('🤷', 'Maybe')], 0, 6, 'Father diz: “It is ready.”')],
    fill=[['The storm is getting stronger.', 'A tempestade está ficando mais forte.'], ['Then we must hold together.', 'Então precisamos nos manter unidos.'],
          ['I see a light on the horizon.', 'Vejo uma luz no horizonte.'], ['Keep the raft steady.', 'Mantenha a jangada firme.']])

OVR[82106] = dict(fill=[['Is the form really optional?', 'O formulário é mesmo opcional?'], ['Yes. You do not have to fill it in.', 'Sim. Você não precisa preenchê-lo.'],
                        ['Then I will keep my weekend free.', 'Então deixo meu fim de semana livre.'], ['Enjoy it. You have earned it.', 'Aproveite. Você mereceu.']])

OVR[7082106] = dict(
    names=('Charlie', 'Wonka'), ids=['tommy', 'willywonka'], rs='hall',
    cv='Na fábrica, Charlie e Wonka falam das regras do corredor.',
    obra=('You must not run in the hall.', 'É proibido correr no corredor.'),
    vocab=[('🏭', 'factory', 'fábrica', 'Soa como “FÉK-to-ri”.'), ('🍬', 'candy', 'doce', 'Soa como “KÉN-di”.'), ('🛗', 'lift', 'elevador', 'Soa como “LÍFT”.'),
           ('📏', 'rule', 'regra', 'Soa como “RÚL”.'), ('🌳', 'garden', 'jardim', 'Soa como “GÁR-den”.'), ('🔔', 'bell', 'sino', 'Soa como “BÉL”.')],
    hot4=('🏭', 'factory', 'fábrica', 'The hall of the factory is off limits.', 'O corredor da fábrica é proibido.'),
    verbs=[('walk', '🚶', 'andar', 'You must walk in the hall.', 'You must to walk in the hall.', 'I walked.', 'Andei.', 'must + **walk**.'),
           ('ask', '🙋', 'perguntar', 'Can I ask something?', 'Can I ask to something?', 'I asked.', 'Perguntei.', 'ask **+ objeto**.'),
           ('ring', '🔔', 'tocar', 'The bell rang.', 'The bell ringed.', 'It rings.', 'Toca.', 'ring → **rang**.'),
           ('waste', '🗑️', 'desperdiçar', 'Do not waste time.', 'Do not wasting time.', 'I wasted it.', 'Desperdicei.', 'do not + **waste**.')],
    lines=[['Charlie', 'Can I run in the hall?', 'Posso correr no corredor?'],
           ['Wonka', 'No. You must not run in the hall.', 'Não. É proibido correr no corredor.'],
           ['Charlie', 'And in the garden?', 'E no jardim?'],
           ['Wonka', 'You do not have to run there. It is optional.', 'Lá você não é obrigado a correr. É opcional.'],
           ['Charlie', 'Should I run to the lift now?', 'Devo correr para o elevador agora?'],
           ['Wonka', 'There is no point in running; the bell rang.', 'Não adianta correr; o sino tocou.'],
           ['Charlie', 'It is not worth the trouble, then.', 'Então não vale o trabalho.'],
           ['Wonka', 'Exactly. Have some candy.', 'Exato. Aceite um doce.']],
    quiz=[('Can he run in the hall?', 'Ele pode correr no corredor?', [('🚫', 'No, it is forbidden'), ('✅', 'Yes'), ('🤷', 'Maybe')], 0, 1, 'Wonka diz: “You must not run in the hall.”'),
          ('Is running in the garden required?', 'Correr no jardim é obrigatório?', [('😌', 'No, it is optional'), ('✅', 'Yes'), ('🚫', 'Forbidden')], 0, 3, 'Wonka diz: “It is optional.”'),
          ('Why is there no point in running?', 'Por que não adianta correr?', [('🔔', 'The bell rang'), ('🌧️', 'It rains'), ('😴', 'He is sleepy')], 0, 5, 'Wonka diz: “the bell rang.”')],
    fill=[['May I taste the new candy?', 'Posso provar o doce novo?'], ['You may, but only one piece.', 'Pode, mas só um pedaço.'],
          ['Do I have to ask for more?', 'Preciso pedir mais?'], ['No, you do not. They will find you.', 'Não precisa. Eles vão achar você.']])

# ---------------------------------------------------------------- 161–166
OVR[930023] = dict(fill=[['I tried a new recipe last night.', 'Testei uma receita nova ontem à noite.'], ['How did it turn out?', 'Como ficou?'],
                         ['Delicious. I will post it today.', 'Deliciosa. Vou postar hoje.'], ['Send me the link when it is up.', 'Me mande o link quando estiver no ar.']])

OVR[7930023] = dict(
    names=('Serena', 'Nate'), ids=['polly', 'tom'], rs='office',
    cv='Em Manhattan, Serena e Nate acompanham o crescimento de um blog.',
    obra=('And the blog? It is picking up speed.', 'E o blog? Está ganhando velocidade.'),
    vocab=[('👗', 'fashion', 'moda', 'Soa como “FÉ-shon”.'), ('🏙️', 'skyline', 'paisagem urbana', 'Soa como “SKÁI-láin”.'), ('🎉', 'party', 'festa', 'Soa como “PÁR-ti”.'),
           ('👥', 'follower', 'seguidor', 'Soa como “FÓ-lo-uer”.'), ('🎓', 'school', 'escola', 'Soa como “SKÚL”.'), ('🤫', 'rumour', 'boato', 'Soa como “RÚ-mor”.')],
    hot4=('👥', 'follower', 'seguidor', 'We have a new follower.', 'Temos um novo seguidor.'),
    verbs=[('improve', '📈', 'melhorar', 'We improve every day.', 'We improves every day.', 'We improved.', 'Melhoramos.', 'we **improve**.'),
           ('grow', '🌱', 'crescer', 'Step by step, we grow.', 'Step by step, we growing.', 'It grew.', 'Cresceu.', 'grow → **grew**.'),
           ('post', '✍️', 'postar', 'We post every Monday.', 'We posts every Monday.', 'We posted.', 'Postamos.', 'we **post**.'),
           ('pick', '💨', 'pegar', 'The blog picks up speed.', 'The blog pick up speed.', 'It picked up.', 'Ganhou.', 'pick up → **picked up**.')],
    fill=[['Our blog has new readers today.', 'Nosso blog tem leitores novos hoje.'], ['Then post again before the party.', 'Então poste de novo antes da festa.'],
          ['I will write it tonight.', 'Escrevo hoje à noite.'], ['Keep the tone light and fun.', 'Mantenha o tom leve e divertido.']])

OVR[82108] = dict(fill=[['Could you bring the tea to the library?', 'Poderia levar o chá à biblioteca?'], ['Certainly, sir. At what time?', 'Certamente, senhor. A que horas?'],
                        ['Half past four, if it is not too much trouble.', 'Às quatro e meia, se não for muito trabalho.'], ['Not at all. It will be ready.', 'De jeito nenhum. Estará pronto.']])

OVR[7082108] = dict(
    names=('Elizabeth', 'Darcy'), ids=['polly', 'tom'], rs='living',
    cv='Numa sala de visitas, Elizabeth e Darcy trocam pedidos formais.',
    obra=('Good morning. May I come in?', 'Bom dia. Posso entrar?'),
    vocab=[('✉️', 'letter', 'carta', 'Soa como “LÉ-ter”.'), ('🏡', 'estate', 'propriedade', 'Soa como “is-TÊIT”.'), ('🎩', 'manners', 'boas maneiras', 'Soa como “MÉ-nerz”.'),
           ('👒', 'bonnet', 'chapéu de dama', 'Soa como “BÓ-nit”.'), ('💍', 'proposal', 'pedido de casamento', 'Soa como “pro-PÔU-zal”.'), ('🐎', 'carriage', 'carruagem', 'Soa como “KÉ-ridj”.')],
    hot4=('✉️', 'letter', 'carta', 'Would you kindly read this letter?', 'Faria a gentileza de ler esta carta?'),
    verbs=[('come', '🚪', 'entrar', 'May I come in?', 'May I to come in?', 'He came.', 'Ele veio.', 'may I + **come**.'),
           ('sit', '🪑', 'sentar', 'Do you mind if I sit here?', 'Do you mind if I sitting here?', 'I sat.', 'Sentei.', 'sit → **sat**.'),
           ('help', '🤝', 'ajudar', 'I would be grateful if you could help.', 'I would be grateful if you can help.', 'I helped.', 'Ajudei.', 'if you **could** help.'),
           ('read', '✉️', 'ler', 'Would you kindly read this letter?', 'Would you kindly to read this letter?', 'I read it.', 'Eu li.', 'would you kindly + **read**?')],
    lines=[['Elizabeth', 'Good morning. May I come in?', 'Bom dia. Posso entrar?'],
           ['Darcy', 'Of course. Come in, Miss Bennet.', 'Claro. Entre, Miss Bennet.'],
           ['Elizabeth', 'Do you mind if I sit here?', 'Você se importa se eu sentar aqui?'],
           ['Darcy', 'Not at all.', 'De jeito nenhum.'],
           ['Elizabeth', 'I would be grateful if you could help me.', 'Eu agradeceria se você pudesse me ajudar.'],
           ['Darcy', 'Certainly. Would you kindly read this letter?', 'Certamente. Faria a gentileza de ler esta carta?'],
           ['Elizabeth', 'Of course.', 'Claro.'],
           ['Darcy', 'Thank you.', 'Obrigado.']],
    quiz=[('What does she ask first?', 'O que ela pergunta primeiro?', [('🚪', 'May I come in?'), ('🪑', 'May I sit?'), ('🍽️', 'May I eat?')], 0, 0, 'Elizabeth diz: “May I come in?”'),
          ('What does she ask about sitting?', 'O que ela pergunta sobre sentar?', [('🪑', 'Do you mind if I sit here?'), ('📞', 'Can I call?'), ('🍕', 'Can I eat?')], 0, 2, 'Elizabeth diz: “Do you mind if I sit here?”'),
          ('What does he ask her to read?', 'O que ele pede para ela ler?', [('✉️', 'A letter'), ('🧩', 'A puzzle'), ('📖', 'A book')], 0, 5, 'Darcy diz: “read this letter.”')],
    fill=[['Your estate is very beautiful.', 'Sua propriedade é muito bonita.'], ['Thank you. The garden is my pride.', 'Obrigado. O jardim é meu orgulho.'],
          ['May I walk there tomorrow?', 'Posso passear lá amanhã?'], ['By all means. I will send a carriage.', 'Com certeza. Mandarei uma carruagem.']])

OVR[82109] = dict(fill=[['Shall we share a taxi home?', 'Vamos dividir um táxi para casa?'], ['Let me pay for it this time.', 'Deixe-me pagar desta vez.'],
                        ['Only if I pay for lunch tomorrow.', 'Só se eu pagar o almoço amanhã.'], ['Deal. I will book a table.', 'Combinado. Reservo uma mesa.']])

OVR[7082109] = dict(
    names=('Mrs Brown', 'Paddington'), ids=['polly', 'bear'], rs='living',
    cv='Na sala da família Brown, Mrs Brown recebe Paddington com chá e sanduíches.',
    obra=('Welcome! Would you like some tea?', 'Bem-vindo! Você gostaria de chá?'),
    vocab=[('🥪', 'marmalade', 'geleia de laranja', 'Soa como “MÁR-ma-lêid”.'), ('🎩', 'hat', 'chapéu', 'Soa como “HÉT”.'), ('🚉', 'station', 'estação', 'Soa como “STÊI-shon”.'),
           ('🫖', 'teapot', 'bule', 'Soa como “TÍ-pót”.'), ('🧥', 'coat', 'casaco', 'Soa como “KÔUT”.'), ('👨‍👩‍👧', 'family', 'família', 'Soa como “FÉ-mi-li”.')],
    hot4=('🥪', 'marmalade', 'geleia de laranja', 'I will bring more marmalade.', 'Trago mais geleia de laranja.'),
    verbs=[('like', '🍵', 'gostar', 'Would you like some tea?', 'Would you liking some tea?', 'I liked it.', 'Gostei.', 'would you **like**?'),
           ('get', '🥪', 'trazer', 'Can I get you a sandwich?', 'Can I getting you a sandwich?', 'I got it.', 'Trouxe.', 'can I **get**?'),
           ('call', '🚕', 'chamar', 'Do you want me to call a taxi?', 'Do you want me to calling a taxi?', 'I called.', 'Chamei.', 'want me to **call**.'),
           ('offer', '🎁', 'oferecer', 'I offer you some tea.', 'I offer to you some tea.', 'I offered.', 'Ofereci.', 'offer **+ pessoa + coisa**.')],
    lines=[['Mrs Brown', 'Welcome! Would you like some tea?', 'Bem-vindo! Você gostaria de chá?'],
           ['Paddington', 'Yes, with marmalade, if you have it.', 'Sim, com geleia de laranja, se tiver.'],
           ['Mrs Brown', 'Can I get you a sandwich too?', 'Posso trazer um sanduíche também?'],
           ['Paddington', 'That is kind. Thank you for the offer.', 'Que gentil. Obrigado pela oferta.'],
           ['Mrs Brown', 'Do you want me to call a taxi later?', 'Quer que eu chame um táxi mais tarde?'],
           ['Paddington', 'Yes, the station is far.', 'Sim, a estação é longe.'],
           ['Mrs Brown', 'I will carry your bag.', 'Eu carrego sua mala.'],
           ['Paddington', 'You are too kind.', 'Você é muito gentil.']],
    quiz=[('What does she offer first?', 'O que ela oferece primeiro?', [('🍵', 'Tea'), ('🥤', 'Juice'), ('☕', 'Coffee')], 0, 0, 'Mrs Brown diz: “Would you like some tea?”'),
          ('What does she offer to call?', 'O que ela oferece chamar?', [('🚕', 'A taxi'), ('🚌', 'A bus'), ('🚑', 'An ambulance')], 0, 4, 'Mrs Brown diz: “call a taxi.”'),
          ('What does she carry?', 'O que ela carrega?', [('🧳', 'His bag'), ('📦', 'A box'), ('🪑', 'A chair')], 0, 6, 'Mrs Brown diz: “I will carry your bag.”')],
    fill=[['Your room is at the top of the stairs.', 'Seu quarto fica no alto da escada.'], ['It has a window and a little desk.', 'Tem uma janela e uma escrivaninha.'],
          ['Shall I bring you a warm blanket?', 'Quer que eu traga um cobertor quente?'], ['That would be lovely. Thank you.', 'Seria ótimo. Obrigado.']])

# ---------------------------------------------------------------- 167–172
OVR[82111] = dict(fill=[['Where are the old books kept now?', 'Onde ficam os livros antigos agora?'], ['In the cellar, under the stairs.', 'No porão, embaixo da escada.'],
                        ['Then no one will find them.', 'Então ninguém vai achá-los.'], ['Let us hope the guards do not either.', 'Vamos torcer para os guardas também não acharem.']])

OVR[7082111] = dict(
    names=('Quixote', 'Sancho'), ids=['quijote', 'sancho'], rs='hall',
    cv='Na biblioteca de Dom Quixote, Quixote e Sancho leem o regulamento.',
    obra=('Can we burn these old books?', 'Podemos queimar estes livros velhos?'),
    vocab=[('🌬️', 'windmill', 'moinho de vento', 'Soa como “UÍND-mil”.'), ('🧑‍🌾', 'squire', 'escudeiro', 'Soa como “SKUÁI-er”.'), ('🗡️', 'lance', 'lança', 'Soa como “LÁNS”.'),
           ('🌀', 'madness', 'loucura', 'Soa como “MÉD-nes”.'), ('🛡️', 'chivalry', 'cavalaria', 'Soa como “SHÍ-vel-ri”.'), ('🔥', 'bonfire', 'fogueira', 'Soa como “BÓN-fáir”.')],
    hot4=('🌬️', 'windmill', 'moinho de vento', 'No fighting windmills!', 'Proibido lutar contra moinhos!'),
    verbs=[('save', '📚', 'salvar', 'Save the books!', 'Save to the books!', 'I saved them.', 'Salvei.', 'save **+ objeto**.'),
           ('read', '📖', 'ler', 'Reading is permitted.', 'Reading are permitted.', 'I read it.', 'Eu li.', 'read **-ing** = sujeito.'),
           ('steal', '🚫', 'roubar', 'It is illegal to steal.', 'It is illegal steal.', 'He stole.', 'Ele roubou.', 'illegal **to** + base.'),
           ('break', '📏', 'quebrar', 'Do not break the rules.', 'Do not to break the rules.', 'He broke it.', 'Ele quebrou.', 'break → **broke**.')],
    lines=[['Sancho', 'Can we burn these old books?', 'Podemos queimar estes livros velhos?'],
           ['Quixote', 'No. You are not allowed to burn books.', 'Não. Você não pode queimar livros.'],
           ['Sancho', 'Why not?', 'Por que não?'],
           ['Quixote', 'It is against the rules. No fire inside.', 'É contra as regras. Proibido fogo aqui dentro.'],
           ['Sancho', 'Is reading permitted?', 'Ler é permitido?'],
           ['Quixote', 'Yes, reading is permitted.', 'Sim, ler é permitido.'],
           ['Sancho', 'And stealing?', 'E roubar?'],
           ['Quixote', 'It is illegal to steal, of course.', 'É ilegal roubar, claro.']],
    fill=[['Where do the old books go now?', 'Para onde vão os livros antigos agora?'], ['To the barn, away from the fire.', 'Para o celeiro, longe do fogo.'],
          ['No bonfire, then. Agreed?', 'Sem fogueira, então. Combinado?'], ['Agreed. I will carry them.', 'Combinado. Eu os carrego.']])

OVR[930024] = dict(fill=[['Is the new software working yet?', 'O software novo já está funcionando?'], ['Almost. We are testing the last step.', 'Quase. Estamos testando a última etapa.'],
                         ['Then I will check the numbers again.', 'Então vou conferir os números de novo.'], ['Thanks. Nobody checks like you.', 'Obrigado. Ninguém confere como você.']])

OVR[7930024] = dict(
    names=('Eduardo', 'Mark'), ids=['tommy', 'tom'], rs='bedroom',
    cv='Num quarto de Harvard, Eduardo e Mark tentam acompanhar o ritmo do trabalho.',
    obra=('You work so fast. I cannot keep up with you.', 'Você trabalha tão rápido. Não consigo acompanhar.'),
    vocab=[('🖥️', 'server', 'servidor', 'Soa como “SÉR-ver”.'), ('🌐', 'website', 'site', 'Soa como “UÉB-sáit”.'), ('👨‍💻', 'programmer', 'programador', 'Soa como “PRÔU-gra-mer”.'),
           ('🚀', 'launch', 'lançamento', 'Soa como “LÓNTCH”.'), ('🎓', 'campus', 'campus', 'Soa como “KÉM-pus”.'), ('🪪', 'profile', 'perfil', 'Soa como “PRÔU-fáil”.')],
    hot4=('🖥️', 'server', 'servidor', 'Keep away from the server.', 'Fique longe do servidor.'),
    verbs=[('follow', '📋', 'seguir', 'Follow the plan.', 'Follow to the plan.', 'I followed it.', 'Segui.', 'follow **+ objeto**.'),
           ('stay', '🚪', 'ficar', 'Stay away from the old files.', 'Stay out the old files.', 'I stayed.', 'Fiquei.', 'stay **away from**.'),
           ('enter', '🔑', 'entrar', 'Do not enter the server room.', 'Do not enter in the server room.', 'I entered.', 'Entrei.', 'enter **+ lugar**.'),
           ('code', '⌨️', 'programar', 'I code every night.', 'I codes every night.', 'I coded.', 'Programei.', 'I **code**.')],
    lines=[['Eduardo', 'You work so fast. I cannot keep up with you.', 'Você trabalha tão rápido. Não consigo acompanhar.'],
           ['Mark', 'Keep to the plan and you will be fine.', 'Siga o plano e ficará bem.'],
           ['Eduardo', 'What about the new software?', 'E o novo software?'],
           ['Mark', 'Keep away from the old files.', 'Fique longe dos arquivos antigos.'],
           ['Eduardo', 'Understood. I will back them up.', 'Entendido. Vou fazer cópia deles.'],
           ['Mark', 'Keep out of the server room.', 'Fique fora da sala do servidor.'],
           ['Eduardo', 'Of course. Who has the key?', 'Claro. Quem tem a chave?'],
           ['Mark', 'Only me. Back to work.', 'Só eu. De volta ao trabalho.']],
    fill=[['The site crashed again this morning.', 'O site caiu de novo esta manhã.'], ['Then restart the server and check the logs.', 'Então reinicie o servidor e confira os registros.'],
          ['I will keep to the checklist this time.', 'Vou seguir a lista desta vez.'], ['Do it fast. We launch tomorrow.', 'Faça rápido. Lançamos amanhã.']])

OVR[82113] = dict(fill=[['Will the road be open by Friday?', 'A estrada estará aberta até sexta?'], ['Probably, unless the storm returns.', 'Provavelmente, a menos que a tempestade volte.'],
                        ['Then we will definitely travel.', 'Então com certeza viajaremos.'], ['Pack warm clothes just in case.', 'Leve roupas quentes por precaução.']])

OVR[7082113] = dict(
    names=('Will', 'Edward'), ids=['tommy', 'tom'], rs='yard',
    cv='Numa varanda, Will e Edward debatem qual versão da história é verdadeira.',
    obra=('Who told the truth? I am not sure.', 'Quem disse a verdade? Não tenho certeza.'),
    vocab=[('🧌', 'giant', 'gigante', 'Soa como “DJÁI-ant”.'), ('📖', 'tale', 'conto', 'Soa como “TÊIL”.'), ('🗣️', 'storyteller', 'contador de histórias', 'Soa como “STÓ-ri-té-ler”.'),
           ('🐊', 'swamp', 'pântano', 'Soa como “SUÓMP”.'), ('⚖️', 'truth', 'verdade', 'Soa como “TRÚTH”.'), ('🎈', 'exaggerate', 'exagerar', 'Soa como “eg-ZÁ-dje-rêit”.')],
    hot4=('📖', 'tale', 'conto', 'That is a tall tale.', 'Isso é uma história exagerada.'),
    verbs=[('believe', '🤔', 'acreditar', 'Do you believe the story?', 'Do you believe to the story?', 'I believed it.', 'Acreditei.', 'believe **+ objeto**.'),
           ('doubt', '❓', 'duvidar', 'I doubt it.', 'I doubt of it.', 'I doubted it.', 'Duvidei.', 'doubt **+ it**.'),
           ('know', '🧠', 'saber', 'I do not know.', 'I do not knows.', 'I knew.', 'Eu sabia.', 'know → **knew**.'),
           ('tell', '🗣️', 'contar', 'He tells great stories.', 'He say great stories.', 'He told me.', 'Ele me contou.', 'tell → **told**.')],
    lines=[['Will', 'Who told the truth?', 'Quem disse a verdade?'],
           ['Edward', 'I am not sure.', 'Não tenho certeza.'],
           ['Will', 'The first story is doubtful.', 'A primeira história é duvidosa.'],
           ['Edward', 'The giant is unlikely to be real.', 'É improvável que o gigante seja real.'],
           ['Will', 'Is the second story certain?', 'A segunda história é certa?'],
           ['Edward', 'By no means. Nothing is certain.', 'De modo algum. Nada é certo.'],
           ['Will', 'True.', 'Verdade.'],
           ['Edward', 'A good story has many faces.', 'Uma boa história tem muitas faces.']],
    quiz=[('Is Edward sure who told the truth?', 'Edward tem certeza de quem disse a verdade?', [('🤷', 'No, he is not sure'), ('✅', 'Yes'), ('🙈', 'He knows')], 0, 1, 'Edward diz: “I am not sure.”'),
          ('What is doubtful?', 'O que é duvidoso?', [('📖', 'The first story'), ('🏠', 'The house'), ('🚪', 'The door')], 0, 2, 'Will diz: “The first story is doubtful.”'),
          ('Is the second story certain?', 'A segunda história é certa?', [('🚫', 'By no means'), ('✅', 'Yes'), ('🤷', 'Maybe')], 0, 5, 'Edward diz: “By no means.”')],
    fill=[['Did the river really turn gold?', 'O rio realmente ficou dourado?'], ['It is doubtful, but I like the idea.', 'É duvidoso, mas gosto da ideia.'],
          ['Tell it once more from the start.', 'Conte mais uma vez desde o começo.'], ['Gladly. Pull up a chair.', 'Com prazer. Puxe uma cadeira.']])
