// Each scene provides a setting, a conversational goal, two twists and a bilingual continuation.
// Each language row has a keyword, an opening turn, a reply and a follow-up.
const sceneExtensions={
  cup:{
    title:['No balcão da cafeteria','At the café counter','En el mostrador del café'],
    intro:['Depois de escolher o que tomar, combine como o pedido será servido. A pergunta convida a escolher entre tomar no local e levar.','Once you’ve ordered, clarify how you’d like it served. The question offers a choice between staying and taking it away.','Después de pedir, aclara cómo quieres que te sirvan. La pregunta ofrece elegir entre tomarlo allí o llevarlo.'],
    roles:[['Atendente','Server','Camarero'],['Cliente','Customer','Cliente']],
    twists:[['Você está com pressa.','You’re in a hurry.','Tienes prisa.'],['Uma segunda pessoa acaba de chegar.','A second person has just arrived.','Acaba de llegar otra persona.']],
    pt:['café','O café é para tomar aqui ou para viagem?','Para viagem, por favor.','E um copo de água, por favor.'],
    eng:['coffee','Is the coffee for here or to go?','To go, please.','And a glass of water, please.'],
    spa:['café','¿El café es para tomar aquí o para llevar?','Para llevar, por favor.','Y un vaso de agua, por favor.'],
    ita:['caffè','Il caffè è da bere qui o da portare via?','Da portare via, per favore.','E un bicchiere d’acqua, per favore.'],
    deu:['Kaffee','Ist der Kaffee für hier oder zum Mitnehmen?','Zum Mitnehmen, bitte.','Und ein Glas Wasser, bitte.'],
    ara:['قَهْوَة','هَلْ سَتَشْرَبُ القَهْوَةَ هُنَا أَمْ سَتَأْخُذُهَا مَعَكَ؟','سَآخُذُهَا مَعِي، مِنْ فَضْلِكَ.','وَكَأْسَ مَاءٍ، مِنْ فَضْلِكَ.'],
    jpn:['コーヒー','コーヒーは店内でお召し上がりですか、それともお持ち帰りですか。','持ち帰りでお願いします。','お水もお願いします。'],
    cmn:['咖啡','咖啡是在这儿喝，还是带走？','请帮我打包。','再来一杯水，谢谢。']
  },
  ticket:{
    title:['Da bilheteria à plataforma','From the ticket desk to the platform','De la taquilla al andén'],
    intro:['Ter o bilhete em mãos resolve só uma parte da viagem. Antes de embarcar, descubra de qual plataforma sai o trem.','Getting your ticket is one part of the journey. Before boarding, find out which platform serves your train.','Tener el billete resuelve solo una parte del viaje. Antes de subir, averigua de qué andén sale el tren.'],
    roles:[['Passageiro','Passenger','Pasajero'],['Funcionário da estação','Station staff member','Empleado de la estación']],
    twists:[['Seu trem sai em cinco minutos.','Your train leaves in five minutes.','Tu tren sale en cinco minutos.'],['O painel de informação está apagado.','The information board is off.','El panel de información está apagado.']],
    pt:['plataforma','De que plataforma sai o trem?','Sai da plataforma três.','A plataforma fica longe?'],
    eng:['platform','Which platform does the train leave from?','It leaves from platform three.','Is the platform far?'],
    spa:['andén','¿De qué andén sale el tren?','Sale del andén tres.','¿Queda lejos el andén?'],
    ita:['binario','Da quale binario parte il treno?','Parte dal binario tre.','Il binario è lontano?'],
    deu:['Gleis','Von welchem Gleis fährt der Zug ab?','Er fährt von Gleis drei ab.','Ist das Gleis weit weg?'],
    ara:['رَصِيف','مِنْ أَيِّ رَصِيفٍ يُغَادِرُ القِطَارُ؟','يُغَادِرُ مِنَ الرَّصِيفِ الثَّالِثِ.','هَلِ الرَّصِيفُ بَعِيدٌ؟'],
    jpn:['ホーム','電車は何番ホームから出ますか。','三番ホームから出ます。','そのホームは遠いですか。'],
    cmn:['站台','火车从哪个站台出发？','从三号站台出发。','那个站台远吗？']
  },
  city:{
    title:['Uma pergunta no bairro','A question in the neighborhood','Una pregunta en el barrio'],
    intro:['Quando alguém fala da cidade onde mora, pergunte sobre um lugar do bairro. Na rua, “perto daqui” ajuda a pedir uma indicação sem saber o endereço.','When someone talks about their city, ask about a place in the neighborhood. On the street, “near here” helps you ask without knowing the address.','Cuando alguien habla de su ciudad, pregunta por un sitio del barrio. En la calle, «cerca de aquí» ayuda a pedir una indicación sin conocer la dirección.'],
    roles:[['Visitante','Visitor','Visitante'],['Morador do bairro','Local resident','Vecino del barrio']],
    twists:[['Você tem tempo para ir a pé.','You have time to walk there.','Tienes tiempo para ir a pie.'],['Você precisa encontrar um lugar que ainda esteja aberto.','You need to find somewhere that is still open.','Necesitas encontrar un lugar que siga abierto.']],
    pt:['bairro','Tem uma padaria neste bairro?','Sim, tem uma perto daqui.','Dá para ir a pé?'],
    eng:['neighborhood','Is there a bakery in this neighborhood?','Yes, there’s one near here.','Can I walk there?'],
    spa:['barrio','¿Hay una panadería en este barrio?','Sí, hay una cerca de aquí.','¿Puedo ir a pie?'],
    ita:['quartiere','C’è una panetteria in questo quartiere?','Sì, ce n’è una qui vicino.','Ci posso andare a piedi?'],
    deu:['Viertel','Gibt es in diesem Viertel eine Bäckerei?','Ja, hier in der Nähe gibt es eine.','Kann ich zu Fuß dorthin gehen?'],
    ara:['حَيّ','هَلْ يُوجَدُ مَخْبَزٌ فِي هَذَا الحَيِّ؟','نَعَمْ، هُنَاكَ مَخْبَزٌ بِالقُرْبِ مِنْ هُنَا.','هَلْ يُمْكِنُنِي الذَّهَابُ إِلَيْهَا مَشْيًا؟'],
    jpn:['近所','この近所にパン屋はありますか。','はい、この近くにあります。','歩いて行けますか。'],
    cmn:['街区','这个街区有面包店吗？','有，就在这附近。','能走过去吗？']
  },
  chat:{
    title:['Do convite ao encontro','From invitation to meetup','De la invitación al encuentro'],
    intro:['Um convite fica mais fácil de aceitar quando já vem com uma proposta de horário. Responda confirmando ou oferecendo outra opção.','An invitation is easier to accept when it includes a suggested time. Confirm it or offer another option.','Es más fácil aceptar una invitación con un horario concreto. Confírmalo o propone otra opción.'],
    roles:[['Quem convida','Host','Quien invita'],['Quem recebe o convite','Guest','Quien recibe la invitación']],
    twists:[['Você só pode ir depois do trabalho.','You can only go after work.','Solo puedes ir después del trabajo.'],['Um amigo quer se juntar a vocês.','A friend wants to join you.','Un amigo quiere acompañarlos.']],
    pt:['horário','Que horário funciona para você?','Às seis funciona para mim.','Onde a gente se encontra?'],
    eng:['time','What time works for you?','Six works for me.','Where should we meet?'],
    spa:['hora','¿Qué hora te viene bien?','A las seis me viene bien.','¿Dónde quedamos?'],
    ita:['orario','Che orario ti va bene?','Le sei mi vanno bene.','Dove ci vediamo?'],
    deu:['Uhrzeit','Welche Uhrzeit passt dir?','Sechs Uhr passt mir.','Wo treffen wir uns?'],
    ara:['وَقْت','أَيُّ وَقْتٍ يُنَاسِبُكَ؟','السَّاعَةُ السَّادِسَةُ تُنَاسِبُنِي.','أَيْنَ نَلْتَقِي؟'],
    jpn:['時間','何時なら都合がいいですか。','六時なら大丈夫です。','どこで会いましょうか。'],
    cmn:['时间','你什么时间方便？','六点我方便。','我们在哪儿见？']
  },
  notebook:{
    title:['Anote antes de começar','Take a note before you start','Anota antes de empezar'],
    intro:['Uma instrução importante passou rápido? Peça que a pessoa repita e use o caderno para registrar o detalhe.','Did an important instruction go by too quickly? Ask the person to repeat it, then note it down.','¿Una instrucción importante se te escapó? Pide que la repitan y anótala.'],
    roles:[['Pessoa que perdeu a instrução','Person who missed the instruction','Quien no oyó la instrucción'],['Colega que ouviu','Classmate who heard it','Compañero que oyó la instrucción']],
    twists:[['Você perdeu o prazo da atividade.','You missed the assignment deadline when it was announced.','No oíste la fecha de entrega.'],['A sala está barulhenta.','The room is noisy.','Hay ruido en la sala.']],
    pt:['caderno','Posso anotar isso no meu caderno?','Claro. Quer que eu repita?','Sim, mais devagar, por favor.'],
    eng:['notebook','Can I write that down in my notebook?','Of course. Want me to repeat it?','Yes, more slowly, please.'],
    spa:['cuaderno','¿Puedo apuntarlo en mi cuaderno?','Claro. ¿Quieres que lo repita?','Sí, más despacio, por favor.'],
    ita:['quaderno','Posso scriverlo sul mio quaderno?','Certo. Vuoi che lo ripeta?','Sì, più piano, per favore.'],
    deu:['Notizbuch','Kann ich das in meinem Notizbuch aufschreiben?','Klar. Soll ich es wiederholen?','Ja, bitte etwas langsamer.'],
    ara:['دَفْتَر','هَلْ يُمْكِنُنِي أَنْ أَكْتُبَ ذَلِكَ فِي دَفْتَرِي؟','بِالطَّبْعِ. هَلْ تُرِيدُ أَنْ أُعِيدَ مَا قُلْتُهُ؟','نَعَمْ، بِبُطْءٍ أَكْثَرَ، مِنْ فَضْلِكَ.'],
    jpn:['ノート','ノートに書いてもいいですか。','もちろんです。もう一度言いましょうか。','はい、もう少しゆっくりお願いします。'],
    cmn:['笔记本','我可以把这个写在笔记本上吗？','当然。要我再说一遍吗？','好，请说慢一点。']
  },
  park:{
    title:['Um plano ao ar livre','A plan outdoors','Un plan al aire libre'],
    intro:['Para transformar a ideia de um passeio em plano, proponha um lugar e convide a pessoa a ir com você.','Turn the idea of a walk into a plan by suggesting a place and inviting someone along.','Para convertir la idea de un paseo en un plan, propón un lugar e invita a la otra persona.'],
    roles:[['Quem propõe o passeio','Person planning the walk','Quien propone el paseo'],['Companhia de passeio','Walking companion','Compañero de paseo']],
    twists:[['Começou a chover.','It just started raining.','Acaba de empezar a llover.'],['Vocês têm só vinte minutos.','You only have twenty minutes.','Solo tienen veinte minutos.']],
    pt:['parque','Vamos dar uma volta pelo parque?','Boa ideia. Vamos!','Vou levar água.'],
    eng:['park','Want to take a walk through the park?','Good idea. Let’s go!','I’ll bring some water.'],
    spa:['parque','¿Damos una vuelta por el parque?','Buena idea. ¡Vamos!','Llevaré agua.'],
    ita:['parco','Facciamo un giro al parco?','Buona idea. Andiamo!','Porto dell’acqua.'],
    deu:['Park','Wollen wir eine Runde durch den Park gehen?','Gute Idee. Los geht’s!','Ich nehme Wasser mit.'],
    ara:['حَدِيقَة','مَا رَأْيُكَ فِي نُزْهَةٍ فِي الحَدِيقَةِ؟','فِكْرَةٌ جَيِّدَةٌ. هَيَّا بِنَا!','سَآخُذُ مَعِي بَعْضَ المَاءِ.'],
    jpn:['公園','公園を散歩しませんか。','いいですね。行きましょう。','水を持っていきます。'],
    cmn:['公园','我们去公园走走吧？','好主意。走吧！','我带点水。']
  },
  health:{
    title:['Na recepção da clínica','At the clinic desk','En la recepción de la clínica'],
    intro:['Ao chegar, avise que tem uma consulta. A recepção pode confirmar o atendimento pedindo seu nome.','On arrival, say you have an appointment. The receptionist may ask for your name to confirm it.','Al llegar, avisa de que tienes una cita. En recepción te pueden preguntar el nombre para confirmarla.'],
    roles:[['Paciente','Patient','Paciente'],['Recepcionista','Receptionist','Recepcionista']],
    twists:[['Você chegou dez minutos antes.','You’re ten minutes early.','Llegaste diez minutos antes.'],['Seu nome é difícil de soletrar.','Your name is hard to spell.','Tu nombre es difícil de deletrear.']],
    pt:['consulta','Bom dia. Tenho uma consulta marcada.','Qual é o seu nome, por favor?','Meu nome é Alex.'],
    eng:['appointment','Good morning. I have an appointment.','May I have your name, please?','My name is Alex.'],
    spa:['cita','Buenos días. Tengo una cita.','¿Me dice su nombre, por favor?','Me llamo Alex.'],
    ita:['appuntamento','Buongiorno. Ho un appuntamento.','Mi dice il suo nome, per favore?','Mi chiamo Alex.'],
    deu:['Termin','Guten Morgen. Ich habe einen Termin.','Wie ist bitte Ihr Name?','Ich heiße Alex.'],
    ara:['مَوْعِد','صَبَاحُ الخَيْرِ. لَدَيَّ مَوْعِدٌ.','مَا اسْمُكَ، مِنْ فَضْلِكَ؟','اسْمِي أَلِكْس.'],
    jpn:['予約','おはようございます。予約しています。','お名前をお願いします。','アレックスです。'],
    cmn:['预约','您好，我有预约。','请问您叫什么名字？','我叫亚历克斯。']
  },
  map:{
    title:['A próxima pergunta no hotel','The next question at the hotel','La siguiente pregunta en el hotel'],
    intro:['Depois do check-in, uma pergunta útil é onde fica o quarto. A resposta pode indicar o andar ou o caminho até o elevador.','After check-in, a useful question is where the room is. The reply can give the floor or point you toward the elevator.','Después de registrarte, pregunta dónde queda la habitación. La respuesta puede indicar la planta o el camino al ascensor.'],
    roles:[['Hóspede','Guest','Huésped'],['Recepcionista','Receptionist','Recepcionista']],
    twists:[['Você carrega uma mala pesada.','You’re carrying a heavy bag.','Llevas una maleta pesada.'],['Você também precisa saber o horário do café da manhã.','You also need to know what time breakfast is.','También necesitas saber a qué hora es el desayuno.']],
    pt:['andar','Em que andar fica o meu quarto?','Fica no segundo andar.','Onde fica o elevador?'],
    eng:['floor','What floor is my room on?','It’s on the second floor.','Where’s the elevator?'],
    spa:['piso','¿En qué piso está mi habitación?','Está en el segundo piso.','¿Dónde está el ascensor?'],
    ita:['piano','A che piano è la mia camera?','È al secondo piano.','Dov’è l’ascensore?'],
    deu:['Stock','In welchem Stock ist mein Zimmer?','Es ist im zweiten Stock.','Wo ist der Aufzug?'],
    ara:['طَابِق','فِي أَيِّ طَابِقٍ تَقَعُ غُرْفَتِي؟','إِنَّهَا فِي الطَّابِقِ الثَّانِي.','أَيْنَ المِصْعَدُ؟'],
    jpn:['階','私の部屋は何階ですか。','二階です。','エレベーターはどこですか。'],
    cmn:['楼','我的房间在几楼？','在二楼。','电梯在哪儿？']
  }
};

