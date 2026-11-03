"""Suplemento Quest v5 · aula 24: Ordering lunch + regular Split the Check (Check, Please!)."""
SUPP = {
 'reg': 13,
 'badge': {'icon': '🥪', 'name': 'Lunch Pro', 'desc': 'Build a sandwich and ask for the check'},
 'sticker': {'cat': 'Everyday culture', 'title': 'The Sandwich Counter', 'sub': 'White or wheat?'},
 'culture': {
  'hook': 'At an American sandwich counter, you make many small choices: bread, cheese, vegetables and a side. Learn the questions and answers so you can order lunch quickly.',
  'polite': 'Answer each question with a short choice and **please**: **Wheat, please.** At the end, say **Thanks!**',
  'mythfact': [
   {'s': 'At a sandwich shop, you can choose your bread.', 'ans': True, 'why': 'The server asks: white, wheat or another bread.'},
   {'s': 'In the USA, “chips” are hot potato sticks.', 'ans': False, 'why': 'In the USA, “chips” are thin potato slices in a bag; hot sticks are “fries”.'},
   {'s': 'Many restaurants give you a box for your leftovers.', 'ans': True, 'why': 'You can ask, “Can I get a box, please?”'},
   {'s': 'The price on the menu usually includes tax.', 'ans': False, 'why': 'In most US states, sales tax is added at the register.'},
   {'s': 'You can say “Check, please!” to ask for the bill.', 'ans': True, 'why': 'In the USA, the bill at a restaurant is called the check.'}],
  'wild': [
   {'kind': 'Lunch menu', 'lines': ['**Turkey Sandwich**  $9', '**Add cheese**  +$1', '**Side:** fries or salad', '**Soda**  $2'], 'decode': {'q': 'How much is a turkey sandwich with cheese and a soda?', 'opts': ['$11', '$12', '$13'], 'ans': 1, 'why': '$9 + $1 + $2 = $12.'}},
   {'kind': 'Receipt', 'lines': ['**Sandwich** · $9.00', '**Salad** · $0.00', '**Tax** · $0.80', '**Total** · $9.80'], 'decode': {'q': 'What is the total?', 'opts': ['$9.00', '$9.80', '$0.80'], 'ans': 1, 'why': 'The last line says Total $9.80.'}}],
  'compare': {'br': 'In Brazil, lunch is often a hot meal of rice, beans and meat, sometimes a self-service “por quilo” restaurant.', 'us': 'In the USA, lunch is often a sandwich, a salad or a quick meal, and it is shorter. You build it with questions and choices.', 'tip': 'Do not say “yes” to every question; choose: “Wheat, please.”', 'ask': 'What is your favorite lunch? Say it in English.'},
  'quiz': [
   {'q': 'Marco asks, “White or wheat bread?” You say…', 'opts': ['Wheat, please.', 'Yes, bread.', 'I bread.'], 'ans': 0, 'why': 'Choose one option.'},
   {'q': 'What do you say to ask for the bill?', 'opts': ['Check, please!', 'Number, please!', 'Money, now!'], 'ans': 0, 'why': 'Check, please! is the usual phrase.'},
   {'q': '“Fries or a salad?” means…', 'opts': ['Two sides, choose one', 'Pay now', 'Go home'], 'ans': 0, 'why': 'It is a choice of side dish.'}]},
 'reading': {
  'genre': 'Blog post', 'title': 'Lunch in Los Angeles',
  'text': [
   'Today I am in **Los Angeles**, and it is lunchtime. My friends say, “**Let’s grab lunch!** I know **a great spot**.” We walk to a small sandwich shop near the beach.',
   'The line is short. A man behind the counter says, “Hi! What can I get you?” I say, “**Can I have** a turkey sandwich?” “**White or wheat?**” “Wheat, please.” “**Any cheese? Lettuce? Tomato?**” “Yes, all of them.” “**Fries or a salad?**” “A salad, please.” Then he says, “**Enjoy your lunch!**”',
   'My friend Mia orders chicken, and Ben orders a cheese sandwich. It is not expensive, and it is **super tasty**. We sit outside and eat in the sun.',
   'The comic “Check, Please!” by Ngozi Ukazu started in 2013. In it, a college student called Eric loves to bake, joins a hockey team and makes new friends. The title is a joke: a “check” is a hockey move, and “Check, please!” is also what you say at a restaurant.',
   'After lunch, I say, “**Check, please!**” and the waiter brings the bill. We **split the check**. It is easy: everybody pays for their own food. I leave a small tip, and we walk to the beach.'],
  'glossary': [{'w': 'lunchtime', 'pt': 'hora do almoço'}, {'w': 'grab', 'pt': 'pegar (rápido)'}, {'w': 'spot', 'pt': 'lugar'}, {'w': 'counter', 'pt': 'balcão'}, {'w': 'wheat', 'pt': 'integral'}, {'w': 'lettuce', 'pt': 'alface'}, {'w': 'tasty', 'pt': 'gostoso'}, {'w': 'comic', 'pt': 'história em quadrinhos'}, {'w': 'bill', 'pt': 'conta'}, {'w': 'split', 'pt': 'dividir'}],
  'fast': {'q': 'What is this text about?', 'opts': ['Ordering lunch in Los Angeles', 'A holiday in Spain', 'A birthday party'], 'ans': 0, 'why': 'The writer orders a sandwich for lunch.'},
  'scan': [{'q': 'What bread does the writer choose?', 'ans': 'wheat', 'alt': ['wheat bread']}, {'q': 'Does the writer choose fries or salad?', 'ans': 'salad', 'alt': ['a salad']}, {'q': 'Who wrote “Check, Please!”?', 'ans': 'Ngozi Ukazu', 'alt': ['ukazu']}],
  'tf': [{'s': 'The sandwich shop is near the beach.', 'ans': True, 'why': '“A small sandwich shop near the beach.”'}, {'s': 'The writer wants white bread.', 'ans': False, 'why': 'The writer says wheat.'}, {'s': 'The friends eat inside.', 'ans': False, 'why': 'They sit outside.'}, {'s': 'The friends split the check.', 'ans': True, 'why': 'Everybody pays for their own food.'}],
  'order': ['The friends walk to the sandwich shop.', 'The writer orders a turkey sandwich.', 'They eat outside in the sun.', 'The writer asks for the check.', 'They split the bill and walk to the beach.'],
  'ctx': [{'sent': 'Let’s grab lunch together.', 'w': 'grab', 'opts': ['drop', 'get quickly', 'cook'], 'ans': 1, 'why': 'Grab lunch = get lunch quickly.'}, {'sent': 'The sandwich is super tasty.', 'w': 'tasty', 'opts': ['delicious', 'cold', 'old'], 'ans': 0, 'why': 'Tasty = good to eat.'}, {'sent': 'We split the bill.', 'w': 'split', 'opts': ['break', 'share the cost', 'forget'], 'ans': 1, 'why': 'Split the bill = each person pays a part.'}],
  'chunkHunt': ['What can I get you?', 'White or wheat?', 'Fries or a salad?', 'Check, please!'],
  'think': 'What do you put in your perfect sandwich? Do you split the check with friends?'},
 'convo': {'npc': {'name': 'Marco'}, 'story': 'You are at a sandwich counter in Los Angeles. Marco is the server. Order lunch.',
  'turns': [
   {'npc': 'Hi! What can I get you?', 'pt': 'Oi! O que posso servir?', 'opts': [
    {'en': 'Can I have a turkey sandwich?', 'pt': 'Posso pegar um sanduíche de peru?', 'ok': True, 'fb': 'Natural and polite.'},
    {'en': 'I am a turkey sandwich.', 'pt': 'Eu sou um sanduíche de peru.', 'ok': False, 'fb': 'Wrong meaning.'},
    {'en': 'Give me sandwich turkey.', 'pt': 'Me dá sanduíche peru.', 'ok': False, 'fb': 'Word order and tone.'}]},
   {'npc': 'Sure. White or wheat bread?', 'pt': 'Claro. Pão branco ou integral?', 'opts': [
    {'en': 'Yes, bread.', 'pt': 'Sim, pão.', 'ok': False, 'fb': 'Choose white or wheat.'},
    {'en': 'Wheat, please.', 'pt': 'Integral, por favor.', 'ok': True, 'fb': 'Choose one.'},
    {'en': 'I wheat.', 'pt': 'Eu integral.', 'ok': False, 'fb': 'Use a short answer.'}]},
   {'npc': 'Any cheese? Lettuce? Tomato?', 'pt': 'Queijo? Alface? Tomate?', 'opts': [
    {'en': 'No, I am cheese.', 'pt': 'Não, eu sou queijo.', 'ok': False, 'fb': 'Wrong meaning.'},
    {'en': 'Yes, all of them.', 'pt': 'Sim, tudo isso.', 'ok': True, 'fb': 'All of them = everything.'},
    {'en': 'Yes, is good.', 'pt': 'Sim, é bom.', 'ok': False, 'fb': 'It does not choose.'}]},
   {'npc': 'Would you like fries or a salad?', 'pt': 'Quer batata frita ou salada?', 'opts': [
    {'en': 'A salad, please.', 'pt': 'Uma salada, por favor.', 'ok': True, 'fb': 'Clear choice.'},
    {'en': 'I like salad of fries.', 'pt': 'Gosto de salada de batata.', 'ok': False, 'fb': 'Choose one: A salad, please.'},
    {'en': 'Fries salad.', 'pt': 'Batata salada.', 'ok': False, 'fb': 'Not a full answer.'}]},
   {'npc': 'Enjoy your lunch!', 'pt': 'Bom almoço!', 'opts': [
    {'en': 'Good night!', 'pt': 'Boa noite!', 'ok': False, 'fb': 'It is lunchtime.'},
    {'en': 'I enjoy, thanks.', 'pt': 'Eu aprecio, valeu.', 'ok': False, 'fb': 'Say Thanks, you too!'},
    {'en': 'Thanks! You too!', 'pt': 'Valeu! Você também!', 'ok': True, 'fb': 'A natural reply.'}]}]},
 'errors': [
  {'wrong': 'I want a sandwich of turkey.', 'fix': 'I’d like a turkey sandwich.', 'alt': 'Give me a sandwich turkey.', 'why': 'Put the noun turkey before sandwich.'},
  {'wrong': 'I will to take a salad.', 'fix': 'I’ll have a salad.', 'alt': 'I take a salad.', 'why': 'Order with I’ll have; no to after will.'},
  {'wrong': 'The account, please.', 'fix': 'The check, please.', 'alt': 'The money, please.', 'why': 'In the USA, “check” is the usual word.'},
  {'wrong': 'Can I have a sandwich with a cheese?', 'fix': 'Can I have a sandwich with cheese?', 'alt': 'Can I have a sandwich with cheeses?', 'why': 'Cheese is uncountable, so no a.'}],
 'homework': 'Write your perfect lunch order in English and practice saying it aloud three times.',
 'homework_items': ['Write your lunch order: bread, filling, side.', 'Record yourself ordering it.', 'Shadow the dialogue with Marco.', 'Review: What can I get you? / White or wheat? / Check, please!']}
