"""Bloco de verbos e expressões da aula 43: perguntar onde fica um lugar."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('ask', '🗣️', 'perguntar', ('ask', 'I ask a woman for help.', 'Eu peço ajuda a uma mulher.'), ('asks', 'Tom asks about the bank.', 'O Tom pergunta sobre o banco.'), ('asked', 'We asked the way.', 'Nós perguntamos o caminho.'), ('asking', 'I am asking about the pharmacy.', 'Estou perguntando sobre a farmácia.'), 'Ask about = perguntar sobre; ask for help = pedir ajuda.'),
  vb('find', '🔎', 'encontrar', ('find', 'I find the bank easily.', 'Eu encontro o banco fácil.'), ('finds', 'She finds the street.', 'Ela encontra a rua.'), ('found', 'We found the post office.', 'Nós encontramos o correio.'), ('finding', 'I am finding the way.', 'Estou encontrando o caminho.'), 'Irregular: find vira found.'),
  vb('walk', '🚶', 'andar / ir a pé', ('walk', 'I walk to the park.', 'Eu vou a pé ao parque.'), ('walks', 'He walks five minutes.', 'Ele anda cinco minutos.'), ('walked', 'We walked to the bank.', 'Nós fomos a pé ao banco.'), ('walking', 'I am walking now.', 'Estou andando agora.'), 'On foot = a pé; walk também serve.'),
  vb('need', '📌', 'precisar', ('need', 'I need a pharmacy.', 'Eu preciso de uma farmácia.'), ('needs', 'Ana needs the post office.', 'A Ana precisa do correio.'), ('needed', 'He needed the bank.', 'Ele precisava do banco.'), ('needing', 'She is needing help.', 'Ela está precisando de ajuda.'), 'Need + substantivo: need a pharmacy. Em inglês falado, prefira I need…'),
  vb('thank', '🙏', 'agradecer', ('thank', 'I thank you.', 'Eu agradeço a você.'), ('thanks', 'She thanks the man.', 'Ela agradece ao homem.'), ('thanked', 'We thanked him.', 'Nós o agradecemos.'), ('thanking', 'I am thanking her.', 'Estou agradecendo a ela.'), 'No dia a dia, Thank you e Thanks bastam.')],
 verb_game=[
  dict(scene='Você para uma pessoa na rua para pedir informação.', en='I ___ a woman about the bank.', opts=['ask', 'asks', 'asked'], ans=2, pt='Eu perguntei a uma mulher sobre o banco.', why='O contexto passado pede asked.'),
  dict(scene='O Tom sempre vai a pé à farmácia.', en='Tom ___ to the pharmacy.', opts=['walk', 'walks', 'walking'], ans=1, pt='O Tom vai a pé à farmácia.', why='Tom (ele) no presente leva -s: walks.'),
  dict(scene='Ontem vocês encontraram o correio.', en='We ___ the post office yesterday.', opts=['find', 'found', 'finding'], ans=1, pt='Nós encontramos o correio ontem.', why='“Yesterday” pede passado: found.'),
  dict(scene='Você precisa de uma farmácia agora.', en='I ___ a pharmacy.', opts=['need', 'needs', 'needed'], ans=0, pt='Eu preciso de uma farmácia.', why='Com “I”, o presente fica na forma base: need.')],
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
