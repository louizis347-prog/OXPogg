"""Suplemento Quest v5 · aula 44: Turn left, turn right + regular Which way is the park? (The Fellowship of the Ring)."""
SUPP = {
 'reg': 144,
 'badge': {'icon': '🧭', 'name': 'Direction Pro', 'desc': 'Give and follow simple directions in English'},
 'sticker': {'cat': 'Everyday culture', 'title': 'Walking Directions in the USA', 'sub': 'Blocks, lights and corners'},
 'culture': {
  'hook': 'In many American cities, people give directions with blocks, traffic lights and left or right turns. A short answer with two or three steps is usually enough.',
  'polite': 'Finish with **“You can’t miss it!”** to tell the person the place is easy to see.',
  'mythfact': [
   {'s': 'In Manhattan, streets run east-west and avenues run north-south.', 'ans': True, 'why': 'This grid helps people find addresses quickly.'},
   {'s': 'Boston has only straight, new streets.', 'ans': False, 'why': 'Boston is old and many of its streets are narrow and curved.'},
   {'s': 'A “block” is the distance from one street to the next.', 'ans': True, 'why': 'People say “walk two blocks”.'},
   {'s': 'Pedestrians must cross when the signal says “Don’t Walk”.', 'ans': False, 'why': 'Wait for the “Walk” signal to cross safely.'}],
  'wild': [
   {'kind': 'Street sign', 'lines': ['**Museum of Science →**', '2 blocks', '**Parking ←**', '1 block'], 'decode': {'q': 'Which way is the museum?', 'opts': ['To the right', 'To the left', 'Behind you'], 'ans': 0, 'why': 'The arrow points right (→).'}},
   {'kind': 'Message from a friend', 'lines': ['Go straight for two blocks.', 'Turn left at the traffic light.', 'My building has a red door!'], 'decode': {'q': 'Where do you turn left?', 'opts': ['At the traffic light', 'At the red door', 'After one block'], 'ans': 0, 'why': '“Turn left at the traffic light.”'}}],
  'compare': {'br': 'In Brazil people often say “segue reto” and use landmarks like a bakery, a church or a gas station.', 'us': 'In the USA people also count blocks and say “turn left at the light”.', 'tip': 'Say the steps in order: straight, turn, walk one more block.', 'ask': 'Explain how to go from your door to a nearby store, in English.'},
  'quiz': [
   {'q': '“Go straight for two blocks.” means…', 'opts': ['Walk forward past two blocks', 'Turn left twice', 'Stop here'], 'ans': 0, 'why': 'Straight = forward, no turn.'},
   {'q': 'The museum is “on your right”. It is…', 'opts': ['On the right side of you', 'Behind you', 'Very far'], 'ans': 0, 'why': 'On your right = on the right side.'},
   {'q': 'When you say “You can’t miss it”, you mean…', 'opts': ['It is easy to see', 'It is closed', 'It is far'], 'ans': 0, 'why': 'It is very easy to find.'}]},
 'reading': {
  'genre': 'Travel blog', 'title': 'A walk to the museum in Boston',
  'text': [
   'On my second day in Boston, I wanted to see a museum. I was near a park, and I saw a woman with a coffee. “**Excuse me, how do I get to the museum?**” I asked.',
   '“**Go straight for two blocks**,” she said. I repeated, “Two blocks, then?” She smiled. “**Turn left at the traffic light**.” “And then?” I asked. “**Walk one more block. It’s on your right**.”',
   'I asked, “Is it a big building?” “**Yes, with a red door**,” she said. “**Good luck! You can’t miss it**.” I said thanks and started to walk. The sun was warm, and the streets were quiet.',
   'I counted: one block, two blocks. At the corner, there was a traffic light, and it was red. I waited. When it turned green, I crossed and turned left. I walked one more block and looked to my right.',
   'There it was! A tall brick building with a big red door. The woman was right: I could not miss it. I felt proud because I understood the directions in English.',
   'Next time, I will ask more questions and use my phone less. People are friendly, and a short conversation can be the best map.'],
  'glossary': [{'w': 'museum', 'pt': 'museu'}, {'w': 'park', 'pt': 'parque'}, {'w': 'straight', 'pt': 'em frente'}, {'w': 'blocks', 'pt': 'quarteirões'}, {'w': 'traffic light', 'pt': 'semáforo'}, {'w': 'corner', 'pt': 'esquina'}, {'w': 'brick', 'pt': 'tijolo'}, {'w': 'proud', 'pt': 'orgulhoso'}, {'w': 'quiet', 'pt': 'tranquilas'}],
  'fast': {'q': 'What is this text about?', 'opts': ['Directions to a museum in Boston', 'A recipe for soup', 'A flight to Brazil'], 'ans': 0, 'why': 'The writer asks and follows directions to the museum.'},
  'scan': [{'q': 'How many blocks straight first?', 'ans': 'two', 'alt': ['2', 'two blocks']}, {'q': 'Where do you turn left?', 'ans': 'at the traffic light', 'alt': ['traffic light', 'at the light']}, {'q': 'What color is the door?', 'ans': 'red', 'alt': ['a red door']}],
  'tf': [{'s': 'The writer asks a woman for directions.', 'ans': True, 'why': 'She is the first person he asks.'}, {'s': 'The museum is on the left.', 'ans': False, 'why': 'It is on the right.'}, {'s': 'The building has a red door.', 'ans': True, 'why': '“A big red door.”'}, {'s': 'The writer cannot understand English.', 'ans': False, 'why': 'He is proud because he understood.'}],
  'order': ['The writer asks how to get to the museum.', 'He goes straight for two blocks.', 'He waits at the traffic light.', 'He turns left and walks one more block.', 'He sees the building with the red door.'],
  'ctx': [{'sent': 'The streets were quiet.', 'w': 'quiet', 'opts': ['with little noise', 'very dirty', 'very new'], 'ans': 0, 'why': 'Quiet = not noisy.'}, {'sent': 'I felt proud because I understood the directions.', 'w': 'proud', 'opts': ['happy about my work', 'angry', 'tired'], 'ans': 0, 'why': 'Proud = happy about something you did.'}, {'sent': 'I could not miss it.', 'w': 'miss', 'opts': ['fail to see', 'feel sad about', 'throw away'], 'ans': 0, 'why': 'You can’t miss it = it is easy to see.'}],
  'chunkHunt': ['How do I get to…?', 'Go straight for two blocks.', 'Turn left at the traffic light.', 'It’s on your right.', 'You can’t miss it.'],
  'think': 'How do you give directions in your city? Say three steps in English.'},
 'convo': {'npc': {'name': 'Grace'}, 'story': 'You are on a street in Boston. Grace needs to find the museum. Give her directions.', 'turns': [
  {'npc': 'Excuse me, how do I get to the museum?', 'pt': 'Com licença, como chego ao museu?', 'opts': [
   {'en': 'You go straight two block.', 'pt': 'Você vai reto dois quarteirão.', 'ok': False, 'fb': 'Use two blocks (plural).'},
   {'en': 'Go straight for two blocks.', 'pt': 'Siga em frente por dois quarteirões.', 'ok': True, 'fb': 'Clear first step.'},
   {'en': 'I love the museum.', 'pt': 'Eu amo o museu.', 'ok': False, 'fb': 'Does not give directions.'}]},
  {'npc': 'Then?', 'pt': 'Depois?', 'opts': [
   {'en': 'Then you turn to left of light.', 'pt': 'Depois você vira para esquerda de semáforo.', 'ok': False, 'fb': 'Say turn left at the light.'},
   {'en': 'It is Tuesday.', 'pt': 'É terça.', 'ok': False, 'fb': 'Out of context.'},
   {'en': 'Turn left at the traffic light.', 'pt': 'Vire à esquerda no semáforo.', 'ok': True, 'fb': 'Turn + direction + where.'}]},
  {'npc': 'And then?', 'pt': 'E depois?', 'opts': [
   {'en': 'Walk one more block. It’s on your right.', 'pt': 'Ande mais um quarteirão. Fica à sua direita.', 'ok': True, 'fb': 'Last step with the side.'},
   {'en': 'Walk more one block.', 'pt': 'Ande mais um quarteirão.', 'ok': False, 'fb': 'Say one more block.'},
   {'en': 'Then you are right.', 'pt': 'Depois você está certo.', 'ok': False, 'fb': 'Wrong meaning of right.'}]},
  {'npc': 'Is it a big building?', 'pt': 'É um prédio grande?', 'opts': [
   {'en': 'Yes, with a red door.', 'pt': 'Sim, com uma porta vermelha.', 'ok': True, 'fb': 'Helpful detail.'},
   {'en': 'No, it have a door.', 'pt': 'Não, tem uma porta.', 'ok': False, 'fb': 'It has, not it have.'},
   {'en': 'I am big.', 'pt': 'Eu sou grande.', 'ok': False, 'fb': 'Wrong subject.'}]},
  {'npc': 'Good luck! You can’t miss it.', 'pt': 'Boa sorte! Não tem como errar.', 'opts': [
   {'en': 'You are welcome. I miss it.', 'pt': 'De nada. Eu sinto falta.', 'ok': False, 'fb': 'Miss means something else here.'},
   {'en': 'Thanks, man.', 'pt': 'Valeu, cara.', 'ok': False, 'fb': 'She said it to you; answer You’re welcome.'},
   {'en': 'You’re welcome. Have a nice day!', 'pt': 'De nada. Tenha um bom dia!', 'ok': True, 'fb': 'Polite end.'}]}]},
 'errors': [
  {'wrong': 'Go straight two block.', 'fix': 'Go straight for two blocks.', 'alt': 'Go straight to two block.', 'why': 'Use for and the plural blocks.'},
  {'wrong': 'Turn to the left in the light.', 'fix': 'Turn left at the traffic light.', 'alt': 'Turn left on the light.', 'why': 'Say turn left and use at the light.'},
  {'wrong': 'It is in your right.', 'fix': 'It is on your right.', 'alt': 'It is at your right.', 'why': 'Use on your right/left.'},
  {'wrong': 'How I go to the museum?', 'fix': 'How do I get to the museum?', 'alt': 'How I get to the museum?', 'why': 'Questions use do + I + get.'}],
 'homework': 'Write directions from your home to the nearest store in 4 sentences, using straight, turn and block.',
 'homework_items': ['Write 4 steps with straight, turn left/right, block.', 'Record yourself giving directions for 30 seconds.', 'Draw a mini map and mark left and right.', 'Review: Turn left at the light / It’s on your right.']}
