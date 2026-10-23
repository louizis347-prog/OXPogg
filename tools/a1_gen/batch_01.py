# Lote 01: posições 6 a 13 do A1 (n do brief, na ordem).
# TROCAS DE OBRA: pos 6: de Dracula: The Castle para The Addams Family
# TROCAS DE OBRA: pos 8: de Gulliver's Travels: Too Big para The Polar Express
# TROCAS DE OBRA: pos 9: de Little Italy para It's a Small World
# TROCAS DE OBRA: pos 10: de Rebecca: The Housekeeper para Harry Potter and the Sorcerer's Stone
# TROCAS DE OBRA: pos 11: de Vila Sésamo para Scrabble
# TROCAS DE OBRA: pos 12: de The Hobbit: The Quest para Zootopia
# TROCAS DE OBRA: pos 13: de Home, Sweet Home para Eloise
# (pos 7 mantém Coming to America)


# ------------------------------------------------------------ ajudantes
def vc(w, pt, snd):
    return [w, pt, 'Soa como “%s”.' % snd]


def qz(q, pt, opts, a, line, why):
    return dict(q=q, pt=pt, opts=[list(o) for o in opts], a=a, line=line, why=why)


def gp(q, pt, opts, a, why):
    return dict(q=q, pt=pt, opts=opts, a=a, why=why)


def tr(opts, a, why, q='Qual frase está certa?'):
    return dict(q=q, opts=opts, a=a, why=why)


def hot(e, x, y, en, pt, say, sayPt):
    return dict(e=e, x=x, y=y, en=en, pt=pt, say=say, sayPt=sayPt)


def xp(ic, en, tag, pt, use, exen, expt):
    return dict(ic=ic, en=en, tag=tag, pt=pt, use=use, ex=[exen, expt])


def rd(say, opts, a, why):
    return dict(fig='🎧', say=say, ask='Qual palavra você ouviu?', opts=opts, a=a, why=why)


def hn(say, opts, a, why, pic=False):
    d = dict(fig='🎧', say=say, ask='Ouça e toque na figura.' if pic else 'Ouça e toque na palavra.',
             opts=[[o, ''] for o in opts] if pic else opts, a=a, why=why)
    if pic:
        d['pic'] = 1
    return d


def vb(v, ic, pt, f1, f2, exen, expt, s):
    return dict(v=v, ic=ic, pt=pt, f=[['eu', f1], ['ele/ela', f2]], ex=[exen, expt],
                note='**%s** = %s. Com he/she: **%s**.' % (v, pt, s))


def cx(text, pt, right, w1, w2):
    return dict(text=text, pt=pt, opts=[right, w1, w2], a=0)


def rs(*s):
    keys = 'review dquiz rdg pat vplay build order soundlab produce wrap dictate'.split()
    assert len(s) == 11
    return dict(zip(keys, s))


def mission(ic, name, desc, prompt, chips, model, check, kw, tips, ok, reply):
    return dict(ic=ic, name=name, desc=desc, data=dict(
        prompt=prompt, ph='Escreva a sua resposta aqui…', chips=chips, model=model,
        check=check, kw=kw, tips=tips, ok=ok, reply=reply))


PH = 'Escreva a sua resposta aqui…'


