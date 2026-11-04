"""Suplemento Quest v5 · aula 183: I lost my phone + regular Keep in touch (The Golden Girls)."""
SUPP = {
 'reg': 231,
 'badge': {'icon': '📱', 'name': 'Phone Found', 'desc': 'Describe a lost phone and ask the lost and found'},
 'culture': {
  'hook': 'When you lose a phone in the USA, you can ask at the train or bus station, call the lost and found, and use a friend’s phone to keep in touch while you wait.',
  'mythfact': [
   {'s': 'Many train and bus systems have a lost and found office.', 'ans': True, 'why': 'You can often call, visit, or fill out a form online.'},
   {'s': 'The staff can give your phone to anyone who asks.', 'ans': False, 'why': 'They usually ask you to describe it and show who you are.'},
   {'s': 'A good answer to “What does it look like?” gives color and case.', 'ans': True, 'why': 'Short details like “black, with a blue case” help a lot.'},
   {'s': 'Most phones have an app to find them.', 'ans': True, 'why': 'Many phones have a “find my phone” tool, but you must turn it on before you lose it.'},
   {'s': '“The Golden Girls” is a TV comedy from the 1980s.', 'ans': True, 'why': 'It started in 1985 and ended in 1992.'}],
  'wild': [
   {'kind': 'Sign at a station', 'lines': ['**Lost and Found**', 'Open Mon–Fri, 9 AM – 5 PM', 'Bring your ID.'], 'decode': {'q': 'What do you bring?', 'opts': ['Your ID', 'Your ticket', 'Your bike'], 'ans': 0, 'why': '“Bring your ID.”'}},
   {'kind': 'Online form', 'lines': ['What did you lose? **Phone**', 'Color: **Black**', 'Case: **Blue**', 'Where? **Train, Line 3**'], 'decode': {'q': 'What color is the case?', 'opts': ['Blue', 'Black', 'Red'], 'ans': 0, 'why': 'The form says “Case: Blue.”'}}],
  'compare': {'br': 'In Brazil, many people say “perdi o celular” and call their own number or ask people at the station.', 'us': 'In the USA, people often go to the lost and found office or use a website form at the transit company.', 'tip': 'Say: “I lost my phone on the train. It’s black, with a blue case.”', 'ask': 'How do you describe your phone in English?'},
  'quiz': [
   {'q': 'You lost your phone. You say…', 'opts': ['I lost my phone!', 'I lose my phone yesterday!', 'My phone is lose!'], 'ans': 0, 'why': 'Use the past: lost.'},
   {'q': 'Someone asks, “What does it look like?” You say…', 'opts': ['It’s black, with a blue case.', 'It looks to me black.', 'It is a phone yes.'], 'ans': 0, 'why': 'Say the color and the case.'},
   {'q': 'You call the lost and found. You ask…', 'opts': ['Did someone find a phone?', 'Do someone find a phone?', 'Someone finded a phone?'], 'ans': 0, 'why': 'Use did + find: Did someone find…?'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Where is my phone?',
  'text': [
   'Dee is in **Chicago**. She gets off the train at a big station. She puts her hand in her pocket, but it is empty. “**Oh no, I lost my phone!**” she says.',
   'Dee goes to the help desk. A worker, Evan, is there. “**Where did you last see it?**” he asks. “**On the train, I think.**” “**What does it look like?**” “**It’s black, with a blue case.**”',
   '“**Let me call the lost and found**,” Evan says. He dials a number. “**Hello, did someone find a phone? It’s black, with a blue case.**” He waits. Dee looks at the clock. She feels worried.',
   'Then Evan smiles. “**Good news. They have it.**” “**Thank goodness!**” Dee says. “**Thank you so much.**” The phone is at the station on the next line. She can pick it up before five o’clock.',
   'Dee borrows Evan’s phone for a minute and sends a message to her friend: “I lost my phone, but I found it.” She wants to keep in touch with her friends. She thinks about “The Golden Girls,” a TV comedy about four friends. They talk a lot, and they always **keep an eye on** each other. Dee smiles and goes to get her phone.'],
  'glossary': [{'w': 'lost', 'pt': 'perdi, perdido'}, {'w': 'pocket', 'pt': 'bolso'}, {'w': 'train', 'pt': 'trem'}, {'w': 'case', 'pt': 'capa'}, {'w': 'station', 'pt': 'estação'}, {'w': 'worker', 'pt': 'funcionário'}, {'w': 'help desk', 'pt': 'balcão de ajuda'}, {'w': 'worried', 'pt': 'preocupada'}, {'w': 'borrows', 'pt': 'pega emprestado'}, {'w': 'dials', 'pt': 'disca'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A woman loses her phone and a worker helps her', 'A man buys a new phone', 'A woman misses the train'], 'ans': 0, 'why': 'Dee loses her phone and Evan calls the lost and found.'},
  'scan': [{'q': 'Where does Dee think she lost her phone?', 'ans': 'on the train', 'alt': ['train', 'in the train']}, {'q': 'What color is the phone?', 'ans': 'black', 'alt': ['it is black', 'black with a blue case']}, {'q': 'What is the name of the worker?', 'ans': 'Evan', 'alt': ['his name is Evan']}],
  'tf': [{'s': 'Dee finds her phone in her pocket.', 'ans': False, 'why': 'Her pocket is empty.'}, {'s': 'The phone has a blue case.', 'ans': True, 'why': 'It is black, with a blue case.'}, {'s': 'The lost and found has the phone.', 'ans': True, 'why': 'Evan says, “They have it.”'}, {'s': 'Dee is angry at Evan.', 'ans': False, 'why': 'She says thank you so much.'}],
  'order': ['Dee loses her phone.', 'Evan asks where she last saw it.', 'Dee describes the phone.', 'Evan calls the lost and found.', 'Dee sends a message to a friend.'],
  'ctx': [{'sent': 'Her pocket is empty.', 'w': 'empty', 'opts': ['with nothing in it', 'with a lot inside', 'very small'], 'ans': 0, 'why': 'Empty = nothing inside.'}, {'sent': 'She feels worried.', 'w': 'worried', 'opts': ['afraid something is wrong', 'very happy', 'sleepy'], 'ans': 0, 'why': 'Worried = you think of a problem.'}, {'sent': 'Dee borrows Evan’s phone.', 'w': 'borrows', 'opts': ['uses it and gives it back', 'buys it', 'breaks it'], 'ans': 0, 'why': 'Borrow = use and return.'}],
  'chunkHunt': ['I lost my phone!', 'Where did you last see it?', 'What does it look like?', 'It’s black, with a blue case.', 'Thank you so much.'],
  'think': 'What do you do first when you lose something important?'},
 'convo': {'npc': {'name': 'Evan'}, 'story': 'You lost your phone at a train station in Chicago. Evan works at the help desk.', 'turns': [
  {'npc': 'Hi. How can I help you?', 'pt': 'Oi. Como posso ajudar?', 'opts': [
   {'en': 'Excuse me, I lost my phone!', 'pt': 'Com licença, perdi meu celular!', 'ok': True, 'fb': 'Clear and in the past.'},
   {'en': 'Excuse me, I lose my phone yesterday.', 'pt': 'Com licença, eu perco meu celular ontem.', 'ok': False, 'fb': 'Use the past: lost.'},
   {'en': 'Hello, I am a phone.', 'pt': 'Olá, eu sou um celular.', 'ok': False, 'fb': 'It does not make sense.'}]},
  {'npc': 'Oh no. Where did you last see it?', 'pt': 'Ai, não. Onde viu pela última vez?', 'opts': [
   {'en': 'On the train, I think.', 'pt': 'No trem, acho.', 'ok': True, 'fb': 'Gives a place.'},
   {'en': 'In the train I am thinking.', 'pt': 'No trem eu estou pensando.', 'ok': False, 'fb': 'Use I think, not I am thinking.'},
   {'en': 'Yes, I see it.', 'pt': 'Sim, eu vejo.', 'ok': False, 'fb': 'It does not answer where.'}]},
  {'npc': 'What does it look like?', 'pt': 'Como ele é?', 'opts': [
   {'en': 'It is black with a case blue.', 'pt': 'É preto com capa azul.', 'ok': False, 'fb': 'Adjective goes before: a blue case.'},
   {'en': 'I like it a lot.', 'pt': 'Eu gosto muito.', 'ok': False, 'fb': 'It does not describe it.'},
   {'en': 'It’s black, with a blue case.', 'pt': 'É preto, com capa azul.', 'ok': True, 'fb': 'Short and clear.'}]},
  {'npc': 'Let me call the lost and found.', 'pt': 'Vou ligar para achados e perdidos.', 'opts': [
   {'en': 'Thank you so much.', 'pt': 'Muito obrigada.', 'ok': True, 'fb': 'Kind reply.'},
   {'en': 'No, I call you.', 'pt': 'Não, eu ligo para você.', 'ok': False, 'fb': 'It does not fit.'},
   {'en': 'You are welcome.', 'pt': 'De nada.', 'ok': False, 'fb': 'You are the one who says thanks.'}]},
  {'npc': 'Good news. They have it.', 'pt': 'Boa notícia. Eles estão com ele.', 'opts': [
   {'en': 'Thank goodness!', 'pt': 'Graças a Deus!', 'ok': True, 'fb': 'Shows relief.'},
   {'en': 'It is a bad news.', 'pt': 'É uma má notícia.', 'ok': False, 'fb': 'The news is good.'},
   {'en': 'Where did you last see it?', 'pt': 'Onde você viu pela última vez?', 'ok': False, 'fb': 'Evan asks that, not you.'}]}]},
 'errors': [
  {'wrong': 'I lose my phone.', 'fix': 'I lost my phone.', 'alt': 'I losed my phone.', 'why': 'Lose is irregular: the past is lost.'},
  {'wrong': 'It is a case blue.', 'fix': 'It has a blue case.', 'alt': 'It has a case blue.', 'why': 'The color comes before the noun: a blue case.'},
  {'wrong': 'Did someone found my phone?', 'fix': 'Did someone find my phone?', 'alt': 'Does someone found my phone?', 'why': 'After did, use the base verb: find.'},
  {'wrong': 'My phone is in my pocket empty.', 'fix': 'My pocket is empty.', 'alt': 'My phone is in empty pocket.', 'why': 'Say what is empty: my pocket is empty.'}],
 'homework': 'Write a short dialogue: you lost your phone at a station and a worker helps you.',
 'homework_items': ['Describe your phone in two sentences.', 'Say aloud: I lost my phone!', 'Listen to the dialogue and shadow Evan.', 'Review: case / station / owner / silver / contact / hand.']}
