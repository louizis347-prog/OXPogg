"""Suplemento Quest v5 · aula 35: Fruit by the pound + regular Fresh Oranges, Please (Oranges and Lemons)."""
SUPP = {
 'reg': 48,
 'badge': {'icon': '🍓', 'name': 'Market Master', 'desc': 'Buy fruit by the pound and understand prices in English'},
 'culture': {
  'hook': 'At a farmers market in San Diego, fruit is sold by the pound or by the box, and the seller often says “That’s eleven dollars.” Learn to buy fruit like a local.',
  'mythfact': [
   {'s': 'In the USA, fruit is often sold by the pound.', 'ans': True, 'why': 'The pound (lb) is the common unit for weight in the USA.'},
   {'s': 'One pound is exactly one kilogram.', 'ans': False, 'why': 'One pound is about 0.45 kilograms, so a kilo is more than two pounds.'},
   {'s': 'A dozen means twelve.', 'ans': True, 'why': 'You can buy a dozen eggs or a dozen oranges.'},
   {'s': 'San Diego is in California.', 'ans': True, 'why': 'It is a coastal city in southern California.'},
   {'s': '“Oranges and Lemons” is a rhyme about bells of London churches.', 'ans': True, 'why': 'The rhyme mentions St. Clement’s and other church bells in London.'}],
  'wild': [
   {'kind': 'Market sign', 'lines': ['**Apples**  $2 a pound', '**Strawberries**  $5 a box', '**Oranges**  $1 each'], 'decode': {'q': 'How much are 3 pounds of apples?', 'opts': ['$6', '$2', '$5'], 'ans': 0, 'why': '3 x $2 = $6.'}},
   {'kind': 'Receipt', 'lines': ['Apples 3 lb  $6.00', 'Strawberries 1 box  $5.00', 'Total  $11.00'], 'decode': {'q': 'What is the total?', 'opts': ['$11', '$6', '$5'], 'ans': 0, 'why': '$6 + $5 = $11.'}}],
  'compare': {'br': 'In Brazil, fruit at the feira is sold by the kilo, or by unit or dozen, like the dúzia of bananas or oranges.', 'us': 'In the USA, you often hear “a pound of”, “a box of” or “a dozen”, and the sign shows the price per pound.', 'tip': 'Remember: one pound is a little less than half a kilo.', 'ask': 'What fruit do you buy? Say it in English.'},
  'quiz': [
   {'q': 'You want three pounds of apples. You say…', 'opts': ['I’ll take three pounds.', 'I take three pound.', 'Three apples pound.'], 'ans': 0, 'why': 'I’ll take + number + pounds.'},
   {'q': '“Five dollars a box” means…', 'opts': ['one box costs $5', 'five boxes cost $1', 'a box has five apples'], 'ans': 0, 'why': 'The price is for one box.'},
   {'q': 'How do you ask if a seller has strawberries?', 'opts': ['Do you have strawberries?', 'You have strawberries?', 'Have you strawberries?'], 'ans': 0, 'why': 'Use Do you have…?'}]},
 'reading': {
  'genre': 'Blog post',
  'title': 'Saturday at the market',
  'text': [
   'Every Saturday, my friend Lily goes to the farmers market in **San Diego**. The sun is warm, and the fruit is bright. Today I went with her.',
   'We stopped at a table full of apples. “**These apples look good**,” I said. The seller smiled. “**They’re fresh today. Two dollars a pound.**” I said, “**I’ll take three pounds.**” He put the apples on the scale. “**Okay. Anything else?**”',
   '“**Do you have strawberries?**” I asked. “**Yes. Five dollars a box.**” “**One box, please.**” “**That’s eleven dollars**,” he said. I paid, and he said, “**Enjoy your fruit!**” Lily laughed. “**What a steal!**” she said.',
   'On my way home, I thought about the old rhyme Oranges and Lemons. It is a game for children, and it talks about the bells of London. The rhyme also has a market feeling: oranges, lemons, a pound of this, a dozen of that.',
   'At home, I washed the strawberries and put the apples in a bowl. They were sweet and cold. I think I will go back next Saturday. Shopping at a market is slow, friendly and delicious.'],
  'glossary': [{'w': 'market', 'pt': 'feira'}, {'w': 'seller', 'pt': 'vendedor'}, {'w': 'pound', 'pt': 'libra'}, {'w': 'scale', 'pt': 'balança'}, {'w': 'box', 'pt': 'caixa'}, {'w': 'strawberries', 'pt': 'morangos'}, {'w': 'apples', 'pt': 'maçãs'}, {'w': 'dozen', 'pt': 'dúzia'}, {'w': 'bowl', 'pt': 'tigela'}],
  'fast': {'q': 'What is this text about?', 'opts': ['Buying fruit at a market', 'Cooking a big dinner', 'Visiting a museum'], 'ans': 0, 'why': 'The writer buys apples and strawberries.'},
  'scan': [{'q': 'How much are the apples per pound?', 'ans': '2 dollars', 'alt': ['two dollars', '$2', '2']}, {'q': 'How many pounds of apples does the writer buy?', 'ans': 'three', 'alt': ['3', 'three pounds']}, {'q': 'How much is the total?', 'ans': '11 dollars', 'alt': ['eleven dollars', '$11', '11']}],
  'tf': [{'s': 'The writer goes to a market in San Diego.', 'ans': True, 'why': 'The first paragraph says this.'}, {'s': 'Strawberries cost two dollars a box.', 'ans': False, 'why': 'Strawberries are five dollars a box.'}, {'s': 'The seller puts the apples on a scale.', 'ans': True, 'why': 'He puts them on the scale to weigh them.'}, {'s': 'The writer never wants to go back.', 'ans': False, 'why': 'They want to go back next Saturday.'}],
  'order': ['The writer arrives at the market.', 'The writer buys three pounds of apples.', 'The writer asks for strawberries.', 'The writer pays eleven dollars.', 'The writer eats the fruit at home.'],
  'ctx': [{'sent': 'They’re fresh today. Two dollars a pound.', 'w': 'fresh', 'opts': ['just picked', 'very old', 'very big'], 'ans': 0, 'why': 'Fresh = new and not old.'}, {'sent': 'What a steal! It is very cheap.', 'w': 'steal', 'opts': ['a great price', 'a thief', 'a hot day'], 'ans': 0, 'why': 'A steal = a very good price.'}, {'sent': 'He put the apples on the scale.', 'w': 'scale', 'opts': ['a tool to weigh', 'a fruit', 'a bag'], 'ans': 0, 'why': 'A scale shows weight.'}],
  'chunkHunt': ['Two dollars a pound.', 'I’ll take three pounds.', 'Do you have…?', 'That’s eleven dollars.'],
  'think': 'Where do you buy fruit? Is it by the kilo, the pound or by unit?'},
 'convo': {'npc': {'name': 'Victor'}, 'story': 'You sell fruit at a market in San Diego. Victor is a customer. Give prices and take his order.', 'turns': [
  {'npc': 'Hi! These apples look good.', 'pt': 'Oi! Essas maçãs estão boas.', 'opts': [
   {'en': 'They’re fresh today. Two dollars a pound.', 'pt': 'São frescas de hoje. Dois dólares a libra.', 'ok': True, 'fb': 'Give the price after you say they are fresh.'},
   {'en': 'They are bad.', 'pt': 'São ruins.', 'ok': False, 'fb': 'Not a good way to sell.'},
   {'en': 'I am two dollars.', 'pt': 'Eu sou dois dólares.', 'ok': False, 'fb': 'Wrong meaning.'}]},
  {'npc': 'I’ll take three pounds.', 'pt': 'Vou levar três libras.', 'opts': [
   {'en': 'Okay. Four dollars.', 'pt': 'Certo. Quatro dólares.', 'ok': False, 'fb': 'Three pounds x $2 = $6.'},
   {'en': 'Okay. Anything else?', 'pt': 'Certo. Mais alguma coisa?', 'ok': True, 'fb': 'Natural next question.'},
   {'en': 'Yes, I am three pounds.', 'pt': 'Sim, eu sou três libras.', 'ok': False, 'fb': 'Wrong meaning.'}]},
  {'npc': 'Do you have strawberries?', 'pt': 'Vocês têm morangos?', 'opts': [
   {'en': 'Yes. Five dollars a box.', 'pt': 'Temos. Cinco dólares a caixa.', 'ok': True, 'fb': 'Yes + price.'},
   {'en': 'Yes, I have five.', 'pt': 'Sim, eu tenho cinco.', 'ok': False, 'fb': 'It does not give the price.'},
   {'en': 'No, I am hungry.', 'pt': 'Não, estou com fome.', 'ok': False, 'fb': 'It does not answer.'}]},
  {'npc': 'One box, please.', 'pt': 'Uma caixa, por favor.', 'opts': [
   {'en': 'The box is eleven.', 'pt': 'A caixa é onze.', 'ok': False, 'fb': 'The total is $11, not the box.'},
   {'en': 'Here you go.', 'pt': 'Aqui está.', 'ok': False, 'fb': 'Give the price first.'},
   {'en': 'That’s eleven dollars.', 'pt': 'São onze dólares.', 'ok': True, 'fb': '$6 + $5 = $11.'}]},
  {'npc': 'Enjoy your fruit!', 'pt': 'Aproveite as frutas!', 'opts': [
   {'en': 'Thanks! See you next time.', 'pt': 'Valeu! Até a próxima.', 'ok': True, 'fb': 'Friendly goodbye.'},
   {'en': 'I enjoy yesterday.', 'pt': 'Eu aproveito ontem.', 'ok': False, 'fb': 'Wrong tense.'},
   {'en': 'You are enjoying.', 'pt': 'Você está aproveitando.', 'ok': False, 'fb': 'It does not make sense here.'}]}]},
 'errors': [
  {'wrong': 'Two dollar a pound.', 'fix': 'Two dollars a pound.', 'alt': 'Two dollars the pound.', 'why': 'More than one dollar needs -s.'},
  {'wrong': 'I want three pound.', 'fix': 'I’ll take three pounds.', 'alt': 'I want three pounds.', 'why': 'Use -s for pounds, and I’ll take… is natural when buying.'},
  {'wrong': 'How many is the strawberry?', 'fix': 'How much is a box of strawberries?', 'alt': 'How many cost strawberries?', 'why': 'For price use How much.'},
  {'wrong': 'A kilo of apples, please. (in the USA)', 'fix': 'Two pounds of apples, please.', 'alt': 'A kilogram of apples please.', 'why': 'In the USA, people use pounds, not kilos.'}],
 'homework': 'Make a fruit shopping list with prices and say what you buy and the total.',
 'homework_items': ['Write a list of 3 fruits with prices.', 'Say your order: I’ll take… Do you have…?', 'Listen to the dialogue again and shadow Victor.', 'Review: a pound of / a box of / a dozen.']}
