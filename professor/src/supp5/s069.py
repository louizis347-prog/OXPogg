"""Suplemento Quest v5 · aula 69: Borrowing sugar + regular Can I borrow your ladder? (Fantastic Mr. Fox)."""
SUPP = {
 'reg': 150,
 'badge': {'icon': '🤝', 'name': 'Good Neighbor', 'desc': 'Ask a favor, borrow something and thank your neighbor'},
 'culture': {
  'hook': 'Borrowing from a neighbor is a classic idea: a cup of sugar, a ladder, a tool. With a polite question and a warm thank you, it is easy in English.',
  'mythfact': [
   {'s': 'Memphis is a city in the state of Tennessee.', 'ans': True, 'why': 'Memphis is on the Mississippi River, in Tennessee.'},
   {'s': '“Borrow” and “lend” mean exactly the same thing.', 'ans': False, 'why': 'You borrow from someone, and someone lends to you.'},
   {'s': 'In English, “a cup of sugar” is a classic example of a small thing you ask a neighbor for.', 'ans': True, 'why': 'It is a popular image of friendly neighbors in the USA.'},
   {'s': 'When you borrow a ladder, you keep it forever.', 'ans': False, 'why': 'Borrowing means you give it back after use.'},
   {'s': '“Fantastic Mr. Fox” is based on a book by Roald Dahl.', 'ans': True, 'why': 'The 2009 film by Wes Anderson comes from Dahl\'s book.'}],
  'wild': [
   {'kind': 'Note on a door', 'lines': ['Hi neighbor!', '**Can I borrow a ladder** this weekend?', 'Thanks! — Apt 4B'], 'decode': {'q': 'What does the person want?', 'opts': ['A ladder for the weekend', 'Some sugar', 'A new door'], 'ans': 0, 'why': 'The note asks to borrow a ladder.'}},
   {'kind': 'Recipe card', 'lines': ['**Birthday cake**', '2 cups flour · 1 cup sugar', '3 eggs · 1 cup milk'], 'decode': {'q': 'How much sugar does the cake need?', 'opts': ['One cup', 'Two cups', 'Three cups'], 'ans': 0, 'why': '“1 cup sugar.”'}}],
  'compare': {'br': 'In Brazil, a neighbor often asks for “um pouquinho de açúcar” or lends a tool, and people drop by without much ceremony.', 'us': 'In the USA, neighbors also lend small things, but people usually ask first, thank you again later and often bring something back, like a slice of cake.', 'tip': 'Ask: “Can I borrow some sugar?” and end with “Thanks, you\'re a lifesaver!”', 'ask': 'What do you borrow from friends or neighbors? Say it in English.'},
  'quiz': [
   {'q': 'You need a favor from a neighbor. You say…', 'opts': ['Hi! Can I ask you a favor?', 'Hi! I ask a favor you.', 'Favor, neighbor, hello?'], 'ans': 0, 'why': 'Can I ask you a favor? is polite and natural.'},
   {'q': 'You want to use her sugar for a while. You say…', 'opts': ['Can I borrow some sugar?', 'Can I lend some sugar?', 'Can I borrow you?'], 'ans': 0, 'why': 'You borrow; the other person lends.'},
   {'q': '“You\'re a lifesaver!” means…', 'opts': ['You helped me a lot', 'You are a swimmer', 'You are late'], 'ans': 0, 'why': 'It is a friendly way to say thanks.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'A cup of sugar',
  'text': [
   'Saturday afternoon in **Memphis**. Miles wants to bake a birthday cake for his sister. He opens the sugar jar, but it is empty. “Oh no,” he says. The shop is far, so he goes next door.',
   'He rings the doorbell. Pearl opens the door. She is his neighbor, and she wears an apron. “Hi, Pearl! **Can I ask you a favor?**” “**Of course, honey. What is it?**” “**Can I borrow some sugar?**”',
   '“**Sure. How much do you need?**” “**Just one cup, please.**” Pearl goes to the kitchen and comes back with a cup of sugar. “**Here you go. Are you baking?**” “**Yes, a cake for tonight**,” Miles says. “It is my sister\'s birthday.”',
   '“**Nice! Save me a slice**,” says Pearl. “Of course! **Thanks again. You\'re a lifesaver!**” “**No big deal**,” she says. “That\'s what neighbors do.” Miles smiles. “**I owe you one**.”',
   'That night, Miles brings a big slice of cake to Pearl. He thinks of the film Fantastic Mr. Fox. In it, the animals ask for help: “Can I borrow your ladder?” Good neighbors lend and borrow things. Pearl smiles and says, “**Come by** later for coffee!”'],
  'glossary': [{'w': 'jar', 'pt': 'pote'}, {'w': 'empty', 'pt': 'vazio'}, {'w': 'doorbell', 'pt': 'campainha'}, {'w': 'apron', 'pt': 'avental'}, {'w': 'borrow', 'pt': 'pegar emprestado'}, {'w': 'favor', 'pt': 'favor'}, {'w': 'lifesaver', 'pt': 'salvador'}, {'w': 'slice', 'pt': 'fatia'}, {'w': 'ladder', 'pt': 'escada'}],
  'fast': {'q': 'What is this story about?', 'opts': ['Borrowing sugar from a neighbor', 'Buying a new house', 'A trip to Memphis'], 'ans': 0, 'why': 'Miles asks Pearl for sugar.'},
  'scan': [{'q': 'What does Miles want to bake?', 'ans': 'a birthday cake', 'alt': ['a cake', 'cake', 'birthday cake']}, {'q': 'How much sugar does he need?', 'ans': 'one cup', 'alt': ['1 cup', 'a cup']}, {'q': 'What does Pearl want?', 'ans': 'a slice of cake', 'alt': ['a slice', 'slice']}],
  'tf': [{'s': 'The sugar jar is full.', 'ans': False, 'why': 'The jar is empty.'}, {'s': 'Pearl is Miles\'s neighbor.', 'ans': True, 'why': 'He goes next door.'}, {'s': 'The cake is for Pearl\'s birthday.', 'ans': False, 'why': 'It is for Miles\'s sister.'}, {'s': 'Miles brings Pearl a slice of cake.', 'ans': True, 'why': 'He brings her a big slice that night.'}],
  'order': ['Miles opens the empty sugar jar.', 'He rings Pearl\'s doorbell.', 'He asks to borrow some sugar.', 'Pearl gives him one cup.', 'He brings her a slice of cake.'],
  'ctx': [{'sent': 'Can I borrow some sugar?', 'w': 'borrow', 'opts': ['use and give back', 'buy for ever', 'throw away'], 'ans': 0, 'why': 'Borrow = take for a short time.'}, {'sent': 'The jar is empty.', 'w': 'empty', 'opts': ['with nothing inside', 'very heavy', 'very big'], 'ans': 0, 'why': 'Empty = nothing inside.'}, {'sent': 'You\'re a lifesaver!', 'w': 'lifesaver', 'opts': ['a person who helps a lot', 'a swimmer', 'a baker'], 'ans': 0, 'why': 'It means you saved me.'}],
  'chunkHunt': ['Can I ask you a favor?', 'Can I borrow some sugar?', 'How much do you need?', 'You\'re a lifesaver!'],
  'think': 'What small thing can you borrow from a neighbor? What can you bring back to say thanks?'},
 'convo': {'npc': {'name': 'Pearl'}, 'story': 'You are Miles. Your sugar jar is empty and you need to bake a cake. Knock on your neighbor Pearl\'s door in Memphis.', 'turns': [
  {'npc': 'Hi, Miles! Come in.', 'pt': 'Oi, Miles! Entre.', 'opts': [
   {'en': 'Hi, Pearl! Can I ask you a favor?', 'pt': 'Oi, Pearl! Posso pedir um favor?', 'ok': True, 'fb': 'Polite way to start a request.'},
   {'en': 'Hi, Pearl! I do you a favor.', 'pt': 'Oi, Pearl! Eu faço você um favor.', 'ok': False, 'fb': 'Say ask you a favor.'},
   {'en': 'Goodbye, Pearl!', 'pt': 'Tchau, Pearl!', 'ok': False, 'fb': 'You just arrived.'}]},
  {'npc': 'Of course, honey. What is it?', 'pt': 'Claro, querido. O que é?', 'opts': [
   {'en': 'Can I lend some sugar?', 'pt': 'Posso emprestar um pouco de açúcar?', 'ok': False, 'fb': 'You borrow; she lends.'},
   {'en': 'Can I borrow some sugar?', 'pt': 'Posso pegar um pouco de açúcar emprestado?', 'ok': True, 'fb': 'Borrow is the right verb.'},
   {'en': 'I am a sugar, thanks.', 'pt': 'Eu sou um açúcar, valeu.', 'ok': False, 'fb': 'It does not make sense.'}]},
  {'npc': 'Sure. How much do you need?', 'pt': 'Claro. Quanto você precisa?', 'opts': [
   {'en': 'Just one cup, please.', 'pt': 'Só uma xícara, por favor.', 'ok': True, 'fb': 'Says the amount clearly.'},
   {'en': 'I need much, please.', 'pt': 'Preciso muito, por favor.', 'ok': False, 'fb': 'Say the amount: one cup.'},
   {'en': 'Yes, it is a cup.', 'pt': 'Sim, é uma xícara.', 'ok': False, 'fb': 'She asked how much, not yes or no.'}]},
  {'npc': 'Here you go. Are you baking?', 'pt': 'Aqui está. Você vai assar algo?', 'opts': [
   {'en': 'I am baking yesterday.', 'pt': 'Estou assando ontem.', 'ok': False, 'fb': 'Yesterday needs past: I baked.'},
   {'en': 'Yes, a cake for tonight.', 'pt': 'Sim, um bolo para hoje à noite.', 'ok': True, 'fb': 'Answers with what you make.'},
   {'en': 'No, I am the cake.', 'pt': 'Não, eu sou o bolo.', 'ok': False, 'fb': 'It does not make sense.'}]},
  {'npc': 'Nice! Save me a slice.', 'pt': 'Que bom! Guarde-me uma fatia.', 'opts': [
   {'en': 'Sure! Thanks again. You\'re a lifesaver!', 'pt': 'Claro! Valeu de novo. Você me salvou!', 'ok': True, 'fb': 'Agrees and thanks warmly.'},
   {'en': 'I save a slice you.', 'pt': 'Eu guardo uma fatia você.', 'ok': False, 'fb': 'Word order: save you a slice.'},
   {'en': 'No, the cake is not for you.', 'pt': 'Não, o bolo não é pra você.', 'ok': False, 'fb': 'Rude after her help.'}]}]},
 'errors': [
  {'wrong': 'Can I lend some sugar?', 'fix': 'Can I borrow some sugar?', 'alt': 'Can I borrow sugar to you?', 'why': 'You borrow from someone; the other person lends to you.'},
  {'wrong': 'Can I ask a favor you?', 'fix': 'Can I ask you a favor?', 'alt': 'Can I ask for you a favor?', 'why': 'Order: ask + person + favor.'},
  {'wrong': 'I need a sugar.', 'fix': 'I need some sugar.', 'alt': 'I need sugars.', 'why': 'Sugar is not counted here: use some.'},
  {'wrong': 'How many sugar do you need?', 'fix': 'How much sugar do you need?', 'alt': 'How much sugars do you need?', 'why': 'Use how much with things you do not count, like sugar.'}],
 'homework': 'Write a short note to a neighbor to borrow something: greet, ask the favor, say how much, and thank.',
 'homework_items': ['Say 3 things people often borrow.', 'Write: Can I borrow…? three times with different things.', 'Listen to the dialogue again and shadow Miles.', 'Review: Can I ask you a favor? / Here you go. / You\'re a lifesaver!']}
