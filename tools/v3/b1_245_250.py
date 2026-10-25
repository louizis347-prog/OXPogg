# B1 · episódios 245–250: idioms de brincadeira, revisão de relativas e conectores, verbo + -ing.
from v3.b1h import *

EPS = []

def mk(n, title, sub, pat, why, names, ids, rs, obra, scenes, cover, teaser, rule, fm, vocab, lab, verbs, mold, prod, m2, hot, gaps, traps, lines, quiz, exps):
    return S(n=n, title=title, sub=sub, pattern=pat, why=why, names=names, ids=ids, rs=rs, obra=(obra, obra),
             hot=hot, gaps=gaps, traps=traps, rule=rule, fm=fm, cover=cover, vocab=vocab, lines=lines, quiz=quiz,
             teaser=teaser, exps=exps, lab=lab, verbs=verbs, mold=mold, prod=prod, m2=m2, scenes=scenes)

# ---------- 245 / 246 · idioms de brincadeira ----------
JK_VOCAB = [('😏', 'wisecrack', 'piada sarcástica', 'Soa como “UÁIZ-krék”.'), ('🎭', 'prank', 'pegadinha', 'Soa como “PRÉNK”.'), ('💨', 'whoopee cushion', 'almofada de pum', 'Soa como “UU-pi KU-shon”.'),
            ('😜', 'kidding', 'brincando', 'Soa como “KÍ-ding”.'), ('🃏', 'practical joke', 'trote', 'Soa como “PRÉK-ti-kal DJÔUK”.'), ('🎤', 'stand-up', 'comédia stand-up', 'Soa como “STÉND-âp”.')]
JK_LAB = dict(short='jk', title='Laboratório de sons: prank, joke e kidding', pt='a soa é; o soa ôu; i soa i curto.', tip='Em joke, o j soa dj.',
              words=[('prank', 'PRÉNK', 'pegadinha', 'a = é', 'prink', 'PRÍNK'), ('joke', 'DJÔUK', 'piada', 'j = dj', 'choke', 'TCHÔUK'), ('kidding', 'KÍ-ding', 'brincando', 'i = i', 'kitten', 'KÍ-ten')])
JK_VERBS = [('pull', '🦵', 'puxar', "Are you pulling my leg?", "Are you pull my leg?", 'I pulled.', 'Puxei.', 'are you **pulling**?'),
            ('break', '🧊', 'quebrar', 'Let us break the ice.', 'Let us breaking the ice.', 'I broke it.', 'Quebrei.', 'let us + **break**.'),
            ('joke', '😜', 'brincar', 'You are joking!', 'You are joke!', 'I joked.', 'Brinquei.', 'you are **joking**.'),
            ('laugh', '😂', 'rir', 'We laughed a lot.', 'We laughed lot.', 'I laugh.', 'Eu rio.', 'passado **laughed**.')]
JK_MOLD = [("Pull someone's leg", 'Are you pulling', 'você está tirando', [(' my leg?', ' sarro de mim?'), (' his leg?', ' sarro dele?'), (' her leg?', ' sarro dela?')]),
           ('Break the ice', 'Let us break', 'vamos quebrar', [(' the ice.', ' o gelo.'), (' the silence.', ' o silêncio.'), (' the news.', ' a notícia.')]),
           ('A piece of cake', 'It is a piece of', 'é moleza', [(' cake.', ' bolo.'), (' cake for me.', ' bolo para mim.'), (' cake today.', ' bolo hoje.')])]
JK_RULE = ('Idioms de brincadeira', 'O sentido não é literal.', 'Em português “tirar sarro”. Em inglês: **pull my leg**.')
JK_FM = [('Pull', 'Are you pulling', 'my leg?', 'Are you pulling my leg?', 'sentido figurado.'), ('Ice', 'Let us break', 'the ice.', 'Let us break the ice.', 'quebrar o gelo.')]
JK_TRAPS = [('Qual frase está certa?', ['Are you pulling my leg?', 'Are you pulling me leg?', 'Do you pull my leg?'], 0, 'pulling my leg.'), ('Qual está certa?', ['It is a piece of cake.', 'It is a part of cake.', 'It is piece cake.'], 0, 'a piece of cake.')]

