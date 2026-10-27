# B1 · episódios 233–238: acrescentar ideias, organizar a fala, phrasal verbs com pull.
from v3.b1h import *

from v3.ovrb1 import install
EPS = []
install(globals(), 'S')

def mk(n, title, sub, pat, why, names, ids, rs, obra, scenes, cover, teaser, rule, fm, vocab, lab, verbs, mold, prod, m2, hot, gaps, traps, lines, quiz, exps):
    return S(n=n, title=title, sub=sub, pattern=pat, why=why, names=names, ids=ids, rs=rs, obra=(obra, obra),
             hot=hot, gaps=gaps, traps=traps, rule=rule, fm=fm, cover=cover, vocab=vocab, lines=lines, quiz=quiz,
             teaser=teaser, exps=exps, lab=lab, verbs=verbs, mold=mold, prod=prod, m2=m2, scenes=scenes)

# ---------- 233 / 234 · acrescentar ideias ----------
ADD_VOCAB = [('➕', 'besides', 'além disso', 'Soa como “bi-SÁIDZ”.'), ('✨', 'moreover', 'além do mais', 'Soa como “mor-ÓU-ver”.'), ('🧮', 'addition', 'adição', 'Soa como “a-DÍ-shon”.'),
             ('🥂', 'guests', 'convidados', 'Soa como “GÉSTS”.'), ('💐', 'flowers', 'flores', 'Soa como “FLÁU-erz”.'), ('💭', 'thoughts', 'pensamentos', 'Soa como “THÓTS”.')]
ADD_LAB = dict(short='bs', title='Laboratório de sons: besides, moreover e thoughts', pt='ai soa ai; o soa ó; th soa s com a língua.', tip='Em thoughts, ponha a língua entre os dentes.',
               words=[('besides', 'bi-SÁIDZ', 'além disso', 'i = ai', 'beside', 'bi-SÁID'), ('moreover', 'mor-ÓU-ver', 'além do mais', 'o = ôu', 'more', 'MÓR'), ('thoughts', 'THÓTS', 'pensamentos', 'th = s', 'thanks', 'THÉNKS')])
ADD_VERBS = [('cook', '🍳', 'cozinhar', 'she is a great cook', 'she is a great cooks', 'I cook.', 'Eu cozinho.', 'a great **cook**.'),
             ('invite', '🥂', 'convidar', 'we invited guests', 'we invite guests yesterday', 'I invite.', 'Eu convido.', 'passado **invited**.'),
             ('think', '💭', 'pensar', 'I think so', 'I thinks so', 'I thought.', 'Pensei.', 'I **think**.'),
             ('add', '➕', 'acrescentar', 'let me add', 'let me adding', 'I add.', 'Eu acrescento.', 'let me **add**.')]
ADD_MOLD = [('Besides', 'Besides,', 'além disso,', [(' she is a great cook.', ' ela cozinha muito bem.'), (' it is cheap.', ' é barato.'), (' I am free.', ' estou livre.')]),
            ('Moreover', 'Moreover,', 'além do mais,', [(' the guests were kind.', ' os convidados foram gentis.'), (' the flowers were pretty.', ' as flores eram lindas.'), (' it was fun.', ' foi divertido.')]),
            ('In addition', 'In addition,', 'além disso,', [(' we have time.', ' temos tempo.'), (' he knows her.', ' ele a conhece.'), (' it is near.', ' é perto.')])]
ADD_RULE = ('Acrescentar ideias', 'Besides e moreover somam um argumento.', 'Em português “além disso”. Em inglês: **besides,**.')
ADD_FM = [('Besides', 'Besides,', 'she is a great cook.', 'Besides, she is a great cook.', 'vírgula depois.'), ('Moreover', 'Moreover,', 'it was fun.', 'Moreover, it was fun.', 'mais formal.')]
ADD_TRAPS = [('Qual frase está certa?', ['Besides, she is a great cook.', 'Besides she, is a great cook.', 'She besides is a great cook.'], 0, 'Besides, + frase.'),
             ('Qual está certa?', ['Moreover, it was fun.', 'Moreover it, was fun.', 'It moreover, was fun.'], 0, 'Moreover, + frase.')]

