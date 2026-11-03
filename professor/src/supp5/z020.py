"""Bloco de verbos e expressões da aula 020."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('look', '👀', 'parecer / olhar', ('look', 'You look happy.', 'Você parece feliz.'), ('looks', 'She looks nice.', 'Ela parece simpática.'), ('looked', 'He looked tired.', 'Ele parecia cansado.'), ('looking', 'I am looking at her.', 'Estou olhando para ela.'), 'Look + adjetivo = parecer; look at = olhar para.'),
  vb('comb', '💇', 'pentear', ('comb', 'I comb my hair.', 'Eu penteio meu cabelo.'), ('combs', 'She combs her long hair.', 'Ela penteia o cabelo comprido.'), ('combed', 'He combed his hair.', 'Ele penteou o cabelo.'), ('combing', 'I am combing my hair.', 'Estou penteando meu cabelo.'), 'Comb = pentear; passado: combed.'),
  vb('wear', '👗', 'usar / vestir', ('wear', 'I wear glasses.', 'Eu uso óculos.'), ('wears', 'She wears a red dress.', 'Ela usa um vestido vermelho.'), ('wore', 'He wore a blue shirt.', 'Ele usava uma camisa azul.'), ('wearing', 'She is wearing a hat.', 'Ela está de chapéu.'), 'Irregular: wear, wore.'),
  vb('dress', '👔', 'vestir', ('dress', 'I dress for work.', 'Eu me visto para o trabalho.'), ('dresses', 'She dresses well.', 'Ela se veste bem.'), ('dressed', 'He dressed up for the party.', 'Ele se arrumou para a festa.'), ('dressing', 'I am dressing now.', 'Estou me vestindo agora.'), 'Com he/she: dresses (-es). Dress up = se arrumar.'),
  vb('know', '🧠', 'conhecer / saber', ('know', 'I know her.', 'Eu a conheço.'), ('knows', 'Tom knows that woman.', 'O Tom conhece aquela mulher.'), ('knew', 'I knew him.', 'Eu o conhecia.'), ('knowing', 'Thanks for knowing!', 'Obrigado por saber!'), 'Irregular: know, knew. Quase nunca com -ing.')],
 verb_game=[
  dict(scene='Ela penteia o cabelo comprido.', en='She ___ her long hair.', opts=['comb', 'combs', 'combed'], ans=1, pt='Ela penteia o cabelo comprido.', why='Com “she”: combs.'),
  dict(scene='Ela está de chapéu agora.', en='She is ___ a hat.', opts=['wear', 'wore', 'wearing'], ans=2, pt='Ela está de chapéu.', why='“is” + -ing: wearing.'),
  dict(scene='Ontem ele se arrumou para a festa.', en='He ___ up for the party yesterday.', opts=['dress', 'dresses', 'dressed'], ans=2, pt='Ontem ele se arrumou para a festa.', why='“Yesterday” pede passado: dressed.'),
  dict(scene='Ela parece simpática.', en='She ___ nice.', opts=['look', 'looks', 'looked'], ans=1, pt='Ela parece simpática.', why='Com “she”: looks.')],
 expressions=[
  dict(en='Who is that woman?', pt='Quem é aquela mulher?', ex='Who is that woman?', exp='Perguntar quem é alguém.', c='a'),
  dict(en='What does she look like?', pt='Como ela é?', ex='What does she look like?', exp='Perguntar a aparência.', c='b'),
  dict(en='She has long hair.', pt='Ela tem cabelo comprido.', ex='She has long, dark hair.', exp='Descrever o cabelo.', c='c'),
  dict(en='She is tall.', pt='Ela é alta.', ex='She is tall, with brown eyes.', exp='Descrever altura.', c='d'),
  dict(en='Come and meet her.', pt='Venha conhecê-la.', ex='Come and meet her.', exp='Apresentar alguém.', c='a'),
  dict(en='Nice to meet you.', pt='Prazer em conhecê-la.', ex='Hi! Nice to meet you.', exp='Cumprimento ao conhecer.', c='b')],
 expr_game=[
  dict(cue='Você quer saber quem é aquela mulher.', opts=['Who is that woman?', 'She is tall.', 'Nice to meet you.'], ans=0, why='Who is…? pergunta quem.'),
  dict(cue='Você quer saber como ela é fisicamente.', opts=['What does she look like?', 'Come and meet her.', 'Who is she?'], ans=0, why='What does… look like? descreve a aparência.'),
  dict(cue='Você acaba de ser apresentado a ela.', opts=['She has long hair.', 'Nice to meet you.', 'Who is that?'], ans=1, why='Nice to meet you. no primeiro encontro.')])
