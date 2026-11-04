X = dict(
 key={'big': 'White or wheat?', 'label': 'Montar o sanduíche', 'sub': 'No balcão de sanduíches dos EUA, o atendente pergunta o tipo de pão e os recheios; você responde escolhendo.'},
 mini=[
  {'who': 'Marco', 'en': 'Hi! What can I get you {today|for lunch|now}?', 'pt': 'Oi! O que posso servir {hoje|no almoço|agora}?'},
  {'who': 'You', 'en': 'Can I have a {turkey|chicken|cheese} sandwich?', 'pt': 'Posso pegar um sanduíche de {peru|frango|queijo}?'},
  {'who': 'Marco', 'en': 'Sure. Do you want {white|wheat|rye} bread?', 'pt': 'Claro. Quer pão {branco|integral|de centeio}?'},
  {'who': 'You', 'en': '{Wheat|White|A roll}, please. And a {salad|soup|drink}.', 'pt': '{Integral|Branco|Francês}, por favor. E uma {salada|sopa|bebida}.'}],
 dlg=[
  {'who': 'Marco', 'en': 'Hi! What can I get you?', 'pt': 'Oi! O que posso servir?'},
  {'who': 'You', 'en': 'Can I have a {turkey|chicken|cheese} sandwich?', 'pt': 'Posso pegar um sanduíche de {peru|frango|queijo}?'},
  {'who': 'Marco', 'en': 'Sure. White or {wheat|rye|a roll}?', 'pt': 'Claro. Pão branco ou {integral|de centeio|francês}?'},
  {'who': 'You', 'en': '{Wheat|White|Rye}, please.', 'pt': '{Integral|Branco|De centeio}, por favor.'},
  {'who': 'Marco', 'en': 'Any {cheese|onions|mustard}? Lettuce? Tomato?', 'pt': 'Algum {queijo|cebola|mostarda}? Alface? Tomate?'},
  {'who': 'You', 'en': 'Yes, all of them.', 'pt': 'Sim, tudo isso.'},
  {'who': 'Marco', 'en': 'Would you like {fries|chips|soup} or a salad?', 'pt': 'Quer {batata frita|batata chips|sopa} ou salada?'},
  {'who': 'You', 'en': 'A {salad|soup|drink}, please.', 'pt': 'Uma {salada|sopa|bebida}, por favor.'},
  {'who': 'Marco', 'en': 'Enjoy your {lunch|sandwich|meal}!', 'pt': 'Bom {almoço|sanduíche|apetite}!'}],
 vocab=[
  {'w': 'sandwich', 'pt': 'sanduíche', 'e': '🥪', 'ex': ['I’d like a turkey sandwich.', 'The sandwich is big.']},
  {'w': 'salad', 'pt': 'salada', 'e': '🥗', 'ex': ['A salad, please.', 'This salad has tomato.']},
  {'w': 'cheese', 'pt': 'queijo', 'e': '🧀', 'ex': ['Any cheese?', 'I like cheese on my sandwich.']},
  {'w': 'pickle', 'pt': 'picles', 'e': '🥒', 'ex': ['I want a pickle.', 'The pickle is sour.']},
  {'w': 'chicken', 'pt': 'frango', 'e': '🍗', 'ex': ['I’ll have the chicken sandwich.', 'The chicken is hot.']},
  {'w': 'bread', 'pt': 'pão', 'e': '🍞', 'ex': ['White or wheat bread?', 'The bread is fresh.']}],
 molds=[
  {'title': 'Pedir o sanduíche', 'frame': 'Can I have a {filling} sandwich?', 'slots': [{'key': 'filling', 'opts': ['turkey', 'chicken', 'cheese']}], 'model': 'Can I have a turkey sandwich?', 'note': 'Can I have a…? é o pedido simples e comum.'},
  {'title': 'Escolher o pão', 'frame': '{bread}, please. With {extra}.', 'slots': [{'key': 'bread', 'opts': ['Wheat', 'White', 'Rye']}, {'key': 'extra', 'opts': ['lettuce', 'tomato', 'cheese']}], 'model': 'Wheat, please. With lettuce.', 'note': 'Responda à escolha com uma palavra e use with para o recheio.'},
  {'title': 'Escolher o acompanhamento (escrever)', 'frame': 'A {side}, please. And {drink}.', 'slots': [{'key': 'side', 'opts': ['salad', 'soup', 'small salad']}, {'key': 'drink', 'opts': ['water', 'a juice', 'a tea']}], 'model': 'A salad, please. And water.', 'note': 'Acompanhamento e bebida cabem em duas frases curtas.'}],
 sounds=[
  {'say': 'White or wheat?', 'tag': 'ligação: or', 'tip': 'Or fica fraco e se junta a white: “whi-tor wheat”. A subida marca a pergunta de escolha.'},
  {'say': 'Can I have a turkey sandwich?', 'tag': 'ligação: can I', 'tip': 'Junte can e I: “kenai”. Sandwich perde o d: “SAN-wich”.'},
  {'say': 'Lettuce, tomato, cheese.', 'tag': 'ritmo: lista', 'tip': 'Numa lista, a voz sobe nos itens e desce no último.'}],
 role={'turns': [
  {'npc': 'Hi! What can I get you?', 'opts': [
   {'en': 'Can I have a turkey sandwich?', 'pt': 'Posso pegar um sanduíche de peru?', 'reply': 'Sure. White or wheat bread?'},
   {'en': 'Can I have a chicken sandwich?', 'pt': 'Posso pegar um sanduíche de frango?', 'reply': 'Sure. White or wheat bread?'},
   {'en': 'I’d like a cheese sandwich, please.', 'pt': 'Eu gostaria de um sanduíche de queijo, por favor.', 'reply': 'Sure. White or wheat bread?'}]},
  {'npc': 'Sure. White or wheat bread?', 'opts': [
   {'en': 'Wheat, please.', 'pt': 'Integral, por favor.', 'reply': 'Wheat. Any cheese? Lettuce? Tomato?'},
   {'en': 'White, please.', 'pt': 'Branco, por favor.', 'reply': 'White. Any cheese? Lettuce? Tomato?'},
   {'en': 'Wheat bread, thanks.', 'pt': 'Pão integral, obrigado.', 'reply': 'Wheat. Any cheese? Lettuce? Tomato?'}]},
  {'npc': 'Any cheese? Lettuce? Tomato?', 'opts': [
   {'en': 'Yes, all of them.', 'pt': 'Sim, tudo isso.', 'reply': 'All of them. Would you like fries or a salad?'},
   {'en': 'Lettuce and tomato, no cheese.', 'pt': 'Alface e tomate, sem queijo.', 'reply': 'No cheese. Would you like fries or a salad?'},
   {'en': 'Just cheese, please.', 'pt': 'Só queijo, por favor.', 'reply': 'Just cheese. Would you like fries or a salad?'}]},
  {'npc': 'Would you like fries or a salad?', 'opts': [
   {'en': 'A salad, please.', 'pt': 'Uma salada, por favor.', 'reply': 'One salad. Enjoy your lunch!'},
   {'en': 'Fries, please.', 'pt': 'Batata frita, por favor.', 'reply': 'Fries. Enjoy your lunch!'},
   {'en': 'A small salad, thanks.', 'pt': 'Uma salada pequena, obrigado.', 'reply': 'A small salad. Enjoy your lunch!'}]}],
  'change': ['Você não come carne: peça um sanduíche só de queijo e tomate.', 'Você não entendeu a pergunta: peça para ele repetir devagar.', 'Você quer levar: diga que é para levar (to go).']},
 writing={'task': 'Escreva seu pedido de almoço para Marco: sanduíche, pão, recheios e acompanhamento.',
  'model': 'Hi! Can I have a chicken sandwich on wheat bread? I’d like lettuce and tomato. A salad, please. Thank you!',
  'kw': ['sandwich', 'bread', 'salad', 'please'],
  'checks': ['Pedi o sanduíche com Can I have…?', 'Escolhi o pão e os recheios.', 'Escolhi o acompanhamento.']},
 scenes={'pool': ['cafe', 'cafe2', 'cafe3', 'bakery', 'supermarket'], 'npc': {'g': 'm', 'role': 'cook'}, 'you': {'g': 'f'}},
 convo={'npc': {'name': 'Marco'}, 'story': 'Você está numa lanchonete na hora do almoço. Monte seu sanduíche com Marco.', 'turns': [
  {'npc': 'Hi! What can I get you?', 'pt': 'Oi! O que posso servir?', 'opts': [
   {'en': 'Can I have a turkey sandwich?', 'pt': 'Posso pegar um sanduíche de peru?', 'ok': True, 'fb': 'Pedido educado e claro.'},
   {'en': 'I’m a good cook.', 'pt': 'Sou um bom cozinheiro.', 'ok': False, 'fb': 'Quem cozinha é Marco; você é o cliente.'},
   {'en': 'Enjoy your lunch!', 'pt': 'Bom almoço!', 'ok': False, 'fb': 'Quem diz isso é o atendente, no fim.'}]},
  {'npc': 'Sure. White or wheat bread?', 'pt': 'Claro. Pão branco ou integral?', 'opts': [
   {'en': 'Yes, please.', 'pt': 'Sim, por favor.', 'ok': False, 'fb': 'É pergunta de escolha: diga white ou wheat.'},
   {'en': 'I like bread.', 'pt': 'Eu gosto de pão.', 'ok': False, 'fb': 'Não escolhe o tipo de pão.'},
   {'en': 'Wheat, please.', 'pt': 'Integral, por favor.', 'ok': True, 'fb': 'Escolhe uma das opções.'}]},
  {'npc': 'Any cheese? Lettuce? Tomato?', 'pt': 'Queijo? Alface? Tomate?', 'opts': [
   {'en': 'Wheat, please.', 'pt': 'Integral, por favor.', 'ok': False, 'fb': 'O pão já foi escolhido; agora são os recheios.'},
   {'en': 'Yes, all of them.', 'pt': 'Sim, tudo isso.', 'ok': True, 'fb': 'Aceita todos os recheios.'},
   {'en': 'No, I’m not a sandwich.', 'pt': 'Não, eu não sou um sanduíche.', 'ok': False, 'fb': 'Não faz sentido nesta pergunta.'}]},
  {'npc': 'Would you like fries or a salad?', 'pt': 'Quer batata frita ou salada?', 'opts': [
   {'en': 'Lettuce and tomato, please.', 'pt': 'Alface e tomate, por favor.', 'ok': False, 'fb': 'Os recheios já foram escolhidos.'},
   {'en': 'A turkey sandwich.', 'pt': 'Um sanduíche de peru.', 'ok': False, 'fb': 'O sanduíche já foi pedido; agora é o acompanhamento.'},
   {'en': 'A salad, please.', 'pt': 'Uma salada, por favor.', 'ok': True, 'fb': 'Escolhe entre fries e salad.'}]},
  {'npc': 'Enjoy your lunch!', 'pt': 'Bom almoço!', 'opts': [
   {'en': 'Thanks! You too.', 'pt': 'Obrigado! Você também.', 'ok': True, 'fb': 'Resposta cordial e natural.'},
   {'en': 'What can I get you?', 'pt': 'O que posso servir?', 'ok': False, 'fb': 'Essa é a pergunta do atendente.'},
   {'en': 'White or wheat?', 'pt': 'Branco ou integral?', 'ok': False, 'fb': 'O pão já foi escolhido; é hora de agradecer.'}]}]},
)
