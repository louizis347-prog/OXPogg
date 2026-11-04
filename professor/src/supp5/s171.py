"""Suplemento Quest v5 · aula 171: Booking a table + regular Happy birthday! (The Birthday Party)."""
SUPP = {
 'reg': 221,
 'badge': {'icon': '📅', 'name': 'Table Booked', 'desc': 'Book a table: people, day, time and seats'},
 'culture': {
  'hook': 'In the USA, many restaurants take reservations by phone or online. A short call is enough: say how many people, the day and the time, and your name.',
  'mythfact': [
   {'s': 'In many US restaurants, you can book a table by phone.', 'ans': True, 'why': 'Many places also take bookings on their website or in an app.'},
   {'s': 'Every restaurant in the USA needs a reservation.', 'ans': False, 'why': 'Many places welcome walk-ins, but busy places on weekends can be full.'},
   {'s': 'Restaurants usually ask for your name when you book.', 'ans': True, 'why': 'They write the name next to the table, and they call it when you arrive.'},
   {'s': 'If you arrive very late, your table is always waiting.', 'ans': False, 'why': 'Many restaurants give the table to other people after some minutes. Call if you are late.'},
   {'s': '“The Birthday Party” is a play by Harold Pinter.', 'ans': True, 'why': 'It was first staged in 1958.'}],
  'wild': [
   {'kind': 'Sign on a restaurant door', 'lines': ['**Reservations welcome**', 'Walk-ins welcome', 'Patio open 5 p.m. – 10 p.m.'], 'decode': {'q': 'Can you come without a reservation?', 'opts': ['Yes, walk-ins are welcome', 'No, never', 'Only at lunch'], 'ans': 0, 'why': '“Walk-ins welcome” means you can come without a booking.'}},
   {'kind': 'Text message from a restaurant', 'lines': ['Your table for **4** is booked.', 'Saturday, 7:30 p.m.', 'Reply C to cancel.'], 'decode': {'q': 'How many people is the table for?', 'opts': ['Four', 'Seven', 'Thirty'], 'ans': 0, 'why': '“Table for 4” means four people.'}}],
  'compare': {'br': 'In Brazil, many people just go to the restaurant and wait for a table, and the group often arrives late.', 'us': 'In the USA, a busy restaurant on Friday or Saturday night can be full. A booking helps, and many places wait only a short time for late guests.', 'tip': 'Say: “A table for four at seven thirty, please.”', 'ask': 'Do you book a table when you go out with friends? Say it in English.'},
  'quiz': [
   {'q': 'The restaurant asks, “For how many people?” You say…', 'opts': ['Four people.', 'Four o’clock.', 'For Saturday.'], 'ans': 0, 'why': 'The question is about the number of people.'},
   {'q': 'You want a table outside. You ask…', 'opts': ['Can we sit outside?', 'Can we outside sit?', 'We can sit to outside?'], 'ans': 0, 'why': 'Can we + verb: Can we sit outside?'},
   {'q': '“Fully booked” means…', 'opts': ['no tables are free', 'the food is free', 'the restaurant is closed forever'], 'ans': 0, 'why': 'All the tables are already taken.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'A table for Leo’s birthday',
  'text': [
   'Alma lives in **Miami**. On Saturday, it is her friend Leo’s birthday. She wants a nice dinner for four people, so she calls Bella’s Kitchen.',
   '“**Hi. I’d like to make a reservation**,” Alma says. “**Sure. For how many people?**” Cole asks. “**Four people.**” “**What day and time?**” “**Saturday at seven thirty.**”',
   'Cole looks at the book. “**Let me check. Yes, we have a table.**” Alma smiles. “**Great. Can we sit outside?**” “**Yes, on the patio.**” The patio is nice, and there are candles on the tables. Alma says thank you and writes the time in her phone.',
   'That night, Alma thinks about “The Birthday Party,” a play by Harold Pinter from 1958. In the play, a strange birthday party happens in a small house by the sea. Alma laughs. Leo’s birthday is happier! At Bella’s Kitchen, the answer is not “**Booked solid**.” The restaurant has a table, and she is lucky!',
   'At a real birthday, friends bring a gift and a card. Everyone sings “**Happy birthday to you!**” The cake comes with a candle, and Leo makes a wish. His party is small. It is four friends, one table and one cake. Alma thinks it is a perfect plan.'],
  'glossary': [{'w': 'birthday', 'pt': 'aniversário'}, {'w': 'dinner', 'pt': 'jantar'}, {'w': 'reservation', 'pt': 'reserva'}, {'w': 'patio', 'pt': 'pátio, área externa'}, {'w': 'candles', 'pt': 'velas'}, {'w': 'gift', 'pt': 'presente'}, {'w': 'cake', 'pt': 'bolo'}, {'w': 'play', 'pt': 'peça de teatro'}, {'w': 'lucky', 'pt': 'com sorte'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A woman books a table for a birthday dinner', 'A man cooks dinner at home', 'A girl buys a movie ticket'], 'ans': 0, 'why': 'Alma books a table at Bella’s Kitchen for Leo’s birthday.'},
  'scan': [{'q': 'How many people is the table for?', 'ans': 'four', 'alt': ['4', 'four people']}, {'q': 'What day is the dinner?', 'ans': 'Saturday', 'alt': ['saturday']}, {'q': 'Where do they sit?', 'ans': 'on the patio', 'alt': ['patio', 'outside']}],
  'tf': [{'s': 'Alma calls the restaurant.', 'ans': True, 'why': 'She calls Bella’s Kitchen.'}, {'s': 'The dinner is on Friday.', 'ans': False, 'why': 'It is on Saturday at seven thirty.'}, {'s': 'The restaurant has a table.', 'ans': True, 'why': 'Cole says, “Yes, we have a table.”'}, {'s': 'Leo’s party is big.', 'ans': False, 'why': 'It is four friends, one table and one cake.'}],
  'order': ['Alma calls the restaurant.', 'Cole asks for how many people.', 'Alma says Saturday at seven thirty.', 'Cole says there is a table.', 'Alma asks for the patio.'],
  'ctx': [{'sent': 'Friends bring a gift.', 'w': 'gift', 'opts': ['a present', 'a plate', 'a chair'], 'ans': 0, 'why': 'A gift is a present.'}, {'sent': 'There are candles on the tables.', 'w': 'candles', 'opts': ['small lights with fire', 'plates for food', 'chairs'], 'ans': 0, 'why': 'A candle gives a small light.'}, {'sent': 'Alma sees a play.', 'w': 'play', 'opts': ['a show on a stage', 'a kind of food', 'a car'], 'ans': 0, 'why': 'A play is a theater show.'}],
  'chunkHunt': ['I’d like to make a reservation.', 'For how many people?', 'Can we sit outside?', 'Happy birthday to you!'],
  'think': 'Do you book a table when you go out for a special dinner? Why or why not?'},
 'convo': {'npc': {'name': 'Cole'}, 'story': 'You call Bella’s Kitchen in Miami to book a table. Cole answers the phone.', 'turns': [
  {'npc': 'Good evening, Bella’s Kitchen.', 'pt': 'Boa noite, Bella’s Kitchen.', 'opts': [
   {'en': 'Hi. I’d like to make a reservation.', 'pt': 'Oi. Gostaria de fazer uma reserva.', 'ok': True, 'fb': 'Natural way to start the call.'},
   {'en': 'Hi. I make a reservation.', 'pt': 'Oi. Eu faço uma reserva.', 'ok': False, 'fb': 'Say I’d like to make…'},
   {'en': 'Good evening, I am hungry table.', 'pt': 'Boa noite, eu sou mesa com fome.', 'ok': False, 'fb': 'Does not make sense.'}]},
  {'npc': 'Sure. For how many people?', 'pt': 'Claro. Para quantas pessoas?', 'opts': [
   {'en': 'For Saturday.', 'pt': 'Para sábado.', 'ok': False, 'fb': 'He asks about the number of people.'},
   {'en': 'Four people.', 'pt': 'Quatro pessoas.', 'ok': True, 'fb': 'Short and clear.'},
   {'en': 'We are four peoples.', 'pt': 'Somos quatro povos.', 'ok': False, 'fb': 'People is already plural.'}]},
  {'npc': 'What day and time?', 'pt': 'Que dia e horário?', 'opts': [
   {'en': 'Saturday at seven thirty.', 'pt': 'Sábado às sete e meia.', 'ok': True, 'fb': 'Day + at + time.'},
   {'en': 'Saturday in seven thirty.', 'pt': 'Sábado em sete e meia.', 'ok': False, 'fb': 'Use at with a time.'},
   {'en': 'Four people.', 'pt': 'Quatro pessoas.', 'ok': False, 'fb': 'You said that already.'}]},
  {'npc': 'Let me check. Yes, we have a table.', 'pt': 'Vou ver. Sim, temos uma mesa.', 'opts': [
   {'en': 'You are welcome.', 'pt': 'De nada.', 'ok': False, 'fb': 'Not a reply to good news.'},
   {'en': 'Can we outside sit?', 'pt': 'Podemos fora sentar?', 'ok': False, 'fb': 'Order: Can we sit outside?'},
   {'en': 'Great. Can we sit outside?', 'pt': 'Ótimo. Podemos ficar do lado de fora?', 'ok': True, 'fb': 'Polite request.'}]},
  {'npc': 'Yes, on the patio.', 'pt': 'Sim, no pátio.', 'opts': [
   {'en': 'That sounds good. Thank you!', 'pt': 'Parece bom. Obrigado!', 'ok': True, 'fb': 'Natural way to end the call.'},
   {'en': 'No, I am sorry.', 'pt': 'Não, sinto muito.', 'ok': False, 'fb': 'He said yes.'},
   {'en': 'Good evening again.', 'pt': 'Boa noite de novo.', 'ok': False, 'fb': 'Too late for a greeting.'}]}]},
 'errors': [
  {'wrong': 'I want a reservation for four persons.', 'fix': 'I’d like a reservation for four people.', 'alt': 'I would like reservation for four.', 'why': 'Use people, not persons, and I’d like is polite.'},
  {'wrong': 'Saturday in seven thirty.', 'fix': 'Saturday at seven thirty.', 'alt': 'Saturday on seven thirty.', 'why': 'Use at with a time.'},
  {'wrong': 'Can we sit in the outside?', 'fix': 'Can we sit outside?', 'alt': 'Can we sit to outside?', 'why': 'Outside has no the or in here.'},
  {'wrong': 'We are four people table.', 'fix': 'A table for four, please.', 'alt': 'A table of four people, please.', 'why': 'Say table for + number.'}],
 'homework': 'Write a short call: you book a table for three people on Friday at eight.',
 'homework_items': ['Write the day and time you want a table.', 'Say aloud: A table for four, please.', 'Listen to the dialogue and shadow Cole.', 'Review: at seven / at seven thirty / at eight.']}
