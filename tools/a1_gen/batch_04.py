# Lote 04: posições 30 a 37 do briefs.json (episódios n = 9806, 70011, 30006, 70012, 9807, 7009807, 70013, 30007).
# TROCAS DE OBRA: pos 30: de Peter Pan para The Sound of Music (Peter Pan é piloto)
# TROCAS DE OBRA: pos 34: de Alice's Adventures in Wonderland para Shrek (Alice é piloto)
# TROCAS DE OBRA: pos 35: de Alice's Adventures in Wonderland para Harry Potter and the Philosopher's Stone (Alice é piloto e repetia o pos 34)
# Observações de recorte: pos 30 foca em This is / These are; pos 31 em His / Her name is; pos 32 em have / has;
# pos 33 em Do you have…?; pos 34 em He's / She's + adjetivo e has (cabelo, olhos); pos 35 em Is he/she + jeito (very);
# pos 36 em What does he look like? (has, wears); pos 37 em How do you feel? / I feel…


# ---------- helpers ----------
def hot(e, x, y, en, pt, say, sayPt):
    return dict(e=e, x=x, y=y, en=en, pt=pt, say=say, sayPt=sayPt)


def gap(q, pt, opts, a, why):
    return dict(q=q, pt=pt, opts=opts, a=a, why=why)


def trap(opts, a, why, q='Qual frase está certa?'):
    return dict(q=q, opts=opts, a=a, why=why)


def cx(text, pt, o1, o2, o3):
    return dict(text=text, pt=pt, opts=[o1, o2, o3], a=0)


def qz(q, pt, opts, a, line, why):
    return dict(q=q, pt=pt, opts=opts, a=a, line=line, why=why)


def verb(v, ic, pt, fi, fh, exen, expt, hs=None):
    hs = hs or v + 's'
    return dict(v=v, ic=ic, pt=pt, f=[['eu', fi], ['ele/ela', fh]], ex=[exen, expt],
                note='**%s** = %s. Com he/she: **%s**.' % (v, pt, hs))


def exp(ic, en, tag, pt, use, exen, expt):
    return dict(ic=ic, en=en, tag=tag, pt=pt, use=use, ex=[exen, expt])


def rnd(say, opts, a, why):
    return dict(fig='🎧', say=say, ask='Qual palavra você ouviu?', opts=opts, a=a, why=why)


def hunt(say, opts, a, why, pic=False):
    d = dict(fig='🎧', say=say, ask='Ouça e toque na figura.' if pic else 'Ouça e toque na palavra.', opts=opts, a=a, why=why)
    if pic:
        d['opts'] = [[o, ''] for o in opts]
        d['pic'] = 1
    return d


def T(*pairs):
    return [list(p) for p in pairs]


def prod(prompt, ph, chips, model, check, kw, tips, ok, reply):
    return dict(prompt=prompt, ph=ph, chips=chips, model=model, check=check, kw=kw, tips=tips, ok=ok, reply=reply)


def mission(ic, name, desc, prompt, chips, model, check, kw, tips, ok, reply, ph='Escreva a sua resposta aqui…'):
    return dict(ic=ic, name=name, desc=desc, data=prod(prompt, ph, chips, model, check, kw, tips, ok, reply))


def page(label, slots, end):
    return dict(label=label, slots=[dict(cat=c, opts=[list(o) for o in os]) for c, os in slots], end=list(end))


def mtrap(ask, opts, a, why, say=None):
    d = dict(ask=ask, opts=opts, a=a, why=why)
    if say:
        d['say'] = say
    return d


def mgap(text, pt, opts, a, why, say):
    return dict(text=text, pt=pt, opts=opts, a=a, why=why, say=say)


def expq(ask, opts, a, why):
    return dict(ask=ask, opts=opts, a=a, why=why)


def rsm(*sc):
    keys = 'review dquiz rdg pat vplay build order soundlab produce wrap dictate balloons scene sbuild scenebuild'.split()
    return {k: sc[i % len(sc)] for i, k in enumerate(keys)}


def lab(short, title, say, what, how, pt, ex, pairs, tip, phrase, rounds):
    return dict(short=short, title=title, say=say, intro=dict(what=what, how=how, pt=pt), ex=ex, pairs=pairs, tip=tip, phrase=phrase, rounds=rounds)


