"""Bloco de verbos e expressões da aula 30: montar uma tigela (bowl)."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('pick', '🥣', 'escolher', ('pick', 'I pick brown rice.', 'Eu escolho arroz integral.'), ('picks', 'Eva picks black beans.', 'A Eva escolhe feijão-preto.'), ('picked', 'He picked chicken yesterday.', 'Ele escolheu frango ontem.'), ('picking', 'I am picking my toppings.', 'Estou escolhendo meus acompanhamentos.'), 'Pick = escolher de forma informal; o passado só acrescenta -ed.'),
  vb('add', '➕', 'adicionar', ('add', 'I add salsa and cheese.', 'Eu coloco molho e queijo.'), ('adds', 'She adds corn.', 'Ela coloca milho.'), ('added', 'He added lettuce.', 'Ele colocou alface.'), ('adding', 'She is adding beans.', 'Ela está colocando feijão.'), 'Add serve para pôr ingredientes na tigela.'),
  vb('hold', '🙋', 'segurar / tirar', ('hold', 'I hold the onions, please.', 'Sem cebola, por favor.'), ('holds', 'Kai holds the bowl.', 'O Kai segura o bowl.'), ('held', 'She held the sauce.', 'Ela deixou o molho de fora.'), ('holding', 'He is holding my bowl.', 'Ele está segurando meu bowl.'), 'Hold the onions = sem cebola, pedido típico nos EUA. Irregular: hold, held.'),
  vb('say', '💬', 'dizer', ('say', 'I say no to sour cream.', 'Eu digo não ao creme azedo.'), ('says', 'Eva says yes to salsa.', 'A Eva diz sim ao molho.'), ('said', 'He said no thanks.', 'Ele disse não, obrigado.'), ('saying', 'I am saying yes to beans.', 'Estou dizendo sim ao feijão.'), 'Passado irregular: said (pronuncia-se “sed”).'),
  vb('put', '🥄', 'colocar', ('put', 'They put rice in the bowl.', 'Eles colocam arroz na tigela.'), ('puts', 'He puts beans on top.', 'Ele coloca feijão por cima.'), ('put', 'She put corn in my bowl.', 'Ela colocou milho na minha tigela.'), ('putting', 'He is putting salsa on it.', 'Ele está pondo molho nisso.'), 'Irregular: put é igual no passado (put).')],
 verb_game=[
  dict(scene='Você escolhe arroz integral.', en='I ___ brown rice.', opts=['pick', 'picks', 'picked'], ans=0, pt='Eu escolho arroz integral.', why='Com “I” no presente: pick.'),
  dict(scene='A Eva diz sim ao molho.', en='Eva ___ yes to the salsa.', opts=['say', 'says', 'saying'], ans=1, pt='A Eva diz sim ao molho.', why='Com “Eva” (ela) o presente leva -s: says.'),
  dict(scene='O atendente está colocando feijão.', en='He is ___ beans in my bowl.', opts=['put', 'puts', 'putting'], ans=2, pt='Ele está colocando feijão na minha tigela.', why='“is” + -ing; put dobra o t: putting.'),
  dict(scene='Ontem ele colocou alface.', en='He ___ lettuce yesterday.', opts=['add', 'adds', 'added'], ans=2, pt='Ele colocou alface ontem.', why='“Yesterday” pede passado: added.')],
 expressions=[
  dict(en='What kind of bowl?', pt='Que tipo de tigela?', ex='Hi! What kind of bowl?', exp='Pergunta inicial do atendente.', c='a'),
  dict(en='White or brown rice?', pt='Arroz branco ou integral?', ex='White or brown rice? — Brown, please.', exp='Escolha da base.', c='b'),
  dict(en='With beans', pt='Com feijão', ex='Brown rice, with beans.', exp='Pedir um ingrediente a mais.', c='c'),
  dict(en='No guacamole.', pt='Sem guacamole.', ex='Salsa, but no guacamole.', exp='Recusar um ingrediente.', c='d'),
  dict(en='Anything else?', pt='Mais alguma coisa?', ex='Anything else? — No, that’s it.', exp='Pergunta do atendente no fim.', c='a'),
  dict(en='That’s it.', pt='É só isso.', ex='No, that’s it. How much?', exp='Encerrar o pedido.', c='b')],
 expr_game=[
  dict(cue='Você não quer guacamole.', opts=['No guacamole.', 'With beans.', 'That’s it.'], ans=0, why='No… recusa um ingrediente.'),
  dict(cue='Você terminou o pedido.', opts=['What kind of bowl?', 'That’s it.', 'Brown rice.'], ans=1, why='That’s it encerra o pedido.'),
  dict(cue='Você quer feijão na tigela.', opts=['With beans.', 'No cheese.', 'Anything else?'], ans=0, why='With… pede um ingrediente.')])
