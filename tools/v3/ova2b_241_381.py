# Reescrita A2 358–380 (ver ova2b.py).
from v3.ova2b import X, W, L, Q

# 358 · How well / how fast / as … as
X(7081255, ('Ted', 'Sam'), ['tom', 'tommy'],
  W('Ted Lasso', '📺 Série', 2020, 'uma série americana de comédia sobre um treinador de futebol americano que passa a comandar um time de futebol na Inglaterra.', 'perguntar como alguém faz algo: How well, How fast, How carefully',
    'castle', ['⚽', '🏟️', '🔔'], 'How well do you kick?', 'Quão bem você chuta?'),
  [('🥅', 'goal', 'gol', 'Soa como “GÔUL”.'), ('🏟️', 'pitch', 'campo', 'Soa como “PÍTX”.'), ('🦵', 'kick', 'chute', 'Soa como “KÍK”.'),
   ('📯', 'whistle', 'apito', 'Soa como “UÍ-sol”.'), ('🚪', 'locker', 'armário', 'Soa como “LÓ-ker”.'), ('🏁', 'match', 'partida', 'Soa como “MÉTX”.')],
  [('🦵', 'How well', 'quão bem', 'How well do you kick?', 'Quão bem você chuta?'),
   ('🏃', 'How fast', 'quão rápido', 'How fast can you run?', 'Quão rápido você corre?'),
   ('🛡️', 'How carefully', 'com que cuidado', 'How carefully do you defend?', 'Com que cuidado você defende?'),
   ('🥅', 'as … as', 'tão … quanto', 'I run as fast as Jamie.', 'Eu corro tão rápido quanto o Jamie.'),
   ('📯', 'whistle', 'apito', 'Listen for the whistle.', 'Escute o apito.')],
  [['Ted', 'How well do you kick, Sam?', 'Quão bem você chuta, Sam?'],
   ['Sam', 'I kick very well.', 'Eu chuto muito bem.'],
   ['Ted', 'How fast can you run?', 'Quão rápido você corre?'],
   ['Sam', 'I run as fast as Jamie.', 'Eu corro tão rápido quanto o Jamie.'],
   ['Ted', 'How carefully do you defend?', 'Com que cuidado você defende?'],
   ['Sam', 'I defend as carefully as Roy.', 'Eu defendo tão cuidadosamente quanto o Roy.'],
   ['Ted', 'How can we score a goal?', 'Como podemos fazer um gol?'],
   ['Sam', 'We play as a team.', 'Jogamos como um time.']],
  [Q('How well does Sam kick?', 'Quão bem o Sam chuta?', 1, ('👍', 'Very well'), ('👎', 'Badly'), ('🤷', 'Not at all')),
   Q('Who is Sam as fast as?', 'Tão rápido quanto quem o Sam é?', 3, ('🏃', 'Jamie'), ('🧑‍🏫', 'Ted'), ('🐢', 'A turtle')),
   Q('How do they score?', 'Como eles fazem gol?', 7, ('👥', 'As a team'), ('🧍', 'Alone'), ('🍀', 'By luck'))],
  [('kick', '🦵', 'chutar', 'Sam kicks the ball.', 'Sam kick the ball.', 'He kicked it far.', 'Ele chutou longe.', 'he **kicks**.'),
   ('defend', '🛡️', 'defender', 'Roy defends well.', 'Roy defend well.', 'We defended all day.', 'Defendemos o dia todo.', 'he **defends**.'),
   ('score', '🥅', 'marcar', 'Jamie scores often.', 'Jamie score often.', 'She scored twice.', 'Ela marcou duas vezes.', 'he **scores**.'),
   ('cheer', '📣', 'torcer', 'The fans cheer loudly.', 'The fans cheers loudly.', 'We cheered for you.', 'Torcemos por você.', 'they **cheer**.')],
  L('tx', 'Laboratório de sons: pitch, whistle e match', 'tch soa tx; wh soa u; i soa í curto.', 'Em pitch, tch soa tx: PÍTX.',
    [('pitch', 'PÍTX', 'campo', 'tch = tx', 'pit', 'PÍT'), ('whistle', 'UÍ-sol', 'apito', 'wh = u; t mudo', 'wrestle', 'RÉ-sol'), ('match', 'MÉTX', 'partida', 'tch = tx', 'mat', 'MÉT')],
    ['How well do you kick?', 'Quão bem você chuta?']),
  cv='No campo de treino, Ted e Sam falam de quão bem, quão rápido e com que cuidado jogam.')

