"""Bloco de verbos e expressões da aula 72: lixo e reciclagem."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('throw', '🗑️', 'jogar / jogar fora', ('throw', 'I throw the paper in the bin.', 'Eu jogo o papel na lixeira.'), ('throws', 'Mei throws the bag away.', 'A Mei joga o saco fora.'), ('threw', 'He threw a bottle in the bin.', 'Ele jogou uma garrafa na lixeira.'), ('throwing', 'She is throwing the box away.', 'Ela está jogando a caixa fora.'), 'Passado irregular: throw, threw. Throw away = jogar fora.'),
  vb('sort', '🧺', 'separar', ('sort', 'We sort the trash.', 'Nós separamos o lixo.'), ('sorts', 'Gabe sorts the bottles.', 'O Gabe separa as garrafas.'), ('sorted', 'I sorted the paper.', 'Eu separei o papel.'), ('sorting', 'They are sorting the cans.', 'Eles estão separando as latas.'), 'Sort = separar por tipo: papel, plástico, vidro.'),
  vb('recycle', '♻️', 'reciclar', ('recycle', 'I recycle plastic bottles.', 'Eu reciclo garrafas plásticas.'), ('recycles', 'She recycles cardboard.', 'Ela recicla papelão.'), ('recycled', 'We recycled the paper.', 'Nós reciclamos o papel.'), ('recycling', 'He is recycling a box.', 'Ele está reciclando uma caixa.'), 'Recycling também é substantivo: Recycling is Friday.'),
  vb('empty', '🪣', 'esvaziar', ('empty', 'I empty the small bin.', 'Eu esvazio a lixeira pequena.'), ('empties', 'Mei empties the bag.', 'A Mei esvazia o saco.'), ('emptied', 'We emptied the kitchen bin.', 'Nós esvaziamos a lixeira da cozinha.'), ('emptying', 'He is emptying the bin.', 'Ele está esvaziando a lixeira.'), 'Empty termina em y: empties, emptied.'),
  vb('collect', '🚛', 'recolher', ('collect', 'They collect the trash on Tuesday.', 'Eles recolhem o lixo na terça.'), ('collects', 'The truck collects the bins.', 'O caminhão recolhe as lixeiras.'), ('collected', 'It collected the bags early.', 'Ele recolheu os sacos cedo.'), ('collecting', 'The truck is collecting now.', 'O caminhão está recolhendo agora.'), 'Collect é o verbo da coleta de lixo: When do they collect it?')],
 verb_game=[
  dict(scene='Toda sexta o caminhão recolhe a reciclagem.', en='The truck ___ the recycling on Friday.', opts=['collect', 'collects', 'collecting'], ans=1, pt='O caminhão recolhe a reciclagem na sexta.', why='Com “the truck” (ele) o presente leva -s: collects.'),
  dict(scene='Ontem a Mei jogou uma caixa fora.', en='Yesterday Mei ___ a box away.', opts=['throw', 'throws', 'threw'], ans=2, pt='Ontem a Mei jogou uma caixa fora.', why='“Yesterday” pede passado: threw (irregular).'),
  dict(scene='Agora o Gabe está esvaziando a lixeira.', en='Gabe is ___ the bin.', opts=['empty', 'emptying', 'empties'], ans=1, pt='O Gabe está esvaziando a lixeira.', why='“is” + verbo termina em -ing: emptying.'),
  dict(scene='Nós sempre separamos o lixo em casa.', en='We always ___ the trash at home.', opts=['sort', 'sorts', 'sorted'], ans=0, pt='Nós sempre separamos o lixo em casa.', why='Com “we” o presente fica na forma base: sort.')],
 expressions=[
  dict(en='Where does the trash go?', pt='Onde vai o lixo?', ex='Excuse me, where does the trash go?', exp='Para perguntar a um vizinho onde deixar o lixo.', c='a'),
  dict(en='When do they collect it?', pt='Quando eles recolhem?', ex='When do they collect the recycling?', exp='Para saber o dia da coleta.', c='b'),
  dict(en='take out the trash', pt='levar o lixo para fora', ex='I take out the trash every night.', exp='Tarefa doméstica muito comum nos EUA.', c='c'),
  dict(en='goes in', pt='vai em / vai na', ex='Glass goes in the green bin.', exp='Para dizer em que lixeira cada coisa entra.', c='d'),
  dict(en='Thanks for the reminder.', pt='Obrigado pelo lembrete.', ex='Oops! Thanks for the reminder.', exp='Quando alguém lembra você de algo.', c='a'),
  dict(en='I\'m on it.', pt='Já estou cuidando disso.', ex='The trash? I\'m on it.', exp='Resposta informal para dizer que você vai fazer algo agora.', c='b')],
 expr_game=[
  dict(cue='Você quer saber o dia em que passa o caminhão do lixo.', opts=['When do they collect it?', 'Where does the trash go?', 'I\'m on it.'], ans=0, why='When... pergunta o momento; collect é o verbo da coleta.'),
  dict(cue='Um vizinho lembra você de levar o lixo para fora.', opts=['Thanks for the reminder.', 'Glass goes in the green bin.', 'When do they collect it?'], ans=0, why='Thanks for the reminder agradece o lembrete.'),
  dict(cue='Você quer dizer que vidro vai na lixeira verde.', opts=['Glass goes in the green bin.', 'I\'m on it.', 'Where does glass go?'], ans=0, why='goes in diz onde cada coisa entra.')])