# ---------- 30 · The Sound of Music · This is / These are ----------
def ep30():
    MARIA = 'p:short:6b4423:f4c7a1:7f8fa6:none:dress'
    LIESL = 'p:long:4a2f1d:f4c7a1:e8dcc4:bow:dress'
    FRIED = 'p:short:3b2a1a:f4c7a1:2c5282:none:shirt'
    B = dict(
        title='My Family, My Friends · This is / These are',
        sub='Apresentar pessoas com This is… (uma) e These are… (várias)',
        pattern_label='This is… · These are…',
        why='Hoje você aprende a apresentar pessoas como a Maria faz ao chegar: This is… para uma pessoa e These are… para várias.',
        vocab=[['Family', 'Família', 'Soa como “FÉ-mi-li”.'], ['Photo', 'Foto', 'Soa como “FÔU-tou”.'],
               ['Home', 'Casa, lar', 'Soa como “RÔUM”.'], ['Brother', 'Irmão', 'Soa como “BRÂ-dher”.'],
               ['Sister', 'Irmã', 'Soa como “SÍS-ter”.'], ['Friend', 'Amigo(a)', 'Soa como “FRÉND”.']],
        balloons=[['📸', 'photo'], ['👨‍👩‍👧‍👦', 'family'], ['🏠', 'home'], ['👦', 'brother'], ['👧', 'sister'], ['🤝', 'friend']],
        cover_art=dict(s='home1', items=[['📸', 104, 56, 20, 'bob'], ['👨‍👩‍👧‍👦', 138, 44, 12, 'bob'], ['🏠', 84, 34, 12, 'bob']], seed='sm1'),
        cover_sub='This is… e These are… Em 10 minutos você apresenta a família e os amigos',
        cover_say='A Maria chega a uma casa nova e conhece uma família grande. Como apresentar uma pessoa? E várias pessoas ao mesmo tempo?',
        wrap_recap=[['This is my brother.', 'Este é o meu irmão.'], ['These are my sisters.', 'Estas são as minhas irmãs.'],
                    ['Look at this photo!', 'Olhe esta foto!'], ['This is your new home!', 'Esta é a sua nova casa!']],
        teaser=dict(t='Over the River and Through the Wood', d='Próximo padrão: dizer quem é cada parente e o nome dele(a), com His name is… e Her name is…'),
        cast={'Maria': ['👩', '#2b6cb0'], 'Liesl': ['👧', '#d64a8a'], 'Friedrich': ['👦', '#2f855a']},
        lines=[['Maria', "Hello! I'm Maria. I'm new here.", 'Olá! Eu sou a Maria. Sou nova aqui.'],
               ['Liesl', 'Welcome, Maria! This is my family.', 'Bem-vinda, Maria! Esta é a minha família.'],
               ['Liesl', 'This is my brother, Friedrich.', 'Este é o meu irmão, o Friedrich.'],
               ['Friedrich', 'Hi, Maria! These are my sisters.', 'Oi, Maria! Estas são as minhas irmãs.'],
               ['Maria', 'Nice to meet you! Who is in the photo?', 'Prazer em conhecer vocês! Quem está na foto?'],
               ['Liesl', 'These are my friends. This is Rolf.', 'Estes são os meus amigos. Este é o Rolf.'],
               ['Friedrich', 'Come in, Maria. This is your new home!', 'Entre, Maria. Esta é a sua nova casa!'],
               ['Maria', 'Thank you! I love this family.', 'Obrigada! Eu adoro esta família.']],
        quiz=[qz('What is Friedrich?', 'O que o Friedrich é para a Liesl?', [['👧', 'A friend'], ['👦', 'A brother'], ['🎩', 'A teacher']], 1, 2, 'Liesl diz: “This is my brother, Friedrich.”'),
              qz('Who is in the photo?', 'Quem está na foto?', [['👫', 'Friends'], ['🐕', 'A dog'], ['🏠', 'A house']], 0, 5, 'Liesl diz: “These are my friends.”'),
              qz('Who is new here?', 'Quem é nova ali?', [['👦', 'Friedrich'], ['👧', 'Liesl'], ['👩', 'Maria']], 2, 0, 'Maria diz: “I’m new here.”')],
        rdg_q=dict(q='Qual frase apresenta várias pessoas?', o=['This is my friends.', 'This are my friends.', 'These are my friends.'], a=2,
                   why='Para várias pessoas use **These are** + plural: These are my friends.'),
        dictate=[['This is my family.', 'Esta é a minha família.'], ['These are my sisters.', 'Estas são as minhas irmãs.'],
                 ['Look at this photo!', 'Olhe esta foto!'], ['Welcome to my home.', 'Bem-vindo à minha casa.']],
        produce=prod('A Maria pergunta: *Who is in your photo?* **Apresente uma pessoa com This is… e duas ou mais com These are…, sempre com my.**',
                     'Ex.: This is my brother. These are my friends.', ['This is', 'These are'],
                     'This is my brother, Leo. These are my friends. I love my family.',
                     ['Usei This is… para uma pessoa?', 'Usei These are… para várias?', 'Usei my (meu, minha)?'],
                     [r'\bthis is\b\s+\w+', r'\bthese are\b\s+\w+', r'\bmy\s+\w+'],
                     [T(('This is my sister.', 'Esta é a minha irmã.'), ('This is Ana.', 'Esta é a Ana.')),
                      T(('These are my friends.', 'Estes são os meus amigos.'), ('These are my brothers.', 'Estes são os meus irmãos.')),
                      T(('my mom', 'minha mãe'), ('my family', 'minha família'))],
                     ['Uma pessoa! 🙋', 'Várias pessoas! 👥', 'Meu, minha! 💙'],
                     ['Nice to meet them! You have a great family!', 'Prazer em conhecê-los! Você tem uma ótima família!']),
        rs=rsm('home1', 'living', 'hall', 'yard', 'kitchen', 'park2', 'bedroom'),
        sc='home1')
    X = dict(
        n=9806, review=True, names=('Maria', 'Liesl'),
        stage=dict(rs='home1', chars=[[MARIA, 26, 0, 1.0], [LIESL, 54, 1, 1.0], [FRIED, 82, 1, 0.95]]),
        obra=dict(name='The Sound of Music', kind='🎬 Filme musical · 1965', year='1965',
                  text='Filme musical americano de 1965, dirigido por Robert Wise, com Julie Andrews. Na Áustria, a jovem Maria vira governanta dos sete filhos de um capitão viúvo e ensina a família a cantar. É baseado num musical da Broadway de 1959.',
                  line=['The hills are alive!', 'As colinas estão vivas! (verso da canção-tema)'],
                  pa=dict(t='andes', e=['🏔️', '🎶', '👩'], p='e', v=1)),
        gancho=['Liesl', 'Welcome, Maria! This is my family.', 'Bem-vinda, Maria! Esta é a minha família.'],
        hot=[hot('📸', 14, 16, 'photo', 'foto', 'This is my family photo.', 'Esta é a minha foto de família.'),
             hot('🏠', 40, 14, 'home', 'casa, lar', 'This is my home.', 'Esta é a minha casa.'),
             hot('👦', 66, 14, 'brother', 'irmão', 'This is my brother.', 'Este é o meu irmão.'),
             hot('👧', 88, 16, 'sister', 'irmã', 'These are my sisters.', 'Estas são as minhas irmãs.'),
             hot('🤝', 12, 82, 'friend', 'amigo(a)', 'These are my friends.', 'Estes são os meus amigos.')],
        gap=[gap('___ is my brother.', 'Este é o meu irmão.', ['This', 'These', 'They'], 0, 'Uma pessoa: **This is**…'),
             gap('___ are my sisters.', 'Estas são as minhas irmãs.', ['This', 'These', 'It'], 1, 'Várias pessoas: **These are**…'),
             gap('This ___ my friend.', 'Este é o meu amigo.', ['are', 'am', 'is'], 2, 'Com **this** (uma pessoa) o verbo é **is**.'),
             gap('These ___ my friends.', 'Estes são os meus amigos.', ['are', 'is', 'am'], 0, 'Com **these** (várias) o verbo é **are**.')],
        trap=[trap(['These is my sisters.', 'This are my sister.', 'These are my sisters.'], 2, 'Várias pessoas: **These are** + plural (sisters).'),
              trap(['This is my friend.', 'These is my friend.', 'This are my friend.'], 0, 'Uma pessoa: **This is** my friend.')],
        sticker=dict(title='Maria e a família', sub='The Sound of Music · 1965', rs='home1', chars=[[MARIA, 34, 0, 1.0], [LIESL, 68, 1, 1.0]]),
        speakers={'Maria': MARIA, 'Liesl': LIESL, 'Friedrich': FRIED},
        rule=dict(who=MARIA, head='This is… · These are…', sub='Uma pessoa ou várias: this → these, is → are.',
                  say=['This is my brother. These are my sisters.', 'Este é o meu irmão. Estas são as minhas irmãs.'],
                  formula=[dict(from_=[['This', 0], ['is', 1], ['my friend.', 3]], to=[['These', 0], ['are', 1], ['my friends.', 3]], say='These are my friends.',
                                note='Uma pessoa: **This is**. Duas ou mais: **These are**. A palavra também ganha **-s**: friend → friends.'),
                           dict(from_=[['Who', 0], ['is', 1], ['this?', 3]], to=[['This', 0], ['is', 1], ['Rolf.', 2]], say='This is Rolf.',
                                note='Para dizer quem é, comece com **This is** + nome.')],
                  uses=[dict(ico='🙋', tag='Uma pessoa', en='This is my brother.', pt='Este é o meu irmão.'),
                        dict(ico='👥', tag='Várias pessoas', en='These are my sisters.', pt='Estas são as minhas irmãs.'),
                        dict(ico='📸', tag='Mostrar a foto', en='Look at this photo!', pt='Olhe esta foto!')],
                  rules=[dict(tag='This is', c=0, text='**Uma** pessoa (ou coisa) perto de você.', ex='This is my mom.'),
                         dict(tag='These are', c=2, text='**Duas ou mais** pessoas (ou coisas).', ex='These are my parents.'),
                         dict(tag='my', c=1, text='**my** = meu, minha, meus, minhas. Não muda no plural.', ex='my brother → my sisters')],
                  tips=['Em português “este / estes” mudam por gênero. Em inglês só importa **uma ou várias**: this / these.']),
        mission_ic='👨‍👩‍👧')
    XT = dict(
        exp=[exp('🤝', "It's a pleasure to meet you.", 'Expressão', 'É um prazer conhecer você.', 'Jeito **educado** de dizer prazer, ao conhecer alguém.', "It's a pleasure to meet you, Liesl.", 'É um prazer conhecer você, Liesl.'),
             exp('🛋️', 'Make yourself at home.', 'Expressão', 'Fique à vontade.', 'Para o visitante se sentir **em casa**.', 'Come in. Make yourself at home.', 'Entre. Fique à vontade.'),
             exp('🚪', 'Come on in!', 'Informal', 'Entra aí! / Pode entrar!', 'Convite **animado** para alguém entrar.', 'Come on in, Maria!', 'Entra aí, Maria!'),
             exp('👪', 'What a big family!', 'Expressão', 'Que família grande!', 'Quando você acha a família **grande e bonita**.', 'Wow, what a big family!', 'Uau, que família grande!')],
        exp_scene=dict(rs='living', lines=[
            ['Liesl', '**Come on in**, Maria!', 'Entra aí, Maria!'],
            ['Maria', "Thank you. **It's a pleasure to meet you** all.", 'Obrigada. É um prazer conhecer todos vocês.'],
            ['Friedrich', '**Make yourself at home**!', 'Fique à vontade!'],
            ['Maria', 'Wow! **What a big family**!', 'Uau! Que família grande!'],
            ['Liesl', 'Yes! Sit here with us.', 'Sim! Sente aqui com a gente.'],
            ['Maria', 'I love it here.', 'Eu adoro estar aqui.']]),
        lab=lab('th sonoro', 'Laboratório de sons: o “th” de this', 'O “th” de this e these não existe em português. Vamos treinar com a família!',
                'O **th** de **this**, **these** e **they** é um som vibrado: a língua fica entre os dentes e a voz vibra.',
                'Ponha a pontinha da língua entre os dentes da frente e solte o ar fazendo a garganta vibrar, como um “z” com a língua para fora. Não diga “d” nem “z”.',
                'Em português não temos esse som, e muita gente diz “dis” ou “zis”. Cuidado: **they** (eles) ≠ **day** (dia).',
                [['this', 'DHÍS', 'este, esta', 'língua entre os dentes'], ['these', 'DHÍZ', 'estes, estas', 'vibre a língua e a garganta'], ['they', 'DHÊI', 'eles, elas', 'não comece com “d”']],
                [['they', 'day', 'th: língua entre os dentes · d: língua atrás dos dentes'], ['then', 'den', '“então” × “covil”'], ['there', 'dare', '“lá” × “ousar”']],
                'Morda de leve a ponta da língua e diga “zzz”. Esse é o “th” de this.',
                ['These are my friends.', 'Estes são os meus amigos.'],
                [rnd('they', ['day', 'they'], 1, 'Em **they** a língua fica entre os dentes. **Day** (dia) começa com “d”.'),
                 rnd('then', ['then', 'den'], 0, '**Then** (então) tem o “th” vibrado. **Den** (covil) começa com “d”.'),
                 rnd('dare', ['there', 'dare'], 1, '**Dare** (ousar) começa com “d”. **There** (lá) começa com o “th”.')]),
        hunt=[hunt('day', ['they', 'day'], 1, '**day** (dia) começa com “d”.'),
              hunt('photo', ['📸', '🏠', '👨‍👩‍👧'], 0, '**photo** = foto.', True),
              hunt('then', ['then', 'den'], 0, '**then** (então) tem o “th” vibrado.'),
              hunt('family', ['🏠', '👨‍👩‍👧', '📸'], 1, '**family** = família.', True)])
    VB = dict(title='Verbos para apresentar', tip='Quatro verbos: introduce, know, look e talk.', items=[
        verb('introduce', '🤝', 'apresentar', 'I introduce my friend.', 'Liesl introduce**s** her brother.', 'I introduce my brother.', 'Eu apresento o meu irmão.'),
        verb('know', '🧠', 'conhecer, saber', 'I know Rolf.', 'Maria know**s** the song.', 'I know your sister.', 'Eu conheço a sua irmã.'),
        verb('look', '👀', 'olhar', 'I look at the photo.', 'Friedrich look**s** at the photo.', 'I look at my family.', 'Eu olho para a minha família.'),
        verb('talk', '🗣️', 'conversar, falar', 'I talk to my sister.', 'Liesl talk**s** to Maria.', 'I talk to my friends.', 'Eu converso com os meus amigos.')])
    MR = dict(
        mold=[page('Apresentar uma pessoa', [('frase', [('This is', 'este(a) é')]), ('pessoa', [('my brother', 'meu irmão'), ('my sister', 'minha irmã'), ('my friend', 'meu amigo'), ('my mom', 'minha mãe'), ('my dad', 'meu pai'), ('my teacher', 'minha professora')])], ('.', '.')),
              page('Apresentar várias pessoas', [('frase', [('These are', 'estes(as) são')]), ('pessoas', [('my sisters', 'minhas irmãs'), ('my friends', 'meus amigos'), ('my parents', 'meus pais'), ('my brothers', 'meus irmãos')])], ('.', '.')),
              page('Mostrar e elogiar', [('frase', [('Look at', 'olhe'), ('I love', 'eu adoro')]), ('o quê', [('this photo', 'esta foto'), ('my family', 'minha família'), ('my home', 'minha casa'), ('these photos', 'estas fotos')])], ('!', '!'))],
        speak=[["This is my brother. These are my sisters.", 'Este é o meu irmão. Estas são as minhas irmãs.'], ['Come on in! Make yourself at home.', 'Entra aí! Fique à vontade.']],
        trap=[mtrap('“Make yourself at home” quer dizer…', ['Vá para casa.', 'Fique à vontade.', 'Faça a sua casa.'], 1, '**Make yourself at home** = fique à vontade.', 'Make yourself at home.'),
              mtrap('Qual frase está certa?', ['Come in on!', 'On come in!', 'Come on in!'], 2, 'O convite informal é **Come on in!**', 'Come on in!')],
        gap=[mgap('What a ___ family!', 'Que família grande!', ['big', 'much', 'many'], 0, '**What a** + adjetivo + substantivo: What a **big** family!', 'What a big family!'),
             mgap("It's a ___ to meet you.", 'É um prazer conhecer você.', ['please', 'pleased', 'pleasure'], 2, "**pleasure** = prazer: It's a **pleasure**.", "It's a pleasure to meet you.")],
        expq=[expq('Seu amigo está esperando na porta. O que você diz?', ['What a big family!', 'Come on in!', "It's a pleasure to meet you."], 1, '**Come on in!** convida a entrar.'),
              expq('Seu amigo entrou na sua casa, meio sem jeito. O que você diz?', ["It's a pleasure to meet you.", 'Come on in!', 'Make yourself at home.'], 2, '**Make yourself at home.** = fique à vontade.'),
              expq('Você vê uma foto com muitas pessoas da família.', ['What a big family!', 'Come on in!', 'Make yourself at home.'], 0, '**What a big family!** = que família grande!')],
        missions=[mission('👨‍👩‍👧', 'Minha família na foto', 'Apresente pessoas com This is e These are.',
                          'Você mostra uma foto para um colega. **Apresente uma pessoa com This is… e duas ou mais com These are…**',
                          ['This is', 'These are'], 'This is my sister, Ana. These are my friends.',
                          ['Usei This is…?', 'Usei These are…?', 'Disse quem é com my?'],
                          [r'\bthis is\b\s+\w+', r'\bthese are\b\s+\w+', r'\bmy\s+\w+'],
                          [T(('This is my sister.', 'Esta é a minha irmã.')), T(('These are my friends.', 'Estes são os meus amigos.')), T(('my brother', 'meu irmão'), ('my friends', 'meus amigos'))],
                          ['Uma pessoa! 🙋', 'Várias pessoas! 👥', 'Meu, minha! 💙'],
                          ['Nice photo! I love your family!', 'Que foto legal! Eu adoro a sua família!']),
                  mission('🚪', 'Visita em casa', 'Receba alguém com as expressões.',
                          'Um amigo chega à sua casa. **Mande-o entrar (Come on in), diga para ele ficar à vontade e apresente a sua família com This is…**',
                          ['Come on in!'], 'Come on in! Make yourself at home. This is my family.',
                          ['Mandei entrar?', 'Pedi para ficar à vontade?', 'Apresentei com This is…?'],
                          [r'\bcome on in\b', r'\bmake yourself at home\b', r'\bthis is\b'],
                          [T(('Come on in!', 'Entra aí!')), T(('Make yourself at home.', 'Fique à vontade.')), T(('This is my family.', 'Esta é a minha família.'))],
                          ['Convite feito! 🚪', 'Visita à vontade! 🛋️', 'Família apresentada! 👪'],
                          ['Thank you! What a big family!', 'Obrigado! Que família grande!'])])
    CX = [cx('We take a ___ to remember this day.', 'Tiramos uma foto para lembrar deste dia.', 'photo', 'brother', 'friend'),
          cx('My mom, my dad, my sister and I are one ___.', 'Minha mãe, meu pai, minha irmã e eu somos uma família.', 'family', 'photo', 'home'),
          cx("My dad's son is my ___.", 'O filho do meu pai é o meu irmão.', 'brother', 'sister', 'friend'),
          cx("My mom's daughter is my ___.", 'A filha da minha mãe é a minha irmã.', 'sister', 'brother', 'family'),
          cx('I am not at work. I am at ___ with my family.', 'Não estou no trabalho. Estou em casa com a minha família.', 'home', 'photo', 'brother'),
          cx('Pedro is not my brother, but I like him a lot. He is my ___.', 'O Pedro não é meu irmão, mas eu gosto muito dele. Ele é meu amigo.', 'friend', 'sister', 'family')]
    return dict(B=B, X=X, XT=XT, VB=VB, MR=MR, CX=CX)


