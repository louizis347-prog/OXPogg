"""Bloco de verbos e expressões da aula 160: convite de casamento."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('invite', '💌', 'convidar', ('invite', 'We invite twenty people.', 'Nós convidamos vinte pessoas.'), ('invites', 'Cole invites his cousin.', 'O Cole convida a prima.'), ('invited', 'They invited me.', 'Eles me convidaram.'), ('inviting', 'She is inviting everyone.', 'Ela está convidando todo mundo.'), 'Invite perde o e antes de -ing: inviting. Passado: invited.'),
  vb('dance', '💃', 'dançar', ('dance', 'We dance at the wedding.', 'Nós dançamos no casamento.'), ('dances', 'The bride dances a lot.', 'A noiva dança muito.'), ('danced', 'I danced all night.', 'Eu dancei a noite toda.'), ('dancing', 'They are dancing now.', 'Eles estão dançando agora.'), 'Dance perde o e antes de -ing: dancing.'),
  vb('cry', '😢', 'chorar', ('cry', 'I cry at weddings.', 'Eu choro em casamentos.'), ('cries', 'Her aunt cries.', 'A tia dela chora.'), ('cried', 'We cried with joy.', 'Nós choramos de alegria.'), ('crying', 'She is crying happy tears.', 'Ela está chorando de felicidade.'), 'Com ele/ela: cries (y vira ies). Passado: cried.'),
  vb('kiss', '💋', 'beijar', ('kiss', 'We kiss our friends.', 'Nós beijamos nossos amigos.'), ('kisses', 'The groom kisses the bride.', 'O noivo beija a noiva.'), ('kissed', 'He kissed her.', 'Ele a beijou.'), ('kissing', 'They are kissing.', 'Eles estão se beijando.'), 'Com ele/ela: kisses (acrescenta -es).'),
  vb('smile', '😊', 'sorrir', ('smile', 'I smile at the bride.', 'Eu sorrio para a noiva.'), ('smiles', 'Cole smiles a lot.', 'O Cole sorri muito.'), ('smiled', 'Everyone smiled.', 'Todos sorriram.'), ('smiling', 'She is smiling in the photo.', 'Ela está sorrindo na foto.'), 'Smile perde o e antes de -ing: smiling.')],
 verb_game=[
  dict(scene='O Cole convida muita gente.', en='Cole ___ a lot of people.', opts=['invite', 'invites', 'invited'], ans=1, pt='O Cole convida muita gente.', why='Com “Cole” (ele), o presente leva -s: invites.'),
  dict(scene='Ontem à noite você dançou muito.', en='Last night I ___ a lot.', opts=['dance', 'dancing', 'danced'], ans=2, pt='Ontem à noite eu dancei muito.', why='“Last night” pede passado: danced.'),
  dict(scene='Agora a tia está chorando de alegria.', en='My aunt is ___ with joy.', opts=['cry', 'cries', 'crying'], ans=2, pt='Minha tia está chorando de alegria.', why='“is” + verbo termina em -ing: crying.'),
  dict(scene='Na foto todos sorriem.', en='We ___ in the photo.', opts=['smile', 'smiles', 'smiled'], ans=0, pt='Nós sorrimos na foto.', why='Com “we” o presente fica na forma base: smile.')],
 expressions=[
  dict(en='I’m so happy for you.', pt='Estou tão feliz por você.', ex='You are getting married? I’m so happy for you!', exp='Para felicitar alguém por uma boa notícia.', c='a'),
  dict(en='Save the date.', pt='Guarde a data.', ex='Save the date: June tenth.', exp='Aviso antecipado do dia de um evento.', c='b'),
  dict(en='What should I wear?', pt='O que devo vestir?', ex='What should I wear to the wedding?', exp='Para perguntar a roupa ideal.', c='c'),
  dict(en='Congratulations!', pt='Parabéns!', ex='Congratulations, Cole and Ellie!', exp='Para felicitar noivos e outras conquistas.', c='d'),
  dict(en='Thanks for inviting me.', pt='Obrigado por me convidar.', ex='Thanks for inviting me. It’s beautiful.', exp='Para agradecer um convite.', c='a'),
  dict(en='See you there!', pt='Te vejo lá!', ex='I can come. See you there!', exp='Para se despedir depois de combinar um evento.', c='b')],
 expr_game=[
  dict(cue='Seu primo disse que vai se casar.', opts=['I’m so happy for you.', 'Save the date.', 'See you there!'], ans=0, why='I’m so happy for you. mostra alegria pela notícia.'),
  dict(cue='Você quer saber que roupa usar no casamento.', opts=['What should I wear?', 'Thanks for inviting me.', 'Congratulations!'], ans=0, why='What should I wear? pergunta a roupa.'),
  dict(cue='Você confirma presença e se despede.', opts=['Save the date.', 'See you there!', 'What should I wear?'], ans=1, why='See you there! fecha a conversa depois de combinar.')])
