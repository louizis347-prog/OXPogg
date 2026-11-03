K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('wash', '🫧', 'lavar', ('wash', 'I wash my clothes on Sunday.', 'Eu lavo minhas roupas no domingo.'), ('washes', 'Claire washes her towels.', 'A Claire lava as toalhas dela.'), ('washed', 'He washed his socks.', 'Ele lavou as meias dele.'), ('washing', 'I am washing my shirts.', 'Estou lavando minhas camisas.'), 'Wash + es na 3ª pessoa: washes.'),
  vb('dry', '🌀', 'secar', ('dry', 'We dry the towels.', 'Nós secamos as toalhas.'), ('dries', 'Dan dries his socks.', 'O Dan seca as meias dele.'), ('dried', 'I dried my shirt.', 'Eu sequei minha camisa.'), ('drying', 'The dryer is drying my clothes.', 'A secadora está secando minhas roupas.'), 'Dry vira dries e dried (y vira i); no -ing fica drying.'),
  vb('fold', '👕', 'dobrar', ('fold', 'I fold the towels.', 'Eu dobro as toalhas.'), ('folds', 'She folds her shirts.', 'Ela dobra as camisas dela.'), ('folded', 'He folded his socks.', 'Ele dobrou as meias dele.'), ('folding', 'I am folding my clothes.', 'Estou dobrando minhas roupas.'), 'Regular: fold, folded, folding.'),
  vb('press', '🔘', 'apertar', ('press', 'You press the green button.', 'Você aperta o botão verde.'), ('presses', 'Claire presses start.', 'A Claire aperta iniciar.'), ('pressed', 'I pressed the wrong button.', 'Eu apertei o botão errado.'), ('pressing', 'I am pressing the button.', 'Estou apertando o botão.'), 'Press + es na 3ª pessoa: presses.'),
  vb('hang', '🪝', 'pendurar', ('hang', 'I hang my shirts.', 'Eu penduro minhas camisas.'), ('hangs', 'Dan hangs his jacket.', 'O Dan pendura a jaqueta dele.'), ('hung', 'She hung her towel.', 'Ela pendurou a toalha dela.'), ('hanging', 'I am hanging my clothes.', 'Estou pendurando minhas roupas.'), 'Irregular: hang, hung (hanged é para outro uso).')],
 verb_game=[
  dict(scene='A Claire lava suas toalhas todo domingo.', en='Claire ___ her towels on Sunday.', opts=['wash', 'washes', 'washing'], ans=1, pt='A Claire lava as toalhas no domingo.', why='Com “Claire” (ela), o presente leva -es: washes.'),
  dict(scene='Agora a secadora está funcionando.', en='The dryer is ___ my clothes.', opts=['dry', 'dries', 'drying'], ans=2, pt='A secadora está secando minhas roupas.', why='“is” + verbo termina em -ing: drying.'),
  dict(scene='Ontem você dobrou as meias.', en='Yesterday I ___ my socks.', opts=['fold', 'folded', 'folding'], ans=1, pt='Ontem eu dobrei minhas meias.', why='“Yesterday” pede passado: folded.'),
  dict(scene='Você aperta o botão para começar.', en='You ___ the green button.', opts=['press', 'presses', 'pressed'], ans=0, pt='Você aperta o botão verde.', why='Com “you” o presente fica na forma base: press.')],
 expressions=[
  dict(en='Excuse me, how does this work?', pt='Com licença, como isto funciona?', ex='Excuse me, how does this machine work?', exp='Para pedir ajuda com uma máquina, de forma educada.', c='a'),
  dict(en='Do you have coins?', pt='Você tem moedas?', ex='Do you have coins for the washer?', exp='Para perguntar se alguém tem moedas.', c='b'),
  dict(en='Press start.', pt='Aperte iniciar.', ex='Close the door and press start.', exp='Instrução comum em máquinas.', c='c'),
  dict(en='How long does it take?', pt='Quanto tempo demora?', ex='How long does it take to dry?', exp='Para perguntar a duração de algo.', c='d'),
  dict(en='laundry day', pt='dia de lavar roupa', ex='Ugh, it\'s laundry day.', exp='Dia em que se lava roupa; informal.', c='a'),
  dict(en='It never ends.', pt='Nunca acaba.', ex='Chores? It never ends.', exp='Queixa leve e bem-humorada sobre tarefas.', c='b')],
 expr_game=[
  dict(cue='Você quer saber quanto tempo a lavadora leva.', opts=['How long does it take?', 'Press start.', 'Do you have coins?'], ans=0, why='How long does it take? pergunta a duração.'),
  dict(cue='Você não sabe usar a máquina e pede ajuda ao vizinho.', opts=['It never ends.', 'Excuse me, how does this work?', 'Forty minutes.'], ans=1, why='Excuse me + how does this work? é o pedido de ajuda.'),
  dict(cue='Você quer saber se o vizinho tem moedas.', opts=['Do you have coins?', 'Laundry day!', 'Press start.'], ans=0, why='Do you have…? pergunta se alguém tem algo.')])
