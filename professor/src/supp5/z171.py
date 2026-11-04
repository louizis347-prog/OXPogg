"""Bloco de verbos e expressões da aula 171: reservar uma mesa."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('book', '📅', 'reservar', ('book', 'I book a table for four.', 'Eu reservo uma mesa para quatro.'), ('books', 'Alma books a table.', 'A Alma reserva uma mesa.'), ('booked', 'We booked the patio.', 'Nós reservamos o pátio.'), ('booking', 'I am booking a table.', 'Estou reservando uma mesa.'), 'Book = reservar (mesa, quarto, voo). Passado regular: booked.'),
  vb('reserve', '🍽️', 'reservar', ('reserve', 'We reserve a table for six.', 'Nós reservamos uma mesa para seis.'), ('reserves', 'Leo reserves a quiet table.', 'O Leo reserva uma mesa tranquila.'), ('reserved', 'I reserved a table for Friday.', 'Eu reservei uma mesa para sexta.'), ('reserving', 'I am reserving a table now.', 'Estou reservando uma mesa agora.'), 'Reserve soa um pouco mais formal que book; os dois servem.'),
  vb('confirm', '✅', 'confirmar', ('confirm', 'I confirm the time.', 'Eu confirmo o horário.'), ('confirms', 'Cole confirms the table.', 'O Cole confirma a mesa.'), ('confirmed', 'They confirmed my name.', 'Eles confirmaram meu nome.'), ('confirming', 'I am confirming my booking.', 'Estou confirmando minha reserva.'), 'Confirm termina em -m: só acrescente -s, -ed ou -ing.'),
  vb('cancel', '❌', 'cancelar', ('cancel', 'I cancel the table.', 'Eu cancelo a mesa.'), ('cancels', 'Alma cancels the dinner.', 'A Alma cancela o jantar.'), ('canceled', 'We canceled our booking.', 'Nós cancelamos nossa reserva.'), ('canceling', 'I am canceling Friday.', 'Estou cancelando sexta.'), 'Nos EUA, escreve-se canceled e canceling, com um só l.'),
  vb('arrive', '🚪', 'chegar', ('arrive', 'We arrive at seven.', 'Nós chegamos às sete.'), ('arrives', 'Leo arrives late.', 'O Leo chega tarde.'), ('arrived', 'They arrived on time.', 'Eles chegaram na hora.'), ('arriving', 'I am arriving now.', 'Estou chegando agora.'), 'Arrive at + horário ou lugar pequeno; arrive in + cidade.')],
 verb_game=[
  dict(scene='Você está ligando agora para reservar.', en='I am ___ a table for four.', opts=['book', 'booking', 'booked'], ans=1, pt='Estou reservando uma mesa para quatro.', why='“am” + verbo termina em -ing: booking.'),
  dict(scene='Ontem a Alma reservou o pátio.', en='Yesterday Alma ___ the patio.', opts=['books', 'booking', 'booked'], ans=2, pt='Ontem a Alma reservou o pátio.', why='“Yesterday” pede passado: booked.'),
  dict(scene='O Cole confirma a mesa toda vez.', en='Cole ___ the table every time.', opts=['confirm', 'confirms', 'confirmed'], ans=1, pt='O Cole confirma a mesa toda vez.', why='Com Cole (ele), o presente leva -s: confirms.'),
  dict(scene='Vocês chegam às sete.', en='We ___ at seven.', opts=['arrive', 'arrives', 'arriving'], ans=0, pt='Nós chegamos às sete.', why='Com “we”, o presente fica na forma base: arrive.')],
 expressions=[
  dict(en='Table for four', pt='Mesa para quatro', ex='A table for four, please.', exp='Para dizer quantas pessoas vão sentar.', c='a'),
  dict(en='Booked solid', pt='Totalmente lotado', ex='Friday is booked solid.', exp='Quando não há nenhuma mesa livre em um dia.', c='b'),
  dict(en='Walk-ins welcome', pt='Aceitamos sem reserva', ex='The sign says walk-ins welcome.', exp='Aviso de que você pode chegar sem reservar.', c='c'),
  dict(en='Let me check.', pt='Deixe-me ver.', ex='Let me check. Yes, we have a table.', exp='Para pedir um instante enquanto olha a agenda.', c='d'),
  dict(en='Hold the line.', pt='Aguarde na linha.', ex='Hold the line, please.', exp='Pedido ao telefone para esperar um momento.', c='a'),
  dict(en='Any vacancies?', pt='Tem vaga?', ex='Any vacancies for tonight?', exp='Pergunta usada em hotéis para saber se há quartos livres.', c='b')],
 expr_game=[
  dict(cue='Você quer dizer quantas pessoas vão jantar.', opts=['Table for four, please.', 'Hold the line.', 'Let me check.'], ans=0, why='Table for + número diz o tamanho do grupo.'),
  dict(cue='Você atende ao telefone e precisa olhar a agenda.', opts=['Walk-ins welcome.', 'Let me check.', 'Booked solid.'], ans=1, why='Let me check pede um instante para conferir.'),
  dict(cue='O restaurante diz que não tem nenhuma mesa livre no sábado.', opts=['Saturday is booked solid.', 'Table for four.', 'Hold the line.'], ans=0, why='Booked solid = totalmente lotado.')])