# ============================================================ POS 6 · The Addams Family
def ep06():
    GOMEZ = 'p:short:1a1a1a:e8d5c4:222222:none:suit'
    MORT = 'p:long:111111:e8d5c4:1a1a1a:none:dress'
    WED = 'p:long:1a1a1a:e8d5c4:2d3748:bow:dress'
    PUGS = 'p:short:3b2a1a:e8d5c4:7a7a7a:none:shirt'
    B = dict(
        title='Foto de família · He\'s / She\'s',
        sub='Falar de uma pessoa com He\'s e She\'s: He is → He\'s, She is → She\'s',
        pattern_label="He's / She's",
        why='Hoje você aprende a apresentar a família com He\'s e She\'s, como a Wednesday faz na foto da família Addams.',
        vocab=[vc('Photo', 'Foto', 'FÔ-tou'), vc('Family', 'Família', 'FÉ-mli'), vc('Mother', 'Mãe', 'MÂ-dhâr'),
               vc('Father', 'Pai', 'FÁ-dhâr'), vc('Brother', 'Irmão', 'BRÂ-dhâr'), vc('Sister', 'Irmã', 'SÍS-târ'),
               vc('Uncle', 'Tio', 'ÂN-kôl')],
        balloons=[['📷', 'photo'], ['👪', 'family'], ['👩', 'mother'], ['👨', 'father'], ['👦', 'brother'], ['👴', 'uncle']],
        cover_art=dict(s='castlehall', items=[['📷', 104, 56, 20, 'bob'], ['🕷️', 138, 44, 12, 'bob'], ['🖼️', 84, 34, 12, 'bob']], seed='ad6'),
        cover_sub="He's / She's: em 10 minutos você apresenta a família como a Wednesday",
        cover_say='A Wednesday mostra uma foto de família ao irmão. Quem é ele? E ela? Como dizer isso em inglês?',
        wrap_recap=[["He's my father.", 'Ele é o meu pai.'], ["She's my mother.", 'Ela é a minha mãe.'],
                    ["He's tall.", 'Ele é alto.'], ["She's pretty.", 'Ela é bonita.']],
        teaser=dict(t='Where Are You From?', d='Próximo padrão: Where are you from? e I’m from…'),
        cast={'Wednesday': ['👧', '#2d3748'], 'Pugsley': ['👦', '#b7791f'], 'Gomez': ['🧔', '#6b46c1']},
        lines=[
            ['Wednesday', 'Look, Pugsley! A family photo!', 'Olhe, Pugsley! Uma foto de família!'],
            ['Pugsley', "He's tall. Is he Dad?", 'Ele é alto. É o papai?'],
            ['Wednesday', "Yes, he is. He's Gomez. He's happy.", 'Sim. Ele é o Gomez. Ele está feliz.'],
            ['Pugsley', "And she's pretty. Is she Mom?", 'E ela é bonita. É a mamãe?'],
            ['Gomez', "Yes, she is! She's Morticia, my wife.", 'Sim! Ela é a Morticia, minha esposa.'],
            ['Wednesday', "And he's Uncle Fester. He's bald.", 'E ele é o tio Fester. Ele é careca.'],
            ['Gomez', "He's funny. We love Fester!", 'Ele é engraçado. Nós adoramos o Fester!'],
            ['Pugsley', "It's a nice photo. Say cheese!", 'É uma bela foto. Digam xis!']],
        quiz=[
            qz('Who is Gomez?', 'Quem é o Gomez?', [('👴', 'The uncle'), ('👦', 'The brother'), ('👨', 'The father')], 2, 2,
               'Wednesday diz: “He’s Gomez.” Pugsley perguntou se ele é o pai.'),
            qz('Who is bald?', 'Quem é careca?', [('👨', 'Gomez'), ('👴', 'Uncle Fester'), ('👩', 'Morticia')], 1, 5,
               'Wednesday diz: “He’s Uncle Fester. He’s bald.”'),
            qz('Who is Morticia?', 'Quem é a Morticia?', [('👩', 'The mother'), ('👧', 'The sister'), ('👵', 'The grandma')], 0, 4,
               'Gomez diz: “She’s Morticia, my wife.” Ela é a mãe.')],
        rdg_q=dict(q='Como se diz “Ela é bonita”?', o=["He's pretty.", "She's pretty.", 'She pretty.'], a=1,
                   why='Para uma mulher, use **She\'s** (She is). Em inglês a frase precisa do verbo.'),
        dictate=[["He's my father.", 'Ele é meu pai.'], ["She's my mother.", 'Ela é minha mãe.'],
                 ["He's my brother.", 'Ele é meu irmão.'], ["She's pretty.", 'Ela é bonita.']],
        produce=dict(
            prompt='A Wednesday mostra a foto: *Who is he? Who is she?* **Diga quem são duas pessoas da sua família com He\'s e She\'s e diga como elas são (tall, happy, funny…).**',
            ph='Ex.: He\'s my father. He\'s tall. She\'s my sister. She\'s funny.',
            chips=["He's my…", "She's my…", "He's tall."],
            model="He's my father. He's tall. She's my sister. She's funny.",
            check=['Falei de um homem com He\'s?', 'Falei de uma mulher com She\'s?', 'Disse como a pessoa é?'],
            kw=["\\bhe(?:['’]s| is)\\b", "\\bshe(?:['’]s| is)\\b", '\\b(?:tall|happy|funny|pretty|nice|old|young|bald|kind)\\b'],
            tips=[[["He's my father.", 'Ele é meu pai.'], ["He's my brother.", 'Ele é meu irmão.']],
                  [["She's my mother.", 'Ela é minha mãe.'], ["She's my sister.", 'Ela é minha irmã.']],
                  [["He's tall.", 'Ele é alto.'], ["She's funny.", 'Ela é engraçada.']]],
            ok=['Ele, certo! 👨', 'Ela, certo! 👩', 'Boa descrição! 😊'],
            reply=['What a nice family! Say cheese!', 'Que família simpática! Digam xis!']),
        rs=rs('garden', 'castlehall', 'library', 'bookshop', 'museum', 'hotelroom', 'bakery', 'musicroom', 'forest', 'christmas', 'beach'),
        sc='museum')
    X = dict(
        n=7030001, review=True, names=('Wednesday', 'Pugsley'),
        stage=dict(rs='castlehall', chars=[[WED, 28, 0, 1.0], [PUGS, 56, 1, 1.0], [GOMEZ, 84, 1, 0.95]]),
        obra=dict(name='The Addams Family', kind='📺 Série de TV · 1964', year='1964',
                  text='Série de TV americana de 1964, baseada nos desenhos humorísticos de Charles Addams, publicados na revista The New Yorker desde 1938. Mostra uma família estranha e muito unida, que adora tudo o que é sombrio.',
                  line=['This is our family photo.', 'Esta é a nossa foto de família.'],
                  pa=dict(t='haunted', e=['🕷️', '🖼️', '🦇'], p='e', v=0)),
        gancho=['Wednesday', 'Look, Pugsley! A family photo!', 'Olhe, Pugsley! Uma foto de família!'],
        hot=[hot('📷', 12, 18, 'photo', 'foto', 'This is a family photo.', 'Esta é uma foto de família.'),
             hot('🖼️', 40, 12, 'picture', 'quadro', "He's in the picture.", 'Ele está no quadro.'),
             hot('🕷️', 66, 14, 'spider', 'aranha', "She's a small spider.", 'Ela é uma aranha pequena.'),
             hot('🕯️', 88, 16, 'candle', 'vela', "It's a black candle. She's happy.", 'É uma vela preta. Ela está feliz.'),
             hot('🪑', 12, 82, 'chair', 'cadeira', "He's in the chair.", 'Ele está na cadeira.')],
        gap=[gp('___ my mother.', 'Ela é minha mãe.', ["She's", "He's", 'Her'], 0, 'Mãe é mulher: **She\'s** (She is).'),
             gp('___ tall.', 'Ele é alto.', ['He', 'Hes', "He's"], 2, 'He is → **He\'s**, com apóstrofo.'),
             gp('She ___ happy.', 'Ela está feliz.', ['are', 'is', 'am'], 1, 'Com **she**, o verbo é **is**.'),
             gp('That man is my uncle. ___ funny.', 'Aquele homem é meu tio. Ele é engraçado.', ["She's", "He's", "I'm"], 1, 'Tio é homem: **He\'s** funny.')],
        trap=[tr(["He's my mother.", "She's my mother.", 'She my mother.'], 1, 'Mãe é mulher: **She\'s**. E a frase precisa do verbo.'),
              tr(["He's pretty.", 'She pretty.', "She's pretty."], 2, 'Sem o verbo fica errado: **She\'s** pretty.', 'Como dizer “Ela é bonita”?')],
        sticker=dict(title='Wednesday e Pugsley', sub='The Addams Family · 1964', rs='castlehall', chars=[[WED, 34, 0, 1.0], [PUGS, 68, 1, 1.0]]),
        speakers={'Wednesday': WED, 'Pugsley': PUGS, 'Gomez': GOMEZ},
        rule=dict(
            who=WED, head="He's / She's", sub='A forma curta de He is e She is.',
            say=["She's my mother.", 'Ela é minha mãe.'],
            formula=[dict(from_=[['He', 0], ['is', 1], ['tall.', 3]], to=[["He's", 0], ['tall.', 3]], say="He's tall.",
                          note='**He is** vira **He’s** para um homem ou menino.'),
                     dict(from_=[['She', 2], ['is', 1], ['pretty.', 3]], to=[["She's", 2], ['pretty.', 3]], say="She's pretty.",
                          note='**She is** vira **She’s** para uma mulher ou menina.')],
            uses=[dict(ico='👨', tag='Pai', en="He's my father.", pt='Ele é meu pai.'),
                  dict(ico='👩', tag='Mãe', en="She's my mother.", pt='Ela é minha mãe.'),
                  dict(ico='😊', tag='Como é', en="She's happy.", pt='Ela está feliz.')],
            rules=[dict(tag="He's", c=0, text='Para **um homem ou menino**: He is → He’s.', ex="He's my brother."),
                   dict(tag="She's", c=2, text='Para **uma mulher ou menina**: She is → She’s.', ex="She's my sister."),
                   dict(tag='Com verbo', c=1, text='Em inglês a frase precisa de **is**. Sem He’s/She’s fica errado.', ex='✗ She pretty  →  ✓ She’s pretty')],
            tips=['Em português basta dizer “é bonita”. Em inglês sempre aparece **he** ou **she**: She’s pretty.']),
        mission_ic='📷')
    XT = dict(
        exp=[xp('📸', 'Say cheese!', 'Informal', 'Digam xis!', 'O que se diz ao **tirar uma foto**, para todo mundo sorrir.', 'Everybody, say cheese!', 'Pessoal, digam xis!'),
             xp('🚪', 'Come on in!', 'Expressão', 'Entre!', 'Para **receber alguém** em casa de forma simpática.', 'Come on in, Uncle Fester!', 'Entre, tio Fester!'),
             xp('🛋️', 'Make yourself at home.', 'Expressão', 'Fique à vontade.', 'Para o visitante **se sentir em casa**.', 'Sit down. Make yourself at home.', 'Sente-se. Fique à vontade.'),
             xp('👋', 'Long time no see!', 'Informal', 'Quanto tempo!', 'Ao ver **alguém depois de muito tempo**.', 'Long time no see, Gomez!', 'Quanto tempo, Gomez!')],
        exp_scene=dict(rs='garden', lines=[
            ['Wednesday', 'The door! It\'s Uncle Fester.', 'A porta! É o tio Fester.'],
            ['Gomez', '**Long time no see**, Fester! **Come on in**!', 'Quanto tempo, Fester! Entre!'],
            ['Pugsley', '**Make yourself at home**, Uncle!', 'Fique à vontade, tio!'],
            ['Wednesday', 'Wait! A family photo. **Say cheese**!', 'Esperem! Uma foto de família. Digam xis!'],
            ['Gomez', 'Cheese! He\'s happy.', 'Xis! Ele está feliz.'],
            ['Pugsley', 'Yes! He\'s happy, she\'s happy.', 'Sim! Ele está feliz, ela está feliz.']]),
        lab=dict(
            short='final -er', title='Laboratório de sons: o final -er de sister',
            say='Em inglês, as palavras da família terminam em -er: sister, brother, mother. Esse final é bem fraquinho!',
            intro=dict(what='O final **-er** de **sister**, **mother** e **brother** é um som fraco e rápido, parecido com “âr”.',
                       how='Não diga “sistér” com força. A sílaba forte é a primeira: SÍS-târ. O final é curto, com a língua um pouco para trás.',
                       pt='Em português o final -er (mulher, colher) é forte e aberto. Em inglês a força fica no começo da palavra e o fim some.'),
            ex=[['sister', 'SÍS-târ', 'irmã', 'a força fica no “SIS”'], ['brother', 'BRÂ-dhâr', 'irmão', 'final curto, sem “ér”'],
                ['mother', 'MÂ-dhâr', 'mãe', 'o “th” é suave, com a língua entre os dentes']],
            pairs=[['mother', 'mud', 'mãe × lama: mother termina em -er fraco; mud termina em “d”'],
                   ['father', 'farm', 'pai × fazenda'], ['brother', 'broth', 'irmão × caldo']],
            tip='Diga a primeira sílaba bem forte e deixe o final cair: SÍS-târ, MÂ-dhâr.',
            phrase=['She\'s my sister. He\'s my brother.', 'Ela é minha irmã. Ele é meu irmão.'],
            rounds=[rd('mother', ['mother', 'mud'], 0, '**mother** (mãe) termina em -er fraco. **Mud** (lama) termina em “d”.'),
                    rd('father', ['farm', 'father'], 1, '**father** (pai) tem dois sons: “FÁ-dhâr”. **Farm** (fazenda) é uma sílaba só.'),
                    rd('brother', ['brother', 'broth'], 0, '**brother** (irmão) tem duas sílabas. **Broth** (caldo) tem uma.')]),
        hunt=[hn('mud', ['mother', 'mud'], 1, '**mud** (lama) é uma sílaba só.'),
              hn('father', ['🚜', '👨', '🍲'], 1, '**father** = pai.', True),
              hn('broth', ['brother', 'broth'], 1, '**broth** (caldo) tem uma sílaba.'),
              hn('farm', ['farm', 'father'], 0, '**farm** (fazenda) tem uma sílaba.'),
              hn('brother', ['🍲', '👦', '🥣'], 1, '**brother** = irmão.', True)])
    VB = dict(title='Verbos da família Addams', tip='Quatro verbos: play, watch, carry e tell.', items=[
        vb('play', '🎲', 'brincar, jogar', 'I play with my sister.', 'Pugsley play**s** in the garden.', 'I play with my sister.', 'Eu brinco com a minha irmã.', 'plays'),
        vb('watch', '👀', 'assistir, observar', 'I watch the family.', 'Wednesday watch**es** the spider.', 'I watch the family.', 'Eu observo a família.', 'watches'),
        vb('carry', '🧺', 'carregar', 'I carry the photo.', 'He carr**ies** the photo.', 'I carry the photo.', 'Eu carrego a foto.', 'carries'),
        vb('tell', '🗣️', 'contar', 'I tell a story.', 'She tell**s** a story.', 'I tell a story.', 'Eu conto uma história.', 'tells')])
    MR = dict(
        mold=[dict(label='Ele é… (família)', slots=[
                   dict(cat='ele', opts=[["He's", 'ele é']]),
                   dict(cat='quem', opts=[['my father', 'meu pai'], ['my brother', 'meu irmão'], ['my uncle', 'meu tio'], ['Gomez', 'o Gomez']])], end=['.', '.']),
              dict(label='Ela é… (família)', slots=[
                   dict(cat='ela', opts=[["She's", 'ela é']]),
                   dict(cat='quem', opts=[['my mother', 'minha mãe'], ['my sister', 'minha irmã'], ['my aunt', 'minha tia'], ['Morticia', 'a Morticia']])], end=['.', '.']),
              dict(label='Como ele/ela é', slots=[
                   dict(cat='quem', opts=[["He's", 'ele é'], ["She's", 'ela é']]),
                   dict(cat='como', opts=[['tall', 'alto(a)'], ['happy', 'feliz'], ['funny', 'engraçado(a)'], ['pretty', 'bonito(a)'], ['bald', 'careca']])], end=['.', '.'])],
        speak=[["He's tall. He's funny.", 'Ele é alto. Ele é engraçado.'], ["She's my sister. She's happy.", 'Ela é minha irmã. Ela está feliz.']],
        trap=[dict(ask='“Say cheese!” é dito quando…', opts=['alguém tira uma foto', 'alguém pede comida', 'alguém vai dormir'], a=0, why='**Say cheese!** faz todo mundo sorrir na foto.', say='Say cheese!'),
              dict(ask='“Long time no see!” quer dizer…', opts=['Boa noite!', 'Quanto tempo!', 'Até logo!'], a=1, why='**Long time no see!** = quanto tempo (sem se ver).', say='Long time no see!')],
        gap=[dict(text='Come ___ in!', pt='Entre!', opts=['on', 'at', 'to'], a=0, why='**Come on in!** = entre!', say='Come on in!'),
             dict(text='Make yourself at ___.', pt='Fique à vontade.', opts=['home', 'house', 'door'], a=0, why='**at home** = à vontade, como em casa.', say='Make yourself at home.')],
        expq=[dict(ask='Um tio chega e você não o vê há anos.', opts=['Long time no see!', 'Say cheese!', 'Make yourself at home.'], a=0, why='**Long time no see!** = quanto tempo!'),
              dict(ask='Você vai tirar uma foto da família.', opts=['Come on in!', 'Long time no see!', 'Say cheese!'], a=2, why='**Say cheese!** na hora da foto.'),
              dict(ask='Seu amigo entra na sua casa e está sem jeito.', opts=['Make yourself at home.', 'Say cheese!', 'Long time no see!'], a=0, why='**Make yourself at home.** = fique à vontade.')],
        missions=[
            mission('👪', 'Minha família', 'Fale de duas pessoas da família.',
                    'Mostre uma foto sua. **Diga quem é um homem e quem é uma mulher da sua família, com He\'s e She\'s.**',
                    ["He's my…", "She's my…"], "He's my father. She's my sister.",
                    ['Usei He\'s para um homem?', 'Usei She\'s para uma mulher?', 'Disse quem eles são na família?'],
                    ["\\bhe(?:['’]s| is)\\b", "\\bshe(?:['’]s| is)\\b", '\\bmy (?:father|dad|mother|mom|brother|sister|uncle|aunt|grandma|grandpa|cousin)\\b'],
                    [[["He's my father.", 'Ele é meu pai.']], [["She's my sister.", 'Ela é minha irmã.']], [['my mother', 'minha mãe'], ['my uncle', 'meu tio']]],
                    ['He’s certo! 👨', 'She’s certo! 👩', 'Família completa! 👪'],
                    ['What a nice family!', 'Que família simpática!']),
            mission('🚪', 'Visita em casa', 'Receba um amigo com as expressões.',
                    'Um amigo chega à sua casa. **Cumprimente com “Long time no see”, peça para ele entrar e diga para ficar à vontade.**',
                    ['Come on in!'], 'Long time no see! Come on in! Make yourself at home.',
                    ['Disse “Long time no see”?', 'Pedi para entrar?', 'Pedi para ficar à vontade?'],
                    ['\\blong time no see\\b', '\\bcome on in\\b', '\\bmake yourself at home\\b'],
                    [[['Long time no see!', 'Quanto tempo!']], [['Come on in!', 'Entre!']], [['Make yourself at home.', 'Fique à vontade.']]],
                    ['Quanto tempo! 👋', 'Porta aberta! 🚪', 'Muito simpático! 🛋️'],
                    ['Thanks! You have a nice home.', 'Obrigado! Você tem uma casa bonita.'])])
    CX = [cx('We look at it and say "cheese". It\'s a family ___.', 'Olhamos para ela e dizemos “xis”. É uma foto de família.', 'photo', 'uncle', 'brother'),
          cx('Mom, Dad and the kids: that is a happy ___.', 'Mamãe, papai e os filhos: essa é uma família feliz.', 'family', 'photo', 'sister'),
          cx('She is my mom. She is my ___.', 'Ela é minha mamãe. Ela é a minha mãe.', 'mother', 'uncle', 'photo'),
          cx('He is my dad. He is my ___.', 'Ele é o meu papai. Ele é o meu pai.', 'father', 'sister', 'family'),
          cx('He is my mom\'s brother. He is my ___.', 'Ele é o irmão da minha mãe. Ele é o meu tio.', 'uncle', 'father', 'photo'),
          cx('She has the same parents as me. She is my ___.', 'Ela tem os mesmos pais que eu. Ela é a minha irmã.', 'sister', 'mother', 'uncle')]
    return dict(B=B, X=X, XT=XT, VB=VB, MR=MR, CX=CX)


