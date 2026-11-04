"""Bloco extra · aula 44: Turn left, turn right."""
X = dict(
 key=dict(big='Turn left at the light', label='Dar direções', sub='Direções simples: siga em frente, vire e diga de que lado o lugar fica.'),
 mini=[
  dict(who='Grace', en='Excuse me, how do I get to the {museum|library|park}?', pt='Com licença, como chego {ao museu|à biblioteca|ao parque}?'),
  dict(who='You', en='Go straight for {two|three|four} blocks.', pt='Siga em frente por {dois|três|quatro} quarteirões.'),
  dict(who='You', en='Turn {left|right} at the traffic light.', pt='Vire à {esquerda|direita} no semáforo.'),
  dict(who='You', en='It’s on your {right|left}.', pt='Fica à sua {direita|esquerda}.')],
 dlg=[
  dict(who='Grace', en='Excuse me, how do I get to the {museum|library|park}?', pt='Com licença, como chego {ao museu|à biblioteca|ao parque}?'),
  dict(who='You', en='Go straight for {two|three|four} blocks.', pt='Siga em frente por {dois|três|quatro} quarteirões.'),
  dict(who='Grace', en='Then?', pt='Depois?'),
  dict(who='You', en='Turn {left|right} at the traffic light.', pt='Vire à {esquerda|direita} no semáforo.'),
  dict(who='Grace', en='And then?', pt='E depois?'),
  dict(who='You', en='Walk one more block. It’s on your {right|left}.', pt='Ande mais um quarteirão. Fica à sua {direita|esquerda}.'),
  dict(who='Grace', en='Is it a {big|small|tall} building?', pt='É um prédio {grande|pequeno|alto}?'),
  dict(who='You', en='Yes, with a {red|blue|green} door.', pt='Sim, com uma porta {vermelha|azul|verde}.'),
  dict(who='Grace', en='Good luck! You can’t miss it.', pt='Boa sorte! Não tem como errar.')],
 vocab=[
  dict(w='straight', pt='em frente', e='⬆️', ex=['Go straight on this street.', 'Keep going straight.']),
  dict(w='turn', pt='virar', e='↪️', ex=['Turn left at the corner.', 'Turn right here.']),
  dict(w='corner', pt='esquina', e='📐', ex=['The cafe is on the corner.', 'Wait for me at the corner.']),
  dict(w='block', pt='quarteirão', e='🏘️', ex=['Walk two blocks.', 'The bank is one block away.']),
  dict(w='light', pt='semáforo', e='🚦', ex=['Turn left at the light.', 'The light is red.']),
 dict(w='hospital', pt='hospital', e='🏥', ex=['The hospital is on the corner.', 'The hospital is near.'])],
 molds=[
  dict(title='Pedir direções', frame='Excuse me, how do I get to the {place}?', slots=[dict(key='place', opts=['museum', 'library', 'park', 'station'])], model='Excuse me, how do I get to the museum?', note='“How do I get to…?” é o jeito comum de pedir um caminho.'),
  dict(title='Dar o caminho', frame='Go straight for {n} blocks. {act} at the {mark}.', slots=[dict(key='n', opts=['two', 'three', 'four']), dict(key='act', opts=['Turn left', 'Turn right', 'Stop']), dict(key='mark', opts=['traffic light', 'corner', 'bank'])], model='Go straight for two blocks. Turn left at the traffic light.', note='Fale em passos curtos: uma instrução por frase.'),
  dict(title='Escrever onde fica', frame='It’s {side}. It’s a {size} building with a {color} door.', slots=[dict(key='side', opts=['on your right', 'on your left', 'on the corner']), dict(key='size', opts=['big', 'small', 'tall']), dict(key='color', opts=['red', 'blue', 'green'])], model='It’s on your right. It’s a big building with a red door.', note='Termine com o lado e um detalhe fácil de ver.')],
 sounds=[
  dict(say='Turn left at the light.', tag='ligação: turn left', tip='O “n” de “turn” e o “l” de “left” ficam juntos. “At the” é fraco e rápido.'),
  dict(say='Go straight for two blocks.', tag='ritmo: palavras fortes', tip='Marque “go”, “straight” e “blocks”. As outras palavras são curtas.'),
  dict(say='You can’t miss it.', tag='acento: can’t', tip='“Can’t” soa forte e longo; “can” afirmativo é fraco. Aqui a voz cai em “miss”.')],
 role=dict(turns=[
  dict(npc='Excuse me, how do I get to the museum?', opts=[
   dict(en='Go straight for two blocks.', pt='Siga em frente por dois quarteirões.', reply='OK, two blocks. Then?'),
   dict(en='Walk straight for three blocks.', pt='Ande em frente por três quarteirões.', reply='Three blocks, OK. Then?'),
   dict(en='Go straight. It’s one block.', pt='Siga em frente. É um quarteirão.', reply='One block, OK. Then?')]),
  dict(npc=None, opts=[
   dict(en='Turn left at the traffic light.', pt='Vire à esquerda no semáforo.', reply='Left at the light. And then?'),
   dict(en='Turn right at the corner.', pt='Vire à direita na esquina.', reply='Right at the corner. And then?'),
   dict(en='Turn left at the bank.', pt='Vire à esquerda no banco.', reply='Left at the bank. And then?')]),
  dict(npc=None, opts=[
   dict(en='Walk one more block. It’s on your right.', pt='Ande mais um quarteirão. Fica à sua direita.', reply='On my right. Is it a big building?'),
   dict(en='Walk two more blocks. It’s on your left.', pt='Ande mais dois quarteirões. Fica à sua esquerda.', reply='On my left. Is it a big building?'),
   dict(en='Walk one block. It’s across from the park.', pt='Ande um quarteirão. Fica em frente ao parque.', reply='Across from the park. Is it a big building?')]),
  dict(npc=None, opts=[
   dict(en='Yes, with a red door.', pt='Sim, com uma porta vermelha.', reply='Great, thank you! Good luck to me!'),
   dict(en='Yes, it’s a big white building.', pt='Sim, é um prédio branco grande.', reply='White and big. I can’t miss it. Thanks!'),
   dict(en='It’s big, with a flag in front.', pt='É grande, com uma bandeira na frente.', reply='A flag, great. Thanks a lot!')])],
  change=['A pessoa não entende “block”; explique de outro jeito.', 'Você erra o lado e precisa corrigir: “Sorry, turn right!”', 'O semáforo está quebrado; mude a referência para outra esquina.']),
 writing=dict(task='Escreva o caminho da sua casa até um lugar próximo (padaria, escola ou parque) em 3 passos curtos.', model='Go straight for two blocks. Turn left at the corner. The park is on your right.', kw=['straight', 'turn', 'block', 'left'], checks=['Usei pelo menos um verbo de direção (go, turn, walk).', 'Disse esquerda ou direita corretamente.', 'Terminei dizendo onde o lugar fica.']),
 scenes=dict(pool=['street', 'park', 'museum', 'bank', 'bookshop'], npc=dict(g='f', role='friend'), you=dict(g='m')),
 convo=dict(npc=dict(name='Grace'), turns=[
  dict(npc='Excuse me, how do I get to the museum?', pt='Com licença, como chego ao museu?', opts=[
   dict(en='I am not a museum.', pt='Eu não sou um museu.', ok=False, fb='Confunde a pergunta; ela quer o caminho.'),
   dict(en='The museum is very old.', pt='O museu é muito antigo.', ok=False, fb='Fala do museu, mas não ajuda a chegar.'),
   dict(en='Go straight for two blocks.', pt='Siga em frente por dois quarteirões.', ok=True, fb='Primeiro passo claro do caminho.')]),
  dict(npc='Then?', pt='Depois?', opts=[
   dict(en='Turn left at the traffic light.', pt='Vire à esquerda no semáforo.', ok=True, fb='Segundo passo: virar num ponto de referência.'),
   dict(en='Then, thank you.', pt='Depois, obrigado.', ok=False, fb='Ela ainda precisa do próximo passo.'),
   dict(en='You are welcome.', pt='De nada.', ok=False, fb='Ela ainda não agradeceu.')]),
  dict(npc='And then?', pt='E depois?', opts=[
   dict(en='Turn the right door.', pt='Vire a porta direita.', ok=False, fb='Frase confusa; use “It’s on your right.”'),
   dict(en='Go back to the light.', pt='Volte ao semáforo.', ok=False, fb='Ela acabou de passar ali; falta o final do caminho.'),
   dict(en='Walk one more block. It’s on your right.', pt='Ande mais um quarteirão. Fica à sua direita.', ok=True, fb='Fecha o caminho com o lado do lugar.')]),
  dict(npc='Is it a big building?', pt='É um prédio grande?', opts=[
   dict(en='Yes, with a red door.', pt='Sim, com uma porta vermelha.', ok=True, fb='Confirma e dá um detalhe visual.'),
   dict(en='Yes, I walk every day.', pt='Sim, eu caminho todo dia.', ok=False, fb='Não responde sobre o prédio.'),
   dict(en='No, the light is red.', pt='Não, o semáforo é vermelho.', ok=False, fb='Mistura o semáforo com o prédio.')]),
  dict(npc='Good luck! You can’t miss it.', pt='Boa sorte! Não tem como errar.', opts=[
   dict(en='Please, miss it.', pt='Por favor, perca.', ok=False, fb='Frase estranha; “miss” aqui significa não ver.'),
   dict(en='Thanks a lot! Bye!', pt='Muito obrigada! Tchau!', ok=False, fb='Quem recebeu ajuda foi ela; você não precisa agradecer.'),
   dict(en='Bye! Have a nice walk!', pt='Tchau! Boa caminhada!', ok=True, fb='Despedida simpática para quem vai andar.')])]),
)
