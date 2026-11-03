"""Bloco de verbos e expressões da aula 2."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('cost', '💲', 'custar', ('cost', 'The mangoes cost two dollars.', 'As mangas custam dois dólares.'), ('costs', 'One apple costs a dollar.', 'Uma maçã custa um dólar.'), ('cost', 'The tomatoes cost three dollars.', 'Os tomates custaram três dólares.'), ('costing', 'The lemons are costing more today.', 'Os limões estão custando mais hoje.'), 'Cost não muda no passado: cost, cost. Com coisa singular, costs.'),
  vb('take', '🛍️', 'levar', ('take', 'I take four apples.', 'Eu levo quatro maçãs.'), ('takes', 'She takes two pounds.', 'Ela leva duas libras.'), ('took', 'He took six mangoes.', 'Ele levou seis mangas.'), ('taking', 'I am taking the bananas.', 'Estou levando as bananas.'), 'I’ll take… é o jeito de decidir o que comprar. Passado: took.'),
  vb('buy', '🛒', 'comprar', ('buy', 'We buy fruit here.', 'Nós compramos frutas aqui.'), ('buys', 'Harper buys onions.', 'A Harper compra cebolas.'), ('bought', 'I bought lemons.', 'Eu comprei limões.'), ('buying', 'I am buying tomatoes.', 'Estou comprando tomates.'), 'Verbo irregular: buy vira bought no passado.'),
  vb('need', '📝', 'precisar', ('need', 'I need two pounds.', 'Eu preciso de duas libras.'), ('needs', 'She needs some onions.', 'Ela precisa de algumas cebolas.'), ('needed', 'We needed more bananas.', 'Nós precisávamos de mais bananas.'), ('needing', 'I am needing nothing else.', 'Não estou precisando de mais nada.'), 'Need + algo: I need apples. Com ele/ela, needs.'),
  vb('ask', '🗣️', 'perguntar', ('ask', 'I ask about the price.', 'Eu pergunto o preço.'), ('asks', 'Harper asks about bananas.', 'A Harper pergunta sobre bananas.'), ('asked', 'He asked, “How much?”', 'Ele perguntou: “Quanto custa?”'), ('asking', 'I am asking about the lemons.', 'Estou perguntando sobre os limões.'), 'Ask about = perguntar sobre algo.')],
 verb_game=[
  dict(scene='Você pergunta quanto custam as mangas.', en='The mangoes ___ two dollars each.', opts=['cost', 'costs', 'taking'], ans=0, pt='As mangas custam dois dólares cada.', why='“Mangoes” é plural: cost, sem -s.'),
  dict(scene='Você decide levar seis maçãs.', en='OK, I’ll ___ six apples.', opts=['took', 'take', 'takes'], ans=1, pt='Certo, vou levar seis maçãs.', why='Depois de “I’ll” o verbo fica na forma base: take.'),
  dict(scene='Ontem a Harper comprou frutas.', en='Yesterday Harper ___ some fruit.', opts=['buys', 'buying', 'bought'], ans=2, pt='Ontem a Harper comprou frutas.', why='“Yesterday” pede passado irregular: bought.'),
  dict(scene='Agora você está levando as bananas.', en='I am ___ two pounds of bananas.', opts=['take', 'taking', 'took'], ans=1, pt='Estou levando duas libras de bananas.', why='“am” + verbo termina em -ing: taking.')],
 expressions=[
  dict(en='How much are…?', pt='Quanto custam…?', ex='How much are the tomatoes?', exp='Para perguntar o preço de coisas no plural.', c='a'),
  dict(en='How much is…?', pt='Quanto custa…?', ex='How much is this melon?', exp='Para perguntar o preço de uma coisa só.', c='b'),
  dict(en='I’ll take…', pt='Vou levar…', ex='I’ll take four, please.', exp='Para decidir o que você compra.', c='c'),
  dict(en='a pound', pt='por libra', ex='Bananas are one dollar a pound.', exp='O preço por peso; “each” é por unidade.', c='d'),
  dict(en='Anything else?', pt='Mais alguma coisa?', ex='Four mangoes. Anything else?', exp='O vendedor pergunta isso depois do pedido.', c='a'),
  dict(en='That’s all.', pt='É só isso.', ex='No, that’s all. Thank you!', exp='Para encerrar a compra.', c='b')],
 expr_game=[
  dict(cue='Você quer saber o preço de um melão.', opts=['How much is this melon?', 'I’ll take four.', 'Anything else?'], ans=0, why='How much is…? pergunta o preço.'),
  dict(cue='Você decidiu comprar seis maçãs.', opts=['How much are they?', 'I’ll take six, please.', 'Do you have lemons?'], ans=1, why='I’ll take… confirma o que você leva.'),
  dict(cue='O vendedor pergunta se você quer mais algo e você não quer.', opts=['Yes, two pounds.', 'No, that’s all. Thank you!', 'It’s a dollar each.'], ans=1, why='That’s all fecha a compra.')])
