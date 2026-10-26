# Reescrita A2 382–406 (ver ova2b.py).
from v3.ova2b import X, W, L, Q

# 382 · Do you mind if I…? (só a obra)
X(7920039, ('Harry', 'Sally'), ['tom', 'polly'],
  W('When Harry Met Sally', '🎬 Filme', 1989, 'uma comédia romântica americana sobre dois amigos que discutem se homem e mulher podem ser só amigos.', 'quebrar o gelo com educação: Do you mind if I…?',
    'castle', ['☕', '🗽', '💬'], 'Do you mind if I sit here?', 'Você se importa se eu sentar aqui?'))

# 384 · used to (só a obra)
X(7081276, ('Mama Coco', 'Miguel'), ['matilda', 'tommy'],
  W('Coco', '🎬 Filme', 2017, 'um filme de animação da Pixar sobre um menino mexicano, sua família e o Dia dos Mortos.', 'lembranças de antigamente: used to',
    'castle', ['🎸', '💀', '🌼'], 'I used to play outside all day.', 'Eu costumava brincar lá fora o dia todo.'))

# 386 · with / without
X(7920040, ('Friday', 'Crusoe'), ['tom', 'tommy'],
  W('Robinson Crusoe', '📖 Romance', 1719, 'um romance do escritor inglês Daniel Defoe sobre um náufrago que vive sozinho numa ilha por muitos anos.', 'viver com ou sem algo: with e without',
    'ship', ['🏝️', '🦜', '🔥'], 'I cannot live without water.', 'Não consigo viver sem água.'),
  [('🏝️', 'island', 'ilha', 'Soa como “ÁI-lend”.'), ('🚢', 'shipwreck', 'naufrágio', 'Soa como “XÍP-rék”.'), ('🦜', 'parrot', 'papagaio', 'Soa como “PÉ-rot”.'),
   ('🐐', 'goat', 'cabra', 'Soa como “GÔUT”.'), ('🔥', 'fire', 'fogo', 'Soa como “FÁI-er”.'), ('🛖', 'hut', 'cabana', 'Soa como “RÂT”.')],
  [('🦜', 'parrot', 'papagaio', 'I live with a parrot and a goat.', 'Eu moro com um papagaio e uma cabra.'),
   ('🔥', 'fire', 'fogo', 'I never make a fire without care.', 'Eu nunca faço fogo sem cuidado.'),
   ('🛖', 'hut', 'cabana', 'The hut is warm with a fire.', 'A cabana é quente com fogo.'),
   ('🏝️', 'island', 'ilha', 'He left the island without a word.', 'Ele deixou a ilha sem dizer uma palavra.'),
   ('🐐', 'goat', 'cabra', 'A goat cannot live without grass.', 'Uma cabra não vive sem capim.')],
  [['Friday', 'Can you live without water, Crusoe?', 'Você consegue viver sem água, Crusoe?'],
   ['Crusoe', 'No. I cannot live without water.', 'Não. Não consigo viver sem água.'],
   ['Friday', 'Can you live with a parrot?', 'Você consegue viver com um papagaio?'],
   ['Crusoe', 'Yes. I live with a parrot and a goat.', 'Sim. Eu moro com um papagaio e uma cabra.'],
   ['Friday', 'Do not make a fire without care.', 'Não faça fogo sem cuidado.'],
   ['Crusoe', 'I never make a fire without care.', 'Eu nunca faço fogo sem cuidado.'],
   ['Friday', 'The old captain left the island without a word.', 'O velho capitão deixou a ilha sem dizer uma palavra.'],
   ['Crusoe', 'That is sad.', 'Isso é triste.']],
  [Q('What can Crusoe not live without?', 'Sem o que o Crusoe não vive?', 1, ('💧', 'Water'), ('📱', 'A phone'), ('🎮', 'Games')),
   Q('Who does Crusoe live with?', 'Com quem o Crusoe mora?', 3, ('🦜', 'A parrot and a goat'), ('🐶', 'A dog'), ('👨', 'A friend')),
   Q('What does he never make without care?', 'O que ele nunca faz sem cuidado?', 5, ('🔥', 'A fire'), ('🍞', 'Bread'), ('🛖', 'A boat'))],
  verbs=None, lab=None)

