"""Bloco de verbos e expressões da aula 034: perguntar onde fica no mercado."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('find', '🔎', 'encontrar', ('find', 'I find the milk in aisle three.', 'Eu encontro o leite no corredor três.'), ('finds', 'She finds the rice.', 'Ela encontra o arroz.'), ('found', 'He found the pasta.', 'Ele encontrou o macarrão.'), ('finding', 'I am finding everything.', 'Estou encontrando tudo.'), 'Irregular: find vira found.'),
  vb('look', '👀', 'procurar / olhar', ('look', 'I look for the juice.', 'Eu procuro o suco.'), ('looks', 'She looks on the shelf.', 'Ela olha na prateleira.'), ('looked', 'We looked in aisle four.', 'Nós procuramos no corredor quatro.'), ('looking', 'I am looking for the rice.', 'Estou procurando o arroz.'), 'Look for = procurar. I’m looking for… é a frase mais útil.'),
  vb('push', '🛒', 'empurrar', ('push', 'I push the cart.', 'Eu empurro o carrinho.'), ('pushes', 'She pushes the cart to aisle five.', 'Ela empurra o carrinho até o corredor cinco.'), ('pushed', 'He pushed the cart.', 'Ele empurrou o carrinho.'), ('pushing', 'I am pushing the cart.', 'Estou empurrando o carrinho.'), 'Push + the cart. Com he/she/it: pushes (-es).'),
  vb('reach', '🙌', 'alcançar', ('reach', 'I reach the top shelf.', 'Eu alcanço a prateleira de cima.'), ('reaches', 'She reaches the cereal.', 'Ela alcança o cereal.'), ('reached', 'We reached aisle three.', 'Nós chegamos ao corredor três.'), ('reaching', 'I am reaching for the rice.', 'Estou esticando o braço para pegar o arroz.'), 'Reach: alcançar algo ou chegar a um lugar. Reaches leva -es.'),
  vb('scan', '📱', 'escanear', ('scan', 'I scan the barcode.', 'Eu escaneio o código de barras.'), ('scans', 'He scans the milk.', 'Ele escaneia o leite.'), ('scanned', 'She scanned the rice.', 'Ela escaneou o arroz.'), ('scanning', 'I am scanning my items.', 'Estou escaneando meus itens.'), 'Scan dobra o n: scanned, scanning.')],
 verb_game=[
  dict(scene='Você empurra o carrinho agora.', en='I am ___ the cart.', opts=['push', 'pushes', 'pushing'], ans=2, pt='Estou empurrando o carrinho.', why='“am” + -ing: pushing.'),
  dict(scene='Ontem você chegou ao corredor três.', en='Yesterday I ___ aisle three.', opts=['reach', 'reached', 'reaches'], ans=1, pt='Ontem eu cheguei ao corredor três.', why='“Yesterday” pede passado: reached.'),
  dict(scene='A Ana encontra o leite.', en='Ana ___ the milk on the shelf.', opts=['find', 'found', 'finds'], ans=2, pt='A Ana encontra o leite na prateleira.', why='Presente com “Ana” leva -s: finds.'),
  dict(scene='Vocês escaneiam o código no fim.', en='We ___ the barcode at the end.', opts=['scan', 'scans', 'scanning'], ans=0, pt='Nós escaneamos o código no final.', why='Com “we” o presente fica na forma base: scan.')],
 expressions=[
  dict(en='Excuse me, where is…?', pt='Com licença, onde fica…?', ex='Excuse me, where is the milk?', exp='Para chamar atenção e perguntar a localização.', c='a'),
  dict(en='in aisle three', pt='no corredor três', ex='It’s in aisle three.', exp='Para dizer em que corredor algo está.', c='b'),
  dict(en='next to', pt='ao lado de', ex='The juice is next to the milk.', exp='Para indicar proximidade.', c='c'),
  dict(en='on the left', pt='à esquerda', ex='The rice is on the left.', exp='Para indicar o lado.', c='d'),
  dict(en='I’m looking for…', pt='Estou procurando…', ex='I’m looking for pasta.', exp='Para dizer o que você procura.', c='a'),
  dict(en='You’re welcome.', pt='De nada.', ex='Thanks! — You’re welcome.', exp='Resposta educada a um agradecimento.', c='b')],
 expr_game=[
  dict(cue='Você quer saber onde fica o queijo.', opts=['Excuse me, where is the cheese?', 'It’s on the left.', 'You’re welcome.'], ans=0, why='Where is…? pergunta o local.'),
  dict(cue='Você quer dizer que o suco fica ao lado do leite.', opts=['I’m looking for juice.', 'It’s next to the milk.', 'In aisle three?'], ans=1, why='Next to = ao lado de.'),
  dict(cue='Alguém agradece e você responde.', opts=['You’re welcome.', 'Excuse me.', 'On the right.'], ans=0, why='You’re welcome = de nada.')])
