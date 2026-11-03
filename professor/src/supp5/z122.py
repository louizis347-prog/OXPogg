"""Bloco de verbos e expressões da aula 122: fim da semana de trabalho."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('finish', '🏁', 'terminar', ('finish', 'We finish at five.', 'Nós terminamos às cinco.'), ('finishes', 'Leo finishes work early.', 'O Leo termina o trabalho cedo.'), ('finished', 'I finished my report.', 'Eu terminei meu relatório.'), ('finishing', 'I am finishing now.', 'Estou terminando agora.'), 'Finish vira finishes na 3ª pessoa (es depois de sh).'),
  vb('relax', '🛋️', 'relaxar', ('relax', 'I relax on Friday.', 'Eu relaxo na sexta.'), ('relaxes', 'She relaxes at home.', 'Ela relaxa em casa.'), ('relaxed', 'We relaxed on the sofa.', 'Nós relaxamos no sofá.'), ('relaxing', 'I am relaxing now.', 'Estou relaxando agora.'), 'Relax termina em x, então a 3ª pessoa é relaxes.'),
  vb('plan', '🗓️', 'planejar', ('plan', 'We plan a dinner.', 'Nós planejamos um jantar.'), ('plans', 'Leo plans the night.', 'O Leo planeja a noite.'), ('planned', 'I planned my weekend.', 'Eu planejei meu fim de semana.'), ('planning', 'We are planning dinner.', 'Estamos planejando o jantar.'), 'Plan dobra o n: planned, planning. Também existe o substantivo plans.'),
  vb('hope', '🤞', 'esperar (que), torcer', ('hope', 'I hope you are well.', 'Espero que você esteja bem.'), ('hopes', 'She hopes for a quiet night.', 'Ela espera uma noite tranquila.'), ('hoped', 'He hoped to leave early.', 'Ele esperava sair cedo.'), ('hoping', 'I am hoping for good news.', 'Estou torcendo por boas notícias.'), 'Hope = esperar com desejo. Esperar um ônibus é wait.'),
  vb('meet', '🤝', 'encontrar, conhecer', ('meet', 'We meet at the Italian place.', 'Nós nos encontramos no italiano.'), ('meets', 'Leo meets friends on Friday.', 'O Leo encontra amigos na sexta.'), ('met', 'I met Leo at seven.', 'Eu encontrei o Leo às sete.'), ('meeting', 'We are meeting at seven thirty.', 'Vamos nos encontrar às sete e meia.'), 'Passado irregular: meet vira met.')],
 verb_game=[
  dict(scene='Toda sexta o Leo termina cedo.', en='Leo ___ work early on Friday.', opts=['finish', 'finishes', 'finished'], ans=1, pt='O Leo termina o trabalho cedo na sexta.', why='Com Leo (ele), o presente leva -es: finishes.'),
  dict(scene='Ontem vocês se encontraram às sete.', en='Yesterday we ___ at seven.', opts=['meet', 'meets', 'met'], ans=2, pt='Ontem nos encontramos às sete.', why='Yesterday pede passado: met.'),
  dict(scene='Agora você está relaxando.', en='I am ___ on the sofa.', opts=['relax', 'relaxes', 'relaxing'], ans=2, pt='Estou relaxando no sofá.', why='am + verbo termina em -ing.'),
  dict(scene='Vocês planejam o jantar agora.', en='We are ___ dinner for tonight.', opts=['planning', 'plans', 'plan'], ans=0, pt='Estamos planejando o jantar de hoje à noite.', why='are + verbo-ing; plan dobra o n.')],
 expressions=[
  dict(en='TGIF!', pt='Graças a Deus é sexta!', ex='TGIF! I need a break.', exp='Gíria comum na sexta, entre colegas.', c='a'),
  dict(en='How was your week?', pt='Como foi sua semana?', ex='How was your week, Leo?', exp='Pergunta de conversa na sexta.', c='b'),
  dict(en='What are your plans?', pt='Quais são seus planos?', ex='What are your plans for tonight?', exp='Para perguntar o que alguém vai fazer.', c='c'),
  dict(en='Do you want to get dinner?', pt='Quer jantar comigo?', ex='Do you want to get dinner tonight?', exp='Um convite simples e amigável.', c='d'),
  dict(en='Let’s celebrate!', pt='Vamos comemorar!', ex='We finished. Let’s celebrate!', exp='Para festejar o fim de algo.', c='a'),
  dict(en='Sounds good.', pt='Combinado.', ex='Seven thirty? Sounds good.', exp='Para aceitar uma ideia ou horário.', c='b')],
 expr_game=[
  dict(cue='Você quer convidar um colega para jantar.', opts=['Do you want to get dinner tonight?', 'How was your week?', 'TGIF!'], ans=0, why='Do you want to…? é o convite.'),
  dict(cue='Você quer aceitar o horário que ele sugeriu.', opts=['What are your plans?', 'Sounds good.', 'Let’s celebrate!'], ans=1, why='Sounds good concorda com a ideia.'),
  dict(cue='Você quer saber o que ele vai fazer no fim de semana.', opts=['What are your plans?', 'Sounds good.', 'TGIF!'], ans=0, why='What are your plans? pergunta sobre planos.')])
