"""Suplemento Quest v5 · aula 174: Movie tickets + regular Return the tapes (Be Kind Rewind)."""
SUPP = {
 'reg': 201,
 'badge': {'icon': '🎫', 'name': 'Movie Night', 'desc': 'Buy movie tickets: movie, time, seats and price'},
 'culture': {
  'hook': 'At a movie theater in the USA, you buy a ticket for one movie at one time. Many theaters also let you choose your seat on a screen or an app.',
  'mythfact': [
   {'s': 'In many US theaters, you can choose your seat.', 'ans': True, 'why': 'Many theaters show a seat map when you buy the ticket.'},
   {'s': 'A movie ticket always costs the same price everywhere.', 'ans': False, 'why': 'The price changes by city, theater, time and day.'},
   {'s': 'Many theaters sell popcorn and drinks in the lobby.', 'ans': True, 'why': 'The snack counter is a normal part of a US theater.'},
   {'s': '“Sold out” means there are many free seats.', 'ans': False, 'why': 'It means there are no tickets left.'},
   {'s': '“Be Kind Rewind” is a comedy from 2008.', 'ans': True, 'why': 'It is about a small video rental shop.'}],
  'wild': [
   {'kind': 'Ticket window board', 'lines': ['**Adult** $12', 'Child $8', 'Today: 5:00 · 7:00 · 9:30'], 'decode': {'q': 'How much is one adult ticket?', 'opts': ['$12', '$8', '$9.30'], 'ans': 0, 'why': 'The board says Adult $12.'}},
   {'kind': 'Ticket', 'lines': ['**Theater 5**', 'Row F · Seat 8', '7:00 p.m. · The New Comedy'], 'decode': {'q': 'Which theater is the movie in?', 'opts': ['Number five', 'Number seven', 'Number eight'], 'ans': 0, 'why': 'The ticket says Theater 5.'}}],
  'compare': {'br': 'In Brazil, people also buy tickets at the box office or online, and many theaters have numbered seats.', 'us': 'In the USA, people often buy tickets on an app and then pick up snacks before the movie. Trailers usually play before the film starts.', 'tip': 'Say: “Two tickets for the seven o’clock movie.”', 'ask': 'What movie do you want to see? Say it in English.'},
  'quiz': [
   {'q': 'You want two tickets. You say…', 'opts': ['Two tickets, please.', 'Two ticket, please.', 'Please two of tickets.'], 'ans': 0, 'why': 'Two + plural noun: tickets.'},
   {'q': 'The seller asks, “Where do you want to sit?” You say…', 'opts': ['In the middle, please.', 'At seven o’clock.', 'Twelve dollars.'], 'ans': 0, 'why': 'The question is about the seat.'},
   {'q': '“Sold out” means…', 'opts': ['no tickets are left', 'the movie is free', 'the theater is closed forever'], 'ans': 0, 'why': 'All tickets are already sold.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Two tickets for seven o’clock',
  'text': [
   'Cory lives in **Portland**. On Friday, he wants to see a new comedy with his sister. He goes to the movie theater, and Carlos works at the ticket window.',
   '“**Hi! Two tickets for the seven o’clock movie.**” “**Which movie?**” “**The new comedy, please.**” “**Okay. Where do you want to sit?**” “**In the middle, not too close.**”',
   '“**Those seats are twelve dollars each**,” Carlos says. The front rows are **sold out**. Cory gives his card. “**Thanks. Theater number five.**” “**Where can I buy popcorn?**” “Over there, next to the door.”',
   'On the wall, Cory sees a poster of an old video shop. He remembers “Be Kind Rewind,” a comedy from 2008. In the film, two friends work at a small shop. People rent old tapes and then return them. The sign says, “**Be kind, rewind.**” Today we do not rewind movies, but we still return things.',
   'At seven, the lights go dark and the movie starts. Cory and his sister laugh a lot. It is a good night, and the popcorn is still warm.'],
  'glossary': [{'w': 'tickets', 'pt': 'ingressos'}, {'w': 'theater', 'pt': 'cinema, sala'}, {'w': 'seats', 'pt': 'lugares, assentos'}, {'w': 'middle', 'pt': 'meio'}, {'w': 'rows', 'pt': 'fileiras'}, {'w': 'popcorn', 'pt': 'pipoca'}, {'w': 'poster', 'pt': 'cartaz'}, {'w': 'tapes', 'pt': 'fitas de vídeo'}, {'w': 'rewind', 'pt': 'rebobinar'}, {'w': 'dark', 'pt': 'escuro'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A man buys movie tickets', 'A man cooks popcorn at home', 'A woman rents a car'], 'ans': 0, 'why': 'Cory buys two tickets for a movie.'},
  'scan': [{'q': 'How many tickets does Cory buy?', 'ans': 'two', 'alt': ['2', 'two tickets']}, {'q': 'How much is each seat?', 'ans': 'twelve dollars', 'alt': ['$12', '12 dollars', 'twelve']}, {'q': 'Which theater is it?', 'ans': 'number five', 'alt': ['five', '5', 'theater five']}],
  'tf': [{'s': 'Cory wants to sit in the middle.', 'ans': True, 'why': '“In the middle, not too close.”'}, {'s': 'Cory pays with cash.', 'ans': False, 'why': 'He gives his card.'}, {'s': 'The front rows are sold out.', 'ans': True, 'why': 'The text says they are sold out.'}, {'s': 'Cory goes to the movie alone.', 'ans': False, 'why': 'He goes with his sister.'}],
  'order': ['Cory goes to the theater.', 'He asks for two tickets.', 'Carlos says the price.', 'Cory pays with his card.', 'The movie starts.'],
  'ctx': [{'sent': 'The front rows are sold out.', 'w': 'sold out', 'opts': ['no tickets are left', 'tickets are free', 'tickets are old'], 'ans': 0, 'why': 'Sold out = no more tickets.'}, {'sent': 'The lights go dark.', 'w': 'dark', 'opts': ['without light', 'very bright', 'very hot'], 'ans': 0, 'why': 'Dark = no light.'}, {'sent': 'People return old tapes.', 'w': 'return', 'opts': ['give back', 'throw away', 'buy'], 'ans': 0, 'why': 'Return = give back.'}],
  'chunkHunt': ['Two tickets for the seven o’clock movie.', 'Where do you want to sit?', 'Here’s my card.', 'Where can I buy popcorn?'],
  'think': 'Where do you like to sit in a movie theater: front, middle or back?'},
 'convo': {'npc': {'name': 'Carlos'}, 'story': 'You are at a movie theater in Portland. Carlos works at the ticket window. Buy your tickets.', 'turns': [
  {'npc': 'Hi! Can I help you?', 'pt': 'Oi! Posso ajudar?', 'opts': [
   {'en': 'Hi! Two tickets for the seven o’clock movie.', 'pt': 'Oi! Dois ingressos para o filme das sete.', 'ok': True, 'fb': 'Clear request: number + time.'},
   {'en': 'Hi! I help two tickets.', 'pt': 'Oi! Eu ajudo dois ingressos.', 'ok': False, 'fb': 'You ask for tickets, you do not help them.'},
   {'en': 'Which movie?', 'pt': 'Qual filme?', 'ok': False, 'fb': 'That is the seller’s question.'}]},
  {'npc': 'Which movie?', 'pt': 'Qual filme?', 'opts': [
   {'en': 'Seven o’clock, please.', 'pt': 'Às sete, por favor.', 'ok': False, 'fb': 'You said the time. He asks which movie.'},
   {'en': 'The new comedy, please.', 'pt': 'A nova comédia, por favor.', 'ok': True, 'fb': 'Names the movie.'},
   {'en': 'Two tickets, thanks.', 'pt': 'Dois ingressos, obrigado.', 'ok': False, 'fb': 'You already said that.'}]},
  {'npc': 'Okay. Where do you want to sit?', 'pt': 'Ok. Onde quer sentar?', 'opts': [
   {'en': 'Twelve dollars each.', 'pt': 'Doze dólares cada.', 'ok': False, 'fb': 'The seller says the price.'},
   {'en': 'Yes, I want to sit.', 'pt': 'Sim, eu quero sentar.', 'ok': False, 'fb': 'He asks where, not if.'},
   {'en': 'In the middle, not too close.', 'pt': 'No meio, não muito perto.', 'ok': True, 'fb': 'Says the place.'}]},
  {'npc': 'Those seats are twelve dollars each.', 'pt': 'Esses lugares são doze dólares cada.', 'opts': [
   {'en': 'Here’s my card.', 'pt': 'Aqui está meu cartão.', 'ok': True, 'fb': 'Natural way to pay.'},
   {'en': 'I am twelve dollars.', 'pt': 'Eu sou doze dólares.', 'ok': False, 'fb': 'Does not make sense.'},
   {'en': 'Which movie?', 'pt': 'Qual filme?', 'ok': False, 'fb': 'Already answered.'}]},
  {'npc': 'Thanks. Theater number five.', 'pt': 'Obrigado. Sala número cinco.', 'opts': [
   {'en': 'Here’s my card.', 'pt': 'Aqui está meu cartão.', 'ok': False, 'fb': 'You already paid.'},
   {'en': 'Where can I buy popcorn?', 'pt': 'Onde posso comprar pipoca?', 'ok': True, 'fb': 'Natural next question.'},
   {'en': 'Where can I buy theater?', 'pt': 'Onde posso comprar sala?', 'ok': False, 'fb': 'Does not fit.'}]}]},
 'errors': [
  {'wrong': 'Two ticket for seven hours.', 'fix': 'Two tickets for seven o’clock.', 'alt': 'Two tickets to seven hours.', 'why': 'Use the plural tickets and o’clock for the time.'},
  {'wrong': 'I want sit in the middle.', 'fix': 'I want to sit in the middle.', 'alt': 'I want sitting in the middle.', 'why': 'After want, use to + verb.'},
  {'wrong': 'Where I can buy popcorn?', 'fix': 'Where can I buy popcorn?', 'alt': 'Where I buy popcorn can?', 'why': 'In questions: Where + can + I.'},
  {'wrong': 'Twelve dollars for each.', 'fix': 'Twelve dollars each.', 'alt': 'Twelve dollar each.', 'why': 'Say each at the end, with dollars in plural.'}],
 'homework': 'Write a short dialogue: you buy three tickets for the nine o’clock movie.',
 'homework_items': ['Write the movie, time and number of tickets.', 'Say aloud: Two tickets, please.', 'Listen to the dialogue and shadow Carlos.', 'Review: front / middle / back.']}
