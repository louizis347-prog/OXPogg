K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('clean', '🧼', 'limpar', ('clean', 'We clean the kitchen.', 'Nós limpamos a cozinha.'), ('cleans', 'Grace cleans the table.', 'A Grace limpa a mesa.'), ('cleaned', 'He cleaned the sink.', 'Ele limpou a pia.'), ('cleaning', 'I am cleaning my room.', 'Estou limpando meu quarto.'), 'Regular: clean, cleaned, cleaning.'),
  vb('vacuum', '🌀', 'passar aspirador', ('vacuum', 'I vacuum the rug.', 'Eu passo aspirador no tapete.'), ('vacuums', 'Finn vacuums the living room.', 'O Finn passa aspirador na sala.'), ('vacuumed', 'She vacuumed the stairs.', 'Ela passou aspirador nas escadas.'), ('vacuuming', 'I am vacuuming now.', 'Estou passando aspirador agora.'), 'Vacuum também é o aspirador, mas aqui é verbo: vacuum the rug.'),
  vb('sweep', '🧹', 'varrer', ('sweep', 'We sweep the floor.', 'Nós varremos o chão.'), ('sweeps', 'Grace sweeps the kitchen.', 'A Grace varre a cozinha.'), ('swept', 'He swept the porch.', 'Ele varreu a varanda.'), ('sweeping', 'I am sweeping the floor.', 'Estou varrendo o chão.'), 'Irregular: sweep, swept.'),
  vb('mop', '🪣', 'passar pano', ('mop', 'I mop the floor.', 'Eu passo pano no chão.'), ('mops', 'Finn mops the kitchen.', 'O Finn passa pano na cozinha.'), ('mopped', 'She mopped the bathroom.', 'Ela passou pano no banheiro.'), ('mopping', 'I am mopping the hall.', 'Estou passando pano no corredor.'), 'No passado e no -ing, dobre o p: mopped, mopping.'),
  vb('throw', '🗑️', 'jogar / jogar fora', ('throw', 'I throw the trash in the bin.', 'Eu jogo o lixo na lixeira.'), ('throws', 'Grace throws out the bag.', 'A Grace joga o saco fora.'), ('threw', 'He threw the box away.', 'Ele jogou a caixa fora.'), ('throwing', 'I am throwing out old papers.', 'Estou jogando papéis velhos fora.'), 'Irregular: throw, threw. Throw away / throw out = jogar fora.')],
 verb_game=[
  dict(scene='O Finn limpa o chão da sala com o aspirador.', en='Finn ___ the living room.', opts=['vacuum', 'vacuums', 'vacuuming'], ans=1, pt='O Finn passa aspirador na sala.', why='Com “Finn” (ele), o presente leva -s: vacuums.'),
  dict(scene='Ontem a Grace varreu a cozinha.', en='Yesterday Grace ___ the kitchen.', opts=['sweep', 'swept', 'sweeping'], ans=1, pt='Ontem a Grace varreu a cozinha.', why='“Yesterday” pede passado: swept.'),
  dict(scene='Agora você está passando pano no chão.', en='I am ___ the floor.', opts=['mop', 'mops', 'mopping'], ans=2, pt='Estou passando pano no chão.', why='“am” + verbo termina em -ing: mopping.'),
  dict(scene='Vocês limpam a casa no sábado.', en='We ___ the house on Saturday.', opts=['clean', 'cleans', 'cleaned'], ans=0, pt='Nós limpamos a casa no sábado.', why='Com “we” o presente fica na forma base: clean.')],
 expressions=[
  dict(en='Whose turn is it to…?', pt='De quem é a vez de…?', ex='Whose turn is it to wash the dishes?', exp='Para saber quem faz uma tarefa.', c='a'),
  dict(en='It\'s mine.', pt='É a minha.', ex='It\'s mine. I\'ll do it now.', exp='Para dizer que a vez é sua.', c='b'),
  dict(en='take out the trash', pt='levar o lixo para fora', ex='I\'ll take out the trash.', exp='Verbo frasal comum para a tarefa do lixo.', c='c'),
  dict(en='Can you… too?', pt='Pode… também?', ex='Can you clean the kitchen too?', exp='Para pedir mais uma ajuda, com educação.', c='d'),
  dict(en='We make a great team.', pt='Formamos um ótimo time.', ex='Look! We make a great team.', exp='Para elogiar o trabalho em dupla.', c='a'),
  dict(en='Thanks for helping out!', pt='Valeu pela ajuda!', ex='Thanks for helping out today!', exp='Para agradecer por ajudar nas tarefas.', c='b')],
 expr_game=[
  dict(cue='Você quer saber de quem é a vez de lavar a louça.', opts=['Whose turn is it to wash the dishes?', 'We make a great team.', 'Thanks for helping out!'], ans=0, why='Whose turn is it to…? pergunta a vez.'),
  dict(cue='É a sua vez e você quer dizer isso.', opts=['It\'s mine. I\'ll do it now.', 'Can you clean it too?', 'Whose turn is it?'], ans=0, why='It\'s mine diz que a tarefa é sua.'),
  dict(cue='Vocês terminaram e você quer elogiar a parceria.', opts=['Take out the trash.', 'We make a great team.', 'Whose turn is it?'], ans=1, why='We make a great team elogia o trabalho em dupla.')])