EPS.append(mk(82152, 'Adding Ideas', "acrescentar argumentos com besides, moreover e in addition (guests, flowers, thoughts)",
    "acrescentar ideias: besides · moreover · in addition", "Hoje você aprende a somar argumentos: Besides, she is a great cook. Moreover, the guests were kind.",
    ('Woman', 'Man'), ['polly', 'tom'], 'cafe2', 'Mrs Dalloway', ['cafe2', 'living', 'street', 'park', 'hall', 'kitchen'],
    ('Adding Ideas: em 10 minutos você soma argumentos como um escritor', 'No café, a mulher e o homem planejam uma festa e somam motivos.'), ('Mais conectores', 'Próximo: Acrescentar ideias'),
    ADD_RULE, ADD_FM, ADD_VOCAB, ADD_LAB, ADD_VERBS, ADD_MOLD,
    ('➕', 'Somar', 'Use besides, moreover e in addition', 'Fale. **Diga além disso ela cozinha bem, além do mais os convidados são gentis e além disso temos tempo.**', 'moreover', 'Besides, she is a great cook. Moreover, the guests are kind. In addition, we have time.',
     [('Usei besides?', r"\bbesides,?\s+she\b", 'Besides, she is a great cook.', 'Além disso, ela cozinha muito bem.', 'Besides! ➕'), ('Usei moreover?', r"\bmoreover,?\s+the\b", 'Moreover, the guests are kind.', 'Além do mais, os convidados são gentis.', 'Moreover! ✨'), ('Usei in addition?', r"\bin\s+addition,?\s+we\b", 'In addition, we have time.', 'Além disso, temos tempo.', 'Addition! 🧮')]),
    ('🥂', 'Fixas', 'Use what is more, on top of that e not to mention', 'Fale. **Diga o que é mais, além disso tudo e sem falar.**', 'not to mention', 'What is more, it is cheap. On top of that, it is near. Not to mention, it is fun.',
     [('Disse what is more?', r"\bwhat\s+is\s+more\b", 'What is more, it is cheap.', 'O que é mais, é barato.', 'More! ➕'), ('Disse on top of that?', r"\bon\s+top\s+of\s+that\b", 'On top of that, it is near.', 'Além disso tudo, é perto.', 'Top! ✨'), ('Disse not to mention?', r"\bnot\s+to\s+mention\b", 'Not to mention, it is fun.', 'Sem falar que é divertido.', 'Mention! 💭')]),
    [('➕', 'Besides,', 'além disso,', 'Besides, she is a great cook.', 'Além disso, ela cozinha muito bem.'), ('✨', 'Moreover,', 'além do mais,', 'Moreover, the guests were kind.', 'Além do mais, os convidados foram gentis.'),
     ('🧮', 'In addition,', 'além disso,', 'In addition, we have time.', 'Além disso, temos tempo.'), ('🥂', 'guests', 'convidados', 'The guests are here.', 'Os convidados estão aqui.'), ('💐', 'flowers', 'flores', 'The flowers are pretty.', 'As flores são lindas.')],
    [('___, she is a great cook.', 'Além disso, ela cozinha bem.', ['Besides', 'Beside', 'Because'], 0, '**Besides**,'), ('___, the guests were kind.', 'Além do mais, os convidados foram gentis.', ['Moreover', 'Morever', 'More'], 0, '**Moreover**,'),
     ('In ___, we have time.', 'Além disso, temos tempo.', ['addition', 'add', 'adding'], 0, 'In **addition**,'), ('The ___ are pretty.', 'As flores são lindas.', ['flowers', 'flowering', 'flower is'], 0, 'the **flowers**.')],
    ADD_TRAPS,
    [['Woman', 'Let us plan the party. Besides, she is a great cook.', 'Vamos planejar a festa. Além disso, ela cozinha muito bem.'], ['Man', 'Moreover, the guests are kind.', 'Além do mais, os convidados são gentis.'],
     ['Woman', 'In addition, we have time.', 'Além disso, temos tempo.'], ['Man', 'Who buys the flowers?', 'Quem compra as flores?'], ['Woman', 'I do. Besides, they are cheap.', 'Eu compro. Além disso, são baratas.'],
     ['Man', 'Good thoughts!', 'Bons pensamentos!'], ['Woman', 'Moreover, it is near.', 'Além do mais, é perto.'], ['Man', 'Perfect.', 'Perfeito.']],
    [('Who is a great cook?', 'Quem cozinha bem?', [('👩‍🍳', 'She is'), ('👨', 'He is'), ('🐶', 'The dog')], 0, 0, 'Diz: “she is a great cook.”'), ('Are the guests kind?', 'Os convidados são gentis?', [('😊', 'Yes'), ('😠', 'No'), ('🤷', 'Unknown')], 0, 1, 'Diz: “the guests are kind.”'),
     ('Who buys the flowers?', 'Quem compra as flores?', [('👩', 'The woman'), ('👨', 'The man'), ('👵', 'Nobody')], 0, 4, 'Diz: “I do.”')],
    [('➕', 'Not only… but also', 'Não só… mas também', 'soma forte', 'Not only kind but also wise.', 'Não só gentil, mas também sábia.'), ('🍰', 'On top of that', 'Além disso tudo', 'empilhar', 'On top of that, it is free.', 'Além disso tudo, é grátis.'),
     ('💐', 'What is more', 'O que é mais', 'enfatizar', 'What is more, I agree.', 'O que é mais, concordo.'), ('🙌', 'Not to mention', 'Sem falar', 'acrescentar', 'Not to mention the food.', 'Sem falar na comida.')]))

