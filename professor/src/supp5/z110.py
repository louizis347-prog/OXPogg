"""Bloco de verbos e expressões da aula 110: enviar um e-mail."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('write', '✏️', 'escrever', ('write', 'I write a short email.', 'Eu escrevo um e-mail curto.'), ('writes', 'Marta writes back.', 'A Marta responde por escrito.'), ('wrote', 'Victor wrote the subject.', 'O Victor escreveu o assunto.'), ('writing', 'I am writing to my manager.', 'Estou escrevendo para minha gerente.'), 'Irregular: write, wrote.'),
  vb('send', '📤', 'enviar', ('send', 'I send the email today.', 'Eu envio o e-mail hoje.'), ('sends', 'Victor sends the report.', 'O Victor envia o relatório.'), ('sent', 'She sent it at noon.', 'Ela enviou ao meio-dia.'), ('sending', 'I am sending it now.', 'Estou enviando agora.'), 'Irregular: send, sent. Send something to someone.'),
  vb('reply', '↩️', 'responder', ('reply', 'I reply to Marta.', 'Eu respondo à Marta.'), ('replies', 'Marta replies fast.', 'A Marta responde rápido.'), ('replied', 'He replied in ten minutes.', 'Ele respondeu em dez minutos.'), ('replying', 'I am replying now.', 'Estou respondendo agora.'), 'Termina em consoante + y: replies, replied.'),
  vb('attach', '📎', 'anexar', ('attach', 'I attach the file.', 'Eu anexo o arquivo.'), ('attaches', 'Victor attaches the report.', 'O Victor anexa o relatório.'), ('attached', 'I attached the form.', 'Eu anexei o formulário.'), ('attaching', 'He is attaching a photo.', 'Ele está anexando uma foto.'), 'Com he/she: attaches (-es).'),
  vb('read', '👀', 'ler', ('read', 'I read my emails.', 'Eu leio meus e-mails.'), ('reads', 'Marta reads the message.', 'A Marta lê a mensagem.'), ('read', 'She read it twice.', 'Ela leu duas vezes.'), ('reading', 'I am reading the report.', 'Estou lendo o relatório.'), 'O passado read se escreve igual, mas soa “red”.')],
 verb_game=[
  dict(scene='A Marta sempre responde rápido.', en='Marta ___ in ten minutes.', opts=['reply', 'replies', 'replied'], ans=1, pt='A Marta responde em dez minutos.', why='Com “Marta” (ela): reply vira replies.'),
  dict(scene='Ontem o Victor mandou o e-mail.', en='Yesterday Victor ___ the email.', opts=['send', 'sends', 'sent'], ans=2, pt='Ontem o Victor enviou o e-mail.', why='“Yesterday” pede passado irregular: sent.'),
  dict(scene='Agora você está escrevendo ao gerente.', en='I am ___ to my manager.', opts=['write', 'writes', 'writing'], ans=2, pt='Estou escrevendo ao meu gerente.', why='“am” + verbo com -ing.'),
  dict(scene='Vocês anexam o arquivo todo dia.', en='We ___ the file every day.', opts=['attach', 'attaches', 'attached'], ans=0, pt='Nós anexamos o arquivo todo dia.', why='Com “we”, use a forma base: attach.')],
 expressions=[
  dict(en='Can you help me write…?', pt='Pode me ajudar a escrever…?', ex='Can you help me write an email?', exp='Para pedir ajuda com um texto.', c='a'),
  dict(en='Who is it for?', pt='Para quem é?', ex='Sure. Who is it for?', exp='Para saber o destinatário.', c='b'),
  dict(en='Keep it short.', pt='Seja breve.', ex='Write your message. Keep it short.', exp='Conselho para e-mails de trabalho.', c='c'),
  dict(en='by Friday', pt='até sexta', ex='I need the report by Friday.', exp='Para dar um prazo.', c='d'),
  dict(en='Thank you.', pt='Obrigado.', ex='End with “Thank you.”', exp='Fecho educado de e-mail.', c='a'),
  dict(en='Do I add an attachment?', pt='Preciso anexar algo?', ex='Do I add an attachment?', exp='Para perguntar sobre anexos.', c='b')],
 expr_game=[
  dict(cue='Você quer dar um prazo no e-mail.', opts=['I need the report by Friday.', 'Who is it for?', 'Keep it short.'], ans=0, why='by Friday marca o prazo.'),
  dict(cue='Você quer saber para quem é o e-mail.', opts=['Thank you.', 'Who is it for?', 'by Friday'], ans=1, why='Who is it for? pergunta o destinatário.'),
  dict(cue='Você quer terminar o e-mail com educação.', opts=['Thank you.', 'Keep it short.', 'Who is it for?'], ans=0, why='Thank you. é o fecho comum.')])
