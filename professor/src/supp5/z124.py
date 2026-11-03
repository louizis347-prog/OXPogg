"""Bloco de verbos e expressões da aula 124: marcar consulta."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('spell', '🔤', 'soletrar', ('spell', 'I spell my last name.', 'Eu soletro meu sobrenome.'), ('spells', 'Alex spells it slowly.', 'O Alex soletra devagar.'), ('spelled', 'She spelled her name.', 'Ela soletrou o nome dela.'), ('spelling', 'I am spelling it now.', 'Estou soletrando agora.'), 'Spell = soletrar. Pergunta comum: How do you spell it?'),
  vb('book', '📘', 'reservar, marcar', ('book', 'I book a time online.', 'Eu marco um horário on-line.'), ('books', 'Ana books a visit.', 'A Ana marca uma visita.'), ('booked', 'He booked Tuesday.', 'Ele marcou terça.'), ('booking', 'I am booking now.', 'Estou marcando agora.'), 'Book também é verbo: book a table, book a visit.'),
  vb('cancel', '❌', 'cancelar', ('cancel', 'We cancel the visit.', 'Nós cancelamos a visita.'), ('cancels', 'She cancels on Monday.', 'Ela cancela na segunda.'), ('canceled', 'I canceled my time.', 'Eu cancelei meu horário.'), ('canceling', 'I am canceling now.', 'Estou cancelando agora.'), 'Nos EUA, canceled; no inglês britânico, cancelled.'),
  vb('confirm', '✅', 'confirmar', ('confirm', 'I confirm the time.', 'Eu confirmo o horário.'), ('confirms', 'The office confirms it.', 'O consultório confirma.'), ('confirmed', 'They confirmed Tuesday.', 'Eles confirmaram terça.'), ('confirming', 'I am confirming now.', 'Estou confirmando agora.'), 'Confirm = confirmar. O acento fica em FIRM.'),
  vb('arrive', '🚪', 'chegar', ('arrive', 'We arrive at ten.', 'Nós chegamos às dez.'), ('arrives', 'Ana arrives early.', 'A Ana chega cedo.'), ('arrived', 'I arrived at nine.', 'Eu cheguei às nove.'), ('arriving', 'I am arriving now.', 'Estou chegando agora.'), 'Use arrive at para lugares e horas: arrive at ten.')],
 verb_game=[
  dict(scene='Ana quer um horário na terça e liga hoje.', en='Ana ___ an appointment for Tuesday.', opts=['book', 'books', 'booked'], ans=1, pt='A Ana marca uma consulta para terça.', why='Com Ana (ela), o presente leva -s: books.'),
  dict(scene='Ontem você cancelou o horário.', en='Yesterday I ___ my time.', opts=['cancel', 'cancels', 'canceled'], ans=2, pt='Ontem eu cancelei meu horário.', why='Yesterday pede passado: canceled.'),
  dict(scene='Agora você soletra seu sobrenome.', en='I am ___ my last name.', opts=['spell', 'spelling', 'spells'], ans=1, pt='Estou soletrando meu sobrenome.', why='am + verbo termina em -ing.'),
  dict(scene='Você chega ao consultório às dez.', en='I ___ at ten o’clock.', opts=['arrive', 'arrives', 'arriving'], ans=0, pt='Eu chego às dez.', why='Com I, o presente fica na forma base.')],
 expressions=[
  dict(en='make an appointment', pt='marcar uma consulta', ex='I’d like to make an appointment.', exp='Para marcar com médico, dentista ou escritório.', c='a'),
  dict(en='How do you spell…?', pt='Como se escreve…?', ex='How do you spell your last name?', exp='Para pedir as letras de um nome.', c='b'),
  dict(en='Do you have time on…?', pt='Vocês têm horário em…?', ex='Do you have time on Tuesday?', exp='Para perguntar por um dia.', c='c'),
  dict(en='Works for me.', pt='Serve para mim.', ex='Ten o’clock works for me.', exp='Para aceitar um horário.', c='d'),
  dict(en='You’re all set.', pt='Está tudo certo.', ex='Thanks, Alex. You’re all set.', exp='Quando o atendente termina o agendamento.', c='a'),
  dict(en='Put me down for…', pt='Anote-me para…', ex='Put me down for Monday.', exp='Para pedir que anotem seu nome em um dia.', c='b')],
 expr_game=[
  dict(cue='Você quer marcar um horário no médico.', opts=['I’d like to make an appointment.', 'You’re all set.', 'Works for me.'], ans=0, why='I’d like to make an appointment é o pedido educado.'),
  dict(cue='Você quer que ele diga as letras do nome.', opts=['Do you have time on Monday?', 'How do you spell your last name?', 'Put me down for Monday.'], ans=1, why='How do you spell…? pede a soletração.'),
  dict(cue='Os horários são dez ou duas e você gosta das dez.', opts=['Ten o’clock works for me.', 'How do you spell it?', 'I’d like to make an appointment.'], ans=0, why='Works for me aceita o horário.')])
