"""Suplemento Quest v5 · aula 144: Museums in D.C. + regular Where's the Restroom? (Around the World in Eighty Days)."""
SUPP = {
 'reg': 23,
 'badge': {'icon': '🦖', 'name': 'Museum Explorer', 'desc': 'Get in, find the dinosaurs and ask about photos'},
 'culture': {
  'hook': 'Many famous museums in Washington, D.C. are free. You walk in, take a map, find the dinosaurs or the paintings, and ask the staff when you need help.',
  'mythfact': [
   {'s': 'Many big museums in Washington, D.C. are free to enter.', 'ans': True, 'why': 'The Smithsonian museums on the National Mall have free admission.'},
   {'s': 'You can always use a flash in a museum.', 'ans': False, 'why': 'Many museums say “no flash” because strong light can hurt old objects.'},
   {'s': 'Museum staff can tell you where things are.', 'ans': True, 'why': 'Ask at the information desk or ask a guard.'},
   {'s': 'Every special exhibit in a museum is free.', 'ans': False, 'why': 'Some special shows ask for a paid ticket, even in a free museum.'},
   {'s': 'You can touch every object in a museum.', 'ans': False, 'why': 'Usually you look with your eyes. Look for a “Please touch” sign.'}],
  'wild': [
   {'kind': 'Museum sign', 'lines': ['**Free admission**', 'No flash photography', 'Open 10 a.m. – 5:30 p.m.'], 'decode': {'q': 'What is not allowed?', 'opts': ['Flash photography', 'Walking', 'Looking at art'], 'ans': 0, 'why': 'The sign says: no flash photography.'}},
   {'kind': 'Museum map note', 'lines': ['**Dinosaurs**: Floor 1, left', 'Gift shop: Floor 1, right', 'Cafe: Floor 2'], 'decode': {'q': 'Where is the cafe?', 'opts': ['On the second floor', 'On the first floor, left', 'Outside'], 'ans': 0, 'why': 'The map says the cafe is on floor 2.'}}],
  'compare': {'br': 'In Brazil, many museums charge a small fee, and some are free on certain days.', 'us': 'In Washington, D.C., the Smithsonian museums are free every day, though special shows may cost money.', 'tip': 'Ask: “Is it free?”', 'ask': 'What is your favorite museum? Say it in English.'},
  'quiz': [
   {'q': 'You want tickets for two adults. You say…', 'opts': ['Two adults, please.', 'Two adult, please.', 'For two adults I want.'], 'ans': 0, 'why': 'Use the plural: two adults.'},
   {'q': 'You want to find the dinosaurs. You ask…', 'opts': ['Where are the dinosaurs?', 'Where is the dinosaurs?', 'Where the dinosaurs are?'], 'ans': 0, 'why': 'Dinosaurs is plural, so use are.'},
   {'q': '“No flash” means…', 'opts': ['Do not use the camera light', 'Do not take any photo', 'Do not run'], 'ans': 0, 'why': 'You can take photos, but without the flash light.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Dinosaurs on the first floor',
  'text': [
   'Ana and her son Leo are in **Washington, D.C.** It rains, so they go to a big museum. Leo is eight years old. He loves one thing more than anything: dinosaurs.',
   '“**Welcome to the museum! How many?**” a man asks. “**Two adults, please**,” Ana says. “**It’s free today**,” the man says. “**Really? That’s great!**” The man gives Ana a paper. “**Here’s a map.**”',
   'Leo asks, “**Where are the dinosaurs?**” “**On the first floor, to the left**,” the man says. Ana thinks about “Around the World in Eighty Days.” In that book, Phileas Fogg is always in a hurry. “Today we are not in a hurry,” she says. “We have all day.”',
   'They find a huge skeleton. It is a long dinosaur with big bones and sharp teeth. Leo looks up for a long time. “It is bigger than our house!” he says. A guard smiles at him.',
   '“**Can we take photos?**” Ana asks the guard. “**Yes, but no flash**,” he says. Ana takes one photo of Leo and the dinosaur. Then they go to the second floor to look at old paintings. Leo likes the bones more.'],
  'glossary': [{'w': 'paintings', 'pt': 'quadros'}, {'w': 'free', 'pt': 'grátis'}, {'w': 'map', 'pt': 'mapa'}, {'w': 'dinosaurs', 'pt': 'dinossauros'}, {'w': 'skeleton', 'pt': 'esqueleto'}, {'w': 'bones', 'pt': 'ossos'}, {'w': 'guard', 'pt': 'segurança, guarda'}, {'w': 'flash', 'pt': 'flash'}, {'w': 'huge', 'pt': 'enorme'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A mother and son visit a museum', 'A man buys a car', 'A girl makes a cake'], 'ans': 0, 'why': 'Ana and Leo see dinosaurs at the museum.'},
  'scan': [{'q': 'How much is it today?', 'ans': 'free', 'alt': ['it is free', 'nothing']}, {'q': 'Where are the dinosaurs?', 'ans': 'on the first floor', 'alt': ['first floor', 'first floor to the left']}, {'q': 'What is not allowed for photos?', 'ans': 'flash', 'alt': ['the flash', 'no flash']}],
  'tf': [{'s': 'Ana and Leo pay a lot for tickets.', 'ans': False, 'why': 'It is free today.'}, {'s': 'The man gives Ana a map.', 'ans': True, 'why': '“Here’s a map.”'}, {'s': 'Leo likes dinosaurs.', 'ans': True, 'why': 'It is his favorite thing.'}, {'s': 'The guard says they can use the flash.', 'ans': False, 'why': 'He says: no flash.'}],
  'order': ['Ana asks for two adult tickets.', 'The man gives her a map.', 'Leo asks where the dinosaurs are.', 'They see the huge skeleton.', 'Ana takes a photo without flash.'],
  'ctx': [{'sent': 'It is a huge skeleton.', 'w': 'huge', 'opts': ['very big', 'very small', 'very old'], 'ans': 0, 'why': 'Huge = very big.'}, {'sent': 'A guard stands near the door.', 'w': 'guard', 'opts': ['a person who watches the place', 'a tour bus', 'a ticket machine'], 'ans': 0, 'why': 'A guard keeps the museum safe.'}, {'sent': 'Dinosaurs have big bones.', 'w': 'bones', 'opts': ['the hard parts inside the body', 'the skin', 'the teeth of a cat'], 'ans': 0, 'why': 'Bones are the hard parts of a skeleton.'}],
  'chunkHunt': ['Two adults, please.', 'It’s free today.', 'Where are the dinosaurs?', 'Yes, but no flash.'],
  'think': 'What do you like to see in a museum: dinosaurs, paintings or something else?'},
 'convo': {'npc': {'name': 'Ethan'}, 'story': 'You arrive at a museum in Washington, D.C. Ethan works at the entrance.', 'turns': [
  {'npc': 'Welcome to the museum! How many?', 'pt': 'Bem-vindos ao museu! Quantos?', 'opts': [
   {'en': 'Two adults, please.', 'pt': 'Dois adultos, por favor.', 'ok': True, 'fb': 'Short and clear.'},
   {'en': 'Two adult, please.', 'pt': 'Dois adulto, por favor.', 'ok': False, 'fb': 'Use the plural: adults.'},
   {'en': 'We are two the adults.', 'pt': 'Nós somos dois os adultos.', 'ok': False, 'fb': 'Wrong structure.'}]},
  {'npc': 'It’s free today.', 'pt': 'Hoje é de graça.', 'opts': [
   {'en': 'Really? That’s great!', 'pt': 'Sério? Que ótimo!', 'ok': True, 'fb': 'Natural reaction.'},
   {'en': 'Really? That great!', 'pt': 'Sério? Isso ótimo!', 'ok': False, 'fb': 'Say: That’s great.'},
   {'en': 'Really? I am free.', 'pt': 'Sério? Eu estou livre.', 'ok': False, 'fb': 'Wrong meaning.'}]},
  {'npc': 'Here’s a map.', 'pt': 'Aqui está um mapa.', 'opts': [
   {'en': 'Where is the dinosaurs?', 'pt': 'Onde fica os dinossauros?', 'ok': False, 'fb': 'Dinosaurs is plural: Where are…?'},
   {'en': 'Where are the dinosaurs?', 'pt': 'Onde ficam os dinossauros?', 'ok': True, 'fb': 'Correct plural question.'},
   {'en': 'Where the dinosaurs are?', 'pt': 'Onde os dinossauros estão?', 'ok': False, 'fb': 'In a question, put Where are first.'}]},
  {'npc': 'On the first floor, to the left.', 'pt': 'No primeiro andar, à esquerda.', 'opts': [
   {'en': 'Can we take photos?', 'pt': 'Podemos tirar fotos?', 'ok': True, 'fb': 'Good question for a museum.'},
   {'en': 'Can we make photos?', 'pt': 'Podemos fazer fotos?', 'ok': False, 'fb': 'We take photos in English.'},
   {'en': 'We can to take photos?', 'pt': 'Nós podemos tirar fotos?', 'ok': False, 'fb': 'Use Can we take…?'}]},
  {'npc': 'Yes, but no flash.', 'pt': 'Sim, mas sem flash.', 'opts': [
   {'en': 'No flash, no problem. Thanks!', 'pt': 'Sem flash, sem problema. Obrigado!', 'ok': True, 'fb': 'Polite and natural.'},
   {'en': 'No flash is yes.', 'pt': 'Sem flash é sim.', 'ok': False, 'fb': 'It does not make sense.'},
   {'en': 'I am flash, thanks.', 'pt': 'Eu sou flash, obrigado.', 'ok': False, 'fb': 'Wrong meaning.'}]}]},
 'errors': [
  {'wrong': 'Two adult, please.', 'fix': 'Two adults, please.', 'alt': 'Two of adults, please.', 'why': 'After two, use a plural noun: adults.'},
  {'wrong': 'Where is the dinosaurs?', 'fix': 'Where are the dinosaurs?', 'alt': 'Where the dinosaurs is?', 'why': 'Dinosaurs is plural, so use are.'},
  {'wrong': 'Can we make photos?', 'fix': 'Can we take photos?', 'alt': 'Can we do photos?', 'why': 'In English you take a photo.'},
  {'wrong': 'It is free today? Really?', 'fix': 'Really? That’s great!', 'alt': 'Really? That great!', 'why': 'Answer a surprise with: Really? That’s great!'}],
 'homework': 'Write a short dialogue: you arrive at a museum, ask for two tickets, and ask where an exhibit is.',
 'homework_items': ['Write 3 things you can see in a museum.', 'Say aloud: Where are the dinosaurs?', 'Listen to the dialogue and shadow Ethan.', 'Review: on the first floor / to the left.']}
