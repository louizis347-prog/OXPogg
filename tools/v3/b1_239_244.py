# B1 · episódios 239–244: both/either/neither, so/such, too/enough.
from v3.b1h import *

EPS = []

def mk(n, title, sub, pat, why, names, ids, rs, obra, scenes, cover, teaser, rule, fm, vocab, lab, verbs, mold, prod, m2, hot, gaps, traps, lines, quiz, exps):
    return S(n=n, title=title, sub=sub, pattern=pat, why=why, names=names, ids=ids, rs=rs, obra=(obra, obra),
             hot=hot, gaps=gaps, traps=traps, rule=rule, fm=fm, cover=cover, vocab=vocab, lines=lines, quiz=quiz,
             teaser=teaser, exps=exps, lab=lab, verbs=verbs, mold=mold, prod=prod, m2=m2, scenes=scenes)

# ---------- both / either / neither ----------
BE_VOCAB = [('👯', 'both', 'ambos', 'Soa como “BÔUTH”.'), ('🔀', 'either', 'um ou outro', 'Soa como “Á-dher”.'), ('🚫', 'neither', 'nenhum', 'Soa como “NÁ-dher”.'),
            ('👬', 'twins', 'gêmeos', 'Soa como “TUÍNZ”.'), ('🪇', 'rattle', 'chocalho', 'Soa como “RÉ-tol”.'), ('🟰', 'alike', 'iguais', 'Soa como “a-LÁIK”.')]
BE_LAB = dict(short='bo', title='Laboratório de sons: both, either e twins', pt='o soa ôu; ei soa ai; w soa u.', tip='Em both, o th soa com a língua entre os dentes.',
              words=[('both', 'BÔUTH', 'ambos', 'o = ôu', 'bath', 'BÉTH'), ('either', 'Á-dher', 'um ou outro', 'ei = ai', 'ether', 'I-ther'), ('twins', 'TUÍNZ', 'gêmeos', 'tw = tu', 'tins', 'TÍNZ')])
BE_VERBS = [('be', '👯', 'ser', 'Both are friendly.', 'Both is friendly.', 'I am.', 'Eu sou.', 'both + **are**.'),
            ('like', '❤️', 'gostar', 'I like both.', 'I likes both.', 'I like.', 'Eu gosto.', 'I **like**.'),
            ('choose', '🔀', 'escolher', 'Choose either one.', 'Choose neither one.', 'I choose.', 'Eu escolho.', 'either **one**.'),
            ('know', '🧠', 'saber', 'Neither knows.', 'Neither know not.', 'I know.', 'Eu sei.', 'Neither **knows**.')]
BE_MOLD = [('Both… and', 'Both', 'ambos', [(' Dum and Dee are friendly.', ' Dum e Dee são amigáveis.'), (' Anna and Tom are tall.', ' Anna e Tom são altos.'), (' tea and coffee are hot.', ' chá e café estão quentes.')]),
           ('Either… or', 'Either', 'ou', [(' Dum or Dee will come.', ' Dum ou Dee virá.'), (' you or I will go.', ' você ou eu iremos.'), (' tea or coffee is fine.', ' chá ou café serve.')]),
           ('Neither… nor', 'Neither', 'nem', [(' Dum nor Dee is late.', ' Dum nem Dee está atrasado.'), (' he nor she knows.', ' nem ele nem ela sabe.'), (' tea nor coffee is cold.', ' nem chá nem café está frio.')])]
BE_RULE = ('Both, either, neither', 'Par de palavras que liga dois itens.', 'Em português “ambos… e”. Em inglês: **both… and**.')
BE_FM = [('Both', 'Both Dum', 'and Dee are friendly.', 'Both Dum and Dee are friendly.', 'both + and.'), ('Either', 'Either Dum', 'or Dee will come.', 'Either Dum or Dee will come.', 'either + or.')]
BE_TRAPS = [('Qual frase está certa?', ['Both Dum and Dee are friendly.', 'Both Dum or Dee are friendly.', 'Both Dum and Dee is friendly.'], 0, 'both + and.'),
            ('Qual está certa?', ['Neither Dum nor Dee is late.', 'Neither Dum or Dee is late.', 'Neither Dum nor Dee is not late.'], 0, 'neither + nor.')]

