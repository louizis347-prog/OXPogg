"""Suplemento Quest v5 · aula 34: Where is the milk? + regular At the Supermarket (Supermarket Flowers)."""
SUPP = {
 'reg': 70,
 'badge': {'icon': '🛒', 'name': 'Aisle Explorer', 'desc': 'Find products and give directions in a store in English'},
 'culture': {
  'hook': 'A big American supermarket can feel like a small town, with numbered aisles and signs everywhere. Learn how to find milk, bread and rice, and how to ask for help.',
  'mythfact': [
   {'s': 'In the USA, people push a “cart” in the supermarket.', 'ans': True, 'why': 'In British English the same thing is called a “trolley”.'},
   {'s': 'Aisles in a supermarket often have numbers and signs.', 'ans': True, 'why': 'The signs list the products, so you can find them quickly.'},
   {'s': 'Honolulu is in the state of Hawaii.', 'ans': True, 'why': 'Honolulu is the capital city of Hawaii, on the island of Oahu.'},
   {'s': 'Staff in a store are never happy to help.', 'ans': False, 'why': 'Asking “Excuse me, where is…?” is normal and polite.'},
   {'s': 'You must always pay a tip at the supermarket.', 'ans': False, 'why': 'Tips are for services like restaurants. At a supermarket, you do not tip.'}],
  'wild': [
   {'kind': 'Aisle sign', 'lines': ['**Aisle 3**  Milk · Eggs · Cheese', '**Aisle 4**  Bread · Cereal', '**Aisle 5**  Rice · Pasta'], 'decode': {'q': 'Where can you find rice?', 'opts': ['Aisle 5', 'Aisle 3', 'Aisle 4'], 'ans': 0, 'why': 'Rice is in Aisle 5.'}},
   {'kind': 'Store announcement', 'lines': ['Attention, shoppers!', 'Fresh bread is now ready in aisle 4.', 'Thank you for shopping with us.'], 'decode': {'q': 'What is ready now?', 'opts': ['Fresh bread', 'Fresh milk', 'Fresh rice'], 'ans': 0, 'why': '“Fresh bread is now ready in aisle 4.”'}}],
  'compare': {'br': 'In Brazil, people often say “Moço, onde fica o leite?” and the staff may walk with you to the shelf.', 'us': 'In the USA, a worker may point and say “Aisle three, on the left”, and the signs help you a lot.', 'tip': 'Use “Excuse me” first, then ask: Where is…? Do you have…?', 'ask': 'Where is the milk in your supermarket? Say it in English.'},
  'quiz': [
   {'q': 'You want to ask a worker for the milk. You say…', 'opts': ['Excuse me, where is the milk?', 'Where milk is?', 'I am the milk.'], 'ans': 0, 'why': 'Excuse me, where is…? is polite.'},
   {'q': '“It’s next to the milk.” Next to means…', 'opts': ['beside', 'inside', 'far from'], 'ans': 0, 'why': 'Next to = beside.'},
   {'q': 'Which is correct?', 'opts': ['Aisle five, on the left.', 'Aisle five in left on.', 'On the aisle left five.'], 'ans': 0, 'why': 'Say the aisle, then the side.'}]},
 'reading': {
  'genre': 'Blog post',
  'title': 'Lost in a big store',
  'text': [
   'Today I went shopping in **Honolulu**. The supermarket was huge, and I felt lost. I needed milk, bread and rice, but I did not know where they were.',
   'I saw a young worker. “**Excuse me, where is the milk?**” I asked. “**It’s in aisle three**,” she said. Then I asked, “**And where is the bread?**” “**It’s next to the milk**,” she said. That was easy!',
   'I pushed my cart and found the milk. It was cold and fresh. Then I asked, “**Do you have rice?**” She smiled. “**Yes, in aisle five, on the left.**” “**Thank you!**” I said. “**You’re welcome**,” she answered. “**Happy shopping!**”',
   'I thought about the song Supermarket Flowers by Ed Sheeran. The title is about a simple bunch of flowers from a supermarket. A big feeling can start in a very ordinary place. Today, my ordinary place was the aisle with the rice.',
   'My basket was ready: milk, bread and rice. I walked to the cashier, paid and went home. Next time I will not be lost. I know the words: aisle, left, right, next to.'],
  'glossary': [{'w': 'aisle', 'pt': 'corredor'}, {'w': 'lost', 'pt': 'perdido'}, {'w': 'huge', 'pt': 'enorme'}, {'w': 'worker', 'pt': 'funcionária'}, {'w': 'cart', 'pt': 'carrinho'}, {'w': 'left', 'pt': 'esquerda'}, {'w': 'rice', 'pt': 'arroz'}, {'w': 'basket', 'pt': 'cesta'}, {'w': 'cashier', 'pt': 'caixa'}],
  'fast': {'q': 'What is the writer doing?', 'opts': ['Finding things in a supermarket', 'Cooking dinner', 'Taking a bus'], 'ans': 0, 'why': 'The writer asks for milk, bread and rice.'},
  'scan': [{'q': 'Which aisle has the milk?', 'ans': 'aisle three', 'alt': ['three', '3', 'aisle 3']}, {'q': 'Where is the bread?', 'ans': 'next to the milk', 'alt': ['next to milk', 'beside the milk']}, {'q': 'Which side is the rice on?', 'ans': 'left', 'alt': ['on the left', 'the left']}],
  'tf': [{'s': 'The supermarket is very small.', 'ans': False, 'why': 'The supermarket was huge.'}, {'s': 'The rice is in aisle five.', 'ans': True, 'why': '“Yes, in aisle five, on the left.”'}, {'s': 'The writer does not need help.', 'ans': False, 'why': 'The writer asks the worker for help.'}, {'s': 'The writer buys milk, bread and rice.', 'ans': True, 'why': 'The last paragraph lists them.'}],
  'order': ['The writer feels lost in the supermarket.', 'The writer asks about the milk.', 'The worker says the bread is next to the milk.', 'The writer asks about rice.', 'The writer pays and goes home.'],
  'ctx': [{'sent': 'The store was huge and I felt lost.', 'w': 'huge', 'opts': ['very big', 'very cheap', 'very cold'], 'ans': 0, 'why': 'Huge = very big.'}, {'sent': 'The bread is next to the milk.', 'w': 'next to', 'opts': ['beside', 'behind', 'under'], 'ans': 0, 'why': 'Next to = beside.'}, {'sent': 'I put the milk in my basket.', 'w': 'basket', 'opts': ['a container for shopping', 'a shoe', 'a cold drink'], 'ans': 0, 'why': 'A basket holds things.'}],
  'chunkHunt': ['Excuse me, where is…?', 'It’s in aisle three.', 'Do you have…?', 'next to the milk'],
  'think': 'Do you ever get lost in a big store? What do you do?'},
 'convo': {'npc': {'name': 'Serena'}, 'story': 'You work in a store in Honolulu. A shopper named Serena asks where things are. Give clear directions.', 'turns': [
  {'npc': 'Excuse me, where is the milk?', 'pt': 'Com licença, onde fica o leite?', 'opts': [
   {'en': 'It’s in aisle three.', 'pt': 'Fica no corredor três.', 'ok': True, 'fb': 'It’s in + aisle number.'},
   {'en': 'It has aisle three.', 'pt': 'Tem corredor três.', 'ok': False, 'fb': 'Use It’s in aisle three.'},
   {'en': 'Yes, I like milk.', 'pt': 'Sim, eu gosto de leite.', 'ok': False, 'fb': 'It is not an answer to where.'}]},
  {'npc': 'And where is the bread?', 'pt': 'E onde fica o pão?', 'opts': [
   {'en': 'The bread is eating.', 'pt': 'O pão está comendo.', 'ok': False, 'fb': 'Wrong meaning.'},
   {'en': 'Aisle three and the bread.', 'pt': 'Corredor três e o pão.', 'ok': False, 'fb': 'Say It’s next to the milk.'},
   {'en': 'It’s next to the milk.', 'pt': 'Fica do lado do leite.', 'ok': True, 'fb': 'Next to = beside.'}]},
  {'npc': 'Thanks! Do you have rice?', 'pt': 'Valeu! Vocês têm arroz?', 'opts': [
   {'en': 'Yes, we do. Aisle five, on the left.', 'pt': 'Sim, temos. Corredor cinco, à esquerda.', 'ok': True, 'fb': 'Yes, we do + place.'},
   {'en': 'Yes, we have. Aisle five.', 'pt': 'Sim, nós temos. Corredor cinco.', 'ok': False, 'fb': 'Natural answer: Yes, we do.'},
   {'en': 'I am a worker.', 'pt': 'Eu sou funcionário.', 'ok': False, 'fb': 'It does not answer.'}]},
  {'npc': 'Great. Thank you!', 'pt': 'Ótimo. Obrigado!', 'opts': [
   {'en': 'Welcome you.', 'pt': 'Bem-vindo você.', 'ok': False, 'fb': 'Say You’re welcome.'},
   {'en': 'No problem, thanks.', 'pt': 'Sem problema, valeu.', 'ok': False, 'fb': 'Close, but the common answer is You’re welcome.'},
   {'en': 'You’re welcome.', 'pt': 'De nada.', 'ok': True, 'fb': 'The standard answer.'}]},
  {'npc': 'Happy shopping!', 'pt': 'Boas compras!', 'opts': [
   {'en': 'Thanks! Have a good day.', 'pt': 'Valeu! Tenha um bom dia.', 'ok': True, 'fb': 'Friendly and natural.'},
   {'en': 'I shop yesterday.', 'pt': 'Eu compro ontem.', 'ok': False, 'fb': 'Wrong tense.'},
   {'en': 'Good night.', 'pt': 'Boa noite.', 'ok': False, 'fb': 'It does not fit.'}]}]},
 'errors': [
  {'wrong': 'Where is located the milk?', 'fix': 'Where is the milk?', 'alt': 'Where the milk is?', 'why': 'In a question, put is before the noun: Where is the milk?'},
  {'wrong': 'It is in the aisle three.', 'fix': 'It’s in aisle three.', 'alt': 'It is on aisle three.', 'why': 'With an aisle number, do not use the.'},
  {'wrong': 'The bread is at side of the milk.', 'fix': 'The bread is next to the milk.', 'alt': 'The bread is near of the milk.', 'why': 'Say next to or beside. Not at side of.'},
  {'wrong': 'You have rice?', 'fix': 'Do you have rice?', 'alt': 'Have you rice?', 'why': 'Questions use Do you have…?'}],
 'homework': 'Draw a simple map of a store and write 4 sentences with where things are.',
 'homework_items': ['Draw a map of a small store with 3 aisles.', 'Write 4 sentences: It’s in aisle… / next to…', 'Listen to the dialogue again and shadow Serena.', 'Review: aisle / left / right / next to.']}
