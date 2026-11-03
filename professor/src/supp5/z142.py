"""Bloco de verbos e expressões da aula 142: trânsito em Los Angeles."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('drive', '🚗', 'dirigir', ('drive', 'We drive to the beach.', 'Nós dirigimos até a praia.'), ('drives', 'Marco drives a blue car.', 'O Marco dirige um carro azul.'), ('drove', 'We drove for two hours.', 'Nós dirigimos por duas horas.'), ('driving', 'I am driving now.', 'Estou dirigindo agora.'), 'Drive é irregular: drove no passado.'),
  vb('hurry', '🏃', 'apressar-se', ('hurry', 'We hurry to the car.', 'Nós nos apressamos até o carro.'), ('hurries', 'Lena hurries to the door.', 'A Lena corre até a porta.'), ('hurried', 'We hurried to the exit.', 'Nós nos apressamos até a saída.'), ('hurrying', 'We are hurrying now.', 'Estamos nos apressando agora.'), 'Hurry troca y por i: hurries, hurried.'),
  vb('turn', '↩️', 'virar', ('turn', 'We turn left here.', 'Nós viramos à esquerda aqui.'), ('turns', 'Marco turns right.', 'O Marco vira à direita.'), ('turned', 'We turned at the light.', 'Nós viramos no sinal.'), ('turning', 'We are turning now.', 'Estamos virando agora.'), 'Turn left / turn right = virar à esquerda / à direita.'),
  vb('stop', '🛑', 'parar', ('stop', 'Cars stop at the light.', 'Os carros param no sinal.'), ('stops', 'The bus stops here.', 'O ônibus para aqui.'), ('stopped', 'We stopped for gas.', 'Nós paramos para abastecer.'), ('stopping', 'We are stopping now.', 'Estamos parando agora.'), 'Stop dobra o p: stopped, stopping.'),
  vb('move', '➡️', 'mover-se', ('move', 'The cars move slowly.', 'Os carros se movem devagar.'), ('moves', 'Nobody moves.', 'Ninguém se move.'), ('moved', 'The traffic moved fast.', 'O trânsito andou rápido.'), ('moving', 'The cars are not moving.', 'Os carros não estão andando.'), 'Move perde o e antes de -ing: moving.')],
 verb_game=[
  dict(scene='Agora os carros não andam.', en='The cars are not ___.', opts=['move', 'moving', 'moved'], ans=1, pt='Os carros não estão andando.', why='“are not” + -ing: moving.'),
  dict(scene='Ontem vocês dirigiram duas horas.', en='Yesterday we ___ for two hours.', opts=['drive', 'drives', 'drove'], ans=2, pt='Ontem nós dirigimos por duas horas.', why='Passado irregular: drove.'),
  dict(scene='O Marco vira à direita.', en='Marco ___ right at the corner.', opts=['turn', 'turns', 'turned'], ans=1, pt='O Marco vira à direita na esquina.', why='Ele (3ª pessoa) leva -s: turns.'),
  dict(scene='Vocês querem parar para abastecer.', en='We want to ___ for gas.', opts=['stop', 'stops', 'stopped'], ans=0, pt='Queremos parar para abastecer.', why='Depois de to, use o verbo base: stop.')],
 expressions=[
  dict(en='Are you ready to go?', pt='Você está pronto para ir?', ex='Hi! Are you ready to go?', exp='Para saber se a pessoa já pode sair.', c='a'),
  dict(en='How long to…?', pt='Quanto tempo até…?', ex='How long to the beach?', exp='Para perguntar a duração de uma viagem.', c='b'),
  dict(en='Without traffic', pt='Sem trânsito', ex='Without traffic, it is thirty minutes.', exp='Para falar do tempo ideal da viagem.', c='c'),
  dict(en='Stuck in traffic', pt='Preso no trânsito', ex='Sorry, I am stuck in traffic.', exp='Para explicar um atraso.', c='d'),
  dict(en='Take the side streets', pt='Pegar as ruas laterais', ex='Let’s take the side streets.', exp='Para sugerir fugir da rodovia.', c='a'),
  dict(en='Good call!', pt='Boa escolha!', ex='The shortcut works. Good call!', exp='Para elogiar uma decisão acertada.', c='b')],
 expr_game=[
  dict(cue='Você quer saber a duração até a praia.', opts=['How long to the beach?', 'Good call!', 'Stuck in traffic'], ans=0, why='How long to… pergunta o tempo da viagem.'),
  dict(cue='Você avisa que vai chegar atrasado por causa dos carros.', opts=['I am stuck in traffic.', 'Are you ready to go?', 'Good call!'], ans=0, why='Stuck in traffic explica o atraso.'),
  dict(cue='O amigo achou um bom atalho e você elogia.', opts=['Good call!', 'Without traffic', 'How long to the beach?'], ans=0, why='Good call! elogia uma boa decisão.')])
