# Lote 04 do A1: posições 30 a 37.
# TROCAS DE OBRA: pos 30: de Peter Pan para The Waltons
# TROCAS DE OBRA: pos 31: de Over the River and Through the Wood para Home Alone
# TROCAS DE OBRA: pos 32: de Over the River and Through the Wood para Downton Abbey
# TROCAS DE OBRA: pos 33: de Little Women para The Sound of Music
# TROCAS DE OBRA: pos 34: de Little Women para Cheaper by the Dozen
# TROCAS DE OBRA: pos 35: mantém Anne of Green Gables
# TROCAS DE OBRA: pos 36: de Anne of Green Gables para Harry Potter and the Philosopher's Stone
# TROCAS DE OBRA: pos 37: de Mary Poppins para Charlie and the Chocolate Factory


# ------------------------------------------------------------------ atalhos
HPOS = [(14, 16), (40, 14), (66, 14), (88, 16), (12, 82)]


def hot(rows, pos=HPOS):
    return [dict(e=e, x=x, y=y, en=en, pt=pt, say=s, sayPt=sp) for (e, en, pt, s, sp), (x, y) in zip(rows, pos)]


def GAP(q, pt, opts, a, why):
    return dict(q=q, pt=pt, opts=opts, a=a, why=why)


def TRAP(opts, a, why, q='Qual frase está certa?'):
    return dict(q=q, opts=opts, a=a, why=why)


def QZ(q, pt, opts, a, line, why):
    return dict(q=q, pt=pt, opts=[list(o) for o in opts], a=a, line=line, why=why)


def EXP(ic, en, tag, pt, use, xe, xp):
    return dict(ic=ic, en=en, tag=tag, pt=pt, use=use, ex=[xe, xp])


def VBI(v, ic, pt, eu, ele, xe, xp, note):
    return dict(v=v, ic=ic, pt=pt, f=[['eu', eu], ['ele/ela', ele]], ex=[xe, xp], note=note)


def PG(label, slots, end='.'):
    return dict(label=label, slots=[dict(cat=c, opts=[list(o) for o in opts]) for c, opts in slots], end=[end, end])


def MIS(ic, name, desc, prompt, chips, model, check, kw, tips, ok, reply):
    return dict(ic=ic, name=name, desc=desc, data=dict(prompt=prompt, ph='Escreva a sua resposta aqui…', chips=chips, model=model, check=check,
                                                         kw=kw, tips=tips, ok=ok, reply=reply))


def HW(say, opts, a, why, ask='Ouça e toque na palavra.'):
    return dict(fig='🎧', say=say, ask=ask, opts=opts, a=a, why=why)


def HP(say, emojis, a, why, ask='Ouça e toque na figura.'):
    return dict(fig='🎧', say=say, ask=ask, opts=[[e, ''] for e in emojis], a=a, why=why, pic=1)


def RND(say, opts, a, why):
    return dict(fig='🎧', say=say, ask='Qual palavra você ouviu?', opts=opts, a=a, why=why)


def CXI(text, pt, right, w1, w2):
    return dict(text=text, pt=pt, opts=[right, w1, w2], a=0)


def RS(review, dquiz, rdg, pat, vplay, build, order, soundlab, produce, wrap, dictate):
    return dict(review=review, dquiz=dquiz, rdg=rdg, pat=pat, vplay=vplay, build=build, order=order, soundlab=soundlab, produce=produce,
                wrap=wrap, dictate=dictate)


def PROD(prompt, ph, chips, model, check, kw, tips, ok, reply):
    return dict(prompt=prompt, ph=ph, chips=chips, model=model, check=check, kw=kw, tips=tips, ok=ok, reply=reply)


def VOC(*rows):
    return [list(r) for r in rows]


def build(B, X, XT, VB, MR, CX):
    return dict(B=B, X=X, XT=XT, VB=VB, MR=MR, CX=CX)


