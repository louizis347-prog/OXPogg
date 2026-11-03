"""Bloco de verbos e expressões da aula 057: estou perdido."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('lose', '😟', 'perder', ('lose', 'I lose my way.', 'Eu perco o caminho.'), ('loses', 'She loses her map.', 'Ela perde o mapa.'), ('lost', 'We lost the bus.', 'Nós perdemos o ônibus.'), ('losing', 'I am losing my way.', 'Estou me perdendo.'), 'Lose vira lost no passado. “I’m lost” usa o adjetivo lost (perdido).'),
  vb('find', '🔍', 'encontrar', ('find', 'We find the stop.', 'Nós encontramos o ponto.'), ('finds', 'Jim finds a map.', 'O Jim encontra um mapa.'), ('found', 'I found the museum.', 'Eu encontrei o museu.'), ('finding', 'I am finding the way.', 'Estou encontrando o caminho.'), 'Find vira found no passado (irregular).'),
  vb('follow', '👣', 'seguir', ('follow', 'I follow the map.', 'Eu sigo o mapa.'), ('follows', 'He follows the bus.', 'Ele segue o ônibus.'), ('followed', 'We followed the sign.', 'Nós seguimos a placa.'), ('following', 'I am following the street.', 'Estou seguindo a rua.'), 'Follow é regular: follows, followed, following.'),
  vb('point', '👉', 'apontar', ('point', 'I point at the stop.', 'Eu aponto para o ponto.'), ('points', 'Ned points down the street.', 'O Ned aponta rua abaixo.'), ('pointed', 'He pointed at the map.', 'Ele apontou para o mapa.'), ('pointing', 'She is pointing at the bus.', 'Ela está apontando para o ônibus.'), 'Point at = apontar para. Regular: pointed.'),
  vb('ask', '🙋', 'perguntar / pedir', ('ask', 'We ask a woman.', 'Nós perguntamos a uma mulher.'), ('asks', 'Grace asks the way.', 'A Grace pergunta o caminho.'), ('asked', 'I asked a man.', 'Eu perguntei a um homem.'), ('asking', 'I am asking for help.', 'Estou pedindo ajuda.'), 'Ask for help = pedir ajuda. Passado regular: asked.')],
 verb_game=[
  dict(scene='Ontem você perdeu o ônibus.', en='Yesterday I ___ the bus.', opts=['lose', 'lost', 'losing'], ans=1, pt='Ontem eu perdi o ônibus.', why='“Yesterday” pede passado: lost.'),
  dict(scene='O Ned aponta para o ponto agora.', en='Ned ___ at the stop.', opts=['point', 'pointed', 'points'], ans=2, pt='O Ned aponta para o ponto.', why='Com “Ned” (ele) o presente leva -s: points.'),
  dict(scene='Você quer pedir ajuda agora.', en='I am ___ for help.', opts=['ask', 'asking', 'asks'], ans=1, pt='Estou pedindo ajuda.', why='“am” + -ing: asking.'),
  dict(scene='Ontem você encontrou o museu.', en='Yesterday I ___ the museum.', opts=['find', 'found', 'finds'], ans=1, pt='Ontem eu encontrei o museu.', why='Passado irregular de find: found.')],
 expressions=[
  dict(en='Excuse me, I’m lost.', pt='Com licença, estou perdido.', ex='Excuse me, I’m lost. Where is the museum?', exp='Para pedir ajuda a um desconhecido.', c='a'),
  dict(en='Where do you want to go?', pt='Aonde você quer ir?', ex='Where do you want to go? — To the park.', exp='Para perguntar o destino da pessoa.', c='b'),
  dict(en='It’s far from here.', pt='Fica longe daqui.', ex='It’s far from here. Take the bus.', exp='Para dizer que o lugar é longe.', c='c'),
  dict(en='Take the bus.', pt='Pegue o ônibus.', ex='Take the bus. It’s number eighty-six.', exp='Para sugerir um transporte.', c='d'),
  dict(en='Good luck!', pt='Boa sorte!', ex='Good luck! You can do it.', exp='Para desejar sorte a quem vai embora.', c='a'),
  dict(en='Safe travels!', pt='Boa viagem!', ex='Thanks, and safe travels!', exp='Para se despedir de quem viaja.', c='b')],
 expr_game=[
  dict(cue='Você precisa de ajuda e não sabe onde está.', opts=['Excuse me, I’m lost.', 'Safe travels!', 'Take the bus.'], ans=0, why='I’m lost = estou perdido.'),
  dict(cue='Você quer saber para onde a pessoa vai.', opts=['Where do you want to go?', 'It’s far from here.', 'Good luck!'], ans=0, why='Where do you want to go? pergunta o destino.'),
  dict(cue='Você quer dizer que o museu fica longe.', opts=['It’s far from here.', 'Take the bus.', 'Excuse me, I’m lost.'], ans=0, why='Far from here = longe daqui.')])
