# Reescrita A2 438–474 (ver ova2b.py): só obra e elenco (falas e quadros ficam como no módulo, com os nomes trocados).
from v3.ova2b import X, W, L, Q


def O(n, names, ids, name, kind, year, desc, topic, t, e, le, lp, **kw):
    X(n, names, ids, W(name, kind, year, desc, topic, t, e, le, lp), **kw)


O(7081322, ('Bertie', 'Jeeves'), ['tom', 'tommy'], 'Jeeves and Wooster', '📖 Contos', 1915, 'uma série de histórias do escritor britânico P. G. Wodehouse sobre um jovem aristocrata atrapalhado e seu mordomo sempre sereno.', 'pedidos educados: Would it be possible to…? e I would appreciate it if…',
  'castle', ['🎩', '☕', '📜'], 'Would it be possible to change the date?', 'Seria possível mudar a data?')
O(7920046, ('Jovie', 'Buddy'), ['polly', 'tommy'], 'Elf', '🎬 Filme', 2003, 'uma comédia de Natal americana sobre um humano criado entre elfos que vai a Nova York procurar o pai.', 'reagir a surpresas: I am surprised, I did not expect e No way!',
  'castle', ['🎄', '🧝', '🎁'], 'No way! I did not expect this.', 'Não acredito! Eu não esperava isso.')
O(7081323, ('Ryder', 'Chase'), ['tommy', 'tom'], 'PAW Patrol', '📺 Série', 2013, 'uma série animada canadense sobre um menino e uma equipe de cachorros que resolvem problemas da cidade.', 'começar juntos: Let us get started, Let us try, Let us make it',
  'toyshop', ['🐶', '🚒', '🚓'], 'Let us get started.', 'Vamos começar.')
O(7081324, ('Manolin', 'Santiago'), ['tommy', 'tom'], 'The Old Man and the Sea', '📖 Novela', 1952, 'uma novela do escritor americano Ernest Hemingway sobre um velho pescador e sua longa luta com um grande peixe.', 'tempo de espera e esforço: all day, for hours, since morning',
  'ship', ['🎣', '🐟', '🌊'], 'I worked all day.', 'Eu trabalhei o dia todo.')
O(7081325, ('Jenny', 'Forrest'), ['polly', 'tom'], 'Forrest Gump', '🎬 Filme', 1994, 'um filme americano sobre um homem simples que vive momentos marcantes da história e corre por todo o país.', 'frequência: every other day, once in a while, on weekdays',
  'street', ['🏃', '🍫', '🦐'], 'I run on weekdays.', 'Eu corro nos dias de semana.')
O(7081326, ('Osono', 'Kiki'), ['matilda', 'polly'], "Kiki's Delivery Service", '🎬 Animação', 1989, 'um filme de animação japonês do estúdio Ghibli sobre uma jovem bruxa que abre um serviço de entregas numa cidade nova.', 'procurar emprego: I am looking for a job as… e I would like to apply for…',
  'bakery', ['🧹', '🐈‍⬛', '🥖'], 'I am looking for a job as a cook.', 'Estou procurando emprego como cozinheira.')
O(7081327, ('Miranda', 'Daniel'), ['matilda', 'tom'], 'Mrs. Doubtfire', '🎬 Filme', 1993, 'uma comédia americana sobre um pai que se disfarça de babá para ficar perto dos filhos.', 'requisitos de um trabalho: years of experience, knowledge of, skilled in',
  'castle', ['👵', '👨‍👧', '🧹'], 'I have two years of experience.', 'Tenho dois anos de experiência.')
O(7920047, ('Sam', 'Flint'), ['polly', 'tommy'], 'Cloudy with a Chance of Meatballs', '🎬 Animação', 2009, 'um filme de animação sobre um inventor cuja máquina faz chover comida do céu.', 'quantidades em receitas: half a cup, a quarter of, double the amount',
  'bakery', ['🍔', '🌧️', '🧪'], 'Double the amount.', 'Dobre a quantidade.')
O(7081333, ('Goro', 'Tampopo'), ['tom', 'polly'], 'Tampopo', '🎬 Filme', 1985, 'uma comédia japonesa sobre a busca pela sopa de macarrão perfeita.', 'o melhor de tudo: one of the most… e by far the best',
  'bakery', ['🍜', '🥢', '🍥'], 'It is by far the best soup here.', 'É de longe a melhor sopa daqui.')
O(7081334, ('Wendy', 'Peter'), ['wendy', 'peter'], 'Peter Pan', '📖 Peça e romance', 1911, 'uma história do escritor escocês J. M. Barrie sobre um menino que não quer crescer e vive na Terra do Nunca.', 'quantidades indefinidas: several, a couple of e a number of',
  'ship', ['🧚', '🏴‍☠️', '⭐'], 'A number of guests came.', 'Vieram vários convidados.')
