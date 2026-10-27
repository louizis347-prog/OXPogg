# B1 · episódios 269–274: finalidade com to, phrasal verbs de movimento, phrasal verbs com look.
from v3.b1h import *

from v3.ovrb1 import install
EPS = []
install(globals(), 'S')

def mk(n, title, sub, pat, why, names, ids, rs, obra, scenes, cover, teaser, rule, fm, vocab, lab, verbs, mold, prod, m2, hot, gaps, traps, lines, quiz, exps):
    return S(n=n, title=title, sub=sub, pattern=pat, why=why, names=names, ids=ids, rs=rs, obra=(obra, obra),
             hot=hot, gaps=gaps, traps=traps, rule=rule, fm=fm, cover=cover, vocab=vocab, lines=lines, quiz=quiz,
             teaser=teaser, exps=exps, lab=lab, verbs=verbs, mold=mold, prod=prod, m2=m2, scenes=scenes)

# ---------- 269 / 270 · finalidade ----------
PU_VOCAB = [('🎓', 'learn', 'aprender', 'Soa como “LÂRN”.'), ('🛒', 'buy', 'comprar', 'Soa como “BÁI”.'), ('🗣️', 'say', 'dizer', 'Soa como “SÊI”.'),
            ('🧠', 'brain', 'cérebro', 'Soa como “BRÊIN”.'), ('🦁', 'courage', 'coragem', 'Soa como “KÂ-ridj”.'), ('🛣️', 'road', 'estrada', 'Soa como “RÔUD”.')]
PU_LAB = dict(short='pu', title='Laboratório de sons: learn, brain e courage', pt='ear soa âr; ai soa êi; ou soa â.', tip='Em courage, o ou soa â.',
              words=[('learn', 'LÂRN', 'aprender', 'ear = âr', 'lawn', 'LÓN'), ('brain', 'BRÊIN', 'cérebro', 'ai = êi', 'brown', 'BRÁUN'), ('courage', 'KÂ-ridj', 'coragem', 'ou = â', 'cottage', 'KÓ-tidj')])
PU_VERBS = [('go', '🏫', 'ir', 'I go to school to learn.', 'I go to school for learn.', 'I went.', 'Fui.', 'to + **verbo**.'),
            ('buy', '🛒', 'comprar', 'I went out to buy bread.', 'I went out for buy bread.', 'I bought.', 'Comprei.', 'to + **buy**.'),
            ('ask', '🗣️', 'pedir', 'He came to ask for help.', 'He came for to ask help.', 'I asked.', 'Pedi.', 'came to + **ask**.'),
            ('follow', '🛣️', 'seguir', 'We follow the road to find him.', 'We follow the road for find him.', 'I followed.', 'Segui.', 'to + **find**.')]
PU_RULE = ('Finalidade com to', 'Para quê? To + verbo.', 'Em português “vou à escola para aprender”. Em inglês: **I go to school to learn**.')
PU_FM = [('Para quê', 'I go to school', 'to learn English.', 'I go to school to learn English.', 'to + verbo.'), ('Não use for', 'I came here', 'to ask for help.', 'I came here to ask for help.', 'não for + verbo.')]
PU_TRAPS = [('Qual frase está certa?', ['I go to school to learn English.', 'I go to school for learn English.', 'I go to school for learning English to.'], 0, 'to + verbo.'), ('Qual está certa?', ['I went out to buy bread.', 'I went out for buy bread.', 'I went out buying bread to.'], 0, 'to buy.')]

