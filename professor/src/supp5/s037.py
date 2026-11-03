"""Suplemento Quest v5 · aula 37: Ice cream flavors + regular A scoop of vanilla (Sugar and Spice)."""
SUPP = {
 'reg': 137,
 'badge': {'icon': '🍦', 'name': 'Scoop Star', 'desc': 'Choose flavors, scoops and a cone or cup in English'},
 'culture': {
  'hook': 'An ice cream shop in Savannah gives you many small choices: flavor, number of scoops, and cup or cone. Learn to choose fast and enjoy it slowly.',
  'mythfact': [
   {'s': 'You can choose two different flavors in one order.', 'ans': True, 'why': 'Two scoops can be two flavors, like chocolate and strawberry.'},
   {'s': 'A “scoop” is one round ball of ice cream.', 'ans': True, 'why': 'The shop uses a scoop tool to make each ball.'},
   {'s': 'Savannah is in the state of Georgia.', 'ans': True, 'why': 'It is a historic port city, founded in 1733.'},
   {'s': 'A cone is the same as a cup.', 'ans': False, 'why': 'A cone is edible. A cup is a small container.'},
   {'s': '“Sugar and Spice” is a very old rhyme that is still repeated today.', 'ans': True, 'why': 'It comes from oral tradition and was printed in the early 1800s.'}],
  'wild': [
   {'kind': 'Ice cream menu', 'lines': ['**One scoop**  $3', '**Two scoops**  $4', '**Waffle cone**  +$1'], 'decode': {'q': 'How much are two scoops in a waffle cone?', 'opts': ['$5', '$4', '$3'], 'ans': 0, 'why': '$4 + $1 = $5.'}},
   {'kind': 'Flavor board', 'lines': ['Chocolate · Vanilla · Strawberry', 'Mint chip · Cookie dough', 'Sample a flavor? Just ask!'], 'decode': {'q': 'What can you ask for before you choose?', 'opts': ['A sample', 'A free cone', 'A discount'], 'ans': 0, 'why': '“Sample a flavor? Just ask!”'}}],
  'compare': {'br': 'In Brazil, you often choose a sorvete by weight in a self-serve shop, or an açaí bowl with toppings.', 'us': 'In the USA, many shops sell by the scoop, in a cup or a cone, and the server puts it together for you.', 'tip': 'Say the flavor first, then the number of scoops.', 'ask': 'What is your favorite flavor? Say it in English.'},
  'quiz': [
   {'q': 'The server asks: “One scoop or two?” You want two. You say…', 'opts': ['Two scoops, please.', 'Two scoop.', 'Scoops two me.'], 'ans': 0, 'why': 'Two scoops, please is natural.'},
   {'q': '“In a cup or a cone?” You choose a cone. You say…', 'opts': ['A cone, please.', 'In cone yes.', 'I cone.'], 'ans': 0, 'why': 'A + noun + please.'},
   {'q': 'What does “sweet tooth” mean?', 'opts': ['You love sweet food', 'Your tooth hurts', 'You do not eat sugar'], 'ans': 0, 'why': 'A sweet tooth = a love of sweets.'}]},
 'reading': {
  'genre': 'Diary',
  'title': 'A sweet afternoon',
  'text': [
   'It is a hot day in **Savannah**. My friend Tess and I walk past an old square. We see a small ice cream shop. I have a **sweet tooth**, so I say, “**Let’s go in!**”',
   'The server, Tiana, smiles. “**Hi! What flavor do you want?**” I say, “**Chocolate, please.**” “**One scoop or two?**” “**Two scoops. And strawberry.**” She asks, “**In a cup or a cone?**” “**A cone, please.**”',
   'Tiana makes the ice cream with a round tool. First chocolate, then strawberry. It looks great! “**That’s four dollars**,” she says. “**Here you go. Thanks!**” I say. “**Enjoy your ice cream!**” she says.',
   'Tess chooses vanilla in a cup. We sit on a bench and eat. The sun is hot, so the ice cream melts fast! We laugh and clean our hands with a napkin. “This is **so good**!” says Tess.',
   'I remember the old rhyme Sugar and Spice. It is a nice idea for a sweet day: sugar, cream and friends. A scoop of vanilla, a cherry on top. “**Why not?**” Tess says. “**Let’s get another.**”'],
  'glossary': [{'w': 'sweet tooth', 'pt': 'gosto por doces'}, {'w': 'flavor', 'pt': 'sabor'}, {'w': 'scoop', 'pt': 'bola (de sorvete)'}, {'w': 'cone', 'pt': 'casquinha'}, {'w': 'cup', 'pt': 'copinho'}, {'w': 'melts', 'pt': 'derrete'}, {'w': 'bench', 'pt': 'banco (de praça)'}, {'w': 'napkin', 'pt': 'guardanapo'}, {'w': 'vanilla', 'pt': 'baunilha'}],
  'fast': {'q': 'What is this diary about?', 'opts': ['Buying ice cream on a hot day', 'A school test', 'A bus trip'], 'ans': 0, 'why': 'The writer and Tess buy ice cream.'},
  'scan': [{'q': 'What flavors does the writer order?', 'ans': 'chocolate and strawberry', 'alt': ['chocolate strawberry', 'chocolate', 'strawberry']}, {'q': 'How much is the ice cream?', 'ans': '4 dollars', 'alt': ['four dollars', '$4', '4']}, {'q': 'What does Tess choose?', 'ans': 'vanilla in a cup', 'alt': ['vanilla', 'a cup']}],
  'tf': [{'s': 'The writer orders one scoop.', 'ans': False, 'why': 'The writer orders two scoops.'}, {'s': 'The writer chooses a cone.', 'ans': True, 'why': '“A cone, please.”'}, {'s': 'The weather is cold.', 'ans': False, 'why': 'It is a hot day.'}, {'s': 'Tess and the writer eat on a bench.', 'ans': True, 'why': 'They sit on a bench and eat.'}],
  'order': ['They walk past an old square.', 'The writer chooses chocolate and strawberry.', 'The writer asks for a cone.', 'The writer pays four dollars.', 'They eat on a bench.'],
  'ctx': [{'sent': 'The ice cream melts fast in the sun.', 'w': 'melts', 'opts': ['becomes liquid', 'becomes cold', 'becomes big'], 'ans': 0, 'why': 'Melt = change from solid to liquid.'}, {'sent': 'She has a sweet tooth.', 'w': 'sweet tooth', 'opts': ['loves sweets', 'has a sore tooth', 'hates sugar'], 'ans': 0, 'why': 'A sweet tooth = loves sweet foods.'}, {'sent': 'We sit on a bench in the shade.', 'w': 'bench', 'opts': ['a long seat', 'a cold drink', 'a small cup'], 'ans': 0, 'why': 'A bench is a long seat for people.'}],
  'chunkHunt': ['What flavor do you want?', 'One scoop or two?', 'In a cup or a cone?', 'That’s four dollars.'],
  'think': 'What is your favorite flavor? Do you like a cup or a cone?'},
 'convo': {'npc': {'name': 'Tiana'}, 'story': 'You are in an ice cream shop in Savannah. Tiana is the server. Pick your flavors, scoops and cone.', 'turns': [
  {'npc': 'Hi! What flavor do you want?', 'pt': 'Oi! Que sabor você quer?', 'opts': [
   {'en': 'Chocolate, please.', 'pt': 'Chocolate, por favor.', 'ok': True, 'fb': 'Flavor + please.'},
   {'en': 'I am chocolate.', 'pt': 'Eu sou chocolate.', 'ok': False, 'fb': 'Funny, but wrong.'},
   {'en': 'Yes, a flavor.', 'pt': 'Sim, um sabor.', 'ok': False, 'fb': 'Say the flavor you want.'}]},
  {'npc': 'One scoop or two?', 'pt': 'Uma bola ou duas?', 'opts': [
   {'en': 'Scoops two.', 'pt': 'Bolas duas.', 'ok': False, 'fb': 'Number first: Two scoops.'},
   {'en': 'I scoop yes.', 'pt': 'Eu bola sim.', 'ok': False, 'fb': 'It does not make sense.'},
   {'en': 'Two scoops. And strawberry.', 'pt': 'Duas bolas. E morango.', 'ok': True, 'fb': 'Add the second flavor.'}]},
  {'npc': 'In a cup or a cone?', 'pt': 'No copo ou na casquinha?', 'opts': [
   {'en': 'A cone, please.', 'pt': 'Na casquinha, por favor.', 'ok': True, 'fb': 'Clear and polite.'},
   {'en': 'In cone me.', 'pt': 'Em casquinha eu.', 'ok': False, 'fb': 'Say A cone, please.'},
   {'en': 'The cup yesterday.', 'pt': 'O copo ontem.', 'ok': False, 'fb': 'It does not match.'}]},
  {'npc': 'That’s four dollars.', 'pt': 'São quatro dólares.', 'opts': [
   {'en': 'Four dollars is hot.', 'pt': 'Quatro dólares é quente.', 'ok': False, 'fb': 'It does not make sense.'},
   {'en': 'I have not.', 'pt': 'Eu não tenho.', 'ok': False, 'fb': 'Say Here you go.'},
   {'en': 'Here you go. Thanks!', 'pt': 'Aqui está. Valeu!', 'ok': True, 'fb': 'Pay and thank.'}]},
  {'npc': 'Enjoy your ice cream!', 'pt': 'Aproveite o sorvete!', 'opts': [
   {'en': 'Thanks! You too!', 'pt': 'Valeu! Você também!', 'ok': True, 'fb': 'A warm answer.'},
   {'en': 'It is cold.', 'pt': 'Está frio.', 'ok': False, 'fb': 'It does not answer the wish.'},
   {'en': 'Good morning.', 'pt': 'Bom dia.', 'ok': False, 'fb': 'It does not fit.'}]}]},
 'errors': [
  {'wrong': 'Two scoop of chocolate.', 'fix': 'Two scoops of chocolate.', 'alt': 'Two scoops chocolate.', 'why': 'More than one scoop needs -s, and of connects scoops and flavor.'},
  {'wrong': 'I want the cone.', 'fix': 'A cone, please.', 'alt': 'I want a cone, please.', 'why': 'Use a for a first choice, and please for politeness.'},
  {'wrong': 'I am with a sweet tooth.', 'fix': 'I have a sweet tooth.', 'alt': 'I am a sweet tooth.', 'why': 'Use have for this expression.'},
  {'wrong': 'In a cone or in a cup?', 'fix': 'In a cup or a cone?', 'alt': 'Cup or a cone in?', 'why': 'Say in once, then list the choices.'}],
 'homework': 'Create an ice cream menu with 4 flavors and prices, then order from it aloud.',
 'homework_items': ['Write your dream ice cream: flavors, scoops, cup or cone.', 'Record the order using Two scoops, please.', 'Listen to the dialogue again and shadow Tiana.', 'Review: a scoop of / a bowl of / a cone.']}