EPS.append(mk(7082152, 'Acrescentar ideias', "acrescentar argumentos na prática: besides, moreover e in addition (guests, flowers, thoughts)",
    "somar argumentos: besides · what is more · on top of that", "Hoje você pratica besides, what is more e on top of that: Besides, it is cheap. On top of that, it is near.",
    ('Girl', 'Boy'), ['polly', 'tommy'], 'living', 'Mrs Dalloway', ['living', 'home1', 'kitchen', 'yard', 'cafe2', 'school'],
    ('Acrescentar ideias: em 10 minutos você convence com mais de um motivo', 'Em casa, a menina e o menino convencem a família a fazer uma festa.'), ('Mais conectores', 'Próximo: First of all'),
    ADD_RULE, ADD_FM, ADD_VOCAB, ADD_LAB, ADD_VERBS, ADD_MOLD,
    ('➕', 'Somar', 'Use besides, what is more e on top of that', 'Fale. **Diga além disso é barato, o que é mais é perto e além disso tudo é divertido.**', 'on top of that', 'Besides, it is cheap. What is more, it is near. On top of that, it is fun.',
     [('Usei besides?', r"\bbesides,?\s+it\b", 'Besides, it is cheap.', 'Além disso, é barato.', 'Besides! ➕'), ('Usei what is more?', r"\bwhat\s+is\s+more\b", 'What is more, it is near.', 'O que é mais, é perto.', 'More! ✨'), ('Usei on top of that?', r"\bon\s+top\s+of\s+that\b", 'On top of that, it is fun.', 'Além disso tudo, é divertido.', 'Top! 🍰')]),
    ('🥂', 'Fixas', 'Use not only but also, to top it off e as well', 'Fale. **Diga não só gentil mas também sábia, para completar e também.**', 'to top it off', 'Not only kind but also wise. To top it off, she sings. I sing as well.',
     [('Disse not only?', r"\bnot\s+only\b.*\bbut\s+also\b", 'Not only kind but also wise.', 'Não só gentil, mas também sábia.', 'Only! ➕'), ('Disse to top it off?', r"\bto\s+top\s+it\s+off\b", 'To top it off, she sings.', 'Para completar, ela canta.', 'Top! 🍰'), ('Disse as well?', r"\bas\s+well\b", 'I sing as well.', 'Eu também canto.', 'Well! 💭')]),
    [('➕', 'Besides,', 'além disso,', 'Besides, it is cheap.', 'Além disso, é barato.'), ('✨', 'What is more,', 'o que é mais,', 'What is more, it is near.', 'O que é mais, é perto.'),
     ('🍰', 'On top of that,', 'além disso tudo,', 'On top of that, it is fun.', 'Além disso tudo, é divertido.'), ('🥂', 'party', 'festa', 'The party is on Friday.', 'A festa é na sexta.'), ('💭', 'thoughts', 'pensamentos', 'I share my thoughts.', 'Compartilho meus pensamentos.')],
    [('___, it is cheap.', 'Além disso, é barato.', ['Besides', 'Beside', 'Because'], 0, '**Besides**,'), ('What is ___, it is near.', 'O que é mais, é perto.', ['more', 'most', 'many'], 0, 'What is **more**,'),
     ('On ___ of that, it is fun.', 'Além disso tudo, é divertido.', ['top', 'up', 'high'], 0, 'On **top** of that,'), ('The ___ is on Friday.', 'A festa é na sexta.', ['party', 'parties', 'partying'], 0, 'the **party**.')],
    ADD_TRAPS,
    [['Girl', 'Let us have a party. Besides, it is cheap.', 'Vamos fazer uma festa. Além disso, é barato.'], ['Boy', 'What is more, it is near.', 'O que é mais, é perto.'],
     ['Girl', 'On top of that, it is fun.', 'Além disso tudo, é divertido.'], ['Boy', 'When is the party?', 'Quando é a festa?'], ['Girl', 'The party is on Friday.', 'A festa é na sexta.'],
     ['Boy', 'I share my thoughts: invite everyone.', 'Dou minha opinião: convide todos.'], ['Girl', 'Besides, we have flowers.', 'Além disso, temos flores.'], ['Boy', 'Great!', 'Ótimo!']],
    [('Is it cheap?', 'É barato?', [('💰', 'Yes'), ('💸', 'No'), ('🤷', 'Unknown')], 0, 0, 'Diz: “it is cheap.”'), ('When is the party?', 'Quando é a festa?', [('📅', 'On Friday'), ('🌙', 'On Monday'), ('☀️', 'On Sunday')], 0, 4, 'Diz: “on Friday.”'),
     ('What does the boy say?', 'O que o menino diz?', [('📣', 'Invite everyone'), ('🙅', 'Cancel it'), ('😴', 'Sleep')], 0, 5, 'Diz: “invite everyone.”')],
    [('➕', 'Not only… but also', 'Não só… mas também', 'soma forte', 'Not only kind but also wise.', 'Não só gentil, mas também sábia.'), ('🍰', 'To top it off', 'Para completar', 'último argumento', 'To top it off, she sings.', 'Para completar, ela canta.'),
     ('💐', 'As well', 'Também', 'incluir', 'I sing as well.', 'Eu também canto.'), ('🙌', 'On top of that', 'Além disso tudo', 'empilhar', 'On top of that, it is free.', 'Além disso tudo, é grátis.')]))

# ---------- 235 / 236 · organizar a fala ----------
SEQ_VOCAB = [('1️⃣', 'first', 'primeiro', 'Soa como “FÂRST”.'), ('➡️', 'next', 'depois', 'Soa como “NÉKST”.'), ('🏁', 'finally', 'por fim', 'Soa como “FÁI-na-li”.'),
             ('🔚', 'lastly', 'por último', 'Soa como “LÉST-li”.'), ('📝', 'summary', 'resumo', 'Soa como “SÂ-ma-ri”.'), ('🔢', 'order', 'ordem', 'Soa como “ÓR-der”.')]
SEQ_LAB = dict(short='fi', title='Laboratório de sons: first, finally e order', pt='ir soa âr; i soa ai; or soa ór.', tip='Em first, o ir soa âr.',
               words=[('first', 'FÂRST', 'primeiro', 'ir = âr', 'fast', 'FÉST'), ('finally', 'FÁI-na-li', 'por fim', 'i = ai', 'final', 'FÁI-nal'), ('order', 'ÓR-der', 'ordem', 'or = ór', 'odor', 'ÓU-der')])
