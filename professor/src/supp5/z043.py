"""Bloco de verbos e expressões da aula 43: perguntar onde fica um lugar."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('show', '📲', 'mostrar', ('show', 'I show the address.', 'Eu mostro o endereço.'), ('shows', 'She shows the map.', 'Ela mostra o mapa.'), ('showed', 'He showed me the bank.', 'Ele me mostrou o banco.'), ('showing', 'I am showing my phone.', 'Estou mostrando meu celular.'), 'Show me… = me mostre. Passado: showed.'),
  vb('look', '👀', 'olhar', ('look', 'I look at the map.', 'Eu olho o mapa.'), ('looks', 'She looks at the sign.', 'Ela olha a placa.'), ('looked', 'We looked at the street.', 'Nós olhamos a rua.'), ('looking', 'I am looking for the bank.', 'Estou procurando o banco.'), 'Look at = olhar para; look for = procurar.'),
  vb('walk', '🚶', 'andar / ir a pé', ('walk', 'I walk to the park.', 'Eu vou a pé ao parque.'), ('walks', 'He walks five minutes.', 'Ele anda cinco minutos.'), ('walked', 'We walked to the bank.', 'Nós fomos a pé ao banco.'), ('walking', 'I am walking now.', 'Estou andando agora.'), 'On foot = a pé; walk também serve.'),
  vb('talk', '🗣️', 'conversar / falar', ('talk', 'I talk to a police officer.', 'Eu falo com um policial.'), ('talks', 'He talks to me.', 'Ele fala comigo.'), ('talked', 'We talked to a woman.', 'Nós falamos com uma mulher.'), ('talking', 'I am talking to a guide.', 'Estou falando com um guia.'), 'Talk to = falar com alguém.'),
  vb('thank', '🙏', 'agradecer', ('thank', 'I thank you.', 'Eu agradeço a você.'), ('thanks', 'She thanks the man.', 'Ela agradece ao homem.'), ('thanked', 'We thanked him.', 'Nós o agradecemos.'), ('thanking', 'I am thanking her.', 'Estou agradecendo a ela.'), 'No dia a dia, Thank you e Thanks bastam.')],
 verb_game=[
 dict(scene='Ontem você mostrou o endereço no celular.', en='I ___ the address on my phone yesterday.', opts=['show', 'showed', 'showing'], ans=1, pt='Eu mostrei o endereço no celular ontem.', why='“Yesterday” pede passado: showed.'),
  dict(scene='O Tom sempre vai a pé à farmácia.', en='Tom ___ to the pharmacy.', opts=['walk', 'walks', 'walking'], ans=1, pt='O Tom vai a pé à farmácia.', why='Tom (ele) no presente leva -s: walks.'),
 dict(scene='Ontem vocês olharam o mapa.', en='We ___ at the map yesterday.', opts=['look', 'looked', 'looking'], ans=1, pt='Nós olhamos o mapa ontem.', why='“Yesterday” pede passado: looked.'),
 dict(scene='Agora você fala com um guia.', en='I am ___ to a guide.', opts=['talk', 'talks', 'talking'], ans=2, pt='Estou falando com um guia.', why='“am” + -ing: talking.')],
 expressions=[
  dict(en='Excuse me, where is…?', pt='Com licença, onde fica…?', ex='Excuse me, where is the bank?', exp='Para abordar alguém e perguntar onde fica um lugar.', c='a'),
  dict(en='Is it far?', pt='É longe?', ex='Is it far from here?', exp='Para saber a distância.', c='b'),
  dict(en='on foot', pt='a pé', ex='It’s five minutes on foot.', exp='Mostra que o tempo é andando.', c='c'),
  dict(en='next to', pt='ao lado de', ex='It’s next to the post office.', exp='Para localizar um lugar perto de outro.', c='d'),
  dict(en='across from', pt='em frente a', ex='It’s across from the park.', exp='O lugar fica do outro lado da rua.', c='a'),
  dict(en='You’re welcome.', pt='De nada.', ex='Thank you! — You’re welcome.', exp='Resposta ao agradecimento.', c='b')],
 expr_game=[
  dict(cue='Você quer saber se o banco fica longe.', opts=['Is it far from here?', 'It’s next to the park.', 'You’re welcome.'], ans=0, why='Is it far…? pergunta a distância.'),
  dict(cue='Alguém diz que o correio fica do outro lado da rua.', opts=['on foot', 'across from', 'Excuse me'], ans=1, why='Across from = em frente, do outro lado.'),
  dict(cue='Alguém agradeceu pela informação que você deu.', opts=['You’re welcome.', 'Excuse me, where is…?', 'Is it far?'], ans=0, why='You’re welcome responde a um obrigado.')])
