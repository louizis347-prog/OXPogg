// In the Portuguese version, studied terms stay in the original language when they are discussed by name.
const readingFrames={
pt:[
`Hoje a turma trabalhou em duplas.
No meu cartão estava escrito «{word}».
O outro cartão trazia a expressão «{expression}».
{example}
No fim, juntamos os cartões para revisar no dia seguinte.
Você trouxe o cartão de hoje?
Trouxe. A palavra que anotei foi «{word}».
{reply}
No meu cartão está a expressão «{expression}».
Vamos colocar os dois no mesmo caderno?
Vamos. Amanhã a gente abre o caderno antes da aula.`,
`Antes da aula, recebi uma mensagem de voz.
A primeira parte era sobre «{word}».
A gravação também trazia a expressão «{expression}».
{example}
Guardei a mensagem para ouvir de novo no caminho de casa.
Você ouviu a mensagem que eu mandei?
Ouvi. A parte com «{word}» passou rápido.
{reply}
Agora entendi. Você também mencionou «{expression}», né?
Sim. Quer que eu mande por escrito?
Quero. Assim posso ler enquanto escuto.`,
`Encontrei duas anotações no caderno da semana passada.
Uma destacava «{word}».
A outra destacava «{expression}».
{example}
Passei as duas para uma página que vou levar para a próxima aula.
Qual parte das anotações você quer rever?
Primeiro a parte com «{word}».
{reply}
Certo. Depois a gente vê «{expression}»?
Sim. Vou separar uma página só para as duas.
Boa. Na próxima aula a gente compara as anotações.`
],
eng:[
`Today the class worked in pairs.
My card said “{word}”.
The other card had the expression “{expression}”.
{example}
In the end, we put the cards together to review them the next day.
Did you bring today’s card?
I did. The word I wrote down was “{word}”.
{reply}
My card has the expression “{expression}”.
Shall we put both cards in the same notebook?
Sure. Tomorrow we’ll open the notebook before class.`,
`Before class, I got a voice message.
The first part was about “{word}”.
The recording also included the expression “{expression}”.
{example}
I saved the message to listen to it again on my way home.
Did you listen to the message I sent?
I did. The part with “{word}” went by quickly.
{reply}
Now I get it. You mentioned “{expression}” too, right?
Yes. Would you like me to send it in writing?
Please. That way I can read while I listen.`,
`I found two notes in last week’s notebook.
One highlighted “{word}”.
The other highlighted “{expression}”.
{example}
I copied both onto a page I’ll take to the next class.
Which part of the notes do you want to review?
The part with “{word}” first.
{reply}
Okay. Shall we look at “{expression}” afterward?
Yes. I’ll set aside a page for both.
Great. We’ll compare our notes in the next class.`
],
spa:[
`Hoy trabajamos en parejas en clase.
En mi tarjeta ponía «{word}».
La otra tarjeta tenía la expresión «{expression}».
{example}
Al final juntamos las tarjetas para repasarlas al día siguiente.
¿Trajiste la tarjeta de hoy?
Sí. La palabra que anoté fue «{word}».
{reply}
En mi tarjeta está la expresión «{expression}».
¿Ponemos las dos en el mismo cuaderno?
Sí. Mañana abrimos el cuaderno antes de clase.`,
`Antes de clase recibí un mensaje de voz.
La primera parte trataba de «{word}».
En la grabación también aparecía la expresión «{expression}».
{example}
Guardé el mensaje para volver a escucharlo de camino a casa.
¿Escuchaste el mensaje que te mandé?
Sí. La parte con «{word}» pasó muy rápido.
{reply}
Ahora lo entiendo. También mencionaste «{expression}», ¿verdad?
Sí. ¿Quieres que te lo mande por escrito?
Sí, así puedo leerlo mientras escucho.`,
`Encontré dos apuntes en el cuaderno de la semana pasada.
Uno destacaba «{word}».
El otro destacaba «{expression}».
{example}
Copié los dos en una hoja que llevaré a la próxima clase.
¿Qué parte de los apuntes quieres repasar?
Primero la parte con «{word}».
{reply}
Vale. ¿Después vemos «{expression}»?
Sí. Voy a reservar una hoja para los dos.
Perfecto. En la próxima clase comparamos los apuntes.`
],
ita:[
`Oggi abbiamo lavorato a coppie in classe.
Sul mio cartoncino c’era scritto «{word}».
Sull’altro c’era l’espressione «{expression}».
{example}
Alla fine abbiamo messo insieme i cartoncini per ripassarli il giorno dopo.
Hai portato il cartoncino di oggi?
Sì. La parola che ho annotato è «{word}».
{reply}
Sul mio c’è l’espressione «{expression}».
Li mettiamo tutti e due nello stesso quaderno?
Va bene. Domani apriamo il quaderno prima della lezione.`,
`Prima della lezione ho ricevuto un messaggio vocale.
La prima parte riguardava «{word}».
Nella registrazione c’era anche l’espressione «{expression}».
{example}
Ho salvato il messaggio per riascoltarlo tornando a casa.
Hai ascoltato il messaggio che ti ho mandato?
Sì. La parte con «{word}» è passata in fretta.
{reply}
Adesso ho capito. Hai menzionato anche «{expression}», vero?
Sì. Vuoi che te lo mandi per iscritto?
Sì, così posso leggere mentre ascolto.`,
`Ho trovato due appunti nel quaderno della settimana scorsa.
Uno metteva in evidenza «{word}».
L’altro metteva in evidenza «{expression}».
{example}
Li ho copiati su un foglio che porterò alla prossima lezione.
Quale parte degli appunti vuoi ripassare?
Prima quella con «{word}».
{reply}
Va bene. Poi guardiamo «{expression}»?
Sì. Tengo da parte un foglio per tutti e due.
Ottimo. Alla prossima lezione confrontiamo gli appunti.`
],
deu:[
`Heute haben wir im Unterricht zu zweit gearbeitet.
Auf meiner Karte stand „{word}“.
Auf der anderen Karte stand der Ausdruck „{expression}“.
{example}
Zum Schluss legten wir die Karten zusammen, um sie am nächsten Tag zu wiederholen.
Hast du die Karte für heute mitgebracht?
Ja. Ich habe das Wort „{word}“ notiert.
{reply}
Auf meiner Karte steht der Ausdruck „{expression}“.
Sollen wir beide Karten ins gleiche Heft legen?
Gern. Morgen öffnen wir das Heft vor dem Unterricht.`,
`Vor dem Unterricht habe ich eine Sprachnachricht bekommen.
Im ersten Teil ging es um „{word}“.
In der Aufnahme kam auch der Ausdruck „{expression}“ vor.
{example}
Ich habe die Nachricht gespeichert, um sie auf dem Heimweg noch einmal anzuhören.
Hast du meine Nachricht angehört?
Ja. Die Stelle mit „{word}“ ging sehr schnell vorbei.
{reply}
Jetzt verstehe ich es. Du hast auch „{expression}“ erwähnt, oder?
Ja. Soll ich dir das auch schriftlich schicken?
Gern. Dann kann ich beim Zuhören mitlesen.`,
`Im Heft von letzter Woche habe ich zwei Notizen gefunden.
In der einen war „{word}“ hervorgehoben.
In der anderen war „{expression}“ hervorgehoben.
{example}
Ich habe beide auf ein Blatt übertragen, das ich zum nächsten Unterricht mitnehme.
Welchen Teil der Notizen möchtest du wiederholen?
Zuerst die Stelle mit „{word}“.
{reply}
Gut. Schauen wir uns danach „{expression}“ an?
Ja. Ich reserviere ein Blatt für beide.
Prima. Beim nächsten Unterricht vergleichen wir unsere Notizen.`
],
ara:[
`عَمِلْنَا اليَوْمَ فِي الصَّفِّ فِي مَجْمُوعَاتٍ مِنْ شَخْصَيْنِ.
كَانَ عَلَى بِطَاقَتِي «{word}».
وَفِي البِطَاقَةِ الأُخْرَى كَانَ التَّعْبِيرُ «{expression}».
{example}
وَفِي النِّهَايَةِ جَمَعْنَا البِطَاقَتَيْنِ لِنُرَاجِعَهُمَا فِي اليَوْمِ التَّالِي.
هَلْ أَحْضَرْتَ بِطَاقَةَ اليَوْمِ؟
نَعَمْ. الكَلِمَةُ الَّتِي دَوَّنْتُهَا هِيَ «{word}».
{reply}
وَعَلَى بِطَاقَتِي التَّعْبِيرُ «{expression}».
هَلْ نَضَعُ البِطَاقَتَيْنِ فِي الدَّفْتَرِ نَفْسِهِ؟
نَعَمْ. سَنَفْتَحُ الدَّفْتَرَ غَدًا قَبْلَ الدَّرْسِ.`,
`تَلَقَّيْتُ رِسَالَةً صَوْتِيَّةً قَبْلَ الدَّرْسِ.
كَانَ الجُزْءُ الأَوَّلُ عَنْ «{word}».
وَرَدَ فِي التَّسْجِيلِ أَيْضًا التَّعْبِيرُ «{expression}».
{example}
حَفِظْتُ الرِّسَالَةَ لِأَسْمَعَهَا مَرَّةً أُخْرَى فِي طَرِيقِ العَوْدَةِ إِلَى البَيْتِ.
هَلْ سَمِعْتَ الرِّسَالَةَ الَّتِي أَرْسَلْتُهَا؟
نَعَمْ. مَرَّ المَقْطَعُ الَّذِي فِيهِ «{word}» بِسُرْعَةٍ.
{reply}
الآنَ فَهِمْتُ. ذَكَرْتَ أَيْضًا «{expression}»، أَلَيْسَ كَذَلِكَ؟
نَعَمْ. هَلْ تُرِيدُ أَنْ أُرْسِلَهُ مَكْتُوبًا؟
نَعَمْ، حَتَّى أَقْرَأَهُ وَأَنَا أَسْتَمِعُ.`,
`وَجَدْتُ مُلَاحَظَتَيْنِ فِي دَفْتَرِ الأُسْبُوعِ المَاضِي.
فِي إِحْدَاهُمَا بَرَزَتْ «{word}».
وَفِي الأُخْرَى بَرَزَتْ «{expression}».
{example}
نَقَلْتُهُمَا إِلَى وَرَقَةٍ سَآخُذُهَا إِلَى الدَّرْسِ القَادِمِ.
أَيَّ جُزْءٍ مِنَ المُلاَحَظَاتِ تُرِيدُ أَنْ تُرَاجِعَ؟
أَوَّلًا الجُزْءَ الَّذِي فِيهِ «{word}».
{reply}
حَسَنًا. هَلْ نَنْظُرُ بَعْدَ ذَلِكَ فِي «{expression}»؟
نَعَمْ. سَأُخَصِّصُ وَرَقَةً لَهُمَا.
مُمْتَازٌ. سَنُقَارِنُ مُلَاحَظَاتِنَا فِي الدَّرْسِ القَادِمِ.`
],
jpn:[
`今日の授業では二人一組で作業をした。
私のカードには「{word}」と書いてあった。
もう一枚には「{expression}」という表現が書いてあった。
{example}
最後に、翌日復習できるようにカードをまとめた。
今日のカードを持ってきた？
うん。「{word}」という言葉をメモしたよ。
{reply}
私のカードには「{expression}」っていう表現があるよ。
二枚とも同じノートに入れておこうか。
そうしよう。明日、授業の前にノートを開こう。`,
`授業の前にボイスメッセージが届いた。
最初は「{word}」についての話だった。
録音には「{expression}」という表現も出てきた。
{example}
帰り道にもう一度聞くために、そのメッセージを保存した。
送ったメッセージ、聞いた？
うん。「{word}」のところが速かったよ。
{reply}
今わかった。「{expression}」も出てきたよね？
うん。文字でも送ろうか。
お願い。そうすれば聞きながら読めるよ。`,
`先週のノートに二つのメモを見つけた。
一つには「{word}」が目立つように書いてあった。
もう一つには「{expression}」が目立つように書いてあった。
{example}
二つとも紙に写して、次の授業に持っていくことにした。
メモのどこを復習したい？
まず「{word}」のところ。
{reply}
わかった。そのあとで「{expression}」を見ようか。
うん。二つのために紙を一枚用意するね。
いいね。次の授業でメモを見比べよう。`
]};
const cafeScenes={
pt:{
  eng:`Entrei no café antes do trabalho.
Pedi um café e um chá.
Queria tomar o chá ali mesmo.
O barista colocou o chá numa xícara.
Sentei perto da janela e tomei o chá.
Bom dia! O que vai querer?
Um café e um chá, por favor.
O chá é para tomar aqui ou para viagem?
O chá é para tomar aqui. O café é para viagem.
Certo. Aqui está o chá, e o café fica pronto daqui a pouco.
Obrigado! Vou esperar aqui.`,
  spa:`A caminho do trabalho, parei num café.
Pedi um café com leite.
Pedi também um sanduíche para viagem.
Colocaram o sanduíche num saco.
Saí com o café e o sanduíche.
Bom dia! O que vai querer?
Um café com leite, por favor.
Quer alguma coisa para comer?
Sim, um sanduíche para viagem.
Aqui estão o café e o sanduíche.
Obrigado. Tenha um bom dia!`,
  ita:`Parei num café antes de pegar o trem.
Pedi um café no balcão.
Pedi também um sanduíche para viagem.
O sanduíche veio num saco de papel.
Tomei o café e fui para a estação.
Bom dia! O que você vai querer?
Um café, por favor.
Mais alguma coisa?
Sim, um sanduíche para viagem.
Aqui estão o café e o sanduíche.
Obrigado! Vou levar o sanduíche para o trem.`,
  deu:`De manhã, parei numa padaria.
Pedi um café para viagem.
Também pedi dois pãezinhos.
A atendente colocou os pães num saco.
Paguei e levei tudo para o escritório.
Bom dia! O que vai querer?
Um café para viagem, por favor.
Mais alguma coisa?
Sim, dois pãezinhos, por favor.
Aqui estão. São seis euros.
Aqui estão os seis euros. Obrigado!`,
  ara:`Entrei num café depois do trabalho.
Pedi um café e me sentei perto da porta.
Tomei o café com calma.
Depois pedi a conta.
Paguei em dinheiro e voltei para casa.
Boa tarde! O que você gostaria de pedir?
Quero um café, por favor.
Aqui está seu café.
Obrigado. A conta, por favor.
Você quer pagar em dinheiro ou com cartão?
Em dinheiro, por favor. Aqui está.`,
  jpn:`No caminho para a estação, entrei num café.
Pedi um café.
Pedi para viagem.
Colocaram o café num copo com tampa.
Levei o café para a estação.
Olá! O que vai querer?
Um café, por favor.
Vai tomar aqui ou levar?
Para viagem, por favor.
Aqui está seu café.
Obrigado. Vou levá-lo para a estação.`
},
eng:`I went into the café before work.
I ordered a coffee and a tea.
I wanted the tea for here.
The barista put the tea in a cup.
I sat by the window and drank my tea.
Good morning! What would you like?
A coffee and a tea, please.
Is the tea for here or to go?
The tea is for here. The coffee is to go.
All right. Here’s the tea, and the coffee will be ready in a minute.
Thanks! I’ll wait here.`,
spa:`De camino al trabajo, paré en una cafetería.
Pedí un café con leche.
También pedí un bocadillo para llevar.
Pusieron el bocadillo en una bolsa.
Salí con el café y el bocadillo.
¡Buenos días! ¿Qué desea?
Un café con leche, por favor.
¿Quiere algo de comer?
Sí, un bocadillo para llevar.
Aquí tiene el café y el bocadillo.
Gracias. ¡Que tenga un buen día!`,
ita:`Prima di prendere il treno, mi sono fermato in un bar.
Ho ordinato un caffè al banco.
Ho chiesto anche un panino da portare via.
Il panino era in un sacchetto di carta.
Ho bevuto il caffè e sono andato in stazione.
Buongiorno! Cosa prende?
Un caffè, per favore.
Desidera altro?
Sì, un panino da portare via.
Ecco il caffè e il panino.
Grazie! Porterò il panino sul treno.`,
deu:`Am Morgen bin ich in eine Bäckerei gegangen.
Ich habe einen Kaffee zum Mitnehmen bestellt.
Dazu habe ich zwei Brötchen bestellt.
Die Verkäuferin hat die Brötchen in eine Tüte gelegt.
Ich habe bezahlt und alles mit ins Büro genommen.
Guten Morgen! Was darf es sein?
Einen Kaffee zum Mitnehmen, bitte.
Darf es sonst noch etwas sein?
Ja, zwei Brötchen, bitte.
Bitte schön. Das macht sechs Euro.
Hier sind die sechs Euro. Danke!`,
ara:`دَخَلْتُ مَقْهًى بَعْدَ العَمَلِ.
طَلَبْتُ قَهْوَةً وَجَلَسْتُ بِالقُرْبِ مِنَ البَابِ.
شَرِبْتُ القَهْوَةَ عَلَى مَهَلٍ.
ثُمَّ طَلَبْتُ الحِسَابَ.
دَفَعْتُ نَقْدًا وَعُدْتُ إِلَى البَيْتِ.
مَسَاءُ الخَيْرِ! مَاذَا تُرِيدُ أَنْ تَطْلُبَ؟
أُرِيدُ قَهْوَةً، مِنْ فَضْلِكَ.
تَفَضَّلْ، هَذِهِ قَهْوَتُكَ.
شُكْرًا. الحِسَابُ، مِنْ فَضْلِكَ.
هَلْ تُرِيدُ الدَّفْعَ نَقْدًا أَمْ بِالبِطَاقَةِ؟
نَقْدًا، مِنْ فَضْلِكَ. تَفَضَّلْ.`,
jpn:`駅へ行く途中でカフェに入りました。
コーヒーを注文しました。
持ち帰りでお願いしました。
店員がふた付きのカップにコーヒーを入れてくれました。
私はコーヒーを持って駅へ行きました。
いらっしゃいませ。ご注文は？
コーヒーをください。
店内でお召し上がりですか、お持ち帰りですか。
持ち帰りでお願いします。
お待たせしました。コーヒーです。
ありがとうございます。駅まで持っていきます。`
};
const readingConnectors={
  pt:['Lemos este exemplo: «{line}»','Olha o exemplo: «{line}»','Comparamos onde os dois termos poderiam aparecer.','A gente pode praticar com essa palavra agora.'],
  eng:['We read this example: “{line}”','Here’s an example: “{line}”','We compared the situations where the two terms might appear.','We can practice that word now.'],
  spa:['Leímos este ejemplo: «{line}»','Mira este ejemplo: «{line}»','Comparamos las situaciones en que podían aparecer los dos términos.','Podemos practicar esa palabra ahora.'],
  ita:['Abbiamo letto questo esempio: «{line}»','Guarda questo esempio: «{line}»','Abbiamo confrontato le situazioni in cui potevano comparire i due termini.','Possiamo esercitarci con questa parola adesso.'],
  deu:['Wir lasen dieses Beispiel: „{line}“','Hier ist ein Beispiel: „{line}“','Wir verglichen die Situationen, in denen die beiden Begriffe vorkommen könnten.','Wir können das Wort jetzt üben.'],
  ara:['قَرَأْنَا هَذَا المِثَالَ: «{line}»','إِلَيْكَ مِثَالًا: «{line}»','قَارَنَّا بَيْنَ المَوَاقِفِ الَّتِي قَدْ يَرِدُ فِيهَا اللَّفْظَانِ.','يُمْكِنُنَا أَنْ نَتَدَرَّبَ عَلَى هَذِهِ الكَلِمَةِ الآنَ.'],
  jpn:['「{line}」という例文を読んだ。','例文は「{line}」だよ。','二つの言葉がどんな場面で出てくるかを比べた。','今その言葉を練習できるよ。']
};
