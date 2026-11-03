X = dict(
 key={'big': 'Two slices, please', 'label': 'Pedir pizza por fatia', 'sub': 'Em pizzarias dos EUA, muita gente pede por fatia (slice); você diz quantas, o sabor, a bebida e o tamanho.'},
 mini=[
  {'who': 'Ravi', 'en': 'Hi! What can I get you {today|tonight|now}?', 'pt': 'Oi! O que vai ser {hoje|hoje à noite|agora}?'},
  {'who': 'You', 'en': '{Two|One|Three} slices of {pepperoni|cheese|mushroom}, please.', 'pt': '{Duas|Uma|Três} fatias de {pepperoni|queijo|cogumelo}, por favor.'},
  {'who': 'Ravi', 'en': 'Anything to drink? {Soda|Water|Juice}?', 'pt': 'Algo para beber? {Refrigerante|Água|Suco}?'},
  {'who': 'You', 'en': 'A {soda|water|juice}, please. {Large|Small|Medium}.', 'pt': '{Um refrigerante|Uma água|Um suco}, por favor. Tamanho {grande|pequeno|médio}.'}],
 dlg=[
  {'who': 'Ravi', 'en': 'Hi! What can I get you?', 'pt': 'Oi! O que vai ser?'},
  {'who': 'You', 'en': '{Two|One|Three} slices of {pepperoni|cheese|mushroom}, please.', 'pt': '{Duas|Uma|Três} fatias de {pepperoni|queijo|cogumelo}, por favor.'},
  {'who': 'Ravi', 'en': 'Anything to drink?', 'pt': 'Algo para beber?'},
  {'who': 'You', 'en': 'A {soda|water|juice}, please.', 'pt': '{Um refrigerante|Uma água|Um suco}, por favor.'},
  {'who': 'Ravi', 'en': 'Small or {large|medium|extra large}?', 'pt': 'Pequeno ou {grande|médio|extra grande}?'},
  {'who': 'You', 'en': '{Large|Small|Medium}. How much is it?', 'pt': '{Grande|Pequeno|Médio}. Quanto custa?'},
  {'who': 'Ravi', 'en': 'That’s {eight|nine|ten} dollars.', 'pt': 'São {oito|nove|dez} dólares.'},
  {'who': 'You', 'en': 'Here you go. Thanks!', 'pt': 'Aqui está. Valeu!'},
  {'who': 'Ravi', 'en': 'Enjoy your {pizza|slices|soda}!', 'pt': 'Aproveite {sua pizza|suas fatias|seu refrigerante}!'}],
 vocab=[
  {'w': 'slice', 'pt': 'fatia', 'e': '🍕', 'ex': ['One slice, please.', 'This slice is hot.']},
  {'w': 'pepperoni', 'pt': 'pepperoni', 'e': '🍕', 'ex': ['Two slices of pepperoni, please.', 'I like pepperoni.']},
  {'w': 'soda', 'pt': 'refrigerante', 'e': '🥤', 'ex': ['A large soda, please.', 'The soda is cold.']},
  {'w': 'water', 'pt': 'água', 'e': '💧', 'ex': ['Can I have water?', 'A small water, please.']},
  {'w': 'dollar', 'pt': 'dólar', 'e': '💵', 'ex': ['It is eight dollars.', 'One dollar, please.']},
  {'w': 'large', 'pt': 'grande', 'e': '📏', 'ex': ['A large soda, please.', 'The large is better.']}],
 molds=[
  {'title': 'Pedir fatias', 'frame': '{number} slices of {kind}, please.', 'slots': [{'key': 'number', 'opts': ['Two', 'Three', 'Four']}, {'key': 'kind', 'opts': ['pepperoni', 'cheese', 'mushroom']}], 'model': 'Two slices of pepperoni, please.', 'note': 'Com mais de uma fatia, use slices no plural. Para uma só: One slice of cheese, please.'},
  {'title': 'Escolher bebida e tamanho', 'frame': 'A {size} {drink}, please.', 'slots': [{'key': 'size', 'opts': ['large', 'small', 'medium']}, {'key': 'drink', 'opts': ['soda', 'water', 'juice']}], 'model': 'A large soda, please.', 'note': 'Em inglês, o tamanho vem antes da bebida.'},
  {'title': 'Perguntar e pagar (escrever)', 'frame': 'How much is it? {amount} dollars? Here you go.', 'slots': [{'key': 'amount', 'opts': ['Eight', 'Nine', 'Ten']}], 'model': 'How much is it? Eight dollars? Here you go.', 'note': 'Repetir o preço confirma que você entendeu.'}],
 sounds=[
  {'say': 'Two slices of pepperoni, please.', 'tag': 'ritmo: palavras fortes', 'tip': 'Acentue two, slices, pepperoni e please; of fica fraco: “uv”.'},
  {'say': 'That’s eight dollars.', 'tag': 'ligação: that’s eight', 'tip': 'That’s e eight se juntam: “thats-eight”, sem pausa.'},
  {'say': 'Small or large?', 'tag': 'entonação: escolha', 'tip': 'Suba em small e desça em large, como numa pergunta de escolha.'}],
 role={'turns': [
  {'npc': 'Hi! What can I get you?', 'opts': [
   {'en': 'Two slices of pepperoni, please.', 'pt': 'Duas fatias de pepperoni, por favor.', 'reply': 'Two pepperoni. Anything to drink?'},
   {'en': 'One slice of cheese, please.', 'pt': 'Uma fatia de queijo, por favor.', 'reply': 'One cheese. Anything to drink?'},
   {'en': 'Three slices of mushroom, please.', 'pt': 'Três fatias de cogumelo, por favor.', 'reply': 'Three mushroom. Anything to drink?'}]},
  {'npc': 'Anything to drink?', 'opts': [
   {'en': 'A soda, please.', 'pt': 'Um refrigerante, por favor.', 'reply': 'A soda. Small or large?'},
   {'en': 'A water, please.', 'pt': 'Uma água, por favor.', 'reply': 'A water. Small or large?'},
   {'en': 'An orange juice, please.', 'pt': 'Um suco de laranja, por favor.', 'reply': 'Orange juice. Small or large?'}]},
  {'npc': 'Small or large?', 'opts': [
   {'en': 'Large. How much is it?', 'pt': 'Grande. Quanto custa?', 'reply': 'That’s eight dollars.'},
   {'en': 'Small, please. How much is it?', 'pt': 'Pequeno, por favor. Quanto custa?', 'reply': 'That’s six dollars.'},
   {'en': 'Large, please. How much?', 'pt': 'Grande, por favor. Quanto?', 'reply': 'That’s eight dollars.'}]},
  {'npc': 'That’s eight dollars.', 'opts': [
   {'en': 'Here you go. Thanks!', 'pt': 'Aqui está. Valeu!', 'reply': 'Thank you! Enjoy your pizza!'},
   {'en': 'Here’s ten dollars.', 'pt': 'Aqui estão dez dólares.', 'reply': 'Thanks! Here’s your change. Enjoy your pizza!'},
   {'en': 'OK. Here you go, thank you.', 'pt': 'Certo. Aqui está, obrigado.', 'reply': 'Thank you! Enjoy your pizza!'}]}],
  'change': ['Você quer a pizza para levar: diga to go.', 'O preço é maior do que você pensava: pergunte de novo, How much is it?', 'Você está com um amigo: peça fatias para dois.']},
 writing={'task': 'Escreva uma mensagem para pedir pizza por fatia: quantidade, sabor, bebida e tamanho.',
  'model': 'Hi! Two slices of cheese, please. A large soda, please. How much is it? Thank you!',
  'kw': ['slices', 'please', 'soda', 'large'],
  'checks': ['Pedi a quantidade e o sabor.', 'Pedi bebida e tamanho.', 'Perguntei o preço.']},
 scenes={'pool': ['restaurant', 'diner', 'street', 'cafe2', 'market'], 'npc': {'g': 'm', 'role': 'cook'}, 'you': {'g': 'f'}},
 convo={'npc': {'name': 'Ravi'}, 'story': 'Você está numa pizzaria e quer comer por fatia. Peça com Ravi.', 'turns': [
  {'npc': 'Hi! What can I get you?', 'pt': 'Oi! O que vai ser?', 'opts': [
   {'en': 'It’s eight dollars.', 'pt': 'São oito dólares.', 'ok': False, 'fb': 'Quem diz o preço é o atendente, depois do pedido.'},
   {'en': 'Two slices of pepperoni, please.', 'pt': 'Duas fatias de pepperoni, por favor.', 'ok': True, 'fb': 'Pedido claro com quantidade e sabor.'},
   {'en': 'Hi! Nice to meet you.', 'pt': 'Oi! Prazer em conhecer.', 'ok': False, 'fb': 'Educado, mas Ravi quer saber o pedido.'}]},
  {'npc': 'Anything to drink?', 'pt': 'Algo para beber?', 'opts': [
   {'en': 'A soda, please.', 'pt': 'Um refrigerante, por favor.', 'ok': True, 'fb': 'Resposta direta.'},
   {'en': 'Two slices, please.', 'pt': 'Duas fatias, por favor.', 'ok': False, 'fb': 'As fatias já foram pedidas; ele pergunta sobre a bebida.'},
   {'en': 'Yes, I’m thirsty.', 'pt': 'Sim, estou com sede.', 'ok': False, 'fb': 'É verdade, mas não diz qual bebida.'}]},
  {'npc': 'Small or large?', 'pt': 'Pequeno ou grande?', 'opts': [
   {'en': 'Yes, thanks.', 'pt': 'Sim, obrigado.', 'ok': False, 'fb': 'É pergunta de escolha: small ou large.'},
   {'en': 'Pepperoni, please.', 'pt': 'Pepperoni, por favor.', 'ok': False, 'fb': 'Sobre o sabor já se falou; agora o tamanho.'},
   {'en': 'Large. How much is it?', 'pt': 'Grande. Quanto custa?', 'ok': True, 'fb': 'Escolhe e já pergunta o preço.'}]},
  {'npc': 'That’s eight dollars.', 'pt': 'São oito dólares.', 'opts': [
   {'en': 'Here you go. Thanks!', 'pt': 'Aqui está. Valeu!', 'ok': True, 'fb': 'Paga e agradece.'},
   {'en': 'Eight dollars is a number.', 'pt': 'Oito dólares é um número.', 'ok': False, 'fb': 'Não responde ao que ele pede: o pagamento.'},
   {'en': 'What can I get you?', 'pt': 'O que posso servir?', 'ok': False, 'fb': 'Essa pergunta é do atendente.'}]},
  {'npc': 'Enjoy your pizza!', 'pt': 'Bom apetite!', 'opts': [
   {'en': 'Small or large?', 'pt': 'Pequeno ou grande?', 'ok': False, 'fb': 'O tamanho já foi escolhido.'},
   {'en': 'Anything to drink?', 'pt': 'Algo para beber?', 'ok': False, 'fb': 'Essa é a pergunta dele, e você já pediu bebida.'},
   {'en': 'Thanks! You too.', 'pt': 'Obrigado! Você também.', 'ok': True, 'fb': 'Resposta cordial.'}]}]},
)
