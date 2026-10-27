# Itens 1–45 do B1: obra, elenco e capa próprios das continuações (dados lidos por v3/b1fix.py).
FIX = {}
AUTORAL = ' A cena é autoral; não adapta nem cita a obra.'


def O(n, name, kind, text, cap_en, cap_pt, t, emo, cast, cover, **more):
    d = dict(obra=(name, kind, text + AUTORAL, cap_en, cap_pt, t, emo), cast=cast, cover=cover)
    d.update(more)
    FIX[n] = d


O(7082001, 'The Birds', '🎬 Filme · 1963', 'The Birds é um filme de suspense de 1963 dirigido por Alfred Hitchcock, em que sons e movimentos estranhos interrompem o dia a dia. Combina com contar o que você fazia quando algo te interrompeu.',
  'The Birds: A noise on the road.', 'Os Pássaros: Um barulho na estrada.', 'lighthouse', ['🐦', '🌊', '😨'], ('Melanie', 'Mitch', 'polly', 'tom'),
  'No parque, Melanie conta a Mitch o que ouviu na volta para casa, como numa cena de suspense de The Birds.')
O(7082004, 'The Railway Children', '📚 Romance · 1906', 'The Railway Children é um romance da escritora inglesa Edith Nesbit, de 1906, sobre irmãos que passam a viver perto de uma estação de trem. Combina com contar uma virada inesperada numa estação.',
  'The Railway Children: Someone steps off the train.', 'As Crianças da Ferrovia: Alguém desce do trem.', 'viaduct', ['🚂', '🚉', '🎩'], ('Bobbie', 'Peter', 'polly', 'tommy'),
  'Na estação, Bobbie e Peter contam o que mudou de repente, como em The Railway Children.')
O(7082005, 'Little Women', '📚 Romance · 1868', 'Little Women é um romance da escritora americana Louisa May Alcott, publicado em 1868, sobre irmãs e vizinhos que cresceram juntos. Combina com lembrar o que você costumava fazer antes.',
  'Little Women: Winter afternoons at home.', 'Mulherzinhas: Tardes de inverno em casa.', 'library', ['📖', '🧣', '🎭'], ('Laurie', 'Meg', 'tommy', 'misshoney'),
  'Na sala, Laurie e Meg lembram os velhos hábitos de infância, como em Little Women.')
O(7930001, 'Bridge to Terabithia', '📚 Romance · 1977', 'Bridge to Terabithia é um romance da escritora americana Katherine Paterson, de 1977, sobre uma amizade que ajuda a atravessar uma perda. Combina com falar de superar um momento difícil com o apoio de um amigo.',
  'Bridge to Terabithia: A friend by the creek.', 'Ponte para Terabítia: Uma amiga perto do riacho.', 'jungle', ['🌉', '🌳', '🤝'], ('Leslie', 'Jess', 'polly', 'tommy'),
  'Perto do riacho, Leslie e Jess falam de como atravessar uma fase difícil, como em Bridge to Terabithia.',
  verbs=[('recover', '💪', 'se recuperar', 'She recovered from the loss.', 'She recovered of the loss.', 'I will recover.', 'Vou me recuperar.', 'recover **from**.'),
         ('survive', '🌱', 'sobreviver', 'We survived a hard winter.', 'We survive a hard winter last year.', 'I survive.', 'Eu sobrevivo.', 'passado: **survived**.'),
         ('miss', '💭', 'sentir falta de', 'I miss my old friend.', 'I miss of my old friend.', 'She missed him.', 'Ela sentiu falta dele.', 'miss **+ objeto**.'),
         ('hug', '🤗', 'abraçar', 'He hugged me tight.', 'He hugged to me tight.', 'I hug her.', 'Eu a abraço.', 'hug **+ objeto**.')])
O(7082008, 'Knives Out', '🎬 Filme · 2019', 'Knives Out é um filme de mistério de 2019 dirigido por Rian Johnson, em que um detetive interroga a família e confere o que cada um fazia na noite do crime. Combina com perguntar o que alguém estava fazendo.',
  'Knives Out: Questions in the old mansion.', 'Entre Facas e Segredos: Perguntas na velha mansão.', 'castle', ['🔍', '🕵️', '🏚️'], ('Marta', 'Blanc', 'misshoney', 'tom'),
  'Na sala da mansão, Marta e o detetive Blanc perguntam o que cada pessoa estava fazendo, como em Knives Out.')