EPS.append(mk(930035, 'Pulling Your Leg', "idioms de brincadeira: pull someone's leg, break the ice, a piece of cake, you're joking (prank, wisecrack, kidding)",
    "idioms: pull someone's leg · break the ice · a piece of cake", "Hoje você aprende idioms de brincadeira: Are you pulling my leg? Let us break the ice. It is a piece of cake.",
    ('Man', 'Woman'), ['tom', 'polly'], 'home1', 'Friends', ['home1', 'living', 'kitchen', 'cafe2', 'yard', 'street'],
    ('Pulling Your Leg: em 10 minutos você entende brincadeiras em inglês', 'Em casa, o homem e a mulher fazem uma pegadinha.'), ('Mais idioms', 'Próximo: Brincadeiras'),
    JK_RULE, JK_FM, JK_VOCAB, JK_LAB, JK_VERBS, JK_MOLD,
    ('😜', 'Idioms', 'Use pulling my leg, break the ice e piece of cake', 'Fale. **Diga você está tirando sarro de mim, vamos quebrar o gelo e é moleza.**', 'break the ice', 'Are you pulling my leg? Let us break the ice. It is a piece of cake.',
     [('Usei pulling my leg?', r"\bpulling\s+my\s+leg\b", 'Are you pulling my leg?', 'Você está tirando sarro de mim?', 'Leg! 🦵'), ('Usei break the ice?', r"\bbreak\s+the\s+ice\b", 'Let us break the ice.', 'Vamos quebrar o gelo.', 'Ice! 🧊'), ('Usei piece of cake?', r"\bpiece\s+of\s+cake\b", 'It is a piece of cake.', 'É moleza.', 'Cake! 🍰')]),
    ('🃏', 'Fixas', 'Use you are joking, no kidding e just kidding', 'Fale. **Diga você está brincando, sem brincadeira e só brincando.**', 'just kidding', 'You are joking! No kidding. Just kidding!',
     [('Disse you are joking?', r"\byou\s+are\s+joking\b", 'You are joking!', 'Você está brincando!', 'Joking! 😜'), ('Disse no kidding?', r"\bno\s+kidding\b", 'No kidding.', 'Sem brincadeira.', 'No! 🙅'), ('Disse just kidding?', r"\bjust\s+kidding\b", 'Just kidding!', 'Só brincando!', 'Kidding! 🃏')]),
    [('🦵', "pull someone's leg", 'tirar sarro', 'Are you pulling my leg?', 'Você está tirando sarro de mim?'), ('🧊', 'break the ice', 'quebrar o gelo', 'Let us break the ice.', 'Vamos quebrar o gelo.'),
     ('🍰', 'a piece of cake', 'moleza', 'It is a piece of cake.', 'É moleza.'), ('🎭', 'prank', 'pegadinha', 'It was a prank.', 'Foi uma pegadinha.'), ('💨', 'whoopee cushion', 'almofada de pum', 'He used a whoopee cushion.', 'Ele usou uma almofada de pum.')],
    [('Are you pulling my ___?', 'Você está tirando sarro de mim?', ['leg', 'arm', 'hand'], 0, 'pulling my **leg**.'), ('Let us break the ___.', 'Vamos quebrar o gelo.', ['ice', 'glass', 'snow'], 0, 'break the **ice**.'),
     ('It is a piece of ___.', 'É moleza.', ['cake', 'bread', 'pie'], 0, 'a piece of **cake**.'), ('It was a ___.', 'Foi uma pegadinha.', ['prank', 'pranking', 'pranks is'], 0, 'a **prank**.')],
    JK_TRAPS,
    [['Man', 'Look! A whoopee cushion on my chair.', 'Olhe! Uma almofada de pum na minha cadeira.'], ['Woman', 'It was a prank!', 'Foi uma pegadinha!'], ['Man', 'Are you pulling my leg?', 'Você está tirando sarro de mim?'], ['Woman', 'Just kidding. Let us break the ice.', 'Só brincando. Vamos quebrar o gelo.'],
     ['Man', 'Okay. Tell me a joke.', 'Certo. Conte uma piada.'], ['Woman', 'It is a piece of cake.', 'É moleza.'], ['Man', 'You are joking!', 'Você está brincando!'], ['Woman', 'No kidding. We laughed a lot.', 'Sem brincadeira. Rimos muito.']],
    [('What was on the chair?', 'O que estava na cadeira?', [('💨', 'A whoopee cushion'), ('🧸', 'A toy'), ('🍎', 'An apple')], 0, 0, 'Diz: “A whoopee cushion.”'), ('What was it?', 'O que foi aquilo?', [('🎭', 'A prank'), ('🎁', 'A gift'), ('🚨', 'An alarm')], 0, 1, 'Diz: “It was a prank!”'),
     ('How was the joke?', 'Como foi a piada?', [('🍰', 'A piece of cake'), ('😭', 'Terrible'), ('🤐', 'Silent')], 0, 5, 'Diz: “a piece of cake.”')],
    [('🦵', 'Pull a fast one', 'Passar a perna', 'enganar', 'He pulled a fast one.', 'Ele passou a perna.'), ('🧊', 'Break the ice', 'Quebrar o gelo', 'iniciar conversa', 'Let us break the ice.', 'Vamos quebrar o gelo.'),
     ('🍰', 'A piece of cake', 'Moleza', 'fácil', 'It is a piece of cake.', 'É moleza.'), ('😜', 'Just kidding', 'Só brincando', 'suavizar', 'Just kidding!', 'Só brincando!')]))

