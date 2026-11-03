X = dict(
key=dict(big='His name is Max.', label='Falar do seu bichinho', sub='Use his/her para o nome e he/she para a idade: His name is Max. He\'s three years old.'),
mini=[
 dict(who='Claire', en='Look! What a cute {dog|cat|puppy}!', pt='Olha! Que {cachorro fofo|gato fofo|filhote fofo}!'),
 dict(who='You', en='Thanks! His name is {Max|Rex|Buddy}.', pt='Valeu! O nome dele é {Max|Rex|Buddy}.'),
 dict(who='Claire', en='How old is he? Does he like {people|kids|cats}?', pt='Quantos anos ele tem? Ele gosta de {gente|crianças|gatos}?'),
 dict(who='You', en='He\'s {three|two|five} years old. He loves {people|kids|cats}.', pt='Ele tem {três|dois|cinco} anos. Ele adora {gente|crianças|gatos}.'),
],
dlg=[
 dict(who='Claire', en='Look! What a cute {dog|puppy|cat}!', pt='Olha! Que {cachorro fofo|filhote fofo|gato fofo}!'),
 dict(who='You', en='Thanks! His name is {Max|Rex|Buddy}.', pt='Valeu! O nome dele é {Max|Rex|Buddy}.'),
 dict(who='Claire', en='How old is he?', pt='Quantos anos ele tem?'),
 dict(who='You', en='He\'s {three|two|five} years old.', pt='Ele tem {três|dois|cinco} anos.'),
 dict(who='Claire', en='Does he like {people|kids|cats}?', pt='Ele gosta de {gente|crianças|gatos}?'),
 dict(who='You', en='Yes, he loves people. Do you have a {pet|dog|cat}?', pt='Sim, ele adora gente. Você tem {um bichinho|um cachorro|um gato}?'),
 dict(who='Claire', en='I have a {cat|bird|fish}. Her name is Luna.', pt='Tenho {uma gata|um pássaro|um peixe}. O nome dela é Luna.'),
 dict(who='You', en='Nice! Max loves cats too.', pt='Legal! O Max também adora gatos.'),
 dict(who='Claire', en='Bring Luna to the {park|party|garden}!', pt='Traga a Luna ao {parque|festa|jardim}!'),
],
vocab=[
 dict(w='dog', pt='cachorro', e='🐶', ex=['I have a dog.', 'The dog is in the park.']),
 dict(w='cat', pt='gato', e='🐱', ex=['Her cat is Luna.', 'My cat sleeps on the sofa.']),
 dict(w='fish', pt='peixe', e='🐟', ex=['My brother has a fish.', 'The fish is small.']),
 dict(w='bird', pt='pássaro', e='🐦', ex=['The bird is on the tree.', 'She has a blue bird.']),
 dict(w='puppy', pt='filhote de cachorro', e='🐕', ex=['What a cute puppy!', 'The puppy is two months old.']),
 dict(w='pet', pt='bichinho de estimação', e='🐾', ex=['Do you have a pet?', 'My pet is a cat.']),
],
molds=[
 dict(title='Apresentar o bichinho', frame='My {pet} is {name}.', slots=[dict(key='pet', opts=['dog', 'cat', 'bird']), dict(key='name', opts=['Max', 'Luna', 'Rex'])], model='My dog is Max.', note='Depois do nome, use he/his ou she/her: His name is Max. Her name is Luna.'),
 dict(title='Idade e gosto', frame='My {pet} is {age} years old. It loves {thing}.', slots=[dict(key='pet', opts=['dog', 'cat', 'bird']), dict(key='age', opts=['two', 'three', 'five']), dict(key='thing', opts=['people', 'kids', 'cats'])], model='My dog is two years old. It loves people.', note='Idade: is + número + years old. It é neutro; com nome, prefira he/she.'),
 dict(title='Perguntar e responder por escrito', frame='Do you have a {pet}? I have a {mine}.', slots=[dict(key='pet', opts=['pet', 'dog', 'cat']), dict(key='mine', opts=['cat', 'bird', 'fish'])], model='Do you have a pet? I have a cat.', note='Do you have a…? pergunta o que a pessoa tem. Responda com I have a…'),
],
sounds=[
 dict(say='What a cute dog!', tag='acento: what a CUTE dog', tip='What a soa "wota". Dê força a CUTE e a DOG, a voz sobe.'),
 dict(say='How old is he?', tag='ligação: old is', tip='Old is liga como "ol-diz" e he perde o h: "ol-diz-ee".'),
 dict(say='He loves people.', tag='h fraco: he loves', tip='No meio da frase, he soa quase "ee". Loves liga com people.'),
],
role=dict(turns=[
 dict(npc='Look! What a cute dog!', opts=[
  dict(en='Thanks! His name is Max.', pt='Valeu! O nome dele é Max.', reply='Hi, Max! How old is he?'),
  dict(en='Thank you! He is Max.', pt='Obrigado! Ele é o Max.', reply='Hi, Max! How old is he?'),
  dict(en='Thanks! This is my dog, Max.', pt='Valeu! Este é meu cachorro, o Max.', reply='Hi, Max! How old is he?')]),
 dict(npc='How old is he?', opts=[
  dict(en='He\'s three years old.', pt='Ele tem três anos.', reply='Nice! Does he like people?'),
  dict(en='He\'s two. He\'s still a puppy!', pt='Ele tem dois. Ainda é um filhote!', reply='Aww! Does he like people?'),
  dict(en='He is five years old.', pt='Ele tem cinco anos.', reply='Nice! Does he like people?')]),
 dict(npc='Does he like people?', opts=[
  dict(en='Yes, he loves people. Do you have a pet?', pt='Sim, ele adora gente. Você tem um bichinho?', reply='I have a cat. Her name is Luna.'),
  dict(en='Yes, he is very friendly. Do you have a pet?', pt='Sim, ele é muito amigável. Você tem um bichinho?', reply='I have a cat. Her name is Luna.'),
  dict(en='Yes, he does. And you? Any pets?', pt='Sim, gosta. E você? Tem bichinhos?', reply='I have a cat. Her name is Luna.')]),
 dict(npc='Bring Luna to the park!', opts=[
  dict(en='Nice! Max loves cats too.', pt='Legal! O Max também adora gatos.', reply='Great! See you at the park!'),
  dict(en='Good idea! We\'ll come on Saturday.', pt='Boa ideia! Vamos no sábado.', reply='Great! See you on Saturday!'),
  dict(en='Sure! Let\'s meet here tomorrow.', pt='Claro! Vamos nos encontrar aqui amanhã.', reply='Great! See you tomorrow!')]),
], change=['O seu bichinho é uma gata chamada Mel; ajuste he/his para she/her.', 'Claire pergunta se o seu cachorro morde; responda com calma.', 'Você não tem bichinho e diz isso, mas fala de um que gostaria de ter.']),
writing=dict(task='Escreva 2 ou 3 frases sobre um bichinho de estimação (real ou imaginado): nome, idade e do que ele gosta.', model='I have a dog. His name is Max. He is three years old. He loves people and the park.', kw=['dog', 'name', 'years', 'loves'], checks=['Disse o tipo de bichinho e o nome.', 'Disse a idade com years old.', 'Disse algo de que ele gosta.']),
scenes=dict(pool=['park', 'park2', 'street', 'garden', 'yard'], npc=dict(g='f', role='neighbor'), you=dict(g='m')),
convo=dict(npc=dict(name='Claire'), story='Você passeia com seu cachorro no parque e conhece Claire.', turns=[
 dict(npc='Look! What a cute dog!', pt='Olha! Que cachorro fofo!', opts=[
  dict(en='Thanks! His name is Max.', pt='Valeu! O nome dele é Max.', ok=True, fb='Agradece e apresenta o cachorro.'),
  dict(en='Yes, I am cute.', pt='Sim, eu sou fofo.', ok=False, fb='O elogio é ao cachorro, não a você.'),
  dict(en='No, thanks.', pt='Não, obrigado.', ok=False, fb='Não é uma oferta; agradeça ao elogio.')]),
 dict(npc='How old is he?', pt='Quantos anos ele tem?', opts=[
  dict(en='His name is Max.', pt='O nome dele é Max.', ok=False, fb='Você já disse o nome; agora ela quer a idade.'),
  dict(en='He has three years.', pt='Ele tem três anos.', ok=False, fb='Em inglês, idade usa to be: He is three years old.'),
  dict(en='He\'s three years old.', pt='Ele tem três anos.', ok=True, fb='Idade com to be.')]),
 dict(npc='Does he like people?', pt='Ele gosta de gente?', opts=[
  dict(en='Yes, he loves people. Do you have a pet?', pt='Sim, ele adora gente. Você tem um bichinho?', ok=True, fb='Responde e devolve a conversa.'),
  dict(en='Yes, he is a dog.', pt='Sim, ele é um cachorro.', ok=False, fb='A pergunta é se ele gosta de pessoas.'),
  dict(en='He is three years old.', pt='Ele tem três anos.', ok=False, fb='A idade já foi dita.')]),
 dict(npc='I have a cat. Her name is Luna.', pt='Tenho uma gata. O nome dela é Luna.', opts=[
  dict(en='Nice! Max loves cats too.', pt='Legal! O Max também adora gatos.', ok=True, fb='Reage e conecta com o seu cachorro.'),
  dict(en='His name is Luna?', pt='O nome dele é Luna?', ok=False, fb='Claire disse her: Luna é uma gata.'),
  dict(en='I have a dog, not a cat.', pt='Tenho um cachorro, não um gato.', ok=False, fb='Soa seco; ela só contou sobre a gata.')]),
 dict(npc='Bring Luna to the park!', pt='Traga a Luna ao parque!', opts=[
  dict(en='Good idea! See you there.', pt='Boa ideia! Até lá.', ok=True, fb='Aceita o convite.'),
  dict(en='How old is Luna?', pt='Quantos anos tem a Luna?', ok=False, fb='É uma pergunta válida, mas ela fez um convite e a resposta natural é aceitar.'),
  dict(en='Look! What a cute cat!', pt='Olha! Que gato fofo!', ok=False, fb='Luna ainda não está aqui.')]),
]),
)
