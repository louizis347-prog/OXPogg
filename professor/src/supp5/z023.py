"""Bloco de verbos e expressões da aula 23: café da manhã no restaurante."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('want', '🍳', 'querer', ('want', 'I want scrambled eggs.', 'Eu quero ovos mexidos.'), ('wants', 'Mia wants tea.', 'A Mia quer chá.'), ('wanted', 'He wanted pancakes.', 'Ele queria panquecas.'), ('wanting', 'I am wanting more juice.', 'Estou querendo mais suco.'), 'Want + coisa. “I’d like” é mais educado que “I want”.'),
  vb('mix', '🙂', 'misturar', ('mix', 'I mix sugar into my coffee.', 'Eu misturo açúcar no café.'), ('mixes', 'Mia mixes honey into her tea.', 'A Mia mistura mel no chá.'), ('mixed', 'I mixed the juice with water.', 'Eu misturei o suco com água.'), ('mixing', 'I am mixing my yogurt.', 'Estou misturando meu iogurte.'), 'Com he/she/it, mix vira mixes (acrescenta -es).'),
  vb('eat', '🥞', 'comer', ('eat', 'We eat breakfast at eight.', 'Nós tomamos café da manhã às oito.'), ('eats', 'Tom eats toast.', 'O Tom come torrada.'), ('ate', 'I ate bacon and eggs.', 'Eu comi bacon e ovos.'), ('eating', 'She is eating pancakes.', 'Ela está comendo panquecas.'), 'Irregular: eat vira ate no passado.'),
  vb('drink', '☕', 'beber', ('drink', 'I drink coffee.', 'Eu bebo café.'), ('drinks', 'Ana drinks orange juice.', 'A Ana bebe suco de laranja.'), ('drank', 'He drank two teas.', 'Ele bebeu dois chás.'), ('drinking', 'I am drinking tea.', 'Estou bebendo chá.'), 'Irregular: drink vira drank.'),
  vb('enjoy', '😋', 'aproveitar', ('enjoy', 'I enjoy a big breakfast.', 'Eu curto um café da manhã grande.'), ('enjoys', 'Leo enjoys the toast.', 'O Leo curte a torrada.'), ('enjoyed', 'We enjoyed the meal.', 'Nós gostamos da refeição.'), ('enjoying', 'I am enjoying my eggs.', 'Estou curtindo meus ovos.'), 'Enjoy your meal! é o que o garçom diz ao servir.')],
 verb_game=[
  dict(scene='Hoje cedo você comeu panquecas.', en='This morning I ___ pancakes.', opts=['eat', 'ate', 'eating'], ans=1, pt='Esta manhã eu comi panquecas.', why='Passado irregular de eat: ate.'),
  dict(scene='A Mia mistura mel no chá.', en='Mia ___ honey into her tea.', opts=['mix', 'mixes', 'mixed'], ans=1, pt='A Mia mistura mel no chá.', why='Com “Mia” (ela) o presente leva -es: mixes.'),
  dict(scene='Agora você está tomando chá.', en='I am ___ tea with milk.', opts=['drink', 'drank', 'drinking'], ans=2, pt='Estou tomando chá com leite.', why='“am” + -ing: drinking.'),
  dict(scene='Nós queremos ovos fritos.', en='We ___ fried eggs, please.', opts=['want', 'wants', 'wanted'], ans=0, pt='Nós queremos ovos fritos, por favor.', why='Com “we” o presente usa a forma base: want.')],
 expressions=[
  dict(en='Table for two?', pt='Mesa para dois?', ex='Good morning! Table for two?', exp='O que o garçom pergunta quando você chega.', c='a'),
  dict(en='I’d like…', pt='Eu gostaria de…', ex='I’d like scrambled eggs, please.', exp='Jeito educado de fazer o pedido.', c='b'),
  dict(en='How do you want your eggs?', pt='Como você quer seus ovos?', ex='How do you want your eggs? — Fried, please.', exp='Pergunta sobre o ponto dos ovos.', c='c'),
  dict(en='With milk, please.', pt='Com leite, por favor.', ex='Coffee with milk, please.', exp='Para pedir um acompanhamento na bebida.', c='d'),
  dict(en='Are you ready to order?', pt='Você já quer pedir?', ex='Are you ready to order? — Yes, please.', exp='O garçom pergunta se pode anotar o pedido.', c='a'),
  dict(en='Enjoy your meal!', pt='Bom apetite!', ex='Here are your eggs. Enjoy your meal!', exp='Dito ao servir a comida.', c='b')],
 expr_game=[
  dict(cue='Você quer ovos mexidos.', opts=['Scrambled, please.', 'Table for two.', 'Enjoy your meal!'], ans=0, why='Scrambled, please responde como você quer os ovos.'),
  dict(cue='Você quer o chá com leite.', opts=['Are you ready to order?', 'With milk, please.', 'How do you want your eggs?'], ans=1, why='With milk, please pede o acompanhamento.'),
  dict(cue='Você quer fazer o pedido com educação.', opts=['I’d like pancakes, please.', 'Table for one?', 'Enjoy your meal!'], ans=0, why='I’d like… é o pedido educado.')])
