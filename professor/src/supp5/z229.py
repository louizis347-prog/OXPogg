"""Quest v5 aula 229 (z)."""
def V(v, ic, pt, note, a, b, c, d):
    return {'v': v, 'ic': ic, 'pt': pt, 'note': note, 'forms': [
        {'k': 'eu · você · nós · eles', 'en': a[0], 'ex': a[1], 'pt': a[2]},
        {'k': 'ele · ela', 'en': b[0], 'ex': b[1], 'pt': b[2]},
        {'k': 'passado', 'en': c[0], 'ex': c[1], 'pt': c[2]},
        {'k': '-ing', 'en': d[0], 'ex': d[1], 'pt': d[2]}]}
Z = {'verbs': [
  V('call', '📣', 'chamar', 'Call = chamar pelo nome ou ligar. Em aula: call the roll.',
    ('call', 'We call the names.', 'Nós chamamos os nomes.'), ('calls', 'She calls the roll.', 'Ela faz a chamada.'), ('called', 'He called my name.', 'Ele chamou o meu nome.'), ('calling', 'She is calling Anna.', 'Ela está chamando a Anna.')),
  V('sit', '🪑', 'sentar', 'Sit = sentar. Passado: sat. Sit down = sentar-se.',
    ('sit', 'We sit at our desks.', 'Nós sentamos nas carteiras.'), ('sits', 'He sits next to Anna.', 'Ele senta ao lado da Anna.'), ('sat', 'I sat in the front.', 'Eu sentei na frente.'), ('sitting', 'They are sitting down.', 'Eles estão sentando.')),
  V('write', '✏️', 'escrever', 'Write = escrever. Passado: wrote. Write it down = anotar.',
    ('write', 'We write the date.', 'Nós escrevemos a data.'), ('writes', 'She writes the test day.', 'Ela escreve o dia da prova.'), ('wrote', 'I wrote it down.', 'Eu anotei.'), ('writing', 'He is writing a note.', 'Ele está escrevendo um bilhete.')),
  V('start', '▶️', 'começar', 'Start = começar. Class starts at eight (com -s para he/she/it).',
    ('start', 'We start at eight.', 'Nós começamos às oito.'), ('starts', 'Class starts at nine.', 'A aula começa às nove.'), ('started', 'The test started late.', 'A prova começou tarde.'), ('starting', 'The class is starting.', 'A aula está começando.')),
  V('answer', '🙋', 'responder', 'Answer = responder. Sem preposição: answer the teacher.',
    ('answer', 'We answer fast.', 'Nós respondemos rápido.'), ('answers', 'Anna answers “Here!”', 'A Anna responde “Presente!”'), ('answered', 'Nobody answered.', 'Ninguém respondeu.'), ('answering', 'He is answering the question.', 'Ele está respondendo à pergunta.'))],
 'verb_game': [
  {'scene': 'Hoje a professora chamou o meu nome.', 'en': 'Today the teacher ___ my name.', 'opts': ['call', 'called', 'calling'], 'ans': 1, 'pt': 'Hoje a professora chamou o meu nome.', 'why': 'O passado de call é called.'},
  {'scene': 'Ontem eu anotei a data da prova.', 'en': 'Yesterday I ___ the test day.', 'opts': ['write', 'writing', 'wrote'], 'ans': 2, 'pt': 'Ontem eu anotei o dia da prova.', 'why': 'O passado de write é wrote.'},
  {'scene': 'A aula começa às oito.', 'en': 'Class ___ at eight.', 'opts': ['start', 'starts', 'starting'], 'ans': 1, 'pt': 'A aula começa às oito.', 'why': 'Com class (it), o verbo leva -s.'},
  {'scene': 'Eles estão sentando agora.', 'en': 'They are ___ down now.', 'opts': ['sit', 'sat', 'sitting'], 'ans': 2, 'pt': 'Eles estão sentando agora.', 'why': 'are + -ing: sitting.'}],
 'expressions': [
  {'en': 'Let me call the roll.', 'pt': 'Vou fazer a chamada.', 'ex': 'Good morning! Let me call the roll.', 'exp': 'Para começar a chamada na aula.', 'c': 'a'},
  {'en': 'Here! / Present.', 'pt': 'Presente!', 'ex': 'Anna? Here!', 'exp': 'Para responder à chamada.', 'c': 'b'},
  {'en': 'He isn’t here today.', 'pt': 'Ele não veio hoje.', 'ex': 'Carlos isn’t here today.', 'exp': 'Para dizer que alguém está ausente.', 'c': 'c'},
  {'en': 'Sorry I’m late.', 'pt': 'Desculpe o atraso.', 'ex': 'Sorry I’m late. The bus was slow.', 'exp': 'Para pedir desculpa por chegar tarde.', 'c': 'd'},
  {'en': 'Sit down, please.', 'pt': 'Sente-se, por favor.', 'ex': 'It’s okay. Sit down, please.', 'exp': 'Para pedir que alguém se sente.', 'c': 'a'},
  {'en': 'The test is on Friday.', 'pt': 'A prova é na sexta.', 'ex': 'Write it down. The test is on Friday.', 'exp': 'Para avisar o dia de um evento.', 'c': 'b'}],
 'expr_game': [
  {'cue': 'Você chega atrasado na aula.', 'opts': ['Sorry I’m late.', 'Let me call the roll.', 'Sit down, please.'], 'ans': 0, 'why': 'Sorry I’m late. pede desculpa pelo atraso.'},
  {'cue': 'O professor diz o seu nome na chamada.', 'opts': ['The test is on Friday.', 'Here!', 'He isn’t here today.'], 'ans': 1, 'why': 'Here! mostra que você está na sala.'},
  {'cue': 'Você quer avisar o dia da prova.', 'opts': ['Sit down, please.', 'Sorry I’m late.', 'The test is on Friday.'], 'ans': 2, 'why': 'Dias pedem on: on Friday.'}]}