EPS.append(mk(82157, 'Both… And', "usar both…and, either…or e neither…nor (twins, rattle, alike)",
    "pares: both…and · either…or · neither…nor", "Hoje você aprende três pares: Both Dum and Dee are friendly. Either Dum or Dee will come. Neither is late.",
    ('Woman', 'Man'), ['polly', 'tom'], 'cafe2', 'Tweedledum and Tweedledee', ['cafe2', 'park', 'living', 'street', 'hall', 'school'],
    ('Both… And: em 10 minutos você liga dois itens como um nativo', 'No café, a mulher e o homem falam de dois gêmeos idênticos.'), ('Mais pares', 'Próximo: Both, either, neither'),
    BE_RULE, BE_FM, BE_VOCAB, BE_LAB, BE_VERBS, BE_MOLD,
    ('👯', 'Pares', 'Use both and, either or e neither nor', 'Fale. **Diga ambos Dum e Dee são amigáveis, um ou outro virá e nenhum está atrasado.**', 'neither nor', 'Both Dum and Dee are friendly. Either Dum or Dee will come. Neither Dum nor Dee is late.',
     [('Usei both and?', r"\bboth\s+\w+\s+and\s+\w+\b", 'Both Dum and Dee are friendly.', 'Ambos, Dum e Dee, são amigáveis.', 'Both! 👯'), ('Usei either or?', r"\beither\s+\w+\s+or\s+\w+\b", 'Either Dum or Dee will come.', 'Dum ou Dee virá.', 'Either! 🔀'), ('Usei neither nor?', r"\bneither\s+\w+\s+nor\s+\w+\b", 'Neither Dum nor Dee is late.', 'Nem Dum nem Dee está atrasado.', 'Neither! 🚫')]),
    ('🟰', 'Fixas', 'Use either way, on both sides e neither here nor there', 'Fale. **Diga de qualquer jeito, dos dois lados e sem importância.**', 'either way', 'Either way, I win. They sit on both sides. It is neither here nor there.',
     [('Disse either way?', r"\beither\s+way\b", 'Either way, I win.', 'De qualquer jeito, eu ganho.', 'Way! 🔀'), ('Disse on both sides?', r"\bon\s+both\s+sides\b", 'They sit on both sides.', 'Eles sentam dos dois lados.', 'Sides! 👯'), ('Disse neither here nor there?', r"\bneither\s+here\s+nor\s+there\b", 'It is neither here nor there.', 'Isso não importa.', 'There! 🚫')]),
    [('👯', 'Both…and', 'ambos…e', 'Both Dum and Dee are friendly.', 'Ambos, Dum e Dee, são amigáveis.'), ('🔀', 'Either…or', 'um ou outro', 'Either Dum or Dee will come.', 'Dum ou Dee virá.'),
     ('🚫', 'Neither…nor', 'nem…nem', 'Neither Dum nor Dee is late.', 'Nem Dum nem Dee está atrasado.'), ('👬', 'twins', 'gêmeos', 'They are twins.', 'Eles são gêmeos.'), ('🟰', 'alike', 'iguais', 'They look alike.', 'Eles são parecidos.')],
    [('___ Dum and Dee are friendly.', 'Ambos, Dum e Dee, são amigáveis.', ['Both', 'Either', 'Neither'], 0, '**Both**… and'), ('Either Dum ___ Dee will come.', 'Dum ou Dee virá.', ['or', 'and', 'nor'], 0, 'either… **or**'),
     ('Neither Dum ___ Dee is late.', 'Nem Dum nem Dee está atrasado.', ['nor', 'or', 'and'], 0, 'neither… **nor**'), ('They are ___.', 'Eles são gêmeos.', ['twins', 'twin is', 'twining'], 0, 'they are **twins**.')],
    BE_TRAPS,
    [['Woman', 'Do you know the twins?', 'Você conhece os gêmeos?'], ['Man', 'Yes. Both Dum and Dee are friendly.', 'Sim. Ambos, Dum e Dee, são amigáveis.'], ['Woman', 'Will they come today?', 'Eles virão hoje?'], ['Man', 'Either Dum or Dee will come.', 'Dum ou Dee virá.'],
     ['Woman', 'Are they late?', 'Estão atrasados?'], ['Man', 'Neither Dum nor Dee is late.', 'Nem Dum nem Dee está atrasado.'], ['Woman', 'They look alike!', 'Eles são parecidos!'], ['Man', 'Yes, they are twins.', 'Sim, são gêmeos.']],
    [('Are they friendly?', 'Eles são amigáveis?', [('😊', 'Yes, both'), ('😠', 'No'), ('🤷', 'Unknown')], 0, 1, 'Diz: “Both… are friendly.”'), ('Who will come?', 'Quem virá?', [('🔀', 'Dum or Dee'), ('👥', 'Everybody'), ('🚫', 'Nobody')], 0, 3, 'Diz: “Either Dum or Dee.”'),
     ('Is anyone late?', 'Alguém está atrasado?', [('✅', 'No one'), ('⏰', 'Dum'), ('🕐', 'Dee')], 0, 5, 'Diz: “Neither… is late.”')],
    [('🔀', 'Either way', 'De qualquer jeito', 'tanto faz', 'Either way, I win.', 'De qualquer jeito, eu ganho.'), ('👯', 'Both sides', 'Os dois lados', 'ambos', 'They sit on both sides.', 'Eles sentam dos dois lados.'),
     ('🚫', 'Neither here nor there', 'Sem importância', 'irrelevante', 'It is neither here nor there.', 'Isso não importa.'), ('🟰', 'Two of a kind', 'Farinha do mesmo saco', 'iguais', 'They are two of a kind.', 'Eles são farinha do mesmo saco.')]))

