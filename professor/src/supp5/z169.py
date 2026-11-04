"""Bloco de verbos e expressões da aula 169: esteira de bagagem."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('lose', '😟', 'perder', ('lose', 'I lose my bag.', 'Eu perco minha mala.'), ('loses', 'The airline loses bags.', 'A companhia perde malas.'), ('lost', 'They lost my suitcase.', 'Eles perderam minha mala.'), ('losing', 'I am losing my keys.', 'Estou perdendo minhas chaves.'), 'Lose é irregular: lost. Cuidado: lose (verbo) e loose (solto).'),
  vb('forget', '🤦', 'esquecer', ('forget', 'I forget my bag.', 'Eu esqueço minha bolsa.'), ('forgets', 'Rita forgets her key.', 'A Rita esquece a chave.'), ('forgot', 'I forgot my ribbon.', 'Eu esqueci minha fita.'), ('forgetting', 'I am forgetting my bag.', 'Estou esquecendo minha bolsa.'), 'Forget é irregular: forgot.'),
  vb('lift', '🏋️', 'levantar, erguer', ('lift', 'I lift the bag.', 'Eu levanto a mala.'), ('lifts', 'He lifts the suitcase.', 'Ele levanta a mala.'), ('lifted', 'She lifted the heavy bag.', 'Ela levantou a mala pesada.'), ('lifting', 'I am lifting my bag.', 'Estou levantando minha mala.'), 'Passado regular: lifted.'),
  vb('push', '🛒', 'empurrar', ('push', 'I push the cart.', 'Eu empurro o carrinho.'), ('pushes', 'Rita pushes the cart.', 'A Rita empurra o carrinho.'), ('pushed', 'We pushed the cart.', 'Nós empurramos o carrinho.'), ('pushing', 'I am pushing the cart.', 'Estou empurrando o carrinho.'), 'Terminação -sh: 3ª pessoa pushes.'),
  vb('pull', '🧲', 'puxar', ('pull', 'I pull the handle.', 'Eu puxo a alça.'), ('pulls', 'He pulls the suitcase.', 'Ele puxa a mala.'), ('pulled', 'She pulled her bag.', 'Ela puxou a mala.'), ('pulling', 'I am pulling my suitcase.', 'Estou puxando minha mala.'), 'Pull é o oposto de push. Passado regular: pulled.')],
 verb_game=[
  dict(scene='Ontem a companhia perdeu sua mala.', en='They ___ my suitcase yesterday.', opts=['lose', 'lost', 'losing'], ans=1, pt='Eles perderam minha mala ontem.', why='Yesterday pede passado: lost.'),
  dict(scene='Rita empurra o carrinho agora.', en='Rita is ___ the cart.', opts=['push', 'pushes', 'pushing'], ans=2, pt='A Rita está empurrando o carrinho.', why='Is + -ing: pushing.'),
  dict(scene='Você não quer esquecer a mala.', en='I don’t want to ___ my bag.', opts=['forget', 'forgot', 'forgets'], ans=0, pt='Não quero esquecer minha mala.', why='Depois de to, use o verbo base: forget.'),
  dict(scene='Ele puxa a mala pela alça.', en='He ___ the suitcase by the handle.', opts=['pull', 'pulls', 'pulled'], ans=1, pt='Ele puxa a mala pela alça.', why='Ele (3ª pessoa) leva -s: pulls.')],
 expressions=[
  dict(en='Excuse me, where is…?', pt='Com licença, onde fica…?', ex='Excuse me, where is baggage claim?', exp='Para perguntar por um lugar.', c='a'),
  dict(en='Follow the signs.', pt='Siga as placas.', ex='Follow the signs. It’s downstairs.', exp='Para indicar o caminho.', c='b'),
  dict(en='I can’t find my suitcase.', pt='Não encontro minha mala.', ex='Excuse me, I can’t find my suitcase.', exp='Para explicar que perdeu algo.', c='c'),
  dict(en='What does it look like?', pt='Como ela é?', ex='What does your bag look like?', exp='Para pedir a descrição de algo.', c='d'),
  dict(en='Fill it out.', pt='Preencha.', ex='Please fill out this form.', exp='Quando pedem para você preencher um formulário.', c='a'),
  dict(en='It’ll turn up.', pt='Vai aparecer.', ex='Don’t worry. It’ll turn up.', exp='Para tranquilizar alguém que perdeu algo.', c='b')],
 expr_game=[
  dict(cue='Você quer saber onde fica a esteira.', opts=['Excuse me, where is…?', 'Fill it out.', 'It’ll turn up.'], ans=0, why='Excuse me, where is…? pede um lugar.'),
  dict(cue='Você consolando um amigo que perdeu a mala.', opts=['It’ll turn up.', 'Follow the signs.', 'I can’t find it.'], ans=0, why='It’ll turn up = vai aparecer.'),
  dict(cue='O funcionário quer saber como é a mala.', opts=['What does it look like?', 'Fill it out.', 'Follow the signs.'], ans=0, why='What does it look like? pede a descrição.')])
