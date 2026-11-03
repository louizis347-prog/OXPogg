"""Bloco de verbos e expressões da aula 037: sorvete."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('scoop', '🍨', 'servir (bola)', ('scoop', 'I scoop two flavors.', 'Eu sirvo dois sabores.'), ('scoops', 'Tiana scoops the ice cream.', 'A Tiana serve o sorvete.'), ('scooped', 'She scooped vanilla.', 'Ela serviu baunilha.'), ('scooping', 'Tiana is scooping a cone.', 'A Tiana está servindo uma casquinha.'), 'Scoop é a bola de sorvete e também o verbo de servi-la.'),
  vb('swirl', '🌀', 'misturar em espiral', ('swirl', 'I swirl chocolate on top.', 'Eu faço uma espiral de chocolate por cima.'), ('swirls', 'She swirls the cream.', 'Ela faz espirais com o creme.'), ('swirled', 'He swirled the syrup.', 'Ele fez espirais com a calda.'), ('swirling', 'I am swirling the sauce.', 'Estou fazendo espirais com a calda.'), 'Swirl descreve o movimento em espiral do sorvete e da calda.'),
  vb('lick', '👅', 'lamber', ('lick', 'I lick the cone.', 'Eu lambo a casquinha.'), ('licks', 'She licks the spoon.', 'Ela lambe a colher.'), ('licked', 'He licked his ice cream.', 'Ele lambeu o sorvete.'), ('licking', 'I am licking a cone.', 'Estou lambendo uma casquinha.'), 'Lick é lamber; regular: licked.'),
  vb('try', '👅', 'provar / tentar', ('try', 'I try the vanilla.', 'Eu provo a baunilha.'), ('tries', 'She tries a small spoon.', 'Ela prova uma colherinha.'), ('tried', 'He tried chocolate.', 'Ele provou chocolate.'), ('trying', 'I am trying a new flavor.', 'Estou provando um sabor novo.'), 'Try vira tries e tried (y vira ie/i).'),
  vb('nibble', '🍪', 'mordiscar', ('nibble', 'I nibble the cone.', 'Eu mordisco a casquinha.'), ('nibbles', 'She nibbles a cookie.', 'Ela mordisca um biscoito.'), ('nibbled', 'He nibbled the edge.', 'Ele mordiscou a pontinha.'), ('nibbling', 'I am nibbling the cone.', 'Estou mordiscando a casquinha.'), 'Nibble é comer em pequenas mordidas; perde o e no -ing.')],
 verb_game=[
  dict(scene='Ontem ele serviu duas bolas.', en='Yesterday he ___ two scoops.', opts=['scoop', 'scooped', 'scoops'], ans=1, pt='Ontem ele serviu duas bolas.', why='Passado regular de scoop: scooped.'),
  dict(scene='A Ana lambe a casquinha.', en='Ana ___ her cone.', opts=['lick', 'licks', 'licking'], ans=1, pt='A Ana lambe a casquinha.', why='Com “Ana” (ela), o presente leva -s: licks.'),
  dict(scene='Você mordisca a casquinha agora.', en='I am ___ the cone.', opts=['nibble', 'nibbles', 'nibbling'], ans=2, pt='Estou mordiscando a casquinha.', why='“am” + -ing: nibbling (sem o e).'),
  dict(scene='Vocês fazem espirais de calda.', en='We ___ syrup on top.', opts=['swirl', 'swirls', 'swirled'], ans=0, pt='Nós fazemos espirais de calda por cima.', why='Com “we” o presente fica na forma base: swirl.')],
 expressions=[
  dict(en='What flavor do you want?', pt='Que sabor você quer?', ex='Hi! What flavor do you want?', exp='A pergunta do atendente.', c='a'),
  dict(en='One scoop or two?', pt='Uma bola ou duas?', ex='One scoop or two? — Two, please.', exp='Para escolher a quantidade.', c='b'),
  dict(en='In a cup or a cone?', pt='No copo ou na casquinha?', ex='A cone, please.', exp='O atendente pergunta como você quer servir.', c='c'),
  dict(en='Can I try it?', pt='Posso provar?', ex='Can I try the vanilla?', exp='Para pedir uma provinha do sabor.', c='d'),
  dict(en='Chocolate, please.', pt='Chocolate, por favor.', ex='Chocolate, please. In a cone.', exp='Resposta curta para escolher o sabor.', c='a'),
  dict(en='Here you go.', pt='Aqui está.', ex='Here you go. Four dollars.', exp='Ao entregar o sorvete ou o dinheiro.', c='b')],
 expr_game=[
  dict(cue='Você quer duas bolas.', opts=['Two scoops, please.', 'In a cone.', 'Can I try it?'], ans=0, why='Two scoops, please pede duas bolas.'),
  dict(cue='O atendente pergunta copo ou casquinha e você escolhe casquinha.', opts=['A cone, please.', 'Chocolate, please.', 'One scoop.'], ans=0, why='A cone, please = casquinha, por favor.'),
  dict(cue='Você quer provar o sabor antes.', opts=['Can I try the vanilla?', 'What flavor do you want?', 'Here you go.'], ans=0, why='Can I try…? pede uma prova.')])
