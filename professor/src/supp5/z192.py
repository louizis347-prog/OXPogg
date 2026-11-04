"""Bloco de verbos e expressões da aula 192: rever um amigo."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('hug', '🤗', 'abraçar', ('hug', 'I hug my friend.', 'Eu abraço meu amigo.'), ('hugs', 'Dina hugs Mark.', 'A Dina abraça o Mark.'), ('hugged', 'We hugged at the door.', 'Nós nos abraçamos na porta.'), ('hugging', 'They are hugging.', 'Eles estão se abraçando.'), 'Hug dobra o g antes de -ed e -ing: hugged, hugging.'),
  vb('miss', '💭', 'sentir falta', ('miss', 'I miss my old school.', 'Sinto falta da minha antiga escola.'), ('misses', 'Dina misses her friends.', 'A Dina sente falta dos amigos.'), ('missed', 'We missed you.', 'Sentimos sua falta.'), ('missing', 'I am missing my family today.', 'Hoje estou com saudade da família.'), 'Com -ss, a 3ª pessoa leva -es: misses. Miss também é perder o ônibus.'),
  vb('live', '🏠', 'morar', ('live', 'I live in Utah.', 'Eu moro em Utah.'), ('lives', 'Mark lives in Salt Lake City.', 'O Mark mora em Salt Lake City.'), ('lived', 'We lived in Texas.', 'Nós moramos no Texas.'), ('living', 'He is living in a hotel this week.', 'Ele está morando em um hotel esta semana.'), 'Para onde você mora, use I live. -ing só para algo temporário.'),
  vb('teach', '🧑‍🏫', 'ensinar', ('teach', 'I teach English.', 'Eu ensino inglês.'), ('teaches', 'Aaron teaches English.', 'O Aaron ensina inglês.'), ('taught', 'She taught me music.', 'Ela me ensinou música.'), ('teaching', 'He is teaching a class.', 'Ele está dando uma aula.'), 'Teach é irregular: taught. Com -ch, a 3ª pessoa leva -es: teaches.'),
  vb('tell', '🗣️', 'contar / dizer', ('tell', 'I tell my friend the news.', 'Eu conto as novidades ao meu amigo.'), ('tells', 'Dina tells Mark her news.', 'A Dina conta suas novidades ao Mark.'), ('told', 'He told me about his job.', 'Ele me contou sobre seu trabalho.'), ('telling', 'I am telling a story.', 'Estou contando uma história.'), 'Tell é irregular: told. Tell + pessoa + algo.')],
 verb_game=[
  dict(scene='A Dina ensina inglês.', en='Dina ___ English.', opts=['teach', 'teaches', 'taught'], ans=1, pt='A Dina ensina inglês.', why='Com “Dina” (ela), o presente leva -es: teaches.'),
  dict(scene='Ontem o amigo contou seu trabalho novo.', en='Yesterday he ___ me about his new job.', opts=['tell', 'telling', 'told'], ans=2, pt='Ontem ele me contou sobre seu trabalho novo.', why='“Yesterday” pede passado irregular: told.'),
  dict(scene='Os dois amigos se abraçam agora.', en='The friends are ___ now.', opts=['hug', 'hugs', 'hugging'], ans=2, pt='Os amigos estão se abraçando agora.', why='“are” + verbo termina em -ing: hugging.'),
  dict(scene='Eu moro em Utah.', en='I ___ in Utah.', opts=['live', 'lives', 'lived'], ans=0, pt='Eu moro em Utah.', why='Com “I”, o presente fica na forma base: live.')],
 expressions=[
  dict(en='Long time no see!', pt='Quanto tempo!', ex='Hi, Dina! Long time no see!', exp='Para cumprimentar quem você não vê há muito.', c='a'),
  dict(en='How have you been?', pt='Como você tem estado?', ex='Hi! How have you been?', exp='Para saber das novidades desde o último encontro.', c='b'),
  dict(en='Since when?', pt='Desde quando?', ex='You live in Utah? Since when?', exp='Para saber quando algo começou.', c='c'),
  dict(en='What do you do?', pt='O que você faz?', ex='So, what do you do?', exp='Para perguntar o trabalho de alguém.', c='d'),
  dict(en='I miss you.', pt='Sinto sua falta.', ex='I miss you, my friend.', exp='Para dizer que está com saudade.', c='a'),
  dict(en='Let’s keep in touch.', pt='Vamos manter contato.', ex='It was great! Let’s keep in touch.', exp='Na despedida, para trocar contatos.', c='b')],
 expr_game=[
  dict(cue='Você vê um velho amigo e quer cumprimentar.', opts=['Since when?', 'Long time no see!', 'What do you do?'], ans=1, why='Long time no see! é o cumprimento para quem não se vê há tempo.'),
  dict(cue='Você quer saber o trabalho do amigo.', opts=['What do you do?', 'I miss you.', 'How have you been?'], ans=0, why='What do you do? pergunta o trabalho.'),
  dict(cue='Na despedida, você quer trocar telefones.', opts=['Since when?', 'Long time no see!', 'Let’s keep in touch.'], ans=2, why='Let’s keep in touch fecha a conversa.')])
