# Reescrita dos episódios B1 313–330 (ver ovrb1.py e ovrb1_251_262.py).
from v3.ovrb1 import OVR, L
from v3.ovrb1_251_262 import C, F, W, WORKS

# ---------------------------------------------------------------- 313 / 314
F(930044, [['Throw away what no longer sparks joy.', 'Jogue fora o que não traz mais alegria.'], ['Throw out the broken lamp too.', 'Jogue fora também o abajur quebrado.'],
           ['Throw on a coat, it is cold outside.', 'Vista um casaco, está frio lá fora.'], ['I feel sick, I might throw up.', 'Estou enjoado, posso vomitar.']])

W(7930044, 'Mary Poppins', '🎬 Filme · 1964', 'Mary Poppins é um filme musical da Disney de 1964, baseado nos livros de P. L. Travers: uma babá mágica chega a uma casa de Londres e muda a rotina das crianças.', ['☂️', '🪁', '🎠'], 'toyshop')
C(7930044, ('Mary', 'Bert'), ['polly', 'tom'], 'kitchen', 'Na cozinha da casa dos Banks, Mary e Bert improvisam lanche e brincadeiras.',
  ('🪁', 'kite', 'pipa', 'Throw back the kite string.', 'Devolva a linha da pipa.'),
  [('☂️', 'umbrella', 'guarda-chuva', 'Soa como “am-BRÉ-la”.'), ('🏠', 'chimney', 'chaminé', 'Soa como “TCHÍM-ni”.'), ('🥪', 'sandwich', 'sanduíche', 'Soa como “SÉN-uitch”.'),
   ('🧸', 'toy', 'brinquedo', 'Soa como “TÓI”.'), ('🛏️', 'nursery', 'quarto das crianças', 'Soa como “NÂR-se-ri”.'), ('👩‍🍼', 'nanny', 'babá', 'Soa como “NÉ-ni”.')],
  [('tidy', '🧹', 'arrumar', 'Tidy the nursery.', 'Tidy to the nursery.', 'I tidied.', 'Arrumei.', 'tidy **+ objeto**.'),
   ('sing', '🎵', 'cantar', 'We sing together.', 'We sings together.', 'We sang.', 'Cantamos.', 'sing → **sang**.'),
   ('fly', '🪁', 'voar', 'The kite flies.', 'The kite fly.', 'It flew.', 'Voou.', 'fly → **flew**.'),
   ('mix', '🥄', 'misturar', 'Mix the batter.', 'Mix to the batter.', 'I mixed it.', 'Misturei.', 'mix **+ objeto**.')],
  [['Mary', 'Throw together a quick snack, Bert.', 'Improvise um lanche rápido, Bert.'], ['Bert', 'I will throw together some sandwiches.', 'Vou improvisar uns sanduíches.'],
   ['Mary', 'Do not throw your toys around the nursery.', 'Não jogue seus brinquedos por todo o quarto.'], ['Bert', 'The kite will throw me off if the wind changes.', 'A pipa vai me desequilibrar se o vento mudar.'],
   ['Mary', 'Throw the ball back to the children.', 'Devolva a bola para as crianças.'], ['Bert', 'They throw it back every single time.', 'Eles devolvem toda vez.'],
   ['Mary', 'Throw off that bad mood, Bert.', 'Livre-se desse mau humor, Bert.'], ['Bert', 'Done. Let us throw a party.', 'Pronto. Vamos dar uma festa.']],
  [('What does Mary want Bert to throw together?', 'O que Mary quer que Bert improvise?', [('🥪', 'A snack'), ('🏠', 'A house'), ('🪁', 'A kite')], 0, 0, 'Mary diz: “Throw together a quick snack.”'),
   ('What do the children throw back?', 'O que as crianças devolvem?', [('⚽', 'The ball'), ('🧸', 'A toy'), ('🥪', 'A sandwich')], 0, 5, 'Bert diz: “They throw it back every single time.”'),
   ('What does Bert want to throw?', 'O que Bert quer dar?', [('🎉', 'A party'), ('🥎', 'A stone'), ('🪁', 'A kite')], 0, 7, 'Bert diz: “Let us throw a party.”')],
  L('mp', 'Laboratório de sons: umbrella, chimney e sandwich', 'u soa â; ch soa tch; a soa é.', 'Em chimney, o ch soa tch.',
    [('umbrella', 'am-BRÉ-la', 'guarda-chuva', 'u = â', 'ambulance', 'ÉM-biu-lans'), ('chimney', 'TCHÍM-ni', 'chaminé', 'ch = tch', 'chimp', 'TCHÍMP'), ('sandwich', 'SÉN-uitch', 'sanduíche', 'a = é', 'sand', 'SÉND')]),
  [['Is the nursery tidy at last?', 'O quarto das crianças está arrumado enfim?'], ['Spotless, in the blink of an eye.', 'Impecável, num piscar de olhos.'],
   ['Then tea can be served on time.', 'Então o chá pode ser servido na hora.'], ['Practically perfect in every way.', 'Praticamente perfeito em todos os sentidos.']])

# ---------------------------------------------------------------- 315 / 316
F(81046, [['It is a dark night, isn’t it?', 'É uma noite escura, não é?'], ['You like old poems, don’t you?', 'Você gosta de poemas antigos, não gosta?'],
          ['She can read it aloud, can’t she?', 'Ela sabe ler em voz alta, não sabe?'], ['It is a long poem, isn’t it?', 'É um poema longo, não é?']])

