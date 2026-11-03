"""Bloco de verbos e expressões da aula 8."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('bake', '🍰', 'assar', ('bake', 'We bake a cake for Mom.', 'Nós assamos um bolo para a mamãe.'), ('bakes', 'Grandma bakes bread.', 'A vovó assa pão.'), ('baked', 'I baked cookies with my sister.', 'Eu assei biscoitos com minha irmã.'), ('baking', 'Dad is baking a pie.', 'O papai está assando uma torta.'), 'Bake = assar no forno; passado só com -d: baked.'),
  vb('chat', '💬', 'conversar', ('chat', 'I chat with my cousins.', 'Eu converso com meus primos.'), ('chats', 'Mom chats with Aunt Lu.', 'A mamãe conversa com a tia Lu.'), ('chatted', 'We chatted all night.', 'Nós conversamos a noite toda.'), ('chatting', 'I am chatting with Grandpa.', 'Estou conversando com o vovô.'), 'Chat with alguém; passado dobra o t: chatted.'),
  vb('visit', '🚪', 'visitar', ('visit', 'We visit my grandma.', 'Nós visitamos minha avó.'), ('visits', 'Paulo visits his brother.', 'O Paulo visita o irmão.'), ('visited', 'I visited my family.', 'Eu visitei minha família.'), ('visiting', 'I am visiting my sister.', 'Estou visitando minha irmã.'), 'Visit não leva “to”: visit my family.'),
  vb('cook', '🍲', 'cozinhar', ('cook', 'I cook with my mother.', 'Eu cozinho com minha mãe.'), ('cooks', 'My father cooks on Sunday.', 'Meu pai cozinha no domingo.'), ('cooked', 'She cooked dinner.', 'Ela fez o jantar.'), ('cooking', 'Grandma is cooking now.', 'A vovó está cozinhando agora.'), 'Passado só com -ed: cooked.'),
  vb('come', '🍽️', 'vir', ('come', 'Come to dinner!', 'Venha jantar!'), ('comes', 'My brother comes on Sunday.', 'Meu irmão vem no domingo.'), ('came', 'They came last night.', 'Eles vieram ontem à noite.'), ('coming', 'My sister is coming too.', 'Minha irmã também está vindo.'), 'Irregular: come vira came.')],
 verb_game=[
  dict(scene='Sua família assa um bolo.', en='We ___ a cake for Mom.', opts=['bake', 'bakes', 'baked'], ans=0, pt='Nós assamos um bolo para a mamãe.', why='Com “we” o presente fica na forma base: bake.'),
  dict(scene='A vovó assa pão aos domingos.', en='Grandma ___ bread on Sundays.', opts=['bake', 'bakes', 'baking'], ans=1, pt='A vovó assa pão aos domingos.', why='Com “Grandma” (ela) o presente leva -s: bakes.'),
  dict(scene='Sua mãe conversa com a tia agora.', en='Mom is ___ with Aunt Lu.', opts=['chat', 'chats', 'chatting'], ans=2, pt='A mamãe está conversando com a tia Lu.', why='“is” + verbo termina em -ing: chatting.'),
  dict(scene='Ontem sua família veio jantar.', en='My family ___ to dinner yesterday.', opts=['came', 'come', 'comes'], ans=0, pt='Minha família veio jantar ontem.', why='“Yesterday” pede passado irregular: came.')],
 expressions=[
  dict(en='This is my…', pt='Este(a) é meu(minha)…', ex='This is my mother.', exp='Para apresentar alguém da família.', c='a'),
  dict(en='Do you have…?', pt='Você tem…?', ex='Do you have sisters?', exp='Para perguntar sobre a família.', c='b'),
  dict(en='His name is…', pt='O nome dele é…', ex='His name is Leo.', exp='Para dizer o nome de um homem.', c='c'),
  dict(en='Her name is…', pt='O nome dela é…', ex='Her name is Ana.', exp='Para dizer o nome de uma mulher.', c='d'),
  dict(en='Come to dinner!', pt='Venha jantar!', ex='Come to dinner on Sunday!', exp='Para convidar alguém.', c='a'),
  dict(en='What a nice family!', pt='Que família legal!', ex='Wow, what a nice family!', exp='Para elogiar a família.', c='b')],
 expr_game=[
  dict(cue='Você apresenta sua mãe a um amigo.', opts=['This is my mother.', 'Do you have sisters?', 'His name is Leo.'], ans=0, why='This is my… apresenta uma pessoa.'),
  dict(cue='Você quer saber se ele tem irmãs.', opts=['This is my sister.', 'Do you have sisters?', 'Come to dinner!'], ans=1, why='Do you have…? pergunta se a pessoa tem algo.'),
  dict(cue='Você quer convidar o vizinho para jantar.', opts=['Come to dinner on Sunday!', 'Her name is Ana.', 'What a nice family!'], ans=0, why='Come to dinner! é um convite.')])
