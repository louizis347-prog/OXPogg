# Lote 01: posições 6 a 13 do A1 (n = 7030001, 70002, 9802, 70003, 7070003, 30002, 70004, 9803).
# TROCAS DE OBRA: pos 6: de Dracula: The Castle para The Addams Family (tema família; combina com "Foto de família")
# TROCAS DE OBRA: pos 10: de Gulliver's Travels (repetida na pos 9) para Rip Van Winkle (Washington Irving, 1819)
# TROCAS DE OBRA: pos 11: de Little Italy (lugar) para It's a Small World (atração/canção da Feira Mundial de NY, 1964)
# TROCAS DE OBRA: pos 13: mantida Vila Sésamo, trabalhada em inglês como Sesame Street
# (pos 7, 8, 9 e 12 mantidas: Rock-a-Bye Baby, Coming to America, Gulliver's Travels, Don Quixote)


# ---------- helpers ----------
def L(who, en, pt):
    return [who, en, pt]


def VOC(*r):
    return [[a, b, "Soa como “%s”." % c] for a, b, c in r]


def BAL(*r):
    return [list(x) for x in r]


def QZ(q, pt, opts, a, line, why):
    return dict(q=q, pt=pt, opts=[list(o) for o in opts], a=a, line=line, why=why)


def HOT(e, x, y, en, pt, say, sayPt):
    return dict(e=e, x=x, y=y, en=en, pt=pt, say=say, sayPt=sayPt)


def GAP(q, pt, opts, a, why):
    return dict(q=q, pt=pt, opts=opts, a=a, why=why)


def TRAP(opts, a, why, q='Qual frase está certa?'):
    return dict(q=q, opts=opts, a=a, why=why)


RSK = 'review dquiz rdg pat vplay build order soundlab produce wrap dictate'.split()


def RS(*s):
    d = dict(zip(RSK, s))
    d['scene'] = s[0]
    d['balloons'] = s[3]
    return d


def PROD(prompt, ph, chips, model, check, kw, tips, ok, reply):
    return dict(prompt=prompt, ph=ph, chips=chips, model=model, check=check, kw=kw, tips=tips, ok=ok, reply=reply)


def MIS(ic, name, desc, **k):
    return dict(ic=ic, name=name, desc=desc, data=PROD(**k))


def EXP(ic, en, tag, pt, use, ex):
    return dict(ic=ic, en=en, tag=tag, pt=pt, use=use, ex=ex)


def RND(say, opts, a, why):
    return dict(fig='🎧', say=say, ask='Qual palavra você ouviu?', opts=opts, a=a, why=why)


def HW(say, opts, a, why):
    return dict(fig='🎧', say=say, ask='Ouça e toque na palavra.', opts=opts, a=a, why=why)


def HP(say, em, a, why):
    return dict(fig='🎧', say=say, ask='Ouça e toque na figura.', opts=[[e, ''] for e in em], a=a, why=why, pic=1)


def VERB(v, ic, pt, f1, f2, ex, expt, note):
    return dict(v=v, ic=ic, pt=pt, f=[['eu', f1], ['ele/ela', f2]], ex=[ex, expt], note=note)


def MOLD(label, slots, end=('.', '.')):
    return dict(label=label, slots=[dict(cat=c, opts=[list(o) for o in os]) for c, os in slots], end=list(end))


def TRM(ask, opts, a, why, say=None):
    d = dict(ask=ask, opts=opts, a=a, why=why)
    if say:
        d['say'] = say
    return d


def GPM(text, pt, opts, a, why, say):
    return dict(text=text, pt=pt, opts=opts, a=a, why=why, say=say)


def EQ(ask, opts, a, why):
    return dict(ask=ask, opts=opts, a=a, why=why)


def CXF(text, pt, opts):
    return dict(text=text, pt=pt, opts=opts, a=0)


def ep(B, X, XT, VB, MR, CX):
    return dict(B=B, X=X, XT=XT, VB=VB, MR=MR, CX=CX)


# ======================================================================
# POS 6 · n=7030001 · The Addams Family · He's / She's (família)
# ======================================================================
GOMEZ = 'p:short:1a1a1a:f4c7a1:2b2b3a:none:suit'
MORT = 'p:long:111111:efe3d6:1a1a1a:none:dress'
WED = 'p:long:222222:efe3d6:2c3e50:none:dress'


