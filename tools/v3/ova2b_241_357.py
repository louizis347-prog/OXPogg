# Reescrita A2 332–356 (ver ova2b.py).
from v3.ova2b import X, W, L, Q

# 332 · passado irregular 2
X(7081233, ('Rachel', 'Ross'), ['polly', 'tom'],
  W('Friends', '📺 Série', 1994, 'uma série americana de comédia sobre seis amigos que vivem em Nova York.', 'o que fizemos no fim de semana: passado irregular',
    'castle', ['☕', '🛋️', '🛍️'], 'I took a bus to the mall.', 'Peguei um ônibus até o shopping.'),
  [('☕', 'coffee', 'café', 'Soa como “KÓ-fi”.'), ('🛋️', 'sofa', 'sofá', 'Soa como “SÔU-fa”.'), ('🏢', 'apartment', 'apartamento', 'Soa como “a-PÁRT-ment”.'),
   ('🏬', 'mall', 'shopping', 'Soa como “MÓL”.'), ('🥪', 'sandwich', 'sanduíche', 'Soa como “SÉN-uitch”.'), ('🚌', 'bus', 'ônibus', 'Soa como “BÂS”.')],
  [('🥪', 'sandwich', 'sanduíche', 'I ate a sandwich.', 'Eu comi um sanduíche.'),
   ('🚌', 'bus', 'ônibus', 'We took a bus to the mall.', 'Pegamos um ônibus até o shopping.'),
   ('🏢', 'apartment', 'apartamento', 'She came to my apartment.', 'Ela veio ao meu apartamento.'),
   ('🛋️', 'sofa', 'sofá', 'He bought a new sofa.', 'Ele comprou um sofá novo.'),
   ('☕', 'coffee', 'café', 'I had coffee at the mall.', 'Tomei café no shopping.')],
  [['Rachel', 'What did you do on Saturday, Ross?', 'O que você fez no sábado, Ross?'],
   ['Ross', 'I took a bus to the mall.', 'Peguei um ônibus até o shopping.'],
   ['Rachel', 'Did you eat there?', 'Você comeu lá?'],
   ['Ross', 'Yes, I ate a sandwich.', 'Sim, comi um sanduíche.'],
   ['Rachel', 'Did anyone come with you?', 'Alguém foi com você?'],
   ['Ross', 'Monica came too. She bought a sofa.', 'A Monica foi também. Ela comprou um sofá.'],
   ['Rachel', 'What did you buy?', 'O que você comprou?'],
   ['Ross', 'I bought coffee for the apartment.', 'Comprei café para o apartamento.']],
  [Q('How did Ross go to the mall?', 'Como o Ross foi ao shopping?', 1, ('🚌', 'By bus'), ('🚗', 'By car'), ('🚲', 'By bike')),
   Q('What did he eat?', 'O que ele comeu?', 3, ('🥪', 'A sandwich'), ('🍕', 'Pizza'), ('🍜', 'Noodles')),
   Q('What did Monica buy?', 'O que a Monica comprou?', 5, ('🛋️', 'A sofa'), ('📺', 'A TV'), ('🪴', 'A plant'))],
  verbs=None, lab=None)

# 334 · When I was… (só a obra)
X(7081235, ('Gordie', 'Chris'), ['tommy', 'tom'],
  W('Stand by Me', '🎬 Filme', 1986, 'um filme americano, baseado numa novela de Stephen King, sobre quatro amigos e uma caminhada que marca a infância.', 'lembranças de infância: When I was young, I…',
    'viaduct', ['🚂', '🎒', '🌲'], 'When I was young, I lived near the sea.', 'Quando eu era jovem, morava perto do mar.'))

# 336 · reclamações (só a obra)
X(7920034, ('Madame D.', 'M. Gustave'), ['matilda', 'tom'],
  W('The Grand Budapest Hotel', '🎬 Filme', 2014, 'uma comédia do diretor Wes Anderson sobre o concierge de um hotel luxuoso e seu jovem ajudante.', 'reclamar com educação: I would like to complain about…',
    'castle', ['🏨', '🛎️', '🎩'], 'I would like to complain about my room.', 'Gostaria de reclamar do meu quarto.'))

