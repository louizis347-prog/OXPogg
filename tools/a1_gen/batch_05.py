# Lote 05: posições 38 a 45 do A1 (n = 70014, 910003, 9808, 7009808, 70015, 30008, 70016, 9809).
# TROCAS DE OBRA: pos 40: de The Wonderful Wizard of Oz (repetida do piloto 3) para Brown Bear, Brown Bear, What Do You See? (1967)
# TROCAS DE OBRA: pos 41: de The Wonderful Wizard of Oz (repetida do piloto 3) para Charlie and the Chocolate Factory (1964)
# Obras mantidas do brief: pos 38 The Happy Prince; 39 Mary Poppins; 42 Baa, Baa, Black Sheep; 43 The Purple Cow; 44 The Golden Touch; 45 Around the World in Eighty Days.
# Recortes afinados: 38 = so/very + elogios; 41 = "the red one" + Can I have…?; 42 = Can I try it on?; 44 = Paint it + cor.

KEYS = 'rdg pat vplay sbuild build order balloons dictate soundlab scene dquiz scenebuild produce review wrap'.split()


def RSD(*sc):
    return {k: sc[i % len(sc)] for i, k in enumerate(KEYS)}


def hot(e, x, y, en, pt, say, sayPt):
    return dict(e=e, x=x, y=y, en=en, pt=pt, say=say, sayPt=sayPt)


def gap(q, pt, opts, a, why):
    return dict(q=q, pt=pt, opts=opts, a=a, why=why)


def trap(opts, a, why, q='Qual frase está certa?'):
    return dict(q=q, opts=opts, a=a, why=why)


def quiz(q, pt, opts, a, line, why):
    return dict(q=q, pt=pt, opts=opts, a=a, line=line, why=why)


def exp(ic, en, tag, pt, use, ex):
    return dict(ic=ic, en=en, tag=tag, pt=pt, use=use, ex=ex)


def rnd(say, opts, a, why):
    return dict(fig='🎧', say=say, ask='Qual palavra você ouviu?', opts=opts, a=a, why=why)


def ht(say, opts, a, why):
    return dict(fig='🎧', say=say, ask='Ouça e toque na palavra.', opts=opts, a=a, why=why)


def hp(say, opts, a, why):
    return dict(fig='🎧', say=say, ask='Ouça e toque na figura.', opts=[[o, ''] for o in opts], a=a, why=why, pic=1)


def verb(v, ic, pt, f1, f2, ex, note):
    return dict(v=v, ic=ic, pt=pt, f=[['eu', f1], ['ele/ela', f2]], ex=ex, note=note)


def mold(label, slots, end=('.', '.')):
    return dict(label=label, slots=[dict(cat=c, opts=o) for c, o in slots], end=list(end))


def mtrap(ask, opts, a, why, say=None):
    d = dict(ask=ask, opts=opts, a=a, why=why)
    if say:
        d['say'] = say
    return d


def mgap(text, pt, opts, a, why, say):
    return dict(text=text, pt=pt, opts=opts, a=a, why=why, say=say)


def expq(ask, opts, a, why):
    return dict(ask=ask, opts=opts, a=a, why=why)


def mission(ic, name, desc, prompt, chips, model, check, kw, tips, ok, reply):
    return dict(ic=ic, name=name, desc=desc, data=dict(prompt=prompt, ph='Escreva a sua resposta aqui…', chips=chips, model=model,
                                                       check=check, kw=kw, tips=tips, ok=ok, reply=reply))


def produce(prompt, ph, chips, model, check, kw, tips, ok, reply):
    return dict(prompt=prompt, ph=ph, chips=chips, model=model, check=check, kw=kw, tips=tips, ok=ok, reply=reply)


def cx(*items):
    return [dict(text=t, pt=p, opts=o, a=0) for t, p, o in items]


# ============================================================ 38 · The Happy Prince
PRINCE = 'p:short:d4af37:e8c98a:d4af37:crown:suit'
BOY38 = 'p:cap:4a3728:f4c7a1:7f8c8d:none:shirt'


def ep38():
    B = dict(
        title='You Are So Kind · so e very',
        sub='Elogiar com You are so… e He is very… e dizer I’m proud of you',
        pattern_label='You are so… / very…',
        why='Hoje você aprende a elogiar como o Príncipe Feliz: You are so kind! He is very brave! I’m proud of you!',
        vocab=[['Kind', 'Gentil', 'Soa como “KÁIND”.'], ['Strong', 'Forte', 'Soa como “STRÓNG”.'], ['Brave', 'Corajoso(a)', 'Soa como “BRÊIV”.'],
               ['Proud', 'Orgulhoso(a)', 'Soa como “PRÁUD”.'], ['Prince', 'Príncipe', 'Soa como “PRÍNS”.'], ['Swallow', 'Andorinha', 'Soa como “SUÓ-lou”.']],
        balloons=[['💛', 'kind'], ['💪', 'strong'], ['🦁', 'brave'], ['🏅', 'proud'], ['🤴', 'prince'], ['🐦', 'swallow']],
        cover_art=dict(s='park', items=[['🤴', 104, 56, 20, 'bob'], ['🐦', 138, 44, 12, 'bob'], ['💛', 84, 34, 12, 'bob']], seed='hp1'),
        cover_sub='You are so kind! Em 10 minutos você elogia como o Príncipe Feliz',
        cover_say='Uma estátua dourada e uma pequena andorinha viram amigas. O Príncipe é muito gentil e a Andorinha é corajosa. Como elogiar alguém em inglês?',
        wrap_recap=[['You are so kind!', 'Você é tão gentil!'], ['He is very strong.', 'Ele é muito forte.'],
                    ['She is very brave.', 'Ela é muito corajosa.'], ["I'm proud of you!", 'Tenho orgulho de você!']],
        teaser=dict(t='Mary Poppins', d='Próximo padrão: Would you like…? Yes, please / No, thanks'),
        cast={'Prince': ['🤴', '#b8860b'], 'Swallow': ['🐦', '#2c5282'], 'Boy': ['👦', '#7f8c8d']},
        lines=[['Swallow', 'Hello! You are so tall, Prince!', 'Olá! Você é tão alto, Príncipe!'],
               ['Prince', 'Hello, little Swallow. You are very small!', 'Olá, pequena Andorinha. Você é muito pequena!'],
               ['Prince', 'Look! The boy is poor and hungry.', 'Olhe! O menino é pobre e está com fome.'],
               ['Prince', 'Take my gold to him, please.', 'Leve o meu ouro até ele, por favor.'],
               ['Swallow', "You are so kind, Prince! I'm strong. I'm ready.", 'Você é tão gentil, Príncipe! Eu sou forte. Estou pronta.'],
               ['Boy', 'Thank you! You are very kind, little bird.', 'Obrigado! Você é muito gentil, passarinho.'],
               ['Swallow', 'He is so happy now.', 'Ele está tão feliz agora.'],
               ['Prince', "You are brave, Swallow. I'm proud of you!", 'Você é corajosa, Andorinha. Tenho orgulho de você!']],
        quiz=[quiz('Who is very small?', 'Quem é muito pequeno?', [['🤴', 'The Prince'], ['👦', 'The boy'], ['🐦', 'The Swallow']], 2, 1, 'O Príncipe diz: “You are very small!”'),
              quiz('Who is poor and hungry?', 'Quem é pobre e está com fome?', [['👦', 'The boy'], ['🤴', 'The Prince'], ['🐦', 'The Swallow']], 0, 2, 'O Príncipe diz: “The boy is poor and hungry.”'),
              quiz('What is the Swallow?', 'O que é a Andorinha?', [['😴', 'Sleepy'], ['🦁', 'Brave'], ['😠', 'Angry']], 1, 7, 'O Príncipe diz: “You are brave, Swallow.”')],
        rdg_q=dict(q='Qual frase está certa para “Você é tão gentil”?', o=['You so kind.', 'You are kind so.', 'You are so kind.'], a=2,
                   why='Use o verbo **are** e ponha **so** antes do adjetivo: You **are** **so** kind.'),
        dictate=[['You are so kind!', 'Você é tão gentil!'], ['He is very brave.', 'Ele é muito corajoso.'], ["I'm proud of you.", 'Tenho orgulho de você.'],
                 ['The prince is very strong.', 'O príncipe é muito forte.']],
        produce=produce('Alguém ajudou você hoje. **Diga que a pessoa é gentil com You are so… ou very…, diga como você está com I’m e elogie outra pessoa com He is… ou She is….**',
                        'Ex.: You are so kind! I’m happy. He is very brave.', ['You are so…', "I'm…", 'He is very…'],
                        "You are so kind! I'm happy. He is very brave.",
                        ['Elogiei a pessoa com so ou very?', 'Disse como eu estou com I’m?', 'Elogiei outra pessoa com He is / She is?'],
                        [r"\byou(?:['’]re| are)\s+(?:so|very)\s+\w+", r"\bI(?:['’]m| am)\s+(?!not\b)\w+", r"\b(?:he|she)(?:['’]s| is)\s+(?:so |very )?(?:kind|strong|brave|proud|smart|nice|good|funny)\b"],
                        [[['You are so kind.', 'Você é tão gentil.'], ['You are very strong.', 'Você é muito forte.']],
                         [["I'm happy.", 'Estou feliz.'], ["I'm proud.", 'Estou orgulhoso.']],
                         [['He is very brave.', 'Ele é muito corajoso.'], ['She is so smart.', 'Ela é tão inteligente.']]],
                        ['Elogio com força! 💛', 'Você falou de si! 🙋', 'Elogio para outra pessoa! 🦁'],
                        ['Thank you! You are so kind too!', 'Obrigado! Você também é muito gentil!']),
        rs=RSD('park', 'street', 'park2', 'school', 'hall', 'lobby1', 'lake'),
        sc='park')
    X = dict(
        n=70014, review=True, names=('Prince', 'Swallow'),
        stage=dict(rs='park', chars=[[PRINCE, 28, 0, 1.0], ['e:🐦', 54, 1, 0.7], [BOY38, 82, 1, 0.9]]),
        obra=dict(name='The Happy Prince', kind='📖 Conto · 1888', year='1888',
                  text='Conto do escritor irlandês Oscar Wilde, de 1888. A estátua de um príncipe, coberta de ouro, pede a uma pequena andorinha que leve suas joias aos mais pobres da cidade. É uma história sobre bondade e amizade.',
                  line=['The Prince is kind.', 'O Príncipe é gentil. (frase do tema do conto)'],
                  pa=dict(t='plaza', e=['🤴', '🐦', '💛'], p='e', v=0)),
        gancho=['Swallow', 'Hello! You are so tall, Prince!', 'Olá! Você é tão alto, Príncipe!'],
        hot=[hot('👑', 14, 16, 'prince', 'príncipe', 'The prince is very kind.', 'O príncipe é muito gentil.'),
             hot('💪', 40, 14, 'strong', 'forte', 'He is very strong.', 'Ele é muito forte.'),
             hot('🦁', 66, 14, 'brave', 'corajoso', 'You are so brave!', 'Você é tão corajoso!'),
             hot('🏅', 88, 16, 'proud', 'orgulhoso', "I'm proud of you!", 'Tenho orgulho de você!'),
             hot('🐦', 12, 82, 'swallow', 'andorinha', 'The swallow is small.', 'A andorinha é pequena.')],
        gap=[gap('You ___ so kind!', 'Você é tão gentil!', ['is', 'are', 'am'], 1, 'Com **you**, o verbo é **are**: You **are** so kind.'),
             gap('He is ___ strong.', 'Ele é muito forte.', ['very', 'are', 'much'], 0, '**very** (muito) vem antes do adjetivo: He is **very** strong.'),
             gap("I'm proud ___ you.", 'Tenho orgulho de você.', ['at', 'to', 'of'], 2, 'Orgulho **de** alguém: proud **of**.'),
             gap('She ___ very brave.', 'Ela é muito corajosa.', ['are', 'is', 'am'], 1, 'Com **she**, o verbo é **is**.')],
        trap=[trap(['You is so kind.', 'You are so kind.', 'You are kind so.'], 1, 'Com **you** use **are**, e **so** vem antes do adjetivo.'),
              trap(['He very is strong.', 'He strong is very.', 'He is very strong.'], 2, 'Ordem certa: He **is** **very** strong.')],
        sticker=dict(title='O Príncipe e a Andorinha', sub='The Happy Prince · 1888', rs='park', chars=[[PRINCE, 32, 0, 1.0], ['e:🐦', 66, 1, 0.7]]),
        speakers={'Prince': PRINCE, 'Swallow': 'e:🐦', 'Boy': BOY38},
        rule=dict(
            who=PRINCE, head='so · very', sub='Dê força ao adjetivo: so e very vêm antes dele.',
            say=['You are so kind!', 'Você é tão gentil!'],
            formula=[dict(from_=[['You', 0], ['are', 1], ['kind.', 3]], to=[['You', 0], ['are', 1], ['so', 2], ['kind!', 3]], say='You are so kind!',
                          note='Ponha **so** antes do adjetivo: fica mais forte, como “tão gentil”.'),
                     dict(from_=[['He', 0], ['is', 1], ['brave.', 3]], to=[['He', 0], ['is', 1], ['very', 2], ['brave.', 3]], say='He is very brave.',
                          note='**very** = muito. Também vem antes do adjetivo, nunca depois.'),
                     dict(from_=[['I', 0], ['am', 1], ['proud.', 3]], to=[["I'm", 2], ['proud', 3], ['of you!', 0]], say="I'm proud of you!",
                          note='Orgulho **de** alguém: **proud of** + pessoa.')],
            uses=[dict(ico='💛', tag='Elogiar', en='You are so kind!', pt='Você é tão gentil!'),
                  dict(ico='💪', tag='Falar de outro', en='He is very strong.', pt='Ele é muito forte.'),
                  dict(ico='🦁', tag='Falar de outra', en='She is very brave.', pt='Ela é muito corajosa.'),
                  dict(ico='🏅', tag='Orgulho', en="I'm proud of you.", pt='Tenho orgulho de você.')],
            rules=[dict(tag='so / very', c=0, text='Vêm **antes** do adjetivo: so kind, very strong.', ex='You are so kind. He is very strong.'),
                   dict(tag='proud of', c=2, text='Em inglês é **proud of**, não “proud with”.', ex='✗ proud with you  →  ✓ proud of you'),
                   dict(tag='Com verbo', c=1, text='Não esqueça o verbo **be**: am, is, are.', ex='✗ You so kind  →  ✓ You are so kind')],
            tips=['Em português também dizemos “tão” e “muito” antes do adjetivo. A diferença é o **verbo**: em inglês ele é obrigatório (You **are** so kind).']),
        mission_ic='💛')
    XT = dict(
        exp=[exp('🥹', "I'm proud of you!", 'Expressão', 'Tenho orgulho de você!', 'Quando alguém **conquistou** algo ou foi muito corajoso.', ["I'm proud of you, Swallow!", 'Tenho orgulho de você, Andorinha!']),
             exp('👏', 'Good job!', 'Informal', 'Bom trabalho!', 'Para **parabenizar** alguém por algo bem feito.', ['Good job, little bird!', 'Bom trabalho, passarinho!']),
             exp('🙏', "That's so kind of you!", 'Expressão', 'Que gentileza a sua!', 'Quando alguém faz algo **gentil** por você.', ["That's so kind of you!", 'Que gentileza a sua!']),
             exp('🎉', 'Way to go!', 'Gíria', 'Mandou bem!', 'Para **comemorar** uma conquista. É bem informal.', ['Way to go, Swallow!', 'Mandou bem, Andorinha!'])],
        exp_scene=dict(rs='park2', lines=[
            ['Boy', "Wow, bread! **That's so kind of you**!", 'Uau, pão! Que gentileza a sua!'],
            ['Swallow', '**Good job**, Prince! You help a lot.', 'Bom trabalho, Príncipe! Você ajuda muito.'],
            ['Prince', '**Way to go**, Swallow! You are fast!', 'Mandou bem, Andorinha! Você é rápida!'],
            ['Swallow', "I'm strong and brave.", 'Sou forte e corajosa.'],
            ['Prince', "**I'm proud of you**!", 'Tenho orgulho de você!'],
            ['Boy', 'Me too! Thank you both.', 'Eu também! Obrigado aos dois.']]),
        lab=dict(
            short='s + consoante', title='Laboratório de sons: s + consoante',
            say='Em inglês, palavras como school e strong começam direto com “s”. Não coloque um “i” antes!',
            intro=dict(what='Em **school**, **strong** e **smart**, o **s** vem colado na consoante: SKUL, STRONG, SMART.',
                       how='Comece com um “sss” longo e só depois solte a consoante, sem nenhuma vogal no começo.',
                       pt='Em português é comum dizer “iscool” ou “istrong”, mas em inglês não existe esse “i” inicial. Cuidado: **stop** (parar) ≠ **top** (topo).'),
            ex=[['school', 'SKÚL', 'escola', 'sss e k colados, sem “i”'], ['strong', 'STRÓNG', 'forte', 'sss-t-r sem vogal antes'], ['smart', 'SMÁRT', 'inteligente', 'sss-m sem vogal antes']],
            pairs=[['stop', 'top', '“parar” × “topo”: em stop há um sss antes'], ['spin', 'pin', '“girar” × “alfinete”'], ['slow', 'low', '“devagar” × “baixo”']],
            tip='Segure o “sss” por um segundo antes da consoante. Não diga “i” antes!',
            phrase=['She is a strong, smart student.', 'Ela é uma aluna forte e esperta.'],
            rounds=[rnd('stop', ['stop', 'top'], 0, '**Stop** começa com “sss” colado no “t”. **Top** começa direto com “t”.'),
                    rnd('pin', ['spin', 'pin'], 1, '**Pin** (alfinete) não tem o “sss” no começo. **Spin** (girar) tem.'),
                    rnd('low', ['slow', 'low'], 1, '**Low** (baixo) começa em “l”. **Slow** (devagar) tem “sss” antes.')]),
        hunt=[ht('top', ['stop', 'top'], 1, '**top** = topo, sem “sss” no começo.'), ht('spin', ['spin', 'pin'], 0, '**spin** = girar, com “sss” colado no “p”.'),
              hp('star', ['⭐', '🍔', '🦴'], 0, '**star** = estrela, começa com “st”.'), ht('slow', ['slow', 'low'], 0, '**slow** = devagar, com “sss” antes do “l”.')])
    VB = dict(title='Verbos para ajudar como o Príncipe', tip='Quatro verbos: help, give, fly e carry.', items=[
        verb('help', '🤝', 'ajudar', 'I help the boy.', 'The Prince help**s** the poor.', ['I help the boy.', 'Eu ajudo o menino.'], '**help** = ajudar. Com he/she: **helps**.'),
        verb('give', '🎁', 'dar', 'I give gold to the boy.', 'He give**s** gold to the poor.', ['I give gold to the boy.', 'Eu dou ouro ao menino.'], '**give** = dar. Com he/she: **gives**.'),
        verb('fly', '🕊️', 'voar', 'I fly to the city.', 'The Swallow fl**ies** fast.', ['I fly to the city.', 'Eu voo para a cidade.'], '**fly** = voar. Com he/she: **flies** (y vira ies).'),
        verb('carry', '🎒', 'carregar, levar', 'I carry a red stone.', 'She carr**ies** the stone.', ['I carry a red stone.', 'Eu levo uma pedra vermelha.'], '**carry** = carregar. Com he/she: **carries** (y vira ies).')])
    MR = dict(
        mold=[mold('Elogiar com so ou very', [('quem', [['You are', 'você é']]), ('força', [['so', 'tão'], ['very', 'muito']]),
                                              ('qualidade', [['kind', 'gentil'], ['strong', 'forte'], ['brave', 'corajoso(a)'], ['smart', 'inteligente'], ['nice', 'legal']])], ('!', '!')),
              mold('Falar de outra pessoa', [('quem', [['He is', 'ele é'], ['She is', 'ela é']]), ('força', [['so', 'tão'], ['very', 'muito']]),
                                             ('qualidade', [['kind', 'gentil'], ['strong', 'forte'], ['brave', 'corajoso(a)'], ['funny', 'engraçado(a)']])]),
              mold('Ter orgulho', [('frase', [["I'm proud of", 'tenho orgulho de']]), ('quem', [['you', 'você'], ['him', 'ele'], ['her', 'ela']])], ('!', '!'))],
        speak=[['You are so kind! Thank you.', 'Você é tão gentil! Obrigado.'], ["I'm proud of him. He is very brave.", 'Tenho orgulho dele. Ele é muito corajoso.']],
        trap=[mtrap('“Good job!” quer dizer…', ['Bom trabalho!', 'Bom dia!', 'Boa viagem!'], 0, '**Good job!** = bom trabalho!', 'Good job!'),
              mtrap('Qual frase está certa?', ['I proud of you.', "I'm proud of you.", "I'm proud you."], 1, 'Use **I’m proud of you.**', "I'm proud of you.")],
        gap=[mgap("I'm proud ___ you!", 'Tenho orgulho de você!', ['of', 'in', 'for'], 0, 'Orgulho **de** alguém: proud **of**.', "I'm proud of you!"),
             mgap('You are ___ kind!', 'Você é tão gentil!', ['so', 'do', 'is'], 0, '**so** vem antes do adjetivo.', 'You are so kind!')],
        expq=[expq('Seu amigo ganhou uma medalha. O que você diz?', ['Hurry up!', 'Good job!', 'Sorry!'], 1, '**Good job!** = bom trabalho!'),
              expq('Alguém carregou suas malas e você agradece.', ["That's so kind of you!", 'Way to go!', 'See you!'], 0, "**That's so kind of you!** agradece uma gentileza."),
              expq('Seu irmão venceu a corrida. Você comemora.', ["I'm full.", 'Take it easy.', 'Way to go!'], 2, '**Way to go!** = mandou bem!')],
        missions=[mission('💛', 'Obrigado, amigo!', 'Agradeça e elogie.', 'Seu amigo ajudou você com a mochila. **Agradeça, diga que ele é gentil (so ou very) e diga que você está feliz.**', ['Thank you!'],
                          "Thank you! You are so kind. I'm happy.", ['Agradeci?', 'Disse que ele é gentil com so ou very?', 'Disse como eu estou?'],
                          [r'\bthank(?:s| you)\b', r"\byou(?:['’]re| are)\s+(?:so|very)\s+\w+", r"\bI(?:['’]m| am)\s+(?!not\b)\w+"],
                          [[['Thank you!', 'Obrigado!']], [['You are so kind.', 'Você é tão gentil.']], [["I'm happy.", 'Estou feliz.']]],
                          ['Educação! 🙏', 'Elogio certo! 💛', 'Você falou de si! 🙋'], ["You're welcome! Let's go!", 'De nada! Vamos!']),
                  mission('🏅', 'Orgulho da irmã', 'Parabenize alguém.', 'Sua irmã ganhou um jogo. **Diga Good job, diga que você tem orgulho dela (I’m proud of her) e que ela é muito inteligente ou forte.**', ['Good job!'],
                          "Good job! I'm proud of her. She is very smart.", ['Disse Good job?', 'Disse que tenho orgulho dela?', 'Elogiei com She is…?'],
                          [r'\bgood job\b', r'\bproud of (?:her|him|you)\b', r"\b(?:she|he)(?:['’]s| is)\s+(?:so |very )?(?:strong|smart|brave|kind)\b"],
                          [[['Good job!', 'Bom trabalho!']], [["I'm proud of her.", 'Tenho orgulho dela.']], [['She is very smart.', 'Ela é muito inteligente.']]],
                          ['Parabéns! 👏', 'Orgulho! 🏅', 'Elogio certo! 💪'], ['Thank you! I practice a lot!', 'Obrigada! Eu treino muito!'])])
    CXs = cx(('She gives food to poor people and always helps. She is very ___.', 'Ela dá comida a quem é pobre e sempre ajuda. Ela é muito gentil.', ['kind', 'proud', 'swallow']),
             ('He lifts the heavy box with one hand. He is ___.', 'Ele levanta a caixa pesada com uma mão. Ele é forte.', ['strong', 'brave', 'prince']),
             ('The firefighter goes into the fire to save a cat. He is ___.', 'O bombeiro entra no fogo para salvar um gato. Ele é corajoso.', ['brave', 'kind', 'strong']),
             ('My son wins the first prize. I am ___ of him.', 'Meu filho ganha o primeiro prêmio. Tenho orgulho dele.', ['proud', 'kind', 'prince']),
             ('He lives in a castle and his father is the king. He is a ___.', 'Ele mora num castelo e o pai dele é o rei. Ele é um príncipe.', ['prince', 'swallow', 'proud']),
             ('It is a small bird with long wings. It flies fast. It is a ___.', 'É um pássaro pequeno de asas longas. Voa rápido. É uma andorinha.', ['swallow', 'prince', 'brave']))
    return dict(B=B, X=X, XT=XT, VB=VB, MR=MR, CX=CXs)


