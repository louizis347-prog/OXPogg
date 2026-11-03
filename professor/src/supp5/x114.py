X = dict(
 key=dict(big="Want to join us?", label="Entrar em um grupo de estudos", sub="Aceite o convite, pergunte quando e onde o grupo se encontra, o que estuda e o que levar."),
 mini=[
  dict(who="Jordan", en="Hey, want to join our {study group?|book club?|running club?}", pt="Ei, quer entrar no nosso {grupo de estudos?|clube do livro?|grupo de corrida?}"),
  dict(who="You", en="Yes! When do you {meet?|study?|start?}", pt="Quero! Quando vocês {se encontram?|estudam?|começam?}"),
  dict(who="Jordan", en="Every {Tuesday|Monday|Friday} at five.", pt="Toda {terça|segunda|sexta} às cinco."),
  dict(who="You", en="Great. Where do you {meet?|study?|sit?}", pt="Ótimo. Onde vocês {se encontram?|estudam?|sentam?}"),
 ],
 dlg=[
  dict(who="Jordan", en="Hey, want to {join|see} our study group?", pt="Ei, quer {entrar no|conhecer o} nosso grupo de estudos?"),
  dict(who="You", en="Yes! When do you {meet?|study?}", pt="Quero! Quando vocês {se encontram?|estudam?}"),
  dict(who="Jordan", en="Every {Tuesday|Thursday} at {five.|six.}", pt="Toda {terça|quinta} às {cinco.|seis.}"),
  dict(who="You", en="Where?", pt="Onde?"),
  dict(who="Jordan", en="In the library, {room three.|room four.}", pt="Na biblioteca, {sala três.|sala quatro.}"),
  dict(who="You", en="Great. What do you {study?|read?}", pt="Ótimo. O que vocês {estudam?|leem?}"),
  dict(who="Jordan", en="English {grammar|words} and vocabulary.", pt="{Gramática|Palavras} e vocabulário de inglês."),
  dict(who="You", en="Perfect. I need {practice.|help.}", pt="Perfeito. Preciso de {prática.|ajuda.}"),
  dict(who="Jordan", en="Bring your {notebook|book} and a {pen.|pencil.}", pt="Traga seu {caderno|livro} e uma {caneta.|lápis.}"),
 ],
 vocab=[
  dict(w="grammar", pt="gramática", e="🔡", ex=["Grammar is not hard.", "I study grammar today."]),
  dict(w="vocabulary", pt="vocabulário", e="📖", ex=["I learn new vocabulary.", "Your vocabulary is good."]),
  dict(w="quiz", pt="teste rápido", e="❓", ex=["We have a quiz today.", "Let's quiz each other."]),
  dict(w="exam", pt="prova", e="📝", ex=["The exam is on Friday.", "I study for the exam."]),
  dict(w="flashcard", pt="cartão de estudo", e="🗂️", ex=["I make a flashcard.", "Flashcards help me."]),
  dict(w="notes", pt="anotações", e="🗒️", ex=["I take notes in class.", "Can I see your notes?"]),
 ],
 molds=[
  dict(title="Convidar alguém", frame="Hey, want to join our {group}?", slots=[dict(key="group", opts=["study group", "book club", "soccer team", "walking group"])], model="Hey, want to join our study group?", note="Want to join…? é um convite informal. Our = nosso(a)."),
  dict(title="Dizer quando e onde", frame="We meet every {day} at {time}, in {place}.", slots=[dict(key="day", opts=["Tuesday", "Monday", "Friday"]), dict(key="time", opts=["five", "six", "seven"]), dict(key="place", opts=["the library", "room three", "the cafe"])], model="We meet every Tuesday at five, in the library.", note="Every + dia = todo(a). Use at com horas e in com lugares."),
  dict(title="Escrever o aviso", frame="Study group on {day}! Bring your {thing} and a pen.", slots=[dict(key="day", opts=["Tuesday", "Thursday", "Saturday"]), dict(key="thing", opts=["notebook", "book", "notes"])], model="Study group on Tuesday! Bring your notebook and a pen.", note="Bring your… é uma ordem amigável: traga seu/sua."),
 ],
 sounds=[
  dict(say="Every Tuesday at five.", tag="ritmo: EV-ry TUES-day at FIVE", tip="Every tem duas sílabas: EV-ry. Acentue TUES e FIVE; at fica fraco."),
  dict(say="I need practice.", tag="ligação: need practice", tip="O d de need quase some antes do p. Soa 'nee-practice'. Acentue PRAC."),
  dict(say="English grammar and vocabulary.", tag="acento: vo-CAB-u-lar-y", tip="Em vocabulary, acentue CAB: vo-CAB-yu-lary. O 'and' vira 'n': 'grammar-n'."),
 ],
 role=dict(turns=[
  dict(npc="Hey, want to join our study group?", opts=[
   dict(en="Yes! When do you meet?", pt="Quero! Quando vocês se encontram?", reply="Every Tuesday at five."),
   dict(en="Sure! What do you study?", pt="Claro! O que vocês estudam?", reply="English grammar and vocabulary."),
   dict(en="That sounds fun. Who is in the group?", pt="Parece divertido. Quem está no grupo?", reply="Four students. We are all friendly.")]),
  dict(npc="Every Tuesday at five.", opts=[
   dict(en="Where?", pt="Onde?", reply="In the library, room three."),
   dict(en="Great. Where do you meet?", pt="Ótimo. Onde vocês se encontram?", reply="In the library, room three."),
   dict(en="Tuesday is good. Is it far?", pt="Terça é bom. É longe?", reply="No, it's near the main door.")]),
  dict(npc="We study English grammar and vocabulary.", opts=[
   dict(en="Perfect. I need practice.", pt="Perfeito. Preciso de prática.", reply="Great! You can practice with us."),
   dict(en="Nice. Grammar is hard for me.", pt="Legal. A gramática é difícil para mim.", reply="No problem. We help each other."),
   dict(en="Cool. I want to learn new words.", pt="Legal. Quero aprender palavras novas.", reply="Good. We have a word list.")]),
  dict(npc="Bring your notebook and a pen.", opts=[
   dict(en="OK. Thanks! See you on Tuesday.", pt="Ok. Obrigado! Vejo você na terça.", reply="See you!"),
   dict(en="Sure. Should I bring a book too?", pt="Claro. Devo levar um livro também?", reply="Yes, bring your English book."),
   dict(en="Got it. Can I invite a friend?", pt="Entendi. Posso convidar um amigo?", reply="Of course! More people, more fun.")]),
 ], change=["Você não pode terça às cinco: pergunte se há outro dia.", "A sala está cheia: pergunte onde mais o grupo pode se encontrar.", "Você esqueceu o caderno: peça uma folha emprestada."]),
 writing=dict(task="Escreva 2 ou 3 frases para um colega: aceite entrar no grupo, pergunte quando e onde, e diga o que vai levar.", model="Yes, I want to join! When and where do you meet? I'll bring my notebook and a pen.", kw=["join", "meet", "bring", "notebook"], checks=["Aceitou o convite.", "Perguntou quando ou onde.", "Disse o que vai levar."]),
 scenes=dict(pool=["school", "library", "hall", "cafe"], npc=dict(g="m", role="friend"), you=dict(g="f")),
 convo=dict(npc=dict(name="Jordan"), story="Depois da aula, o Jordan convida você para um grupo de estudos.", turns=[
  dict(npc="Hey, want to join our study group?", pt="Ei, quer entrar no nosso grupo de estudos?", opts=[
   dict(en="Every Tuesday at five.", pt="Toda terça às cinco.", ok=False, fb="Essa informação é dele."),
   dict(en="Yes! When do you meet?", pt="Quero! Quando vocês se encontram?", ok=True, fb="Aceita e pergunta quando."),
   dict(en="Bring your notebook.", pt="Traga seu caderno.", ok=False, fb="Não responde ao convite.")]),
  dict(npc="Every Tuesday at five.", pt="Toda terça às cinco.", opts=[
   dict(en="In the library, room three.", pt="Na biblioteca, sala três.", ok=False, fb="Quem responde onde é ele."),
   dict(en="Where do you meet?", pt="Onde vocês se encontram?", ok=True, fb="Próxima pergunta natural."),
   dict(en="When do you meet?", pt="Quando vocês se encontram?", ok=False, fb="Ele acabou de dizer.")]),
  dict(npc="In the library, room three.", pt="Na biblioteca, sala três.", opts=[
   dict(en="Great. What do you study?", pt="Ótimo. O que vocês estudam?", ok=True, fb="Pergunta o conteúdo."),
   dict(en="Great. Where do you meet?", pt="Ótimo. Onde vocês se encontram?", ok=False, fb="Ele já respondeu."),
   dict(en="English grammar and vocabulary.", pt="Gramática e vocabulário de inglês.", ok=False, fb="Quem diz o assunto é ele.")]),
  dict(npc="English grammar and vocabulary.", pt="Gramática e vocabulário de inglês.", opts=[
   dict(en="Hey, want to join our group?", pt="Ei, quer entrar no nosso grupo?", ok=False, fb="O convite foi dele."),
   dict(en="Bring your notebook and a pen.", pt="Traga seu caderno e uma caneta.", ok=False, fb="Quem diz isso é ele."),
   dict(en="Perfect. I need practice.", pt="Perfeito. Preciso de prática.", ok=True, fb="Mostra que combina com você.")]),
  dict(npc="Bring your notebook and a pen.", pt="Traga seu caderno e uma caneta.", opts=[
   dict(en="Where is the room?", pt="Onde fica a sala?", ok=False, fb="Você já sabe onde é."),
   dict(en="Every Tuesday at five.", pt="Toda terça às cinco.", ok=False, fb="Essa fala é dele."),
   dict(en="OK, thanks! See you on Tuesday.", pt="Ok, obrigado! Até terça.", ok=True, fb="Despedida simpática.")]),
 ]),
)
