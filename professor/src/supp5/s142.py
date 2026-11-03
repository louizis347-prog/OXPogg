"""Suplemento Quest v5 · aula 142: Traffic in L.A. + regular How Far Is the Station? (The Bremen Town Musicians)."""
SUPP = {
 'reg': 143,
 'badge': {'icon': '🚦', 'name': 'Freeway Survivor', 'desc': 'Ask how long a trip takes and choose another road'},
 'culture': {
  'hook': 'Los Angeles is a huge city with many freeways, and most people drive. A trip of thirty minutes can become two hours, so people always ask about traffic before they leave.',
  'mythfact': [
   {'s': 'Many people in Los Angeles drive to work.', 'ans': True, 'why': 'The city is very wide, and most people use a car.'},
   {'s': 'Traffic in L.A. is the same at every hour.', 'ans': False, 'why': 'Rush hour in the morning and late afternoon is usually the worst time.'},
   {'s': 'In Los Angeles, people often say “the 405” for a freeway.', 'ans': True, 'why': 'Californians put “the” before the freeway number.'},
   {'s': 'A phone app can help you find a faster road.', 'ans': True, 'why': 'Many apps show traffic and offer another way.'},
   {'s': 'You cannot get to a beach from L.A. by car.', 'ans': False, 'why': 'Beaches like Santa Monica are close to the city, and many people drive there.'}],
  'wild': [
   {'kind': 'Freeway sign', 'lines': ['**Traffic ahead**', 'Accident: right lane closed', 'Expect delays'], 'decode': {'q': 'What is the problem?', 'opts': ['An accident closes one lane', 'The beach is closed', 'The bus is free'], 'ans': 0, 'why': 'The sign says an accident closes the right lane.'}},
   {'kind': 'App message', 'lines': ['**Faster route found**', 'Save 20 min', 'Exit at Main St.'], 'decode': {'q': 'What does the app say?', 'opts': ['Take another road and save time', 'Stay on the freeway', 'Stop and wait'], 'ans': 0, 'why': 'A faster route saves 20 minutes.'}}],
  'compare': {'br': 'In São Paulo and Rio, people also face heavy traffic, but many use buses, the subway or trains.', 'us': 'In Los Angeles, a car is very common, and a short trip can take a long time at rush hour.', 'tip': 'Ask: “How long with traffic?”', 'ask': 'How do you go to work or school? Say it in English.'},
  'quiz': [
   {'q': 'You want to know the time to the beach. You ask…', 'opts': ['How long to the beach?', 'How much long beach?', 'Long time the beach how?'], 'ans': 0, 'why': 'How long to + place asks the time of a trip.'},
   {'q': '“Without traffic, thirty minutes.” It means…', 'opts': ['If the roads are empty, it takes 30 minutes', 'There is no beach', 'The trip is always 30 minutes'], 'ans': 0, 'why': 'Without traffic = if there are no cars on the road.'},
   {'q': 'What is a freeway?', 'opts': ['a big road for fast cars', 'a free bus ticket', 'a park for walking'], 'ans': 0, 'why': 'A freeway is a wide road with no stoplights.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Two hours to the sea',
  'text': [
   'Lena is on vacation in **Los Angeles**. Her friend Marco lives here. This morning they want to go to the beach. Marco has a small blue car and a phone full of maps.',
   '“**Are you ready to go?**” Marco asks. “**Yes. How long to the beach?**” Lena asks. “**Without traffic, thirty minutes**,” Marco says. “**And with traffic?**” “**Maybe two hours!**” Lena opens her eyes wide. “**Wow. Is it always like this?**”',
   '“**Almost always, on the freeway**,” Marco says. “There are six lanes, but they are all full. Today there is an accident near the exit.” Lena sees red lights, white lights and many cars. Nobody moves.',
   'Lena thinks about “The Bremen Town Musicians.” In the old story, a donkey, a dog, a cat and a rooster walk to the city of Bremen, but they never arrive. “I do not want to be a musician on the road,” she laughs. “I want to see the ocean!”',
   '“**Should we take the side streets?**” she asks. “**Good idea. Let me check the app**,” Marco says. He finds a shortcut. They turn left, then right. The streets are small and quiet, and soon Lena sees the blue sea.'],
  'glossary': [{'w': 'freeway', 'pt': 'rodovia urbana'}, {'w': 'traffic', 'pt': 'trânsito'}, {'w': 'accident', 'pt': 'acidente'}, {'w': 'exit', 'pt': 'saída (da rodovia)'}, {'w': 'lanes', 'pt': 'faixas'}, {'w': 'shortcut', 'pt': 'atalho'}, {'w': 'side streets', 'pt': 'ruas laterais'}, {'w': 'rooster', 'pt': 'galo'}, {'w': 'ocean', 'pt': 'oceano'}],
  'fast': {'q': 'What is this story about?', 'opts': ['Two friends try to reach the beach', 'A woman cooks dinner', 'A man loses his phone'], 'ans': 0, 'why': 'Lena and Marco face traffic on the way to the beach.'},
  'scan': [{'q': 'How long is the trip without traffic?', 'ans': 'thirty minutes', 'alt': ['30 minutes', 'thirty']}, {'q': 'Where is the accident?', 'ans': 'near the exit', 'alt': ['exit', 'on the freeway']}, {'q': 'What does Marco check?', 'ans': 'the app', 'alt': ['app', 'his phone']}],
  'tf': [{'s': 'Marco says the trip can take two hours.', 'ans': True, 'why': '“Maybe two hours!”'}, {'s': 'There is no traffic today.', 'ans': False, 'why': 'There is an accident and many cars.'}, {'s': 'Marco and Lena take the side streets.', 'ans': True, 'why': 'Marco finds a shortcut.'}, {'s': 'Lena lives in Los Angeles.', 'ans': False, 'why': 'She is on vacation. Marco lives there.'}],
  'order': ['Marco asks if Lena is ready.', 'Lena asks how long it takes.', 'They see the accident and red lights.', 'Marco checks the app.', 'They take the side streets.'],
  'ctx': [{'sent': 'There is an accident near the exit.', 'w': 'exit', 'opts': ['a way off the freeway', 'a car key', 'a beach chair'], 'ans': 0, 'why': 'An exit is where you leave the freeway.'}, {'sent': 'Marco finds a shortcut.', 'w': 'shortcut', 'opts': ['a faster, shorter way', 'a very old map', 'a red light'], 'ans': 0, 'why': 'A shortcut saves time.'}, {'sent': 'The freeway has six lanes.', 'w': 'lanes', 'opts': ['strips of road for cars', 'big trucks', 'road signs'], 'ans': 0, 'why': 'Cars drive in lanes.'}],
  'chunkHunt': ['How long to the beach?', 'Without traffic, thirty minutes.', 'Is it always like this?', 'Let me check the app.'],
  'think': 'How do you go to work or school? Is it fast or slow?'},
 'convo': {'npc': {'name': 'Marco'}, 'story': 'You are in Los Angeles with your friend Marco. You want to go to the beach.', 'turns': [
  {'npc': 'Are you ready to go?', 'pt': 'Você está pronto para ir?', 'opts': [
   {'en': 'Yes. How long to the beach?', 'pt': 'Sim. Quanto tempo até a praia?', 'ok': True, 'fb': 'Natural question about time.'},
   {'en': 'Yes. How much time the beach?', 'pt': 'Sim. Quanto tempo a praia?', 'ok': False, 'fb': 'Say: How long to the beach?'},
   {'en': 'Yes, I am a beach.', 'pt': 'Sim, eu sou uma praia.', 'ok': False, 'fb': 'Wrong meaning.'}]},
  {'npc': 'Without traffic, thirty minutes.', 'pt': 'Sem trânsito, trinta minutos.', 'opts': [
   {'en': 'And with traffic?', 'pt': 'E com trânsito?', 'ok': True, 'fb': 'Good follow-up.'},
   {'en': 'And with the traffic?', 'pt': 'E com o trânsito?', 'ok': False, 'fb': 'Say with traffic, with no the.'},
   {'en': 'And without traffic?', 'pt': 'E sem trânsito?', 'ok': False, 'fb': 'He just said that.'}]},
  {'npc': 'Maybe two hours!', 'pt': 'Talvez duas horas!', 'opts': [
   {'en': 'Wow. It is always like this?', 'pt': 'Uau. É sempre assim?', 'ok': False, 'fb': 'Question order: Is it always like this?'},
   {'en': 'Wow. Is it always like this?', 'pt': 'Uau. Sempre é assim?', 'ok': True, 'fb': 'Correct question.'},
   {'en': 'Wow. Two hours is a beach.', 'pt': 'Uau. Duas horas é uma praia.', 'ok': False, 'fb': 'It does not make sense.'}]},
  {'npc': 'Almost always, on the freeway.', 'pt': 'Quase sempre, na rodovia.', 'opts': [
   {'en': 'Should we take the side streets?', 'pt': 'Devemos pegar as ruas laterais?', 'ok': True, 'fb': 'Good idea.'},
   {'en': 'Should we to take the side streets?', 'pt': 'Devemos pegar as ruas laterais?', 'ok': False, 'fb': 'After should, use the base verb: take.'},
   {'en': 'We should the freeway take?', 'pt': 'Devemos a rodovia pegar?', 'ok': False, 'fb': 'Wrong word order.'}]},
  {'npc': 'Good idea. Let me check the app.', 'pt': 'Boa ideia. Vou ver o aplicativo.', 'opts': [
   {'en': 'Thanks. I check you.', 'pt': 'Obrigado. Eu confiro você.', 'ok': False, 'fb': 'Wrong meaning.'},
   {'en': 'Okay. Is a good app?', 'pt': 'Certo. É um bom aplicativo?', 'ok': False, 'fb': 'Say: Is it a good app?'},
   {'en': 'Great. Thanks, Marco!', 'pt': 'Ótimo. Obrigado, Marco!', 'ok': True, 'fb': 'Polite and natural.'}]}]},
 'errors': [
  {'wrong': 'How much time to the beach?', 'fix': 'How long to the beach?', 'alt': 'How many time to the beach?', 'why': 'For the length of a trip, say How long.'},
  {'wrong': 'With the traffic, two hours.', 'fix': 'With traffic, two hours.', 'alt': 'With a traffic, two hours.', 'why': 'Traffic has no the or a here.'},
  {'wrong': 'Always is like this?', 'fix': 'Is it always like this?', 'alt': 'It is always like this?', 'why': 'In a question, put Is first: Is it always…?'},
  {'wrong': 'We should to take side streets.', 'fix': 'We should take the side streets.', 'alt': 'We should taking the side streets.', 'why': 'After should, use the base verb without to.'}],
 'homework': 'Write a short dialogue: you ask how long a trip takes with traffic and without traffic.',
 'homework_items': ['Write 3 sentences about traffic in your city.', 'Say aloud: How long to the beach?', 'Listen to the dialogue and shadow Marco.', 'Review: with traffic / without traffic.']}
