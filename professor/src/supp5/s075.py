"""Suplemento Quest v5 · aula 75: At the mall + regular Could I try it on? (Confessions of a Shopaholic)."""
SUPP = {
 'reg': 152,
 'badge': {'icon': '🛍️', 'name': 'Smart Shopper', 'desc': 'Ask the price, find a sale and pay at the mall'},
 'culture': {
  'hook': 'A mall in the USA is a big building with many shops, a food court and lots of sales. Learn how to ask the price, understand a discount and pay.',
  'mythfact': [
   {'s': '"30% off" means you pay only 30% of the price.', 'ans': False, 'why': '30% off means you save 30%, so you pay 70% of the price.'},
   {'s': 'The price on the tag usually does not include sales tax.', 'ans': True, 'why': 'In most US states, sales tax is added at the register.'},
   {'s': 'Most US malls are open only at night.', 'ans': False, 'why': 'Most malls are open during the day and in the evening, but hours vary.'},
   {'s': 'You can often return an item if you keep the receipt.', 'ans': True, 'why': 'The receipt is usually needed for returns, but each store has its own rules.'},
   {'s': 'In "Confessions of a Shopaholic", the main character loves shopping.', 'ans': True, 'why': 'It is a 2009 comedy about a young woman who cannot stop buying things.'}],
  'wild': [
   {'kind': 'Sale sign', 'lines': ['**BIG SALE**', 'All bags **30% off**', 'This weekend only'], 'decode': {'q': 'When is the bag sale?', 'opts': ['This weekend only', 'Every day', 'Next year'], 'ans': 0, 'why': 'The sign says "This weekend only".'}},
   {'kind': 'Receipt', 'lines': ['**Bag**  $35.00', 'Sales tax  $2.89', '**Total**  $37.89 · Paid by card'], 'decode': {'q': 'How did the customer pay?', 'opts': ['By card', 'With cash', 'With a gift'], 'ans': 0, 'why': 'The receipt says "Paid by card".'}}],
  'compare': {'br': 'In Brazil, the price on the tag usually already includes taxes, and many people ask for parcelas (installments) on the card.', 'us': 'In the USA, tax is added at the register, so the final price is higher than the tag. Sales are shown as "% off".', 'tip': 'Check the tag and think: price + tax = total.', 'ask': 'Do you prefer to pay by cash or by card? Say it in English.'},
  'quiz': [
   {'q': 'You like a bag and want to know the cost. You ask...', 'opts': ['How much is it?', 'How many is it?', 'What is its much?'], 'ans': 0, 'why': 'How much is it? asks the price.'},
   {'q': 'A bag is $50 and it is 30% off. You pay...', 'opts': ['$35', '$20', '$30'], 'ans': 0, 'why': '30% of $50 is $15. $50 - $15 = $35.'},
   {'q': 'At the register, the clerk asks how you pay. You say...', 'opts': ['Card, please.', 'Price, please.', 'Mall, please.'], 'ans': 0, 'why': 'Cash or card? is answered with Card, please or Cash, please.'}]},
 'reading': {
  'genre': 'Blog post',
  'title': 'A Saturday at the mall',
  'text': [
   'Last Saturday, my friend Rosa and I went to the **mall** in **Houston**. It was hot outside, but inside the mall it was cool. There were people, music and shops everywhere.',
   'We walked past many shops. Suddenly Rosa stopped. "Look at this bag! It\'s so cute," she said. It was small and red. "**How much is it?**" I asked. "**It\'s fifty dollars**," she said. That is not **cheap**.',
   'Then I saw a sign: **30% off**. "**Is it on sale?**" I asked. "**Yes, thirty percent off**," said the clerk. Thirty percent of fifty is fifteen, so the new **price** was thirty-five dollars. "**That\'s a good price**," I said. Rosa agreed. "**I\'ll take it.**"',
   'At the register, the clerk asked, "**Cash or card?**" Rosa said, "Card, please." She got a **receipt**. "Keep it," I said. "You can return the bag with the receipt if you want."',
   'I saw a jacket, too. It was perfect, but it was very **expensive**: one hundred and twenty dollars! I said, "**Maybe later.**" My friend smiled. "**Retail therapy!**" she said.',
   'We ended the day with a big juice in the food court. We spent a little, but we had a great time. "**Thanks for coming in!**" said the clerk as we left.'],
  'glossary': [{'w': 'mall', 'pt': 'shopping center'}, {'w': 'cute', 'pt': 'fofa'}, {'w': 'cheap', 'pt': 'barato'}, {'w': 'sign', 'pt': 'placa'}, {'w': 'on sale', 'pt': 'em promoção'}, {'w': 'price', 'pt': 'preço'}, {'w': 'register', 'pt': 'caixa'}, {'w': 'receipt', 'pt': 'recibo'}, {'w': 'return', 'pt': 'devolver'}, {'w': 'expensive', 'pt': 'caro'}],
  'fast': {'q': 'What is this text about?', 'opts': ['Buying a bag on sale at the mall', 'A trip to the airport', 'Cooking at home'], 'ans': 0, 'why': 'Rosa buys a red bag on sale at a mall in Houston.'},
  'scan': [{'q': 'What color is the bag?', 'ans': 'red', 'alt': ['it is red', 'small and red']}, {'q': 'How much is the bag after the discount?', 'ans': '35 dollars', 'alt': ['$35', '35', 'thirty-five dollars', 'thirty-five']}, {'q': 'How much is the jacket?', 'ans': '120 dollars', 'alt': ['$120', '120', 'one hundred and twenty dollars']}],
  'tf': [
   {'s': 'The mall is in Houston.', 'ans': True, 'why': '"...went to the mall in Houston."'},
   {'s': 'The bag costs thirty dollars at first.', 'ans': False, 'why': '"It\'s fifty dollars."'},
   {'s': 'Rosa pays with a card.', 'ans': True, 'why': 'She says, "Card, please."'},
   {'s': 'The narrator buys the jacket.', 'ans': False, 'why': 'She says "Maybe later" because it is expensive.'}],
  'order': ['Rosa and the narrator go to the mall.', 'Rosa sees a cute red bag.', 'They learn it is 30% off.', 'Rosa pays by card and gets a receipt.', 'They drink juice in the food court.'],
  'ctx': [
   {'sent': 'It was not cheap.', 'w': 'cheap', 'opts': ['low in price', 'very big', 'very old'], 'ans': 0, 'why': 'Cheap = low price.'},
   {'sent': 'The jacket was very expensive.', 'w': 'expensive', 'opts': ['high in price', 'small', 'broken'], 'ans': 0, 'why': 'Expensive = costs a lot.'},
   {'sent': 'We spent a little money.', 'w': 'spent', 'opts': ['used money to buy', 'lost', 'found'], 'ans': 0, 'why': 'Spent = paid money.'}],
  'chunkHunt': ['How much is it?', 'Is it on sale?', 'That\'s a good price', 'Cash or card?'],
  'think': 'Do you like going to the mall? What do you usually buy there?'},
 'convo': {'npc': {'name': 'Rosa'}, 'story': 'You are at a mall in Houston with your friend Rosa. She sees a cute bag.', 'turns': [
  {'npc': 'Look at this bag! It\'s so cute.', 'pt': 'Olha esta bolsa! É tão fofa.', 'opts': [
   {'en': 'How much is it?', 'pt': 'Quanto custa?', 'ok': True, 'fb': 'Natural question about the price.'},
   {'en': 'How many is it?', 'pt': 'Quantos é?', 'ok': False, 'fb': 'For price, use How much.'},
   {'en': 'I am a bag.', 'pt': 'Eu sou uma bolsa.', 'ok': False, 'fb': 'No sense.'}]},
  {'npc': 'It\'s fifty dollars.', 'pt': 'São cinquenta dólares.', 'opts': [
   {'en': 'It is a sale?', 'pt': 'É uma venda?', 'ok': False, 'fb': 'The question is Is it on sale?'},
   {'en': 'Is it on sale?', 'pt': 'Está em promoção?', 'ok': True, 'fb': 'Asks about a discount.'},
   {'en': 'Fifty is my age.', 'pt': 'Cinquenta é minha idade.', 'ok': False, 'fb': 'It does not fit.'}]},
  {'npc': 'Yes, thirty percent off.', 'pt': 'Sim, trinta por cento de desconto.', 'opts': [
   {'en': 'That\'s a good price.', 'pt': 'É um bom preço.', 'ok': True, 'fb': 'Natural comment about a deal.'},
   {'en': 'I am off.', 'pt': 'Eu saí.', 'ok': False, 'fb': 'Wrong meaning of off.'},
   {'en': 'Thirty is Tuesday.', 'pt': 'Trinta é terça.', 'ok': False, 'fb': 'No sense.'}]},
  {'npc': 'I\'ll take it.', 'pt': 'Vou levar.', 'opts': [
   {'en': 'You take it me.', 'pt': 'Você leva isso eu.', 'ok': False, 'fb': 'Not correct English.'},
   {'en': 'I am the price.', 'pt': 'Eu sou o preço.', 'ok': False, 'fb': 'No sense.'},
   {'en': 'Cash or card?', 'pt': 'Dinheiro ou cartão?', 'ok': True, 'fb': 'The next step is paying.'}]}]},
 'homework': 'Find one thing you want to buy. Write in English its price, the discount and how you want to pay.',
 'homework_items': ['Write 4 sentences about something you want: price, sale, cheap or expensive.', 'Record yourself asking: How much is it? Is it on sale?', 'Listen to the dialogue again and shadow Rosa.', 'Review: How much is it? / Is it on sale? / That\'s a good price.'],
 'errors': [
  {'wrong': 'How many is it?', 'fix': 'How much is it?', 'alt': 'How much costs?', 'why': 'For price, say How much is it?'},
  {'wrong': 'It is in sale?', 'fix': 'Is it on sale?', 'alt': 'It is on sale?', 'why': 'Say on sale, and in questions put is first.'},
  {'wrong': 'It costs fifty dollar.', 'fix': 'It costs fifty dollars.', 'alt': 'It cost fifty dollars.', 'why': 'More than one dollar is plural: dollars.'},
  {'wrong': 'Is very expensive.', 'fix': 'It\'s very expensive.', 'alt': 'This very expensive.', 'why': 'English needs a subject: it is.'}]}
