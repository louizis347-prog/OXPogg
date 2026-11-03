"""Suplemento Quest v5 · aula 48: Taking a taxi + regular A bumpy ride (Black Beauty)."""
SUPP = {
 'reg': 149,
 'badge': {'icon': '🚕', 'name': 'Taxi Talker', 'desc': 'Give a destination, time and price for a ride in English'},
 'sticker': {'cat': 'Everyday culture', 'title': 'Taxis and Rides in the USA', 'sub': 'Hail it or book it on an app'},
 'culture': {
  'hook': 'In big American cities you can raise your hand for a taxi, or book a ride with an app. Either way, a short, clear request gets you where you want to go.',
  'polite': 'Say **“To the airport, please”** and **“Thank you”** when you arrive. A tip is common.',
  'mythfact': [
   {'s': 'Taxis in New York City are famous for being yellow.', 'ans': True, 'why': 'The yellow cab is a symbol of the city.'},
   {'s': 'In the USA nobody uses apps to get a ride.', 'ans': False, 'why': 'Uber and Lyft are widely used.'},
   {'s': 'It is common to tip the driver in a taxi.', 'ans': True, 'why': 'People often add a tip, around 15 to 20 percent.'},
   {'s': 'Airports have only one terminal.', 'ans': False, 'why': 'Large airports, like LAX, have several terminals.'}],
  'wild': [
   {'kind': 'Ride app screen', 'lines': ['**Your driver is Marco**', 'Gray car · Arrives in 3 min', 'Pickup: Main Street, Door B'], 'decode': {'q': 'When does the driver arrive?', 'opts': ['In 3 minutes', 'In 30 minutes', 'In 3 hours'], 'ans': 0, 'why': '“Arrives in 3 min.”'}},
   {'kind': 'Taxi sign', 'lines': ['**Airport Terminal 2**', 'Taxi stand · Wait here', 'Do not block the lane'], 'decode': {'q': 'Where should you wait for a taxi?', 'opts': ['At the taxi stand', 'In the lane', 'On the roof'], 'ans': 0, 'why': '“Taxi stand · Wait here.”'}}],
  'compare': {'br': 'In Brazil many people use taxis or apps like 99 and Uber, and some taxis have a meter.', 'us': 'In the USA you raise your hand in big cities or use an app, and many people tip.', 'tip': 'Tell the driver the terminal number, not just “airport”.', 'ask': 'How do you get to the airport in your city? Say it in English.'},
  'quiz': [
   {'q': 'The driver says “Where to?” You want the airport. You say…', 'opts': ['To the airport, please.', 'I am airport.', 'Airport me.'], 'ans': 0, 'why': 'To + place + please.'},
   {'q': 'Which question asks about time?', 'opts': ['How long does it take?', 'How much is it?', 'Which terminal?'], 'ans': 0, 'why': 'How long = time.'},
   {'q': 'What is Terminal 2?', 'opts': ['A part of the airport', 'A kind of taxi', 'A phone app'], 'ans': 0, 'why': 'A terminal is a building at an airport.'}]},
 'reading': {
  'genre': 'Blog post', 'title': 'A taxi ride in Los Angeles',
  'text': [
   'I had an early flight from Los Angeles, so I booked a taxi for six in the morning. A white car stopped in front of my hotel, and the driver, Marco, opened the window. “**Hi! Where to?**” he asked.',
   '“**To the airport, please**,” I said. “**Sure. Which terminal?**” he asked. “**Terminal two**,” I said. I put my bag in the trunk and sat in the back seat. The car was clean and smelled like lemons.',
   'We drove through quiet streets. “**How long does it take?**” Marco asked. “**About thirty minutes**,” I said. “The traffic is bad later, but now the roads are empty.” He smiled and said, “That’s good.”',
   '“**How much is it?**” Marco asked. “**About forty dollars**,” I said. He nodded. I looked at the app on my phone. It showed a map, the time and the price. Everything was clear.',
   'When we arrived at Terminal 2, I paid and gave a small tip. Marco put my bag on the sidewalk. “**Safe travels!**” he said. I thanked him and walked into the building.',
   'The ride was short, but it was easy and friendly. I think a clear sentence and a smile are the best tools for a trip.'],
  'glossary': [{'w': 'flight', 'pt': 'voo'}, {'w': 'booked', 'pt': 'reservei'}, {'w': 'trunk', 'pt': 'porta-malas'}, {'w': 'back seat', 'pt': 'banco de trás'}, {'w': 'traffic', 'pt': 'trânsito'}, {'w': 'empty', 'pt': 'vazias'}, {'w': 'tip', 'pt': 'gorjeta'}, {'w': 'sidewalk', 'pt': 'calçada'}, {'w': 'terminal', 'pt': 'terminal'}],
  'fast': {'q': 'What is this text about?', 'opts': ['A taxi ride to the airport', 'A birthday party', 'A cooking class'], 'ans': 0, 'why': 'The writer takes a taxi to the airport.'},
  'scan': [{'q': 'Which terminal?', 'ans': 'terminal two', 'alt': ['2', 'terminal 2', 'two']}, {'q': 'How long is the ride?', 'ans': 'about thirty minutes', 'alt': ['30 minutes', 'thirty minutes']}, {'q': 'How much is the ride?', 'ans': 'about forty dollars', 'alt': ['$40', '40 dollars', '40']}],
  'tf': [{'s': 'The writer goes to the airport.', 'ans': True, 'why': '“To the airport, please.”'}, {'s': 'The traffic is very bad in the early morning.', 'ans': False, 'why': 'The roads are empty.'}, {'s': 'The writer gives a tip.', 'ans': True, 'why': '“I paid and gave a small tip.”'}, {'s': 'The car smells like fish.', 'ans': False, 'why': 'It smells like lemons.'}],
  'order': ['The writer books a taxi.', 'Marco asks where to.', 'They talk about time and price.', 'They arrive at Terminal 2.', 'Marco says Safe travels!'],
  'ctx': [{'sent': 'The car was clean and smelled like lemons.', 'w': 'smelled', 'opts': ['had the odor', 'looked', 'sounded'], 'ans': 0, 'why': 'Smelled = had a smell.'}, {'sent': 'He nodded.', 'w': 'nodded', 'opts': ['moved his head to say yes', 'ran', 'shouted'], 'ans': 0, 'why': 'Nod = move the head down.'}, {'sent': 'Everything was clear.', 'w': 'clear', 'opts': ['easy to understand', 'very dark', 'very small'], 'ans': 0, 'why': 'Clear = easy to understand.'}],
  'chunkHunt': ['Where to?', 'To the airport, please.', 'Which terminal?', 'How long does it take?', 'Safe travels!'],
  'think': 'How do you get to the airport? Write three questions you can ask the driver.'},
 'convo': {'npc': {'name': 'Marco'}, 'story': 'You are in a taxi in Los Angeles. Marco is the driver. Tell him where you want to go.', 'turns': [
  {'npc': 'Hi! Where to?', 'pt': 'Oi! Para onde?', 'opts': [
   {'en': 'I go to airport.', 'pt': 'Eu vou para aeroporto.', 'ok': False, 'fb': 'Use To the airport, please.'},
   {'en': 'I am a taxi.', 'pt': 'Eu sou um táxi.', 'ok': False, 'fb': 'Wrong meaning.'},
   {'en': 'To the airport, please.', 'pt': 'Para o aeroporto, por favor.', 'ok': True, 'fb': 'Short and polite.'}]},
  {'npc': 'Sure. Which terminal?', 'pt': 'Claro. Qual terminal?', 'opts': [
   {'en': 'Terminal two.', 'pt': 'Terminal dois.', 'ok': True, 'fb': 'Gives the number.'},
   {'en': 'The terminal is much.', 'pt': 'O terminal é muito.', 'ok': False, 'fb': 'Not natural.'},
   {'en': 'It is a Monday.', 'pt': 'É segunda.', 'ok': False, 'fb': 'Out of context.'}]},
  {'npc': 'How long does it take?', 'pt': 'Quanto tempo demora?', 'opts': [
   {'en': 'Take thirty minutes about.', 'pt': 'Demora trinta minutos cerca.', 'ok': False, 'fb': 'Say About thirty minutes.'},
   {'en': 'About thirty minutes.', 'pt': 'Uns trinta minutos.', 'ok': True, 'fb': 'Natural estimate.'},
   {'en': 'Thirty dollars.', 'pt': 'Trinta dólares.', 'ok': False, 'fb': 'He asked about time.'}]},
  {'npc': 'How much is it?', 'pt': 'Quanto custa?', 'opts': [
   {'en': 'About forty dollars.', 'pt': 'Uns quarenta dólares.', 'ok': True, 'fb': 'Gives a price.'},
   {'en': 'It costs forty hour.', 'pt': 'Custa quarenta hora.', 'ok': False, 'fb': 'Dollars, not hour.'},
   {'en': 'I am forty.', 'pt': 'Eu tenho quarenta.', 'ok': False, 'fb': 'This is about age.'}]},
  {'npc': 'Safe travels!', 'pt': 'Boa viagem!', 'opts': [
   {'en': 'Safe is the travel.', 'pt': 'Seguro é a viagem.', 'ok': False, 'fb': 'Not natural.'},
   {'en': 'Welcome!', 'pt': 'Bem-vindo!', 'ok': False, 'fb': 'Wrong reply.'},
   {'en': 'Thanks! You too.', 'pt': 'Obrigado! Você também.', 'ok': True, 'fb': 'Friendly goodbye.'}]}]},
 'errors': [
  {'wrong': 'I go to airport.', 'fix': 'To the airport, please.', 'alt': 'I go to the airport please.', 'why': 'Use the + airport and polite please.'},
  {'wrong': 'How much time is it?', 'fix': 'How long does it take?', 'alt': 'How much time it takes?', 'why': 'Use How long does it take?'},
  {'wrong': 'It costs about forty dollar.', 'fix': 'It costs about forty dollars.', 'alt': 'It cost about forty dollars.', 'why': 'Dollars is plural; costs for it.'},
  {'wrong': 'I want go to terminal two.', 'fix': 'I want to go to terminal two.', 'alt': 'I want going to terminal two.', 'why': 'want + to + verb.'}],
 'homework': 'Write a short dialogue with a taxi driver: place, terminal, time and price. Then read both parts aloud.',
 'homework_items': ['Write a 6-line taxi dialogue.', 'Record: “To the airport, please.”', 'Learn: terminal, trunk, tip, meter.', 'Review: Which terminal? / How long does it take?']}
