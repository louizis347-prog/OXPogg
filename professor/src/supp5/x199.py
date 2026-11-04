X = dict(
 key=dict(big="I'm so late!", label="Estou atrasado", sub="Diga que está atrasado, explique o motivo em uma frase e pergunte a hora. Frases curtas e calmas bastam."),
 mini=[
  dict(who="Cole", en="Wake up! It's {seven thirty!|eight o'clock!|almost eight!}", pt="Acorde! São {sete e meia!|oito horas!|quase oito!}"),
  dict(who="You", en="What? My {alarm|phone} didn't ring.", pt="O quê? {Meu alarme|Meu celular} não tocou."),
  dict(who="Cole", en="Oh no. When does your {class|bus} start?", pt="Ai, não. Quando {começa sua aula?|sai seu ônibus?}"),
  dict(who="You", en="At {eight o'clock.|nine o'clock.|eight thirty.} I'm so late!", pt="{Às oito horas.|Às nove horas.|Às oito e meia.} Estou tão atrasado!"),
 ],
 dlg=[
  dict(who="Cole", en="Wake up! It's {seven thirty!|eight o'clock!}", pt="Acorde! São {sete e meia!|oito horas!}"),
  dict(who="You", en="What? My {alarm|phone} didn't ring.", pt="O quê? {Meu alarme|Meu celular} não tocou."),
  dict(who="Cole", en="Did you set it for {six?|five?}", pt="Você programou para as {seis?|cinco?}"),
  dict(who="You", en="No, I set it for {seven.|eight.}", pt="Não, programei para as {sete.|oito.}"),
  dict(who="Cole", en="Then it rang an {hour|day} ago!", pt="Então tocou {uma hora|um dia} atrás!"),
  dict(who="You", en="Oh no, I'm so {late.|tired.}", pt="Ai, não, estou tão {atrasado.|cansado.}"),
  dict(who="Cole", en="When does your {class|bus} start?", pt="Quando {começa sua aula?|sai seu ônibus?}"),
  dict(who="You", en="At {eight|nine} o'clock.", pt="Às {oito|nove} horas."),
  dict(who="Cole", en="Take a {quick|cold} shower.", pt="Tome um banho {rápido.|frio.}"),
 ],
 vocab=[
  dict(w="shower", pt="banho (de chuveiro)", e="🚿", ex=["I take a quick shower.", "The shower is hot."]),
  dict(w="sleep", pt="dormir, sono", e="😴", ex=["I sleep eight hours.", "I need more sleep."]),
  dict(w="quick", pt="rápido", e="⚡", ex=["I take a quick shower.", "Make a quick call."]),
  dict(w="rush", pt="correria, apressar-se", e="🏃", ex=["I rush to class.", "It is rush hour."]),
  dict(w="oversleep", pt="dormir demais", e="💤", ex=["I oversleep on Sundays.", "Don't oversleep!"]),
  dict(w="clothes", pt="roupas", e="👕", ex=["I put on my clothes.", "My clothes are on the chair."]),
 ],
 molds=[
  dict(title="Dizer que o alarme falhou", frame="My {thing} didn't ring. I'm so late!", slots=[dict(key="thing", opts=["alarm", "phone", "clock"])], model="My alarm didn't ring. I'm so late!", note="Didn't + verbo base: didn't ring. A segunda frase mostra a consequência."),
  dict(title="Dizer a hora que programou", frame="I set it for {time}. My class starts at {start}.", slots=[dict(key="time", opts=["seven", "six", "eight"]), dict(key="start", opts=["eight", "nine", "ten"])], model="I set it for seven. My class starts at eight.", note="Set não muda no passado. At + hora para dizer quando começa."),
  dict(title="Escrever uma mensagem de atraso", frame="Sorry, I'm running late. I'll be there in {time}.", slots=[dict(key="time", opts=["ten minutes", "fifteen minutes", "half an hour"])], model="Sorry, I'm running late. I'll be there in ten minutes.", note="I'm running late avisa o atraso. In + tempo diz quando você chega."),
 ],
 sounds=[
  dict(say="Wake up! It's seven thirty!", tag="ritmo: WAKE up, SEVen THIRty", tip="Acentue WAKE, SEV e THIR. As palavras pequenas ficam leves e rápidas."),
  dict(say="Did you set it?", tag="redução: did you", tip="Did you soa 'didja'. O d e o y se juntam num som só."),
  dict(say="I'm so late.", tag="som: l inicial de late", tip="Late começa com l claro e termina em t. A vogal é longa: 'leit'."),
 ],
 role=dict(turns=[
  dict(npc="Wake up! It's seven thirty!", opts=[
   dict(en="What? My alarm didn't ring.", pt="O quê? Meu alarme não tocou.", reply="Did you set it for six?"),
   dict(en="Seven thirty? I'm so late!", pt="Sete e meia? Estou tão atrasado!", reply="When does your class start?"),
   dict(en="What? Is it that late?", pt="O quê? Já é tão tarde?", reply="Yes! Did you set your alarm?")]),
  dict(npc="Did you set it for six?", opts=[
   dict(en="No, I set it for seven.", pt="Não, programei para as sete.", reply="Then it rang an hour ago!"),
   dict(en="No, I set it for eight.", pt="Não, programei para as oito.", reply="Then it didn't ring yet. But you're late!"),
   dict(en="Yes, but it didn't ring.", pt="Sim, mas não tocou.", reply="Maybe the phone is off. Check it!")]),
  dict(npc="When does your class start?", opts=[
   dict(en="At eight o'clock.", pt="Às oito horas.", reply="Take a quick shower."),
   dict(en="At nine o'clock.", pt="Às nove horas.", reply="You have time. Take a quick shower."),
   dict(en="At eight thirty.", pt="Às oito e meia.", reply="Take a quick shower. Go!")]),
  dict(npc="Take a quick shower.", opts=[
   dict(en="Okay. Where are my keys?", pt="Certo. Onde estão minhas chaves?", reply="On the table. And take a banana!"),
   dict(en="Okay. Can you make breakfast?", pt="Certo. Você pode fazer o café?", reply="No time! Take a banana."),
   dict(en="Thanks, Cole!", pt="Valeu, Cole!", reply="Hurry up! Take your keys.")]),
 ], change=["O ônibus passa em cinco minutos: diga que precisa correr.", "Você não acha as chaves: pergunte onde estão.", "A aula foi cancelada: diga que está aliviado e vai dormir mais."]),
 writing=dict(task="Você acordou tarde. Escreva 2 ou 3 frases para um amigo: diga que está atrasado, que o alarme não tocou e a que horas começa a sua aula.", model="I'm so late! My alarm didn't ring. My class starts at eight.", kw=["late", "alarm", "ring", "class"], checks=["Disse que está atrasado.", "Explicou o alarme.", "Disse a hora da aula."]),
 scenes=dict(pool=["bedroom", "living", "bath", "kitchen"], npc=dict(g="m", role="friend"), you=dict(g="f")),
 convo=dict(npc=dict(name="Cole"), story="Você mora com o Cole. Você acorda tarde, e ele ajuda você a se arrumar para a aula.", turns=[
  dict(npc="Wake up! It's seven thirty!", pt="Acorde! São sete e meia!", opts=[
   dict(en="What? My alarm didn't ring.", pt="O quê? Meu alarme não tocou.", ok=True, fb="Explica o que aconteceu."),
   dict(en="At eight o'clock.", pt="Às oito horas.", ok=False, fb="Ninguém perguntou a hora da aula ainda."),
   dict(en="Take a quick shower.", pt="Tome um banho rápido.", ok=False, fb="Essa fala é do Cole.")]),
  dict(npc="Did you set it for six?", pt="Você programou para as seis?", opts=[
   dict(en="No, I set it for seven.", pt="Não, programei para as sete.", ok=True, fb="Responde com set no passado."),
   dict(en="Then it rang an hour ago!", pt="Então tocou uma hora atrás!", ok=False, fb="Essa conclusão é do Cole."),
   dict(en="Oh no, I'm so late.", pt="Ai, não, estou tão atrasado.", ok=False, fb="Ainda falta responder a pergunta.")]),
  dict(npc="Then it rang an hour ago!", pt="Então tocou uma hora atrás!", opts=[
   dict(en="Oh no, I'm so late.", pt="Ai, não, estou tão atrasado.", ok=True, fb="Reação natural."),
   dict(en="No, I set it for seven.", pt="Não, programei para as sete.", ok=False, fb="Você já disse isso."),
   dict(en="Did you set it for six?", pt="Você programou para as seis?", ok=False, fb="Quem pergunta isso é o Cole.")]),
  dict(npc="When does your class start?", pt="Quando começa sua aula?", opts=[
   dict(en="Take a quick shower.", pt="Tome um banho rápido.", ok=False, fb="Essa fala é do Cole."),
   dict(en="Wake up!", pt="Acorde!", ok=False, fb="Você já acordou."),
   dict(en="At eight o'clock.", pt="Às oito horas.", ok=True, fb="Responde a hora com at.")]),
  dict(npc="Take a quick shower.", pt="Tome um banho rápido.", opts=[
   dict(en="Good idea. Thanks, Cole!", pt="Boa ideia. Valeu, Cole!", ok=True, fb="Aceita a ajuda e agradece."),
   dict(en="At eight o'clock.", pt="Às oito horas.", ok=False, fb="A hora da aula já foi dita."),
   dict(en="My alarm didn't ring.", pt="Meu alarme não tocou.", ok=False, fb="Você já explicou isso.")]),
 ]),
)