# ============================================================ 39 · Mary Poppins
MARY = 'p:bun:2b1b17:f4c7a1:1f3a5f:hat:dress'
BERT = 'p:cap:3e2723:e8b48a:37474f:none:shirt'
MICHAEL = 'p:short:5d4037:f4c7a1:c0392b:none:shirt'


def ep39():
    B = dict(
        title='Yes, Please! No, Thanks! · Would you like…?',
        sub='Oferecer, aceitar e recusar com educação',
        pattern_label='Would you like…?',
        why='Hoje você aprende a oferecer algo como a Mary Poppins: Would you like some tea? E a responder com Yes, please! ou No, thanks.',
        vocab=[['Tea', 'Chá', 'Soa como “TÍ”.'], ['Cookie', 'Biscoito', 'Soa como “KÚ-ki”.'], ['Cake', 'Bolo', 'Soa como “KÊIK”.'],
               ['Sandwich', 'Sanduíche', 'Soa como “SÉN-uitch”.'], ['Juice', 'Suco', 'Soa como “DJÚS”.'], ['Apple', 'Maçã', 'Soa como “É-pol”.']],
        balloons=[['🍵', 'tea'], ['🍪', 'cookie'], ['🍰', 'cake'], ['🥪', 'sandwich'], ['🧃', 'juice'], ['🍎', 'apple']],
        cover_art=dict(s='kitchen', items=[['🍵', 104, 56, 20, 'bob'], ['🍰', 138, 44, 12, 'bob'], ['🌂', 84, 34, 12, 'bob']], seed='mp1'),
        cover_sub='Would you like…? Em 10 minutos você oferece e aceita como na hora do chá',
        cover_say='A babá Mary Poppins serve o chá para as crianças e para o amigo Bert. Como oferecer algo com educação? E como dizer sim ou não?',
        wrap_recap=[['Would you like some tea?', 'Você quer um pouco de chá?'], ['Yes, please!', 'Sim, por favor!'], ['No, thanks.', 'Não, obrigado.'], ['Would you like a cookie?', 'Você quer um biscoito?']],
        teaser=dict(t='Brown Bear, Brown Bear, What Do You See?', d='Próximo padrão: What’s this? It’s a… e as cores'),
        cast={'Mary': ['🌂', '#1f3a5f'], 'Bert': ['🧹', '#37474f'], 'Michael': ['👦', '#c0392b']},
        lines=[['Mary', 'Good morning, Michael. Would you like some tea?', 'Bom dia, Michael. Você quer um pouco de chá?'],
               ['Michael', 'Yes, please! I love tea.', 'Sim, por favor! Eu adoro chá.'],
               ['Mary', 'Here you are. Bert, would you like a sandwich?', 'Aqui está. Bert, você quer um sanduíche?'],
               ['Bert', "No, thanks. I'm not hungry.", 'Não, obrigado. Não estou com fome.'],
               ['Mary', 'Would you like some cake, then?', 'Então, você quer um pouco de bolo?'],
               ['Bert', 'Yes, please! Cake is my favorite.', 'Sim, por favor! Bolo é o meu favorito.'],
               ['Michael', 'Mary, would you like a cookie?', 'Mary, você quer um biscoito?'],
               ['Mary', 'No, thanks. Just tea for me.', 'Não, obrigada. Só chá para mim.']],
        quiz=[quiz('Who says no to the sandwich?', 'Quem recusa o sanduíche?', [['🌂', 'Mary'], ['👦', 'Michael'], ['🧹', 'Bert']], 2, 3, 'Bert diz: “No, thanks.”'),
              quiz('What does Bert want?', 'O que o Bert quer?', [['🍵', 'Tea'], ['🍰', 'Cake'], ['🥪', 'Sandwich']], 1, 5, 'Bert diz: “Yes, please! Cake is my favorite.”'),
              quiz('What does Mary want?', 'O que a Mary quer?', [['🍵', 'Tea'], ['🍪', 'A cookie'], ['🍰', 'Cake']], 0, 7, 'Mary diz: “Just tea for me.”')],
        rdg_q=dict(q='Alguém oferece bolo e você não quer. Qual resposta educada está certa?', o=['No, please.', 'No, thanks.', 'Not thanks.'], a=1,
                   why='Para recusar com educação: **No, thanks.** “No, please” não se usa.'),
        dictate=[['Would you like some tea?', 'Você quer um pouco de chá?'], ['Yes, please!', 'Sim, por favor!'], ['No, thanks.', 'Não, obrigado.'], ['Would you like a cookie?', 'Você quer um biscoito?']],
        produce=produce('A Mary pergunta: *Would you like some tea? Would you like a cookie?* **Aceite uma oferta com Yes, please, recuse outra com No, thanks e ofereça algo a ela com Would you like…?**',
                        "Ex.: Yes, please! No, thanks, I'm full. Would you like a sandwich?", ['Yes, please!', 'No, thanks.', 'Would you like…?'],
                        "Yes, please! I love tea. No, thanks, I'm full. Would you like a sandwich, Mary?",
                        ['Aceitei com Yes, please?', 'Recusei com No, thanks?', 'Ofereci algo com Would you like…?'],
                        [r'\byes,?\s*please\b', r'\bno,?\s*thank(?:s| you)\b', r'\bwould you like\b[^.!?]*\?'],
                        [[['Yes, please!', 'Sim, por favor!']], [['No, thanks.', 'Não, obrigado.'], ["No, thanks. I'm full.", 'Não, obrigado. Estou satisfeito.']],
                         [['Would you like a sandwich?', 'Você quer um sanduíche?'], ['Would you like some juice?', 'Você quer um pouco de suco?']]],
                        ['Aceitou com educação! ✅', 'Recusou com educação! 🙅', 'Boa oferta! 🍪'],
                        ['No, thank you. Just tea for me!', 'Não, obrigada. Só chá para mim!']),
        rs=RSD('kitchen', 'living', 'cafe3', 'home1', 'bedroom', 'cafe2', 'yard'),
        sc='kitchen')
    X = dict(
        n=910003, review=True, names=('Mary', 'Michael'),
        stage=dict(rs='kitchen', chars=[[MARY, 28, 0, 1.0], [BERT, 56, 1, 1.0], [MICHAEL, 82, 1, 0.8]]),
        obra=dict(name='Mary Poppins', kind='🎬 Filme · 1964', year='1964',
                  text='Musical da Disney de 1964, estrelado por Julie Andrews, baseado nos livros de P. L. Travers. A babá Mary Poppins chega à casa da família Banks, enche as crianças de magia e canta sobre uma colher de açúcar.',
                  line=['Supercalifragilisticexpialidocious!', 'Palavra inventada da música famosa do filme.'],
                  pa=dict(t='attic', e=['🌂', '🍵', '🎩'], p='b', v=1)),
        gancho=['Mary', 'Good morning, Michael. Would you like some tea?', 'Bom dia, Michael. Você quer um pouco de chá?'],
        hot=[hot('🍵', 14, 16, 'tea', 'chá', 'Would you like some tea?', 'Você quer um pouco de chá?'),
             hot('🍪', 40, 14, 'cookie', 'biscoito', 'Would you like a cookie?', 'Você quer um biscoito?'),
             hot('🍰', 66, 14, 'cake', 'bolo', 'Would you like some cake?', 'Você quer um pouco de bolo?'),
             hot('🥪', 88, 16, 'sandwich', 'sanduíche', 'Would you like a sandwich?', 'Você quer um sanduíche?'),
             hot('🍎', 12, 82, 'apple', 'maçã', 'Would you like an apple?', 'Você quer uma maçã?')],
        gap=[gap('___ you like some tea?', 'Você quer um pouco de chá?', ['Do', 'Would', 'Are'], 1, 'Para oferecer com educação: **Would** you like…?'),
             gap('Yes, ___!', 'Sim, por favor!', ['sorry', 'no', 'please'], 2, 'Para aceitar: Yes, **please**!'),
             gap("No, ___. I'm full.", 'Não, obrigado. Estou satisfeito.', ['thanks', 'hello', 'welcome'], 0, 'Para recusar: No, **thanks**.'),
             gap('Would you like ___ apple?', 'Você quer uma maçã?', ['a', 'an', 'two'], 1, '**an** antes de som de vogal: an apple.')],
        trap=[trap(['You would like some tea?', 'Would you like some tea?', 'Would you likes some tea?'], 1, 'O **Would** vem na frente e o verbo **like** não leva -s.'),
              trap(['Yes, I want.', 'Yes, I would please.', 'Yes, please!'], 2, 'Para aceitar uma oferta, o jeito natural é **Yes, please!**')],
        sticker=dict(title='Mary Poppins e o chá', sub='Mary Poppins · 1964', rs='kitchen', chars=[[MARY, 34, 0, 1.0], [MICHAEL, 68, 1, 0.8]]),
        speakers={'Mary': MARY, 'Bert': BERT, 'Michael': MICHAEL},
        rule=dict(
            who=MARY, head='Would you like…?', sub='Oferecer com educação, aceitar e recusar.',
            say=['Would you like some tea?', 'Você quer um pouco de chá?'],
            formula=[dict(from_=[['You', 0], ['like', 2], ['some tea.', 3]], to=[['Would', 1], ['you', 0], ['like', 2], ['some tea?', 3]], say='Would you like some tea?',
                          note='**Would** vem na frente. O verbo **like** não muda e não leva -s.'),
                     dict(from_=[['Would you like a cookie?', 3]], to=[['Yes, please!', 2]], say='Yes, please!', note='Para **aceitar**: Yes, please!'),
                     dict(from_=[['Would you like a sandwich?', 3]], to=[['No, thanks.', 1]], say='No, thanks.', note='Para **recusar**: No, thanks. Pode explicar: I’m full.')],
            uses=[dict(ico='🍵', tag='Oferecer', en='Would you like some tea?', pt='Você quer um pouco de chá?'),
                  dict(ico='✅', tag='Aceitar', en='Yes, please!', pt='Sim, por favor!'),
                  dict(ico='❌', tag='Recusar', en='No, thanks.', pt='Não, obrigado.'),
                  dict(ico='😋', tag='Explicar', en="No, thanks. I'm full.", pt='Não, obrigado. Estou satisfeito.')],
            rules=[dict(tag='Would you like', c=0, text='Oferta educada: **Would you like + algo?**', ex='Would you like some cake?'),
                   dict(tag='some / a / an', c=3, text='**some** para bebida e quantidade (some tea, some cake). **a / an** para uma unidade.', ex='a cookie · an apple · some juice'),
                   dict(tag='Yes, please', c=2, text='Aceite com **please** e recuse com **thanks**.', ex='✗ Yes, I want.  →  ✓ Yes, please!')],
            tips=['Em português dizemos “Aceita um chá?” e a resposta pode ser só “sim”. Em inglês, responder só “Yes” soa seco: acrescente **please**.']),
        mission_ic='🍵')
    XT = dict(
        exp=[exp('🍽️', 'Help yourself!', 'Expressão', 'Fique à vontade! / Sirva-se!', 'Quando você oferece comida e a pessoa pode **se servir**.', ['Help yourself, Michael!', 'Sirva-se, Michael!']),
             exp('😋', "I'm full.", 'Expressão', 'Estou satisfeito.', 'Para dizer que **já comeu o bastante**.', ["No, thanks. I'm full.", 'Não, obrigado. Estou satisfeito.']),
             exp('💸', 'My treat!', 'Informal', 'É por minha conta!', 'Quando **você paga** pelo outro.', ['Tea for everyone. My treat!', 'Chá para todos. É por minha conta!']),
             exp('🕐', 'Maybe later.', 'Expressão', 'Talvez mais tarde.', 'Jeito educado de **adiar** um sim.', ['Cake? Maybe later, thanks.', 'Bolo? Talvez mais tarde, obrigada.'])],
        exp_scene=dict(rs='cafe3', lines=[
            ['Bert', 'Hello! **My treat** today! Tea for everyone.', 'Olá! Hoje é por minha conta! Chá para todos.'],
            ['Michael', 'Wow! Can I have a cookie?', 'Uau! Posso pegar um biscoito?'],
            ['Mary', '**Help yourself**, Michael.', 'Fique à vontade, Michael.'],
            ['Bert', 'Would you like some cake, Mary?', 'Você quer um pouco de bolo, Mary?'],
            ['Mary', '**Maybe later**. **I\'m full**, thanks.', 'Talvez mais tarde. Estou satisfeita, obrigada.'],
            ['Michael', 'More cookies for me!', 'Mais biscoitos para mim!']]),
        lab=dict(
            short='h aspirado', title='Laboratório de sons: o “h” do inglês',
            say='Em inglês, o “h” no começo da palavra sai como um sopro de ar. Em português ele é mudo!',
            intro=dict(what='O **h** de **hello**, **have** e **hot** é um sopro leve, como quando você embaça um vidro.',
                       how='Abra a boca, solte um sopro de ar da garganta e depois diga a vogal: “HHÉ-lou”. Não precisa raspar a garganta.',
                       pt='Em português o “h” é mudo (hora, homem). Em inglês ele existe! Se você o esquecer, **heat** (calor) vira **eat** (comer).'),
            ex=[['hello', 'HHÉ-lou', 'olá', 'comece com um sopro de ar'], ['have', 'HÉV', 'ter', 'sopro e depois a vogal'], ['hot', 'HÓT', 'quente', 'sopre antes do “o”']],
            pairs=[['eat', 'heat', '“comer” × “calor”: em heat há um sopro no começo'], ['air', 'hair', '“ar” × “cabelo”'], ['old', 'hold', '“velho” × “segurar”']],
            tip='Coloque a mão na frente da boca: no “h” você sente o ar quente na palma da mão.',
            phrase=['Have some hot tea, Mary.', 'Tome um pouco de chá quente, Mary.'],
            rounds=[rnd('heat', ['eat', 'heat'], 1, '**Heat** (calor) começa com o sopro do “h”. **Eat** começa direto na vogal.'),
                    rnd('air', ['air', 'hair'], 0, '**Air** (ar) começa direto na vogal. **Hair** (cabelo) começa com sopro.'),
                    rnd('hold', ['old', 'hold'], 1, '**Hold** (segurar) começa com o sopro do “h”. **Old** (velho) não.')]),
        hunt=[ht('hair', ['air', 'hair'], 1, '**hair** = cabelo, com sopro de “h”.'), ht('eat', ['eat', 'heat'], 0, '**eat** = comer, sem sopro no começo.'),
              hp('hat', ['👒', '🍰', '🚪'], 0, '**hat** = chapéu, começa com sopro de “h”.'), ht('old', ['old', 'hold'], 0, '**old** = velho, sem “h”.')])
    VB = dict(title='Verbos para a hora do chá', tip='Quatro verbos: offer, pour, accept e share.', items=[
        verb('offer', '🎁', 'oferecer', 'I offer a cookie.', 'Mary offer**s** some tea.', ['I offer a cookie.', 'Eu ofereço um biscoito.'], '**offer** = oferecer. Com he/she: **offers**.'),
        verb('pour', '🫖', 'servir (líquido)', 'I pour the tea.', 'Bert pour**s** the juice.', ['I pour the tea.', 'Eu sirvo o chá.'], '**pour** = servir (um líquido). Com he/she: **pours**.'),
        verb('accept', '✅', 'aceitar', 'I accept the cake.', 'She accept**s** the tea.', ['I accept the cake.', 'Eu aceito o bolo.'], '**accept** = aceitar. Com he/she: **accepts**.'),
        verb('share', '🤝', 'dividir', 'I share my cookie.', 'He share**s** the sandwich.', ['I share my cookie.', 'Eu divido o meu biscoito.'], '**share** = dividir, compartilhar. Com he/she: **shares**.')])
    MR = dict(
        mold=[mold('Oferecer algo', [('oferta', [['Would you like', 'você quer']]), ('o quê', [['some tea', 'um pouco de chá'], ['some juice', 'um pouco de suco'], ['some cake', 'um pouco de bolo'], ['a cookie', 'um biscoito'], ['a sandwich', 'um sanduíche'], ['an apple', 'uma maçã']])], ('?', '?')),
              mold('Responder à oferta', [('sim ou não', [['Yes,', 'sim,'], ['No,', 'não,']]), ('educado', [['please!', 'por favor!'], ['thanks.', 'obrigado.']])], ('', '')),
              mold('Explicar o não', [('recusa', [['No, thanks.', 'não, obrigado.']]), ('motivo', [["I'm full.", 'estou satisfeito.'], ["I'm not hungry.", 'não estou com fome.'], ["I'm tired.", 'estou cansado.']])], ('', ''))],
        speak=[['Would you like some tea? Yes, please!', 'Você quer um pouco de chá? Sim, por favor!'], ["No, thanks. I'm full.", 'Não, obrigado. Estou satisfeito.']],
        trap=[mtrap('“Help yourself!” quer dizer…', ['Me ajude!', 'Sirva-se!', 'Ajude-se a sair!'], 1, '**Help yourself!** = fique à vontade, sirva-se.', 'Help yourself!'),
              mtrap('Qual frase está certa?', ["I'm full of.", 'I full.', "I'm full."], 2, 'Estou satisfeito = **I’m full.**', "I'm full.")],
        gap=[mgap('Would ___ like some juice?', 'Você quer um pouco de suco?', ['you', 'I', 'he'], 0, 'Oferecendo a você: Would **you** like…?', 'Would you like some juice?'),
             mgap('___ later, thanks.', 'Talvez mais tarde, obrigado.', ['Maybe', 'Many', 'May'], 0, '**Maybe later** = talvez mais tarde.', 'Maybe later, thanks.')],
        expq=[expq('Você já comeu bastante e alguém oferece mais bolo.', ["I'm full, thanks.", 'My treat!', 'Help yourself!'], 0, '**I’m full, thanks.** = estou satisfeito.'),
              expq('Você paga a conta de todos no café.', ['Maybe later.', 'My treat!', "I'm full."], 1, '**My treat!** = é por minha conta!'),
              expq('Seu convidado quer pegar um biscoito. O que você diz?', ['Help yourself!', "I'm full.", 'Maybe later.'], 0, '**Help yourself!** = fique à vontade!')],
        missions=[mission('🍵', 'Hora do chá', 'Aceite, recuse e explique.', 'Seu amigo oferece comida. **Aceite o chá com Yes, please, recuse o bolo com No, thanks e explique que você está satisfeito (I’m full).**', ['Yes, please!'],
                          "Yes, please! No, thanks. I'm full.", ['Aceitei o chá?', 'Recusei com No, thanks?', 'Disse que estou satisfeito?'],
                          [r'\byes,?\s*please\b', r'\bno,?\s*thank(?:s| you)\b', r"\bI(?:['’]m| am) full\b"],
                          [[['Yes, please!', 'Sim, por favor!']], [['No, thanks.', 'Não, obrigado.']], [["I'm full.", 'Estou satisfeito.']]],
                          ['Aceitou! ✅', 'Recusou! 🙅', 'Explicou! 😋'], ['Great! Enjoy your tea!', 'Ótimo! Aproveite o seu chá!']),
                  mission('🍪', 'Você é o anfitrião', 'Ofereça com educação.', 'Receba uma amiga em casa. **Ofereça chá e depois outra coisa para comer com Would you like…? e diga Help yourself.**', ['Would you like…?'],
                          'Would you like some tea? Would you like a cookie? Help yourself!', ['Ofereci chá?', 'Ofereci outra coisa?', 'Disse Help yourself?'],
                          [r'\bwould you like\b[^.!?]*\btea\b', r'\bwould you like\b[^.!?]*\b(?:cookie|cake|sandwich|juice|apple)\b', r'\bhelp yourself\b'],
                          [[['Would you like some tea?', 'Você quer um pouco de chá?']], [['Would you like a cookie?', 'Você quer um biscoito?']], [['Help yourself!', 'Sirva-se!']]],
                          ['Chá oferecido! 🍵', 'Outra oferta! 🍪', 'Bem-vinda! 🍽️'], ['Yes, please! Thank you!', 'Sim, por favor! Obrigada!'])])
    CXs = cx(('It is a hot drink. English people love it with milk at five o\'clock. Would you like some ___?', 'É uma bebida quente. Os ingleses adoram com leite às cinco da tarde. Você quer um pouco de chá?', ['tea', 'juice', 'apple']),
             ('It is small, sweet and round. You eat it with milk. It is a ___.', 'É pequeno, doce e redondo. Você come com leite. É um biscoito.', ['cookie', 'sandwich', 'cake']),
             ('It is my birthday. There are candles on the ___.', 'É meu aniversário. Há velas no bolo.', ['cake', 'tea', 'apple']),
             ('Bread, cheese and ham. It is a ___.', 'Pão, queijo e presunto. É um sanduíche.', ['sandwich', 'cookie', 'juice']),
             ('Orange ___ is a cold drink. I drink it at breakfast.', 'O suco de laranja é uma bebida gelada. Eu bebo no café da manhã.', ['juice', 'cake', 'tea']),
             ('A red or green fruit that grows on a tree. A doctor says: eat one every day. It is an ___.', 'Uma fruta vermelha ou verde que cresce numa árvore. O médico diz: coma uma por dia. É uma maçã.', ['apple', 'cookie', 'sandwich']))
    return dict(B=B, X=X, XT=XT, VB=VB, MR=MR, CX=CXs)