EPS.append(mk(7930035, 'Brincadeiras', "mais idioms de brincadeira: hit the sack, crack up, make fun of e you are kidding (prank, practical joke, stand-up)",
    "mais idioms: crack up · make fun of · play a joke on", "Hoje você aprende mais idioms: We cracked up. Do not make fun of him. They played a joke on me.",
    ('Girl', 'Boy'), ['polly', 'tommy'], 'living', 'Friends', ['living', 'home1', 'kitchen', 'cafe2', 'school', 'park'],
    ('Brincadeiras: em 10 minutos você ri e entende piadas em inglês', 'Em casa, a menina e o menino assistem a um stand-up e riem.'), ('Mais idioms', 'Próximo: Revisão'),
    ('Mais idioms', 'Brincar sem ofender.', 'Em português “morrer de rir”. Em inglês: **crack up**.'),
    [('Crack up', 'We', 'cracked up.', 'We cracked up.', 'crack up = rir muito.'), ('Make fun of', 'Do not', 'make fun of him.', 'Do not make fun of him.', 'make fun of + pessoa.')],
    JK_VOCAB, JK_LAB, JK_VERBS, [('Crack up', 'We cracked', 'nós morremos', [(' up.', ' de rir.'), (' up at the joke.', ' de rir da piada.'), (' up on stage.', ' de rir no palco.')]), ('Make fun of', 'Do not make fun of', 'não zombe', [(' him.', ' dele.'), (' her.', ' dela.'), (' them.', ' deles.')]), ('Play a joke', 'They played a joke', 'eles pregaram uma peça', [(' on me.', ' em mim.'), (' on him.', ' nele.'), (' on us.', ' em nós.')])],
    ('😂', 'Idioms', 'Use crack up, make fun of e play a joke on', 'Fale. **Diga nós morremos de rir, não zombe dele e eles pregaram uma peça em mim.**', 'crack up', 'We cracked up. Do not make fun of him. They played a joke on me.',
     [('Usei crack up?', r"\bcracked\s+up\b", 'We cracked up.', 'Nós morremos de rir.', 'Crack! 😂'), ('Usei make fun of?', r"\bmake\s+fun\s+of\b", 'Do not make fun of him.', 'Não zombe dele.', 'Fun! 🙅'), ('Usei play a joke on?', r"\bplayed\s+a\s+joke\s+on\b", 'They played a joke on me.', 'Eles pregaram uma peça em mim.', 'Joke! 🃏')]),
    ('🎤', 'Fixas', 'Use for fun, laugh it off e joking aside', 'Fale. **Diga por diversão, levar na brincadeira e brincadeiras à parte.**', 'joking aside', 'We did it for fun. She laughed it off. Joking aside, thank you.',
     [('Disse for fun?', r"\bfor\s+fun\b", 'We did it for fun.', 'Fizemos por diversão.', 'Fun! 🎉'), ('Disse laugh it off?', r"\blaughed\s+it\s+off\b", 'She laughed it off.', 'Ela levou na brincadeira.', 'Off! 😅'), ('Disse joking aside?', r"\bjoking\s+aside\b", 'Joking aside, thank you.', 'Brincadeiras à parte, obrigado.', 'Aside! 🎤')]),
    [('😂', 'crack up', 'morrer de rir', 'We cracked up.', 'Nós morremos de rir.'), ('🙅', 'make fun of', 'zombar de', 'Do not make fun of him.', 'Não zombe dele.'),
     ('🃏', 'play a joke on', 'pregar uma peça em', 'They played a joke on me.', 'Eles pregaram uma peça em mim.'), ('🎤', 'stand-up', 'stand-up', 'The stand-up was funny.', 'O stand-up foi engraçado.'), ('🎪', 'practical joke', 'trote', 'It was a practical joke.', 'Foi um trote.')],
    [('We cracked ___.', 'Nós morremos de rir.', ['up', 'out', 'on'], 0, 'crack **up**.'), ('Do not make ___ of him.', 'Não zombe dele.', ['fun', 'joke', 'play'], 0, 'make **fun** of.'),
     ('They played a joke ___ me.', 'Eles pregaram uma peça em mim.', ['on', 'to', 'at'], 0, 'a joke **on**.'), ('The ___ was funny.', 'O stand-up foi engraçado.', ['stand-up', 'stand-ups is', 'standing'], 0, 'the **stand-up**.')],
    [('Qual frase está certa?', ['We cracked up.', 'We cracked on up.', 'We crack up yesterday.'], 0, 'cracked up.'), ('Qual está certa?', ['Do not make fun of him.', 'Do not make fun to him.', 'Do not fun of him.'], 0, 'make fun of.')],
    [['Girl', 'The stand-up was so funny.', 'O stand-up foi muito engraçado.'], ['Boy', 'We cracked up!', 'Nós morremos de rir!'], ['Girl', 'They played a joke on me yesterday.', 'Eles pregaram uma peça em mim ontem.'], ['Boy', 'Do not make fun of me.', 'Não zombe de mim.'],
     ['Girl', 'I am not. I laughed it off.', 'Não estou. Levei na brincadeira.'], ['Boy', 'It was a practical joke.', 'Foi um trote.'], ['Girl', 'Joking aside, I like it.', 'Brincadeiras à parte, gosto disso.'], ['Boy', 'Me too.', 'Eu também.']],
    [('What was funny?', 'O que foi engraçado?', [('🎤', 'The stand-up'), ('📺', 'The news'), ('🎵', 'The song')], 0, 0, 'Diz: “The stand-up was so funny.”'), ('Who played a joke?', 'Quem pregou uma peça?', [('👧', 'On her'), ('👦', 'On him'), ('👵', 'On Grandma')], 0, 2, 'Diz: “played a joke on me.”'),
     ('What does she do?', 'O que ela faz?', [('😅', 'Laughs it off'), ('😠', 'Gets angry'), ('😭', 'Cries')], 0, 4, 'Diz: “I laughed it off.”')],
    [('🎉', 'For fun', 'Por diversão', 'sem motivo sério', 'We did it for fun.', 'Fizemos por diversão.'), ('😅', 'Laugh it off', 'Levar na brincadeira', 'minimizar', 'She laughed it off.', 'Ela levou na brincadeira.'),
     ('🎤', 'Joking aside', 'Brincadeiras à parte', 'ficar sério', 'Joking aside, thank you.', 'Brincadeiras à parte, obrigado.'), ('🤣', 'Crack someone up', 'Fazer rir muito', 'divertir', 'He cracks me up.', 'Ele me faz rir muito.')]))

# ---------- 247 / 248 · revisão ----------
RV_VOCAB = [('😔', 'upset', 'chateada', 'Soa como “âp-SÉT”.'), ('❌', 'failed', 'falhou', 'Soa como “FÊILD”.'), ('🍼', 'born', 'nascida', 'Soa como “BÓRN”.'),
            ('🗝️', 'housekeeper', 'governanta', 'Soa como “RÁUS-ki-per”.'), ('😒', 'jealous', 'ciumenta', 'Soa como “DJÉ-las”.'), ('🧠', 'memory', 'memória', 'Soa como “MÉ-mo-ri”.')]
RV_LAB = dict(short='rv', title='Laboratório de sons: upset, born e jealous', pt='u soa â; or soa ór; j soa dj.', tip='Em jealous, o j soa dj.',
              words=[('upset', 'âp-SÉT', 'chateada', 'u = â', 'asset', 'É-set'), ('born', 'BÓRN', 'nascida', 'or = ór', 'barn', 'BÁRN'), ('jealous', 'DJÉ-las', 'ciumenta', 'j = dj', 'zealous', 'ZÉ-las')])
