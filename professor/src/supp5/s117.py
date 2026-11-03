"""Suplemento Quest v5 · aula 117: Homework help + regular At school and at home (School of Rock)."""
SUPP = {
 'reg': 123,
 'badge': {'icon': '🧮', 'name': 'Homework Hero', 'desc': 'Ask for homework help and check your answer'},
 'culture': {
  'hook': 'In the USA, children often have homework after school. Parents, older brothers and sisters, or a teacher can help. Asking for help is normal, and praise like “Great job!” is very common.',
  'mythfact': [
   {'s': 'In many US schools, students do some homework at home.', 'ans': True, 'why': 'Homework is common, and the amount depends on the school and the grade.'},
   {'s': 'In English, we say “seven plus eight” for 7 + 8.', 'ans': True, 'why': 'Plus is the normal word for + when you read a math problem.'},
   {'s': 'It is wrong to ask a parent for homework help.', 'ans': False, 'why': 'Many families work together, and teachers often say it is fine to ask.'},
   {'s': 'Many US libraries have a place to do homework.', 'ans': True, 'why': 'Many public libraries have tables, computers and sometimes homework help.'},
   {'s': '“School of Rock” is a comedy about a teacher and a band.', 'ans': True, 'why': 'It is a 2003 film with Jack Black.'}],
  'wild': [
   {'kind': 'Note from a teacher', 'lines': ['**Math homework: page 12**', 'Numbers 1–10', 'Show your work. Due Friday.'], 'decode': {'q': 'When is the homework due?', 'opts': ['Friday', 'Monday', 'Today'], 'ans': 0, 'why': 'The note says “Due Friday.”'}},
   {'kind': 'Sign at a library table', 'lines': ['**Homework Help**', 'Mon–Thu, 4:00–6:00 p.m.', 'Free. Ask at the desk.'], 'decode': {'q': 'Is Homework Help free?', 'opts': ['Yes', 'No, it is five dollars', 'Only on Friday'], 'ans': 0, 'why': 'The sign says “Free.”'}}],
  'compare': {'br': 'In Brazil, the homework is often called “lição de casa” or “dever”, and many families help with it at the table.', 'us': 'In the USA, many teachers also say “Show your work”, so you write the steps, not only the answer.', 'tip': 'Say: “Can you help me with my homework?”', 'ask': 'Who helps you when you do not understand something? Say it in English.'},
  'quiz': [
   {'q': 'You want help. You say…', 'opts': ['Can you help me with my homework?', 'You help my homework?', 'Help me with homework of me.'], 'ans': 0, 'why': 'Can you help me with…? is natural and polite.'},
   {'q': 'What is nine minus three?', 'opts': ['six', 'twelve', 'three plus nine'], 'ans': 0, 'why': '9 − 3 = 6.'},
   {'q': 'What does “Practice makes perfect” mean?', 'opts': ['Do it many times and you get better', 'You are perfect now', 'Practice is not important'], 'ans': 0, 'why': 'More practice means better skills.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Number five',
  'text': [
   'Leo is a student in **Atlanta**. After school, he sits at the table in the living room with his math book. He has a lot of homework, and one problem is hard.',
   '“**Mom, can you help me with my homework?**” “**Sure. What is it?**” “**It’s math. I don’t understand number five.**” “**Let’s read it together**,” says Mom.',
   '“**What is seven plus eight?**” Mom asks. Leo counts on his fingers. “**It’s fifteen.**” “**Right!**” says Mom. “**Now write the answer.**” Leo writes it on the page. “**I wrote it. Is it correct?**” “**Yes, great job!**”',
   'Number six is hard too. Leo wants to stop. “**Don’t give up**,” says Mom. “**Practice makes perfect.**” They do it step by step. “**Almost there!**” Soon Leo has the answer, and he says, “**This is a piece of cake!**”',
   'Leo thinks about the film “School of Rock.” In that movie, a funny teacher plays the guitar with his class instead of doing math. Leo laughs. “First math, then music,” he says. He closes his book and picks up his guitar.'],
  'glossary': [{'w': 'student', 'pt': 'aluno'}, {'w': 'problem', 'pt': 'problema, exercício'}, {'w': 'counts', 'pt': 'conta'}, {'w': 'fingers', 'pt': 'dedos'}, {'w': 'correct', 'pt': 'certo, correto'}, {'w': 'give up', 'pt': 'desistir'}, {'w': 'step by step', 'pt': 'passo a passo'}, {'w': 'soon', 'pt': 'logo'}, {'w': 'funny', 'pt': 'engraçado'}, {'w': 'instead of', 'pt': 'em vez de'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A boy gets help with math homework', 'A boy cooks dinner', 'A girl goes to the park'], 'ans': 0, 'why': 'Leo asks Mom for help with math.'},
  'scan': [{'q': 'Which number does Leo not understand?', 'ans': 'number five', 'alt': ['five', '5']}, {'q': 'What is seven plus eight?', 'ans': 'fifteen', 'alt': ['15']}, {'q': 'What does Leo pick up at the end?', 'ans': 'his guitar', 'alt': ['guitar', 'a guitar']}],
  'tf': [{'s': 'Leo asks his mother for help.', 'ans': True, 'why': '“Mom, can you help me with my homework?”'}, {'s': 'The homework is about English.', 'ans': False, 'why': 'It is math.'}, {'s': 'Seven plus eight is fifteen.', 'ans': True, 'why': 'Mom and Leo say “It’s fifteen.”'}, {'s': 'Leo wants to give up, and Mom says yes.', 'ans': False, 'why': 'Mom says, “Don’t give up.”'}],
  'order': ['Leo asks Mom for help.', 'They read number five together.', 'Leo says seven plus eight is fifteen.', 'Leo writes the answer.', 'Leo picks up his guitar.'],
  'ctx': [{'sent': 'Is the answer correct?', 'w': 'correct', 'opts': ['right', 'long', 'cold'], 'ans': 0, 'why': 'Correct = right, without a mistake.'}, {'sent': 'Please don’t give up.', 'w': 'give up', 'opts': ['stop trying', 'give a gift', 'stand up'], 'ans': 0, 'why': 'Give up = stop trying.'}, {'sent': 'Soon he has the answer.', 'w': 'soon', 'opts': ['in a short time', 'never', 'last year'], 'ans': 0, 'why': 'Soon = in a short time.'}],
  'chunkHunt': ['Can you help me with my homework?', 'I don’t understand number five.', 'Let’s read it together.', 'Is it correct?'],
  'think': 'Who helps you with hard things? How do you ask them for help?'},
 'convo': {'npc': {'name': 'Mom'}, 'story': 'You are a student with hard math homework. You ask your mom for help.', 'turns': [
  {'npc': 'You look worried. What’s wrong?', 'pt': 'Você parece preocupado. O que foi?', 'opts': [
   {'en': 'Hi, Mom. Can you help me with my homework?', 'pt': 'Oi, mãe. Pode me ajudar com a lição?', 'ok': True, 'fb': 'Natural way to ask for help.'},
   {'en': 'Hi, Mom. I help you with homework?', 'pt': 'Oi, mãe. Eu ajudo você com a lição?', 'ok': False, 'fb': 'You ask for help: Can you help me…?'},
   {'en': 'I love homework, Mom.', 'pt': 'Eu amo lição, mãe.', 'ok': False, 'fb': 'It does not answer her question.'}]},
  {'npc': 'Sure. What is it?', 'pt': 'Claro. O que é?', 'opts': [
   {'en': 'It’s math. I no understand number five.', 'pt': 'É matemática. Eu não entender a número cinco.', 'ok': False, 'fb': 'Say: I don’t understand.'},
   {'en': 'It’s a pencil.', 'pt': 'É um lápis.', 'ok': False, 'fb': 'It does not fit.'},
   {'en': 'It’s math. I don’t understand number five.', 'pt': 'É matemática. Não entendo a número cinco.', 'ok': True, 'fb': 'Clear and short.'}]},
  {'npc': 'Let’s read it together. What is seven plus eight?', 'pt': 'Vamos ler juntos. Quanto é sete mais oito?', 'opts': [
   {'en': 'It’s fifteen.', 'pt': 'São quinze.', 'ok': True, 'fb': 'Correct and natural.'},
   {'en': 'Is fiveteen.', 'pt': 'É quinze.', 'ok': False, 'fb': 'Say: fifteen, and start with It’s.'},
   {'en': 'It’s Monday.', 'pt': 'É segunda-feira.', 'ok': False, 'fb': 'Wrong answer.'}]},
  {'npc': 'Right! Now write the answer.', 'pt': 'Certo! Agora escreva a resposta.', 'opts': [
   {'en': 'I write it. It is correct?', 'pt': 'Eu escrevo. É correto?', 'ok': False, 'fb': 'Use I wrote it. Is it correct?'},
   {'en': 'I am the answer.', 'pt': 'Eu sou a resposta.', 'ok': False, 'fb': 'Wrong meaning.'},
   {'en': 'I wrote it. Is it correct?', 'pt': 'Escrevi. Está certo?', 'ok': True, 'fb': 'Past tense: wrote. Then a question.'}]},
  {'npc': 'Yes, great job!', 'pt': 'Sim, ótimo trabalho!', 'opts': [
   {'en': 'Thanks, Mom! You are the best.', 'pt': 'Valeu, mãe! Você é demais.', 'ok': True, 'fb': 'Warm and natural.'},
   {'en': 'Great job to you.', 'pt': 'Ótimo trabalho para você.', 'ok': False, 'fb': 'Say Thanks first.'},
   {'en': 'No, I am not.', 'pt': 'Não, eu não sou.', 'ok': False, 'fb': 'It does not fit.'}]}]},
 'errors': [
  {'wrong': 'I no understand number five.', 'fix': 'I don’t understand number five.', 'alt': 'I not understand number five.', 'why': 'For no in the present, use don’t before the verb.'},
  {'wrong': 'Can you help me in my homework?', 'fix': 'Can you help me with my homework?', 'alt': 'Can you help me on my homework?', 'why': 'Help someone with something.'},
  {'wrong': 'Seven more eight is fifteen.', 'fix': 'Seven plus eight is fifteen.', 'alt': 'Seven and plus eight is fifteen.', 'why': 'Use plus for + in math.'},
  {'wrong': 'I write the answer yesterday.', 'fix': 'I wrote the answer yesterday.', 'alt': 'I writed the answer yesterday.', 'why': 'Write is irregular: wrote.'}],
 'homework': 'Write 3 math problems in English, like “nine minus four is five,” and solve them.',
 'homework_items': ['Write 5 numbers from 11 to 20.', 'Say aloud: Can you help me with my homework?', 'Listen to the dialogue and shadow Bethany.', 'Say 3 problems with plus and 3 with minus.']}
