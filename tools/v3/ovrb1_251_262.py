# Reescrita dos episódios B1 251–262 (ver ovrb1.py): obra, elenco, palavras, verbos, sons e falas próprios.
# C(...) monta o override e guarda a ficha da obra em WORKS (gravada em obras_new_b1_251_330_*.json por gen_obras_251_330.py).
from v3.ovrb1 import OVR, L

WORKS = {}


def W(n, name, kind, text, e, t):
    WORKS[str(n)] = dict(name=name, kind=kind, text=text + ' A referência combina com o tema do episódio. A cena é autoral; não adapta nem cita a obra.', line=['', ''], pa=dict(t=t, e=e, v=0))


def C(n, names, ids, rs, cv, hot4, vocab, verbs, lines, quiz, lab, fill):
    OVR[n] = dict(names=names, ids=ids, rs=rs, cv=cv, obra=(lines[0][1], lines[0][2]), hot4=hot4, vocab=vocab, verbs=verbs, lines=lines, quiz=quiz, lab=lab, fill=fill)


def F(n, fill):
    OVR[n] = dict(fill=fill)


# ---------------------------------------------------------------- 251 / 252
F(930036, [['Is the toaster still on the blink?', 'A torradeira ainda está com defeito?'], ['Yes, so I will plug in the old one.', 'Sim, então vou ligar a antiga.'],
           ['Use the extension cord by the window.', 'Use a extensão perto da janela.'], ['Thanks, the bread smells great already.', 'Obrigada, o pão já está cheirando bem.']])

W(7930036, 'The Jetsons', '📺 Série · 1962', 'The Jetsons é um desenho animado americano de 1962, da Hanna-Barbera, sobre uma família do futuro com carros voadores e robôs.', ['📺', '🔊', '🔋'], 'castle')
C(7930036, ('George', 'Jane'), ['tom', 'polly'], 'living', 'Na sala do futuro, George e Jane acertam o som e a antena da TV.',
  ('🎚️', 'volume', 'volume', 'Turn the volume down.', 'Diminua o volume.'),
  [('📺', 'remote', 'controle remoto', 'Soa como “ri-MÔUT”.'), ('🔊', 'speaker', 'caixa de som', 'Soa como “SPÍ-ker”.'), ('🔋', 'battery', 'pilha', 'Soa como “BÉ-te-ri”.'),
   ('📡', 'antenna', 'antena', 'Soa como “an-TÉ-na”.'), ('💡', 'bulb', 'lâmpada', 'Soa como “BÂLB”.'), ('🎚️', 'volume', 'volume', 'Soa como “VÓ-lium”.')],
  [('press', '🔘', 'apertar', 'Press the button.', 'Press on the button.', 'I pressed it.', 'Apertei.', 'press **+ objeto**.'),
   ('charge', '🔋', 'carregar', 'Charge the battery.', 'Charge up the battery of.', 'I charged it.', 'Carreguei.', 'charge **+ objeto**.'),
   ('listen', '🎧', 'ouvir', 'Listen to the speaker.', 'Listen the speaker.', 'I listened.', 'Ouvi.', 'listen **to**.'),
   ('fix', '🛠️', 'consertar', 'Fix the antenna.', 'Fix to the antenna.', 'I fixed it.', 'Consertei.', 'fix **+ objeto**.')],
  [['George', 'Jane, the sound is too low.', 'Jane, o som está baixo demais.'], ['Jane', 'Turn it up, then.', 'Então aumente.'], ['George', 'Now it is too loud. Turn it down.', 'Agora está alto demais. Diminua.'],
   ['Jane', 'Hook it up to the speaker first.', 'Conecte primeiro na caixa de som.'], ['George', 'We ran out of batteries!', 'Ficamos sem pilhas!'],
   ['Jane', 'Press the button and charge the battery.', 'Aperte o botão e carregue a pilha.'], ['George', 'Fine. Is the antenna fixed?', 'Certo. A antena está consertada?'], ['Jane', 'Yes. Now we can watch the show.', 'Sim. Agora podemos ver o programa.']],
  [('What is wrong with the sound?', 'O que há de errado com o som?', [('🔈', 'It is too low'), ('🔊', 'It is too loud'), ('📵', 'No sound at all')], 0, 0, 'George diz: “the sound is too low.”'),
   ('What did they run out of?', 'Do que ficaram sem?', [('🔋', 'Batteries'), ('🍞', 'Bread'), ('💡', 'Light')], 0, 4, 'George diz: “We ran out of batteries!”'),
   ('What goes first?', 'O que vem primeiro?', [('🔊', 'Hook it up to the speaker'), ('📡', 'Fix the roof'), ('🍽️', 'Dinner')], 0, 3, 'Jane diz: “Hook it up to the speaker first.”')],
  L('jt', 'Laboratório de sons: remote, battery e volume', 'o final soa ôu; a soa é; vo soa vó.', 'Em remote, o final soa ôu.',
    [('remote', 'ri-MÔUT', 'controle', 'o = ôu', 'remove', 'ri-MÚV'), ('battery', 'BÉ-te-ri', 'pilha', 'a = é', 'bakery', 'BÊI-ke-ri'), ('volume', 'VÓ-lium', 'volume', 'o = ó', 'value', 'VÉ-liu')]),
  [['Elroy wants the cartoon channel tonight.', 'Elroy quer o canal de desenhos hoje à noite.'], ['He can wait until the news is over.', 'Ele pode esperar o noticiário acabar.'],
   ['Then I will hand him the remote.', 'Aí eu entrego o controle a ele.'], ['Good plan. Dinner is ready too.', 'Bom plano. O jantar também está pronto.']])