EPS.append(mk(82173, 'Infinitive of Purpose', "dizer para que algo serve com to + verbo (learn, buy, say, courage)",
    "finalidade: to + verbo · in order to · so as to", "Hoje você aprende a dizer para quê: I go to school to learn English. I went out to buy bread.",
    ('Girl', 'Man'), ['polly', 'tom'], 'cafe2', 'The Wonderful Wizard of Oz', ['cafe2', 'street', 'park', 'living', 'hall', 'shop'],
    ('Infinitive of Purpose: em 10 minutos você explica para que faz as coisas', 'No café, a menina e o homem falam de uma viagem pela estrada de tijolos.'), ('Mais finalidade', 'Próximo: Finalidade com to'),
    PU_RULE, PU_FM, PU_VOCAB, PU_LAB, PU_VERBS,
    [('To + verbo', 'I go to school', 'vou à escola', [(' to learn English.', ' para aprender inglês.'), (' to meet friends.', ' para ver amigos.'), (' to read.', ' para ler.')]), ('Came to', 'He came', 'ele veio', [(' to ask for help.', ' pedir ajuda.'), (' to see me.', ' me ver.'), (' to say hello.', ' dizer olá.')]), ('Went to', 'We went out', 'saímos', [(' to buy bread.', ' para comprar pão.'), (' to find him.', ' para achá-lo.'), (' to get air.', ' para tomar ar.')])],
    ('🎓', 'Finalidade', 'Use to learn, to buy e to ask', 'Fale. **Diga vou à escola para aprender inglês, saí para comprar pão e ele veio pedir ajuda.**', 'to buy', 'I go to school to learn English. I went out to buy bread. He came to ask for help.',
     [('Usei to learn?', r"\bto\s+learn\b", 'I go to school to learn English.', 'Vou à escola para aprender inglês.', 'Learn! 🎓'), ('Usei to buy?', r"\bto\s+buy\b", 'I went out to buy bread.', 'Saí para comprar pão.', 'Buy! 🛒'), ('Usei to ask?', r"\bto\s+ask\b", 'He came to ask for help.', 'Ele veio pedir ajuda.', 'Ask! 🗣️')]),
    ('🦁', 'Fixas', 'Use in order to, so as to e for fun', 'Fale. **Diga a fim de, de modo a e por diversão.**', 'so as to', 'In order to win, be brave. Walk slowly so as to see. We do it for fun.',
     [('Disse in order to?', r"\bin\s+order\s+to\b", 'In order to win, be brave.', 'A fim de vencer, seja corajoso.', 'Order! 🏆'), ('Disse so as to?', r"\bso\s+as\s+to\b", 'Walk slowly so as to see.', 'Ande devagar para ver.', 'So! 👀'), ('Disse for fun?', r"\bfor\s+fun\b", 'We do it for fun.', 'Fazemos por diversão.', 'Fun! 🎉')]),
    [('🎓', 'to learn', 'para aprender', 'I go to school to learn English.', 'Vou à escola para aprender inglês.'), ('🛒', 'to buy', 'para comprar', 'I went out to buy bread.', 'Saí para comprar pão.'), ('🗣️', 'to ask', 'para pedir', 'He came to ask for help.', 'Ele veio pedir ajuda.'), ('🦁', 'courage', 'coragem', 'He needs courage.', 'Ele precisa de coragem.'), ('🧠', 'brain', 'cérebro', 'He wants a brain.', 'Ele quer um cérebro.')],
    [('I go to school ___ learn English.', 'Vou à escola para aprender inglês.', ['to', 'for', 'in to'], 0, '**to** + verbo.'), ('I went out ___ buy bread.', 'Saí para comprar pão.', ['to', 'for', 'at'], 0, '**to** buy.'), ('He came ___ ask for help.', 'Ele veio pedir ajuda.', ['to', 'for', 'by'], 0, 'came **to** ask.'), ('He needs ___.', 'Ele precisa de coragem.', ['courage', 'courageous', 'courageously'], 0, 'needs **courage**.')],
    PU_TRAPS,
    [['Girl', 'Why are you on the road?', 'Por que você está na estrada?'], ['Man', 'I am going to the city to ask for a brain.', 'Vou à cidade pedir um cérebro.'], ['Girl', 'And your friend?', 'E seu amigo?'], ['Man', 'He walks with me to find courage.', 'Ele anda comigo para achar coragem.'],
     ['Girl', 'I went out to buy bread.', 'Eu saí para comprar pão.'], ['Man', 'We follow the road to get there.', 'Seguimos a estrada para chegar lá.'], ['Girl', 'Good luck!', 'Boa sorte!'], ['Man', 'Thanks!', 'Obrigado!']],
    [('Why is he going to the city?', 'Por que vai à cidade?', [('🧠', 'To ask for a brain'), ('🍞', 'To buy bread'), ('🎡', 'To play')], 0, 1, 'Diz: “to ask for a brain.”'), ('Why does his friend walk?', 'Por que o amigo anda?', [('🦁', 'To find courage'), ('🍎', 'To find food'), ('💤', 'To sleep')], 0, 3, 'Diz: “to find courage.”'),
     ('Why did she go out?', 'Por que ela saiu?', [('🍞', 'To buy bread'), ('🎬', 'To see a film'), ('🏃', 'To run')], 0, 4, 'Diz: “to buy bread.”')],
    [('🏆', 'In order to', 'A fim de', 'formal', 'In order to win, be brave.', 'A fim de vencer, seja corajoso.'), ('👀', 'So as to', 'De modo a', 'cuidado', 'Walk slowly so as to see.', 'Ande devagar para ver.'), ('🎉', 'For fun', 'Por diversão', 'sem razão séria', 'We do it for fun.', 'Fazemos por diversão.'), ('🛣️', 'On my way to', 'A caminho de', 'trajeto', 'On my way to the city.', 'A caminho da cidade.')]))

