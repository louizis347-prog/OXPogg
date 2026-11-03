"""Suplemento Quest v5 · aula 81: At the checkout + regular Sold out! (Black Friday)."""
SUPP = {
 'reg': 176,
 'badge': {'icon': '🛒', 'name': 'Checkout Pro', 'desc': 'Pay, choose a bag and ask for a receipt in English'},
 'sticker': {'cat': 'Everyday culture', 'title': 'Paper or Plastic?', 'sub': 'The question at every checkout'},
 'culture': {
  'hook': 'At an American supermarket checkout, the cashier asks a few quick questions. They are always almost the same, so you can learn them once and feel calm every time.',
  'polite': 'Answer each question in a short, friendly way: **Yes, thanks**, **Paper, please**, **No receipt, thanks**.',
  'mythfact': [
   {'s': 'The cashier often asks “Paper or plastic?”', 'ans': True, 'why': 'This is a very common question in US supermarkets.'},
   {'s': 'Many US stores have self-checkout machines.', 'ans': True, 'why': 'Customers scan and pay by themselves.'},
   {'s': 'You can only pay with cash at a supermarket.', 'ans': False, 'why': 'Most stores accept cards, and many accept phone payments too.'},
   {'s': 'In every US city, plastic bags are free.', 'ans': False, 'why': 'Some cities and states limit plastic bags or charge a small fee.'},
   {'s': 'You must say a full long sentence to the cashier.', 'ans': False, 'why': 'Short answers like “Paper, please.” are normal and polite.'}],
  'wild': [
   {'kind': 'Receipt', 'lines': ['**Bread**  $3.50', '**Milk**  $2.00', '**Apples**  $4.25', '**Total**  $9.75'], 'decode': {'q': 'How much is the milk?', 'opts': ['$2.00', '$3.50', '$9.75'], 'ans': 0, 'why': 'The line says Milk $2.00.'}},
   {'kind': 'Sign at the register', 'lines': ['**Self-checkout**  10 items or less', '**Bags**  5 cents each', '**Please insert your card**'], 'decode': {'q': 'What do you do with your card?', 'opts': ['Insert it', 'Throw it away', 'Give it to a friend'], 'ans': 0, 'why': 'The sign says “Please insert your card”.'}}],
  'compare': {'br': 'In Brazil the cashier often asks “CPF na nota?” and then puts everything in plastic bags.', 'us': 'In the USA the cashier often asks “Paper or plastic?”, and you say your choice in one or two words.', 'tip': 'Answer the question you hear: paper, plastic, card, cash, receipt.', 'ask': 'What does the cashier ask you where you live? Say one question in English.'},
  'quiz': [
   {'q': 'The cashier asks, “Paper or plastic?” You say…', 'opts': ['Paper, please.', 'Yes, bag.', 'I am paper.'], 'ans': 0, 'why': 'Choose one: paper or plastic.'},
   {'q': 'You want to use your card. You ask…', 'opts': ['Can I pay by card?', 'Card I pay?', 'I pay card can?'], 'ans': 0, 'why': 'Can I pay by card? is the natural question.'},
   {'q': '“Do you want the receipt?” You do not need it. You say…', 'opts': ['No, thanks.', 'No receipt am I.', 'Receipt is no.'], 'ans': 0, 'why': 'No, thanks. is short and polite.'}]},
 'reading': {
  'genre': 'Blog post', 'title': 'Sold out at the checkout!',
  'text': [
   'Last Friday, I went to a big store in **San Diego**. It was a sale day, a bit like **Black Friday**, the sales day after Thanksgiving in the United States. Many things were **sold out**. “Selling like hotcakes!” said a man next to me.',
   'I wanted a blue backpack, but the shelf was empty. A worker said, “Sorry, it is **out of stock**.” I said, “**Put me on the list**. Call me when it arrives.” He smiled and wrote my phone number.',
   'Then I went to the checkout. The line was long. Victor, the cashier, said, “Hi! **Did you find everything?**” I said, “Yes, thanks.” He asked, “**Paper or plastic?**” “Paper, please,” I said.',
   'My bag cost twenty-three dollars and fifty cents. I asked, “**Can I pay by card?**” “Yes,” said Victor. “**Insert your card here.**” I pushed the card into the machine and waited. Beep! Then he asked, “Do you want the receipt?” “Yes, please,” I said, because I wanted to keep it.',
   '“**Have a great day!**” said Victor. I said, “You too!” There was a self-checkout next to us, but I like to talk to a real person. A little talk makes shopping nicer.',
   'At home, I looked at my receipt. The total was right. Now I know how a checkout works in English.'],
  'glossary': [{'w': 'sold out', 'pt': 'esgotado'}, {'w': 'out of stock', 'pt': 'sem estoque'}, {'w': 'checkout', 'pt': 'caixa'}, {'w': 'cashier', 'pt': 'caixa (pessoa)'}, {'w': 'receipt', 'pt': 'recibo'}, {'w': 'backpack', 'pt': 'mochila'}, {'w': 'shelf', 'pt': 'prateleira'}, {'w': 'insert', 'pt': 'inserir'}, {'w': 'self-checkout', 'pt': 'caixa de autoatendimento'}],
  'fast': {'q': 'What is this text about?', 'opts': ['Shopping and paying at a store', 'A trip to the beach', 'A morning routine'], 'ans': 0, 'why': 'The writer shops and pays at the checkout.'},
  'scan': [{'q': 'What name does the cashier have?', 'ans': 'Victor', 'alt': []}, {'q': 'What does the writer choose, paper or plastic?', 'ans': 'paper', 'alt': ['a paper bag']}, {'q': 'How much does the bag cost?', 'ans': 'twenty-three dollars and fifty cents', 'alt': ['23.50', '$23.50', '23 dollars fifty']}],
  'tf': [{'s': 'The store is in San Diego.', 'ans': True, 'why': '“A big store in San Diego.”'}, {'s': 'The blue backpack is on the shelf.', 'ans': False, 'why': 'The shelf was empty: it was out of stock.'}, {'s': 'The writer pays with cash.', 'ans': False, 'why': 'The writer pays by card.'}, {'s': 'The writer keeps the receipt.', 'ans': True, 'why': 'The writer says yes to the receipt.'}],
  'order': ['The writer goes to a big store.', 'The backpack is out of stock.', 'The writer asks to be on the list.', 'The cashier asks paper or plastic.', 'The writer pays by card.'],
  'ctx': [{'sent': 'The blue backpack is out of stock.', 'w': 'out of stock', 'opts': ['not in the store now', 'very cheap', 'very big'], 'ans': 0, 'why': 'Out of stock = the store has none.'}, {'sent': 'The line at the checkout was long.', 'w': 'checkout', 'opts': ['where you pay', 'where you sleep', 'where you cook'], 'ans': 0, 'why': 'The checkout is where you pay.'}, {'sent': 'I want to keep the receipt.', 'w': 'receipt', 'opts': ['a paper that shows what you paid', 'a kind of bag', 'a shopping list'], 'ans': 0, 'why': 'A receipt shows your purchase.'}],
  'chunkHunt': ['Did you find everything?', 'Paper or plastic?', 'Can I pay by card?', 'Have a great day!'],
  'think': 'Do you prefer self-checkout or a real cashier? Why?'},
 'convo': {'npc': {'name': 'Victor'}, 'story': 'You are at a supermarket checkout in San Diego. Victor is the cashier.',
  'turns': [
   {'npc': 'Hi! Did you find everything?', 'pt': 'Oi! Achou tudo?', 'opts': [
    {'en': 'I find all, yes.', 'pt': 'Eu acho tudo, sim.', 'ok': False, 'fb': 'Use the past: I found everything.'},
    {'en': 'Yes, thanks.', 'pt': 'Sim, valeu.', 'ok': True, 'fb': 'Short and friendly.'},
    {'en': 'I am a cart.', 'pt': 'Eu sou um carrinho.', 'ok': False, 'fb': 'Wrong meaning.'}]},
   {'npc': 'Paper or plastic?', 'pt': 'Papel ou plástico?', 'opts': [
    {'en': 'Paper, please.', 'pt': 'Papel, por favor.', 'ok': True, 'fb': 'Choose one.'},
    {'en': 'Yes, bag.', 'pt': 'Sim, sacola.', 'ok': False, 'fb': 'Choose paper or plastic.'},
    {'en': 'I am paper.', 'pt': 'Eu sou papel.', 'ok': False, 'fb': 'Wrong meaning.'}]},
   {'npc': 'That’s twenty-three fifty.', 'pt': 'São vinte e três e cinquenta.', 'opts': [
    {'en': 'I pay with card can?', 'pt': 'Eu pago com cartão posso?', 'ok': False, 'fb': 'Word order.'},
    {'en': 'Can I pay by card?', 'pt': 'Posso pagar com cartão?', 'ok': True, 'fb': 'Natural question.'},
    {'en': 'Card is twenty.', 'pt': 'Cartão é vinte.', 'ok': False, 'fb': 'It does not ask to pay.'}]},
   {'npc': 'Yes. Insert your card here.', 'pt': 'Sim. Insira o cartão aqui.', 'opts': [
    {'en': 'Done! Do you want the receipt?', 'pt': 'Pronto! Quer o recibo?', 'ok': False, 'fb': 'The cashier asks that, not you.'},
    {'en': 'No, thanks, I am card.', 'pt': 'Não, valeu, eu sou cartão.', 'ok': False, 'fb': 'Wrong meaning.'},
    {'en': 'OK. Yes, the receipt, please.', 'pt': 'Ok. Sim, o recibo, por favor.', 'ok': True, 'fb': 'Polite and clear.'}]},
   {'npc': 'Have a great day!', 'pt': 'Tenha um ótimo dia!', 'opts': [
    {'en': 'You too! Bye!', 'pt': 'Você também! Tchau!', 'ok': True, 'fb': 'Natural answer.'},
    {'en': 'Good night!', 'pt': 'Boa noite!', 'ok': False, 'fb': 'It is not night.'},
    {'en': 'Yes, I have.', 'pt': 'Sim, eu tenho.', 'ok': False, 'fb': 'It does not answer the wish.'}]}]},
 'errors': [
  {'wrong': 'I pay with card?', 'fix': 'Can I pay by card?', 'alt': 'Can I pay with a card by?', 'why': 'Ask with Can I… and the base verb pay.'},
  {'wrong': 'Plastic or paper, yes.', 'fix': 'Paper, please.', 'alt': 'I paper want.', 'why': 'Choose one word and add please.'},
  {'wrong': 'You want the receipt?', 'fix': 'Do you want the receipt?', 'alt': 'Want you the receipt?', 'why': 'Questions with want use Do you want…?'},
  {'wrong': 'The shelf is out of the stock.', 'fix': 'The shelf is out of stock.', 'alt': 'The shelf is stock out.', 'why': 'Say out of stock, with no “the”.'}],
 'homework': 'Write a short checkout dialogue with a cashier (6 lines) and say it aloud with a friend.',
 'homework_items': ['Write 6 lines at the checkout.', 'Record yourself: Paper, please. / Can I pay by card?', 'Shadow the dialogue with Victor.', 'Review: Did you find everything? / Out of stock. / Put me on the list.']}
