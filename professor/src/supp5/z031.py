"""Bloco de verbos e expressões da aula 31: pedir café com tamanho e leite."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('make', '☕', 'fazer / preparar', ('make', 'I make coffee at home.', 'Eu faço café em casa.'), ('makes', 'Sam makes a latte.', 'O Sam faz um latte.'), ('made', 'She made my tea.', 'Ela fez meu chá.'), ('making', 'He is making a mocha.', 'Ele está fazendo um mocha.'), 'Passado irregular: make vira made.'),
  vb('pour', '🫗', 'servir / despejar', ('pour', 'I pour milk in my coffee.', 'Eu coloco leite no meu café.'), ('pours', 'Sam pours oat milk.', 'O Sam coloca leite de aveia.'), ('poured', 'She poured the syrup.', 'Ela despejou a calda.'), ('pouring', 'I am pouring cream now.', 'Estou colocando creme agora.'), 'Pour é despejar líquido: milk, cream, syrup.'),
  vb('add', '🍫', 'adicionar / pôr', ('add', 'I add cinnamon to my latte.', 'Eu ponho canela no meu latte.'), ('adds', 'She adds sugar to her tea.', 'Ela põe açúcar no chá.'), ('added', 'He added ice to my cup.', 'Ele pôs gelo no meu copo.'), ('adding', 'I am adding milk to my coffee.', 'Estou pondo leite no meu café.'), 'Add to = pôr em algo. Passado só com -ed.'),
  vb('drink', '🥤', 'beber / tomar', ('drink', 'I drink coffee in the morning.', 'Eu tomo café de manhã.'), ('drinks', 'Sam drinks tea.', 'O Sam toma chá.'), ('drank', 'She drank her latte.', 'Ela tomou o latte dela.'), ('drinking', 'I am drinking iced coffee.', 'Estou tomando café gelado.'), 'Passado irregular: drink vira drank.'),
  vb('mix', '🥄', 'misturar / mexer', ('mix', 'I mix sugar in my coffee.', 'Eu mexo açúcar no meu café.'), ('mixes', 'Sam mixes the mocha.', 'O Sam mistura o mocha.'), ('mixed', 'She mixed her tea.', 'Ela mexeu o chá dela.'), ('mixing', 'I am mixing my coffee.', 'Estou mexendo meu café.'), 'Mix vira mixes na forma ele/ela.')],
 verb_game=[
  dict(scene='O Sam toma café de manhã.', en='Sam ___ coffee in the morning.', opts=['drink', 'drinks', 'drank'], ans=1, pt='O Sam toma café de manhã.', why='Com “Sam” (ele) o presente leva -s: drinks.'),
  dict(scene='Você põe canela no café.', en='I ___ cinnamon to my latte.', opts=['add', 'adds', 'added'], ans=0, pt='Eu ponho canela no meu latte.', why='Com “I” no presente: add.'),
  dict(scene='Ontem ele colocou leite de aveia.', en='He ___ oat milk yesterday.', opts=['pour', 'poured', 'pouring'], ans=1, pt='Ele colocou leite de aveia ontem.', why='“Yesterday” pede passado: poured.'),
  dict(scene='Agora você mexe o café.', en='I am ___ my coffee.', opts=['mix', 'mixed', 'mixing'], ans=2, pt='Estou mexendo meu café.', why='“am” + -ing: mixing.')],
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
