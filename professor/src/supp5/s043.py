"""Suplemento Quest v5 · aula 43: Where is the bank? + regular Beside the fountain (West Side Story)."""
SUPP = {
 'reg': 146,
 'badge': {'icon': '🏦', 'name': 'Street Helper', 'desc': 'Ask and tell where places are in English'},
 'sticker': {'cat': 'Everyday culture', 'title': 'Finding Places in a US City', 'sub': 'Main Street and the next block'},
 'culture': {
  'hook': 'American cities are often built in blocks, so people explain distance with blocks and minutes. Asking a stranger for help is normal and usually friendly.',
  'polite': 'Start with **“Excuse me”** and finish with **“Thank you so much!”** It sounds polite and natural.',
  'mythfact': [
   {'s': 'Main Street is a very common street name in the USA.', 'ans': True, 'why': 'Many American towns have a Main Street in the center.'},
   {'s': 'The post office in the USA is called USPS.', 'ans': True, 'why': 'USPS means United States Postal Service.'},
   {'s': 'Nobody in the USA uses ATMs.', 'ans': False, 'why': 'ATMs are everywhere, and many work 24 hours.'},
   {'s': 'People give directions only in kilometers.', 'ans': False, 'why': 'The USA uses miles, blocks and walking minutes.'}],
  'wild': [
   {'kind': 'Door sign', 'lines': ['**First City Bank**', 'Mon–Fri 9:00–5:00', 'ATM open 24 hours', 'Closed on Sunday'], 'decode': {'q': 'Can you use the ATM at night?', 'opts': ['Yes, it is open 24 hours', 'No, never', 'Only on Sunday'], 'ans': 0, 'why': '“ATM open 24 hours.”'}},
   {'kind': 'Text message', 'lines': ['Hi! I\'m at the bank on Main Street.', 'It\'s next to the post office.', 'See you in five minutes!'], 'decode': {'q': 'Where is the bank?', 'opts': ['Next to the post office', 'Behind the school', 'Across the river'], 'ans': 0, 'why': '“It’s next to the post office.”'}}],
  'compare': {'br': 'In Brazil people often use landmarks, like “perto da padaria”, and many streets have a long name.', 'us': 'In the USA people often use blocks, street names and “next to”, and many towns have a Main Street.', 'tip': 'Use short landmarks: “next to the post office” is easy to understand.', 'ask': 'Where is a bank or a pharmacy near your home? Explain in English.'},
  'quiz': [
   {'q': 'You want help. How do you start?', 'opts': ['Excuse me, where is the bank?', 'You, bank where?', 'Bank is where?'], 'ans': 0, 'why': 'Excuse me + a full question is polite.'},
   {'q': '“It’s five minutes on foot.” It means…', 'opts': ['You can walk there', 'You need a plane', 'It is closed'], 'ans': 0, 'why': 'On foot = walking.'},
   {'q': 'What is Main Street?', 'opts': ['A very common street name', 'A kind of bank', 'A big store'], 'ans': 0, 'why': 'Many American towns have a Main Street.'}]},
 'reading': {
  'genre': 'Short story', 'title': 'A stranger asks for help',
  'text': [
   'Evan was new in Chicago. He had a map on his phone, but the battery was dead. He needed the bank, so he asked a woman on the corner, “**Excuse me, where is the bank?**”',
   'She smiled. “**It’s on Main Street**,” she said. “Is it far?” Evan asked. “**No, it’s five minutes on foot**,” she answered. “You can walk there.”',
   'Evan looked at the street. There was a pharmacy on the left and a small café on the right. “Is it next to the post office?” he asked. “**Yes, it’s next to it**,” she said. “The post office has a big blue sign.”',
   '“**Thank you so much!**” Evan said. “**You’re welcome. Have a nice day!**” she said. “**Good luck! It’s easy to find**.” Evan felt happy. People in this city were friendly.',
   'He walked past the café, past the pharmacy and saw the blue sign. Next to it was the bank, a tall gray building. It was open, and the door was heavy.',
   'Inside, a man at the desk said, “Good morning. How can I help you?” Evan took a deep breath and began to speak slowly, in clear English.'],
  'glossary': [{'w': 'new', 'pt': 'novo'}, {'w': 'battery', 'pt': 'bateria'}, {'w': 'dead', 'pt': 'descarregada'}, {'w': 'corner', 'pt': 'esquina'}, {'w': 'pharmacy', 'pt': 'farmácia'}, {'w': 'sign', 'pt': 'placa'}, {'w': 'tall', 'pt': 'alto'}, {'w': 'heavy', 'pt': 'pesada'}, {'w': 'on foot', 'pt': 'a pé'}],
  'fast': {'q': 'What is this text about?', 'opts': ['A man asks where the bank is', 'A boy loses his dog', 'A family goes to the beach'], 'ans': 0, 'why': 'Evan asks for the way to the bank.'},
  'scan': [{'q': 'Which street is the bank on?', 'ans': 'Main Street', 'alt': ['main street', 'main']}, {'q': 'How far is it on foot?', 'ans': 'five minutes', 'alt': ['5 minutes', '5']}, {'q': 'What color is the post office sign?', 'ans': 'blue', 'alt': ['big blue']}],
  'tf': [{'s': 'Evan’s phone battery is dead.', 'ans': True, 'why': 'The battery was dead.'}, {'s': 'The bank is far from the corner.', 'ans': False, 'why': 'It is five minutes on foot.'}, {'s': 'The bank is next to the post office.', 'ans': True, 'why': '“Yes, it’s next to it.”'}, {'s': 'The people in the city are unfriendly.', 'ans': False, 'why': 'Evan thinks people are friendly.'}],
  'order': ['Evan’s phone battery is dead.', 'Evan asks a woman where the bank is.', 'She says it is on Main Street.', 'Evan walks past the café and the pharmacy.', 'He sees the bank next to the post office.'],
  'ctx': [{'sent': 'He had a map on his phone, but the battery was dead.', 'w': 'dead', 'opts': ['empty, with no power', 'very old', 'very loud'], 'ans': 0, 'why': 'A dead battery has no power.'}, {'sent': 'It was open, and the door was heavy.', 'w': 'heavy', 'opts': ['hard to lift or push', 'very small', 'very cheap'], 'ans': 0, 'why': 'Heavy = not light.'}, {'sent': 'The bank was a tall gray building.', 'w': 'tall', 'opts': ['high', 'short', 'round'], 'ans': 0, 'why': 'Tall = high.'}],
  'chunkHunt': ['Where is the bank?', 'It’s on Main Street.', 'Is it far?', 'five minutes on foot', 'next to the post office'],
  'think': 'Think of a place near your home. How can you explain where it is in English?'},
 'convo': {'npc': {'name': 'Evan'}, 'story': 'You are on a street in Chicago. Evan is lost and needs the bank. Help him.', 'turns': [
  {'npc': 'Excuse me, where is the bank?', 'pt': 'Com licença, onde fica o banco?', 'opts': [
   {'en': 'It is on Main Street.', 'pt': 'Fica na Rua Principal.', 'ok': True, 'fb': 'Clear and short.'},
   {'en': 'The bank is not exist.', 'pt': 'O banco não existe.', 'ok': False, 'fb': 'Wrong grammar and meaning.'},
   {'en': 'I go to the bank yesterday.', 'pt': 'Eu vou ao banco ontem.', 'ok': False, 'fb': 'Does not give directions.'}]},
  {'npc': 'Is it far from here?', 'pt': 'Fica longe daqui?', 'opts': [
   {'en': 'Yes, it is five dollars.', 'pt': 'Sim, são cinco dólares.', 'ok': False, 'fb': 'Distance is not money.'},
   {'en': 'It is far of here.', 'pt': 'É longe daqui.', 'ok': False, 'fb': 'Say far from here.'},
   {'en': 'No, it’s five minutes on foot.', 'pt': 'Não, é a cinco minutos a pé.', 'ok': True, 'fb': 'Time on foot is a natural answer.'}]},
  {'npc': 'Is it next to the post office?', 'pt': 'Fica ao lado do correio?', 'opts': [
   {'en': 'Yes, it’s next to it.', 'pt': 'Sim, fica ao lado.', 'ok': True, 'fb': 'Confirms the place.'},
   {'en': 'Yes, it have a post office.', 'pt': 'Sim, tem um correio.', 'ok': False, 'fb': 'Use it is, not it have.'},
   {'en': 'I like the post.', 'pt': 'Eu gosto do correio.', 'ok': False, 'fb': 'Out of context.'}]},
  {'npc': 'Thank you so much!', 'pt': 'Muito obrigado!', 'opts': [
   {'en': 'Thank you too, bye.', 'pt': 'Obrigado você também, tchau.', 'ok': False, 'fb': 'He thanks you; answer You’re welcome.'},
   {'en': 'You’re welcome. Have a nice day!', 'pt': 'De nada. Tenha um bom dia!', 'ok': True, 'fb': 'The natural reply.'},
   {'en': 'No problem you.', 'pt': 'Sem problema você.', 'ok': False, 'fb': 'Grammar problem.'}]},
  {'npc': 'Good luck! It’s easy to find.', 'pt': 'Boa sorte! É fácil de achar.', 'opts': [
   {'en': 'You are easy.', 'pt': 'Você é fácil.', 'ok': False, 'fb': 'Wrong meaning.'},
   {'en': 'Thanks, see you!', 'pt': 'Valeu, até mais!', 'ok': True, 'fb': 'Friendly goodbye.'},
   {'en': 'Where is easy?', 'pt': 'Onde é fácil?', 'ok': False, 'fb': 'Does not make sense.'}]}]},
 'errors': [
  {'wrong': 'Where is the bank? It is in Main Street.', 'fix': 'It is on Main Street.', 'alt': 'It is at Main Street.', 'why': 'Use on with street names.'},
  {'wrong': 'It is five minutes by foot.', 'fix': 'It is five minutes on foot.', 'alt': 'It is five minutes with foot.', 'why': 'The fixed phrase is on foot.'},
  {'wrong': 'Is far from here?', 'fix': 'Is it far from here?', 'alt': 'It is far from here?', 'why': 'Questions need is it.'},
  {'wrong': 'The bank is next of the post office.', 'fix': 'The bank is next to the post office.', 'alt': 'The bank is next at the post office.', 'why': 'Next to is the fixed phrase.'}],
 'homework': 'Choose 3 places near your home and say in English where each one is, using next to and on foot.',
 'homework_items': ['Write 3 sentences with next to.', 'Record: “It’s five minutes on foot.”', 'Draw a small map and label 4 places.', 'Review: Excuse me, where is…? / You’re welcome.']}
