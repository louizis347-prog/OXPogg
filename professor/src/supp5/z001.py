"""Bloco de verbos e expressões da aula 1 (modelo): pedir um café."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('get', '☕', 'pegar / pedir', ('get', 'I get a small coffee.', 'Eu pego um café pequeno.'), ('gets', 'She gets a muffin.', 'Ela pega um muffin.'), ('got', 'He got a latte.', 'Ele pegou um latte.'), ('getting', 'I am getting a tea.', 'Estou pegando um chá.'), 'Can I get…? é o jeito mais comum de pedir. Passado: got.'),
  vb('order', '🧾', 'pedir', ('order', 'We order at the counter.', 'Nós pedimos no balcão.'), ('orders', 'Evan orders a bagel.', 'O Evan pede um bagel.'), ('ordered', 'I ordered oat milk.', 'Eu pedi leite de aveia.'), ('ordering', 'She is ordering now.', 'Ela está pedindo agora.'), 'Order serve para pedir comida e bebida; o passado só acrescenta -ed.'),
  vb('pay', '💳', 'pagar', ('pay', 'I pay by card.', 'Eu pago no cartão.'), ('pays', 'Ana pays here.', 'A Ana paga aqui.'), ('paid', 'He paid three dollars.', 'Ele pagou três dólares.'), ('paying', 'I am paying now.', 'Estou pagando agora.'), 'Atenção: pay vira paid (não “payed”) no passado.'),
  vb('wait', '⏳', 'esperar', ('wait', 'You wait on the left.', 'Você espera à esquerda.'), ('waits', 'She waits for her cup.', 'Ela espera pelo copo.'), ('waited', 'We waited five minutes.', 'Nós esperamos cinco minutos.'), ('waiting', 'I am waiting for my name.', 'Estou esperando meu nome.'), 'Wait for + algo ou alguém: wait for my order.'),
  vb('ask', '🗣️', 'perguntar / pedir', ('ask', 'I ask about oat milk.', 'Eu pergunto sobre leite de aveia.'), ('asks', 'Evan asks, “For here or to go?”', 'O Evan pergunta: “Para ficar ou levar?”'), ('asked', 'She asked for the price.', 'Ela perguntou o preço.'), ('asking', 'I am asking about the counter.', 'Estou perguntando sobre o balcão.'), 'Ask about = perguntar sobre; ask for = pedir algo.')],
 verb_game=[
  dict(scene='Toda manhã a Ana pede o mesmo café.', en='Ana ___ a small coffee every morning.', opts=['get', 'gets', 'got'], ans=1, pt='A Ana pega um café pequeno toda manhã.', why='Com “Ana” (ela), o presente leva -s: gets.'),
  dict(scene='Ontem você pagou três dólares.', en='Yesterday I ___ three dollars.', opts=['pay', 'paid', 'paying'], ans=1, pt='Ontem eu paguei três dólares.', why='“Yesterday” pede passado: paid.'),
  dict(scene='Agora o Evan está atendendo.', en='Evan is ___ for the order number.', opts=['ask', 'asks', 'asking'], ans=2, pt='O Evan está perguntando pelo número do pedido.', why='“is” + verbo termina em -ing: asking.'),
  dict(scene='Vocês esperam no balcão da esquerda.', en='We ___ at the pickup counter.', opts=['wait', 'waits', 'waited'], ans=0, pt='Nós esperamos no balcão de retirada.', why='Com “we” o presente fica na forma base: wait.')],
 expressions=[
  dict(en='Can I get…?', pt='Posso pedir…?', ex='Can I get a small coffee, please?', exp='Para pedir algo com educação em qualquer balcão.', c='a'),
  dict(en='For here or to go?', pt='Para ficar ou levar?', ex='“For here or to go?” — “To go, please.”', exp='A pergunta do atendente logo depois do pedido.', c='b'),
  dict(en='Do you have…?', pt='Vocês têm…?', ex='Do you have oat milk?', exp='Para saber se existe uma opção.', c='c'),
  dict(en='That’s all, thanks.', pt='É só isso, obrigado.', ex='No, that’s all, thanks.', exp='Para encerrar o pedido quando perguntam “Anything else?”.', c='d'),
  dict(en='pick up', pt='retirar / pegar', ex='I pick up my coffee on the left.', exp='Verbo frasal: pegar o pedido pronto.', c='a'),
  dict(en='Have a good one!', pt='Tenha um ótimo dia!', ex='Thanks! Have a good one!', exp='Despedida simpática e informal nos EUA.', c='b')],
 expr_game=[
  dict(cue='Você quer saber onde pegar a bebida pronta.', opts=['Where is the pickup counter?', 'Can I get a large tea?', 'That’s all, thanks.'], ans=0, why='Where is…? pergunta onde fica um lugar.'),
  dict(cue='O atendente pergunta se você quer mais alguma coisa e você não quer.', opts=['Do you have oat milk?', 'No, that’s all, thanks.', 'For here, please.'], ans=1, why='That’s all, thanks fecha o pedido.'),
  dict(cue='Você quer saber se existe leite de aveia.', opts=['For here or to go?', 'Do you have oat milk?', 'Have a good one!'], ans=1, why='Do you have…? verifica se existe uma opção.')])
