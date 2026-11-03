"""Suplemento Quest v5 · aula 31: Coffee, your way + regular Make Tea, Make a Cake."""
SUPP = {
 'reg': 58,
 'badge': {'icon': '🥛', 'name': 'Custom Coffee Pro', 'desc': 'Order a drink your way: size, milk and hot or iced'},
 'culture': {
  'hook': 'In Seattle, a coffee order is a small list of choices: drink, size, milk and temperature. Learn the list and you can order your way anywhere in the USA.',
  'mythfact': [
   {'s': 'The coffee company Starbucks began in Seattle.', 'ans': True, 'why': 'Starbucks opened its first shop in Seattle in 1971.'},
   {'s': 'In the USA, people only drink hot coffee.', 'ans': False, 'why': 'Iced coffee and iced lattes are very common, even in winter.'},
   {'s': 'Oat milk is made from oats.', 'ans': True, 'why': 'It is a plant-based milk, a popular choice instead of cow’s milk.'},
   {'s': 'A barista chooses your size for you.', 'ans': False, 'why': 'You choose: small, medium or large. The barista asks you.'},
   {'s': 'The Great British Bake Off is filmed in a big tent.', 'ans': True, 'why': 'The bakers work in a large tent in the countryside.'}],
  'wild': [
   {'kind': 'Menu board', 'lines': ['**Latte**  small $4 · medium $5 · large $6', '**Oat milk**  +$0.75', '**Blueberry muffin**  $3.50'], 'decode': {'q': 'How much is a medium latte with oat milk?', 'opts': ['$5.75', '$4.75', '$6.75'], 'ans': 0, 'why': '$5 + $0.75 = $5.75.'}},
   {'kind': 'Sign at the counter', 'lines': ['Please wait here for your name.', 'Cups are hot!', 'Refills: ask at the counter.'], 'decode': {'q': 'What should you do after you order?', 'opts': ['Wait for your name', 'Go home', 'Make your coffee'], 'ans': 0, 'why': '“Please wait here for your name.”'}}],
  'compare': {'br': 'In Brazil, a small hot cafezinho is the normal coffee, and people often drink it standing at the counter.', 'us': 'In the USA, coffee has many choices: size, milk, hot or iced. The barista asks and you answer one by one.', 'tip': 'Answer each question with one short word: Medium. Oat milk. Hot.', 'ask': 'How do you like your coffee? Say it in English.'},
  'quiz': [
   {'q': 'The barista asks: “Hot or iced?” You want a cold drink. You say…', 'opts': ['Iced, please.', 'I cold.', 'Ice me.'], 'ans': 0, 'why': 'Answer with one word and please.'},
   {'q': 'Which question is about size?', 'opts': ['Hot or iced?', 'What size?', 'Anything to eat?'], 'ans': 1, 'why': '“What size? Small, medium or large?”'},
   {'q': 'What is a latte?', 'opts': ['Coffee with milk', 'A kind of bread', 'A cold sandwich'], 'ans': 0, 'why': 'A latte is espresso with a lot of milk.'}]},
 'reading': {
  'genre': 'Blog post',
  'title': 'Coffee first, cake later',
  'text': [
   'My friend Joy lives in **Seattle**. She loves coffee. Every morning she goes to a small café near her house. Today I went with her, and I learned a lot.',
   'At the counter, the barista smiled and said, “**What can I get started for you?**” Joy said, “A latte, please.” “**What size?**” “Medium. **With oat milk.**” “**Hot or iced?**” “Hot, please.” Her order was clear, short and polite.',
   'Then the barista asked, “**Anything to eat?**” Joy chose a **blueberry muffin**. I laughed because it looked like a small cake. Joy said, “I need my **caffeine fix**!” The barista answered, “Have a great day!”',
   'At home, we watched The Great British Bake Off. It is a baking show from 2010. Bakers make cakes and bread in a big tent. They follow a recipe, watch the timer and check the oven. “The oven is hot! Time’s up!” the hosts say.',
   'I want to bake a cake, too. I can make the cake, and Joy can make the coffee. We can eat together. For me, coffee is more fun with a friend and something sweet.'],
  'glossary': [{'w': 'counter', 'pt': 'balcão'}, {'w': 'size', 'pt': 'tamanho'}, {'w': 'oat milk', 'pt': 'leite de aveia'}, {'w': 'iced', 'pt': 'gelado'}, {'w': 'muffin', 'pt': 'bolinho de café'}, {'w': 'recipe', 'pt': 'receita'}, {'w': 'timer', 'pt': 'cronômetro'}, {'w': 'oven', 'pt': 'forno'}, {'w': 'bakers', 'pt': 'confeiteiros'}],
  'fast': {'q': 'What is this text about?', 'opts': ['Ordering coffee and watching a baking show', 'A trip to Brazil', 'Learning to swim'], 'ans': 0, 'why': 'Joy orders coffee, then they watch a baking show.'},
  'scan': [{'q': 'Where does Joy live?', 'ans': 'Seattle', 'alt': ['in seattle']}, {'q': 'What milk does Joy choose?', 'ans': 'oat milk', 'alt': ['oat']}, {'q': 'What does Joy eat?', 'ans': 'a blueberry muffin', 'alt': ['muffin', 'blueberry muffin']}],
  'tf': [{'s': 'Joy orders an iced latte.', 'ans': False, 'why': 'She says “Hot, please.”'}, {'s': 'Joy chooses a medium size.', 'ans': True, 'why': '“Medium. With oat milk.”'}, {'s': 'The Bake Off bakers work in a big tent.', 'ans': True, 'why': 'The text says they make cakes in a big tent.'}, {'s': 'The writer wants to bake a cake.', 'ans': True, 'why': '“I want to bake a cake, too.”'}],
  'order': ['Joy and the writer go to the café.', 'Joy orders a medium latte with oat milk.', 'She chooses a blueberry muffin.', 'They watch The Great British Bake Off.', 'The writer wants to bake a cake.'],
  'ctx': [{'sent': 'Her order was clear, short and polite.', 'w': 'polite', 'opts': ['nice and respectful', 'very long', 'loud'], 'ans': 0, 'why': 'Polite = respectful with please and thanks.'}, {'sent': 'Joy said, “I need my caffeine fix!”', 'w': 'fix', 'opts': ['a needed dose', 'a broken thing', 'a cold drink'], 'ans': 0, 'why': 'A caffeine fix = the coffee you need.'}, {'sent': 'Bakers follow a recipe.', 'w': 'recipe', 'opts': ['steps to make food', 'a kind of oven', 'a prize'], 'ans': 0, 'why': 'A recipe tells you how to make food.'}],
  'chunkHunt': ['What can I get started for you?', 'What size?', 'Hot or iced?', 'Anything to eat?'],
  'think': 'How do you like your coffee or tea? Say your order in English.'},
 'convo': {'npc': {'name': 'Mei'}, 'story': 'You are in a café in Seattle. Mei is the barista. Order your latte your way.', 'turns': [
  {'npc': 'Hi! What can I get started for you?', 'pt': 'Oi! O que posso preparar?', 'opts': [
   {'en': 'A latte, please.', 'pt': 'Um latte, por favor.', 'ok': True, 'fb': 'Short and polite.'},
   {'en': 'I am wanting a latte.', 'pt': 'Estou querendo um latte.', 'ok': False, 'fb': 'Use A latte, please or I’d like…'},
   {'en': 'Yes, I am fine.', 'pt': 'Sim, estou bem.', 'ok': False, 'fb': 'It does not answer the question.'}]},
  {'npc': 'What size? Small, medium or large?', 'pt': 'Que tamanho?', 'opts': [
   {'en': 'Medium size is good for me.', 'pt': 'Tamanho médio é bom para mim.', 'ok': False, 'fb': 'Too long. Say: Medium, please.'},
   {'en': 'Medium. With oat milk.', 'pt': 'Médio. Com leite de aveia.', 'ok': True, 'fb': 'Answer the size, then add the milk.'},
   {'en': 'At eight o’clock.', 'pt': 'Às oito horas.', 'ok': False, 'fb': 'It is about size, not time.'}]},
  {'npc': 'Hot or iced?', 'pt': 'Quente ou gelado?', 'opts': [
   {'en': 'I like very much.', 'pt': 'Eu gosto muito.', 'ok': False, 'fb': 'Choose: hot or iced.'},
   {'en': 'Cold hot.', 'pt': 'Frio quente.', 'ok': False, 'fb': 'Pick one word.'},
   {'en': 'Hot, please.', 'pt': 'Quente, por favor.', 'ok': True, 'fb': 'Pick one and add please.'}]},
  {'npc': 'Anything to eat?', 'pt': 'Algo para comer?', 'opts': [
   {'en': 'A blueberry muffin.', 'pt': 'Um muffin de mirtilo.', 'ok': True, 'fb': 'A + food is enough.'},
   {'en': 'I eat the muffin yesterday.', 'pt': 'Eu como o muffin ontem.', 'ok': False, 'fb': 'Wrong tense and not an order.'},
   {'en': 'Eat is good.', 'pt': 'Comer é bom.', 'ok': False, 'fb': 'It does not answer.'}]},
  {'npc': 'Have a great day!', 'pt': 'Tenha um ótimo dia!', 'opts': [
   {'en': 'You are welcome.', 'pt': 'De nada.', 'ok': False, 'fb': 'Use it after Thank you, not here.'},
   {'en': 'Good night!', 'pt': 'Boa noite!', 'ok': False, 'fb': 'It is not night.'},
   {'en': 'Thanks, you too!', 'pt': 'Obrigado, você também!', 'ok': True, 'fb': 'The natural answer.'}]}]},
 'errors': [
  {'wrong': 'I want a latte hot.', 'fix': 'I’d like a hot latte.', 'alt': 'I’d like a latte hot.', 'why': 'In English the adjective goes before the noun: a hot latte.'},
  {'wrong': 'Medium size, me.', 'fix': 'Medium, please.', 'alt': 'Medium size me.', 'why': 'Say the size, then please.'},
  {'wrong': 'Milk of oat.', 'fix': 'Oat milk.', 'alt': 'Milk oat.', 'why': 'The first noun describes the second: oat milk.'},
  {'wrong': 'I am wanting a muffin.', 'fix': 'I’d like a muffin.', 'alt': 'I am want a muffin.', 'why': 'Use I’d like or I want. Not “am wanting”.'}],
 'homework': 'Write and say your perfect café order in English: drink, size, milk and hot or iced.',
 'homework_items': ['Write your perfect coffee or tea order in 4 short lines.', 'Say it aloud twice and record it.', 'Listen to the dialogue again and shadow Mei.', 'Review: What size? / Hot or iced? / Anything to eat?']}
