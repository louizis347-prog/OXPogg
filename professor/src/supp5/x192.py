X = dict(
 key=dict(big="Long time no see!", label="Rever um amigo", sub="Cumprimente com simpatia, pergunte como a pessoa tem estado e conte uma novidade curta."),
 mini=[
  dict(who="You", en="{Long time no see!|Hey, stranger!|Wow, it's you!} How have you been?", pt="{Quanto tempo!|E aí, sumido!|Uau, é você!} Como você tem estado?"),
  dict(who="Aaron", en="Great! I live in {Utah|Texas|Ohio} now.", pt="Ótimo! Moro em {Utah|Texas|Ohio} agora."),
  dict(who="You", en="Really? {Since when?|How is it?|That's wonderful!}", pt="Sério? {Desde quando?|Como é?|Que maravilha!}"),
  dict(who="Aaron", en="Since {last year.|January.|spring.} I got a new {job.|house.}", pt="Desde {o ano passado.|janeiro.|a primavera.} Arrumei um novo {emprego.|casa.}"),
 ],
 dlg=[
  dict(who="Aaron", en="Oh my gosh! Is that you, {Mark?|Mark!}", pt="Meu Deus! É você, {Mark?|Mark!}"),
  dict(who="You", en="Dina! Long time {no see!|no see.}", pt="Dina! {Quanto tempo!|Quanto tempo.}"),
  dict(who="Aaron", en="How have you {been?|been, Mark?}", pt="Como você tem {estado?|estado, Mark?}"),
  dict(who="You", en="{Great!|Good!} I live in Utah now.", pt="{Ótimo!|Bem!} Moro em Utah agora."),
  dict(who="Aaron", en="Really? Since {when?|then?}", pt="Sério? Desde {quando?|então?}"),
  dict(who="You", en="Since last year. I got a new {job.|home.}", pt="Desde o ano passado. Arrumei um novo {emprego.|lar.}"),
  dict(who="Aaron", en="That's {wonderful.|great.} What do you do?", pt="Que {maravilha.|ótimo.} O que você faz?"),
  dict(who="You", en="I'm a graphic {designer.|artist.} And you?", pt="Sou {designer|artista} gráfico. E você?"),
  dict(who="Aaron", en="I {teach|study} English.", pt="Eu {ensino|estudo} inglês."),
 ],
 vocab=[
  dict(w="kiss", pt="beijo, beijar", e="😘", ex=["She gives me a kiss.", "I kiss my old friend."]),
  dict(w="married", pt="casado(a)", e="💍", ex=["Dina is married.", "They are married."]),
  dict(w="news", pt="novidades, notícias", e="📰", ex=["I have good news.", "What's your news?"]),
  dict(w="miss", pt="sentir saudade", e="💭", ex=["I miss you.", "We miss our old school."]),
  dict(w="wonderful", pt="maravilhoso", e="🌟", ex=["That's wonderful!", "She has a wonderful job."]),
  dict(w="designer", pt="designer", e="🎨", ex=["He is a designer.", "My sister is a graphic designer."]),
 ],
 molds=[
  dict(title="Dizer onde você mora", frame="I live in {place} now.", slots=[dict(key="place", opts=["Utah", "Texas", "Boston", "Brazil"])], model="I live in Utah now.", note="Live é verbo de estado: use I live, não I am living."),
  dict(title="Dizer o que você faz", frame="I'm a {job}. And you?", slots=[dict(key="job", opts=["graphic designer", "teacher", "nurse", "driver"])], model="I'm a graphic designer. And you?", note="Use a/an antes da profissão. And you? devolve a pergunta."),
  dict(title="Escrever novidades", frame="Long time no see! I live in {place} now. I {news}.", slots=[dict(key="place", opts=["Utah", "Texas", "Boston"]), dict(key="news", opts=["got a new job", "got married", "have a new house"])], model="Long time no see! I live in Utah now. I got a new job.", note="Comece com a saudação, conte onde mora e uma novidade."),
 ],
 sounds=[
  dict(say="How have you been?", tag="o som do h: sopro leve", tip="O h é só um sopro de ar, sem vibrar a garganta. Não diga 'r' forte."),
  dict(say="Long time no see!", tag="ritmo: LONG TIME no SEE", tip="Acentue LONG, TIME e SEE. O 'no' fica fraquinho."),
  dict(say="Is that you, Mark?", tag="ligação: is that you", tip="Una as palavras: 'is-that-chu'. O t de that vira um som de 'tch' antes de you."),
 ],
 role=dict(turns=[
  dict(npc="Oh my gosh! Is that you?", opts=[
   dict(en="Long time no see!", pt="Quanto tempo!", reply="It's been years! How have you been?"),
   dict(en="Yes, it's me! Hi!", pt="Sim, sou eu! Oi!", reply="Wow! How have you been?"),
   dict(en="Hey! What a surprise!", pt="Oi! Que surpresa!", reply="I know! How have you been?")]),
  dict(npc="How have you been?", opts=[
   dict(en="Great! I live in Utah now.", pt="Ótimo! Moro em Utah agora.", reply="Really? Since when?"),
   dict(en="Good! I live in Texas now.", pt="Bem! Moro no Texas agora.", reply="Really? Since when?"),
   dict(en="Great! I have a new home.", pt="Ótimo! Tenho uma casa nova.", reply="Really? Since when?")]),
  dict(npc="Since when?", opts=[
   dict(en="Since last year. I got a new job.", pt="Desde o ano passado. Arrumei um emprego novo.", reply="That's wonderful! What do you do?"),
   dict(en="Since January. I got a new job.", pt="Desde janeiro. Arrumei um emprego novo.", reply="That's great! What do you do?"),
   dict(en="Since spring. I got married.", pt="Desde a primavera. Me casei.", reply="Congratulations! And what do you do?")]),
  dict(npc="What do you do?", opts=[
   dict(en="I'm a graphic designer. And you?", pt="Sou designer gráfico. E você?", reply="I teach English."),
   dict(en="I'm a nurse. And you?", pt="Sou enfermeiro. E você?", reply="I teach English."),
   dict(en="I'm a driver. And you?", pt="Sou motorista. E você?", reply="I teach English.")]),
 ], change=["Você não lembra o nome do amigo: diga que é você mesmo e pergunte o nome.", "O amigo conta que está casado: reaja e peça mais detalhes.", "Vocês estão com pressa: troque telefones e combine um café."]),
 writing=dict(task="Escreva 2 ou 3 frases para um amigo antigo: cumprimente, diga onde mora e o que faz.", model="Long time no see! I live in Utah now. I'm a graphic designer.", kw=["long", "see", "live", "designer"], checks=["Cumprimentou o amigo.", "Disse onde mora.", "Disse o que faz."]),
 scenes=dict(pool=["cafe", "cafe2", "street", "park"], npc=dict(g="f", role="friend"), you=dict(g="m")),
 convo=dict(npc=dict(name="Aaron"), story="Você encontra uma velha amiga em um café. Faz muito tempo que vocês não se veem.", turns=[
  dict(npc="Oh my gosh! Is that you, Mark?", pt="Meu Deus! É você, Mark?", opts=[
   dict(en="Dina! Long time no see!", pt="Dina! Quanto tempo!", ok=True, fb="Cumprimento caloroso para um velho amigo."),
   dict(en="How have you been?", pt="Como você tem estado?", ok=False, fb="Primeiro cumprimente; essa pergunta vem depois."),
   dict(en="Since last year.", pt="Desde o ano passado.", ok=False, fb="Ninguém perguntou isso ainda.")]),
  dict(npc="How have you been?", pt="Como você tem estado?", opts=[
   dict(en="I teach English.", pt="Eu ensino inglês.", ok=False, fb="Essa fala é da Dina, e não responde à pergunta."),
   dict(en="Great! I live in Utah now.", pt="Ótimo! Moro em Utah agora.", ok=True, fb="Resposta curta com uma novidade."),
   dict(en="Long time no see!", pt="Quanto tempo!", ok=False, fb="Você já disse isso.")]),
  dict(npc="Really? Since when?", pt="Sério? Desde quando?", opts=[
   dict(en="Since last year. I got a new job.", pt="Desde o ano passado. Arrumei um emprego novo.", ok=True, fb="Diz quando e por quê."),
   dict(en="That's wonderful. What do you do?", pt="Que maravilha. O que você faz?", ok=False, fb="Quem pergunta isso é a Dina."),
   dict(en="I'm a graphic designer.", pt="Sou designer gráfico.", ok=False, fb="Ainda não perguntaram seu trabalho.")]),
  dict(npc="That's wonderful. What do you do?", pt="Que maravilha. O que você faz?", opts=[
   dict(en="Really? Since when?", pt="Sério? Desde quando?", ok=False, fb="Você já falou disso."),
   dict(en="I live in Utah now.", pt="Moro em Utah agora.", ok=False, fb="Não responde ao trabalho."),
   dict(en="I'm a graphic designer. And you?", pt="Sou designer gráfico. E você?", ok=True, fb="Responde e pergunta de volta.")]),
  dict(npc="I teach English.", pt="Eu ensino inglês.", opts=[
   dict(en="That's great! I miss our school.", pt="Que ótimo! Sinto saudade da escola.", ok=True, fb="Reação simpática."),
   dict(en="I'm a graphic designer.", pt="Sou designer gráfico.", ok=False, fb="Você já disse isso."),
   dict(en="How have you been?", pt="Como você tem estado?", ok=False, fb="Já perguntaram isso no começo.")]),
 ]),
)