W(7081046, 'Peter Pan', '📚 Livro · 1911', 'Peter Pan, ou O Menino que Não Queria Crescer, é uma história de J. M. Barrie, que virou peça em 1904 e livro em 1911: Peter leva Wendy e os irmãos à Terra do Nunca.', ['🧚', '🏴‍☠️', '🌟'], 'castle')
C(7081046, ('Wendy', 'Peter'), ['wendy', 'peter'], 'bedroom', 'No quarto das crianças, Wendy e Peter confirmam planos com tags no fim das frases.',
  ('✨', 'dust', 'pó de fada', 'Pass the dust, will you?', 'Passe o pó de fada, pode ser?'),
  [('🧚', 'fairy', 'fada', 'Soa como “FÉ-ri”.'), ('🏴‍☠️', 'pirate', 'pirata', 'Soa como “PÁI-rit”.'), ('🐊', 'crocodile', 'crocodilo', 'Soa como “KRÓ-ko-dáil”.'),
   ('🌟', 'star', 'estrela', 'Soa como “STAR”.'), ('🏝️', 'island', 'ilha', 'Soa como “ÁI-lend”.'), ('👤', 'shadow', 'sombra', 'Soa como “SHÉ-dôu”.')],
  [('believe', '🙏', 'acreditar', 'I believe in fairies.', 'I believe on fairies.', 'I believed.', 'Acreditei.', 'believe **in**.'),
   ('clap', '👏', 'bater palmas', 'Clap if you believe.', 'Claps if you believe.', 'I clapped.', 'Bati palmas.', 'plural/imperativo: **clap**.'),
   ('shine', '✨', 'brilhar', 'The star shines.', 'The star shine.', 'It shone.', 'Brilhou.', 'shine → **shone**.'),
   ('tell', '🗣️', 'contar', 'Tell me a story.', 'Tell to me a story.', 'I told you.', 'Contei a você.', 'tell → **told**.')],
  [['Wendy', 'I am late, aren’t I?', 'Estou atrasada, não estou?'], ['Peter', 'Let us fly now, shall we?', 'Vamos voar agora, certo?'],
   ['Wendy', 'Do not leave without me, will you?', 'Não vá sem mim, está bem?'], ['Peter', 'You do not doubt the fairies, do you?', 'Você não duvida das fadas, duvida?'],
   ['Wendy', 'I do believe. I am not silly, am I?', 'Eu acredito. Não sou boba, sou?'], ['Peter', 'Close the window, will you?', 'Feche a janela, pode ser?'],
   ['Wendy', 'Let us take John and Michael, shall we?', 'Vamos levar John e Michael, certo?'], ['Peter', 'You are ready, aren’t you?', 'Você está pronta, não está?']],
  [('Is Wendy late?', 'Wendy está atrasada?', [('⏰', 'Yes, she thinks so'), ('😴', 'No, she sleeps'), ('🎉', 'She is early')], 0, 0, 'Wendy diz: “I am late, aren’t I?”'),
   ('What does Peter ask her to close?', 'O que Peter pede que ela feche?', [('🪟', 'The window'), ('🚪', 'The door'), ('📖', 'A book')], 0, 5, 'Peter diz: “Close the window, will you?”'),
   ('Who else do they take?', 'Quem mais levam?', [('👦', 'John and Michael'), ('🧚', 'A fairy'), ('🏴‍☠️', 'A pirate')], 0, 6, 'Wendy diz: “Let us take John and Michael.”')],
  L('pp', 'Laboratório de sons: fairy, pirate e island', 'a soa é; i soa ái; s é mudo.', 'Em island, o s é mudo.',
    [('fairy', 'FÉ-ri', 'fada', 'a = é', 'fury', 'FIÚ-ri'), ('pirate', 'PÁI-rit', 'pirata', 'i = ái', 'parrot', 'PÉ-rot'), ('island', 'ÁI-lend', 'ilha', 's mudo', 'is land', 'ÍZ-lénd')]),
  [['Will the children remember the way back?', 'As crianças vão lembrar o caminho de volta?'], ['Second star to the right, I believe.', 'Segunda estrela à direita, acredito.'],
   ['Then we follow it until morning.', 'Então a seguimos até de manhã.'], ['And we do not look down, do we?', 'E não olhamos para baixo, certo?']])

# ---------------------------------------------------------------- 317 / 318
F(82203, [['I worry about my privacy online.', 'Me preocupo com a minha privacidade online.'], ['We depend on phones for everything.', 'Dependemos do celular para tudo.'],
          ['But we benefit from them too.', 'Mas também nos beneficiamos deles.'], ['On the one hand, they connect us.', 'Por um lado, eles nos conectam.']])