RV_VERBS = [('welcome', '🤝', 'receber', 'nobody welcomed her', 'nobody welcome her', 'I welcomed.', 'Recebi.', 'passado **welcomed**.'),
            ('fail', '❌', 'falhar', 'who failed', 'who fail yesterday', 'I failed.', 'Falhei.', 'passado **failed**.'),
            ('remember', '🧠', 'lembrar', 'whose memory', 'who memory', 'I remember.', 'Lembro.', 'whose **+ substantivo**.'),
            ('work', '🗝️', 'trabalhar', 'who works here', 'who work here', 'She works.', 'Ela trabalha.', 'who **works**.')]
RV_MOLD = [('Who', 'She is the housekeeper', 'ela é a governanta', [(' who works here.', ' que trabalha aqui.'), (' who knows everything.', ' que sabe de tudo.'), (' who was upset.', ' que ficou chateada.')]),
           ('Whose', 'She is the woman', 'ela é a mulher', [(' whose memory is great.', ' cuja memória é ótima.'), (' whose house is big.', ' cuja casa é grande.'), (' whose son is born.', ' cujo filho nasceu.')]),
           ('Because/although', 'She was upset', 'ela estava chateada', [(' because nobody welcomed her.', ' porque ninguém a recebeu.'), (' although she smiled.', ' embora sorrisse.'), (' because she failed.', ' porque falhou.')])]
RV_RULE = ('Revisão', 'Relativas e conectores juntos.', 'Em português “a governanta que trabalha aqui”. Em inglês: **the housekeeper who works here**.')
RV_FM = [('Relativa', 'She is the housekeeper', 'who works here.', 'She is the housekeeper who works here.', 'who + pessoa.'), ('Conector', 'She was upset', 'because nobody welcomed her.', 'She was upset because nobody welcomed her.', 'because + motivo.')]
RV_TRAPS = [('Qual frase está certa?', ['She is the housekeeper who works here.', 'She is the housekeeper which works here.', 'She is the housekeeper whose works here.'], 0, 'who + pessoa.'), ('Qual está certa?', ['She was upset because nobody welcomed her.', 'She was upset because of nobody welcomed her.', 'She was upset so nobody welcomed her.'], 0, 'because + frase.')]

EPS.append(mk(82160, 'Relative Clauses Review', "revisar relativas e conectores: who, which, whose, because, although e however (upset, housekeeper, memory)",
    "revisão: relativas + conectores de causa e contraste", "Hoje você revisa: She is the housekeeper who works here. She was upset because nobody welcomed her. However, she smiled.",
    ('Woman', 'Man'), ['polly', 'tom'], 'hall', 'Rebecca', ['hall', 'living', 'cafe2', 'street', 'lobby1', 'park'],
    ('Relative Clauses Review: em 10 minutos você junta relativas e conectores', 'No salão, a mulher e o homem falam da governanta de uma mansão.'), ('Revisão', 'Próximo: Revisão de relativas'),
    RV_RULE, RV_FM, RV_VOCAB, RV_LAB, RV_VERBS, RV_MOLD,
    ('🗝️', 'Revisão', 'Use who, whose e because', 'Fale. **Diga ela é a governanta que trabalha aqui, a mulher cuja memória é ótima e estava chateada porque ninguém a recebeu.**', 'whose', 'She is the housekeeper who works here. She is the woman whose memory is great. She was upset because nobody welcomed her.',
     [('Usei who?', r"\bhousekeeper\s+who\b", 'She is the housekeeper who works here.', 'Ela é a governanta que trabalha aqui.', 'Who! 🗝️'), ('Usei whose?', r"\bwhose\s+memory\b", 'She is the woman whose memory is great.', 'Ela é a mulher cuja memória é ótima.', 'Whose! 🧠'), ('Usei because?', r"\bbecause\s+nobody\b", 'She was upset because nobody welcomed her.', 'Ela ficou chateada porque ninguém a recebeu.', 'Because! 😔')]),
    ('😒', 'Fixas', 'Use as a result, in spite of e on the other hand', 'Fale. **Diga como resultado, apesar de e por outro lado.**', 'in spite of', 'As a result, she left. In spite of the rain, she came. On the other hand, she smiled.',
     [('Disse as a result?', r"\bas\s+a\s+result\b", 'As a result, she left.', 'Como resultado, ela saiu.', 'Result! ❌'), ('Disse in spite of?', r"\bin\s+spite\s+of\b", 'In spite of the rain, she came.', 'Apesar da chuva, ela veio.', 'Spite! 🌧️'), ('Disse on the other hand?', r"\bon\s+the\s+other\s+hand\b", 'On the other hand, she smiled.', 'Por outro lado, ela sorriu.', 'Hand! 😒')]),
    [('🗝️', 'who', 'que (pessoa)', 'She is the housekeeper who works here.', 'Ela é a governanta que trabalha aqui.'), ('🧠', 'whose', 'cujo', 'The woman whose memory is great.', 'A mulher cuja memória é ótima.'),
     ('😔', 'because', 'porque', 'She was upset because nobody welcomed her.', 'Ela estava chateada porque ninguém a recebeu.'), ('😒', 'jealous', 'ciumenta', 'She was jealous.', 'Ela era ciumenta.'), ('🍼', 'born', 'nascida', 'She was born here.', 'Ela nasceu aqui.')],
    [('She is the housekeeper ___ works here.', 'Ela é a governanta que trabalha aqui.', ['who', 'whose', 'which'], 0, '**who** + pessoa.'), ('The woman ___ memory is great.', 'A mulher cuja memória é ótima.', ['whose', 'who', 'that is'], 0, '**whose** + substantivo.'),
     ('She was upset ___ nobody welcomed her.', 'Ela estava chateada porque ninguém a recebeu.', ['because', 'so', 'but'], 0, '**because** + motivo.'), ('She was ___ here.', 'Ela nasceu aqui.', ['born', 'bore', 'bear'], 0, 'was **born**.')],
    RV_TRAPS,
    [['Woman', 'Who is that? She is the housekeeper who works here.', 'Quem é? Ela é a governanta que trabalha aqui.'], ['Man', 'She looks upset.', 'Ela parece chateada.'], ['Woman', 'She was upset because nobody welcomed her.', 'Ela ficou chateada porque ninguém a recebeu.'], ['Man', 'Is she jealous?', 'Ela é ciumenta?'],
     ['Woman', 'Yes, she was jealous. However, she smiled.', 'Sim, era ciumenta. No entanto, ela sorriu.'], ['Man', 'And her memory?', 'E a memória dela?'], ['Woman', 'She is a woman whose memory is great.', 'Ela é uma mulher cuja memória é ótima.'], ['Man', 'Interesting.', 'Interessante.']],
    [('Who is she?', 'Quem é ela?', [('🗝️', 'The housekeeper'), ('👩‍🏫', 'A teacher'), ('👵', 'A guest')], 0, 0, 'Diz: “the housekeeper.”'), ('Why was she upset?', 'Por que ela estava chateada?', [('😔', 'Nobody welcomed her'), ('🌧️', 'It rained'), ('🍽️', 'No food')], 0, 2, 'Diz: “nobody welcomed her.”'),
     ('How is her memory?', 'Como é a memória dela?', [('🧠', 'Great'), ('🌫️', 'Bad'), ('😴', 'Sleepy')], 0, 6, 'Diz: “memory is great.”')],
    [('🔁', 'As a result', 'Como resultado', 'consequência', 'As a result, she left.', 'Como resultado, ela saiu.'), ('🌧️', 'In spite of', 'Apesar de', 'contraste', 'In spite of the rain, she came.', 'Apesar da chuva, ela veio.'),
     ('😒', 'On the other hand', 'Por outro lado', 'comparar', 'On the other hand, she smiled.', 'Por outro lado, ela sorriu.'), ('🧠', 'Bear in mind', 'Lembre-se', 'avisar', 'Bear in mind her memory.', 'Lembre-se da memória dela.')]))