# 388 · all of / most of / none of (obra e verbos)
X(7081284, ('Denham', 'Mr Thackeray'), ['tommy', 'tom'],
  W('To Sir, with Love', '🎬 Filme', 1967, 'um filme britânico sobre um professor que conquista uma turma difícil numa escola de Londres.', 'quantidades de pessoas: all of, most of, some of e none of',
    'school', ['🏫', '🎓', '🍎'], 'All of the students came.', 'Todos os alunos vieram.'),
  verbs=[('attend', '🏫', 'frequentar', 'All of them attend class.', 'All of them attends class.', 'He attended school.', 'Ele frequentou a escola.', 'they **attend**.'),
         ('graduate', '🎓', 'formar-se', 'Most of them graduate.', 'Most of them graduates.', 'She graduated in June.', 'Ela se formou em junho.', 'they **graduate**.'),
         ('answer', '🙋', 'responder', 'Some of them answer well.', 'Some of them answers well.', 'None of them answered.', 'Nenhum respondeu.', 'they **answer**.'),
         ('celebrate', '🎉', 'comemorar', 'We celebrate together.', 'We celebrates together.', 'They celebrated today.', 'Eles comemoraram hoje.', 'we **celebrate**.')])

# 390 · height / length / width (obra e verbos)
X(7081285, ('Amy', 'Wayne'), ['polly', 'tom'],
  W('Honey, I Shrunk the Kids', '🎬 Filme', 1989, 'uma comédia de aventura americana em que crianças são encolhidas por uma máquina e enfrentam o quintal como se fosse uma selva.', 'medidas: the height, the length, the width of…',
    'castle', ['📏', '🌱', '🐜'], 'The height is two meters.', 'A altura é de dois metros.'),
  verbs=[('shrink', '🤏', 'encolher', 'The machine shrinks the kids.', 'The machine shrink the kids.', 'It shrank the box.', 'Encolheu a caixa.', 'it **shrinks**.'),
         ('grow', '🌱', 'crescer', 'The grass grows tall.', 'The grass grow tall.', 'The ant grew big.', 'A formiga cresceu.', 'it **grows**.'),
         ('estimate', '🧮', 'estimar', 'Wayne estimates the width.', 'Wayne estimate the width.', 'I estimated it.', 'Eu estimei.', 'he **estimates**.'),
         ('compare', '⚖️', 'comparar', 'Amy compares the sizes.', 'Amy compare the sizes.', 'We compared them.', 'Nós os comparamos.', 'she **compares**.')])

# 392 · When did you…? (obra e verbos)
X(7081286, ('Rose', 'Jack'), ['polly', 'tom'],
  W('Titanic', '🎬 Filme', 1997, 'um filme épico sobre o amor de dois jovens a bordo do navio Titanic, em sua viagem inaugural.', 'perguntar quando algo aconteceu: When did you…?',
    'ship', ['🚢', '🧊', '🎻'], 'When did you arrive?', 'Quando você chegou?'),
  verbs=[('board', '🚢', 'embarcar', 'Jack boarded the ship.', 'Jack boarded to the ship.', 'We board at noon.', 'Embarcamos ao meio-dia.', 'did you **board**?'),
         ('sail', '⛵', 'navegar', 'The ship sailed on Monday.', 'The ship sail on Monday.', 'When did it sail?', 'Quando ela zarpou?', 'did it **sail**?'),
         ('draw', '🖍️', 'desenhar', 'He drew a portrait.', 'He drawed a portrait.', 'When did he draw it?', 'Quando ele a desenhou?', 'did he **draw**?'),
         ('dance', '💃', 'dançar', 'They danced last night.', 'They dance last night.', 'When did you dance?', 'Quando vocês dançaram?', 'did you **dance**?')])