# ---------------------------------------------------------------- 253 / 254
F(82165, [['Will you let me go to the party?', 'Você me deixa ir à festa?'], ['I will, if you make your bed first.', 'Deixo, se você fizer a cama primeiro.'],
          ['Can I help you with the dishes too?', 'Posso ajudar com a louça também?'], ['That would make me very happy.', 'Isso me deixaria muito feliz.']])

W(7082165, 'Cinderella', '📚 Conto de fadas · 1697', 'Cinderela é um conto de fadas popularizado por Charles Perrault em 1697: uma jovem obrigada a trabalhar na cozinha vai ao baile com a ajuda da madrinha.', ['👠', '🎃', '🕛'], 'castle')
C(7082165, ('Cinderella', 'Stepmother'), ['polly', 'misshoney'], 'kitchen', 'Na cozinha da casa, Cinderela e a madrasta falam do que ela pode e não pode fazer.',
  ('🧹', 'broom', 'vassoura', 'I am made to sweep with a broom.', 'Sou obrigada a varrer com a vassoura.'),
  [('🎃', 'pumpkin', 'abóbora', 'Soa como “PÂMP-kin”.'), ('👠', 'slipper', 'sapatinho', 'Soa como “SLÍ-per”.'), ('🕛', 'midnight', 'meia-noite', 'Soa como “MÍD-náit”.'),
   ('💃', 'ball', 'baile', 'Soa como “BÓL”.'), ('🪄', 'wand', 'varinha', 'Soa como “UÓND”.'), ('🏠', 'chore', 'tarefa de casa', 'Soa como “TCHÓR”.')],
  [('allow', '✅', 'permitir', 'I am allowed to go.', 'I am allowed go.', 'She allowed me.', 'Ela permitiu.', 'be allowed **to**.'),
   ('force', '⛓️', 'obrigar', 'I am forced to work.', 'I am forced work.', 'She forced me.', 'Ela me obrigou.', 'be forced **to**.'),
   ('sweep', '🧹', 'varrer', 'I sweep the floor.', 'I sweeps the floor.', 'I swept it.', 'Varri.', 'sweep → **swept**.'),
   ('cheer', '😄', 'alegrar', 'A dress will cheer me up.', 'A dress will cheer me.', 'It cheered me up.', 'Isso me alegrou.', 'cheer **up**.')],
  [['Cinderella', 'Am I allowed to go to the ball tonight?', 'Posso ir ao baile esta noite?'], ['Stepmother', 'No. You are made to finish the chores first.', 'Não. Você é obrigada a terminar as tarefas primeiro.'],
   ['Cinderella', 'I am made to sweep every single day.', 'Sou obrigada a varrer todos os dias.'], ['Stepmother', 'Then sweep. A clean house makes me happy.', 'Então varra. Uma casa limpa me deixa feliz.'],
   ['Cinderella', 'A dress would make me happy too.', 'Um vestido me deixaria feliz também.'], ['Stepmother', 'You are not allowed to touch my dresses.', 'Você não pode mexer nos meus vestidos.'],
   ['Cinderella', 'Then I will be home before midnight.', 'Então volto para casa antes da meia-noite.'], ['Stepmother', 'Home? You are not going anywhere!', 'Para casa? Você não vai a lugar nenhum!']],
  [('What is Cinderella allowed to do?', 'O que Cinderela pode fazer?', [('🚫', 'Nothing yet'), ('💃', 'Go to the ball'), ('🍰', 'Eat cake')], 0, 1, 'A madrasta diz: “No. You are made to finish the chores first.”'),
   ('What is she made to do every day?', 'O que ela é obrigada a fazer todo dia?', [('🧹', 'Sweep'), ('🎵', 'Sing'), ('🏊', 'Swim')], 0, 2, 'Cinderella diz: “I am made to sweep every single day.”'),
   ('What does a clean house do?', 'O que uma casa limpa faz?', [('😊', 'Makes the stepmother happy'), ('😢', 'Makes her sad'), ('😴', 'Makes her sleep')], 0, 3, 'Stepmother diz: “A clean house makes me happy.”')],
  L('cd', 'Laboratório de sons: pumpkin, slipper e midnight', 'u soa â; i soa i; ni soa nái.', 'Em pumpkin, o u soa â.',
    [('pumpkin', 'PÂMP-kin', 'abóbora', 'u = â', 'pocket', 'PÓ-kit'), ('slipper', 'SLÍ-per', 'sapatinho', 'i = í curto', 'sleeper', 'SLÍ-per'), ('midnight', 'MÍD-náit', 'meia-noite', 'ight = áit', 'mid-sight', 'MÍD-sáit')]),
  [['Does the fairy godmother come tonight?', 'A fada madrinha vem esta noite?'], ['She comes when the house is quiet.', 'Ela vem quando a casa está quieta.'],
   ['Then the clock starts running.', 'Então o relógio começa a correr.'], ['Midnight is the only deadline she gives.', 'A meia-noite é o único prazo que ela dá.']])

