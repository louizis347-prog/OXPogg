"""Suplemento Quest v5 · aula 196: Video call home + regular Say hi to Grandma (Five Little Peppers)."""
SUPP = {
 'reg': 106,
 'badge': {'icon': '📹', 'name': 'Video Call Pro', 'desc': 'Fix sound and picture on a video call and say goodbye warmly'},
 'culture': {
  'hook': 'Many families in the USA and Brazil stay close by video call. A few short sentences about sound and picture can save a long call.',
  'mythfact': [
   {'s': 'On a video call, it is normal to ask, “Can you hear me?”', 'ans': True, 'why': 'Sound problems are common, so people check early.'},
   {'s': 'You cannot talk if you see “You’re on mute.”', 'ans': False, 'why': 'It only means your microphone is off. Turn it on and talk.'},
   {'s': 'People often say “Talk soon” at the end of a call.', 'ans': True, 'why': 'It is a friendly, short goodbye.'},
   {'s': '“Five Little Peppers and How They Grew” is from 1881.', 'ans': True, 'why': 'Margaret Sidney published it in 1881.'},
   {'s': 'It is rude to show your home on a video call to family.', 'ans': False, 'why': 'Family and friends often love to see a new home.'}],
  'wild': [
   {'kind': 'Message on a screen', 'lines': ['**You’re on mute.**', 'Click the microphone to talk.'], 'decode': {'q': 'What should you do?', 'opts': ['Click the microphone', 'Close the door', 'Call again tomorrow'], 'ans': 0, 'why': 'The message says to click the microphone.'}},
   {'kind': 'Text message', 'lines': ['Hi Mom! Call at 7?', '**Bad connection** at my place today.', 'Maybe the wi-fi is slow.'], 'decode': {'q': 'What is the problem?', 'opts': ['The wi-fi is slow', 'The phone is broken', 'It is too late'], 'ans': 0, 'why': 'She says the wi-fi is slow.'}}],
  'compare': {'br': 'In Brazil, many people say “Está me ouvindo?” and “Tchau, beijo!” at the end of a call.', 'us': 'In the USA, people often say “Can you hear me?” at the start and “Love you, talk soon” at the end.', 'tip': 'Say: “Can you hear me? Turn up the volume.”', 'ask': 'How do you ask if people can hear you? Say it in English.'},
  'quiz': [
   {'q': 'You want to know if she hears you. You ask…', 'opts': ['Can you hear me?', 'You hear me can?', 'Do you hearing me?'], 'ans': 0, 'why': 'Can + you + base verb: Can you hear me?'},
   {'q': 'The sound is low. You say…', 'opts': ['Turn up the volume.', 'Turn the volume up me.', 'Up the volume turn.'], 'ans': 0, 'why': 'Turn up the volume is a short command.'},
   {'q': 'You want to see the room. You say…', 'opts': ['Show me your room!', 'Show to me you room!', 'Show I your room!'], 'ans': 0, 'why': 'Show me + your + noun.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Can you hear me?',
  'text': [
   'Ruth lives in a new apartment in Dayton. It is winter, and it is cold outside. Her mom is far away, so Ruth makes a **video call**. She sits on the sofa and opens her laptop. The screen is bright, and she smiles. She waits for her mom to answer the call.',
   '“**Hi, Mom! Can you see me?**” “**Hi, honey! Yes, I can see you!**” “**Can you hear me?**” “**A little. Turn up the volume.**” Ruth clicks the button. “**Better now?**” “**Yes, perfect. How are you?**”',
   '“**I’m great. I love my new place.**” “**Show me your apartment!**” “**Okay. This is my living room.**” Ruth turns the camera. Her mom sees a sofa, a window and a green plant. Mom smiles, and her eyes get wet.',
   'Ruth thinks about a book, “Five Little Peppers.” A poor mother and her five children stay close with love, not money. Ruth has a family like that. “**Miss you**,” she says. “**Love you. Talk soon.**” Mom starts to answer, but Ruth hears nothing. “Oh no,” Mom says, “**you’re on mute!**” They both laugh.'],
  'glossary': [{'w': 'video call', 'pt': 'chamada de vídeo'}, {'w': 'winter', 'pt': 'inverno'}, {'w': 'screen', 'pt': 'tela'}, {'w': 'volume', 'pt': 'volume'}, {'w': 'camera', 'pt': 'câmera'}, {'w': 'plant', 'pt': 'planta'}, {'w': 'miss', 'pt': 'sentir saudade de'}, {'w': 'mute', 'pt': 'sem som (microfone desligado)'}, {'w': 'laugh', 'pt': 'rir'}, {'w': 'poor', 'pt': 'pobre'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A daughter shows her new home on a video call', 'A mother buys a laptop', 'A girl cooks dinner'], 'ans': 0, 'why': 'Ruth calls her mom and shows her apartment.'},
  'scan': [{'q': 'Where does Ruth live?', 'ans': 'Dayton', 'alt': ['in Dayton']}, {'q': 'What does Ruth turn?', 'ans': 'the camera', 'alt': ['camera']}, {'q': 'What is the weather?', 'ans': 'cold', 'alt': ['it is cold', 'winter']}],
  'tf': [{'s': 'Ruth’s mom is far away.', 'ans': True, 'why': 'This is why they make a video call.'}, {'s': 'Mom cannot see Ruth.', 'ans': False, 'why': 'She says, “Yes, I can see you!”'}, {'s': 'Ruth shows her living room.', 'ans': True, 'why': 'She turns the camera.'}, {'s': 'At the end, Mom is on mute.', 'ans': False, 'why': 'Ruth is on mute, so Mom says, “You’re on mute!”'}],
  'order': ['Ruth opens her laptop.', 'Mom cannot hear well.', 'Ruth turns up the volume.', 'Ruth shows her living room.', 'Mom says Ruth is on mute.'],
  'ctx': [{'sent': 'It is winter, and it is cold outside.', 'w': 'winter', 'opts': ['the cold season', 'a small room', 'a kind of food'], 'ans': 0, 'why': 'Winter is the cold season.'}, {'sent': 'Ruth turns the camera.', 'w': 'camera', 'opts': ['it shows the picture', 'it makes the sound', 'it opens the door'], 'ans': 0, 'why': 'The camera shows the picture.'}, {'sent': 'They both laugh.', 'w': 'laugh', 'opts': ['make a happy sound', 'cry a lot', 'sleep'], 'ans': 0, 'why': 'Laugh is a happy sound.'}],
  'chunkHunt': ['Can you hear me?', 'Turn up the volume.', 'Show me your apartment!', 'You’re on mute.'],
  'think': 'Who do you call by video? What is the first thing you say?'},
 'convo': {'npc': {'name': 'Ruth'}, 'story': 'You call your friend Ruth by video. She just moved to a new apartment.', 'turns': [
  {'npc': 'Hi! Can you see me?', 'pt': 'Oi! Você me vê?', 'opts': [
   {'en': 'Hi! Yes, I can see you!', 'pt': 'Oi! Sim, eu vejo você!', 'ok': True, 'fb': 'Natural answer with can.'},
   {'en': 'Yes, I see you can.', 'pt': 'Sim, eu vejo você pode.', 'ok': False, 'fb': 'Word order: I can see you.'},
   {'en': 'No, goodbye.', 'pt': 'Não, tchau.', 'ok': False, 'fb': 'Too early to say goodbye.'}]},
  {'npc': 'Can you hear me?', 'pt': 'Você me ouve?', 'opts': [
   {'en': 'I am hearing you no.', 'pt': 'Eu estou ouvindo você não.', 'ok': False, 'fb': 'Use: I can’t hear you.'},
   {'en': 'A little. Turn up the volume.', 'pt': 'Um pouco. Aumente o volume.', 'ok': True, 'fb': 'Says the problem and a fix.'},
   {'en': 'Yes, it is my screen.', 'pt': 'Sim, é a minha tela.', 'ok': False, 'fb': 'It does not answer the question.'}]},
  {'npc': 'Better now?', 'pt': 'Melhor agora?', 'opts': [
   {'en': 'Yes, perfect. How are you?', 'pt': 'Sim, perfeito. Como você está?', 'ok': True, 'fb': 'Good answer and a nice question.'},
   {'en': 'Yes, I am perfect volume.', 'pt': 'Sim, eu sou volume perfeito.', 'ok': False, 'fb': 'The sound is perfect, not you.'},
   {'en': 'Better now? Yes.', 'pt': 'Melhor agora? Sim.', 'ok': False, 'fb': 'Do not repeat the question.'}]},
  {'npc': 'I’m great. I love my new place.', 'pt': 'Estou ótima. Adoro meu lugar novo.', 'opts': [
   {'en': 'Okay. I am great place.', 'pt': 'Ok. Eu sou lugar ótimo.', 'ok': False, 'fb': 'Does not answer what Ruth said.'},
   {'en': 'I love it too! Show me your apartment!', 'pt': 'Eu também adoro! Me mostre seu apartamento!', 'ok': True, 'fb': 'Shares the joy, then asks.'},
   {'en': 'Show me, I love apartment.', 'pt': 'Mostre, eu adoro apartamento.', 'ok': False, 'fb': 'Use: Show me your apartment.'}]}]},
 'errors': [
  {'wrong': 'You are hearing me?', 'fix': 'Can you hear me?', 'alt': 'Can you to hear me?', 'why': 'Use Can + you + base verb. Do not use -ing with hear.'},
  {'wrong': 'I don’t see you good.', 'fix': 'I can’t see you well.', 'alt': 'I no can see you.', 'why': 'Use can’t + see, and well, not good, for how you see.'},
  {'wrong': 'Raise the volume to up.', 'fix': 'Turn up the volume.', 'alt': 'Turn the volume to up.', 'why': 'Turn up is a phrasal verb, with no to.'},
  {'wrong': 'I have missing you.', 'fix': 'I miss you.', 'alt': 'I am missing to you.', 'why': 'Use the simple present for feelings: I miss you.'}],
 'homework': 'Write a short video call with a friend: check the sound, turn up the volume and ask to see their room.',
 'homework_items': ['Write three sentences about a video call with your family.', 'Say aloud: Can you hear me?', 'Listen to the dialogue and shadow Ruth.', 'Review: video / volume / winter / miss.']}
