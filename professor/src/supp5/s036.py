"""Suplemento Quest v5 · aula 36: Burger combo + regular Have Breakfast, Have Lunch (The Very Hungry Caterpillar)."""
SUPP = {
 'reg': 46,
 'badge': {'icon': '🍔', 'name': 'Combo Champion', 'desc': 'Order a burger combo and say no thanks politely in English'},
 'culture': {
  'hook': 'In a burger place in Milwaukee, you say your order, hear one question about a combo and move on. Learn how to order fast food without stress.',
  'mythfact': [
   {'s': 'A combo meal usually includes a main food, fries and a drink.', 'ans': True, 'why': 'A burger combo is typically a burger, fries and a drink in one price.'},
   {'s': 'In the USA, people always call a soft drink “cola”.', 'ans': False, 'why': 'Many say “soda”, and some regions say “pop” or the brand name.'},
   {'s': 'Milwaukee is in the state of Wisconsin.', 'ans': True, 'why': 'It is the biggest city in Wisconsin, on Lake Michigan.'},
   {'s': 'It is rude to say “No, thanks. That’s all.”', 'ans': False, 'why': 'It is a normal and polite way to end an order.'},
   {'s': '“The Very Hungry Caterpillar” was written by Eric Carle.', 'ans': True, 'why': 'The picture book came out in 1969.'}],
  'wild': [
   {'kind': 'Menu board', 'lines': ['**Cheeseburger**  $6', '**Combo** (burger + fries + drink)  $9', '**Extra ketchup**  free'], 'decode': {'q': 'How much more is the combo than the burger alone?', 'opts': ['$3', '$9', '$6'], 'ans': 0, 'why': '$9 - $6 = $3.'}},
   {'kind': 'Order screen', 'lines': ['Your order: 1 Cheeseburger Combo', 'Drink: Cola', 'Order number: 47'], 'decode': {'q': 'What is the order number?', 'opts': ['47', '1', '9'], 'ans': 0, 'why': '“Order number: 47.”'}}],
  'compare': {'br': 'In Brazil, a “combo” or “promoção” at a lanchonete is also common, and you may order at a counter or from an app.', 'us': 'In the USA, the cashier usually asks “Do you want a combo?” and “Anything else?”.', 'tip': 'Say “No, thanks. That’s all.” to finish your order.', 'ask': 'What is your favorite fast-food combo? Say it in English.'},
  'quiz': [
   {'q': 'The cashier asks: “Do you want a combo?” You want to know what is in it. You say…', 'opts': ['What comes with it?', 'What is combo?', 'I combo.'], 'ans': 0, 'why': 'What comes with it? asks about the extras.'},
   {'q': 'You do not want anything else. You say…', 'opts': ['No, thanks. That’s all.', 'No more nothing.', 'I am finished food.'], 'ans': 0, 'why': 'That’s all = I want nothing more.'},
   {'q': 'The cashier says “Enjoy your burger!” You answer…', 'opts': ['Thanks!', 'Yes, I have.', 'Good morning.'], 'ans': 0, 'why': 'Thanks is the natural answer.'}]},
 'reading': {
  'genre': 'Blog post',
  'title': 'My burger day',
  'text': [
   'I am in **Milwaukee**, and I am very hungry. It is like the story of The Very Hungry Caterpillar: today I want to eat a lot! My friend Gus takes me to a burger place.',
   'The cashier, Malik, smiles. “**Welcome! What can I get you?**” I say, “**A cheeseburger, please.**” He asks, “**Do you want a combo?**” I am not sure, so I ask, “**What comes with it?**” “**Fries and a drink**,” he says.',
   'That sounds good. “**OK. A combo, and a cola.**” “**Anything else?**” “**No, thanks. That’s all.**” Gus laughs because he wants lemonade and extra ketchup. The tray is full: a burger, fries and a cold drink.',
   '“**Enjoy your burger!**” Malik says. I take a big bite. It is hot and tasty. Gus says, “**Let’s supersize it!**” but I say, “No, I feel full.” That is a good ending: not too much, not too little.',
   'The caterpillar in the book becomes a butterfly after a big meal. I just became a very happy customer. Next time I will say, “I’m so hungry!” again, but maybe I will order a salad.'],
  'glossary': [{'w': 'hungry', 'pt': 'com fome'}, {'w': 'cashier', 'pt': 'caixa (atendente)'}, {'w': 'cheeseburger', 'pt': 'hambúrguer com queijo'}, {'w': 'combo', 'pt': 'combo'}, {'w': 'fries', 'pt': 'batata frita'}, {'w': 'drink', 'pt': 'bebida'}, {'w': 'lemonade', 'pt': 'limonada'}, {'w': 'ketchup', 'pt': 'ketchup'}, {'w': 'full', 'pt': 'satisfeito'}],
  'fast': {'q': 'What is this text about?', 'opts': ['Ordering a burger combo', 'Going to school', 'Playing baseball'], 'ans': 0, 'why': 'The writer orders a cheeseburger combo.'},
  'scan': [{'q': 'What does the combo come with?', 'ans': 'fries and a drink', 'alt': ['fries', 'a drink', 'fries and drink']}, {'q': 'What drink does the writer order?', 'ans': 'cola', 'alt': ['a cola']}, {'q': 'Who wants lemonade?', 'ans': 'Gus', 'alt': ['gus']}],
  'tf': [{'s': 'The writer orders a cheeseburger.', 'ans': True, 'why': '“A cheeseburger, please.”'}, {'s': 'The combo comes with a salad.', 'ans': False, 'why': 'It comes with fries and a drink.'}, {'s': 'The writer asks for something more.', 'ans': False, 'why': 'The writer says “No, thanks. That’s all.”'}, {'s': 'Malik is the cashier.', 'ans': True, 'why': 'Malik takes the order.'}],
  'order': ['The writer feels very hungry.', 'The writer orders a cheeseburger.', 'Malik asks about a combo.', 'The writer says that is all.', 'The writer eats the burger.'],
  'ctx': [{'sent': 'I am very hungry. I want to eat a lot.', 'w': 'hungry', 'opts': ['needing food', 'needing sleep', 'needing water only'], 'ans': 0, 'why': 'Hungry = wanting food.'}, {'sent': 'The tray is full of food.', 'w': 'full', 'opts': ['with no space left', 'very light', 'broken'], 'ans': 0, 'why': 'Full = no more space.'}, {'sent': 'It is a big meal, so I feel full.', 'w': 'feel full', 'opts': ['cannot eat more', 'want more food', 'am sick'], 'ans': 0, 'why': 'Feel full = not hungry now.'}],
  'chunkHunt': ['What can I get you?', 'Do you want a combo?', 'What comes with it?', 'No, thanks. That’s all.'],
  'think': 'What do you order at a burger place? Do you like to get a combo?'},
 'convo': {'npc': {'name': 'Malik'}, 'story': 'You are at a burger place in Milwaukee. Malik is the cashier. Order a combo and finish politely.', 'turns': [
  {'npc': 'Welcome! What can I get you?', 'pt': 'Bem-vindo! O que vai ser?', 'opts': [
   {'en': 'I am wanting a burger.', 'pt': 'Estou querendo um hambúrguer.', 'ok': False, 'fb': 'Use A cheeseburger, please.'},
   {'en': 'Yes, I am welcome.', 'pt': 'Sim, eu sou bem-vindo.', 'ok': False, 'fb': 'It does not answer.'},
   {'en': 'A cheeseburger, please.', 'pt': 'Um cheeseburger, por favor.', 'ok': True, 'fb': 'Short and polite.'}]},
  {'npc': 'Do you want a combo?', 'pt': 'Quer o combo?', 'opts': [
   {'en': 'What comes with it?', 'pt': 'O que vem nele?', 'ok': True, 'fb': 'A good question when you are not sure.'},
   {'en': 'What is the come?', 'pt': 'O que é o vir?', 'ok': False, 'fb': 'Wrong structure.'},
   {'en': 'I combo yes.', 'pt': 'Eu combo sim.', 'ok': False, 'fb': 'Combo is a noun, not a verb.'}]},
  {'npc': 'Fries and a drink.', 'pt': 'Batata frita e uma bebida.', 'opts': [
   {'en': 'I have fries.', 'pt': 'Eu tenho batata.', 'ok': False, 'fb': 'Say OK, a combo, please.'},
   {'en': 'No drink, I am a cola.', 'pt': 'Sem bebida, eu sou uma cola.', 'ok': False, 'fb': 'Wrong meaning.'},
   {'en': 'OK. A combo, and a cola.', 'pt': 'Ok. Um combo e uma cola.', 'ok': True, 'fb': 'Choose the combo and the drink.'}]},
  {'npc': 'Anything else?', 'pt': 'Mais alguma coisa?', 'opts': [
   {'en': 'No more nothing.', 'pt': 'Mais nada, nada.', 'ok': False, 'fb': 'Double negative. Say No, thanks.'},
   {'en': 'No, thanks. That’s all.', 'pt': 'Não, valeu. É só isso.', 'ok': True, 'fb': 'The usual way to end.'},
   {'en': 'I eat all.', 'pt': 'Eu como tudo.', 'ok': False, 'fb': 'It is not an answer.'}]},
  {'npc': 'Enjoy your burger!', 'pt': 'Bom apetite!', 'opts': [
   {'en': 'You are welcome.', 'pt': 'De nada.', 'ok': False, 'fb': 'Not a thank-you situation.'},
   {'en': 'Thanks! You too.', 'pt': 'Valeu! Você também.', 'ok': True, 'fb': 'Natural and friendly.'},
   {'en': 'Good appetite.', 'pt': 'Bom apetite.', 'ok': False, 'fb': 'Not natural English.'}]}]},
 'errors': [
  {'wrong': 'I want a combo with the cola.', 'fix': 'I’ll have a combo with a cola.', 'alt': 'I want combo with cola.', 'why': 'Use a before a drink, and I’ll have… is common when ordering.'},
  {'wrong': 'No more nothing.', 'fix': 'No, thanks. That’s all.', 'alt': 'No thanks. I am all.', 'why': 'Do not use a double negative. Say That’s all.'},
  {'wrong': 'What come with the combo?', 'fix': 'What comes with the combo?', 'alt': 'What is come with the combo?', 'why': 'With it/what, use comes (third person).'},
  {'wrong': 'I am with hungry.', 'fix': 'I’m hungry.', 'alt': 'I have hungry.', 'why': 'In English, hungry is a feeling with be: I am hungry.'}],
 'homework': 'Write your own burger-combo order and say it aloud like a real customer.',
 'homework_items': ['Write a 6-line order dialogue with a cashier.', 'Record yourself saying What comes with it?', 'Listen to the dialogue again and shadow Malik.', 'Review: I’m so hungry! / I feel full. / That’s all.']}