# ---------------------------------------------------------------- 255 / 256
F(82166, [['Are you afraid of speaking in public?', 'Você tem medo de falar em público?'], ['A little, but I am good at telling stories.', 'Um pouco, mas sou boa em contar histórias.'],
          ['Then start without worrying about errors.', 'Então comece sem se preocupar com erros.'], ['I am interested in trying it today.', 'Tenho interesse em tentar hoje.']])

W(7082166, 'The Hobbit', '📚 Livro · 1937', 'The Hobbit é um livro de J. R. R. Tolkien publicado em 1937: o hobbit Bilbo Bolseiro sai de casa numa aventura com anões e com o mago Gandalf.', ['🧙', '🗝️', '🏔️'], 'library')
C(7082166, ('Gandalf', 'Bilbo'), ['gandalf', 'tom'], 'hall', 'Na porta redonda da toca, Gandalf convida Bilbo para uma aventura.',
  ('🗝️', 'key', 'chave', 'Take the key before leaving.', 'Pegue a chave antes de sair.'),
  [('🏔️', 'mountain', 'montanha', 'Soa como “MÁUN-tin”.'), ('🗝️', 'key', 'chave', 'Soa como “KÍ”.'), ('🐉', 'dragon', 'dragão', 'Soa como “DRÉ-gon”.'),
   ('🗺️', 'map', 'mapa', 'Soa como “MÉP”.'), ('🍳', 'breakfast', 'café da manhã', 'Soa como “BRÉK-fest”.'), ('🧳', 'adventure', 'aventura', 'Soa como “ed-VÉN-tcher”.')],
  [('pack', '🎒', 'arrumar a mala', 'Pack your bag before leaving.', 'Pack your bag before to leave.', 'I packed.', 'Arrumei.', 'before **+ -ing**.'),
   ('learn', '🎓', 'aprender', 'You learn by walking.', 'You learn by to walk.', 'I learned.', 'Aprendi.', 'by **+ -ing**.'),
   ('knock', '🚪', 'bater', 'Knock before entering.', 'Knock before to enter.', 'I knocked.', 'Bati.', 'before **+ -ing**.'),
   ('rest', '🛌', 'descansar', 'Rest after walking.', 'Rest after to walk.', 'I rested.', 'Descansei.', 'after **+ -ing**.')],
  [['Gandalf', 'Bilbo, take the key before leaving.', 'Bilbo, pegue a chave antes de sair.'], ['Bilbo', 'After eating breakfast, may I think about it?', 'Depois de tomar café, posso pensar nisso?'],
   ['Gandalf', 'You learn about adventure by going on one.', 'Você aprende sobre aventura vivendo uma.'], ['Bilbo', 'Before packing, I need a map.', 'Antes de arrumar a mala, preciso de um mapa.'],
   ['Gandalf', 'I have it. We cross the mountain by walking at night.', 'Eu tenho. Atravessamos a montanha caminhando à noite.'], ['Bilbo', 'And after crossing, we meet the dragon?', 'E depois de atravessar, encontramos o dragão?'],
   ['Gandalf', 'Be honest, Bilbo, are you afraid of trying?', 'Seja honesto, Bilbo, você tem medo de tentar?'], ['Bilbo', 'A little. But I will go.', 'Um pouco. Mas eu vou.']],
  [('What does Gandalf say to take?', 'O que Gandalf diz para pegar?', [('🗝️', 'The key'), ('🗡️', 'A sword'), ('🍎', 'An apple')], 0, 0, 'Gandalf diz: “take the key before leaving.”'),
   ('What does Bilbo need before packing?', 'O que Bilbo precisa antes de arrumar a mala?', [('🗺️', 'A map'), ('🐴', 'A horse'), ('💰', 'Gold')], 0, 3, 'Bilbo diz: “Before packing, I need a map.”'),
   ('How do they cross the mountain?', 'Como atravessam a montanha?', [('🌙', 'Walking at night'), ('🚗', 'By car'), ('🛶', 'By boat')], 0, 4, 'Gandalf diz: “by walking at night.”')],
  L('hb', 'Laboratório de sons: mountain, dragon e breakfast', 'ou soa áu; a soa é; ea soa é.', 'Em mountain, o ou soa áu.',
    [('mountain', 'MÁUN-tin', 'montanha', 'ou = áu', 'fountain', 'FÁUN-tin'), ('dragon', 'DRÉ-gon', 'dragão', 'a = é', 'dragging', 'DRÉ-guin'), ('breakfast', 'BRÉK-fest', 'café da manhã', 'ea = é', 'brake fast', 'BRÊIK-fést')]),
  [['Why does Bilbo hesitate at the door?', 'Por que Bilbo hesita na porta?'], ['He is worried about leaving home.', 'Ele está preocupado em deixar a casa.'],
   ['Tell him he will be back for tea.', 'Diga a ele que voltará para o chá.'], ['I will. A good story begins with one step.', 'Direi. Uma boa história começa com um passo.']])