W(7082203, 'Ex Machina', '🎬 Filme · 2014', 'Ex Machina é um filme de ficção científica de 2014, escrito e dirigido por Alex Garland: um jovem programador é chamado para testar se uma robô consegue pensar como uma pessoa.', ['🤖', '🧠', '🔬'], 'cave')
C(7082203, ('Caleb', 'Ava'), ['tom', 'polly'], 'office', 'Numa sala de testes, Caleb e Ava debatem o que a máquina pode ou não pensar.',
  ('🔬', 'lab', 'laboratório', 'According to the lab, it works.', 'Segundo o laboratório, funciona.'),
  [('🤖', 'robot', 'robô', 'Soa como “RÔU-bót”.'), ('💻', 'code', 'código', 'Soa como “KÔUD”.'), ('🧠', 'mind', 'mente', 'Soa como “MÁIND”.'),
   ('🧪', 'experiment', 'experimento', 'Soa como “ik-SPÉ-ri-ment”.'), ('🪞', 'mirror', 'espelho', 'Soa como “MÍ-rer”.'), ('📋', 'test', 'teste', 'Soa como “TÉST”.')],
  [('program', '💻', 'programar', 'They program the robot.', 'They programs the robot.', 'They programmed it.', 'Programaram.', 'plural: **program**.'),
   ('test', '📋', 'testar', 'We test her mind.', 'We test to her mind.', 'We tested it.', 'Testamos.', 'test **+ objeto**.'),
   ('prove', '✅', 'provar', 'Prove it to me.', 'Prove me it.', 'I proved it.', 'Provei.', 'prove **it to me**.'),
   ('observe', '👀', 'observar', 'I observe her closely.', 'I observe to her closely.', 'I observed her.', 'Observei-a.', 'observe **+ objeto**.')],
  [['Caleb', 'Some experts argue that machines can think.', 'Alguns especialistas defendem que máquinas podem pensar.'], ['Ava', 'According to the manual, I am only code.', 'Segundo o manual, sou só código.'],
   ['Caleb', 'The company claims that you are not alive.', 'A empresa afirma que você não está viva.'], ['Ava', 'Let me point out that I ask questions too.', 'Deixe-me apontar que eu também faço perguntas.'],
   ['Caleb', 'According to the test, you passed.', 'De acordo com o teste, você passou.'], ['Ava', 'Do you argue that I am real?', 'Você defende que eu sou real?'],
   ['Caleb', 'I claim nothing. I only point out what I see.', 'Não afirmo nada. Só aponto o que vejo.'], ['Ava', 'According to you, what do you see?', 'Segundo você, o que vê?']],
  [('What do some experts argue?', 'O que alguns especialistas defendem?', [('🧠', 'Machines can think'), ('🌍', 'Earth is flat'), ('🚗', 'Cars can fly')], 0, 0, 'Caleb diz: “Some experts argue that machines can think.”'),
   ('What does the manual say Ava is?', 'O que o manual diz que Ava é?', [('💻', 'Only code'), ('👩', 'A woman'), ('🐱', 'A cat')], 0, 1, 'Ava diz: “I am only code.”'),
   ('What did Ava do on the test?', 'O que Ava fez no teste?', [('✅', 'She passed'), ('❌', 'She failed'), ('🏃', 'She left')], 0, 4, 'Caleb diz: “you passed.”')],
  L('xm', 'Laboratório de sons: robot, mind e mirror', 'o soa ôu; i soa ái; i soa í.', 'Em mind, o i soa ái.',
    [('robot', 'RÔU-bót', 'robô', 'o = ôu', 'rabbit', 'RÉ-bit'), ('mind', 'MÁIND', 'mente', 'i = ái', 'mend', 'MÉND'), ('mirror', 'MÍ-rer', 'espelho', 'i = í', 'mere', 'MÍR')]),
  [['Does Ava want to leave the building?', 'Ava quer sair do prédio?'], ['She asks about the outside world often.', 'Ela pergunta sempre sobre o mundo lá fora.'],
   ['Then Caleb should report that.', 'Então Caleb deve relatar isso.'], ['He will, once he understands why.', 'Ele vai relatar, quando entender o motivo.']])

# ---------------------------------------------------------------- 319 / 320
F(82204, [['Everyone should have a decent home.', 'Todos deveriam ter uma moradia digna.'], ['Workers deserve a fair wage.', 'Trabalhadores merecem um salário justo.'],
          ['We must close the gap between rich and poor.', 'Precisamos reduzir a distância entre ricos e pobres.'], ['Many families suffer from hunger.', 'Muitas famílias sofrem de fome.']])

