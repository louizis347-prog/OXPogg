"""Suplemento Quest v5 · aula 141: Deep dish and windy days (Chicago) + regular A Piece of Cake (Cloudy with a Chance of Meatballs)."""
SUPP = {
 'reg': 104,
 'badge': {'icon': '🍕', 'name': 'Windy City Diner', 'desc': 'Ask for a table, a pizza and a drink in Chicago'},
 'culture': {
  'hook': 'Chicago is famous for its tall deep dish pizza and for the cold wind from the lake. At a pizzeria, you ask for a table, choose your pizza, and wait a long time for it.',
  'mythfact': [
   {'s': 'A deep dish pizza is baked in a tall pan.', 'ans': True, 'why': 'The pan is deep, so the crust is thick and the pizza has many layers.'},
   {'s': 'A deep dish pizza is ready in five minutes.', 'ans': False, 'why': 'It usually takes 30 to 45 minutes to bake.'},
   {'s': 'Chicago is next to a very big lake.', 'ans': True, 'why': 'It is on Lake Michigan, and the wind from the water can be strong.'},
   {'s': 'The nickname “Windy City” comes only from the weather.', 'ans': False, 'why': 'Many people link it to the wind, but some say it also came from talkative politicians.'},
   {'s': 'At a pizzeria with waiters, people usually leave a tip.', 'ans': True, 'why': 'In the USA, a tip is normal when someone serves you at the table.'}],
  'wild': [
   {'kind': 'Pizzeria menu', 'lines': ['**Deep Dish** (serves 2–3) $24', 'Please allow **40 minutes**', 'Add sausage or onions $3'], 'decode': {'q': 'How long do you wait for a deep dish?', 'opts': ['About 40 minutes', 'Two minutes', 'All night'], 'ans': 0, 'why': 'The menu says: allow 40 minutes.'}},
   {'kind': 'Sign at the door', 'lines': ['**Wait to be seated**', 'Hold the door: it is windy!', 'Coats on the hooks'], 'decode': {'q': 'What should you do first?', 'opts': ['Wait for the host', 'Sit anywhere', 'Go to the kitchen'], 'ans': 0, 'why': '“Wait to be seated” means the host shows you a table.'}}],
  'compare': {'br': 'In Brazil, pizza is often thin and round, and many families order it for home delivery.', 'us': 'In Chicago, many people eat a thick deep dish pizza with a knife and fork, and it takes a long time to bake.', 'tip': 'Ask: “How long does it take?”', 'ask': 'Do you prefer thin pizza or thick pizza? Say it in English.'},
  'quiz': [
   {'q': 'You want a table for two people. You say…', 'opts': ['A table for two, please.', 'A table of two people I want.', 'Two table, please.'], 'ans': 0, 'why': 'A table for two, please is short and polite.'},
   {'q': '“It takes forty minutes.” It means…', 'opts': ['You wait about forty minutes', 'The pizza costs forty dollars', 'The pizza has forty slices'], 'ans': 0, 'why': 'Takes + time = how long something needs.'},
   {'q': 'A friend says, “We’re not in a hurry.” It means…', 'opts': ['We have time', 'We are very hungry', 'We are late'], 'ans': 0, 'why': 'Not in a hurry = no rush.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Forty minutes for a pizza',
  'text': [
   'Evan and his sister Nora are in **Chicago**. It is a cold, windy day. They are hungry, so they walk to a pizzeria near the lake. The host is a tall man with a big smile.',
   '“**Hi. A table for two, please**,” Evan says. “**Sure. Follow me**,” the host says. They sit near the window. “**We want a deep dish pizza**,” Nora says. “**It takes forty minutes**,” the host says. “**That’s fine. We’re not in a hurry**,” Evan says.',
   'The pizza has a thick crust, a lot of cheese and sausage. It bakes in a tall pan. Nora thinks about the film “Cloudy with a Chance of Meatballs.” In the film, food falls from the sky! “Today only the wind falls from our sky,” she says and laughs.',
   '“**Would you like something to drink?**” the host asks. “**Two sodas, please**,” Evan says. Outside, a gust of wind moves a sign. “**It’s so windy today!**” the host says. “**That’s why they call it the Windy City**,” Evan says. Some people say the name comes from the wind off the lake.',
   'Forty minutes later, the pizza comes. It is hot and the cheese is long and soft. Evan cuts a big slice. “Eating this pizza is a piece of cake,” he says. Nora smiles. The wind is loud outside, but the pizzeria is warm.'],
  'glossary': [{'w': 'host', 'pt': 'recepcionista (do restaurante)'}, {'w': 'pizzeria', 'pt': 'pizzaria'}, {'w': 'lake', 'pt': 'lago'}, {'w': 'crust', 'pt': 'massa, borda'}, {'w': 'sausage', 'pt': 'linguiça'}, {'w': 'pan', 'pt': 'forma, panela'}, {'w': 'gust', 'pt': 'rajada de vento'}, {'w': 'hurry', 'pt': 'pressa'}, {'w': 'soft', 'pt': 'macio'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A brother and sister wait for a pizza', 'A man buys a coat', 'A girl takes a train'], 'ans': 0, 'why': 'Evan and Nora wait forty minutes for a deep dish pizza.'},
  'scan': [{'q': 'How long does the pizza take?', 'ans': 'forty minutes', 'alt': ['40 minutes', 'forty']}, {'q': 'What do Evan and Nora drink?', 'ans': 'sodas', 'alt': ['soda', 'two sodas']}, {'q': 'What is the nickname of Chicago?', 'ans': 'the Windy City', 'alt': ['Windy City']}],
  'tf': [{'s': 'Evan and Nora want a deep dish pizza.', 'ans': True, 'why': 'Nora says it.'}, {'s': 'They are in a big hurry.', 'ans': False, 'why': 'Evan says they are not in a hurry.'}, {'s': 'The host says it is a sunny day.', 'ans': False, 'why': 'He says it is so windy.'}, {'s': 'The pizza has a thick crust.', 'ans': True, 'why': 'It is a deep dish pizza.'}],
  'order': ['Evan asks for a table for two.', 'The host says to follow him.', 'Nora asks for a deep dish pizza.', 'They order two sodas.', 'The hot pizza comes.'],
  'ctx': [{'sent': 'A gust of wind moves the sign.', 'w': 'gust', 'opts': ['a short strong wind', 'a loud song', 'a cold drink'], 'ans': 0, 'why': 'A gust is a sudden strong wind.'}, {'sent': 'The pizza has a thick crust.', 'w': 'crust', 'opts': ['the outside bread part', 'the red sauce', 'the paper box'], 'ans': 0, 'why': 'The crust is the bread part of a pizza.'}, {'sent': 'The host is a tall man.', 'w': 'host', 'opts': ['the person who greets guests', 'the cook', 'a hungry guest'], 'ans': 0, 'why': 'The host welcomes you and shows your table.'}],
  'chunkHunt': ['A table for two, please.', 'Follow me.', 'It takes forty minutes.', 'We’re not in a hurry.'],
  'think': 'Do you like thick pizza or thin pizza? Why?'},
 'convo': {'npc': {'name': 'Sam'}, 'story': 'You are in a pizzeria in Chicago. Sam is the host. Ask for a table and order.', 'turns': [
  {'npc': 'Hi! How many people?', 'pt': 'Oi! Quantas pessoas?', 'opts': [
   {'en': 'A table for two, please.', 'pt': 'Uma mesa para dois, por favor.', 'ok': True, 'fb': 'Short and polite.'},
   {'en': 'A table of two, please.', 'pt': 'Uma mesa de dois, por favor.', 'ok': False, 'fb': 'Say a table for two.'},
   {'en': 'I am two, thanks.', 'pt': 'Eu sou dois, obrigado.', 'ok': False, 'fb': 'It does not make sense.'}]},
  {'npc': 'Sure. Follow me. What would you like?', 'pt': 'Claro. Siga-me. O que vocês querem?', 'opts': [
   {'en': 'We are wanting a deep dish pizza.', 'pt': 'Estamos querendo uma pizza de massa grossa.', 'ok': False, 'fb': 'Want is a state verb: We want.'},
   {'en': 'We want a pizza deep dish.', 'pt': 'Queremos uma pizza massa grossa.', 'ok': False, 'fb': 'Adjective first: a deep dish pizza.'},
   {'en': 'We want a deep dish pizza.', 'pt': 'Queremos uma pizza de massa grossa.', 'ok': True, 'fb': 'Natural order.'}]},
  {'npc': 'It takes forty minutes.', 'pt': 'Leva quarenta minutos.', 'opts': [
   {'en': 'That’s fine. We’re not in a hurry.', 'pt': 'Tudo bem. Não temos pressa.', 'ok': True, 'fb': 'Polite and clear.'},
   {'en': 'That is fine. We not in hurry.', 'pt': 'Tudo bem. Nós não em pressa.', 'ok': False, 'fb': 'Say: We’re not in a hurry.'},
   {'en': 'Forty dollars is fine.', 'pt': 'Quarenta dólares está bom.', 'ok': False, 'fb': 'He said minutes, not dollars.'}]},
  {'npc': 'Would you like something to drink?', 'pt': 'Vocês querem algo para beber?', 'opts': [
   {'en': 'Two sodas, please.', 'pt': 'Dois refrigerantes, por favor.', 'ok': True, 'fb': 'Clear order.'},
   {'en': 'Yes, I drink soda.', 'pt': 'Sim, eu bebo refrigerante.', 'ok': False, 'fb': 'Order with: Two sodas, please.'},
   {'en': 'Two soda, please.', 'pt': 'Dois refrigerante, por favor.', 'ok': False, 'fb': 'Two sodas: use the plural.'}]},
  {'npc': 'It’s so windy today!', 'pt': 'Está ventando muito hoje!', 'opts': [
   {'en': 'It is windy yes today.', 'pt': 'Está ventoso sim hoje.', 'ok': False, 'fb': 'Wrong word order.'},
   {'en': 'That’s why they call it the Windy City.', 'pt': 'Por isso chamam de Cidade dos Ventos.', 'ok': True, 'fb': 'Fits Chicago.'},
   {'en': 'I am wind, too.', 'pt': 'Eu sou vento também.', 'ok': False, 'fb': 'Wrong meaning.'}]}]},
 'errors': [
  {'wrong': 'A table to two, please.', 'fix': 'A table for two, please.', 'alt': 'A table of two, please.', 'why': 'Use for with the number of people.'},
  {'wrong': 'We want a pizza deep dish.', 'fix': 'We want a deep dish pizza.', 'alt': 'We want a pizza of deep dish.', 'why': 'In English, the describing words come before pizza.'},
  {'wrong': 'We not in hurry.', 'fix': 'We’re not in a hurry.', 'alt': 'We are not in hurry.', 'why': 'Use are not and a before hurry.'},
  {'wrong': 'It takes forty minute.', 'fix': 'It takes forty minutes.', 'alt': 'It take forty minutes.', 'why': 'Forty needs plural minutes, and it takes has -s.'}],
 'homework': 'Write a short dialogue: you ask for a table for three and order one pizza and three drinks.',
 'homework_items': ['Write how to ask for a table for four.', 'Say aloud: It takes forty minutes.', 'Listen to the dialogue and shadow the host.', 'Review: hot / cold / windy.']}
