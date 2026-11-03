"""Suplemento Quest v5 · aula 145: History walk (Boston) + regular How Do I Get to the River? (The Wind in the Willows)."""
SUPP = {
 'reg': 132,
 'badge': {'icon': '🧱', 'name': 'Freedom Trail Walker', 'desc': 'Join a walking tour and ask about time and distance'},
 'culture': {
  'hook': 'In Boston, a red line on the ground leads you through the history of the USA. You can follow it on your own or join a guided walking tour.',
  'mythfact': [
   {'s': 'The Freedom Trail in Boston is marked by a red line.', 'ans': True, 'why': 'The line is red brick or red paint on the sidewalk, so it is easy to follow.'},
   {'s': 'The Freedom Trail is about 2.5 miles long.', 'ans': True, 'why': 'That is about 4 kilometers, and it passes many historic sites.'},
   {'s': 'Boston is a very new city.', 'ans': False, 'why': 'It was founded in 1630, so it is one of the oldest cities in the USA.'},
   {'s': 'You must have a guide to walk the Freedom Trail.', 'ans': False, 'why': 'You can walk it alone, but many people like a guided tour.'},
   {'s': 'The Freedom Trail walk is mostly flat and easy.', 'ans': True, 'why': 'There are some stairs and bridges, but the walk is not very hard.'}],
  'wild': [
   {'kind': 'Tour poster', 'lines': ['**Freedom Trail Walking Tour**', 'Starts every hour', '90 minutes · Meet at the park'], 'decode': {'q': 'How long is the tour?', 'opts': ['90 minutes', '9 minutes', 'All day'], 'ans': 0, 'why': 'The poster says 90 minutes.'}},
   {'kind': 'Sign on the sidewalk', 'lines': ['**Follow the red line**', 'Next stop: Old State House', '0.2 miles'], 'decode': {'q': 'What should you follow?', 'opts': ['The red line', 'The green bus', 'The blue sign'], 'ans': 0, 'why': 'The sign says to follow the red line.'}}],
  'compare': {'br': 'In Brazil, many historic centers have guided walks, often with a local guide or a free map.', 'us': 'In Boston, you can follow a red line on the sidewalk. Guides often wear old-style clothes and tell stories.', 'tip': 'Ask: “When does it start?”', 'ask': 'Which historic place in your city do you like? Say it in English.'},
  'quiz': [
   {'q': 'You want to know the start time of a tour. You ask…', 'opts': ['When does it start?', 'When it starts?', 'What time start it?'], 'ans': 0, 'why': 'Use does + it + start.'},
   {'q': '“About two and a half miles” means…', 'opts': ['2.5 miles, more or less', 'exactly 25 miles', 'two miles and a house'], 'ans': 0, 'why': 'About = more or less.'},
   {'q': '“It’s easy and flat.” It means…', 'opts': ['Not hard, with no big hills', 'Very hard, with many hills', 'Very short'], 'ans': 0, 'why': 'Flat = no hills.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'The red line',
  'text': [
   'Pablo is visiting **Boston** with his friend Dana. It is a bright autumn morning. They stand in a park near an old building. A young woman holds a small flag.',
   '“**Hello! Are you here for the tour?**” the woman asks. “**Yes. When does it start?**” Pablo asks. “**In five minutes. Follow the red line**,” she says. Pablo looks down. A red line of bricks runs along the sidewalk. “**Why is there a red line?**” “**It shows the Freedom Trail**,” she says.',
   'Dana thinks about “The Wind in the Willows.” In the book, Mole and Rat walk along a river and go to the meadow. They ask, “How do I get to the river?” “Our red line is like the river,” Dana laughs. “We just follow it.”',
   '“**How long is the walk?**” Pablo asks. “**About two and a half miles**,” the guide says. “**Is it hard?**” “**No, it’s easy and flat.**” They go past a church, a harbor view and a very old street. The guide tells stories about the people of the city.',
   'At the end, Pablo and Dana feel tired but happy. They sit on a bench near the harbor. “History is not only in books,” Dana says. “It is under our feet.” Pablo looks at the red line and smiles.'],
  'glossary': [{'w': 'tour', 'pt': 'passeio guiado'}, {'w': 'flag', 'pt': 'bandeira'}, {'w': 'bricks', 'pt': 'tijolos'}, {'w': 'sidewalk', 'pt': 'calçada'}, {'w': 'trail', 'pt': 'trilha'}, {'w': 'harbor', 'pt': 'porto'}, {'w': 'church', 'pt': 'igreja'}, {'w': 'history', 'pt': 'história'}, {'w': 'guide', 'pt': 'guia'}],
  'fast': {'q': 'What is this story about?', 'opts': ['Two friends take a walking tour', 'A man cooks dinner', 'A woman buys a coat'], 'ans': 0, 'why': 'Pablo and Dana follow the red line in Boston.'},
  'scan': [{'q': 'When does the tour start?', 'ans': 'in five minutes', 'alt': ['five minutes', '5 minutes']}, {'q': 'What color is the line?', 'ans': 'red', 'alt': ['a red line']}, {'q': 'How long is the walk?', 'ans': 'about two and a half miles', 'alt': ['two and a half miles', '2.5 miles']}],
  'tf': [{'s': 'The tour starts in one hour.', 'ans': False, 'why': 'It starts in five minutes.'}, {'s': 'The line is made of red bricks.', 'ans': True, 'why': 'A red line of bricks runs along the sidewalk.'}, {'s': 'The walk is very hard.', 'ans': False, 'why': 'The guide says it is easy and flat.'}, {'s': 'Dana thinks about a book.', 'ans': True, 'why': '“The Wind in the Willows.”'}],
  'order': ['The guide welcomes Pablo and Dana.', 'The guide says the tour starts in five minutes.', 'They ask about the red line.', 'They ask how long the walk is.', 'They sit near the harbor.'],
  'ctx': [{'sent': 'A red line of bricks runs along the sidewalk.', 'w': 'sidewalk', 'opts': ['the path for people next to the road', 'the road for cars', 'a bridge'], 'ans': 0, 'why': 'People walk on the sidewalk.'}, {'sent': 'They sit near the harbor.', 'w': 'harbor', 'opts': ['a place where boats stay', 'a big park', 'a school'], 'ans': 0, 'why': 'Boats wait in a harbor.'}, {'sent': 'The tour guide holds a flag.', 'w': 'guide', 'opts': ['a person who shows a place', 'a map', 'a train driver'], 'ans': 0, 'why': 'A guide tells you about a place.'}],
  'chunkHunt': ['When does it start?', 'Follow the red line.', 'How long is the walk?', 'It’s easy and flat.'],
  'think': 'Do you like to learn about history when you travel? Why?'},
 'convo': {'npc': {'name': 'Grace'}, 'story': 'You arrive at a walking tour in Boston. Grace is the guide.', 'turns': [
  {'npc': 'Hello! Are you here for the tour?', 'pt': 'Olá! Vocês vieram para o passeio?', 'opts': [
   {'en': 'Yes. When does it start?', 'pt': 'Sim. Quando começa?', 'ok': True, 'fb': 'Natural reply and question.'},
   {'en': 'Yes. When it starts?', 'pt': 'Sim. Quando começa?', 'ok': False, 'fb': 'Use does: When does it start?'},
   {'en': 'Yes. What hour start?', 'pt': 'Sim. Que hora começar?', 'ok': False, 'fb': 'Wrong structure.'}]},
  {'npc': 'In five minutes. Follow the red line.', 'pt': 'Em cinco minutos. Sigam a linha vermelha.', 'opts': [
   {'en': 'Why is there a red line?', 'pt': 'Por que tem uma linha vermelha?', 'ok': True, 'fb': 'Good question.'},
   {'en': 'Why have a red line?', 'pt': 'Por que ter uma linha vermelha?', 'ok': False, 'fb': 'Say: Why is there…?'},
   {'en': 'Where is the red line yes?', 'pt': 'Onde é a linha vermelha sim?', 'ok': False, 'fb': 'It does not make sense.'}]},
  {'npc': 'It shows the Freedom Trail.', 'pt': 'Ela mostra a Trilha da Liberdade.', 'opts': [
   {'en': 'How much long is the walk?', 'pt': 'Quanto longo é a caminhada?', 'ok': False, 'fb': 'Say: How long is the walk?'},
   {'en': 'How long is the walk?', 'pt': 'Quanto tempo dura a caminhada?', 'ok': True, 'fb': 'Correct question.'},
   {'en': 'How long the walk is?', 'pt': 'Quanto tempo a caminhada é?', 'ok': False, 'fb': 'Put is before the walk.'}]},
  {'npc': 'About two and a half miles.', 'pt': 'Cerca de quatro quilômetros.', 'opts': [
   {'en': 'Is hard?', 'pt': 'É difícil?', 'ok': False, 'fb': 'Use it: Is it hard?'},
   {'en': 'It is hard yes?', 'pt': 'É difícil, sim?', 'ok': False, 'fb': 'Wrong order for a question.'},
   {'en': 'Is it hard?', 'pt': 'É difícil?', 'ok': True, 'fb': 'Correct and short.'}]},
  {'npc': 'No, it’s easy and flat.', 'pt': 'Não, é fácil e plano.', 'opts': [
   {'en': 'Great. Let’s go!', 'pt': 'Ótimo. Vamos!', 'ok': True, 'fb': 'Natural end of the talk.'},
   {'en': 'Great. I am flat.', 'pt': 'Ótimo. Eu sou plano.', 'ok': False, 'fb': 'Wrong meaning.'},
   {'en': 'Great. Is easy flat.', 'pt': 'Ótimo. É fácil plano.', 'ok': False, 'fb': 'Wrong grammar.'}]}]},
 'errors': [
  {'wrong': 'When it starts?', 'fix': 'When does it start?', 'alt': 'When does it starts?', 'why': 'A question needs does, and then the base verb: start.'},
  {'wrong': 'Why have a red line?', 'fix': 'Why is there a red line?', 'alt': 'Why there is a red line?', 'why': 'Use Why is there… for something that exists.'},
  {'wrong': 'How much long is the walk?', 'fix': 'How long is the walk?', 'alt': 'How many long is the walk?', 'why': 'For time or length, say How long.'},
  {'wrong': 'Is hard?', 'fix': 'Is it hard?', 'alt': 'It is hard?', 'why': 'English needs the subject: it.'}],
 'homework': 'Write a short dialogue: you join a walking tour and ask when it starts and how long it is.',
 'homework_items': ['Write 3 questions for a tour guide.', 'Say aloud: When does it start?', 'Listen to the dialogue and shadow Grace.', 'Review: easy / hard / flat.']}
