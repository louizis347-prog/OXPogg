"""Suplemento Quest v5 · aula 114: Study group + regular Work hard, study hard (The Karate Kid)."""
SUPP = {
 'reg': 187,
 'badge': {'icon': '🧠', 'name': 'Study Buddy', 'desc': 'Join a study group: when, where and what to bring'},
 'culture': {
  'hook': 'In the USA, many students study in small groups. They choose a day, a place and a topic, and they help each other practice. A group like this is also a good way to make friends.',
  'mythfact': [
   {'s': 'Study groups often meet in a library or a school room.', 'ans': True, 'why': 'Many libraries have small rooms that groups can use.'},
   {'s': 'In a study group, only one person talks.', 'ans': False, 'why': 'Everyone talks, asks questions and helps.'},
   {'s': 'Some libraries ask you to reserve a study room.', 'ans': True, 'why': 'Rooms can be busy, so reserving helps; the rules vary by place.'},
   {'s': 'It is rude to ask a classmate to join your group.', 'ans': False, 'why': 'Inviting people is friendly and common.'},
   {'s': '“The Karate Kid” is an American film from 1984.', 'ans': True, 'why': 'It is about a boy who learns karate from an old master.'}],
  'wild': [
   {'kind': 'Library room sign', 'lines': ['**Study Room 3**', 'Groups only: 2–6 people', 'Please keep the door closed.'], 'decode': {'q': 'Who can use Room 3?', 'opts': ['Groups of two to six people', 'Only one person', 'Only teachers'], 'ans': 0, 'why': '“Groups only: 2–6 people.”'}},
   {'kind': 'Group chat message', 'lines': ['**Study group tomorrow, 5 p.m.**', 'Bring your notebook and a pen.', 'We meet at the library!'], 'decode': {'q': 'What do you bring?', 'opts': ['A notebook and a pen', 'A pizza', 'A ticket'], 'ans': 0, 'why': '“Bring your notebook and a pen.”'}}],
  'compare': {'br': 'No Brasil, muita gente estuda em grupo na casa de um colega ou na biblioteca da escola.', 'us': 'Nos EUA, é comum combinar dia, hora e sala, e cada pessoa leva o seu material.', 'tip': 'Ask: “When and where do you meet?”', 'ask': 'Do you like to study alone or in a group? Why?'},
  'quiz': [
   {'q': 'A classmate says, “Want to join us?” You say…', 'opts': ['Yes! When do you meet?', 'Yes, I join you of the group.', 'No, you are a group.'], 'ans': 0, 'why': 'Natural and friendly.'},
   {'q': '“Every Tuesday at five” answers…', 'opts': ['When?', 'Where?', 'Who?'], 'ans': 0, 'why': 'It gives a day and a time.'},
   {'q': 'What do you bring to a study group?', 'opts': ['A notebook and a pen', 'A big sofa', 'A car'], 'ans': 0, 'why': 'You need things to write.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Mia joins a group',
  'text': [
   'Mia studies English in **Minneapolis**. She likes the class, but she is shy and does not speak much. After class, a boy named Jordan says, “Hey, want to join our study group?”',
   '“Yes! **When do you meet?**” “**Every Tuesday at five.**” “**Where?**” “**In the library, room three.**” Mia smiles. That is near her home.',
   '“**What do you study?**” Mia asks. “**English grammar and vocabulary.**” “**Perfect. I need practice**,” Mia says. Jordan laughs. “Me too! **Bring your notebook and a pen.**”',
   'After that talk, Mia feels nervous. She says to herself, “I am not good at speaking.” But she wants to try. A new place can feel scary, but a small group is often friendly, and Jordan seems kind.',
   'That evening, Mia thinks about “The Karate Kid,” an American film from 1984. In the story, a boy learns karate from an old master. He does simple jobs again and again, and slowly he gets strong. Mia thinks, “Practice is like that.”',
   'On Tuesday, she goes to room three. Four students are at the table. They read words, ask questions and say the meanings. After one hour, Mia feels happy. She is not shy now. She has new friends.'],
  'glossary': [{'w': 'study group', 'pt': 'grupo de estudos'}, {'w': 'join', 'pt': 'entrar, juntar-se'}, {'w': 'shy', 'pt': 'tímida'}, {'w': 'grammar', 'pt': 'gramática'}, {'w': 'vocabulary', 'pt': 'vocabulário'}, {'w': 'practice', 'pt': 'prática'}, {'w': 'notebook', 'pt': 'caderno'}, {'w': 'master', 'pt': 'mestre'}, {'w': 'meanings', 'pt': 'significados'}, {'w': 'strong', 'pt': 'forte'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A student joins a study group', 'A man buys a bike', 'A dog runs away'], 'ans': 0, 'why': 'Mia joins Jordan’s study group.'},
  'scan': [{'q': 'When does the group meet?', 'ans': 'every Tuesday at five', 'alt': ['tuesday at five', 'tuesday', 'at five']}, {'q': 'Where is the group?', 'ans': 'in the library, room three', 'alt': ['the library', 'room three', 'library']}, {'q': 'What do they bring?', 'ans': 'a notebook and a pen', 'alt': ['notebook and pen', 'notebook']}],
  'tf': [{'s': 'Mia is a very loud student.', 'ans': False, 'why': 'She is shy.'}, {'s': 'The group meets in the library.', 'ans': True, 'why': 'It is room three.'}, {'s': 'The group studies math.', 'ans': False, 'why': 'They study English grammar and vocabulary.'}, {'s': 'At the end, Mia has new friends.', 'ans': True, 'why': 'She is happy and has new friends.'}],
  'order': ['Jordan invites Mia.', 'Mia asks when and where.', 'Jordan says what to bring.', 'Mia goes to room three.', 'Mia feels happy.'],
  'ctx': [{'sent': 'Want to join our study group?', 'w': 'join', 'opts': ['become part of', 'leave', 'break'], 'ans': 0, 'why': 'Join = become a member.'}, {'sent': 'Mia is shy and does not speak much.', 'w': 'shy', 'opts': ['quiet with new people', 'very hungry', 'very fast'], 'ans': 0, 'why': 'A shy person feels nervous with others.'}, {'sent': 'He does simple jobs again and again.', 'w': 'again and again', 'opts': ['many times', 'only once', 'never'], 'ans': 0, 'why': 'Again and again = many times.'}],
  'chunkHunt': ['Want to join our study group?', 'When do you meet?', 'I need practice.', 'Bring your notebook and a pen.'],
  'think': 'Do you like to study alone or with friends? Why?'},
 'convo': {'npc': {'name': 'Jordan'}, 'story': 'After class, Jordan talks to you about a study group.', 'turns': [
  {'npc': 'Hey, want to join our study group?', 'pt': 'Ei, quer entrar no nosso grupo de estudos?', 'opts': [
   {'en': 'Yes! When do you meet?', 'pt': 'Quero! Quando vocês se encontram?', 'ok': True, 'fb': 'Accepts and asks when.'},
   {'en': 'Yes! I want to join you group.', 'pt': 'Quero! Quero entrar vocês grupo.', 'ok': False, 'fb': 'Use join your group or just say Yes!'},
   {'en': 'No, I am a group.', 'pt': 'Não, eu sou um grupo.', 'ok': False, 'fb': 'Wrong meaning.'}]},
  {'npc': 'Every Tuesday at five.', 'pt': 'Toda terça às cinco.', 'opts': [
   {'en': 'Where?', 'pt': 'Onde?', 'ok': True, 'fb': 'Short and natural.'},
   {'en': 'Who is Tuesday?', 'pt': 'Quem é terça?', 'ok': False, 'fb': 'Wrong question.'},
   {'en': 'Where is a library?', 'pt': 'Onde é uma biblioteca?', 'ok': False, 'fb': 'Too long and not natural.'}]},
  {'npc': 'In the library, room three.', 'pt': 'Na biblioteca, sala três.', 'opts': [
   {'en': 'It is the room three.', 'pt': 'É a sala três.', 'ok': False, 'fb': 'Not needed; ask your next question.'},
   {'en': 'Great. What do you study?', 'pt': 'Ótimo. O que vocês estudam?', 'ok': True, 'fb': 'Natural next question.'},
   {'en': 'Great. What you study?', 'pt': 'Ótimo. O que você estuda?', 'ok': False, 'fb': 'Use What do you study?'}]},
  {'npc': 'English grammar and vocabulary.', 'pt': 'Gramática e vocabulário de inglês.', 'opts': [
   {'en': 'Perfect. I need practice.', 'pt': 'Perfeito. Preciso de prática.', 'ok': True, 'fb': 'Says why it is good for you.'},
   {'en': 'Perfect. I am needing practice.', 'pt': 'Perfeito. Estou precisando de prática.', 'ok': False, 'fb': 'Need is a state verb; say I need.'},
   {'en': 'Perfect. I am a pen.', 'pt': 'Perfeito. Eu sou uma caneta.', 'ok': False, 'fb': 'Does not fit.'}]},
  {'npc': 'Bring your notebook and a pen.', 'pt': 'Traga seu caderno e uma caneta.', 'opts': [
   {'en': 'Thanks! See you on Tuesday.', 'pt': 'Obrigado! Vejo você na terça.', 'ok': True, 'fb': 'Friendly goodbye.'},
   {'en': 'Thanks! I see you on the Tuesday.', 'pt': 'Obrigado! Eu vejo você na a terça.', 'ok': False, 'fb': 'Say See you on Tuesday.'},
   {'en': 'Bring your notebook too.', 'pt': 'Traga seu caderno também.', 'ok': False, 'fb': 'Jordan already said that to you.'}]}]},
 'errors': [
  {'wrong': 'I need practice me.', 'fix': 'I need practice.', 'alt': 'I am need practice.', 'why': 'Say I need + noun. No extra “me”.'},
  {'wrong': 'We meet in Tuesday.', 'fix': 'We meet on Tuesday.', 'alt': 'We meet at Tuesday.', 'why': 'Use on with days: on Tuesday.'},
  {'wrong': 'I study at the library.', 'fix': 'I study in the library.', 'alt': 'I study on the library.', 'why': 'Use in for a room or building: in the library.'},
  {'wrong': 'Bring your caderno.', 'fix': 'Bring your notebook.', 'alt': 'Bring you notebook.', 'why': 'Notebook is the English word; use your, not you.'}],
 'homework': 'Write a short dialogue: you ask a friend about a study group (when, where, what to bring).',
 'homework_items': ['Write 3 things you bring to a study group.', 'Say aloud: When do you meet?', 'Listen to the dialogue and shadow Jordan.', 'Review: in the library / on Tuesday / at five.']}
