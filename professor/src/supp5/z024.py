"""Bloco de verbos e expressões da aula 24: montar um sanduíche."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('melt', '🧀', 'derreter', ('melt', 'I melt cheese on my sandwich.', 'Eu derreto queijo no meu sanduíche.'), ('melts', 'Sam melts the cheese.', 'O Sam derrete o queijo.'), ('melted', 'He melted butter on the bread.', 'Ele derreteu manteiga no pão.'), ('melting', 'He is melting the cheese now.', 'Ele está derretendo o queijo agora.'), 'Melt serve para queijo e manteiga; o passado só acrescenta -ed.'),
  vb('choose', '🍞', 'escolher', ('choose', 'I choose wheat bread.', 'Eu escolho pão integral.'), ('chooses', 'Eva chooses a roll.', 'A Eva escolhe um pãozinho.'), ('chose', 'He chose white bread.', 'Ele escolheu pão branco.'), ('choosing', 'I am choosing a drink.', 'Estou escolhendo uma bebida.'), 'Irregular: choose vira chose.'),
  vb('add', '🥬', 'adicionar', ('add', 'I add lettuce and tomato.', 'Eu coloco alface e tomate.'), ('adds', 'He adds mustard.', 'Ele coloca mostarda.'), ('added', 'She added cheese.', 'Ela colocou queijo.'), ('adding', 'I am adding onions.', 'Estou colocando cebola.'), 'Add serve para pôr ingredientes no sanduíche.'),
  vb('make', '👩‍🍳', 'fazer', ('make', 'They make sandwiches fast.', 'Eles fazem sanduíches rápido.'), ('makes', 'Sam makes my sandwich.', 'O Sam faz meu sanduíche.'), ('made', 'She made a turkey sandwich.', 'Ela fez um sanduíche de peru.'), ('making', 'He is making lunch.', 'Ele está fazendo o almoço.'), 'Irregular: make vira made.'),
  vb('heat', '🔥', 'esquentar', ('heat', 'I heat my sandwich for a minute.', 'Eu esquento meu sanduíche por um minuto.'), ('heats', 'Sam heats the bread.', 'O Sam esquenta o pão.'), ('heated', 'He heated the soup.', 'Ele esquentou a sopa.'), ('heating', 'They are heating my sandwich.', 'Estão esquentando meu sanduíche.'), 'Can you heat it up? pede para esquentar a comida.')],
 verb_game=[
  dict(scene='O Sam derrete o queijo no sanduíche.', en='Sam ___ the cheese on my sandwich.', opts=['melt', 'melts', 'melted'], ans=1, pt='O Sam derrete o queijo no meu sanduíche.', why='Com “Sam” (ele) o presente leva -s: melts.'),
  dict(scene='Ontem a Eva escolheu pão branco.', en='Eva ___ white bread yesterday.', opts=['chooses', 'chose', 'choosing'], ans=1, pt='A Eva escolheu pão branco ontem.', why='Passado irregular de choose: chose.'),
  dict(scene='O Sam monta seu sanduíche agora.', en='Sam is ___ my sandwich.', opts=['make', 'makes', 'making'], ans=2, pt='O Sam está fazendo meu sanduíche.', why='“is” + -ing: making.'),
  dict(scene='O Ben sempre coloca mostarda.', en='Ben ___ mustard to his sandwich.', opts=['add', 'adds', 'added'], ans=1, pt='O Ben coloca mostarda no sanduíche dele.', why='Com “Ben” (ele) no presente: adds.')],
 expressions=[
  dict(en='What can I get you?', pt='O que posso te servir?', ex='Hi! What can I get you today?', exp='O que o atendente diz ao receber o pedido.', c='a'),
  dict(en='Can I have…?', pt='Posso pedir…?', ex='Can I have a turkey sandwich?', exp='Para pedir algo.', c='b'),
  dict(en='White or wheat?', pt='Branco ou integral?', ex='White or wheat bread?', exp='Pergunta sobre o tipo de pão.', c='c'),
  dict(en='No onions, please.', pt='Sem cebola, por favor.', ex='Lettuce and tomato, no onions, please.', exp='Para tirar um ingrediente.', c='d'),
  dict(en='Yes, all of them.', pt='Sim, todos.', ex='Lettuce, tomato? — Yes, all of them.', exp='Quando você quer todos os ingredientes.', c='a'),
  dict(en='a salad or soup', pt='uma salada ou uma sopa', ex='Would you like a salad or soup?', exp='Opção de acompanhamento do combo.', c='b')],
 expr_game=[
  dict(cue='Você quer pão integral.', opts=['Wheat, please.', 'All of them.', 'Hi! What can I get you?'], ans=0, why='Wheat, please escolhe o pão.'),
  dict(cue='Você não quer cebola.', opts=['Yes, all of them.', 'No onions, please.', 'Can I have a roll?'], ans=1, why='No… , please tira um ingrediente.'),
  dict(cue='Você quer pedir um sanduíche de peru.', opts=['White or wheat?', 'Can I have a turkey sandwich?', 'Enjoy your lunch!'], ans=1, why='Can I have…? faz o pedido.')])
