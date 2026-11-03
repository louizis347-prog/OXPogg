"""Suplemento Quest v5 · aula 61: Tourist information + regular Tour guide and audio (Museum Hours)."""
SUPP = {
 'reg': 214,
 'badge': {'icon': '🗺️', 'name': 'Smart Tourist', 'desc': 'Ask for tips, prices and a map at a tourist information desk'},
 'culture': {
  'hook': 'Many big cities have a tourist information desk. The staff answer simple questions, give you a free map and tell you what to see in one day.',
  'mythfact': [
   {'s': 'A tourist information center can give you a map.', 'ans': True, 'why': 'Maps and short guides are a normal part of the service, and they are often free.'},
   {'s': 'The Liberty Bell is in Philadelphia.', 'ans': True, 'why': 'It is a famous symbol of American history and you can see it in the city center.'},
   {'s': 'You must always pay to enter a famous place.', 'ans': False, 'why': 'Some places are free and some cost money. It is good to ask: “Is it free?”'},
   {'s': 'A cheesesteak is a sandwich with beef and cheese.', 'ans': True, 'why': 'It is a classic sandwich from Philadelphia.'},
   {'s': '“Museum Hours” is a film about a museum guard in Vienna.', 'ans': True, 'why': 'It is a 2012 film about a guard and a visitor who walk around the city.'}],
  'wild': [
   {'kind': 'Sign at a tourist desk', 'lines': ['**Free city maps**', 'Open 9 a.m. – 5 p.m.', 'Closed on holidays'], 'decode': {'q': 'When is the desk closed?', 'opts': ['On holidays', 'At 9 a.m.', 'Never'], 'ans': 0, 'why': '“Closed on holidays.”'}},
   {'kind': 'Museum ticket board', 'lines': ['**Adults** $15', '**Children** under 6: free', '**Audio guide** +$5'], 'decode': {'q': 'How much is an adult ticket with an audio guide?', 'opts': ['$20', '$15', '$5'], 'ans': 0, 'why': '$15 + $5 = $20.'}}],
  'compare': {'br': 'In Brazil, many tourists ask a hotel worker or use a phone app to find a good place to eat.', 'us': 'In the USA, people also use the tourist desk. The staff are used to simple questions, and they often have a free printed map.', 'tip': 'Start with: “Hi. What can I see in one day?”', 'ask': 'What is a famous place in your city? Say it in English.'},
  'quiz': [
   {'q': 'You want to know the price. You say…', 'opts': ['Is it free?', 'Is it famous yes?', 'It free is?'], 'ans': 0, 'why': 'Is it free? is a short, natural question.'},
   {'q': 'What does “a local favorite” mean?', 'opts': ['people from that place love it', 'it is very far', 'it is very old'], 'ans': 0, 'why': 'Local = from that place.'},
   {'q': 'You need directions on paper. You ask…', 'opts': ['Do you have a map?', 'Do you have a mapping?', 'Have you map?'], 'ans': 0, 'why': 'Do you have a…? is the normal pattern.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'One day in Philadelphia',
  'text': [
   'Mia is a tourist. She is in **Philadelphia** for one day. She has a small bag and a big smile. She walks to the tourist information desk near the park.',
   '“**Welcome to Philadelphia! Can I help you?**” a man asks. His name is Leo. “**Yes, what can I see in one day?**” Mia asks. “**Visit the Liberty Bell. It’s famous.**” “**Is it free?**” “**Yes, it’s free.**”',
   '“**Where can I eat?**” she asks. “**Try a cheesesteak. It’s a local favorite.**” Mia laughs. “**Great idea. Do you have a map?**” Leo gives her a paper map. “**Enjoy your day!**” he says.',
   'Mia likes the map. She remembers the film Museum Hours. In the film, a guard and a visitor walk around a city and look at art. Mia does not have a guide today, but the map is enough.',
   'She finds the Liberty Bell. It is old and big. The line is short, and the visit is free. She takes a photo. Then she eats a hot cheesesteak in the street. It is a perfect day.'],
  'glossary': [{'w': 'tourist', 'pt': 'turista'}, {'w': 'desk', 'pt': 'balcão'}, {'w': 'famous', 'pt': 'famoso'}, {'w': 'map', 'pt': 'mapa'}, {'w': 'local', 'pt': 'local, da região'}, {'w': 'guard', 'pt': 'guarda, segurança'}, {'w': 'visitor', 'pt': 'visitante'}, {'w': 'line', 'pt': 'fila'}, {'w': 'photo', 'pt': 'foto'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A tourist asks for help in a city', 'A girl cooks dinner', 'A boy buys a car'], 'ans': 0, 'why': 'Mia asks Leo for tips in Philadelphia.'},
  'scan': [{'q': 'What is the name of the man at the desk?', 'ans': 'Leo', 'alt': ['leo']}, {'q': 'What famous place does Leo tell her to visit?', 'ans': 'the Liberty Bell', 'alt': ['liberty bell']}, {'q': 'What does Leo give Mia?', 'ans': 'a map', 'alt': ['a paper map', 'map']}],
  'tf': [{'s': 'Mia is in Philadelphia for one week.', 'ans': False, 'why': 'She is there for one day.'}, {'s': 'The Liberty Bell visit is free.', 'ans': True, 'why': '“Yes, it’s free.”'}, {'s': 'Leo says to try a cheesesteak.', 'ans': True, 'why': 'A cheesesteak is a local favorite.'}, {'s': 'Mia has a guide today.', 'ans': False, 'why': 'She only has a map.'}],
  'order': ['Mia goes to the tourist desk.', 'Leo says to visit the Liberty Bell.', 'Mia asks where to eat.', 'Leo gives her a map.', 'Mia eats a cheesesteak.'],
  'ctx': [{'sent': 'The Liberty Bell is famous.', 'w': 'famous', 'opts': ['many people know it', 'it is very small', 'it is closed'], 'ans': 0, 'why': 'Famous = known by many people.'}, {'sent': 'It’s a local favorite.', 'w': 'local', 'opts': ['from that place', 'very far', 'very cheap'], 'ans': 0, 'why': 'Local = from that place.'}, {'sent': 'The line is short.', 'w': 'line', 'opts': ['people waiting one after another', 'a pen mark', 'a bus'], 'ans': 0, 'why': 'A line = people waiting.'}],
  'chunkHunt': ['Can I help you?', 'What can I see in one day?', 'Is it free?', 'Do you have a map?'],
  'think': 'What would you ask at a tourist desk in your city?'},
 'convo': {'npc': {'name': 'Leo'}, 'story': 'You are a tourist in Philadelphia. Leo works at the tourist information desk. Ask for tips and a map.', 'turns': [
  {'npc': 'Welcome to Philadelphia! Can I help you?', 'pt': 'Bem-vindo à Filadélfia! Posso ajudar?', 'opts': [
   {'en': 'Yes, what can I see in one day?', 'pt': 'Sim, o que posso ver em um dia?', 'ok': True, 'fb': 'Clear and short.'},
   {'en': 'Yes, I see Philadelphia.', 'pt': 'Sim, eu vejo a Filadélfia.', 'ok': False, 'fb': 'Ask what you can see.'},
   {'en': 'No, I am a tourist yesterday.', 'pt': 'Não, sou turista ontem.', 'ok': False, 'fb': 'Does not answer the question.'}]},
  {'npc': 'Visit the Liberty Bell. It’s famous.', 'pt': 'Visite o Sino da Liberdade. É famoso.', 'opts': [
   {'en': 'It is free?', 'pt': 'É grátis?', 'ok': False, 'fb': 'Use the question form: Is it free?'},
   {'en': 'Is it free?', 'pt': 'É de graça?', 'ok': True, 'fb': 'Natural question about price.'},
   {'en': 'It is a famous yes.', 'pt': 'É um famoso sim.', 'ok': False, 'fb': 'It does not make sense.'}]},
  {'npc': 'Yes, it’s free.', 'pt': 'Sim, é grátis.', 'opts': [
   {'en': 'Where can I eat?', 'pt': 'Onde posso comer?', 'ok': True, 'fb': 'Good next question.'},
   {'en': 'Where I can eat?', 'pt': 'Onde eu posso comer?', 'ok': False, 'fb': 'Word order: Where can I eat?'},
   {'en': 'I eat free.', 'pt': 'Eu como de graça.', 'ok': False, 'fb': 'Wrong meaning.'}]},
  {'npc': 'Try a cheesesteak. It’s a local favorite.', 'pt': 'Experimente um cheesesteak. É o preferido daqui.', 'opts': [
   {'en': 'I am trying a cheesesteak.', 'pt': 'Estou experimentando um cheesesteak.', 'ok': False, 'fb': 'Leo gives a tip. Answer the tip.'},
   {'en': 'Local is my favorite.', 'pt': 'Local é meu preferido.', 'ok': False, 'fb': 'Does not fit.'},
   {'en': 'Great idea. Do you have a map?', 'pt': 'Ótima ideia. Vocês têm mapa?', 'ok': True, 'fb': 'Thanks him and asks for a map.'}]},
  {'npc': 'Enjoy your day!', 'pt': 'Aproveite o seu dia!', 'opts': [
   {'en': 'Thanks! You too!', 'pt': 'Obrigado! Você também!', 'ok': True, 'fb': 'Natural goodbye.'},
   {'en': 'Welcome to Philadelphia!', 'pt': 'Bem-vindo à Filadélfia!', 'ok': False, 'fb': 'That is Leo’s line.'},
   {'en': 'Yes, I enjoy.', 'pt': 'Sim, eu aprecio.', 'ok': False, 'fb': 'Does not fit the goodbye.'}]}]},
 'errors': [
  {'wrong': 'Where I can eat?', 'fix': 'Where can I eat?', 'alt': 'Where can eat I?', 'why': 'In questions, can comes before I.'},
  {'wrong': 'You have a map?', 'fix': 'Do you have a map?', 'alt': 'Have you a map?', 'why': 'Use Do you have…? for a polite question.'},
  {'wrong': 'It is free the museum?', 'fix': 'Is the museum free?', 'alt': 'Is free the museum?', 'why': 'Put is before the thing you ask about.'},
  {'wrong': 'I want see the Liberty Bell.', 'fix': 'I want to see the Liberty Bell.', 'alt': 'I want seeing the Liberty Bell.', 'why': 'After want, use to + verb.'}],
 'homework': 'Write 5 questions you can ask at a tourist desk in your own city.',
 'homework_items': ['Write the price question: Is it free?', 'Say aloud: What can I see in one day?', 'Listen to the dialogue and shadow Leo.', 'Name one famous place in your city in English.']}