function sceneExtensionAt(theme){
  return sceneExtensions[theme]||sceneExtensions.map;
}
function extensionTarget(scene){
  return scene[lang==='por'?'pt':lang].map(text=>lessonLevelText(text));
}
function extensionTranslation(scene){
  return lang==='por'?scene[support==='spa'?'spa':'eng']:scene.pt;
}

function sceneTerm(word,gloss=''){
  const item=wordIndex[lang]?.lookup.get(word);
  const meaning=gloss||companionText(item?.row[10])||'';
  return '<div class="scene-term"><div>'+ (item?linkTo(item,''):nativeText(word,'strong'))+
    lessonPlayButton(word,{compact:true})+'</div>'+pinyinLine(word)+(meaning?'<p lang="'+supportTag()+'">'+clean(meaning)+'</p>':'')+'</div>';
}
function sceneCitation(word,content){
  const fold=text=>text.normalize('NFC').toLocaleLowerCase(languages[lang][2]);
  const needle=fold(word);
  const hasWord=line=>fold(line.text).includes(needle);
  const quote=content.dialogue.find(hasWord)||content.reading.find(hasWord);
  if(!quote)return '';
  return '<blockquote>'+nativeText(quote.text,'p')+pinyinLine(quote.text)+
    '<p lang="'+supportTag()+'">'+clean(quote.pt)+'</p>'+lessonPlayButton(quote.text,{compact:true})+'</blockquote>';
}
function renderSceneArticle(content,vocabulary,theme){
  const scene=sceneExtensionAt(theme);
  const [keyword,...turns]=extensionTarget(scene);
  const [gloss,...translations]=extensionTranslation(scene);
  const core=[...new Set([vocabulary.word,vocabulary.expression])];
  const meanings=(vocabulary.sceneTranslation||[]).slice(1,3);
  const bridge=lang==='eng'&&theme==='city'&&vocabulary.word==='city'?
    'A conversa começa com a diferença entre morar numa cidade e numa cidade pequena. Continue com uma pergunta que um visitante faria a alguém do bairro.':
    routeLabel(...scene.intro);
  return '<article class="lesson-card scene-article" id="sceneVocabularyArticle" aria-labelledby="sceneVocabularyTitle">'+
    '<header><span class="eyebrow">'+routeLabel('Vocabulário da leitura e do diálogo','Reading and dialogue vocabulary','Vocabulario de la lectura y el diálogo')+'</span>'+
    '<h3 id="sceneVocabularyTitle">'+clean(routeLabel(...scene.title))+'</h3><p>'+clean(bridge)+'</p></header>'+
    '<div class="scene-article-grid"><div><h4>'+routeLabel('Da cena original','From the original scene','De la escena original')+'</h4>'+
    core.map((word,index)=>sceneTerm(word,meanings[index])+sceneCitation(word,content)).join('')+
    '</div>'+lessonPhoto(theme)+'</div>'+
    '<section class="scene-continuation" data-playback-block aria-labelledby="sceneContinuationTitle"><h4 id="sceneContinuationTitle">'+
    routeLabel('Continue a conversa','Keep the conversation going','Continúa la conversación')+'</h4>'+
    '<div class="scene-continuation-terms">'+sceneTerm(keyword,gloss)+sceneTerm(turns[1],translations[1])+sceneTerm(turns[2],translations[2])+'</div>'+
    sectionPlayButton('continuation',routeLabel('Ouvir a continuação','Play the next exchange','Escuchar la continuación'))+
    lessonLinesMarkup(turns.map((text,index)=>({text,pt:translations[index]})),'continuation',{theme})+
    lessonCoach(routeLabel('Leve a expressão para outra situação','Use the expression in another situation','Usa la expresión en otra situación'),
      routeLabel('Escolha uma das expressões da continuação. Troque um detalhe, como o horário ou o lugar, e diga sua nova fala.','Choose an expression from the follow-up. Change one detail, such as the time or place, and say your new line.','Elige una expresión de la continuación. Cambia un detalle, como la hora o el lugar, y di tu nueva intervención.'))+
    '</section><a class="scene-practice-link" href="#workshopTitle" data-scene-jump>'+routeLabel('Experimentar na conversa guiada','Try it in guided conversation','Pruébalo en la conversación guiada')+'</a></article>';
}

