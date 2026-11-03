"""Bloco complementar da aula 57: leitura guiada, laboratório de sons, cartões de cultura."""
EN = [['Ned lives in Boston.', 'One morning, he walks across the plaza.', 'A woman stands near the fountain.', 'She has a big map in her hands, and she looks worried.'], ['“**Excuse me, I’m lost**,” she says.', '“**Where do you want to go?**” Ned asks.', '“**To the Science Museum**,” she answers.', 'She shows him a name on the map.'], ['Ned thinks for a moment.', '“**It’s far from here. Take the bus**,” he says.', '“**Which bus?**” she asks.', '“**Number eighty-six. The stop is there**,” he says, and he points down the street.'], ['The woman smiles.', '“**Thank you very much**,” she says.', '“**Good luck!**” Ned says.', '“**Good luck, and safe travels!**” she says. Then she walks to the stop.'], ['Ned thinks of Treasure Planet, a Disney film from 2002.', 'In the story, a boy named Jim finds a map and follows it across space.', 'The crew asks, “Which way?” all the time.', 'Today, many people use a phone, but a kind answer is still better.', '“**Good thing we asked**,” Ned says to himself, and he goes to work.']]
PT = [
 ['O Ned mora em Boston.', 'Numa manhã, ele atravessa a praça.', 'Uma mulher está perto da fonte.', 'Ela tem um mapa grande nas mãos e parece preocupada.'],
 ['“**Com licença, estou perdida**”, ela diz.', '“**Aonde você quer ir?**”, o Ned pergunta.', '“**Ao Museu de Ciências**”, ela responde.', 'Ela mostra a ele um nome no mapa.'],
 ['O Ned pensa um momento.', '“**Fica longe daqui. Pegue o ônibus**”, ele diz.', '“**Qual ônibus?**”, ela pergunta.', '“**O número oitenta e seis. O ponto é ali**”, ele diz, e aponta rua abaixo.'],
 ['A mulher sorri.', '“**Muito obrigada**”, ela diz.', '“**Boa sorte!**”, diz o Ned.', '“**Boa sorte e boa viagem!**”, ela diz. Depois caminha até o ponto.'],
 ['O Ned pensa em Treasure Planet, um filme da Disney de 2002.', 'Na história, um menino chamado Jim encontra um mapa e o segue pelo espaço.', 'A tripulação pergunta “Qual caminho?” o tempo todo.', 'Hoje, muita gente usa o celular, mas uma resposta gentil ainda é melhor.', '“**Que bom que perguntamos**”, diz o Ned a si mesmo, e vai para o trabalho.'],
]
Y = {'sentences': [[{'en': e, 'pt': p} for e, p in zip(a, b)] for a, b in zip(EN, PT)],
 'soundlab': {'focus': 'acento em números: eighty × eighteen',
  'what': 'Em inglês, números como “eighty” e “eighteen” são quase iguais. A diferença está em qual sílaba tem força. Para dar o número do ônibus, isso muda tudo.',
  'how': 'Em números com -ty (eighty, sixty), a força vai na primeira sílaba e o final é curto: EIGH-ty. Em números com -teen (eighteen, sixteen), as duas sílabas são longas, com a força no final: eigh-TEEN.',
  'tip': 'Bata o dedo na mesa na sílaba forte: uma batida em EIGH-ty, e uma batida no final de eigh-TEEN.',
  'words': [{'w': 'eighty', 'pt': 'oitenta'}, {'w': 'museum', 'pt': 'museu'}, {'w': 'tourist', 'pt': 'turista'}],
  'pairs': [{'a': 'eighty', 'b': 'eighteen'}, {'a': 'sixty', 'b': 'sixteen'}, {'a': 'thirty', 'b': 'thirteen'}],
  'phrase': {'en': 'Number eighty-six. The stop is there.', 'pt': 'O número oitenta e seis. O ponto é ali.'}},
 'cards': [
  {'icon': '🙋', 'big': 'Excuse me', 'label': 'Comece com educação', 'sub': 'Nos EUA, para pedir ajuda a um desconhecido, comece com “Excuse me”. Fale devagar, sorria e faça uma pergunta curta. Muitas pessoas gostam de ajudar, mas tem gente com pressa, então agradeça com “Thank you”.'},
  {'icon': '📱', 'big': 'Phone maps', 'label': 'Mapa no celular', 'sub': 'Hoje, muita gente usa o aplicativo de mapa no celular. Mesmo assim, perguntar a uma pessoa ainda é comum, principalmente para saber qual ônibus pegar ou onde fica o ponto. Sempre confirme o número da linha.'},
  {'icon': '🚌', 'big': 'The T', 'label': 'Ônibus e metrô em Boston', 'sub': 'Em Boston, o metrô e os ônibus fazem parte de um sistema chamado “the T”. Para pegar o ônibus, procure uma placa com o número da linha no ponto. Se tiver dúvida, pergunte ao motorista antes de pagar.'},
  {'icon': '📏', 'big': 'Miles', 'label': 'Distâncias em milhas', 'sub': 'Nos EUA, as distâncias costumam ser em milhas: uma milha é um pouco mais de 1,6 km. Para dizer que algo é perto, as pessoas falam em minutos a pé, por exemplo “ten minutes on foot”.'}]}
