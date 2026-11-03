"""Suplemento Quest v5 · aula 72: Trash and recycling + regular Take out the trash (Cheaper by the Dozen)."""
SUPP = {
 'reg': 129,
 'badge': {'icon': '♻️', 'name': 'Green Neighbor', 'desc': 'Ask where things go and learn the trash and recycling days'},
 'culture': {
  'hook': 'In the USA, every building and city has its own trash rules. Learn the words for bins and pickup days so you never put the wrong thing in the wrong place.',
  'mythfact': [
   {'s': 'In American English, people usually say "trash" or "garbage" for things you throw away.', 'ans': True, 'why': 'In British English people often say "rubbish".'},
   {'s': 'Every US city uses the same colors for its bins.', 'ans': False, 'why': 'Colors and rules change from city to city, so read the label or ask a neighbor.'},
   {'s': 'In many cities, trucks collect trash and recycling on different days.', 'ans': True, 'why': 'A common schedule is trash one day and recycling another day.'},
   {'s': 'In some cities, food scraps go in a separate compost bin.', 'ans': True, 'why': 'Seattle, for example, asks people to put food scraps in a compost bin.'},
   {'s': 'You can put a pizza box with grease in the recycling bin.', 'ans': False, 'why': 'Greasy cardboard is often not accepted. Check the rules of your city.'}],
  'wild': [
   {'kind': 'Notice in a building', 'lines': ['**TRASH** pickup: Tuesday', '**RECYCLING** pickup: Friday', 'Please put bins out after 6 p.m. the night before'], 'decode': {'q': 'When is the recycling pickup?', 'opts': ['Friday', 'Tuesday', 'Monday'], 'ans': 0, 'why': '"RECYCLING pickup: Friday".'}},
   {'kind': 'Label on a bin', 'lines': ['**BLUE BIN**', 'YES: paper, cardboard, plastic bottles, cans', 'NO: food, plastic bags'], 'decode': {'q': 'Can you put a plastic bag in the blue bin?', 'opts': ['No', 'Yes', 'Only on Friday'], 'ans': 0, 'why': 'The label says "NO: food, plastic bags".'}}],
  'compare': {'br': 'In Brazil, many buildings have a trash room or a bin on the street, and in many cities the collection days are told by the building manager.', 'us': 'In the USA, people often put bins on the curb the night before pickup and bring them back after the truck passes.', 'tip': 'Ask a neighbor: "When do they collect the trash?" It is the fastest way to learn the local rules.', 'ask': 'How does trash collection work where you live? Describe it in English.'},
  'quiz': [
   {'q': 'You want to know where to put the trash. You say...', 'opts': ['Where does the trash go?', 'Where is trash my?', 'What trash is where?'], 'ans': 0, 'why': 'Where does ... go? is the natural question.'},
   {'q': 'A neighbor says, "Trash is Tuesday." This means...', 'opts': ['The truck comes on Tuesday', 'You throw trash on Tuesday only at night', 'Trash is a name'], 'ans': 0, 'why': 'It tells the day of the trash pickup.'},
   {'q': 'Where does glass often go in a city with separate bins?', 'opts': ['In a special glass or recycling bin', 'In the compost bin', 'Down the sink'], 'ans': 0, 'why': 'Many cities collect glass separately, but rules vary.'}]},
 'reading': {
  'genre': 'Note to a new neighbor',
  'title': 'Welcome to the building!',
  'text': [
   'Hi Mei! My name is Gabe. I live next door, in **Seattle**. Welcome to our building. I want to help you with the **trash** because it is the first thing new neighbors ask.',
   'The **big bin** is **behind the building**. All the trash goes there. Please **take out the trash** in a bag and close the lid. In our building, trash day is **Tuesday**.',
   'The **blue bin** is for **recycling**. You can put clean paper, cardboard and plastic bottles inside. Please do not put food in it. **Recycling is Friday.**',
   'The **green bin** is for **glass**. Be careful! Do not throw a glass bottle in the trash. Put it in the green bin. **Almost done!** One more thing: food scraps go in the small brown bin in the kitchen.',
   'At first, I forgot the days all the time. Now I write them on a card and put the card on my fridge. My neighbor says, "**Thanks for the reminder**," every week.',
   'If you have a question, **knock on my door**. A big building is like a team. Thanks for helping us keep it clean!'],
  'glossary': [{'w': 'trash', 'pt': 'lixo'}, {'w': 'bin', 'pt': 'lixeira'}, {'w': 'behind', 'pt': 'atrás de'}, {'w': 'lid', 'pt': 'tampa'}, {'w': 'recycling', 'pt': 'reciclagem'}, {'w': 'cardboard', 'pt': 'papelão'}, {'w': 'glass', 'pt': 'vidro'}, {'w': 'scraps', 'pt': 'sobras'}, {'w': 'reminder', 'pt': 'lembrete'}, {'w': 'knock', 'pt': 'bater (à porta)'}],
  'fast': {'q': 'What is this text about?', 'opts': ['Trash and recycling rules in a building', 'A trip to Seattle', 'A recipe for dinner'], 'ans': 0, 'why': 'Gabe explains the bins and days to a new neighbor.'},
  'scan': [{'q': 'Where is the big bin?', 'ans': 'behind the building', 'alt': ['behind', 'in back']}, {'q': 'What day is recycling?', 'ans': 'Friday', 'alt': ['on friday']}, {'q': 'What color is the bin for glass?', 'ans': 'green', 'alt': ['the green bin']}],
  'tf': [
   {'s': 'Trash day is Tuesday.', 'ans': True, 'why': '"Trash day is Tuesday."'},
   {'s': 'Food goes in the blue bin.', 'ans': False, 'why': '"Please do not put food in it."'},
   {'s': 'Gabe lives in Seattle.', 'ans': True, 'why': '"I live next door, in Seattle."'},
   {'s': 'Gabe puts glass in the trash.', 'ans': False, 'why': 'Glass goes in the green bin.'}],
  'order': ['Gabe writes a note to Mei.', 'He says where the big bin is.', 'He explains the blue bin and Friday.', 'He says glass goes in the green bin.', 'He asks Mei to knock if she has a question.'],
  'ctx': [
   {'sent': 'Please close the lid.', 'w': 'lid', 'opts': ['the cover of a bin', 'a kind of food', 'a door key'], 'ans': 0, 'why': 'A lid is the cover on a bin or pot.'},
   {'sent': 'Please do not put food in it.', 'w': 'put', 'opts': ['place', 'eat', 'break'], 'ans': 0, 'why': 'To put = to place something somewhere.'},
   {'sent': 'Thanks for the reminder.', 'w': 'reminder', 'opts': ['a note that helps you remember', 'a present', 'a trash bag'], 'ans': 0, 'why': 'A reminder helps you not to forget.'}],
  'chunkHunt': ['take out the trash', 'Almost done', 'Thanks for the reminder', 'behind the building'],
  'think': 'Who takes out the trash in your home? How often do you do it?'},
 'convo': {'npc': {'name': 'Mei'}, 'story': 'You live in a building in Seattle. Mei is a new neighbor and asks about trash and recycling.', 'turns': [
  {'npc': 'Excuse me, where does the trash go?', 'pt': 'Com licença, onde vai o lixo?', 'opts': [
   {'en': 'The trash is very good.', 'pt': 'O lixo é muito bom.', 'ok': False, 'fb': 'It does not answer where it goes.'},
   {'en': 'In the big bin behind the building.', 'pt': 'Na lixeira grande atrás do prédio.', 'ok': True, 'fb': 'Natural answer with a place.'},
   {'en': 'I am a neighbor.', 'pt': 'Eu sou vizinho.', 'ok': False, 'fb': 'True, but it does not answer.'}]},
  {'npc': 'And recycling?', 'pt': 'E reciclagem?', 'opts': [
   {'en': 'Blue bin for paper and plastic.', 'pt': 'Lixeira azul para papel e plástico.', 'ok': True, 'fb': 'Short and clear.'},
   {'en': 'Yes, recycling is blue.', 'pt': 'Sim, reciclagem é azul.', 'ok': False, 'fb': '"Yes" does not fit a where question.'},
   {'en': 'I recycle on my bed.', 'pt': 'Eu reciclo na minha cama.', 'ok': False, 'fb': 'Wrong place, no sense.'}]},
  {'npc': 'When do they collect it?', 'pt': 'Quando eles recolhem?', 'opts': [
   {'en': 'In the green bin.', 'pt': 'Na lixeira verde.', 'ok': False, 'fb': 'She asks when, not where.'},
   {'en': 'It collects Tuesday.', 'pt': 'Ele coleta terça.', 'ok': False, 'fb': 'Use the days: Trash is Tuesday.'},
   {'en': 'Trash is Tuesday. Recycling is Friday.', 'pt': 'O lixo é terça. A reciclagem é sexta.', 'ok': True, 'fb': 'Gives both days clearly.'}]},
  {'npc': 'Thanks! What about glass?', 'pt': 'Valeu! E o vidro?', 'opts': [
   {'en': 'Glass goes in the green bin.', 'pt': 'Vidro vai na lixeira verde.', 'ok': True, 'fb': 'Use "goes in" for where things go.'},
   {'en': 'I see through glass.', 'pt': 'Eu vejo através do vidro.', 'ok': False, 'fb': 'Wrong meaning of the question.'},
   {'en': 'Glass is on Monday.', 'pt': 'O vidro é na segunda.', 'ok': False, 'fb': 'It is not what she asked, and it is not the right day.'}]}]},
 'homework': 'Write the trash and recycling rules of your home in English: where each thing goes and what day the truck comes.',
 'homework_items': ['Write 4 sentences: where trash, paper, plastic and glass go.', 'Record yourself saying: Trash is Tuesday. Recycling is Friday.', 'Listen to the dialogue again and shadow Mei.', 'Review: Where does the trash go? / When do they collect it? / goes in.'],
 'errors': [
  {'wrong': 'Where goes the trash?', 'fix': 'Where does the trash go?', 'alt': 'Where does go the trash?', 'why': 'Questions use does + subject + base verb: does the trash go.'},
  {'wrong': 'The trash is in Tuesday.', 'fix': 'Trash is Tuesday.', 'alt': 'The trash is on Tuesday.', 'why': 'For days, use on (on Tuesday) or just say the day.'},
  {'wrong': 'Glass go in the green bin.', 'fix': 'Glass goes in the green bin.', 'alt': 'Glass going in the green bin.', 'why': 'Glass is singular, so the verb takes -es: goes.'},
  {'wrong': 'I throw the trash to the bin.', 'fix': 'I put the trash in the bin.', 'alt': 'I throw the trash at the bin.', 'why': 'Use in for the place: in the bin.'}]}
