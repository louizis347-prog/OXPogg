"""Bloco complementar da aula 56: leitura guiada, laboratório de sons, cartões de cultura."""
EN = [['Sol is in Miami.', 'He is at a big hotel.', 'It is night, and he is tired.', 'He stands at the door of room 412.', 'He puts his key card on the lock.', 'The light stays red.'], ['Sol goes down to the lobby.', 'A man at the front desk says, “**Hello, how can I help?**”', '“**My key doesn’t work**,” Sol says.', '“**I’m sorry. I’ll send someone**,” the man says.'], ['“Thank you. Also, **the air conditioner is off**.”', '“Is it too hot?”', '“Yes, very hot.”', '“**We’ll fix it right away**,” the man says.'], ['Soon, a woman from the hotel opens the door with a new key.', 'She fixes the air conditioner in five minutes.', 'The room is cool again.', '“**Thanks for your patience**,” she says.', 'Sol puts a towel on the chair and smiles.'], ['Sol thinks of Rapunzel, a girl in an old fairy tale.', 'She is in a high tower with no door, and she needs help.', 'Sol’s problem is small.', 'He can ask for help at the front desk.', '“**It’s not a big deal**,” he says to himself.', 'Tonight, he sleeps well.']]
PT = [
 ['O Sol está em Miami.', 'Ele está num hotel grande.', 'É noite, e ele está cansado.', 'Ele está na porta do quarto 412.', 'Ele coloca o cartão-chave na fechadura.', 'A luz continua vermelha.'],
 ['O Sol desce até o saguão.', 'Um homem na recepção diz: “**Olá, como posso ajudar?**”', '“**Minha chave não funciona**”, diz o Sol.', '“**Sinto muito. Vou mandar alguém**”, diz o homem.'],
 ['“Obrigado. Além disso, **o ar-condicionado está desligado**.”', '“Está muito quente?”', '“Sim, muito quente.”', '“**Vamos consertar já**”, diz o homem.'],
 ['Logo, uma mulher do hotel abre a porta com uma chave nova.', 'Ela conserta o ar-condicionado em cinco minutos.', 'O quarto fica fresco de novo.', '“**Obrigada pela paciência**”, ela diz.', 'O Sol coloca uma toalha na cadeira e sorri.'],
 ['O Sol pensa na Rapunzel, uma menina de um conto de fadas antigo.', 'Ela está numa torre alta, sem porta, e precisa de ajuda.', 'O problema do Sol é pequeno.', 'Ele pode pedir ajuda na recepção.', '“**Não é nada demais**”, ele diz para si mesmo.', 'Esta noite, ele dorme bem.'],
]
Y = {'sentences': [[{'en': e, 'pt': p} for e, p in zip(a, b)] for a, b in zip(EN, PT)],
 'soundlab': {'focus': 'contrações com ’ll: I’ll, we’ll',
  'what': 'Em “I’ll send someone” e “We’ll fix it”, o ’ll é uma forma curta de “will” (futuro imediato). Brasileiros costumam acrescentar uma vogal (“aiu”) e o som fica pesado.',
  'how': 'Diga “ail” e “uil” numa só sílaba, terminando com a ponta da língua atrás dos dentes de cima, sem vogal depois. Em seguida, passe direto para o verbo: ail-SEND, uil-FIX.',
  'tip': 'Compare “I send” e “I’ll send” colocando a mão no pescoço: no segundo, a língua toca o céu da boca antes de “send”.',
  'words': [{'w': 'fix', 'pt': 'consertar'}, {'w': 'towel', 'pt': 'toalha'}, {'w': 'lobby', 'pt': 'saguão'}],
  'pairs': [{'a': 'I’ll send someone.', 'b': 'I send someone.'}, {'a': 'We’ll fix it.', 'b': 'We fix it.'}, {'a': 'He’ll help us.', 'b': 'He helps us.'}],
  'phrase': {'en': 'I’ll send someone, and we’ll fix it right away.', 'pt': 'Vou mandar alguém, e vamos consertar já.'}},
 'cards': [
  {'icon': '🛎️', 'big': 'Front desk', 'label': 'A recepção resolve', 'sub': 'Em hotéis dos EUA, o front desk costuma ajudar com chave, quarto, toalhas e problemas pequenos. Você pode ir ao saguão ou ligar do telefone do quarto. Diga o número do quarto logo no começo.'},
  {'icon': '🗝️', 'big': 'Key card', 'label': 'Cartão em vez de chave', 'sub': 'Muitos hotéis usam cartão magnético ou com chip. Se a luz da porta fica vermelha, tente de novo devagar. Se ainda não abrir, vá à recepção; às vezes o cartão perdeu o código perto do celular.'},
  {'icon': '🙏', 'big': 'Be polite', 'label': 'Educação ajuda', 'sub': 'Comece com “Hello” e termine com “Thank you”. Frases como “Can you send someone?” soam educadas. Reclamar com calma costuma resolver mais rápido do que falar alto. “Sorry for the trouble” é uma resposta comum do hotel.'},
  {'icon': '💵', 'big': 'Small tip', 'label': 'Gorjeta é costume', 'sub': 'Nos EUA, muitas pessoas deixam uma gorjeta pequena para quem ajuda com as malas ou limpa o quarto, em dinheiro. Não é obrigatório para um simples conserto, mas “Thank you” é sempre bem-vindo.'}]}