EPS.append(mk(7082173, 'Finalidade com to', "finalidade com to, for e so that (learn, buy, say, road)",
    "finalidade: to × for × so that", "Hoje você pratica: I use it to cut. It is for cutting. I speak slowly so that you understand.",
    ('Man', 'Girl'), ['tom', 'polly'], 'kitchen', 'The Wonderful Wizard of Oz', ['kitchen', 'home1', 'living', 'shop', 'cafe2', 'street'],
    ('Finalidade com to: em 10 minutos você diz para que serve cada coisa', 'Na cozinha, o homem e a menina falam para que serve cada objeto.'), ('Mais finalidade', 'Próximo: Phrasal verbs de movimento'),
    ('Serve para', 'To + verbo, for + -ing, so that + frase.', 'Em português “serve para cortar”. Em inglês: **it is for cutting** ou **I use it to cut**.'),
    [('To', 'I use it', 'to cut bread.', 'I use it to cut bread.', 'use it to + verbo.'), ('For', 'It is', 'for cutting bread.', 'It is for cutting bread.', 'for + -ing.')],
    PU_VOCAB, PU_LAB, PU_VERBS,
    [('Use to', 'I use it', 'eu uso para', [(' to cut bread.', ' cortar pão.'), (' to open it.', ' abrir isso.'), (' to learn.', ' aprender.')]), ('For -ing', 'It is for', 'serve para', [(' cutting bread.', ' cortar pão.'), (' opening cans.', ' abrir latas.'), (' mixing food.', ' misturar comida.')]), ('So that', 'I speak slowly so that', 'falo devagar para que', [(' you understand.', ' você entenda.'), (' he learns.', ' ele aprenda.'), (' they hear.', ' eles ouçam.')])],
    ('🔪', 'Serve para', 'Use to, for e so that', 'Fale. **Diga eu uso para cortar pão, serve para abrir latas e falo devagar para que você entenda.**', 'so that', 'I use it to cut bread. It is for opening cans. I speak slowly so that you understand.',
     [('Usei use it to?', r"\buse\s+it\s+to\s+cut\b", 'I use it to cut bread.', 'Eu uso para cortar pão.', 'To! 🔪'), ('Usei for -ing?', r"\bfor\s+opening\b", 'It is for opening cans.', 'Serve para abrir latas.', 'For! 🥫'), ('Usei so that?', r"\bso\s+that\s+you\b", 'I speak slowly so that you understand.', 'Falo devagar para que você entenda.', 'So that! 🗣️')]),
    ('🦁', 'Fixas', 'Use what for, just in case e on purpose', 'Fale. **Diga para quê, por precaução e de propósito.**', 'just in case', 'What is it for? Take it just in case. He did it on purpose.',
     [('Disse what for?', r"\bwhat\s+is\s+it\s+for\b", 'What is it for?', 'Para que serve?', 'For! ❓'), ('Disse just in case?', r"\bjust\s+in\s+case\b", 'Take it just in case.', 'Leve por precaução.', 'Case! 🎒'), ('Disse on purpose?', r"\bon\s+purpose\b", 'He did it on purpose.', 'Ele fez de propósito.', 'Purpose! 🎯')]),
    [('🔪', 'use it to', 'usar para', 'I use it to cut bread.', 'Eu uso para cortar pão.'), ('🥫', 'for -ing', 'serve para', 'It is for opening cans.', 'Serve para abrir latas.'), ('🗣️', 'so that', 'para que', 'I speak slowly so that you understand.', 'Falo devagar para que você entenda.'), ('🛣️', 'road', 'estrada', 'The road is long.', 'A estrada é longa.'), ('💬', 'say', 'dizer', 'Say it slowly.', 'Diga devagar.')],
    [('I use it ___ cut bread.', 'Eu uso para cortar pão.', ['to', 'for', 'at'], 0, 'use it **to** cut.'), ('It is for ___ cans.', 'Serve para abrir latas.', ['opening', 'open', 'to open'], 0, 'for + **-ing**.'), ('I speak slowly so ___ you understand.', 'Falo devagar para que você entenda.', ['that', 'to', 'for'], 0, 'so **that**.'), ('The ___ is long.', 'A estrada é longa.', ['road', 'roads is', 'roading'], 0, 'the **road**.')],
    [('Qual frase está certa?', ['It is for cutting bread.', 'It is for cut bread.', 'It is for to cut bread.'], 0, 'for + -ing.'), ('Qual está certa?', ['I use it to cut bread.', 'I use it for cut bread.', 'I use it cutting to bread.'], 0, 'to + verbo.')],
    [['Man', 'What is this tool for?', 'Para que serve esta ferramenta?'], ['Girl', 'It is for opening cans.', 'Serve para abrir latas.'], ['Man', 'And this knife?', 'E esta faca?'], ['Girl', 'I use it to cut bread.', 'Eu uso para cortar pão.'],
     ['Man', 'Say it slowly.', 'Diga devagar.'], ['Girl', 'I speak slowly so that you understand.', 'Falo devagar para que você entenda.'], ['Man', 'Take a bag just in case.', 'Leve uma sacola por precaução.'], ['Girl', 'Good idea.', 'Boa ideia.']],
    [('What is the tool for?', 'Para que serve a ferramenta?', [('🥫', 'Opening cans'), ('🍞', 'Cutting bread'), ('🔨', 'Hitting nails')], 0, 1, 'Diz: “for opening cans.”'), ('What is the knife for?', 'Para que serve a faca?', [('🍞', 'Cutting bread'), ('🥫', 'Opening cans'), ('🔩', 'Fixing')], 0, 3, 'Diz: “to cut bread.”'),
     ('Why does she speak slowly?', 'Por que fala devagar?', [('👂', 'So he understands'), ('😴', 'She is tired'), ('📞', 'On the phone')], 0, 5, 'Diz: “so that you understand.”')],
    [('❓', 'What for?', 'Para quê?', 'perguntar finalidade', 'What is it for?', 'Para que serve?'), ('🎒', 'Just in case', 'Por precaução', 'prevenção', 'Take it just in case.', 'Leve por precaução.'), ('🎯', 'On purpose', 'De propósito', 'intencional', 'He did it on purpose.', 'Ele fez de propósito.'), ('🧰', 'Come in handy', 'Ser útil', 'servir', 'It will come in handy.', 'Vai ser útil.')]))

# ---------- 271 / 272 · movimento ----------
MV_VOCAB = [('🚗', 'get in', 'entrar (carro)', 'Soa como “GUÉT IN”.'), ('🚪', 'get out', 'sair', 'Soa como “GUÉT ÁUT”.'), ('🚌', 'get on', 'subir (ônibus)', 'Soa como “GUÉT ÓN”.'),
            ('🚏', 'get off', 'descer', 'Soa como “GUÉT ÓF”.'), ('🚓', 'pull over', 'encostar', 'Soa como “PUL ÔU-ver”.'), ('🧳', 'set off', 'partir', 'Soa como “SÉT ÓF”.')]
