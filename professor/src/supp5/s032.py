"""Suplemento Quest v5 · aula 32: Water, please + regular Cheers! (Pat-a-Cake)."""
SUPP = {
 'reg': 12,
 'badge': {'icon': '💧', 'name': 'Table Talk Star', 'desc': 'Ask for water, ask for time and enjoy your meal in English'},
 'culture': {
  'hook': 'In many American restaurants, the first thing a server does is bring water. Learn what to say about ice, time and the menu, so you feel relaxed at the table.',
  'mythfact': [
   {'s': 'In many American restaurants, the server brings you a glass of tap water for free.', 'ans': True, 'why': 'This is common: you can also say “No ice, please” if you do not want ice.'},
   {'s': 'You must order your food as soon as you sit down.', 'ans': False, 'why': 'You can say “Not yet, five more minutes.” Servers expect it.'},
   {'s': 'The Rock and Roll Hall of Fame is in Cleveland, Ohio.', 'ans': True, 'why': 'Yes, the museum opened in Cleveland in 1995.'},
   {'s': 'In the USA, a glass of water usually comes without ice.', 'ans': False, 'why': 'Ice water is the usual style, so people ask for “no ice” when they want it.'},
   {'s': '“Pat-a-Cake” is an English nursery rhyme.', 'ans': True, 'why': 'It is an old rhyme that children say while they clap.'}],
  'wild': [
   {'kind': 'Drink menu', 'lines': ['**Water**  free', '**Lemonade**  $3', '**Iced tea**  $3 · free refills'], 'decode': {'q': 'Which drink is free?', 'opts': ['Water', 'Lemonade', 'Iced tea'], 'ans': 0, 'why': 'The menu says “Water: free”.'}},
   {'kind': 'Table card', 'lines': ['Ready to order? Wave to your server.', 'Need more time? No problem!', 'Enjoy your meal!'], 'decode': {'q': 'What can you do if you need more time?', 'opts': ['Order now', 'Say you need more time', 'Leave'], 'ans': 1, 'why': '“Need more time? No problem!”'}}],
  'compare': {'br': 'In Brazil, the waiter often brings the menu and takes your drink order, and mineral water is often bought by the bottle.', 'us': 'In the USA, the server often brings a glass of water first, then waits for you to be ready.', 'tip': 'Say “Just water, please” and “No ice, please”. Both are polite and normal.', 'ask': 'What do you drink with your meal? Say it in English.'},
  'quiz': [
   {'q': 'You do not want ice in your water. You say…', 'opts': ['No ice, please.', 'Ice no.', 'I am without ice.'], 'ans': 0, 'why': 'No ice, please is short and polite.'},
   {'q': 'You are not ready to order. You say…', 'opts': ['Not yet. Five more minutes.', 'I do not like food.', 'Go away.'], 'ans': 0, 'why': 'Say it and the server will wait.'},
   {'q': 'At the end of the meal the server says “Enjoy your meal!” when…', 'opts': ['the food comes to the table', 'you leave', 'you pay'], 'ans': 0, 'why': 'It is said when the food arrives.'}]},
 'reading': {
  'genre': 'Diary',
  'title': 'Dinner in Cleveland',
  'text': [
   'Tonight I am in **Cleveland** with my friend Pete. We want dinner. The restaurant is warm, and the room smells great.',
   'A server named Maya comes to our table. She says, “Hi! **Can I get you something to drink?**” I say, “**Just water, please.**” She asks, “**With ice?**” “**No ice, please**,” I say. She brings the glass quickly. “**Here you go.** Ready to order?”',
   'Pete and I are not ready. I say, “**Not yet. Five more minutes.**” Maya smiles. “**No problem. Take your time.**” We read the menu and look at the napkin, the fork and the spoon on the table. They are all ready, and so are we.',
   'Then the food comes. I have soup and a sandwich. It is hot and delicious! A little baby at the next table claps her hands. Pete says, “It reminds me of the rhyme Pat-a-Cake!” We laugh.',
   'Pete lifts his glass. “**Cheers!**” he says. “**Enjoy your meal**,” Maya says. I say, “Thank you!” Dinner is simple, but it is perfect.'],
  'glossary': [{'w': 'server', 'pt': 'garçom/garçonete'}, {'w': 'ice', 'pt': 'gelo'}, {'w': 'glass', 'pt': 'copo de vidro'}, {'w': 'menu', 'pt': 'cardápio'}, {'w': 'napkin', 'pt': 'guardanapo'}, {'w': 'fork', 'pt': 'garfo'}, {'w': 'spoon', 'pt': 'colher'}, {'w': 'soup', 'pt': 'sopa'}, {'w': 'delicious', 'pt': 'delicioso'}],
  'fast': {'q': 'What is this diary about?', 'opts': ['A simple dinner in a restaurant', 'A day at school', 'A holiday at the beach'], 'ans': 0, 'why': 'The writer and Pete have dinner in Cleveland.'},
  'scan': [{'q': 'What is the server’s name?', 'ans': 'Maya', 'alt': ['maya']}, {'q': 'What does the writer drink?', 'ans': 'water', 'alt': ['just water']}, {'q': 'What food does the writer have?', 'ans': 'soup and a sandwich', 'alt': ['soup', 'a sandwich', 'sandwich']}],
  'tf': [{'s': 'The writer wants ice in the water.', 'ans': False, 'why': 'The writer says “No ice, please.”'}, {'s': 'They need more time before ordering.', 'ans': True, 'why': '“Not yet. Five more minutes.”'}, {'s': 'Pete is the server.', 'ans': False, 'why': 'Maya is the server. Pete is a friend.'}, {'s': 'Pete says “Cheers!”', 'ans': True, 'why': 'He lifts his glass and says Cheers.'}],
  'order': ['Maya asks about a drink.', 'The writer asks for water with no ice.', 'They ask for five more minutes.', 'The food comes.', 'Pete says Cheers.'],
  'ctx': [{'sent': 'Take your time. We are not in a hurry.', 'w': 'in a hurry', 'opts': ['fast because of time', 'happy', 'sleepy'], 'ans': 0, 'why': 'In a hurry = needing to be fast.'}, {'sent': 'The soup is hot and delicious.', 'w': 'delicious', 'opts': ['very tasty', 'very cold', 'very small'], 'ans': 0, 'why': 'Delicious = tastes very good.'}, {'sent': 'A baby claps her hands.', 'w': 'claps', 'opts': ['hits hands together', 'cries', 'runs'], 'ans': 0, 'why': 'Clap = hit your hands together.'}],
  'chunkHunt': ['Just water, please.', 'No ice, please.', 'Not yet. Five more minutes.', 'Enjoy your meal!'],
  'think': 'What do you drink at dinner? Do you like ice in your drink?'},
 'convo': {'npc': {'name': 'Maya'}, 'story': 'You are at a restaurant in Cleveland. Maya is your server. Order a drink and ask for time.', 'turns': [
  {'npc': 'Hi! Can I get you something to drink?', 'pt': 'Oi! Posso trazer algo para beber?', 'opts': [
   {'en': 'Yes, I am drinking water.', 'pt': 'Sim, eu estou bebendo água.', 'ok': False, 'fb': 'Say Just water, please.'},
   {'en': 'Just water, please.', 'pt': 'Só água, por favor.', 'ok': True, 'fb': 'Natural and short.'},
   {'en': 'I am hungry, thanks.', 'pt': 'Estou com fome, obrigado.', 'ok': False, 'fb': 'The question is about drinks.'}]},
  {'npc': 'With ice?', 'pt': 'Com gelo?', 'opts': [
   {'en': 'No ice, please.', 'pt': 'Sem gelo, por favor.', 'ok': True, 'fb': 'Answer directly.'},
   {'en': 'I am no ice.', 'pt': 'Eu sou sem gelo.', 'ok': False, 'fb': 'Wrong structure. Say No ice, please.'},
   {'en': 'Twice a day.', 'pt': 'Duas vezes por dia.', 'ok': False, 'fb': 'It does not match the question.'}]},
  {'npc': 'Here you go. Ready to order?', 'pt': 'Aqui está. Pronto para pedir?', 'opts': [
   {'en': 'Yes, I am ready for the bathroom.', 'pt': 'Sim, estou pronto para o banheiro.', 'ok': False, 'fb': 'Not what she asked.'},
   {'en': 'I am not ready yet. Wait.', 'pt': 'Eu não estou pronto ainda. Espere.', 'ok': False, 'fb': 'Too direct. Say Not yet, five more minutes.'},
   {'en': 'Not yet. Five more minutes.', 'pt': 'Ainda não. Mais cinco minutos.', 'ok': True, 'fb': 'Polite and clear.'}]},
  {'npc': 'No problem. Take your time.', 'pt': 'Sem problema. Fique à vontade.', 'opts': [
   {'en': 'Thank you!', 'pt': 'Obrigado!', 'ok': True, 'fb': 'Simple and polite.'},
   {'en': 'Yes, I take.', 'pt': 'Sim, eu pego.', 'ok': False, 'fb': 'It makes no sense here.'},
   {'en': 'Good morning!', 'pt': 'Bom dia!', 'ok': False, 'fb': 'It is dinner time.'}]},
  {'npc': 'Enjoy your meal!', 'pt': 'Bom apetite!', 'opts': [
   {'en': 'Good appetite!', 'pt': 'Bom apetite!', 'ok': False, 'fb': 'Not common in English. Say Thanks, you too.'},
   {'en': 'You are welcome.', 'pt': 'De nada.', 'ok': False, 'fb': 'It is not a thank you.'},
   {'en': 'Thanks, you too!', 'pt': 'Obrigado, você também!', 'ok': True, 'fb': 'A natural answer.'}]}]},
 'errors': [
  {'wrong': 'Water for me, no ice.', 'fix': 'Just water, please. No ice.', 'alt': 'Water to me, please.', 'why': 'Order with Just … please, then add a short extra request.'},
  {'wrong': 'I am not ready yet to order.', 'fix': 'I’m not ready to order yet.', 'alt': 'I not ready yet.', 'why': 'English puts yet at the end of the sentence.'},
  {'wrong': 'Good appetite!', 'fix': 'Enjoy your meal!', 'alt': 'Enjoy the meal!', 'why': 'Brazilians say bom apetite, but English says Enjoy your meal.'},
  {'wrong': 'Can you bring me one water?', 'fix': 'Could I have some water, please?', 'alt': 'Can you bring water me?', 'why': 'Use Could I have… to ask politely.'}],
 'homework': 'Record yourself ordering a drink and asking for more time at a restaurant.',
 'homework_items': ['Write 4 lines of a restaurant dialogue with a server.', 'Practice: Just water, please. / No ice, please.', 'Listen to the dialogue again and shadow Maya.', 'Review: Take your time. / Enjoy your meal! / Cheers!']}