# 360 · há quanto tempo (só a obra)
X(7081257, ('Tess', 'Jack'), ['polly', 'tom'],
  W('Working Girl', '🎬 Filme', 1988, 'uma comédia americana sobre uma secretária ambiciosa que quer crescer no mundo dos negócios de Nova York.', 'tempo de trabalho e moradia: for e since',
    'castle', ['💼', '🗽', '📞'], 'I have worked here for five years.', 'Trabalho aqui há cinco anos.'))

# 362 · I really appreciate…
X(7081258, ('Mary', 'George'), ['polly', 'tom'],
  W("It's a Wonderful Life", '🎬 Filme', 1946, 'um clássico do cinema americano sobre um homem de uma cidade pequena que vê como sua vida ajudou os outros.', 'agradecer: I really appreciate… e Many thanks for…',
    'castle', ['🔔', '😇', '🎄'], 'I really appreciate your help.', 'Agradeço muito a sua ajuda.'),
  [('😇', 'angel', 'anjo', 'Soa como “ÊIN-djol”.'), ('🔔', 'bell', 'sino', 'Soa como “BÉL”.'), ('🪽', 'wings', 'asas', 'Soa como “UÍNGZ”.'),
   ('🏘️', 'town', 'cidade pequena', 'Soa como “TÁUN”.'), ('🌠', 'wish', 'desejo', 'Soa como “UÍX”.'), ('🎁', 'gift', 'presente', 'Soa como “GÍFT”.')],
  [('😇', 'angel', 'anjo', 'I really appreciate the angel.', 'Agradeço muito ao anjo.'),
   ('🔔', 'bell', 'sino', 'Many thanks for the bell.', 'Muito obrigado pelo sino.'),
   ('🏘️', 'town', 'cidade', 'I appreciate your help with the town.', 'Agradeço a sua ajuda com a cidade.'),
   ('🌠', 'wish', 'desejo', 'Thanks for your wish for me.', 'Obrigado pelo seu desejo por mim.'),
   ('🎁', 'gift', 'presente', 'I appreciate the gift of friends.', 'Agradeço o presente da amizade.')],
  [['Mary', 'I really appreciate your help, George.', 'Agradeço muito a sua ajuda, George.'],
   ['George', 'You are welcome.', 'De nada.'],
   ['Mary', 'Many thanks for saving the town.', 'Muito obrigada por salvar a cidade.'],
   ['George', 'No problem.', 'Sem problema.'],
   ['Mary', 'I appreciate you coming home today.', 'Agradeço você ter voltado para casa hoje.'],
   ['George', 'I appreciate the gift of friends.', 'Agradeço o presente da amizade.'],
   ['Mary', 'And thanks for the bell on the tree.', 'E obrigada pelo sino na árvore.'],
   ['George', 'I appreciate your wish for me.', 'Agradeço o seu desejo por mim.']],
  [Q('What does Mary thank George for saving?', 'O que a Mary agradece o George por salvar?', 2, ('🏘️', 'The town'), ('🐕', 'A dog'), ('🚗', 'A car')),
   Q('What does George appreciate?', 'O que o George agradece?', 5, ('🎁', 'The gift of friends'), ('💰', 'Money'), ('🏠', 'A house')),
   Q('What is on the tree?', 'O que está na árvore?', 6, ('🔔', 'A bell'), ('⭐', 'A star'), ('🕯️', 'A candle'))],
  verbs=None, lab=None)

