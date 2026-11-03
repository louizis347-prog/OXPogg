X = dict(
 key={'big': 'Do you want to share?', 'label': 'Dividir a comida', 'sub': 'Em muitos restaurantes dos EUA, as porções são grandes e é comum dividir um prato; o garçom pode perguntar se vocês querem dividir.'},
 mini=[
  {'who': 'Aaron', 'en': 'Welcome! Do you want to {share|order|sit}?', 'pt': 'Bem-vindos! Querem {dividir|pedir|sentar}?'},
  {'who': 'You', 'en': 'Yes. What’s {good|popular|fresh} here?', 'pt': 'Sim. O que é {bom|famoso|fresco} aqui?'},
  {'who': 'Aaron', 'en': 'The {ribs|wings|fries} are great. Do you want {sides|corn|beans}?', 'pt': '{As costelas|As asinhas|As batatas} são ótimos. Querem {acompanhamentos|milho|feijão}?'},
  {'who': 'You', 'en': 'We’ll have one {rack of ribs|plate of wings|plate of fries}. {Corn|Beans|Salad}, please.', 'pt': 'Vamos querer {uma porção de costelas|um prato de asinhas|um prato de batatas}. {Milho|Feijão|Salada}, por favor.'}],
 dlg=[
  {'who': 'Aaron', 'en': 'Welcome! Do you want to share?', 'pt': 'Bem-vindos! Querem dividir?'},
  {'who': 'You', 'en': 'Yes. What’s {good|popular|fresh} here?', 'pt': 'Sim. O que é {bom|famoso|fresco} aqui?'},
  {'who': 'Aaron', 'en': 'The {ribs|wings|fries} are great.', 'pt': '{As costelas|As asinhas|As batatas} são ótimos.'},
  {'who': 'You', 'en': 'We’ll have one {rack of ribs|plate of wings|big plate of fries}.', 'pt': 'Vamos querer {uma porção de costelas|um prato de asinhas|um prato grande de batatas}.'},
  {'who': 'Aaron', 'en': 'Do you want {sides|salad|bread}?', 'pt': 'Querem {acompanhamentos|salada|pão}?'},
  {'who': 'You', 'en': '{Corn|Beans|Salad} and {beans|corn|bread}, please.', 'pt': '{Milho|Feijão|Salada} e {feijão|milho|pão}, por favor.'},
  {'who': 'Aaron', 'en': 'Anything to drink?', 'pt': 'Algo para beber?'},
  {'who': 'You', 'en': '{Two waters|Two sodas|Two teas}, please.', 'pt': '{Duas águas|Dois refrigerantes|Dois chás}, por favor.'},
  {'who': 'Aaron', 'en': 'Enjoy the {ribs|food|meal}!', 'pt': 'Aproveitem {as costelas|a comida|a refeição}!'}],
 vocab=[
  {'w': 'ribs', 'pt': 'costelas', 'e': '🍖', 'ex': ['The ribs are great.', 'We’ll have the ribs.']},
  {'w': 'plate', 'pt': 'prato', 'e': '🍽️', 'ex': ['One plate, please.', 'The plate is hot.']},
  {'w': 'corn', 'pt': 'milho', 'e': '🌽', 'ex': ['Corn and beans, please.', 'I like corn.']},
  {'w': 'beans', 'pt': 'feijão', 'e': '🫘', 'ex': ['Beans are my favorite side.', 'Beans and rice, please.']},
  {'w': 'share', 'pt': 'dividir', 'e': '🤝', 'ex': ['Do you want to share?', 'We can share a plate.']},
  {'w': 'side', 'pt': 'acompanhamento', 'e': '🥗', 'ex': ['Do you want a side?', 'One side is corn.']}],
 molds=[
  {'title': 'Oferecer e aceitar dividir', 'frame': 'Yes, let’s {action}. What’s {adj} here?', 'slots': [{'key': 'action', 'opts': ['share', 'order', 'sit here']}, {'key': 'adj', 'opts': ['good', 'popular', 'fresh']}], 'model': 'Yes, let’s share. What’s good here?', 'note': 'Let’s + verbo é uma proposta para o grupo; depois peça uma sugestão.'},
  {'title': 'Pedir pelo grupo', 'frame': 'We’ll have {main}. {side}, please.', 'slots': [{'key': 'main', 'opts': ['one rack of ribs', 'one big burger', 'one plate of chicken']}, {'key': 'side', 'opts': ['Corn', 'Beans', 'Salad']}], 'model': 'We’ll have one rack of ribs. Corn, please.', 'note': 'We’ll have… é natural para pedir em grupo.'},
  {'title': 'Pedir bebidas (escrever)', 'frame': '{number} {drink}, please.', 'slots': [{'key': 'number', 'opts': ['Two', 'Three', 'Four']}, {'key': 'drink', 'opts': ['waters', 'sodas', 'teas']}], 'model': 'Two waters, please.', 'note': 'Com número maior que um, o item vai para o plural.'}],
 sounds=[
  {'say': 'We’ll have one rack of ribs.', 'tag': 'redução: we’ll', 'tip': 'We’ll soa quase como “wil”. Dê força a one rack e ribs.'},
  {'say': 'Corn and beans, please.', 'tag': 'redução: and', 'tip': 'And fica “n”: “corn-n-beans”.'},
  {'say': 'Do you want to share?', 'tag': 'redução: want to', 'tip': 'Na fala natural, want to soa como “wanna”: “do-ya WANNA share?”.'}],
 role={'turns': [
  {'npc': 'Welcome! Do you want to share?', 'opts': [
   {'en': 'Yes. What’s good here?', 'pt': 'Sim. O que é bom aqui?', 'reply': 'The ribs are great.'},
   {'en': 'Yes, we do. What do you recommend?', 'pt': 'Sim. O que você recomenda?', 'reply': 'I recommend the ribs. They are great.'},
   {'en': 'Yes, please. What’s popular?', 'pt': 'Sim, por favor. O que é famoso?', 'reply': 'The ribs are great. Everybody likes them.'}]},
  {'npc': 'The ribs are great.', 'opts': [
   {'en': 'We’ll have one rack of ribs.', 'pt': 'Vamos querer uma porção de costelas.', 'reply': 'One rack of ribs. Do you want sides?'},
   {'en': 'Great! One rack to share, please.', 'pt': 'Ótimo! Uma porção para dividir, por favor.', 'reply': 'One rack to share. Do you want sides?'},
   {'en': 'We’ll take the ribs, please.', 'pt': 'Vamos levar as costelas, por favor.', 'reply': 'The ribs. Do you want sides?'}]},
  {'npc': 'Do you want sides?', 'opts': [
   {'en': 'Corn and beans, please.', 'pt': 'Milho e feijão, por favor.', 'reply': 'Corn and beans. Anything to drink?'},
   {'en': 'Just corn, please.', 'pt': 'Só milho, por favor.', 'reply': 'Corn. Anything to drink?'},
   {'en': 'Beans and a salad, please.', 'pt': 'Feijão e uma salada, por favor.', 'reply': 'Beans and a salad. Anything to drink?'}]},
  {'npc': 'Anything to drink?', 'opts': [
   {'en': 'Two waters, please.', 'pt': 'Duas águas, por favor.', 'reply': 'Two waters. Enjoy the ribs!'},
   {'en': 'Two sodas, please.', 'pt': 'Dois refrigerantes, por favor.', 'reply': 'Two sodas. Enjoy the ribs!'},
   {'en': 'One water and one tea, please.', 'pt': 'Uma água e um chá, por favor.', 'reply': 'One water and one tea. Enjoy the ribs!'}]}],
  'change': ['Seu amigo não come carne: peça frango para dividir.', 'Vocês são três: peça uma porção maior e três bebidas.', 'Falta um prato: peça outro prato para dividir.']},
 writing={'task': 'Escreva o pedido do seu grupo para Aaron: o prato para dividir, dois acompanhamentos e as bebidas.',
  'model': 'Hello! We’ll have one rack of ribs to share. Corn and beans, please. Two waters, please. Thank you!',
  'kw': ['share', 'ribs', 'corn', 'please'],
  'checks': ['Usei We’ll have… para pedir.', 'Pedi o prato para dividir e os acompanhamentos.', 'Pedi as bebidas no plural.']},
 scenes={'pool': ['diner', 'restaurant', 'cafe2', 'cafe3'], 'npc': {'g': 'm', 'role': 'waiter'}, 'you': {'g': 'f'}},
 convo={'npc': {'name': 'Aaron'}, 'story': 'Você e um amigo chegam a um restaurante de costelas. Aaron é o garçom.', 'turns': [
  {'npc': 'Welcome! Do you want to share?', 'pt': 'Bem-vindos! Querem dividir?', 'opts': [
   {'en': 'Thank you, welcome!', 'pt': 'Obrigada, bem-vindo!', 'ok': False, 'fb': 'Quem recebe é o garçom; ele fez uma pergunta.'},
   {'en': 'Yes. What’s good here?', 'pt': 'Sim. O que é bom aqui?', 'ok': True, 'fb': 'Aceita e pede uma sugestão.'},
   {'en': 'Enjoy the ribs!', 'pt': 'Aproveite as costelas!', 'ok': False, 'fb': 'Essa frase é do garçom, no fim.'}]},
  {'npc': 'The ribs are great.', 'pt': 'As costelas são ótimas.', 'opts': [
   {'en': 'Two waters, please.', 'pt': 'Duas águas, por favor.', 'ok': False, 'fb': 'Está cedo para a bebida; escolha o prato.'},
   {'en': 'We’ll have one rack of ribs.', 'pt': 'Vamos querer uma porção de costelas.', 'ok': True, 'fb': 'Faz o pedido do grupo.'},
   {'en': 'Yes, they are great.', 'pt': 'Sim, são ótimas.', 'ok': False, 'fb': 'Concorda, mas não pede nada.'}]},
  {'npc': 'Do you want sides?', 'pt': 'Querem acompanhamentos?', 'opts': [
   {'en': 'Corn and beans, please.', 'pt': 'Milho e feijão, por favor.', 'ok': True, 'fb': 'Escolhe os acompanhamentos.'},
   {'en': 'I am a side.', 'pt': 'Eu sou um acompanhamento.', 'ok': False, 'fb': 'Não faz sentido aqui.'},
   {'en': 'One rack, please.', 'pt': 'Uma porção, por favor.', 'ok': False, 'fb': 'As costelas já foram pedidas; agora são os acompanhamentos.'}]},
  {'npc': 'Anything to drink?', 'pt': 'Algo para beber?', 'opts': [
   {'en': 'Corn and beans, please.', 'pt': 'Milho e feijão, por favor.', 'ok': False, 'fb': 'Os acompanhamentos já foram escolhidos.'},
   {'en': 'Yes, I am thirsty.', 'pt': 'Sim, estou com sede.', 'ok': False, 'fb': 'Verdade, mas ele quer saber qual bebida.'},
   {'en': 'Two waters, please.', 'pt': 'Duas águas, por favor.', 'ok': True, 'fb': 'Pede as bebidas do grupo.'}]},
  {'npc': 'Enjoy the ribs!', 'pt': 'Aproveite as costelas!', 'opts': [
   {'en': 'Do you want to share?', 'pt': 'Querem dividir?', 'ok': False, 'fb': 'A pergunta é do garçom e já foi respondida.'},
   {'en': 'Thanks! This looks great.', 'pt': 'Obrigado! Parece ótimo.', 'ok': True, 'fb': 'Agradece de forma natural.'},
   {'en': 'Welcome to the restaurant!', 'pt': 'Bem-vindo ao restaurante!', 'ok': False, 'fb': 'Você é o cliente, não o garçom.'}]}]},
)
