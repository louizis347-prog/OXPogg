"""Bloco extra · aula 47: Buy a transit card."""
X = dict(
 key=dict(big='Tap it on the reader', label='Cartão de transporte', sub='Em muitas cidades você compra e recarrega um cartão e encosta no leitor para passar; os nomes e preços variam.'),
 mini=[
  dict(who='Nina', en='Hi! I need a {transit card|ticket|one-way ticket}.', pt='Oi! Preciso de {um cartão de transporte|um bilhete|um bilhete só de ida}.'),
  dict(who='You', en='Sure. How much do you want to add?', pt='Claro. Quanto quer adicionar?'),
  dict(who='Nina', en='{Twenty|Ten|Thirty} dollars, please.', pt='{Vinte|Dez|Trinta} dólares, por favor.'),
  dict(who='You', en='Cash or card? Your {card|ticket|pass} is ready.', pt='Dinheiro ou cartão? Seu {cartão|bilhete|passe} está pronto.')],
 dlg=[
  dict(who='Nina', en='Hi! I need a {transit card|ticket|one-way ticket}.', pt='Oi! Preciso de {um cartão de transporte|um bilhete|um bilhete só de ida}.'),
  dict(who='You', en='Sure. How much do you want to add?', pt='Claro. Quanto quer adicionar?'),
  dict(who='Nina', en='{Twenty|Ten|Thirty} dollars, please.', pt='{Vinte|Dez|Trinta} dólares, por favor.'),
  dict(who='You', en='Cash or card?', pt='Dinheiro ou cartão?'),
  dict(who='Nina', en='{Cash|Card}. Here you go.', pt='{Dinheiro|Cartão}. Aqui está.'),
  dict(who='You', en='Here’s your {card|ticket} and your {change|receipt}.', pt='Aqui está seu {cartão|bilhete} e seu {troco|recibo}.'),
  dict(who='Nina', en='How do I use it?', pt='Como eu uso?'),
  dict(who='You', en='Tap it on the {reader|gate|machine}.', pt='Encoste no {leitor|portão|aparelho}.'),
  dict(who='Nina', en='Have a nice {day|trip|evening}!', pt='Tenha um bom {dia|trajeto|noite}!')],
 vocab=[
  dict(w='money', pt='dinheiro', e='💰', ex=['I have no money.', 'Money is in my wallet.']),
  dict(w='insert', pt='inserir', e='⬇️', ex=['Insert your card here.', 'I insert the ticket.']),
  dict(w='reader', pt='leitor', e='📟', ex=['Tap your card on the reader.', 'The reader is green now.']),
  dict(w='pass', pt='passe', e='🎫', ex=['I want a day pass.', 'This pass is for one day.']),
  dict(w='add', pt='adicionar / recarregar', e='➕', ex=['I want to add ten dollars.', 'How much do you want to add?']),
  dict(w='one-way', pt='só ida', e='➡️', ex=['A one-way ticket, please.', 'Is this a one-way trip?'])],
 molds=[
  dict(title='Pedir o cartão', frame='Hi! I need a {item}. {amount} dollars, please.', slots=[dict(key='item', opts=['transit card', 'one-way ticket', 'day pass']), dict(key='amount', opts=['Twenty', 'Ten', 'Thirty'])], model='Hi! I need a transit card. Twenty dollars, please.', note='Diga o que quer e quanto adicionar. “Please” suaviza o pedido.'),
  dict(title='Atender o cliente', frame='{ask}? Here’s your {item} and your {extra}.', slots=[dict(key='ask', opts=['Cash or card', 'Card or cash', 'Cash or phone']), dict(key='item', opts=['card', 'ticket', 'pass']), dict(key='extra', opts=['change', 'receipt', 'map'])], model='Cash or card? Here’s your card and your change.', note='Perguntas curtas: “X or Y?” para escolher entre duas opções.'),
  dict(title='Explicar como usar', frame='Tap it on the {where}. Then wait for the {sign}.', slots=[dict(key='where', opts=['reader', 'gate', 'machine']), dict(key='sign', opts=['green light', 'beep', 'screen'])], model='Tap it on the reader. Then wait for the green light.', note='Escreva duas instruções curtas com “Tap” e “wait”.')],
 sounds=[
  dict(say='Cash or card?', tag='ligação: cash or', tip='Junte: “cashor card”. A voz sobe em “cash” e desce em “card”.'),
  dict(say='Here you go.', tag='redução: here you go', tip='Rápido, quase “hear-ya-go”. É o que se diz ao entregar algo.'),
  dict(say='Tap it on the reader.', tag='ligação: tap it', tip='O “p” e o “it” se juntam: “tapit”. Forte em “tap” e “reader”.')],
 role=dict(turns=[
  dict(npc='Hi! I need a transit card.', opts=[
   dict(en='Sure. How much do you want to add?', pt='Claro. Quanto quer adicionar?', reply='Twenty dollars, please.'),
   dict(en='Of course. How much money do you want on it?', pt='Claro. Quanto dinheiro quer nele?', reply='Twenty dollars, please.'),
   dict(en='No problem. How much do you want to add?', pt='Sem problema. Quanto quer adicionar?', reply='Ten dollars is fine, please.')]),
  dict(npc=None, opts=[
   dict(en='Cash or card?', pt='Dinheiro ou cartão?', reply='Cash. Here you go.'),
   dict(en='OK. Will you pay with cash or card?', pt='Ok. Vai pagar em dinheiro ou cartão?', reply='Cash. Here you go.'),
   dict(en='Okay. Cash or card?', pt='São vinte dólares. Dinheiro ou cartão?', reply='Card, please. Here you go.')]),
  dict(npc=None, opts=[
   dict(en='Here’s your card and your change.', pt='Aqui está seu cartão e seu troco.', reply='Thanks! How do I use it?'),
   dict(en='Here you go. Your card is ready.', pt='Aqui está. Seu cartão está pronto.', reply='Thanks! How do I use it?'),
   dict(en='Thank you. Here’s your receipt too.', pt='Obrigado. Aqui está o recibo também.', reply='Great! How do I use it?')]),
  dict(npc=None, opts=[
   dict(en='Tap it on the reader.', pt='Encoste no leitor.', reply='Got it. Have a nice day!'),
   dict(en='Just tap it on the reader at the gate.', pt='É só encostar no leitor na catraca.', reply='Easy! Have a nice day!'),
   dict(en='Tap it, then go through the gate.', pt='Encoste e passe pela catraca.', reply='Thanks! Have a nice day!')])],
  change=['A cliente quer um bilhete só de ida em vez de um cartão.', 'A cliente só tem uma nota grande e você precisa dar troco.', 'O leitor não funciona; peça para ela tentar de novo.']),
 writing=dict(task='Escreva um diálogo curto de 3 falas: você compra um cartão de transporte, escolhe o valor e pergunta como usar.', model='Hi! I need a transit card. Twenty dollars, please. How do I use it? Thanks!', kw=['card', 'dollars', 'please', 'use'], checks=['Pedi o cartão de forma educada.', 'Disse quanto quero adicionar.', 'Perguntei como usar.']),
 scenes=dict(pool=['station', 'subway', 'sub2', 'counter'], npc=dict(g='f', role='customer'), you=dict(g='m')),
 convo=dict(npc=dict(name='Nina'), turns=[
  dict(npc='Hi! I need a transit card.', pt='Oi! Preciso de um cartão de transporte.', opts=[
   dict(en='Sure. How much do you want to add?', pt='Claro. Quanto quer adicionar?', ok=True, fb='Atende o pedido e pergunta o valor.'),
   dict(en='Yes, I need it too.', pt='Sim, eu também preciso.', ok=False, fb='Você é quem atende; não é cliente.'),
   dict(en='Where is the subway?', pt='Onde fica o metrô?', ok=False, fb='É pergunta de cliente, não de quem atende.')]),
  dict(npc='Twenty dollars, please.', pt='Vinte dólares, por favor.', opts=[
   dict(en='Thanks, see you.', pt='Obrigado, até logo.', ok=False, fb='A venda mal começou.'),
   dict(en='How much is it?', pt='Quanto custa?', ok=False, fb='Ela já disse o valor; falta perguntar a forma de pagar.'),
   dict(en='Cash or card?', pt='Dinheiro ou cartão?', ok=True, fb='Pergunta a forma de pagamento.')]),
  dict(npc='Cash. Here you go.', pt='Dinheiro. Aqui está.', opts=[
   dict(en='Here’s your card and your change.', pt='Aqui está seu cartão e seu troco.', ok=True, fb='Entrega o cartão e o troco.'),
   dict(en='Please, give me cash.', pt='Por favor, me dê dinheiro.', ok=False, fb='Ela já deu o dinheiro.'),
   dict(en='You are welcome.', pt='De nada.', ok=False, fb='Ela ainda não agradeceu.')]),
  dict(npc='How do I use it?', pt='Como eu uso?', opts=[
   dict(en='It costs twenty dollars.', pt='Custa vinte dólares.', ok=False, fb='Ela já pagou; quer saber como usar.'),
   dict(en='Tap it on the reader.', pt='Encoste no leitor.', ok=True, fb='Instrução curta e clara.'),
   dict(en='Use it to read.', pt='Use para ler.', ok=False, fb='Confunde “reader” com leitura.')]),
  dict(npc='Have a nice day!', pt='Tenha um bom dia!', opts=[
   dict(en='You too! Bye!', pt='Você também! Tchau!', ok=True, fb='Retribui o desejo.'),
   dict(en='Cash or card?', pt='Dinheiro ou cartão?', ok=False, fb='O pagamento já terminou.'),
   dict(en='Welcome to the station.', pt='Bem-vinda à estação.', ok=False, fb='É uma saudação de chegada, não de despedida.')])]),
)
