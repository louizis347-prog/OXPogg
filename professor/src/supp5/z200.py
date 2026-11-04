"""Bloco de verbos e expressões da aula 200: escolher a roupa."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('wear', '👕', 'vestir, usar', ('wear', 'I wear long pants.', 'Eu uso calça comprida.'), ('wears', 'Miles wears a blue shirt.', 'O Miles veste uma camisa azul.'), ('wore', 'He wore a jacket.', 'Ele vestiu um casaco.'), ('wearing', 'I am wearing sneakers.', 'Estou usando tênis.'), 'Wear é para roupas que você já está usando. Passado irregular: wore.'),
  vb('pick', '👆', 'escolher', ('pick', 'I pick the blue shirt.', 'Eu escolho a camisa azul.'), ('picks', 'Mom picks a jacket.', 'A mãe escolhe um casaco.'), ('picked', 'She picked green socks.', 'Ela escolheu meias verdes.'), ('picking', 'I am picking my outfit.', 'Estou escolhendo minha roupa.'), 'Pick é mais informal que choose. Passado regular: picked.'),
  vb('hang', '🪝', 'pendurar', ('hang', 'I hang my coat here.', 'Eu penduro meu casaco aqui.'), ('hangs', 'Miles hangs his jacket.', 'O Miles pendura o casaco.'), ('hung', 'She hung her shirt.', 'Ela pendurou a camisa.'), ('hanging', 'The coat is hanging there.', 'O casaco está pendurado ali.'), 'Hang vira hung no passado, quando se trata de roupas.'),
  vb('fold', '📦', 'dobrar', ('fold', 'I fold my shirts.', 'Eu dobro minhas camisas.'), ('folds', 'Mom folds the socks.', 'A mãe dobra as meias.'), ('folded', 'He folded his pants.', 'Ele dobrou a calça.'), ('folding', 'I am folding clothes.', 'Estou dobrando roupas.'), 'Fold é regular: acrescente -ed no passado.'),
  vb('change', '🔄', 'trocar', ('change', 'I change my shirt.', 'Eu troco de camisa.'), ('changes', 'Miles changes his socks.', 'O Miles troca de meias.'), ('changed', 'I changed my shoes.', 'Eu troquei de sapatos.'), ('changing', 'I am changing now.', 'Estou me trocando agora.'), 'Change termina em e: o passado leva só -d, e o -ing perde o e.')],
 verb_game=[
  dict(scene='O Miles usa uma camisa azul hoje.', en='Miles ___ a blue shirt today.', opts=['wear', 'wears', 'wore'], ans=1, pt='O Miles veste uma camisa azul hoje.', why='Com Miles (ele) no presente: wears.'),
  dict(scene='Ontem você escolheu uma camisa verde.', en='Yesterday I ___ a green shirt.', opts=['pick', 'picks', 'picked'], ans=2, pt='Ontem eu escolhi uma camisa verde.', why='Yesterday pede passado: picked.'),
  dict(scene='Agora você está trocando de roupa.', en='I am ___ my clothes.', opts=['change', 'changes', 'changing'], ans=2, pt='Estou trocando de roupa.', why='Am + verbo termina em -ing: changing.'),
  dict(scene='Toda noite vocês dobram as roupas.', en='We ___ our clothes every night.', opts=['fold', 'folds', 'folded'], ans=0, pt='Nós dobramos nossas roupas toda noite.', why='Com we no presente: fold.')],
 expressions=[
  dict(en='What should I wear?', pt='O que devo vestir?', ex='What should I wear today?', exp='Para pedir conselho sobre a roupa.', c='a'),
  dict(en='What’s the weather like?', pt='Como está o tempo?', ex='What’s the weather like outside?', exp='Para saber o tempo antes de sair.', c='b'),
  dict(en='It’s cool and cloudy.', pt='Está fresco e nublado.', ex='It’s cool and cloudy today.', exp='Para descrever o tempo.', c='c'),
  dict(en='looks nice', pt='fica bonito', ex='The blue one looks nice.', exp='Para elogiar uma roupa.', c='d'),
  dict(en='put on', pt='vestir, colocar', ex='Put on your jacket.', exp='Verbo frasal para vestir uma peça.', c='a'),
  dict(en='Should I wear a jacket?', pt='Devo vestir um casaco?', ex='It’s cold. Should I wear a jacket?', exp='Para decidir se leva um casaco.', c='b')],
 expr_game=[
  dict(cue='Você quer saber se deve levar um casaco.', opts=['Should I wear a jacket?', 'It’s cool and cloudy.', 'looks nice'], ans=0, why='Should I wear…? pede conselho sobre a roupa.'),
  dict(cue='Você descreve um dia frio e com nuvens.', opts=['put on', 'What should I wear?', 'It’s cool and cloudy.'], ans=2, why='It’s + adjetivo descreve o tempo.'),
  dict(cue='Você quer elogiar a camisa azul do seu amigo.', opts=['The blue one looks nice.', 'What’s the weather like?', 'put on'], ans=0, why='Looks nice elogia a roupa.')])
