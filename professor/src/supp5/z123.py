"""Bloco de verbos e expressões da aula 123: não me sinto bem."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('feel', '😷', 'sentir(-se)', ('feel', 'I feel hot.', 'Eu sinto calor.'), ('feels', 'Nell feels tired.', 'A Nell se sente cansada.'), ('felt', 'I felt sick at noon.', 'Eu me senti mal ao meio-dia.'), ('feeling', 'I am feeling better.', 'Estou me sentindo melhor.'), 'Passado irregular: feel vira felt. Em estados, feel e feeling são ambos comuns.'),
  vb('rest', '🛌', 'descansar', ('rest', 'I rest on Sunday.', 'Eu descanso no domingo.'), ('rests', 'She rests on the sofa.', 'Ela descansa no sofá.'), ('rested', 'He rested for an hour.', 'Ele descansou por uma hora.'), ('resting', 'I am resting now.', 'Estou descansando agora.'), 'Rest também é substantivo: a rest = um descanso.'),
  vb('lie', '🛋️', 'deitar(-se)', ('lie', 'I lie on the sofa.', 'Eu me deito no sofá.'), ('lies', 'Nell lies on the bed.', 'A Nell se deita na cama.'), ('lay', 'He lay down at noon.', 'Ele se deitou ao meio-dia.'), ('lying', 'She is lying down.', 'Ela está deitada.'), 'Passado irregular: lie vira lay; -ing é lying (ie vira y). Use lie down.'),
  vb('hurt', '🤕', 'doer', ('hurt', 'My head and back hurt.', 'Minha cabeça e minhas costas doem.'), ('hurts', 'My head hurts.', 'Minha cabeça dói.'), ('hurt', 'My neck hurt last night.', 'Meu pescoço doeu ontem à noite.'), ('hurting', 'My foot is hurting.', 'Meu pé está doendo.'), 'Hurt não muda no passado. My head hurts = minha cabeça dói.'),
  vb('sleep', '💤', 'dormir', ('sleep', 'We sleep eight hours.', 'Nós dormimos oito horas.'), ('sleeps', 'Nell sleeps a lot.', 'A Nell dorme bastante.'), ('slept', 'I slept an hour.', 'Eu dormi uma hora.'), ('sleeping', 'He is sleeping now.', 'Ele está dormindo agora.'), 'Passado irregular: sleep vira slept.')],
 verb_game=[
  dict(scene='Sua cabeça dói agora.', en='My head ___.', opts=['hurt', 'hurts', 'hurting'], ans=1, pt='Minha cabeça dói.', why='Head é singular (it): hurts.'),
  dict(scene='Ontem a Nell dormiu uma hora.', en='Yesterday Nell ___ one hour.', opts=['sleeps', 'sleeping', 'slept'], ans=2, pt='Ontem a Nell dormiu uma hora.', why='Yesterday pede passado: slept.'),
  dict(scene='Agora ela está deitada no sofá.', en='She is ___ on the sofa.', opts=['lie', 'lying', 'lays'], ans=1, pt='Ela está deitada no sofá.', why='is + -ing; lie vira lying.'),
  dict(scene='Você descansa um pouco todo dia.', en='I ___ a little every day.', opts=['rest', 'rests', 'resting'], ans=0, pt='Eu descanso um pouco todo dia.', why='Com I, o presente fica na forma base.')],
 expressions=[
  dict(en='I don’t feel well.', pt='Não me sinto bem.', ex='I don’t feel well today.', exp='Para dizer que está mal.', c='a'),
  dict(en='I have a headache.', pt='Estou com dor de cabeça.', ex='I have a headache and I’m tired.', exp='Para dizer o que dói.', c='b'),
  dict(en='Are you OK?', pt='Você está bem?', ex='You look tired. Are you OK?', exp='Para mostrar preocupação.', c='c'),
  dict(en='lie down', pt='deitar-se', ex='Lie down on the sofa.', exp='Verbo frasal: deitar para descansar.', c='d'),
  dict(en='take a nap', pt='tirar uma soneca', ex='I’ll take a nap.', exp='Para dormir um pouco de dia.', c='a'),
  dict(en='Feel better!', pt='Melhoras!', ex='Bye, Nell. Feel better!', exp='Para desejar melhoras a alguém.', c='b')],
 expr_game=[
  dict(cue='Você quer dizer que a cabeça dói.', opts=['I have a headache.', 'Are you OK?', 'Feel better!'], ans=0, why='I have a headache descreve a dor.'),
  dict(cue='Um amigo parece doente e você se preocupa.', opts=['Take a nap.', 'Are you OK?', 'I have a fever.'], ans=1, why='Are you OK? mostra preocupação.'),
  dict(cue='Você quer desejar melhoras.', opts=['Feel better!', 'Lie down.', 'I don’t feel well.'], ans=0, why='Feel better! é o desejo comum.')])
