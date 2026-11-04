"""Suplemento Quest v5 · aula 156: Book club night + regular Paperback or hardcover? (Wishbone)."""
SUPP = {
 'reg': 180,
 'badge': {'icon': '📚', 'name': 'Book Club Star', 'desc': 'Talk about a book: ending, character and story'},
 'culture': {
  'hook': 'In the USA, many people join a book club to read the same book and talk about it. Meetings are often in a living room, with tea, snacks and friendly opinions.',
  'mythfact': [
   {'s': 'In the USA, a book club often meets in someone’s home.', 'ans': True, 'why': 'Many clubs meet in a living room, but others meet in libraries, cafés or bookshops.'},
   {'s': 'Members usually read the same book before the meeting.', 'ans': True, 'why': 'That is the main idea: everyone has something to say about the same story.'},
   {'s': 'You must love every book in the club.', 'ans': False, 'why': 'Honest opinions are welcome. You can say, “It was not my favorite.”'},
   {'s': 'Book clubs only read very old classic books.', 'ans': False, 'why': 'Clubs read all kinds of books: mysteries, novels, true stories and more.'},
   {'s': '“Wishbone” is an American TV series about a dog who loves books.', 'ans': True, 'why': 'It started in 1995. The dog imagines he is a character in famous stories.'}],
  'wild': [
   {'kind': 'Club message', 'lines': ['**Book Club Night!**', 'Thursday, 7 p.m. at Ava’s house', 'Please read chapters 1–12', 'Tea and cookies for everyone'], 'decode': {'q': 'What should you read before Thursday?', 'opts': ['Chapters 1–12', 'The whole library', 'Only the cover'], 'ans': 0, 'why': '“Please read chapters 1–12.”'}},
   {'kind': 'Sign at a bookshop', 'lines': ['**Spoiler alert!**', 'Do not tell the ending.', 'Ask a worker for a mystery book'], 'decode': {'q': 'What does “Do not tell the ending” ask you to do?', 'opts': ['Keep the end of the story a secret', 'Read faster', 'Buy two books'], 'ans': 0, 'why': 'A spoiler tells the end and ruins the surprise.'}}],
  'compare': {'br': 'In Brazil, people often talk about books with friends or in school, and book clubs are growing in bookshops and online.', 'us': 'In the USA, book clubs are common in homes, libraries and bookshops. People often bring a snack and say what they think, kindly.', 'tip': 'Say: “I agree, and I also liked…”', 'ask': 'What is your favorite book? Say its title and one thing you like.'},
  'quiz': [
   {'q': 'You want to know if your friend read the whole book. You ask…', 'opts': ['Did you finish the book?', 'You finish the book?', 'Did you finished the book?'], 'ans': 0, 'why': 'After did, the verb stays in the base form: finish.'},
   {'q': 'What is the ending of a story?', 'opts': ['the last part', 'the first page', 'the title'], 'ans': 0, 'why': 'The ending is how the story finishes.'},
   {'q': 'Your friend says, “Spoiler alert!” What happens next?', 'opts': ['She may tell part of the story', 'She gives you a gift', 'She says goodbye'], 'ans': 0, 'why': 'It is a warning before she talks about the plot.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'First night at the club',
  'text': [
   'Lena goes to a book club in Brooklyn. It is her first night. Her friend Ava has tea and cookies in the living room. Six people sit on the sofa and on chairs.',
   '“**Welcome to book club!**” Ava says. “**Thanks for having me**,” Lena says. The book is a short novel about a family. Lena likes the cover. “**What a nice cover!**” she says.',
   '“**Did you finish the book?**” Ava asks. “**Yes, I loved the ending**,” Lena says. “**Who’s your favorite character?**” “**The grandmother. She’s so funny.**” Everyone laughs. They talk about the plot: a family and a secret.',
   'Ava has a small dog. His name is Wishbone, like the dog in the American TV series “Wishbone.” In that show, a dog imagines he is inside famous books. Lena smiles. “Now I want to **read the first chapter** again,” she says.',
   'At the end, Ava asks, “**Would you recommend it?**” Lena says yes. She writes the title on a card for her sister. The next book is a mystery. Lena goes home happy.'],
  'glossary': [{'w': 'club', 'pt': 'clube'}, {'w': 'sofa', 'pt': 'sofá'}, {'w': 'novel', 'pt': 'romance (livro)'}, {'w': 'cover', 'pt': 'capa'}, {'w': 'ending', 'pt': 'final'}, {'w': 'character', 'pt': 'personagem'}, {'w': 'plot', 'pt': 'enredo'}, {'w': 'secret', 'pt': 'segredo'}, {'w': 'chapter', 'pt': 'capítulo'}, {'w': 'recommend', 'pt': 'recomendar'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A woman at a book club', 'A man at a restaurant', 'A girl at school'], 'ans': 0, 'why': 'Lena goes to her first book club night.'},
  'scan': [{'q': 'What does Ava have in the living room?', 'ans': 'tea and cookies', 'alt': ['tea', 'cookies']}, {'q': 'What is the name of Ava’s dog?', 'ans': 'Wishbone', 'alt': ['wishbone']}, {'q': 'What is the next book?', 'ans': 'a mystery', 'alt': ['mystery']}],
  'tf': [{'s': 'Lena loved the ending.', 'ans': True, 'why': '“Yes, I loved the ending.”'}, {'s': 'Lena’s favorite character is the mother.', 'ans': False, 'why': 'It is the grandmother.'}, {'s': 'It is Lena’s tenth night at the club.', 'ans': False, 'why': 'It is her first night.'}, {'s': 'Ava has a dog named Wishbone.', 'ans': True, 'why': 'The dog has the same name as the TV dog.'}],
  'order': ['Lena goes to the book club.', 'Ava says, “Welcome to book club!”', 'Lena says she loved the ending.', 'Lena says the grandmother is her favorite.', 'Lena goes home happy.'],
  'ctx': [{'sent': 'They talk about the plot.', 'w': 'plot', 'opts': ['what happens in the story', 'the color of the book', 'the price of the book'], 'ans': 0, 'why': 'The plot is the events of a story.'}, {'sent': 'Would you recommend it?', 'w': 'recommend', 'opts': ['say it is good and suggest it', 'throw it away', 'forget it'], 'ans': 0, 'why': 'Recommend = tell someone to try something good.'}, {'sent': 'Everyone laughs.', 'w': 'laughs', 'opts': ['makes a happy sound', 'goes home', 'feels very tired'], 'ans': 0, 'why': 'People laugh when something is funny.'}],
  'chunkHunt': ['Welcome to book club!', 'Did you finish the book?', 'Who’s your favorite character?', 'Would you recommend it?'],
  'think': 'What book do you want to talk about with friends? Why?'},
 'convo': {'npc': {'name': 'Ava'}, 'story': 'You are at Ava’s book club for the first time. Talk about the book.', 'turns': [
  {'npc': 'Welcome to book club!', 'pt': 'Bem-vindos ao clube do livro!', 'opts': [
   {'en': 'Thanks for having me.', 'pt': 'Obrigada por me receber.', 'ok': True, 'fb': 'Polite thanks for the invitation.'},
   {'en': 'Thanks, I have a book club.', 'pt': 'Obrigada, eu tenho um clube do livro.', 'ok': False, 'fb': 'It does not answer the welcome.'},
   {'en': 'Good night, see you.', 'pt': 'Boa noite, até logo.', 'ok': False, 'fb': 'It is a goodbye, not a hello.'}]},
  {'npc': 'Did you finish the book?', 'pt': 'Você terminou o livro?', 'opts': [
   {'en': 'Yes, I finished it. I loved it.', 'pt': 'Sim, terminei. Adorei.', 'ok': False, 'fb': 'Good, but the key chunk here is the ending.'},
   {'en': 'Yes, I love the ending.', 'pt': 'Sim, eu amo o final.', 'ok': False, 'fb': 'Use the past: loved.'},
   {'en': 'Yes, I loved the ending.', 'pt': 'Sim, adorei o final.', 'ok': True, 'fb': 'Natural and in the past.'}]},
  {'npc': 'Who’s your favorite character?', 'pt': 'Quem é seu personagem favorito?', 'opts': [
   {'en': 'The grandmother. She’s so funny.', 'pt': 'A avó. Ela é muito engraçada.', 'ok': True, 'fb': 'Name + reason.'},
   {'en': 'The grandmother. He is so funny.', 'pt': 'A avó. Ele é muito engraçado.', 'ok': False, 'fb': 'A grandmother is she.'},
   {'en': 'On the table.', 'pt': 'Na mesa.', 'ok': False, 'fb': 'It does not fit the question.'}]},
  {'npc': 'I agree. And the story?', 'pt': 'Concordo. E a história?', 'opts': [
   {'en': 'The story is about a family and a secret.', 'pt': 'A história é sobre uma família e um segredo.', 'ok': False, 'fb': 'Good, but short is more natural: It’s about…'},
   {'en': 'It’s about a family and a secret.', 'pt': 'É sobre uma família e um segredo.', 'ok': True, 'fb': 'Short and clear.'},
   {'en': 'It speaks about a family.', 'pt': 'Fala sobre uma família.', 'ok': False, 'fb': 'Books are about something; they do not speak.'}]},
  {'npc': 'Would you recommend it?', 'pt': 'Você recomendaria?', 'opts': [
   {'en': 'Yes! It’s a great book.', 'pt': 'Sim! É um ótimo livro.', 'ok': True, 'fb': 'A clear yes with a reason.'},
   {'en': 'Yes, I recommend you.', 'pt': 'Sim, eu recomendo você.', 'ok': False, 'fb': 'You recommend the book, not the person.'},
   {'en': 'No, thanks, I am full.', 'pt': 'Não, obrigada, estou satisfeita.', 'ok': False, 'fb': 'Wrong meaning.'}]}]},
 'errors': [
  {'wrong': 'I am agree.', 'fix': 'I agree.', 'alt': 'I agree with.', 'why': 'In English, agree is a verb: I agree. No “am”.'},
  {'wrong': 'Did you finished the book?', 'fix': 'Did you finish the book?', 'alt': 'You finished the book?', 'why': 'After did, use the base verb: finish.'},
  {'wrong': 'The book speaks about a family.', 'fix': 'The book is about a family.', 'alt': 'The book talk about a family.', 'why': 'Use is about for a book or a movie.'},
  {'wrong': 'Thanks by invite me.', 'fix': 'Thanks for having me.', 'alt': 'Thanks for invite me.', 'why': 'Say Thanks for having me (or for inviting me).'}],
 'homework': 'Write 3 sentences about a book or movie you like: the title, a character and the ending.',
 'homework_items': ['Say aloud: Did you finish the book?', 'Write one sentence with ending and one with character.', 'Listen to the dialogue and shadow Ava.', 'Review: He is / She is and the word funny.']}
