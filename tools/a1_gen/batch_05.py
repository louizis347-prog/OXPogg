# Lote 05 · posições 38 a 45 do A1 (padrões: Would you like…? · What's this? · It's / It isn't · pronomes-objeto ·
# adjetivo antes do substantivo · What color is it? · I want / I'd like · Where's the…?)
# TROCAS DE OBRA: pos 38: de Mary Poppins para Charlie and the Chocolate Factory
# TROCAS DE OBRA: pos 39: de The Wonderful Wizard of Oz para Composition II in Red, Blue, and Yellow (Mondrian)
# TROCAS DE OBRA: pos 40: de The Wonderful Wizard of Oz para Handa's Surprise
# TROCAS DE OBRA: pos 41: de Baa, Baa, Black Sheep para The Devil Wears Prada
# TROCAS DE OBRA: pos 42: mantém Baa, Baa, Black Sheep (agora só no episódio 42)
# TROCAS DE OBRA: pos 43: de The Purple Cow para The Starry Night (Van Gogh)
# TROCAS DE OBRA: pos 44: de The Purple Cow para The Little Prince
# TROCAS DE OBRA: pos 45: de Around the World in Eighty Days para Harry Potter and the Philosopher's Stone
import re

EPS = []

RSKEYS = ['review', 'dquiz', 'rdg', 'pat', 'vplay', 'sbuild', 'build', 'order', 'balloons', 'dictate',
          'soundlab', 'scene', 'scenebuild', 'produce', 'wrap']


def rs15(lst):
    assert len(lst) == 15
    return dict(zip(RSKEYS, lst))


def Q(q, pt, opts, a, line, why):
    return dict(q=q, pt=pt, opts=opts, a=a, line=line, why=why)


def G(q, pt, opts, a, why):
    return dict(q=q, pt=pt, opts=opts, a=a, why=why)


def TR(opts, a, why, q='Qual frase está certa?'):
    return dict(q=q, opts=opts, a=a, why=why)


def H(e, x, y, en, pt, say, sayPt):
    return dict(e=e, x=x, y=y, en=en, pt=pt, say=say, sayPt=sayPt)


def E(ic, en, tag, pt, use, ex):
    return dict(ic=ic, en=en, tag=tag, pt=pt, use=use, ex=ex)


def VBI(v, ic, pt, f1, f2, ex, note):
    return dict(v=v, ic=ic, pt=pt, f=[['eu', f1], ['ele/ela', f2]], ex=ex, note=note)


def RD(say, opts, a, why):
    return dict(fig='🎧', say=say, ask='Qual palavra você ouviu?', opts=opts, a=a, why=why)


def HU(say, opts, a, why, pic=False):
    d = dict(fig='🎧', say=say, ask='Ouça e toque na figura.' if pic else 'Ouça e toque na palavra.', opts=opts, a=a, why=why)
    if pic:
        d['pic'] = 1
    return d


def SL(cat, opts):
    return dict(cat=cat, opts=opts)


def MP(label, slots, end):
    return dict(label=label, slots=slots, end=end)


def MT(ask, opts, a, why, say=None):
    d = dict(ask=ask, opts=opts, a=a, why=why)
    if say:
        d['say'] = say
    return d


def MG(text, pt, opts, a, why, say):
    return dict(text=text, pt=pt, opts=opts, a=a, why=why, say=say)


def MS(ic, name, desc, prompt, ph, chips, model, check, kw, tips, ok, reply):
    return dict(ic=ic, name=name, desc=desc, data=dict(prompt=prompt, ph=ph, chips=chips, model=model, check=check,
                                                          kw=kw, tips=tips, ok=ok, reply=reply))


def CXI(text, pt, right, w1, w2):
    return dict(text=text, pt=pt, opts=[right, w1, w2], a=0)


def PRD(prompt, ph, chips, model, check, kw, tips, ok, reply):
    return dict(prompt=prompt, ph=ph, chips=chips, model=model, check=check, kw=kw, tips=tips, ok=ok, reply=reply)


def ch3(*a):
    return list(a)


# ============================================================ 38 · Would you like…? · Charlie and the Chocolate Factory
def ep38():
    wonka = 'p:curly:7a4a24:f4c7a1:6a2c8f:hat:suit'
    charlie = 'p:short:3b2a1a:f4c7a1:3f6fb5:none:shirt'
    joe = 'p:bald:cfcfcf:f4c7a1:7f8c8d:glasses:suit'
    B = dict(
        title='Aceitar e recusar doces · Would you like…?',
        sub='Oferecer com Would you like…? e responder com Yes, please / No, thanks',
        pattern_label='Would you like…?',
        why='Hoje você aprende a oferecer algo com Would you like…? e a responder com educação: Yes, please / No, thanks.',
        vocab=[['Chocolate', 'Chocolate', 'Soa como “TCHÓ-klit”.'], ['Candy', 'Bala, doce', 'Soa como “KÉN-di”.'],
               ['Cake', 'Bolo', 'Soa como “KÊIK”.'], ['Milk', 'Leite', 'Soa como “MÍLK”.'],
               ['Cookie', 'Biscoito', 'Soa como “KÚ-ki”.'], ['Juice', 'Suco', 'Soa como “DJUS”.']],
        balloons=[['🍫', 'chocolate'], ['🍬', 'candy'], ['🎂', 'cake'], ['🥛', 'milk'], ['🍪', 'cookie'], ['🧃', 'juice']],
        cover_art=dict(s='chefkitchen', items=[['🍫', 104, 56, 20, 'bob'], ['🍬', 138, 44, 12, 'bob'], ['🎂', 84, 34, 12, 'bob']], seed='wk1'),
        cover_sub='Would you like…? Em 10 minutos você oferece e aceita doces como na fábrica do Wonka',
        cover_say='O senhor Wonka abre as portas da sua fábrica de chocolate. Ele quer oferecer doces a todo mundo. Como oferecer? E como responder com educação?',
        wrap_recap=[['Would you like some chocolate?', 'Você quer um pouco de chocolate?'], ['Yes, please!', 'Sim, por favor!'],
                    ['No, thanks.', 'Não, obrigado.'], ['Would you like a cake or a candy?', 'Você quer um bolo ou uma bala?']],
        teaser=dict(t='Composition II in Red, Blue, and Yellow', d="Próximo padrão: What's this? para perguntar o que é"),
        cast={'Wonka': ['🎩', '#6C3483'], 'Charlie': ['👦', '#2b6cb0'], 'Joe': ['👴', '#7f8c8d']},
        lines=[['Wonka', 'Welcome! Would you like some chocolate?', 'Bem-vindos! Vocês querem um pouco de chocolate?'],
               ['Charlie', 'Yes, please! I love chocolate.', 'Sim, por favor! Eu adoro chocolate.'],
               ['Wonka', 'Joe, would you like some milk?', 'Joe, você quer um pouco de leite?'],
               ['Joe', "No, thanks. I'm not hungry.", 'Não, obrigado. Não estou com fome.'],
               ['Wonka', 'Would you like a cake or a candy?', 'Você quer um bolo ou uma bala?'],
               ['Charlie', 'A candy, please! Grandpa, would you like a candy?', 'Uma bala, por favor! Vovô, você quer uma bala?'],
               ['Joe', 'Yes, please! It is very good.', 'Sim, por favor! É muito boa.'],
               ['Wonka', 'Great! Enjoy your candy!', 'Ótimo! Aproveitem a bala!']],
        quiz=[Q('What does Charlie love?', 'O que o Charlie adora?', [['🍫', 'Chocolate'], ['🥛', 'Milk'], ['🎂', 'Cake']], 0, 1, 'Charlie diz: “I love chocolate.”'),
              Q('Who says “No, thanks”?', 'Quem diz “No, thanks”?', [['👦', 'Charlie'], ['🎩', 'Mr. Wonka'], ['👴', 'Grandpa Joe']], 2, 3, 'O vovô Joe diz: “No, thanks.”'),
              Q('What does Charlie choose?', 'O que o Charlie escolhe?', [['🎂', 'A cake'], ['🍬', 'A candy'], ['🥛', 'Milk']], 1, 5, 'Charlie diz: “A candy, please!”')],
        rdg_q=dict(q='Você quer aceitar uma oferta com educação. O que você diz?', o=['Yes, I want.', 'Yes, please.', 'Yes, I do.'], a=1,
                   why='Para aceitar uma oferta, diga **Yes, please.** (“Yes, I want” soa seco).'),
        dictate=[['Would you like some chocolate?', 'Você quer um pouco de chocolate?'], ['Yes, please!', 'Sim, por favor!'],
                 ["No, thanks. I'm not hungry.", 'Não, obrigado. Não estou com fome.'], ['Would you like a cake or a candy?', 'Você quer um bolo ou uma bala?']],
        produce=PRD('O Wonka pergunta: *Would you like some chocolate? Would you like a cake or a cookie?* **Responda com Yes, please ou No, thanks, escolha uma coisa e ofereça algo a ele com Would you like…?**',
                    'Ex.: Yes, please! A cookie, please. Would you like some milk?', ['Yes, please.', 'No, thanks.', 'Would you like…?'],
                    'Yes, please! A cookie, please. Would you like some milk, Willy?',
                    ['Aceitei ou recusei com Yes, please / No, thanks?', 'Escolhi uma coisa?', 'Ofereci algo com Would you like…?'],
                    [r'\b(?:yes,?\s*please|no,?\s*thank(?:s| you))\b', r'\b(?:cake|cookie|candy|chocolate|milk|juice)\b', r'\bwould you like\b[^.!?]*\?'],
                    [[['Yes, please.', 'Sim, por favor.'], ['No, thanks.', 'Não, obrigado.']], [['A cookie, please.', 'Um biscoito, por favor.'], ['Milk, please.', 'Leite, por favor.']],
                     [['Would you like some milk?', 'Você quer um pouco de leite?'], ['Would you like a cake?', 'Você quer um bolo?']]],
                    ['Resposta educada! ✅', 'Boa escolha! 🍪', 'Boa oferta! 🍫'],
                    ['Thank you! I love milk. Yes, please!', 'Obrigado! Eu adoro leite. Sim, por favor!']),
        rs=rs15(['hotelroom', 'bakery', 'library', 'chefkitchen', 'playground', 'restaurant', 'supermarket', 'museum', 'garden',
                 'pool', 'musicroom', 'chefkitchen', 'fair', 'bakery', 'christmas']),
        sc='chefkitchen')
    X = dict(
        n=7910003, review=True, names=('Wonka', 'Charlie'),
        stage=dict(rs='chefkitchen', chars=[[wonka, 28, 0, 1.0], [charlie, 56, 1, 1.0], [joe, 84, 1, 0.95]]),
        obra=dict(name='Charlie and the Chocolate Factory', kind='📖 Livro infantil · 1964', year='1964',
                  text='Livro do escritor britânico Roald Dahl, publicado em 1964. O menino Charlie Bucket ganha um bilhete dourado e visita a fábrica de chocolate do senhor Willy Wonka, cheia de doces mágicos. Lá, ele e o avô provam de tudo.',
                  line=['Would you like some chocolate?', 'Você quer um pouco de chocolate? (frase do tema)'],
                  pa=dict(t='bakery', e=['🍫', '🏭', '🎟️'], p='a', v=0)),
        gancho=['Wonka', 'Welcome! Would you like some chocolate?', 'Bem-vindos! Vocês querem um pouco de chocolate?'],
        hot=[H('🍫', 14, 16, 'chocolate', 'chocolate', 'Would you like some chocolate?', 'Você quer um pouco de chocolate?'),
             H('🍬', 40, 14, 'candy', 'bala', 'Yes, please! A candy!', 'Sim, por favor! Uma bala!'),
             H('🎂', 66, 14, 'cake', 'bolo', 'Would you like a cake?', 'Você quer um bolo?'),
             H('🥛', 88, 16, 'milk', 'leite', 'No, thanks. No milk for me.', 'Não, obrigado. Sem leite para mim.'),
             H('🍪', 12, 82, 'cookie', 'biscoito', 'Would you like a cookie?', 'Você quer um biscoito?')],
        gap=[G('___ you like some cake?', 'Você quer um pouco de bolo?', ['Are', 'Is', 'Would'], 2, 'Para oferecer, use **Would you like…?**'),
             G('Would you like ___ milk?', 'Você quer um pouco de leite?', ['a', 'some', 'an'], 1, 'Leite não se conta: use **some milk**.'),
             G('Would you like ___ cookie?', 'Você quer um biscoito?', ['some', 'an', 'a'], 2, 'Um biscoito só: **a cookie**.'),
             G("No, ___. I'm not hungry.", 'Não, obrigado. Não estou com fome.', ['thanks', 'thank', 'thanking'], 0, 'Recusa educada: **No, thanks.**')],
        trap=[TR(['You would like some tea?', 'Would you like some tea?', 'Do you would like some tea?'], 1, 'Na pergunta, **Would** vem primeiro: **Would** you like…?'),
              TR(['Yes, I want.', 'Yes, I would please.', 'Yes, please.'], 2, 'Para aceitar com educação: **Yes, please.**')],
        sticker=dict(title='Wonka e Charlie', sub='Charlie and the Chocolate Factory · 1964', rs='bakery', chars=[[wonka, 34, 0, 1.0], [charlie, 68, 1, 1.0]]),
        speakers={'Wonka': wonka, 'Charlie': charlie, 'Joe': joe},
        rule=dict(who=wonka, head='Would you like…?', sub='Uma forma educada de oferecer.',
                  say=['Would you like some chocolate?', 'Você quer um pouco de chocolate?'],
                  formula=[
                      dict(from_=[['Would', 1], ['you', 0], ['like', 2], ['some cake?', 3]], to=[['Yes,', 1], ['please.', 2]], say='Yes, please.', note='Aceitar: **Yes, please.** Não diga só “Yes”.'),
                      dict(from_=[['Would', 1], ['you', 0], ['like', 2], ['some milk?', 3]], to=[['No,', 1], ['thanks.', 2]], say='No, thanks.', note='Recusar: **No, thanks.**'),
                      dict(from_=[['Would you like', 1], ['a cake', 0], ['or', 2], ['a candy?', 3]], to=[['A candy,', 3], ['please.', 1]], say='A candy, please.', note='Com **or**, você escolhe uma opção.')],
                  uses=[dict(ico='🍫', tag='Oferecer', en='Would you like some chocolate?', pt='Você quer um pouco de chocolate?'),
                        dict(ico='✅', tag='Aceitar', en='Yes, please!', pt='Sim, por favor!'),
                        dict(ico='🙅', tag='Recusar', en='No, thanks.', pt='Não, obrigado.')],
                  rules=[dict(tag='a + um só', c=0, text='Uma coisa que se conta: **a cake, a candy, a cookie**.', ex='Would you like a cake?'),
                         dict(tag='some + porção', c=2, text='Coisa que não se conta: **some milk, some juice, some chocolate**.', ex='Would you like some milk?'),
                         dict(tag='Yes, please', c=1, text='Dizer só “Yes” soa seco. Junte **please**.', ex='Yes, please. / No, thanks.')],
                  tips=['Em português basta dizer “Aceita?”. Em inglês a oferta educada começa com **Would you like**, e a resposta leva **please** ou **thanks**.']),
        mission_ic='🍫')
    XT = dict(
        exp=[E('🤲', 'Help yourself!', 'Expressão', 'Sirva-se!', 'Quando você **convida** alguém a pegar comida ou bebida.', ['Help yourself to some candy!', 'Sirva-se de algumas balas!']),
             E('🤏', 'Just a little, please.', 'Expressão', 'Só um pouquinho, por favor.', 'Para aceitar uma oferta, mas **com pouca quantidade**.', ['Just a little milk, please.', 'Só um pouquinho de leite, por favor.']),
             E('😋', "I'm full.", 'Expressão', 'Estou satisfeito.', 'Para recusar mais comida com educação: você **já comeu bastante**.', ["No, thanks. I'm full.", 'Não, obrigado. Estou satisfeito.']),
             E('👍', 'Sounds great!', 'Informal', 'Parece ótimo!', 'Resposta animada a uma **proposta ou oferta**.', ['A cake? Sounds great!', 'Um bolo? Parece ótimo!'])],
        exp_scene=dict(rs='restaurant', lines=[
            ['Wonka', 'Come in! **Help yourself** to the cake.', 'Entrem! Sirvam-se do bolo.'],
            ['Charlie', 'Would you like some cake, Grandpa?', 'Vovô, você quer um pouco de bolo?'],
            ['Joe', '**Just a little, please.**', 'Só um pouquinho, por favor.'],
            ['Wonka', 'Would you like some chocolate too?', 'Você quer chocolate também?'],
            ['Joe', "No, thanks. **I'm full.**", 'Não, obrigado. Estou satisfeito.'],
            ['Charlie', 'A candy for me? **Sounds great!**', 'Uma bala para mim? Parece ótimo!']]),
        lab=dict(short='sh × ch', title='Laboratório de sons: “ch” de chocolate e “sh” de share',
                 say='Em inglês, “ch” e “sh” são sons diferentes. Vamos treinar com os doces da fábrica!',
                 intro=dict(what='O **ch** de **chocolate**, **cheese** e **cherry** é um som forte, como o “tch” de “tchau”. O **sh** de **share**, **she** e **shoe** é um som solto e longo, como pedir silêncio: “shhh”.',
                            how='Para o **ch**, a língua encosta e solta de repente. Para o **sh**, a língua não encosta: o ar sai contínuo, com os lábios um pouco redondos.',
                            pt='Em português dizemos “chuva” com um som parecido com o **sh**. Cuidado: em inglês **ship** (navio) e **chip** (batata frita) são palavras diferentes.'),
                 ex=[['chocolate', 'TCHÓ-klit', 'chocolate', 'comece com “tch”'], ['cheese', 'TCHIZ', 'queijo', 'tch forte no começo'], ['share', 'SHÉR', 'dividir', 'só ar contínuo, como “shhh”']],
                 pairs=[['ship', 'chip', 'sh: ar contínuo · ch: “tch” de repente'], ['sheep', 'cheap', '“ovelha” × “barato”'], ['wash', 'watch', '“lavar” × “assistir”']],
                 tip='Diga “shhh” alto e comprido. Depois comece de novo com um “tch” curtinho: assim você sente a diferença.',
                 phrase=['Would you like some cheese or chocolate?', 'Você quer queijo ou chocolate?'],
                 rounds=[RD('chip', ['ship', 'chip'], 1, '**Chip** (batata frita) começa com “tch”. **Ship** (navio) começa com “sh”.'),
                         RD('sheep', ['sheep', 'cheap'], 0, '**Sheep** (ovelha) tem o “sh” contínuo. **Cheap** (barato) começa com “tch”.'),
                         RD('watch', ['wash', 'watch'], 1, '**Watch** (assistir) termina em “tch”. **Wash** (lavar) termina em “sh”.')]),
        hunt=[HU('cheese', ['cheese', 'sheese'], 0, '**cheese** (queijo) começa com “tch”.'),
              HU('share', ['share', 'chair'], 0, '**share** (dividir) tem o “sh”.'),
              HU('cherry', [['🍒', ''], ['🐑', ''], ['👟', '']], 0, '**cherry** = cereja, começa com “tch”.', True),
              HU('shoe', [['🍒', ''], ['🐑', ''], ['👟', '']], 2, '**shoe** = sapato, começa com “sh”.', True),
              HU('chair', ['chair', 'share'], 0, '**chair** (cadeira) começa com “tch”.')])
    VB = dict(title='Verbos para dividir doces', tip='Quatro verbos: eat, share, offer e pour.',
              items=[VBI('eat', '🍽️', 'comer', 'I eat chocolate.', 'Charlie eat**s** candy.', ['I eat chocolate.', 'Eu como chocolate.'], '**eat** = comer. Com he/she: **eats**.'),
                     VBI('share', '🤝', 'dividir', 'I share my cake.', 'Joe share**s** his candy.', ['I share my cake.', 'Eu divido o meu bolo.'], '**share** = dividir. Com he/she: **shares**.'),
                     VBI('offer', '🎁', 'oferecer', 'I offer some milk.', 'Wonka offer**s** a cookie.', ['I offer some milk.', 'Eu ofereço um pouco de leite.'], '**offer** = oferecer. Com he/she: **offers**.'),
                     VBI('pour', '🫗', 'servir (líquido)', 'I pour the juice.', 'He pour**s** the milk.', ['I pour the juice.', 'Eu sirvo o suco.'], '**pour** = servir um líquido. Com he/she: **pours**.')])
    MR = dict(
        mold=[MP('Oferecer com Would you like…?', [SL('pergunta', [['Would you like', 'você quer']]),
                                                   SL('coisa', [['a candy', 'uma bala'], ['a cake', 'um bolo'], ['a cookie', 'um biscoito'], ['some milk', 'um pouco de leite'],
                                                                ['some juice', 'um pouco de suco'], ['some chocolate', 'um pouco de chocolate']])], ['?', '?']),
              MP('Responder', [SL('resposta', [['Yes, please', 'sim, por favor'], ['No, thanks', 'não, obrigado'], ['No, thank you', 'não, obrigado']])], ['.', '.']),
              MP('Escolher entre duas coisas', [SL('pergunta', [['Would you like', 'você quer']]),
                                                SL('primeira', [['a cake', 'um bolo'], ['some milk', 'um pouco de leite'], ['a cookie', 'um biscoito']]),
                                                SL('ou', [['or', 'ou']]),
                                                SL('segunda', [['a candy', 'uma bala'], ['some juice', 'um pouco de suco'], ['some chocolate', 'um pouco de chocolate']])], ['?', '?'])],
        speak=[['Would you like some milk? No, thanks.', 'Você quer um pouco de leite? Não, obrigado.'], ['Yes, please! I love candy.', 'Sim, por favor! Eu adoro bala.']],
        trap=[MT('“Help yourself!” quer dizer…', ['Sirva-se!', 'Me ajude!', 'Ajude-se a sair!'], 0, '**Help yourself!** = sirva-se (convite para pegar comida).', 'Help yourself!'),
              MT('Qual frase está certa?', ["I'm full.", 'I have full.', 'I am fullness.'], 0, 'Estou satisfeito = **I\'m full.**', "I'm full.")],
        gap=[MG('Would you like ___ cookie?', 'Você quer um biscoito?', ['a', 'some', 'two'], 0, 'Um biscoito só: **a cookie**.', 'Would you like a cookie?'),
             MG('Just a little ___, please.', 'Só um pouquinho, por favor.', ['milk', 'cookie', 'candies'], 0, '**Just a little** combina com coisa que não se conta: **milk**.', 'Just a little milk, please.')],
        expq=[MT('Você já comeu bastante e alguém oferece mais bolo.', ["No, thanks. I'm full.", 'Help yourself!', 'Sounds great!'], 0, "**No, thanks. I'm full.** recusa com educação."),
              MT('Você convida o amigo a pegar um biscoito.', ['Sounds great!', "I'm full.", 'Help yourself!'], 2, '**Help yourself!** convida a pegar.'),
              MT('Alguém oferece um passeio e você fica animado.', ['Sounds great!', 'Just a little.', "I'm full."], 0, '**Sounds great!** mostra entusiasmo.')],
        missions=[MS('🍫', 'Festa de doces', 'Ofereça e responda com educação.',
                     'Você recebe amigos em casa. **Ofereça duas coisas com Would you like…? e responda a um amigo com Yes, please ou No, thanks.**',
                     'Escreva a sua resposta aqui…', ['Would you like'],
                     'Would you like some juice? Would you like a cookie? Yes, please!',
                     ['Fiz uma oferta com Would you like…?', 'Fiz duas ofertas?', 'Usei Yes, please ou No, thanks?'],
                     [r'\bwould you like\b[^.!?]*\?', r'(?:\bwould you like\b[^.!?]*\?[\s\S]*){2}', r'\b(?:yes,?\s*please|no,?\s*thank(?:s| you))\b'],
                     [[['Would you like some juice?', 'Você quer suco?']], [['Would you like a cookie?', 'Você quer um biscoito?']], [['Yes, please.', 'Sim, por favor.'], ['No, thanks.', 'Não, obrigado.']]],
                     ['Oferta educada! 🎁', 'Duas ofertas! ✌️', 'Resposta certa! ✅'],
                     ['Yes, please! Thank you!', 'Sim, por favor! Obrigado!']),
                  MS('🤲', 'Na mesa', 'Use as expressões do episódio.',
                     'Você está na mesa de um amigo. **Convide alguém com Help yourself, aceite um pouquinho com Just a little e diga que está satisfeito com I\'m full.**',
                     'Escreva a sua resposta aqui…', ['Help yourself'],
                     "Help yourself! Just a little, please. I'm full, thanks.",
                     ['Convidei com Help yourself?', 'Pedi só um pouquinho?', 'Disse que estou satisfeito?'],
                     [r'\bhelp yourself\b', r'\bjust a little\b', r"\bi['’]m full\b"],
                     [[['Help yourself!', 'Sirva-se!']], [['Just a little, please.', 'Só um pouquinho, por favor.']], [["I'm full.", 'Estou satisfeito.']]],
                     ['Convite feito! 🤲', 'Pouquinho! 🤏', 'Satisfeito! 😋'],
                     ['Great! Enjoy your food!', 'Ótimo! Aproveite a comida!'])])
    CX = [CXI('It is brown and sweet. I love eating ___ at Christmas.', 'É marrom e doce. Eu adoro comer chocolate no Natal.', 'chocolate', 'milk', 'juice'),
          CXI('It is a small sweet. Tom has a red ___ in his hand.', 'É um doce pequeno. O Tom tem uma bala vermelha na mão.', 'candy', 'cake', 'cookie'),
          CXI('It is Ana\'s birthday. We have a big ___ with candles.', 'É aniversário da Ana. Temos um bolo grande com velas.', 'cake', 'juice', 'milk'),
          CXI('A baby drinks white ___ from a bottle.', 'O bebê bebe leite branco na mamadeira.', 'milk', 'cookie', 'cake'),
          CXI('It is round and crunchy. I eat a ___ with my coffee.', 'É redondo e crocante. Eu como um biscoito com o meu café.', 'cookie', 'juice', 'milk'),
          CXI('It is a cold drink made of oranges. I like orange ___.', 'É uma bebida gelada feita de laranjas. Eu gosto de suco de laranja.', 'juice', 'candy', 'cake')]
    return dict(B=B, X=X, XT=XT, VB=VB, MR=MR, CX=CX)


