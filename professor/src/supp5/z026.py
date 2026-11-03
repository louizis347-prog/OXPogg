"""Bloco de verbos e expressões da aula 26: barraca de bolinhos no mercado."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('try', '🥟', 'provar / experimentar', ('try', 'I try one dumpling.', 'Eu provo um bolinho.'), ('tries', 'Mia tries the pork.', 'A Mia prova o de porco.'), ('tried', 'We tried the chicken.', 'Nós provamos o de frango.'), ('trying', 'I am trying a taco.', 'Estou provando um taco.'), 'Try one! é um convite comum. try vira tries / tried.'),
  vb('smell', '👃', 'cheirar', ('smell', 'These tacos smell good.', 'Estes tacos cheiram bem.'), ('smells', 'It smells great.', 'Cheira muito bem.'), ('smelled', 'The pies smelled good.', 'As tortas cheiravam bem.'), ('smelling', 'I am smelling the ginger.', 'Estou sentindo o cheiro do gengibre.'), 'smell + adjetivo: smells good.'),
  vb('munch', '🍽️', 'mastigar / petiscar', ('munch', 'I munch on chips.', 'Eu petisco batata frita.'), ('munches', 'Ana munches on a taco.', 'A Ana petisca um taco.'), ('munched', 'We munched on dumplings.', 'Nós petiscamos bolinhos.'), ('munching', 'I am munching on a taco.', 'Estou petiscando um taco.'), 'Munch on = comer aos poucos, de forma descontraída.'),
  vb('taste', '😋', 'ter gosto / provar', ('taste', 'They taste fresh.', 'Eles têm gosto de frescos.'), ('tastes', 'This one tastes good.', 'Este tem um gosto bom.'), ('tasted', 'It tasted great.', 'Estava ótimo.'), ('tasting', 'I am tasting the beef.', 'Estou provando a carne.'), 'taste + adjetivo: tastes good.'),
  vb('load', '🌮', 'encher / carregar', ('load', 'I load my taco with salsa.', 'Eu encho meu taco de molho.'), ('loads', 'The cook loads each taco.', 'O cozinheiro enche cada taco.'), ('loaded', 'He loaded it with onions.', 'Ele encheu com cebola.'), ('loading', 'She is loading my plate.', 'Ela está enchendo meu prato.'), 'Load it with… = colocar bastante cobertura ou recheio.')],
 verb_game=[
  dict(scene='Você petisca batata frita enquanto espera.', en='I ___ on chips while I wait.', opts=['munch', 'munches', 'munched'], ans=0, pt='Eu petisco batata frita enquanto espero.', why='Com “I” o presente usa a forma base: munch.'),
  dict(scene='O taco cheira bem.', en='This taco ___ good.', opts=['smell', 'smells', 'smelling'], ans=1, pt='Este taco cheira bem.', why='“This taco” é ele/ela: smells.'),
  dict(scene='Ontem a Ana encheu o taco de cebola.', en='Ana ___ her taco with onions yesterday.', opts=['loads', 'loaded', 'loading'], ans=1, pt='A Ana encheu o taco de cebola ontem.', why='“Yesterday” pede passado: loaded.'),
  dict(scene='Você está provando um bolinho agora.', en='I am ___ a dumpling.', opts=['try', 'tries', 'trying'], ans=2, pt='Estou provando um bolinho.', why='“am” + -ing: trying.')],
 expressions=[
  dict(en='What’s in it?', pt='O que tem nisso?', ex='What’s in it? — Pork and cabbage.', exp='Para saber os ingredientes.', c='a'),
  dict(en='I don’t eat…', pt='Eu não como…', ex='I don’t eat pork.', exp='Para dizer o que você não come.', c='b'),
  dict(en='Do you have…?', pt='Vocês têm…?', ex='Do you have chicken?', exp='Para pedir outra opção.', c='c'),
  dict(en='Try one!', pt='Experimente um!', ex='Thank you! Try one!', exp='Convite do vendedor para provar.', c='d'),
  dict(en='Six for twelve dollars.', pt='Seis por doze dólares.', ex='Six for twelve dollars, please.', exp='Preço por quantidade.', c='a'),
  dict(en='smells good', pt='cheira bem', ex='These tacos smell good!', exp='Elogiar a comida pelo cheiro.', c='b')],
 expr_game=[
  dict(cue='Você quer saber os ingredientes.', opts=['Try one!', 'What’s in it?', 'Six for twelve dollars.'], ans=1, why='What’s in it? pergunta o recheio.'),
  dict(cue='Você não come camarão.', opts=['I don’t eat shrimp.', 'Try one!', 'It smells good.'], ans=0, why='I don’t eat… avisa uma restrição.'),
  dict(cue='Você quer outra opção, frango.', opts=['What’s in it?', 'Do you have chicken?', 'Six for twelve dollars.'], ans=1, why='Do you have…? pede uma opção.')])
