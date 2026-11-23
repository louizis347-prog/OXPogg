const extraOpening=Object.fromEntries(Object.entries({
eng:`Could I have a coffee with milk?|Posso pedir um café com leite?|This sandwich is for here, please.|Este sanduíche é para comer aqui, por favor.
The bus stop is around the corner.|O ponto de ônibus fica logo na esquina.|How do I get to the nearest pharmacy?|Como chego à farmácia mais próxima?
Let’s put off the meeting until Monday.|Vamos adiar a reunião até segunda-feira.|We checked in as soon as we arrived.|Fizemos o check-in assim que chegamos.
I forgot my notebook, but it’s no big deal.|Esqueci meu caderno, mas não tem problema.|I’m down for a game after work.|Eu topo jogar depois do trabalho.
It all comes down to how much time we have.|Tudo depende de quanto tempo temos.|On balance, it was a good decision.|Considerando tudo, foi uma boa decisão.
The little inn was a far cry from the hotel in the ad.|A pousadinha era bem diferente do hotel do anúncio.|For all its flaws, the report raised an important question.|Apesar de todos os seus defeitos, o relatório levantou uma questão importante.`,
spa:`¿Me pones un café solo, por favor?|Um café preto, por favor?|Quiero una porción de tarta para llevar.|Quero uma fatia de torta para viagem.
La parada está a la vuelta de la esquina.|O ponto fica logo na esquina.|¿Queda lejos el aeropuerto?|O aeroporto fica longe?
Hicimos las maletas después de cenar.|Fizemos as malas depois do jantar.|Necesito un billete de ida y vuelta a Córdoba.|Preciso de uma passagem de ida e volta para Córdoba.
El concierto estuvo muy guay.|O show foi muito legal.|Pasamos un día chévere en la playa.|Passamos um dia bem legal na praia.
Las nuevas pruebas ponen en tela de juicio la sentencia.|As novas provas põem a sentença em dúvida.|A grandes rasgos, el libro trata de la memoria.|Em linhas gerais, o livro trata da memória.
La discusión no ha terminado, ni mucho menos.|A discussão está longe de ter terminado.|Huelga decir que deben respetarse las reglas.|Nem é preciso dizer que as regras devem ser respeitadas.`,
ita:`Il caffè senza zucchero è per me.|O café sem açúcar é para mim.|Vorrei due caffè da portare via.|Gostaria de dois cafés para viagem.
La fermata dell’autobus è dietro l’angolo.|O ponto de ônibus fica logo na esquina.|Vado al lavoro a piedi.|Vou a pé para o trabalho.
Se partiamo presto, possiamo fare le valigie stasera.|Se sairmos cedo, podemos fazer as malas hoje à noite.|Quanto costa un biglietto di andata e ritorno?|Quanto custa uma passagem de ida e volta?
Boh, chiediamolo a lei.|Sei lá, vamos perguntar para ela.|Dai, manca solo un minuto!|Vamos, só falta um minuto!
Quel risultato mette in discussione il metodo.|Esse resultado põe o método em questão.|In linea di massima possiamo accettare le modifiche.|Em princípio, podemos aceitar as mudanças.
A conti fatti, il viaggio è costato poco.|No fim das contas, a viagem custou pouco.|Per quanto mi consta, il documento non è ancora pubblico.|Até onde sei, o documento ainda não é público.`,
deu:`Möchtest du noch einen Kaffee?|Você quer mais um café?|Zwei Suppen zum Mitnehmen, bitte.|Duas sopas para viagem, por favor.
Die Bank ist gleich um die Ecke.|O banco fica logo na esquina.|Ich komme heute zu Fuß.|Hoje vou a pé.
Wir packen die Koffer morgen früh.|Fazemos as malas amanhã cedo.|In Frankfurt muss ich umsteigen.|Preciso fazer baldeação em Frankfurt.
Die Fahrt war echt krass.|O passeio foi muito intenso.|Ich habe Bock auf ein Eis.|Estou a fim de um sorvete.
Die neuen Zahlen stellen die Prognose in Frage.|Os novos números põem a previsão em dúvida.|Unter dem Strich hat niemand Geld verloren.|No fim das contas, ninguém perdeu dinheiro.
Ich habe nicht mal angerufen, geschweige denn einen Brief geschrieben.|Nem cheguei a ligar, muito menos a escrever uma carta.|Wir fahren morgen, es sei denn, der Zug fällt aus.|Vamos amanhã, a menos que o trem seja cancelado.`,
ara:`هَلْ تُرِيدُ قَهْوَةً بِدُونِ سُكَّرٍ؟|Você quer café sem açúcar?|الحِسَابُ، مِنْ فَضْلِكَ. هَلْ يُمْكِنُنِي الدَّفْعُ بِالبِطَاقَةِ؟|A conta, por favor. Posso pagar com cartão?
البَنْكُ بِالقُرْبِ مِنَ المَكْتَبَةِ.|O banco fica perto da biblioteca.|ذَهَبْتُ إِلَى المَحَطَّةِ عَلَى الأَقْدَامِ.|Fui a pé até a estação.
حَجَزَ أَخِي طَاوِلَةً لِأَرْبَعَةِ أَشْخَاصٍ.|Meu irmão reservou uma mesa para quatro pessoas.|كَمْ سِعْرُ التَّذْكِرَةِ ذَهَابًا وَإِيَابًا؟|Quanto custa a passagem de ida e volta?
ماشي، هستنّاك عند الباب.|Beleza, vou esperar você na porta.|الماتش ده كان جامد!|Esse jogo foi demais!
وَضَعَتِ الشَّهَادَةُ الرِّوَايَةَ الرَّسْمِيَّةَ مَوْضِعَ الشَّكِّ.|O depoimento pôs a versão oficial em dúvida.|مِنْ حَيْثُ المَبْدَأِ، يُمْكِنُ تَأْجِيلُ الاِجْتِمَاعِ.|Em princípio, é possível adiar a reunião.
الطَّرِيقُ بَعِيدٌ، نَاهِيكَ عَنْ زِحَامِ الصَّبَاحِ.|O caminho é longo, sem falar no trânsito da manhã.|وَخَيْرُ دَلِيلٍ عَلَى ذَلِكَ شَهَادَةُ المَرْضَى.|E a melhor prova disso é o depoimento dos pacientes.`,
jpn:`コーヒーは砂糖なしでお願いします。|Quero o café sem açúcar, por favor.|このケーキは持ち帰りで。|Este bolo é para viagem.
その角を曲がったところに郵便局があります。|Logo depois de virar aquela esquina, há uma agência dos correios.|ここから歩いて帰ります。|Vou voltar a pé daqui.
来週の切符を予約したいです。|Quero reservar a passagem da semana que vem.|京都駅で新幹線に乗り換えます。|Vou trocar para o trem-bala na estação de Quioto.
このラーメン、やばいほどおいしい。|Este lámen é absurdamente gostoso.|マジで助かった。|Sério, você me salvou.
委員会は調査方法に疑問を呈した。|O comitê questionou o método de pesquisa.|年齢だけでは一概には言えない。|Não dá para generalizar só pela idade.
安全が最優先なのは言うまでもない。|Nem é preciso dizer que a segurança vem primeiro.|彼はあえて返事をしなかった。|Ele decidiu deliberadamente não responder.`,
cmn:`我想要一杯不加糖的咖啡。|Quero um café sem açúcar.|这两个包子能打包带走吗？|Dá para embalar estes dois pãezinhos para viagem?
从车站走到学校要十分钟。|São dez minutos a pé da estação até a escola.|一直走，在药店那儿往左拐。|Siga em frente e vire à esquerda na farmácia.
你预订明晚的餐厅了吗？|Você reservou o restaurante para amanhã à noite?|我们需要提前出发，免得错过火车。|Precisamos sair mais cedo para não perder o trem.
我们下周再讨论预算。|Voltamos a discutir o orçamento na semana que vem.|我们为什么没去？说来话长。|Por que não fomos? É uma longa história.
这种说法没有充分的依据。|Essa afirmação não tem fundamento suficiente.|总的来说，居民更喜欢新路线。|De modo geral, os moradores preferem a nova rota.
她权衡了价格和质量，最后选了这一款。|Ela ponderou o preço e a qualidade e escolheu este modelo.|话虽如此，事情还没有完全解决。|Dito isso, a questão ainda não está totalmente resolvida.`
}).map(([key,value])=>[key,value.split('\n').map(line=>line.split('|'))]));
extraOpening.por=[
 ['Prefiro café sem açúcar.','I prefer coffee without sugar.','Prefiero el café sin azúcar.','Pode embalar para viagem?','Could you pack that to go?','¿Puedes prepararlo para llevar?'],
 ['Tem uma padaria na esquina.','There’s a bakery on the corner.','Hay una panadería en la esquina.','A escola fica a dez minutos a pé.','The school is a ten-minute walk away.','La escuela queda a diez minutos a pie.'],
 ['Vamos adiar a reunião por uma semana.','Let’s postpone the meeting for a week.','Vamos a aplazar la reunión una semana.','Ela fez as malas de manhã.','She packed in the morning.','Hizo las maletas por la mañana.'],
 ['A gente pode combinar os detalhes por mensagem.','We can work out the details by text.','Podemos acordar los detalles por mensaje.','Hoje estou de boa, sem compromisso.','I’m taking it easy today, with no plans.','Hoy estoy tranquilo y no tengo planes.'],
 ['Ele aceitou o acordo sem ressalvas.','He accepted the agreement without reservations.','Aceptó el acuerdo sin salvedades.','Em linhas gerais, a equipe aprovou o orçamento.','Broadly speaking, the team approved the budget.','A grandes rasgos, el equipo aprobó el presupuesto.'],
 ['Este capítulo acompanha os desdobramentos da crise.','This chapter follows the developments of the crisis.','Este capítulo sigue la evolución de la crisis.','À luz dos resultados, a hipótese precisa ser revista.','In light of the results, the hypothesis needs to be reconsidered.','A la luz de los resultados, hay que revisar la hipótesis.']
].map(([w,wEn,wEs,e,eEn,eEs])=>[w,bilingual(wEn,wEs),e,bilingual(eEn,eEs)]);
