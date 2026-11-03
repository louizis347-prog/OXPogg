"""Bloco de verbos e expressões da aula 45: pegar o metrô."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('board', '🚉', 'embarcar', ('board', 'We board the train.', 'Nós embarcamos no trem.'), ('boards', 'She boards the express.', 'Ela embarca no expresso.'), ('boarded', 'I boarded the local.', 'Eu embarquei no trem local.'), ('boarding', 'We are boarding now.', 'Estamos embarcando agora.'), 'Board é regular: boarded.'),
  vb('transfer', '🔁', 'fazer transferência', ('transfer', 'We transfer at Union.', 'Nós trocamos de linha em Union.'), ('transfers', 'Ana transfers here.', 'A Ana troca de linha aqui.'), ('transferred', 'I transferred to the A.', 'Eu troquei para a linha A.'), ('transferring', 'I am transferring now.', 'Estou trocando de linha agora.'), 'Transfer dobra o r: transferred.'),
  vb('change', '🔁', 'trocar / fazer baldeação', ('change', 'I change trains at Union.', 'Eu troco de trem em Union.'), ('changes', 'He changes at Atlantic.', 'Ele troca em Atlantic.'), ('changed', 'We changed to the six.', 'Nós trocamos para o seis.'), ('changing', 'I am changing trains.', 'Estou trocando de trem.'), 'Change trains = fazer baldeação.'),
  vb('stand', '🧍', 'ficar de pé', ('stand', 'I stand near the door.', 'Eu fico em pé perto da porta.'), ('stands', 'He stands on the platform.', 'Ele fica em pé na plataforma.'), ('stood', 'We stood all the way.', 'Nós ficamos em pé o caminho todo.'), ('standing', 'I am standing now.', 'Estou em pé agora.'), 'Irregular: stand vira stood.'),
  vb('ride', '🎢', 'andar / viajar', ('ride', 'We ride the subway.', 'Nós andamos de metrô.'), ('rides', 'Tom rides the train daily.', 'O Tom anda de trem todo dia.'), ('rode', 'I rode the express.', 'Eu andei no expresso.'), ('riding', 'I am riding the local.', 'Estou no trem local.'), 'Irregular: ride vira rode.')],
 verb_game=[
  dict(scene='Você embarcou no expresso ontem.', en='I ___ the express yesterday.', opts=['board', 'boarded', 'boarding'], ans=1, pt='Eu embarquei no expresso ontem.', why='“Yesterday” pede passado: boarded.'),
  dict(scene='A Ana troca de linha em Union todo dia.', en='Ana ___ at Union every day.', opts=['transfer', 'transfers', 'transferred'], ans=1, pt='A Ana troca de linha em Union todo dia.', why='Ana (ela) no presente leva -s: transfers.'),
  dict(scene='Você está em pé na plataforma agora.', en='I am ___ on the platform.', opts=['stand', 'stands', 'standing'], ans=2, pt='Estou em pé na plataforma.', why='“am” + -ing: standing.'),
  dict(scene='Vocês fazem baldeação em Union.', en='We ___ trains at Union.', opts=['change', 'changes', 'changed'], ans=0, pt='Nós trocamos de trem em Union.', why='Com “we”, presente na forma base: change.')],
 expressions=[
  dict(en='Which train goes to…?', pt='Qual trem vai para…?', ex='Which train goes to Brooklyn?', exp='Para saber que trem pegar.', c='a'),
  dict(en='Where is the platform?', pt='Onde fica a plataforma?', ex='Where is the platform for the six?', exp='Para achar o lugar de embarque.', c='b'),
  dict(en='get off', pt='descer', ex='Get off at Atlantic Avenue.', exp='Verbo frasal: sair do transporte.', c='c'),
  dict(en='How many stops?', pt='Quantas paradas?', ex='How many stops to the airport?', exp='Para saber a distância em paradas.', c='d'),
  dict(en='Is it express or local?', pt='É expresso ou local?', ex='Is it express or local?', exp='Para saber se o trem para em todas as estações.', c='a'),
  dict(en='Take the number two train.', pt='Pegue o trem número dois.', ex='Take the number two train downtown.', exp='Resposta comum a “which train?”.', c='b')],
 expr_game=[
  dict(cue='Você quer saber quantas estações faltam.', opts=['How many stops?', 'Get off here.', 'Where is the platform?'], ans=0, why='How many stops? pergunta o número de paradas.'),
  dict(cue='Você precisa descer na próxima estação.', opts=['get off', 'take the number two', 'change trains'], ans=0, why='Get off = descer do transporte.'),
  dict(cue='Você quer saber qual trem vai para o aeroporto.', opts=['Which train goes to the airport?', 'Where is the exit?', 'Is it local?'], ans=0, why='Which train goes to…? escolhe o trem.')])