# 338 · too / enough
X(7081240, ('Scrooge', 'Webby'), ['tom', 'polly'],
  W('DuckTales', '📺 Série', 1987, 'uma série animada da Disney sobre o pato milionário Tio Patinhas e seus sobrinhos aventureiros.', 'preço e suficiência: too e enough',
    'castle', ['💰', '💎', '🦆'], 'It is too expensive.', 'É caro demais.'),
  [('🪙', 'coin', 'moeda', 'Soa como “KÓIN”.'), ('🏦', 'vault', 'cofre grande', 'Soa como “VÓLT”.'), ('💎', 'diamond', 'diamante', 'Soa como “DÁI-mond”.'),
   ('🥇', 'gold', 'ouro', 'Soa como “GÔULD”.'), ('🔐', 'safe', 'cofre', 'Soa como “SÊIF”.'), ('🦆', 'duck', 'pato', 'Soa como “DÂK”.')],
  [('💎', 'diamond', 'diamante', 'This diamond is too expensive.', 'Este diamante é caro demais.'),
   ('🪙', 'coin', 'moeda', 'This coin is cheap enough.', 'Esta moeda é barata o bastante.'),
   ('🏦', 'vault', 'cofre grande', 'The vault is big enough.', 'O cofre grande é grande o bastante.'),
   ('🥇', 'gold', 'ouro', 'I do not have enough gold.', 'Não tenho ouro suficiente.'),
   ('🔐', 'safe', 'cofre', 'The safe is too small.', 'O cofre é pequeno demais.')],
  [['Scrooge', 'This diamond costs a fortune.', 'Este diamante custa uma fortuna.'],
   ['Webby', 'That is too expensive.', 'Isso é caro demais.'],
   ['Scrooge', 'This gold coin is cheap enough.', 'Esta moeda de ouro é barata o bastante.'],
   ['Webby', 'But it is too small for the vault.', 'Mas é pequena demais para o cofre grande.'],
   ['Scrooge', 'Is the big coin heavy enough?', 'A moeda grande é pesada o bastante?'],
   ['Webby', 'Yes. But I do not have enough gold.', 'Sim. Mas não tenho ouro suficiente.'],
   ['Scrooge', 'Save a little more, lass.', 'Economize mais um pouco, mocinha.'],
   ['Webby', 'OK. I will come back.', 'Certo. Eu volto.']],
  [Q('What costs a fortune?', 'O que custa uma fortuna?', 0, ('💎', 'The diamond'), ('🍞', 'The bread'), ('🧢', 'The cap')),
   Q('What is cheap enough?', 'O que é barato o bastante?', 2, ('🪙', 'The gold coin'), ('💎', 'The diamond'), ('🏦', 'The vault')),
   Q('What does Webby not have enough of?', 'De que a Webby não tem o bastante?', 5, ('🥇', 'Gold'), ('⏰', 'Time'), ('🍰', 'Cake'))],
  verbs=None, lab=None)

# 340 · só os verbos
X(7081241, verbs=[('climb', '🧗', 'subir', 'We climb the stairs.', 'We climbs the stairs.', 'He climbed up.', 'Ele subiu.', 'we **climb**.'),
                  ('ride', '🛗', 'andar de', 'Ride the escalator.', 'Ride to the escalator.', 'She rode the lift.', 'Ela usou o elevador.', 'ride **the**.'),
                  ('wait', '⏳', 'esperar', 'Wait on the first floor.', 'Wait in the first floor.', 'We waited downstairs.', 'Esperamos no térreo.', 'wait **on**.'),
                  ('search', '👀', 'procurar', 'Search for the exit.', 'Search the exit.', 'I searched upstairs.', 'Procurei no andar de cima.', 'search **for**.')])

