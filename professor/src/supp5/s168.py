"""Suplemento Quest v5 · aula 168: Passport control + regular Where do you live? (The Aristocats)."""
SUPP = {
 'reg': 130,
 'badge': {'icon': '🛂', 'name': 'Border Ready', 'desc': 'Answer the officer at passport control'},
 'culture': {
  'hook': 'When you arrive in the USA, an officer checks your passport and asks a few short questions. The questions are simple, and short, honest answers are the best.',
  'mythfact': [
   {'s': 'At passport control, the officer usually asks why you are visiting.', 'ans': True, 'why': 'Questions like “What’s the purpose of your visit?” are very common.'},
   {'s': 'You should give long, funny answers to the officer.', 'ans': False, 'why': 'Short, clear and honest answers are best.'},
   {'s': 'Many visitors need a visa or a special permission to enter the USA.', 'ans': True, 'why': 'It depends on the country, so check the rules before you travel.'},
   {'s': 'It is a good idea to know the address of your hotel.', 'ans': True, 'why': 'The officer may ask where you will stay.'},
   {'s': '“The Aristocats” is a movie about cats that live in Paris.', 'ans': True, 'why': 'It is an animated Disney film from 1970.'}],
  'wild': [
   {'kind': 'Sign at passport control', 'lines': ['**Visitors**', 'Have your passport ready', 'No phones, please'], 'decode': {'q': 'What should you have ready?', 'opts': ['Your passport', 'Your phone', 'Your coffee'], 'ans': 0, 'why': '“Have your passport ready.”'}},
   {'kind': 'Line sign', 'lines': ['**Wait here** for the next officer', 'One person at a time', 'Thank you'], 'decode': {'q': 'When do you go to the officer?', 'opts': ['When the officer calls you', 'Before everyone', 'Never'], 'ans': 0, 'why': 'You wait for the next officer.'}}],
  'compare': {'br': 'In Brazil, people usually say a short “Boa tarde” to the officer and show the passport.', 'us': 'In the USA, the officer often asks a few questions: purpose, how long, where you will stay. They may also take a photo and fingerprints.', 'tip': 'Say: “Tourism. Two weeks. At a hotel.”', 'ask': 'Where do you want to stay on a trip? Say it in English.'},
  'quiz': [
   {'q': 'The officer says: “How long will you stay?” You answer…', 'opts': ['Two weeks.', 'At a hotel.', 'Tourism.'], 'ans': 0, 'why': 'How long = time.'},
   {'q': 'The officer asks: “Where will you stay?” You say…', 'opts': ['At a hotel in Midtown.', 'Two weeks.', 'I am on vacation.'], 'ans': 0, 'why': 'Where = place.'},
   {'q': 'What is a passport?', 'opts': ['a document for travel between countries', 'a kind of bag', 'a hotel room'], 'ans': 0, 'why': 'You need a passport to travel to other countries.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Lia at passport control',
  'text': [
   'Lia lands in **Atlanta** after a long flight. She is tired, but she is happy. This is her first trip to the USA. She follows the signs to passport control.',
   'The line is long. Lia waits. She holds her passport and thinks about the cat movie “The Aristocats.” In the film, the cats live in Paris. “Where do I live?” she thinks. “In São Paulo. And now I am in Atlanta.” She smiles.',
   'An officer named Bethany says, “**Next, please. Passport?**” “**Here you go.**” Bethany looks at the passport. “**What’s the purpose of your visit?**” “**Tourism. I’m here on vacation.**” “**How long will you stay?**” “**Two weeks.**”',
   '“**Where will you stay?**” “**At a hotel in Midtown.**” Lia has the name of the hotel on her phone. “**Do you have a return ticket?**” “Yes, I do,” Lia says. She shows the ticket. Bethany takes a photo of Lia and checks her fingers on a small machine.',
   'Bethany gives the passport back. “Welcome to the USA. Enjoy your trip!” “Thank you!” Lia says. She walks to baggage claim. Her trip starts now.'],
  'glossary': [{'w': 'lands', 'pt': 'pousa, aterrissa'}, {'w': 'tired', 'pt': 'cansada'}, {'w': 'passport control', 'pt': 'controle de passaportes'}, {'w': 'officer', 'pt': 'oficial, agente'}, {'w': 'purpose', 'pt': 'motivo, objetivo'}, {'w': 'tourism', 'pt': 'turismo'}, {'w': 'stay', 'pt': 'ficar, hospedar-se'}, {'w': 'return ticket', 'pt': 'passagem de volta'}, {'w': 'machine', 'pt': 'máquina, aparelho'}, {'w': 'welcome', 'pt': 'bem-vindo'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A tourist arrives in the USA', 'A cat goes to school', 'A man cooks lunch'], 'ans': 0, 'why': 'Lia goes through passport control in Atlanta.'},
  'scan': [{'q': 'What city does Lia land in?', 'ans': 'Atlanta', 'alt': ['atlanta']}, {'q': 'How long will Lia stay?', 'ans': 'two weeks', 'alt': ['2 weeks', 'two']}, {'q': 'Where will Lia stay?', 'ans': 'at a hotel in Midtown', 'alt': ['a hotel', 'hotel', 'in Midtown']}],
  'tf': [{'s': 'This is Lia’s first trip to the USA.', 'ans': True, 'why': 'The first paragraph says so.'}, {'s': 'Lia is in the USA for work.', 'ans': False, 'why': 'She is here on vacation.'}, {'s': 'Lia has a return ticket.', 'ans': True, 'why': '“Yes, I do,” and she shows it.'}, {'s': 'Bethany is not friendly at the end.', 'ans': False, 'why': 'She says welcome and enjoy your trip.'}],
  'order': ['Lia lands in Atlanta.', 'She waits in the line.', 'She gives her passport to Bethany.', 'She answers the questions.', 'Lia walks to baggage claim.'],
  'ctx': [{'sent': 'What’s the purpose of your visit?', 'w': 'purpose', 'opts': ['the reason', 'the price', 'the time'], 'ans': 0, 'why': 'Purpose = reason for the trip.'}, {'sent': 'How long will you stay?', 'w': 'stay', 'opts': ['be in a place for some time', 'run very fast', 'buy something'], 'ans': 0, 'why': 'Stay = be in a place for a time.'}, {'sent': 'Lia is tired.', 'w': 'tired', 'opts': ['needs to rest', 'is very hungry', 'is very cold'], 'ans': 0, 'why': 'Tired = needs rest.'}],
  'chunkHunt': ['Here you go.', 'What’s the purpose of your visit?', 'How long will you stay?', 'Where will you stay?'],
  'think': 'What are three things you must say at passport control?'},
 'convo': {'npc': {'name': 'Bethany'}, 'story': 'You arrive in Atlanta. Bethany is the passport officer. Answer her questions.', 'turns': [
  {'npc': 'Next, please. Passport?', 'pt': 'Próximo, por favor. Passaporte?', 'opts': [
   {'en': 'Here you go.', 'pt': 'Aqui está.', 'ok': True, 'fb': 'Gives the passport.'},
   {'en': 'Yes, I am next.', 'pt': 'Sim, eu sou o próximo.', 'ok': False, 'fb': 'She asks for a document.'},
   {'en': 'I have good.', 'pt': 'Eu tenho bom.', 'ok': False, 'fb': 'Does not make sense.'}]},
  {'npc': 'What’s the purpose of your visit?', 'pt': 'Qual o motivo da sua visita?', 'opts': [
   {'en': 'I am here for a hotel.', 'pt': 'Estou aqui por um hotel.', 'ok': False, 'fb': 'A hotel is not a purpose.'},
   {'en': 'Two weeks.', 'pt': 'Duas semanas.', 'ok': False, 'fb': 'That answers how long.'},
   {'en': 'Tourism. I’m here on vacation.', 'pt': 'Turismo. Estou de férias.', 'ok': True, 'fb': 'Clear reason.'}]},
  {'npc': 'How long will you stay?', 'pt': 'Quanto tempo vai ficar?', 'opts': [
   {'en': 'Two weeks.', 'pt': 'Duas semanas.', 'ok': True, 'fb': 'Short and clear.'},
   {'en': 'I stay in Atlanta since two weeks.', 'pt': 'Fico em Atlanta desde duas semanas.', 'ok': False, 'fb': 'Use: for two weeks.'},
   {'en': 'At a hotel.', 'pt': 'Em um hotel.', 'ok': False, 'fb': 'That answers where.'}]},
  {'npc': 'Where will you stay?', 'pt': 'Onde vai ficar?', 'opts': [
   {'en': 'Tourism.', 'pt': 'Turismo.', 'ok': False, 'fb': 'That answers why.'},
   {'en': 'In a hotel of Midtown.', 'pt': 'Em um hotel de Midtown.', 'ok': False, 'fb': 'Say: a hotel in Midtown.'},
   {'en': 'At a hotel in Midtown.', 'pt': 'Em um hotel em Midtown.', 'ok': True, 'fb': 'Clear place.'}]},
  {'npc': 'Do you have a return ticket?', 'pt': 'Tem passagem de volta?', 'opts': [
   {'en': 'Yes, I do. Here it is.', 'pt': 'Sim, tenho. Aqui está.', 'ok': True, 'fb': 'Answer and show it.'},
   {'en': 'Yes, I have return.', 'pt': 'Sim, eu tenho volta.', 'ok': False, 'fb': 'Say: a return ticket.'},
   {'en': 'At the airport.', 'pt': 'No aeroporto.', 'ok': False, 'fb': 'Does not answer the question.'}]}]},
 'errors': [
  {'wrong': 'I am here by vacation.', 'fix': 'I’m here on vacation.', 'alt': 'I am here in vacation.', 'why': 'Use on vacation.'},
  {'wrong': 'I stay two weeks.', 'fix': 'I’ll stay for two weeks.', 'alt': 'I stay since two weeks.', 'why': 'Future with will, and for + time.'},
  {'wrong': 'I will stay in a hotel of Midtown.', 'fix': 'I’ll stay at a hotel in Midtown.', 'alt': 'I will stay on a hotel in Midtown.', 'why': 'Use at a hotel and in a place.'},
  {'wrong': 'Yes, I have a volta ticket.', 'fix': 'Yes, I have a return ticket.', 'alt': 'Yes, I have a back ticket.', 'why': 'Return ticket is the name in English.'}],
 'homework': 'Write a short dialogue: you answer an officer about your trip, your time and your hotel.',
 'homework_items': ['Write your three answers: purpose, time, place.', 'Say aloud: How long will you stay?', 'Listen to the dialogue and shadow Lia.', 'Review the numbers and the weeks.']}
