"""Suplemento Quest v5 · aula 33: At the bakery + regular Flour for the bread (The Little Red Hen)."""
SUPP = {
 'reg': 101,
 'badge': {'icon': '🍞', 'name': 'Bakery Buddy', 'desc': 'Ask the price, choose and pay at a bakery in English'},
 'culture': {
  'hook': 'A neighborhood bakery in Brooklyn smells like warm bread and sugar. Learn the words you need to ask the price, choose and pay.',
  'mythfact': [
   {'s': 'In the USA, the price on a shelf usually does not include sales tax.', 'ans': True, 'why': 'In most states, sales tax is added when you pay.'},
   {'s': 'Bakeries only sell bread.', 'ans': False, 'why': 'Most also sell cookies, cakes, croissants and coffee.'},
   {'s': 'Brooklyn is a part of New York City.', 'ans': True, 'why': 'Brooklyn is one of the five boroughs of New York City.'},
   {'s': 'You say “a bread” to ask for one loaf.', 'ans': False, 'why': 'Bread is uncountable. Say “a loaf of bread”.'},
   {'s': '“The Little Red Hen” is a folk tale with no known author.', 'ans': True, 'why': 'It comes from oral tradition and many people tell it.'}],
  'wild': [
   {'kind': 'Bakery price board', 'lines': ['**Bread**  $4 a loaf', '**Cookie**  $1.50 each', '**Croissant**  $3'], 'decode': {'q': 'How much are two cookies?', 'opts': ['$3', '$1.50', '$4'], 'ans': 0, 'why': '2 x $1.50 = $3.'}},
   {'kind': 'Sign on the door', 'lines': ['Fresh bread every morning!', 'Open 7 a.m. to 3 p.m.', 'Closed on Mondays.'], 'decode': {'q': 'When is the bakery closed?', 'opts': ['On Mondays', 'Every morning', 'At 7 a.m.'], 'ans': 0, 'why': '“Closed on Mondays.”'}}],
  'compare': {'br': 'In Brazil, the padaria is part of daily life: people go early for pão francês and coffee, often buying by unit or by weight.', 'us': 'In the USA, many people buy a whole loaf, or a few cookies, and the shop may be smaller and more focused on sweets.', 'tip': 'To count bread, use “a loaf of bread”, “two loaves of bread”.', 'ask': 'What do you buy at the bakery? Say it in English.'},
  'quiz': [
   {'q': 'You want to know the price of the bread. You say…', 'opts': ['How much is the bread?', 'How many is the bread?', 'What is bread price?'], 'ans': 0, 'why': 'How much is…? asks for a price.'},
   {'q': 'You want one loaf. You say…', 'opts': ['I’ll take one, please.', 'I take bread one.', 'One me, please.'], 'ans': 0, 'why': 'I’ll take one, please is natural.'},
   {'q': '“That’s six dollars.” Then you…', 'opts': ['pay and say Here you go', 'say Good night', 'walk away'], 'ans': 0, 'why': 'Give the money and say Here you go.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'A loaf for Anya',
  'text': [
   'Anya lives in **Brooklyn**. On Saturday, she wants to make a sandwich for her little brother. She needs one thing: fresh bread. She goes to the bakery on her street.',
   'The bakery is warm and smells sweet. Ava works at the counter. “Hi! **Can I help you?**” she asks. Anya says, “Yes. **How much is the bread?**” “**Four dollars a loaf**,” says Ava. “**I’ll take one, please.**”',
   '“**Anything else?** The cookies are **fresh**,” says Ava. Anya looks at the cakes, the croissants and the cookies. They all look great. “**Two cookies, please**,” she says. “**That’s six dollars.**”',
   'Anya gives Ava the money. “**Here you go. Thanks!**” “**Have a sweet day!**” says Ava. Anya smiles and leaves with a loaf of bread and two cookies.',
   'At home, Anya remembers the story of the Little Red Hen. The hen makes flour and then bread, all alone. Anya is lucky: she only needs a few dollars and a short walk. She shares a cookie with her brother. “You bet it’s good!” he says.'],
  'glossary': [{'w': 'bakery', 'pt': 'padaria'}, {'w': 'counter', 'pt': 'balcão'}, {'w': 'loaf', 'pt': 'pão (unidade)'}, {'w': 'fresh', 'pt': 'fresco'}, {'w': 'cookies', 'pt': 'biscoitos'}, {'w': 'croissants', 'pt': 'croissants'}, {'w': 'cakes', 'pt': 'bolos'}, {'w': 'flour', 'pt': 'farinha'}, {'w': 'dollars', 'pt': 'dólares'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A girl buys bread and cookies', 'A boy plays soccer', 'A family travels by train'], 'ans': 0, 'why': 'Anya buys bread and two cookies.'},
  'scan': [{'q': 'How much is one loaf of bread?', 'ans': '4 dollars', 'alt': ['four dollars', '$4', '4']}, {'q': 'How many cookies does Anya buy?', 'ans': 'two', 'alt': ['2', 'two cookies']}, {'q': 'What is the total?', 'ans': '6 dollars', 'alt': ['six dollars', '$6', '6']}],
  'tf': [{'s': 'Anya lives in Brooklyn.', 'ans': True, 'why': 'The first line says she lives in Brooklyn.'}, {'s': 'The bread costs six dollars.', 'ans': False, 'why': 'The bread is four dollars. The total is six.'}, {'s': 'Ava works at the counter.', 'ans': True, 'why': 'Ava is at the counter of the bakery.'}, {'s': 'Anya eats all the cookies alone.', 'ans': False, 'why': 'She shares a cookie with her brother.'}],
  'order': ['Anya goes to the bakery.', 'She asks the price of the bread.', 'She buys two cookies.', 'She pays six dollars.', 'She shares a cookie at home.'],
  'ctx': [{'sent': 'The cookies are fresh today.', 'w': 'fresh', 'opts': ['new and just made', 'very old', 'very big'], 'ans': 0, 'why': 'Fresh = just made.'}, {'sent': 'Anya looks at the cakes.', 'w': 'cakes', 'opts': ['sweet baked food', 'bus tickets', 'shoes'], 'ans': 0, 'why': 'Cakes are sweet baked foods.'}, {'sent': 'Anya is lucky: she only needs a short walk.', 'w': 'lucky', 'opts': ['has good fortune', 'is tired', 'is lost'], 'ans': 0, 'why': 'Lucky = having good luck.'}],
  'chunkHunt': ['How much is the bread?', 'I’ll take one, please.', 'Anything else?', 'Here you go.'],
  'think': 'What is your favorite thing at the bakery? How much is it where you live?'},
 'convo': {'npc': {'name': 'Ava'}, 'story': 'You are at a bakery in Brooklyn. Ava works at the counter. Buy bread and cookies.', 'turns': [
  {'npc': 'Hi! Can I help you?', 'pt': 'Oi! Posso ajudar?', 'opts': [
   {'en': 'Yes. How much is the bread?', 'pt': 'Sim. Quanto custa o pão?', 'ok': True, 'fb': 'How much is…? asks the price.'},
   {'en': 'Yes. How many is the bread?', 'pt': 'Sim. Quantos é o pão?', 'ok': False, 'fb': 'Use How much for price.'},
   {'en': 'Yes, I help you.', 'pt': 'Sim, eu ajudo você.', 'ok': False, 'fb': 'Wrong meaning.'}]},
  {'npc': 'Four dollars a loaf.', 'pt': 'Quatro dólares o pão.', 'opts': [
   {'en': 'I take it one.', 'pt': 'Eu levo um.', 'ok': False, 'fb': 'Say I’ll take one, please.'},
   {'en': 'It is four years.', 'pt': 'São quatro anos.', 'ok': False, 'fb': 'Years are not dollars.'},
   {'en': 'I’ll take one, please.', 'pt': 'Vou levar um, por favor.', 'ok': True, 'fb': 'Natural and polite.'}]},
  {'npc': 'Anything else? The cookies are fresh.', 'pt': 'Mais alguma coisa? Os biscoitos são frescos.', 'opts': [
   {'en': 'Two cookies, please.', 'pt': 'Dois biscoitos, por favor.', 'ok': True, 'fb': 'Number + noun + please.'},
   {'en': 'Cookie two.', 'pt': 'Biscoito dois.', 'ok': False, 'fb': 'Put the number first.'},
   {'en': 'I am a cookie.', 'pt': 'Eu sou um biscoito.', 'ok': False, 'fb': 'Funny, but wrong.'}]},
  {'npc': 'That’s six dollars.', 'pt': 'São seis dólares.', 'opts': [
   {'en': 'Sorry, I no money.', 'pt': 'Desculpe, eu sem dinheiro.', 'ok': False, 'fb': 'Say I don’t have any money.'},
   {'en': 'Six dollars is me.', 'pt': 'Seis dólares sou eu.', 'ok': False, 'fb': 'Wrong meaning.'},
   {'en': 'Here you go. Thanks!', 'pt': 'Aqui está. Valeu!', 'ok': True, 'fb': 'Pay and thank.'}]},
  {'npc': 'Have a sweet day!', 'pt': 'Tenha um dia doce!', 'opts': [
   {'en': 'You too! Bye!', 'pt': 'Você também! Tchau!', 'ok': True, 'fb': 'The natural answer.'},
   {'en': 'It is not sweet.', 'pt': 'Não é doce.', 'ok': False, 'fb': 'Too literal.'},
   {'en': 'Yes, I have.', 'pt': 'Sim, eu tenho.', 'ok': False, 'fb': 'It does not answer the wish.'}]}]},
 'errors': [
  {'wrong': 'How many costs the bread?', 'fix': 'How much is the bread?', 'alt': 'How much costs the bread?', 'why': 'For price, say How much is…?'},
  {'wrong': 'I want one bread.', 'fix': 'I’ll take a loaf of bread.', 'alt': 'I want a breads.', 'why': 'Bread is uncountable. Use a loaf of.'},
  {'wrong': 'Two cookie, please.', 'fix': 'Two cookies, please.', 'alt': 'Cookies two, please.', 'why': 'More than one noun needs -s.'},
  {'wrong': 'Is four dollars the loaf.', 'fix': 'It’s four dollars a loaf.', 'alt': 'Four dollars for loaf.', 'why': 'The price pattern is It’s … dollars a loaf.'}],
 'homework': 'Write a short price list for your own bakery and say it aloud in English.',
 'homework_items': ['Write 4 items with prices (bread, cookies…).', 'Record yourself asking How much is…?', 'Listen to the dialogue again and shadow Ava.', 'Review: a loaf of / a bag of / a box of.']}
