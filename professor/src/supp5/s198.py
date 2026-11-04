"""Suplemento Quest v5 · aula 198: Can I get a ride? + regular See you around (See You Later, Alligator)."""
SUPP = {
 'reg': 232,
 'badge': {'icon': '🚗', 'name': 'Ride Asker', 'desc': 'Ask for a ride, set a place and time, and offer to share the gas'},
 'culture': {
  'hook': 'In much of the USA, people drive almost everywhere, so asking a neighbor or coworker for a ride is normal. A short, polite question and an offer to help with gas make it easy.',
  'mythfact': [
   {'s': 'In the USA, it is normal to ask a coworker for a ride when your car is in the shop.', 'ans': True, 'why': 'People often help each other, especially neighbors and coworkers.'},
   {'s': 'You must always pay a friend for a ride.', 'ans': False, 'why': 'It is a favor, but offering to help with gas is polite.'},
   {'s': '“Can I chip in for gas?” means “Can I help pay?”', 'ans': True, 'why': 'Chip in means to give a part of the money.'},
   {'s': 'A mechanic is a person who fixes cars.', 'ans': True, 'why': 'The car stays at the shop while the mechanic works.'},
   {'s': '“See You Later, Alligator” is a song from the 1950s.', 'ans': True, 'why': 'It was a famous rock and roll song, and the phrase is also a playful goodbye.'}],
  'wild': [
   {'kind': 'Text message', 'lines': ['Hi Leo! My car is in the shop.', '**Can I get a ride** tomorrow?', 'I can leave at 8.'], 'decode': {'q': 'What does the person want?', 'opts': ['A ride tomorrow', 'A new car', 'A job'], 'ans': 0, 'why': 'He asks, “Can I get a ride tomorrow?”'}},
   {'kind': 'Sign at a repair shop', 'lines': ['**Car ready by 5 p.m.**', 'Please bring your keys and card.', 'Closed Sunday'], 'decode': {'q': 'When is the car ready?', 'opts': ['By 5 p.m.', 'On Sunday', 'At noon'], 'ans': 0, 'why': 'The sign says “Car ready by 5 p.m.”'}}],
  'compare': {'br': 'In Brazil, many people say “Me dá uma carona?” and often split the cost of gas or just say thanks.', 'us': 'In the USA, people often say “Can I get a ride?” and offer a few dollars for gas, even if the driver says no.', 'tip': 'Say: “Can I get a ride? I can chip in for gas.”', 'ask': 'How do you ask for a ride in English? Say it.'},
  'quiz': [
   {'q': 'You ask a coworker for a ride. You say…', 'opts': ['Can I get a ride?', 'Can I take a ride?', 'Do you give me a ride?'], 'ans': 0, 'why': 'The usual phrase is Can I get a ride?'},
   {'q': 'You want to know the place to meet. You ask…', 'opts': ['Where should I meet you?', 'Where I should meet you?', 'Where do I meeting you?'], 'ans': 0, 'why': 'Where + should + I + verb.'},
   {'q': 'You ask how long the trip is. You say…', 'opts': ['How long is the drive?', 'How much long is the drive?', 'How long the drive is?'], 'ans': 0, 'why': 'How long + is + the drive?'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'A ride to work',
  'text': [
   'Sam’s car is in the shop. The mechanic says it is ready on Friday. Today is Wednesday, and Sam needs to go to work. He sees his neighbor Leo in the parking lot, with a coffee in his hand.',
   '“**Hey, are you going to work?**” Sam asks. “**Yes. Why?**” “**My car is in the shop. Can I get a ride?**” “**Sure. I’m leaving in ten minutes.**” Sam smiles. He is happy.',
   '“**Thank you so much. Where should I meet you?**” “**In front of the building.**” “**Great. How long is the drive?**” “**About twenty-five minutes.**” Ten minutes later, Sam is in front of the building, and Leo stops his blue car.',
   'In the car, Leo plays a rock song from the 1950s, “See You Later, Alligator.” Sam knows the title, and they both sing the chorus. At work, Leo parks the car. “**Can I chip in for gas?**” Sam asks. “Sure, thanks!” Leo says. Sam gives him five dollars. “Thanks for the favor. **See you around!**” “Later, alligator!” Leo answers with a big smile.'],
  'glossary': [{'w': 'shop', 'pt': 'oficina'}, {'w': 'mechanic', 'pt': 'mecânico'}, {'w': 'neighbor', 'pt': 'vizinho'}, {'w': 'parking lot', 'pt': 'estacionamento'}, {'w': 'ride', 'pt': 'carona'}, {'w': 'drive', 'pt': 'trajeto de carro'}, {'w': 'chip in', 'pt': 'contribuir com dinheiro'}, {'w': 'gas', 'pt': 'gasolina'}, {'w': 'favor', 'pt': 'favor'}, {'w': 'chorus', 'pt': 'refrão'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A man asks a neighbor for a ride to work', 'A man buys a new car', 'A mechanic fixes a car'], 'ans': 0, 'why': 'Sam’s car is in the shop, so Leo gives him a ride.'},
  'scan': [{'q': 'When is Sam’s car ready?', 'ans': 'Friday', 'alt': ['on Friday']}, {'q': 'How long is the drive?', 'ans': 'twenty-five minutes', 'alt': ['25 minutes', 'about twenty-five minutes']}, {'q': 'How much does Sam give for gas?', 'ans': 'five dollars', 'alt': ['$5', '5 dollars']}],
  'tf': [{'s': 'Sam’s car is in the shop.', 'ans': True, 'why': 'The mechanic fixes it.'}, {'s': 'Leo leaves in an hour.', 'ans': False, 'why': 'He leaves in ten minutes.'}, {'s': 'They meet in front of the building.', 'ans': True, 'why': 'Leo says, “In front of the building.”'}, {'s': 'Leo says no to the money for gas.', 'ans': False, 'why': 'He says, “Sure, thanks!”'}],
  'order': ['Sam asks for a ride.', 'Leo says he leaves in ten minutes.', 'They meet in front of the building.', 'They sing in the car.', 'Sam gives money for gas.'],
  'ctx': [{'sent': 'The mechanic says it is ready on Friday.', 'w': 'mechanic', 'opts': ['a person who fixes cars', 'a kind of coffee', 'a bus driver'], 'ans': 0, 'why': 'A mechanic fixes cars.'}, {'sent': 'Sam asks, “Can I chip in for gas?”', 'w': 'chip in', 'opts': ['give some money', 'drive fast', 'sing a song'], 'ans': 0, 'why': 'Chip in means give a part of the money.'}, {'sent': 'Thanks for the favor.', 'w': 'favor', 'opts': ['a kind help', 'a new job', 'a big car'], 'ans': 0, 'why': 'A favor is a kind help.'}],
  'chunkHunt': ['Can I get a ride?', 'Where should I meet you?', 'How long is the drive?', 'Can I chip in for gas?'],
  'think': 'Do you ask people for a ride? What do you say, and how do you thank them?'},
 'convo': {'npc': {'name': 'Miles'}, 'story': 'You are Miles’s neighbor. Your car is in the shop. You meet Miles in the plaza, and he drives to work.', 'turns': [
  {'npc': 'Hey, are you going to work?', 'pt': 'Ei, você vai para o trabalho?', 'opts': [
   {'en': 'Yes. My car is in the shop. Can I get a ride?', 'pt': 'Sim. Meu carro está na oficina. Posso pegar carona?', 'ok': True, 'fb': 'Gives the reason and asks politely.'},
   {'en': 'Yes. Give me a ride.', 'pt': 'Sim. Me dê uma carona.', 'ok': False, 'fb': 'Too direct. Use Can I get a ride?'},
   {'en': 'I am going to shop work.', 'pt': 'Eu vou para o trabalho de oficina.', 'ok': False, 'fb': 'Your car is in the shop. Say it clearly.'}]},
  {'npc': 'Sure. I’m leaving in ten minutes.', 'pt': 'Claro. Saio em dez minutos.', 'opts': [
   {'en': 'Thank you so much. Where should I meet you?', 'pt': 'Muito obrigado. Onde devo te encontrar?', 'ok': True, 'fb': 'Thanks and asks the place.'},
   {'en': 'Where I should meet you?', 'pt': 'Onde eu devo te encontrar?', 'ok': False, 'fb': 'Word order: Where should I meet you?'},
   {'en': 'Yes, I am leaving ten minutes.', 'pt': 'Sim, eu saio dez minutos.', 'ok': False, 'fb': 'Miles is the one leaving. You should thank him.'}]},
  {'npc': 'In front of the building.', 'pt': 'Na frente do prédio.', 'opts': [
   {'en': 'In the front of the building, no.', 'pt': 'Na frente do prédio, não.', 'ok': False, 'fb': 'It does not fit.'},
   {'en': 'Okay. See you there.', 'pt': 'Certo. Te vejo lá.', 'ok': False, 'fb': 'Good, but ask about the trip first.'},
   {'en': 'Great. How long is the drive?', 'pt': 'Ótimo. Quanto dura o trajeto?', 'ok': True, 'fb': 'Natural question about time.'}]},
  {'npc': 'About twenty-five minutes.', 'pt': 'Uns vinte e cinco minutos.', 'opts': [
   {'en': 'Can I chip in for gas?', 'pt': 'Posso dividir a gasolina?', 'ok': True, 'fb': 'Polite offer to pay a part.'},
   {'en': 'Can I pay you the gas?', 'pt': 'Posso pagar a gasolina para você?', 'ok': False, 'fb': 'The natural phrase is chip in for gas.'},
   {'en': 'Twenty-five minutes is a gas.', 'pt': 'Vinte e cinco minutos é gasolina.', 'ok': False, 'fb': 'Does not fit.'}]}]},
 'errors': [
  {'wrong': 'Can you give me a carona?', 'fix': 'Can I get a ride?', 'alt': 'Can I take a ride?', 'why': 'In English, ride is the word, and we say get a ride.'},
  {'wrong': 'Where I should meet you?', 'fix': 'Where should I meet you?', 'alt': 'Where do I should meet you?', 'why': 'In questions, put should before I.'},
  {'wrong': 'How much time is the drive?', 'fix': 'How long is the drive?', 'alt': 'How long the drive is?', 'why': 'To ask time, use How long + is.'},
  {'wrong': 'My car is in the oficina.', 'fix': 'My car is in the shop.', 'alt': 'My car is on the shop.', 'why': 'Use in the shop for a repair place.'}],
 'homework': 'Write a short dialogue: you ask a neighbor for a ride, set a place and offer to chip in for gas.',
 'homework_items': ['Write two reasons to ask for a ride.', 'Say aloud: Can I get a ride?', 'Listen to the dialogue and shadow Miles.', 'Review: mechanic / favor / tank / passenger.']}
