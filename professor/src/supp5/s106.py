"""Suplemento Quest v5 · aula 106: Printing documents + regular Can I use your pot?"""
SUPP = {'reg': 102, 'badge': {'icon': '🖨️', 'name': 'Office Printer Pro', 'desc': 'Print, copy and fix a paper problem at work in English'},
 'culture': {'hook': 'In many American offices one big printer is shared by everyone. Learn what to click, what to press and what to say when the machine says “No paper”.',
  'mythfact': [
   {'s': 'In many offices people share one printer.', 'ans': True, 'why': 'A shared printer in a hall or a small room is very common.'},
   {'s': 'If the printer is empty, you must call the boss.', 'ans': False, 'why': 'Most people just add paper to the tray or ask a coworker.'},
   {'s': 'It is rude to ask a coworker, “How do I use the printer?”', 'ans': False, 'why': 'It is a normal question, especially for a new person.'},
   {'s': 'Many printers have a number pad for the copies.', 'ans': True, 'why': 'You press a number and then Start.'}],
  'wild': [
   {'kind': 'Printer screen', 'lines': ['**No paper**', 'Add paper to Tray 1', 'Then press OK'], 'decode': {'q': 'What do you do first?', 'opts': ['Add paper to the tray', 'Turn off the computer', 'Call the boss'], 'ans': 0, 'why': 'The screen says to add paper to Tray 1.'}},
   {'kind': 'Sign on the wall', 'lines': ['**Please do not leave pages here.**', 'Take your documents.', 'Ask Sam for paper.'], 'decode': {'q': 'Who can give you paper?', 'opts': ['Sam', 'The boss', 'Nobody'], 'ans': 0, 'why': '“Ask Sam for paper.”'}}],
  'compare': {'br': 'In Brazil many people print at a copy shop (a “copiadora”) near the office or school.', 'us': 'In the USA many offices have a printer for everyone, and people print their own pages.', 'tip': 'Take your pages quickly and add paper if the tray is empty. It is polite.', 'ask': 'Where do you print your documents? Say it in English.'},
  'quiz': [
   {'q': 'You do not know the printer. A natural question is…', 'opts': ['How do I use the printer?', 'I use printer you?', 'Printer is where?'], 'ans': 0, 'why': 'How do I + verb is the natural form.'},
   {'q': 'The screen says “No paper.” You…', 'opts': ['put paper in the tray', 'press Start again and again', 'throw the printer'], 'ans': 0, 'why': 'Paper goes in the tray.'},
   {'q': 'You want five copies. You press…', 'opts': ['the number five, then Start', 'the green light', 'Print five times'], 'ans': 0, 'why': 'Press the number, then Start.'}]},
 'reading': {'genre': 'Short story', 'title': 'Grace and the Printer',
  'text': ['It is Monday morning in **Boston**. Grace has a new job in a small office. Her boss wants a **document** on paper today. Grace has the file on her computer. But she does not know the printer.',
   'She goes to the printer room. A coworker, Quinn, is there. “**Excuse me, how do I use the printer?**” she asks. “**Click Print** on your computer,” Quinn says. “Then **press the green button**.” Grace goes back to her desk and clicks Print.',
   'Grace presses the green button. The screen says “No paper.” “**Let me help**,” Quinn says. He opens the **tray** and puts in new paper. “**Paper goes here**,” he says. The printer starts to make a noise.',
   'Now Grace needs more pages. “**I need five copies**,” she says. Quinn shows her the number pad. “**Press the number five, then Start.**” Grace smiles. “That is easy!”',
   'The printer works. Five pages come out, one by one. “**It works!** But where is my document?” Grace asks. Quinn laughs and points to the output tray. She takes the pages and uses a **stapler**. Now she can print alone, and she says thanks.'],
  'glossary': [{'w': 'office', 'pt': 'escritório'}, {'w': 'boss', 'pt': 'chefe'}, {'w': 'document', 'pt': 'documento'}, {'w': 'coworker', 'pt': 'colega de trabalho'}, {'w': 'desk', 'pt': 'mesa de trabalho'}, {'w': 'tray', 'pt': 'bandeja'}, {'w': 'noise', 'pt': 'barulho'}, {'w': 'pages', 'pt': 'páginas'}, {'w': 'stapler', 'pt': 'grampeador'}, {'w': 'alone', 'pt': 'sozinha'}],
  'fast': {'q': 'What is this text about?', 'opts': ['A new worker learns to use a printer', 'A trip to Boston', 'A job interview'], 'ans': 0, 'why': 'Grace learns to print at her new office.'},
  'scan': [{'q': 'Who helps Grace?', 'ans': 'Quinn', 'alt': ['quinn', 'a coworker']}, {'q': 'How many copies does Grace need?', 'ans': 'five', 'alt': ['5']}, {'q': 'What does the screen say?', 'ans': 'No paper', 'alt': ['no paper.']}],
  'tf': [{'s': 'Grace works in Boston.', 'ans': True, 'why': 'The story starts in Boston.'}, {'s': 'Quinn is Grace’s boss.', 'ans': False, 'why': 'Quinn is a coworker.'}, {'s': 'The printer has no paper at first.', 'ans': True, 'why': 'The screen says “No paper.”'}, {'s': 'Grace needs two copies.', 'ans': False, 'why': 'She needs five copies.'}],
  'order': ['Grace asks how to use the printer.', 'She clicks Print and presses the green button.', 'The screen says “No paper.”', 'Quinn puts paper in the tray.', 'Grace gets five copies.'],
  'ctx': [{'sent': 'Grace has a new job in a small office.', 'w': 'office', 'opts': ['a place to work', 'a kind of food', 'a bus'], 'ans': 0, 'why': 'An office is a place where people work.'}, {'sent': 'The printer starts to make a noise.', 'w': 'noise', 'opts': ['a sound', 'a color', 'a button'], 'ans': 0, 'why': 'Noise = sound.'}, {'sent': 'Now she can print alone.', 'w': 'alone', 'opts': ['without help', 'with a friend', 'very fast'], 'ans': 0, 'why': 'Alone = without other people.'}],
  'chunkHunt': ['How do I use the printer?', 'Click Print', 'Let me help.', 'I need five copies.'], 'think': 'What is hard for you in a new office? What can you ask a coworker?'},
 'convo': {'npc': {'name': 'Grace'}, 'story': 'You start a new job in an office in Boston. Grace is a coworker. You need to print a document.', 'turns': [
  {'npc': 'Hi! You look lost. Can I help?', 'pt': 'Oi! Você parece perdido. Posso ajudar?', 'opts': [
   {'en': 'I help you, thanks.', 'pt': 'Eu ajudo você, obrigado.', 'ok': False, 'fb': 'Wrong person: you need help.'},
   {'en': 'Yes, please. How do I use the printer?', 'pt': 'Sim, por favor. Como uso a impressora?', 'ok': True, 'fb': 'Clear and polite: How do I…?'},
   {'en': 'I am the printer.', 'pt': 'Eu sou a impressora.', 'ok': False, 'fb': 'This does not answer her.'}]},
  {'npc': 'Click Print on your computer. Then press the green button.', 'pt': 'Clique em Imprimir no computador. Depois aperte o botão verde.', 'opts': [
   {'en': 'No, I print the computer.', 'pt': 'Não, eu imprimo o computador.', 'ok': False, 'fb': 'You print a document, not the computer.'},
   {'en': 'The button is green yesterday.', 'pt': 'O botão é verde ontem.', 'ok': False, 'fb': 'Wrong tense and no sense here.'},
   {'en': 'Okay, thanks. I click Print first.', 'pt': 'Ok, obrigado. Eu clico em Imprimir primeiro.', 'ok': True, 'fb': 'You repeat the step to check.'}]},
  {'npc': 'What does the screen say?', 'pt': 'O que diz a tela?', 'opts': [
   {'en': 'It says “No paper.”', 'pt': 'Diz “Sem papel”.', 'ok': True, 'fb': 'It says + the message.'},
   {'en': 'Yes, it is a printer.', 'pt': 'Sim, é uma impressora.', 'ok': False, 'fb': 'She asks what the screen says.'},
   {'en': 'It says me no.', 'pt': 'Diz me não.', 'ok': False, 'fb': 'Use: It says “…”.'}]},
  {'npc': 'Paper goes in the tray. Do you need copies?', 'pt': 'O papel vai na bandeja. Você precisa de cópias?', 'opts': [
   {'en': 'Yes, I copy five.', 'pt': 'Sim, eu copio cinco.', 'ok': False, 'fb': 'Say: I need five copies.'},
   {'en': 'No, I am five.', 'pt': 'Não, eu sou cinco.', 'ok': False, 'fb': 'It does not answer the question.'},
   {'en': 'Yes, I need five copies.', 'pt': 'Sim, preciso de cinco cópias.', 'ok': True, 'fb': 'I need + number + copies.'}]},
  {'npc': 'Press the number five, then Start.', 'pt': 'Aperte o número cinco e depois Iniciar.', 'opts': [
   {'en': 'Thank you, I am welcome.', 'pt': 'Obrigado, eu sou bem-vindo.', 'ok': False, 'fb': 'You say “You are welcome” to others.'},
   {'en': 'It works! Thanks for your help!', 'pt': 'Funcionou! Obrigado pela ajuda!', 'ok': True, 'fb': 'Natural thanks after help.'},
   {'en': 'No, you press five.', 'pt': 'Não, você aperta cinco.', 'ok': False, 'fb': 'She is helping you.'}]}]},
 'homework': 'Look at a printer or a copy machine and say the steps in English: click, press, paper, start.',
 'homework_items': ['Say 3 steps to print a page.', 'Write: I need three copies, please.', 'Listen to the dialogue and shadow Grace.', 'Review: How do I use the printer? / Let me help. / It works!'],
 'errors': [
  {'wrong': 'How I use the printer?', 'fix': 'How do I use the printer?', 'alt': 'How do I using the printer?', 'why': 'Questions need do: How do I + verb?'},
  {'wrong': 'I need five copy.', 'fix': 'I need five copies.', 'alt': 'I need five copys.', 'why': 'More than one: copy becomes copies.'},
  {'wrong': 'Press in the button.', 'fix': 'Press the button.', 'alt': 'Press on the button green.', 'why': 'Press + the button, no preposition.'},
  {'wrong': 'Paper go here.', 'fix': 'Paper goes here.', 'alt': 'Paper is go here.', 'why': 'With paper (it), the verb takes -s: goes.'}]}
