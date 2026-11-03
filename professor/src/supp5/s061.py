"""Suplemento Quest v5 · aula 61: Tourist information + regular At the Art Gallery (The Starry Night)."""
SUPP = {
 'reg': 95,
 'badge': {'icon': '🗺️', 'name': 'City Explorer', 'desc': 'Ask for tips and plan a day in a new city'},
 'sticker': {'cat': 'Everyday culture', 'title': 'The Tourist Desk', 'sub': 'What can I see in one day?'},
 'culture': {
  'hook': 'Many American cities have a visitor center where friendly people give you a free map and tips. Learn the short questions that help you plan a whole day in a new place.',
  'polite': 'Start with **Excuse me** or **Hi**, then ask one clear question. End with **Thank you so much!**',
  'mythfact': [
   {'s': 'The Liberty Bell is in Philadelphia.', 'ans': True, 'why': 'You can see it in Independence National Historical Park.'},
   {'s': 'The Liberty Bell has a famous crack.', 'ans': True, 'why': 'The crack is a big part of its story.'},
   {'s': 'A cheesesteak is a dessert.', 'ans': False, 'why': 'A cheesesteak is a hot sandwich with meat and cheese.'},
   {'s': 'Visitor centers often give free maps.', 'ans': True, 'why': 'Many tourist offices have free paper maps.'},
   {'s': 'Van Gogh painted “The Starry Night” in 1950.', 'ans': False, 'why': 'He painted it in 1889.'}],
  'wild': [
   {'kind': 'Sign at a museum', 'lines': ['**Open** 10 a.m. – 5 p.m.', '**Closed** on Mondays', '**Free** for children under 12'], 'decode': {'q': 'On which day is the museum closed?', 'opts': ['Sunday', 'Monday', 'Friday'], 'ans': 1, 'why': 'The sign says: Closed on Mondays.'}},
   {'kind': 'Map note', 'lines': ['**You are here**', 'Museum: 5 minutes on foot', 'Park: 10 minutes on foot'], 'decode': {'q': 'Which place is closer?', 'opts': ['The museum', 'The park', 'They are the same'], 'ans': 0, 'why': '5 minutes is shorter than 10.'}}],
  'compare': {'br': 'In Brazil, many tourists ask hotel staff or local people for tips, and many cities also have tourist information points.', 'us': 'In the USA, you can often ask at a visitor center, and people may also say “Try this local favorite!”', 'tip': 'Ask for one thing at a time: a place, a price, a map.', 'ask': 'What is a must-see place in your city? Say it in English.'},
  'quiz': [
   {'q': 'You want to know the price. You ask…', 'opts': ['Is it free?', 'It is free?', 'Free is it?'], 'ans': 0, 'why': 'Questions with is: Is it…?'},
   {'q': '“A must-see” means…', 'opts': ['You should see it', 'You can’t see it', 'It is small'], 'ans': 0, 'why': 'A must-see is a place not to miss.'},
   {'q': 'You need directions on paper. You say…', 'opts': ['Do you have a map?', 'You have a map?', 'Map have you?'], 'ans': 0, 'why': 'Do you have…? is the natural question.'}]},
 'reading': {
  'genre': 'Travel diary', 'title': 'One day in Philadelphia',
  'text': [
   'Today I am in **Philadelphia**. I go to the visitor center and say, “**What can I see in one day?**” A man called Leo smiles and gives me a **map**.',
   '“**Visit the Liberty Bell**,” he says. “**It’s famous.**” I ask, “**Is it free?**” “Yes, it’s free,” he says. I like that! The bell has a big crack, and many people take a photo of it. My friend says, “**Say cheese!**”',
   'Then I ask, “**Where can I eat?**” Leo says, “**Try a cheesesteak.** It’s a local favorite.” A cheesesteak is a hot sandwich with meat and cheese. It is not small! I eat it in the park, and it is so good.',
   'In the afternoon, I want to see art. At the museum, a sign says **open** until five, and another sign says **closed** on Mondays. I am lucky: today is Saturday. I look at a picture of a blue night sky with big yellow stars. It is “The Starry Night” by Vincent van Gogh, from 1889. I like it very much, and I say, “It’s my favorite!” But that painting is not in Philadelphia. The real one is in New York, so I see a small copy in a book.',
   'At night, I look at my photos. It was a great day. “**Enjoy your day!**” Leo said at the end. I did.'],
  'glossary': [{'w': 'visitor center', 'pt': 'centro de visitantes'}, {'w': 'map', 'pt': 'mapa'}, {'w': 'famous', 'pt': 'famoso'}, {'w': 'free', 'pt': 'grátis'}, {'w': 'crack', 'pt': 'rachadura'}, {'w': 'sandwich', 'pt': 'sanduíche'}, {'w': 'sign', 'pt': 'placa'}, {'w': 'closed', 'pt': 'fechado'}, {'w': 'lucky', 'pt': 'com sorte'}, {'w': 'copy', 'pt': 'cópia'}],
  'fast': {'q': 'What is this text about?', 'opts': ['A tourist day in Philadelphia', 'A trip by airplane', 'A cooking class'], 'ans': 0, 'why': 'The writer visits places in Philadelphia.'},
  'scan': [{'q': 'Who gives the writer a map?', 'ans': 'Leo', 'alt': ['a man called Leo']}, {'q': 'What food does Leo suggest?', 'ans': 'a cheesesteak', 'alt': ['cheesesteak']}, {'q': 'Who painted “The Starry Night”?', 'ans': 'Vincent van Gogh', 'alt': ['van gogh']}],
  'tf': [{'s': 'The Liberty Bell is free.', 'ans': True, 'why': 'Leo says, “Yes, it’s free.”'}, {'s': 'The writer eats the cheesesteak in a museum.', 'ans': False, 'why': 'The writer eats it in the park.'}, {'s': 'The museum is closed on Mondays.', 'ans': True, 'why': 'A sign says closed on Mondays.'}, {'s': 'The real “Starry Night” is in Philadelphia.', 'ans': False, 'why': 'The real painting is in New York.'}],
  'order': ['The writer goes to the visitor center.', 'Leo gives the writer a map.', 'The writer sees the Liberty Bell.', 'The writer eats a cheesesteak.', 'The writer goes to the museum.'],
  'ctx': [{'sent': 'The Liberty Bell is famous.', 'w': 'famous', 'opts': ['known by many people', 'very small', 'very old shoes'], 'ans': 0, 'why': 'Famous = many people know it.'}, {'sent': 'The museum is closed on Mondays.', 'w': 'closed', 'opts': ['not open', 'very big', 'free'], 'ans': 0, 'why': 'Closed is the opposite of open.'}, {'sent': 'It is a local favorite.', 'w': 'local', 'opts': ['from this place', 'from space', 'very hot'], 'ans': 0, 'why': 'Local = from this area.'}],
  'chunkHunt': ['What can I see in one day?', 'Is it free?', 'Where can I eat?', 'Try a cheesesteak.'],
  'think': 'You have one day in your city with a visitor. What three places do you show? Say why.'},
 'convo': {'npc': {'name': 'Leo'}, 'story': 'You are at the visitor center in Philadelphia. Leo works at the desk.',
  'turns': [
   {'npc': 'Welcome to Philadelphia! Can I help you?', 'pt': 'Bem-vindo à Filadélfia! Posso ajudar?', 'opts': [
    {'en': 'I am one day here.', 'pt': 'Eu sou um dia aqui.', 'ok': False, 'fb': 'Say: I have one day.'},
    {'en': 'Yes, what can I see in one day?', 'pt': 'Sim, o que posso ver em um dia?', 'ok': True, 'fb': 'Clear question for a tourist.'},
    {'en': 'No, I see Philadelphia.', 'pt': 'Não, eu vejo a Filadélfia.', 'ok': False, 'fb': 'It does not ask for help.'}]},
   {'npc': 'Visit the Liberty Bell. It’s famous.', 'pt': 'Visite o Sino da Liberdade. É famoso.', 'opts': [
    {'en': 'Is it free?', 'pt': 'É de graça?', 'ok': True, 'fb': 'Good question about the price.'},
    {'en': 'It is free?', 'pt': 'É de graça?', 'ok': False, 'fb': 'Use Is it…? for questions.'},
    {'en': 'I am free.', 'pt': 'Eu sou livre.', 'ok': False, 'fb': 'Wrong meaning.'}]},
   {'npc': 'Yes, it’s free.', 'pt': 'Sim, é grátis.', 'opts': [
    {'en': 'Where can I eat?', 'pt': 'Onde posso comer?', 'ok': True, 'fb': 'Natural next question.'},
    {'en': 'Where I can eat?', 'pt': 'Onde eu posso comer?', 'ok': False, 'fb': 'Word order: Where can I…?'},
    {'en': 'I eat the bell.', 'pt': 'Eu como o sino.', 'ok': False, 'fb': 'Funny, but wrong.'}]},
   {'npc': 'Try a cheesesteak. It’s a local favorite.', 'pt': 'Experimente um cheesesteak. É o preferido daqui.', 'opts': [
    {'en': 'I try yesterday.', 'pt': 'Eu tento ontem.', 'ok': False, 'fb': 'Does not fit.'},
    {'en': 'Good idea!', 'pt': 'Boa ideia!', 'ok': False, 'fb': 'Natural, but the best answer asks for the map.'},
    {'en': 'Great idea. Do you have a map?', 'pt': 'Ótima ideia. Vocês têm mapa?', 'ok': True, 'fb': 'Accept the tip and ask for help.'}]},
   {'npc': 'Here you go. Enjoy your day!', 'pt': 'Aqui está. Aproveite o seu dia!', 'opts': [
    {'en': 'Thanks! You too!', 'pt': 'Obrigado! Você também!', 'ok': True, 'fb': 'Natural reply.'},
    {'en': 'Yes, I enjoy.', 'pt': 'Sim, eu aprecio.', 'ok': False, 'fb': 'Does not answer the wish.'},
    {'en': 'Good night!', 'pt': 'Boa noite!', 'ok': False, 'fb': 'It is the day, not the night.'}]}]},
 'errors': [
  {'wrong': 'Where I can eat?', 'fix': 'Where can I eat?', 'alt': 'Where can eat I?', 'why': 'In questions, can comes before I.'},
  {'wrong': 'It is free?', 'fix': 'Is it free?', 'alt': 'Is free it?', 'why': 'Put is before it to ask.'},
  {'wrong': 'I have a map? ', 'fix': 'Do you have a map?', 'alt': 'You have map?', 'why': 'Ask a person with Do you have…?'},
  {'wrong': 'I want see the bell.', 'fix': 'I want to see the bell.', 'alt': 'I want seeing the bell.', 'why': 'After want, use to + verb.'}],
 'homework': 'Write 4 questions you can ask at a tourist desk in your city, then say them aloud.',
 'homework_items': ['Write 4 tourist questions.', 'Record yourself asking them.', 'Shadow the dialogue with Leo.', 'Review: Is it free? / Where can I eat? / Do you have a map?']}
