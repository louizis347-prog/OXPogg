"""Bloco de verbos e expressões da aula 31: pedir café com tamanho e leite."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('start', '☕', 'começar', ('start', 'I start with a latte.', 'Eu começo com um latte.'), ('starts', 'Her day starts with coffee.', 'O dia dela começa com café.'), ('started', 'We started early.', 'Nós começamos cedo.'), ('starting', 'I am starting my order.', 'Estou começando meu pedido.'), 'What can I get started for you? é a saudação do barista.'),
  vb('want', '👍', 'querer', ('want', 'I want a medium latte.', 'Eu quero um latte médio.'), ('wants', 'Sam wants oat milk.', 'O Sam quer leite de aveia.'), ('wanted', 'I wanted iced coffee.', 'Eu queria café gelado.'), ('wanting', 'I am wanting a muffin.', 'Estou querendo um muffin.'), 'Para pedir, I’d like… ou Can I get… são mais educados.'),
  vb('add', '🥛', 'adicionar', ('add', 'I add sugar.', 'Eu coloco açúcar.'), ('adds', 'He adds soy milk.', 'Ele coloca leite de soja.'), ('added', 'She added oat milk.', 'Ela colocou leite de aveia.'), ('adding', 'I am adding sugar.', 'Estou colocando açúcar.'), 'Add serve para leite, açúcar, calda.'),
  vb('drink', '🥤', 'beber', ('drink', 'I drink iced coffee.', 'Eu bebo café gelado.'), ('drinks', 'Eva drinks a large latte.', 'A Eva bebe um latte grande.'), ('drank', 'He drank hot tea.', 'Ele bebeu chá quente.'), ('drinking', 'I am drinking a cappuccino.', 'Estou bebendo um cappuccino.'), 'Irregular: drink vira drank.'),
  vb('take', '🛍️', 'levar / tomar', ('take', 'I take my coffee iced.', 'Eu tomo meu café gelado.'), ('takes', 'He takes it with sugar.', 'Ele toma com açúcar.'), ('took', 'She took a medium.', 'Ela pegou um médio.'), ('taking', 'I am taking a muffin too.', 'Estou levando um muffin também.'), 'Irregular: take vira took. “How do you take it?” = como você toma?')],
 verb_game=[
  dict(scene='O Sam sempre pede leite de aveia.', en='Sam ___ oat milk.', opts=['want', 'wants', 'wanted'], ans=1, pt='O Sam quer leite de aveia.', why='Com “Sam” (ele) o presente leva -s: wants.'),
  dict(scene='Você coloca açúcar no café.', en='I ___ sugar to my coffee.', opts=['add', 'adds', 'adding'], ans=0, pt='Eu coloco açúcar no meu café.', why='Com “I” no presente: add.'),
  dict(scene='Ontem ele bebeu chá quente.', en='He ___ hot tea yesterday.', opts=['drink', 'drank', 'drinking'], ans=1, pt='Ele bebeu chá quente ontem.', why='Passado irregular de drink: drank.'),
  dict(scene='Agora você está bebendo cappuccino.', en='I am ___ a cappuccino.', opts=['drink', 'drank', 'drinking'], ans=2, pt='Estou bebendo um cappuccino.', why='“am” + -ing: drinking.')],
 expressions=[
  dict(en='What size?', pt='Que tamanho?', ex='What size? Small, medium or large?', exp='Pergunta do barista.', c='a'),
  dict(en='Medium, please.', pt='Médio, por favor.', ex='Medium, please. With oat milk.', exp='Escolher o tamanho.', c='b'),
  dict(en='Hot or iced?', pt='Quente ou gelado?', ex='Hot or iced? — Iced, please.', exp='Pergunta sobre a temperatura.', c='c'),
  dict(en='With oat milk', pt='Com leite de aveia', ex='A latte with oat milk, please.', exp='Escolher o tipo de leite.', c='d'),
  dict(en='Anything to eat?', pt='Algo para comer?', ex='Anything to eat? — A muffin.', exp='O barista oferece comida.', c='a'),
  dict(en='Have a great day!', pt='Tenha um ótimo dia!', ex='Thanks! Have a great day!', exp='Despedida simpática.', c='b')],
 expr_game=[
  dict(cue='Você quer o café gelado.', opts=['Iced, please.', 'What size?', 'Have a great day!'], ans=0, why='Iced, please responde Hot or iced?.'),
  dict(cue='Você quer leite de soja.', opts=['Medium, please.', 'With soy milk.', 'Anything to eat?'], ans=1, why='With… escolhe o leite.'),
  dict(cue='Você escolhe o tamanho grande.', opts=['Large, please.', 'Hot, please.', 'Have a great day!'], ans=0, why='Large, please responde What size?.')])