EPS.append(mk(7082160, 'Revisão de relativas e conectores', "revisão prática de who, which, that, although e however (housekeeper, jealous, failed)",
    "revisão prática: which × that · although × however", "Hoje você revisa na prática: The house which she keeps is big. Although she failed, she smiled. However, she tried.",
    ('Girl', 'Man'), ['polly', 'tom'], 'hall', 'Rebecca', ['hall', 'living', 'office', 'street', 'lobby1', 'cafe2'],
    ('Revisão de relativas e conectores: em 10 minutos você mostra o que já domina', 'No salão, a menina e o homem revisam a história da mansão.'), ('Revisão', 'Próximo: Verbo + ing'),
    ('Revisão', 'Which, that, although e however.', 'Em português “a casa que ela cuida”. Em inglês: **the house which she keeps**.'),
    [('Which', 'The house', 'which she keeps is big.', 'The house which she keeps is big.', 'which + coisa.'), ('Although', 'Although she failed,', 'she smiled.', 'Although she failed, she smiled.', 'although + vírgula.')],
    RV_VOCAB, RV_LAB, RV_VERBS, [('Which', 'The house', 'a casa', [(' which she keeps is big.', ' que ela cuida é grande.'), (' that she loves is old.', ' que ela ama é velha.'), (' which burned is gone.', ' que queimou sumiu.')]), ('Although', 'Although she failed,', 'embora tenha falhado,', [(' she smiled.', ' ela sorriu.'), (' she tried again.', ' tentou de novo.'), (' she was calm.', ' ficou calma.')]), ('However', 'She failed; however,', 'ela falhou; no entanto,', [(' she tried again.', ' tentou de novo.'), (' she smiled.', ' sorriu.'), (' she was brave.', ' foi corajosa.')])],
    ('🏚️', 'Revisão', 'Use which, although e however', 'Fale. **Diga a casa que ela cuida é grande, embora tenha falhado ela sorriu e no entanto tentou.**', 'although', 'The house which she keeps is big. Although she failed, she smiled. However, she tried again.',
     [('Usei which?', r"\bhouse\s+which\b", 'The house which she keeps is big.', 'A casa que ela cuida é grande.', 'Which! 🏚️'), ('Usei although?', r"\balthough\s+she\b", 'Although she failed, she smiled.', 'Embora tenha falhado, ela sorriu.', 'Although! 😊'), ('Usei however?', r"\bhowever,?\s+she\b", 'However, she tried again.', 'No entanto, ela tentou de novo.', 'However! ⚖️')]),
    ('😒', 'Fixas', 'Use in the first place, to be honest e by the way', 'Fale. **Diga em primeiro lugar, para ser honesto e a propósito.**', 'by the way', 'In the first place, she failed. To be honest, she smiled. By the way, who is she?',
     [('Disse in the first place?', r"\bin\s+the\s+first\s+place\b", 'In the first place, she failed.', 'Em primeiro lugar, ela falhou.', 'Place! 1️⃣'), ('Disse to be honest?', r"\bto\s+be\s+honest\b", 'To be honest, she smiled.', 'Para ser honesta, ela sorriu.', 'Honest! 😊'), ('Disse by the way?', r"\bby\s+the\s+way\b", 'By the way, who is she?', 'A propósito, quem é ela?', 'Way! ❓')]),
    [('🏚️', 'which', 'que (coisa)', 'The house which she keeps is big.', 'A casa que ela cuida é grande.'), ('😊', 'although', 'embora', 'Although she failed, she smiled.', 'Embora tenha falhado, ela sorriu.'),
     ('⚖️', 'however', 'no entanto', 'However, she tried again.', 'No entanto, ela tentou de novo.'), ('❌', 'failed', 'falhou', 'She failed the test.', 'Ela falhou no teste.'), ('🍼', 'born', 'nascida', 'She was born in May.', 'Ela nasceu em maio.')],
    [('The house ___ she keeps is big.', 'A casa que ela cuida é grande.', ['which', 'who', 'whose'], 0, '**which** + coisa.'), ('___ she failed, she smiled.', 'Embora tenha falhado, ela sorriu.', ['Although', 'Because', 'So'], 0, '**Although**,'),
     ('She failed; ___, she tried again.', 'Ela falhou; no entanto, tentou de novo.', ['however', 'because', 'and so'], 0, '**however**,'), ('She ___ the test.', 'Ela falhou no teste.', ['failed', 'fail', 'failing'], 0, 'passado **failed**.')],
    [('Qual frase está certa?', ['Although she failed, she smiled.', 'Although she failed but she smiled.', 'Although she failed, but she smiled.'], 0, 'although sem but.'), ('Qual está certa?', ['The house which she keeps is big.', 'The house who she keeps is big.', 'The house whose she keeps is big.'], 0, 'which + coisa.')],
    [['Man', 'Tell me about the house which she keeps.', 'Conte-me sobre a casa que ela cuida.'], ['Girl', 'The house which she keeps is big.', 'A casa que ela cuida é grande.'], ['Man', 'Did she fail the test?', 'Ela falhou no teste?'], ['Girl', 'Although she failed, she smiled.', 'Embora tenha falhado, ela sorriu.'],
     ['Man', 'Was she sad?', 'Estava triste?'], ['Girl', 'She failed; however, she tried again.', 'Falhou; no entanto, tentou de novo.'], ['Man', 'By the way, when was she born?', 'A propósito, quando ela nasceu?'], ['Girl', 'She was born in May.', 'Ela nasceu em maio.']],
    [('How is the house?', 'Como é a casa?', [('🏚️', 'Big'), ('🏠', 'Tiny'), ('🏗️', 'New')], 0, 1, 'Diz: “is big.”'), ('What did she do after failing?', 'O que ela fez depois de falhar?', [('😊', 'Smiled'), ('😭', 'Cried'), ('🏃', 'Left')], 0, 3, 'Diz: “she smiled.”'),
     ('When was she born?', 'Quando ela nasceu?', [('🌸', 'In May'), ('❄️', 'In July'), ('🍂', 'In April')], 0, 7, 'Diz: “born in May.”')],
    [('1️⃣', 'In the first place', 'Em primeiro lugar', 'ordenar', 'In the first place, she failed.', 'Em primeiro lugar, ela falhou.'), ('😊', 'To be honest', 'Para ser honesto', 'franqueza', 'To be honest, she smiled.', 'Para ser honesta, ela sorriu.'),
     ('❓', 'By the way', 'A propósito', 'mudar de assunto', 'By the way, who is she?', 'A propósito, quem é ela?'), ('🏚️', 'Keep house', 'Cuidar da casa', 'rotina', 'She keeps house.', 'Ela cuida da casa.')]))

