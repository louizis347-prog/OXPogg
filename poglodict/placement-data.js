const placementUse=[
[
 ['Nina ___ my neighbor.','is','are','am','be','Use is com um sujeito singular na terceira pessoa.'],
 ['There is ___ orange on the table.','an','a','some','many','Orange começa com som vocálico.'],
 ['We ___ work on Sundays.','don’t','doesn’t','aren’t','isn’t','Com we, use don’t + verbo base para negar um hábito.'],
 ['___ do you live?','Where','When','How many','Who','Where pergunta pelo lugar.'],
 ['You want the total price. What do you ask?','How much is it?','What time is it?','How old is it?','Where is it?','How much pergunta pelo preço.'],
 ['The shop is next to the bank. Where is it?','Beside the bank.','Far from the bank.','Inside the bank.','Across town.','Next to equivale a beside.']
],
[
 ['We ___ the bus yesterday.','took','take','have take','were take','Yesterday situa a ação concluída. O passado de take é took.'],
 ['Are there ___ cafés near the station?','any','a','much','an','Any é natural numa pergunta sobre substantivos contáveis no plural.'],
 ['This route is ___ than the old one.','shorter','short','shortest','as short','Use o comparativo shorter antes de than.'],
 ['She’s going ___ the doctor tomorrow.','to call','calling','call','called','Be going to + infinitivo descreve um plano.'],
 ['“I’d like to return this shirt.” What is the speaker doing?','Taking an item back to the store.','Trying on an item for the first time.','Asking the store to deliver an item.','Looking for a different store.','Return, nesse contexto, é devolver uma compra.'],
 ['The train is delayed. It will ___.','leave or arrive later than planned','never run again','arrive earlier than planned','go to a different country','Delayed indica atraso em relação ao horário previsto.']
],
[
 ['I ___ at this library since May.','have worked','work','had work','was worked','Since aponta para o início de uma situação que continua no presente.'],
 ['When you called, I ___ dinner.','was making','make','have made','am making','O passado contínuo apresenta uma ação em andamento na hora da ligação.'],
 ['If we miss the bus, we ___ a taxi.','will take','would have taken','took','had taken','Para uma condição futura possível, use presente após if e will na consequência.'],
 ['The bike ___ last week.','was repaired','has repair','was repairing','repairs','A passiva no passado usa was + particípio.'],
 ['We had to put off the meeting. What happened?','We postponed it.','We ended it early.','We attended it online.','We wrote up the minutes.','Put off equivale a postpone.'],
 ['“Can you look after my dog?” means ___.','Can you take care of my dog?','Can you find my dog?','Can you look at my dog?','Can you buy my dog?','Look after significa cuidar de alguém ou de algo.']
],
[
 ['I wish I ___ the answer.','knew','know','had know','will know','O passado depois de wish expressa uma situação presente desejada.'],
 ['By next Friday, we ___ the report.','will have finished','finished','have been finish','will finishing','O futuro perfeito situa a conclusão antes de um marco futuro.'],
 ['You ___ all that food; we already had enough.','needn’t have bought','must have bought','can’t have buy','shouldn’t buying','Needn’t have bought indica uma compra feita sem necessidade.'],
 ['The manager suggested ___ the deadline.','moving','to moving','move','have moved','Suggest admite verbo em -ing nessa construção.'],
 ['“We need a workaround.” What do they need?','An alternative way to get around a problem.','A written record of who caused the problem.','An immediate permanent repair.','A larger budget for the same approach.','Workaround contorna o problema, mesmo sem resolvê-lo de forma permanente.'],
 ['The new policy met with resistance. What happened?','Some people opposed it.','Everyone agreed immediately.','It was never announced.','It was too expensive to write.','Meet with resistance significa encontrar oposição.']
],
[
 ['Hardly ___ when the meeting began.','had we arrived','we had arrived','did we arrived','we did arrive','Hardly no início pede inversão do auxiliar e sujeito.'],
 ['The plan is viable, ___ its initial costs.','despite','although','whereas','even if','Despite admite sintagma nominal, como its initial costs.'],
 ['___ about the shortage, we would have ordered more.','Had we known','Were we knew','Did we know','Have we known','Had we known é inversão da condicional if we had known.'],
 ['It was the timetable, rather than the cost, ___ caused the delay.','that','what','which it','because','A clivagem it was X that destaca o fator responsável.'],
 ['The authors qualify their conclusion. What do they do?','They specify limits to what it claims.','They show that it passes an official test.','They eliminate all uncertainty.','They remove it from the report.','Qualify a claim é delimitá-la ou acrescentar ressalvas.'],
 ['“His assurance rang hollow.” What does this imply?','It did not sound sincere or convincing.','It was heard over a loudspeaker.','It was legally enforceable.','It addressed a completely different topic.','Ring hollow descreve algo que soa vazio ou pouco convincente.']
],
[
 ['Much as I ___ the result, I cannot endorse the method.','welcome','would welcoming','welcomed be','am welcome to','Much as introduz a concessão, seguida por uma oração com verbo conjugado.'],
 ['The findings are preliminary, ___ they should be treated with caution.','in which case','despite that therefore','whereupon that','which nonetheless it','In which case retoma o fato anterior e introduz sua consequência.'],
 ['Only after the samples were rechecked ___ apparent.','did the discrepancy become','the discrepancy did become','became the discrepancy did','had become the discrepancy did','A expressão restritiva inicial exige inversão na oração principal.'],
 ['The editor’s revisions, judicious ___ they were, could not remedy the missing evidence.','though','that','so','even','Adjective + though + sujeito + verbo é uma forma concessiva.'],
 ['The concession was merely cosmetic. What is the implication?','It changed appearances without changing the substance.','It removed most of the document’s technical details.','It was intended to be permanent and legally binding.','It was published without the author’s consent.','Cosmetic implica mudança superficial, sem efeito substantivo.'],
 ['Her response was uncharacteristically equivocal. What changed?','She was unusually unwilling to take a clear position.','She became more direct than usual.','She quoted an unfamiliar source at length.','She defended an unexpectedly unpopular position clearly.','Equivocal faz referência à falta de clareza ou compromisso.']
]
];
const placementReading=[
 ['Library notice','The Oak Street Library opens at nine today. The children’s reading group starts at ten in Room B. Bring your library card. You can borrow books at the front desk, but the computers are closed today.',[
  ['When does the reading group start?','At ten.','At nine.','At noon.','At eight.','O aviso diz que o grupo começa às dez.'],
  ['What is unavailable today?','The computers.','The front desk.','Room B.','Borrowing books.','A última frase informa que os computadores estão indisponíveis.']]],
 ['Message from a colleague','Hi Sam. I’m moving our team lunch from Tuesday to Thursday because Jo has a medical appointment. We’re still meeting at the same café, but I reserved a table for twelve thirty instead of noon. Let me know by Wednesday if you need a vegetarian meal.',[
  ['What stayed the same?','The café.','The day.','The time.','The menu for everyone.','O local permanece o mesmo, apesar da troca de dia e de horário.'],
  ['What should a vegetarian colleague do?','Reply by Wednesday.','Arrive at noon.','Ask Jo to change the appointment.','Reserve a separate table.','A última frase pede que a necessidade de refeição vegetariana seja informada até quarta.']]],
 ['A change at work','Last year our store introduced online orders. At first, staff picked items just before customers arrived, which caused delays at busy times. We now prepare orders in the morning. Customers can change an order until ten, but after that they need to contact the help desk. The system has reduced queues, although errors still happen when products sell out.',[
  ['Why did the store change when orders were prepared?','To reduce delays during busy periods.','To remove its help desk.','To let people order after closing.','To make every item available online.','O primeiro método atrasava a retirada nos períodos de maior movimento.'],
  ['What does the writer say about the new system?','It improved waiting times but did not remove all errors.','It made queues longer.','It stopped stock from selling out.','It prevents people from editing orders in the morning.','Although introduz a ressalva sobre os erros restantes.']]],
 ['A proposal about commuting','The city tested a fare-free bus route for three months. Passenger numbers increased, especially on weekends, but traffic did not fall as much as expected. The survey suggested a reason: many new passengers had previously walked or cycled, while most drivers still considered the bus too slow. Rather than ending the trial, the transport team wants to add dedicated bus lanes before measuring it again.',[
  ['Why did traffic fall less than expected?','Many new bus users had not been driving before.','The number of weekend passengers fell.','Most new riders switched to cars.','The route charged more at busy times.','Muitos passageiros passaram da caminhada ou bicicleta para o ônibus, sem retirar carros das ruas.'],
  ['What does the team want to test next?','Whether faster bus service attracts more drivers.','Whether higher parking prices reduce weekend trips.','Whether cyclists should pay the same fare.','Whether the trial can run without a survey.','Faixas exclusivas atacam o problema da lentidão relatado pelos motoristas.']]],
 ['Interpreting a survey','After the hospital changed its booking system, missed appointments fell by 18 percent. The director presented the drop as evidence that text reminders were effective. The researchers noted, however, that the same period saw evening appointments introduced, and evening patients were less likely to miss a visit even before the change. They recommended following comparable groups with and without reminders rather than simply comparing the periods before and after. In their view, the decrease was encouraging, but it told the hospital less about what to invest in next than the headline number suggested.',[
  ['What is the researchers’ main concern?','The study cannot separate the reminders from a simultaneous change.','The percentage is too small to count as a decrease.','Evening appointments were definitely the only cause.','Patients no longer received text messages.','Uma segunda intervenção ocorreu no mesmo período e pode explicar parte da queda.'],
  ['Why does the last sentence refer to investment?','Choosing an intervention requires knowing which change brought the benefit.','The booking system cannot be maintained without new funding.','The researchers want every appointment moved to the evening.','The director plans to remove all reminders.','A associação é promissora, mas não basta para decidir onde investir.']]],
 ['When a metric becomes the target','When the council began ranking libraries by the number of loans per visitor, several branches shortened their lending periods. The rankings improved: the same books now moved more often. One analyst said this showed the measure was malleable, not that every gain was spurious. Shorter loans really did improve access to some heavily requested titles. Yet the branches that best supported readers who needed more time—people learning to read, for example—fell down the list. In the next report, the council retained the metric but published it alongside waiting times and the proportion of loans renewed. The point was to make the trade-offs visible without pretending that a compromise indicator could settle them.',[
  ['Which claim best captures the analyst’s distinction?','A metric can be manipulated while still tracking some real improvements.','Any strategy that improves a metric invalidates every reported gain.','Shorter lending periods benefited all readers to the same extent.','The ranking originally measured literacy better than access.','O analista distingue a possibilidade de manipulação da existência de ganhos concretos para alguns títulos.'],
  ['Why did the council add other measures?','To expose tensions a single ranking concealed.','To prove renewals are preferable to short loans.','To construct a universal score that settles the debate.','To make the best-performing branches harder to identify.','O último período explicita que os indicadores adicionais revelam trocas sem resolvê-las automaticamente.']]]
];
const placementListening=[
 ['Hi, this is Mia. I’m at the bus stop in front of the park. My bus leaves at eight fifteen. Please bring my blue bag. It’s next to the front door.',[
  ['Where is Mia?','At the bus stop.','Inside the park.','At home.','At the train station.','Mia diz I’m at the bus stop.'],
  ['What does she want the listener to bring?','A blue bag.','A bus ticket.','A phone.','A coat.','A pessoa deve trazer a bolsa azul.']]],
 ['Attention, passengers. The train to Brighton will depart from platform six, not platform two. It is running twenty minutes late. If you have a ticket for a different service, please speak to a member of staff before you get on.',[
  ['Which platform should people use now?','Platform six.','Platform two.','Platform four.','Platform twenty.','O anúncio corrige a plataforma para six.'],
  ['Who should talk to a member of staff?','Passengers with a ticket for another service.','Everyone who arrived early.','Passengers on platform six with the correct ticket.','Passengers without any luggage.','A orientação se dirige a quem tem passagem para outro serviço.']]],
 ['I tried working from home every day last winter. I saved money on travel and got more done in the mornings. By the afternoon, though, I missed having someone nearby to ask for help. Now I work from home on Mondays and Fridays, and go into the office the rest of the week.',[
  ['What was one advantage of working from home?','She spent less on travel.','She had more people around in the afternoons.','She stopped working in the mornings.','She moved closer to the office.','A locutora diz I saved money on travel.'],
  ['How often does she work from home now?','Two days a week.','Every day.','Only on Fridays.','Three days a week.','Mondays and Fridays são dois dias por semana.']]],
 ['At first I supported moving the market indoors. The sellers would be protected from rain, and customers could shop all year. But the rental fee would force out many of the smaller stalls. I’d support the move if the council offered reduced rent to independent sellers. Until then, repairing the outdoor shelters seems like the better option.',[
  ['What changed the speaker’s position?','Concern that higher rent would exclude small sellers.','Concern that outdoor shelters could not be repaired.','A preference for shopping outdoors in winter.','A decision to close the market for part of the year.','O custo da locação poderia expulsar vendedores menores.'],
  ['Under what condition would the speaker support the move?','If independent sellers paid reduced rent.','If the outdoor market were removed immediately.','If all stalls charged the same prices.','If the council limited customers during rain.','A frase I’d support the move if... apresenta a condição.']]],
 ['I wouldn’t call the workshop a failure. We identified a genuine problem with the application process. What we didn’t do was hear from the people most likely to be affected, because the session was held during their working hours. So I’d treat the proposals as promising starting points. Before adopting them, we should test them in a format those applicants can actually attend.',[
  ['How does the speaker assess the workshop?','Useful, with an important limitation.','Unsuccessful in every respect.','Sufficient to finalize the proposals.','Useful only because attendance was high.','A oficina revelou um problema, mas não ouviu o grupo mais afetado.'],
  ['Why does the speaker want another format?','To involve applicants who could not attend.','To avoid recording any comments from applicants.','To prove the original proposals were wrong.','To attract more workshop organizers.','O problema era o horário incompatível com os participantes.']]],
 ['The panel’s recommendation was framed as a pause. That word suggested that the project would resume once the evidence improved. In practice, the same recommendation made no provision to retain staff or store the data. I’m not saying they intended to end the project. But an intention can be perfectly sincere and still be at odds with the arrangements made to carry it out.',[
  ['What tension is the speaker pointing out?','The temporary framing conflicts with plans that make resumption harder.','The staff plan to continue even though the evidence was destroyed.','The panel disagrees about whether the project helped the public.','The evidence improved faster than the panel expected.','Pause implica retomada, mas faltam medidas para manter sua viabilidade.'],
  ['What is the speaker careful to distinguish?','A sincere intention and the practical effect of a decision.','Two legal interpretations of the same document.','The reliability of staff and the validity of their data.','Two different timelines for publishing evidence.','A fala final admite sinceridade e mostra que as providências podem contrariá-la.']]]
];
const placementProduction=[
 ['Escreva uma mensagem curta dizendo seu nome, onde mora e o que faz num dia comum.','Apresente-se e diga uma coisa que você faz no fim de semana.'],
 ['Convide alguém para um passeio. Inclua dia, horário, local e uma alternativa se chover.','Explique a um visitante como chegar a um lugar conhecido.'],
 ['Conte uma viagem que deu errado e explique como você resolveu o problema.','Reconte um imprevisto, situando as ações e o desfecho.'],
 ['Compare duas propostas para melhorar o transporte do seu bairro. Defenda uma e responda a uma objeção.','Apresente sua posição sobre trabalho remoto e reconheça uma vantagem da posição oposta.'],
 ['Redija uma recomendação profissional com duas opções, critérios de decisão e uma ressalva sobre a evidência.','Resuma uma diferença de opinião e proponha uma solução com condições.'],
 ['Reformule uma decisão controversa para dois públicos. Explique as mudanças de registro, foco e grau de certeza.','Explique duas interpretações plausíveis da mesma decisão e diga quais evidências mudariam sua opinião.']
];
