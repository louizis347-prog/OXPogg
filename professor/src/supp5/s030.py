"""Suplemento Quest v5 · aula 30: Build your bowl + regular Let's Cook! (MasterChef Junior)."""
SUPP = {
 'reg': 80,
 'badge': {'icon': '🥑', 'name': 'Bowl Builder', 'desc': 'Choose every layer of your own bowl'},
 'sticker': {'cat': 'Everyday culture', 'title': 'Build Your Own Bowl', 'sub': 'Salsa and cheese. No guacamole.'},
 'culture': {
  'hook': 'Many American fast restaurants let you build your own meal along a counter: you point, choose and the worker adds each layer. Learn the steps, in order, so you never freeze.',
  'polite': 'Choose one item at a time and say **please**. Say **No, thanks** or **No guacamole** if you do not want something.',
  'mythfact': [
   {'s': 'At a build-your-own bowl place, you choose each ingredient.', 'ans': True, 'why': 'The worker asks for rice, beans, toppings and sauce.'},
   {'s': 'The word “salsa” is Spanish for “sauce”.', 'ans': True, 'why': 'Salsa means sauce in Spanish.'},
   {'s': 'Guacamole is always free at American restaurants.', 'ans': False, 'why': 'Guacamole often costs extra.'},
   {'s': 'Phoenix, Arizona, has very hot summers.', 'ans': True, 'why': 'Summer days there are often above 100°F (38°C).'},
   {'s': '“Guacamole” is made mainly from tomatoes.', 'ans': False, 'why': 'Guacamole is mainly mashed avocado.'}],
  'wild': [
   {'kind': 'Bowl menu', 'lines': ['**Chicken bowl**  $9', '**Brown or white rice**  free', '**Guacamole**  +$2', '**Cheese · salsa**  free'], 'decode': {'q': 'How much is a chicken bowl with guacamole?', 'opts': ['$9', '$11', '$13'], 'ans': 1, 'why': '$9 + $2 = $11.'}},
   {'kind': 'Order screen', 'lines': ['**Protein:** chicken', '**Rice:** brown', '**Beans:** yes', '**Toppings:** salsa, cheese · no guacamole'], 'decode': {'q': 'Which topping is NOT in this order?', 'opts': ['Salsa', 'Cheese', 'Guacamole'], 'ans': 2, 'why': 'The screen says “no guacamole”.'}}],
  'compare': {'br': 'In Brazil, a “prato feito” or a self-service “por quilo” restaurant also lets you choose what goes on your plate.', 'us': 'In the USA, you often go down a line and say each choice to the worker: protein, rice, beans, toppings.', 'tip': 'Learn the order of the questions; the answers are one or two words.', 'ask': 'What would you put in your perfect bowl? Say it in English.'},
  'quiz': [
   {'q': 'Kai asks, “White rice or brown rice?” You say…', 'opts': ['Brown rice, please.', 'Yes, rice.', 'I am rice.'], 'ans': 0, 'why': 'Choose one.'},
   {'q': 'You do not want guacamole. You say…', 'opts': ['No guacamole, please.', 'I no guacamole.', 'Guacamole no want.'], 'ans': 0, 'why': 'No + noun is clear.'},
   {'q': '“That’s it” means…', 'opts': ['That is all', 'That is a bowl', 'That is hot'], 'ans': 0, 'why': 'That’s it = I don’t want anything else.'}]},
 'reading': {
  'genre': 'How-to guide', 'title': 'How to build your bowl',
  'text': [
   'Today, my friend Hector and I go to a bowl restaurant in **Phoenix**. The sun is hot, but the restaurant is cool. A man called Kai says, “Hi! **What kind of bowl?**”',
   '**First**, choose a protein. I say, “**A chicken bowl, please.**” **Then**, Kai asks, “**White rice or brown rice?**” “Brown rice, with beans,” I say. **Next**, he asks about toppings. “**Salsa? Cheese? Guacamole?**” I say, “**Salsa and cheese. No guacamole.**”',
   '**Finally**, Kai asks, “**Anything else?**” “No, **that’s it**. How much?” “Nine dollars,” he says. I pay, and he says, “**Enjoy your bowl!**” It looks so good. Hector says, “**That looks sick!**” and his bowl is full of everything.',
   'I love cooking shows. My favorite is “MasterChef Junior”, a show from 2013, where kids from eight to thirteen cook in a big kitchen. They use pots, pans and a stove. The judges say, “First, then, next, finally.” A bowl is a bit like a recipe too.',
   'At home, you can build a bowl in four steps: first, rice; then, beans; next, toppings; finally, sauce. **Load it up**, and **dig in**!'],
  'glossary': [{'w': 'bowl', 'pt': 'tigela'}, {'w': 'protein', 'pt': 'proteína'}, {'w': 'brown rice', 'pt': 'arroz integral'}, {'w': 'beans', 'pt': 'feijão'}, {'w': 'toppings', 'pt': 'coberturas'}, {'w': 'salsa', 'pt': 'molho de tomate'}, {'w': 'guacamole', 'pt': 'guacamole'}, {'w': 'judges', 'pt': 'jurados'}, {'w': 'stove', 'pt': 'fogão'}, {'w': 'recipe', 'pt': 'receita'}],
  'fast': {'q': 'What is this text about?', 'opts': ['Building a bowl step by step', 'A day at school', 'A ride on a train'], 'ans': 0, 'why': 'The writer chooses each part of a bowl.'},
  'scan': [{'q': 'What protein does the writer choose?', 'ans': 'chicken', 'alt': ['a chicken bowl']}, {'q': 'How much is the bowl?', 'ans': 'nine dollars', 'alt': ['9', '$9', '9 dollars']}, {'q': 'What year did MasterChef Junior start?', 'ans': '2013', 'alt': []}],
  'tf': [{'s': 'The writer chooses white rice.', 'ans': False, 'why': 'The writer chooses brown rice.'}, {'s': 'The writer says no to guacamole.', 'ans': True, 'why': '“No guacamole.”'}, {'s': 'The restaurant is in Phoenix.', 'ans': True, 'why': 'It is in Phoenix.'}, {'s': 'The bowl costs twelve dollars.', 'ans': False, 'why': 'It costs nine dollars.'}],
  'order': ['The friends enter the restaurant.', 'The writer chooses chicken.', 'The writer chooses brown rice and beans.', 'The writer chooses salsa and cheese.', 'The writer pays nine dollars.'],
  'ctx': [{'sent': 'First, choose rice.', 'w': 'First', 'opts': ['at the beginning', 'at the end', 'never'], 'ans': 0, 'why': 'First = step one.'}, {'sent': 'Load it up with beans and salsa.', 'w': 'Load it up', 'opts': ['Add a lot', 'Take it away', 'Throw it'], 'ans': 0, 'why': 'Load it up = fill it with a lot.'}, {'sent': 'No, that’s it, thanks.', 'w': 'that’s it', 'opts': ['that is all', 'that is hot', 'that is mine'], 'ans': 0, 'why': 'That’s it = nothing more.'}],
  'chunkHunt': ['What kind of bowl?', 'White rice or brown rice?', 'Anything else?', 'That’s it.'],
  'think': 'What do you put in your perfect bowl? Write the steps with First, Then, Next, Finally.'},
 'convo': {'npc': {'name': 'Kai'}, 'story': 'You are at a build-your-own bowl restaurant in Phoenix. Kai is the worker at the counter.',
  'turns': [
   {'npc': 'Hi! What kind of bowl?', 'pt': 'Oi! Que tipo de bowl?', 'opts': [
    {'en': 'I am a chicken bowl.', 'pt': 'Eu sou um bowl de frango.', 'ok': False, 'fb': 'Wrong meaning.'},
    {'en': 'Bowl chicken, yes.', 'pt': 'Bowl frango, sim.', 'ok': False, 'fb': 'Word order.'},
    {'en': 'A chicken bowl, please.', 'pt': 'Um bowl de frango, por favor.', 'ok': True, 'fb': 'Clear and polite.'}]},
   {'npc': 'White rice or brown rice?', 'pt': 'Arroz branco ou integral?', 'opts': [
    {'en': 'Brown rice. With beans.', 'pt': 'Arroz integral. Com feijão.', 'ok': True, 'fb': 'Choose and add.'},
    {'en': 'Yes, rice.', 'pt': 'Sim, arroz.', 'ok': False, 'fb': 'Choose white or brown.'},
    {'en': 'Rice is good.', 'pt': 'Arroz é bom.', 'ok': False, 'fb': 'It does not choose.'}]},
   {'npc': 'Salsa? Cheese? Guacamole?', 'pt': 'Molho? Queijo? Guacamole?', 'opts': [
    {'en': 'No guacamole I want.', 'pt': 'Sem guacamole eu quero.', 'ok': False, 'fb': 'Word order.'},
    {'en': 'I am salsa and cheese.', 'pt': 'Eu sou molho e queijo.', 'ok': False, 'fb': 'Wrong meaning.'},
    {'en': 'Salsa and cheese. No guacamole.', 'pt': 'Molho e queijo. Sem guacamole.', 'ok': True, 'fb': 'Say yes to some, no to one.'}]},
   {'npc': 'Anything else?', 'pt': 'Mais alguma coisa?', 'opts': [
    {'en': 'No, that’s it. How much?', 'pt': 'Não, é isso. Quanto custa?', 'ok': True, 'fb': 'Close the order.'},
    {'en': 'Yes, nothing.', 'pt': 'Sim, nada.', 'ok': False, 'fb': 'Confusing.'},
    {'en': 'I am finished eat.', 'pt': 'Eu terminei comer.', 'ok': False, 'fb': 'Not natural.'}]},
   {'npc': 'Enjoy your bowl!', 'pt': 'Aproveite seu bowl!', 'opts': [
    {'en': 'Good morning!', 'pt': 'Bom dia!', 'ok': False, 'fb': 'Not the right reply.'},
    {'en': 'Thanks! You too!', 'pt': 'Valeu! Você também!', 'ok': True, 'fb': 'Natural.'},
    {'en': 'I enjoy it yes.', 'pt': 'Eu aprecio sim.', 'ok': False, 'fb': 'Say Thanks!'}]}]},
 'errors': [
  {'wrong': 'I want a bowl of chicken.', 'fix': 'I’d like a chicken bowl.', 'alt': 'I want a bowl chicken.', 'why': 'Chicken goes before bowl.'},
  {'wrong': 'With no guacamole.', 'fix': 'No guacamole, please.', 'alt': 'Without guacamole yes.', 'why': 'No guacamole is short and clear.'},
  {'wrong': 'First I choosing the rice.', 'fix': 'First, I choose the rice.', 'alt': 'First I chose to the rice.', 'why': 'Use the base verb choose after I.'},
  {'wrong': 'How much costs?', 'fix': 'How much is it?', 'alt': 'How many is it?', 'why': 'Ask the price with How much is it?'}],
 'homework': 'Write the 4 steps of your perfect bowl with First, Then, Next and Finally, then say them aloud.',
 'homework_items': ['Write 4 steps with First, Then, Next, Finally.', 'Record your order at the counter.', 'Shadow the dialogue with Kai.', 'Review: What kind of bowl? / No guacamole. / That’s it.']}
