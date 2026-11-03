"""Suplemento Quest v5 · aula 73: Clothes and sizes + regular Is This My Size? (Honey, We Shrunk Ourselves)."""
SUPP = {
 'reg': 74,
 'badge': {'icon': '👕', 'name': 'Size Master', 'desc': 'Ask for a size, a color and a fitting room in English'},
 'sticker': {'cat': 'Everyday culture', 'title': 'What Size Are You?', 'sub': 'Small, medium or large?'},
 'culture': {
  'hook': 'In US stores, clothes often come in letter sizes like S, M and L, and the numbers can change from brand to brand. Learn how to ask for the right size.',
  'polite': 'Say **“Excuse me, do you have this in a medium?”** A smile and **“Thank you!”** go a long way in a shop.',
  'mythfact': [
   {'s': 'Many US stores use letter sizes such as S, M and L for shirts.', 'ans': True, 'why': 'S, M, L and XL are very common on T-shirts and sweaters.'},
   {'s': 'A medium is always the same size in every store.', 'ans': False, 'why': 'Brands often cut clothes differently, so it is smart to try things on.'},
   {'s': 'The abbreviation XL means “extra large”.', 'ans': True, 'why': 'X = extra, L = large.'},
   {'s': 'In the USA you can never try clothes on in a shop.', 'ans': False, 'why': 'Most clothing stores have fitting rooms where you can try things on.'},
   {'s': '“On sale” means the price is lower than usual.', 'ans': True, 'why': 'A sale is a time with lower prices.'}],
  'wild': [
   {'kind': 'Size chart', 'lines': ['**S** (small)  chest 34–36 in', '**M** (medium)  chest 38–40 in', '**L** (large)  chest 42–44 in', 'Sizes can vary. Try it on!'], 'decode': {'q': 'What does M mean?', 'opts': ['medium', 'many', 'men'], 'ans': 0, 'why': 'M = medium.'}},
   {'kind': 'Shop sign', 'lines': ['**SUMMER SALE**', 'T-shirts $8 · Jeans $25', 'Fitting rooms are at the back.'], 'decode': {'q': 'Where are the fitting rooms?', 'opts': ['At the back', 'At the door', 'Upstairs'], 'ans': 0, 'why': 'The sign says they are at the back.'}}],
  'compare': {'br': 'In Brazil many shops use numbers like 38 or 40 for clothes and also P, M and G for shirts.', 'us': 'In the USA you often see S, M, L and numbers like 6 or 8 for dresses and pants, and the sizes change by brand.', 'tip': 'Learn your size in English: small, medium, large. If you are not sure, ask: “Can I try it on?”', 'ask': 'What size are you in a T-shirt? Say it in English.'},
  'quiz': [
   {'q': 'You want a shirt in blue. You ask…', 'opts': ['Do you have it in blue?', 'You are blue?', 'It has blue you?'], 'ans': 0, 'why': 'Do you have it in blue? is the natural question.'},
   {'q': 'You are not sure about the size. You say…', 'opts': ['Where can I try it on?', 'Where I try the size?', 'I try on to go.'], 'ans': 0, 'why': 'Where can I try it on? is correct.'},
   {'q': 'The clerk says “What size are you?” You answer…', 'opts': ['I’m a medium.', 'I have medium years.', 'Medium is me size.'], 'ans': 0, 'why': 'I’m a medium is the usual answer.'}]},
 'reading': {
  'genre': 'Funny story', 'title': 'Too small, too big',
  'text': [
   'In the 1997 family film **Honey, We Shrunk Ourselves**, the actor Rick Moranis plays an inventor. A machine makes people very tiny, and the adults must walk across a garden. For them, a button looks like a plate.',
   'Now think about a normal day in a shop in Los Angeles. Wendy says to the clerk, “Hi, **I’m looking for** a T-shirt.” The clerk asks, “**What size are you?**” “I’m a medium,” she says.',
   'The clerk brings a few shirts. “**Is this my size?**” Wendy asks. She holds the first one. It is too big. “**It’s too big**,” she says. The second shirt is too small. “**It’s too small**.”',
   '“Can I **try it on**?” Wendy asks about a third one. The clerk smiles. “Sure. The fitting room is over there.” Wendy goes in. Then she comes out and looks in the mirror.',
   '“**It fits well**!” she says. She asks, “Do you have it in blue?” “Yes, here you go,” says the clerk. The shirt is on sale, too.',
   'Wendy pays and says, “Thank you!” Size is a small thing, but it changes your whole day.'],
  'glossary': [{'w': 'inventor', 'pt': 'inventor'}, {'w': 'tiny', 'pt': 'minúsculo'}, {'w': 'button', 'pt': 'botão'}, {'w': 'clerk', 'pt': 'atendente de loja'}, {'w': 'fitting room', 'pt': 'provador'}, {'w': 'mirror', 'pt': 'espelho'}, {'w': 'size', 'pt': 'tamanho'}, {'w': 'on sale', 'pt': 'em promoção'}, {'w': 'plate', 'pt': 'prato'}, {'w': 'garden', 'pt': 'jardim'}],
  'fast': {'q': 'What is this text about?', 'opts': ['Finding the right clothes size', 'Cooking dinner', 'Going to the airport'], 'ans': 0, 'why': 'Wendy tries shirts until one fits.'},
  'scan': [{'q': 'What size is Wendy?', 'ans': 'medium', 'alt': ['a medium', 'Medium']}, {'q': 'What color does Wendy ask for?', 'ans': 'blue', 'alt': ['Blue']}, {'q': 'Which year is the film from?', 'ans': '1997', 'alt': ['nineteen ninety-seven']}],
  'tf': [{'s': 'Wendy is in Los Angeles.', 'ans': True, 'why': 'The shop is in Los Angeles.'}, {'s': 'The first shirt is too small.', 'ans': False, 'why': 'The first shirt is too big.'}, {'s': 'The fitting room is over there.', 'ans': True, 'why': 'The clerk says so.'}, {'s': 'Wendy does not buy the shirt.', 'ans': False, 'why': 'She pays and says thank you.'}],
  'order': ['Wendy says she wants a T-shirt.', 'The first shirt is too big.', 'The second shirt is too small.', 'Wendy tries on the third shirt.', 'She says, “It fits well!”'],
  'ctx': [{'sent': 'The button is tiny.', 'w': 'tiny', 'opts': ['very small', 'very loud', 'very old'], 'ans': 0, 'why': 'Tiny = very small.'}, {'sent': 'The clerk works in a shop.', 'w': 'clerk', 'opts': ['a person who helps customers', 'a kind of shirt', 'a kind of shoe'], 'ans': 0, 'why': 'A clerk helps customers in a store.'}, {'sent': 'The shirt fits well.', 'w': 'fits', 'opts': ['is the right size', 'is dirty', 'is expensive'], 'ans': 0, 'why': 'Fits = is the right size and shape.'}],
  'chunkHunt': ['Is this my size?', 'It’s too small.', 'Can I try it on?', 'It fits well.'],
  'think': 'Do you find your size easily when you shop? What size are you in a T-shirt?'},
 'convo': {'npc': {'name': 'Marco'}, 'story': 'You are in a clothing store in Los Angeles. Marco is the store clerk. Find a T-shirt.',
  'turns': [
   {'npc': 'Hi! Can I help you?', 'pt': 'Oi! Posso ajudar?', 'opts': [
    {'en': 'Yes, I’m looking for a T-shirt.', 'pt': 'Sim, estou procurando uma camiseta.', 'ok': True, 'fb': 'I’m looking for… is natural in shops.'},
    {'en': 'I look a T-shirt.', 'pt': 'Eu olho uma camiseta.', 'ok': False, 'fb': 'Use I’m looking for.'},
    {'en': 'No, I am Marco.', 'pt': 'Não, eu sou Marco.', 'ok': False, 'fb': 'Marco is the clerk, not you.'}]},
   {'npc': 'What size are you?', 'pt': 'Qual é seu tamanho?', 'opts': [
    {'en': 'I have 30 years.', 'pt': 'Eu tenho 30 anos.', 'ok': False, 'fb': 'He asked about size, not age.'},
    {'en': 'I’m a medium.', 'pt': 'Eu sou M.', 'ok': True, 'fb': 'The usual way to say your size.'},
    {'en': 'My size is the medium me.', 'pt': 'Meu tamanho é o M eu.', 'ok': False, 'fb': 'Unnatural. Say: I’m a medium.'}]},
   {'npc': 'Here are some in medium.', 'pt': 'Aqui estão algumas no M.', 'opts': [
    {'en': 'Do you have it in blue?', 'pt': 'Tem em azul?', 'ok': True, 'fb': 'Ask for a color politely.'},
    {'en': 'You have the blue?', 'pt': 'Você tem o azul?', 'ok': False, 'fb': 'Use Do you have…?'},
    {'en': 'I am blue today.', 'pt': 'Estou azul hoje.', 'ok': False, 'fb': 'Wrong meaning.'}]},
   {'npc': 'Yes, here you go.', 'pt': 'Tem, aqui está.', 'opts': [
    {'en': 'Where I can try it?', 'pt': 'Onde eu posso provar?', 'ok': False, 'fb': 'Say: Where can I try it on?'},
    {'en': 'Thanks. Where can I try it on?', 'pt': 'Obrigado. Onde posso provar?', 'ok': True, 'fb': 'Thank him and ask.'},
    {'en': 'I go home now.', 'pt': 'Eu vou para casa agora.', 'ok': False, 'fb': 'It does not fit the situation.'}]},
   {'npc': 'Thanks for shopping with us!', 'pt': 'Obrigado por comprar conosco!', 'opts': [
    {'en': 'I shop you.', 'pt': 'Eu compro você.', 'ok': False, 'fb': 'Wrong meaning.'},
    {'en': 'No, I do not.', 'pt': 'Não, eu não.', 'ok': False, 'fb': 'It does not answer.'},
    {'en': 'Thank you! Have a nice day.', 'pt': 'Obrigado! Tenha um bom dia.', 'ok': True, 'fb': 'A friendly closing.'}]}]},
 'errors': [
  {'wrong': 'I use size M.', 'fix': 'I’m a medium.', 'alt': 'I’m size of medium.', 'why': 'To say your size, use I’m a medium or I wear a medium.'},
  {'wrong': 'It is too much small.', 'fix': 'It’s too small.', 'alt': 'It’s very too small.', 'why': 'Use too + adjective, without much.'},
  {'wrong': 'Where I can try it on?', 'fix': 'Where can I try it on?', 'alt': 'Where I try it on can?', 'why': 'In questions, can comes before I.'},
  {'wrong': 'You have it in blue?', 'fix': 'Do you have it in blue?', 'alt': 'Have you it in blue?', 'why': 'Questions with have usually use Do you have…?'}],
 'homework': 'Look at the labels of 3 clothes at home. Say the size, the color and the thing in English, and send a 30-second audio to your teacher.',
 'homework_items': ['Write your size and 3 colors in English.', 'Say: I’m looking for… / Is this my size?', 'Listen to the dialogue again and shadow Marco.', 'Review: Do you have it in…? / Can I try it on? / It fits well.']}
