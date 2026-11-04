"""Bloco de verbos e expressões da aula 195: noite de boliche."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('roll', '🎳', 'rolar', ('roll', 'I roll the ball.', 'Eu rolo a bola.'), ('rolls', 'Maya rolls the ball.', 'A Maya rola a bola.'), ('rolled', 'He rolled a strike.', 'Ele fez um strike.'), ('rolling', 'She is rolling the blue ball.', 'Ela está rolando a bola azul.'), 'Roll a ball = rolar/lançar a bola no boliche. Passado regular: rolled.'),
  vb('win', '🏆', 'ganhar', ('win', 'We win the game.', 'Nós ganhamos o jogo.'), ('wins', 'Maya wins the game.', 'A Maya ganha o jogo.'), ('won', 'Leo won the first game.', 'O Leo ganhou o primeiro jogo.'), ('winning', 'Ana is winning now.', 'A Ana está ganhando agora.'), 'Win é irregular: won. Win = ganhar um jogo (não um presente).'),
  vb('lose', '😅', 'perder', ('lose', 'I lose the game.', 'Eu perco o jogo.'), ('loses', 'Leo loses again.', 'O Leo perde de novo.'), ('lost', 'We lost by two points.', 'Nós perdemos por dois pontos.'), ('losing', 'I am losing now.', 'Estou perdendo agora.'), 'Lose é irregular: lost. O e cai antes de -ing: losing.'),
  vb('clap', '👏', 'bater palmas', ('clap', 'We clap for Maya.', 'Nós batemos palmas para a Maya.'), ('claps', 'Leo claps loudly.', 'O Leo bate palmas alto.'), ('clapped', 'They clapped for him.', 'Eles bateram palmas para ele.'), ('clapping', 'Everyone is clapping.', 'Todo mundo está batendo palmas.'), 'Clap dobra o p antes de -ed e -ing: clapped, clapping.'),
  vb('laugh', '😂', 'rir', ('laugh', 'We laugh a lot.', 'Nós rimos muito.'), ('laughs', 'Leo laughs at himself.', 'O Leo ri de si mesmo.'), ('laughed', 'They laughed together.', 'Eles riram juntos.'), ('laughing', 'She is laughing.', 'Ela está rindo.'), 'Laugh soa “laf”: o gh vira f. Passado regular: laughed.')],
 verb_game=[
  dict(scene='No primeiro jogo, o Leo ganhou.', en='Leo ___ the first game.', opts=['win', 'won', 'winning'], ans=1, pt='O Leo ganhou o primeiro jogo.', why='Passado irregular de win: won.'),
  dict(scene='Agora todo mundo está batendo palmas.', en='Everyone is ___.', opts=['clap', 'claps', 'clapping'], ans=2, pt='Todo mundo está batendo palmas.', why='“is” + verbo termina em -ing: clapping.'),
  dict(scene='A Maya rola a bola azul.', en='Maya ___ the blue ball.', opts=['roll', 'rolls', 'rolled'], ans=1, pt='A Maya rola a bola azul.', why='Com “Maya” (ela), o presente leva -s: rolls.'),
  dict(scene='Nós rimos muito no boliche.', en='We ___ a lot at the alley.', opts=['laugh', 'laughs', 'laughed'], ans=0, pt='Nós rimos muito na pista.', why='Com “we”, o presente fica na forma base: laugh.')],
 expressions=[
  dict(en='How many players?', pt='Quantos jogadores?', ex='Welcome! How many players?', exp='Pergunta do atendente ao receber o grupo.', c='a'),
  dict(en='Here you go.', pt='Aqui está.', ex='Here you go. Lane six.', exp='Para entregar algo a alguém.', c='b'),
  dict(en='Who goes first?', pt='Quem começa?', ex='Okay. Who goes first?', exp='Para saber quem joga primeiro.', c='c'),
  dict(en='Ladies first!', pt='As damas primeiro!', ex='Ladies first! Go, Maya.', exp='Frase tradicional para dar a vez às mulheres, dita com simpatia.', c='d'),
  dict(en='Your turn!', pt='Sua vez!', ex='It’s your turn, Leo!', exp='Para avisar quem joga agora.', c='a'),
  dict(en='Nice shot!', pt='Boa jogada!', ex='Nice shot, Ana!', exp='Para elogiar uma jogada.', c='b')],
 expr_game=[
  dict(cue='Você quer saber quem joga primeiro.', opts=['Who goes first?', 'Nice shot!', 'Here you go.'], ans=0, why='Who goes first? pergunta quem começa.'),
  dict(cue='O atendente entrega os sapatos.', opts=['How many players?', 'Here you go.', 'Your turn!'], ans=1, why='Here you go = aqui está.'),
  dict(cue='Seu amigo faz uma boa jogada.', opts=['Nice shot!', 'Who goes first?', 'How many players?'], ans=0, why='Nice shot! elogia a jogada.')])
