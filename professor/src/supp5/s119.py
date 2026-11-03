"""Suplemento Quest v5 · aula 119: Job application + regular The Job Interview (Jobs)."""
SUPP = {
 'reg': 94,
 'badge': {'icon': '📝', 'name': 'First Step', 'desc': 'Fill in a job application with name, phone and email'},
 'culture': {
  'hook': 'In the USA, many stores and restaurants ask you to fill in an application for a job. It can be a paper form or a website. You write your name, address, phone number, email and work experience.',
  'mythfact': [
   {'s': 'A job application usually asks for your name, address and phone number.', 'ans': True, 'why': 'This basic contact information is on almost every form.'},
   {'s': 'In the USA, all job applications are on paper.', 'ans': False, 'why': 'Many stores and companies use websites, and some use paper forms.'},
   {'s': 'People often say phone numbers one digit at a time.', 'ans': True, 'why': 'For example: five five five, one four two two.'},
   {'s': 'A resume is a short paper about your work and studies.', 'ans': True, 'why': 'Many jobs ask for a resume with the application.'},
   {'s': 'The film “Jobs” is about the life of Steve Jobs.', 'ans': True, 'why': 'It is a 2013 film about the founder of Apple.'}],
  'wild': [
   {'kind': 'Sign in a store window', 'lines': ['**Now hiring!**', 'Part-time cashier', 'Ask for an application inside.'], 'decode': {'q': 'What can you do at this store?', 'opts': ['Ask for a job application', 'Buy a cashier', 'Sign a ticket'], 'ans': 0, 'why': '“Ask for an application inside.”'}},
   {'kind': 'Top of an application form', 'lines': ['**Name:** ________', '**Phone:** ________', '**Email:** ________', 'Please print clearly.'], 'decode': {'q': 'What does “print clearly” mean?', 'opts': ['Write in clear letters', 'Use a printer', 'Write very small'], 'ans': 0, 'why': 'Print = write letters by hand, clearly.'}}],
  'compare': {'br': 'In Brazil, people often take a printed “currículo” to a store, and many jobs ask for a CPF.', 'us': 'In the USA, many stores use online forms, and a resume is common. The form asks for name, address, phone, email and experience.', 'tip': 'Spell your email: “noor at mail dot com.”', 'ask': 'Say your phone number in English, one digit at a time.'},
  'quiz': [
   {'q': 'You want a form for a job. You say…', 'opts': ['I’m here for the job application.', 'I am here by the job.', 'I come for a form of job.'], 'ans': 0, 'why': 'I’m here for… is a natural way to say why you came.'},
   {'q': 'How do you say noor@mail.com?', 'opts': ['noor at mail dot com', 'noor arroba mail ponto com', 'noor and mail point com'], 'ans': 0, 'why': '@ is “at” and the dot is “dot”.'},
   {'q': 'What does “experience” mean on a form?', 'opts': ['work you did before', 'your favorite food', 'your home address'], 'ans': 0, 'why': 'Experience = past work or skills.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Noor’s first form',
  'text': [
   'Noor lives in **Dearborn**. He wants to work in a store, so he goes to a shoe store on Main Street. He is a little nervous. “**Fingers crossed**,” he says.',
   '“**Hello! I’m here for the job application.**” “**Great. Please take this form**,” says the manager. “**What do I write first?**” “**Your name and address.**” “**Here is my name: Noor Ali.**”',
   '“**And your phone number?**” “**It’s five five five, one four two two.**” “**What’s your email?**” “**It’s noor at mail dot com.**” The manager writes the numbers on the form. “Do you have any experience?” “A little. I help in my uncle’s shop.”',
   'Noor signs his name at the bottom. The manager smiles. “**You’ve got what it takes**,” she says. “We will call you.” “**Thanks! I could use the job**,” says Noor. “**Keep me posted!**” “**Fingers crossed** for you,” she says.',
   'At home, Noor thinks about the film “Jobs.” In the film, Steve Jobs and his friends start Apple in a garage. Noor smiles. “Every big story starts with a small step,” he says. “My first step is this form.”'],
  'glossary': [{'w': 'store', 'pt': 'loja'}, {'w': 'nervous', 'pt': 'nervoso'}, {'w': 'manager', 'pt': 'gerente'}, {'w': 'form', 'pt': 'formulário'}, {'w': 'phone number', 'pt': 'número de telefone'}, {'w': 'email', 'pt': 'e-mail'}, {'w': 'experience', 'pt': 'experiência'}, {'w': 'bottom', 'pt': 'parte de baixo'}, {'w': 'garage', 'pt': 'garagem'}, {'w': 'step', 'pt': 'passo'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A man fills in a job application', 'A woman buys shoes', 'A boy plays in a garage'], 'ans': 0, 'why': 'Noor fills in a form at a store.'},
  'scan': [{'q': 'What is Noor’s last name?', 'ans': 'Ali', 'alt': ['noor ali']}, {'q': 'What is the first thing to write?', 'ans': 'name and address', 'alt': ['his name and address', 'name']}, {'q': 'What is Noor’s email?', 'ans': 'noor at mail dot com', 'alt': ['noor@mail.com']}],
  'tf': [{'s': 'Noor goes to a shoe store.', 'ans': True, 'why': 'He goes to a shoe store on Main Street.'}, {'s': 'The manager asks for his phone number.', 'ans': True, 'why': '“And your phone number?”'}, {'s': 'Noor has no experience at all.', 'ans': False, 'why': 'He helps in his uncle’s shop.'}, {'s': 'The manager says no.', 'ans': False, 'why': 'She says, “You’ve got what it takes.”'}],
  'order': ['Noor goes to the store.', 'The manager gives him a form.', 'He writes his name and address.', 'He says his phone and email.', 'He signs the form.'],
  'ctx': [{'sent': 'I’m nervous about the form.', 'w': 'nervous', 'opts': ['a little afraid', 'very happy', 'very sleepy'], 'ans': 0, 'why': 'Nervous = a little afraid or worried.'}, {'sent': 'Please take this form.', 'w': 'form', 'opts': ['a paper with spaces to write', 'a kind of shoe', 'a city street'], 'ans': 0, 'why': 'A form is a paper you fill in.'}, {'sent': 'Do you have any experience?', 'w': 'experience', 'opts': ['work you did before', 'a new phone', 'a free day'], 'ans': 0, 'why': 'Experience = past work.'}],
  'chunkHunt': ['I’m here for the job application.', 'What do I write first?', 'It’s noor at mail dot com.', 'Fingers crossed.'],
  'think': 'What job do you want? What is your first step?'},
 'convo': {'npc': {'name': 'Ms. Reyes'}, 'story': 'You want a job at a store. You talk to the manager, Ms. Reyes, and fill in the application.', 'turns': [
  {'npc': 'Hello. Can I help you?', 'pt': 'Olá. Posso ajudar?', 'opts': [
   {'en': 'Hello! I’m here for the work application.', 'pt': 'Olá! Estou aqui para a ficha de trabalho.', 'ok': False, 'fb': 'Say: job application.'},
   {'en': 'Hello! I’m a store.', 'pt': 'Olá! Eu sou uma loja.', 'ok': False, 'fb': 'Wrong meaning.'},
   {'en': 'Hello! I’m here for the job application.', 'pt': 'Olá! Estou aqui para a ficha de emprego.', 'ok': True, 'fb': 'Says why you came.'}]},
  {'npc': 'Great. Please take this form.', 'pt': 'Ótimo. Pegue este formulário.', 'opts': [
   {'en': 'Thanks. What do I write first?', 'pt': 'Obrigado. O que escrevo primeiro?', 'ok': True, 'fb': 'Good question to start.'},
   {'en': 'Thanks. What I write first?', 'pt': 'Obrigado. O que eu escrevo primeiro?', 'ok': False, 'fb': 'Use: What do I write…?'},
   {'en': 'Thanks. I am a form.', 'pt': 'Obrigado. Eu sou um formulário.', 'ok': False, 'fb': 'Wrong meaning.'}]},
  {'npc': 'Your name and address.', 'pt': 'Seu nome e endereço.', 'opts': [
   {'en': 'Here is it my name: Noor Ali.', 'pt': 'Aqui é meu nome: Noor Ali.', 'ok': False, 'fb': 'Say: Here is my name.'},
   {'en': 'Your name and address, too.', 'pt': 'Seu nome e endereço também.', 'ok': False, 'fb': 'You answer with your own name.'},
   {'en': 'Here is my name: Noor Ali.', 'pt': 'Aqui está meu nome: Noor Ali.', 'ok': True, 'fb': 'Clear and natural.'}]},
  {'npc': 'And your phone number?', 'pt': 'E seu telefone?', 'opts': [
   {'en': 'I have a number of phone.', 'pt': 'Eu tenho um número de telefone.', 'ok': False, 'fb': 'Say: It’s …, then the digits.'},
   {'en': 'It’s five five five, one four two two.', 'pt': 'É cinco cinco cinco, um quatro dois dois.', 'ok': True, 'fb': 'Digits one by one.'},
   {'en': 'It’s my mother.', 'pt': 'É minha mãe.', 'ok': False, 'fb': 'It does not answer.'}]},
  {'npc': 'What’s your email?', 'pt': 'Qual é seu e-mail?', 'opts': [
   {'en': 'It’s noor arroba mail ponto com.', 'pt': 'É noor arroba mail ponto com.', 'ok': False, 'fb': 'In English: at and dot.'},
   {'en': 'It’s noor at mail point com.', 'pt': 'É noor at mail ponto com.', 'ok': False, 'fb': 'Say dot, not point.'},
   {'en': 'It’s noor at mail dot com.', 'pt': 'É noor arroba mail ponto com.', 'ok': True, 'fb': '@ = at, . = dot.'}]}]},
 'errors': [
  {'wrong': 'I come for the job.', 'fix': 'I’m here for the job application.', 'alt': 'I am here by the job.', 'why': 'Use I’m here for… to say why you came.'},
  {'wrong': 'What I write first?', 'fix': 'What do I write first?', 'alt': 'What I do write first?', 'why': 'Questions need do before the subject: What do I…?'},
  {'wrong': 'My email is noor arroba mail.', 'fix': 'My email is noor at mail dot com.', 'alt': 'My email is noor at mail point com.', 'why': 'Say at and dot.'},
  {'wrong': 'I have experience of work.', 'fix': 'I have some work experience.', 'alt': 'I have a experience.', 'why': 'Experience here is not counted: some work experience.'}],
 'homework': 'Write your full name, phone number and email in English, and say them aloud.',
 'homework_items': ['Write a short form: name, address, phone, email.', 'Say aloud: I’m here for the job application.', 'Listen to the dialogue and shadow Malik.', 'Learn: form, resume, experience, interview.']}