# ============================================================ POS 7 · Coming to America
def ep07():
    LISA = 'p:curly:2b1b12:8d5524:e67e22:none:dress'
    AKEEM = 'p:short:1a1a1a:5c3a21:8e44ad:crown:suit'
    SEMMI = 'p:short:111111:5c3a21:c0392b:none:shirt'
    B = dict(
        title='Where Are You From? · I\'m from…',
        sub='Perguntar e dizer de onde você é: Brazil, Mexico, country, city',
        pattern_label='Where are you from?',
        why='Hoje você aprende a perguntar Where are you from? e a responder I\'m from…, como o príncipe Akeem ao chegar em Nova York.',
        vocab=[vc('Where', 'Onde', 'UÉR'), vc('Country', 'País', 'KÂN-tri'), vc('City', 'Cidade', 'SÍ-ti'),
               vc('Plane', 'Avião', 'PLÊIN'), vc('Brazil', 'Brasil', 'bra-ZÍL'), vc('Mexico', 'México', 'MÉK-si-kou')],
        balloons=[['🌍', 'country'], ['🏙️', 'city'], ['✈️', 'plane'], ['🇧🇷', 'Brazil'], ['🇲🇽', 'Mexico'], ['📍', 'where']],
        cover_art=dict(s='busstop', items=[['✈️', 104, 56, 20, 'bob'], ['🌍', 138, 44, 12, 'bob'], ['🏙️', 84, 34, 12, 'bob']], seed='ca7'),
        cover_sub='Where are you from? Em 10 minutos você diz de onde é, como o príncipe Akeem',
        cover_say='O príncipe Akeem chega a Nova York. Uma moça pergunta de onde ele é. Como perguntar e responder?',
        wrap_recap=[['Where are you from?', 'De onde você é?'], ["I'm from Brazil.", 'Eu sou do Brasil.'],
                    ['Brazil is a country.', 'O Brasil é um país.'], ['New York is a city.', 'Nova York é uma cidade.']],
        teaser=dict(t='Na fila do embarque', d='Próximo padrão: Are you ready? Are you cold? e as respostas curtas'),
        cast={'Lisa': ['👩', '#d97706'], 'Akeem': ['🤴', '#7c3aed'], 'Semmi': ['🧑', '#2f855a']},
        lines=[
            ['Lisa', 'Hi! Where are you from?', 'Oi! De onde você é?'],
            ['Akeem', "I'm from Zamunda. It's a country in Africa.", 'Eu sou de Zamunda. É um país na África.'],
            ['Semmi', "I'm from Zamunda, too. This city is big!", 'Eu também sou de Zamunda. Esta cidade é grande!'],
            ['Lisa', "Welcome! I'm from here. I'm from Queens.", 'Bem-vindos! Eu sou daqui. Sou do Queens.'],
            ['Akeem', 'Queens? Is that a country?', 'Queens? Isso é um país?'],
            ['Lisa', "No, it isn't! It's a city.", 'Não! É uma cidade.'],
            ['Akeem', 'A country, a city… Now I know!', 'Um país, uma cidade… Agora eu sei!'],
            ['Semmi', "I'm tired. It's a long plane trip!", 'Estou cansado. É uma viagem longa de avião!']],
        quiz=[
            qz('Where is Akeem from?', 'De onde o Akeem é?', [('🇲🇽', 'Mexico'), ('🌍', 'Zamunda'), ('🇧🇷', 'Brazil')], 1, 1,
               'Akeem diz: “I’m from Zamunda.”'),
            qz('What is Queens?', 'O que é Queens?', [('🌍', 'A country'), ('🏙️', 'A city'), ('✈️', 'A plane')], 1, 5,
               'Lisa diz: “It’s a city.”'),
            qz('Who is tired?', 'Quem está cansado?', [('🧑', 'Semmi'), ('👩', 'Lisa'), ('🤴', 'Akeem')], 0, 7,
               'Semmi diz: “I’m tired.”')],
        rdg_q=dict(q='Como se responde “Where are you from?”', o=["I'm from Brazil.", 'I from Brazil.', "I'm of Brazil."], a=0,
                   why='Use **I\'m from** + lugar. Em inglês é **from**, nunca “of”.'),
        dictate=[['Where are you from?', 'De onde você é?'], ["I'm from Brazil.", 'Eu sou do Brasil.'],
                 ['Are you from Mexico?', 'Você é do México?'], ["It's a big city.", 'É uma cidade grande.']],
        produce=dict(
            prompt='Lisa pergunta: *Where are you from?* **Diga de onde você é com I\'m from…, diga se o lugar é um país ou uma cidade e pergunte de onde ela é.**',
            ph="Ex.: I'm from Brazil. Brazil is a country. Where are you from?",
            chips=["I'm from…", 'country', 'Where are you from?'],
            model="I'm from Brazil. Brazil is a big country. Where are you from?",
            check=['Disse de onde sou com I\'m from?', 'Falei de um país ou de uma cidade?', 'Perguntei de onde ela é?'],
            kw=["\\bI(?:['’]m| am) from\\b", '\\b(?:country|city)\\b', '\\bwhere are you from\\b'],
            tips=[[["I'm from Brazil.", 'Eu sou do Brasil.'], ["I'm from Recife.", 'Eu sou de Recife.']],
                  [['Brazil is a country.', 'O Brasil é um país.'], ['Recife is a city.', 'Recife é uma cidade.']],
                  [['Where are you from?', 'De onde você é?']]],
            ok=['I’m from! 🙋', 'País ou cidade! 🌍', 'Boa pergunta! ❓'],
            reply=["I'm from Queens. Nice to meet you!", 'Eu sou do Queens. Prazer em conhecer você!']),
        rs=rs('harbor', 'busstop', 'bookshop', 'nightcity', 'supermarket', 'airport', 'pharmacy', 'stadium', 'bank', 'zoo', 'fishing'),
        sc='nightcity')
    X = dict(
        n=9802, review=True, names=('Lisa', 'Akeem'),
        stage=dict(rs='busstop', chars=[[LISA, 28, 0, 1.0], [AKEEM, 56, 1, 1.0], [SEMMI, 84, 1, 0.95]]),
        obra=dict(name='Coming to America', kind='🎬 Filme · 1988', year='1988',
                  text='Comédia americana de 1988, dirigida por John Landis e estrelada por Eddie Murphy. O príncipe Akeem, de um país imaginário chamado Zamunda, viaja até o bairro do Queens, em Nova York, para encontrar uma esposa.',
                  line=['Where are you from?', 'De onde você é?'],
                  pa=dict(t='plaza', e=['✈️', '👑', '🏙️'], p='f', v=1)),
        gancho=['Lisa', 'Hi! Where are you from?', 'Oi! De onde você é?'],
        hot=[hot('✈️', 12, 18, 'plane', 'avião', "I'm from Brazil. I'm in a plane.", 'Eu sou do Brasil. Estou num avião.'),
             hot('🏙️', 40, 14, 'city', 'cidade', "I'm from a big city.", 'Eu sou de uma cidade grande.'),
             hot('🌍', 66, 14, 'country', 'país', 'Brazil is a country.', 'O Brasil é um país.'),
             hot('🇲🇽', 88, 16, 'Mexico', 'México', "Ana is from Mexico.", 'A Ana é do México.'),
             hot('🇧🇷', 12, 82, 'Brazil', 'Brasil', "I'm from Brazil.", 'Eu sou do Brasil.')],
        gap=[gp('Where ___ you from?', 'De onde você é?', ['is', 'are', 'do'], 1, 'Com **you**, o verbo é **are**: Where **are** you from?'),
             gp("I'm ___ Brazil.", 'Eu sou do Brasil.', ['from', 'of', 'in'], 0, 'Em inglês: I\'m **from** + lugar.'),
             gp('Chicago is a ___.', 'Chicago é uma cidade.', ['country', 'plane', 'city'], 2, '**city** = cidade.'),
             gp('Mexico is a ___.', 'O México é um país.', ['plane', 'country', 'city'], 1, '**country** = país.')],
        trap=[tr(['Where you are from?', 'Where are you from?', 'From where you are?'], 1, 'O verbo vem logo depois de Where: Where **are** you from?'),
              tr(["I'm of Brazil.", 'I from Brazil.', "I'm from Brazil."], 2, 'Use **I\'m from**. “De” em inglês é **from**, não “of”.')],
        sticker=dict(title='Akeem e Lisa', sub='Coming to America · 1988', rs='busstop', chars=[[AKEEM, 34, 0, 1.0], [LISA, 68, 1, 1.0]]),
        speakers={'Lisa': LISA, 'Akeem': AKEEM, 'Semmi': SEMMI},
        rule=dict(
            who=LISA, head='Where are you from?', sub='Para perguntar e dizer de onde você é.',
            say=['Hi! Where are you from?', 'Oi! De onde você é?'],
            formula=[dict(from_=[['You', 0], ['are', 1], ['from', 2], ['Brazil.', 3]], to=[['Where', 3], ['are', 1], ['you', 0], ['from?', 2]],
                          say='Where are you from?', note='**Where** abre a pergunta, **are** vem antes de **you** e **from** fica no final.'),
                     dict(from_=[['I', 0], ['am', 1], ['from', 2], ['Brazil.', 3]], to=[["I'm", 0], ['from', 2], ['Brazil.', 3]],
                          say="I'm from Brazil.", note='Na resposta, **I am** vira **I’m**: I’m from + lugar.')],
            uses=[dict(ico='❓', tag='Perguntar', en='Where are you from?', pt='De onde você é?'),
                  dict(ico='🇧🇷', tag='País', en="I'm from Brazil.", pt='Eu sou do Brasil.'),
                  dict(ico='🏙️', tag='Cidade', en="I'm from New York.", pt='Eu sou de Nova York.')],
            rules=[dict(tag='Where are you', c=0, text='Pergunta: **Where are you from?** O **from** fica no fim.', ex='Where are you from?'),
                   dict(tag="I'm from", c=1, text='Resposta: **I’m from** + país ou cidade.', ex="I'm from Mexico."),
                   dict(tag='from, não of', c=2, text='“De” de origem é **from**.', ex='✗ I\'m of Brazil  →  ✓ I\'m from Brazil')],
            tips=['Em português perguntamos “De onde você é?”. Em inglês o **from** vai para o final: Where are you **from**?']),
        mission_ic='🌍')
    XT = dict(
        exp=[xp('🗽', 'Welcome to New York!', 'Expressão', 'Bem-vindo a Nova York!', 'Para **receber** alguém em um lugar. Troque o nome da cidade.', 'Welcome to New York, Akeem!', 'Bem-vindo a Nova York, Akeem!'),
             xp('🤝', 'Nice to meet you.', 'Expressão', 'Prazer em conhecer você.', 'Ao **conhecer alguém** pela primeira vez.', 'Nice to meet you, Lisa.', 'Prazer em conhecer você, Lisa.'),
             xp('🏙️', 'What a big city!', 'Informal', 'Que cidade grande!', 'Quando você **se surpreende** com o tamanho de um lugar.', 'What a big city!', 'Que cidade grande!'),
             xp('🙌', 'Me too!', 'Informal', 'Eu também!', 'Para dizer que **você sente o mesmo** que outra pessoa.', "I'm tired. Me too!", 'Estou cansado. Eu também!')],
        exp_scene=dict(rs='nightcity', lines=[
            ['Lisa', '**Welcome to New York**! I\'m Lisa.', 'Bem-vindo a Nova York! Eu sou a Lisa.'],
            ['Akeem', '**Nice to meet you**, Lisa! I\'m Akeem.', 'Prazer em conhecer você, Lisa! Eu sou o Akeem.'],
            ['Lisa', 'Is it your first day here?', 'É o seu primeiro dia aqui?'],
            ['Akeem', 'Yes, it is. **What a big city**!', 'Sim, é. Que cidade grande!'],
            ['Semmi', "I'm tired and hungry.", 'Estou cansado e com fome.'],
            ['Lisa', '**Me too**! Let\'s eat!', 'Eu também! Vamos comer!']]),
        lab=dict(
            short='i curto × i longo', title='Laboratório de sons: o “i” de city e de meet',
            say='Em inglês existem dois sons de “i”. Um é curto e outro é longo. Vamos treinar com as palavras da viagem do Akeem!',
            intro=dict(what='O **i curto** de **city**, **big** e **ship** é rápido e relaxado. O **i longo** de **meet**, **sheep** e **leave** é esticado, com o sorriso aberto.',
                       how='No i longo, abra um pequeno sorriso e segure o som: “MIIT”. No i curto, deixe a boca solta e solte rápido: “BÍG”.',
                       pt='Em português só temos um “i”. Por isso brasileiros dizem **sheep** (ovelha) e **ship** (navio) iguais. A diferença muda o sentido!'),
            ex=[['city', 'SÍ-ti', 'cidade', 'i curto e rápido'], ['big', 'BÍG', 'grande', 'boca solta, som curto'], ['meet', 'MIIT', 'encontrar', 'sorriso e som esticado']],
            pairs=[['ship', 'sheep', 'navio × ovelha'], ['bit', 'beat', 'pedacinho × batida'], ['live', 'leave', 'morar × sair']],
            tip='Para o i longo, sorria e estique o som. Para o i curto, relaxe a boca e seja rápido.',
            phrase=['I live in a big city.', 'Eu moro numa cidade grande.'],
            rounds=[rd('sheep', ['ship', 'sheep'], 1, '**sheep** (ovelha) tem i longo. **Ship** (navio) tem i curto.'),
                    rd('bit', ['bit', 'beat'], 0, '**bit** (pedacinho) tem i curto. **Beat** (batida) tem i longo.'),
                    rd('leave', ['live', 'leave'], 1, '**leave** (sair) tem i longo. **Live** (morar) tem i curto.')]),
        hunt=[hn('ship', ['ship', 'sheep'], 0, '**ship** (navio) tem i curto.'),
              hn('sheep', ['🚢', '🐑', '🏙️'], 1, '**sheep** = ovelha.', True),
              hn('beat', ['bit', 'beat'], 1, '**beat** (batida) tem i longo.'),
              hn('live', ['live', 'leave'], 0, '**live** (morar) tem i curto.'),
              hn('ship', ['🐑', '🏙️', '🚢'], 2, '**ship** = navio.', True)])
    VB = dict(title='Verbos de viagem', tip='Quatro verbos: travel, arrive, visit e come.', items=[
        vb('travel', '🧳', 'viajar', 'I travel by plane.', 'Akeem travel**s** to New York.', 'I travel by plane.', 'Eu viajo de avião.', 'travels'),
        vb('arrive', '🛬', 'chegar', 'I arrive in the city.', 'Semmi arrive**s** tired.', 'I arrive in the city.', 'Eu chego na cidade.', 'arrives'),
        vb('visit', '🗽', 'visitar', 'I visit Mexico.', 'She visit**s** Brazil.', 'I visit Mexico.', 'Eu visito o México.', 'visits'),
        vb('come', '🚶', 'vir, ser de', 'I come from Brazil.', 'He come**s** from Zamunda.', 'I come from Brazil.', 'Eu venho do Brasil.', 'comes')])
    MR = dict(
        mold=[dict(label='De onde você é?', slots=[
                   dict(cat='frase', opts=[["I'm from", 'eu sou de']]),
                   dict(cat='lugar', opts=[['Brazil', 'Brasil'], ['Mexico', 'México'], ['Zamunda', 'Zamunda'], ['Queens', 'Queens'], ['New York', 'Nova York'], ['Africa', 'África']])], end=['.', '.']),
              dict(label='Você é de…?', slots=[
                   dict(cat='pergunta', opts=[['Are you from', 'você é de']]),
                   dict(cat='lugar', opts=[['Brazil', 'Brasil'], ['Mexico', 'México'], ['Queens', 'Queens'], ['New York', 'Nova York']])], end=['?', '?']),
              dict(label='País ou cidade?', slots=[
                   dict(cat='lugar', opts=[['Brazil', 'Brasil'], ['Mexico', 'México'], ['Zamunda', 'Zamunda']]),
                   dict(cat='o que é', opts=[['is a country', 'é um país'], ['is a big country', 'é um país grande'], ['is far', 'fica longe']])], end=['.', '.'])],
        speak=[["Welcome to New York! Nice to meet you.", 'Bem-vindo a Nova York! Prazer em conhecer você.'], ["I'm tired. Me too!", 'Estou cansado. Eu também!']],
        trap=[dict(ask='“Me too!” quer dizer…', opts=['Eu também!', 'Eu não!', 'Para mim!'], a=0, why='**Me too!** = eu também!', say='Me too!'),
              dict(ask='Qual frase é uma boas-vindas?', opts=['Nice to meet you.', 'Welcome to New York!', 'What a big city!'], a=1, why='**Welcome to…!** = bem-vindo a…!', say='Welcome to New York!')],
        gap=[dict(text='Nice to ___ you.', pt='Prazer em conhecer você.', opts=['meet', 'know', 'see'], a=0, why='**Nice to meet you.** é a frase pronta.', say='Nice to meet you.'),
             dict(text='What a ___ city!', pt='Que cidade grande!', opts=['big', 'plane', 'Brazil'], a=0, why='**big** = grande.', say='What a big city!')],
        expq=[dict(ask='Você acabou de conhecer uma pessoa.', opts=['Me too!', 'Nice to meet you.', 'What a big city!'], a=1, why='**Nice to meet you.** ao conhecer alguém.'),
              dict(ask='Seu amigo diz: “I’m hungry.” Você também está.', opts=['Welcome to New York!', 'Nice to meet you.', 'Me too!'], a=2, why='**Me too!** = eu também.'),
              dict(ask='Você chega a uma cidade enorme e fica surpreso.', opts=['What a big city!', 'Me too!', 'Welcome to New York!'], a=0, why='**What a big city!** mostra surpresa.')],
        missions=[
            mission('🌍', 'De onde você é?', 'Diga de onde você é e pergunte ao outro.',
                    'Você conhece uma pessoa nova. **Diga de onde você é, diga se o lugar é um país ou uma cidade e pergunte de onde ela é.**',
                    ["I'm from…"], "I'm from Brazil. It's a big country. Where are you from?",
                    ['Disse de onde sou?', 'Falei de país ou cidade?', 'Perguntei de onde ela é?'],
                    ["\\bI(?:['’]m| am) from\\b", '\\b(?:country|city)\\b', '\\bwhere are you from\\b'],
                    [[["I'm from Brazil.", 'Eu sou do Brasil.']], [["It's a country.", 'É um país.'], ["It's a city.", 'É uma cidade.']], [['Where are you from?', 'De onde você é?']]],
                    ['Origem dita! 🙋', 'País ou cidade! 🌍', 'Boa pergunta! ❓'],
                    ["I'm from Queens. Welcome!", 'Eu sou do Queens. Bem-vindo!']),
            mission('🗽', 'Boas-vindas', 'Receba alguém na sua cidade.',
                    'Um turista chega à sua cidade. **Dê as boas-vindas, diga que é um prazer conhecê-lo e diga que a cidade é grande.**',
                    ['Welcome to…'], 'Welcome to São Paulo! Nice to meet you. It is a big city!',
                    ['Dei as boas-vindas?', 'Disse “Nice to meet you”?', 'Falei que a cidade é grande?'],
                    ['\\bwelcome to\\b', '\\bnice to meet you\\b', '\\bbig city\\b'],
                    [[['Welcome to Brazil!', 'Bem-vindo ao Brasil!']], [['Nice to meet you.', 'Prazer em conhecer você.']], [['It is a big city.', 'É uma cidade grande.']]],
                    ['Boas-vindas! 🗽', 'Prazer! 🤝', 'Cidade grande! 🏙️'],
                    ['Thank you! What a big city!', 'Obrigado! Que cidade grande!'])])
    CX = [cx('Brazil, Mexico and Peru are each a ___.', 'Brasil, México e Peru são, cada um, um país.', 'country', 'city', 'plane'),
          cx('New York has tall buildings and many people. It is a big ___.', 'Nova York tem prédios altos e muita gente. É uma cidade grande.', 'city', 'country', 'plane'),
          cx('To go from Brazil to the U.S. fast, I take a ___.', 'Para ir do Brasil aos EUA rápido, eu pego um avião.', 'plane', 'city', 'country'),
          cx('Samba, Carnival and football: I\'m from ___.', 'Samba, Carnaval e futebol: eu sou do Brasil.', 'Brazil', 'Mexico', 'where'),
          cx('Tacos, mariachi and Mexico City: I\'m from ___.', 'Tacos, mariachi e a Cidade do México: eu sou do México.', 'Mexico', 'Brazil', 'plane'),
          cx('___ are you from? I\'m from Queens.', 'De onde você é? Eu sou do Queens.', 'Where', 'City', 'Plane')]
    return dict(B=B, X=X, XT=XT, VB=VB, MR=MR, CX=CX)


