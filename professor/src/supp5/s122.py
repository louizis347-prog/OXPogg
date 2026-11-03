"""Suplemento Quest v5 · aula 122: End of the work week + regular And, But, Or (Peppa Pig)."""
SUPP = {
 'reg': 40,
 'badge': {'icon': '🎉', 'name': 'Friday Mood', 'desc': 'Talk about your week and make Friday plans'},
 'culture': {
  'hook': 'In the USA, Friday is the happy day of the work week. Coworkers often ask about your week and your plans, and some invite you to dinner or drinks.',
  'mythfact': [
   {'s': 'Many US workers say “TGIF” on Friday.', 'ans': True, 'why': 'TGIF means “Thank God it’s Friday”, a common and friendly phrase.'},
   {'s': 'In the USA, most people work on Saturday and rest on Wednesday.', 'ans': False, 'why': 'The usual work week is Monday to Friday, and the weekend is Saturday and Sunday.'},
   {'s': 'It is polite to ask a coworker, “How was your week?”', 'ans': True, 'why': 'It is a common small-talk question on Friday.'},
   {'s': 'Restaurants are often busy on Friday night, so a reservation can help.', 'ans': True, 'why': 'Many people go out on Friday, and popular places can be full.'},
   {'s': 'Peppa Pig is a British children’s TV series.', 'ans': True, 'why': 'It started in 2004 in the UK.'}],
  'wild': [
   {'kind': 'Text message', 'lines': ['TGIF! Dinner tonight?', 'The **Italian place** at **7:30**?', 'I’ll make a **reservation**.'], 'decode': {'q': 'What time is dinner?', 'opts': ['7:30', '7:00', '8:30'], 'ans': 0, 'why': 'The message says 7:30.'}},
   {'kind': 'Sign at a restaurant', 'lines': ['**Friday night**: no walk-ins after 7:00.', 'Please call for a **reservation**.'], 'decode': {'q': 'What should you do for Friday night?', 'opts': ['Call for a reservation', 'Come at 9:00', 'Bring food'], 'ans': 0, 'why': 'The sign asks you to call for a reservation.'}}],
  'compare': {'br': 'In Brazil, “sextou!” is a happy Friday word, and friends often meet for a happy hour, a churrasco or a pizza.', 'us': 'In the USA, “TGIF” is similar. Coworkers may go out for dinner or drinks, and everyone pays for their own part unless someone says “It’s on me”.', 'tip': 'If you say “I’m busy, but thanks!”, it is a polite no.', 'ask': 'What do you do on Friday night? Say it in English.'},
  'quiz': [
   {'q': 'A coworker asks, “How was your week?” You say…', 'opts': ['It was busy, but good.', 'It is Friday week.', 'I have week.'], 'ans': 0, 'why': 'Use was for a finished week, and add a short opinion.'},
   {'q': 'You want to ask for a plan. You say…', 'opts': ['What are your plans?', 'What is your plan week?', 'Where plans are you?'], 'ans': 0, 'why': 'What are your plans? is the natural question.'},
   {'q': 'What does “Drinks on me!” mean?', 'opts': ['I will pay for the drinks.', 'I want a drink now.', 'Drinks are on the table.'], 'ans': 0, 'why': 'On me = I pay.'}]},
 'reading': {
  'genre': 'Email',
  'title': 'Friday plans',
  'text': [
   'Hi Mia, **TGIF!** I am in my office in **Philadelphia**, and the work week is almost over. I want to tell you about my day.',
   'My **week** was **busy**, **but good**. On Monday, I had a long meeting. On Tuesday and Wednesday, I wrote many reports. On Thursday, my computer was slow, and I was angry. Today, I am happy.',
   'At three o’clock, my coworker Leo asked, “**What are your plans?**” I said, “**I’m going to relax at home.**” Then he asked, “**Do you want to get dinner tonight?**” I said, “**Sure! Where?**”',
   'Leo wants to go to the Italian place, **and** I love Italian food. He said, “**At seven thirty.**” I like pasta **or** pizza, but I am not hungry yet. I need a big **break** and a good dinner.',
   'On Friday nights, the place is full, so Leo is going to call for a **reservation**. After work, I am going to walk home and take a short nap. Then I am going to put on a nice shirt.',
   'Do you want to join us? Come at seven thirty! **Let’s celebrate** the end of the week. Cheers! — Vera'],
  'glossary': [{'w': 'week', 'pt': 'semana'}, {'w': 'busy', 'pt': 'ocupado, corrido'}, {'w': 'reports', 'pt': 'relatórios'}, {'w': 'coworker', 'pt': 'colega de trabalho'}, {'w': 'plans', 'pt': 'planos'}, {'w': 'relax', 'pt': 'relaxar'}, {'w': 'break', 'pt': 'pausa, descanso'}, {'w': 'reservation', 'pt': 'reserva'}, {'w': 'nap', 'pt': 'soneca'}, {'w': 'join', 'pt': 'juntar-se'}],
  'fast': {'q': 'What is this text about?', 'opts': ['Plans for a Friday dinner', 'A job interview', 'A trip to the beach'], 'ans': 0, 'why': 'Vera writes about Friday and a dinner with Leo.'},
  'scan': [{'q': 'What kind of restaurant do they choose?', 'ans': 'Italian', 'alt': ['the italian place', 'italian place']}, {'q': 'What time is dinner?', 'ans': 'seven thirty', 'alt': ['7:30', '7.30', 'half past seven']}, {'q': 'Who is going to call the restaurant?', 'ans': 'Leo', 'alt': ['leo']}],
  'tf': [
   {'s': 'Vera’s week was easy and slow.', 'ans': False, 'why': 'She says her week was busy.'},
   {'s': 'Vera is going to relax at home.', 'ans': True, 'why': 'She says, “I’m going to relax at home.”'},
   {'s': 'Leo wants to eat Chinese food.', 'ans': False, 'why': 'He wants the Italian place.'},
   {'s': 'Dinner is at seven thirty.', 'ans': True, 'why': 'Leo says, “At seven thirty.”'}],
  'order': ['Vera has a busy week.', 'Leo asks about her plans.', 'Leo invites her to dinner.', 'They choose the Italian place.', 'Leo is going to call for a reservation.'],
  'ctx': [
   {'sent': 'The week was busy, but good.', 'w': 'busy', 'opts': ['full of work', 'very quiet', 'cold'], 'ans': 0, 'why': 'Busy = with a lot to do.'},
   {'sent': 'I need a break.', 'w': 'break', 'opts': ['a short rest', 'a new job', 'a big meal'], 'ans': 0, 'why': 'Break = a short rest.'},
   {'sent': 'Leo is going to call for a reservation.', 'w': 'reservation', 'opts': ['a table saved for you', 'a bill', 'a menu'], 'ans': 0, 'why': 'A reservation saves a table.'}],
  'chunkHunt': ['What are your plans?', 'I’m going to relax at home.', 'Do you want to get dinner tonight?', 'At seven thirty.'],
  'think': 'What do you usually do on Friday night? Write two sentences.'},
 'convo': {'npc': {'name': 'Leo'}, 'story': 'It is Friday afternoon at work in Philadelphia. Your coworker Leo wants to talk about the week and the night.', 'turns': [
  {'npc': 'It’s Friday! How was your week?', 'pt': 'É sexta! Como foi sua semana?', 'opts': [
   {'en': 'I have a week.', 'pt': 'Eu tenho uma semana.', 'ok': False, 'fb': 'Use was to talk about a week that is over.'},
   {'en': 'It was busy, but good. And yours?', 'pt': 'Foi corrida, mas boa. E a sua?', 'ok': True, 'fb': 'Answer and ask back with And yours?'},
   {'en': 'It is Friday.', 'pt': 'É sexta.', 'ok': False, 'fb': 'He already said that.'}]},
  {'npc': 'Same here. What are your plans?', 'pt': 'Igual. Quais são seus planos?', 'opts': [
   {'en': 'I’m going to relax at home.', 'pt': 'Vou relaxar em casa.', 'ok': True, 'fb': 'Going to + verb talks about plans.'},
   {'en': 'I relaxed home.', 'pt': 'Eu relaxei casa.', 'ok': False, 'fb': 'You need going to and at home.'},
   {'en': 'My plans are Monday.', 'pt': 'Meus planos são segunda.', 'ok': False, 'fb': 'It does not say what you will do.'}]},
  {'npc': 'Do you want to get dinner tonight?', 'pt': 'Quer jantar hoje à noite?', 'opts': [
   {'en': 'No, thanks, I have dinner.', 'pt': 'Não, obrigado, eu tenho jantar.', 'ok': False, 'fb': 'Sounds strange. Say: Sorry, I’m busy.'},
   {'en': 'Yes, I am.', 'pt': 'Sim, eu sou.', 'ok': False, 'fb': 'The question starts with Do you want.'},
   {'en': 'Sure! Where?', 'pt': 'Claro! Onde?', 'ok': True, 'fb': 'Accept and ask for the place.'}]},
  {'npc': 'How about the Italian place?', 'pt': 'Que tal o italiano?', 'opts': [
   {'en': 'Great. What time?', 'pt': 'Ótimo. Que horas?', 'ok': True, 'fb': 'Agree and ask the time.'},
   {'en': 'Great. Which hour is?', 'pt': 'Ótimo. Que hora é?', 'ok': False, 'fb': 'Say What time?'},
   {'en': 'Italian is Brazil?', 'pt': 'Italiano é Brasil?', 'ok': False, 'fb': 'Not a natural answer.'}]},
  {'npc': 'At seven thirty. See you there!', 'pt': 'Às sete e meia. Até lá!', 'opts': [
   {'en': 'Good morning!', 'pt': 'Bom dia!', 'ok': False, 'fb': 'It is the afternoon and you are saying goodbye.'},
   {'en': 'I am seven thirty.', 'pt': 'Eu sou sete e meia.', 'ok': False, 'fb': 'Not a way to confirm time.'},
   {'en': 'Sounds good. See you at seven thirty!', 'pt': 'Combinado. Até as sete e meia!', 'ok': True, 'fb': 'Confirm the plan and say goodbye.'}]}]},
 'homework': 'Write a short message to a friend: say how your week was and invite him or her to dinner. Then read it aloud.',
 'homework_items': ['Say: It was busy, but good.', 'Write 3 plans for this weekend with I’m going to.', 'Listen to the dialogue and repeat each line.', 'Review: What are your plans? / What time? / Sounds good.'],
 'errors': [
  {'wrong': 'I go to relax at home.', 'fix': 'I’m going to relax at home.', 'alt': 'I going to relax at home.', 'why': 'For plans, use am/is/are + going to + verb.'},
  {'wrong': 'Do you want get dinner?', 'fix': 'Do you want to get dinner?', 'alt': 'Do you wanting to get dinner?', 'why': 'After want, use to + verb.'},
  {'wrong': 'My week is busy yesterday.', 'fix': 'My week was busy.', 'alt': 'My week were busy.', 'why': 'For a past week, use was.'},
  {'wrong': 'At the seven thirty.', 'fix': 'At seven thirty.', 'alt': 'In seven thirty.', 'why': 'Use at for clock time, with no the.'}],
}