MV_LAB = dict(short='mv', title='Laboratório de sons: get in, get off e set off', pt='g soa g; e soa é; off soa óf.', tip='Em off, o o soa ó.',
              words=[('get', 'GUÉT', 'pegar', 'e = é', 'gate', 'GUÊIT'), ('off', 'ÓF', 'fora', 'o = ó', 'oaf', 'ÔUF'), ('set', 'SÉT', 'pôr', 'e = é', 'seat', 'SIT')])
MV_VERBS = [('get', '🚗', 'entrar', 'Get in the car.', 'Get on the car.', 'I got in.', 'Entrei.', 'car = get **in**.'),
            ('get', '🚌', 'subir', 'Get on the bus.', 'Get in the bus.', 'I got on.', 'Subi.', 'bus = get **on**.'),
            ('get', '🚏', 'descer', 'Get off the bus.', 'Get out the bus.', 'I got off.', 'Desci.', 'bus = get **off**.'),
            ('set', '🧳', 'partir', 'We set off early.', 'We set on early.', 'I set off.', 'Parti.', 'set **off**.')]
MV_RULE = ('Movimento', 'Carro: in/out. Ônibus/trem: on/off.', 'Em português “entre no carro”. Em inglês: **get in the car**. “Suba no ônibus”: **get on the bus**.')
MV_FM = [('Carro', 'Get', 'in the car.', 'Get in the car.', 'carro = in/out.'), ('Ônibus', 'Get', 'on the bus.', 'Get on the bus.', 'ônibus = on/off.')]
MV_TRAPS = [('Qual frase está certa?', ['Get in the car.', 'Get on the car.', 'Get at the car.'], 0, 'carro = in.'), ('Qual está certa?', ['Get on the bus.', 'Get in the bus.', 'Get at the bus.'], 0, 'ônibus = on.')]

EPS.append(mk(82175, 'Phrasal Verbs of Movement', "usar verbos de movimento com partículas: get in, get out, get on, get off, pull over, set off",
    "movimento: get in/out · get on/off · pull over · set off", "Hoje você aprende verbos de movimento: Get in the car. Get on the bus. Get off here. We set off early.",
    ('Man', 'Woman'), ['tom', 'polly'], 'street', 'Planes, Trains and Automobiles', ['street', 'pier', 'park2', 'lobby1', 'cafe2', 'hall'],
    ('Phrasal Verbs of Movement: em 10 minutos você entra, sai, sobe e desce em inglês', 'Na rua, o homem e a mulher pegam carro e ônibus para viajar.'), ('Mais movimento', 'Próximo: Phrasal verbs de movimento'),
    MV_RULE, MV_FM, MV_VOCAB, MV_LAB, MV_VERBS,
    [('Get in/out', 'Get', 'entre', [(' in the car.', ' no carro.'), (' out of the car.', ' para fora do carro.'), (' in quickly.', ' rápido.')]), ('Get on/off', 'Get', 'suba', [(' on the bus.', ' no ônibus.'), (' off the bus.', ' (desça) do ônibus.'), (' on the train.', ' no trem.')]), ('Set off', 'We set off', 'nós partimos', [(' early.', ' cedo.'), (' at six.', ' às seis.'), (' for Paris.', ' para Paris.')])],
    ('🚗', 'Viagem', 'Use get in, get on e set off', 'Fale. **Diga entre no carro, suba no ônibus e partimos cedo.**', 'set off', 'Get in the car. Get on the bus. We set off early.',
     [('Usei get in?', r"\bget\s+in\s+the\s+car\b", 'Get in the car.', 'Entre no carro.', 'In! 🚗'), ('Usei get on?', r"\bget\s+on\s+the\s+bus\b", 'Get on the bus.', 'Suba no ônibus.', 'On! 🚌'), ('Usei set off?', r"\bset\s+off\b", 'We set off early.', 'Partimos cedo.', 'Off! 🧳')]),
    ('🚌', 'Fixas', 'Use on the way, miss the bus e hit the road', 'Fale. **Diga no caminho, perder o ônibus e pegar a estrada.**', 'hit the road', 'We are on the way. I missed the bus. Let us hit the road.',
     [('Disse on the way?', r"\bon\s+the\s+way\b", 'We are on the way.', 'Estamos a caminho.', 'Way! 🛣️'), ('Disse miss the bus?', r"\bmissed\s+the\s+bus\b", 'I missed the bus.', 'Perdi o ônibus.', 'Missed! 🚌'), ('Disse hit the road?', r"\bhit\s+the\s+road\b", 'Let us hit the road.', 'Vamos pegar a estrada.', 'Road! 🚗')]),
    [('🚗', 'get in', 'entrar (carro)', 'Get in the car.', 'Entre no carro.'), ('🚪', 'get out', 'sair', 'Get out of the car.', 'Saia do carro.'), ('🚌', 'get on', 'subir', 'Get on the bus.', 'Suba no ônibus.'), ('🚏', 'get off', 'descer', 'Get off the bus.', 'Desça do ônibus.'), ('🧳', 'set off', 'partir', 'We set off early.', 'Partimos cedo.')],
    [('Get ___ the car.', 'Entre no carro.', ['in', 'on', 'at'], 0, 'carro = **in**.'), ('Get ___ the bus.', 'Suba no ônibus.', ['on', 'in', 'at'], 0, 'ônibus = **on**.'), ('Get ___ at the next stop.', 'Desça na próxima parada.', ['off', 'out to', 'down in'], 0, 'get **off**.'), ('We set ___ early.', 'Partimos cedo.', ['off', 'up to', 'in'], 0, 'set **off**.')],
    MV_TRAPS,
    [['Man', 'Get in the car quickly.', 'Entre no carro rápido.'], ['Woman', 'We set off early today.', 'Partimos cedo hoje.'], ['Man', 'Pull over here. I need to get out.', 'Encoste aqui. Preciso sair.'], ['Woman', 'The bus is coming. Get on.', 'O ônibus está vindo. Suba.'],
     ['Man', 'Where do we get off?', 'Onde descemos?'], ['Woman', 'At the pier.', 'No cais.'], ['Man', 'Let us hit the road.', 'Vamos pegar a estrada.'], ['Woman', 'Okay.', 'Certo.']],
    [('What must they get into?', 'No que devem entrar?', [('🚗', 'The car'), ('🚌', 'The bus'), ('🚆', 'The train')], 0, 0, 'Diz: “Get in the car.”'), ('When do they set off?', 'Quando partem?', [('🌅', 'Early'), ('🌙', 'Late'), ('☀️', 'At noon')], 0, 1, 'Diz: “set off early.”'),
     ('Where do they get off?', 'Onde descem?', [('⛴️', 'At the pier'), ('🏫', 'At school'), ('🏠', 'At home')], 0, 5, 'Diz: “At the pier.”')],
    [('🛣️', 'On the way', 'A caminho', 'trajeto', 'We are on the way.', 'Estamos a caminho.'), ('🚌', 'Miss the bus', 'Perder o ônibus', 'chegar tarde', 'I missed the bus.', 'Perdi o ônibus.'), ('🚗', 'Hit the road', 'Pegar a estrada', 'partir', 'Let us hit the road.', 'Vamos pegar a estrada.'), ('🧳', 'See off', 'Despedir-se de alguém', 'acompanhar partida', 'I saw him off.', 'Eu me despedi dele.')]))

