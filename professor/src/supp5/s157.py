"""Suplemento Quest v5 · aula 157: Pickup basketball + regular The Biggest and the Best (Guinness World Records)."""
SUPP = {
 'reg': 86,
 'badge': {'icon': '🏀', 'name': 'Pickup Player', 'desc': 'Join a game: team, shirt, ball and a nice shot'},
 'culture': {
  'hook': 'In the USA, many parks have a basketball court, and people play pickup games there. You do not need a team: you just ask, “Do you need one more player?”',
  'mythfact': [
   {'s': 'Basketball was invented in the USA.', 'ans': True, 'why': 'James Naismith created it in Massachusetts in 1891.'},
   {'s': 'You always need a reservation to play pickup basketball.', 'ans': False, 'why': 'Pickup means informal. At many public courts, people just arrive and join a game.'},
   {'s': 'In many parks, outdoor courts are free to use.', 'ans': True, 'why': 'Many public courts are free, but some places have rules and opening hours.'},
   {'s': 'At a pickup game, every player has the same uniform.', 'ans': False, 'why': 'People wear their own clothes, so teams may use shirts of two colors.'},
   {'s': '“Guinness World Records” is a book about records.', 'ans': True, 'why': 'It was first published in 1955 and lists the biggest, the fastest and the tallest in the world.'}],
  'wild': [
   {'kind': 'Park court sign', 'lines': ['**Basketball Court**', 'Open 6 a.m. – 10 p.m.', 'No glass bottles', 'Please share the court'], 'decode': {'q': 'What does “Please share the court” mean?', 'opts': ['Let other people play too', 'Play alone', 'Bring your own court'], 'ans': 0, 'why': 'Share = use it together with others.'}},
   {'kind': 'Group chat message', 'lines': ['**Pickup game tonight!**', '6 p.m. at Maple Park', 'We need two more players', 'Bring a light shirt and a dark shirt'], 'decode': {'q': 'Why do you bring two shirts?', 'opts': ['For the two teams', 'For two days', 'For the weather'], 'ans': 0, 'why': 'A light shirt and a dark shirt help to see the teams.'}}],
  'compare': {'br': 'In Brazil, friends often meet for a “racha” of football, and pickup basketball is also played in squares and clubs.', 'us': 'In the USA, pickup basketball in a park is very common. A friendly question is enough to join a game.', 'tip': 'Say: “Do you need one more player?”', 'ask': 'Do you play a sport with friends? Say the sport and the day.'},
  'quiz': [
   {'q': 'You want to join a game. You ask…', 'opts': ['Do you need one more player?', 'You need one more player?', 'Do you needs one player more?'], 'ans': 0, 'why': 'Do you need…? is the natural question.'},
   {'q': 'In “three on three,” how many players are in the game?', 'opts': ['six', 'three', 'nine'], 'ans': 0, 'why': 'Three players on each team: 3 + 3 = 6.'},
   {'q': 'A friend says, “Nice shot!” She means…', 'opts': ['You threw the ball well', 'You lost the game', 'You need a shirt'], 'ans': 0, 'why': 'Nice shot! is a compliment.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Three on three',
  'text': [
   'Finn is at a park in Phoenix. It is very hot, so the game is in the evening. Kai and his friends have a ball and a court.',
   '“**Hey! Do you want to play?**” Kai asks. “**Sure. Do you need one more player?**” Finn says. “**Yes, we’re three on three.**” “**Which team am I on?**” “**You’re with us. Take a blue shirt.**”',
   'The game starts. “**Who has the ball?**” Finn asks. “**I do. Pass it to me!**” Kai says. Finn runs and shouts, “**Here! Shoot!**” Kai shoots, and the ball goes in. “**Nice shot!**” everyone says.',
   'Later, Finn shoots, but he misses. “Keep trying!” his team says. After the game, Finn remembers a book from school, “Guinness World Records.” It is a book of records, first published in 1955. It lists the tallest, the fastest and the biggest things in the world. Finn laughs and says, “I am not the best player today. I can try again.”',
   'The sun goes down. The players sit on a bench and drink water. “**Good game!**” Kai says. “See you next week,” Finn says. He goes home tired and happy.'],
  'glossary': [{'w': 'court', 'pt': 'quadra'}, {'w': 'team', 'pt': 'time'}, {'w': 'shirt', 'pt': 'camisa'}, {'w': 'shoots', 'pt': 'arremessa'}, {'w': 'misses', 'pt': 'erra'}, {'w': 'records', 'pt': 'recordes'}, {'w': 'tallest', 'pt': 'o mais alto'}, {'w': 'bench', 'pt': 'banco'}, {'w': 'evening', 'pt': 'fim de tarde / noite'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A man joins a basketball game', 'A girl cooks dinner', 'A boy buys shoes'], 'ans': 0, 'why': 'Finn joins a game in a park.'},
  'scan': [{'q': 'Where is Finn?', 'ans': 'at a park in Phoenix', 'alt': ['park', 'in Phoenix', 'Phoenix']}, {'q': 'What color is Finn’s shirt?', 'ans': 'blue', 'alt': ['a blue shirt']}, {'q': 'What does Kai say after the shot?', 'ans': 'Nice shot', 'alt': ['Nice shot!', 'nice shot']}],
  'tf': [{'s': 'Kai and his friends are four on four.', 'ans': False, 'why': 'They are three on three.'}, {'s': 'Finn is on Kai’s team.', 'ans': True, 'why': '“You’re with us.”'}, {'s': 'The game is in the morning.', 'ans': False, 'why': 'It is very hot, so the game is in the evening.'}, {'s': 'Finn remembers a book of records.', 'ans': True, 'why': 'It is “Guinness World Records.”'}],
  'order': ['Kai asks Finn to play.', 'Finn takes a blue shirt.', 'Kai shoots and the ball goes in.', 'Finn misses a shot and remembers a book.', 'Finn says, “See you next week.”'],
  'ctx': [{'sent': 'Finn shoots, but he misses.', 'w': 'misses', 'opts': ['does not get it', 'wins the game', 'goes home'], 'ans': 0, 'why': 'Miss = not hit the target.'}, {'sent': 'The players sit on a bench.', 'w': 'bench', 'opts': ['a long seat', 'a small ball', 'a blue shirt'], 'ans': 0, 'why': 'A bench is a long seat for many people.'}, {'sent': 'The book has many records.', 'w': 'records', 'opts': ['the best or biggest results', 'old songs', 'team shirts'], 'ans': 0, 'why': 'A record is the best, biggest or fastest result.'}],
  'chunkHunt': ['Do you need one more player?', 'Which team am I on?', 'Who has the ball?', 'Nice shot!'],
  'think': 'Do you like to play a sport with friends? Which one?'},
 'convo': {'npc': {'name': 'Kai'}, 'story': 'You are at a park. Kai asks you to join a basketball game.', 'turns': [
  {'npc': 'Hey! Do you want to play?', 'pt': 'Oi! Quer jogar?', 'opts': [
   {'en': 'Sure. Do you need one more player?', 'pt': 'Claro. Precisam de mais um jogador?', 'ok': True, 'fb': 'Accepts and asks a useful question.'},
   {'en': 'Sure. You need more one player?', 'pt': 'Claro. Você precisa mais um jogador?', 'ok': False, 'fb': 'Use Do you need one more player?'},
   {'en': 'Nice shot!', 'pt': 'Bela cesta!', 'ok': False, 'fb': 'Too early. No shot yet.'}]},
  {'npc': 'Yes, we’re three on three.', 'pt': 'Sim, somos três contra três.', 'opts': [
   {'en': 'In which team I am?', 'pt': 'Em qual time eu estou?', 'ok': False, 'fb': 'Say: Which team am I on?'},
   {'en': 'Which team am I on?', 'pt': 'Em que time estou?', 'ok': True, 'fb': 'Natural question order.'},
   {'en': 'Yes, I am three.', 'pt': 'Sim, eu sou três.', 'ok': False, 'fb': 'Does not fit.'}]},
  {'npc': 'You’re with us. Take a blue shirt.', 'pt': 'Você está conosco. Pegue uma camisa azul.', 'opts': [
   {'en': 'Thanks. Who has the ball?', 'pt': 'Valeu. Quem está com a bola?', 'ok': True, 'fb': 'Thanks first, then the question.'},
   {'en': 'Thanks. Who have the ball?', 'pt': 'Valeu. Quem tem a bola?', 'ok': False, 'fb': 'Who has (not have).'},
   {'en': 'You’re welcome. Take a shirt.', 'pt': 'De nada. Pegue uma camisa.', 'ok': False, 'fb': 'Kai gave you the shirt; you say thanks.'}]},
  {'npc': 'I do. Pass it to me!', 'pt': 'Eu estou. Passe para mim!', 'opts': [
   {'en': 'Thanks. Who has the ball?', 'pt': 'Valeu. Quem está com a bola?', 'ok': False, 'fb': 'Kai just said: I do.'},
   {'en': 'Pass to me the ball!', 'pt': 'Passe para mim a bola!', 'ok': False, 'fb': 'Wrong word order.'},
   {'en': 'Here! Shoot!', 'pt': 'Aqui! Arremesse!', 'ok': True, 'fb': 'Short and quick, like in a game.'}]},
  {'npc': 'Nice shot!', 'pt': 'Bela cesta!', 'opts': [
   {'en': 'Thanks! Good game.', 'pt': 'Valeu! Bom jogo.', 'ok': True, 'fb': 'Friendly reply.'},
   {'en': 'Is a nice shoot.', 'pt': 'É um belo arremessar.', 'ok': False, 'fb': 'Shot is the noun.'},
   {'en': 'Take a blue shirt.', 'pt': 'Pegue uma camisa azul.', 'ok': False, 'fb': 'It does not fit now.'}]}]},
 'errors': [
  {'wrong': 'Do you need one more players?', 'fix': 'Do you need one more player?', 'alt': 'Do you need more one player?', 'why': 'After one, use a singular noun: one more player.'},
  {'wrong': 'In which team I am?', 'fix': 'Which team am I on?', 'alt': 'Which team I am on?', 'why': 'In a question, the verb comes before I: am I on?'},
  {'wrong': 'Who have the ball?', 'fix': 'Who has the ball?', 'alt': 'Who is have the ball?', 'why': 'Who + he/she form: has.'},
  {'wrong': 'Pass to me the ball!', 'fix': 'Pass the ball to me!', 'alt': 'Pass me to the ball!', 'why': 'Say pass + thing + to + person.'}],
 'homework': 'Write 4 sentences to ask to join a game: ask for a place, a team, a shirt and the ball.',
 'homework_items': ['Say aloud: Which team am I on?', 'Write: Who has the ball? and answer with I do.', 'Listen to the dialogue and shadow Kai.', 'Review: three on three, one more player.']}
