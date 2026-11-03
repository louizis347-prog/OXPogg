"""Suplemento Quest v5 · aula 26: What's in this? + regular Are These Sweet? (Hansel and Gretel)."""
SUPP = {
 'reg': 49,
 'badge': {'icon': '🥟', 'name': 'Food Detective', 'desc': 'Ask what is in your food and say what you do not eat'},
 'sticker': {'cat': 'Everyday culture', 'title': 'What Is in This?', 'sub': 'I don’t eat pork.'},
 'culture': {
  'hook': 'In the USA, people with many different diets eat at the same market. Asking “What’s in this?” is normal, polite and sometimes very important for health.',
  'polite': 'Say **I don’t eat pork** or **I’m allergic to peanuts**. Then ask, **Do you have something else?**',
  'mythfact': [
   {'s': 'It is normal to ask what is in a dish.', 'ans': True, 'why': 'Cooks and servers expect the question.'},
   {'s': 'In the USA, food labels show nothing about allergies.', 'ans': False, 'why': 'US labels must name major allergens like milk, eggs, peanuts and wheat.'},
   {'s': 'San Francisco has a famous Chinatown with many dumpling shops.', 'ans': True, 'why': 'It is one of the oldest Chinatowns in North America.'},
   {'s': '“Vegan” food has no meat, no fish, no eggs and no milk.', 'ans': True, 'why': 'Vegan = no animal products.'},
   {'s': 'Being allergic is the same as not liking a food.', 'ans': False, 'why': 'An allergy can make you sick; saying “I don’t like it” is different.'}],
  'wild': [
   {'kind': 'Menu with notes', 'lines': ['**Pork & cabbage dumplings** (6) · $8', '**Chicken & mushroom dumplings** (6) · $8', '**Veggie dumplings (vegan)** (6) · $7'], 'decode': {'q': 'Which dumplings have no meat?', 'opts': ['Pork & cabbage', 'Veggie dumplings', 'Chicken & mushroom'], 'ans': 1, 'why': 'The vegan veggie dumplings have no meat.'}},
   {'kind': 'Food label', 'lines': ['**Ingredients:** rice, beans, salt, oil', '**Contains:** soy', 'May contain peanuts'], 'decode': {'q': 'What does this food contain?', 'opts': ['Soy', 'Milk', 'Fish'], 'ans': 0, 'why': 'The label says “Contains: soy”.'}}],
  'compare': {'br': 'In Brazil, “feijão com arroz” is an everyday meal, and people often ask the cook, “Tem carne?” before they eat.', 'us': 'In the USA, many people say clearly what they can’t eat: I’m vegan, I’m allergic to nuts, I don’t eat pork.', 'tip': 'Use “I don’t eat…” for a rule and “I’m allergic to…” for health.', 'ask': 'Is there a food you don’t eat? Say it in English.'},
  'quiz': [
   {'q': 'You want to know the filling. You ask…', 'opts': ['What’s in it?', 'Who is in it?', 'Where is it?'], 'ans': 0, 'why': 'What’s in it? asks about the ingredients.'},
   {'q': 'You don’t eat pork. You say…', 'opts': ['I don’t eat pork.', 'I no eat pork.', 'I am not pork.'], 'ans': 0, 'why': 'Use don’t + eat.'},
   {'q': '“Six for eight dollars” means…', 'opts': ['6 dumplings cost $8', '8 dumplings cost $6', '6 dollars each'], 'ans': 0, 'why': 'Six for eight dollars = six dumplings for $8.'}]},
 'reading': {
  'genre': 'Short story', 'title': 'The dumpling stand',
  'text': [
   'Mei has a small dumpling stand in **San Francisco**. Every day, people come and say, “**Yum!** These smell good.” Mei smiles. “**Try one**,” she says.',
   'One day, a woman called Nina comes to the stand. “**What’s in it?**” she asks. “Pork and cabbage,” says Mei. “**I don’t eat pork**,” says Nina. “**Do you have** chicken?” “Yes! Chicken and mushroom,” says Mei.',
   'Nina eats one. “**Perfect!** How much?” “**Six for eight dollars**,” says Mei. Nina buys six, and she tries the sauce. It is a little spicy. “**It’s fire!**” she laughs, and drinks some water.',
   'Mei thinks about her grandmother’s story. It is a fairy tale from Germany, “Hansel and Gretel”. The Brothers Grimm collected it in 1812. Two children find a house of bread, cake and candy. “Are these sweet?” they ask. Mei’s dumplings are not sweet, but the children in her street love them too.',
   'Nina comes back the next week. “**Enjoy the dumplings!**” says Mei. Now Nina is a happy customer, and she tells her friends about the little stand.'],
  'glossary': [{'w': 'stand', 'pt': 'barraca'}, {'w': 'smell', 'pt': 'cheirar'}, {'w': 'cabbage', 'pt': 'repolho'}, {'w': 'pork', 'pt': 'carne de porco'}, {'w': 'mushroom', 'pt': 'cogumelo'}, {'w': 'sauce', 'pt': 'molho'}, {'w': 'spicy', 'pt': 'picante'}, {'w': 'fairy tale', 'pt': 'conto de fadas'}, {'w': 'candy', 'pt': 'doce'}, {'w': 'customer', 'pt': 'cliente'}],
  'fast': {'q': 'What is this text about?', 'opts': ['A woman buys dumplings at a stand', 'A trip to the airport', 'A soccer game'], 'ans': 0, 'why': 'Nina buys dumplings from Mei.'},
  'scan': [{'q': 'What does Nina not eat?', 'ans': 'pork', 'alt': ['she does not eat pork']}, {'q': 'How many dumplings cost eight dollars?', 'ans': 'six', 'alt': ['6']}, {'q': 'Who collected the fairy tale in 1812?', 'ans': 'the Brothers Grimm', 'alt': ['brothers grimm', 'grimm']}],
  'tf': [{'s': 'Mei sells dumplings in San Francisco.', 'ans': True, 'why': '“A small dumpling stand in San Francisco.”'}, {'s': 'Nina eats pork.', 'ans': False, 'why': '“I don’t eat pork.”'}, {'s': 'The sauce is a little spicy.', 'ans': True, 'why': 'It is a little spicy.'}, {'s': 'The fairy tale is from Italy.', 'ans': False, 'why': 'It is from Germany.'}],
  'order': ['Mei says, “Try one.”', 'Nina asks what is in the dumplings.', 'Nina chooses chicken and mushroom.', 'Nina pays eight dollars for six.', 'Nina comes back the next week.'],
  'ctx': [{'sent': 'The sauce is spicy.', 'w': 'spicy', 'opts': ['hot with pepper', 'very sweet', 'cold'], 'ans': 0, 'why': 'Spicy = hot in taste.'}, {'sent': 'Try one, please.', 'w': 'Try', 'opts': ['taste', 'throw', 'buy'], 'ans': 0, 'why': 'Try = taste to see.'}, {'sent': 'I don’t eat pork.', 'w': 'pork', 'opts': ['meat from a pig', 'meat from a cow', 'a vegetable'], 'ans': 0, 'why': 'Pork comes from a pig.'}],
  'chunkHunt': ['What’s in it?', 'I don’t eat pork.', 'Do you have chicken?', 'Six for eight dollars.'],
  'think': 'Is there a food you don’t eat? How do you say it politely?'},
 'convo': {'npc': {'name': 'Nina'}, 'story': 'You sell dumplings at a stand in San Francisco. Nina is a customer. Answer her questions.',
  'turns': [
   {'npc': 'Hi! These dumplings smell good.', 'pt': 'Oi! Esses bolinhos estão com cheiro bom.', 'opts': [
    {'en': 'Thank you! Try one.', 'pt': 'Obrigada! Experimente um.', 'ok': True, 'fb': 'Thank her and offer one.'},
    {'en': 'You are welcome!', 'pt': 'De nada!', 'ok': False, 'fb': 'She did not thank you.'},
    {'en': 'I smell good.', 'pt': 'Eu cheiro bem.', 'ok': False, 'fb': 'Wrong meaning.'}]},
   {'npc': 'What’s in it?', 'pt': 'O que tem dentro?', 'opts': [
    {'en': 'It is in the box.', 'pt': 'Está na caixa.', 'ok': False, 'fb': 'She asks about the filling.'},
    {'en': 'Pork and cabbage.', 'pt': 'Carne de porco e repolho.', 'ok': True, 'fb': 'Name the ingredients.'},
    {'en': 'Is very good.', 'pt': 'É muito bom.', 'ok': False, 'fb': 'It does not say the ingredients.'}]},
   {'npc': 'I don’t eat pork. Do you have chicken?', 'pt': 'Não como porco. Tem de frango?', 'opts': [
    {'en': 'Yes! Chicken and mushroom.', 'pt': 'Tem! Frango e cogumelo.', 'ok': True, 'fb': 'Answer and add details.'},
    {'en': 'No eat, sorry.', 'pt': 'Não come, desculpe.', 'ok': False, 'fb': 'Not clear.'},
    {'en': 'I have chicken.', 'pt': 'Eu tenho frango.', 'ok': False, 'fb': 'Close, but say Yes, we do.'}]},
   {'npc': 'Perfect. How much?', 'pt': 'Perfeito. Quanto custa?', 'opts': [
    {'en': 'Eight dollars for six.', 'pt': 'Oito dólares por seis.', 'ok': False, 'fb': 'Natural: Six for eight dollars.'},
    {'en': 'Six for eight dollars.', 'pt': 'Seis por oito dólares.', 'ok': True, 'fb': 'Quantity first, then price.'},
    {'en': 'I am six dollars.', 'pt': 'Eu sou seis dólares.', 'ok': False, 'fb': 'Wrong meaning.'}]},
   {'npc': 'Enjoy the dumplings!', 'pt': 'Aproveite os bolinhos!', 'opts': [
    {'en': 'Thanks! Come back soon.', 'pt': 'Obrigada! Volte logo.', 'ok': True, 'fb': 'Friendly goodbye.'},
    {'en': 'I enjoy the dumplings.', 'pt': 'Eu aproveito os bolinhos.', 'ok': False, 'fb': 'She is wishing you well.'},
    {'en': 'Good morning!', 'pt': 'Bom dia!', 'ok': False, 'fb': 'It is a goodbye moment.'}]}]},
 'errors': [
  {'wrong': 'I no eat pork.', 'fix': 'I don’t eat pork.', 'alt': 'I not eat pork.', 'why': 'Use don’t before the verb.'},
  {'wrong': 'What has inside?', 'fix': 'What’s in it?', 'alt': 'What is inside it has?', 'why': 'Use What’s in it? for ingredients.'},
  {'wrong': 'You have chicken?', 'fix': 'Do you have chicken?', 'alt': 'Have you chicken?', 'why': 'Questions with have need Do you have…?'},
  {'wrong': 'Six dumplings by eight dollars.', 'fix': 'Six dumplings for eight dollars.', 'alt': 'Six dumplings of eight dollars.', 'why': 'Use for with a price.'}],
 'homework': 'Write 4 sentences about foods you eat and foods you do not eat, and say them aloud.',
 'homework_items': ['Write 4 sentences: I eat… / I don’t eat…', 'Ask “What’s in it?” about 3 foods.', 'Shadow the dialogue with Nina.', 'Review: What’s in it? / I don’t eat… / Six for eight dollars.']}
