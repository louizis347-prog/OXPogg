"""Suplemento Quest v5 · aula 65: Meet the landlord + regular The new neighbor (Doc McStuffins)."""
SUPP = {
 'reg': 162,
 'badge': {'icon': '🔑', 'name': 'Good Tenant', 'desc': 'Meet your landlord: key, laundry, trash day and problems'},
 'culture': {
  'hook': 'On the first day in a new home, you meet the landlord. You get the key and ask where things are, when trash day is and who to call for problems.',
  'mythfact': [
   {'s': 'The landlord is the person or company that owns the building.', 'ans': True, 'why': 'The tenant pays rent to the landlord.'},
   {'s': 'A tenant is a person who rents a home.', 'ans': True, 'why': 'The tenant lives in the home but does not own it.'},
   {'s': 'In many older buildings in the USA, the laundry room is in the basement.', 'ans': True, 'why': 'Shared laundry rooms are common in apartment buildings, often in the basement.'},
   {'s': 'Trash day is the same day all over the USA.', 'ans': False, 'why': 'Each city and building has its own days, so you must ask.'},
   {'s': '“Doc McStuffins” is an animated series about a girl who cares for toys.', 'ans': True, 'why': 'It started in 2012 and was created by Chris Nee.'}],
  'wild': [
   {'kind': 'Notice in the lobby', 'lines': ['**Trash day: every Tuesday**', 'Put bags outside by 8 a.m.', 'Thank you!'], 'decode': {'q': 'What day is trash day?', 'opts': ['Tuesday', 'Friday', 'Sunday'], 'ans': 0, 'why': '“every Tuesday”.'}},
   {'kind': 'Sign on a door', 'lines': ['**Laundry room**', 'Open 8 a.m. – 10 p.m.', 'Please clean the machines'], 'decode': {'q': 'What should you do after using the machines?', 'opts': ['Clean them', 'Break them', 'Lock them'], 'ans': 0, 'why': '“Please clean the machines.”'}}],
  'compare': {'br': 'In Brazil, the “síndico” helps with the building, and many people have a washing machine at home.', 'us': 'In the USA, the landlord or a building manager helps with problems, and many buildings have a shared laundry room.', 'tip': 'Ask: “Who do I call for problems?”', 'ask': 'Who helps you with problems at home? Say it in English.'},
  'quiz': [
   {'q': 'You want to find the laundry room. You ask…', 'opts': ['Where is the laundry room?', 'Where the laundry room is?', 'Where have the laundry?'], 'ans': 0, 'why': 'Where is… is the normal question.'},
   {'q': '“Don’t worry, I’ll fix it today.” It means…', 'opts': ['it will be repaired today', 'it is broken forever', 'it is a gift'], 'ans': 0, 'why': 'Fix = repair.'},
   {'q': '“Heads up!” is…', 'opts': ['a short warning', 'a goodbye', 'a price'], 'ans': 0, 'why': 'A heads up is a warning or tip.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Welcome home, Evan',
  'text': [
   'Evan has a new home in **Chicago**. Today he meets the landlord, Mrs. Park, in the lobby. He has two bags and a big smile. “**Hi! I’m your new tenant.**”',
   '“**Welcome! Here’s your key**,” she says. “**Thank you. Where is the laundry room?**” “**It’s in the basement.**” Evan asks, “**What day is trash day?**” She answers, “**It’s every Tuesday.**”',
   '“**Who do I call for problems?**” Evan asks. “**Call me. My number is on the door.**” “**Don’t worry, I’ll fix it today**,” she says, when he shows her a small problem with the light. Evan feels better.',
   'Evan thinks of Doc McStuffins, a cartoon about a girl and her toys. In many stories, a new neighbor rings the doorbell and says hello. Mrs. Park says, “Drop by anytime.” Evan laughs. A good home has good neighbors.',
   'That night, Evan sits in his new room. The light is on, and the key is on the table. He puts a sticky note on the door: “Trash day: Tuesday.” He is home. He smiles and says, “Good night, new place.”'],
  'glossary': [{'w': 'landlord', 'pt': 'proprietário (que aluga)'}, {'w': 'tenant', 'pt': 'inquilino'}, {'w': 'lobby', 'pt': 'saguão'}, {'w': 'basement', 'pt': 'porão'}, {'w': 'laundry room', 'pt': 'lavanderia'}, {'w': 'trash', 'pt': 'lixo'}, {'w': 'problem', 'pt': 'problema'}, {'w': 'doorbell', 'pt': 'campainha'}, {'w': 'neighbor', 'pt': 'vizinho'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A tenant meets his landlord', 'A man buys a car', 'A girl visits a museum'], 'ans': 0, 'why': 'Evan meets Mrs. Park, his landlord.'},
  'scan': [{'q': 'Where is the laundry room?', 'ans': 'in the basement', 'alt': ['basement', 'the basement']}, {'q': 'What day is trash day?', 'ans': 'Tuesday', 'alt': ['every Tuesday', 'tuesday']}, {'q': 'Where is the landlord’s number?', 'ans': 'on the door', 'alt': ['door', 'the door']}],
  'tf': [{'s': 'Evan is the landlord.', 'ans': False, 'why': 'Evan is the new tenant.'}, {'s': 'Trash day is every Tuesday.', 'ans': True, 'why': '“It’s every Tuesday.”'}, {'s': 'The laundry room is on the roof.', 'ans': False, 'why': 'It is in the basement.'}, {'s': 'Mrs. Park says she will fix the problem today.', 'ans': True, 'why': '“I’ll fix it today.”'}],
  'order': ['Evan says hi to the landlord.', 'She gives him the key.', 'He asks about the laundry room.', 'He asks about trash day.', 'She says she will fix a problem.'],
  'ctx': [{'sent': 'The landlord owns the building.', 'w': 'landlord', 'opts': ['a person who rents homes to others', 'a person who cooks', 'a person who drives'], 'ans': 0, 'why': 'A landlord rents a home to a tenant.'}, {'sent': 'The laundry room is in the basement.', 'w': 'basement', 'opts': ['the floor under the ground floor', 'the top floor', 'a small garden'], 'ans': 0, 'why': 'Basement = underground floor.'}, {'sent': 'Don’t worry.', 'w': 'worry', 'opts': ['feel afraid or nervous', 'sing a song', 'drink tea'], 'ans': 0, 'why': 'Don’t worry = it’s okay.'}],
  'chunkHunt': ['I’m your new tenant.', 'Where is the laundry room?', 'What day is trash day?', 'Who do I call for problems?'],
  'think': 'What do you ask on your first day in a new home?'},
 'convo': {'npc': {'name': 'Evan'}, 'story': 'You are the landlord. Evan is your new tenant. Welcome him and answer his questions.', 'turns': [
  {'npc': 'Hi! I’m your new tenant.', 'pt': 'Oi! Sou seu novo inquilino.', 'opts': [
   {'en': 'Welcome! Here’s your key.', 'pt': 'Bem-vindo! Aqui está sua chave.', 'ok': True, 'fb': 'A friendly welcome and the key.'},
   {'en': 'Welcome! Here is key you.', 'pt': 'Bem-vindo! Aqui é chave você.', 'ok': False, 'fb': 'Say: Here’s your key.'},
   {'en': 'I am a tenant too.', 'pt': 'Sou inquilino também.', 'ok': False, 'fb': 'You are the landlord.'}]},
  {'npc': 'Thank you. Where is the laundry room?', 'pt': 'Obrigado. Onde fica a lavanderia?', 'opts': [
   {'en': 'It is in the basement.', 'pt': 'Fica no porão.', 'ok': True, 'fb': 'Clear answer with in.'},
   {'en': 'It is on basement.', 'pt': 'Fica em porão.', 'ok': False, 'fb': 'Use in the basement.'},
   {'en': 'The laundry is key.', 'pt': 'A lavanderia é a chave.', 'ok': False, 'fb': 'Wrong meaning.'}]},
  {'npc': 'What day is trash day?', 'pt': 'Que dia é o dia do lixo?', 'opts': [
   {'en': 'It’s every Tuesday.', 'pt': 'É toda terça.', 'ok': True, 'fb': 'Use every + day.'},
   {'en': 'Trash is a day.', 'pt': 'Lixo é um dia.', 'ok': False, 'fb': 'It does not answer.'},
   {'en': 'It’s all the Tuesday.', 'pt': 'É toda a terça.', 'ok': False, 'fb': 'Say every Tuesday.'}]},
  {'npc': 'Who do I call for problems?', 'pt': 'Quem eu chamo se tiver problema?', 'opts': [
   {'en': 'You call to me.', 'pt': 'Você liga para mim.', 'ok': False, 'fb': 'Say: Call me.'},
   {'en': 'Call me. My number is on the door.', 'pt': 'Me ligue. Meu telefone está na porta.', 'ok': True, 'fb': 'Short and clear.'},
   {'en': 'The door is a problem.', 'pt': 'A porta é um problema.', 'ok': False, 'fb': 'Does not answer.'}]},
  {'npc': 'Don’t worry, I’ll fix it today.', 'pt': 'Não se preocupe, eu conserto hoje.', 'opts': [
   {'en': 'Thank you. See you soon!', 'pt': 'Obrigado. Até logo!', 'ok': True, 'fb': 'Polite ending.'},
   {'en': 'I am a tenant, you fix.', 'pt': 'Sou inquilino, você conserta.', 'ok': False, 'fb': 'It does not fit.'},
   {'en': 'Welcome! Here’s your key.', 'pt': 'Bem-vindo! Aqui está sua chave.', 'ok': False, 'fb': 'You already said that.'}]}]},
 'errors': [
  {'wrong': 'Where is the laundry room? It is on basement.', 'fix': 'It is in the basement.', 'alt': 'It is at the basement.', 'why': 'Use in for places inside a building.'},
  {'wrong': 'What day is the trash?', 'fix': 'What day is trash day?', 'alt': 'What day trash is?', 'why': 'The common phrase is trash day.'},
  {'wrong': 'It is all Tuesday.', 'fix': 'It is every Tuesday.', 'alt': 'It is each Tuesday.', 'why': 'For a weekly event, say every Tuesday.'},
  {'wrong': 'Who I call for problems?', 'fix': 'Who do I call for problems?', 'alt': 'Who I do call?', 'why': 'Questions need do before I.'}],
 'homework': 'Write 5 questions to ask your landlord on the first day.',
 'homework_items': ['Write 3 places in a building: lobby, basement, door.', 'Say aloud: Where is the laundry room?', 'Listen to the dialogue and shadow Evan.', 'Write your own trash day in English.']}