W(7082204, 'Moneyball', '🎬 Filme · 2011', 'Moneyball é um filme de 2011, dirigido por Bennett Miller e baseado no livro de Michael Lewis: um dirigente de beisebol usa estatísticas para montar um time competitivo.', ['⚾', '📊', '🏟️'], 'viaduct')
C(7082204, ('Billy', 'Peter'), ['tom', 'tommy'], 'office', 'Na sala do clube, Billy e Peter leem os números da temporada.',
  ('📊', 'chart', 'gráfico', 'The line on the chart has risen.', 'A linha do gráfico subiu.'),
  [('⚾', 'baseball', 'beisebol', 'Soa como “BÊIS-ból”.'), ('👥', 'fans', 'torcedores', 'Soa como “FÉNZ”.'), ('💲', 'salary', 'salário', 'Soa como “SÉ-la-ri”.'),
   ('🏟️', 'stadium', 'estádio', 'Soa como “STÊI-dium”.'), ('📉', 'trend', 'tendência', 'Soa como “TRÉND”.'), ('🧮', 'average', 'média', 'Soa como “É-ve-ridj”.')],
  [('count', '🔢', 'contar', 'Count the wins.', 'Count to the wins.', 'I counted.', 'Contei.', 'count **+ objeto**.'),
   ('compare', '⚖️', 'comparar', 'Compare the numbers.', 'Compare to the numbers.', 'I compared.', 'Comparei.', 'compare **+ objeto**.'),
   ('improve', '📈', 'melhorar', 'Our score improves.', 'Our score improve.', 'It improved.', 'Melhorou.', 'he/she/it **improves**.'),
   ('measure', '📏', 'medir', 'Measure the results.', 'Measure to the results.', 'I measured.', 'Medi.', 'measure **+ objeto**.')],
  [['Peter', 'Our win rate has risen since April.', 'Nossa taxa de vitórias subiu desde abril.'], ['Billy', 'Attendance fell last month, though.', 'Mas o público caiu no mês passado.'],
   ['Peter', 'The number of fans is increasing again.', 'O número de torcedores está aumentando de novo.'], ['Billy', 'Ticket prices decreased slightly.', 'O preço dos ingressos diminuiu um pouco.'],
   ['Peter', 'The average score has risen all season.', 'A pontuação média subiu a temporada toda.'], ['Billy', 'Our spending fell, but our wins increased.', 'Nosso gasto caiu, mas as vitórias aumentaram.'],
   ['Peter', 'The rate of errors decreased too.', 'A taxa de erros também diminuiu.'], ['Billy', 'Then the trend is clear.', 'Então a tendência é clara.']],
  [('What has risen since April?', 'O que subiu desde abril?', [('🏆', 'The win rate'), ('🌧️', 'The rain'), ('🎟️', 'Ticket prices')], 0, 0, 'Peter diz: “Our win rate has risen since April.”'),
   ('What fell last month?', 'O que caiu no mês passado?', [('👥', 'Attendance'), ('🏆', 'Wins'), ('📈', 'The score')], 0, 1, 'Billy diz: “Attendance fell last month.”'),
   ('What decreased slightly?', 'O que diminuiu um pouco?', [('🎟️', 'Ticket prices'), ('🥤', 'Drinks'), ('👥', 'Fans')], 0, 3, 'Billy diz: “Ticket prices decreased slightly.”')],
  L('mb', 'Laboratório de sons: baseball, stadium e average', 'a soa êi; a soa êi; a soa é.', 'Em stadium, o a soa êi.',
    [('baseball', 'BÊIS-ból', 'beisebol', 'a = êi', 'basement', 'BÊIS-ment'), ('stadium', 'STÊI-dium', 'estádio', 'a = êi', 'studio', 'STIÚ-diôu'), ('average', 'É-ve-ridj', 'média', 'a = é', 'avenue', 'É-ve-niu')]),
  [['Will the team keep this form next year?', 'O time vai manter esse ritmo no ano que vem?'], ['If the numbers stay honest, yes.', 'Se os números continuarem honestos, sim.'],
   ['Then the board must stop doubting.', 'Então a diretoria precisa parar de duvidar.'], ['They will, after one more win.', 'Vão parar, depois de mais uma vitória.']])

# ---------------------------------------------------------------- 321 / 322
F(930045, [['I run a small business with my sister.', 'Administro um pequeno negócio com minha irmã.'], ['Do you make a profit already?', 'Vocês já têm lucro?'],
           ['We almost ran out of stock last week.', 'Quase ficamos sem estoque semana passada.'], ['Then you need a partner to grow.', 'Então você precisa de um sócio para crescer.']])

