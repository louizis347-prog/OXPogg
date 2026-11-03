"""Bloco de verbos e expressões da aula 088: na praia."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('swim', '🏊', 'nadar', ('swim', 'We swim in the sea.', 'Nós nadamos no mar.'), ('swims', 'Serena swims fast.', 'A Serena nada rápido.'), ('swam', 'I swam for an hour.', 'Eu nadei por uma hora.'), ('swimming', 'They are swimming now.', 'Eles estão nadando agora.'), 'Swim é irregular: swam no passado. Dobra o m no -ing: swimming.'),
  vb('jump', '🤸', 'pular', ('jump', 'I jump over the waves.', 'Eu pulo as ondas.'), ('jumps', 'Nora jumps in the water.', 'A Nora pula na água.'), ('jumped', 'He jumped off the rock.', 'Ele pulou da pedra.'), ('jumping', 'The kids are jumping.', 'As crianças estão pulando.'), 'Passado regular: jumped.'),
  vb('dig', '⛏️', 'cavar', ('dig', 'We dig a hole in the sand.', 'Nós cavamos um buraco na areia.'), ('digs', 'The boy digs with a shovel.', 'O menino cava com uma pá.'), ('dug', 'She dug a big hole.', 'Ela cavou um buraco grande.'), ('digging', 'I am digging in the sand.', 'Estou cavando na areia.'), 'Dig é irregular: dug no passado. Dobra o g no -ing: digging.'),
  vb('build', '🏰', 'construir', ('build', 'We build a sand castle.', 'Nós construímos um castelo de areia.'), ('builds', 'A boy builds a wall.', 'Um menino constrói um muro.'), ('built', 'They built a small castle.', 'Eles construíram um castelo pequeno.'), ('building', 'I am building a tower.', 'Estou construindo uma torre.'), 'Build é irregular: built no passado.'),
  vb('wear', '🕶️', 'usar (roupa, óculos)', ('wear', 'I wear a hat at the beach.', 'Eu uso chapéu na praia.'), ('wears', 'Serena wears sunglasses.', 'A Serena usa óculos de sol.'), ('wore', 'Nora wore a red hat.', 'A Nora usou um chapéu vermelho.'), ('wearing', 'She is wearing sunscreen.', 'Ela está de protetor solar.'), 'Wear é irregular: wore no passado. Serve para roupa, chapéu e óculos.')],
 verb_game=[
  dict(scene='A Serena nada todo dia de manhã.', en='Serena ___ every morning.', opts=['swim', 'swims', 'swam'], ans=1, pt='A Serena nada toda manhã.', why='Com “Serena” (ela), o presente leva -s: swims.'),
  dict(scene='Ontem a Nora cavou um buraco.', en='Yesterday Nora ___ a big hole.', opts=['dig', 'dug', 'digging'], ans=1, pt='Ontem a Nora cavou um buraco grande.', why='“Yesterday” pede passado: dug.'),
  dict(scene='Agora o menino está construindo um castelo.', en='The boy is ___ a castle.', opts=['build', 'builds', 'building'], ans=2, pt='O menino está construindo um castelo.', why='“is” + verbo termina em -ing: building.'),
  dict(scene='Vocês pulam as ondas pequenas.', en='We ___ over small waves.', opts=['jump', 'jumps', 'jumped'], ans=0, pt='Nós pulamos ondas pequenas.', why='Com “we”, o presente fica na forma base: jump.')],
 expressions=[
  dict(en='What a beautiful beach!', pt='Que praia linda!', ex='Wow, what a beautiful beach!', exp='Para elogiar o lugar quando você chega.', c='a'),
  dict(en='Is the water cold?', pt='A água está fria?', ex='Is the water cold today?', exp='Para saber a temperatura antes de entrar.', c='b'),
  dict(en='I need sunscreen.', pt='Preciso de protetor solar.', ex='Wait. I need sunscreen.', exp='Para avisar que você precisa passar protetor.', c='c'),
  dict(en='Here, use mine.', pt='Toma, use o meu.', ex='Here, use mine. I have two.', exp='Para emprestar algo a alguém.', c='d'),
  dict(en='under the umbrella', pt='debaixo do guarda-sol', ex='The bag is under the umbrella.', exp='Para dizer onde algo está (under = debaixo).', c='a'),
  dict(en='Have fun!', pt='Divirta-se!', ex='Have fun at the beach!', exp='Despedida simpática antes de um passeio.', c='b')],
 expr_game=[
  dict(cue='Você quer saber se dá para nadar sem passar frio.', opts=['Is the water cold?', 'Have fun!', 'Here, use mine.'], ans=0, why='Is the water cold? pergunta a temperatura.'),
  dict(cue='Seu amigo esqueceu o protetor e você tem um extra.', opts=['What a beautiful beach!', 'Here, use mine.', 'I need sunscreen.'], ans=1, why='Here, use mine empresta algo seu.'),
  dict(cue='Você diz onde a toalha está: ao lado do guarda-sol.', opts=['Is the water cold?', 'I need sunscreen.', 'It’s under the umbrella.'], ans=2, why='under = debaixo; diz onde algo está.')])
