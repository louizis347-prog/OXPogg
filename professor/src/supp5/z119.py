"""Bloco de verbos e expressões da aula 119: ficha de emprego."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('apply', '📨', 'candidatar-se', ('apply', 'I apply for the job.', 'Eu me candidato à vaga.'), ('applies', 'Noor applies today.', 'O Noor se candidata hoje.'), ('applied', 'She applied last week.', 'Ela se candidatou semana passada.'), ('applying', 'I am applying now.', 'Estou me candidatando agora.'), 'Apply for + vaga. Com ele/ela: applies; passado: applied (y vira i).'),
  vb('fill', '🖊️', 'preencher', ('fill', 'We fill in the form.', 'Nós preenchemos o formulário.'), ('fills', 'He fills in his name.', 'Ele preenche o nome.'), ('filled', 'I filled in the form.', 'Eu preenchi o formulário.'), ('filling', 'I am filling in the form.', 'Estou preenchendo o formulário.'), 'Fill in (ou fill out) the form = preencher o formulário.'),
  vb('sign', '✍️', 'assinar', ('sign', 'I sign at the bottom.', 'Eu assino embaixo.'), ('signs', 'Noor signs his name.', 'O Noor assina o nome.'), ('signed', 'She signed the paper.', 'Ela assinou o papel.'), ('signing', 'I am signing now.', 'Estou assinando agora.'), 'Sign é o verbo; signature é a assinatura (substantivo).'),
  vb('work', '💼', 'trabalhar', ('work', 'I work in a store.', 'Eu trabalho em uma loja.'), ('works', 'Ana works at a bank.', 'A Ana trabalha em um banco.'), ('worked', 'I worked in a shop.', 'Eu trabalhei em uma loja.'), ('working', 'I am working today.', 'Estou trabalhando hoje.'), 'Work in + lugar/área, work at + empresa específica.'),
  vb('type', '⌨️', 'digitar', ('type', 'I type my email.', 'Eu digito meu e-mail.'), ('types', 'She types fast.', 'Ela digita rápido.'), ('typed', 'He typed his name.', 'Ele digitou o nome.'), ('typing', 'I am typing my phone number.', 'Estou digitando meu telefone.'), 'Type serve para digitar no teclado; write é escrever à mão.')],
 verb_game=[
  dict(scene='Noor se candidata a uma vaga hoje.', en='Noor ___ for a job today.', opts=['apply', 'applies', 'applied'], ans=1, pt='O Noor se candidata a uma vaga hoje.', why='Com “Noor” (ele), o presente leva -es: applies.'),
  dict(scene='Ontem você assinou a ficha.', en='Yesterday I ___ the form.', opts=['sign', 'signs', 'signed'], ans=2, pt='Ontem eu assinei o formulário.', why='“Yesterday” pede passado: signed.'),
  dict(scene='Agora você preenche o formulário.', en='I am ___ in the form.', opts=['fill', 'fills', 'filling'], ans=2, pt='Estou preenchendo o formulário.', why='“am” + verbo termina em -ing: filling.'),
  dict(scene='Vocês trabalham na mesma loja.', en='We ___ in the same store.', opts=['work', 'works', 'worked'], ans=0, pt='Nós trabalhamos na mesma loja.', why='Com “we”, o presente fica na forma base: work.')],
 expressions=[
  dict(en='I’m here for…', pt='Estou aqui para…', ex='I’m here for the job application.', exp='Para dizer o motivo da visita.', c='a'),
  dict(en='What do I write first?', pt='O que escrevo primeiro?', ex='Thanks. What do I write first?', exp='Para pedir o primeiro passo no formulário.', c='b'),
  dict(en='at / dot', pt='arroba / ponto', ex='It’s noor at mail dot com.', exp='Para dizer um e-mail em voz alta.', c='c'),
  dict(en='Fingers crossed.', pt='Dedos cruzados.', ex='Fingers crossed you get the job.', exp='Para desejar sorte a alguém.', c='d'),
  dict(en='Keep me posted.', pt='Me mantenha informado.', ex='Thank you. Keep me posted.', exp='Para pedir notícias depois.', c='a'),
  dict(en='I could use the job.', pt='Eu preciso desse emprego.', ex='Thanks! I could use the job.', exp='Informal: dizer que o emprego ajudaria.', c='b')],
 expr_game=[
  dict(cue='Você quer dizer seu e-mail em voz alta.', opts=['Fingers crossed.', 'It’s noor at mail dot com.', 'Keep me posted.'], ans=1, why='Em e-mails, @ é “at” e . é “dot”.'),
  dict(cue='Você chegou na loja para pedir uma vaga.', opts=['I’m here for the job application.', 'I could use the job.', 'What do I write first?'], ans=0, why='I’m here for… diz o motivo da visita.'),
  dict(cue='Você quer receber notícias depois de entregar a ficha.', opts=['What do I write first?', 'Keep me posted.', 'Fingers crossed.'], ans=1, why='Keep me posted pede notícias.')])
