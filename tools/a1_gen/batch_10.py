# Lote 10 do A1 (posições 103-110). Cada episódio numa função.
# TROCAS DE OBRA: pos 103: de The Gift of the Magi para The Jolly Postman
# TROCAS DE OBRA: pos 104: de The Gift of the Magi para The Polar Express
# TROCAS DE OBRA: pos 105: de Planes, Trains and Automobiles para Curious George
# TROCAS DE OBRA: pos 106: de Planes, Trains and Automobiles para Eloise
# TROCAS DE OBRA: pos 107: de Cinderella para Harry Potter and the Philosopher's Stone
# TROCAS DE OBRA: pos 108: de Cinderella para Finding Nemo
# TROCAS DE OBRA: pos 109: de Alice's Adventures in Wonderland para Peanuts
# TROCAS DE OBRA: pos 110: de Alice's Adventures in Wonderland para Diary of a Wimpy Kid


def vocab(rows):
    return [[w, pt, 'Soa como “%s”.' % s] for w, pt, s in rows]


def RSD(v):
    keys = ['rdg', 'pat', 'vplay', 'sbuild', 'build', 'order', 'balloons', 'dictate', 'soundlab', 'scene', 'dquiz',
            'scenebuild', 'produce', 'review', 'wrap']
    return dict(zip(keys, v))


def hot(rows):
    return [dict(e=e, x=x, y=y, en=en, pt=pt, say=s, sayPt=sp) for e, x, y, en, pt, s, sp in rows]


def G(q, pt, opts, a, why):
    return dict(q=q, pt=pt, opts=opts, a=a, why=why)


def T(opts, a, why, q='Qual frase está certa?'):
    return dict(q=q, opts=opts, a=a, why=why)


def QZ(q, pt, opts, a, line, why):
    return dict(q=q, pt=pt, opts=opts, a=a, line=line, why=why)


def exp(ic, en, tag, pt, use, ex_en, ex_pt):
    return dict(ic=ic, en=en, tag=tag, pt=pt, use=use, ex=[ex_en, ex_pt])


def vb(title, tip, rows):
    items = []
    for v, v3, ic, pt, f1, f2, exen, expt in rows:
        items.append(dict(v=v, ic=ic, pt=pt, f=[['eu', f1], ['ele/ela', f2]], ex=[exen, expt],
                          note='**%s** = %s. Com he/she: **%s**.' % (v, pt, v3)))
    return dict(title=title, tip=tip, items=items)


def pg(label, slots, end=('.', '.')):
    return dict(label=label, slots=[dict(cat=c, opts=[list(o) for o in os_]) for c, os_ in slots], end=list(end))


def mission(ic, name, desc, prompt, chips, model, check, kw, tips, ok, reply):
    return dict(ic=ic, name=name, desc=desc, data=dict(
        prompt=prompt, ph='Escreva a sua resposta aqui…', chips=chips, model=model, check=check, kw=kw,
        tips=tips, ok=ok, reply=reply))


def cx(rows):
    return [dict(text=t, pt=p, opts=o, a=0) for t, p, o in rows]


def hunt_t(say, opts, a, why, ask='Ouça e toque na palavra.'):
    return dict(fig='🎧', say=say, ask=ask, opts=opts, a=a, why=why)


def hunt_p(say, opts, a, why):
    return dict(fig='🎧', say=say, ask='Ouça e toque na figura.', opts=[[e, ''] for e in opts], a=a, why=why, pic=1)


def rnd(say, opts, a, why):
    return dict(fig='🎧', say=say, ask='Qual palavra você ouviu?', opts=opts, a=a, why=why)


def lab(short, title, say, what, how, pt, ex, pairs, tip, phrase, rounds, hunt):
    return dict(short=short, title=title, say=say, intro=dict(what=what, how=how, pt=pt), ex=ex, pairs=pairs,
                tip=tip, phrase=phrase, rounds=rounds), hunt


def produce(prompt, ph, chips, model, check, kw, tips, ok, reply):
    return dict(prompt=prompt, ph=ph, chips=chips, model=model, check=check, kw=kw, tips=tips, ok=ok, reply=reply)


def sticker_chars(a, b):
    return [[a, 34, 0, 1.0], [b, 68, 1, 1.0]]


EPS = []


# ======================================================================= 103 · The Jolly Postman
def ep103():
    PM = 'p:short:3b2a20:f4c7a1:2b6cb0:hat:suit'
    GL = 'p:long:f1c40f:f4c7a1:d69e2e:bow:dress'
    WF = 'e:🐺'
    L, H = lab(
        'e × i', 'Laboratório de sons: o “e” de letter e o “i” de pin',
        'Letter, ten, pen! O “e” inglês é aberto. Vamos treinar com o carteiro.',
        'O som **e** de **letter**, **ten** e **pen** é aberto, parecido com o “é” de “café”.',
        'Abra um pouco a boca e deixe a língua baixa, como em “pé”. No **i** curto de **pin** a boca fica mais fechada e relaxada.',
        'Muitos brasileiros dizem **pen** como **pin**. Cuidado: **ten** (dez) não é **tin** (lata).',
        [['letter', 'LÉ-ter', 'carta', 'boca aberta, como em “pé”'],
         ['pen', 'PÉN', 'caneta', 'não diga PIN'],
         ['ten', 'TÉN', 'dez', 'o “e” é aberto']],
        [['pen', 'pin', '“caneta” × “alfinete”'], ['ten', 'tin', '“dez” × “lata”'], ['bet', 'bit', '“apostar” × “pedaço”']],
        'Diga “pé” e “pin” em sequência: o primeiro tem a boca bem mais aberta.',
        ['Ten letters, ten pens.', 'Dez cartas, dez canetas.'],
        [rnd('ten', ['ten', 'tin'], 0, '**Ten** (dez) tem o “e” aberto. **Tin** é lata.'),
         rnd('pin', ['pen', 'pin'], 1, '**Pin** (alfinete) tem o “i” curto e fechado. **Pen** é caneta.'),
         rnd('bit', ['bet', 'bit'], 1, '**Bit** (pedaço) tem o “i” curto. **Bet** (apostar) tem o “e” aberto.')],
        [hunt_t('pen', ['pen', 'pin'], 0, '**pen** (caneta) tem o “e” aberto.'),
         hunt_p('letter', ['✉️', '📌', '📦'], 0, '**letter** = carta.'),
         hunt_t('tin', ['ten', 'tin'], 1, '**tin** (lata) tem o “i” curto.'),
         hunt_t('bet', ['bet', 'bit'], 0, '**bet** (apostar) tem o “e” aberto.'),
         hunt_p('pin', ['✉️', '📌', '📦'], 1, '**pin** = alfinete.')])
    B = dict(
        title='Who Is It For? · for + pessoa',
        sub='Perguntar para quem é e responder com It’s for me / you / him / her',
        pattern_label='Who is it for?',
        why='Hoje você aprende a perguntar Who is it for? e a responder It’s for me, for you, for him ou for her, como o carteiro do livro.',
        vocab=vocab([('Letter', 'Carta', 'LÉ-ter'), ('Parcel', 'Encomenda', 'PÁR-sel'), ('Envelope', 'Envelope', 'ÉN-ve-lôup'),
                     ('Mailbox', 'Caixa de correio', 'MÊIL-box'), ('Mailman', 'Carteiro', 'MÊIL-men'),
                     ('Postcard', 'Cartão-postal', 'PÔUST-card'), ('For', 'Para', 'FÓR')]),
        balloons=[['✉️', 'letter'], ['📦', 'parcel'], ['💌', 'envelope'], ['📮', 'mailbox'], ['🧑‍💼', 'mailman'], ['🖼️', 'postcard']],
        cover_art=dict(s='forest', items=[['📦', 104, 56, 20, 'bob'], ['✉️', 138, 44, 12, 'bob'], ['📮', 84, 34, 12, 'bob']], seed='jp1'),
        cover_sub='Who is it for? Em 10 minutos você diz para quem é cada carta',
        cover_say='O carteiro chega com uma encomenda, uma carta e um cartão-postal. Mas para quem é cada um? Como perguntar e responder?',
        wrap_recap=[['Who is it for?', 'Para quem é?'], ['It’s for you.', 'É para você.'],
                    ['It’s for him. It’s for her.', 'É para ele. É para ela.'], ['Is it for me?', 'É para mim?']],
        teaser=dict(t='The Polar Express', d='Próximo padrão: Who is it from? It’s from…'),
        cast={'Postman': ['🧑‍💼', '#2b6cb0'], 'Goldilocks': ['👧', '#D69E2E'], 'Wolf': ['🐺', '#4A5568']},
        lines=[['Postman', 'Good morning! I have a parcel.', 'Bom dia! Tenho uma encomenda.'],
               ['Wolf', 'Who is it for? Is it for me?', 'Para quem é? É para mim?'],
               ['Postman', 'No, it isn’t for you. It’s for her.', 'Não, não é para você. É para ela.'],
               ['Goldilocks', 'For me? Thank you!', 'Para mim? Obrigada!'],
               ['Goldilocks', 'And this letter? Who is it for?', 'E esta carta? Para quem é?'],
               ['Postman', 'It’s for him. It’s for the Wolf.', 'É para ele. É para o Lobo.'],
               ['Wolf', 'Oh, it’s for me! Hooray!', 'Ah, é para mim! Oba!'],
               ['Postman', 'One for you, one for her. Have a nice day!', 'Um para você, um para ela. Tenha um bom dia!']],
        quiz=[QZ('Who is the parcel for?', 'Para quem é a encomenda?', [['🐺', 'The Wolf'], ['👧', 'Goldilocks'], ['🧑‍💼', 'The Postman']], 1, 2,
                 'O carteiro diz ao Lobo: “It’s for her.” Ela é a Goldilocks.'),
              QZ('Who is the letter for?', 'Para quem é a carta?', [['👧', 'Goldilocks'], ['🧑‍💼', 'The Postman'], ['🐺', 'The Wolf']], 2, 5,
                 'O carteiro diz: “It’s for him. It’s for the Wolf.”'),
              QZ('Is the parcel for the Wolf?', 'A encomenda é para o Lobo?', [['❌', 'No, it isn’t'], ['✅', 'Yes, it is'], ['🤷', 'Maybe']], 0, 2,
                 'O carteiro diz: “No, it isn’t for you.”')],
        rdg_q=dict(q='A carta é do Max e ele é um menino. Qual resposta está certa para “Who is it for?”',
                   o=['It’s for he.', 'It’s for him.', 'It’s to him.'], a=1,
                   why='Depois de **for** use **him** (ele) ou **her** (ela), nunca he/she.'),
        dictate=[['Who is it for?', 'Para quem é?'], ['It’s for you.', 'É para você.'], ['It’s for me.', 'É para mim.'],
                 ['It’s for him, not for her.', 'É para ele, não para ela.']],
        produce=produce(
            'O carteiro toca a sua campainha. *Who is it for?* **Diga que a encomenda é para você, pergunte para quem é a carta e agradeça.**',
            'Ex.: It’s for me. Who is the letter for? Thank you!',
            ['It’s for me.', 'Who is it for?', 'Thank you!'],
            'It’s for me. Who is the letter for? Thank you!',
            ['Disse que é para mim ou para outra pessoa com It’s for…?', 'Perguntei para quem é com Who is … for?', 'Agradeci?'],
            ["\\bit(?:['’]s| is) for (?:me|you|him|her|us|them)\\b", '\\bwho is (?:it|this|that|the \\w+) for\\b', '\\b(?:thanks|thank you)\\b'],
            [[['It’s for me.', 'É para mim.'], ['It’s for her.', 'É para ela.']],
             [['Who is it for?', 'Para quem é?'], ['Who is the letter for?', 'Para quem é a carta?']],
             [['Thank you!', 'Obrigado!'], ['Thanks!', 'Valeu!']]],
            ['Resposta com for! 📦', 'Pergunta certa! ❓', 'Educado! 🙏'],
            ['Great! Here is your parcel. Have a nice day!', 'Ótimo! Aqui está a sua encomenda. Tenha um bom dia!']),
        rs=RSD(['bookshop', 'garden', 'bakery', 'playground', 'supermarket', 'farm', 'pharmacy', 'library', 'musicroom',
                'postoffice', 'busstop', 'bank', 'museum', 'zoo', 'christmas']),
        sc='postoffice')
    X = dict(
        n=30019, review=True, names=('Postman', 'Goldilocks'),
        stage=dict(rs='postoffice', chars=[[PM, 26, 0, 1.0], [GL, 54, 1, 1.0], [WF, 82, 1, 0.9]]),
        obra=dict(name='The Jolly Postman', kind='📖 Livro infantil · 1986', year='1986',
                  text='Livro ilustrado dos ingleses Janet e Allan Ahlberg, de 1986. Um carteiro alegre anda de bicicleta e entrega cartas a personagens de contos de fadas. Dentro do livro há envelopes de verdade, com cartas para abrir.',
                  line=['Special delivery!', 'Entrega especial! (frase do tema)'],
                  pa=dict(t='postoffice', e=['📮', '✉️', '🚲'], p='c', v=0)),
        gancho=['Goldilocks', 'And this letter? Who is it for?', 'E esta carta? Para quem é?'],
        hot=hot([('📦', 12, 18, 'parcel', 'encomenda', 'The parcel is for her.', 'A encomenda é para ela.'),
                 ('📮', 88, 16, 'mailbox', 'caixa de correio', 'The mailbox is for letters.', 'A caixa de correio é para cartas.'),
                 ('✉️', 14, 84, 'letter', 'carta', 'Who is the letter for?', 'Para quem é a carta?'),
                 ('💌', 86, 84, 'envelope', 'envelope', 'The envelope is for you.', 'O envelope é para você.'),
                 ('🖼️', 50, 10, 'postcard', 'cartão-postal', 'The postcard is for him.', 'O cartão-postal é para ele.')]),
        gap=[G('Who is it ___?', 'Para quem é?', ['for', 'to', 'of'], 0, 'A pergunta termina com **for**: Who is it **for**?'),
             G('It’s for ___. (a menina)', 'É para ela.', ['she', 'her', 'hers'], 1, 'Depois de **for** use **her**.'),
             G('The parcel is for ___. (eu)', 'A encomenda é para mim.', ['I', 'me', 'my'], 1, 'Depois de **for** use **me**.'),
             G('Is it for ___? (o menino)', 'É para ele?', ['he', 'his', 'him'], 2, 'Depois de **for** use **him**.')],
        trap=[T(['For who is it?', 'Who is it for?', 'Who it is for?'], 1, 'A ordem é: **Who is it for?** O **for** fica no fim.'),
              T(['It’s for I.', 'It’s for me.', 'It’s to me.'], 1, 'Depois de **for** use o pronome certo: **for me**.')],
        sticker=dict(title='O Carteiro Alegre', sub='The Jolly Postman · 1986', rs='postoffice', chars=sticker_chars(PM, GL)),
        speakers={'Postman': PM, 'Goldilocks': GL, 'Wolf': WF},
        rule=dict(who=PM, head='Who is it for?', sub='Para quem é? For + me, you, him, her, us, them.',
                  say=['Who is it for? It’s for you.', 'Para quem é? É para você.'],
                  pairsHead='📬 Eu, você, ele… → for + pronome',
                  pairs=[dict(ico='🙋', a='I', b='for <u>me</u>', pta='eu', ptb='para mim', n=1),
                         dict(ico='👉', a='you', b='for <u>you</u>', pta='você', ptb='para você', n=1),
                         dict(ico='👦', a='he', b='for <u>him</u>', pta='ele', ptb='para ele', n=1),
                         dict(ico='👧', a='she', b='for <u>her</u>', pta='ela', ptb='para ela', n=1),
                         dict(ico='🧑‍🤝‍🧑', a='we', b='for <u>us</u>', pta='nós', ptb='para nós', n=2),
                         dict(ico='👥', a='they', b='for <u>them</u>', pta='eles', ptb='para eles', n=2)],
                  uses=[dict(ico='❓', tag='Perguntar', en='Who is it for?', pt='Para quem é?'),
                        dict(ico='📦', tag='Responder', en='It’s for me.', pt='É para mim.'),
                        dict(ico='✉️', tag='Outra pessoa', en='It’s for him.', pt='É para ele.'),
                        dict(ico='🎁', tag='Dar algo', en='This is for you.', pt='Isto é para você.')],
                  rules=[dict(tag='Who is it for?', c=0, text='Pergunta **para quem** é. O **for** fica no fim da frase.', ex='Who is the parcel for?'),
                         dict(tag='It’s for + pessoa', c=2, text='Responda com **It’s for** e um pronome: me, you, him, her, us, them.', ex='It’s for her.'),
                         dict(tag='him / her', c=1, text='Depois de **for** não use he/she. Use **him/her**.', ex='✗ for he  →  ✓ for him')],
                  tips=['Em inglês a pergunta termina em **for**: Who is it **for**? Não dá para começar com “For who”.']),
        mission_ic='📮')
    XT = dict(
        exp=[exp('📦', 'Special delivery!', 'Expressão', 'Entrega especial!', 'Quando alguém chega com algo **importante ou surpresa**.',
                 'Special delivery! It’s for you.', 'Entrega especial! É para você.'),
             exp('🙏', 'Thanks a lot!', 'Informal', 'Muito obrigado!', 'Agradecimento **caloroso**, entre amigos.',
                 'Thanks a lot! It’s for me?', 'Muito obrigada! É para mim?'),
             exp('📭', 'Any mail for me?', 'Expressão', 'Tem correspondência para mim?', 'Pergunta ao **carteiro** ou a quem pega a correspondência.',
                 'Any mail for me today?', 'Tem correspondência para mim hoje?'),
             exp('✍️', 'Sign here, please.', 'Expressão', 'Assine aqui, por favor.', 'Quando uma entrega pede **assinatura**.',
                 'Sign here, please. It’s for you.', 'Assine aqui, por favor. É para você.')],
        exp_scene=dict(rs='garden', lines=[
            ['Postman', '**Special delivery**! A parcel for Goldilocks.', 'Entrega especial! Uma encomenda para a Cachinhos Dourados.'],
            ['Goldilocks', 'For me? **Thanks a lot**!', 'Para mim? Muito obrigada!'],
            ['Postman', '**Sign here, please**.', 'Assine aqui, por favor.'],
            ['Wolf', '**Any mail for me**?', 'Tem correspondência para mim?'],
            ['Postman', 'Yes, one letter. It’s for you.', 'Sim, uma carta. É para você.'],
            ['Wolf', 'Hooray! A letter for me!', 'Oba! Uma carta para mim!']]),
        lab=L, hunt=H)
    VB = vb('Verbos do carteiro', 'Quatro verbos: mail, open, read e give.', [
        ('mail', 'mails', '📮', 'enviar pelo correio', 'I mail a letter.', 'The mailman mail**s** a letter.', 'I mail a letter to my friend.', 'Eu envio uma carta para meu amigo.'),
        ('open', 'opens', '📬', 'abrir', 'I open the envelope.', 'She open**s** the envelope.', 'I open the envelope.', 'Eu abro o envelope.'),
        ('read', 'reads', '📖', 'ler', 'I read the postcard.', 'He read**s** the postcard.', 'I read the postcard.', 'Eu leio o cartão-postal.'),
        ('give', 'gives', '🎁', 'dar', 'I give the parcel to Mom.', 'The mailman give**s** a parcel to Mom.', 'I give the letter to you.', 'Eu dou a carta a você.')])
    MR = dict(
        mold=[pg('Perguntar para quem é', [('pergunta', [('Who is the letter', 'Quem é a carta'), ('Who is the parcel', 'Quem é a encomenda'),
                                                         ('Who is the postcard', 'Quem é o cartão-postal'), ('Who is it', 'Quem é')]),
                                           ('final', [('for', 'para')])], ('?', '?')),
              pg('Responder', [('começo', [('It’s for', 'é para')]),
                               ('pessoa', [('me', 'mim'), ('you', 'você'), ('him', 'ele'), ('her', 'ela'), ('us', 'nós'), ('them', 'eles')])]),
              pg('Dar algo', [('o que', [('This letter is for', 'Esta carta é para'), ('This parcel is for', 'Esta encomenda é para'),
                                         ('This postcard is for', 'Este cartão-postal é para')]),
                              ('quem', [('Mom', 'a mamãe'), ('Dad', 'o papai'), ('you', 'você'), ('him', 'ele'), ('her', 'ela')])])],
        speak=[['Who is it for? It’s for you.', 'Para quem é? É para você.'], ['Special delivery! Thanks a lot!', 'Entrega especial! Muito obrigado!']],
        trap=[dict(ask='“Special delivery!” quer dizer…', opts=['Carta perdida!', 'Entrega especial!', 'Assine aqui!'], a=1,
                   why='**Special delivery!** = entrega especial!', say='Special delivery!'),
              dict(ask='Qual frase está certa?', opts=['Any mails for me?', 'Some mail to me?', 'Any mail for me?'], a=2,
                   why='**Mail** não tem plural: Any **mail** for me?', say='Any mail for me?')],
        gap=[dict(text='Thanks a ___!', pt='Muito obrigado!', opts=['much', 'lot', 'many'], a=1, why='**Thanks a lot!** é a expressão.', say='Thanks a lot!'),
             dict(text='___ here, please.', pt='Assine aqui, por favor.', opts=['Signal', 'Sing', 'Sign'], a=2, why='**Sign** = assinar.', say='Sign here, please.')],
        expq=[dict(ask='Você chega com uma encomenda surpresa. O que diz?', opts=['Sign here, please.', 'Special delivery!', 'Any mail for me?'], a=1,
                   why='**Special delivery!** = entrega especial!'),
              dict(ask='Você quer saber se chegou algo para você.', opts=['Thanks a lot!', 'Sign here, please.', 'Any mail for me?'], a=2,
                   why='**Any mail for me?** = tem correspondência para mim?'),
              dict(ask='Alguém te entrega um presente e você agradece com carinho.', opts=['Thanks a lot!', 'Special delivery!', 'Sign here, please.'], a=0,
                   why='**Thanks a lot!** = muito obrigado!')],
        missions=[mission('📮', 'Carteiro por um dia', 'Entregue uma encomenda.',
                          'Você é o carteiro e chega a uma casa. **Diga Special delivery!, diga para quem é a encomenda e peça uma assinatura.**',
                          ['Special delivery!'], 'Special delivery! It’s for you. Sign here, please.',
                          ['Disse Special delivery!?', 'Disse para quem é com for?', 'Pedi a assinatura?'],
                          ['\\bspecial delivery\\b', '\\bfor (?:you|him|her|them|us|me)\\b', '\\bsign here\\b'],
                          [[['Special delivery!', 'Entrega especial!']], [['It’s for you.', 'É para você.']], [['Sign here, please.', 'Assine aqui, por favor.']]],
                          ['Entrega feita! 📦', 'Destinatário certo! 🎯', 'Assinatura pedida! ✍️'],
                          ['Thank you! Have a nice day!', 'Obrigada! Tenha um bom dia!']),
                  mission('✉️', 'Correio em casa', 'Pergunte pelas cartas.',
                          'Você chega em casa. **Pergunte se tem correspondência para você, pergunte para quem é uma carta e agradeça.**',
                          ['Any mail for me?'], 'Any mail for me? Who is this letter for? Thanks a lot!',
                          ['Perguntei por correspondência?', 'Perguntei para quem é a carta?', 'Agradeci?'],
                          ['\\bany mail for me\\b', '\\bwho is (?:this|the|that|it)[^.!?]*for\\b', '\\b(?:thanks a lot|thank you)\\b'],
                          [[['Any mail for me?', 'Tem correspondência para mim?']], [['Who is this letter for?', 'Para quem é esta carta?']], [['Thanks a lot!', 'Muito obrigado!']]],
                          ['Boa pergunta! 📭', 'Para quem? ❓', 'Educado! 🙏'],
                          ['It’s for you! Here you go.', 'É para você! Aqui está.'])])
    CX = cx([('Dear Ana, I miss you! Love, Bia. This is a ___.', 'Querida Ana, sinto sua falta! Beijos, Bia. Isto é uma carta.', ['letter', 'parcel', 'mailbox']),
             ('It is a big box with a toy inside. The mailman has a ___ for me.', 'É uma caixa grande com um brinquedo dentro. O carteiro tem uma encomenda para mim.', ['parcel', 'postcard', 'letter']),
             ('You put the paper inside it before you mail it. It’s the ___.', 'Você põe o papel dentro dele antes de enviar. É o envelope.', ['envelope', 'mailbox', 'mailman']),
             ('I put my letter in the red ___ on the street.', 'Ponho minha carta na caixa de correio vermelha na rua.', ['mailbox', 'parcel', 'postcard']),
             ('He brings letters to every house. He is the ___.', 'Ele leva cartas a todas as casas. Ele é o carteiro.', ['mailman', 'envelope', 'letter']),
             ('I am on vacation in Rio. I send a ___ to my grandma.', 'Estou de férias no Rio. Mando um cartão-postal para minha avó.', ['postcard', 'mailbox', 'parcel'])])
    return dict(B=B, X=X, XT=XT, VB=VB, MR=MR, CX=CX)