# ============================================================ POS 8 · The Polar Express
def ep08():
    BOY = 'p:short:5a3a1a:f4c7a1:2b6cb0:none:shirt'
    GIRL = 'p:long:8b5a2b:f4c7a1:c0392b:scarf:dress'
    COND = 'p:short:777777:f4c7a1:1a365d:hat:suit'
    B = dict(
        title='Na fila do embarque · Are you…?',
        sub='Are you ready? Are you cold? Perguntas com sentimentos e respostas curtas',
        pattern_label='Are you ready / cold…?',
        why='Hoje você aprende a perguntar como a pessoa está (ready, cold, hungry, scared) e a responder, como na fila do Expresso Polar.',
        vocab=[vc('Ticket', 'Bilhete', 'TÍ-kit'), vc('Train', 'Trem', 'TRÊIN'), vc('Ready', 'Pronto(a)', 'RÉ-di'),
               vc('Cold', 'Com frio, frio', 'KÔULD'), vc('Hungry', 'Com fome', 'RÂN-gri'), vc('Scared', 'Com medo', 'SKÉRD'),
               vc('Chocolate', 'Chocolate', 'TCHÓK-lit')],
        balloons=[['🎫', 'ticket'], ['🚂', 'train'], ['✅', 'ready'], ['🥶', 'cold'], ['😋', 'hungry'], ['😨', 'scared']],
        cover_art=dict(s='traincar', items=[['🚂', 104, 56, 20, 'bob'], ['🎫', 138, 44, 12, 'bob'], ['❄️', 84, 34, 12, 'bob']], seed='pe8'),
        cover_sub='Are you ready? Em 10 minutos você pergunta como a pessoa está, como no trem do Polo Norte',
        cover_say='É noite de Natal e um trem mágico espera na neve. O maquinista pergunta: você está pronto? Como perguntar e responder?',
        wrap_recap=[['Are you ready?', 'Você está pronto?'], ['Are you cold?', 'Você está com frio?'],
                    ['Yes, I am. / No, I\'m not.', 'Sim, estou. / Não, não estou.'], ["I'm hungry, too.", 'Eu também estou com fome.']],
        teaser=dict(t='Is He From Japan?', d='Próximo padrão: Is he…? e Is she…? para perguntar sobre os outros'),
        cast={'Boy': ['👦', '#2b6cb0'], 'Girl': ['👧', '#c0392b'], 'Conductor': ['🎩', '#1a365d']},
        lines=[
            ['Conductor', 'All aboard! Are you ready?', 'Todos a bordo! Vocês estão prontos?'],
            ['Boy', 'Yes, I am! Look, my ticket!', 'Sim, estou! Olhe, o meu bilhete!'],
            ['Conductor', 'Good! Are you cold? It is cold outside.', 'Ótimo! Você está com frio? Está frio lá fora.'],
            ['Boy', "No, I'm not. But I'm a little scared.", 'Não, não estou. Mas estou com um pouco de medo.'],
            ['Girl', "Are you scared? I'm a little scared, too.", 'Você está com medo? Eu também estou com um pouco de medo.'],
            ['Boy', 'Are you hungry? I am!', 'Você está com fome? Eu estou!'],
            ['Conductor', 'Hot chocolate for everyone!', 'Chocolate quente para todos!'],
            ['Girl', "Yes, please! I'm not scared now.", 'Sim, por favor! Agora não estou com medo.']],
        quiz=[
            qz('Who is hungry?', 'Quem está com fome?', [('🧒', 'The Girl'), ('👦', 'The Boy'), ('🎩', 'The Conductor')], 1, 5,
               'O menino diz: “Are you hungry? I am!”'),
            qz('Is the Boy cold?', 'O menino está com frio?', [('✅', 'Yes, he is'), ('❌', "No, he isn't"), ('🤷', 'Maybe')], 1, 3,
               'Ele diz: “No, I’m not.”'),
            qz('What is for everyone?', 'O que é para todos?', [('🍕', 'Pizza'), ('🍪', 'Cookies'), ('☕', 'Hot chocolate')], 2, 6,
               'O maquinista diz: “Hot chocolate for everyone!”')],
        rdg_q=dict(q='Qual é a resposta curta certa para “Are you ready?” (sim)', o=['Yes, I\'m.', 'Yes, I do.', 'Yes, I am.'], a=2,
                   why='Na resposta curta afirmativa não se contrai: **Yes, I am.**'),
        dictate=[['Are you ready?', 'Você está pronto?'], ['Are you hungry?', 'Você está com fome?'],
                 ["No, I'm not.", 'Não, não estou.'], ["I'm cold, too.", 'Eu também estou com frio.']],
        produce=dict(
            prompt='O maquinista pergunta: *Are you cold? Are you hungry?* **Responda com Yes, I am ou No, I\'m not, diga mais uma coisa sobre você com I\'m… e pergunte algo a ele com Are you…?**',
            ph="Ex.: Yes, I am. I'm hungry. Are you cold?",
            chips=['Yes, I am.', "No, I'm not.", 'Are you…?'],
            model="Yes, I am. I'm hungry, too. Are you cold?",
            check=['Respondi com Yes, I am ou No, I\'m not?', 'Disse como estou com I\'m?', 'Fiz uma pergunta com Are you…?'],
            kw=["\\b(?:yes,?\\s*i am|no,?\\s*i(?:['’]m| am) not)\\b", "\\bI(?:['’]m| am)\\s+(?!not\\b)\\w+", '\\bare you\\b[^.!?]*\\?'],
            tips=[[['Yes, I am.', 'Sim, estou.'], ["No, I'm not.", 'Não, não estou.']],
                  [["I'm hungry.", 'Estou com fome.'], ["I'm a little scared.", 'Estou com um pouco de medo.']],
                  [['Are you cold?', 'Você está com frio?'], ['Are you ready?', 'Você está pronto?']]],
            ok=['Resposta curta! ✅', 'Disse como está! 🙋', 'Boa pergunta! ❓'],
            reply=["I'm fine, thanks. Here is your hot chocolate!", 'Estou bem, obrigado. Aqui está o seu chocolate quente!']),
        rs=rs('library', 'traincar', 'farm', 'playground', 'snow', 'pool', 'chefkitchen', 'artroom', 'mountain', 'christmas', 'museum'),
        sc='snow')
    X = dict(
        n=7009802, review=True, names=('Boy', 'Conductor'),
        stage=dict(rs='traincar', chars=[[BOY, 28, 0, 1.0], [GIRL, 56, 1, 1.0], [COND, 84, 1, 1.0]]),
        obra=dict(name='The Polar Express', kind='📖 Livro ilustrado · 1985', year='1985',
                  text='Livro ilustrado do americano Chris Van Allsburg, de 1985. Na noite de Natal, um menino embarca num trem mágico rumo ao Polo Norte. Em 2004 virou um filme de animação dirigido por Robert Zemeckis.',
                  line=['All aboard!', 'Todos a bordo!'],
                  pa=dict(t='snowvillage', e=['🚂', '🎫', '❄️'], p='a', v=1)),
        gancho=['Conductor', 'All aboard! Are you ready?', 'Todos a bordo! Vocês estão prontos?'],
        hot=[hot('🎫', 12, 18, 'ticket', 'bilhete', 'Are you ready? Show your ticket.', 'Você está pronto? Mostre o bilhete.'),
             hot('🚂', 40, 12, 'train', 'trem', 'Are you in the train?', 'Você está no trem?'),
             hot('🥶', 66, 14, 'cold', 'com frio', 'Are you cold? I am.', 'Você está com frio? Eu estou.'),
             hot('🍫', 88, 16, 'chocolate', 'chocolate', 'Are you hungry? Have chocolate!', 'Você está com fome? Tome chocolate!'),
             hot('😨', 12, 82, 'scared', 'com medo', 'Are you scared? No, I\'m not.', 'Você está com medo? Não, não estou.')],
        gap=[gp('___ you ready?', 'Você está pronto?', ['Is', 'Do', 'Are'], 2, 'Com **you**, o verbo é **are**: **Are** you ready?'),
             gp("Yes, I ___.", 'Sim, estou.', ['am', 'are', "I'm"], 0, 'Resposta curta: Yes, I **am**.'),
             gp("No, I'm ___.", 'Não, não estou.', ['not', 'no', "don't"], 0, 'Negativa: I\'m **not**.'),
             gp('Are you hungry? I\'m hungry, ___.', 'Você está com fome? Eu também estou com fome.', ['also', 'too', 'two'], 1, '**too** no final = também.')],
        trap=[tr(['You are cold?', 'Do you cold?', 'Are you cold?'], 2, 'Na pergunta o verbo vem primeiro: **Are you** cold?'),
              tr(["Yes, I'm.", 'Yes, I am.', 'Yes, I are.'], 1, 'Na resposta curta afirmativa não se contrai: Yes, I **am**.', 'Qual resposta está certa?')],
        sticker=dict(title='O menino e a menina no trem', sub='The Polar Express · 1985', rs='traincar', chars=[[BOY, 34, 0, 1.0], [GIRL, 68, 1, 1.0]]),
        speakers={'Boy': BOY, 'Girl': GIRL, 'Conductor': COND},
        rule=dict(
            who=COND, head='Are you ready / cold…?', sub='Pergunte como a pessoa está.',
            say=['All aboard! Are you ready?', 'Todos a bordo! Vocês estão prontos?'],
            formula=[dict(from_=[['You', 0], ['are', 1], ['cold.', 3]], to=[['Are', 1], ['you', 0], ['cold?', 3]], say='Are you cold?',
                          note='A pergunta troca a ordem: **are** vai para a frente de **you**.'),
                     dict(from_=[['Are you', 0], ['hungry?', 3]], to=[['Yes,', 2], ['I am.', 1]], say='Yes, I am.',
                          note='A resposta curta repete o verbo: **Yes, I am.** ou **No, I’m not.**')],
            uses=[dict(ico='✅', tag='Pronto?', en='Are you ready?', pt='Você está pronto?'),
                  dict(ico='🥶', tag='Sensação', en='Are you cold?', pt='Você está com frio?'),
                  dict(ico='🙌', tag='Também', en="I'm hungry, too.", pt='Eu também estou com fome.')],
            rules=[dict(tag='Are you + palavra', c=0, text='Perguntas sobre **como a pessoa está**: ready, cold, hungry, scared.', ex='Are you scared?'),
                   dict(tag='Resposta curta', c=2, text='Sim: **Yes, I am.** Não: **No, I’m not.**', ex="✗ Yes, I'm  →  ✓ Yes, I am"),
                   dict(tag='too', c=1, text='**too** no fim da frase = também.', ex="I'm cold, too.")],
            tips=['Em português dizemos “estou com frio”. Em inglês usamos o verbo ser/estar: **I’m cold**, e não “I have cold”.']),
        mission_ic='🚂')
    XT = dict(
        exp=[xp('🚂', 'All aboard!', 'Expressão', 'Todos a bordo!', 'Chamado para **embarcar** em trem ou navio.', 'All aboard! The train leaves now.', 'Todos a bordo! O trem sai agora.'),
             xp('🧭', 'Where to?', 'Informal', 'Para onde?', 'Pergunta rápida de **quem vai levar você** a algum lugar.', 'Where to, miss?', 'Para onde, senhorita?'),
             xp('👣', 'Watch your step!', 'Expressão', 'Cuidado com o degrau!', 'Aviso para **não tropeçar** ao subir ou descer.', 'Watch your step, kids!', 'Cuidado com o degrau, crianças!'),
             xp('🎄', 'Have a nice trip!', 'Expressão', 'Boa viagem!', 'Desejo a **quem vai viajar**.', 'Have a nice trip, Boy!', 'Boa viagem, menino!')],
        exp_scene=dict(rs='snow', lines=[
            ['Conductor', '**All aboard**! The train leaves now.', 'Todos a bordo! O trem sai agora.'],
            ['Girl', '**Watch your step**! It is cold.', 'Cuidado com o degrau! Está frio.'],
            ['Conductor', '**Where to**, kids?', 'Para onde, crianças?'],
            ['Boy', 'To the North Pole!', 'Para o Polo Norte!'],
            ['Conductor', 'Great! **Have a nice trip**!', 'Ótimo! Boa viagem!'],
            ['Girl', 'Thank you! Are you ready, Boy?', 'Obrigada! Você está pronto, menino?']]),
        lab=dict(
            short='h inicial', title='Laboratório de sons: o “h” de hungry',
            say='O “h” inglês é um sopro suave. Vamos treinar com hungry e hot chocolate!',
            intro=dict(what='O **h** de **hungry**, **hot** e **hat** é só um sopro de ar, como quando você embaça um vidro.',
                       how='Abra a boca e solte o ar da garganta, de leve: “hhhot”. A língua não faz nada e não há nenhum “r” na frente.',
                       pt='Em português o “h” é mudo (hora, hotel). Já em inglês ele se escuta. Cuidado: brasileiros dizem “rungry”, com um “r” forte. Aqui o som é só ar.'),
            ex=[['hungry', 'HÂN-gri', 'com fome', 'sopro de ar, sem “r”'], ['hot', 'HÓT', 'quente', 'solte o ar antes do “ó”'],
                ['help', 'HÉLP', 'ajuda', 'sopro suave, sem força na garganta']],
            pairs=[['hat', 'at', 'chapéu × em (lugar)'], ['hear', 'ear', 'ouvir × orelha'], ['heat', 'eat', 'calor × comer']],
            tip='Segure a mão na frente da boca: no “h” você sente o ar quente. No “r” e na vogal sem “h”, não.',
            phrase=['Are you hungry? Hot chocolate!', 'Você está com fome? Chocolate quente!'],
            rounds=[rd('hat', ['hat', 'at'], 0, '**hat** (chapéu) começa com sopro de ar. **At** começa direto na vogal.'),
                    rd('eat', ['heat', 'eat'], 1, '**eat** (comer) começa direto na vogal. **Heat** (calor) tem o sopro do “h”.'),
                    rd('hear', ['ear', 'hear'], 1, '**hear** (ouvir) tem o “h”. **Ear** (orelha) não tem.')]),
        hunt=[hn('hungry', ['hungry', 'angry'], 0, '**hungry** (com fome) começa com sopro de ar.'),
              hn('hot', ['🔥', '🥶', '🎫'], 0, '**hot** = quente.', True),
              hn('heat', ['heat', 'eat'], 0, '**heat** (calor) tem “h”.'),
              hn('at', ['hat', 'at'], 1, '**at** começa direto na vogal.'),
              hn('hat', ['🎩', '🍴', '🥶'], 0, '**hat** = chapéu.', True)])
    VB = dict(title='Verbos do trem', tip='Quatro verbos: ride, wait, drink e sit.', items=[
        vb('ride', '🚂', 'andar de (trem, bicicleta)', 'I ride the train.', 'The Boy ride**s** the train.', 'I ride the train.', 'Eu ando de trem.', 'rides'),
        vb('wait', '⏳', 'esperar', 'I wait for the train.', 'She wait**s** in line.', 'I wait for the train.', 'Eu espero o trem.', 'waits'),
        vb('drink', '☕', 'beber', 'I drink hot chocolate.', 'He drink**s** hot chocolate.', 'I drink hot chocolate.', 'Eu bebo chocolate quente.', 'drinks'),
        vb('sit', '💺', 'sentar', 'I sit by the window.', 'She sit**s** by the window.', 'I sit by the window.', 'Eu sento perto da janela.', 'sits')])
    MR = dict(
        mold=[dict(label='Perguntar como a pessoa está', slots=[
                   dict(cat='pergunta', opts=[['Are you', 'você está']]),
                   dict(cat='como', opts=[['ready', 'pronto(a)'], ['cold', 'com frio'], ['hungry', 'com fome'], ['scared', 'com medo'], ['tired', 'cansado(a)'], ['happy', 'feliz']])], end=['?', '?']),
              dict(label='Responder', slots=[
                   dict(cat='sim ou não', opts=[['Yes,', 'sim,'], ['No,', 'não,']]),
                   dict(cat='resposta', opts=[['I am.', 'estou.'], ["I'm not.", 'não estou.']])], end=['.', '.']),
              dict(label='Eu também', slots=[
                   dict(cat='eu', opts=[["I'm", 'eu estou']]),
                   dict(cat='como', opts=[['cold', 'com frio'], ['hungry', 'com fome'], ['scared', 'com medo'], ['ready', 'pronto(a)']]),
                   dict(cat='também', opts=[[', too', ', também']])], end=['.', '.'])],
        speak=[["Are you ready? Yes, I am.", 'Você está pronto? Sim, estou.'], ["I'm cold, too. Hot chocolate, please!", 'Eu também estou com frio. Chocolate quente, por favor!']],
        trap=[dict(ask='“All aboard!” é dito…', opts=['antes de embarcar', 'depois de comer', 'ao dormir'], a=0, why='**All aboard!** chama todos para embarcar.', say='All aboard!'),
              dict(ask='“Watch your step!” quer dizer…', opts=['Cuidado com o degrau!', 'Qual é o seu passo?', 'Chegue cedo!'], a=0, why='**Watch your step!** = cuidado onde pisa.', say='Watch your step!')],
        gap=[dict(text='All ___!', pt='Todos a bordo!', opts=['aboard', 'board', 'inside'], a=0, why='**All aboard!** é a frase pronta.', say='All aboard!'),
             dict(text='Have a nice ___!', pt='Boa viagem!', opts=['trip', 'train', 'ticket'], a=0, why='**Have a nice trip!** = boa viagem!', say='Have a nice trip!')],
        expq=[dict(ask='O trem vai sair e as pessoas precisam entrar.', opts=['Have a nice trip!', 'All aboard!', 'Where to?'], a=1, why='**All aboard!** chama para embarcar.'),
              dict(ask='O motorista quer saber o destino.', opts=['Where to?', 'Watch your step!', 'All aboard!'], a=0, why='**Where to?** = para onde?'),
              dict(ask='Um amigo vai viajar amanhã.', opts=['Where to?', 'Watch your step!', 'Have a nice trip!'], a=2, why='**Have a nice trip!** = boa viagem!')],
        missions=[
            mission('🚂', 'Fila do embarque', 'Pergunte e responda sobre como estão.',
                    'Você está na fila do trem. **Pergunte se a pessoa está com frio, responda se você está com fome (Yes, I am ou No, I\'m not) e diga como você está.**',
                    ['Are you…?'], "Are you cold? Yes, I am. I'm hungry, too.",
                    ['Fiz uma pergunta com Are you…?', 'Usei a resposta curta?', 'Disse como estou com I\'m?'],
                    ['\\bare you\\b[^.!?]*\\?', "\\b(?:yes,?\\s*i am|no,?\\s*i(?:['’]m| am) not)\\b", "\\bI(?:['’]m| am)\\s+(?!not\\b)\\w+"],
                    [[['Are you cold?', 'Você está com frio?']], [['Yes, I am.', 'Sim, estou.'], ["No, I'm not.", 'Não, não estou.']], [["I'm hungry.", 'Estou com fome.']]],
                    ['Pergunta certa! ❓', 'Resposta curta! ✅', 'Muito bem! 🙋'],
                    ["Me, too! Let's get some hot chocolate!", 'Eu também! Vamos tomar chocolate quente!']),
            mission('🎄', 'Despedida na estação', 'Use as expressões do trem.',
                    'Seu amigo vai embarcar. **Chame para embarcar, avise para ter cuidado com o degrau e deseje boa viagem.**',
                    ['All aboard!'], 'All aboard! Watch your step! Have a nice trip!',
                    ['Chamei para embarcar?', 'Avisei do degrau?', 'Desejei boa viagem?'],
                    ['\\ball aboard\\b', '\\bwatch your step\\b', '\\bhave a nice trip\\b'],
                    [[['All aboard!', 'Todos a bordo!']], [['Watch your step!', 'Cuidado com o degrau!']], [['Have a nice trip!', 'Boa viagem!']]],
                    ['Embarque! 🚂', 'Cuidado! 👣', 'Boa viagem! 🎄'],
                    ['Thanks! See you soon!', 'Obrigado! Até logo!'])])
    CX = [cx('You show it to get on the train. It is a ___.', 'Você mostra isso para entrar no trem. É um bilhete.', 'ticket', 'chocolate', 'train'),
          cx('It has wheels, runs on rails and says choo-choo. It is a ___.', 'Tem rodas, anda em trilhos e faz tchu-tchu. É um trem.', 'train', 'ticket', 'cold'),
          cx('The bag is packed and I\'m at the door. I\'m ___ to go.', 'A mala está pronta e estou na porta. Estou pronto para ir.', 'ready', 'cold', 'hungry'),
          cx('It is snowing and I have no coat. I am ___.', 'Está nevando e estou sem casaco. Estou com frio.', 'cold', 'ready', 'scared'),
          cx('I have no lunch today. My stomach says "grr". I am ___.', 'Hoje não almocei. Meu estômago faz “grr”. Estou com fome.', 'hungry', 'ready', 'cold'),
          cx('It is a dark night and a loud noise: the boy is ___.', 'É uma noite escura e um barulho alto: o menino está com medo.', 'scared', 'ready', 'hungry')]
    return dict(B=B, X=X, XT=XT, VB=VB, MR=MR, CX=CX)


