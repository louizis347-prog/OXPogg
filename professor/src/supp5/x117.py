X = dict(
 key=dict(big="Can you help me?", label="Pedir ajuda com a lição", sub="Peça ajuda com o dever de casa, diga o que não entende e confira se a resposta está certa."),
 mini=[
  dict(who="You", en="Can you help me with my {homework|math|reading}?", pt="Pode me ajudar com {a lição|a matemática|a leitura}?"),
  dict(who="Bethany", en="Sure. What is it?", pt="Claro. O que é?"),
  dict(who="You", en="I don't understand number {five|six|ten}.", pt="Não entendo a número {cinco|seis|dez}."),
  dict(who="Bethany", en="Let's {read|do|check} it together.", pt="Vamos {ler|fazer|conferir} juntos."),
 ],
 dlg=[
  dict(who="Bethany", en="Hi, Mom. Can you {help me|check} with my homework?", pt="Oi, mãe. Pode {me ajudar|conferir} com a lição?"),
  dict(who="You", en="Sure. What is it?", pt="Claro. O que é?"),
  dict(who="Bethany", en="It's {math.|reading.|science.} I don't understand number five.", pt="É {matemática.|leitura.|ciências.} Não entendo a número cinco."),
  dict(who="You", en="Let's {read|do} it together.", pt="Vamos {ler|fazer} juntos."),
  dict(who="Bethany", en="What is seven {plus|minus} eight?", pt="Quanto é sete {mais|menos} oito?"),
  dict(who="You", en="It's {fifteen.|fifty.}", pt="São {quinze.|cinquenta.}"),
  dict(who="Bethany", en="Right! Now write the {answer.|number.}", pt="Certo! Agora escreva {a resposta.|o número.}"),
  dict(who="You", en="I wrote it. Is it {correct?|right?}", pt="Escrevi. Está {certo?|certo?}"),
  dict(who="Bethany", en="Yes, great {job!|work!}", pt="Sim, ótimo {trabalho!|trabalho!}"),
 ],
 vocab=[
  dict(w="plus", pt="mais", e="➕", ex=["Two plus two is four.", "Seven plus eight is fifteen."]),
  dict(w="minus", pt="menos", e="➖", ex=["Ten minus three is seven.", "Nine minus five is four."]),
  dict(w="equals", pt="é igual a", e="🟰", ex=["Two plus two equals four.", "Five minus one equals four."]),
  dict(w="correct", pt="certo, correto", e="✔️", ex=["Is my answer correct?", "Yes, it is correct."]),
  dict(w="half", pt="metade", e="➗", ex=["Half of ten is five.", "I have half of the page."]),
  dict(w="fifteen", pt="quinze", e="1️⃣5️⃣", ex=["I am fifteen.", "It's fifteen dollars."]),
 ],
 molds=[
  dict(title="Ler uma conta", frame="What is {a} {op} {b}?", slots=[dict(key="a", opts=["seven", "nine", "twelve"]), dict(key="op", opts=["plus", "minus", "times"]), dict(key="b", opts=["two", "three", "four"])], model="What is seven plus two?", note="Plus = +, minus = −, times = ×. Resposta: It's nine."),
  dict(title="Pedir ajuda", frame="Can you help me with my {subject} homework?", slots=[dict(key="subject", opts=["math", "English", "science", "reading"])], model="Can you help me with my math homework?", note="Help me WITH. Não diga 'help me in'."),
  dict(title="Escrever o pedido", frame="Hi, {person}. I don't understand number {n}. Can you help me, please?", slots=[dict(key="person", opts=["Mom", "Dad", "Anna", "teacher"]), dict(key="n", opts=["five", "six", "eight"])], model="Hi, Mom. I don't understand number five. Can you help me, please?", note="I don't understand = Não entendo. Termine com please."),
 ],
 sounds=[
  dict(say="It's fifteen.", tag="acento: fifTEEN", tip="Em -teen a força vai para o final: fifTEEN. Alongue o 'ee'."),
  dict(say="It's fifty.", tag="acento: FIFty", tip="Em -ty a força vai para o começo: FIFty. O final é curto, quase 'di'."),
  dict(say="Seven plus eight.", tag="ligação: plus eight", tip="Plus e eight se unem: 'plu-seit'. O s liga na vogal seguinte."),
 ],
 role=dict(turns=[
  dict(npc="Hi! You look worried.", opts=[
   dict(en="Hi, Mom. Can you help me with my homework?", pt="Oi, mãe. Pode me ajudar com a lição?", reply="Sure. What is it?"),
   dict(en="Hi, Dad. I need help with my homework.", pt="Oi, pai. Preciso de ajuda com a lição.", reply="Sure. What is it?"),
   dict(en="Hi! Can you help me, please?", pt="Oi! Pode me ajudar, por favor?", reply="Sure. What is it?")]),
  dict(npc="Sure. What is it?", opts=[
   dict(en="It's math. I don't understand number five.", pt="É matemática. Não entendo a número cinco.", reply="Let's read it together."),
   dict(en="It's science. I don't understand page ten.", pt="É ciências. Não entendo a página dez.", reply="Let's read it together."),
   dict(en="It's math. Number six is hard.", pt="É matemática. A número seis é difícil.", reply="Let's read it together.")]),
  dict(npc="What is seven plus eight?", opts=[
   dict(en="It's fifteen.", pt="São quinze.", reply="Right! Now write the answer."),
   dict(en="Fifteen, I think.", pt="Quinze, acho.", reply="Right! Now write the answer."),
   dict(en="Is it fifteen?", pt="São quinze?", reply="Right! Now write the answer.")]),
  dict(npc="Now write the answer.", opts=[
   dict(en="I wrote it. Is it correct?", pt="Escrevi. Está certo?", reply="Yes, great job!"),
   dict(en="Done! Is it right?", pt="Pronto! Está certo?", reply="Yes, great job!"),
   dict(en="I wrote it. Can you check?", pt="Escrevi. Pode conferir?", reply="Yes, great job!")]),
 ], change=["A resposta está errada: peça para a pessoa explicar de novo.", "Você não entende uma palavra do exercício: pergunte o que ela significa.", "Terminaram a lição: agradeça e diga que vai tocar violão."]),
 writing=dict(task="Escreva uma mensagem curta para um familiar: peça ajuda com a lição de matemática e diga qual número você não entende.", model="Hi, Mom. Can you help me with my math homework? I don't understand number five.", kw=["help", "homework", "math", "understand"], checks=["Pediu ajuda com a lição.", "Disse que a lição é matemática.", "Disse o que não entende."]),
 scenes=dict(pool=["living", "kitchen", "home1", "bedroom", "library"], npc=dict(g="f", role="mother"), you=dict(g="m")),
 convo=dict(npc=dict(name="Mom"), story="Você tem lição de matemática difícil e pede ajuda para sua mãe.", turns=[
  dict(npc="You look worried. What's wrong?", pt="Você parece preocupado. O que foi?", opts=[
   dict(en="Hi, Mom. Can you help me with my homework?", pt="Oi, mãe. Pode me ajudar com a lição?", ok=True, fb="Pede ajuda de forma natural."),
   dict(en="Sure. What is it?", pt="Claro. O que é?", ok=False, fb="Quem diz isso é quem vai ajudar."),
   dict(en="Yes, great job!", pt="Sim, ótimo trabalho!", ok=False, fb="É um elogio, e ainda não há o que elogiar.")]),
  dict(npc="Sure. What is it?", pt="Claro. O que é?", opts=[
   dict(en="Let's read it together.", pt="Vamos ler juntos.", ok=False, fb="Quem sugere isso é quem ajuda."),
   dict(en="It's math. I don't understand number five.", pt="É matemática. Não entendo a número cinco.", ok=True, fb="Diz a matéria e o que não entende."),
   dict(en="Can you help me with my homework?", pt="Pode me ajudar com a lição?", ok=False, fb="Você já pediu e ela já aceitou.")]),
  dict(npc="Let's read it together. What is seven plus eight?", pt="Vamos ler juntos. Quanto é sete mais oito?", opts=[
   dict(en="I don't understand.", pt="Não entendo.", ok=False, fb="É uma conta fácil: responda."),
   dict(en="It's fifteen.", pt="São quinze.", ok=True, fb="Responde a conta."),
   dict(en="Can I use a calculator?", pt="Posso usar uma calculadora?", ok=False, fb="Ela fez uma pergunta de matemática; responda.")]),
  dict(npc="Right! Now write the answer.", pt="Certo! Agora escreva a resposta.", opts=[
   dict(en="What is seven plus eight?", pt="Quanto é sete mais oito?", ok=False, fb="Já foi respondido."),
   dict(en="Yes, great job!", pt="Sim, ótimo trabalho!", ok=False, fb="Esse elogio vem dela, não de você."),
   dict(en="I wrote it. Is it correct?", pt="Escrevi. Está certo?", ok=True, fb="Mostra que escreveu e pede confirmação.")]),
  dict(npc="Yes, great job!", pt="Sim, ótimo trabalho!", opts=[
   dict(en="Thanks, Mom! I get it now.", pt="Valeu, mãe! Agora entendi.", ok=True, fb="Agradece e mostra que aprendeu."),
   dict(en="I wrote it. Is it correct?", pt="Escrevi. Está certo?", ok=False, fb="Ela acabou de confirmar."),
   dict(en="Please write the answer.", pt="Por favor, escreva a resposta.", ok=False, fb="Você já escreveu.")]),
 ]),
)
