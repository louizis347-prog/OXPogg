"""Suplemento Quest v5 · aula 124: Make an appointment + regular Come back at five (Back to the Future)."""
SUPP = {
 'reg': 147,
 'badge': {'icon': '📅', 'name': 'Appointment Pro', 'desc': 'Call an office and book a time in English'},
 'culture': {
  'hook': 'In the USA, you usually call or use a website to make an appointment before you see a doctor. The office asks for your name, your birthday and a good day and time.',
  'mythfact': [
   {'s': 'In the USA, you often need an appointment to see a regular doctor.', 'ans': True, 'why': 'Most offices work by appointment, except urgent care places.'},
   {'s': 'The office may ask you to spell your last name.', 'ans': True, 'why': 'Spelling letter by letter avoids mistakes.'},
   {'s': 'You never need to show an ID or insurance card.', 'ans': False, 'why': 'Many offices ask for your photo ID and insurance card at the first visit.'},
   {'s': 'It is polite to arrive a little early for an appointment.', 'ans': True, 'why': 'Many offices ask you to come 10 or 15 minutes early to fill out forms.'},
   {'s': '“Back to the Future” is a film about time travel.', 'ans': True, 'why': 'Marty McFly travels in a car that goes through time.'}],
  'wild': [
   {'kind': 'Reminder text', 'lines': ['Reminder: you have an **appointment** with **Dr. Rivera**.', 'Tuesday at **2:00 PM**.', 'Reply C to confirm or R to change.'], 'decode': {'q': 'What do you send to confirm?', 'opts': ['C', 'R', 'Tuesday'], 'ans': 0, 'why': 'The message says reply C to confirm.'}},
   {'kind': 'Sign at the front desk', 'lines': ['Please bring your **ID** and your **insurance** card.', 'Arrive 15 minutes **early**.'], 'decode': {'q': 'When should you arrive?', 'opts': ['15 minutes early', '15 minutes late', 'At night'], 'ans': 0, 'why': 'The sign says arrive 15 minutes early.'}}],
  'compare': {'br': 'In Brazil, many people call, use WhatsApp or an app, and sometimes go to the clinic early to get a number.', 'us': 'In the USA, most offices ask you to call or book online. They ask for your name, spelling and insurance.', 'tip': 'Say the day and the time slowly, and repeat them at the end: “Tuesday at two. Thank you.”', 'ask': 'How do you spell your last name in English? Say the letters.'},
  'quiz': [
   {'q': 'You want to book a visit. You say…', 'opts': ['I’d like to make an appointment.', 'I want appointment doctor.', 'I make a doctor.'], 'ans': 0, 'why': 'I’d like to make an appointment is polite and clear.'},
   {'q': 'The office asks, “How do you spell your last name?” You…', 'opts': ['Say the letters: S-I-L-V-A.', 'Say it faster.', 'Say yes.'], 'ans': 0, 'why': 'Say each letter slowly.'},
   {'q': 'They say, “Ten or two?” and you like ten. You say…', 'opts': ['Ten o’clock works for me.', 'I am ten o’clock.', 'Two is not ten.'], 'ans': 0, 'why': 'Works for me means the time is good for you.'}]},
 'reading': {
  'genre': 'Blog post',
  'title': 'My first call to the doctor’s office',
  'text': [
   'Last week I needed to see a doctor in **Orlando**. I was nervous, because I had to make a phone call in English. I took a pen, a paper and my **insurance** card.',
   'A man answered: “Good morning, **Dr. Rivera’s office**.” I said, “Hi. **I’d like to make an appointment**.” He said, “Sure. **What’s your name?**” I said, “It’s Alex Silva.”',
   'Then he asked, “**How do you spell your last name?**” I said slowly, “**S-I-L-V-A**.” He repeated it. I was happy because he understood me.',
   'He asked, “**When can you come?**” I said, “**Do you have time on Tuesday?**” He answered, “We have **ten o’clock** or **two o’clock**.” I like to go **early**, so I said, “Ten o’clock **works for me**.”',
   'He said, “Great. Please bring your **ID** and your insurance card. Come ten minutes early.” I wrote it all on the paper. At the end he said, “**You’re all set**.”',
   'The call was only three minutes long. Now I know the steps: say what you want, give your name, spell it and choose a time. Next time I am going to call a little faster!'],
  'glossary': [{'w': 'appointment', 'pt': 'consulta, horário marcado'}, {'w': 'insurance', 'pt': 'seguro (saúde)'}, {'w': 'office', 'pt': 'consultório, escritório'}, {'w': 'last name', 'pt': 'sobrenome'}, {'w': 'spell', 'pt': 'soletrar'}, {'w': 'slowly', 'pt': 'devagar'}, {'w': 'early', 'pt': 'cedo'}, {'w': 'ID', 'pt': 'documento de identidade'}, {'w': 'steps', 'pt': 'passos'}, {'w': 'repeated', 'pt': 'repetiu'}],
  'fast': {'q': 'What is this text about?', 'opts': ['A call to make a doctor’s appointment', 'A trip to the airport', 'A cooking class'], 'ans': 0, 'why': 'Alex calls Dr. Rivera’s office to book a visit.'},
  'scan': [{'q': 'What is the doctor’s name?', 'ans': 'Dr. Rivera', 'alt': ['rivera']}, {'q': 'What day does Alex choose?', 'ans': 'Tuesday', 'alt': ['tuesday']}, {'q': 'What time does Alex choose?', 'ans': 'ten o’clock', 'alt': ['10', '10:00', 'ten']}],
  'tf': [
   {'s': 'Alex is nervous before the call.', 'ans': True, 'why': 'He says he was nervous.'},
   {'s': 'Alex spells his first name.', 'ans': False, 'why': 'He spells his last name: S-I-L-V-A.'},
   {'s': 'The office offers ten o’clock or two o’clock.', 'ans': True, 'why': 'The man says, “We have ten o’clock or two o’clock.”'},
   {'s': 'The call is thirty minutes long.', 'ans': False, 'why': 'It was only three minutes long.'}],
  'order': ['Alex calls Dr. Rivera’s office.', 'He says he wants an appointment.', 'He spells his last name.', 'He chooses Tuesday at ten.', 'The man says, “You’re all set.”'],
  'ctx': [
   {'sent': 'I like to go early.', 'w': 'early', 'opts': ['before the time', 'after the time', 'with friends'], 'ans': 0, 'why': 'Early = before the expected time.'},
   {'sent': 'Ten o’clock works for me.', 'w': 'works for me', 'opts': ['is good for me', 'is far from me', 'is hard for me'], 'ans': 0, 'why': 'Works for me = it suits me.'},
   {'sent': 'Please bring your ID.', 'w': 'ID', 'opts': ['a card with your name and photo', 'a type of food', 'a phone number'], 'ans': 0, 'why': 'ID = identification, like a passport or license.'}],
  'chunkHunt': ['I’d like to make an appointment.', 'How do you spell your last name?', 'Do you have time on Tuesday?', 'Works for me.'],
  'think': 'What do you need to say when you call an office to book a time? Write the steps.'},
 'convo': {'npc': {'name': 'Darius'}, 'story': 'You call Dr. Rivera’s office in Orlando. Darius answers the phone. Make an appointment.', 'turns': [
  {'npc': 'Good morning, Dr. Rivera’s office.', 'pt': 'Bom dia, consultório do Dr. Rivera.', 'opts': [
   {'en': 'Hi. I’d like to make an appointment.', 'pt': 'Oi. Gostaria de marcar uma consulta.', 'ok': True, 'fb': 'Say hello and why you call.'},
   {'en': 'Hi. I make you appointment.', 'pt': 'Oi. Eu faço você consulta.', 'ok': False, 'fb': 'Use I’d like to make an appointment.'},
   {'en': 'Hello, I’m a doctor.', 'pt': 'Olá, sou médico.', 'ok': False, 'fb': 'Wrong role: you are the patient.'}]},
  {'npc': 'Sure. What’s your name?', 'pt': 'Claro. Qual é seu nome?', 'opts': [
   {'en': 'My name Alex.', 'pt': 'Meu nome Alex.', 'ok': False, 'fb': 'Add is: My name is Alex.'},
   {'en': 'It’s Alex Silva.', 'pt': 'É Alex Silva.', 'ok': True, 'fb': 'Short and clear.'},
   {'en': 'Yes, thank you.', 'pt': 'Sim, obrigado.', 'ok': False, 'fb': 'It does not answer What’s your name?'}]},
  {'npc': 'How do you spell your last name?', 'pt': 'Como se escreve seu sobrenome?', 'opts': [
   {'en': 'S-I-L-V-A.', 'pt': 'S-I-L-V-A.', 'ok': True, 'fb': 'Say each letter slowly.'},
   {'en': 'It is Brazilian.', 'pt': 'É brasileiro.', 'ok': False, 'fb': 'It does not spell the name.'},
   {'en': 'I am Silva.', 'pt': 'Eu sou Silva.', 'ok': False, 'fb': 'He asks for letters, not for the name again.'}]},
  {'npc': 'When can you come?', 'pt': 'Quando você pode vir?', 'opts': [
   {'en': 'I come to Orlando.', 'pt': 'Eu venho a Orlando.', 'ok': False, 'fb': 'He asks for a day and time.'},
   {'en': 'Do you have time on Tuesday?', 'pt': 'Vocês têm horário na terça?', 'ok': True, 'fb': 'Ask for a day.'},
   {'en': 'I can yesterday.', 'pt': 'Eu posso ontem.', 'ok': False, 'fb': 'You cannot book the past.'}]},
  {'npc': 'We have ten o’clock or two o’clock.', 'pt': 'Temos às dez ou às duas.', 'opts': [
   {'en': 'Ten o’clock works for me. Thank you!', 'pt': 'Às dez serve pra mim. Obrigado!', 'ok': True, 'fb': 'Choose one time and thank him.'},
   {'en': 'Ten or two, yes.', 'pt': 'Dez ou duas, sim.', 'ok': False, 'fb': 'You must choose one.'},
   {'en': 'Two o’clock is morning.', 'pt': 'Duas horas é manhã.', 'ok': False, 'fb': 'Two o’clock is in the afternoon.'}]}]},
 'homework': 'Prepare and say a 30-second phone call: make an appointment, give your name and spell it, and choose a day.',
 'homework_items': ['Say the English alphabet slowly.', 'Spell your first and last name aloud.', 'Listen to the dialogue and repeat each line.', 'Review: I’d like to make an appointment / Works for me / You’re all set.'],
 'errors': [
  {'wrong': 'I want a appointment.', 'fix': 'I’d like to make an appointment.', 'alt': 'I want make appointment.', 'why': 'Use I’d like to make an appointment; before a vowel sound, say an.'},
  {'wrong': 'How you spell your name?', 'fix': 'How do you spell your name?', 'alt': 'How spell you your name?', 'why': 'Questions need do before you.'},
  {'wrong': 'Do you have time in Tuesday?', 'fix': 'Do you have time on Tuesday?', 'alt': 'Do you have time at Tuesday?', 'why': 'Use on with days of the week.'},
  {'wrong': 'At ten hours.', 'fix': 'At ten o’clock.', 'alt': 'In ten o’clock.', 'why': 'Use at + o’clock for clock time.'}],
}
