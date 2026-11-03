"""Suplemento Quest v5 · aula 72: Trash and recycling + regular Take out the trash (Cheaper by the Dozen)."""
SUPP = {
 'reg': 129,
 'badge': {'icon': '♻️', 'name': 'Recycling Pro', 'desc': 'Ask about trash, recycling and pickup days in English'},
 'sticker': {'cat': 'Everyday culture', 'title': 'Trash Day', 'sub': 'Blue bin or green bin?'},
 'culture': {
  'hook': 'In many American neighborhoods, each kind of waste has its own bin and its own pickup day. Learn how to ask and what to put where.',
  'polite': 'Start with **“Excuse me, where does the trash go?”** and end with **“Thanks for helping!”** Neighbors are usually happy to explain.',
  'mythfact': [
   {'s': 'In many US cities, recycling has a different bin from regular trash.', 'ans': True, 'why': 'Many cities ask people to separate recycling, often in a blue bin, but colors change from place to place.'},
   {'s': 'Every city in the USA uses the same bin colors.', 'ans': False, 'why': 'Rules and colors are set by each city or company, so always check local signs.'},
   {'s': 'Trash and recycling are often collected on different days.', 'ans': True, 'why': 'Many places collect trash one day and recycling another day.'},
   {'s': 'You can put a greasy pizza box in the paper recycling bin in many places.', 'ans': False, 'why': 'Food grease often spoils paper recycling, so many programs ask you not to.'},
   {'s': '“Take out the trash” means to carry the garbage outside.', 'ans': True, 'why': 'It is a very common home chore.'}],
  'wild': [
   {'kind': 'Pickup calendar', 'lines': ['**Trash:** Tuesday', '**Recycling:** Friday', '**Yard waste:** first Monday of the month', 'Bins out by 7 a.m.'], 'decode': {'q': 'When is recycling collected?', 'opts': ['Friday', 'Tuesday', 'Monday'], 'ans': 0, 'why': 'The calendar says “Recycling: Friday.”'}},
   {'kind': 'Sign on a bin', 'lines': ['**PAPER AND PLASTIC ONLY**', 'Please rinse bottles.', 'No food. No bags.'], 'decode': {'q': 'What can you put in this bin?', 'opts': ['Paper and plastic', 'Food', 'Plastic bags full of trash'], 'ans': 0, 'why': 'The sign says paper and plastic only.'}}],
  'compare': {'br': 'In Brazil many buildings have a place for lixo and, in some cities, coleta seletiva with different days or colors.', 'us': 'In the USA, many houses have curbside bins and a pickup day. Apartment buildings often have big bins in a shared place.', 'tip': 'Learn the words bin, trash, recycling and pickup day. They help in any new home.', 'ask': 'How do you separate your trash at home? Say it in English.'},
  'quiz': [
   {'q': 'You need to find the trash bin. You say…', 'opts': ['Excuse me, where does the trash go?', 'Where I throw it?', 'You have the trash?'], 'ans': 0, 'why': 'Where does the trash go? is the natural question.'},
   {'q': 'Trash is Tuesday. This means…', 'opts': ['It is collected on Tuesday', 'You buy trash on Tuesday', 'Tuesday is a bin'], 'ans': 0, 'why': 'Trash is Tuesday = pickup day is Tuesday.'},
   {'q': 'Which words go together?', 'opts': ['take out the trash', 'take on the trash up', 'put out the garbage up'], 'ans': 0, 'why': 'Take out the trash is the common phrase.'}]},
 'reading': {
  'genre': 'Family notice', 'title': 'Chores at the Baker house',
  'text': [
   'The Baker family is big and busy. In the film **Cheaper by the Dozen** (2003, directed by Shawn Levy), the parents, Tom and Kate, have twelve children. The house is noisy, and everyone must help.',
   'Today I imagine a note on their kitchen door. It says: “**Take out the trash**! **Clean the floor**! **Almost done**? **Thanks for the help**.”',
   'Jake takes the big trash bag to the bin behind the house. Nora puts paper and plastic in the blue bin. Glass goes in the green bin. “Trash is Tuesday,” says Kate, “and recycling is Friday.”',
   'Two small children sweep the floor with a broom. A teenager washes the dishes. “**Almost done**!” shouts Jake from the garden.',
   'In the evening, they sit at a long table for a big dinner. Tom smiles and says, “**Thanks for the help**, team.” A big family works well when everyone has a job.',
   'After dinner, the youngest child asks, “Is it Tuesday tomorrow?” “Yes,” says Jake, “so do not forget the trash!”'],
  'glossary': [{'w': 'trash', 'pt': 'lixo'}, {'w': 'bin', 'pt': 'lixeira'}, {'w': 'recycling', 'pt': 'reciclagem'}, {'w': 'plastic', 'pt': 'plástico'}, {'w': 'glass', 'pt': 'vidro'}, {'w': 'broom', 'pt': 'vassoura'}, {'w': 'sweep', 'pt': 'varrer'}, {'w': 'dishes', 'pt': 'louça'}, {'w': 'floor', 'pt': 'chão'}, {'w': 'noisy', 'pt': 'barulhenta'}],
  'fast': {'q': 'What is this text about?', 'opts': ['Chores and trash day in a big family', 'A trip on a plane', 'A new phone'], 'ans': 0, 'why': 'The family shares chores and sorts the trash.'},
  'scan': [{'q': 'How many children do Tom and Kate have?', 'ans': 'twelve', 'alt': ['12']}, {'q': 'Which day is recycling?', 'ans': 'Friday', 'alt': ['friday']}, {'q': 'What goes in the green bin?', 'ans': 'glass', 'alt': ['Glass']}],
  'tf': [{'s': 'The Baker house is quiet.', 'ans': False, 'why': 'The house is noisy.'}, {'s': 'Trash is on Tuesday.', 'ans': True, 'why': '“Trash is Tuesday.”'}, {'s': 'Glass goes in the blue bin.', 'ans': False, 'why': 'Paper and plastic go in the blue bin. Glass goes in the green bin.'}, {'s': 'The family has a big dinner in the evening.', 'ans': True, 'why': 'They sit at a long table for a big dinner.'}],
  'order': ['Kate says trash is Tuesday and recycling is Friday.', 'Jake takes the trash bag to the bin.', 'Nora puts paper and plastic in the blue bin.', 'Jake shouts, “Almost done!”', 'The family has a big dinner.'],
  'ctx': [{'sent': 'The house is noisy with twelve children.', 'w': 'noisy', 'opts': ['full of loud sounds', 'very clean', 'very cold'], 'ans': 0, 'why': 'Noisy = makes a lot of sound.'}, {'sent': 'Two children sweep the floor.', 'w': 'sweep', 'opts': ['clean with a broom', 'jump on', 'paint'], 'ans': 0, 'why': 'Sweep = clean with a broom.'}, {'sent': 'Almost done!', 'w': 'almost', 'opts': ['nearly', 'never', 'not at all'], 'ans': 0, 'why': 'Almost = nearly.'}],
  'chunkHunt': ['Take out the trash!', 'Clean the floor.', 'Almost done!', 'Thanks for the help.'],
  'think': 'What chores do you do at home? Who takes out the trash in your house?'},
 'convo': {'npc': {'name': 'Mei'}, 'story': 'You live in an apartment building in Seattle. Your new neighbor Mei asks about trash and recycling.',
  'turns': [
   {'npc': 'Excuse me, where does the trash go?', 'pt': 'Com licença, onde vai o lixo?', 'opts': [
    {'en': 'In the big bin behind the building.', 'pt': 'Na lixeira grande atrás do prédio.', 'ok': True, 'fb': 'Clear place: behind the building.'},
    {'en': 'The trash is going in Tuesday.', 'pt': 'O lixo vai terça.', 'ok': False, 'fb': 'She asked where, not when.'},
    {'en': 'Yes, I do.', 'pt': 'Sim, eu faço.', 'ok': False, 'fb': 'It does not answer.'}]},
   {'npc': 'And recycling?', 'pt': 'E reciclagem?', 'opts': [
    {'en': 'I recycle not.', 'pt': 'Eu não reciclo.', 'ok': False, 'fb': 'Say: I don’t recycle.'},
    {'en': 'Blue bin for paper and plastic.', 'pt': 'Lixeira azul para papel e plástico.', 'ok': True, 'fb': 'Short and clear.'},
    {'en': 'Recycling is a good idea.', 'pt': 'Reciclagem é uma boa ideia.', 'ok': False, 'fb': 'True, but it does not answer where.'}]},
   {'npc': 'When do they collect it?', 'pt': 'Quando eles recolhem?', 'opts': [
    {'en': 'Trash is Tuesday. Recycling is Friday.', 'pt': 'O lixo é terça. A reciclagem é sexta.', 'ok': True, 'fb': 'Two days, short sentences.'},
    {'en': 'They collect it in the bin.', 'pt': 'Eles recolhem na lixeira.', 'ok': False, 'fb': 'She asked when.'},
    {'en': 'In Tuesday and in Friday.', 'pt': 'Em terça e em sexta.', 'ok': False, 'fb': 'Use on with days, or just say Tuesday.'}]},
   {'npc': 'Thanks! What about glass?', 'pt': 'Valeu! E o vidro?', 'opts': [
    {'en': 'The glass go in green.', 'pt': 'O vidro vai em verde.', 'ok': False, 'fb': 'Say: Glass goes in the green bin.'},
    {'en': 'No, thanks.', 'pt': 'Não, obrigado.', 'ok': False, 'fb': 'Mei asked a question.'},
    {'en': 'Glass goes in the green bin.', 'pt': 'Vidro vai na lixeira verde.', 'ok': True, 'fb': 'Goes with glass (it).'}]},
   {'npc': 'Perfect. Thanks for helping!', 'pt': 'Perfeito. Valeu pela ajuda!', 'opts': [
    {'en': 'Any time! Welcome to the building.', 'pt': 'Quando quiser! Bem-vinda ao prédio.', 'ok': True, 'fb': 'Friendly and natural.'},
    {'en': 'You are welcome to trash.', 'pt': 'Você é bem-vinda ao lixo.', 'ok': False, 'fb': 'Wrong meaning.'},
    {'en': 'I thank you the help.', 'pt': 'Eu agradeço a ajuda.', 'ok': False, 'fb': 'Mei thanked you; say Any time.'}]}]},
 'errors': [
  {'wrong': 'Where I put the trash?', 'fix': 'Where do I put the trash?', 'alt': 'Where I do put the trash?', 'why': 'Questions need do/does: Where do I…?'},
  {'wrong': 'The trash is in Tuesday.', 'fix': 'The trash is on Tuesday.', 'alt': 'The trash is at Tuesday.', 'why': 'Use on with days of the week.'},
  {'wrong': 'Take out the garbage up.', 'fix': 'Take out the trash.', 'alt': 'Take the trash out of.', 'why': 'No extra up; the phrase is take out the trash.'},
  {'wrong': 'Glass go in the green bin.', 'fix': 'Glass goes in the green bin.', 'alt': 'Glass going in the green bin.', 'why': 'Third person singular: goes.'}],
 'homework': 'Look at your trash bins at home. Say in English where paper, plastic and glass go, and send a 30-second audio to your teacher.',
 'homework_items': ['Write the pickup days of your street in English.', 'Say 3 sentences with take out the trash.', 'Listen to the dialogue again and shadow Mei.', 'Review: Where does…go? / When do they collect it? / Almost done!']}
