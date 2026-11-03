"""Suplemento Quest v5 · aula 56: A small problem + regular Call for Help! (Rapunzel)."""
TXT = [
 ['Sol is in Miami.', 'He is at a big hotel.', 'It is night, and he is tired.', 'He stands at the door of room 412.', 'He puts his key card on the lock.', 'The light stays red.'],
 ['Sol goes down to the lobby.', 'A man at the front desk says, “**Hello, how can I help?**”', '“**My key doesn’t work**,” Sol says.', '“**I’m sorry. I’ll send someone**,” the man says.'],
 ['“Thank you. Also, **the air conditioner is off**.”', '“Is it too hot?”', '“Yes, very hot.”', '“**We’ll fix it right away**,” the man says.'],
 ['Soon, a woman from the hotel opens the door with a new key.', 'She fixes the air conditioner in five minutes.', 'The room is cool again.', '“**Thanks for your patience**,” she says.', 'Sol puts a towel on the chair and smiles.'],
 ['Sol thinks of Rapunzel, a girl in an old fairy tale.', 'She is in a high tower with no door, and she needs help.', 'Sol’s problem is small.', 'He can ask for help at the front desk.', '“**It’s not a big deal**,” he says to himself.', 'Tonight, he sleeps well.'],
]
SUPP = {
 'reg': 88,
 'badge': {'icon': '🛎️', 'name': 'Front Desk Friend', 'desc': 'Report a small hotel problem politely and get help'},
 'culture': {
  'hook': 'A hotel problem is not the end of your trip. Staff expect questions, and a clear, polite sentence at the front desk usually gets help very fast.',
  'mythfact': [
   {'s': 'Many hotels use plastic key cards, not metal keys.', 'ans': True, 'why': 'You touch or insert the card, and a light on the lock changes color.'},
   {'s': 'You must pay extra to report a broken air conditioner.', 'ans': False, 'why': 'A problem in your room is for the hotel to fix. Just tell the front desk.'},
   {'s': 'You can often call the front desk from the phone in your room.', 'ans': True, 'why': 'Many room phones have a button or a short number for the front desk.'},
   {'s': 'Miami is a city in the state of Florida.', 'ans': True, 'why': 'It is in the south of Florida, and it is warm most of the year.'},
   {'s': 'The story of Rapunzel is about a hotel in Miami.', 'ans': False, 'why': 'It is an old German fairy tale, published by the Brothers Grimm in 1812.'}],
  'wild': [
   {'kind': 'Door hanger', 'lines': ['**Do Not Disturb**', 'Please come back later.', 'Thank you!'], 'decode': {'q': 'When do you hang this sign on your door?', 'opts': ['When you do not want visitors', 'When you want a towel', 'When the key is broken'], 'ans': 0, 'why': 'Do Not Disturb = please do not knock.'}},
   {'kind': 'Sign at the front desk', 'lines': ['**Need help?**', 'Dial 0 from your room phone.', 'We are here 24 hours a day.'], 'decode': {'q': 'How can you call the front desk?', 'opts': ['Dial 0', 'Dial 24', 'Send a letter'], 'ans': 0, 'why': '“Dial 0 from your room phone.”'}}],
  'compare': {'br': 'In Brazil, many hotels also have a recepção open all day, and people often ask for help in person.', 'us': 'In the USA, you can call from your room or go to the lobby. Staff usually say “Sorry for the trouble” and act fast.', 'tip': 'Start with a short sentence: “My key doesn’t work.”', 'ask': 'What small problem can happen in a hotel room? Say it in English.'},
  'quiz': [
   {'q': 'Your key card does not open the door. You say…', 'opts': ['My key doesn’t work.', 'My key is hungry.', 'I work key.'], 'ans': 0, 'why': 'Doesn’t work = does not work.'},
   {'q': 'The staff say “We’ll fix it right away.” It means…', 'opts': ['They will fix it very soon', 'They will never fix it', 'You must fix it'], 'ans': 0, 'why': 'Right away = very soon.'},
   {'q': 'Where do you go for help in a hotel?', 'opts': ['The front desk', 'The pool', 'The elevator'], 'ans': 0, 'why': 'The front desk helps guests with problems.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Room 412',
  'text': [' '.join(p) for p in TXT],
  'glossary': [{'w': 'lobby', 'pt': 'saguão'}, {'w': 'front desk', 'pt': 'recepção'}, {'w': 'key', 'pt': 'chave'}, {'w': 'air conditioner', 'pt': 'ar-condicionado'}, {'w': 'fix', 'pt': 'consertar'}, {'w': 'towel', 'pt': 'toalha'}, {'w': 'tower', 'pt': 'torre'}, {'w': 'patience', 'pt': 'paciência'}, {'w': 'someone', 'pt': 'alguém'}, {'w': 'lock', 'pt': 'fechadura'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A small problem in a hotel room', 'A trip to the beach', 'A birthday party'], 'ans': 0, 'why': 'The key and the air conditioner do not work.'},
  'scan': [{'q': 'What is the room number?', 'ans': '412', 'alt': ['four twelve', 'room 412']}, {'q': 'Who helps Sol at the lobby?', 'ans': 'a man at the front desk', 'alt': ['a man', 'the man']}, {'q': 'How many minutes to fix the air conditioner?', 'ans': 'five', 'alt': ['5', 'five minutes']}],
  'tf': [{'s': 'Sol is at a hotel in Miami.', 'ans': True, 'why': 'Sol is in Miami, at a big hotel.'}, {'s': 'His key opens the door.', 'ans': False, 'why': 'The light stays red.'}, {'s': 'The room is too cold.', 'ans': False, 'why': 'The air conditioner is off, so the room is very hot.'}, {'s': 'A woman fixes the air conditioner.', 'ans': True, 'why': 'She fixes it in five minutes.'}],
  'order': ['Sol puts his key card on the lock.', 'He goes down to the lobby.', 'He says, “My key doesn’t work.”', 'A woman fixes the air conditioner.', 'Sol thinks of Rapunzel and sleeps well.'],
  'ctx': [{'sent': 'Sol goes down to the lobby.', 'w': 'lobby', 'opts': ['the big hall at the hotel entrance', 'a small room upstairs', 'a kind of food'], 'ans': 0, 'why': 'The lobby is the hall near the entrance.'}, {'sent': 'We’ll fix it right away.', 'w': 'right away', 'opts': ['very soon', 'next year', 'at night'], 'ans': 0, 'why': 'Right away = very soon.'}, {'sent': 'It’s not a big deal.', 'w': 'big deal', 'opts': ['a serious problem', 'not important', 'a big hotel'], 'ans': 1, 'why': 'Not a big deal = not important.'}],
  'chunkHunt': ['My key doesn’t work.', 'I’ll send someone.', 'The air conditioner is off.', 'We’ll fix it right away.'],
  'think': 'What small problem can happen on a trip? Who can help you?'},
 'convo': {'npc': {'name': 'Cole'}, 'story': 'You are at a hotel in Miami. Cole works at the front desk. Tell him about your problem.', 'turns': [
  {'npc': 'Hello, front desk. How can I help?', 'pt': 'Olá, recepção. Como posso ajudar?', 'opts': [
   {'en': 'My key doesn’t work.', 'pt': 'Minha chave não funciona.', 'ok': True, 'fb': 'Short and clear.'},
   {'en': 'My key no work.', 'pt': 'Minha chave não trabalha.', 'ok': False, 'fb': 'Use doesn’t work.'},
   {'en': 'I am the front desk.', 'pt': 'Eu sou a recepção.', 'ok': False, 'fb': 'Cole is at the front desk.'}]},
  {'npc': 'I’m sorry. I’ll send someone.', 'pt': 'Sinto muito. Vou mandar alguém.', 'opts': [
   {'en': 'Also, the air conditioner is on.', 'pt': 'Além disso, o ar está ligado.', 'ok': False, 'fb': 'The problem is that it is off.'},
   {'en': 'The air conditioner is no.', 'pt': 'O ar-condicionado é não.', 'ok': False, 'fb': 'Say it is off.'},
   {'en': 'Thank you. Also, the air conditioner is off.', 'pt': 'Obrigado. Além disso, o ar-condicionado está desligado.', 'ok': True, 'fb': 'Also adds a second problem.'}]},
  {'npc': 'Is it too hot?', 'pt': 'Está muito quente?', 'opts': [
   {'en': 'Yes, very hot.', 'pt': 'Sim, muito quente.', 'ok': True, 'fb': 'Natural short answer.'},
   {'en': 'Yes, I have hot.', 'pt': 'Sim, eu tenho quente.', 'ok': False, 'fb': 'Use it is hot or very hot.'},
   {'en': 'No, thank you.', 'pt': 'Não, obrigado.', 'ok': False, 'fb': 'It does not answer the question.'}]},
  {'npc': 'We’ll fix it right away.', 'pt': 'Vamos consertar já.', 'opts': [
   {'en': 'You are welcome.', 'pt': 'De nada.', 'ok': False, 'fb': 'You thank him; he does not thank you.'},
   {'en': 'Thanks a lot.', 'pt': 'Muito obrigado.', 'ok': True, 'fb': 'Polite thanks.'},
   {'en': 'I fix the air.', 'pt': 'Eu conserto o ar.', 'ok': False, 'fb': 'The hotel fixes it.'}]},
  {'npc': 'Sorry again for the trouble!', 'pt': 'Desculpe de novo pelo problema!', 'opts': [
   {'en': 'No worries. Thanks!', 'pt': 'Sem problema. Valeu!', 'ok': True, 'fb': 'Friendly and short.'},
   {'en': 'You are very trouble.', 'pt': 'Você é muito problema.', 'ok': False, 'fb': 'Not polite and not correct.'},
   {'en': 'My key is red.', 'pt': 'Minha chave é vermelha.', 'ok': False, 'fb': 'It does not fit the conversation.'}]}]},
 'errors': [
  {'wrong': 'My key not works.', 'fix': 'My key doesn’t work.', 'alt': 'My key don’t work.', 'why': 'With it/he/she use doesn’t + base verb: work.'},
  {'wrong': 'The air conditioner is turned off.', 'fix': 'The air conditioner is off.', 'alt': 'The air conditioner is no.', 'why': 'For a simple problem say is off.'},
  {'wrong': 'I want that you fix it.', 'fix': 'Can you fix it, please?', 'alt': 'You fix it now.', 'why': 'Use Can you…? + base verb. It is polite.'},
  {'wrong': 'I have hot in my room.', 'fix': 'It is very hot in my room.', 'alt': 'I am hot of the room.', 'why': 'For the room, say it is hot.'}],
 'homework': 'Write 3 short sentences about a problem in a hotel room and ask the front desk for help.',
 'homework_items': ['Write: My ___ doesn’t work.', 'Record yourself saying 3 hotel problems.', 'Listen to the dialogue again and shadow Cole.', 'Review: I’ll send someone / We’ll fix it right away.']}
