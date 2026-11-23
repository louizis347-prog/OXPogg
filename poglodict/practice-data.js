const coreSeconds=Object.fromEntries(Object.entries({
eng:`Do you drink coffee every morning?|Você toma café todas as manhãs?|Is this sandwich for here?|Este sanduíche é para comer aqui?
The bakery is just around the corner.|A padaria fica logo na esquina.|How do I get to the train station?|Como chego à estação de trem?
Don’t put off your appointment again.|Não adie seu compromisso de novo.|Guests can check in online.|Os hóspedes podem fazer o check-in pela internet.
It’s no big deal if you forget.|Tudo bem se você esquecer.|I’m down for a walk this afternoon.|Eu topo uma caminhada hoje à tarde.
The choice comes down to price.|A escolha se resume ao preço.|On balance, I would keep the old schedule.|Considerando tudo, eu manteria o horário antigo.
This is a far cry from her first draft.|Isto está bem longe da primeira versão dela.|For all its flaws, the book is worth reading.|Apesar de todos os seus defeitos, vale a pena ler o livro.`,
spa:`El café está demasiado caliente.|O café está quente demais.|¿Puedo pedir dos bocadillos para llevar?|Posso pedir dois sanduíches para viagem?
La librería está a la vuelta de la esquina.|A livraria fica logo na esquina.|¿Queda lejos el museo?|O museu fica longe?
Tengo que hacer las maletas esta noche.|Preciso fazer as malas hoje à noite.|El billete de ida y vuelta cuesta menos.|A passagem de ida e volta custa menos.
Tu chaqueta es muy guay.|Sua jaqueta é muito legal.|¡Qué chévere que hayan venido!|Que legal que vocês vieram!
La periodista puso en tela de juicio la versión oficial.|A jornalista pôs em dúvida a versão oficial.|A grandes rasgos, el plan consiste en ampliar el servicio.|Em linhas gerais, o plano consiste em ampliar o serviço.
No fue fácil, ni mucho menos.|Longe de ter sido fácil.|Huelga decir que nadie está obligado a participar.|Nem é preciso dizer que ninguém é obrigado a participar.`,
ita:`Il caffè è già pronto.|O café já está pronto.|Una pizza da portare via, per favore.|Uma pizza para viagem, por favor.
Il bar è proprio dietro l’angolo.|O bar fica bem ali na esquina.|Andiamo a piedi fino alla stazione.|Vamos a pé até a estação.
Abbiamo fatto le valigie ieri sera.|Fizemos as malas ontem à noite.|Il viaggio di andata e ritorno dura tre ore.|A viagem de ida e volta leva três horas.
Boh, non ne so niente.|Sei lá, eu não sei nada disso.|Dai, proviamo un’altra volta!|Vamos lá, vamos tentar mais uma vez!
La nuova scoperta mette in discussione l’ipotesi iniziale.|A nova descoberta põe em questão a hipótese inicial.|In linea di massima il progetto è fattibile.|Em princípio, o projeto é viável.
A conti fatti, abbiamo speso meno del previsto.|No fim das contas, gastamos menos do que o previsto.|Per quanto mi consta, la riunione è confermata.|Até onde sei, a reunião está confirmada.`,
deu:`Der Kaffee ist noch heiß.|O café ainda está quente.|Zwei Brötchen zum Mitnehmen, bitte.|Dois pãezinhos para viagem, por favor.
Der Bäcker ist gleich um die Ecke.|A padaria fica logo na esquina.|Wie lange dauert es zu Fuß?|Quanto tempo leva a pé?
Wir müssen noch die Koffer packen.|Ainda precisamos fazer as malas.|Steigen Sie bitte in Bonn um.|Faça a baldeação em Bonn, por favor.
Die Aussicht war echt krass.|A vista era realmente impressionante.|Ich habe heute keinen Bock auf Sport.|Hoje não estou a fim de fazer exercício.
Die Studie stellt diese Annahme in Frage.|O estudo põe essa suposição em dúvida.|Unter dem Strich haben wir Zeit gespart.|No fim das contas, economizamos tempo.
Sie hat keine Zeit für einen Kaffee, geschweige denn für ein Essen.|Ela não tem tempo para um café, muito menos para uma refeição.|Ich komme morgen, es sei denn, ich muss arbeiten.|Vou amanhã, a menos que tenha de trabalhar.`,
ara:`القَهْوَةُ سَاخِنَةٌ.|O café está quente.|الحِسَابُ، مِنْ فَضْلِكَ. سَأَدْفَعُ بِالبِطَاقَةِ.|A conta, por favor. Vou pagar com cartão.
المَتْحَفُ بِالقُرْبِ مِنَ الحَدِيقَةِ.|O museu fica perto do parque.|يُمْكِنُنَا الذَّهَابُ عَلَى الأَقْدَامِ.|Podemos ir a pé.
حَجَزْنَا تَذْكِرَتَيْنِ إِلَى القَاهِرَةِ.|Reservamos duas passagens para o Cairo.|هَذِهِ تَذْكِرَةٌ ذَهَابًا وَإِيَابًا.|Esta é uma passagem de ida e volta.
ماشي، هكلّمك بعدين.|Beleza, te ligo depois.|الأغنية دي جامدة أوي!|Essa música é muito boa!
وَضَعَتِ الدِّرَاسَةُ هَذَا الاِفْتِرَاضَ مَوْضِعَ الشَّكِّ.|O estudo pôs essa hipótese em dúvida.|مِنْ حَيْثُ المَبْدَأِ، هَذَا الحَلُّ مُمْكِنٌ.|Em princípio, essa solução é possível.
لَا أَمْلِكُ ثَمَنَ التَّذْكِرَةِ، نَاهِيكَ عَنْ تَكَالِيفِ الإِقَامَةِ.|Não tenho dinheiro para a passagem, sem falar nos custos da hospedagem.|وَخَيْرُ دَلِيلٍ عَلَى ذَلِكَ زِيَادَةُ المَبِيعَاتِ.|E a melhor prova disso é o aumento das vendas.`,
jpn:`毎朝コーヒーを飲みます。|Tomo café todas as manhãs.|このサンドイッチは持ち帰りでお願いします。|Este sanduíche é para viagem, por favor.
角を曲がると、コンビニがあります。|Ao virar a esquina, há uma loja de conveniência.|学校まで歩いて行きます。|Vou a pé até a escola.
レストランを予約しました。|Reservei um restaurante.|ここで地下鉄に乗り換えてください。|Faça a baldeação para o metrô aqui, por favor.
この景色、やばいくらいきれい。|Esta paisagem é absurdamente linda.|マジでそう思う？|Você acha isso mesmo?
記者は発表の内容に疑問を呈した。|O jornalista questionou o conteúdo do anúncio.|この方法が最善だとは一概には言えない。|Não dá para dizer de forma geral que este é o melhor método.
健康が大切なのは言うまでもない。|Nem é preciso dizer que a saúde é importante.|彼女はあえてその話題に触れなかった。|Ela deliberadamente evitou tocar nesse assunto.`
}).map(([k,v])=>[k,v.split('\n').map(line=>line.split('|'))]));
const grammarPractice=Object.fromEntries(Object.entries({
eng:`Artigo indefinido|Use a antes de som consonantal e an antes de som vocálico.|She has an umbrella.|Ela tem um guarda-chuva.
Passado simples em perguntas|Use did e deixe o verbo principal na forma base.|Did you see the sign?|Você viu a placa?
Contrastar tempos passados|Use was ou were com -ing para a ação em andamento e o passado simples para o evento pontual.|I was cooking when she called.|Eu estava cozinhando quando ela ligou.
Dedução sobre o passado|Use must have com particípio para expressar uma conclusão forte sobre o passado.|He must have missed the train.|Ele deve ter perdido o trem.
Frases clivadas|Use it was … that para destacar um elemento no enunciado.|It was her tone that surprised me.|Foi o tom dela que me surpreendeu.
Condicionais com inversão|Use had antes do sujeito para uma condição passada em registro formal.|Had we known, we would have waited.|Se soubéssemos, teríamos esperado.`,
spa:`Gênero e número|Faça artigo e adjetivo concordarem com o substantivo.|Las ventanas grandes están abiertas.|As janelas grandes estão abertas.
Objeto direto com lo e la|Coloque lo ou la antes do verbo conjugado para retomar um objeto conhecido.|La compré ayer.|Comprei-a ontem.
Futuro com ir a|Use ir conjugado, a e o infinitivo para anunciar um plano.|Vamos a visitar el museo.|Vamos visitar o museu.
Regência do subjuntivo|Use para que com subjuntivo quando a finalidade envolve outro sujeito.|Te escribo para que sepas la verdad.|Escrevo para que você saiba a verdade.
Concessão com por más que|Use por más que para indicar que uma ação ou esforço não muda o resultado.|Por más que insista, no cambiaré de opinión.|Por mais que insista, não vou mudar de opinião.
Condição implícita com de|Em registro formal, de seguido de infinitivo pode introduzir uma condição.|De haberlo sabido, habría intervenido.|Se soubesse, teria intervindo.`,
ita:`Artigos no singular|Use il antes da maioria das consoantes e lo antes de s mais consoante.|Lo zaino è nuovo.|A mochila é nova.
Pronomes de objeto direto|Coloque lo ou la antes de um verbo conjugado para retomar um objeto conhecido.|La vedo ogni giorno.|Eu a vejo todos os dias.
Combinar ci com verbos de lugar|Use ci para retomar um lugar já mencionado.|A Roma? Ci torno domani.|A Roma? Volto lá amanhã.
Finalidade com affinché|Use affinché seguido de congiuntivo para indicar o objetivo de uma ação.|Spiego tutto affinché tu possa decidere.|Explico tudo para que você possa decidir.
Deslocar o tema para a esquerda|Retome com um pronome o objeto colocado em destaque antes da oração.|Quel libro, l’ho letto ieri.|Aquele livro, eu o li ontem.
Valores do imperfetto|No diálogo, o imperfetto pode suavizar um pedido presente.|Volevo chiederle un favore.|Eu queria lhe pedir um favor.`,
deu:`Posição do verbo principal|Em uma oração declarativa, coloque o verbo conjugado na segunda posição.|Heute lerne ich Deutsch.|Hoje eu estudo alemão.
Verbos separáveis|Mande o prefixo separável para o fim de uma oração principal simples.|Der Zug fährt um acht ab.|O trem parte às oito.
Subordinadas com weil|Em alemão padrão, leve o verbo conjugado ao fim da oração subordinada introduzida por weil.|Ich bleibe zu Hause, weil es regnet.|Fico em casa porque está chovendo.
Passiva com werden|Combine werden com o particípio para descrever uma ação sofrida pelo sujeito.|Die Brücke wird repariert.|A ponte está sendo consertada.
Modalidade com dürfte|Use dürfte para expressar uma suposição cautelosa, dependendo do contexto.|Das dürfte stimmen.|Isso provavelmente é verdade.
Integração de ressalvas|Use insofern para delimitar o alcance daquilo que se afirma.|Die Kritik ist insofern berechtigt, als sie auf Daten beruht.|A crítica é válida na medida em que se baseia em dados.`,
ara:`Artigo definido|Acrescente ال ao substantivo definido. Em الكتاب, lê-se al-kitāb.|الكِتَابُ هُنَا.|O livro está aqui.
Posse com إضافة|Justaponha o elemento possuído e o possuidor na construção iḍāfa.|هَذَا كِتَابُ الطَّالِبِ.|Este é o livro do aluno.
Negar o futuro|Use لَنْ antes de um verbo no imperfeito no modo subjuntivo.|لَنْ أَسَافِرَ غَدًا.|Não vou viajar amanhã.
Relativa com الذي|Use الذي para introduzir uma oração relativa referente a um antecedente masculino singular definido.|هَذَا هُوَ الكِتَابُ الَّذِي قَرَأْتُهُ.|Este é o livro que li.
Finalidade com لكي|Use لكي seguido de um verbo no subjuntivo para indicar finalidade.|دَرَسْتُ لِكَيْ أَنْجَحَ.|Estudei para passar.
Delimitar escopo com ما دام|Use ما دام para indicar a condição que continua valendo por certo tempo.|سَنَنْتَظِرُ مَا دَامَ الأَمَلُ قَائِمًا.|Vamos esperar enquanto houver esperança.`,
jpn:`Tema com は|Use は, pronunciado wa nessa posição, para marcar o tema da frase.|私は学生です。|Sou estudante.
Fazer comparações|Use より para marcar o ponto de referência e のほうが para destacar a alternativa comparada.|電車よりバスのほうが安いです。|O ônibus é mais barato que o trem.
Expressar uma decisão|Use a forma de dicionário ou negativa do verbo com ことにする para indicar uma decisão pessoal.|毎日歩くことにしました。|Decidi caminhar todos os dias.
Corrigir uma suposição|Use わけではない para rejeitar uma conclusão que poderia ser inferida.|嫌いなわけではない。|Não quer dizer que eu não goste.
Contrastar aparência e realidade|Use と見せかけて para indicar que algo aparenta uma coisa enquanto outra acontece.|帰ると見せかけて、その場に残った。|Fingiu que ia embora e ficou ali.
Expressar ausência de relação|Use いかんにかかわらず em registro formal para indicar que um resultado independe de certo fator.|理由のいかんにかかわらず、返金はできません。|Independentemente do motivo, não é possível fazer o reembolso.`
}).map(([k,v])=>[k,v.split('\n').map(line=>line.split('|'))]));
const variedPractice=[
  [
    ['Reconhecer o assunto','Leia as duas frases e use as palavras que conhece para identificar o assunto.'],
    ['Apresentar uma informação','Use uma das frases como modelo para dizer algo simples sobre você ou seu dia.'],
    ['Fazer uma pergunta breve','Transforme a ideia de uma das frases em uma pergunta que caiba numa conversa cotidiana.'],
    ['Reconhecer palavras-chave','Escolha duas palavras que bastem para lembrar o sentido de cada frase.'],
    ['Responder em uma frase','Imagine alguém dizendo a primeira frase. Dê uma resposta curta coerente com a situação.']
  ],
  [
    ['Trocar pessoa ou lugar','Reescreva uma frase com outra pessoa ou outro lugar. Ajuste as palavras que precisarem concordar.'],
    ['Negar uma informação','Passe a primeira ideia para a forma negativa. Compare a ordem das palavras antes e depois.'],
    ['Situar a ação no tempo','Acrescente uma referência a ontem, hoje ou amanhã. Adapte a frase quando for preciso.'],
    ['Dar um detalhe','Acrescente um complemento curto que esclareça onde, quando ou como a ação ocorre.'],
    ['Pedir esclarecimento','Faça uma pergunta simples sobre a frase. Use o contexto para imaginar uma resposta.']
  ],
  [
    ['Contar em sequência','Use uma das frases entre dois acontecimentos e conecte as ideias em três frases.'],
    ['Explicar uma razão','Acrescente um motivo plausível ao que acontece em um dos exemplos.'],
    ['Combinar informações','Una as ideias dos dois exemplos com um conector adequado. Se forem situações diferentes, construa uma transição.'],
    ['Relatar uma experiência','Conte uma situação parecida em primeira pessoa. Diga como ela começou e terminou.'],
    ['Confirmar o que entendeu','Imagine que você ouviu a primeira frase numa conversa. Parafraseie e peça confirmação.']
  ],
  [
    ['Adaptar ao interlocutor','Reformule uma das frases como se falasse primeiro com um amigo e depois em uma situação profissional.'],
    ['Expressar ressalva','Acrescente uma ressalva que qualifique o que a frase afirma. Preserve a ideia principal.'],
    ['Comparar reformulações','Use outra construção para transmitir a mesma informação. Compare o foco das versões.'],
    ['Negociar uma solução','Imagine um problema relacionado ao exemplo. Use o termo para propor uma solução e indicar uma condição.'],
    ['Defender uma escolha','Use a situação como ponto de partida para justificar uma posição. Inclua um motivo e uma objeção.']
  ],
  [
    ['Precisar o sentido','Identifique a acepção usada em cada frase. Substitua o termo por um equivalente adequado ao contexto.'],
    ['Condensar sem perder informação','Reduza uma frase ao essencial. Explique que detalhe foi possível omitir e por quê.'],
    ['Explicitar o que ficou implícito','Identifique uma inferência que depende do contexto. Reformule a frase para torná-la explícita.'],
    ['Reorganizar a informação','Mude o início da frase para destacar outro elemento. Observe como a ênfase se altera.'],
    ['Mudar o gênero textual','Reescreva uma frase para um e-mail formal ou para um texto informativo e justifique duas escolhas.']
  ],
  [
    ['Ajustar a força da afirmação','Produza uma versão mais categórica e outra mais cautelosa. Explique o efeito de cada mudança.'],
    ['Controlar subentendidos','Reescreva a frase de modo que sugira uma conclusão sem afirmá-la diretamente. Identifique a pista deixada ao leitor.'],
    ['Construir uma resposta diplomática','Formule uma discordância cuidadosa em relação a uma das frases. Preserve a nuance que mereça ser reconhecida.'],
    ['Interpretar a escolha lexical','Compare o termo com uma alternativa próxima. Analise o que muda no tom, nas implicações ou na adequação ao público.'],
    ['Redistribuir a ênfase','Crie duas versões que privilegiem perspectivas diferentes e explique o papel da sintaxe em cada leitura.']
  ]
];
const starterSeconds={
eng:`The room is quiet.|O quarto está silencioso.
The bus is late.|O ônibus está atrasado.
She walks to school.|Ela vai a pé para a escola.
We need one more chair.|Precisamos de mais uma cadeira.
What was your first job?|Qual foi seu primeiro emprego?
I speak Portuguese.|Eu falo português.
We saw a bird.|Vimos um pássaro.
Do you live here?|Você mora aqui?
This bag is small and light.|Esta bolsa é pequena e leve.
They have a dog.|Eles têm um cachorro.
We go there every Friday.|Vamos lá toda sexta-feira.
Would you like some coffee?|Você quer um pouco de café?`,
spa:`Mi hermana es médica.|Minha irmã é médica.
Salgo de casa a las ocho.|Saio de casa às oito.
La biblioteca cierra a las seis.|A biblioteca fecha às seis.
Me dijo que tenía frío.|Ela me disse que estava com frio.
No sé dónde está.|Não sei onde fica.
Llegamos a Madrid por la mañana.|Chegamos a Madri de manhã.
Vivimos en una calle tranquila.|Moramos numa rua tranquila.
Hoy estoy cansada.|Hoje estou cansada.
Hay dos sillas en la cocina.|Tem duas cadeiras na cozinha.
Mi hermano se afeita cada mañana.|Meu irmão se barbeia toda manhã.
¿Tienes un mapa?|Você tem um mapa?
¿Vas al mercado?|Você vai ao mercado?`,
ita:`Non capisco questa parola.|Não entendo esta palavra.
Abito a Firenze.|Moro em Florença.
Siamo pronti.|Estamos prontos.
La borsa è di Marta.|A bolsa é da Marta.
Penso che sia tardi.|Acho que é tarde.
Il telefono è in borsa.|O telefone está na bolsa.
La porta è chiusa.|A porta está fechada.
Hai tempo domani?|Você tem tempo amanhã?
Questi fiori sono per Anna.|Estas flores são para a Anna.
Io preferisco il tè.|Eu prefiro chá.
Le chiavi sono sul tavolo.|As chaves estão sobre a mesa.
Mi aiuti, per favore?|Você me ajuda, por favor?`,
deu:`Wir sind bereit.|Estamos prontos.
Ich wohne in Berlin.|Eu moro em Berlim.
Hast du einen Stift?|Você tem uma caneta?
Ich kaufe einen Apfel.|Vou comprar uma maçã.
Der Laden ist heute nicht offen.|A loja está fechada hoje.
Sie kommen aus Brasilien.|Eles vêm do Brasil.
Das Kind spielt im Garten.|A criança brinca no jardim.
Der Kaffee ist heiß.|O café está quente.
Sie wird Ärztin.|Ela vai se tornar médica.
Ich muss zum Arzt.|Preciso ir ao médico.
Wo wohnst du?|Onde você mora?
Wann gehst du nach Hause?|Quando você vai para casa?`,
ara:`المِفْتَاحُ فِي الحَقِيبَةِ.|A chave está na bolsa.
عُدْتُ مِنَ العَمَلِ.|Voltei do trabalho.
أُحِبُّ أَنْ أَقْرَأَ.|Gosto de ler.
لَا أَشْرَبُ القَهْوَةَ لَيْلًا.|Não tomo café à noite.
كَانَ المَتْحَفُ مُغْلَقًا.|O museu estava fechado.
هَلْ تَتَكَلَّمُ العَرَبِيَّةَ؟|Você fala árabe?
لَمْ أَفْهَمْ مَا قُلْتَ.|Não entendi o que você disse.
الهَاتِفُ عَلَى المَكْتَبِ.|O telefone está sobre a mesa.
سَافَرْنَا إِلَى مِصْرَ.|Viajamos para o Egito.
هَذَا هُوَ البَابُ.|Esta é a porta.
مَا هَذَا؟|O que é isto?
أَنَا مِنْ سَاوْ بَاوْلُو.|Sou de São Paulo.`,
jpn:`彼は毎朝走ります。|Ele corre todas as manhãs.
私はコーヒーが好きです。|Gosto de café.
彼女は毎日ここに来ます。|Ela vem aqui todos os dias.
公園にはたくさんの人がいます。|Há muitas pessoas no parque.
何を読みますか。|O que você vai ler?
君はどう思う？|O que você acha?
その話は本当ですか。|Essa história é verdadeira?
駅まで歩いて行きます。|Vou a pé até a estação.
夜に星を見ます。|À noite, observo as estrelas.
昼ご飯に何を食べますか。|O que você vai comer no almoço?
水を飲みます。|Vou beber água.
図書館で本を借りました。|Peguei um livro emprestado na biblioteca.`
};
const authoredSeconds=Object.fromEntries(Object.entries(starterSeconds).map(([language,lines])=>[
  language,new Map(starterEntries[language].split('\n').map((line,i)=>{
    const [text,translation]=lines.split('\n')[i].split('|');
    return [line.split('|')[0],{text,translation}];
  }))
]));