EPS.append(ep103())


# ======================================================================= 104 · The Polar Express
def ep104():
    BOY = 'p:cap:6b3f26:f4c7a1:3b82c4:none:shirt'
    CON = 'p:short:2d2d2d:e8b48a:1a365d:hat:suit'
    SAN = 'p:short:f5f5f5:f4c7a1:c0392b:beard:suit'
    L, H = lab(
        'l final', 'Laboratório de sons: o “l” final de bell',
        'Bell, tell, hill! No fim da palavra o “l” inglês é bem diferente do nosso.',
        'O **l** no fim de **bell**, **tell** e **hill** não vira “u”. A ponta da língua toca atrás dos dentes de cima.',
        'Diga a vogal e, sem fechar a boca, suba a ponta da língua até a gengiva atrás dos dentes de cima. Segure um instante.',
        'Em português “mil” soa como “miu”. Em inglês, se você diz “béu”, soa como **bay**. Faça o toque da língua para **bell** soar certo.',
        [['bell', 'BÉL', 'sino', 'termine com a língua no céu da boca'],
         ['tell', 'TÉL', 'contar, dizer', 'não diga “téu”'],
         ['hill', 'RIL', 'colina', 'o “l” final firme']],
        [['bell', 'bed', '“sino” × “cama”'], ['tell', 'ten', '“contar” × “dez”'], ['hill', 'hit', '“colina” × “bater”']],
        'Diga “bell” e fique com a língua no lugar do “l” por um segundo.',
        ['The bell is on the tree.', 'O sino está na árvore.'],
        [rnd('bell', ['bell', 'bed'], 0, 'Em **bell** a língua toca no fim. **Bed** (cama) termina com “d”.'),
         rnd('ten', ['tell', 'ten'], 1, '**Ten** (dez) termina em “n”. **Tell** termina com o “l” firme.'),
         rnd('hill', ['hit', 'hill'], 1, '**Hill** (colina) termina em “l”. **Hit** termina em “t”.')],
        [hunt_t('tell', ['tell', 'ten'], 0, '**tell** termina com “l”.'),
         hunt_p('bell', ['🛏️', '🔔', '🎄'], 1, '**bell** = sino.'),
         hunt_t('bed', ['bell', 'bed'], 1, '**bed** (cama) termina com “d”.'),
         hunt_t('hill', ['hill', 'hit'], 0, '**hill** termina com “l”.'),
         hunt_p('bed', ['🛏️', '🔔', '🎄'], 0, '**bed** = cama.')])
    B = dict(
        title='Who Is It From? · from',
        sub='Perguntar quem mandou e responder com It’s from…',
        pattern_label='Who is it from?',
        why='Hoje você aprende a perguntar Who is it from? e a dizer de quem veio um presente: It’s from Santa, It’s from my mom.',
        vocab=vocab([('Gift', 'Presente', 'GUIFT'), ('Card', 'Cartão', 'KÁRD'), ('Bell', 'Sino', 'BÉL'),
                     ('Ribbon', 'Fita', 'RÍ-bon'), ('Tree', 'Árvore', 'TRÍ'), ('Santa', 'Papai Noel', 'SÉN-ta'),
                     ('From', 'De (vindo de)', 'FRÂM')]),
        balloons=[['🎁', 'gift'], ['💌', 'card'], ['🔔', 'bell'], ['🎀', 'ribbon'], ['🎄', 'tree'], ['🎅', 'Santa']],
        cover_art=dict(s='traincar', items=[['🔔', 104, 56, 20, 'bob'], ['🎁', 138, 44, 12, 'bob'], ['🚂', 84, 34, 12, 'bob']], seed='pe1'),
        cover_sub='Who is it from? Em 10 minutos você descobre de quem veio cada presente',
        cover_say='É Natal e tem uma caixa misteriosa embaixo da árvore. Quem mandou? Como perguntar e responder em inglês?',
        wrap_recap=[['Who is it from?', 'Quem mandou?'], ['It’s from Santa.', 'É do Papai Noel.'],
                    ['It’s for me. It’s from Mom.', 'É para mim. É da mamãe.'], ['Is it from you?', 'É de você?']],
        teaser=dict(t='Curious George', d='Próximo padrão: take a bus, take a taxi, take a train'),
        cast={'Boy': ['👦', '#3B82C4'], 'Conductor': ['🚂', '#1A365D'], 'Santa': ['🎅', '#C0392B']},
        lines=[['Boy', 'Wow! A big box. Who is it from?', 'Uau! Uma caixa grande. Quem mandou?'],
               ['Conductor', 'Read the card. It’s from Santa.', 'Leia o cartão. É do Papai Noel.'],
               ['Boy', 'From Santa? Is it for me?', 'Do Papai Noel? É para mim?'],
               ['Conductor', 'Yes, it is. It’s for you.', 'Sim. É para você.'],
               ['Boy', 'And this small box? Who is it from?', 'E esta caixa pequena? Quem mandou?'],
               ['Santa', 'Ho ho ho! It’s from the elves.', 'Ho ho ho! É dos duendes.'],
               ['Boy', 'Thank you! Is this bell from the sleigh?', 'Obrigado! Este sino é do trenó?'],
               ['Santa', 'Yes, it is. Merry Christmas!', 'Sim. Feliz Natal!']],
        quiz=[QZ('Who is the big box from?', 'De quem é a caixa grande?', [['🚂', 'The Conductor'], ['🧝', 'The elves'], ['🎅', 'Santa']], 2, 1,
                 'O Condutor diz: “It’s from Santa.”'),
              QZ('Who is the small box from?', 'De quem é a caixa pequena?', [['🧝', 'The elves'], ['🚂', 'The Conductor'], ['🎅', 'Santa']], 0, 5,
                 'Santa diz: “It’s from the elves.”'),
              QZ('Is the bell from the sleigh?', 'O sino é do trenó?', [['❌', 'No, it isn’t'], ['✅', 'Yes, it is'], ['🤷', 'Maybe']], 1, 7,
                 'Santa responde: “Yes, it is.”')],
        rdg_q=dict(q='O presente veio da sua mãe. Qual frase está certa?',
                   o=['It’s for my mom.', 'It’s from my mom.', 'It’s of my mom.'], a=1,
                   why='**from** mostra de quem veio. **For** seria “para a minha mãe”.'),
        dictate=[['Who is it from?', 'Quem mandou?'], ['It’s from Santa.', 'É do Papai Noel.'], ['It’s from my mom.', 'É da minha mãe.'],
                 ['Is it from you?', 'É de você?']],
        produce=produce(
            'Seu amigo mostra um presente com um cartão. **Pergunte quem mandou, diga que é para você (for) e diga de quem veio (from).**',
            'Ex.: Who is it from? It’s for me. It’s from my mom.',
            ['Who is it from?', 'It’s for me.', 'It’s from…'],
            'Who is it from? It’s for me. It’s from my mom.',
            ['Perguntei quem mandou com Who is it from?', 'Disse para quem é com It’s for…?', 'Disse de quem veio com It’s from…?'],
            ['\\bwho is (?:it|this|the \\w+) from\\b', "\\bit(?:['’]s| is) for (?:me|you|him|her|us|them)\\b", "\\bit(?:['’]s| is) from \\w+"],
            [[['Who is it from?', 'Quem mandou?'], ['Who is the card from?', 'Quem mandou o cartão?']],
             [['It’s for me.', 'É para mim.'], ['It’s for her.', 'É para ela.']],
             [['It’s from Dad.', 'É do papai.'], ['It’s from my friend.', 'É do meu amigo.']]],
            ['Pergunta certa! ❓', 'Para quem? 🎁', 'De quem? 💌'],
            ['Nice gift! Merry Christmas!', 'Que presente legal! Feliz Natal!']),
        rs=RSD(['mountain', 'stage', 'hotelroom', 'restaurant', 'fair', 'bakery', 'library', 'museum', 'pool', 'christmas',
                'garden', 'shop', 'zoo', 'harbor', 'stadium']),
        sc='christmas')
    X = dict(
        n=7030019, review=True, names=('Boy', 'Conductor'),
        stage=dict(rs='christmas', chars=[[BOY, 26, 0, 1.0], [CON, 56, 1, 1.0], [SAN, 84, 1, 1.0]]),
        obra=dict(name='The Polar Express', kind='📖 Livro infantil · 1985', year='1985',
                  text='Livro ilustrado do americano Chris Van Allsburg, de 1985. Na véspera de Natal, um menino embarca num trem misterioso rumo ao Polo Norte. Lá, o Papai Noel lhe dá o primeiro presente do Natal: um sino de prata. O livro ganhou a Medalha Caldecott em 1986.',
                  line=['Merry Christmas!', 'Feliz Natal! (frase do tema)'],
                  pa=dict(t='snowvillage', e=['🚂', '🔔', '🎄'], p='d', v=1)),
        gancho=['Boy', 'Wow! A big box. Who is it from?', 'Uau! Uma caixa grande. Quem mandou?'],
        hot=hot([('🎄', 12, 20, 'tree', 'árvore', 'The gift is under the tree. Who is it from?', 'O presente está embaixo da árvore. Quem mandou?'),
                 ('🔔', 88, 16, 'bell', 'sino', 'The bell is from Santa.', 'O sino é do Papai Noel.'),
                 ('🎁', 86, 82, 'gift', 'presente', 'This gift is from my mom.', 'Este presente é da minha mãe.'),
                 ('🎀', 14, 84, 'ribbon', 'fita', 'The ribbon is red. It’s from Dad.', 'A fita é vermelha. É do papai.'),
                 ('💌', 50, 88, 'card', 'cartão', 'The card is for you. It’s from me.', 'O cartão é para você. É meu.')]),
        gap=[G('Who is it ___?', 'Quem mandou?', ['for', 'from', 'to'], 1, 'Quem mandou = de onde veio: Who is it **from**?'),
             G('It’s ___ Santa.', 'É do Papai Noel.', ['of', 'to', 'from'], 2, 'Veio dele: It’s **from** Santa.'),
             G('It’s for me. It’s ___ my mom.', 'É para mim. É da minha mãe.', ['from', 'for', 'at'], 0, 'De quem veio = **from**; para quem vai = for.'),
             G('Is it ___ you?', 'É de você?', ['to', 'from', 'by to'], 1, 'Para saber quem mandou: Is it **from** you?')],
        trap=[T(['Who is it of?', 'Who is it from?', 'Who it is from?'], 1, 'A pergunta é **Who is it from?** Não use “of”.'),
              T(['It’s from for my mom.', 'It’s for my mom from.', 'It’s from my mom.'], 2, 'Diga só uma palavra: **from** + pessoa.')],
        sticker=dict(title='O Sino do Polo Norte', sub='The Polar Express · 1985', rs='snow', chars=sticker_chars(BOY, SAN)),
        speakers={'Boy': BOY, 'Conductor': CON, 'Santa': SAN},
        rule=dict(who=CON, head='Who is it from?', sub='from = de quem veio. for = para quem vai.',
                  say=['Read the card. It’s from Santa.', 'Leia o cartão. É do Papai Noel.'],
                  formula=[dict(from_=[['Who', 0], ['is it', 1], ['from?', 2]], to=[['It’s', 1], ['from', 2], ['Santa.', 3]],
                                say='Who is it from? It’s from Santa.', note='A pergunta termina com **from**. A resposta põe a pessoa depois de **from**.'),
                           dict(from_=[['It’s', 1], ['for', 0], ['me.', 3]], to=[['It’s', 1], ['from', 2], ['Mom.', 3]],
                                say='It’s for me. It’s from Mom.', note='**for** = para quem recebe. **from** = quem mandou.')],
                  uses=[dict(ico='❓', tag='Perguntar', en='Who is it from?', pt='Quem mandou?'),
                        dict(ico='🎅', tag='Responder', en='It’s from Santa.', pt='É do Papai Noel.'),
                        dict(ico='🙋', tag='Para mim', en='It’s for me.', pt='É para mim.'),
                        dict(ico='🤔', tag='Confirmar', en='Is it from you?', pt='É de você?')],
                  rules=[dict(tag='Who is it from?', c=0, text='Pergunta **quem mandou**. O **from** fica no fim.', ex='Who is the card from?'),
                         dict(tag='It’s from + pessoa', c=2, text='Responda com **It’s from** e quem mandou.', ex='It’s from my mom.'),
                         dict(tag='for × from', c=1, text='**for** é quem recebe. **from** é quem manda.', ex='It’s for you. It’s from Dad.')],
                  tips=['Você já viu **from** em “I’m from Brazil”. É a mesma ideia: o ponto de onde algo vem.']),
        mission_ic='🎁')
    XT = dict(
        exp=[exp('🎄', 'Merry Christmas!', 'Expressão', 'Feliz Natal!', 'Para **desejar** um bom Natal a alguém.',
                 'Merry Christmas, Mom!', 'Feliz Natal, mãe!'),
             exp('🙈', 'You shouldn’t have.', 'Expressão', 'Você não precisava.', 'Quando alguém te dá um presente e você fica **tocado**.',
                 'A gift? You shouldn’t have!', 'Um presente? Você não precisava!'),
             exp('😲', 'What a surprise!', 'Expressão', 'Que surpresa!', 'Quando algo **inesperado** acontece, bom ou ruim.',
                 'What a surprise! It’s from Dad!', 'Que surpresa! É do papai!'),
             exp('😍', 'I love it!', 'Informal', 'Adorei!', 'Depois de **abrir** um presente ou ver algo bonito.',
                 'A bell! I love it!', 'Um sino! Adorei!')],
        exp_scene=dict(rs='snow', lines=[
            ['Santa', '**Merry Christmas**, my friend!', 'Feliz Natal, meu amigo!'],
            ['Boy', '**What a surprise**! A gift for me?', 'Que surpresa! Um presente para mim?'],
            ['Conductor', 'Open it! It’s from the elves.', 'Abra! É dos duendes.'],
            ['Boy', 'A bell! **I love it**!', 'Um sino! Adorei!'],
            ['Santa', 'It’s from all of us.', 'É de todos nós.'],
            ['Boy', '**You shouldn’t have**, Santa! Thank you!', 'Você não precisava, Papai Noel! Obrigado!']]),
        lab=L, hunt=H)
    VB = vb('Verbos do Natal', 'Quatro verbos: wrap, send, ring e ride.', [
        ('wrap', 'wraps', '🎁', 'embrulhar', 'I wrap the gift.', 'Mom wrap**s** the gift.', 'I wrap the gift with a ribbon.', 'Eu embrulho o presente com uma fita.'),
        ('send', 'sends', '💌', 'mandar, enviar', 'I send a card.', 'She send**s** a card.', 'I send a card to my friend.', 'Eu mando um cartão para minha amiga.'),
        ('ring', 'rings', '🔔', 'tocar (sino)', 'I ring the bell.', 'He ring**s** the bell.', 'I ring the bell.', 'Eu toco o sino.'),
        ('ride', 'rides', '🚂', 'andar de, viajar em', 'I ride the train.', 'The boy ride**s** the train.', 'I ride the train at night.', 'Eu viajo de trem à noite.')])
    MR = dict(
        mold=[pg('Perguntar quem mandou', [('pergunta', [('Who is the gift from', 'Quem mandou o presente'), ('Who is the card from', 'Quem mandou o cartão'),
                                                         ('Who is the box from', 'Quem mandou a caixa'), ('Who is it from', 'Quem mandou')])], ('?', '?')),
              pg('Responder', [('começo', [('It’s from', 'é de')]),
                               ('quem', [('Santa', 'o Papai Noel'), ('my mom', 'minha mãe'), ('my dad', 'meu pai'), ('my friend', 'meu amigo'),
                                         ('Brazil', 'o Brasil'), ('the elves', 'os duendes')])]),
              pg('for ou from', [('qual', [('It’s for', 'é para'), ('It’s from', 'é de')]),
                                 ('pessoa', [('me', 'mim'), ('you', 'você'), ('him', 'ele'), ('her', 'ela')])])],
        speak=[['Who is it from? It’s from Santa.', 'Quem mandou? É do Papai Noel.'], ['Merry Christmas! I love it!', 'Feliz Natal! Adorei!']],
        trap=[dict(ask='Quando se diz “You shouldn’t have.”?', opts=['Quando você perde um presente', 'Quando alguém te dá um presente e você fica tocado', 'Quando você pede um presente'], a=1,
                   why='**You shouldn’t have.** = você não precisava (agradecendo).', say='You shouldn’t have.'),
              dict(ask='Qual frase está certa?', opts=['I love!', 'Love it I!', 'I love it!'], a=2,
                   why='Adorei = **I love it!** O objeto **it** é necessário.', say='I love it!')],
        gap=[dict(text='___ a surprise!', pt='Que surpresa!', opts=['What', 'How', 'Who'], a=0, why='**What a surprise!** é a expressão.', say='What a surprise!'),
             dict(text='I ___ it!', pt='Adorei!', opts=['loves', 'love', 'am love'], a=1, why='Com **I**, o verbo fica sem -s: I **love** it!', say='I love it!')],
        expq=[dict(ask='Alguém te dá um presente caro e você fica tocado.', opts=['What a surprise!', 'You shouldn’t have.', 'Merry Christmas!'], a=1,
                   why='**You shouldn’t have.** = você não precisava.'),
              dict(ask='Você abre a caixa e gosta muito do presente.', opts=['I love it!', 'Merry Christmas!', 'What a surprise?'], a=0,
                   why='**I love it!** = adorei!'),
              dict(ask='É 25 de dezembro e você cumprimenta a família.', opts=['I love it!', 'You shouldn’t have.', 'Merry Christmas!'], a=2,
                   why='**Merry Christmas!** = Feliz Natal!')],
        missions=[mission('🎁', 'Presente misterioso', 'Descubra quem mandou.',
                          'Você acha um presente com um cartão. **Pergunte quem mandou, diga que é para você e diga que adorou.**',
                          ['Who is it from?'], 'Who is it from? It’s for me! I love it!',
                          ['Perguntei quem mandou?', 'Disse que é para mim?', 'Disse que adorei?'],
                          ['\\bwho is (?:it|this|the \\w+) from\\b', "\\bit(?:['’]s| is) for me\\b", '\\bi love (?:it|this)\\b'],
                          [[['Who is it from?', 'Quem mandou?']], [['It’s for me!', 'É para mim!']], [['I love it!', 'Adorei!']]],
                          ['Boa pergunta! ❓', 'É seu! 🙋', 'Que alegria! 😍'],
                          ['It’s from Santa!', 'É do Papai Noel!']),
                  mission('🎄', 'Cartão de Natal', 'Fale de um cartão que chegou.',
                          'Seu amigo pergunta quem mandou o seu cartão. **Diga que é da sua mãe, deseje Feliz Natal e diga que foi uma surpresa.**',
                          ['It’s from…'], 'It’s from my mom. Merry Christmas! What a surprise!',
                          ['Disse de quem veio com It’s from?', 'Desejei Merry Christmas?', 'Disse What a surprise?'],
                          ["\\bit(?:['’]s| is) from \\w+", '\\bmerry christmas\\b', '\\bwhat a surprise\\b'],
                          [[['It’s from my mom.', 'É da minha mãe.']], [['Merry Christmas!', 'Feliz Natal!']], [['What a surprise!', 'Que surpresa!']]],
                          ['De quem? 💌', 'Natal! 🎄', 'Surpresa! 😲'],
                          ['Merry Christmas to you too!', 'Feliz Natal para você também!'])])
    CX = cx([('Mom puts a box in pretty paper. It is a birthday ___.', 'A mamãe põe uma caixa em papel bonito. É um presente de aniversário.', ['gift', 'tree', 'bell']),
             ('I write “Merry Christmas” on it and put it in an envelope. It’s a Christmas ___.', 'Escrevo “Feliz Natal” nele e ponho num envelope. É um cartão de Natal.', ['card', 'ribbon', 'tree']),
             ('Ding-dong! The sleigh has a silver ___.', 'Ding-dong! O trenó tem um sino de prata.', ['bell', 'gift', 'card']),
             ('The gift has a red ___ on top.', 'O presente tem uma fita vermelha em cima.', ['ribbon', 'bell', 'tree']),
             ('We put lights and a star on the Christmas ___.', 'Colocamos luzes e uma estrela na árvore de Natal.', ['tree', 'card', 'gift']),
             ('He has a white beard and a red suit. He brings gifts. He is ___.', 'Ele tem barba branca e roupa vermelha. Ele traz presentes. Ele é o Papai Noel.', ['Santa', 'ribbon', 'bell'])])
    return dict(B=B, X=X, XT=XT, VB=VB, MR=MR, CX=CX)


