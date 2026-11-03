"""Suplemento Quest v5 · aula 49: Parking + regular You mustn't park here (The Selfish Giant)."""
SUPP = {
 'reg': 155,
 'badge': {'icon': '🅿️', 'name': 'Parking Pro', 'desc': 'Read parking signs and ask where to park in English'},
 'sticker': {'cat': 'Everyday culture', 'title': 'Parking Rules in the USA', 'sub': 'Signs, meters and lots'},
 'culture': {
  'hook': 'Parking in American cities can be confusing, because signs give times and rules. A quick look at the sign can save you a big fine.',
  'polite': 'Ask **“Excuse me, can I park here?”** before you leave your car.',
  'mythfact': [
   {'s': 'In most places you cannot park in front of a fire hydrant.', 'ans': True, 'why': 'Fire trucks need access, so cars must keep a distance.'},
   {'s': 'A parking meter often takes coins, cards or a phone app.', 'ans': True, 'why': 'Many cities allow all three.'},
   {'s': 'A “no parking” sign means you can stay as long as you like.', 'ans': False, 'why': 'It means you cannot park there at the times shown.'},
   {'s': 'All parking lots are free in the USA.', 'ans': False, 'why': 'Many lots charge by the hour or day.'}],
  'wild': [
   {'kind': 'Street sign', 'lines': ['**2 HOUR PARKING**', '8 AM – 6 PM', 'MON – FRI'], 'decode': {'q': 'How long can you park?', 'opts': ['Two hours', 'All day', 'Ten minutes'], 'ans': 0, 'why': '“2 hour parking.”'}},
   {'kind': 'Parking lot sign', 'lines': ['**Parking · $5 per hour**', 'Pay at the machine', 'Keep your ticket'], 'decode': {'q': 'Where do you pay?', 'opts': ['At the machine', 'At the car', 'At a house'], 'ans': 0, 'why': '“Pay at the machine.”'}}],
  'compare': {'br': 'In Brazil you may see “proibido estacionar” signs, and in some places a guardador helps with parking.', 'us': 'In the USA signs show hours and days, and you may pay a meter or a machine.', 'tip': 'Read the whole sign from top to bottom. The rule often changes by time or day.', 'ask': 'Is parking easy or hard where you live? Say it in English.'},
  'quiz': [
   {'q': 'A sign says “No Parking.” You can…', 'opts': ['not park there', 'park for free', 'sleep there'], 'ans': 0, 'why': 'No Parking = not allowed.'},
   {'q': 'Which question asks where to park?', 'opts': ['Where can I park?', 'Where is my park?', 'Park where is?'], 'ans': 0, 'why': 'Where can I park? is natural.'},
   {'q': '“Five dollars an hour” means…', 'opts': ['The price for one hour', 'Five hours', 'A big car'], 'ans': 0, 'why': 'Per hour pricing.'}]},
 'reading': {
  'genre': 'Short story', 'title': 'The wrong spot',
  'text': [
   'Rosa drove around the block three times. It was Saturday, and the streets in Houston were busy. She saw an empty place near a bank and stopped. A man on the sidewalk waved his hand.',
   '“**Excuse me, can I park here?**” Rosa asked. “**No, this is a no parking zone**,” the man said. He pointed to a red sign. Rosa read it: “No Parking, 8 AM to 6 PM.” It was ten o’clock.',
   '“**Where can I park?**” she asked. “**There’s a parking lot on Oak Street**,” the man said. “It’s around the corner.” “**How much is it?**” “**Five dollars an hour**,” he said. “You pay at the machine.”',
   '“**OK. Thanks for the help**,” Rosa said. “**No problem!**” the man answered. “**Drive safe!**” Rosa smiled. She was happy, because a big fine can cost a lot of money.',
   'She drove to Oak Street and found the lot. It was clean and well lit. She parked, took her ticket and put it on the dashboard. Then she walked to the machine and paid for two hours.',
   'Rosa learned something that day: read the sign before you leave the car. A short question can save your day, and your money.'],
  'glossary': [{'w': 'block', 'pt': 'quarteirão'}, {'w': 'sidewalk', 'pt': 'calçada'}, {'w': 'waved', 'pt': 'acenou'}, {'w': 'zone', 'pt': 'zona'}, {'w': 'sign', 'pt': 'placa'}, {'w': 'parking lot', 'pt': 'estacionamento'}, {'w': 'machine', 'pt': 'máquina'}, {'w': 'fine', 'pt': 'multa'}, {'w': 'dashboard', 'pt': 'painel do carro'}],
  'fast': {'q': 'What is this text about?', 'opts': ['A driver asks where to park', 'A man buys a bus ticket', 'A girl cooks pasta'], 'ans': 0, 'why': 'Rosa asks where she can park.'},
  'scan': [{'q': 'Which street has the parking lot?', 'ans': 'Oak Street', 'alt': ['oak street', 'oak']}, {'q': 'How much is the lot per hour?', 'ans': 'five dollars', 'alt': ['$5', '5 dollars', '5']}, {'q': 'What time is it when Rosa asks?', 'ans': 'ten o’clock', 'alt': ['10', '10 am', 'ten']}],
  'tf': [{'s': 'Rosa can park near the bank.', 'ans': False, 'why': 'It is a no parking zone.'}, {'s': 'The parking lot is on Oak Street.', 'ans': True, 'why': 'The man says so.'}, {'s': 'Parking in the lot is free.', 'ans': False, 'why': 'It costs five dollars an hour.'}, {'s': 'Rosa pays at a machine.', 'ans': True, 'why': 'She walks to the machine and pays.'}],
  'order': ['Rosa drives around the block.', 'She asks if she can park near the bank.', 'The man says there is a lot on Oak Street.', 'Rosa learns the price.', 'She parks and pays at the machine.'],
  'ctx': [{'sent': 'A man on the sidewalk waved his hand.', 'w': 'waved', 'opts': ['moved his hand to say hi or stop', 'washed his hand', 'lost his hand'], 'ans': 0, 'why': 'Wave = move the hand.'}, {'sent': 'A big fine can cost a lot of money.', 'w': 'fine', 'opts': ['money you pay for breaking a rule', 'a gift', 'a ticket for a bus'], 'ans': 0, 'why': 'A fine is a penalty.'}, {'sent': 'It was clean and well lit.', 'w': 'lit', 'opts': ['with good light', 'very noisy', 'very small'], 'ans': 0, 'why': 'Well lit = lots of light.'}],
  'chunkHunt': ['Can I park here?', 'This is a no parking zone.', 'Where can I park?', 'There’s a parking lot on…', 'Five dollars an hour.'],
  'think': 'What parking signs do you know? Write one rule in English.'},
 'convo': {'npc': {'name': 'Rosa'}, 'story': 'You are on a street in Houston. Rosa is a driver who wants to park. Help her.', 'turns': [
  {'npc': 'Excuse me, can I park here?', 'pt': 'Com licença, posso estacionar aqui?', 'opts': [
   {'en': 'No, this is a no parking zone.', 'pt': 'Não, aqui é proibido estacionar.', 'ok': True, 'fb': 'Clear answer with the reason.'},
   {'en': 'Yes, you are park.', 'pt': 'Sim, você é estacionar.', 'ok': False, 'fb': 'Grammar error.'},
   {'en': 'I like your car.', 'pt': 'Eu gosto do seu carro.', 'ok': False, 'fb': 'Out of context.'}]},
  {'npc': 'Where can I park?', 'pt': 'Onde posso estacionar?', 'opts': [
   {'en': 'Park in the sky.', 'pt': 'Estacione no céu.', 'ok': False, 'fb': 'Silly answer.'},
   {'en': 'There is a parking in Oak Street.', 'pt': 'Tem um estacionando na Rua Oak.', 'ok': False, 'fb': 'Say a parking lot on Oak Street.'},
   {'en': 'There’s a parking lot on Oak Street.', 'pt': 'Tem um estacionamento na Rua Oak.', 'ok': True, 'fb': 'Natural way to give a place.'}]},
  {'npc': 'How much is it?', 'pt': 'Quanto custa?', 'opts': [
   {'en': 'It is five hour.', 'pt': 'São cinco hora.', 'ok': False, 'fb': 'Price is in dollars.'},
   {'en': 'Five dollars an hour.', 'pt': 'Cinco dólares por hora.', 'ok': True, 'fb': 'Price + time.'},
   {'en': 'I have five.', 'pt': 'Eu tenho cinco.', 'ok': False, 'fb': 'Not what she asked.'}]},
  {'npc': 'OK. Thanks for the help.', 'pt': 'Ok. Valeu pela ajuda.', 'opts': [
   {'en': 'You help me too.', 'pt': 'Você me ajuda também.', 'ok': False, 'fb': 'Not a normal reply.'},
   {'en': 'No problem!', 'pt': 'Sem problema!', 'ok': True, 'fb': 'Natural, friendly reply.'},
   {'en': 'Yes, I help.', 'pt': 'Sim, eu ajudo.', 'ok': False, 'fb': 'Not natural.'}]},
  {'npc': 'Drive safe!', 'pt': 'Dirija com segurança!', 'opts': [
   {'en': 'Thanks, you too!', 'pt': 'Valeu, você também!', 'ok': False, 'fb': 'Close, but she is the driver. Say Thanks, bye!'},
   {'en': 'I am safe.', 'pt': 'Eu estou seguro.', 'ok': False, 'fb': 'Does not answer.'},
   {'en': 'Thanks, bye!', 'pt': 'Valeu, tchau!', 'ok': True, 'fb': 'Natural close.'}]}]},
 'errors': [
  {'wrong': 'Can I park in here?', 'fix': 'Can I park here?', 'alt': 'Can I to park here?', 'why': 'Here already means in this place.'},
  {'wrong': 'It is prohibited to park.', 'fix': 'It is a no parking zone.', 'alt': 'It is not allowed park.', 'why': 'Use no parking zone or you can’t park.'},
  {'wrong': 'Five dollars by hour.', 'fix': 'Five dollars an hour.', 'alt': 'Five dollar an hour.', 'why': 'Use an hour for rates.'},
  {'wrong': 'There is a parking in Oak Street.', 'fix': 'There is a parking lot on Oak Street.', 'alt': 'There is a parking at Oak Street.', 'why': 'Parking lot is the place; use on with streets.'}],
 'homework': 'Draw 3 parking signs and write what each one means in English. Say the rules aloud.',
 'homework_items': ['Draw and explain 3 parking signs.', 'Record: “Can I park here?”', 'Write the prices: $3, $5, $10 an hour.', 'Review: no parking zone / parking lot / fine.']}
