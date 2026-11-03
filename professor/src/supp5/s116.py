"""Suplemento Quest v5 · aula 116: Ask the teacher + regular Any Questions? (The Boy Who Cried Wolf)."""
SUPP = {
 'reg': 31,
 'badge': {'icon': '🙋', 'name': 'Brave Question', 'desc': 'Ask the teacher for help and ask to repeat'},
 'culture': {
  'hook': 'In many American classrooms, teachers like questions. Students raise a hand and say “Excuse me” or “I have a question.” Asking is a normal way to learn, not a problem.',
  'mythfact': [
   {'s': 'In many US classes, it is normal to ask the teacher a question.', 'ans': True, 'why': 'Teachers often say “Any questions?” and want students to ask.'},
   {'s': 'Asking a teacher to repeat something is rude.', 'ans': False, 'why': 'It is polite if you say “Can you repeat, please?”'},
   {'s': 'Students in the USA often raise a hand before they speak.', 'ans': True, 'why': 'Raising a hand is a common way to ask for a turn, mainly in school.'},
   {'s': 'You can only ask a question after the class ends.', 'ans': False, 'why': 'You can ask during class, and many teachers also answer after class.'},
   {'s': '“The Boy Who Cried Wolf” is a very old fable.', 'ans': True, 'why': 'It is a fable usually linked to Aesop, from ancient Greece.'}],
  'wild': [
   {'kind': 'Sign on a classroom door', 'lines': ['**Room 12 – Ms. Lee**', 'Questions? Come in!', 'Office hours: Tue 3:00–4:00'], 'decode': {'q': 'When can students talk to Ms. Lee after school?', 'opts': ['Tuesday at 3:00', 'Every morning', 'Never'], 'ans': 0, 'why': 'The sign says Tue 3:00–4:00.'}},
   {'kind': 'Note on a board', 'lines': ['**Homework: page 14**', 'Due Thursday', 'Ask me if it is not clear.'], 'decode': {'q': 'What should you do if the homework is not clear?', 'opts': ['Ask the teacher', 'Wait until Friday', 'Skip page 14'], 'ans': 0, 'why': '“Ask me if it is not clear.”'}}],
  'compare': {'br': 'In Brazil, many students call the teacher “professor” or “tia” and may wait for the teacher to finish before they speak.', 'us': 'In the USA, students often call the teacher Mr., Ms. or Mrs. plus the last name, and questions in class are welcome in many schools.', 'tip': 'Start with “Excuse me” and the name: “Excuse me, Ms. Lee.”', 'ask': 'What do you say in your language when you do not understand? Say it in English.'},
  'quiz': [
   {'q': 'You do not hear the teacher. You say…', 'opts': ['Can you repeat, please?', 'Repeat me, please.', 'What repeat?'], 'ans': 0, 'why': 'Can you…, please? is a polite request.'},
   {'q': 'What does “It gets easier” mean?', 'opts': ['It becomes less hard with time', 'It is already finished', 'It is only for children'], 'ans': 0, 'why': 'Gets easier = becomes easier.'},
   {'q': 'Which question asks for a meaning?', 'opts': ['What does “homework” mean?', 'Where is homework?', 'Who is homework?'], 'ans': 0, 'why': 'What does … mean? asks for the meaning of a word.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Lia’s big question',
  'text': [
   'Lia is a student in an English class in **San Antonio**. The class is new for her, and she feels **so lost**. Her teacher, Ms. Lee, writes a new word on the board: “homework.”',
   'Lia raises her hand. “**Excuse me, teacher. I have a question.**” “**Of course. What is it?**” Ms. Lee asks. “**What does “homework” mean?**” “**It’s work you do at home**,” says the teacher. “**Ah, I see. Thank you.**”',
   'Ms. Lee looks at the class. “**Any questions?**” Lia raises her hand again. “**Can you repeat, please?**” “**Sure. Slowly this time.**” Ms. Lee says the sentence again, one word at a time. “**Now it’s clear**,” Lia says. “**Don’t worry**,” says Ms. Lee. “**It gets easier.**”',
   'Then Ms. Lee tells an old story, “The Boy Who Cried Wolf.” A boy shouts “Wolf!” as a joke, and the people run to help him. But there is no wolf. Later a real wolf comes, and nobody believes the boy. “In class, a real question is a good thing,” Ms. Lee says. “**Ask the teacher** anytime.”',
   'After class, Lia opens her dictionary and her notebook. She writes “homework” and “repeat” with a pencil. She is not lost now. She smiles, and she wants to ask again tomorrow.'],
  'glossary': [{'w': 'student', 'pt': 'aluno'}, {'w': 'board', 'pt': 'quadro'}, {'w': 'raises', 'pt': 'levanta'}, {'w': 'repeat', 'pt': 'repetir'}, {'w': 'slowly', 'pt': 'devagar'}, {'w': 'clear', 'pt': 'claro'}, {'w': 'wolf', 'pt': 'lobo'}, {'w': 'joke', 'pt': 'brincadeira'}, {'w': 'dictionary', 'pt': 'dicionário'}, {'w': 'pencil', 'pt': 'lápis'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A student asks her teacher for help', 'A boy loses a wolf', 'A teacher goes to the market'], 'ans': 0, 'why': 'Lia asks Ms. Lee two questions.'},
  'scan': [{'q': 'What is the teacher’s name?', 'ans': 'Ms. Lee', 'alt': ['Lee', 'ms lee']}, {'q': 'Which word does Lia ask about?', 'ans': 'homework', 'alt': ['"homework"', 'the word homework']}, {'q': 'What does Lia use to write after class?', 'ans': 'a pencil', 'alt': ['pencil', 'her pencil']}],
  'tf': [{'s': 'Lia raises her hand to ask a question.', 'ans': True, 'why': '“Lia raises her hand.”'}, {'s': 'Ms. Lee is angry about the question.', 'ans': False, 'why': 'She says, “Of course. What is it?”'}, {'s': 'Ms. Lee says the sentence again slowly.', 'ans': True, 'why': 'She says it one word at a time.'}, {'s': 'In the story, the wolf is real at the start.', 'ans': False, 'why': 'At first there is no wolf. The boy tells a joke.'}],
  'order': ['Ms. Lee writes “homework” on the board.', 'Lia asks what “homework” means.', 'Lia asks the teacher to repeat.', 'Ms. Lee tells a story about a wolf.', 'Lia writes new words after class.'],
  'ctx': [{'sent': 'Can you repeat, please?', 'w': 'repeat', 'opts': ['say it again', 'stop talking', 'write it down'], 'ans': 0, 'why': 'Repeat = say again.'}, {'sent': 'Say it slowly, please.', 'w': 'slowly', 'opts': ['not fast', 'very loud', 'in a book'], 'ans': 0, 'why': 'Slowly = not fast.'}, {'sent': 'Now it’s clear.', 'w': 'clear', 'opts': ['easy to understand', 'very cold', 'not in class'], 'ans': 0, 'why': 'Clear = easy to understand.'}],
  'chunkHunt': ['I have a question.', 'What does “homework” mean?', 'Can you repeat, please?', 'It gets easier.'],
  'think': 'When do you feel lost in English? What can you ask?'},
 'convo': {'npc': {'name': 'Ms. Lee'}, 'story': 'You are a student in an English class. You are lost, so you ask your teacher, Ms. Lee, for help.', 'turns': [
  {'npc': 'Okay, class. Look at the board. Any questions?', 'pt': 'Certo, turma. Olhem o quadro. Alguma pergunta?', 'opts': [
   {'en': 'I have a doubt, teacher.', 'pt': 'Eu tenho uma dúvida, professora.', 'ok': False, 'fb': 'Say: I have a question.'},
   {'en': 'Excuse me, teacher. I have a question.', 'pt': 'Com licença, professora. Tenho uma pergunta.', 'ok': True, 'fb': 'Polite and clear.'},
   {'en': 'The board is green.', 'pt': 'O quadro é verde.', 'ok': False, 'fb': 'It does not answer her.'}]},
  {'npc': 'Of course. What is it?', 'pt': 'Claro. Qual é?', 'opts': [
   {'en': 'What does “homework” mean?', 'pt': 'O que quer dizer “homework”?', 'ok': True, 'fb': 'Good way to ask for a meaning.'},
   {'en': 'What means homework?', 'pt': 'O que significa homework?', 'ok': False, 'fb': 'Use: What does … mean?'},
   {'en': 'It’s work you do at home.', 'pt': 'É o trabalho que você faz em casa.', 'ok': False, 'fb': 'That is the teacher’s answer.'}]},
  {'npc': 'It’s work you do at home.', 'pt': 'É o trabalho que você faz em casa.', 'opts': [
   {'en': 'Can you repeat, please?', 'pt': 'Pode repetir, por favor?', 'ok': True, 'fb': 'Polite request to hear it again.'},
   {'en': 'Repeat to me.', 'pt': 'Repita para mim.', 'ok': False, 'fb': 'Too direct. Use Can you…, please?'},
   {'en': 'Yes, I am home.', 'pt': 'Sim, estou em casa.', 'ok': False, 'fb': 'Does not fit.'}]},
  {'npc': 'Sure. Slowly this time. It’s work you do at home.', 'pt': 'Claro. Devagar desta vez. É o trabalho que você faz em casa.', 'opts': [
   {'en': 'Now is clear.', 'pt': 'Agora é claro.', 'ok': False, 'fb': 'Say: Now it’s clear.'},
   {'en': 'Ah, I see. Now it’s clear. Thank you.', 'pt': 'Ah, entendi. Agora está claro. Obrigado.', 'ok': True, 'fb': 'Shows you understand, and you say thanks.'},
   {'en': 'No, thank you. I am lost.', 'pt': 'Não, obrigado. Estou perdido.', 'ok': False, 'fb': 'It does not fit after a clear answer.'}]},
  {'npc': 'Don’t worry. It gets easier.', 'pt': 'Não se preocupe. Fica mais fácil.', 'opts': [
   {'en': 'Thank you, teacher.', 'pt': 'Obrigado, professora.', 'ok': True, 'fb': 'Simple and kind.'},
   {'en': 'Easier than what?', 'pt': 'Mais fácil do que o quê?', 'ok': False, 'fb': 'Natural, but not the reply she expects.'},
   {'en': 'I am worry.', 'pt': 'Eu sou preocupado.', 'ok': False, 'fb': 'Say: I’m worried.'}]}]},
 'errors': [
  {'wrong': 'I have a doubt.', 'fix': 'I have a question.', 'alt': 'I have one doubt, teacher.', 'why': 'In English, doubt is not the same as “dúvida”. Use question.'},
  {'wrong': 'What means homework?', 'fix': 'What does “homework” mean?', 'alt': 'What “homework” means?', 'why': 'In a question, use does + mean.'},
  {'wrong': 'Repeat, please.', 'fix': 'Can you repeat, please?', 'alt': 'You can repeat me?', 'why': 'Can you…? is softer and more polite.'},
  {'wrong': 'I am lost in the class.', 'fix': 'I’m so lost in this class.', 'alt': 'I am losted in this class.', 'why': 'Use this class, and lost is already the right form.'}],
 'homework': 'Write 3 questions you can ask your teacher when you do not understand.',
 'homework_items': ['Write: What does ___ mean?', 'Say aloud: Can you repeat, please?', 'Listen to the dialogue and shadow Claire.', 'Choose 3 new words and ask a friend what they mean.']}
