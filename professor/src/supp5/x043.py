"""Bloco extra · aula 43: Where is the bank?"""
X = dict(
 key=dict(big='Where is the bank?', label='Perguntar onde fica', sub='A pergunta básica para achar um lugar; responda com “It’s on…”, “It’s next to…” ou “It’s near…”.'),
 mini=[
  dict(who='Evan', en='Excuse me, where is the {bank|pharmacy|post office}?', pt='Com licença, onde fica o {banco|a farmácia|o correio}?'),
  dict(who='You', en='It’s on {Main Street|Oak Street|Park Street}.', pt='Fica na {Rua Principal|Rua Oak|Rua do Parque}.'),
  dict(who='Evan', en='Is it far from {here|the park|the station}?', pt='Fica longe {daqui|do parque|da estação}?'),
  dict(who='You', en='No, it’s {five|ten|two} minutes on foot.', pt='Não, é a {cinco|dez|dois} minutos a pé.')],
 dlg=[
  dict(who='Evan', en='Excuse me, where is the {bank|pharmacy|post office}?', pt='Com licença, onde fica {o banco|a farmácia|o correio}?'),
  dict(who='You', en='It’s on {Main Street|Oak Street|Park Street}.', pt='Fica na {Rua Principal|Rua Oak|Rua do Parque}.'),
  dict(who='Evan', en='Is it far from {here|the park|the station}?', pt='Fica longe {daqui|do parque|da estação}?'),
  dict(who='You', en='No, it’s {five|ten|two} minutes on foot.', pt='Não, é a {cinco|dez|dois} minutos a pé.'),
  dict(who='Evan', en='Is it {next to|across from|behind} the post office?', pt='Fica {ao lado do|em frente ao|atrás do} correio?'),
  dict(who='You', en='Yes, it’s {next to|across from|behind} it.', pt='Sim, fica {ao lado|em frente|atrás}.'),
  dict(who='Evan', en='Thank you so much!', pt='Muito obrigado!'),
  dict(who='You', en='You’re welcome. Have a {nice|great} day!', pt='De nada. Tenha um {bom|ótimo} dia!'),
  dict(who='Evan', en='Good luck! It’s {easy|simple|quick} to find.', pt='Boa sorte! É {fácil|simples|rápido} de achar.')],
 vocab=[
  dict(w='bank', pt='banco', e='🏦', ex=['The bank opens at nine.', 'I need to go to the bank.']),
  dict(w='pharmacy', pt='farmácia', e='💊', ex=['The pharmacy is near the park.', 'Is there a pharmacy here?']),
  dict(w='street', pt='rua', e='🛣️', ex=['The cafe is on Main Street.', 'This street is very quiet.']),
  dict(w='near', pt='perto', e='📍', ex=['My school is near my house.', 'Is the bank near here?']),
  dict(w='far', pt='longe', e='↔️', ex=['The airport is far from here.', 'It is not far.']),
  dict(w='next to', pt='ao lado de', e='🧱', ex=['The bank is next to the post office.', 'Sit next to me.'])],
 molds=[
  dict(title='Perguntar onde fica', frame='Excuse me, where is the {place}? Is it far from {dist}?', slots=[dict(key='place', opts=['bank', 'pharmacy', 'post office']), dict(key='dist', opts=['here', 'the park', 'the station'])], model='Excuse me, where is the bank? Is it far from here?', note='Comece com “Excuse me” para chamar a atenção com educação.'),
  dict(title='Dizer onde fica', frame='It’s {pos} the {landmark}, on {street}.', slots=[dict(key='pos', opts=['next to', 'across from', 'behind']), dict(key='landmark', opts=['post office', 'bank', 'pharmacy']), dict(key='street', opts=['Main Street', 'Oak Street', 'Park Street'])], model='It’s next to the post office, on Main Street.', note='Use “on” com nome de rua e uma referência para ajudar a achar.'),
  dict(title='Escrever uma resposta', frame='The {place} is {pos} the {landmark}. It’s {time} minutes on foot.', slots=[dict(key='place', opts=['bank', 'pharmacy', 'library']), dict(key='pos', opts=['near', 'next to', 'across from']), dict(key='landmark', opts=['park', 'post office', 'school']), dict(key='time', opts=['five', 'ten', 'two'])], model='The bank is near the park. It’s five minutes on foot.', note='Escreva a resposta completa, com lugar, referência e tempo a pé.')],
 sounds=[
  dict(say='Excuse me, where is the bank?', tag='acento: where is', tip='A voz sobe em “where” e desce no final. “is the” fica fraco e rápido.'),
  dict(say='It’s next to it.', tag='ligação: next to', tip='O “t” de “next” quase some e liga com “to”: “nexto”.'),
  dict(say='five minutes on foot', tag='ritmo: palavras fortes', tip='Bata “five”, “min-” e “foot”. O “on” é bem curto.')],
 role=dict(turns=[
  dict(npc='Excuse me, where is the bank?', opts=[
   dict(en='It’s on Main Street.', pt='Fica na Rua Principal.', reply='Is it far from here?'),
   dict(en='It’s on Oak Street, near the park.', pt='Fica na Rua Oak, perto do parque.', reply='Is it far from here?'),
   dict(en='It’s right there, on the corner.', pt='Fica ali mesmo, na esquina.', reply='Oh, is it far from here?')]),
  dict(npc=None, opts=[
   dict(en='No, it’s five minutes on foot.', pt='Não, é a cinco minutos a pé.', reply='Is it next to the post office?'),
   dict(en='No, it’s very close.', pt='Não, é bem perto.', reply='Great! Is it next to the post office?'),
   dict(en='A little. It’s ten minutes on foot.', pt='Um pouco. É a dez minutos a pé.', reply='OK. Is it next to the post office?')]),
  dict(npc=None, opts=[
   dict(en='Yes, it’s next to it.', pt='Sim, fica ao lado.', reply='Thank you so much!'),
   dict(en='Yes, it’s right next to the post office.', pt='Sim, fica bem ao lado do correio.', reply='Perfect. Thank you so much!'),
   dict(en='No, it’s across from the post office.', pt='Não, fica em frente ao correio.', reply='Oh, I see. Thank you so much!')]),
  dict(npc=None, opts=[
   dict(en='You’re welcome. Have a nice day!', pt='De nada. Tenha um bom dia!', reply='Thanks! I’ll find it. It’s easy!'),
   dict(en='No problem! Have a great day!', pt='Sem problema! Tenha um ótimo dia!', reply='You too! It’s easy to find.'),
   dict(en='My pleasure. Good luck!', pt='Imagina. Boa sorte!', reply='Thanks! It’s easy to find.')])],
  change=['A pessoa pergunta onde fica a farmácia em vez do banco.', 'Você não sabe: diga que não conhece e sugira perguntar a outra pessoa.', 'O lugar fica longe e a pessoa pergunta se há ônibus.']),
 writing=dict(task='Alguém pergunta onde fica um lugar perto de você. Escreva uma resposta curta: rua, referência e quanto tempo a pé.', model='The bank is on Main Street. It is next to the post office. It is five minutes on foot from here.', kw=['street', 'next', 'minutes', 'foot'], checks=['Disse em que rua fica o lugar.', 'Usei uma referência (next to, near, across from).', 'Disse a distância ou o tempo a pé.']),
 scenes=dict(pool=['street', 'bank', 'postoffice', 'pharmacy', 'park'], npc=dict(g='m', role='friend'), you=dict(g='f')),
 convo=dict(npc=dict(name='Evan'), turns=[
  dict(npc='Excuse me, where is the bank?', pt='Com licença, onde fica o banco?', opts=[
   dict(en='It’s on Main Street.', pt='Fica na Rua Principal.', ok=True, fb='Diz a rua onde o banco fica.'),
   dict(en='The bank is a big place.', pt='O banco é um lugar grande.', ok=False, fb='Descreve o banco, mas não diz onde ele fica.'),
   dict(en='Yes, I know the bank.', pt='Sim, eu conheço o banco.', ok=False, fb='A pergunta é “where”, não “do you know”.')]),
  dict(npc='Is it far from here?', pt='Fica longe daqui?', opts=[
   dict(en='I am far from here.', pt='Eu estou longe daqui.', ok=False, fb='O sujeito é o banco, não você.'),
   dict(en='No, it’s five minutes on foot.', pt='Não, é a cinco minutos a pé.', ok=True, fb='Responde à pergunta e dá o tempo.'),
   dict(en='It is a good bank.', pt='É um bom banco.', ok=False, fb='Não responde sobre a distância.')]),
  dict(npc='Is it next to the post office?', pt='Fica ao lado do correio?', opts=[
   dict(en='Yes, it’s next to it.', pt='Sim, fica ao lado.', ok=True, fb='Confirma a posição de forma curta.'),
   dict(en='Yes, I send a letter.', pt='Sim, eu mando uma carta.', ok=False, fb='Mudou de assunto; a pergunta é sobre a localização.'),
   dict(en='The post office is closed.', pt='O correio está fechado.', ok=False, fb='Pode até ser verdade, mas não responde.')]),
  dict(npc='Thank you so much!', pt='Muito obrigado!', opts=[
   dict(en='You’re welcome. Have a nice day!', pt='De nada. Tenha um bom dia!', ok=True, fb='Resposta natural a um agradecimento.'),
   dict(en='Nice to meet you!', pt='Prazer em conhecer!', ok=False, fb='Ele agradeceu; responda ao agradecimento.'),
   dict(en='Excuse me, where is the bank?', pt='Com licença, onde fica o banco?', ok=False, fb='Ele já perguntou isso; agora ele agradeceu.')]),
  dict(npc='Good luck! It’s easy to find.', pt='Boa sorte! É fácil de achar.', opts=[
   dict(en='Good luck with the bank!', pt='Boa sorte com o banco!', ok=False, fb='Estranho: ele que vai procurar, e a frase fica sem sentido.'),
   dict(en='Bye! See you around.', pt='Tchau! Até mais.', ok=True, fb='Despedida simpática.'),
   dict(en='Please, repeat the street.', pt='Por favor, repita a rua.', ok=False, fb='Não combina com “é fácil de achar”; ele já entendeu.')])]),
)
