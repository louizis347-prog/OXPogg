"""Bloco de verbos e expressões da aula 059: é longe?"""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('walk', '🚶', 'andar / caminhar', ('walk', 'We walk to the lake.', 'Nós caminhamos até o lago.'), ('walks', 'Evan walks to the park.', 'O Evan caminha até o parque.'), ('walked', 'I walked ten minutes.', 'Eu caminhei dez minutos.'), ('walking', 'I am walking to the lake.', 'Estou caminhando até o lago.'), 'Walk é regular. O l é mudo: “uók”.'),
  vb('ride', '🚲', 'andar de (bicicleta)', ('ride', 'I ride my bike.', 'Eu ando de bicicleta.'), ('rides', 'She rides to the lake.', 'Ela vai de bicicleta até o lago.'), ('rode', 'He rode a bike yesterday.', 'Ele andou de bicicleta ontem.'), ('riding', 'I am riding my bike.', 'Estou andando de bicicleta.'), 'Ride vira rode no passado (irregular). O -ing perde o e: riding.'),
  vb('see', '👀', 'ver', ('see', 'We see many trees.', 'Nós vemos muitas árvores.'), ('sees', 'Evan sees the lake.', 'O Evan vê o lago.'), ('saw', 'I saw many bikes.', 'Eu vi muitas bicicletas.'), ('seeing', 'We are seeing the lake today.', 'Vamos ver o lago hoje.'), 'See vira saw no passado (irregular).'),
  vb('rest', '🛋️', 'descansar', ('rest', 'I rest on a bench.', 'Eu descanso num banco.'), ('rests', 'He rests under a tree.', 'Ele descansa debaixo de uma árvore.'), ('rested', 'We rested for ten minutes.', 'Nós descansamos por dez minutos.'), ('resting', 'I am resting now.', 'Estou descansando agora.'), 'Rest é regular: rests, rested, resting.'),
  vb('run', '🏃', 'correr', ('run', 'They run by the lake.', 'Eles correm perto do lago.'), ('runs', 'She runs every morning.', 'Ela corre toda manhã.'), ('ran', 'I ran to the bus.', 'Eu corri até o ônibus.'), ('running', 'I am running to the park.', 'Estou correndo até o parque.'), 'Run vira ran no passado. No -ing dobra o n: running.')],
 verb_game=[
  dict(scene='O Evan caminha até o lago.', en='Evan ___ to the lake.', opts=['walk', 'walks', 'walking'], ans=1, pt='O Evan caminha até o lago.', why='Com “Evan” (ele) o presente leva -s: walks.'),
  dict(scene='Ontem você viu muitas árvores.', en='Yesterday I ___ many trees.', opts=['see', 'sees', 'saw'], ans=2, pt='Ontem eu vi muitas árvores.', why='“Yesterday” pede passado: saw.'),
  dict(scene='Agora você anda de bicicleta.', en='I am ___ my bike.', opts=['ride', 'rode', 'riding'], ans=2, pt='Estou andando de bicicleta.', why='“am” + -ing: riding.'),
  dict(scene='Ontem ela correu até o parque.', en='Yesterday she ___ to the park.', opts=['run', 'ran', 'runs'], ans=1, pt='Ontem ela correu até o parque.', why='Passado irregular de run: ran.')],
 expressions=[
  dict(en='Is it far from here?', pt='Fica longe daqui?', ex='Excuse me, is it far from here?', exp='Para perguntar a distância.', c='a'),
  dict(en='Not really.', pt='Nem tanto.', ex='Not really. It’s close.', exp='Para dizer que não é muito.', c='b'),
  dict(en='ten minutes on foot', pt='dez minutos a pé', ex='It’s ten minutes on foot.', exp='Para dizer o tempo andando.', c='c'),
  dict(en='Can I walk there?', pt='Posso ir a pé?', ex='Can I walk there?', exp='Para saber se dá para ir andando.', c='d'),
  dict(en='It’s a nice walk.', pt='É um passeio agradável.', ex='It’s a nice walk by the lake.', exp='Para dizer que o caminho é bom.', c='a'),
  dict(en='Enjoy your walk!', pt='Aproveite a caminhada!', ex='Thanks! Enjoy your walk!', exp='Para se despedir de quem vai andar.', c='b')],
 expr_game=[
  dict(cue='Você quer saber se o lago é longe.', opts=['Is it far from here?', 'Enjoy your walk!', 'Not really.'], ans=0, why='Far from here = longe daqui.'),
  dict(cue='Você quer dizer que o lago está a dez minutos andando.', opts=['It’s ten minutes on foot.', 'Can I walk there?', 'It’s a nice walk.'], ans=0, why='On foot = a pé.'),
  dict(cue='Você quer saber se pode ir andando.', opts=['Can I walk there?', 'Not really.', 'Enjoy your walk!'], ans=0, why='Can I walk there? pergunta se dá para ir a pé.')])
