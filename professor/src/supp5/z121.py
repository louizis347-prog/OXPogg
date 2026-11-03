"""Bloco de verbos e expressões da aula 121: conversa com a professora."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('talk', '💬', 'conversar', ('talk', 'We talk about school.', 'Nós conversamos sobre a escola.'), ('talks', 'She talks to the teacher.', 'Ela conversa com a professora.'), ('talked', 'I talked to Ms. Lane.', 'Eu conversei com a Ms. Lane.'), ('talking', 'We are talking now.', 'Estamos conversando agora.'), 'Talk to alguém = conversar com. Talk about algo = falar sobre.'),
  vb('study', '📖', 'estudar', ('study', 'Kids study at school.', 'As crianças estudam na escola.'), ('studies', 'Anna studies every night.', 'A Anna estuda toda noite.'), ('studied', 'He studied for a test.', 'Ele estudou para uma prova.'), ('studying', 'She is studying math.', 'Ela está estudando matemática.'), 'Study muda para studies (y vira ies) e studied.'),
  vb('help', '🤝', 'ajudar', ('help', 'I help my son at home.', 'Eu ajudo meu filho em casa.'), ('helps', 'The teacher helps him.', 'A professora o ajuda.'), ('helped', 'She helped with homework.', 'Ela ajudou na lição de casa.'), ('helping', 'I am helping Leo.', 'Estou ajudando o Leo.'), 'Help + pessoa: help him, help her.'),
  vb('read', '📚', 'ler', ('read', 'We read at night.', 'Nós lemos à noite.'), ('reads', 'He reads a book.', 'Ele lê um livro.'), ('read', 'She read a story.', 'Ela leu uma história.'), ('reading', 'He is reading now.', 'Ele está lendo agora.'), 'No passado, read se escreve igual, mas se fala “réd”.'),
  vb('practice', '✏️', 'praticar', ('practice', 'They practice every day.', 'Eles praticam todo dia.'), ('practices', 'She practices spelling.', 'Ela pratica a escrita.'), ('practiced', 'He practiced math.', 'Ele praticou matemática.'), ('practicing', 'I am practicing English.', 'Estou praticando inglês.'), 'Practice termina em e: practicing perde o e.')],
 verb_game=[
  dict(scene='A professora conversa com os pais hoje.', en='Ms. Lane ___ to the parents.', opts=['talk', 'talks', 'talked'], ans=1, pt='A Ms. Lane conversa com os pais.', why='Com ela, o presente leva -s: talks.'),
  dict(scene='Ontem a filha leu uma história.', en='Yesterday she ___ a story.', opts=['reads', 'read', 'reading'], ans=1, pt='Ontem ela leu uma história.', why='Yesterday pede passado: read.'),
  dict(scene='Agora você está ajudando seu filho.', en='I am ___ my son.', opts=['help', 'helps', 'helping'], ans=2, pt='Estou ajudando meu filho.', why='am + verbo termina em -ing.'),
  dict(scene='Anna estuda toda noite.', en='Anna ___ every night.', opts=['studies', 'study', 'studied'], ans=0, pt='A Anna estuda toda noite.', why='Study vira studies com she/Anna.')],
 expressions=[
  dict(en='Please sit down.', pt='Sente-se, por favor.', ex='Hello! Please sit down.', exp='Para convidar alguém a sentar.', c='a'),
  dict(en='How is he in class?', pt='Como ele vai na aula?', ex='How is he in class?', exp='Para perguntar à professora sobre o aluno.', c='b'),
  dict(en='good student', pt='bom aluno', ex='She is a good student.', exp='Elogio simples para uma criança.', c='c'),
  dict(en='every day', pt='todo dia', ex='He reads every day.', exp='Para dizer que algo é rotina.', c='d'),
  dict(en='Is there anything…?', pt='Há algo…?', ex='Is there anything she needs?', exp='Para perguntar se falta alguma coisa.', c='a'),
  dict(en='Good job!', pt='Bom trabalho!', ex='Good job, Anna!', exp='Para elogiar uma criança.', c='b')],
 expr_game=[
  dict(cue='Você quer saber se a criança precisa de algo.', opts=['Is there anything she needs?', 'Please sit down.', 'Good job!'], ans=0, why='Is there anything…? pergunta se falta algo.'),
  dict(cue='Você quer elogiar o desenho de uma criança.', opts=['Every day.', 'Good job!', 'How is she in class?'], ans=1, why='Good job! é um elogio.'),
  dict(cue='Você quer saber como seu filho vai na escola.', opts=['How is he in class?', 'Please sit down.', 'He is a good student.'], ans=0, why='How is he…? pergunta como ele está indo.')])
