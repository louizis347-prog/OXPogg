"""Bloco de verbos e expressões da aula 114: grupo de estudos."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('study', '📚', 'estudar', ('study', 'We study on Tuesday.', 'Nós estudamos na terça.'), ('studies', 'Mia studies grammar.', 'A Mia estuda gramática.'), ('studied', 'I studied for an hour.', 'Eu estudei por uma hora.'), ('studying', 'I am studying words.', 'Estou estudando palavras.'), 'Study muda o y: studies, studied.'),
  vb('practice', '🏋️', 'praticar', ('practice', 'I practice every day.', 'Eu pratico todo dia.'), ('practices', 'Jordan practices English.', 'O Jordan pratica inglês.'), ('practiced', 'We practiced new words.', 'Nós praticamos palavras novas.'), ('practicing', 'I am practicing now.', 'Estou praticando agora.'), 'Nos EUA, practice é o verbo e o substantivo.'),
  vb('join', '🤝', 'entrar, juntar-se', ('join', 'You join our group.', 'Você entra no nosso grupo.'), ('joins', 'Mia joins the class.', 'A Mia entra na aula.'), ('joined', 'She joined last week.', 'Ela entrou semana passada.'), ('joining', 'I am joining the group.', 'Estou entrando no grupo.'), 'Join não leva “in”: join a group.'),
  vb('meet', '📍', 'encontrar-se', ('meet', 'We meet at five.', 'Nós nos encontramos às cinco.'), ('meets', 'The group meets here.', 'O grupo se encontra aqui.'), ('met', 'We met in the library.', 'Nós nos encontramos na biblioteca.'), ('meeting', 'We are meeting now.', 'Estamos nos encontrando agora.'), 'Irregular: meet vira met no passado.'),
  vb('review', '🔁', 'revisar', ('review', 'We review the words.', 'Nós revisamos as palavras.'), ('reviews', 'Jordan reviews his notes.', 'O Jordan revisa suas anotações.'), ('reviewed', 'I reviewed the lesson.', 'Eu revisei a lição.'), ('reviewing', 'I am reviewing grammar.', 'Estou revisando a gramática.'), 'Review é “revisar”, não “rever” um filme.')],
 verb_game=[
  dict(scene='O Jordan estuda gramática toda semana.', en='Jordan ___ grammar every week.', opts=['study', 'studies', 'studied'], ans=1, pt='O Jordan estuda gramática toda semana.', why='Com “Jordan” (ele), study vira studies.'),
  dict(scene='Ontem o grupo se encontrou na biblioteca.', en='Yesterday we ___ in the library.', opts=['meet', 'met', 'meeting'], ans=1, pt='Ontem nós nos encontramos na biblioteca.', why='“Yesterday” pede passado; meet vira met.'),
  dict(scene='Agora você pratica inglês.', en='I am ___ English now.', opts=['practice', 'practices', 'practicing'], ans=2, pt='Estou praticando inglês agora.', why='“am” + verbo termina em -ing: practicing.'),
  dict(scene='Vocês revisam as palavras juntos.', en='We ___ the words together.', opts=['review', 'reviews', 'reviewed'], ans=0, pt='Nós revisamos as palavras juntos.', why='Com “we”, o presente fica na forma base: review.')],
 expressions=[
  dict(en='Want to join us?', pt='Quer se juntar a nós?', ex='We study at five. Want to join us?', exp='Convite informal para um grupo.', c='a'),
  dict(en='When do you meet?', pt='Quando vocês se encontram?', ex='When do you meet, and where?', exp='Para saber dia e hora do grupo.', c='b'),
  dict(en='I need practice.', pt='Preciso de prática.', ex='I need practice with speaking.', exp='Para explicar por que você quer estudar.', c='c'),
  dict(en='Bring your notebook.', pt='Traga seu caderno.', ex='Bring your notebook and a pen.', exp='Para dizer o que o outro deve levar.', c='d'),
  dict(en='quiz each other', pt='fazer perguntas um ao outro', ex='Let’s quiz each other on words.', exp='Atividade comum em grupos de estudo.', c='a'),
  dict(en='Good luck!', pt='Boa sorte!', ex='Good luck on the exam!', exp='Para desejar sucesso antes de uma prova.', c='b')],
 expr_game=[
  dict(cue='Você quer saber o dia e a hora do grupo.', opts=['When do you meet?', 'Bring your notebook.', 'Good luck!'], ans=0, why='When do you meet? pergunta a hora e o dia.'),
  dict(cue='Um colega vai fazer uma prova amanhã.', opts=['Want to join us?', 'I need practice.', 'Good luck!'], ans=2, why='Good luck! deseja sucesso.'),
  dict(cue='Você quer chamar um colega para estudar com vocês.', opts=['Want to join us?', 'Quiz each other.', 'When do you meet?'], ans=0, why='Want to join us? é o convite.')])