W(7930045, 'The Pursuit of Happyness', '🎬 Filme · 2006', 'À Procura da Felicidade é um filme de 2006, dirigido por Gabriele Muccino: um pai luta para conseguir um estágio numa corretora e sustentar o filho pequeno.', ['💼', '🚌', '👔'], 'viaduct')
C(7930045, ('Chris', 'Christopher'), ['tom', 'tommy'], 'street', 'Na calçada, Chris e o filho correm para o ponto de ônibus e ensaiam a entrevista.',
  ('💼', 'briefcase', 'pasta', 'Run through it with the briefcase.', 'Repasse isso com a pasta na mão.'),
  [('🚌', 'bus stop', 'ponto de ônibus', 'Soa como “BÂS-stóp”.'), ('🗣️', 'interview', 'entrevista', 'Soa como “ÍN-ter-viu”.'), ('👔', 'tie', 'gravata', 'Soa como “TÁI”.'),
   ('💸', 'debt', 'dívida', 'Soa como “DÉT”.'), ('🛌', 'shelter', 'abrigo', 'Soa como “SHÉL-ter”.'), ('💹', 'broker', 'corretor', 'Soa como “BRÔU-ker”.')],
  [('study', '📖', 'estudar', 'I study at night.', 'I studies at night.', 'I studied.', 'Estudei.', 'I **study**.'),
   ('sleep', '😴', 'dormir', 'We sleep at the shelter.', 'We sleeps at the shelter.', 'We slept.', 'Dormimos.', 'sleep → **slept**.'),
   ('smile', '😀', 'sorrir', 'Smile at the manager.', 'Smile to the manager.', 'I smiled.', 'Sorri.', 'smile **at**.'),
   ('save', '💰', 'economizar', 'We save every dollar.', 'We saves every dollar.', 'We saved.', 'Economizamos.', 'plural: **save**.')],
  [['Chris', 'Run up to the bus stop, we are late.', 'Corra até o ponto de ônibus, estamos atrasados.'], ['Christopher', 'I nearly ran into a lamp post.', 'Quase bati num poste.'],
   ['Chris', 'Be careful, a bus can run over your foot.', 'Cuidado, um ônibus pode passar por cima do seu pé.'], ['Christopher', 'Let us run through the plan for the interview.', 'Vamos repassar o plano da entrevista.'],
   ['Chris', 'Good idea. I run through it every night.', 'Boa ideia. Eu repasso toda noite.'], ['Christopher', 'We can run up a debt if we are careless.', 'Podemos acumular uma dívida se formos descuidados.'],
   ['Chris', 'I will run into the broker tomorrow.', 'Vou topar com o corretor amanhã.'], ['Christopher', 'Then run through your best answers again.', 'Então repasse suas melhores respostas de novo.']],
  [('Where must they run?', 'Para onde devem correr?', [('🚌', 'To the bus stop'), ('🏫', 'To school'), ('🏠', 'Home')], 0, 0, 'Chris diz: “Run up to the bus stop.”'),
   ('What do they run through?', 'O que repassam?', [('🗣️', 'The plan for the interview'), ('📺', 'A TV show'), ('🗺️', 'A map')], 0, 3, 'Christopher diz: “run through the plan for the interview.”'),
   ('What can they run up if careless?', 'O que podem acumular se forem descuidados?', [('💸', 'A debt'), ('🏃', 'A race'), ('🪜', 'Stairs')], 0, 5, 'Christopher diz: “run up a debt.”')],
  L('ph', 'Laboratório de sons: interview, shelter e debt', 'i soa í; sh soa x; b é mudo.', 'Em debt, o b é mudo.',
    [('interview', 'ÍN-ter-viu', 'entrevista', 'i = í', 'entrance', 'ÉN-trens'), ('shelter', 'SHÉL-ter', 'abrigo', 'sh = x', 'welter', 'UÉL-ter'), ('debt', 'DÉT', 'dívida', 'b mudo', 'dead', 'DÉD')]),
  [['Did the manager remember Chris from before?', 'O gerente lembrou de Chris de antes?'], ['He did, and he asked about the tie.', 'Lembrou, e perguntou sobre a gravata.'],
   ['Then the interview starts well.', 'Então a entrevista começa bem.'], ['One good laugh can open a door.', 'Uma boa risada pode abrir uma porta.']])

# ---------------------------------------------------------------- 323 / 324
F(82209, [['Anyway, how was your trip?', 'Enfim, como foi sua viagem?'], ['By the way, did you call Mum?', 'A propósito, você ligou para a mamãe?'],
          ['Speaking of Mum, she sends hugs.', 'Falando da mamãe, ela manda abraços.'], ['That reminds me, I owe her a visit.', 'Isso me lembra que devo uma visita a ela.']])

W(7082209, 'Forrest Gump', '🎬 Filme · 1994', 'Forrest Gump é um filme de 1994, dirigido por Robert Zemeckis: num banco de ponto de ônibus, Forrest conta a história da sua vida a quem senta ao lado.', ['🪶', '🚌', '🍫'], 'toyshop')
C(7082209, ('Forrest', 'Jenny'), ['tom', 'polly'], 'park', 'No banco do ponto de ônibus, Forrest conta sua história e se perde no assunto.',
  ('🪶', 'feather', 'pena', 'Back to the feather.', 'Voltando à pena.'),
  [('🍫', 'chocolate', 'chocolate', 'Soa como “TCHÓK-lit”.'), ('🚌', 'bus', 'ônibus', 'Soa como “BÂS”.'), ('👟', 'shoe', 'sapato', 'Soa como “SHÚ”.'),
   ('🦐', 'shrimp', 'camarão', 'Soa como “SHRÍMP”.'), ('📖', 'story', 'história', 'Soa como “STÓ-ri”.'), ('🏈', 'football', 'futebol americano', 'Soa como “FÚT-ból”.')],
  [('sit', '🪑', 'sentar', 'I sit on the bench.', 'I sits on the bench.', 'I sat.', 'Sentei.', 'sit → **sat**.'),
   ('talk', '🗣️', 'conversar', 'We talk for hours.', 'We talks for hours.', 'We talked.', 'Conversamos.', 'plural: **talk**.'),
   ('chat', '💬', 'bater papo', 'We chat on the bench.', 'We chats on the bench.', 'We chatted.', 'Batemos papo.', 'plural: **chat**.'),
   ('ride', '🚌', 'andar de', 'I ride the bus.', 'I rides the bus.', 'I rode.', 'Andei.', 'ride → **rode**.')],
  [['Forrest', 'As I was saying, I sit on this bench every day.', 'Como eu dizia, sento neste banco todo dia.'], ['Jenny', 'Where was I? Oh, I asked about your shoes.', 'Onde eu estava? Ah, perguntei dos seus sapatos.'],
   ['Forrest', 'My shoes? That is off topic, Jenny.', 'Meus sapatos? Isso é fugir do assunto, Jenny.'], ['Jenny', 'Back to the bench, then.', 'Voltando ao banco, então.'],
   ['Forrest', 'As I was saying, the bus comes at noon.', 'Como eu dizia, o ônibus passa ao meio-dia.'], ['Jenny', 'Back to you. Where was I? The story of the feather.', 'Voltando a você. Onde eu estava? A história da pena.'],
   ['Forrest', 'Sorry, I went off topic again.', 'Desculpe, saí do assunto de novo.'], ['Jenny', 'Never mind. Back to the story.', 'Deixa para lá. Voltando à história.']],
  [('Where does Forrest sit?', 'Onde Forrest senta?', [('🪑', 'On a bench'), ('🛋️', 'On a sofa'), ('🏖️', 'On the sand')], 0, 0, 'Forrest diz: “I sit on this bench every day.”'),
   ('When does the bus come?', 'Quando o ônibus passa?', [('🕛', 'At noon'), ('🌙', 'At night'), ('🌅', 'At dawn')], 0, 4, 'Forrest diz: “the bus comes at noon.”'),
   ('What story are they back to?', 'A que história voltam?', [('🪶', 'The feather'), ('🍫', 'The chocolates'), ('👟', 'The shoes')], 0, 5, 'Jenny diz: “The story of the feather.”')],
  L('fg', 'Laboratório de sons: chocolate, shrimp e football', 'o soa ó; sh soa x; oo soa ú.', 'Em shrimp, o sh soa x.',
    [('chocolate', 'TCHÓK-lit', 'chocolate', 'o = ó', 'chalet', 'SHÉ-lêi'), ('shrimp', 'SHRÍMP', 'camarão', 'sh = x', 'shrink', 'SHRÍNK'), ('football', 'FÚT-ból', 'futebol americano', 'oo = ú', 'feet', 'FÍT')]),
  [['Did anyone else sit on the bench today?', 'Mais alguém sentou no banco hoje?'], ['One lady, with a suitcase and a smile.', 'Uma senhora, com mala e sorriso.'],
   ['And did she listen to the whole story?', 'E ela ouviu a história inteira?'], ['Every word, until her bus arrived.', 'Cada palavra, até o ônibus dela chegar.']])

