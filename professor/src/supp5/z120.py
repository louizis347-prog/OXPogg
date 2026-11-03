"""Bloco de verbos e expressões da aula 120: dia do voluntário."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('pick', '🧤', 'pegar, colher', ('pick', 'We pick up bottles.', 'Nós recolhemos garrafas.'), ('picks', 'Rosa picks up paper.', 'A Rosa recolhe papel.'), ('picked', 'I picked up five cans.', 'Eu recolhi cinco latas.'), ('picking', 'I am picking up trash.', 'Estou recolhendo lixo.'), 'Pick up = recolher do chão. Com ele/ela: picks (k + s).'),
  vb('collect', '🗑️', 'coletar, juntar', ('collect', 'We collect the bags.', 'Nós juntamos as sacolas.'), ('collects', 'He collects the bottles.', 'Ele junta as garrafas.'), ('collected', 'They collected ten bags.', 'Eles juntaram dez sacolas.'), ('collecting', 'I am collecting cans.', 'Estou juntando latas.'), 'Collect = juntar várias coisas em um lugar.'),
  vb('join', '🤝', 'participar, juntar-se a', ('join', 'We join the team.', 'Nós nos juntamos à equipe.'), ('joins', 'Tom joins Rosa.', 'O Tom se junta à Rosa.'), ('joined', 'My friend joined us.', 'Meu amigo se juntou a nós.'), ('joining', 'I am joining the cleanup.', 'Estou participando da limpeza.'), 'Join + pessoa/grupo, sem “to”: join us, join the team.'),
  vb('plant', '🌱', 'plantar', ('plant', 'We plant flowers.', 'Nós plantamos flores.'), ('plants', 'She plants a tree.', 'Ela planta uma árvore.'), ('planted', 'They planted ten trees.', 'Eles plantaram dez árvores.'), ('planting', 'I am planting flowers.', 'Estou plantando flores.'), 'Plant também é substantivo: uma planta.'),
  vb('rake', '🍂', 'juntar com rastelo', ('rake', 'We rake the leaves.', 'Nós juntamos as folhas.'), ('rakes', 'He rakes the grass.', 'Ele rasteleia a grama.'), ('raked', 'I raked the leaves.', 'Eu juntei as folhas.'), ('raking', 'I am raking the leaves.', 'Estou juntando as folhas.'), 'Rake é um verbo e também o nome da ferramenta (rastelo). No -ing o e cai: raking.')],
 verb_game=[
  dict(scene='A Rosa recolhe papel do chão.', en='Rosa ___ up paper from the grass.', opts=['pick', 'picks', 'picked'], ans=1, pt='A Rosa recolhe papel da grama.', why='Com “Rosa” (ela), o presente leva -s: picks.'),
  dict(scene='Ontem seu amigo se juntou ao grupo.', en='Yesterday my friend ___ the team.', opts=['join', 'joins', 'joined'], ans=2, pt='Ontem meu amigo se juntou à equipe.', why='“Yesterday” pede passado: joined.'),
  dict(scene='Agora você planta flores.', en='I am ___ flowers near the lake.', opts=['plant', 'plants', 'planting'], ans=2, pt='Estou plantando flores perto do lago.', why='“am” + verbo termina em -ing: planting.'),
  dict(scene='Vocês juntam as folhas todo ano.', en='We ___ the leaves every fall.', opts=['rake', 'rakes', 'raked'], ans=0, pt='Nós juntamos as folhas todo outono.', why='Com “we”, o presente fica na forma base: rake.')],
 expressions=[
  dict(en='What can I do?', pt='O que posso fazer?', ex='Yes! What can I do?', exp='Para oferecer ajuda e pedir uma tarefa.', c='a'),
  dict(en='Where do I start?', pt='Por onde começo?', ex='Thanks. Where do I start?', exp='Para pedir instrução sobre o começo.', c='b'),
  dict(en='pick up', pt='recolher, pegar', ex='Please pick up trash in the park.', exp='Verbo frasal: pegar algo do chão.', c='c'),
  dict(en='Many hands make light work.', pt='Muitas mãos tornam o trabalho leve.', ex='Right! Many hands make light work.', exp='Provérbio: em grupo, o trabalho é mais fácil.', c='d'),
  dict(en='pitch in', pt='ajudar, colaborar', ex='Let’s pitch in!', exp='Informal: todos ajudam com a tarefa.', c='a'),
  dict(en='give back', pt='retribuir à comunidade', ex='It feels great to give back.', exp='Ajudar a comunidade que ajudou você.', c='b')],
 expr_game=[
  dict(cue='Você chega e quer saber como ajudar.', opts=['Many hands make light work.', 'What can I do?', 'It feels great to give back.'], ans=1, why='What can I do? pede uma tarefa.'),
  dict(cue='Seu grupo é grande e o trabalho fica fácil.', opts=['Where do I start?', 'Many hands make light work.', 'pick up'], ans=1, why='O provérbio diz que em grupo o trabalho fica leve.'),
  dict(cue='Você quer saber por onde começar.', opts=['Where do I start?', 'What can I do?', 'Let’s pitch in!'], ans=0, why='Where do I start? pede o ponto de partida.')])
