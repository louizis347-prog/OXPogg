"""Bloco de verbos e expressões da aula 6."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('say', '💬', 'dizer', ('say', 'I say hello to Ben.', 'Eu digo oi para o Ben.'), ('says', 'Ben says good morning.', 'O Ben diz bom dia.'), ('said', 'She said goodbye.', 'Ela disse tchau.'), ('saying', 'I am saying good night.', 'Estou dizendo boa noite.'), 'Irregular: say vira said (pronuncia-se “sed”).'),
  vb('see', '👀', 'ver', ('see', 'I see Ben every day.', 'Eu vejo o Ben todo dia.'), ('sees', 'She sees him on Monday.', 'Ela o vê na segunda.'), ('saw', 'I saw you yesterday.', 'Eu vi você ontem.'), ('seeing', 'I am seeing him tomorrow.', 'Vou ver ele amanhã.'), 'See you later! usa a forma base. Passado: saw.'),
  vb('have', '🌞', 'ter / passar', ('have', 'I have a great day.', 'Eu tenho um ótimo dia.'), ('has', 'Ben has a busy morning.', 'O Ben tem uma manhã corrida.'), ('had', 'We had a nice evening.', 'Nós tivemos uma noite agradável.'), ('having', 'I am having a good day.', 'Estou tendo um bom dia.'), 'Have a nice day! Com ele/ela, has; passado: had.'),
  vb('go', '🚶', 'ir', ('go', 'I go home now.', 'Eu vou para casa agora.'), ('goes', 'Ben goes to work.', 'O Ben vai trabalhar.'), ('went', 'We went home early.', 'Nós fomos para casa cedo.'), ('going', 'I am going home.', 'Estou indo para casa.'), 'Irregular: go vira went. Com ele/ela, goes.'),
  vb('feel', '🙂', 'sentir-se', ('feel', 'I feel great today.', 'Eu me sinto ótimo hoje.'), ('feels', 'Ben feels tired.', 'O Ben se sente cansado.'), ('felt', 'I felt good yesterday.', 'Eu me senti bem ontem.'), ('feeling', 'I am feeling fine.', 'Estou me sentindo bem.'), 'Irregular: feel vira felt. I feel fine = eu estou bem.')],
 verb_game=[
  dict(scene='Você deseja um bom dia ao vizinho.', en='___ a nice day!', opts=['Have', 'Has', 'Had'], ans=0, pt='Tenha um bom dia!', why='No pedido/desejo usa-se a forma base: Have.'),
  dict(scene='O Ben vai para o trabalho.', en='Ben ___ to work at eight.', opts=['go', 'goes', 'went'], ans=1, pt='O Ben vai trabalhar às oito.', why='Com “Ben” (ele) o presente é goes.'),
  dict(scene='Ontem você viu o Ben.', en='I ___ Ben yesterday.', opts=['see', 'sees', 'saw'], ans=2, pt='Eu vi o Ben ontem.', why='“Yesterday” pede passado irregular: saw.'),
  dict(scene='Agora você se sente bem.', en='I am ___ great today.', opts=['feeling', 'feel', 'felt'], ans=0, pt='Estou me sentindo ótimo hoje.', why='“am” + verbo termina em -ing: feeling.')],
 expressions=[
  dict(en='How are you?', pt='Como vai você?', ex='Good morning! How are you?', exp='Cumprimento comum ao encontrar alguém.', c='a'),
  dict(en='I’m fine, thanks.', pt='Estou bem, obrigado.', ex='I’m fine, thanks. And you?', exp='Resposta curta e educada.', c='b'),
  dict(en='Have a nice day!', pt='Tenha um bom dia!', ex='Bye! Have a nice day!', exp='Despedida simpática de dia.', c='c'),
  dict(en='See you later!', pt='Até mais tarde!', ex='See you later, Ben!', exp='Quando você vai ver a pessoa de novo.', c='d'),
  dict(en='Take care.', pt='Se cuide.', ex='Bye, Ben. Take care.', exp='Despedida carinhosa.', c='a'),
  dict(en='Good night!', pt='Boa noite!', ex='Good night, Ben!', exp='Despedida à noite ou antes de dormir.', c='b')],
 expr_game=[
  dict(cue='Você encontra o Ben de manhã e quer cumprimentar.', opts=['Good morning! How are you?', 'Good night!', 'See you later!'], ans=0, why='Good morning é o cumprimento da manhã.'),
  dict(cue='Você vai dormir e quer se despedir.', opts=['Good morning!', 'Good night!', 'How are you?'], ans=1, why='Good night é a despedida da noite.'),
  dict(cue='Alguém pergunta como você está e você está bem.', opts=['I’m fine, thanks.', 'Have a nice day!', 'Take care.'], ans=0, why='I’m fine, thanks responde à pergunta.')])
