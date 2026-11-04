"""Bloco de verbos e expressões da aula 157: basquete no parque."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('shoot', '🎯', 'arremessar', ('shoot', 'I shoot from here.', 'Eu arremesso daqui.'), ('shoots', 'Kai shoots well.', 'O Kai arremessa bem.'), ('shot', 'He shot the ball twice.', 'Ele arremessou a bola duas vezes.'), ('shooting', 'She is shooting now.', 'Ela está arremessando agora.'), 'Passado irregular: shoot vira shot (o mesmo da palavra “cesta”).'),
  vb('run', '🏃', 'correr', ('run', 'We run on the court.', 'Nós corremos na quadra.'), ('runs', 'Finn runs fast.', 'O Finn corre rápido.'), ('ran', 'I ran to the ball.', 'Eu corri até a bola.'), ('running', 'They are running now.', 'Eles estão correndo agora.'), 'Passado irregular: run vira ran. Em -ing, dobra o n: running.'),
  vb('catch', '🤲', 'pegar / agarrar', ('catch', 'I catch the ball.', 'Eu pego a bola.'), ('catches', 'Kai catches the pass.', 'O Kai pega o passe.'), ('caught', 'She caught the ball.', 'Ela pegou a bola.'), ('catching', 'He is catching the pass.', 'Ele está pegando o passe.'), 'Passado irregular: catch vira caught. Com ele/ela: catches.'),
  vb('win', '🏆', 'ganhar (um jogo)', ('win', 'We win the game.', 'Nós ganhamos o jogo.'), ('wins', 'The blue team wins.', 'O time azul ganha.'), ('won', 'We won last week.', 'Nós ganhamos semana passada.'), ('winning', 'We are winning now.', 'Estamos ganhando agora.'), 'Win é ganhar um jogo; ganhar dinheiro é earn. Passado: won.'),
  vb('jump', '⬆️', 'pular', ('jump', 'I jump and shoot.', 'Eu pulo e arremesso.'), ('jumps', 'Kai jumps high.', 'O Kai pula alto.'), ('jumped', 'He jumped for the ball.', 'Ele pulou para pegar a bola.'), ('jumping', 'I am jumping now.', 'Estou pulando agora.'), 'Jump é regular: só acrescente -ed no passado.')],
 verb_game=[
  dict(scene='Toda semana o Kai arremessa bem.', en='Kai ___ well every week.', opts=['shoot', 'shoots', 'shot'], ans=1, pt='O Kai arremessa bem toda semana.', why='Com “Kai” (ele), o presente leva -s: shoots.'),
  dict(scene='Semana passada vocês ganharam.', en='We ___ last week.', opts=['win', 'wins', 'won'], ans=2, pt='Nós ganhamos semana passada.', why='“Last week” pede passado: won.'),
  dict(scene='Agora o Finn está correndo.', en='Finn is ___ to the ball.', opts=['run', 'runs', 'running'], ans=2, pt='O Finn está correndo até a bola.', why='“is” + verbo termina em -ing: running.'),
  dict(scene='Ontem a Ana pegou o passe.', en='Yesterday Ana ___ the pass.', opts=['catch', 'caught', 'catching'], ans=1, pt='Ontem a Ana pegou o passe.', why='“Yesterday” pede passado: caught.')],
 expressions=[
  dict(en='Nice shot!', pt='Bela cesta!', ex='Nice shot! That is two points.', exp='Para elogiar um arremesso ou uma jogada.', c='a'),
  dict(en='Pass it to me!', pt='Passe para mim!', ex='I’m open! Pass it to me!', exp='Para pedir a bola durante o jogo.', c='b'),
  dict(en='I’m open!', pt='Estou livre!', ex='I’m open! Here!', exp='Para avisar que ninguém está marcando você.', c='c'),
  dict(en='Which team am I on?', pt='Em que time estou?', ex='Which team am I on? Blue or red?', exp='Para saber de que lado jogar.', c='d'),
  dict(en='We need one more.', pt='Falta mais um.', ex='We need one more. Do you want to play?', exp='Para dizer que falta um jogador.', c='a'),
  dict(en='Good game!', pt='Bom jogo!', ex='Good game! See you next week.', exp='Despedida simpática no fim da partida.', c='b')],
 expr_game=[
  dict(cue='Você está livre perto da cesta e quer receber a bola.', opts=['Pass it to me!', 'Good game!', 'We need one more.'], ans=0, why='Pass it to me! pede a bola.'),
  dict(cue='O jogo acabou e você quer se despedir com simpatia.', opts=['Which team am I on?', 'Good game!', 'I’m open!'], ans=1, why='Good game! encerra a partida com educação.'),
  dict(cue='Seu amigo fez uma cesta bonita.', opts=['Nice shot!', 'We need one more.', 'Which team am I on?'], ans=0, why='Nice shot! elogia o arremesso.')])
