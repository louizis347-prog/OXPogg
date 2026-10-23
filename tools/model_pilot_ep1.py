# Episódio 1 · I'm · Paddington
def cast_(*a):
    return {n: [i, c] for n, i, c in a}


CAST = cast_(('Mrs. Brown', '👩', '#2b6cb0'), ('Paddington', '🐻', '#C0392B'))
LINES = [
    ['Mrs. Brown', 'Hello! You look lost. What is your name?', 'Olá! Você parece perdido. Qual é o seu nome?'],
    ['Paddington', "Hello! I'm Paddington.", 'Olá! Eu sou o Paddington.'],
    ['Mrs. Brown', "Nice to meet you, Paddington. I'm Mary Brown.", 'Prazer, Paddington. Eu sou a Mary Brown.'],
    ['Paddington', "I'm from Peru. I'm a bear.", 'Eu sou do Peru. Eu sou um urso.'],
    ['Mrs. Brown', "I can see! And I'm sure you're hungry.", 'Estou vendo! E tenho certeza de que você está com fome.'],
    ['Paddington', "Yes, I'm a little hungry. And I'm tired.", 'Sim, estou um pouco com fome. E estou cansado.'],
    ['Mrs. Brown', 'Come home with us. We have tea and sandwiches.', 'Venha para casa com a gente. Temos chá e sanduíches.'],
    ['Paddington', "Thank you! I'm very happy.", 'Obrigado! Estou muito feliz.'],
]