# ---------------------------------------------------------------- 325 / 326
F(82210, [['Really? Tell me more about Vienna.', 'Sério? Conte mais sobre Viena.'], ['Go on, I want to hear it all.', 'Continue, quero ouvir tudo.'],
          ['How interesting, I never knew that.', 'Que interessante, eu nunca soube disso.'], ['I wonder what happened next.', 'Fico curiosa para saber o que aconteceu depois.']])

W(7082210, 'One Thousand and One Nights', '📖 Contos · Idade Média', 'As Mil e Uma Noites é uma coleção de contos do Oriente Médio e do sul da Ásia; no quadro central, Scheherazade conta uma história por noite ao sultão.', ['🌙', '🏺', '🐪'], 'castle')
C(7082210, ('Scheherazade', 'Sultan'), ['polly', 'tom'], 'bedroom', 'Ao anoitecer, o sultão faz perguntas para saber o final da história de Scheherazade.',
  ('🏺', 'jar', 'jarro', 'What happened next to the jar?', 'O que aconteceu depois com o jarro?'),
  [('🌙', 'night', 'noite', 'Soa como “NÁIT”.'), ('🧑‍🌾', 'merchant', 'mercador', 'Soa como “MÉR-tchent”.'), ('📖', 'tale', 'conto', 'Soa como “TÊIL”.'),
   ('🐪', 'camel', 'camelo', 'Soa como “KÉ-mol”.'), ('🗣️', 'voice', 'voz', 'Soa como “VÓIS”.'), ('🌅', 'sunrise', 'nascer do sol', 'Soa como “SÂN-ráiz”.')],
  [('end', '🔚', 'terminar', 'The tale ends here.', 'The tale end here.', 'It ended.', 'Terminou.', 'he/she/it **ends**.'),
   ('wake', '⏰', 'acordar', 'I wake at sunrise.', 'I wakes at sunrise.', 'I woke.', 'Acordei.', 'wake → **woke**.'),
   ('hear', '👂', 'ouvir', 'I hear a voice.', 'I hears a voice.', 'I heard it.', 'Ouvi.', 'hear → **heard**.'),
   ('break', '💥', 'quebrar', 'The jar breaks.', 'The jar break.', 'It broke.', 'Quebrou.', 'break → **broke**.')],
  [['Sultan', 'What happened next, Scheherazade?', 'O que aconteceu depois, Scheherazade?'], ['Scheherazade', 'And then the merchant opened the jar.', 'E então o mercador abriu o jarro.'],
   ['Sultan', 'How come he opened it?', 'Como assim ele abriu?'], ['Scheherazade', 'He heard a voice inside.', 'Ele ouviu uma voz lá dentro.'],
   ['Sultan', 'And then? Keep talking.', 'E então? Continue falando.'], ['Scheherazade', 'The jar broke, and a genie flew out.', 'O jarro quebrou, e um gênio saiu voando.'],
   ['Sultan', 'How come you stop at the best part?', 'Como assim você para na melhor parte?'], ['Scheherazade', 'Because the sun is rising. Tomorrow I keep talking.', 'Porque o sol está nascendo. Amanhã continuo falando.']],
  [('Who opened the jar?', 'Quem abriu o jarro?', [('🧑‍🌾', 'The merchant'), ('👑', 'The sultan'), ('🐪', 'The camel')], 0, 1, 'Scheherazade diz: “the merchant opened the jar.”'),
   ('What did he hear inside?', 'O que ouviu lá dentro?', [('🗣️', 'A voice'), ('🎵', 'Music'), ('🐕', 'A dog')], 0, 3, 'Scheherazade diz: “He heard a voice inside.”'),
   ('Why does she stop?', 'Por que ela para?', [('🌅', 'The sun is rising'), ('😴', 'She is tired'), ('🍽️', 'Dinner is ready')], 0, 7, 'Scheherazade diz: “the sun is rising.”')],
  L('sn', 'Laboratório de sons: merchant, camel e voice', 'er soa ér; a soa é; oi soa ói.', 'Em voice, o oi soa ói.',
    [('merchant', 'MÉR-tchent', 'mercador', 'ch = tch', 'march', 'MÁRTCH'), ('camel', 'KÉ-mol', 'camelo', 'a = é', 'camera', 'KÉ-me-ra'), ('voice', 'VÓIS', 'voz', 'oi = ói', 'vase', 'VÊIS')]),
  [['Does the sultan stay awake all night?', 'O sultão fica acordado a noite toda?'], ['Until the story reaches its best part.', 'Até a história chegar à melhor parte.'],
   ['Then he must wait for another night.', 'Então ele precisa esperar mais uma noite.'], ['And that is exactly her plan.', 'E esse é exatamente o plano dela.']])

