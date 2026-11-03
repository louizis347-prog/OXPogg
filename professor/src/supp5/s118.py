"""Suplemento Quest v5 · aula 118: Lost and found + regular Look for the keys (Finding Dory)."""
SUPP = {
 'reg': 89,
 'badge': {'icon': '🎒', 'name': 'Found It!', 'desc': 'Describe a lost item at the lost and found'},
 'culture': {
  'hook': 'Many buses, stations, airports, schools and stores in the USA have a lost and found. You go to the desk, say what you lost, and describe it. The staff look in a box or on a shelf.',
  'mythfact': [
   {'s': 'In English, “lost and found” is a place where lost things go.', 'ans': True, 'why': 'Staff keep found items there until the owner comes.'},
   {'s': 'At a lost and found, staff usually ask you to describe the item.', 'ans': True, 'why': 'Color, size and what is inside help them find it and check it is yours.'},
   {'s': 'You always get a lost item back the same day.', 'ans': False, 'why': 'It depends. Some places check once a day, and they keep items for a limited time.'},
   {'s': 'You may need to show an ID or sign a paper to take a found item.', 'ans': True, 'why': 'Many places do this to be sure the item goes to the right person.'},
   {'s': '“Finding Dory” is a Pixar film about a fish.', 'ans': True, 'why': 'Dory is a blue fish who looks for her family.'}],
  'wild': [
   {'kind': 'Sign at a bus station', 'lines': ['**Lost and Found**', 'Window 3', 'Open 9 a.m. – 5 p.m.', 'Bring your ID.'], 'decode': {'q': 'What should you bring?', 'opts': ['Your ID', 'Your bus', 'A water bottle'], 'ans': 0, 'why': 'The sign says “Bring your ID.”'}},
   {'kind': 'Tag on a found item', 'lines': ['**Found: black umbrella**', 'Date: March 4', 'Place: Bus 22'], 'decode': {'q': 'Where did they find the umbrella?', 'opts': ['On Bus 22', 'At a school', 'At Window 3'], 'ans': 0, 'why': 'The tag says “Place: Bus 22.”'}}],
  'compare': {'br': 'In Brazil, we say “achados e perdidos”, and many places keep lost items at the front desk too.', 'us': 'In the USA, big places often have a Lost and Found desk or a web form. Staff may ask you to describe the item and sign.', 'tip': 'Say: “I lost my … It’s … with …”', 'ask': 'Describe your bag in English: color, size, one thing inside.'},
  'quiz': [
   {'q': 'You lost your wallet. You say…', 'opts': ['I lost my wallet.', 'I lose my wallet yesterday.', 'My wallet is losted.'], 'ans': 0, 'why': 'Lose is irregular: lost.'},
   {'q': 'The staff ask: “What does it look like?” You…', 'opts': ['describe it', 'say your name only', 'ask for a taxi'], 'ans': 0, 'why': 'They want the color, size and details.'},
   {'q': 'What does “It happens” mean?', 'opts': ['This is normal. Don’t worry.', 'This is a big problem.', 'This never happens.'], 'ans': 0, 'why': 'It happens comforts a person after a small mistake.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'The black backpack',
  'text': [
   'Sam rides the bus home from class in **Cleveland**. At home, he looks for his backpack, but it is not there. “**I’m such a klutz**,” he says. His friend says, “**It happens.** Check **lost and found**.”',
   'The next day, Sam goes to the bus station. A woman works at the lost and found desk. “**Excuse me, I lost my backpack.**” “**What color is it?**” “**It’s black with a red zipper.**” “**Where did you lose it?**” “**Maybe on the bus.**”',
   '“**What’s inside?**” “**A notebook and a water bottle.**” “**Let me check.**” The woman goes to a shelf. She sees a hat, glasses, a purse, a charger and a wallet. Then she finds a black backpack. “**Is this it?**”',
   '“**Yes! That’s mine. Thank you!**” Sam says. He opens the bag and sees his notebook and his water bottle. “**Found it!**” he says, with a big smile. The woman writes his name on a paper, and Sam signs it.',
   'Sam thinks about the film “Finding Dory.” Dory forgets things, but she looks and looks until she finds her family. Sam smiles. Now he checks his bag before he leaves the bus.'],
  'glossary': [{'w': 'rides', 'pt': 'anda de (ônibus)'}, {'w': 'klutz', 'pt': 'desastrado'}, {'w': 'lost and found', 'pt': 'achados e perdidos'}, {'w': 'zipper', 'pt': 'zíper'}, {'w': 'inside', 'pt': 'dentro'}, {'w': 'shelf', 'pt': 'prateleira'}, {'w': 'hat', 'pt': 'chapéu, boné'}, {'w': 'glasses', 'pt': 'óculos'}, {'w': 'purse', 'pt': 'bolsa'}, {'w': 'charger', 'pt': 'carregador'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A student finds his lost backpack', 'A woman buys a hat', 'A bus driver lost a ticket'], 'ans': 0, 'why': 'Sam goes to lost and found and finds his backpack.'},
  'scan': [{'q': 'What color is the backpack?', 'ans': 'black', 'alt': ['black with a red zipper']}, {'q': 'What is inside the backpack?', 'ans': 'a notebook and a water bottle', 'alt': ['notebook and water bottle', 'a notebook and a bottle']}, {'q': 'Where does Sam go the next day?', 'ans': 'the bus station', 'alt': ['bus station', 'to the bus station']}],
  'tf': [{'s': 'Sam loses his backpack on a plane.', 'ans': False, 'why': 'He says, “Maybe on the bus.”'}, {'s': 'The backpack has a red zipper.', 'ans': True, 'why': 'It is black with a red zipper.'}, {'s': 'The woman finds the backpack on a shelf.', 'ans': True, 'why': 'She goes to a shelf and finds it.'}, {'s': 'Sam is angry at the woman.', 'ans': False, 'why': 'He says thank you and smiles.'}],
  'order': ['Sam looks for his backpack at home.', 'He goes to the lost and found desk.', 'He describes the backpack.', 'The woman finds a black backpack.', 'Sam signs a paper.'],
  'ctx': [{'sent': 'What’s inside the bag?', 'w': 'inside', 'opts': ['in the bag', 'next to the bag', 'far from the bag'], 'ans': 0, 'why': 'Inside = in the middle of something.'}, {'sent': 'The charger is on the shelf.', 'w': 'shelf', 'opts': ['a flat board on a wall', 'a kind of bus', 'a school desk'], 'ans': 0, 'why': 'A shelf holds things on a wall.'}, {'sent': 'She wears glasses to read.', 'w': 'glasses', 'opts': ['things you wear to see better', 'cups for water', 'a kind of hat'], 'ans': 0, 'why': 'Glasses help you see.'}],
  'chunkHunt': ['I lost my backpack.', 'What color is it?', 'Where did you lose it?', 'Is this it?'],
  'think': 'What was the last thing you lost? Where did you look for it?'},
 'convo': {'npc': {'name': 'Ms. Ortiz'}, 'story': 'You lost your backpack. You go to the lost and found desk at the bus station. Ms. Ortiz works there.', 'turns': [
  {'npc': 'Hello. Can I help you?', 'pt': 'Olá. Posso ajudar?', 'opts': [
   {'en': 'Excuse me, I losted my backpack.', 'pt': 'Com licença, eu perdi minha mochila.', 'ok': False, 'fb': 'Lose is irregular: I lost.'},
   {'en': 'Excuse me, I lost my backpack.', 'pt': 'Com licença, perdi minha mochila.', 'ok': True, 'fb': 'Clear and polite.'},
   {'en': 'Excuse me, I am a backpack.', 'pt': 'Com licença, eu sou uma mochila.', 'ok': False, 'fb': 'Wrong meaning.'}]},
  {'npc': 'What color is it?', 'pt': 'De que cor é?', 'opts': [
   {'en': 'It’s a backpack of black.', 'pt': 'É uma mochila de preto.', 'ok': False, 'fb': 'Say: It’s black.'},
   {'en': 'It’s on the bus.', 'pt': 'Está no ônibus.', 'ok': False, 'fb': 'She asks about color, not place.'},
   {'en': 'It’s black with a red zipper.', 'pt': 'É preta com zíper vermelho.', 'ok': True, 'fb': 'Gives color and one detail.'}]},
  {'npc': 'Where did you lose it?', 'pt': 'Onde você perdeu?', 'opts': [
   {'en': 'Maybe on the bus.', 'pt': 'Talvez no ônibus.', 'ok': True, 'fb': 'Maybe shows you are not sure.'},
   {'en': 'Maybe in the bus I lose.', 'pt': 'Talvez no ônibus eu perco.', 'ok': False, 'fb': 'The word order is wrong.'},
   {'en': 'Yes, I did.', 'pt': 'Sim, eu perdi.', 'ok': False, 'fb': 'It is a Where question, not yes/no.'}]},
  {'npc': 'What’s inside?', 'pt': 'O que tem dentro?', 'opts': [
   {'en': 'Inside is outside.', 'pt': 'Dentro é fora.', 'ok': False, 'fb': 'It does not make sense.'},
   {'en': 'It’s inside the bus.', 'pt': 'Está dentro do ônibus.', 'ok': False, 'fb': 'She asks about the things in the bag.'},
   {'en': 'A notebook and a water bottle.', 'pt': 'Um caderno e uma garrafa de água.', 'ok': True, 'fb': 'Lists two things.'}]},
  {'npc': 'Let me check. Is this it?', 'pt': 'Vou ver. É esta?', 'opts': [
   {'en': 'Yes! It’s me. Thanks!', 'pt': 'Sim! Sou eu. Valeu!', 'ok': False, 'fb': 'Say: That’s mine.'},
   {'en': 'No, I’m not.', 'pt': 'Não, eu não sou.', 'ok': False, 'fb': 'Wrong answer for this question.'},
   {'en': 'Yes! That’s mine. Thank you!', 'pt': 'Sim! É minha. Obrigado!', 'ok': True, 'fb': 'Mine = it belongs to me.'}]}]},
 'errors': [
  {'wrong': 'I losted my backpack.', 'fix': 'I lost my backpack.', 'alt': 'I have lost me backpack.', 'why': 'Lose is irregular: lost, not losted.'},
  {'wrong': 'It’s a backpack of black.', 'fix': 'It’s a black backpack.', 'alt': 'It’s black the backpack.', 'why': 'Color comes before the noun, or after It’s.'},
  {'wrong': 'Where you lost it?', 'fix': 'Where did you lose it?', 'alt': 'Where did you lost it?', 'why': 'Question in the past: did + you + lose.'},
  {'wrong': 'It is me.', 'fix': 'It’s mine.', 'alt': 'It is my.', 'why': 'Use mine for a thing that belongs to you.'}],
 'homework': 'Describe a bag, an umbrella or a wallet in 3 sentences: color, size, and what is inside.',
 'homework_items': ['Write: I lost my ___. It’s ___.', 'Say aloud: Where did you lose it?', 'Listen to the dialogue and shadow Maya.', 'Learn: hat, glasses, purse, wallet.']}