EPS.append(ep38())


# ============================================================ 39 · What's this? · Composition II in Red, Blue, and Yellow
def ep39():
    rosa = 'p:bun:5a3a2a:c68642:c0392b:glasses:dress'
    leo = 'p:short:222222:8d5524:2e86c1:none:shirt'
    nina = 'p:curly:2c1b12:e8b48a:f1c40f:bow:dress'
    B = dict(
        title="O que é isto? · What's this?",
        sub="Perguntar o que é com What's this? e responder It's a… / It's an…",
        pattern_label="What's this?",
        why="Hoje você aprende a perguntar o que é cada coisa com What's this? e a responder com It's a… e uma cor.",
        vocab=[['Red', 'Vermelho', 'Soa como “RÉD”.'], ['Yellow', 'Amarelo', 'Soa como “IÉ-lou”.'], ['Blue', 'Azul', 'Soa como “BLÚ”.'],
               ['Green', 'Verde', 'Soa como “GRIN”.'], ['Orange', 'Laranja', 'Soa como “Ó-rinj”.'], ['Brush', 'Pincel', 'Soa como “BRÂSH”.']],
        balloons=[['🟥', 'red'], ['🟨', 'yellow'], ['🟦', 'blue'], ['🟩', 'green'], ['🟧', 'orange'], ['🖌️', 'brush']],
        cover_art=dict(s='artroom', items=[['🟥', 104, 56, 20, 'bob'], ['🟦', 138, 44, 12, 'bob'], ['🟨', 84, 34, 12, 'bob']], seed='mo1'),
        cover_sub="What's this? Em 10 minutos você pergunta o que é e fala das cores",
        cover_say='Uma turma de arte olha um quadro cheio de quadrados coloridos. Todo mundo quer saber: o que é isto? Como perguntar e como responder?',
        wrap_recap=[["What's this?", 'O que é isto?'], ["It's a painting.", 'É uma pintura.'], ["It's an orange brush.", 'É um pincel laranja.'], ["It's red, yellow and blue.", 'É vermelho, amarelo e azul.']],
        teaser=dict(t="Handa's Surprise", d="Próximo padrão: It's / It isn't para dizer o que é e o que não é"),
        cast={'Rosa': ['👩‍🏫', '#c0392b'], 'Leo': ['👦', '#2e86c1'], 'Nina': ['👧', '#d4ac0d']},
        lines=[['Rosa', "Look at this! What's this, Leo?", 'Olhe isto! O que é isto, Leo?'],
               ['Leo', "It's a painting. Cool!", 'É uma pintura. Legal!'],
               ['Nina', "It's red, yellow and blue. I love it!", 'É vermelho, amarelo e azul. Eu adorei!'],
               ['Rosa', "And what's this, Nina?", 'E o que é isto, Nina?'],
               ['Nina', "It's an orange brush.", 'É um pincel laranja.'],
               ['Leo', "A brush? No way! It's a pencil!", 'Um pincel? Não acredito! É um lápis!'],
               ['Nina', "No, Leo. It's a brush. It's a green brush.", 'Não, Leo. É um pincel. É um pincel verde.'],
               ['Rosa', 'Good! Now we paint.', 'Muito bem! Agora vamos pintar.']],
        quiz=[Q('What is it? It is a…', 'O que é? É uma…', [['🖼️', 'A painting'], ['🖌️', 'A brush'], ['✏️', 'A pencil']], 0, 1, 'Leo diz: “It’s a painting.”'),
              Q('What color is the brush?', 'De que cor é o pincel?', [['🟦', 'Blue'], ['🟧', 'Orange'], ['🟩', 'Green']], 1, 4, 'Nina diz: “It’s an orange brush.”'),
              Q('What does Leo say it is?', 'O que o Leo diz que é?', [['🖌️', 'A brush'], ['🖼️', 'A painting'], ['✏️', 'A pencil']], 2, 5, 'Leo diz: “It’s a pencil!”')],
        rdg_q=dict(q='Como responder a “What’s this?” quando é um pincel laranja?', o=['It’s a orange brush.', 'It’s an orange brush.', 'It’s one orange brush.'], a=1,
                   why='Antes de som de vogal, use **an**: **an** orange brush.'),
        dictate=[["What's this?", 'O que é isto?'], ["It's a painting.", 'É uma pintura.'], ["It's an orange brush.", 'É um pincel laranja.'], ["It's red, yellow and blue.", 'É vermelho, amarelo e azul.']],
        produce=PRD('Você está na aula de arte e vê uma mesa cheia de coisas. **Pergunte o que é com What\'s this? e responda com It\'s a… / It\'s an… dizendo a cor.**',
                    "Ex.: What's this? It's a blue brush.", ["What's this?", "It's a…", "It's an…"],
                    "What's this? It's a red square. It's an orange brush.",
                    ['Perguntei com What’s this?', 'Respondi com It’s a… / It’s an…?', 'Falei uma cor?'],
                    [r"\bwhat['’]?s this\b", r"\bit['’]?s an? \w+", r'\b(?:red|yellow|blue|green|orange)\b'],
                    [[["What's this?", 'O que é isto?']], [["It's a brush.", 'É um pincel.'], ["It's an orange brush.", 'É um pincel laranja.']], [['red', 'vermelho'], ['green', 'verde']]],
                    ['Boa pergunta! ❓', 'Resposta completa! ✅', 'Cores no ponto! 🎨'],
                    ["It's a great painting! Good job!", 'É uma ótima pintura! Bom trabalho!']),
        rs=rs15(['museum', 'library', 'postoffice', 'artroom', 'bookshop', 'garden', 'pharmacy', 'bank', 'playground', 'mountain',
                 'stage', 'artroom', 'zoo', 'fair', 'beach']),
        sc='artroom')
    X = dict(
        n=9808, review=True, names=('Rosa', 'Leo'),
        stage=dict(rs='artroom', chars=[[rosa, 28, 0, 1.0], [leo, 56, 1, 1.0], [nina, 84, 1, 0.95]]),
        obra=dict(name='Composition II in Red, Blue, and Yellow', kind='🎨 Pintura · 1930', year='1930',
                  text='Pintura do artista holandês Piet Mondrian, de 1930. Ela é feita só de retângulos vermelho, azul, amarelo e branco, separados por linhas pretas bem grossas. Mondrian queria uma arte simples, com linhas e cores puras.',
                  line=["It's red, yellow and blue.", 'É vermelho, amarelo e azul. (frase do tema)'],
                  pa=dict(t='artstudio', e=['🟥', '🟦', '🟨'], p='e', v=1)),
        gancho=['Rosa', "Look at this! What's this, Leo?", 'Olhe isto! O que é isto, Leo?'],
        hot=[H('🟥', 14, 16, 'red', 'vermelho', "What's this? It's a red square.", 'O que é isto? É um quadrado vermelho.'),
             H('🟨', 40, 14, 'yellow', 'amarelo', "It's a yellow square.", 'É um quadrado amarelo.'),
             H('🟦', 66, 14, 'blue', 'azul', "What's this? It's blue.", 'O que é isto? É azul.'),
             H('🖌️', 88, 16, 'brush', 'pincel', "It's an orange brush.", 'É um pincel laranja.'),
             H('🟩', 12, 82, 'green', 'verde', "What's this? It's a green square.", 'O que é isto? É um quadrado verde.')],
        gap=[G('___ this?', 'O que é isto?', ["Who's", "What's", "Where's"], 1, 'Para perguntar “o que é”, use **What’s this?**'),
             G("It's ___ orange brush.", 'É um pincel laranja.', ['an', 'a', 'two'], 0, '**Orange** começa com som de vogal: **an** orange.'),
             G("What's this? ___ a brush.", 'O que é isto? É um pincel.', ['Is', 'It', "It's"], 2, 'A resposta começa com **It’s** (it is).'),
             G("It's ___ painting.", 'É uma pintura.', ['an', 'a', 'two'], 1, '**Painting** começa com som de consoante: **a** painting.')],
        trap=[TR(['What this is?', "What's this?", 'Is what this?'], 1, 'A ordem é **What’s** + this: What’s this?'),
              TR(["It's a orange brush.", "It's one orange brush.", "It's an orange brush."], 2, 'Antes de vogal: **an** orange brush.')],
        sticker=dict(title='Aula de arte', sub='Composition II in Red, Blue, and Yellow · 1930', rs='museum', chars=[[leo, 34, 0, 1.0], [nina, 68, 1, 1.0]]),
        speakers={'Rosa': rosa, 'Leo': leo, 'Nina': nina},
        rule=dict(who=rosa, head="What's this?", sub='Perguntar o que é e responder com It’s…',
                  say=["Look at this! What's this?", 'Olhe isto! O que é isto?'],
                  formula=[
                      dict(from_=[["What's", 1], ['this?', 0]], to=[["It's", 1], ['a brush.', 3]], say="It's a brush.", note='**What’s** = What is. Responda com **It’s** (It is) + a coisa.'),
                      dict(from_=[["What's", 1], ['this?', 0]], to=[["It's", 1], ['a', 2], ['red', 2], ['square.', 3]], say="It's a red square.", note='A cor vem **antes** do nome: a **red** square.'),
                      dict(from_=[["What's", 1], ['this?', 0]], to=[["It's", 1], ['an', 2], ['orange', 2], ['brush.', 3]], say="It's an orange brush.", note='Antes de som de vogal use **an**: an orange brush.')],
                  uses=[dict(ico='❓', tag='Perguntar', en="What's this?", pt='O que é isto?'),
                        dict(ico='🖼️', tag='Responder', en="It's a painting.", pt='É uma pintura.'),
                        dict(ico='🎨', tag='Dizer a cor', en="It's red.", pt='É vermelho.')],
                  rules=[dict(tag="What's", c=0, text='**What’s** = What is. Pergunta: o que é?', ex="What's this? = What is this?"),
                         dict(tag="It's a / an", c=2, text='Responda com **It’s a** (consoante) ou **It’s an** (vogal).', ex="It's a brush. · It's an orange brush."),
                         dict(tag='Cor antes', c=1, text='Em inglês a cor vem **antes** do nome.', ex='✗ a brush orange  →  ✓ an orange brush')],
                  tips=['Em português dizemos “O que é isso?”. Em inglês, **this** é para o que está perto de você: What’s **this**?']),
        mission_ic='🎨')
    XT = dict(
        exp=[E('👀', 'Look at this!', 'Expressão', 'Olhe isto!', 'Para **chamar a atenção** de alguém para algo.', ['Look at this! A red square!', 'Olhe isto! Um quadrado vermelho!']),
             E('😎', 'Cool!', 'Gíria', 'Legal!', 'Quando algo **é bacana**. Muito comum entre jovens.', ['A big painting? Cool!', 'Uma pintura grande? Legal!']),
             E('😲', 'No way!', 'Informal', 'Não acredito!', 'Quando você **não acredita** ou fica surpreso.', ["It's a pencil? No way!", 'É um lápis? Não acredito!']),
             E('😍', 'I love it!', 'Expressão', 'Eu adorei!', 'Para dizer que você **gostou muito** de algo.', ['I love it! It is so red!', 'Eu adorei! É tão vermelho!'])],
        exp_scene=dict(rs='museum', lines=[
            ['Rosa', "**Look at this!** What's this, Leo?", 'Olhe isto! O que é isto, Leo?'],
            ['Leo', "It's a painting. **Cool!**", 'É uma pintura. Legal!'],
            ['Nina', "It's red, yellow and blue. **I love it!**", 'É vermelho, amarelo e azul. Eu adorei!'],
            ['Rosa', "And what's this, Nina?", 'E o que é isto, Nina?'],
            ['Nina', "It's an orange brush.", 'É um pincel laranja.'],
            ['Leo', "A brush? **No way!** It's a pencil!", 'Um pincel? Não acredito! É um lápis!']]),
        lab=dict(short='th surdo', title='Laboratório de sons: o “th” de three',
                 say='O “th” inglês não existe em português. Vamos treinar com os números e os quadrados do quadro!',
                 intro=dict(what='O **th** de **three**, **thanks** e **think** é um som feito com a língua entre os dentes, só com ar, sem voz.',
                            how='Coloque a pontinha da língua entre os dentes da frente e sopre o ar de leve. Não use a voz: é só ar. Depois solte a língua.',
                            pt='Muita gente troca por **t** ou **s**: **three** vira “tree” e **think** vira “sink”. Esses erros trocam a palavra!'),
                 ex=[['three', 'THRI', 'três', 'língua entre os dentes, só ar'], ['thanks', 'THÉNKS', 'obrigado', 'th antes do “anks”'], ['think', 'THÍNK', 'pensar', 'sopre o ar, sem vibrar']],
                 pairs=[['three', 'tree', '“três” × “árvore”'], ['think', 'sink', '“pensar” × “afundar”'], ['thank', 'tank', '“agradecer” × “tanque”']],
                 tip='Morda de leve a ponta da língua e sopre devagar, como se fosse um pneu murchando. Isso é o **th**.',
                 phrase=['Thanks! Three red squares.', 'Obrigado! Três quadrados vermelhos.'],
                 rounds=[RD('three', ['three', 'tree'], 0, '**Three** (três) começa com a língua entre os dentes. **Tree** (árvore) começa com “t”.'),
                         RD('sink', ['think', 'sink'], 1, '**Sink** (afundar) começa com “s”. **Think** (pensar) começa com o “th”.'),
                         RD('tank', ['thank', 'tank'], 1, '**Tank** (tanque) começa com “t”. **Thank** (agradecer) começa com o “th”.')]),
        hunt=[HU('tree', ['three', 'tree'], 1, '**tree** (árvore) começa com “t”.'),
              HU('think', ['think', 'sink'], 0, '**think** (pensar) começa com o “th”.'),
              HU('three', [['3️⃣', ''], ['🌳', ''], ['🏊', '']], 0, '**three** = três, começa com “th”.', True),
              HU('tree', [['3️⃣', ''], ['🌳', ''], ['🏊', '']], 1, '**tree** = árvore, começa com “t”.', True),
              HU('thank', ['thank', 'tank'], 0, '**thank** (agradecer) começa com “th”.')])
    VB = dict(title='Verbos para ver e tocar', tip='Quatro verbos: see, point, find e touch.',
              items=[VBI('see', '👀', 'ver', 'I see a painting.', 'Leo see**s** a red square.', ['I see a painting.', 'Eu vejo uma pintura.'], '**see** = ver. Com he/she: **sees**.'),
                     VBI('point', '👉', 'apontar', 'I point at the brush.', 'Nina point**s** at the wall.', ['I point at the brush.', 'Eu aponto para o pincel.'], '**point** = apontar. Com he/she: **points**.'),
                     VBI('find', '🔍', 'achar', 'I find a green pencil.', 'Rosa find**s** a blue brush.', ['I find a green pencil.', 'Eu acho um lápis verde.'], '**find** = achar, encontrar. Com he/she: **finds**.'),
                     VBI('touch', '✋', 'tocar', 'I touch the paint.', 'He touch**es** the brush.', ['I touch the paint.', 'Eu toco na tinta.'], '**touch** = tocar. Com he/she: **touches** (termina em -ch, então -es).')])
    MR = dict(
        mold=[MP('Perguntar o que é', [SL('pergunta', [["What's this", 'o que é isto']])], ['?', '?']),
              MP('Responder com a cor', [SL('começo', [["It's"]] if False else [["It's", 'é']]),
                                         SL('coisa', [['a red square', 'um quadrado vermelho'], ['a yellow square', 'um quadrado amarelo'], ['a blue brush', 'um pincel azul'],
                                                      ['a green pencil', 'um lápis verde'], ['an orange brush', 'um pincel laranja'], ['a painting', 'uma pintura']])], ['.', '.']),
              MP('Falar da cor', [SL('coisa', [['The brush is', 'O pincel é'], ['The square is', 'O quadrado é'], ['The pencil is', 'O lápis é']]),
                                  SL('cor', [['red', 'vermelho'], ['yellow', 'amarelo'], ['blue', 'azul'], ['green', 'verde'], ['orange', 'laranja']])], ['.', '.'])],
        speak=[["What's this? It's a blue brush.", 'O que é isto? É um pincel azul.'], ['Look at this! I love it!', 'Olhe isto! Eu adorei!']],
        trap=[MT('“No way!” quer dizer…', ['Sem caminho!', 'Não acredito!', 'Não vou!'], 1, '**No way!** = não acredito! / de jeito nenhum!', 'No way!'),
              MT('Qual frase está certa?', ["It's an orange brush.", "It's a orange brush.", 'It is orange a brush.'], 0, 'Antes de vogal: **an** orange brush.', "It's an orange brush.")],
        gap=[MG('Look ___ this!', 'Olhe isto!', ['at', 'in', 'on'], 0, '**Look at** = olhar para.', 'Look at this!'),
             MG('I ___ it!', 'Eu adorei!', ['love', 'loves', 'am'], 0, 'Com **I**, o verbo fica sem -s: I **love** it.', 'I love it!')],
        expq=[MT('Você quer mostrar um quadro ao amigo.', ['I love it!', 'Look at this!', 'No way!'], 1, '**Look at this!** chama a atenção.'),
              MT('Você gostou muito do quadro.', ['No way!', 'Look at this!', 'I love it!'], 2, '**I love it!** = eu adorei.'),
              MT('O amigo diz que o quadro é de uma criança e você não acredita.', ['No way!', 'Cool!', 'I love it!'], 0, '**No way!** mostra que você não acredita.')],
        missions=[MS('🎨', 'Aula de arte', 'Pergunte e responda sobre as coisas.',
                     "Você está na aula de arte. **Pergunte duas vezes What's this? e responda uma delas com It's a… ou It's an….**",
                     'Escreva a sua resposta aqui…', ["What's this?"],
                     "What's this? It's a green brush. What's this?",
                     ['Perguntei com What’s this?', 'Perguntei duas vezes?', 'Respondi com It’s a… / It’s an…?'],
                     [r"\bwhat['’]?s this\b", r"(?:\bwhat['’]?s this\b[\s\S]*){2}", r"\bit['’]?s an? \w+"],
                     [[["What's this?", 'O que é isto?']], [["What's this? What's this?", 'O que é isto? O que é isto?']], [["It's a brush.", 'É um pincel.']]],
                     ['Pergunta certa! ❓', 'Duas perguntas! ✌️', 'Resposta completa! ✅'],
                     ["It's a pencil! Good job!", 'É um lápis! Bom trabalho!']),
                  MS('😎', 'No museu', 'Use as expressões do episódio.',
                     'Você vê um quadro lindo. **Chame o amigo com Look at this, diga que adorou com I love it e reaja com Cool ou No way.**',
                     'Escreva a sua resposta aqui…', ['Look at this'],
                     'Look at this! I love it! Cool!',
                     ['Chamei o amigo com Look at this?', 'Disse que adorei?', 'Reagi com Cool / No way?'],
                     [r'\blook at this\b', r'\bi love it\b', r'\b(?:cool|no way)\b'],
                     [[['Look at this!', 'Olhe isto!']], [['I love it!', 'Eu adorei!']], [['Cool!', 'Legal!'], ['No way!', 'Não acredito!']]],
                     ['Atenção chamada! 👀', 'Adorou! 😍', 'Reação certa! 😎'],
                     ['Wow! Me too!', 'Uau! Eu também!'])])
    CX = [CXI('It is the color of a tomato and of fire. The tomato is ___.', 'É a cor do tomate e do fogo. O tomate é vermelho.', 'red', 'blue', 'green'),
          CXI('The sun is round and bright. The sun is ___.', 'O sol é redondo e brilhante. O sol é amarelo.', 'yellow', 'green', 'blue'),
          CXI('Look up at the sky on a sunny day. The sky is ___.', 'Olhe para o céu num dia de sol. O céu é azul.', 'blue', 'red', 'orange'),
          CXI('The grass in the park is ___.', 'A grama do parque é verde.', 'green', 'red', 'yellow'),
          CXI('I eat an ___ for breakfast. It is a fruit, and it is also a color.', 'Eu como uma laranja no café da manhã. É uma fruta e também uma cor.', 'orange', 'brush', 'blue'),
          CXI('The artist paints with a ___ and with colors.', 'O artista pinta com um pincel e com tintas.', 'brush', 'green', 'yellow')]
    return dict(B=B, X=X, XT=XT, VB=VB, MR=MR, CX=CX)