EPS.append(mk(7082157, 'Both, either, neither', "both, either e neither sozinhos e com of (twins, rattle, alike)",
    "sozinhos e com of: both of · either of · neither of", "Hoje você usa both, either e neither com of: Both of them are kind. Either of them can come. Neither of them is late.",
    ('Girl', 'Boy'), ['polly', 'tommy'], 'park', 'Tweedledum and Tweedledee', ['park', 'yard', 'school', 'lake', 'street', 'home1'],
    ('Both, either, neither: em 10 minutos você fala de dois sem repetir nomes', 'No parque, a menina e o menino falam de dois amigos.'), ('Mais pares', 'Próximo: Tão e tal'),
    ('Both of', 'Both, either e neither + of them.', 'Em português “os dois”. Em inglês: **both of them**.'),
    [('Both of', 'Both of', 'them are kind.', 'Both of them are kind.', 'both of them + are.'), ('Neither of', 'Neither of', 'them is late.', 'Neither of them is late.', 'neither of them + is.')],
    BE_VOCAB, BE_LAB, BE_VERBS, [('Both of', 'Both of them', 'os dois', [(' are kind.', ' são gentis.'), (' like tea.', ' gostam de chá.'), (' are here.', ' estão aqui.')]), ('Either of', 'Either of them', 'qualquer um deles', [(' can come.', ' pode vir.'), (' can help.', ' pode ajudar.'), (' knows.', ' sabe.')]), ('Neither of', 'Neither of them', 'nenhum deles', [(' is late.', ' está atrasado.'), (' is sad.', ' está triste.'), (' is here.', ' está aqui.')])],
    ('👯', 'Com of', 'Use both of them, either of them e neither of them', 'Fale. **Diga os dois são gentis, qualquer um pode vir e nenhum está atrasado.**', 'either of them', 'Both of them are kind. Either of them can come. Neither of them is late.',
     [('Usei both of them?', r"\bboth\s+of\s+them\b", 'Both of them are kind.', 'Os dois são gentis.', 'Both! 👯'), ('Usei either of them?', r"\beither\s+of\s+them\b", 'Either of them can come.', 'Qualquer um pode vir.', 'Either! 🔀'), ('Usei neither of them?', r"\bneither\s+of\s+them\b", 'Neither of them is late.', 'Nenhum deles está atrasado.', 'Neither! 🚫')]),
    ('🟰', 'Fixas', 'Use both ways, either side e neither of us', 'Fale. **Diga dos dois jeitos, de qualquer lado e nenhum de nós.**', 'neither of us', 'It works both ways. Park on either side. Neither of us knows.',
     [('Disse both ways?', r"\bboth\s+ways\b", 'It works both ways.', 'Funciona dos dois jeitos.', 'Ways! 👯'), ('Disse either side?', r"\beither\s+side\b", 'Park on either side.', 'Estacione de qualquer lado.', 'Side! 🔀'), ('Disse neither of us?', r"\bneither\s+of\s+us\b", 'Neither of us knows.', 'Nenhum de nós sabe.', 'Us! 🚫')]),
    [('👯', 'Both of them', 'os dois', 'Both of them are kind.', 'Os dois são gentis.'), ('🔀', 'Either of them', 'qualquer um deles', 'Either of them can come.', 'Qualquer um pode vir.'),
     ('🚫', 'Neither of them', 'nenhum deles', 'Neither of them is late.', 'Nenhum deles está atrasado.'), ('🪇', 'rattle', 'chocalho', 'The rattle is loud.', 'O chocalho é barulhento.'), ('🟰', 'alike', 'iguais', 'They look alike.', 'Eles são parecidos.')],
    [('___ of them are kind.', 'Os dois são gentis.', ['Both', 'Either', 'Neither'], 0, '**Both** of them'), ('___ of them can come.', 'Qualquer um deles pode vir.', ['Either', 'Both', 'Neither'], 0, '**Either** of them'),
     ('___ of them is late.', 'Nenhum deles está atrasado.', ['Neither', 'Both', 'Either'], 0, '**Neither** of them'), ('The ___ is loud.', 'O chocalho é barulhento.', ['rattle', 'rattles are', 'rattling'], 0, 'the **rattle**.')],
    [('Qual frase está certa?', ['Both of them are kind.', 'Both of them is kind.', 'Both them are kind.'], 0, 'both of them + are.'), ('Qual está certa?', ['Neither of them is late.', 'Neither of them are not late.', 'Neither them is late.'], 0, 'neither of them + is.')],
    [['Girl', 'Look at my friends. Both of them are kind.', 'Olhe meus amigos. Os dois são gentis.'], ['Boy', 'Can they help me?', 'Eles podem me ajudar?'], ['Girl', 'Either of them can help.', 'Qualquer um deles pode ajudar.'], ['Boy', 'Are they late?', 'Estão atrasados?'],
     ['Girl', 'Neither of them is late.', 'Nenhum deles está atrasado.'], ['Boy', 'The rattle is loud.', 'O chocalho é barulhento.'], ['Girl', 'They look alike.', 'Eles são parecidos.'], ['Boy', 'Nice!', 'Legal!']],
    [('Are the friends kind?', 'Os amigos são gentis?', [('😊', 'Both are'), ('😠', 'Neither is'), ('🤷', 'Unknown')], 0, 0, 'Diz: “Both of them are kind.”'), ('Who can help?', 'Quem pode ajudar?', [('🙋', 'Either of them'), ('🚫', 'Nobody'), ('👴', 'Grandpa')], 0, 2, 'Diz: “Either of them can help.”'),
     ('What is loud?', 'O que é barulhento?', [('🪇', 'The rattle'), ('🚗', 'The car'), ('📻', 'The radio')], 0, 5, 'Diz: “The rattle is loud.”')],
    [('👯', 'Both of us', 'Nós dois', 'dois falantes', 'Both of us agree.', 'Nós dois concordamos.'), ('🔀', 'Either of you', 'Qualquer um de vocês', 'oferecer', 'Either of you can go.', 'Qualquer um de vocês pode ir.'),
     ('🚫', 'Neither of us', 'Nenhum de nós', 'negar', 'Neither of us knows.', 'Nenhum de nós sabe.'), ('🟰', 'Look alike', 'Ser parecido', 'comparar', 'They look alike.', 'Eles são parecidos.')]))

# ---------- so / such ----------
SS_VOCAB = [('🛏️', 'mattress', 'colchão', 'Soa como “MÉ-tris”.'), ('😴', 'pillow', 'travesseiro', 'Soa como “PÍ-lôu”.'), ('🧣', 'blanket', 'cobertor', 'Soa como “BLÉN-kit”.'),
            ('🥱', 'sleepy', 'com sono', 'Soa como “SLI-pi”.'), ('🛋️', 'comfortable', 'confortável', 'Soa como “KÂM-fer-ta-bol”.'), ('🚪', 'bedroom', 'quarto', 'Soa como “BÉD-rum”.')]
