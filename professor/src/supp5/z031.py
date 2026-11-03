"""Bloco de verbos e expressões da aula 31: pedir café com tamanho e leite."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('prepare', '👩\u200d🍳', 'preparar', ('prepare', 'I prepare my coffee at home.', 'Eu preparo meu café em casa.'), ('prepares', 'Mei prepares the drinks.', 'A Mei prepara as bebidas.'), ('prepared', 'She prepared a latte.', 'Ela preparou um latte.'), ('preparing', 'Mei is preparing my order.', 'A Mei está preparando meu pedido.'), 'Prepare vale para bebida e comida: passado regular, prepared.'),
  vb('pour', '🫗', 'servir / despejar', ('pour', 'I pour milk in my coffee.', 'Eu coloco leite no meu café.'), ('pours', 'Sam pours oat milk.', 'O Sam coloca leite de aveia.'), ('poured', 'She poured the syrup.', 'Ela despejou a calda.'), ('pouring', 'I am pouring cream now.', 'Estou colocando creme agora.'), 'Pour é despejar líquido: milk, cream, syrup.'),
  vb('sprinkle', '🍫', 'polvilhar', ('sprinkle', 'I sprinkle cinnamon on top.', 'Eu polvilho canela por cima.'), ('sprinkles', 'He sprinkles chocolate.', 'Ele polvilha chocolate.'), ('sprinkled', 'She sprinkled sugar.', 'Ela polvilhou açúcar.'), ('sprinkling', 'I am sprinkling cocoa.', 'Estou polvilhando cacau.'), 'Sprinkle … on top: polvilhar algo por cima (canela, cacau).'),
  vb('sip', '🥤', 'tomar em goles', ('sip', 'I sip my iced coffee.', 'Eu tomo meu café gelado aos poucos.'), ('sips', 'Eva sips her latte.', 'A Eva toma o latte em golinhos.'), ('sipped', 'He sipped his tea.', 'Ele tomou o chá em golinhos.'), ('sipping', 'I am sipping a cappuccino.', 'Estou tomando um cappuccino aos golinhos.'), 'Sip dobra o p no passado e no -ing: sipped, sipping.'),
  vb('stir', '🥄', 'mexer', ('stir', 'I stir my coffee.', 'Eu mexo meu café.'), ('stirs', 'He stirs in the sugar.', 'Ele mexe o açúcar.'), ('stirred', 'She stirred her latte.', 'Ela mexeu o latte.'), ('stirring', 'I am stirring my tea.', 'Estou mexendo meu chá.'), 'Stir dobra o r: stirred, stirring.')],
 verb_game=[
  dict(scene='O Sam toma o café aos poucos.', en='Sam ___ his coffee slowly.', opts=['sip', 'sips', 'sipped'], ans=1, pt='O Sam toma o café devagar, em golinhos.', why='Com “Sam” (ele) o presente leva -s: sips.'),
  dict(scene='Você polvilha canela no café.', en='I ___ cinnamon on my latte.', opts=['sprinkle', 'sprinkles', 'sprinkled'], ans=0, pt='Eu polvilho canela no meu latte.', why='Com “I” no presente: sprinkle.'),
  dict(scene='Ontem ele colocou leite de aveia.', en='He ___ oat milk yesterday.', opts=['pour', 'poured', 'pouring'], ans=1, pt='Ele colocou leite de aveia ontem.', why='“Yesterday” pede passado: poured.'),
  dict(scene='Agora você mexe o café.', en='I am ___ my coffee.', opts=['stir', 'stirred', 'stirring'], ans=2, pt='Estou mexendo meu café.', why='“am” + -ing: stirring (o r dobra).')],
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
