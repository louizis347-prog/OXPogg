"""Bloco de verbos e expressões da aula 73: roupas e tamanhos."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('wear', '👕', 'usar / vestir', ('wear', 'I wear a medium.', 'Eu uso M.'), ('wears', 'Marco wears a blue shirt.', 'O Marco usa uma camisa azul.'), ('wore', 'She wore a black dress.', 'Ela usou um vestido preto.'), ('wearing', 'He is wearing a jacket.', 'Ele está usando uma jaqueta.'), 'Passado irregular: wear, wore. Wear = usar roupas.'),
  vb('fit', '📐', 'servir (no tamanho)', ('fit', 'These jeans fit me.', 'Esses jeans servem em mim.'), ('fits', 'The shirt fits well.', 'A camisa serve bem.'), ('fit', 'The jacket fit last year.', 'A jaqueta servia no ano passado.'), ('fitting', 'The dress is fitting well.', 'O vestido está servindo bem.'), 'Fit não muda no passado; o -ing dobra o t: fitting.'),
  vb('fold', '🧺', 'dobrar', ('fold', 'I fold the shirts.', 'Eu dobro as camisas.'), ('folds', 'Marco folds the jeans.', 'O Marco dobra os jeans.'), ('folded', 'She folded the dress.', 'Ela dobrou o vestido.'), ('folding', 'He is folding a T-shirt.', 'Ele está dobrando uma camiseta.'), 'Fold = dobrar roupa; passado regular com -ed.'),
  vb('hang', '🪝', 'pendurar', ('hang', 'I hang the jacket here.', 'Eu penduro a jaqueta aqui.'), ('hangs', 'She hangs the dress.', 'Ela pendura o vestido.'), ('hung', 'He hung the shirt up.', 'Ele pendurou a camisa.'), ('hanging', 'The jacket is hanging on the door.', 'A jaqueta está pendurada na porta.'), 'Passado irregular: hang, hung.'),
  vb('choose', '👆', 'escolher', ('choose', 'I choose the blue one.', 'Eu escolho a azul.'), ('chooses', 'Wendy chooses a jacket.', 'A Wendy escolhe uma jaqueta.'), ('chose', 'She chose a medium.', 'Ela escolheu um M.'), ('choosing', 'I am choosing a color.', 'Estou escolhendo uma cor.'), 'Passado irregular: choose, chose. Cuidado com o -ing: choosing (sem o e).')],
 verb_game=[
  dict(scene='A Wendy agora usa a camiseta azul.', en='Wendy is ___ the blue shirt.', opts=['wear', 'wearing', 'wore'], ans=1, pt='A Wendy está usando a camiseta azul.', why='“is” + verbo termina em -ing: wearing.'),
  dict(scene='O Marco sempre dobra as camisas de manhã.', en='Marco always ___ the shirts in the morning.', opts=['fold', 'folds', 'folded'], ans=1, pt='O Marco sempre dobra as camisas de manhã.', why='Com “Marco” (ele) o presente leva -s: folds.'),
  dict(scene='Ontem a Wendy escolheu um tamanho M.', en='Yesterday Wendy ___ a medium.', opts=['choose', 'chooses', 'chose'], ans=2, pt='Ontem a Wendy escolheu um M.', why='“Yesterday” pede passado: chose (irregular).'),
  dict(scene='Esses jeans servem bem em mim.', en='These jeans ___ me well.', opts=['fit', 'fits', 'fitting'], ans=0, pt='Esses jeans servem bem em mim.', why='“These jeans” é plural: forma base fit.')],
 expressions=[
  dict(en='Can I help you?', pt='Posso ajudar?', ex='Hi! Can I help you?', exp='O vendedor oferece ajuda quando você entra.', c='a'),
  dict(en='I\'m looking for…', pt='Estou procurando…', ex='I\'m looking for a T-shirt.', exp='Para dizer o que você quer encontrar na loja.', c='b'),
  dict(en='What size are you?', pt='Qual é o seu tamanho?', ex='What size are you in jeans?', exp='Pergunta do vendedor sobre o tamanho.', c='c'),
  dict(en='Do you have it in…?', pt='Tem em…?', ex='Do you have it in blue?', exp='Para pedir outra cor ou outro tamanho.', c='d'),
  dict(en='try on', pt='provar (roupa)', ex='Can I try this jacket on?', exp='Verbo frasal: vestir uma peça para ver se serve.', c='a'),
  dict(en='It fits me!', pt='Serve em mim!', ex='It fits me! I\'ll take it.', exp='Quando a roupa tem o tamanho certo.', c='b')],
 expr_game=[
  dict(cue='Você quer ver a camiseta em outra cor.', opts=['Do you have it in blue?', 'What size are you?', 'Can I help you?'], ans=0, why='Do you have it in...? pede outra cor.'),
  dict(cue='Você quer saber onde provar a jaqueta.', opts=['Where can I try it on?', 'I\'m a medium.', 'Thanks for shopping with us!'], ans=0, why='try it on = provar a peça.'),
  dict(cue='A camiseta ficou perfeita e você comenta isso.', opts=['It fits me!', 'I\'m looking for a dress.', 'What size are you?'], ans=0, why='It fits me! diz que o tamanho está certo.')])
