"""Bloco de verbos e expressões da aula 43: perguntar onde fica um lugar."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('type', '📲', 'digitar', ('type', 'I type the address.', 'Eu digito o endereço.'), ('types', 'She types the name.', 'Ela digita o nome.'), ('typed', 'He typed the street.', 'Ele digitou a rua.'), ('typing', 'I am typing it now.', 'Estou digitando agora.'), 'Type é regular: typed.'),
  vb('zoom', '🔍', 'dar zoom', ('zoom', 'I zoom in on the map.', 'Eu dou zoom no mapa.'), ('zooms', 'He zooms out.', 'Ele diminui o zoom.'), ('zoomed', 'We zoomed in.', 'Nós demos zoom.'), ('zooming', 'I am zooming in.', 'Estou dando zoom.'), 'Zoom in = aproximar; zoom out = afastar.'),
  vb('walk', '🚶', 'andar / ir a pé', ('walk', 'I walk to the park.', 'Eu vou a pé ao parque.'), ('walks', 'He walks five minutes.', 'Ele anda cinco minutos.'), ('walked', 'We walked to the bank.', 'Nós fomos a pé ao banco.'), ('walking', 'I am walking now.', 'Estou andando agora.'), 'On foot = a pé; walk também serve.'),
  vb('wander', '🧭', 'vagar / andar sem rumo', ('wander', 'We wander downtown.', 'Nós vagamos pelo centro.'), ('wanders', 'Tom wanders around.', 'O Tom anda sem rumo.'), ('wandered', 'I wandered for an hour.', 'Eu vaguei por uma hora.'), ('wandering', 'I am wandering around.', 'Estou perambulando.'), 'Wander é regular: wandered.'),
  vb('thank', '🙏', 'agradecer', ('thank', 'I thank you.', 'Eu agradeço a você.'), ('thanks', 'She thanks the man.', 'Ela agradece ao homem.'), ('thanked', 'We thanked him.', 'Nós o agradecemos.'), ('thanking', 'I am thanking her.', 'Estou agradecendo a ela.'), 'No dia a dia, Thank you e Thanks bastam.')],
 verb_game=[
  dict(scene='Ontem você digitou o endereço no celular.', en='I ___ the address into my phone yesterday.', opts=['type', 'typed', 'typing'], ans=1, pt='Eu digitei o endereço no celular ontem.', why='“Yesterday” pede passado: typed.'),
  dict(scene='O Tom sempre vai a pé à farmácia.', en='Tom ___ to the pharmacy.', opts=['walk', 'walks', 'walking'], ans=1, pt='O Tom vai a pé à farmácia.', why='Tom (ele) no presente leva -s: walks.'),
  dict(scene='Ontem vocês deram zoom no mapa.', en='We ___ in on the map yesterday.', opts=['zoom', 'zoomed', 'zooming'], ans=1, pt='Nós demos zoom no mapa ontem.', why='“Yesterday” pede passado: zoomed.'),
  dict(scene='Agora você anda sem rumo pelo bairro.', en='I am ___ around the neighborhood.', opts=['wander', 'wanders', 'wandering'], ans=2, pt='Estou perambulando pelo bairro.', why='“am” + -ing: wandering.')],
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
