"""Suplemento Quest v5 · aula 74: Shoe shopping + regular I like your necklace (The Red Shoes)."""
SUPP = {
 'reg': 110,
 'badge': {'icon': '👟', 'name': 'Perfect Fit', 'desc': 'Ask for a size, try shoes on and say how they feel'},
 'culture': {
  'hook': 'Shoe sizes change from country to country, and shoes can feel different from brand to brand. Learn how to ask for your size and how to say that shoes feel too tight or too big.',
  'mythfact': [
   {'s': 'A size 10 shoe is the same number in every country.', 'ans': False, 'why': 'The USA, Brazil and Europe use different systems, so numbers do not match.'},
   {'s': 'US shoe sizes include half sizes, like 10 and a half.', 'ans': True, 'why': 'Half sizes are common, so you can try a little bigger or smaller.'},
   {'s': 'Many shoe stores let you try shoes on before you buy them.', 'ans': True, 'why': 'Trying on is a normal part of shoe shopping.'},
   {'s': 'Shoes are made in only one width.', 'ans': False, 'why': 'Many brands also sell narrow and wide shoes.'},
   {'s': 'In "The Red Shoes", a girl cannot stop dancing in her red shoes.', 'ans': True, 'why': 'It is a fairy tale by Hans Christian Andersen, from 1845.'}],
  'wild': [
   {'kind': 'Shoe store sign', 'lines': ['**Running shoes** · all sizes', '**Buy 2 pairs**, get the second pair 50% off', 'Try them on before you buy!'], 'decode': {'q': 'What do you get with two pairs?', 'opts': ['The second pair is half price', 'Both pairs are free', 'A free bag'], 'ans': 0, 'why': '"The second pair 50% off" means half price.'}},
   {'kind': 'Text message', 'lines': ['Hi! I need size 10 in black.', 'Do you have the black ones?', 'I can come at 5 p.m. Thanks!'], 'decode': {'q': 'What size does the customer need?', 'opts': ['10', '5', '50'], 'ans': 0, 'why': '"I need size 10 in black."'}}],
  'compare': {'br': 'In Brazil, adult shoe sizes are usually numbers like 36, 40 or 42, and many people try the shoes on in the store.', 'us': 'In the USA, sizes are different numbers like 7, 8 or 10, with half sizes, and men\'s and women\'s sizes are not the same.', 'tip': 'Ask the clerk for a size chart or try on two sizes.', 'ask': 'What shoe size do you wear? Say it in English.'},
  'quiz': [
   {'q': 'The shoes hurt a little. You say...', 'opts': ['They are a little tight.', 'They are a little water.', 'They are very Tuesday.'], 'ans': 0, 'why': 'Tight = too small and pressing on your feet.'},
   {'q': 'You want to see if the shoes are comfortable. You ask...', 'opts': ['Can I try them on?', 'Can I eat them?', 'Can I wash them?'], 'ans': 0, 'why': 'Try on = put on to test.'},
   {'q': 'A clerk asks, "How do they feel?" A good answer is...', 'opts': ['Great, they feel comfortable.', 'I am Tuesday.', 'They are a pair.'], 'ans': 0, 'why': 'Feel + adjective answers how they feel.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Hank and the running shoes',
  'text': [
   'Hank works in a shoe store in **Detroit**. It is a busy Saturday. Many people want new sneakers, and his feet are tired.',
   'A man walks in. His name is Evan. "Hi! **I need running shoes**," he says. Hank smiles. "**What size?**" "**Size ten**," says Evan. "**Let me check**," says Hank. He goes to the back and brings a box.',
   '"**Here\'s a pair**," says Hank. Evan sits down, puts on a pair of socks and takes the shoes out of the box. They are blue and white. "**Can I try them on?**" he asks. "**Sure**," says Hank. "**How do they feel?**"',
   'Evan stands up and walks around the store. He frowns. "**A little tight**," he says. Hank is not surprised. Shoes from this brand often run small. "**Try size ten and a half**," says Hank.',
   'The new pair is better. Evan runs a few steps and jumps. "Wow! They feel great." Hank laughs. "**They suit you!**" he says. "**You\'re too kind**," says Evan. "**Great choice! Enjoy your shoes!**"',
   'Evan pays at the counter. He leaves the store with a big smile, and Hank is ready for the next customer.'],
  'glossary': [{'w': 'sneakers', 'pt': 'tênis'}, {'w': 'running shoes', 'pt': 'tênis de corrida'}, {'w': 'size', 'pt': 'tamanho / número'}, {'w': 'a pair of', 'pt': 'um par de'}, {'w': 'socks', 'pt': 'meias'}, {'w': 'tight', 'pt': 'apertado'}, {'w': 'frowns', 'pt': 'franze a testa'}, {'w': 'surprised', 'pt': 'surpreso'}, {'w': 'jumps', 'pt': 'pula'}, {'w': 'counter', 'pt': 'balcão'}],
  'fast': {'q': 'What is this text about?', 'opts': ['Buying running shoes in the right size', 'A trip to Detroit by train', 'Cooking dinner'], 'ans': 0, 'why': 'Evan tries shoes on and chooses a bigger size.'},
  'scan': [{'q': 'What size does Evan ask for first?', 'ans': 'ten', 'alt': ['10', 'size ten']}, {'q': 'How do the first shoes feel?', 'ans': 'a little tight', 'alt': ['tight']}, {'q': 'What size does Hank bring next?', 'ans': 'ten and a half', 'alt': ['10.5', '10 and a half', 'ten and half']}],
  'tf': [
   {'s': 'Hank works in a shoe store.', 'ans': True, 'why': '"Hank works in a shoe store in Detroit."'},
   {'s': 'The first shoes are too big.', 'ans': False, 'why': 'Evan says they are a little tight.'},
   {'s': 'Evan tries the shoes on.', 'ans': True, 'why': 'Hank says, "Sure," and Evan puts them on.'},
   {'s': 'Evan leaves without buying shoes.', 'ans': False, 'why': 'He pays and leaves with a big smile.'}],
  'order': ['Evan says he needs running shoes.', 'Hank brings size ten.', 'Evan tries them on and says they are tight.', 'Hank brings size ten and a half.', 'Evan pays and leaves happy.'],
  'ctx': [
   {'sent': 'Evan walks around the store.', 'w': 'walks around', 'opts': ['moves here and there', 'sits down', 'buys a bag'], 'ans': 0, 'why': 'Walks around = moves in different places.'},
   {'sent': 'The shoes are a little tight.', 'w': 'tight', 'opts': ['too small', 'too cheap', 'too red'], 'ans': 0, 'why': 'Tight = too small for your foot.'},
   {'sent': 'You\'re too kind.', 'w': 'kind', 'opts': ['nice and generous', 'angry', 'tired'], 'ans': 0, 'why': 'Kind = nice to other people.'}],
  'chunkHunt': ['What size?', 'Can I try them on?', 'How do they feel?', 'A little tight'],
  'think': 'What are your favorite shoes? How do they feel when you walk in them?'},
 'convo': {'npc': {'name': 'Evan'}, 'story': 'You work in a shoe store in Detroit. Evan is a customer and needs running shoes.', 'turns': [
  {'npc': 'Hi! I need running shoes.', 'pt': 'Oi! Preciso de tênis de corrida.', 'opts': [
   {'en': 'What size?', 'pt': 'Que número?', 'ok': True, 'fb': 'Short and natural question.'},
   {'en': 'I run every day.', 'pt': 'Eu corro todo dia.', 'ok': False, 'fb': 'You are the clerk, not the customer.'},
   {'en': 'The shoes are yellow.', 'pt': 'Os tênis são amarelos.', 'ok': False, 'fb': 'It does not move the sale forward.'}]},
  {'npc': 'Size ten.', 'pt': 'Número dez.', 'opts': [
   {'en': 'I am size ten too.', 'pt': 'Eu também sou dez.', 'ok': False, 'fb': 'It is not about you.'},
   {'en': 'Let me check. Here\'s a pair.', 'pt': 'Vou ver. Aqui está um par.', 'ok': True, 'fb': 'Offers help and brings the shoes.'},
   {'en': 'Ten is a number.', 'pt': 'Dez é um número.', 'ok': False, 'fb': 'True, but not useful.'}]},
  {'npc': 'Can I try them on?', 'pt': 'Posso experimentar?', 'opts': [
   {'en': 'Sure. How do they feel?', 'pt': 'Claro. Como estão?', 'ok': True, 'fb': 'Says yes and asks how they feel.'},
   {'en': 'No, I try them.', 'pt': 'Não, eu os experimento.', 'ok': False, 'fb': 'Confusing answer.'},
   {'en': 'They are fifty dollars.', 'pt': 'Custam cinquenta dólares.', 'ok': False, 'fb': 'He asks about trying on, not the price.'}]},
  {'npc': 'A little tight.', 'pt': 'Um pouco apertados.', 'opts': [
   {'en': 'You are tight.', 'pt': 'Você está apertado.', 'ok': False, 'fb': 'Wrong subject.'},
   {'en': 'Great choice.', 'pt': 'Ótima escolha.', 'ok': False, 'fb': 'It is too early; they do not fit.'},
   {'en': 'Try size ten and a half.', 'pt': 'Experimente o dez e meio.', 'ok': True, 'fb': 'Suggests a bigger size.'}]}]},
 'homework': 'Look at the size of three pairs of shoes at home. Write the size and how they feel, like: These sneakers are size 8 and they feel comfortable.',
 'homework_items': ['Write 4 sentences about your shoes: size, color and how they feel.', 'Record yourself asking: Can I try them on? How do they feel?', 'Listen to the dialogue again and shadow Evan.', 'Review: What size? / A little tight. / Try size ten and a half.'],
 'errors': [
  {'wrong': 'I need running shoe.', 'fix': 'I need running shoes.', 'alt': 'I need a running shoes.', 'why': 'Shoes are a pair, so use the plural: shoes.'},
  {'wrong': 'The shoes are tights.', 'fix': 'The shoes are tight.', 'alt': 'The shoes are tighten.', 'why': 'Tight is an adjective and has no -s.'},
  {'wrong': 'Can I try it them on?', 'fix': 'Can I try them on?', 'alt': 'Can I try on them?', 'why': 'With a pronoun, put it between try and on: try them on.'},
  {'wrong': 'How is the shoes?', 'fix': 'How do they feel?', 'alt': 'How are the shoes feel?', 'why': 'Use How do they feel? for comfort.'}]}