# ---------------------------------------------------------------- 257 / 258
F(82168, [['I used to live in a quiet town.', 'Eu morava numa cidade tranquila.'], ['And now you are used to the noise?', 'E agora você já se acostumou ao barulho?'],
          ['Almost, but I still wake up at night.', 'Quase, mas ainda acordo à noite.'], ['It takes time to get used to it.', 'Leva tempo para se acostumar.']])

W(7082168, 'Paddington', '📚 Livro · 1958', 'Paddington é um livro infantil de Michael Bond, publicado em 1958: um urso vindo do Peru chega a Londres e é acolhido pela família Brown na estação.', ['🐻', '🧳', '🍊'], 'bakery')
C(7082168, ('Paddington', 'Mrs Brown'), ['bear', 'mrs'], 'living', 'Na sala dos Brown, Paddington conta como era a vida no Peru e como é em Londres.',
  ('🧳', 'suitcase', 'mala', 'I am used to carrying a suitcase.', 'Estou acostumado a carregar uma mala.'),
  [('🧳', 'suitcase', 'mala', 'Soa como “SUT-kêis”.'), ('🍊', 'marmalade', 'geleia de laranja', 'Soa como “MAR-me-lêid”.'), ('🚇', 'underground', 'metrô', 'Soa como “ÂN-der-gráund”.'),
   ('🌧️', 'drizzle', 'garoa', 'Soa como “DRÍ-zol”.'), ('🧥', 'duffle coat', 'casaco de lã', 'Soa como “DÂ-fol KÔUT”.'), ('🏙️', 'crowd', 'multidão', 'Soa como “KRÁUD”.')],
  [('carry', '🧳', 'carregar', 'I am used to carrying a suitcase.', 'I am used to carry a suitcase.', 'I carried it.', 'Carreguei.', 'be used to **+ -ing**.'),
   ('queue', '🚏', 'fazer fila', 'I am not used to queueing.', 'I am not used to queue.', 'I queued.', 'Fiz fila.', 'be used to **+ -ing**.'),
   ('speak', '🗣️', 'falar', 'I used to speak Spanish.', 'I used to speaking Spanish.', 'I spoke.', 'Falei.', 'used to **+ verbo**.'),
   ('eat', '🍽️', 'comer', 'I did not use to eat jam.', 'I did not used to eat jam.', 'I ate.', 'Comi.', 'did not **use** to.')],
  [['Mrs Brown', 'Did you use to live in the jungle, Paddington?', 'Você morava na selva, Paddington?'], ['Paddington', 'Yes. I did not use to see so many people.', 'Sim. Eu não via tantas pessoas.'],
   ['Mrs Brown', 'Are you used to the crowd now?', 'Você já está acostumado à multidão agora?'], ['Paddington', 'Not yet. I am used to carrying a suitcase, though.', 'Ainda não. Mas estou acostumado a carregar uma mala.'],
   ['Mrs Brown', 'And the rain? It is strange for a bear.', 'E a chuva? É estranha para um urso.'], ['Paddington', 'I am getting used to the drizzle and the underground.', 'Estou me acostumando à garoa e ao metrô.'],
   ['Mrs Brown', 'Did you use to eat marmalade in Peru?', 'Você comia geleia de laranja no Peru?'], ['Paddington', 'Yes, but not every day. Now I do.', 'Sim, mas não todo dia. Agora como.']],
  [('Where did Paddington use to live?', 'Onde Paddington morava?', [('🌴', 'In the jungle'), ('🏙️', 'In London'), ('🏖️', 'On a beach')], 0, 0, 'Mrs Brown diz: “Did you use to live in the jungle?”'),
   ('What is he used to doing?', 'A que ele está acostumado?', [('🧳', 'Carrying a suitcase'), ('🚇', 'Taking the underground'), ('🌧️', 'Walking in rain')], 0, 3, 'Paddington diz: “used to carrying a suitcase.”'),
   ('What is he getting used to?', 'A que ele está se acostumando?', [('🌧️', 'The drizzle and the underground'), ('🍰', 'Cake'), ('🏫', 'School')], 0, 5, 'Paddington diz: “getting used to the drizzle and the underground.”')],
  L('pd', 'Laboratório de sons: suitcase, marmalade e drizzle', 'ui soa u; ma soa mar; dr soa drí.', 'Em suitcase, o ui soa u.',
    [('suitcase', 'SUT-kêis', 'mala', 'ui = u', 'suit', 'SÚT'), ('marmalade', 'MAR-me-lêid', 'geleia', 'a = êi', 'lemonade', 'lé-mo-NÊID'), ('drizzle', 'DRÍ-zol', 'garoa', 'i = í', 'dazzle', 'DÉ-zol')]),
  [['Is the marmalade sandwich ready?', 'O sanduíche de geleia está pronto?'], ['It is in your hat, as always.', 'Está no seu chapéu, como sempre.'],
   ['Good. I keep one for emergencies.', 'Ótimo. Guardo um para emergências.'], ['Then you are ready for the big city.', 'Então você está pronto para a cidade grande.']])

