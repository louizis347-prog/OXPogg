"""Bloco de verbos e expressões da aula 191: presente para uma amiga."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('wrap', '🎀', 'embrulhar', ('wrap', 'I wrap the gift.', 'Eu embrulho o presente.'), ('wraps', 'Leo wraps the mug.', 'O Leo embrulha a caneca.'), ('wrapped', 'She wrapped the book.', 'Ela embrulhou o livro.'), ('wrapping', 'He is wrapping a box.', 'Ele está embrulhando uma caixa.'), 'Wrap dobra o p antes de -ed e -ing: wrapped, wrapping.'),
  vb('give', '🤲', 'dar', ('give', 'I give her a book.', 'Eu dou um livro a ela.'), ('gives', 'Nora gives Tia a mug.', 'A Nora dá uma caneca à Tia.'), ('gave', 'We gave her tea.', 'Nós demos chá a ela.'), ('giving', 'I am giving her a card.', 'Estou dando um cartão a ela.'), 'Give é irregular: gave no passado. Give + pessoa + coisa.'),
  vb('pick', '👆', 'escolher', ('pick', 'I pick the blue mug.', 'Eu escolho a caneca azul.'), ('picks', 'Nora picks a book.', 'A Nora escolhe um livro.'), ('picked', 'They picked a card.', 'Eles escolheram um cartão.'), ('picking', 'She is picking a gift.', 'Ela está escolhendo um presente.'), 'Pick é mais informal que choose e muito usado em lojas.'),
  vb('spend', '💵', 'gastar', ('spend', 'We spend twenty dollars.', 'Nós gastamos vinte dólares.'), ('spends', 'She spends ten dollars.', 'Ela gasta dez dólares.'), ('spent', 'I spent six dollars.', 'Eu gastei seis dólares.'), ('spending', 'He is spending too much.', 'Ele está gastando demais.'), 'Spend é irregular: spent no passado.'),
  vb('wish', '🌟', 'desejar', ('wish', 'I wish you a happy birthday.', 'Eu te desejo um feliz aniversário.'), ('wishes', 'Leo wishes her luck.', 'O Leo deseja sorte a ela.'), ('wished', 'We wished him well.', 'Nós desejamos o bem a ele.'), ('wishing', 'I am wishing Tia a nice day.', 'Estou desejando um bom dia à Tia.'), 'Wish + pessoa + coisa boa. Com -sh, a 3ª pessoa leva -es: wishes.')],
 verb_game=[
  dict(scene='Ontem a Nora gastou seis dólares.', en='Yesterday Nora ___ six dollars.', opts=['spend', 'spent', 'spending'], ans=1, pt='Ontem a Nora gastou seis dólares.', why='“Yesterday” pede passado irregular: spent.'),
  dict(scene='Agora o Leo está embrulhando o presente.', en='Leo is ___ the gift.', opts=['wrap', 'wraps', 'wrapping'], ans=2, pt='O Leo está embrulhando o presente.', why='“is” + verbo termina em -ing: wrapping.'),
  dict(scene='A Nora costuma dar livros à amiga.', en='Nora ___ books to her friend.', opts=['give', 'gives', 'gave'], ans=1, pt='A Nora dá livros à amiga.', why='Com “Nora” (ela), o presente leva -s: gives.'),
  dict(scene='Nós escolhemos uma caneca azul.', en='We ___ a blue mug.', opts=['pick', 'picks', 'picked'], ans=0, pt='Nós escolhemos uma caneca azul.', why='Com “we”, o presente fica na forma base: pick.')],
 expressions=[
  dict(en='How about…?', pt='Que tal…?', ex='How about a book and a mug?', exp='Para sugerir uma ideia.', c='a'),
  dict(en='It’s for…', pt='É para…', ex='It’s for my best friend.', exp='Para dizer quem vai receber o presente.', c='b'),
  dict(en='What’s your budget?', pt='Qual é seu orçamento?', ex='What’s your budget for the gift?', exp='Pergunta quanto a pessoa quer gastar.', c='c'),
  dict(en='gift wrap', pt='embrulho de presente', ex='Do you have gift wrap?', exp='Para pedir embrulho na loja.', c='d'),
  dict(en='I’ll take it.', pt='Vou levar.', ex='It’s perfect. I’ll take it.', exp='Para decidir a compra.', c='a'),
  dict(en='That’s a great idea.', pt='Ótima ideia.', ex='A mug? That’s a great idea.', exp='Para aceitar uma sugestão com simpatia.', c='b')],
 expr_game=[
  dict(cue='Você aceita a sugestão do atendente.', opts=['How about a mug?', 'That’s a great idea.', 'What’s your budget?'], ans=1, why='That’s a great idea aceita uma sugestão.'),
  dict(cue='Você quer pedir embrulho.', opts=['Do you have gift wrap?', 'I’ll take it.', 'It’s for my friend.'], ans=0, why='Gift wrap é o embrulho de presente.'),
  dict(cue='Você decidiu comprar o livro.', opts=['I’ll take it.', 'How about a book?', 'What’s your budget?'], ans=0, why='I’ll take it fecha a compra.')])
