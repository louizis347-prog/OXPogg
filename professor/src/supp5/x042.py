"""Bloco extra · aula 42: Dinner at my place."""
X = dict(
 key=dict(big='What should I bring?', label='Aceitar um convite', sub='Pergunta educada para quem aceita jantar na casa de alguém; a resposta costuma ser leve, como “Just yourself”.'),
 mini=[
  dict(who='Jordan', en='Hi! Do you want to have {dinner|lunch|breakfast} at my place?', pt='Oi! Quer {jantar|almoçar|tomar café da manhã} na minha casa?'),
  dict(who='You', en='I’d love to! Is {Friday|Saturday|Sunday} OK?', pt='Eu adoraria! {Sexta|Sábado|Domingo} pode ser?'),
  dict(who='Jordan', en='Sure. Come at {seven|six|eight}. Do you like {pasta|pizza|soup}?', pt='Claro. Venha às {sete|seis|oito}. Você gosta de {massa|pizza|sopa}?'),
  dict(who='You', en='Yes, I love it! What should I bring?', pt='Sim, adoro! O que devo levar?')],
 dlg=[
  dict(who='Jordan', en='Hi! Do you want to have {dinner|lunch|breakfast} at my place?', pt='Oi! Quer {jantar|almoçar|tomar café da manhã} na minha casa?'),
  dict(who='You', en='I’d love to! {When|Where|What time}?', pt='Eu adoraria! {Quando|Onde|Que horas}?'),
  dict(who='Jordan', en='{Friday|Saturday|Sunday} at seven. Is that OK?', pt='{Sexta|Sábado|Domingo} às sete. Pode ser?'),
  dict(who='You', en='Perfect. What should I {bring|buy|make}?', pt='Perfeito. O que devo {levar|comprar|fazer}?'),
  dict(who='Jordan', en='Just yourself. Do you like {pasta|pizza|soup}?', pt='Só você mesmo. Você gosta de {massa|pizza|sopa}?'),
  dict(who='You', en='Yes, I love {pasta|pizza|soup}!', pt='Sim, adoro {massa|pizza|sopa}!'),
  dict(who='Jordan', en='Great. I’ll {cook|make|order} for you.', pt='Ótimo. Vou {cozinhar|preparar|pedir} para você.'),
  dict(who='You', en='Thanks, Jordan! See you {Friday|Saturday|Sunday}.', pt='Valeu, Jordan! Até {sexta|sábado|domingo}.'),
  dict(who='Jordan', en='Thanks for coming!', pt='Obrigado por vir!')],
 vocab=[
  dict(w='dinner', pt='jantar', e='🍽️', ex=['We have dinner at seven.', 'Dinner is ready!']),
  dict(w='guest', pt='convidado', e='🙋', ex=['You are my guest tonight.', 'Every guest brings a small gift.']),
  dict(w='invite', pt='convidar', e='💌', ex=['I want to invite you to my home.', 'Thanks for the invite!']),
  dict(w='bring', pt='levar / trazer', e='🎁', ex=['I can bring dessert.', 'Please bring a friend.']),
  dict(w='cook', pt='cozinhar', e='🍳', ex=['I cook pasta on Fridays.', 'Can you cook rice?']),
  dict(w='ready', pt='pronto', e='✅', ex=['Dinner is ready.', 'Are you ready to eat?'])],
 molds=[
  dict(title='Aceitar um convite', frame='I’d love to! Is {day} at {time} OK?', slots=[dict(key='day', opts=['Friday', 'Saturday', 'Sunday']), dict(key='time', opts=['six', 'seven', 'eight'])], model='I’d love to! Is Friday at six OK?', note='“I’d love to!” é um sim caloroso. Depois você confirma o dia e a hora.'),
  dict(title='Perguntar o que levar', frame='What should I {verb}? Do you like {food}?', slots=[dict(key='verb', opts=['bring', 'buy', 'make']), dict(key='food', opts=['dessert', 'fruit', 'cake'])], model='What should I bring? Do you like dessert?', note='“What should I…?” pede conselho. Aqui o anfitrião também pode responder “Just yourself”.'),
  dict(title='Agradecer ao anfitrião', frame='Thanks for {thing}! The {food} was {adj}.', slots=[dict(key='thing', opts=['having me over', 'the dinner', 'the invitation']), dict(key='food', opts=['pasta', 'soup', 'cake']), dict(key='adj', opts=['delicious', 'great', 'perfect'])], model='Thanks for having me over! The pasta was delicious.', note='Escreva uma mensagem curta de agradecimento depois do jantar.')],
 sounds=[
  dict(say='I’d love to!', tag='ritmo: love to', tip='Dê força a “love”. “I’d” fica curto e “to” fica fraco, quase “tuh”.'),
  dict(say='Do you like pasta?', tag='redução: do you', tip='Na fala rápida, “Do you” soa quase como “Dyuh”. Ouça e repita no ritmo.'),
  dict(say='Thanks for having me over!', tag='ligação: having me', tip='As palavras se juntam: “having-me-over”. A sílaba mais forte é “o” de “over”.')],
 role=dict(turns=[
  dict(npc='Hi! Do you want to have dinner at my place?', opts=[
   dict(en='I’d love to! When?', pt='Eu adoraria! Quando?', reply='Friday at seven. Is that OK?'),
   dict(en='Yes, thanks! What day?', pt='Sim, obrigado! Que dia?', reply='Friday at seven. Is that OK?'),
   dict(en='Sure! Which day?', pt='Claro! Qual dia?', reply='Friday at seven. Is that OK?')]),
  dict(npc=None, opts=[
   dict(en='Perfect. What should I bring?', pt='Perfeito. O que devo levar?', reply='Just yourself. Do you like pasta?'),
   dict(en='Yes, that’s fine. Can I bring dessert?', pt='Sim, pode ser. Posso levar sobremesa?', reply='That’s kind! Do you like pasta?'),
   dict(en='Great. Can I bring something?', pt='Ótimo. Posso levar alguma coisa?', reply='Just yourself. Do you like pasta?')]),
  dict(npc=None, opts=[
   dict(en='Yes, I love pasta!', pt='Sim, adoro massa!', reply='Great. I’ll cook for you.'),
   dict(en='Yes, pasta is my favorite.', pt='Sim, massa é a minha favorita.', reply='Great. I’ll cook for you.'),
   dict(en='Yes, but no meat, please.', pt='Sim, mas sem carne, por favor.', reply='No problem. I’ll make a vegetable sauce.')]),
  dict(npc=None, opts=[
   dict(en='Thanks, Jordan! See you Friday.', pt='Valeu, Jordan! Até sexta.', reply='See you Friday!'),
   dict(en='That’s so nice. See you Friday!', pt='Que gentil. Até sexta!', reply='See you! Come hungry.'),
   dict(en='Thank you! I can’t wait.', pt='Obrigado! Mal posso esperar.', reply='Me too! See you Friday.')])],
  change=['Você tem uma alergia e precisa avisar o anfitrião.', 'Você vai chegar quinze minutos atrasado.', 'O anfitrião muda o jantar para sábado.']),
 writing=dict(task='Escreva uma mensagem curta aceitando um convite para jantar. Pergunte o horário e o que levar, e agradeça.', model='I’d love to come to dinner on Friday! What time should I arrive? Can I bring dessert? Thanks for inviting me.', kw=['love', 'bring', 'friday', 'thanks'], checks=['Aceitei o convite de forma simpática.', 'Fiz pelo menos uma pergunta (horário ou o que levar).', 'Agradeci no final.']),
 scenes=dict(pool=['living', 'kitchen', 'home1', 'garden'], npc=dict(g='m', role='friend'), you=dict(g='f')),
 convo=dict(npc=dict(name='Jordan'), turns=[
  dict(npc='Hi! Do you want to have dinner at my place?', pt='Oi! Quer jantar na minha casa?', opts=[
   dict(en='I’d love to! When?', pt='Eu adoraria! Quando?', ok=True, fb='Resposta calorosa e já pergunta o horário.'),
   dict(en='Thanks. Where is your house?', pt='Obrigado. Onde fica sua casa?', ok=False, fb='Faz sentido, mas você não aceitou o convite antes.'),
   dict(en='Yes, I do want dinner.', pt='Sim, eu quero jantar.', ok=False, fb='Soa seco, como se você só quisesse comida. Aceite com “I’d love to!”.')]),
  dict(npc='Friday at seven. Is that OK?', pt='Sexta às sete. Pode ser?', opts=[
   dict(en='I like Friday.', pt='Eu gosto de sexta.', ok=False, fb='Não responde se o horário serve.'),
   dict(en='Perfect. What should I bring?', pt='Perfeito. O que devo levar?', ok=True, fb='Confirma o horário e oferece ajuda.'),
   dict(en='Yes, you are welcome.', pt='Sim, de nada.', ok=False, fb='“You’re welcome” responde a um agradecimento, não a uma pergunta.')]),
  dict(npc='Just yourself. Do you like pasta?', pt='Só você mesmo. Você gosta de massa?', opts=[
   dict(en='Yes, I love pasta!', pt='Sim, adoro massa!', ok=True, fb='Resposta direta e natural.'),
   dict(en='I can bring pasta.', pt='Posso levar massa.', ok=False, fb='O anfitrião disse que vai cozinhar; responda à pergunta.'),
   dict(en='No, thanks. I’m full.', pt='Não, obrigado. Estou cheio.', ok=False, fb='Essa frase serve quando oferecem comida na hora, não aqui.')]),
  dict(npc='Great. I’ll cook for you.', pt='Ótimo. Vou cozinhar para você.', opts=[
   dict(en='Good morning, Jordan!', pt='Bom dia, Jordan!', ok=False, fb='É uma saudação, não um agradecimento.'),
   dict(en='Do you cook every day?', pt='Você cozinha todo dia?', ok=False, fb='Possível, mas ignora a gentileza. Agradeça primeiro.'),
   dict(en='Thanks, Jordan! See you Friday.', pt='Valeu, Jordan! Até sexta.', ok=True, fb='Agradece e confirma o dia.')]),
  dict(npc='Thanks for coming!', pt='Obrigado por vir!', opts=[
   dict(en='Thanks for having me over!', pt='Obrigado por me receber!', ok=True, fb='Frase clássica do convidado.'),
   dict(en='Thanks for coming too!', pt='Obrigado por vir também!', ok=False, fb='Você é o convidado; quem recebeu foi ele.'),
   dict(en='Come to my place next time.', pt='Venha à minha casa na próxima.', ok=False, fb='Bom convite, mas agradeça primeiro.')])]))
