# Episódio 4 · Is he / she / it? · Peter Pan
def cast_(*a):
    return {n: [i, c] for n, i, c in a}


CAST = cast_(('Wendy', '👧', '#2b6cb0'), ('Peter', '🧒', '#2F9E44'))
LINES = [
    ['Wendy', 'Peter, what is that light? Is it a bird?', 'Peter, que luz é aquela? É um pássaro?'],
    ['Peter', "No, it isn't. It's Tinker Bell!", 'Não, não é. É a Sininho!'],
    ['Wendy', 'Is she a fairy?', 'Ela é uma fada?'],
    ['Peter', 'Yes, she is.', 'Sim, ela é.'],
    ['Wendy', 'Is she nice?', 'Ela é legal?'],
    ['Peter', 'Not always! Look at that ship.', 'Nem sempre! Olhe aquele navio.'],
    ['Wendy', "Is it Captain Hook's ship?", 'É o navio do Capitão Gancho?'],
    ['Peter', 'Yes, it is. Is he angry? Probably!', 'Sim, é. Ele está bravo? Provavelmente!'],
]

EP = dict(
    n=7030002,
    title='É ele? É ela? · Is he / she / it?',
    sub='Perguntar sobre uma pessoa ou coisa e responder com Yes, he is / No, it isn\'t',
    pattern_label='Is he…? Is she…? Is it…?',
    why='Hoje você aprende a perguntar sobre ele, ela e isso, como a Wendy na Terra do Nunca.',
    vocab=[['Fairy', 'Fada', 'Soa como “FÉ-ri”.'], ['Ship', 'Navio', 'Soa como “CHIP”.'],
           ['Bird', 'Pássaro', 'Soa como “BÉRD”.'], ['Angry', 'Bravo(a)', 'Soa como “ÉN-gri”.'],
           ['Captain', 'Capitão', 'Soa como “KÉP-tin”.'], ['Light', 'Luz', 'Soa como “LÁIT”.']],
    themes={
        'cultob': ('lighthouse', ['🧒', '🧚', '🏴‍☠️'], 'd'),
        'rdg': ('island', ['🏝️', '🧚', '❓'], 'e'),
        'pat': ('pier', ['⚓', '❓', '🚢'], 'a'),
        'vplay': ('seacliff', ['🧚', '🚢', '⭐'], 'a'),
        'sbuild': ('ship', ['🚢', '🏴‍☠️', '🧒'], 'c'),
        'build': ('cave', ['🗝️', '🧒', '🏴‍☠️'], 'c'),
        'order': ('rooftop', ['🌙', '🧒', '👧'], 'd'),
        'balloons': ('balloons', ['🎈', '🧚', '🎈'], 'f'),
        'dictate': ('observatory', ['🎧', '⭐', '🌙'], 'd'),
        'soundlab': ('lab', ['🔬', '🗣️', '👄'], 'a'),
        'dquiz': ('sunsetbeach', ['🌅', '👧', '🧒'], 'b'),
        'cultx': ('space', ['⭐', '🧒', '🌙'], 'd'),
        'scenebuild': ('underwater', ['🐚', '🧜', '🪸'], 'e'),
        'produce': ('planewin', ['☁️', '🗣️', '❓'], 'a'),
        'review': ('attic', ['🎒', '🧙', '🦁'], 'h'),
        'wrap': ('fireworks', ['🎆', '🧸', '⭐'], 'd'),
    },
    cover_art={'s': 'harbor', 'items': [['🧚', 100, 26, 16, 'bob'], ['🚢', 126, 62, 14, 'bob'], ['❓', 84, 36, 12, 'bob']], 'seed': 'pp1'},
    cover_sub='Is he…? Is she…? Is it…? Em 10 minutos você faz perguntas sobre quem está ao seu redor',
    cover_say='A Wendy vê uma luz brilhando no céu da Terra do Nunca. O que é? Como perguntar?',
    hook=['Is it a bird? Is she a fairy?', 'É um pássaro? Ela é uma fada?'],
    work=dict(
        name='Peter Pan', chips=['🎭 Peça de teatro', '1904'], year='1904',
        panels=[
            '“Peter Pan” é uma peça de teatro do escritor escocês J. M. Barrie, estreada em Londres em 1904. O menino Peter, que não quer crescer, leva Wendy e os irmãos dela para a Terra do Nunca, onde vivem a fada Sininho (Tinker Bell) e o pirata Capitão Gancho.',
            'Na viagem, Wendy faz muitas perguntas sobre o que vê. Hoje você vai fazer o mesmo: “Is she a fairy? Is it a ship?”'],
        facts=['🎭 J. M. Barrie · 1904', '🧚 Sininho (Tinker Bell)', '🏴‍☠️ Capitão Gancho']),
    rdg_s=[['{{Is it}} a bird?', 'É um pássaro?'], ['{{Is she}} a fairy?', 'Ela é uma fada?'],
           ["{{Is it}} Captain Hook's ship?", 'É o navio do Capitão Gancho?'], ['{{Is he}} angry?', 'Ele está bravo?']],
    rule="Para perguntar, o verbo vem primeiro: **He is** → **Is he…?** **She is** → **Is she…?** **It is** → **Is it…?** Resposta curta: **Yes, he is.** / **No, it isn't.**",
    rdg_q={'q': 'Como se pergunta “Ela é uma fada?”', 'o': ['Is she a fairy?', 'She is a fairy?', 'Does she a fairy?'], 'a': 0, 'why': 'O verbo **is** vem antes de **she**.'},
    pat_title='Como perguntar sobre ele, ela e isso?', pat_sub='Pergunte e responda.',
    pat_tip="**Is** + he / she / it + palavra? Resposta: **Yes, he is.** / **No, it isn't.**",
    pat_pages=[
        {'label': 'Perguntar', 'slots': [
            {'cat': 'Question', 'catpt': 'pergunta', 'opts': [['Is he', 'ele é/está'], ['Is she', 'ela é/está'], ['Is it', 'isso é/está']]},
            {'cat': 'Word', 'catpt': 'palavra', 'opts': [['a fairy', 'uma fada'], ['a bird', 'um pássaro'], ['angry', 'bravo(a)'], ["Captain Hook's ship", 'o navio do Capitão Gancho']]}],
         'end': ['?', '?'], 'tip': None},
        {'label': 'Responder', 'slots': [
            {'cat': 'Yes / No', 'catpt': 'sim / não', 'opts': [['Yes,', 'sim,'], ['No,', 'não,']]},
            {'cat': 'Short answer', 'catpt': 'resposta curta', 'opts': [['he is.', 'ele é.'], ['she is.', 'ela é.'], ['it is.', 'é.'], ["he isn't.", 'ele não é.'], ["it isn't.", 'não é.']]}],
         'end': ['', ''], 'tip': None},
        {'label': 'Pergunta e resposta', 'slots': [
            {'cat': 'Ask', 'catpt': 'pergunta', 'opts': [['Is Tinker Bell a fairy?', 'A Sininho é uma fada?'], ['Is Peter Pan a bird?', 'O Peter Pan é um pássaro?'], ['Is the ship big?', 'O navio é grande?']]},
            {'cat': 'Answer', 'catpt': 'resposta', 'opts': [['Yes, she is.', 'Sim, é.'], ["No, he isn't.", 'Não, não é.'], ['Yes, it is.', 'Sim, é.']]}],
         'end': ['', ''], 'tip': None}],
    vplay=[
        {'v': 'Fairy', 'ic': '🧚', 'pt': 'Fada', 'f': [['uso', 'Fairy']], 'ex': ['Is she a fairy?', 'Ela é uma fada?'], 'note': 'Soa como “FÉ-ri”.'},
        {'v': 'Ship', 'ic': '🚢', 'pt': 'Navio', 'f': [['uso', 'Ship']], 'ex': ['Is it a big ship?', 'É um navio grande?'], 'note': 'Soa como “CHIP”.'},
        {'v': 'Bird', 'ic': '🐦', 'pt': 'Pássaro', 'f': [['uso', 'Bird']], 'ex': ['Is it a bird?', 'É um pássaro?'], 'note': 'Soa como “BÉRD”.'},
        {'v': 'Angry', 'ic': '😠', 'pt': 'Bravo', 'f': [['uso', 'Angry']], 'ex': ['Is he angry?', 'Ele está bravo?'], 'note': 'Soa como “ÉN-gri”.'}],
    sbuild=[
        {'tip': 'Na pergunta, o verbo vem primeiro.', 'b': [['Is', 'Verbo'], ['she', 'Quem'], ['a fairy', 'O quê']], 'x': ['are', 'am', 'he'], 'pt': 'Ela é uma fada?', 'end': '?'},
        {'tip': 'Troque o condutor.', 'b': [['Is', 'Verbo'], ['it', 'Quem'], ['a bird', 'O quê']], 'x': ['are', 'she', 'ship'], 'pt': 'É um pássaro?', 'end': '?'},
        {'tip': 'Um vagão de sentimento.', 'b': [['Is', 'Verbo'], ['he', 'Quem'], ['angry', 'Como']], 'x': ['am', 'you', 'ship'], 'pt': 'Ele está bravo?', 'end': '?'},
        {'tip': 'A resposta curta.', 'b': [['Yes', 'Sim'], ['she', 'Quem'], ['is', 'Verbo']], 'x': ["she's", 'are', 'do'], 'pt': 'Sim, ela é.', 'end': '.'}],
    build=[['Is she a fairy', 'Ela é uma fada?'], ['Is it a bird', 'É um pássaro?'], ['Yes she is', 'Sim, ela é'], ["No it isn't", 'Não, não é']],
    order_cast=cast_(('Wendy', '👧', '#2b6cb0'), ('Peter', '🧒', '#2F9E44')),
    order_lines=[
        ['Wendy', 'Look! Is that a ship?', 'Olhe! Aquilo é um navio?'],
        ['Peter', 'Yes, it is. Captain Hook is there.', 'Sim, é. O Capitão Gancho está lá.'],
        ['Wendy', 'Is he angry?', 'Ele está bravo?'],
        ['Peter', 'Yes, he is! Very angry.', 'Sim, está! Muito bravo.'],
        ['Wendy', 'Is it far from here?', 'Fica longe daqui?']],
    order_extra=[['Peter', 'Yes, she is.', 'Sim, ela é.']],
    balloons_ban=['🧚', '🚢', '⭐', '🧒', '❓'],
    balloons=[['🧚', 'fairy'], ['🚢', 'ship'], ['🐦', 'bird'], ['😠', 'angry'], ['⚓', 'captain'], ['💡', 'light']],
    clues=[
        {'en': 'Tinker Bell is small and she has wings. She’s a…', 'pt': 'A Sininho é pequena e tem asas. Ela é uma…', 'a': 0, 'why': 'Fada = **fairy**.', 'hint': 'Ela brilha.'},
        {'en': 'Captain Hook is on a big…', 'pt': 'O Capitão Gancho está em um grande…', 'a': 1, 'why': 'Navio = **ship**.', 'hint': 'Navega pelo mar.'},
        {'en': 'It has wings and it flies, but it is not a plane. It’s a…', 'pt': 'Tem asas e voa, mas não é um avião. É um…', 'a': 2, 'why': 'Pássaro = **bird**.', 'hint': 'Canta nas árvores.'},
        {'en': 'His face is red. He shouts. He is…', 'pt': 'O rosto dele está vermelho. Ele grita. Ele está…', 'a': 3, 'why': 'Bravo = **angry**.', 'hint': 'Grrr!'}],
    dictate=[['Is she a fairy?', 'Ela é uma fada?'], ['Yes, she is.', 'Sim, ela é.'],
             ["No, it isn't.", 'Não, não é.'], ['Is he angry?', 'Ele está bravo?']],
    scene_art={'s': 'harbor', 'items': [['🧒', 92, 50, 16, 'bob'], ['🧚', 126, 30, 12, 'bob'], ['🚢', 150, 66, 14, 'bob']], 'seed': 'pps1'},
    cast=CAST, lines=LINES,
    quiz=[
        {'q': 'Is the light a bird?', 'pt': 'A luz é um pássaro?', 'opts': [['❌', "No, it isn't"], ['✅', 'Yes, it is'], ['🤷', 'Maybe']], 'a': 0, 'line': 1, 'why': 'Peter diz: “No, it isn’t. It’s Tinker Bell!”'},
        {'q': 'What is Tinker Bell?', 'pt': 'O que é a Sininho?', 'opts': [['🧚', 'A fairy'], ['🐦', 'A bird'], ['👧', 'A girl']], 'a': 0, 'line': 3, 'why': 'Peter diz: “Yes, she is.”'},
        {'q': 'Whose ship is it?', 'pt': 'De quem é o navio?', 'opts': [['🏴‍☠️', "Captain Hook's"], ['🧒', "Peter's"], ['👧', "Wendy's"]], 'a': 0, 'line': 6, 'why': 'Wendy pergunta e Peter responde: “Yes, it is.”'}],
    cultx=[
        {'ic': '💡', 'l': 'Curiosidade', 't': 'J. M. Barrie escreveu a peça para o teatro, e ela estreou em Londres em 1904. Depois ele transformou a história em livro, publicado em 1911.'},
        {'ic': '🗣️', 'l': 'Personagens', 't': 'A fada Tinker Bell não fala: ela “conversa” com sininhos. Já o Capitão Gancho tem uma mão de gancho e é o grande inimigo do Peter.'},
        {'ic': '🌍', 'l': 'E você?', 't': 'Olhe ao seu redor agora. Faça uma pergunta com Is he…? Is she…? ou Is it…? sobre algo ou alguém.'}],
    sb_items=[['🧚', 'fairy'], ['🚢', 'ship'], ['⭐', 'star'], ['🗝️', 'key']],
    sb_spots=[['☁️', 'cloud'], ['🌊', 'sea'], ['🌳', 'tree'], ['🪑', 'chair']],
    sb_rounds=[
        {'say': ['Put the fairy on the cloud.'], 'pt': ['Ponha a fada na nuvem.'], 'steps': [[0, 0]], 'items': [0, 3]},
        {'say': ['Put the ship in the sea.'], 'pt': ['Ponha o navio no mar.'], 'steps': [[1, 1]], 'items': [1, 2]},
        {'say': ['Put the star on the tree.', 'Then put the key on the chair.'], 'pt': ['Ponha a estrela na árvore.', 'Depois ponha a chave na cadeira.'], 'steps': [[2, 2], [3, 3]], 'items': [2, 3, 0]}],
    produce=dict(
        prompt='Você vê uma foto misteriosa. **Faça três perguntas curtas: uma com Is he…?, uma com Is she…? e uma com Is it…?**',
        ph='Ex.: Is he a pirate? Is she a fairy? Is it a ship?',
        chips=['Is he…?', 'Is she…?', 'Is it…?'],
        model="Is he a pirate? Is she a fairy? Is it a big ship? Yes, it is!",
        check=['Fiz uma pergunta com Is he…?', 'Fiz uma pergunta com Is she…?', 'Fiz uma pergunta com Is it…?'],
        kw=[r"\bis he\b[^.!?]*\?", r"\bis she\b[^.!?]*\?", r"\bis it\b[^.!?]*\?"],
        tips=[[['Is he a pirate?', 'Ele é um pirata?'], ['Is he angry?', 'Ele está bravo?']],
              [['Is she a fairy?', 'Ela é uma fada?'], ['Is she nice?', 'Ela é legal?']],
              [['Is it a bird?', 'É um pássaro?'], ['Is it a big ship?', 'É um navio grande?']]],
        ok=['Pergunta sobre ele! 🧒', 'Pergunta sobre ela! 👧', 'Pergunta sobre a coisa! 🚢'],
        reply=["Good questions! The answers are: yes, he is; yes, she is; and yes, it is!", 'Boas perguntas! As respostas são: sim, ele é; sim, ela é; e sim, é!']),
    review=dict(
        prev="Quem é ele? Quem é ela? · He's / She's", work='The Wizard of Oz',
        recap=[["She's Glinda. She's the Good Witch.", 'Ela é a Glinda. Ela é a Bruxa Boa.'], ["He's the Wizard.", 'Ele é o Mágico.'], ["He's a little scared, but he's kind.", 'Ele está um pouco assustado, mas é gentil.']],
        bag=[{'ic': '🔤', 'l': 'Palavras', 'items': [{'ic': '🧙‍♀️', 't': 'Witch', 'pt': 'Bruxa'}, {'ic': '🧙', 't': 'Wizard', 'pt': 'Mágico'}, {'ic': '🦁', 't': 'Lion', 'pt': 'Leão'}, {'ic': '💚', 't': 'Kind', 'pt': 'Gentil'}]},
             {'ic': '💬', 'l': 'Expressões', 'items': [{'ic': '👩', 't': "She's Glinda.", 'pt': 'Ela é a Glinda.'}, {'ic': '👨', 't': "He's the Wizard.", 'pt': 'Ele é o Mágico.'}, {'ic': '🏠', 't': 'There is no place like home.', 'pt': 'Não há lugar como o nosso lar.'}]}]),
    wrap_recap=[['Is she a fairy?', 'Ela é uma fada?'], ['Yes, she is.', 'Sim, ela é.'], ["No, it isn't.", 'Não, não é.'], ['Is he angry?', 'Ele está bravo?']],
    teaser={'t': 'Toy Story', 'd': 'Próximo padrão: plural com -s e -ies'},
)

EP['rs'] = {'rdg': 'lake', 'pat': 'park', 'vplay': 'bedroom', 'sbuild': 'park2', 'build': 'hall', 'order': 'living', 'balloons': 'flags', 'dictate': 'home1', 'soundlab': 'school', 'scene': 'pier', 'dquiz': 'yard', 'scenebuild': 'kitchen', 'produce': 'street', 'review': 'cafe3', 'wrap': 'lobby'}
EP['sc'] = 'harbor'