def ep6():
    B = dict(
        title="Foto de família · He's / She's",
        sub="Dizer quem é quem na família com He's e She's: brother, sister, uncle…",
        pattern_label="He's / She's",
        why="Hoje você mostra uma foto de família como os Addams e diz quem é quem: He's my brother. She's my daughter.",
        vocab=VOC(('Family', 'Família', 'FÉ-mi-li'), ('Photo', 'Foto', 'FÔU-tou'), ('Brother', 'Irmão', 'BRÂ-dâr'),
                  ('Sister', 'Irmã', 'SÍS-târ'), ('Daughter', 'Filha', 'DÓ-târ'), ('Uncle', 'Tio', 'ÂN-kol'),
                  ('Funny', 'Engraçado(a)', 'FÂ-ni'), ('Serious', 'Sério(a)', 'SÍ-ri-âs')),
        balloons=BAL(('👪', 'family'), ('📸', 'photo'), ('👦', 'brother'), ('👭', 'sister'), ('👧', 'daughter'),
                     ('🧔', 'uncle'), ('🤪', 'funny'), ('😐', 'serious')),
        cover_art={'s': 'living', 'items': [['👪', 100, 56, 20, 'bob'], ['📸', 138, 44, 12, 'bob'], ['🦇', 84, 34, 12, 'bob']], 'seed': 'ad1'},
        cover_sub="He's / She's: em 10 minutos você apresenta a família como os Addams",
        cover_say="Os Addams vão tirar uma foto de família. Quem é ele? Quem é ela? Como dizer quem é quem?",
        wrap_recap=[["She's my daughter.", 'Ela é minha filha.'], ["He's my brother.", 'Ele é meu irmão.'],
                    ["He's funny.", 'Ele é engraçado.'], ['Who is she?', 'Quem é ela?']],
        teaser={'t': 'Rock-a-Bye Baby', 'd': "Próximo padrão: He's a… e She's a… para dizer quem é e como está"},
        cast={'Gomez': ['🎩', '#34495e'], 'Morticia': ['🖤', '#6c3483'], 'Wednesday': ['🕷️', '#1b2631']},
        lines=[L('Gomez', 'Look! A family photo!', 'Olhe! Uma foto de família!'),
               L('Morticia', 'Oh, darling! Who is she?', 'Ah, querido! Quem é ela?'),
               L('Gomez', "She's Wednesday. She's my daughter.", 'É a Wednesday. Ela é minha filha.'),
               L('Wednesday', "And he's Pugsley. He's my brother.", 'E ele é o Pugsley. Ele é meu irmão.'),
               L('Morticia', "He's happy. She's serious.", 'Ele está feliz. Ela está séria.'),
               L('Wednesday', "Look, Uncle Fester! He's my uncle.", 'Olhe, tio Fester! Ele é meu tio.'),
               L('Morticia', "Yes! He's funny. Smile, everyone!", 'Sim! Ele é engraçado. Sorriam, todos!'),
               L('Wednesday', "No, thanks. I'm serious.", 'Não, obrigada. Eu sou séria.')],
        quiz=[QZ('Who is Pugsley?', 'Quem é o Pugsley?', [('👨', 'Her uncle'), ('👦', 'Her brother'), ('👩', 'Her mother')], 1, 3, 'Wednesday diz: “He’s my brother.”'),
              QZ('Who is funny?', 'Quem é engraçado?', [('👦', 'Pugsley'), ('🕷️', 'Wednesday'), ('🧔', 'Uncle Fester')], 2, 6, 'A Morticia diz: “He’s funny.” sobre o tio Fester.'),
              QZ('How is Wednesday?', 'Como está a Wednesday?', [('😐', 'Serious'), ('🤪', 'Funny'), ('😊', 'Happy')], 0, 4, 'A Morticia diz: “She’s serious.”')],
        rdg_q={'q': "Como dizer “Ela é minha irmã”?", 'o': ["She is sister.", "He's my sister.", "She's my sister."], 'a': 2,
               'why': "Fale de uma mulher com **She's** e use **my** antes do parentesco: She's **my** sister."},
        dictate=[['Look! A family photo!', 'Olhe! Uma foto de família!'], ["She's my daughter.", 'Ela é minha filha.'],
                 ["He's my brother.", 'Ele é meu irmão.'], ["He's funny.", 'Ele é engraçado.']],
        produce=PROD("A Morticia pergunta: *Who is he? Who is she?* **Diga quem é um homem e uma mulher da sua família com He's e She's e como um deles é.**",
                     "Ex.: He's my brother. She's my sister. She's funny.",
                     ["He's my brother.", "She's my sister.", "He's funny."],
                     "He's my brother. He's funny. She's my sister.",
                     ['Falei de um homem com He’s…?', 'Falei de uma mulher com She’s…?', 'Disse como ele ou ela é?'],
                     [r"\bhe['’]s\s+my\s+\w+", r"\bshe['’]s\s+my\s+\w+", r"\b(?:he|she)['’]s\s+(?!my\b)\w+"],
                     [[["He's my brother.", 'Ele é meu irmão.'], ["He's my uncle.", 'Ele é meu tio.']],
                      [["She's my sister.", 'Ela é minha irmã.'], ["She's my daughter.", 'Ela é minha filha.']],
                      [["He's funny.", 'Ele é engraçado.'], ["She's serious.", 'Ela é séria.']]],
                     ['Ele! 👨', 'Ela! 👩', 'Boa descrição! 😄'],
                     ['What a lovely family! Smile, everyone!', 'Que família linda! Sorriam, todos!']),
        rs=RS('living', 'hall', 'home1', 'kitchen', 'yard', 'bedroom', 'diner', 'school', 'living', 'hall', 'cafe2'),
        sc='living')
    X = dict(
        n=7030001, review=True, names=('Gomez', 'Wednesday'),
        stage=dict(rs='living', chars=[[GOMEZ, 26, 0, 1.0], [MORT, 54, 1, 1.0], [WED, 82, 1, 0.8]]),
        obra=dict(name='The Addams Family', kind='📺 Série · 1964', year='1964',
                  text='Família esquisita criada pelo cartunista americano Charles Addams, que desenhava os personagens na revista The New Yorker desde 1938. A série de TV estreou em 1964. Gomez, Morticia, Wednesday e Pugsley moram numa casa sombria e adoram tudo o que é estranho.',
                  line=['Snap, snap!', 'Estalo, estalo! (os dois estalos de dedos do tema da série)'],
                  pa=dict(t='haunted', e=['🏚️', '🕷️', '🦇'], p='g', v=0)),
        gancho=['Gomez', 'Look! A family photo!', 'Olhe! Uma foto de família!'],
        hot=[HOT('📸', 14, 16, 'photo', 'foto', "It's a family photo.", 'É uma foto de família.'),
             HOT('👦', 40, 14, 'brother', 'irmão', "He's my brother.", 'Ele é meu irmão.'),
             HOT('👭', 66, 14, 'sister', 'irmã', "She's my sister.", 'Ela é minha irmã.'),
             HOT('🧔', 88, 16, 'uncle', 'tio', "He's my uncle. He's funny.", 'Ele é meu tio. Ele é engraçado.'),
             HOT('🕷️', 12, 82, 'spider', 'aranha', "She's a big spider.", 'Ela é uma aranha grande.')],
        gap=[GAP('___ my brother.', 'Ele é meu irmão.', ["He's", "She's", "I'm"], 0, 'Irmão é homem: **He\'s** my brother.'),
             GAP('___ my sister.', 'Ela é minha irmã.', ["He's", "She's", "It's"], 1, 'Irmã é mulher: **She\'s** my sister.'),
             GAP("He's my ___.", 'Ele é meu tio.', ['daughter', 'sister', 'uncle'], 2, '**uncle** = tio. Daughter e sister são mulheres.'),
             GAP("She's ___.", 'Ela é séria.', ['serious', 'brother', 'uncle'], 0, '**serious** = sério(a). Brother e uncle são pessoas, não descrevem.')],
        trap=[TRAP(["He's my sister.", "She's my sister.", 'She my sister.'], 1, 'Irmã é mulher: **She\'s** my sister. E o verbo não pode faltar.'),
              TRAP(['She is my brother.', 'He my brother.', "He's my brother."], 2, 'Irmão é homem: **He\'s** my brother.')],
        sticker=dict(title='Foto dos Addams', sub='The Addams Family · 1964', rs='living', chars=[[GOMEZ, 34, 0, 1.0], [MORT, 68, 1, 1.0]]),
        speakers={'Gomez': GOMEZ, 'Morticia': MORT, 'Wednesday': WED},
        rule=dict(
            who=GOMEZ, head="He's · She's", sub='Quem é quem na família.',
            say=["She's Wednesday. She's my daughter.", 'Ela é a Wednesday. Ela é minha filha.'],
            formula=[dict(from_=[['He', 0], ['is', 1], ['my brother.', 2]], to=[["He's", 2], ['my brother.', 2]], say="He's my brother.", note='**He\'s** = ele (homem, menino). **my** = meu / minha.'),
                     dict(from_=[['She', 3], ['is', 1], ['my sister.', 2]], to=[["She's", 2], ['my sister.', 2]], say="She's my sister.", note='**She\'s** = ela (mulher, menina).')],
            uses=[dict(ico='👦', tag='Irmão', en="He's my brother.", pt='Ele é meu irmão.'),
                  dict(ico='👧', tag='Filha', en="She's my daughter.", pt='Ela é minha filha.'),
                  dict(ico='🤪', tag='Como ele é', en="He's funny.", pt='Ele é engraçado.'),
                  dict(ico='😐', tag='Como ela é', en="She's serious.", pt='Ela é séria.')],
            rules=[dict(tag="He's", c=0, text='Falando de **um homem ou menino** da família.', ex="He's my uncle."),
                   dict(tag="She's", c=3, text='Falando de **uma mulher ou menina** da família.', ex="She's my sister."),
                   dict(tag='my + família', c=2, text='**my** vem antes do parentesco e vale para homem e mulher.', ex="He's my brother. She's my sister.")],
            tips=['Em português dizemos “ele é irmão” ou “é meu irmão”. Em inglês o **my** é quase sempre dito: He\'s **my** brother.']),
        mission_ic='📸')
    XT = dict(
        exp=[EXP('📸', 'Say cheese!', 'Informal', 'Sorria! (para a foto)', 'Quando alguém vai **tirar uma foto** e pede para todos sorrirem.', ['Say cheese, everyone!', 'Sorriam, todos!']),
             EXP('🏠', 'Make yourself at home.', 'Expressão', 'Fique à vontade.', 'Para deixar um **visitante** confortável na sua casa.', ['Come in! Make yourself at home.', 'Entre! Fique à vontade.']),
             EXP('🤝', 'Long time no see!', 'Informal', 'Quanto tempo!', 'Ao rever **alguém depois de muito tempo**.', ['Uncle Fester! Long time no see!', 'Tio Fester! Quanto tempo!']),
             EXP('💬', "He's really nice.", 'Expressão', 'Ele é muito simpático.', 'Para **elogiar** uma pessoa. Com mulher: She\'s really nice.', ["Look at Fester. He's really nice.", 'Olhe o Fester. Ele é muito simpático.'])],
        exp_scene=dict(rs='living', lines=[
            L('Morticia', 'Fester! **Long time no see**!', 'Fester! Quanto tempo!'),
            L('Gomez', 'Come in! **Make yourself at home**.', 'Entre! Fique à vontade.'),
            L('Wednesday', 'Look, Mother! **He\'s really nice**.', 'Olhe, mãe! Ele é muito simpático.'),
            L('Gomez', 'Now, a photo! **Say cheese**, everyone!', 'Agora, uma foto! Sorriam, todos!'),
            L('Wednesday', "I'm serious. No cheese.", 'Eu sou séria. Nada de queijo.'),
            L('Morticia', 'Smile, Wednesday!', 'Sorria, Wednesday!')]),
        lab=dict(
            short='final -er', title='Laboratório de sons: o final -er de sister',
            say='Em inglês, o final -er de sister, brother e daughter não é “ér”. Vamos treinar com os Addams.',
            intro=dict(what='O final **-er** de **sister**, **brother** e **daughter** é um som curto e fraco, parecido com “âr”, com o r inglês.',
                       how='Deixe a boca relaxada, diga um “â” curto e leve a ponta da língua um pouco para trás, sem vibrar. A última sílaba é fraca e rápida.',
                       pt='Em português lemos “ér” forte (mulher). Em inglês a sílaba final é fraca: **SÍS-târ**, não “sis-TÉR”.'),
            ex=[['sister', 'SÍS-târ', 'irmã', 'sílaba final fraca e curta'], ['brother', 'BRÂ-dâr', 'irmão', 'th de “brother” + final fraco'],
                ['daughter', 'DÓ-târ', 'filha', 'o “gh” não soa; só o final fraco']],
            pairs=[['her', 'hair', 'her: som fraco “âr” · hair: “ér” aberto'], ['fur', 'fair', 'fur (pelo): “âr” · fair (justo): “ér”'],
                   ['bird', 'bed', 'bird: “bârd” · bed: “béd”']],
            tip='Pense num “âr” curtinho, com a boca relaxada. Não abra a boca em “ér”.',
            phrase=["She's my sister. He's my brother.", 'Ela é minha irmã. Ele é meu irmão.'],
            rounds=[RND('her', ['her', 'hair'], 0, '**her** tem o som fraco “âr”. **Hair** (cabelo) é “ér” aberto.'),
                    RND('fair', ['fur', 'fair'], 1, '**Fair** (justo) tem o “ér” aberto. **Fur** (pelo) é “âr”.'),
                    RND('bird', ['bed', 'bird'], 1, '**Bird** (pássaro) tem o “âr”. **Bed** (cama) tem “é”.')]),
        hunt=[HW('hair', ['her', 'hair'], 1, '**hair** = cabelo, com “ér” aberto.'),
              HP('sister', ['📸', '👭', '🧔'], 1, '**sister** = irmã.'),
              HW('bed', ['bed', 'bird'], 0, '**bed** = cama, som “é”.'),
              HP('brother', ['👦', '🧔', '📸'], 0, '**brother** = irmão.'),
              HW('fur', ['fur', 'fair'], 0, '**fur** = pelo, som “âr”.')])
    VB = dict(title='Verbos de uma tarde em família', tip='Quatro verbos: play, watch, carry e tell.',
              items=[VERB('play', '🎲', 'brincar, jogar', 'I play with my brother.', 'Pugsley play**s** with a toy.', 'I play with my brother.', 'Eu brinco com o meu irmão.', '**play** = brincar, jogar. Com he/she: **plays**.'),
                     VERB('watch', '📺', 'assistir, observar', 'I watch a funny show.', 'She watch**es** a funny show.', 'I watch a funny show.', 'Eu assisto a um programa engraçado.', '**watch** = assistir. Com he/she: **watches** (termina em -ch: +es).'),
                     VERB('carry', '🧳', 'carregar', 'I carry the photo.', 'Fester carr**ies** the photo.', 'I carry the photo.', 'Eu carrego a foto.', '**carry** = carregar. Com he/she: **carries** (y → ies).'),
                     VERB('tell', '🗣️', 'contar, dizer', 'I tell a story.', 'He tell**s** a funny story.', 'I tell a story.', 'Eu conto uma história.', '**tell** = contar. Com he/she: **tells**.')])
    MR = dict(
        mold=[MOLD('Ele é…', [('quem', [("He's", 'ele é')]), ('família', [('my brother', 'meu irmão'), ('my uncle', 'meu tio'), ('my dad', 'meu pai'), ('funny', 'engraçado'), ('serious', 'sério')])]),
              MOLD('Ela é…', [('quem', [("She's", 'ela é')]), ('família', [('my sister', 'minha irmã'), ('my daughter', 'minha filha'), ('my mom', 'minha mãe'), ('funny', 'engraçada'), ('serious', 'séria')])]),
              MOLD('Perguntar quem é', [('pergunta', [('Who is', 'quem é')]), ('pessoa', [('he', 'ele'), ('she', 'ela')])], ('?', '?'))],
        speak=[['Say cheese! He\'s my brother.', 'Sorria! Ele é meu irmão.'], ["Long time no see! He's really nice.", 'Quanto tempo! Ele é muito simpático.']],
        trap=[TRM('“Make yourself at home” quer dizer…', ['Fique à vontade.', 'Construa uma casa.', 'Vá para casa.'], 0, '**Make yourself at home.** = fique à vontade.', 'Make yourself at home.'),
              TRM('Qual frase está certa?', ['Long time not see!', 'Long time no see!', 'Long no time see!'], 1, 'A expressão é **Long time no see!** (quanto tempo!).', 'Long time no see!')],
        gap=[GPM('___ cheese, everyone!', 'Sorriam, todos!', ['Say', 'Tell', 'Make'], 0, 'A expressão é **Say cheese!**', 'Say cheese, everyone!'),
             GPM('Make yourself at ___.', 'Fique à vontade.', ['house', 'home', 'room'], 1, 'A expressão é **at home**.', 'Make yourself at home.')],
        expq=[EQ('Você vai tirar uma foto da família. O que diz?', ['Long time no see!', 'Say cheese!', "He's really nice."], 1, '**Say cheese!** = sorria!'),
              EQ('Um amigo chega à sua casa. Diga para ele ficar à vontade.', ['Make yourself at home.', 'Say cheese!', 'Long time no see!'], 0, '**Make yourself at home.** = fique à vontade.'),
              EQ('Você encontra seu tio depois de muitos anos.', ['Say cheese!', 'Make yourself at home.', 'Long time no see!'], 2, '**Long time no see!** = quanto tempo!')],
        missions=[MIS('📸', 'Minha foto de família', "Apresente a sua família com He's e She's.",
                      prompt="Você mostra uma foto da sua família. **Diga quem é um homem e quem é uma mulher da foto com He's my… e She's my… e como uma pessoa é.**",
                      ph='Escreva a sua resposta aqui…', chips=["He's my…", "She's my…"],
                      model="He's my brother. She's my sister. She's funny.",
                      check=["Falei de um homem com He's my…?", "Falei de uma mulher com She's my…?", 'Disse como ele ou ela é?'],
                      kw=[r"\bhe['’]s\s+my\s+\w+", r"\bshe['’]s\s+my\s+\w+", r"\b(?:he|she)['’]s\s+(?!my\b)\w+"],
                      tips=[[["He's my brother.", 'Ele é meu irmão.']], [["She's my sister.", 'Ela é minha irmã.']], [["She's funny.", 'Ela é engraçada.'], ["He's serious.", 'Ele é sério.']]],
                      ok=['Ele! 👨', 'Ela! 👩', 'Boa descrição! 😄'], reply=['What a lovely family!', 'Que família linda!']),
                  MIS('🤝', 'Visita surpresa', 'Use as expressões do episódio.',
                      prompt='Seu tio chega de surpresa. **Diga que faz muito tempo que não o vê, peça para ele ficar à vontade e chame todos para a foto.**',
                      ph='Escreva a sua resposta aqui…', chips=['Long time no see!'],
                      model='Long time no see! Make yourself at home. Say cheese, everyone!',
                      check=['Disse que faz tempo que não vejo?', 'Pedi para ficar à vontade?', 'Chamei todos para a foto?'],
                      kw=[r'\blong time no see\b', r'\bmake yourself at home\b', r'\bsay cheese\b'],
                      tips=[[['Long time no see!', 'Quanto tempo!']], [['Make yourself at home.', 'Fique à vontade.']], [['Say cheese!', 'Sorriam!']]],
                      ok=['Quanto tempo! 🤝', 'Visita em casa! 🏠', 'Foto! 📸'], reply=['Thank you! What a nice family!', 'Obrigado! Que família simpática!'])])
    CX = [CXF('Mom, dad, brother and sister: this is my ___.', 'Mãe, pai, irmão e irmã: esta é a minha família.', ['family', 'photo', 'uncle']),
          CXF('Say cheese! Click! Now we have a ___.', 'Sorria! Clique! Agora temos uma foto.', ['photo', 'family', 'daughter']),
          CXF('We have the same mom and dad. He is my ___.', 'Temos a mesma mãe e o mesmo pai. Ele é meu irmão.', ['brother', 'uncle', 'daughter']),
          CXF('He is my dad\'s brother. He is my ___.', 'Ele é irmão do meu pai. Ele é meu tio.', ['uncle', 'brother', 'photo']),
          CXF('He tells jokes and everybody laughs. He is ___.', 'Ele conta piadas e todo mundo ri. Ele é engraçado.', ['funny', 'serious', 'family']),
          CXF('Mr. and Mrs. Addams have a girl. She is their ___.', 'O casal Addams tem uma menina. Ela é a filha deles.', ['daughter', 'uncle', 'photo'])]
    return ep(B, X, XT, VB, MR, CX)