# 342 · he / she / it + -s
X(7081242, ('Lisa', 'Bart'), ['polly', 'tommy'],
  W('The Simpsons', '📺 Série', 1989, 'uma série animada americana sobre uma família da cidade de Springfield.', 'a rotina de alguém: he, she, it + verbo com -s, -es, -ies',
    'castle', ['🛹', '🍩', '📺'], 'He wakes up at six.', 'Ele acorda às seis.'),
  verbs=[('skate', '🛹', 'andar de skate', 'Bart skates to school.', 'Bart skate to school.', 'They skate daily.', 'Eles andam de skate todo dia.', 'he **skates**.'),
         ('catch', '🪝', 'pegar', 'He catches the bus.', 'He catchs the bus.', 'She catches a cold.', 'Ela pega um resfriado.', 'he **catches**.'),
         ('carry', '🎒', 'carregar', 'She carries her books.', 'She carrys her books.', 'He carries a bag.', 'Ele carrega uma bolsa.', 'she **carries**.'),
         ('hurry', '🏃', 'apressar-se', 'He hurries home.', 'He hurrys home.', 'She hurries to class.', 'Ela corre para a aula.', 'he **hurries**.')])

# 344 · viagem (só a obra)
X(7081244, ('Neal', 'Del'), ['tom', 'tommy'],
  W('Planes, Trains and Automobiles', '🎬 Filme', 1987, 'uma comédia americana sobre dois desconhecidos que tentam voltar para casa na época do feriado, usando todo tipo de transporte.', 'tempo de viagem e transportes: How long does it take?',
    'street', ['🚆', '✈️', '🚕'], 'It takes two hours by train.', 'Leva duas horas de trem.'))

# 346 · Shall we / Let's
X(7920035, ('Sebastian', 'Mia'), ['tom', 'polly'],
  W('La La Land', '🎬 Filme', 2016, 'um filme musical americano sobre um pianista de jazz e uma atriz que perseguem seus sonhos em Los Angeles.', 'convites e sugestões: Shall we…? e Let us…',
    'lighthouse', ['🎹', '⭐', '🎷'], 'Shall we walk under the stars?', 'Vamos andar sob as estrelas?'),
  [('🎷', 'jazz', 'jazz', 'Soa como “DJÉZ”.'), ('🎹', 'piano', 'piano', 'Soa como “pi-É-nou”.'), ('🍽️', 'dinner', 'jantar', 'Soa como “DÍ-ner”.'),
   ('🎞️', 'cinema', 'cinema', 'Soa como “SÍ-ne-ma”.'), ('⭐', 'stars', 'estrelas', 'Soa como “STÁRZ”.'), ('🚶', 'walk', 'caminhada', 'Soa como “UÓK”.')],
  [('🎷', 'jazz', 'jazz', 'Shall we go to a jazz club?', 'Vamos a um clube de jazz?'),
   ('🍽️', 'dinner', 'jantar', "Let's have dinner first.", 'Vamos jantar primeiro.'),
   ('🎞️', 'cinema', 'cinema', 'Shall we see a film at the cinema?', 'Vamos ver um filme no cinema?'),
   ('⭐', 'stars', 'estrelas', 'Shall we walk under the stars?', 'Vamos andar sob as estrelas?'),
   ('🎹', 'piano', 'piano', "Let's not stop the piano.", 'Não vamos parar o piano.')],
  [['Sebastian', 'Are you free tonight, Mia?', 'Você está livre hoje à noite, Mia?'],
   ['Mia', 'Yes. What shall we do?', 'Estou. O que vamos fazer?'],
   ['Sebastian', "Let's go to a jazz club first.", 'Vamos primeiro a um clube de jazz.'],
   ['Mia', 'Great. And then the cinema?', 'Ótimo. E depois o cinema?'],
   ['Sebastian', 'Shall we walk under the stars after dinner?', 'Vamos andar sob as estrelas depois do jantar?'],
   ['Mia', "Yes. Let's not be late for the film.", 'Sim. Não vamos nos atrasar para o filme.'],
   ['Sebastian', 'Shall we go now?', 'Vamos agora?'],
   ['Mia', "Yes, let's go.", 'Sim, vamos.']],
  [Q('Where do they go first?', 'Aonde eles vão primeiro?', 2, ('🎷', 'A jazz club'), ('🏫', 'School'), ('🏖️', 'The beach')),
   Q('What do they do after dinner?', 'O que fazem depois do jantar?', 4, ('⭐', 'Walk under the stars'), ('😴', 'Sleep'), ('📚', 'Study')),
   Q('What do they not want to be?', 'O que eles não querem ser?', 5, ('⏰', 'Late'), ('😢', 'Sad'), ('🥱', 'Bored'))],
  verbs=None, lab=None)