O(7082009, 'The Haunting of Hill House', '📚 Romance · 1959', 'The Haunting of Hill House é um romance de terror da escritora americana Shirley Jackson, de 1959, sobre uma casa que parece observar quem entra. Combina com criar suspense e contar passo a passo.',
  'The Haunting of Hill House: Footsteps in the hall.', 'A Assombração da Casa da Colina: Passos no corredor.', 'castle', ['🏚️', '🕯️', '👣'], ('Dr. Montague', 'Eleanor', 'tom', 'polly'),
  'No corredor, o doutor Montague e Eleanor contam a história passo a passo, como em The Haunting of Hill House.')
O(7930002, 'Educating Rita', '🎬 Filme · 1983', 'Educating Rita é um filme britânico de 1983, baseado na peça de Willy Russell, sobre uma cabeleireira que decide estudar literatura. Combina com falar de escolhas, decisões e erros.',
  'Educating Rita: A choice about the course.', 'Educando Rita: Uma escolha sobre o curso.', 'library', ['📚', '✂️', '🎓'], ('Frank', 'Rita', 'tom', 'misshoney'),
  'No escritório da universidade, Frank e Rita falam de uma decisão sobre o curso, como em Educating Rita.')
O(7082012, 'Finding Nemo', '🎬 Animação · 2003', 'Finding Nemo é uma animação de 2003 do estúdio Pixar, dirigida por Andrew Stanton, sobre um peixe-palhaço que atravessa o oceano para encontrar o filho. Combina com contar uma história de se perder, entrar em pânico e se achar.',
  'Finding Nemo: Lost in the open sea.', 'Procurando Nemo: Perdido em mar aberto.', 'ship', ['🐠', '🌊', '🧭'], ('Marlin', 'Dory', 'tom', 'misshoney'),
  'No fundo do mar, Marlin e Dory contam em sequência como se perderam e se encontraram, como em Finding Nemo.')
O(7082013, 'Dear Mr. Henshaw', '📚 Livro · 1983', 'Dear Mr. Henshaw é um livro da escritora americana Beverly Cleary, de 1983, contado em cartas de um menino a um autor. Combina com falar do que já tinha acontecido antes de ler ou abrir uma carta.',
  'Dear Mr. Henshaw: A letter on the kitchen table.', 'Querido Sr. Henshaw: Uma carta na mesa da cozinha.', 'library', ['✉️', '📖', '✍️'], ('Leigh', 'Mr. Henshaw', 'tommy', 'tom'),
  'Na sala, Leigh e o Sr. Henshaw falam da carta e do que já tinha acontecido antes, como em Dear Mr. Henshaw.')
O(7082014, 'Mary Poppins', '📚 Livro · 1934', 'Mary Poppins é um livro infantil da escritora P. L. Travers, de 1934, sobre uma babá que muda a rotina de uma família. Combina com comparar como era antes e como é agora.',
  'Mary Poppins: Then and now.', 'Mary Poppins: Antes e agora.', 'toyshop', ['☂️', '🎩', '🏠'], ('Mary Poppins', 'Michael', 'misshoney', 'tommy'),
  'Na sala, Mary Poppins e Michael comparam o passado com o presente, como no livro Mary Poppins.')
O(7930003, 'Office Space', '🎬 Filme · 1999', 'Office Space é uma comédia de 1999 dirigida por Mike Judge, sobre funcionários cansados da rotina de escritório. Combina com encerrar o expediente e combinar o fim de semana.',
  'Office Space: Friday at five.', 'Office Space: Sexta às cinco.', 'library', ['🖨️', '💼', '🍻'], ('Peter', 'Joanna', 'tom', 'polly'),
  'No escritório, Peter e Joanna encerram o dia e combinam o fim de semana, como numa cena de Office Space.')
