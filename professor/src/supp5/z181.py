"""Bloco de verbos e expressões da aula 181: barulho."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('knock', '🚪', 'bater (na porta)', ('knock', 'I knock on his door.', 'Eu bato na porta dele.'), ('knocks', 'Mia knocks twice.', 'A Mia bate duas vezes.'), ('knocked', 'She knocked softly.', 'Ela bateu de leve.'), ('knocking', 'Someone is knocking.', 'Alguém está batendo.'), 'Knock on the door: use on. O k inicial não soa.'),
  vb('sleep', '😴', 'dormir', ('sleep', 'I sleep at eleven.', 'Eu durmo às onze.'), ('sleeps', 'The baby sleeps now.', 'O bebê dorme agora.'), ('slept', 'I slept badly.', 'Dormi mal.'), ('sleeping', 'She is sleeping.', 'Ela está dormindo.'), 'Passado irregular: sleep vira slept.'),
  vb('wake', '⏰', 'acordar', ('wake', 'We wake at seven.', 'Nós acordamos às sete.'), ('wakes', 'The noise wakes him.', 'O barulho o acorda.'), ('woke', 'The music woke me.', 'A música me acordou.'), ('waking', 'I am waking the kids.', 'Estou acordando as crianças.'), 'Passado irregular: wake vira woke. Wake up é muito comum.'),
  vb('shout', '📢', 'gritar', ('shout', 'Please do not shout.', 'Por favor, não grite.'), ('shouts', 'He shouts at night.', 'Ele grita à noite.'), ('shouted', 'They shouted in the hall.', 'Eles gritaram no corredor.'), ('shouting', 'Who is shouting?', 'Quem está gritando?'), 'Shout at alguém costuma soar bravo; shout to chama de longe.'),
  vb('listen', '👂', 'escutar', ('listen', 'I listen to music.', 'Eu escuto música.'), ('listens', 'Theo listens to jazz.', 'O Theo escuta jazz.'), ('listened', 'We listened for an hour.', 'Escutamos por uma hora.'), ('listening', 'I am listening now.', 'Estou escutando agora.'), 'Use listen to + algo: listen to music.')],
 verb_game=[
  dict(scene='A Mia bate na porta do vizinho.', en='Mia ___ on his door.', opts=['knock', 'knocks', 'knocked'], ans=1, pt='A Mia bate na porta dele.', why='Com Mia (ela), o presente leva -s: knocks.'),
  dict(scene='A música acordou você ontem à noite.', en='The music ___ me last night.', opts=['wake', 'wakes', 'woke'], ans=2, pt='A música me acordou ontem à noite.', why='“Last night” pede passado: woke.'),
  dict(scene='Agora o bebê está dormindo.', en='The baby is ___ now.', opts=['sleep', 'sleeps', 'sleeping'], ans=2, pt='O bebê está dormindo agora.', why='Is + verbo termina em -ing: sleeping.'),
  dict(scene='Você pede ao vizinho para não gritar.', en='Please do not ___.', opts=['shout', 'shouts', 'shouted'], ans=0, pt='Por favor, não grite.', why='Depois de do not, use a forma base: shout.')],
 expressions=[
  dict(en='Sorry to bother you.', pt='Desculpe incomodar.', ex='Hi. Sorry to bother you.', exp='Para começar a falar com alguém sem soar rude.', c='a'),
  dict(en='a little loud', pt='um pouco alto', ex='The TV is a little loud.', exp='Jeito suave de dizer que há barulho.', c='b'),
  dict(en='turn it down', pt='abaixar (o som)', ex='Could you turn it down, please?', exp='Pedir para diminuir o volume.', c='c'),
  dict(en='I have to sleep.', pt='Preciso dormir.', ex='It is late, and I have to sleep.', exp='Para dar o motivo do pedido.', c='d'),
  dict(en='It happens.', pt='Acontece.', ex='It’s okay. It happens.', exp='Resposta gentil quando alguém pede desculpas.', c='a'),
  dict(en='Sleep tight.', pt='Durma bem.', ex='Good night. Sleep tight!', exp='Despedida carinhosa antes de dormir.', c='b')],
 expr_game=[
  dict(cue='Você quer pedir que o vizinho diminua o volume.', opts=['Could you turn it down, please?', 'Sleep tight.', 'It happens.'], ans=0, why='Turn it down = abaixar o som.'),
  dict(cue='O vizinho pede desculpas e você quer ser gentil.', opts=['Sorry to bother you.', 'It’s okay. It happens.', 'I have to sleep.'], ans=1, why='It happens suaviza a conversa.'),
  dict(cue='Você bate na porta e quer começar com educação.', opts=['Sleep tight.', 'It happens.', 'Sorry to bother you.'], ans=2, why='Sorry to bother you abre a conversa.')])
