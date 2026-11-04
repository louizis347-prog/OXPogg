"""Suplemento Quest v5 · aula 175: Self-checkout + regular There isn't any left (Jack Sprat)."""
SUPP = {
 'reg': 139,
 'badge': {'icon': '🛒', 'name': 'Self-Checkout Star', 'desc': 'Use a self-checkout: scan, bag, weigh and pay'},
 'culture': {
  'hook': 'Many US supermarkets have self-checkout machines. You scan your own items, put them in a bag and pay. A store worker stands near the machines to help if there is a problem.',
  'mythfact': [
   {'s': 'At a self-checkout, you scan your own items.', 'ans': True, 'why': 'That is the main idea: you do the work of the cashier.'},
   {'s': 'There is never a worker to help at a self-checkout.', 'ans': False, 'why': 'Usually a worker stays nearby and helps with problems.'},
   {'s': 'Fruit and vegetables often need to be weighed.', 'ans': True, 'why': 'You choose the item on the screen and put it on the scale.'},
   {'s': 'The machine says “unexpected item” when it is happy.', 'ans': False, 'why': 'It means the machine finds something in the bag area that it did not expect.'},
   {'s': '“Jack Sprat” is a traditional English rhyme.', 'ans': True, 'why': 'It is known since the 1600s.'}],
  'wild': [
   {'kind': 'Self-checkout screen', 'lines': ['**Scan your first item**', 'Place items in the bag area', 'Need help? Touch the blue button'], 'decode': {'q': 'What do you do first?', 'opts': ['Scan your first item', 'Pay with cash', 'Weigh the bag'], 'ans': 0, 'why': 'The screen says “Scan your first item.”'}},
   {'kind': 'Receipt', 'lines': ['**Apples 2.10 lb** $3.15', 'Bread $2.50', 'Total $5.65'], 'decode': {'q': 'How much is the bread?', 'opts': ['$2.50', '$3.15', '$5.65'], 'ans': 0, 'why': 'The receipt says Bread $2.50.'}}],
  'compare': {'br': 'In Brazil, self-checkout machines also exist in some large supermarkets, but many people still use a cashier.', 'us': 'In the USA, many supermarkets have a row of self-checkout machines, and a worker helps when the machine has a problem.', 'tip': 'Ask: “Excuse me, how does this work?”', 'ask': 'Do you prefer a cashier or a self-checkout? Say it in English.'},
  'quiz': [
   {'q': 'You do not know how the machine works. You ask…', 'opts': ['Excuse me, how does this work?', 'Excuse me, how work this?', 'Excuse me, this works how?'], 'ans': 0, 'why': 'Question: how + does + this + work.'},
   {'q': 'You want to weigh apples. You choose…', 'opts': ['produce on the screen', 'cash on the screen', 'bag on the screen'], 'ans': 0, 'why': 'Fruit and vegetables are “produce”.'},
   {'q': 'The machine says “unexpected item.” You…', 'opts': ['put the item in the bag', 'run away', 'scan it ten times'], 'ans': 0, 'why': 'Put it in the bag area and the machine can count it.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'No cashier today',
  'text': [
   'Tom lives in **Houston**. His fridge is empty. There is no cheese, no bread and no fruit, so it is time to **stock up**. He goes to the supermarket with a cart.',
   'At the end of the store, there are no cashiers. Tom goes to the self-checkout. “**Excuse me, how does this work?**” he asks. Rosa works at the store. “**Scan each item, then pay.**” “**Where do I scan?**” “**Here, on the red light.**”',
   'Tom scans the cheese and the bread. Then the machine says, “unexpected item.” “**Put it in the bag first**,” Rosa says. Tom puts the bread in the bag. “**Oh, I see. Now it works.**”',
   '“**How do I weigh the apples?**” Tom asks. “**Choose ‘produce’ on the screen.**” Tom touches the screen and puts the apples and three lemons on the scale. The bag is heavy now.',
   'At home, Tom thinks about “Jack Sprat,” an old English rhyme. Jack could eat no fat, and his wife could eat no lean, so between the two of them they cleaned the platter. Tom smiles. Now his fridge is full, and he does not **run out of** food.'],
  'glossary': [{'w': 'fridge', 'pt': 'geladeira'}, {'w': 'empty', 'pt': 'vazio'}, {'w': 'cart', 'pt': 'carrinho'}, {'w': 'cashiers', 'pt': 'caixas (pessoas)'}, {'w': 'scan', 'pt': 'escanear'}, {'w': 'item', 'pt': 'item'}, {'w': 'weigh', 'pt': 'pesar'}, {'w': 'screen', 'pt': 'tela'}, {'w': 'lemons', 'pt': 'limões'}, {'w': 'heavy', 'pt': 'pesado'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A man learns to use a self-checkout', 'A man cooks apples', 'A woman works as a cashier'], 'ans': 0, 'why': 'Tom asks Rosa how the machine works.'},
  'scan': [{'q': 'Where does Tom scan?', 'ans': 'on the red light', 'alt': ['red light', 'the red light']}, {'q': 'What does Tom put in the bag first?', 'ans': 'the bread', 'alt': ['bread']}, {'q': 'What does Tom choose on the screen?', 'ans': 'produce', 'alt': ['‘produce’', 'the word produce']}],
  'tf': [{'s': 'Tom’s fridge is empty.', 'ans': True, 'why': 'There is no cheese, bread or fruit.'}, {'s': 'There are many cashiers at the end of the store.', 'ans': False, 'why': 'There are no cashiers.'}, {'s': 'Tom puts the bread in the bag, and the machine works.', 'ans': True, 'why': '“Oh, I see. Now it works.”'}, {'s': 'Tom buys three oranges.', 'ans': False, 'why': 'He buys apples and three lemons.'}],
  'order': ['Tom goes to the self-checkout.', 'Rosa tells him to scan each item.', 'The machine says unexpected item.', 'Tom puts the bread in the bag.', 'Tom weighs the apples.'],
  'ctx': [{'sent': 'The bag is heavy now.', 'w': 'heavy', 'opts': ['not light', 'very small', 'very cold'], 'ans': 0, 'why': 'Heavy = hard to lift.'}, {'sent': 'His fridge is empty.', 'w': 'empty', 'opts': ['with nothing inside', 'very full', 'very old'], 'ans': 0, 'why': 'Empty = nothing inside.'}, {'sent': 'How do I weigh the apples?', 'w': 'weigh', 'opts': ['find how heavy they are', 'cut them', 'wash them'], 'ans': 0, 'why': 'Weigh = measure weight.'}],
  'chunkHunt': ['How does this work?', 'Scan each item, then pay.', 'Put it in the bag first.', 'How do I weigh the apples?'],
  'think': 'Do you like self-checkout machines? Why or why not?'},
 'convo': {'npc': {'name': 'Rosa'}, 'story': 'You are at a supermarket in Houston. Rosa works near the self-checkout. Ask her for help.', 'turns': [
  {'npc': 'Hi! Can I help you?', 'pt': 'Oi! Posso ajudar?', 'opts': [
   {'en': 'Excuse me, how does this work?', 'pt': 'Com licença, como isso funciona?', 'ok': True, 'fb': 'Polite question for help.'},
   {'en': 'Excuse me, how work this?', 'pt': 'Com licença, como funciona isso?', 'ok': False, 'fb': 'Use how does this work?'},
   {'en': 'Yes, I am a machine.', 'pt': 'Sim, eu sou uma máquina.', 'ok': False, 'fb': 'Does not fit.'}]},
  {'npc': 'Scan each item, then pay.', 'pt': 'Escaneie cada item, depois pague.', 'opts': [
   {'en': 'Cash or card?', 'pt': 'Dinheiro ou cartão?', 'ok': False, 'fb': 'Not yet: first you need to scan.'},
   {'en': 'I scan where?', 'pt': 'Eu escaneio onde?', 'ok': False, 'fb': 'Use Where do I scan?'},
   {'en': 'Where do I scan?', 'pt': 'Onde escaneio?', 'ok': True, 'fb': 'Correct question order.'}]},
  {'npc': 'Here, on the red light.', 'pt': 'Aqui, na luz vermelha.', 'opts': [
   {'en': 'It says “unexpected item.”', 'pt': 'Diz “item inesperado”.', 'ok': True, 'fb': 'Reports the problem.'},
   {'en': 'The red light is here.', 'pt': 'A luz vermelha está aqui.', 'ok': False, 'fb': 'She just said that.'},
   {'en': 'I scan the red.', 'pt': 'Eu escaneio o vermelho.', 'ok': False, 'fb': 'Does not make sense.'}]},
  {'npc': 'Put it in the bag first.', 'pt': 'Ponha na sacola primeiro.', 'opts': [
   {'en': 'No, the bag is not first.', 'pt': 'Não, a sacola não é a primeira.', 'ok': False, 'fb': 'It does not fit.'},
   {'en': 'Oh, I see. Now it works.', 'pt': 'Ah, entendi. Agora funciona.', 'ok': True, 'fb': 'Shows that you understand.'},
   {'en': 'Where do I scan?', 'pt': 'Onde escaneio?', 'ok': False, 'fb': 'She already answered that.'}]},
  {'npc': 'Great! Anything else?', 'pt': 'Ótimo! Mais alguma coisa?', 'opts': [
   {'en': 'The apples are heavy to scan.', 'pt': 'As maçãs são pesadas para escanear.', 'ok': False, 'fb': 'It does not ask for help.'},
   {'en': 'Yes, thanks, goodbye.', 'pt': 'Sim, obrigado, tchau.', 'ok': False, 'fb': 'Yes means you need more help.'},
   {'en': 'How do I weigh the apples?', 'pt': 'Como peso as maçãs?', 'ok': True, 'fb': 'Next useful question.'}]}]},
 'errors': [
  {'wrong': 'How works this machine?', 'fix': 'How does this machine work?', 'alt': 'How this machine works?', 'why': 'In questions, use does + subject + base verb.'},
  {'wrong': 'I scan where?', 'fix': 'Where do I scan?', 'alt': 'Where I scan?', 'why': 'Question word first, then do + I.'},
  {'wrong': 'Put it inside the bag first.', 'fix': 'Put it in the bag first.', 'alt': 'Put it on bag first.', 'why': 'In the bag is the natural phrase for this.'},
  {'wrong': 'How I weigh the apples?', 'fix': 'How do I weigh the apples?', 'alt': 'How weigh the apples?', 'why': 'Use do in the question: How do I…?'}],
 'homework': 'Write a short dialogue: you ask a worker how to weigh bananas at the self-checkout.',
 'homework_items': ['Write three steps to use a self-checkout.', 'Say aloud: Excuse me, how does this work?', 'Listen to the dialogue and shadow Rosa.', 'Review: scan / bag / weigh / pay.']}