O(7920048, ('Mike', 'Roz'), ['tommy', 'matilda'], 'Monsters, Inc.', '🎬 Animação', 2001, 'um filme de animação da Pixar sobre monstros que trabalham numa fábrica de sustos e descobrem algo inesperado.', 'o ambiente de trabalho: my boss, my colleagues, I report to…',
  'castle', ['👁️', '🚪', '🏭'], 'I report to my boss.', 'Eu me reporto à minha chefe.')
O(7081339, ('Derek', 'Meredith'), ['tom', 'polly'], "Grey's Anatomy", '📺 Série', 2005, 'uma série americana sobre médicos de um hospital de Seattle.', 'o que vem acontecendo: have been + -ing, for e since',
  'castle', ['🩺', '🏥', '❤️'], 'I have been doing exercises.', 'Venho fazendo exercícios.')
O(7081342, ('Hallie', 'Annie'), ['polly', 'matilda'], 'The Parent Trap', '🎬 Filme', 1998, 'uma comédia americana sobre duas gêmeas separadas que se conhecem num acampamento e trocam de lugar.', 'o que fizemos nas férias: passado irregular',
  'lake', ['🏕️', '🛶', '✈️'], 'I swam in the lake.', 'Eu nadei no lago.')
O(7920049, ('Vanellope', 'Ralph'), ['polly', 'tom'], 'Wreck-It Ralph', '🎬 Animação', 2012, 'um filme de animação da Disney sobre um vilão de videogame que quer ser herói.', 'recomendar filmes: If you like…, you will love…, similar to',
  'castle', ['🎮', '🍬', '🏎️'], 'If you like games, you will love it.', 'Se você gosta de jogos, vai adorar.')
O(7081345, ('Emma', 'Mr Knightley'), ['polly', 'tom'], 'Emma', '📖 Romance', 1815, 'um romance da escritora inglesa Jane Austen sobre uma jovem que adora juntar casais, mas se engana sobre o próprio coração.', 'confirmar com perguntas curtas: isn\'t it?, don\'t you?, can\'t you?',
  'castle', ['💌', '🎩', '🌸'], "It is a lovely day, isn't it?", 'É um dia lindo, não é?',
  verbs=[('think', '💭', 'achar', "You think so, don't you?", "You think so, doesn't you?", 'She thinks so.', 'Ela acha que sim.', "he **thinks**, **doesn't** he?"),
         ('agree', '🤝', 'concordar', "You agree, don't you?", "You agree, doesn't you?", 'He agreed.', 'Ele concordou.', "you **agree**, **don't** you?"),
         ('invite', '💌', 'convidar', "We invite them, don't we?", "We invite them, doesn't we?", 'She invited me.', 'Ela me convidou.', "we **invite**, **don't** we?"),
         ('wonder', '🤔', 'imaginar', "You wonder, don't you?", "You wonder, doesn't you?", 'I wondered why.', 'Eu me perguntei por quê.', "you **wonder**, **don't** you?")])
O(7081346, ('Brutus', 'Antony'), ['tom', 'tommy'], 'Julius Caesar', '🎭 Peça', 1599, 'uma peça de William Shakespeare sobre a conspiração contra um líder de Roma e os discursos que se seguem.', 'organizar ideias: First of all, In addition, As a result, In conclusion',
  'castle', ['🏛️', '🗡️', '📜'], 'First of all, friends, listen.', 'Antes de tudo, amigos, ouçam.')
O(7081349, ('Estella', 'Pip'), ['polly', 'tommy'], 'Great Expectations', '📖 Romance', 1861, 'um romance do escritor inglês Charles Dickens sobre um órfão que sonha melhorar de vida.', 'planos para o futuro: from now on, in the future, as soon as possible',
  'castle', ['🕰️', '📖', '🌫️'], 'From now on, I will study daily.', 'De agora em diante, vou estudar todos os dias.')
O(7081350, ('Mr Tumnus', 'Lucy'), ['tom', 'polly'], 'The Lion, the Witch and the Wardrobe', '📖 Romance', 1950, 'um romance de fantasia do escritor C. S. Lewis sobre crianças que entram em outro mundo por um guarda-roupa.', 'ansiedade pelo que vem: I cannot wait to…, I am excited about…',
  'castle', ['🦁', '🚪', '❄️'], 'I cannot wait to start!', 'Mal posso esperar para começar!')
O(7920050, ('Astrid', 'Hiccup'), ['polly', 'tommy'], 'How to Train Your Dragon', '🎬 Animação', 2010, 'um filme de animação sobre um jovem viking que faz amizade com um dragão.', 'o que aprendemos: I have learned to…, I have learned that…, I now know…',
  'cave', ['🐉', '⚔️', '🔥'], 'I have learned that mistakes help.', 'Aprendi que os erros ajudam.')
