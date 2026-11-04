"""Suplemento Quest v5 · aula 191: A gift for a friend + regular Open the Book, Close the Door (Matilda)."""
SUPP = {
 'reg': 32,
 'badge': {'icon': '🎁', 'name': 'Gift Finder', 'desc': 'Ask for help and choose a gift for a friend'},
 'culture': {
  'hook': 'In the USA, a small gift for a birthday is common, and many shops will wrap it for you. Most people say what their friend likes and ask the clerk for ideas.',
  'mythfact': [
   {'s': 'A shop clerk in the USA often asks, “Can I help you find something?”', 'ans': True, 'why': 'It is a very common and friendly question.'},
   {'s': 'You must spend a lot of money on a birthday gift.', 'ans': False, 'why': 'A small, thoughtful gift is fine for most friends.'},
   {'s': 'Many shops sell gift bags or offer gift wrap.', 'ans': True, 'why': 'It is easy to find a bag or wrap for a present.'},
   {'s': 'A “gift receipt” shows the price to the person who gets the gift.', 'ans': False, 'why': 'It usually has no price, and it helps the person exchange the gift.'},
   {'s': '“Matilda” is a book by Roald Dahl.', 'ans': True, 'why': 'It was published in 1988, and a film came in 1996.'}],
  'wild': [
   {'kind': 'Sign in a gift shop', 'lines': ['**Gift wrap: $3**', 'Cards: $4', 'Bags: $2', 'Ask at the counter'], 'decode': {'q': 'How much is gift wrap?', 'opts': ['$3', '$4', '$2'], 'ans': 0, 'why': 'The sign says “Gift wrap: $3.”'}},
   {'kind': 'Shelf label', 'lines': ['**Books for kids**', 'Ages 6 to 10', 'All paperbacks $8', 'Aisle 2'], 'decode': {'q': 'Where are the kids’ books?', 'opts': ['Aisle 2', 'At the counter', 'Outside'], 'ans': 0, 'why': 'The label says “Aisle 2.”'}}],
  'compare': {'br': 'In Brazil, many people bring a gift to a birthday party and the shop often puts a pretty bow on it.', 'us': 'In the USA, people often bring a gift and a card, and a shop clerk may suggest ideas if you say what your friend likes.', 'tip': 'Say: “It’s for my best friend. She loves books.”', 'ask': 'What gift do you give to a friend? Say it in English.'},
  'quiz': [
   {'q': 'The clerk asks who the gift is for. You say…', 'opts': ['It’s for my best friend.', 'It is to my best friend.', 'It for best friend.'], 'ans': 0, 'why': 'It’s for + person.'},
   {'q': 'You say what your friend likes. You say…', 'opts': ['She loves books and tea.', 'She is loving books and tea.', 'She love books and tea.'], 'ans': 0, 'why': 'Love is a state verb, and she takes -s: loves.'},
   {'q': 'The clerk asks about money. He says…', 'opts': ['What’s your budget?', 'How is your budget?', 'Where is your budget?'], 'ans': 0, 'why': 'What’s your budget? asks how much you want to spend.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'A book and a mug',
  'text': ['Nora needs a **birthday gift** for her best friend, Tia. The party is on Saturday. Nora goes to a small shop in Austin. She is a little nervous because she has no idea.', 'A clerk named Leo smiles at her. “**Can I help you find something?**” “**Yes, I need a birthday gift.**” “**Who is it for?**” “**It’s for my best friend.**” “**What does she like?**” “**She loves books and tea.**”', '“**How about a book and a mug?**” Leo says. “**That’s a great idea**,” says Nora. Leo shows her a book about a girl with a special power. It is “Matilda,” a book by Roald Dahl from 1988. Matilda loves to read, just like Tia. Leo also adds a blue bookmark.', '“**What’s your budget?**” Leo asks. “About twenty dollars.” The book is twelve dollars, the mug is six and the bookmark is two. It is exactly twenty dollars!', 'Leo puts the things in a nice bag. “**Would you like a gift receipt?**” “Yes, please.” Nora pays and says, “Thanks for your help.” She is happy now, and Tia will love the gift.'],
  'glossary': [{'w': 'gift', 'pt': 'presente'}, {'w': 'shop', 'pt': 'loja'}, {'w': 'clerk', 'pt': 'atendente'}, {'w': 'mug', 'pt': 'caneca'}, {'w': 'budget', 'pt': 'orçamento'}, {'w': 'bookmark', 'pt': 'marcador de página'}, {'w': 'special', 'pt': 'especial'}, {'w': 'nervous', 'pt': 'nervosa'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A girl finds a gift for her friend', 'A girl sells books', 'A girl makes tea'], 'ans': 0, 'why': 'Nora needs a birthday gift for Tia.'},
  'scan': [{'q': 'Who is the gift for?', 'ans': 'Tia', 'alt': ['her best friend', 'her friend Tia']}, {'q': 'How much is the mug?', 'ans': 'six dollars', 'alt': ['$6', '6 dollars', 'six']}, {'q': 'What color is the bookmark?', 'ans': 'blue', 'alt': ['a blue bookmark']}],
  'tf': [{'s': 'The party is on Saturday.', 'ans': True, 'why': 'The story says the party is on Saturday.'}, {'s': 'Tia loves music and pizza.', 'ans': False, 'why': 'She loves books and tea.'}, {'s': 'Nora has about twenty dollars.', 'ans': True, 'why': 'Her budget is about twenty dollars.'}, {'s': 'Leo gives her the gift for free.', 'ans': False, 'why': 'Nora pays at the counter.'}],
  'order': ['Nora goes to a small shop.', 'Leo asks who the gift is for.', 'Leo suggests a book and a mug.', 'Leo asks about the budget.', 'Nora pays and takes the bag.'],
  'ctx': [{'sent': 'She is a little nervous.', 'w': 'nervous', 'opts': ['not calm', 'very tall', 'full'], 'ans': 0, 'why': 'Nervous means a little afraid or not calm.'}, {'sent': 'What’s your budget?', 'w': 'budget', 'opts': ['how much money you can spend', 'your favorite color', 'your phone number'], 'ans': 0, 'why': 'A budget is the money you plan to spend.'}, {'sent': 'Leo adds a blue bookmark.', 'w': 'bookmark', 'opts': ['a small thing to mark a page', 'a kind of tea', 'a bag for books'], 'ans': 0, 'why': 'You put a bookmark in a book.'}],
  'chunkHunt': ['Can I help you find something?', 'It’s for my best friend.', 'What’s your budget?', 'That’s a great idea.'],
  'think': 'What was the last gift you gave to a friend? What does your best friend like?'},
 'convo': {'npc': {'name': 'Leo'}, 'story': 'You are in a small gift shop. Leo works there and helps you find a birthday gift.', 'turns': [
  {'npc': 'Hi! Can I help you find something?', 'pt': 'Oi! Posso ajudar a achar algo?', 'opts': [
   {'en': 'Yes, I need a birthday gift.', 'pt': 'Sim, preciso de um presente de aniversário.', 'ok': True, 'fb': 'Clear and polite.'},
   {'en': 'Yes, I am needing a gift.', 'pt': 'Sim, estou precisando de um presente.', 'ok': False, 'fb': 'Need is a state verb: I need.'},
   {'en': 'No, thanks. I am fine.', 'pt': 'Não, obrigado. Estou bem.', 'ok': False, 'fb': 'It does not say what you want.'}]},
  {'npc': 'Who is it for?', 'pt': 'Para quem é?', 'opts': [
   {'en': 'It is for the shop.', 'pt': 'É para a loja.', 'ok': False, 'fb': 'It does not fit the question.'},
   {'en': 'It for my best friend.', 'pt': 'Para minha melhor amiga.', 'ok': False, 'fb': 'Use It’s: It’s for my best friend.'},
   {'en': 'It’s for my best friend.', 'pt': 'É para minha melhor amiga.', 'ok': True, 'fb': 'Perfect short answer.'}]},
  {'npc': 'What does she like?', 'pt': 'Do que ela gosta?', 'opts': [
   {'en': 'She loves books and tea.', 'pt': 'Ela adora livros e chá.', 'ok': True, 'fb': 'Loves + things she likes.'},
   {'en': 'She love books and tea.', 'pt': 'Ela adora livros e chá.', 'ok': False, 'fb': 'With she, use loves.'},
   {'en': 'She is tall and young.', 'pt': 'Ela é alta e jovem.', 'ok': False, 'fb': 'The question is about likes.'}]},
  {'npc': 'How about a book and a mug?', 'pt': 'Que tal um livro e uma caneca?', 'opts': [
   {'en': 'It is a book.', 'pt': 'É um livro.', 'ok': False, 'fb': 'It does not answer the idea.'},
   {'en': 'That’s a great idea.', 'pt': 'Ótima ideia.', 'ok': True, 'fb': 'A friendly way to say yes.'},
   {'en': 'That is a great idea, no.', 'pt': 'Ótima ideia, não.', 'ok': False, 'fb': 'It mixes yes and no.'}]},
  {'npc': 'What’s your budget?', 'pt': 'Qual é seu orçamento?', 'opts': [
   {'en': 'My budget is a mug.', 'pt': 'Meu orçamento é uma caneca.', 'ok': False, 'fb': 'Say an amount: about twenty dollars.'},
   {'en': 'About twenty dollars.', 'pt': 'Uns vinte dólares.', 'ok': True, 'fb': 'Gives a price.'},
   {'en': 'I am twenty dollars.', 'pt': 'Eu sou vinte dólares.', 'ok': False, 'fb': 'A person is not a price.'}]}]},
 'errors': [
  {'wrong': 'I am needing a gift.', 'fix': 'I need a gift.', 'alt': 'I needing a gift.', 'why': 'Need is a state verb: no -ing.'},
  {'wrong': 'It is to my friend.', 'fix': 'It’s for my friend.', 'alt': 'It for my friend.', 'why': 'Use for with the person who gets the gift.'},
  {'wrong': 'She love books.', 'fix': 'She loves books.', 'alt': 'She is love books.', 'why': 'He, she and it take -s: loves.'},
  {'wrong': 'I want a gift to my mother.', 'fix': 'I want a gift for my mother.', 'alt': 'I want a gift of my mother.', 'why': 'A gift for a person.'}],
 'homework': 'Write three lines: who the gift is for, what the person likes and your budget.',
 'homework_items': ['Write a gift idea for your best friend.', 'Say aloud: It’s for my best friend.', 'Listen to the dialogue and shadow Leo.', 'Review: gift / mug / book / budget.']}
