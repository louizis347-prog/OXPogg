"""Bloco de verbos e expressões da aula 44: dar e seguir direções."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('veer', '↗️', 'desviar / pegar levemente', ('veer', 'I veer right here.', 'Eu pego levemente à direita aqui.'), ('veers', 'The road veers left.', 'A rua faz uma curva leve à esquerda.'), ('veered', 'We veered left.', 'Nós desviamos à esquerda.'), ('veering', 'I am veering right.', 'Estou desviando à direita.'), 'Veer é uma curva suave, não uma esquina.'),
  vb('pass', '🏛️', 'passar por', ('pass', 'We pass the bank.', 'Nós passamos pelo banco.'), ('passes', 'He passes the park.', 'Ele passa pelo parque.'), ('passed', 'I passed the museum.', 'Eu passei pelo museu.'), ('passing', 'I am passing the school.', 'Estou passando pela escola.'), 'Pass vira passes com ele/ela.'),
  vb('cross', '🚸', 'atravessar', ('cross', 'I cross the street.', 'Eu atravesso a rua.'), ('crosses', 'She crosses at the light.', 'Ela atravessa no semáforo.'), ('crossed', 'We crossed Main Street.', 'Nós atravessamos a Main Street.'), ('crossing', 'I am crossing now.', 'Estou atravessando agora.'), 'Cross the street = atravessar a rua.'),
  vb('stop', '🛑', 'parar', ('stop', 'I stop at the corner.', 'Eu paro na esquina.'), ('stops', 'He stops at the light.', 'Ele para no semáforo.'), ('stopped', 'We stopped at the library.', 'Nós paramos na biblioteca.'), ('stopping', 'I am stopping here.', 'Estou parando aqui.'), 'Dobra o p no passado: stopped, stopping.'),
  vb('spot', '🔭', 'avistar', ('spot', 'I spot the sign.', 'Eu avisto a placa.'), ('spots', 'She spots the bank.', 'Ela avista o banco.'), ('spotted', 'We spotted the park.', 'Nós avistamos o parque.'), ('spotting', 'I am spotting the tower.', 'Estou avistando a torre.'), 'Spot dobra o t: spotted, spotting.')],
 verb_game=[
  dict(scene='Vocês passam pelo banco à esquerda.', en='We ___ the bank on the left.', opts=['pass', 'passes', 'passed'], ans=0, pt='Nós passamos pelo banco à esquerda.', why='Com “we”, presente na forma base: pass.'),
  dict(scene='Na bifurcação, a Ana pega levemente à direita.', en='Ana ___ right at the fork.', opts=['veer', 'veers', 'veering'], ans=1, pt='A Ana pega levemente à direita na bifurcação.', why='Ana (ela) leva -s: veers.'),
  dict(scene='Ontem você avistou o museu da esquina.', en='I ___ the museum yesterday.', opts=['spot', 'spots', 'spotted'], ans=2, pt='Eu avistei o museu ontem.', why='“Yesterday” pede passado: spotted (o t dobra).'),
  dict(scene='Agora você está atravessando a rua.', en='I am ___ the street.', opts=['cross', 'crosses', 'crossing'], ans=2, pt='Estou atravessando a rua.', why='“am” + -ing: crossing.')],
 expressions=[
  dict(en='How do I get to…?', pt='Como chego a…?', ex='How do I get to the library?', exp='Para pedir o caminho até um lugar.', c='a'),
  dict(en='Go straight.', pt='Siga em frente.', ex='Go straight for two blocks.', exp='Para dizer que não deve virar.', c='b'),
  dict(en='Turn left / right.', pt='Vire à esquerda / direita.', ex='Turn left at the traffic light.', exp='Para indicar uma curva.', c='c'),
  dict(en='on your right', pt='à sua direita', ex='The museum is on your right.', exp='Para dizer em que lado fica o lugar.', c='d'),
  dict(en='at the corner', pt='na esquina', ex='Turn right at the corner.', exp='Para marcar onde virar.', c='a'),
  dict(en='You can’t miss it.', pt='Não tem erro.', ex='It’s a big red door. You can’t miss it.', exp='Para dizer que o lugar é fácil de ver.', c='b')],
 expr_game=[
  dict(cue='Você quer pedir o caminho até a biblioteca.', opts=['How do I get to the library?', 'Go straight.', 'On your right.'], ans=0, why='How do I get to…? pede o caminho.'),
  dict(cue='Você diz a alguém para não virar, seguir direto.', opts=['Turn left.', 'Go straight.', 'You can’t miss it.'], ans=1, why='Go straight = siga em frente.'),
  dict(cue='O lugar é tão visível que ninguém erra.', opts=['You can’t miss it.', 'At the corner.', 'How do I get to…?'], ans=0, why='You can’t miss it = não tem erro.')])
