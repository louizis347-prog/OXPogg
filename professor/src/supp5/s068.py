"""Suplemento Quest v5 · aula 68: At the laundry room + regular Sunday at home (The Flintstones)."""
SUPP = {
 'reg': 197,
 'badge': {'icon': '🧺', 'name': 'Laundry Pro', 'desc': 'Ask how a machine works, pay with quarters and ask how long it takes'},
 'culture': {
  'hook': 'Many people in the USA wash their clothes in a shared laundry room. You put in clothes and soap, pay with coins or a card, and wait. Short questions are enough.',
  'mythfact': [
   {'s': 'A quarter is a US coin worth 25 cents.', 'ans': True, 'why': 'Four quarters make one dollar.'},
   {'s': 'Four quarters equal two dollars.', 'ans': False, 'why': 'Four quarters equal one dollar. For two dollars you need eight.'},
   {'s': 'Many apartment buildings in the USA have a shared laundry room.', 'ans': True, 'why': 'It is common in apartment buildings, though not in every one.'},
   {'s': 'Dallas is a city in Texas.', 'ans': True, 'why': 'Dallas is one of the biggest cities in Texas.'},
   {'s': 'In the USA, people never use a dryer; they always hang clothes outside.', 'ans': False, 'why': 'Dryers are very common in American homes and laundry rooms.'}],
  'wild': [
   {'kind': 'Laundry room sign', 'lines': ['**LAUNDRY ROOM**', 'Open 7 a.m. – 10 p.m.', 'Quarters only. No change machine.'], 'decode': {'q': 'What can you use to pay?', 'opts': ['Quarters', 'Dollar bills', 'A phone'], 'ans': 0, 'why': '“Quarters only.”'}},
   {'kind': 'Machine label', 'lines': ['**WASH** $2.00', '**DRY** $1.50', 'Time: 30 minutes'], 'decode': {'q': 'How much for wash and dry together?', 'opts': ['$3.50', '$2.00', '$1.50'], 'ans': 0, 'why': '$2.00 + $1.50 = $3.50.'}}],
  'compare': {'br': 'In Brazil, many people have a washing machine at home or use a laundromat, and some wash by hand.', 'us': 'In the USA, shared laundry rooms are common in apartment buildings, and machines often use quarters or a laundry card.', 'tip': 'Check the sign first, then ask: “How does this machine work?”', 'ask': 'Where do you wash your clothes? Say it in English.'},
  'quiz': [
   {'q': 'You do not know the machine. You say…', 'opts': ['Excuse me, how does this machine work?', 'Excuse me, I am a machine.', 'Machine, where is clothes?'], 'ans': 0, 'why': 'Excuse me + a simple question is polite.'},
   {'q': '“Press start.” What do you do?', 'opts': ['Push the start button', 'Open the door', 'Add more soap'], 'ans': 0, 'why': 'Press = push a button.'},
   {'q': '“It takes forty minutes.” It means…', 'opts': ['It is ready in forty minutes', 'It costs forty dollars', 'It is forty clothes'], 'ans': 0, 'why': 'Takes forty minutes = needs that time.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Laundry day',
  'text': [
   'Sunday morning in **Dallas**. Claire has a big basket of dirty clothes. Her apartment has no washer, so she goes down to the laundry room. It is her first time there.',
   'The room is quiet. A man named Dan is there. “**Excuse me, how does this machine work?**” Claire asks. “**Put your clothes in and add soap**,” he says. “**How much is it?**” “**Two dollars. Do you have coins?**”',
   '“**Yes, I have four quarters**,” she says. “And four more in my pocket.” Dan smiles. “**Great. Press start.**” Claire puts in the coins and pushes the button. The washer begins to turn. “**How long does it take?**” “**Forty minutes**,” Dan says.',
   '“Ugh, **laundry day**,” says Claire. “Same. **It never ends**,” Dan says. They laugh. Claire sits and reads a book. Dan puts his socks and towels in the dryer. Soon the washer stops.',
   'Claire moves her wet clothes to the dryer. She thinks of the cartoon The Flintstones. Every Sunday the family stays home, and Fred\'s house has funny stone machines. “My washer is not made of stone,” she thinks. “**Thanks for the help. Bye!**” she says to Dan.'],
  'glossary': [{'w': 'basket', 'pt': 'cesto'}, {'w': 'dirty', 'pt': 'sujo'}, {'w': 'quarters', 'pt': 'moedas de 25 centavos'}, {'w': 'coins', 'pt': 'moedas'}, {'w': 'button', 'pt': 'botão'}, {'w': 'towels', 'pt': 'toalhas'}, {'w': 'socks', 'pt': 'meias'}, {'w': 'wet', 'pt': 'molhado'}, {'w': 'quiet', 'pt': 'silencioso'}],
  'fast': {'q': 'What is this story about?', 'opts': ['Washing clothes in a laundry room', 'Buying a new washer', 'Cooking dinner'], 'ans': 0, 'why': 'Claire uses the laundry room for the first time.'},
  'scan': [{'q': 'How much is the washer?', 'ans': 'two dollars', 'alt': ['$2', '2 dollars', '$2.00']}, {'q': 'How long does it take?', 'ans': 'forty minutes', 'alt': ['40 minutes', '40']}, {'q': 'What is the man\'s name?', 'ans': 'Dan', 'alt': ['dan']}],
  'tf': [{'s': 'Claire has a washer in her apartment.', 'ans': False, 'why': 'Her apartment has no washer.'}, {'s': 'Dan helps Claire with the machine.', 'ans': True, 'why': 'He tells her what to do.'}, {'s': 'The washer takes ten minutes.', 'ans': False, 'why': 'It takes forty minutes.'}, {'s': 'Claire moves her wet clothes to the dryer.', 'ans': True, 'why': 'After the washer stops, she moves them.'}],
  'order': ['Claire goes to the laundry room.', 'She asks how the machine works.', 'She puts in the coins and presses the button.', 'She waits and reads a book.', 'She moves her clothes to the dryer.'],
  'ctx': [{'sent': 'Press the button to start.', 'w': 'Press', 'opts': ['push', 'open', 'wash'], 'ans': 0, 'why': 'Press = push.'}, {'sent': 'My clothes are wet.', 'w': 'wet', 'opts': ['not dry', 'very clean', 'very old'], 'ans': 0, 'why': 'Wet is the opposite of dry.'}, {'sent': 'Ugh, laundry day. It never ends.', 'w': 'never ends', 'opts': ['always continues', 'is very short', 'is finished'], 'ans': 0, 'why': 'It never ends = there is always more.'}],
  'chunkHunt': ['How does this machine work?', 'Put your clothes in and add soap.', 'Do you have coins?', 'How long does it take?'],
  'think': 'Do you wash clothes at home or somewhere else? What day is laundry day for you?'},
 'convo': {'npc': {'name': 'Dan'}, 'story': 'You are in the laundry room of your building in Dallas. Dan is there. Ask him how the machine works.', 'turns': [
  {'npc': 'Hi! Is this your first time here?', 'pt': 'Oi! É a sua primeira vez aqui?', 'opts': [
   {'en': 'Yes. How does this machine work?', 'pt': 'Sim. Como funciona esta máquina?', 'ok': True, 'fb': 'Answers and asks how it works.'},
   {'en': 'Yes. This machine works me.', 'pt': 'Sim. Esta máquina me funciona.', 'ok': False, 'fb': 'Say how does it work.'},
   {'en': 'I am wash clothes now.', 'pt': 'Eu sou lavar roupas agora.', 'ok': False, 'fb': 'It does not answer the question.'}]},
  {'npc': 'Put your clothes in and add soap.', 'pt': 'Coloque as roupas e adicione sabão.', 'opts': [
   {'en': 'I put my clothes yesterday.', 'pt': 'Eu coloquei minhas roupas ontem.', 'ok': False, 'fb': 'It talks about the past.'},
   {'en': 'The soap is cheap.', 'pt': 'O sabão é barato.', 'ok': False, 'fb': 'It does not ask the price of the machine.'},
   {'en': 'Okay. How much is it?', 'pt': 'Certo. Quanto custa?', 'ok': True, 'fb': 'Asks the price of the machine.'}]},
  {'npc': 'Two dollars. Do you have coins?', 'pt': 'Dois dólares. Você tem moedas?', 'opts': [
   {'en': 'Yes, I have four quarters.', 'pt': 'Tenho, quatro moedas de vinte e cinco.', 'ok': True, 'fb': 'Says what coins you have.'},
   {'en': 'Yes, I am coins.', 'pt': 'Sim, eu sou moedas.', 'ok': False, 'fb': 'Use I have.'},
   {'en': 'Two dollars is Monday.', 'pt': 'Dois dólares é segunda.', 'ok': False, 'fb': 'It does not make sense.'}]},
  {'npc': 'Great. Press start.', 'pt': 'Ótimo. Aperte iniciar.', 'opts': [
   {'en': 'I have a start.', 'pt': 'Eu tenho um iniciar.', 'ok': False, 'fb': 'It does not fit.'},
   {'en': 'Okay. Done. How long it takes?', 'pt': 'Ok. Pronto. Quanto tempo leva?', 'ok': False, 'fb': 'In questions use does it: how long does it take.'},
   {'en': 'Done. How long does it take?', 'pt': 'Pronto. Quanto tempo demora?', 'ok': True, 'fb': 'Natural question for time.'}]},
  {'npc': 'Forty minutes.', 'pt': 'Quarenta minutos.', 'opts': [
   {'en': 'Thanks for the help. Bye!', 'pt': 'Valeu pela ajuda. Tchau!', 'ok': True, 'fb': 'Thanks and goodbye.'},
   {'en': 'Forty dollars? Wow.', 'pt': 'Quarenta dólares? Nossa.', 'ok': False, 'fb': 'Minutes are time, not money.'},
   {'en': 'I forty minutes yesterday.', 'pt': 'Eu quarenta minutos ontem.', 'ok': False, 'fb': 'It does not make sense.'}]}]},
 'errors': [
  {'wrong': 'How works this machine?', 'fix': 'How does this machine work?', 'alt': 'How this machine works?', 'why': 'In questions, use does before the subject, and work stays simple.'},
  {'wrong': 'How much time it takes?', 'fix': 'How long does it take?', 'alt': 'How many time does it take?', 'why': 'For duration say how long does it take.'},
  {'wrong': 'I have four quarter.', 'fix': 'I have four quarters.', 'alt': 'I have four quartes.', 'why': 'Use the plural -s with numbers: four quarters.'},
  {'wrong': 'Put the clothes inside of the washer.', 'fix': 'Put your clothes in the washer.', 'alt': 'Put your clothes on the washer.', 'why': 'Use in the washer, without inside of.'}],
 'homework': 'Write 4 steps to wash clothes in a laundry room: clothes in, soap, coins, start.',
 'homework_items': ['Say 5 things you wash: clothes, socks, towels…', 'Write: How does this machine work? and How long does it take?', 'Listen to the dialogue again and shadow Claire.', 'Review: Do you have coins? / Press start. / Forty minutes.']}