# ---------- 249 / 250 · verbo + -ing ----------
IN_VOCAB = [('📖', 'enjoy', 'gostar', 'Soa como “en-DJÓI”.'), ('🚫', 'avoid', 'evitar', 'Soa como “a-VÓID”.'), ('💡', 'suggest', 'sugerir', 'Soa como “sa-DJÉST”.'),
            ('🙋', 'mind', 'importar-se', 'Soa como “MÁIND”.'), ('🏁', 'finish', 'terminar', 'Soa como “FÍ-nish”.'), ('🌈', 'imagine', 'imaginar', 'Soa como “i-MÉ-djin”.')]
IN_LAB = dict(short='in', title='Laboratório de sons: enjoy, avoid e imagine', pt='oy soa ói; oi soa ói; g soa dj.', tip='Em imagine, o g soa dj.',
              words=[('enjoy', 'en-DJÓI', 'gostar', 'oy = ói', 'annoy', 'a-NÓI'), ('avoid', 'a-VÓID', 'evitar', 'oi = ói', 'void', 'VÓID'), ('imagine', 'i-MÉ-djin', 'imaginar', 'g = dj', 'image', 'Í-midj')])
IN_VERBS = [('enjoy', '📖', 'gostar', 'I enjoy reading.', 'I enjoy to read.', 'I enjoyed.', 'Gostei.', 'enjoy + **-ing**.'),
            ('avoid', '🚫', 'evitar', 'He avoids driving.', 'He avoids to drive.', 'I avoided.', 'Evitei.', 'avoid + **-ing**.'),
            ('suggest', '💡', 'sugerir', 'I suggest leaving.', 'I suggest to leave.', 'I suggested.', 'Sugeri.', 'suggest + **-ing**.'),
            ('mind', '🙋', 'importar-se', 'Do you mind waiting?', 'Do you mind to wait?', 'I mind.', 'Eu me importo.', 'mind + **-ing**.')]
IN_MOLD = [('Enjoy', 'I enjoy', 'eu gosto de', [(' reading at night.', ' ler à noite.'), (' walking home.', ' andar para casa.'), (' cooking dinner.', ' cozinhar o jantar.')]),
           ('Avoid', 'He avoids', 'ele evita', [(' driving at night.', ' dirigir à noite.'), (' eating sugar.', ' comer açúcar.'), (' talking to me.', ' falar comigo.')]),
           ('Mind', 'Do you mind', 'você se importa de', [(' waiting?', ' esperar?'), (' closing it?', ' fechar isso?'), (' helping me?', ' me ajudar?')])]
IN_RULE = ('Verbo + -ing', 'Enjoy, avoid, suggest e mind pedem -ing.', 'Em português “gosto de ler”. Em inglês: **I enjoy reading**.')
IN_FM = [('Enjoy', 'I enjoy', 'reading at night.', 'I enjoy reading at night.', 'enjoy + -ing.'), ('Mind', 'Do you mind', 'waiting?', 'Do you mind waiting?', 'mind + -ing.')]
IN_TRAPS = [('Qual frase está certa?', ['I enjoy reading at night.', 'I enjoy to read at night.', 'I enjoy read at night.'], 0, 'enjoy + -ing.'), ('Qual está certa?', ['Do you mind waiting?', 'Do you mind to wait?', 'Do you mind wait?'], 0, 'mind + -ing.')]

