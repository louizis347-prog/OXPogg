"""Bloco de verbos e expressões da aula 167: elogios."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('thank', '🙏', 'agradecer', ('thank', 'I thank Omar.', 'Eu agradeço ao Omar.'), ('thanks', 'Cleo thanks Omar.', 'A Cleo agradece ao Omar.'), ('thanked', 'I thanked her.', 'Eu agradeci a ela.'), ('thanking', 'I am thanking my friend.', 'Estou agradecendo ao meu amigo.'), 'No dia a dia, diga Thank you! ou Thanks!.'),
  vb('smile', '😊', 'sorrir', ('smile', 'I smile at my friend.', 'Eu sorrio para meu amigo.'), ('smiles', 'Cleo smiles at Omar.', 'A Cleo sorri para o Omar.'), ('smiled', 'He smiled and said thanks.', 'Ele sorriu e disse obrigado.'), ('smiling', 'She is smiling now.', 'Ela está sorrindo agora.'), 'Smile at = sorrir para.'),
  vb('wear', '🧥', 'vestir, usar (roupa)', ('wear', 'I wear a blue jacket.', 'Eu uso uma jaqueta azul.'), ('wears', 'Cleo wears a new jacket.', 'A Cleo usa uma jaqueta nova.'), ('wore', 'I wore it yesterday.', 'Eu usei ontem.'), ('wearing', 'She is wearing a blue jacket.', 'Ela está usando uma jaqueta azul.'), 'Wear é irregular: wore. Usado para roupas, sapatos e óculos.'),
  vb('shop', '🛍️', 'fazer compras', ('shop', 'I shop at the mall.', 'Eu faço compras no shopping.'), ('shops', 'Omar shops downtown.', 'O Omar faz compras no centro.'), ('shopped', 'We shopped on Saturday.', 'Nós fizemos compras no sábado.'), ('shopping', 'We are shopping at the mall.', 'Estamos fazendo compras no shopping.'), 'Dobra o p: shopped, shopping.'),
  vb('wrap', '🎀', 'embrulhar', ('wrap', 'I wrap the gift.', 'Eu embrulho o presente.'), ('wraps', 'Omar wraps the bag.', 'O Omar embrulha a bolsa.'), ('wrapped', 'She wrapped a gift.', 'Ela embrulhou um presente.'), ('wrapping', 'I am wrapping a gift.', 'Estou embrulhando um presente.'), 'Dobra o p: wrapped, wrapping.')],
 verb_game=[
  dict(scene='Cleo está com a jaqueta azul agora.', en='Cleo is ___ a blue jacket.', opts=['wear', 'wearing', 'wore'], ans=1, pt='A Cleo está usando uma jaqueta azul.', why='Is + -ing: wearing.'),
  dict(scene='Omar elogia e Cleo sorri.', en='Cleo ___ and says thank you.', opts=['smile', 'smiles', 'smiling'], ans=1, pt='A Cleo sorri e diz obrigada.', why='Ela (3ª pessoa) leva -s: smiles.'),
  dict(scene='Ontem você fez compras no shopping.', en='Yesterday I ___ at the mall.', opts=['shop', 'shopping', 'shopped'], ans=2, pt='Ontem eu fiz compras no shopping.', why='Yesterday pede passado: shopped.'),
  dict(scene='Você quer agradecer ao Omar.', en='I want to ___ Omar.', opts=['thank', 'thanks', 'thanked'], ans=0, pt='Quero agradecer ao Omar.', why='Depois de to, verbo base: thank.')],
 expressions=[
  dict(en='I like your jacket.', pt='Gosto da sua jaqueta.', ex='Hey! I like your jacket.', exp='Para elogiar uma peça de roupa.', c='a'),
  dict(en='It looks great on you.', pt='Fica ótimo em você.', ex='The color looks great on you.', exp='Para dizer que uma roupa combina com a pessoa.', c='b'),
  dict(en='Where did you get it?', pt='Onde você comprou?', ex='Nice bag! Where did you get it?', exp='Para perguntar onde a pessoa comprou algo.', c='c'),
  dict(en='You’re so kind.', pt='Você é muito gentil.', ex='Thank you, you’re so kind.', exp='Para agradecer um elogio.', c='d'),
  dict(en='That’s so sweet.', pt='Que gentil, que fofo.', ex='Aw, that’s so sweet.', exp='Para reagir a uma gentileza.', c='a'),
  dict(en='It was a gift.', pt='Foi presente.', ex='Thanks! It was a gift.', exp='Para dizer como você ganhou algo.', c='b')],
 expr_game=[
  dict(cue='Você gostou da bolsa do seu amigo.', opts=['It was a gift.', 'I like your bag.', 'You’re so kind.'], ans=1, why='I like your… elogia algo.'),
  dict(cue='Você quer saber onde ele comprou a camisa.', opts=['Where did you get it?', 'That’s so sweet.', 'It looks great on you.'], ans=0, why='Where did you get it? pergunta onde comprou.'),
  dict(cue='Alguém foi gentil com você.', opts=['Where did you get it?', 'It was a gift.', 'That’s so sweet.'], ans=2, why='That’s so sweet reage a uma gentileza.')])