EP = dict(
    n=7009801,
    title="Quem é você? · I'm",
    sub="Apresentar-se com I'm: nome, origem e como você está",
    pattern_label="I am → I'm",
    why="Hoje você aprende a se apresentar como o Paddington: I'm + nome, origem e sentimento.",
    vocab=[['Bear', 'Urso', 'Soa como “BÉR”.'], ['Station', 'Estação', 'Soa como “STÊ-chan”.'],
           ['London', 'Londres', 'Soa como “LÂN-dan”.'], ['Hungry', 'Com fome', 'Soa como “RÂN-gri”.'],
           ['Tired', 'Cansado', 'Soa como “TÁI-erd”.'], ['Happy', 'Feliz', 'Soa como “RÉ-pi”.']],
    themes={
        'cultob': ('rainycafe', ['🐻', '🧳', '🚉'], 'b'),
        'rdg': ('busstop', ['🐻', '💬', '🚌'], 'a'),
        'pat': ('bakery', ['🥪', '🐻', '☕'], 'g'),
        'vplay': ('postoffice', ['📮', '🐻', '🧳'], 'h'),
        'sbuild': ('tram', ['🚃', '🐻', '🚉'], 'e'),
        'build': ('library', ['📚', '🐻', '✍️'], 'c'),
        'order': ('terrace', ['☕', '👩', '🐻'], 'f'),
        'balloons': ('balloons', ['🎈', '🐻', '🎈'], 'f'),
        'dictate': ('musicstage', ['🎧', '🐻', '🎶'], 'c'),
        'soundlab': ('lab', ['🔬', '🗣️', '👄'], 'a'),
        'dquiz': ('suburb', ['🏠', '👩', '🐻'], 'd'),
        'cultx': ('colonial', ['📖', '🐻', '🧳'], 'b'),
        'scenebuild': ('kitchen', ['🫖', '🥪', '🐻'], 'g'),
        'produce': ('coffeeshop', ['☕', '🗣️', '🌍'], 'e'),
        'review': ('attic', ['🎒', '🗽', '📦'], 'h'),
        'wrap': ('clocktower', ['🕰️', '🐻', '🏠'], 'd'),
    },
    cover_art={'s': 'station', 'items': [['🐻', 100, 52, 22, 'bob'], ['🧳', 128, 66, 12, 'bob'], ['💬', 112, 30, 12, 'bob']], 'seed': 'pg1'},
    cover_sub="Quem é você? Em 10 minutos você se apresenta como o Paddington",
    cover_say='Um urso chega sozinho à estação de Londres. Alguém pergunta o nome dele. O que ele responde?',
    hook=["Hello! You look lost. What is your name?", 'Olá! Você parece perdido. Qual é o seu nome?'],
    work=dict(
        name='A Bear Called Paddington', chips=['📖 Livro infantil', '1958'], year='1958',
        panels=[
            '“A Bear Called Paddington” é um livro infantil do escritor inglês Michael Bond, publicado em 1958. Um casal, os Brown, encontra um pequeno urso na estação ferroviária de Paddington, em Londres. Ele tem uma etiqueta no pescoço e vem do Peru.',
            'Hoje você vai se apresentar como ele faz no primeiro encontro: “I’m Paddington. I’m from Peru.”'],
        facts=['📖 Michael Bond · 1958', '📍 Londres', '🐻 O urso vem do Peru']),
    rdg_s=[["{{I'm}} Paddington.", 'Eu sou o Paddington.'], ["{{I'm}} from Peru.", 'Eu sou do Peru.'],
           ["{{I'm}} a bear.", 'Eu sou um urso.'], ["{{I'm}} a little hungry.", 'Estou um pouco com fome.']],
    rule="**I'm** é a forma curta de **I am**. Use **I'm** + nome, origem ou como você está: *I'm Ana. I'm from Brazil. I'm tired.*",
    rdg_q={'q': "Qual é a forma curta de “I am”?", 'o': ["I'm", 'I me', 'Im am'], 'a': 0, 'why': "I am → I'm. É assim que se fala no dia a dia."},
    pat_title='Como você se apresenta em inglês?', pat_sub='Nome, origem e como você está.',
    pat_tip="**I'm** + nome / **from** + lugar / **I'm** + como você está.",
    pat_pages=[
        {'label': 'Dizer quem você é', 'slots': [
            {'cat': 'Greeting', 'catpt': 'saudação', 'opts': [['Hi,', 'oi,'], ['Hello,', 'olá,'], ['Hey there,', 'e aí,']]},
            {'cat': 'Pronoun + be', 'catpt': 'eu + ser', 'opts': [["I'm", 'eu sou']]},
            {'cat': 'Name', 'catpt': 'nome', 'opts': [['Paddington', 'Paddington'], ['Mary', 'a Mary'], ['Ana', 'a Ana'], ['Leo', 'o Leo']]}],
         'end': ['.', '.'], 'tip': None},
        {'label': 'Dizer de onde você é', 'slots': [
            {'cat': 'Pronoun + be', 'catpt': 'eu + ser', 'opts': [["I'm from", 'eu sou de']]},
            {'cat': 'Place', 'catpt': 'lugar', 'opts': [['Peru', 'Peru'], ['Brazil', 'Brasil'], ['London', 'Londres'], ['Portugal', 'Portugal']]}],
         'end': ['.', '.'], 'tip': None},
        {'label': 'Dizer como você está', 'slots': [
            {'cat': 'Pronoun + be', 'catpt': 'eu + ser/estar', 'opts': [["I'm", 'eu estou']]},
            {'cat': 'Feeling', 'catpt': 'como você está', 'opts': [['hungry', 'com fome'], ['tired', 'cansado(a)'], ['happy', 'feliz'], ['a little sad', 'um pouco triste']]}],
         'end': ['.', '.'], 'tip': None}],
    vplay=[
        {'v': 'Bear', 'ic': '🐻', 'pt': 'Urso', 'f': [['uso', 'Bear']], 'ex': ["I'm a bear.", 'Eu sou um urso.'], 'note': 'Soa como “BÉR”.'},
        {'v': 'Station', 'ic': '🚉', 'pt': 'Estação', 'f': [['uso', 'Station']], 'ex': ["I'm at the station.", 'Estou na estação.'], 'note': 'Soa como “STÊ-chan”.'},
        {'v': 'Hungry', 'ic': '🥪', 'pt': 'Com fome', 'f': [['uso', 'Hungry']], 'ex': ["I'm hungry.", 'Estou com fome.'], 'note': 'Soa como “RÂN-gri”.'},
        {'v': 'Tired', 'ic': '😴', 'pt': 'Cansado', 'f': [['uso', 'Tired']], 'ex': ["I'm tired.", 'Estou cansado.'], 'note': 'Soa como “TÁI-erd”.'}],
    sbuild=[
        {'tip': 'Todo trem tem um condutor e uma ação.', 'b': [["I'm", 'Quem + ser'], ['Paddington', 'Nome']], 'x': ["You're", 'bear', 'Peru'], 'pt': 'Eu sou o Paddington.', 'end': '.'},
        {'tip': 'Agora entra o vagão do lugar.', 'b': [["I'm", 'Quem + ser'], ['from', 'De onde'], ['Peru', 'Lugar']], 'x': ['am', 'London', 'Brown'], 'pt': 'Eu sou do Peru.', 'end': '.'},
        {'tip': 'Um vagão de sentimento.', 'b': [["I'm", 'Quem + ser'], ['a little', 'Quanto'], ['hungry', 'Como']], 'x': ['you', 'tea', 'bear'], 'pt': 'Estou um pouco com fome.', 'end': '.'},
        {'tip': 'Quatro vagões: saudação, ser, nome, sobrenome.', 'b': [['Hi', 'Saudação'], ["I'm", 'Quem + ser'], ['Mary', 'Nome'], ['Brown', 'Sobrenome']], 'x': ['am', 'Peru'], 'pt': 'Oi, eu sou a Mary Brown.', 'end': '.'}],
    build=[["I'm from Peru", 'Eu sou do Peru'], ["I'm a little hungry", 'Estou um pouco com fome'],
           ["Hi I'm Mary Brown", 'Oi, eu sou a Mary Brown'], ["I'm very happy", 'Estou muito feliz']],
    order_cast=cast_(('Mr. Brown', '👨', '#2b6cb0'), ('Paddington', '🐻', '#C0392B')),
    order_lines=[
        ['Mr. Brown', "Hello! I'm Henry Brown.", 'Olá! Eu sou o Henry Brown.'],
        ['Paddington', "Hello! I'm Paddington.", 'Olá! Eu sou o Paddington.'],
        ['Mr. Brown', 'Where are you from?', 'De onde você é?'],
        ['Paddington', "I'm from Peru.", 'Eu sou do Peru.'],
        ['Mr. Brown', 'Welcome to London!', 'Bem-vindo a Londres!']],
    order_extra=[['Paddington', "I'm from Brazil.", 'Eu sou do Brasil.']],
    balloons_ban=['🐻', '🚉', '🥪', '😴', '🎈'],
    balloons=[['🐻', 'bear'], ['🚉', 'station'], ['🥪', 'hungry'], ['😴', 'tired'], ['😄', 'happy'], ['🇵🇪', 'Peru']],
    clues=[
        {'en': "I'm Paddington. I'm a…", 'pt': 'Eu sou o Paddington. Eu sou um…', 'a': 0, 'why': 'Paddington é um **bear** (urso).', 'hint': 'Ele tem pelo marrom e um chapéu.'},
        {'en': "I'm at Paddington…", 'pt': 'Estou em Paddington…', 'a': 1, 'why': 'Estação = **station**.', 'hint': 'O trem para ali.'},
        {'en': 'I want a sandwich. I’m…', 'pt': 'Quero um sanduíche. Estou…', 'a': 2, 'why': 'Com fome = **hungry**.', 'hint': 'Quem quer comer está…'},
        {'en': "It's late at night. I'm…", 'pt': 'É tarde da noite. Estou…', 'a': 3, 'why': 'Cansado = **tired**.', 'hint': 'Vontade de dormir.'},
        {'en': "I'm from…", 'pt': 'Eu sou do…', 'a': 5, 'why': 'O Paddington é do **Peru**.', 'hint': 'Fica na América do Sul.'}],
    dictate=[["I'm Paddington.", 'Eu sou o Paddington.'], ["I'm from Peru.", 'Eu sou do Peru.'],
             ["I'm a little hungry.", 'Estou um pouco com fome.'], ['Welcome to London!', 'Bem-vindo a Londres!']],
    scene_art={'s': 'station', 'items': [['🐻', 96, 56, 18, 'bob'], ['🧳', 120, 68, 10, 'bob']], 'seed': 'pgs1'},
    cast=CAST, lines=LINES,
    quiz=[
        {'q': 'Where is Paddington from?', 'pt': 'De onde o Paddington é?', 'opts': [['🇵🇪', 'Peru'], ['🇧🇷', 'Brazil'], ['🇬🇧', 'London']], 'a': 0, 'line': 3, 'why': 'Paddington diz: “I’m from Peru.”'},
        {'q': 'How does Paddington feel?', 'pt': 'Como o Paddington se sente?', 'opts': [['🥪', 'Hungry and tired'], ['😄', 'Only happy'], ['😡', 'Angry']], 'a': 0, 'line': 5, 'why': 'Ele diz: “I’m a little hungry. And I’m tired.”'},
        {'q': 'What does Mrs. Brown have at home?', 'pt': 'O que a Sra. Brown tem em casa?', 'opts': [['🫖', 'Tea and sandwiches'], ['🍕', 'Pizza'], ['🍦', 'Ice cream']], 'a': 0, 'line': 6, 'why': 'Ela diz: “We have tea and sandwiches.”'}],
    cultx=[
        {'ic': '💡', 'l': 'Curiosidade', 't': 'O urso foi batizado com o nome da estação onde os Brown o encontraram: Paddington. Ele adora sanduíches de geleia de laranja (marmalade).'},
        {'ic': '🗣️', 'l': 'A etiqueta famosa', 't': 'No pescoço dele há um bilhete: “Please look after this bear. Thank you.” (Por favor, cuide deste urso. Obrigado.)'},
        {'ic': '🌍', 'l': 'E você?', 't': 'Se você chegasse sozinho a um lugar novo, como se apresentaria? Treine: “I’m… I’m from…”.'}],
    sb_items=[['🐻', 'bear'], ['🧳', 'bag'], ['🥪', 'sandwich'], ['🫖', 'tea']],
    sb_spots=[['🚉', 'station'], ['🪑', 'chair'], ['🛏️', 'bed'], ['🏠', 'house']],
    sb_rounds=[
        {'say': ['Put the bear on the chair.'], 'pt': ['Ponha o urso na cadeira.'], 'steps': [[0, 1]], 'items': [0, 3]},
        {'say': ['Put the sandwich in the house.'], 'pt': ['Ponha o sanduíche na casa.'], 'steps': [[2, 3]], 'items': [2, 1]},
        {'say': ['Put the bag on the bed.', 'Then put the tea on the chair.'], 'pt': ['Ponha a mala na cama.', 'Depois ponha o chá na cadeira.'], 'steps': [[1, 2], [3, 1]], 'items': [1, 3, 0]}],
    produce=dict(
        prompt="Você encontra o Paddington e ele pergunta quem é você. **Diga seu nome com I'm, diga de onde você é e como você está.**",
        ph="Ex.: Hi! I'm Ana. I'm from Brazil. I'm a little tired.",
        chips=["Hi! I'm", "I'm from", "I'm a little"],
        model="Hi, Paddington! I'm Ana. I'm from Brazil. I'm a little tired, but happy to meet you.",
        check=["Disse meu nome com I'm?", 'Disse de onde eu sou?', 'Disse como eu estou?'],
        kw=[r"\bI(?:['’]m| am)\s+(?!(?:from|a|an|the|not|very|so|really|fine|good|great|tired|hungry|happy|ok|okay|sleepy|excited|nervous|cold|hot|well|sad|busy)\b)[a-zà-ú]+|\bmy name is\s+\w+",
            r"\bfrom\s+\w+",
            r"\bI(?:['’]m| am)\s+(?:very |so |really |a little |a bit )?(?:fine|good|great|tired|hungry|happy|ok|okay|sleepy|excited|nervous|cold|hot|well|sad|busy)\b|\bnot bad\b"],
        tips=[[["Hi! I'm Ana.", 'Oi! Eu sou a Ana.'], ["Hello, I'm Leo.", 'Olá, eu sou o Leo.']],
              [["I'm from Brazil.", 'Eu sou do Brasil.'], ["I'm from São Paulo.", 'Eu sou de São Paulo.']],
              [["I'm a little tired.", 'Estou um pouco cansada.'], ["I'm so happy to be here!", 'Estou muito feliz de estar aqui!']]],
        ok=['Nome com I\'m! 🙋', 'Você disse de onde é! 🌎', 'E como você está! 😄'],
        reply=["Nice to meet you! I'm Paddington. Come and have some tea!", 'Prazer! Eu sou o Paddington. Venha tomar um chá!']),
    review=dict(
        prev='Hello, New York!', work='The New Colossus',
        recap=[["Hi! I'm Sam. Welcome to New York!", 'Oi! Eu sou o Sam. Bem-vinda a Nova York!'], ['Do you need a taxi?', 'Você precisa de um táxi?'], ["It's my first time in New York!", 'É a minha primeira vez em Nova York!']],
        bag=[{'ic': '🔤', 'l': 'Palavras', 'items': [{'ic': '🔤', 't': 'Hi', 'pt': 'Oi'}, {'ic': '🔤', 't': 'Coffee', 'pt': 'Café'}, {'ic': '🔤', 't': 'Taxi', 'pt': 'Táxi'}, {'ic': '🔤', 't': 'Map', 'pt': 'Mapa'}]},
             {'ic': '💬', 'l': 'Expressões', 'items': [{'ic': '🙂', 't': "How's it going?", 'pt': 'E aí, tudo bem?'}, {'ic': '👍', 't': 'Not bad.', 'pt': 'Nada mal.'}, {'ic': '🙌', 't': 'No problem.', 'pt': 'Sem problema.'}]}]),
    wrap_recap=[["I'm Paddington.", 'Eu sou o Paddington.'], ["I'm from Peru.", 'Eu sou do Peru.'], ["I'm a little hungry.", 'Estou um pouco com fome.'], ["I'm very happy.", 'Estou muito feliz.']],
    teaser={'t': 'Alice no País das Maravilhas', 'd': 'Próximo padrão: perguntas com Are you…?'},
)

EP['rs'] = {'rdg': 'hall', 'pat': 'street', 'vplay': 'cafe3', 'sbuild': 'subway', 'build': 'home1', 'order': 'lobby', 'balloons': 'park2', 'dictate': 'cafe', 'soundlab': 'school', 'scene': 'station', 'dquiz': 'living', 'scenebuild': 'kitchen', 'produce': 'counter', 'review': 'nyc', 'wrap': 'bedroom'}
EP['sc'] = 'station'