# ---------------------------------------------------------------- 259 / 260
F(930037, [['Did he show up on time this morning?', 'Ele chegou na hora hoje de manhã?'], ['He showed up late and showed off his watch.', 'Chegou atrasado e exibiu o relógio.'],
           ['Show him in, then show him around.', 'Mande-o entrar e mostre o lugar.'], ['Right away. He will love the garden.', 'Já. Ele vai adorar o jardim.']])

W(7930037, 'Dead Poets Society', '🎬 Filme · 1989', 'Sociedade dos Poetas Mortos é um filme de 1989, dirigido por Peter Weir: o professor Keating ensina poesia num colégio rígido e incentiva os alunos a pensar por si mesmos.', ['📜', '🪑', '✍️'], 'library')
C(7930037, ('Keating', 'Neil'), ['tom', 'tommy'], 'school', 'Na sala de aula, o professor Keating pede uma votação por levantar as mãos.',
  ('🎟️', 'ticket', 'ingresso', 'Please show your ticket.', 'Mostre seu ingresso, por favor.'),
  [('🙋', 'raise', 'levantar', 'Soa como “RÊIZ”.'), ('🪑', 'desk', 'carteira', 'Soa como “DÉSK”.'), ('📜', 'poem', 'poema', 'Soa como “PÔU-em”.'),
   ('🏫', 'academy', 'colégio', 'Soa como “a-KÉ-de-mi”.'), ('🎫', 'ticket', 'ingresso', 'Soa como “TÍ-kit”.'), ('🙌', 'respect', 'respeito', 'Soa como “ri-SPÉKT”.')],
  [('raise', '✋', 'levantar', 'Raise your hand.', 'Rise your hand.', 'I raised it.', 'Levantei.', 'raise **+ objeto**.'),
   ('vote', '🗳️', 'votar', 'We vote by a show of hands.', 'We vote with a show hands.', 'We voted.', 'Votamos.', 'a show **of** hands.'),
   ('read', '📖', 'ler', 'Read the poem aloud.', 'Read the poem loud.', 'I read it.', 'Li.', 'read → **read** (pronuncia-se red).'),
   ('stand', '🧍', 'ficar de pé', 'Stand on your desk.', 'Stand in your desk.', 'I stood.', 'Fiquei de pé.', 'stand → **stood**.')],
  [['Keating', 'Class, let us vote with a show of hands.', 'Turma, vamos votar levantando as mãos.'], ['Neil', 'What is the question, Mr Keating?', 'Qual é a pergunta, Sr. Keating?'],
   ['Keating', 'Who wants to read the poem aloud?', 'Quem quer ler o poema em voz alta?'], ['Neil', 'I will. Do I show my ticket for the school play first?', 'Eu leio. Mostro meu ingresso da peça da escola antes?'],
   ['Keating', 'Show your ticket at the door, and show respect on stage.', 'Mostre o ingresso na porta e mostre respeito no palco.'], ['Neil', 'Understood. May I stand on my desk?', 'Entendido. Posso subir na carteira?'],
   ['Keating', 'Yes. From up there, you see the room differently.', 'Pode. De lá de cima, você vê a sala de outro jeito.'], ['Neil', 'Now it is a show of hands for everyone.', 'Agora é uma votação para todos.']],
  [('How do they vote?', 'Como votam?', [('✋', 'With a show of hands'), ('📧', 'By email'), ('🗳️', 'With a box')], 0, 0, 'Keating diz: “vote with a show of hands.”'),
   ('What should Neil show at the door?', 'O que Neil deve mostrar na porta?', [('🎟️', 'His ticket'), ('📘', 'His book'), ('🪪', 'His passport')], 0, 4, 'Keating diz: “Show your ticket at the door.”'),
   ('Where does Neil stand?', 'Onde Neil fica de pé?', [('🪑', 'On his desk'), ('🏠', 'At home'), ('🌳', 'In a tree')], 0, 5, 'Neil diz: “May I stand on my desk?”')],
  L('ds', 'Laboratório de sons: desk, poem e respect', 'e soa é; oe soa ôu-em; e soa i.', 'Em poem, o oe soa ôu-em.',
    [('desk', 'DÉSK', 'carteira', 'e = é', 'disk', 'DÍSK'), ('poem', 'PÔU-em', 'poema', 'oe = ôu-em', 'power', 'PÁU-er'), ('respect', 'ri-SPÉKT', 'respeito', 're = ri', 'reject', 'ri-DJÉKT')]),
  [['Why is Neil nervous about the play?', 'Por que Neil está nervoso com a peça?'], ['His father does not want him on stage.', 'O pai dele não quer que ele suba ao palco.'],
   ['Then he must find his own voice.', 'Então ele precisa achar a própria voz.'], ['I think he already has one.', 'Acho que ele já tem uma.']])