EPS.append(mk(82161, 'Verb + -ing', "usar verbos seguidos de -ing: enjoy, avoid, suggest, mind, finish e imagine",
    "verbos + -ing: enjoy · avoid · suggest · mind", "Hoje você aprende verbos seguidos de -ing: I enjoy reading. He avoids driving. Do you mind waiting?",
    ('Man', 'Woman'), ['tom', 'polly'], 'cafe2', 'The Count of Monte Cristo', ['cafe2', 'lake', 'living', 'street', 'park', 'hall'],
    ('Verb + -ing: em 10 minutos você acerta o verbo depois de enjoy, avoid e mind', 'No café, o homem e a mulher falam de hábitos e esperas.'), ('Mais verbos', 'Próximo: Verbo + -ing na prática'),
    IN_RULE, IN_FM, IN_VOCAB, IN_LAB, IN_VERBS, IN_MOLD,
    ('📖', 'Hábitos', 'Use enjoy, avoid e mind com -ing', 'Fale. **Diga gosto de ler à noite, ele evita dirigir e você se importa de esperar.**', 'avoid', 'I enjoy reading at night. He avoids driving. Do you mind waiting?',
     [('Usei enjoy?', r"\benjoy\s+reading\b", 'I enjoy reading at night.', 'Gosto de ler à noite.', 'Enjoy! 📖'), ('Usei avoid?', r"\bavoids?\s+driving\b", 'He avoids driving.', 'Ele evita dirigir.', 'Avoid! 🚫'), ('Usei mind?', r"\bmind\s+waiting\b", 'Do you mind waiting?', 'Você se importa de esperar?', 'Mind! 🙋')]),
    ('🌈', 'Fixas', 'Use cannot help, it is no use e look forward to', 'Fale. **Diga não consigo evitar, não adianta e estou ansioso por.**', 'look forward to', 'I cannot help laughing. It is no use crying. I look forward to seeing you.',
     [('Disse cannot help?', r"\bcannot\s+help\s+laughing\b", 'I cannot help laughing.', 'Não consigo evitar rir.', 'Help! 😂'), ('Disse no use?', r"\bno\s+use\s+crying\b", 'It is no use crying.', 'Não adianta chorar.', 'Use! 😭'), ('Disse look forward to?', r"\blook\s+forward\s+to\s+seeing\b", 'I look forward to seeing you.', 'Estou ansioso para ver você.', 'Forward! 🌈')]),
    [('📖', 'enjoy', 'gostar', 'I enjoy reading at night.', 'Gosto de ler à noite.'), ('🚫', 'avoid', 'evitar', 'He avoids driving.', 'Ele evita dirigir.'),
     ('💡', 'suggest', 'sugerir', 'I suggest leaving.', 'Sugiro sair.'), ('🙋', 'mind', 'importar-se', 'Do you mind waiting?', 'Você se importa de esperar?'), ('🏁', 'finish', 'terminar', 'I finished eating.', 'Terminei de comer.')],
    [('I enjoy ___ at night.', 'Gosto de ler à noite.', ['reading', 'to read', 'read'], 0, 'enjoy + **-ing**.'), ('He avoids ___.', 'Ele evita dirigir.', ['driving', 'to drive', 'drive'], 0, 'avoid + **-ing**.'),
     ('I suggest ___.', 'Sugiro sair.', ['leaving', 'to leave', 'leave to'], 0, 'suggest + **-ing**.'), ('I finished ___.', 'Terminei de comer.', ['eating', 'to eat', 'eat'], 0, 'finish + **-ing**.')],
    IN_TRAPS,
    [['Man', 'What do you do at night? I enjoy reading.', 'O que você faz à noite? Gosto de ler.'], ['Woman', 'My brother avoids driving at night.', 'Meu irmão evita dirigir à noite.'], ['Man', 'I suggest taking the bus.', 'Sugiro pegar o ônibus.'], ['Woman', 'Do you mind waiting a minute?', 'Você se importa de esperar um minuto?'],
     ['Man', 'Not at all.', 'De jeito nenhum.'], ['Woman', 'I will finish eating soon.', 'Vou terminar de comer logo.'], ['Man', 'Can you imagine living here?', 'Consegue imaginar morar aqui?'], ['Woman', 'Yes!', 'Sim!']],
    [('What does he enjoy?', 'Do que ele gosta?', [('📖', 'Reading'), ('🏊', 'Swimming'), ('🎮', 'Gaming')], 0, 0, 'Diz: “I enjoy reading.”'), ('What does her brother avoid?', 'O que o irmão dela evita?', [('🚗', 'Driving at night'), ('🍕', 'Pizza'), ('🏃', 'Running')], 0, 1, 'Diz: “avoids driving.”'),
     ('What does he suggest?', 'O que ele sugere?', [('🚌', 'Taking the bus'), ('🚕', 'A taxi'), ('🚶', 'Walking')], 0, 2, 'Diz: “taking the bus.”')],
    [('😂', 'Cannot help', 'Não consigo evitar', 'reação', 'I cannot help laughing.', 'Não consigo evitar rir.'), ('😭', 'It is no use', 'Não adianta', 'inútil', 'It is no use crying.', 'Não adianta chorar.'),
     ('🌈', 'Look forward to', 'Estar ansioso por', 'expectativa', 'I look forward to seeing you.', 'Estou ansioso para ver você.'), ('🤔', 'Feel like', 'Estar com vontade de', 'desejo', 'I feel like walking.', 'Estou com vontade de caminhar.')]))