# ============================================================ 40 · Brown Bear, Brown Bear
BEAR = 'e:🐻'
BIRD = 'e:🐦'
DUCK = 'e:🦆'


def ep40():
    B = dict(
        title="What's This? · What's this? It's a…",
        sub="Perguntar o que é e responder com cores: It's a red ball.",
        pattern_label="What's this? It's a…",
        why="Hoje você aprende a perguntar What's this? e a responder It's a… com as cores red, yellow, blue, green e orange.",
        vocab=[['Red', 'Vermelho', 'Soa como “RÉD”.'], ['Yellow', 'Amarelo', 'Soa como “IÉ-lou”.'], ['Blue', 'Azul', 'Soa como “BLÚ”.'],
               ['Green', 'Verde', 'Soa como “GRÍIN”.'], ['Orange', 'Laranja', 'Soa como “Ó-rinj”.'], ['Color', 'Cor', 'Soa como “KÂ-lor”.']],
        balloons=[['🔴', 'red'], ['🟡', 'yellow'], ['🔵', 'blue'], ['🟢', 'green'], ['🟠', 'orange'], ['🎨', 'color']],
        cover_art=dict(s='shop', items=[['🐻', 104, 56, 20, 'bob'], ['🔴', 138, 44, 12, 'bob'], ['❓', 84, 34, 12, 'bob']], seed='bb1'),
        cover_sub="What's this? Em 10 minutos você pergunta e responde com cores",
        cover_say='O Urso Marrom e seus amigos bichos estão numa loja cheia de coisas coloridas. O que é isso? E de que cor é? Vamos descobrir!',
        wrap_recap=[["What's this?", 'O que é isto?'], ["It's a red ball.", 'É uma bola vermelha.'], ["It's an orange.", 'É uma laranja.'], ["It's a yellow hat.", 'É um chapéu amarelo.']],
        teaser=dict(t='Charlie and the Chocolate Factory', d='Próximo padrão: the red one e Can I have…, please?'),
        cast={'Bear': ['🐻', '#8d5524'], 'Bird': ['🐦', '#c0392b'], 'Duck': ['🦆', '#d4a017']},
        lines=[['Bear', "Look at the shelf! What's this?", 'Olhe a prateleira! O que é isto?'],
               ['Bird', "It's a ball. It's a red ball!", 'É uma bola. É uma bola vermelha!'],
               ['Duck', "Oh! And what's this?", 'Ah! E o que é isto?'],
               ['Bear', "It's a hat. It's a yellow hat!", 'É um chapéu. É um chapéu amarelo!'],
               ['Bird', "Look, a book! It's a blue book.", 'Olhe, um livro! É um livro azul.'],
               ['Duck', "What's this? Is it a frog?", 'O que é isto? É um sapo?'],
               ['Bear', "No, it's an orange!", 'Não, é uma laranja!'],
               ['Bird', 'An orange orange! Ha ha!', 'Uma laranja laranja! Ha ha!']],
        quiz=[quiz('What is red?', 'O que é vermelho?', [['🎩', 'The hat'], ['⚽', 'The ball'], ['📘', 'The book']], 1, 1, 'O Pássaro diz: “It’s a red ball!”'),
              quiz('What color is the hat?', 'De que cor é o chapéu?', [['🟡', 'Yellow'], ['🔵', 'Blue'], ['🔴', 'Red']], 0, 3, 'O Urso diz: “It’s a yellow hat!”'),
              quiz('What is the last thing?', 'O que é a última coisa?', [['🐸', 'A frog'], ['🍎', 'An apple'], ['🍊', 'An orange']], 2, 6, 'O Urso diz: “No, it’s an orange!”')],
        rdg_q=dict(q='Qual frase diz “É uma bola vermelha”?', o=["It's red a ball.", "It's a ball red.", "It's a red ball."], a=2,
                   why='Em inglês a cor vem **antes** do nome: a **red** ball.'),
        dictate=[["What's this?", 'O que é isto?'], ["It's a red ball.", 'É uma bola vermelha.'], ["It's a yellow hat.", 'É um chapéu amarelo.'], ["It's an orange.", 'É uma laranja.']],
        produce=produce('O Urso mostra um objeto e pergunta: *What’s this?* **Responda com It’s a… e uma cor, pergunte o que é outra coisa com What’s this? e diga o nome de uma fruta com an.**',
                        "Ex.: It's a red ball. What's this? It's an orange.", ["It's a…", "What's this?", "It's an…"],
                        "It's a red ball. What's this? It's an orange!",
                        ['Respondi com It’s a + cor + coisa?', 'Perguntei What’s this?', 'Usei an antes de vogal?'],
                        [r"\bit(?:['’]s| is) an? (?:red|yellow|blue|green|orange)\s+\w+", r"\bwhat(?:['’]s| is) this\b", r'\ban (?:orange|apple|egg|umbrella|ice cream|elephant)\b'],
                        [[["It's a red ball.", 'É uma bola vermelha.'], ["It's a blue book.", 'É um livro azul.']], [["What's this?", 'O que é isto?']], [["It's an orange.", 'É uma laranja.'], ["It's an apple.", 'É uma maçã.']]],
                        ['Cor antes da coisa! 🔴', 'Boa pergunta! ❓', 'An certo! 🍊'],
                        ["Great! It's a green frog!", 'Ótimo! É um sapo verde!']),
        rs=RSD('shop', 'park2', 'school', 'market', 'home1', 'kitchen', 'yard'),
        sc='shop')
    X = dict(
        n=9808, review=True, names=('Bear', 'Bird'),
        stage=dict(rs='shop', chars=[[BEAR, 28, 0, 1.1], [BIRD, 56, 1, 0.7], [DUCK, 82, 1, 0.7]]),
        obra=dict(name='Brown Bear, Brown Bear, What Do You See?', kind='📖 Livro infantil · 1967', year='1967',
                  text='Livro infantil de Bill Martin Jr., com ilustrações de Eric Carle, de 1967. Cada página mostra um bicho de uma cor (urso marrom, pássaro vermelho, pato amarelo…) e repete a pergunta “What do you see?”. É um clássico para aprender cores.',
                  line=['Brown Bear, what do you see?', 'Urso Marrom, o que você vê? (pergunta que se repete no livro)'],
                  pa=dict(t='toyshop', e=['🐻', '🐦', '🎨'], p='a', v=0)),
        gancho=['Bear', "Look at the shelf! What's this?", 'Olhe a prateleira! O que é isto?'],
        hot=[hot('🍎', 14, 16, 'apple', 'maçã', "It's a red apple.", 'É uma maçã vermelha.'),
             hot('🍌', 40, 14, 'banana', 'banana', "It's a yellow banana.", 'É uma banana amarela.'),
             hot('🐳', 66, 14, 'whale', 'baleia', "It's a blue whale.", 'É uma baleia azul.'),
             hot('🐸', 88, 16, 'frog', 'sapo', "It's a green frog.", 'É um sapo verde.'),
             hot('🍊', 12, 82, 'orange', 'laranja', "It's an orange.", 'É uma laranja.')],
        gap=[gap("___ this? It's a hat.", 'O que é isto? É um chapéu.', ["Where's", "What's", "Why's"], 1, "Para perguntar o que é algo: **What's** this?"),
             gap("It's ___ orange.", 'É uma laranja.', ['a', 'an', 'two'], 1, '**an** antes de som de vogal: an orange.'),
             gap("It's a red ___.", 'É uma bola vermelha.', ['ball', 'balls', 'a ball'], 0, 'Depois da cor vem o nome no singular: a red **ball**.'),
             gap("It's ___ yellow hat.", 'É um chapéu amarelo.', ['a', 'an', 'some'], 0, '**yellow** começa com som de consoante: **a** yellow hat.')],
        trap=[trap(["It's a orange.", "It's an orange.", "It's one orange apple."], 1, '**orange** começa com som de vogal, então use **an**.'),
              trap(['What this is?', "What's this?", "What it's this?"], 1, 'A pergunta é **What’s this?** (What + is = What’s).')],
        sticker=dict(title='O Urso Marrom e a bola vermelha', sub='Brown Bear, Brown Bear · 1967', rs='shop', chars=[[BEAR, 34, 0, 1.1], [BIRD, 68, 1, 0.7]]),
        speakers={'Bear': BEAR, 'Bird': BIRD, 'Duck': DUCK},
        rule=dict(
            who=BEAR, head="What's this? It's a…", sub='Perguntar o que é e responder com a cor.',
            say=["What's this? It's a red ball.", 'O que é isto? É uma bola vermelha.'],
            formula=[dict(from_=[['What', 0], ['is', 1], ['this?', 3]], to=[["What's", 2], ['this?', 3]], say="What's this?", note='What + is = **What’s**. Pergunta o que é uma coisa.'),
                     dict(from_=[['It', 0], ['is', 1], ['a ball.', 3]], to=[["It's", 2], ['a', 1], ['red', 0], ['ball.', 3]], say="It's a red ball.", note='Responda com **It’s** + a + **cor** + coisa. A cor vem antes da coisa.'),
                     dict(from_=[['a', 1], ['orange', 3]], to=[['an', 2], ['orange', 3]], say="It's an orange.", note='**an** antes de som de vogal: an orange, an apple.')],
            uses=[dict(ico='❓', tag='Perguntar', en="What's this?", pt='O que é isto?'),
                  dict(ico='🔴', tag='Responder', en="It's a red ball.", pt='É uma bola vermelha.'),
                  dict(ico='🍊', tag='Com an', en="It's an orange.", pt='É uma laranja.'),
                  dict(ico='🟡', tag='Outra cor', en="It's a yellow hat.", pt='É um chapéu amarelo.')],
            rules=[dict(tag="What's this?", c=0, text='Pergunta sobre **uma coisa** perto de você.', ex="What's this?"),
                   dict(tag='cor + coisa', c=1, text='A cor vem **antes** do nome.', ex='✗ a ball red  →  ✓ a red ball'),
                   dict(tag='a / an', c=2, text='**a** antes de consoante, **an** antes de vogal.', ex='a green frog · an orange')],
            tips=['Em português a cor vem depois (bola vermelha). Em inglês vem **antes**: a **red** ball.']),
        mission_ic='🎨')
    XT = dict(
        exp=[exp('👀', 'Just looking, thanks.', 'Expressão', 'Só olhando, obrigado.', 'Quando o vendedor pergunta se pode ajudar e você quer **apenas olhar**.', ['Just looking, thanks.', 'Só olhando, obrigado.']),
             exp('🎨', 'Do you have it in blue?', 'Expressão', 'Você tem em azul?', 'Para perguntar se **existe outra cor** do mesmo produto.', ['Do you have it in blue?', 'Você tem em azul?']),
             exp('🏷️', "It's on sale!", 'Informal', 'Está em promoção!', 'Quando algo está com **preço baixo**.', ["Look! It's on sale!", 'Olhe! Está em promoção!']),
             exp('😍', 'I love it!', 'Expressão', 'Eu adorei!', 'Quando você **gosta muito** de algo.', ['A yellow hat? I love it!', 'Um chapéu amarelo? Eu adorei!'])],
        exp_scene=dict(rs='shop', lines=[
            ['Bear', 'Welcome! Can I help you?', 'Bem-vindos! Posso ajudar?'],
            ['Bird', '**Just looking, thanks**.', 'Só olhando, obrigado.'],
            ['Duck', "Look! What's this? **I love it**!", 'Olhe! O que é isto? Eu adorei!'],
            ['Bear', "It's a hat. **It's on sale**!", 'É um chapéu. Está em promoção!'],
            ['Duck', '**Do you have it in blue**?', 'Você tem em azul?'],
            ['Bear', "Yes! It's a blue hat.", 'Tenho! É um chapéu azul.']]),
        lab=dict(
            short='“th” surdo', title='Laboratório de sons: o “th” de thanks',
            say='O “th” inglês não existe em português! Vamos treinar com Thanks, Three e Think.',
            intro=dict(what='O **th** de **thanks**, **three** e **think** é um som surdo: só ar, sem vibração na garganta.',
                       how='Coloque a pontinha da língua entre os dentes e sopre ar de leve. Não troque por **s** nem por **f**.',
                       pt='Muita gente diz “sanks” ou “fanks”. Cuidado: **think** (pensar) ≠ **sink** (pia), **thank** (agradecer) ≠ **sank** (afundou).'),
            ex=[['thanks', 'THÉNKS', 'obrigado', 'língua entre os dentes'], ['three', 'THRÍ', 'três', 'sopre antes do “r”'], ['think', 'THÍNK', 'pensar', 'ar saindo entre língua e dentes']],
            pairs=[['think', 'sink', '“pensar” × “pia”: em think a língua aparece entre os dentes'], ['thank', 'sank', '“agradecer” × “afundou”'], ['three', 'free', '“três” × “livre/grátis”']],
            tip='Língua entre os dentes e sopro suave. Se a língua ficar atrás dos dentes, vira “s”.',
            phrase=['Thanks! Three red balls, I think.', 'Obrigado! Três bolas vermelhas, acho.'],
            rounds=[rnd('sink', ['think', 'sink'], 1, '**Sink** começa com “s”, a língua fica atrás dos dentes.'),
                    rnd('thank', ['thank', 'sank'], 0, '**Thank** tem a língua entre os dentes. **Sank** começa com “s”.'),
                    rnd('free', ['three', 'free'], 1, '**Free** começa com “f”: o lábio de baixo encosta nos dentes de cima.')]),
        hunt=[ht('think', ['think', 'sink'], 0, '**think** começa com “th”, com a língua entre os dentes.'), hp('thumb', ['👍', '🎸', '🏠'], 0, '**thumb** = polegar, começa com “th”.'),
              ht('thick', ['thick', 'sick'], 0, '**thick** = grosso, com “th” de língua entre os dentes.'), ht('thanks', ['thanks', 'sanks'], 0, '**thanks** começa com “th”.')])
    VB = dict(title='Verbos para olhar a loja', tip='Quatro verbos: see, point, find e touch.', items=[
        verb('see', '👀', 'ver', 'I see a red ball.', 'The Bear see**s** a blue book.', ['I see a red ball.', 'Eu vejo uma bola vermelha.'], '**see** = ver. Com he/she: **sees**.'),
        verb('point', '👉', 'apontar', 'I point at the hat.', 'She point**s** at the frog.', ['I point at the hat.', 'Eu aponto para o chapéu.'], '**point** = apontar. Com he/she: **points**.'),
        verb('find', '🔎', 'achar, encontrar', 'I find a yellow hat.', 'He find**s** a green frog.', ['I find a yellow hat.', 'Eu acho um chapéu amarelo.'], '**find** = achar, encontrar. Com he/she: **finds**.'),
        verb('touch', '🖐️', 'tocar', 'I touch the red ball.', 'She touch**es** the orange.', ['I touch the red ball.', 'Eu toco a bola vermelha.'], '**touch** = tocar. Com he/she: **touches** (terminou em ch: ponha es).')])
    MR = dict(
        mold=[mold('Dizer o que é', [('frase', [["It's a", 'é um/uma']]), ('cor', [['red', 'vermelho(a)'], ['yellow', 'amarelo(a)'], ['blue', 'azul'], ['green', 'verde']]),
                                     ('coisa', [['ball', 'bola'], ['hat', 'chapéu'], ['book', 'livro'], ['frog', 'sapo'], ['bag', 'bolsa']])]),
              mold('Com an', [('frase', [["It's an", 'é um/uma']]), ('coisa', [['orange', 'laranja'], ['apple', 'maçã'], ['egg', 'ovo'], ['umbrella', 'guarda-chuva'], ['ice cream', 'sorvete']])]),
              mold('Pedir outra cor', [('frase', [['Do you have it in', 'você tem em']]), ('cor', [['blue', 'azul'], ['red', 'vermelho'], ['green', 'verde'], ['yellow', 'amarelo'], ['orange', 'laranja']])], ('?', '?'))],
        speak=[["What's this? It's a red ball.", 'O que é isto? É uma bola vermelha.'], ['Just looking, thanks. I love it!', 'Só olhando, obrigado. Eu adorei!']],
        trap=[mtrap('“Just looking, thanks.” quer dizer…', ['Só olhando, obrigado.', 'Quero comprar, obrigado.', 'Está caro, obrigado.'], 0, '**Just looking** = só olhando.', 'Just looking, thanks.'),
              mtrap('Qual frase está certa?', ['It on sale!', "It's on sale!", "It's in sale!"], 1, 'Em promoção = **on sale**.', "It's on sale!")],
        gap=[mgap('Do you have it ___ blue?', 'Você tem em azul?', ['in', 'on', 'at'], 0, 'Pedir uma cor: **in** blue.', 'Do you have it in blue?'),
             mgap("It's ___ sale!", 'Está em promoção!', ['on', 'in', 'to'], 0, 'Em promoção = **on** sale.', "It's on sale!")],
        expq=[expq('O vendedor pergunta se pode ajudar, mas você só quer olhar.', ['I love it!', "It's on sale!", 'Just looking, thanks.'], 2, '**Just looking, thanks.** = só olhando.'),
              expq('Você gosta do casaco, mas quer outra cor.', ['Do you have it in green?', 'Just looking.', "It's on sale!"], 0, '**Do you have it in…?** pede outra cor.'),
              expq('Você vê um tênis lindo com preço baixo.', ['Just looking.', "It's on sale!", 'Do you have it?'], 1, "**It's on sale!** = está em promoção!")],
        missions=[mission('🛍️', 'Na loja', 'Use as frases da loja.', 'Na loja, **diga que está só olhando, pergunte se tem em azul e diga que adorou.**', ['Just looking, thanks.'],
                          'Just looking, thanks. Do you have it in blue? I love it!', ['Disse que estou só olhando?', 'Perguntei se tem em azul?', 'Disse que adorei?'],
                          [r'\bjust looking\b', r'\bdo you have it in (?:blue|red|green|yellow|orange)\b', r'\bI love it\b'],
                          [[['Just looking, thanks.', 'Só olhando, obrigado.']], [['Do you have it in blue?', 'Você tem em azul?']], [['I love it!', 'Eu adorei!']]],
                          ['Educado! 👀', 'Cor pedida! 🎨', 'Que bom! 😍'], ['Yes! Here it is, in blue.', 'Tenho! Aqui está, em azul.']),
                  mission('🎒', 'Descreva um objeto', 'Pergunte e responda.', 'Pegue um objeto da sua mesa. **Pergunte What’s this?, responda com It’s a + cor + objeto e use an em uma frase.**', ["What's this?"],
                          "What's this? It's a green pen. It's an orange.", ['Perguntei What’s this?', 'Respondi com It’s a + cor + objeto?', 'Usei an?'],
                          [r"\bwhat(?:['’]s| is) this\b", r"\bit(?:['’]s| is) an? \w+", r'\ban \w+'],
                          [[["What's this?", 'O que é isto?']], [["It's a green pen.", 'É uma caneta verde.']], [["It's an orange.", 'É uma laranja.']]],
                          ['Boa pergunta! ❓', 'Cor e coisa! 🟢', 'An certo! 🍊'], ["It's great! I see a red bag too.", 'Que legal! Eu vejo uma bolsa vermelha também.'])])
    CXs = cx(('The color of a ripe tomato and a stop sign is ___.', 'A cor de um tomate maduro e de uma placa de pare é vermelho.', ['red', 'blue', 'green']),
             ('The sun and a banana are ___.', 'O sol e uma banana são amarelos.', ['yellow', 'green', 'orange']),
             ('The sky on a sunny day is ___.', 'O céu num dia de sol é azul.', ['blue', 'red', 'yellow']),
             ('Grass and leaves are ___.', 'A grama e as folhas são verdes.', ['green', 'blue', 'color']),
             ('It is a fruit and also a color between red and yellow. It is ___.', 'É uma fruta e também uma cor entre o vermelho e o amarelo. É laranja.', ['orange', 'green', 'red']),
             ('I love rainbows! They have many ___.', 'Eu adoro arco-íris! Eles têm muitas cores.', ['colors', 'balls', 'hats']))
    return dict(B=B, X=X, XT=XT, VB=VB, MR=MR, CX=CXs)


