"""Suplemento Quest v5 · aula 63: Apartment tour + regular My New Apartment (Rear Window)."""
SUPP = {
 'reg': 92,
 'badge': {'icon': '🏠', 'name': 'Apartment Hunter', 'desc': 'Take an apartment tour and ask about rooms'},
 'culture': {
  'hook': 'Looking for an apartment is exciting. On a tour, the agent shows you each room, and you can ask simple questions about the kitchen, the bedroom and the windows.',
  'mythfact': [
   {'s': 'In the USA, a “one-bedroom” apartment has one bedroom.', 'ans': True, 'why': 'The number tells you how many bedrooms there are. The living room and kitchen are extra.'},
   {'s': 'A “studio” has a separate bedroom.', 'ans': False, 'why': 'A studio is one main room with a small bathroom, and the bed is in the same room.'},
   {'s': 'Many apartments in the USA come with a stove in the kitchen.', 'ans': True, 'why': 'A stove is common, and many places also have a fridge.'},
   {'s': 'You can often ask to see an apartment before you rent it.', 'ans': True, 'why': 'A tour is normal. You can ask questions during the visit.'},
   {'s': '“Rear Window” is a film by Alfred Hitchcock.', 'ans': True, 'why': 'It is a 1954 film about a man who watches his neighbors from his window.'}],
  'wild': [
   {'kind': 'Apartment ad', 'lines': ['**2 bedrooms, 1 bathroom**', 'New kitchen · Big windows', 'Balcony · $1,400 / month'], 'decode': {'q': 'How many bedrooms are there?', 'opts': ['Two', 'One', 'Four'], 'ans': 0, 'why': '“2 bedrooms.”'}},
   {'kind': 'Door sign', 'lines': ['**Apartment tour today**', '2 p.m. – 4 p.m.', 'Please knock and come in'], 'decode': {'q': 'When can you visit today?', 'opts': ['From 2 to 4 p.m.', 'At night', 'Before 9 a.m.'], 'ans': 0, 'why': '“2 p.m. – 4 p.m.”'}}],
  'compare': {'br': 'In Brazil, people often say “quarto” and “sala” when they describe a flat, and many apartments come without a stove.', 'us': 'In the USA, ads say “1 bed, 1 bath”, and the stove and fridge often come with the apartment.', 'tip': 'Ask: “How many bedrooms are there?”', 'ask': 'Describe your home in English: kitchen, bedroom, bathroom.'},
  'quiz': [
   {'q': 'You want to know about the kitchen. You ask…', 'opts': ['Is there a kitchen?', 'There is kitchen?', 'Have a kitchen?'], 'ans': 0, 'why': 'Is there a…? asks if something exists.'},
   {'q': '“It’s down the hall.” It means…', 'opts': ['it is along the corridor', 'it is on the roof', 'it is very far away'], 'ans': 0, 'why': 'Down the hall = along the corridor.'},
   {'q': '“It’s yours!” is something you say when…', 'opts': ['someone can have the place', 'the place is closed', 'the place is dirty'], 'ans': 0, 'why': 'It means the place is for you.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Ruth’s new place',
  'text': [
   'Ruth is looking for a home in **Phoenix**. Today she has a tour of a small apartment. A man named Kai opens the door. “**Welcome! Let me show you the apartment.**”',
   '“**Thanks. It looks nice**,” Ruth says. “**This is the living room. It has a big window.**” Ruth sees a sofa and a tree outside. “**I like it. Is there a kitchen?**” “**Yes, it’s here. It has a new stove.**”',
   '“**And the bedroom?**” she asks. “**It’s down the hall, next to the bathroom.**” The bedroom is small, but it is quiet. “**Perfect. How many rooms are there?**” Kai says, “Three: the living room, the kitchen and the bedroom, plus the bathroom.”',
   'Ruth goes back to the window. She thinks of the film Rear Window. In the film, a man stays in his apartment and watches his neighbors across the yard. Ruth smiles. Her window looks at a quiet street, and that is better.',
   '“**Come back anytime. It’s yours!**” Kai says. Ruth takes a photo of the kitchen and says, “I want this place.” Tomorrow she signs the paper.'],
  'glossary': [{'w': 'apartment', 'pt': 'apartamento'}, {'w': 'living room', 'pt': 'sala de estar'}, {'w': 'window', 'pt': 'janela'}, {'w': 'stove', 'pt': 'fogão'}, {'w': 'bedroom', 'pt': 'quarto'}, {'w': 'bathroom', 'pt': 'banheiro'}, {'w': 'quiet', 'pt': 'silencioso'}, {'w': 'yard', 'pt': 'quintal, pátio'}, {'w': 'sofa', 'pt': 'sofá'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A woman sees an apartment', 'A man cooks dinner', 'A girl buys a car'], 'ans': 0, 'why': 'Ruth takes an apartment tour with Kai.'},
  'scan': [{'q': 'In which city is the apartment?', 'ans': 'Phoenix', 'alt': ['phoenix']}, {'q': 'What is new in the kitchen?', 'ans': 'the stove', 'alt': ['stove', 'a new stove']}, {'q': 'Where is the bedroom?', 'ans': 'next to the bathroom', 'alt': ['down the hall', 'down the hall, next to the bathroom']}],
  'tf': [{'s': 'The living room has a big window.', 'ans': True, 'why': '“It has a big window.”'}, {'s': 'The apartment does not have a kitchen.', 'ans': False, 'why': 'Kai says: “Yes, it’s here.”'}, {'s': 'The bedroom is next to the bathroom.', 'ans': True, 'why': '“Next to the bathroom.”'}, {'s': 'Ruth does not like the apartment.', 'ans': False, 'why': 'She says: “I want this place.”'}],
  'order': ['Kai opens the door.', 'Ruth sees the living room.', 'Kai shows the kitchen.', 'They look at the bedroom.', 'Kai says it is hers.'],
  'ctx': [{'sent': 'The bedroom is quiet.', 'w': 'quiet', 'opts': ['with little noise', 'very loud', 'very hot'], 'ans': 0, 'why': 'Quiet = not noisy.'}, {'sent': 'It has a new stove.', 'w': 'stove', 'opts': ['a kitchen machine for cooking', 'a window', 'a bed'], 'ans': 0, 'why': 'You cook on a stove.'}, {'sent': 'The yard is small.', 'w': 'yard', 'opts': ['a small outside space', 'a big car', 'a room'], 'ans': 0, 'why': 'A yard is an outside space near a building.'}],
  'chunkHunt': ['Let me show you the apartment.', 'It looks nice.', 'Is there a kitchen?', 'How many rooms are there?'],
  'think': 'What is your favorite room at home? Why?'},
 'convo': {'npc': {'name': 'Kai'}, 'story': 'You visit an apartment in Phoenix. Kai shows you around. Ask about the rooms.', 'turns': [
  {'npc': 'Welcome! Let me show you the apartment.', 'pt': 'Bem-vindo! Deixe-me mostrar o apartamento.', 'opts': [
   {'en': 'Thanks. It looks nice.', 'pt': 'Valeu. Parece bonito.', 'ok': True, 'fb': 'Polite and natural.'},
   {'en': 'Thanks. It is looking nice.', 'pt': 'Valeu. Está parecendo bonito.', 'ok': False, 'fb': 'Use it looks nice.'},
   {'en': 'Welcome to my apartment!', 'pt': 'Bem-vindo ao meu apartamento!', 'ok': False, 'fb': 'That is not your apartment.'}]},
  {'npc': 'This is the living room. It has a big window.', 'pt': 'Esta é a sala. Tem uma janela grande.', 'opts': [
   {'en': 'I like it. Is there a kitchen?', 'pt': 'Gostei. Tem cozinha?', 'ok': True, 'fb': 'Natural next question.'},
   {'en': 'I like. There is kitchen?', 'pt': 'Gosto. Tem cozinha?', 'ok': False, 'fb': 'Say I like it and Is there a kitchen?'},
   {'en': 'A kitchen is yours.', 'pt': 'Uma cozinha é sua.', 'ok': False, 'fb': 'Does not fit.'}]},
  {'npc': 'Yes, it’s here. It has a new stove.', 'pt': 'Tem, é aqui. Tem um fogão novo.', 'opts': [
   {'en': 'The bedroom is yes?', 'pt': 'O quarto é sim?', 'ok': False, 'fb': 'Ask: And the bedroom?'},
   {'en': 'And the bedroom?', 'pt': 'E o quarto?', 'ok': True, 'fb': 'Short and clear.'},
   {'en': 'I stove the bedroom.', 'pt': 'Eu fogão o quarto.', 'ok': False, 'fb': 'Wrong meaning.'}]},
  {'npc': 'It’s down the hall, next to the bathroom.', 'pt': 'Fica no corredor, ao lado do banheiro.', 'opts': [
   {'en': 'Perfect. How many rooms are there?', 'pt': 'Perfeito. Quantos cômodos tem?', 'ok': True, 'fb': 'Correct word order.'},
   {'en': 'Perfect. How many rooms have?', 'pt': 'Perfeito. Quantos cômodos têm?', 'ok': False, 'fb': 'Say: How many rooms are there?'},
   {'en': 'Down the hall is a stove.', 'pt': 'No corredor há um fogão.', 'ok': False, 'fb': 'It repeats the wrong idea.'}]},
  {'npc': 'Come back anytime. It’s yours!', 'pt': 'Volte quando quiser. É seu!', 'opts': [
   {'en': 'Thank you. I love it!', 'pt': 'Obrigado. Eu amo!', 'ok': False, 'fb': 'Good idea, but need it: I love it!'},
   {'en': 'Thanks! I want it.', 'pt': 'Valeu! Eu quero.', 'ok': True, 'fb': 'Natural reply to a good tour.'},
   {'en': 'Welcome! Let me show you.', 'pt': 'Bem-vindo! Deixe-me mostrar.', 'ok': False, 'fb': 'That is Kai’s line.'}]}]},
 'errors': [
  {'wrong': 'There is a kitchen?', 'fix': 'Is there a kitchen?', 'alt': 'Have a kitchen?', 'why': 'For questions, put is before there.'},
  {'wrong': 'How many rooms have?', 'fix': 'How many rooms are there?', 'alt': 'How many rooms is there?', 'why': 'Use are there with plural rooms.'},
  {'wrong': 'The bedroom is in the side of the bathroom.', 'fix': 'The bedroom is next to the bathroom.', 'alt': 'The bedroom is near of the bathroom.', 'why': 'Use next to for “ao lado de”.'},
  {'wrong': 'It have a big window.', 'fix': 'It has a big window.', 'alt': 'It haves a big window.', 'why': 'With it, use has.'}],
 'homework': 'Draw your home and write 5 sentences: This is the… It has…',
 'homework_items': ['Write the names of 6 rooms or things in your home.', 'Say aloud: Is there a kitchen?', 'Listen to the dialogue and shadow Kai.', 'Describe one room: It has a big window.']}
