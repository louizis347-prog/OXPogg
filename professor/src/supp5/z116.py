"""Bloco de verbos e expressões da aula 116: perguntar ao professor."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('repeat', '🔁', 'repetir', ('repeat', 'We repeat the words.', 'Nós repetimos as palavras.'), ('repeats', 'Ms. Lee repeats the sentence.', 'A Ms. Lee repete a frase.'), ('repeated', 'She repeated it slowly.', 'Ela repetiu devagar.'), ('repeating', 'I am repeating the word.', 'Estou repetindo a palavra.'), 'Repeat termina em t; no passado só acrescenta -ed: repeated.'),
  vb('explain', '🗣️', 'explicar', ('explain', 'Teachers explain the lesson.', 'Os professores explicam a lição.'), ('explains', 'She explains the word.', 'Ela explica a palavra.'), ('explained', 'He explained it twice.', 'Ele explicou duas vezes.'), ('explaining', 'She is explaining now.', 'Ela está explicando agora.'), 'Explain something to someone: explain it to me.'),
  vb('answer', '✅', 'responder', ('answer', 'I answer the question.', 'Eu respondo a pergunta.'), ('answers', 'Lia answers in English.', 'A Lia responde em inglês.'), ('answered', 'He answered quickly.', 'Ele respondeu rápido.'), ('answering', 'I am answering number two.', 'Estou respondendo a número dois.'), 'Answer a question: sem “to”. Answer me, não “answer to me”.'),
  vb('listen', '👂', 'escutar', ('listen', 'We listen to the teacher.', 'Nós escutamos a professora.'), ('listens', 'Lia listens carefully.', 'A Lia escuta com atenção.'), ('listened', 'I listened to the story.', 'Eu escutei a história.'), ('listening', 'I am listening now.', 'Estou escutando agora.'), 'Listen to + alguém ou algo. Não esqueça o to.'),
  vb('write', '✍️', 'escrever', ('write', 'I write new words.', 'Eu escrevo palavras novas.'), ('writes', 'Ms. Lee writes on the board.', 'A Ms. Lee escreve no quadro.'), ('wrote', 'She wrote “homework”.', 'Ela escreveu “homework”.'), ('writing', 'I am writing the answer.', 'Estou escrevendo a resposta.'), 'Verbo irregular: write, wrote. O -ing perde o e: writing.')],
 verb_game=[
  dict(scene='A professora explica a palavra todos os dias.', en='Ms. Lee ___ the new word every day.', opts=['explain', 'explains', 'explained'], ans=1, pt='A Ms. Lee explica a palavra nova todo dia.', why='Com “Ms. Lee” (ela), o presente leva -s: explains.'),
  dict(scene='Ontem a Lia escreveu uma palavra no caderno.', en='Yesterday Lia ___ a word in her notebook.', opts=['write', 'writes', 'wrote'], ans=2, pt='Ontem a Lia escreveu uma palavra no caderno.', why='“Yesterday” pede passado: wrote.'),
  dict(scene='Agora você escuta a professora.', en='I am ___ to the teacher.', opts=['listen', 'listens', 'listening'], ans=2, pt='Estou escutando a professora.', why='“am” + verbo termina em -ing: listening.'),
  dict(scene='Vocês repetem a frase juntos.', en='We ___ the sentence together.', opts=['repeat', 'repeats', 'repeated'], ans=0, pt='Nós repetimos a frase juntos.', why='Com “we”, o presente fica na forma base: repeat.')],
 expressions=[
  dict(en='I have a question.', pt='Tenho uma pergunta.', ex='Excuse me, I have a question.', exp='Para chamar a atenção do professor antes de perguntar.', c='a'),
  dict(en='What does … mean?', pt='O que quer dizer…?', ex='What does “lesson” mean?', exp='Para saber o significado de uma palavra.', c='b'),
  dict(en='Can you repeat, please?', pt='Pode repetir, por favor?', ex='Sorry, can you repeat, please?', exp='Quando você não ouviu ou não entendeu.', c='c'),
  dict(en='I see.', pt='Entendi.', ex='Ah, I see. Thank you.', exp='Mostra que você entendeu a explicação.', c='d'),
  dict(en='It gets easier.', pt='Fica mais fácil.', ex='Don’t worry. It gets easier.', exp='Para animar quem está com dificuldade.', c='a'),
  dict(en='I’m lost.', pt='Estou perdido (sem entender).', ex='Sorry, I’m lost. Can you help?', exp='Quando você perdeu o fio da explicação.', c='b')],
 expr_game=[
  dict(cue='Você não ouviu a última frase da professora.', opts=['Can you repeat, please?', 'It gets easier.', 'I see.'], ans=0, why='Can you repeat, please? pede para ouvir de novo.'),
  dict(cue='Você quer saber o significado de “clear”.', opts=['I have a question.', 'What does “clear” mean?', 'I’m lost.'], ans=1, why='What does … mean? pergunta o significado.'),
  dict(cue='Um colega está desanimado com o inglês. Você anima.', opts=['It gets easier.', 'Can you repeat, please?', 'What does it mean?'], ans=0, why='It gets easier é uma frase de apoio.')])
