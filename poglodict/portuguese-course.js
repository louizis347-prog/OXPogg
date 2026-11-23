const supportSpanish=new Map();
function bilingual(en,es){
  supportSpanish.set(en,es);
  return en;
}
const portugueseOpening=[
  ['Café','café','coffee','café','Tomo café todas as manhãs.','I drink coffee every morning.','Tomo café todas las mañanas.','O café ainda está quente.','The coffee is still hot.','El café todavía está caliente.',
   'para viagem','to go','para llevar','Um café para viagem, por favor.','A coffee to go, please.','Un café para llevar, por favor.','Quero dois pães de queijo para viagem.','I’d like two cheese rolls to go.','Quiero dos panes de queso para llevar.'],
  ['Direções','esquina','street corner','esquina','A farmácia fica na esquina.','The pharmacy is on the corner.','La farmacia está en la esquina.','A gente vai se encontrar na esquina.','We’re going to meet at the corner.','Nos vamos a encontrar en la esquina.',
   'a pé','on foot','a pie','Vou a pé até o metrô.','I’m walking to the subway station.','Voy a pie hasta el metro.','Dá para chegar lá a pé.','You can get there on foot.','Se puede llegar a pie.'],
  ['Viagem','adiar','to postpone','aplazar','Adiamos a viagem por causa da chuva.','We postponed the trip because of the rain.','Aplazamos el viaje por la lluvia.','O grupo decidiu adiar a saída.','The group decided to postpone its departure.','El grupo decidió aplazar la salida.',
   'fazer as malas','to pack','hacer las maletas','Fiz as malas na noite anterior.','I packed the night before.','Hice las maletas la noche anterior.','Precisamos fazer as malas antes do jantar.','We need to pack before dinner.','Tenemos que hacer las maletas antes de cenar.'],
  ['Conversas','combinar','to arrange, to agree on','acordar, quedar','Vamos combinar um horário amanhã?','Can we agree on a time tomorrow?','¿Acordamos una hora mañana?','Já combinamos o local do encontro.','We’ve already agreed on where to meet.','Ya acordamos el lugar de encuentro.',
   'de boa','okay, relaxed (informal)','tranquilo, sin problema (informal)','Se você chegar mais tarde, tudo de boa.','It’s totally fine if you arrive later.','No hay problema si llegas más tarde.','No fim de semana eu fico de boa em casa.','On the weekend I just relax at home.','El fin de semana me quedo tranquilo en casa.'],
  ['Argumentação','ressalva','reservation or qualification','reserva, salvedad','Concordo com a proposta, com uma ressalva.','I agree with the proposal, with one reservation.','Estoy de acuerdo con la propuesta, con una salvedad.','Ela fez uma ressalva sobre o prazo.','She raised a concern about the deadline.','Hizo una salvedad sobre el plazo.',
   'em linhas gerais','in broad terms','a grandes rasgos','Vou descrever o projeto em linhas gerais.','I’ll describe the project in broad terms.','Voy a describir el proyecto a grandes rasgos.','Em linhas gerais, o plano continua o mesmo.','Broadly speaking, the plan is the same.','A grandes rasgos, el plan sigue igual.'],
  ['Nuances','desdobramento','development or consequence','consecuencia, evolución','O relatório examina os desdobramentos da decisão.','The report examines the consequences of the decision.','El informe analiza las consecuencias de la decisión.','Ninguém previu esse desdobramento.','No one anticipated this development.','Nadie previó este desenlace.',
   'à luz de','in light of','a la luz de','À luz das novas evidências, reconsideramos a hipótese.','In light of the new evidence, we reconsidered the hypothesis.','A la luz de las nuevas pruebas, reconsideramos la hipótesis.','O contrato foi revisto à luz da nova lei.','The contract was reviewed in light of the new law.','El contrato se revisó a la luz de la nueva ley.']
];
const portugueseGrammar=[
  ['Ser and estar','Ser y estar','Use ser for identity or origin and estar for a state or current location.','Usa ser para la identidad o el origen y estar para un estado o una ubicación actual.','Estar often contracts in speech: está becomes tá. Use the full form in neutral writing.','En el habla, está se reduce a menudo a tá. Usa la forma completa en la escritura neutra.',
   'Sou do Recife e estou em Brasília.','I’m from Recife and I’m in Brasília.','Soy de Recife y estoy en Brasilia.','A Ana é médica e está cansada.','Ana is a doctor and she’s tired.','Ana es médica y está cansada.','O café está quente.','The coffee is hot.','El café está caliente.'],
  ['Plans with ir','Planes con ir','Use a present-tense form of ir followed directly by an infinitive.','Usa una forma de ir en presente seguida directamente de un infinitivo.','Brazilian Portuguese says vou sair, without a between the two verbs.','En portugués brasileño se dice vou sair, sin a entre los dos verbos.',
   'Vou sair às oito.','I’m going to leave at eight.','Voy a salir a las ocho.','Vamos pegar o metrô.','We’re going to take the subway.','Vamos a tomar el metro.','Eles vão ligar amanhã.','They’re going to call tomorrow.','Van a llamar mañana.'],
  ['Past events and background','Pasado puntual e imperfecto','Use the simple past for a completed event and the imperfect for the background.','Usa el pretérito perfecto simple para un hecho concluido y el imperfecto para el contexto.','Combine the two forms to signal which action was already happening.','Combina las dos formas para indicar qué acción ya estaba ocurriendo.',
   'Quando cheguei, chovia.','When I arrived, it was raining.','Cuando llegué, llovía.','Ela lia quando o telefone tocou.','She was reading when the phone rang.','Leía cuando sonó el teléfono.','A loja fechou enquanto esperávamos.','The store closed while we were waiting.','La tienda cerró mientras esperábamos.'],
  ['Wishes with the subjunctive','Deseos con el subjuntivo','Use the subjunctive after espero que or quero que when the next clause expresses a wish.','Usa el subjuntivo después de espero que o quero que cuando la siguiente oración expresa un deseo.','Compare quero viajar, with one subject, and quero que você viaje, with two subjects.','Compara quero viajar, con un sujeto, y quero que você viaje, con dos sujetos.',
   'Espero que você chegue cedo.','I hope you arrive early.','Espero que llegues temprano.','Quero que a equipe leia o contrato.','I want the team to read the contract.','Quiero que el equipo lea el contrato.','Tomara que não chova no domingo.','I hope it doesn’t rain on Sunday.','Ojalá no llueva el domingo.'],
  ['Concessions with embora','Concesiones con embora','Use embora followed by the subjunctive to acknowledge an obstacle or qualification.','Usa embora seguido del subjuntivo para reconocer un obstáculo o una salvedad.','A fact can still take the subjunctive after embora. The main clause carries the point you want to make.','Incluso un hecho puede ir en subjuntivo después de embora. La oración principal contiene la afirmación central.',
   'Embora esteja caro, o serviço é confiável.','Although it’s expensive, the service is reliable.','Aunque sea caro, el servicio es fiable.','Embora a sala fosse pequena, todos couberam.','Although the room was small, everyone fit.','Aunque la sala era pequeña, cabíamos todos.','Embora tenham surgido dúvidas, a equipe concluiu a análise.','Although questions came up, the team completed the analysis.','Aunque surgieron dudas, el equipo terminó el análisis.'],
  ['The future subjunctive','El futuro de subjuntivo','Use the future subjunctive after quando or se for a future situation that may occur.','Usa el futuro de subjuntivo después de quando o se para una situación futura que puede ocurrir.','The irregular forms vier, tiver and fizer come from vir, ter and fazer. This tense is common in Brazil.','Las formas irregulares vier, tiver y fizer provienen de vir, ter y fazer. Este tiempo es común en Brasil.',
   'Quando você vier, conversaremos.','When you come, we’ll talk.','Cuando vengas, hablaremos.','Se ela tiver tempo, revisará o relatório.','If she has time, she’ll review the report.','Si tiene tiempo, revisará el informe.','Avise quando fizer a reserva.','Let me know when you make the reservation.','Avísame cuando hagas la reserva.'],
  ['Definite articles','Artículos definidos','Use o, a, os and as according to the noun’s gender and number.','Usa o, a, os y as según el género y el número del sustantivo.','Some nouns have a different gender in Spanish. Memorize o leite and a viagem with their articles.','Algunos sustantivos tienen un género distinto en español. Memoriza o leite y a viagem con sus artículos.',
   'A viagem começa amanhã.','The trip starts tomorrow.','El viaje comienza mañana.','O leite está na geladeira.','The milk is in the fridge.','La leche está en el refrigerador.','As lojas estão fechadas.','The stores are closed.','Las tiendas están cerradas.'],
  ['Preposition contractions','Contracciones de preposiciones','Combine de or em with definite articles, as in do, da, no and na.','Combina de o em con los artículos definidos, como en do, da, no y na.','In careful writing, keep de separate from a pronoun that is the subject of a following infinitive, as in antes de ele sair.','En la escritura cuidada, se recomienda separar de del pronombre que funciona como sujeto de un infinitivo, como en antes de ele sair.',
   'As chaves estão na mochila.','The keys are in the backpack.','Las llaves están en la mochila.','Ela chegou do trabalho cedo.','She got home from work early.','Llegó temprano del trabajo.','O museu fica no centro.','The museum is downtown.','El museo está en el centro.'],
  ['Comparisons with mais and menos','Comparaciones con mais y menos','Use mais or menos with an adjective followed by que or do que.','Usa mais o menos con un adjetivo seguido de que o do que.','Melhor and pior replace mais bom and mais ruim in many standard comparisons.','Melhor y pior reemplazan a mais bom y mais ruim en muchas comparaciones estándar.',
   'O trem é mais rápido que o ônibus.','The train is faster than the bus.','El tren es más rápido que el autobús.','Este quarto é menos barulhento do que o outro.','This room is less noisy than the other one.','Esta habitación es menos ruidosa que la otra.','O segundo plano é melhor que o primeiro.','The second plan is better than the first.','El segundo plan es mejor que el primero.'],
  ['Polite requests','Peticiones corteses','Use poderia or gostaria de to soften a request.','Usa poderia o gostaria de para suavizar una petición.','Poderia plus an infinitive requests an action. Gostaria de can introduce a noun or an infinitive.','Poderia más un infinitivo pide una acción. Gostaria de puede introducir un nombre o un infinitivo.',
   'Você poderia fechar a janela?','Could you close the window?','¿Podrías cerrar la ventana?','Gostaria de uma mesa para duas pessoas.','I’d like a table for two.','Quisiera una mesa para dos personas.','Poderia confirmar o horário da consulta?','Could you confirm the appointment time?','¿Podría confirmar la hora de la cita?'],
  ['Personal infinitive','Infinitivo personal','An infinitive can have its own subject and take endings such as -mos and -em.','Un infinitivo puede tener sujeto propio y tomar terminaciones como -mos y -em.','An explicit subject makes the relationship clear, as in para os alunos lerem.','Un sujeto expreso aclara la relación, como en para os alunos lerem.',
   'Saímos cedo para pegarmos o trem.','We left early so we could catch the train.','Salimos temprano para tomar el tren.','Deixei o livro para os alunos lerem.','I left the book for the students to read.','Dejé el libro para que los alumnos lo leyeran.','Antes de vocês assinarem, leiam o contrato.','Before you sign, read the contract.','Antes de que firmen, lean el contrato.'],
  ['Counterfactual past','Condicional irreal en el pasado','Combine se + tivesse with a past participle and a result with teria + participle.','Combina se + tivesse con un participio y una consecuencia con teria + participio.','Place the unreal condition first or last. Use a comma after an initial se clause.','Puedes colocar la condición irreal al principio o al final. Usa una coma después de la oración inicial con se.',
   'Se eu tivesse sabido, teria avisado.','If I had known, I would have told you.','Si lo hubiera sabido, habría avisado.','Teríamos chegado antes se o ônibus tivesse saído no horário.','We would have arrived earlier if the bus had left on time.','Habríamos llegado antes si el autobús hubiera salido a tiempo.','Se a equipe tivesse testado o arquivo, teria encontrado o erro.','If the team had tested the file, it would have found the error.','Si el equipo hubiera probado el archivo, habría encontrado el error.']
];
const ptGrammar = portugueseGrammar.map(row=>{
  const [t,tEs,rule,ruleEs,note,noteEs,...examples]=row;
  const translations=[];
  for(let i=0;i<examples.length;i+=3)translations.push(examples[i],bilingual(examples[i+1],examples[i+2]));
  return {topic:[bilingual(t,tEs),bilingual(rule,ruleEs),...translations.slice(0,2)],note:bilingual(note,noteEs),extra:translations.slice(2)};
});
study.por=portugueseOpening.map((row,index)=>[row[0],row[1],row[4],bilingual(row[5],row[6]),...ptGrammar[index].topic]);
glosses.por=portugueseOpening.map(row=>bilingual(row[2],row[3]));
phrases.por=portugueseOpening.map(row=>[row[10],bilingual(row[11],row[12]),row[13],bilingual(row[14],row[15])]);
coreSeconds.por=portugueseOpening.map(row=>[row[7],bilingual(row[8],row[9]),row[16],bilingual(row[17],row[18])]);
grammarPractice.por=ptGrammar.slice(6).map(row=>row.topic);
extraGrammar.por=ptGrammar.map(row=>row.extra);
grammarNotes.por=ptGrammar.map(row=>row.note);
starterEntries.por=`café|noun|coffee|coffee|O café está pronto.|The coffee is ready.
água|noun|water|water|Você quer água?|Do you want some water?
obrigado|intj|thank you|thank you|Obrigado pela ajuda.|Thank you for your help.
ônibus|noun|bus|bus|O ônibus chegou cedo.|The bus arrived early.
hoje|adv|today|today|Hoje eu trabalho em casa.|I work from home today.
amanhã|adv|tomorrow|tomorrow|A aula é amanhã.|Class is tomorrow.`;
authoredSeconds.por=new Map([
  ['café',{text:'Eu tomo café sem açúcar.',translation:bilingual('I drink coffee without sugar.','Tomo café sin azúcar.')}],
  ['água',{text:'Trouxe uma garrafa de água.',translation:bilingual('I brought a bottle of water.','Traje una botella de agua.')}],
  ['obrigado',{text:'Obrigado pelo convite!',translation:bilingual('Thanks for the invitation!','¡Gracias por la invitación!')}],
  ['ônibus',{text:'Vou de ônibus para a escola.',translation:bilingual('I take the bus to school.','Voy a la escuela en autobús.')}],
  ['hoje',{text:'O mercado fecha cedo hoje.',translation:bilingual('The market closes early today.','El mercado cierra temprano hoy.')}],
  ['amanhã',{text:'Amanhã vou visitar a minha avó.',translation:bilingual('Tomorrow I’m going to visit my grandma.','Mañana voy a visitar a mi abuela.')}]
]);
[
  ['coffee','café'],['water','agua'],['thank you','gracias'],['bus','autobús'],['today','hoy'],['tomorrow','mañana'],
  ['The coffee is ready.','El café está listo.'],['Do you want some water?','¿Quieres agua?'],['Thank you for your help.','Gracias por tu ayuda.'],
  ['The bus arrived early.','El autobús llegó temprano.'],['I work from home today.','Hoy trabajo desde casa.'],['Class is tomorrow.','La clase es mañana.']
].forEach(([en,es])=>bilingual(en,es));
reviewedEntries.por=new Map();
sceneVocabulary.por=[
  ['pedido','noun',bilingual('order','pedido'),'O meu pedido está pronto?',bilingual('Is my order ready?','¿Está listo mi pedido?'),'Fiz o pedido no balcão.',bilingual('I placed my order at the counter.','Hice el pedido en el mostrador.')],
  ['pão de queijo','phrase',bilingual('Brazilian cheese roll','pan de queso brasileño'),'Pedi um pão de queijo.',bilingual('I ordered a cheese roll.','Pedí un pan de queso.'),'O pão de queijo acabou.',bilingual('They ran out of cheese rolls.','Se acabó el pan de queso.')],
  ['cartão','noun',bilingual('card','tarjeta'),'Escrevi a palavra no cartão.',bilingual('I wrote the word on the card.','Escribí la palabra en la tarjeta.'),'Pegue o cartão de hoje.',bilingual('Pick up today’s card.','Toma la tarjeta de hoy.')],
  ['mensagem de voz','phrase',bilingual('voice message','mensaje de voz'),'Recebi uma mensagem de voz.',bilingual('I got a voice message.','Recibí un mensaje de voz.'),'Mandei uma mensagem de voz para a Lia.',bilingual('I sent Lia a voice message.','Le mandé un mensaje de voz a Lia.')],
  ['anotações','noun',bilingual('notes','apuntes'),'Revisei as minhas anotações.',bilingual('I reviewed my notes.','Repasé mis apuntes.'),'Minhas anotações estão no caderno.',bilingual('My notes are in my notebook.','Mis apuntes están en el cuaderno.')]
];
const portugueseCafe={
  por:'Entrei no café perto da estação.\nPedi um café e um pão de queijo.\nO café era para viagem.\nO atendente colocou meu pedido no balcão.\nPaguei e fui à estação.\nBom dia! O que vai querer?\nUm café e um pão de queijo, por favor.\nÉ para tomar aqui?\nNão, é para viagem.\nSeu pedido está aqui no balcão.\nObrigado! Até logo.',
  eng:'I went into the café near the station.\nI ordered a coffee and a cheese roll.\nThe coffee was to go.\nThe server put my order on the counter.\nI paid and went to the station.\nGood morning! What would you like?\nA coffee and a cheese roll, please.\nIs that for here?\nNo, it’s to go.\nYour order is here on the counter.\nThanks! See you later.',
  spa:'Entré en el café cerca de la estación.\nPedí un café y un pan de queso.\nEl café era para llevar.\nEl empleado puso mi pedido en el mostrador.\nPagué y fui a la estación.\n¡Buenos días! ¿Qué desea?\nUn café y un pan de queso, por favor.\n¿Es para tomar aquí?\nNo, es para llevar.\nSu pedido está aquí en el mostrador.\n¡Gracias! Hasta luego.'
};
const ptReviewed=`ser|verb|to be (identity or origin)|ser (identidad u origen)|Eu sou do Brasil.|I’m from Brazil.|Soy de Brasil.|A Lia é professora.|Lia is a teacher.|Lia es profesora.
estar|verb|to be (state or location)|estar (estado o ubicación)|Estamos em casa.|We’re at home.|Estamos en casa.|O café está quente.|The coffee is hot.|El café está caliente.
o|det|the, masculine singular definite article|el, artículo definido masculino singular|O trem chegou.|The train arrived.|El tren llegó.|Abra o livro, por favor.|Open the book, please.|Abre el libro, por favor.
a|det|the, feminine singular definite article|la, artículo definido femenino singular|A loja fechou.|The store closed.|La tienda cerró.|Onde está a mochila?|Where is the backpack?|¿Dónde está la mochila?
os|det|the, masculine plural definite article|los, artículo definido masculino plural|Os alunos chegaram.|The students arrived.|Los alumnos llegaron.|Guarde os bilhetes.|Keep the tickets.|Guarda los boletos.
as|det|the, feminine plural definite article|las, artículo definido femenino plural|As portas estão abertas.|The doors are open.|Las puertas están abiertas.|As chaves estão na bolsa.|The keys are in the bag.|Las llaves están en el bolso.
eu|pron|I, first-person singular subject pronoun|yo, pronombre sujeto de primera persona del singular|Eu estudo português.|I study Portuguese.|Estudio portugués.|Eu falo inglês.|I speak English.|Hablo inglés.
você|pron|you, common singular second-person pronoun in Brazil|tú o usted, pronombre de segunda persona singular común en Brasil|Você está bem?|Are you okay?|¿Estás bien?|Você mora aqui?|Do you live here?|¿Vives aquí?
é|verb|third-person singular present of ser|tercera persona del singular del presente de ser|A Lia é brasileira.|Lia is Brazilian.|Lia es brasileña.|O livro é meu.|The book is mine.|El libro es mío.
estou|verb|first-person singular present of estar|primera persona del singular del presente de estar|Estou na estação.|I’m at the station.|Estoy en la estación.|Estou com fome.|I’m hungry.|Tengo hambre.
foi|verb|past form of ser or ir|forma de pasado de ser o ir|Ela foi ao mercado.|She went to the market.|Fue al mercado.|A viagem foi tranquila.|The trip was smooth.|El viaje fue tranquilo.
tom|noun|tone, a quality of voice or a shade of color|tono, cualidad de voz o matiz de color|Ela respondeu num tom calmo.|She answered in a calm tone.|Respondió con un tono tranquilo.|A parede tem um tom de azul bem claro.|The wall is a very light shade of blue.|La pared tiene un tono de azul muy claro.
suar|verb|to sweat|sudar|Comecei a suar durante a corrida.|I started sweating during the run.|Empecé a sudar durante la carrera.|Está tão quente que todo mundo está suando.|It’s so hot everyone is sweating.|Hace tanto calor que todos están sudando.
podar|verb|to prune|podar|Vamos podar a roseira amanhã.|We’ll prune the rosebush tomorrow.|Vamos a podar el rosal mañana.|Ela precisa podar os galhos secos.|She needs to prune the dry branches.|Tiene que podar las ramas secas.
poder|verb|can, to be able or allowed to|poder, tener capacidad o permiso|Você pode me ajudar?|Can you help me?|¿Puedes ayudarme?|Posso sentar aqui?|May I sit here?|¿Puedo sentarme aquí?
dizer|verb|to say or tell|decir|O que você disse?|What did you say?|¿Qué dijiste?|Ela disse que chegaria cedo.|She said she would arrive early.|Dijo que llegaría temprano.
achar|verb|to find or to think, depending on the construction|encontrar o pensar, según la construcción|Achei as chaves na bolsa.|I found the keys in the bag.|Encontré las llaves en el bolso.|Acho que vai chover.|I think it’s going to rain.|Creo que va a llover.
casar|verb|to get married|casarse|Eles vão se casar em junho.|They’re getting married in June.|Se van a casar en junio.|A gente se casou no Recife.|We got married in Recife.|Nos casamos en Recife.
para|prep|for or to, indicating purpose or direction|para, indica finalidad o destino|Esse presente é para você.|This gift is for you.|Este regalo es para ti.|Peguei o ônibus para o centro.|I took the bus downtown.|Tomé el autobús hacia el centro.`;
for(const line of ptReviewed.split('\n')){
  const [word,part,definition,definitionEs,first,firstEn,firstEs,second,secondEn,secondEs]=line.split('|');
  reviewedEntries.por.set(word,{word,part,gloss:bilingual(definition,definitionEs),
    examples:[{text:first,translation:bilingual(firstEn,firstEs)},{text:second,translation:bilingual(secondEn,secondEs)}]});
}