EPS.append(ep39())


# ============================================================ 40 · It's / It isn't · Handa's Surprise
def ep40():
    handa = 'p:bun:1a1a1a:5c3a21:d35400:none:dress'
    akeyo = 'p:curly:1a1a1a:8d5524:27ae60:bow:dress'
    monkey = 'e:🐒'
    B = dict(
        title="Jogo da fruta · It's / It isn't",
        sub="Dizer o que é e o que não é: It's… / It isn't… / Is it…?",
        pattern_label="It's / It isn't",
        why="Hoje você aprende a dizer o que algo é (It's…) e o que não é (It isn't…), e a adivinhar com Is it…?",
        vocab=[['Banana', 'Banana', 'Soa como “ba-NÉ-na”.'], ['Mango', 'Manga', 'Soa como “MÉN-gou”.'], ['Orange', 'Laranja', 'Soa como “Ó-rinj”.'],
               ['Pineapple', 'Abacaxi', 'Soa como “PÁI-né-pol”.'], ['Avocado', 'Abacate', 'Soa como “a-vo-KÁ-dou”.'], ['Basket', 'Cesto', 'Soa como “BÉS-kit”.']],
        balloons=[['🍌', 'banana'], ['🥭', 'mango'], ['🍊', 'orange'], ['🍍', 'pineapple'], ['🥑', 'avocado'], ['🧺', 'basket']],
        cover_art=dict(s='fair', items=[['🧺', 104, 56, 20, 'bob'], ['🥭', 138, 44, 12, 'bob'], ['❓', 84, 34, 12, 'bob']], seed='hs1'),
        cover_sub="It isn't…? Em 10 minutos você adivinha frutas como a Handa e a Akeyo",
        cover_say='A Handa leva um cesto com uma fruta surpresa. A amiga Akeyo quer adivinhar qual é. Como dizer “é” e “não é” em inglês?',
        wrap_recap=[['Is it a banana?', 'É uma banana?'], ["No, it isn't.", 'Não, não é.'], ["It isn't yellow.", 'Não é amarelo.'], ["Yes, it is! It's an avocado.", 'Sim, é! É um abacate.']],
        teaser=dict(t='The Devil Wears Prada', d='Próximo padrão: me, him, her, us, them (pronomes depois do verbo)'),
        cast={'Handa': ['👧', '#d35400'], 'Akeyo': ['🧒', '#27ae60'], 'Monkey': ['🐒', '#a0522d']},
        lines=[['Handa', 'Akeyo, I have a surprise in my basket!', 'Akeyo, tenho uma surpresa no meu cesto!'],
               ['Akeyo', 'Is it a banana?', 'É uma banana?'],
               ['Handa', "No, it isn't. It isn't yellow.", 'Não, não é. Não é amarelo.'],
               ['Akeyo', 'Is it an orange?', 'É uma laranja?'],
               ['Handa', "No, it isn't. It's green!", 'Não, não é. É verde!'],
               ['Akeyo', 'Is it an avocado?', 'É um abacate?'],
               ['Handa', "Yes, it is! It's an avocado.", 'Sim, é! É um abacate.'],
               ['Monkey', 'Mmm! Thank you, Handa!', 'Hum! Obrigado, Handa!']],
        quiz=[Q('Is the surprise a banana?', 'A surpresa é uma banana?', [['✅', 'Yes, it is'], ['❌', "No, it isn't"], ['🤷', 'Maybe']], 1, 2, 'Handa diz: “No, it isn’t.”'),
              Q('What is the surprise?', 'Qual é a surpresa?', [['🥭', 'A mango'], ['🍊', 'An orange'], ['🥑', 'An avocado']], 2, 6, 'Handa diz: “It’s an avocado.”'),
              Q('Who says “Thank you, Handa”?', 'Quem diz “Thank you, Handa”?', [['🐒', 'The monkey'], ['👧', 'Handa'], ['🧒', 'Akeyo']], 0, 7, 'O macaco diz: “Thank you, Handa!”')],
        rdg_q=dict(q='Qual é a resposta curta certa para “Is it a mango?” quando NÃO é?', o=['No, it not.', "No, it isn't.", "No, it doesn't."], a=1,
                   why='A resposta negativa curta é **No, it isn’t.**'),
        dictate=[['Is it a banana?', 'É uma banana?'], ["No, it isn't.", 'Não, não é.'], ["It isn't yellow. It's green.", 'Não é amarelo. É verde.'], ["Yes, it is! It's an avocado.", 'Sim, é! É um abacate.']],
        produce=PRD('A Handa esconde uma fruta no cesto. **Faça duas perguntas com Is it…? e responda a uma delas com Yes, it is ou No, it isn\'t.**',
                    "Ex.: Is it a mango? Is it a banana? No, it isn't.", ['Is it…?', 'Yes, it is.', "No, it isn't."],
                    "Is it a mango? Is it a banana? No, it isn't.",
                    ['Fiz uma pergunta com Is it…?', 'Fiz duas perguntas?', 'Usei Yes, it is / No, it isn’t?'],
                    [r'\bis it\b[^.!?]*\?', r'(?:\bis it\b[^.!?]*\?[\s\S]*){2}', r"\b(?:yes,?\s*it is|no,?\s*it (?:isn['’]t|is not))\b"],
                    [[['Is it a mango?', 'É uma manga?']], [['Is it a banana? Is it an orange?', 'É uma banana? É uma laranja?']], [['Yes, it is.', 'Sim, é.'], ["No, it isn't.", 'Não, não é.']]],
                    ['Boa pergunta! ❓', 'Duas perguntas! ✌️', 'Resposta curta certa! ✅'],
                    ["Yes, it is! It's a mango!", 'Sim, é! É uma manga!']),
        rs=rs15(['farm', 'zoo', 'supermarket', 'fair', 'garden', 'bakery', 'pool', 'beach', 'playground', 'forest',
                 'harbor', 'fair', 'mountain', 'busstop', 'stadium']),
        sc='fair')
    X = dict(
        n=7009808, review=True, names=('Handa', 'Akeyo'),
        stage=dict(rs='fair', chars=[[handa, 28, 0, 1.0], [akeyo, 56, 1, 1.0], [monkey, 84, 1, 0.9]]),
        obra=dict(name="Handa's Surprise", kind='📖 Livro infantil · 1994', year='1994',
                  text='Livro infantil da autora britânica Eileen Browne, de 1994. A menina Handa, do povo Luo do Quênia, leva um cesto com sete frutas para a amiga Akeyo. No caminho, animais pegam as frutas sem ela perceber.',
                  line=["It's a surprise!", 'É uma surpresa! (frase do tema)'],
                  pa=dict(t='picnic', e=['🧺', '🥭', '🐒'], p='d', v=1)),
        gancho=['Handa', 'Akeyo, I have a surprise in my basket!', 'Akeyo, tenho uma surpresa no meu cesto!'],
        hot=[H('🍌', 14, 16, 'banana', 'banana', "Is it a banana? No, it isn't.", 'É uma banana? Não, não é.'),
             H('🥭', 40, 14, 'mango', 'manga', "It's a mango. It isn't green.", 'É uma manga. Não é verde.'),
             H('🍍', 66, 14, 'pineapple', 'abacaxi', "Is it a pineapple? Yes, it is!", 'É um abacaxi? Sim, é!'),
             H('🥑', 88, 16, 'avocado', 'abacate', "It's an avocado. It's green.", 'É um abacate. É verde.'),
             H('🧺', 12, 82, 'basket', 'cesto', "Is it a basket? Yes, it is.", 'É um cesto? Sim, é.')],
        gap=[G('___ it a mango?', 'É uma manga?', ['Is', 'Are', 'Do'], 0, 'Para perguntar com **it**, use **Is it…?**'),
             G('No, it ___.', 'Não, não é.', ['not', "isn't", "don't"], 1, 'Resposta negativa curta: **No, it isn’t.**'),
             G("It ___ yellow. It's green.", 'Não é amarelo. É verde.', ["aren't", "doesn't", "isn't"], 2, 'Com **it**, a negativa é **isn’t** (is not).'),
             G('Yes, it ___.', 'Sim, é.', ['are', 'is', "it's"], 1, 'A resposta curta afirmativa repete o verbo: Yes, it **is**.')],
        trap=[TR(['It no is green.', "It isn't green.", 'It not green isn\'t.'], 1, 'Para negar, **isn’t** vem depois de it: It **isn’t** green.'),
              TR(["Yes, it's.", 'Yes, it are.', 'Yes, it is.'], 2, 'Na resposta curta afirmativa não se contrai: Yes, it **is**.')],
        sticker=dict(title='Handa e Akeyo', sub="Handa's Surprise · 1994", rs='farm', chars=[[handa, 34, 0, 1.0], [akeyo, 68, 1, 1.0]]),
        speakers={'Handa': handa, 'Akeyo': akeyo, 'Monkey': monkey},
        rule=dict(who=handa, head="It's / It isn't", sub='Dizer o que é e o que não é.',
                  say=["No, it isn't. It isn't yellow.", 'Não, não é. Não é amarelo.'],
                  formula=[
                      dict(from_=[['It', 0], ['is', 1], ['green.', 3]], to=[['It', 0], ["isn't", 1], ['green.', 3]], say="It isn't green.", note='Para negar, junte **not**: is + not = **isn’t**.'),
                      dict(from_=[["It's", 0], ['a banana.', 3]], to=[['Is', 1], ['it', 0], ['a banana?', 3]], say='Is it a banana?', note='Na pergunta, **is** passa para a frente de **it**.'),
                      dict(from_=[['Is', 1], ['it', 0], ['a mango?', 3]], to=[['No,', 1], ['it', 0], ["isn't.", 2]], say="No, it isn't.", note='Resposta curta: repita **it** e o verbo.')],
                  uses=[dict(ico='🍌', tag='Adivinhar', en='Is it a banana?', pt='É uma banana?'),
                        dict(ico='✅', tag='Responder sim', en='Yes, it is.', pt='Sim, é.'),
                        dict(ico='❌', tag='Responder não', en="No, it isn't.", pt='Não, não é.')],
                  rules=[dict(tag="It isn't", c=1, text='Negativa com **it**: **isn’t** (ou **It’s not**).', ex="It isn't yellow. = It's not yellow."),
                         dict(tag='Is it…?', c=0, text='Pergunta com **it**: o verbo vem primeiro.', ex='Is it a mango?'),
                         dict(tag='Yes, it is', c=2, text='Resposta curta **sim**: não se contrai.', ex='✗ Yes, it’s  →  ✓ Yes, it is')],
                  tips=['Em português a negativa usa “não” antes: “não é”. Em inglês o **not** vem depois do verbo: it is **not** → it **isn’t**.']),
        mission_ic='🥭')
    XT = dict(
        exp=[E('🤫', 'Guess what!', 'Expressão', 'Adivinhe só!', 'Para **dar uma novidade** ou começar um jogo de adivinhação.', ['Guess what! I have a surprise.', 'Adivinhe só! Eu tenho uma surpresa.']),
             E('🎯', 'Good guess!', 'Expressão', 'Bom palpite!', 'Quando alguém **chega perto** da resposta ou acerta.', ['Good guess! It is a mango.', 'Bom palpite! É uma manga.']),
             E('🙃', 'Not really.', 'Informal', 'Na verdade, não.', 'Jeito **suave** de dizer não.', ['Is it big? Not really.', 'É grande? Na verdade, não.']),
             E('😋', 'Yum!', 'Informal', 'Hum, que delícia!', 'Quando a comida **parece boa** ou está boa.', ['Yum! A sweet mango!', 'Hum! Uma manga doce!'])],
        exp_scene=dict(rs='farm', lines=[
            ['Handa', '**Guess what!** I have a surprise.', 'Adivinhe só! Eu tenho uma surpresa.'],
            ['Akeyo', 'Is it a mango?', 'É uma manga?'],
            ['Handa', "**Not really.** It isn't yellow.", 'Na verdade, não. Não é amarelo.'],
            ['Akeyo', 'Is it an avocado?', 'É um abacate?'],
            ['Handa', '**Good guess!** Yes, it is!', 'Bom palpite! Sim, é!'],
            ['Monkey', '**Yum!** Thank you, Handa!', 'Hum, que delícia! Obrigado, Handa!']]),
        lab=dict(short='i curto', title='Laboratório de sons: o “i” curto de it',
                 say='Em inglês, o “i” de it e o “ee” de eat são sons diferentes. Vamos treinar com as frutas!',
                 intro=dict(what='O **i** curto de **it**, **is** e **six** é rápido e relaxado, bem diferente do **ee** longo de **eat**.',
                            how='Para o **i** curto, os lábios ficam soltos e o som dura pouco. Para o **ee** longo, os lábios esticam como num sorriso e o som é mais comprido.',
                            pt='Em português o “i” é sempre igual. Em inglês ele muda o sentido: **it** (isso) ≠ **eat** (comer), **sit** (sentar) ≠ **seat** (assento).'),
                 ex=[['it', 'ÍT', 'isso, ele', 'curto, lábios soltos'], ['is', 'ÍZ', 'é, está', 'curto, sem esticar'], ['six', 'SÍKS', 'seis', 'o i dura bem pouco']],
                 pairs=[['it', 'eat', 'curto × longo, com sorriso'], ['sit', 'seat', '“sentar” × “assento”'], ['bit', 'beat', '“pedaço” × “bater”']],
                 tip='Sorria bem aberto para o **ee** de eat. Para o **i** de it, deixe o rosto solto, sem sorrir.',
                 phrase=['Is it big? Yes, it is.', 'É grande? Sim, é.'],
                 rounds=[RD('eat', ['it', 'eat'], 1, '**Eat** (comer) tem o som longo, com sorriso. **It** é curto.'),
                         RD('sit', ['sit', 'seat'], 0, '**Sit** (sentar) tem o som curto. **Seat** (assento) é longo.'),
                         RD('beat', ['bit', 'beat'], 1, '**Beat** (bater) tem o som longo. **Bit** (pedaço) é curto.')]),
        hunt=[HU('eat', ['it', 'eat'], 1, '**eat** (comer) tem o “ee” longo.'),
              HU('sit', ['sit', 'seat'], 0, '**sit** (sentar) tem o “i” curto.'),
              HU('bit', ['bit', 'beat'], 0, '**bit** (pedaço) é curto.'),
              HU('seat', [['🪑', ''], ['🍽️', ''], ['🐑', '']], 0, '**seat** = assento, cadeira.', True),
              HU('beat', ['bit', 'beat'], 1, '**beat** (bater) tem o “ee” longo.')])
    VB = dict(title='Verbos para o jogo da fruta', tip='Quatro verbos: pick, peel, taste e guess.',
              items=[VBI('pick', '🧺', 'colher', 'I pick a mango.', 'Handa pick**s** a banana.', ['I pick a mango.', 'Eu colho uma manga.'], '**pick** = colher, escolher. Com he/she: **picks**.'),
                     VBI('peel', '🍌', 'descascar', 'I peel a banana.', 'Akeyo peel**s** an orange.', ['I peel a banana.', 'Eu descasco uma banana.'], '**peel** = descascar. Com he/she: **peels**.'),
                     VBI('taste', '👅', 'provar', 'I taste the mango.', 'The monkey taste**s** the avocado.', ['I taste the mango.', 'Eu provo a manga.'], '**taste** = provar. Com he/she: **tastes**.'),
                     VBI('guess', '🤔', 'adivinhar', 'I guess a fruit.', 'Akeyo guess**es** the fruit.', ['I guess a fruit.', 'Eu adivinho uma fruta.'], '**guess** = adivinhar. Com he/she: **guesses** (termina em -ss, então -es).')])
    MR = dict(
        mold=[MP('Adivinhar com Is it…?', [SL('pergunta', [['Is it', 'é']]),
                                           SL('fruta', [['a banana', 'uma banana'], ['a mango', 'uma manga'], ['an orange', 'uma laranja'], ['a pineapple', 'um abacaxi'],
                                                        ['an avocado', 'um abacate'], ['a basket', 'um cesto']])], ['?', '?']),
              MP('Responder', [SL('resposta', [['Yes, it is', 'sim, é'], ["No, it isn't", 'não, não é']])], ['.', '.']),
              MP('Dizer o que não é', [SL('começo', [["It isn't", 'não é']]),
                                       SL('palavra', [['yellow', 'amarelo'], ['green', 'verde'], ['orange', 'laranja'], ['big', 'grande'], ['small', 'pequeno']])], ['.', '.'])],
        speak=[["Is it a mango? No, it isn't.", 'É uma manga? Não, não é.'], ['Guess what! Yum!', 'Adivinhe só! Hum, que delícia!']],
        trap=[MT('“Not really.” quer dizer…', ['Na verdade, não.', 'Não é real.', 'Realmente sim.'], 0, '**Not really.** = na verdade, não (um “não” suave).', 'Not really.'),
              MT('Qual frase está certa?', ["It's isn't big.", "It isn't big.", 'It no is big.'], 1, 'Negativa: it + **isn’t** + palavra.', "It isn't big.")],
        gap=[MG('Is it ___ mango?', 'É uma manga?', ['a', 'an', 'one'], 0, '**Mango** começa com som de consoante: **a** mango.', 'Is it a mango?'),
             MG('___ what! I have a surprise.', 'Adivinhe só! Eu tenho uma surpresa.', ['Guess', 'Guessing', 'Guesses'], 0, 'A expressão é **Guess what!**', 'Guess what! I have a surprise.')],
        expq=[MT('O amigo acerta quase tudo. O que você diz?', ['Not really.', 'Yum!', 'Good guess!'], 2, '**Good guess!** elogia o palpite.'),
              MT('Você quer começar um jogo de adivinhação.', ['Guess what!', 'Yum!', 'Not really.'], 0, '**Guess what!** chama a atenção para a novidade.'),
              MT('Você prova uma manga deliciosa.', ['Not really.', 'Good guess!', 'Yum!'], 2, '**Yum!** mostra que está gostoso.')],
        missions=[MS('🥭', 'Jogo de adivinhação', 'Adivinhe e responda com is / isn\'t.',
                     'Seu amigo esconde uma fruta. **Faça duas perguntas com Is it…? e responda com Yes, it is ou No, it isn\'t.**',
                     'Escreva a sua resposta aqui…', ['Is it'],
                     "Is it a banana? No, it isn't. Is it an orange? Yes, it is!",
                     ['Fiz uma pergunta com Is it…?', 'Fiz duas perguntas?', 'Usei Yes, it is / No, it isn’t?'],
                     [r'\bis it\b[^.!?]*\?', r'(?:\bis it\b[^.!?]*\?[\s\S]*){2}', r"\b(?:yes,?\s*it is|no,?\s*it (?:isn['’]t|is not))\b"],
                     [[['Is it a mango?', 'É uma manga?']], [['Is it a banana? Is it an orange?', 'É uma banana? É uma laranja?']], [['Yes, it is.', 'Sim, é.'], ["No, it isn't.", 'Não, não é.']]],
                     ['Pergunta certa! ❓', 'Duas perguntas! ✌️', 'Resposta curta certa! ✅'],
                     ['Yes, it is! Good guess!', 'Sim, é! Bom palpite!']),
                  MS('🤫', 'Surpresa!', 'Use as expressões do episódio.',
                     'Você tem uma surpresa para o amigo. **Comece com Guess what, elogie o palpite com Good guess e prove a fruta com Yum.**',
                     'Escreva a sua resposta aqui…', ['Guess what'],
                     'Guess what! Good guess! Yum!',
                     ['Comecei com Guess what?', 'Elogiei com Good guess?', 'Disse Yum?'],
                     [r'\bguess what\b', r'\bgood guess\b', r'\byum\b'],
                     [[['Guess what!', 'Adivinhe só!']], [['Good guess!', 'Bom palpite!']], [['Yum!', 'Hum, que delícia!']]],
                     ['Novidade! 🤫', 'Elogio! 🎯', 'Delícia! 😋'],
                     ['Wow! A surprise for me?', 'Uau! Uma surpresa para mim?'])])
    CX = [CXI('Monkeys love this long yellow fruit. It is a ___.', 'Os macacos adoram esta fruta comprida e amarela. É uma banana.', 'banana', 'basket', 'mango'),
          CXI('It is a sweet tropical fruit with orange juice inside. It is a ___.', 'É uma fruta tropical doce, com suco alaranjado por dentro. É uma manga.', 'mango', 'basket', 'avocado'),
          CXI('You make juice from this round fruit. It is also a color: ___.', 'Você faz suco com esta fruta redonda. Também é uma cor: laranja.', 'orange', 'pineapple', 'basket'),
          CXI('It has a spiky green top and a sweet yellow inside. It is a ___.', 'Tem um topo verde com espinhos e é doce e amarelo por dentro. É um abacaxi.', 'pineapple', 'banana', 'basket'),
          CXI('It is green outside, and people make guacamole with it. It is an ___.', 'É verde por fora, e com ele se faz guacamole. É um abacate.', 'avocado', 'orange', 'mango'),
          CXI('Handa carries her fruit in a ___ on her head.', 'A Handa leva as frutas num cesto na cabeça.', 'basket', 'mango', 'banana')]
    return dict(B=B, X=X, XT=XT, VB=VB, MR=MR, CX=CX)


