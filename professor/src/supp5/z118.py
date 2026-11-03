"""Bloco de verbos e expressões da aula 118: achados e perdidos."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('lose', '😟', 'perder', ('lose', 'I lose my keys a lot.', 'Eu perco minhas chaves muito.'), ('loses', 'He loses his hat.', 'Ele perde o boné.'), ('lost', 'I lost my wallet.', 'Eu perdi minha carteira.'), ('losing', 'I am losing my patience.', 'Estou perdendo a paciência.'), 'Lose é irregular: lose, lost. Cuidado: loose é “solto”.'),
  vb('find', '🔍', 'achar, encontrar', ('find', 'We find the bag.', 'Nós achamos a mochila.'), ('finds', 'She finds a hat.', 'Ela acha um chapéu.'), ('found', 'He found his glasses.', 'Ele achou os óculos.'), ('finding', 'I am finding my things.', 'Estou achando minhas coisas.'), 'Find é irregular: find, found. O sinal diz Lost and found.'),
  vb('describe', '📝', 'descrever', ('describe', 'I describe my bag.', 'Eu descrevo minha mochila.'), ('describes', 'She describes the color.', 'Ela descreve a cor.'), ('described', 'He described his wallet.', 'Ele descreveu a carteira.'), ('describing', 'I am describing it now.', 'Estou descrevendo agora.'), 'Describe + o objeto, sem to: describe the bag.'),
  vb('leave', '🚪', 'deixar, sair', ('leave', 'We leave at five.', 'Nós saímos às cinco.'), ('leaves', 'Ana leaves her bag on the bus.', 'A Ana deixa a mochila no ônibus.'), ('left', 'I left my hat here.', 'Eu deixei meu boné aqui.'), ('leaving', 'I am leaving now.', 'Estou saindo agora.'), 'Leave serve para deixar algo e para sair. Passado: left.'),
  vb('drop', '⬇️', 'deixar cair', ('drop', 'Kids drop things.', 'Crianças deixam coisas caírem.'), ('drops', 'He drops his keys.', 'Ele deixa as chaves caírem.'), ('dropped', 'I dropped my phone.', 'Eu deixei o celular cair.'), ('dropping', 'I am dropping the bag.', 'Estou deixando a mochila cair.'), 'No passado e no -ing, o p dobra: dropped, dropping.')],
 verb_game=[
  dict(scene='Ontem você perdeu a carteira.', en='Yesterday I ___ my wallet.', opts=['lose', 'lost', 'losing'], ans=1, pt='Ontem eu perdi minha carteira.', why='“Yesterday” pede passado: lost.'),
  dict(scene='A funcionária acha uma mochila preta.', en='The woman ___ a black backpack.', opts=['find', 'finds', 'found'], ans=1, pt='A mulher acha uma mochila preta.', why='Com “the woman” (ela), o presente leva -s: finds.'),
  dict(scene='Agora você descreve a mochila.', en='I am ___ my backpack.', opts=['describe', 'describes', 'describing'], ans=2, pt='Estou descrevendo minha mochila.', why='“am” + verbo termina em -ing: describing.'),
  dict(scene='Vocês saem do ônibus.', en='We ___ the bus at the station.', opts=['leave', 'leaves', 'left'], ans=0, pt='Nós saímos do ônibus na estação.', why='Com “we”, o presente fica na forma base: leave.')],
 expressions=[
  dict(en='I lost my…', pt='Perdi meu/minha…', ex='Excuse me, I lost my backpack.', exp='Para dizer o que perdeu.', c='a'),
  dict(en='It’s … with …', pt='É … com …', ex='It’s black with a red zipper.', exp='Para descrever cor e detalhe.', c='b'),
  dict(en='Maybe on the bus.', pt='Talvez no ônibus.', ex='Maybe on the bus, or at school.', exp='Quando você não tem certeza do lugar.', c='c'),
  dict(en='Is this it?', pt='É esta?', ex='Let me check. Is this it?', exp='Para confirmar se acharam o item.', c='d'),
  dict(en='That’s mine.', pt='É minha / meu.', ex='Yes! That’s mine.', exp='Para dizer que o objeto é seu.', c='a'),
  dict(en='It happens.', pt='Acontece.', ex='Don’t worry. It happens.', exp='Para consolar alguém depois de uma perda pequena.', c='b')],
 expr_game=[
  dict(cue='Você viu sua mochila entre os objetos.', opts=['Maybe on the bus.', 'That’s mine.', 'It happens.'], ans=1, why='That’s mine diz que o objeto é seu.'),
  dict(cue='Você não sabe onde perdeu o objeto.', opts=['Is this it?', 'I lost my wallet.', 'Maybe on the bus.'], ans=2, why='Maybe indica que você não tem certeza.'),
  dict(cue='Um amigo perdeu as chaves e está triste.', opts=['It happens.', 'That’s mine.', 'It’s black with a red zipper.'], ans=0, why='It happens consola a pessoa.')])