EPS.append(mk(7082175, 'Phrasal verbs de movimento', "phrasal verbs de movimento: pull up, pull away, drop off, pick up (set off, get on, get off)",
    "movimento 2: drop off · pick up · pull up · see off", "Hoje você pratica: I will drop you off. She picked me up. The taxi pulled up. We saw them off.",
    ('Girl', 'Man'), ['polly', 'tom'], 'street', 'Planes, Trains and Automobiles', ['street', 'pier', 'lobby1', 'park2', 'cafe2', 'hall'],
    ('Phrasal verbs de movimento: em 10 minutos você pede carona e combina buscar', 'Na rua, a menina e o homem combinam quem leva e quem busca.'), ('Mais movimento', 'Próximo: Phrasal verbs com look'),
    ('Levar e buscar', 'Drop off e pick up.', 'Em português “eu te deixo lá”. Em inglês: **I will drop you off**.'),
    [('Drop off', 'I will', 'drop you off.', 'I will drop you off.', 'drop you off.'), ('Pick up', 'She', 'picked me up.', 'She picked me up.', 'pick me up.')],
    MV_VOCAB, MV_LAB, MV_VERBS,
    [('Drop off', 'I will drop', 'eu vou deixar', [(' you off.', ' você lá.'), (' her off.', ' ela lá.'), (' them off.', ' eles lá.')]), ('Pick up', 'She picked', 'ela buscou', [(' me up.', ' eu.'), (' him up.', ' ele.'), (' us up.', ' a gente.')]), ('See off', 'We saw', 'nós nos despedimos de', [(' them off.', ' eles.'), (' her off.', ' ela.'), (' him off.', ' ele.')])],
    ('🚕', 'Carona', 'Use drop off, pick up e pull up', 'Fale. **Diga eu te deixo lá, ela me buscou e o táxi parou.**', 'pick up', 'I will drop you off. She picked me up. The taxi pulled up.',
     [('Usei drop off?', r"\bdrop\s+you\s+off\b", 'I will drop you off.', 'Eu te deixo lá.', 'Drop! 🚕'), ('Usei pick up?', r"\bpicked\s+me\s+up\b", 'She picked me up.', 'Ela me buscou.', 'Pick! 🧍'), ('Usei pull up?', r"\bpulled\s+up\b", 'The taxi pulled up.', 'O táxi parou.', 'Pull! 🚖')]),
    ('🚌', 'Fixas', 'Use give someone a lift, catch a ride e door to door', 'Fale. **Diga dar carona, pegar carona e porta a porta.**', 'give a lift', 'Can you give me a lift? I caught a ride. It is door to door.',
     [('Disse give a lift?', r"\bgive\s+me\s+a\s+lift\b", 'Can you give me a lift?', 'Pode me dar carona?', 'Lift! 🚗'), ('Disse catch a ride?', r"\bcaught\s+a\s+ride\b", 'I caught a ride.', 'Peguei carona.', 'Ride! 🚕'), ('Disse door to door?', r"\bdoor\s+to\s+door\b", 'It is door to door.', 'É porta a porta.', 'Door! 🚪')]),
    [('🚕', 'drop off', 'deixar', 'I will drop you off.', 'Eu te deixo lá.'), ('🧍', 'pick up', 'buscar', 'She picked me up.', 'Ela me buscou.'), ('🚖', 'pull up', 'parar', 'The taxi pulled up.', 'O táxi parou.'), ('👋', 'see off', 'despedir-se', 'We saw them off.', 'Nos despedimos deles.'), ('🧳', 'set off', 'partir', 'We set off at six.', 'Partimos às seis.')],
    [('I will drop you ___.', 'Eu te deixo lá.', ['off', 'out to', 'on'], 0, 'drop you **off**.'), ('She picked me ___.', 'Ela me buscou.', ['up', 'down', 'at'], 0, 'picked me **up**.'), ('The taxi pulled ___.', 'O táxi parou.', ['up', 'for', 'to'], 0, 'pulled **up**.'), ('We saw them ___.', 'Nos despedimos deles.', ['off', 'over', 'in'], 0, 'saw them **off**.')],
    [('Qual frase está certa?', ['I will drop you off.', 'I will drop off you.', 'I will dropping you off.'], 0, 'drop you off.'), ('Qual está certa?', ['She picked me up.', 'She picked up me.', 'She pick me up.'], 0, 'picked me up.')],
    [['Girl', 'Can you give me a lift?', 'Pode me dar carona?'], ['Man', 'Sure. I will pick you up at six.', 'Claro. Busco você às seis.'], ['Girl', 'And then drop me off at the pier?', 'E depois me deixa no cais?'], ['Man', 'Yes. It is door to door.', 'Sim. É porta a porta.'],
     ['Girl', 'Look! The taxi pulled up.', 'Olhe! O táxi parou.'], ['Man', 'Let us see them off.', 'Vamos nos despedir deles.'], ['Girl', 'Okay.', 'Certo.'], ['Man', 'Thanks for coming.', 'Obrigado por vir.']],
    [('What does she ask for?', 'O que ela pede?', [('🚗', 'A lift'), ('💰', 'Money'), ('🍽️', 'Food')], 0, 0, 'Diz: “give me a lift.”'), ('When does he pick her up?', 'Quando ele a busca?', [('6️⃣', 'At six'), ('8️⃣', 'At eight'), ('🔟', 'At ten')], 0, 1, 'Diz: “at six.”'),
     ('Where does he drop her off?', 'Onde a deixa?', [('⛴️', 'At the pier'), ('🏫', 'At school'), ('🏠', 'At home')], 0, 2, 'Diz: “drop me off at the pier.”')],
    [('🚗', 'Give a lift', 'Dar carona', 'oferecer', 'Can you give me a lift?', 'Pode me dar carona?'), ('🚕', 'Catch a ride', 'Pegar carona', 'aceitar', 'I caught a ride.', 'Peguei carona.'), ('🚪', 'Door to door', 'Porta a porta', 'completo', 'It is door to door.', 'É porta a porta.'), ('👋', 'See someone off', 'Despedir-se', 'acompanhar partida', 'I saw him off.', 'Eu me despedi dele.')]))

