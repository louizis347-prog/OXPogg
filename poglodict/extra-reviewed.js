const editorialThird=Object.fromEntries(Object.entries({
eng:`Tom|Tom is meeting us at the café.|Tom vai se encontrar com a gente no café.
've|We’ve seen that movie twice.|Já vimos esse filme duas vezes.
is|My phone is on the table.|Meu celular está sobre a mesa.
they|They’re waiting outside.|Eles estão esperando do lado de fora.
out|Could you let the dog out?|Você pode deixar o cachorro sair?
up|She looked up when the bell rang.|Ela olhou para cima quando o sino tocou.
withe|The basket maker bound the handle with a withe.|O cesteiro prendeu a alça com uma vara flexível.
set store by|She sets great store by honest feedback.|Ela valoriza muito opiniões sinceras.
was|The coffee was cold.|O café estava frio.
for|I bought these flowers for my grandmother.|Comprei estas flores para a minha avó.
of|The door of the classroom was open.|A porta da sala de aula estava aberta.
he|He left his keys in the car.|Ele deixou as chaves no carro.
will|I will bring your book back tomorrow.|Vou devolver seu livro amanhã.
can|Can I borrow your bike?|Posso pegar sua bicicleta emprestada?
shall|Shall we meet at noon?|Vamos nos encontrar ao meio-dia?
have|Do you have a map?|Você tem um mapa?
be|Be careful on the stairs.|Tome cuidado na escada.`,
deu:`haten|Man muss nicht gleich alle haten, die anderer Meinung sind.|Não precisa sair atacando todo mundo que pensa diferente.
einen|Sie liest einen langen Brief.|Ela lê uma carta comprida.
können|Die Kinder können schon schwimmen.|As crianças já sabem nadar.
meinen|Mein Bruder meint, dass der Weg zu lang ist.|Meu irmão acha que o caminho é longo demais.
fahren|Morgen fahre ich mit dem Zug nach Köln.|Amanhã vou de trem para Colônia.
wassern|Das Flugboot wasserte in einer geschützten Bucht.|O hidroavião pousou numa baía abrigada.
zu|Kommst du heute zu mir?|Você vem à minha casa hoje?`,
spa:`parar|El conductor paró antes del puente.|O motorista parou antes da ponte.
con|La sopa va con pan.|A sopa vem com pão.
las|Las manzanas están maduras.|As maçãs estão maduras.
haber|Habrá una reunión el lunes.|Vai ter uma reunião na segunda.
se|Ravi se peina antes de salir.|Ravi penteia o cabelo antes de sair.`,
ita:`e|La cucina è grande e luminosa.|A cozinha é grande e iluminada.
era|Il treno era in ritardo.|O trem estava atrasado.
fare|Lia deve fare una telefonata.|Lia precisa fazer uma ligação.
lei|Lei sa come risolvere il problema.|Ela sabe como resolver o problema.
ha|Lia ha un biglietto per il concerto.|Lia tem um ingresso para o show.
mi|Mi puoi aspettare qui?|Você pode me esperar aqui?`,
ara:`سامي|سَامِي يَعْمَلُ فِي مَكْتَبَةٍ.|Sami trabalha numa biblioteca.
ليلى|تَقْرَأُ لَيْلَى كِتَابًا جَدِيدًا.|Laila está lendo um livro novo.
عن|هَذَا الفِيلْمُ عَنِ السَّفَرِ.|Este filme é sobre viagens.
أين|أَيْنَ سَتَنْزِلُ؟|Onde você vai descer?
كان|كَانَ البَابُ مَفْتُوحًا.|A porta estava aberta.`,
jpn:`家|今日は家で仕事をします。|Hoje vou trabalhar em casa.
僕|僕の名前はリクです。|Meu nome é Riku.
仕事|新しい仕事を探しています。|Estou procurando um novo trabalho.
時|時間がない時は電話で話しましょう。|Quando estiver sem tempo, vamos conversar por telefone.
今|今、何をしていますか。|O que você está fazendo agora?
思う|明日は雨だと思います。|Acho que amanhã vai chover.
気|今日は本を読む気がしない。|Hoje não estou com vontade de ler.
話|その話は初めて聞きました。|Foi a primeira vez que ouvi essa história.
前|ドアの前に荷物を置かないでください。|Não deixe suas coisas na frente da porta, por favor.
日|あと三日で旅行です。|Faltam três dias para a viagem.
車|駅の前に車が止まっています。|Há um carro parado em frente à estação.`
}).map(([language,lines])=>[language,new Map(lines.split('\n').map(line=>{
  const [word,text,translation]=line.split('|');return [word,{text,translation}];
}))]));
