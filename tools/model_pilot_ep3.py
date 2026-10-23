# Episódio 3 · He's / She's · O Mágico de Oz
def cast_(*a):
    return {n: [i, c] for n, i, c in a}


CAST = cast_(('Scarecrow', '🧑‍🌾', '#B7791F'), ('Dorothy', '👧', '#2b6cb0'))
LINES = [
    ['Scarecrow', 'Dorothy, who is that woman?', 'Dorothy, quem é aquela mulher?'],
    ['Dorothy', "She's Glinda. She's the Good Witch.", 'Ela é a Glinda. Ela é a Bruxa Boa.'],
    ['Scarecrow', 'And who is that man?', 'E quem é aquele homem?'],
    ['Dorothy', "He's the Wizard. He's in the Emerald City.", 'Ele é o Mágico. Ele está na Cidade das Esmeraldas.'],
    ['Scarecrow', 'And the lion?', 'E o leão?'],
    ['Dorothy', "He's a little scared, but he's kind.", 'Ele está um pouco assustado, mas é gentil.'],
    ['Scarecrow', 'And you, Dorothy?', 'E você, Dorothy?'],
    ['Dorothy', "I'm from Kansas. There's no place like home!", 'Eu sou do Kansas. Não há lugar como o nosso lar!'],
]