# ------------------------------------------------------------------ pos 30 · The Waltons
def ep30():
    JB = 'p:short:6b4423:f4c7a1:2b6cb0:none:shirt'
    SAM = 'p:cap:2d2d2d:c68642:2f855a:none:shirt'
    GM = 'p:bun:cfcfcf:f4c7a1:b83280:glasses:dress'
    cast = {'John-Boy': ['👦', '#2b6cb0'], 'Sam': ['🧢', '#2f855a'], 'Grandma': ['👵', '#b83280']}
    lines = [
        ['John-Boy', 'Come in, Sam! This is my home.', 'Entre, Sam! Esta é a minha casa.'],
        ['Sam', 'Nice home! Is this your family?', 'Que casa legal! Esta é a sua família?'],
        ['John-Boy', 'Yes! These are my parents, John and Olivia.', 'Sim! Estes são os meus pais, John e Olivia.'],
        ['Sam', 'Your parents are nice! And who is he?', 'Seus pais são simpáticos! E quem é ele?'],
        ['John-Boy', 'This is my grandpa. He is funny!', 'Este é o meu vovô. Ele é engraçado!'],
        ['Grandma', "Hello, Sam! I'm the grandma.", 'Olá, Sam! Eu sou a vovó.'],
        ['John-Boy', 'These are my grandparents, Sam.', 'Estes são os meus avós, Sam.'],
        ['Sam', 'I love your family!', 'Eu adoro a sua família!'],
    ]
    B = dict(
        title='Plural: pai e mãe · These are…',
        sub='Apresentar mais de uma pessoa: This is my… vira These are my…',
        pattern_label='These are my…',
        why='Hoje você aprende a apresentar mais de uma pessoa, como o John-Boy: This is my… vira These are my… e a palavra vai para o plural.',
        vocab=VOC(['Parents', 'Pais (pai e mãe)', 'Soa como “PÉ-rents”.'], ['Grandma', 'Vovó', 'Soa como “GRÉN-ma”.'],
                  ['Grandpa', 'Vovô', 'Soa como “GRÉN-pa”.'], ['Family', 'Família', 'Soa como “FÉ-mi-li”.'],
                  ['Photo', 'Foto', 'Soa como “FÔU-tou”.'], ['Home', 'Casa (lar)', 'Soa como “RÔUM”, com um sopro no começo.'],
                  ['Grandparents', 'Avós (vovô e vovó)', 'Soa como “GRÉN-pé-rents”.']),
        balloons=[['👫', 'parents'], ['👵', 'grandma'], ['👴', 'grandpa'], ['👪', 'family'], ['📸', 'photo'], ['🏠', 'home']],
        cover_art=dict(s='farm', items=[['👴', 100, 56, 20, 'bob'], ['👵', 134, 50, 18, 'bob'], ['📸', 82, 34, 12, 'bob']], seed='wl1'),
        cover_sub='These are my… Em 10 minutos você apresenta a família como o John-Boy',
        cover_say='O John-Boy mostra uma foto da família para um amigo. Uma pessoa é This is my… e duas ou mais? Vamos descobrir!',
        wrap_recap=[['This is my grandma.', 'Esta é a minha vovó.'], ['These are my parents.', 'Estes são os meus pais.'],
                    ['These are my grandparents.', 'Estes são os meus avós.'], ['I love your family!', 'Eu adoro a sua família!']],
        teaser=dict(t='Home Alone', d='Próximo padrão: Meet my… para apresentar tios, primos e o bebê'),
        cast=cast, lines=lines,
        quiz=[QZ('Who is funny?', 'Quem é engraçado?', [('👵', 'The grandma'), ('🧢', 'Sam'), ('👴', 'The grandpa')], 2, 4,
                 'O John-Boy diz: “This is my grandpa. He is funny!”'),
              QZ('Who are John and Olivia?', 'Quem são John e Olivia?', [('👫', 'The parents'), ('🧑‍🏫', 'The teachers'), ('🧒', 'The cousins')], 0, 2,
                 'John-Boy diz: “These are my parents, John and Olivia.”'),
              QZ('What does Sam say at the end?', 'O que o Sam diz no final?', [('😴', "I'm tired!"), ('❤️', 'I love your family!'), ('🏃', "I'm late!")], 1, 7,
                 'Sam diz: “I love your family!”')],
        rdg_q=dict(q='O que muda de “This is my grandma” para falar de duas pessoas?',
                   o=['This is vira These are e a palavra vai para o plural', 'Só a palavra grandma muda', 'Nada muda'], a=0,
                   why='Duas ou mais pessoas: **These are** + my + plural. Exemplo: These are my parents.'),
        dictate=[['This is my home.', 'Esta é a minha casa.'], ['These are my parents.', 'Estes são os meus pais.'],
                 ['This is my grandpa.', 'Este é o meu vovô.'], ['Your parents are nice!', 'Seus pais são simpáticos!']],
        produce=PROD('O Sam pergunta: *Is this your family?* **Apresente uma pessoa com This is my… e duas pessoas com These are my…**',
                     'Ex.: This is my grandma. These are my parents.', ['This is my', 'These are my'],
                     'Yes! This is my grandma. These are my parents.',
                     ['Apresentei uma pessoa com This is my…?', 'Apresentei duas pessoas com These are my…?', 'Usei uma palavra de família?'],
                     [r'\bthis is my\s+\w+', r'\bthese are my\s+\w+', r'\b(?:parents|grandparents|grandma|grandpa|family|friends)\b'],
                     [[['This is my grandma.', 'Esta é a minha vovó.'], ['This is my friend.', 'Este é o meu amigo.']],
                      [['These are my parents.', 'Estes são os meus pais.'], ['These are my friends.', 'Estes são os meus amigos.']],
                      [['my parents', 'os meus pais'], ['my family', 'a minha família']]],
                     ['Uma pessoa certa! 🙋', 'Duas pessoas certas! 👫', 'Palavra de família! 👪'],
                     ['Nice family! Dinner is at six. Come in!', 'Que família legal! O jantar é às seis. Entre!']),
        rs=RS('living', 'garden', 'library', 'playground', 'bookshop', 'kitchen', 'bakery', 'musicroom', 'hotelroom', 'christmas', 'pool'),
        sc='farm',
    )
    X = dict(
        n=7009806, review=True, names=('John-Boy', 'Sam'),
        stage=dict(rs='farm', chars=[[JB, 26, 0, 1.0], [SAM, 56, 1, 1.0], [GM, 84, 1, 0.95]]),
        obra=dict(name='The Waltons', kind='📺 Série de TV · 1972', year='1972',
                  text='Série de TV americana que estreou em 1972. Ela mostra uma família grande que mora nas montanhas da Virgínia, nos anos 1930. Pais, avós e filhos vivem sob o mesmo teto, e cada episódio termina com os “boa-noite” da casa.',
                  line=['Good night, John-Boy.', 'Boa noite, John-Boy. (despedida famosa da série)'],
                  pa=dict(t='barn', e=['👪', '🏠', '📸'], p='d', v=0)),
        gancho=['John-Boy', 'Come in, Sam! This is my home.', 'Entre, Sam! Esta é a minha casa.'],
        hot=hot([('📸', 'photo', 'foto', 'This is a photo of my family.', 'Esta é uma foto da minha família.'),
                 ('🏠', 'home', 'casa (lar)', 'This is my home.', 'Esta é a minha casa.'),
                 ('👴', 'grandpa', 'vovô', 'This is my grandpa.', 'Este é o meu vovô.'),
                 ('👵', 'grandma', 'vovó', 'This is my grandma.', 'Esta é a minha vovó.'),
                 ('👫', 'parents', 'pais', 'These are my parents.', 'Estes são os meus pais.')]),
        gap=[GAP('___ is my grandma.', 'Esta é a minha vovó.', ['These', 'This', 'They'], 1, 'Uma pessoa só: **This is**.'),
             GAP('These ___ my parents.', 'Estes são os meus pais.', ['are', 'is', 'am'], 0, 'Com **these**, o verbo é **are**: These **are**.'),
             GAP('These are my ___.', 'Estes são os meus pais.', ['parent', 'parents', 'a parents'], 1, 'Depois de **these are**, a palavra vai para o plural: parents.'),
             GAP('___ are my grandparents.', 'Estes são os meus avós.', ['This', 'It', 'These'], 2, 'Duas pessoas: **These are**.')],
        trap=[TRAP(['These are my parent.', 'This are my parents.', 'These are my parents.'], 2, 'Plural: **these are** + palavra com -s: parents.'),
              TRAP(['This is my grandpas.', 'This is my grandpa.', 'These is my grandpa.'], 1, 'Uma pessoa: **This is my grandpa.** Sem -s.')],
        sticker=dict(title='A família do John-Boy', sub='The Waltons · 1972', rs='farm', chars=[[JB, 34, 0, 1.0], [GM, 68, 1, 1.0]]),
        speakers={'John-Boy': JB, 'Sam': SAM, 'Grandma': GM},
        rule=dict(who=GM, head='This is… → These are…', sub='Um → vários: como apresentar mais de uma pessoa.',
                  say=['These are my parents.', 'Estes são os meus pais.'], pairsHead='👀 Um → vários',
                  pairs=[dict(ico='🧑', a='<u>This is</u> my friend', b='<u>These are</u> my friend<u>s</u>', pta='este é o meu amigo', ptb='estes são os meus amigos', n=2),
                         dict(ico='📸', a='<u>This is</u> my photo', b='<u>These are</u> my photo<u>s</u>', pta='esta é a minha foto', ptb='estas são as minhas fotos', n=2),
                         dict(ico='🧑‍🏫', a='<u>This is</u> my teacher', b='<u>These are</u> my teacher<u>s</u>', pta='este é o meu professor', ptb='estes são os meus professores', n=2),
                         dict(ico='👧', a='<u>This is</u> my sister', b='<u>These are</u> my sister<u>s</u>', pta='esta é a minha irmã', ptb='estas são as minhas irmãs', n=2)],
                  uses=[dict(ico='🧓', tag='Uma pessoa', en='This is my grandpa.', pt='Este é o meu vovô.'),
                        dict(ico='👪', tag='Duas ou mais', en='These are my parents.', pt='Estes são os meus pais.')],
                  rules=[dict(tag='This is', c=0, text='**Uma** pessoa ou coisa: This is my grandma.', ex='This is + my + 1'),
                         dict(tag='These are', c=1, text='**Duas ou mais**: These are + my + palavra com -s.', ex='These are my parents.'),
                         dict(tag='my', c=2, text='**my** não muda no plural.', ex='my friend → my friends')],
                  tips=['Em português “este” vira “estes” e a palavra ganha -s. Em inglês também: this is → these are, friend → friends.',
                        '**parents** = pai e mãe. “Parentes” em inglês é outra palavra: relatives.']),
        mission_ic='👪',
    )
    XT = dict(
        exp=[EXP('🤝', "It's a pleasure to meet you.", 'Expressão', 'É um prazer te conhecer.', 'Jeito **educado** de dizer prazer, quando você conhece alguém.',
                 "It's a pleasure to meet you, ma'am.", 'É um prazer te conhecer, senhora.'),
             EXP('🏡', 'Make yourself at home!', 'Expressão', 'Fique à vontade!', 'Para o convidado se sentir **em casa**.',
                 'Come in! Make yourself at home!', 'Entre! Fique à vontade!'),
             EXP('🪑', 'Please, sit down.', 'Expressão', 'Por favor, sente-se.', 'Para **convidar** alguém a se sentar.',
                 'Please, sit down, Sam.', 'Por favor, sente-se, Sam.'),
             EXP('👂', "I've heard so much about you!", 'Expressão', 'Ouvi falar muito de você!', 'Quando você **já conhecia** a pessoa por histórias.',
                 "Hello! I've heard so much about you!", 'Olá! Ouvi falar muito de você!')],
        exp_scene=dict(rs='garden', lines=[
            ['Grandma', "Hello, Sam! **I've heard so much about you**!", 'Olá, Sam! Ouvi falar muito de você!'],
            ['Sam', "**It's a pleasure to meet you**!", 'É um prazer te conhecer!'],
            ['Grandma', '**Make yourself at home**. **Please, sit down**.', 'Fique à vontade. Por favor, sente-se.'],
            ['Sam', 'Thank you! This is a nice home.', 'Obrigado! Esta é uma casa legal.'],
            ['John-Boy', 'And these are my parents.', 'E estes são os meus pais.'],
            ['Sam', "Hello, John and Olivia. **It's a pleasure to meet you**!", 'Olá, John e Olivia. É um prazer conhecer vocês!']]),
        lab=dict(short='th sonoro', title='Laboratório de sons: o “th” de these', say='Em these, this e they existe um som que o português não tem. Vamos treinar com o John-Boy!',
                 intro=dict(what='O **th** sonoro de **these**, **this** e **they**: a língua fica entre os dentes e a voz “vibra”.',
                            how='Coloque a ponta da língua entre os dentes da frente e ligue a voz, como um “z” mole. A língua não fica atrás dos dentes.',
                            pt='Muitos brasileiros trocam por “d” ou “z”: “dis” ou “zis”. Em inglês a língua aparece um pouquinho entre os dentes.'),
                 ex=[['these', 'DHIZ', 'estes', 'língua entre os dentes, voz ligada'], ['this', 'DHIS', 'este', 'não diga “dis”'],
                     ['they', 'DHÊI', 'eles', 'sinta a vibração na língua']],
                 pairs=[['they', 'day', 'th: língua entre os dentes · d: língua atrás dos dentes'], ['then', 'den', '“então” × “toca”'],
                        ['those', 'doze', '“aqueles” × “cochilar”']],
                 tip='Ponha a língua entre os dentes e diga “zzz”: você sente a vibração. Esse é o th sonoro.',
                 phrase=['These are my parents.', 'Estes são os meus pais.'],
                 rounds=[RND('day', ['they', 'day'], 1, 'Em **day** a língua toca atrás dos dentes (d). Em **they** ela aparece entre os dentes.'),
                         RND('then', ['then', 'den'], 0, '**Then** (então) tem a língua entre os dentes. **Den** (toca) começa com “d”.'),
                         RND('those', ['doze', 'those'], 1, '**Those** (aqueles) começa com o th sonoro. **Doze** começa com “d”.')]),
        hunt=[HW('day', ['they', 'day'], 1, '**day** (dia) começa com “d”: a língua fica atrás dos dentes.'),
              HP('grandpa', ['👵', '👴', '📸'], 1, '**grandpa** = vovô.'),
              HW('those', ['those', 'doze'], 0, '**those** começa com o th sonoro, língua entre os dentes.'),
              HP('photo', ['📸', '🏠', '👪'], 0, '**photo** = foto.'),
              HW('then', ['then', 'den'], 0, '**then** tem o th sonoro: língua entre os dentes.')],
    )
    VB = dict(title='Verbos para apresentar a família', tip='Quatro verbos: introduce, know, look e talk.', items=[
        VBI('introduce', '🤝', 'apresentar', 'I introduce my parents.', 'John-Boy introduce**s** Sam.', 'I introduce my parents.', 'Eu apresento os meus pais.',
            '**introduce** = apresentar. Com he/she: **introduces**.'),
        VBI('know', '💡', 'conhecer, saber', 'I know your grandma.', 'Sam know**s** the family.', 'I know your grandma.', 'Eu conheço a sua vovó.',
            '**know** = conhecer, saber. Com he/she: **knows**.'),
        VBI('look', '👀', 'olhar', 'I look at the photo.', 'Grandma look**s** at the photo.', 'I look at the photo.', 'Eu olho a foto.',
            '**look** = olhar. Com he/she: **looks**.'),
        VBI('talk', '💬', 'conversar', 'I talk to my grandpa.', 'Sam talk**s** to my grandma.', 'I talk to my grandpa.', 'Eu converso com o meu vovô.',
            '**talk** = conversar. Com he/she: **talks**.')])
    MR = dict(
        mold=[PG('Apresentar uma pessoa', [('apresentar', [('This is my', 'este(a) é o(a) meu(minha)')]),
                                           ('quem', [('grandma', 'vovó'), ('grandpa', 'vovô'), ('friend', 'amigo(a)'), ('teacher', 'professor(a)'), ('sister', 'irmã')])]),
              PG('Apresentar duas ou mais', [('apresentar', [('These are my', 'estes(as) são os(as) meus(minhas)')]),
                                             ('quem', [('parents', 'pais'), ('grandparents', 'avós'), ('friends', 'amigos'), ('teachers', 'professores'), ('sisters', 'irmãs')])]),
              PG('Olhar a foto', [('olhar', [('Look at', 'olhe')]),
                                  ('o quê', [('this photo', 'esta foto'), ('my family', 'a minha família'), ('my home', 'a minha casa'), ('these photos', 'estas fotos')])], '!')],
        speak=[['These are my grandparents.', 'Estes são os meus avós.'], ['I love your family!', 'Eu adoro a sua família!']],
        trap=[dict(ask='“Make yourself at home” quer dizer…', opts=['Vá para casa!', 'Fique à vontade!', 'Construa uma casa!'], a=1,
                   why='**Make yourself at home** = fique à vontade.', say='Make yourself at home.'),
              dict(ask='Qual frase está certa?', opts=["I've heard much of you!", 'I heard so much of you!', "I've heard so much about you!"], a=2,
                   why="A expressão certa é **I've heard so much about you!**", say="I've heard so much about you!")],
        gap=[dict(text="It's a pleasure to ___ you.", pt='É um prazer te conhecer.', opts=['make', 'meet', 'do'], a=1, why='**meet** = conhecer: pleasure to **meet** you.',
                  say="It's a pleasure to meet you."),
             dict(text='Please, ___ down.', pt='Por favor, sente-se.', opts=['sit', 'sits', 'seat'], a=0, why='Pedido educado: Please, **sit** down.', say='Please, sit down.')],
        expq=[dict(ask='Seu amigo chegou à sua casa. Você quer que ele relaxe.', opts=["It's a pleasure to meet you.", 'Make yourself at home.', "I've heard so much about you!"], a=1,
                   why='**Make yourself at home.** = fique à vontade.'),
              dict(ask='Você conhece o pai de uma amiga e quer ser educado.', opts=["It's a pleasure to meet you.", 'Please, sit down.', 'Make yourself at home.'], a=0,
                   why='**It\'s a pleasure to meet you.** = é um prazer te conhecer.'),
              dict(ask='A avó do seu amigo já ouviu histórias sobre você. O que ela diz?', opts=['Please, sit down.', "It's a pleasure to meet you.", "I've heard so much about you!"], a=2,
                   why="**I've heard so much about you!** = ouvi falar muito de você!")],
        missions=[MIS('👪', 'Foto de família', 'Apresente a sua família.',
                      'Você mostra uma foto da família a um amigo. **Apresente uma pessoa com This is my… e duas pessoas com These are my…**',
                      ['This is my', 'These are my'], 'This is my grandma. These are my parents.',
                      ['Usei This is my…?', 'Usei These are my…?', 'Falei de pessoas da família?'],
                      [r'\bthis is my\s+\w+', r'\bthese are my\s+\w+', r'\b(?:mom|dad|mother|father|grandma|grandpa|parents|grandparents|friends|sister|brother)\b'],
                      [[['This is my grandma.', 'Esta é a minha vovó.']], [['These are my parents.', 'Estes são os meus pais.']], [['my sister', 'a minha irmã'], ['my grandparents', 'os meus avós']]],
                      ['Uma pessoa certa! 🙋', 'Duas pessoas certas! 👫', 'Família na foto! 📸'],
                      ['Nice photo! Your family is great!', 'Que foto legal! A sua família é ótima!']),
              MIS('🤝', 'Receber uma visita', 'Use as expressões do episódio.',
                  'Um amigo chega à sua casa. **Diga que é um prazer conhecê-lo, peça para ele se sentar e diga para ele ficar à vontade.**',
                  ["It's a pleasure"], "It's a pleasure to meet you. Please, sit down. Make yourself at home.",
                  ['Disse que é um prazer?', 'Pedi para sentar?', 'Pedi para ficar à vontade?'],
                  [r'\bpleasure to meet you\b', r'\bsit down\b', r'\bmake yourself at home\b'],
                  [[["It's a pleasure to meet you.", 'É um prazer te conhecer.']], [['Please, sit down.', 'Por favor, sente-se.']], [['Make yourself at home.', 'Fique à vontade.']]],
                  ['Educado! 🤝', 'Cadeira oferecida! 🪑', 'Visita à vontade! 🏡'],
                  ['Thank you! This is a nice home.', 'Obrigado! Esta é uma casa legal.'])])
    CX = [CXI('My mom and my dad are my ___.', 'Minha mãe e meu pai são os meus pais.', 'parents', 'photo', 'home'),
          CXI('She is old and she makes cookies for me. She is my ___.', 'Ela é idosa e faz biscoitos para mim. Ela é a minha vovó.', 'grandma', 'grandpa', 'photo'),
          CXI('He is my dad\'s father. He is old and funny. He is my ___.', 'Ele é o pai do meu pai. Ele é idoso e engraçado. Ele é o meu vovô.', 'grandpa', 'grandma', 'family'),
          CXI('Mom, dad, my sister and me: we are a ___.', 'Mãe, pai, minha irmã e eu: somos uma família.', 'family', 'home', 'photo'),
          CXI('Smile! I take a ___ of the family.', 'Sorriam! Eu tiro uma foto da família.', 'photo', 'home', 'parents'),
          CXI("I'm tired. Let's go ___.", 'Estou cansado. Vamos para casa.', 'home', 'photo', 'grandpa')]
    return build(B, X, XT, VB, MR, CX)