SEQ_VERBS = [('build', '🛖', 'construir', 'I built a cabin', 'I builded a cabin', 'I build.', 'Eu construo.', 'passado **built**.'),
             ('plant', '🌱', 'plantar', 'Next, I planted beans', 'Next, I plant beans yesterday', 'I plant.', 'Eu planto.', 'passado **planted**.'),
             ('write', '📝', 'escrever', 'Finally, I wrote a book', 'Finally, I writed a book', 'I write.', 'Eu escrevo.', 'passado **wrote**.'),
             ('finish', '🏁', 'terminar', 'Lastly, I finished', 'Lastly, I finish yesterday', 'I finish.', 'Eu termino.', 'passado **finished**.')]
SEQ_MOLD = [('First of all', 'First of all,', 'antes de tudo,', [(' I built a cabin.', ' construí uma cabana.'), (' I made a plan.', ' fiz um plano.'), (' we ate.', ' comemos.')]),
            ('Next', 'Next,', 'depois,', [(' I planted beans.', ' plantei feijão.'), (' we cleaned up.', ' limpamos.'), (' I read a book.', ' li um livro.')]),
            ('Finally', 'Finally,', 'por fim,', [(' I wrote a book.', ' escrevi um livro.'), (' we left.', ' saímos.'), (' it was done.', ' estava pronto.')])]
SEQ_RULE = ('Organizar a fala', 'First, next, finally dão ordem à história.', 'Em português “primeiro… depois… por fim”. Em inglês: **first… next… finally**.')
SEQ_FM = [('Início', 'First of all,', 'I built a cabin.', 'First of all, I built a cabin.', 'abre a lista.'), ('Fim', 'Finally,', 'I wrote a book.', 'Finally, I wrote a book.', 'fecha a lista.')]
SEQ_TRAPS = [('Qual frase está certa?', ['First of all, I built a cabin.', 'First of all I, built a cabin.', 'I first of all, built a cabin.'], 0, 'First of all, + frase.'),
             ('Qual está certa?', ['Finally, I wrote a book.', 'Final, I wrote a book.', 'Finally I, wrote a book.'], 0, 'Finally, + frase.')]

EPS.append(mk(82155, 'First of All', "organizar um texto ou fala com first of all, next, finally e lastly (summary, order)",
    "organizar a fala: first of all · next · finally · lastly", "Hoje você aprende a pôr ordem na fala: First of all, I built a cabin. Next, I planted beans. Finally, I wrote a book.",
    ('Man', 'Woman'), ['tom', 'polly'], 'cafe2', 'Walden', ['cafe2', 'lake', 'park', 'living', 'street', 'hall'],
    ('First of All: em 10 minutos você conta uma história em ordem', 'No café, o homem conta à mulher como viveu perto de um lago.'), ('Mais conectores', 'Próximo: Organizar as ideias'),
    SEQ_RULE, SEQ_FM, SEQ_VOCAB, SEQ_LAB, SEQ_VERBS, SEQ_MOLD,
    ('1️⃣', 'Ordem', 'Use first of all, next e finally', 'Fale. **Diga antes de tudo construí uma cabana, depois plantei feijão e por fim escrevi um livro.**', 'finally', 'First of all, I built a cabin. Next, I planted beans. Finally, I wrote a book.',
     [('Usei first of all?', r"\bfirst\s+of\s+all,?\s+I\b", 'First of all, I built a cabin.', 'Antes de tudo, construí uma cabana.', 'First! 1️⃣'), ('Usei next?', r"\bnext,?\s+I\b", 'Next, I planted beans.', 'Depois, plantei feijão.', 'Next! ➡️'), ('Usei finally?', r"\bfinally,?\s+I\b", 'Finally, I wrote a book.', 'Por fim, escrevi um livro.', 'Finally! 🏁')]),
    ('🔚', 'Fixas', 'Use to begin with, after that e last but not least', 'Fale. **Diga para começar, depois disso e por último mas não menos importante.**', 'last but not least', 'To begin with, I made a plan. After that, I worked. Last but not least, I rested.',
     [('Disse to begin with?', r"\bto\s+begin\s+with\b", 'To begin with, I made a plan.', 'Para começar, fiz um plano.', 'Begin! 1️⃣'), ('Disse after that?', r"\bafter\s+that\b", 'After that, I worked.', 'Depois disso, trabalhei.', 'After! ➡️'), ('Disse last but not least?', r"\blast\s+but\s+not\s+least\b", 'Last but not least, I rested.', 'Por último, mas não menos importante, descansei.', 'Least! 🔚')]),
    [('1️⃣', 'First of all,', 'antes de tudo,', 'First of all, I built a cabin.', 'Antes de tudo, construí uma cabana.'), ('➡️', 'Next,', 'depois,', 'Next, I planted beans.', 'Depois, plantei feijão.'),
     ('🏁', 'Finally,', 'por fim,', 'Finally, I wrote a book.', 'Por fim, escrevi um livro.'), ('🔚', 'Lastly,', 'por último,', 'Lastly, I rested.', 'Por último, descansei.'), ('📝', 'summary', 'resumo', 'Here is a summary.', 'Aqui vai um resumo.')],
    [('___ of all, I built a cabin.', 'Antes de tudo, construí uma cabana.', ['First', 'Firstly of', 'One'], 0, '**First** of all,'), ('___, I planted beans.', 'Depois, plantei feijão.', ['Next', 'Nexts', 'After next'], 0, '**Next**,'),
     ('___, I wrote a book.', 'Por fim, escrevi um livro.', ['Finally', 'Final', 'Finish'], 0, '**Finally**,'), ('___, I rested.', 'Por último, descansei.', ['Lastly', 'Last of', 'Lasted'], 0, '**Lastly**,')],
    SEQ_TRAPS,
    [['Woman', 'Tell me about the lake.', 'Conte-me sobre o lago.'], ['Man', 'First of all, I built a cabin.', 'Antes de tudo, construí uma cabana.'], ['Woman', 'Then?', 'E depois?'], ['Man', 'Next, I planted beans.', 'Depois, plantei feijão.'],
     ['Woman', 'And after that?', 'E depois disso?'], ['Man', 'Finally, I wrote a book.', 'Por fim, escrevi um livro.'], ['Woman', 'What was the last thing?', 'Qual foi a última coisa?'], ['Man', 'Lastly, I rested.', 'Por último, descansei.']],
    [('What did he build first?', 'O que ele construiu primeiro?', [('🛖', 'A cabin'), ('🏰', 'A castle'), ('🚗', 'A car')], 0, 1, 'Diz: “I built a cabin.”'), ('What did he plant?', 'O que ele plantou?', [('🫘', 'Beans'), ('🌽', 'Corn'), ('🍅', 'Tomatoes')], 0, 3, 'Diz: “planted beans.”'),
     ('What did he do last?', 'O que ele fez por último?', [('😴', 'He rested'), ('📖', 'He read'), ('🏃', 'He ran')], 0, 7, 'Diz: “Lastly, I rested.”')],
    [('1️⃣', 'To begin with', 'Para começar', 'abrir', 'To begin with, I made a plan.', 'Para começar, fiz um plano.'), ('➡️', 'After that', 'Depois disso', 'continuar', 'After that, I worked.', 'Depois disso, trabalhei.'),
     ('🔚', 'Last but not least', 'Por último, mas não menos importante', 'fechar', 'Last but not least, I rested.', 'Por último, descansei.'), ('📝', 'In short', 'Em resumo', 'concluir', 'In short, it was good.', 'Em resumo, foi bom.')]))

