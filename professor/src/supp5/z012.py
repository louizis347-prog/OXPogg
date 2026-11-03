"""Bloco de verbos e expressões da aula 012."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('sing', '🎤', 'cantar', ('sing', 'We sing Happy Birthday.', 'Nós cantamos Parabéns.'), ('sings', 'Mia sings loudly.', 'A Mia canta alto.'), ('sang', 'Everyone sang to her.', 'Todo mundo cantou para ela.'), ('singing', 'We are singing now.', 'Estamos cantando agora.'), 'Passado irregular: sing vira sang.'),
  vb('invite', '💌', 'convidar', ('invite', 'I invite my friends.', 'Eu convido meus amigos.'), ('invites', 'Ana invites everyone.', 'A Ana convida todo mundo.'), ('invited', 'He invited me to the party.', 'Ele me convidou para a festa.'), ('inviting', 'I am inviting Sam.', 'Estou convidando o Sam.'), 'Invite someone to + evento: invite me to the party.'),
  vb('cut', '🔪', 'cortar', ('cut', 'I cut the cake.', 'Eu corto o bolo.'), ('cuts', 'Mia cuts the cake.', 'A Mia corta o bolo.'), ('cut', 'He cut a big piece.', 'Ele cortou um pedaço grande.'), ('cutting', 'I am cutting the cake.', 'Estou cortando o bolo.'), 'Cut é igual no passado: cut. Só o -ing duplica o t: cutting.'),
  vb('eat', '🍰', 'comer', ('eat', 'We eat cake.', 'Nós comemos bolo.'), ('eats', 'Sam eats two pieces.', 'O Sam come dois pedaços.'), ('ate', 'She ate a big slice.', 'Ela comeu uma fatia grande.'), ('eating', 'I am eating cake.', 'Estou comendo bolo.'), 'Passado irregular: eat vira ate.'),
  vb('turn', '🎈', 'fazer (idade)', ('turn', 'I turn thirty in July.', 'Eu faço trinta anos em julho.'), ('turns', 'Max turns five today.', 'O Max faz cinco anos hoje.'), ('turned', 'She turned ten in March.', 'Ela fez dez anos em março.'), ('turning', 'I am turning twenty.', 'Estou fazendo vinte anos.'), 'Turn + idade = completar anos.')],
 verb_game=[
  dict(scene='A Mia corta o bolo de aniversário.', en='Mia ___ the cake.', opts=['cut', 'cuts', 'cutting'], ans=1, pt='A Mia corta o bolo.', why='Com “Mia” (ela) o presente leva -s: cuts.'),
  dict(scene='Ano passado ela comeu duas fatias.', en='She ___ two slices last year.', opts=['eat', 'eats', 'ate'], ans=2, pt='Ela comeu duas fatias ano passado.', why='“Last year” pede passado irregular: ate.'),
  dict(scene='Você está chamando o Sam agora.', en='I am ___ Sam to the party.', opts=['invite', 'inviting', 'invited'], ans=1, pt='Estou convidando o Sam para a festa.', why='“am” + verbo termina em -ing: inviting.'),
  dict(scene='Seus amigos e você cantam parabéns.', en='We ___ Happy Birthday.', opts=['sing', 'sings', 'sang'], ans=0, pt='Nós cantamos Parabéns.', why='Com “we”, o presente fica na forma base: sing.')],
 expressions=[
  dict(en='When is your birthday?', pt='Quando é seu aniversário?', ex='When is your birthday? — In July.', exp='Para perguntar a data do aniversário de alguém.', c='a'),
  dict(en='My birthday is in…', pt='Meu aniversário é em…', ex='My birthday is in December.', exp='Para dizer o mês do seu aniversário.', c='b'),
  dict(en='on July fourth', pt='no dia 4 de julho', ex='The party is on July fourth.', exp='Datas usam on + mês + número ordinal.', c='c'),
  dict(en='Happy birthday!', pt='Feliz aniversário!', ex='Happy birthday! How old are you?', exp='Para parabenizar no dia.', c='d'),
  dict(en='Let’s celebrate!', pt='Vamos comemorar!', ex='Great idea! Let’s celebrate!', exp='Para propor uma comemoração.', c='a'),
  dict(en='See you then!', pt='A gente se vê lá!', ex='Perfect. See you then!', exp='Para se despedir combinando a data.', c='b')],
 expr_game=[
  dict(cue='Você quer saber o dia do aniversário de um amigo.', opts=['When is your birthday?', 'Happy birthday!', 'See you then!'], ans=0, why='When is…? pergunta a data.'),
  dict(cue='É o aniversário dele hoje e você quer parabenizar.', opts=['My birthday is in May.', 'Happy birthday!', 'When is your party?'], ans=1, why='Happy birthday! é o parabéns.'),
  dict(cue='Você combina a festa e quer se despedir.', opts=['See you then!', 'How old are you?', 'Let me see.'], ans=0, why='See you then! fecha o combinado.')])
