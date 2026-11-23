// Four exchanges per setting. The paired rows keep the turn order consistent across courses.
const dialoguePracticeText={
cup:{
pt:'O que vai querer beber?|Um chá, por favor.|Quer algo para comer?|Um pão com queijo.|Vai comer aqui?|Não, é para viagem.|Quer pagar agora?|Sim. Posso pagar com cartão?',
eng:'What would you like to drink?|Tea, please.|Would you like something to eat?|A cheese sandwich.|Will you be eating here?|No, it’s to go.|Would you like to pay now?|Yes. Can I pay by card?',
spa:'¿Qué le pongo para beber?|Un té, por favor.|¿Quiere algo de comer?|Un bocadillo de queso.|¿Va a comer aquí?|No, es para llevar.|¿Quiere pagar ahora?|Sí. ¿Puedo pagar con tarjeta?',
ita:'Cosa prende da bere?|Un tè, per favore.|Vuole anche qualcosa da mangiare?|Un panino al formaggio.|Mangia qui?|No, è da portare via.|Vuole pagare adesso?|Sì. Posso pagare con la carta?',
deu:'Was möchten Sie trinken?|Einen Tee, bitte.|Möchten Sie auch etwas essen?|Ein Käsebrötchen.|Essen Sie hier?|Nein, zum Mitnehmen.|Möchten Sie jetzt zahlen?|Ja. Kann ich mit Karte zahlen?',
ara:'مَاذَا تُرِيدُ أَنْ تَشْرَبَ؟|شَايًا، مِنْ فَضْلِكَ.|هَلْ تُرِيدُ شَيْئًا لِلْأَكْلِ؟|شَطِيرَةَ جُبْنٍ.|هَلْ سَتَأْكُلُ هُنَا؟|لَا، سَآخُذُ الطَّلَبَ مَعِي.|هَلْ تُرِيدُ الدَّفْعَ الآنَ؟|نَعَمْ. هَلْ يُمْكِنُنِي الدَّفْعُ بِالْبِطَاقَةِ؟',
jpn:'お飲み物は何になさいますか。|紅茶をお願いします。|お食事はいかがですか。|チーズサンドをお願いします。|店内でお召し上がりですか。|いいえ、持ち帰りです。|お会計は今なさいますか。|はい。カードで払えますか。',
cmn:'您想喝点儿什么？|请给我一杯茶。|您想吃点儿什么吗？|我想要一个奶酪三明治。|您在这儿吃吗？|不，我要打包带走。|您现在结账吗？|是的。可以刷卡吗？'
},
ticket:{
pt:'Bom dia. Tem trem para a cidade vizinha hoje?|Sim, o próximo sai às dez.|Dá para voltar hoje à tarde?|Sim, há um trem de volta às cinco.|Então quanto custa a ida e volta?|Trinta euros.|Pode me dizer de qual plataforma sai o das dez?|Da plataforma dois. Boa viagem!',
eng:'Good morning. Is there a train to the next town today?|Yes, the next one leaves at ten.|Can I come back this afternoon?|Yes, there’s a return train at five.|How much is a round-trip ticket, then?|Thirty euros.|Which platform does the ten o’clock train leave from?|Platform two. Have a good trip!',
spa:'Buenos días. ¿Hay tren para la ciudad vecina hoy?|Sí, el próximo sale a las diez.|¿Puedo volver esta tarde?|Sí, hay un tren de vuelta a las cinco.|Entonces, ¿cuánto cuesta el billete de ida y vuelta?|Treinta euros.|¿De qué andén sale el tren de las diez?|Del andén dos. ¡Buen viaje!',
ita:'Buongiorno. C’è un treno per la città vicina oggi?|Sì, il prossimo parte alle dieci.|Posso tornare oggi pomeriggio?|Sì, c’è un treno di ritorno alle cinque.|Quanto costa allora un biglietto di andata e ritorno?|Trenta euro.|Da quale binario parte quello delle dieci?|Dal binario due. Buon viaggio!',
deu:'Guten Morgen. Fährt heute ein Zug in die Nachbarstadt?|Ja, der nächste fährt um zehn.|Kann ich heute Nachmittag zurückfahren?|Ja, um fünf fährt ein Zug zurück.|Was kostet dann eine Fahrkarte für Hin- und Rückfahrt?|Dreißig Euro.|Von welchem Gleis fährt der Zug um zehn ab?|Von Gleis zwei. Gute Reise!',
ara:'صَبَاحُ الخَيْرِ. هَلْ هُنَاكَ قِطَارٌ إِلَى الْمَدِينَةِ الْمُجَاوِرَةِ الْيَوْمَ؟|نَعَمْ، الْقِطَارُ التَّالِي يُغَادِرُ فِي الْعَاشِرَةِ.|هَلْ يُمْكِنُنِي الْعَوْدَةُ بَعْدَ الظُّهْرِ؟|نَعَمْ، هُنَاكَ قِطَارُ عَوْدَةٍ فِي الْخَامِسَةِ.|كَمْ سِعْرُ تَذْكِرَةِ الذَّهَابِ وَالْعَوْدَةِ إِذَنْ؟|ثَلَاثُونَ يُورُو.|مِنْ أَيِّ رَصِيفٍ يُغَادِرُ قِطَارُ الْعَاشِرَةِ؟|مِنَ الرَّصِيفِ الثَّانِي. رِحْلَةً سَعِيدَةً!',
jpn:'おはようございます。今日、隣の町へ行く電車はありますか。|はい、次は十時に出ます。|今日の午後に戻れますか。|はい、帰りの電車は五時に出ます。|では、往復切符はいくらですか。|三十ユーロです。|十時の電車は何番ホームから出ますか。|二番ホームです。お気をつけて。',
cmn:'您好，今天有去邻镇的火车吗？|有，下一班十点发车。|今天下午能回来吗？|能，五点有一班回程车。|那往返票多少钱？|三十欧元。|十点的车从哪个站台发车？|二号站台。祝您一路顺风！'
},
city:{
pt:'Você cresceu nesta cidade?|Não, cresci numa cidade pequena perto do mar.|O que você mais gostava de fazer lá?|Eu gostava de andar pela praia.|Tem algum lugar aqui para caminhar perto da água?|Tem um caminho bonito à beira do rio.|Quer me mostrar o caminho amanhã de manhã?|Quero. Vamos nos encontrar na ponte às nove.',
eng:'Did you grow up in this city?|No, I grew up in a small town by the sea.|What did you like doing there?|I liked walking along the beach.|Is there anywhere to walk by the water here?|There’s a lovely path by the river.|Can you show me the path tomorrow morning?|Sure. Let’s meet on the bridge at nine.',
spa:'¿Creciste en esta ciudad?|No, crecí en un pueblo pequeño junto al mar.|¿Qué te gustaba hacer allí?|Me gustaba pasear por la playa.|¿Hay algún sitio por aquí para caminar junto al agua?|Hay un sendero precioso al lado del río.|¿Me enseñas el sendero mañana por la mañana?|Claro. Quedamos en el puente a las nueve.',
ita:'Sei cresciuto in questa città?|No, sono cresciuto in un paesino sul mare.|Che cosa ti piaceva fare lì?|Mi piaceva passeggiare sulla spiaggia.|Qui c’è un posto dove camminare vicino all’acqua?|C’è un bel sentiero lungo il fiume.|Mi fai vedere il sentiero domani mattina?|Certo. Ci vediamo sul ponte alle nove.',
deu:'Bist du in dieser Stadt aufgewachsen?|Nein, ich bin in einer kleinen Stadt am Meer aufgewachsen.|Was hast du dort gern gemacht?|Ich bin gern am Strand spazieren gegangen.|Kann man hier irgendwo am Wasser spazieren gehen?|Am Fluss gibt es einen schönen Weg.|Zeigst du mir den Weg morgen früh?|Klar. Treffen wir uns um neun auf der Brücke.',
ara:'هَلْ نَشَأْتَ فِي هَذِهِ الْمَدِينَةِ؟|لَا، نَشَأْتُ فِي بَلْدَةٍ صَغِيرَةٍ قُرْبَ الْبَحْرِ.|مَاذَا كُنْتَ تُحِبُّ أَنْ تَفْعَلَ هُنَاكَ؟|كُنْتُ أُحِبُّ الْمَشْيَ عَلَى الشَّاطِئِ.|هَلْ يُوجَدُ مَكَانٌ لِلْمَشْيِ قُرْبَ الْمَاءِ هُنَا؟|هُنَاكَ مَمَرٌّ جَمِيلٌ بِجَانِبِ النَّهْرِ.|هَلْ تُرِينِي الْمَمَرَّ غَدًا صَبَاحًا؟|بِالطَّبْعِ. لِنَلْتَقِ عَلَى الْجِسْرِ فِي التَّاسِعَةِ.',
jpn:'この街で育ったんですか。|いいえ、海のそばの小さな町で育ちました。|そこでは何をするのが好きでしたか。|海辺を散歩するのが好きでした。|この辺にも水辺を歩ける場所はありますか。|川沿いにいい遊歩道がありますよ。|明日の朝、その道を案内してくれますか。|いいですよ。九時に橋の上で会いましょう。',
cmn:'你是在这个城市长大的吗？|不是，我在海边的一个小镇长大。|你在那里喜欢做什么？|我喜欢沿着海滩散步。|这儿有能在水边散步的地方吗？|河边有一条很漂亮的小路。|你明天早上能带我去看看那条小路吗？|可以。我们九点在桥上见。'
},
chat:{
pt:'Você quer jantar comigo no domingo?|Quero, mas só posso depois das oito.|Que tipo de comida você quer comer?|Comida italiana seria uma boa.|Onde a gente se encontra?|Na entrada do restaurante.|Então posso reservar uma mesa para as oito e meia?|Pode. Até domingo!',
eng:'Would you like to have dinner with me on Sunday?|I’d love to, but I’m only free after eight.|What kind of food would you like?|Italian food would be great.|Where should we meet?|At the entrance to the restaurant.|Shall I book a table for eight thirty, then?|Yes, please. See you Sunday!',
spa:'¿Quieres cenar conmigo el domingo?|Me encantaría, pero solo puedo después de las ocho.|¿Qué tipo de comida te apetece?|La comida italiana estaría genial.|¿Dónde quedamos?|En la entrada del restaurante.|Entonces, ¿reservo una mesa para las ocho y media?|Sí, por favor. ¡Hasta el domingo!',
ita:'Ti va di cenare con me domenica?|Volentieri, ma sono libero solo dopo le otto.|Che cosa ti va di mangiare?|Mi andrebbe della cucina italiana.|Dove ci vediamo?|All’entrata del ristorante.|Allora prenoto un tavolo per le otto e mezza?|Sì, grazie. A domenica!',
deu:'Möchtest du am Sonntag mit mir essen gehen?|Gern, aber ich habe erst nach acht Zeit.|Worauf hast du Lust?|Italienisches Essen wäre toll.|Wo treffen wir uns?|Am Eingang des Restaurants.|Soll ich dann einen Tisch für halb neun reservieren?|Ja, bitte. Bis Sonntag!',
ara:'هَلْ تُرِيدُ أَنْ تَتَنَاوَلَ الْعَشَاءَ مَعِي يَوْمَ الْأَحَدِ؟|بِكُلِّ سُرُورٍ، لَكِنَّنِي لَا أَسْتَطِيعُ قَبْلَ الثَّامِنَةِ.|مَا نَوْعُ الطَّعَامِ الَّذِي تُفَضِّلُهُ؟|الطَّعَامُ الْإِيطَالِيُّ خِيَارٌ رَائِعٌ.|أَيْنَ نَلْتَقِي؟|عِنْدَ مَدْخَلِ الْمَطْعَمِ.|هَلْ أَحْجِزُ طَاوِلَةً لِلثَّامِنَةِ وَالنِّصْفِ إِذَنْ؟|نَعَمْ، مِنْ فَضْلِكَ. إِلَى اللِّقَاءِ يَوْمَ الْأَحَدِ!',
jpn:'日曜日に一緒に夕食を食べませんか。|いいですね。でも八時過ぎなら大丈夫です。|何が食べたいですか。|イタリア料理がいいです。|どこで会いましょうか。|レストランの入り口で会いましょう。|では、八時半に席を予約しましょうか。|お願いします。日曜日に会いましょう！',
cmn:'星期天想和我一起吃晚饭吗？|好啊，不过我八点以后才有空。|你想吃什么菜？|意大利菜不错。|我们在哪儿见？|在餐厅门口见吧。|那我订八点半的位子，好吗？|好，麻烦你了。星期天见！'
},
notebook:{
pt:'Você está com o caderno da aula?|Sim, está aberto na página cinco.|Qual é a primeira tarefa?|Ler o parágrafo no alto da página.|Quem vai anotar a resposta?|Eu anoto enquanto você lê.|Onde entregamos a atividade?|Na mesa da professora, antes de sair.',
eng:'Do you have your class notebook with you?|Yes, it’s open to page five.|What’s the first task?|Read the paragraph at the top of the page.|Who’s going to write down the answer?|I’ll write it down while you read.|Where do we turn in the assignment?|On the teacher’s desk before we leave.',
spa:'¿Tienes el cuaderno de clase?|Sí, está abierto por la página cinco.|¿Cuál es la primera tarea?|Leer el párrafo de arriba.|¿Quién va a apuntar la respuesta?|La apunto yo mientras lees.|¿Dónde entregamos la actividad?|En la mesa de la profesora, antes de salir.',
ita:'Hai il quaderno della lezione?|Sì, è aperto a pagina cinque.|Qual è il primo compito?|Leggere il paragrafo in cima alla pagina.|Chi scrive la risposta?|La scrivo io mentre leggi.|Dove consegniamo il lavoro?|Sulla cattedra dell’insegnante, prima di uscire.',
deu:'Hast du dein Heft für den Unterricht dabei?|Ja, es ist bei Seite fünf aufgeschlagen.|Was ist die erste Aufgabe?|Den Absatz oben auf der Seite lesen.|Wer schreibt die Antwort auf?|Ich schreibe sie auf, während du liest.|Wo geben wir die Aufgabe ab?|Auf dem Tisch der Lehrerin, bevor wir gehen.',
ara:'هَلْ مَعَكَ دَفْتَرُ الدَّرْسِ؟|نَعَمْ، هُوَ مَفْتُوحٌ عَلَى الصَّفْحَةِ الْخَامِسَةِ.|مَا الْمَهَمَّةُ الْأُولَى؟|قِرَاءَةُ الْفِقْرَةِ فِي أَعْلَى الصَّفْحَةِ.|مَنْ سَيَكْتُبُ الْإِجَابَةَ؟|سَأَكْتُبُهَا أَنَا بَيْنَمَا تَقْرَأُ أَنْتَ.|أَيْنَ نُسَلِّمُ الْوَاجِبَ؟|عَلَى مَكْتَبِ الْمُعَلِّمَةِ قَبْلَ أَنْ نَخْرُجَ.',
jpn:'授業のノートを持っていますか。|はい、五ページを開いています。|最初の課題は何ですか。|ページの上の段落を読むことです。|誰が答えを書きますか。|あなたが読んでいる間に私が書きます。|課題はどこに出しますか。|帰る前に先生の机の上に置きます。',
cmn:'你带课堂笔记本了吗？|带了，已经翻到第五页了。|第一项任务是什么？|读这一页最上面的那一段。|谁来写下答案？|你读的时候我来写。|我们把作业交到哪里？|离开前放在老师的桌子上。'
},
park:{
pt:'Quer dar uma volta no parque?|Quero. Vamos pelo caminho do lago.|Quanto tempo leva para chegar ao lago?|Uns quinze minutos a pé.|Será que precisamos levar alguma coisa?|Só água. Hoje está quente.|Onde a gente se encontra?|Na entrada do parque, às quatro.',
eng:'Want to take a walk in the park?|Sure. Let’s take the path to the lake.|How long does it take to get there?|About fifteen minutes on foot.|Should we bring anything?|Just water. It’s hot today.|Where should we meet?|At the park entrance at four.',
spa:'¿Te apetece dar una vuelta por el parque?|Sí. Vamos por el camino del lago.|¿Cuánto se tarda en llegar al lago?|Unos quince minutos a pie.|¿Tenemos que llevar algo?|Solo agua. Hoy hace calor.|¿Dónde quedamos?|En la entrada del parque a las cuatro.',
ita:'Ti va di fare un giro al parco?|Sì. Prendiamo il sentiero per il lago.|Quanto ci vuole per arrivare al lago?|Circa un quarto d’ora a piedi.|Dobbiamo portare qualcosa?|Solo dell’acqua. Oggi fa caldo.|Dove ci vediamo?|All’ingresso del parco alle quattro.',
deu:'Hast du Lust auf einen Spaziergang im Park?|Gern. Nehmen wir den Weg zum See.|Wie lange braucht man bis zum See?|Ungefähr fünfzehn Minuten zu Fuß.|Sollen wir etwas mitbringen?|Nur Wasser. Heute ist es heiß.|Wo treffen wir uns?|Um vier am Eingang zum Park.',
ara:'هَلْ تُرِيدُ أَنْ نَتَنَزَّهَ فِي الْحَدِيقَةِ؟|نَعَمْ. لِنَسْلُكِ الطَّرِيقَ إِلَى الْبُحَيْرَةِ.|كَمْ يَسْتَغْرِقُ الْوُصُولُ إِلَى الْبُحَيْرَةِ؟|حَوَالَيْ خَمْسَ عَشْرَةَ دَقِيقَةً مَشْيًا.|هَلْ نَحْتَاجُ إِلَى إِحْضَارِ شَيْءٍ؟|الْمَاءَ فَقَطْ. الْجَوُّ حَارٌّ الْيَوْمَ.|أَيْنَ نَلْتَقِي؟|عِنْدَ مَدْخَلِ الْحَدِيقَةِ فِي الرَّابِعَةِ.',
jpn:'公園を散歩しませんか。|いいですね。湖へ続く道を歩きましょう。|湖までどのくらいかかりますか。|歩いて十五分くらいです。|何か持っていったほうがいいですか。|水だけでいいです。今日は暑いですから。|どこで会いましょうか。|四時に公園の入り口で会いましょう。',
cmn:'想去公园走走吗？|好啊。我们走通往湖边的那条路吧。|到湖边要多久？|走路大概十五分钟。|我们需要带点儿什么吗？|只带水就行，今天很热。|我们在哪儿见？|四点在公园门口见。'
},
health:{
pt:'Clínica do bairro, bom dia. Como posso ajudar?|Quero remarcar minha consulta.|Qual era o dia da consulta?|Era na terça-feira.|Posso marcar para quinta às duas?|Quinta às duas funciona para mim.|Você pode confirmar seu nome?|Alex Silva. Obrigado pela ajuda.',
eng:'Good morning, neighborhood clinic. How can I help?|I’d like to reschedule my appointment.|What day was your appointment on?|It was on Tuesday.|Can I book you for Thursday at two?|Thursday at two works for me.|Could you confirm your name?|Alex Silva. Thanks for your help.',
spa:'Centro de salud del barrio, buenos días. ¿En qué puedo ayudarle?|Quisiera cambiar mi cita.|¿Para qué día tenía la cita?|La tenía el martes.|¿Le va bien el jueves a las dos?|Sí, el jueves a las dos me viene bien.|¿Me confirma su nombre?|Alex Silva. Gracias por su ayuda.',
ita:'Buongiorno, ambulatorio di quartiere. Come posso aiutarla?|Vorrei spostare il mio appuntamento.|Per che giorno era fissato?|Era martedì.|Va bene giovedì alle due?|Giovedì alle due va bene.|Mi conferma il suo nome?|Alex Silva. Grazie per l’aiuto.',
deu:'Guten Morgen, Stadtteilpraxis. Wie kann ich Ihnen helfen?|Ich möchte meinen Termin verschieben.|Für welchen Tag war der Termin?|Er war am Dienstag.|Passt Ihnen Donnerstag um zwei?|Donnerstag um zwei passt mir.|Können Sie mir bitte Ihren Namen bestätigen?|Alex Silva. Danke für Ihre Hilfe.',
ara:'صَبَاحُ الخَيْرِ، عِيَادَةُ الْحَيِّ. كَيْفَ يُمْكِنُنِي مُسَاعَدَتُكَ؟|أُرِيدُ تَغْيِيرَ مَوْعِدِي.|فِي أَيِّ يَوْمٍ كَانَ الْمَوْعِدُ؟|كَانَ يَوْمَ الثُّلَاثَاءِ.|هَلْ يُنَاسِبُكَ يَوْمُ الْخَمِيسِ فِي الثَّانِيَةِ؟|نَعَمْ، يُنَاسِبُنِي الْخَمِيسُ فِي الثَّانِيَةِ.|هَلْ يُمْكِنُكَ تَأْكِيدُ اسْمِكَ؟|أَلِكْس سِيلْفَا. شُكْرًا عَلَى مُسَاعَدَتِكَ.',
jpn:'おはようございます。クリニックです。どうなさいましたか。|予約を変更したいです。|ご予約は何曜日でしたか。|火曜日でした。|木曜日の二時はいかがですか。|木曜日の二時で大丈夫です。|お名前を確認してもよろしいですか。|アレックス・シルバです。ありがとうございます。',
cmn:'您好，这里是社区诊所。有什么可以帮您的吗？|我想改一下预约。|您原来约的是星期几？|是星期二。|给您改到星期四两点，可以吗？|星期四两点我有空。|能确认一下您的姓名吗？|亚历克斯·席尔瓦。谢谢您的帮助。'
},
map:{
pt:'A Lia já voltou?|Ainda não, ela saiu para comprar pão.|Posso deixar um recado?|Claro. Pegue um papel aqui na portaria.|Pode pedir que ela me ligue antes das seis?|Posso. Vou escrever o horário também.|Como ela vai receber o recado?|Vou entregar quando ela voltar.',
eng:'Is Lia back yet?|Not yet. She went out to buy bread.|Can I leave a message?|Of course. Here’s some paper from the front desk.|Could you ask her to call me before six?|Yes. I’ll write down the time too.|How will she get the message?|I’ll give it to her when she gets back.',
spa:'¿Ya volvió Lia?|Todavía no. Salió a comprar pan.|¿Puedo dejarle un recado?|Claro. Aquí tiene papel de recepción.|¿Puede pedirle que me llame antes de las seis?|Sí. También voy a anotar la hora.|¿Cómo recibirá el recado?|Se lo daré cuando vuelva.',
ita:'Lia è già tornata?|Non ancora. È uscita a comprare il pane.|Posso lasciarle un messaggio?|Certo. Qui alla reception c’è della carta.|Può chiederle di chiamarmi prima delle sei?|Sì. Segnerò anche l’ora.|Come riceverà il messaggio?|Glielo darò quando torna.',
deu:'Ist Lia schon zurück?|Noch nicht. Sie ist Brot kaufen gegangen.|Kann ich eine Nachricht hinterlassen?|Natürlich. Hier am Empfang gibt es Papier.|Können Sie sie bitten, mich vor sechs anzurufen?|Ja. Ich schreibe die Uhrzeit auch auf.|Wie bekommt sie die Nachricht?|Ich gebe sie ihr, wenn sie zurückkommt.',
ara:'هَلْ عَادَتْ لِيَا؟|لَمْ تَعُدْ بَعْدُ. خَرَجَتْ لِشِرَاءِ الْخُبْزِ.|هَلْ يُمْكِنُنِي تَرْكُ رِسَالَةٍ لَهَا؟|بِالطَّبْعِ. تَفَضَّلْ هَذِهِ الْوَرَقَةَ مِنَ الِاسْتِقْبَالِ.|هَلْ تَطْلُبُ مِنْهَا أَنْ تَتَّصِلَ بِي قَبْلَ السَّادِسَةِ؟|نَعَمْ. سَأَكْتُبُ الْوَقْتَ أَيْضًا.|كَيْفَ سَتَصِلُهَا الرِّسَالَةُ؟|سَأُعْطِيهَا الرِّسَالَةَ عِنْدَمَا تَعُودُ.',
jpn:'リアさんはもう戻りましたか。|まだです。パンを買いに出かけました。|伝言をお願いできますか。|はい。受付に紙がありますよ。|六時までに電話をくれるように伝えてもらえますか。|はい。時間も書いておきます。|伝言はどうやって渡しますか。|戻ってきたときに渡します。',
cmn:'莉娅回来了吗？|还没有，她出去买面包了。|我可以给她留个口信吗？|当然，前台这里有纸。|能请她六点前给我打电话吗？|可以，我也会记下时间。|她怎么收到这个口信？|等她回来，我就把口信交给她。'
}
};
