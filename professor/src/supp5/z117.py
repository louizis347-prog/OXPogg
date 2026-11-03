"""Bloco de verbos e expressões da aula 117: ajuda com a lição."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('help', '🤝', 'ajudar', ('help', 'I help my brother.', 'Eu ajudo meu irmão.'), ('helps', 'Mom helps me with math.', 'A mamãe me ajuda com matemática.'), ('helped', 'She helped me yesterday.', 'Ela me ajudou ontem.'), ('helping', 'She is helping me now.', 'Ela está me ajudando agora.'), 'Help someone with something: help me with my homework.'),
  vb('count', '🔢', 'contar (números)', ('count', 'We count to ten.', 'Nós contamos até dez.'), ('counts', 'Leo counts on his fingers.', 'O Leo conta nos dedos.'), ('counted', 'I counted the pages.', 'Eu contei as páginas.'), ('counting', 'I am counting the numbers.', 'Estou contando os números.'), 'Count serve para números; “contar uma história” é tell.'),
  vb('solve', '🧩', 'resolver', ('solve', 'I solve one problem.', 'Eu resolvo um problema.'), ('solves', 'Anna solves it fast.', 'A Anna resolve rápido.'), ('solved', 'He solved number six.', 'Ele resolveu a número seis.'), ('solving', 'I am solving number five.', 'Estou resolvendo a número cinco.'), 'Solve a problem = resolver um exercício ou problema.'),
  vb('finish', '🏁', 'terminar', ('finish', 'We finish at five.', 'Nós terminamos às cinco.'), ('finishes', 'Leo finishes his homework.', 'O Leo termina a lição.'), ('finished', 'I finished page ten.', 'Eu terminei a página dez.'), ('finishing', 'I am finishing now.', 'Estou terminando agora.'), 'Com ele/ela, finish vira finishes (-es depois de sh).'),
  vb('practice', '🔁', 'praticar', ('practice', 'I practice English every day.', 'Eu pratico inglês todo dia.'), ('practices', 'She practices math.', 'Ela pratica matemática.'), ('practiced', 'We practiced a lot.', 'Nós praticamos muito.'), ('practicing', 'I am practicing numbers.', 'Estou praticando números.'), 'Practice termina com -ice; o passado é practiced.')],
 verb_game=[
  dict(scene='Toda tarde a mãe ajuda o Leo.', en='Mom ___ Leo with math every afternoon.', opts=['help', 'helps', 'helped'], ans=1, pt='A mãe ajuda o Leo com matemática toda tarde.', why='Com “Mom” (ela), o presente leva -s: helps.'),
  dict(scene='Ontem você terminou a página dez.', en='Yesterday I ___ page ten.', opts=['finish', 'finished', 'finishing'], ans=1, pt='Ontem eu terminei a página dez.', why='“Yesterday” pede passado: finished.'),
  dict(scene='Agora o Leo está resolvendo o exercício.', en='Leo is ___ number five.', opts=['solve', 'solves', 'solving'], ans=2, pt='O Leo está resolvendo a número cinco.', why='“is” + verbo termina em -ing: solving.'),
  dict(scene='Vocês contam juntos até vinte.', en='We ___ to twenty together.', opts=['count', 'counts', 'counted'], ans=0, pt='Nós contamos até vinte juntos.', why='Com “we”, o presente fica na forma base: count.')],
 expressions=[
  dict(en='Can you help me with…?', pt='Pode me ajudar com…?', ex='Can you help me with my homework?', exp='Para pedir ajuda com uma tarefa.', c='a'),
  dict(en='I don’t understand…', pt='Não entendo…', ex='I don’t understand number five.', exp='Para dizer exatamente o que está difícil.', c='b'),
  dict(en='Let’s … together.', pt='Vamos … juntos.', ex='Let’s read it together.', exp='Para propor fazer algo com outra pessoa.', c='c'),
  dict(en='Is it correct?', pt='Está certo?', ex='I wrote it. Is it correct?', exp='Para conferir uma resposta.', c='d'),
  dict(en='Practice makes perfect.', pt='A prática leva à perfeição.', ex='Don’t give up. Practice makes perfect.', exp='Para incentivar quem está aprendendo.', c='a'),
  dict(en='Great job!', pt='Ótimo trabalho!', ex='Yes, great job!', exp='Elogio simples e comum.', c='b')],
 expr_game=[
  dict(cue='Você quer saber se sua resposta está certa.', opts=['Is it correct?', 'Great job!', 'Let’s read it together.'], ans=0, why='Is it correct? confere uma resposta.'),
  dict(cue='Você precisa de ajuda com a lição.', opts=['Practice makes perfect.', 'Can you help me with my homework?', 'Great job!'], ans=1, why='Can you help me with…? pede ajuda.'),
  dict(cue='Um amigo quer desistir do exercício. Você anima.', opts=['I don’t understand.', 'Is it correct?', 'Practice makes perfect.'], ans=2, why='Practice makes perfect incentiva a continuar.')])
