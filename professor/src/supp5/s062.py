"""Suplemento Quest v5 · aula 62: Renting a car + regular Can You Open the Trunk? (The Elephant's Child)."""
SUPP = {
 'reg': 72,
 'badge': {'icon': '🚗', 'name': 'Road Trip Ready', 'desc': 'Rent a car: license, days, price and gas'},
 'culture': {
  'hook': 'In the USA, a car is often the best way to see a big state. At a rental office, the steps are always the same: license, days, car size, price and gas.',
  'mythfact': [
   {'s': 'You usually need a driver’s license to rent a car in the USA.', 'ans': True, 'why': 'The office asks for your license, and often for a credit card too.'},
   {'s': 'In the USA, many rental cars are automatic.', 'ans': True, 'why': 'Automatic cars are the most common, and a manual car is hard to find.'},
   {'s': 'In the USA, people drive on the left side of the road.', 'ans': False, 'why': 'They drive on the right side, like in Brazil.'},
   {'s': 'Gas is always included in the price of a rental.', 'ans': False, 'why': 'Many offices ask you to return the car with a full tank, so ask the staff.'},
   {'s': '“The Elephant’s Child” is a story by Rudyard Kipling.', 'ans': True, 'why': 'It is one of the Just So Stories, from 1902.'}],
  'wild': [
   {'kind': 'Rental price board', 'lines': ['**Small car** $50 / day', '**Big car** $80 / day', 'Gas not included'], 'decode': {'q': 'How much are 3 days in a small car?', 'opts': ['$150', '$50', '$240'], 'ans': 0, 'why': '3 × $50 = $150.'}},
   {'kind': 'Sign at a rental desk', 'lines': ['**Please show your license.**', 'Return the car with a full tank.', 'Open 8 a.m. – 8 p.m.'], 'decode': {'q': 'What should you do with the car at the end?', 'opts': ['Return it with a full tank', 'Wash it', 'Keep it'], 'ans': 0, 'why': '“Return the car with a full tank.”'}}],
  'compare': {'br': 'In Brazil, many cars are manual, and people often fill the tank before returning a rental.', 'us': 'In the USA, most rental cars are automatic, and the price is usually per day. Gas and extra drivers can cost more.', 'tip': 'Ask: “Is gas included?”', 'ask': 'Do you drive a manual or an automatic car? Say it in English.'},
  'quiz': [
   {'q': 'You want to know the time of the rental. You ask…', 'opts': ['For how many days?', 'How many day you?', 'Days for how?'], 'ans': 0, 'why': 'For how many days? is the normal question.'},
   {'q': '“A small car is fifty dollars a day.” It means…', 'opts': ['$50 each day', '$50 for the whole year', '50 small cars'], 'ans': 0, 'why': 'A day = each day.'},
   {'q': 'What is an automatic car?', 'opts': ['a car without a clutch pedal', 'a car with no engine', 'a very old car'], 'ans': 0, 'why': 'Automatic cars change gears by themselves.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'A car for three days',
  'text': [
   'Claire is in **San Antonio**. She wants to see the Texas hills, so she goes to a car rental office. A young man named Ben works at the desk.',
   '“**Hi! I’d like to rent a car**,” Claire says. “**Sure. Do you have a driver’s license?**” Ben asks. “**Yes, here it is.**” He looks at the license. “**For how many days?**” “**Three days.**”',
   '“**A small car is fifty dollars a day**,” Ben says. “**That’s fine. Is gas included?**” “**No, it isn’t.**” Claire nods. She signs the paper, and Ben gives her the key. “**Have a safe trip!**”',
   'Claire walks to the parking lot. She remembers a story about an elephant. In “The Elephant’s Child,” a curious young elephant asks many questions and gets a long trunk. Claire smiles and says, “Now I want to see the trunk of my car.”',
   'The trunk is big. She puts her bag inside and closes it. Then she starts the car, puts on her seatbelt and drives out of the office. The road is open.'],
  'glossary': [{'w': 'rent', 'pt': 'alugar'}, {'w': 'office', 'pt': 'escritório, agência'}, {'w': 'license', 'pt': 'carteira de motorista'}, {'w': 'included', 'pt': 'incluído'}, {'w': 'parking lot', 'pt': 'estacionamento'}, {'w': 'curious', 'pt': 'curioso'}, {'w': 'trunk', 'pt': 'porta-malas (também: tromba)'}, {'w': 'seatbelt', 'pt': 'cinto de segurança'}, {'w': 'road', 'pt': 'estrada'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A woman rents a car', 'A man cooks lunch', 'A girl buys a ticket'], 'ans': 0, 'why': 'Claire rents a car in San Antonio.'},
  'scan': [{'q': 'For how many days does Claire rent the car?', 'ans': 'three days', 'alt': ['3 days', 'three']}, {'q': 'How much is a small car per day?', 'ans': 'fifty dollars', 'alt': ['$50', '50 dollars', 'fifty']}, {'q': 'What does Ben give Claire?', 'ans': 'the key', 'alt': ['key', 'a key']}],
  'tf': [{'s': 'Claire shows her driver’s license.', 'ans': True, 'why': '“Yes, here it is.”'}, {'s': 'Gas is included in the price.', 'ans': False, 'why': 'Ben says it is not included.'}, {'s': 'Claire rents the car for a week.', 'ans': False, 'why': 'She rents it for three days.'}, {'s': 'Claire puts her bag in the trunk.', 'ans': True, 'why': 'The trunk is big, and she puts her bag inside.'}],
  'order': ['Claire goes to the rental office.', 'She shows her license.', 'Ben says the price.', 'Ben gives her the key.', 'Claire drives away.'],
  'ctx': [{'sent': 'Is gas included?', 'w': 'included', 'opts': ['part of the price', 'very far', 'not allowed'], 'ans': 0, 'why': 'Included = already in the price.'}, {'sent': 'A curious elephant asks many questions.', 'w': 'curious', 'opts': ['wants to know things', 'is very tired', 'is very big'], 'ans': 0, 'why': 'Curious = wants to learn.'}, {'sent': 'She puts on her seatbelt.', 'w': 'seatbelt', 'opts': ['a belt in a car for safety', 'a seat in a bus', 'a car key'], 'ans': 0, 'why': 'A seatbelt keeps you safe.'}],
  'chunkHunt': ['I’d like to rent a car.', 'For how many days?', 'Is gas included?', 'Have a safe trip!'],
  'think': 'Do you want to drive in another country? Why or why not?'},
 'convo': {'npc': {'name': 'Claire'}, 'story': 'You work at a car rental office. Claire wants to rent a car. Help her.', 'turns': [
  {'npc': 'Hi! I’d like to rent a car.', 'pt': 'Oi! Eu gostaria de alugar um carro.', 'opts': [
   {'en': 'Sure. Do you have a driver’s license?', 'pt': 'Claro. Você tem carteira de motorista?', 'ok': True, 'fb': 'Normal first question.'},
   {'en': 'Sure. You have a license of drive?', 'pt': 'Claro. Você tem uma licença de dirigir?', 'ok': False, 'fb': 'Say a driver’s license.'},
   {'en': 'I am a car, thanks.', 'pt': 'Sou um carro, obrigado.', 'ok': False, 'fb': 'Wrong meaning.'}]},
  {'npc': 'Yes, here it is.', 'pt': 'Sim, aqui está.', 'opts': [
   {'en': 'The license is yes.', 'pt': 'A carteira é sim.', 'ok': False, 'fb': 'It does not make sense.'},
   {'en': 'How many days for?', 'pt': 'Quantos dias para?', 'ok': False, 'fb': 'Say: For how many days?'},
   {'en': 'Thanks. For how many days?', 'pt': 'Obrigado. Por quantos dias?', 'ok': True, 'fb': 'Natural next question.'}]},
  {'npc': 'Three days.', 'pt': 'Três dias.', 'opts': [
   {'en': 'A small car is fifty dollars a day.', 'pt': 'Um carro pequeno custa cinquenta dólares por dia.', 'ok': True, 'fb': 'Gives the price per day.'},
   {'en': 'A small car costs fifty dollars day.', 'pt': 'Um carro pequeno custa cinquenta dólares dia.', 'ok': False, 'fb': 'Use a day.'},
   {'en': 'Three days is a car.', 'pt': 'Três dias é um carro.', 'ok': False, 'fb': 'Does not fit.'}]},
  {'npc': 'That’s fine. Is gas included?', 'pt': 'Tudo bem. A gasolina está incluída?', 'opts': [
   {'en': 'No, it is not included.', 'pt': 'Não, não está incluída.', 'ok': False, 'fb': 'Good, but short is more natural: No, it isn’t.'},
   {'en': 'No, it isn’t.', 'pt': 'Não, não está.', 'ok': True, 'fb': 'Short and natural.'},
   {'en': 'Yes, I included.', 'pt': 'Sim, eu incluí.', 'ok': False, 'fb': 'Wrong grammar and wrong answer.'}]},
  {'npc': 'Okay. Thank you!', 'pt': 'Certo. Obrigada!', 'opts': [
   {'en': 'Have a safe trip!', 'pt': 'Boa viagem!', 'ok': True, 'fb': 'Natural goodbye for a driver.'},
   {'en': 'Welcome to a safe!', 'pt': 'Bem-vindo a um cofre!', 'ok': False, 'fb': 'Wrong meaning.'},
   {'en': 'I am safe, thanks.', 'pt': 'Estou seguro, valeu.', 'ok': False, 'fb': 'Does not fit.'}]}]},
 'errors': [
  {'wrong': 'I want rent a car.', 'fix': 'I want to rent a car.', 'alt': 'I want renting a car.', 'why': 'After want, use to + verb.'},
  {'wrong': 'For how many day?', 'fix': 'For how many days?', 'alt': 'For how much days?', 'why': 'Use many + plural days.'},
  {'wrong': 'Fifty dollars by day.', 'fix': 'Fifty dollars a day.', 'alt': 'Fifty dollar a day.', 'why': 'In English, say a day for each day.'},
  {'wrong': 'Gas is include?', 'fix': 'Is gas included?', 'alt': 'Gas included is?', 'why': 'Question: Is + thing + included?'}],
 'homework': 'Write a short dialogue: you rent a car for two days and ask about the price and gas.',
 'homework_items': ['Write the 5 steps to rent a car.', 'Say aloud: For how many days?', 'Listen to the dialogue and shadow Claire.', 'Review: a day / a week / a month.']}
