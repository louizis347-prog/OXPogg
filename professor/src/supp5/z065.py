"""Bloco de verbos e expressões da aula 065: conhecer o proprietário."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('fix', '🔧', 'consertar', ('fix', 'I fix the light.', 'Eu conserto a luz.'), ('fixes', 'The landlord fixes it.', 'O proprietário conserta.'), ('fixed', 'She fixed the door.', 'Ela consertou a porta.'), ('fixing', 'She is fixing the light.', 'Ela está consertando a luz.'), 'Fix leva -es na 3ª pessoa: fixes.'),
  vb('wash', '🧺', 'lavar', ('wash', 'I wash my clothes.', 'Eu lavo minhas roupas.'), ('washes', 'Evan washes his shirts.', 'O Evan lava as camisas.'), ('washed', 'We washed the towels.', 'Nós lavamos as toalhas.'), ('washing', 'I am washing my clothes.', 'Estou lavando minhas roupas.'), 'Wash leva -es: washes.'),
  vb('leave', '🚪', 'deixar / sair', ('leave', 'I leave the key here.', 'Eu deixo a chave aqui.'), ('leaves', 'She leaves at eight.', 'Ela sai às oito.'), ('left', 'He left the bag.', 'Ele deixou a mochila.'), ('leaving', 'I am leaving now.', 'Estou saindo agora.'), 'Leave é irregular: left no passado.'),
  vb('worry', '😟', 'preocupar-se', ('worry', 'I worry about the rent.', 'Eu me preocupo com o aluguel.'), ('worries', 'Evan worries a lot.', 'O Evan se preocupa muito.'), ('worried', 'She worried about the light.', 'Ela se preocupou com a luz.'), ('worrying', 'Stop worrying!', 'Pare de se preocupar!'), 'Worry vira worries e worried (y vira i).'),
  vb('throw', '🗑️', 'jogar fora', ('throw', 'I throw the trash away.', 'Eu jogo o lixo fora.'), ('throws', 'He throws the bag out.', 'Ele joga o saco fora.'), ('threw', 'She threw the box away.', 'Ela jogou a caixa fora.'), ('throwing', 'I am throwing the trash out.', 'Estou jogando o lixo fora.'), 'Throw é irregular: threw no passado. Throw away = jogar fora.')],
 verb_game=[
  dict(scene='O Evan lava as roupas agora.', en='Evan is ___ his clothes.', opts=['wash', 'washes', 'washing'], ans=2, pt='O Evan está lavando as roupas.', why='“is” + -ing: washing.'),
  dict(scene='A proprietária conserta a luz.', en='The landlord ___ the light.', opts=['fix', 'fixes', 'fixed'], ans=1, pt='A proprietária conserta a luz.', why='Ela (3ª pessoa) leva -es: fixes.'),
  dict(scene='Ontem você jogou o lixo fora.', en='Yesterday I ___ the trash away.', opts=['throw', 'throws', 'threw'], ans=2, pt='Ontem eu joguei o lixo fora.', why='Passado irregular de throw: threw.'),
  dict(scene='Você deixa a chave na mesa.', en='I ___ the key on the table.', opts=['leave', 'leaves', 'leaving'], ans=0, pt='Eu deixo a chave na mesa.', why='Com I, use o verbo base: leave.')],
 expressions=[
  dict(en='I’m your new tenant.', pt='Sou seu novo inquilino.', ex='Hi! I’m your new tenant.', exp='Para se apresentar ao proprietário.', c='a'),
  dict(en='Here’s your key.', pt='Aqui está sua chave.', ex='Welcome! Here’s your key.', exp='Para entregar a chave.', c='b'),
  dict(en='trash day', pt='dia do lixo', ex='What day is trash day?', exp='Para falar do dia da coleta de lixo.', c='c'),
  dict(en='Who do I call?', pt='Quem eu chamo?', ex='Who do I call for problems?', exp='Para saber a quem pedir ajuda.', c='d'),
  dict(en='Don’t worry.', pt='Não se preocupe.', ex='Don’t worry, I’ll fix it today.', exp='Para tranquilizar alguém.', c='a'),
  dict(en='heads up', pt='aviso, dica', ex='Heads up, trash day is Tuesday.', exp='Para dar um aviso rápido e informal.', c='b')],
 expr_game=[
  dict(cue='Você se apresenta como novo morador.', opts=['I’m your new tenant.', 'Don’t worry.', 'trash day'], ans=0, why='I’m your new tenant. apresenta o inquilino.'),
  dict(cue='Você quer saber a quem ligar em caso de problema.', opts=['Who do I call for problems?', 'Here’s your key.', 'heads up'], ans=0, why='Who do I call...? pergunta a quem pedir ajuda.'),
  dict(cue='Você tranquiliza o morador.', opts=['Don’t worry.', 'Here’s your key.', 'trash day'], ans=0, why='Don’t worry. = não se preocupe.')])
