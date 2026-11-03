"""Bloco de verbos e expressões da aula 49: estacionar o carro."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('park', '🅿️', 'estacionar', ('park', 'I park here.', 'Eu estaciono aqui.'), ('parks', 'Sam parks in the lot.', 'O Sam estaciona no estacionamento.'), ('parked', 'We parked on Oak Street.', 'Nós estacionamos na Oak Street.'), ('parking', 'I am parking now.', 'Estou estacionando agora.'), 'Park é regular: parked, parking.'),
  vb('pay', '💳', 'pagar', ('pay', 'I pay at the machine.', 'Eu pago na máquina.'), ('pays', 'She pays for parking.', 'Ela paga o estacionamento.'), ('paid', 'He paid two dollars.', 'Ele pagou dois dólares.'), ('paying', 'I am paying now.', 'Estou pagando agora.'), 'Atenção: pay vira paid (não “payed”).'),
  vb('lock', '🔒', 'trancar', ('lock', 'I lock the car.', 'Eu tranco o carro.'), ('locks', 'He locks the door.', 'Ele tranca a porta.'), ('locked', 'We locked the car.', 'Nós trancamos o carro.'), ('locking', 'I am locking it.', 'Estou trancando.'), 'Lock é regular: locked.'),
  vb('open', '🚪', 'abrir', ('open', 'I open the car door.', 'Eu abro a porta do carro.'), ('opens', 'She opens the trunk.', 'Ela abre o porta-malas.'), ('opened', 'He opened the door.', 'Ele abriu a porta.'), ('opening', 'I am opening the door.', 'Estou abrindo a porta.'), 'Passado só acrescenta -ed: opened.'),
  vb('drive', '🚗', 'dirigir', ('drive', 'I drive to the shop.', 'Eu dirijo até a loja.'), ('drives', 'Tom drives to work.', 'O Tom dirige até o trabalho.'), ('drove', 'We drove downtown.', 'Nós dirigimos até o centro.'), ('driving', 'I am driving to the lot.', 'Estou dirigindo até o estacionamento.'), 'Irregular: drive vira drove.')],
 verb_game=[
  dict(scene='Você quer estacionar em frente à loja.', en='Can I ___ here?', opts=['park', 'parks', 'parked'], ans=0, pt='Posso estacionar aqui?', why='Depois de “can”, usa-se a forma base: park.'),
  dict(scene='Ontem você trancou o carro.', en='I ___ the car yesterday.', opts=['lock', 'locked', 'locking'], ans=1, pt='Eu tranquei o carro ontem.', why='“Yesterday” pede passado: locked.'),
 dict(scene='A Ana paga o tíquete na máquina.', en='Ana ___ at the machine.', opts=['pay', 'pays', 'paid'], ans=1, pt='A Ana paga na máquina.', why='Ana (ela) no presente leva -s: pays.'),
  dict(scene='Agora você está estacionando.', en='I am ___ now.', opts=['park', 'parks', 'parking'], ans=2, pt='Estou estacionando agora.', why='“am” + -ing: parking.')],
 expressions=[
  dict(en='Can I park here?', pt='Posso estacionar aqui?', ex='Excuse me, can I park here?', exp='Para checar se pode parar o carro.', c='a'),
  dict(en='Where can I park?', pt='Onde posso estacionar?', ex='Where can I park near the shop?', exp='Para achar um lugar permitido.', c='b'),
  dict(en='no parking zone', pt='zona de proibido estacionar', ex='This is a no parking zone.', exp='Aviso de que é proibido parar o carro.', c='c'),
  dict(en='parking lot', pt='estacionamento', ex='There is a parking lot on Oak Street.', exp='Lugar com vagas para carros.', c='d'),
  dict(en='dollars an hour', pt='dólares por hora', ex='It’s five dollars an hour.', exp='Como se diz o preço do estacionamento.', c='a'),
  dict(en='Drive safe!', pt='Dirija com cuidado!', ex='Thanks for the help. Drive safe!', exp='Despedida para quem vai dirigir.', c='b')],
 expr_game=[
  dict(cue='Você quer achar um lugar para o carro.', opts=['Where can I park?', 'Drive safe!', 'No parking zone.'], ans=0, why='Where can I park? pergunta onde estacionar.'),
  dict(cue='Você quer saber o preço do estacionamento.', opts=['How much is it?', 'Can I park here?', 'Drive safe!'], ans=0, why='How much is it? pergunta o preço.'),
  dict(cue='Seu amigo vai dirigir para casa.', opts=['Drive safe!', 'Where can I park?', 'It’s five dollars.'], ans=0, why='Drive safe! é a despedida para quem dirige.')])
