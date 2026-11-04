"""Suplemento Quest v5 · aula 199: I'm late! + regular What happened next? (The Three Billy Goats Gruff)."""
SUPP = {
 'reg': 205,
 'badge': {'icon': '⏰', 'name': 'Just On Time', 'desc': 'Explain why you are late and get ready fast'},
 'culture': {
  'hook': 'In the USA, being on time matters at school and at work. If you are late, a short, honest sentence and a quick “Sorry!” usually work better than a long story.',
  'mythfact': [
   {'s': 'In the USA, many people say “I’m late!” when they are in a hurry.', 'ans': True, 'why': 'It is a very common short sentence.'},
   {'s': 'Most phones have an alarm you can set for a time.', 'ans': True, 'why': 'Many people set more than one alarm.'},
   {'s': 'You say “I overslept” when you wake up early.', 'ans': False, 'why': 'Oversleep means to sleep longer than you planned.'},
   {'s': 'In “The Three Billy Goats Gruff,” the goats cross a bridge.', 'ans': True, 'why': 'A troll lives under the bridge.'},
   {'s': 'It is rude to say “Sorry, I’m late” when you arrive.', 'ans': False, 'why': 'It is polite to say it.'}],
  'wild': [
   {'kind': 'Phone alarm', 'lines': ['**Alarm 6:00 · Mon–Fri**', 'Alarm 7:00 · Weekend', 'Snooze: 10 min'], 'decode': {'q': 'When does the alarm ring on weekdays?', 'opts': ['At 6:00', 'At 7:00', 'At 10:00'], 'ans': 0, 'why': 'The first line says 6:00 Monday to Friday.'}},
   {'kind': 'Text message', 'lines': ['Sorry, **I’m running late**!', 'Class starts at 8.', 'See you in 15 minutes.'], 'decode': {'q': 'What is the problem?', 'opts': ['The person will be late', 'Class is over', 'The class is cancelled'], 'ans': 0, 'why': '“I’m running late” means the person will be late.'}}],
  'compare': {'br': 'In Brazil, many people say “Estou atrasado!” and often send a message like “Já estou chegando”.', 'us': 'In the USA, people also text “I’m running late” and give a time, like “See you in 15 minutes.”', 'tip': 'Say: “Sorry, I’m late. My alarm didn’t ring.”', 'ask': 'What do you say when you are late? Say it in English.'},
  'quiz': [
   {'q': 'You are in a hurry. You say…', 'opts': ['I’m so late!', 'I have late!', 'I am lately!'], 'ans': 0, 'why': 'Be + late: I’m so late.'},
   {'q': 'Your alarm did not work. You say…', 'opts': ['My alarm didn’t ring.', 'My alarm no rings.', 'My alarm not ring.'], 'ans': 0, 'why': 'Past negative: didn’t + base verb.'},
   {'q': 'You ask about the class time. You say…', 'opts': ['When does your class start?', 'When your class starts?', 'When do your class start?'], 'ans': 0, 'why': 'With class (it) use does + start.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Seven thirty!',
  'text': [
   'Tom reads late last night. He reads a story about three goats and a troll under a bridge. Then he sleeps like a rock. In the morning, the sun is bright, and his roommate Cole opens the door.',
   '“**Wake up! It’s seven thirty!**” “**What? My alarm didn’t ring.**” “**Did you set it for six?**” “**No, I set it for seven.**” “**Then it rang an hour ago!**” Tom looks at his phone. He sees a long list of alarms.',
   '“**Oh no, I’m so late.**” “**When does your class start?**” “**At eight o’clock.**” “**Take a quick shower.**” Tom jumps up. He takes a quick shower, brushes his teeth and grabs a banana. Then he cannot find his keys. They are under the sofa.',
   'Tom runs to the bus stop. The bus comes just in time. On the bus, he thinks about the goat story. In the end, the big goat wins, and all the goats eat grass on the hill. Tom hopes his day ends well, too. He walks into class at 7:59, and he is out of breath. The teacher smiles. “Good morning, Tom. You are on time!”'],
  'glossary': [{'w': 'goat', 'pt': 'cabra'}, {'w': 'troll', 'pt': 'troll'}, {'w': 'bridge', 'pt': 'ponte'}, {'w': 'roommate', 'pt': 'colega de quarto'}, {'w': 'alarm', 'pt': 'alarme'}, {'w': 'quick', 'pt': 'rápido'}, {'w': 'shower', 'pt': 'banho'}, {'w': 'keys', 'pt': 'chaves'}, {'w': 'on time', 'pt': 'na hora'}, {'w': 'hill', 'pt': 'colina'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A student wakes up late and hurries to class', 'A student plays a game', 'A man travels by bus'], 'ans': 0, 'why': 'Tom oversleeps and rushes to class.'},
  'scan': [{'q': 'What time does Cole wake Tom?', 'ans': 'seven thirty', 'alt': ['7:30', 'half past seven']}, {'q': 'What does Tom grab?', 'ans': 'a banana', 'alt': ['banana']}, {'q': 'Where are the keys?', 'ans': 'under the sofa', 'alt': ['under the couch']}],
  'tf': [{'s': 'Tom set his alarm for six.', 'ans': False, 'why': 'He set it for seven.'}, {'s': 'Tom’s class starts at eight.', 'ans': True, 'why': 'He says, “At eight o’clock.”'}, {'s': 'Tom takes a long shower.', 'ans': False, 'why': 'He takes a quick shower.'}, {'s': 'Tom is on time for class.', 'ans': True, 'why': 'He arrives at 7:59.'}],
  'order': ['Cole wakes Tom up.', 'Tom learns his alarm rang before.', 'Tom takes a quick shower.', 'Tom finds his keys.', 'Tom gets to class on time.'],
  'ctx': [{'sent': 'Take a quick shower.', 'w': 'quick', 'opts': ['fast', 'long', 'cold'], 'ans': 0, 'why': 'Quick means fast.'}, {'sent': 'Tom opens his phone and sees an alarm.', 'w': 'alarm', 'opts': ['a sound at a set time', 'a kind of food', 'a key'], 'ans': 0, 'why': 'An alarm rings at a set time.'}, {'sent': 'The bus comes just in time.', 'w': 'in time', 'opts': ['not late', 'very late', 'too early'], 'ans': 0, 'why': 'Just in time means not late.'}],
  'chunkHunt': ['Wake up!', 'My alarm didn’t ring.', 'I’m so late.', 'Take a quick shower.'],
  'think': 'What do you do when you wake up late? What is the first thing you do?'},
 'convo': {'npc': {'name': 'Cole'}, 'story': 'You live with Cole. You wake up late, and Cole helps you get ready for class.', 'turns': [
  {'npc': 'Wake up! It’s seven thirty!', 'pt': 'Acorde! São sete e meia!', 'opts': [
   {'en': 'What? My alarm didn’t ring.', 'pt': 'O quê? Meu alarme não tocou.', 'ok': True, 'fb': 'Natural past negative.'},
   {'en': 'What? My alarm no ring.', 'pt': 'O quê? Meu alarme não toca.', 'ok': False, 'fb': 'Use didn’t + base verb.'},
   {'en': 'Good night, Cole.', 'pt': 'Boa noite, Cole.', 'ok': False, 'fb': 'It is morning.'}]},
  {'npc': 'Did you set it for six?', 'pt': 'Você programou para as seis?', 'opts': [
   {'en': 'No, I set it for seven.', 'pt': 'Não, programei para as sete.', 'ok': True, 'fb': 'Clear answer, with set in the past.'},
   {'en': 'No, I setted it for seven.', 'pt': 'Não, eu programei para as sete.', 'ok': False, 'fb': 'Set does not change: I set it.'},
   {'en': 'Yes, it is seven.', 'pt': 'Sim, são sete.', 'ok': False, 'fb': 'Does not answer the question.'}]},
  {'npc': 'Then it rang an hour ago!', 'pt': 'Então tocou uma hora atrás!', 'opts': [
   {'en': 'Oh no, I’m so late.', 'pt': 'Ai, não, estou tão atrasado.', 'ok': True, 'fb': 'Short and natural.'},
   {'en': 'Oh no, I have late.', 'pt': 'Ai, não, eu tenho atrasado.', 'ok': False, 'fb': 'Use am + late.'},
   {'en': 'Thank you very much.', 'pt': 'Muito obrigado.', 'ok': False, 'fb': 'This is not good news.'}]},
  {'npc': 'When does your class start?', 'pt': 'Quando começa sua aula?', 'opts': [
   {'en': 'At eight o’clock.', 'pt': 'Às oito horas.', 'ok': True, 'fb': 'Answers the time.'},
   {'en': 'In eight o’clock.', 'pt': 'Em oito horas.', 'ok': False, 'fb': 'Use at for the time.'},
   {'en': 'I am late in class.', 'pt': 'Estou atrasado na aula.', 'ok': False, 'fb': 'Does not answer when it starts.'}]},
  {'npc': 'Take a quick shower.', 'pt': 'Tome um banho rápido.', 'opts': [
   {'en': 'Good idea. Where are my keys?', 'pt': 'Boa ideia. Cadê minhas chaves?', 'ok': True, 'fb': 'Agrees and asks for the next thing.'},
   {'en': 'I take a shower fast, no.', 'pt': 'Eu tomo banho rápido, não.', 'ok': False, 'fb': 'Does not sound natural.'},
   {'en': 'The shower is my keys.', 'pt': 'O banho é minhas chaves.', 'ok': False, 'fb': 'Does not make sense.'}]}]},
 'errors': [
  {'wrong': 'I have late.', 'fix': 'I’m late.', 'alt': 'I am lately.', 'why': 'Use am + late. Lately has another meaning.'},
  {'wrong': 'My alarm no ringed.', 'fix': 'My alarm didn’t ring.', 'alt': 'My alarm didn’t rang.', 'why': 'After didn’t, use the base verb: ring.'},
  {'wrong': 'I setted it for seven.', 'fix': 'I set it for seven.', 'alt': 'I sat it for seven.', 'why': 'Set is the same in the past: set, set.'},
  {'wrong': 'The class starts in eight o’clock.', 'fix': 'The class starts at eight o’clock.', 'alt': 'The class start at eight.', 'why': 'Use at for a clock time, and starts for it.'}],
 'homework': 'Write a short dialogue: you wake up late, tell your roommate why and get ready fast.',
 'homework_items': ['Write three things you do fast in the morning.', 'Say aloud: I’m so late.', 'Listen to the dialogue and shadow Cole.', 'Review: shower / sleep / quick / rush.']}
