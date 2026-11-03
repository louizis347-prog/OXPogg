"""Bloco de verbos e expressões da aula 064: quarto para alugar."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('call', '☎️', 'ligar', ('call', 'I call about the room.', 'Eu ligo sobre o quarto.'), ('calls', 'Ava calls Cole.', 'A Ava liga para o Cole.'), ('called', 'She called yesterday.', 'Ela ligou ontem.'), ('calling', 'I am calling about the room.', 'Estou ligando sobre o quarto.'), 'Call about = ligar sobre um assunto.'),
  vb('see', '👀', 'ver', ('see', 'I see the room.', 'Eu vejo o quarto.'), ('sees', 'Ava sees the desk.', 'A Ava vê a escrivaninha.'), ('saw', 'We saw the kitchen.', 'Nós vimos a cozinha.'), ('seeing', 'I am seeing the room tomorrow.', 'Vou ver o quarto amanhã.'), 'See é irregular: saw no passado. See it = ver o quarto.'),
  vb('ask', '❓', 'perguntar / pedir', ('ask', 'I ask about the rent.', 'Eu pergunto sobre o aluguel.'), ('asks', 'Ava asks about bills.', 'A Ava pergunta sobre as contas.'), ('asked', 'He asked the price.', 'Ele perguntou o preço.'), ('asking', 'I am asking about the room.', 'Estou perguntando sobre o quarto.'), 'Ask about = perguntar sobre.'),
  vb('pay', '💵', 'pagar', ('pay', 'I pay the rent.', 'Eu pago o aluguel.'), ('pays', 'Ava pays on Monday.', 'A Ava paga na segunda.'), ('paid', 'We paid the deposit.', 'Nós pagamos o depósito.'), ('paying', 'I am paying the bill.', 'Estou pagando a conta.'), 'Pay é irregular: paid no passado.'),
  vb('share', '🤝', 'dividir', ('share', 'We share the kitchen.', 'Nós dividimos a cozinha.'), ('shares', 'Ava shares a flat.', 'A Ava divide um apartamento.'), ('shared', 'They shared a room.', 'Eles dividiram um quarto.'), ('sharing', 'I am sharing a room.', 'Estou dividindo um quarto.'), 'Share perde o e antes de -ing: sharing.')],
 verb_game=[
  dict(scene='Você está ligando agora.', en='I am ___ about the room.', opts=['call', 'calls', 'calling'], ans=2, pt='Estou ligando sobre o quarto.', why='“am” + -ing: calling.'),
  dict(scene='Ontem a Ava viu o quarto.', en='Yesterday Ava ___ the room.', opts=['see', 'sees', 'saw'], ans=2, pt='Ontem a Ava viu o quarto.', why='Passado irregular de see: saw.'),
  dict(scene='A Ava paga o aluguel.', en='Ava ___ the rent every month.', opts=['pay', 'pays', 'paid'], ans=1, pt='A Ava paga o aluguel todo mês.', why='Ela (3ª pessoa) leva -s: pays.'),
  dict(scene='Você divide o apartamento.', en='We ___ a small flat.', opts=['share', 'shares', 'sharing'], ans=0, pt='Nós dividimos um apartamento pequeno.', why='Com we, use o verbo base: share.')],
 expressions=[
  dict(en='I’m calling about the room.', pt='Estou ligando sobre o quarto.', ex='Hi! I’m calling about the room for rent.', exp='Para abrir a ligação.', c='a'),
  dict(en='still available', pt='ainda disponível', ex='Is it still available?', exp='Para saber se algo continua livre.', c='b'),
  dict(en='How much is the rent?', pt='Quanto é o aluguel?', ex='How much is the rent a month?', exp='Para perguntar o preço do aluguel.', c='c'),
  dict(en='Are bills included?', pt='As contas estão incluídas?', ex='Are bills included in the rent?', exp='Para saber se as contas já estão no preço.', c='d'),
  dict(en='a month', pt='por mês', ex='It is eight hundred dollars a month.', exp='Para dar o valor mensal.', c='a'),
  dict(en='See you tomorrow!', pt='Até amanhã!', ex='Great. See you tomorrow at five!', exp='Despedida quando vocês vão se ver no dia seguinte.', c='b')],
 expr_game=[
  dict(cue='Você quer saber se o preço já tem as contas.', opts=['Are bills included?', 'See you tomorrow!', 'a month'], ans=0, why='Are... included? pergunta o que está no preço.'),
  dict(cue='Você quer saber se o quarto continua livre.', opts=['Is it still available?', 'How much is the rent?', 'See you tomorrow!'], ans=0, why='Still available = ainda disponível.'),
  dict(cue='Você se despede para se ver amanhã.', opts=['See you tomorrow!', 'Are bills included?', 'still available'], ans=0, why='See you tomorrow! é uma despedida com data.')])