SS_LAB = dict(short='sl', title='Laboratório de sons: mattress, pillow e sleepy', pt='a soa é; ow soa ôu; ee soa i longo.', tip='Em sleepy, o ee soa i longo.',
              words=[('mattress', 'MÉ-tris', 'colchão', 'a = é', 'matches', 'MÉ-tchiz'), ('pillow', 'PÍ-lôu', 'travesseiro', 'ow = ôu', 'pillar', 'PÍ-ler'), ('sleepy', 'SLI-pi', 'com sono', 'ee = i', 'slippy', 'SLÍ-pi')])
SS_VERBS = [('sleep', '😴', 'dormir', 'I sleep so well.', 'I sleep such well.', 'I slept.', 'Dormi.', 'so + **adjetivo/advérbio**.'),
            ('feel', '🛋️', 'sentir', 'It feels so soft.', 'It feels such soft.', 'I felt.', 'Senti.', 'so + **soft**.'),
            ('have', '🛏️', 'ter', 'It is such a soft bed.', 'It is so a soft bed.', 'I had.', 'Tive.', 'such a + **substantivo**.'),
            ('wake', '🥱', 'acordar', 'I woke up so tired.', 'I woke up such tired.', 'I wake.', 'Eu acordo.', 'passado **woke**.')]
SS_MOLD = [('So + adj', 'It is so', 'é tão', [(' soft.', ' macio.'), (' comfortable.', ' confortável.'), (' quiet.', ' silencioso.')]),
           ('Such a', 'It is such a', 'é um(a) tão', [(' soft bed.', ' cama macia.'), (' nice room.', ' quarto agradável.'), (' big pillow.', ' travesseiro grande.')]),
           ('So… that', 'I was so tired', 'eu estava tão cansada', [(' that I slept.', ' que dormi.'), (' that I fell.', ' que caí.'), (' that I left.', ' que saí.')])]
SS_RULE = ('So e such', 'So vai com adjetivo; such a com substantivo.', 'Em português “tão macio”. Em inglês: **so soft**.')
SS_FM = [('So', 'The bed is', 'so soft.', 'The bed is so soft.', 'so + adjetivo.'), ('Such', 'It is', 'such a soft bed.', 'It is such a soft bed.', 'such a + substantivo.')]
SS_TRAPS = [('Qual frase está certa?', ['The bed is so soft.', 'The bed is such soft.', 'The bed is so a soft.'], 0, 'so + adjetivo.'), ('Qual está certa?', ['It is such a soft bed.', 'It is so a soft bed.', 'It is such soft bed.'], 0, 'such a + adj + subst.')]

EPS.append(mk(81292, 'Sleep Well', "falar de dormir bem com so e such (mattress, pillow, blanket)",
    "so × such: so soft · such a soft bed", "Hoje você aprende so e such: The bed is so soft. It is such a soft bed. I was so tired that I slept.",
    ('Woman', 'Man'), ['polly', 'tom'], 'bedroom', 'The Princess and the Pea', ['bedroom', 'living', 'home1', 'kitchen', 'hall', 'cafe2'],
    ('Sleep Well: em 10 minutos você diz “tão macio” e “uma cama tão boa”', 'No quarto, a mulher e o homem testam um colchão muito macio.'), ('Mais intensidade', 'Próximo: Tão e tal'),
    SS_RULE, SS_FM, SS_VOCAB, SS_LAB, SS_VERBS, SS_MOLD,
    ('🛏️', 'Intensidade', 'Use so, such a e so…that', 'Fale. **Diga a cama é tão macia, é uma cama tão boa e eu estava tão cansada que dormi.**', 'such a', 'The bed is so soft. It is such a nice bed. I was so tired that I slept.',
     [('Usei so?', r"\bis\s+so\s+soft\b", 'The bed is so soft.', 'A cama é tão macia.', 'So! 🛏️'), ('Usei such a?', r"\bsuch\s+a\s+nice\s+bed\b", 'It is such a nice bed.', 'É uma cama tão boa.', 'Such! 😴'), ('Usei so that?', r"\bso\s+tired\s+that\b", 'I was so tired that I slept.', 'Eu estava tão cansada que dormi.', 'That! 🥱')]),
    ('🧣', 'Fixas', 'Use sleep like a log, hit the hay e sleep tight', 'Fale. **Diga dormir como pedra, ir para a cama e durma bem.**', 'sleep tight', 'I slept like a log. I will hit the hay. Sleep tight!',
     [('Disse like a log?', r"\blike\s+a\s+log\b", 'I slept like a log.', 'Dormi como pedra.', 'Log! 🪵'), ('Disse hit the hay?', r"\bhit\s+the\s+hay\b", 'I will hit the hay.', 'Vou para a cama.', 'Hay! 🛏️'), ('Disse sleep tight?', r"\bsleep\s+tight\b", 'Sleep tight!', 'Durma bem!', 'Tight! 😴')]),
    [('🛏️', 'so soft', 'tão macio', 'The mattress is so soft.', 'O colchão é tão macio.'), ('😴', 'such a bed', 'uma cama tão boa', 'It is such a nice bed.', 'É uma cama tão boa.'),
     ('🥱', 'so tired', 'tão cansada', 'I was so tired.', 'Eu estava tão cansada.'), ('🧣', 'blanket', 'cobertor', 'The blanket is warm.', 'O cobertor é quente.'), ('🛋️', 'comfortable', 'confortável', 'It is comfortable.', 'É confortável.')],
    [('The mattress is ___ soft.', 'O colchão é tão macio.', ['so', 'such', 'such a'], 0, '**so** + adjetivo.'), ('It is ___ a nice bed.', 'É uma cama tão boa.', ['such', 'so', 'very a'], 0, '**such** a + substantivo.'),
     ('I was so tired ___ I slept.', 'Eu estava tão cansada que dormi.', ['that', 'than', 'what'], 0, 'so… **that**.'), ('The ___ is warm.', 'O cobertor é quente.', ['blanket', 'blankets are', 'blanketing'], 0, 'the **blanket**.')],
    SS_TRAPS,
    [['Woman', 'Try the bed. The mattress is so soft.', 'Experimente a cama. O colchão é tão macio.'], ['Man', 'It is such a nice bed!', 'É uma cama tão boa!'], ['Woman', 'And the blanket is warm.', 'E o cobertor é quente.'], ['Man', 'Is it comfortable?', 'É confortável?'],
     ['Woman', 'So comfortable. I was so tired that I slept.', 'Muito confortável. Eu estava tão cansada que dormi.'], ['Man', 'Are you sleepy now?', 'Está com sono agora?'], ['Woman', 'A little.', 'Um pouco.'], ['Man', 'Sleep tight!', 'Durma bem!']],
    [('How is the mattress?', 'Como é o colchão?', [('☁️', 'So soft'), ('🪨', 'Hard'), ('🔥', 'Hot')], 0, 0, 'Diz: “so soft.”'), ('How is the blanket?', 'Como é o cobertor?', [('🔥', 'Warm'), ('🧊', 'Cold'), ('💧', 'Wet')], 0, 2, 'Diz: “the blanket is warm.”'),
     ('Why did she sleep?', 'Por que ela dormiu?', [('🥱', 'She was tired'), ('📺', 'TV was on'), ('🎵', 'Music')], 0, 4, 'Diz: “so tired that I slept.”')],
    [('🪵', 'Sleep like a log', 'Dormir como pedra', 'dormir fundo', 'I slept like a log.', 'Dormi como pedra.'), ('🛏️', 'Hit the hay', 'Ir para a cama', 'ir dormir', 'I will hit the hay.', 'Vou para a cama.'),
     ('😴', 'Sleep tight', 'Durma bem', 'boa noite', 'Sleep tight!', 'Durma bem!'), ('🌙', 'Call it a night', 'Encerrar o dia', 'ir descansar', 'Let us call it a night.', 'Vamos encerrar o dia.')]))

