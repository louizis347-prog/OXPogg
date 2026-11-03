"""Suplemento Quest v5 · aula 47: Buy a transit card + regular Here is your change (Alexander, Who Used to Be Rich Last Sunday)."""
SUPP = {
 'reg': 172,
 'badge': {'icon': '💳', 'name': 'Card Master', 'desc': 'Buy and use a transit card in English'},
 'sticker': {'cat': 'Everyday culture', 'title': 'Tap and Go Transit Cards', 'sub': 'Clipper, reload and change'},
 'culture': {
  'hook': 'Many American cities have a reloadable card for buses and trains. You add money once, then you just tap the card and go.',
  'polite': 'Staff often ask **“How much do you want to add?”** You can answer with just the amount.',
  'mythfact': [
   {'s': 'San Francisco Bay Area transit uses a card called Clipper.', 'ans': True, 'why': 'Clipper works on buses, trains and ferries around the Bay.'},
   {'s': 'Every US city uses the same transit card.', 'ans': False, 'why': 'Each region has its own card, like SmarTrip in Washington, DC.'},
   {'s': 'You can add cash to some cards at a machine.', 'ans': True, 'why': 'Station machines often take cash or cards.'},
   {'s': 'You must show the card to the driver and wait.', 'ans': False, 'why': 'You usually tap it on the reader and walk in.'}],
  'wild': [
   {'kind': 'Machine screen', 'lines': ['**Add value**', 'Choose an amount: $10 · $20 · $50', 'Pay with cash or card'], 'decode': {'q': 'What can you choose first?', 'opts': ['An amount', 'A color', 'A seat'], 'ans': 0, 'why': '“Choose an amount.”'}},
   {'kind': 'Receipt', 'lines': ['Card reloaded: $20.00', 'Cash paid: $20.00', 'Thank you!'], 'decode': {'q': 'How did the customer pay?', 'opts': ['Cash', 'Credit card', 'Check'], 'ans': 0, 'why': '“Cash paid: $20.00.”'}}],
  'compare': {'br': 'In Brazil, many cities have their own transit card (São Paulo has the Bilhete Único), and you can often recharge it at a booth or an app.', 'us': 'In the USA each region has its own card, and you can often add money at a machine or online.', 'tip': 'Check your balance before you travel so you do not have a problem at the reader.', 'ask': 'How much money do you usually add to your card? Say it in English.'},
  'quiz': [
   {'q': 'The clerk asks “Cash or card?” You want to pay cash. You say…', 'opts': ['Cash, please.', 'I have cash me.', 'Card is cash.'], 'ans': 0, 'why': 'Answer directly: Cash, please.'},
   {'q': 'How do you use a transit card?', 'opts': ['Tap it on the reader', 'Show it to a stranger', 'Cut it in half'], 'ans': 0, 'why': 'Tap on the reader.'},
   {'q': '“Here’s your change” means…', 'opts': ['The money you get back', 'Your new job', 'Your bus number'], 'ans': 0, 'why': 'Change = extra money returned.'}]},
 'reading': {
  'genre': 'Story', 'title': 'Nina’s first transit card',
  'text': [
   'Nina arrived in San Francisco on Monday. She wanted to ride the bus, but she did not have a transit card. She walked to a small shop near the station and said, “**Hi! I need a transit card.**”',
   '“**Sure. How much do you want to add?**” the clerk asked. Nina counted her money. “**Twenty dollars, please**,” she said. “**Cash or card?**” “**Cash. Here you go**,” she answered and gave him a twenty-dollar bill.',
   'The clerk put the card in a machine and added the money. Then he said, “**Here’s your card and your change**.” Nina looked at the change in her hand. There were a few coins because the card cost a little.',
   '“**How do I use it?**” she asked. “**Tap it on the reader**,” he said. “It makes a small sound when it works.” Nina put the card in her bag and said, “**Have a nice day!**”',
   'At the bus stop, she tapped the card on the reader. It made a short sound, and a green light came on. Nina smiled. She did not need coins, and she did not need to ask the driver for help.',
   'Later, she told her friend, “A transit card is easy. You tap and go!” Nina felt more at home in the city.'],
  'glossary': [{'w': 'transit card', 'pt': 'cartão de transporte'}, {'w': 'clerk', 'pt': 'atendente'}, {'w': 'add', 'pt': 'adicionar'}, {'w': 'cash', 'pt': 'dinheiro vivo'}, {'w': 'bill', 'pt': 'cédula'}, {'w': 'change', 'pt': 'troco'}, {'w': 'coins', 'pt': 'moedas'}, {'w': 'reader', 'pt': 'leitor'}, {'w': 'tap', 'pt': 'encostar'}],
  'fast': {'q': 'What is this text about?', 'opts': ['Buying and using a transit card', 'Cooking dinner', 'Planning a party'], 'ans': 0, 'why': 'Nina buys a card and taps it.'},
  'scan': [{'q': 'How much money does Nina add?', 'ans': 'twenty dollars', 'alt': ['$20', '20 dollars', '20']}, {'q': 'How does Nina pay?', 'ans': 'cash', 'alt': ['with cash']}, {'q': 'What color is the light after the tap?', 'ans': 'green', 'alt': ['a green light']}],
  'tf': [{'s': 'Nina arrives on Monday.', 'ans': True, 'why': 'The text says Monday.'}, {'s': 'Nina pays by credit card.', 'ans': False, 'why': 'She pays cash.'}, {'s': 'The clerk gives her change.', 'ans': True, 'why': '“Here’s your card and your change.”'}, {'s': 'She uses the card at a restaurant.', 'ans': False, 'why': 'She uses it on the bus.'}],
  'order': ['Nina says she needs a transit card.', 'She asks to add twenty dollars.', 'She pays cash.', 'The clerk gives her the card and the change.', 'She taps the card on the bus reader.'],
  'ctx': [{'sent': 'Nina counted her money.', 'w': 'counted', 'opts': ['said the numbers one by one', 'threw away', 'lost'], 'ans': 0, 'why': 'Counted = checked how many.'}, {'sent': 'The card made a small sound when it worked.', 'w': 'sound', 'opts': ['noise', 'color', 'price'], 'ans': 0, 'why': 'Sound = noise you hear.'}, {'sent': 'She felt more at home in the city.', 'w': 'at home', 'opts': ['comfortable', 'sick', 'late'], 'ans': 0, 'why': 'At home = comfortable.'}],
  'chunkHunt': ['I need a transit card.', 'How much do you want to add?', 'Cash or card?', 'Here’s your card and your change.', 'Tap it on the reader.'],
  'think': 'Do you use a transit card? What is easy and what is hard about it?'},
 'convo': {'npc': {'name': 'Nina'}, 'story': 'You work at a transit ticket booth in San Francisco. Nina wants a card. Help her.', 'turns': [
  {'npc': 'Hi! I need a transit card.', 'pt': 'Oi! Preciso de um cartão de transporte.', 'opts': [
   {'en': 'Sure. How much do you want to add?', 'pt': 'Claro. Quanto quer adicionar?', 'ok': True, 'fb': 'Polite and useful.'},
   {'en': 'You need yes.', 'pt': 'Você precisa sim.', 'ok': False, 'fb': 'Not natural.'},
   {'en': 'I am a card.', 'pt': 'Eu sou um cartão.', 'ok': False, 'fb': 'Wrong meaning.'}]},
  {'npc': 'Twenty dollars, please.', 'pt': 'Vinte dólares, por favor.', 'opts': [
   {'en': 'I have twenty years.', 'pt': 'Eu tenho vinte anos.', 'ok': False, 'fb': 'Wrong context.'},
   {'en': 'Cash or card?', 'pt': 'Dinheiro ou cartão?', 'ok': True, 'fb': 'The next logical question.'},
   {'en': 'Twenty is a number.', 'pt': 'Vinte é um número.', 'ok': False, 'fb': 'Does not help.'}]},
  {'npc': 'Cash. Here you go.', 'pt': 'Dinheiro. Aqui está.', 'opts': [
   {'en': 'Here is card, change you.', 'pt': 'Aqui é cartão, troco você.', 'ok': False, 'fb': 'Broken sentence.'},
   {'en': 'Here’s your card and your change.', 'pt': 'Aqui está seu cartão e seu troco.', 'ok': True, 'fb': 'Natural and complete.'},
   {'en': 'You give me the cash.', 'pt': 'Você me dá o dinheiro.', 'ok': False, 'fb': 'She already did.'}]},
  {'npc': 'How do I use it?', 'pt': 'Como eu uso?', 'opts': [
   {'en': 'Tap it on the reader.', 'pt': 'Encoste no leitor.', 'ok': True, 'fb': 'Simple instruction.'},
   {'en': 'You eat it.', 'pt': 'Você come.', 'ok': False, 'fb': 'Silly answer.'},
   {'en': 'Use with the hand.', 'pt': 'Use com a mão.', 'ok': False, 'fb': 'Not clear.'}]},
  {'npc': 'Have a nice day!', 'pt': 'Tenha um bom dia!', 'opts': [
   {'en': 'You are welcome.', 'pt': 'De nada.', 'ok': False, 'fb': 'She did not thank you.'},
   {'en': 'I have a nice day.', 'pt': 'Eu tenho um dia bom.', 'ok': False, 'fb': 'Not a reply.'},
   {'en': 'You too!', 'pt': 'Você também!', 'ok': True, 'fb': 'The natural answer.'}]}]},
 'errors': [
  {'wrong': 'I want one transit card of twenty.', 'fix': 'I need a transit card with twenty dollars.', 'alt': 'I need a card of twenty.', 'why': 'Say with twenty dollars.'},
  {'wrong': 'How much I add?', 'fix': 'How much do I add?', 'alt': 'How much I do add?', 'why': 'Questions use do + I.'},
  {'wrong': 'Cash or card, please? I pay cash.', 'fix': 'Cash, please.', 'alt': 'I pay on cash.', 'why': 'Answer short: Cash, please.'},
  {'wrong': 'Where I put the card?', 'fix': 'Where do I put the card?', 'alt': 'Where I do put the card?', 'why': 'Use do before I.'}],
 'homework': 'Role-play with a friend: one buys a card, one is the clerk. Use cash or card, change and tap.',
 'homework_items': ['Write a 6-line dialogue at a ticket booth.', 'Record the clerk and the customer.', 'Practice saying amounts: $10, $15, $20.', 'Review: Cash or card? / Here’s your change.']}