# ---------- 31 · Over the River and Through the Wood · His / Her name is ----------
def ep31():
    TOM = 'p:short:6b4423:f4c7a1:2f855a:none:shirt'
    SAM = 'p:cap:2d2d2d:c68642:2b6cb0:none:shirt'
    GRAN = 'p:bun:d0d0d0:f4c7a1:8e44ad:glasses:dress'
    B = dict(
        title='Meet My Grandma · His name is… · Her name is…',
        sub='Dizer quem é cada parente (He’s / She’s my…) e como ele ou ela se chama',
        pattern_label='His name is… · Her name is…',
        why='Hoje você aprende a apresentar parentes: dizer quem é (She’s my aunt) e o nome (Her name is Kate).',
        vocab=[['Grandma', 'Vovó', 'Soa como “GRÉN-ma”.'], ['Grandpa', 'Vovô', 'Soa como “GRÉN-pa”.'], ['Aunt', 'Tia', 'Soa como “ÉNT”.'],
               ['Uncle', 'Tio', 'Soa como “ÂN-kol”.'], ['Cousin', 'Primo(a)', 'Soa como “KÂ-zin”.'], ['Baby', 'Bebê', 'Soa como “BÊI-bi”.'],
               ['House', 'Casa', 'Soa como “RÁUS”.']],
        balloons=[['👵', 'grandma'], ['👴', 'grandpa'], ['👩', 'aunt'], ['👨', 'uncle'], ['🧒', 'cousin'], ['👶', 'baby'], ['🏡', 'house']],
        cover_art=dict(s='home1', items=[['🛷', 104, 56, 20, 'bob'], ['🥧', 138, 44, 12, 'bob'], ['👵', 84, 34, 12, 'bob']], seed='ov1'),
        cover_sub='His name is… Her name is… Em 10 minutos você apresenta toda a família',
        cover_say='É Dia de Ação de Graças e a família toda vai à casa da vovó. Tem tia, tio, primo e bebê. Como dizer quem é quem e o nome de cada um?',
        wrap_recap=[["She's my aunt.", 'Ela é a minha tia.'], ['Her name is Kate.', 'O nome dela é Kate.'], ["He's my grandpa.", 'Ele é o meu avô.'], ['His name is Joe.', 'O nome dele é Joe.']],
        teaser=dict(t='Little Women', d='Próximo padrão: falar de quem você tem na família, com have e has'),
        cast={'Tom': ['👦', '#2f855a'], 'Sam': ['🧢', '#2b6cb0'], 'Grandma': ['👵', '#8e44ad']},
        lines=[['Tom', 'Sam, this is my grandma. Her name is Rose.', 'Sam, esta é a minha avó. O nome dela é Rose.'],
               ['Grandma', 'Hello, Sam! Welcome to my house!', 'Olá, Sam! Bem-vindo à minha casa!'],
               ['Sam', 'Thank you! Who is he?', 'Obrigado! Quem é ele?'],
               ['Tom', "He's my grandpa. His name is Joe.", 'Ele é o meu avô. O nome dele é Joe.'],
               ['Sam', 'And who is she? Is she your aunt?', 'E quem é ela? Ela é a sua tia?'],
               ['Tom', "Yes, she is. Her name is Kate. He's my uncle.", 'Sim, é. O nome dela é Kate. Ele é o meu tio.'],
               ['Sam', 'Is the baby your cousin?', 'O bebê é o seu primo?'],
               ['Tom', 'Yes, he is! His name is Max.', 'Sim, é! O nome dele é Max.']],
        quiz=[qz("What is the grandma's name?", 'Qual é o nome da avó?', [['👵', 'Rose'], ['👩', 'Kate'], ['👴', 'Joe']], 0, 0, 'Tom diz: “Her name is Rose.”'),
              qz('Who is Joe?', 'Quem é o Joe?', [['👨', 'The uncle'], ['👴', 'The grandpa'], ['🧒', 'The cousin']], 1, 3, 'Tom diz: “He’s my grandpa. His name is Joe.”'),
              qz('Who is Max?', 'Quem é o Max?', [['👴', 'The grandpa'], ['👩', 'The aunt'], ['👶', 'The baby']], 2, 7, 'Tom diz: “His name is Max.” e Sam fala do bebê.')],
        rdg_q=dict(q='Como se diz “O nome dele é Joe”?', o=['He name is Joe.', 'His name is Joe.', 'Her name is Joe.'], a=1,
                   why='**His** = dele (homem). **Her** = dela (mulher).'),
        dictate=[["She's my aunt.", 'Ela é a minha tia.'], ['Her name is Kate.', 'O nome dela é Kate.'], ["He's my uncle.", 'Ele é o meu tio.'], ['His name is Max.', 'O nome dele é Max.']],
        produce=prod('Sam pergunta: *Who is in your family?* **Fale de duas pessoas: diga quem são (He’s / She’s my…) e o nome (His / Her name is…).**',
                     "Ex.: She's my aunt. Her name is Ana.", ["She's my…", 'Her name is…'],
                     "She's my aunt. Her name is Ana. He's my cousin. His name is Leo.",
                     ['Disse quem é a pessoa (He’s / She’s my…)?', 'Disse o nome (His / Her name is…)?', 'Falei de duas pessoas?'],
                     [r"\b(?:he|she)(?:['’]s| is)\s+my\s+\w+", r'\b(?:his|her) name is\s+\w+', r"(?:\b(?:he|she)(?:['’]s| is)\s+my\s+\w+[\s\S]*){2}"],
                     [T(("She's my aunt.", 'Ela é a minha tia.'), ("He's my uncle.", 'Ele é o meu tio.')),
                      T(('Her name is Ana.', 'O nome dela é Ana.'), ('His name is Leo.', 'O nome dele é Leo.')),
                      T(("She's my grandma.", 'Ela é a minha avó.'), ("He's my cousin.", 'Ele é o meu primo.'))],
                     ['Parentesco certo! 👪', 'Nome dito! 🏷️', 'Duas pessoas! ✌️'],
                     ['Nice family! I love the names!', 'Que família legal! Eu adoro os nomes!']),
        rs=rsm('home1', 'kitchen', 'living', 'yard', 'hall', 'bedroom', 'park2'),
        sc='kitchen')
    X = dict(
        n=70011, review=True, names=('Tom', 'Sam'),
        stage=dict(rs='kitchen', chars=[[TOM, 26, 0, 1.0], [SAM, 54, 1, 1.0], [GRAN, 82, 1, 0.95]]),
        obra=dict(name='Over the River and Through the Wood', kind='🎶 Canção de Ação de Graças · 1844', year='1844',
                  text='Poema da escritora americana Lydia Maria Child, de 1844, que virou canção. Uma família vai de trenó, sobre o rio e pela floresta, até a casa do avô no Dia de Ação de Graças.',
                  line=['Over the river and through the wood', 'Sobre o rio e pela floresta (primeiro verso)'],
                  pa=dict(t='snowvillage', e=['🛷', '🥧', '🏡'], p='a', v=0)),
        gancho=['Tom', 'Sam, this is my grandma. Her name is Rose.', 'Sam, esta é a minha avó. O nome dela é Rose.'],
        hot=[hot('👵', 14, 16, 'grandma', 'vovó', "She's my grandma. Her name is Rose.", 'Ela é a minha avó. O nome dela é Rose.'),
             hot('👴', 40, 14, 'grandpa', 'vovô', "He's my grandpa. His name is Joe.", 'Ele é o meu avô. O nome dele é Joe.'),
             hot('👩', 66, 14, 'aunt', 'tia', "She's my aunt. Her name is Kate.", 'Ela é a minha tia. O nome dela é Kate.'),
             hot('👶', 88, 16, 'baby', 'bebê', "He's a baby. His name is Max.", 'Ele é um bebê. O nome dele é Max.'),
             hot('🏡', 12, 82, 'house', 'casa', 'Welcome to my house!', 'Bem-vindo à minha casa!')],
        gap=[gap('___ name is Rose.', 'O nome dela é Rose.', ['His', 'Her', 'She'], 1, '**Her** = dela. Rose é mulher.'),
             gap('___ name is Joe.', 'O nome dele é Joe.', ['His', 'Her', 'He'], 0, '**His** = dele. Joe é homem.'),
             gap("He's my ___.", 'Ele é o meu tio.', ['house', 'baby', 'uncle'], 2, '**uncle** = tio.'),
             gap('Her name ___ Kate.', 'O nome dela é Kate.', ['are', 'is', 'am'], 1, 'Com **name** (uma coisa) use **is**.')],
        trap=[trap(['He name is Max.', 'His name is Max.', 'Her name is Max.'], 1, 'Max é menino. Use **His** (dele): His name is Max.'),
              trap(['She name is Kate.', 'Her name are Kate.', 'Her name is Kate.'], 2, '**Her name is** Kate. Não use “she name”.')],
        sticker=dict(title='Tom, Sam e a vovó', sub='Over the River and Through the Wood · 1844', rs='kitchen', chars=[[TOM, 34, 0, 1.0], [GRAN, 68, 1, 1.0]]),
        speakers={'Tom': TOM, 'Sam': SAM, 'Grandma': GRAN},
        rule=dict(who=GRAN, head='His name is… · Her name is…', sub='Quem é a pessoa e como ela se chama.',
                  say=["She's my grandma. Her name is Rose.", 'Ela é a minha avó. O nome dela é Rose.'],
                  formula=[dict(from_=[['He', 0], ['is', 1], ['Joe.', 3]], to=[['His', 0], ['name', 2], ['is', 1], ['Joe.', 3]], say='His name is Joe.',
                                note='**He** = ele. Para dizer o nome dele: **His name is**…'),
                           dict(from_=[['She', 0], ['is', 1], ['Kate.', 3]], to=[['Her', 0], ['name', 2], ['is', 1], ['Kate.', 3]], say='Her name is Kate.',
                                note='**She** = ela. Para dizer o nome dela: **Her name is**…')],
                  uses=[dict(ico='👵', tag='Quem é', en="She's my grandma.", pt='Ela é a minha avó.'),
                        dict(ico='🏷️', tag='Nome dela', en='Her name is Rose.', pt='O nome dela é Rose.'),
                        dict(ico='🏷️', tag='Nome dele', en='His name is Joe.', pt='O nome dele é Joe.')],
                  rules=[dict(tag='His name is', c=0, text='**His** = dele. Use para homem ou menino.', ex='His name is Joe.'),
                         dict(tag='Her name is', c=3, text='**Her** = dela. Use para mulher ou menina.', ex='Her name is Kate.'),
                         dict(tag="He's / She's", c=2, text='Antes do nome, diga **quem é**: parentesco com my.', ex="She's my aunt.")],
                  tips=['Cuidado: o nome dela é **her name**, não “she name”. Use **his** para ele e **her** para ela.']),
        mission_ic='👵')
    XT = dict(
        exp=[exp('🎉', 'Welcome to the family!', 'Expressão', 'Bem-vindo à família!', 'Quando alguém **entra para a família** ou o grupo.', 'Welcome to the family, Sam!', 'Bem-vindo à família, Sam!'),
             exp('❤️', 'Family comes first.', 'Expressão', 'A família vem em primeiro lugar.', 'Para dizer que a **família é a prioridade**.', 'Family comes first for Grandma.', 'Para a vovó, a família vem em primeiro lugar.'),
             exp('🏁', 'Here we are!', 'Expressão', 'Chegamos!', 'Quando você **chega ao lugar** depois de uma viagem.', 'Here we are! This is the house.', 'Chegamos! Esta é a casa.'),
             exp('🥧', 'Help yourself!', 'Informal', 'Sirva-se!', 'Ao **oferecer comida** a alguém, sem cerimônia.', 'Help yourself! The pie is for you.', 'Sirva-se! A torta é para você.')],
        exp_scene=dict(rs='kitchen', lines=[
            ['Tom', '**Here we are**, Sam! Look at the house!', 'Chegamos, Sam! Olhe a casa!'],
            ['Grandma', '**Welcome to the family**, Sam!', 'Bem-vindo à família, Sam!'],
            ['Sam', 'Thank you! I love the pie.', 'Obrigado! Eu adoro a torta.'],
            ['Grandma', '**Help yourself**! The pie is for you.', 'Sirva-se! A torta é para você.'],
            ['Tom', 'Grandma says, “**Family comes first**.”', 'A vovó diz: “A família vem em primeiro lugar.”'],
            ['Sam', 'She is right!', 'Ela tem razão!']]),
        lab=lab('h inicial', 'Laboratório de sons: o “h” de house', 'Em português o “h” é mudo. Em inglês ele é um sopro! Vamos treinar com a casa da vovó.',
                'O **h** de **house**, **home** e **hug** é um sopro de ar saindo da garganta, bem suave.',
                'Abra um pouco a boca e solte o ar, como quando você embaça um vidro. Não use o “r” forte do português (“rouse”).',
                'Em português o **h** é mudo, então muita gente apaga o som e diz “ouse”. Cuidado: **hat** (chapéu) ≠ **at** (em); **old** (velho) ≠ **hold** (segurar).',
                [['house', 'RÁUS', 'casa', 'sopre um H suave, sem “r” forte'], ['hug', 'RÂG', 'abraço', 'solte o ar na garganta'], ['home', 'RÔUM', 'lar', 'comece só com o sopro']],
                [['hat', 'at', 'com sopro × sem sopro'], ['heat', 'eat', '“calor” × “comer”'], ['old', 'hold', '“velho” × “segurar”']],
                'Coloque a mão na frente da boca: no “h” você sente o ar quente na mão.',
                ['Her house is a happy home.', 'A casa dela é um lar feliz.'],
                [rnd('hat', ['hat', 'at'], 0, 'Em **hat** (chapéu) há um sopro no começo. **At** (em) começa direto na vogal.'),
                 rnd('old', ['hold', 'old'], 1, '**Old** (velho) começa direto no “o”. **Hold** (segurar) tem o sopro do “h”.'),
                 rnd('heat', ['eat', 'heat'], 1, '**Heat** (calor) tem o sopro do “h”. **Eat** (comer) não tem.')]),
        hunt=[hunt('house', ['🍰', '🏡', '👶'], 1, '**house** = casa.', True),
              hunt('eat', ['heat', 'eat'], 1, '**eat** (comer) começa direto no “i”, sem sopro.'),
              hunt('hug', ['🫂', '🛷', '🥧'], 0, '**hug** = abraço.', True),
              hunt('hold', ['hold', 'old'], 0, '**hold** (segurar) tem o sopro do “h”.')])
    VB = dict(title='Verbos para a visita à vovó', tip='Quatro verbos: come, say, laugh e hug.', items=[
        verb('come', '🚶', 'vir, chegar', 'I come to the big house.', 'Sam come**s** to the party.', 'I come to the party.', 'Eu venho para a festa.'),
        verb('say', '💬', 'dizer', 'I say hello to Grandma.', 'Grandma say**s** “Welcome!”', 'I say hello to my aunt.', 'Eu digo olá para a minha tia.', 'says'),
        verb('laugh', '😂', 'rir', 'I laugh with my cousin.', 'Tom laugh**s** with Sam.', 'I laugh with my cousin.', 'Eu rio com o meu primo.'),
        verb('hug', '🫂', 'abraçar', 'I hug my grandma.', 'Sam hug**s** his uncle.', 'I hug my grandma.', 'Eu abraço a minha avó.')])
    VB['items'][1]['note'] = '**say** = dizer. Com he/she: **says** (lê-se “SEZ”).'
    MR = dict(
        mold=[page('Quem é?', [('quem', [("He's", 'ele é'), ("She's", 'ela é')]), ('parente', [('my grandpa', 'meu avô'), ('my grandma', 'minha avó'), ('my uncle', 'meu tio'), ('my aunt', 'minha tia'), ('my cousin', 'meu primo'), ('a baby', 'um bebê')])], ('.', '.')),
              page('O nome', [('de quem', [('His name is', 'o nome dele é'), ('Her name is', 'o nome dela é')]), ('nome', [('Tom', 'Tom'), ('Kate', 'Kate'), ('Joe', 'Joe'), ('Rose', 'Rose'), ('Max', 'Max')])], ('.', '.')),
              page('Perguntar', [('pergunta', [('Who is he', 'quem é ele'), ('Who is she', 'quem é ela'), ('Is he your cousin', 'ele é seu primo'), ('Is she your aunt', 'ela é sua tia')])], ('?', '?'))],
        speak=[["She's my aunt. Her name is Kate.", 'Ela é minha tia. O nome dela é Kate.'], ['Here we are! Welcome to the family!', 'Chegamos! Bem-vindo à família!']],
        trap=[mtrap('“Help yourself!” quer dizer…', ['Ajude-se!', 'Sirva-se!', 'Me ajude!'], 1, '**Help yourself!** = sirva-se (de comida, bebida).', 'Help yourself!'),
              mtrap('“Family comes first” quer dizer…', ['A família vem em primeiro lugar.', 'A família chega primeiro.', 'A primeira família.'], 0, '**Family comes first** = a família é a prioridade.', 'Family comes first.')],
        gap=[mgap('Welcome to the ___!', 'Bem-vindo à família!', ['please', 'family', 'happy'], 1, 'A expressão é **Welcome to the family!**', 'Welcome to the family!'),
             mgap('Here we ___!', 'Chegamos!', ['are', 'is', 'do'], 0, 'A expressão é **Here we are!**', 'Here we are!')],
        expq=[expq('Vocês chegam ao fim de uma longa viagem.', ['Help yourself!', 'Here we are!', 'Family comes first.'], 1, '**Here we are!** = chegamos!'),
              expq('Seu amigo olha para a torta. Você oferece.', ['Welcome to the family!', 'Here we are!', 'Help yourself!'], 2, '**Help yourself!** = sirva-se!'),
              expq('Um novo primo entra para a família.', ['Welcome to the family!', 'Help yourself!', 'Here we are!'], 0, '**Welcome to the family!** = bem-vindo à família!')],
        missions=[mission('👪', 'Dois parentes', 'Diga quem são e como se chamam.',
                          'Você mostra uma foto de dois parentes. **Diga quem é cada um (He’s / She’s my…) e o nome deles (His / Her name is…).**',
                          ["He's my…", 'Her name is…'], "He's my uncle. His name is Joe. She's my aunt. Her name is Kate.",
                          ['Disse o parentesco?', 'Disse o nome com His / Her name is?', 'Falei de duas pessoas?'],
                          [r"\b(?:he|she)(?:['’]s| is)\s+my\s+\w+", r'\b(?:his|her) name is\s+\w+', r'(?:\b(?:his|her) name is\s+\w+[\s\S]*){2}'],
                          [T(("He's my uncle.", 'Ele é o meu tio.')), T(('His name is Joe.', 'O nome dele é Joe.'), ('Her name is Kate.', 'O nome dela é Kate.')), T(("She's my aunt.", 'Ela é a minha tia.'))],
                          ['Parentesco certo! 👪', 'Nome dito! 🏷️', 'Duas pessoas! ✌️'],
                          ['What a nice family!', 'Que família legal!']),
                  mission('🛷', 'Chegada à casa da vovó', 'Use as expressões do episódio.',
                          'Você chega à casa da vovó com um amigo. **Diga que chegaram (Here we are!), dê boas-vindas à família e ofereça comida (Help yourself!).**',
                          ['Here we are!'], 'Here we are! Welcome to the family! Help yourself!',
                          ['Avisei que chegamos?', 'Dei boas-vindas?', 'Ofereci comida?'],
                          [r'\bhere we are\b', r'\bwelcome to the family\b', r'\bhelp yourself\b'],
                          [T(('Here we are!', 'Chegamos!')), T(('Welcome to the family!', 'Bem-vindo à família!')), T(('Help yourself!', 'Sirva-se!'))],
                          ['Chegamos! 🏁', 'Boas-vindas! 🎉', 'Sirva-se! 🥧'],
                          ['Thank you! The pie is great!', 'Obrigado! A torta está ótima!'])])
    CX = [cx("My mom's mother is my ___.", 'A mãe da minha mãe é a minha avó.', 'grandma', 'aunt', 'baby'),
          cx("My dad's father is my ___.", 'O pai do meu pai é o meu avô.', 'grandpa', 'uncle', 'cousin'),
          cx("My mom's sister is my ___.", 'A irmã da minha mãe é a minha tia.', 'aunt', 'grandma', 'baby'),
          cx("My dad's brother is my ___.", 'O irmão do meu pai é o meu tio.', 'uncle', 'grandpa', 'cousin'),
          cx("My aunt has a son. He is my ___.", 'A minha tia tem um filho. Ele é o meu primo.', 'cousin', 'uncle', 'grandpa'),
          cx('She is only three months old. She drinks milk and sleeps. She is a ___.', 'Ela tem só três meses. Toma leite e dorme. É um bebê.', 'baby', 'aunt', 'grandma')]
    return dict(B=B, X=X, XT=XT, VB=VB, MR=MR, CX=CX)