EPS.append(mk(7082155, 'Organizar as ideias', "organizar a fala na prática: first, next, finally e lastly (summary, order)",
    "dar ordem à história: to begin with · after that · last but not least", "Hoje você pratica to begin with, after that e last but not least: To begin with, I made a plan. After that, I worked.",
    ('Girl', 'Man'), ['polly', 'tom'], 'office', 'Walden', ['office', 'cafe2', 'school', 'hall', 'street', 'park2'],
    ('Organizar as ideias: em 10 minutos você apresenta um plano com clareza', 'No escritório, a menina e o homem montam um resumo em ordem.'), ('Mais conectores', 'Próximo: Pull over'),
    SEQ_RULE, SEQ_FM, SEQ_VOCAB, SEQ_LAB, SEQ_VERBS, SEQ_MOLD,
    ('1️⃣', 'Ordem', 'Use to begin with, after that e last but not least', 'Fale. **Diga para começar fiz um plano, depois disso trabalhei e por último descansei.**', 'to begin with', 'To begin with, I made a plan. After that, I worked. Last but not least, I rested.',
     [('Usei to begin with?', r"\bto\s+begin\s+with,?\s+I\b", 'To begin with, I made a plan.', 'Para começar, fiz um plano.', 'Begin! 1️⃣'), ('Usei after that?', r"\bafter\s+that,?\s+I\b", 'After that, I worked.', 'Depois disso, trabalhei.', 'After! ➡️'), ('Usei last but not least?', r"\blast\s+but\s+not\s+least\b", 'Last but not least, I rested.', 'Por último, descansei.', 'Least! 🔚')]),
    ('📝', 'Fixas', 'Use in short, in the end e all in all', 'Fale. **Diga em resumo, no fim e no geral.**', 'all in all', 'In short, it was good. In the end, we won. All in all, it was fine.',
     [('Disse in short?', r"\bin\s+short\b", 'In short, it was good.', 'Em resumo, foi bom.', 'Short! 📝'), ('Disse in the end?', r"\bin\s+the\s+end\b", 'In the end, we won.', 'No fim, vencemos.', 'End! 🏁'), ('Disse all in all?', r"\ball\s+in\s+all\b", 'All in all, it was fine.', 'No geral, foi bom.', 'All! 🔢')]),
    [('1️⃣', 'To begin with,', 'para começar,', 'To begin with, I made a plan.', 'Para começar, fiz um plano.'), ('➡️', 'After that,', 'depois disso,', 'After that, I worked.', 'Depois disso, trabalhei.'),
     ('🔚', 'Last but not least,', 'por último,', 'Last but not least, I rested.', 'Por último, descansei.'), ('📝', 'summary', 'resumo', 'Write a summary.', 'Escreva um resumo.'), ('🔢', 'order', 'ordem', 'Keep the order.', 'Mantenha a ordem.')],
    [('To begin ___, I made a plan.', 'Para começar, fiz um plano.', ['with', 'in', 'on'], 0, 'To begin **with**,'), ('After ___, I worked.', 'Depois disso, trabalhei.', ['that', 'it is', 'those'], 0, 'After **that**,'),
     ('Last but not ___, I rested.', 'Por último, mas não menos importante, descansei.', ['least', 'last', 'less'], 0, 'Last but not **least**,'), ('Write a ___.', 'Escreva um resumo.', ['summary', 'summarize', 'summing'], 0, 'a **summary**.')],
    SEQ_TRAPS,
    [['Man', 'Give me a summary of your week.', 'Dê-me um resumo da sua semana.'], ['Girl', 'To begin with, I made a plan.', 'Para começar, fiz um plano.'], ['Man', 'And then?', 'E então?'], ['Girl', 'After that, I worked.', 'Depois disso, trabalhei.'],
     ['Man', 'Good order!', 'Boa ordem!'], ['Girl', 'Last but not least, I rested.', 'Por último, descansei.'], ['Man', 'In short, a good week.', 'Em resumo, uma boa semana.'], ['Girl', 'Yes!', 'Sim!']],
    [('What did she make first?', 'O que ela fez primeiro?', [('📋', 'A plan'), ('🍰', 'A cake'), ('🎨', 'A drawing')], 0, 1, 'Diz: “I made a plan.”'), ('What did she do after that?', 'O que ela fez depois?', [('💼', 'She worked'), ('🎮', 'She played'), ('😴', 'She slept')], 0, 3, 'Diz: “I worked.”'),
     ('How was the week?', 'Como foi a semana?', [('👍', 'Good'), ('👎', 'Bad'), ('😐', 'Boring')], 0, 6, 'Diz: “a good week.”')],
    [('1️⃣', 'In short', 'Em resumo', 'concluir', 'In short, it was good.', 'Em resumo, foi bom.'), ('🏁', 'In the end', 'No fim', 'terminar', 'In the end, we won.', 'No fim, vencemos.'),
     ('🔢', 'All in all', 'No geral', 'resumir', 'All in all, it was fine.', 'No geral, foi bom.'), ('📝', 'To sum up', 'Resumindo', 'fechar', 'To sum up, it works.', 'Resumindo, funciona.')]))

