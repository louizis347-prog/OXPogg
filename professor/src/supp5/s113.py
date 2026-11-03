"""Suplemento Quest v5 · aula 113: Enroll in a class + regular I take a guitar class (A Little Princess)."""
SUPP = {
 'reg': 164,
 'badge': {'icon': '🎓', 'name': 'Class Starter', 'desc': 'Enroll: form, schedule, price and payment'},
 'culture': {
  'hook': 'To start a class in the USA, you usually fill out a form, check the schedule, ask about the price and then pay. Adult schools and community colleges often offer English classes.',
  'mythfact': [
   {'s': 'In the USA, adults can often take English classes at a community college or adult school.', 'ans': True, 'why': 'Many places offer them, and some are free or low cost.'},
   {'s': 'Every English class costs the same everywhere.', 'ans': False, 'why': 'Prices and rules change by school, city and class.'},
   {'s': 'A school may ask you to take a short test to find your level.', 'ans': True, 'why': 'A placement test helps put you in the right class.'},
   {'s': 'You must pay the whole price in one payment.', 'ans': False, 'why': 'Some schools let you pay in parts; it is good to ask.'},
   {'s': '“A Little Princess” is a novel from 1905.', 'ans': True, 'why': 'Frances Hodgson Burnett wrote it, and Sara Crewe goes to a boarding school.'}],
  'wild': [
   {'kind': 'Class flyer', 'lines': ['**English for Beginners**', 'Mon & Wed, 6:00–8:00 p.m.', 'Register at the front office.'], 'decode': {'q': 'When is the class?', 'opts': ['Monday and Wednesday evening', 'Saturday morning', 'Every day at noon'], 'ans': 0, 'why': 'Mon & Wed, 6:00–8:00 p.m.'}},
   {'kind': 'Registration note', 'lines': ['**Class fee:** $200', 'You can pay in 2 parts.', 'Bring a photo ID.'], 'decode': {'q': 'What do you bring?', 'opts': ['A photo ID', 'A pet', 'A bike'], 'ans': 0, 'why': '“Bring a photo ID.”'}}],
  'compare': {'br': 'No Brasil, a matrícula em cursos de idiomas costuma ser feita na secretaria, com ficha e documento.', 'us': 'Nos EUA, muitas escolas também deixam fazer a matrícula pelo site, com formulário e pagamento on-line.', 'tip': 'Ask: “What’s the class schedule?”', 'ask': 'What class do you want to take? When can you study?'},
  'quiz': [
   {'q': 'You want to join a class. You say…', 'opts': ['I’d like to enroll in a class.', 'I want enter on a class.', 'I enroll class me.'], 'ans': 0, 'why': 'Enroll in a class is the natural phrase.'},
   {'q': 'Which question asks about price?', 'opts': ['How much is the class?', 'Where is the class?', 'Who is the teacher?'], 'ans': 0, 'why': 'How much…? asks about price.'},
   {'q': '“Monday and Wednesday, from six to eight” is…', 'opts': ['the schedule', 'the price', 'the level'], 'ans': 0, 'why': 'Days and hours are the schedule.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Leo joins a class',
  'text': [
   'Leo lives in **Phoenix**. He works in a restaurant, but he wants to speak better English. A coworker says, “There is a good class at the adult school.” So Leo goes there after work.',
   'At the front office, a woman named Kai helps him. “Hi! **I’d like to enroll in an English class**,” Leo says. “**Sure. Do you have a form?**” “No. **Can I have one?**” “**Here you go. Fill it out, please.**”',
   'Leo writes his name and phone number. Then he asks, “**What’s the class schedule?**” “**Monday and Wednesday, from six to eight.**” “**How much is the class?**” “**It’s two hundred dollars.**” Leo thinks for a moment. “**Can I pay in two parts?**”',
   'While he waits, Leo reads a poster about “A Little Princess.” It is a novel from 1905 about Sara Crewe, a girl at a boarding school in London. Sara is kind, and she keeps learning, even when life is hard. Leo likes that idea.',
   'Kai says, “Yes, you can pay in two parts.” Leo signs the form and smiles. His first lesson is on Monday. He is a beginner, but he is ready to learn.'],
  'glossary': [{'w': 'enroll', 'pt': 'matricular-se'}, {'w': 'form', 'pt': 'formulário'}, {'w': 'schedule', 'pt': 'horário'}, {'w': 'dollars', 'pt': 'dólares'}, {'w': 'parts', 'pt': 'partes, parcelas'}, {'w': 'poster', 'pt': 'cartaz'}, {'w': 'novel', 'pt': 'romance'}, {'w': 'boarding school', 'pt': 'internato'}, {'w': 'lesson', 'pt': 'aula'}, {'w': 'beginner', 'pt': 'iniciante'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A man enrolls in a class', 'A woman buys a dress', 'A boy visits a zoo'], 'ans': 0, 'why': 'Leo enrolls in an English class.'},
  'scan': [{'q': 'Who helps Leo?', 'ans': 'Kai', 'alt': ['a woman named Kai']}, {'q': 'How much is the class?', 'ans': 'two hundred dollars', 'alt': ['$200', '200 dollars', '200']}, {'q': 'When is his first lesson?', 'ans': 'Monday', 'alt': ['on monday']}],
  'tf': [{'s': 'Leo has a form at the start.', 'ans': False, 'why': 'He says, “No. Can I have one?”'}, {'s': 'The class is on Monday and Wednesday.', 'ans': True, 'why': 'From six to eight.'}, {'s': 'Leo can pay in two parts.', 'ans': True, 'why': 'Kai says yes.'}, {'s': 'Leo is an expert in English.', 'ans': False, 'why': 'He is a beginner.'}],
  'order': ['Leo goes to the adult school.', 'Kai gives him a form.', 'Leo asks about the schedule.', 'He asks about the price.', 'Leo signs the form.'],
  'ctx': [{'sent': 'I’d like to enroll in an English class.', 'w': 'enroll', 'opts': ['join officially', 'say goodbye', 'cook'], 'ans': 0, 'why': 'Enroll = sign up for a class.'}, {'sent': 'What’s the class schedule?', 'w': 'schedule', 'opts': ['days and times', 'price', 'teacher'], 'ans': 0, 'why': 'A schedule gives days and hours.'}, {'sent': 'He is a beginner.', 'w': 'beginner', 'opts': ['a person who just started', 'a very old man', 'a teacher'], 'ans': 0, 'why': 'A beginner is new to something.'}],
  'chunkHunt': ['I’d like to enroll in an English class.', 'What’s the class schedule?', 'How much is the class?', 'Can I pay in two parts?'],
  'think': 'What class do you want to take? Why?'},
 'convo': {'npc': {'name': 'Kai'}, 'story': 'You are at the front office of a school. Kai works there and helps you enroll.', 'turns': [
  {'npc': 'Hi! Can I help you?', 'pt': 'Oi! Posso ajudar?', 'opts': [
   {'en': 'Hi! I’d like to enroll in an English class.', 'pt': 'Oi! Eu gostaria de me matricular em uma aula de inglês.', 'ok': True, 'fb': 'Clear request.'},
   {'en': 'Hi! I want to enroll an English class.', 'pt': 'Oi! Quero matricular uma aula de inglês.', 'ok': False, 'fb': 'Say enroll in a class.'},
   {'en': 'Yes, I am a class.', 'pt': 'Sim, eu sou uma aula.', 'ok': False, 'fb': 'Wrong meaning.'}]},
  {'npc': 'Sure. Do you have a form?', 'pt': 'Claro. Você tem um formulário?', 'opts': [
   {'en': 'No. Can I have one?', 'pt': 'Não. Posso pegar um?', 'ok': True, 'fb': 'Polite and short.'},
   {'en': 'No. I have not form.', 'pt': 'Não. Eu não tenho formulário.', 'ok': False, 'fb': 'Use I don’t have one.'},
   {'en': 'Yes, it is two hundred dollars.', 'pt': 'Sim, são duzentos dólares.', 'ok': False, 'fb': 'It does not answer.'}]},
  {'npc': 'Here you go. Fill it out, please.', 'pt': 'Aqui está. Preencha, por favor.', 'opts': [
   {'en': 'Thanks. What’s the class schedule?', 'pt': 'Obrigado. Qual é o horário da aula?', 'ok': True, 'fb': 'Natural next question.'},
   {'en': 'Thanks. Which is the schedule of class?', 'pt': 'Obrigado. Qual é o horário de aula?', 'ok': False, 'fb': 'Say the class schedule.'},
   {'en': 'Fill it out too.', 'pt': 'Preencha você também.', 'ok': False, 'fb': 'Rude and does not fit.'}]},
  {'npc': 'Monday and Wednesday, from six to eight.', 'pt': 'Segunda e quarta, das seis às oito.', 'opts': [
   {'en': 'The class is cheap.', 'pt': 'A aula é barata.', 'ok': False, 'fb': 'You do not know the price yet.'},
   {'en': 'How much is the class?', 'pt': 'Quanto custa a aula?', 'ok': True, 'fb': 'Asks the price.'},
   {'en': 'How many the class?', 'pt': 'Quantos a aula?', 'ok': False, 'fb': 'Use How much is…?'}]},
  {'npc': 'It’s two hundred dollars.', 'pt': 'São duzentos dólares.', 'opts': [
   {'en': 'Can I pay in two parts?', 'pt': 'Posso pagar em duas partes?', 'ok': True, 'fb': 'Good question about payment.'},
   {'en': 'Can I pay by two parts?', 'pt': 'Posso pagar por duas partes?', 'ok': False, 'fb': 'Use pay in two parts.'},
   {'en': 'I am two hundred dollars.', 'pt': 'Eu sou duzentos dólares.', 'ok': False, 'fb': 'Wrong meaning.'}]}]},
 'errors': [
  {'wrong': 'I want to matriculate in a class.', 'fix': 'I want to enroll in a class.', 'alt': 'I want to enroll a class.', 'why': 'Use enroll in, not “matriculate”.'},
  {'wrong': 'What is the hour of the class?', 'fix': 'What’s the class schedule?', 'alt': 'What is the class hours?', 'why': 'Schedule = days and times.'},
  {'wrong': 'The class is from six until eight.', 'fix': 'The class is from six to eight.', 'alt': 'The class is of six to eight.', 'why': 'Use from… to… for a time range.'},
  {'wrong': 'I pay in two times.', 'fix': 'I pay in two parts.', 'alt': 'I pay by two times.', 'why': 'In English, say two parts or two payments.'}],
 'homework': 'Write a short dialogue: you enroll in a class and ask about the schedule and the price.',
 'homework_items': ['Write the days and times of a class you want.', 'Say aloud: How much is the class?', 'Listen to the dialogue and shadow Kai.', 'Review: Monday / Wednesday / six to eight.']}