EPS.append(mk(7081292, 'Tão e tal', "so, such, so many e so much na prática (mattress, pillow, comfortable)",
    "tão e tal: so many · so much · such a lot", "Hoje você pratica so many, so much e such a: So many pillows! So much noise! Such a lot of fun.",
    ('Girl', 'Boy'), ['polly', 'tommy'], 'bedroom', 'The Princess and the Pea', ['bedroom', 'home1', 'living', 'kitchen', 'yard', 'school'],
    ('Tão e tal: em 10 minutos você diz “tantos” e “tanto” sem errar', 'No quarto, a menina e o menino arrumam muitos travesseiros e cobertores.'), ('Mais intensidade', 'Próximo: Too and Enough'),
    ('So many, so much', 'Contável × incontável.', 'Em português “tantos travesseiros”. Em inglês: **so many pillows**.'),
    [('So many', 'There are', 'so many pillows.', 'There are so many pillows.', 'so many + contável.'), ('So much', 'There is', 'so much noise.', 'There is so much noise.', 'so much + incontável.')],
    SS_VOCAB, SS_LAB, SS_VERBS, [('So many', 'There are so many', 'há tantos', [(' pillows.', ' travesseiros.'), (' blankets.', ' cobertores.'), (' beds.', ' camas.')]), ('So much', 'There is so much', 'há tanto', [(' noise.', ' barulho.'), (' light.', ' luz.'), (' space.', ' espaço.')]), ('Such a lot', 'It is such a lot of', 'é muita coisa de', [(' fun.', ' diversão.'), (' work.', ' trabalho.'), (' love.', ' amor.')])],
    ('🛏️', 'Quantidade', 'Use so many, so much e such a lot', 'Fale. **Diga há tantos travesseiros, há tanto barulho e é muita diversão.**', 'so much', 'There are so many pillows. There is so much noise. It is such a lot of fun.',
     [('Usei so many?', r"\bso\s+many\s+pillows\b", 'There are so many pillows.', 'Há tantos travesseiros.', 'Many! 😴'), ('Usei so much?', r"\bso\s+much\s+noise\b", 'There is so much noise.', 'Há tanto barulho.', 'Much! 🔊'), ('Usei such a lot?', r"\bsuch\s+a\s+lot\s+of\s+fun\b", 'It is such a lot of fun.', 'É muita diversão.', 'Lot! 🎉')]),
    ('🧣', 'Fixas', 'Use so far, so long e so what', 'Fale. **Diga até agora, até logo e e daí.**', 'so what', 'So far, so good. So long! So what?',
     [('Disse so far?', r"\bso\s+far\b", 'So far, so good.', 'Até agora, tudo bem.', 'Far! 🛏️'), ('Disse so long?', r"\bso\s+long\b", 'So long!', 'Até logo!', 'Long! 👋'), ('Disse so what?', r"\bso\s+what\b", 'So what?', 'E daí?', 'What! 🤷')]),
    [('😴', 'so many', 'tantos', 'So many pillows!', 'Tantos travesseiros!'), ('🔊', 'so much', 'tanto', 'So much noise!', 'Tanto barulho!'),
     ('🎉', 'such a lot of', 'muita coisa de', 'It is such a lot of fun.', 'É muita diversão.'), ('🧣', 'blanket', 'cobertor', 'Take a blanket.', 'Pegue um cobertor.'), ('🚪', 'bedroom', 'quarto', 'My bedroom is big.', 'Meu quarto é grande.')],
    [('There are so ___ pillows.', 'Há tantos travesseiros.', ['many', 'much', 'a lot'], 0, 'so **many** + contável.'), ('There is so ___ noise.', 'Há tanto barulho.', ['much', 'many', 'few'], 0, 'so **much** + incontável.'),
     ('It is such a ___ of fun.', 'É muita diversão.', ['lot', 'lots', 'many'], 0, 'such a **lot** of.'), ('My ___ is big.', 'Meu quarto é grande.', ['bedroom', 'bedrooms are', 'bedding'], 0, 'my **bedroom**.')],
    [('Qual frase está certa?', ['There are so many pillows.', 'There are so much pillows.', 'There is so many pillows.'], 0, 'so many + plural.'), ('Qual está certa?', ['There is so much noise.', 'There is so many noise.', 'There are so much noise.'], 0, 'so much + incontável.')],
    [['Girl', 'Look! There are so many pillows.', 'Olhe! Há tantos travesseiros.'], ['Boy', 'And so many blankets.', 'E tantos cobertores.'], ['Girl', 'There is so much noise!', 'Há tanto barulho!'], ['Boy', 'My bedroom is big.', 'Meu quarto é grande.'],
     ['Girl', 'It is such a lot of fun.', 'É muita diversão.'], ['Boy', 'Are you sleepy?', 'Está com sono?'], ['Girl', 'So what? Let us play.', 'E daí? Vamos brincar.'], ['Boy', 'Okay!', 'Certo!']],
    [('What are there many of?', 'Do que há muitos?', [('😴', 'Pillows'), ('🍎', 'Apples'), ('📚', 'Books')], 0, 0, 'Diz: “so many pillows.”'), ('What is noisy?', 'O que é barulhento?', [('🔊', 'The room'), ('🌳', 'The tree'), ('🐟', 'The fish')], 0, 2, 'Diz: “so much noise.”'),
     ('Is she sleepy?', 'Ela está com sono?', [('🎮', 'No, she plays'), ('😴', 'Yes, she sleeps'), ('📖', 'She reads')], 0, 6, 'Diz: “Let us play.”')],
    [('🧣', 'So far, so good', 'Até agora, tudo bem', 'balanço', 'So far, so good.', 'Até agora, tudo bem.'), ('👋', 'So long', 'Até logo', 'despedida', 'So long!', 'Até logo!'),
     ('🤷', 'So what?', 'E daí?', 'indiferença', 'So what?', 'E daí?'), ('💤', 'And so on', 'E assim por diante', 'listar', 'Pillows, and so on.', 'Travesseiros e assim por diante.')]))

