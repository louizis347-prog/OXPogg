"""Bloco de verbos e expressões da aula 111: uma ligação no trabalho."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('transfer', '🔀', 'transferir', ('transfer', 'We transfer calls to Sales.', 'Nós transferimos ligações para as Vendas.'), ('transfers', 'Tessa transfers the call.', 'A Tessa transfere a ligação.'), ('transferred', 'She transferred me to Mr. Lee.', 'Ela me transferiu para o Sr. Lee.'), ('transferring', 'I am transferring you now.', 'Estou transferindo você agora.'), 'Transfer vira transferred no passado (dobra o r).'),
  vb('dial', '🔢', 'discar', ('dial', 'I dial the extension.', 'Eu disco o ramal.'), ('dials', 'Sam dials the number.', 'O Sam disca o número.'), ('dialed', 'He dialed five five five.', 'Ele discou cinco cinco cinco.'), ('dialing', 'I am dialing now.', 'Estou discando agora.'), 'Dial = digitar o número para ligar. Passado regular: dialed.'),
  vb('repeat', '🔁', 'repetir', ('repeat', 'Please repeat the number.', 'Por favor, repita o número.'), ('repeats', 'Tessa repeats the name.', 'A Tessa repete o nome.'), ('repeated', 'She repeated the number.', 'Ela repetiu o número.'), ('repeating', 'I am repeating my name.', 'Estou repetindo meu nome.'), 'Pedido útil: Can you repeat that, please?'),
  vb('answer', '📞', 'atender / responder', ('answer', 'We answer at nine.', 'Nós atendemos às nove.'), ('answers', 'Tessa answers the phone.', 'A Tessa atende o telefone.'), ('answered', 'Nobody answered.', 'Ninguém atendeu.'), ('answering', 'She is answering a call.', 'Ela está atendendo uma ligação.'), 'Answer the phone = atender o telefone (sem “to”).'),
  vb('speak', '🗣️', 'falar', ('speak', 'I speak to the manager.', 'Eu falo com o gerente.'), ('speaks', 'Omar speaks slowly.', 'O Omar fala devagar.'), ('spoke', 'I spoke to Mr. Lee.', 'Eu falei com o Sr. Lee.'), ('speaking', 'Tessa speaking.', 'Tessa falando.'), 'Speak to alguém = falar com. Passado irregular: spoke.')],
 verb_game=[
  dict(scene='A recepcionista atende o telefone toda manhã.', en='Tessa ___ the phone every morning.', opts=['answer', 'answers', 'answered'], ans=1, pt='A Tessa atende o telefone toda manhã.', why='Com “Tessa” (ela), o presente leva -s: answers.'),
  dict(scene='Ontem você falou com o Sr. Lee.', en='Yesterday I ___ to Mr. Lee.', opts=['speak', 'spoke', 'speaking'], ans=1, pt='Ontem eu falei com o Sr. Lee.', why='“Yesterday” pede passado; speak vira spoke.'),
  dict(scene='Agora ela passa a ligação para outro ramal.', en='She is ___ the call now.', opts=['transfer', 'transfers', 'transferring'], ans=2, pt='Ela está transferindo a ligação agora.', why='“is” + verbo termina em -ing: transferring.'),
  dict(scene='Vocês discam o ramal toda vez.', en='We ___ the extension first.', opts=['dial', 'dials', 'dialed'], ans=0, pt='Nós discamos o ramal primeiro.', why='Com “we”, o presente fica na forma base: dial.')],
 expressions=[
  dict(en='Can I speak to…?', pt='Posso falar com…?', ex='Can I speak to Ms. Rose, please?', exp='Para pedir uma pessoa ao telefone.', c='a'),
  dict(en='One moment, please.', pt='Um momento, por favor.', ex='One moment, please. I’ll check.', exp='Para pedir que a pessoa espere na linha.', c='b'),
  dict(en='Can I take a message?', pt='Posso anotar um recado?', ex='He’s out. Can I take a message?', exp='Quem atende oferece isso quando a pessoa não está.', c='c'),
  dict(en='Hold on.', pt='Espere um pouco.', ex='Hold on, I’ll get a pen.', exp='Jeito informal de pedir para esperar.', c='d'),
  dict(en='call back', pt='ligar de volta', ex='Please call me back at ten.', exp='Verbo frasal: retornar uma ligação.', c='a'),
  dict(en='Sorry, wrong number.', pt='Desculpe, número errado.', ex='Oh, sorry, wrong number!', exp='Quando você liga para o lugar errado.', c='b')],
 expr_game=[
  dict(cue='Você quer falar com a Sra. Rose.', opts=['Can I speak to Ms. Rose?', 'Can I take a message?', 'Sorry, wrong number.'], ans=0, why='Can I speak to…? pede uma pessoa.'),
  dict(cue='A pessoa não está e você quer ajudar quem ligou.', opts=['Hold on.', 'Can I take a message?', 'Call back.'], ans=1, why='Can I take a message? oferece anotar o recado.'),
  dict(cue='Você disca e cai na casa de outra pessoa.', opts=['Sorry, wrong number.', 'One moment, please.', 'Can I speak to you?'], ans=0, why='Sorry, wrong number é o pedido de desculpas padrão.')])