function renderSceneRoleplay(vocabulary,theme){
  const scene=sceneExtensionAt(theme);
  const [,opening,reply,followUp]=extensionTarget(scene);
  const [,first,second,third]=extensionTranslation(scene);
  return '<section class="scene-roleplay" aria-labelledby="roleplayTitle"><h4 id="roleplayTitle">'+
    routeLabel('Faça uma versão sua','Try your own version','Haz tu propia versión')+'</h4><p>'+
    routeLabel('Improviso em dupla. Faça um papel e imagine a fala da outra pessoa.','Two-person improv. Take one role and imagine what the other person says.','Improvisación en pareja. Elige un papel e imagina qué dice la otra persona.')+'</p>'+
    '<fieldset class="roleplay-roles"><legend>'+routeLabel('Escolha seu papel','Choose your role','Elige tu papel')+'</legend>'+
    scene.roles.map((role,index)=>'<label><input type="radio" name="sceneRole" value="'+index+'"'+(index===1?' checked':'')+'>'+
    clean(routeLabel(...role))+'</label>').join('')+'</fieldset>'+
    '<div class="roleplay-twist"><strong>'+routeLabel('Imprevisto da cena','A twist in the scene','Un giro en la escena')+'</strong>'+
    '<p id="sceneTwist" aria-live="polite">'+clean(routeLabel(...scene.twists[unit%scene.twists.length]))+'</p>'+
    '<button type="button" data-scene-twist="'+(unit%scene.twists.length)+'">'+routeLabel('Trocar o imprevisto','Change the twist','Cambiar el giro')+'</button></div>'+
    '<div class="roleplay-cue" data-role-cue="0" hidden><strong>'+routeLabel('Você abre a conversa','Start the conversation','Tú empiezas la conversación')+'</strong>'+
    '<p>'+routeLabel('Use a palavra abaixo para abrir a conversa. Em seguida, imagine o que a outra pessoa diria.','Start with the word below. Then imagine the other person’s reply.','Empieza con la palabra de abajo. Luego imagina la respuesta de la otra persona.')+'</p></div>'+
    '<div class="roleplay-cue" data-role-cue="1"><strong>'+routeLabel('A outra pessoa começa','The other person starts','La otra persona empieza')+'</strong>'+
    nativeText(opening,'p')+pinyinLine(opening)+lessonPlayButton(opening,{compact:true})+'</div>'+
    '<div class="roleplay-word"><strong>'+routeLabel('Sua palavra de apoio','Your cue word','Tu palabra de apoyo')+'</strong>'+
    nativeText(extensionTarget(scene)[0])+lessonVocabularyAudio(extensionTarget(scene)[0])+'</div>'+
    '<p class="workshop-keyword"><strong>'+routeLabel('Expressão da lição','Lesson expression','Expresión de la lección')+'</strong>'+nativeText(vocabulary.expression)+lessonPlayButton(vocabulary.expression,{compact:true})+'</p>'+
    roleplayWriting(theme,scene)+
    '<details class="roleplay-model"><summary>'+routeLabel('Ouvir uma versão de referência','Hear a sample version','Oír una versión de referencia')+'</summary><p>'+
    routeLabel('Esta versão mostra a cena antes do imprevisto. Compare e acrescente o seu detalhe.','This example shows the scene before the twist. Compare it and add your own detail.','Este ejemplo muestra la escena antes del giro. Compara y añade tu propio detalle.')+'</p>'+
    '<div class="roleplay-model-lines">'+nativeText(opening,'p')+pinyinLine(opening)+'<p lang="'+supportTag()+'">'+clean(first)+'</p>'+lessonPlayButton(opening,{compact:true})+
    nativeText(reply,'p')+pinyinLine(reply)+'<p lang="'+supportTag()+'">'+clean(second)+'</p>'+lessonPlayButton(reply,{compact:true,voice:1})+
    nativeText(followUp,'p')+pinyinLine(followUp)+'<p lang="'+supportTag()+'">'+clean(third)+'</p>'+lessonPlayButton(followUp,{compact:true})+'</div>'+
    '</details>'+
    '<fieldset class="roleplay-check"><legend>'+routeLabel('Na minha versão eu…','In my version I…','En mi versión…')+'</legend>'+
    [
      ['Fiz uma pergunta ou dei uma resposta clara.','Asked a clear question or gave a clear reply.','Hice una pregunta o di una respuesta clara.'],
      ['Reaproveitei uma palavra ou expressão da cena.','Reused a word or expression from the scene.','Reutilicé una palabra o expresión de la escena.'],
      ['Adaptei a fala ao imprevisto.','Adapted my line to the twist.','Adapté mi intervención al giro.']
    ].map(text=>'<label><input type="checkbox">'+clean(routeLabel(...text))+'</label>').join('')+
    '<p class="roleplay-result" id="roleplayResult" role="status"></p></fieldset></section>';
}