# ---------- too / enough ----------
TE_VOCAB = [('⌛', 'too', 'demais', 'Soa como “TUU”.'), ('✅', 'enough', 'suficiente', 'Soa como “i-NÂF”.'), ('🏋️', 'lift', 'levantar', 'Soa como “LIFT”.'),
            ('🗿', 'giant', 'gigante', 'Soa como “DJÁI-ent”.'), ('🐜', 'tiny', 'minúsculo', 'Soa como “TÁI-ni”.'), ('💪', 'strong', 'forte', 'Soa como “STRÓNG”.')]
TE_LAB = dict(short='te', title='Laboratório de sons: too, enough e giant', pt='oo soa u; ough soa âf; g soa dj.', tip='Em enough, o ough soa âf.',
              words=[('too', 'TUU', 'demais', 'oo = u', 'toe', 'TÔU'), ('enough', 'i-NÂF', 'suficiente', 'ough = âf', 'enjoy', 'en-DJÓI'), ('giant', 'DJÁI-ent', 'gigante', 'g = dj', 'giraffe', 'dji-RÉF')])
TE_VERBS = [('lift', '🏋️', 'levantar', 'I cannot lift it.', 'I cannot lifting it.', 'I lifted.', 'Levantei.', 'cannot + **lift**.'),
            ('carry', '🎒', 'carregar', 'too heavy to carry', 'too heavy for carrying it', 'I carried.', 'Carreguei.', 'too + adj + **to** verbo.'),
            ('reach', '🙆', 'alcançar', 'tall enough to reach', 'enough tall to reach', 'I reached.', 'Alcancei.', 'adj + **enough**.'),
            ('fit', '👟', 'caber', 'small enough to fit', 'enough small to fit', 'It fits.', 'Cabe.', 'small **enough**.')]
TE_MOLD = [('Too + adj', 'This bag is too', 'esta bolsa é pesada demais', [(' heavy for me.', ' para mim.'), (' big to carry.', ' para carregar.'), (' hot to hold.', ' para segurar.')]),
           ('Adj + enough', 'He is strong', 'ele é forte', [(' enough to lift it.', ' o bastante para levantar.'), (' enough to win.', ' o bastante para vencer.'), (' enough to help.', ' o bastante para ajudar.')]),
           ('Enough + noun', 'We have enough', 'temos o bastante de', [(' time.', ' tempo.'), (' money.', ' dinheiro.'), (' food.', ' comida.')])]
TE_RULE = ('Too e enough', 'Too = demais; enough = o bastante.', 'Em português “pesado demais”. Em inglês: **too heavy**.')
TE_FM = [('Too', 'This bag is', 'too heavy for me.', 'This bag is too heavy for me.', 'too antes do adjetivo.'), ('Enough', 'He is strong', 'enough to lift it.', 'He is strong enough to lift it.', 'enough depois do adjetivo.')]
TE_TRAPS = [('Qual frase está certa?', ['This bag is too heavy for me.', 'This bag is heavy too for me.', 'This bag is too much heavy for me.'], 0, 'too + adjetivo.'), ('Qual está certa?', ['He is strong enough to lift it.', 'He is enough strong to lift it.', 'He is strong enough lifting it.'], 0, 'adjetivo + enough.')]