# ============================================================ POS 9 · It's a Small World
def ep09():
    MIA = 'p:long:6b3f26:f4c7a1:d53f8c:bow:dress'
    LEO = 'p:cap:2b1b12:e8b48a:2b6cb0:none:shirt'
    GUIDE = 'p:short:2d3748:c68642:2f855a:hat:suit'
    B = dict(
        title='Is He From Japan? · Is he…? Is she…?',
        sub='Perguntar de onde os outros são: Is he from…? Is she from…?',
        pattern_label='Is he / she from…?',
        why='Hoje você aprende a perguntar de onde outra pessoa é com Is he…? e Is she…?, como duas crianças diante dos bonecos de um passeio mágico.',
        vocab=[vc('Doll', 'Boneca, boneco', 'DÓL'), vc('Flag', 'Bandeira', 'FLÉG'), vc('Language', 'Língua, idioma', 'LÉN-guedj'),
               vc('China', 'China', 'TCHÁI-na'), vc('India', 'Índia', 'ÍN-dia'), vc('Canada', 'Canadá', 'KÉ-na-da'), vc('Japan', 'Japão', 'dje-PÉN')],
        balloons=[['🪆', 'doll'], ['🚩', 'flag'], ['🗣️', 'language'], ['🇨🇳', 'China'], ['🇮🇳', 'India'], ['🇨🇦', 'Canada'], ['🇯🇵', 'Japan']],
        cover_art=dict(s='fair', items=[['🪆', 104, 56, 20, 'bob'], ['🚩', 138, 44, 12, 'bob'], ['🌍', 84, 34, 12, 'bob']], seed='sw9'),
        cover_sub='Is he from…? Em 10 minutos você pergunta de onde os outros são, num passeio de bonecos do mundo todo',
        cover_say='Mia e Leo entram num passeio com bonecos de muitos países. De onde eles são? Como perguntar sobre ele e ela?',
        wrap_recap=[['Is he from Japan?', 'Ele é do Japão?'], ['Is she from India?', 'Ela é da Índia?'],
                    ['Yes, he is.', 'Sim, é.'], ["No, she isn't.", 'Não, não é.']],
        teaser=dict(t='A nova aluna', d='Próximo padrão: Is he…? Is she…? para perguntar quem a pessoa é'),
        cast={'Mia': ['👧', '#d53f8c'], 'Leo': ['👦', '#2b6cb0'], 'Guide': ['🧑', '#2f855a']},
        lines=[
            ['Mia', 'Look at the dolls! Is he from Japan?', 'Olhe os bonecos! Ele é do Japão?'],
            ['Guide', "Yes, he is. He's Kenji. He speaks Japanese.", 'Sim, é. Ele é o Kenji. Ele fala japonês.'],
            ['Leo', 'And she? Is she from India?', 'E ela? Ela é da Índia?'],
            ['Guide', "Yes, she is. She's Priya.", 'Sim, é. Ela é a Priya.'],
            ['Mia', 'Look at the flag! Is he from Canada?', 'Olhe a bandeira! Ele é do Canadá?'],
            ['Guide', "No, he isn't. He's from Mexico.", 'Não, não é. Ele é do México.'],
            ['Leo', 'Is that girl from China?', 'Aquela menina é da China?'],
            ['Guide', "Yes, she is! It's a small world!", 'Sim, é! O mundo é pequeno!']],
        quiz=[
            qz('Where is Kenji from?', 'De onde o Kenji é?', [('🇨🇳', 'China'), ('🇯🇵', 'Japan'), ('🇮🇳', 'India')], 1, 1,
               'O guia diz: “He’s Kenji.” e responde que o boneco é do Japão.'),
            qz('Is the boy from Canada?', 'O menino é do Canadá?', [('✅', 'Yes, he is'), ('❌', "No, he isn't"), ('🤷', 'Maybe')], 1, 5,
               'O guia diz: “No, he isn’t. He’s from Mexico.”'),
            qz('Who is from India?', 'Quem é da Índia?', [('🧒', 'Priya'), ('👦', 'Kenji'), ('👧', 'Mia')], 0, 3,
               'O guia diz: “She’s Priya.” Ela é da Índia.')],
        rdg_q=dict(q='Qual é a resposta curta certa para “Is she from India?” (sim)', o=['Yes, she is.', "Yes, she's.", 'Yes, he is.'], a=0,
                   why='Na resposta curta afirmativa não se contrai: **Yes, she is.** E “ela” é **she**.'),
        dictate=[['Is he from Japan?', 'Ele é do Japão?'], ['Yes, he is.', 'Sim, é.'],
                 ["No, she isn't.", 'Não, não é.'], ["It's a small world!", 'O mundo é pequeno!']],
        produce=dict(
            prompt='Mia olha os bonecos: *Is he from Japan? Is she from India?* **Pergunte se um menino é de um país, pergunte se uma menina é de um país e responda com Yes, she is ou No, he isn\'t.**',
            ph='Ex.: Is he from Canada? Is she from China? Yes, she is.',
            chips=['Is he from…?', 'Is she from…?', 'Yes, she is.'],
            model='Is he from Canada? Is she from China? Yes, she is.',
            check=['Perguntei sobre ele com Is he…?', 'Perguntei sobre ela com Is she…?', 'Usei uma resposta curta?'],
            kw=['\\bis he\\b[^.!?]*\\?', '\\bis she\\b[^.!?]*\\?', "\\b(?:yes|no),?\\s*(?:he|she) (?:is|isn['’]t)\\b"],
            tips=[[['Is he from Japan?', 'Ele é do Japão?']], [['Is she from India?', 'Ela é da Índia?']],
                  [['Yes, he is.', 'Sim, ele é.'], ["No, she isn't.", 'Não, ela não é.']]],
            ok=['Sobre ele! 👦', 'Sobre ela! 👧', 'Resposta curta! ✅'],
            reply=["Yes, she is! And he's from Mexico. It's a small world!", 'Sim, é! E ele é do México. O mundo é pequeno!']),
        rs=rs('museum', 'fair', 'stadium', 'harbor', 'zoo', 'garden', 'restaurant', 'mountain', 'bakery', 'christmas', 'pool'),
        sc='stadium')
    X = dict(
        n=30002, review=True, names=('Mia', 'Guide'),
        stage=dict(rs='fair', chars=[[MIA, 28, 0, 1.0], [LEO, 56, 1, 1.0], [GUIDE, 84, 1, 1.0]]),
        obra=dict(name="It's a Small World", kind='🎡 Atração e canção · 1964', year='1964',
                  text='Atração da Disney criada para a Feira Mundial de Nova York de 1964, com música dos irmãos Sherman. Bonecos de crianças de vários países cantam sobre um mundo pequeno e unido. Hoje existe em vários parques.',
                  line=["It's a small world after all.", 'No fim das contas, o mundo é pequeno.'],
                  pa=dict(t='ferris', e=['🪆', '🚩', '🌍'], p='g', v=1)),
        gancho=['Mia', 'Look at the dolls! Is he from Japan?', 'Olhe os bonecos! Ele é do Japão?'],
        hot=[hot('🇯🇵', 12, 18, 'Japan', 'Japão', 'Is he from Japan?', 'Ele é do Japão?'),
             hot('🇮🇳', 40, 12, 'India', 'Índia', 'Is she from India?', 'Ela é da Índia?'),
             hot('🇨🇦', 66, 14, 'Canada', 'Canadá', 'Is he from Canada?', 'Ele é do Canadá?'),
             hot('🇨🇳', 88, 16, 'China', 'China', 'Is she from China?', 'Ela é da China?'),
             hot('🪆', 12, 82, 'doll', 'boneca', 'Is she a doll? Yes, she is.', 'Ela é uma boneca? Sim, é.')],
        gap=[gp('___ he from Japan?', 'Ele é do Japão?', ['Is', 'Are', 'Does'], 0, 'Com **he**, o verbo é **is**: **Is** he…?'),
             gp('Yes, she ___.', 'Sim, ela é.', ['does', 'is', 'are'], 1, 'A resposta curta repete o verbo: Yes, she **is**.'),
             gp('No, he ___.', 'Não, ele não é.', ['not', "aren't", "isn't"], 2, 'Negativa curta: No, he **isn\'t**.'),
             gp('Is ___ from India? (uma menina)', 'Ela é da Índia?', ['he', 'she', 'it'], 1, 'Menina é **she**: Is **she** from India?')],
        trap=[tr(['He is from Japan?', 'Does he from Japan?', 'Is he from Japan?'], 2, 'Na pergunta o verbo vem primeiro: **Is** he from Japan?'),
              tr(["Yes, he's.", 'Yes, he is.', 'Yes, he are.'], 1, 'Na resposta curta afirmativa não se contrai: Yes, he **is**.', 'Qual resposta está certa?')],
        sticker=dict(title='Mia, Leo e o guia', sub="It's a Small World · 1964", rs='fair', chars=[[MIA, 30, 0, 1.0], [LEO, 56, 1, 1.0], [GUIDE, 84, 1, 0.95]]),
        speakers={'Mia': MIA, 'Leo': LEO, 'Guide': GUIDE},
        rule=dict(
            who=GUIDE, head='Is he / she from…?', sub='Pergunte de onde um homem ou uma mulher é.',
            say=["Yes, she is. She's Priya.", 'Sim, é. Ela é a Priya.'],
            formula=[dict(from_=[['He', 0], ['is', 1], ['from Japan.', 3]], to=[['Is', 1], ['he', 0], ['from Japan?', 3]], say='Is he from Japan?',
                          note='Para ele, **is** passa para a frente de **he**.'),
                     dict(from_=[['She', 2], ['is', 1], ['from India.', 3]], to=[['Is', 1], ['she', 2], ['from India?', 3]], say='Is she from India?',
                          note='Para ela, **is** passa para a frente de **she**.')],
            uses=[dict(ico='❓', tag='Perguntar', en='Is he from Canada?', pt='Ele é do Canadá?'),
                  dict(ico='✅', tag='Sim', en='Yes, she is.', pt='Sim, ela é.'),
                  dict(ico='❌', tag='Não', en="No, he isn't.", pt='Não, ele não é.')],
            rules=[dict(tag='Is he / Is she', c=0, text='Pergunta sobre **ele** ou **ela**: o **is** vai para a frente.', ex='Is she from China?'),
                   dict(tag='Yes, he is', c=2, text='Resposta curta **sim**: repita o verbo, sem contrair.', ex="✗ Yes, he's  →  ✓ Yes, he is"),
                   dict(tag="No, he isn't", c=1, text='Resposta curta **não**: use **isn’t**.', ex="No, she isn't.")],
            tips=['Em português a pergunta só muda a entonação. Em inglês, **troque a ordem**: He is → Is he.']),
        mission_ic='🌍')
    XT = dict(
        exp=[xp('🤨', 'Really?', 'Informal', 'Sério?', 'Quando você **se surpreende** com algo e quer saber mais.', 'He is from Mexico. Really?', 'Ele é do México. Sério?'),
             xp('😲', 'No way!', 'Gíria', 'Não acredito!', 'Reação de **muita surpresa**, com amigos.', 'No way! She is from Canada!', 'Não acredito! Ela é do Canadá!'),
             xp('👍', 'I see.', 'Expressão', 'Entendi.', 'Quando você **compreende** o que a outra pessoa explicou.', 'I see. He speaks Japanese.', 'Entendi. Ele fala japonês.'),
             xp('🌎', "It's a small world!", 'Expressão', 'O mundo é pequeno!', 'Quando você **encontra algo conhecido** em um lugar distante.', "She is from Recife, too? It's a small world!", 'Ela também é de Recife? O mundo é pequeno!')],
        exp_scene=dict(rs='playground', lines=[
            ['Mia', 'Is she from Canada?', 'Ela é do Canadá?'],
            ['Guide', 'Yes, she is. And he is from Canada, too.', 'Sim, é. E ele também é do Canadá.'],
            ['Leo', '**Really**? Both of them?', 'Sério? Os dois?'],
            ['Mia', '**No way**! My mom is from Canada!', 'Não acredito! A minha mãe é do Canadá!'],
            ['Guide', '**It\'s a small world**!', 'O mundo é pequeno!'],
            ['Leo', '**I see**. Now I know!', 'Entendi. Agora eu sei!']]),
        lab=dict(
            short='ch × sh', title='Laboratório de sons: ch de China e sh de she',
            say='Dois sons que parecem iguais: o “ch” de China e o “sh” de she. Vamos treinar!',
            intro=dict(what='O **ch** de **China** e **chair** é um “tch” explosivo. O **sh** de **she** e **ship** é só um “shhh” contínuo, como pedir silêncio.',
                       how='No **ch**, encoste a língua no céu da boca e solte de repente: “tch”. No **sh**, deixe o ar sair devagar, com os lábios um pouco arredondados: “shhh”.',
                       pt='Em português “ch” de chá é o “sh” inglês. O “tch” de tchau é o “ch” inglês. Muita gente troca: **ship** (navio) e **chip** (batata frita) ficam iguais!'),
            ex=[['China', 'TCHÁI-na', 'China', 'comece com “tch”, língua no céu da boca'], ['she', 'SHII', 'ela', 'só ar, sem “tch”'],
                ['chair', 'TCHÉR', 'cadeira', '“tch” de tchau']],
            pairs=[['chip', 'ship', 'batata frita × navio'], ['cheap', 'sheep', 'barato × ovelha'], ['watch', 'wash', 'assistir × lavar']],
            tip='Para o “ch”, pare o ar e solte de repente. Para o “sh”, deixe o ar fluir sem parar.',
            phrase=['She is from China.', 'Ela é da China.'],
            rounds=[rd('chip', ['chip', 'ship'], 0, '**chip** começa com “tch”. **Ship** começa com “shhh”.'),
                    rd('sheep', ['cheap', 'sheep'], 1, '**sheep** (ovelha) começa com “shhh”. **Cheap** (barato) começa com “tch”.'),
                    rd('wash', ['watch', 'wash'], 1, '**wash** (lavar) termina em “sh”. **Watch** termina em “tch”.')]),
        hunt=[hn('ship', ['chip', 'ship'], 1, '**ship** (navio) começa com “shhh”.'),
              hn('chair', ['🪑', '🚢', '🐑'], 0, '**chair** = cadeira.', True),
              hn('cheap', ['cheap', 'sheep'], 0, '**cheap** (barato) começa com “tch”.'),
              hn('watch', ['watch', 'wash'], 0, '**watch** termina em “tch”.'),
              hn('sheep', ['🪑', '🚢', '🐑'], 2, '**sheep** = ovelha.', True)])
    VB = dict(title='Verbos de quem viaja pelo mundo', tip='Quatro verbos: speak, live, learn e like.', items=[
        vb('speak', '🗣️', 'falar (uma língua)', 'I speak English.', 'Kenji speak**s** Japanese.', 'I speak a little English.', 'Eu falo um pouco de inglês.', 'speaks'),
        vb('live', '🏠', 'morar', 'I live in Brazil.', 'Priya live**s** in India.', 'I live in a big city.', 'Eu moro numa cidade grande.', 'lives'),
        vb('learn', '📚', 'aprender', 'I learn a language.', 'She learn**s** English.', 'I learn English every day.', 'Eu aprendo inglês todo dia.', 'learns'),
        vb('like', '❤️', 'gostar', 'I like the dolls.', 'He like**s** the song.', 'I like the dolls.', 'Eu gosto dos bonecos.', 'likes')])
    MR = dict(
        mold=[dict(label='Is he from…?', slots=[
                   dict(cat='pergunta', opts=[['Is he from', 'ele é de']]),
                   dict(cat='país', opts=[['Japan', 'Japão'], ['India', 'Índia'], ['Canada', 'Canadá'], ['China', 'China'], ['Mexico', 'México'], ['Brazil', 'Brasil']])], end=['?', '?']),
              dict(label='Is she from…?', slots=[
                   dict(cat='pergunta', opts=[['Is she from', 'ela é de']]),
                   dict(cat='país', opts=[['Japan', 'Japão'], ['India', 'Índia'], ['Canada', 'Canadá'], ['China', 'China'], ['Mexico', 'México'], ['Brazil', 'Brasil']])], end=['?', '?']),
              dict(label='Responder', slots=[
                   dict(cat='sim ou não', opts=[['Yes,', 'sim,'], ['No,', 'não,']]),
                   dict(cat='quem', opts=[['he', 'ele'], ['she', 'ela']]),
                   dict(cat='resposta', opts=[['is.', 'é.'], ["isn't.", 'não é.']])], end=['', ''])],
        speak=[['Is he from Japan? Yes, he is.', 'Ele é do Japão? Sim, é.'], ["It's a small world! Really?", 'O mundo é pequeno! Sério?']],
        trap=[dict(ask='“No way!” quer dizer…', opts=['Não acredito!', 'Sem caminho!', 'Sem problema!'], a=0, why='**No way!** mostra muita surpresa.', say='No way!'),
              dict(ask='“It’s a small world!” é dito quando…', opts=['o mundo é pequeno mesmo no mapa', 'você encontra algo conhecido longe de casa', 'você quer ir embora'], a=1, why='Dizemos **It’s a small world!** ao ver algo conhecido em lugar distante.', say="It's a small world!")],
        gap=[dict(text='___? Both of them?', pt='Sério? Os dois?', opts=['Really', 'Real', 'Truly'], a=0, why='**Really?** = sério?', say='Really? Both of them?'),
             dict(text='I ___. Now I know!', pt='Entendi. Agora eu sei!', opts=['see', 'look', 'watch'], a=0, why='**I see.** = entendi.', say='I see. Now I know!')],
        expq=[dict(ask='Seu amigo diz algo incrível e você não acredita.', opts=['I see.', 'No way!', "It's a small world!"], a=1, why='**No way!** mostra surpresa.'),
              dict(ask='Alguém explica o caminho e você entendeu.', opts=['I see.', 'Really?', 'No way!'], a=0, why='**I see.** = entendi.'),
              dict(ask='Você encontra um vizinho de casa em outro país.', opts=['I see.', 'No way!', "It's a small world!"], a=2, why='**It’s a small world!** = o mundo é pequeno!')],
        missions=[
            mission('🌍', 'Quem é de onde?', 'Pergunte sobre um menino e uma menina.',
                    'Você vê duas fotos de colegas. **Pergunte se ele é de um país, pergunte se ela é de outro e responda com Yes, he is ou No, she isn\'t.**',
                    ['Is he from…?'], 'Is he from Japan? Is she from India? Yes, she is.',
                    ['Perguntei sobre ele?', 'Perguntei sobre ela?', 'Usei a resposta curta?'],
                    ['\\bis he\\b[^.!?]*\\?', '\\bis she\\b[^.!?]*\\?', "\\b(?:yes|no),?\\s*(?:he|she) (?:is|isn['’]t)\\b"],
                    [[['Is he from Japan?', 'Ele é do Japão?']], [['Is she from India?', 'Ela é da Índia?']], [['Yes, she is.', 'Sim, ela é.'], ["No, he isn't.", 'Não, ele não é.']]],
                    ['Sobre ele! 👦', 'Sobre ela! 👧', 'Resposta curta! ✅'],
                    ['Yes, she is! They are friends from my class.', 'Sim, ela é! Eles são amigos da minha turma.']),
            mission('😲', 'Que surpresa!', 'Reaja com as expressões do episódio.',
                    'Seu amigo diz que a nova colega é do Canadá. **Mostre surpresa com “Really?” ou “No way!”, diga que entendeu e comente que o mundo é pequeno.**',
                    ['Really?'], "Really? No way! I see. It's a small world!",
                    ['Mostrei surpresa?', 'Disse que entendi?', 'Falei que o mundo é pequeno?'],
                    ['\\b(?:really|no way)\\b', '\\bi see\\b', "\\bit['’]?s a small world\\b"],
                    [[['Really?', 'Sério?'], ['No way!', 'Não acredito!']], [['I see.', 'Entendi.']], [["It's a small world!", 'O mundo é pequeno!']]],
                    ['Que surpresa! 😲', 'Entendi! 👍', 'Mundo pequeno! 🌎'],
                    ['Yes! She is from Toronto.', 'Sim! Ela é de Toronto.'])])
    CX = [cx('The Great Wall and the giant panda: they are from ___.', 'A Grande Muralha e o panda-gigante: eles são da China.', 'China', 'Canada', 'Japan'),
          cx('Taj Mahal, curry and Bollywood: it is ___.', 'Taj Mahal, curry e Bollywood: é a Índia.', 'India', 'China', 'Canada'),
          cx('Maple leaf, hockey and Toronto: it is ___.', 'Folha de bordo, hóquei e Toronto: é o Canadá.', 'Canada', 'India', 'Japan'),
          cx('Sushi, anime and Tokyo: it is ___.', 'Sushi, anime e Tóquio: é o Japão.', 'Japan', 'China', 'Canada'),
          cx('English, Portuguese and Spanish are each a ___.', 'Inglês, português e espanhol são, cada um, uma língua.', 'language', 'flag', 'doll'),
          cx('Every country has one with its own colors. It is a ___.', 'Todo país tem uma com suas cores. É uma bandeira.', 'flag', 'doll', 'language')]
    return dict(B=B, X=X, XT=XT, VB=VB, MR=MR, CX=CX)


