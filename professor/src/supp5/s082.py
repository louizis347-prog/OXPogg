"""Suplemento Quest v5 · aula 82: Garage sale + regular Sounds good! It's a deal! (Shark Tank)."""
SUPP = {
 'reg': 228,
 'badge': {'icon': '🪑', 'name': 'Deal Maker', 'desc': 'Ask a price, make an offer and close a deal'},
 'sticker': {'cat': 'Everyday culture', 'title': 'The Garage Sale', 'sub': 'Can you do eight?'},
 'culture': {
  'hook': 'In many American towns, people sell old things from their garage or yard on a weekend morning. You can ask the price, make an offer and often pay less than the sign says.',
  'polite': 'Be friendly: **How much is this?**, **Can you do eight?**, **Thanks for stopping by!**',
  'mythfact': [
   {'s': 'A garage sale is where people sell used things from home.', 'ans': True, 'why': 'Families sell old chairs, books, toys and more.'},
   {'s': 'At a garage sale, asking for a lower price is often normal.', 'ans': True, 'why': 'Many sellers expect an offer, such as “Can you do eight?”'},
   {'s': 'Garage sales happen only inside big stores.', 'ans': False, 'why': 'They usually happen in a garage, yard or driveway.'},
   {'s': 'Garage sales are often on weekends.', 'ans': True, 'why': 'Many people have more free time on Saturday or Sunday.'},
   {'s': 'You must always pay the price on the sticker.', 'ans': False, 'why': 'Often you can make a small offer.'}],
  'wild': [
   {'kind': 'Sign on a street', 'lines': ['**GARAGE SALE**', '**Saturday 8 to 12**', 'Lamps $10 · Chairs $15 · Books $1'], 'decode': {'q': 'How much is one chair?', 'opts': ['$10', '$15', '$1'], 'ans': 1, 'why': 'The sign says Chairs $15.'}},
   {'kind': 'Price stickers', 'lines': ['**Toy car**  $2', '**Lamp**  $10', '**Chair**  $15'], 'decode': {'q': 'How much are the lamp and the toy car together?', 'opts': ['$12', '$17', '$25'], 'ans': 0, 'why': '$10 + $2 = $12.'}}],
  'compare': {'br': 'In Brazil people also sell used things at a “bazar” or a “brechó”, and asking for a discount is common.', 'us': 'In the USA a garage sale is often at someone’s house, and many sellers happily say “OK, eight dollars.”', 'tip': 'Make the offer friendly: “Can you do eight?” and smile.', 'ask': 'Have you ever bought something used? Say what it was in English.'},
  'quiz': [
   {'q': 'You want a lower price. You ask…', 'opts': ['Can you do eight?', 'Eight you do?', 'I am eight.'], 'ans': 0, 'why': 'Can you do…? asks for a lower price.'},
   {'q': 'The seller says “Fifteen.” You want to ask the price of a lamp. You say…', 'opts': ['How much is this lamp?', 'How many is lamp?', 'What lamp price?'], 'ans': 0, 'why': 'Use How much is…?'},
   {'q': 'You agree on a price. You say…', 'opts': ['Deal!', 'Dealing no.', 'I deal you.'], 'ans': 0, 'why': 'Deal! = we agree.'}]},
 'reading': {
  'genre': 'Story', 'title': 'A deal on Saturday',
  'text': [
   'Brad lives in **Columbus**. On Saturday morning, he puts a sign on the street: “**Garage sale**.” He has a lamp, a chair, some books and a toy. He wants a **fair price** for each thing.',
   'Andre comes at nine. He sees the lamp. “Hi! **How much is this lamp?**” he asks. “Ten dollars,” says Brad. “**Can you do eight?**” Andre asks. Brad thinks. “OK, eight dollars.” Andre smiles. They both feel good.',
   'Then Andre looks at the chair. “And this chair?” “Fifteen. **It’s in good shape**,” says Brad. Andre says, “I’ll take both for twenty.” Brad says, “**Sounds good! It’s a deal!**” They **shake on it**. The word “deal” means “agreement”. Andre pays with twenty dollars.',
   'Brad likes the day. At home that night, he watches “**Shark Tank**”, an American TV show that started in 2009. People ask rich investors for money, and sometimes they **strike a deal**. Brad laughs: “My garage sale is a very small deal, but I like it.”',
   'The sale ends at noon. Brad has twenty-eight dollars, a clean garage and a happy afternoon. “**Thanks for stopping by!**” he says to the last visitor. “See you next time!”'],
  'glossary': [{'w': 'garage sale', 'pt': 'venda de garagem'}, {'w': 'fair price', 'pt': 'preço justo'}, {'w': 'lamp', 'pt': 'luminária'}, {'w': 'chair', 'pt': 'cadeira'}, {'w': 'in good shape', 'pt': 'em bom estado'}, {'w': 'deal', 'pt': 'acordo'}, {'w': 'shake on it', 'pt': 'apertar as mãos para fechar'}, {'w': 'investors', 'pt': 'investidores'}, {'w': 'strike a deal', 'pt': 'fechar um acordo'}],
  'fast': {'q': 'What is this text about?', 'opts': ['Selling things at a garage sale', 'Cooking dinner', 'Going to the gym'], 'ans': 0, 'why': 'Brad sells things and Andre makes an offer.'},
  'scan': [{'q': 'Where does Brad live?', 'ans': 'Columbus', 'alt': []}, {'q': 'How much does Andre pay for the lamp?', 'ans': 'eight dollars', 'alt': ['8', '$8', '8 dollars']}, {'q': 'What year did Shark Tank start?', 'ans': '2009', 'alt': []}],
  'tf': [{'s': 'The garage sale is on Saturday.', 'ans': True, 'why': '“On Saturday morning.”'}, {'s': 'Andre pays ten dollars for the lamp.', 'ans': False, 'why': 'He asks for eight and pays eight.'}, {'s': 'Andre buys the lamp and the chair.', 'ans': True, 'why': 'He takes both for twenty.'}, {'s': 'Brad is angry at the end.', 'ans': False, 'why': 'He is happy with the day.'}],
  'order': ['Brad puts a sign on the street.', 'Andre asks the price of the lamp.', 'They agree on eight dollars.', 'Andre buys both things for twenty.', 'Brad watches Shark Tank at night.'],
  'ctx': [{'sent': 'The chair is in good shape.', 'w': 'in good shape', 'opts': ['in good condition', 'very old and broken', 'very expensive'], 'ans': 0, 'why': 'In good shape = in good condition.'}, {'sent': 'They shake on it.', 'w': 'shake on it', 'opts': ['show agreement with a handshake', 'dance together', 'drop it'], 'ans': 0, 'why': 'A handshake shows you agree.'}, {'sent': 'It is a fair price.', 'w': 'fair price', 'opts': ['a price that is right', 'a very high price', 'a free thing'], 'ans': 0, 'why': 'Fair = right for both people.'}],
  'chunkHunt': ['How much is this lamp?', 'Can you do eight?', 'Sounds good! It’s a deal!', 'Thanks for stopping by!'],
  'think': 'What would you sell at a garage sale? What price would you ask?'},
 'convo': {'npc': {'name': 'Andre'}, 'story': 'You are at a garage sale in Columbus. Andre is a visitor who wants to buy.',
  'turns': [
   {'npc': 'Hi! How much is this lamp?', 'pt': 'Oi! Quanto custa esta luminária?', 'opts': [
    {'en': 'The lamp is ten.', 'pt': 'A luminária é dez.', 'ok': False, 'fb': 'Add the unit: ten dollars.'},
    {'en': 'Ten dollars.', 'pt': 'Dez dólares.', 'ok': True, 'fb': 'Clear and short.'},
    {'en': 'I am a lamp.', 'pt': 'Eu sou uma luminária.', 'ok': False, 'fb': 'Wrong meaning.'}]},
   {'npc': 'Can you do eight?', 'pt': 'Pode fazer oito?', 'opts': [
    {'en': 'No, nine me.', 'pt': 'Não, nove eu.', 'ok': False, 'fb': 'Word order.'},
    {'en': 'I do not eight.', 'pt': 'Eu não oito.', 'ok': False, 'fb': 'Not natural.'},
    {'en': 'OK, eight dollars.', 'pt': 'Ok, oito dólares.', 'ok': True, 'fb': 'You accept the offer.'}]},
   {'npc': 'And this chair?', 'pt': 'E esta cadeira?', 'opts': [
    {'en': 'Fifteen. It’s in good shape.', 'pt': 'Quinze. Está em bom estado.', 'ok': True, 'fb': 'Price and a reason.'},
    {'en': 'The chair no cost.', 'pt': 'A cadeira não custa.', 'ok': False, 'fb': 'Not natural English.'},
    {'en': 'Chair is fifteen years.', 'pt': 'Cadeira é quinze anos.', 'ok': False, 'fb': 'Years is not money.'}]},
   {'npc': 'I’ll take both for twenty.', 'pt': 'Levo as duas por vinte.', 'opts': [
    {'en': 'I take you twenty.', 'pt': 'Eu levo você vinte.', 'ok': False, 'fb': 'Wrong meaning.'},
    {'en': 'Deal!', 'pt': 'Fechado!', 'ok': True, 'fb': 'Agree with Deal!'},
    {'en': 'Both is bad.', 'pt': 'Os dois é ruim.', 'ok': False, 'fb': 'Not a reply.'}]},
   {'npc': 'Thanks for stopping by!', 'pt': 'Valeu por passar aqui!', 'opts': [
    {'en': 'Thank you! Bye!', 'pt': 'Obrigado! Tchau!', 'ok': True, 'fb': 'Polite answer.'},
    {'en': 'I stop yes.', 'pt': 'Eu paro sim.', 'ok': False, 'fb': 'Not natural.'},
    {'en': 'Good morning!', 'pt': 'Bom dia!', 'ok': False, 'fb': 'Not a goodbye.'}]}]},
 'errors': [
  {'wrong': 'How much costs this lamp?', 'fix': 'How much is this lamp?', 'alt': 'How many is this lamp?', 'why': 'Ask the price with How much is…?'},
  {'wrong': 'You can do eight?', 'fix': 'Can you do eight?', 'alt': 'Do you can eight?', 'why': 'Put Can first in the question.'},
  {'wrong': 'I take the both.', 'fix': 'I’ll take both.', 'alt': 'I take both of the.', 'why': 'Say both with no “the”.'},
  {'wrong': 'It is in good form.', 'fix': 'It’s in good shape.', 'alt': 'It is on good shape.', 'why': 'The fixed expression is in good shape.'}],
 'homework': 'Choose 3 things at home and write their prices, then say a short dialogue to sell them.',
 'homework_items': ['Write 3 things and prices.', 'Record a dialogue: price, offer, deal.', 'Shadow the dialogue with Andre.', 'Review: Can you do eight? / It’s a deal! / Shake on it.']}
