"""Suplemento Quest v5 · aula 45: Taking the subway + regular Past the railway (The Little Engine That Could)."""
SUPP = {
 'reg': 145,
 'badge': {'icon': '🚇', 'name': 'Subway Rider', 'desc': 'Ask about trains, platforms and stops in English'},
 'sticker': {'cat': 'Everyday culture', 'title': 'Riding the New York Subway', 'sub': 'Local, express and your stop'},
 'culture': {
  'hook': 'The New York subway is one of the busiest in the world and many people use it every day. Learn a few words and you can travel across the city like a local.',
  'polite': 'Say **“Excuse me”** before you pass someone, and let people get off the train first.',
  'mythfact': [
   {'s': 'The New York City subway runs 24 hours a day.', 'ans': True, 'why': 'It is one of the few big subway systems that does not close at night.'},
   {'s': 'All trains stop at every station.', 'ans': False, 'why': 'Express trains skip stations, and local trains stop at every one.'},
   {'s': '“Uptown” means going toward the north part of Manhattan.', 'ans': True, 'why': 'Uptown = north, downtown = south in Manhattan.'},
   {'s': 'You must always talk loudly to a stranger on the train.', 'ans': False, 'why': 'Most people are quiet, and it is normal to keep to yourself.'}],
  'wild': [
   {'kind': 'Train announcement', 'lines': ['**This is a Brooklyn-bound 2 train.**', 'The next stop is Atlantic Avenue.', 'Stand clear of the closing doors, please.'], 'decode': {'q': 'Where is the train going?', 'opts': ['To Brooklyn', 'To the airport', 'To a park'], 'ans': 0, 'why': '“Brooklyn-bound” means going to Brooklyn.'}},
   {'kind': 'Platform sign', 'lines': ['**2 · 3 · Brooklyn →**', 'Stairs down to the platform', 'Local trains only'], 'decode': {'q': 'What kind of trains stop here?', 'opts': ['Local trains', 'Express trains', 'Taxis'], 'ans': 0, 'why': '“Local trains only.”'}}],
  'compare': {'br': 'In Brazil many people take the metrô, the trem or the ônibus, and each city has its own card or app.', 'us': 'In New York people take the subway almost everywhere, and trains have numbers or letters.', 'tip': 'Check the train number and the direction before you go down the stairs.', 'ask': 'How do you go to work or school? Say it in English.'},
  'quiz': [
   {'q': 'You want to know which train goes to Brooklyn. You say…', 'opts': ['Which train goes to Brooklyn?', 'Where Brooklyn train is?', 'I want Brooklyn train now.'], 'ans': 0, 'why': 'Which train goes to… is a clear question.'},
   {'q': 'A local train…', 'opts': ['stops at every station', 'skips many stations', 'does not stop'], 'ans': 0, 'why': 'Local = every stop.'},
   {'q': '“Get off at Atlantic Avenue” means…', 'opts': ['Leave the train there', 'Get on the train there', 'Sleep there'], 'ans': 0, 'why': 'Get off = leave the train.'}]},
 'reading': {
  'genre': 'Blog post', 'title': 'My first subway ride in New York',
  'text': [
   'Yesterday I took the subway in New York for the first time. I was very nervous. The station was big, loud and full of people. I wanted to go to Brooklyn, but I did not know which train to take.',
   'I saw a man with a map and said, “**Excuse me, which train goes to Brooklyn?**” “**Take the number two train**,” he said. “Where is the platform?” I asked. “**Go down the stairs. It’s on the left**,” he answered.',
   'I went down the stairs and found the platform. A train came with a loud noise. I asked a woman, “**How many stops?**” She said, “**Four stops. Get off at Atlantic Avenue**.” I thanked her and got on the train.',
   'The train was a local, so it stopped at every station. It was slow, but I did not mind. I counted the stops: one, two, three, four. A voice said, “The next stop is Atlantic Avenue.”',
   'I got off, went up the stairs and walked into the sun. A smiling man at the exit said, “**Have a good trip!**” It was a small moment, but I felt very happy.',
   'Now I know that the subway is not scary. You can always ask for help, and most people are kind.'],
  'glossary': [{'w': 'nervous', 'pt': 'nervoso'}, {'w': 'station', 'pt': 'estação'}, {'w': 'platform', 'pt': 'plataforma'}, {'w': 'stairs', 'pt': 'escada'}, {'w': 'stops', 'pt': 'paradas'}, {'w': 'local', 'pt': 'local'}, {'w': 'slow', 'pt': 'lento'}, {'w': 'exit', 'pt': 'saída'}, {'w': 'scary', 'pt': 'assustador'}],
  'fast': {'q': 'What is this text about?', 'opts': ['A first subway ride in New York', 'A bus trip in Brazil', 'A boat tour'], 'ans': 0, 'why': 'The writer takes the subway for the first time.'},
  'scan': [{'q': 'Which train does the writer take?', 'ans': 'number two', 'alt': ['the 2', '2', 'the number two train']}, {'q': 'How many stops?', 'ans': 'four', 'alt': ['4']}, {'q': 'Where does the writer get off?', 'ans': 'Atlantic Avenue', 'alt': ['atlantic avenue']}],
  'tf': [{'s': 'The writer feels nervous at the start.', 'ans': True, 'why': '“I was very nervous.”'}, {'s': 'The platform is on the right.', 'ans': False, 'why': 'It is on the left.'}, {'s': 'The train is local.', 'ans': True, 'why': 'It stops at every station.'}, {'s': 'The writer never asks for help.', 'ans': False, 'why': 'He asks a man and a woman.'}],
  'order': ['The writer asks which train goes to Brooklyn.', 'He goes down the stairs to the platform.', 'He asks how many stops.', 'The train stops four times.', 'He gets off at Atlantic Avenue.'],
  'ctx': [{'sent': 'The station was big, loud and full of people.', 'w': 'loud', 'opts': ['with a lot of noise', 'very quiet', 'very clean'], 'ans': 0, 'why': 'Loud = noisy.'}, {'sent': 'It was slow, but I did not mind.', 'w': 'did not mind', 'opts': ['was not bothered', 'was angry', 'was lost'], 'ans': 0, 'why': 'Not mind = it was OK.'}, {'sent': 'A smiling man at the exit said hello.', 'w': 'exit', 'opts': ['the way out', 'the way in', 'a ticket'], 'ans': 0, 'why': 'Exit = way out.'}],
  'chunkHunt': ['Which train goes to…?', 'Take the number two train.', 'Where is the platform?', 'How many stops?', 'Get off at…'],
  'think': 'Is public transport easy where you live? What do you say to ask for help?'},
 'convo': {'npc': {'name': 'Ravi'}, 'story': 'You are in a New York subway station. Ravi is a traveler. Help him get to Brooklyn.', 'turns': [
  {'npc': 'Excuse me, which train goes to Brooklyn?', 'pt': 'Com licença, qual trem vai ao Brooklyn?', 'opts': [
   {'en': 'Take the number two train.', 'pt': 'Pegue o trem número dois.', 'ok': True, 'fb': 'Clear and short.'},
   {'en': 'The train go to Brooklyn.', 'pt': 'O trem vai ao Brooklyn.', 'ok': False, 'fb': 'The train goes (with s).'},
   {'en': 'I am from Brooklyn.', 'pt': 'Eu sou do Brooklyn.', 'ok': False, 'fb': 'Not an answer.'}]},
  {'npc': 'Where is the platform?', 'pt': 'Onde fica a plataforma?', 'opts': [
   {'en': 'Platform is in down.', 'pt': 'Plataforma é em baixo.', 'ok': False, 'fb': 'Say go down the stairs.'},
   {'en': 'Go down the stairs. It’s on the left.', 'pt': 'Desça a escada. Fica à esquerda.', 'ok': True, 'fb': 'Direction + side.'},
   {'en': 'I like stairs.', 'pt': 'Eu gosto de escadas.', 'ok': False, 'fb': 'Out of context.'}]},
  {'npc': 'How many stops?', 'pt': 'Quantas paradas?', 'opts': [
   {'en': 'Four stops. Get off at Atlantic Avenue.', 'pt': 'Quatro paradas. Desça na Atlantic Avenue.', 'ok': True, 'fb': 'Number + where to get off.'},
   {'en': 'It is four hours.', 'pt': 'São quatro horas.', 'ok': False, 'fb': 'Stops are not hours.'},
   {'en': 'Four stop.', 'pt': 'Quatro parada.', 'ok': False, 'fb': 'Plural: four stops.'}]},
  {'npc': 'Is it express?', 'pt': 'É expresso?', 'opts': [
   {'en': 'No, I am not express.', 'pt': 'Não, eu não sou expresso.', 'ok': False, 'fb': 'The train is express, not you.'},
   {'en': 'Yes, it stops never.', 'pt': 'Sim, ele para nunca.', 'ok': False, 'fb': 'Wrong word order, and it is a local train.'},
   {'en': 'No, it’s local. It’s slow.', 'pt': 'Não, é local. É lento.', 'ok': True, 'fb': 'Short and natural.'}]},
  {'npc': 'Have a good trip!', 'pt': 'Boa viagem!', 'opts': [
   {'en': 'Thanks! You too.', 'pt': 'Obrigado! Você também.', 'ok': True, 'fb': 'A friendly reply.'},
   {'en': 'I have a good.', 'pt': 'Eu tenho um bom.', 'ok': False, 'fb': 'Not natural.'},
   {'en': 'Welcome.', 'pt': 'Bem-vindo.', 'ok': False, 'fb': 'Not the right reply.'}]}]},
 'errors': [
  {'wrong': 'Which train go to Brooklyn?', 'fix': 'Which train goes to Brooklyn?', 'alt': 'Which train does go to Brooklyn?', 'why': 'He/she/it verbs take -s: goes.'},
  {'wrong': 'I go down in the stairs.', 'fix': 'I go down the stairs.', 'alt': 'I go down of the stairs.', 'why': 'No in after down.'},
  {'wrong': 'Four stop.', 'fix': 'Four stops.', 'alt': 'Four stoppes.', 'why': 'After a number use plural: stops.'},
  {'wrong': 'I descend in Atlantic Avenue.', 'fix': 'I get off at Atlantic Avenue.', 'alt': 'I get out in Atlantic Avenue.', 'why': 'Use get off + at a stop.'}],
 'homework': 'Describe your usual trip to school or work in English: which transport, where you get on and where you get off.',
 'homework_items': ['Write 4 sentences about your trip.', 'Record: “Get off at …”.', 'Make a list: bus, train, subway, taxi.', 'Review: Which train goes to…? / How many stops?']}
