"""Suplemento Quest v5 · aula 38: The check, please + regular Dollars and Cents (Silas Marner)."""
SUPP = {
 'reg': 100,
 'badge': {'icon': '💳', 'name': 'Check Pro', 'desc': 'Ask for the check, split it and pay by card in English'},
 'culture': {
  'hook': 'In the USA, the server does not bring the bill until you ask for it. Learn to say “The check, please” and to split it with friends.',
  'mythfact': [
   {'s': 'In the USA, the check is called “the check” in a restaurant.', 'ans': True, 'why': 'In British English, people say “the bill”.'},
   {'s': 'In many US restaurants, the server brings the check without being asked.', 'ans': False, 'why': 'Usually you ask for it, so you can stay as long as you like.'},
   {'s': 'You can ask for separate checks.', 'ans': True, 'why': 'Servers often ask “Together or separate?”.'},
   {'s': 'Albuquerque is in New Mexico.', 'ans': True, 'why': 'It is the biggest city in New Mexico and hosts a famous balloon festival every October.'},
   {'s': 'You pay the server with cash only.', 'ans': False, 'why': 'Cards are very common, and the server usually takes your card to the register.'}],
  'wild': [
   {'kind': 'Restaurant check', 'lines': ['Burger $12 · Salad $9', 'Soda $3 · Water free', 'Subtotal $24 · Tax $2 · Total $26'], 'decode': {'q': 'What is the total?', 'opts': ['$26', '$24', '$12'], 'ans': 0, 'why': 'The last line says Total $26.'}},
   {'kind': 'Text message', 'lines': ['Dinner was great!', 'I paid $60. Can you send $30?', 'Thanks!'], 'decode': {'q': 'How much should the friend send?', 'opts': ['$30', '$60', '$15'], 'ans': 0, 'why': '“Can you send $30?”'}}],
  'compare': {'br': 'In Brazil, it is common to ask “A conta, por favor” and split the bill, often adding a 10% service charge.', 'us': 'In the USA, you ask for “the check”, and the tip is not included, so you add it yourself.', 'tip': 'Learn two phrases: “Separate checks, please.” / “Let’s split it.”', 'ask': 'How do you pay with friends? Say it in English.'},
  'quiz': [
   {'q': 'You want the bill. You say…', 'opts': ['The check, please.', 'The bill me.', 'Give pay.'], 'ans': 0, 'why': 'In the USA, say the check.'},
   {'q': '“Together or separate?” You want one check. You say…', 'opts': ['Together, please.', 'Separate together.', 'One me.'], 'ans': 0, 'why': 'Together, please is clear.'},
   {'q': 'Which is a question about paying with a credit card?', 'opts': ['Can I pay by card?', 'Can I pay card?', 'I pay by card?'], 'ans': 0, 'why': 'Can I pay by card? is natural.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Who pays the check?',
  'text': [
   'It is Friday night in **Albuquerque**. Raúl and his friend Leila finish dinner at a small restaurant. They laugh because the dessert was huge. Now it is time to pay.',
   'Leila lifts her hand. “**Excuse me. The check, please.**” The server comes with a smile. “**Sure. Together or separate?**” Leila answers, “**Together, please.**” The server brings the paper. “**Here you go. It’s forty dollars.**”',
   '“**I got this**,” says Raúl. “No, **let me**,” says Leila. They are both kind, so they decide to **split it**. Leila asks, “**Can I pay by card?**” “**Yes, of course**,” the server says. “**Here’s my card**,” says Leila.',
   'Then they think about the novel Silas Marner. Silas loves his gold coins, but a little girl, Eppie, becomes his true treasure. “Gold isn’t everything,” says Raúl. Friends often say “Half and half” when the check comes. It is a simple way to be fair.',
   'At the door, the server says, “**Thank you, come again!**” Raúl smiles. “**Next one’s on me**,” he says. They walk home slowly under the warm night sky, happy and full.'],
  'glossary': [{'w': 'check', 'pt': 'conta'}, {'w': 'server', 'pt': 'garçom'}, {'w': 'together', 'pt': 'junto'}, {'w': 'separate', 'pt': 'separado'}, {'w': 'card', 'pt': 'cartão'}, {'w': 'split', 'pt': 'dividir'}, {'w': 'dessert', 'pt': 'sobremesa'}, {'w': 'novel', 'pt': 'romance (livro)'}, {'w': 'fair', 'pt': 'justo'}],
  'fast': {'q': 'What is this story about?', 'opts': ['Two friends pay for dinner', 'A school lesson', 'A day at the beach'], 'ans': 0, 'why': 'Raúl and Leila pay the check after dinner.'},
  'scan': [{'q': 'What city are they in?', 'ans': 'Albuquerque', 'alt': ['albuquerque']}, {'q': 'How much is the check?', 'ans': '40 dollars', 'alt': ['forty dollars', '$40', '40']}, {'q': 'How does Leila pay?', 'ans': 'by card', 'alt': ['card', 'with a card']}],
  'tf': [{'s': 'They ask for separate checks.', 'ans': False, 'why': 'Leila says “Together, please.”'}, {'s': 'Leila pays by card.', 'ans': True, 'why': '“Here’s my card.”'}, {'s': 'The dessert was small.', 'ans': False, 'why': 'The dessert was huge.'}, {'s': 'Raúl says the next dinner is on him.', 'ans': True, 'why': '“Next one’s on me.”'}],
  'order': ['Leila asks for the check.', 'The server asks together or separate.', 'The server brings the check.', 'Leila pays by card.', 'The server says come again.'],
  'ctx': [{'sent': 'They want to split the check.', 'w': 'split', 'opts': ['divide', 'break', 'lose'], 'ans': 0, 'why': 'Split = divide between people.'}, {'sent': 'It is a fair way to pay.', 'w': 'fair', 'opts': ['equal and just', 'very expensive', 'very fast'], 'ans': 0, 'why': 'Fair = equal and right.'}, {'sent': 'Next one’s on me.', 'w': 'on me', 'opts': ['I will pay', 'I am sick', 'I am here'], 'ans': 0, 'why': 'On me = I pay.'}],
  'chunkHunt': ['The check, please.', 'Together or separate?', 'Can I pay by card?', 'Let’s split it.'],
  'think': 'Do you split the check with friends or does one person pay?'},
 'convo': {'npc': {'name': 'Leila'}, 'story': 'You work as a server in Albuquerque. Leila is a customer. Bring her the check and take her card.', 'turns': [
  {'npc': 'Excuse me. The check, please.', 'pt': 'Com licença. A conta, por favor.', 'opts': [
   {'en': 'Sure. Together or separate?', 'pt': 'Claro. Junto ou separado?', 'ok': True, 'fb': 'A typical server question.'},
   {'en': 'The check is not here.', 'pt': 'A conta não está aqui.', 'ok': False, 'fb': 'It does not help.'},
   {'en': 'Yes, I pay.', 'pt': 'Sim, eu pago.', 'ok': False, 'fb': 'The server does not pay.'}]},
  {'npc': 'Together, please.', 'pt': 'Junto, por favor.', 'opts': [
   {'en': 'Here it is you.', 'pt': 'Aqui está você.', 'ok': False, 'fb': 'Wrong order.'},
   {'en': 'Here you go. It’s forty dollars.', 'pt': 'Aqui está. São quarenta dólares.', 'ok': True, 'fb': 'Give the check and say the total.'},
   {'en': 'Forty dollars, no.', 'pt': 'Quarenta dólares, não.', 'ok': False, 'fb': 'Not polite.'}]},
  {'npc': 'Can I pay by card?', 'pt': 'Posso pagar com cartão?', 'opts': [
   {'en': 'No card, no.', 'pt': 'Sem cartão, não.', 'ok': False, 'fb': 'Too short and unclear.'},
   {'en': 'You can pay with card yes.', 'pt': 'Você pode pagar com cartão sim.', 'ok': False, 'fb': 'Use Yes, of course.'},
   {'en': 'Yes, of course.', 'pt': 'Sim, claro.', 'ok': True, 'fb': 'Short and polite.'}]},
  {'npc': 'Here’s my card.', 'pt': 'Aqui está meu cartão.', 'opts': [
   {'en': 'Thank you. Have a nice day!', 'pt': 'Obrigado. Tenha um bom dia!', 'ok': True, 'fb': 'A standard closing.'},
   {'en': 'The card is nice.', 'pt': 'O cartão é bonito.', 'ok': False, 'fb': 'Not the point.'},
   {'en': 'I am the card.', 'pt': 'Eu sou o cartão.', 'ok': False, 'fb': 'Wrong meaning.'}]},
  {'npc': 'Thank you, come again!', 'pt': 'Obrigado, volte sempre!', 'opts': [
   {'en': 'Welcome you!', 'pt': 'Bem-vindo você!', 'ok': False, 'fb': 'Say You’re welcome.'},
   {'en': 'You’re welcome. Goodbye!', 'pt': 'De nada. Tchau!', 'ok': True, 'fb': 'Natural and friendly.'},
   {'en': 'I come yesterday.', 'pt': 'Eu venho ontem.', 'ok': False, 'fb': 'Wrong tense.'}]}]},
 'errors': [
  {'wrong': 'The bill, please.', 'fix': 'The check, please.', 'alt': 'The count, please.', 'why': 'In the USA, people usually say the check. Bill is more British.'},
  {'wrong': 'I pay with card.', 'fix': 'I’ll pay by card.', 'alt': 'I pay by the card.', 'why': 'Use by card with no article.'},
  {'wrong': 'We divide the account.', 'fix': 'We’ll split the check.', 'alt': 'We split the account.', 'why': 'Account is not the word for a restaurant bill.'},
  {'wrong': 'Together or separated?', 'fix': 'Together or separate?', 'alt': 'Together or separately?', 'why': 'The adjective here is separate.'}],
 'homework': 'Role-play asking for the check and paying with a friend, and record it.',
 'homework_items': ['Write a short dialogue: ask for the check and split it.', 'Practice: Together or separate? / Can I pay by card?', 'Listen to the dialogue again and shadow Leila.', 'Review: check / card / cash / split.']}
