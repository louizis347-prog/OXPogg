"""Bloco de verbos e expressões da aula 4."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('spell', '🔤', 'soletrar', ('spell', 'I spell my name slowly.', 'Eu soletro meu nome devagar.'), ('spells', 'Sofia spells her last name.', 'A Sofia soletra o sobrenome.'), ('spelled', 'He spelled it for me.', 'Ele soletrou para mim.'), ('spelling', 'I am spelling it now.', 'Estou soletrando agora.'), 'How do you spell that? é a pergunta-chave. Passado: spelled.'),
  vb('say', '💬', 'dizer', ('say', 'I say my name twice.', 'Eu digo meu nome duas vezes.'), ('says', 'Lucas says his number.', 'O Lucas diz o número dele.'), ('said', 'She said, “Daniel.”', 'Ela disse: “Daniel.”'), ('saying', 'I am saying it again.', 'Estou dizendo de novo.'), 'Irregular: say vira said (pronuncia-se “sed”).'),
  vb('write', '✍️', 'escrever', ('write', 'I write my name here.', 'Eu escrevo meu nome aqui.'), ('writes', 'She writes the number.', 'Ela escreve o número.'), ('wrote', 'He wrote his last name.', 'Ele escreveu o sobrenome.'), ('writing', 'I am writing it down.', 'Estou anotando.'), 'Irregular: write vira wrote. Write down = anotar.'),
  vb('call', '📞', 'chamar / ligar', ('call', 'People call me Dan.', 'As pessoas me chamam de Dan.'), ('calls', 'Sofia calls her mother.', 'A Sofia liga para a mãe.'), ('called', 'He called yesterday.', 'Ele ligou ontem.'), ('calling', 'I am calling you back.', 'Estou retornando a ligação.'), 'Call = chamar de (um nome) ou ligar para alguém.'),
  vb('give', '🎁', 'dar', ('give', 'I give my phone number.', 'Eu dou meu número de telefone.'), ('gives', 'Lucas gives his name.', 'O Lucas diz o nome dele.'), ('gave', 'She gave me a pen.', 'Ela me deu uma caneta.'), ('giving', 'I am giving my number.', 'Estou dando meu número.'), 'Irregular: give vira gave. Give me… = me dê…')],
 verb_game=[
  dict(scene='O atendente pede a grafia do seu nome.', en='How do you ___ your name?', opts=['spell', 'spells', 'spelled'], ans=0, pt='Como você soletra seu nome?', why='Depois de “do you” o verbo fica na forma base: spell.'),
  dict(scene='A Sofia soletra o sobrenome dela.', en='Sofia ___ her last name.', opts=['spell', 'spells', 'spelling'], ans=1, pt='A Sofia soletra o sobrenome dela.', why='Com “Sofia” (ela) o presente leva -s: spells.'),
  dict(scene='Ontem ele disse o nome dele.', en='Yesterday he ___ his name.', opts=['says', 'saying', 'said'], ans=2, pt='Ontem ele disse o nome dele.', why='“Yesterday” pede passado irregular: said.'),
  dict(scene='Agora você está anotando o número.', en='I am ___ the number down.', opts=['write', 'wrote', 'writing'], ans=2, pt='Estou anotando o número.', why='“am” + verbo termina em -ing: writing.')],
 expressions=[
  dict(en='How do you spell that?', pt='Como se soletra isso?', ex='How do you spell that?', exp='Para pedir a grafia de um nome.', c='a'),
  dict(en='Can I have your name?', pt='Posso saber seu nome?', ex='Can I have your name, please?', exp='Para pedir o nome de alguém com educação.', c='b'),
  dict(en='Can you repeat that?', pt='Pode repetir?', ex='Sorry, can you repeat that?', exp='Quando você não entendeu bem.', c='c'),
  dict(en='It’s D-A-N-I-E-L.', pt='É D-A-N-I-E-L.', ex='It’s D-A-N-I-E-L.', exp='Para dar a grafia, letra por letra.', c='d'),
  dict(en='write down', pt='anotar', ex='I write down your number.', exp='Verbo frasal: registrar no papel.', c='a'),
  dict(en='That’s right.', pt='Isso mesmo.', ex='Yes, that’s right.', exp='Para confirmar que a informação está correta.', c='b')],
 expr_game=[
  dict(cue='Você quer saber como se escreve o nome da pessoa.', opts=['How do you spell that?', 'That’s right.', 'Have a good day!'], ans=0, why='How do you spell…? pede a grafia.'),
  dict(cue='Você não ouviu direito e quer que repitam.', opts=['Can you repeat that?', 'It’s five five five.', 'That’s right.'], ans=0, why='Can you repeat that? pede para repetir.'),
  dict(cue='O atendente repetiu seu número certo e você confirma.', opts=['Sorry, what?', 'Yes, that’s right.', 'How do you spell that?'], ans=1, why='That’s right confirma que está correto.')])