# ---------- 237 / 238 · phrasal verbs com pull ----------
PULL_VOCAB = [('🛣️', 'motorway', 'autoestrada', 'Soa como “MÓU-ter-uêi”.'), ('👮', 'officer', 'policial', 'Soa como “Ó-fi-ser”.'), ('🕳️', 'pothole', 'buraco na pista', 'Soa como “PÓT-rôul”.'),
              ('🎫', 'speeding ticket', 'multa por excesso de velocidade', 'Soa como “SPI-ding TÍ-kit”.'), ('🚗', 'traffic jam', 'congestionamento', 'Soa como “TRÉ-fik DJÉM”.'), ('🧳', 'road trip', 'viagem de carro', 'Soa como “RÔUD TRIP”.')]
PULL_LAB = dict(short='pu', title='Laboratório de sons: pull, officer e jam', pt='u soa u curto; o soa ó; j soa dj.', tip='Em pull, o u é curto, como em “pulo”.',
                words=[('pull', 'PUL', 'puxar', 'u = u', 'pool', 'PUUL'), ('officer', 'Ó-fi-ser', 'policial', 'o = ó', 'offer', 'Ó-fer'), ('jam', 'DJÉM', 'congestionamento', 'j = dj', 'gem', 'DJÉM-s')])
PULL_VERBS = [('pull', '🚓', 'encostar', 'Pull over, please.', 'Pull on over, please.', 'I pulled.', 'Eu puxei.', 'pull **over**.'),
              ('pull', '🚗', 'sair', 'He pulled out.', 'He pulled in out.', 'I pull.', 'Eu puxo.', 'pull **out**.'),
              ('stop', '🛑', 'parar', 'We pulled up.', 'We pulled down.', 'I stop.', 'Eu paro.', 'pull **up**.'),
              ('recover', '💪', 'se recuperar', 'She pulled through.', 'She pulled over.', 'I recover.', 'Eu me recupero.', 'pull **through**.')]
PULL_MOLD = [('Pull over', 'Pull over,', 'encoste,', [(' please.', ' por favor.'), (' here.', ' aqui.'), (' now.', ' agora.')]),
             ('Pull out', 'He pulled out', 'ele saiu', [(' of the lot.', ' do estacionamento.'), (' slowly.', ' devagar.'), (' fast.', ' rápido.')]),
             ('Pull up', 'We pulled up', 'nós paramos', [(' at the light.', ' no semáforo.'), (' near the shop.', ' perto da loja.'), (' behind him.', ' atrás dele.')])]

def pull(n, title, sub, pat, why, names, ids, rs, scenes, cover, teaser, rule, fm, hot, gaps, traps, lines, quiz, prod, m2, exps):
    return mk(n, title, sub, pat, why, names, ids, rs, 'Thelma & Louise', scenes, cover, teaser, rule, fm, PULL_VOCAB, PULL_LAB, PULL_VERBS, PULL_MOLD, prod, m2, hot, gaps, traps, lines, quiz, exps)

