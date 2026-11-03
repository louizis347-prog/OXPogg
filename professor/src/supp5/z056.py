"""Bloco de verbos e expressões da aula 056: um problema no hotel."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('fix', '🔧', 'consertar', ('fix', 'They fix the light.', 'Eles consertam a luz.'), ('fixes', 'She fixes the air conditioner.', 'Ela conserta o ar-condicionado.'), ('fixed', 'He fixed my TV.', 'Ele consertou minha TV.'), ('fixing', 'He is fixing the shower.', 'Ele está consertando a ducha.'), 'Fix é regular. Com ele/ela escreva fixes; no passado, fixed.'),
  vb('send', '📨', 'mandar / enviar', ('send', 'We send a towel to your room.', 'Nós mandamos uma toalha ao seu quarto.'), ('sends', 'The hotel sends someone.', 'O hotel manda alguém.'), ('sent', 'They sent a man.', 'Eles mandaram um homem.'), ('sending', 'I am sending a message.', 'Estou enviando uma mensagem.'), 'Send vira sent no passado (irregular).'),
  vb('break', '💔', 'quebrar', ('break', 'I never break my phone.', 'Eu nunca quebro meu celular.'), ('breaks', 'The key card breaks.', 'O cartão-chave quebra.'), ('broke', 'The TV broke last night.', 'A TV quebrou ontem à noite.'), ('breaking', 'The shower is breaking.', 'A ducha está quebrando.'), 'Break é irregular: broke no passado. O adjetivo é broken (quebrado).'),
  vb('work', '⚙️', 'funcionar / trabalhar', ('work', 'The lights work.', 'As luzes funcionam.'), ('works', 'My key works now.', 'Minha chave funciona agora.'), ('worked', 'The TV worked yesterday.', 'A TV funcionou ontem.'), ('working', 'The air conditioner is not working.', 'O ar-condicionado não está funcionando.'), 'Work também significa funcionar. Doesn’t work = não funciona.'),
  vb('check', '✅', 'conferir', ('check', 'We check the room.', 'Nós conferimos o quarto.'), ('checks', 'She checks the lock.', 'Ela confere a fechadura.'), ('checked', 'He checked the shower.', 'Ele conferiu a ducha.'), ('checking', 'I am checking my key.', 'Estou conferindo minha chave.'), 'Check = conferir, olhar se está certo. Passado regular: checked.')],
 verb_game=[
  dict(scene='O hotel manda uma pessoa agora.', en='The hotel ___ someone.', opts=['send', 'sends', 'sent'], ans=1, pt='O hotel manda alguém.', why='Com “the hotel” (ele) o presente leva -s: sends.'),
  dict(scene='Ontem a TV quebrou.', en='The TV ___ last night.', opts=['break', 'broke', 'breaking'], ans=1, pt='A TV quebrou ontem à noite.', why='“Last night” pede passado: broke.'),
  dict(scene='O técnico conserta a ducha agora.', en='He is ___ the shower.', opts=['fix', 'fixed', 'fixing'], ans=2, pt='Ele está consertando a ducha.', why='“is” + -ing: fixing.'),
  dict(scene='Sua chave funciona hoje.', en='My key ___ today.', opts=['works', 'work', 'worked'], ans=0, pt='Minha chave funciona hoje.', why='“My key” é singular (it): works.')],
 expressions=[
  dict(en='My key doesn’t work.', pt='Minha chave não funciona.', ex='Hello. My key doesn’t work.', exp='Para contar o problema na recepção.', c='a'),
  dict(en='I’ll send someone.', pt='Vou mandar alguém.', ex='I’m sorry. I’ll send someone.', exp='O hotel promete ajuda.', c='b'),
  dict(en='right away', pt='já / imediatamente', ex='We’ll fix it right away.', exp='Para dizer que será muito rápido.', c='c'),
  dict(en='Sorry for the trouble.', pt='Desculpe pelo problema.', ex='Sorry for the trouble!', exp='O hotel se desculpa por um problema.', c='d'),
  dict(en='Thanks for your patience.', pt='Obrigado pela paciência.', ex='Thanks for your patience.', exp='A equipe agradece quando você espera.', c='a'),
  dict(en='It’s not a big deal.', pt='Não é nada demais.', ex='No worries. It’s not a big deal.', exp='Para dizer que o problema é pequeno.', c='b')],
 expr_game=[
  dict(cue='Você quer dizer que sua chave não abre a porta.', opts=['My key doesn’t work.', 'I’ll send someone.', 'Sorry for the trouble.'], ans=0, why='Doesn’t work = não funciona.'),
  dict(cue='A recepção quer dizer que vai consertar muito rápido.', opts=['We’ll fix it right away.', 'My key doesn’t work.', 'Thanks a lot.'], ans=0, why='Right away = imediatamente.'),
  dict(cue='Você quer dizer que o problema é pequeno.', opts=['It’s not a big deal.', 'It’s very hot.', 'I’ll send someone.'], ans=0, why='Not a big deal = não é nada demais.')])