function changeSceneRole(event){
  const roleplay=event.target.closest('.scene-roleplay');
  if(!roleplay)return;
  if(event.target.type==='checkbox'){
    const count=roleplay.querySelectorAll('.roleplay-check input:checked').length;
    $('roleplayResult').textContent=count===3?
      routeLabel('Cena completa! Troque de papel e tente de novo.','Scene complete! Swap roles and try again.','¡Escena completa! Cambia de papel y vuelve a intentarlo.'):
      routeLabel(count+' de 3 ingredientes da cena.',count+' of 3 scene ingredients.',count+' de 3 ingredientes de la escena.');
    return;
  }
  if(event.target.name!=='sceneRole')return;
  for(const cue of roleplay.querySelectorAll('[data-role-cue]'))cue.hidden=cue.dataset.roleCue!==event.target.value;
  resetSceneRoleplay(roleplay);
}
function resetSceneRoleplay(roleplay){
  roleplay.querySelector('.roleplay-model').open=false;
  $('roleplayResult').textContent='';
  for(const check of roleplay.querySelectorAll('.roleplay-check input'))check.checked=false;
}
function handleSceneRoleplay(event){
  const jump=event.target.closest('[data-scene-jump]');
  if(jump){
    event.preventDefault();
    openLessonSection('workshop');
    return true;
  }
  const button=event.target.closest('[data-scene-twist]');
  if(!button)return false;
  const scene=sceneExtensionAt(lessonVisualTheme());
  const next=(Number(button.dataset.sceneTwist)+1)%scene.twists.length;
  button.dataset.sceneTwist=String(next);
  $('sceneTwist').textContent=routeLabel(...scene.twists[next]);
  resetSceneRoleplay(button.closest('.scene-roleplay'));
  return true;
}
