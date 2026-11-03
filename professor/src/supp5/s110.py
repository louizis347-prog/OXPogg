"""Suplemento Quest v5 · aula 110: Send an email + regular Read a story, write a note"""
SUPP = {'reg': 126, 'badge': {'icon': '📧', 'name': 'Email Writer', 'desc': 'Write a short, polite work email in English'},
 'culture': {'hook': 'A good work email is short, clear and polite. Learn how to start, what to write, how to end and when to add an attachment, so your message gets a fast answer.',
  'mythfact': [
   {'s': 'A work email in the USA usually starts with “Hi” or “Hello” and the first name.', 'ans': True, 'why': 'First names are common at work, even with a manager.'},
   {'s': 'A good email is very long and has many topics.', 'ans': False, 'why': 'Short emails with one clear topic are easier to read.'},
   {'s': 'The subject line tells the reader what the email is about.', 'ans': True, 'why': 'A short subject helps people find the message later.'},
   {'s': 'You do not need to mention an attachment in the message.', 'ans': False, 'why': 'It is polite to say “I attached the report” so nobody misses it.'}],
  'wild': [
   {'kind': 'Email', 'lines': ['**Subject:** Report for Friday', 'Hello Marta,', 'I need the report by Friday. I attached the form.', 'Thank you, Victor'], 'decode': {'q': 'When does Victor need the report?', 'opts': ['By Friday', 'By Monday', 'Today only'], 'ans': 0, 'why': '“I need the report by Friday.”'}},
   {'kind': 'Auto-reply', 'lines': ['**I am out of the office until Monday.**', 'For urgent help, write to Sam.', 'Thank you.'], 'decode': {'q': 'Who can help with an urgent problem?', 'opts': ['Sam', 'The writer', 'Nobody'], 'ans': 0, 'why': '“For urgent help, write to Sam.”'}}],
  'compare': {'br': 'In Brazil work emails can be warm and a little long, often with “Prezados” or “Olá” and a polite opening.', 'us': 'In the USA work emails are usually short: a greeting, one or two clear sentences, thanks and a name.', 'tip': 'Put the main point in the first sentence. People often read emails fast.', 'ask': 'Write a one-sentence email to a coworker in English.'},
  'quiz': [
   {'q': 'You want to start an email to Marta. You write…', 'opts': ['Hello, Marta,', 'Marta is the Hello,', 'To the Marta,'], 'ans': 0, 'why': 'Hello + name, then a comma.'},
   {'q': 'The best way to end an email is…', 'opts': ['Thank you.', 'I am finished.', 'Goodbye, report.'], 'ans': 0, 'why': 'Thank you is polite and normal.'},
   {'q': 'You want to send a file with the email. You…', 'opts': ['add an attachment', 'write the file in the subject', 'send two emails'], 'ans': 0, 'why': 'You attach the file to the email.'}]},
 'reading': {'genre': 'Short story', 'title': 'Victor’s First Email',
  'text': ['Victor needs to write an **email** to his manager, Marta. It is his first email in English at work. He is not sure what to write, so he asks a coworker for help.',
   '“**Can you help me write an email?**” Victor asks. “**Sure. Who is it for?**” the coworker says. “**It’s for my manager.**” “OK. **Start with “Hello” and her name.**” Victor types, “Hello, Marta.” “**Then what?**” he asks.',
   '“**Write your message. Keep it short**,” the coworker says. Victor thinks for a minute. He writes, “**I need the report by Friday.**” Then he adds a short **subject**: “Report for Friday.”',
   '“Good. **End with “Thank you.”**” Victor types “Thank you” and his name. Then he asks, “**Do I add an attachment?**” “Yes,” says the coworker. “Click the paperclip and pick the file.” The **attachment** appears at the bottom of the message.',
   'Victor reads the email one more time. Then he clicks **send**. Ten minutes later, a new message is in his **inbox**. It is from Marta. She writes, “Thanks, Victor. I will **reply** with the details soon.” Victor smiles. His first work email in English is done.'],
  'glossary': [{'w': 'manager', 'pt': 'gerente'}, {'w': 'coworker', 'pt': 'colega de trabalho'}, {'w': 'message', 'pt': 'mensagem'}, {'w': 'subject', 'pt': 'assunto'}, {'w': 'report', 'pt': 'relatório'}, {'w': 'attachment', 'pt': 'anexo'}, {'w': 'paperclip', 'pt': 'clipe de papel'}, {'w': 'inbox', 'pt': 'caixa de entrada'}, {'w': 'reply', 'pt': 'responder'}, {'w': 'details', 'pt': 'detalhes'}],
  'fast': {'q': 'What is this text about?', 'opts': ['A man writes his first work email in English', 'A man calls his boss', 'A man prints a document'], 'ans': 0, 'why': 'Victor writes an email to Marta with help.'},
  'scan': [{'q': 'Who is the email for?', 'ans': 'Marta', 'alt': ['marta', 'his manager', 'the manager']}, {'q': 'When does Victor need the report?', 'ans': 'by Friday', 'alt': ['friday', 'Friday']}, {'q': 'How does Victor end the email?', 'ans': 'Thank you', 'alt': ['thank you.', 'with thank you']}],
  'tf': [{'s': 'Victor asks a coworker for help.', 'ans': True, 'why': '“Can you help me write an email?”'}, {'s': 'The email is for a client.', 'ans': False, 'why': 'It is for his manager.'}, {'s': 'Victor adds an attachment.', 'ans': True, 'why': 'The coworker tells him to click the paperclip.'}, {'s': 'Marta never answers.', 'ans': False, 'why': 'She replies after ten minutes.'}],
  'order': ['Victor asks a coworker for help.', 'He starts with Hello and Marta’s name.', 'He writes a short message.', 'He adds an attachment and clicks send.', 'Marta replies.'],
  'ctx': [{'sent': 'Victor adds a short subject.', 'w': 'subject', 'opts': ['a title for the email', 'a school class', 'a phone number'], 'ans': 0, 'why': 'The subject tells what the email is about.'}, {'sent': 'A new message is in his inbox.', 'w': 'inbox', 'opts': ['the place for new emails', 'a small box', 'a printer'], 'ans': 0, 'why': 'Inbox = where new emails arrive.'}, {'sent': 'She will reply soon.', 'w': 'reply', 'opts': ['answer', 'delete', 'forget'], 'ans': 0, 'why': 'Reply = answer a message.'}],
  'chunkHunt': ['Can you help me write an email?', 'Who is it for?', 'Keep it short.', 'Do I add an attachment?'], 'think': 'Who do you write emails to? What is hard to write in English?'},
 'convo': {'npc': {'name': 'Victor'}, 'story': 'You need to write an email to your manager. Victor, a coworker, can help you.', 'turns': [
  {'npc': 'Hi! Do you need help?', 'pt': 'Oi! Você precisa de ajuda?', 'opts': [
   {'en': 'Yes, I write email help.', 'pt': 'Sim, eu escrevo e-mail ajuda.', 'ok': False, 'fb': 'Wrong order. Say: Can you help me write an email?'},
   {'en': 'No, the email is me.', 'pt': 'Não, o e-mail sou eu.', 'ok': False, 'fb': 'Wrong meaning.'},
   {'en': 'Yes. Can you help me write an email?', 'pt': 'Sim. Pode me ajudar a escrever um e-mail?', 'ok': True, 'fb': 'Can you help me + verb is polite and clear.'}]},
  {'npc': 'Sure. Who is it for?', 'pt': 'Claro. Para quem é?', 'opts': [
   {'en': 'It’s for my manager.', 'pt': 'É para minha gerente.', 'ok': True, 'fb': 'It’s for + person.'},
   {'en': 'It’s for yesterday.', 'pt': 'É para ontem.', 'ok': False, 'fb': 'He asks who, not when.'},
   {'en': 'I am for my manager.', 'pt': 'Eu sou para minha gerente.', 'ok': False, 'fb': 'Use: It’s for…'}]},
  {'npc': 'OK. Start with “Hello” and her name.', 'pt': 'Ok. Comece com “Olá” e o nome dela.', 'opts': [
   {'en': 'Hello, Marta is then what.', 'pt': 'Olá, Marta é então o quê.', 'ok': False, 'fb': 'Not a real sentence.'},
   {'en': 'Hello, Marta. Then what?', 'pt': 'Olá, Marta. E depois?', 'ok': True, 'fb': 'Shows the step and asks for the next one.'},
   {'en': 'I start with Victor.', 'pt': 'Eu começo com Victor.', 'ok': False, 'fb': 'The email is for Marta.'}]},
  {'npc': 'Write your message. Keep it short.', 'pt': 'Escreva sua mensagem. Seja breve.', 'opts': [
   {'en': 'I need the report on Friday by.', 'pt': 'Preciso do relatório na sexta por.', 'ok': False, 'fb': 'Word order: by Friday.'},
   {'en': 'I need the report by Friday.', 'pt': 'Preciso do relatório até sexta.', 'ok': True, 'fb': 'Short, clear and with a deadline.'},
   {'en': 'I am the report Friday.', 'pt': 'Eu sou o relatório sexta.', 'ok': False, 'fb': 'Wrong meaning.'}]},
  {'npc': 'Good. End with “Thank you.”', 'pt': 'Boa. Termine com “Obrigado”.', 'opts': [
   {'en': 'I am add a attachment?', 'pt': 'Eu sou adicionar um anexo?', 'ok': False, 'fb': 'Use: Do I add an attachment?'},
   {'en': 'Yes, I add attachment you.', 'pt': 'Sim, eu adiciono anexo você.', 'ok': False, 'fb': 'Wrong word order.'},
   {'en': 'Okay. Do I add an attachment?', 'pt': 'Ok. Preciso anexar algo?', 'ok': True, 'fb': 'Natural question for the next step.'}]}]},
 'homework': 'Write a real or imaginary 3-line email in English to a coworker: greeting, one sentence, thank you.',
 'homework_items': ['Write an email: Hello + message + Thank you.', 'Say: Can you help me write an email? / Keep it short.', 'Listen to the dialogue and shadow Victor.', 'Review: Who is it for? / by Friday / attachment.'],
 'errors': [
  {'wrong': 'Can you help me to write an email?', 'fix': 'Can you help me write an email?', 'alt': 'Can you help me writing an email?', 'why': 'After help me, use the base verb: write.'},
  {'wrong': 'I need the report until Friday.', 'fix': 'I need the report by Friday.', 'alt': 'I need the report at Friday.', 'why': 'By = no later than.'},
  {'wrong': 'It is for my manager boss.', 'fix': 'It’s for my manager.', 'alt': 'It is to my manager.', 'why': 'Use: It’s for + person.'},
  {'wrong': 'I send the email for her.', 'fix': 'I send the email to her.', 'alt': 'I send to her the email.', 'why': 'You send something to someone.'}]}
