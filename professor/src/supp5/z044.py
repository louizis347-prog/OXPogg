"""Bloco de verbos e expressões da aula 44: dar e seguir direções."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('turn', '↪️', 'virar', ('turn', 'I turn left here.', 'Eu viro à esquerda aqui.'), ('turns', 'The road turns right.', 'A rua vira à direita.'), ('turned', 'We turned at the light.', 'Nós viramos no semáforo.'), ('turning', 'I am turning right.', 'Estou virando à direita.'), 'Turn left / turn right: sempre com a direção.'),
  vb('go', '➡️', 'ir', ('go', 'You go straight.', 'Você vai em frente.'), ('goes', 'The road goes to the park.', 'A rua vai até o parque.'), ('went', 'We went two blocks.', 'Nós fomos dois quarteirões.'), ('going', 'I am going to the museum.', 'Estou indo ao museu.'), 'Irregular: go vira went.'),
  vb('cross', '🚸', 'atravessar', ('cross', 'I cross the street.', 'Eu atravesso a rua.'), ('crosses', 'She crosses at the light.', 'Ela atravessa no semáforo.'), ('crossed', 'We crossed Main Street.', 'Nós atravessamos a Main Street.'), ('crossing', 'I am crossing now.', 'Estou atravessando agora.'), 'Cross the street = atravessar a rua.'),
  vb('stop', '🛑', 'parar', ('stop', 'I stop at the corner.', 'Eu paro na esquina.'), ('stops', 'He stops at the light.', 'Ele para no semáforo.'), ('stopped', 'We stopped at the library.', 'Nós paramos na biblioteca.'), ('stopping', 'I am stopping here.', 'Estou parando aqui.'), 'Dobra o p no passado: stopped, stopping.'),
  vb('see', '👀', 'ver', ('see', 'I see the building.', 'Eu vejo o prédio.'), ('sees', 'Ana sees the red door.', 'A Ana vê a porta vermelha.'), ('saw', 'We saw the museum.', 'Nós vimos o museu.'), ('seeing', 'I am seeing the park.', 'Estou vendo o parque.'), 'Irregular: see vira saw.')],
 verb_game=[
  dict(scene='Você segue direto por dois quarteirões.', en='We ___ straight for two blocks.', opts=['go', 'goes', 'went'], ans=0, pt='Nós vamos em frente por dois quarteirões.', why='Com “we”, presente na forma base: go.'),
  dict(scene='No semáforo, a Ana vira à esquerda.', en='Ana ___ left at the light.', opts=['turn', 'turns', 'turning'], ans=1, pt='A Ana vira à esquerda no semáforo.', why='Ana (ela) leva -s: turns.'),
  dict(scene='Ontem você viu o museu da esquina.', en='I ___ the museum yesterday.', opts=['see', 'sees', 'saw'], ans=2, pt='Eu vi o museu ontem.', why='“Yesterday” pede passado: saw.'),
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
