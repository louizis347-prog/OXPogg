"""Bloco extra · aula 45: Taking the subway."""
X = dict(
 key=dict(big='Which train goes to…?', label='Escolher o trem', sub='Pergunta útil na estação: qual trem, qual plataforma e quantas paradas até o seu destino.'),
 mini=[
  dict(who='Ravi', en='Excuse me, which train goes to {Brooklyn|downtown|the airport}?', pt='Com licença, qual trem vai {ao Brooklyn|ao centro|ao aeroporto}?'),
  dict(who='You', en='Take the number {two|four|six} train.', pt='Pegue o trem número {dois|quatro|seis}.'),
  dict(who='Ravi', en='Where is the {platform|exit|ticket machine}?', pt='Onde fica {a plataforma|a saída|a máquina de bilhetes}?'),
  dict(who='You', en='Go down the stairs. It’s on the {left|right}.', pt='Desça a escada. Fica à {esquerda|direita}.')],
 dlg=[
  dict(who='Ravi', en='Excuse me, which train goes to {Brooklyn|downtown|the airport}?', pt='Com licença, qual trem vai {ao Brooklyn|ao centro|ao aeroporto}?'),
  dict(who='You', en='Take the number {two|four|six} train.', pt='Pegue o trem número {dois|quatro|seis}.'),
  dict(who='Ravi', en='Where is the {platform|exit|ticket machine}?', pt='Onde fica {a plataforma|a saída|a máquina de bilhetes}?'),
  dict(who='You', en='Go down the stairs. It’s on the {left|right}.', pt='Desça a escada. Fica à {esquerda|direita}.'),
  dict(who='Ravi', en='How many {stops|minutes|blocks}?', pt='Quantas {paradas|minutos|quadras}?'),
  dict(who='You', en='{Four|Three|Five} stops. Get off at Atlantic Avenue.', pt='{Quatro|Três|Cinco} paradas. Desça na Atlantic Avenue.'),
  dict(who='Ravi', en='Is it {express|local|fast}?', pt='É {expresso|local|rápido}?'),
  dict(who='You', en='No, it’s local. It’s {slow|crowded|old}.', pt='Não, é local. É {lento|lotado|antigo}.'),
  dict(who='Ravi', en='Have a good {trip|day}!', pt='Tenha uma boa {viagem|dia}!')],
 vocab=[
  dict(w='subway', pt='metrô', e='🚇', ex=['I take the subway to work.', 'The subway is fast in the city.']),
  dict(w='train', pt='trem', e='🚆', ex=['Which train goes downtown?', 'The train is late today.']),
  dict(w='platform', pt='plataforma', e='🛤️', ex=['The platform is downstairs.', 'Wait on the platform.']),
  dict(w='stop', pt='parada', e='🛑', ex=['Our stop is next.', 'It is three stops from here.']),
  dict(w='stairs', pt='escada', e='🪜', ex=['Go down the stairs.', 'The stairs are on the left.']),
  dict(w='express', pt='expresso', e='⚡', ex=['The express train skips stops.', 'Is this train express?'])],
 molds=[
  dict(title='Perguntar qual trem', frame='Excuse me, which {vehicle} goes to {place}?', slots=[dict(key='vehicle', opts=['train', 'bus', 'subway line']), dict(key='place', opts=['Brooklyn', 'downtown', 'the airport'])], model='Excuse me, which train goes to Brooklyn?', note='“Which train…?” escolhe entre várias linhas possíveis.'),
  dict(title='Dizer como ir', frame='Take the number {n} train. Get off at {stop}.', slots=[dict(key='n', opts=['two', 'four', 'six']), dict(key='stop', opts=['Atlantic Avenue', 'Union Square', 'Grand Central'])], model='Take the number two train. Get off at Atlantic Avenue.', note='“Take” é pegar o transporte e “get off” é descer dele.'),
  dict(title='Escrever as paradas', frame='It’s {n} stops. The platform is down the stairs, on the {side}.', slots=[dict(key='n', opts=['four', 'three', 'five']), dict(key='side', opts=['left', 'right', 'left side'])], model='It’s four stops. The platform is down the stairs, on the left.', note='Escreva quantas paradas faltam e onde fica a plataforma.')],
 sounds=[
  dict(say='Take the number two train.', tag='ritmo: palavras fortes', tip='Marque “take”, “num-”, “two” e “train”. “The” fica muito curto.'),
  dict(say='Get off at Atlantic Avenue.', tag='ligação: get off at', tip='Junte tudo: “get-off-at”. O “t” de “get” liga ao “off”, quase “gedoff”.'),
  dict(say='How many stops?', tag='acento: stops', tip='A voz sobe um pouco e a palavra mais forte é “stops”.')],
 role=dict(turns=[
  dict(npc='Excuse me, which train goes to Brooklyn?', opts=[
   dict(en='Take the number two train.', pt='Pegue o trem número dois.', reply='Thanks. Where is the platform?'),
   dict(en='Take the number four train.', pt='Pegue o trem número quatro.', reply='The four. Where is the platform?'),
   dict(en='The number two goes there.', pt='O número dois vai para lá.', reply='Great. Where is the platform?')]),
  dict(npc=None, opts=[
   dict(en='Go down the stairs. It’s on the left.', pt='Desça a escada. Fica à esquerda.', reply='Stairs, on the left. How many stops?'),
   dict(en='It’s down the stairs, on the right.', pt='Fica descendo a escada, à direita.', reply='On the right. How many stops?'),
   dict(en='Follow me. I’m going there too.', pt='Siga-me. Também vou para lá.', reply='Oh, thanks! How many stops?')]),
  dict(npc=None, opts=[
   dict(en='Four stops. Get off at Atlantic Avenue.', pt='Quatro paradas. Desça na Atlantic Avenue.', reply='Four stops. Is it express?'),
   dict(en='Three stops. Get off at Union Square.', pt='Três paradas. Desça em Union Square.', reply='Three stops. Is it express?'),
   dict(en='About five stops. Look at the map.', pt='Umas cinco paradas. Olhe o mapa.', reply='OK, five stops. Is it express?')]),
  dict(npc=None, opts=[
   dict(en='No, it’s local. It’s slow.', pt='Não, é local. É lento.', reply='OK, thanks. Have a good trip!'),
   dict(en='No, it’s local. It stops everywhere.', pt='Não, é local. Para em todas.', reply='I see. Thanks! Have a good trip!'),
   dict(en='Yes, it’s express. It’s fast.', pt='Sim, é expresso. É rápido.', reply='Great, that’s faster! Have a good trip!')])],
  change=['A pessoa quer ir a outro bairro; mude o número do trem e as paradas.', 'A plataforma está fechada e você indica outra saída.', 'O trem está atrasado; diga isso e sugira esperar.']),
 writing=dict(task='Escreva como ir de metrô de um lugar para outro: qual trem pegar, quantas paradas e onde descer.', model='Take the number two train. It is four stops. Get off at Atlantic Avenue. The platform is down the stairs.', kw=['train', 'stops', 'off', 'stairs'], checks=['Disse qual trem pegar.', 'Disse quantas paradas ou onde descer.', 'Usei “take” e “get off” corretamente.']),
 scenes=dict(pool=['subway', 'sub2', 'station', 'nyc'], npc=dict(g='m', role='friend'), you=dict(g='f')),
 convo=dict(npc=dict(name='Ravi'), turns=[
  dict(npc='Excuse me, which train goes to Brooklyn?', pt='Com licença, qual trem vai ao Brooklyn?', opts=[
   dict(en='Brooklyn is a big place.', pt='O Brooklyn é um lugar grande.', ok=False, fb='Não diz qual trem pegar.'),
   dict(en='I like the subway too.', pt='Eu também gosto do metrô.', ok=False, fb='Fala do metrô, mas não responde.'),
   dict(en='Take the number two train.', pt='Pegue o trem número dois.', ok=True, fb='Diz qual linha pegar.')]),
  dict(npc='Where is the platform?', pt='Onde fica a plataforma?', opts=[
   dict(en='Go down the stairs. It’s on the left.', pt='Desça a escada. Fica à esquerda.', ok=True, fb='Diz como chegar e de que lado.'),
   dict(en='The platform is a train.', pt='A plataforma é um trem.', ok=False, fb='Troca os significados de platform e train.'),
   dict(en='Yes, it is on the platform.', pt='Sim, está na plataforma.', ok=False, fb='A pergunta é “where”; não é sim ou não.')]),
  dict(npc='How many stops?', pt='Quantas paradas?', opts=[
   dict(en='It is two dollars.', pt='São dois dólares.', ok=False, fb='Isso responde a “how much”, não a “how many stops”.'),
   dict(en='Four stops. Get off at Atlantic Avenue.', pt='Quatro paradas. Desça na Atlantic Avenue.', ok=True, fb='Dá o número e onde descer.'),
   dict(en='I stop the train.', pt='Eu paro o trem.', ok=False, fb='Mistura o verbo stop com o substantivo stop.')]),
  dict(npc='Is it express?', pt='É expresso?', opts=[
   dict(en='No, it’s local. It’s slow.', pt='Não, é local. É lento.', ok=True, fb='Responde e explica a diferença.'),
   dict(en='Yes, it is a train.', pt='Sim, é um trem.', ok=False, fb='Óbvio demais; ele quer saber se é expresso.'),
   dict(en='No, it is not a subway.', pt='Não, não é metrô.', ok=False, fb='O trem é do metrô; a dúvida é sobre expresso ou local.')]),
  dict(npc='Have a good trip!', pt='Boa viagem!', opts=[
   dict(en='Bye! Take care.', pt='Tchau! Se cuide.', ok=True, fb='Despedida simpática de quem ajudou.'),
   dict(en='Thank you for the ticket.', pt='Obrigado pela passagem.', ok=False, fb='Você não deu passagem a ninguém.'),
   dict(en='You’re welcome. Bye!', pt='De nada. Tchau!', ok=False, fb='Ele ainda não agradeceu; “you’re welcome” fica cedo demais.')])]),
)