# 364 · It turns out · I found out · I realized
X(7920037, ('Shaggy', 'Velma'), ['tommy', 'polly'],
  W('Scooby-Doo, Where Are You!', '📺 Série', 1969, 'uma série animada americana sobre um grupo de jovens e um cachorro que desvendam mistérios de fantasmas.', 'descobertas: It turns out…, I found out… e I realized…',
    'cave', ['👻', '🔦', '🐶'], 'It turns out the ghost is a man in a mask.', 'Descobrimos que o fantasma é um homem de máscara.'),
  [('👻', 'ghost', 'fantasma', 'Soa como “GÔUST”.'), ('🎭', 'mask', 'máscara', 'Soa como “MÉSK”.'), ('🧩', 'clue', 'pista', 'Soa como “KLÚ”.'),
   ('🔦', 'flashlight', 'lanterna', 'Soa como “FLÉX-láit”.'), ('🏚️', 'mansion', 'mansão', 'Soa como “MÉN-xon”.'), ('🕵️', 'mystery', 'mistério', 'Soa como “MÍS-te-ri”.')],
  [('👻', 'ghost', 'fantasma', 'It turns out the ghost is a man.', 'Descobrimos que o fantasma é um homem.'),
   ('🎭', 'mask', 'máscara', 'I found out that it is a mask.', 'Descobri que é uma máscara.'),
   ('🧩', 'clue', 'pista', 'I realized that this clue is old.', 'Percebi que esta pista é antiga.'),
   ('🔦', 'flashlight', 'lanterna', 'It turns out the flashlight is dead.', 'Descobrimos que a lanterna está sem pilha.'),
   ('🏚️', 'mansion', 'mansão', 'I realized that we are in the mansion.', 'Percebi que estamos na mansão.')],
  [['Shaggy', 'It turns out the ghost is very old.', 'Descobrimos que o fantasma é muito antigo.'],
   ['Velma', 'How do you know?', 'Como você sabe?'],
   ['Shaggy', 'I found out that it is a mask.', 'Descobri que é uma máscara.'],
   ['Velma', 'What does this clue mean?', 'O que esta pista significa?'],
   ['Shaggy', 'It turns out it means the mansion.', 'Descobrimos que significa a mansão.'],
   ['Velma', 'Then we look here with the flashlight.', 'Então procuramos aqui com a lanterna.'],
   ['Shaggy', 'Wait. I realized that we are lost.', 'Espere. Percebi que estamos perdidos.'],
   ['Velma', 'Oh no. Where is Scooby?', 'Ai, não. Cadê o Scooby?']],
  [Q('What is the ghost?', 'O que é o fantasma?', 2, ('🎭', 'A man in a mask'), ('🐉', 'A dragon'), ('🤖', 'A robot')),
   Q('What does the clue mean?', 'O que a pista significa?', 4, ('🏚️', 'The mansion'), ('🏫', 'The school'), ('🌳', 'The park')),
   Q('What did Shaggy realize?', 'O que o Shaggy percebeu?', 6, ('🗺️', 'They are lost'), ('🍔', 'He is hungry'), ('🌙', 'It is late'))],
  verbs=None, lab=None)

# 366 · I work as a… (obra e verbos)
X(7081261, ('Leslie', 'Ron'), ['polly', 'tom'],
  W('Parks and Recreation', '📺 Série', 2009, 'uma série americana de comédia sobre os funcionários do departamento de parques de uma cidade pequena.', 'profissões: What do you do? e I work as a…',
    'castle', ['🌳', '📋', '🧇'], 'I work as a manager.', 'Eu trabalho como gerente.'),
  verbs=[('organize', '📋', 'organizar', 'Leslie organizes the event.', 'Leslie organize the event.', 'We organized a party.', 'Organizamos uma festa.', 'she **organizes**.'),
         ('build', '🪵', 'construir', 'Ron builds a table.', 'Ron build a table.', 'He built a boat.', 'Ele construiu um barco.', 'he **builds**.'),
         ('cook', '🍳', 'cozinhar', 'He cooks breakfast.', 'He cook breakfast.', 'She cooked dinner.', 'Ela cozinhou o jantar.', 'he **cooks**.'),
         ('plan', '🗓️', 'planejar', 'She plans every detail.', 'She plan every detail.', 'We planned the park.', 'Planejamos o parque.', 'she **plans**.')])