# 394 · e-mails
X(7920041, ('Ben', 'Jules'), ['tom', 'polly'],
  W('The Intern', '🎬 Filme', 2015, 'uma comédia americana sobre um senhor aposentado que vira estagiário numa empresa de moda online.', 'escrever e-mails formais: I am writing to…, Please find attached…',
    'castle', ['💻', '📧', '👔'], 'I am writing to ask about the internship.', 'Estou escrevendo para perguntar sobre o estágio.'),
  [('📥', 'inbox', 'caixa de entrada', 'Soa como “ÍN-bóks”.'), ('📄', 'resume', 'currículo', 'Soa como “RÉ-zu-mêi”.'), ('🧑‍💼', 'interview', 'entrevista', 'Soa como “ÍN-ter-viu”.'),
   ('🎓', 'internship', 'estágio', 'Soa como “ÍN-tern-xip”.'), ('↩️', 'reply', 'resposta', 'Soa como “ri-PLÁI”.'), ('✍️', 'signature', 'assinatura', 'Soa como “SÍG-na-tcher”.')],
  [('📄', 'resume', 'currículo', 'Please find attached my resume.', 'Segue anexo o meu currículo.'),
   ('🧑‍💼', 'interview', 'entrevista', 'I look forward to the interview.', 'Aguardo a entrevista.'),
   ('📥', 'inbox', 'caixa de entrada', 'I am writing to check my inbox.', 'Escrevo para verificar a minha caixa de entrada.'),
   ('↩️', 'reply', 'resposta', 'I look forward to your reply.', 'Aguardo a sua resposta.'),
   ('✍️', 'signature', 'assinatura', 'Please add your signature.', 'Por favor, adicione a sua assinatura.')],
  [['Jules', 'What is the subject, Ben?', 'Qual é o assunto, Ben?'],
   ['Ben', 'The internship at your company.', 'O estágio na sua empresa.'],
   ['Jules', 'How do we start?', 'Como começamos?'],
   ['Ben', 'I am writing to ask about the internship.', 'Estou escrevendo para perguntar sobre o estágio.'],
   ['Jules', 'And the resume?', 'E o currículo?'],
   ['Ben', 'Please find attached my resume.', 'Segue anexo o meu currículo.'],
   ['Jules', 'And the ending?', 'E o final?'],
   ['Ben', 'I look forward to hearing from you.', 'Aguardo o seu retorno.']],
  [Q('What is the subject?', 'Qual é o assunto?', 1, ('🎓', 'The internship'), ('🏖️', 'A holiday'), ('🛒', 'A sale')),
   Q('What is attached?', 'O que está anexo?', 5, ('📄', 'A resume'), ('📷', 'A photo'), ('🎵', 'A song')),
   Q('How does the e-mail end?', 'Como o e-mail termina?', 7, ('📬', 'I look forward to hearing from you'), ('👋', 'Bye'), ('😂', 'Ha ha'))],
  verbs=None, lab=None)

# 396 · with / without ingrediente
X(7081288, ('SpongeBob', 'Patrick'), ['tommy', 'tom'],
  W('SpongeBob SquarePants', '📺 Série', 1999, 'uma série animada americana sobre uma esponja do mar que trabalha numa lanchonete no fundo do oceano.', 'fazer pedidos de comida: with, without, extra e no',
    'ship', ['🍔', '🧽', '🍟'], 'A Krabby Patty with pickles, please.', 'Um Krabby Patty com picles, por favor.'),
  [('🍔', 'burger', 'hambúrguer', 'Soa como “BÉR-ger”.'), ('🥒', 'pickles', 'picles', 'Soa como “PÍ-kolz”.'), ('🍞', 'bun', 'pão', 'Soa como “BÂN”.'),
   ('🍟', 'fries', 'batata frita', 'Soa como “FRÁIZ”.'), ('🥤', 'shake', 'milk-shake', 'Soa como “XÊIK”.'), ('🧅', 'ketchup', 'ketchup', 'Soa como “KÉ-tchap”.')],
  [('🥒', 'with pickles', 'com picles', 'A burger with pickles, please.', 'Um hambúrguer com picles, por favor.'),
   ('🧀', 'without cheese', 'sem queijo', 'Without cheese, please.', 'Sem queijo, por favor.'),
   ('🍟', 'extra fries', 'batata extra', 'Extra fries, please.', 'Batata extra, por favor.'),
   ('🥤', 'no ice', 'sem gelo', 'A shake with no ice.', 'Um milk-shake sem gelo.'),
   ('🧅', 'ketchup', 'ketchup', 'Ketchup on the side.', 'Ketchup à parte.')],
  [['SpongeBob', 'What would you like, Patrick?', 'O que você gostaria, Patrick?'],
   ['Patrick', 'A Krabby Patty with pickles, please.', 'Um Krabby Patty com picles, por favor.'],
   ['SpongeBob', 'With cheese?', 'Com queijo?'],
   ['Patrick', 'Without cheese, please.', 'Sem queijo, por favor.'],
   ['SpongeBob', 'Any fries?', 'Alguma batata frita?'],
   ['Patrick', 'Extra fries, please. And a shake.', 'Batata extra, por favor. E um milk-shake.'],
   ['SpongeBob', 'Ice in the shake?', 'Gelo no milk-shake?'],
   ['Patrick', 'No ice, actually. Ketchup on the side.', 'Sem gelo, na verdade. Ketchup à parte.']],
  [Q('What does Patrick want on the burger?', 'O que o Patrick quer no hambúrguer?', 1, ('🥒', 'Pickles'), ('🍅', 'Tomato'), ('🥬', 'Lettuce')),
   Q('What does he want without?', 'O que ele quer sem?', 3, ('🧀', 'Cheese'), ('🍟', 'Fries'), ('🥤', 'A shake')),
   Q('What does he want extra?', 'O que ele quer extra?', 5, ('🍟', 'Fries'), ('🧅', 'Onions'), ('🍔', 'Burgers'))],
  verbs=None, lab=None)

