"""Bloco de verbos e expressões da aula 125: no consultório médico."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('cough', '😷', 'tossir', ('cough', 'I cough at night.', 'Eu tusso à noite.'), ('coughs', 'Reed coughs a lot.', 'O Reed tosse muito.'), ('coughed', 'He coughed all day.', 'Ele tossiu o dia todo.'), ('coughing', 'I am coughing now.', 'Estou tossindo agora.'), 'Cough também é substantivo: a cough = uma tosse.'),
  vb('breathe', '🌬️', 'respirar', ('breathe', 'I breathe slowly.', 'Eu respiro devagar.'), ('breathes', 'He breathes deeply.', 'Ele respira fundo.'), ('breathed', 'She breathed in.', 'Ela inspirou.'), ('breathing', 'I am breathing deeply.', 'Estou respirando fundo.'), 'Breathe tem som “bríd”; o substantivo breath tem som “bréth”.'),
  vb('swallow', '🥤', 'engolir', ('swallow', 'I swallow slowly.', 'Eu engulo devagar.'), ('swallows', 'She swallows water.', 'Ela engole água.'), ('swallowed', 'He swallowed a pill.', 'Ele engoliu um comprimido.'), ('swallowing', 'I am swallowing water.', 'Estou engolindo água.'), 'Swallow = engolir. It hurts when I swallow = dói quando engulo.'),
  vb('open', '👄', 'abrir', ('open', 'Open your mouth.', 'Abra a boca.'), ('opens', 'The doctor opens the door.', 'A médica abre a porta.'), ('opened', 'He opened his mouth.', 'Ele abriu a boca.'), ('opening', 'I am opening my mouth.', 'Estou abrindo a boca.'), 'Open your mouth é um pedido comum no consultório.'),
  vb('listen', '🎧', 'escutar', ('listen', 'Listen to my chest.', 'Escute meu peito.'), ('listens', 'The doctor listens to him.', 'A médica o escuta.'), ('listened', 'She listened to my chest.', 'Ela escutou meu peito.'), ('listening', 'The doctor is listening.', 'A médica está escutando.'), 'Listen to = escutar alguém ou algo. Não esqueça o to.')],
 verb_game=[
  dict(scene='Reed tosse muito à noite.', en='Reed ___ at night.', opts=['cough', 'coughs', 'coughed'], ans=1, pt='O Reed tosse à noite.', why='Com Reed (ele), o presente leva -s: coughs.'),
  dict(scene='Ontem ela abriu a boca para o médico.', en='Yesterday she ___ her mouth.', opts=['opens', 'opening', 'opened'], ans=2, pt='Ontem ela abriu a boca.', why='Yesterday pede passado: opened.'),
  dict(scene='Agora a médica escuta o peito.', en='The doctor is ___ to my chest.', opts=['listen', 'listening', 'listens'], ans=1, pt='A médica está escutando meu peito.', why='is + verbo termina em -ing.'),
  dict(scene='Você respira devagar, como ela pediu.', en='I ___ slowly.', opts=['breathe', 'breathes', 'breathing'], ans=0, pt='Eu respiro devagar.', why='Com I, o presente fica na forma base.')],
 expressions=[
  dict(en='sore throat', pt='dor de garganta', ex='I have a sore throat.', exp='Para dizer que a garganta dói.', c='a'),
  dict(en='What’s the problem?', pt='Qual é o problema?', ex='Hello. What’s the problem?', exp='A pergunta do médico no início.', c='b'),
  dict(en='How long?', pt='Há quanto tempo?', ex='How long do you have them?', exp='Para saber quando começou.', c='c'),
  dict(en='since Monday', pt='desde segunda', ex='I have a cough since Monday.', exp='Para dar o dia em que começou.', c='d'),
  dict(en='Say “ah.”', pt='Diga “ah”.', ex='Open your mouth. Say “ah.”', exp='Pedido do médico para olhar a garganta.', c='a'),
  dict(en='Stay home.', pt='Fique em casa.', ex='Stay home and rest.', exp='Conselho comum quando alguém está doente.', c='b')],
 expr_game=[
  dict(cue='Você quer dizer que a garganta dói.', opts=['I have a sore throat.', 'How long?', 'Say “ah.”'], ans=0, why='Sore throat é dor de garganta.'),
  dict(cue='Você quer dizer que está assim desde segunda.', opts=['Stay home.', 'Since Monday.', 'What’s the problem?'], ans=1, why='Since + dia diz quando começou.'),
  dict(cue='A médica quer olhar sua garganta.', opts=['Open your mouth. Say “ah.”', 'How long do you have it?', 'Stay home.'], ans=0, why='Open your mouth. Say “ah” é o pedido do exame.')])