# 368 · a bit / much / a lot + comparativo
X(7081263, ('Beth', 'Mr Shaibel'), ['polly', 'tom'],
  W("The Queen's Gambit", '📺 Minissérie', 2020, 'uma minissérie americana, baseada num romance de Walter Tevis, sobre uma jovem prodígio do xadrez.', 'comparar melhoras: a bit, much e a lot + comparativo',
    'castle', ['♟️', '👑', '🏆'], 'I am much faster now.', 'Estou muito mais rápida agora.'),
  hot=[('♟️', 'a bit stronger', 'um pouco mais forte', 'Her game is a bit stronger.', 'O jogo dela está um pouco mais forte.'),
       ('⏱️', 'much quicker', 'muito mais rápido', 'She plays much quicker.', 'Ela joga muito mais rápido.'),
       ('📉', 'a lot weaker', 'muito mais fraco', 'Last year she was a lot weaker.', 'No ano passado ela era muito mais fraca.'),
       ('🔲', 'board', 'tabuleiro', 'I study the board a lot.', 'Eu estudo muito o tabuleiro.'),
       ('🏆', 'tournament', 'torneio', 'I want to win the tournament.', 'Quero ganhar o torneio.')],
  lines=[['Mr Shaibel', 'How is your chess now, Beth?', 'Como está o seu xadrez agora, Beth?'],
         ['Beth', 'It is a bit better.', 'Está um pouco melhor.'],
         ['Mr Shaibel', 'And your speed?', 'E a sua velocidade?'],
         ['Beth', 'I am much faster.', 'Estou muito mais rápida.'],
         ['Mr Shaibel', 'And last year?', 'E no ano passado?'],
         ['Beth', 'It was a lot worse.', 'Era muito pior.'],
         ['Mr Shaibel', 'You practice a lot.', 'Você treina muito.'],
         ['Beth', 'Yes. I want to be even stronger.', 'Sim. Quero ficar ainda mais forte.']],
  quiz=[Q('How is Beth\'s chess?', 'Como está o xadrez da Beth?', 1, ('📈', 'A bit better'), ('📉', 'Much worse'), ('➖', 'The same')),
        Q('How fast is she now?', 'Quão rápida ela está agora?', 3, ('⚡', 'Much faster'), ('🐢', 'A bit slower'), ('🧍', 'The same')),
        Q('What does Beth want?', 'O que a Beth quer?', 7, ('💪', 'To be even stronger'), ('😴', 'To rest'), ('🚪', 'To leave'))],
  verbs=[('study', '📖', 'estudar', 'Beth studies the board.', 'Beth study the board.', 'She studied all night.', 'Ela estudou a noite toda.', 'she **studies**.'),
         ('move', '♟️', 'mover', 'He moves the pawn.', 'He move the pawn.', 'She moved the queen.', 'Ela moveu a rainha.', 'he **moves**.'),
         ('capture', '♞', 'capturar', 'She captures the knight.', 'She capture the knight.', 'He captured a bishop.', 'Ele capturou um bispo.', 'she **captures**.'),
         ('train', '🏋️', 'treinar', 'Beth trains daily.', 'Beth train daily.', 'We trained hard.', 'Treinamos muito.', 'she **trains**.')])