# ============================================================ 41 · Charlie and the Chocolate Factory
CHARLIE = 'p:short:4a3728:f4c7a1:8d6e63:none:shirt'
JOE = 'p:short:d9d9d9:e8b48a:2e5a88:glasses:shirt'
SHOPK = 'p:bun:3b2f2f:f4c7a1:c0392b:none:dress'


def ep41():
    B = dict(
        title='Candy Shop · the red one',
        sub='Escolher pela cor com the red one e pedir com Can I have…, please?',
        pattern_label='the red one',
        why='Hoje você aprende a escolher e pedir na loja de doces do Charlie: the yellow one, the green one e Can I have…, please?',
        vocab=[['Chocolate', 'Chocolate', 'Soa como “TCHÓK-lit”.'], ['Candy', 'Bala, doce', 'Soa como “KÉN-di”.'], ['Lollipop', 'Pirulito', 'Soa como “LÓ-li-pop”.'],
               ['Ticket', 'Bilhete, ingresso', 'Soa como “TÍ-kit”.'], ['Ice cream', 'Sorvete', 'Soa como “ÁIS-crim”.'], ['Box', 'Caixa', 'Soa como “BÓKS”.']],
        balloons=[['🍫', 'chocolate'], ['🍬', 'candy'], ['🍭', 'lollipop'], ['🎫', 'ticket'], ['🍦', 'ice cream'], ['📦', 'box']],
        cover_art=dict(s='shop', items=[['🍫', 104, 56, 20, 'bob'], ['🍭', 138, 44, 12, 'bob'], ['🎫', 84, 34, 12, 'bob']], seed='cc1'),
        cover_sub='The red one! Em 10 minutos você escolhe doces como o Charlie',
        cover_say='O Charlie e o avô Joe entram numa loja de doces. Tem balas, pirulitos e chocolates de todas as cores. Como pedir exatamente o que você quer?',
        wrap_recap=[['The yellow one, please.', 'O amarelo, por favor.'], ['Can I have the red one?', 'Posso ficar com o vermelho?'], ['I want the green one.', 'Eu quero o verde.'], ['Open it!', 'Abra!']],
        teaser=dict(t='Baa, Baa, Black Sheep', d='Próximo padrão: Can I try it on? e mais cores'),
        cast={'Charlie': ['👦', '#8d6e63'], 'Grandpa': ['👴', '#2e5a88'], 'Shopkeeper': ['👩', '#c0392b']},
        lines=[['Charlie', "Hello! What's this?", 'Olá! O que é isto?'],
               ['Shopkeeper', "It's a lollipop. It's a green lollipop.", 'É um pirulito. É um pirulito verde.'],
               ['Charlie', "And what's this? Is it a box?", 'E o que é isto? É uma caixa?'],
               ['Shopkeeper', "Yes! It's a blue box of candy.", 'Sim! É uma caixa azul de balas.'],
               ['Grandpa', "Charlie, look! What's the yellow one?", 'Charlie, olhe! O que é o amarelo?'],
               ['Shopkeeper', "It's a chocolate bar.", 'É uma barra de chocolate.'],
               ['Charlie', 'Can I have the yellow one, please?', 'Posso ficar com o amarelo, por favor?'],
               ['Grandpa', 'Open it! Look, a ticket!', 'Abra! Olhe, um bilhete!']],
        quiz=[quiz('What color is the lollipop?', 'De que cor é o pirulito?', [['🟢', 'Green'], ['🔴', 'Red'], ['🔵', 'Blue']], 0, 1, 'A vendedora diz: “It’s a green lollipop.”'),
              quiz('What does Charlie ask for?', 'O que o Charlie pede?', [['🟢', 'The green one'], ['🔵', 'The blue one'], ['🟡', 'The yellow one']], 2, 6, 'Charlie diz: “Can I have the yellow one, please?”'),
              quiz('What is the yellow one?', 'O que é o amarelo?', [['🍭', 'A lollipop'], ['🍫', 'A chocolate bar'], ['📦', 'A box']], 1, 5, 'A vendedora diz: “It’s a chocolate bar.”')],
        rdg_q=dict(q='Como pedir “o amarelo” (o doce amarelo)?', o=['The yellow it', 'The yellow one', 'The one yellow'], a=1,
                   why='Para não repetir o nome, use **one**: the yellow **one**. A cor vem antes.'),
        dictate=[['The yellow one, please.', 'O amarelo, por favor.'], ['Can I have the red one?', 'Posso ficar com o vermelho?'], ['I want the green one.', 'Eu quero o verde.'], ["What's the blue one?", 'O que é o azul?']],
        produce=produce('Você está numa loja de doces. **Peça um doce pela cor com Can I have the … one, please?, diga que quer outro com I want the… one e agradeça.**',
                        'Ex.: Can I have the yellow one, please? I want the green one too. Thanks!', ['Can I have…?', 'I want the… one', 'Thanks!'],
                        'Can I have the yellow one, please? I want the green one too. Thanks!',
                        ['Pedi pela cor com Can I have the … one?', 'Disse I want the … one?', 'Agradeci?'],
                        [r'\bcan i have the \w+ one\b', r'\bI want the \w+ one\b', r'\bthank(?:s| you)\b'],
                        [[['Can I have the red one, please?', 'Posso ficar com o vermelho, por favor?']], [['I want the green one.', 'Eu quero o verde.']], [['Thanks!', 'Obrigado!'], ['Thank you!', 'Obrigado!']]],
                        ['Pedido educado! 🍬', 'Escolha feita! 🍭', 'Educação! 🙏'],
                        ['Here you go! Enjoy your candy!', 'Aqui está! Aproveite os seus doces!']),
        rs=RSD('shop', 'market', 'counter', 'diner', 'street', 'cafe2', 'park'),
        sc='shop')
    X = dict(
        n=7009808, review=True, names=('Charlie', 'Shopkeeper'),
        stage=dict(rs='shop', chars=[[CHARLIE, 28, 0, 0.9], [JOE, 56, 1, 1.0], [SHOPK, 84, 1, 1.0]]),
        obra=dict(name='Charlie and the Chocolate Factory', kind='📖 Livro infantil · 1964', year='1964',
                  text='Livro infantil do escritor britânico Roald Dahl, de 1964. O menino pobre Charlie Bucket acha um bilhete dourado numa barra de chocolate e ganha uma visita à fábrica secreta do Sr. Wonka.',
                  line=['I want the yellow one, please.', 'Eu quero o amarelo, por favor. (frase do tema da cena)'],
                  pa=dict(t='bakery', e=['🍫', '🎫', '🍭'], p='d', v=0)),
        gancho=['Charlie', "Hello! What's this?", 'Olá! O que é isto?'],
        hot=[hot('🍫', 14, 16, 'chocolate', 'chocolate', 'I want the yellow one, please.', 'Eu quero o amarelo, por favor.'),
             hot('🍭', 40, 14, 'lollipop', 'pirulito', 'The green one, please.', 'O verde, por favor.'),
             hot('🍬', 66, 14, 'candy', 'bala', 'Can I have the red one?', 'Posso ficar com a vermelha?'),
             hot('📦', 88, 16, 'box', 'caixa', 'The blue box, please.', 'A caixa azul, por favor.'),
             hot('🍦', 12, 82, 'ice cream', 'sorvete', 'Can I have the orange one?', 'Posso ficar com o laranja?')],
        gap=[gap('Can I ___ the red one?', 'Posso ficar com o vermelho?', ['have', 'has', 'am'], 0, 'Depois de **Can I** o verbo fica no infinitivo: Can I **have**…'),
             gap('I want the ___ one.', 'Eu quero o azul.', ['a blue', 'blue', 'blues'], 1, 'A cor fica sozinha antes de **one**: the **blue** one.'),
             gap("It's ___ orange ice cream.", 'É um sorvete de laranja.', ['an', 'a', 'two'], 0, '**orange** começa com som de vogal: **an** orange.'),
             gap("What's ___? It's a ticket.", 'O que é isto? É um bilhete.', ['they', 'I', 'this'], 2, 'Pergunta sobre uma coisa: What’s **this**?')],
        trap=[trap(['The one yellow, please.', 'The yellow one, please.', 'The yellow it, please.'], 1, 'A cor vem antes de **one**: the **yellow one**.'),
              trap(['Can I has a candy?', 'Can I having a candy?', 'Can I have a candy?'], 2, 'Depois de **Can I** use o verbo simples: Can I **have**.')],
        sticker=dict(title='Charlie e o bilhete', sub='Charlie and the Chocolate Factory · 1964', rs='shop', chars=[[CHARLIE, 34, 0, 0.9], [JOE, 68, 1, 1.0]]),
        speakers={'Charlie': CHARLIE, 'Grandpa': JOE, 'Shopkeeper': SHOPK},
        rule=dict(
            who=CHARLIE, head='the red one', sub='Escolher pela cor sem repetir o nome.',
            say=['Can I have the yellow one, please?', 'Posso ficar com o amarelo, por favor?'],
            formula=[dict(from_=[['a', 0], ['red', 2], ['box', 3]], to=[['the', 0], ['red', 2], ['one', 3]], say='the red one', note='Para não repetir o nome, troque-o por **one**: the red **one**.'),
                     dict(from_=[['I want', 0], ['the red one.', 3]], to=[['Can I have', 1], ['the red one,', 3], ['please?', 2]], say='Can I have the red one, please?', note='Para pedir com educação: **Can I have…, please?**')],
            uses=[dict(ico='🍬', tag='Escolher', en='The red one, please.', pt='O vermelho, por favor.'),
                  dict(ico='🙋', tag='Pedir', en='Can I have the green one?', pt='Posso ficar com o verde?'),
                  dict(ico='👉', tag='Dizer o que quer', en='I want the yellow one.', pt='Eu quero o amarelo.'),
                  dict(ico='❓', tag='Perguntar', en="What's the blue one?", pt='O que é o azul?')],
            rules=[dict(tag='the + cor + one', c=0, text='**one** substitui o nome. A cor vem antes dele.', ex='the yellow one · the green one'),
                   dict(tag='Can I have', c=1, text='Depois de **Can I**, o verbo é **have**.', ex='✗ Can I has  →  ✓ Can I have'),
                   dict(tag='please', c=2, text='Termine com **please** para ser educado.', ex='Can I have the red one, please?')],
            tips=['Em português trocamos o nome por “o” ou “a” (o amarelo). Em inglês fica **the yellow one**: sempre com **one**.']),
        mission_ic='🍬')
    XT = dict(
        exp=[exp('🤲', 'Here you go.', 'Expressão', 'Aqui está.', 'Quando você **entrega** algo a alguém.', ['Here you go. One lollipop.', 'Aqui está. Um pirulito.']),
             exp('❓', 'Anything else?', 'Expressão', 'Mais alguma coisa?', 'O vendedor pergunta se você quer **mais algo**.', ['Anything else, sir?', 'Mais alguma coisa, senhor?']),
             exp('✅', "That's all, thanks.", 'Expressão', 'É só isso, obrigado.', 'Para dizer que seu **pedido terminou**.', ["That's all, thanks.", 'É só isso, obrigado.']),
             exp('🤩', 'Sweet!', 'Gíria', 'Legal! / Que bom!', 'Gíria americana para dizer que algo é **ótimo**. Aqui também é doce!', ['Sweet! A golden ticket!', 'Legal! Um bilhete dourado!'])],
        exp_scene=dict(rs='counter', lines=[
            ['Charlie', 'Hi! The green lollipop, please.', 'Oi! O pirulito verde, por favor.'],
            ['Shopkeeper', '**Here you go**. **Anything else**?', 'Aqui está. Mais alguma coisa?'],
            ['Grandpa', 'The yellow chocolate bar, please.', 'A barra de chocolate amarela, por favor.'],
            ['Shopkeeper', 'Sure. Two dollars, please.', 'Claro. Dois dólares, por favor.'],
            ['Grandpa', "**That's all, thanks**.", 'É só isso, obrigado.'],
            ['Charlie', '**Sweet**! I love candy!', 'Legal! Eu adoro doces!']]),
        lab=dict(
            short='sh × ch', title='Laboratório de sons: sh × ch',
            say='O “sh” de shop e o “ch” de chop são sons diferentes! Vamos treinar na loja do Charlie.',
            intro=dict(what='O **sh** de **shop** é um som contínuo, como pedir silêncio: shhh. O **ch** de **chop** é uma explosão curta: tch.',
                       how='No **sh**, solte o ar devagar com os lábios para frente. No **ch**, feche a língua no céu da boca e solte de uma vez.',
                       pt='Em português o “ch” é o nosso “x” de chave. O som de **ch** inglês é o do “tch” de “tchau”. Cuidado: **shop** (loja) ≠ **chop** (cortar).'),
            ex=[['shop', 'SHÓP', 'loja', 'ar contínuo, como “shhh”'], ['chocolate', 'TCHÓK-lit', 'chocolate', 'começa com “tch”'], ['cheese', 'TCHÍIZ', 'queijo', 'explosão curta no começo']],
            pairs=[['shop', 'chop', '“loja” × “cortar”: sh é contínuo, ch é explosivo'], ['shoe', 'chew', '“sapato” × “mastigar”'], ['wish', 'which', '“desejo” × “qual”']],
            tip='Peça silêncio (“shhh”) para o sh. Para o ch, diga “tchau” bem curtinho.',
            phrase=['Which shop has cheap chocolate?', 'Qual loja tem chocolate barato?'],
            rounds=[rnd('chop', ['shop', 'chop'], 1, '**Chop** começa com explosão “tch”. **Shop** é um sopro contínuo.'),
                    rnd('shoe', ['shoe', 'chew'], 0, '**Shoe** (sapato) é sopro contínuo. **Chew** (mastigar) tem “tch”.'),
                    rnd('which', ['wish', 'which'], 1, '**Which** (qual) termina com “tch”. **Wish** (desejo) termina com “sh” contínuo.')]),
        hunt=[ht('shoe', ['shoe', 'chew'], 0, '**shoe** = sapato, com “sh” contínuo.'), ht('chop', ['shop', 'chop'], 1, '**chop** = cortar, com “ch” explosivo.'),
              hp('cheese', ['🧀', '👞', '🚢'], 0, '**cheese** = queijo, começa com “ch”.'), ht('wish', ['wish', 'which'], 0, '**wish** = desejo, termina com “sh”.')])
    VB = dict(title='Verbos para a loja de doces', tip='Quatro verbos: look, open, smell e taste.', items=[
        verb('look', '👀', 'olhar', 'I look at the candy.', 'The boy look**s** at the box.', ['I look at the candy.', 'Eu olho para as balas.'], '**look** = olhar (look at). Com he/she: **looks**.'),
        verb('open', '📦', 'abrir', 'I open the box.', 'He open**s** the chocolate.', ['I open the box.', 'Eu abro a caixa.'], '**open** = abrir. Com he/she: **opens**.'),
        verb('smell', '👃', 'cheirar', 'I smell the chocolate.', 'It smell**s** good.', ['I smell the chocolate.', 'Eu sinto o cheiro do chocolate.'], '**smell** = cheirar. Com he/she/it: **smells**.'),
        verb('taste', '👅', 'provar', 'I taste the candy.', 'She taste**s** the ice cream.', ['I taste the candy.', 'Eu provo a bala.'], '**taste** = provar, ter gosto. Com he/she: **tastes**.')])
    MR = dict(
        mold=[mold('Pedir pelo doce', [('pedido', [['Can I have', 'posso ficar com']]), ('qual', [['the red one', 'o vermelho'], ['the green one', 'o verde'], ['the yellow one', 'o amarelo'], ['the blue one', 'o azul'], ['the orange one', 'o laranja']]),
                                      ('educação', [[', please', ', por favor']])], ('?', '?')),
              mold('Perguntar o que é', [('pergunta', [["What's", 'o que é']]), ('qual', [['this', 'isto'], ['the yellow one', 'o amarelo'], ['the blue box', 'a caixa azul']])], ('?', '?')),
              mold('Dizer o que quer', [('frase', [['I want', 'eu quero']]), ('o quê', [['the green lollipop', 'o pirulito verde'], ['the red candy', 'a bala vermelha'], ['the yellow one', 'o amarelo'], ['the blue box', 'a caixa azul']])])],
        speak=[['Can I have the yellow one, please?', 'Posso ficar com o amarelo, por favor?'], ["Here you go. That's all, thanks.", 'Aqui está. É só isso, obrigado.']],
        trap=[mtrap('“Anything else?” quer dizer…', ['Mais alguma coisa?', 'Quanto custa?', 'Onde fica?'], 0, '**Anything else?** = mais alguma coisa?', 'Anything else?'),
              mtrap('Qual frase está certa?', ['That all, thanks.', "That's all, thanks.", 'That is all thanks it.'], 1, "É só isso = **That's all.**", "That's all, thanks.")],
        gap=[mgap('Here you ___.', 'Aqui está.', ['go', 'are going', 'went'], 0, '**Here you go.** = aqui está.', 'Here you go.'),
             mgap("That's ___, thanks.", 'É só isso, obrigado.', ['all', 'any', 'every'], 0, "**That's all** = é só isso.", "That's all, thanks.")],
        expq=[expq('A vendedora pergunta se você quer mais algo, mas você já terminou.', ['Sweet!', "That's all, thanks.", 'Here you go.'], 1, "**That's all, thanks.** = é só isso."),
              expq('Você entrega o dinheiro à vendedora.', ['Anything else?', 'Here you go.', 'Sweet!'], 1, '**Here you go.** = aqui está.'),
              expq('Você ganhou um chocolate de graça! Reação animada:', ['Sweet!', 'Anything else?', "That's all."], 0, '**Sweet!** = legal!')],
        missions=[mission('🍭', 'No balcão', 'Peça e encerre o pedido.', 'O vendedor pergunta: *Anything else?* **Responda That’s all, thanks e peça um doce pela cor: Can I have the red one, please?**', ['Can I have…?'],
                          "That's all, thanks. Can I have the red one, please?", ['Disse que é só isso?', 'Pedi pela cor com Can I have the… one?', 'Usei please?'],
                          [r"\bthat['’]s all\b", r'\bcan i have the \w+ one\b', r'\bplease\b'],
                          [[["That's all, thanks.", 'É só isso, obrigado.']], [['Can I have the red one?', 'Posso ficar com o vermelho?']], [['please', 'por favor']]],
                          ['Fim do pedido! ✅', 'Pedido pela cor! 🍬', 'Educação! 🙏'], ['Sure! Here you go!', 'Claro! Aqui está!']),
                  mission('🍫', 'O que é isto?', 'Pergunte e reaja.', 'Você vê um doce estranho. **Pergunte What’s this?, diga o que é com It’s… e reaja com Sweet!**', ["What's this?"],
                          "What's this? It's a green candy. Sweet!", ['Perguntei What’s this?', 'Disse o que é com It’s…?', 'Reagi com Sweet?'],
                          [r"\bwhat(?:['’]s| is) this\b", r"\bit(?:['’]s| is) an? \w+", r'\bsweet\b'],
                          [[["What's this?", 'O que é isto?']], [["It's a green candy.", 'É uma bala verde.']], [['Sweet!', 'Legal!']]],
                          ['Boa pergunta! ❓', 'Descrição certa! 🍬', 'Que legal! 🤩'], ["It's very sweet! Try it!", 'É bem doce! Prove!'])])
    CXs = cx(('It is a sweet food made from cocoa. It is brown and you can eat a bar. It is ___.', 'É um alimento doce feito de cacau. É marrom e vem em barra. É chocolate.', ['chocolate', 'lollipop', 'ticket']),
             ('It is small, sweet and colorful. Children love it. It is a ___.', 'É pequena, doce e colorida. As crianças adoram. É uma bala.', ['candy', 'box', 'ticket']),
             ('It is candy on a stick. You lick it. It is a ___.', 'É um doce num palito. Você lambe. É um pirulito.', ['lollipop', 'ice cream', 'candy']),
             ('You need a ___ to enter the factory.', 'Você precisa de um bilhete para entrar na fábrica.', ['ticket', 'lollipop', 'box']),
             ('It is cold and sweet. In summer, you eat it in a cone. It is ___.', 'É gelado e doce. No verão, você come na casquinha. É sorvete.', ['ice cream', 'chocolate', 'ticket']),
             ('You put the candy in a ___ and close it.', 'Você põe as balas numa caixa e fecha.', ['box', 'ticket', 'lollipop']))
    return dict(B=B, X=X, XT=XT, VB=VB, MR=MR, CX=CXs)