# ======================================================================
# POS 7 · n=70002 · Rock-a-Bye Baby · He's a… / She's a… (papel e estado)
# ======================================================================
MOM = 'p:long:6b3f26:f4c7a1:e07a9f:none:dress'
DAD = 'p:short:2c2c2c:e8b48a:2f6fa8:glasses:shirt'
SAM = 'p:cap:8b5a2b:f4c7a1:f1c40f:none:shirt'


def ep7():
    B = dict(
        title="Say Hi to Mom · He's a… / She's a…",
        sub="Dizer quem é e como está: He's a dad, She's a baby, She's sleepy",
        pattern_label="He's a… / She's a…",
        why="Hoje você usa He's e She's com a, para dizer quem alguém é (a baby, a dad, a student) e como está (sleepy, small, happy).",
        vocab=VOC(('Mom', 'Mãe', 'MÓM'), ('Dad', 'Pai', 'DÉD'), ('Baby', 'Bebê', 'BÊI-bi'), ('Sleepy', 'Com sono', 'SLÍ-pi'),
                  ('Small', 'Pequeno(a)', 'SMÓL'), ('Student', 'Estudante', 'STIÚ-dent'), ('Pet', 'Bicho de estimação', 'PÉT')),
        balloons=BAL(('👩', 'mom'), ('👨', 'dad'), ('👶', 'baby'), ('😴', 'sleepy'), ('🤏', 'small'), ('🎒', 'student'), ('🐱', 'pet')),
        cover_art={'s': 'bedroom', 'items': [['👶', 100, 56, 20, 'bob'], ['🌙', 138, 40, 12, 'bob'], ['🧸', 84, 34, 12, 'bob']], 'seed': 'rb1'},
        cover_sub="He's a… / She's a…: em 10 minutos você fala de mãe, pai e bebê",
        cover_say="Chegou um bebê em casa! Quem é ela? Como ela está? Como dizer isso em inglês?",
        wrap_recap=[["She's a baby.", 'Ela é um bebê.'], ["He's a happy dad.", 'Ele é um pai feliz.'],
                    ["She's sleepy.", 'Ela está com sono.'], ['Say hi to Dad.', 'Dê um oi para o papai.']],
        teaser={'t': 'Coming to America', 'd': 'Próximo padrão: Are you from…? para perguntar de onde alguém é'},
        cast={'Mom': ['👩', '#e07a9f'], 'Sam': ['👦', '#d4a017'], 'Dad': ['👨', '#2f6fa8']},
        lines=[L('Mom', "Shh, Sam! She's sleepy.", 'Psiu, Sam! Ela está com sono.'),
               L('Sam', 'Who is she, Mom?', 'Quem é ela, mãe?'),
               L('Mom', "She's your sister. She's a baby.", 'Ela é a sua irmã. Ela é um bebê.'),
               L('Sam', "Wow! She's small. Is she happy?", 'Uau! Ela é pequena. Ela está feliz?'),
               L('Dad', 'Yes, she is. And Sam is a big brother!', 'Sim, está. E o Sam é um irmão mais velho!'),
               L('Sam', "Hi, baby! I'm Sam. I'm your brother.", 'Oi, bebê! Eu sou o Sam. Sou o seu irmão.'),
               L('Mom', "Look, baby! Say hi to Dad. He's a happy dad!", 'Olhe, bebê! Dê um oi para o papai. Ele é um pai feliz!'),
               L('Dad', "Shh! She's sleepy again.", 'Psiu! Ela está com sono de novo.')],
        quiz=[QZ('Who is sleepy?', 'Quem está com sono?', [('👶', 'The baby'), ('👨', 'Dad'), ('👦', 'Sam')], 0, 0, 'A Mãe diz: “She’s sleepy.” sobre o bebê.'),
              QZ('Who is the baby?', 'Quem é o bebê?', [('👩', "Sam's mom"), ('👶', "Sam's sister"), ('🐱', "Sam's pet")], 1, 2, 'A Mãe diz: “She’s your sister.”'),
              QZ('What is Sam now?', 'O que o Sam é agora?', [('👨', 'A dad'), ('👶', 'A baby'), ('👦', 'A big brother')], 2, 4, 'O Pai diz: “Sam is a big brother!”')],
        rdg_q={'q': 'Qual frase fala do bebê (uma menina)?', 'o': ["He's a baby.", 'Is a baby.', "She's a baby."], 'a': 2,
               'why': 'Menina → **She\'s**. Depois vem **a** + o papel: She\'s **a** baby.'},
        dictate=[['Shh! She\'s sleepy.', 'Psiu! Ela está com sono.'], ["She's a baby.", 'Ela é um bebê.'],
                 ["He's a happy dad.", 'Ele é um pai feliz.'], ['Say hi to Mom.', 'Dê um oi para a mamãe.']],
        produce=PROD("O Sam pergunta: *Who is he? Who is she?* **Diga quem são duas pessoas usando He's a… e She's a… e diga como uma delas está.**",
                     "Ex.: He's a dad. She's a student. She's happy.",
                     ["He's a dad.", "She's a student.", "She's happy."],
                     "He's a dad. She's a student. She's happy.",
                     ['Usei He’s a… para um homem?', 'Usei She’s a… para uma mulher?', 'Disse como alguém está?'],
                     [r"\bhe['’]s\s+an?\s+\w+", r"\bshe['’]s\s+an?\s+\w+", r"\b(?:he|she)['’]s\s+(?!an?\b)\w+"],
                     [[["He's a dad.", 'Ele é um pai.'], ["He's a student.", 'Ele é um estudante.']],
                      [["She's a mom.", 'Ela é uma mãe.'], ["She's a baby.", 'Ela é um bebê.']],
                      [["She's happy.", 'Ela está feliz.'], ["He's sleepy.", 'Ele está com sono.']]],
                     ['Ele é… 👨', 'Ela é… 👩', 'Como está! 😴'],
                     ['What a nice family! Say hi to Mom!', 'Que família simpática! Dê um oi para a mamãe!']),
        rs=RS('bedroom', 'living', 'home1', 'kitchen', 'park2', 'clinic', 'cafe', 'school', 'bedroom', 'home1', 'yard'),
        sc='bedroom')
    X = dict(
        n=70002, review=True, names=('Mom', 'Sam'),
        stage=dict(rs='bedroom', chars=[[MOM, 26, 0, 1.0], [SAM, 54, 1, 0.8], [DAD, 82, 1, 1.0]]),
        obra=dict(name='Rock-a-Bye Baby', kind='🎶 Canção de ninar · séc. XVIII', year='séc. XVIII',
                  text='Canção de ninar tradicional em inglês, com registros do século 18. A letra fala de um bebê num berço no alto de uma árvore, balançando com o vento. Pais de língua inglesa cantam essa música para o bebê dormir.',
                  line=['Rock-a-bye, baby.', 'Dorme, neném. (primeiro verso da canção)'],
                  pa=dict(t='treehouse', e=['🌳', '👶', '🌙'], p='h', v=1)),
        gancho=['Mom', "Shh, Sam! She's sleepy.", 'Psiu, Sam! Ela está com sono.'],
        hot=[HOT('👶', 14, 16, 'baby', 'bebê', "She's a baby. She's small.", 'Ela é um bebê. Ela é pequena.'),
             HOT('😴', 40, 14, 'sleepy', 'com sono', "She's sleepy.", 'Ela está com sono.'),
             HOT('🐱', 66, 14, 'pet', 'bicho de estimação', "She's a cat. She's my pet.", 'Ela é uma gata. Ela é o meu bichinho.'),
             HOT('🎒', 88, 16, 'student', 'estudante', "He's a student.", 'Ele é um estudante.'),
             HOT('🍼', 12, 82, 'bottle', 'mamadeira', "She's hungry. Here's a bottle.", 'Ela está com fome. Aqui está a mamadeira.')],
        gap=[GAP('___ sleepy.', 'Ela está com sono.', ["He's", "She's", "I'm"], 1, 'Falando da bebê (uma menina): **She\'s** sleepy.'),
             GAP("She's ___ student.", 'Ela é estudante.', ['an', 'the', 'a'], 2, 'Antes de **student** use **a**. (**an** só antes de som de vogal.)'),
             GAP("He's a happy ___.", 'Ele é um pai feliz.', ['dad', 'mom', 'sister'], 0, '**dad** = pai. Ele é homem.'),
             GAP("She's very ___.", 'Ela é muito pequena.', ['Sam', 'small', 'Mom'], 1, '**small** = pequeno(a).')],
        trap=[TRAP(["She's a baby.", 'She a baby.', 'Is a baby.'], 0, 'Precisa do verbo: **She\'s** a baby.'),
              TRAP(["He's dad.", "He's an dad.", "He's a dad."], 2, 'Antes do papel, use **a**: He\'s **a** dad.')],
        sticker=dict(title='Sam e a bebê', sub='Rock-a-Bye Baby · séc. XVIII', rs='bedroom', chars=[[SAM, 34, 0, 0.9], [MOM, 68, 1, 1.0]]),
        speakers={'Mom': MOM, 'Sam': SAM, 'Dad': DAD},
        rule=dict(
            who=MOM, head="He's a… · She's a…", sub='Quem é e como está.',
            say=["She's a baby. She's sleepy.", 'Ela é um bebê. Ela está com sono.'],
            formula=[dict(from_=[['He', 0], ['is', 1], ['a dad.', 2]], to=[["He's", 1], ['a dad.', 2]], say="He's a dad.", note='**a** vem antes do papel: **a** dad, **a** student, **a** baby.'),
                     dict(from_=[['He', 0], ['is', 1], ['an uncle.', 2]], to=[["He's", 1], ['an uncle.', 2]], say="He's an uncle.", note='Antes de som de vogal, use **an**: **an** uncle, **an** artist.')],
            uses=[dict(ico='👶', tag='Quem é', en="She's a baby.", pt='Ela é um bebê.'),
                  dict(ico='😴', tag='Como está', en="She's sleepy.", pt='Ela está com sono.'),
                  dict(ico='🎒', tag='Papel', en="He's a student.", pt='Ele é um estudante.')],
            rules=[dict(tag='a / an', c=1, text='Antes de papel ou profissão, use **a** (ou **an** antes de som de vogal).', ex='a dad · a student · an uncle'),
                   dict(tag='só descreve', c=2, text='Se só diz como a pessoa está, **não** use a.', ex="She's sleepy. ✓  She's a sleepy. ✗")],
            tips=['Em português dizemos “ela é estudante”. Em inglês o **a** é obrigatório: She\'s **a** student.']),
        mission_ic='👶')
    XT = dict(
        exp=[EXP('💕', 'How sweet!', 'Expressão', 'Que fofo!', 'Quando alguém faz algo **carinhoso** ou você vê um **bebê**.', ['Look at the baby! How sweet!', 'Olhe o bebê! Que fofo!']),
             EXP('🙏', "You're welcome!", 'Expressão', 'De nada!', 'Resposta natural quando alguém diz **thank you**.', ["Thank you, Sam! You're welcome!", 'Obrigada, Sam! De nada!']),
             EXP('👋', 'Say hi to Dad.', 'Informal', 'Dê um oi para o papai.', 'Para **mandar um oi** a alguém ou pedir que alguém cumprimente.', ['Say hi to Dad for me!', 'Dê um oi para o papai por mim!']),
             EXP('😊', "That's so nice of you!", 'Expressão', 'Que gentileza a sua!', 'Para **agradecer** um gesto gentil.', ["A toy for the baby? That's so nice of you!", 'Um brinquedo para o bebê? Que gentileza a sua!'])],
        exp_scene=dict(rs='living', lines=[
            L('Sam', 'Mom, a toy for the baby!', 'Mãe, um brinquedo para o bebê!'),
            L('Mom', "Thank you, Sam! **That's so nice of you!**", 'Obrigada, Sam! Que gentileza a sua!'),
            L('Sam', "**You're welcome**! She's happy.", 'De nada! Ela está feliz.'),
            L('Dad', "**How sweet**! She's a happy baby.", 'Que fofo! Ela é um bebê feliz.'),
            L('Mom', 'Look, baby! **Say hi to Dad**!', 'Olhe, bebê! Dê um oi para o papai!'),
            L('Dad', 'Hi, baby! Hi, Sam!', 'Oi, bebê! Oi, Sam!')]),
        lab=dict(
            short='“a” de dad', title='Laboratório de sons: o “a” de dad',
            say='O “a” de dad, cat e sad é um som que não existe no português. Vamos treinar com o Sam.',
            intro=dict(what='O **a** de **dad**, **bad** e **sad** é um som aberto, entre o “a” e o “é”.',
                       how='Abra bem a boca, como num sorriso, deixe a língua baixa e diga um “é” aberto e curto, quase “ae”.',
                       pt='Em português não temos esse som. Muita gente diz “dêd” e o ouvinte entende **dead** (morto). Abra mais a boca: **DÉD** (pai).'),
            ex=[['dad', 'DÉD', 'pai', 'boca bem aberta'], ['sad', 'SÉD', 'triste', 'língua baixa, “é” aberto'], ['man', 'MÉN', 'homem', 'o mesmo “a” aberto']],
            pairs=[['dad', 'dead', 'dad: “a” aberto · dead: “é” fechado'], ['bad', 'bed', '“ruim” × “cama”'], ['sad', 'said', '“triste” × “disse”'], ['man', 'men', '“homem” × “homens”']],
            tip='Sorria ao dizer: o “a” de dad pede a boca bem aberta.',
            phrase=['Dad is a happy man.', 'O papai é um homem feliz.'],
            rounds=[RND('dad', ['dad', 'dead'], 0, '**Dad** (pai) tem o “a” aberto. **Dead** (morto) tem “é”.'),
                    RND('bed', ['bad', 'bed'], 1, '**Bed** (cama) tem “é”. **Bad** (ruim) tem o “a” aberto.'),
                    RND('said', ['sad', 'said'], 1, '**Said** (disse) tem “é”. **Sad** (triste) tem o “a” aberto.')]),
        hunt=[HW('dead', ['dad', 'dead'], 1, '**dead** = morto, com “é”.'),
              HP('dad', ['👨', '🛏️', '😢'], 0, '**dad** = pai.'),
              HW('sad', ['sad', 'said'], 0, '**sad** = triste, com o “a” aberto.'),
              HP('bed', ['👶', '🛏️', '👨'], 1, '**bed** = cama.'),
              HW('men', ['man', 'men'], 1, '**men** = homens, com “é”.')])
    VB = dict(title='Verbos para ajudar em casa', tip='Quatro verbos: help, cook, clean e wash.',
              items=[VERB('help', '🤝', 'ajudar', 'I help my mom.', 'Dad help**s** the baby.', 'I help my mom.', 'Eu ajudo a minha mãe.', '**help** = ajudar. Com he/she: **helps**.'),
                     VERB('cook', '🍳', 'cozinhar', 'I cook dinner.', 'Mom cook**s** dinner.', 'I cook dinner.', 'Eu faço o jantar.', '**cook** = cozinhar. Com he/she: **cooks**.'),
                     VERB('clean', '🧹', 'limpar', 'I clean my room.', 'She clean**s** the kitchen.', 'I clean my room.', 'Eu limpo o meu quarto.', '**clean** = limpar. Com he/she: **cleans**.'),
                     VERB('wash', '🫧', 'lavar', 'I wash the cup.', 'He wash**es** the cup.', 'I wash the cup.', 'Eu lavo o copo.', '**wash** = lavar. Com he/she: **washes** (termina em -sh: +es).')])
    MR = dict(
        mold=[MOLD('Ele é…', [('quem', [("He's", 'ele é')]), ('papel ou estado', [('a dad', 'um pai'), ('a student', 'um estudante'), ('a baby', 'um bebê'), ('an uncle', 'um tio'), ('happy', 'feliz'), ('sleepy', 'com sono')])]),
              MOLD('Ela é…', [('quem', [("She's", 'ela é')]), ('papel ou estado', [('a mom', 'uma mãe'), ('a student', 'uma estudante'), ('a baby', 'um bebê'), ('happy', 'feliz'), ('small', 'pequena'), ('sleepy', 'com sono')])]),
              MOLD('Dizer oi', [('verbo', [('Say hi to', 'dê um oi para')]), ('quem', [('Mom', 'a mamãe'), ('Dad', 'o papai'), ('the baby', 'o bebê'), ('Sam', 'o Sam')])], ('!', '!'))],
        speak=[['How sweet! She\'s a happy baby.', 'Que fofo! Ela é um bebê feliz.'], ["You're welcome! Say hi to Dad.", 'De nada! Dê um oi para o papai.']],
        trap=[TRM('“Say hi to Dad” quer dizer…', ['Dê um oi para o papai.', 'Diga tchau ao papai.', 'Fale com o bebê.'], 0, '**Say hi to Dad.** = dê um oi para o papai.', 'Say hi to Dad.'),
              TRM('Qual frase está certa?', ['That\'s so nice of you!', "That's so nice for you!", 'That so nice of you!'], 0, 'A expressão é **That\'s so nice of you!**', "That's so nice of you!")],
        gap=[GPM("You're ___!", 'De nada!', ['thanks', 'welcome', 'please'], 1, 'A resposta a thank you é **You\'re welcome!**', "You're welcome!"),
             GPM("That's so nice ___ you!", 'Que gentileza a sua!', ['for', 'to', 'of'], 2, 'A expressão é **nice of you**.', "That's so nice of you!")],
        expq=[EQ('Você vê um bebê muito fofo.', ['How sweet!', "You're welcome!", 'Say hi to Dad.'], 0, '**How sweet!** = que fofo!'),
              EQ('Um amigo diz thank you.', ['Say hi to Dad.', 'How sweet!', "You're welcome!"], 2, '**You\'re welcome!** = de nada!'),
              EQ('Alguém fez algo muito gentil por você.', ['Say hi to Dad.', "You're welcome!", "That's so nice of you!"], 2, '**That\'s so nice of you!** = que gentileza a sua!')],
        missions=[MIS('👨‍👩‍👧', 'Minha família', "Diga quem são e como estão as pessoas.",
                      prompt='Você mostra a sua família a um amigo. **Diga quem é um homem e quem é uma mulher com He\'s a… e She\'s a… e como uma pessoa está.**',
                      ph='Escreva a sua resposta aqui…', chips=["He's a…", "She's a…"],
                      model="He's a dad. She's a mom. She's happy.",
                      check=["Usei He's a…?", "Usei She's a…?", 'Disse como alguém está?'],
                      kw=[r"\bhe['’]s\s+an?\s+\w+", r"\bshe['’]s\s+an?\s+\w+", r"\b(?:he|she)['’]s\s+(?!an?\b)\w+"],
                      tips=[[["He's a dad.", 'Ele é um pai.']], [["She's a student.", 'Ela é uma estudante.']], [["She's sleepy.", 'Ela está com sono.']]],
                      ok=['Ele é… 👨', 'Ela é… 👩', 'Como está! 😊'], reply=['Nice! What a happy family!', 'Legal! Que família feliz!']),
                  MIS('🎁', 'Presente para o bebê', 'Use as expressões do episódio.',
                      prompt='Seu amigo trouxe um presente para o bebê. **Diga que foi gentil dele, que o bebê é fofo e peça para ele dar um oi para o papai.**',
                      ph='Escreva a sua resposta aqui…', chips=["That's so nice of you!"],
                      model="That's so nice of you! How sweet! Say hi to Dad.",
                      check=['Agradeci a gentileza?', 'Disse que é fofo?', 'Pedi um oi para o papai?'],
                      kw=[r"\bthat['’]s so nice of you\b", r'\bhow sweet\b', r'\bsay hi to\b'],
                      tips=[[["That's so nice of you!", 'Que gentileza a sua!']], [['How sweet!', 'Que fofo!']], [['Say hi to Dad.', 'Dê um oi para o papai.']]],
                      ok=['Gentil! 😊', 'Fofo! 💕', 'Oi! 👋'], reply=["You're welcome! She's happy.", 'De nada! Ela está feliz.'])])
    CX = [CXF('She cooks dinner and says goodnight. She is my ___.', 'Ela faz o jantar e dá boa-noite. Ela é a minha mãe.', ['mom', 'dad', 'pet']),
          CXF('He works and plays with me. He is my ___.', 'Ele trabalha e brinca comigo. Ele é o meu pai.', ['dad', 'mom', 'student']),
          CXF('She is one month old. She drinks milk and cries. She is a ___.', 'Ela tem um mês. Bebe leite e chora. Ela é um bebê.', ['baby', 'student', 'pet']),
          CXF("It's 11 p.m. and my eyes are closing. I'm ___.", 'São 11 da noite e meus olhos estão fechando. Estou com sono.', ['sleepy', 'small', 'student']),
          CXF('A mouse is not big. It is ___.', 'Um rato não é grande. Ele é pequeno.', ['small', 'sleepy', 'dad']),
          CXF('My cat lives with me and I love her. She is my ___.', 'Minha gata mora comigo e eu a amo. Ela é meu bichinho.', ['pet', 'student', 'baby'])]
    return ep(B, X, XT, VB, MR, CX)


