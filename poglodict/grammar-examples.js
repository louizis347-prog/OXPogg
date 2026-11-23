// The first six rows per language extend the opening topics; the next six extend guided topics.
const extraGrammar=Object.fromEntries(Object.entries({
eng:`Can you show me the way to the station?|Você pode me mostrar o caminho até a estação?|Can we move the meeting to Friday?|Podemos passar a reunião para sexta?
Open your book to page ten.|Abra o livro na página dez.|Don’t leave your bag on the bus.|Não deixe sua bolsa no ônibus.
I’ve tried sushi before.|Já experimentei sushi.|Our team has worked with this client twice.|Nossa equipe já trabalhou duas vezes com esse cliente.
If I lived near the office, I would walk to work.|Se eu morasse perto do escritório, iria a pé para o trabalho.|If we had a bigger kitchen, we could invite everyone over.|Se tivéssemos uma cozinha maior, poderíamos convidar todo mundo.
Much as I admire the chef, I wouldn’t pay that much for dinner.|Por mais que eu admire o chef, eu não pagaria tanto pelo jantar.|Much as I want to help, I can’t take another shift.|Por mais que eu queira ajudar, não consigo pegar outro turno.
Not until we reached the station did we notice the missing bag.|Só percebemos que a bolsa estava faltando quando chegamos à estação.|Not until the results were published did the team see the error.|Só quando publicaram os resultados a equipe percebeu o erro.
She left a message at the office.|Ela deixou um recado no escritório.|It took an hour to reach the station.|Levamos uma hora para chegar à estação.
Did you lock the door?|Você trancou a porta?|Did they send the application yesterday?|Eles enviaram a inscrição ontem?
We were waiting for the train when the lights went out.|Estávamos esperando o trem quando as luzes se apagaram.|I was reading the report when the manager arrived.|Eu estava lendo o relatório quando a gerente chegou.
The keys aren’t here. I must have left them at home.|As chaves não estão aqui. Devo ter deixado em casa.|The floor is wet. It must have rained overnight.|O chão está molhado. Deve ter chovido durante a madrugada.
It was the bread that made the sandwich so good.|Foi o pão que deixou o sanduíche tão gostoso.|It was on Tuesday that the clinic called.|Foi na terça-feira que a clínica ligou.
Had the train arrived on time, we would have caught the ferry.|Se o trem tivesse chegado no horário, teríamos pegado a balsa.|Had I read the instructions, I wouldn’t have made that mistake.|Se eu tivesse lido as instruções, não teria cometido aquele erro.`,
spa:`Quiero una entrada para el museo.|Quero um ingresso para o museu.|Quiero hablar con la profesora.|Quero falar com a professora.
La parada está detrás del hospital.|O ponto fica atrás do hospital.|Las llaves están en la mochila.|As chaves estão na mochila.
Mientras estudiaba, sonó el teléfono.|Enquanto eu estudava, o telefone tocou.|Cuando abrimos la tienda, hacía mucho frío.|Quando abrimos a loja, estava fazendo muito frio.
Me sorprende que el tren salga tan temprano.|Me surpreende que o trem saia tão cedo.|Nos alegra que hayas conseguido el trabajo.|Ficamos felizes que você tenha conseguido o emprego.
Aunque mañana llueva, iremos al mercado.|Mesmo que chova amanhã, vamos ao mercado.|Aunque no te guste el plan, escúchame un momento.|Mesmo que você não goste do plano, me escute um instante.
Si hubiéramos reservado antes, habríamos pagado menos.|Se tivéssemos reservado antes, teríamos pagado menos.|Si me hubieras avisado, te habría esperado.|Se você tivesse me avisado, eu teria esperado.
Los libros nuevos están sobre la mesa.|Os livros novos estão sobre a mesa.|Compramos dos manzanas verdes.|Compramos duas maçãs verdes.
¿El informe? Lo terminé anoche.|O relatório? Terminei ontem à noite.|¿La mochila? La dejé en casa.|A mochila? Deixei em casa.
Esta noche voy a preparar la cena.|Hoje à noite vou preparar o jantar.|Mañana van a llamar al médico.|Amanhã eles vão ligar para o médico.
Cerré la ventana para que el bebé pudiera dormir.|Fechei a janela para que o bebê pudesse dormir.|Deja una nota para que todos sepan la hora.|Deixe um recado para que todos saibam o horário.
Por más que corramos, no alcanzaremos el último tren.|Por mais que a gente corra, não vai alcançar o último trem.|Por más que lo intente, no consigo abrir el archivo.|Por mais que eu tente, não consigo abrir o arquivo.
De haber salido antes, no habríamos perdido el vuelo.|Se tivéssemos saído mais cedo, não teríamos perdido o voo.|De contar con su autorización, iniciaríamos las obras.|Se tivéssemos sua autorização, iniciaríamos as obras.`,
ita:`Vorrei prenotare una camera per domani.|Gostaria de reservar um quarto para amanhã.|Vorrei un biglietto per il museo.|Gostaria de um ingresso para o museu.
Lavoro a Milano, in Italia.|Trabalho em Milão, na Itália.|Domani vado a Torino. In estate vado in Spagna.|Amanhã vou a Turim. No verão, vou para a Espanha.
Mentre leggevo, è suonato il telefono.|Enquanto eu lia, o telefone tocou.|Quando siamo arrivati, il negozio era già chiuso.|Quando chegamos, a loja já estava fechada.
Penso che il treno parta alle otto.|Acho que o trem sai às oito.|Penso che questa soluzione sia più economica.|Acho que esta solução é mais econômica.
Benché piova, usciamo a fare la spesa.|Embora esteja chovendo, vamos sair para fazer compras.|Benché i dati fossero incompleti, abbiamo discusso i risultati.|Embora os dados estivessem incompletos, discutimos os resultados.
Se fossimo partiti prima, avremmo preso il treno.|Se tivéssemos saído mais cedo, teríamos pegado o trem.|Se avessi letto il contratto, avrei fatto più domande.|Se tivesse lido o contrato, teria feito mais perguntas.
Il libro è sul tavolo.|O livro está na mesa.|Lo scaffale è pieno.|A estante está cheia.
Il biglietto? Lo compro online.|A passagem? Compro pela internet.|La chiave? La tengo in tasca.|A chave? Guardo no bolso.
Al mercato? Ci vado ogni sabato.|Ao mercado? Vou lá todo sábado.|In biblioteca? Ci resto fino alle sei.|Na biblioteca? Fico lá até as seis.
Hanno acceso una luce affinché tutti potessero vedere.|Acenderam uma luz para que todos pudessem ver.|Invio il documento affinché possiate leggerlo prima della riunione.|Envio o documento para que vocês possam ler antes da reunião.
La porta, la chiudo io.|A porta, eu fecho.|Quel film, l’abbiamo visto ieri.|Aquele filme, a gente viu ontem.
Volevo sapere se avete un tavolo libero.|Queria saber se vocês têm uma mesa livre.|Volevo chiederle il prezzo della riparazione.|Queria perguntar quanto custa o conserto.`,
deu:`Ich hätte gern ein Stück Kuchen.|Eu gostaria de um pedaço de bolo.|Ich hätte gern eine Fahrkarte nach Bonn.|Eu gostaria de uma passagem para Bonn.
Ich stelle die Tasse auf den Tisch. Sie steht auf dem Tisch.|Coloco a xícara sobre a mesa. Ela está sobre a mesa.|Wir gehen in die Schule. Wir sind schon in der Schule.|Vamos para a escola. Já estamos na escola.
Ich habe gestern für die Prüfung gelernt.|Estudei para a prova ontem.|Sie ist heute früh nach Hause gekommen.|Ela chegou em casa cedo hoje.
Wenn der Laden noch offen wäre, würde ich Brot kaufen.|Se a loja ainda estivesse aberta, eu compraria pão.|Wenn wir ein Auto hätten, würden wir dich abholen.|Se tivéssemos carro, iríamos buscar você.
Der Sprecher erklärte, die Verhandlungen hätten begonnen.|O porta-voz explicou que as negociações haviam começado.|Die Ärztin erklärte, sie sehe keine Anzeichen einer Infektion.|A médica explicou que não via sinais de infecção.
So dringend die Anfrage auch ist, wir müssen sie erst prüfen.|Por mais urgente que seja o pedido, primeiro precisamos analisá-lo.|So gern ich auch mitkäme, ich habe heute keine Zeit.|Por mais que eu queira ir junto, hoje não tenho tempo.
Am Bahnhof wartet meine Schwester.|Minha irmã está esperando na estação.|Morgen beginnt der Kurs.|Amanhã começa o curso.
Ich rufe dich später an.|Eu ligo para você mais tarde.|Machst du bitte das Fenster auf?|Você abre a janela, por favor?
Wir fahren mit dem Bus, weil das Auto kaputt ist.|Vamos de ônibus porque o carro está quebrado.|Sie lernt heute länger, weil sie morgen eine Prüfung hat.|Ela vai estudar mais tempo hoje porque tem prova amanhã.
Die Bestellungen werden am Freitag verschickt.|Os pedidos serão enviados na sexta-feira.|Der Patient wird gerade untersucht.|O paciente está sendo examinado agora.
Der Zug dürfte gleich ankommen.|O trem deve chegar a qualquer momento.|Das Problem dürfte mit einem Neustart behoben sein.|Provavelmente o problema se resolve reiniciando o aparelho.
Die Prognose ist insofern hilfreich, als sie saisonale Effekte berücksichtigt.|A previsão é útil na medida em que considera os efeitos sazonais.|Der Vergleich ist insofern sinnvoll, als beide Gruppen gleich groß sind.|A comparação faz sentido na medida em que os dois grupos têm o mesmo tamanho.`,
ara:`أُرِيدُ تَذْكِرَةً إِلَى عَمَّانَ.|Quero uma passagem para Amã.|أُرِيدُ أَنْ أَتَعَلَّمَ العَرَبِيَّةَ.|Quero aprender árabe.
المَفَاتِيحُ فِي الحَقِيبَةِ.|As chaves estão na bolsa.|المَكْتَبَةُ أَمَامَ المَدْرَسَةِ.|A biblioteca fica em frente à escola.
كَتَبْتُ رِسَالَةً صَبَاحًا.|Escrevi uma mensagem de manhã.|طَبَخْتُ العَشَاءَ لِعَائِلَتِي.|Preparei o jantar para a minha família.
لَوْ كُنْتُ أَعْرِفُ الطَّرِيقَ لَذَهَبْتُ وَحْدِي.|Se eu conhecesse o caminho, iria sozinho.|لَوْ كَانَ المَتْجَرُ مَفْتُوحًا لَاشْتَرَيْتُ الخُبْزَ.|Se a loja estivesse aberta, eu compraria pão.
رَغْمَ أَنَّ الطَّقْسَ بَارِدٌ، خَرَجْنَا لِلمَشْيِ.|Embora estivesse frio, saímos para caminhar.|رَغْمَ أَنَّ البَيَانَاتِ نَاقِصَةٌ، نَشَرَ الفَرِيقُ تَقْرِيرًا أَوَّلِيًّا.|Embora os dados estejam incompletos, a equipe publicou um relatório preliminar.
إِنَّمَا طَلَبْتُ مُهْلَةً قَصِيرَةً.|Só pedi um prazo curto.|إِنَّمَا نَبْحَثُ عَنْ حَلٍّ مُؤَقَّتٍ.|Estamos apenas procurando uma solução temporária.
القَهْوَةُ سَاخِنَةٌ.|O café está quente.|الشَّمْسُ ظَاهِرَةٌ الآنَ.|O sol está aparecendo agora.
هَذَا مِفْتَاحُ البَيْتِ.|Esta é a chave de casa.|أَيْنَ مَحَطَّةُ القِطَارِ؟|Onde fica a estação de trem?
لَنْ أَشْرَبَ القَهْوَةَ مَسَاءً.|Não vou tomar café à noite.|لَنْ يَحْضُرَ المُدِيرُ الاِجْتِمَاعَ.|O gerente não vai comparecer à reunião.
وَصَلَ القِطَارُ الَّذِي كُنَّا نَنْتَظِرُهُ.|Chegou o trem que estávamos esperando.|هَذَا هُوَ الطَّبِيبُ الَّذِي عَالَجَنِي.|Este é o médico que me tratou.
أَغْلَقْتُ البَابَ لِكَيْ يَنَامَ الطِّفْلُ.|Fechei a porta para que a criança dormisse.|خَرَجْنَا مُبَكِّرًا لِكَيْ نَلْحَقَ بِالقِطَارِ.|Saímos cedo para pegar o trem.
يُمْكِنُنَا البَقَاءُ فِي الحَدِيقَةِ مَا دَامَ الطَّقْسُ جَمِيلًا.|Podemos ficar no parque enquanto o tempo estiver bom.|لَنْ نَنْشُرَ النَّتَائِجَ مَا دَامَ التَّحْقِيقُ مُسْتَمِرًّا.|Não vamos publicar os resultados enquanto a investigação estiver em andamento.`,
jpn:`切符を一枚ください。|Uma passagem, por favor.|紙を二枚ください。|Duas folhas de papel, por favor.
この書類に名前を書いてください。|Escreva seu nome neste documento, por favor.|窓を開けてください。|Abra a janela, por favor.
富士山に登ったことがあります。|Já subi o monte Fuji.|その料理は食べたことがありません。|Nunca comi esse prato.
早く家を出たのに、電車に間に合わなかった。|Mesmo saindo cedo de casa, perdi o trem.|薬を飲んだのに、まだ頭が痛い。|Embora eu tenha tomado o remédio, ainda estou com dor de cabeça.
駅から近いとはいえ、歩いて十五分かかる。|Embora fique perto da estação, são quinze minutos a pé.|経験が少ないとはいえ、彼女の提案は検討に値する。|Apesar de ela ter pouca experiência, sua proposta merece ser analisada.
こちらこそありがとうございます。|Eu é que agradeço.|今度こそ約束を守ります。|Desta vez eu vou cumprir a promessa.
今日は休みです。|Hoje é dia de folga.|この店は八時に閉まります。|Esta loja fecha às oito.
この店より駅前の店のほうが安いです。|A loja em frente à estação é mais barata que esta.|冬より春のほうが旅行しやすいです。|É mais fácil viajar na primavera do que no inverno.
今年は車を買わないことにしました。|Decidi não comprar carro este ano.|来月から日本語を勉強することにしました。|Decidi estudar japonês a partir do mês que vem.
時間がないわけではない。|Não é que eu não tenha tempo.|すべての点に賛成しているわけではない。|Não quer dizer que eu concorde com tudo.
手紙を捨てると見せかけて、引き出しにしまった。|Fingiu jogar a carta fora e a guardou na gaveta.|値下げしたと見せかけて、実は量を減らしていた。|Parecia que tinham baixado o preço, mas na verdade reduziram a quantidade.
年齢のいかんにかかわらず、応募できます。|É possível se candidatar independentemente da idade.|結果のいかんにかかわらず、調査の経過を公開します。|Publicaremos o andamento da investigação independentemente do resultado.`
}).map(([language,rows])=>[language,rows.split('\n').map(line=>line.trim().split('|'))]));
const grammarNotes={
eng:[
  'O verbo depois do sujeito fica na forma base. Can I pede permissão, enquanto Can you geralmente introduz um pedido.',
  'O sujeito you costuma ficar implícito. Para uma instrução negativa, use don’t antes do verbo.',
  'Before, ever e twice podem falar de experiências sem localizar cada uma numa data. Para contar algo ocorrido yesterday, prefira o passado simples.',
  'Nesse padrão, could pode substituir would para indicar uma possibilidade, como a de convidar mais gente.',
  'Much as introduz aquilo que o falante admite. A segunda oração traz a decisão ou a limitação que ainda vale.',
  'A inversão ocorre na oração principal. Em did we notice, notice volta à forma base.',
  'Ouça a palavra seguinte: hour começa com som vocálico, por isso se diz an hour.',
  'Did já marca o passado. Compare Did you lock…? com You locked… na afirmativa.',
  'A forma contínua descreve o que já estava em andamento quando o outro fato aconteceu.',
  'Use essa construção para inferir algo a partir de uma pista. Não é uma obrigação passada.',
  'O elemento entre it was e that recebe o destaque. Pode ser o motivo, a pessoa ou o momento.',
  'A estrutura had + sujeito + particípio equivale a if + sujeito + had + particípio. A oração de resultado conserva would have.'
],
spa:[
  'Depois de quiero, use um nome para pedir algo ou um infinitivo para indicar o que você quer fazer.',
  'Estar concorda com o sujeito: está para la parada e están para las llaves.',
  'O imperfeito apresenta uma ação em andamento ou uma condição de fundo. O indefinido avança a sequência dos acontecimentos.',
  'Estés apresenta uma situação atual. Hayas conseguido indica algo já realizado que provoca a reação.',
  'Com indicativo, aunque pode apresentar um fato assumido como certo. Com subjuntivo, o foco pode ficar no resultado apesar da condição.',
  'A condição vai depois de si: hubiéramos reservado primeiro, habríamos pagado como consequência.',
  'Observe o conjunto completo: las ventanas grandes e los libros nuevos. Adjetivos como grandes variam no número, sem trocar de gênero.',
  'Lo e la retomam o objeto mencionado e aparecem antes de terminé e dejé nesses exemplos.',
  'Quem muda é o verbo ir: voy para eu e van para eles ou elas. O verbo seguinte continua no infinitivo.',
  'Compare para que todos sepan, com dois sujeitos, e para saber, que pode servir quando o sujeito continua o mesmo.',
  'A concessão apresenta o esforço. A oração principal mostra por que ele não muda o resultado.',
  'De haber + particípio remete a uma condição anterior. De contar + infinitivo pode introduzir uma condição ainda possível.'
],
ita:[
  'Depois de vorrei, use um nome para pedir algo ou um infinitivo para dizer o que deseja fazer.',
  'A preposição vale tanto para localização quanto para destino nestes casos: a Milano, a Torino e in Spagna.',
  'O imperfetto descreve a situação. O passato prossimo destaca o fato que aconteceu naquele cenário.',
  'Sia vem de essere. Parta vem de partire. As duas formas são do congiuntivo presente.',
  'Benché admite uma dificuldade antes da informação principal. Piova aponta para o presente e fossero para uma situação passada.',
  'Com partire, a condição usa essere. Com leggere, usa avere. O resultado continua no condizionale passato.',
  'Em s seguido de consoante, use lo, como em lo scaffale. Antes de vogal, muitas vezes você verá l’.',
  'Lo retoma il biglietto e la retoma la chiave. Com um verbo conjugado, o pronome vem antes.',
  'Ci pode significar lá mesmo com verbos diferentes, como andare, tornare e restare.',
  'O sujeito da ação principal e o da finalidade podem ser diferentes. O tempo do congiuntivo acompanha a relação temporal.',
  'A pausa depois do objeto destacado é comum na fala. O pronome retoma esse objeto dentro da oração.',
  'Volevo pode suavizar uma solicitação que está sendo feita agora, especialmente no atendimento.'
],
deu:[
  'Observe o artigo do objeto: einen Tee, ein Stück e eine Fahrkarte. A expressão inteira é uma forma gentil de fazer pedidos.',
  'Com essas preposições, a pergunta wohin? investiga o destino e wo? investiga a posição.',
  'Muitos verbos usam haben. Alguns verbos de deslocamento, como kommen, usam sein.',
  'Wäre é uma forma de sein. Hätte é uma forma de haben. Depois de würde, o outro verbo vai ao fim no infinitivo.',
  'Sehe sinaliza discurso indireto. Quando o Konjunktiv I coincide com o indicativo no plural, o Konjunktiv II pode diferenciar as formas, como hätten.',
  'Auch pode aparecer na oração concessiva. A afirmação principal apresenta a ressalva que continua válida.',
  'A primeira posição pode ter várias palavras, como am Bahnhof. O verbo conjugado ocupa a segunda posição sintática.',
  'Em rufe … an e fährt … ab, o prefixo fecha a oração principal. Numa pergunta simples, o verbo conjugado pode abrir a frase.',
  'A vírgula separa a subordinada. Depois de weil, ist e hat fecham as respectivas orações.',
  'A ação é o foco. O autor dela pode ficar implícito, como em wird untersucht.',
  'Dürfte costuma indicar probabilidade. A construção com um particípio pode sugerir o resultado provável de uma ação.',
  'A oração com als explica em que aspecto a afirmação se sustenta.'
],
ara:[
  'Depois de أريد, você pode pôr um substantivo ou usar أنْ seguido de um verbo para indicar o que deseja fazer.',
  'Uma expressão como فِي الحَقِيبَةِ pode funcionar como predicado e dizer onde algo está.',
  'Compare كَتَبْتُ, escrevi, com كَتَبَ, ele escreveu. A vogal do sufixo indica a primeira pessoa.',
  'Identifique لو na condição e o لَ no início da resposta afirmativa. A tradução pode usar o futuro do pretérito.',
  'O trecho com رغم أنَّ apresenta um fato ou obstáculo. A oração seguinte mostra o que ocorreu apesar dele.',
  'A restrição depende do foco da frase. Em português, experimente apenas ou só.',
  'Antes de uma letra solar como ش, o som do ل do artigo se assimila à consoante seguinte.',
  'Na construção de posse, o primeiro substantivo fica sem o artigo ال. O segundo pode ter artigo, como em مِفْتَاحُ البَيْتِ.',
  'Compare a negação com لن no futuro e com لم para negar um fato passado.',
  'Na relativa, um pronome final pode retomar o antecedente, como em نَنْتَظِرُهُ. Se o antecedente é o sujeito da relativa, esse pronome separado não é necessário.',
  'A finalidade pode envolver o mesmo sujeito ou outro, como a criança no primeiro exemplo.',
  'A construção também pode aparecer com tradução equivalente a enquanto durar a condição.'
],
jpn:[
  'A partícula を marca o objeto que você pede. 一枚 e 二枚 contam objetos planos, como folhas e passagens.',
  'A forma て muda conforme o verbo. 書く vira 書いて e 開ける vira 開けて.',
  'Use ありません para dizer que ainda não teve a experiência. Uma data específica normalmente pede outra construção.',
  'のに conecta a expectativa àquilo que realmente aconteceu. Pode transmitir frustração ou surpresa.',
  'O que vem depois de とはいえ limita a conclusão que o leitor poderia tirar da primeira ideia.',
  '今度こそ destaca desta vez. こちらこそ devolve o agradecimento com ênfase.',
  'O tema não precisa ser a pessoa que faz a ação. Pode ser um dia, como 今日, ou um local, como この店.',
  'より marca a referência da comparação. のほうが indica o lado ao qual se atribui a característica.',
  'Com ことにしました, a decisão já foi tomada. O verbo anterior também pode aparecer na forma negativa.',
  'A estrutura permite corrigir uma interpretação ampla ou absoluta, como a ideia de concordar com tudo.',
  'A ação aparente vem antes de と見せかけて. A continuação revela o que aconteceu de fato.',
  'Use substantivo + のいかんにかかわらず para nomear o fator que não altera a regra ou a decisão.'
]};