# ---------- 273 / 274 · look ----------
LK_VOCAB = [('📖', 'look up', 'procurar', 'Soa como “LUK ÂP”.'), ('🐕', 'look after', 'cuidar de', 'Soa como “LUK ÉF-ter”.'), ('⚠️', 'look out', 'cuidado', 'Soa como “LUK ÁUT”.'),
            ('🎉', 'look forward to', 'esperar ansioso', 'Soa como “LUK FÓR-uerd tu”.'), ('🔎', 'look for', 'procurar', 'Soa como “LUK FÓR”.'), ('🕵️', 'look into', 'investigar', 'Soa como “LUK ÍN-tu”.')]
LK_LAB = dict(short='lk', title='Laboratório de sons: look, after e forward', pt='oo soa u curto; a soa é; or soa ór.', tip='Em look, o oo é curto.',
              words=[('look', 'LUK', 'olhar', 'oo = u', 'luck', 'LÂK'), ('after', 'ÉF-ter', 'depois', 'a = é', 'offer', 'Ó-fer'), ('forward', 'FÓR-uerd', 'adiante', 'or = ór', 'fervid', 'FÂR-vid')])
LK_VERBS = [('look', '📖', 'procurar', 'I look up new words.', 'I look new words up in.', 'I looked.', 'Procurei.', 'look **up** (dicionário).'),
            ('look', '🐕', 'cuidar', 'She looks after the dog.', 'She looks at the dog after.', 'I looked.', 'Cuidei.', 'look **after**.'),
            ('look', '⚠️', 'cuidar', 'Look out!', 'Look in!', 'I looked.', 'Olhei.', 'look **out**!'),
            ('look', '🎉', 'esperar', 'I look forward to it.', 'I look forward it.', 'I looked.', 'Esperei.', 'look forward **to**.')]

def lk(n, title, sub, pat, why, names, ids, rs, scenes, cover, teaser, rule, fm, mold, prod, m2, hot, gaps, traps, lines, quiz, exps):
    return mk(n, title, sub, pat, why, names, ids, rs, "Charlotte's Web", scenes, cover, teaser, rule, fm, LK_VOCAB, LK_LAB, LK_VERBS, mold, prod, m2, hot, gaps, traps, lines, quiz, exps)

