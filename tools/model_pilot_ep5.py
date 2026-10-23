# Episódio 5 · Plural -s / -ies · Toy Story
def cast_(*a):
    return {n: [i, c] for n, i, c in a}


CAST = cast_(('Woody', '🤠', '#B7791F'), ('Buzz', '🧑‍🚀', '#2b6cb0'))
LINES = [
    ['Woody', "Buzz, look! It's Andy's birthday party.", 'Buzz, olhe! É a festa de aniversário do Andy.'],
    ['Buzz', 'Parties are fun, Woody!', 'Festas são divertidas, Woody!'],
    ['Woody', 'Yes! I see balloons and toys everywhere.', 'Sim! Vejo balões e brinquedos por todo lado.'],
    ['Buzz', 'I see two puppies under the table.', 'Vejo dois cachorrinhos debaixo da mesa.'],
    ['Woody', 'Puppies? Andy loves puppies!', 'Cachorrinhos? O Andy adora cachorrinhos!'],
    ['Buzz', 'I love stories about planets, Woody.', 'Eu adoro histórias sobre planetas, Woody.'],
    ['Woody', 'Great! Tell your stories to the other toys.', 'Ótimo! Conte suas histórias para os outros brinquedos.'],
    ['Buzz', 'To infinity and beyond!', 'Ao infinito e além!'],
]

