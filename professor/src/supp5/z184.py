"""Bloco de verbos e expressões da aula 184: pneu furado."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('stop', '🛑', 'parar', ('stop', 'I stop on the side.', 'Eu paro no acostamento.'), ('stops', 'Sam stops the car.', 'O Sam para o carro.'), ('stopped', 'We stopped near the exit.', 'Paramos perto da saída.'), ('stopping', 'I am stopping now.', 'Estou parando agora.'), 'Stop dobra o p: stopped, stopping.'),
  vb('change', '🔄', 'trocar', ('change', 'I change the tire.', 'Eu troco o pneu.'), ('changes', 'He changes the wheel.', 'Ele troca a roda.'), ('changed', 'We changed the tire.', 'Trocamos o pneu.'), ('changing', 'She is changing it.', 'Ela está trocando.'), 'Change a tire = trocar o pneu. Perde o e antes de -ing.'),
  vb('pull', '🧲', 'puxar', ('pull', 'I pull the car over.', 'Eu encosto o carro.'), ('pulls', 'He pulls the bag out.', 'Ele puxa a bolsa para fora.'), ('pulled', 'Sam pulled over.', 'O Sam encostou.'), ('pulling', 'I am pulling the handle.', 'Estou puxando a alavanca.'), 'Pull over = encostar o carro.'),
  vb('push', '👉', 'empurrar', ('push', 'We push the car.', 'Nós empurramos o carro.'), ('pushes', 'He pushes the button.', 'Ele aperta o botão.'), ('pushed', 'She pushed the door.', 'Ela empurrou a porta.'), ('pushing', 'They are pushing it.', 'Eles estão empurrando.'), 'A 3ª pessoa de push leva -es: pushes.'),
  vb('lift', '⬆️', 'levantar', ('lift', 'I lift the car with a jack.', 'Eu levanto o carro com um macaco.'), ('lifts', 'He lifts the spare.', 'Ele levanta o estepe.'), ('lifted', 'We lifted the bag.', 'Levantamos a bolsa.'), ('lifting', 'I am lifting the wheel.', 'Estou levantando a roda.'), 'Lift = levantar algo pesado.')],
 verb_game=[
  dict(scene='O Sam para o carro agora.', en='Sam ___ the car.', opts=['stop', 'stops', 'stopped'], ans=1, pt='O Sam para o carro.', why='Com Sam (ele), o presente leva -s: stops.'),
  dict(scene='Ontem vocês trocaram o pneu.', en='Yesterday we ___ the tire.', opts=['change', 'changed', 'changing'], ans=1, pt='Ontem trocamos o pneu.', why='Yesterday pede passado: changed.'),
  dict(scene='Eles estão empurrando o carro agora.', en='They are ___ the car.', opts=['push', 'pushes', 'pushing'], ans=2, pt='Eles estão empurrando o carro.', why='Are + verbo termina em -ing: pushing.'),
  dict(scene='Você encosta o carro.', en='I ___ the car over.', opts=['pull', 'pulls', 'pulled'], ans=0, pt='Eu encosto o carro.', why='Com I, o presente fica na forma base: pull.')],
 expressions=[
  dict(en='flat tire', pt='pneu furado', ex='I have a flat tire.', exp='O problema mais comum na estrada.', c='a'),
  dict(en='on the side of the road', pt='no acostamento', ex='I’m on the side of the road.', exp='Para dizer que está em um lugar seguro.', c='b'),
  dict(en='What’s your location?', pt='Qual é sua localização?', ex='What’s your location? — Highway ten.', exp='Pergunta do atendente.', c='c'),
  dict(en='spare tire', pt='estepe', ex='Do you have a spare tire?', exp='Pneu reserva no carro.', c='d'),
  dict(en='Stay put.', pt='Fique onde está.', ex='Stay put. Help is on the way.', exp='Para pedir que alguém não saia do lugar.', c='a'),
  dict(en='Tow it.', pt='Rebocar.', ex='We can tow it to a shop.', exp='Levar o carro com um guincho.', c='b')],
 expr_game=[
  dict(cue='Você diz ao atendente qual é o problema.', opts=['I have a flat tire.', 'Stay put.', 'Tow it.'], ans=0, why='Flat tire = pneu furado.'),
  dict(cue='O atendente pergunta onde você está.', opts=['A white Honda.', 'Highway ten, near exit five.', 'Do you have a spare?'], ans=1, why='A pergunta pede o lugar.'),
  dict(cue='Você quer dizer que está em lugar seguro.', opts=['I’m on the side of the road.', 'What’s your location?', 'Tow it.'], ans=0, why='On the side of the road = no acostamento.')])
