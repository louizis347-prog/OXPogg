# Reescrita A2 408–436 (ver ova2b.py): na maioria só obra e elenco; falas e quadros ficam como no módulo (nomes trocados).
from v3.ova2b import X, W, L, Q


def O(n, names, ids, name, kind, year, desc, topic, t, e, le, lp, **kw):
    X(n, names, ids, W(name, kind, year, desc, topic, t, e, le, lp), **kw)


O(7081299, ('Principal Duvall', 'Cady'), ['tom', 'polly'], 'Mean Girls', '🎬 Filme', 2004, 'uma comédia americana sobre uma adolescente que chega a uma escola nova e descobre suas regras sociais.', 'regras e proibições: must not e be allowed to',
  'castle', ['🏫', '📵', '📚'], 'You must not run in the hall.', 'Você não deve correr no corredor.')
O(7920043, ('Frank', 'Rachel'), ['tom', 'polly'], 'The Bodyguard', '🎬 Filme', 1992, 'um filme americano sobre um segurança profissional contratado para proteger uma cantora famosa.', 'oferecer ajuda: Shall I…? e Would you like me to…?',
  'castle', ['🛡️', '🎤', '🚪'], "I'll show you the way.", 'Eu mostro o caminho.')
O(7081302, ('Penny', 'Sheldon'), ['polly', 'tom'], 'The Big Bang Theory', '📺 Série', 2007, 'uma série americana de comédia sobre amigos cientistas e a vizinha que mora ao lado.', 'dizer que não entendeu: I do not get it e What do you mean?',
  'castle', ['🔬', '🛋️', '❓'], 'I do not get it. What do you mean?', 'Eu não entendi. O que você quer dizer?')
O(7081305, ('Marilyn', 'Jim'), ['polly', 'tom'], 'Apollo 13', '🎬 Filme', 1995, 'um filme americano baseado na história real de uma missão espacial que enfrentou um grande problema a caminho da Lua.', 'ações prestes a acontecer: be about to e have just',
  'lighthouse', ['🚀', '🌕', '📡'], 'I am about to leave.', 'Estou prestes a sair.',
  verbs=[('launch', '🚀', 'lançar', 'They launch at noon.', 'They launchs at noon.', 'It has just launched.', 'Acabou de ser lançado.', 'it **launches**.'),
         ('count', '🔢', 'contar', 'I am about to count down.', 'I am about to counting down.', 'He has just counted.', 'Ele acabou de contar.', 'about to **count**.'),
         ('land', '🛬', 'pousar', 'The ship is about to land.', 'The ship is about to landing.', 'It has just landed.', 'Acabou de pousar.', 'about to **land**.'),
         ('report', '📡', 'relatar', 'Jim has just reported it.', 'Jim has just report it.', 'She reports daily.', 'Ela relata todo dia.', 'has just **reported**.')])
O(7081306, ('Ray Arnold', 'Ellie Sattler'), ['tom', 'polly'], 'Jurassic Park', '🎬 Filme', 1993, 'um filme de aventura americano sobre um parque de dinossauros que sai do controle.', 'avisos e regras de lugares: Staff only e Visitors must…',
  'jungle', ['🦖', '🚙', '🌴'], 'Visitors must sign in.', 'Os visitantes devem se registrar.')
O(7081308, ('Carl', 'Ellie'), ['tom', 'polly'], 'Up', '🎬 Filme', 2009, 'um filme de animação da Pixar sobre um senhor que amarra balões em sua casa para realizar o sonho de uma vida.', 'experiências de viagem: Have you ever been to…?',
  'castle', ['🎈', '🏠', '🗺️'], 'Have you ever been abroad?', 'Você já viajou para o exterior?')
O(7920044, ('Natalie', 'Ryan'), ['polly', 'tom'], 'Up in the Air', '🎬 Filme', 2009, 'um filme americano sobre um homem que passa a vida viajando de avião a trabalho.', 'no aeroporto: I would like a window seat e Can I check this bag?',
  'lighthouse', ['✈️', '🧳', '🎫'], 'I would like a window seat.', 'Eu gostaria de um assento na janela.')
