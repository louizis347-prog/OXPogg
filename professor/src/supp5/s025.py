"""Suplemento Quest v5 · aula 25: Pizza by the slice + regular Ten Dollars, Please (This Old Man)."""
SUPP = {
 'reg': 10,
 'badge': {'icon': '🍕', 'name': 'Slice Master', 'desc': 'Order a slice, a drink and pay in dollars'},
 'sticker': {'cat': 'Everyday culture', 'title': 'The New York Slice', 'sub': 'Fold it like this!'},
 'culture': {
  'hook': 'In New York City, you can buy pizza by the slice and eat it on the street in two minutes. Learn how to order, pay and eat it like a New Yorker.',
  'polite': 'Say **Can I get…?** or **Two slices, please**, then **Thanks!** Keep it short; the line is moving.',
  'mythfact': [
   {'s': 'In New York, many pizza shops sell single slices.', 'ans': True, 'why': 'You can order one, two or more slices and eat right away.'},
   {'s': 'People often fold a New York slice before they eat it.', 'ans': True, 'why': 'The slice is large and thin, so folding it is easy and clean.'},
   {'s': 'Pepperoni is a very common topping in the USA.', 'ans': True, 'why': 'Pepperoni is one of the most popular pizza toppings in the USA.'},
   {'s': 'You must use a knife and a fork to eat a slice.', 'ans': False, 'why': 'Most people eat a slice with their hands.'},
   {'s': 'A “soda” in the USA is a type of cake.', 'ans': False, 'why': 'A soda is a fizzy soft drink.'}],
  'wild': [
   {'kind': 'Pizza shop menu', 'lines': ['**Cheese slice**  $3', '**Pepperoni slice**  $3.50', '**Soda (small)**  $2 · **(large)**  $3'], 'decode': {'q': 'How much are one pepperoni slice and a large soda?', 'opts': ['$6.50', '$5.50', '$7'], 'ans': 0, 'why': '$3.50 + $3 = $6.50.'}},
   {'kind': 'Sign on the counter', 'lines': ['**Cash or card**', 'Napkins are free', 'Please do not sit without ordering'], 'decode': {'q': 'How can you pay?', 'opts': ['Only cash', 'Cash or card', 'Only a gift'], 'ans': 1, 'why': 'The sign says “Cash or card.”'}}],
  'compare': {'br': 'In Brazil, pizza is often a whole pie shared by a group, at a pizzeria or delivery, with a knife and fork or by hand.', 'us': 'In New York, a quick slice is a street meal: you stand, eat with your hands and pay a few dollars.', 'tip': 'Know your numbers: three dollars is “three dollars”, not “three”.', 'ask': 'How do you eat pizza? With your hands or knife and fork? Say it in English.'},
  'quiz': [
   {'q': 'Ravi asks, “What can I get you?” You say…', 'opts': ['Two slices of pepperoni, please.', 'I get you two.', 'Pizza is New York.'], 'ans': 0, 'why': 'Say how many and what.'},
   {'q': 'The price is eight dollars. You give the money and say…', 'opts': ['Here you go. Thanks!', 'It is a dollar.', 'You are welcome!'], 'ans': 0, 'why': 'Here you go = take it.'},
   {'q': 'A “slice” is…', 'opts': ['A piece of pizza', 'A whole pizza', 'A kind of cheese'], 'ans': 0, 'why': 'A slice is one piece.'}]},
 'reading': {
  'genre': 'Travel diary', 'title': 'My first slice in New York',
  'text': [
   'Today I am in **New York**, and I am very hungry. On the corner, I see a pizza shop with a big sign: “Pizza by the slice.” I go in.',
   'A man called Ravi says, “Hi! **What can I get you?**” I say, “**Two slices of pepperoni, please.**” He puts the slices in a hot oven, and in a minute they are ready. “**Anything to drink?**” he asks. “A soda, please.” “**Small or large?**” “Large. **How much is it?**” “**That’s eight dollars.**” I say, “**Here you go. Thanks!**” and he says, “**Enjoy your pizza!**”',
   'The slices are huge! A woman next to me **folds** her slice in half and eats it with her hands. I do the same. It is hot, cheesy and so good. A man says, “**New York style, baby!**”',
   'I remember a song from my English class, “This Old Man”. It is a British counting song, written down in the early 1900s. It counts from one to ten, and each number has a rhyme. I count my dollars too: one, two, three… up to ten.',
   'I give Ravi ten dollars, and he gives me two dollars back. “**Keep the change**,” I say, and I smile. It is a great lunch, and it costs only a few dollars.'],
  'glossary': [{'w': 'slice', 'pt': 'fatia'}, {'w': 'corner', 'pt': 'esquina'}, {'w': 'oven', 'pt': 'forno'}, {'w': 'huge', 'pt': 'enorme'}, {'w': 'folds', 'pt': 'dobra'}, {'w': 'cheesy', 'pt': 'com muito queijo'}, {'w': 'counting', 'pt': 'de contar'}, {'w': 'dollars', 'pt': 'dólares'}, {'w': 'change', 'pt': 'troco'}, {'w': 'soda', 'pt': 'refrigerante'}],
  'fast': {'q': 'What is this text about?', 'opts': ['Buying pizza by the slice in New York', 'A bus ride in London', 'A movie about a farm'], 'ans': 0, 'why': 'The writer buys pizza slices in New York.'},
  'scan': [{'q': 'How many slices does the writer order?', 'ans': 'two', 'alt': ['2', 'two slices']}, {'q': 'How much is it?', 'ans': 'eight dollars', 'alt': ['8', '$8', '8 dollars']}, {'q': 'What does the woman do with her slice?', 'ans': 'folds it', 'alt': ['fold', 'folds it in half']}],
  'tf': [{'s': 'The pizza shop sells whole pizzas only.', 'ans': False, 'why': 'The sign says “Pizza by the slice.”'}, {'s': 'The writer orders a large soda.', 'ans': True, 'why': '“Large. How much is it?”'}, {'s': 'The writer pays nine dollars.', 'ans': False, 'why': 'The price is eight dollars; the writer gives ten.'}, {'s': 'The writer eats with hands.', 'ans': True, 'why': 'The writer folds the slice and eats it.'}],
  'order': ['The writer sees the pizza shop.', 'The writer orders two slices.', 'The writer asks for a large soda.', 'The writer folds a slice and eats.', 'The writer pays and says keep the change.'],
  'ctx': [{'sent': 'The slice is huge!', 'w': 'huge', 'opts': ['very small', 'very big', 'very cold'], 'ans': 1, 'why': 'Huge = very big.'}, {'sent': 'She folds her slice in half.', 'w': 'folds', 'opts': ['bends', 'cuts', 'cooks'], 'ans': 0, 'why': 'Fold = bend over itself.'}, {'sent': 'Keep the change, please.', 'w': 'change', 'opts': ['the extra money returned', 'a new shirt', 'a different pizza'], 'ans': 0, 'why': 'Change = the money returned to you.'}],
  'chunkHunt': ['What can I get you?', 'Small or large?', 'How much is it?', 'Here you go.'],
  'think': 'Do you like pizza? What toppings do you like? What do you pay for a slice where you live?'},
 'convo': {'npc': {'name': 'Ravi'}, 'story': 'You are in a pizza shop in New York. Ravi works at the counter. Order and pay.',
  'turns': [
   {'npc': 'Hi! What can I get you?', 'pt': 'Oi! O que vai ser?', 'opts': [
    {'en': 'Pizza I want, two.', 'pt': 'Pizza eu quero, duas.', 'ok': False, 'fb': 'Wrong word order.'},
    {'en': 'I get you pizza.', 'pt': 'Eu te dou pizza.', 'ok': False, 'fb': 'Wrong meaning.'},
    {'en': 'Two slices of pepperoni, please.', 'pt': 'Duas fatias de pepperoni, por favor.', 'ok': True, 'fb': 'Number + slices of + topping.'}]},
   {'npc': 'Anything to drink?', 'pt': 'Algo para beber?', 'opts': [
    {'en': 'A soda, please.', 'pt': 'Um refrigerante, por favor.', 'ok': True, 'fb': 'Short and polite.'},
    {'en': 'I drink not.', 'pt': 'Eu bebo não.', 'ok': False, 'fb': 'Use No, thanks.'},
    {'en': 'Water of soda.', 'pt': 'Água de refri.', 'ok': False, 'fb': 'Not natural.'}]},
   {'npc': 'Small or large?', 'pt': 'Pequeno ou grande?', 'opts': [
    {'en': 'Yes, soda.', 'pt': 'Sim, refri.', 'ok': False, 'fb': 'Choose small or large.'},
    {'en': 'Large. How much is it?', 'pt': 'Grande. Quanto custa?', 'ok': True, 'fb': 'Choose and ask the price.'},
    {'en': 'I am large.', 'pt': 'Eu sou grande.', 'ok': False, 'fb': 'Wrong meaning.'}]},
   {'npc': 'That’s eight dollars.', 'pt': 'São oito dólares.', 'opts': [
    {'en': 'Eight is my number.', 'pt': 'Oito é meu número.', 'ok': False, 'fb': 'Not a reply.'},
    {'en': 'Here you go. Thanks!', 'pt': 'Aqui está. Valeu!', 'ok': True, 'fb': 'Hand over the money.'},
    {'en': 'I have eight years.', 'pt': 'Eu tenho oito anos.', 'ok': False, 'fb': 'Wrong meaning.'}]},
   {'npc': 'Enjoy your pizza!', 'pt': 'Bom apetite!', 'opts': [
    {'en': 'Good night!', 'pt': 'Boa noite!', 'ok': False, 'fb': 'Not the right reply.'},
    {'en': 'Thanks! Bye!', 'pt': 'Valeu! Tchau!', 'ok': True, 'fb': 'Natural.'},
    {'en': 'I enjoy it very.', 'pt': 'Eu aproveito muito.', 'ok': False, 'fb': 'Say Thanks!'}]}]},
 'errors': [
  {'wrong': 'I want two slice of pizza.', 'fix': 'I’d like two slices of pizza.', 'alt': 'I want two slices pizza.', 'why': 'Two needs the plural slices.'},
  {'wrong': 'How many costs?', 'fix': 'How much is it?', 'alt': 'How much costs?', 'why': 'For price, say How much is it?'},
  {'wrong': 'It is eight dollar.', 'fix': 'It is eight dollars.', 'alt': 'It are eight dollars.', 'why': 'After eight, use the plural dollars.'},
  {'wrong': 'I will take a soda large.', 'fix': 'I’ll have a large soda.', 'alt': 'I’ll have a soda of large.', 'why': 'The adjective large comes before soda.'}],
 'homework': 'Write a short order for a friend: two slices, a drink and the price, and say it aloud.',
 'homework_items': ['Write a pizza-shop order with prices.', 'Say numbers 1 to 10 in dollars.', 'Shadow the dialogue with Ravi.', 'Review: What can I get you? / Small or large? / How much is it?']}
