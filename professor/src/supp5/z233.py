"""Bloco de verbos e expressões da aula 233: perdi meu crachá."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('lose', '😟', 'perder', ('lose', 'I lose my keys a lot.', 'Eu perco minhas chaves muito.'), ('loses', 'Ben loses his badge.', 'O Ben perde o crachá.'), ('lost', 'I lost my badge.', 'Eu perdi meu crachá.'), ('losing', 'I am losing my keys.', 'Estou perdendo minhas chaves.'), 'Lose vira lost no passado (irregular).'),
  vb('drop', '⬇️', 'deixar cair', ('drop', 'I drop my pen.', 'Eu deixo minha caneta cair.'), ('drops', 'Ben drops his bag.', 'O Ben deixa a bolsa cair.'), ('dropped', 'She dropped her badge.', 'Ela deixou o crachá cair.'), ('dropping', 'He is dropping the card.', 'Ele está deixando o cartão cair.'), 'Dobra o p no passado: dropped.'),
  vb('keep', '🧷', 'guardar / manter', ('keep', 'I keep it in my pocket.', 'Eu guardo no bolso.'), ('keeps', 'Rosa keeps the keys here.', 'A Rosa guarda as chaves aqui.'), ('kept', 'He kept it in his bag.', 'Ele guardou na bolsa.'), ('keeping', 'I am keeping it safe.', 'Estou mantendo isso seguro.'), 'Keep vira kept no passado.'),
  vb('worry', '😬', 'preocupar-se', ('worry', 'I worry about my badge.', 'Eu me preocupo com meu crachá.'), ('worries', 'Ben worries a lot.', 'O Ben se preocupa muito.'), ('worried', 'He worried all morning.', 'Ele se preocupou a manhã toda.'), ('worrying', 'Stop worrying!', 'Pare de se preocupar!'), 'Worry vira worries e worried (y vira i).'),
  vb('tell', '🗣️', 'contar / avisar', ('tell', 'I tell security.', 'Eu aviso a segurança.'), ('tells', 'Ben tells Rosa his name.', 'O Ben diz seu nome à Rosa.'), ('told', 'I told her yesterday.', 'Eu avisei ela ontem.'), ('telling', 'I am telling the guard.', 'Estou avisando o guarda.'), 'Tell vira told no passado.')],
 verb_game=[
  dict(scene='Ontem você perdeu o crachá.', en='Yesterday I ___ my badge.', opts=['lose', 'lost', 'losing'], ans=1, pt='Ontem eu perdi meu crachá.', why='“Yesterday” pede passado: lost.'),
  dict(scene='O Ben sempre guarda o crachá no bolso.', en='Ben ___ his badge in his pocket.', opts=['keep', 'keeps', 'kept'], ans=1, pt='O Ben guarda o crachá no bolso.', why='Com “Ben” (ele), o presente leva -s: keeps.'),
  dict(scene='Agora você avisa o guarda.', en='I am ___ the guard.', opts=['tell', 'told', 'telling'], ans=2, pt='Estou avisando o guarda.', why='“am” + verbo termina em -ing: telling.'),
  dict(scene='Ele está ansioso.', en='He ___ about his badge.', opts=['worries', 'worry', 'worrying'], ans=0, pt='Ele se preocupa com o crachá.', why='Com “He”, worry vira worries.')],
 expressions=[
  dict(en='I lost my badge.', pt='Perdi meu crachá.', ex='Hi, I lost my badge.', exp='Para dizer o problema na segurança.', c='a'),
  dict(en='When did you last see it?', pt='Quando viu pela última vez?', ex='When did you last see your keys?', exp='Pergunta usada para achar um objeto perdido.', c='b'),
  dict(en='Don’t worry.', pt='Não se preocupe.', ex='Don’t worry. It’s OK.', exp='Para acalmar alguém.', c='c'),
  dict(en='May I see another ID?', pt='Posso ver outro documento?', ex='May I see another ID, please?', exp='Pedido educado da segurança.', c='d'),
  dict(en='on the third floor', pt='no terceiro andar', ex='I work on the third floor.', exp='Para dizer onde trabalha: sempre on.', c='a'),
  dict(en='I can’t open the door.', pt='Não consigo abrir a porta.', ex='I can’t open the door without my badge.', exp='Para explicar o que o problema causa.', c='b')],
 expr_game=[
  dict(cue='Você quer dizer ao segurança que perdeu o crachá.', opts=['I lost my badge.', 'Don’t worry.', 'May I see another ID?'], ans=0, why='I lost my badge diz o problema.'),
  dict(cue='O colega está nervoso e você quer acalmá-lo.', opts=['Don’t worry.', 'On the third floor.', 'When did you last see it?'], ans=0, why='Don’t worry acalma.'),
  dict(cue='Você quer dizer em que andar trabalha.', opts=['I work on the third floor.', 'I can’t open the door.', 'Here you go.'], ans=0, why='On the third floor diz o andar.')])
