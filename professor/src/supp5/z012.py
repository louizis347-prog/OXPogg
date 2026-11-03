"""Bloco de verbos e expressões da aula 012."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('celebrate', '🎉', 'comemorar', ('celebrate', 'We celebrate in July.', 'Nós comemoramos em julho.'), ('celebrates', 'Mia celebrates at home.', 'A Mia comemora em casa.'), ('celebrated', 'I celebrated with friends.', 'Eu comemorei com amigos.'), ('celebrating', 'We are celebrating today.', 'Estamos comemorando hoje.'), 'Celebrate + -d no passado; serve para aniversário e feriados.'),
  vb('invite', '💌', 'convidar', ('invite', 'I invite my friends.', 'Eu convido meus amigos.'), ('invites', 'Ana invites everyone.', 'A Ana convida todo mundo.'), ('invited', 'He invited me to the party.', 'Ele me convidou para a festa.'), ('inviting', 'I am inviting Sam.', 'Estou convidando o Sam.'), 'Invite someone to + evento: invite me to the party.'),
  vb('have', '🎂', 'ter / fazer (festa)', ('have', 'We have a party in March.', 'Nós fazemos uma festa em março.'), ('has', 'She has a birthday in May.', 'Ela faz aniversário em maio.'), ('had', 'I had a cake last year.', 'Eu tive um bolo ano passado.'), ('having', 'We are having a party.', 'Estamos fazendo uma festa.'), 'Have vira has com ele/ela e had no passado.'),
  vb('come', '🚪', 'vir', ('come', 'Please come to my party.', 'Por favor, venha à minha festa.'), ('comes', 'Raj comes at six.', 'O Raj vem às seis.'), ('came', 'Everyone came on Sunday.', 'Todo mundo veio no domingo.'), ('coming', 'Are you coming on Friday?', 'Você vem na sexta?'), 'Irregular: come, came. Também serve para “ir” a algo de quem convida.'),
  vb('turn', '🎈', 'fazer (idade)', ('turn', 'I turn thirty in July.', 'Eu faço trinta anos em julho.'), ('turns', 'Max turns five today.', 'O Max faz cinco anos hoje.'), ('turned', 'She turned ten in March.', 'Ela fez dez anos em março.'), ('turning', 'I am turning twenty.', 'Estou fazendo vinte anos.'), 'Turn + idade = completar anos.')],
 verb_game=[
  dict(scene='Você diz que a Mia faz aniversário em maio.', en='Mia ___ a birthday in May.', opts=['have', 'has', 'had'], ans=1, pt='A Mia faz aniversário em maio.', why='Com “Mia” (ela), have vira has.'),
  dict(scene='Ano passado todos foram à sua festa.', en='Everyone ___ to my party last year.', opts=['come', 'comes', 'came'], ans=2, pt='Todo mundo veio à minha festa ano passado.', why='“Last year” pede passado: came.'),
  dict(scene='Você está chamando o Sam agora.', en='I am ___ Sam to the party.', opts=['invite', 'inviting', 'invited'], ans=1, pt='Estou convidando o Sam para a festa.', why='“am” + verbo termina em -ing: inviting.'),
  dict(scene='Seus amigos e você sempre comemoram em julho.', en='We ___ in July.', opts=['celebrate', 'celebrates', 'celebrated'], ans=0, pt='Nós comemoramos em julho.', why='Com “we”, o presente fica na forma base.')],
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