EPS.append(ep104())


# ======================================================================= 105 · Curious George
def ep105():
    MAN = 'p:short:8b5a2b:f4c7a1:f1c40f:hat:suit'
    DRV = 'p:cap:2c2c2c:c68642:2f855a:glasses:shirt'
    MIA = 'p:curly:4a2c1a:8d5524:e84393:bow:dress'
    GEO = 'e:🐵'
    L, H = lab(
        's + consoante', 'Laboratório de sons: stop, station, street',
        'Stop! Station! Street! Em inglês tem palavra que começa com “s” colado na consoante.',
        'Em **stop**, **station** e **street** o **s** vem colado na consoante seguinte, sem vogal no meio.',
        'Comece só com o chiado “sss” e, sem parar, emende o “t”. Não coloque um “i” ou “e” antes: nada de “estop”.',
        'Em português dizemos “es-tação”, “es-trada”. Em inglês, se você diz **estop**, soa como outra palavra. Comece direto no “sss”.',
        [['stop', 'STÓP', 'parar, ponto', 'chiado “sss” e já o “t”'],
         ['station', 'STÊI-shon', 'estação', 'sem “e” antes do s'],
         ['street', 'STRÍT', 'rua', 'sss-t-r em sequência']],
        [['stop', 'top', '“parar” × “topo”'], ['spin', 'pin', '“girar” × “alfinete”'], ['sport', 'port', '“esporte” × “porto”']],
        'Faça um “sss” longo antes da palavra: sss-top, sss-tation.',
        ['Stop at the station.', 'Pare na estação.'],
        [rnd('top', ['stop', 'top'], 1, '**Top** começa direto no “t”. **Stop** começa com “sss”.'),
         rnd('spin', ['spin', 'pin'], 0, '**Spin** (girar) começa com “sss”. **Pin** começa com “p”.'),
         rnd('port', ['sport', 'port'], 1, '**Port** (porto) começa com “p”. **Sport** começa com “sss”.')],
        [hunt_t('stop', ['stop', 'top'], 0, '**stop** começa com “sss-t”.'),
         hunt_p('station', ['🚉', '🏔️', '🛑'], 0, '**station** = estação.'),
         hunt_t('pin', ['spin', 'pin'], 1, '**pin** começa direto no “p”.'),
         hunt_t('sport', ['sport', 'port'], 0, '**sport** começa com “sss-p”.'),
         hunt_p('stop', ['🚉', '🏔️', '🛑'], 2, '**stop** = parar / pare.')])
    B = dict(
        title='Take a Bus, Take a Taxi · take + transporte',
        sub='Dizer como você vai: take the bus, take a taxi, take the train',
        pattern_label='take + transporte',
        why='Hoje você aprende a dizer como se desloca com o verbo take: I take the bus, I take a taxi, I take the train.',
        vocab=vocab([('Bus', 'Ônibus', 'BÂS'), ('Taxi', 'Táxi', 'TÉK-si'), ('Train', 'Trem', 'TRÊIN'), ('Subway', 'Metrô', 'SÂB-uei'),
                     ('Plane', 'Avião', 'PLÊIN'), ('Ticket', 'Bilhete, passagem', 'TÍ-kit'), ('Seat', 'Assento, lugar', 'SÍT')]),
        balloons=[['🚌', 'bus'], ['🚕', 'taxi'], ['🚆', 'train'], ['🚇', 'subway'], ['✈️', 'plane'], ['🎫', 'ticket']],
        cover_art=dict(s='harbor', items=[['🚌', 104, 56, 20, 'bob'], ['🐵', 138, 44, 12, 'bob'], ['🎫', 84, 34, 12, 'bob']], seed='cg1'),
        cover_sub='take + transporte. Em 10 minutos você diz como vai para qualquer lugar',
        cover_say='O George, um macaquinho muito curioso, quer ir ao zoológico. Mas como se chega lá? Em inglês, a gente toma o ônibus: take the bus!',
        wrap_recap=[['I take the bus.', 'Eu pego o ônibus.'], ['Take a taxi, please.', 'Pegue um táxi, por favor.'],
                    ['She takes the train.', 'Ela pega o trem.'], ['Take a seat, please.', 'Sente-se, por favor.']],
        teaser=dict(t='Eloise', d='Próximo padrão: take a shower, take a bath, take a nap'),
        cast={'Man': ['🎩', '#D69E2E'], 'Driver': ['🧑‍✈️', '#2F855A'], 'Mia': ['👧', '#E84393']},
        lines=[['Man', 'Let’s go to the zoo, George. We take the bus.', 'Vamos ao zoológico, George. Pegamos o ônibus.'],
               ['Driver', 'Hello! Take a seat, please.', 'Olá! Sente-se, por favor.'],
               ['Man', 'Thank you. Is this the bus to the zoo?', 'Obrigado. Este é o ônibus para o zoológico?'],
               ['Driver', 'No, it isn’t. Take the number twelve.', 'Não. Pegue o número doze.'],
               ['Mia', 'I take the number twelve to school.', 'Eu pego o número doze para a escola.'],
               ['Man', 'Good! We wait here. George, sit down, please.', 'Ótimo! Esperamos aqui. George, sente-se, por favor.'],
               ['Driver', 'Number twelve is here. Take it!', 'O número doze chegou. Pegue!'],
               ['Mia', 'Bye, George! Have fun at the zoo!', 'Tchau, George! Divirta-se no zoológico!']],
        quiz=[QZ('How do they go to the zoo?', 'Como eles vão ao zoológico?', [['🚕', 'By taxi'], ['🚌', 'By bus'], ['🚇', 'By subway']], 1, 0,
                 'O homem diz: “We take the bus.”'),
              QZ('Is this the bus to the zoo?', 'Este é o ônibus para o zoológico?', [['✅', 'Yes, it is'], ['🤷', 'Maybe'], ['❌', 'No, it isn’t']], 2, 3,
                 'O motorista diz: “No, it isn’t.”'),
              QZ('Which number do they take?', 'Qual número eles pegam?', [['1️⃣2️⃣', 'Number 12'], ['2️⃣0️⃣', 'Number 20'], ['2️⃣', 'Number 2']], 0, 3,
                 'O motorista diz: “Take the number twelve.”')],
        rdg_q=dict(q='Como se diz “Eu pego o ônibus para a escola”?',
                   o=['I pick the bus to school.', 'I take the bus to school.', 'I make the bus to school.'], a=1,
                   why='Em inglês usamos **take** com transportes. **Pick** não serve aqui.'),
        dictate=[['We take the bus.', 'Pegamos o ônibus.'], ['I take the train to work.', 'Eu pego o trem para o trabalho.'],
                 ['Take a taxi, please.', 'Pegue um táxi, por favor.'], ['Take a seat, please.', 'Sente-se, por favor.']],
        produce=produce(
            'Seu amigo pergunta como você vai para a escola ou para o trabalho. **Diga qual transporte você pega, para onde vai e a que horas.**',
            'Ex.: I take the bus to work. I take it at seven.',
            ['I take the…', 'to work', 'at seven'],
            'I take the bus to work. I take it at seven.',
            ['Usei I take + transporte?', 'Disse para onde vou com to…?', 'Disse a hora com at?'],
            ['\\bI take (?:the|a) (?:bus|train|subway|taxi|plane)\\b', '\\bto (?:work|school|the \\w+)\\b',
             '\\bat (?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|\\d{1,2})\\b'],
            [[['I take the bus.', 'Eu pego o ônibus.'], ['I take a taxi.', 'Eu pego um táxi.']],
             [['to school', 'para a escola'], ['to work', 'para o trabalho']],
             [['at seven', 'às sete'], ['at eight', 'às oito']]],
            ['Transporte certo! 🚌', 'Destino! 📍', 'Na hora certa! ⏰'],
            ['Nice! I take the subway. It’s fast!', 'Legal! Eu pego o metrô. É rápido!']),
        rs=RSD(['zoo', 'forest', 'bookshop', 'stadium', 'museum', 'garden', 'fair', 'soccerfield', 'bakery', 'busstop',
                'nightcity', 'pharmacy', 'traincar', 'hotelroom', 'christmas']),
        sc='busstop')
    X = dict(
        n=910009, review=True, names=('Man', 'Driver'),
        stage=dict(rs='busstop', chars=[[MAN, 26, 0, 1.0], [GEO, 48, 0, 0.7], [MIA, 78, 1, 1.0]]),
        obra=dict(name='Curious George', kind='📖 Livro infantil · 1941', year='1941',
                  text='Livro ilustrado criado por H. A. Rey e Margret Rey, publicado em 1941. George é um macaquinho muito curioso que o Homem do Chapéu Amarelo leva para a cidade. Onde ele vai, sempre aparece uma aventura nova.',
                  line=['This is George.', 'Este é o George. (o livro começa assim)'],
                  pa=dict(t='busstop', e=['🐵', '🍌', '🚌'], p='e', v=0)),
        gancho=['Man', 'Let’s go to the zoo, George. We take the bus.', 'Vamos ao zoológico, George. Pegamos o ônibus.'],
        hot=hot([('🚕', 12, 16, 'taxi', 'táxi', 'I take a taxi to school.', 'Eu pego um táxi para a escola.'),
                 ('🚏', 50, 10, 'bus stop', 'ponto de ônibus', 'We take the bus here.', 'Pegamos o ônibus aqui.'),
                 ('🚌', 88, 18, 'bus', 'ônibus', 'Take the bus, please.', 'Pegue o ônibus, por favor.'),
                 ('🎫', 14, 84, 'ticket', 'bilhete', 'I have a ticket. I take the bus.', 'Tenho um bilhete. Eu pego o ônibus.'),
                 ('🕐', 86, 84, 'clock', 'relógio', 'I take the bus at one.', 'Eu pego o ônibus à uma.')]),
        gap=[G('We ___ the bus.', 'Nós pegamos o ônibus.', ['pick', 'make', 'take'], 2, 'Com transporte o verbo é **take**: We **take** the bus.'),
             G('She ___ the train to work.', 'Ela pega o trem para o trabalho.', ['takes', 'take', 'taking'], 0, 'Com she, o verbo leva **-s**: She **takes**.'),
             G('___ a taxi, please.', 'Pegue um táxi, por favor.', ['Take', 'Takes', 'To take'], 0, 'Ordem: tire o sujeito e use só **Take**.'),
             G('I take the subway ___ work.', 'Eu pego o metrô para o trabalho.', ['at', 'to', 'in'], 1, 'Destino → **to**: to work.')],
        trap=[T(['I pick the bus.', 'I go the bus.', 'I take the bus.'], 2, 'Não é “pick”. Em inglês você **take** o ônibus.'),
              T(['He take the train.', 'He takes the train.', 'He taking the train.'], 1, 'Com he/she o verbo leva -s: **takes**.')],
        sticker=dict(title='George no Ponto de Ônibus', sub='Curious George · 1941', rs='busstop', chars=sticker_chars(MAN, GEO)),
        speakers={'Man': MAN, 'Driver': DRV, 'Mia': MIA},
        rule=dict(who=MAN, head='take + transporte', sub='Em inglês, você toma o ônibus, o trem, o metrô.',
                  say=['We take the bus.', 'Pegamos o ônibus.'],
                  formula=[dict(from_=[['You', 0], ['take', 1], ['the bus.', 3]], to=[['Take', 1], ['the bus!', 3]],
                                say='Take the bus!', note='Para dar uma dica ou ordem, tire o **you**: Take the bus!'),
                           dict(from_=[['I', 0], ['take', 1], ['a taxi.', 3]], to=[['She', 2], ['takes', 1], ['a taxi.', 3]],
                                say='She takes a taxi.', note='Com **he/she**, o verbo leva **-s**: takes.')],
                  uses=[dict(ico='🚌', tag='Transporte', en='I take the bus.', pt='Eu pego o ônibus.'),
                        dict(ico='🏫', tag='Destino', en='I take the train to school.', pt='Eu pego o trem para a escola.'),
                        dict(ico='🚕', tag='Dica', en='Take a taxi, please.', pt='Pegue um táxi, por favor.'),
                        dict(ico='💺', tag='Outra combinação', en='Take a seat, please.', pt='Sente-se, por favor.')],
                  rules=[dict(tag='take + transporte', c=0, text='Para ir de ônibus, trem ou metrô, use **take**.', ex='take the bus · take the train · take the subway'),
                         dict(tag='the ou a', c=2, text='**the** para o transporte de sempre; **a** para um qualquer.', ex='I take the bus. Take a taxi.'),
                         dict(tag='he/she → takes', c=1, text='Com ele/ela o verbo ganha **-s**.', ex='She takes the train.')],
                  tips=['Em português “pegar o ônibus”. Em inglês o verbo é **take**, nunca “pick” ou “catch” no A1.']),
        mission_ic='🚌')
    XT = dict(
        exp=[exp('💺', 'Take a seat.', 'Expressão', 'Sente-se. / Fique à vontade.', 'Convite educado para **sentar**.',
                 'Take a seat, please.', 'Sente-se, por favor.'),
             exp('🏃', 'Hop on!', 'Informal', 'Suba! / Entre aí!', 'Para chamar alguém a **subir** no ônibus, no táxi ou numa bicicleta.',
                 'Hop on, George! The bus is here!', 'Suba, George! O ônibus chegou!'),
             exp('📍', 'Where to?', 'Informal', 'Para onde?', 'Pergunta do **motorista de táxi** ao passageiro.',
                 'Hello! Where to?', 'Olá! Para onde?'),
             exp('💰', 'Keep the change.', 'Expressão', 'Fique com o troco.', 'Ao pagar, quando você **não quer o troco**.',
                 'Here you are. Keep the change!', 'Aqui está. Fique com o troco!')],
        exp_scene=dict(rs='nightcity', lines=[
            ['Mia', 'Look, a taxi! **Hop on**, George!', 'Olha, um táxi! Suba, George!'],
            ['Driver', 'Hello! **Where to**?', 'Olá! Para onde?'],
            ['Man', 'To the zoo, please.', 'Para o zoológico, por favor.'],
            ['Driver', 'OK. **Take a seat**, please.', 'Certo. Sentem-se, por favor.'],
            ['Man', 'Here you are. **Keep the change**!', 'Aqui está. Fique com o troco!'],
            ['Driver', 'Thank you! Have fun!', 'Obrigado! Divirtam-se!']]),
        lab=L, hunt=H)
    VB = vb('Verbos da viagem', 'Quatro verbos: wait, sit, pay e arrive.', [
        ('wait', 'waits', '⏳', 'esperar', 'I wait for the bus.', 'George wait**s** for the bus.', 'I wait for the bus.', 'Eu espero o ônibus.'),
        ('sit', 'sits', '💺', 'sentar', 'I sit by the window.', 'Mia sit**s** by the window.', 'I sit by the window.', 'Eu sento perto da janela.'),
        ('pay', 'pays', '💳', 'pagar', 'I pay for the ticket.', 'He pay**s** for the ticket.', 'I pay for the ticket.', 'Eu pago a passagem.'),
        ('arrive', 'arrives', '📍', 'chegar', 'I arrive at the zoo.', 'The bus arrive**s** at the zoo.', 'I arrive at the zoo at ten.', 'Eu chego ao zoológico às dez.')])
    MR = dict(
        mold=[pg('Como você vai?', [('quem', [('I take', 'eu pego'), ('We take', 'nós pegamos'), ('You take', 'você pega')]),
                                    ('transporte', [('the bus', 'o ônibus'), ('the train', 'o trem'), ('the subway', 'o metrô'), ('a taxi', 'um táxi'), ('a plane', 'um avião')])]),
              pg('Para onde?', [('transporte', [('I take the bus', 'eu pego o ônibus'), ('I take the train', 'eu pego o trem'), ('I take a taxi', 'eu pego um táxi')]),
                                ('destino', [('to school', 'para a escola'), ('to work', 'para o trabalho'), ('to the zoo', 'para o zoológico'), ('to the airport', 'para o aeroporto')])]),
              pg('Dar uma dica', [('começo', [('Take the', 'Pegue o'), ('Take a', 'Pegue um')]),
                                  ('transporte', [('bus', 'ônibus'), ('train', 'trem'), ('subway', 'metrô'), ('taxi', 'táxi')])], ('!', '!'))],
        speak=[['I take the bus to school.', 'Eu pego o ônibus para a escola.'], ['Hop on! Take a seat.', 'Suba! Sente-se.']],
        trap=[dict(ask='“Keep the change.” quer dizer…', opts=['Troque a moeda.', 'Guarde o bilhete.', 'Fique com o troco.'], a=2,
                   why='**Keep the change.** = fique com o troco.', say='Keep the change.'),
              dict(ask='Qual frase está certa?', opts=['I pick the bus.', 'I take the bus.', 'I go the bus.'], a=1,
                   why='Com ônibus, trem e metrô o verbo é **take**.', say='I take the bus.')],
        gap=[dict(text='___ a seat, please.', pt='Sente-se, por favor.', opts=['Take', 'Pick', 'Make'], a=0, why='**Take a seat** = sentar.', say='Take a seat, please.'),
             dict(text='Where ___?', pt='Para onde?', opts=['to', 'at', 'is'], a=0, why='O motorista pergunta **Where to?**', say='Where to?')],
        expq=[dict(ask='Você quer convidar alguém para sentar.', opts=['Where to?', 'Take a seat.', 'Hop on!'], a=1, why='**Take a seat.** = sente-se.'),
              dict(ask='O taxista quer saber seu destino.', opts=['Keep the change.', 'Hop on!', 'Where to?'], a=2, why='**Where to?** = para onde?'),
              dict(ask='Você paga o táxi e não quer o troco.', opts=['Keep the change.', 'Take a seat.', 'Where to?'], a=0, why='**Keep the change.** = fique com o troco.')],
        missions=[mission('🚌', 'Meu caminho', 'Conte como você vai.',
                          'Diga como você vai para o trabalho ou para a escola. **Diga qual transporte você pega, para onde vai e a que horas pega.**',
                          ['I take the…'], 'I take the bus to work. I take it at seven.',
                          ['Disse qual transporte pego?', 'Disse para onde vou?', 'Disse a hora?'],
                          ['\\bI take (?:the|a) (?:bus|train|subway|taxi|plane)\\b', '\\bto (?:work|school|the \\w+)\\b',
                           '\\bat (?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|\\d{1,2})\\b'],
                          [[['I take the bus.', 'Eu pego o ônibus.']], [['to work', 'para o trabalho']], [['at seven', 'às sete']]],
                          ['Take certo! 🚌', 'Destino! 📍', 'Horário! ⏰'],
                          ['Nice! See you at the bus stop!', 'Legal! Até o ponto de ônibus!']),
                  mission('🚕', 'No táxi', 'Chegue ao destino.',
                          'Você chegou ao destino de táxi. **Diga para onde quer ir, diga Keep the change e agradeça.**',
                          ['Keep the change!'], 'To the zoo, please. Keep the change! Thank you!',
                          ['Disse o destino com to…?', 'Disse Keep the change?', 'Agradeci?'],
                          ['\\bto the \\w+', '\\bkeep the change\\b', '\\b(?:thank you|thanks)\\b'],
                          [[['To the zoo, please.', 'Para o zoológico, por favor.']], [['Keep the change!', 'Fique com o troco!']], [['Thank you!', 'Obrigado!']]],
                          ['Destino dado! 📍', 'Generoso! 💰', 'Educado! 🙏'],
                          ['Thank you! Have a nice day!', 'Obrigado! Tenha um bom dia!'])])
    CX = cx([('It is big, has wheels and drives on the street. Many people ride it to school. It stops every few blocks. It is a ___.', 'É grande, tem rodas e anda na rua. Muita gente vai nele para a escola. Ele para a cada poucos quarteirões. É um ônibus.', ['bus', 'plane', 'ticket']),
             ('I call a car with a driver and a meter. I pay at the end. It is a ___.', 'Chamo um carro com motorista e taxímetro. Pago no fim. É um táxi.', ['taxi', 'train', 'seat']),
             ('It runs on rails and goes from station to station. It’s a ___.', 'Anda sobre trilhos e vai de estação em estação. É um trem.', ['train', 'taxi', 'ticket']),
             ('It goes under the city in a tunnel. I take the ___ to work.', 'Anda embaixo da cidade num túnel. Pego o metrô para o trabalho.', ['subway', 'plane', 'bus']),
             ('It flies high in the sky. I take a ___ to Rio.', 'Voa alto no céu. Pego um avião para o Rio.', ['plane', 'subway', 'seat']),
             ('I show my ___ to the driver before I go in.', 'Mostro minha passagem ao motorista antes de entrar.', ['ticket', 'seat', 'taxi'])])
    return dict(B=B, X=X, XT=XT, VB=VB, MR=MR, CX=CX)


