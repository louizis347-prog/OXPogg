"""Suplemento Quest v5 · aula 115: School supplies + regular Hard or easy subjects (Rebecca of Sunnybrook Farm)."""
SUPP = {
 'reg': 186,
 'badge': {'icon': '✏️', 'name': 'Supply Shopper', 'desc': 'Ask for supplies, find the aisle and check the price'},
 'culture': {
  'hook': 'In August and September, many stores in the USA fill their shelves with school supplies. Schools often send a list, and families buy pencils, notebooks, rulers and backpacks.',
  'mythfact': [
   {'s': 'Many US schools send parents a list of school supplies.', 'ans': True, 'why': 'Teachers often list what each student needs.'},
   {'s': 'The price on the shelf usually includes sales tax in the USA.', 'ans': False, 'why': 'Tax is usually added at the register.'},
   {'s': 'Some US states have a “tax-free weekend” for school supplies.', 'ans': True, 'why': 'Texas, for example, has one in August; rules change by state and year.'},
   {'s': 'In a store, an aisle is a long path between shelves.', 'ans': True, 'why': 'Signs show the aisle number.'},
   {'s': '“Rebecca of Sunnybrook Farm” is a novel from 1903.', 'ans': True, 'why': 'Kate Douglas Wiggin wrote it, and Rebecca goes to school.'}],
  'wild': [
   {'kind': 'Store sign', 'lines': ['**Back to School Sale**', 'Pencils, 10-pack: $3', 'Aisle 4'], 'decode': {'q': 'How much is a pack of ten pencils?', 'opts': ['$3', '$10', '$4'], 'ans': 0, 'why': '“Pencils, 10-pack: $3.”'}},
   {'kind': 'School supply list', 'lines': ['**Grade 5 list**', '2 notebooks, 1 ruler', '1 backpack, 24 pencils'], 'decode': {'q': 'How many notebooks does the list ask for?', 'opts': ['2', '1', '24'], 'ans': 0, 'why': '“2 notebooks.”'}}],
  'compare': {'br': 'No Brasil, a lista de material escolar também é comum no início do ano, em janeiro ou fevereiro.', 'us': 'Nos EUA, as compras costumam ser em agosto e setembro, e muitas lojas têm promoções nessa época.', 'tip': 'Ask: “Where are the notebooks?”', 'ask': 'What do you buy for school or work? Which color do you like?'},
  'quiz': [
   {'q': 'You need a ruler. You ask…', 'opts': ['Where is the ruler?', 'Where are the rulers on me?', 'The ruler where?'], 'ans': 0, 'why': 'Where is…? asks for a place.'},
   {'q': '“A pack of ten is three dollars” means…', 'opts': ['Ten for $3', 'Three for $10', 'One for $13'], 'ans': 0, 'why': 'A pack of ten = ten pencils for $3.'},
   {'q': 'What is an eraser for?', 'opts': ['to remove pencil marks', 'to cut paper', 'to draw lines'], 'ans': 0, 'why': 'An eraser removes pencil marks.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Back to school',
  'text': [
   'Tom lives in **Houston**. School starts next week, and his teacher sends a list. Tom reads it twice. Then he goes to a big store with his sister Lily.',
   'At the door, a woman named Rosa works at the information desk. “Hi! **I need school supplies**,” Tom says. “**What do you need?**” “**Pencils, notebooks and a ruler.**” “**They’re in aisle four.**”',
   'In aisle four, Tom sees a sign. “**How much are the pencils?**” he asks. “**A pack of ten is three dollars.**” “**I’ll take two packs.**” Rosa smiles. “**What about a backpack?**” “**We have red, blue and black.**” Lily likes the blue one.',
   'Lily tells Tom about “Rebecca of Sunnybrook Farm,” a novel from 1903. Rebecca is a girl who loves words, and she goes to a school in a small town. Spelling is tricky for some students, but Rebecca likes it. Tom laughs. “Math is tricky for me,” he says. So he picks a calculator too.',
   'At the register, Tom puts everything on the counter: pencils, notebooks, a ruler, an eraser, glue and a blue backpack. He pays, and the cashier gives him a receipt. “Have a great school year!” she says.'],
  'glossary': [{'w': 'school supplies', 'pt': 'material escolar'}, {'w': 'list', 'pt': 'lista'}, {'w': 'pencils', 'pt': 'lápis'}, {'w': 'ruler', 'pt': 'régua'}, {'w': 'aisle', 'pt': 'corredor (de loja)'}, {'w': 'pack', 'pt': 'pacote'}, {'w': 'backpack', 'pt': 'mochila'}, {'w': 'tricky', 'pt': 'difícil, enganoso'}, {'w': 'calculator', 'pt': 'calculadora'}, {'w': 'receipt', 'pt': 'recibo'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A boy buys school supplies', 'A woman rents a car', 'A girl plays soccer'], 'ans': 0, 'why': 'Tom shops for school supplies in Houston.'},
  'scan': [{'q': 'In which aisle are the pencils?', 'ans': 'aisle four', 'alt': ['four', '4', 'aisle 4']}, {'q': 'How many packs of pencils does Tom take?', 'ans': 'two', 'alt': ['2', 'two packs']}, {'q': 'What color backpack does Tom buy?', 'ans': 'blue', 'alt': ['a blue backpack']}],
  'tf': [{'s': 'A pack of ten pencils is three dollars.', 'ans': True, 'why': 'Rosa says so.'}, {'s': 'Tom takes one pack of pencils.', 'ans': False, 'why': 'He says, “I’ll take two packs.”'}, {'s': 'Lily likes the blue backpack.', 'ans': True, 'why': 'The story says Lily likes the blue one.'}, {'s': 'Tom does not buy a calculator.', 'ans': False, 'why': 'He picks a calculator too.'}],
  'order': ['Tom reads the school list.', 'Rosa says the supplies are in aisle four.', 'Tom takes two packs of pencils.', 'Tom picks a blue backpack.', 'Tom pays at the register.'],
  'ctx': [{'sent': 'They’re in aisle four.', 'w': 'aisle', 'opts': ['a path between shelves', 'a kind of fruit', 'a school bus'], 'ans': 0, 'why': 'Aisle = path in a store.'}, {'sent': 'Spelling is tricky for some students.', 'w': 'tricky', 'opts': ['hard to get right', 'very cheap', 'very short'], 'ans': 0, 'why': 'Tricky = a little difficult.'}, {'sent': 'The cashier gives him a receipt.', 'w': 'receipt', 'opts': ['a paper that shows what you paid', 'a bag', 'a pencil'], 'ans': 0, 'why': 'A receipt shows your purchase.'}],
  'chunkHunt': ['I need school supplies.', 'They’re in aisle four.', 'How much are the pencils?', 'I’ll take two packs.'],
  'think': 'What do you always have in your bag?'},
 'convo': {'npc': {'name': 'Rosa'}, 'story': 'You are in a store and need school supplies. Rosa works there and helps you.', 'turns': [
  {'npc': 'Hi! Can I help you?', 'pt': 'Oi! Posso ajudar?', 'opts': [
   {'en': 'Hi! I need school supplies.', 'pt': 'Oi! Preciso de material escolar.', 'ok': True, 'fb': 'Says what you need.'},
   {'en': 'Hi! I am needing school supplies.', 'pt': 'Oi! Estou precisando de material escolar.', 'ok': False, 'fb': 'Need is a state verb; say I need.'},
   {'en': 'Hi! I am a school.', 'pt': 'Oi! Eu sou uma escola.', 'ok': False, 'fb': 'Wrong meaning.'}]},
  {'npc': 'What do you need?', 'pt': 'Do que você precisa?', 'opts': [
   {'en': 'Pencils, notebooks and a ruler.', 'pt': 'Lápis, cadernos e uma régua.', 'ok': True, 'fb': 'Names the items.'},
   {'en': 'Pencils, notebooks and one rule.', 'pt': 'Lápis, cadernos e uma regra.', 'ok': False, 'fb': 'Ruler is the tool; rule is a regra.'},
   {'en': 'I need three dollars.', 'pt': 'Preciso de três dólares.', 'ok': False, 'fb': 'She asks about supplies.'}]},
  {'npc': 'They’re in aisle four.', 'pt': 'Estão no corredor quatro.', 'opts': [
   {'en': 'Thanks! How much are the pencils?', 'pt': 'Obrigado! Quanto custam os lápis?', 'ok': True, 'fb': 'Natural next step.'},
   {'en': 'Thanks! How many are the pencils?', 'pt': 'Obrigado! Quantos são os lápis?', 'ok': False, 'fb': 'For price, say How much.'},
   {'en': 'I am in aisle four.', 'pt': 'Eu estou no corredor quatro.', 'ok': False, 'fb': 'Does not fit.'}]},
  {'npc': 'A pack of ten is three dollars.', 'pt': 'Um pacote com dez custa três dólares.', 'opts': [
   {'en': 'I take two packs.', 'pt': 'Eu pego dois pacotes.', 'ok': False, 'fb': 'Natural form is I’ll take.'},
   {'en': 'I’ll take two packs.', 'pt': 'Vou levar dois pacotes.', 'ok': True, 'fb': 'Decides to buy.'},
   {'en': 'A pack is a pencil.', 'pt': 'Um pacote é um lápis.', 'ok': False, 'fb': 'Wrong meaning.'}]},
  {'npc': 'What about a backpack? We have red, blue and black.', 'pt': 'E uma mochila? Temos vermelha, azul e preta.', 'opts': [
   {'en': 'The blue one, please.', 'pt': 'A azul, por favor.', 'ok': True, 'fb': 'Chooses a color.'},
   {'en': 'I am blue, please.', 'pt': 'Eu sou azul, por favor.', 'ok': False, 'fb': 'Wrong meaning.'},
   {'en': 'We have a backpack.', 'pt': 'Nós temos uma mochila.', 'ok': False, 'fb': 'She already said that.'}]}]},
 'errors': [
  {'wrong': 'I need of school supplies.', 'fix': 'I need school supplies.', 'alt': 'I am need school supplies.', 'why': 'In English, need goes directly with the noun: no “of”.'},
  {'wrong': 'How many costs the pencils?', 'fix': 'How much are the pencils?', 'alt': 'How much costs the pencils?', 'why': 'For price, use How much + are for plural things.'},
  {'wrong': 'I will to take two packs.', 'fix': 'I’ll take two packs.', 'alt': 'I take two packs.', 'why': 'After will, use the base verb with no “to”.'},
  {'wrong': 'They are in the corridor four.', 'fix': 'They’re in aisle four.', 'alt': 'They are on aisle four.', 'why': 'In a store, the path between shelves is an aisle.'}],
 'homework': 'Write a short dialogue: you buy school supplies and ask about price and colors.',
 'homework_items': ['Write 5 school supplies you need.', 'Say aloud: How much are the pencils?', 'Listen to the dialogue and shadow Rosa.', 'Review: red / blue / black.']}
