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
  vb('ask', '🙋', 'perguntar', ('ask', 'I ask the clerk.', 'Eu pergunto ao atendente.'), ('asks', 'He asks, “Where is the milk?”', 'Ele pergunta: “Onde fica o leite?”'), ('asked', 'She asked about the rice.', 'Ela perguntou sobre o arroz.'), ('asking', 'I am asking for help.', 'Estou pedindo ajuda.'), 'Ask about = perguntar sobre; ask for = pedir.'),
  vb('go', '🚶', 'ir', ('go', 'We go to aisle five.', 'Nós vamos ao corredor cinco.'), ('goes', 'He goes to the left.', 'Ele vai para a esquerda.'), ('went', 'I went to aisle three.', 'Eu fui ao corredor três.'), ('going', 'I am going to the dairy aisle.', 'Estou indo ao corredor de laticínios.'), 'Irregular: go vira went.'),
  vb('turn', '↩️', 'virar', ('turn', 'You turn left here.', 'Você vira à esquerda aqui.'), ('turns', 'She turns right.', 'Ela vira à direita.'), ('turned', 'I turned left.', 'Eu virei à esquerda.'), ('turning', 'I am turning right.', 'Estou virando à direita.'), 'Turn left / turn right para dar direções.')],
 verb_game=[
  dict(scene='Você procura o arroz agora.', en='I am ___ for the rice.', opts=['look', 'looks', 'looking'], ans=2, pt='Estou procurando o arroz.', why='“am” + -ing: looking.'),
  dict(scene='Ontem você foi ao corredor três.', en='Yesterday I ___ to aisle three.', opts=['go', 'went', 'goes'], ans=1, pt='Ontem eu fui ao corredor três.', why='Passado irregular de go: went.'),
  dict(scene='A Ana encontra o leite.', en='Ana ___ the milk on the shelf.', opts=['find', 'found', 'finds'], ans=2, pt='A Ana encontra o leite na prateleira.', why='Presente com “Ana” leva -s: finds.'),
  dict(scene='Vocês viram à direita no fim do corredor.', en='We ___ right at the end.', opts=['turn', 'turns', 'turning'], ans=0, pt='Nós viramos à direita no final.', why='Com “we” o presente fica na forma base: turn.')],
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