EPS.append(pull(930034, 'Pull Over, Pull Out', "phrasal verbs com pull: pull over, pull out, pull up e pull through (officer, pothole, speeding ticket)",
    "phrasal verbs: pull over · pull out · pull up · pull through", "Hoje você aprende quatro phrasal verbs com pull: Pull over, please. He pulled out. We pulled up.",
    ('Woman', 'Man'), ['polly', 'tom'], 'street', ['street', 'park2', 'pier', 'lobby1', 'cafe2', 'hall'],
    ('Pull Over, Pull Out: em 10 minutos você dirige em inglês', 'Na estrada, a mulher e o homem são parados por um policial.'), ('Mais com pull', 'Próximo: Na estrada'),
    ('Pull', 'Quatro sentidos novos.', 'Em português “encoste”. Em inglês: **pull over**.'),
    [('Encostar', 'Pull', 'over, please.', 'Pull over, please.', 'pull over.'), ('Sair', 'He pulled', 'out.', 'He pulled out.', 'pull out.')],
    [('🚓', 'pull over', 'encostar', 'Pull over, please.', 'Encoste, por favor.'), ('🚗', 'pull out', 'sair', 'He pulled out.', 'Ele saiu.'), ('🛑', 'pull up', 'parar', 'We pulled up.', 'Nós paramos.'),
     ('💪', 'pull through', 'se recuperar', 'She pulled through.', 'Ela se recuperou.'), ('👮', 'officer', 'policial', 'The officer waved.', 'O policial acenou.')],
    [('Pull ___, please.', 'Encoste, por favor.', ['over', 'in to', 'off to'], 0, 'pull **over**.'), ('He pulled ___.', 'Ele saiu.', ['out', 'over to', 'for'], 0, 'pull **out**.'),
     ('We pulled ___.', 'Nós paramos.', ['up', 'of', 'round to'], 0, 'pull **up**.'), ('She pulled ___.', 'Ela se recuperou.', ['through', 'across to', 'by to'], 0, 'pull **through**.')],
    [('Qual frase está certa?', ['Pull over, please.', 'Pull please over.', 'Pulls over, please.'], 0, 'pull over.'), ('Qual está certa?', ['He pulled out.', 'He pulled outs.', 'He pull out.'], 0, 'pulled out.')],
    [['Man', 'Look! The officer is behind us.', 'Olhe! O policial está atrás de nós.'], ['Woman', 'Pull over, please.', 'Encoste, por favor.'], ['Man', 'I will pull over here.', 'Vou encostar aqui.'], ['Woman', 'Another car pulled out.', 'Outro carro saiu.'],
     ['Man', 'We pulled up near a pothole.', 'Paramos perto de um buraco.'], ['Woman', 'Do not worry. We will pull through.', 'Não se preocupe. Vamos nos recuperar.'], ['Man', 'He gave us a speeding ticket.', 'Ele nos deu uma multa.'], ['Woman', 'It is okay.', 'Tudo bem.']],
    [('Who is behind them?', 'Quem está atrás deles?', [('👮', 'The officer'), ('🐶', 'A dog'), ('👵', 'A woman')], 0, 0, 'Diz: “The officer is behind us.”'), ('What do they get?', 'O que eles recebem?', [('🎫', 'A ticket'), ('🎁', 'A gift'), ('🍕', 'A pizza')], 0, 6, 'Diz: “speeding ticket.”'),
     ('Where did they stop?', 'Onde pararam?', [('🕳️', 'Near a pothole'), ('🏖️', 'At the beach'), ('🏠', 'At home')], 0, 4, 'Diz: “near a pothole.”')],
    ('🚓', 'Pull', 'Use pull over, pull out e pull up', 'Fale. **Diga encoste por favor, ele saiu e nós paramos.**', 'pull over', 'Pull over, please. He pulled out. We pulled up.',
     [('Usei pull over?', r"\bpull\s+over\b", 'Pull over, please.', 'Encoste, por favor.', 'Over! 🚓'), ('Usei pull out?', r"\bpulled\s+out\b", 'He pulled out.', 'Ele saiu.', 'Out! 🚗'), ('Usei pull up?', r"\bpulled\s+up\b", 'We pulled up.', 'Nós paramos.', 'Up! 🛑')]),
    ('💪', 'Fixas', 'Use pull a face, pull your weight e pull strings', 'Fale. **Diga fazer careta, fazer sua parte e mexer os pauzinhos.**', 'pull strings', 'He pulled a face. Pull your weight. She can pull strings.',
     [('Disse pull a face?', r"\bpulled\s+a\s+face\b", 'He pulled a face.', 'Ele fez careta.', 'Face! 😖'), ('Disse pull your weight?', r"\bpull\s+your\s+weight\b", 'Pull your weight.', 'Faça sua parte.', 'Weight! 💪'), ('Disse pull strings?', r"\bpull\s+strings\b", 'She can pull strings.', 'Ela pode mexer os pauzinhos.', 'Strings! 🧵')]),
    [('😖', 'Pull a face.', 'Fazer careta.', 'mostrar desagrado', 'He pulled a face.', 'Ele fez careta.'), ('💪', 'Pull your weight.', 'Fazer sua parte.', 'ajudar igual', 'Pull your weight.', 'Faça sua parte.'),
     ('🧵', 'Pull strings.', 'Mexer os pauzinhos.', 'usar influência', 'She can pull strings.', 'Ela pode mexer os pauzinhos.'), ('🧲', 'Pull a fast one.', 'Passar a perna.', 'enganar', 'He pulled a fast one.', 'Ele passou a perna.')]))