EPS.append(mk(7082161, 'Verbo + -ing', "verbo + -ing na prática: finish, imagine, keep, practise e consider",
    "mais verbos + -ing: keep · practise · consider · imagine", "Hoje você pratica mais verbos com -ing: She keeps talking. We practise speaking. Imagine living here.",
    ('Girl', 'Boy'), ['polly', 'tommy'], 'school', 'The Count of Monte Cristo', ['school', 'hall', 'living', 'cafe2', 'park', 'yard'],
    ('Verbo + -ing: em 10 minutos você treina mais cinco verbos seguidos de -ing', 'Na escola, a menina e o menino treinam inglês juntos.'), ('Mais verbos', 'Próximo: Próximo bloco'),
    ('Mais -ing', 'Keep, practise, consider e imagine.', 'Em português “continue falando”. Em inglês: **keep talking**.'),
    [('Keep', 'She keeps', 'talking.', 'She keeps talking.', 'keep + -ing.'), ('Practise', 'We practise', 'speaking.', 'We practise speaking.', 'practise + -ing.')],
    IN_VOCAB, IN_LAB, IN_VERBS, [('Keep', 'She keeps', 'ela continua', [(' talking.', ' falando.'), (' smiling.', ' sorrindo.'), (' trying.', ' tentando.')]), ('Practise', 'We practise', 'nós praticamos', [(' speaking.', ' falar.'), (' reading.', ' ler.'), (' writing.', ' escrever.')]), ('Imagine', 'Imagine', 'imagine', [(' living here.', ' morar aqui.'), (' flying home.', ' voar para casa.'), (' winning.', ' vencer.')])],
    ('🏫', 'Prática', 'Use keep, practise e imagine com -ing', 'Fale. **Diga ela continua falando, nós praticamos falar e imagine morar aqui.**', 'practise', 'She keeps talking. We practise speaking. Imagine living here.',
     [('Usei keep?', r"\bkeeps?\s+talking\b", 'She keeps talking.', 'Ela continua falando.', 'Keep! 🔁'), ('Usei practise?', r"\bpracti[sc]e\s+speaking\b", 'We practise speaking.', 'Nós praticamos falar.', 'Practise! 🗣️'), ('Usei imagine?', r"\bimagine\s+living\b", 'Imagine living here.', 'Imagine morar aqui.', 'Imagine! 🌈')]),
    ('🌈', 'Fixas', 'Use give up, put off e carry on', 'Fale. **Diga desistir de, adiar e continuar.**', 'carry on', 'Do not give up trying. Do not put off studying. Carry on working.',
     [('Disse give up?', r"\bgive\s+up\s+trying\b", 'Do not give up trying.', 'Não desista de tentar.', 'Give! 🏳️'), ('Disse put off?', r"\bput\s+off\s+studying\b", 'Do not put off studying.', 'Não adie o estudo.', 'Off! ⏳'), ('Disse carry on?', r"\bcarry\s+on\s+working\b", 'Carry on working.', 'Continue trabalhando.', 'Carry! 🔁')]),
    [('🔁', 'keep', 'continuar', 'She keeps talking.', 'Ela continua falando.'), ('🗣️', 'practise', 'praticar', 'We practise speaking.', 'Nós praticamos falar.'),
     ('🌈', 'imagine', 'imaginar', 'Imagine living here.', 'Imagine morar aqui.'), ('🤔', 'consider', 'considerar', 'I consider moving.', 'Considero me mudar.'), ('🏫', 'school', 'escola', 'We practise at school.', 'Praticamos na escola.')],
    [('She keeps ___.', 'Ela continua falando.', ['talking', 'to talk', 'talk'], 0, 'keep + **-ing**.'), ('We practise ___.', 'Nós praticamos falar.', ['speaking', 'to speak', 'speak'], 0, 'practise + **-ing**.'),
     ('Imagine ___ here.', 'Imagine morar aqui.', ['living', 'to live', 'live'], 0, 'imagine + **-ing**.'), ('I consider ___.', 'Considero me mudar.', ['moving', 'to move', 'move'], 0, 'consider + **-ing**.')],
    [('Qual frase está certa?', ['She keeps talking.', 'She keeps to talk.', 'She keeps talk.'], 0, 'keep + -ing.'), ('Qual está certa?', ['We practise speaking.', 'We practise to speak.', 'We practise speak.'], 0, 'practise + -ing.')],
    [['Girl', 'My teacher keeps talking about grammar.', 'Minha professora continua falando de gramática.'], ['Boy', 'We practise speaking every day.', 'Nós praticamos falar todo dia.'], ['Girl', 'Do not give up trying.', 'Não desista de tentar.'], ['Boy', 'I consider moving to London.', 'Considero me mudar para Londres.'],
     ['Girl', 'Imagine living there!', 'Imagine morar lá!'], ['Boy', 'I cannot help smiling.', 'Não consigo evitar sorrir.'], ['Girl', 'Let us carry on working.', 'Vamos continuar trabalhando.'], ['Boy', 'Okay.', 'Certo.']],
    [('What does the teacher keep doing?', 'O que a professora continua fazendo?', [('🗣️', 'Talking'), ('😴', 'Sleeping'), ('🏃', 'Running')], 0, 0, 'Diz: “keeps talking.”'), ('Where does he consider moving?', 'Para onde ele considera se mudar?', [('🇬🇧', 'London'), ('🇫🇷', 'Paris'), ('🇧🇷', 'Rio')], 0, 3, 'Diz: “moving to London.”'),
     ('What can he not help?', 'O que ele não consegue evitar?', [('😊', 'Smiling'), ('😭', 'Crying'), ('😴', 'Sleeping')], 0, 5, 'Diz: “help smiling.”')],
    [('🏳️', 'Give up', 'Desistir', 'parar de tentar', 'Do not give up trying.', 'Não desista de tentar.'), ('⏳', 'Put off', 'Adiar', 'deixar para depois', 'Do not put off studying.', 'Não adie o estudo.'),
     ('🔁', 'Carry on', 'Continuar', 'seguir em frente', 'Carry on working.', 'Continue trabalhando.'), ('🤝', 'Go on', 'Prosseguir', 'continuar', 'Go on talking.', 'Continue falando.')]))