# ---------------------------------------------------------------- 327 / 328
F(930046, [['Can we meet on Friday afternoon?', 'Podemos nos encontrar sexta à tarde?'], ['Does three o’clock suit you?', 'Três horas funciona para você?'],
           ['I am afraid I cannot make it.', 'Receio não poder ir.'], ['Then let us check our availability again.', 'Então vamos conferir de novo nossa disponibilidade.']])

W(7930046, 'Notting Hill', '🎬 Filme · 1999', 'Um Lugar Chamado Notting Hill é uma comédia romântica de 1999, dirigida por Roger Michell: o dono de uma livraria em Londres conhece uma famosa atriz de cinema.', ['📚', '🎬', '🌹'], 'rainycafe')
C(7930046, ('Anna', 'William'), ['polly', 'tom'], 'shop', 'Ao telefone, Anna e William, dono de uma livraria, remarcam um encontro.',
  ('📖', 'bookshop', 'livraria', 'Hold on, I am at the bookshop.', 'Espere, estou na livraria.'),
  [('🎬', 'actress', 'atriz', 'Soa como “ÉK-tres”.'), ('🎞️', 'premiere', 'estreia', 'Soa como “pri-MÍR”.'), ('💐', 'bouquet', 'buquê', 'Soa como “bu-KÊI”.'),
   ('📕', 'travel guide', 'guia de viagem', 'Soa como “TRÉ-vol GÁID”.'), ('☎️', 'receiver', 'fone', 'Soa como “ri-SÍ-ver”.'), ('🌳', 'garden', 'jardim', 'Soa como “GAR-den”.')],
  [('apologise', '🙏', 'pedir desculpas', 'I apologise for the delay.', 'I apologise the delay.', 'I apologised.', 'Pedi desculpas.', 'apologise **for**.'),
   ('postpone', '⏭️', 'adiar', 'Postpone the meeting.', 'Postpone to the meeting.', 'I postponed it.', 'Adiei.', 'postpone **+ objeto**.'),
   ('confirm', '✅', 'confirmar', 'Confirm the time.', 'Confirm to the time.', 'I confirmed it.', 'Confirmei.', 'confirm **+ objeto**.'),
   ('leave', '📨', 'deixar', 'Leave a message.', 'Leave one message to.', 'I left one.', 'Deixei uma.', 'leave → **left**.')],
  [['William', 'Hello, Anna? Please hold on, I am in the shop.', 'Alô, Anna? Por favor, espere, estou na loja.'], ['Anna', 'I will hold on. I need to reschedule the interview.', 'Eu espero. Preciso remarcar a entrevista.'],
   ['William', 'Reschedule? I thought we could not cancel it.', 'Remarcar? Achei que não podíamos cancelar.'], ['Anna', 'I must cancel the lunch, too. Sorry.', 'Preciso cancelar o almoço também. Desculpe.'],
   ['William', 'Can I call you back in a minute?', 'Posso ligar de volta já?'], ['Anna', 'Please call me back after the shop closes.', 'Por favor, ligue de volta depois que a loja fechar.'],
   ['William', 'I will. Shall I reschedule for Friday?', 'Ligo. Devo remarcar para sexta?'], ['Anna', 'Yes, reschedule it. Do not cancel.', 'Sim, remarque. Não cancele.']],
  [('Where is William?', 'Onde William está?', [('📚', 'In the shop'), ('🏠', 'At home'), ('🚌', 'On a bus')], 0, 0, 'William diz: “I am in the shop.”'),
   ('What must Anna cancel?', 'O que Anna precisa cancelar?', [('🍽️', 'The lunch'), ('🎬', 'The film'), ('✈️', 'The flight')], 0, 3, 'Anna diz: “I must cancel the lunch.”'),
   ('When does William reschedule for?', 'Para quando William remarca?', [('📅', 'Friday'), ('🌙', 'Tonight'), ('📆', 'Next month')], 0, 6, 'William diz: “reschedule for Friday?”')],
  L('nh', 'Laboratório de sons: actress, premiere e bouquet', 'a soa é; ie soa í; et soa êi.', 'Em bouquet, o et soa êi.',
    [('actress', 'ÉK-tres', 'atriz', 'a = é', 'actors', 'ÉK-ters'), ('premiere', 'pri-MÍR', 'estreia', 'ie = í', 'primer', 'PRÁI-mer'), ('bouquet', 'bu-KÊI', 'buquê', 'et = êi', 'bucket', 'BÂ-kit')]),
  [['Is the actress free for lunch on Friday?', 'A atriz está livre para almoçar na sexta?'], ['Her agent says the afternoon works better.', 'O agente dela diz que a tarde é melhor.'],
   ['Then I move the books to the back room.', 'Então levo os livros para a sala dos fundos.'], ['And keep the bouquet fresh for her.', 'E mantenha o buquê fresco para ela.']])

