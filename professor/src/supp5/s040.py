"""Suplemento Quest v5 · aula 40: Takeout by phone + regular With or without onions? (Mystic Pizza)."""
SUPP = {
 'reg': 141,
 'badge': {'icon': '🍕', 'name': 'Phone Order Pro', 'desc': 'Order takeout by phone: size, toppings, name and time'},
 'culture': {
  'hook': 'Calling a pizza place can feel scary at first. The call is short and always follows the same steps: size, kind, extras, your name and the wait time.',
  'mythfact': [
   {'s': 'In the USA, “takeout” means food you take away from the restaurant.', 'ans': True, 'why': 'In British English, people say “takeaway”.'},
   {'s': 'On the phone, the restaurant asks for your name for the order.', 'ans': True, 'why': 'They write it on the box or bag so you can find your order.'},
   {'s': 'You can ask for half cheese, half pepperoni on one pizza.', 'ans': True, 'why': 'Half and half pizzas are common in many pizza places.'},
   {'s': 'Newark is the capital of New Jersey.', 'ans': False, 'why': 'Newark is the biggest city, but the capital is Trenton.'},
   {'s': '“Mystic Pizza” is a 1988 film with Julia Roberts.', 'ans': True, 'why': 'It is a film about three friends who work at a pizza restaurant.'}],
  'wild': [
   {'kind': 'Pizza menu', 'lines': ['**Cheese pizza** large  $14', '**Toppings**  +$2 each', '**Soda** (bottle)  $3'], 'decode': {'q': 'How much is a large pizza with one topping?', 'opts': ['$16', '$14', '$17'], 'ans': 0, 'why': '$14 + $2 = $16.'}},
   {'kind': 'Voice mail', 'lines': ['Thank you for calling Joe’s Pizza.', 'We are closed now.', 'Please call back after 11 a.m.'], 'decode': {'q': 'When should you call back?', 'opts': ['After 11 a.m.', 'Before 11 a.m.', 'At night'], 'ans': 0, 'why': '“Please call back after 11 a.m.”'}}],
  'compare': {'br': 'In Brazil, many people order pizza by app or WhatsApp, and the delivery is very common.', 'us': 'In the USA, a phone call is still normal for a small pizza place, and “for pickup” means you go and get it.', 'tip': 'Start with: “Hi, I’d like a large pizza for takeout.”', 'ask': 'How do you order food at home? Say it in English.'},
  'quiz': [
   {'q': 'You start a phone order. You say…', 'opts': ['Hi. I’d like a large pizza for takeout.', 'Hi, I am a pizza.', 'Large pizza, what?'], 'ans': 0, 'why': 'I’d like… for takeout is natural.'},
   {'q': 'What does “half cheese, half pepperoni” mean?', 'opts': ['one pizza, two toppings', 'two pizzas', 'a small pizza'], 'ans': 0, 'why': 'Each half has a different topping.'},
   {'q': '“It’ll be twenty minutes.” It means…', 'opts': ['it will be ready in 20 minutes', 'it is 20 minutes late', 'it is 20 dollars'], 'ans': 0, 'why': 'It’ll be = it will be.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Pizza for three',
  'text': [
   'Friday night in **Newark**. Abe and his two friends are hungry. They want pizza, and nobody wants to cook. Abe picks up the phone.',
   '“Joe’s Pizza. **How can I help you?**” a woman says. Abe answers, “**Hi. I’d like a large pizza for takeout.**” “**What kind of pizza?**” “**Half cheese, half pepperoni.**” One friend likes mushrooms, but Abe says, “Not today!”',
   '“**Anything else?**” she asks. “**A bottle of soda, please.**” She answers, “**It’ll be twenty minutes.**” “**Great. My name is Sam**,” Abe says. “Your order will be ready soon,” she says. Abe says thank you and ends the call.',
   'Twenty minutes later, they walk to the shop. The smell is wonderful. The box is warm in Abe’s hands. “**Pizza’s here!**” he says. They laugh and sit in the park to eat.',
   'Abe remembers the film Mystic Pizza. In it, three young women work at a small pizza place. The place is the heart of their town. “**This hits the spot**,” says one friend. Abe smiles. A simple phone call, and a perfect Friday.'],
  'glossary': [{'w': 'takeout', 'pt': 'para viagem'}, {'w': 'large', 'pt': 'grande'}, {'w': 'kind', 'pt': 'tipo'}, {'w': 'pepperoni', 'pt': 'calabresa picante (pepperoni)'}, {'w': 'bottle', 'pt': 'garrafa'}, {'w': 'soda', 'pt': 'refrigerante'}, {'w': 'order', 'pt': 'pedido'}, {'w': 'mushrooms', 'pt': 'cogumelos'}, {'w': 'box', 'pt': 'caixa'}],
  'fast': {'q': 'What is this story about?', 'opts': ['Ordering pizza by phone', 'A soccer game', 'A trip to the beach'], 'ans': 0, 'why': 'Abe orders a pizza on the phone.'},
  'scan': [{'q': 'What kind of pizza does Abe order?', 'ans': 'half cheese, half pepperoni', 'alt': ['cheese and pepperoni', 'half cheese half pepperoni']}, {'q': 'How long is the wait?', 'ans': 'twenty minutes', 'alt': ['20 minutes', '20']}, {'q': 'What name does Abe give?', 'ans': 'Sam', 'alt': ['sam']}],
  'tf': [{'s': 'Abe orders a small pizza.', 'ans': False, 'why': 'He orders a large pizza.'}, {'s': 'Abe orders a bottle of soda.', 'ans': True, 'why': '“A bottle of soda, please.”'}, {'s': 'The pizza will be ready in two hours.', 'ans': False, 'why': 'It will be ready in twenty minutes.'}, {'s': 'The friends eat in the park.', 'ans': True, 'why': 'They sit in the park to eat.'}],
  'order': ['Abe calls Joe’s Pizza.', 'He orders half cheese, half pepperoni.', 'He asks for a bottle of soda.', 'He gives his name.', 'They eat in the park.'],
  'ctx': [{'sent': 'I’d like a pizza for takeout.', 'w': 'takeout', 'opts': ['food to take away', 'food at the table', 'a kind of pizza'], 'ans': 0, 'why': 'Takeout = food you take with you.'}, {'sent': 'The order will be ready soon.', 'w': 'soon', 'opts': ['in a short time', 'never', 'yesterday'], 'ans': 0, 'why': 'Soon = in a short time.'}, {'sent': 'This hits the spot!', 'w': 'hits the spot', 'opts': ['is exactly right', 'is too hot', 'is too big'], 'ans': 0, 'why': 'Hits the spot = perfectly satisfying.'}],
  'chunkHunt': ['I’d like a large pizza for takeout.', 'Half cheese, half pepperoni.', 'It’ll be twenty minutes.', 'My name is…'],
  'think': 'Do you order food by phone or by app? What is the hardest part?'},
 'convo': {'npc': {'name': 'Chloe'}, 'story': 'You call Joe’s Pizza in Newark. Chloe answers the phone. Order your takeout pizza.', 'turns': [
  {'npc': 'Joe’s Pizza. How can I help you?', 'pt': 'Joe’s Pizza. Como posso ajudar?', 'opts': [
   {'en': 'I am wanting a pizza.', 'pt': 'Estou querendo uma pizza.', 'ok': False, 'fb': 'Say I’d like a large pizza for takeout.'},
   {'en': 'I’m a pizza, thanks.', 'pt': 'Sou uma pizza, valeu.', 'ok': False, 'fb': 'Wrong meaning.'},
   {'en': 'Hi. I’d like a large pizza for takeout.', 'pt': 'Oi. Eu gostaria de uma pizza grande para viagem.', 'ok': True, 'fb': 'Polite and complete.'}]},
  {'npc': 'What kind of pizza?', 'pt': 'Que tipo de pizza?', 'opts': [
   {'en': 'Half cheese, half pepperoni.', 'pt': 'Metade queijo, metade pepperoni.', 'ok': True, 'fb': 'Say the two halves.'},
   {'en': 'The kind is large.', 'pt': 'O tipo é grande.', 'ok': False, 'fb': 'Kind is not size.'},
   {'en': 'Yes, a pizza.', 'pt': 'Sim, uma pizza.', 'ok': False, 'fb': 'Say the toppings.'}]},
  {'npc': 'Anything else?', 'pt': 'Mais alguma coisa?', 'opts': [
   {'en': 'A soda bottle, please.', 'pt': 'Uma garrafa de soda, por favor.', 'ok': False, 'fb': 'Natural order: a bottle of soda.'},
   {'en': 'A bottle of soda, please.', 'pt': 'Uma garrafa de refrigerante, por favor.', 'ok': True, 'fb': 'Use a bottle of.'},
   {'en': 'No more pizza hello.', 'pt': 'Sem mais pizza olá.', 'ok': False, 'fb': 'It does not make sense.'}]},
  {'npc': 'It’ll be twenty minutes.', 'pt': 'Fica pronto em vinte minutos.', 'opts': [
   {'en': 'Great. My name is Sam.', 'pt': 'Ótimo. Meu nome é Sam.', 'ok': True, 'fb': 'Give your name for the order.'},
   {'en': 'Twenty minutes is dollars.', 'pt': 'Vinte minutos é dólares.', 'ok': False, 'fb': 'Minutes are time, not money.'},
   {'en': 'I am wait.', 'pt': 'Eu sou espere.', 'ok': False, 'fb': 'Say I’ll be there.'}]},
  {'npc': 'Your order will be ready soon!', 'pt': 'Seu pedido ficará pronto logo!', 'opts': [
   {'en': 'Thank you. See you soon!', 'pt': 'Obrigado. Até logo!', 'ok': False, 'fb': 'Good, but the standard ending is Thanks, bye!'},
   {'en': 'Thanks! Bye!', 'pt': 'Valeu! Tchau!', 'ok': True, 'fb': 'Short and natural.'},
   {'en': 'It is soon yes.', 'pt': 'É logo sim.', 'ok': False, 'fb': 'Does not end the call.'}]}]},
 'errors': [
  {'wrong': 'I want a pizza for take.', 'fix': 'I’d like a pizza for takeout.', 'alt': 'I want a pizza to taking.', 'why': 'The noun is takeout, and I’d like is more polite.'},
  {'wrong': 'A bottle soda, please.', 'fix': 'A bottle of soda, please.', 'alt': 'A soda of bottle, please.', 'why': 'Use a bottle of + drink.'},
  {'wrong': 'Pizza of cheese.', 'fix': 'Cheese pizza.', 'alt': 'Pizza cheese.', 'why': 'In English, the first noun describes the second.'},
  {'wrong': 'My name are Sam.', 'fix': 'My name is Sam.', 'alt': 'I name Sam.', 'why': 'Use is with name.'}],
 'homework': 'Record a one-minute phone order for a pizza and send it to your teacher.',
 'homework_items': ['Write the 5 steps of a phone order.', 'Record yourself ordering pizza for takeout.', 'Listen to the dialogue again and shadow Chloe.', 'Review: I’d like… / Anything else? / It’ll be…']}
