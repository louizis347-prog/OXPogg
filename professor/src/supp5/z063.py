"""Bloco de verbos e expressões da aula 063: visita ao apartamento."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('look', '👀', 'olhar / parecer', ('look', 'I look at the kitchen.', 'Eu olho a cozinha.'), ('looks', 'It looks nice.', 'Parece bonito.'), ('looked', 'We looked at the bedroom.', 'Nós olhamos o quarto.'), ('looking', 'I am looking for a flat.', 'Estou procurando um apartamento.'), 'Look at = olhar; look for = procurar; looks nice = parece bonito.'),
  vb('live', '🏠', 'morar', ('live', 'I live in Phoenix.', 'Eu moro em Phoenix.'), ('lives', 'Kai lives next door.', 'O Kai mora ao lado.'), ('lived', 'We lived there a year.', 'Nós moramos lá um ano.'), ('living', 'I am living with a friend.', 'Estou morando com um amigo.'), 'Live: o i é curto (/lɪv/). Passado regular: lived.'),
  vb('move', '📦', 'mudar-se', ('move', 'We move on Monday.', 'Nós nos mudamos na segunda.'), ('moves', 'Ruth moves to a new flat.', 'A Ruth se muda para um novo apartamento.'), ('moved', 'I moved last week.', 'Eu me mudei semana passada.'), ('moving', 'I am moving next month.', 'Vou me mudar mês que vem.'), 'Move perde o e antes de -ed e -ing: moved, moving.'),
  vb('open', '🚪', 'abrir', ('open', 'I open the window.', 'Eu abro a janela.'), ('opens', 'Kai opens the door.', 'O Kai abre a porta.'), ('opened', 'She opened the closet.', 'Ela abriu o armário.'), ('opening', 'He is opening the window.', 'Ele está abrindo a janela.'), 'Passado regular: opened.'),
  vb('clean', '🧽', 'limpar', ('clean', 'I clean the kitchen.', 'Eu limpo a cozinha.'), ('cleans', 'Kai cleans the stove.', 'O Kai limpa o fogão.'), ('cleaned', 'We cleaned the bedroom.', 'Nós limpamos o quarto.'), ('cleaning', 'I am cleaning the window.', 'Estou limpando a janela.'), 'Clean também é adjetivo: a clean kitchen.')],
 verb_game=[
  dict(scene='Você procura um apartamento agora.', en='I am ___ for an apartment.', opts=['look', 'looks', 'looking'], ans=2, pt='Estou procurando um apartamento.', why='“am” + -ing: looking.'),
  dict(scene='O Kai abre a porta.', en='Kai ___ the door.', opts=['open', 'opens', 'opened'], ans=1, pt='O Kai abre a porta.', why='Ele (3ª pessoa) leva -s: opens.'),
  dict(scene='Semana passada você se mudou.', en='Last week I ___ to a new place.', opts=['move', 'moves', 'moved'], ans=2, pt='Semana passada eu me mudei para um novo lugar.', why='“Last week” pede passado: moved.'),
  dict(scene='Você mora em Phoenix.', en='I ___ in Phoenix.', opts=['live', 'lives', 'lived'], ans=0, pt='Eu moro em Phoenix.', why='Com I, presente sem -s: live.')],
 expressions=[
  dict(en='Let me show you the apartment.', pt='Deixe-me mostrar o apartamento.', ex='Welcome! Let me show you the apartment.', exp='Frase do corretor ao começar a visita.', c='a'),
  dict(en='It looks nice.', pt='Parece bonito.', ex='Thanks. It looks nice.', exp='Para elogiar um lugar.', c='b'),
  dict(en='Is there a kitchen?', pt='Tem cozinha?', ex='I like it. Is there a kitchen?', exp='Para perguntar se existe um cômodo.', c='c'),
  dict(en='down the hall', pt='no corredor', ex='It is down the hall.', exp='Para dizer que algo fica ao longo do corredor.', c='d'),
  dict(en='next to', pt='ao lado de', ex='It is next to the bathroom.', exp='Para dizer a posição de algo.', c='a'),
  dict(en='It’s yours!', pt='É seu!', ex='Come back anytime. It’s yours!', exp='Para dizer que o lugar pode ser da pessoa.', c='b')],
 expr_game=[
  dict(cue='Você quer saber se a casa tem cozinha.', opts=['Is there a kitchen?', 'It’s yours!', 'next to'], ans=0, why='Is there a...? pergunta se algo existe.'),
  dict(cue='Você quer dizer que o quarto fica ao lado do banheiro.', opts=['It is next to the bathroom.', 'It looks nice.', 'It’s yours!'], ans=0, why='Next to = ao lado de.'),
  dict(cue='Você quer elogiar o apartamento.', opts=['It looks nice.', 'Is there a kitchen?', 'down the hall'], ans=0, why='It looks nice. elogia o que você vê.')])
