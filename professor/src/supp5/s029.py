"""Suplemento Quest v5 · aula 29: Vegetarian options + regular At the Supermarket (Supermarket Flowers)."""
SUPP = {
 'reg': 70,
 'badge': {'icon': '🥗', 'name': 'Veggie Chooser', 'desc': 'Ask for vegetarian food and say what you do not eat'},
 'sticker': {'cat': 'Everyday culture', 'title': 'Vegetarian in Portland', 'sub': 'Is there meat in it?'},
 'culture': {
  'hook': 'Portland, Oregon, is known for food carts and for restaurants with many vegetarian dishes. Learn the words that help you choose food with no meat.',
  'polite': 'Ask **Do you have vegetarian dishes?** and **Is there meat in it?** Then say **Thank you, that’s perfect.**',
  'mythfact': [
   {'s': 'A vegetarian does not eat meat.', 'ans': True, 'why': 'Many vegetarians still eat eggs, milk and cheese.'},
   {'s': 'Vegetarian and vegan mean exactly the same thing.', 'ans': False, 'why': 'Vegans also avoid eggs, milk, cheese and honey.'},
   {'s': 'Many US menus mark vegetarian dishes with a letter like “V”.', 'ans': True, 'why': 'A small V or a leaf symbol is a common sign.'},
   {'s': 'Portland is a city in Oregon.', 'ans': True, 'why': 'There is also a city called Portland in Maine.'},
   {'s': 'Restaurants in the USA never offer a veggie burger.', 'ans': False, 'why': 'A veggie burger is a common option on menus.'}],
  'wild': [
   {'kind': 'Restaurant menu', 'lines': ['**Tomato pasta (V)**  $11', '**Chicken salad**  $12', '**Veggie burger (V)**  $10'], 'decode': {'q': 'Which dishes have no meat?', 'opts': ['Chicken salad and pasta', 'Pasta and veggie burger', 'Chicken salad and burger'], 'ans': 1, 'why': 'The (V) dishes are the vegetarian ones.'}},
   {'kind': 'Server’s question card', 'lines': ['**Allergies?** · **Diet?**', '[ ] Vegetarian', '[ ] No fish', '[ ] Gluten-free'], 'decode': {'q': 'What is this card asking?', 'opts': ['What you eat or can’t eat', 'Your name', 'Your address'], 'ans': 0, 'why': 'It asks about diets and allergies.'}}],
  'compare': {'br': 'In Brazil, “sem carne” can be a surprise in a churrascaria, but vegetarian options are growing, with “prato vegetariano” at many places.', 'us': 'In the USA, restaurants often mark vegetarian and vegan dishes, and servers are used to the question “Is there meat in it?”', 'tip': 'Say what you don’t eat: “I don’t eat meat or fish.”', 'ask': 'Do you know a vegetarian dish from your country? Say it in English.'},
  'quiz': [
   {'q': 'You want to ask about meat. You say…', 'opts': ['Is there meat in it?', 'Meat is there in?', 'It has meat me?'], 'ans': 0, 'why': 'Is there… in it? is natural.'},
   {'q': 'You don’t eat meat. You say…', 'opts': ['I don’t eat meat.', 'I no meat eat.', 'I am meat.'], 'ans': 0, 'why': 'Don’t + base verb.'},
   {'q': 'A “veggie burger” has…', 'opts': ['Vegetables or beans, no meat', 'Beef', 'Fish'], 'ans': 0, 'why': 'It is a burger without meat.'}]},
 'reading': {
  'genre': 'Blog post', 'title': 'No meat, please!',
  'text': [
   'My friend Carlos lives in **Portland**, and he doesn’t eat meat or fish. When we go to a restaurant, he always asks, “**Do you have vegetarian dishes?**”',
   'Last Saturday, we went to a small restaurant. The server said, “Yes, we do. **The pasta is vegetarian.**” Carlos asked, “**Is there meat in it?**” “**No meat**,” she said. “Just tomato and cheese. **We have a veggie burger too.**” Carlos smiled. “**I’ll have the pasta**, please.” “**Good choice!**” she said.',
   'My order was different. I had chicken and rice, and a glass of water. We shared a big salad: lettuce, tomato, cucumber and carrots. We said, “**Great idea!**” and “**Yum!**”',
   'After lunch, we went to the supermarket. Carlos wanted some vegetables, and I wanted flowers for my mother. I thought of the song “Supermarket Flowers” by Ed Sheeran, from 2017. It is a gentle song about love for a family member, and it is named after simple flowers from a supermarket.',
   'In the evening, I thought about our day. It is easy to eat with friends who have a different diet. You just ask a question, listen to the answer, and **enjoy your meal**.'],
  'glossary': [{'w': 'vegetarian', 'pt': 'vegetariano'}, {'w': 'meat', 'pt': 'carne'}, {'w': 'fish', 'pt': 'peixe'}, {'w': 'dishes', 'pt': 'pratos'}, {'w': 'pasta', 'pt': 'massa'}, {'w': 'veggie burger', 'pt': 'hambúrguer de legumes'}, {'w': 'cucumber', 'pt': 'pepino'}, {'w': 'supermarket', 'pt': 'supermercado'}, {'w': 'gentle', 'pt': 'suave'}, {'w': 'diet', 'pt': 'dieta'}],
  'fast': {'q': 'What is this text about?', 'opts': ['Eating out with a vegetarian friend', 'A flight to Texas', 'A new phone'], 'ans': 0, 'why': 'Carlos is vegetarian and orders pasta.'},
  'scan': [{'q': 'Where does Carlos live?', 'ans': 'Portland', 'alt': ['in portland']}, {'q': 'What does Carlos order?', 'ans': 'the pasta', 'alt': ['pasta']}, {'q': 'Who sings “Supermarket Flowers”?', 'ans': 'Ed Sheeran', 'alt': ['sheeran']}],
  'tf': [{'s': 'Carlos eats meat and fish.', 'ans': False, 'why': 'He doesn’t eat meat or fish.'}, {'s': 'The pasta has meat.', 'ans': False, 'why': 'It has only tomato and cheese.'}, {'s': 'The restaurant also has a veggie burger.', 'ans': True, 'why': '“We have a veggie burger too.”'}, {'s': 'The writer orders chicken and rice.', 'ans': True, 'why': 'The writer had chicken and rice.'}],
  'order': ['Carlos asks about vegetarian dishes.', 'The server says the pasta is vegetarian.', 'Carlos orders the pasta.', 'The friends share a salad.', 'They go to the supermarket.'],
  'ctx': [{'sent': 'Carlos doesn’t eat meat.', 'w': 'meat', 'opts': ['beef or pork', 'rice', 'bread'], 'ans': 0, 'why': 'Meat is beef, pork, chicken.'}, {'sent': 'The song is gentle and calm.', 'w': 'gentle', 'opts': ['soft', 'loud', 'angry'], 'ans': 0, 'why': 'Gentle = soft and kind.'}, {'sent': 'What is your diet?', 'w': 'diet', 'opts': ['what you usually eat', 'your age', 'your job'], 'ans': 0, 'why': 'Diet = the food you usually eat.'}],
  'chunkHunt': ['Do you have vegetarian dishes?', 'Is there meat in it?', 'No meat.', 'Good choice!'],
  'think': 'Do you have a friend who eats differently from you? How do you choose a restaurant together?'},
 'convo': {'npc': {'name': 'Carlos'}, 'story': 'You work in a restaurant in Portland. Carlos is a vegetarian customer. Help him choose.',
  'turns': [
   {'npc': 'Hi! Do you have vegetarian dishes?', 'pt': 'Oi! Vocês têm pratos vegetarianos?', 'opts': [
    {'en': 'Yes, we do. The pasta is vegetarian.', 'pt': 'Temos. A massa é vegetariana.', 'ok': True, 'fb': 'Short answer plus detail.'},
    {'en': 'Yes, I have.', 'pt': 'Sim, eu tenho.', 'ok': False, 'fb': 'Say Yes, we do.'},
    {'en': 'We are vegetarian dishes.', 'pt': 'Nós somos pratos vegetarianos.', 'ok': False, 'fb': 'Wrong meaning.'}]},
   {'npc': 'Great. Is there meat in it?', 'pt': 'Ótimo. Tem carne?', 'opts': [
    {'en': 'It has meat no.', 'pt': 'Tem carne não.', 'ok': False, 'fb': 'Word order.'},
    {'en': 'Yes, is delicious.', 'pt': 'Sim, é delicioso.', 'ok': False, 'fb': 'It does not answer.'},
    {'en': 'No meat. Just tomato and cheese.', 'pt': 'Sem carne. Só tomate e queijo.', 'ok': True, 'fb': 'Clear and complete.'}]},
   {'npc': 'I don’t eat meat or fish.', 'pt': 'Não como carne nem peixe.', 'opts': [
    {'en': 'No problem. We have a veggie burger too.', 'pt': 'Sem problema. Também temos hambúrguer de legumes.', 'ok': True, 'fb': 'Offer another option.'},
    {'en': 'I no have problem.', 'pt': 'Eu não tenho problema.', 'ok': False, 'fb': 'Say No problem.'},
    {'en': 'Fish is very good.', 'pt': 'Peixe é muito bom.', 'ok': False, 'fb': 'He doesn’t eat fish.'}]},
   {'npc': 'I’ll have the pasta, please.', 'pt': 'Vou querer a massa, por favor.', 'opts': [
    {'en': 'You are pasta.', 'pt': 'Você é massa.', 'ok': False, 'fb': 'Wrong meaning.'},
    {'en': 'Pasta is it.', 'pt': 'Massa é isso.', 'ok': False, 'fb': 'Not natural.'},
    {'en': 'Good choice!', 'pt': 'Boa escolha!', 'ok': True, 'fb': 'A friendly reply.'}]},
   {'npc': 'Enjoy your pasta!', 'pt': 'Bom apetite!', 'opts': [
    {'en': 'I enjoy yes.', 'pt': 'Eu aprecio sim.', 'ok': False, 'fb': 'Not natural.'},
    {'en': 'Thank you! Have a nice day.', 'pt': 'Obrigado! Tenha um bom dia.', 'ok': True, 'fb': 'Polite.'},
    {'en': 'Good night!', 'pt': 'Boa noite!', 'ok': False, 'fb': 'It is a meal, not night.'}]}]},
 'errors': [
  {'wrong': 'I don’t eat meats.', 'fix': 'I don’t eat meat.', 'alt': 'I no eat meat.', 'why': 'Meat is uncountable: no -s.'},
  {'wrong': 'Has meat in it?', 'fix': 'Is there meat in it?', 'alt': 'It has meat in?', 'why': 'Use Is there… in it?'},
  {'wrong': 'I am vegetarian of meat.', 'fix': 'I’m vegetarian. I don’t eat meat.', 'alt': 'I am no meat.', 'why': 'Say I’m vegetarian or I don’t eat meat.'},
  {'wrong': 'We have a vegetarians dish.', 'fix': 'We have a vegetarian dish.', 'alt': 'We have an vegetarian dish.', 'why': 'Adjectives never take -s.'}],
 'homework': 'Write 5 sentences about vegetarian and meat dishes in your country and say them aloud.',
 'homework_items': ['Write 5 sentences about food with and without meat.', 'Ask 3 questions: Is there meat in it?', 'Shadow the dialogue with Carlos.', 'Review: Do you have…? / Is there meat in it? / I don’t eat…']}