EPS.append(ep40())


# ============================================================ 41 · me, him, her, us, them · The Devil Wears Prada
def ep41():
    andy = 'p:long:6b3f26:f4c7a1:2c3e50:none:suit'
    miranda = 'p:short:d9d9d9:f4c7a1:111111:glasses:suit'
    nigel = 'p:bald:2b2b2b:c68642:7f8c8d:glasses:suit'
    B = dict(
        title='Me, him, her, us · Pronomes depois do verbo',
        sub='I → me, he → him, she → her, we → us, they → them',
        pattern_label='me · him · her · us · them',
        why='Hoje você aprende os pronomes que vêm depois do verbo: help me, look at her, I like them.',
        vocab=[['Black', 'Preto', 'Soa como “BLÉK”.'], ['White', 'Branco', 'Soa como “UÁIT”.'], ['Pink', 'Rosa', 'Soa como “PÍNK”.'],
               ['Purple', 'Roxo', 'Soa como “PÂR-pol”.'], ['Brown', 'Marrom', 'Soa como “BRÁUN”.'], ['Shirt', 'Camisa', 'Soa como “SHÂRT”.']],
        balloons=[['⚫', 'black'], ['⚪', 'white'], ['🌸', 'pink'], ['🟣', 'purple'], ['🟤', 'brown'], ['👔', 'shirt']],
        cover_art=dict(s='meetingroom', items=[['👔', 104, 56, 20, 'bob'], ['👜', 138, 44, 12, 'bob'], ['👠', 84, 34, 12, 'bob']], seed='dp1'),
        cover_sub='me, him, her, us, them. Em 10 minutos você fala de pessoas e coisas como na redação de uma revista de moda',
        cover_say='Na redação de uma revista de moda, todo mundo precisa de ajuda. Andy ajuda Nigel, Nigel ajuda Andy, e a chefe precisa de todos. Como dizer “me ajude”, “olhe para ela” e “eu gosto deles”?',
        wrap_recap=[['Can you help me?', 'Você pode me ajudar?'], ['Look at her!', 'Olhe para ela!'], ['I like them.', 'Eu gosto deles.'], ['She needs us.', 'Ela precisa de nós.']],
        teaser=dict(t='Baa, Baa, Black Sheep', d='Próximo padrão: a cor vem antes do nome (a black sheep)'),
        cast={'Andy': ['👩', '#2c3e50'], 'Miranda': ['👩‍💼', '#111111'], 'Nigel': ['👨', '#7f8c8d']},
        lines=[['Andy', 'Nigel, can you help me? I need a shirt.', 'Nigel, você pode me ajudar? Preciso de uma camisa.'],
               ['Nigel', 'Sure! Look at this white shirt. I love it!', 'Claro! Olhe esta camisa branca. Eu adoro!'],
               ['Andy', "It's nice! Miranda is here. Look at her!", 'É bonita! A Miranda está aqui. Olhe para ela!'],
               ['Miranda', 'Andy, Nigel, I need you now.', 'Andy, Nigel, preciso de vocês agora.'],
               ['Nigel', 'The brown bags are for you, Miranda. I like them.', 'As bolsas marrons são para você, Miranda. Eu gosto delas.'],
               ['Miranda', 'Good. Come with me.', 'Bom. Venham comigo.'],
               ['Andy', 'Quick, Nigel! She needs us.', 'Rápido, Nigel! Ela precisa de nós.'],
               ['Nigel', 'OK! I like Andy. I help her and she helps me.', 'Certo! Eu gosto da Andy. Eu a ajudo e ela me ajuda.']],
        quiz=[Q('What does Andy need?', 'De que a Andy precisa?', [['👔', 'A shirt'], ['👜', 'A bag'], ['👠', 'Shoes']], 0, 0, 'Andy diz: “I need a shirt.”'),
              Q('What color are the bags?', 'De que cor são as bolsas?', [['⚫', 'Black'], ['🟤', 'Brown'], ['⚪', 'White']], 1, 4, 'Nigel diz: “The brown bags…”'),
              Q('Who needs Andy and Nigel?', 'Quem precisa da Andy e do Nigel?', [['👨', 'Nigel'], ['👩', 'Andy'], ['👩‍💼', 'Miranda']], 2, 3, 'Miranda diz: “I need you now.”')],
        rdg_q=dict(q='Qual palavra completa: “Nigel can help ___.” (ajudar a mim)', o=['I', 'me', 'my'], a=1,
                   why='Depois do verbo, use **me**: help **me**. (**I** é só antes do verbo.)'),
        dictate=[['Can you help me?', 'Você pode me ajudar?'], ['Look at her!', 'Olhe para ela!'], ['I like them.', 'Eu gosto deles.'], ['She needs us.', 'Ela precisa de nós.']],
        produce=PRD('Você está numa loja de roupas com um amigo. **Peça ajuda com help me, diga que gosta de uma roupa com it ou them e fale de uma pessoa com him ou her.**',
                    'Ex.: Can you help me? I like it. Look at her!', ['help me', 'I like it', 'Look at him'],
                    'Can you help me? I like it. Look at her!',
                    ['Pedi ajuda com help me?', 'Falei de uma roupa com it ou them?', 'Falei de uma pessoa com him ou her?'],
                    [r'\bhelp me\b', r'\b(?:love|like|need) (?:it|them)\b', r'\b(?:at|with|for|help|call) (?:him|her)\b'],
                    [[['Can you help me?', 'Você pode me ajudar?']], [['I like it.', 'Eu gosto dele(a).'], ['I love them.', 'Eu adoro eles(as).']], [['Look at her!', 'Olhe para ela!'], ['Call him!', 'Ligue para ele!']]],
                    ['Pediu ajuda! 🙋', 'Roupa certa! 👔', 'Pessoa certa! 👀'],
                    ['Sure! I help you. Look at this one!', 'Claro! Eu ajudo você. Olhe este aqui!']),
        rs=rs15(['hotelroom', 'bank', 'stadium', 'library', 'playground', 'restaurant', 'pharmacy', 'harbor', 'zoo', 'forest',
                 'musicroom', 'meetingroom', 'postoffice', 'pool', 'christmas']),
        sc='meetingroom')
    X = dict(
        n=70015, review=True, names=('Andy', 'Nigel'),
        stage=dict(rs='meetingroom', chars=[[andy, 28, 0, 1.0], [miranda, 56, 1, 1.0], [nigel, 84, 1, 0.95]]),
        obra=dict(name='The Devil Wears Prada', kind='🎬 Filme · 2006', year='2006',
                  text='Filme de 2006 baseado no romance de Lauren Weisberger. A jovem Andy consegue trabalho numa famosa revista de moda e aprende a lidar com a chefe exigente, Miranda, e com o colega Nigel.',
                  line=['Look at her!', 'Olhe para ela! (frase do tema)'],
                  pa=dict(t='runway', e=['👠', '👜', '🧥'], p='f', v=0)),
        gancho=['Andy', 'Nigel, can you help me? I need a shirt.', 'Nigel, você pode me ajudar? Preciso de uma camisa.'],
        hot=[H('👔', 14, 16, 'shirt', 'camisa', 'I love it!', 'Eu adoro!'),
             H('👜', 40, 14, 'bag', 'bolsa', 'Give it to me, please.', 'Dê para mim, por favor.'),
             H('🧥', 66, 14, 'jacket', 'jaqueta', 'The jacket is for her.', 'A jaqueta é para ela.'),
             H('👠', 88, 16, 'shoes', 'sapatos', 'I like them.', 'Eu gosto deles.'),
             H('📱', 12, 82, 'phone', 'telefone', 'Call me!', 'Ligue para mim!')],
        gap=[G('Look at ___!', 'Olhe para ela!', ['she', 'her', 'hers'], 1, 'Depois do verbo/preposição, use **her**: look at **her**.'),
             G('Nigel can help ___.', 'O Nigel pode me ajudar.', ['me', 'I', 'my'], 0, 'Depois do verbo, **me**: help **me**.'),
             G('She needs ___. (nós)', 'Ela precisa de nós.', ['we', 'our', 'us'], 2, 'Depois do verbo, **us**: needs **us**.'),
             G('I like the shoes. I love ___.', 'Eu gosto dos sapatos. Eu os adoro.', ['they', 'them', 'their'], 1, 'Para coisas no plural, depois do verbo: **them**.')],
        trap=[TR(['Help I, please.', 'Help me, please.', 'Help my, please.'], 1, 'Depois do verbo, use **me**: help **me**.'),
              TR(['I see she.', 'I see hers.', 'I see her.'], 2, 'Depois do verbo, **her**: I see **her**.')],
        sticker=dict(title='Andy e Nigel', sub='The Devil Wears Prada · 2006', rs='hotelroom', chars=[[andy, 34, 0, 1.0], [nigel, 68, 1, 1.0]]),
        speakers={'Andy': andy, 'Miranda': miranda, 'Nigel': nigel},
        rule=dict(who=andy, head='me · him · her · us · them', sub='Pronomes que vêm depois do verbo.',
                  say=['Nigel, can you help me?', 'Nigel, você pode me ajudar?'],
                  pairsHead='👀 Antes do verbo → depois do verbo',
                  pairs=[dict(ico='🙋', a='I', b='<u>me</u>', pta='eu', ptb='me, mim', n=1),
                         dict(ico='👨', a='he', b='<u>him</u>', pta='ele', ptb='o, ele', n=1),
                         dict(ico='👩', a='she', b='<u>her</u>', pta='ela', ptb='a, ela', n=1),
                         dict(ico='👫', a='we', b='<u>us</u>', pta='nós', ptb='nos, nós', n=2),
                         dict(ico='👥', a='they', b='<u>them</u>', pta='eles/elas', ptb='os, as, eles', n=2)],
                  uses=[dict(ico='🙋', tag='Pedir ajuda', en='Can you help me?', pt='Você pode me ajudar?'),
                        dict(ico='👀', tag='Olhar', en='Look at her!', pt='Olhe para ela!'),
                        dict(ico='❤️', tag='Gostar', en='I like them.', pt='Eu gosto deles.')],
                  rules=[dict(tag='Depois do verbo', c=0, text='Depois de um verbo ou de **at, with, for**, use **me, him, her, us, them**.', ex='Look at her. · Come with me.'),
                         dict(tag='it e you', c=2, text='**it** e **you** não mudam.', ex='I love it. · I need you.'),
                         dict(tag='Antes do verbo', c=1, text='Antes do verbo, use **I, he, she, we, they**.', ex='She needs us. · We need her.')],
                  tips=['Em português dizemos “me ajude”. Em inglês o pronome vem **depois** do verbo: help **me**, look at **her**. Não diga “help I”.']),
        mission_ic='👔')
    XT = dict(
        exp=[E('✨', 'It looks good on you.', 'Expressão', 'Fica bem em você.', 'Elogio quando uma roupa **combina com a pessoa**.', ['The black shirt looks good on you.', 'A camisa preta fica bem em você.']),
             E('😎', "That's so me!", 'Gíria', 'Isso é a minha cara!', 'Quando algo **combina com o seu estilo**.', ["A purple bag? That's so me!", 'Uma bolsa roxa? Isso é a minha cara!']),
             E('🙅', "It's not for me.", 'Expressão', 'Não é para mim.', 'Jeito educado de dizer que **não é o seu estilo**.', ["Pink? Thanks, but it's not for me.", 'Rosa? Obrigado, mas não é para mim.']),
             E('🙏', 'Thanks a lot!', 'Informal', 'Muito obrigado!', 'Agradecimento **caloroso**, comum no dia a dia.', ['You help me? Thanks a lot!', 'Você me ajuda? Muito obrigado!'])],
        exp_scene=dict(rs='stage', lines=[
            ['Andy', "Look at this purple bag. **That's so me!**", 'Olhe esta bolsa roxa. Isso é a minha cara!'],
            ['Nigel', 'Yes! **It looks good on you.**', 'Sim! Fica bem em você.'],
            ['Miranda', 'Andy, look at the pink shirt. It is for you.', 'Andy, olhe a camisa rosa. É para você.'],
            ['Andy', "Pink? **It's not for me**, Miranda.", 'Rosa? Não é para mim, Miranda.'],
            ['Nigel', 'Andy, take the brown bag. It is nice.', 'Andy, pegue a bolsa marrom. É bonita.'],
            ['Andy', '**Thanks a lot**, Nigel!', 'Muito obrigada, Nigel!']]),
        lab=dict(short='h aspirado', title='Laboratório de sons: o “h” de him e her',
                 say='Em inglês o “h” é um sopro de ar. Em português ele é mudo! Vamos treinar com os pronomes.',
                 intro=dict(what='O **h** de **him**, **her**, **hat** e **help** é um sopro leve de ar saindo da garganta, como quando você bafeja no vidro.',
                            how='Abra a boca, solte o ar como um “rrrr” bem fraquinho e já emende a vogal. Não vibre a garganta.',
                            pt='Em português o **h** não tem som (hotel, hoje). Se você pular o **h** em inglês, **hat** (chapéu) vira **at** e **hold** (segurar) vira **old** (velho).'),
                 ex=[['him', 'HÍM', 'ele (depois do verbo)', 'sopro de ar antes do i'], ['her', 'HÃR', 'ela', 'sopre e emende o “ãr”'], ['help', 'HÉLP', 'ajuda, ajudar', 'ar saindo no começo']],
                 pairs=[['at', 'hat', 'sem sopro × com sopro'], ['eat', 'heat', '“comer” × “calor”'], ['old', 'hold', '“velho” × “segurar”']],
                 tip='Coloque a mão na frente da boca e diga **hat**. Você deve sentir o ar quente na mão. Em **at**, quase nada.',
                 phrase=['Help him, help her, help me.', 'Ajude ele, ajude ela, me ajude.'],
                 rounds=[RD('hat', ['at', 'hat'], 1, '**Hat** (chapéu) começa com sopro de ar. **At** não tem sopro.'),
                         RD('eat', ['eat', 'heat'], 0, '**Eat** (comer) não tem sopro. **Heat** (calor) começa com o “h”.'),
                         RD('hold', ['old', 'hold'], 1, '**Hold** (segurar) começa com o “h”. **Old** (velho) não.')]),
        hunt=[HU('him', ['him', 'in'], 0, '**him** começa com o sopro do “h”.'),
              HU('heat', ['eat', 'heat'], 1, '**heat** (calor) tem o “h” soprado.'),
              HU('hat', [['🎩', ''], ['🐜', ''], ['👂', '']], 0, '**hat** = chapéu, começa com sopro.', True),
              HU('old', ['old', 'hold'], 0, '**old** (velho) não tem sopro.'),
              HU('hold', ['old', 'hold'], 1, '**hold** (segurar) tem o “h”.')])
    VB = dict(title='Verbos para ajudar e chamar', tip='Quatro verbos: help, need, call e love.',
              items=[VBI('help', '🤝', 'ajudar', 'I help him.', 'Nigel help**s** Andy.', ['I help him.', 'Eu o ajudo.'], '**help** = ajudar. Com he/she: **helps**.'),
                     VBI('need', '🆘', 'precisar de', 'I need you.', 'Miranda need**s** us.', ['I need you.', 'Eu preciso de você.'], '**need** = precisar de. Com he/she: **needs**.'),
                     VBI('call', '📞', 'ligar para', 'I call her.', 'Andy call**s** Nigel.', ['I call her.', 'Eu ligo para ela.'], '**call** = ligar para. Com he/she: **calls**.'),
                     VBI('love', '❤️', 'adorar', 'I love them.', 'She love**s** the shoes.', ['I love them.', 'Eu os adoro.'], '**love** = adorar, amar. Com he/she: **loves**.')])
    MR = dict(
        mold=[MP('Olhar e gostar', [SL('verbo', [['Look at', 'olhe para'], ['I like', 'eu gosto de'], ['I love', 'eu adoro']]),
                                    SL('pronome', [['me', 'mim'], ['him', 'ele'], ['her', 'ela'], ['us', 'nós'], ['them', 'eles/elas'], ['it', 'isso']])], ['.', '.']),
              MP('Pedir ajuda', [SL('verbo', [['Help', 'ajude'], ['Call', 'ligue para'], ['Wait for', 'espere por']]),
                                 SL('pronome', [['me', 'mim'], ['him', 'ele'], ['her', 'ela'], ['us', 'nós'], ['them', 'eles/elas']])], ['!', '!']),
              MP('Precisar', [SL('começo', [['I need', 'eu preciso de']]), SL('pronome', [['it', 'isso'], ['them', 'eles/elas'], ['you', 'você']])], ['.', '.'])],
        speak=[['Can you help me? Thanks a lot!', 'Você pode me ajudar? Muito obrigado!'], ["That's so me! I love it.", 'Isso é a minha cara! Eu adorei.']],
        trap=[MT('“It’s not for me.” quer dizer…', ['Não é para mim.', 'Eu não sou isso.', 'Não tenho isso.'], 0, '**It’s not for me.** = não é para mim (não é o meu estilo).', "It's not for me."),
              MT('Qual frase está certa?', ['Look at she.', 'Look at her.', 'Look at hers.'], 1, 'Depois de **at**, use **her**.', 'Look at her.')],
        gap=[MG('Can you help ___?', 'Você pode me ajudar?', ['me', 'I', 'my'], 0, 'Depois do verbo, **me**.', 'Can you help me?'),
             MG('It looks good ___ you.', 'Fica bem em você.', ['on', 'in', 'at'], 0, 'A expressão é **looks good on you**.', 'It looks good on you.')],
        expq=[MT('Seu amigo experimenta uma camisa que ficou ótima.', ['It looks good on you.', "It's not for me.", 'Thanks a lot!'], 0, '**It looks good on you.** é um elogio.'),
              MT('Alguém lhe mostra uma roupa que não é o seu estilo.', ['Thanks a lot!', "That's so me!", "It's not for me."], 2, "**It's not for me.** recusa com educação."),
              MT('Você vê uma bolsa que tem tudo a ver com você.', ["That's so me!", "It's not for me.", 'It looks good on you.'], 0, "**That's so me!** = isso é a minha cara.")],
        missions=[MS('👔', 'Na loja', 'Use os pronomes depois do verbo.',
                     'Você vai às compras com uma amiga. **Peça ajuda com help me, diga que gosta de uma roupa com it ou them e fale dela com him ou her.**',
                     'Escreva a sua resposta aqui…', ['help me'],
                     'Can you help me? I like it. Look at her!',
                     ['Pedi ajuda com help me?', 'Falei de uma roupa com it ou them?', 'Falei de uma pessoa com him ou her?'],
                     [r'\bhelp me\b', r'\b(?:love|like|need) (?:it|them)\b', r'\b(?:at|with|for|help|call) (?:him|her)\b'],
                     [[['Can you help me?', 'Você pode me ajudar?']], [['I like it.', 'Eu gosto.'], ['I love them.', 'Eu adoro.']], [['Look at her!', 'Olhe para ela!']]],
                     ['Pediu ajuda! 🙋', 'Roupa certa! 👔', 'Pessoa certa! 👀'],
                     ['Sure! I help you. Look at this one!', 'Claro! Eu ajudo você. Olhe este aqui!']),
                  MS('✨', 'Elogio de moda', 'Use as expressões do episódio.',
                     'Seu amigo experimenta uma roupa. **Diga que fica bem nele com It looks good on you, mostre que gostou com That\'s so me e agradeça com Thanks a lot.**',
                     'Escreva a sua resposta aqui…', ['It looks good on you'],
                     "It looks good on you! That's so me! Thanks a lot!",
                     ['Elogiei com It looks good on you?', 'Usei That’s so me?', 'Agradeci com Thanks a lot?'],
                     [r'\bit looks good on you\b', r"\bthat['’]?s so me\b", r'\bthanks a lot\b'],
                     [[['It looks good on you.', 'Fica bem em você.']], [["That's so me!", 'Isso é a minha cara!']], [['Thanks a lot!', 'Muito obrigado!']]],
                     ['Elogio! ✨', 'Estilo! 😎', 'Obrigado! 🙏'],
                     ['Thanks! You are so nice!', 'Obrigado! Você é muito gentil!'])])
    CX = [CXI('The night sky is very dark. A cat in the dark is ___.', 'O céu da noite é muito escuro. Um gato no escuro é preto.', 'black', 'white', 'pink'),
          CXI('Snow and milk have the same color: ___.', 'A neve e o leite têm a mesma cor: branco.', 'white', 'black', 'brown'),
          CXI('A flamingo and a baby doll are often ___.', 'Um flamingo e uma boneca de bebê muitas vezes são rosa.', 'pink', 'brown', 'white'),
          CXI('Grapes are green or ___.', 'Uvas são verdes ou roxas.', 'purple', 'shirt', 'black'),
          CXI('Chocolate and tree trunks are ___.', 'O chocolate e os troncos de árvore são marrons.', 'brown', 'pink', 'white'),
          CXI('I wear a ___ and pants to work.', 'Eu uso uma camisa e calça para trabalhar.', 'shirt', 'purple', 'brown')]
    return dict(B=B, X=X, XT=XT, VB=VB, MR=MR, CX=CX)