# ============================================================ POS 10 · Harry Potter
def ep10():
    HARRY = 'p:short:1a1a1a:f4c7a1:8e1b1b:glasses:suit'
    RON = 'p:short:c0501c:f4c7a1:6b2d2d:none:suit'
    HERM = 'p:curly:6b3f26:f4c7a1:8e1b1b:none:dress'
    B = dict(
        title='A nova aluna · Is he…? Is she…?',
        sub='Perguntar quem é e como é: Is she a student? Is he smart?',
        pattern_label='Is he / she…?',
        why='Hoje você aprende a perguntar sobre ele e ela (Is he a student? Is she smart?), como os amigos na biblioteca de Hogwarts.',
        vocab=[vc('Student', 'Aluno(a)', 'STÚ-dent'), vc('Teacher', 'Professor(a)', 'TÍ-tchâr'), vc('Friend', 'Amigo(a)', 'FRÉND'),
               vc('New', 'Novo(a)', 'NIÚ'), vc('Book', 'Livro', 'BÚK'), vc('Smart', 'Inteligente', 'SMÁRT'), vc('Library', 'Biblioteca', 'LÁI-bré-ri')],
        balloons=[['🎓', 'student'], ['👩‍🏫', 'teacher'], ['🤝', 'friend'], ['🆕', 'new'], ['📖', 'book'], ['🧠', 'smart']],
        cover_art=dict(s='library', items=[['📚', 104, 56, 20, 'bob'], ['🎓', 138, 44, 12, 'bob'], ['🦉', 84, 34, 12, 'bob']], seed='hp10'),
        cover_sub='Is he…? Is she…? Em 10 minutos você pergunta sobre os colegas, como na escola de magia',
        cover_say='Na biblioteca de Hogwarts aparece uma aluna nova com um livro enorme. Quem é ela? Como perguntar sobre ele e ela?',
        wrap_recap=[['Is she a student?', 'Ela é aluna?'], ['Is he smart?', 'Ele é inteligente?'],
                    ['Yes, she is.', 'Sim, é.'], ["No, he isn't.", 'Não, não é.']],
        teaser=dict(t='Spell It for Me', d='Próximo padrão: What’s…? para perguntar o que é algo (What is → What’s)'),
        cast={'Ron': ['🧑', '#c0501c'], 'Harry': ['🧙', '#8e1b1b'], 'Hermione': ['👧', '#6b3f26']},
        lines=[
            ['Ron', 'Harry, look! Is she a new student?', 'Harry, olhe! Ela é uma aluna nova?'],
            ['Harry', 'Yes, she is. She is in the library.', 'Sim, é. Ela está na biblioteca.'],
            ['Ron', 'Is she smart? That is a big book!', 'Ela é inteligente? Aquele livro é enorme!'],
            ['Harry', 'I think so. She is very busy.', 'Acho que sim. Ela está muito ocupada.'],
            ['Hermione', 'Hello! Are you Harry Potter?', 'Olá! Você é o Harry Potter?'],
            ['Harry', "Yes, I am. And he's Ron.", 'Sim, sou. E ele é o Ron.'],
            ['Hermione', 'Is he a first-year student, too?', 'Ele também é aluno do primeiro ano?'],
            ['Ron', 'Yes, I am! Nice to meet you.', 'Sim, sou! Prazer em conhecer você.']],
        quiz=[
            qz('Who is new?', 'Quem é novo(a)?', [('🧑', 'Ron'), ('🧙', 'Harry'), ('👧', 'Hermione')], 2, 0,
               'Ron pergunta: “Is she a new student?” e Harry diz que sim.'),
            qz('Where is Hermione?', 'Onde está a Hermione?', [('🍽️', 'In the kitchen'), ('📚', 'In the library'), ('🏟️', 'In the stadium')], 1, 1,
               'Harry diz: “She is in the library.”'),
            qz('Is Ron a student?', 'O Ron é aluno?', [('✅', 'Yes, he is'), ('❌', "No, he isn't"), ('🤷', 'Maybe')], 0, 7,
               'Ron diz: “Yes, I am!” (o Ron é aluno do primeiro ano).')],
        rdg_q=dict(q='Qual pergunta está certa para “Ele é inteligente?”', o=['He is smart?', 'Is he smart?', 'Does he smart?'], a=1,
                   why='Na pergunta o verbo vem primeiro: **Is he** smart?'),
        dictate=[['Is she a student?', 'Ela é aluna?'], ['Is he your friend?', 'Ele é seu amigo?'],
                 ['Yes, she is.', 'Sim, ela é.'], ["No, he isn't.", 'Não, ele não é.']],
        produce=dict(
            prompt='Hermione chega à turma: *Is he a teacher? Is she a student?* **Pergunte sobre um menino com Is he…?, sobre uma menina com Is she…? e responda com Yes, he is ou No, she isn\'t.**',
            ph='Ex.: Is he a teacher? Is she smart? No, he isn\'t.',
            chips=['Is he…?', 'Is she…?', "No, he isn't."],
            model="Is he a teacher? Is she smart? No, he isn't.",
            check=['Perguntei sobre ele com Is he…?', 'Perguntei sobre ela com Is she…?', 'Usei uma resposta curta?'],
            kw=['\\bis he\\b[^.!?]*\\?', '\\bis she\\b[^.!?]*\\?', "\\b(?:yes|no),?\\s*(?:he|she) (?:is|isn['’]t)\\b"],
            tips=[[['Is he a student?', 'Ele é aluno?'], ['Is he your friend?', 'Ele é seu amigo?']],
                  [['Is she smart?', 'Ela é inteligente?'], ['Is she new?', 'Ela é nova?']],
                  [['Yes, she is.', 'Sim, ela é.'], ["No, he isn't.", 'Não, ele não é.']]],
            ok=['Sobre ele! 👦', 'Sobre ela! 👧', 'Resposta curta! ✅'],
            reply=["No, he isn't. He's a student. She's smart, too!", 'Não, ele não é. Ele é aluno. Ela também é inteligente!']),
        rs=rs('bookshop', 'library', 'bank', 'stage', 'forest', 'harbor', 'supermarket', 'soccerfield', 'pharmacy', 'snow', 'artroom'),
        sc='castlehall')
    X = dict(
        n=7030002, review=True, names=('Ron', 'Hermione'),
        stage=dict(rs='library', chars=[[RON, 28, 0, 1.0], [HARRY, 56, 0, 1.0], [HERM, 84, 1, 1.0]]),
        obra=dict(name="Harry Potter and the Sorcerer's Stone", kind='📖 Livro · 1997', year='1997',
                  text='Primeiro livro da série da escritora britânica J. K. Rowling, publicado em 1997. O menino Harry descobre que é bruxo e vai estudar na escola Hogwarts, onde conhece os amigos Ron e Hermione. Nos Estados Unidos o título é Sorcerer’s Stone.',
                  line=['Is she a new student?', 'Ela é uma aluna nova?'],
                  pa=dict(t='castle', e=['🪄', '🦉', '📚'], p='h', v=0)),
        gancho=['Ron', 'Harry, look! Is she a new student?', 'Harry, olhe! Ela é uma aluna nova?'],
        hot=[hot('📚', 12, 18, 'books', 'livros', 'Is she a student? She has books.', 'Ela é aluna? Ela tem livros.'),
             hot('🦉', 40, 12, 'owl', 'coruja', 'Is he a friend? No, he is an owl!', 'Ele é um amigo? Não, ele é uma coruja!'),
             hot('🪄', 66, 14, 'wand', 'varinha', 'Is she a teacher? No, she is a student.', 'Ela é professora? Não, é aluna.'),
             hot('🎓', 88, 16, 'student', 'aluno', 'Is he a student? Yes, he is.', 'Ele é aluno? Sim, é.'),
             hot('🤝', 12, 82, 'friend', 'amigo', 'Is she your friend? Yes, she is.', 'Ela é sua amiga? Sim, é.')],
        gap=[gp('___ she a new student?', 'Ela é uma aluna nova?', ['Is', 'Are', 'Does'], 0, 'Com **she**, o verbo é **is**: **Is** she…?'),
             gp('Is he your friend? Yes, he ___.', 'Ele é seu amigo? Sim, é.', ['does', 'is', 'are'], 1, 'A resposta curta repete o verbo: Yes, he **is**.'),
             gp('Is she a teacher? No, she ___.', 'Ela é professora? Não, não é.', ['not', "aren't", "isn't"], 2, 'Negativa curta: No, she **isn\'t**.'),
             gp('Is ___ smart? (uma menina)', 'Ela é inteligente?', ['he', 'she', 'it'], 1, 'Menina é **she**: Is **she** smart?')],
        trap=[tr(['She is a student?', 'Does she a student?', 'Is she a student?'], 2, 'Na pergunta o verbo vem primeiro: **Is** she a student?'),
              tr(["Yes, he's.", 'Yes, he is.', 'Yes, he are.'], 1, 'Na resposta curta afirmativa não se contrai: Yes, he **is**.', 'Qual resposta está certa?')],
        sticker=dict(title='Os amigos da biblioteca', sub="Harry Potter and the Sorcerer's Stone · 1997", rs='library', chars=[[HARRY, 30, 0, 1.0], [HERM, 66, 1, 1.0]]),
        speakers={'Ron': RON, 'Harry': HARRY, 'Hermione': HERM},
        rule=dict(
            who=HERM, head='Is he / she…?', sub='Pergunte quem a pessoa é e como ela é.',
            say=['Is he a first-year student, too?', 'Ele também é aluno do primeiro ano?'],
            formula=[dict(from_=[['She', 2], ['is', 1], ['a student.', 3]], to=[['Is', 1], ['she', 2], ['a student?', 3]], say='Is she a student?',
                          note='**Is** passa para a frente de **she**.'),
                     dict(from_=[['He', 0], ['is', 1], ['smart.', 3]], to=[['Is', 1], ['he', 0], ['smart?', 3]], say='Is he smart?',
                          note='O mesmo vale para **he**: Is he smart?')],
            uses=[dict(ico='🎓', tag='Quem é', en='Is she a student?', pt='Ela é aluna?'),
                  dict(ico='🧠', tag='Como é', en='Is he smart?', pt='Ele é inteligente?'),
                  dict(ico='✅', tag='Responder', en="Yes, she is. / No, he isn't.", pt='Sim, ela é. / Não, ele não é.')],
            rules=[dict(tag='Is he…?', c=0, text='Para **ele**: o **is** vai para a frente de **he**.', ex='Is he a teacher?'),
                   dict(tag='Is she…?', c=2, text='Para **ela**: o **is** vai para a frente de **she**.', ex='Is she new?'),
                   dict(tag='Resposta curta', c=1, text='Sim: **Yes, she is.** Não: **No, she isn’t.** Não contraia o “is” no sim.', ex="✗ Yes, she's  →  ✓ Yes, she is")],
            tips=['Em inglês a pergunta com **ser/estar** troca a ordem: She is → Is she. Não use “Does”.']),
        mission_ic='🎓')
    XT = dict(
        exp=[xp('🍀', 'Good luck!', 'Expressão', 'Boa sorte!', 'Para desejar **sorte** antes de uma prova ou um desafio.', 'Good luck on the test!', 'Boa sorte na prova!'),
             xp('🫶', "Don't worry.", 'Expressão', 'Não se preocupe.', 'Para **acalmar** alguém nervoso.', "Don't worry. It's easy.", 'Não se preocupe. É fácil.'),
             xp('😎', 'How cool!', 'Informal', 'Que legal!', 'Quando algo é **muito legal**.', 'How cool! A magic book!', 'Que legal! Um livro mágico!'),
             xp('🪑', 'Sit with us!', 'Informal', 'Sente com a gente!', 'Convite para **sentar junto** com um grupo.', 'Sit with us, Hermione!', 'Sente com a gente, Hermione!')],
        exp_scene=dict(rs='classroom' if False else 'school', lines=[
            ['Hermione', "I'm new here. Is the class hard?", 'Eu sou nova aqui. A aula é difícil?'],
            ['Ron', "**Don't worry**! It's fun.", 'Não se preocupe! É divertida.'],
            ['Harry', '**Sit with us**, Hermione!', 'Sente com a gente, Hermione!'],
            ['Hermione', 'Thanks! Look, a magic book.', 'Obrigada! Olhe, um livro mágico.'],
            ['Ron', '**How cool**!', 'Que legal!'],
            ['Harry', 'The test is today. **Good luck**, everyone!', 'A prova é hoje. Boa sorte, pessoal!']]),
        lab=dict(
            short='s + consoante', title='Laboratório de sons: o “st” de student',
            say='Em inglês, muitas palavras começam com “s” seguido de outra consoante, como student e school. Não coloque um “e” na frente!',
            intro=dict(what='Em **student**, **school** e **smart**, o **s** vem colado na consoante seguinte: “STÚ-dent”, “SKÚL”, “SMÁRT”.',
                       how='Comece com um “sss” prolongado e só depois junte a próxima consoante. Não coloque nenhuma vogal antes do s.',
                       pt='Em português não começamos palavras assim: dizemos “estudante”, “escola”. Muitos brasileiros falam “estudent”, “eschool”. Em inglês, comece direto com o **s**.'),
            ex=[['student', 'STÚ-dent', 'aluno', '“sss” antes do “t”, sem “e” na frente'], ['school', 'SKÚL', 'escola', 'comece com “sss” e junte o “k”'],
                ['smart', 'SMÁRT', 'inteligente', '“sss” e “m” juntos']],
            pairs=[['stop', 'top', 'parar × topo'], ['school', 'cool', 'escola × legal'], ['sport', 'port', 'esporte × porto']],
            tip='Estique o “sss” no começo e só depois fale o resto. Nada de “e” na frente.',
            phrase=['Is she a student at school?', 'Ela é aluna na escola?'],
            rounds=[rd('stop', ['stop', 'top'], 0, '**stop** (parar) começa com “st”. **Top** (topo) começa só com “t”.'),
                    rd('cool', ['school', 'cool'], 1, '**cool** (legal) começa com “k”. **School** começa com “sk”.'),
                    rd('sport', ['port', 'sport'], 1, '**sport** (esporte) começa com “sp”. **Port** (porto) começa com “p”.')]),
        hunt=[hn('top', ['stop', 'top'], 1, '**top** (topo) começa só com “t”.'),
              hn('school', ['🏫', '😎', '🛑'], 0, '**school** = escola.', True),
              hn('port', ['port', 'sport'], 0, '**port** (porto) começa com “p”.'),
              hn('stop', ['stop', 'top'], 0, '**stop** (parar) começa com “st”.'),
              hn('cool', ['🏫', '😎', '🛑'], 1, '**cool** = legal.', True)])
    VB = dict(title='Verbos da escola de magia', tip='Quatro verbos: study, ask, help e meet.', items=[
        vb('study', '📚', 'estudar', 'I study in the library.', 'Hermione stud**ies** every day.', 'I study every day.', 'Eu estudo todo dia.', 'studies'),
        vb('ask', '🙋', 'perguntar', 'I ask a question.', 'Ron ask**s** a question.', 'I ask a question.', 'Eu faço uma pergunta.', 'asks'),
        vb('help', '🤝', 'ajudar', 'I help my friend.', 'She help**s** her friend.', 'I help my friend.', 'Eu ajudo o meu amigo.', 'helps'),
        vb('meet', '👋', 'conhecer, encontrar', 'I meet a new friend.', 'He meet**s** a new student.', 'I meet a new friend.', 'Eu conheço um novo amigo.', 'meets')])
    MR = dict(
        mold=[dict(label='Is he…?', slots=[
                   dict(cat='pergunta', opts=[['Is he', 'ele é']]),
                   dict(cat='palavra', opts=[['a student', 'aluno'], ['a teacher', 'professor'], ['smart', 'inteligente'], ['new', 'novo'], ['your friend', 'seu amigo']])], end=['?', '?']),
              dict(label='Is she…?', slots=[
                   dict(cat='pergunta', opts=[['Is she', 'ela é']]),
                   dict(cat='palavra', opts=[['a student', 'aluna'], ['a teacher', 'professora'], ['smart', 'inteligente'], ['new', 'nova'], ['your friend', 'sua amiga']])], end=['?', '?']),
              dict(label='Responder', slots=[
                   dict(cat='sim ou não', opts=[['Yes,', 'sim,'], ['No,', 'não,']]),
                   dict(cat='quem', opts=[['he', 'ele'], ['she', 'ela']]),
                   dict(cat='resposta', opts=[['is.', 'é.'], ["isn't.", 'não é.']])], end=['', ''])],
        speak=[["Good luck! Don't worry.", 'Boa sorte! Não se preocupe.'], ['How cool! Sit with us!', 'Que legal! Sente com a gente!']],
        trap=[dict(ask='“Don’t worry.” quer dizer…', opts=['Não se preocupe.', 'Não trabalhe.', 'Não se atrase.'], a=0, why='**Don’t worry.** = não se preocupe.', say="Don't worry."),
              dict(ask='“Good luck!” é dito antes de…', opts=['um desafio ou prova', 'dormir', 'comer'], a=0, why='**Good luck!** = boa sorte.', say='Good luck!')],
        gap=[dict(text='Good ___ on the test!', pt='Boa sorte na prova!', opts=['luck', 'lucky', 'look'], a=0, why='**Good luck!** é a frase pronta.', say='Good luck on the test!'),
             dict(text='How ___! A magic book!', pt='Que legal! Um livro mágico!', opts=['cool', 'cold', 'cook'], a=0, why='**How cool!** = que legal!', say='How cool!')],
        expq=[dict(ask='Seu amigo vai fazer uma prova amanhã.', opts=['Good luck!', 'How cool!', 'Sit with us!'], a=0, why='**Good luck!** = boa sorte.'),
              dict(ask='Uma colega nova está sozinha e você quer incluí-la.', opts=["Don't worry.", 'Sit with us!', 'How cool!'], a=1, why='**Sit with us!** = sente com a gente!'),
              dict(ask='Seu colega está nervoso com a aula.', opts=['How cool!', 'Sit with us!', "Don't worry."], a=2, why='**Don’t worry.** acalma a pessoa.')],
        missions=[
            mission('🎓', 'Quem é quem na turma?', 'Pergunte sobre dois colegas.',
                    'Você vê dois colegas novos. **Pergunte se ele é aluno, pergunte se ela é professora e responda com Yes, he is ou No, she isn\'t.**',
                    ['Is he…?', 'Is she…?'], "Is he a student? Is she a teacher? Yes, he is.",
                    ['Perguntei sobre ele?', 'Perguntei sobre ela?', 'Usei a resposta curta?'],
                    ['\\bis he\\b[^.!?]*\\?', '\\bis she\\b[^.!?]*\\?', "\\b(?:yes|no),?\\s*(?:he|she) (?:is|isn['’]t)\\b"],
                    [[['Is he a student?', 'Ele é aluno?']], [['Is she a teacher?', 'Ela é professora?']], [['Yes, he is.', 'Sim, ele é.'], ["No, she isn't.", 'Não, ela não é.']]],
                    ['Sobre ele! 👦', 'Sobre ela! 👧', 'Resposta curta! ✅'],
                    ["Yes, he is. She's a teacher, too!", 'Sim, ele é. Ela é professora também!']),
            mission('🍀', 'Antes da prova', 'Anime uma colega com as expressões.',
                    'Uma colega está nervosa antes da prova. **Diga para ela não se preocupar, deseje boa sorte e diga “How cool!” para o livro dela.**',
                    ["Don't worry."], "Don't worry! Good luck! How cool, a new book!",
                    ['Pedi para não se preocupar?', 'Desejei boa sorte?', 'Disse “How cool”?'],
                    ["\\bdon['’]?t worry\\b", '\\bgood luck\\b', '\\bhow cool\\b'],
                    [[["Don't worry.", 'Não se preocupe.']], [['Good luck!', 'Boa sorte!']], [['How cool!', 'Que legal!']]],
                    ['Calma! 🫶', 'Boa sorte! 🍀', 'Legal! 😎'],
                    ['Thank you! I am ready.', 'Obrigada! Estou pronta.'])])
    CX = [cx('He is in my class and he learns with me. He is a ___.', 'Ele está na minha turma e aprende comigo. Ele é um aluno.', 'student', 'teacher', 'book'),
          cx('She is in front of the class and she explains the lesson. She is a ___.', 'Ela está na frente da turma e explica a lição. Ela é uma professora.', 'teacher', 'student', 'friend'),
          cx('I play with him and we help each other. He is my ___.', 'Eu brinco com ele e nós nos ajudamos. Ele é o meu amigo.', 'friend', 'teacher', 'library'),
          cx('Today is her first day at school. She is ___.', 'Hoje é o primeiro dia dela na escola. Ela é nova.', 'new', 'smart', 'book'),
          cx('She reads it and turns the pages. It is a ___.', 'Ela lê isso e vira as páginas. É um livro.', 'book', 'friend', 'teacher'),
          cx('He gets ten out of ten on every test. He is very ___.', 'Ele tira dez em todas as provas. Ele é muito inteligente.', 'smart', 'new', 'library')]
    return dict(B=B, X=X, XT=XT, VB=VB, MR=MR, CX=CX)


EPS = [ep06(), ep07(), ep08(), ep09(), ep10()]