# ============================================================ 42 · Baa, Baa, Black Sheep
SHEEP = 'e:🐑'
DAME = 'p:bun:b0b0b0:f4c7a1:8e44ad:glasses:dress'
BOY42 = 'p:cap:6b3f26:f4c7a1:2980b9:none:shirt'


def ep42():
    B = dict(
        title='A Jacket in the Shop · Can I try it on?',
        sub='Cores black, white, pink, purple, brown e pedir para experimentar',
        pattern_label='Can I try it on?',
        why='Hoje você aprende a comprar roupa como o menino da rima: Can I try it on? E a falar das cores black, white, pink, purple e brown.',
        vocab=[['Black', 'Preto', 'Soa como “BLÉK”.'], ['White', 'Branco', 'Soa como “UÁIT”.'], ['Pink', 'Rosa', 'Soa como “PÍNK”.'], ['Purple', 'Roxo', 'Soa como “PÂR-pol”.'],
               ['Brown', 'Marrom', 'Soa como “BRÁUN”.'], ['Jacket', 'Jaqueta, casaco', 'Soa como “DJÉ-kit”.'], ['Shirt', 'Camisa', 'Soa como “SHÂRT”.']],
        balloons=[['⚫', 'black'], ['⚪', 'white'], ['🩷', 'pink'], ['🟣', 'purple'], ['🟤', 'brown'], ['🧥', 'jacket'], ['👕', 'shirt']],
        cover_art=dict(s='shop', items=[['🐑', 104, 56, 20, 'bob'], ['🧥', 138, 44, 12, 'bob'], ['👕', 84, 34, 12, 'bob']], seed='bs1'),
        cover_sub='Can I try it on? Em 10 minutos você compra roupa em inglês',
        cover_say='Na rima, a ovelha negra tem lã para todo mundo: um saco para o patrão, um para a patroa e um para o menino. Hoje o menino vai à loja de casacos de lã!',
        wrap_recap=[['Can I try it on?', 'Posso experimentar?'], ["I like the white one.", 'Eu gosto do branco.'], ["It fits!", 'Serviu!'], ["I'll take it.", 'Eu vou levar.']],
        teaser=dict(t='The Purple Cow', d='Próximo padrão: What color is it?'),
        cast={'Sheep': ['🐑', '#2d2d2d'], 'Dame': ['👵', '#8e44ad'], 'Boy': ['👦', '#2980b9']},
        lines=[['Dame', 'Welcome to my shop! The wool jackets are here.', 'Bem-vindo à minha loja! Os casacos de lã estão aqui.'],
               ['Boy', 'I like this jacket. Do you have it in white?', 'Eu gosto deste casaco. Você tem em branco?'],
               ['Dame', "Yes. It's in white, brown and pink.", 'Tenho. Tem em branco, marrom e rosa.'],
               ['Boy', 'Can I try the white one on?', 'Posso experimentar o branco?'],
               ['Dame', 'Of course! Here you are.', 'Claro! Aqui está.'],
               ['Sheep', "Baa! It's my wool!", 'Béé! É a minha lã!'],
               ['Boy', "It fits! I like it. I'll take it.", 'Serviu! Eu gostei. Eu vou levar.'],
               ['Sheep', 'Baa, baa! Three bags full!', 'Béé, béé! Três sacos cheios!']],
        quiz=[quiz('What color does the boy want?', 'Que cor o menino quer?', [['🩷', 'Pink'], ['🟤', 'Brown'], ['⚪', 'White']], 2, 1, 'O menino pergunta: “Do you have it in white?”'),
              quiz('What does the boy try on?', 'O que o menino experimenta?', [['🧥', 'A jacket'], ['👕', 'A shirt'], ['👜', 'A bag']], 0, 3, 'Ele pergunta: “Can I try the white one on?” Ele fala do casaco (jacket).'),
              quiz('What does the boy say about the jacket?', 'O que o menino diz sobre o casaco?', [['📏', "It's big"], ['✅', 'It fits'], ['🩷', "It's pink"]], 1, 6, 'O menino diz: “It fits!”')],
        rdg_q=dict(q='Como pedir para experimentar uma jaqueta?', o=['Can I try on it?', 'Can I trying it?', 'Can I try it on?'], a=2,
                   why='Com **it**, o it fica no meio: try **it** on.'),
        dictate=[['Can I try it on?', 'Posso experimentar?'], ['I like the white one.', 'Eu gosto do branco.'], ['It fits!', 'Serviu!'], ["I'll take it.", 'Eu vou levar.']],
        produce=produce('Você está numa loja de roupas. **Diga que gosta de uma cor, peça para experimentar com Can I try it on? e diga que vai levar com I’ll take it.**',
                        "Ex.: I like the white jacket. Can I try it on? I'll take it.", ['I like the…', 'Can I try it on?', "I'll take it."],
                        "I like the white jacket. Can I try it on? It fits! I'll take it.",
                        ['Disse que gosto de uma cor?', 'Pedi para experimentar?', 'Disse que vou levar?'],
                        [r'\bI like\b[^.!?]*\b(?:black|white|pink|purple|brown|blue|red|green|yellow)\b', r'\bcan i try it on\b', r"\bI['’]ll take it\b|\bI will take it\b"],
                        [[['I like the white jacket.', 'Eu gosto do casaco branco.']], [['Can I try it on?', 'Posso experimentar?']], [["I'll take it.", 'Eu vou levar.']]],
                        ['Cor escolhida! ⚪', 'Pedido educado! 🧥', 'Compra feita! 🛍️'],
                        ['Great! The fitting room is over there.', 'Ótimo! O provador é ali.']),
        rs=RSD('shop', 'market', 'counter', 'lobby2', 'park2', 'home1', 'yard'),
        sc='shop')
    X = dict(
        n=70015, review=True, names=('Boy', 'Dame'),
        stage=dict(rs='shop', chars=[[BOY42, 28, 0, 0.95], [DAME, 56, 1, 1.0], [SHEEP, 84, 1, 0.8]]),
        obra=dict(name='Baa, Baa, Black Sheep', kind='🎶 Rima infantil · c. 1744', year='1744',
                  text='Rima infantil inglesa publicada por volta de 1744. Um menino pergunta à ovelha negra se ela tem lã, e ela responde: três sacos cheios, um para o patrão, um para a patroa e um para o menino da rua.',
                  line=['Baa, baa, black sheep, have you any wool?', 'Béé, béé, ovelha negra, você tem lã? (primeiro verso)'],
                  pa=dict(t='workshop', e=['🐑', '🧥', '🧶'], p='f', v=1)),
        gancho=['Dame', 'Welcome to my shop! The wool jackets are here.', 'Bem-vindo à minha loja! Os casacos de lã estão aqui.'],
        hot=[hot('🧥', 14, 16, 'jacket', 'jaqueta', "It's a black jacket.", 'É uma jaqueta preta.'),
             hot('👕', 40, 14, 'shirt', 'camisa', "It's a white shirt.", 'É uma camisa branca.'),
             hot('🎀', 66, 14, 'bow', 'laço', "It's a pink bow.", 'É um laço rosa.'),
             hot('👜', 88, 16, 'bag', 'bolsa', "It's a purple bag.", 'É uma bolsa roxa.'),
             hot('🧸', 12, 82, 'teddy bear', 'ursinho', "It's a brown teddy bear.", 'É um ursinho marrom.')],
        gap=[gap('Can I try it ___?', 'Posso experimentar?', ['on', 'in', 'up'], 0, 'Experimentar roupa = try **on**.'),
             gap('I like the ___ one.', 'Eu gosto do branco.', ['whites', 'a white', 'white'], 2, 'A cor fica sozinha antes de **one**: the **white** one.'),
             gap("It ___! I'll take it.", 'Serviu! Eu vou levar.', ['fit', 'fits', 'fitting'], 1, 'Com **it** o verbo leva **s**: it fit**s**.'),
             gap("I'll ___ it.", 'Eu vou levar.', ['take', 'takes', 'taking'], 0, "Depois de **I'll** use o verbo simples: I'll **take** it.")],
        trap=[trap(['Can I try on it?', 'Can I try it on?', 'Can I trying it on?'], 1, 'Com **it**, ele fica no meio: try **it** on.'),
              trap(['It fit me.', 'It fiting.', 'It fits.'], 2, 'Com **it** o verbo leva **s**: It fit**s**.')],
        sticker=dict(title='O menino e a ovelha negra', sub='Baa, Baa, Black Sheep · c. 1744', rs='shop', chars=[[BOY42, 34, 0, 0.95], [SHEEP, 68, 1, 0.8]]),
        speakers={'Sheep': SHEEP, 'Dame': DAME, 'Boy': BOY42},
        rule=dict(
            who=BOY42, head='Can I try it on?', sub='Experimentar roupa e decidir.',
            say=['Can I try it on?', 'Posso experimentar?'],
            formula=[dict(from_=[['I', 0], ['try', 1], ['it on.', 3]], to=[['Can', 1], ['I', 0], ['try', 1], ['it on?', 3]], say='Can I try it on?', note='**Can** vem na frente. O **it** fica no meio de try e on.'),
                     dict(from_=[['I take', 1], ['it.', 3]], to=[["I'll", 2], ['take', 1], ['it.', 3]], say="I'll take it.", note='**I’ll take it** = eu vou levar (decidi comprar).')],
            uses=[dict(ico='🧥', tag='Pedir', en='Can I try it on?', pt='Posso experimentar?'),
                  dict(ico='✅', tag='Servir', en='It fits!', pt='Serviu!'),
                  dict(ico='🛍️', tag='Decidir', en="I'll take it.", pt='Eu vou levar.'),
                  dict(ico='⚪', tag='Escolher', en='I like the white one.', pt='Eu gosto do branco.')],
            rules=[dict(tag='try it on', c=0, text='Com **it**, o it fica **no meio**.', ex='✗ try on it  →  ✓ try it on'),
                   dict(tag='it fits', c=1, text='Com it, he, she o verbo leva **s**.', ex='It fits. · He fits? ✗'),
                   dict(tag="I'll take it", c=2, text='Para dizer que vai comprar.', ex="I'll take it.")],
            tips=['Em português dizemos “posso provar?”. Em inglês, roupa se **experimenta** com **try it on**; “taste” é só para comida.']),
        mission_ic='🧥')
    XT = dict(
        exp=[exp('🧥', 'Can I try it on?', 'Expressão', 'Posso experimentar?', 'Pergunta feita **na loja de roupas**.', ['Can I try it on, please?', 'Posso experimentar, por favor?']),
             exp('🚪', 'Where is the fitting room?', 'Expressão', 'Onde fica o provador?', 'Para achar o **provador** da loja.', ['Where is the fitting room?', 'Onde fica o provador?']),
             exp('🛍️', "I'll take it.", 'Expressão', 'Eu vou levar.', 'Quando você **decidiu comprar**.', ["It's perfect. I'll take it.", 'É perfeito. Eu vou levar.']),
             exp('📏', "It's a little big.", 'Expressão', 'Está um pouco grande.', 'Quando a roupa **não serve bem**.', ["It's a little big. Do you have a small?", 'Está um pouco grande. Tem um menor?'])],
        exp_scene=dict(rs='counter', lines=[
            ['Boy', 'Hello! **Can I try it on**? **Where is the fitting room**?', 'Olá! Posso experimentar? Onde fica o provador?'],
            ['Dame', 'Over there, by the door.', 'Ali, perto da porta.'],
            ['Boy', 'Hmm. **It\'s a little big**.', 'Hum. Está um pouco grande.'],
            ['Dame', 'Try the black one.', 'Experimente o preto.'],
            ['Boy', "Perfect! **I'll take it**!", 'Perfeito! Eu vou levar!'],
            ['Sheep', 'Baa! Nice jacket, boy.', 'Béé! Bonito casaco, menino.']]),
        lab=dict(
            short='i curto × i longo', title='Laboratório de sons: ship × sheep',
            say='Em inglês, ship e sheep são palavras diferentes! A diferença é o tamanho do “i”.',
            intro=dict(what='**sheep** tem um “i” longo (ii), com a boca esticada como num sorriso. **ship** tem um “i” curto e relaxado.',
                       how='Em **sheep**, estique os lábios e segure o som: “shiiip”. Em **ship**, relaxe a boca e faça um “i” rápido.',
                       pt='Em português só temos um “i”. Por isso muita gente diz **ship** e **sheep** do mesmo jeito. Cuidado: **sheep** (ovelha) ≠ **ship** (navio).'),
            ex=[['sheep', 'SHÍIP', 'ovelha', 'i longo, boca esticada'], ['ship', 'SHIP', 'navio', 'i curto, boca relaxada'], ['pink', 'PÍNK', 'rosa', 'i curto']],
            pairs=[['sheep', 'ship', '“ovelha” × “navio”'], ['feet', 'fit', '“pés” × “servir”'], ['seat', 'sit', '“assento” × “sentar”']],
            tip='Sorria para o i longo (sheep) e relaxe a boca para o i curto (ship).',
            phrase=['The sheep sits on the ship.', 'A ovelha senta no navio.'],
            rounds=[rnd('sheep', ['sheep', 'ship'], 0, '**Sheep** (ovelha) tem “i” longo. **Ship** (navio) tem “i” curto.'),
                    rnd('fit', ['feet', 'fit'], 1, '**Fit** (servir) tem “i” curto. **Feet** (pés) tem “i” longo.'),
                    rnd('seat', ['seat', 'sit'], 0, '**Seat** (assento) tem “i” longo. **Sit** (sentar) tem “i” curto.')]),
        hunt=[ht('ship', ['sheep', 'ship'], 1, '**ship** = navio, com “i” curto.'), hp('sheep', ['🐑', '🚢', '🪑'], 0, '**sheep** = ovelha, com “i” longo.'),
              ht('feet', ['feet', 'fit'], 0, '**feet** = pés, com “i” longo.'), ht('sit', ['seat', 'sit'], 1, '**sit** = sentar, com “i” curto.')])
    VB = dict(title='Verbos para comprar roupa', tip='Quatro verbos: try, pick, take e fit.', items=[
        verb('try', '🧥', 'experimentar, tentar', 'I try the black jacket.', 'He tr**ies** the white shirt.', ['I try the black jacket.', 'Eu experimento a jaqueta preta.'], '**try** = experimentar. Com he/she: **tries** (y vira ies).'),
        verb('pick', '👆', 'escolher', 'I pick the pink bag.', 'She pick**s** the brown shirt.', ['I pick the pink bag.', 'Eu escolho a bolsa rosa.'], '**pick** = escolher. Com he/she: **picks**.'),
        verb('take', '🛍️', 'levar, ficar com', 'I take the purple jacket.', 'He take**s** the white one.', ['I take the purple jacket.', 'Eu levo a jaqueta roxa.'], '**take** = levar. Com he/she: **takes**.'),
        verb('fit', '📏', 'servir (tamanho)', 'The shirt fits me.', 'The jacket fit**s** him.', ['The shirt fits me.', 'A camisa serve em mim.'], '**fit** = servir. Com it/he/she: **fits**.')])
    MR = dict(
        mold=[mold('Pedir para experimentar', [('pedido', [['Can I try', 'posso experimentar']]), ('o quê', [['it on', 'isto (peça)'], ['the white one on', 'o branco'], ['the black one on', 'o preto'], ['the pink one on', 'o rosa']])], ('?', '?')),
              mold('Dizer o que gosta', [('frase', [['I like', 'eu gosto']]), ('o quê', [['the black jacket', 'da jaqueta preta'], ['the white shirt', 'da camisa branca'], ['the pink bag', 'da bolsa rosa'], ['the purple one', 'do roxo'], ['the brown one', 'do marrom']])]),
              mold('Decidir', [('frase', [["I'll take", 'eu vou levar']]), ('o quê', [['it', 'isto'], ['the black one', 'o preto'], ['the white one', 'o branco'], ['the brown one', 'o marrom']])])],
        speak=[['Can I try it on? It fits!', 'Posso experimentar? Serviu!'], ["It's a little big. I'll take the black one.", 'Está um pouco grande. Eu levo o preto.']],
        trap=[mtrap('“I\'ll take it.” quer dizer…', ['Eu vou levar.', 'Eu vou experimentar.', 'Eu vou devolver.'], 0, "**I'll take it.** = eu vou levar.", "I'll take it."),
              mtrap('Qual frase está certa?', ['Where fitting room is?', 'Where is the fitting room?', 'Where the fitting room?'], 1, 'Pergunta: **Where is the fitting room?**', 'Where is the fitting room?')],
        gap=[mgap('Where is the fitting ___?', 'Onde fica o provador?', ['room', 'rooms', 'rum'], 0, '**fitting room** = provador.', 'Where is the fitting room?'),
             mgap("It's a little ___.", 'Está um pouco grande.', ['big', 'bigs', 'bigger'], 0, "**It's a little big.** = está um pouco grande.", "It's a little big.")],
        expq=[expq('A camisa está folgada demais.', ["It's a little big.", "I'll take it.", 'Where is it?'], 0, "**It's a little big.** = está um pouco grande."),
              expq('Você quer provar uma jaqueta.', ['I like it.', 'Can I try it on?', "I'll take it."], 1, '**Can I try it on?** = posso experimentar?'),
              expq('A camisa serviu e você quer comprar.', ["It's a little big.", 'Where is the fitting room?', "I'll take it."], 2, "**I'll take it.** = eu vou levar.")],
        missions=[mission('🚪', 'No provador', 'Peça e comente o tamanho.', 'Você experimenta uma roupa. **Pergunte onde fica o provador, diga que está um pouco grande e peça o preto.**', ['Where is the fitting room?'],
                          "Where's the fitting room? It's a little big. Can I have the black one?", ['Perguntei onde fica o provador?', 'Disse que está um pouco grande?', 'Pedi o preto?'],
                          [r"\bwhere(?:['’]s| is) the fitting room\b", r'\ba little big\b', r'\bthe black one\b'],
                          [[['Where is the fitting room?', 'Onde fica o provador?']], [["It's a little big.", 'Está um pouco grande.']], [['Can I have the black one?', 'Posso ficar com o preto?']]],
                          ['Provador achado! 🚪', 'Tamanho dito! 📏', 'Cor pedida! ⚫'], ['Here is the black one.', 'Aqui está o preto.']),
                  mission('🎨', 'Minhas roupas', 'Descreva suas roupas.', 'Descreva suas roupas. **Fale de três cores (black, white, pink, purple, brown) com I like… e diga que serve com It fits.**', ['I like…'],
                          'I like the black jacket, the white shirt and the pink bag. It fits!', ['Disse I like…?', 'Citei três cores?', 'Disse It fits?'],
                          [r'\bI like\b', r'(?:\b(?:black|white|pink|purple|brown)\b[\s\S]*){3}', r'\bit fits\b'],
                          [[['I like the black jacket.', 'Eu gosto da jaqueta preta.']], [['the white shirt and the pink bag', 'a camisa branca e a bolsa rosa']], [['It fits!', 'Serviu!']]],
                          ['Gosto declarado! 👍', 'Três cores! 🌈', 'Serviu! ✅'], ['Nice colors! You look great.', 'Que cores legais! Você está ótimo.'])])
    CXs = cx(('Coal and a dark night are ___.', 'O carvão e a noite escura são pretos.', ['black', 'white', 'pink']),
             ('Snow and milk are ___.', 'A neve e o leite são brancos.', ['white', 'black', 'brown']),
             ('Strawberry milk and ballet shoes are ___.', 'O leite de morango e a sapatilha de balé são rosa.', ['pink', 'purple', 'brown']),
             ('Mix red and blue and you get ___.', 'Misture vermelho e azul e você tem roxo.', ['purple', 'pink', 'white']),
             ('Chocolate and tree trunks are ___.', 'O chocolate e os troncos de árvore são marrons.', ['brown', 'black', 'purple']),
             ('It is cold! Put on your ___ and your hat.', 'Está frio! Vista seu casaco e seu chapéu.', ['jacket', 'shirt', 'purple']))
    return dict(B=B, X=X, XT=XT, VB=VB, MR=MR, CX=CXs)


