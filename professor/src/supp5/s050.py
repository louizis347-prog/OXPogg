"""Suplemento Quest v5 · aula 50: At the gas station + regular Take a Shower, Take a Bus (Planes, Trains and Automobiles)."""
SUPP = {
 'reg': 53,
 'badge': {'icon': '⛽', 'name': 'Road Trip Ready', 'desc': 'Fill the tank, pay and buy a snack in English'},
 'sticker': {'cat': 'Everyday culture', 'title': 'The American Gas Station', 'sub': 'Regular, premium and a snack'},
 'culture': {
  'hook': 'On an American road trip, the gas station is a small stop with fuel, snacks and a restroom. You pick a pump, choose a grade and pay by the gallon.',
  'polite': 'Say **“Pump number three, please”** if you pay inside. Many people simply pay at the pump with a card.',
  'mythfact': [
   {'s': 'In the USA gas is sold by the gallon.', 'ans': True, 'why': 'Prices on the big sign are per gallon, not per liter.'},
   {'s': 'Most gas stations in the USA have a free attendant who pumps for you.', 'ans': False, 'why': 'Most people pump their own gas. New Jersey is a well-known exception, and Oregon has allowed self-service only recently.'},
   {'s': 'Regular and premium are two kinds of gasoline.', 'ans': True, 'why': 'Premium has a higher octane number and costs more.'},
   {'s': 'A gas station only sells gas.', 'ans': False, 'why': 'Many also sell water, snacks and coffee, and have a restroom.'}],
  'wild': [
   {'kind': 'Price sign', 'lines': ['**Regular $3.49**', '**Premium $4.09**', 'Price per gallon'], 'decode': {'q': 'Which gas costs more?', 'opts': ['Premium', 'Regular', 'They cost the same'], 'ans': 0, 'why': '$4.09 is more than $3.49.'}},
   {'kind': 'Pump screen', 'lines': ['**Pay here or inside?**', 'Choose: Regular · Plus · Premium', 'Lift the nozzle to start'], 'decode': {'q': 'What do you do to start?', 'opts': ['Lift the nozzle', 'Turn off the car', 'Call the police'], 'ans': 0, 'why': '“Lift the nozzle to start.”'}}],
  'compare': {'br': 'In Brazil an attendant, the frentista, usually fills the tank, and many cars can use ethanol or gasoline.', 'us': 'In the USA most drivers fill the car themselves and pay by the gallon.', 'tip': 'Choose regular unless your car manual says premium.', 'ask': 'Who fills your car at the gas station? Say it in English.'},
  'quiz': [
   {'q': 'The attendant asks “Regular or premium?” You want the cheaper one. You say…', 'opts': ['Regular, please.', 'Cheap is regular.', 'I am regular.'], 'ans': 0, 'why': 'Regular is the standard gasoline.'},
   {'q': 'How is gas sold in the USA?', 'opts': ['By the gallon', 'By the meter', 'By the pound'], 'ans': 0, 'why': 'US prices are per gallon.'},
   {'q': '“Fill ’er up” means…', 'opts': ['Fill the tank', 'Buy a snack', 'Wash the car'], 'ans': 0, 'why': 'It is a casual way to ask for a full tank.'}]},
 'reading': {
  'genre': 'Travel blog', 'title': 'A stop in Denver',
  'text': [
   'We were on a long road trip from Denver to Utah. After two hours, the fuel light came on. “We are running on empty!” my friend Jonah said. We stopped at a gas station near the highway.',
   'The station had six pumps. We parked at pump number three. Jonah went inside and said to the clerk, “**Hi! Pump number three, please.**” The clerk asked, “**How much gas do you want?**” “**Twenty dollars, please**,” Jonah answered.',
   '“**Do you want regular or premium?**” the clerk asked. “**Regular, please**,” Jonah said. “**Do you need anything else?**” “**A bottle of water**,” Jonah said. The clerk said, “**That’s twenty-two dollars**.” Jonah paid with a card.',
   'I filled the tank. First, I lifted the nozzle. Then I put it in the car and pressed the handle. The numbers on the pump went up fast. Finally, I hung the nozzle back and closed the cap.',
   'We used the restroom, and I bought a coffee. The clerk smiled and said, “**Drive safe!**” “**Thanks!**” I said. The sun was low, and the mountains looked red and gold.',
   'Back on the road, Jonah drank his water and I watched the map. A small stop like this one is a good moment to rest and check the car.'],
  'glossary': [{'w': 'road trip', 'pt': 'viagem de carro'}, {'w': 'fuel', 'pt': 'combustível'}, {'w': 'highway', 'pt': 'rodovia'}, {'w': 'pump', 'pt': 'bomba'}, {'w': 'clerk', 'pt': 'atendente'}, {'w': 'tank', 'pt': 'tanque'}, {'w': 'nozzle', 'pt': 'bico da bomba'}, {'w': 'cap', 'pt': 'tampa'}, {'w': 'restroom', 'pt': 'banheiro'}],
  'fast': {'q': 'What is this text about?', 'opts': ['A stop at a gas station on a trip', 'A cooking class', 'A school test'], 'ans': 0, 'why': 'They stop for gas on a road trip.'},
  'scan': [{'q': 'Which pump number?', 'ans': 'three', 'alt': ['3', 'pump three', 'number three']}, {'q': 'How much gas does Jonah buy?', 'ans': 'twenty dollars', 'alt': ['$20', '20 dollars', '20']}, {'q': 'What is the total?', 'ans': 'twenty-two dollars', 'alt': ['$22', '22', '22 dollars']}],
  'tf': [{'s': 'The friends are on a road trip.', 'ans': True, 'why': 'Denver to Utah.'}, {'s': 'Jonah buys premium gas.', 'ans': False, 'why': 'He says regular, please.'}, {'s': 'Jonah pays with a card.', 'ans': True, 'why': '“Jonah paid with a card.”'}, {'s': 'The station has only one pump.', 'ans': False, 'why': 'It has six pumps.'}],
  'order': ['The fuel light comes on.', 'They stop at pump number three.', 'Jonah asks for twenty dollars of regular gas.', 'The writer fills the tank.', 'The clerk says Drive safe!'],
  'ctx': [{'sent': 'We are running on empty!', 'w': 'running on empty', 'opts': ['almost out of fuel', 'very fast', 'very happy'], 'ans': 0, 'why': 'On empty = no fuel left.'}, {'sent': 'The numbers on the pump went up fast.', 'w': 'went up', 'opts': ['became bigger', 'became smaller', 'fell down'], 'ans': 0, 'why': 'Went up = increased.'}, {'sent': 'I hung the nozzle back.', 'w': 'hung', 'opts': ['put it in its place', 'threw it away', 'broke it'], 'ans': 0, 'why': 'Hung = put on a hook.'}],
  'chunkHunt': ['Pump number three, please.', 'How much gas do you want?', 'Regular or premium?', 'Do you need anything else?', 'Drive safe!'],
  'think': 'Do you like road trips? What do you buy at a stop?'},
 'convo': {'npc': {'name': 'Jonah'}, 'story': 'You work at a gas station in Denver. Jonah is a customer on a road trip. Help him.', 'turns': [
  {'npc': 'Hi! Pump number three, please.', 'pt': 'Oi! Bomba número três, por favor.', 'opts': [
   {'en': 'How much gas do you want?', 'pt': 'Quanto de gasolina você quer?', 'ok': True, 'fb': 'The natural question.'},
   {'en': 'What is your age?', 'pt': 'Qual é a sua idade?', 'ok': False, 'fb': 'Not relevant.'},
   {'en': 'You are three?', 'pt': 'Você é três?', 'ok': False, 'fb': 'Wrong meaning.'}]},
  {'npc': 'Twenty dollars, please.', 'pt': 'Vinte dólares, por favor.', 'opts': [
   {'en': 'Do you want regular or premium?', 'pt': 'Quer comum ou premium?', 'ok': True, 'fb': 'The next step.'},
   {'en': 'Twenty is a good.', 'pt': 'Vinte é um bom.', 'ok': False, 'fb': 'Not natural.'},
   {'en': 'I have twenty years.', 'pt': 'Eu tenho vinte anos.', 'ok': False, 'fb': 'Wrong context.'}]},
  {'npc': 'Regular, please.', 'pt': 'Comum, por favor.', 'opts': [
   {'en': 'Anything else is need?', 'pt': 'Mais alguma coisa é precisar?', 'ok': False, 'fb': 'Grammar error.'},
   {'en': 'Regular is a color.', 'pt': 'Comum é uma cor.', 'ok': False, 'fb': 'Wrong meaning.'},
   {'en': 'Do you need anything else?', 'pt': 'Precisa de mais alguma coisa?', 'ok': True, 'fb': 'Polite service phrase.'}]},
  {'npc': 'A bottle of water.', 'pt': 'Uma garrafa de água.', 'opts': [
   {'en': 'It is twenty-two dollar.', 'pt': 'São vinte e dois dólar.', 'ok': False, 'fb': 'Dollars (plural).'},
   {'en': 'That’s twenty-two dollars.', 'pt': 'São vinte e dois dólares.', 'ok': True, 'fb': 'Total with the unit.'},
   {'en': 'The water has twenty-two.', 'pt': 'A água tem vinte e dois.', 'ok': False, 'fb': 'Not a price statement.'}]},
  {'npc': 'Drive safe!', 'pt': 'Dirija com segurança!', 'opts': [
   {'en': 'You drive safe too.', 'pt': 'Você dirige seguro também.', 'ok': False, 'fb': 'Not natural.'},
   {'en': 'Thanks! Have a good trip.', 'pt': 'Valeu! Boa viagem.', 'ok': True, 'fb': 'Friendly close.'},
   {'en': 'I am safe, thanks.', 'pt': 'Estou seguro, valeu.', 'ok': False, 'fb': 'Not what he said.'}]}]},
 'errors': [
  {'wrong': 'I want twenty dollars of gas.', 'fix': 'Twenty dollars, please.', 'alt': 'Twenty dollar, please.', 'why': 'Short and polite for a service.'},
  {'wrong': 'Regular or premium you want?', 'fix': 'Do you want regular or premium?', 'alt': 'You want regular or premium?', 'why': 'Questions start with do you.'},
  {'wrong': 'Is twenty-two dollars.', 'fix': 'That’s twenty-two dollars.', 'alt': 'It are twenty-two dollars.', 'why': 'Start with That’s or It’s.'},
  {'wrong': 'I need a water.', 'fix': 'I need a bottle of water.', 'alt': 'I need bottle of water.', 'why': 'Water is uncountable: use a bottle of.'}],
 'homework': 'Write 5 lines of a dialogue at a gas station: pump, amount, type of gas, extra item and total.',
 'homework_items': ['Write a 6-line gas station dialogue.', 'Record: “Regular, please.”', 'Practice numbers: 20, 22, 30, 40.', 'Review: Pump number… / Regular or premium?']}
