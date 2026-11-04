"""Bloco de verbos e expressões da aula 159: festa surpresa."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('hide', '🙈', 'esconder(-se)', ('hide', 'We hide behind the door.', 'Nós nos escondemos atrás da porta.'), ('hides', 'Hugo hides behind the sofa.', 'O Hugo se esconde atrás do sofá.'), ('hid', 'They hid in the kitchen.', 'Eles se esconderam na cozinha.'), ('hiding', 'We are hiding now.', 'Estamos nos escondendo agora.'), 'Passado irregular: hide vira hid. Em -ing, perde o e: hiding.'),
  vb('blow', '💨', 'soprar', ('blow', 'I blow out the candles.', 'Eu sopro as velas.'), ('blows', 'Mia blows out the candles.', 'A Mia sopra as velas.'), ('blew', 'She blew out the candles.', 'Ela soprou as velas.'), ('blowing', 'She is blowing now.', 'Ela está soprando agora.'), 'Passado irregular: blow vira blew. Blow out = apagar soprando.'),
  vb('light', '🕯️', 'acender', ('light', 'We light the candles.', 'Nós acendemos as velas.'), ('lights', 'Rosa lights the candles.', 'A Rosa acende as velas.'), ('lit', 'I lit ten candles.', 'Eu acendi dez velas.'), ('lighting', 'He is lighting a candle.', 'Ele está acendendo uma vela.'), 'Passado: lit (ou lighted). Light também é a palavra “luz”.'),
  vb('hug', '🤗', 'abraçar', ('hug', 'I hug my friends.', 'Eu abraço meus amigos.'), ('hugs', 'Mia hugs Rosa.', 'A Mia abraça a Rosa.'), ('hugged', 'We hugged Mia.', 'Nós abraçamos a Mia.'), ('hugging', 'They are hugging her.', 'Eles estão abraçando ela.'), 'Hug dobra o g no passado e no -ing: hugged, hugging.'),
  vb('shout', '📣', 'gritar', ('shout', 'We shout Surprise!', 'Nós gritamos Surpresa!'), ('shouts', 'Rosa shouts, “Surprise!”', 'A Rosa grita: “Surpresa!”'), ('shouted', 'Everyone shouted.', 'Todos gritaram.'), ('shouting', 'They are shouting now.', 'Eles estão gritando agora.'), 'Shout é regular. Shout at alguém pode soar bravo; aqui é de alegria.')],
 verb_game=[
  dict(scene='Toda vez a Mia sopra as velas.', en='Mia ___ out the candles.', opts=['blow', 'blows', 'blew'], ans=1, pt='A Mia sopra as velas.', why='Com “Mia” (ela), o presente leva -s: blows.'),
  dict(scene='Ontem todos se esconderam.', en='Yesterday we ___ behind the door.', opts=['hide', 'hid', 'hiding'], ans=1, pt='Ontem nós nos escondemos atrás da porta.', why='“Yesterday” pede passado: hid.'),
  dict(scene='Agora os amigos estão abraçando a Mia.', en='They are ___ Mia.', opts=['hug', 'hugs', 'hugging'], ans=2, pt='Eles estão abraçando a Mia.', why='“are” + verbo termina em -ing: hugging.'),
  dict(scene='Vocês acendem as velas no bolo.', en='We ___ the candles.', opts=['light', 'lights', 'lit'], ans=0, pt='Nós acendemos as velas.', why='Com “we” o presente fica na forma base: light.')],
 expressions=[
  dict(en='Shh! She’s coming.', pt='Shh! Ela está chegando.', ex='Shh! She’s coming. Hide!', exp='Para avisar que a pessoa está chegando.', c='a'),
  dict(en='Surprise!', pt='Surpresa!', ex='Surprise! Happy birthday!', exp='O grito quando a pessoa entra.', c='b'),
  dict(en='Make a wish.', pt='Faça um pedido.', ex='Make a wish and blow out the candles.', exp='Antes de soprar as velas do bolo.', c='c'),
  dict(en='I can’t believe it!', pt='Não acredito!', ex='Oh my gosh! I can’t believe it!', exp='Para mostrar muita surpresa.', c='d'),
  dict(en='Keep it a secret.', pt='Mantenha em segredo.', ex='Please keep it a secret.', exp='Para pedir que ninguém conte algo.', c='a'),
  dict(en='Happy birthday!', pt='Feliz aniversário!', ex='Happy birthday, Mia!', exp='A felicitação mais comum em festas.', c='b')],
 expr_game=[
  dict(cue='Você quer pedir segredo sobre a festa.', opts=['Keep it a secret.', 'Make a wish.', 'Surprise!'], ans=0, why='Keep it a secret. pede segredo.'),
  dict(cue='A aniversariante entra na sala.', opts=['Shh! She’s coming.', 'Surprise!', 'Make a wish.'], ans=1, why='Surprise! é o grito na hora da entrada.'),
  dict(cue='Ela vai soprar as velas do bolo.', opts=['Make a wish.', 'I can’t believe it!', 'Keep it a secret.'], ans=0, why='Make a wish. é dito antes de soprar as velas.')])
