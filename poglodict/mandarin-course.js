const mandarinOpening=[
['Café','咖啡 (kāfēi)','café','我每天早上喝咖啡。','Tomo café todas as manhãs.','这杯咖啡有点儿苦。','Esse café é um pouco amargo.','打包带走','embalar para levar','这杯咖啡请打包带走。','Embale este café para viagem, por favor.','我想把这个三明治打包带走。','Quero levar este sanduíche para viagem.'],
['Direções','车站 (chēzhàn)','estação','车站在银行旁边。','A estação fica ao lado do banco.','我们在车站门口见吧。','Vamos nos encontrar na entrada da estação.','往左拐','virar à esquerda','到路口往左拐。','Vire à esquerda no cruzamento.','过了桥以后往左拐。','Depois da ponte, vire à esquerda.'],
['Viagem','预订 (yùdìng)','reservar','我预订了一间双人房。','Reservei um quarto duplo.','我们最好提前预订车票。','É melhor reservar as passagens com antecedência.','提前出发','sair com antecedência','为了避开堵车，我们决定提前出发。','Para evitar o trânsito, decidimos sair com antecedência.','明天可能下雪，还是提前出发吧。','Pode nevar amanhã. É melhor sair mais cedo.'],
['Conversas','讨论 (tǎolùn)','discutir','我们先讨论一下这个问题。','Vamos discutir esse problema primeiro.','大家正在讨论新的安排。','Todos estão discutindo a nova programação.','说来话长','é uma longa história','问我为什么搬家？说来话长。','Por que eu me mudei? É uma longa história.','这件事说来话长，我们边走边聊吧。','É uma longa história. Vamos conversando pelo caminho.'],
['Argumentação','依据 (yījù)','base, fundamento','这个结论有什么依据？','Qual é a base dessa conclusão?','这份报告为决策提供了依据。','Este relatório deu base à decisão.','总的来说','de modo geral','总的来说，这项改革取得了成效。','De modo geral, essa reforma deu resultado.','总的来说，调查结果支持我们的判断。','De modo geral, os resultados da pesquisa sustentam nossa avaliação.'],
['Nuances','权衡 (quánhéng)','ponderar, pesar alternativas','我们必须权衡各种方案的利弊。','Precisamos ponderar os prós e contras das alternativas.','在做决定前，她仔细权衡了风险。','Antes de decidir, ela ponderou cuidadosamente os riscos.','话虽如此','dito isso, ainda assim','话虽如此，这个方案仍值得一试。','Dito isso, ainda vale a pena tentar esse plano.','话虽如此，我们也不能忽视成本。','Ainda assim, não podemos ignorar o custo.']
];
const mandarinGrammar=[
['Perguntas com 吗','Acrescente 吗 ao fim de uma afirmação para transformá-la em pergunta de sim ou não.','A ordem da frase é preservada. Palavras interrogativas, como 什么, normalmente dispensam 吗.',
 '你喝咖啡吗？','Você toma café?','这本书是你的吗？','Este livro é seu?','今天冷吗？','Está frio hoje?','你明天上班吗？','Você trabalha amanhã?'],
['Lugar com 在','Use sujeito + 在 + lugar para dizer onde alguém ou algo está.','Compare 在车站, na estação, com 去车站, ir à estação.',
 '我在车站。','Estou na estação.','钥匙在桌子上。','A chave está sobre a mesa.','医生在二楼。','A médica está no segundo andar.','图书馆在学校旁边。','A biblioteca fica ao lado da escola.'],
['Experiência com 过','Coloque 过 depois do verbo para falar de uma experiência anterior.','Na negativa, use 没(有) + verbo + 过.',
 '我去过上海。','Já fui a Xangai.','她没坐过飞机。','Ela nunca andou de avião.','你看过这部电影吗？','Você já viu este filme?','我们在那家店吃过饭。','Já comemos naquele restaurante.'],
['Concessão com 虽然…但是…','Use 虽然 para introduzir um fato e 但是 para apresentar o contraste.','O segundo conector pode ser omitido quando a relação fica clara.',
 '虽然下雨，但是我们还是出门了。','Embora chovesse, saímos mesmo assim.','虽然房间很小，但是很安静。','Embora o quarto seja pequeno, é bem silencioso.','虽然他很忙，却愿意帮忙。','Embora esteja ocupado, ele se dispõe a ajudar.','虽然比赛输了，大家还是很高兴。','Apesar de perder o jogo, todo mundo ficou feliz.'],
['Condição suficiente com 只要…就…','Use 只要 para a condição suficiente e 就 para a consequência.','Compare 只要, basta que, com 只有, somente se.',
 '只要你同意，我们就开始。','Basta você concordar para começarmos.','只要天气好，我们就去公园。','Se o tempo estiver bom, vamos ao parque.','只要按时交表，你就可以参加。','Basta entregar o formulário no prazo para participar.','只要给我两天，我就能修好。','Só preciso de dois dias para consertar.'],
['Ênfase com 正是…才…','Use 正是 para destacar a causa e 才 para indicar o resultado que depende dela.','Em registros formais, 正是因为 torna explícita a relação de causa.',
 '正是因为有你的帮助，我们才按时完成了任务。','Foi graças à sua ajuda que concluímos a tarefa a tempo.','正是这次失败，才让我们看清了问题。','Foi justamente essa derrota que nos fez enxergar o problema.','正是因为路上堵车，他才迟到了。','Foi por causa do trânsito que ele se atrasou.','正是有了对比，差异才变得明显。','Foi a comparação que tornou a diferença evidente.'],
['Classificadores com números','Entre o número e o substantivo, use um classificador adequado.','个 é comum, mas 本 serve para livros, 杯 para copos ou xícaras, e 张 para itens planos.',
 '我要一杯茶。','Quero uma xícara de chá.','他买了两本书。','Ele comprou dois livros.','请给我三张票。','Por favor, me dê três ingressos.','我们有四个问题。','Temos quatro perguntas.'],
['Posse com 的','Use possuidor + 的 + substantivo para indicar posse ou vínculo.','Em relações próximas, o 的 muitas vezes some, como em 我妈妈.',
 '这是我的手机。','Este é meu celular.','那是老师的书。','Aquele é o livro do professor.','这辆车是我姐姐的。','Este carro é da minha irmã.','他的朋友住得很近。','O amigo dele mora bem perto.'],
['Ação concluída com 了','Coloque 了 depois do verbo para marcar um acontecimento visto como concluído.','Com 没, normalmente não se usa esse 了 depois do verbo.',
 '我买了两张票。','Comprei dois ingressos.','她昨天写了三封邮件。','Ela escreveu três e-mails ontem.','孩子吃了早餐才出门。','A criança tomou café da manhã antes de sair.','我没买票，朋友买了两张。','Eu não comprei ingresso. Um amigo comprou dois.'],
['Objeto com 把','Use 把 antes de um objeto específico, seguido de uma ação que o afeta.','O verbo normalmente vem acompanhado de resultado, destino ou outro complemento.',
 '请把窗户关上。','Feche a janela, por favor.','我把票放进包里了。','Coloquei os ingressos dentro da bolsa.','她把文章改得更清楚了。','Ela editou o texto para deixá-lo mais claro.','别把手机忘在车上。','Não esqueça o celular no carro.'],
['Nem se… com 即使…也…','Use 即使 para criar uma hipótese extrema e 也 para manter a conclusão.','Compare com 虽然, que costuma admitir um fato já apresentado como real.',
 '即使下雨，我们也要出发。','Mesmo que chova, vamos partir.','即使时间不多，也应该核对数据。','Mesmo com pouco tempo, é preciso conferir os dados.','即使他反对，我们也可以继续讨论。','Mesmo que ele seja contra, podemos continuar discutindo.','即使没有掌声，她也会把戏演完。','Mesmo sem aplausos, ela vai terminar a peça.'],
['Escopo com 就…而言','Use 就 + assunto + 而言 para limitar o aspecto avaliado.','A construção é comum em textos argumentativos e relatórios.',
 '就成本而言，这个方案更合适。','Do ponto de vista do custo, essa proposta é mais adequada.','就目前的数据而言，还不能下结论。','Com os dados atuais, ainda não dá para tirar uma conclusão.','就交通而言，这个地点很方便。','Em termos de transporte, esse local é conveniente.','就长远发展而言，这笔投资很重要。','Em termos de desenvolvimento de longo prazo, esse investimento é importante.']
];
study.cmn=mandarinOpening.map((r,i)=>[r[0],r[1],r[3],r[4],mandarinGrammar[i][0],mandarinGrammar[i][1],mandarinGrammar[i][3],mandarinGrammar[i][4]]);
glosses.cmn=mandarinOpening.map(r=>r[2]);
phrases.cmn=mandarinOpening.map(r=>r.slice(7,11));
coreSeconds.cmn=mandarinOpening.map(r=>[r[5],r[6],r[11],r[12]]);
grammarPractice.cmn=mandarinGrammar.slice(6).map(r=>[r[0],r[1],r[3],r[4]]);
extraGrammar.cmn=mandarinGrammar.map(r=>r.slice(5,9));
grammarNotes.cmn=mandarinGrammar.map(r=>r[2]);
starterEntries.cmn=`你好|intj|hello|olá|你好，欢迎你！|Olá, seja bem-vindo!
谢谢|verb|to thank|agradecer, obrigado|谢谢你的帮助。|Obrigado pela ajuda.
请|verb|to ask or invite; please|pedir, convidar; por favor|请坐。|Sente-se, por favor.
水|noun|water|água|请给我一杯水。|Dê-me um copo de água, por favor.
今天|noun|today|hoje|今天天气很好。|O tempo está ótimo hoje.
明天|noun|tomorrow|amanhã|我们明天见。|Nos vemos amanhã.`;
authoredSeconds.cmn=new Map([
 ['你好',{text:'你好，我叫莉娅。',translation:'Olá, eu me chamo Lia.'}],
 ['谢谢',{text:'谢谢你等我。',translation:'Obrigado por me esperar.'}],
 ['请',{text:'请关门。',translation:'Feche a porta, por favor.'}],
 ['水',{text:'我带了一瓶水。',translation:'Trouxe uma garrafa de água.'}],
 ['今天',{text:'我今天在家工作。',translation:'Trabalho de casa hoje.'}],
 ['明天',{text:'图书馆明天开门。',translation:'A biblioteca abre amanhã.'}]
]);
reviewedEntries.cmn=new Map();
sceneVocabulary.cmn=[
 ['茶','noun','chá','我想喝茶。','Quero tomar chá.','这杯茶是热的。','Este chá está quente.'],
 ['三明治','noun','sanduíche','我要一个三明治。','Quero um sanduíche.','我带了一个三明治。','Trouxe um sanduíche.'],
 ['卡片','noun','cartão','我把单词写在卡片上。','Escrevi a palavra no cartão.','请给我一张卡片。','Por favor, me dê um cartão.'],
 ['语音消息','phrase','mensagem de voz','我收到了一条语音消息。','Recebi uma mensagem de voz.','你可以发一条语音消息。','Você pode mandar uma mensagem de voz.'],
 ['笔记','noun','anotações','我复习了昨天的笔记。','Revisei as anotações de ontem.','她喜欢用纸做笔记。','Ela gosta de fazer anotações no papel.']
];
readingFrames.cmn=[
`今天上课的时候，我们两个人一组。
我的卡片上写着“{word}”。
另一张卡片上写着“{expression}”。
{example}
最后，我们把卡片放在一起，第二天再复习。
你带今天的卡片了吗？
带了。我记下的是“{word}”。
{reply}
我的卡片上有“{expression}”这个表达。
我们把两张都夹在同一个本子里吧？
好。明天上课前我们再打开本子。`,
`上课前，我收到了一条语音消息。
第一部分讲的是“{word}”。
录音里还提到了“{expression}”。
{example}
我把消息存了下来，打算回家的路上再听一遍。
你听了我发的消息吗？
听了。“{word}”那一段说得太快了。
{reply}
我明白了。你还提到了“{expression}”，对吧？
对。要我把文字也发给你吗？
好，这样我可以一边听一边看。`,
`我在上周的本子里找到了两条笔记。
一条标出了“{word}”。
另一条标出了“{expression}”。
{example}
我把两条都抄在一页纸上，准备下节课带去。
你想复习哪一部分？
先看“{word}”那一部分。
{reply}
好，那之后再看“{expression}”吧？
行，我留一页纸来记这两个。
好。下节课我们对一对笔记。`
];
readingConnectors.cmn=['我们读了这个例句：“{line}”','看看这个例句：“{line}”','我们比较了这两个词语可以用在什么情境里。','我们现在可以练这个词。'];
cafeScenes.cmn=`上班前，我进了一家咖啡馆。
我点了一杯咖啡和一杯茶。
我请店员把咖啡打包带走。
店员把茶倒进了杯子里。
我坐在窗边喝完了茶。
早上好！您想喝点什么？
一杯咖啡，再来一杯茶，谢谢。
您在这儿喝，还是打包带走？
茶在这儿喝，咖啡打包带走。
好的。这是您的茶，咖啡马上就好。
谢谢，我就在这儿等。`;
cafeScenes.pt.cmn=`Antes do trabalho, entrei em um café.
Pedi um café e um chá.
Pedi ao atendente que embalasse o café para viagem.
O atendente colocou o chá numa xícara.
Sentei perto da janela e terminei o chá.
Bom dia! O que você gostaria de beber?
Um café e um chá, por favor.
Vai consumir aqui ou levar?
Vou tomar o chá aqui e levar o café.
Certo. Aqui está seu chá. O café fica pronto daqui a pouco.
Obrigado, vou esperar aqui mesmo.`;