O(7082016, 'Sleeping Beauty', '🏰 Conto de fadas · 1697', 'A Bela Adormecida (Sleeping Beauty) é um conto de fadas publicado pelo francês Charles Perrault em 1697, sobre uma princesa que adormece sob um feitiço. Combina com contar o que aconteceu depois, em sequência.',
  'Sleeping Beauty: The spell breaks.', 'A Bela Adormecida: O feitiço se quebra.', 'castle', ['🏰', '🧵', '🤴'], ('Prince', 'King', 'tommy', 'tom'),
  'No castelo, o príncipe e o rei resumem o conto passo a passo, como em A Bela Adormecida.',
  rep=[('she ate the apple', 'she pricked her finger'), ('she eat the apple', 'she prick her finger'), ('she eating the apple', 'she pricking her finger'), (' ate the apple', ' pricked her finger'),
       ('comeu a maçã', 'espetou o dedo'), ('After the apple', 'After the prick'), ('depois da maçã', 'depois da picada'), ('after the apple', 'after the prick'), ('🍎', '🧵'), ('She eats apples.', 'She pricks her finger.'), ('Ela come maçãs.', 'Ela espeta o dedo.')],
  verbs=[('prick', '🧵', 'espetar', 'After she pricked her finger…', 'After she prick her finger…', 'She pricks her finger.', 'Ela espeta o dedo.', 'passado: **pricked**.'),
         ('arrive', '🤴', 'chegar', 'As soon as he arrived…', 'As soon as he arrive…', 'He arrives at noon.', 'Ele chega ao meio-dia.', 'passado: **arrived**.'),
         ('wake', '⏰', 'acordar', 'Once she woke, she smiled.', 'Once she waked, she smiled.', 'I wake early.', 'Acordo cedo.', 'passado: **woke**.'),
         ('dance', '💃', 'dançar', 'Before it ended, they danced.', 'Before it ended, they dance.', 'We dance a lot.', 'Dançamos muito.', 'passado: **danced**.')])
O(7082017, 'The Adventures of Sherlock Holmes', '📚 Livro · 1892', 'The Adventures of Sherlock Holmes é uma coletânea de contos policiais de Arthur Conan Doyle, publicada em 1892, em que o detetive desvenda casos com pistas pequenas. Combina com narrar como o mistério se revelou.',
  'The Adventures of Sherlock Holmes: Footprints in the hall.', 'As Aventuras de Sherlock Holmes: Pegadas no corredor.', 'rainycafe', ['🔍', '🧥', '👣'], ('Sherlock', 'Mrs. Hudson', 'sherlock', 'misshoney'),
  'Na sala de Baker Street, Sherlock e a Sra. Hudson contam como o mistério se resolveu, como em As Aventuras de Sherlock Holmes.')
O(7082019, 'The Wonderful Wizard of Oz', '📚 Livro · 1900', 'The Wonderful Wizard of Oz é um livro infantil do escritor americano L. Frank Baum, de 1900, sobre uma menina levada por um ciclone a uma terra mágica. Combina com contar um sonho de forma vaga.',
  'The Wonderful Wizard of Oz: The yellow road.', 'O Mágico de Oz: A estrada amarela.', 'castle', ['🌪️', '👠', '🏰'], ('Tin Man', 'Glinda', 'tinman', 'glinda'),
  'Na estrada amarela, o Homem de Lata e Glinda contam um sonho esquisito, como em O Mágico de Oz.')
O(7930004, 'Pride and Prejudice', '📚 Romance · 1813', 'Pride and Prejudice é um romance da escritora inglesa Jane Austen, publicado em 1813, cheio de conversas sobre gostos e preferências. Combina com dizer o que você prefere.',
  'Pride and Prejudice: Tea in the drawing room.', 'Orgulho e Preconceito: Chá na sala de visitas.', 'library', ['🫖', '📖', '💌'], ('Elizabeth', 'Darcy', 'polly', 'tom'),
  'Na sala de visitas, Elizabeth e Darcy falam do que preferem, como em Pride and Prejudice.')
O(7082020, 'Bend It Like Beckham', '🎬 Filme · 2002', 'Bend It Like Beckham é uma comédia de 2002 dirigida por Gurinder Chadha, sobre uma jovem apaixonada por futebol na Inglaterra. Combina com narrar uma partida emocionante.',
  'Bend It Like Beckham: The final minutes.', 'Driblando o Destino: Os minutos finais.', 'bakery', ['⚽', '🥅', '🏆'], ('Joe', 'Jess', 'tom', 'polly'),
  'No campo, o treinador Joe e Jess contam os últimos minutos da partida, como em Bend It Like Beckham.')
