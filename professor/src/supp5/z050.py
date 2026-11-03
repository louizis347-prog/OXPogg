"""Bloco de verbos e expressões da aula 50: abastecer no posto."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('fill', '⛽', 'encher', ('fill', 'I fill the tank.', 'Eu encho o tanque.'), ('fills', 'She fills the car.', 'Ela enche o carro.'), ('filled', 'He filled the tank.', 'Ele encheu o tanque.'), ('filling', 'I am filling the car.', 'Estou enchendo o carro.'), 'Fill up = encher o tanque.'),
  vb('pump', '🔧', 'bombear / abastecer', ('pump', 'I pump the gas.', 'Eu abasteço o carro.'), ('pumps', 'Sam pumps the gas.', 'O Sam abastece.'), ('pumped', 'We pumped twenty dollars.', 'Nós abastecemos vinte dólares.'), ('pumping', 'I am pumping gas.', 'Estou abastecendo.'), 'Nos EUA, quase sempre você mesmo abastece (pump gas).'),
  vb('choose', '☑️', 'escolher', ('choose', 'I choose regular.', 'Eu escolho comum.'), ('chooses', 'Ana chooses premium.', 'A Ana escolhe premium.'), ('chose', 'He chose regular.', 'Ele escolheu comum.'), ('choosing', 'I am choosing a pump.', 'Estou escolhendo uma bomba.'), 'Irregular: choose vira chose.'),
  vb('pay', '💳', 'pagar', ('pay', 'I pay inside.', 'Eu pago lá dentro.'), ('pays', 'He pays by card.', 'Ele paga no cartão.'), ('paid', 'We paid twenty dollars.', 'Nós pagamos vinte dólares.'), ('paying', 'I am paying now.', 'Estou pagando agora.'), 'Irregular: pay vira paid.'),
  vb('need', '📌', 'precisar', ('need', 'I need gas.', 'Eu preciso de gasolina.'), ('needs', 'The car needs gas.', 'O carro precisa de gasolina.'), ('needed', 'We needed water.', 'Nós precisávamos de água.'), ('needing', 'He is needing gas.', 'Ele está precisando de gasolina.'), 'Need + substantivo: need gas. Na fala, prefira I need…')],
 verb_game=[
  dict(scene='Você quer escolher a gasolina comum.', en='I ___ regular, please.', opts=['choose', 'chooses', 'chose'], ans=0, pt='Eu escolho a comum, por favor.', why='Com “I”, presente na forma base: choose.'),
  dict(scene='Ontem o Sam encheu o tanque.', en='Sam ___ the tank yesterday.', opts=['fill', 'fills', 'filled'], ans=2, pt='O Sam encheu o tanque ontem.', why='“Yesterday” pede passado: filled.'),
  dict(scene='A Ana paga lá dentro.', en='Ana ___ inside.', opts=['pay', 'pays', 'paid'], ans=1, pt='A Ana paga lá dentro.', why='Ana (ela) no presente leva -s: pays.'),
  dict(scene='Agora você está abastecendo.', en='I am ___ gas.', opts=['pump', 'pumps', 'pumping'], ans=2, pt='Estou abastecendo.', why='“am” + -ing: pumping.')],
 expressions=[
  dict(en='Pump number three, please.', pt='Bomba número três, por favor.', ex='Hi! Pump number three, please.', exp='Para dizer qual bomba você usou.', c='a'),
  dict(en='Regular or premium?', pt='Comum ou premium?', ex='Regular or premium? — Regular, please.', exp='Pergunta sobre o tipo de gasolina.', c='b'),
  dict(en='Twenty dollars, please.', pt='Vinte dólares, por favor.', ex='Twenty dollars of regular, please.', exp='Para dizer quanto quer abastecer.', c='c'),
  dict(en='fill it up', pt='encher o tanque', ex='Fill it up, please.', exp='Para pedir o tanque cheio.', c='d'),
  dict(en='Anything else?', pt='Mais alguma coisa?', ex='Anything else? — A bottle of water.', exp='O caixa pergunta se falta algo.', c='a'),
  dict(en='Drive safe!', pt='Dirija com cuidado!', ex='Thanks! Drive safe!', exp='Despedida para quem vai dirigir.', c='b')],
 expr_game=[
  dict(cue='Você quer encher o tanque.', opts=['Fill it up, please.', 'Regular or premium?', 'Drive safe!'], ans=0, why='Fill it up = encher o tanque.'),
  dict(cue='O caixa pergunta o tipo de gasolina.', opts=['Regular, please.', 'Anything else?', 'Drive safe!'], ans=0, why='Regular, please responde ao tipo.'),
  dict(cue='Você quer dizer qual bomba usou.', opts=['Pump number three, please.', 'Anything else?', 'Fill it up.'], ans=0, why='Pump number… informa a bomba.')])
