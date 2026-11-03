"""Suplemento Quest v5 · aula 46: The bus stop + regular The next stop is… (The Wheels on the Bus)."""
SUPP = {
 'reg': 148,
 'badge': {'icon': '🚌', 'name': 'Bus Buddy', 'desc': 'Ask about fares, stops and time on a bus in English'},
 'sticker': {'cat': 'Everyday culture', 'title': 'Taking the Bus in the USA', 'sub': 'Fare, card and stop button'},
 'culture': {
  'hook': 'City buses in the USA can be a cheap way to travel, but each city has its own rules. Knowing how to ask a few questions makes your first ride easy.',
  'polite': 'Say **“Thank you”** to the driver when you get off. Many riders do it.',
  'mythfact': [
   {'s': 'In many US cities, bus drivers do not give change if you pay in cash.', 'ans': True, 'why': 'Many systems ask for exact fare, so keep coins or use a card.'},
   {'s': 'School buses in the USA are yellow.', 'ans': True, 'why': 'The yellow color is very well known.'},
   {'s': 'You shout the name of your stop to the driver.', 'ans': False, 'why': 'You press the stop button or pull the cord.'},
   {'s': 'Every American bus is free.', 'ans': False, 'why': 'Most city buses charge a fare, though some cities offer free routes.'}],
  'wild': [
   {'kind': 'Bus stop sign', 'lines': ['**Route 12 · Downtown**', 'Every 15 minutes', 'Fare: $2.50 · Exact change or card'], 'decode': {'q': 'How often does the bus come?', 'opts': ['Every 15 minutes', 'Every hour', 'Every 2 minutes'], 'ans': 0, 'why': '“Every 15 minutes.”'}},
   {'kind': 'On-bus sign', 'lines': ['**Please offer your seat**', 'to people who need it.', 'Press the button to request a stop.'], 'decode': {'q': 'How do you ask the bus to stop?', 'opts': ['Press the button', 'Shout', 'Open the door'], 'ans': 0, 'why': '“Press the button to request a stop.”'}}],
  'compare': {'br': 'In Brazil many people pay a cobrador or use a card at the turnstile, and buses can get very full.', 'us': 'In the USA you usually pay the driver at the front or tap a card, and you press the button to get off.', 'tip': 'Keep your card or small bills ready before the bus arrives.', 'ask': 'How do you pay for the bus in your city? Say it in English.'},
  'quiz': [
   {'q': 'You want to know the price. You say…', 'opts': ['How much is the fare?', 'How is the bus money?', 'Fare is how?'], 'ans': 0, 'why': 'Fare = the price of the ride.'},
   {'q': 'Does this bus go downtown?', 'opts': ['A question to the driver', 'A bus brand', 'A kind of ticket'], 'ans': 0, 'why': 'It asks if the bus goes to the center.'},
   {'q': 'How do you ask the bus to stop?', 'opts': ['Press the stop button', 'Call the driver’s name', 'Stand at the door'], 'ans': 0, 'why': 'The button tells the driver.'}]},
 'reading': {
  'genre': 'Diary entry', 'title': 'Waiting for the bus in Washington',
  'text': [
   'This morning I waited at a bus stop in Washington. A man named Ethan was next to me. He looked at the sign, then he looked at me. “**Excuse me, does this bus go downtown?**” he asked.',
   '“**Yes, it goes downtown**,” I said. “**How much is the fare?**” he asked. “**Two dollars and fifty cents**,” I answered. “**Do I pay the driver?**” “**Yes, or use a card**.”',
   'Then the bus came. It was blue and white, and it was almost empty. We got on, and Ethan put the money in the machine. “**How long does it take?**” he asked. “**About twenty minutes**,” I said.',
   'We sat near a window. The city moved past us: buildings, trees, people with coffee. I like buses because I can look outside and think. Ethan took a small notebook and wrote the name of each street.',
   'When we came near downtown, I pressed the stop button. A red light said “Stop requested.” Ethan stood up and said, “**Enjoy your trip!**” I smiled and said, “You too!”',
   'I thanked the driver and got off. A simple talk at a bus stop made my morning better.'],
  'glossary': [{'w': 'bus stop', 'pt': 'ponto de ônibus'}, {'w': 'sign', 'pt': 'placa'}, {'w': 'fare', 'pt': 'passagem'}, {'w': 'driver', 'pt': 'motorista'}, {'w': 'empty', 'pt': 'vazio'}, {'w': 'machine', 'pt': 'máquina'}, {'w': 'window', 'pt': 'janela'}, {'w': 'button', 'pt': 'botão'}, {'w': 'notebook', 'pt': 'caderno'}],
  'fast': {'q': 'What is this text about?', 'opts': ['A short talk and a bus ride downtown', 'A shopping day', 'A soccer game'], 'ans': 0, 'why': 'Two people talk at a bus stop and ride downtown.'},
  'scan': [{'q': 'How much is the fare?', 'ans': 'two dollars and fifty cents', 'alt': ['$2.50', '2.50', '2 dollars 50']}, {'q': 'How long does the trip take?', 'ans': 'about twenty minutes', 'alt': ['20 minutes', 'twenty minutes']}, {'q': 'What color is the bus?', 'ans': 'blue and white', 'alt': ['blue', 'blue white']}],
  'tf': [{'s': 'The bus goes downtown.', 'ans': True, 'why': '“Yes, it goes downtown.”'}, {'s': 'The bus is very full.', 'ans': False, 'why': 'It is almost empty.'}, {'s': 'The writer presses the stop button.', 'ans': True, 'why': 'He pressed it near downtown.'}, {'s': 'The trip takes two hours.', 'ans': False, 'why': 'It takes about twenty minutes.'}],
  'order': ['Ethan asks if the bus goes downtown.', 'The writer says the fare is $2.50.', 'They get on the bus.', 'The writer presses the stop button.', 'They say goodbye and get off.'],
  'ctx': [{'sent': 'The bus was almost empty.', 'w': 'empty', 'opts': ['with few people', 'very loud', 'very old'], 'ans': 0, 'why': 'Empty = nobody or almost nobody.'}, {'sent': 'The city moved past us.', 'w': 'past', 'opts': ['by', 'under', 'into'], 'ans': 0, 'why': 'Past = going by.'}, {'sent': 'A simple talk made my morning better.', 'w': 'simple', 'opts': ['easy and short', 'very expensive', 'very loud'], 'ans': 0, 'why': 'Simple = not complicated.'}],
  'chunkHunt': ['Does this bus go downtown?', 'How much is the fare?', 'Do I pay the driver?', 'How long does it take?', 'Enjoy your trip!'],
  'think': 'Do you take the bus? Tell a friend how to pay and how to stop it.'},
 'convo': {'npc': {'name': 'Ethan'}, 'story': 'You are at a bus stop in Washington. Ethan is new in the city and asks you questions.', 'turns': [
  {'npc': 'Excuse me, does this bus go downtown?', 'pt': 'Com licença, este ônibus vai ao centro?', 'opts': [
   {'en': 'This bus go to downtown.', 'pt': 'Este ônibus vai para o centro.', 'ok': False, 'fb': 'It goes downtown (no to, with s).'},
   {'en': 'I like the bus.', 'pt': 'Eu gosto do ônibus.', 'ok': False, 'fb': 'Not an answer.'},
   {'en': 'Yes, it goes downtown.', 'pt': 'Sim, vai ao centro.', 'ok': True, 'fb': 'Short and natural.'}]},
  {'npc': 'How much is the fare?', 'pt': 'Quanto custa a passagem?', 'opts': [
   {'en': 'Two dollars and fifty cents.', 'pt': 'Dois dólares e cinquenta centavos.', 'ok': True, 'fb': 'Say the full price.'},
   {'en': 'It is two hours.', 'pt': 'São duas horas.', 'ok': False, 'fb': 'Fare is money, not time.'},
   {'en': 'The fare is have two.', 'pt': 'A passagem é ter dois.', 'ok': False, 'fb': 'Grammar error.'}]},
  {'npc': 'Do I pay the driver?', 'pt': 'Pago ao motorista?', 'opts': [
   {'en': 'You pay a driver of bus.', 'pt': 'Você paga um motorista de ônibus.', 'ok': False, 'fb': 'Say the driver.'},
   {'en': 'No, I am the driver.', 'pt': 'Não, eu sou o motorista.', 'ok': False, 'fb': 'Wrong answer.'},
   {'en': 'Yes, or use a card.', 'pt': 'Sim, ou use um cartão.', 'ok': True, 'fb': 'Gives two options.'}]},
  {'npc': 'How long does it take?', 'pt': 'Quanto tempo demora?', 'opts': [
   {'en': 'About twenty minutes.', 'pt': 'Uns vinte minutos.', 'ok': True, 'fb': 'About = approximately.'},
   {'en': 'It takes twenty minute.', 'pt': 'Demora vinte minuto.', 'ok': False, 'fb': 'Minutes (plural).'},
   {'en': 'It is twenty dollars.', 'pt': 'São vinte dólares.', 'ok': False, 'fb': 'He asked about time.'}]},
  {'npc': 'Enjoy your trip!', 'pt': 'Aproveite a viagem!', 'opts': [
   {'en': 'You are welcome.', 'pt': 'De nada.', 'ok': False, 'fb': 'He did not thank you.'},
   {'en': 'Thanks! Bye.', 'pt': 'Valeu! Tchau.', 'ok': True, 'fb': 'Friendly close.'},
   {'en': 'I enjoy the trips.', 'pt': 'Eu gosto das viagens.', 'ok': False, 'fb': 'Does not answer the wish.'}]}]},
 'errors': [
  {'wrong': 'This bus go downtown?', 'fix': 'Does this bus go downtown?', 'alt': 'Do this bus go downtown?', 'why': 'Use Does with this bus.'},
  {'wrong': 'How much costs the fare?', 'fix': 'How much is the fare?', 'alt': 'How much are the fare?', 'why': 'Use How much is…'},
  {'wrong': 'I pay to the driver.', 'fix': 'I pay the driver.', 'alt': 'I pay at the driver.', 'why': 'Pay + person, no to.'},
  {'wrong': 'It takes twenty minute.', 'fix': 'It takes twenty minutes.', 'alt': 'It take twenty minutes.', 'why': 'Plural minutes and takes.'}],
 'homework': 'Write 5 sentences about how you take a bus in your city: stop, fare, time and how you get off.',
 'homework_items': ['Write 5 sentences about your bus trip.', 'Record: “Does this bus go to…?”', 'Practice saying prices: $1.75, $2.50.', 'Review: fare / driver / downtown.']}