EPS.append(ep41())


# ============================================================ 42 · a black sheep (adjetivo antes do nome) · Baa, Baa, Black Sheep
def ep42():
    sheep = 'e:🐑'
    farmer = 'p:short:5a3a22:f4c7a1:2e7d32:hat:shirt'
    boy = 'p:short:7a4a24:f4c7a1:2980b9:none:shirt'
    B = dict(
        title='Cor antes do nome · a black sheep',
        sub='Em inglês a cor vem antes: a black sheep, the white one',
        pattern_label='a black sheep',
        why='Hoje você aprende que, em inglês, a cor vem antes do nome (a black sheep) e que one evita repetir a palavra (the white one).',
        vocab=[['Sheep', 'Ovelha', 'Soa como “SHÍIP”.'], ['Wool', 'Lã', 'Soa como “UÚL”.'], ['Bag', 'Sacola, bolsa', 'Soa como “BÉG”.'],
               ['Coat', 'Casaco', 'Soa como “KÔUT”.'], ['Black', 'Preto', 'Soa como “BLÉK”.'], ['White', 'Branco', 'Soa como “UÁIT”.']],
        balloons=[['🐑', 'sheep'], ['🧶', 'wool'], ['🛍️', 'bag'], ['🧥', 'coat'], ['⚫', 'black'], ['⚪', 'white']],
        cover_art=dict(s='farm', items=[['🐑', 104, 56, 20, 'bob'], ['🧶', 138, 44, 12, 'bob'], ['🧥', 84, 34, 12, 'bob']], seed='bb1'),
        cover_sub='a black sheep. Em 10 minutos você coloca a cor no lugar certo, como na cantiga da ovelha negra',
        cover_say='Numa fazenda, um menino quer lã para fazer um casaco. Tem ovelha preta, ovelha branca, sacola marrom. Mas em que ordem se diz isso em inglês?',
        wrap_recap=[['a black sheep', 'uma ovelha preta'], ['a white coat', 'um casaco branco'], ['the white one', 'o branco'], ['two brown bags', 'duas sacolas marrons']],
        teaser=dict(t='The Starry Night', d='Próximo padrão: What color is it? (claro e escuro)'),
        cast={'Boy': ['👦', '#2980b9'], 'Farmer': ['👨‍🌾', '#2e7d32'], 'Sheep': ['🐑', '#555555']},
        lines=[['Boy', 'Look, Farmer! A black sheep and a white sheep!', 'Olhe, fazendeiro! Uma ovelha preta e uma ovelha branca!'],
               ['Farmer', 'Yes! The black sheep has black wool.', 'Sim! A ovelha preta tem lã preta.'],
               ['Boy', 'Can I have some wool? I need it for a coat.', 'Posso ter um pouco de lã? Preciso dela para um casaco.'],
               ['Sheep', 'Baa! Yes, you can. Take the white one.', 'Bé! Sim, pode. Pegue a branca.'],
               ['Boy', 'Thank you! I love a white coat.', 'Obrigado! Eu adoro um casaco branco.'],
               ['Farmer', 'Here is a big brown bag. Put the wool in it.', 'Aqui está uma sacola marrom grande. Ponha a lã nela.'],
               ['Boy', 'One bag, two bags, three bags full!', 'Uma sacola, duas sacolas, três sacolas cheias!'],
               ['Sheep', 'Baa! Now you have a white coat.', 'Bé! Agora você tem um casaco branco.']],
        quiz=[Q('What does the boy need wool for?', 'Para que o menino precisa da lã?', [['🧥', 'A coat'], ['🛍️', 'A bag'], ['🐑', 'A sheep']], 0, 2, 'O menino diz: “I need it for a coat.”'),
              Q('What color is the bag?', 'De que cor é a sacola?', [['⚫', 'Black'], ['⚪', 'White'], ['🟤', 'Brown']], 2, 5, 'O fazendeiro diz: “a big brown bag”.'),
              Q('Which wool does the boy take?', 'Qual lã o menino pega?', [['⚫', 'The black one'], ['⚪', 'The white one'], ['🟤', 'The brown one']], 1, 3, 'A ovelha diz: “Take the white one.”')],
        rdg_q=dict(q='Qual é a ordem certa em inglês para “uma ovelha preta”?', o=['a sheep black', 'a black sheep', 'black a sheep'], a=1,
                   why='A cor vem **antes** do nome: a **black** sheep.'),
        dictate=[['a black sheep', 'uma ovelha preta'], ['I love a white coat.', 'Eu adoro um casaco branco.'], ['Take the white one.', 'Pegue o branco.'], ['A big brown bag.', 'Uma sacola marrom grande.']],
        produce=PRD('Você está numa loja de roupas. **Descreva duas coisas com a cor antes do nome (a black coat) e escolha uma com the … one.**',
                    'Ex.: I have a black sheep and a white coat. I like the white one.', ['a black…', 'a white…', 'the white one'],
                    'I have a black sheep and a white coat. I like the white one.',
                    ['Coloquei a cor antes do nome?', 'Descrevi duas coisas?', 'Escolhi com the … one?'],
                    [r'\b(?:a|an|the) (?:black|white|brown|pink|purple|red|blue|green|yellow|orange)\s+\w+',
                     r'(?:\b(?:a|an) (?:black|white|brown|pink|purple|red|blue|green|yellow|orange)\s+\w+[\s\S]*){2}',
                     r'\bthe (?:black|white|brown|pink|purple|red|blue|green|yellow|orange) one\b'],
                    [[['a black coat', 'um casaco preto']], [['a white bag', 'uma bolsa branca'], ['a brown shirt', 'uma camisa marrom']], [['the white one', 'o branco'], ['the black one', 'o preto']]],
                    ['Cor no lugar certo! 🎨', 'Duas coisas! ✌️', 'One ajudou! ☝️'],
                    ['Nice! The white one is very good.', 'Legal! O branco é muito bom.']),
        rs=rs15(['museum', 'library', 'bank', 'farm', 'pharmacy', 'bookshop', 'playground', 'postoffice', 'stadium', 'harbor',
                 'garden', 'farm', 'busstop', 'hotelroom', 'snow']),
        sc='farm')
    X = dict(
        n=7070015, review=True, names=('Boy', 'Farmer'),
        stage=dict(rs='farm', chars=[[boy, 28, 0, 1.0], [farmer, 56, 1, 1.0], [sheep, 84, 1, 0.9]]),
        obra=dict(name='Baa, Baa, Black Sheep', kind='🎶 Cantiga infantil · 1744', year='1744',
                  text='Cantiga infantil inglesa, publicada pela primeira vez em 1744. Uma ovelha preta responde que tem lã: uma sacola para o patrão, uma para a patroa e uma para o menino que mora na estrada. Quase toda criança de língua inglesa conhece a cantiga.',
                  line=['Baa, baa, black sheep.', 'Bé, bé, ovelha negra.'],
                  pa=dict(t='barn', e=['🐑', '🧶', '🛍️'], p='b', v=0)),
        gancho=['Boy', 'Look, Farmer! A black sheep and a white sheep!', 'Olhe, fazendeiro! Uma ovelha preta e uma ovelha branca!'],
        hot=[H('🐑', 14, 16, 'sheep', 'ovelha', 'A black sheep and a white sheep.', 'Uma ovelha preta e uma ovelha branca.'),
             H('🧶', 40, 14, 'wool', 'lã', 'I like the white wool.', 'Eu gosto da lã branca.'),
             H('🛍️', 66, 14, 'bag', 'sacola', 'A big brown bag.', 'Uma sacola marrom grande.'),
             H('🧥', 88, 16, 'coat', 'casaco', 'I love the white one.', 'Eu adoro o branco.'),
             H('🌾', 12, 82, 'hay', 'feno', 'The hay is yellow.', 'O feno é amarelo.')],
        gap=[G('I have a ___ bag.', 'Eu tenho uma sacola marrom.', ['browns', 'brown', 'bag'], 1, 'A cor vem antes do nome e não leva -s: a **brown** bag.'),
             G('I like the white coat. I love the white ___.', 'Eu gosto do casaco branco. Eu adoro o branco.', ['ones', 'one', 'a'], 1, 'Para não repetir **coat**, use **one**: the white **one**.'),
             G('Two ___ bags.', 'Duas sacolas marrons.', ['brown', 'browns', 'bags brown'], 0, 'A cor não muda no plural: two **brown** bags.'),
             G("It's a ___ sheep.", 'É uma ovelha preta.', ['sheep black', 'blacks', 'black'], 2, 'Antes do nome: a **black** sheep.')],
        trap=[TR(['a sheep black', 'a black sheep', 'black a sheep'], 1, 'A cor vem antes do nome: a **black** sheep.'),
              TR(['two browns bags', 'two bags brown', 'two brown bags'], 2, 'Cor antes do nome e sem -s: two **brown** bags.')],
        sticker=dict(title='O menino e a ovelha', sub='Baa, Baa, Black Sheep · 1744', rs='garden', chars=[[boy, 34, 0, 1.0], [sheep, 68, 1, 0.95]]),
        speakers={'Boy': boy, 'Farmer': farmer, 'Sheep': sheep},
        rule=dict(who=farmer, head='a black sheep', sub='A cor vem antes do nome.',
                  say=['The black sheep has black wool.', 'A ovelha preta tem lã preta.'],
                  formula=[
                      dict(from_=[['uma', 1], ['ovelha', 3], ['preta', 2]], to=[['a', 1], ['black', 2], ['sheep', 3]], say='a black sheep', note='Em português a cor vem depois. Em inglês ela vem **antes** do nome.'),
                      dict(from_=[['o', 1], ['casaco', 3], ['branco', 2]], to=[['the', 1], ['white', 2], ['coat', 3]], say='the white coat', note='A cor fica **entre** o artigo e o nome.'),
                      dict(from_=[['the white', 2], ['coat', 3]], to=[['the white', 2], ['one', 3]], say='the white one', note='Para não repetir o nome, troque-o por **one**.')],
                  uses=[dict(ico='🐑', tag='Descrever', en='a black sheep', pt='uma ovelha preta'),
                        dict(ico='☝️', tag='Escolher', en='the white one', pt='o branco'),
                        dict(ico='🛍️', tag='Contar', en='two brown bags', pt='duas sacolas marrons')],
                  rules=[dict(tag='Cor + nome', c=0, text='A cor (e outras palavras que descrevem) vêm **antes** do nome.', ex='✗ a sheep black  →  ✓ a black sheep'),
                         dict(tag='one', c=2, text='**one** substitui um nome já dito.', ex='the white coat → the white one'),
                         dict(tag='Sem -s', c=1, text='A cor **não muda** no plural.', ex='two brown bags (✗ two browns bags)')],
                  tips=['Em português dizemos “sacola marrom”. Em inglês a ordem se inverte: **brown bag**. Se errar, pense: cor primeiro!']),
        mission_ic='🐑')
    XT = dict(
        exp=[E('🐑', 'the black sheep', 'Expressão', 'a ovelha negra', 'Pessoa **diferente** do resto da família ou do grupo (igual ao português).', ['He is the black sheep of the family.', 'Ele é a ovelha negra da família.']),
             E('🧥', 'What a nice coat!', 'Expressão', 'Que casaco bonito!', 'Elogio **animado** ao que alguém tem ou veste.', ['What a nice white coat!', 'Que casaco branco bonito!']),
             E('☝️', 'This one, please.', 'Expressão', 'Este aqui, por favor.', 'Para **escolher** entre duas ou mais coisas.', ['This one, please. I like the black one.', 'Este aqui, por favor. Eu gosto do preto.']),
             E('🙋', 'Me too!', 'Informal', 'Eu também!', 'Quando você **sente ou gosta da mesma coisa**.', ['I like wool. Me too!', 'Eu gosto de lã. Eu também!'])],
        exp_scene=dict(rs='garden', lines=[
            ['Farmer', 'Hello! This is **the black sheep** of the farm.', 'Olá! Esta é a ovelha negra da fazenda.'],
            ['Boy', '**What a nice coat!**', 'Que casaco bonito!'],
            ['Farmer', 'Thank you. Take a white one or a black one.', 'Obrigado. Pegue uma branca ou uma preta.'],
            ['Boy', '**This one, please.** I like the white one.', 'Esta aqui, por favor. Eu gosto da branca.'],
            ['Sheep', 'Baa! I like white wool.', 'Bé! Eu gosto de lã branca.'],
            ['Boy', '**Me too!**', 'Eu também!']]),
        lab=dict(short='w × v', title='Laboratório de sons: o “w” de wool e white',
                 say='O “w” inglês é bem diferente do “v”. Vamos treinar com a ovelha e a lã!',
                 intro=dict(what='O **w** de **wool**, **white** e **we** é um som de “u” rápido, feito só com os lábios.',
                            how='Arredonde os lábios como se fosse dizer “u”, e abra rápido para a vogal. Os dentes NÃO tocam o lábio.',
                            pt='O **v** de **vest** e **vine** é diferente: os dentes de cima tocam o lábio de baixo. Brasileiros costumam trocar: **west** vira “vest”.'),
                 ex=[['wool', 'UÚL', 'lã', 'lábios redondos, depois abre'], ['white', 'UÁIT', 'branco', 'comece com “u” rápido'], ['we', 'UÍ', 'nós', 'sem dente no lábio']],
                 pairs=[['west', 'vest', 'w: lábios redondos · v: dentes no lábio'], ['wine', 'vine', '“vinho” × “videira”'], ['wet', 'vet', '“molhado” × “veterinário”']],
                 tip='Sinta o lábio de baixo. No **v** ele faz cócegas nos dentes. No **w** ele fica livre, com os lábios redondos.',
                 phrase=['We have white wool.', 'Nós temos lã branca.'],
                 rounds=[RD('vest', ['west', 'vest'], 1, '**Vest** (colete) começa com dentes no lábio. **West** (oeste) começa com “u”.'),
                         RD('wine', ['wine', 'vine'], 0, '**Wine** (vinho) começa com lábios redondos. **Vine** (videira) começa com o “v”.'),
                         RD('vet', ['wet', 'vet'], 1, '**Vet** (veterinário) começa com o “v”. **Wet** (molhado) com o “w”.')]),
        hunt=[HU('west', ['west', 'vest'], 0, '**west** (oeste) começa com lábios redondos.'),
              HU('vine', ['wine', 'vine'], 1, '**vine** (videira) começa com o “v”.'),
              HU('wine', [['🍷', ''], ['🌿', ''], ['🐕', '']], 0, '**wine** = vinho, começa com o “w”.', True),
              HU('wet', ['wet', 'vet'], 0, '**wet** (molhado) começa com o “w”.'),
              HU('vet', ['wet', 'vet'], 1, '**vet** (veterinário) começa com o “v”.')])
    VB = dict(title='Verbos para a loja de lã', tip='Quatro verbos: wear, take, put e give.',
              items=[VBI('wear', '🧥', 'vestir, usar', 'I wear a white coat.', 'The boy wear**s** a brown coat.', ['I wear a white coat.', 'Eu uso um casaco branco.'], '**wear** = vestir, usar. Com he/she: **wears**.'),
                     VBI('take', '🤲', 'pegar, levar', 'I take the white one.', 'She take**s** the black bag.', ['I take the white one.', 'Eu pego o branco.'], '**take** = pegar, levar. Com he/she: **takes**.'),
                     VBI('put', '📥', 'pôr, colocar', 'I put the wool in the bag.', 'He put**s** the wool in the bag.', ['I put the wool in the bag.', 'Eu ponho a lã na sacola.'], '**put** = pôr, colocar. Com he/she: **puts**.'),
                     VBI('give', '🎁', 'dar', 'I give him some wool.', 'The sheep give**s** him some wool.', ['I give him some wool.', 'Eu dou um pouco de lã a ele.'], '**give** = dar. Com he/she: **gives**.')])
    MR = dict(
        mold=[MP('Cor antes do nome', [SL('artigo', [['a', 'um(a)']]),
                                       SL('cor', [['black', 'preto'], ['white', 'branco'], ['brown', 'marrom'], ['pink', 'rosa'], ['purple', 'roxo']]),
                                       SL('coisa', [['sheep', 'ovelha'], ['coat', 'casaco'], ['bag', 'sacola'], ['shirt', 'camisa']])], ['.', '.']),
              MP('Escolher com one', [SL('começo', [['I like the', 'eu gosto do(a)']]),
                                      SL('cor', [['black', 'preto'], ['white', 'branco'], ['brown', 'marrom'], ['pink', 'rosa']]),
                                      SL('palavra', [['one', 'aquele']])], ['.', '.']),
              MP('Mais de um', [SL('começo', [['I need', 'eu preciso de']]), SL('número', [['two', 'dois'], ['three', 'três']]),
                                SL('cor', [['brown', 'marrons'], ['white', 'brancos'], ['black', 'pretos']]),
                                SL('coisa', [['bags', 'sacolas'], ['coats', 'casacos'], ['shirts', 'camisas']])], ['.', '.'])],
        speak=[['I have a black sheep and a white coat.', 'Eu tenho uma ovelha preta e um casaco branco.'], ['This one, please. Me too!', 'Este aqui, por favor. Eu também!']],
        trap=[MT('“the black sheep of the family” quer dizer…', ['Uma ovelha de verdade', 'Um tipo de lã', 'A pessoa diferente do grupo'], 2, '**the black sheep** = a ovelha negra (como em português).', 'The black sheep of the family.'),
              MT('Qual frase está certa?', ['a coat white', 'a white coat', 'a coat whites'], 1, 'A cor vem antes do nome: a **white** coat.', 'A white coat.')],
        gap=[MG('What a ___ coat!', 'Que casaco bonito!', ['nice', 'nicely', 'niced'], 0, 'Antes do nome, use o adjetivo: **nice** coat.', 'What a nice coat!'),
             MG('This ___, please.', 'Este aqui, por favor.', ['ones', 'one', 'is'], 1, 'A expressão é **This one, please.**', 'This one, please.')],
        expq=[MT('Seu amigo diz que gosta de lã e você também.', ['Me too!', 'This one, please.', 'What a nice coat!'], 0, '**Me too!** = eu também.'),
              MT('Você vê um casaco lindo na vitrine.', ['Me too!', 'What a nice coat!', 'This one, please.'], 1, '**What a nice coat!** elogia o casaco.'),
              MT('A vendedora mostra dois casacos. Você escolhe um.', ['This one, please.', 'Me too!', 'What a nice coat!'], 0, '**This one, please.** escolhe.')],
        missions=[MS('🧥', 'Na loja de lã', 'Cor antes do nome e one.',
                     'Você está numa loja de roupas. **Descreva duas coisas com a cor antes do nome (a black coat) e escolha uma com the … one.**',
                     'Escreva a sua resposta aqui…', ['a black…'],
                     'I have a black sheep and a white coat. I like the white one.',
                     ['Coloquei a cor antes do nome?', 'Descrevi duas coisas?', 'Escolhi com the … one?'],
                     [r'\b(?:a|an|the) (?:black|white|brown|pink|purple|red|blue|green|yellow|orange)\s+\w+',
                      r'(?:\b(?:a|an) (?:black|white|brown|pink|purple|red|blue|green|yellow|orange)\s+\w+[\s\S]*){2}',
                      r'\bthe (?:black|white|brown|pink|purple|red|blue|green|yellow|orange) one\b'],
                     [[['a black coat', 'um casaco preto']], [['a white bag', 'uma bolsa branca']], [['the white one', 'o branco']]],
                     ['Cor no lugar certo! 🎨', 'Duas coisas! ✌️', 'One ajudou! ☝️'],
                     ['Nice choice!', 'Boa escolha!']),
                  MS('🐑', 'Na fazenda', 'Use as expressões do episódio.',
                     'Você está na fazenda. **Elogie algo com What a nice…, escolha com This one, please e concorde com Me too.**',
                     'Escreva a sua resposta aqui…', ['What a nice…'],
                     'What a nice coat! This one, please. Me too!',
                     ['Elogiei com What a nice…?', 'Escolhi com This one, please?', 'Concordei com Me too?'],
                     [r'\bwhat an? nice\b', r'\bthis one, please\b', r'\bme too\b'],
                     [[['What a nice coat!', 'Que casaco bonito!']], [['This one, please.', 'Este aqui, por favor.']], [['Me too!', 'Eu também!']]],
                     ['Elogio! 🧥', 'Escolha! ☝️', 'Concordou! 🙋'],
                     ['Great! Welcome to the farm!', 'Ótimo! Bem-vindo à fazenda!'])])
    CX = [CXI('It is a white animal with soft wool. It says “baa”. It is a ___.', 'É um animal branco com lã macia. Faz “bé”. É uma ovelha.', 'sheep', 'coat', 'bag'),
          CXI('We make warm clothes from the soft ___ of a sheep.', 'Fazemos roupas quentes com a lã macia da ovelha.', 'wool', 'bag', 'black'),
          CXI('I put my books and my lunch in a ___.', 'Eu ponho os meus livros e o meu almoço numa sacola.', 'bag', 'wool', 'sheep'),
          CXI('It is cold outside! I wear a warm ___.', 'Está frio lá fora! Eu uso um casaco quente.', 'coat', 'sheep', 'bag'),
          CXI('The night is dark and the cat is ___.', 'A noite é escura e o gato é preto.', 'black', 'white', 'wool'),
          CXI('Snow is cold and ___.', 'A neve é fria e branca.', 'white', 'black', 'coat')]
    return dict(B=B, X=X, XT=XT, VB=VB, MR=MR, CX=CX)


