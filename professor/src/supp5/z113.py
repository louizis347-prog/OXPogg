"""Bloco de verbos e expressões da aula 113: matrícula em uma aula."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('enroll', '📝', 'matricular-se', ('enroll', 'We enroll in July.', 'Nós nos matriculamos em julho.'), ('enrolls', 'Leo enrolls in a class.', 'O Leo se matricula em uma aula.'), ('enrolled', 'She enrolled last week.', 'Ela se matriculou semana passada.'), ('enrolling', 'I am enrolling today.', 'Estou me matriculando hoje.'), 'Enroll in + aula. Passado regular: enrolled (dois l).'),
  vb('attend', '🎒', 'frequentar / assistir', ('attend', 'I attend class at night.', 'Eu frequento a aula à noite.'), ('attends', 'Ana attends every lesson.', 'A Ana frequenta toda aula.'), ('attended', 'He attended the first class.', 'Ele foi à primeira aula.'), ('attending', 'I am attending a class now.', 'Estou assistindo a uma aula agora.'), 'Attend não é “atender”: significa estar presente em uma aula.'),
  vb('fill out', '📋', 'preencher', ('fill out', 'You fill out the form.', 'Você preenche o formulário.'), ('fills out', 'Leo fills out the form.', 'O Leo preenche o formulário.'), ('filled out', 'I filled out the page.', 'Eu preenchi a página.'), ('filling out', 'She is filling out a form.', 'Ela está preenchendo um formulário.'), 'Fill out + formulário. O objeto pode ficar no meio: fill it out.'),
  vb('sign', '✍️', 'assinar', ('sign', 'I sign my name here.', 'Eu assino meu nome aqui.'), ('signs', 'Kai signs the paper.', 'A Kai assina o papel.'), ('signed', 'He signed the form.', 'Ele assinou o formulário.'), ('signing', 'I am signing now.', 'Estou assinando agora.'), 'Sign your name = assinar seu nome. Passado regular: signed.'),
  vb('register', '🗂️', 'inscrever-se', ('register', 'We register at the office.', 'Nós nos inscrevemos na secretaria.'), ('registers', 'Tom registers online.', 'O Tom se inscreve on-line.'), ('registered', 'She registered for math.', 'Ela se inscreveu em matemática.'), ('registering', 'I am registering for a class.', 'Estou me inscrevendo em uma aula.'), 'Register for = inscrever-se em. É quase igual a enroll.')],
 verb_game=[
  dict(scene='O Leo preenche o formulário agora.', en='Leo ___ the form.', opts=['fill out', 'fills out', 'filled out'], ans=1, pt='O Leo preenche o formulário.', why='Com “Leo” (ele), o presente leva -s: fills out.'),
  dict(scene='Semana passada você se matriculou.', en='Last week I ___ in a class.', opts=['enroll', 'enrolled', 'enrolling'], ans=1, pt='Semana passada eu me matriculei em uma aula.', why='“Last week” pede passado: enrolled.'),
  dict(scene='Agora a Kai assina o papel.', en='Kai is ___ the paper.', opts=['sign', 'signs', 'signing'], ans=2, pt='A Kai está assinando o papel.', why='“is” + verbo termina em -ing: signing.'),
  dict(scene='Vocês frequentam a aula à noite.', en='We ___ class at night.', opts=['attend', 'attends', 'attended'], ans=0, pt='Nós frequentamos a aula à noite.', why='Com “we”, o presente fica na forma base: attend.')],
 expressions=[
  dict(en='I’d like to enroll.', pt='Eu gostaria de me matricular.', ex='I’d like to enroll in an art class.', exp='Para dizer que quer entrar em uma aula.', c='a'),
  dict(en='What’s the schedule?', pt='Qual é o horário?', ex='What’s the schedule for this class?', exp='Para saber dias e horas.', c='b'),
  dict(en='How much is it?', pt='Quanto custa?', ex='How much is the class?', exp='Para perguntar o preço.', c='c'),
  dict(en='Can I pay in parts?', pt='Posso pagar em partes?', ex='Can I pay in two parts?', exp='Para pedir pagamento parcelado.', c='d'),
  dict(en='sign up', pt='inscrever-se', ex='I want to sign up for yoga.', exp='Verbo frasal comum para se inscrever.', c='a'),
  dict(en='first come, first served', pt='quem chega primeiro é atendido', ex='It is first come, first served.', exp='Muito usado quando as vagas são limitadas.', c='b')],
 expr_game=[
  dict(cue='Você quer saber o preço da aula.', opts=['What’s the schedule?', 'How much is it?', 'I’d like to enroll.'], ans=1, why='How much is it? pergunta o preço.'),
  dict(cue='Você quer entrar em uma aula de arte.', opts=['I’d like to enroll in an art class.', 'Can I pay in parts?', 'How much is it?'], ans=0, why='I’d like to enroll… pede a matrícula.'),
  dict(cue='Você acha o valor alto e quer dividir.', opts=['What’s the schedule?', 'Can I pay in parts?', 'Sign up.'], ans=1, why='Can I pay in parts? pede o parcelamento.')])
