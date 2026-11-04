X = dict(
 key={'big': 'Can I bring something?', 'label': 'Aceitar e ajudar', 'sub': 'Depois de aceitar um convite, é comum perguntar se pode levar algo; a resposta varia conforme o anfitrião.'},
 mini=[
  {'who': 'Lina', 'en': 'Hi! Can you come to my {party|dinner|birthday party}?', 'pt': 'Oi! Você pode vir à minha {festa|jantar|festa de aniversário}?'},
  {'who': 'You', 'en': 'Sure! {When|Where|What time} is it?', 'pt': 'Claro! {Quando|Onde|Que horas} é?'},
  {'who': 'Lina', 'en': 'It’s on {Saturday|Friday|Sunday} at {eight|seven|six}.', 'pt': 'É no {sábado|sexta|domingo} às {oito|sete|seis}.'},
  {'who': 'You', 'en': 'Can I bring {something|a drink|a snack}?', 'pt': 'Posso levar {alguma coisa|uma bebida|um lanche}?'}],
 dlg=[
  {'who': 'Lina', 'en': 'Hi! Can you come to my {party|dinner|birthday party}?', 'pt': 'Oi! Você pode vir à minha {festa|jantar|festa de aniversário}?'},
  {'who': 'You', 'en': 'Sure! {When|Where|What time} is it?', 'pt': 'Claro! {Quando|Onde|Que horas} é?'},
  {'who': 'Lina', 'en': 'It’s on {Saturday|Friday|Sunday} at eight.', 'pt': 'É no {sábado|sexta|domingo} às oito.'},
  {'who': 'You', 'en': 'Where is it?', 'pt': 'Onde é?'},
  {'who': 'Lina', 'en': 'At my {house|apartment|friend’s place}. Here’s the address.', 'pt': 'Na minha {casa|apartamento|casa de um amigo}. Aqui está o endereço.'},
  {'who': 'You', 'en': 'Can I bring something?', 'pt': 'Posso levar alguma coisa?'},
  {'who': 'Lina', 'en': 'Sure! A {drink|juice|soda} or a snack.', 'pt': 'Claro! {Uma bebida|Um suco|Um refrigerante} ou um lanche.'},
  {'who': 'You', 'en': 'Great. I’ll bring {chips|juice|cookies}.', 'pt': 'Ótimo. Levo {salgadinhos|suco|biscoitos}.'},
  {'who': 'Lina', 'en': 'See you {Saturday|soon|then}!', 'pt': 'Até {sábado|logo|lá}!'}],
 vocab=[
  {'w': 'party', 'pt': 'festa', 'e': '🎉', 'ex': ['Can you come to my party?', 'The party is at eight.']},
  {'w': 'invite', 'pt': 'convidar', 'e': '💌', 'ex': ['I want to invite you.', 'Thanks for the invite!']},
  {'w': 'drink', 'pt': 'bebida', 'e': '🥤', 'ex': ['I’ll bring a drink.', 'Do you want a drink?']},
  {'w': 'snack', 'pt': 'lanche', 'e': '🍿', 'ex': ['A snack is fine.', 'I’ll bring a snack.']},
  {'w': 'gift', 'pt': 'presente', 'e': '🎁', 'ex': ['I have a gift for you.', 'The gift is small.']},
  {'w': 'address', 'pt': 'endereço', 'e': '📍', 'ex': ['What is your address?', 'Here’s the address.']}],
 molds=[
  {'title': 'Aceitar e perguntar', 'frame': 'Sure! {question} is it?', 'slots': [{'key': 'question', 'opts': ['When', 'Where', 'What time']}], 'model': 'Sure! When is it?', 'note': 'Depois de aceitar, pergunte quando, onde ou a hora. Em inglês, o verbo is vem antes de it.'},
  {'title': 'Perguntar o que levar', 'frame': 'Can I bring {thing}?', 'slots': [{'key': 'thing', 'opts': ['something', 'a drink', 'a snack', 'a dessert']}], 'model': 'Can I bring something?', 'note': 'Can I bring…? é um pedido educado de permissão.'},
  {'title': 'Decidir o que levar (escrever)', 'frame': 'I’ll bring {thing} on {day}.', 'slots': [{'key': 'thing', 'opts': ['chips', 'juice', 'cookies']}, {'key': 'day', 'opts': ['Saturday', 'Friday', 'Sunday']}], 'model': 'I’ll bring chips on Saturday.', 'note': 'I’ll + verbo mostra uma decisão tomada agora.'}],
 sounds=[
  {'say': 'Can I bring something?', 'tag': 'ligação: can I', 'tip': 'Junte can e I: “kenai”. Can fica fraco, e bring something fica fluido.'},
  {'say': 'It’s on Saturday at eight.', 'tag': 'ligação: at eight', 'tip': 'At e eight se ligam: “a-teit”. Sem pausa entre as palavras.'},
  {'say': 'I’ll bring chips.', 'tag': 'redução: I’ll', 'tip': 'I’ll soa como “ail”. É curto e leve, sem destacar.'}],
 role={'turns': [
  {'npc': 'Hi! Can you come to my party?', 'opts': [
   {'en': 'Sure! When is it?', 'pt': 'Claro! Quando é?', 'reply': 'It’s on Saturday at eight.'},
   {'en': 'I’d love to! What time is it?', 'pt': 'Eu adoraria! Que horas é?', 'reply': 'It starts at eight on Saturday.'},
   {'en': 'Yes, thanks! When is it?', 'pt': 'Sim, obrigado! Quando é?', 'reply': 'It’s this Saturday at eight.'}]},
  {'npc': 'It’s on Saturday at eight.', 'opts': [
   {'en': 'Where is it?', 'pt': 'Onde é?', 'reply': 'At my house. Here’s the address.'},
   {'en': 'Great! Where is the party?', 'pt': 'Ótimo! Onde é a festa?', 'reply': 'At my house. I’ll send the address.'},
   {'en': 'Nice. Where is it?', 'pt': 'Legal. Onde é?', 'reply': 'At my house. Here’s the address.'}]},
  {'npc': 'At my house. Here’s the address.', 'opts': [
   {'en': 'Can I bring something?', 'pt': 'Posso levar alguma coisa?', 'reply': 'Sure! A drink or a snack.'},
   {'en': 'Thanks! Can I bring a drink?', 'pt': 'Obrigado! Posso levar uma bebida?', 'reply': 'Yes, please! That’s great.'},
   {'en': 'Thank you. What can I bring?', 'pt': 'Obrigado. O que posso levar?', 'reply': 'A drink or a snack is perfect.'}]},
  {'npc': 'Sure! A drink or a snack.', 'opts': [
   {'en': 'Great. I’ll bring chips.', 'pt': 'Ótimo. Levo salgadinhos.', 'reply': 'Perfect! See you Saturday!'},
   {'en': 'OK. I’ll bring juice.', 'pt': 'Certo. Levo suco.', 'reply': 'Nice! See you Saturday!'},
   {'en': 'Good. I’ll bring cookies.', 'pt': 'Bom. Levo biscoitos.', 'reply': 'Yum! See you Saturday!'}]}],
  'change': ['Lina diz que não precisa levar nada: agradeça e diga que leva só um presente pequeno.', 'A festa mudou para domingo: confirme o novo dia e a hora.', 'Você não pode ir: recuse com educação e agradeça o convite.']},
 writing={'task': 'Responda ao convite de Lina por mensagem: agradeça, confirme o dia e diga o que vai levar.',
  'model': 'Hi Lina! Thanks for the invite. I can come on Saturday at eight. I’ll bring chips and juice. See you there!',
  'kw': ['thanks', 'saturday', 'bring', 'see'],
  'checks': ['Agradeci o convite (Thanks for the invite).', 'Confirmei o dia e a hora.', 'Disse o que vou levar com I’ll bring.']},
 scenes={'pool': ['home1', 'living', 'kitchen', 'street'], 'npc': {'g': 'f', 'role': 'friend'}, 'you': {'g': 'f'}},
 convo={'npc': {'name': 'Lina'}, 'story': 'Sua amiga Lina convida você para uma festa. Responda como um bom convidado.', 'turns': [
  {'npc': 'Hi! Can you come to my party?', 'pt': 'Oi! Você pode vir à minha festa?', 'opts': [
   {'en': 'Hi! I’m fine, thanks.', 'pt': 'Oi! Estou bem, obrigado.', 'ok': False, 'fb': 'Lina fez um convite, não perguntou como você está.'},
   {'en': 'Sure! When is it?', 'pt': 'Claro! Quando é?', 'ok': True, 'fb': 'Aceita e pergunta o horário.'},
   {'en': 'Yes, I have a party too.', 'pt': 'Sim, eu também tenho uma festa.', 'ok': False, 'fb': 'Não responde ao convite dela.'}]},
  {'npc': 'It’s on Saturday at eight.', 'pt': 'É no sábado às oito.', 'opts': [
   {'en': 'Where is it?', 'pt': 'Onde é?', 'ok': True, 'fb': 'A próxima pergunta natural: o lugar.'},
   {'en': 'I’m free on Saturday.', 'pt': 'Estou livre no sábado.', 'ok': False, 'fb': 'Não pergunta o local; falta saber onde é.'},
   {'en': 'See you Saturday!', 'pt': 'Até sábado!', 'ok': False, 'fb': 'Despedida cedo demais; ainda falta o endereço.'}]},
  {'npc': 'At my house. Here’s the address.', 'pt': 'Na minha casa. Aqui está o endereço.', 'opts': [
   {'en': 'Thanks! When is it?', 'pt': 'Obrigado! Quando é?', 'ok': False, 'fb': 'Ela já disse o horário.'},
   {'en': 'Can I bring something?', 'pt': 'Posso levar alguma coisa?', 'ok': True, 'fb': 'Boa pergunta para um convidado.'},
   {'en': 'I’m sorry, I can’t.', 'pt': 'Sinto muito, não posso.', 'ok': False, 'fb': 'Você já aceitou o convite.'}]},
  {'npc': 'Sure! A drink or a snack.', 'pt': 'Claro! Uma bebida ou um lanche.', 'opts': [
   {'en': 'Where is the address?', 'pt': 'Onde está o endereço?', 'ok': False, 'fb': 'Ela já entregou o endereço.'},
   {'en': 'You’re welcome.', 'pt': 'De nada.', 'ok': False, 'fb': 'Ninguém agradeceu ainda; você deve escolher o que levar.'},
   {'en': 'Great. I’ll bring chips.', 'pt': 'Ótimo. Levo salgadinhos.', 'ok': True, 'fb': 'Escolhe um lanche, como ela sugeriu.'}]},
  {'npc': 'See you Saturday!', 'pt': 'Até sábado!', 'opts': [
   {'en': 'See you! Thanks for the invite.', 'pt': 'Até lá! Obrigado pelo convite.', 'ok': True, 'fb': 'Despede-se e agradece.'},
   {'en': 'Good morning, Lina!', 'pt': 'Bom dia, Lina!', 'ok': False, 'fb': 'Isto é uma saudação, não uma despedida.'},
   {'en': 'Can you come to my party?', 'pt': 'Você pode vir à minha festa?', 'ok': False, 'fb': 'O convidado é você, não ela.'}]}]},
)