EPS.append(ep105())


# ======================================================================= 106 · Eloise
def ep106():
    ELO = 'p:long:f6d365:f4c7a1:ec4899:bow:dress'
    NAN = 'p:bun:9ca3af:f4c7a1:6b7280:glasses:dress'
    BEL = 'p:short:3b2a20:c68642:7f1d1d:hat:suit'
    L, H = lab(
        'sh × ch', 'Laboratório de sons: sh de shower e ch de cheese',
        'Shower! Cheese! Dois sons parecidos que mudam a palavra inteira.',
        'O **sh** de **shower** e **shoe** é um chiado suave, como quando pedimos silêncio: “shhh”. O **ch** de **cheese** é “tch”, com uma batidinha no início.',
        'Para **sh**: lábios para frente e o ar sai contínuo, sem parar. Para **ch**: encoste a língua no céu da boca, solte o ar de uma vez, como o “tch” de “tchau”.',
        'No português o “x” de “xícara” é igual ao **sh**, mas o “tch” de “tchau” é o **ch** inglês. Cuidado: **shoe** (sapato) ≠ **chew** (mastigar).',
        [['shower', 'SHÁU-er', 'chuveiro, ducha', 'chiado contínuo no começo'],
         ['shoe', 'SHÚ', 'sapato', 'só “shhh”, sem “t”'],
         ['cheese', 'TCHÍZ', 'queijo', 'comece com o “tch”']],
        [['ship', 'chip', '“navio” × “batata frita, ficha”'], ['shoe', 'chew', '“sapato” × “mastigar”'], ['sheep', 'cheap', '“ovelha” × “barato”']],
        'Faça “shhh” sem parar o ar. No “tch”, a língua dá uma batidinha no céu da boca.',
        ['Say cheese in the shower!', 'Diga xis no chuveiro!'],
        [rnd('shoe', ['shoe', 'chew'], 0, '**Shoe** (sapato) é só chiado. **Chew** começa com “tch”.'),
         rnd('cheap', ['sheep', 'cheap'], 1, '**Cheap** (barato) começa com “tch”. **Sheep** (ovelha) é só chiado.'),
         rnd('chip', ['ship', 'chip'], 1, '**Chip** começa com “tch”. **Ship** (navio) é só chiado.')],
        [hunt_t('ship', ['ship', 'chip'], 0, '**ship** (navio) tem só o chiado “sh”.'),
         hunt_p('shower', ['🚿', '🧀', '👟'], 0, '**shower** = chuveiro.'),
         hunt_t('chew', ['shoe', 'chew'], 1, '**chew** (mastigar) começa com “tch”.'),
         hunt_t('sheep', ['sheep', 'cheap'], 0, '**sheep** (ovelha) tem só “sh”.'),
         hunt_p('cheese', ['🚿', '🧀', '👟'], 1, '**cheese** = queijo.')])
    B = dict(
        title='Take a Shower · take + rotina',
        sub='Falar de rotina e descanso: take a shower, take a bath, take a nap',
        pattern_label='take a shower / bath / nap',
        why='Hoje você aprende combinações com take para falar de rotina: take a shower, take a bath, take a nap, take a break, take a photo.',
        vocab=vocab([('Shower', 'Ducha, banho de chuveiro', 'SHÁU-er'), ('Bath', 'Banho de banheira', 'BÉTH'), ('Nap', 'Soneca', 'NÉP'),
                     ('Break', 'Pausa, intervalo', 'BRÊIK'), ('Photo', 'Foto', 'FÔU-tou'), ('Room', 'Quarto, sala', 'RÚM'),
                     ('Towel', 'Toalha', 'TÁU-el')]),
        balloons=[['🚿', 'shower'], ['🛁', 'bath'], ['😴', 'nap'], ['📸', 'photo'], ['🛏️', 'room'], ['☕', 'break']],
        cover_art=dict(s='pool', items=[['🛁', 104, 56, 20, 'bob'], ['🚿', 138, 44, 12, 'bob'], ['😴', 84, 34, 12, 'bob']], seed='el1'),
        cover_sub='take + rotina. Em 10 minutos você descreve o seu dia como a Eloise',
        cover_say='A Eloise mora num hotel e a babá quer que ela tome banho. Mas ela só quer uma soneca! Em inglês, banho, soneca e foto combinam com take.',
        wrap_recap=[['Take a shower, please.', 'Tome um banho, por favor.'], ['I take a nap.', 'Eu tiro uma soneca.'],
                    ['Take a photo of me.', 'Tire uma foto de mim.'], ['Take a break.', 'Faça uma pausa.']],
        teaser=dict(t='Harry Potter and the Philosopher’s Stone', d='Próximo padrão: Whose bag is this? my, your, his, her'),
        cast={'Eloise': ['👧', '#EC4899'], 'Nanny': ['👵', '#6B7280'], 'Bellboy': ['🛎️', '#7F1D1D']},
        lines=[['Nanny', 'Eloise, take a shower now, please.', 'Eloise, tome um banho agora, por favor.'],
               ['Eloise', 'No shower! I take a nap first.', 'Sem banho! Primeiro eu tiro uma soneca.'],
               ['Nanny', 'OK. Take a nap, then take a bath.', 'Certo. Tire uma soneca e depois tome um banho.'],
               ['Eloise', 'A bath? Hot or cold?', 'Um banho? Quente ou frio?'],
               ['Bellboy', 'Room service! Here are the towels.', 'Serviço de quarto! Aqui estão as toalhas.'],
               ['Eloise', 'Thank you! Take a photo of me, please!', 'Obrigada! Tire uma foto de mim, por favor!'],
               ['Bellboy', 'Say cheese! Nice photo!', 'Diga xis! Que foto bonita!'],
               ['Nanny', 'Very nice. Now take a break, then a bath.', 'Muito bem. Agora faça uma pausa, depois o banho.']],
        quiz=[QZ('What does Eloise take first?', 'O que a Eloise faz primeiro?', [['🚿', 'A shower'], ['🛁', 'A bath'], ['😴', 'A nap']], 2, 1,
                 'Eloise diz: “I take a nap first.”'),
              QZ('What does Eloise ask for?', 'O que a Eloise pede?', [['📸', 'A photo'], ['🛎️', 'Room service'], ['🧺', 'A towel']], 0, 5,
                 'Ela diz: “Take a photo of me, please!”'),
              QZ('Is Eloise ready for the shower?', 'A Eloise está pronta para o banho?', [['✅', 'Yes, she is'], ['❌', 'No, she isn’t'], ['🤷', 'Maybe']], 1, 1,
                 'Ela diz: “No shower!”')],
        rdg_q=dict(q='Como se diz “Eu tomo banho às seis”?',
                   o=['I make a shower at six.', 'I do a shower at six.', 'I take a shower at six.'], a=2,
                   why='Banho de chuveiro: **take a shower**. “Make” e “do” não combinam aqui.'),
        dictate=[['Take a shower, please.', 'Tome um banho, por favor.'], ['I take a nap.', 'Eu tiro uma soneca.'],
                 ['Take a photo of me.', 'Tire uma foto de mim.'], ['Take a break.', 'Faça uma pausa.']],
        produce=produce(
            'A babá pergunta sobre a sua rotina. **Diga quando você toma banho, diga que faz uma pausa ou uma soneca e a que horas.**',
            'Ex.: I take a shower at seven. I take a break after lunch.',
            ['I take a shower', 'I take a break', 'at seven'],
            'I take a shower at seven. I take a break after lunch.',
            ['Disse que tomo banho com take a shower/bath?', 'Disse que faço uma pausa ou soneca com take?', 'Disse o horário?'],
            ['\\btake a (?:shower|bath)\\b', '\\btake a (?:break|nap)\\b',
             '\\bat (?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|\\d{1,2})\\b|\\b(?:in the morning|at night|after lunch)\\b'],
            [[['I take a shower.', 'Eu tomo banho.'], ['I take a bath.', 'Eu tomo banho de banheira.']],
             [['I take a nap.', 'Eu tiro uma soneca.'], ['I take a break.', 'Eu faço uma pausa.']],
             [['at seven', 'às sete'], ['after lunch', 'depois do almoço']]],
            ['Banho! 🚿', 'Descanso! 😴', 'Horário! ⏰'],
            ['Good! That’s a nice day, darling.', 'Ótimo! É um dia agradável, querida.']),
        rs=RSD(['playground', 'farm', 'beach', 'fishing', 'library', 'stadium', 'bakery', 'mountain', 'musicroom', 'hotelroom',
                'forest', 'supermarket', 'museum', 'artroom', 'christmas']),
        sc='hotelroom')
    X = dict(
        n=7910009, review=True, names=('Eloise', 'Nanny'),
        stage=dict(rs='hotelroom', chars=[[ELO, 26, 0, 1.0], [NAN, 56, 1, 1.0], [BEL, 84, 1, 1.0]]),
        obra=dict(name='Eloise', kind='📖 Livro ilustrado · 1955', year='1955',
                  text='Livro ilustrado escrito por Kay Thompson e desenhado por Hilary Knight, de 1955. Eloise é uma menina de seis anos que mora no Hotel Plaza, em Nova York, e faz do hotel o seu parque de diversões. A babá tenta, sem sucesso, manter a ordem.',
                  line=['I am Eloise.', 'Eu sou a Eloise. (frase do tema)'],
                  pa=dict(t='suburb', e=['🏨', '🛎️', '🎀'], p='f', v=1)),
        gancho=['Nanny', 'Eloise, take a shower now, please.', 'Eloise, tome um banho agora, por favor.'],
        hot=hot([('🚿', 12, 16, 'shower', 'ducha', 'I take a shower at seven.', 'Eu tomo banho às sete.'),
                 ('🛏️', 50, 10, 'bed', 'cama', 'I take a nap on the bed.', 'Eu tiro uma soneca na cama.'),
                 ('🛁', 88, 16, 'bath', 'banheira', 'Take a bath, Eloise.', 'Tome um banho, Eloise.'),
                 ('📸', 14, 84, 'camera', 'câmera', 'Take a photo of me.', 'Tire uma foto de mim.'),
                 ('🛎️', 86, 84, 'room bell', 'sino da recepção', 'Ring the bell. Take a towel.', 'Toque o sino. Pegue uma toalha.')]),
        gap=[G('I ___ a shower at six.', 'Eu tomo banho às seis.', ['make', 'take', 'do'], 1, 'Banho de chuveiro = **take a shower**.'),
             G('Take a ___ of me, please.', 'Tire uma foto de mim, por favor.', ['photo', 'photos', 'phone'], 0, 'Depois de **a** use o singular: a **photo**.'),
             G('She ___ a nap after lunch.', 'Ela tira uma soneca depois do almoço.', ['take', 'takes', 'taking'], 1, 'Com she o verbo leva -s: She **takes**.'),
             G('Take a ___ and relax.', 'Faça uma pausa e relaxe.', ['break', 'brake', 'bread'], 0, '**break** = pausa. (brake é freio; bread é pão.)')],
        trap=[T(['I do a shower.', 'I make a shower.', 'I take a shower.'], 2, 'Em inglês o banho combina com **take**: take a shower.'),
              T(['Make a photo of me.', 'Do a photo of me.', 'Take a photo of me.'], 2, 'Foto combina com **take**: take a photo.')],
        sticker=dict(title='Eloise no Plaza', sub='Eloise · 1955', rs='hotelroom', chars=sticker_chars(ELO, NAN)),
        speakers={'Eloise': ELO, 'Nanny': NAN, 'Bellboy': BEL},
        rule=dict(who=NAN, head='take a shower / bath / nap', sub='Com take, falamos de rotina e descanso.',
                  say=['Take a nap, then take a bath.', 'Tire uma soneca e depois tome um banho.'],
                  pairsHead='🛁 Em português é “tomar” ou “fazer”. Em inglês é take',
                  pairs=[dict(ico='🚿', a='shower', b='take a <u>shower</u>', pta='ducha', ptb='tomar banho', n=1),
                         dict(ico='🛁', a='bath', b='take a <u>bath</u>', pta='banheira', ptb='tomar banho de banheira', n=1),
                         dict(ico='😴', a='nap', b='take a <u>nap</u>', pta='soneca', ptb='tirar uma soneca', n=1),
                         dict(ico='☕', a='break', b='take a <u>break</u>', pta='pausa', ptb='fazer uma pausa', n=1),
                         dict(ico='📸', a='photo', b='take a <u>photo</u>', pta='foto', ptb='tirar uma foto', n=1)],
                  uses=[dict(ico='🚿', tag='Rotina', en='I take a shower at seven.', pt='Eu tomo banho às sete.'),
                        dict(ico='😴', tag='Descanso', en='I take a nap after lunch.', pt='Eu tiro uma soneca depois do almoço.'),
                        dict(ico='📸', tag='Pedir', en='Take a photo of me.', pt='Tire uma foto de mim.'),
                        dict(ico='👵', tag='Ordem', en='Take a break, Eloise.', pt='Faça uma pausa, Eloise.')],
                  rules=[dict(tag='take a + palavra', c=0, text='Use **take a** com shower, bath, nap, break e photo.', ex='take a shower · take a break'),
                         dict(tag='he/she → takes', c=1, text='Com ele/ela, o verbo leva **-s**.', ex='She takes a nap.'),
                         dict(tag='Não é make/do', c=3, text='Não use “make” ou “do” com essas palavras.', ex='✗ do a shower  →  ✓ take a shower')],
                  tips=['Em português cada palavra pede um verbo (tomar banho, tirar foto, fazer pausa). Em inglês é quase sempre **take**.']),
        mission_ic='🛁')
    XT = dict(
        exp=[exp('📸', 'Say cheese!', 'Informal', 'Diga xis!', 'Antes de tirar uma **foto**, para todo mundo sorrir.',
                 'Say cheese! One, two, three!', 'Diga xis! Um, dois, três!'),
             exp('😌', 'Take it easy.', 'Expressão', 'Vá com calma. / Relaxe.', 'Para pedir que alguém **relaxe** ou se despedir de forma amigável.',
                 'Take it easy, Eloise.', 'Vá com calma, Eloise.'),
             exp('😩', 'I’m beat.', 'Gíria', 'Estou exausto.', 'Quando você está **muito cansado**, sem energia.',
                 'I’m beat! I need a nap.', 'Estou exausta! Preciso de uma soneca.'),
             exp('🏠', 'Make yourself at home.', 'Expressão', 'Fique à vontade.', 'Para receber alguém e dizer que pode **se sentir em casa**.',
                 'Welcome! Make yourself at home.', 'Bem-vindo! Fique à vontade.')],
        exp_scene=dict(rs='pool', lines=[
            ['Nanny', 'You look tired. **Take it easy**, Eloise.', 'Você parece cansada. Vá com calma, Eloise.'],
            ['Eloise', '**I’m beat**, Nanny! Can I take a nap?', 'Estou exausta, Babá! Posso tirar uma soneca?'],
            ['Bellboy', 'Welcome to the pool! **Make yourself at home**.', 'Bem-vinda à piscina! Fique à vontade.'],
            ['Eloise', 'Thanks! Take a photo of me, please.', 'Obrigada! Tire uma foto de mim, por favor.'],
            ['Bellboy', '**Say cheese**!', 'Diga xis!'],
            ['Eloise', 'Cheese!', 'Xis!']]),
        lab=L, hunt=H)
    VB = vb('Verbos da rotina', 'Quatro verbos: brush, wash, sleep e relax.', [
        ('brush', 'brushes', '🪥', 'escovar', 'I brush my teeth.', 'Eloise brush**es** her teeth.', 'I brush my teeth at night.', 'Eu escovo os dentes à noite.'),
        ('wash', 'washes', '🧼', 'lavar', 'I wash my hands.', 'He wash**es** his hands.', 'I wash my hands.', 'Eu lavo as mãos.'),
        ('sleep', 'sleeps', '🛌', 'dormir', 'I sleep in the room.', 'She sleep**s** in the room.', 'I sleep at ten.', 'Eu durmo às dez.'),
        ('relax', 'relaxes', '😌', 'relaxar', 'I relax in the bath.', 'Nanny relax**es** in the bath.', 'I relax after lunch.', 'Eu relaxo depois do almoço.')])
    MR = dict(
        mold=[pg('Minha rotina', [('quem', [('I take', 'eu tomo / tiro / faço'), ('We take', 'nós tomamos / tiramos / fazemos')]),
                                  ('o quê', [('a shower', 'um banho de chuveiro'), ('a bath', 'um banho de banheira'), ('a nap', 'uma soneca'),
                                             ('a break', 'uma pausa'), ('a photo', 'uma foto')])]),
              pg('Quando?', [('ação', [('I take a shower', 'eu tomo banho'), ('I take a nap', 'eu tiro uma soneca'), ('I take a break', 'eu faço uma pausa')]),
                             ('hora', [('at night', 'à noite'), ('in the morning', 'de manhã'), ('after lunch', 'depois do almoço'), ('at six', 'às seis')])]),
              pg('Pedir ou mandar', [('começo', [('Take a', 'Faça / Tire / Tome um'), ('Please take a', 'Por favor, faça / tire / tome um')]),
                                     ('o quê', [('shower', 'banho'), ('break', 'pausa'), ('photo', 'foto'), ('nap', 'soneca')])], ('!', '!'))],
        speak=[['I take a shower at seven.', 'Eu tomo banho às sete.'], ['Say cheese! Take it easy.', 'Diga xis! Vá com calma.']],
        trap=[dict(ask='“I’m beat.” quer dizer…', opts=['Estou com fome.', 'Estou exausto.', 'Estou animado.'], a=1,
                   why='**I’m beat.** = estou exausto (gíria).', say='I’m beat.'),
              dict(ask='Qual frase está certa?', opts=['Make a photo of me.', 'Take a photo of me.', 'Do a photo of me.'], a=1,
                   why='Foto combina com **take**.', say='Take a photo of me.')],
        gap=[dict(text='Say ___!', pt='Diga xis!', opts=['cheese', 'chess', 'chase'], a=0, why='**Say cheese!** antes da foto.', say='Say cheese!'),
             dict(text='___ it easy.', pt='Vá com calma.', opts=['Make', 'Do', 'Take'], a=2, why='**Take it easy.** é a expressão.', say='Take it easy.')],
        expq=[dict(ask='Você está sem energia nenhuma.', opts=['Say cheese!', 'I’m beat.', 'Make yourself at home.'], a=1, why='**I’m beat.** = estou exausto.'),
              dict(ask='Um amigo chega à sua casa e você o recebe.', opts=['Make yourself at home.', 'Take it easy.', 'I’m beat.'], a=0, why='**Make yourself at home.** = fique à vontade.'),
              dict(ask='Você vai tirar uma foto do grupo.', opts=['Take it easy.', 'I’m beat.', 'Say cheese!'], a=2, why='**Say cheese!** = diga xis!')],
        missions=[mission('🚿', 'Meu dia', 'Conte sua rotina.',
                          'Conte a sua rotina. **Diga que você toma um banho, que faz uma pausa e a que horas.**',
                          ['I take a shower'], 'I take a shower at seven. I take a break after lunch.',
                          ['Disse take a shower/bath?', 'Disse take a break/nap?', 'Disse o horário?'],
                          ['\\btake a (?:shower|bath)\\b', '\\btake a (?:break|nap)\\b',
                           '\\bat (?:one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|\\d{1,2})\\b|\\b(?:in the morning|at night|after lunch)\\b'],
                          [[['I take a shower.', 'Eu tomo banho.']], [['I take a break.', 'Eu faço uma pausa.']], [['at seven', 'às sete']]],
                          ['Banho! 🚿', 'Pausa! ☕', 'Horário! ⏰'],
                          ['That’s a good routine!', 'É uma boa rotina!']),
                  mission('📸', 'Foto no hotel', 'Peça uma foto.',
                          'Você está num hotel com um amigo. **Peça uma foto, diga Say cheese! e diga que está exausto com I’m beat.**',
                          ['Say cheese!'], 'Take a photo of me, please. Say cheese! I’m beat.',
                          ['Pedi uma foto com take a photo?', 'Disse Say cheese?', 'Disse I’m beat?'],
                          ['\\btake a photo\\b', '\\bsay cheese\\b', '\\bi[’\']?m beat\\b'],
                          [[['Take a photo of me.', 'Tire uma foto de mim.']], [['Say cheese!', 'Diga xis!']], [['I’m beat.', 'Estou exausto.']]],
                          ['Foto! 📸', 'Sorria! 😁', 'Cansaço! 😩'],
                          ['Cheese! Nice photo!', 'Xis! Que foto bonita!'])])
    CX = cx([('Water falls from above and I wash my hair. It’s a ___.', 'A água cai de cima e eu lavo o cabelo. É uma ducha.', ['shower', 'bath', 'nap']),
             ('I fill the tub with warm water and bubbles. I take a ___.', 'Encho a banheira com água morna e espuma. Tomo um banho de banheira.', ['bath', 'photo', 'room']),
             ('I’m tired. I close my eyes for twenty minutes. It’s a short ___.', 'Estou cansado. Fecho os olhos por vinte minutos. É uma soneca.', ['nap', 'break', 'shower']),
             ('I use my phone camera and click. It’s a ___ of my friends.', 'Uso a câmera do celular e clico. É uma foto dos meus amigos.', ['photo', 'towel', 'bath']),
             ('We stop work for ten minutes and drink coffee. It’s a ___.', 'Paramos o trabalho por dez minutos e tomamos café. É uma pausa.', ['break', 'room', 'nap']),
             ('I sleep in a hotel ___. It has a bed and a TV.', 'Durmo num quarto de hotel. Tem cama e TV.', ['room', 'towel', 'shower'])])
    return dict(B=B, X=X, XT=XT, VB=VB, MR=MR, CX=CX)


