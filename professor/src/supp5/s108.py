"""Suplemento Quest v5 · aula 108: What time is the meeting? + regular Early for the Meeting"""
SUPP = {'reg': 39, 'badge': {'icon': '📅', 'name': 'On-Time Pro', 'desc': 'Ask about time, place and length of a meeting in English'},
 'culture': {'hook': 'Being on time at work matters a lot in the USA. Learn to ask when and where a meeting is, how long it is and what to bring, so you arrive ready.',
  'mythfact': [
   {'s': 'In the USA the first floor is usually the ground floor.', 'ans': True, 'why': 'In American buildings “first floor” is normally the street level.'},
   {'s': 'Most people use a 24-hour clock at work.', 'ans': False, 'why': 'In daily life Americans use 12-hour time with a.m. and p.m.'},
   {'s': 'Many meetings start at the exact time.', 'ans': True, 'why': 'On time is often the same as a few minutes early.'},
   {'s': 'It is rude to ask what to bring to a meeting.', 'ans': False, 'why': 'It is a smart question, especially for a new person.'}],
  'wild': [
   {'kind': 'Calendar invite', 'lines': ['**Team Meeting**', 'Tuesday · 10:00–10:30 AM', 'Room 2 · Second floor', 'Bring: notebook and pen'], 'decode': {'q': 'How long is the meeting?', 'opts': ['30 minutes', 'One hour', '10 minutes'], 'ans': 0, 'why': 'From 10:00 to 10:30 is thirty minutes.'}},
   {'kind': 'Sign on a door', 'lines': ['**MEETING IN PROGRESS**', 'Please do not enter.', 'Back at 11:00'], 'decode': {'q': 'What should you do?', 'opts': ['Wait outside', 'Go in and sit', 'Knock loudly'], 'ans': 0, 'why': 'The sign says please do not enter.'}}],
  'compare': {'br': 'In Brazil people often say “térreo” for the ground floor and a meeting can start a little later.', 'us': 'In the USA the ground floor is usually called the first floor, and many meetings start right on time.', 'tip': 'Arrive five minutes early. It is usually seen as on time.', 'ask': 'Ask a coworker when the next meeting is. Say it in English.'},
  'quiz': [
   {'q': 'You want to know the time of a meeting. You ask…', 'opts': ['When is the meeting?', 'Where is the time?', 'What meeting is it?'], 'ans': 0, 'why': 'When is…? asks for the time.'},
   {'q': 'The answer is “It’s at ten o’clock.” That means…', 'opts': ['10:00', '1:00', '12:00'], 'ans': 0, 'why': 'Ten o’clock = 10:00.'},
   {'q': 'You want to know the length. You ask…', 'opts': ['How long is it?', 'How far is it?', 'How old is it?'], 'ans': 0, 'why': 'How long…? asks about time length.'}]},
 'reading': {'genre': 'Diary', 'title': 'My First Team Meeting',
  'text': ['Today is my first day at a new job. I am a little nervous. My boss says there is a team **meeting** this morning. I look at my **calendar**, but I do not see it.',
   'I ask a coworker, “**Excuse me, when is the team meeting?**” “**It’s at ten o’clock**,” she says. “**Where is it?**” I ask. “**In room two, on the second floor**,” she says.',
   'I ask, “**How long is it?**” “**About thirty minutes**,” she says. Then I ask, “**Do I need to bring anything?**” “**Just a pen and your notebook**,” she says. I write all this in my calendar.',
   'I want to be early. At nine forty I go upstairs. Room two is empty. A **projector** shows a picture on the wall. On the table there is an **agenda** with three items. I sit down and wait.',
   'Then the people come in. Everyone smiles. The boss begins at ten o’clock exactly. I open my notebook and write. After the meeting I ask, “What time is it now?” “Ten thirty,” says my coworker. I am happy: I was early, ready and on time.'],
  'glossary': [{'w': 'nervous', 'pt': 'nervoso'}, {'w': 'calendar', 'pt': 'agenda de datas'}, {'w': 'coworker', 'pt': 'colega de trabalho'}, {'w': 'floor', 'pt': 'andar'}, {'w': 'upstairs', 'pt': 'lá em cima'}, {'w': 'empty', 'pt': 'vazia'}, {'w': 'projector', 'pt': 'projetor'}, {'w': 'agenda', 'pt': 'pauta'}, {'w': 'exactly', 'pt': 'em ponto'}, {'w': 'ready', 'pt': 'pronto'}],
  'fast': {'q': 'What is this text about?', 'opts': ['A new worker asks about his first meeting', 'A trip to a museum', 'A party at home'], 'ans': 0, 'why': 'The writer asks about time, place and length of a meeting.'},
  'scan': [{'q': 'What time is the meeting?', 'ans': 'ten o’clock', 'alt': ['10', 'ten', '10:00', 'ten o\'clock']}, {'q': 'Which room is it?', 'ans': 'room two', 'alt': ['two', '2']}, {'q': 'What does he bring?', 'ans': 'a pen and a notebook', 'alt': ['pen and notebook', 'a pen and his notebook', 'notebook']}],
  'tf': [{'s': 'The meeting is on the second floor.', 'ans': True, 'why': '“In room two, on the second floor.”'}, {'s': 'The meeting is about one hour.', 'ans': False, 'why': 'It is about thirty minutes.'}, {'s': 'The writer arrives early.', 'ans': True, 'why': 'He goes upstairs at nine forty.'}, {'s': 'The room is full at nine forty.', 'ans': False, 'why': 'Room two is empty.'}],
  'order': ['The writer does not see the meeting in his calendar.', 'He asks a coworker about the time and place.', 'He goes upstairs early.', 'The boss begins at ten o’clock.', 'He asks what time it is now.'],
  'ctx': [{'sent': 'Room two is empty.', 'w': 'empty', 'opts': ['with nobody inside', 'very big', 'very cold'], 'ans': 0, 'why': 'Empty = nothing or nobody inside.'}, {'sent': 'The boss begins at ten o’clock exactly.', 'w': 'exactly', 'opts': ['at that precise time', 'a little late', 'maybe'], 'ans': 0, 'why': 'Exactly = precisely.'}, {'sent': 'I go upstairs at nine forty.', 'w': 'upstairs', 'opts': ['to a higher floor', 'outside', 'home'], 'ans': 0, 'why': 'Upstairs = to the floor above.'}],
  'chunkHunt': ['When is the team meeting?', 'It’s at ten o’clock.', 'How long is it?', 'Do I need to bring anything?'], 'think': 'What do you ask before a new meeting or class? Write three questions.'},
 'convo': {'npc': {'name': 'Evan'}, 'story': 'You are new at the office. Evan is a coworker who knows the team schedule.', 'turns': [
  {'npc': 'Hi! I’m Evan. Are you new here?', 'pt': 'Oi! Sou o Evan. Você é novo aqui?', 'opts': [
   {'en': 'The meeting is a new.', 'pt': 'A reunião é um novo.', 'ok': False, 'fb': 'It does not answer the question.'},
   {'en': 'Yes. Excuse me, when is the team meeting?', 'pt': 'Sou. Com licença, quando é a reunião da equipe?', 'ok': True, 'fb': 'Answer, then ask.'},
   {'en': 'Yes, I am at ten.', 'pt': 'Sim, eu estou às dez.', 'ok': False, 'fb': 'You do not say the time yet.'}]},
  {'npc': 'It’s at ten o’clock.', 'pt': 'É às dez horas.', 'opts': [
   {'en': 'I am in room two.', 'pt': 'Eu estou na sala dois.', 'ok': False, 'fb': 'You do not know the room yet.'},
   {'en': 'Where it is?', 'pt': 'Onde é?', 'ok': False, 'fb': 'Word order: Where is it?'},
   {'en': 'Where is it?', 'pt': 'Onde é?', 'ok': True, 'fb': 'Where is it? asks for the place.'}]},
  {'npc': 'In room two, on the second floor.', 'pt': 'Na sala dois, no segundo andar.', 'opts': [
   {'en': 'How long is it?', 'pt': 'Quanto tempo dura?', 'ok': True, 'fb': 'How long…? asks for the length.'},
   {'en': 'How much is it?', 'pt': 'Quanto custa?', 'ok': False, 'fb': 'How much asks about price.'},
   {'en': 'How many time?', 'pt': 'Quantos tempo?', 'ok': False, 'fb': 'Use How long.'}]},
  {'npc': 'About thirty minutes.', 'pt': 'Uns trinta minutos.', 'opts': [
   {'en': 'I need bring something?', 'pt': 'Eu preciso trazer algo?', 'ok': False, 'fb': 'Use: Do I need to bring anything?'},
   {'en': 'Do I bring need anything?', 'pt': 'Eu trago preciso algo?', 'ok': False, 'fb': 'Wrong word order.'},
   {'en': 'Do I need to bring anything?', 'pt': 'Preciso levar algo?', 'ok': True, 'fb': 'Natural, polite question.'}]},
  {'npc': 'Just a pen and your notebook.', 'pt': 'Só uma caneta e seu caderno.', 'opts': [
   {'en': 'Yes, I am a pen.', 'pt': 'Sim, eu sou uma caneta.', 'ok': False, 'fb': 'Wrong meaning.'},
   {'en': 'No, thanks, it is early.', 'pt': 'Não, obrigado, é cedo.', 'ok': False, 'fb': 'Does not fit his answer.'},
   {'en': 'Great, thanks! See you there.', 'pt': 'Ótimo, valeu! Até lá.', 'ok': True, 'fb': 'Thank him and close the talk.'}]}]},
 'homework': 'Ask a friend in English: “When is…? Where is it? How long is it?” Use a real class, show or meeting.',
 'homework_items': ['Write the times of 3 events you have this week.', 'Say: It’s at ten o’clock. / About thirty minutes.', 'Listen to the dialogue and shadow Evan.', 'Review: When is…? / Where is it? / How long is it?'],
 'errors': [
  {'wrong': 'The meeting is in ten hours.', 'fix': 'The meeting is at ten o’clock.', 'alt': 'The meeting is on ten o’clock.', 'why': 'For a clock time use at: at ten o’clock.'},
  {'wrong': 'In room two, in the second floor.', 'fix': 'In room two, on the second floor.', 'alt': 'In room two, at the second floor.', 'why': 'Use on with floors.'},
  {'wrong': 'How many time is the meeting?', 'fix': 'How long is the meeting?', 'alt': 'How much time is the meeting?', 'why': 'Ask about length with How long.'},
  {'wrong': 'I need bring a pen?', 'fix': 'Do I need to bring a pen?', 'alt': 'Do I need bring a pen?', 'why': 'need + to + verb, and the question starts with Do.'}]}
