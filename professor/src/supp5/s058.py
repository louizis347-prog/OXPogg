"""Suplemento Quest v5 · aula 58: Buying tickets + regular Next, Please! (I've Been Working on the Railroad)."""
TXT = [
 ['Mei and her friend Lia are in Seattle.', 'They are at the station.', 'There is a small window for city tour tickets.', 'A man waits behind the window.'],
 ['“**Hi! Two tickets for the tour, please**,” Mei says.', '“**Adults or children?**” the man asks.', '“**Two adults**,” she says.', '“**That’s forty dollars**,” he says.'],
 ['Mei asks, “**Is there a student discount?**”', '“**Yes, with a student card**,” the man says.', 'The two friends have their cards.', '“**Here you go**,” Mei says. The price is lower now.', '“**What time is the tour?**” “**At two o’clock.**”'],
 ['“**Enjoy the tour!**” the man says.', 'Mei and Lia have one hour, so they sit on a bench near the platform.', 'A worker calls, “**Next, please!**” and the line moves.', 'A train comes, and the people get on.'],
 ['Mei thinks of an old American folk song, “I’ve Been Working on the Railroad.”', 'People sing it about workers on the railroad.', 'In the song, they say, “**All aboard!**”', 'At two o’clock, the guide says it too, and the tour starts.', 'Mei is happy.', 'Tickets are easy when you know the words.'],
]
SUPP = {
 'reg': 11,
 'badge': {'icon': '🎟️', 'name': 'Ticket Buyer', 'desc': 'Buy tickets, ask about discounts and time'},
 'culture': {
  'hook': 'Buying a ticket is one of the first things you do on a trip. The words are short and always the same: how many, adult or child, how much, and what time.',
  'mythfact': [
   {'s': 'Tickets for children are often cheaper than tickets for adults.', 'ans': True, 'why': 'Many tours and museums have a lower child price.'},
   {'s': 'You usually need a student card to get a student discount.', 'ans': True, 'why': 'The seller wants to see proof that you are a student.'},
   {'s': 'In the USA, the price on a sign often includes all taxes.', 'ans': False, 'why': 'Sales tax is often added at the cash register, so the final price can be a little higher.'},
   {'s': 'Seattle is the capital of the state of Washington.', 'ans': False, 'why': 'Seattle is the biggest city, but the capital is Olympia.'},
   {'s': '“I’ve Been Working on the Railroad” is an American folk song.', 'ans': True, 'why': 'People have sung it since the 1800s.'}],
  'wild': [
   {'kind': 'Price board', 'lines': ['**City Tour**', 'Adult  $20', 'Child (under 12)  $10', 'Student (with card)  $15'], 'decode': {'q': 'How much are two adult tickets?', 'opts': ['$40', '$20', '$30'], 'ans': 0, 'why': '2 × $20 = $40.'}},
   {'kind': 'Tour times', 'lines': ['**Tours today**', '10:00 · 12:00 · 2:00 · 4:00', 'Buy tickets at the window'], 'decode': {'q': 'Where do you buy tickets?', 'opts': ['At the window', 'On the train', 'At home'], 'ans': 0, 'why': '“Buy tickets at the window.”'}}],
  'compare': {'br': 'In Brazil, a student can often pay meia-entrada with a student card, and many places have a similar discount.', 'us': 'In the USA, discounts for students and children exist too, but you often have to ask: “Is there a student discount?”', 'tip': 'Say the number first: “Two tickets for the tour, please.”', 'ask': 'Do you use a student card when you buy tickets? Say it in English.'},
  'quiz': [
   {'q': 'You want two tickets. You say…', 'opts': ['Two tickets for the tour, please.', 'Two tour tickets is.', 'I am two tickets.'], 'ans': 0, 'why': 'Say the number, then the ticket and what it is for.'},
   {'q': '“Adults or children?” The seller wants to know…', 'opts': ['who the tickets are for', 'what time it is', 'where the tour is'], 'ans': 0, 'why': 'The price changes for adults and children.'},
   {'q': 'The seller says “Here you go.” It means…', 'opts': ['This is for you', 'Go away', 'I am here'], 'ans': 0, 'why': 'We say it when we give something to a person.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Two Tickets for Two O’Clock',
  'text': [' '.join(p) for p in TXT],
  'glossary': [{'w': 'tickets', 'pt': 'ingressos'}, {'w': 'window', 'pt': 'guichê / janela'}, {'w': 'tour', 'pt': 'passeio'}, {'w': 'adults', 'pt': 'adultos'}, {'w': 'children', 'pt': 'crianças'}, {'w': 'student', 'pt': 'estudante'}, {'w': 'discount', 'pt': 'desconto'}, {'w': 'price', 'pt': 'preço'}, {'w': 'bench', 'pt': 'banco (de sentar)'}, {'w': 'folk song', 'pt': 'canção folclórica'}],
  'fast': {'q': 'What is this story about?', 'opts': ['Two friends buy tour tickets', 'A trip to the airport', 'A dinner at a restaurant'], 'ans': 0, 'why': 'Mei buys two tickets for a city tour.'},
  'scan': [{'q': 'How many tickets does Mei buy?', 'ans': 'two', 'alt': ['2', 'two tickets']}, {'q': 'What city are they in?', 'ans': 'Seattle', 'alt': ['seattle']}, {'q': 'What time is the tour?', 'ans': 'two o’clock', 'alt': ['2 o’clock', 'at two o’clock', '2:00']}],
  'tf': [{'s': 'The tickets are for two adults.', 'ans': True, 'why': '“Two adults.”'}, {'s': 'The friends have no student cards.', 'ans': False, 'why': 'The two friends have their cards.'}, {'s': 'The tour is at four o’clock.', 'ans': False, 'why': 'The tour is at two o’clock.'}, {'s': 'The friends wait near the platform.', 'ans': True, 'why': 'They sit on a bench near the platform.'}],
  'order': ['Mei asks for two tickets.', 'The man says it is forty dollars.', 'Mei asks about a student discount.', 'The friends wait on a bench.', 'The guide says “All aboard!”'],
  'ctx': [{'sent': 'Is there a student discount?', 'w': 'discount', 'opts': ['a lower price', 'a bigger ticket', 'a train'], 'ans': 0, 'why': 'A discount is a lower price.'}, {'sent': 'Here you go.', 'w': 'Here you go', 'opts': ['This is for you', 'Please go home', 'I do not know'], 'ans': 0, 'why': 'We say it when we give something to a person.'}, {'sent': 'The line moves.', 'w': 'line', 'opts': ['people waiting one behind the other', 'a long song', 'a piece of paper'], 'ans': 0, 'why': 'A line is a queue of people.'}],
  'chunkHunt': ['Two tickets for the tour, please.', 'Adults or children?', 'Is there a student discount?', 'What time is the tour?'],
  'think': 'Do you buy tickets online or at a window? Which one is easier for you?'},
 'convo': {'npc': {'name': 'Mei'}, 'story': 'You sell tickets at a window in Seattle. Mei is your customer. Help her buy tickets for the tour.', 'turns': [
  {'npc': 'Hi! Two tickets for the tour, please.', 'pt': 'Oi! Dois ingressos para o passeio, por favor.', 'opts': [
   {'en': 'Adults or children?', 'pt': 'Adultos ou crianças?', 'ok': True, 'fb': 'It gives the right price.'},
   {'en': 'I am a ticket.', 'pt': 'Eu sou um ingresso.', 'ok': False, 'fb': 'It does not make sense.'},
   {'en': 'Two tickets is.', 'pt': 'Dois ingressos é.', 'ok': False, 'fb': 'Ask Adults or children?'}]},
  {'npc': 'Two adults.', 'pt': 'Dois adultos.', 'opts': [
   {'en': 'That is forty dollar.', 'pt': 'Isso é quarenta dólar.', 'ok': False, 'fb': 'Dollars with -s.'},
   {'en': 'That’s forty dollars.', 'pt': 'São quarenta dólares.', 'ok': True, 'fb': 'Clear and natural.'},
   {'en': 'Two adults is nice.', 'pt': 'Dois adultos é legal.', 'ok': False, 'fb': 'Say the price.'}]},
  {'npc': 'Is there a student discount?', 'pt': 'Tem desconto para estudante?', 'opts': [
   {'en': 'Yes, with a student card.', 'pt': 'Sim, com carteirinha.', 'ok': True, 'fb': 'The card is the proof.'},
   {'en': 'Yes, I am student.', 'pt': 'Sim, eu sou estudante.', 'ok': False, 'fb': 'Say with a student card.'},
   {'en': 'No, the tour is at two.', 'pt': 'Não, o passeio é às duas.', 'ok': False, 'fb': 'It does not answer the question.'}]},
  {'npc': 'Here you go. What time is the tour?', 'pt': 'Aqui está. Que horas é o passeio?', 'opts': [
   {'en': 'At two o’clock.', 'pt': 'Às duas horas.', 'ok': True, 'fb': 'Use at + time.'},
   {'en': 'In two hours o’clock.', 'pt': 'Em duas horas relógio.', 'ok': False, 'fb': 'Say at two o’clock.'},
   {'en': 'Two dollars.', 'pt': 'Dois dólares.', 'ok': False, 'fb': 'She asks about time, not price.'}]},
  {'npc': 'Thank you!', 'pt': 'Obrigada!', 'opts': [
   {'en': 'You’re welcome. Enjoy the tour!', 'pt': 'De nada. Aproveite o passeio!', 'ok': True, 'fb': 'A friendly end.'},
   {'en': 'Do you have a card?', 'pt': 'Você tem cartão?', 'ok': False, 'fb': 'She already showed it.'},
   {'en': 'Adults or children?', 'pt': 'Adultos ou crianças?', 'ok': False, 'fb': 'It was asked at the beginning.'}]}]},
 'errors': [
  {'wrong': 'Two ticket for tour, please.', 'fix': 'Two tickets for the tour, please.', 'alt': 'Two tickets to tour, please.', 'why': 'More than one: tickets. Say the tour.'},
  {'wrong': 'It is forty dollar.', 'fix': 'It’s forty dollars.', 'alt': 'It are forty dollars.', 'why': 'More than one dollar uses -s.'},
  {'wrong': 'I am student.', 'fix': 'I’m a student.', 'alt': 'I student.', 'why': 'Use a before a job or role.'},
  {'wrong': 'The tour is in two o’clock.', 'fix': 'The tour is at two o’clock.', 'alt': 'The tour is on two o’clock.', 'why': 'Use at with clock times.'}],
 'homework': 'Write a short dialogue: you buy three tickets for a tour and ask about a discount.',
 'homework_items': ['Write the price of 2 adults and 1 child at $20 and $10.', 'Record yourself asking for tickets.', 'Listen to the dialogue again and shadow Mei.', 'Review: Adults or children? / Is there a student discount?']}
