"""Suplemento Quest v5 · aula 41: Cooking at home + regular Some more pancakes? (The Magic Porridge Pot)."""
SUPP = {
 'reg': 136,
 'badge': {'icon': '🍝', 'name': 'Kitchen Helper', 'desc': 'Cook and give simple steps in English'},
 'sticker': {'cat': 'Everyday culture', 'title': 'The American Home Kitchen', 'sub': 'Cups, ovens and hot pans'},
 'culture': {
  'hook': 'In many American homes, the kitchen is the center of the house. Friends talk, kids help, and everyone ends up standing near the stove.',
  'polite': 'When you help in someone else\'s kitchen, ask first: **“Can I help?”** Then listen to the steps.',
  'mythfact': [
   {'s': 'American recipes often use cups and tablespoons.', 'ans': True, 'why': 'Many US recipes measure by volume: a cup of flour, a tablespoon of oil.'},
   {'s': 'American ovens use degrees Celsius.', 'ans': False, 'why': 'Ovens in the USA use degrees Fahrenheit, for example 350°F.'},
   {'s': 'A guest can ask “Can I help?” in the kitchen.', 'ans': True, 'why': 'It is friendly and normal, and hosts often say yes.'},
   {'s': 'You should touch a pan to see if it is hot.', 'ans': False, 'why': 'Never touch it. Say “Careful! The pan is hot!” and use a pot holder.'}],
  'wild': [
   {'kind': 'Recipe card', 'lines': ['**Easy Tomato Pasta**', '1. Boil the pasta for 10 minutes.', '2. Cut 1 onion. Fry it in a pan.', '3. Add 2 tomatoes and a pinch of salt.'], 'decode': {'q': 'What do you do after you cut the onion?', 'opts': ['Fry it in a pan', 'Boil the pasta again', 'Add ice'], 'ans': 0, 'why': 'Step 2 says: “Fry it in a pan.”'}},
   {'kind': 'Note on the fridge', 'lines': ['Dinner is in the oven!', 'Please wait 20 minutes.', 'Careful: the dish is HOT.'], 'decode': {'q': 'Where is dinner?', 'opts': ['In the oven', 'In the fridge', 'On the table'], 'ans': 0, 'why': '“Dinner is in the oven!”'}}],
  'compare': {'br': 'In Brazil many home cooks measure by eye and use grams, liters and a fogão with a gas flame.', 'us': 'In the USA recipes often say cups, tablespoons and Fahrenheit, and many homes have an electric or gas stove.', 'tip': 'When you read an American recipe, check the unit first: cup, tablespoon or degrees F.', 'ask': 'What is one dish you can cook? Say the first two steps in English.'},
  'quiz': [
   {'q': 'You want to help a friend cook. You say…', 'opts': ['Can I help?', 'I help you now.', 'Help me cook.'], 'ans': 0, 'why': 'Can I help? is the polite offer.'},
   {'q': 'The pan is very hot. You say…', 'opts': ['Careful! The pan is hot!', 'Look, a pan.', 'The pan is happy.'], 'ans': 0, 'why': 'Careful! warns people about danger.'},
   {'q': 'A recipe says “350°F”. What is it about?', 'opts': ['Oven temperature', 'Weight of flour', 'Time to cook'], 'ans': 0, 'why': '°F means degrees Fahrenheit, used for oven heat.'}]},
 'reading': {
  'genre': 'Blog post', 'title': 'Pasta night with my roommate',
  'text': [
   'On Sunday night, my roommate Aaron and I cooked together in our small kitchen. He opened the fridge and asked, “**What are you making?**” I smiled and said, “**Pasta with tomato sauce**.”',
   'Aaron wanted to help. “**Can I help?**” he asked. “**Sure**,” I said. “**Cut the onions, please**.” He took a knife and a cutting board. “**How many?**” he asked. “**Just one**,” I said. “Then **add the tomatoes**.”',
   'I put a big pan on the stove and added some oil and a little salt. The kitchen smelled so good! Aaron came near the stove, and I said, “**Careful! The pan is hot**.” He stepped back and laughed.',
   'My family always says that cooking is like a game. First you cut, then you fry, next you add, and finally you taste. I thought about the fairy tale The Magic Porridge Pot, with a small pot that cooks porridge by magic. We have no magic pot, but tonight we made pasta, and it was a lot of fun.',
   'When the sauce was ready, I put the pasta on two plates. Aaron looked at his plate and said, “**Dinner is served!**” We sat at the small table and ate slowly. The food was simple, but it was delicious.'],
  'glossary': [{'w': 'fridge', 'pt': 'geladeira'}, {'w': 'knife', 'pt': 'faca'}, {'w': 'onions', 'pt': 'cebolas'}, {'w': 'pan', 'pt': 'panela/frigideira'}, {'w': 'stove', 'pt': 'fogão'}, {'w': 'salt', 'pt': 'sal'}, {'w': 'sauce', 'pt': 'molho'}, {'w': 'plates', 'pt': 'pratos'}, {'w': 'delicious', 'pt': 'delicioso'}],
  'fast': {'q': 'What is this text about?', 'opts': ['Two roommates cooking pasta', 'A trip to a restaurant', 'A day at school'], 'ans': 0, 'why': 'The writer and Aaron cook pasta at home.'},
  'scan': [{'q': 'How many onions does the writer ask for?', 'ans': 'one', 'alt': ['1', 'just one']}, {'q': 'What does the writer say when the pan is hot?', 'ans': 'Careful', 'alt': ['careful!', 'the pan is hot']}, {'q': 'What does Aaron say at the end?', 'ans': 'Dinner is served', 'alt': ['dinner is served!']}],
  'tf': [{'s': 'They cook on Sunday night.', 'ans': True, 'why': '“On Sunday night… we cooked together.”'}, {'s': 'Aaron cuts three onions.', 'ans': False, 'why': 'The writer says “Just one.”'}, {'s': 'The writer warns Aaron about the hot pan.', 'ans': True, 'why': '“Careful! The pan is hot.”'}, {'s': 'They eat in a restaurant.', 'ans': False, 'why': 'They eat at the small table at home.'}],
  'order': ['Aaron asks what the writer is making.', 'Aaron cuts one onion.', 'The writer adds salt to the pan.', 'The writer warns about the hot pan.', 'They sit and eat dinner.'],
  'ctx': [{'sent': 'The kitchen smelled so good!', 'w': 'smelled', 'opts': ['had a nice odor', 'was very loud', 'was dark'], 'ans': 0, 'why': 'Smelled = had an odor.'}, {'sent': 'He stepped back and laughed.', 'w': 'stepped back', 'opts': ['moved away', 'sat down', 'ran home'], 'ans': 0, 'why': 'Stepped back = moved away from something.'}, {'sent': 'The food was simple, but it was delicious.', 'w': 'delicious', 'opts': ['very tasty', 'very cold', 'very old'], 'ans': 0, 'why': 'Delicious = tastes great.'}],
  'chunkHunt': ['What are you making?', 'Can I help?', 'Careful! The pan is hot.', 'Dinner is served!'],
  'think': 'What can you cook? Tell a friend the steps in English.'},
 'convo': {'npc': {'name': 'Aaron'}, 'story': 'You are cooking in your kitchen in Salt Lake City. Your friend Aaron comes in to help.', 'turns': [
  {'npc': 'What are you making?', 'pt': 'O que você está fazendo?', 'opts': [
   {'en': 'I make you the pasta.', 'pt': 'Eu faço você a massa.', 'ok': False, 'fb': 'Wrong word order. Say I’m making pasta.'},
   {'en': 'Pasta with tomato sauce.', 'pt': 'Massa com molho de tomate.', 'ok': True, 'fb': 'Short and natural answer.'},
   {'en': 'I am Pasta.', 'pt': 'Eu sou massa.', 'ok': False, 'fb': 'Not a food answer.'}]},
  {'npc': 'Can I help?', 'pt': 'Posso ajudar?', 'opts': [
   {'en': 'No, you can’t.', 'pt': 'Não, você não pode.', 'ok': False, 'fb': 'Too rude for a friend.'},
   {'en': 'Yes, I help.', 'pt': 'Sim, eu ajudo.', 'ok': False, 'fb': 'Aaron is the helper. Say Sure.'},
   {'en': 'Sure. Cut the onions, please.', 'pt': 'Claro. Corte as cebolas, por favor.', 'ok': True, 'fb': 'Polite request with please.'}]},
  {'npc': 'How many?', 'pt': 'Quantas?', 'opts': [
   {'en': 'Just one. Then add the tomatoes.', 'pt': 'Só uma. Depois adicione os tomates.', 'ok': True, 'fb': 'Gives the number and the next step.'},
   {'en': 'It is Tuesday.', 'pt': 'É terça.', 'ok': False, 'fb': 'Out of context.'},
   {'en': 'I have one years.', 'pt': 'Eu tenho um anos.', 'ok': False, 'fb': 'This is about age, not onions.'}]},
  {'npc': 'OK. Is it hot?', 'pt': 'Ok. Está quente?', 'opts': [
   {'en': 'Yes, it is hot, careful.', 'pt': 'Sim, é quente, cuidado.', 'ok': False, 'fb': 'Close, but the natural form is Careful! The pan is hot.'},
   {'en': 'The pan has hot.', 'pt': 'A panela tem quente.', 'ok': False, 'fb': 'Use is hot, not has hot.'},
   {'en': 'Careful! The pan is hot.', 'pt': 'Cuidado! A panela está quente.', 'ok': True, 'fb': 'A warning plus the reason.'}]},
  {'npc': 'Dinner is served!', 'pt': 'O jantar está servido!', 'opts': [
   {'en': 'Smells amazing! Thanks for helping.', 'pt': 'Cheiro incrível! Obrigado por ajudar.', 'ok': True, 'fb': 'Compliment the food and thank your helper.'},
   {'en': 'I serve you.', 'pt': 'Eu sirvo você.', 'ok': False, 'fb': 'Does not answer his message.'},
   {'en': 'Dinner is a table.', 'pt': 'Jantar é uma mesa.', 'ok': False, 'fb': 'Does not make sense.'}]}]},
 'errors': [
  {'wrong': 'I’m cooking a pasta.', 'fix': 'I’m making pasta.', 'alt': 'I make pasta now.', 'why': 'Pasta is uncountable here: no a.'},
  {'wrong': 'Cut the onions, please you.', 'fix': 'Cut the onions, please.', 'alt': 'Please cut onions you.', 'why': 'Please goes at the end or the start; no you.'},
  {'wrong': 'The pan is hotter.', 'fix': 'The pan is hot.', 'alt': 'The pan has hot.', 'why': 'Use is + adjective.'},
  {'wrong': 'How much onions?', 'fix': 'How many onions?', 'alt': 'How many onion?', 'why': 'Onions are countable: How many + plural.'}],
 'homework': 'Write the 4 steps of an easy recipe in English and read them aloud to your teacher.',
 'homework_items': ['Write a 4-step recipe with First, Then, Next, Finally.', 'Record yourself saying “Careful! The pan is hot.”', 'Shadow Aaron’s lines in the dialogue.', 'Review: Can I help? / How many? / Dinner is served!']}