EPS.append(mk(82159, 'Too and Enough', "falar de excesso e suficiência com too e enough (lift, giant, tiny)",
    "too × enough: too heavy · strong enough", "Hoje você aprende too e enough: This bag is too heavy for me. He is strong enough to lift it.",
    ('Man', 'Woman'), ['tom', 'polly'], 'street', "Gulliver's Travels", ['street', 'park', 'shop', 'cafe2', 'hall', 'pier'],
    ('Too and Enough: em 10 minutos você diz “pesado demais” e “forte o bastante”', 'Na rua, o homem e a mulher tentam carregar uma mala gigante.'), ('Mais intensidade', 'Próximo: Too e enough'),
    TE_RULE, TE_FM, TE_VOCAB, TE_LAB, TE_VERBS, TE_MOLD,
    ('⌛', 'Medida', 'Use too, enough e too…to', 'Fale. **Diga esta bolsa é pesada demais, ele é forte o bastante e é pesada demais para carregar.**', 'strong enough', 'This bag is too heavy for me. He is strong enough to lift it. It is too heavy to carry.',
     [('Usei too?', r"\btoo\s+heavy\b", 'This bag is too heavy for me.', 'Esta bolsa é pesada demais para mim.', 'Too! ⌛'), ('Usei enough?', r"\bstrong\s+enough\b", 'He is strong enough to lift it.', 'Ele é forte o bastante para levantar.', 'Enough! ✅'), ('Usei too to?', r"\btoo\s+heavy\s+to\s+carry\b", 'It is too heavy to carry.', 'É pesada demais para carregar.', 'To! 🏋️')]),
    ('🗿', 'Fixas', 'Use too good to be true, good enough e more than enough', 'Fale. **Diga bom demais para ser verdade, bom o bastante e mais que o bastante.**', 'good enough', 'It is too good to be true. It is good enough. We have more than enough.',
     [('Disse too good to be true?', r"\btoo\s+good\s+to\s+be\s+true\b", 'It is too good to be true.', 'É bom demais para ser verdade.', 'True! ⌛'), ('Disse good enough?', r"\bgood\s+enough\b", 'It is good enough.', 'Está bom o bastante.', 'Good! ✅'), ('Disse more than enough?', r"\bmore\s+than\s+enough\b", 'We have more than enough.', 'Temos mais que o bastante.', 'More! 🍽️')]),
    [('⌛', 'too heavy', 'pesado demais', 'This bag is too heavy for me.', 'Esta bolsa é pesada demais para mim.'), ('✅', 'strong enough', 'forte o bastante', 'He is strong enough.', 'Ele é forte o bastante.'),
     ('🗿', 'giant', 'gigante', 'It is a giant bag.', 'É uma bolsa gigante.'), ('🐜', 'tiny', 'minúsculo', 'The key is tiny.', 'A chave é minúscula.'), ('🏋️', 'lift', 'levantar', 'I cannot lift it.', 'Não consigo levantá-la.')],
    [('This bag is ___ heavy for me.', 'Esta bolsa é pesada demais para mim.', ['too', 'enough', 'very much'], 0, '**too** + adjetivo.'), ('He is strong ___ to lift it.', 'Ele é forte o bastante para levantar.', ['enough', 'too', 'much'], 0, 'adjetivo + **enough**.'),
     ('I cannot ___ it.', 'Não consigo levantá-la.', ['lift', 'lifts', 'lifting'], 0, 'cannot + **lift**.'), ('The key is ___.', 'A chave é minúscula.', ['tiny', 'tinily', 'a tiny'], 0, 'is **tiny**.')],
    TE_TRAPS,
    [['Man', 'This bag is too heavy for me.', 'Esta bolsa é pesada demais para mim.'], ['Woman', 'It is a giant bag.', 'É uma bolsa gigante.'], ['Man', 'I cannot lift it.', 'Não consigo levantá-la.'], ['Woman', 'Ask Ben. He is strong enough to lift it.', 'Peça ao Ben. Ele é forte o bastante.'],
     ['Man', 'Is the key in the bag?', 'A chave está na bolsa?'], ['Woman', 'Yes, but the key is tiny.', 'Sim, mas a chave é minúscula.'], ['Man', 'We have enough time to search.', 'Temos tempo suficiente para procurar.'], ['Woman', 'Good.', 'Bom.']],
    [('Why can he not lift it?', 'Por que ele não consegue levantar?', [('🏋️', 'Too heavy'), ('🪶', 'Too light'), ('🔥', 'Too hot')], 0, 0, 'Diz: “too heavy for me.”'), ('Who is strong enough?', 'Quem é forte o bastante?', [('💪', 'Ben'), ('👶', 'A baby'), ('🐶', 'A dog')], 0, 3, 'Diz: “Ben… strong enough.”'),
     ('How is the key?', 'Como é a chave?', [('🐜', 'Tiny'), ('🗿', 'Giant'), ('🔥', 'Hot')], 0, 5, 'Diz: “the key is tiny.”')],
    [('⌛', 'Too good to be true', 'Bom demais para ser verdade', 'desconfiar', 'It is too good to be true.', 'É bom demais para ser verdade.'), ('✅', 'Good enough', 'Bom o bastante', 'aceitar', 'It is good enough.', 'Está bom o bastante.'),
     ('🍽️', 'More than enough', 'Mais que o bastante', 'sobrar', 'We have more than enough.', 'Temos mais que o bastante.'), ('🏁', 'Enough is enough', 'Chega', 'limite', 'Enough is enough!', 'Chega!')]))