EPS.append(ep42())


# ============================================================ 43 · What color is it? · The Starry Night
def ep43():
    vincent = 'p:short:c0562b:f4c7a1:2e86c1:beard:shirt'
    emma = 'p:long:3b2a1a:f4c7a1:8e44ad:none:dress'
    theo = 'p:short:7a4a24:f4c7a1:34495e:none:suit'
    B = dict(
        title='Claro e escuro · What color is it?',
        sub='Perguntar a cor com What color is it? e responder com light / dark',
        pattern_label='What color is it?',
        why='Hoje você aprende a perguntar a cor com What color is it? e a responder com cores claras e escuras: dark blue, light yellow.',
        vocab=[['Gray', 'Cinza', 'Soa como “GRÊI”.'], ['Gold', 'Dourado', 'Soa como “GÔULD”.'], ['Silver', 'Prateado', 'Soa como “SÍL-ver”.'],
               ['Light', 'Claro', 'Soa como “LÁIT”.'], ['Dark', 'Escuro', 'Soa como “DÁRK”.'], ['Star', 'Estrela', 'Soa como “STÁR”.']],
        balloons=[['☁️', 'gray'], ['🥇', 'gold'], ['🥈', 'silver'], ['💡', 'light'], ['🌑', 'dark'], ['⭐', 'star']],
        cover_art=dict(s='nightcity', items=[['⭐', 104, 56, 20, 'bob'], ['🌙', 138, 44, 12, 'bob'], ['🎨', 84, 34, 12, 'bob']], seed='sn1'),
        cover_sub='What color is it? Em 10 minutos você descreve o céu da noite como um pintor',
        cover_say='É noite, e o céu está cheio de estrelas. Um pintor e seus amigos olham para cima. De que cor é o céu? E a lua? E as estrelas?',
        wrap_recap=[['What color is the sky?', 'Qual é a cor do céu?'], ["It's dark blue.", 'É azul-escuro.'], ['The star is gold.', 'A estrela é dourada.'], ["It's light yellow.", 'É amarelo-claro.']],
        teaser=dict(t='The Little Prince', d="Próximo padrão: I want / I'd like para pedir o que você quer"),
        cast={'Vincent': ['🎨', '#2e86c1'], 'Emma': ['👩', '#8e44ad'], 'Theo': ['👨', '#34495e']},
        lines=[['Emma', 'Vincent, what color is the sky?', 'Vincent, qual é a cor do céu?'],
               ['Vincent', "It's dark blue. The moon is light yellow.", 'É azul-escuro. A lua é amarelo-claro.'],
               ['Theo', 'And what color is the big star?', 'E qual é a cor da estrela grande?'],
               ['Vincent', "It's gold. Look at it!", 'É dourada. Olhe para ela!'],
               ['Emma', 'What color is the village? Is it gray?', 'Qual é a cor da vila? É cinza?'],
               ['Vincent', "Yes, it is. It's dark gray.", 'Sim, é. É cinza-escuro.'],
               ['Theo', 'And what color is your brush?', 'E qual é a cor do seu pincel?'],
               ['Vincent', "It's silver. I love it!", 'É prateado. Eu adoro!']],
        quiz=[Q('What color is the sky?', 'Qual é a cor do céu?', [['☁️', 'Light gray'], ['🌌', 'Dark blue'], ['⭐', 'Gold']], 1, 1, 'Vincent diz: “It’s dark blue.”'),
              Q('What color is the big star?', 'Qual é a cor da estrela grande?', [['🥇', 'Gold'], ['🥈', 'Silver'], ['⚫', 'Black']], 0, 3, 'Vincent diz: “It’s gold.”'),
              Q('What color is the brush?', 'Qual é a cor do pincel?', [['🥇', 'Gold'], ['☁️', 'Gray'], ['🥈', 'Silver']], 2, 7, 'Vincent diz: “It’s silver.”')],
        rdg_q=dict(q='Como se diz “azul-escuro” em inglês?', o=['blue dark', 'dark blue', 'dark of blue'], a=1,
                   why='**dark** vem antes da cor: **dark** blue.'),
        dictate=[['What color is the sky?', 'Qual é a cor do céu?'], ["It's dark blue.", 'É azul-escuro.'], ['The star is gold.', 'A estrela é dourada.'], ["It's light yellow.", 'É amarelo-claro.']],
        produce=PRD('Um amigo olha o céu da noite. **Pergunte a cor de algo com What color is…? e responda usando dark ou light mais uma cor.**',
                    "Ex.: What color is the sky? It's dark blue. The star is gold.", ['What color is…?', "It's dark…", "It's light…"],
                    "What color is the sky? It's dark blue. The star is gold.",
                    ['Perguntei com What color is…?', 'Usei dark ou light com uma cor?', 'Falei de gold, silver ou gray?'],
                    [r'\bwhat color is\b[^.!?]*\?', r'\b(?:dark|light) (?:blue|gray|yellow|green|gold|silver|red|orange|pink|purple|brown)\b', r'\b(?:gold|silver|gray)\b'],
                    [[['What color is the sky?', 'Qual é a cor do céu?']], [["It's dark blue.", 'É azul-escuro.'], ["It's light yellow.", 'É amarelo-claro.']], [['The star is gold.', 'A estrela é dourada.']]],
                    ['Boa pergunta! ❓', 'Claro ou escuro! 🌗', 'Cor dourada! ⭐'],
                    ["Yes! It's a beautiful night.", 'Sim! É uma noite linda.']),
        rs=rs15(['castlehall', 'zoo', 'mountain', 'pool', 'bakery', 'museum', 'supermarket', 'nightcity', 'stadium', 'busstop',
                 'fishing', 'nightcity', 'bookshop', 'harbor', 'christmas']),
        sc='nightcity')
    X = dict(
        n=30008, review=True, names=('Vincent', 'Emma'),
        stage=dict(rs='nightcity', chars=[[vincent, 28, 0, 1.0], [emma, 56, 1, 1.0], [theo, 84, 1, 0.95]]),
        obra=dict(name='The Starry Night', kind='🖼️ Pintura · 1889', year='1889',
                  text='Quadro do pintor holandês Vincent van Gogh, de 1889. Mostra um céu azul-escuro cheio de estrelas e de espirais de luz sobre uma vila tranquila. Hoje a pintura está no museu MoMA, em Nova York.',
                  line=["It's dark blue.", 'É azul-escuro. (frase do tema)'],
                  pa=dict(t='observatory', e=['🌌', '⭐', '🌙'], p='g', v=1)),
        gancho=['Emma', 'Vincent, what color is the sky?', 'Vincent, qual é a cor do céu?'],
        hot=[H('🌙', 14, 16, 'moon', 'lua', 'The moon is light yellow.', 'A lua é amarelo-claro.'),
             H('⭐', 40, 14, 'star', 'estrela', 'What color is the star? It is gold.', 'Qual é a cor da estrela? É dourada.'),
             H('🏠', 66, 14, 'house', 'casa', 'The house is dark gray.', 'A casa é cinza-escuro.'),
             H('🌳', 88, 16, 'tree', 'árvore', 'The tree is dark green.', 'A árvore é verde-escuro.'),
             H('💡', 12, 82, 'lamp', 'lâmpada', 'The lamp is light yellow.', 'A lâmpada é amarelo-claro.')],
        gap=[G('___ color is the sky?', 'Qual é a cor do céu?', ['What', 'Who', 'Where'], 0, 'Para perguntar a cor, use **What color is…?**'),
             G("It's ___ blue.", 'É azul-escuro.', ['light', 'dark', 'gray'], 1, '**dark** = escuro. Ele vem antes da cor: **dark** blue.'),
             G('The star is ___.', 'A estrela é dourada.', ['golds', 'gold', 'goldly'], 1, 'Cor é uma palavra só, sem -s: **gold**.'),
             G('What color is it? ___ silver.', 'Qual é a cor? É prateado.', ['Its', 'Is', "It's"], 2, 'A resposta começa com **It’s** (it is).')],
        trap=[TR(['blue dark', 'dark blue', 'dark of blue'], 1, 'O **dark** vem antes: **dark** blue.'),
              TR(['What color it is?', 'What is color it?', 'What color is it?'], 2, 'A ordem é **What color is it?**')],
        sticker=dict(title='Vincent e os amigos', sub='The Starry Night · 1889', rs='nightcity', chars=[[vincent, 34, 0, 1.0], [emma, 68, 1, 1.0]]),
        speakers={'Vincent': vincent, 'Emma': emma, 'Theo': theo},
        rule=dict(who=vincent, head='What color is it?', sub='Perguntar e dizer a cor, com claro e escuro.',
                  say=['Vincent, what color is the sky?', 'Vincent, qual é a cor do céu?'],
                  formula=[
                      dict(from_=[['What', 0], ['color', 3], ['is it?', 1]], to=[["It's", 1], ['blue.', 3]], say="It's blue.", note='Pergunta: **What color is it?** Resposta: **It’s** + cor.'),
                      dict(from_=[["It's", 1], ['blue.', 3]], to=[["It's", 1], ['dark', 2], ['blue.', 3]], say="It's dark blue.", note='**dark** (escuro) vem antes da cor.'),
                      dict(from_=[["It's", 1], ['yellow.', 3]], to=[["It's", 1], ['light', 2], ['yellow.', 3]], say="It's light yellow.", note='**light** (claro) também vem antes da cor.')],
                  uses=[dict(ico='❓', tag='Perguntar', en='What color is the sky?', pt='Qual é a cor do céu?'),
                        dict(ico='🌌', tag='Responder', en="It's dark blue.", pt='É azul-escuro.'),
                        dict(ico='🌕', tag='Responder', en="It's light yellow.", pt='É amarelo-claro.')],
                  rules=[dict(tag='What color', c=0, text='**What color is…?** = qual é a cor de…?', ex='What color is the star?'),
                         dict(tag='light / dark', c=2, text='**light** e **dark** vêm **antes** da cor.', ex='dark blue · light yellow'),
                         dict(tag='Ordem', c=1, text='Não inverta como em português.', ex='✗ blue dark  →  ✓ dark blue')],
                  tips=['Em português dizemos “azul-escuro” (cor primeiro). Em inglês é **dark blue** (claro/escuro primeiro).']),
        mission_ic='🌌')
    XT = dict(
        exp=[E('🤩', "It's beautiful!", 'Expressão', 'Que lindo!', 'Para elogiar **algo bonito** que você vê.', ["Look at the sky. It's beautiful!", 'Olhe o céu. Que lindo!']),
             E('🌟', 'What a night!', 'Expressão', 'Que noite!', 'Quando a noite foi **especial**.', ['What a night! Look at the stars!', 'Que noite! Olhe as estrelas!']),
             E('👌', 'Not bad!', 'Informal', 'Nada mau!', 'Elogio **modesto**: está bem bom.', ['A gray village? Not bad!', 'Uma vila cinza? Nada mau!']),
             E('💙', 'My favorite color is…', 'Expressão', 'Minha cor favorita é…', 'Para dizer a cor que você **mais gosta**.', ['My favorite color is dark blue.', 'Minha cor favorita é azul-escuro.'])],
        exp_scene=dict(rs='harbor', lines=[
            ['Emma', '**What a night!** Look at the sky.', 'Que noite! Olhe o céu.'],
            ['Theo', "**It's beautiful!** What color is it?", 'Que lindo! Qual é a cor?'],
            ['Vincent', "It's dark blue. **My favorite color is** dark blue.", 'É azul-escuro. Minha cor favorita é azul-escuro.'],
            ['Emma', 'And the village? It is gray.', 'E a vila? É cinza.'],
            ['Vincent', 'Yes, it is.', 'Sim, é.'],
            ['Theo', 'A gold star and a gray village? **Not bad!**', 'Uma estrela dourada e uma vila cinza? Nada mau!']]),
        lab=dict(short='g × k', title='Laboratório de sons: o “g” de gold e gray',
                 say='O “g” e o “k” são parecidos, mas trocam o sentido das palavras. Vamos treinar com as cores!',
                 intro=dict(what='O **g** de **gold**, **gray** e **go** é um som feito no fundo da boca, com a voz ligada.',
                            how='A parte de trás da língua toca o céu da boca e solta com a voz ligada (ponha a mão na garganta: ela vibra). No **k** de **cold** a garganta não vibra.',
                            pt='Em português o “g” de “gato” é igual. O problema é ouvir a diferença entre **gold** (dourado) e **cold** (frio), ou **glass** e **class**.'),
                 ex=[['gold', 'GÔULD', 'dourado', 'garganta vibrando'], ['gray', 'GRÊI', 'cinza', 'g com voz, depois r suave'], ['go', 'GÔU', 'ir', 'g sonoro, curto']],
                 pairs=[['gold', 'cold', 'g: garganta vibra · c/k: sem vibrar'], ['gap', 'cap', '“lacuna” × “boné”'], ['glass', 'class', '“copo” × “aula”']],
                 tip='Ponha dois dedos na garganta. Diga **gold**: vibra. Diga **cold**: quase nada.',
                 phrase=['The gold star is good.', 'A estrela dourada é boa.'],
                 rounds=[RD('gold', ['gold', 'cold'], 0, '**Gold** (dourado) tem o “g” com voz. **Cold** (frio) começa sem vibrar.'),
                         RD('cap', ['gap', 'cap'], 1, '**Cap** (boné) começa sem vibrar. **Gap** (lacuna) tem “g”.'),
                         RD('glass', ['class', 'glass'], 1, '**Glass** (copo) começa com “g” vibrando. **Class** (aula) começa com “k”.')]),
        hunt=[HU('cold', ['gold', 'cold'], 1, '**cold** (frio) começa com o “k”, sem vibrar.'),
              HU('gold', [['🥇', ''], ['🥶', ''], ['🥈', '']], 0, '**gold** = dourado, começa com “g”.', True),
              HU('class', ['class', 'glass'], 0, '**class** (aula) começa com “k”.'),
              HU('gap', ['gap', 'cap'], 0, '**gap** (lacuna) começa com o “g”.'),
              HU('cap', [['🧢', ''], ['🥇', ''], ['🥶', '']], 0, '**cap** = boné, começa com “k”.', True)])
    VB = dict(title='Verbos para olhar o céu', tip='Quatro verbos: look, paint, shine e draw.',
              items=[VBI('look', '👀', 'olhar', 'I look at the sky.', 'Emma look**s** at the stars.', ['I look at the sky.', 'Eu olho para o céu.'], '**look** = olhar. Com he/she: **looks**.'),
                     VBI('paint', '🎨', 'pintar', 'I paint a gold star.', 'Vincent paint**s** the night.', ['I paint a gold star.', 'Eu pinto uma estrela dourada.'], '**paint** = pintar. Com he/she: **paints**.'),
                     VBI('shine', '✨', 'brilhar', 'I shine like a star.', 'The moon shine**s** at night.', ['I shine like a star.', 'Eu brilho como uma estrela.'], '**shine** = brilhar. Com he/she: **shines**.'),
                     VBI('draw', '✏️', 'desenhar', 'I draw a village.', 'Theo draw**s** a gray house.', ['I draw a village.', 'Eu desenho uma vila.'], '**draw** = desenhar. Com he/she: **draws**.')])
    MR = dict(
        mold=[MP('Perguntar a cor', [SL('pergunta', [['What color is', 'qual é a cor de']]),
                                     SL('coisa', [['the sky', 'o céu'], ['the star', 'a estrela'], ['the moon', 'a lua'], ['the village', 'a vila'], ['the brush', 'o pincel']])], ['?', '?']),
              MP('Claro ou escuro', [SL('começo', [["It's", 'é']]), SL('tom', [['dark', 'escuro'], ['light', 'claro']]),
                                     SL('cor', [['blue', 'azul'], ['gray', 'cinza'], ['yellow', 'amarelo'], ['green', 'verde']])], ['.', '.']),
              MP('Cores metálicas', [SL('coisa', [['The star is', 'A estrela é'], ['The brush is', 'O pincel é'], ['The ring is', 'O anel é']]),
                                     SL('cor', [['gold', 'dourado'], ['silver', 'prateado'], ['gray', 'cinza']])], ['.', '.'])],
        speak=[["What color is the sky? It's dark blue.", 'Qual é a cor do céu? É azul-escuro.'], ['My favorite color is gold. Not bad!', 'Minha cor favorita é dourado. Nada mau!']],
        trap=[MT('“Not bad!” quer dizer…', ['Muito ruim!', 'Nada mau!', 'Não tem!'], 1, '**Not bad!** = nada mau (um elogio modesto).', 'Not bad!'),
              MT('Qual frase está certa?', ["It's blue dark.", "It's dark of blue.", "It's dark blue."], 2, '**dark** vem antes da cor.', "It's dark blue.")],
        gap=[MG('What color ___ the moon?', 'Qual é a cor da lua?', ['is', 'are', 'do'], 0, 'Com uma coisa só: **is**.', 'What color is the moon?'),
             MG('My ___ color is gold.', 'Minha cor favorita é dourado.', ['favorite', 'favorites', 'favor'], 0, 'A palavra é **favorite** (favorita).', 'My favorite color is gold.')],
        expq=[MT('Você olha o céu cheio de estrelas e quer elogiar.', ["It's beautiful!", 'Not bad!', 'My favorite color is…'], 0, "**It's beautiful!** elogia algo bonito."),
              MT('Alguém pergunta qual é a sua cor preferida.', ['What a night!', 'My favorite color is gold.', 'Not bad!'], 1, '**My favorite color is…** responde a pergunta.'),
              MT('A noite foi incrível e você quer comentar.', ['Not bad!', 'What a night!', "It's beautiful!"], 1, '**What a night!** = que noite!')],
        missions=[MS('🌌', 'Quadro da noite', 'Pergunte e descreva a cor.',
                     'Seu amigo pinta o céu da noite. **Pergunte a cor de algo com What color is…? e responda usando dark ou light e uma cor.**',
                     'Escreva a sua resposta aqui…', ['What color is…?'],
                     "What color is the sky? It's dark blue. The star is gold.",
                     ['Perguntei com What color is…?', 'Usei dark ou light com uma cor?', 'Falei de gold, silver ou gray?'],
                     [r'\bwhat color is\b[^.!?]*\?', r'\b(?:dark|light) (?:blue|gray|yellow|green|gold|silver|red|orange|pink|purple|brown)\b', r'\b(?:gold|silver|gray)\b'],
                     [[['What color is the sky?', 'Qual é a cor do céu?']], [["It's dark blue.", 'É azul-escuro.'], ["It's light yellow.", 'É amarelo-claro.']], [['The star is gold.', 'A estrela é dourada.']]],
                     ['Boa pergunta! ❓', 'Claro ou escuro! 🌗', 'Cor dourada! ⭐'],
                     ['Wow! It is a beautiful painting.', 'Uau! É uma pintura linda.']),
                  MS('🤩', 'Comentando a noite', 'Use as expressões do episódio.',
                     'Você olha o céu com um amigo. **Diga que é lindo com It\'s beautiful, comente a noite com What a night e diga a sua cor favorita com My favorite color is….**',
                     'Escreva a sua resposta aqui…', ["It's beautiful"],
                     "It's beautiful! What a night! My favorite color is dark blue.",
                     ['Disse que é lindo?', 'Comentei com What a night?', 'Falei a minha cor favorita?'],
                     [r"\bit['’]?s beautiful\b", r'\bwhat a night\b', r'\bmy favorite color is\b'],
                     [[["It's beautiful!", 'Que lindo!']], [['What a night!', 'Que noite!']], [['My favorite color is blue.', 'Minha cor favorita é azul.']]],
                     ['Lindo! 🤩', 'Que noite! 🌟', 'Cor favorita! 💙'],
                     ['Me too! Dark blue is great.', 'Eu também! Azul-escuro é ótimo.'])])
    CX = [CXI('The sky is full of clouds and it is going to rain. The clouds are ___.', 'O céu está cheio de nuvens e vai chover. As nuvens estão cinzentas.', 'gray', 'gold', 'light'),
          CXI('The winner gets the first place medal. It is ___.', 'O vencedor recebe a medalha do primeiro lugar. Ela é dourada.', 'gold', 'silver', 'dark'),
          CXI('The second place medal is ___.', 'A medalha do segundo lugar é prateada.', 'silver', 'gold', 'gray'),
          CXI('My shirt is not dark. It is ___ blue.', 'Minha camisa não é escura. É azul-claro.', 'light', 'dark', 'star'),
          CXI('At night, the room is ___. Turn on the lamp!', 'À noite, o quarto está escuro. Acenda a lâmpada!', 'dark', 'light', 'gold'),
          CXI('It shines in the sky at night. It is a ___.', 'Ela brilha no céu à noite. É uma estrela.', 'star', 'gray', 'silver')]
    return dict(B=B, X=X, XT=XT, VB=VB, MR=MR, CX=CX)


EPS.append(ep43())