O(7082021, "Charlie and the Chocolate Factory", '📚 Livro · 1964', 'Charlie and the Chocolate Factory é um livro infantil do escritor britânico Roald Dahl, de 1964, sobre um menino e uma fábrica de doces cheia de invenções. Combina com dizer quem escreveu, fundou ou inventou algo.',
  'Charlie and the Chocolate Factory: Before the golden ticket.', 'A Fantástica Fábrica de Chocolate: Antes do bilhete dourado.', 'bakery', ['🍫', '🎫', '🏭'], ('Mr. Bucket', 'Veruca', 'tom', 'polly'),
  'Na escola, o Sr. Bucket e Veruca conversam sobre quem escreveu o livro e quem fundou a fábrica, como em A Fantástica Fábrica de Chocolate.',
  rep=[('Who wrote this diary?', 'Who wrote this book?'), ('Quem escreveu este diário?', 'Quem escreveu este livro?'),
       ('It was written by a young girl.', 'It was written by Roald Dahl.'), ('Foi escrito por uma menina.', 'Foi escrito por Roald Dahl.'),
       ('The diary was written by a girl.', 'The book was written by Roald Dahl.'), ('O diário foi escrito por uma menina.', 'O livro foi escrito por Roald Dahl.'),
       ('The diary was written ___ a girl.', 'The book was written ___ Roald Dahl.'), ('The diary', 'The book'), ('O diário', 'O livro'),
       ('Yes. The museum was founded by her father.', 'Yes. The factory was founded by Mr. Wonka.'), ('Sim. O museu foi fundado pelo pai dela.', 'Sim. A fábrica foi fundada pelo Sr. Wonka.'),
       ('The museum was founded by her father.', 'The factory was founded by Mr. Wonka.'), ('O museu foi fundado pelo pai dela.', 'A fábrica foi fundada pelo Sr. Wonka.'),
       ('The museum was ___ by her father.', 'The factory was ___ by Mr. Wonka.'), ('Foi fundado pelo pai dela.', 'Foi fundado pelo Sr. Wonka.'), ('It was founded by her father.', 'It was founded by Mr. Wonka.'),
       ('Yes, into seventy languages.', 'Yes, into many languages.'), ('Sim, para setenta idiomas.', 'Sim, para muitos idiomas.'),
       ('Who wrote the diary?', 'Who wrote the book?'), ('Quem escreveu o diário?', 'Quem escreveu o livro?'), ('A young girl', 'Roald Dahl'), ('Her father', 'Mr. Wonka'),
       ('Who founded the museum?', 'Who founded the factory?'), ('Quem fundou o museu?', 'Quem fundou a fábrica?'), ('written by a young girl', 'written by Roald Dahl'), ('founded by her father', 'founded by Mr. Wonka'),
       ('The museum was founded by', 'The factory was founded by'), ('o museu foi fundado por', 'a fábrica foi fundada por'), ('o diário foi escrito por', 'o livro foi escrito por'),
       (' a young girl.', ' Roald Dahl.'), (' uma menina.', ' Roald Dahl.'), (' her father.', ' Mr. Wonka.'), (' o pai dela.', ' o Sr. Wonka.'), ('by Anne.', 'by Dahl.'),
       ('It was **penned by** a girl.', 'It was **penned by** Roald Dahl.'), ('The museum was **built from scratch**.', 'The factory was **built from scratch**.'), ('O museu foi feito do zero.', 'A fábrica foi feita do zero.'),
       ('It was penned by a girl.', 'It was penned by Roald Dahl.'), ('She wrote daily.', 'He wrote daily.'), ('Ela escrevia todo dia.', 'Ele escrevia todo dia.'),
       ('Penned by a famous author.', 'Penned by a famous author.')])
O(7082022, 'Around the World in Eighty Days', '📚 Romance · 1872', 'Around the World in Eighty Days é um romance do escritor francês Jules Verne, de 1872, sobre uma aposta de dar a volta ao mundo. Combina com contar as etapas de uma viagem.',
  'Around the World in Eighty Days: The next stop.', 'A Volta ao Mundo em 80 Dias: A próxima parada.', 'ship', ['🎈', '🚂', '🌍'], ('Fogg', 'Aouda', 'tom', 'polly'),
  'No trem, Fogg e Aouda contam as etapas da viagem, como em A Volta ao Mundo em 80 Dias.',
  rep=[('your trip to Peru', 'your trip around the world'), ('viagem ao Peru', 'viagem ao redor do mundo'), ('Lima', 'Suez'), ('🇵🇪', '🇪🇬')])
O(7930005, 'Home Alone', '🎬 Filme · 1990', 'Home Alone é uma comédia de 1990 dirigida por Chris Columbus, sobre um menino que fica sozinho em casa no Natal e depois se reconcilia com a família. Combina com fazer as pazes e perdoar.',
  'Home Alone: Making up with the family.', 'Esqueceram de Mim: Fazendo as pazes com a família.', 'toyshop', ['🏠', '🎄', '👨‍👩‍👦'], ('Kevin', 'Kate', 'tommy', 'misshoney'),
  'Na sala de casa, Kevin e Kate conversam sobre fazer as pazes com o irmão, como em Home Alone.')
