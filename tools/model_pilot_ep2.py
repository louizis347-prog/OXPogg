# Episódio 2 · Are you…? · Alice
def cast_(*a):
    return {n: [i, c] for n, i, c in a}


CAST = cast_(('Alice', '👧', '#2b6cb0'), ('Rabbit', '🐰', '#C0392B'), ('Cat', '🐱', '#7C4DFF'))
LINES = [
    ['Rabbit', "Oh dear! I'm late!", 'Meu Deus! Estou atrasado!'],
    ['Alice', 'Wait! Are you in a hurry?', 'Espere! Você está com pressa?'],
    ['Rabbit', 'Yes, I am! Are you new here?', 'Sim, estou! Você é nova aqui?'],
    ['Alice', "Yes, I am. I'm Alice.", 'Sim, sou. Eu sou a Alice.'],
    ['Cat', 'Hello, Alice! Are you lost?', 'Olá, Alice! Você está perdida?'],
    ['Alice', "No, I'm not. Are you a cat?", 'Não, não estou. Você é um gato?'],
    ['Cat', "Yes, I am. And we're all mad here!", 'Sim, sou. E aqui somos todos loucos!'],
    ['Alice', "Then I'm in the right place!", 'Então estou no lugar certo!'],
]

EP = dict(
    n=7070001,
    title='Quem está aí? · Are you…?',
    sub='Fazer perguntas com Are you…? e responder com Yes, I am / No, I\'m not',
    pattern_label='Are you…?',
    why='Hoje você aprende a perguntar como a Alice: Are you…? e a responder com Yes, I am / No, I\'m not.',
    vocab=[['Late', 'Atrasado', 'Soa como “LÊIT”.'], ['Hurry', 'Pressa', 'Soa como “RÂ-ri”.'],
           ['New', 'Novo(a)', 'Soa como “NIÚ”.'], ['Lost', 'Perdido(a)', 'Soa como “LÓST”.'],
           ['Cat', 'Gato', 'Soa como “KÉT”.'], ['Rabbit', 'Coelho', 'Soa como “RÉ-bit”.']],
    themes={
        'cultob': ('library', ['🐇', '📖', '⏰'], 'c'),
        'rdg': ('greenhouse', ['🌷', '🐇', '❓'], 'e'),
        'pat': ('treehouse', ['🐱', '❓', '🌳'], 'e'),
        'vplay': ('clocktower', ['⏰', '🐇', '🕰️'], 'g'),
        'sbuild': ('circus', ['🎪', '🐱', '🎩'], 'f'),
        'build': ('attic', ['🔑', '🚪', '🐇'], 'h'),
        'order': ('picnic', ['🫖', '🐇', '👧'], 'b'),
        'balloons': ('balloons', ['🎈', '🐇', '🎈'], 'c'),
        'dictate': ('theatre', ['🎭', '🎧', '🐱'], 'c'),
        'soundlab': ('lab', ['🔬', '🗣️', '👄'], 'a'),
        'dquiz': ('castle', ['🏰', '👧', '🐇'], 'f'),
        'cultx': ('cave', ['🐰', '🕳️', '📖'], 'c'),
        'scenebuild': ('kitchen', ['🫖', '🍰', '🐱'], 'g'),
        'produce': ('terrace', ['🫖', '🗣️', '❓'], 'b'),
        'review': ('attic', ['🎒', '🐻', '🧳'], 'h'),
        'wrap': ('observatory', ['🔭', '🧙', '⭐'], 'd'),
    },
    cover_art={'s': 'park', 'items': [['🐇', 104, 56, 20, 'bob'], ['⏰', 138, 44, 12, 'bob'], ['❓', 84, 34, 12, 'bob']], 'seed': 'al1'},
    cover_sub='Are you…? Em 10 minutos você faz perguntas como a Alice',
    cover_say='A Alice vê um coelho correndo com um relógio. Ela quer saber: ele está com pressa? Como perguntar?',
    hook=['Wait! Are you in a hurry?', 'Espere! Você está com pressa?'],
    work=dict(
        name="Alice's Adventures in Wonderland", chips=['📖 Livro', '1865'], year='1865',
        panels=[
            '“Alice’s Adventures in Wonderland” é um livro do inglês Lewis Carroll, publicado em 1865. Lewis Carroll é o nome de escritor de Charles Dodgson, que também era professor de matemática. A menina Alice segue um coelho branco, cai em uma toca e chega a um mundo cheio de personagens estranhos.',
            'Alice faz muitas perguntas durante a história. Hoje você vai fazer o mesmo, com Are you…?'],
        facts=['📖 Lewis Carroll · 1865', '🐇 O Coelho Branco', '🐱 O Gato de Cheshire']),
    rdg_s=[['{{Are you}} in a hurry?', 'Você está com pressa?'], ['{{Are you}} new here?', 'Você é nova aqui?'],
           ['{{Are you}} lost?', 'Você está perdida?'], ['{{Are you}} a cat?', 'Você é um gato?']],
    rule='Para perguntar, inverta: **You are** → **Are you…?** Responda curto: **Yes, I am.** ou **No, I\'m not.** (Não use *I\'m* no “Yes”.)',
    rdg_q={'q': 'Qual é a resposta curta certa para “Are you new here?”', 'o': ['Yes, I am.', "Yes, I'm.", 'Yes, I do.'], 'a': 0, 'why': 'Na resposta curta afirmativa, use **Yes, I am.** (nunca “Yes, I’m”).'},
    pat_title='Como perguntar com Are you…?', pat_sub='Pergunte e responda.',
    pat_tip='**Are you** + palavra? Resposta: **Yes, I am.** / **No, I\'m not.**',
    pat_pages=[
        {'label': 'Perguntar', 'slots': [
            {'cat': 'Question', 'catpt': 'pergunta', 'opts': [['Are you', 'você está/é']]},
            {'cat': 'Word', 'catpt': 'palavra', 'opts': [['late', 'atrasado(a)'], ['lost', 'perdido(a)'], ['new here', 'novo(a) aqui'], ['in a hurry', 'com pressa'], ['a cat', 'um gato']]}],
         'end': ['?', '?'], 'tip': None},
        {'label': 'Responder', 'slots': [
            {'cat': 'Yes / No', 'catpt': 'sim / não', 'opts': [['Yes,', 'sim,'], ['No,', 'não,']]},
            {'cat': 'Short answer', 'catpt': 'resposta curta', 'opts': [['I am.', 'eu estou/sou.'], ["I'm not.", 'eu não estou/sou.']]}],
         'end': ['', ''], 'tip': None},
        {'label': 'Pergunta e resposta', 'slots': [
            {'cat': 'Ask', 'catpt': 'pergunta', 'opts': [['Are you lost?', 'Você está perdida?'], ['Are you tired?', 'Você está cansada?'], ['Are you ready?', 'Você está pronta?']]},
            {'cat': 'Answer', 'catpt': 'resposta', 'opts': [['Yes, I am.', 'Sim, estou.'], ["No, I'm not.", 'Não, não estou.']]}],
         'end': ['', ''], 'tip': None}],
    vplay=[
        {'v': 'Late', 'ic': '⏰', 'pt': 'Atrasado', 'f': [['uso', 'Late']], 'ex': ["Are you late?", 'Você está atrasado?'], 'note': 'Soa como “LÊIT”.'},
        {'v': 'Lost', 'ic': '🧭', 'pt': 'Perdido', 'f': [['uso', 'Lost']], 'ex': ['Are you lost?', 'Você está perdida?'], 'note': 'Soa como “LÓST”.'},
        {'v': 'New', 'ic': '🆕', 'pt': 'Novo(a)', 'f': [['uso', 'New']], 'ex': ['Are you new here?', 'Você é nova aqui?'], 'note': 'Soa como “NIÚ”.'},
        {'v': 'Hurry', 'ic': '🏃', 'pt': 'Pressa', 'f': [['uso', 'Hurry']], 'ex': ["I'm in a hurry.", 'Estou com pressa.'], 'note': 'Soa como “RÂ-ri”.'}],
    sbuild=[
        {'tip': 'Na pergunta, o verbo vem primeiro.', 'b': [['Are', 'Verbo'], ['you', 'Quem'], ['late', 'Como']], 'x': ['am', 'is', 'cat'], 'pt': 'Você está atrasado?', 'end': '?'},
        {'tip': 'Troque o final.', 'b': [['Are', 'Verbo'], ['you', 'Quem'], ['lost', 'Como']], 'x': ['I', 'rabbit', 'is'], 'pt': 'Você está perdida?', 'end': '?'},
        {'tip': 'Agora um lugar.', 'b': [['Are', 'Verbo'], ['you', 'Quem'], ['new', 'Como'], ['here', 'Onde']], 'x': ['am', 'there'], 'pt': 'Você é nova aqui?', 'end': '?'},
        {'tip': 'A resposta curta.', 'b': [['Yes', 'Sim'], ['I', 'Quem'], ['am', 'Verbo']], 'x': ["I'm", 'are', 'do'], 'pt': 'Sim, eu sou.', 'end': '.'}],
    build=[['Are you in a hurry', 'Você está com pressa?'], ['Are you a cat', 'Você é um gato?'],
           ['Yes I am', 'Sim, eu sou'], ["No I'm not", 'Não, eu não sou']],
    order_cast=cast_(('Alice', '👧', '#2b6cb0'), ('Cat', '🐱', '#7C4DFF')),
    order_lines=[
        ['Alice', 'Hello! Are you a cat?', 'Olá! Você é um gato?'],
        ['Cat', 'Yes, I am. Are you lost?', 'Sim, sou. Você está perdida?'],
        ['Alice', "No, I'm not. I'm Alice.", 'Não, não estou. Eu sou a Alice.'],
        ['Cat', 'Are you new here?', 'Você é nova aqui?'],
        ['Alice', 'Yes, I am!', 'Sim, sou!']],
    order_extra=[['Cat', 'Yes, I do.', 'Sim, eu faço.']],
    balloons_ban=['🐇', '⏰', '🐱', '🎩', '❓'],
    balloons=[['🐇', 'rabbit'], ['⏰', 'late'], ['🧭', 'lost'], ['🆕', 'new'], ['🐱', 'cat'], ['🏃', 'hurry']],
    clues=[
        {'en': 'The White Rabbit says: “Oh dear! I’m…”', 'pt': 'O Coelho Branco diz: “Meu Deus! Estou…”', 'a': 1, 'why': 'Atrasado = **late**.', 'hint': 'Ele olha o relógio.'},
        {'en': 'Alice asks: “Are you a…?” It has whiskers.', 'pt': 'A Alice pergunta: “Você é um…?” Tem bigodes.', 'a': 4, 'why': 'O Gato de Cheshire é um **cat**.', 'hint': 'Miau!'},
        {'en': 'The Cat asks: “Are you…?” You don’t know the way.', 'pt': 'O Gato pergunta: “Você está…?” Você não sabe o caminho.', 'a': 2, 'why': 'Perdido = **lost**.', 'hint': 'Sem bússola.'},
        {'en': 'It is Alice’s first day in Wonderland. She is…', 'pt': 'É o primeiro dia da Alice no País das Maravilhas. Ela é…', 'a': 3, 'why': 'Nova = **new**.', 'hint': 'O contrário de “old”.'}],
    dictate=[['Are you in a hurry?', 'Você está com pressa?'], ['Yes, I am.', 'Sim, estou.'],
             ["No, I'm not.", 'Não, não estou.'], ['Are you new here?', 'Você é nova aqui?']],
    scene_art={'s': 'park', 'items': [['🐇', 92, 56, 18, 'bob'], ['🐱', 130, 40, 14, 'bob']], 'seed': 'als1'},
    cast=CAST, lines=LINES,
    quiz=[
        {'q': 'Who is late?', 'pt': 'Quem está atrasado?', 'opts': [['🐰', 'The Rabbit'], ['🐱', 'The Cat'], ['👧', 'Alice']], 'a': 0, 'line': 0, 'why': 'O Coelho diz: “I’m late!”'},
        {'q': 'Is Alice lost?', 'pt': 'A Alice está perdida?', 'opts': [['❌', "No, she isn't"], ['✅', 'Yes, she is'], ['🤷', 'Maybe']], 'a': 0, 'line': 5, 'why': 'Alice diz: “No, I’m not.”'},
        {'q': 'What is the Cat?', 'pt': 'O que é o Gato?', 'opts': [['🐱', 'A cat'], ['🐇', 'A rabbit'], ['🎩', 'A hat']], 'a': 0, 'line': 6, 'why': 'O Gato diz: “Yes, I am.”'}],
    cultx=[
        {'ic': '💡', 'l': 'Curiosidade', 't': 'Lewis Carroll era o nome de escritor de Charles Dodgson, professor de matemática na Universidade de Oxford. Ele criou a história para uma menina de verdade, Alice Liddell.'},
        {'ic': '🗣️', 'l': 'Pergunta famosa', 't': 'Na história, uma Lagarta pergunta à Alice: “Who are you?” (Quem é você?). Ela mal sabe responder!'},
        {'ic': '🌍', 'l': 'E você?', 't': 'Se um personagem estranho perguntasse “Are you lost?”, o que você responderia? Treine as respostas curtas.'}],
    sb_items=[['🐇', 'rabbit'], ['⏰', 'clock'], ['🫖', 'teapot'], ['🎩', 'hat']],
    sb_spots=[['🪑', 'chair'], ['🛏️', 'bed'], ['🌳', 'tree'], ['🚪', 'door']],
    sb_rounds=[
        {'say': ['Put the clock on the tree.'], 'pt': ['Ponha o relógio na árvore.'], 'steps': [[1, 2]], 'items': [1, 0]},
        {'say': ['Put the hat on the chair.'], 'pt': ['Ponha o chapéu na cadeira.'], 'steps': [[3, 0]], 'items': [3, 2]},
        {'say': ['Put the rabbit at the door.', 'Then put the teapot on the bed.'], 'pt': ['Ponha o coelho na porta.', 'Depois ponha o bule na cama.'], 'steps': [[0, 3], [2, 1]], 'items': [0, 2, 1]}],
    produce=dict(
        prompt='A Alice pergunta: *Are you tired? Are you from Brazil?* **Responda com Yes, I am ou No, I\'m not, diga algo sobre você com I\'m e faça uma pergunta para ela com Are you…?**',
        ph="Ex.: Yes, I am. I'm from Brazil. Are you lost?",
        chips=['Yes, I am.', "No, I'm not.", 'Are you…?'],
        model="Yes, I am. I'm a little tired. No, I'm not from Portugal. I'm from Brazil. Are you lost, Alice?",
        check=['Respondi com Yes, I am ou No, I\'m not?', 'Disse algo sobre mim com I\'m?', 'Fiz uma pergunta com Are you…?'],
        kw=[r"\b(?:yes,?\s*i am|no,?\s*i(?:['’]m| am) not)\b", r"\bI(?:['’]m| am)\s+(?!not\b)\w+", r"\bare you\b[^.!?]*\?"],
        tips=[[['Yes, I am.', 'Sim, estou.'], ["No, I'm not.", 'Não, não estou.']],
              [["I'm from Brazil.", 'Eu sou do Brasil.'], ["I'm a little tired.", 'Estou um pouco cansada.']],
              [['Are you lost?', 'Você está perdida?'], ['Are you new here?', 'Você é nova aqui?']]],
        ok=['Resposta curta certa! ✅', 'Você falou de si! 🙋', 'Boa pergunta! ❓'],
        reply=["Oh, nice! I'm not lost. I'm just late! See you later!", 'Que bom! Eu não estou perdido. Só atrasado! Até mais!']),
    review=dict(
        prev="Quem é você? · I'm", work='A Bear Called Paddington',
        recap=[["Hello! I'm Paddington.", 'Olá! Eu sou o Paddington.'], ["I'm from Peru. I'm a bear.", 'Eu sou do Peru. Eu sou um urso.'], ["I'm a little hungry.", 'Estou um pouco com fome.']],
        bag=[{'ic': '🔤', 'l': 'Palavras', 'items': [{'ic': '🐻', 't': 'Bear', 'pt': 'Urso'}, {'ic': '🚉', 't': 'Station', 'pt': 'Estação'}, {'ic': '🥪', 't': 'Hungry', 'pt': 'Com fome'}, {'ic': '😴', 't': 'Tired', 'pt': 'Cansado'}]},
             {'ic': '💬', 'l': 'Expressões', 'items': [{'ic': '🙋', 't': "I'm Paddington.", 'pt': 'Eu sou o Paddington.'}, {'ic': '🇵🇪', 't': "I'm from Peru.", 'pt': 'Eu sou do Peru.'}, {'ic': '😴', 't': "I'm tired.", 'pt': 'Estou cansado.'}]}]),
    wrap_recap=[['Are you in a hurry?', 'Você está com pressa?'], ['Yes, I am.', 'Sim, estou.'], ["No, I'm not.", 'Não, não estou.'], ['Are you new here?', 'Você é nova aqui?']],
    teaser={'t': 'O Mágico de Oz', 'd': 'Próximo padrão: He\'s e She\'s para falar de outras pessoas'},
)

EP['rs'] = {'rdg': 'pier', 'pat': 'yard', 'vplay': 'hall', 'sbuild': 'lake', 'build': 'home1', 'order': 'cafe3', 'balloons': 'park2', 'dictate': 'living', 'soundlab': 'school', 'scene': 'park', 'dquiz': 'street', 'scenebuild': 'kitchen', 'produce': 'cafe2', 'review': 'station', 'wrap': 'bedroom'}
EP['sc'] = 'park'
