"""Suplemento Quest v5 · aula 67: In my kitchen + regular Room on the Fifth Floor (Home, Sweet Home)."""
SUPP = {
 'reg': 68,
 'badge': {'icon': '🍳', 'name': 'Kitchen Helper', 'desc': 'Offer help, ask where things are and understand places in a kitchen'},
 'culture': {
  'hook': 'When you help in a friend\'s kitchen, you ask short questions: where are the forks, where is the salt? Place words like in, on and under make it easy.',
  'mythfact': [
   {'s': 'Denver is a city in the state of Colorado.', 'ans': True, 'why': 'Denver is the capital of Colorado.'},
   {'s': 'In English, a glass is a kind of table.', 'ans': False, 'why': 'A glass is a cup for drinks. A table is furniture.'},
   {'s': 'Guests often offer to help in the kitchen.', 'ans': True, 'why': 'It is polite to say, “Can I help?”'},
   {'s': '“Make yourself at home” means the host wants you to feel comfortable.', 'ans': True, 'why': 'It is a friendly, common phrase.'},
   {'s': 'In English, you say “in the drawer” and “on the shelf”.', 'ans': True, 'why': 'A drawer is a closed space, so we use in; a shelf is a flat surface, so we use on.'}],
  'wild': [
   {'kind': 'Kitchen notes', 'lines': ['**Forks**: top drawer, left', '**Plates**: cabinet over the sink', '**Salt**: shelf by the stove'], 'decode': {'q': 'Where are the plates?', 'opts': ['In the cabinet over the sink', 'In the top drawer', 'On the shelf'], 'ans': 0, 'why': 'The note says: Plates, cabinet over the sink.'}},
   {'kind': 'Oven label', 'lines': ['**CAUTION**: HOT', 'Do not touch the door', 'Use oven gloves'], 'decode': {'q': 'What should you use?', 'opts': ['Oven gloves', 'Your hands', 'A plate'], 'ans': 0, 'why': '“Use oven gloves.”'}}],
  'compare': {'br': 'In Brazil, a guest often helps with the dishes after a meal, and the host may say no at first.', 'us': 'In the USA, a guest says “Can I help?” and the host often says “Sure” or “No, relax!”. Both answers are polite.', 'tip': 'Offer once: “Can I help you in the kitchen?”', 'ask': 'Where do you keep your forks at home? Say it in English.'},
  'quiz': [
   {'q': 'You want to help your friend. You say…', 'opts': ['Can I help you in the kitchen?', 'I am helping the kitchen.', 'Kitchen, you, help?'], 'ans': 0, 'why': 'Can I help you…? is a polite offer.'},
   {'q': '“It\'s under the stove.” Where is the pan?', 'opts': ['Below the stove', 'On the stove', 'Next to the window'], 'ans': 0, 'why': 'Under = below.'},
   {'q': 'You want the salt. You ask…', 'opts': ['Where is the salt?', 'Where are the salt?', 'Salt is where?'], 'ans': 0, 'why': 'Salt is singular, so use is.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Dinner at Tara\'s',
  'text': [
   'Sunday evening in **Denver**. Tara has a small, **cozy** kitchen. Her friend Jonah comes for dinner. Tara says, “**Make yourself at home**.” The kitchen smells like garlic and fresh bread.',
   '“**Can I help you in the kitchen?**” Jonah asks. “**Sure. Get a plate from the cabinet**,” Tara says. He takes two plates. “**Where are the forks?**” “**In the drawer, on the left.**” Jonah opens the drawer and finds forks, spoons and knives.',
   'Tara wants to cook pasta. “**Do you have a big pan?**” Jonah asks. “**Yes, it\'s under the stove**,” she says. He puts water in the pan and puts it on the stove. Tara boils water in the kettle for tea.',
   '“**Where is the salt?**” Jonah asks. “**It\'s on the shelf**,” she says. He adds a little salt to the water. Tara smiles. “**Help yourself** to some bread,” she says. “**You\'re too kind**,” Jonah says.',
   'The pasta is ready. They sit at the table. Jonah thinks of the song “Home, Sweet Home.” It says there is no place like home. “Your kitchen is **cozy**,” he says. “Thanks! Come back soon,” says Tara. Then they eat.'],
  'glossary': [{'w': 'cozy', 'pt': 'aconchegante'}, {'w': 'cabinet', 'pt': 'armário'}, {'w': 'drawer', 'pt': 'gaveta'}, {'w': 'stove', 'pt': 'fogão'}, {'w': 'shelf', 'pt': 'prateleira'}, {'w': 'kettle', 'pt': 'chaleira'}, {'w': 'boils', 'pt': 'ferve'}, {'w': 'pan', 'pt': 'panela'}, {'w': 'garlic', 'pt': 'alho'}],
  'fast': {'q': 'What is this story about?', 'opts': ['Helping a friend in the kitchen', 'Buying a new stove', 'A trip to Denver'], 'ans': 0, 'why': 'Jonah helps Tara cook dinner.'},
  'scan': [{'q': 'Where are the forks?', 'ans': 'in the drawer', 'alt': ['drawer', 'in the drawer, on the left', 'on the left']}, {'q': 'Where is the big pan?', 'ans': 'under the stove', 'alt': ['under the stove.']}, {'q': 'Where is the salt?', 'ans': 'on the shelf', 'alt': ['shelf']}],
  'tf': [{'s': 'Jonah and Tara are friends.', 'ans': True, 'why': 'Tara calls Jonah her friend.'}, {'s': 'The plates are in the drawer.', 'ans': False, 'why': 'The plates are in the cabinet.'}, {'s': 'Tara makes tea.', 'ans': True, 'why': 'She boils water in the kettle for tea.'}, {'s': 'The salt is under the stove.', 'ans': False, 'why': 'The salt is on the shelf.'}],
  'order': ['Jonah comes for dinner.', 'He gets two plates from the cabinet.', 'He finds the forks in the drawer.', 'He puts water in the pan.', 'They sit and eat pasta.'],
  'ctx': [{'sent': 'Tara has a cozy kitchen.', 'w': 'cozy', 'opts': ['small, warm and nice', 'very cold', 'very dirty'], 'ans': 0, 'why': 'Cozy = warm and comfortable.'}, {'sent': 'Help yourself to some bread.', 'w': 'Help yourself', 'opts': ['take what you want', 'call a doctor', 'go away'], 'ans': 0, 'why': 'Help yourself = take it, it is free for you.'}, {'sent': 'Tara boils water for tea.', 'w': 'boils', 'opts': ['heats water until it bubbles', 'freezes water', 'drinks water'], 'ans': 0, 'why': 'Boil = heat water until it is very hot.'}],
  'chunkHunt': ['Can I help you in the kitchen?', 'Where are the forks?', 'Do you have a big pan?', 'It\'s on the shelf.'],
  'think': 'What is on the shelf in your kitchen? Say two things with “on the shelf”.'},
 'convo': {'npc': {'name': 'Tara'}, 'story': 'You visit your friend Tara in Denver. She is cooking dinner. Offer to help and ask where things are.', 'turns': [
  {'npc': 'Welcome! Make yourself at home. I\'m cooking dinner.', 'pt': 'Bem-vindo! Fique à vontade. Estou fazendo o jantar.', 'opts': [
   {'en': 'Can I help you in the kitchen?', 'pt': 'Posso ajudar você na cozinha?', 'ok': True, 'fb': 'A polite offer to help.'},
   {'en': 'I am home yesterday.', 'pt': 'Eu estou em casa ontem.', 'ok': False, 'fb': 'It does not fit the situation.'},
   {'en': 'I help the kitchen.', 'pt': 'Eu ajudo a cozinha.', 'ok': False, 'fb': 'Say help you in the kitchen.'}]},
  {'npc': 'Sure. Get a plate from the cabinet.', 'pt': 'Claro. Pegue um prato no armário.', 'opts': [
   {'en': 'The plate is a cabinet.', 'pt': 'O prato é um armário.', 'ok': False, 'fb': 'It mixes the words.'},
   {'en': 'Okay. Where are the forks?', 'pt': 'Certo. Onde ficam os garfos?', 'ok': True, 'fb': 'Asks about the next thing.'},
   {'en': 'Where is the forks?', 'pt': 'Onde está os garfos?', 'ok': False, 'fb': 'Forks is plural: where are.'}]},
  {'npc': 'In the drawer, on the left.', 'pt': 'Na gaveta, à esquerda.', 'opts': [
   {'en': 'Do you have a big pan?', 'pt': 'Você tem uma panela grande?', 'ok': True, 'fb': 'Natural next question.'},
   {'en': 'You have a pan big?', 'pt': 'Você tem uma panela grande?', 'ok': False, 'fb': 'Adjective goes before the noun.'},
   {'en': 'I am on the left.', 'pt': 'Eu estou à esquerda.', 'ok': False, 'fb': 'It does not answer.'}]},
  {'npc': 'Yes, it\'s under the stove.', 'pt': 'Sim, fica embaixo do fogão.', 'opts': [
   {'en': 'Thanks. Where is the salt?', 'pt': 'Valeu. Onde está o sal?', 'ok': True, 'fb': 'Thanks and a new question.'},
   {'en': 'The stove is under me.', 'pt': 'O fogão está embaixo de mim.', 'ok': False, 'fb': 'It does not make sense.'},
   {'en': 'Thanks. Where are the salt?', 'pt': 'Valeu. Onde estão o sal?', 'ok': False, 'fb': 'Salt is singular: where is.'}]},
  {'npc': 'It\'s on the shelf. Enjoy cooking!', 'pt': 'Está na prateleira. Bom cozinhar!', 'opts': [
   {'en': 'Thank you. Your kitchen is cozy!', 'pt': 'Obrigado. Sua cozinha é aconchegante!', 'ok': True, 'fb': 'A kind compliment.'},
   {'en': 'It is in shelf.', 'pt': 'Está em prateleira.', 'ok': False, 'fb': 'Say on the shelf.'},
   {'en': 'I cook you yesterday.', 'pt': 'Eu cozinho você ontem.', 'ok': False, 'fb': 'It does not make sense.'}]}]},
 'errors': [
  {'wrong': 'Where is the forks?', 'fix': 'Where are the forks?', 'alt': 'Where the forks are?', 'why': 'Forks is plural, so use are. In questions, the verb comes first.'},
  {'wrong': 'The salt is in the shelf.', 'fix': 'The salt is on the shelf.', 'alt': 'The salt is at the shelf.', 'why': 'A shelf is a flat surface, so use on.'},
  {'wrong': 'Do you have a pan big?', 'fix': 'Do you have a big pan?', 'alt': 'Have you a pan big?', 'why': 'In English, the adjective goes before the noun.'},
  {'wrong': 'The pan is below of the stove.', 'fix': 'The pan is under the stove.', 'alt': 'The pan is under of the stove.', 'why': 'Say under the stove, with no of.'}],
 'homework': 'Describe your kitchen in 4 sentences: where are the plates, the forks, the salt and the pan?',
 'homework_items': ['Say where 3 things are in your kitchen.', 'Write: Where is / Where are… 3 times.', 'Listen to the dialogue again and shadow Jonah.', 'Review: in the drawer / on the shelf / under the stove.']}
