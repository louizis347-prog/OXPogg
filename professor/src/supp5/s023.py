"""Suplemento Quest v5 · aula 23: Breakfast at the diner + regular Have Breakfast, Have Lunch (The Very Hungry Caterpillar)."""
SUPP = {
 'reg': 46,
 'badge': {'icon': '🥞', 'name': 'Diner Regular', 'desc': 'Order a full American breakfast'},
 'sticker': {'cat': 'Everyday culture', 'title': 'The Diner Breakfast', 'sub': 'How do you want your eggs?'},
 'culture': {
  'hook': 'A diner is a classic American restaurant with long counters, big menus and breakfast all day. Learn how to order eggs, pancakes and coffee with confidence.',
  'polite': 'Say **Yes, please** and **Thank you**. Servers often ask, **“Are you ready to order?”**',
  'mythfact': [
   {'s': 'Many American diners serve breakfast all day.', 'ans': True, 'why': 'You can often order pancakes and eggs in the afternoon.'},
   {'s': 'You only have one way to cook your eggs.', 'ans': False, 'why': 'The server asks: scrambled, fried (sunny-side up or over easy) or boiled.'},
   {'s': 'Pancakes usually come with syrup, often maple syrup.', 'ans': True, 'why': 'Syrup and butter are the typical toppings.'},
   {'s': 'In a diner, you pay before you sit down.', 'ans': False, 'why': 'In a diner the server brings the check at the end of the meal.'},
   {'s': 'Many diners bring more coffee to your cup.', 'ans': True, 'why': 'Refills of regular coffee are common in diners.'}],
  'wild': [
   {'kind': 'Diner menu', 'lines': ['**Pancake Stack** (3 pancakes)  $7', '**Two Eggs Any Style** with toast  $6', '**Bacon** on the side  $3', '**Orange juice**  $2.50'], 'decode': {'q': 'How much are two eggs with toast and a side of bacon?', 'opts': ['$9', '$10', '$13'], 'ans': 0, 'why': '$6 + $3 = $9.'}},
   {'kind': 'Server’s note', 'lines': ['Table 4', '1 coffee with milk', '1 pancakes + eggs, scrambled', 'No bacon, please'], 'decode': {'q': 'How does the customer want the eggs?', 'opts': ['Fried', 'Scrambled', 'Boiled'], 'ans': 1, 'why': 'The note says “eggs, scrambled”.'}}],
  'compare': {'br': 'In Brazil, breakfast is often pão com manteiga, café com leite and fruit, usually at home or at a padaria.', 'us': 'In an American diner, breakfast can be big: eggs, bacon, toast, pancakes and coffee. It is often a sit-down meal with friends.', 'tip': 'Learn the egg words: scrambled, fried and boiled. The server will ask!', 'ask': 'What do you eat for breakfast? Say it in English.'},
  'quiz': [
   {'q': 'The server says, “Table for one?” You say…', 'opts': ['Yes, please.', 'I am one.', 'No, a table.'], 'ans': 0, 'why': 'A short polite answer is perfect.'},
   {'q': '“How do you want your eggs?” A good answer is…', 'opts': ['Eggs, thanks.', 'Scrambled, please.', 'I want hungry.'], 'ans': 1, 'why': 'Name the style.'},
   {'q': 'What is a “diner”?', 'opts': ['A casual restaurant', 'A type of car', 'A hotel'], 'ans': 0, 'why': 'A diner is an informal restaurant with simple food.'}]},
 'reading': {
  'genre': 'Blog post', 'title': 'Breakfast with a hungry caterpillar',
  'text': [
   'Good morning! I am in **Philadelphia**, and **I’m starving**. This morning, I walk into a small diner near my hotel. The sign says, “Breakfast all day.”',
   'A server says, “**Table for one?**” I say, “**Yes, please.**” She brings the menu and a cup of coffee. “**Are you ready to order?**” she asks. I say, “**I’d like** pancakes and eggs, please.” “**How do you want your eggs?**” “Scrambled, please.”',
   'The food comes fast. The pancakes are big and warm, with butter and syrup. The eggs are soft and yellow. I eat toast too, and I drink my coffee with milk. **This is delicious!** The best breakfast ever.',
   'I think about a famous picture book, “The Very Hungry Caterpillar” by Eric Carle, from 1969. A tiny caterpillar is very hungry, and every day she eats more food. At the end she is not hungry, and she becomes a beautiful butterfly. I laugh. This morning, I feel like a very hungry caterpillar!',
   'I pay the check and leave a tip. The server says, “**Enjoy your day!**” Now I am full, and I am ready for a walk in the city.'],
  'glossary': [{'w': 'diner', 'pt': 'lanchonete tradicional'}, {'w': 'starving', 'pt': 'morrendo de fome'}, {'w': 'server', 'pt': 'garçom/garçonete'}, {'w': 'pancakes', 'pt': 'panquecas'}, {'w': 'scrambled', 'pt': 'mexidos'}, {'w': 'syrup', 'pt': 'calda'}, {'w': 'toast', 'pt': 'torrada'}, {'w': 'caterpillar', 'pt': 'lagarta'}, {'w': 'butterfly', 'pt': 'borboleta'}, {'w': 'full', 'pt': 'satisfeito'}],
  'fast': {'q': 'What is this text about?', 'opts': ['Breakfast in a diner in Philadelphia', 'A trip to the zoo', 'A job interview'], 'ans': 0, 'why': 'The writer eats breakfast in a diner.'},
  'scan': [{'q': 'What city is the writer in?', 'ans': 'Philadelphia', 'alt': []}, {'q': 'How does the writer want the eggs?', 'ans': 'scrambled', 'alt': ['scrambled eggs']}, {'q': 'Who wrote the caterpillar book?', 'ans': 'Eric Carle', 'alt': ['carle']}],
  'tf': [{'s': 'The diner is far from the hotel.', 'ans': False, 'why': 'It is near the hotel.'}, {'s': 'The writer orders pancakes and eggs.', 'ans': True, 'why': '“I’d like pancakes and eggs, please.”'}, {'s': 'The writer drinks tea.', 'ans': False, 'why': 'The writer drinks coffee with milk.'}, {'s': 'The writer leaves a tip.', 'ans': True, 'why': '“I pay the check and leave a tip.”'}],
  'order': ['The writer walks into a diner.', 'The server asks about a table.', 'The writer orders pancakes and eggs.', 'The food comes and it is delicious.', 'The writer pays and leaves a tip.'],
  'ctx': [{'sent': 'I’m starving, so I order two pancakes.', 'w': 'starving', 'opts': ['very hungry', 'very tired', 'very cold'], 'ans': 0, 'why': 'Starving = very hungry.'}, {'sent': 'The eggs are scrambled and soft.', 'w': 'scrambled', 'opts': ['broken and cooked together', 'cold', 'very hard'], 'ans': 0, 'why': 'Scrambled eggs are mixed while they cook.'}, {'sent': 'I feel full after breakfast.', 'w': 'full', 'opts': ['hungry', 'not hungry anymore', 'afraid'], 'ans': 1, 'why': 'Full = no more room for food.'}],
  'chunkHunt': ['Table for one?', 'Are you ready to order?', 'How do you want your eggs?', 'I’d like…'],
  'think': 'What is your perfect breakfast? How do you like your eggs?'},
 'convo': {'npc': {'name': 'Leo'}, 'story': 'You are in a diner in Philadelphia. Leo is the server. Order your breakfast.',
  'turns': [
   {'npc': 'Good morning! Table for one?', 'pt': 'Bom dia! Mesa para um?', 'opts': [
    {'en': 'Yes, please.', 'pt': 'Sim, por favor.', 'ok': True, 'fb': 'Short and polite.'},
    {'en': 'I am one.', 'pt': 'Eu sou um.', 'ok': False, 'fb': 'Not natural. Say Yes, please.'},
    {'en': 'Table is good.', 'pt': 'A mesa é boa.', 'ok': False, 'fb': 'It does not answer.'}]},
   {'npc': 'Here’s the menu. Coffee?', 'pt': 'Aqui está o cardápio. Café?', 'opts': [
    {'en': 'Coffee I want.', 'pt': 'Café eu quero.', 'ok': False, 'fb': 'Wrong word order.'},
    {'en': 'No, I am coffee.', 'pt': 'Não, eu sou café.', 'ok': False, 'fb': 'Wrong meaning.'},
    {'en': 'Yes, please. With milk.', 'pt': 'Sim, por favor. Com leite.', 'ok': True, 'fb': 'Add details with With…'}]},
   {'npc': 'Are you ready to order?', 'pt': 'Pronto para pedir?', 'opts': [
    {'en': 'I’d like pancakes and eggs.', 'pt': 'Eu gostaria de panquecas e ovos.', 'ok': True, 'fb': 'I’d like + noun is polite.'},
    {'en': 'I like to pancakes.', 'pt': 'Eu gosto de panquecas.', 'ok': False, 'fb': 'Say I’d like pancakes.'},
    {'en': 'I am ready to the eggs.', 'pt': 'Estou pronto para os ovos.', 'ok': False, 'fb': 'It does not order.'}]},
   {'npc': 'How do you want your eggs?', 'pt': 'Como quer seus ovos?', 'opts': [
    {'en': 'With salt, yes.', 'pt': 'Com sal, sim.', 'ok': False, 'fb': 'He asked how to cook them.'},
    {'en': 'Scrambled, please.', 'pt': 'Mexidos, por favor.', 'ok': True, 'fb': 'Name the egg style.'},
    {'en': 'Many eggs.', 'pt': 'Muitos ovos.', 'ok': False, 'fb': 'It does not say the style.'}]},
   {'npc': 'Enjoy your breakfast!', 'pt': 'Bom apetite!', 'opts': [
    {'en': 'Thank you, I enjoy.', 'pt': 'Obrigado, eu aprecio.', 'ok': False, 'fb': 'Say Thank you!'},
    {'en': 'Good night!', 'pt': 'Boa noite!', 'ok': False, 'fb': 'It is morning.'},
    {'en': 'Thank you!', 'pt': 'Obrigado!', 'ok': True, 'fb': 'Perfect.'}]}]},
 'errors': [
  {'wrong': 'I want pancake and egg.', 'fix': 'I’d like pancakes and eggs.', 'alt': 'I like pancakes and eggs now.', 'why': 'I’d like is polite; pancakes and eggs are plural.'},
  {'wrong': 'I am hungry of breakfast.', 'fix': 'I’m hungry. I want breakfast.', 'alt': 'I have hungry.', 'why': 'Use I’m hungry (not have).'},
  {'wrong': 'Eggs scramble, please.', 'fix': 'Scrambled eggs, please.', 'alt': 'Eggs scrambling, please.', 'why': 'Use the adjective scrambled before eggs.'},
  {'wrong': 'I eat the breakfast at eight.', 'fix': 'I have breakfast at eight.', 'alt': 'I make the breakfast at eight.', 'why': 'Say have breakfast, without the.'}],
 'homework': 'Write the menu of your perfect breakfast in English, then record yourself ordering it.',
 'homework_items': ['Write a 5-item breakfast menu.', 'Record yourself ordering it.', 'Shadow the dialogue with Leo.', 'Review: Table for one? / I’d like… / Scrambled, please.']}
