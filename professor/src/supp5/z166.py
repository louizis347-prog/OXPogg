"""Bloco de verbos e expressões da aula 166: pedir para repetir."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('repeat', '🔁', 'repetir', ('repeat', 'I repeat the number.', 'Eu repito o número.'), ('repeats', 'Mei repeats the price.', 'A Mei repete o preço.'), ('repeated', 'She repeated it slowly.', 'Ela repetiu devagar.'), ('repeating', 'Mei is repeating the total.', 'A Mei está repetindo o total.'), 'Passado regular: repeated.'),
  vb('speak', '🗣️', 'falar', ('speak', 'I speak English a little.', 'Eu falo um pouco de inglês.'), ('speaks', 'Mei speaks fast.', 'A Mei fala rápido.'), ('spoke', 'She spoke slowly.', 'Ela falou devagar.'), ('speaking', 'I am speaking slowly.', 'Estou falando devagar.'), 'Speak é irregular: spoke no passado.'),
  vb('understand', '💡', 'entender', ('understand', 'I understand the price.', 'Eu entendo o preço.'), ('understands', 'Ana understands now.', 'A Ana entende agora.'), ('understood', 'I understood the number.', 'Eu entendi o número.'), ('understanding', 'I am understanding more.', 'Estou entendendo mais.'), 'Irregular: understood. Com sentido de “entender”, o -ing é pouco usado.'),
  vb('hear', '👂', 'ouvir', ('hear', 'I hear the music.', 'Eu ouço a música.'), ('hears', 'Ana hears the cashier.', 'A Ana ouve a caixa.'), ('heard', 'I heard the price.', 'Eu ouvi o preço.'), ('hearing', 'I am hearing a loud noise.', 'Estou ouvindo um barulho alto.'), 'Hear é irregular: heard. Para “não ouvi bem”, diga I can’t hear you.'),
  vb('spell', '🔤', 'soletrar', ('spell', 'I spell my name.', 'Eu soletro meu nome.'), ('spells', 'Mei spells the word.', 'A Mei soletra a palavra.'), ('spelled', 'He spelled it for me.', 'Ele soletrou para mim.'), ('spelling', 'I am spelling the word.', 'Estou soletrando a palavra.'), 'Passado: spelled (EUA).')],
 verb_game=[
  dict(scene='Você não ouviu o preço e pede para a caixa dizer de novo.', en='Could you ___ that?', opts=['repeat', 'repeats', 'repeated'], ans=0, pt='Pode repetir isso?', why='Depois de could you, use o verbo base: repeat.'),
  dict(scene='A Mei fala muito rápido.', en='Mei ___ very fast.', opts=['speak', 'speaks', 'spoke'], ans=1, pt='A Mei fala muito rápido.', why='Ela (3ª pessoa) no presente leva -s: speaks.'),
  dict(scene='Ontem você ouviu o preço errado.', en='Yesterday I ___ the wrong price.', opts=['hear', 'hearing', 'heard'], ans=2, pt='Ontem eu ouvi o preço errado.', why='Yesterday pede passado: heard.'),
  dict(scene='Agora a Mei está falando devagar.', en='Mei is ___ slowly now.', opts=['speaking', 'speak', 'spoke'], ans=0, pt='A Mei está falando devagar agora.', why='Is + -ing: speaking.')],
 expressions=[
  dict(en='Could you repeat that?', pt='Pode repetir?', ex='Sorry, could you repeat that?', exp='Para pedir que repitam o que disseram.', c='a'),
  dict(en='Say that again?', pt='Pode falar de novo?', ex='Say that again? I didn’t hear.', exp='Jeito informal de pedir para repetir.', c='b'),
  dict(en='I didn’t catch that.', pt='Eu não entendi (bem).', ex='Sorry, I didn’t catch that.', exp='Para dizer que não ouviu ou não entendeu direito.', c='c'),
  dict(en='Slow down, please.', pt='Mais devagar, por favor.', ex='Slow down, please.', exp='Para pedir que a pessoa fale mais devagar.', c='d'),
  dict(en='Got it.', pt='Entendi.', ex='Okay, got it. Thanks!', exp='Para dizer que agora você entendeu.', c='a'),
  dict(en='What does it mean?', pt='O que significa?', ex='What does “receipt” mean?', exp='Para perguntar o significado de uma palavra.', c='b')],
 expr_game=[
  dict(cue='Você não ouviu o preço.', opts=['Got it.', 'Could you repeat that?', 'Slow down, please.'], ans=1, why='Could you repeat that? pede que repitam.'),
  dict(cue='Você já entendeu tudo.', opts=['Say that again?', 'What does it mean?', 'Got it.'], ans=2, why='Got it = entendi.'),
  dict(cue='A pessoa fala rápido demais.', opts=['I didn’t catch that.', 'Slow down, please.', 'Got it.'], ans=1, why='Slow down, please pede ritmo mais lento.')])
