"""Suplemento Quest v5 · aula 109: Can you help me? + regular I Can, I Can't"""
SUPP = {'reg': 81, 'badge': {'icon': '🙋', 'name': 'Ask for Help', 'desc': 'Ask a coworker for help and understand the steps in English'},
 'culture': {'hook': 'At work, nobody knows everything. Learn how to ask a coworker for help with a computer problem, say what you can’t do and ask them to show you again.',
  'mythfact': [
   {'s': 'Asking a coworker for help is normal in the USA.', 'ans': True, 'why': 'Most people are happy to help, especially a new person.'},
   {'s': 'You should never say “I can’t” at work.', 'ans': False, 'why': '“I can’t open this file” simply states the problem.'},
   {'s': 'Many companies have an IT help desk for computer problems.', 'ans': True, 'why': 'IT staff help with files, passwords and programs.'},
   {'s': 'It is rude to ask someone to show you again.', 'ans': False, 'why': 'A polite “Can you show me again?” is fine.'}],
  'wild': [
   {'kind': 'Error message', 'lines': ['**Cannot open file**', 'The file is in use by another person.', 'Try again later.'], 'decode': {'q': 'Why can’t you open the file?', 'opts': ['Another person is using it', 'The folder is empty', 'The computer is off'], 'ans': 0, 'why': 'The message says the file is in use by another person.'}},
   {'kind': 'Help desk sign', 'lines': ['**Computer problem?**', 'Send an email to help@company.example', 'or call extension 500.'], 'decode': {'q': 'How can you ask for help?', 'opts': ['Send an email or call', 'Wait one week', 'Ask the boss only'], 'ans': 0, 'why': 'The sign says email or call.'}}],
  'compare': {'br': 'In Brazil many people ask a close coworker for help in person and may not write to a help desk.', 'us': 'In the USA people often use both: a quick “Can you help me?” to a coworker, or a message to the IT help desk.', 'tip': 'Say what the problem is first: “I can’t open this file.” Then ask: “Can you help me?”', 'ask': 'What computer problem do you have? Describe it in English.'},
  'quiz': [
   {'q': 'You need help. You say…', 'opts': ['Excuse me, can you help me?', 'Excuse me, you help I?', 'Help me you can?'], 'ans': 0, 'why': 'Can you + verb is the polite question.'},
   {'q': 'Your file does not open. You say…', 'opts': ['I can’t open this file.', 'I no open file.', 'This file is a can’t.'], 'ans': 0, 'why': 'I can’t + verb.'},
   {'q': 'You want to see the steps again. You say…', 'opts': ['Can you show me again?', 'Show me me again?', 'You show again?'], 'ans': 0, 'why': 'Can you show me again? is polite and clear.'}]},
 'reading': {'genre': 'Short story', 'title': 'Ravi Asks for Help',
  'text': ['Ravi works on a computer all day. Today he has a problem. He can’t open a **file**. The file is important, and his boss needs it before lunch.',
   'He looks around the office. A coworker, Mia, is at the next desk. “**Excuse me, can you help me?**” Ravi asks. “**Sure. What do you need?**” Mia says.',
   '“**I can’t open this file**,” Ravi says. Mia comes to his desk. “**Let me see. Click here**,” she says. She clicks a small **link** and the file opens. “**It’s working now!**” Ravi says.',
   'Ravi smiles, but he wants to learn. “**Can you show me again?**” he asks. “**Of course. First, open the folder**,” Mia says. “**Then double-click the file.**” Ravi writes the steps on a piece of paper.',
   'Mia asks, “**Is it clear?**” “Yes, thanks!” Ravi says. He saves the file in a new folder. Then he asks one more **question**: “Can I **update** it now?” “Yes, go ahead,” Mia says. Ravi feels happy. Asking for help is easy when people are kind.'],
  'glossary': [{'w': 'file', 'pt': 'arquivo'}, {'w': 'boss', 'pt': 'chefe'}, {'w': 'coworker', 'pt': 'colega de trabalho'}, {'w': 'desk', 'pt': 'mesa de trabalho'}, {'w': 'link', 'pt': 'link'}, {'w': 'folder', 'pt': 'pasta'}, {'w': 'steps', 'pt': 'passos'}, {'w': 'clear', 'pt': 'claro'}, {'w': 'update', 'pt': 'atualizar'}, {'w': 'kind', 'pt': 'gentil'}],
  'fast': {'q': 'What is this text about?', 'opts': ['A man asks a coworker for help with a file', 'A man buys a computer', 'A lunch at a deli'], 'ans': 0, 'why': 'Ravi can’t open a file and Mia helps him.'},
  'scan': [{'q': 'Who helps Ravi?', 'ans': 'Mia', 'alt': ['mia', 'a coworker']}, {'q': 'What can’t Ravi open?', 'ans': 'a file', 'alt': ['file', 'the file']}, {'q': 'Where does he save the file?', 'ans': 'in a new folder', 'alt': ['new folder', 'a new folder', 'folder']}],
  'tf': [{'s': 'Ravi’s boss needs the file before lunch.', 'ans': True, 'why': 'The text says his boss needs it before lunch.'}, {'s': 'Mia is Ravi’s boss.', 'ans': False, 'why': 'Mia is a coworker.'}, {'s': 'Ravi asks Mia to show him again.', 'ans': True, 'why': '“Can you show me again?”'}, {'s': 'Ravi is angry at the end.', 'ans': False, 'why': 'He feels happy.'}],
  'order': ['Ravi can’t open a file.', 'He asks Mia for help.', 'Mia clicks a link and the file opens.', 'Ravi asks to see the steps again.', 'He saves the file in a new folder.'],
  'ctx': [{'sent': 'Mia asks, “Is it clear?”', 'w': 'clear', 'opts': ['easy to understand', 'very light', 'empty'], 'ans': 0, 'why': 'Clear = easy to understand.'}, {'sent': 'Asking for help is easy when people are kind.', 'w': 'kind', 'opts': ['nice and friendly', 'a type of food', 'very busy'], 'ans': 0, 'why': 'Kind = nice to others.'}, {'sent': 'Can I update it now?', 'w': 'update', 'opts': ['make it new', 'delete it', 'print it'], 'ans': 0, 'why': 'Update = change to a newer version.'}],
  'chunkHunt': ['Can you help me?', 'What do you need?', 'I can’t open this file.', 'Can you show me again?'], 'think': 'When do you ask for help? Who helps you? What do you say?'},
 'convo': {'npc': {'name': 'Mia'}, 'story': 'You work in an office. Your computer has a problem. Mia is a coworker at the next desk.', 'turns': [
  {'npc': 'Hi! Do you need something?', 'pt': 'Oi! Você precisa de algo?', 'opts': [
   {'en': 'No, I am a file.', 'pt': 'Não, eu sou um arquivo.', 'ok': False, 'fb': 'Wrong meaning.'},
   {'en': 'Yes, I can you.', 'pt': 'Sim, eu posso você.', 'ok': False, 'fb': 'Wrong order. Use: Can you help me?'},
   {'en': 'Yes. Can you help me, please?', 'pt': 'Sim. Pode me ajudar, por favor?', 'ok': True, 'fb': 'Polite and clear.'}]},
  {'npc': 'Sure. What’s the problem?', 'pt': 'Claro. Qual é o problema?', 'opts': [
   {'en': 'I can’t open this file.', 'pt': 'Não consigo abrir este arquivo.', 'ok': True, 'fb': 'I can’t + verb states the problem.'},
   {'en': 'I not can open this file.', 'pt': 'Eu não posso abrir este arquivo.', 'ok': False, 'fb': 'The negative is can’t.'},
   {'en': 'It is a problem file, yes.', 'pt': 'É um arquivo problema, sim.', 'ok': False, 'fb': 'It does not say the real problem.'}]},
  {'npc': 'Let me see. Click here.', 'pt': 'Deixe-me ver. Clique aqui.', 'opts': [
   {'en': 'Click here, thanks.', 'pt': 'Clique aqui, obrigado.', 'ok': False, 'fb': 'Mia is the one who says click.'},
   {'en': 'Thanks! It’s working now!', 'pt': 'Valeu! Agora está funcionando!', 'ok': True, 'fb': 'Thank her and say the result.'},
   {'en': 'No, I am here.', 'pt': 'Não, eu estou aqui.', 'ok': False, 'fb': 'It does not fit.'}]},
  {'npc': 'Great. Is it clear?', 'pt': 'Ótimo. Ficou claro?', 'opts': [
   {'en': 'Yes, it is a clear.', 'pt': 'Sim, é um claro.', 'ok': False, 'fb': 'Say: Yes, it is clear.'},
   {'en': 'Yes. Can you show me again?', 'pt': 'Sim. Pode me mostrar de novo?', 'ok': True, 'fb': 'Ask politely to repeat.'},
   {'en': 'Clear is the file.', 'pt': 'Claro é o arquivo.', 'ok': False, 'fb': 'Does not make sense.'}]},
  {'npc': 'Of course. First, open the folder. Then double-click the file.', 'pt': 'Claro. Primeiro, abra a pasta. Depois clique duas vezes no arquivo.', 'opts': [
   {'en': 'First, I am the folder.', 'pt': 'Primeiro, eu sou a pasta.', 'ok': False, 'fb': 'It does not answer.'},
   {'en': 'Of course, thank you, you open.', 'pt': 'Claro, obrigado, você abre.', 'ok': False, 'fb': 'Not natural.'},
   {'en': 'Okay, I understand. Thanks a lot!', 'pt': 'Ok, entendi. Muito obrigado!', 'ok': True, 'fb': 'A clear, polite close.'}]}]},
 'homework': 'Practice asking for help in English with three problems: a file, a password and a printer. Use “Can you help me?”',
 'homework_items': ['Write 3 problems you can’t solve: I can’t…', 'Say: Can you help me? / Can you show me again?', 'Listen to the dialogue and shadow Ravi.', 'Review: What do you need? / Let me see. / Is it clear?'],
 'errors': [
  {'wrong': 'Can you to help me?', 'fix': 'Can you help me?', 'alt': 'Can you helping me?', 'why': 'After can, use the base verb: help.'},
  {'wrong': 'I no can open this file.', 'fix': 'I can’t open this file.', 'alt': 'I don’t can open this file.', 'why': 'The negative of can is can’t.'},
  {'wrong': 'Show me again, please can you?', 'fix': 'Can you show me again, please?', 'alt': 'You can show me again?', 'why': 'The question starts with Can you…?'},
  {'wrong': 'It is working now! Is clear?', 'fix': 'It’s working now! Is it clear?', 'alt': 'It is working now! Are clear?', 'why': 'Use Is it clear? with the subject it.'}]}
