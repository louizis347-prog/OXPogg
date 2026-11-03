X = dict(
key=dict(big='I like… / I don\'t like…', label='Dizer o que você gosta', sub='Responda Do you like…? com Yes, I do. ou No, I don\'t. e acrescente I like…'),
mini=[
 dict(who='Malik', en='Do you like {coffee|tea|juice}?', pt='Você gosta de {café|chá|suco}?'),
 dict(who='You', en='Yes, I do. I like it with {milk|sugar|ice}.', pt='Gosto. Gosto {com leite|com açúcar|com gelo}.'),
 dict(who='Malik', en='What do you like for {breakfast|lunch|dinner}?', pt='O que você gosta {no café da manhã|no almoço|no jantar}?'),
 dict(who='You', en='I like {eggs|fruit|cereal} and toast.', pt='Gosto de {ovos|fruta|cereal} e torrada.'),
],
dlg=[
 dict(who='Malik', en='Do you like {coffee|tea|juice}?', pt='Você gosta de {café|chá|suco}?'),
 dict(who='You', en='Yes, I do. I like it with {milk|sugar|ice}.', pt='Gosto. Gosto {com leite|com açúcar|com gelo}.'),
 dict(who='Malik', en='Do you like {tea|juice|water}?', pt='Você gosta de {chá|suco|água}?'),
 dict(who='You', en='No, I don\'t. I like {coffee|juice|milk}.', pt='Não. Eu gosto de {café|suco|leite}.'),
 dict(who='Malik', en='What do you like for {breakfast|lunch|dinner}?', pt='O que você gosta {no café da manhã|no almoço|no jantar}?'),
 dict(who='You', en='I like {eggs|toast|fruit} and toast.', pt='Gosto de {ovos|torrada|fruta} e torrada.'),
 dict(who='Malik', en='Me too! I love {eggs|toast|fruit}.', pt='Eu também! Adoro {ovos|torrada|fruta}.'),
 dict(who='You', en='Let\'s have {breakfast|lunch|dinner} together.', pt='Vamos {tomar café da manhã|almoçar|jantar} juntos.'),
 dict(who='Malik', en='See you at {breakfast|lunch|dinner}!', pt='Até {o café da manhã|o almoço|o jantar}!'),
],
vocab=[
 dict(w='like', pt='gostar', e='👍', ex=['I like coffee.', 'Do you like eggs?']),
 dict(w='love', pt='amar, adorar', e='❤️', ex=['I love toast.', 'Malik loves eggs.']),
 dict(w='eggs', pt='ovos', e='🥚', ex=['I like eggs for breakfast.', 'We have eggs and toast.']),
 dict(w='milk', pt='leite', e='🥛', ex=['I like coffee with milk.', 'The milk is cold.']),
 dict(w='toast', pt='torrada', e='🍞', ex=['I eat toast every morning.', 'Eggs and toast, please.']),
 dict(w='breakfast', pt='café da manhã', e='🍳', ex=['What do you like for breakfast?', 'Breakfast is at eight.']),
],
molds=[
 dict(title='Perguntar o que a pessoa gosta', frame='Do you like {thing}? Yes, I {ans}.', slots=[dict(key='thing', opts=['coffee', 'tea', 'eggs']), dict(key='ans', opts=['do', 'really do', 'do, a lot'])], model='Do you like coffee? Yes, I do.', note='Resposta curta: Yes, I do. / No, I don\'t. Repetir o verbo like não é preciso.'),
 dict(title='Dizer o que gosta', frame='I like {thing} for {meal}.', slots=[dict(key='thing', opts=['eggs', 'toast', 'fruit']), dict(key='meal', opts=['breakfast', 'lunch', 'dinner'])], model='I like eggs for breakfast.', note='For + refeição diz para quando é: for breakfast.'),
 dict(title='Escrever sobre gostos', frame='I like {a}. I don\'t like {b}. I love {c}!', slots=[dict(key='a', opts=['coffee', 'milk', 'toast']), dict(key='b', opts=['tea', 'juice', 'eggs']), dict(key='c', opts=['pizza', 'fruit', 'music'])], model='I like coffee. I don\'t like tea. I love pizza!', note='Like para gostar, don\'t like para não gostar, love para gostar muito.'),
],
sounds=[
 dict(say='Do you like coffee?', tag='ligação: do you', tip='Do you soa "du-yu", ou até "ju". A voz sobe no fim, em COF-fee.'),
 dict(say='No, I don\'t.', tag='acento: don\'t', tip='Don\'t é forte: "dont". Fale com uma pausa curta depois de No.'),
 dict(say='I like it with milk.', tag='ligação: like it', tip='Like it liga: "lai-kit". Com e milk têm o th fraco e o l final claro.'),
],
role=dict(turns=[
 dict(npc='Do you like coffee?', opts=[
  dict(en='Yes, I do. I like it with milk.', pt='Gosto. Gosto com leite.', reply='Me too! Do you like tea?'),
  dict(en='Yes, I love it! I like it with sugar.', pt='Adoro! Gosto com açúcar.', reply='Me too! Do you like tea?'),
  dict(en='Yes, I do. Every morning!', pt='Gosto. Toda manhã!', reply='Me too! Do you like tea?')]),
 dict(npc='Do you like tea?', opts=[
  dict(en='No, I don\'t. I like coffee.', pt='Não. Eu gosto de café.', reply='OK! What do you like for breakfast?'),
  dict(en='Not really. I like juice.', pt='Nem tanto. Eu gosto de suco.', reply='OK! What do you like for breakfast?'),
  dict(en='Yes, I do. But I like coffee more.', pt='Gosto. Mas gosto mais de café.', reply='OK! What do you like for breakfast?')]),
 dict(npc='What do you like for breakfast?', opts=[
  dict(en='I like eggs and toast.', pt='Gosto de ovos e torrada.', reply='Me too! I love eggs.'),
  dict(en='I like fruit and milk.', pt='Gosto de fruta e leite.', reply='Nice! I like fruit too.'),
  dict(en='I like toast with coffee.', pt='Gosto de torrada com café.', reply='Me too! I love toast.')]),
 dict(npc='Let\'s have breakfast together!', opts=[
  dict(en='Great idea! See you at breakfast.', pt='Ótima ideia! Até o café da manhã.', reply='See you at breakfast!'),
  dict(en='Sure! At eight?', pt='Claro! Às oito?', reply='Yes, at eight. See you!'),
  dict(en='Yes, let\'s! Where?', pt='Vamos! Onde?', reply='At my place. See you at breakfast!')]),
], change=['Malik diz que não gosta de ovos; reaja e sugira outra comida.', 'Você tem alergia a leite e explica com educação.', 'Malik pergunta o que você gosta no jantar.']),
writing=dict(task='Escreva 2 ou 3 frases sobre o que você gosta e não gosta de comer no café da manhã.', model='I like coffee with milk. I don\'t like tea. For breakfast, I like eggs and toast.', kw=['like', 'coffee', 'breakfast', 'eggs'], checks=['Usou I like…', 'Usou I don\'t like…', 'Citou pelo menos duas comidas ou bebidas.']),
scenes=dict(pool=['cafe', 'cafe2', 'kitchen', 'diner', 'bakery'], npc=dict(g='m', role='friend'), you=dict(g='f')),
convo=dict(npc=dict(name='Malik'), story='Você toma café com o vizinho Malik e fala sobre o que gosta de comer e beber.', turns=[
 dict(npc='Do you like coffee?', pt='Você gosta de café?', opts=[
  dict(en='Yes, I do. I like it with milk.', pt='Gosto. Gosto com leite.', ok=True, fb='Resposta curta e um detalhe.'),
  dict(en='Yes, I like.', pt='Sim, eu gosto.', ok=False, fb='Na resposta curta use do: Yes, I do. Ou diga I like it.'),
  dict(en='I am coffee.', pt='Eu sou café.', ok=False, fb='Gostar é like, não to be.')]),
 dict(npc='Do you like tea?', pt='Você gosta de chá?', opts=[
  dict(en='No, I don\'t. I like coffee.', pt='Não. Eu gosto de café.', ok=True, fb='Nega e diz sua preferência.'),
  dict(en='No, I not like.', pt='Não, eu não gosto (errado).', ok=False, fb='Use don\'t: No, I don\'t. / I don\'t like tea.'),
  dict(en='Yes, please.', pt='Sim, por favor.', ok=False, fb='Please aparece quando se pede algo, não ao responder do que gosta.')]),
 dict(npc='What do you like for breakfast?', pt='O que você gosta no café da manhã?', opts=[
  dict(en='Yes, I like breakfast.', pt='Sim, eu gosto de café da manhã.', ok=False, fb='What pede comidas, não sim ou não.'),
  dict(en='I like breakfast at eight.', pt='Gosto de café da manhã às oito.', ok=False, fb='Malik quer saber quais comidas; a hora é outra pergunta.'),
  dict(en='I like eggs and toast.', pt='Gosto de ovos e torrada.', ok=True, fb='Lista duas comidas com and.')]),
 dict(npc='Me too! I love eggs.', pt='Eu também! Adoro ovos.', opts=[
  dict(en='Let\'s have breakfast together.', pt='Vamos tomar café da manhã juntos.', ok=True, fb='Sugere um plano com Let\'s.'),
  dict(en='I don\'t like eggs.', pt='Não gosto de ovos.', ok=False, fb='Contradiz o que você acabou de dizer.'),
  dict(en='Do you like tea?', pt='Você gosta de chá?', ok=False, fb='Essa pergunta já foi feita.')]),
 dict(npc='See you at breakfast!', pt='Até o café da manhã!', opts=[
  dict(en='See you! Bye!', pt='Até! Tchau!', ok=True, fb='Despedida natural.'),
  dict(en='Yes, I do.', pt='Sim, gosto.', ok=False, fb='Ele não fez pergunta; é uma despedida.'),
  dict(en='What do you like?', pt='O que você gosta?', ok=False, fb='A conversa está terminando.')]),
]),
)