# 370 · still / yet / no longer / already
X(7081265, ('Ilsa', 'Rick'), ['polly', 'tom'],
  W('Casablanca', '🎬 Filme', 1942, 'um clássico do cinema americano passado em Casablanca durante a Segunda Guerra, sobre amor, escolhas e documentos de viagem.', 'o que já aconteceu ou ainda não: still, yet, no longer, already',
    'castle', ['✈️', '☕', '🎹'], 'I still need a letter of transit.', 'Ainda preciso de uma carta de trânsito.'),
  [('✉️', 'letter', 'carta', 'Soa como “LÉ-ter”.'), ('📄', 'papers', 'documentos', 'Soa como “PÊI-perz”.'), ('✈️', 'plane', 'avião', 'Soa como “PLÊIN”.'),
   ('☕', 'cafe', 'café (casa)', 'Soa como “ka-FÊI”.'), ('🚪', 'exit', 'saída', 'Soa como “ÉK-sit”.'), ('🎟️', 'ticket', 'passagem', 'Soa como “TÍ-kit”.')],
  [('✉️', 'letter', 'carta', 'I still need the letter.', 'Ainda preciso da carta.'),
   ('📄', 'papers', 'documentos', 'I do not have my papers yet.', 'Ainda não tenho meus documentos.'),
   ('✈️', 'plane', 'avião', 'The plane already left.', 'O avião já partiu.'),
   ('☕', 'cafe', 'café', 'I no longer work at the cafe.', 'Eu não trabalho mais no café.'),
   ('🚪', 'exit', 'saída', 'The exit is already closed.', 'A saída já está fechada.')],
  [['Rick', 'Do you have your papers?', 'Você tem seus documentos?'],
   ['Ilsa', 'Not yet. I still need a letter of transit.', 'Ainda não. Ainda preciso de uma carta de trânsito.'],
   ['Rick', 'And your ticket?', 'E a sua passagem?'],
   ['Ilsa', 'I already have it.', 'Eu já tenho.'],
   ['Rick', 'Do you still live in Paris?', 'Você ainda mora em Paris?'],
   ['Ilsa', 'No, I no longer live there.', 'Não, não moro mais lá.'],
   ['Rick', 'Has the plane left?', 'O avião já partiu?'],
   ['Ilsa', 'Yes, it already left.', 'Sim, já partiu.']],
  [Q('What does Ilsa still need?', 'O que a Ilsa ainda precisa?', 1, ('✉️', 'A letter of transit'), ('🍕', 'A pizza'), ('🧳', 'A suitcase')),
   Q('What does she already have?', 'O que ela já tem?', 3, ('🎟️', 'Her ticket'), ('🏠', 'A house'), ('💍', 'A ring')),
   Q('Where does she no longer live?', 'Onde ela não mora mais?', 5, ('🗼', 'In Paris'), ('🗽', 'In New York'), ('🏰', 'In London'))],
  verbs=None, lab=None)

# 372 · plenty of · lots of · hardly any (só a obra)
X(7081266, ('Marian', 'Robin'), ['polly', 'robin'],
  W('Robin Hood', '📖 Lenda', 'séc. XV', 'uma lenda inglesa sobre um arqueiro que vive na floresta de Sherwood e ajuda os pobres.', 'quantidades: plenty of, lots of e hardly any',
    'castle', ['🏹', '🌲', '💰'], 'There are plenty of volunteers.', 'Há muitos voluntários.'))

# 374 · gírias (obra e palavras)
X(7920038, ('Cher', 'Josh'), ['polly', 'tom'],
  W('Clueless', '🎬 Filme', 1995, 'uma comédia americana sobre uma adolescente rica de Beverly Hills, inspirada no romance Emma, de Jane Austen.', 'gírias do dia a dia: awesome, totally, for real',
    'castle', ['👗', '🚗', '📱'], 'That is totally awesome!', 'Isso é totalmente incrível!'),
  vocab=[('🎤', 'concert', 'show', 'Soa como “KÓN-sert”.'), ('👗', 'outfit', 'visual', 'Soa como “ÁUT-fit”.'), ('🎟️', 'ticket', 'ingresso', 'Soa como “TÍ-kit”.'),
         ('🚗', 'ride', 'carona', 'Soa como “RÁID”.'), ('💘', 'crush', 'paixonite', 'Soa como “KRÂX”.'), ('🛍️', 'sale', 'liquidação', 'Soa como “SÊIL”.')])

