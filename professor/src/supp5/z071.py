"""Bloco de verbos e expressões da aula 71: Wi-Fi e internet."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('connect', '🔗', 'conectar', ('connect', 'I connect to the home network.', 'Eu me conecto à rede de casa.'), ('connects', 'Cole connects his laptop.', 'O Cole conecta o notebook.'), ('connected', 'We connected to the Wi-Fi.', 'Nós nos conectamos ao Wi-Fi.'), ('connecting', 'He is connecting now.', 'Ele está se conectando agora.'), 'Connect to + rede: connect to the Wi-Fi.'),
  vb('type', '⌨️', 'digitar', ('type', 'You type the password here.', 'Você digita a senha aqui.'), ('types', 'Lia types fast.', 'A Lia digita rápido.'), ('typed', 'I typed the wrong letter.', 'Eu digitei a letra errada.'), ('typing', 'He is typing the password.', 'Ele está digitando a senha.'), 'Passado só com -ed: typed. Senhas têm maiúsculas e minúsculas.'),
  vb('check', '🔍', 'conferir / ver', ('check', 'I check the light.', 'Eu confiro a luz.'), ('checks', 'She checks the router.', 'Ela confere o roteador.'), ('checked', 'We checked the plug.', 'Nós conferimos a tomada.'), ('checking', 'I am checking the network.', 'Estou conferindo a rede.'), 'Let me check = deixe-me ver / conferir.'),
  vb('turn', '🔄', 'virar / ligar-desligar', ('turn', 'I turn the router off.', 'Eu desligo o roteador.'), ('turns', 'He turns it on.', 'Ele o liga.'), ('turned', 'We turned it off.', 'Nós o desligamos.'), ('turning', 'She is turning it on.', 'Ela está ligando.'), 'Turn on = ligar; turn off = desligar. Com “it”, fica no meio: turn it off.'),
  vb('search', '🌐', 'pesquisar', ('search', 'I search online.', 'Eu pesquiso na internet.'), ('searches', 'Lia searches for a tip.', 'A Lia pesquisa uma dica.'), ('searched', 'I searched for the answer.', 'Eu pesquisei a resposta.'), ('searching', 'He is searching for a website.', 'Ele está procurando um site.'), 'Search for = procurar por algo; a 3ª pessoa é searches.')],
 verb_game=[
  dict(scene='O Cole digita a senha agora mesmo.', en='Cole is ___ the password.', opts=['type', 'typing', 'types'], ans=1, pt='O Cole está digitando a senha.', why='“is” + verbo termina em -ing: typing.'),
  dict(scene='Ontem vocês desligaram o roteador.', en='Yesterday we ___ the router off.', opts=['turn', 'turns', 'turned'], ans=2, pt='Ontem nós desligamos o roteador.', why='“Yesterday” pede passado: turned.'),
  dict(scene='A Lia sempre confere a luz primeiro.', en='Lia always ___ the light first.', opts=['check', 'checks', 'checked'], ans=1, pt='A Lia sempre confere a luz primeiro.', why='Com “Lia” (ela) o presente leva -s: checks.'),
  dict(scene='Eu me conecto à rede da casa todo dia.', en='I ___ to the home network every day.', opts=['connect', 'connects', 'connecting'], ans=0, pt='Eu me conecto à rede da casa todo dia.', why='Com “I” o presente fica na forma base: connect.')],
 expressions=[
  dict(en='What\'s the Wi-Fi password?', pt='Qual é a senha do Wi-Fi?', ex='Hi! What\'s the Wi-Fi password?', exp='Para pedir a senha em casa, loja ou café.', c='a'),
  dict(en='It doesn\'t work.', pt='Não funciona.', ex='The Wi-Fi doesn\'t work.', exp='Para dizer que algo não está funcionando.', c='b'),
  dict(en='Let me check.', pt='Deixe-me ver.', ex='Let me check the router.', exp='Quando você vai olhar ou conferir antes de ajudar.', c='c'),
  dict(en='Turn it off and on again.', pt='Desligue e ligue de novo.', ex='Turn it off and on again, please.', exp='Dica clássica para consertar aparelhos.', c='d'),
  dict(en='The Wi-Fi is down.', pt='O Wi-Fi caiu.', ex='The Wi-Fi is down again.', exp='Para avisar que a internet está fora do ar.', c='a'),
  dict(en='Try resetting it.', pt='Tente reiniciá-lo.', ex='Try resetting it. Then wait a minute.', exp='Para sugerir reiniciar um aparelho.', c='b')],
 expr_game=[
  dict(cue='Você quer saber a senha da rede na casa de um amigo.', opts=['What\'s the Wi-Fi password?', 'It doesn\'t work.', 'Try resetting it.'], ans=0, why='What\'s the... password? pede a senha.'),
  dict(cue='Você digitou a senha, mas a internet não conecta.', opts=['Let me check.', 'It doesn\'t work.', 'Enjoy the internet!'], ans=1, why='It doesn\'t work avisa que não funciona.'),
  dict(cue='Seu amigo diz que a luz está vermelha. Você sugere uma solução.', opts=['What\'s the password?', 'Turn it off and on again.', 'Thanks for the help.'], ans=1, why='Desligar e ligar é a primeira solução comum.')])
