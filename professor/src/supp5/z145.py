"""Bloco de verbos e expressões da aula 145: passeio histórico em Boston."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('follow', '🔴', 'seguir', ('follow', 'We follow the red line.', 'Nós seguimos a linha vermelha.'), ('follows', 'Dana follows the guide.', 'A Dana segue a guia.'), ('followed', 'We followed the trail.', 'Nós seguimos a trilha.'), ('following', 'We are following the line.', 'Estamos seguindo a linha.'), 'Passado regular: followed.'),
  vb('lead', '🚩', 'guiar, conduzir', ('lead', 'Grace leads the tour.', 'A Grace conduz o passeio.'), ('leads', 'The line leads to the church.', 'A linha leva até a igreja.'), ('led', 'She led us to the harbor.', 'Ela nos levou até o porto.'), ('leading', 'She is leading the group.', 'Ela está guiando o grupo.'), 'Lead é irregular: led no passado.'),
  vb('rest', '🪑', 'descansar', ('rest', 'We rest on a bench.', 'Nós descansamos em um banco.'), ('rests', 'Dana rests for a minute.', 'A Dana descansa por um minuto.'), ('rested', 'We rested near the harbor.', 'Nós descansamos perto do porto.'), ('resting', 'We are resting now.', 'Estamos descansando agora.'), 'Rest = descansar. Passado regular: rested.'),
  vb('stand', '🧍', 'ficar de pé', ('stand', 'We stand in the park.', 'Nós ficamos de pé no parque.'), ('stands', 'The guide stands by the flag.', 'A guia fica perto da bandeira.'), ('stood', 'We stood in line.', 'Nós ficamos na fila.'), ('standing', 'We are standing here.', 'Estamos em pé aqui.'), 'Stand é irregular: stood no passado.'),
  vb('tell', '🗣️', 'contar', ('tell', 'I tell a story.', 'Eu conto uma história.'), ('tells', 'The guide tells stories.', 'A guia conta histórias.'), ('told', 'She told us about the church.', 'Ela nos contou sobre a igreja.'), ('telling', 'She is telling a story.', 'Ela está contando uma história.'), 'Tell é irregular: told. Tell me / tell us leva alguém.')],
 verb_game=[
  dict(scene='Agora vocês estão seguindo a linha vermelha.', en='We are ___ the red line.', opts=['follow', 'following', 'followed'], ans=1, pt='Estamos seguindo a linha vermelha.', why='“are” + -ing: following.'),
  dict(scene='Ontem a guia contou uma história.', en='Yesterday the guide ___ us a story.', opts=['tells', 'told', 'telling'], ans=1, pt='Ontem a guia nos contou uma história.', why='Passado irregular: told.'),
  dict(scene='A Grace conduz o grupo.', en='Grace ___ the group.', opts=['lead', 'leads', 'led'], ans=1, pt='A Grace conduz o grupo.', why='Ela (3ª pessoa) leva -s: leads.'),
  dict(scene='Vocês querem descansar um pouco.', en='We want to ___ for a minute.', opts=['rest', 'rests', 'rested'], ans=0, pt='Queremos descansar por um minuto.', why='Depois de to, use o verbo base: rest.')],
 expressions=[
  dict(en='Are you here for the tour?', pt='Vocês vieram para o passeio?', ex='Hello! Are you here for the tour?', exp='O guia confirma quem está no grupo.', c='a'),
  dict(en='When does it start?', pt='Quando começa?', ex='When does the tour start?', exp='Para perguntar a hora de início.', c='b'),
  dict(en='Follow the red line.', pt='Siga a linha vermelha.', ex='Please follow the red line.', exp='Para mostrar o caminho a seguir.', c='c'),
  dict(en='How long is the walk?', pt='Quanto tempo dura a caminhada?', ex='How long is the walk? About two hours.', exp='Para perguntar a duração do passeio.', c='d'),
  dict(en='It’s easy and flat.', pt='É fácil e plano.', ex='Don’t worry. It’s easy and flat.', exp='Para dizer que não é cansativo.', c='a'),
  dict(en='Lead the way!', pt='Vá na frente!', ex='We are ready. Lead the way!', exp='Para pedir que o guia vá na frente.', c='b')],
 expr_game=[
  dict(cue='Você quer saber a hora de início do passeio.', opts=['When does it start?', 'Lead the way!', 'It’s easy and flat.'], ans=0, why='When does it start? pergunta a hora.'),
  dict(cue='Você quer saber quanto tempo dura a caminhada.', opts=['How long is the walk?', 'Follow the red line.', 'Lead the way!'], ans=0, why='How long is… pergunta a duração.'),
  dict(cue='O grupo está pronto e você pede que o guia vá na frente.', opts=['Lead the way!', 'When does it start?', 'It’s easy and flat.'], ans=0, why='Lead the way! = vá na frente.')])