EPS.append(lk(82176, 'Look Up, Look After', "aprender phrasal verbs com look: look up, look after, look out, look forward to, look for, look into",
    "phrasal verbs: look up · look after · look out · look forward to", "Hoje você aprende phrasal verbs com look: I look up new words. She looks after the pig. Look out! I look forward to it.",
    ('Girl', 'Man'), ['polly', 'tom'], 'park', ['park', 'yard', 'cafe2', 'living', 'home1', 'school'],
    ('Look Up, Look After: em 10 minutos você domina seis usos de look', 'Na fazenda, a menina e o homem cuidam de um porquinho.'), ('Mais com look', 'Próximo: Phrasal verbs com look'),
    ('Look', 'Seis sentidos novos.', 'Em português “procuro no dicionário”. Em inglês: **I look it up**.'),
    [('Look up', 'I', 'look up new words.', 'I look up new words.', 'look up.'), ('Look after', 'She', 'looks after the pig.', 'She looks after the pig.', 'look after.')],
    [('Look up', 'I look up', 'eu procuro', [(' new words.', ' palavras novas.'), (' the meaning.', ' o significado.'), (' the time.', ' o horário.')]), ('Look after', 'She looks after', 'ela cuida de', [(' the pig.', ' porquinho.'), (' the children.', ' as crianças.'), (' the farm.', ' a fazenda.')]), ('Look forward to', 'I look forward to', 'espero ansioso por', [(' it.', ' isso.'), (' the party.', ' a festa.'), (' seeing you.', ' ver você.')])],
    ('👀', 'Look', 'Use look up, look after e look forward to', 'Fale. **Diga eu procuro palavras novas, ela cuida do porquinho e espero ansioso por isso.**', 'look after', 'I look up new words. She looks after the pig. I look forward to it.',
     [('Usei look up?', r"\blook\s+up\b", 'I look up new words.', 'Eu procuro palavras novas.', 'Up! 📖'), ('Usei look after?', r"\blooks?\s+after\b", 'She looks after the pig.', 'Ela cuida do porquinho.', 'After! 🐕'), ('Usei look forward to?', r"\blook\s+forward\s+to\b", 'I look forward to it.', 'Espero ansioso por isso.', 'Forward! 🎉')]),
    ('🔎', 'Fixas', 'Use look out, look alike e look on the bright side', 'Fale. **Diga cuidado, parecidos e olhe o lado bom.**', 'look on the bright side', 'Look out! They look alike. Look on the bright side.',
     [('Disse look out?', r"\blook\s+out\b", 'Look out!', 'Cuidado!', 'Out! ⚠️'), ('Disse look alike?', r"\blook\s+alike\b", 'They look alike.', 'Eles são parecidos.', 'Alike! 👯'), ('Disse bright side?', r"\bbright\s+side\b", 'Look on the bright side.', 'Olhe o lado bom.', 'Bright! ☀️')]),
    [('📖', 'look up', 'procurar', 'I look up new words.', 'Eu procuro palavras novas.'), ('🐕', 'look after', 'cuidar de', 'She looks after the pig.', 'Ela cuida do porquinho.'), ('⚠️', 'look out', 'cuidado', 'Look out!', 'Cuidado!'), ('🎉', 'look forward to', 'esperar ansioso', 'I look forward to it.', 'Espero ansioso por isso.'), ('🔎', 'look for', 'procurar', 'I look for my keys.', 'Procuro minhas chaves.')],
    [('I look ___ new words.', 'Eu procuro palavras novas.', ['up', 'at', 'in'], 0, 'look **up**.'), ('She looks ___ the pig.', 'Ela cuida do porquinho.', ['after', 'at', 'out'], 0, 'look **after**.'), ('Look ___!', 'Cuidado!', ['out', 'in', 'to'], 0, 'look **out**.'), ('I look forward ___ it.', 'Espero ansioso por isso.', ['to', 'for', 'at'], 0, 'look forward **to**.')],
    [('Qual frase está certa?', ['She looks after the pig.', 'She looks at after the pig.', 'She look after the pig.'], 0, 'looks after.'), ('Qual está certa?', ['I look forward to it.', 'I look forward it.', 'I look forward for it.'], 0, 'forward to.')],
    [['Girl', 'Who looks after the pig?', 'Quem cuida do porquinho?'], ['Man', 'I do. I look after him every day.', 'Eu. Cuido dele todo dia.'], ['Girl', 'Look out! He is running.', 'Cuidado! Ele está correndo.'], ['Man', 'I look for his food.', 'Procuro a comida dele.'],
     ['Girl', 'I look up new words in a dictionary.', 'Procuro palavras novas no dicionário.'], ['Man', 'Good habit.', 'Bom hábito.'], ['Girl', 'I look forward to the fair.', 'Espero ansiosa pela feira.'], ['Man', 'Me too.', 'Eu também.']],
    [('Who looks after the pig?', 'Quem cuida do porquinho?', [('👨', 'The man'), ('👧', 'The girl'), ('👵', 'Grandma')], 0, 1, 'Diz: “I look after him.”'), ('What does she look up?', 'O que ela procura?', [('📖', 'New words'), ('🔑', 'Keys'), ('🐷', 'The pig')], 0, 4, 'Diz: “look up new words.”'),
     ('What does she look forward to?', 'Pelo que espera?', [('🎡', 'The fair'), ('🏫', 'School'), ('🍰', 'Cake')], 0, 6, 'Diz: “the fair.”')],
    [('⚠️', 'Look out', 'Cuidado', 'alertar', 'Look out!', 'Cuidado!'), ('👯', 'Look alike', 'Ser parecido', 'comparar', 'They look alike.', 'Eles são parecidos.'), ('☀️', 'Look on the bright side', 'Olhar o lado bom', 'otimismo', 'Look on the bright side.', 'Olhe o lado bom.'), ('🔎', 'Look into', 'Investigar', 'examinar', 'I will look into it.', 'Vou investigar.')]))