# ---------------------------------------------------------------- 329 / 330
F(82213, [['I am writing to apply for the post.', 'Escrevo para me candidatar à vaga.'], ['I have solid experience in sales.', 'Tenho sólida experiência em vendas.'],
          ['I attach my CV to this email.', 'Anexo meu currículo a este e-mail.'], ['Yours faithfully, Ana Lima.', 'Atenciosamente, Ana Lima.']])

W(7082213, 'Legally Blonde', '🎬 Filme · 2001', 'Legalmente Loira (Legally Blonde) é uma comédia de 2001, dirigida por Robert Luketic: Elle entra numa faculdade de direito e prova seu valor como advogada.', ['⚖️', '📁', '🎓'], 'bakery')
C(7082213, ('Elle', 'Emmett'), ['polly', 'tom'], 'hall', 'Numa entrevista de estágio, Elle fala de suas qualidades e de quando pode começar.',
  ('📁', 'portfolio', 'portfólio', 'Look at my portfolio.', 'Veja meu portfólio.'),
  [('⚖️', 'law', 'direito', 'Soa como “LÓ”.'), ('🏛️', 'court', 'tribunal', 'Soa como “KÓRT”.'), ('📚', 'research', 'pesquisa', 'Soa como “ri-SÉRTCH”.'),
   ('🤝', 'kindness', 'gentileza', 'Soa como “KÁIND-nes”.'), ('🎯', 'focus', 'foco', 'Soa como “FÔU-kes”.'), ('🧑‍⚖️', 'lawyer', 'advogada', 'Soa como “LÓ-ier”.')],
  [('research', '📚', 'pesquisar', 'I research the case.', 'I research to the case.', 'I researched it.', 'Pesquisei.', 'research **+ objeto**.'),
   ('prepare', '🗂️', 'preparar', 'I prepare the files.', 'I prepare to the files.', 'I prepared them.', 'Preparei.', 'prepare **+ objeto**.'),
   ('graduate', '🎓', 'formar-se', 'I graduate in June.', 'I graduate at June.', 'I graduated.', 'Formei-me.', 'graduate **in**.'),
   ('start', '🚀', 'começar', 'I start on Monday.', 'I start in Monday.', 'I started.', 'Comecei.', 'start **on + dia**.')],
  [['Emmett', 'Tell me about yourself, Elle.', 'Fale de você, Elle.'], ['Elle', 'I am skilled in research and in talking to people.', 'Sou habilidosa em pesquisa e em conversar com as pessoas.'],
   ['Emmett', 'What are your strengths?', 'Quais são seus pontos fortes?'], ['Elle', 'My strengths are focus and kindness.', 'Meus pontos fortes são foco e gentileza.'],
   ['Emmett', 'Are you available to start soon?', 'Você está disponível para começar logo?'], ['Elle', 'Yes, I am available to start on Monday.', 'Sim, estou disponível para começar na segunda.'],
   ['Emmett', 'This is a big opportunity for a first job.', 'É uma grande oportunidade para um primeiro emprego.'], ['Elle', 'I know. Thank you for the opportunity.', 'Eu sei. Obrigada pela oportunidade.']],
  [('What is Elle skilled in?', 'Em que Elle é habilidosa?', [('📚', 'Research and talking to people'), ('🍳', 'Cooking'), ('🎸', 'Music')], 0, 1, 'Elle diz: “skilled in research and in talking to people.”'),
   ('What are her strengths?', 'Quais são seus pontos fortes?', [('🎯', 'Focus and kindness'), ('💪', 'Muscle'), ('🏃', 'Speed')], 0, 3, 'Elle diz: “My strengths are focus and kindness.”'),
   ('When can she start?', 'Quando ela pode começar?', [('📅', 'On Monday'), ('🌙', 'Tonight'), ('📆', 'In June')], 0, 5, 'Elle diz: “available to start on Monday.”')],
  L('lb', 'Laboratório de sons: lawyer, court e focus', 'aw soa ó; ou soa ó; o soa ôu.', 'Em focus, o o soa ôu.',
    [('lawyer', 'LÓ-ier', 'advogada', 'aw = ó', 'layer', 'LÊI-er'), ('court', 'KÓRT', 'tribunal', 'ou = ó', 'cat', 'KÉT'), ('focus', 'FÔU-kes', 'foco', 'o = ôu', 'fuss', 'FÂS')]),
  [['Did the firm like her portfolio?', 'O escritório gostou do portfólio dela?'], ['They asked for a second meeting.', 'Pediram uma segunda reunião.'],
   ['Then she should prepare her answers.', 'Então ela deve preparar as respostas.'], ['She already has, down to the last page.', 'Ela já preparou, até a última página.']])