# ============================================================ 43 · The Purple Cow
COW = 'e:🐮'
GIRL43 = 'p:long:d35400:f4c7a1:e91e63:bow:dress'
FARMER = 'p:short:6b3f26:e8b48a:2e7d32:hat:shirt'


def ep43():
    B = dict(
        title='What Color Is It? · What color…?',
        sub='Perguntar a cor e escolher: gray, gold, silver, light, dark',
        pattern_label='What color is it?',
        why='Hoje você aprende a perguntar What color is it? e a escolher com I want… usando gray, gold, silver, light e dark.',
        vocab=[['Gray', 'Cinza', 'Soa como “GRÊI”.'], ['Gold', 'Dourado', 'Soa como “GÔULD”.'], ['Silver', 'Prateado', 'Soa como “SÍL-ver”.'], ['Light', 'Claro', 'Soa como “LÁIT”.'],
               ['Dark', 'Escuro', 'Soa como “DÁRK”.'], ['Flower', 'Flor', 'Soa como “FLÁU-er”.'], ['Cow', 'Vaca', 'Soa como “KÁU”.']],
        balloons=[['🐘', 'gray'], ['🥇', 'gold'], ['🥈', 'silver'], ['☀️', 'light'], ['🌑', 'dark'], ['🌸', 'flower'], ['🐄', 'cow']],
        cover_art=dict(s='park2', items=[['🐄', 104, 56, 20, 'bob'], ['🌸', 138, 44, 12, 'bob'], ['🎨', 84, 34, 12, 'bob']], seed='pc1'),
        cover_sub='What color is it? Em 10 minutos você pergunta e escolhe cores',
        cover_say='Uma menina encontra uma vaca na fazenda. Mas de que cor ela é? Cinza? Dourada? Ou será roxa, como no poema famoso?',
        wrap_recap=[['What color is it?', 'De que cor é?'], ["It's light blue.", 'É azul claro.'], ['I want the silver one.', 'Eu quero o prateado.'], ['Gray or gold?', 'Cinza ou dourado?']],
        teaser=dict(t='The Golden Touch', d='Próximo padrão: Paint it gold! (verbo + it + cor)'),
        cast={'Girl': ['👧', '#e91e63'], 'Farmer': ['👨‍🌾', '#2e7d32'], 'Cow': ['🐮', '#8e44ad']},
        lines=[['Girl', 'Look, a cow! What color is it?', 'Olhe, uma vaca! De que cor ela é?'],
               ['Farmer', "It's gray. But the flower is purple.", 'Ela é cinza. Mas a flor é roxa.'],
               ['Girl', 'And the bell? What color is it?', 'E o sino? De que cor ele é?'],
               ['Farmer', "It's gold. The cow likes gold.", 'É dourado. A vaca gosta de dourado.'],
               ['Cow', 'Moo! I want a silver bell!', 'Mu! Eu quero um sino prateado!'],
               ['Girl', 'Is the flower light or dark?', 'A flor é clara ou escura?'],
               ['Farmer', "It's light purple. A purple cow! Ha ha!", 'É roxo claro. Uma vaca roxa! Ha ha!'],
               ['Cow', "Moo! I'm a purple cow today!", 'Mu! Hoje eu sou uma vaca roxa!']],
        quiz=[quiz('What color is the cow?', 'De que cor é a vaca?', [['🟣', 'Purple'], ['🐘', 'Gray'], ['🥇', 'Gold']], 1, 1, 'O fazendeiro diz: “It’s gray.”'),
              quiz('What color is the bell?', 'De que cor é o sino?', [['🥈', 'Silver'], ['🔵', 'Blue'], ['🥇', 'Gold']], 2, 3, 'O fazendeiro diz: “It’s gold.”'),
              quiz('What does the cow want?', 'O que a vaca quer?', [['🥈', 'A silver bell'], ['🥇', 'A gold bell'], ['🌸', 'A flower']], 0, 4, 'A vaca diz: “I want a silver bell!”')],
        rdg_q=dict(q='Como dizer “azul claro” em inglês?', o=['blue light', 'light blue', 'lightly blue'], a=1, why='Em inglês **light** (claro) vem antes da cor: light blue.'),
        dictate=[['What color is it?', 'De que cor é?'], ["It's light blue.", 'É azul claro.'], ['I want the silver one.', 'Eu quero o prateado.'], ['Gray or gold?', 'Cinza ou dourado?']],
        produce=produce('A menina pergunta: *What color is it?* **Responda com It’s e uma cor (gray, gold, silver, light ou dark), diga qual você quer com I want… e pergunte a cor favorita dela.**',
                        "Ex.: It's light blue. I want the silver one. What's your favorite color?", ["It's…", 'I want…', "What's your favorite color?"],
                        "It's light blue. I want the silver one. What's your favorite color?",
                        ['Respondi com It’s + cor?', 'Disse o que eu quero?', 'Perguntei a cor favorita dela?'],
                        [r"\bit(?:['’]s| is)\s+(?:an? )?(?:light |dark )?(?:gray|gold|silver|blue|red|green|yellow|orange|purple|pink|brown|black|white)\b", r'\bI want\b', r"\bwhat(?:['’]s| is) your favorite color\b"],
                        [[["It's gray.", 'É cinza.'], ["It's dark blue.", 'É azul escuro.']], [['I want the gold one.', 'Eu quero o dourado.']], [["What's your favorite color?", 'Qual é a sua cor favorita?']]],
                        ['Cor dita! 🎨', 'Desejo dito! ⭐', 'Boa pergunta! ❓'],
                        ['My favorite color is purple, of course!', 'Minha cor favorita é roxo, claro!']),
        rs=RSD('park2', 'yard', 'park', 'market', 'lake', 'shop', 'street'),
        sc='park2')
    X = dict(
        n=30008, review=True, names=('Girl', 'Farmer'),
        stage=dict(rs='park2', chars=[[GIRL43, 28, 0, 0.9], [FARMER, 56, 1, 1.0], [COW, 84, 1, 1.0]]),
        obra=dict(name='The Purple Cow', kind='📜 Poema curto · 1895', year='1895',
                  text='Poema curto do humorista americano Gelett Burgess, de 1895. Em quatro versos ele diz que nunca viu uma vaca roxa e nem quer ver, mas prefere ver uma a ser uma! É uma brincadeira famosa com cores.',
                  line=['I never saw a Purple Cow.', 'Eu nunca vi uma vaca roxa. (primeiro verso; saw = vi)'],
                  pa=dict(t='barn', e=['🐄', '🌸', '🎨'], p='h', v=1)),
        gancho=['Girl', 'Look, a cow! What color is it?', 'Olhe, uma vaca! De que cor ela é?'],
        hot=[hot('🐘', 14, 16, 'gray', 'cinza', "It's a gray elephant.", 'É um elefante cinza.'),
             hot('🥇', 40, 14, 'gold', 'dourado', "It's a gold medal.", 'É uma medalha dourada.'),
             hot('🥈', 66, 14, 'silver', 'prateado', "It's a silver medal.", 'É uma medalha prateada.'),
             hot('🌸', 88, 16, 'flower', 'flor', "It's a light pink flower.", 'É uma flor rosa clara.'),
             hot('🌑', 12, 82, 'dark', 'escuro', 'The night is dark.', 'A noite é escura.')],
        gap=[gap('What ___ is it?', 'De que cor é?', ['color', 'colors', 'colored'], 0, 'A pergunta é **What color** is it? (cor no singular).'),
             gap("It's ___ blue.", 'É azul claro.', ['lightly', 'light', 'lighter'], 1, '**light blue** = azul claro: o light vem antes da cor.'),
             gap('I ___ the silver one.', 'Eu quero o prateado.', ['wants', 'want', 'wanting'], 1, 'Com **I** o verbo não leva s: I **want**.'),
             gap('Gray ___ gold?', 'Cinza ou dourado?', ['and', 'but', 'or'], 2, 'Para escolher entre duas opções: **or**.')],
        trap=[trap(['What is color it?', 'What color is it?', 'What it is color?'], 1, 'Ordem certa: **What color is it?**'),
              trap(['I want the one silver.', 'I want the silver one.', 'I want silver the one.'], 1, 'Em inglês: the + cor + **one**.')],
        sticker=dict(title='A vaca roxa', sub='The Purple Cow · 1895', rs='park2', chars=[[GIRL43, 34, 0, 0.9], [COW, 68, 1, 1.0]]),
        speakers={'Girl': GIRL43, 'Farmer': FARMER, 'Cow': COW},
        rule=dict(
            who=GIRL43, head='What color is it?', sub='Perguntar a cor e escolher.',
            say=['What color is it?', 'De que cor é?'],
            formula=[dict(from_=[['It', 0], ['is', 1], ['blue.', 3]], to=[["It's", 2], ['light', 0], ['blue.', 3]], say="It's light blue.", note='**light** (claro) e **dark** (escuro) vêm **antes** da cor.'),
                     dict(from_=[['The cow', 0], ['is', 1], ['gray.', 3]], to=[['What', 1], ['color', 3], ['is', 1], ['the cow?', 0]], say='What color is the cow?', note='Para perguntar a cor: **What color** + is + a coisa?')],
            uses=[dict(ico='❓', tag='Perguntar', en='What color is it?', pt='De que cor é?'),
                  dict(ico='🐘', tag='Responder', en="It's gray.", pt='É cinza.'),
                  dict(ico='🌗', tag='Claro/escuro', en='A dark blue shirt.', pt='Uma camisa azul escura.'),
                  dict(ico='⭐', tag='Querer', en='I want a silver star.', pt='Eu quero uma estrela prateada.')],
            rules=[dict(tag='What color', c=0, text='Pergunta pela cor de algo.', ex='What color is the cow?'),
                   dict(tag='light / dark', c=1, text='Vêm **antes** da cor.', ex='✗ blue light  →  ✓ light blue'),
                   dict(tag='I want', c=2, text='Para dizer o que você quer.', ex='I want the silver one.')],
            tips=['Em português a cor vem depois: “azul claro”. Em inglês, **light** vem antes: **light blue**.']),
        mission_ic='🐄')
    XT = dict(
        exp=[exp('💖', "What's your favorite color?", 'Expressão', 'Qual é a sua cor favorita?', 'Para **conhecer o gosto** de alguém.', ["What's your favorite color?", 'Qual é a sua cor favorita?']),
             exp('🤷', "I can't decide.", 'Expressão', 'Não consigo decidir.', 'Quando você tem **duas boas opções**.', ["Gray or gold? I can't decide.", 'Cinza ou dourado? Não consigo decidir.']),
             exp('🎯', "It's a perfect match!", 'Expressão', 'Combinou perfeitamente!', 'Quando duas coisas **combinam muito bem**.', ["Silver and blue? It's a perfect match!", 'Prateado e azul? Combinou perfeitamente!']),
             exp('👌', 'Either one is fine.', 'Expressão', 'Qualquer um serve.', 'Quando **tanto faz** qual escolher.', ['Gray or gold? Either one is fine.', 'Cinza ou dourado? Qualquer um serve.'])],
        exp_scene=dict(rs='park', lines=[
            ['Girl', "**What's your favorite color**, cow?", 'Qual é a sua cor favorita, vaca?'],
            ['Cow', 'Moo! Gray or gold? **I can\'t decide**.', 'Mu! Cinza ou dourado? Não consigo decidir.'],
            ['Farmer', '**Either one is fine**, my friend.', 'Qualquer um serve, minha amiga.'],
            ['Girl', 'Look! A gold bell and a gray cow.', 'Olhe! Um sino dourado e uma vaca cinza.'],
            ['Farmer', "**It's a perfect match**!", 'Combinou perfeitamente!'],
            ['Cow', 'Moo! I love it!', 'Mu! Eu adorei!']]),
        lab=dict(
            short='k × g', title='Laboratório de sons: k × g',
            say='Cold ou gold? Cap ou gap? Vamos treinar a diferença entre “k” e “g” com a vaca!',
            intro=dict(what='O **k** de **cold** e o **g** de **gold** nascem no mesmo lugar da boca, mas o **g** usa a voz e o **k** só ar.',
                       how='No **k**, solte um sopro forte de ar, sem voz. No **g**, ligue a voz na garganta, como num “gá” suave.',
                       pt='Em português o “c” de casa e o “g” de gato são parecidos com os ingleses, mas o **k** inglês é mais forte (aspirado). Cuidado: **gold** (ouro) ≠ **cold** (frio).'),
            ex=[['gold', 'GÔULD', 'dourado', 'voz ligada no começo'], ['gray', 'GRÊI', 'cinza', 'voz ligada no “g”'], ['cow', 'KÁU', 'vaca', 'sopro forte no “k”']],
            pairs=[['gold', 'cold', '“dourado” × “frio”'], ['goat', 'coat', '“cabra” × “casaco”'], ['gap', 'cap', '“fenda” × “boné”']],
            tip='Ponha a mão na garganta: no “g” ela vibra, no “k” não.',
            phrase=['The gray goat has a gold coat.', 'A cabra cinza tem um casaco dourado.'],
            rounds=[rnd('cold', ['gold', 'cold'], 1, '**Cold** (frio) começa com “k”: sopro forte, sem voz.'),
                    rnd('goat', ['goat', 'coat'], 0, '**Goat** (cabra) começa com “g”: voz ligada.'),
                    rnd('cap', ['gap', 'cap'], 1, '**Cap** (boné) começa com “k”. **Gap** começa com “g”.')]),
        hunt=[ht('gold', ['gold', 'cold'], 0, '**gold** = dourado, com “g” de voz ligada.'), hp('coat', ['🧥', '🐐', '🌸'], 0, '**coat** = casaco, começa com “k”.'),
              ht('goat', ['goat', 'coat'], 0, '**goat** = cabra, começa com “g”.'), ht('cap', ['gap', 'cap'], 1, '**cap** = boné, começa com “k”.')])
    VB = dict(title='Verbos para escolher cores', tip='Quatro verbos: choose, want, decide e match.', items=[
        verb('choose', '👆', 'escolher', 'I choose the gold one.', 'She choos**es** the silver one.', ['I choose the gold one.', 'Eu escolho o dourado.'], '**choose** = escolher. Com he/she: **chooses**.'),
        verb('want', '🙋', 'querer', 'I want a silver bell.', 'The cow want**s** a bell.', ['I want a silver bell.', 'Eu quero um sino prateado.'], '**want** = querer. Com he/she: **wants**.'),
        verb('decide', '🤔', 'decidir', 'I decide now.', 'He decide**s** fast.', ['I decide now.', 'Eu decido agora.'], '**decide** = decidir. Com he/she: **decides**.'),
        verb('match', '🎯', 'combinar', 'Gray and gold match.', 'This color match**es** my shirt.', ['Gray and gold match.', 'Cinza e dourado combinam.'], '**match** = combinar. Com he/she/it: **matches** (terminou em ch: ponha es).')])
    MR = dict(
        mold=[mold('Perguntar a cor', [('pergunta', [['What color is', 'de que cor é']]), ('coisa', [['it', 'isto'], ['the cow', 'a vaca'], ['the flower', 'a flor'], ['your bag', 'a sua bolsa'], ['the bell', 'o sino']])], ('?', '?')),
              mold('Responder com a cor', [('frase', [["It's", 'é']]), ('tom', [['light', 'claro'], ['dark', 'escuro'], ['—', '(só a cor)']]), ('cor', [['gray', 'cinza'], ['gold', 'dourado'], ['silver', 'prateado'], ['blue', 'azul'], ['green', 'verde']])]),
              mold('Escolher', [('frase', [['I want the', 'eu quero o']]), ('cor', [['gray', 'cinza'], ['gold', 'dourado'], ['silver', 'prateado'], ['dark blue', 'azul escuro'], ['light green', 'verde claro']]), ('one', [['one', '(o)']])])],
        speak=[["What color is it? It's light blue.", 'De que cor é? É azul claro.'], ["Gray or gold? I can't decide.", 'Cinza ou dourado? Não consigo decidir.']],
        trap=[mtrap('“Either one is fine.” quer dizer…', ['Qualquer um serve.', 'Nenhum serve.', 'Os dois são caros.'], 0, '**Either one is fine.** = qualquer um serve.', 'Either one is fine.'),
              mtrap('Qual frase está certa?', ['What your favorite color is?', "What's your favorite color?", "What's favorite your color?"], 1, 'Ordem certa: **What’s your favorite color?**', "What's your favorite color?")],
        gap=[mgap("It's a perfect ___!", 'Combinou perfeitamente!', ['match', 'matches', 'matching'], 0, "**It's a perfect match!** = combinou perfeitamente!", "It's a perfect match!"),
             mgap('I can\'t ___.', 'Não consigo decidir.', ['decide', 'decides', 'decision'], 0, 'Depois de **can’t** o verbo fica simples: can’t **decide**.', "I can't decide.")],
        expq=[expq('Você não sabe se escolhe cinza ou dourado.', ["I can't decide.", "It's a perfect match!", 'Either one is fine.'], 0, "**I can't decide.** = não consigo decidir."),
              expq('Alguém pergunta qual cor você prefere e você acha tanto faz.', ['Either one is fine.', "What's your favorite color?", "I can't decide."], 0, '**Either one is fine.** = qualquer um serve.'),
              expq('Você conhece uma pessoa nova e quer saber o gosto dela.', ["It's a perfect match!", "What's your favorite color?", 'Either one is fine.'], 1, "**What's your favorite color?** pergunta a cor favorita.")],
        missions=[mission('🤷', 'Escolha difícil', 'Escolha entre duas cores.', 'Você não sabe escolher entre duas cores. **Pergunte Gray or gold?, diga I can’t decide e escolha uma com I want…**', ['Gray or gold?'],
                          "Gray or gold? I can't decide. I want the gold one.", ['Perguntei a opção com or?', 'Disse que não consigo decidir?', 'Escolhi com I want?'],
                          [r'\b(?:gray|gold|silver|blue)\s+or\s+(?:gray|gold|silver|blue)\b', r"\bI can['’]t decide\b", r'\bI want\b'],
                          [[['Gray or gold?', 'Cinza ou dourado?']], [["I can't decide.", 'Não consigo decidir.']], [['I want the gold one.', 'Eu quero o dourado.']]],
                          ['Opção com or! 🔀', 'Dúvida dita! 🤷', 'Escolha feita! ⭐'], ['Gold is great!', 'Dourado é ótimo!']),
                  mission('💖', 'Minha cor favorita', 'Fale da sua cor.', '**Diga qual é a sua cor favorita, diga se ela é clara ou escura e diga o que você tem dessa cor.**', ['My favorite color is…'],
                          'My favorite color is blue. It is dark blue. I have a dark blue jacket.', ['Disse a cor favorita?', 'Disse se é clara ou escura?', 'Disse o que tenho dessa cor?'],
                          [r'\bmy favorite color is\b', r'\b(?:light|dark)\b', r'\bI have\b'],
                          [[['My favorite color is blue.', 'Minha cor favorita é azul.']], [['It is dark blue.', 'É azul escuro.']], [['I have a dark blue jacket.', 'Eu tenho uma jaqueta azul escura.']]],
                          ['Cor favorita! 💖', 'Claro ou escuro! 🌗', 'Seu objeto! 🧥'], ['Nice! That is a great color.', 'Legal! É uma cor ótima.'])])
    CXs = cx(('Elephants and rain clouds are ___.', 'Os elefantes e as nuvens de chuva são cinza.', ['gray', 'gold', 'dark']),
             ('The first-place medal is ___.', 'A medalha do primeiro lugar é dourada.', ['gold', 'silver', 'gray']),
             ('The second-place medal is ___.', 'A medalha do segundo lugar é prateada.', ['silver', 'gold', 'dark']),
             ('It is not dark blue. It is a ___ blue, like the morning sky.', 'Não é azul escuro. É um azul claro, como o céu da manhã.', ['light', 'dark', 'gray']),
             ('At night my room is very ___. I cannot see.', 'À noite meu quarto é muito escuro. Eu não enxergo.', ['dark', 'light', 'gold']),
             ('A rose is a red ___.', 'Uma rosa é uma flor vermelha.', ['flower', 'cow', 'silver']))
    return dict(B=B, X=X, XT=XT, VB=VB, MR=MR, CX=CXs)


