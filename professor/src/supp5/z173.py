"""Bloco de verbos e expressões da aula 173: drive-thru."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('pull', '⬆️', 'puxar, avançar', ('pull', 'I pull forward.', 'Eu avanço o carro.'), ('pulls', 'Bo pulls to the window.', 'O Bo avança até a janela.'), ('pulled', 'We pulled forward.', 'Nós avançamos.'), ('pulling', 'I am pulling forward.', 'Estou avançando.'), 'Pull forward = avançar o carro um pouco. Passado regular: pulled.'),
  vb('hand', '🤝', 'entregar', ('hand', 'I hand him the money.', 'Eu entrego o dinheiro a ele.'), ('hands', 'Kai hands me the bag.', 'O Kai me entrega a sacola.'), ('handed', 'She handed me a straw.', 'Ela me entregou um canudo.'), ('handing', 'He is handing me the drink.', 'Ele está me entregando a bebida.'), 'Hand + pessoa + coisa: hand me the bag.'),
  vb('drive', '🚗', 'dirigir', ('drive', 'We drive to the window.', 'Nós dirigimos até a janela.'), ('drives', 'Bo drives every day.', 'O Bo dirige todo dia.'), ('drove', 'I drove to the drive-thru.', 'Eu dirigi até o drive-thru.'), ('driving', 'I am driving now.', 'Estou dirigindo agora.'), 'Drive é irregular: drove no passado.'),
  vb('hear', '👂', 'ouvir', ('hear', 'I hear the speaker.', 'Eu ouço o alto-falante.'), ('hears', 'Bo hears Kai.', 'O Bo ouve o Kai.'), ('heard', 'I heard the price.', 'Eu ouvi o preço.'), ('hearing', 'I am hearing a loud noise.', 'Estou ouvindo um barulho alto.'), 'Hear é irregular: heard. Hear = ouvir sem querer; listen = prestar atenção.'),
  vb('repeat', '🔁', 'repetir', ('repeat', 'Please repeat the price.', 'Por favor, repita o preço.'), ('repeats', 'Kai repeats the order.', 'O Kai repete o pedido.'), ('repeated', 'He repeated my order.', 'Ele repetiu meu pedido.'), ('repeating', 'I am repeating my order.', 'Estou repetindo meu pedido.'), 'Repeat = dizer de novo; passado regular: repeated.')],
 verb_game=[
  dict(scene='O atendente pede para você avançar o carro.', en='Please ___ forward.', opts=['pull', 'pulls', 'pulled'], ans=0, pt='Por favor, avance.', why='Em pedidos com please, use o verbo base: pull.'),
  dict(scene='Agora o Bo está dirigindo até a janela.', en='Bo is ___ to the window.', opts=['drive', 'drives', 'driving'], ans=2, pt='O Bo está dirigindo até a janela.', why='“is” + verbo termina em -ing: driving.'),
  dict(scene='O Kai entrega a sacola toda vez.', en='Kai ___ me the bag.', opts=['hand', 'hands', 'handed'], ans=1, pt='O Kai me entrega a sacola.', why='Com Kai (ele), o presente leva -s: hands.'),
  dict(scene='Ontem você não ouviu o preço.', en='Yesterday I did not ___ the price.', opts=['hear', 'heard', 'hears'], ans=0, pt='Ontem eu não ouvi o preço.', why='Depois de did not, use o verbo base: hear.')],
 expressions=[
  dict(en='Drive-thru', pt='Drive-thru', ex='Let’s go to the drive-thru.', exp='Lugar onde você pede e pega comida sem sair do carro.', c='a'),
  dict(en='Fast food', pt='Comida rápida', ex='I eat fast food on Fridays.', exp='Comida pronta e rápida, como hambúrguer e batata.', c='b'),
  dict(en='To go', pt='Para levar', ex='A burger to go, please.', exp='Para dizer que vai levar a comida.', c='c'),
  dict(en='Hold the onions.', pt='Sem cebola.', ex='A burger, hold the onions.', exp='Para pedir sem um ingrediente.', c='d'),
  dict(en='Super size it.', pt='Faça o tamanho maior.', ex='Can you super size it?', exp='Para pedir a versão maior do combo.', c='a'),
  dict(en='Pull forward.', pt='Avance o carro.', ex='Pull forward to the window.', exp='O atendente diz isso para você ir à próxima janela.', c='b')],
 expr_game=[
  dict(cue='Você quer o hambúrguer sem cebola.', opts=['Hold the onions.', 'Pull forward.', 'To go.'], ans=0, why='Hold the onions = sem cebola.'),
  dict(cue='Você é atendente e quer que o carro vá à janela.', opts=['Fast food.', 'Pull forward.', 'Hold the onions.'], ans=1, why='Pull forward = avance o carro.'),
  dict(cue='Você quer o combo em tamanho maior.', opts=['Super size it.', 'To go.', 'Drive-thru.'], ans=0, why='Super size it pede a versão maior.')])
