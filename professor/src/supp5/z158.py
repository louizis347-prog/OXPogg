"""Bloco de verbos e expressões da aula 158: aula de yoga."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('breathe', '🌬️', 'respirar', ('breathe', 'We breathe slowly.', 'Nós respiramos devagar.'), ('breathes', 'Ines breathes in and out.', 'A Ines inspira e expira.'), ('breathed', 'I breathed slowly.', 'Eu respirei devagar.'), ('breathing', 'I am breathing slowly.', 'Estou respirando devagar.'), 'Verbo: breathe (com e). O substantivo é breath (sem e).'),
  vb('stretch', '🤸', 'alongar', ('stretch', 'I stretch my arms.', 'Eu alongo os braços.'), ('stretches', 'Victor stretches his legs.', 'O Victor alonga as pernas.'), ('stretched', 'We stretched for ten minutes.', 'Nós alongamos por dez minutos.'), ('stretching', 'She is stretching her back.', 'Ela está alongando as costas.'), 'Com ele/ela: stretches (acrescenta -es).'),
  vb('relax', '😌', 'relaxar', ('relax', 'I relax my shoulders.', 'Eu relaxo os ombros.'), ('relaxes', 'Ines relaxes on the mat.', 'A Ines relaxa no tapete.'), ('relaxed', 'We relaxed at the end.', 'Nós relaxamos no fim.'), ('relaxing', 'I am relaxing now.', 'Estou relaxando agora.'), 'Relax é regular. Com ele/ela: relaxes.'),
  vb('bend', '🙇', 'dobrar', ('bend', 'I bend my legs.', 'Eu dobro as pernas.'), ('bends', 'Victor bends his arms.', 'O Victor dobra os braços.'), ('bent', 'She bent her knees.', 'Ela dobrou os joelhos.'), ('bending', 'I am bending my back.', 'Estou dobrando as costas.'), 'Passado irregular: bend vira bent.'),
  vb('lift', '🏋️', 'levantar / erguer', ('lift', 'We lift our arms.', 'Nós levantamos os braços.'), ('lifts', 'Ines lifts her leg.', 'A Ines levanta a perna.'), ('lifted', 'I lifted my head.', 'Eu levantei a cabeça.'), ('lifting', 'He is lifting his arms.', 'Ele está levantando os braços.'), 'Lift = erguer algo; levantar da cama é get up.')],
 verb_game=[
  dict(scene='Toda aula a Ines relaxa no fim.', en='Ines ___ at the end of class.', opts=['relax', 'relaxes', 'relaxed'], ans=1, pt='A Ines relaxa no fim da aula.', why='Com “Ines” (ela), o presente leva -es: relaxes.'),
  dict(scene='Ontem você dobrou as pernas.', en='Yesterday I ___ my legs.', opts=['bend', 'bent', 'bending'], ans=1, pt='Ontem eu dobrei as pernas.', why='“Yesterday” pede passado: bent.'),
  dict(scene='Agora vocês estão respirando devagar.', en='We are ___ slowly.', opts=['breathe', 'breathes', 'breathing'], ans=2, pt='Estamos respirando devagar.', why='“are” + verbo termina em -ing: breathing.'),
  dict(scene='Todos erguem os braços.', en='We ___ our arms.', opts=['lift', 'lifts', 'lifted'], ans=0, pt='Nós levantamos os braços.', why='Com “we” o presente fica na forma base: lift.')],
 expressions=[
  dict(en='Is this your first time?', pt='É sua primeira vez?', ex='Welcome! Is this your first time?', exp='Pergunta comum para quem chega a uma aula nova.', c='a'),
  dict(en='Don’t worry.', pt='Não se preocupe.', ex='Don’t worry. It is easy.', exp='Para acalmar alguém que está nervoso.', c='b'),
  dict(en='Where should I put it?', pt='Onde devo colocar?', ex='Where should I put my mat?', exp='Para perguntar o lugar de um objeto.', c='c'),
  dict(en='Anywhere you like.', pt='Onde quiser.', ex='Sit anywhere you like.', exp='Para dizer que a pessoa pode escolher o lugar.', c='d'),
  dict(en='Take a deep breath.', pt='Respire fundo.', ex='Take a deep breath and relax.', exp='Para pedir calma, no yoga ou no dia a dia.', c='a'),
  dict(en='Go at your own pace.', pt='Siga seu ritmo.', ex='Go at your own pace. No rush.', exp='Para dizer que ninguém precisa se apressar.', c='b')],
 expr_game=[
  dict(cue='Você quer saber onde colocar o tapete.', opts=['Where should I put it?', 'Don’t worry.', 'Anywhere you like.'], ans=0, why='Where should I put it? pergunta o lugar.'),
  dict(cue='Um aluno está nervoso e você quer acalmá-lo.', opts=['Is this your first time?', 'Don’t worry.', 'Where should I put it?'], ans=1, why='Don’t worry. acalma a pessoa.'),
  dict(cue='Você quer dizer que a pessoa escolhe o lugar.', opts=['Take a deep breath.', 'Anywhere you like.', 'Is this your first time?'], ans=1, why='Anywhere you like. dá liberdade de escolha.')])
