"""Bloco de verbos e expressões da aula 109: pedir ajuda no trabalho."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('help', '🆘', 'ajudar', ('help', 'I help my coworker.', 'Eu ajudo meu colega.'), ('helps', 'Mia helps Ravi.', 'A Mia ajuda o Ravi.'), ('helped', 'She helped me yesterday.', 'Ela me ajudou ontem.'), ('helping', 'She is helping him now.', 'Ela está ajudando ele agora.'), 'Help + pessoa: help me, help him.'),
  vb('click', '🖱️', 'clicar', ('click', 'I click the link.', 'Eu clico no link.'), ('clicks', 'Mia clicks the file.', 'A Mia clica no arquivo.'), ('clicked', 'He clicked here.', 'Ele clicou aqui.'), ('clicking', 'I am clicking the folder.', 'Estou clicando na pasta.'), 'Click here = clique aqui. Regular: clicked.'),
  vb('explain', '💬', 'explicar', ('explain', 'I explain the steps.', 'Eu explico os passos.'), ('explains', 'Mia explains the file.', 'A Mia explica o arquivo.'), ('explained', 'She explained it twice.', 'Ela explicou duas vezes.'), ('explaining', 'He is explaining the link.', 'Ele está explicando o link.'), 'Explain it to me, não “explain me”.'),
  vb('fix', '🔧', 'consertar', ('fix', 'We fix the problem.', 'Nós consertamos o problema.'), ('fixes', 'The help desk fixes it.', 'O suporte conserta isso.'), ('fixed', 'Mia fixed the file.', 'A Mia consertou o arquivo.'), ('fixing', 'She is fixing my computer.', 'Ela está consertando meu computador.'), 'Com he/she: fixes (-es).'),
  vb('save', '💾', 'salvar', ('save', 'I save the file.', 'Eu salvo o arquivo.'), ('saves', 'Ravi saves the folder.', 'O Ravi salva a pasta.'), ('saved', 'He saved the report.', 'Ele salvou o relatório.'), ('saving', 'I am saving my work.', 'Estou salvando meu trabalho.'), 'Tire o e: saving. Passado: saved.')],
 verb_game=[
  dict(scene='A Mia sempre ajuda o Ravi.', en='Mia ___ Ravi with his computer.', opts=['help', 'helps', 'helped'], ans=1, pt='A Mia ajuda o Ravi com o computador.', why='Com “Mia” (ela), o presente leva -s.'),
  dict(scene='Ontem ele conseguiu salvar o arquivo.', en='Yesterday he ___ the file.', opts=['save', 'saving', 'saved'], ans=2, pt='Ontem ele salvou o arquivo.', why='“Yesterday” pede passado: saved.'),
  dict(scene='Agora a Mia está consertando o computador.', en='Mia is ___ my computer.', opts=['fix', 'fixes', 'fixing'], ans=2, pt='A Mia está consertando meu computador.', why='“is” + verbo com -ing.'),
  dict(scene='Vocês clicam no link todo dia.', en='We ___ the link every day.', opts=['click', 'clicks', 'clicked'], ans=0, pt='Nós clicamos no link todo dia.', why='Com “we”, use a forma base: click.')],
 expressions=[
  dict(en='Can you help me?', pt='Pode me ajudar?', ex='Excuse me, can you help me?', exp='Para pedir ajuda com educação.', c='a'),
  dict(en='What do you need?', pt='Do que você precisa?', ex='Sure. What do you need?', exp='Para oferecer ajuda e saber o problema.', c='b'),
  dict(en='I can’t open it', pt='Não consigo abrir', ex='I can’t open this file.', exp='Para dizer qual é o problema.', c='c'),
  dict(en='Let me see.', pt='Deixe-me ver.', ex='Let me see. Click here.', exp='Para dizer que vai olhar o problema.', c='d'),
  dict(en='Can you show me again?', pt='Pode me mostrar de novo?', ex='Yes. Can you show me again?', exp='Para pedir uma nova explicação.', c='a'),
  dict(en='It’s working now!', pt='Agora está funcionando!', ex='Thanks! It’s working now!', exp='Para dizer que o problema foi resolvido.', c='b')],
 expr_game=[
  dict(cue='Você precisa de ajuda com seu computador.', opts=['Can you help me?', 'Let me see.', 'What do you need?'], ans=0, why='Can you help me? pede ajuda.'),
  dict(cue='Você não entendeu e quer ver de novo.', opts=['Can you show me again?', 'It’s working now!', 'I can’t open it'], ans=0, why='Pede para mostrar de novo.'),
  dict(cue='O arquivo abriu e você quer avisar.', opts=['Let me see.', 'It’s working now!', 'What do you need?'], ans=1, why='It’s working now! avisa o resultado.')])