EP = dict(
    n=7030001,
    title="Quem é ele? Quem é ela? · He's / She's",
    sub="Falar de outras pessoas com He's e She's",
    pattern_label="He is → He's · She is → She's",
    why="Hoje você aprende a falar de outras pessoas como a Dorothy: He's e She's.",
    vocab=[['Witch', 'Bruxa', 'Soa como “UÍTCH”.'], ['Wizard', 'Mágico', 'Soa como “UÍ-zerd”.'],
           ['Lion', 'Leão', 'Soa como “LÁI-an”.'], ['Kind', 'Gentil', 'Soa como “KÁIND”.'],
           ['Scared', 'Assustado', 'Soa como “SKÉRD”.'], ['Home', 'Lar / casa', 'Soa como “RÔUM”.']],
    themes={
        'cultob': ('pampa', ['🌪️', '👧', '🌈'], 'b'),
        'rdg': ('windmill', ['🌾', '🧑‍🌾', '💬'], 'g'),
        'pat': ('canyon', ['🦁', '🤖', '🌈'], 'b'),
        'vplay': ('castle', ['🧙', '🏰', '🔮'], 'e'),
        'sbuild': ('roadtrip', ['🛣️', '👧', '🐕'], 'a'),
        'build': ('barn', ['🏠', '🌾', '👧'], 'g'),
        'order': ('campfire', ['🔥', '🧑‍🌾', '👧'], 'f'),
        'balloons': ('balloons', ['🎈', '🦁', '🎈'], 'e'),
        'dictate': ('musicstage', ['🎧', '🌈', '🎶'], 'c'),
        'soundlab': ('lab', ['🔬', '🗣️', '👄'], 'a'),
        'dquiz': ('olivegrove', ['🌳', '👧', '🧑‍🌾'], 'e'),
        'cultx': ('cathedral', ['💚', '🏙️', '🧙'], 'e'),
        'scenebuild': ('vineyard', ['🌈', '🐕', '👠'], 'f'),
        'produce': ('terrace', ['👨‍👩‍👧', '🗣️', '📷'], 'b'),
        'review': ('attic', ['🎒', '🐇', '🐻'], 'h'),
        'wrap': ('observatory', ['🔭', '🧚', '⭐'], 'd'),
    },
    cover_art={'s': 'park', 'items': [['🌈', 100, 30, 20, 'bob'], ['🐕', 120, 70, 12, 'bob'], ['👧', 84, 64, 16, 'bob']], 'seed': 'oz1'},
    cover_sub="He's e She's: em 10 minutos você apresenta seus amigos como a Dorothy",
    cover_say='A Dorothy chega a Oz e conhece vários personagens. Como falar de cada um deles?',
    hook=["She's Glinda. She's the Good Witch.", 'Ela é a Glinda. Ela é a Bruxa Boa.'],
    work=dict(
        name='The Wizard of Oz', chips=['🎬 Filme', '1939'], year='1939',
        panels=[
            '“The Wizard of Oz” é um filme musical americano de 1939, baseado no livro de L. Frank Baum de 1900. A menina Dorothy, interpretada por Judy Garland, é levada por um tornado do Kansas para a terra mágica de Oz. Lá ela conhece o Espantalho, o Homem de Lata e o Leão.',
            'Hoje você vai falar desses personagens como a Dorothy faz: “He’s the Scarecrow. She’s Glinda.”'],
        facts=['🎬 Filme de 1939', '📖 Livro de L. Frank Baum', '🌈 “Over the Rainbow”']),
    rdg_s=[["{{She's}} Glinda.", 'Ela é a Glinda.'], ["{{He's}} the Wizard.", 'Ele é o Mágico.'],
           ["{{He's}} a little scared.", 'Ele está um pouco assustado.'], ["{{She's}} the Good Witch.", 'Ela é a Bruxa Boa.']],
    rule="Para **ele**, use **He's** (He is). Para **ela**, use **She's** (She is). *He's a lion. She's a witch.*",
    rdg_q={'q': "Como se diz “Ela é a Glinda”?", 'o': ["She's Glinda.", "He's Glinda.", "I'm Glinda."], 'a': 0, 'why': 'Ela → **She\'s**.'},
    pat_title='Como falar de outra pessoa?', pat_sub='Ele e ela.',
    pat_tip="**He's** = ele é / está. **She's** = ela é / está.",
    pat_pages=[
        {'label': 'Dizer quem é', 'slots': [
            {'cat': 'Who', 'catpt': 'quem', 'opts': [["He's", 'ele é'], ["She's", 'ela é']]},
            {'cat': 'Name', 'catpt': 'nome', 'opts': [['Glinda', 'a Glinda'], ['the Wizard', 'o Mágico'], ['the Scarecrow', 'o Espantalho'], ['Dorothy', 'a Dorothy']]}],
         'end': ['.', '.'], 'tip': None},
        {'label': 'Dizer como é', 'slots': [
            {'cat': 'Who', 'catpt': 'quem', 'opts': [["He's", 'ele é'], ["She's", 'ela é']]},
            {'cat': 'Feeling', 'catpt': 'como é', 'opts': [['kind', 'gentil'], ['brave', 'corajoso(a)'], ['scared', 'assustado(a)'], ['happy', 'feliz']]}],
         'end': ['.', '.'], 'tip': None},
        {'label': 'Dizer de onde é', 'slots': [
            {'cat': 'Who', 'catpt': 'quem', 'opts': [["He's", 'ele é'], ["She's", 'ela é']]},
            {'cat': 'From', 'catpt': 'de onde', 'opts': [['from Kansas', 'do Kansas'], ['from Oz', 'de Oz'], ['in the Emerald City', 'na Cidade das Esmeraldas']]}],
         'end': ['.', '.'], 'tip': None}],
    vplay=[
        {'v': 'Witch', 'ic': '🧙‍♀️', 'pt': 'Bruxa', 'f': [['uso', 'Witch']], 'ex': ["She's a witch.", 'Ela é uma bruxa.'], 'note': 'Soa como “UÍTCH”.'},
        {'v': 'Wizard', 'ic': '🧙', 'pt': 'Mágico', 'f': [['uso', 'Wizard']], 'ex': ["He's the Wizard.", 'Ele é o Mágico.'], 'note': 'Soa como “UÍ-zerd”.'},
        {'v': 'Lion', 'ic': '🦁', 'pt': 'Leão', 'f': [['uso', 'Lion']], 'ex': ["He's a lion.", 'Ele é um leão.'], 'note': 'Soa como “LÁI-an”.'},
        {'v': 'Kind', 'ic': '💚', 'pt': 'Gentil', 'f': [['uso', 'Kind']], 'ex': ["She's kind.", 'Ela é gentil.'], 'note': 'Soa como “KÁIND”.'}],
    sbuild=[
        {'tip': 'Troque o condutor: he ou she.', 'b': [["She's", 'Quem'], ['the', 'Artigo'], ['Good Witch', 'O quê']], 'x': ["He's", 'am', 'lion'], 'pt': 'Ela é a Bruxa Boa.', 'end': '.'},
        {'tip': 'Agora ele.', 'b': [["He's", 'Quem'], ['the', 'Artigo'], ['Wizard', 'O quê']], 'x': ["She's", 'is', 'Glinda'], 'pt': 'Ele é o Mágico.', 'end': '.'},
        {'tip': 'Um vagão de sentimento.', 'b': [["He's", 'Quem'], ['a little', 'Quanto'], ['scared', 'Como']], 'x': ["She's", 'brave', 'home'], 'pt': 'Ele está um pouco assustado.', 'end': '.'},
        {'tip': 'Um vagão de lugar.', 'b': [["He's", 'Quem'], ['in', 'Onde'], ['the Emerald City', 'Lugar']], 'x': ['am', 'Kansas'], 'pt': 'Ele está na Cidade das Esmeraldas.', 'end': '.'}],
    build=[["She's the Good Witch", 'Ela é a Bruxa Boa'], ["He's a little scared", 'Ele está um pouco assustado'],
           ["He's in the Emerald City", 'Ele está na Cidade das Esmeraldas'], ["She's kind", 'Ela é gentil']],
    order_cast=cast_(('Lion', '🦁', '#B7791F'), ('Dorothy', '👧', '#2b6cb0')),
    order_lines=[
        ['Lion', 'Dorothy, who is that girl?', 'Dorothy, quem é aquela menina?'],
        ['Dorothy', "She's Glinda. She's kind.", 'Ela é a Glinda. Ela é gentil.'],
        ['Lion', 'And who is that man?', 'E quem é aquele homem?'],
        ['Dorothy', "He's the Scarecrow. He's my friend.", 'Ele é o Espantalho. Ele é meu amigo.'],
        ['Lion', 'Oh! Hello, Scarecrow!', 'Ah! Olá, Espantalho!']],
    order_extra=[['Lion', "She's the Scarecrow.", 'Ela é o Espantalho.']],
    balloons_ban=['🦁', '🧙', '🌈', '🏰', '💚'],
    balloons=[['🧙‍♀️', 'witch'], ['🧙', 'wizard'], ['🦁', 'lion'], ['💚', 'kind'], ['😨', 'scared'], ['🏠', 'home']],
    clues=[
        {'en': "She's Glinda. She's a good…", 'pt': 'Ela é a Glinda. Ela é uma boa…', 'a': 0, 'why': 'Bruxa = **witch**.', 'hint': 'Ela usa uma coroa.'},
        {'en': "He's in the Emerald City. He's the…", 'pt': 'Ele está na Cidade das Esmeraldas. Ele é o…', 'a': 1, 'why': 'Mágico = **wizard**.', 'hint': 'Ele faz mágica.'},
        {'en': "He's a big cat with a mane. He's a…", 'pt': 'Ele é um gato grande com juba. Ele é um…', 'a': 2, 'why': 'Leão = **lion**.', 'hint': 'O rei da selva.'},
        {'en': "Dorothy says: There's no place like…", 'pt': 'Dorothy diz: Não há lugar como o…', 'a': 5, 'why': 'Lar = **home**.', 'hint': 'Onde moramos.'}],
    dictate=[["She's Glinda.", 'Ela é a Glinda.'], ["He's the Wizard.", 'Ele é o Mágico.'],
             ["He's a little scared.", 'Ele está um pouco assustado.'], ["She's kind.", 'Ela é gentil.']],
    scene_art={'s': 'park', 'items': [['🧑‍🌾', 92, 56, 18, 'bob'], ['🦁', 128, 62, 14, 'bob'], ['🌈', 110, 22, 16, 'bob']], 'seed': 'ozs1'},
    cast=CAST, lines=LINES,
    quiz=[
        {'q': 'Who is Glinda?', 'pt': 'Quem é a Glinda?', 'opts': [['🧙‍♀️', 'The Good Witch'], ['🧙', 'The Wizard'], ['🦁', 'The Lion']], 'a': 0, 'line': 1, 'why': 'Dorothy diz: “She’s the Good Witch.”'},
        {'q': 'Where is the Wizard?', 'pt': 'Onde está o Mágico?', 'opts': [['🏙️', 'In the Emerald City'], ['🌾', 'In Kansas'], ['🏠', 'At home']], 'a': 0, 'line': 3, 'why': 'Dorothy diz: “He’s in the Emerald City.”'},
        {'q': 'How is the Lion?', 'pt': 'Como está o Leão?', 'opts': [['😨', 'A little scared'], ['😡', 'Angry'], ['😴', 'Sleepy']], 'a': 0, 'line': 5, 'why': 'Dorothy diz: “He’s a little scared.”'}],
    cultx=[
        {'ic': '💡', 'l': 'Curiosidade', 't': 'No filme, a casa de Dorothy no Kansas é mostrada em tons de sépia (marrom). Quando ela chega a Oz, tudo ganha cor com a tecnologia Technicolor.'},
        {'ic': '🗣️', 'l': 'Frase famosa', 't': '“There’s no place like home.” (Não há lugar como o nosso lar.) É a frase que a Dorothy repete para voltar para casa.'},
        {'ic': '🌍', 'l': 'E você?', 't': 'Pense em duas pessoas que você conhece. Como você diria quem elas são com He’s e She’s?'}],
    sb_items=[['🐕', 'dog'], ['👠', 'shoes'], ['🌈', 'rainbow'], ['🏠', 'house']],
    sb_spots=[['🪑', 'chair'], ['🛏️', 'bed'], ['🌳', 'tree'], ['🚪', 'door']],
    sb_rounds=[
        {'say': ['Put the dog on the bed.'], 'pt': ['Ponha o cachorro na cama.'], 'steps': [[0, 1]], 'items': [0, 3]},
        {'say': ['Put the shoes at the door.'], 'pt': ['Ponha os sapatos na porta.'], 'steps': [[1, 3]], 'items': [1, 2]},
        {'say': ['Put the house on the tree.', 'Then put the dog on the chair.'], 'pt': ['Ponha a casa na árvore.', 'Depois ponha o cachorro na cadeira.'], 'steps': [[3, 2], [0, 0]], 'items': [3, 0, 1]}],
    produce=dict(
        prompt='Você mostra uma foto da sua família ou de amigos. **Fale de duas pessoas: use He\'s e She\'s para dizer quem são e como são.**',
        ph="Ex.: He's Leo. He's my brother. She's Ana. She's kind.",
        chips=["He's", "She's", 'my friend'],
        model="He's Leo. He's my brother. He's funny. She's Ana. She's my friend. She's from Brazil.",
        check=["Falei de um homem com He's?", "Falei de uma mulher com She's?", 'Disse quem é ou como é?'],
        kw=[r"\bhe(?:['’]s| is)\b", r"\bshe(?:['’]s| is)\b",
            r"\b(?:he|she)(?:['’]s| is)\s+(?:my|from|a|an|the|kind|nice|funny|brave|tall|happy|tired|smart|friendly)\b"],
        tips=[[["He's Leo.", 'Ele é o Leo.'], ["He's my friend.", 'Ele é meu amigo.']],
              [["She's Ana.", 'Ela é a Ana.'], ["She's my sister.", 'Ela é minha irmã.']],
              [["He's kind.", 'Ele é gentil.'], ["She's from Brazil.", 'Ela é do Brasil.']]],
        ok=['Falou dele! 👨', 'Falou dela! 👩', 'Ótimo: quem e como! 🌟'],
        reply=["Nice! They're your friends. They're lucky to have you!", 'Legal! São seus amigos. Eles têm sorte de ter você!']),
    review=dict(
        prev='Quem está aí? · Are you…?', work="Alice's Adventures in Wonderland",
        recap=[['Are you in a hurry?', 'Você está com pressa?'], ['Yes, I am.', 'Sim, estou.'], ["No, I'm not.", 'Não, não estou.']],
        bag=[{'ic': '🔤', 'l': 'Palavras', 'items': [{'ic': '⏰', 't': 'Late', 'pt': 'Atrasado'}, {'ic': '🧭', 't': 'Lost', 'pt': 'Perdido'}, {'ic': '🆕', 't': 'New', 'pt': 'Novo(a)'}, {'ic': '🏃', 't': 'Hurry', 'pt': 'Pressa'}]},
             {'ic': '💬', 'l': 'Expressões', 'items': [{'ic': '❓', 't': 'Are you lost?', 'pt': 'Você está perdida?'}, {'ic': '✅', 't': 'Yes, I am.', 'pt': 'Sim, estou.'}, {'ic': '❌', 't': "No, I'm not.", 'pt': 'Não, não estou.'}]}]),
    wrap_recap=[["She's Glinda.", 'Ela é a Glinda.'], ["He's the Wizard.", 'Ele é o Mágico.'], ["He's a little scared.", 'Ele está um pouco assustado.'], ["She's the Good Witch.", 'Ela é a Bruxa Boa.']],
    teaser={'t': 'Peter Pan', 'd': 'Próximo padrão: perguntas com Is he…? Is she…? Is it…?'},
)

EP['rs'] = {'rdg': 'yard', 'pat': 'park2', 'vplay': 'hall', 'sbuild': 'street', 'build': 'home1', 'order': 'park', 'balloons': 'flags', 'dictate': 'living', 'soundlab': 'school', 'scene': 'lake', 'dquiz': 'pier', 'scenebuild': 'kitchen', 'produce': 'cafe2', 'review': 'cafe3', 'wrap': 'bedroom'}
EP['sc'] = 'park'
