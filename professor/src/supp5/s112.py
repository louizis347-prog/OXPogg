"""Suplemento Quest v5 · aula 112: The library card + regular A library card (Library Lion)."""
SUPP = {
 'reg': 173,
 'badge': {'icon': '📚', 'name': 'Card Holder', 'desc': 'Get a library card with ID, proof of address and a form'},
 'culture': {
  'hook': 'In the USA, a public library is a place for everyone. With a library card, you can borrow books, movies and more, and many libraries ask for an ID and proof of address.',
  'mythfact': [
   {'s': 'In many places, a public library card is free for local residents.', 'ans': True, 'why': 'Many public libraries give cards to residents at no cost; the rules can change by city.'},
   {'s': 'You can only borrow paper books with a library card.', 'ans': False, 'why': 'Many libraries also lend movies, music and e-books.'},
   {'s': 'Libraries often ask for a bill with your address.', 'ans': True, 'why': 'It is a common way to show where you live.'},
   {'s': 'You can keep a library book forever.', 'ans': False, 'why': 'Each item has a due date, and you return it or renew it.'},
   {'s': '“Library Lion” is a picture book from 2006.', 'ans': True, 'why': 'Michelle Knudsen wrote it, and it tells about a lion in a library.'}],
  'wild': [
   {'kind': 'Library sign', 'lines': ['**Quiet, please.**', 'Return books to the **book drop**.', 'Open Mon–Sat, 10 a.m. – 6 p.m.'], 'decode': {'q': 'Where do you put books you return?', 'opts': ['In the book drop', 'On a chair', 'In your bag'], 'ans': 0, 'why': '“Return books to the book drop.”'}},
   {'kind': 'Receipt from a library', 'lines': ['**Due date:** March 18', '3 books checked out', 'Renew online or call us.'], 'decode': {'q': 'What can you do before March 18?', 'opts': ['Renew online', 'Throw the books', 'Buy a card'], 'ans': 0, 'why': '“Renew online or call us.”'}}],
  'compare': {'br': 'No Brasil, muitas bibliotecas pedem comprovante de residência ou documento para a carteirinha.', 'us': 'Nos EUA, é comum levar um documento com foto e uma conta que mostre o endereço.', 'tip': 'Ask: “What do I need to get a card?”', 'ask': 'Do you have a library card? Which books do you like?'},
  'quiz': [
   {'q': 'You want a card. You say…', 'opts': ['I’d like a library card, please.', 'I want card of library.', 'Library card me now.'], 'ans': 0, 'why': 'I’d like… is polite and clear.'},
   {'q': 'What is a due date?', 'opts': ['The day you return the book', 'The day you buy the book', 'The name of the author'], 'ans': 0, 'why': 'Due date = the last day to return.'},
   {'q': 'What does “borrow” mean?', 'opts': ['take for a short time', 'buy forever', 'write a book'], 'ans': 0, 'why': 'You borrow a book and give it back.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Ana gets a card',
  'text': [
   'Ana lives in **Portland**. She loves stories, but books are expensive. A friend says, “Go to the library. It is free!” So Ana goes on Saturday morning.',
   'At the desk, a librarian smiles. “Hi! **I’d like a library card, please**,” Ana says. “**Sure. Do you have an ID?**” “Yes, here’s my passport.” “**And a bill with your address?**” “Here’s my phone bill.”',
   '“**Great. Please fill out this form**,” the librarian says. Ana writes her name, address and phone number. Then she asks, “**Is the card free?**” “**Yes, it’s free.**” “**Here’s your card.**” Ana is very happy.',
   'Ana walks through the shelves. She remembers “Library Lion,” a picture book from 2006. In the story, a lion comes to the library and learns the rules. He must be quiet, and he likes story time. Ana laughs and thinks, “I follow the rules too.”',
   'She borrows three books. The due date is on the receipt. “I can renew online,” the librarian says. Ana puts the books in her bag and says, “Thank you! I’ll be back next week.”'],
  'glossary': [{'w': 'library', 'pt': 'biblioteca'}, {'w': 'librarian', 'pt': 'bibliotecário(a)'}, {'w': 'ID', 'pt': 'documento de identidade'}, {'w': 'bill', 'pt': 'conta'}, {'w': 'address', 'pt': 'endereço'}, {'w': 'form', 'pt': 'formulário'}, {'w': 'borrows', 'pt': 'pega emprestado'}, {'w': 'due date', 'pt': 'data de devolução'}, {'w': 'renew', 'pt': 'renovar'}, {'w': 'shelves', 'pt': 'prateleiras'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A woman gets a library card', 'A man buys a car', 'A girl cooks dinner'], 'ans': 0, 'why': 'Ana gets her card at the library.'},
  'scan': [{'q': 'What ID does Ana show?', 'ans': 'her passport', 'alt': ['passport', 'a passport']}, {'q': 'What bill does she show?', 'ans': 'her phone bill', 'alt': ['phone bill', 'a phone bill']}, {'q': 'How many books does Ana borrow?', 'ans': 'three', 'alt': ['3', 'three books']}],
  'tf': [{'s': 'The library card is free for Ana.', 'ans': True, 'why': 'The librarian says, “Yes, it’s free.”'}, {'s': 'Ana goes to the library on Monday.', 'ans': False, 'why': 'She goes on Saturday morning.'}, {'s': 'Ana fills out a form.', 'ans': True, 'why': 'She writes her name, address and phone number.'}, {'s': 'Ana can renew the books online.', 'ans': True, 'why': 'The librarian says she can renew online.'}],
  'order': ['Ana goes to the library.', 'She shows her passport and phone bill.', 'She fills out the form.', 'She gets her card.', 'She borrows three books.'],
  'ctx': [{'sent': 'Ana borrows three books.', 'w': 'borrows', 'opts': ['takes for a short time', 'buys for a lot', 'writes'], 'ans': 0, 'why': 'Borrow = take and return later.'}, {'sent': 'The due date is on the receipt.', 'w': 'due date', 'opts': ['the day to return it', 'the price', 'the author’s name'], 'ans': 0, 'why': 'Due date = last day to return.'}, {'sent': 'I can renew online.', 'w': 'renew', 'opts': ['keep it longer', 'throw it away', 'read it fast'], 'ans': 0, 'why': 'Renew = extend the time.'}],
  'chunkHunt': ['I’d like a library card, please.', 'Do you have an ID?', 'Please fill out this form.', 'Is the card free?'],
  'think': 'What kind of books do you like to borrow?'},
 'convo': {'npc': {'name': 'Ms. Hill'}, 'story': 'You want a library card. Ms. Hill works at the desk and helps you.', 'turns': [
  {'npc': 'Hi! Can I help you?', 'pt': 'Oi! Posso ajudar?', 'opts': [
   {'en': 'Yes. I’d like a library card, please.', 'pt': 'Sim. Eu gostaria de uma carteirinha da biblioteca, por favor.', 'ok': True, 'fb': 'Polite request.'},
   {'en': 'Yes. I want a card of library.', 'pt': 'Sim. Quero uma carteirinha de biblioteca.', 'ok': False, 'fb': 'Say a library card.'},
   {'en': 'No, I have a book.', 'pt': 'Não, eu tenho um livro.', 'ok': False, 'fb': 'Does not answer her question.'}]},
  {'npc': 'Sure. Do you have an ID?', 'pt': 'Claro. Você tem um documento?', 'opts': [
   {'en': 'I am ID.', 'pt': 'Eu sou documento.', 'ok': False, 'fb': 'Wrong meaning.'},
   {'en': 'Yes, here’s my passport.', 'pt': 'Tenho, aqui está meu passaporte.', 'ok': True, 'fb': 'Shows an ID.'},
   {'en': 'Yes, I have a card.', 'pt': 'Sim, eu tenho uma carteirinha.', 'ok': False, 'fb': 'You want the card; you do not have it.'}]},
  {'npc': 'And a bill with your address?', 'pt': 'E uma conta com seu endereço?', 'opts': [
   {'en': 'Here’s my phone bill.', 'pt': 'Aqui está minha conta de telefone.', 'ok': True, 'fb': 'A bill with an address.'},
   {'en': 'My address is a bill.', 'pt': 'Meu endereço é uma conta.', 'ok': False, 'fb': 'It does not make sense.'},
   {'en': 'I pay the bill tomorrow.', 'pt': 'Pago a conta amanhã.', 'ok': False, 'fb': 'She wants to see the bill.'}]},
  {'npc': 'Great. Please fill out this form.', 'pt': 'Ótimo. Preencha este formulário.', 'opts': [
   {'en': 'OK. Is the card free?', 'pt': 'Ok. A carteirinha é grátis?', 'ok': True, 'fb': 'A useful question.'},
   {'en': 'OK. I fill the form out the card.', 'pt': 'Ok. Eu preencho o formulário da carteirinha.', 'ok': False, 'fb': 'Grammar problem.'},
   {'en': 'OK. Here’s your card.', 'pt': 'Ok. Aqui está sua carteirinha.', 'ok': False, 'fb': 'She gives you the card.'}]},
  {'npc': 'Yes, it’s free. Here’s your card.', 'pt': 'Sim, é grátis. Aqui está sua carteirinha.', 'opts': [
   {'en': 'Thank you very much!', 'pt': 'Muito obrigado!', 'ok': True, 'fb': 'Natural thanks.'},
   {'en': 'Yes, it is free.', 'pt': 'Sim, é grátis.', 'ok': False, 'fb': 'Does not fit; she said that.'},
   {'en': 'Fill out this form.', 'pt': 'Preencha este formulário.', 'ok': False, 'fb': 'You already filled it out.'}]}]},
 'errors': [
  {'wrong': 'I want a card of library.', 'fix': 'I want a library card.', 'alt': 'I want a library of card.', 'why': 'In English, the first word describes the second: a library card.'},
  {'wrong': 'I have 20 years and no ID.', 'fix': 'I’m 20 and I have no ID.', 'alt': 'I have 20 years old.', 'why': 'In English, we use I’m + age, not “have”.'},
  {'wrong': 'I need to borrow a book to you.', 'fix': 'Can I borrow a book?', 'alt': 'Can I borrow a book of you?', 'why': 'Borrow a book is enough; no “to you”.'},
  {'wrong': 'The card is for free?', 'fix': 'Is the card free?', 'alt': 'Is free the card?', 'why': 'Question: Is + thing + free?'}],
 'homework': 'Write a short dialogue: you ask for a library card and ask if it is free.',
 'homework_items': ['Write the 3 things you need for a library card.', 'Say aloud: Is the card free?', 'Listen to the dialogue and shadow the librarian.', 'Review: borrow / return / renew.']}
