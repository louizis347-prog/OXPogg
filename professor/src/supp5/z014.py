"""Bloco de verbos e expressões da aula 014."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('call', '📞', 'ligar', ('call', 'I call Raj.', 'Eu ligo para o Raj.'), ('calls', 'Mia calls me.', 'A Mia me liga.'), ('called', 'I called you.', 'Eu liguei para você.'), ('calling', 'Who is calling?', 'Quem está ligando?'), 'Call + pessoa; sem “to”.'),
  vb('open', '🚪', 'abrir', ('open', 'I open the door.', 'Eu abro a porta.'), ('opens', 'Raj opens the gate.', 'O Raj abre o portão.'), ('opened', 'He opened the window.', 'Ele abriu a janela.'), ('opening', 'I am opening it now.', 'Estou abrindo agora.'), 'Passado regular: opened.'),
  vb('forget', '🔑', 'esquecer', ('forget', 'I forget my key.', 'Eu esqueço minha chave.'), ('forgets', 'Sam forgets his phone.', 'O Sam esquece o celular.'), ('forgot', 'I forgot my key.', 'Eu esqueci minha chave.'), ('forgetting', 'I am forgetting it again!', 'Estou esquecendo de novo!'), 'Irregular: forget, forgot.'),
  vb('help', '🤝', 'ajudar', ('help', 'I help my neighbor.', 'Eu ajudo meu vizinho.'), ('helps', 'Raj helps me.', 'O Raj me ajuda.'), ('helped', 'He helped me today.', 'Ele me ajudou hoje.'), ('helping', 'You are helping me.', 'Você está me ajudando.'), 'Can you help me? é o pedido básico.'),
  vb('speak', '🗣️', 'falar', ('speak', 'I speak to Raj.', 'Eu falo com o Raj.'), ('speaks', 'Mia speaks softly.', 'A Mia fala baixo.'), ('spoke', 'I spoke to Ana.', 'Eu falei com a Ana.'), ('speaking', 'This is Raj speaking.', 'Aqui é o Raj falando.'), 'Irregular: speak, spoke. “Speaking” = sou eu, no telefone.')],
 verb_game=[
  dict(scene='Você esqueceu a chave hoje cedo.', en='I ___ my key this morning.', opts=['forget', 'forgot', 'forgetting'], ans=1, pt='Eu esqueci minha chave hoje cedo.', why='Passado de forget: forgot.'),
  dict(scene='O Raj abre o portão para você.', en='Raj ___ the gate.', opts=['open', 'opens', 'opening'], ans=1, pt='O Raj abre o portão.', why='Com “Raj” (ele): opens.'),
  dict(scene='Alguém atende e quer saber quem liga.', en='Who is ___?', opts=['call', 'called', 'calling'], ans=2, pt='Quem está ligando?', why='“is” + -ing: calling.'),
  dict(scene='Você fala com a Ana ontem.', en='I ___ to Ana yesterday.', opts=['speak', 'spoke', 'speaks'], ans=1, pt='Eu falei com a Ana ontem.', why='Passado de speak: spoke.')],
 expressions=[
  dict(en='Is Raj there?', pt='O Raj está?', ex='Hi, is Raj there?', exp='Para pedir alguém ao telefone.', c='a'),
  dict(en='Who is this?', pt='Quem é?', ex='Who is this, please?', exp='Para perguntar quem fala.', c='b'),
  dict(en='This is Ana.', pt='É a Ana.', ex='This is Ana, from 4B.', exp='Para se identificar ao telefone.', c='c'),
  dict(en='Can you open the door?', pt='Você pode abrir a porta?', ex='Can you open the door? I forgot my key.', exp='Para pedir um favor.', c='d'),
  dict(en='Thanks, you’re a lifesaver!', pt='Valeu, você me salvou!', ex='Thanks, you’re a lifesaver!', exp='Para agradecer um grande favor.', c='a'),
  dict(en='Anytime.', pt='Quando quiser.', ex='Anytime. Bye!', exp='Resposta simpática a um agradecimento.', c='b')],
 expr_game=[
  dict(cue='Você liga e quer falar com o Raj.', opts=['This is Raj.', 'Is Raj there?', 'Anytime.'], ans=1, why='Is… there? pede alguém ao telefone.'),
  dict(cue='Você esqueceu a chave e pede ajuda.', opts=['Can you open the door?', 'Who is this?', 'Anytime.'], ans=0, why='Can you…? pede um favor.'),
  dict(cue='Alguém agradece e você responde simpático.', opts=['Anytime.', 'Is Raj there?', 'This is Ana.'], ans=0, why='Anytime = disponha.')])