EPS.append(mk(7082159, 'Too e enough', "too e enough com to, for e not…enough (lift, giant, tiny)",
    "too e enough: too…to · not…enough · enough of", "Hoje você pratica too…to e not…enough: It is too big to lift. It is not strong enough. We have enough food.",
    ('Girl', 'Boy'), ['polly', 'tommy'], 'park2', "Gulliver's Travels", ['park2', 'yard', 'street', 'school', 'lake', 'cafe2'],
    ('Too e enough: em 10 minutos você fala de limites com precisão', 'No parque, a menina e o menino tentam levantar uma pedra gigante.'), ('Mais intensidade', 'Próximo: Pulling your leg'),
    ('Too…to, not…enough', 'Dois jeitos de dizer “não dá”.', 'Em português “grande demais para levantar”. Em inglês: **too big to lift**.'),
    [('Too…to', 'It is', 'too big to lift.', 'It is too big to lift.', 'too + adj + to.'), ('Not enough', 'I am', 'not strong enough.', 'I am not strong enough.', 'not + adj + enough.')],
    TE_VOCAB, TE_LAB, TE_VERBS, [('Too…to', 'It is too big', 'é grande demais', [(' to lift.', ' para levantar.'), (' to move.', ' para mover.'), (' to hide.', ' para esconder.')]), ('Not enough', 'I am not', 'eu não sou', [(' strong enough.', ' forte o bastante.'), (' tall enough.', ' alto o bastante.'), (' fast enough.', ' rápido o bastante.')]), ('Enough', 'We have enough', 'temos o bastante de', [(' food.', ' comida.'), (' chairs.', ' cadeiras.'), (' water.', ' água.')])],
    ('⌛', 'Limites', 'Use too to, not enough e enough', 'Fale. **Diga é grande demais para levantar, não sou forte o bastante e temos comida suficiente.**', 'not strong enough', 'It is too big to lift. I am not strong enough. We have enough food.',
     [('Usei too to?', r"\btoo\s+big\s+to\s+lift\b", 'It is too big to lift.', 'É grande demais para levantar.', 'Big! ⌛'), ('Usei not enough?', r"\bnot\s+strong\s+enough\b", 'I am not strong enough.', 'Não sou forte o bastante.', 'Not! 🚫'), ('Usei enough?', r"\benough\s+food\b", 'We have enough food.', 'Temos comida suficiente.', 'Food! 🍽️')]),
    ('🗿', 'Fixas', 'Use too much, too many e far too', 'Fale. **Diga demais, muitos demais e bem demais.**', 'far too', 'Too much sugar. Too many cars. It is far too late.',
     [('Disse too much?', r"\btoo\s+much\b", 'Too much sugar.', 'Açúcar demais.', 'Much! 🍬'), ('Disse too many?', r"\btoo\s+many\b", 'Too many cars.', 'Carros demais.', 'Many! 🚗'), ('Disse far too?', r"\bfar\s+too\b", 'It is far too late.', 'É tarde demais.', 'Far! ⏰')]),
    [('⌛', 'too big to lift', 'grande demais para levantar', 'It is too big to lift.', 'É grande demais para levantar.'), ('🚫', 'not strong enough', 'não forte o bastante', 'I am not strong enough.', 'Não sou forte o bastante.'),
     ('🍽️', 'enough food', 'comida suficiente', 'We have enough food.', 'Temos comida suficiente.'), ('🗿', 'giant', 'gigante', 'The rock is giant.', 'A pedra é gigante.'), ('💪', 'strong', 'forte', 'You are strong.', 'Você é forte.')],
    [('It is too big ___ lift.', 'É grande demais para levantar.', ['to', 'for', 'of'], 0, 'too big **to** lift.'), ('I am not strong ___.', 'Não sou forte o bastante.', ['enough', 'too', 'very'], 0, 'strong **enough**.'),
     ('We have ___ food.', 'Temos comida suficiente.', ['enough', 'too', 'much'], 0, '**enough** + substantivo.'), ('The rock is ___.', 'A pedra é gigante.', ['giant', 'gigantly', 'a giant is'], 0, 'is **giant**.')],
    [('Qual frase está certa?', ['It is too big to lift.', 'It is too big for lift.', 'It is too big lifting.'], 0, 'too big to lift.'), ('Qual está certa?', ['I am not strong enough.', 'I am not enough strong.', 'I am no strong enough.'], 0, 'not strong enough.')],
    [['Girl', 'Look at this rock. It is too big to lift.', 'Olhe esta pedra. É grande demais para levantar.'], ['Boy', 'I am not strong enough.', 'Não sou forte o bastante.'], ['Girl', 'The rock is giant.', 'A pedra é gigante.'], ['Boy', 'You are strong!', 'Você é forte!'],
     ['Girl', 'Not enough. Let us ask for help.', 'Não o bastante. Vamos pedir ajuda.'], ['Boy', 'Do we have enough food for the picnic?', 'Temos comida suficiente para o piquenique?'], ['Girl', 'Yes, we have enough food.', 'Sim, temos comida suficiente.'], ['Boy', 'Great!', 'Ótimo!']],
    [('What is too big?', 'O que é grande demais?', [('🗿', 'The rock'), ('🌳', 'The tree'), ('🚗', 'The car')], 0, 0, 'Diz: “too big to lift.”'), ('Who is not strong enough?', 'Quem não é forte o bastante?', [('👦', 'The boy'), ('👧', 'The girl'), ('👴', 'Grandpa')], 0, 1, 'Diz: “I am not strong enough.”'),
     ('Do they have food?', 'Eles têm comida?', [('🍽️', 'Yes, enough'), ('🚫', 'No'), ('🤷', 'Unknown')], 0, 6, 'Diz: “enough food.”')],
    [('⌛', 'Too much', 'Demais', 'excesso', 'Too much sugar.', 'Açúcar demais.'), ('🚗', 'Too many', 'Muitos demais', 'excesso contável', 'Too many cars.', 'Carros demais.'),
     ('⏰', 'Far too', 'Bem demais', 'reforço', 'It is far too late.', 'É tarde demais.'), ('🏁', 'Enough is enough', 'Chega', 'limite', 'Enough is enough!', 'Chega!')]))
