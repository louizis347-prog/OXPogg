"""Suplemento Quest v5 · aula 121: My child's school + regular Welcome to My Class (Mary Had a Little Lamb)."""
SUPP = {
 'reg': 30,
 'badge': {'icon': '🏫', 'name': 'School Parent', 'desc': 'Talk to your child’s teacher in English'},
 'culture': {
  'hook': 'In many US schools, parents meet the teacher to talk about the child’s class, homework and friends. These talks are short, friendly and very common.',
  'mythfact': [
   {'s': 'In the USA, parents can often meet the teacher at the school.', 'ans': True, 'why': 'Schools usually have parent-teacher meetings, and many teachers also send emails.'},
   {'s': 'Parents must never ask questions about homework.', 'ans': False, 'why': 'Teachers like questions about homework, grades and friends.'},
   {'s': 'Many US schools have a break called recess.', 'ans': True, 'why': 'Younger children usually play outside at recess.'},
   {'s': 'A teacher is often called by the first name.', 'ans': False, 'why': 'Children usually say Ms., Mr. or Mrs. plus the last name.'},
   {'s': '“Mary Had a Little Lamb” is a children’s poem from the USA.', 'ans': True, 'why': 'It was published in 1830.'}],
  'wild': [
   {'kind': 'Note from the teacher', 'lines': ['Dear parents,', '**Parent meeting** is on **Thursday** at 5:00.', 'Please bring your child’s **notebook**.'], 'decode': {'q': 'What should parents bring?', 'opts': ['The child’s notebook', 'Lunch', 'A new pencil box'], 'ans': 0, 'why': 'The note says: bring your child’s notebook.'}},
   {'kind': 'Sign at the school door', 'lines': ['**Visitors**: please stop at the **front office**.', 'Sign in and take a badge.'], 'decode': {'q': 'Where do visitors go first?', 'opts': ['The front office', 'The playground', 'The classroom'], 'ans': 0, 'why': 'Visitors stop at the front office first.'}}],
  'compare': {'br': 'In Brazil, the parent often talks to the teacher at the school gate or in a reunião de pais, and many schools use a notebook or app for messages.', 'us': 'In the USA, many schools use emails, apps and short meetings. Visitors usually sign in at the front office first.', 'tip': 'A short, kind question, like “How is my son in class?”, starts a good talk.', 'ask': 'What do you ask a teacher about your child? Say one question in English.'},
  'quiz': [
   {'q': 'You want to know about your daughter’s class. You ask…', 'opts': ['How is she in class?', 'How old is class?', 'Where is she class?'], 'ans': 0, 'why': 'How is she in class? asks about her work and behavior.'},
   {'q': 'The teacher says your son is a good student. A natural answer is…', 'opts': ['Thank you! That is good to hear.', 'No, I am not.', 'He is a good teacher.'], 'ans': 0, 'why': 'Thank the teacher for the good news.'},
   {'q': 'Where do visitors usually go first at a US school?', 'opts': ['The front office', 'The gym', 'The bus'], 'ans': 0, 'why': 'Most schools ask visitors to sign in at the office.'}]},
 'reading': {
  'genre': 'Diary',
  'title': 'A talk with my son’s teacher',
  'text': [
   'Today I went to my son’s **school** in **Honolulu**. I stopped at the front office and wrote my name. A woman gave me a badge. Then I walked to the classroom.',
   'The room was nice. Colorful drawings were on the wall, and each child had a **desk**. The teacher, Ms. Lane, smiled and said, “**Please sit down.**” I sat next to a small table.',
   'I was nervous, but I asked, “**How is he in class?**” Ms. Lane said, “**He is a good student.**” Then I asked, “**Does he do his homework?**” She said, “**Yes, every day.** **Good job**, Leo!”',
   'I also asked, “**Does he have friends?**” “Yes,” she said. “He is very friendly. At recess he plays with three boys.” I felt so happy.',
   'In class, Ms. Lane says, “**Quiet, please**” and “**Hands up!**” The children know the rules. She showed me Leo’s notebook. His writing was neat, and there was a small star on the page.',
   'At the end, I asked, “**Is there anything he needs?**” “Just more time to read at home,” she said. I thanked her. On the way out, I looked at the poem on the wall: “Mary Had a Little Lamb.” I smiled. School is a good place.'],
  'glossary': [{'w': 'school', 'pt': 'escola'}, {'w': 'badge', 'pt': 'crachá'}, {'w': 'desk', 'pt': 'carteira'}, {'w': 'drawings', 'pt': 'desenhos'}, {'w': 'recess', 'pt': 'recreio'}, {'w': 'notebook', 'pt': 'caderno'}, {'w': 'neat', 'pt': 'caprichado'}, {'w': 'star', 'pt': 'estrela'}, {'w': 'rules', 'pt': 'regras'}, {'w': 'friendly', 'pt': 'simpático'}],
  'fast': {'q': 'What is this text about?', 'opts': ['A parent talks to a teacher', 'A trip to the beach', 'A job interview'], 'ans': 0, 'why': 'The writer meets Leo’s teacher at school.'},
  'scan': [{'q': 'What is the teacher’s name?', 'ans': 'Ms. Lane', 'alt': ['lane']}, {'q': 'What is the son’s name?', 'ans': 'Leo', 'alt': ['leo']}, {'q': 'Where does the writer stop first?', 'ans': 'front office', 'alt': ['the front office', 'office']}],
  'tf': [
   {'s': 'The writer goes to the classroom before the front office.', 'ans': False, 'why': 'The writer stops at the front office first.'},
   {'s': 'Leo does his homework every day.', 'ans': True, 'why': 'Ms. Lane says, “Yes, every day.”'},
   {'s': 'Leo has no friends.', 'ans': False, 'why': 'The teacher says he is very friendly.'},
   {'s': 'Ms. Lane says Leo needs more time to read at home.', 'ans': True, 'why': '“Just more time to read at home.”'}],
  'order': ['The writer signs in at the front office.', 'The teacher says, “Please sit down.”', 'The writer asks about class and homework.', 'The writer asks about friends.', 'The teacher says Leo needs more time to read.'],
  'ctx': [
   {'sent': 'I was nervous, but I asked a question.', 'w': 'nervous', 'opts': ['a little worried', 'very hungry', 'sleepy'], 'ans': 0, 'why': 'Nervous = worried or tense.'},
   {'sent': 'His writing was neat.', 'w': 'neat', 'opts': ['clean and careful', 'very long', 'hard to read'], 'ans': 0, 'why': 'Neat = clean and well done.'},
   {'sent': 'At recess he plays with three boys.', 'w': 'recess', 'opts': ['a school break to play', 'a long test', 'a bus trip'], 'ans': 0, 'why': 'Recess = the break when children play.'}],
  'chunkHunt': ['How is he in class?', 'He is a good student.', 'Does he do his homework?', 'Is there anything he needs?'],
  'think': 'What do you want to ask your child’s teacher? Write two questions in English.'},
 'convo': {'npc': {'name': 'Ms. Lane'}, 'story': 'You are a parent at your child’s school in Honolulu. Ms. Lane is the teacher. Talk about your child.', 'turns': [
  {'npc': 'Hello! I’m Ms. Lane, Anna’s teacher. Please sit down.', 'pt': 'Olá! Sou a Ms. Lane, professora da Anna. Sente-se, por favor.', 'opts': [
   {'en': 'Thank you. How is Anna in class?', 'pt': 'Obrigada. Como a Anna está na aula?', 'ok': True, 'fb': 'Thank her, then ask your question.'},
   {'en': 'Yes, I am Anna.', 'pt': 'Sim, eu sou a Anna.', 'ok': False, 'fb': 'Anna is your child, not you.'},
   {'en': 'She is a good student.', 'pt': 'Ela é uma boa aluna.', 'ok': False, 'fb': 'That is the teacher’s answer, not your question.'}]},
  {'npc': 'Anna is a good student. She works very well.', 'pt': 'A Anna é uma boa aluna. Ela trabalha muito bem.', 'opts': [
   {'en': 'I am a student.', 'pt': 'Eu sou aluna.', 'ok': False, 'fb': 'It does not answer the teacher.'},
   {'en': 'Does she do her homework?', 'pt': 'Ela faz a lição de casa?', 'ok': False, 'fb': 'Good question, but first react to the good news.'},
   {'en': 'That’s great to hear. Does she do her homework?', 'pt': 'Que bom ouvir isso. Ela faz a lição de casa?', 'ok': True, 'fb': 'React, then ask the next question.'}]},
  {'npc': 'Yes, every day. She is very careful.', 'pt': 'Sim, todo dia. Ela é muito cuidadosa.', 'opts': [
   {'en': 'Good. Does she have friends?', 'pt': 'Que bom. Ela tem amigos?', 'ok': True, 'fb': 'A natural next question.'},
   {'en': 'Yes, every day.', 'pt': 'Sim, todo dia.', 'ok': False, 'fb': 'That repeats the teacher’s words.'},
   {'en': 'Do you have homework?', 'pt': 'Você tem lição de casa?', 'ok': False, 'fb': 'You ask about Anna, not the teacher.'}]},
  {'npc': 'Yes! She is very friendly. She plays with many children.', 'pt': 'Sim! Ela é muito simpática. Brinca com muitas crianças.', 'opts': [
   {'en': 'I am friendly, too.', 'pt': 'Eu também sou simpática.', 'ok': False, 'fb': 'The talk is about Anna.'},
   {'en': 'That makes me happy. Is there anything she needs?', 'pt': 'Isso me deixa feliz. Ela precisa de algo?', 'ok': True, 'fb': 'Close the talk with a useful question.'},
   {'en': 'She needs me.', 'pt': 'Ela precisa de mim.', 'ok': False, 'fb': 'This is not an answer to the situation.'}]},
  {'npc': 'Just a little more reading at home. Thanks for coming!', 'pt': 'Só um pouco mais de leitura em casa. Obrigada por vir!', 'opts': [
   {'en': 'Good morning!', 'pt': 'Bom dia!', 'ok': False, 'fb': 'This is a goodbye, not a greeting.'},
   {'en': 'We will read every night. Thank you, Ms. Lane!', 'pt': 'Vamos ler toda noite. Obrigada, Ms. Lane!', 'ok': True, 'fb': 'Promise to help and thank the teacher.'},
   {'en': 'I am reading now.', 'pt': 'Estou lendo agora.', 'ok': False, 'fb': 'It does not answer her request.'}]}]},
 'homework': 'Write 4 questions you can ask a teacher about a child, then say them out loud.',
 'homework_items': ['Say: How is he/she in class?', 'Write 3 sentences about a child you know: student, homework, friends.', 'Listen to the dialogue and repeat each line.', 'Review: Please sit down / Good job / Is there anything…?'],
 'errors': [
  {'wrong': 'She have friends.', 'fix': 'She has friends.', 'alt': 'She haves friends.', 'why': 'With she/he, have becomes has.'},
  {'wrong': 'She does her homework every days.', 'fix': 'She does her homework every day.', 'alt': 'She do her homework every day.', 'why': 'After every, use singular: every day. After she, use does.'},
  {'wrong': 'Does she has friends?', 'fix': 'Does she have friends?', 'alt': 'Do she have friends?', 'why': 'After Does, use the base verb: have.'},
  {'wrong': 'How is she on class?', 'fix': 'How is she in class?', 'alt': 'How she is in class?', 'why': 'Say in class, and keep the question order: How is she…?'}],
}