# ---------- 32 · Little Women · I have / She has ----------
def ep32():
    MARMEE = 'p:bun:5b3a29:f4c7a1:6d4c41:none:dress'
    JO = 'p:long:6b3f26:f4c7a1:c0392b:none:dress'
    BETH = 'p:curly:7a4b2a:f4c7a1:3182ce:bow:dress'
    B = dict(
        title='Our Big Family · I have / She has',
        sub='Falar de quem você tem: I have two sons, she has a husband',
        pattern_label='have · has',
        why='Hoje você aprende a dizer o que e quem você tem: I have… e, com he/she, has…',
        vocab=[['Son', 'Filho', 'Soa como “SÂN”.'], ['Daughter', 'Filha', 'Soa como “DÓ-ter”.'], ['Husband', 'Marido', 'Soa como “RÂS-bend”.'],
               ['Wife', 'Esposa', 'Soa como “UÁIF”.'], ['Kids', 'Crianças, filhos', 'Soa como “KIDZ”.'], ['Heart', 'Coração', 'Soa como “RÁRT”.']],
        balloons=[['👦', 'son'], ['👧', 'daughter'], ['🤵', 'husband'], ['👰', 'wife'], ['🧒', 'kids'], ['❤️', 'heart']],
        cover_art=dict(s='living', items=[['💌', 104, 56, 20, 'bob'], ['❤️', 138, 44, 12, 'bob'], ['👧', 84, 34, 12, 'bob']], seed='lw1'),
        cover_sub='have e has. Em 10 minutos você fala de quem tem a sua família',
        cover_say='A Marmee tem quatro filhas e um marido longe de casa. O que ela tem? E o que cada uma das meninas tem? Hoje você aprende have e has.',
        wrap_recap=[['I have a big family.', 'Eu tenho uma família grande.'], ['She has four daughters.', 'Ela tem quatro filhas.'], ['He has a kind heart.', 'Ele tem um coração bondoso.'], ['I love my kids.', 'Eu amo meus filhos.']],
        teaser=dict(t='There Was an Old Woman Who Lived in a Shoe', d='Próximo padrão: perguntar o que alguém tem, com Do you have…?'),
        cast={'Marmee': ['👩', '#8e44ad'], 'Jo': ['👧', '#c0392b'], 'Beth': ['👧', '#2b6cb0']},
        lines=[['Jo', 'Marmee, look! A letter from Father!', 'Marmee, olhe! Uma carta do papai!'],
               ['Marmee', 'My husband is far away. He has a big heart.', 'O meu marido está longe. Ele tem um grande coração.'],
               ['Beth', 'I have a big family. I have three sisters.', 'Eu tenho uma família grande. Tenho três irmãs.'],
               ['Jo', 'Yes! Marmee has four daughters.', 'Sim! A Marmee tem quatro filhas.'],
               ['Marmee', 'I love my kids with all my heart.', 'Eu amo meus filhos de todo o coração.'],
               ['Beth', 'Jo has a kind heart too.', 'A Jo também tem um coração bondoso.'],
               ['Jo', "Marmee, you have no son. I'm your son!", 'Marmee, você não tem filho homem. Eu sou o seu filho!'],
               ['Marmee', 'You are my daughter, Jo. I love you!', 'Você é a minha filha, Jo. Eu amo você!']],
        quiz=[qz('Marmee has…', 'A Marmee tem…', [['2️⃣', 'two daughters'], ['4️⃣', 'four daughters'], ['👦', 'three sons']], 1, 3, 'Jo diz: “Marmee has four daughters.”'),
              qz('Is the husband at home?', 'O marido está em casa?', [['❌', "No, he isn't"], ['✅', 'Yes, he is'], ['🤷', 'Maybe']], 0, 1, 'Marmee diz: “My husband is far away.”'),
              qz('What does Marmee love with all her heart?', 'O que a Marmee ama de todo o coração?', [['🐱', 'Her cats'], ['🍰', 'Her cakes'], ['👧', 'Her kids']], 2, 4, 'Marmee diz: “I love my kids with all my heart.”')],
        rdg_q=dict(q='Qual frase está certa para falar da Marmee?', o=['Marmee have four daughters.', 'Marmee has four daughters.', 'Marmee haves four daughters.'], a=1,
                   why='Com uma pessoa só (he, she, Marmee) use **has**. Não existe “haves”.'),
        dictate=[['I have a big family.', 'Eu tenho uma família grande.'], ['She has four daughters.', 'Ela tem quatro filhas.'], ['He has a kind heart.', 'Ele tem um coração bondoso.'], ['I love my kids.', 'Eu amo meus filhos.']],
        produce=prod('A Marmee pergunta: *Who is in your family?* **Diga o que você tem (I have…) e o que outra pessoa tem (He has… ou She has…).**',
                     'Ex.: I have two sisters. She has a son.', ['I have', 'He has', 'She has'],
                     'I have two sisters. She has a husband. He has a son.',
                     ['Usei I have…?', 'Usei He has… ou She has…?', 'Falei de família (son, wife, kids…)?'],
                     [r'\bI have\b\s+\w+', r'\b(?:he|she) has\s+\w+', r'\b(?:son|daughter|husband|wife|kids?|sister|brother|mom|dad)s?\b'],
                     [T(('I have a brother.', 'Eu tenho um irmão.'), ('I have two kids.', 'Eu tenho dois filhos.')),
                      T(('She has a husband.', 'Ela tem um marido.'), ('He has a daughter.', 'Ele tem uma filha.')),
                      T(('son', 'filho'), ('wife', 'esposa'))],
                     ['Eu tenho! 🙋', 'Ele ou ela tem! 👩', 'Família! 👪'],
                     ['What a lovely family! I love it!', 'Que família adorável! Eu adoro!']),
        rs=rsm('living', 'home1', 'kitchen', 'bedroom', 'yard', 'hall', 'park2'),
        sc='living')
    X = dict(
        n=30006, review=True, names=('Marmee', 'Jo'),
        stage=dict(rs='living', chars=[[MARMEE, 26, 0, 1.0], [JO, 54, 1, 1.0], [BETH, 82, 1, 0.95]]),
        obra=dict(name='Little Women', kind='📖 Romance · 1868', year='1868',
                  text='Romance da escritora americana Louisa May Alcott, publicado em 1868. Conta a vida das quatro irmãs March (Meg, Jo, Beth e Amy) e da mãe delas, a Marmee, enquanto o pai está longe, na Guerra Civil americana.',
                  line=["Christmas won't be Christmas without any presents.", 'O Natal não será Natal sem presentes. (primeira frase do livro)'],
                  pa=dict(t='attic', e=['📖', '💌', '🎄'], p='f', v=1)),
        gancho=['Jo', 'Marmee, look! A letter from Father!', 'Marmee, olhe! Uma carta do papai!'],
        hot=[hot('👦', 14, 16, 'son', 'filho', 'I have a son.', 'Eu tenho um filho.'),
             hot('👧', 40, 14, 'daughter', 'filha', 'She has a daughter.', 'Ela tem uma filha.'),
             hot('🤵', 66, 14, 'husband', 'marido', 'She has a husband.', 'Ela tem um marido.'),
             hot('👰', 88, 16, 'wife', 'esposa', 'He has a wife.', 'Ele tem uma esposa.'),
             hot('❤️', 12, 82, 'heart', 'coração', 'He has a big heart.', 'Ele tem um grande coração.')],
        gap=[gap('I ___ two sisters.', 'Eu tenho duas irmãs.', ['have', 'has', 'am'], 0, 'Com **I**, use **have**.'),
             gap('She ___ four daughters.', 'Ela tem quatro filhas.', ['have', 'has', 'is'], 1, 'Com **she**, use **has**.'),
             gap('He ___ a kind heart.', 'Ele tem um coração bondoso.', ['haves', 'have', 'has'], 2, 'Com **he**, use **has**.'),
             gap('You ___ a big heart.', 'Você tem um grande coração.', ['has', 'have', 'are'], 1, 'Com **you**, use **have**.')],
        trap=[trap(['She have a son.', 'She has a son.', 'She haves a son.'], 1, 'Com she: **has**. Não existe “haves”.'),
              trap(['I has two kids.', 'I haves two kids.', 'I have two kids.'], 2, 'Com **I**, use **have**: I have two kids.')],
        sticker=dict(title='Marmee e as filhas', sub='Little Women · 1868', rs='living', chars=[[MARMEE, 30, 0, 1.0], [JO, 62, 1, 1.0]]),
        speakers={'Marmee': MARMEE, 'Jo': JO, 'Beth': BETH},
        rule=dict(who=MARMEE, head='have · has', sub='Ter: com he / she, have vira has.',
                  say=['I have four daughters. She has a big heart.', 'Eu tenho quatro filhas. Ela tem um grande coração.'],
                  formula=[dict(from_=[['I', 0], ['have', 1], ['a son.', 3]], to=[['He', 0], ['has', 1], ['a son.', 3]], say='He has a son.',
                                note='Com **I** e **you**: **have**. Com **he** e **she**: **has**.'),
                           dict(from_=[['I', 0], ['have', 1], ['a daughter.', 3]], to=[['She', 0], ['has', 1], ['a daughter.', 3]], say='She has a daughter.',
                                note='Uma só pessoa (he, she, Marmee): **has**.')],
                  uses=[dict(ico='👪', tag='Quem eu tenho', en='I have two kids.', pt='Eu tenho dois filhos.'),
                        dict(ico='👩', tag='Quem ela tem', en='She has a husband.', pt='Ela tem um marido.'),
                        dict(ico='❤️', tag='Jeito de ser', en='He has a kind heart.', pt='Ele tem um coração bondoso.')],
                  rules=[dict(tag='I have · you have', c=0, text='Com **I** e **you**, use **have**.', ex='I have a son. You have a daughter.'),
                         dict(tag='he has · she has', c=3, text='Com **he**, **she** ou o nome de uma pessoa, use **has**.', ex='She has a husband.'),
                         dict(tag='have = ter', c=2, text='“Ter” serve para família, objetos e até sentimentos.', ex='He has a kind heart.')],
                  tips=['Cuidado: **has** não é “haves”. Só mude **have → has** com he / she.']),
        mission_ic='💌')
    XT = dict(
        exp=[exp('🤗', 'Give me a hug!', 'Informal', 'Me dê um abraço!', 'Para **pedir um abraço** a quem você ama.', 'Give me a hug, Mom!', 'Me dê um abraço, mãe!'),
             exp('🎉', 'The more, the merrier!', 'Expressão', 'Quanto mais, melhor!', 'Quando **mais gente** deixa a festa ainda melhor.', 'Come in! The more, the merrier!', 'Entre! Quanto mais, melhor!'),
             exp('📸', 'Say cheese!', 'Informal', 'Diga xis!', 'Antes de **tirar uma foto**, para todo mundo sorrir.', 'Everybody, say cheese!', 'Todo mundo, diga xis!'),
             exp('💖', 'I love you with all my heart.', 'Expressão', 'Eu amo você de todo o coração.', 'Para dizer **muito carinho**, de forma sincera.', 'I love you with all my heart, Jo.', 'Eu amo você de todo o coração, Jo.')],
        exp_scene=dict(rs='living', lines=[
            ['Marmee', 'Everybody, **say cheese**! Look at the photo.', 'Todo mundo, diga xis! Olhem para a foto.'],
            ['Jo', 'Cheese! Beth, **give me a hug**!', 'Xis! Beth, me dê um abraço!'],
            ['Beth', 'Yes, Jo! I love hugs.', 'Sim, Jo! Eu adoro abraços.'],
            ['Marmee', '**The more, the merrier**! Come in, Meg!', 'Quanto mais, melhor! Entre, Meg!'],
            ['Jo', 'I love my family.', 'Eu amo a minha família.'],
            ['Marmee', '**I love you with all my heart**, girls.', 'Eu amo vocês de todo o coração, meninas.']]),
        lab=lab('ow × oh', 'Laboratório de sons: ow × oh', 'Now e no são muito diferentes! Vamos treinar o “ow” e o “oh” com a Marmee.',
                'O **ow** de **now**, **how** e **house** começa com a boca bem aberta (“á”) e termina em “u”. O **oh** de **no**, **home** e **hose** começa em “ô” e termina em “u”.',
                'Em **now** (NÁU) abra bem a boca, como num “á”. Em **no** (NÔU) arredonde os lábios desde o começo, como num “ô”.',
                'Em português “nau” e “nô” existem, mas muita gente fala os dois iguais. Cuidado: **now** (agora) ≠ **no** (não); **house** (casa) ≠ **hose** (mangueira).',
                [['now', 'NÁU', 'agora', 'boca aberta no começo'], ['how', 'RÁU', 'como', 'mesmo som de now'], ['house', 'RÁUS', 'casa', 'boca aberta, termina em u']],
                [['now', 'no', '“agora” × “não”'], ['town', 'tone', '“cidade” × “tom”'], ['house', 'hose', '“casa” × “mangueira”']],
                'Para o “ow”, abra a boca como no “á” de “pá” e feche devagar até o “u”.',
                ['How is your house now?', 'Como está a sua casa agora?'],
                [rnd('no', ['now', 'no'], 1, '**No** (não) começa com o “ô” redondo. **Now** (agora) começa com a boca aberta.'),
                 rnd('house', ['house', 'hose'], 0, '**House** (casa) tem o “ow” aberto. **Hose** (mangueira) tem o “oh” redondo.'),
                 rnd('tone', ['town', 'tone'], 1, '**Tone** (tom) tem o “oh”. **Town** (cidade) tem o “ow” aberto.')]),
        hunt=[hunt('now', ['now', 'no'], 0, '**now** (agora) tem o “ow” aberto.'),
              hunt('heart', ['❤️', '🏠', '🤵'], 0, '**heart** = coração.', True),
              hunt('hose', ['house', 'hose'], 1, '**hose** (mangueira) tem o “oh” redondo.'),
              hunt('house', ['🤵', '👰', '🏠'], 2, '**house** = casa.', True)])
    VB = dict(title='Verbos da família March', tip='Quatro verbos: have, love, call e visit.', items=[
        verb('have', '🤲', 'ter', 'I have two kids.', 'Marmee ha**s** four daughters.', 'I have a big family.', 'Eu tenho uma família grande.', 'has'),
        verb('love', '❤️', 'amar', 'I love my family.', 'Beth love**s** her sisters.', 'I love my kids.', 'Eu amo os meus filhos.'),
        verb('call', '📞', 'ligar, chamar', 'I call my daughter.', 'Jo call**s** her mother.', 'I call my son.', 'Eu ligo para o meu filho.'),
        verb('visit', '🚪', 'visitar', 'I visit my aunt.', 'Beth visit**s** her friend.', 'I visit my grandma.', 'Eu visito a minha avó.')])
    VB['items'][0]['note'] = '**have** = ter. Com he/she vira **has** (é irregular!).'
    MR = dict(
        mold=[page('I have… · You have…', [('quem', [('I have', 'eu tenho'), ('You have', 'você tem')]), ('o quê', [('a son', 'um filho'), ('a daughter', 'uma filha'), ('two kids', 'dois filhos'), ('a big family', 'uma família grande'), ('a kind heart', 'um coração bondoso')])], ('.', '.')),
              page('He has… · She has…', [('quem', [('He has', 'ele tem'), ('She has', 'ela tem')]), ('o quê', [('a wife', 'uma esposa'), ('a husband', 'um marido'), ('three sons', 'três filhos'), ('two daughters', 'duas filhas'), ('a big heart', 'um grande coração')])], ('.', '.')),
              page('Dizer que ama', [('frase', [('I love my kids', 'eu amo meus filhos'), ('I love my husband', 'eu amo meu marido'), ('I love my wife', 'eu amo minha esposa'), ('I love my family', 'eu amo minha família')]), ('como', [('with all my heart', 'de todo o coração'), ('very much', 'muito')])], ('.', '.'))],
        speak=[['I have two kids. She has a son.', 'Eu tenho dois filhos. Ela tem um filho.'], ['Say cheese! Give me a hug!', 'Diga xis! Me dê um abraço!']],
        trap=[mtrap('“Give me a hug” quer dizer…', ['Me dê a mão', 'Me dê um presente', 'Me dê um abraço'], 2, '**hug** = abraço.', 'Give me a hug!'),
              mtrap('Quando se diz “Say cheese!”?', ['Ao tirar uma foto', 'Ao comer queijo', 'Ao pedir a conta'], 0, '**Say cheese!** faz todo mundo sorrir para a foto.', 'Say cheese!')],
        gap=[mgap('The more, the ___!', 'Quanto mais, melhor!', ['more', 'merrier', 'best'], 1, 'A expressão é **The more, the merrier!**', 'The more, the merrier!'),
             mgap('I love you with all my ___.', 'Eu amo você de todo o coração.', ['hand', 'house', 'heart'], 2, 'A expressão é **with all my heart**.', 'I love you with all my heart.')],
        expq=[expq('Você quer abraçar o seu filho.', ['Give me a hug!', 'Say cheese!', 'The more, the merrier!'], 0, '**Give me a hug!** = me dê um abraço!'),
              expq('Alguém vai tirar uma foto da família.', ['The more, the merrier!', 'Say cheese!', 'Give me a hug!'], 1, '**Say cheese!** = diga xis!'),
              expq('Chegam mais convidados e você fica feliz.', ['Say cheese!', 'Give me a hug!', 'The more, the merrier!'], 2, '**The more, the merrier!** = quanto mais, melhor!')],
        missions=[mission('👪', 'Minha família', 'Fale do que você e os outros têm.',
                          'Apresente a sua família. **Diga o que você tem (I have…) e o que outra pessoa tem (He has… ou She has…).**',
                          ['I have', 'She has'], 'I have a brother. He has two kids. She has a husband.',
                          ['Usei I have…?', 'Usei He has / She has…?', 'Falei de família?'],
                          [r'\bI have\b', r'\b(?:he|she) has\b', r'\b(?:son|daughter|husband|wife|kids?|brother|sister|mom|dad|dog)s?\b'],
                          [T(('I have a sister.', 'Eu tenho uma irmã.')), T(('He has a son.', 'Ele tem um filho.'), ('She has two kids.', 'Ela tem dois filhos.')), T(('brother', 'irmão'), ('husband', 'marido'))],
                          ['Eu tenho! 🙋', 'Ele ou ela tem! 👩', 'Família! 👪'],
                          ['Wow, what a family!', 'Uau, que família!']),
                  mission('📸', 'Foto de família', 'Use as expressões do episódio.',
                          'Você vai tirar uma foto com a família. **Peça para todos dizerem xis (Say cheese!), peça um abraço (Give me a hug!) e diga que ama a sua família.**',
                          ['Say cheese!'], 'Say cheese! Give me a hug! I love my family.',
                          ['Pedi o xis?', 'Pedi um abraço?', 'Disse que amo a família?'],
                          [r'\bsay cheese\b', r'\bgive me a hug\b', r'\bI love\b'],
                          [T(('Say cheese!', 'Diga xis!')), T(('Give me a hug!', 'Me dê um abraço!')), T(('I love my family.', 'Eu amo a minha família.'))],
                          ['Xis! 📸', 'Abraço! 🤗', 'Amor! ❤️'],
                          ['Cheese! We love you too!', 'Xis! Nós também amamos você!'])])
    CX = [cx('My brother has a boy. The boy is his ___.', 'O meu irmão tem um menino. O menino é o filho dele.', 'son', 'wife', 'heart'),
          cx('My sister has a girl. The girl is her ___.', 'A minha irmã tem uma menina. A menina é a filha dela.', 'daughter', 'husband', 'kids'),
          cx('Mrs. Silva is married. Her ___ is Mr. Silva.', 'A Sra. Silva é casada. O marido dela é o Sr. Silva.', 'husband', 'wife', 'son'),
          cx('Mr. Silva is married. His ___ is Mrs. Silva.', 'O Sr. Silva é casado. A esposa dele é a Sra. Silva.', 'wife', 'daughter', 'heart'),
          cx('Ana has two boys and one girl. She has three ___.', 'A Ana tem dois meninos e uma menina. Ela tem três filhos.', 'kids', 'wife', 'heart'),
          cx('My ___ beats fast when I run.', 'O meu coração bate rápido quando eu corro.', 'heart', 'son', 'wife')]
    return dict(B=B, X=X, XT=XT, VB=VB, MR=MR, CX=CX)


