"""Suplemento Quest v5 · aula 86: Movie night + regular Awesome! Cool! Great! (Ted Lasso)."""
SUPP = {
 'reg': 99,
 'badge': {'icon': '🍿', 'name': 'Movie Night Pro', 'desc': 'Choose a movie, a time, seats and popcorn'},
 'culture': {
  'hook': 'In the USA, a night at the movies has simple steps: choose a film, check the time, buy tickets on a phone app or at the desk, and get some popcorn.',
  'mythfact': [
   {'s': 'In many US cinemas, you can choose your seat when you buy the ticket.', 'ans': True, 'why': 'Many cinemas show a seat map on the app or on the website, but not all of them do.'},
   {'s': 'Popcorn is a very common snack at the cinema in the USA.', 'ans': True, 'why': 'Most cinemas sell it in small, medium and large sizes.'},
   {'s': 'The film always starts at the exact time on your ticket.', 'ans': False, 'why': 'Many cinemas show trailers first, so the film starts a little later.'},
   {'s': 'You must buy tickets only at the cinema door.', 'ans': False, 'why': 'Many people buy tickets online before they go.'},
   {'s': '“Ted Lasso” is a comedy series.', 'ans': True, 'why': 'It is a comedy series from 2020 about a kind American coach in England.'}],
  'wild': [
   {'kind': 'Cinema screen board', 'lines': ['**Comedy** 7:00 p.m.', '**Action** 8:00 p.m.', '**Cartoon** 5:30 p.m.'], 'decode': {'q': 'Which film starts at eight?', 'opts': ['The action film', 'The comedy', 'The cartoon'], 'ans': 0, 'why': 'Action is at 8:00 p.m.'}},
   {'kind': 'Snack menu', 'lines': ['**Popcorn** small $6 · large $9', '**Soda** $5', '**Candy** $4'], 'decode': {'q': 'How much is a large popcorn?', 'opts': ['$9', '$6', '$5'], 'ans': 0, 'why': 'Large popcorn is $9.'}}],
  'compare': {'br': 'In Brazil, many people say “vamos ao cinema” and buy a combo with popcorn and a drink.', 'us': 'In the USA, a small, medium or large popcorn is common, and many cinemas let you choose your seat online.', 'tip': 'Say: “A large popcorn, please.”', 'ask': 'Do you like comedies or action films? Say it in English.'},
  'quiz': [
   {'q': 'You want to know the time. You ask…', 'opts': ['What time does it start?', 'What time it starts?', 'When time start?'], 'ans': 0, 'why': 'With does, the verb has no -s: start.'},
   {'q': 'A friend asks “Do you want popcorn?” You want a big one. You say…', 'opts': ['Yes, a large one!', 'Yes, I large.', 'Popcorn is yes.'], 'ans': 0, 'why': 'A large one = um grande.'},
   {'q': 'What is a trailer?', 'opts': ['a short video of a film', 'a big truck', 'a cinema seat'], 'ans': 0, 'why': 'A trailer shows small parts of a film before it opens.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Friday at the cinema',
  'text': [
   'It is Friday night. Mia and her friend Sam want to watch a film. “**What do you want to watch tonight?**” Sam asks. “**I like comedies**,” Mia says. “**And you?**” “**I like action movies**,” Sam says. Then he smiles. “**How about a comedy tonight?**”',
   '“**What time does it start?**” Mia asks. “**At eight. Let’s buy tickets online.**” They use a phone app and pick two seats in row F. The seats are in the middle, near the big screen.',
   'At the cinema, the room is dark. A trailer starts. “**Do you want popcorn?**” Sam asks. “**Yes, a large one!**” Mia says. Sam pays, and they find their row. A man at the door says, “**Enjoy the movie!**”',
   'Mia thinks about “Ted Lasso,” a comedy series about an American coach in England. Ted is kind, and he often says, “Awesome!” and “Great!” Mia likes that kind of comedy.',
   'The film ends. An actor makes a funny face on the screen, and everybody laughs. “**That was awesome!**” Mia says. Sam laughs too. “**Great idea, Mia!**” They eat the last popcorn and walk home.'],
  'glossary': [{'w': 'comedies', 'pt': 'comédias'}, {'w': 'online', 'pt': 'pela internet'}, {'w': 'app', 'pt': 'aplicativo'}, {'w': 'row', 'pt': 'fileira'}, {'w': 'screen', 'pt': 'tela'}, {'w': 'trailer', 'pt': 'trailer, prévia do filme'}, {'w': 'popcorn', 'pt': 'pipoca'}, {'w': 'actor', 'pt': 'ator'}, {'w': 'laughs', 'pt': 'ri'}, {'w': 'kind', 'pt': 'gentil'}],
  'fast': {'q': 'What is this story about?', 'opts': ['Two friends go to the cinema', 'A man buys a car', 'A girl cooks dinner'], 'ans': 0, 'why': 'Mia and Sam choose a comedy and watch it.'},
  'scan': [{'q': 'What time does the film start?', 'ans': 'at eight', 'alt': ['eight', '8', '8 o’clock']}, {'q': 'Which row are the seats in?', 'ans': 'row F', 'alt': ['F']}, {'q': 'What size is Mia’s popcorn?', 'ans': 'large', 'alt': ['a large one', 'a large']}],
  'tf': [{'s': 'Mia likes comedies.', 'ans': True, 'why': '“I like comedies.”'}, {'s': 'Sam buys tickets at the door.', 'ans': False, 'why': 'They buy tickets online.'}, {'s': 'The seats are in the middle.', 'ans': True, 'why': 'The seats are in the middle, near the screen.'}, {'s': 'Mia does not want popcorn.', 'ans': False, 'why': 'She says, “Yes, a large one!”'}],
  'order': ['Sam and Mia choose a comedy.', 'They buy tickets online.', 'Sam asks about popcorn.', 'They watch the film.', 'They walk home.'],
  'ctx': [{'sent': 'They buy tickets online.', 'w': 'online', 'opts': ['on the internet', 'in a shop', 'on the street'], 'ans': 0, 'why': 'Online = pela internet.'}, {'sent': 'A trailer starts.', 'w': 'trailer', 'opts': ['a short video about a film', 'a loud song', 'a cinema door'], 'ans': 0, 'why': 'A trailer is a short preview.'}, {'sent': 'Everybody laughs.', 'w': 'laughs', 'opts': ['makes a happy sound', 'goes home', 'is very sad'], 'ans': 0, 'why': 'People laugh at funny things.'}],
  'chunkHunt': ['What do you want to watch tonight?', 'How about a comedy tonight?', 'What time does it start?', 'Enjoy the movie!'],
  'think': 'Do you like comedies or action films? Why?'},
 'convo': {'npc': {'name': 'Cole'}, 'story': 'You plan a movie night with your friend Cole. Answer him.', 'turns': [
  {'npc': 'What do you want to watch tonight?', 'pt': 'O que você quer ver hoje à noite?', 'opts': [
   {'en': 'I like comedies. And you?', 'pt': 'Gosto de comédias. E você?', 'ok': True, 'fb': 'Natural answer, and a question back.'},
   {'en': 'I watch comedy yesterday.', 'pt': 'Eu vi comédia ontem.', 'ok': False, 'fb': 'Wrong time and wrong grammar.'},
   {'en': 'At eight o’clock.', 'pt': 'Às oito.', 'ok': False, 'fb': 'He asks what, not when.'}]},
  {'npc': 'I like action movies.', 'pt': 'Gosto de filmes de ação.', 'opts': [
   {'en': 'I am a comedy.', 'pt': 'Eu sou uma comédia.', 'ok': False, 'fb': 'Wrong meaning.'},
   {'en': 'How about a comedy tonight?', 'pt': 'Que tal uma comédia hoje?', 'ok': True, 'fb': 'A friendly idea.'},
   {'en': 'How about to watch?', 'pt': 'Que tal para ver?', 'ok': False, 'fb': 'Say: How about + a thing.'}]},
  {'npc': 'OK. What time does it start?', 'pt': 'Ok. Que horas começa?', 'opts': [
   {'en': 'At eight. Let’s buy tickets online.', 'pt': 'Às oito. Vamos comprar ingressos online.', 'ok': True, 'fb': 'Gives the time and a plan.'},
   {'en': 'It starts for eight.', 'pt': 'Começa para oito.', 'ok': False, 'fb': 'Use at + time.'},
   {'en': 'I like popcorn.', 'pt': 'Gosto de pipoca.', 'ok': False, 'fb': 'Does not answer the time.'}]},
  {'npc': 'Do you want popcorn?', 'pt': 'Quer pipoca?', 'opts': [
   {'en': 'Yes, a large one!', 'pt': 'Quero, uma grande!', 'ok': True, 'fb': 'Short and natural.'},
   {'en': 'Yes, I want.', 'pt': 'Sim, eu quero.', 'ok': False, 'fb': 'Better: Yes, I do.'},
   {'en': 'Popcorn is eight.', 'pt': 'Pipoca é oito.', 'ok': False, 'fb': 'Does not fit.'}]},
  {'npc': 'Enjoy the movie!', 'pt': 'Aproveite o filme!', 'opts': [
   {'en': 'Welcome to the movie!', 'pt': 'Bem-vindo ao filme!', 'ok': False, 'fb': 'Not the right reply.'},
   {'en': 'I enjoy the film now.', 'pt': 'Eu aproveito o filme agora.', 'ok': False, 'fb': 'It sounds strange here.'},
   {'en': 'Thanks! You too!', 'pt': 'Obrigado! Você também!', 'ok': True, 'fb': 'Natural reply.'}]}]},
 'errors': [
  {'wrong': 'I want see a comedy.', 'fix': 'I want to see a comedy.', 'alt': 'I want seeing a comedy.', 'why': 'After want, use to + verb.'},
  {'wrong': 'What time it starts?', 'fix': 'What time does it start?', 'alt': 'What time does it starts?', 'why': 'In questions, use does + start (no -s).'},
  {'wrong': 'I am liking comedies.', 'fix': 'I like comedies.', 'alt': 'I am like comedies.', 'why': 'Like is a state verb: no -ing.'},
  {'wrong': 'Yes, a large.', 'fix': 'Yes, a large one!', 'alt': 'Yes, one large.', 'why': 'Use one to avoid repeating popcorn.'}],
 'homework': 'Write a short dialogue: you and a friend choose a film, a time and a snack.',
 'homework_items': ['Write 3 film types you like.', 'Say aloud: What time does it start?', 'Listen to the dialogue and shadow Cole.', 'Review: I like… / How about…?']}