# 398 · more / less / fewer (obra e verbos)
X(7081290, ('Olive Oyl', 'Popeye'), ['polly', 'tom'],
  W('Popeye the Sailor', '📺 Desenho animado', 1933, 'um personagem de quadrinhos e desenhos animados americano, um marinheiro que fica forte ao comer espinafre.', 'comer melhor: more, less e fewer',
    'ship', ['⚓', '🥬', '💪'], 'Eat more vegetables.', 'Coma mais legumes.'),
  verbs=[('chew', '🦷', 'mastigar', 'Popeye chews the pipe.', 'Popeye chew the pipe.', 'He chewed slowly.', 'Ele mastigou devagar.', 'he **chews**.'),
         ('snack', '🍿', 'petiscar', 'She snacks on fruit.', 'She snack on fruit.', 'We snacked at noon.', 'Petiscamos ao meio-dia.', 'she **snacks**.'),
         ('taste', '😋', 'provar', 'Olive tastes the soup.', 'Olive taste the soup.', 'He tasted spinach.', 'Ele provou espinafre.', 'she **tastes**.'),
         ('avoid', '🚫', 'evitar', 'Popeye avoids sugar.', 'Popeye avoid sugar.', 'I avoided sweets.', 'Evitei doces.', 'he **avoids**.')])

# 400 · where from (só a obra)
X(7081291, ('Carmen Sandiego', 'Zack'), ['polly', 'tommy'],
  W('Where in the World Is Carmen Sandiego?', '🎮 Jogo', 1985, 'um jogo educativo de computador em que o jogador segue pistas geográficas para encontrar uma ladra misteriosa.', 'origem das coisas e das pessoas: Where is it from?',
    'castle', ['🌍', '🧭', '🕵️'], 'Where are you from?', 'De onde você é?'))

# 402 · If you ask me / I would say
X(7920042, ('Atticus', 'Judge Taylor'), ['tom', 'tommy'],
  W('To Kill a Mockingbird', '📖 Romance', 1960, 'um romance da escritora americana Harper Lee sobre um advogado que defende um homem acusado injustamente.', 'dar opiniões: If you ask me… e I would say…',
    'castle', ['⚖️', '🐦', '📖'], 'If you ask me, he is not guilty.', 'Se você quer saber, ele não é culpado.'),
  verbs=[('defend', '🛡️', 'defender', 'Atticus defends the man.', 'Atticus defend the man.', 'He defended him well.', 'Ele o defendeu bem.', 'he **defends**.'),
         ('judge', '⚖️', 'julgar', 'The judge listens first.', 'The judge listen first.', 'He judged fairly.', 'Ele julgou com justiça.', 'he **judges**.'),
         ('decide', '🤔', 'decidir', 'The jury decides today.', 'The jury decide today.', 'They decided quickly.', 'Eles decidiram rápido.', 'it **decides**.'),
         ('doubt', '❓', 'duvidar', 'I doubt the proof.', 'I doubts the proof.', 'She doubted him.', 'Ela duvidou dele.', 'I **doubt**.')])

# 404 · How far is it? (só a obra)
X(7081295, ('Bilbo', 'Gandalf'), ['frodo', 'gandalf'],
  W('The Hobbit', '📖 Romance', 1937, 'um romance de fantasia de J. R. R. Tolkien sobre um hobbit que sai de casa numa grande aventura.', 'distâncias e tempo de caminho: How far is it?',
    'castle', ['🧙', '⛰️', '🐉'], 'How far is the mountain?', 'A que distância fica a montanha?'))

# 406 · the same as / different from (só a obra)
X(7081296, ('Edward', 'Tom Canty'), ['tommy', 'tom'],
  W('The Prince and the Pauper', '📖 Romance', 1881, 'um romance do escritor americano Mark Twain sobre dois meninos muito parecidos que trocam de lugar em Londres.', 'comparar lugares e vidas: the same as, different from, similar to',
    'castle', ['👑', '🧒', '🏰'], 'My life is different from yours.', 'A minha vida é diferente da sua.'))
