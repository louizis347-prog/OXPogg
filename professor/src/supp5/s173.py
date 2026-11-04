"""Suplemento Quest v5 · aula 173: At the drive-thru + regular Is it ready yet? (The Tale of Squirrel Nutkin)."""
SUPP = {
 'reg': 194,
 'badge': {'icon': '🚗', 'name': 'Drive-Thru Pro', 'desc': 'Order a meal from your car: drink, side, extra and pay'},
 'culture': {
  'hook': 'A drive-thru lets you order food from your car. In the USA, it is very common: you talk to a speaker, pay at one window and pick up your food at the next.',
  'mythfact': [
   {'s': 'At a drive-thru, you stay in your car.', 'ans': True, 'why': 'You order, pay and get your food from the car window.'},
   {'s': 'You order at the first window, not at a speaker.', 'ans': False, 'why': 'Usually you talk first to a speaker or a screen, then you drive to the windows.'},
   {'s': 'Staff often ask, “Anything else?” at the end of an order.', 'ans': True, 'why': 'It is a normal question before the price.'},
   {'s': 'A “meal” at a fast food place is only a sandwich.', 'ans': False, 'why': 'A meal usually has a sandwich, fries and a drink.'},
   {'s': '“The Tale of Squirrel Nutkin” is a children’s book by Beatrix Potter.', 'ans': True, 'why': 'It is from 1903.'}],
  'wild': [
   {'kind': 'Drive-thru menu board', 'lines': ['**Cheeseburger meal** $8.50', 'Small / Medium / Large drink', 'Extra sauce $0.50'], 'decode': {'q': 'How much is the cheeseburger meal?', 'opts': ['$8.50', '$0.50', '$5.80'], 'ans': 0, 'why': 'The board says $8.50.'}},
   {'kind': 'Sign at the drive-thru lane', 'lines': ['**Order here**', 'Please wait for the speaker.', 'Pay at window 1 · Pick up at window 2'], 'decode': {'q': 'Where do you pay?', 'opts': ['At window 1', 'At the speaker', 'At window 3'], 'ans': 0, 'why': 'The sign says “Pay at window 1.”'}}],
  'compare': {'br': 'In Brazil, drive-thru lanes also exist at fast food places, but many people still go inside, order at the counter or use delivery.', 'us': 'In the USA, many people use the drive-thru every day. Orders are short, and the staff speak fast.', 'tip': 'Say: “A cheeseburger meal, please.”', 'ask': 'What do you order at a fast food place? Say it in English.'},
  'quiz': [
   {'q': 'The staff ask, “What size drink?” You say…', 'opts': ['Medium, with cola.', 'Yes, with cola.', 'Cola is a medium.'], 'ans': 0, 'why': 'Say the size first.'},
   {'q': 'You want one more thing. You say…', 'opts': ['An apple pie, too.', 'Too apple pie.', 'I am apple pie.'], 'ans': 0, 'why': 'Too goes at the end.'},
   {'q': '“Pull forward” means…', 'opts': ['drive to the next window', 'park and walk', 'turn off the car'], 'ans': 0, 'why': 'The staff want you to move your car to the window.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Lunch from the car',
  'text': [
   'Bo lives in **Phoenix**. It is lunch time, and he is very hungry. He drives to a **fast food** restaurant and stops at the drive-thru. The sun is hot, and there are four cars in the line. A voice comes from the speaker.',
   '“**Welcome! What can I get you?**” “**Hi. A cheeseburger meal, please.**” “**What size drink?**” “**Medium, with cola.**” “**Any sides? Fries or salad?**” “**Fries, please.**”',
   '“**Anything else?**” “**An apple pie, too.**” “**That’s nine fifty. Pull forward.**” Bo drives to the window and pays. Kai gives him a bag with a straw, napkins and ketchup.',
   'At the next window, Bo asks, “**Is it ready yet?**” Kai smiles. “**It’s already ready!**” Bo thinks about “The Tale of Squirrel Nutkin.” It is a children’s book by Beatrix Potter from 1903. Nutkin is a cheeky squirrel, and he is never patient. Today Bo is not patient, too.',
   'He parks under a tree and opens the bag. The fries are **piping hot**. Bo takes a big bite of the burger and smiles. It is a small lunch, but a good one.'],
  'glossary': [{'w': 'drive-thru', 'pt': 'drive-thru (atendimento no carro)'}, {'w': 'speaker', 'pt': 'alto-falante'}, {'w': 'meal', 'pt': 'combo, refeição'}, {'w': 'size', 'pt': 'tamanho'}, {'w': 'sides', 'pt': 'acompanhamentos'}, {'w': 'fries', 'pt': 'batata frita'}, {'w': 'straw', 'pt': 'canudo'}, {'w': 'napkins', 'pt': 'guardanapos'}, {'w': 'squirrel', 'pt': 'esquilo'}, {'w': 'patient', 'pt': 'paciente'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A man orders lunch at a drive-thru', 'A man cooks fries at home', 'A woman buys a car'], 'ans': 0, 'why': 'Bo orders a meal from his car.'},
  'scan': [{'q': 'What size is the drink?', 'ans': 'medium', 'alt': ['a medium']}, {'q': 'What does Bo order for dessert?', 'ans': 'an apple pie', 'alt': ['apple pie', 'a pie']}, {'q': 'How much is the order?', 'ans': 'nine fifty', 'alt': ['$9.50', '9.50', 'nine dollars fifty']}],
  'tf': [{'s': 'Bo gets out of the car to order.', 'ans': False, 'why': 'He orders from the car.'}, {'s': 'Bo orders fries.', 'ans': True, 'why': '“Fries, please.”'}, {'s': 'The order is ready.', 'ans': True, 'why': 'Kai says, “It’s already ready!”'}, {'s': 'Bo eats the lunch in the restaurant.', 'ans': False, 'why': 'He parks under a tree and eats there.'}],
  'order': ['Bo stops at the drive-thru.', 'He orders a cheeseburger meal.', 'He asks for an apple pie, too.', 'Kai says the price.', 'Bo eats under a tree.'],
  'ctx': [{'sent': 'The sun is hot, and there are four cars in the line. A voice comes from the speaker.', 'w': 'speaker', 'opts': ['a box that makes sound', 'a person at home', 'a kind of food'], 'ans': 0, 'why': 'A speaker plays sound.'}, {'sent': 'Kai gives him a straw.', 'w': 'straw', 'opts': ['a thin tube for a drink', 'a small plate', 'a paper bag'], 'ans': 0, 'why': 'You use a straw to drink.'}, {'sent': 'Nutkin is never patient.', 'w': 'patient', 'opts': ['good at waiting', 'very tall', 'very loud'], 'ans': 0, 'why': 'Patient = can wait calmly.'}],
  'chunkHunt': ['What can I get you?', 'Medium, with cola.', 'Fries, please.', 'Is it ready yet?'],
  'think': 'Do you like fast food? What do you usually order?'},
 'convo': {'npc': {'name': 'Kai'}, 'story': 'You are in your car at a drive-thru in Phoenix. Kai works at the speaker. Order your lunch.', 'turns': [
  {'npc': 'Welcome! What can I get you?', 'pt': 'Bem-vindo! O que vai querer?', 'opts': [
   {'en': 'Hi. A cheeseburger meal, please.', 'pt': 'Oi. Um combo de cheeseburger, por favor.', 'ok': True, 'fb': 'Clear order with please.'},
   {'en': 'Hi. I want cheeseburger.', 'pt': 'Oi. Eu quero cheeseburger.', 'ok': False, 'fb': 'Better: A cheeseburger meal, please.'},
   {'en': 'Welcome! Thank you!', 'pt': 'Bem-vindo! Obrigado!', 'ok': False, 'fb': 'Kai is the one who welcomes you.'}]},
  {'npc': 'What size drink?', 'pt': 'Que tamanho de bebida?', 'opts': [
   {'en': 'Yes, I have a drink.', 'pt': 'Sim, eu tenho uma bebida.', 'ok': False, 'fb': 'He asks about size.'},
   {'en': 'Fries, please.', 'pt': 'Fritas, por favor.', 'ok': False, 'fb': 'That is for the side question.'},
   {'en': 'Medium, with cola.', 'pt': 'Médio, com cola.', 'ok': True, 'fb': 'Size + drink.'}]},
  {'npc': 'Any sides? Fries or salad?', 'pt': 'Algum acompanhamento? Fritas ou salada?', 'opts': [
   {'en': 'Medium, please.', 'pt': 'Médio, por favor.', 'ok': False, 'fb': 'You already said the size.'},
   {'en': 'Yes, I am fries.', 'pt': 'Sim, eu sou fritas.', 'ok': False, 'fb': 'You choose fries, you are not fries.'},
   {'en': 'Fries, please.', 'pt': 'Fritas, por favor.', 'ok': True, 'fb': 'Short and polite.'}]},
  {'npc': 'Anything else?', 'pt': 'Mais alguma coisa?', 'opts': [
   {'en': 'An apple pie, too.', 'pt': 'Uma torta de maçã também.', 'ok': True, 'fb': 'Adds one more item.'},
   {'en': 'Pull forward, please.', 'pt': 'Siga em frente, por favor.', 'ok': False, 'fb': 'That is what Kai says.'},
   {'en': 'No, I am else.', 'pt': 'Não, eu sou outro.', 'ok': False, 'fb': 'Say: No, that’s all.'}]},
  {'npc': 'That’s nine fifty. Pull forward.', 'pt': 'São nove e cinquenta. Siga em frente.', 'opts': [
   {'en': 'Welcome! What can I get you?', 'pt': 'Bem-vindo! O que vai querer?', 'ok': False, 'fb': 'That is Kai’s first line.'},
   {'en': 'Okay. Thank you!', 'pt': 'Certo. Obrigado!', 'ok': True, 'fb': 'Natural end of the order.'},
   {'en': 'Yes, a cheeseburger meal.', 'pt': 'Sim, um combo de cheeseburger.', 'ok': False, 'fb': 'You already ordered it.'}]}]},
 'errors': [
  {'wrong': 'I want a cheeseburger meal.', 'fix': 'A cheeseburger meal, please.', 'alt': 'I wants a cheeseburger meal.', 'why': 'At a counter, a short order with please sounds more natural.'},
  {'wrong': 'A drink size medium.', 'fix': 'A medium drink.', 'alt': 'A drink medium.', 'why': 'The size goes before the noun: a medium drink.'},
  {'wrong': 'Fries too, please.', 'fix': 'Fries, please.', 'alt': 'Fries are please.', 'why': 'Say the item and please. Too goes at the end for “also”.'},
  {'wrong': 'It is ready already?', 'fix': 'Is it ready yet?', 'alt': 'Is it yet ready?', 'why': 'In questions, use yet at the end.'}],
 'homework': 'Write a short drive-thru order: a burger, a small drink and fries.',
 'homework_items': ['Write your own fast food order.', 'Say aloud: A cheeseburger meal, please.', 'Listen to the dialogue and shadow Kai.', 'Review: small / medium / large.']}