# ======================================================================
# POS 8 · n=9802 · Coming to America · Are you from…?
# ======================================================================
AKEEM = 'p:short:1a1a1a:8d5524:6c3483:crown:suit'
SEMMI = 'p:short:2b1d12:5c3a21:2e86c1:none:shirt'
OFFICER = 'p:cap:2c3e50:f4c7a1:34495e:none:shirt'


def ep8():
    B = dict(
        title="Where Are You From? · Are you from…?",
        sub="Perguntar de onde alguém é: Are you from…? e responder I'm from…",
        pattern_label="Are you from…?",
        why="Hoje você pergunta e diz de onde é, como o príncipe Akeem chegando a Nova York: Are you from Mexico? I'm from Brazil.",
        vocab=VOC(('Country', 'País', 'KÂN-tri'), ('City', 'Cidade', 'SÍ-ti'), ('Plane', 'Avião', 'PLÊIN'), ('Brazil', 'Brasil', 'bra-ZÍL'),
                  ('Mexico', 'México', 'MÉK-si-kou'), ('Africa', 'África', 'É-fri-ka'), ('The U.S.', 'Estados Unidos', 'dhi iu-ÉS')),
        balloons=BAL(('🏳️', 'country'), ('🏙️', 'city'), ('✈️', 'plane'), ('🇧🇷', 'Brazil'), ('🇲🇽', 'Mexico'), ('🌍', 'Africa'), ('🇺🇸', 'The U.S.')),
        cover_art={'s': 'airport2', 'items': [['✈️', 100, 56, 20, 'bob'], ['🌍', 138, 44, 12, 'bob'], ['🗽', 84, 34, 12, 'bob']], 'seed': 'ca1'},
        cover_sub='Are you from…? Em 10 minutos você pergunta de onde as pessoas são',
        cover_say='O príncipe Akeem chega a Nova York. O policial do aeroporto pergunta: de onde você é? Como perguntar e responder?',
        wrap_recap=[['Are you from Mexico?', 'Você é do México?'], ["I'm from Brazil.", 'Eu sou do Brasil.'],
                    ['Where are you from?', 'De onde você é?'], ["No, I'm not.", 'Não, não sou.']],
        teaser={'t': "Gulliver's Travels", 'd': 'Próximo padrão: Are you a…? para conversar em um hotel'},
        cast={'Akeem': ['👑', '#6c3483'], 'Semmi': ['🧳', '#2e86c1'], 'Officer': ['🛂', '#34495e']},
        lines=[L('Officer', 'Welcome to the U.S.! Where are you from?', 'Bem-vindo aos EUA! De onde você é?'),
               L('Akeem', "I'm from Zamunda. It's a big country.", 'Eu sou de Zamunda. É um país grande.'),
               L('Officer', 'Are you here for work?', 'Você está aqui a trabalho?'),
               L('Akeem', "No, I'm not. I'm here for fun!", 'Não, não estou. Estou aqui para me divertir!'),
               L('Officer', 'Are you from Zamunda too, sir?', 'O senhor também é de Zamunda?'),
               L('Semmi', "Yes, I am. I'm his friend.", 'Sim, sou. Eu sou amigo dele.'),
               L('Officer', 'Are you new in New York?', 'Vocês são novos em Nova York?'),
               L('Akeem', 'Yes, I am. Hello, big city!', 'Sim, sou. Olá, cidade grande!')],
        quiz=[QZ('Where is Akeem from?', 'De onde o Akeem é?', [('🇲🇽', 'Mexico'), ('🇧🇷', 'Brazil'), ('👑', 'Zamunda')], 2, 1, 'Akeem diz: “I’m from Zamunda.”'),
              QZ('Is Akeem here for work?', 'O Akeem está aqui a trabalho?', [('✅', 'Yes, he is'), ('❌', "No, he isn't"), ('🤷', 'Maybe')], 1, 3, 'Akeem diz: “No, I’m not. I’m here for fun!”'),
              QZ('Who is Semmi?', 'Quem é o Semmi?', [('🧳', "Akeem's friend"), ('🛂', 'The officer'), ('👩', 'A teacher')], 0, 5, 'Semmi diz: “I’m his friend.”')],
        rdg_q={'q': 'Como perguntar “Você é do Brasil?”', 'o': ['Is you from Brazil?', 'Are you from Brazil?', 'Do you from Brazil?'], 'a': 1,
               'why': 'Com **you**, a pergunta começa com **Are**: Are you from Brazil?'},
        dictate=[['Where are you from?', 'De onde você é?'], ["I'm from Zamunda.", 'Eu sou de Zamunda.'],
                 ['Are you from Africa?', 'Você é da África?'], ["I'm here for fun.", 'Estou aqui para me divertir.']],
        produce=PROD('O policial pergunta: *Where are you from? Are you here for work?* **Diga de onde você é, por que está aqui e faça uma pergunta com Are you from…? para ele.**',
                     "Ex.: I'm from Brazil. I'm here for fun. Are you from New York?",
                     ["I'm from…", "I'm here for fun.", 'Are you from…?'],
                     "I'm from Brazil. I'm here for fun. Are you from New York?",
                     ['Disse de onde eu sou com I’m from…?', 'Disse por que estou aqui?', 'Fiz uma pergunta com Are you from…?'],
                     [r"\bi['’]m from\s+\w+", r"\bi['’]m here for\s+\w+", r"\bare you from\b[^.!?]*\?"],
                     [[["I'm from Brazil.", 'Eu sou do Brasil.'], ["I'm from Mexico.", 'Eu sou do México.']],
                      [["I'm here for fun.", 'Estou aqui para me divertir.'], ["I'm here for work.", 'Estou aqui a trabalho.']],
                      [['Are you from New York?', 'Você é de Nova York?'], ['Are you from Canada?', 'Você é do Canadá?']]],
                     ['De onde eu sou! 🌎', 'Por que estou aqui! ✈️', 'Boa pergunta! ❓'],
                     ["Welcome! I'm from New York. Have fun!", 'Bem-vindo! Eu sou de Nova York. Divirta-se!']),
        rs=RS('airport', 'airport2', 'lobby', 'street', 'station', 'counter', 'cafe3', 'school', 'airport2', 'nyc', 'flags'),
        sc='airport2')
    X = dict(
        n=9802, review=True, names=('Akeem', 'Officer'),
        stage=dict(rs='airport2', chars=[[AKEEM, 26, 0, 1.0], [SEMMI, 54, 0, 1.0], [OFFICER, 84, 1, 1.0]]),
        obra=dict(name='Coming to America', kind='🎬 Filme · 1988', year='1988',
                  text='Filme de comédia americano de 1988, dirigido por John Landis e estrelado por Eddie Murphy. O príncipe Akeem, de um país africano imaginário chamado Zamunda, viaja para Nova York, no bairro do Queens, em busca de uma esposa.',
                  line=['Coming to America', 'Chegando à América. (o título do filme)'],
                  pa=dict(t='planewin', e=['✈️', '👑', '🗽'], p='d', v=0)),
        gancho=['Officer', 'Welcome to the U.S.! Where are you from?', 'Bem-vindo aos EUA! De onde você é?'],
        hot=[HOT('✈️', 14, 16, 'plane', 'avião', 'Is the plane from Brazil? Yes, it is.', 'O avião é do Brasil? Sim, é.'),
             HOT('🇧🇷', 40, 14, 'Brazil', 'Brasil', 'Are you from Brazil?', 'Você é do Brasil?'),
             HOT('🇲🇽', 66, 14, 'Mexico', 'México', 'Are you from Mexico?', 'Você é do México?'),
             HOT('🌍', 88, 16, 'Africa', 'África', 'Are you from Africa?', 'Você é da África?'),
             HOT('🏙️', 12, 82, 'city', 'cidade', 'Are you from this city?', 'Você é desta cidade?')],
        gap=[GAP('___ you from Mexico?', 'Você é do México?', ['Are', 'Is', 'Do'], 0, 'Com **you**, a pergunta começa com **Are**.'),
             GAP("I'm ___ Brazil.", 'Eu sou do Brasil.', ['of', 'from', 'in'], 1, 'Origem se diz com **from**: I\'m **from** Brazil.'),
             GAP('Where ___ you from?', 'De onde você é?', ['is', 'do', 'are'], 2, 'Com **you**: Where **are** you from?'),
             GAP('Brazil is a big ___.', 'O Brasil é um país grande.', ['country', 'city', 'plane'], 0, '**country** = país. **City** é cidade.')],
        trap=[TRAP(['You are from Mexico?', 'Are you from Mexico?', 'Do you from Mexico?'], 1, 'O verbo vai para o início: **Are you** from Mexico?'),
              TRAP(["I'm from Brazil.", "I'm of Brazil.", 'I from Brazil.'], 0, 'Em inglês dizemos **from**, não “of”, e o verbo (I\'m) é obrigatório.')],
        sticker=dict(title='Akeem em Nova York', sub='Coming to America · 1988', rs='airport2', chars=[[AKEEM, 34, 0, 1.0], [SEMMI, 68, 1, 1.0]]),
        speakers={'Akeem': AKEEM, 'Semmi': SEMMI, 'Officer': OFFICER},
        rule=dict(
            who=OFFICER, head='Are you from…?', sub='De onde você é?',
            say=['Are you from Zamunda too, sir?', 'O senhor também é de Zamunda?'],
            formula=[dict(from_=[['You', 0], ['are', 1], ['from Brazil.', 3]], to=[['Are', 1], ['you', 0], ['from Brazil?', 3]], say='Are you from Brazil?', note='O verbo **are** vai para a frente de **you**.')],
            uses=[dict(ico='❓', tag='Perguntar', en='Are you from Mexico?', pt='Você é do México?'),
                  dict(ico='🌎', tag='Responder', en="I'm from Brazil.", pt='Eu sou do Brasil.'),
                  dict(ico='🗣️', tag='De onde?', en='Where are you from?', pt='De onde você é?'),
                  dict(ico='✅', tag='Resposta curta', en='Yes, I am. / No, I\'m not.', pt='Sim, sou. / Não, não sou.')],
            rules=[dict(tag='Are you from', c=0, text='Pergunta sim ou não: **Are you from** + lugar?', ex='Are you from Africa?'),
                   dict(tag="I'm from", c=2, text='Para dizer o seu lugar: **I\'m from** + lugar.', ex="I'm from Brazil."),
                   dict(tag='Where…?', c=1, text='Quando você **não** sabe o lugar, use **Where are you from?**', ex='Where are you from?')],
            tips=['Países e cidades começam com **maiúscula** em inglês: Brazil, Mexico, New York. E use **from**, nunca “of”.']),
        mission_ic='🛂')
    XT = dict(
        exp=[EXP('❓', 'First time here?', 'Informal', 'Primeira vez aqui?', 'Pergunta simpática a quem **acabou de chegar** a um lugar.', ['First time here? Welcome!', 'Primeira vez aqui? Bem-vindo!']),
             EXP('🎉', "I'm here for fun.", 'Expressão', 'Estou aqui para me divertir.', 'Para dizer que você veio **passear**, não trabalhar.', ["I'm here for fun, not for work.", 'Estou aqui para me divertir, não para trabalhar.']),
             EXP('🚕', 'Where to?', 'Informal', 'Para onde?', 'Pergunta do **taxista** sobre o destino.', ['Taxi! Where to?', 'Táxi! Para onde?']),
             EXP('😮‍💨', 'What a long day!', 'Expressão', 'Que dia longo!', 'Quando o dia foi **cansativo**.', ["What a long day! I'm tired.", 'Que dia longo! Estou cansado.'])],
        exp_scene=dict(rs='airport', lines=[
            L('Officer', '**First time here**?', 'Primeira vez aqui?'),
            L('Akeem', "Yes! **I'm here for fun**.", 'Sim! Estou aqui para me divertir.'),
            L('Semmi', '**What a long day**! I\'m tired.', 'Que dia longo! Estou cansado.'),
            L('Officer', 'Welcome to New York! Taxi?', 'Bem-vindos a Nova York! Táxi?'),
            L('Akeem', 'Yes, please!', 'Sim, por favor!'),
            L('Officer', '**Where to**?', 'Para onde?')]),
        lab=dict(
            short='i curto × i longo', title='Laboratório de sons: i curto × i longo',
            say='Em inglês, live e leave não soam iguais. Vamos treinar o i curto e o i longo com o Akeem.',
            intro=dict(what='O **i curto** (live, it, city) é rápido e relaxado. O **i longo** (leave, eat, he) é mais comprido, com os lábios esticados.',
                       how='No i curto, relaxe os lábios e diga um “i” bem breve e aberto. No i longo, estique os lábios num sorriso e segure o “iii”.',
                       pt='Em português só temos um “i”. Em inglês a diferença muda a palavra: **live** (morar) ≠ **leave** (sair); **ship** (navio) ≠ **sheep** (ovelha).'),
            ex=[['live', 'LÍV', 'morar', 'i curto, boca relaxada'], ['leave', 'LÍÍV', 'sair, partir', 'i longo, boca esticada'], ['city', 'SÍ-ti', 'cidade', 'primeiro i curto']],
            pairs=[['live', 'leave', '“morar” × “partir”'], ['ship', 'sheep', '“navio” × “ovelha”'], ['it', 'eat', '“isso” × “comer”']],
            tip='Sorria para o i longo (leave, eat). Relaxe a boca para o i curto (live, it).',
            phrase=['Is this city big? Yes, it is.', 'Esta cidade é grande? Sim, é.'],
            rounds=[RND('leave', ['live', 'leave'], 1, '**Leave** (sair) tem o i longo. **Live** (morar) tem o i curto.'),
                    RND('ship', ['ship', 'sheep'], 0, '**Ship** (navio) tem i curto. **Sheep** (ovelha) tem i longo.'),
                    RND('eat', ['it', 'eat'], 1, '**Eat** (comer) tem i longo. **It** tem i curto.')]),
        hunt=[HW('sheep', ['ship', 'sheep'], 1, '**sheep** = ovelha, com i longo.'),
              HP('sheep', ['🐑', '🚢', '🏙️'], 0, '**sheep** = ovelha.'),
              HW('it', ['it', 'eat'], 0, '**it** tem i curto.'),
              HP('ship', ['🐑', '🚢', '✈️'], 1, '**ship** = navio.'),
              HW('live', ['live', 'leave'], 0, '**live** = morar, com i curto.')])
    VB = dict(title='Verbos para chegar a Nova York', tip='Quatro verbos: travel, arrive, visit e come.',
              items=[VERB('travel', '🧳', 'viajar', 'I travel by plane.', 'Akeem travel**s** by plane.', 'I travel by plane.', 'Eu viajo de avião.', '**travel** = viajar. Com he/she: **travels**.'),
                     VERB('arrive', '🛬', 'chegar', 'I arrive in New York.', 'He arrive**s** in New York.', 'I arrive in New York.', 'Eu chego em Nova York.', '**arrive** = chegar. Com he/she: **arrives**.'),
                     VERB('visit', '🏙️', 'visitar', 'I visit a big city.', 'She visit**s** a big city.', 'I visit a big city.', 'Eu visito uma cidade grande.', '**visit** = visitar. Com he/she: **visits**.'),
                     VERB('come', '🚶', 'vir, ser de', 'I come from Brazil.', 'He come**s** from Zamunda.', 'I come from Brazil.', 'Eu venho do Brasil.', '**come** = vir. Com he/she: **comes**.')])
    MR = dict(
        mold=[MOLD('Perguntar de onde é', [('pergunta', [('Are you from', 'você é de')]), ('lugar', [('Brazil', 'Brasil'), ('Mexico', 'México'), ('Africa', 'África'), ('the U.S.', 'Estados Unidos'), ('New York', 'Nova York')])], ('?', '?')),
              MOLD('Responder', [('sim ou não', [('Yes, I am.', 'Sim, sou.'), ("No, I'm not.", 'Não, não sou.')]), ('de onde', [("I'm from Brazil", 'sou do Brasil'), ("I'm from Mexico", 'sou do México'), ("I'm from New York", 'sou de Nova York')])]),
              MOLD('Dar boas-vindas', [('frase', [('Welcome to', 'bem-vindo a')]), ('lugar', [('New York', 'Nova York'), ('the U.S.', 'os EUA'), ('Brazil', 'o Brasil'), ('Mexico', 'o México')])], ('!', '!'))],
        speak=[["First time here? I'm here for fun.", 'Primeira vez aqui? Estou aqui para me divertir.'], ['Where to? What a long day!', 'Para onde? Que dia longo!']],
        trap=[TRM('“First time here?” quer dizer…', ['Primeira vez aqui?', 'Primeiro dia de trabalho?', 'Hora de ir?'], 0, '**First time here?** = primeira vez aqui?', 'First time here?'),
              TRM('Qual frase está certa?', ['What long a day!', 'What a long day!', 'What day long a!'], 1, 'A ordem é **What a long day!**', 'What a long day!')],
        gap=[GPM("I'm here ___ fun.", 'Estou aqui para me divertir.', ['for', 'to', 'at'], 0, 'A expressão é **here for fun**.', "I'm here for fun."),
             GPM('___ to?', 'Para onde?', ['How', 'Where', 'What'], 1, 'A pergunta é **Where to?**', 'Where to?')],
        expq=[EQ('O taxista pergunta o destino.', ['First time here?', 'What a long day!', 'Where to?'], 2, '**Where to?** = para onde?'),
              EQ('Você chegou cansado depois de uma viagem longa.', ['What a long day!', 'Where to?', "I'm here for fun."], 0, '**What a long day!** = que dia longo!'),
              EQ('Perguntam por que você está na cidade e é passeio.', ['What a long day!', "I'm here for fun.", 'Where to?'], 1, '**I\'m here for fun.** = vim passear.')],
        missions=[MIS('🛂', 'No aeroporto', 'Diga de onde você é e por que está ali.',
                      prompt='Você chega a Nova York e o policial pergunta de onde você é. **Diga de onde você é, por que está ali e faça uma pergunta com Are you from…? para ele.**',
                      ph='Escreva a sua resposta aqui…', chips=["I'm from…"],
                      model="I'm from Brazil. I'm here for fun. Are you from New York?",
                      check=['Disse de onde sou com I’m from…?', 'Disse por que estou aqui?', 'Fiz uma pergunta com Are you from…?'],
                      kw=[r"\bi['’]m from\s+\w+", r"\bi['’]m here for\s+\w+", r"\bare you from\b[^.!?]*\?"],
                      tips=[[["I'm from Brazil.", 'Eu sou do Brasil.']], [["I'm here for fun.", 'Estou aqui para me divertir.']], [['Are you from New York?', 'Você é de Nova York?']]],
                      ok=['De onde eu sou! 🌎', 'Motivo da viagem! ✈️', 'Boa pergunta! ❓'], reply=['Welcome to New York! Have fun!', 'Bem-vindo a Nova York! Divirta-se!']),
                  MIS('🚕', 'Amigo chegando', 'Use as expressões do episódio.',
                      prompt='Um amigo chega do aeroporto. **Pergunte se é a primeira vez dele aqui, diga que o dia foi longo e pergunte para onde ele vai.**',
                      ph='Escreva a sua resposta aqui…', chips=['First time here?'],
                      model='First time here? What a long day! Where to?',
                      check=['Perguntei se é a primeira vez?', 'Disse que o dia foi longo?', 'Perguntei para onde vai?'],
                      kw=[r'\bfirst time here\b', r'\bwhat a long day\b', r'\bwhere to\b'],
                      tips=[[['First time here?', 'Primeira vez aqui?']], [['What a long day!', 'Que dia longo!']], [['Where to?', 'Para onde?']]],
                      ok=['Primeira vez! ❓', 'Dia longo! 😮‍💨', 'Destino! 🚕'], reply=['Yes! To the hotel, please.', 'Sim! Para o hotel, por favor.'])])
    CX = [CXF('Brazil, Mexico and Peru are in America. Each one is a ___.', 'Brasil, México e Peru ficam na América. Cada um é um país.', ['country', 'plane', 'city']),
          CXF('São Paulo, Chicago and Mexico City are big. Each one is a ___.', 'São Paulo, Chicago e Cidade do México são grandes. Cada uma é uma cidade.', ['city', 'country', 'plane']),
          CXF('It flies in the sky and takes people to other countries. It is a ___.', 'Ele voa no céu e leva as pessoas a outros países. É um avião.', ['plane', 'city', 'Brazil']),
          CXF('Samba, soccer and Rio de Janeiro: this is ___.', 'Samba, futebol e Rio de Janeiro: este é o Brasil.', ['Brazil', 'Mexico', 'Africa']),
          CXF('Tacos and tequila are famous in ___.', 'Tacos e tequila são famosos no México.', ['Mexico', 'Africa', 'Brazil']),
          CXF('Elephants and lions live in big savannas in ___.', 'Elefantes e leões vivem nas grandes savanas da África.', ['Africa', 'Brazil', 'Mexico'])]
    return ep(B, X, XT, VB, MR, CX)