# ============================================================ 44 · The Golden Touch
MIDAS = 'p:short:b8860b:f4c7a1:6a1b9a:crown:suit'
MARYGOLD = 'p:long:f1c40f:f4c7a1:e67e22:bow:dress'
PAINTER = 'p:curly:2d2d2d:e8b48a:3498db:hat:shirt'
COLORS = r'(?:gold|blue|white|green|red|yellow|silver|gray|pink|purple|brown|black|orange)'


def ep44():
    B = dict(
        title='Paint It Gold · Paint it + cor',
        sub='Mandar pintar: Paint it gold! Paint the wall blue! E falar de tinta, pincel, parede, céu e estrela',
        pattern_label='Paint it + cor',
        why='Hoje você aprende a dar ordens simples como o rei Midas: Paint it gold! Paint the wall blue! E a dizer Let me paint.',
        vocab=[['Paint', 'Tinta, pintar', 'Soa como “PÊINT”.'], ['Brush', 'Pincel', 'Soa como “BRÂSH”.'], ['Wall', 'Parede', 'Soa como “UÓL”.'],
               ['Sky', 'Céu', 'Soa como “SKÁI”.'], ['Picture', 'Quadro, desenho', 'Soa como “PÍK-tcher”.'], ['Star', 'Estrela', 'Soa como “STÁR”.']],
        balloons=[['🎨', 'paint'], ['🖌️', 'brush'], ['🧱', 'wall'], ['🌤️', 'sky'], ['🖼️', 'picture'], ['⭐', 'star']],
        cover_art=dict(s='park2', items=[['👑', 104, 56, 20, 'bob'], ['🖌️', 138, 44, 12, 'bob'], ['⭐', 84, 34, 12, 'bob']], seed='gt1'),
        cover_sub='Paint it gold! Em 10 minutos você manda pintar tudo da cor que quiser',
        cover_say='O rei Midas ama o ouro! Ele chama um pintor e quer tudo dourado: a parede, a estrela e até o céu. Será que a filha dele concorda?',
        wrap_recap=[['Paint it gold!', 'Pinte de dourado!'], ['Paint the wall blue.', 'Pinte a parede de azul.'], ['Let me paint the sky.', 'Deixe-me pintar o céu.'], ['The star is gold.', 'A estrela é dourada.']],
        teaser=dict(t='Around the World in Eighty Days', d='Próximo padrão: Where’s the…? (onde fica?)'),
        cast={'Midas': ['👑', '#b8860b'], 'Marygold': ['👧', '#e67e22'], 'Painter': ['🎨', '#3498db']},
        lines=[['Midas', 'Painter, paint the wall gold!', 'Pintor, pinte a parede de dourado!'],
               ['Painter', 'Gold? Do you want the sky gold too?', 'Dourado? O senhor quer o céu dourado também?'],
               ['Midas', 'Yes! Paint it gold! Paint the star too!', 'Sim! Pinte de dourado! Pinte a estrela também!'],
               ['Marygold', 'Papa, no! Let me paint the sky blue.', 'Papai, não! Deixe-me pintar o céu de azul.'],
               ['Midas', 'Hmm. Blue is nice. Paint it blue.', 'Hum. Azul é bonito. Pinte de azul.'],
               ['Painter', 'Here is the picture. The star is gold.', 'Aqui está o quadro. A estrela é dourada.'],
               ['Marygold', 'I love it! The wall is gold, the sky is blue.', 'Eu adorei! A parede é dourada, o céu é azul.'],
               ['Midas', 'Perfect! Gold and blue, a picture for a king.', 'Perfeito! Dourado e azul, um quadro digno de um rei.']],
        quiz=[quiz('The first gold thing is…', 'A primeira coisa dourada é…', [['🧱', 'The wall'], ['🌤️', 'The sky'], ['🚪', 'The door']], 0, 0, 'Midas diz: “paint the wall gold!”'),
              quiz('What color is the sky at the end?', 'De que cor é o céu no final?', [['🥇', 'Gold'], ['🔵', 'Blue'], ['⚪', 'White']], 1, 4, 'Midas aceita: “Paint it blue.”'),
              quiz('What is gold in the picture?', 'O que é dourado no quadro?', [['🌤️', 'The sky'], ['🧱', 'The brush'], ['⭐', 'The star']], 2, 5, 'O pintor diz: “The star is gold.”')],
        rdg_q=dict(q='Como mandar pintar a parede de azul?', o=['Paint blue the wall.', 'Paint the wall blue.', 'Paint the blue wall of.'], a=1, why='Ordem simples: Paint + **o quê** + **cor**: Paint the wall blue.'),
        dictate=[['Paint it gold!', 'Pinte de dourado!'], ['Paint the wall blue.', 'Pinte a parede de azul.'], ['Let me paint the sky.', 'Deixe-me pintar o céu.'], ['The star is gold.', 'A estrela é dourada.']],
        produce=produce('O pintor pergunta: *What color is the wall?* **Mande pintar algo com Paint it + cor, diga uma cor para o céu com The sky is… e peça para ver o quadro com Show me the picture.**',
                        'Ex.: Paint it gold! The sky is blue. Show me the picture, please.', ['Paint it…', 'The sky is…', 'Show me…'],
                        'Paint it gold! The sky is blue. Show me the picture, please.',
                        ['Mandei pintar com Paint it + cor?', 'Disse a cor do céu?', 'Pedi para ver o quadro?'],
                        [r'\bpaint (?:it|the \w+) ' + COLORS + r'\b', r'\bthe sky is\s+\w+', r'\bshow me\b'],
                        [[['Paint it gold!', 'Pinte de dourado!'], ['Paint the wall blue.', 'Pinte a parede de azul.']], [['The sky is blue.', 'O céu é azul.']], [['Show me the picture.', 'Mostre-me o quadro.']]],
                        ['Ordem dada! 🖌️', 'Céu descrito! 🌤️', 'Quadro pedido! 🖼️'],
                        ['Here is the picture! Do you like it?', 'Aqui está o quadro! Você gostou?']),
        rs=RSD('park2', 'yard', 'home1', 'school', 'living', 'lobby2', 'park'),
        sc='park2')
    X = dict(
        n=70016, review=True, names=('Midas', 'Painter'),
        stage=dict(rs='park2', chars=[[MIDAS, 28, 0, 1.0], [PAINTER, 56, 1, 1.0], [MARYGOLD, 84, 1, 0.85]]),
        obra=dict(name='The Golden Touch', kind='📖 Conto · 1851', year='1851',
                  text='Conto do escritor americano Nathaniel Hawthorne, de 1851, que recria o mito grego do rei Midas. O rei ganha o poder de transformar em ouro tudo o que toca, e aprende que ouro não é tudo na vida.',
                  line=['Paint it gold!', 'Pinte de dourado! (frase do tema do conto)'],
                  pa=dict(t='artstudio', e=['👑', '🖌️', '⭐'], p='b', v=0)),
        gancho=['Midas', 'Painter, paint the wall gold!', 'Pintor, pinte a parede de dourado!'],
        hot=[hot('🎨', 14, 16, 'paint', 'tinta', 'Paint it gold!', 'Pinte de dourado!'),
             hot('🖌️', 40, 14, 'brush', 'pincel', 'Give me the brush, please.', 'Me dê o pincel, por favor.'),
             hot('🧱', 66, 14, 'wall', 'parede', 'Paint the wall blue.', 'Pinte a parede de azul.'),
             hot('🌤️', 88, 16, 'sky', 'céu', 'The sky is blue.', 'O céu é azul.'),
             hot('⭐', 12, 82, 'star', 'estrela', 'Paint the star gold.', 'Pinte a estrela de dourado.')],
        gap=[gap('Paint the wall ___!', 'Pinte a parede de dourado!', ['gold', 'golds', 'of gold the'], 0, 'A cor vem no final: Paint the wall **gold**.'),
             gap('Paint ___ blue.', 'Pinte de azul. (o céu)', ['they', 'it', 'is'], 1, '**it** substitui o nome: Paint **it** blue.'),
             gap('Let me ___ the sky.', 'Deixe-me pintar o céu.', ['painting', 'paints', 'paint'], 2, 'Depois de **Let me** o verbo fica simples: Let me **paint**.'),
             gap('The star ___ gold.', 'A estrela é dourada.', ['are', 'is', 'am'], 1, 'Com **the star** (uma só), o verbo é **is**.')],
        trap=[trap(['Paint gold the wall.', 'Paint the gold wall of.', 'Paint the wall gold.'], 2, 'Ordem: Paint + **a parede** + **cor**.'),
              trap(['Let me to paint.', 'Let me paint.', 'Let me painting.'], 1, 'Depois de **Let me** não se usa **to**: Let me paint.')],
        sticker=dict(title='O rei e o pintor', sub='The Golden Touch · 1851', rs='park2', chars=[[MIDAS, 34, 0, 1.0], [PAINTER, 68, 1, 1.0]]),
        speakers={'Midas': MIDAS, 'Marygold': MARYGOLD, 'Painter': PAINTER},
        rule=dict(
            who=MIDAS, head='Paint it + cor', sub='Mandar pintar e dizer a cor.',
            say=['Paint it gold!', 'Pinte de dourado!'],
            formula=[dict(from_=[['Paint', 1], ['the wall', 3], ['gold.', 2]], to=[['Paint', 1], ['it', 0], ['gold!', 2]], say='Paint it gold!', note='**it** substitui o nome (the wall). A cor vem depois.'),
                     dict(from_=[['I paint', 1], ['the sky.', 3]], to=[['Let me', 0], ['paint', 1], ['the sky.', 3]], say='Let me paint the sky.', note='**Let me** + verbo simples = deixe-me fazer.')],
            uses=[dict(ico='🖌️', tag='Mandar', en='Paint it gold!', pt='Pinte de dourado!'),
                  dict(ico='🧱', tag='Dizer o quê', en='Paint the wall blue.', pt='Pinte a parede de azul.'),
                  dict(ico='🙋', tag='Pedir para fazer', en='Let me paint the sky.', pt='Deixe-me pintar o céu.'),
                  dict(ico='⭐', tag='Descrever', en='The star is gold.', pt='A estrela é dourada.')],
            rules=[dict(tag='Paint + cor', c=0, text='Mande pintar: **Paint** + o quê + **cor**.', ex='Paint the wall gold.'),
                   dict(tag='it', c=1, text='Para não repetir o nome, use **it**.', ex='Paint the wall gold. → Paint it gold.'),
                   dict(tag='Let me', c=2, text='**Let me** + verbo simples, sem “to”.', ex='✗ Let me to paint  →  ✓ Let me paint')],
            tips=['Em português dizemos “pinte de dourado” (com “de”). Em inglês não há “de”: Paint it **gold**.']),
        mission_ic='🖌️')
    XT = dict(
        exp=[exp('😊', 'Looks good to me.', 'Expressão', 'Para mim está bom.', 'Quando você **aprova** o que viu.', ['The wall is gold? Looks good to me.', 'A parede é dourada? Para mim está bom.']),
             exp('🤔', 'Let me think about it.', 'Expressão', 'Deixe-me pensar sobre isso.', 'Quando você precisa de **tempo** para decidir.', ['Gold or blue? Let me think about it.', 'Dourado ou azul? Deixe-me pensar sobre isso.']),
             exp('✋', "Don't touch!", 'Expressão', 'Não toque!', 'Aviso para **não encostar** em algo.', ["Don't touch! The paint is wet.", 'Não toque! A tinta está molhada.']),
             exp('⚠️', 'Be careful!', 'Expressão', 'Tenha cuidado!', 'Para **alertar** sobre um perigo.', ['Be careful with the brush!', 'Cuidado com o pincel!'])],
        exp_scene=dict(rs='park2', lines=[
            ['Midas', 'Painter, **let me think about it**. Gold or blue?', 'Pintor, deixe-me pensar sobre isso. Dourado ou azul?'],
            ['Painter', '**Be careful**! The paint is wet.', 'Cuidado! A tinta está molhada.'],
            ['Marygold', "**Don't touch**, Papa!", 'Não toque, papai!'],
            ['Midas', 'Oh, sorry. The wall is gold.', 'Ah, desculpe. A parede é dourada.'],
            ['Painter', 'And the sky is blue. **Looks good to me**.', 'E o céu é azul. Para mim está bom.'],
            ['Marygold', 'Yes! I love it!', 'Sim! Eu adorei!']]),
        lab=dict(
            short='u de brush', title='Laboratório de sons: o “u” de brush',
            say='O som de “u” em brush, cup e luck não existe em português. Vamos treinar com o pincel!',
            intro=dict(what='O **u** de **brush**, **cup** e **luck** é um som curto e neutro, entre o “â” e o “a” da nossa boca.',
                       how='Deixe a boca relaxada e meio aberta, a língua parada embaixo, e diga um “â” curto: BRÂSH, CÂP, LÂK.',
                       pt='Em português a gente tende a dizer “u” de “bruxa”. Em inglês é um “â” curto. Cuidado: **luck** (sorte) ≠ **lock** (trancar); **duck** (pato) ≠ **dock** (doca).'),
            ex=[['brush', 'BRÂSH', 'pincel', 'boca relaxada, som curto'], ['cup', 'KÂP', 'xícara', 'não faça “u” redondo'], ['luck', 'LÂK', 'sorte', 'som curto e neutro']],
            pairs=[['duck', 'dock', '“pato” × “doca”'], ['luck', 'lock', '“sorte” × “trancar”'], ['hut', 'hot', '“cabana” × “quente”']],
            tip='Relaxe a boca como se fosse um “â” de surpresa, bem curtinho.',
            phrase=['The duck has a gold cup.', 'O pato tem uma xícara dourada.'],
            rounds=[rnd('duck', ['duck', 'dock'], 0, '**Duck** (pato) tem som curto de “â”. **Dock** (doca) tem “ó”.'),
                    rnd('lock', ['luck', 'lock'], 1, '**Lock** (trancar) tem “ó”. **Luck** (sorte) tem “â”.'),
                    rnd('hot', ['hut', 'hot'], 1, '**Hot** (quente) tem “ó”. **Hut** (cabana) tem “â”.')]),
        hunt=[ht('luck', ['luck', 'lock'], 0, '**luck** = sorte, com “â” curto.'), hp('duck', ['🦆', '⚓', '🔒'], 0, '**duck** = pato, com “â” curto.'),
              ht('dock', ['duck', 'dock'], 1, '**dock** = doca, com “ó”.'), ht('hut', ['hut', 'hot'], 0, '**hut** = cabana, com “â” curto.')])
    VB = dict(title='Verbos para pintar', tip='Quatro verbos: paint, mix, draw e show.', items=[
        verb('paint', '🖌️', 'pintar', 'I paint the wall.', 'The painter paint**s** the sky.', ['I paint the wall.', 'Eu pinto a parede.'], '**paint** = pintar. Com he/she: **paints**.'),
        verb('mix', '🥣', 'misturar', 'I mix blue and white.', 'She mix**es** red and yellow.', ['I mix blue and white.', 'Eu misturo azul e branco.'], '**mix** = misturar. Com he/she: **mixes** (terminou em x: ponha es).'),
        verb('draw', '✏️', 'desenhar', 'I draw a gold star.', 'He draw**s** a big picture.', ['I draw a gold star.', 'Eu desenho uma estrela dourada.'], '**draw** = desenhar. Com he/she: **draws**.'),
        verb('show', '🖼️', 'mostrar', 'I show the picture.', 'The painter show**s** the wall.', ['I show the picture.', 'Eu mostro o quadro.'], '**show** = mostrar. Com he/she: **shows**.')])
    MR = dict(
        mold=[mold('Mandar pintar', [('verbo', [['Paint', 'pinte']]), ('o quê', [['it', '(isso)'], ['the wall', 'a parede'], ['the sky', 'o céu'], ['the star', 'a estrela']]),
                                    ('cor', [['gold', 'dourado'], ['blue', 'azul'], ['white', 'branco'], ['green', 'verde'], ['red', 'vermelho']])], ('!', '!')),
              mold('Dizer a cor', [('coisa', [['The sky is', 'o céu é'], ['The wall is', 'a parede é'], ['The star is', 'a estrela é'], ['The picture is', 'o quadro é']]),
                                   ('cor', [['blue', 'azul'], ['gold', 'dourado'], ['white', 'branco'], ['gray', 'cinza']])]),
              mold('Pedir', [('pedido', [['Give me', 'me dê'], ['Show me', 'me mostre'], ['Let me paint', 'deixe-me pintar']]), ('o quê', [['the brush', 'o pincel'], ['the picture', 'o quadro'], ['the wall', 'a parede']])], ('.', '.'))],
        speak=[['Paint it gold! Looks good to me.', 'Pinte de dourado! Para mim está bom.'], ["Be careful! Don't touch!", 'Cuidado! Não toque!']],
        trap=[mtrap('“Be careful!” quer dizer…', ['Cuidado!', 'Bom dia!', 'Boa sorte!'], 0, '**Be careful!** = tenha cuidado!', 'Be careful!'),
              mtrap('Qual frase está certa?', ['Looks good for me.', 'Look good to me.', 'Looks good to me.'], 2, 'Expressão fixa: **Looks good to me.**', 'Looks good to me.')],
        gap=[mgap("Don't ___!", 'Não toque!', ['touch', 'touches', 'touching'], 0, 'Depois de **Don’t** o verbo fica simples: Don’t **touch**.', "Don't touch!"),
             mgap('Let me ___ about it.', 'Deixe-me pensar sobre isso.', ['think', 'thinks', 'to think'], 0, 'Depois de **Let me** o verbo fica simples: Let me **think**.', 'Let me think about it.')],
        expq=[expq('O pintor mostra a parede pronta e você aprova.', ['Looks good to me.', "Don't touch!", 'Be careful!'], 0, '**Looks good to me.** = para mim está bom.'),
              expq('A tinta ainda está molhada e uma criança vai encostar.', ["Don't touch!", 'Looks good to me.', 'Let me think.'], 0, "**Don't touch!** = não toque!"),
              expq('Você ainda não sabe a cor da parede.', ['Looks good to me.', 'Let me think about it.', 'Be careful!'], 1, '**Let me think about it.** = deixe-me pensar.')],
        missions=[mission('🧱', 'Parede nova', 'Peça material e mande pintar.', 'Você vai pintar o quarto. **Peça a tinta e o pincel com Give me…, mande pintar a parede e diga a cor que você quer.**', ['Give me…'],
                          'Give me the paint and the brush, please. Paint the wall blue.', ['Pedi o material com Give me?', 'Mandei pintar?', 'Disse a cor?'],
                          [r'\bgive me\b', r'\bpaint\b', r'\b' + COLORS + r'\b'],
                          [[['Give me the brush, please.', 'Me dê o pincel, por favor.']], [['Paint the wall.', 'Pinte a parede.']], [['blue', 'azul'], ['gold', 'dourado']]],
                          ['Material pedido! 🎨', 'Ordem dada! 🖌️', 'Cor escolhida! 🔵'], ['OK! Here is the paint.', 'Certo! Aqui está a tinta.']),
                  mission('🖼️', 'Desenho do céu', 'Descreva um desenho.', '**Descreva um desenho: a cor do céu, uma estrela e a parede, com The … is ….**', ['The sky is…'],
                          'The sky is blue. The star is gold. The wall is white.', ['Descrevi o céu?', 'Falei da estrela?', 'Falei da parede?'],
                          [r'\bthe sky is\b', r'\bstar\b', r'\bthe wall is\b'],
                          [[['The sky is blue.', 'O céu é azul.']], [['The star is gold.', 'A estrela é dourada.']], [['The wall is white.', 'A parede é branca.']]],
                          ['Céu descrito! 🌤️', 'Estrela citada! ⭐', 'Parede citada! 🧱'], ['What a nice picture!', 'Que desenho bonito!'])])
    CXs = cx(('I need ___ for the wall. A can of white.', 'Preciso de tinta para a parede. Uma lata de branca.', ['paint', 'brush', 'star']),
             ('You use a ___ to paint. It has a handle and soft hairs.', 'Você usa um pincel para pintar. Tem cabo e pelos macios.', ['brush', 'picture', 'wall']),
             ('The picture is on the ___. It is white.', 'O quadro está na parede. Ela é branca.', ['wall', 'sky', 'brush']),
             ('Birds fly in the ___. It is blue today.', 'Os pássaros voam no céu. Hoje ele está azul.', ['sky', 'wall', 'paint']),
             ('The Mona Lisa is a famous ___.', 'A Mona Lisa é um quadro famoso.', ['picture', 'star', 'brush']),
             ('It is small and bright. You see it at night. Twinkle, twinkle, little ___.', 'É pequena e brilhante. Você vê à noite. Brilha, brilha, estrelinha.', ['star', 'wall', 'paint']))
    return dict(B=B, X=X, XT=XT, VB=VB, MR=MR, CX=CXs)


