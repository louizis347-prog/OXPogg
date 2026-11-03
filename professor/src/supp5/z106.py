"""Bloco de verbos e expressões da aula 106: imprimir documentos."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('print', '🖨️', 'imprimir', ('print', 'I print my document.', 'Eu imprimo meu documento.'), ('prints', 'The printer prints five pages.', 'A impressora imprime cinco páginas.'), ('printed', 'Grace printed a report.', 'A Grace imprimiu um relatório.'), ('printing', 'She is printing now.', 'Ela está imprimindo agora.'), 'Regular: print, printed, printing.'),
  vb('press', '🔘', 'apertar', ('press', 'You press the green button.', 'Você aperta o botão verde.'), ('presses', 'Quinn presses Start.', 'O Quinn aperta Iniciar.'), ('pressed', 'I pressed the wrong button.', 'Eu apertei o botão errado.'), ('pressing', 'I am pressing five.', 'Estou apertando o cinco.'), 'Com he/she, press vira presses (-es).'),
  vb('copy', '📑', 'copiar', ('copy', 'We copy the pages.', 'Nós copiamos as páginas.'), ('copies', 'Ravi copies the form.', 'O Ravi copia o formulário.'), ('copied', 'I copied five pages.', 'Eu copiei cinco páginas.'), ('copying', 'They are copying a map.', 'Eles estão copiando um mapa.'), 'Copy termina em consoante + y: copies, copied.'),
  vb('fill', '📥', 'encher', ('fill', 'I fill the tray with paper.', 'Eu encho a bandeja de papel.'), ('fills', 'Quinn fills the tray.', 'O Quinn enche a bandeja.'), ('filled', 'She filled the tray.', 'Ela encheu a bandeja.'), ('filling', 'He is filling it now.', 'Ele está enchendo agora.'), 'Fill the tray with paper = encher a bandeja de papel.'),
  vb('type', '⌨️', 'digitar', ('type', 'I type my name.', 'Eu digito meu nome.'), ('types', 'Grace types the number.', 'A Grace digita o número.'), ('typed', 'He typed the report.', 'Ele digitou o relatório.'), ('typing', 'I am typing a letter.', 'Estou digitando uma carta.'), 'Type serve para digitar no teclado.')],
 verb_game=[
  dict(scene='A impressora está funcionando agora.', en='The printer ___ five pages.', opts=['print', 'prints', 'printed'], ans=1, pt='A impressora imprime cinco páginas.', why='Com “printer” (it), o presente leva -s.'),
  dict(scene='Ontem você apertou o botão errado.', en='Yesterday I ___ the wrong button.', opts=['press', 'pressing', 'pressed'], ans=2, pt='Ontem eu apertei o botão errado.', why='“Yesterday” pede passado: pressed.'),
  dict(scene='Agora o Quinn está colocando papel.', en='Quinn is ___ the tray.', opts=['fill', 'fills', 'filling'], ans=2, pt='O Quinn está enchendo a bandeja.', why='“is” + verbo com -ing: filling.'),
  dict(scene='Você explica o que sempre faz.', en='I ___ my name and press Print.', opts=['type', 'types', 'typing'], ans=0, pt='Eu digito meu nome e aperto Imprimir.', why='Com “I”, use a forma base: type.')],
 expressions=[
  dict(en='How do I use…?', pt='Como eu uso…?', ex='How do I use the printer?', exp='Para pedir instruções de uma máquina.', c='a'),
  dict(en='Let me help.', pt='Deixe eu ajudar.', ex='Let me help. Paper goes here.', exp='Para oferecer ajuda a um colega.', c='b'),
  dict(en='No paper', pt='Sem papel', ex='The screen says “No paper.”', exp='Aviso comum de impressora.', c='c'),
  dict(en='I need five copies.', pt='Preciso de cinco cópias.', ex='I need five copies, please.', exp='Para dizer quantas cópias quer.', c='d'),
  dict(en='Press Start', pt='Aperte Iniciar', ex='Press the number, then press Start.', exp='Último passo para copiar ou imprimir.', c='a'),
  dict(en='It works!', pt='Funcionou!', ex='Thanks, it works!', exp='Quando algo volta a funcionar.', c='b')],
 expr_game=[
  dict(cue='Você não sabe usar a impressora e pede ajuda.', opts=['How do I use the printer?', 'It works!', 'Let me help.'], ans=0, why='How do I use…? pede instruções.'),
  dict(cue='Seu colega está com problema e você quer ajudar.', opts=['No paper', 'Let me help.', 'I need five copies.'], ans=1, why='Let me help oferece ajuda.'),
  dict(cue='A impressora finalmente deu certo.', opts=['It works!', 'Press Start', 'How do I use…?'], ans=0, why='It works! comemora o resultado.')])