# 348 · Have you seen…?
X(7081251, ('Mike', 'Eleven'), ['tommy', 'polly'],
  W('Stranger Things', '📺 Série', 2016, 'uma série americana de ficção científica passada nos anos 1980, sobre um grupo de crianças e fenômenos estranhos numa cidadezinha.', 'perguntar o que já se viu: Have you seen…?',
    'cave', ['🚲', '🔦', '👾'], 'Have you seen the monster?', 'Você já viu o monstro?'),
  [('📺', 'series', 'série', 'Soa como “SÍ-riz”.'), ('👾', 'monster', 'monstro', 'Soa como “MÓN-ster”.'), ('🏬', 'mall', 'shopping', 'Soa como “MÓL”.'),
   ('🏚️', 'basement', 'porão', 'Soa como “BÊIS-ment”.'), ('🌀', 'portal', 'portal', 'Soa como “PÓR-tal”.'), ('🤫', 'secret', 'segredo', 'Soa como “SÍ-kret”.')],
  [('📺', 'seen', 'visto', 'Have you seen the new series?', 'Você já viu a nova série?'),
   ('👾', 'Yes, I have', 'Sim, já', 'Yes, I have.', 'Sim, já vi.'),
   ('🏚️', "No, I haven't", 'Não, ainda não', "No, I haven't.", 'Não, ainda não vi.'),
   ('🌀', 'Has he', 'Ele já', 'Has he seen the portal?', 'Ele já viu o portal?'),
   ('🏬', 'every', 'todo', 'I have seen every episode.', 'Eu vi todos os episódios.')],
  [['Mike', 'Have you seen the new series?', 'Você já viu a nova série?'],
   ['Eleven', 'Yes, I have.', 'Sim, já vi.'],
   ['Mike', 'Have you seen the monster?', 'Você já viu o monstro?'],
   ['Eleven', "No, I haven't. Has Dustin seen it?", 'Não, ainda não. O Dustin já viu?'],
   ['Mike', 'Yes, he has.', 'Sim, já viu.'],
   ['Eleven', 'Have they seen the portal?', 'Eles já viram o portal?'],
   ['Mike', "No, they haven't.", 'Não, ainda não.'],
   ['Eleven', "I haven't either. Let us look in the basement.", 'Eu também não. Vamos olhar no porão.']],
  [Q('Has Eleven seen the new series?', 'A Eleven já viu a nova série?', 1, ('✅', 'Yes, she has'), ('❌', 'No, she has not'), ('❓', 'She does not know')),
   Q('Who has seen the monster?', 'Quem já viu o monstro?', 4, ('🧑', 'Dustin'), ('🧒', 'Eleven'), ('👦', 'Mike')),
   Q('Where do they look?', 'Onde eles olham?', 7, ('🏚️', 'In the basement'), ('🏫', 'At school'), ('🏬', 'At the mall'))],
  verbs=None, lab=None)

