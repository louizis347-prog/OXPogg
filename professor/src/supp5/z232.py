"""Bloco de verbos e expressões da aula 232: cartões de visita."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('introduce', '🙋', 'apresentar', ('introduce', 'I introduce myself.', 'Eu me apresento.'), ('introduces', 'Paul introduces his boss.', 'O Paul apresenta o chefe dele.'), ('introduced', 'She introduced me to Nina.', 'Ela me apresentou à Nina.'), ('introducing', 'I am introducing a friend.', 'Estou apresentando uma amiga.'), 'Introduce myself = me apresentar.'),
  vb('exchange', '🔄', 'trocar', ('exchange', 'We exchange cards.', 'Nós trocamos cartões.'), ('exchanges', 'Lia exchanges emails with Paul.', 'A Lia troca e-mails com o Paul.'), ('exchanged', 'They exchanged phone numbers.', 'Eles trocaram números de telefone.'), ('exchanging', 'We are exchanging cards.', 'Estamos trocando cartões.'), 'Exchange cards = trocar cartões entre duas pessoas.'),
  vb('hand', '✋', 'entregar', ('hand', 'I hand him my card.', 'Eu entrego meu cartão a ele.'), ('hands', 'Paul hands her a card.', 'O Paul entrega um cartão a ela.'), ('handed', 'She handed me a pen.', 'Ela me entregou uma caneta.'), ('handing', 'He is handing out cards.', 'Ele está distribuindo cartões.'), 'Passado regular: handed.'),
  vb('know', '🧠', 'saber / conhecer', ('know', 'I know your company.', 'Eu conheço sua empresa.'), ('knows', 'Paul knows Nina.', 'O Paul conhece a Nina.'), ('knew', 'I knew his name.', 'Eu sabia o nome dele.'), ('knowing', 'I am knowing her.', 'Estou conhecendo ela.'), 'Know é verbo de estado, evite -ing. Passado irregular: knew.'),
  vb('prefer', '⭐', 'preferir', ('prefer', 'I prefer email.', 'Eu prefiro e-mail.'), ('prefers', 'Lia prefers email to calls.', 'A Lia prefere e-mail a ligações.'), ('preferred', 'He preferred a text.', 'Ele preferiu uma mensagem.'), ('preferring', 'I am preferring the card.', 'Estou preferindo o cartão.'), 'Prefer é verbo de estado: use “I prefer”. Dobra o r no passado: preferred.')],
 verb_game=[
  dict(scene='A Lia sempre prefere e-mail.', en='Lia ___ email to phone calls.', opts=['prefer', 'prefers', 'preferred'], ans=1, pt='A Lia prefere e-mail a ligações.', why='Com “Lia” (ela), o presente leva -s: prefers.'),
  dict(scene='Ontem eles trocaram telefones.', en='Yesterday they ___ phone numbers.', opts=['exchange', 'exchanges', 'exchanged'], ans=2, pt='Ontem eles trocaram números de telefone.', why='“Yesterday” pede passado: exchanged.'),
  dict(scene='Você entrega o cartão agora.', en='I am ___ him my card.', opts=['hand', 'hands', 'handing'], ans=2, pt='Estou entregando meu cartão a ele.', why='“am” + verbo termina em -ing: handing.'),
  dict(scene='Você conhece a empresa dele.', en='I ___ his company.', opts=['know', 'knows', 'knew'], ans=0, pt='Eu conheço a empresa dele.', why='Com “I”, o presente fica na forma base: know.')],
 expressions=[
  dict(en='Nice to meet you.', pt='Prazer em conhecer você.', ex='Nice to meet you. I’m Ana.', exp='Ao conhecer alguém.', c='a'),
  dict(en='What do you do?', pt='O que você faz?', ex='What do you do, Ana?', exp='Pergunta sobre o trabalho de alguém.', c='b'),
  dict(en='Here’s my card.', pt='Aqui está meu cartão.', ex='Here’s my card. Call me.', exp='Ao entregar o cartão.', c='c'),
  dict(en='Here’s mine.', pt='Aqui está o meu.', ex='Thank you. Here’s mine.', exp='Para entregar o seu depois de receber o dele.', c='d'),
  dict(en='I’ll send you a message.', pt='Vou te mandar uma mensagem.', ex='Great. I’ll send you a message.', exp='Para prometer um contato depois.', c='a'),
  dict(en='I prefer…', pt='Eu prefiro…', ex='I prefer email to phone calls.', exp='Para dizer o que você escolhe de preferência.', c='b')],
 expr_game=[
  dict(cue='Você recebeu o cartão dele e quer dar o seu.', opts=['Thank you. Here’s mine.', 'What do you do?', 'I’ll send you a message.'], ans=0, why='Here’s mine entrega o seu cartão.'),
  dict(cue='Você quer saber qual é o trabalho dele.', opts=['Nice to meet you.', 'What do you do?', 'Here’s my card.'], ans=1, why='What do you do? pergunta o trabalho.'),
  dict(cue='Você quer dizer que gosta mais de e-mail.', opts=['I prefer email.', 'Here’s mine.', 'Nice to meet you.'], ans=0, why='I prefer… mostra sua escolha.')])