EPS.append(ep106())


# ======================================================================= 107 · Harry Potter
def ep107():
    HAR = 'p:short:1f1f1f:f4c7a1:111827:glasses:suit'
    HER = 'p:curly:6b3f26:f4c7a1:7f1d1d:none:dress'
    NEV = 'p:short:7a5230:f4c7a1:7f1d1d:none:shirt'
    L, H = lab(
        'u curto × u longo', 'Laboratório de sons: book e food',
        'Book e food parecem iguais, mas o “u” é diferente! Vamos treinar com os bruxos.',
        'O **u curto** de **book**, **good** e **look** é rápido e relaxado. O **u longo** de **food**, **pool** e **too** é comprido e com os lábios bem redondos.',
        'No curto, os lábios ficam soltos e o som dura pouco. No longo, estique os lábios para frente, como num bico, e segure o som.',
        'No português só temos um “u”. Por isso muita gente diz **full** (cheio) como **fool** (bobo). Cuidado com o tamanho!',
        [['book', 'BÚK', 'livro', 'u curto, lábios soltos'],
         ['good', 'GÚD', 'bom', 'rápido e relaxado'],
         ['food', 'FÚÚD', 'comida', 'u longo, lábios em bico']],
        [['full', 'fool', '“cheio” × “bobo”'], ['pull', 'pool', '“puxar” × “piscina”'], ['look', 'Luke', '“olhar” × “Luke”']],
        'Faça um bico para o u longo (food) e relaxe os lábios para o u curto (book).',
        ['Look at the good book!', 'Olhe para o bom livro!'],
        [rnd('pull', ['pull', 'pool'], 0, '**Pull** (puxar) tem o “u” curto. **Pool** (piscina) tem o “u” longo.'),
         rnd('pool', ['pull', 'pool'], 1, '**Pool** (piscina) tem o “u” longo, com lábios em bico.'),
         rnd('fool', ['full', 'fool'], 1, '**Fool** (bobo) tem o “u” longo. **Full** (cheio) tem o “u” curto.')],
        [hunt_t('full', ['full', 'fool'], 0, '**full** (cheio) tem o “u” curto.'),
         hunt_p('book', ['📖', '🏊', '🍲'], 0, '**book** = livro (u curto).'),
         hunt_t('pool', ['pull', 'pool'], 1, '**pool** (piscina) tem o “u” longo.'),
         hunt_t('look', ['look', 'Luke'], 0, '**look** (olhar) tem o “u” curto.'),
         hunt_p('food', ['📖', '🏊', '🍲'], 2, '**food** = comida (u longo).')])
    B = dict(
        title='Whose Is It? · my, your, his, her',
        sub='Perguntar de quem é com Whose…? e responder com my, your, his, her',
        pattern_label='Whose … is this?',
        why='Hoje você aprende a perguntar de quem é uma coisa com Whose…? e a responder com my, your, his e her, como na escola dos bruxos.',
        vocab=vocab([('Wand', 'Varinha mágica', 'UÓND'), ('Owl', 'Coruja', 'ÁUL'), ('Scarf', 'Cachecol', 'SKÁRF'), ('Cloak', 'Capa', 'KLÔUK'),
                     ('Trunk', 'Baú, mala grande', 'TRÂNK'), ('Whose', 'De quem', 'RÚZ'), ('Name', 'Nome', 'NÊIM')]),
        balloons=[['🪄', 'wand'], ['🦉', 'owl'], ['🧣', 'scarf'], ['🧥', 'cloak'], ['🧳', 'trunk'], ['🏷️', 'name']],
        cover_art=dict(s='library', items=[['🪄', 104, 56, 20, 'bob'], ['🦉', 138, 44, 12, 'bob'], ['🧣', 84, 34, 12, 'bob']], seed='hp1'),
        cover_sub='Whose…? Em 10 minutos você descobre de quem é cada coisa',
        cover_say='Na escola de magia, a caixa de achados e perdidos está cheia: varinha, cachecol, até uma coruja! De quem é cada coisa? Como perguntar em inglês?',
        wrap_recap=[['Whose wand is this?', 'De quem é esta varinha?'], ['It’s my wand.', 'É a minha varinha.'],
                    ['It’s his scarf.', 'É o cachecol dele.'], ['Her name is Hedwig.', 'O nome dela é Hedwig.']],
        teaser=dict(t='Finding Nemo', d='Próximo padrão: mine, yours, his, hers. It’s mine!'),
        cast={'Hermione': ['👧', '#7F1D1D'], 'Harry': ['👦', '#111827'], 'Neville': ['🧑', '#B45309']},
        lines=[['Hermione', 'Look! A wand on the table. Whose wand is this?', 'Olha! Uma varinha na mesa. De quem é esta varinha?'],
               ['Harry', 'It isn’t my wand. Is it your wand, Neville?', 'Não é a minha varinha. É a sua varinha, Neville?'],
               ['Neville', 'No, it isn’t. My wand is in my bag.', 'Não. A minha varinha está na minha bolsa.'],
               ['Hermione', 'Whose scarf is this? It’s red and gold.', 'De quem é este cachecol? É vermelho e dourado.'],
               ['Harry', 'It’s his scarf. Look, the tag says Ron.', 'É o cachecol dele. Olha, a etiqueta diz Ron.'],
               ['Neville', 'And whose owl is this?', 'E de quem é esta coruja?'],
               ['Harry', 'It’s my owl. Her name is Hedwig.', 'É a minha coruja. O nome dela é Hedwig.'],
               ['Hermione', 'Great! Now everything has an owner.', 'Ótimo! Agora tudo tem um dono.']],
        quiz=[QZ('Whose wand is in a bag?', 'De quem é a varinha que está na bolsa?', [['👦', 'Harry’s'], ['👧', 'Hermione’s'], ['🧑', 'Neville’s']], 2, 2,
                 'Neville diz: “My wand is in my bag.”'),
              QZ('Whose scarf is red and gold?', 'De quem é o cachecol vermelho e dourado?', [['🧑‍🦰', 'Ron’s'], ['👦', 'Harry’s'], ['🧑', 'Neville’s']], 0, 4,
                 'Harry lê a etiqueta: “Ron”.'),
              QZ('What is the owl’s name?', 'Qual é o nome da coruja?', [['🐱', 'Crookshanks'], ['🦉', 'Hedwig'], ['🐸', 'Trevor']], 1, 6,
                 'Harry diz: “Her name is Hedwig.”')],
        rdg_q=dict(q='A bolsa é da Hermione. Qual frase está certa?',
                   o=['It’s she bag.', 'It’s her bag.', 'It’s hers bag.'], a=1,
                   why='Antes do nome da coisa use **her** (dela): her bag. **She** é o sujeito e **hers** vem sozinho.'),
        dictate=[['Whose wand is this?', 'De quem é esta varinha?'], ['It’s my wand.', 'É a minha varinha.'],
                 ['Is it your owl?', 'É a sua coruja?'], ['It’s her scarf.', 'É o cachecol dela.']],
        produce=produce(
            'Você acha uma bolsa na sala. **Pergunte de quem é com Whose…?, diga que não é sua e pergunte se é dele ou dela.**',
            'Ex.: Whose bag is this? It isn’t my bag. Is it his bag?',
            ['Whose…?', 'It isn’t my…', 'his / her'],
            'Whose bag is this? It isn’t my bag. Is it his bag?',
            ['Perguntei de quem é com Whose…?', 'Disse que não é meu com my?', 'Usei his, her, your ou their?'],
            ['\\bwhose \\w+ is (?:this|that|it)\\b', "\\b(?:it isn['’]t|it is not|this isn['’]t|that isn['’]t) my \\w+", '\\b(?:his|her|your|their) \\w+'],
            [[['Whose bag is this?', 'De quem é esta bolsa?'], ['Whose coat is that?', 'De quem é aquele casaco?']],
             [['It isn’t my bag.', 'Não é a minha bolsa.'], ['It isn’t my coat.', 'Não é o meu casaco.']],
             [['Is it his bag?', 'É a bolsa dele?'], ['Is it her bag?', 'É a bolsa dela?']]],
            ['Whose certo! ❓', 'My certo! 🙋', 'His/her certo! 👦👧'],
            ['No, it isn’t mine. Ask the teacher!', 'Não, não é minha. Pergunte ao professor!']),
        rs=RSD(['garden', 'pharmacy', 'soccerfield', 'bookshop', 'restaurant', 'farm', 'zoo', 'chefkitchen', 'stadium',
                'castlehall', 'snow', 'bank', 'playground', 'forest', 'fishing']),
        sc='castlehall')
    X = dict(
        n=10160, review=True, names=('Hermione', 'Harry'),
        stage=dict(rs='castlehall', chars=[[HER, 24, 0, 1.0], [HAR, 54, 1, 1.0], [NEV, 84, 1, 1.0]]),
        obra=dict(name='Harry Potter and the Philosopher’s Stone', kind='📖 Livro · 1997', year='1997',
                  text='Primeiro livro da série da escritora britânica J. K. Rowling, publicado em 1997. Harry é um menino órfão que descobre, aos onze anos, que é bruxo. Ele vai estudar em Hogwarts, uma escola de magia, onde conhece Hermione e Ron.',
                  line=['Yer a wizard, Harry.', 'Você é um bruxo, Harry. (fala do Hagrid)'],
                  pa=dict(t='castle', e=['🪄', '🦉', '⚡'], p='g', v=0)),
        gancho=['Hermione', 'Look! A wand on the table. Whose wand is this?', 'Olha! Uma varinha na mesa. De quem é esta varinha?'],
        hot=hot([('🪄', 12, 18, 'wand', 'varinha', 'Whose wand is this? It’s my wand.', 'De quem é esta varinha? É a minha.'),
                 ('🦉', 88, 16, 'owl', 'coruja', 'Her name is Hedwig. It’s my owl.', 'O nome dela é Hedwig. É a minha coruja.'),
                 ('🧣', 14, 84, 'scarf', 'cachecol', 'It’s his scarf.', 'É o cachecol dele.'),
                 ('🧥', 86, 84, 'cloak', 'capa', 'Is this your cloak?', 'Esta é a sua capa?'),
                 ('🧳', 50, 10, 'trunk', 'baú', 'It’s her trunk.', 'É o baú dela.')]),
        gap=[G('___ wand is this?', 'De quem é esta varinha?', ['Whose', 'Who’s', 'Who'], 0, 'De quem é = **Whose**. (Who’s = quem é.)'),
             G('It isn’t ___ wand. (eu)', 'Não é a minha varinha.', ['I', 'me', 'my'], 2, 'Antes do nome da coisa: **my** wand.'),
             G('Is this ___ scarf? (você)', 'Este é o seu cachecol?', ['you', 'your', 'yours'], 1, 'Antes do nome da coisa: **your** scarf.'),
             G('___ name is Hedwig. (a coruja)', 'O nome dela é Hedwig.', ['She', 'Hers', 'Her'], 2, 'Dela, antes do nome: **Her** name.')],
        trap=[T(['Who’s wand is this?', 'Whose wand this is?', 'Whose wand is this?'], 2, '**Whose** (de quem) + coisa + is this? Já **Who’s** quer dizer “quem é”.'),
              T(['It’s he scarf.', 'It’s his scarf.', 'It’s him scarf.'], 1, 'Antes do nome da coisa use **his** (dele).')],
        sticker=dict(title='A Coruja do Harry', sub='Harry Potter and the Philosopher’s Stone · 1997', rs='castlehall', chars=sticker_chars(HAR, HER)),
        speakers={'Hermione': HER, 'Harry': HAR, 'Neville': NEV},
        rule=dict(who=HER, head='Whose…? · my, your, his, her', sub='Whose pergunta de quem é. my, your, his e her respondem.',
                  say=['Whose scarf is this? It’s his scarf.', 'De quem é este cachecol? É o cachecol dele.'],
                  pairsHead='🪄 Eu, você, ele… → my, your, his…',
                  pairs=[dict(ico='🙋', a='I', b='<u>my</u> wand', pta='eu', ptb='minha varinha', n=1),
                         dict(ico='👉', a='you', b='<u>your</u> owl', pta='você', ptb='sua coruja', n=1),
                         dict(ico='👦', a='he', b='<u>his</u> scarf', pta='ele', ptb='o cachecol dele', n=1),
                         dict(ico='👧', a='she', b='<u>her</u> cloak', pta='ela', ptb='a capa dela', n=1),
                         dict(ico='🧑‍🤝‍🧑', a='we', b='<u>our</u> trunk', pta='nós', ptb='nosso baú', n=2),
                         dict(ico='👥', a='they', b='<u>their</u> owls', pta='eles', ptb='as corujas deles', n=2)],
                  uses=[dict(ico='❓', tag='Perguntar', en='Whose wand is this?', pt='De quem é esta varinha?'),
                        dict(ico='🙋', tag='É meu', en='It’s my wand.', pt='É a minha varinha.'),
                        dict(ico='👉', tag='É seu?', en='Is it your owl?', pt='É a sua coruja?'),
                        dict(ico='🦉', tag='Nome', en='Her name is Hedwig.', pt='O nome dela é Hedwig.')],
                  rules=[dict(tag='Whose + coisa', c=0, text='**Whose** pergunta de quem é. Ele vem junto com o nome da coisa.', ex='Whose scarf is this?'),
                         dict(tag='my, your, his, her', c=2, text='Vêm **antes** do nome da coisa.', ex='my wand · his scarf · her cloak'),
                         dict(tag='Whose ≠ Who’s', c=1, text='**Whose** = de quem. **Who’s** = quem é.', ex='Whose bag? · Who’s that?')],
                  tips=['Em português “o meu”, “a sua” mudam com a coisa. Em inglês **my, your, his, her** não mudam: my wand, my owl.']),
        mission_ic='🦉')
    XT = dict(
        exp=[exp('🧳', 'Lost and found', 'Expressão', 'Achados e perdidos', 'Nome do **lugar** onde ficam as coisas perdidas.',
                 'Check the lost and found.', 'Veja nos achados e perdidos.'),
             exp('🪙', 'Finders keepers!', 'Gíria', 'Achado não é roubado!', 'Brincadeira de quem **encontrou algo** e quer ficar com ele.',
                 'A coin! Finders keepers!', 'Uma moeda! Achado não é roubado!'),
             exp('🙅', 'No way!', 'Informal', 'De jeito nenhum! / Não acredito!', 'Para **recusar** algo ou mostrar surpresa.',
                 'No way! That’s my wand!', 'De jeito nenhum! Essa é a minha varinha!'),
             exp('⚠️', 'Watch out!', 'Expressão', 'Cuidado!', 'Aviso de **perigo**, rápido e forte.',
                 'Watch out! The owl is here!', 'Cuidado! A coruja está aqui!')],
        exp_scene=dict(rs='library', lines=[
            ['Hermione', 'Look! The **lost and found** box is full.', 'Olha! A caixa de achados e perdidos está cheia.'],
            ['Neville', 'A coin! **Finders keepers**!', 'Uma moeda! Achado não é roubado!'],
            ['Hermione', '**No way**, Neville! Whose coin is it?', 'De jeito nenhum, Neville! De quem é a moeda?'],
            ['Harry', '**Watch out**! The owl is here!', 'Cuidado! A coruja está aqui!'],
            ['Neville', 'OK, OK. It isn’t my coin.', 'Tá, tá. Não é a minha moeda.'],
            ['Hermione', 'Good. Put it in the box.', 'Bom. Ponha na caixa.']]),
        lab=L, hunt=H)
    VB = vb('Verbos dos achados', 'Quatro verbos: find, lose, keep e carry.', [
        ('find', 'finds', '🔍', 'encontrar', 'I find a wand.', 'Harry find**s** a wand.', 'I find a scarf in the box.', 'Eu encontro um cachecol na caixa.'),
        ('lose', 'loses', '😟', 'perder', 'I lose my scarf.', 'Neville lose**s** his scarf.', 'I lose my cloak.', 'Eu perco a minha capa.'),
        ('keep', 'keeps', '🧰', 'guardar, ficar com', 'I keep my trunk here.', 'She keep**s** her trunk here.', 'I keep my wand in my bag.', 'Eu guardo minha varinha na bolsa.'),
        ('carry', 'carries', '🎒', 'carregar', 'I carry my bag.', 'He carr**ies** his bag.', 'I carry my owl.', 'Eu carrego minha coruja.')])
    MR = dict(
        mold=[pg('De quem é?', [('whose', [('Whose wand', 'De quem é a varinha'), ('Whose owl', 'De quem é a coruja'), ('Whose scarf', 'De quem é o cachecol'),
                                           ('Whose bag', 'De quem é a bolsa'), ('Whose cloak', 'De quem é a capa')]),
                                ('final', [('is this', 'isto'), ('is that', 'aquilo')])], ('?', '?')),
              pg('É meu, seu, dele…', [('de quem', [('It’s my', 'É o meu / a minha'), ('It’s your', 'É o seu / a sua'), ('It’s his', 'É o dele / a dele'),
                                                   ('It’s her', 'É o dela / a dela'), ('It’s our', 'É o nosso / a nossa'), ('It’s their', 'É o deles / a deles')]),
                                       ('coisa', [('wand', 'varinha'), ('owl', 'coruja'), ('scarf', 'cachecol'), ('cloak', 'capa'), ('trunk', 'baú')])]),
              pg('É seu?', [('começo', [('Is this', 'Esta coisa é'), ('Is that', 'Aquela coisa é')]),
                            ('coisa', [('your wand', 'a sua varinha'), ('your scarf', 'o seu cachecol'), ('your owl', 'a sua coruja'), ('your cloak', 'a sua capa')])], ('?', '?'))],
        speak=[['Whose wand is this? It’s my wand.', 'De quem é esta varinha? É a minha varinha.'], ['Finders keepers! No way!', 'Achado não é roubado! De jeito nenhum!']],
        trap=[dict(ask='“Finders keepers!” quer dizer…', opts=['Procure o dono.', 'Quem acha, fica com o objeto.', 'Entregue ao diretor.'], a=1,
                   why='**Finders keepers!** = achado não é roubado (brincadeira).', say='Finders keepers!'),
              dict(ask='Qual frase está certa?', opts=['Who’s wand is this?', 'Whos wand is this?', 'Whose wand is this?'], a=2,
                   why='**Whose** = de quem. **Who’s** = quem é.', say='Whose wand is this?')],
        gap=[dict(text='___ owl is this?', pt='De quem é esta coruja?', opts=['Whose', 'Who’s', 'Who'], a=0, why='De quem é = **Whose**.', say='Whose owl is this?'),
             dict(text='___ way!', pt='De jeito nenhum!', opts=['No', 'Not', 'None'], a=0, why='**No way!** é a expressão.', say='No way!')],
        expq=[dict(ask='Você procura a sua capa que sumiu.', opts=['Watch out!', 'Lost and found', 'Finders keepers!'], a=1, why='**Lost and found** = achados e perdidos.'),
              dict(ask='Você acha uma moeda e quer ficar com ela, brincando.', opts=['Finders keepers!', 'Watch out!', 'No way!'], a=0, why='**Finders keepers!** = achado não é roubado!'),
              dict(ask='Um carro vem na sua direção. O que você grita?', opts=['Lost and found', 'No way!', 'Watch out!'], a=2, why='**Watch out!** = cuidado!')],
        missions=[mission('🧳', 'Achados e perdidos', 'Descubra o dono.',
                          'Você acha uma bolsa. **Pergunte de quem é com Whose…?, diga que não é sua e pergunte se é dele ou dela.**',
                          ['Whose…?'], 'Whose bag is this? It isn’t my bag. Is it his bag?',
                          ['Perguntei de quem é?', 'Disse que não é minha?', 'Usei his, her, your ou their?'],
                          ['\\bwhose \\w+ is (?:this|that|it)\\b', "\\b(?:it isn['’]t|it is not|this isn['’]t|that isn['’]t) my \\w+", '\\b(?:his|her|your|their) \\w+'],
                          [[['Whose bag is this?', 'De quem é esta bolsa?']], [['It isn’t my bag.', 'Não é a minha bolsa.']], [['Is it his bag?', 'É a bolsa dele?']]],
                          ['Pergunta certa! ❓', 'Não é minha! 🙅', 'De quem é? 🔍'],
                          ['Yes, it is his bag!', 'Sim, é a bolsa dele!']),
                  mission('🦉', 'A coruja do Harry', 'Defenda a sua coruja.',
                          'Uma coruja chegou à sala. **Diga que é a sua coruja, diga o nome dela com Her name is… e diga No way! se alguém quiser ficar com ela.**',
                          ['Her name is…'], 'It’s my owl. Her name is Hedwig. No way!',
                          ['Disse que é minha com It’s my…?', 'Disse o nome com Her name is?', 'Disse No way?'],
                          ["\\bit['’]?s my \\w+", '\\bher name is \\w+', '\\bno way\\b'],
                          [[['It’s my owl.', 'É a minha coruja.']], [['Her name is Hedwig.', 'O nome dela é Hedwig.']], [['No way!', 'De jeito nenhum!']]],
                          ['É sua! 🦉', 'Nome dado! 🏷️', 'Firme! 🙅'],
                          ['OK, OK. She is your owl!', 'Tá bom. Ela é a sua coruja!'])])
    CX = cx([('It is a magic stick. Wizards say a word and move it. It’s a ___.', 'É um bastão mágico. Os bruxos dizem uma palavra e o movem. É uma varinha.', ['wand', 'trunk', 'name']),
             ('It has big eyes and flies at night. Harry’s pet is a white ___.', 'Tem olhos grandes e voa à noite. O bichinho do Harry é uma coruja branca.', ['owl', 'scarf', 'cloak']),
             ('It’s winter and cold. I wear it around my neck. It’s a ___.', 'É inverno e faz frio. Eu uso no pescoço. É um cachecol.', ['scarf', 'wand', 'trunk']),
             ('It is a long, loose coat that wizards wear over their clothes. It’s a ___.', 'É um casaco longo e largo que os bruxos usam sobre a roupa. É uma capa.', ['cloak', 'owl', 'name']),
             ('I put my books and clothes in this big box to travel to school. It’s a ___.', 'Ponho meus livros e roupas nesta caixa grande para viajar para a escola. É um baú.', ['trunk', 'scarf', 'wand']),
             ('___ coat is this? It isn’t mine.', 'De quem é este casaco? Não é meu.', ['Whose', 'Who', 'Where'])])
    return dict(B=B, X=X, XT=XT, VB=VB, MR=MR, CX=CX)