# ------------------------------------------------------------------ pos 31 · Home Alone
def ep31():
    KEV = 'p:short:d69e2e:f4c7a1:c0392b:none:shirt'
    MIA = 'p:long:2d2d2d:e8b48a:6b46c1:bow:dress'
    LES = 'p:curly:8d4a1f:f4c7a1:2f855a:scarf:dress'
    cast = {'Kevin': ['👦', '#c0392b'], 'Mia': ['👧', '#6b46c1'], 'Leslie': ['👩', '#2f855a']}
    lines = [
        ['Kevin', 'Mia, meet my aunt. This is Aunt Leslie.', 'Mia, esta é a minha tia. Esta é a tia Leslie.'],
        ['Mia', 'Nice to meet you, Leslie!', 'Prazer em conhecer você, Leslie!'],
        ['Leslie', 'Nice to meet you, too! Are you from school?', 'Prazer também! Você é da escola?'],
        ['Mia', 'Yes, I am. Kevin is my friend.', 'Sim, sou. O Kevin é meu amigo.'],
        ['Kevin', "Now meet my uncle. He's in the kitchen.", 'Agora conheça o meu tio. Ele está na cozinha.'],
        ['Mia', 'Wow, a big family!', 'Uau, que família grande!'],
        ['Leslie', "And meet the baby cousin! She's Ella.", 'E conheça a prima bebê! Ela é a Ella.'],
        ['Mia', "Nice to meet you, Ella! She's so cute!", 'Prazer, Ella! Ela é muito fofa!'],
    ]
    B = dict(
        title='Meet My Grandma · Meet my…',
        sub='Apresentar tios, primos e o bebê com Meet my…',
        pattern_label='Meet my…',
        why='Hoje você aprende a apresentar parentes como o Kevin: Meet my… (conheça o meu…), Nice to meet you e He’s / She’s para dizer quem é.',
        vocab=VOC(['Aunt', 'Tia', 'Soa como “ÉNT”.'], ['Uncle', 'Tio', 'Soa como “ÂN-kol”.'], ['Cousin', 'Primo(a)', 'Soa como “KÂ-zin”.'],
                  ['Baby', 'Bebê', 'Soa como “BÊI-bi”.'], ['House', 'Casa', 'Soa como “RÁUS”, com sopro no começo.'],
                  ['Bedroom', 'Quarto', 'Soa como “BÉD-rum”.'], ['Meet', 'Conhecer, apresentar', 'Soa como “MIT”.']),
        balloons=[['👩', 'aunt'], ['👨', 'uncle'], ['🧒', 'cousin'], ['👶', 'baby'], ['🏠', 'house'], ['🛏️', 'bedroom'], ['🤝', 'meet']],
        cover_art=dict(s='christmas', items=[['👩', 104, 56, 18, 'bob'], ['👶', 136, 52, 14, 'bob'], ['🎄', 84, 36, 14, 'bob']], seed='ha1'),
        cover_sub='Meet my… Em 10 minutos você apresenta a família numa festa de Natal',
        cover_say='O Kevin recebe a amiga Mia na festa de Natal da família. Tem tia, tio e até um bebê! Como apresentar todo mundo?',
        wrap_recap=[['Meet my aunt.', 'Conheça a minha tia.'], ['Nice to meet you, too!', 'Prazer em conhecer você também!'],
                    ["He's my uncle.", 'Ele é o meu tio.'], ["She's my cousin.", 'Ela é a minha prima.']],
        teaser=dict(t='Downton Abbey', d='Próximo padrão: This is my… e This is your… para mostrar uma casa'),
        cast=cast, lines=lines,
        quiz=[QZ('Who is Leslie?', 'Quem é a Leslie?', [('👩', 'An aunt'), ('🧒', 'A cousin'), ('🧑‍🏫', 'A teacher')], 0, 0,
                 'O Kevin diz: “Meet my aunt. This is Aunt Leslie.”'),
              QZ('Where is the uncle?', 'Onde está o tio?', [('🛏️', 'In the bedroom'), ('🍳', 'In the kitchen'), ('🚗', 'In the car')], 1, 4,
                 'Kevin diz: “He’s in the kitchen.”'),
              QZ('Who is Ella?', 'Quem é a Ella?', [('👨', 'The uncle'), ('👩', 'The aunt'), ('👶', 'The baby')], 2, 6,
                 'A Leslie diz: “Meet the baby cousin! She’s Ella.”')],
        rdg_q=dict(q='Alguém diz “Nice to meet you!”. O que você responde?',
                   o=['Nice to meet you, too!', 'Yes, I am.', 'Nice to meet you, no!'], a=0,
                   why='Resposta natural: **Nice to meet you, too!** (prazer também!).'),
        dictate=[['Meet my aunt.', 'Conheça a minha tia.'], ['Nice to meet you, too!', 'Prazer em conhecer você também!'],
                 ['Meet my uncle.', 'Conheça o meu tio.'], ["She's my cousin.", 'Ela é a minha prima.']],
        produce=PROD('Um amigo chega à sua festa de Natal. **Apresente um parente com Meet my… e diga Nice to meet you.**',
                     "Ex.: Meet my aunt. She's from Texas. Nice to meet you!", ['Meet my', 'Nice to meet you'],
                     "Meet my aunt. She's from Texas. Nice to meet you!",
                     ['Usei Meet my…?', 'Disse Nice to meet you?', 'Usei He’s ou She’s?'],
                     [r'\bmeet my\s+\w+', r'\bnice to meet you\b', r'\b(?:he|she)(?:[\'’]s| is)\s+\w+'],
                     [[['Meet my uncle.', 'Conheça o meu tio.'], ['Meet my cousin.', 'Conheça o meu primo.']],
                      [['Nice to meet you!', 'Prazer em conhecer você!'], ['Nice to meet you, too!', 'Prazer também!']],
                      [["He's my uncle.", 'Ele é o meu tio.'], ["She's my aunt.", 'Ela é a minha tia.']]],
                     ['Apresentação feita! 🤝', 'Educado! 😊', 'Ele ou ela, certo! 👍'],
                     ['Nice to meet you, too! You have a nice family!', 'Prazer também! Você tem uma família legal!']),
        rs=RS('living', 'bakery', 'snow', 'library', 'museum', 'zoo', 'garden', 'stage', 'restaurant', 'bedroom', 'playground'),
        sc='christmas',
    )
    X = dict(
        n=70011, review=True, names=('Kevin', 'Mia'),
        stage=dict(rs='christmas', chars=[[KEV, 26, 0, 1.0], [MIA, 54, 1, 1.0], [LES, 82, 1, 1.0]]),
        obra=dict(name='Home Alone', kind='🎬 Filme · 1990', year='1990',
                  text='Comédia americana de 1990, com Macaulay Culkin no papel de Kevin. No Natal, uma família grande, cheia de tios e primos, viaja para Paris e deixa o menino sozinho em casa, nos Estados Unidos.',
                  line=['Merry Christmas!', 'Feliz Natal! (tema do filme)'],
                  pa=dict(t='snowvillage', e=['🎄', '🏠', '👶'], p='e', v=1)),
        gancho=['Kevin', 'Mia, meet my aunt. This is Aunt Leslie.', 'Mia, esta é a minha tia. Esta é a tia Leslie.'],
        hot=hot([('👩', 'aunt', 'tia', 'Meet my aunt.', 'Conheça a minha tia.'),
                 ('👨', 'uncle', 'tio', 'Meet my uncle.', 'Conheça o meu tio.'),
                 ('🧒', 'cousin', 'primo(a)', 'Meet my cousin.', 'Conheça o meu primo.'),
                 ('👶', 'baby', 'bebê', 'Meet the baby!', 'Conheça o bebê!'),
                 ('🏠', 'house', 'casa', 'Nice to meet you in my house!', 'Prazer em conhecer você na minha casa!')]),
        gap=[GAP('___ my aunt.', 'Conheça a minha tia.', ['Meet', 'Meets', 'Meeting'], 0, 'Para apresentar alguém: **Meet** my…'),
             GAP('Nice to ___ you.', 'Prazer em conhecer você.', ['meets', 'meet', 'met'], 1, 'Depois de **to**, o verbo fica simples: to **meet**.'),
             GAP('This is my uncle. ___ in the kitchen.', 'Ele está na cozinha.', ['It’s', 'She’s', 'He’s'], 2, 'Tio é homem: **He’s**.'),
             GAP('Nice to meet you, ___!', 'Prazer em conhecer você também!', ['to', 'too', 'two'], 1, 'Na resposta, **too** quer dizer “também”.')],
        trap=[TRAP(['Meet to my aunt.', 'Meet my aunt.', 'Meeting my aunt.'], 1, 'Para apresentar alguém: **Meet** my aunt. Sem “to”.'),
              TRAP(['He’s my uncle.', 'She’s my uncle.', 'It’s my uncle.'], 0, 'Tio é homem, então **He’s**.')],
        sticker=dict(title='Kevin e a tia Leslie', sub='Home Alone · 1990', rs='christmas', chars=[[KEV, 34, 0, 1.0], [LES, 68, 1, 1.0]]),
        speakers={'Kevin': KEV, 'Mia': MIA, 'Leslie': LES},
        rule=dict(who=LES, head='Meet my…', sub='Para apresentar parentes e amigos.',
                  say=['Meet my aunt.', 'Conheça a minha tia.'],
                  formula=[dict(from_=[['This is', 0], ['my', 1], ['aunt.', 2]], to=[['Meet', 0], ['my', 1], ['aunt.', 2]], say='Meet my aunt.',
                                note='Ao apresentar alguém a outra pessoa, troque **This is** por **Meet**: Meet my aunt.'),
                           dict(from_=[['Nice to meet you.', 0]], to=[['Nice to meet you,', 0], ['too!', 3]], say='Nice to meet you, too!',
                                note='Ao responder, junte **too** (também): Nice to meet you, **too**!')],
                  uses=[dict(ico='🤝', tag='Apresentar', en='Meet my uncle.', pt='Conheça o meu tio.'),
                        dict(ico='😊', tag='Responder', en='Nice to meet you, too!', pt='Prazer em conhecer você também!'),
                        dict(ico='👉', tag='Dizer quem é', en="She's my cousin.", pt='Ela é a minha prima.')],
                  rules=[dict(tag='Meet my', c=0, text='**Conheça o meu / a minha…** Serve para parentes e amigos.', ex='Meet my aunt.'),
                         dict(tag='Nice to meet you', c=1, text='Prazer em conhecer você. Responda com **too**.', ex='Nice to meet you, too!'),
                         dict(tag='He’s / She’s', c=2, text='Depois da apresentação, diga **quem é**: ele (He’s) ou ela (She’s).', ex="He's my uncle. She's my aunt.")],
                  tips=['Em português dizemos “esta é a minha tia”. Em inglês, ao apresentar alguém a outra pessoa, é comum dizer **Meet my aunt**.',
                        '**cousin** serve para primo e prima. O contexto mostra se é menino ou menina.']),
        mission_ic='🤝',
    )
    XT = dict(
        exp=[EXP('🎉', 'Welcome to the family!', 'Expressão', 'Bem-vindo à família!', 'Para dar boas-vindas a alguém que **entra** na família.',
                 'Welcome to the family, Mia!', 'Bem-vinda à família, Mia!'),
             EXP('❤️', 'Family comes first.', 'Expressão', 'A família vem primeiro.', 'Quando a família é **mais importante** que o resto.',
                 'Family comes first. Always.', 'A família vem primeiro. Sempre.'),
             EXP('🚗', 'Here we are!', 'Expressão', 'Chegamos!', 'Quando o grupo **chega** ao lugar.',
                 'Here we are! This is the house!', 'Chegamos! Esta é a casa!'),
             EXP('👋', 'Long time no see!', 'Informal', 'Quanto tempo!', 'Ao ver alguém que você **não vê há muito tempo**.',
                 'Long time no see, Uncle Frank!', 'Quanto tempo, tio Frank!')],
        exp_scene=dict(rs='chefkitchen', lines=[
            ['Leslie', '**Here we are**! Hello, Kevin!', 'Chegamos! Olá, Kevin!'],
            ['Kevin', '**Long time no see**, Aunt Leslie!', 'Quanto tempo, tia Leslie!'],
            ['Leslie', 'And you are Mia? **Welcome to the family**!', 'E você é a Mia? Bem-vinda à família!'],
            ['Mia', 'Thank you! Nice to meet you.', 'Obrigada! Prazer em conhecer você.'],
            ['Kevin', '**Family comes first**, Mia. Come in!', 'A família vem primeiro, Mia. Entre!'],
            ['Mia', 'Wow, a nice house!', 'Uau, que casa legal!']]),
        lab=dict(short='u de uncle', title='Laboratório de sons: o “u” de uncle', say='A palavra uncle tem um som curtinho que confunde muita gente. Vamos treinar com o Kevin!',
                 intro=dict(what='O **u** curto de **uncle**, **cousin** e **come**: é um “â” relaxado, bem curto e baixo.',
                            how='Deixe a boca meio aberta e relaxada, a língua parada no meio, sem arredondar os lábios. O som é curto.',
                            pt='Muitos brasileiros dizem “ôn-cle” ou “kô-zin”. O certo fica entre “a” e “â”. Cuidado para não trocar pelo **a** de cat: cut ≠ cat.'),
                 ex=[['uncle', 'ÂN-kol', 'tio', 'boca relaxada, som curto'], ['cousin', 'KÂ-zin', 'primo(a)', 'não diga “kô-zin”'],
                     ['come', 'KÂM', 'vir', 'curto, sem arredondar os lábios']],
                 pairs=[['cut', 'cat', 'u: boca relaxada · a: boca bem aberta'], ['cup', 'cap', '“copo” × “boné”'], ['but', 'bat', '“mas” × “morcego”']],
                 tip='Diga “âh…” curtinho, como quando você pensa. Esse é o som de uncle, cousin e come.',
                 phrase=['Meet my uncle and my cousin.', 'Conheça o meu tio e o meu primo.'],
                 rounds=[RND('cat', ['cut', 'cat'], 1, '**Cat** (gato) tem a boca bem aberta. **Cut** (cortar) tem o “â” relaxado.'),
                         RND('cup', ['cup', 'cap'], 0, '**Cup** (copo) tem o “â” curto. **Cap** (boné) tem o “é” aberto.'),
                         RND('bat', ['but', 'bat'], 1, '**Bat** (morcego) tem o “é” aberto. **But** (mas) tem o “â” curto.')]),
        hunt=[HW('cut', ['cut', 'cat'], 0, '**cut** (cortar) tem o “â” curto, boca relaxada.'),
              HP('cap', ['☕', '🧢', '👶'], 1, '**cap** = boné.'),
              HW('cup', ['cup', 'cap'], 0, '**cup** (copo) tem o “â” curto.'),
              HP('baby', ['🧢', '👶', '☕'], 1, '**baby** = bebê.'),
              HW('bat', ['but', 'bat'], 1, '**bat** (morcego) tem o “é” aberto.')],
    )
    VB = dict(title='Verbos para apresentar parentes', tip='Quatro verbos: meet, come, laugh e hug.', items=[
        VBI('meet', '🤝', 'conhecer', 'I meet my aunt.', 'Mia meet**s** the baby.', 'I meet my aunt.', 'Eu conheço a minha tia.',
            '**meet** = conhecer. Com he/she: **meets**.'),
        VBI('come', '🚪', 'vir', 'I come to the house.', 'Uncle Frank come**s** to the house.', 'I come to the house.', 'Eu venho à casa.',
            '**come** = vir. Com he/she: **comes**.'),
        VBI('laugh', '😂', 'rir', 'I laugh with my cousin.', 'The baby laugh**s**.', 'I laugh with my cousin.', 'Eu rio com o meu primo.',
            '**laugh** = rir. Com he/she: **laughs**.'),
        VBI('hug', '🤗', 'abraçar', 'I hug my aunt.', 'Kevin hug**s** the baby.', 'I hug my aunt.', 'Eu abraço a minha tia.',
            '**hug** = abraçar. Com he/she: **hugs**.')])
    MR = dict(
        mold=[PG('Apresentar um parente', [('apresentar', [('Meet my', 'conheça o(a) meu(minha)')]),
                                           ('quem', [('aunt', 'tia'), ('uncle', 'tio'), ('cousin', 'primo(a)'), ('baby', 'bebê'), ('friend', 'amigo(a)')])]),
              PG('Dizer onde está', [('quem', [("He's", 'ele está'), ("She's", 'ela está')]),
                                     ('onde', [('in the house', 'na casa'), ('in the kitchen', 'na cozinha'), ('in the bedroom', 'no quarto'), ('at home', 'em casa')])]),
              PG('Responder ao prazer', [('começo', [('Nice to meet you,', 'prazer em conhecer você,')]),
                                         ('fim', [('too', 'também'), ('Leslie', 'Leslie'), ('Mia', 'Mia')])], '!')],
        speak=[['Meet the baby! She is so cute!', 'Conheça o bebê! Ela é muito fofa!'], ['Nice to meet you, Ella!', 'Prazer em conhecer você, Ella!']],
        trap=[dict(ask='“Long time no see!” quer dizer…', opts=['Até logo!', 'Não vejo nada!', 'Quanto tempo!'], a=2,
                   why='**Long time no see!** = quanto tempo (sem ver você).', say='Long time no see!'),
              dict(ask='Qual frase está certa?', opts=['Family come first.', 'Family comes first.', 'Families comes first.'], a=1,
                   why='**Family** é uma palavra só, então **comes**.', say='Family comes first.')],
        gap=[dict(text='___ we are!', pt='Chegamos!', opts=['Here', 'Hear', 'Where'], a=0, why='**Here we are!** = chegamos!', say='Here we are!'),
             dict(text='Welcome ___ the family!', pt='Bem-vindo à família!', opts=['at', 'to', 'on'], a=1, why='Boas-vindas: Welcome **to** the family!',
                  say='Welcome to the family!')],
        expq=[dict(ask='Você chega com o grupo à casa da sua tia.', opts=['Here we are!', 'Welcome to the family!', 'Long time no see!'], a=0,
                   why='**Here we are!** = chegamos!'),
              dict(ask='Você encontra um primo que não vê há muito tempo.', opts=['Family comes first.', 'Long time no see!', 'Here we are!'], a=1,
                   why='**Long time no see!** = quanto tempo!'),
              dict(ask='Uma pessoa nova entra na sua família.', opts=['Here we are!', 'Long time no see!', 'Welcome to the family!'], a=2,
                   why='**Welcome to the family!** = bem-vindo à família!')],
        missions=[MIS('🎄', 'Festa de Natal', 'Apresente dois parentes.',
                      'Seu amigo chega à festa de Natal. **Apresente dois parentes com Meet my… e diga onde um deles está com He’s ou She’s.**',
                      ['Meet my'], "Meet my aunt. She's in the kitchen. Meet my uncle.",
                      ['Usei Meet my…?', 'Apresentei duas pessoas?', 'Usei He’s ou She’s?'],
                      [r'\bmeet my\s+(?:aunt|uncle|cousin|baby|grandma|grandpa|mom|dad|sister|brother)\b', r'(?:\bmeet my\b[\s\S]*){2}', r'\b(?:he|she)(?:[\'’]s| is)\b'],
                      [[['Meet my aunt.', 'Conheça a minha tia.']], [['Meet my uncle.', 'Conheça o meu tio.']], [["She's in the kitchen.", 'Ela está na cozinha.']]],
                      ['Boa apresentação! 🤝', 'Duas pessoas! ✌️', 'Ele ou ela, certo! 👍'],
                      ['Nice to meet you both! What a big family!', 'Prazer em conhecer vocês! Que família grande!']),
              MIS('🚗', 'Chegada em casa', 'Use as expressões do episódio.',
                  'Você chega à casa de uma prima. **Diga Here we are!, diga Long time no see! e dê as boas-vindas com Welcome to the family!**',
                  ['Here we are'], 'Here we are! Long time no see! Welcome to the family!',
                  ['Disse Here we are?', 'Disse Long time no see?', 'Dei as boas-vindas?'],
                  [r'\bhere we are\b', r'\blong time no see\b', r'\bwelcome to the family\b'],
                  [[['Here we are!', 'Chegamos!']], [['Long time no see!', 'Quanto tempo!']], [['Welcome to the family!', 'Bem-vindo à família!']]],
                  ['Chegamos! 🚗', 'Quanto tempo! 👋', 'Boas-vindas! 🎉'],
                  ['Thank you! Come in, come in!', 'Obrigada! Entre, entre!'])])
    CX = [CXI('My mom\'s sister is my ___.', 'A irmã da minha mãe é a minha tia.', 'aunt', 'cousin', 'baby'),
          CXI('My dad\'s brother is my ___.', 'O irmão do meu pai é o meu tio.', 'uncle', 'cousin', 'house'),
          CXI('My aunt\'s son is my ___.', 'O filho da minha tia é o meu primo.', 'cousin', 'uncle', 'baby'),
          CXI('She is one year old. She cries and sleeps a lot. She is a ___.', 'Ela tem um ano. Chora e dorme muito. Ela é um bebê.', 'baby', 'aunt', 'bedroom'),
          CXI('We live in a big ___ with a garden.', 'Moramos numa casa grande com jardim.', 'house', 'bedroom', 'uncle'),
          CXI('I sleep in my ___. My bed is there.', 'Eu durmo no meu quarto. A minha cama fica lá.', 'bedroom', 'house', 'cousin')]
    return build(B, X, XT, VB, MR, CX)