EPS.append(pull(7930034, 'Na estrada', "phrasal verbs com pull: pull over, pull out, pull up e pull through na prática (motorway, traffic jam, road trip)",
    "pull na estrada: pull away · pull in · pull back · pull down", "Hoje você pratica mais quatro com pull: The car pulled away. We pulled in. He pulled back. They pulled down the sign.",
    ('Man', 'Girl'), ['tom', 'polly'], 'street', ['street', 'pier', 'park', 'lobby1', 'hall', 'cafe2'],
    ('Na estrada: em 10 minutos você viaja de carro em inglês', 'Na viagem de carro, o homem e a menina enfrentam o trânsito.'), ('Mais com pull', 'Próximo: Pulling your leg'),
    ('Pull', 'Mais quatro sentidos.', 'Em português “o carro partiu”. Em inglês: **the car pulled away**.'),
    [('Partir', 'The car', 'pulled away.', 'The car pulled away.', 'pull away.'), ('Entrar', 'We', 'pulled in.', 'We pulled in.', 'pull in.')],
    [('🚗', 'pull away', 'partir', 'The car pulled away.', 'O carro partiu.'), ('🅿️', 'pull in', 'estacionar', 'We pulled in.', 'Estacionamos.'), ('↩️', 'pull back', 'recuar', 'He pulled back.', 'Ele recuou.'),
     ('🪧', 'pull down', 'derrubar', 'They pulled down the sign.', 'Eles derrubaram a placa.'), ('🛣️', 'motorway', 'autoestrada', 'The motorway is long.', 'A autoestrada é longa.')],
    [('The car pulled ___.', 'O carro partiu.', ['away', 'at', 'through to'], 0, 'pull **away**.'), ('We pulled ___.', 'Estacionamos.', ['in', 'on to', 'of'], 0, 'pull **in**.'),
     ('He pulled ___.', 'Ele recuou.', ['back', 'for', 'to'], 0, 'pull **back**.'), ('They pulled ___ the sign.', 'Eles derrubaram a placa.', ['down', 'for', 'about'], 0, 'pull **down**.')],
    [('Qual frase está certa?', ['The car pulled away.', 'The car pulled to away.', 'The car pull away.'], 0, 'pulled away.'), ('Qual está certa?', ['We pulled in.', 'We pulled at in.', 'We pull in yesterday.'], 0, 'pulled in.')],
    [['Girl', 'There is a traffic jam on the motorway.', 'Há um congestionamento na autoestrada.'], ['Man', 'The car pulled away fast.', 'O carro partiu rápido.'], ['Girl', 'Pull in here.', 'Estacione aqui.'], ['Man', 'We pulled in near the shop.', 'Estacionamos perto da loja.'],
     ['Girl', 'This road trip is long.', 'Esta viagem é longa.'], ['Man', 'A truck pulled back.', 'Um caminhão recuou.'], ['Girl', 'They pulled down the old sign.', 'Eles derrubaram a placa velha.'], ['Man', 'Let us go.', 'Vamos.']],
    [('Where is the jam?', 'Onde é o congestionamento?', [('🛣️', 'On the motorway'), ('🏖️', 'On the beach'), ('🏠', 'At home')], 0, 0, 'Diz: “jam on the motorway.”'), ('What did the truck do?', 'O que o caminhão fez?', [('↩️', 'Pulled back'), ('🚀', 'Flew'), ('🛑', 'Crashed')], 0, 5, 'Diz: “A truck pulled back.”'),
     ('What did they pull down?', 'O que derrubaram?', [('🪧', 'The sign'), ('🏠', 'The house'), ('🌳', 'The tree')], 0, 6, 'Diz: “pulled down the old sign.”')],
    ('🚗', 'Pull', 'Use pull away, pull in e pull down', 'Fale. **Diga o carro partiu, estacionamos e eles derrubaram a placa.**', 'pull in', 'The car pulled away. We pulled in. They pulled down the sign.',
     [('Usei pull away?', r"\bpulled\s+away\b", 'The car pulled away.', 'O carro partiu.', 'Away! 🚗'), ('Usei pull in?', r"\bpulled\s+in\b", 'We pulled in.', 'Estacionamos.', 'In! 🅿️'), ('Usei pull down?', r"\bpulled\s+down\b", 'They pulled down the sign.', 'Eles derrubaram a placa.', 'Down! 🪧')]),
    ('💪', 'Fixas', 'Use pull yourself together, pull the plug e pull an all-nighter', 'Fale. **Diga se recomponha, desligar tudo e virar a noite.**', 'pull the plug', 'Pull yourself together. They pulled the plug. I pulled an all-nighter.',
     [('Disse pull yourself together?', r"\bpull\s+yourself\s+together\b", 'Pull yourself together.', 'Recomponha-se.', 'Together! 💪'), ('Disse pull the plug?', r"\bpulled\s+the\s+plug\b", 'They pulled the plug.', 'Eles desligaram tudo.', 'Plug! 🔌'), ('Disse an all-nighter?', r"\ball-nighter\b", 'I pulled an all-nighter.', 'Virei a noite.', 'Night! 🌙')]),
    [('💪', 'Pull yourself together.', 'Recomponha-se.', 'se acalmar', 'Pull yourself together.', 'Recomponha-se.'), ('🔌', 'Pull the plug.', 'Desligar tudo.', 'encerrar', 'They pulled the plug.', 'Eles desligaram tudo.'),
     ('🌙', 'Pull an all-nighter.', 'Virar a noite.', 'estudar a noite toda', 'I pulled an all-nighter.', 'Virei a noite.'), ('🎯', 'Pull it off.', 'Conseguir.', 'ter êxito', 'She pulled it off.', 'Ela conseguiu.')]))
