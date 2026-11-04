"""Bloco de verbos e expressões da aula 197: mini golf."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('hit', '🏌️', 'bater, acertar', ('hit', 'I hit the ball softly.', 'Eu bato na bola de leve.'), ('hits', 'Mia hits the ball.', 'A Mia bate na bola.'), ('hit', 'He hit it too hard.', 'Ele bateu forte demais.'), ('hitting', 'I am hitting the ball now.', 'Estou batendo na bola agora.'), 'Hit é igual no presente e no passado: hit, hit. Só mude o -s com ele ou ela.'),
  vb('win', '🏆', 'ganhar', ('win', 'We win a prize.', 'Nós ganhamos um prêmio.'), ('wins', 'Mia wins the game.', 'A Mia ganha o jogo.'), ('won', 'Dan won the first hole.', 'O Dan ganhou o primeiro buraco.'), ('winning', 'I am winning!', 'Estou ganhando!'), 'Win vira won no passado, e o -ing dobra o n: winning.'),
  vb('lose', '😅', 'perder', ('lose', 'I lose the ball.', 'Eu perco a bola.'), ('loses', 'Dan loses the game.', 'O Dan perde o jogo.'), ('lost', 'We lost the game.', 'Nós perdemos o jogo.'), ('losing', 'You are losing now.', 'Você está perdendo agora.'), 'Lose é perder um jogo ou um objeto. Passado: lost. Cuidado: loose é outra palavra.'),
  vb('play', '🎮', 'jogar', ('play', 'We play mini golf.', 'Nós jogamos mini golfe.'), ('plays', 'She plays well.', 'Ela joga bem.'), ('played', 'They played 18 holes.', 'Eles jogaram 18 buracos.'), ('playing', 'I am playing with Mia.', 'Estou jogando com a Mia.'), 'Em inglês se joga (play) golf, sem “o” ou “de”: play mini golf.'),
  vb('keep', '💰', 'ficar com, guardar', ('keep', 'I keep the receipt.', 'Eu guardo o recibo.'), ('keeps', 'Dan keeps the ball.', 'O Dan fica com a bola.'), ('kept', 'She kept the change.', 'Ela ficou com o troco.'), ('keeping', 'I am keeping score.', 'Estou marcando os pontos.'), 'Keep vira kept no passado. Keep the change = fique com o troco.')],
 verb_game=[
  dict(scene='Você quer que o atendente fique com o troco.', en='Please ___ the change.', opts=['keep', 'kept', 'keeps'], ans=0, pt='Por favor, fique com o troco.', why='Depois de please, use o verbo base: keep.'),
  dict(scene='A Mia ganhou o jogo ontem.', en='Mia ___ the game yesterday.', opts=['wins', 'won', 'winning'], ans=1, pt='A Mia ganhou o jogo ontem.', why='Yesterday pede passado: won.'),
  dict(scene='O Dan bate na bola agora.', en='Dan ___ the ball into the hole.', opts=['hit', 'hits', 'hitting'], ans=1, pt='O Dan bate a bola no buraco.', why='Com Dan (ele) no presente: hits.'),
  dict(scene='Vocês jogam mini golfe aos sábados.', en='We ___ mini golf on Saturdays.', opts=['play', 'plays', 'played'], ans=0, pt='Nós jogamos mini golfe aos sábados.', why='Com we no presente: play.')],
 expressions=[
  dict(en='Two for mini golf, please.', pt='Dois para mini golfe, por favor.', ex='Hi! Two for mini golf, please.', exp='Para comprar entrada para duas pessoas.', c='a'),
  dict(en='ten dollars each', pt='dez dólares cada', ex='It is ten dollars each.', exp='O preço é por pessoa.', c='b'),
  dict(en='Keep the change.', pt='Fique com o troco.', ex='Here’s twenty. Keep the change.', exp='Quando você não quer o troco.', c='c'),
  dict(en='Which color do you want?', pt='Qual cor você quer?', ex='Which color do you want? Red or blue?', exp='Para escolher uma bola ou taco.', c='d'),
  dict(en='How does it work?', pt='Como funciona?', ex='How does it work? I’m new.', exp='Para pedir as regras.', c='a'),
  dict(en='Your turn.', pt='Sua vez.', ex='Your turn, Mia!', exp='Para avisar que é a vez do outro jogar.', c='b')],
 expr_game=[
  dict(cue='Você quer entrar com mais uma pessoa.', opts=['Two for mini golf, please.', 'Keep the change.', 'Your turn.'], ans=0, why='Número + for + atividade + please.'),
  dict(cue='Você pagou vinte e não quer o troco.', opts=['How does it work?', 'Keep the change.', 'Which color do you want?'], ans=1, why='Keep the change dispensa o troco.'),
  dict(cue='Você não conhece as regras do jogo.', opts=['Your turn.', 'ten dollars each', 'How does it work?'], ans=2, why='How does it work? pede explicação.')])
