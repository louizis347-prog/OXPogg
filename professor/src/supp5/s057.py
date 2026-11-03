"""Suplemento Quest v5 · aula 57: I'm lost + regular Which Way? (Treasure Planet)."""
TXT = [
 ['Ned lives in Boston.', 'One morning, he walks across the plaza.', 'A woman stands near the fountain.', 'She has a big map in her hands, and she looks worried.'],
 ['“**Excuse me, I’m lost**,” she says.', '“**Where do you want to go?**” Ned asks.', '“**To the Science Museum**,” she answers.', 'She shows him a name on the map.'],
 ['Ned thinks for a moment.', '“**It’s far from here. Take the bus**,” he says.', '“**Which bus?**” she asks.', '“**Number eighty-six. The stop is there**,” he says, and he points down the street.'],
 ['The woman smiles.', '“**Thank you very much**,” she says.', '“**Good luck!**” Ned says.', '“**Good luck, and safe travels!**” she says. Then she walks to the stop.'],
 ['Ned thinks of Treasure Planet, a Disney film from 2002.', 'In the story, a boy named Jim finds a map and follows it across space.', 'The crew asks, “Which way?” all the time.', 'Today, many people use a phone, but a kind answer is still better.', '“**Good thing we asked**,” Ned says to himself, and he goes to work.'],
]
SUPP = {
 'reg': 79,
 'badge': {'icon': '🧭', 'name': 'Direction Helper', 'desc': 'Say you are lost, ask where to go and give simple directions'},
 'culture': {
  'hook': 'Everyone gets lost sometimes. In English, one polite sentence and a smile are enough to start: most people stop and help, even in a big city.',
  'mythfact': [
   {'s': '“Excuse me” is a polite way to start a question to a stranger.', 'ans': True, 'why': 'People say it before they ask for help or directions.'},
   {'s': 'In the USA, distances on road signs are usually in kilometers.', 'ans': False, 'why': 'Road signs in the USA usually use miles.'},
   {'s': 'Boston is a city in the state of Massachusetts.', 'ans': True, 'why': 'It is one of the oldest big cities in the USA.'},
   {'s': 'In big American cities, nobody ever helps a person who is lost.', 'ans': False, 'why': 'Many people are happy to help, and a short question is normal.'},
   {'s': '“Treasure Planet” is a Disney film from 2002.', 'ans': True, 'why': 'It tells the story of “Treasure Island” with space pirates.'}],
  'wild': [
   {'kind': 'Bus stop sign', 'lines': ['**Route 86**', 'to Science Museum', 'Every 15 minutes'], 'decode': {'q': 'How often does the bus come?', 'opts': ['Every 15 minutes', 'Every 86 minutes', 'Only at night'], 'ans': 0, 'why': '“Every 15 minutes.”'}},
   {'kind': 'Street sign', 'lines': ['**Museum of Science**', '→ 0.5 mile', 'Open daily'], 'decode': {'q': 'Where is the museum?', 'opts': ['Half a mile this way', 'Five miles back', 'It is closed'], 'ans': 0, 'why': '0.5 mile = half a mile, and the arrow points ahead.'}}],
  'compare': {'br': 'In Brazil, people often say “Moço, onde fica…?” and sometimes walk with you to show the way.', 'us': 'In the USA, people usually give short directions with their hands: “Go straight, turn left.” Many also say “Use your phone.”', 'tip': 'Start with: “Excuse me, I’m lost.”', 'ask': 'How do you ask for directions in your city? Say it in English.'},
  'quiz': [
   {'q': 'You need help in the street. You say…', 'opts': ['Excuse me, I’m lost.', 'Excuse me, I am a map.', 'Hello, you are lost.'], 'ans': 0, 'why': 'I’m lost = I do not know where I am.'},
   {'q': '“It’s far from here.” It means…', 'opts': ['It is a long way', 'It is very close', 'It is closed'], 'ans': 0, 'why': 'Far = a long way.'},
   {'q': 'Someone says “Safe travels!” It means…', 'opts': ['Have a good, safe trip', 'Wait here', 'Go home'], 'ans': 0, 'why': 'We say it when a person goes on a trip.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'A Woman with a Map',
  'text': [' '.join(p) for p in TXT],
  'glossary': [{'w': 'plaza', 'pt': 'praça'}, {'w': 'fountain', 'pt': 'fonte / chafariz'}, {'w': 'map', 'pt': 'mapa'}, {'w': 'worried', 'pt': 'preocupada'}, {'w': 'lost', 'pt': 'perdido'}, {'w': 'museum', 'pt': 'museu'}, {'w': 'far', 'pt': 'longe'}, {'w': 'stop', 'pt': 'ponto (de ônibus)'}, {'w': 'points', 'pt': 'aponta'}, {'w': 'crew', 'pt': 'tripulação'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A woman who asks for directions', 'A big birthday party', 'A cooking lesson'], 'ans': 0, 'why': 'The woman is lost and Ned helps her.'},
  'scan': [{'q': 'Where does the woman want to go?', 'ans': 'the Science Museum', 'alt': ['to the Science Museum', 'Science Museum']}, {'q': 'Which bus does Ned say?', 'ans': 'number eighty-six', 'alt': ['86', 'eighty-six', 'number 86']}, {'q': 'What city does Ned live in?', 'ans': 'Boston', 'alt': ['boston']}],
  'tf': [{'s': 'The woman has a map.', 'ans': True, 'why': 'She has a big map in her hands.'}, {'s': 'The museum is near the plaza.', 'ans': False, 'why': 'Ned says it is far from here.'}, {'s': 'Ned says to take the bus.', 'ans': True, 'why': '“Take the bus.”'}, {'s': 'The woman is angry with Ned.', 'ans': False, 'why': 'She smiles and says thank you.'}],
  'order': ['The woman says she is lost.', 'Ned asks where she wants to go.', 'Ned says to take bus eighty-six.', 'The woman says thank you.', 'The woman walks to the stop.'],
  'ctx': [{'sent': 'The woman looks worried.', 'w': 'worried', 'opts': ['a little afraid or sad', 'very happy', 'very hungry'], 'ans': 0, 'why': 'Worried = thinking something bad can happen.'}, {'sent': 'It’s far from here.', 'w': 'far', 'opts': ['a long way', 'very near', 'very big'], 'ans': 0, 'why': 'Far = a long way.'}, {'sent': 'Good thing we asked.', 'w': 'Good thing', 'opts': ['It was lucky that', 'It is a nice object', 'It is bad that'], 'ans': 0, 'why': 'Good thing = it was lucky that…'}],
  'chunkHunt': ['Excuse me, I’m lost.', 'Where do you want to go?', 'It’s far from here.', 'Take the bus.'],
  'think': 'Do you ask a person or use your phone when you are lost? Why?'},
 'convo': {'npc': {'name': 'Grace'}, 'story': 'You are in a plaza in Boston. Grace has a map and looks lost. Help her.', 'turns': [
  {'npc': 'Excuse me, I’m lost.', 'pt': 'Com licença, estou perdida.', 'opts': [
   {'en': 'Where do you want to go?', 'pt': 'Aonde você quer ir?', 'ok': True, 'fb': 'A good first question.'},
   {'en': 'Where are you want to go?', 'pt': 'Onde você é querer ir?', 'ok': False, 'fb': 'Use Where do you want to go?'},
   {'en': 'I am lost too, goodbye.', 'pt': 'Também estou perdido, tchau.', 'ok': False, 'fb': 'It does not help her.'}]},
  {'npc': 'To the Science Museum.', 'pt': 'Ao Museu de Ciências.', 'opts': [
   {'en': 'It is long from here.', 'pt': 'É comprido daqui.', 'ok': False, 'fb': 'Say far for distance.'},
   {'en': 'It’s far from here. Take the bus.', 'pt': 'Fica longe daqui. Pegue o ônibus.', 'ok': True, 'fb': 'Clear and useful.'},
   {'en': 'It’s a museum, yes.', 'pt': 'É um museu, sim.', 'ok': False, 'fb': 'She knows. She needs directions.'}]},
  {'npc': 'Which bus?', 'pt': 'Qual ônibus?', 'opts': [
   {'en': 'Number eighty-six. The stop is there.', 'pt': 'O número oitenta e seis. O ponto é ali.', 'ok': True, 'fb': 'Number and place.'},
   {'en': 'Number eighteen. Stop is here.', 'pt': 'Número dezoito. Ponto é aqui.', 'ok': False, 'fb': 'Wrong number, and use The stop is…'},
   {'en': 'The bus is big.', 'pt': 'O ônibus é grande.', 'ok': False, 'fb': 'It does not answer Which bus?'}]},
  {'npc': 'Thank you very much.', 'pt': 'Muito obrigada.', 'opts': [
   {'en': 'You are welcome. Good luck!', 'pt': 'De nada. Boa sorte!', 'ok': False, 'fb': 'Good, but the dialogue answers with Good luck! only.'},
   {'en': 'Good luck!', 'pt': 'Boa sorte!', 'ok': True, 'fb': 'Short and friendly.'},
   {'en': 'Thank you very much too.', 'pt': 'Muito obrigado também.', 'ok': False, 'fb': 'You helped, so she thanks you.'}]},
  {'npc': 'Good luck, and safe travels!', 'pt': 'Boa sorte e boa viagem!', 'opts': [
   {'en': 'Thanks! Bye!', 'pt': 'Valeu! Tchau!', 'ok': True, 'fb': 'A natural end.'},
   {'en': 'I am lost now.', 'pt': 'Agora estou perdido.', 'ok': False, 'fb': 'It does not fit.'},
   {'en': 'Which bus?', 'pt': 'Qual ônibus?', 'ok': False, 'fb': 'She asked this before.'}]}]},
 'errors': [
  {'wrong': 'I am lose.', 'fix': 'I’m lost.', 'alt': 'I lost.', 'why': 'To say where you are, use am + lost.'},
  {'wrong': 'Where you want go?', 'fix': 'Where do you want to go?', 'alt': 'Where you are want to go?', 'why': 'Questions need do, and want is followed by to go.'},
  {'wrong': 'Is long from here.', 'fix': 'It’s far from here.', 'alt': 'It is far of here.', 'why': 'Use It’s far from here. Far is for distance.'},
  {'wrong': 'Take a bus eighty-six.', 'fix': 'Take bus number eighty-six.', 'alt': 'Take the bus number of eighty-six.', 'why': 'Say bus number + the number.'}],
 'homework': 'Write a short dialogue: someone is lost and you give directions to the bus stop.',
 'homework_items': ['Write: Excuse me, I’m lost. Where is…?', 'Record yourself giving directions to a place.', 'Listen to the dialogue again and shadow Grace.', 'Review: It’s far from here. / Take the bus.']}