X(81310, verbs=[('sell', '🏷️', 'vender', 'The farmer sells apples.', 'The farmer sell apples.', 'She sold tomatoes.', 'Ela vendeu tomates.', 'he **sells**.'),
                ('taste', '😋', 'provar', 'I taste the cheese.', 'I tastes the cheese.', 'He tasted the jam.', 'Ele provou a geleia.', 'I **taste**.'),
                ('haggle', '🤝', 'pechinchar', 'She haggles for a price.', 'She haggle for a price.', 'We haggled a bit.', 'Pechinchamos um pouco.', 'she **haggles**.'),
                ('bag', '🛍️', 'embalar', 'He bags the fruit.', 'He bag the fruit.', 'I bagged the bread.', 'Embalei o pão.', 'he **bags**.')])
O(7081310, ('Peppa', 'Mummy Pig'), ['tommy', 'matilda'], 'Peppa Pig', '📺 Série', 2004, 'uma série animada britânica infantil sobre uma porquinha, sua família e seus amigos.', 'embalagens e quantidades: a bottle of, a bag of, a carton of',
  'toyshop', ['🐷', '🥛', '🛒'], 'A carton of milk and a loaf of bread.', 'Uma caixa de leite e um pão.')
O(7081311, ('Sandy', 'Danny'), ['polly', 'tom'], 'Grease', '🎬 Filme', 1978, 'um musical americano sobre um grupo de estudantes e um romance de verão que continua na escola.', 'escolher entre opções: either … or, neither … nor, both',
  'castle', ['🎶', '🚗', '🥤'], 'Either tea or coffee is fine.', 'Tanto chá quanto café está bom.')
O(7081313, ('Pat', 'Mrs Goggins'), ['tommy', 'mrs'], 'Postman Pat', '📺 Série', 1981, 'uma série animada britânica sobre um carteiro de uma pequena vila e seu gato.', 'dizer onde fica: between, in front of e opposite',
  'toyshop', ['📮', '🐈', '🏘️'], 'The cafe is between the shop and the bank.', 'O café fica entre a loja e o banco.')
O(7081315, ('Katherine', 'Dorothy'), ['polly', 'matilda'], 'Hidden Figures', '🎬 Filme', 2016, 'um filme americano sobre três matemáticas que trabalharam na NASA nos anos 1960.', 'interesses e emoções: interested in, good at, afraid of, proud of',
  'lighthouse', ['🧮', '🚀', '📐'], 'I am interested in math.', 'Eu me interesso por matemática.')
O(7920045, ('Professor Oak', 'Ash'), ['tom', 'tommy'], 'Pokémon', '📺 Série', 1997, 'uma série animada japonesa sobre um menino que viaja pelo mundo para capturar e treinar criaturas chamadas Pokémon.', 'perguntar quando: When did you…? e How long ago…?',
  'jungle', ['⚡', '🔴', '🧢'], 'When did you arrive?', 'Quando você chegou?')
O(7081318, ('Sally', 'Lightning McQueen'), ['polly', 'tom'], 'Cars', '🎬 Filme', 2006, 'um filme de animação da Pixar sobre um carro de corrida que aprende lições numa cidadezinha esquecida.', 'conselhos de segurança: ought to e had better',
  'street', ['🏎️', '🛣️', '🏁'], 'You had better be careful.', 'É melhor você ter cuidado.')
O(7081319, ('Helen', 'Dash'), ['polly', 'tommy'], 'The Incredibles', '🎬 Filme', 2004, 'um filme de animação da Pixar sobre uma família de super-heróis que tenta ter uma vida normal.', 'lembretes: Remember to…, Do not forget to… e Make sure…',
  'castle', ['🦸', '🔑', '💡'], 'Remember to lock the door.', 'Lembre-se de trancar a porta.')
O(7081320, ('Anna', 'William'), ['polly', 'tom'], 'Notting Hill', '🎬 Filme', 1999, 'uma comédia romântica britânica sobre um livreiro de Londres e uma atriz famosa.', 'condições: unless, as long as e in case',
  'castle', ['📚', '🌂', '🏘️'], 'We go, unless it rains.', 'Nós vamos, a menos que chova.')