# ============================================================ 45 · Around the World in Eighty Days
FOGG = 'p:short:6b3f26:f4c7a1:2c3e50:hat:suit'
PASSE = 'p:curly:2d2d2d:e8b48a:2980b9:none:shirt'
CLERK = 'p:bun:2d2d2d:f4c7a1:7f1d1d:none:dress'


def ep45():
    B = dict(
        title="Where's the Restroom? · Where's the…?",
        sub="Perguntar onde as coisas ficam: Where's the restroom? It's down the hall.",
        pattern_label="Where's the…?",
        why="Hoje você aprende a perguntar onde fica algo como Phileas Fogg: Where's the elevator? E a entender: It's down the hall.",
        vocab=[['Restroom', 'Banheiro', 'Soa como “RÉST-rum”.'], ['Elevator', 'Elevador', 'Soa como “É-le-vei-ter”.'], ['Stairs', 'Escadas', 'Soa como “STÉRZ”.'],
               ['Hall', 'Corredor', 'Soa como “RÓL”.'], ['Corner', 'Esquina', 'Soa como “KÓR-ner”.'], ['Building', 'Prédio', 'Soa como “BÍL-ding”.']],
        balloons=[['🚻', 'restroom'], ['🛗', 'elevator'], ['⬆️', 'stairs'], ['🚪', 'hall'], ['📍', 'corner'], ['🏢', 'building']],
        cover_art=dict(s='lobby1', items=[['🎩', 104, 56, 20, 'bob'], ['🛗', 138, 44, 12, 'bob'], ['🚻', 84, 34, 12, 'bob']], seed='aw1'),
        cover_sub="Where's the…? Em 10 minutos você acha o caminho num prédio",
        cover_say='O senhor Fogg e seu empregado Passepartout chegam a um hotel. Eles precisam achar o banheiro, o elevador e a estação. Como perguntar onde fica?',
        wrap_recap=[["Where's the restroom?", 'Onde fica o banheiro?'], ["It's down the hall.", 'Fica no fim do corredor.'], ["It's next to the stairs.", 'Fica ao lado das escadas.'], ["You can't miss it.", 'Você não tem como errar.']],
        teaser=dict(t='The House That Jack Built', d='Próximo padrão: Where’s the…? (esquerda, direita, em frente)'),
        cast={'Fogg': ['🎩', '#2c3e50'], 'Passepartout': ['🧳', '#2980b9'], 'Clerk': ['👩‍💼', '#7f1d1d']},
        lines=[['Passepartout', "Excuse me! Where's the restroom?", 'Com licença! Onde fica o banheiro?'],
               ['Clerk', "It's down the hall, sir.", 'Fica no fim do corredor, senhor.'],
               ['Fogg', "Where's the elevator, please?", 'Onde fica o elevador, por favor?'],
               ['Clerk', "It's next to the stairs.", 'Fica ao lado das escadas.'],
               ['Fogg', "Where's the station? I'm in a hurry.", 'Onde fica a estação? Estou com pressa.'],
               ['Clerk', "It's at the corner. You can't miss it.", 'Fica na esquina. Você não tem como errar.'],
               ['Passepartout', "Sir, where's my bag?", 'Senhor, onde está a minha mala?'],
               ['Fogg', "It's in the hall. Let's go! Eighty days!", 'Está no corredor. Vamos! Oitenta dias!']],
        quiz=[quiz("Where's the restroom?", 'Onde fica o banheiro?', [['🧱', 'Next to the stairs'], ['🚪', 'Down the hall'], ['📍', 'At the corner']], 1, 1, 'A recepcionista diz: “It’s down the hall.”'),
              quiz("Where's the elevator?", 'Onde fica o elevador?', [['⬆️', 'Next to the stairs'], ['🚪', 'Down the hall'], ['📍', 'At the corner']], 0, 3, 'A recepcionista diz: “It’s next to the stairs.”'),
              quiz("Where's the station?", 'Onde fica a estação?', [['🚪', 'Down the hall'], ['⬆️', 'Next to the stairs'], ['📍', 'At the corner']], 2, 5, 'A recepcionista diz: “It’s at the corner.”')],
        rdg_q=dict(q="Qual frase pergunta “Onde fica o elevador?”", o=["Where's the elevator?", 'Where the elevator is?', 'What is the elevator where?'], a=0, why='Pergunta: **Where’s** (Where + is) + the + coisa?'),
        dictate=[["Where's the restroom?", 'Onde fica o banheiro?'], ["It's down the hall.", 'Fica no fim do corredor.'], ["It's next to the stairs.", 'Fica ao lado das escadas.'], ["Where's the station?", 'Onde fica a estação?']],
        produce=produce('No hotel, a recepcionista pergunta: *Can I help you?* **Pergunte onde fica o banheiro com Where’s…?, pergunte por outro lugar e agradeça.**',
                        "Ex.: Excuse me, where's the restroom? Where's the elevator? Thank you!", ["Where's the…?", 'Excuse me', 'Thank you!'],
                        "Excuse me, where's the restroom? Where's the elevator? Thank you!",
                        ['Perguntei do banheiro com Where’s?', 'Perguntei de outro lugar?', 'Agradeci?'],
                        [r"\bwhere(?:['’]s| is) the (?:restroom|bathroom)\b", r"\bwhere(?:['’]s| is) the (?!restroom|bathroom)\w+", r'\bthank(?:s| you)\b'],
                        [[["Where's the restroom?", 'Onde fica o banheiro?']], [["Where's the elevator?", 'Onde fica o elevador?']], [['Thank you!', 'Obrigado!']]],
                        ['Banheiro procurado! 🚻', 'Outro lugar! 🛗', 'Educação! 🙏'],
                        ["It's down the hall. You can't miss it!", 'Fica no fim do corredor. Você não tem como errar!']),
        rs=RSD('lobby1', 'hall', 'lobby2', 'station', 'street', 'office', 'airport'),
        sc='lobby1')
    X = dict(
        n=9809, review=True, names=('Fogg', 'Clerk'),
        stage=dict(rs='lobby1', chars=[[FOGG, 28, 0, 1.0], [PASSE, 56, 1, 0.95], [CLERK, 84, 1, 1.0]]),
        obra=dict(name='Around the World in Eighty Days', kind='📖 Romance de aventura · 1872', year='1872',
                  text='Romance de aventura do escritor francês Jules Verne, de 1872. O inglês Phileas Fogg aposta que consegue dar a volta ao mundo em 80 dias e parte com seu empregado, Passepartout, passando por trens, navios e muitas cidades.',
                  line=['Around the world in eighty days!', 'Dar a volta ao mundo em oitenta dias! (a aposta de Fogg)'],
                  pa=dict(t='ship', e=['🚂', '🚢', '🌍'], p='c', v=1)),
        gancho=['Passepartout', "Excuse me! Where's the restroom?", 'Com licença! Onde fica o banheiro?'],
        hot=[hot('🚻', 14, 16, 'restroom', 'banheiro', "Where's the restroom?", 'Onde fica o banheiro?'),
             hot('🛗', 40, 14, 'elevator', 'elevador', "Where's the elevator?", 'Onde fica o elevador?'),
             hot('⬆️', 66, 14, 'stairs', 'escadas', "It's next to the stairs.", 'Fica ao lado das escadas.'),
             hot('🏢', 88, 16, 'building', 'prédio', "Where's the building?", 'Onde fica o prédio?'),
             hot('🚉', 12, 82, 'station', 'estação', "Where's the station?", 'Onde fica a estação?')],
        gap=[gap('___ the elevator, please?', 'Onde fica o elevador, por favor?', ["What's", "Where's", 'Where'], 1, 'Para perguntar onde: **Where’s** (Where + is) the…?'),
             gap("It's ___ the hall.", 'Fica no fim do corredor.', ['down', 'to', 'for'], 0, 'No fim do corredor = **down** the hall.'),
             gap("It's next ___ the stairs.", 'Fica ao lado das escadas.', ['at', 'in', 'to'], 2, 'Ao lado de = next **to**.'),
             gap('Where ___ the restroom?', 'Onde fica o banheiro?', ['are', 'is', 'do'], 1, 'Uma coisa só: Where **is** the restroom?')],
        trap=[trap(['Where the restroom is?', "Where's the restroom?", 'Where is restroom the?'], 1, 'Na pergunta o **is** vem logo depois de **where**: Where’s the restroom?'),
              trap(['It\'s next the stairs.', "It's next of the stairs.", "It's next to the stairs."], 2, 'Ao lado de = **next to**.')],
        sticker=dict(title='Fogg e Passepartout', sub='Around the World in Eighty Days · 1872', rs='lobby1', chars=[[FOGG, 34, 0, 1.0], [PASSE, 68, 1, 0.95]]),
        speakers={'Fogg': FOGG, 'Passepartout': PASSE, 'Clerk': CLERK},
        rule=dict(
            who=FOGG, head="Where's the…?", sub='Perguntar onde as coisas ficam e entender a resposta.',
            say=["Where's the restroom?", 'Onde fica o banheiro?'],
            formula=[dict(from_=[['Where', 0], ['is', 1], ['the elevator?', 3]], to=[["Where's", 2], ['the elevator?', 3]], say="Where's the elevator?", note='Where + is = **Where’s**. Para perguntar onde fica uma coisa.'),
                     dict(from_=[['The elevator', 3], ['is', 1], ['next to the stairs.', 0]], to=[["It's", 2], ['next to the stairs.', 0]], say="It's next to the stairs.", note='Responda com **It’s** + o lugar: down the hall, next to…, at the corner.')],
            uses=[dict(ico='🚻', tag='Perguntar', en="Where's the restroom?", pt='Onde fica o banheiro?'),
                  dict(ico='🚪', tag='Responder', en="It's down the hall.", pt='Fica no fim do corredor.'),
                  dict(ico='⬆️', tag='Ao lado', en="It's next to the stairs.", pt='Fica ao lado das escadas.'),
                  dict(ico='📍', tag='Esquina', en="It's at the corner.", pt='Fica na esquina.')],
            rules=[dict(tag="Where's", c=0, text='Where + is = **Where’s**. Vem antes de the + coisa.', ex="Where's the station?"),
                   dict(tag='down / next to', c=1, text='**down the hall** = no fim do corredor. **next to** = ao lado de.', ex="It's down the hall. It's next to the stairs."),
                   dict(tag='It’s…', c=2, text='Na resposta, comece com **It’s**.', ex="It's at the corner.")],
            tips=['Em português perguntamos “onde fica?”. Em inglês o verbo é só o **is**: Where **is** the restroom? Não existe “Where stays”.']),
        mission_ic='🧭')
    XT = dict(
        exp=[exp('🙋', 'Excuse me!', 'Expressão', 'Com licença! / Desculpe!', 'Para **chamar a atenção** de alguém de forma educada.', ["Excuse me! Where's the elevator?", 'Com licença! Onde fica o elevador?']),
             exp('🚪', "It's down the hall.", 'Expressão', 'Fica no fim do corredor.', 'Para indicar algo **no corredor, mais adiante**.', ["It's down the hall, on the left.", 'Fica no fim do corredor, à esquerda.']),
             exp('➡️', 'Go straight ahead.', 'Expressão', 'Siga em frente.', 'Para dizer **para continuar reto**.', ['Go straight ahead. The restroom is there.', 'Siga em frente. O banheiro fica ali.']),
             exp('😉', "You can't miss it.", 'Expressão', 'Você não tem como errar.', 'Quando o lugar é **fácil de achar**.', ["It's at the corner. You can't miss it.", 'Fica na esquina. Você não tem como errar.'])],
        exp_scene=dict(rs='hall', lines=[
            ['Passepartout', '**Excuse me**! Where\'s the elevator?', 'Com licença! Onde fica o elevador?'],
            ['Clerk', '**Go straight ahead**, sir.', 'Siga em frente, senhor.'],
            ['Clerk', "It's **down the hall**.", 'Fica no fim do corredor.'],
            ['Fogg', 'And the station?', 'E a estação?'],
            ['Clerk', "It's at the corner. **You can't miss it**.", 'Fica na esquina. Você não tem como errar.'],
            ['Fogg', 'Thank you. Let us go, Passepartout!', 'Obrigado. Vamos, Passepartout!']]),
        lab=dict(
            short='r depois da vogal', title='Laboratório de sons: o “r” depois da vogal',
            say='Em turn, corner e hard o “r” aparece depois da vogal e muda o som. Vamos treinar!',
            intro=dict(what='Em **turn**, **corner** e **hard**, o **r** fica logo depois da vogal e a “colore”: o som é de vogal com “r” junto.',
                       how='Faça a vogal e, sem parar, puxe a língua um pouco para trás, sem encostar no céu da boca. O “r” é suave, nunca vibrado.',
                       pt='Em português muitos brasileiros engolem esse “r” (como em “porta”). Em inglês ele aparece! Cuidado: **short** (curto) ≠ **shot** (tiro).'),
            ex=[['turn', 'TÂRN', 'virar', 'língua para trás no “r”'], ['corner', 'KÓR-ner', 'esquina', 'faça o “r” depois do “ó”'], ['hard', 'RÁRD', 'duro, difícil', 'puxe a língua no “r”']],
            pairs=[['short', 'shot', '“curto” × “tiro”: em short há um “r” depois da vogal'], ['hard', 'had', '“duro” × “tinha”'], ['park', 'pack', '“parque” × “pacote”']],
            tip='Depois da vogal, puxe a língua para trás como se fosse dizer “r” bem suave.',
            phrase=['Turn at the corner, it is hard to miss.', 'Vire na esquina, é difícil não ver.'],
            rounds=[rnd('shot', ['short', 'shot'], 1, '**Shot** (tiro) não tem “r”. **Short** (curto) tem “r” depois da vogal.'),
                    rnd('park', ['park', 'pack'], 0, '**Park** tem “r” depois da vogal. **Pack** (pacote) não tem.'),
                    rnd('had', ['hard', 'had'], 1, '**Had** (tinha) não tem “r”. **Hard** (duro) tem.')]),
        hunt=[ht('hard', ['hard', 'had'], 0, '**hard** = duro, com “r” depois da vogal.'), ht('pack', ['park', 'pack'], 1, '**pack** = pacote, sem “r”.'),
              hp('park', ['🌳', '📦', '🔫'], 0, '**park** = parque, com “r” depois do “a”.'), ht('short', ['short', 'shot'], 0, '**short** = curto, com “r” depois do “o”.')])
    VB = dict(title='Verbos para achar o caminho', tip='Quatro verbos: go, turn, walk e follow.', items=[
        verb('go', '🚶', 'ir', 'I go to the elevator.', 'Mr. Fogg go**es** to the station.', ['I go to the elevator.', 'Eu vou ao elevador.'], '**go** = ir. Com he/she: **goes** (com es).'),
        verb('turn', '↩️', 'virar', 'I turn at the corner.', 'She turn**s** at the hall.', ['I turn at the corner.', 'Eu viro na esquina.'], '**turn** = virar. Com he/she: **turns**.'),
        verb('walk', '🚶‍♂️', 'andar a pé', 'I walk down the hall.', 'He walk**s** to the building.', ['I walk down the hall.', 'Eu ando pelo corredor.'], '**walk** = andar a pé. Com he/she: **walks**.'),
        verb('follow', '👣', 'seguir', 'I follow the clerk.', 'Passepartout follow**s** Mr. Fogg.', ['I follow the clerk.', 'Eu sigo a recepcionista.'], '**follow** = seguir. Com he/she: **follows**.')])
    MR = dict(
        mold=[mold('Perguntar onde fica', [('pergunta', [["Where's the", 'onde fica o/a']]), ('lugar', [['restroom', 'banheiro'], ['elevator', 'elevador'], ['station', 'estação'], ['building', 'prédio'], ['hall', 'corredor']])], ('?', '?')),
              mold('Responder onde fica', [('frase', [["It's", 'fica']]), ('onde', [['down the hall', 'no fim do corredor'], ['next to the stairs', 'ao lado das escadas'], ['at the corner', 'na esquina'], ['in the building', 'no prédio']])]),
              mold('Pedir com educação', [('abertura', [['Excuse me!', 'com licença!']]), ('pergunta', [["Where's the restroom?", 'onde fica o banheiro?'], ["Where's the elevator?", 'onde fica o elevador?'], ["Where's the station?", 'onde fica a estação?']])], ('', ''))],
        speak=[["Excuse me! Where's the restroom?", 'Com licença! Onde fica o banheiro?'], ["It's down the hall. You can't miss it.", 'Fica no fim do corredor. Você não tem como errar.']],
        trap=[mtrap('“You can\'t miss it.” quer dizer…', ['Você não tem como errar.', 'Você não pode faltar.', 'Você perdeu o trem.'], 0, '**You can’t miss it.** = é fácil de achar.', "You can't miss it."),
              mtrap('Qual frase está certa?', ['Go ahead straight.', 'Straight go ahead.', 'Go straight ahead.'], 2, 'Expressão fixa: **Go straight ahead.**', 'Go straight ahead.')],
        gap=[mgap('___ me! Where is the station?', 'Com licença! Onde fica a estação?', ['Excuse', 'Sorry', 'Thank'], 0, '**Excuse me!** chama a atenção com educação.', 'Excuse me! Where is the station?'),
             mgap('Go straight ___.', 'Siga em frente.', ['ahead', 'before', 'up'], 0, '**Go straight ahead.** = siga em frente.', 'Go straight ahead.')],
        expq=[expq('Você quer perguntar algo a um desconhecido.', ['Excuse me!', 'Go straight ahead.', "You can't miss it."], 0, '**Excuse me!** = com licença!'),
              expq('O lugar é bem visível e você quer tranquilizar o turista.', ["You can't miss it.", 'Excuse me!', "It's down the hall."], 0, "**You can't miss it.** = não tem como errar."),
              expq('O elevador fica no fim do corredor.', ['Go straight ahead.', "It's down the hall.", 'Excuse me!'], 1, "**It's down the hall.** = fica no fim do corredor.")],
        missions=[mission('🧭', 'Dando direções', 'Ajude um turista.', 'Um turista está perdido. **Diga que o elevador fica no fim do corredor, que a escada fica ao lado e que ele não tem como errar.**', ["It's down the hall."],
                          "The elevator is down the hall. It's next to the stairs. You can't miss it!", ['Disse que fica no fim do corredor?', 'Disse que fica ao lado das escadas?', 'Disse que não tem como errar?'],
                          [r'\bdown the hall\b', r'\bnext to the stairs\b', r'\bcan[’\']t miss it\b'],
                          [[["It's down the hall.", 'Fica no fim do corredor.']], [["It's next to the stairs.", 'Fica ao lado das escadas.']], [["You can't miss it.", 'Você não tem como errar.']]],
                          ['Corredor! 🚪', 'Escadas! ⬆️', 'Fácil de achar! 😉'], ['Thank you so much!', 'Muito obrigado!']),
                  mission('🚉', 'Procurando a estação', 'Peça ajuda com educação.', '**Peça licença, pergunte onde fica a estação e diga que está com pressa.**', ['Excuse me!'],
                          "Excuse me, where's the station? I'm in a hurry!", ['Pedi licença?', 'Perguntei onde fica a estação?', 'Disse que estou com pressa?'],
                          [r'\bexcuse me\b', r"\bwhere(?:['’]s| is) the station\b", r'\bin a hurry\b'],
                          [[['Excuse me!', 'Com licença!']], [["Where's the station?", 'Onde fica a estação?']], [["I'm in a hurry.", 'Estou com pressa.']]],
                          ['Educado! 🙋', 'Pergunta certa! 🚉', 'Pressa avisada! 🏃'], ["It's at the corner. Run!", 'Fica na esquina. Corra!'])])
    CXs = cx(('I need to wash my hands. Where is the ___?', 'Preciso lavar as mãos. Onde fica o banheiro?', ['restroom', 'corner', 'building']),
             ('The office is on the tenth floor. I take the ___.', 'O escritório fica no décimo andar. Eu pego o elevador.', ['elevator', 'stairs', 'hall']),
             ('The elevator is broken. Take the ___.', 'O elevador está quebrado. Pegue as escadas.', ['stairs', 'restroom', 'corner']),
             ('The doors are on both sides of the long ___.', 'As portas ficam dos dois lados do corredor comprido.', ['hall', 'building', 'elevator']),
             ('Walk to the end of the street and turn at the ___.', 'Ande até o fim da rua e vire na esquina.', ['corner', 'hall', 'restroom']),
             ('It is very tall, with many floors and windows. It is a ___.', 'É muito alto, com muitos andares e janelas. É um prédio.', ['building', 'stairs', 'corner']))
    return dict(B=B, X=X, XT=XT, VB=VB, MR=MR, CX=CXs)


EPS = [ep38(), ep39(), ep40(), ep41(), ep42(), ep43(), ep44(), ep45()]
