X = dict(
 key={'big': 'White rice or brown rice?', 'label': 'Montar o seu bowl', 'sub': 'Em lanchonetes de bowl, você escolhe a base, a proteína e os molhos em etapas; ao terminar, o atendente pergunta se quer mais algo.'},
 mini=[
  {'who': 'Kai', 'en': 'Hi! What kind of {bowl|salad|burrito}?', 'pt': 'Oi! Que tipo de {bowl|salada|burrito}?'},
  {'who': 'You', 'en': 'A {chicken|beef|veggie} bowl, please.', 'pt': 'Um bowl de {frango|carne|legumes}, por favor.'},
  {'who': 'Kai', 'en': 'White rice or {brown|yellow|black} rice? Salsa? Cheese?', 'pt': 'Arroz branco ou arroz {integral|amarelo|preto}? Molho? Queijo?'},
  {'who': 'You', 'en': 'Brown rice. With {beans|corn|avocado}. No {guacamole|cheese|salsa}.', 'pt': 'Arroz integral. Com {feijão|milho|abacate}. Sem {guacamole|queijo|molho}.'}],
 dlg=[
  {'who': 'Kai', 'en': 'Hi! What kind of {bowl|salad|burrito}?', 'pt': 'Oi! Que tipo de {bowl|salada|burrito}?'},
  {'who': 'You', 'en': 'A {chicken|beef|veggie} bowl, please.', 'pt': 'Um bowl de {frango|carne|legumes}, por favor.'},
  {'who': 'Kai', 'en': 'White rice or {brown|black|yellow} rice?', 'pt': 'Arroz branco ou arroz {integral|preto|amarelo}?'},
  {'who': 'You', 'en': '{Brown|White|Yellow} rice. With {beans|corn|vegetables}.', 'pt': 'Arroz {integral|branco|amarelo}. Com {feijão|milho|legumes}.'},
  {'who': 'Kai', 'en': '{Salsa|Beans|Lettuce}? Cheese? Guacamole?', 'pt': '{Molho|Feijão|Alface}? Queijo? Guacamole?'},
  {'who': 'You', 'en': 'Salsa and {cheese|lettuce|corn}. No guacamole.', 'pt': 'Molho e {queijo|alface|milho}. Sem guacamole.'},
  {'who': 'Kai', 'en': 'Anything else?', 'pt': 'Mais alguma coisa?'},
  {'who': 'You', 'en': 'No, that’s it. How much?', 'pt': 'Não, é isso. Quanto custa?'},
  {'who': 'Kai', 'en': 'Enjoy your {bowl|lunch|meal}!', 'pt': 'Aproveite seu {bowl|almoço|prato}!'}],
 vocab=[
  {'w': 'bowl', 'pt': 'tigela', 'e': '🥣', 'ex': ['A chicken bowl, please.', 'The bowl is big.']},
  {'w': 'rice', 'pt': 'arroz', 'e': '🍚', 'ex': ['Brown rice, please.', 'The rice is hot.']},
  {'w': 'beans', 'pt': 'feijão', 'e': '🫘', 'ex': ['Rice with beans, please.', 'I like beans.']},
  {'w': 'avocado', 'pt': 'abacate', 'e': '🥑', 'ex': ['Avocado is green.', 'I’d like avocado on top.']},
  {'w': 'salsa', 'pt': 'molho de tomate', 'e': '🍅', 'ex': ['Salsa and cheese, please.', 'The salsa is spicy.']},
  {'w': 'cheese', 'pt': 'queijo', 'e': '🧀', 'ex': ['Cheese, please.', 'No cheese for me.']}],
 molds=[
  {'title': 'Pedir o bowl', 'frame': 'A {protein} bowl with {base}, please.', 'slots': [{'key': 'protein', 'opts': ['chicken', 'beef', 'veggie']}, {'key': 'base', 'opts': ['brown rice', 'white rice', 'beans']}], 'model': 'A chicken bowl with brown rice, please.', 'note': 'Bowl é a palavra principal; a proteína vem antes dela.'},
  {'title': 'Escolher molhos', 'frame': '{sauce} and {extra}. No {skip}.', 'slots': [{'key': 'sauce', 'opts': ['Salsa', 'Corn', 'Beans']}, {'key': 'extra', 'opts': ['cheese', 'lettuce', 'avocado']}, {'key': 'skip', 'opts': ['guacamole', 'onions', 'sour cream']}], 'model': 'Salsa and cheese. No guacamole.', 'note': 'No + item pede para tirar aquele ingrediente.'},
  {'title': 'Fechar o pedido (escrever)', 'frame': 'No, that’s it. {question}', 'slots': [{'key': 'question', 'opts': ['How much?', 'How much is it?', 'Thanks!']}], 'model': 'No, that’s it. How much?', 'note': 'That’s it encerra o pedido; depois pergunte o preço ou agradeça.'}],
 sounds=[
  {'say': 'White rice or brown rice?', 'tag': 'entonação: escolha', 'tip': 'A voz sobe em white rice e desce em brown rice.'},
  {'say': 'Salsa and cheese.', 'tag': 'redução: and', 'tip': 'And vira “n”: “salsa-n-cheese”.'},
  {'say': 'No, that’s it.', 'tag': 'ritmo: that’s it', 'tip': 'That’s it soa “thats-it”, curto, com força em it.'}],
 role={'turns': [
  {'npc': 'Hi! What kind of bowl?', 'opts': [
   {'en': 'A chicken bowl, please.', 'pt': 'Um bowl de frango, por favor.', 'reply': 'Chicken. White rice or brown rice?'},
   {'en': 'A veggie bowl, please.', 'pt': 'Um bowl de legumes, por favor.', 'reply': 'Veggie. White rice or brown rice?'},
   {'en': 'A beef bowl, please.', 'pt': 'Um bowl de carne, por favor.', 'reply': 'Beef. White rice or brown rice?'}]},
  {'npc': 'White rice or brown rice?', 'opts': [
   {'en': 'Brown rice. With beans.', 'pt': 'Arroz integral. Com feijão.', 'reply': 'Brown rice and beans. Salsa? Cheese? Guacamole?'},
   {'en': 'White rice, please. With corn.', 'pt': 'Arroz branco, por favor. Com milho.', 'reply': 'White rice and corn. Salsa? Cheese? Guacamole?'},
   {'en': 'Brown rice, please.', 'pt': 'Arroz integral, por favor.', 'reply': 'Brown rice. Salsa? Cheese? Guacamole?'}]},
  {'npc': 'Salsa? Cheese? Guacamole?', 'opts': [
   {'en': 'Salsa and cheese. No guacamole.', 'pt': 'Molho e queijo. Sem guacamole.', 'reply': 'Salsa and cheese. Anything else?'},
   {'en': 'All of them, please.', 'pt': 'Tudo isso, por favor.', 'reply': 'All three. Anything else?'},
   {'en': 'Just guacamole, please.', 'pt': 'Só guacamole, por favor.', 'reply': 'Guacamole only. Anything else?'}]},
  {'npc': 'Anything else?', 'opts': [
   {'en': 'No, that’s it. How much?', 'pt': 'Não, é isso. Quanto custa?', 'reply': 'That’s ten dollars. Enjoy your bowl!'},
   {'en': 'No, thanks. How much is it?', 'pt': 'Não, obrigado. Quanto é?', 'reply': 'That’s ten dollars. Enjoy your bowl!'},
   {'en': 'That’s all, thank you.', 'pt': 'É tudo, obrigado.', 'reply': 'OK! That’s ten dollars. Enjoy your bowl!'}]}],
  'change': ['Você tem alergia a abacate: peça sem guacamole e explique.', 'Kai não entendeu um item: repita mais devagar.', 'Você quer uma segunda bebida: peça antes de pagar.']},
 writing={'task': 'Escreva o seu bowl ideal para Kai: proteína, arroz, dois acompanhamentos e um item que você não quer.',
  'model': 'Hi! A chicken bowl with brown rice, please. Beans and salsa. No guacamole. Thank you!',
  'kw': ['bowl', 'rice', 'salsa', 'guacamole'],
  'checks': ['Pedi o bowl com a proteína.', 'Escolhi arroz e acompanhamentos.', 'Usei No… para tirar um item.']},
 scenes={'pool': ['cafe', 'cafe2', 'cafe3', 'restaurant', 'market'], 'npc': {'g': 'm', 'role': 'cook'}, 'you': {'g': 'f'}},
 convo={'npc': {'name': 'Kai'}, 'story': 'Você está numa lanchonete de bowls. Kai pergunta etapa por etapa. Monte o seu.', 'turns': [
  {'npc': 'Hi! What kind of bowl?', 'pt': 'Oi! Que tipo de bowl?', 'opts': [
   {'en': 'A chicken bowl, please.', 'pt': 'Um bowl de frango, por favor.', 'ok': True, 'fb': 'Diz o tipo de bowl.'},
   {'en': 'It is a big bowl.', 'pt': 'É uma tigela grande.', 'ok': False, 'fb': 'Descreve o tamanho, mas Kai pergunta o tipo.'},
   {'en': 'Enjoy your bowl!', 'pt': 'Aproveite seu bowl!', 'ok': False, 'fb': 'Quem diz isso é o atendente, no fim.'}]},
  {'npc': 'White rice or brown rice?', 'pt': 'Arroz branco ou integral?', 'opts': [
   {'en': 'Yes, rice.', 'pt': 'Sim, arroz.', 'ok': False, 'fb': 'É pergunta de escolha: white ou brown.'},
   {'en': 'A chicken bowl, please.', 'pt': 'Um bowl de frango, por favor.', 'ok': False, 'fb': 'Você já escolheu o bowl; agora é o arroz.'},
   {'en': 'Brown rice. With beans.', 'pt': 'Arroz integral. Com feijão.', 'ok': True, 'fb': 'Escolhe o arroz e acrescenta feijão.'}]},
  {'npc': 'Salsa? Cheese? Guacamole?', 'pt': 'Molho? Queijo? Guacamole?', 'opts': [
   {'en': 'Brown rice, please.', 'pt': 'Arroz integral, por favor.', 'ok': False, 'fb': 'O arroz já foi escolhido; agora os molhos.'},
   {'en': 'Salsa and cheese. No guacamole.', 'pt': 'Molho e queijo. Sem guacamole.', 'ok': True, 'fb': 'Escolhe e recusa um item.'},
   {'en': 'It is green.', 'pt': 'É verde.', 'ok': False, 'fb': 'Não responde ao que ele pergunta.'}]},
  {'npc': 'Anything else?', 'pt': 'Mais alguma coisa?', 'opts': [
   {'en': 'No, that’s it. How much?', 'pt': 'Não, é isso. Quanto custa?', 'ok': True, 'fb': 'Encerra o pedido e pergunta o preço.'},
   {'en': 'Yes, I am.', 'pt': 'Sim, eu estou.', 'ok': False, 'fb': 'Anything else? pede o item, não “estar”.'},
   {'en': 'What kind of bowl?', 'pt': 'Que tipo de bowl?', 'ok': False, 'fb': 'Essa pergunta é do atendente.'}]},
  {'npc': 'Enjoy your bowl!', 'pt': 'Aproveite seu bowl!', 'opts': [
   {'en': 'Thanks! Have a good day.', 'pt': 'Obrigado! Tenha um bom dia.', 'ok': True, 'fb': 'Agradece e se despede.'},
   {'en': 'Salsa? Cheese?', 'pt': 'Molho? Queijo?', 'ok': False, 'fb': 'O bowl já está pronto.'},
   {'en': 'Hi! What kind of bowl?', 'pt': 'Oi! Que tipo de bowl?', 'ok': False, 'fb': 'É uma saudação de início; agora é o fim.'}]}]},
)