EP = dict(
    n=7070024,
    title='Mais de um · Plural: -s e -ies',
    sub='Formar o plural: toy → toys, puppy → puppies',
    pattern_label='Plural: -s e -ies',
    why='Hoje você aprende a falar de mais de uma coisa, como no quarto do Andy: toys, balloons, puppies.',
    vocab=[['Toy', 'Brinquedo', 'Soa como “TÓI”.'], ['Balloon', 'Balão', 'Soa como “ba-LUN”.'],
           ['Puppy', 'Cachorrinho', 'Soa como “PÂ-pi”.'], ['Story', 'História', 'Soa como “STÓ-ri”.'],
           ['Party', 'Festa', 'Soa como “PÁR-ti”.'], ['Planet', 'Planeta', 'Soa como “PLÉ-nit”.']],
    themes={
        'cultob': ('toyshop', ['🤠', '🧑‍🚀', '🧸'], 'g'),
        'rdg': ('bedroom', ['🛏️', '🧸', '💬'], 'f'),
        'pat': ('parade', ['🎈', '🧸', '🎉'], 'f'),
        'vplay': ('attic', ['🧸', '🎈', '🐶'], 'g'),
        'sbuild': ('movingtruck', ['🚚', '🧸', '📦'], 'b'),
        'build': ('workshop', ['🔧', '🧸', '🧩'], 'h'),
        'order': ('picnic', ['🎂', '🤠', '🧑‍🚀'], 'b'),
        'balloons': ('balloons', ['🎈', '🐶', '🎈'], 'a'),
        'dictate': ('musicstage', ['🎧', '🎶', '🧸'], 'c'),
        'soundlab': ('lab', ['🔬', '🗣️', '👄'], 'a'),
        'dquiz': ('suburb', ['🏠', '🧸', '🎂'], 'e'),
        'cultx': ('space', ['🚀', '🧑‍🚀', '⭐'], 'd'),
        'scenebuild': ('skatepark', ['🛹', '🧸', '🎈'], 'b'),
        'produce': ('bedroom', ['🛏️', '🗣️', '🧸'], 'f'),
        'review': ('attic', ['🎒', '🧒', '🚢'], 'h'),
        'wrap': ('fireworks', ['🎆', '🚀', '⭐'], 'd'),
    },
    cover_art={'s': 'living', 'items': [['🧸', 100, 56, 16, 'bob'], ['🎈', 130, 34, 14, 'bob'], ['🎈', 76, 30, 12, 'bob']], 'seed': 'ts1'},
    cover_sub='Plural: em 10 minutos você conta brinquedos, balões e histórias',
    cover_say='É dia de festa no quarto do Andy. Quantos balões? Quantos brinquedos? Como dizer no plural?',
    hook=['I see balloons and toys everywhere.', 'Vejo balões e brinquedos por todo lado.'],
    work=dict(
        name='Toy Story', chips=['🎬 Filme', '1995'], year='1995',
        panels=[
            '“Toy Story” é um filme de animação lançado em 1995 pelos estúdios Pixar, dirigido por John Lasseter. Foi o primeiro longa-metragem feito inteiramente em animação por computador. A história mostra o que os brinquedos do menino Andy fazem quando ninguém está olhando. O cowboy Woody e o astronauta Buzz Lightyear são os protagonistas.',
            'Em um quarto cheio de brinquedos, você precisa do plural o tempo todo: toys, balloons, stories.'],
        facts=['🎬 Pixar · 1995', '🤠 Woody e Buzz', '🖥️ Primeiro longa 100% em computação gráfica']),
    rdg_s=[['I see two {{toys}}.', 'Vejo dois brinquedos.'], ['I see three {{balloons}}.', 'Vejo três balões.'],
           ['Andy loves {{puppies}}.', 'O Andy adora cachorrinhos.'], ['I love {{stories}}.', 'Eu adoro histórias.']],
    rule='Plural: em geral, junte **-s**: *toy → toys, balloon → balloons*. Se terminar em **consoante + y**, troque **y** por **-ies**: *puppy → puppies, story → stories, party → parties.*',
    rdg_q={'q': 'Qual é o plural de “puppy”?', 'o': ['puppies', 'puppys', 'puppyes'], 'a': 0, 'why': 'Consoante + y → tire o y e use **-ies**: puppy → puppies.'},
    pat_title='Como formar o plural?', pat_sub='Um, dois, muitos.',
    pat_tip='Regra geral: **+ s**. Terminou em consoante + **y**: **-ies**.',
    pat_pages=[
        {'label': 'Plural com -s', 'slots': [
            {'cat': 'Number', 'catpt': 'número', 'opts': [['two', 'dois'], ['three', 'três'], ['four', 'quatro'], ['five', 'cinco']]},
            {'cat': 'Word + s', 'catpt': 'palavra + s', 'opts': [['toys', 'brinquedos'], ['balloons', 'balões'], ['planets', 'planetas'], ['boxes', 'caixas']]}],
         'end': ['.', '.'], 'tip': None},
        {'label': 'Plural com -ies', 'slots': [
            {'cat': 'Number', 'catpt': 'número', 'opts': [['two', 'dois'], ['three', 'três'], ['four', 'quatro']]},
            {'cat': 'y → ies', 'catpt': 'y → ies', 'opts': [['puppies', 'cachorrinhos'], ['stories', 'histórias'], ['parties', 'festas'], ['babies', 'bebês']]}],
         'end': ['.', '.'], 'tip': None},
        {'label': 'Frases do episódio', 'slots': [
            {'cat': 'I see / I love', 'catpt': 'eu vejo / eu adoro', 'opts': [['I see', 'eu vejo'], ['I love', 'eu adoro']]},
            {'cat': 'Plural', 'catpt': 'plural', 'opts': [['balloons', 'balões'], ['puppies', 'cachorrinhos'], ['stories', 'histórias'], ['toys', 'brinquedos']]}],
         'end': ['.', '.'], 'tip': None}],
    vplay=[
        {'v': 'Toys', 'ic': '🧸', 'pt': 'Brinquedos', 'f': [['uso', 'Toys']], 'ex': ['I see two toys.', 'Vejo dois brinquedos.'], 'note': 'Soa como “TÓIZ”.'},
        {'v': 'Balloons', 'ic': '🎈', 'pt': 'Balões', 'f': [['uso', 'Balloons']], 'ex': ['I see three balloons.', 'Vejo três balões.'], 'note': 'Soa como “ba-LUNZ”.'},
        {'v': 'Puppies', 'ic': '🐶', 'pt': 'Cachorrinhos', 'f': [['uso', 'Puppies']], 'ex': ['Andy loves puppies.', 'O Andy adora cachorrinhos.'], 'note': 'Soa como “PÂ-piz”.'},
        {'v': 'Stories', 'ic': '📖', 'pt': 'Histórias', 'f': [['uso', 'Stories']], 'ex': ['I love stories.', 'Eu adoro histórias.'], 'note': 'Soa como “STÓ-riz”.'}],
    sbuild=[
        {'tip': 'Um condutor e uma ação.', 'b': [['I', 'Quem'], ['see', 'Faz o quê'], ['two toys', 'O quê']], 'x': ['toy', 'sees', 'puppy'], 'pt': 'Vejo dois brinquedos.', 'end': '.'},
        {'tip': 'Com plural, o artigo some.', 'b': [['Andy', 'Quem'], ['loves', 'Faz o quê'], ['puppies', 'O quê']], 'x': ['puppys', 'love', 'a puppy'], 'pt': 'O Andy adora cachorrinhos.', 'end': '.'},
        {'tip': 'Consoante + y vira -ies.', 'b': [['I', 'Quem'], ['love', 'Faz o quê'], ['stories', 'O quê']], 'x': ['storys', 'loves', 'story'], 'pt': 'Eu adoro histórias.', 'end': '.'},
        {'tip': 'Um vagão de lugar.', 'b': [['Two', 'Quantos'], ['puppies', 'O quê'], ['are', 'Verbo'], ['under the table', 'Onde']], 'x': ['is', 'puppy'], 'pt': 'Dois cachorrinhos estão debaixo da mesa.', 'end': '.'}],
    build=[['I see two toys', 'Vejo dois brinquedos'], ['Andy loves puppies', 'O Andy adora cachorrinhos'],
           ['I love stories about planets', 'Eu adoro histórias sobre planetas'], ['Parties are fun', 'Festas são divertidas']],
    order_cast=cast_(('Woody', '🤠', '#B7791F'), ('Andy', '👦', '#2b6cb0')),
    order_lines=[
        ['Andy', 'Look at my toys!', 'Olhe os meus brinquedos!'],
        ['Woody', 'I see three toys and two balloons.', 'Vejo três brinquedos e dois balões.'],
        ['Andy', 'And I have puppies!', 'E eu tenho cachorrinhos!'],
        ['Woody', 'Puppies? Great!', 'Cachorrinhos? Ótimo!'],
        ['Andy', 'Parties are fun!', 'Festas são divertidas!']],
    order_extra=[['Woody', 'I see three toy.', 'Vejo três brinquedo.']],
    balloons_ban=['🧸', '🎈', '🐶', '📖', '🎉'],
    balloons=[['🧸', 'toys'], ['🎈', 'balloons'], ['🐶', 'puppies'], ['📖', 'stories'], ['🎉', 'parties'], ['🪐', 'planets']],
    clues=[
        {'en': 'One toy, two…', 'pt': 'Um brinquedo, dois…', 'a': 0, 'why': 'toy → **toys** (só junte -s).', 'hint': 'Termina em -oy: só s.'},
        {'en': 'One puppy, two…', 'pt': 'Um cachorrinho, dois…', 'a': 2, 'why': 'puppy → **puppies** (consoante + y → -ies).', 'hint': 'Tire o y e ponha -ies.'},
        {'en': 'One story, many…', 'pt': 'Uma história, muitas…', 'a': 3, 'why': 'story → **stories**.', 'hint': 'Consoante + y.'},
        {'en': 'One party, three…', 'pt': 'Uma festa, três…', 'a': 4, 'why': 'party → **parties**.', 'hint': 'Consoante + y.'}],
    dictate=[['I see two toys.', 'Vejo dois brinquedos.'], ['Andy loves puppies.', 'O Andy adora cachorrinhos.'],
             ['I love stories about planets.', 'Eu adoro histórias sobre planetas.'], ['To infinity and beyond!', 'Ao infinito e além!']],
    scene_art={'s': 'living', 'items': [['🤠', 90, 56, 16, 'bob'], ['🧑‍🚀', 126, 56, 16, 'bob'], ['🎈', 110, 26, 14, 'bob']], 'seed': 'tss1'},
    cast=CAST, lines=LINES,
    quiz=[
        {'q': 'What does Woody see?', 'pt': 'O que o Woody vê?', 'opts': [['🎈', 'Balloons and toys'], ['🐶', 'A big dog'], ['🚀', 'A rocket']], 'a': 0, 'line': 2, 'why': 'Woody diz: “I see balloons and toys everywhere.”'},
        {'q': 'Where are the puppies?', 'pt': 'Onde estão os cachorrinhos?', 'opts': [['🪑', 'Under the table'], ['🛏️', 'On the bed'], ['🚪', 'At the door']], 'a': 0, 'line': 3, 'why': 'Buzz diz: “two puppies under the table”.'},
        {'q': 'What does Buzz love?', 'pt': 'O que o Buzz adora?', 'opts': [['🪐', 'Stories about planets'], ['🎂', 'Cake'], ['🎮', 'Games']], 'a': 0, 'line': 5, 'why': 'Buzz diz: “I love stories about planets.”'}],
    cultx=[
        {'ic': '💡', 'l': 'Curiosidade', 't': '“Toy Story” foi o primeiro longa-metragem do mundo feito inteiramente em animação por computador. Foi lançado em 1995 pela Pixar, estúdio de John Lasseter.'},
        {'ic': '🗣️', 'l': 'Frase famosa', 't': '“To infinity and beyond!” (Ao infinito e além!) é o grito do astronauta Buzz Lightyear.'},
        {'ic': '🌍', 'l': 'E você?', 't': 'Quantos brinquedos você tinha quando era criança? Treine: “I have two… I have three…”.'}],
    sb_items=[['🧸', 'bear'], ['🎈', 'balloon'], ['🐶', 'puppy'], ['📖', 'book']],
    sb_spots=[['🪑', 'chair'], ['🛏️', 'bed'], ['🎂', 'table'], ['🚪', 'door']],
    sb_rounds=[
        {'say': ['Put the balloon on the chair.'], 'pt': ['Ponha o balão na cadeira.'], 'steps': [[1, 0]], 'items': [1, 3]},
        {'say': ['Put the puppy under the table.'], 'pt': ['Ponha o cachorrinho debaixo da mesa.'], 'steps': [[2, 2]], 'items': [2, 0]},
        {'say': ['Put the bear on the bed.', 'Then put the book at the door.'], 'pt': ['Ponha o urso na cama.', 'Depois ponha o livro na porta.'], 'steps': [[0, 1], [3, 3]], 'items': [0, 3, 1]}],
    produce=dict(
        prompt='Você mostra o seu quarto ou a sua casa. **Fale de coisas que você tem ou vê: use pelo menos um plural com -s e um plural com -ies.**',
        ph='Ex.: I see two books and three balloons. I love stories.',
        chips=['I see two', 'I love', 'I have three'],
        model='I see two books and three balloons. I love stories and puppies. I have three parties this month!',
        check=['Usei um número com plural?', 'Usei um plural com -ies?', 'Disse o que vejo ou adoro?'],
        kw=[r"\b(?:two|three|four|five|six|seven|eight|nine|ten|many|some)\s+\w+s\b", r"\b\w+ies\b",
            r"\bI\s+(?:see|love|have|like)\b"],
        tips=[[['I see two books.', 'Vejo dois livros.'], ['I have three toys.', 'Tenho três brinquedos.']],
              [['I love puppies.', 'Eu adoro cachorrinhos.'], ['I love stories.', 'Eu adoro histórias.']],
              [['I see balloons.', 'Vejo balões.'], ['I love parties.', 'Eu adoro festas.']]],
        ok=['Plural com número! 🔢', 'Plural com -ies! 🐶', 'Frase completa! 🎈'],
        reply=["Wow! Your room is full of fun things. I'm jealous!", 'Uau! Seu quarto está cheio de coisas divertidas. Estou com inveja!']),
    review=dict(
        prev='É ele? É ela? É isso?', work='Peter Pan',
        recap=[['Is she a fairy?', 'Ela é uma fada?'], ['Yes, she is.', 'Sim, ela é.'], ["No, it isn't.", 'Não, não é.']],
        bag=[{'ic': '🔤', 'l': 'Palavras', 'items': [{'ic': '🧚', 't': 'Fairy', 'pt': 'Fada'}, {'ic': '🚢', 't': 'Ship', 'pt': 'Navio'}, {'ic': '🐦', 't': 'Bird', 'pt': 'Pássaro'}, {'ic': '😠', 't': 'Angry', 'pt': 'Bravo'}]},
             {'ic': '💬', 'l': 'Expressões', 'items': [{'ic': '❓', 't': 'Is she a fairy?', 'pt': 'Ela é uma fada?'}, {'ic': '✅', 't': 'Yes, she is.', 'pt': 'Sim, ela é.'}, {'ic': '❌', 't': "No, it isn't.", 'pt': 'Não, não é.'}]}]),
    wrap_recap=[['I see two toys.', 'Vejo dois brinquedos.'], ['Andy loves puppies.', 'O Andy adora cachorrinhos.'], ['I love stories about planets.', 'Eu adoro histórias sobre planetas.'], ['To infinity and beyond!', 'Ao infinito e além!']],
    teaser={'t': 'Próximo episódio', 'd': 'Novos padrões e novas obras, em breve!'},
)

EP['rs'] = {'rdg': 'hall', 'pat': 'shop', 'vplay': 'home1', 'sbuild': 'street', 'build': 'school', 'order': 'park2', 'balloons': 'flags', 'dictate': 'cafe', 'soundlab': 'gym', 'scene': 'living', 'dquiz': 'yard', 'scenebuild': 'kitchen', 'produce': 'bedroom', 'review': 'pier', 'wrap': 'park'}
EP['sc'] = 'living'
