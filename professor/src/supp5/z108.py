"""Bloco de verbos e expressões da aula 108: horário da reunião."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('begin', '▶️', 'começar', ('begin', 'We begin at ten.', 'Nós começamos às dez.'), ('begins', 'The meeting begins at ten.', 'A reunião começa às dez.'), ('began', 'It began on time.', 'Começou na hora.'), ('beginning', 'She is beginning now.', 'Ela está começando agora.'), 'Irregular: begin, began. Dobre o n: beginning.'),
  vb('finish', '🏁', 'terminar', ('finish', 'We finish at eleven.', 'Nós terminamos às onze.'), ('finishes', 'The boss finishes early.', 'O chefe termina cedo.'), ('finished', 'The meeting finished at ten thirty.', 'A reunião terminou às dez e meia.'), ('finishing', 'I am finishing my notes.', 'Estou terminando minhas anotações.'), 'Com he/she: finishes (-es).'),
  vb('plan', '🗺️', 'planejar', ('plan', 'I plan my day.', 'Eu planejo meu dia.'), ('plans', 'Evan plans the meeting.', 'O Evan planeja a reunião.'), ('planned', 'We planned it on Monday.', 'Nós planejamos na segunda.'), ('planning', 'They are planning a meeting.', 'Eles estão planejando uma reunião.'), 'Dobre o n: planned, planning.'),
  vb('check', '✅', 'conferir', ('check', 'I check the calendar.', 'Eu confiro o calendário.'), ('checks', 'She checks the room.', 'Ela confere a sala.'), ('checked', 'I checked the time.', 'Eu conferi a hora.'), ('checking', 'He is checking his email.', 'Ele está conferindo o e-mail.'), 'Check = conferir; também serve para olhar a hora.'),
  vb('write', '✏️', 'escrever', ('write', 'I write notes in my notebook.', 'Eu escrevo anotações no caderno.'), ('writes', 'Evan writes the time.', 'O Evan escreve o horário.'), ('wrote', 'She wrote the room number.', 'Ela escreveu o número da sala.'), ('writing', 'I am writing a list.', 'Estou escrevendo uma lista.'), 'Irregular: write, wrote.')],
 verb_game=[
  dict(scene='A reunião começa sempre às dez.', en='The meeting ___ at ten.', opts=['begin', 'begins', 'began'], ans=1, pt='A reunião começa às dez.', why='Com “meeting” (it), o presente leva -s.'),
  dict(scene='Ontem a Ana escreveu o número da sala.', en='Yesterday Ana ___ the room number.', opts=['write', 'writes', 'wrote'], ans=2, pt='Ontem a Ana escreveu o número da sala.', why='“Yesterday” pede passado irregular: wrote.'),
  dict(scene='Agora você está conferindo o horário.', en='I am ___ the time.', opts=['check', 'checks', 'checking'], ans=2, pt='Estou conferindo o horário.', why='“am” + verbo com -ing.'),
  dict(scene='Vocês terminam todo dia às cinco.', en='We ___ at five every day.', opts=['finish', 'finishes', 'finishing'], ans=0, pt='Nós terminamos às cinco todo dia.', why='Com “we”, use a forma base: finish.')],
 expressions=[
  dict(en='When is…?', pt='Quando é…?', ex='When is the team meeting?', exp='Para perguntar o horário ou o dia.', c='a'),
  dict(en='It’s at ten o’clock.', pt='É às dez horas.', ex='The meeting is at ten o’clock.', exp='Para dizer a hora exata.', c='b'),
  dict(en='on the second floor', pt='no segundo andar', ex='It is in room two, on the second floor.', exp='Para dizer em que andar fica.', c='c'),
  dict(en='About thirty minutes', pt='Uns trinta minutos', ex='It is about thirty minutes.', exp='Para dizer a duração, sem precisão.', c='d'),
  dict(en='Do I need to bring anything?', pt='Preciso levar algo?', ex='Do I need to bring anything?', exp='Para saber o que levar.', c='a'),
  dict(en='on time', pt='na hora certa', ex='I am always on time.', exp='Para dizer que chegou no horário.', c='b')],
 expr_game=[
  dict(cue='Você quer saber o horário da reunião.', opts=['When is the meeting?', 'How long is it?', 'It’s at ten o’clock.'], ans=0, why='When is…? pergunta quando.'),
  dict(cue='Você quer saber quanto tempo a reunião dura.', opts=['Where is it?', 'How long is it?', 'on time'], ans=1, why='How long is it? pergunta a duração.'),
  dict(cue='Você quer saber se deve levar algum material.', opts=['Do I need to bring anything?', 'About thirty minutes', 'on the second floor'], ans=0, why='É a pergunta sobre o que levar.')])