# 350 · I recommend / I suggest
X(7081252, ('Roz', 'Frasier'), ['polly', 'tom'],
  W('Frasier', '📺 Série', 1993, 'uma série americana de comédia sobre um psiquiatra que apresenta um programa de rádio.', 'recomendar e sugerir: I recommend + -ing e I suggest + -ing',
    'castle', ['🎙️', '🎧', '📞'], 'I recommend listening carefully.', 'Eu recomendo ouvir com atenção.'),
  [('📞', 'caller', 'ouvinte que liga', 'Soa como “KÓ-ler”.'), ('💬', 'advice', 'conselho', 'Soa como “ed-VÁIS”.'), ('🎙️', 'microphone', 'microfone', 'Soa como “MÁI-kro-fôun”.'),
   ('🎧', 'headphones', 'fones de ouvido', 'Soa como “RÉD-fôunz”.'), ('📻', 'show', 'programa', 'Soa como “XÔU”.'), ('🕒', 'schedule', 'horário', 'Soa como “SKÉ-djul”.')],
  [('📞', 'caller', 'ouvinte', 'I recommend answering the caller.', 'Eu recomendo atender o ouvinte.'),
   ('💬', 'advice', 'conselho', 'I suggest giving good advice.', 'Eu sugiro dar bons conselhos.'),
   ('🎙️', 'microphone', 'microfone', 'I recommend this microphone.', 'Eu recomendo este microfone.'),
   ('🎧', 'headphones', 'fones de ouvido', 'I suggest wearing headphones.', 'Eu sugiro usar fones de ouvido.'),
   ('📻', 'show', 'programa', 'I recommend my show.', 'Eu recomendo o meu programa.')],
  [['Roz', 'What do you recommend for this caller, Frasier?', 'O que você recomenda para este ouvinte, Frasier?'],
   ['Frasier', 'I recommend listening carefully.', 'Recomendo ouvir com atenção.'],
   ['Roz', 'Anything else?', 'Mais alguma coisa?'],
   ['Frasier', 'I suggest giving good advice.', 'Sugiro dar bons conselhos.'],
   ['Roz', 'Which microphone?', 'Qual microfone?'],
   ['Frasier', 'I suggest this microphone.', 'Sugiro este microfone.'],
   ['Roz', 'And a good show?', 'E um bom programa?'],
   ['Frasier', 'I recommend my show. It is funny.', 'Recomendo o meu programa. É engraçado.']],
  [Q('What does Frasier recommend?', 'O que o Frasier recomenda?', 1, ('👂', 'Listening carefully'), ('😴', 'Sleeping'), ('🏃', 'Running')),
   Q('What does he suggest giving?', 'O que ele sugere dar?', 3, ('💬', 'Good advice'), ('🎁', 'A gift'), ('💰', 'Money')),
   Q('Which show does he recommend?', 'Qual programa ele recomenda?', 7, ('📻', 'His own show'), ('📺', 'A TV show'), ('🎬', 'A film'))],
  verbs=None, lab=None)

# 352 · look forward to (só a obra)
X(7920036, ('Mrs Sheffield', 'Fran'), ['matilda', 'polly'],
  W('The Nanny', '📺 Série', 1993, 'uma série americana de comédia sobre uma jovem de Nova York que vira babá numa casa elegante.', 'expectativa e hábito: look forward to e be used to + -ing',
    'castle', ['👶', '🧸', '👗'], 'I look forward to meeting the baby.', 'Estou ansiosa para conhecer o bebê.'))