EPS.append(lk(7082176, 'Phrasal verbs com look', "mais phrasal verbs com look: look over, look down on, look up to, look through (look for, look into)",
    "phrasal verbs: look over · look through · look down on · look up to", "Hoje você aprende mais quatro com look: Look over the form. Look through the book. Do not look down on him. I look up to her.",
    ('Man', 'Woman'), ['tom', 'polly'], 'school', ['school', 'cafe2', 'office', 'hall', 'park', 'living'],
    ('Phrasal verbs com look: em 10 minutos você revisa, folheia e admira', 'Na escola, o homem e a mulher revisam um formulário e falam de quem admiram.'), ('Mais com look', 'Próximo: Phrasal verbs com take'),
    ('Look', 'Mais quatro sentidos.', 'Em português “dê uma olhada”. Em inglês: **look over**.'),
    [('Look over', 'Look over', 'the form.', 'Look over the form.', 'look over.'), ('Look up to', 'I look up to', 'her.', 'I look up to her.', 'look up to.')],
    [('Look over', 'Look over', 'revise', [(' the form.', ' o formulário.'), (' my work.', ' meu trabalho.'), (' the list.', ' a lista.')]), ('Look through', 'Look through', 'folheie', [(' the book.', ' o livro.'), (' the papers.', ' os papéis.'), (' the files.', ' os arquivos.')]), ('Look up to', 'I look up to', 'eu admiro', [(' her.', ' ela.'), (' my teacher.', ' meu professor.'), (' my parents.', ' meus pais.')])],
    ('🧐', 'Look', 'Use look over, look through e look up to', 'Fale. **Diga revise o formulário, folheie o livro e eu admiro ela.**', 'look up to', 'Look over the form. Look through the book. I look up to her.',
     [('Usei look over?', r"\blook\s+over\b", 'Look over the form.', 'Revise o formulário.', 'Over! 🧐'), ('Usei look through?', r"\blook\s+through\b", 'Look through the book.', 'Folheie o livro.', 'Through! 📚'), ('Usei look up to?', r"\blook\s+up\s+to\b", 'I look up to her.', 'Eu admiro ela.', 'Up to! 🌟')]),
    ('🔎', 'Fixas', 'Use look down on, look into e look the part', 'Fale. **Diga olhar de cima, investigar e ter a pinta.**', 'look the part', 'Do not look down on him. I will look into it. You look the part.',
     [('Disse look down on?', r"\blook\s+down\s+on\b", 'Do not look down on him.', 'Não o olhe de cima.', 'Down! 👎'), ('Disse look into?', r"\blook\s+into\s+it\b", 'I will look into it.', 'Vou investigar.', 'Into! 🕵️'), ('Disse look the part?', r"\blook\s+the\s+part\b", 'You look the part.', 'Você tem a pinta.', 'Part! 🎭')]),
    [('🧐', 'look over', 'revisar', 'Look over the form.', 'Revise o formulário.'), ('📚', 'look through', 'folhear', 'Look through the book.', 'Folheie o livro.'), ('🌟', 'look up to', 'admirar', 'I look up to her.', 'Eu admiro ela.'), ('👎', 'look down on', 'desprezar', 'Do not look down on him.', 'Não o despreze.'), ('🕵️', 'look into', 'investigar', 'I will look into it.', 'Vou investigar.')],
    [('Look ___ the form.', 'Revise o formulário.', ['over', 'to', 'by'], 0, 'look **over**.'), ('Look ___ the book.', 'Folheie o livro.', ['through', 'for', 'at'], 0, 'look **through**.'), ('I look up ___ her.', 'Eu admiro ela.', ['to', 'at', 'for'], 0, 'look up **to**.'), ('Do not look ___ on him.', 'Não o despreze.', ['down', 'up', 'out'], 0, 'look **down** on.')],
    [('Qual frase está certa?', ['I look up to her.', 'I look to up her.', 'I look up her to.'], 0, 'look up to.'), ('Qual está certa?', ['Do not look down on him.', 'Do not look on down him.', 'Do not look down him on.'], 0, 'look down on.')],
    [['Man', 'Please look over this form.', 'Por favor, revise este formulário.'], ['Woman', 'Okay. I will look through the papers too.', 'Certo. Vou folhear os papéis também.'], ['Man', 'Who do you look up to?', 'Quem você admira?'], ['Woman', 'I look up to my teacher.', 'Admiro minha professora.'],
     ['Man', 'Do not look down on anyone.', 'Não despreze ninguém.'], ['Woman', 'Never. I will look into the mistake.', 'Nunca. Vou investigar o erro.'], ['Man', 'You look the part.', 'Você tem a pinta.'], ['Woman', 'Thank you!', 'Obrigada!']],
    [('What must she look over?', 'O que deve revisar?', [('📄', 'The form'), ('🍰', 'The cake'), ('🚗', 'The car')], 0, 0, 'Diz: “look over this form.”'), ('Who does she look up to?', 'Quem ela admira?', [('👩‍🏫', 'Her teacher'), ('👮', 'A guard'), ('🐶', 'A dog')], 0, 3, 'Diz: “look up to my teacher.”'),
     ('What will she look into?', 'O que vai investigar?', [('❌', 'The mistake'), ('🏠', 'The house'), ('🌳', 'The tree')], 0, 5, 'Diz: “look into the mistake.”')],
    [('👎', 'Look down on', 'Desprezar', 'julgar', 'Do not look down on him.', 'Não o despreze.'), ('🕵️', 'Look into', 'Investigar', 'examinar', 'I will look into it.', 'Vou investigar.'), ('🎭', 'Look the part', 'Ter a pinta', 'combinar', 'You look the part.', 'Você tem a pinta.'), ('👀', 'Look back', 'Relembrar', 'passado', 'I look back with joy.', 'Relembro com alegria.')]))
