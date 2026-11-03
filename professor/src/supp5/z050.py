"""Bloco de verbos e expressões da aula 50: abastecer no posto."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('fill', '⛽', 'encher', ('fill', 'I fill the tank.', 'Eu encho o tanque.'), ('fills', 'She fills the car.', 'Ela enche o carro.'), ('filled', 'He filled the tank.', 'Ele encheu o tanque.'), ('filling', 'I am filling the car.', 'Estou enchendo o carro.'), 'Fill up = encher o tanque.'),
  vb('put', '⛽', 'colocar / pôr', ('put', 'I put gas in the car.', 'Eu ponho gasolina no carro.'), ('puts', 'She puts gas in the tank.', 'Ela põe gasolina no tanque.'), ('put', 'He put ten dollars in.', 'Ele pôs dez dólares.'), ('putting', 'I am putting gas in.', 'Estou pondo gasolina.'), 'Put não muda no passado: put, put.'),
  vb('open', '🔓', 'abrir', ('open', 'I open the gas cap.', 'Eu abro a tampa do tanque.'), ('opens', 'She opens the cap.', 'Ela abre a tampa.'), ('opened', 'He opened the cap.', 'Ele abriu a tampa.'), ('opening', 'I am opening the cap.', 'Estou abrindo a tampa.'), 'Passado só acrescenta -ed: opened.'),
  vb('close', '🔒', 'fechar', ('close', 'I close the cap.', 'Eu fecho a tampa.'), ('closes', 'She closes the door.', 'Ela fecha a porta.'), ('closed', 'He closed the cap.', 'Ele fechou a tampa.'), ('closing', 'I am closing the cap.', 'Estou fechando a tampa.'), 'Close = fechar; o contrário de open.'),
  vb('clean', '🧹', 'limpar', ('clean', 'I clean the window.', 'Eu limpo o vidro.'), ('cleans', 'She cleans the car.', 'Ela limpa o carro.'), ('cleaned', 'He cleaned the mirror.', 'Ele limpou o espelho.'), ('cleaning', 'I am cleaning the car.', 'Estou limpando o carro.'), 'Clean = limpar; passado: cleaned.')],
 verb_game=[
 dict(scene='Você abre a tampa do tanque.', en='I ___ the gas cap.', opts=['open', 'opens', 'opened'], ans=0, pt='Eu abro a tampa do tanque.', why='Com “I”, presente na forma base: open.'),
  dict(scene='Ontem o Sam encheu o tanque.', en='Sam ___ the tank yesterday.', opts=['fill', 'fills', 'filled'], ans=2, pt='O Sam encheu o tanque ontem.', why='“Yesterday” pede passado: filled.'),
 dict(scene='A Ana fecha a tampa.', en='Ana ___ the cap.', opts=['close', 'closes', 'closed'], ans=1, pt='A Ana fecha a tampa.', why='Ana (ela) no presente leva -s: closes.'),
 dict(scene='Agora você está colocando gasolina.', en='I am ___ gas in.', opts=['put', 'puts', 'putting'], ans=2, pt='Estou colocando gasolina.', why='“am” + -ing: putting (o t dobra).')],
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