# 354 · be going to
X(7081253, ('Marlin', 'Dory'), ['tom', 'polly'],
  W('Finding Nemo', '🎬 Filme', 2003, 'um filme de animação da Pixar sobre um peixe-palhaço que atravessa o oceano para encontrar o filho.', 'planos: be going to e not going to',
    'ship', ['🐠', '🐢', '🌊'], 'We are going to find him.', 'Nós vamos encontrá-lo.'),
  [('🌊', 'ocean', 'oceano', 'Soa como “Ô-xan”.'), ('🪸', 'reef', 'recife', 'Soa como “RÍF”.'), ('🐢', 'turtle', 'tartaruga', 'Soa como “TÉR-tol”.'),
   ('🦈', 'shark', 'tubarão', 'Soa como “XÁRK”.'), ('🕸️', 'net', 'rede', 'Soa como “NÉT”.'), ('🫧', 'bubble', 'bolha', 'Soa como “BÂ-bol”.')],
  [('🪸', 'reef', 'recife', 'I am going to swim to the reef.', 'Vou nadar até o recife.'),
   ('🐢', 'turtle', 'tartaruga', 'The turtle is going to take us.', 'A tartaruga vai nos levar.'),
   ('🦈', 'shark', 'tubarão', 'We are not going to stay near the shark.', 'Não vamos ficar perto do tubarão.'),
   ('🕸️', 'net', 'rede', 'Are you going to avoid the net?', 'Você vai evitar a rede?'),
   ('🌊', 'ocean', 'oceano', 'We are going to cross the ocean.', 'Vamos atravessar o oceano.')],
  [['Marlin', 'What are you going to do tomorrow, Dory?', 'O que você vai fazer amanhã, Dory?'],
   ['Dory', 'I am going to swim to the reef.', 'Vou nadar até o recife.'],
   ['Marlin', 'Are you going to ride the turtle?', 'Você vai pegar carona na tartaruga?'],
   ['Dory', 'The turtle is going to take us across the ocean.', 'A tartaruga vai nos levar pelo oceano.'],
   ['Marlin', 'Are you going to meet the shark?', 'Você vai encontrar o tubarão?'],
   ['Dory', 'No, we are not going to stay near him.', 'Não, não vamos ficar perto dele.'],
   ['Marlin', 'Are you going to look for Nemo?', 'Você vai procurar o Nemo?'],
   ['Dory', 'Yes, we are going to find him.', 'Sim, vamos encontrá-lo.']],
  [Q('Where is Dory going to swim?', 'Para onde a Dory vai nadar?', 1, ('🪸', 'To the reef'), ('🏠', 'Home'), ('🏖️', 'To the beach')),
   Q('Who is going to take them across the ocean?', 'Quem vai levá-los pelo oceano?', 3, ('🐢', 'The turtle'), ('🐳', 'The whale'), ('🦀', 'The crab')),
   Q('Who are they going to find?', 'Quem eles vão encontrar?', 7, ('🐠', 'Nemo'), ('🦈', 'The shark'), ('🐙', 'An octopus'))],
  [('swim', '🏊', 'nadar', 'Dory swims fast.', 'Dory swim fast.', 'We swam to the reef.', 'Nadamos até o recife.', 'she **swims**.'),
   ('find', '🔍', 'encontrar', 'They find the way.', 'They finds the way.', 'He found his son.', 'Ele encontrou o filho.', 'they **find**.'),
   ('float', '🫧', 'flutuar', 'The bubble floats up.', 'The bubble float up.', 'It floated away.', 'Flutuou para longe.', 'it **floats**.'),
   ('dive', '🤿', 'mergulhar', 'Marlin dives deep.', 'Marlin dive deep.', 'We dived together.', 'Mergulhamos juntos.', 'he **dives**.')],
  L('r', 'Laboratório de sons: ocean, reef e turtle', 'o soa ô; ee soa í; ur soa ér.', 'Em reef, ee soa í: RÍF.',
    [('ocean', 'Ô-xan', 'oceano', 'c = x', 'option', 'ÓP-xon'), ('reef', 'RÍF', 'recife', 'ee = í', 'rift', 'RÍFT'), ('turtle', 'TÉR-tol', 'tartaruga', 'ur = ér', 'title', 'TÁI-tol')],
    ['I am going to swim to the reef.', 'Vou nadar até o recife.']),
  cv='No fundo do mar, Marlin e Dory fazem planos: be going to e not going to.')

# 356 · while I was -ing
X(7081254, ('Pollyanna', 'Aunt Polly'), ['polly', 'matilda'],
  W('Pollyanna', '📖 Romance', 1913, 'um romance da escritora americana Eleanor H. Porter sobre uma menina sempre otimista que muda a vida de uma cidade.', 'o que estava acontecendo quando algo interrompeu: while e when',
    'toyshop', ['🧵', '📞', '🏠'], 'While I was sewing, the phone rang.', 'Enquanto eu costurava, o telefone tocou.'),
  verbs=[('knock', '🚪', 'bater', 'Someone knocked at the door.', 'Someone knocked on at door.', 'I was knocking.', 'Eu estava batendo.', 'knock **at**.'),
         ('laugh', '😂', 'rir', 'She was laughing.', 'She was laugh.', 'We laughed a lot.', 'Rimos muito.', 'was **laughing**.'),
         ('whistle', '🎵', 'assobiar', 'He was whistling.', 'He was whistle.', 'I whistled a tune.', 'Assobiei uma melodia.', 'was **whistling**.'),
         ('wait', '⏳', 'esperar', 'I was waiting for you.', 'I was wait for you.', 'They waited outside.', 'Eles esperaram do lado de fora.', 'was **waiting**.')])
