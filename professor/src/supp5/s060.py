"""Suplemento Quest v5 · aula 60: Crossing the street + regular First, Next, Then, Finally (Sesame Street)."""
TXT = [
 ['Uma lives in Portland.', 'This morning, she is late for class.', 'She walks fast to the corner.', 'The light is red, but she is ready to cross.', 'Many people wait there with her.', 'There is a lot of traffic on the street.'],
 ['Her friend Carlos is at the corner too.', '“**Wait! The light is red**,” he says.', '“**Thanks. When can I cross?**” Uma asks.', '“**When the light is green**,” Carlos says.'],
 ['The light changes.', '“**Now it’s green. Let’s go**,” says Uma.', '“**Look both ways!**” Carlos says.', '“**Good point. Cars are coming**,” she says.', 'A car turns the corner, and then it stops.', 'The driver waves at them.'],
 ['“**Be careful with bikes too**,” Carlos says.', 'A bike goes fast on the street.', '“**Thanks, I will**,” Uma says.', 'They walk across on the crosswalk.', '“**Have a safe walk!**” Carlos says. Uma smiles.'],
 ['Many children’s shows teach safe habits.', 'Sesame Street, a TV show from 1969, uses simple steps for children.', 'First, stop. Next, look. Then, listen. Finally, cross.', 'Uma knows the steps.', '“**Safety first**,” she says, and she runs to class.'],
]
SUPP = {
 'reg': 93,
 'badge': {'icon': '🚦', 'name': 'Safe Crosser', 'desc': 'Cross the street safely and talk about lights and traffic'},
 'culture': {
  'hook': 'Crossing the street is something you do many times a day. Knowing the signs, the lights and a few safe habits helps you feel calm in any American city.',
  'mythfact': [
   {'s': 'In the USA, cars drive on the right side of the road.', 'ans': True, 'why': 'So many visitors look left first when they step off the curb.'},
   {'s': 'Crossing the street away from a crosswalk can be illegal in many places.', 'ans': True, 'why': 'It is called jaywalking, and in some cities people can get a fine.'},
   {'s': 'A flashing orange hand on a crossing light means “go now”.', 'ans': False, 'why': 'The hand means don’t walk, or don’t start to cross.'},
   {'s': 'Portland is a city in the state of Oregon.', 'ans': True, 'why': 'Many people there ride bikes.'},
   {'s': '“Sesame Street” is a TV show for children that began in 1969.', 'ans': True, 'why': 'It teaches letters, numbers and good habits.'}],
  'wild': [
   {'kind': 'Pedestrian signal', 'lines': ['🚶 **WALK**', '✋ **DON’T WALK**'], 'decode': {'q': 'What does the orange hand mean?', 'opts': ['Do not start to cross', 'Cross fast', 'Buy a ticket'], 'ans': 0, 'why': 'The hand means don’t walk.'}},
   {'kind': 'Sign at the corner', 'lines': ['**Push button to cross**', 'Wait for the signal'], 'decode': {'q': 'What do you do first?', 'opts': ['Push the button', 'Cross', 'Run'], 'ans': 0, 'why': '“Push button to cross.”'}}],
  'compare': {'br': 'In Brazil, cars also drive on the right, but many people cross between cars when the street is slow.', 'us': 'In the USA, people usually wait for the signal and cross at the crosswalk, even when no car is near.', 'tip': 'Wait for the walk sign, then look both ways.', 'ask': 'Do you wait for the green light? Say it in English.'},
  'quiz': [
   {'q': 'The light is red. A friend says…', 'opts': ['Wait! The light is red.', 'Go! The light is red.', 'Red is nice.'], 'ans': 0, 'why': 'Red = stop and wait.'},
   {'q': '“Look both ways!” means…', 'opts': ['Look left and right', 'Look at the sky', 'Look at your phone'], 'ans': 0, 'why': 'Both ways = left and right.'},
   {'q': '“Be careful” means…', 'opts': ['Pay attention', 'Be fast', 'Be loud'], 'ans': 0, 'why': 'Careful = paying attention to stay safe.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'The Red Light',
  'text': [' '.join(p) for p in TXT],
  'glossary': [{'w': 'corner', 'pt': 'esquina'}, {'w': 'light', 'pt': 'sinal / semáforo'}, {'w': 'red', 'pt': 'vermelho'}, {'w': 'green', 'pt': 'verde'}, {'w': 'cross', 'pt': 'atravessar'}, {'w': 'both ways', 'pt': 'os dois lados'}, {'w': 'careful', 'pt': 'cuidadoso'}, {'w': 'crosswalk', 'pt': 'faixa de pedestres'}, {'w': 'habits', 'pt': 'hábitos'}, {'w': 'safe', 'pt': 'seguro'}],
  'fast': {'q': 'What is this story about?', 'opts': ['Crossing the street safely', 'A trip by plane', 'A lunch at school'], 'ans': 0, 'why': 'Carlos tells Uma how to cross safely.'},
  'scan': [{'q': 'What color is the light first?', 'ans': 'red', 'alt': ['Red']}, {'q': 'Which city does Uma live in?', 'ans': 'Portland', 'alt': ['portland']}, {'q': 'What does Carlos say about bikes?', 'ans': 'be careful', 'alt': ['be careful with bikes', 'careful']}],
  'tf': [{'s': 'Uma is late for class.', 'ans': True, 'why': 'She is late this morning.'}, {'s': 'Carlos says to cross when the light is red.', 'ans': False, 'why': 'He says to wait until the light is green.'}, {'s': 'They cross on the crosswalk.', 'ans': True, 'why': 'They walk across on the crosswalk.'}, {'s': 'Uma crosses without looking.', 'ans': False, 'why': 'Carlos says “Look both ways!” and she answers him.'}],
  'order': ['The light is red.', 'Carlos says to wait.', 'The light is green.', 'They look both ways and cross.', 'Uma runs to class.'],
  'ctx': [{'sent': 'When can I cross?', 'w': 'cross', 'opts': ['go to the other side', 'sit down', 'call someone'], 'ans': 0, 'why': 'Cross = go from one side to the other.'}, {'sent': 'Be careful with bikes too.', 'w': 'careful', 'opts': ['paying attention', 'very fast', 'very tired'], 'ans': 0, 'why': 'Careful = paying attention to stay safe.'}, {'sent': 'Safety first.', 'w': 'Safety', 'opts': ['being safe', 'being late', 'being loud'], 'ans': 0, 'why': 'Safety = being safe, without danger.'}],
  'chunkHunt': ['Wait! The light is red.', 'When the light is green.', 'Look both ways!', 'Be careful with bikes.'],
  'think': 'Do you always wait for the green light? What can happen if you do not?'},
 'convo': {'npc': {'name': 'Carlos'}, 'story': 'You are at a corner in Portland. Carlos is a friend and gives you street safety tips.', 'turns': [
  {'npc': 'Wait! The light is red.', 'pt': 'Espere! O sinal está vermelho.', 'opts': [
   {'en': 'Thanks. When can I cross?', 'pt': 'Valeu. Quando posso atravessar?', 'ok': True, 'fb': 'Thank him and ask when.'},
   {'en': 'Thanks. I cross now.', 'pt': 'Valeu. Eu atravesso agora.', 'ok': False, 'fb': 'The light is red, so wait.'},
   {'en': 'Red is a color.', 'pt': 'Vermelho é uma cor.', 'ok': False, 'fb': 'It does not help.'}]},
  {'npc': 'When the light is green.', 'pt': 'Quando o sinal estiver verde.', 'opts': [
   {'en': 'Now it’s green. Let’s go.', 'pt': 'Agora está verde. Vamos.', 'ok': True, 'fb': 'The light changes, and you go.'},
   {'en': 'Now is green. We go.', 'pt': 'Agora é verde. Nós vamos.', 'ok': False, 'fb': 'Say it’s green and Let’s go.'},
   {'en': 'The light is red now.', 'pt': 'O sinal está vermelho agora.', 'ok': False, 'fb': 'It is green now.'}]},
  {'npc': 'Look both ways!', 'pt': 'Olhe para os dois lados!', 'opts': [
   {'en': 'Look at my shoes!', 'pt': 'Olhe para meus sapatos!', 'ok': False, 'fb': 'It does not fit.'},
   {'en': 'Good point. Cars are coming.', 'pt': 'Boa. Estão vindo carros.', 'ok': True, 'fb': 'A natural answer.'},
   {'en': 'Both ways is good.', 'pt': 'Os dois lados é bom.', 'ok': False, 'fb': 'Say Good point.'}]},
  {'npc': 'Be careful with bikes too.', 'pt': 'Cuidado com as bicicletas também.', 'opts': [
   {'en': 'Thanks, I will.', 'pt': 'Valeu, vou ter cuidado.', 'ok': True, 'fb': 'I will = I will be careful.'},
   {'en': 'I am a bike.', 'pt': 'Eu sou uma bicicleta.', 'ok': False, 'fb': 'It does not fit.'},
   {'en': 'Thanks, I do.', 'pt': 'Valeu, eu faço.', 'ok': False, 'fb': 'Use I will for a promise.'}]},
  {'npc': 'Have a safe walk!', 'pt': 'Boa caminhada!', 'opts': [
   {'en': 'Thanks! You too!', 'pt': 'Valeu! Você também!', 'ok': True, 'fb': 'A friendly end.'},
   {'en': 'The light is red.', 'pt': 'O sinal está vermelho.', 'ok': False, 'fb': 'It does not fit.'},
   {'en': 'Look both ways!', 'pt': 'Olhe para os dois lados!', 'ok': False, 'fb': 'It was Carlos’s sentence.'}]}]},
 'errors': [
  {'wrong': 'The light is in red.', 'fix': 'The light is red.', 'alt': 'The light has red.', 'why': 'A color after is has no preposition.'},
  {'wrong': 'When I can cross?', 'fix': 'When can I cross?', 'alt': 'When I cross can?', 'why': 'In questions, the helper verb goes first: When can I…?'},
  {'wrong': 'Look the two sides.', 'fix': 'Look both ways.', 'alt': 'Look in both ways.', 'why': 'The usual phrase is both ways.'},
  {'wrong': 'Be careful of the bikes.', 'fix': 'Be careful with bikes.', 'alt': 'Be careful at bikes.', 'why': 'The natural phrase is careful with.'}],
 'homework': 'Write 4 safe habits for crossing the street, and say each one out loud.',
 'homework_items': ['Write: First, stop. Next, look. Then, listen. Finally, cross.', 'Record yourself saying 3 street safety tips.', 'Listen to the dialogue again and shadow Carlos.', 'Review: When the light is green. / Look both ways!']}