EPS.append(ep107())


# ======================================================================= 108 · Finding Nemo
def ep108():
    NEM, DOR, GUL = 'e:🐠', 'e:🐟', 'e:🐦'
    L, H = lab(
        '-s final = z', 'Laboratório de sons: o “s” de his e yours',
        'His, hers, yours! O “s” no fim dessas palavras faz um zumbido, não um chiado.',
        'Em **his**, **hers**, **yours**, **ours** e **buzz**, o **s** final soa como **z**: a garganta vibra, como uma abelha.',
        'Ponha a mão na garganta. Se vibrar, é “z”. Em **hiss** (sibilo) o “s” é só ar, sem vibração.',
        'Em português, “s” final costuma ser chiado. Em inglês, depois de som sonoro, é **z**: **his** soa “RIZ”, não “RIS”. Cuidado: **his** ≠ **hiss**.',
        [['his', 'RIZ', 'dele', 'garganta vibrando no final'],
         ['yours', 'IÓRZ', 'seu, sua', 'termine com zumbido'],
         ['hers', 'RÂRZ', 'dela', 'o “rz” final vibra']],
        [['his', 'hiss', '“dele” × “sibilo”'], ['bus', 'buzz', '“ônibus” × “zumbido”'], ['peace', 'peas', '“paz” × “ervilhas”']],
        'Mão na garganta: se vibrar no final, o “z” está certo.',
        ['It’s his, not hers.', 'É dele, não dela.'],
        [rnd('his', ['his', 'hiss'], 0, '**His** termina com “z” vibrando. **Hiss** termina em “s” sem vibração.'),
         rnd('buzz', ['bus', 'buzz'], 1, '**Buzz** (zumbido) termina em “z”. **Bus** termina em “s”.'),
         rnd('peace', ['peace', 'peas'], 0, '**Peace** (paz) termina em “s”. **Peas** (ervilhas) termina em “z”.')],
        [hunt_t('peas', ['peace', 'peas'], 1, '**peas** termina em “z”.'),
         hunt_p('buzz', ['🐝', '🚌', '🕊️'], 0, '**buzz** = zumbido (abelha).'),
         hunt_t('hiss', ['his', 'hiss'], 1, '**hiss** termina em “s” sem vibração.'),
         hunt_t('bus', ['bus', 'buzz'], 0, '**bus** termina em “s”.'),
         hunt_p('bus', ['🐝', '🚌', '🕊️'], 1, '**bus** = ônibus.')])
    B = dict(
        title='Mine, Yours, His, Hers · pronomes possessivos',
        sub='Dizer de quem é sem repetir a coisa: It’s mine. Is it yours?',
        pattern_label='mine · yours · his · hers',
        why='Hoje você aprende a dizer de quem é uma coisa sem repetir o nome dela: It’s mine, Is it yours?, It’s his, It’s hers.',
        vocab=vocab([('Mine', 'Meu, minha', 'MÁIN'), ('Yours', 'Seu, sua', 'IÓRZ'), ('His', 'Dele', 'RIZ'), ('Hers', 'Dela', 'RÂRZ'),
                     ('Shell', 'Concha', 'SHÉL'), ('Bucket', 'Balde', 'BÂ-kit'), ('Hat', 'Chapéu', 'RÉT'), ('Fish', 'Peixe', 'FÍSH'),
                     ('Net', 'Rede', 'NÉT'), ('Mask', 'Máscara', 'MÉSK')]),
        balloons=[['🐚', 'shell'], ['🪣', 'bucket'], ['👒', 'hat'], ['🐠', 'fish'], ['🥅', 'net'], ['🤿', 'mask']],
        cover_art=dict(s='fishing', items=[['🐠', 104, 56, 20, 'bob'], ['🐚', 138, 44, 12, 'bob'], ['🐦', 84, 34, 12, 'bob']], seed='fn1'),
        cover_sub='mine, yours, his, hers. Em 10 minutos você diz “é meu!” como as gaivotas',
        cover_say='No porto, as gaivotas gritam “Mine! Mine!” para tudo. E você? Como dizer que algo é seu, dele ou dela, sem repetir a coisa?',
        wrap_recap=[['It’s mine!', 'É meu!'], ['Is it yours?', 'É seu?'], ['The hat is his.', 'O chapéu é dele.'],
                    ['The bucket is hers.', 'O balde é dela.']],
        teaser=dict(t='Peanuts', d='Próximo padrão: Revisão com be: perguntas, negativas e respostas curtas'),
        cast={'Nemo': ['🐠', '#F97316'], 'Dory': ['🐟', '#2563EB'], 'Gull': ['🐦', '#6B7280']},
        lines=[['Gull', 'Mine! Mine! Mine! This shell is mine!', 'Meu! Meu! Meu! Esta concha é minha!'],
               ['Nemo', 'No, it isn’t yours. It’s mine!', 'Não, não é sua. É minha!'],
               ['Dory', 'Wait. Is the shell really yours, Nemo?', 'Espere. A concha é mesmo sua, Nemo?'],
               ['Nemo', 'Yes! Look, my name is on it.', 'Sim! Olha, o meu nome está nela.'],
               ['Gull', 'OK, OK. Then the hat is mine.', 'Tá bom, tá bom. Então o chapéu é meu.'],
               ['Dory', 'Yes, the hat is yours. And the bucket is mine.', 'Sim, o chapéu é seu. E o balde é meu.'],
               ['Nemo', 'So the hat is his, and the bucket is hers!', 'Então o chapéu é dele e o balde é dela!'],
               ['Gull', 'And the fish? Mine, mine, mine!', 'E o peixe? Meu, meu, meu!']],
        quiz=[QZ('Whose is the shell?', 'De quem é a concha?', [['🐦', 'The Gull’s'], ['🐟', 'Dory’s'], ['🐠', 'Nemo’s']], 2, 3,
                 'Nemo diz: “my name is on it.”'),
              QZ('Whose is the hat?', 'De quem é o chapéu?', [['🐦', 'The Gull’s'], ['🐟', 'Dory’s'], ['🐠', 'Nemo’s']], 0, 5,
                 'Dory diz: “the hat is yours” (da Gaivota).'),
              QZ('Whose is the bucket?', 'De quem é o balde?', [['🐠', 'Nemo’s'], ['🐟', 'Dory’s'], ['🐦', 'The Gull’s']], 1, 5,
                 'Dory diz: “the bucket is mine.” Nemo conclui: hers.')],
        rdg_q=dict(q='A concha é minha. Qual frase está certa?',
                   o=['The shell is my.', 'The shell is me.', 'The shell is mine.'], a=2,
                   why='Sem o nome da coisa depois, use **mine**. Com a coisa, use **my shell**.'),
        dictate=[['The shell is mine.', 'A concha é minha.'], ['Is it yours?', 'É sua?'],
                 ['The hat is his.', 'O chapéu é dele.'], ['The bucket is hers.', 'O balde é dela.']],
        produce=produce(
            'Você e um amigo acham coisas na praia. **Diga que uma é sua com mine, pergunte se outra é do seu amigo com yours e diga que a terceira é dele ou dela.**',
            'Ex.: The shell is mine. Is the hat yours? The bucket is hers.',
            ['…is mine.', 'Is it yours?', 'It’s his / hers.'],
            'The shell is mine. Is the hat yours? The bucket is hers.',
            ['Disse que algo é meu com mine?', 'Perguntei se algo é do outro com yours?', 'Disse que algo é dele ou dela?'],
            ["\\b(?:is|it['’]s) mine\\b", '\\bis (?:it|the \\w+|this|that) yours\\b', "\\b(?:is|it['’]s) (?:his|hers)\\b"],
            [[['The shell is mine.', 'A concha é minha.'], ['It’s mine!', 'É meu!']],
             [['Is it yours?', 'É seu?'], ['Is the hat yours?', 'O chapéu é seu?']],
             [['The bucket is hers.', 'O balde é dela.'], ['It’s his.', 'É dele.']]],
            ['Meu! 🙋', 'Seu? 👉', 'Dele ou dela! 👦👧'],
            ['Yes, the hat is mine! Thank you!', 'Sim, o chapéu é meu! Obrigado!']),
        rs=RSD(['restaurant', 'mountain', 'bakery', 'stage', 'garden', 'library', 'farm', 'zoo', 'musicroom', 'harbor',
                'supermarket', 'snow', 'museum', 'playground', 'pool']),
        sc='harbor')
    X = dict(
        n=7010160, review=True, names=('Nemo', 'Dory'),
        stage=dict(rs='harbor', chars=[[NEM, 24, 0, 0.8], [DOR, 54, 1, 0.8], [GUL, 84, 1, 0.8]]),
        obra=dict(name='Finding Nemo', kind='🎬 Filme · 2003', year='2003',
                  text='Animação do estúdio Pixar, de 2003. O peixe-palhaço Marlin atravessa o oceano para achar o filho, Nemo, com a ajuda de Dory, uma peixe muito esquecida. No caminho aparecem tubarões, tartarugas e gaivotas que só sabem gritar “Mine!”.',
                  line=['Mine! Mine! Mine!', 'Meu! Meu! Meu! (as gaivotas)'],
                  pa=dict(t='underwater', e=['🐠', '🐟', '🌊'], p='a', v=1)),
        gancho=['Gull', 'Mine! Mine! Mine! This shell is mine!', 'Meu! Meu! Meu! Esta concha é minha!'],
        hot=hot([('🐚', 12, 18, 'shell', 'concha', 'The shell is mine.', 'A concha é minha.'),
                 ('🪣', 88, 16, 'bucket', 'balde', 'The bucket is hers.', 'O balde é dela.'),
                 ('👒', 14, 84, 'hat', 'chapéu', 'The hat is his.', 'O chapéu é dele.'),
                 ('🥅', 86, 84, 'net', 'rede', 'Is the net yours?', 'A rede é sua?'),
                 ('🤿', 50, 10, 'mask', 'máscara', 'The mask is theirs.', 'A máscara é deles.')]),
        gap=[G('The shell is ___. (minha)', 'A concha é minha.', ['my', 'mine', 'me'], 1, 'Sem a coisa depois, use **mine**.'),
             G('Is the net ___? (sua)', 'A rede é sua?', ['your', 'yours', 'you'], 1, 'No fim da frase: **yours**.'),
             G('The hat is ___. (dele)', 'O chapéu é dele.', ['he', 'hers', 'his'], 2, 'Dele: **his**.'),
             G('The bucket is ___. (dela)', 'O balde é dela.', ['hers', 'her', 'she'], 0, 'Sozinho no fim: **hers**. (her vem antes da coisa.)')],
        trap=[T(['It’s mine shell.', 'It’s mine.', 'It’s me.'], 1, 'Sem a coisa depois, diga **It’s mine.** Com a coisa: It’s **my** shell.'),
              T(['The hat is hers.', 'The hat is her’s.', 'The hat is hersh.'], 0, '**hers** não leva apóstrofo: The hat is **hers**.')],
        sticker=dict(title='Mine! Mine! Mine!', sub='Finding Nemo · 2003', rs='harbor', chars=sticker_chars(NEM, GUL)),
        speakers={'Nemo': NEM, 'Dory': DOR, 'Gull': GUL},
        rule=dict(who=DOR, head='mine · yours · his · hers', sub='Eles substituem my + coisa. Não leve a coisa junto.',
                  say=['The shell is mine. Is it yours?', 'A concha é minha. É sua?'],
                  pairsHead='🐚 my + coisa → pronome sozinho',
                  pairs=[dict(ico='🙋', a='my shell', b='<u>mine</u>', pta='minha concha', ptb='a minha', n=1),
                         dict(ico='👉', a='your hat', b='<u>yours</u>', pta='seu chapéu', ptb='o seu', n=1),
                         dict(ico='👦', a='his hat', b='<u>his</u>', pta='chapéu dele', ptb='o dele', n=1),
                         dict(ico='👧', a='her bucket', b='<u>hers</u>', pta='balde dela', ptb='o dela', n=1),
                         dict(ico='🧑‍🤝‍🧑', a='our net', b='<u>ours</u>', pta='nossa rede', ptb='a nossa', n=2),
                         dict(ico='👥', a='their shells', b='<u>theirs</u>', pta='conchas deles', ptb='as deles', n=2)],
                  uses=[dict(ico='🙋', tag='É meu', en='It’s mine!', pt='É meu!'),
                        dict(ico='👉', tag='Perguntar', en='Is it yours?', pt='É seu?'),
                        dict(ico='👦', tag='Dele', en='The hat is his.', pt='O chapéu é dele.'),
                        dict(ico='👧', tag='Dela', en='The bucket is hers.', pt='O balde é dela.')],
                  rules=[dict(tag='Sozinho', c=0, text='**mine, yours, his, hers** ficam sozinhos, sem a coisa depois.', ex='It’s my shell. → It’s mine.'),
                         dict(tag='Não repita a coisa', c=1, text='Nunca diga mine + coisa. Use my + coisa **ou** mine.', ex='✗ mine shell  →  ✓ my shell / mine'),
                         dict(tag='his e hers', c=3, text='**his** não muda. Já **her** vira **hers** quando fica sozinho.', ex='his hat → his · her bucket → hers')],
                  tips=['Em português “meu, minha, meus, minhas” mudam. Em inglês **mine** serve para tudo.']),
        mission_ic='🐚')
    XT = dict(
        exp=[exp('🎁', 'It’s all yours.', 'Expressão', 'É todo seu.', 'Quando você **entrega** algo a alguém: pode usar à vontade.',
                 'The net? It’s all yours.', 'A rede? É toda sua.'),
             exp('😤', 'That’s not fair!', 'Informal', 'Isso não é justo!', 'Quando você acha que algo é **injusto**.',
                 'That’s not fair! It’s my shell!', 'Isso não é justo! É a minha concha!'),
             exp('🤝', 'Sharing is caring.', 'Expressão', 'Compartilhar é cuidar.', 'Frase usada para pedir que as pessoas **dividam** o que têm.',
                 'Sharing is caring, Gull.', 'Compartilhar é cuidar, Gaivota.'),
             exp('🙌', 'Be my guest.', 'Expressão', 'Fique à vontade. / Pode usar.', 'Para **deixar** alguém usar algo ou fazer algo.',
                 'The bucket? Be my guest.', 'O balde? Fique à vontade.')],
        exp_scene=dict(rs='fishing', lines=[
            ['Nemo', '**That’s not fair**! The net is mine!', 'Isso não é justo! A rede é minha!'],
            ['Dory', 'Hey, **sharing is caring**, Nemo.', 'Ei, compartilhar é cuidar, Nemo.'],
            ['Nemo', 'OK. Take the net, Dory.', 'Tá bom. Pegue a rede, Dory.'],
            ['Dory', 'Thank you! Is it yours?', 'Obrigada! É sua mesmo?'],
            ['Nemo', 'Yes. **Be my guest**. **It’s all yours**.', 'Sim. Fique à vontade. É toda sua.'],
            ['Gull', 'Mine, mine, mine?', 'Meu, meu, meu?']]),
        lab=L, hunt=H)
    VB = vb('Verbos de dividir', 'Quatro verbos: share, lend, borrow e return.', [
        ('share', 'shares', '🤝', 'dividir, compartilhar', 'I share my hat.', 'Nemo share**s** his shell.', 'I share my bucket with you.', 'Eu divido meu balde com você.'),
        ('lend', 'lends', '📤', 'emprestar', 'I lend my net.', 'Dory lend**s** her net.', 'I lend you my hat.', 'Eu empresto meu chapéu a você.'),
        ('borrow', 'borrows', '📥', 'pegar emprestado', 'I borrow a mask.', 'The Gull borrow**s** a mask.', 'I borrow your bucket.', 'Eu pego seu balde emprestado.'),
        ('return', 'returns', '↩️', 'devolver', 'I return the shell.', 'She return**s** the shell.', 'I return your hat.', 'Eu devolvo o seu chapéu.')])
    MR = dict(
        mold=[pg('É de quem?', [('coisa', [('The shell is', 'A concha é'), ('The hat is', 'O chapéu é'), ('The bucket is', 'O balde é'), ('The net is', 'A rede é')]),
                                ('de quem', [('mine', 'meu / minha'), ('yours', 'seu / sua'), ('his', 'dele'), ('hers', 'dela')])]),
              pg('É seu?', [('coisa', [('Is the shell', 'A concha é'), ('Is the hat', 'O chapéu é'), ('Is the net', 'A rede é')]),
                            ('de quem', [('yours', 'sua / seu'), ('his', 'dele'), ('hers', 'dela')])], ('?', '?')),
              pg('Dizer de quem é', [('de quem', [('It’s mine', 'É meu'), ('It’s yours', 'É seu'), ('It’s his', 'É dele'), ('It’s hers', 'É dela'),
                                                  ('It’s ours', 'É nosso'), ('It’s theirs', 'É deles')])], ('!', '!'))],
        speak=[['The shell is mine. Is it yours?', 'A concha é minha. É sua?'], ['That’s not fair! Be my guest.', 'Isso não é justo! Fique à vontade.']],
        trap=[dict(ask='“It’s all yours.” quer dizer…', opts=['É tudo meu.', 'É tudo deles.', 'É todo seu.'], a=2,
                   why='**It’s all yours.** = é todo seu.', say='It’s all yours.'),
              dict(ask='Qual frase está certa?', opts=['It’s mine shell.', 'It’s mine.', 'It’s me.'], a=1,
                   why='Sozinho, sem a coisa: **It’s mine.**', say='It’s mine.')],
        gap=[dict(text='Be my ___.', pt='Fique à vontade.', opts=['guest', 'gust', 'guess'], a=0, why='**Be my guest.** é a expressão.', say='Be my guest.'),
             dict(text='That’s not ___!', pt='Isso não é justo!', opts=['far', 'fair', 'fear'], a=1, why='**fair** = justo.', say='That’s not fair!')],
        expq=[dict(ask='Seu amigo quer usar sua rede e você deixa.', opts=['That’s not fair!', 'Be my guest.', 'Sharing is caring.'], a=1, why='**Be my guest.** = pode usar.'),
              dict(ask='Alguém pegou algo seu sem pedir. Você reclama.', opts=['That’s not fair!', 'It’s all yours.', 'Be my guest.'], a=0, why='**That’s not fair!** = isso não é justo!'),
              dict(ask='Você pede para as crianças dividirem o brinquedo.', opts=['It’s all yours.', 'That’s not fair!', 'Sharing is caring.'], a=2, why='**Sharing is caring.** = compartilhar é cuidar.')],
        missions=[mission('🐚', 'Coisas da praia', 'Diga de quem é cada coisa.',
                          'Você e um amigo acham três coisas na praia. **Diga que uma é sua com mine, pergunte se outra é do amigo com yours e diga que a terceira é dele ou dela.**',
                          ['…is mine.'], 'The shell is mine. Is the hat yours? The bucket is hers.',
                          ['Disse que algo é meu com mine?', 'Perguntei se é do outro com yours?', 'Disse que algo é his ou hers?'],
                          ["\\b(?:is|it['’]s) mine\\b", '\\bis (?:it|the \\w+|this|that) yours\\b', "\\b(?:is|it['’]s) (?:his|hers)\\b"],
                          [[['It’s mine!', 'É meu!']], [['Is it yours?', 'É seu?']], [['It’s hers.', 'É dela.']]],
                          ['Meu! 🙋', 'Seu? 👉', 'Dela! 👧'],
                          ['Yes, the hat is mine!', 'Sim, o chapéu é meu!']),
                  mission('🤝', 'Dividir a rede', 'Use as expressões.',
                          'Seu amigo pegou a sua rede sem pedir. **Diga That’s not fair!, depois deixe com Be my guest e diga It’s all yours.**',
                          ['That’s not fair!'], 'That’s not fair! OK, be my guest. It’s all yours.',
                          ['Disse That’s not fair?', 'Disse Be my guest?', 'Disse It’s all yours?'],
                          ["\\bthat['’]?s not fair\\b", '\\bbe my guest\\b', "\\bit['’]?s all yours\\b"],
                          [[['That’s not fair!', 'Isso não é justo!']], [['Be my guest.', 'Fique à vontade.']], [['It’s all yours.', 'É todo seu.']]],
                          ['Justo! ⚖️', 'Gentil! 🙌', 'Dado! 🎁'],
                          ['Thanks! Sharing is caring!', 'Obrigado! Compartilhar é cuidar!'])])
    CX = cx([('I find it on the beach. It is hard and I hear the sea in it. It’s a ___.', 'Eu encontro na praia. É duro e ouço o mar nele. É uma concha.', ['shell', 'hat', 'net']),
             ('Kids carry sand and water in this to make a castle. It’s a ___.', 'As crianças levam areia e água nisto para fazer um castelo. É um balde.', ['bucket', 'mask', 'fish']),
             ('I wear it on my head under the sun. It’s a ___.', 'Uso na cabeça sob o sol. É um chapéu.', ['hat', 'bucket', 'net']),
             ('It lives in the sea and swims. Nemo is a ___.', 'Vive no mar e nada. O Nemo é um peixe.', ['fish', 'shell', 'hat']),
             ('Fishermen use it to catch fish. It’s a ___.', 'Pescadores usam para pegar peixes. É uma rede.', ['net', 'hat', 'mask']),
             ('A diver wears it on the face to see under the water. It’s a ___.', 'O mergulhador usa no rosto para ver embaixo d’água. É uma máscara.', ['mask', 'bucket', 'shell'])])
    return dict(B=B, X=X, XT=XT, VB=VB, MR=MR, CX=CX)


EPS.append(ep108())
