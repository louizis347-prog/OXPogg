"""Bloco de verbos e expressões da aula 9."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('work', '💼', 'trabalhar', ('work', 'I work in a restaurant.', 'Eu trabalho em um restaurante.'), ('works', 'Tony works at night.', 'O Tony trabalha à noite.'), ('worked', 'She worked all day.', 'Ela trabalhou o dia todo.'), ('working', 'I am working today.', 'Estou trabalhando hoje.'), 'Work in + lugar fechado; work at + empresa. Passado: worked.'),
  vb('cook', '👨‍🍳', 'cozinhar', ('cook', 'I cook pasta.', 'Eu cozinho macarrão.'), ('cooks', 'Tony cooks lunch.', 'O Tony faz o almoço.'), ('cooked', 'He cooked dinner.', 'Ele fez o jantar.'), ('cooking', 'I am cooking now.', 'Estou cozinhando agora.'), 'Passado só com -ed: cooked.'),
  vb('teach', '🍎', 'ensinar', ('teach', 'I teach English.', 'Eu ensino inglês.'), ('teaches', 'Maria teaches children.', 'A Maria ensina crianças.'), ('taught', 'She taught math.', 'Ela ensinou matemática.'), ('teaching', 'I am teaching today.', 'Estou dando aula hoje.'), 'Irregular: teach vira taught; ele/ela usa teaches.'),
  vb('help', '🤝', 'ajudar', ('help', 'I help people.', 'Eu ajudo pessoas.'), ('helps', 'Anna helps patients.', 'A Anna ajuda pacientes.'), ('helped', 'He helped a customer.', 'Ele ajudou um cliente.'), ('helping', 'I am helping a customer.', 'Estou ajudando um cliente.'), 'Passado só com -ed: helped.'),
  vb('like', '👍', 'gostar', ('like', 'I like my job.', 'Eu gosto do meu trabalho.'), ('likes', 'Sam likes his job.', 'O Sam gosta do trabalho dele.'), ('liked', 'She liked the restaurant.', 'Ela gostou do restaurante.'), ('liking', 'I am liking this job.', 'Estou gostando deste trabalho.'), 'Do you like your job? = Você gosta do seu trabalho?')],
 verb_game=[
  dict(scene='Você trabalha em um restaurante.', en='I ___ in a restaurant.', opts=['work', 'works', 'worked'], ans=0, pt='Eu trabalho em um restaurante.', why='Com “I” o presente é work.'),
  dict(scene='A Maria dá aula.', en='Maria ___ English to children.', opts=['teach', 'teaches', 'taught'], ans=1, pt='A Maria ensina inglês para crianças.', why='Com “Maria” (ela) o presente é teaches.'),
  dict(scene='Ontem o Tony fez o almoço.', en='Yesterday Tony ___ lunch.', opts=['cooks', 'cooking', 'cooked'], ans=2, pt='Ontem o Tony fez o almoço.', why='“Yesterday” pede passado: cooked.'),
  dict(scene='Agora você está ajudando um cliente.', en='I am ___ a customer.', opts=['helping', 'help', 'helps'], ans=0, pt='Estou ajudando um cliente.', why='“am” + verbo termina em -ing: helping.')],
 expressions=[
  dict(en='What do you do?', pt='O que você faz (de trabalho)?', ex='What do you do, Maria?', exp='Para perguntar a profissão.', c='a'),
  dict(en='I’m a…', pt='Eu sou…', ex='I’m a teacher.', exp='Para dizer sua profissão (com a/an).', c='b'),
  dict(en='I work in/at…', pt='Eu trabalho em…', ex='I work in a restaurant.', exp='Para dizer onde você trabalha.', c='c'),
  dict(en='Do you like your job?', pt='Você gosta do seu trabalho?', ex='Do you like your job?', exp='Para puxar conversa sobre trabalho.', c='d'),
  dict(en='It’s busy but fun.', pt='É corrido, mas divertido.', ex='It’s busy but fun.', exp='Para descrever o trabalho.', c='a'),
  dict(en='Come for lunch!', pt='Venha almoçar!', ex='Come for lunch on Friday!', exp='Para convidar alguém ao seu local de trabalho.', c='b')],
 expr_game=[
  dict(cue='Você quer saber a profissão dele.', opts=['What do you do?', 'I’m a nurse.', 'Come for lunch!'], ans=0, why='What do you do? pergunta a profissão.'),
  dict(cue='Você é professor e responde.', opts=['I’m a teacher.', 'I work busy.', 'Do you like it?'], ans=0, why='I’m a + profissão.'),
  dict(cue='Você quer saber se ela gosta do emprego.', opts=['Do you like your job?', 'What do you do?', 'I work in a hospital.'], ans=0, why='Do you like…? pergunta sobre gosto.')])
