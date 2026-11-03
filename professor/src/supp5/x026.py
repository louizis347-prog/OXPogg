X = dict(
 key={'big': 'What’s in it?', 'label': 'Perguntar os ingredientes', 'sub': 'Antes de comprar ou comer, é normal perguntar o que tem na comida, principalmente se você evita algum ingrediente.'},
 mini=[
  {'who': 'Nina', 'en': 'Hi! These {dumplings|tacos|pies} smell good. What’s in {it|them|this}?', 'pt': 'Oi! Esses {bolinhos|tacos|pasteis} estão com cheiro bom. O que tem {dentro|neles|nisso}?'},
  {'who': 'You', 'en': '{Pork|Beef|Chicken} and {cabbage|rice|mushroom}.', 'pt': '{Carne de porco|Carne bovina|Frango} e {repolho|arroz|cogumelo}.'},
  {'who': 'Nina', 'en': 'I don’t eat {pork|beef|shrimp}. Do you have chicken?', 'pt': 'Não como {porco|carne bovina|camarão}. Tem de frango?'},
  {'who': 'You', 'en': 'Yes! Chicken and {mushroom|cabbage|ginger}.', 'pt': 'Tem! Frango e {cogumelo|repolho|gengibre}.'}],
 dlg=[
  {'who': 'Nina', 'en': 'Hi! These {dumplings|tacos|pies} smell good.', 'pt': 'Oi! Esses {bolinhos|tacos|pasteis} estão com cheiro bom.'},
  {'who': 'You', 'en': 'Thank you! Try one.', 'pt': 'Obrigada! Experimente um.'},
  {'who': 'Nina', 'en': 'What’s in it?', 'pt': 'O que tem dentro?'},
  {'who': 'You', 'en': '{Pork|Beef|Shrimp} and {cabbage|onion|ginger}.', 'pt': '{Carne de porco|Carne bovina|Camarão} e {repolho|cebola|gengibre}.'},
  {'who': 'Nina', 'en': 'I don’t eat {pork|beef|shrimp}. Do you have chicken?', 'pt': 'Não como {porco|carne bovina|camarão}. Tem de frango?'},
  {'who': 'You', 'en': 'Yes! Chicken and {mushroom|cabbage|ginger}.', 'pt': 'Tem! Frango e {cogumelo|repolho|gengibre}.'},
  {'who': 'Nina', 'en': 'Perfect. How much?', 'pt': 'Perfeito. Quanto custa?'},
  {'who': 'You', 'en': '{Six|Four|Ten} for {eight|six|twelve} dollars.', 'pt': '{Seis|Quatro|Dez} por {oito|seis|doze} dólares.'},
  {'who': 'Nina', 'en': 'Enjoy the {dumplings|tacos|pies}!', 'pt': 'Aproveite os {bolinhos|tacos|pasteis}!'}],
 vocab=[
  {'w': 'rice', 'pt': 'arroz', 'e': '🍚', 'ex': ['The dumplings come with rice.', 'I’d like rice, please.']},
  {'w': 'pork', 'pt': 'carne de porco', 'e': '🐖', 'ex': ['These dumplings have pork.', 'I don’t eat pork.']},
  {'w': 'beef', 'pt': 'carne bovina', 'e': '🥩', 'ex': ['Is there beef in it?', 'The beef is fresh.']},
  {'w': 'mushroom', 'pt': 'cogumelo', 'e': '🍄', 'ex': ['Chicken and mushroom, please.', 'I like mushroom soup.']},
  {'w': 'spicy', 'pt': 'picante', 'e': '🌶️', 'ex': ['Is it spicy?', 'I like spicy food.']},
  {'w': 'dumpling', 'pt': 'bolinho recheado', 'e': '🥟', 'ex': ['Try one dumpling.', 'This dumpling is hot.']}],
 molds=[
  {'title': 'Perguntar o que tem', 'frame': 'What’s in {thing}?', 'slots': [{'key': 'thing', 'opts': ['it', 'this', 'the soup']}], 'model': 'What’s in it?', 'note': 'What’s in…? pergunta pelos ingredientes. Não use “What has it?”.'},
  {'title': 'Dizer o que você não come', 'frame': 'I don’t eat {food}. Do you have {other}?', 'slots': [{'key': 'food', 'opts': ['pork', 'beef', 'fish']}, {'key': 'other', 'opts': ['chicken', 'vegetables', 'rice']}], 'model': 'I don’t eat pork. Do you have chicken?', 'note': 'I don’t eat… informa sua restrição; Do you have…? pede uma opção.'},
  {'title': 'Pedir e pagar (escrever)', 'frame': '{number} dumplings, please. Is it {taste}?', 'slots': [{'key': 'number', 'opts': ['Six', 'Four', 'Ten']}, {'key': 'taste', 'opts': ['spicy', 'sweet', 'salty']}], 'model': 'Six dumplings, please. Is it spicy?', 'note': 'Is it spicy? pergunta se a comida é picante.'}],
 sounds=[
  {'say': 'What’s in it?', 'tag': 'ligação: in it', 'tip': 'In e it se unem: “in-nit”. What’s fica curto: “wats”.'},
  {'say': 'I don’t eat pork.', 'tag': 'acento: don’t', 'tip': 'Dê força a don’t e a pork. “I” e “eat” ficam leves e rápidos.'},
  {'say': 'Chicken and mushroom.', 'tag': 'redução: and', 'tip': 'And vira “n”: “chicken-n-mushroom”.'}],
 role={'turns': [
  {'npc': 'Hi! These dumplings smell good.', 'opts': [
   {'en': 'Thank you! Try one.', 'pt': 'Obrigada! Experimente um.', 'reply': 'Thanks! What’s in it?'},
   {'en': 'Thanks! Do you want to try one?', 'pt': 'Obrigada! Quer experimentar um?', 'reply': 'Sure. What’s in it?'},
   {'en': 'Thank you! They are fresh.', 'pt': 'Obrigada! Estão fresquinhos.', 'reply': 'Great! What’s in them?'}]},
  {'npc': 'What’s in it?', 'opts': [
   {'en': 'Pork and cabbage.', 'pt': 'Carne de porco e repolho.', 'reply': 'Oh, I don’t eat pork. Do you have chicken?'},
   {'en': 'Beef and onion.', 'pt': 'Carne bovina e cebola.', 'reply': 'Hmm, I don’t eat beef. Do you have chicken?'},
   {'en': 'Shrimp and ginger.', 'pt': 'Camarão e gengibre.', 'reply': 'Oh, I don’t eat shrimp. Do you have chicken?'}]},
  {'npc': 'I don’t eat pork. Do you have chicken?', 'opts': [
   {'en': 'Yes! Chicken and mushroom.', 'pt': 'Tem! Frango e cogumelo.', 'reply': 'Perfect. How much?'},
   {'en': 'Yes! Chicken and cabbage.', 'pt': 'Tem! Frango e repolho.', 'reply': 'Perfect. How much?'},
   {'en': 'Yes, we do. Chicken and rice.', 'pt': 'Temos sim. Frango e arroz.', 'reply': 'Perfect. How much?'}]},
  {'npc': 'Perfect. How much?', 'opts': [
   {'en': 'Six for eight dollars.', 'pt': 'Seis por oito dólares.', 'reply': 'OK, six, please. Here you go.'},
   {'en': 'Four for six dollars.', 'pt': 'Quatro por seis dólares.', 'reply': 'OK, four, please. Here you go.'},
   {'en': 'Ten for twelve dollars.', 'pt': 'Dez por doze dólares.', 'reply': 'Ten is a lot! Six, please. Here you go.'}]}],
  'change': ['Nina pergunta se é picante: responda que não é, ou que é só um pouco.', 'Nina é vegetariana: ofereça os bolinhos de cogumelo e legumes.', 'O preço mudou: diga o novo preço e peça para ela confirmar.']},
 writing={'task': 'Você vende bolinhos numa feira. Escreva um aviso curto: recheios, um sem carne de porco e o preço.',
  'model': 'Fresh dumplings! Pork and cabbage, or chicken and mushroom. No pork in the chicken ones. Six for eight dollars.',
  'kw': ['dumplings', 'chicken', 'pork', 'dollars'],
  'checks': ['Listei pelo menos dois recheios.', 'Mostrei uma opção sem porco.', 'Escrevi o preço em dollars.']},
 scenes={'pool': ['market', 'supermarket', 'street', 'fair', 'bakery'], 'npc': {'g': 'f', 'role': 'customer'}, 'you': {'g': 'f'}},
 convo={'npc': {'name': 'Nina'}, 'story': 'Você vende bolinhos numa barraca no mercado. Nina é a cliente. Responda a ela.', 'turns': [
  {'npc': 'Hi! These dumplings smell good.', 'pt': 'Oi! Esses bolinhos estão com cheiro bom.', 'opts': [
   {'en': 'Thank you! Try one.', 'pt': 'Obrigada! Experimente um.', 'ok': True, 'fb': 'Agradece e convida a provar.'},
   {'en': 'What’s in it?', 'pt': 'O que tem dentro?', 'ok': False, 'fb': 'Quem pergunta o recheio é a cliente.'},
   {'en': 'I don’t eat pork.', 'pt': 'Não como porco.', 'ok': False, 'fb': 'Você é a vendedora; ela é quem pode ter restrições.'}]},
  {'npc': 'What’s in it?', 'pt': 'O que tem dentro?', 'opts': [
   {'en': 'It is in the market.', 'pt': 'Está no mercado.', 'ok': False, 'fb': 'Ela pergunta os ingredientes, não o lugar.'},
   {'en': 'Six for eight dollars.', 'pt': 'Seis por oito dólares.', 'ok': False, 'fb': 'É o preço; ela pediu o recheio.'},
   {'en': 'Pork and cabbage.', 'pt': 'Carne de porco e repolho.', 'ok': True, 'fb': 'Diz os ingredientes.'}]},
  {'npc': 'I don’t eat pork. Do you have chicken?', 'pt': 'Não como porco. Tem de frango?', 'opts': [
   {'en': 'Yes, I eat pork.', 'pt': 'Sim, eu como porco.', 'ok': False, 'fb': 'Ela perguntou se há frango.'},
   {'en': 'Yes! Chicken and mushroom.', 'pt': 'Tem! Frango e cogumelo.', 'ok': True, 'fb': 'Oferece a opção sem porco.'},
   {'en': 'No, thank you.', 'pt': 'Não, obrigada.', 'ok': False, 'fb': 'Perde a venda e não responde à pergunta; o frango existe.'}]},
  {'npc': 'Perfect. How much?', 'pt': 'Perfeito. Quanto custa?', 'opts': [
   {'en': 'Very much, thank you.', 'pt': 'Muito, obrigada.', 'ok': False, 'fb': 'How much? pede o preço aqui.'},
   {'en': 'Six for eight dollars.', 'pt': 'Seis por oito dólares.', 'ok': True, 'fb': 'Dá quantidade e preço.'},
   {'en': 'Try one, please.', 'pt': 'Experimente um, por favor.', 'ok': False, 'fb': 'Ela já provou; agora quer o preço.'}]},
  {'npc': 'Enjoy the dumplings!', 'pt': 'Aproveite os bolinhos!', 'opts': [
   {'en': 'Hi! They smell good.', 'pt': 'Oi! Estão com cheiro bom.', 'ok': False, 'fb': 'Isso é uma saudação do começo da conversa.'},
   {'en': 'Thanks! See you next time.', 'pt': 'Obrigada! Até a próxima.', 'ok': True, 'fb': 'Despedida simpática da vendedora.'},
   {'en': 'What’s in it?', 'pt': 'O que tem dentro?', 'ok': False, 'fb': 'Pergunta já respondida; agora é a despedida.'}]}]},
)
