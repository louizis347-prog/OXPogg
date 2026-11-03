"""Suplemento Quest v5 · aula 73: Clothes and sizes + regular Getting Dressed (Project Runway)."""
SUPP = {
 'reg': 59,
 'badge': {'icon': '👕', 'name': 'Size Master', 'desc': 'Ask for a size, a color and a fitting room in a clothes shop'},
 'culture': {
  'hook': 'Buying clothes in the USA starts with one question: what size are you? Learn the letters and numbers, and how to ask for another color or size.',
  'mythfact': [
   {'s': 'Many US stores use letters for sizes: S, M, L and XL.', 'ans': True, 'why': 'S is small, M is medium, L is large and XL is extra large.'},
   {'s': 'A medium is the same size in every store.', 'ans': False, 'why': 'Sizes change from brand to brand, so trying clothes on is important.'},
   {'s': 'The price on the tag usually includes sales tax in the USA.', 'ans': False, 'why': 'In most places sales tax is added at the register.'},
   {'s': 'Most clothes shops have a fitting room to try clothes on.', 'ans': True, 'why': 'The staff often gives you a number for the items you take inside.'},
   {'s': 'Jeans in the USA are sold only in letter sizes.', 'ans': False, 'why': 'Jeans usually use numbers, like waist and length in inches.'}],
  'wild': [
   {'kind': 'Price tag', 'lines': ['**Blue Jacket**', 'Size: **M**', 'Was $60 · **Now $45**'], 'decode': {'q': 'How much is the jacket now?', 'opts': ['$45', '$60', '$15'], 'ans': 0, 'why': 'The tag says "Now $45".'}},
   {'kind': 'Sign in a shop', 'lines': ['**FITTING ROOMS**', 'Maximum 6 items', 'Please ask for a number'], 'decode': {'q': 'How many items can you take in?', 'opts': ['6', '3', '12'], 'ans': 0, 'why': '"Maximum 6 items".'}}],
  'compare': {'br': 'In Brazil, sizes are often P, M, G and GG, and numbers like 38 or 40 are also common for clothes and jeans.', 'us': 'In the USA, sizes are S, M, L, XL, or numbers like 6 or 8, and the same size can fit differently in each store.', 'tip': 'Take two sizes into the fitting room, one bigger and one smaller.', 'ask': 'What size are you in a T-shirt? Say it in English.'},
  'quiz': [
   {'q': 'A shop assistant asks, "What size are you?" You say...', 'opts': ['I\'m a medium.', 'I\'m in the shop.', 'I have a size.'], 'ans': 0, 'why': 'Use I\'m + size to answer.'},
   {'q': 'You want the same T-shirt in another color. You ask...', 'opts': ['Do you have it in blue?', 'Is you blue?', 'Where is blue?'], 'ans': 0, 'why': 'Do you have it in + color? is the natural question.'},
   {'q': 'You want to see how the jacket looks on you. You ask...', 'opts': ['Where can I try it on?', 'Where is the shower?', 'Can I buy air?'], 'ans': 0, 'why': 'Try on = put clothes on to see if they fit.'}]},
 'reading': {
  'genre': 'Diary',
  'title': 'Wendy goes shopping',
  'text': [
   'Today I went shopping in **Los Angeles**. It was Saturday, and I needed new clothes for work. I walked into a small shop near my apartment.',
   'A young man smiled at me. His name was Marco. "Hi! **Can I help you?**" he asked. "Yes, **I\'m looking for a T-shirt**," I said. "**What size are you?**" "**I\'m a medium.**" He gave me three shirts.',
   'I liked a gray one, but I wanted a different color. "**Do you have it in blue?**" I asked. "**Just a minute!**" said Marco. He came back with a blue shirt. "**Yes, here you go.**"',
   'I also saw a black **jacket** and a nice **dress**, and some jeans too. "**Where can I try it on?**" I asked. Marco showed me the **fitting room**. The jacket was too big, but the blue shirt was perfect. "**It fits me!**" I said.',
   'In the mirror, I looked at myself. "**You look great!**" said Marco. He was right. I paid for the shirt and a pair of jeans, and I said, "**Thanks!**"',
   '"**Thanks for shopping with us!**" Marco said. I walked home with a big smile and a new bag.'],
  'glossary': [{'w': 'went shopping', 'pt': 'fui fazer compras'}, {'w': 'clothes', 'pt': 'roupas'}, {'w': 'looking for', 'pt': 'procurando'}, {'w': 'size', 'pt': 'tamanho'}, {'w': 'medium', 'pt': 'médio (M)'}, {'w': 'jacket', 'pt': 'jaqueta'}, {'w': 'dress', 'pt': 'vestido'}, {'w': 'fitting room', 'pt': 'provador'}, {'w': 'too big', 'pt': 'grande demais'}, {'w': 'mirror', 'pt': 'espelho'}],
  'fast': {'q': 'What is this text about?', 'opts': ['Buying a shirt in a clothes shop', 'Cooking in a kitchen', 'A flight to Brazil'], 'ans': 0, 'why': 'Wendy buys a T-shirt and jeans and tries clothes on.'},
  'scan': [{'q': 'What is the salesperson\'s name?', 'ans': 'Marco', 'alt': ['marco']}, {'q': 'What size is Wendy?', 'ans': 'medium', 'alt': ['m', 'a medium']}, {'q': 'What color is the shirt she likes best?', 'ans': 'blue', 'alt': ['a blue shirt']}],
  'tf': [
   {'s': 'Wendy is looking for a T-shirt.', 'ans': True, 'why': '"I\'m looking for a T-shirt."'},
   {'s': 'The jacket is perfect for her.', 'ans': False, 'why': '"The jacket was too big."'},
   {'s': 'Marco brings a blue shirt.', 'ans': True, 'why': '"He came back with a blue shirt."'},
   {'s': 'Wendy does not buy anything.', 'ans': False, 'why': 'She paid for the shirt and a pair of jeans.'}],
  'order': ['Wendy walks into a shop.', 'She says her size: medium.', 'Marco brings a blue shirt.', 'Wendy tries clothes on in the fitting room.', 'She pays and leaves with a bag.'],
  'ctx': [
   {'sent': 'The jacket was too big.', 'w': 'too big', 'opts': ['bigger than good', 'very small', 'very cheap'], 'ans': 0, 'why': '"Too big" means bigger than you want.'},
   {'sent': 'It fits me!', 'w': 'fits', 'opts': ['is the right size', 'is expensive', 'is dirty'], 'ans': 0, 'why': 'When clothes fit, they are the right size.'},
   {'sent': 'I\'m looking for a T-shirt.', 'w': 'looking for', 'opts': ['trying to find', 'throwing away', 'washing'], 'ans': 0, 'why': 'Looking for = trying to find.'}],
  'chunkHunt': ['Can I help you?', 'What size are you?', 'Do you have it in blue?', 'Where can I try it on?'],
  'think': 'What size are you in a T-shirt? Do you like to try clothes on, or do you buy them fast?'},
 'convo': {'npc': {'name': 'Marco'}, 'story': 'You are in a clothes shop in Los Angeles. Marco works there. You need a T-shirt.', 'turns': [
  {'npc': 'Hi! Can I help you?', 'pt': 'Oi! Posso ajudar?', 'opts': [
   {'en': 'Yes, I\'m looking for a T-shirt.', 'pt': 'Sim, estou procurando uma camiseta.', 'ok': True, 'fb': 'Clear request: looking for + thing.'},
   {'en': 'I help you.', 'pt': 'Eu ajudo você.', 'ok': False, 'fb': 'This changes who helps.'},
   {'en': 'Yes, I am a T-shirt.', 'pt': 'Sim, eu sou uma camiseta.', 'ok': False, 'fb': 'Wrong meaning.'}]},
  {'npc': 'What size are you?', 'pt': 'Qual é seu tamanho?', 'opts': [
   {'en': 'I have thirty years.', 'pt': 'Eu tenho trinta anos.', 'ok': False, 'fb': 'Size is not age.'},
   {'en': 'I\'m a medium.', 'pt': 'Eu sou M.', 'ok': True, 'fb': 'Natural: I\'m a + size.'},
   {'en': 'The size is yes.', 'pt': 'O tamanho é sim.', 'ok': False, 'fb': 'Does not answer.'}]},
  {'npc': 'Here are some in medium.', 'pt': 'Aqui estão algumas no M.', 'opts': [
   {'en': 'Do you have it in blue?', 'pt': 'Tem em azul?', 'ok': True, 'fb': 'Natural way to ask for a color.'},
   {'en': 'Where is my medium?', 'pt': 'Onde está meu M?', 'ok': False, 'fb': 'Marco just showed you the shirts.'},
   {'en': 'You are blue.', 'pt': 'Você é azul.', 'ok': False, 'fb': 'Wrong meaning.'}]},
  {'npc': 'Yes, here you go.', 'pt': 'Tem, aqui está.', 'opts': [
   {'en': 'Where can I try it on?', 'pt': 'Onde posso provar?', 'ok': True, 'fb': 'Asks for the fitting room.'},
   {'en': 'I do not try.', 'pt': 'Eu não tento.', 'ok': False, 'fb': 'You want to try it on.'},
   {'en': 'Thanks for shopping with us!', 'pt': 'Obrigado por comprar conosco!', 'ok': False, 'fb': 'That is what the seller says at the end.'}]}]},
 'homework': 'Look at the labels on three of your clothes. Write the size and color of each one in English, like: This is a medium, blue T-shirt.',
 'homework_items': ['Write 4 sentences about your clothes: size and color.', 'Record yourself asking: Do you have it in blue? Where can I try it on?', 'Listen to the dialogue again and shadow Marco.', 'Review: What size are you? / I\'m a medium. / It fits me.'],
 'errors': [
  {'wrong': 'I have size medium.', 'fix': 'I\'m a medium.', 'alt': 'I am size of medium.', 'why': 'In English you say I\'m a medium (or I wear a medium).'},
  {'wrong': 'You have in blue?', 'fix': 'Do you have it in blue?', 'alt': 'Have you it in blue?', 'why': 'Questions with have use Do you have...?'},
  {'wrong': 'I\'m looking a T-shirt.', 'fix': 'I\'m looking for a T-shirt.', 'alt': 'I look for T-shirt now.', 'why': 'The phrase is looking for something.'},
  {'wrong': 'Where I can try it?', 'fix': 'Where can I try it on?', 'alt': 'Where can I to try it on?', 'why': 'Question order: Where + can + I. And say try it on.'}]}
