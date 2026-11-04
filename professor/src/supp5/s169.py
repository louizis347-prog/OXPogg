"""Suplemento Quest v5 · aula 169: Baggage claim + regular Don't forget your keys! (The Frog Prince)."""
SUPP = {
 'reg': 153,
 'badge': {'icon': '🧳', 'name': 'Bag Hunter', 'desc': 'Find your bag and report a lost one'},
 'culture': {
  'hook': 'After a flight, you go to baggage claim and wait for your bag on a moving belt. If your bag does not come, there is a simple way to ask for help.',
  'mythfact': [
   {'s': 'At many airports, each flight has a belt number on a screen.', 'ans': True, 'why': 'The screen shows the flight and the belt, for example “Belt 4”.'},
   {'s': 'If your bag does not come, you should just go home.', 'ans': False, 'why': 'You should go to the baggage office and fill out a form.'},
   {'s': 'A bright ribbon or tag can help you see your bag.', 'ans': True, 'why': 'Many bags look the same, so a ribbon makes yours easy to find.'},
   {'s': 'Airlines often ask for your flight number and a description of the bag.', 'ans': True, 'why': 'They use it to look for the bag.'},
   {'s': '“The Frog Prince” is a fairy tale where a princess loses a golden ball.', 'ans': True, 'why': 'A frog finds the ball in the story.'}],
  'wild': [
   {'kind': 'Airport screen', 'lines': ['**Baggage claim**', 'Flight 214 from Miami: Belt 4', 'Flight 88 from Boston: Belt 2'], 'decode': {'q': 'Which belt is for the flight from Miami?', 'opts': ['Belt 4', 'Belt 2', 'Belt 8'], 'ans': 0, 'why': 'Flight 214 from Miami: Belt 4.'}},
   {'kind': 'Sign near the belts', 'lines': ['**Check your bag**', 'Many bags look the same', 'Lost bag? Go to the baggage office'], 'decode': {'q': 'Where do you go for a lost bag?', 'opts': ['The baggage office', 'The parking lot', 'The gate'], 'ans': 0, 'why': 'The sign says: go to the baggage office.'}}],
  'compare': {'br': 'In Brazil, people also wait at the esteira, and many use a ribbon or a colorful strap on the bag.', 'us': 'In the USA, a screen shows the belt for your flight. If your bag is lost, you report it to the airline at the baggage office.', 'tip': 'Take a photo of your bag before the trip.', 'ask': 'How is your suitcase? Describe it in English.'},
  'quiz': [
   {'q': 'You do not know where to go. You ask…', 'opts': ['Excuse me, where is baggage claim?', 'Where is the claim of bag?', 'Excuse me, baggage where?'], 'ans': 0, 'why': 'Where is + place is the normal question.'},
   {'q': 'Someone asks: “What does it look like?” You say…', 'opts': ['It’s big and blue.', 'It looks like me.', 'It is on Tuesday.'], 'ans': 0, 'why': 'You describe the bag.'},
   {'q': 'What is a belt at the airport?', 'opts': ['a moving band that brings bags', 'a kind of bag', 'a ticket'], 'ans': 0, 'why': 'Bags come out on the belt.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Rita and the red ribbon',
  'text': [
   'Rita lands in **Newark** after a long flight. She is tired, but she wants her suitcase. She asks a woman, “**Excuse me, where is baggage claim?**”',
   'The woman says, “**Follow the signs. It’s downstairs.**” Rita says thanks and goes down. A worker stands near the belts. “**Which belt is for my flight?**” “**Belt number four.**”',
   'Rita waits at belt four. Many bags go by, but she cannot see hers. “**I can’t find my suitcase,**” she says. The worker asks, “**What does it look like?**” “**It’s big, blue, with a red ribbon.**” They check the other belts. “**It’s not here. Where can I ask?**”',
   'The worker takes Rita to the baggage office. A man gives her a form. “**Fill it out**, please,” he says. Rita writes her name, her flight and her hotel. She thinks of “The Frog Prince.” In that story, a princess loses her golden ball, and a frog helps her. “I need a frog,” Rita laughs. The man says, “**It’ll turn up.**”',
   'The next day, the phone rings. The airline has her suitcase! A driver brings it to the hotel. The red ribbon is easy to see. Rita smiles and says, “Now I will not forget my bag again.”'],
  'glossary': [{'w': 'lands', 'pt': 'pousa'}, {'w': 'tired', 'pt': 'cansada'}, {'w': 'baggage claim', 'pt': 'restituição de bagagem'}, {'w': 'belt', 'pt': 'esteira'}, {'w': 'worker', 'pt': 'funcionário'}, {'w': 'ribbon', 'pt': 'fita'}, {'w': 'form', 'pt': 'formulário'}, {'w': 'fill it out', 'pt': 'preencha'}, {'w': 'turn up', 'pt': 'aparecer'}, {'w': 'princess', 'pt': 'princesa'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A woman looks for her suitcase', 'A man buys a ticket', 'A girl cooks dinner'], 'ans': 0, 'why': 'Rita cannot find her suitcase at the airport.'},
  'scan': [{'q': 'Which belt is for Rita’s flight?', 'ans': 'belt four', 'alt': ['four', 'belt 4', '4']}, {'q': 'What color is the ribbon?', 'ans': 'red', 'alt': ['it is red']}, {'q': 'What does the man give Rita?', 'ans': 'a form', 'alt': ['form']}],
  'tf': [{'s': 'Baggage claim is downstairs.', 'ans': True, 'why': '“It’s downstairs.”'}, {'s': 'Rita finds her suitcase at belt four.', 'ans': False, 'why': 'She cannot find it.'}, {'s': 'The suitcase is blue.', 'ans': True, 'why': 'It is big, blue, with a red ribbon.'}, {'s': 'The airline never finds the suitcase.', 'ans': False, 'why': 'A driver brings it the next day.'}],
  'order': ['Rita asks where baggage claim is.', 'She goes to belt four.', 'She cannot find her suitcase.', 'She fills out a form.', 'A driver brings the suitcase.'],
  'ctx': [{'sent': 'Rita is tired.', 'w': 'tired', 'opts': ['needs to rest', 'is very hungry', 'is very happy'], 'ans': 0, 'why': 'Tired = needs rest.'}, {'sent': 'A worker stands near the belts.', 'w': 'worker', 'opts': ['a person with a job', 'a kind of bag', 'a ticket'], 'ans': 0, 'why': 'A worker has a job at the airport.'}, {'sent': 'It’ll turn up.', 'w': 'turn up', 'opts': ['appear', 'break', 'go away'], 'ans': 0, 'why': 'Turn up = appear.'}],
  'chunkHunt': ['Excuse me, where is baggage claim?', 'Which belt is for my flight?', 'What does it look like?', 'Where can I ask?'],
  'think': 'How can you make your suitcase easy to find?'},
 'convo': {'npc': {'name': 'Chloe'}, 'story': 'You land in Newark. Chloe is an airport worker. Ask her for help.', 'turns': [
  {'npc': 'Hello! Can I help you?', 'pt': 'Olá! Posso ajudar?', 'opts': [
   {'en': 'Excuse me, where is baggage claim?', 'pt': 'Com licença, onde fica a esteira de bagagem?', 'ok': True, 'fb': 'Polite and clear.'},
   {'en': 'Where is the claim of bag?', 'pt': 'Onde fica a reclamação de mala?', 'ok': False, 'fb': 'Say baggage claim.'},
   {'en': 'Yes, I am helping.', 'pt': 'Sim, estou ajudando.', 'ok': False, 'fb': 'You need help.'}]},
  {'npc': 'Follow the signs. It’s downstairs.', 'pt': 'Siga as placas. Fica lá embaixo.', 'opts': [
   {'en': 'Belt number four.', 'pt': 'Esteira número quatro.', 'ok': False, 'fb': 'That is not a question.'},
   {'en': 'Thanks. Which belt is for my flight?', 'pt': 'Valeu. Qual esteira é do meu voo?', 'ok': True, 'fb': 'Natural next question.'},
   {'en': 'Which belt is my flight for?', 'pt': 'Qual esteira meu voo é para?', 'ok': False, 'fb': 'Word order: Which belt is for my flight?'}]},
  {'npc': 'Belt number four.', 'pt': 'Esteira número quatro.', 'opts': [
   {'en': 'Thank you. I can’t find my suitcase.', 'pt': 'Obrigada. Não encontro minha mala.', 'ok': True, 'fb': 'Explains the problem.'},
   {'en': 'I no find my suitcase.', 'pt': 'Eu não acho minha mala.', 'ok': False, 'fb': 'Say I can’t find.'},
   {'en': 'Four belts, thank you.', 'pt': 'Quatro esteiras, obrigada.', 'ok': False, 'fb': 'Does not fit.'}]},
  {'npc': 'What does it look like?', 'pt': 'Como ela é?', 'opts': [
   {'en': 'It’s big, blue, with a red ribbon.', 'pt': 'É grande, azul, com uma fita vermelha.', 'ok': True, 'fb': 'Describes the bag.'},
   {'en': 'It looks like a suitcase.', 'pt': 'Parece uma mala.', 'ok': False, 'fb': 'True, but not helpful.'},
   {'en': 'It is in my hotel.', 'pt': 'Está no meu hotel.', 'ok': False, 'fb': 'It does not answer.'}]},
  {'npc': 'Let’s check the other belts.', 'pt': 'Vamos ver nas outras esteiras.', 'opts': [
   {'en': 'It’s not here. Where can I ask?', 'pt': 'Não está aqui. Onde posso perguntar?', 'ok': True, 'fb': 'Asks where to get help.'},
   {'en': 'Yes, I check the belts.', 'pt': 'Sim, eu confiro as esteiras.', 'ok': False, 'fb': 'She said let’s.'},
   {'en': 'I like the red ribbon.', 'pt': 'Gosto da fita vermelha.', 'ok': False, 'fb': 'Does not fit.'}]}]},
 'errors': [
  {'wrong': 'Where is the baggage claim place?', 'fix': 'Where is baggage claim?', 'alt': 'Where is the claim of baggage?', 'why': 'In English: baggage claim, no “place”.'},
  {'wrong': 'I don’t find my suitcase.', 'fix': 'I can’t find my suitcase.', 'alt': 'I no find my suitcase.', 'why': 'Use can’t find when you cannot find it.'},
  {'wrong': 'How is your suitcase?', 'fix': 'What does your suitcase look like?', 'alt': 'How looks your suitcase?', 'why': 'To ask the look: What does it look like?'},
  {'wrong': 'It is downstair.', 'fix': 'It’s downstairs.', 'alt': 'It is in downstairs.', 'why': 'Downstairs has an s and needs no “in”.'}],
 'homework': 'Write a short dialogue: you cannot find your suitcase and describe it to an airport worker.',
 'homework_items': ['Describe your suitcase in 3 sentences.', 'Say aloud: Which belt is for my flight?', 'Listen to the dialogue and shadow Rita.', 'Review the colors and the sizes: big, small.']}