# ------------------------------------------------------------------ pos 32 · Downton Abbey
def ep32():
    CAR = 'p:bald:cfcfcf:f4c7a1:1a202c:none:suit'
    ANN = 'p:bun:5c3a21:f4c7a1:2f855a:none:dress'
    DAI = 'p:long:8d4a1f:f4c7a1:c0392b:bow:dress'
    cast = {'Carson': ['🎩', '#1a365d'], 'Anna': ['👩', '#2f855a'], 'Daisy': ['👧', '#c0392b']}
    lines = [
        ['Carson', 'Welcome, Daisy. This is the hall.', 'Bem-vinda, Daisy. Este é o saguão.'],
        ['Daisy', "Wow! It's a big house.", 'Uau! É uma casa grande.'],
        ['Carson', 'This is my office. And this is your kitchen.', 'Este é o meu escritório. E esta é a sua cozinha.'],
        ['Anna', 'Daisy, come with me. This is your room.', 'Daisy, venha comigo. Este é o seu quarto.'],
        ['Daisy', 'Is this my bed?', 'Esta é a minha cama?'],
        ['Anna', 'Yes, this is your bed. And this is your key.', 'Sim, esta é a sua cama. E esta é a sua chave.'],
        ['Daisy', 'And this is my window! I love it.', 'E esta é a minha janela! Eu adoro.'],
        ['Anna', 'Good. Dinner is at six, Daisy.', 'Ótimo. O jantar é às seis, Daisy.'],
    ]
    B = dict(
        title='This is / This is my · This is your…',
        sub='Mostrar uma casa com This is my… e This is your…',
        pattern_label='This is my / your…',
        why='Hoje você aprende a mostrar uma casa como o Mr. Carson: This is my… (meu) e This is your… (seu), e a perguntar Is this my…?',
        vocab=VOC(['Room', 'Quarto, sala', 'Soa como “RUM”.'], ['Bed', 'Cama', 'Soa como “BÉD”.'], ['Door', 'Porta', 'Soa como “DÓR”.'],
                  ['Window', 'Janela', 'Soa como “UÍN-dou”.'], ['Stairs', 'Escada', 'Soa como “STÉRZ”.'], ['Key', 'Chave', 'Soa como “KI”.']),
        balloons=[['🛏️', 'bed'], ['🚪', 'door'], ['🪟', 'window'], ['🔑', 'key'], ['🪜', 'stairs'], ['🏠', 'room']],
        cover_art=dict(s='castlehall', items=[['🔑', 104, 54, 16, 'bob'], ['🚪', 136, 50, 18, 'bob'], ['🪟', 84, 34, 12, 'bob']], seed='dw1'),
        cover_sub='This is my… / This is your… Em 10 minutos você mostra uma casa inteira',
        cover_say='Hoje é o primeiro dia da Daisy numa casa enorme. O Mr. Carson mostra tudo: o que é dele e o que é dela. Como falar?',
        wrap_recap=[['This is my office.', 'Este é o meu escritório.'], ['This is your room.', 'Este é o seu quarto.'],
                    ['Is this my bed?', 'Esta é a minha cama?'], ['Dinner is at six.', 'O jantar é às seis.']],
        teaser=dict(t='The Sound of Music', d='Próximo padrão: I have… para falar de quem você tem na família'),
        cast=cast, lines=lines,
        quiz=[QZ('Who is new in the house?', 'Quem é novo na casa?', [('🎩', 'Carson'), ('👩', 'Anna'), ('👧', 'Daisy')], 2, 0,
                 'Carson diz: “Welcome, Daisy.” Ela é a nova da casa.'),
              QZ('What does Daisy love?', 'O que a Daisy adora?', [('🪜', 'The stairs'), ('🪟', 'The window'), ('🚪', 'The door')], 1, 6,
                 'Daisy diz: “And this is my window! I love it.”'),
              QZ('What time is dinner?', 'A que horas é o jantar?', [('6️⃣', 'At six'), ('9️⃣', 'At nine'), ('2️⃣', 'At two')], 0, 7,
                 'Anna diz: “Dinner is at six.”')],
        rdg_q=dict(q='Qual palavra a Anna usa para falar da cama da Daisy?', o=['my bed', 'you bed', 'your bed'], a=2,
                   why='Para a pessoa com quem você fala, use **your**. Para você mesmo, use **my**.'),
        dictate=[['This is my office.', 'Este é o meu escritório.'], ['This is your room.', 'Este é o seu quarto.'],
                 ['Is this my bed?', 'Esta é a minha cama?'], ['Dinner is at six.', 'O jantar é às seis.']],
        produce=PROD('Um amigo visita a sua casa. **Mostre a casa com This is my… (algo seu) e This is your… (algo para ele).**',
                     'Ex.: This is my room. This is your bed.', ['This is my', 'This is your'],
                     'This is my room. This is your bed. This is your key.',
                     ['Usei This is my…?', 'Usei This is your…?', 'Usei uma palavra da casa?'],
                     [r'\bthis is my\s+\w+', r'\bthis is your\s+\w+', r'\b(?:room|bed|door|window|stairs|key|kitchen|house|hall)\b'],
                     [[['This is my room.', 'Este é o meu quarto.'], ['This is my bed.', 'Esta é a minha cama.']],
                      [['This is your bed.', 'Esta é a sua cama.'], ['This is your key.', 'Esta é a sua chave.']],
                      [['the door', 'a porta'], ['the window', 'a janela']]],
                     ['Meu, certo! 🙋', 'Seu, certo! 🫵', 'Palavra da casa! 🏠'],
                     ['Thank you! I love this house!', 'Obrigado! Eu adoro esta casa!']),
        rs=RS('library', 'hotelroom', 'museum', 'garden', 'bookshop', 'bakery', 'zoo', 'musicroom', 'stage', 'pool', 'fair'),
        sc='castlehall',
    )
    X = dict(
        n=7070011, review=True, names=('Carson', 'Daisy'),
        stage=dict(rs='castlehall', chars=[[CAR, 26, 0, 1.0], [DAI, 55, 1, 1.0], [ANN, 84, 1, 1.0]]),
        obra=dict(name='Downton Abbey', kind='📺 Série de TV · 2010', year='2010',
                  text='Série britânica de TV exibida de 2010 a 2015. A história se passa numa grande casa de campo na Inglaterra, no começo do século XX. Ela mostra a vida da família e dos empregados que moram e trabalham na casa.',
                  line=['Dinner is served.', 'O jantar está servido. (o mordomo anuncia)'],
                  pa=dict(t='castle', e=['🏰', '🔑', '🛏️'], p='f', v=0)),
        gancho=['Carson', 'Welcome, Daisy. This is the hall.', 'Bem-vinda, Daisy. Este é o saguão.'],
        hot=hot([('🔑', 'key', 'chave', 'This is your key.', 'Esta é a sua chave.'),
                 ('🪟', 'window', 'janela', 'This is my window.', 'Esta é a minha janela.'),
                 ('🚪', 'door', 'porta', 'This is your door.', 'Esta é a sua porta.'),
                 ('🛏️', 'bed', 'cama', 'Is this my bed?', 'Esta é a minha cama?'),
                 ('🪜', 'stairs', 'escada', 'This is the stairs.', 'Esta é a escada.')]),
        gap=[GAP('Daisy, this is ___ room.', 'Daisy, este é o seu quarto.', ['my', 'your', 'you'], 1, 'Falando com a Daisy: **your** (seu).'),
             GAP('This is ___ key.', 'Esta é a minha chave.', ['my', 'your', 'me'], 0, 'Para algo seu: **my** (meu/minha).'),
             GAP('___ is your bed.', 'Esta é a sua cama.', ['These', 'They', 'This'], 2, 'Uma coisa só: **This is**.'),
             GAP('Yes, this is ___ window!', 'Sim, esta é a minha janela!', ['your', 'my', 'I'], 1, 'Quem fala diz que é dele: **my**.')],
        trap=[TRAP(['This is you room.', 'This is your room.', 'This is yours room.'], 1, 'Antes do nome da coisa use **your**: your room.'),
              TRAP(['Is this my key?', 'This is my key?', 'Is this me key?'], 0, 'Pergunta: **Is this** my key? O **is** vem primeiro.')],
        sticker=dict(title='Carson e Daisy', sub='Downton Abbey · 2010', rs='castlehall', chars=[[CAR, 34, 0, 1.0], [DAI, 68, 1, 1.0]]),
        speakers={'Carson': CAR, 'Anna': ANN, 'Daisy': DAI},
        rule=dict(who=CAR, head='This is my / your…', sub='Meu é de quem fala. Seu é de quem ouve.',
                  say=['This is my office.', 'Este é o meu escritório.'],
                  formula=[dict(from_=[['This is', 0], ['my', 1], ['key.', 2]], to=[['This is', 0], ['your', 3], ['key.', 2]], say='This is your key.',
                                note='Para algo **seu**, use **my**. Para algo da **outra pessoa**, troque por **your**.'),
                           dict(from_=[['This is', 0], ['my bed.', 2]], to=[['Is', 0], ['this', 0], ['my bed?', 2]], say='Is this my bed?',
                                note='Na pergunta, o **is** vai para a frente: **Is this** my bed?')],
                  uses=[dict(ico='🙋', tag='Meu', en='This is my office.', pt='Este é o meu escritório.'),
                        dict(ico='🫵', tag='Seu', en='This is your room.', pt='Este é o seu quarto.'),
                        dict(ico='❓', tag='Perguntar', en='Is this my bed?', pt='Esta é a minha cama?')],
                  rules=[dict(tag='my', c=0, text='**Meu / minha**: é de quem está falando.', ex='This is my window.'),
                         dict(tag='your', c=1, text='**Seu / sua**: é da pessoa com quem você fala.', ex='This is your key.'),
                         dict(tag='Is this…?', c=2, text='Para perguntar, comece com **Is this**.', ex='Is this my bed?')],
                  tips=['Em português “seu” pode ser dele, dela ou seu. Em inglês, **your** é só **seu, de você**.']),
        mission_ic='🔑',
    )
    XT = dict(
        exp=[EXP('👉', 'This way, please.', 'Expressão', 'Por aqui, por favor.', 'Para **guiar** alguém até um lugar.',
                 'This way, please, Daisy.', 'Por aqui, por favor, Daisy.'),
             EXP('🚪', 'After you.', 'Expressão', 'Depois de você. (Passe primeiro.)', 'Quando você deixa a outra pessoa **passar primeiro**.',
                 'After you, Mr. Carson.', 'Depois do senhor, Mr. Carson.'),
             EXP('🙋', 'Just ask!', 'Informal', 'É só pedir!', 'Quando alguém pode **pedir ajuda** a qualquer hora.',
                 'Need a key? Just ask!', 'Precisa de uma chave? É só pedir!'),
             EXP('😍', 'Nice place!', 'Informal', 'Que lugar legal!', 'Para **elogiar** uma casa ou um lugar.',
                 'Nice place! It is big!', 'Que lugar legal! É grande!')],
        exp_scene=dict(rs='hall', lines=[
            ['Carson', '**This way, please**, Daisy.', 'Por aqui, por favor, Daisy.'],
            ['Daisy', '**After you**, Mr. Carson.', 'Depois do senhor, Mr. Carson.'],
            ['Carson', 'This is the hall, and this is your kitchen.', 'Este é o saguão, e esta é a sua cozinha.'],
            ['Daisy', '**Nice place**! It is very big.', 'Que lugar legal! É muito grande.'],
            ['Anna', 'Daisy, this is your room. Need a key? **Just ask**!', 'Daisy, este é o seu quarto. Precisa de uma chave? É só pedir!'],
            ['Daisy', 'Thank you, Anna! I love my new room.', 'Obrigada, Anna! Eu adoro o meu quarto novo.']]),
        lab=dict(short='s + consoante', title='Laboratório de sons: o “s” de stairs', say='Em stairs e school o s vem sozinho, antes de outra consoante. Vamos treinar com o Mr. Carson!',
                 intro=dict(what='O **s** no começo de **stairs**, **school** e **stop**: ele vem junto da outra consoante, sem vogal antes.',
                            how='Comece com um “sss” comprido e emende o “t”, o “k” ou o “p”. Não coloque nenhum “i” na frente da palavra.',
                            pt='Em português dizemos “es-ta-dos”. Em inglês, **stairs** é “sss-térz”. Cuidado: **school** não é “iscool”.'),
                 ex=[['stairs', 'STÉRZ', 'escada', 'sss colado no “t”, sem “i” antes'], ['school', 'SKUL', 'escola', 'sss colado no “k”'],
                     ['stop', 'STÓP', 'parar', 'comece com “sss”']],
                 pairs=[['school', 'cool', 'com s: escola · sem s: legal'], ['star', 'tar', '“estrela” × “piche”'], ['stop', 'top', '“parar” × “topo”']],
                 tip='Comece segurando um “sss” (como uma cobra) e só depois solte o “t”. Assim não sai o “i” na frente.',
                 phrase=['Stop! This is my room.', 'Pare! Este é o meu quarto.'],
                 rounds=[RND('cool', ['school', 'cool'], 1, '**Cool** (legal) começa direto no “k”. **School** tem o “sss” antes.'),
                         RND('star', ['star', 'tar'], 0, '**Star** (estrela) tem o “sss” antes do “t”. **Tar** começa direto no “t”.'),
                         RND('top', ['stop', 'top'], 1, '**Top** (topo) começa no “t”. **Stop** (parar) tem o “sss” antes.')]),
        hunt=[HW('cool', ['school', 'cool'], 1, '**cool** (legal) não tem o “sss” no começo.'),
              HP('key', ['🔑', '🚪', '🪟'], 0, '**key** = chave.'),
              HW('stop', ['stop', 'top'], 0, '**stop** (parar) tem o “sss” antes do “t”.'),
              HP('door', ['🪟', '🚪', '🔑'], 1, '**door** = porta.'),
              HW('star', ['tar', 'star'], 1, '**star** (estrela) tem o “sss” antes do “t”.')],
    )
    VB = dict(title='Verbos para cuidar da casa', tip='Quatro verbos: show, open, sleep e clean.', items=[
        VBI('show', '👉', 'mostrar', 'I show the house.', 'Carson show**s** the hall.', 'I show the house.', 'Eu mostro a casa.',
            '**show** = mostrar. Com he/she: **shows**.'),
        VBI('open', '🔓', 'abrir', 'I open the door.', 'Anna open**s** the window.', 'I open the door.', 'Eu abro a porta.',
            '**open** = abrir. Com he/she: **opens**.'),
        VBI('sleep', '😴', 'dormir', 'I sleep in my bed.', 'Daisy sleep**s** in the room.', 'I sleep in my bed.', 'Eu durmo na minha cama.',
            '**sleep** = dormir. Com he/she: **sleeps**.'),
        VBI('clean', '🧹', 'limpar', 'I clean the kitchen.', 'Daisy clean**s** the hall.', 'I clean the kitchen.', 'Eu limpo a cozinha.',
            '**clean** = limpar. Com he/she: **cleans**.')])
    MR = dict(
        mold=[PG('Meu ou seu?', [('começo', [('This is', 'este(a) é')]), ('de quem', [('my', 'meu(minha)'), ('your', 'seu(sua)')]),
                                 ('o quê', [('room', 'quarto'), ('bed', 'cama'), ('key', 'chave'), ('door', 'porta'), ('window', 'janela')])]),
              PG('Perguntar', [('pergunta', [('Is this', 'é este(a)')]), ('de quem', [('my', 'meu(minha)'), ('your', 'seu(sua)')]),
                               ('o quê', [('room', 'quarto'), ('bed', 'cama'), ('key', 'chave'), ('window', 'janela')])], '?'),
              PG('Mostrar a casa', [('começo', [('This is the', 'este(a) é o(a)')]), ('lugar', [('hall', 'saguão'), ('kitchen', 'cozinha'), ('office', 'escritório'), ('door', 'porta')])])],
        speak=[['This is your key.', 'Esta é a sua chave.'], ['And this is my window!', 'E esta é a minha janela!']],
        trap=[dict(ask='“After you” quer dizer…', opts=['Depois de você (passe primeiro)', 'Depois do jantar', 'Atrás de você'], a=0,
                   why='**After you** = depois de você, passe primeiro.', say='After you.'),
              dict(ask='Qual frase está certa?', opts=['Nice a place!', 'Place nice!', 'Nice place!'], a=2,
                   why='A expressão é **Nice place!** (que lugar legal!).', say='Nice place!')],
        gap=[dict(text='___ way, please.', pt='Por aqui, por favor.', opts=['These', 'This', 'Those'], a=1, why='Uma direção só: **This way**.', say='This way, please.'),
             dict(text='Just ___!', pt='É só pedir!', opts=['ask', 'asks', 'asking'], a=0, why='Depois de **just**, o verbo fica simples: Just **ask**!', say='Just ask!')],
        expq=[dict(ask='Você quer mostrar o caminho a um visitante.', opts=['After you.', 'This way, please.', 'Nice place!'], a=1,
                   why='**This way, please.** = por aqui, por favor.'),
              dict(ask='Você abre a porta e deixa o outro passar primeiro.', opts=['After you.', 'Just ask!', 'This way, please.'], a=0,
                   why='**After you.** = depois de você.'),
              dict(ask='Você quer dizer ao colega novo que ele pode pedir ajuda.', opts=['Nice place!', 'After you.', 'Just ask!'], a=2,
                   why='**Just ask!** = é só pedir!')],
        missions=[MIS('🛏️', 'Quarto novo', 'Pergunte com Is this my…?',
                      'Você chega a um quarto novo. **Pergunte com Is this my…? sobre a cama e sobre a chave, e agradeça.**',
                      ['Is this my'], 'Is this my bed? Is this my key? Thank you!',
                      ['Usei Is this my…?', 'Fiz duas perguntas?', 'Agradeci?'],
                      [r'\bis this my\s+\w+\s*\?', r'(?:\bis this my\b[\s\S]*){2}', r'\bthank(?:s| you)\b'],
                      [[['Is this my bed?', 'Esta é a minha cama?']], [['Is this my key?', 'Esta é a minha chave?']], [['Thank you!', 'Obrigado!']]],
                      ['Pergunta certa! ❓', 'Duas perguntas! ✌️', 'Educado! 🙏'],
                      ['Yes, it is. Welcome home!', 'Sim, é. Bem-vindo à casa!']),
              MIS('🏰', 'Guia da casa', 'Use as expressões do episódio.',
                  'Guie um amigo pela casa. **Diga This way, please, mostre algo com This is your… e diga Just ask!**',
                  ['This way'], 'This way, please. This is your room. Just ask!',
                  ['Disse This way, please?', 'Usei This is your…?', 'Disse Just ask?'],
                  [r'\bthis way,? please\b', r'\bthis is your\s+\w+', r'\bjust ask\b'],
                  [[['This way, please.', 'Por aqui, por favor.']], [['This is your room.', 'Este é o seu quarto.']], [['Just ask!', 'É só pedir!']]],
                  ['Bom guia! 👉', 'Seu, certo! 🫵', 'Ajuda oferecida! 🙋'],
                  ['Thanks! Nice place!', 'Obrigado! Que lugar legal!'])])
    CX = [CXI('I sleep in a ___ at night.', 'Eu durmo numa cama à noite.', 'bed', 'key', 'door'),
          CXI('I walk into the room through the ___.', 'Eu entro no quarto pela porta.', 'door', 'window', 'stairs'),
          CXI('It is hot. I open the ___ and the air comes in.', 'Está quente. Abro a janela e o ar entra.', 'window', 'stairs', 'bed'),
          CXI('My room is up. I walk up the ___.', 'Meu quarto é em cima. Eu subo a escada.', 'stairs', 'key', 'room'),
          CXI('I open the front door with a ___.', 'Eu abro a porta da frente com uma chave.', 'key', 'bed', 'window'),
          CXI('This is my ___. I sleep here.', 'Este é o meu quarto. Eu durmo aqui.', 'room', 'key', 'stairs')]
    return build(B, X, XT, VB, MR, CX)

EPS = [ep30(), ep31(), ep32()]