# ======================================================================
# POS 9 · n=70003 · Gulliver's Travels · Are you a…? (hotel)
# ======================================================================
GULLIVER = 'p:short:6b4423:f4c7a1:1f3a5f:none:suit'
CLERK = 'p:short:2a2a2a:f4c7a1:b03a2e:bow:suit'
PIP = 'p:curly:8b5a2b:e8b48a:27ae60:none:shirt'


def ep9():
    B = dict(
        title="Enjoy Your Stay · Are you a…?",
        sub="Perguntar com Are you a…? em um hotel: a guest, a giant, an artist",
        pattern_label="Are you a…?",
        why="Hoje você faz perguntas com Are you a…? e Are you from…?, como na recepção do hotel onde o Gulliver chega: Are you a guest? Are you a giant?",
        vocab=VOC(('Hotel', 'Hotel', 'rou-TÉL'), ('Luggage', 'Bagagem', 'LÂ-guij'), ('Guest', 'Hóspede', 'GÉST'), ('Giant', 'Gigante', 'DJÁI-ant'),
                  ('Tiny', 'Minúsculo(a)', 'TÁI-ni'), ('Japan', 'Japão', 'dja-PÉN'), ('France', 'França', 'FRÉNS')),
        balloons=BAL(('🏨', 'hotel'), ('🧳', 'luggage'), ('🛎️', 'guest'), ('🧌', 'giant'), ('🐜', 'tiny'), ('🇯🇵', 'Japan'), ('🇫🇷', 'France')),
        cover_art={'s': 'lobby', 'items': [['🏨', 100, 56, 20, 'bob'], ['🧳', 138, 44, 12, 'bob'], ['🛎️', 84, 34, 12, 'bob']], 'seed': 'gu1'},
        cover_sub='Are you a…? Em 10 minutos você conversa na recepção de um hotel',
        cover_say='O Gulliver chega a um hotel de gente minúscula! O recepcionista faz perguntas. Como perguntar e responder?',
        wrap_recap=[['Are you a guest?', 'Você é hóspede?'], ['Are you a giant?', 'Você é um gigante?'],
                    ['Are you from France?', 'Você é da França?'], ['Enjoy your stay!', 'Aproveite a estadia!']],
        teaser={'t': 'Rip Van Winkle', 'd': 'Próximo padrão: Are you…? com fome, sede, frio e sono'},
        cast={'Gulliver': ['🧔', '#1f3a5f'], 'Clerk': ['🛎️', '#b03a2e'], 'Pip': ['🧒', '#27ae60']},
        lines=[L('Clerk', 'Welcome to the hotel! Are you a guest?', 'Bem-vindo ao hotel! O senhor é hóspede?'),
               L('Gulliver', "Yes, I am. I'm Gulliver.", 'Sim, sou. Eu sou o Gulliver.'),
               L('Pip', 'Wow! Are you a giant?', 'Uau! Você é um gigante?'),
               L('Gulliver', "No, I'm not. You are tiny!", 'Não, não sou. Vocês é que são minúsculos!'),
               L('Clerk', 'Are you from France?', 'O senhor é da França?'),
               L('Gulliver', "No, I'm not. I'm from England.", 'Não, não sou. Eu sou da Inglaterra.'),
               L('Clerk', 'Are you tired? Enjoy your stay!', 'O senhor está cansado? Aproveite a estadia!'),
               L('Gulliver', 'Yes, I am. Thank you!', 'Sim, estou. Obrigado!')],
        quiz=[QZ('Where is Gulliver from?', 'De onde o Gulliver é?', [('🇫🇷', 'France'), ('🇬🇧', 'England'), ('🇯🇵', 'Japan')], 1, 5, 'Gulliver diz: “I’m from England.”'),
              QZ('Is Gulliver tired?', 'O Gulliver está cansado?', [('😴', 'Yes, he is'), ('😀', "No, he isn't"), ('🤷', 'Maybe')], 0, 7, 'Gulliver diz: “Yes, I am.”'),
              QZ('Who asks: “Are you a giant?”', 'Quem pergunta: “Are you a giant?”', [('🛎️', 'The clerk'), ('🧔', 'Gulliver'), ('🧒', 'Pip')], 2, 2, 'O Pip pergunta: “Are you a giant?”')],
        rdg_q={'q': 'Como perguntar “Você é um hóspede?”', 'o': ['Are you guest?', 'Are you a guest?', 'You are a guest?'], 'a': 1,
               'why': 'Faltou o **a**: com um papel, use **Are you a** + papel?'},
        dictate=[['Are you a guest?', 'Você é hóspede?'], ["No, I'm not.", 'Não, não sou.'],
                 ['Are you from France?', 'Você é da França?'], ['Enjoy your stay!', 'Aproveite a estadia!']],
        produce=PROD('O recepcionista pergunta: *Are you a guest? Are you tired?* **Responda com Yes, I am ou No, I\'m not, diga quem você é com I\'m a… e faça uma pergunta com Are you…?**',
                     "Ex.: Yes, I am. I'm a guest. Are you tired?",
                     ['Yes, I am.', "I'm a guest.", 'Are you…?'],
                     "Yes, I am. I'm a guest. Are you tired?",
                     ['Respondi com Yes, I am ou No, I’m not?', 'Disse quem sou com I’m a…?', 'Fiz uma pergunta com Are you…?'],
                     [r"\b(?:yes,?\s*i am|no,?\s*i(?:['’]m| am) not)\b", r"\bi['’]m an?\s+\w+", r"\bare you\b[^.!?]*\?"],
                     [[['Yes, I am.', 'Sim, sou.'], ["No, I'm not.", 'Não, não sou.']],
                      [["I'm a guest.", 'Eu sou hóspede.'], ["I'm a student.", 'Eu sou estudante.']],
                      [['Are you tired?', 'Você está cansado?'], ['Are you from Italy?', 'Você é da Itália?']]],
                     ['Resposta curta! ✅', 'Quem eu sou! 🙋', 'Boa pergunta! ❓'],
                     ['Welcome! Here is your room. Enjoy your stay!', 'Bem-vindo! Aqui está o seu quarto. Aproveite a estadia!']),
        rs=RS('lobby', 'lobby1', 'lobby2', 'hall', 'airport', 'counter', 'diner', 'school', 'lobby1', 'bedroom', 'street'),
        sc='lobby')
    X = dict(
        n=70003, review=True, names=('Gulliver', 'Clerk'),
        stage=dict(rs='lobby', chars=[[GULLIVER, 26, 0, 1.05], [CLERK, 60, 1, 0.65], [PIP, 84, 1, 0.55]]),
        obra=dict(name="Gulliver's Travels", kind='📖 Romance de viagens · 1726', year='1726',
                  text='Romance do escritor irlandês Jonathan Swift, publicado em 1726. O inglês Lemuel Gulliver viaja por terras incríveis, como Lilliput, onde as pessoas são minúsculas. No livro, ele até visita o Japão.',
                  line=['Lilliput', 'Lilliput. A ilha das pessoas minúsculas.'],
                  pa=dict(t='ship', e=['⛵', '🏝️', '🧍'], p='d', v=1)),
        gancho=['Clerk', 'Welcome to the hotel! Are you a guest?', 'Bem-vindo ao hotel! O senhor é hóspede?'],
        hot=[HOT('🏨', 14, 16, 'hotel', 'hotel', 'Is it a hotel? Are you a guest?', 'É um hotel? Você é hóspede?'),
             HOT('🧳', 40, 14, 'luggage', 'bagagem', 'Is this your luggage? It is big!', 'Esta é a sua bagagem? Ela é grande!'),
             HOT('🐜', 66, 14, 'tiny', 'minúsculo', 'Are you tiny? Yes, I am.', 'Você é minúsculo? Sim, sou.'),
             HOT('🇯🇵', 88, 16, 'Japan', 'Japão', 'Are you from Japan?', 'Você é do Japão?'),
             HOT('🇫🇷', 12, 82, 'France', 'França', 'Are you from France?', 'Você é da França?')],
        gap=[GAP('___ you a guest?', 'Você é hóspede?', ['Is', 'Are', 'Do'], 1, 'Com **you**, use **Are**: Are you a guest?'),
             GAP('Are you ___ giant?', 'Você é um gigante?', ['a', 'an', 'the'], 0, 'Antes de **giant** (som de “dj”) use **a**.'),
             GAP('Are you ___ artist?', 'Você é um artista?', ['a', 'the', 'an'], 2, 'Antes de som de vogal (**artist**), use **an**.'),
             GAP('No, I\'m ___.', 'Não, não sou.', ['no', 'not', "don't"], 1, 'A resposta curta negativa é **No, I\'m not.**')],
        trap=[TRAP(['Are you guest?', 'Are you a guest?', 'You a guest?'], 1, 'Com um papel, não esqueça o **a**: Are you **a** guest?'),
              TRAP(['Are you an giant?', 'Are you a giant?', 'Do you a giant?'], 1, '**giant** começa com som de “dj” (consoante): use **a**.')],
        sticker=dict(title='Gulliver no hotel', sub="Gulliver's Travels · 1726", rs='lobby', chars=[[GULLIVER, 36, 0, 1.0], [CLERK, 70, 1, 0.65]]),
        speakers={'Gulliver': GULLIVER, 'Clerk': CLERK, 'Pip': PIP},
        rule=dict(
            who=CLERK, head='Are you a…?', sub='Perguntar quem você é.',
            say=['Are you a guest?', 'Você é hóspede?'],
            formula=[dict(from_=[['You', 0], ['are', 1], ['a guest.', 2]], to=[['Are', 1], ['you', 0], ['a guest?', 2]], say='Are you a guest?', note='O verbo **are** vem antes de **you**. O **a** fica antes do papel.'),
                     dict(from_=[['You', 0], ['are', 1], ['an artist.', 2]], to=[['Are', 1], ['you', 0], ['an artist?', 2]], say='Are you an artist?', note='Antes de som de vogal, use **an**: an artist, an uncle.')],
            uses=[dict(ico='🛎️', tag='Papel', en='Are you a guest?', pt='Você é hóspede?'),
                  dict(ico='🧌', tag='Papel', en='Are you a giant?', pt='Você é um gigante?'),
                  dict(ico='🇫🇷', tag='Origem', en='Are you from France?', pt='Você é da França?'),
                  dict(ico='✅', tag='Resposta', en='Yes, I am. / No, I\'m not.', pt='Sim, sou. / Não, não sou.')],
            rules=[dict(tag='Are you a', c=0, text='Para perguntar o **papel**: Are you **a** + papel?', ex='Are you a guest?'),
                   dict(tag='a / an', c=1, text='**a** antes de som de consoante, **an** antes de som de vogal.', ex='a giant · an artist'),
                   dict(tag='Yes, I am', c=2, text='Resposta curta: **Yes, I am.** (sem contrair) ou **No, I\'m not.**', ex="No, I'm not.")],
            tips=['Em português “você é hóspede?” não leva artigo. Em inglês, o **a** é obrigatório: Are you **a** guest?']),
        mission_ic='🏨')
    XT = dict(
        exp=[EXP('🎉', 'Enjoy your stay!', 'Expressão', 'Aproveite a estadia!', 'O que o hotel diz ao **hóspede** na chegada.', ['Welcome! Enjoy your stay!', 'Bem-vindo! Aproveite a estadia!']),
             EXP('🤲', 'Here you go.', 'Expressão', 'Aqui está.', 'Quando você **entrega** algo a alguém.', ["Here you go. That's your room.", 'Aqui está. Esse é o seu quarto.']),
             EXP('✈️', 'How was your flight?', 'Expressão', 'Como foi o voo?', 'Pergunta simpática a quem **acabou de chegar de avião**.', ['Hello, Gulliver! How was your flight?', 'Olá, Gulliver! Como foi o voo?']),
             EXP('👌', 'No problem!', 'Informal', 'Sem problema!', 'Resposta quando alguém **agradece** ou pede desculpa por algo pequeno.', ["I'm sorry. No problem!", 'Desculpe. Sem problema!'])],
        exp_scene=dict(rs='lobby1', lines=[
            L('Clerk', 'Good evening! **How was your flight**?', 'Boa noite! Como foi o voo?'),
            L('Gulliver', 'Very long! I\'m tired.', 'Muito longo! Estou cansado.'),
            L('Clerk', '**Here you go**. This is your room.', 'Aqui está. Este é o seu quarto.'),
            L('Gulliver', 'Thank you! My luggage is big. Is that a problem?', 'Obrigado! Minha bagagem é grande. Isso é um problema?'),
            L('Pip', '**No problem**! We help.', 'Sem problema! Nós ajudamos.'),
            L('Clerk', '**Enjoy your stay**, Gulliver!', 'Aproveite a estadia, Gulliver!')]),
        lab=dict(
            short='h inicial', title='Laboratório de sons: o h de hotel',
            say='Em inglês o h é pronunciado: um sopro de ar. Vamos treinar com o hotel do Gulliver.',
            intro=dict(what='O **h** inicial de **hotel**, **hi** e **help** é só um sopro de ar, como quando você bafeja num vidro.',
                       how='Abra a boca e solte o ar sem raspar a garganta. Não faça o “r” forte do português. Ponha a mão na frente da boca e sinta o ar quente.',
                       pt='Em português o h é mudo (hotel = “otel”). Em inglês, sem o h a palavra muda: **hat** (chapéu) ≠ **at** (em); **his** (dele) ≠ **is** (é).'),
            ex=[['hotel', 'rou-TÉL', 'hotel', 'comece com um sopro de ar'], ['hi', 'HÁI', 'oi', 'sopro e depois “ai”'], ['help', 'HÉLP', 'ajuda', 'sopro, sem raspar a garganta']],
            pairs=[['hat', 'at', 'hat: com sopro · at: sem sopro'], ['hear', 'ear', '“ouvir” × “orelha”'], ['his', 'is', '“dele” × “é”']],
            tip='Mão na frente da boca: no h você sente o ar quente; no a, no e ou no i sem h, não.',
            phrase=['Hi! Are you at the hotel?', 'Oi! Você está no hotel?'],
            rounds=[RND('hat', ['hat', 'at'], 0, '**Hat** (chapéu) começa com o sopro do h. **At** não tem sopro.'),
                    RND('ear', ['hear', 'ear'], 1, '**Ear** (orelha) começa direto na vogal. **Hear** (ouvir) tem o sopro.'),
                    RND('is', ['is', 'his'], 0, '**Is** (é) não tem sopro. **His** (dele) começa com o h.')]),
        hunt=[HW('hear', ['hear', 'ear'], 0, '**hear** = ouvir, com o sopro do h.'),
              HP('hotel', ['🎩', '🏨', '🦻'], 1, '**hotel** = hotel.'),
              HW('at', ['hat', 'at'], 1, '**at** = em, sem o h.'),
              HP('hat', ['🎩', '🏨', '🦻'], 0, '**hat** = chapéu.'),
              HW('his', ['his', 'is'], 0, '**his** = dele, com o sopro do h.')])
    VB = dict(title='Verbos para o hotel', tip='Quatro verbos: stay, fly, enjoy e wait.',
              items=[VERB('stay', '🛏️', 'ficar, hospedar-se', 'I stay at a hotel.', 'Gulliver stay**s** at a hotel.', 'I stay at a hotel.', 'Eu fico em um hotel.', '**stay** = ficar. Com he/she: **stays**.'),
                     VERB('fly', '✈️', 'voar', 'I fly to Japan.', 'She fl**ies** to Japan.', 'I fly to Japan.', 'Eu voo para o Japão.', '**fly** = voar. Com he/she: **flies** (y → ies).'),
                     VERB('enjoy', '😊', 'curtir, aproveitar', 'I enjoy the hotel.', 'He enjoy**s** the hotel.', 'I enjoy the hotel.', 'Eu curto o hotel.', '**enjoy** = aproveitar. Com he/she: **enjoys**.'),
                     VERB('wait', '⏳', 'esperar', 'I wait here.', 'Pip wait**s** at the desk.', 'I wait here.', 'Eu espero aqui.', '**wait** = esperar. Com he/she: **waits**.')])
    MR = dict(
        mold=[MOLD('Are you a…?', [('pergunta', [('Are you', 'você é')]), ('papel', [('a guest', 'hóspede'), ('a giant', 'um gigante'), ('a student', 'estudante'), ('an artist', 'um artista'), ('a teacher', 'professor(a)')])], ('?', '?')),
              MOLD('Are you from…?', [('pergunta', [('Are you from', 'você é de')]), ('lugar', [('France', 'França'), ('Japan', 'Japão'), ('Italy', 'Itália'), ('England', 'Inglaterra'), ('Brazil', 'Brasil')])], ('?', '?')),
              MOLD('Dar boas-vindas', [('frase', [('Welcome to', 'bem-vindo a')]), ('lugar', [('the hotel', 'o hotel'), ('Italy', 'a Itália'), ('Japan', 'o Japão'), ('France', 'a França')])], ('!', '!'))],
        speak=[['Here you go. Enjoy your stay!', 'Aqui está. Aproveite a estadia!'], ['No problem! Are you tired?', 'Sem problema! Você está cansado?']],
        trap=[TRM('“Here you go” é dito quando você…', ['entrega algo a alguém', 'pede o caminho', 'se despede'], 0, '**Here you go.** = aqui está (ao entregar algo).', 'Here you go.'),
              TRM('Qual frase está certa?', ['Enjoy you stay!', 'Enjoy your stay!', 'Enjoy yours stay!'], 1, 'Use **your**: Enjoy **your** stay!', 'Enjoy your stay!')],
        gap=[GPM('Here you ___.', 'Aqui está.', ['go', 'come', 'do'], 0, 'A expressão é **Here you go.**', 'Here you go.'),
             GPM('___ was your flight?', 'Como foi o voo?', ['What', 'How', 'Where'], 1, 'A pergunta é **How was your flight?**', 'How was your flight?')],
        expq=[EQ('Você entrega algo a alguém. O que diz?', ['No problem!', 'Here you go.', 'Enjoy your stay!'], 1, '**Here you go.** = aqui está.'),
              EQ('Um hóspede acaba de chegar. O recepcionista deseja…', ['Enjoy your stay!', 'Here you go.', 'No problem!'], 0, '**Enjoy your stay!** = aproveite a estadia!'),
              EQ('Um amigo chega de viagem. O que você pergunta?', ['No problem!', 'Here you go.', 'How was your flight?'], 2, '**How was your flight?** = como foi o voo?')],
        missions=[MIS('🏨', 'Check-in', 'Responda ao recepcionista com Are you…?',
                      prompt='O recepcionista pergunta: *Are you a guest? Are you tired?* **Responda com Yes, I am ou No, I\'m not, diga quem você é com I\'m a… e faça uma pergunta com Are you…? a ele.**',
                      ph='Escreva a sua resposta aqui…', chips=['Yes, I am.'],
                      model="Yes, I am. I'm a guest. Are you tired?",
                      check=['Usei a resposta curta?', 'Disse quem sou com I’m a…?', 'Fiz uma pergunta com Are you…?'],
                      kw=[r"\b(?:yes,?\s*i am|no,?\s*i(?:['’]m| am) not)\b", r"\bi['’]m an?\s+\w+", r"\bare you\b[^.!?]*\?"],
                      tips=[[['Yes, I am.', 'Sim, sou.']], [["I'm a guest.", 'Eu sou hóspede.']], [['Are you tired?', 'Você está cansado?']]],
                      ok=['Resposta curta! ✅', 'Quem eu sou! 🙋', 'Boa pergunta! ❓'], reply=['Yes, I am. Here is your room!', 'Sim, estou. Aqui está o seu quarto!']),
                  MIS('🧳', 'Amigo no hotel', 'Use as expressões do episódio.',
                      prompt='Um amigo chega ao hotel. **Pergunte como foi o voo dele, diga "aqui está" ao entregar a bagagem e deseje uma boa estadia.**',
                      ph='Escreva a sua resposta aqui…', chips=['How was your flight?'],
                      model='How was your flight? Here you go. Enjoy your stay!',
                      check=['Perguntei sobre o voo?', 'Disse aqui está?', 'Desejei boa estadia?'],
                      kw=[r'\bhow was your flight\b', r'\bhere you go\b', r'\benjoy your stay\b'],
                      tips=[[['How was your flight?', 'Como foi o voo?']], [['Here you go.', 'Aqui está.']], [['Enjoy your stay!', 'Aproveite a estadia!']]],
                      ok=['Voo! ✈️', 'Bagagem! 🧳', 'Boa estadia! 🏨'], reply=['Thank you! No problem at all.', 'Obrigado! Sem problema nenhum.'])])
    CX = [CXF('You sleep here when you travel. You pay for a room. It is a ___.', 'Você dorme aqui quando viaja. Paga por um quarto. É um hotel.', ['hotel', 'luggage', 'giant']),
          CXF('I carry my clothes in a big bag. It is my ___.', 'Eu levo minhas roupas em uma mala grande. É a minha bagagem.', ['luggage', 'hotel', 'guest']),
          CXF('He is very, very big and strong. He is a ___.', 'Ele é muito, muito grande e forte. Ele é um gigante.', ['giant', 'guest', 'hotel']),
          CXF('An ant is very, very small. It is ___.', 'Uma formiga é muito, muito pequena. Ela é minúscula.', ['tiny', 'giant', 'Japan']),
          CXF('A person who sleeps at a hotel is a ___.', 'Uma pessoa que dorme em um hotel é um hóspede.', ['guest', 'giant', 'luggage']),
          CXF('Tokyo is the capital of ___.', 'Tóquio é a capital do Japão.', ['Japan', 'France', 'tiny'])]
    return ep(B, X, XT, VB, MR, CX)
