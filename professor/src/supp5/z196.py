"""Bloco de verbos e expressões da aula 196: chamada de vídeo."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('hear', '👂', 'ouvir', ('hear', 'I hear you now.', 'Eu ouço você agora.'), ('hears', 'Mom hears a little.', 'A mãe ouve um pouco.'), ('heard', 'I heard nothing.', 'Eu não ouvi nada.'), ('hearing', 'I am hearing a loud noise.', 'Estou ouvindo um barulho alto.'), 'Hear é ouvir sem querer; com can: Can you hear me? Passado irregular: heard.'),
  vb('talk', '🗣️', 'conversar', ('talk', 'We talk every Sunday.', 'Nós conversamos todo domingo.'), ('talks', 'Ruth talks to her mom.', 'A Ruth conversa com a mãe.'), ('talked', 'We talked for an hour.', 'Nós conversamos por uma hora.'), ('talking', 'I am talking now.', 'Estou conversando agora.'), 'Talk to = conversar com alguém. Passado regular: talked.'),
  vb('wave', '👋', 'acenar', ('wave', 'I wave at the camera.', 'Eu aceno para a câmera.'), ('waves', 'She waves goodbye.', 'Ela acena para dizer tchau.'), ('waved', 'He waved hello.', 'Ele acenou para dizer oi.'), ('waving', 'Mom is waving.', 'A mãe está acenando.'), 'Wave termina em e: o passado só leva -d (waved).'),
  vb('miss', '💛', 'sentir saudade', ('miss', 'I miss my family.', 'Eu sinto saudade da minha família.'), ('misses', 'Ruth misses her mom.', 'A Ruth sente saudade da mãe.'), ('missed', 'We missed you.', 'Sentimos sua falta.'), ('missing', 'I am missing my bus.', 'Estou perdendo meu ônibus.'), 'Miss tem dois usos: sentir falta e perder (um ônibus). Com ele, a 3ª pessoa é misses.'),
  vb('laugh', '😂', 'rir', ('laugh', 'We laugh a lot.', 'Nós rimos muito.'), ('laughs', 'Mom laughs at the joke.', 'A mãe ri da piada.'), ('laughed', 'They laughed together.', 'Eles riram juntos.'), ('laughing', 'I am laughing now.', 'Estou rindo agora.'), 'Laugh at = rir de algo. A pronúncia é “laf”: o gh soa como f.')],
 verb_game=[
  dict(scene='O som está baixo e você não escuta bem.', en='I can ___ you a little.', opts=['hear', 'hears', 'heard'], ans=0, pt='Eu consigo ouvir você um pouco.', why='Depois de can, use o verbo base: hear.'),
  dict(scene='A mãe da Ruth ri da situação agora.', en='Mom ___ at the mute message.', opts=['laugh', 'laughs', 'laughed'], ans=1, pt='A mãe ri da mensagem de mudo.', why='Com Mom (ela) no presente: laughs.'),
  dict(scene='Ontem vocês conversaram por vídeo.', en='We ___ for an hour yesterday.', opts=['talk', 'talks', 'talked'], ans=2, pt='Nós conversamos por uma hora ontem.', why='Yesterday pede passado: talked.'),
  dict(scene='Agora a Ruth está acenando para a câmera.', en='Ruth is ___ at the camera.', opts=['wave', 'waves', 'waving'], ans=2, pt='A Ruth está acenando para a câmera.', why='Is + verbo termina em -ing: waving.')],
 expressions=[
  dict(en='Can you hear me?', pt='Você me ouve?', ex='Hi! Can you hear me?', exp='Para checar o som no começo da chamada.', c='a'),
  dict(en='Turn up the volume.', pt='Aumente o volume.', ex='A little. Turn up the volume.', exp='Quando o som está baixo.', c='b'),
  dict(en='You’re on mute.', pt='Você está no mudo.', ex='Sorry, you’re on mute.', exp='Para avisar que o microfone está desligado.', c='c'),
  dict(en='Bad connection', pt='Conexão ruim', ex='I have a bad connection today.', exp='Quando a imagem trava ou o som corta.', c='d'),
  dict(en='Show me…', pt='Me mostre…', ex='Show me your apartment!', exp='Para pedir para ver algo pela câmera.', c='a'),
  dict(en='Talk soon.', pt='Falamos logo.', ex='Love you. Talk soon.', exp='Despedida simpática no fim da ligação.', c='b')],
 expr_game=[
  dict(cue='Você quer saber se a outra pessoa escuta você.', opts=['Can you hear me?', 'Talk soon.', 'Show me your room!'], ans=0, why='Can you hear me? checa o som.'),
  dict(cue='Você vê que a pessoa fala, mas não há som. O microfone dela está desligado.', opts=['Bad connection', 'You’re on mute.', 'Turn up the volume.'], ans=1, why='You’re on mute avisa do microfone.'),
  dict(cue='Você quer terminar a ligação com carinho.', opts=['Show me your room!', 'Can you hear me?', 'Love you. Talk soon.'], ans=2, why='Love you. Talk soon. fecha a ligação.')])
