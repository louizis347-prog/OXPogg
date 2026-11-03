"""Suplemento Quest v5 · aula 64: A room for rent + regular Room on the Fifth Floor (Home, Sweet Home)."""
SUPP = {
 'reg': 7,
 'badge': {'icon': '🛏️', 'name': 'Room Finder', 'desc': 'Ask about a room for rent: price, bills and visit time'},
 'culture': {
  'hook': 'In big cities, many people share a flat and rent only one room. Before you visit, you call or write and ask the same short questions: price, bills and time.',
  'mythfact': [
   {'s': 'In the USA, rent is usually paid every month.', 'ans': True, 'why': 'Monthly rent is the normal way, and many people pay on the first day of the month.'},
   {'s': '“Bills” can mean water, electricity and internet.', 'ans': True, 'why': 'Bills are the regular payments for home services.'},
   {'s': 'A roommate is a person who shares your home.', 'ans': True, 'why': 'Roommates share a flat or house and often split the rent.'},
   {'s': 'Brooklyn is a city in California.', 'ans': False, 'why': 'Brooklyn is a part of New York City.'},
   {'s': '“Home, Sweet Home” is a song about the love of a home.', 'ans': True, 'why': 'The words are by John Howard Payne, from 1823.'}],
  'wild': [
   {'kind': 'Room ad', 'lines': ['**Room for rent** in Brooklyn', '$800 / month · Water and Wi-Fi included', 'Call Cole: 555-0142'], 'decode': {'q': 'What is NOT included?', 'opts': ['Electricity', 'Water', 'Wi-Fi'], 'ans': 0, 'why': 'Only water and Wi-Fi are listed.'}},
   {'kind': 'Text message', 'lines': ['Hi! Is the room still available?', 'Can I see it tomorrow at 5?', 'Thanks, Ava'], 'decode': {'q': 'When does Ava want to see the room?', 'opts': ['Tomorrow at 5', 'Today at 5', 'Tomorrow at 8'], 'ans': 0, 'why': '“tomorrow at 5”.'}}],
  'compare': {'br': 'In Brazil, people often say “aluguel” and the building fee can be part of it, and the “república” is a shared house for students.', 'us': 'In the USA, rent and bills are often separate, and you ask what is included. Many people live with roommates.', 'tip': 'Ask: “How much is the rent? Are bills included?”', 'ask': 'How much do people pay for a room in your city? Say it in English.'},
  'quiz': [
   {'q': 'You want to know if the room is free to rent. You ask…', 'opts': ['Is it still available?', 'It is available still?', 'Has it available?'], 'ans': 0, 'why': 'Is it still available? is a natural question.'},
   {'q': '“It’s eight hundred dollars a month.” It means…', 'opts': ['$800 each month', '$800 each day', '8 dollars'], 'ans': 0, 'why': 'A month = each month.'},
   {'q': 'What does “See you tomorrow at five!” mean?', 'opts': ['We meet tomorrow at 5 o’clock', 'We met yesterday', 'We never meet'], 'ans': 0, 'why': 'See you = a short goodbye with a time.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'A room in Brooklyn',
  'text': [
   'Ava is new in **Brooklyn**. She needs a room, and she finds an ad on a wall: “Room for rent.” She takes out her phone and calls the number.',
   '“**Hi! I’m calling about the room for rent**,” she says. A man answers. His name is Cole. “**Yes, it’s still available.**” “**How much is the rent?**” “**It’s eight hundred dollars a month.**”',
   '“**Are bills included?**” Ava asks. “**Yes, water and Wi-Fi, but not electricity.**” Ava writes it in her notebook. She likes the price. “**When can I see it?**” “**Tomorrow at five?**” “**Great. See you tomorrow at five!**”',
   'That night Ava hums an old song, “Home, Sweet Home.” The words say that no place is like home. A room is small, but it can be a home. Cole says the room is on the fifth floor, and there is an elevator.',
   'The next day, Ava goes to see the room. Cole says, “Welcome! Here’s the key.” The room has a bed, a desk and a window. “It’s small,” Ava says, “but I like it.”'],
  'glossary': [{'w': 'room', 'pt': 'quarto, cômodo'}, {'w': 'available', 'pt': 'disponível'}, {'w': 'rent', 'pt': 'aluguel'}, {'w': 'bills', 'pt': 'contas'}, {'w': 'electricity', 'pt': 'luz (eletricidade)'}, {'w': 'notebook', 'pt': 'caderno'}, {'w': 'fifth', 'pt': 'quinto'}, {'w': 'elevator', 'pt': 'elevador'}, {'w': 'desk', 'pt': 'mesa de estudo'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A woman calls about a room for rent', 'A man buys a car', 'A girl cooks dinner'], 'ans': 0, 'why': 'Ava calls Cole about a room.'},
  'scan': [{'q': 'How much is the rent?', 'ans': 'eight hundred dollars a month', 'alt': ['$800', '800 dollars', '800 a month']}, {'q': 'What is not included in the bills?', 'ans': 'electricity', 'alt': ['the electricity']}, {'q': 'When does Ava see the room?', 'ans': 'tomorrow at five', 'alt': ['tomorrow at 5', 'at five']}],
  'tf': [{'s': 'The room is still available.', 'ans': True, 'why': '“Yes, it’s still available.”'}, {'s': 'The rent is $800 a week.', 'ans': False, 'why': 'It is $800 a month.'}, {'s': 'Wi-Fi is included.', 'ans': True, 'why': 'Water and Wi-Fi are included.'}, {'s': 'The room is on the first floor.', 'ans': False, 'why': 'It is on the fifth floor.'}],
  'order': ['Ava sees an ad.', 'She calls Cole.', 'She asks about the rent and the bills.', 'They set a time for tomorrow.', 'Cole gives her the key.'],
  'ctx': [{'sent': 'The room is still available.', 'w': 'available', 'opts': ['free to take', 'very dirty', 'very far'], 'ans': 0, 'why': 'Available = you can have it.'}, {'sent': 'Electricity is not included.', 'w': 'electricity', 'opts': ['power for lights and machines', 'a type of water', 'a kind of food'], 'ans': 0, 'why': 'Electricity gives power to lights.'}, {'sent': 'The room is on the fifth floor.', 'w': 'fifth', 'opts': ['number five in order', 'five rooms', 'five dollars'], 'ans': 0, 'why': 'Fifth is the ordinal for 5.'}],
  'chunkHunt': ['I’m calling about the room for rent.', 'How much is the rent?', 'Are bills included?', 'When can I see it?'],
  'think': 'Do you prefer to live alone or with a roommate? Why?'},
 'convo': {'npc': {'name': 'Ava'}, 'story': 'You have a room for rent in Brooklyn. Ava calls you. Answer her questions.', 'turns': [
  {'npc': 'Hi! I’m calling about the room for rent.', 'pt': 'Oi! Estou ligando sobre o quarto para alugar.', 'opts': [
   {'en': 'Yes, it’s still available.', 'pt': 'Sim, ainda está disponível.', 'ok': True, 'fb': 'Clear answer.'},
   {'en': 'Yes, is still available.', 'pt': 'Sim, ainda disponível.', 'ok': False, 'fb': 'Add it’s: it’s still available.'},
   {'en': 'No, I call you.', 'pt': 'Não, eu ligo você.', 'ok': False, 'fb': 'Does not answer her.'}]},
  {'npc': 'How much is the rent?', 'pt': 'Quanto é o aluguel?', 'opts': [
   {'en': 'It’s eight hundred dollars a month.', 'pt': 'São oitocentos dólares por mês.', 'ok': True, 'fb': 'Price + a month.'},
   {'en': 'It is eight hundred of dollars by month.', 'pt': 'São oitocentos de dólares por mês.', 'ok': False, 'fb': 'Say: eight hundred dollars a month.'},
   {'en': 'Rent is a room.', 'pt': 'Aluguel é um quarto.', 'ok': False, 'fb': 'She asks about the price.'}]},
  {'npc': 'Are bills included?', 'pt': 'As contas estão incluídas?', 'opts': [
   {'en': 'The bills includes water yes.', 'pt': 'As contas inclui água sim.', 'ok': False, 'fb': 'Bills are included.'},
   {'en': 'Yes, water and Wi-Fi, but not electricity.', 'pt': 'Sim, água e Wi-Fi, mas não a luz.', 'ok': True, 'fb': 'Complete and clear.'},
   {'en': 'Electricity is rent.', 'pt': 'A luz é aluguel.', 'ok': False, 'fb': 'Does not answer.'}]},
  {'npc': 'When can I see it?', 'pt': 'Quando posso ver?', 'opts': [
   {'en': 'You see it tomorrow.', 'pt': 'Você vê amanhã.', 'ok': False, 'fb': 'Suggest a time: Tomorrow at five?'},
   {'en': 'Tomorrow at five?', 'pt': 'Amanhã às cinco?', 'ok': True, 'fb': 'Offers a clear time.'},
   {'en': 'I am five tomorrow.', 'pt': 'Eu sou cinco amanhã.', 'ok': False, 'fb': 'Wrong meaning.'}]},
  {'npc': 'Great. See you tomorrow at five!', 'pt': 'Ótimo. Até amanhã às cinco!', 'opts': [
   {'en': 'See you! Bye!', 'pt': 'Até lá! Tchau!', 'ok': True, 'fb': 'Short and friendly.'},
   {'en': 'I am calling about the room.', 'pt': 'Estou ligando sobre o quarto.', 'ok': False, 'fb': 'That is Ava’s first line.'},
   {'en': 'How much is the rent?', 'pt': 'Quanto é o aluguel?', 'ok': False, 'fb': 'It is the end of the call.'}]}]},
 'errors': [
  {'wrong': 'I am calling for the room.', 'fix': 'I’m calling about the room.', 'alt': 'I call about the room.', 'why': 'Use calling about for a topic.'},
  {'wrong': 'Eight hundred dollar a month.', 'fix': 'Eight hundred dollars a month.', 'alt': 'Eight hundreds dollars a month.', 'why': 'Use dollars, but hundred has no -s here.'},
  {'wrong': 'Bills are include?', 'fix': 'Are bills included?', 'alt': 'Bills included are?', 'why': 'Question: Are + bills + included?'},
  {'wrong': 'We meet in tomorrow at five.', 'fix': 'We meet tomorrow at five.', 'alt': 'We meet on tomorrow at five.', 'why': 'No preposition before tomorrow.'}],
 'homework': 'Write an ad for a room for rent in your home: price, bills and your phone.',
 'homework_items': ['Write numbers 100, 200, 800 in English.', 'Say aloud: Are bills included?', 'Listen to the dialogue and shadow Ava.', 'Write 3 questions to ask about a room.']}
