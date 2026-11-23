// Two starts for each role, followed by two starts for the person replying.
const roleplayFragments={
 cup:{
 pt:'O que você quer …?|Você prefere …?|Para viagem, e também quero …|Prefiro tomar aqui porque …',
 eng:'What would you like …?|Would you prefer …?|To go, please. I’d also like …|I’d rather stay here because …',
 spa:'¿Qué quiere …?|¿Prefiere …?|Para llevar. También quiero …|Prefiero tomarlo aquí porque …',
 ita:'Che cosa desidera …?|Preferisce …?|Da portare via. Vorrei anche …|Preferisco prenderlo qui perché …',
 deu:'Was möchten Sie …?|Möchten Sie lieber …?|Zum Mitnehmen. Ich hätte auch gern …|Ich bleibe lieber hier, weil …',
 ara:'مَاذَا تُرِيدُ …؟|هَلْ تُفَضِّلُ …؟|سَآخُذُهُ مَعِي، وَأُرِيدُ أَيْضًا …|أُفَضِّلُ أَنْ أَبْقَى هُنَا لِأَنَّ …',
 jpn:'…は何になさいますか。|…と…、どちらがいいですか。|持ち帰りで、…もお願いします。|…ので、店内でお願いします。',
 cmn:'您想要……？|您更想要……吗？|我想带走，还要……。|我想在这儿喝，因为……。'
 },
 ticket:{
 pt:'De que plataforma sai o trem para …?|Que horas sai o próximo trem para …?|Sai da plataforma …|O próximo trem sai às …',
 eng:'Which platform is the train to … on?|What time is the next train to …?|It leaves from platform …|The next train leaves at …',
 spa:'¿De qué andén sale el tren a …?|¿A qué hora sale el próximo tren a …?|Sale del andén …|El próximo tren sale a las …',
 ita:'Da quale binario parte il treno per …?|A che ora parte il prossimo treno per …?|Parte dal binario …|Il prossimo treno parte alle …',
 deu:'Von welchem Gleis fährt der Zug nach … ab?|Wann fährt der nächste Zug nach …?|Er fährt von Gleis … ab.|Der nächste Zug fährt um … ab.',
 ara:'مِنْ أَيِّ رَصِيفٍ يُغَادِرُ الْقِطَارُ إِلَى …؟|مَتَى يُغَادِرُ الْقِطَارُ التَّالِي إِلَى …؟|يُغَادِرُ مِنَ الرَّصِيفِ …|يُغَادِرُ الْقِطَارُ التَّالِي فِي السَّاعَةِ …',
 jpn:'…行きの電車は何番ホームから出ますか。|…行きの次の電車は何時ですか。|…番ホームから出ます。|次の電車は…時に出ます。',
 cmn:'去……的火车从哪个站台出发？|去……的下一班火车几点开？|从……号站台出发。|下一班火车……点开。'
 },
 city:{
 pt:'Tem uma … neste bairro?|Onde fica …?|Sim, tem uma perto de …|Dá para ir a pé até …',
 eng:'Is there a … in this neighborhood?|Where can I find …?|Yes, there’s one near …|You can walk to …',
 spa:'¿Hay una … en este barrio?|¿Dónde puedo encontrar …?|Sí, hay una cerca de …|Puedes ir a pie hasta …',
 ita:'C’è una … in questo quartiere?|Dove posso trovare …?|Sì, ce n’è una vicino a …|Puoi andare a piedi fino a …',
 deu:'Gibt es hier im Viertel eine …?|Wo finde ich …?|Ja, es gibt eine in der Nähe von …|Du kannst zu Fuß zu … gehen.',
 ara:'هَلْ يُوجَدُ … فِي هَذَا الْحَيِّ؟|أَيْنَ أَجِدُ …؟|نَعَمْ، هُنَاكَ وَاحِدٌ قُرْبَ …|يُمْكِنُكَ الذَّهَابُ مَشْيًا إِلَى …',
 jpn:'この近所に…はありますか。|…はどこにありますか。|はい、…の近くにあります。|…まで歩いて行けます。',
 cmn:'这个街区有……吗？|在哪儿能找到……？|有，就在……附近。|可以走路去……。'
 },
 chat:{
 pt:'Que horário funciona para você no …?|A gente pode se encontrar em …?|Para mim funciona às …|Prefiro me encontrar em …',
 eng:'What time works for you on …?|Could we meet at …?|… works for me.|I’d rather meet at …',
 spa:'¿Qué hora te viene bien el …?|¿Podemos quedar en …?|A las … me viene bien.|Prefiero quedar en …',
 ita:'A che ora ti va bene …?|Possiamo vederci a …?|Per me va bene alle …|Preferisco vederci a …',
 deu:'Welche Uhrzeit passt dir am …?|Können wir uns bei … treffen?|… Uhr passt mir.|Ich würde mich lieber bei … treffen.',
 ara:'أَيُّ وَقْتٍ يُنَاسِبُكَ يَوْمَ …؟|هَلْ يُمْكِنُنَا أَنْ نَلْتَقِيَ عِنْدَ …؟|السَّاعَةُ … تُنَاسِبُنِي.|أُفَضِّلُ أَنْ نَلْتَقِيَ عِنْدَ …',
 jpn:'…なら何時がいいですか。|…で会えますか。|…時なら大丈夫です。|…で会ったほうがいいです。',
 cmn:'……你几点方便？|我们能在……见面吗？|我……点方便。|我更想在……见面。'
 },
 notebook:{
 pt:'Posso anotar … no caderno?|Você pode repetir …?|Claro. Anote primeiro …|Posso repetir … mais devagar.',
 eng:'Can I write … in my notebook?|Could you repeat …?|Sure. Write down … first.|I can repeat … more slowly.',
 spa:'¿Puedo apuntar … en mi cuaderno?|¿Puedes repetir …?|Claro. Apunta primero …|Puedo repetir … más despacio.',
 ita:'Posso scrivere … sul quaderno?|Puoi ripetere …?|Certo. Scrivi prima …|Posso ripetere … più lentamente.',
 deu:'Kann ich … in mein Heft schreiben?|Kannst du … wiederholen?|Klar. Schreib zuerst … auf.|Ich kann … langsamer wiederholen.',
 ara:'هَلْ يُمْكِنُنِي كِتَابَةُ … فِي دَفْتَرِي؟|هَلْ يُمْكِنُكَ إِعَادَةُ …؟|بِالطَّبْعِ. اكْتُبْ أَوَّلًا …|يُمْكِنُنِي إِعَادَةُ … بِبُطْءٍ.',
 jpn:'…をノートに書いてもいいですか。|…をもう一度言ってくれますか。|もちろんです。まず…を書いてください。|…をもう少しゆっくり言います。',
 cmn:'我可以把……写在笔记本上吗？|可以再说一遍……吗？|当然，先记下……。|我可以把……说慢一点。'
 },
 park:{
 pt:'Vamos dar uma volta perto de …?|Você prefere ir para …?|Boa ideia. Vamos às …|Prefiro ir para …',
 eng:'Want to take a walk near …?|Would you rather go to …?|Good idea. Let’s go at …|I’d rather go to …',
 spa:'¿Damos una vuelta cerca de …?|¿Prefieres ir a …?|Buena idea. Vamos a las …|Prefiero ir a …',
 ita:'Facciamo un giro vicino a …?|Preferisci andare a …?|Buona idea. Andiamo alle …|Preferisco andare a …',
 deu:'Wollen wir bei … spazieren gehen?|Möchtest du lieber zu … gehen?|Gute Idee. Gehen wir um … Uhr.|Ich würde lieber zu … gehen.',
 ara:'هَلْ نَتَنَزَّهُ قُرْبَ …؟|هَلْ تُفَضِّلُ الذَّهَابَ إِلَى …؟|فِكْرَةٌ جَيِّدَةٌ. لِنَذْهَبْ فِي السَّاعَةِ …|أُفَضِّلُ الذَّهَابَ إِلَى …',
 jpn:'…の近くを散歩しませんか。|…へ行きたいですか。|いいですね。…時に行きましょう。|…へ行きたいです。',
 cmn:'我们去……附近走走吧？|你更想去……吗？|好主意。我们……点去吧。|我更想去……。'
 },
 health:{
 pt:'Tenho uma consulta marcada para …|Bom dia. Uma consulta em nome de …|Qual é o seu …?|A consulta está marcada para …',
 eng:'I have an appointment at …|Good morning. The appointment is under …|May I have your …?|Your appointment is at …',
 spa:'Tengo una cita a las …|Buenos días. La cita está a nombre de …|¿Me da su …?|Su cita es a las …',
 ita:'Ho un appuntamento alle …|Buongiorno. L’appuntamento è a nome di …|Mi può dire il suo …?|Il suo appuntamento è alle …',
 deu:'Ich habe um … einen Termin.|Guten Morgen. Der Termin ist auf den Namen … eingetragen.|Wie lautet Ihr …?|Ihr Termin ist um … Uhr.',
 ara:'لَدَيَّ مَوْعِدٌ فِي السَّاعَةِ …|صَبَاحُ الْخَيْرِ. الْمَوْعِدُ بِاسْمِ …|مَا …، مِنْ فَضْلِكَ؟|مَوْعِدُكَ فِي السَّاعَةِ …',
 jpn:'…時に予約しています。|おはようございます。…の名前で予約しています。|…をお願いします。|ご予約は…時です。',
 cmn:'我预约了……点。|您好，我用……的名字预约了。|请问您的……是什么？|您的预约在……点。'
 },
 map:{
 pt:'Em que andar fica …?|Onde fica …?|Fica no … andar.|O elevador fica perto de …',
 eng:'What floor is … on?|Where is …?|It’s on the … floor.|The elevator is near …',
 spa:'¿En qué piso está …?|¿Dónde está …?|Está en el … piso.|El ascensor está cerca de …',
 ita:'A che piano è …?|Dov’è …?|È al … piano.|L’ascensore è vicino a …',
 deu:'In welchem Stock ist …?|Wo ist …?|Es ist im … Stock.|Der Aufzug ist in der Nähe von …',
 ara:'فِي أَيِّ طَابِقٍ يَقَعُ …؟|أَيْنَ …؟|فِي الطَّابِقِ …|الْمِصْعَدُ قُرْبَ …',
 jpn:'…は何階ですか。|…はどこですか。|…階です。|エレベーターは…の近くです。',
 cmn:'……在几楼？|……在哪儿？|在……楼。|电梯在……附近。'
 }
};
const roleplayHints={
  cup:['Complete com uma bebida ou outra opção do cardápio.','Complete with a drink or another item on the menu.','Completa con una bebida u otra opción del menú.'],
  ticket:['Use um destino, um número de plataforma ou um horário.','Use a destination, a platform number or a time.','Usa un destino, un número de andén o una hora.'],
  city:['Use um comércio, um ponto de referência ou outro lugar do bairro.','Use a shop, a landmark or another place in the neighborhood.','Usa un comercio, un punto de referencia u otro lugar del barrio.'],
  chat:['Use um dia, um horário ou um local para o encontro.','Use a day, a time or a meeting place.','Usa un día, una hora o un lugar para quedar.'],
  notebook:['Use uma instrução ou um detalhe que vale a pena anotar.','Use an instruction or a detail worth writing down.','Usa una instrucción o un detalle que convenga anotar.'],
  park:['Use um caminho, um lugar para passear ou um horário.','Use a path, somewhere to walk or a time.','Usa un sendero, un lugar para pasear o una hora.'],
  health:['Use um nome, uma hora ou um dado necessário na recepção.','Use a name, a time or a detail the receptionist needs.','Usa un nombre, una hora o un dato necesario en recepción.'],
  map:['Use um lugar do hotel, um andar ou um ponto de referência.','Use a place in the hotel, a floor or a landmark.','Usa un lugar del hotel, un piso o un punto de referencia.']
};
const roleplayCueWords={
  cup:['chá|um pão com queijo','tea|a cheese sandwich','té|un bocadillo de queso','tè|un panino al formaggio','Tee|ein Käsebrötchen','شَاي|شَطِيرَة جُبْن','紅茶|チーズサンド','茶|奶酪三明治'],
  ticket:['a próxima cidade|dez horas','the next town|ten o’clock','la ciudad vecina|las diez','la città vicina|le dieci','die Nachbarstadt|zehn Uhr','الْمَدِينَة الْمُجَاوِرَة|السَّاعَة الْعَاشِرَة','隣の町|十時','邻镇|十点'],
  city:['uma padaria|a estação','a bakery|the station','una panadería|la estación','una panetteria|la stazione','eine Bäckerei|der Bahnhof','مَخْبَز|الْمَحَطَّة','パン屋|駅','面包店|车站'],
  chat:['domingo|o restaurante','Sunday|the restaurant','domingo|el restaurante','domenica|il ristorante','Sonntag|das Restaurant','يَوْم الْأَحَد|الْمَطْعَم','日曜日|レストラン','星期天|餐厅'],
  notebook:['a pergunta|o horário','the question|the time','la pregunta|la hora','la domanda|l’orario','die Frage|die Uhrzeit','السُّؤَال|الْوَقْت','質問|時間','问题|时间'],
  park:['o lago|quatro horas','the lake|four o’clock','el lago|las cuatro','il lago|le quattro','der See|vier Uhr','الْبُحَيْرَة|السَّاعَة الرَّابِعَة','湖|四時','湖边|四点'],
  health:['Alex Silva|duas horas','Alex Silva|two o’clock','Alex Silva|las dos','Alex Silva|le due','Alex Silva|zwei Uhr','أَلِكْس سِيلْفَا|السَّاعَة الثَّانِيَة','アレックス・シルバ|二時','亚历克斯·席尔瓦|两点'],
  map:['o elevador|a recepção','the elevator|the front desk','el ascensor|la recepción','l’ascensore|la reception','der Aufzug|die Rezeption','الْمِصْعَد|الِاسْتِقْبَال','エレベーター|フロント','电梯|前台']
};
const roleplayDrafts=new Map();
function storeRoleplayDraft(text){
  const key=lessonHash(unit);
  if(text)roleplayDrafts.set(key,text);else roleplayDrafts.delete(key);
}
function roleplayWriting(theme,scene){
  const fragments=(roleplayFragments[theme]||roleplayFragments.map)[lang==='por'?'pt':lang].split('|');
  const prompts=[
    ['Escolha um molde e complete uma fala.','Choose a template and complete one line.','Elige un molde y completa una intervención.'],
    ['Complete um molde e acrescente um detalhe do imprevisto.','Complete a template and add a detail about the twist.','Completa un molde y añade un detalle del imprevisto.'],
    ['Reescreva a fala para lidar com o imprevisto. Em seguida, explique o motivo em uma segunda frase.','Rewrite the line to deal with the twist. Explain why in a second sentence.','Reescribe la intervención para resolver el imprevisto. Explica el motivo en una segunda frase.'],
    ['Proponha uma solução e faça uma pergunta de seguimento adequada ao seu papel.','Offer a solution and ask a follow-up question that fits your role.','Propón una solución y haz una pregunta de seguimiento adecuada a tu papel.'],
    ['Improvise uma resposta com uma alternativa. Ajuste o registro à pessoa com quem você está falando.','Improvise a reply with an alternative. Match your register to the person you are speaking to.','Improvisa una respuesta con una alternativa. Ajusta el registro a tu interlocutor.'],
    ['Escreva uma resposta que antecipe uma objeção e dê espaço para a outra pessoa negociar.','Write a reply that anticipates an objection and leaves room to negotiate.','Escribe una respuesta que se anticipe a una objeción y deje margen para negociar.']
  ];
  const target=extensionTarget(scene),translated=extensionTranslation(scene);
  const label=routeLabel('Modelo completo','Full example','Modelo completo');
  const pairs=[0,1].map(role=>'<div data-role-cue="'+role+'"'+(role===0?' hidden':'')+'>'+
    '<p class="roleplay-sample"><strong>'+label+'</strong> '+nativeText(target[role+1])+lessonPlayButton(target[role+1],{compact:true,voice:role})+
    '<span class="meta" lang="'+supportTag()+'">'+clean(translated[role+1])+'</span></p>'+
    '<ol class="roleplay-fragments">'+fragments.slice(role*2,role*2+2).map(text=>'<li>'+nativeText(text)+'</li>').join('')+'</ol></div>').join('');
  const cueWords=roleplayCueWords[theme]||roleplayCueWords.map;
  const cueLocale=['por','eng','spa','ita','deu','ara','jpn','cmn'].indexOf(lang);
  const aid=pairs+'<p class="meta" id="roleplayHint">'+clean(routeLabel(...(roleplayHints[theme]||roleplayHints.map)))+'</p>'+
    '<ul class="roleplay-cue-words">'+cueWords[cueLocale].split('|').map(word=>'<li>'+nativeText(word)+lessonVocabularyAudio(word)+'</li>').join('')+'</ul>';
  const suggestions=level<2?aid:'<details class="roleplay-writing-aid"><summary>'+
    routeLabel('Ver modelo, moldes e dica','Show example, templates and hint','Ver ejemplo, moldes y pista')+'</summary>'+aid+'</details>';
  return '<div class="roleplay-writing"><p id="roleplayWritingPrompt">'+routeLabel(...prompts[level])+'</p>'+suggestions+
    '<label for="roleplayDraft">'+routeLabel('Escreva sua versão','Write your version','Escribe tu versión')+'</label>'+
    '<textarea id="roleplayDraft" rows="'+(level<2?3:4)+'" lang="'+languages[lang][2]+'" dir="auto" aria-describedby="roleplayWritingPrompt">'+
    clean(roleplayDrafts.get(lessonHash(unit))||'')+'</textarea></div>';
}