# 376 · as … as
X(7081269, ('Constanze', 'Salieri'), ['polly', 'tom'],
  W('Amadeus', '🎬 Filme', 1984, 'um filme sobre o compositor Antonio Salieri e sua rivalidade com Mozart, baseado numa peça de Peter Shaffer.', 'comparar com as … as e not as … as',
    'castle', ['🎻', '🎹', '🎼'], 'His music is as good as any.', 'A música dele é tão boa quanto qualquer outra.'),
  [('🎭', 'opera', 'ópera', 'Soa como “Ó-pe-ra”.'), ('🎼', 'symphony', 'sinfonia', 'Soa como “SÍM-fo-ni”.'), ('🎻', 'violin', 'violino', 'Soa como “vai-o-LÍN”.'),
   ('✍️', 'composer', 'compositor', 'Soa como “kom-PÔU-zer”.'), ('😠', 'rival', 'rival', 'Soa como “RÁI-vol”.'), ('✨', 'genius', 'gênio', 'Soa como “DJÍ-ni-es”.')],
  [('🎼', 'as famous as', 'tão famoso quanto', 'His music is as famous as mine.', 'A música dele é tão famosa quanto a minha.'),
   ('🎭', 'as loud as', 'tão alto quanto', 'The opera is as loud as the symphony.', 'A ópera é tão alta quanto a sinfonia.'),
   ('🎻', 'not as fast as', 'não tão rápido quanto', 'The piano is not as fast as the violin.', 'O piano não é tão rápido quanto o violino.'),
   ('✨', 'as good as', 'tão bom quanto', 'His melody is as good as any.', 'A melodia dele é tão boa quanto qualquer outra.'),
   ('😠', 'as clever as', 'tão esperto quanto', 'The rival is as clever as a fox.', 'O rival é esperto como uma raposa.')],
  [['Constanze', 'Is Wolfgang\'s music as famous as yours?', 'A música do Wolfgang é tão famosa quanto a sua?'],
   ['Salieri', 'It is as famous as mine, almost.', 'É quase tão famosa quanto a minha.'],
   ['Constanze', 'Is the opera as loud as the symphony?', 'A ópera é tão alta quanto a sinfonia?'],
   ['Salieri', 'The opera is as loud as the symphony sometimes.', 'Às vezes a ópera é tão alta quanto a sinfonia.'],
   ['Constanze', 'And the piano?', 'E o piano?'],
   ['Salieri', 'It is not as fast as the violin.', 'Não é tão rápido quanto o violino.'],
   ['Constanze', 'But his melody is as good as any.', 'Mas a melodia dele é tão boa quanto qualquer outra.'],
   ['Salieri', 'I agree.', 'Concordo.']],
  [Q('Whose music is almost as famous?', 'A música de quem é quase tão famosa?', 1, ('🎼', 'Wolfgang\'s'), ('🎹', 'The neighbor\'s'), ('🎸', 'A rock band\'s')),
   Q('What is not as fast as the violin?', 'O que não é tão rápido quanto o violino?', 5, ('🎹', 'The piano'), ('🎺', 'The trumpet'), ('🥁', 'The drum')),
   Q('What is as good as any?', 'O que é tão bom quanto qualquer outra?', 6, ('🎶', 'His melody'), ('🎤', 'His voice'), ('🎬', 'His film'))],
  verbs=None, lab=None)

# 378 · might / may (só a obra)
X(7081272, ('Jo', 'Bill'), ['polly', 'tom'],
  W('Twister', '🎬 Filme', 1996, 'um filme de aventura americano sobre cientistas que perseguem tornados nas planícies dos Estados Unidos.', 'possibilidades: might, may e might not',
    'castle', ['🌪️', '⛈️', '🚙'], 'A storm might come.', 'Uma tempestade pode vir.'))

# 380 · superlativos + in the world (só a obra)
X(7081273, ('Arnold', 'Ms Frizzle'), ['tommy', 'matilda'],
  W('The Magic School Bus', '📺 Série', 1994, 'uma série animada americana sobre uma professora que leva a turma em viagens mágicas num ônibus escolar.', 'recordes do planeta: the hottest, the coldest e one of the…',
    'school', ['🚌', '🌍', '🔬'], 'The Sahara is the hottest desert.', 'O Saara é o deserto mais quente.'))