# ---------------------------------------------------------------- 261 / 262
F(82169, [['I am pleased to meet you, Mr Stevens.', 'Prazer em conhecê-lo, Sr. Stevens.'], ['I am ready to serve dinner at eight.', 'Estou pronto para servir o jantar às oito.'],
          ['I was surprised to hear that news.', 'Fiquei surpreso ao ouvir essa notícia.'], ['We are proud to work in this house.', 'Temos orgulho de trabalhar nesta casa.']])

W(7082169, 'Mulan', '🎬 Filme · 1998', 'Mulan é uma animação da Disney de 1998, inspirada numa lenda chinesa: uma jovem toma o lugar do pai no exército e aprende que treinar é difícil, mas possível.', ['🗡️', '🏯', '🐉'], 'castle')
C(7082169, ('Mulan', 'Shang'), ['mulan', 'tom'], 'park', 'No campo de treino, Mulan e o capitão Shang falam de como é difícil e como é bom treinar.',
  ('🏹', 'arrow', 'flecha', 'It is hard to shoot an arrow.', 'É difícil atirar uma flecha.'),
  [('🏹', 'arrow', 'flecha', 'Soa como “Á-rôu”.'), ('🏯', 'camp', 'acampamento', 'Soa como “KÉMP”.'), ('🧗', 'pole', 'poste', 'Soa como “PÔUL”.'),
   ('🥋', 'training', 'treino', 'Soa como “TRÊI-nin”.'), ('🛡️', 'armor', 'armadura', 'Soa como “ÁR-mer”.'), ('🏔️', 'summit', 'topo', 'Soa como “SÂ-mit”.')],
  [('shoot', '🏹', 'atirar', 'It is hard to shoot an arrow.', 'It is hard shoot an arrow.', 'I shot.', 'Atirei.', 'hard **to** + verbo.'),
   ('climb', '🧗', 'escalar', 'It is easy to climb with practice.', 'It is easy climb with practice.', 'I climbed.', 'Escalei.', 'easy **to** + verbo.'),
   ('train', '🥋', 'treinar', 'It is nice to train with friends.', 'It is nice train with friends.', 'I trained.', 'Treinei.', 'nice **to** + verbo.'),
   ('win', '🏆', 'vencer', 'I am happy to win today.', 'I am happy win today.', 'I won.', 'Venci.', 'happy **to** + verbo.')],
  [['Shang', 'It is hard to climb this pole, soldier.', 'É difícil subir neste poste, soldado.'], ['Mulan', 'It is easy to say, but hard to do.', 'É fácil dizer, mas difícil fazer.'],
   ['Shang', 'It is nice to see you try again.', 'É bom ver você tentar de novo.'], ['Mulan', 'I am happy to train every morning.', 'Fico feliz em treinar toda manhã.'],
   ['Shang', 'Is it hard to shoot an arrow?', 'É difícil atirar uma flecha?'], ['Mulan', 'Not now. It was hard to hold the bow at first.', 'Agora não. Foi difícil segurar o arco no começo.'],
   ['Shang', 'Good. Climb the pole before sunset.', 'Bom. Suba no poste antes do pôr do sol.'], ['Mulan', 'It is easy now. Look!', 'Agora é fácil. Olhe!']],
  [('What is hard to climb?', 'O que é difícil de escalar?', [('🧗', 'The pole'), ('🏔️', 'A mountain'), ('🌳', 'A tree')], 0, 0, 'Shang diz: “hard to climb this pole.”'),
   ('What is Mulan happy to do?', 'O que Mulan fica feliz em fazer?', [('🥋', 'Train every morning'), ('😴', 'Sleep late'), ('🍜', 'Cook')], 0, 3, 'Mulan diz: “happy to train every morning.”'),
   ('What was hard at first?', 'O que foi difícil no começo?', [('🏹', 'Holding the bow'), ('🐎', 'Riding'), ('🍚', 'Eating')], 0, 5, 'Mulan diz: “hard to hold the bow at first.”')],
  L('ml', 'Laboratório de sons: arrow, training e summit', 'rr soa r; ai soa êi; u soa â.', 'Em training, o ai soa êi.',
    [('arrow', 'Á-rôu', 'flecha', 'a = á', 'narrow', 'NÁ-rôu'), ('training', 'TRÊI-nin', 'treino', 'ai = êi', 'trending', 'TRÉN-din'), ('summit', 'SÂ-mit', 'topo', 'u = â', 'sum it', 'SÂM-it')]),
  [['Is the captain pleased with Mulan now?', 'O capitão está satisfeito com Mulan agora?'], ['He is proud to say she improved.', 'Ele tem orgulho de dizer que ela melhorou.'],
   ['Then he should tell her himself.', 'Então ele devia dizer isso a ela.'], ['He will, after the next drill.', 'Dirá, depois do próximo exercício.']])