# ---------- 33 · There Was an Old Woman Who Lived in a Shoe · Do you have…? ----------
def ep33():
    WOMAN = 'p:bun:e0e0e0:f4c7a1:7b2d8e:glasses:dress'
    BEN = 'p:short:8a5a2b:f4c7a1:2b6cb0:none:shirt'
    LUCY = 'p:curly:3b2a1a:e8b48a:d64a8a:bow:dress'
    B = dict(
        title='Cousins Everywhere · Do you have…?',
        sub='Perguntar o que alguém tem: Do you have a gift? Yes, I do. No, I don’t.',
        pattern_label='Do you have…?',
        why='Hoje você aprende a perguntar o que as pessoas têm com Do you have…? e a responder com Yes, I do / No, I don’t.',
        vocab=[['Yard', 'Quintal', 'Soa como “IÁRD”.'], ['Birthday', 'Aniversário', 'Soa como “BÉR-dêi”.'], ['Gift', 'Presente', 'Soa como “GUIFT”.'],
               ['Party', 'Festa', 'Soa como “PÁR-ti”.'], ['Balloon', 'Balão', 'Soa como “ba-LUN”.'], ['Music', 'Música', 'Soa como “MIÚ-zik”.']],
        balloons=[['🏡', 'yard'], ['🎂', 'birthday'], ['🎁', 'gift'], ['🎉', 'party'], ['🎈', 'balloon'], ['🎵', 'music']],
        cover_art=dict(s='yard', items=[['🎈', 104, 56, 20, 'bob'], ['🎁', 138, 44, 12, 'bob'], ['🎂', 84, 34, 12, 'bob']], seed='sh1'),
        cover_sub='Do you have…? Em 10 minutos você pergunta o que os outros têm',
        cover_say='Hoje é aniversário da velhinha do sapato e o quintal está cheio de crianças. Quem tem presente? Quem tem balão? Como perguntar?',
        wrap_recap=[['Do you have a gift?', 'Você tem um presente?'], ['Yes, I do.', 'Sim, eu tenho.'], ["No, I don't.", 'Não, eu não tenho.'], ['Happy birthday!', 'Feliz aniversário!']],
        teaser=dict(t='Shrek', d='Próximo padrão: descrever pessoas com He’s / She’s + adjetivo'),
        cast={'Old Woman': ['👵', '#7b2d8e'], 'Ben': ['👦', '#2b6cb0'], 'Lucy': ['👧', '#d64a8a']},
        lines=[['Old Woman', "Come to the yard, kids! It's my birthday party!", 'Venham ao quintal, crianças! É a minha festa de aniversário!'],
               ['Ben', 'Happy birthday, Mom! This gift is for you.', 'Feliz aniversário, mamãe! Este presente é para você.'],
               ['Old Woman', 'Thank you, Ben! Do you have a balloon, Lucy?', 'Obrigada, Ben! Você tem um balão, Lucy?'],
               ['Lucy', 'Yes, I do! I have a red balloon.', 'Sim, eu tenho! Eu tenho um balão vermelho.'],
               ['Ben', 'Mom, do you have music?', 'Mamãe, você tem música?'],
               ['Old Woman', "No, I don't. Sing and dance with me!", 'Não, eu não tenho. Cantem e dancem comigo!'],
               ['Lucy', 'I sing. Ben dances!', 'Eu canto. O Ben dança!'],
               ['Old Woman', 'I have so many kids. I love this party!', 'Eu tenho tantos filhos. Eu adoro esta festa!']],
        quiz=[qz('What day is it?', 'Que dia é hoje?', [['🎄', 'Christmas'], ['💍', 'A wedding'], ['🎂', 'A birthday']], 2, 0, 'A velhinha diz: “It’s my birthday party!”'),
              qz('Who has a balloon?', 'Quem tem um balão?', [['👦', 'Ben'], ['👧', 'Lucy'], ['👵', 'The Old Woman']], 1, 3, 'Lucy diz: “Yes, I do! I have a red balloon.”'),
              qz('Ben has a ___ for his mom.', 'O Ben tem um ___ para a mãe.', [['🎁', 'gift'], ['🎈', 'balloon'], ['🎵', 'song']], 0, 1, 'Ben diz: “This gift is for you.”')],
        rdg_q=dict(q='Como perguntar “Você tem um presente?”', o=['Are you have a gift?', 'Do you have a gift?', 'Does you have a gift?'], a=1,
                   why='Com **you**, a pergunta começa com **Do**: Do you have…?'),
        dictate=[['Do you have a balloon?', 'Você tem um balão?'], ['Yes, I do.', 'Sim, eu tenho.'], ["No, I don't.", 'Não, eu não tenho.'], ['This gift is for you.', 'Este presente é para você.']],
        produce=prod('A velhinha pergunta: *Do you have a gift? Do you have a balloon?* **Responda com Yes, I do ou No, I don’t, diga o que você tem (I have…) e faça uma pergunta com Do you have…?**',
                     'Ex.: Yes, I do. I have a gift. Do you have music?', ['Yes, I do.', "No, I don't.", 'Do you have…?'],
                     "Yes, I do. I have a gift. No, I don't have a balloon. Do you have music?",
                     ['Respondi com Yes, I do ou No, I don’t?', 'Disse o que tenho com I have…?', 'Fiz uma pergunta com Do you have…?'],
                     [r"\b(?:yes,?\s*i do|no,?\s*i do(?:n['’]t| not))\b", r'\bI have\b\s+\w+', r'\bdo you have\b[^.!?]*\?'],
                     [T(('Yes, I do.', 'Sim, eu tenho.'), ("No, I don't.", 'Não, eu não tenho.')),
                      T(('I have a gift.', 'Eu tenho um presente.'), ('I have a balloon.', 'Eu tenho um balão.')),
                      T(('Do you have music?', 'Você tem música?'), ('Do you have a party?', 'Você tem uma festa?'))],
                     ['Resposta curta certa! ✅', 'Eu tenho! 🎁', 'Boa pergunta! ❓'],
                     ["Great! Let's dance at the party!", 'Ótimo! Vamos dançar na festa!']),
        rs=rsm('yard', 'park2', 'home1', 'living', 'kitchen', 'hall', 'park'),
        sc='yard')
    X = dict(
        n=70012, review=True, names=('Ben', 'Lucy'),
        stage=dict(rs='yard', chars=[[WOMAN, 26, 0, 1.0], [BEN, 54, 1, 1.0], [LUCY, 82, 1, 0.95]]),
        obra=dict(name='There Was an Old Woman Who Lived in a Shoe', kind='🎶 Rima infantil tradicional', year='séc. XVIII',
                  text='Rima infantil tradicional da Inglaterra, das cantigas da “Mamãe Gansa” (Mother Goose). Fala de uma velha que mora num sapato e tem tantos filhos que não sabe o que fazer. Versões impressas já circulavam no século XVIII.',
                  line=['She had so many children.', 'Ela tinha tantas crianças. (da rima)'],
                  pa=dict(t='picnic', e=['👞', '🎂', '🎈'], p='h', v=1)),
        gancho=['Old Woman', "Come to the yard, kids! It's my birthday!", 'Venham ao quintal, crianças! É o meu aniversário!'],
        hot=[hot('🎂', 14, 16, 'birthday', 'aniversário', 'Do you have a cake? Yes, I do.', 'Você tem um bolo? Sim, eu tenho.'),
             hot('🎁', 40, 14, 'gift', 'presente', 'Do you have a gift? Yes, I do.', 'Você tem um presente? Sim, eu tenho.'),
             hot('🎈', 66, 14, 'balloon', 'balão', 'I have a red balloon.', 'Eu tenho um balão vermelho.'),
             hot('🎉', 88, 16, 'party', 'festa', 'I love this party!', 'Eu adoro esta festa!'),
             hot('🎵', 12, 82, 'music', 'música', "Do you have music? No, I don't.", 'Você tem música? Não, eu não tenho.')],
        gap=[gap('___ you have a gift?', 'Você tem um presente?', ['Do', 'Are', 'Does'], 0, 'A pergunta com **you** começa com **Do**.'),
             gap('Yes, I ___.', 'Sim, eu tenho.', ['am', 'do', 'have'], 1, 'Na resposta curta repita o **do**: Yes, I **do**.'),
             gap("No, I ___.", 'Não, eu não tenho.', ['am not', "haven't", "don't"], 2, "Resposta curta negativa: No, I **don't**."),
             gap('Do you ___ music?', 'Você tem música?', ['have', 'has', 'having'], 0, 'Depois de **Do you**, use **have**.')],
        trap=[trap(['Do you has a gift?', 'Do you have a gift?', 'Do you having a gift?'], 1, 'Depois de **Do you**, o verbo fica simples: have.'),
              trap(['Yes, I am.', 'Yes, I does.', 'Yes, I do.'], 2, 'Para “Do you…?”, responda **Yes, I do.**')],
        sticker=dict(title='A festa da velhinha', sub='Old Woman in a Shoe · rima tradicional', rs='yard', chars=[[WOMAN, 30, 0, 1.0], [BEN, 62, 1, 1.0]]),
        speakers={'Old Woman': WOMAN, 'Ben': BEN, 'Lucy': LUCY},
        rule=dict(who=WOMAN, head='Do you have…?', sub='Perguntar o que alguém tem: Do + you + have.',
                  say=['Do you have a gift? Yes, I do.', 'Você tem um presente? Sim, eu tenho.'],
                  formula=[dict(from_=[['You', 0], ['have', 1], ['a gift.', 3]], to=[['Do', 2], ['you', 0], ['have', 1], ['a gift?', 3]], say='Do you have a gift?',
                                note='Na pergunta, entra o **Do** no começo. O **have** continua igual.'),
                           dict(from_=[['Do', 2], ['you', 0], ['have', 1], ['music?', 3]], to=[['Yes,', 2], ['I', 0], ['do.', 2]], say='Yes, I do.',
                                note='Na resposta curta repita o **do**: Yes, I **do**. / No, I **don’t**.')],
                  uses=[dict(ico='❓', tag='Perguntar', en='Do you have a balloon?', pt='Você tem um balão?'),
                        dict(ico='✅', tag='Responder sim', en='Yes, I do.', pt='Sim, eu tenho.'),
                        dict(ico='❌', tag='Responder não', en="No, I don't.", pt='Não, eu não tenho.')],
                  rules=[dict(tag='Do you have', c=0, text='Pergunta com **você**: Do + you + have + coisa?', ex='Do you have a gift?'),
                         dict(tag='Yes, I do', c=2, text='Resposta curta **sim**: repita o **do**.', ex='✗ Yes, I am  →  ✓ Yes, I do'),
                         dict(tag="No, I don't", c=1, text="Resposta curta **não**: **don't** = do + not.", ex="No, I don't.")],
                  tips=['Em português a pergunta só muda a entonação (“Você tem um presente?”). Em inglês, comece com **Do**: Do you have…?']),
        mission_ic='🎈')
    XT = dict(
        exp=[exp('🎂', 'Happy birthday!', 'Expressão', 'Feliz aniversário!', 'Para **parabenizar** alguém no dia do aniversário.', 'Happy birthday, Mom!', 'Feliz aniversário, mamãe!'),
             exp('🕯️', 'Make a wish!', 'Expressão', 'Faça um pedido!', 'Antes de **soprar as velas** do bolo.', 'Make a wish, Lucy!', 'Faça um pedido, Lucy!'),
             exp('🎁', 'This is for you!', 'Expressão', 'Isto é para você!', 'Ao **entregar um presente** a alguém.', 'This is for you, Mom!', 'Isto é para você, mamãe!'),
             exp('👪', 'You look just like your dad!', 'Informal', 'Você é a cara do seu pai!', 'Quando alguém é **muito parecido** com um parente.', 'You look just like your dad, Ben!', 'Você é a cara do seu pai, Ben!')],
        exp_scene=dict(rs='park2', lines=[
            ['Ben', '**Happy birthday**, Mom! **This is for you!**', 'Feliz aniversário, mamãe! Isto é para você!'],
            ['Old Woman', 'A gift! Thank you, Ben!', 'Um presente! Obrigada, Ben!'],
            ['Lucy', 'Look at the cake, Mom. **Make a wish!**', 'Olhe o bolo, mamãe. Faça um pedido!'],
            ['Old Woman', 'I have a wish. I love this party!', 'Eu tenho um pedido. Eu adoro esta festa!'],
            ['Ben', 'Lucy, **you look just like your dad!**', 'Lucy, você é a cara do seu pai!'],
            ['Lucy', 'Ha ha! Come on, dance with me!', 'Ha ha! Vamos, dance comigo!']]),
        lab=lab('i curto × longo', 'Laboratório de sons: i curto × longo', 'Gift e sheep têm “i” diferentes. Vamos treinar o i curto e o i longo!',
                'O **i** curto de **gift**, **big** e **sing** é rápido e relaxado. O **ee** de **sheep**, **eat** e **see** é longo e esticado.',
                'Em **bit** (BIT) a boca fica relaxada e o som é curto, entre “i” e “e”. Em **beat** (BIIT) sorria e estique o som.',
                'Em português só temos um “i”, então muita gente fala **ship** como **sheep**. Cuidado: **ship** (navio) ≠ **sheep** (ovelha); **live** (morar) ≠ **leave** (sair).',
                [['gift', 'GUIFT', 'presente', 'i curto e relaxado'], ['kids', 'KIDZ', 'crianças', 'não estique o i'], ['big', 'BIG', 'grande', 'i curto']],
                [['bit', 'beat', '“pedaço” × “batida”'], ['ship', 'sheep', '“navio” × “ovelha”'], ['live', 'leave', '“morar” × “sair”']],
                'No i longo, sorria como numa foto. No i curto, deixe a boca relaxada.',
                ['Do you have a big gift?', 'Você tem um presente grande?'],
                [rnd('sheep', ['ship', 'sheep'], 1, '**Sheep** (ovelha) tem o i longo. **Ship** (navio) tem o i curto.'),
                 rnd('bit', ['bit', 'beat'], 0, '**Bit** (pedaço) tem o i curto. **Beat** (batida) tem o i longo.'),
                 rnd('leave', ['live', 'leave'], 1, '**Leave** (sair) tem o i longo. **Live** (morar) tem o i curto.')]),
        hunt=[hunt('ship', ['ship', 'sheep'], 0, '**ship** (navio) tem o i curto.'),
              hunt('gift', ['🎵', '🎁', '🎈'], 1, '**gift** = presente.', True),
              hunt('beat', ['bit', 'beat'], 1, '**beat** (batida) tem o i longo.'),
              hunt('balloon', ['🎈', '🎂', '🎁'], 0, '**balloon** = balão.', True)])
    VB = dict(title='Verbos para a festa', tip='Quatro verbos: play, sing, dance e invite.', items=[
        verb('play', '🎲', 'brincar, jogar', 'I play in the yard.', 'Ben play**s** in the yard.', 'I play with my cousin.', 'Eu brinco com o meu primo.'),
        verb('sing', '🎤', 'cantar', 'I sing at the party.', 'Lucy sing**s** a song.', 'I sing a birthday song.', 'Eu canto uma música de aniversário.'),
        verb('dance', '💃', 'dançar', 'I dance with my kids.', 'She dance**s** with Ben.', 'I dance at the party.', 'Eu danço na festa.'),
        verb('invite', '💌', 'convidar', 'I invite my friends.', 'Mom invite**s** the kids.', 'I invite my aunt.', 'Eu convido a minha tia.')])
    MR = dict(
        mold=[page('Do you have…?', [('pergunta', [('Do you have', 'você tem')]), ('coisa', [('a gift', 'um presente'), ('a balloon', 'um balão'), ('music', 'música'), ('a big family', 'uma família grande'), ('a dog', 'um cachorro'), ('a yard', 'um quintal')])], ('?', '?')),
              page('Responder', [('sim ou não', [('Yes,', 'sim,'), ('No,', 'não,')]), ('resposta curta', [('I do.', 'eu tenho.'), ("I don't.", 'eu não tenho.')])], ('.', '.')),
              page('Convidar e festejar', [('frase', [('Come to my', 'venha à minha'), ('I love my', 'eu adoro a minha')]), ('o quê', [('party', 'festa'), ('yard', 'quintal'), ('birthday', 'aniversário'), ('house', 'casa')])], ('!', '!'))],
        speak=[['Do you have a gift? Yes, I do.', 'Você tem um presente? Sim, tenho.'], ['Happy birthday! This is for you!', 'Feliz aniversário! Isto é para você!']],
        trap=[mtrap('“This is for you!” quer dizer…', ['Isto é você!', 'Isto vem de você!', 'Isto é para você!'], 2, '**for you** = para você.', 'This is for you!'),
              mtrap('Qual frase está certa?', ['You look just as your dad!', 'You look just like your dad!', 'You look like just your dad!'], 1, '**look just like** = ser a cara de alguém.', 'You look just like your dad!')],
        gap=[mgap('Make a ___!', 'Faça um pedido!', ['wash', 'wish', 'gift'], 1, '**wish** = desejo, pedido: Make a **wish**!', 'Make a wish!'),
             mgap('Happy ___!', 'Feliz aniversário!', ['birthday', 'party', 'gift'], 0, 'A expressão é **Happy birthday!**', 'Happy birthday!')],
        expq=[expq('É aniversário do seu amigo hoje.', ['Make a wish!', 'This is for you!', 'Happy birthday!'], 2, '**Happy birthday!** = feliz aniversário!'),
              expq('Você entrega um presente.', ['This is for you!', 'Happy birthday!', 'Make a wish!'], 0, '**This is for you!** = isto é para você!'),
              expq('O bolo está na mesa com as velas acesas.', ['Happy birthday!', 'Make a wish!', 'This is for you!'], 1, '**Make a wish!** = faça um pedido!')],
        missions=[mission('🎈', 'Festa no quintal', 'Pergunte o que os amigos têm.',
                          'Você faz uma festa no quintal. **Faça duas perguntas com Do you have…? e responda uma delas com Yes, I do ou No, I don’t.**',
                          ['Do you have'], "Do you have a gift? Do you have music? Yes, I do.",
                          ['Fiz uma pergunta com Do you have…?', 'Fiz duas perguntas?', 'Usei a resposta curta?'],
                          [r'\bdo you have\b[^.!?]*\?', r'(?:\bdo you have\b[^.!?]*\?[\s\S]*){2}', r"\b(?:yes,?\s*i do|no,?\s*i do(?:n['’]t| not))\b"],
                          [T(('Do you have a gift?', 'Você tem um presente?')), T(('Do you have music?', 'Você tem música?')), T(('Yes, I do.', 'Sim, eu tenho.'), ("No, I don't.", 'Não, eu não tenho.'))],
                          ['Pergunta certa! ❓', 'Duas perguntas! ✌️', 'Resposta curta! ✅'],
                          ['Yes, I do! Come to the party!', 'Sim, eu tenho! Venha à festa!']),
                  mission('🎂', 'Parabéns!', 'Use as expressões do episódio.',
                          'É aniversário da sua mãe. **Diga Happy birthday, entregue o presente (This is for you!) e peça para ela fazer um pedido (Make a wish!).**',
                          ['Happy birthday!'], 'Happy birthday, Mom! This is for you! Make a wish!',
                          ['Disse Happy birthday?', 'Entreguei o presente?', 'Pedi um desejo?'],
                          [r'\bhappy birthday\b', r'\bthis is for you\b', r'\bmake a wish\b'],
                          [T(('Happy birthday!', 'Feliz aniversário!')), T(('This is for you!', 'Isto é para você!')), T(('Make a wish!', 'Faça um pedido!'))],
                          ['Parabéns! 🎂', 'Presente! 🎁', 'Um desejo! 🕯️'],
                          ['Thank you! I love my gift!', 'Obrigada! Eu adoro o meu presente!'])])
    CX = [cx('The kids play in the ___ behind the house.', 'As crianças brincam no quintal atrás da casa.', 'yard', 'gift', 'music'),
          cx('Today I am ten years old. It is my ___.', 'Hoje eu faço dez anos. É o meu aniversário.', 'birthday', 'balloon', 'yard'),
          cx('I have a box with a bow. It is a ___ for you.', 'Eu tenho uma caixa com um laço. É um presente para você.', 'gift', 'party', 'yard'),
          cx('We have cake, friends and music. It is a ___.', 'Temos bolo, amigos e música. É uma festa.', 'party', 'gift', 'balloon'),
          cx('It is round, red and full of air. It floats! It is a ___.', 'É redondo, vermelho e cheio de ar. Flutua! É um balão.', 'balloon', 'music', 'birthday'),
          cx('The piano and the guitar make ___.', 'O piano e o violão fazem música.', 'music', 'yard', 'gift')]
    return dict(B=B, X=X, XT=XT, VB=VB, MR=MR, CX=CX)

EPS = [ep30(), ep31(), ep32(), ep33()]
