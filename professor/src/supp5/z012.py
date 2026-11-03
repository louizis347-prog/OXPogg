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
  vb('decorate', '🎈', 'decorar', ('decorate', 'We decorate the room.', 'Nós decoramos a sala.'), ('decorates', 'Mia decorates the cake.', 'A Mia decora o bolo.'), ('decorated', 'I decorated the house.', 'Eu decorei a casa.'), ('decorating', 'We are decorating now.', 'Estamos decorando agora.'), 'Decorate + -d no passado: decorated.'),
  vb('blow', '🕯️', 'soprar', ('blow', 'I blow out the candles.', 'Eu sopro as velas.'), ('blows', 'Max blows out the candles.', 'O Max sopra as velas.'), ('blew', 'She blew out five candles.', 'Ela soprou cinco velas.'), ('blowing', 'He is blowing up balloons.', 'Ele está enchendo balões.'), 'Irregular: blow, blew. Blow out = apagar soprando.'),
  vb('turn', '🎈', 'fazer (idade)', ('turn', 'I turn thirty in July.', 'Eu faço trinta anos em julho.'), ('turns', 'Max turns five today.', 'O Max faz cinco anos hoje.'), ('turned', 'She turned ten in March.', 'Ela fez dez anos em março.'), ('turning', 'I am turning twenty.', 'Estou fazendo vinte anos.'), 'Turn + idade = completar anos.')],
 verb_game=[
  dict(scene='A Mia decora o bolo de aniversário.', en='Mia ___ the cake.', opts=['decorate', 'decorates', 'decorated'], ans=1, pt='A Mia decora o bolo.', why='Com “Mia” (ela) o presente leva -s: decorates.'),
  dict(scene='Ano passado ela soprou as velas.', en='She ___ out the candles last year.', opts=['blow', 'blows', 'blew'], ans=2, pt='Ela soprou as velas ano passado.', why='“Last year” pede passado irregular: blew.'),
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
