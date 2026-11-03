"""Bloco de verbos e expressões da aula 10."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('attend', '🎓', 'frequentar', ('attend', 'I attend class on Monday.', 'Eu frequento a aula na segunda.'), ('attends', 'Sam attends yoga on Friday.', 'O Sam frequenta ioga na sexta.'), ('attended', 'We attended class on Tuesday.', 'Nós fomos à aula na terça.'), ('attending', 'I am attending a new class.', 'Estou frequentando uma aula nova.'), 'Attend não leva “to”: attend class.'),
  vb('go', '🚶', 'ir', ('go', 'I go to class on Monday.', 'Eu vou à aula na segunda.'), ('goes', 'She goes to yoga on Friday.', 'Ela vai à ioga na sexta.'), ('went', 'We went on Saturday.', 'Nós fomos no sábado.'), ('going', 'I am going to class.', 'Estou indo à aula.'), 'Irregular: go vira went; ele/ela usa goes.'),
  vb('start', '▶️', 'começar', ('start', 'Class starts at six.', 'A aula começa às seis.'), ('starts', 'Yoga starts on Friday.', 'A ioga começa na sexta.'), ('started', 'The class started on Monday.', 'A aula começou na segunda.'), ('starting', 'I am starting a new class.', 'Estou começando uma aula nova.'), 'Com coisas no singular, starts: class starts.'),
  vb('study', '📖', 'estudar', ('study', 'I study on Thursday.', 'Eu estudo na quinta.'), ('studies', 'Lena studies on Sunday.', 'A Lena estuda no domingo.'), ('studied', 'We studied on Friday.', 'Nós estudamos na sexta.'), ('studying', 'I am studying now.', 'Estou estudando agora.'), 'Study vira studies e studied (y vira i).'),
  vb('book', '📅', 'reservar', ('book', 'I book a class online.', 'Eu reservo uma aula pela internet.'), ('books', 'Sam books yoga for Friday.', 'O Sam reserva ioga para sexta.'), ('booked', 'We booked a spot on Monday.', 'Nós reservamos uma vaga na segunda.'), ('booking', 'I am booking a class now.', 'Estou reservando uma aula agora.'), 'Book = reservar; passado: booked.')],
 verb_game=[
  dict(scene='Você frequenta aula toda segunda.', en='I ___ class on Mondays.', opts=['attend', 'attends', 'attended'], ans=0, pt='Eu frequento a aula às segundas.', why='Com “I” o presente é a forma base: attend.'),
  dict(scene='O Sam vai à ioga na sexta.', en='Sam ___ to yoga on Friday.', opts=['go', 'goes', 'went'], ans=1, pt='O Sam vai à ioga na sexta.', why='Com “Sam” (ele) o presente é goes.'),
  dict(scene='A aula começa às seis.', en='The class ___ at six.', opts=['start', 'starting', 'starts'], ans=2, pt='A aula começa às seis.', why='“The class” é singular: starts.'),
  dict(scene='Ontem você reservou uma vaga.', en='Yesterday I ___ a spot in class.', opts=['book', 'booked', 'booking'], ans=1, pt='Ontem eu reservei uma vaga na aula.', why='“Yesterday” pede passado: booked.')],
 expressions=[
  dict(en='What day is it today?', pt='Que dia é hoje?', ex='What day is it today?', exp='Para perguntar o dia da semana.', c='a'),
  dict(en='It’s Monday.', pt='É segunda-feira.', ex='It’s Monday.', exp='Para responder qual é o dia.', c='b'),
  dict(en='on Fridays', pt='às sextas', ex='I have yoga on Fridays.', exp='Para falar de algo que se repete toda semana.', c='c'),
  dict(en='When do you have class?', pt='Quando você tem aula?', ex='When do you have class?', exp='Para perguntar o dia ou horário.', c='d'),
  dict(en='What time?', pt='A que horas?', ex='Great! What time?', exp='Para perguntar a hora de um compromisso.', c='a'),
  dict(en='See you on Friday!', pt='Te vejo na sexta!', ex='Bye! See you on Friday!', exp='Para combinar de se ver de novo.', c='b')],
 expr_game=[
  dict(cue='Você esqueceu que dia é hoje.', opts=['What day is it today?', 'See you on Friday!', 'On Mondays.'], ans=0, why='What day is it today? pergunta o dia.'),
  dict(cue='Você quer saber o dia da aula dele.', opts=['When do you have class?', 'It’s Monday.', 'What time?'], ans=0, why='When do you…? pergunta quando.'),
  dict(cue='Você quer se despedir e voltar a vê-lo na sexta.', opts=['It’s Friday.', 'See you on Friday!', 'What day is it?'], ans=1, why='See you on + dia combina um novo encontro.')])
