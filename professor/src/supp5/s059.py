"""Suplemento Quest v5 · aula 59: Is it far? + regular From Venice to China (The Travels of Marco Polo)."""
TXT = [
 ['Evan is new in Chicago.', 'He is at the plaza with a small bag.', 'He wants to see the lake, but he is not sure where it is.', 'The sun is out, and the day is warm.'],
 ['“**Excuse me, is the lake far from here?**” he asks a woman.', '“**Not really. It’s ten minutes on foot**,” she answers.', '“**Can I walk there?**” Evan asks.', 'He looks at his phone, but he likes to ask people.'],
 ['“**Yes. Go straight and then turn right**,” she says.', '“**Is it a nice walk?**” he asks.', '“**Yes, you’ll see many trees and bikes**,” she says.', 'Evan smiles.'],
 ['“**Should I take a bus?**” he asks.', '“**No, walking is better**,” she says.', 'Evan is a little tired, but the walk is short.', '“**Enjoy your walk!**” she says.', 'He says thank you and starts to walk.'],
 ['On the way, Evan thinks of Marco Polo, a traveler from Venice.', 'The book “The Travels of Marco Polo” says he went to China in the 1200s.', 'He traveled for years, by ship, by camel and on foot.', '“**That’s far!**” Evan says, and he laughs.', 'His own trip is only ten minutes.', 'He sees the lake, the trees and many bikes.'],
]
SUPP = {
 'reg': 116,
 'badge': {'icon': '🚶', 'name': 'Walk Planner', 'desc': 'Ask if a place is far and talk about walking time'},
 'culture': {
  'hook': 'In English, people measure a trip in minutes more often than in kilometers. “Ten minutes on foot” is the answer you will hear again and again in a new city.',
  'mythfact': [
   {'s': 'In the USA, people often use miles for distance.', 'ans': True, 'why': 'A mile is a little more than 1.6 kilometers.'},
   {'s': '“On foot” means by car.', 'ans': False, 'why': 'On foot = walking.'},
   {'s': 'Chicago is on the shore of a very big lake, Lake Michigan.', 'ans': True, 'why': 'The lake is so big that people use it for beaches and walks.'},
   {'s': 'Every city in the USA is easy to walk across.', 'ans': False, 'why': 'Some cities are walkable, but in many places people drive.'},
   {'s': 'Marco Polo was a traveler from Venice.', 'ans': True, 'why': 'His book tells about a long trip to China in the 1200s.'}],
  'wild': [
   {'kind': 'Park sign', 'lines': ['**Lakefront Trail**', 'Walk · Run · Bike', 'Beach 1 mile →'], 'decode': {'q': 'How far is the beach?', 'opts': ['One mile', 'Ten miles', 'Zero miles'], 'ans': 0, 'why': '“Beach 1 mile.”'}},
   {'kind': 'Phone map', 'lines': ['**Lake Park**', '🚶 12 min', '🚌 6 min', '🚲 4 min'], 'decode': {'q': 'How long is the walk?', 'opts': ['12 minutes', '6 minutes', '4 minutes'], 'ans': 0, 'why': 'The walking icon shows 12 min.'}}],
  'compare': {'br': 'In Brazil, people often say “são dez minutos a pé” or use blocks and corners to explain distance.', 'us': 'In the USA, people also say minutes (“ten minutes on foot”) or blocks, and for longer trips, miles.', 'tip': 'Ask: “Is it far from here?” and then: “Can I walk there?”', 'ask': 'How long is the walk from your home to the bus stop? Say it in English.'},
  'quiz': [
   {'q': 'You want to know if the lake is a long way. You say…', 'opts': ['Is the lake far from here?', 'Is the lake long from here?', 'The lake is far?'], 'ans': 0, 'why': 'Far is for distance.'},
   {'q': '“It’s ten minutes on foot.” It means…', 'opts': ['You walk for ten minutes', 'You take a ten-minute bus', 'It costs ten dollars'], 'ans': 0, 'why': 'On foot = walking.'},
   {'q': '“Not really.” in answer to “Is it far?” means…', 'opts': ['It is not very far', 'It is very far', 'I do not know'], 'ans': 0, 'why': 'Not really = no, not very.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Ten Minutes on Foot',
  'text': [' '.join(p) for p in TXT],
  'glossary': [{'w': 'plaza', 'pt': 'praça'}, {'w': 'lake', 'pt': 'lago'}, {'w': 'on foot', 'pt': 'a pé'}, {'w': 'straight', 'pt': 'em frente'}, {'w': 'trees', 'pt': 'árvores'}, {'w': 'bikes', 'pt': 'bicicletas'}, {'w': 'tired', 'pt': 'cansado'}, {'w': 'traveler', 'pt': 'viajante'}, {'w': 'camel', 'pt': 'camelo'}, {'w': 'ship', 'pt': 'navio'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A man asks the way to the lake', 'A man buys a bike', 'A man cooks dinner'], 'ans': 0, 'why': 'Evan asks if the lake is far.'},
  'scan': [{'q': 'How long is the walk?', 'ans': 'ten minutes', 'alt': ['10 minutes', 'ten']}, {'q': 'Which city is Evan in?', 'ans': 'Chicago', 'alt': ['chicago']}, {'q': 'Where was Marco Polo from?', 'ans': 'Venice', 'alt': ['venice']}],
  'tf': [{'s': 'The lake is ten minutes on foot.', 'ans': True, 'why': '“It’s ten minutes on foot.”'}, {'s': 'The woman says to take a bus.', 'ans': False, 'why': 'She says walking is better.'}, {'s': 'Evan will see trees and bikes.', 'ans': True, 'why': '“You’ll see many trees and bikes.”'}, {'s': 'Evan is very tired.', 'ans': False, 'why': 'He is a little tired, but the walk is short.'}],
  'order': ['Evan asks if the lake is far.', 'The woman says it is ten minutes on foot.', 'She says to go straight and turn right.', 'She says walking is better than the bus.', 'Evan thinks of Marco Polo.'],
  'ctx': [{'sent': 'It’s ten minutes on foot.', 'w': 'on foot', 'opts': ['walking', 'by car', 'by plane'], 'ans': 0, 'why': 'On foot = walking.'}, {'sent': 'Go straight and then turn right.', 'w': 'straight', 'opts': ['in a line, no turn', 'to the left', 'back'], 'ans': 0, 'why': 'Straight = without turning.'}, {'sent': 'That’s far!', 'w': 'far', 'opts': ['a long way', 'very close', 'very cold'], 'ans': 0, 'why': 'Far = a long way.'}],
  'chunkHunt': ['Is the lake far from here?', 'It’s ten minutes on foot.', 'Can I walk there?', 'Walking is better.'],
  'think': 'Do you like to walk or take a bus? How many minutes do you walk every day?'},
 'convo': {'npc': {'name': 'Evan'}, 'story': 'You are in a plaza in Chicago. Evan is a visitor and asks you about the lake. Help him.', 'turns': [
  {'npc': 'Excuse me, is the lake far from here?', 'pt': 'Com licença, o lago fica longe daqui?', 'opts': [
   {'en': 'Not really. It’s ten minutes on foot.', 'pt': 'Nem tanto. São dez minutos a pé.', 'ok': True, 'fb': 'Answer and give the time.'},
   {'en': 'Yes, I am the lake.', 'pt': 'Sim, eu sou o lago.', 'ok': False, 'fb': 'It does not make sense.'},
   {'en': 'It is long ten minutes.', 'pt': 'É longo dez minutos.', 'ok': False, 'fb': 'Say It’s ten minutes on foot.'}]},
  {'npc': 'Can I walk there?', 'pt': 'Posso ir a pé?', 'opts': [
   {'en': 'No, I do not walk.', 'pt': 'Não, eu não ando.', 'ok': False, 'fb': 'It does not answer his question.'},
   {'en': 'Yes. Go straight and then turn right.', 'pt': 'Sim. Siga em frente e vire à direita.', 'ok': True, 'fb': 'Short, clear directions.'},
   {'en': 'Yes, you walk straight right.', 'pt': 'Sim, você anda reto direita.', 'ok': False, 'fb': 'Say Go straight and turn right.'}]},
  {'npc': 'Is it a nice walk?', 'pt': 'É um bom passeio?', 'opts': [
   {'en': 'Yes, you’ll see many trees and bikes.', 'pt': 'Sim, você verá muitas árvores e bicicletas.', 'ok': True, 'fb': 'Natural, with details.'},
   {'en': 'Yes, many tree and bike.', 'pt': 'Sim, muita árvore e bicicleta.', 'ok': False, 'fb': 'Use trees and bikes.'},
   {'en': 'I am tired.', 'pt': 'Estou cansado.', 'ok': False, 'fb': 'It does not answer the question.'}]},
  {'npc': 'Should I take a bus?', 'pt': 'Devo pegar um ônibus?', 'opts': [
   {'en': 'Yes, take a plane.', 'pt': 'Sim, pegue um avião.', 'ok': False, 'fb': 'It does not fit.'},
   {'en': 'No, walking is better.', 'pt': 'Não, andar é melhor.', 'ok': True, 'fb': 'Walking is the subject, so: walking is.'},
   {'en': 'No, is better walk.', 'pt': 'Não, é melhor andar.', 'ok': False, 'fb': 'Say walking is better.'}]},
  {'npc': 'Enjoy your walk!', 'pt': 'Aproveite a caminhada!', 'opts': [
   {'en': 'Thanks! Have a nice day!', 'pt': 'Valeu! Tenha um bom dia!', 'ok': True, 'fb': 'A friendly end.'},
   {'en': 'Not really.', 'pt': 'Nem tanto.', 'ok': False, 'fb': 'It does not fit.'},
   {'en': 'It’s far from here.', 'pt': 'Fica longe daqui.', 'ok': False, 'fb': 'It is not what you said before.'}]}]},
 'errors': [
  {'wrong': 'Is it long from here?', 'fix': 'Is it far from here?', 'alt': 'Is it far of here?', 'why': 'For distance use far, and from here.'},
  {'wrong': 'It is ten minutes walking.', 'fix': 'It’s ten minutes on foot.', 'alt': 'It is ten minutes in foot.', 'why': 'The natural phrase is on foot.'},
  {'wrong': 'I can to walk there?', 'fix': 'Can I walk there?', 'alt': 'I can walk there?', 'why': 'Questions start with Can + subject + base verb.'},
  {'wrong': 'Walk is better.', 'fix': 'Walking is better.', 'alt': 'To walking is better.', 'why': 'Use walking (verb with -ing) as the subject.'}],
 'homework': 'Write 4 short sentences: how far your home is from a park and how you go there.',
 'homework_items': ['Write the time from your home to school or work.', 'Record yourself asking: Is it far from here?', 'Listen to the dialogue again and shadow Evan.', 'Review: on foot / Walking is better.']}
