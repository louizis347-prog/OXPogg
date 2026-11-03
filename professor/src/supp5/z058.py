"""Bloco de verbos e expressões da aula 058: comprar ingressos."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('buy', '🎟️', 'comprar', ('buy', 'We buy two tickets.', 'Nós compramos dois ingressos.'), ('buys', 'Mei buys a ticket.', 'A Mei compra um ingresso.'), ('bought', 'I bought a ticket.', 'Eu comprei um ingresso.'), ('buying', 'I am buying tickets.', 'Estou comprando ingressos.'), 'Buy vira bought no passado (irregular).'),
  vb('cost', '💲', 'custar', ('cost', 'The tickets cost forty dollars.', 'Os ingressos custam quarenta dólares.'), ('costs', 'A child ticket costs ten dollars.', 'Um ingresso infantil custa dez dólares.'), ('cost', 'The tour cost twenty dollars.', 'O passeio custou vinte dólares.'), ('costing', 'The tickets are costing more now.', 'Os ingressos estão custando mais agora.'), 'Cost é igual no passado. Com ele/ela: costs.'),
  vb('show', '🪪', 'mostrar', ('show', 'I show my student card.', 'Eu mostro minha carteirinha.'), ('shows', 'She shows her card.', 'Ela mostra a carteirinha.'), ('showed', 'He showed his ticket.', 'Ele mostrou o ingresso.'), ('showing', 'I am showing my card.', 'Estou mostrando minha carteirinha.'), 'Show é regular: showed. Show + o que + (to) quem.'),
  vb('start', '▶️', 'começar', ('start', 'The tours start at ten.', 'Os passeios começam às dez.'), ('starts', 'The tour starts at two.', 'O passeio começa às duas.'), ('started', 'The tour started late.', 'O passeio começou tarde.'), ('starting', 'The tour is starting now.', 'O passeio está começando agora.'), 'Start é regular. Com ele/ela: starts.'),
  vb('save', '🏷️', 'economizar', ('save', 'We save ten dollars.', 'Nós economizamos dez dólares.'), ('saves', 'The card saves money.', 'A carteirinha economiza dinheiro.'), ('saved', 'I saved five dollars.', 'Eu economizei cinco dólares.'), ('saving', 'I am saving money.', 'Estou economizando dinheiro.'), 'Save termina em e: saves, saved, saving (cai o e).')],
 verb_game=[
  dict(scene='O passeio começa às duas.', en='The tour ___ at two.', opts=['start', 'starts', 'starting'], ans=1, pt='O passeio começa às duas.', why='Com “the tour” (ele) o presente leva -s: starts.'),
  dict(scene='Ontem você comprou ingressos.', en='Yesterday I ___ two tickets.', opts=['buy', 'buys', 'bought'], ans=2, pt='Ontem eu comprei dois ingressos.', why='“Yesterday” pede passado: bought.'),
  dict(scene='Você mostra a carteirinha agora.', en='I am ___ my card.', opts=['show', 'showing', 'shows'], ans=1, pt='Estou mostrando minha carteirinha.', why='“am” + -ing: showing.'),
  dict(scene='Os ingressos custam quarenta dólares.', en='The tickets ___ forty dollars.', opts=['cost', 'costs', 'costing'], ans=0, pt='Os ingressos custam quarenta dólares.', why='“Tickets” é plural: cost, sem -s.')],
 expressions=[
  dict(en='Two tickets for the tour, please.', pt='Dois ingressos para o passeio, por favor.', ex='Hi! Two tickets for the tour, please.', exp='Para pedir ingressos no guichê.', c='a'),
  dict(en='Adults or children?', pt='Adultos ou crianças?', ex='Adults or children?', exp='O atendente pergunta quem vai.', c='b'),
  dict(en='That’s forty dollars.', pt='São quarenta dólares.', ex='That’s forty dollars. Cash or card?', exp='O atendente diz o preço.', c='c'),
  dict(en='student discount', pt='desconto de estudante', ex='Is there a student discount?', exp='Para perguntar por um preço menor.', c='d'),
  dict(en='Here you go.', pt='Aqui está.', ex='Here you go. Forty dollars.', exp='Para entregar algo à pessoa.', c='a'),
  dict(en='What time is the tour?', pt='Que horas é o passeio?', ex='What time is the tour? — At two.', exp='Para perguntar o horário.', c='b')],
 expr_game=[
  dict(cue='Você quer pedir dois ingressos.', opts=['Two tickets for the tour, please.', 'That’s forty dollars.', 'Adults or children?'], ans=0, why='Número + tickets + for the tour + please.'),
  dict(cue='Você quer saber se existe preço menor para estudante.', opts=['Is there a student discount?', 'Here you go.', 'What time is the tour?'], ans=0, why='Student discount = desconto de estudante.'),
  dict(cue='Você quer saber o horário do passeio.', opts=['What time is the tour?', 'Adults or children?', 'That’s forty dollars.'], ans=0, why='What time…? pergunta a hora.')])
