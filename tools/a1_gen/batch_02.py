# Lote 02 — posições 14 a 21 do A1 (Arco A1·2 · Soletrar, números e dinheiro).
# TROCAS DE OBRA:
# pos 14: de Jabberwocky para You've Got Mail (filme, 1998) — poema nonsense não ajuda a ensinar e-mail/telefone.
# pos 16: de Ratatouille: The Experiment para Eloise (livro, 1955) — a obra do brief era fraca/duvidosa; Eloise vive num hotel de Nova York.
# pos 17: de Home, Sweet Home para The Grand Budapest Hotel (filme, 2014) — a frase "there's no place like home" já foi usada no piloto de Oz.
# pos 18: de Friends "📏 Livro" para Friends (série de TV, 1994) — mesma obra, só corrigido o tipo (série, não livro).
# pos 21: de Casey Jones para The Polar Express (livro, 1985) — Casey Jones aparece repetida na pos 22.
# (pos 15 Waldorf Astoria, pos 19 One, Two, Buckle My Shoe e pos 20 This Old Man foram mantidas.)


# ---------------------------------------------------------------- helpers
def RSD(*v):
    k = 'rdg pat vplay sbuild build order balloons dictate soundlab scene dquiz scenebuild produce review wrap'.split()
    assert len(v) == len(k)
    return dict(zip(k, v))


def H(e, x, y, en, pt, say, sayPt):
    return dict(e=e, x=x, y=y, en=en, pt=pt, say=say, sayPt=sayPt)


def G(q, pt, opts, a, why):
    return dict(q=q, pt=pt, opts=opts, a=a, why=why)


def T(opts, a, why, q='Qual frase está certa?'):
    return dict(q=q, opts=opts, a=a, why=why)


def Q(q, pt, opts, a, line, why):
    return dict(q=q, pt=pt, opts=[list(o) for o in opts], a=a, line=line, why=why)


def PR(prompt, ph, chips, model, check, kw, tips, ok, reply):
    return dict(prompt=prompt, ph=ph, chips=chips, model=model, check=check, kw=kw, tips=tips, ok=ok, reply=reply)


def MS(ic, name, desc, prompt, chips, model, check, kw, tips, ok, reply):
    return dict(ic=ic, name=name, desc=desc, data=PR(prompt, 'Escreva a sua resposta aqui…', chips, model, check, kw, tips, ok, reply))


def EXP(ic, en, tag, pt, use, ex):
    return dict(ic=ic, en=en, tag=tag, pt=pt, use=use, ex=ex)


def RND(say, opts, a, why):
    return dict(fig='🎧', say=say, ask='Qual palavra você ouviu?', opts=opts, a=a, why=why)


def HW(say, opts, a, why):
    return dict(fig='🎧', say=say, ask='Ouça e toque na palavra.', opts=opts, a=a, why=why)


def HP(say, emojis, a, why):
    return dict(fig='🎧', say=say, ask='Ouça e toque na figura.', opts=[[e, ''] for e in emojis], a=a, why=why, pic=1)


def VBI(v, ic, pt, f1, f2, ex, note):
    return dict(v=v, ic=ic, pt=pt, f=[['eu', f1], ['ele/ela', f2]], ex=ex, note=note)


def MOLD(label, slots, end):
    return dict(label=label, slots=[dict(cat=c, opts=[list(o) for o in os]) for c, os in slots], end=end)


def CXI(text, pt, opts):
    return dict(text=text, pt=pt, opts=opts, a=0)


def TR(ask, opts, a, why, say=None):
    d = dict(ask=ask, opts=opts, a=a, why=why)
    if say:
        d['say'] = say
    return d


def MG(text, pt, opts, a, why, say):
    return dict(text=text, pt=pt, opts=opts, a=a, why=why, say=say)


def EQ(ask, opts, a, why):
    return dict(ask=ask, opts=opts, a=a, why=why)


def ART(s, items, seed):
    return dict(s=s, items=[[e, x, y, z, 'bob'] for e, x, y, z in items], seed=seed)


def PA(t, e, p, v=0):
    return dict(t=t, e=e, p=p, v=v)


def EP(B, X, XT, VB, MR, CX):
    return dict(B=B, X=X, XT=XT, VB=VB, MR=MR, CX=CX)


# ================================================================ pos 14 · You've Got Mail
def E14():
    B = dict(
        title="Your Email, Please · What's your…?",
        sub="Pedir e dar contatos: What's your email? What's your phone number? Spell it, please.",
        pattern_label="What's your…?",
        why="Hoje você aprende a pedir dados como o Joe e a Kathleen: What's your email? What's your phone number? E a responder com It's…",
        vocab=[["Spell", "Soletrar", "Soa como “SPÉL”."],
               ["Email", "E-mail", "Soa como “Í-mêil”."],
               ["Phone", "Telefone", "Soa como “FÔUN”."],
               ["Pen", "Caneta", "Soa como “PÉN”."],
               ["Number", "Número", "Soa como “NÂM-ber”."],
               ["Computer", "Computador", "Soa como “kam-PIÚ-ter”."]],
        balloons=[["✉️", "email"], ["📞", "phone"], ["🖊️", "pen"], ["💻", "computer"], ["🔤", "spell"], ["🔢", "number"]],
        cover_art=ART('shop', [("✉️", 104, 56, 20), ("💻", 138, 44, 12), ("📞", 84, 34, 12)], 'yg1'),
        cover_sub="What's your…? Em 10 minutos você pede e-mail e telefone como em Nova York",
        cover_say="O Joe e a Kathleen trocam e-mails sem saber quem é quem. Você sabe perguntar o e-mail de alguém em inglês?",
        wrap_recap=[["What's your email?", "Qual é o seu e-mail?"],
                    ["What's your phone number?", "Qual é o seu número de telefone?"],
                    ["It's joe at fox dot com.", "É joe arroba fox ponto com."],
                    ["Spell it, please.", "Soletre, por favor."]],
        teaser=dict(t="Your Room Key", d="Próximo padrão: my e your para falar do que é seu e do que é do outro"),
        cast={"Kathleen": ["👩", "#2f8f6b"], "Joe": ["👨", "#34495e"], "Birdie": ["👵", "#8e6aa8"]},
        lines=[["Kathleen", "Hello! I'm Kathleen. What's your name?", "Olá! Eu sou a Kathleen. Qual é o seu nome?"],
               ["Joe", "I'm Joe. What's your email, Kathleen?", "Eu sou o Joe. Qual é o seu e-mail, Kathleen?"],
               ["Kathleen", "It's shopgirl at mail dot com.", "É shopgirl arroba mail ponto com."],
               ["Joe", "Spell it, please. I'm on the computer.", "Soletre, por favor. Estou no computador."],
               ["Kathleen", "S-H-O-P-G-I-R-L. Now your email, Joe. Use a pen!", "S-H-O-P-G-I-R-L. Agora o seu e-mail, Joe. Use uma caneta!"],
               ["Joe", "Ha! It's joe at fox dot com.", "Ha! É joe arroba fox ponto com."],
               ["Birdie", "Joe, what's your phone number?", "Joe, qual é o seu número de telefone?"],
               ["Joe", "Oh, it's a secret, Birdie!", "Ah, é um segredo, Birdie!"]],
        quiz=[Q("Who is on the computer?", "Quem está no computador?", [("👩", "Kathleen"), ("👨", "Joe"), ("👵", "Birdie")], 1, 3, "Joe diz: “I'm on the computer.”"),
              Q("What is Joe's email?", "Qual é o e-mail do Joe?", [("✉️", "shopgirl at mail dot com"), ("📧", "joe at mail dot com"), ("📨", "joe at fox dot com")], 2, 5, "Joe diz: “It's joe at fox dot com.”"),
              Q("Who asks for the phone number?", "Quem pede o número de telefone?", [("👵", "Birdie"), ("👩", "Kathleen"), ("👨", "Joe")], 0, 6, "Birdie pergunta: “What's your phone number?”")],
        rdg_q=dict(q="Como perguntar o e-mail de alguém?", o=["What's you email?", "What's your email?", "What your email?"], a=1,
                   why="Use **What's your** + palavra: What's your email? (**your** com r, e **What's** com o verbo.)"),
        dictate=[["What's your email?", "Qual é o seu e-mail?"], ["Spell it, please.", "Soletre, por favor."],
                 ["It's joe at fox dot com.", "É joe arroba fox ponto com."], ["What's your phone number?", "Qual é o seu número de telefone?"]],
        produce=PR("A Kathleen pergunta: *What's your name? What's your email?* **Diga o seu nome com I'm, dê um e-mail inventado com It's… e pergunte o telefone dela com What's your…?**",
                   "Ex.: I'm Ana. It's ana at mail dot com. What's your phone number?",
                   ["I'm", "It's", "What's your…?"],
                   "I'm Ana. It's ana at mail dot com. What's your phone number, Kathleen?",
                   ["Disse o meu nome com I'm?", "Dei o e-mail com It's…?", "Fiz uma pergunta com What's your…?"],
                   ["\\bI(?:['’]m| am)\\s+(?!not\\b)\\w+", "\\bit(?:['’]s| is)\\b[^.!?]*\\b(?:at|dot)\\b", "\\bwhat(?:['’]s| is)\\s+your\\b[^.!?]*\\?"],
                   [[["I'm Ana.", "Eu sou a Ana."], ["I'm Pedro.", "Eu sou o Pedro."]],
                    [["It's ana at mail dot com.", "É ana arroba mail ponto com."], ["It's pedro at mail dot com.", "É pedro arroba mail ponto com."]],
                    [["What's your phone number?", "Qual é o seu número de telefone?"], ["What's your email?", "Qual é o seu e-mail?"]]],
                   ["Nome dito! 🙋", "E-mail dado! ✉️", "Boa pergunta! ❓"],
                   ["Thanks, Ana! Now I know your email. Bye!", "Obrigada, Ana! Agora eu sei o seu e-mail. Tchau!"]),
        rs=RSD('shop', 'office', 'lobby1', 'home1', 'counter', 'cafe3', 'school', 'living', 'hall', 'office', 'street', 'shop', 'counter', 'cafe', 'bedroom'),
        sc='shop')
    X = dict(
        n=70005, review=True, names=("Kathleen", "Joe"),
        stage=dict(rs='shop', chars=[["p:short:d8b45a:f4c7a1:5b8a72:none:dress", 26, 0, 1.0], ["p:short:5a3b25:f4c7a1:2c3e50:none:suit", 56, 1, 1.0], ["p:bun:cfcfcf:f4c7a1:8e6aa8:glasses:dress", 84, 1, 0.95]]),
        obra=dict(name="You've Got Mail", kind="🎬 Filme · 1998", year="1998",
                  text="Comédia romântica americana de 1998, dirigida por Nora Ephron, com Tom Hanks e Meg Ryan. Em Nova York, dois donos de livrarias rivais trocam e-mails sem saber quem é quem. O título vem do aviso que o computador dava ao chegar uma mensagem.",
                  line=["You've got mail!", "Você recebeu um e-mail! (aviso do computador no filme)"],
                  pa=PA('postoffice', ['💌', '💻', '📚'], 'e', 1)),
        gancho=["Joe", "Hi, Kathleen! What's your email?", "Oi, Kathleen! Qual é o seu e-mail?"],
        hot=[H("✉️", 14, 16, "email", "e-mail", "What's your email?", "Qual é o seu e-mail?"),
             H("📞", 40, 14, "phone", "telefone", "What's your phone number?", "Qual é o seu número de telefone?"),
             H("🖊️", 66, 14, "pen", "caneta", "Use a pen, please.", "Use uma caneta, por favor."),
             H("💻", 88, 16, "computer", "computador", "I'm on the computer.", "Estou no computador."),
             H("🔤", 12, 82, "spell", "soletrar", "Spell it, please.", "Soletre, por favor.")],
        gap=[G("___ your email?", "Qual é o seu e-mail?", ["What's", "Where", "Who"], 0, "Para pedir uma informação: **What's** your email? (What is → What's)"),
             G("What's ___ phone number?", "Qual é o seu número de telefone?", ["you", "your", "yours"], 1, "Antes do nome da coisa, use **your**: your phone number."),
             G("___ it, please.", "Soletre, por favor.", ["Spell", "Spelled", "Spells"], 0, "Para pedir algo, use o verbo sozinho: **Spell** it, please."),
             G("It's joe ___ fox dot com.", "É joe arroba fox ponto com.", ["in", "at", "on"], 1, "O símbolo @ se diz **at**: joe **at** fox dot com.")],
        trap=[T(["What your email?", "Whats you email?", "What's your email?"], 2, "A pergunta precisa do verbo: **What's** (What is) your email?"),
              T(["It's a secret.", "Is a secret.", "Its a secret?"], 0, "Para responder, use **It's** (It is): It's a secret.")],
        sticker=dict(title="Kathleen e Joe", sub="You've Got Mail · 1998", rs='shop', chars=[["p:short:d8b45a:f4c7a1:5b8a72:none:dress", 34, 0, 1.0], ["p:short:5a3b25:f4c7a1:2c3e50:none:suit", 68, 1, 1.0]]),
        speakers={"Kathleen": "p:short:d8b45a:f4c7a1:5b8a72:none:dress", "Joe": "p:short:5a3b25:f4c7a1:2c3e50:none:suit", "Birdie": "p:bun:cfcfcf:f4c7a1:8e6aa8:glasses:dress"},
        rule=dict(
            who="p:short:5a3b25:f4c7a1:2c3e50:none:suit", head="What's your…?",
            sub="What is vira What's. Depois vem your + a informação que você quer.",
            say=["What's your email? Spell it, please.", "Qual é o seu e-mail? Soletre, por favor."],
            formula=[dict(from_=[["What", 0], ["is", 1], ["your email?", 3]], to=[["What's", 2], ["your email?", 3]], say="What's your email?", note="**What is** vira **What's**. Assim os americanos falam."),
                     dict(from_=[["What's your phone number?", 3]], to=[["It's", 2], ["joe at fox dot com.", 0]], say="It's joe at fox dot com.", note="Para responder, comece com **It's** e diga a informação.")],
            uses=[dict(ico="✉️", tag="E-mail", en="What's your email?", pt="Qual é o seu e-mail?"),
                  dict(ico="📞", tag="Telefone", en="What's your phone number?", pt="Qual é o seu número de telefone?"),
                  dict(ico="🙋", tag="Nome", en="What's your name?", pt="Qual é o seu nome?"),
                  dict(ico="🔤", tag="Soletrar", en="Spell it, please.", pt="Soletre, por favor.")],
            rules=[dict(tag="What's your", c=0, text="Para **pedir uma informação** sobre a pessoa: nome, e-mail, telefone.", ex="What's your email?"),
                   dict(tag="It's", c=2, text="Para **responder**: It's + a informação. O @ lê-se **at** e o ponto, **dot**.", ex="It's ana at mail dot com."),
                   dict(tag="Spell it", c=1, text="Para **pedir que soletrem**: Spell it, please.", ex="S-H-O-P-G-I-R-L.")],
            tips=["Em português dizemos “qual é o seu e-mail?”. Em inglês o verbo aparece: **What's** (é) your email? Não esqueça o **'s**."]),
        mission_ic="✉️")
    XT = dict(
        exp=[EXP("⏳", "Hang on a sec.", "Informal", "Espere um instante.", "Para pedir que alguém **espere um pouquinho**. *Sec* é *second* (segundo).", ["Hang on a sec, Joe. I'm on the phone.", "Espere um instante, Joe. Estou no telefone."]),
             EXP("👍", "You're all set.", "Expressão", "Está tudo certo.", "Quando você **terminou de ajudar** alguém e não falta mais nada.", ["Thanks, Joe. You're all set!", "Obrigada, Joe. Está tudo certo!"]),
             EXP("📬", "You've got mail!", "Expressão", "Você recebeu um e-mail!", "Frase famosa do **aviso de e-mail** dos anos 90. Hoje também se diz de brincadeira.", ["Kathleen, you've got mail!", "Kathleen, você recebeu um e-mail!"]),
             EXP("🔡", "How do you spell that?", "Expressão", "Como se escreve isso?", "Para pedir que **soletrem** uma palavra ou um nome que você não entendeu.", ["How do you spell that, Joe?", "Como se escreve isso, Joe?"])],
        exp_scene=dict(rs='shop', lines=[["Birdie", "Kathleen, **you've got mail**!", "Kathleen, você recebeu um e-mail!"],
                                         ["Kathleen", "**Hang on a sec**, Birdie. I'm with Joe.", "Espere um instante, Birdie. Estou com o Joe."],
                                         ["Joe", "Kathleen, what's your email?", "Kathleen, qual é o seu e-mail?"],
                                         ["Kathleen", "It's shopgirl at mail dot com.", "É shopgirl arroba mail ponto com."],
                                         ["Joe", "**How do you spell that**?", "Como se escreve isso?"],
                                         ["Kathleen", "S-H-O-P-G-I-R-L. **You're all set**!", "S-H-O-P-G-I-R-L. Está tudo certo!"]]),
        lab=dict(short="nomes das letras A, E, I", title="Laboratório de sons: as letras A, E, I",
                 say="Para soletrar um e-mail em inglês, você precisa dos nomes das letras. Vamos treinar A, E e I!",
                 intro=dict(what="Em inglês, **A** = “êi”, **E** = “i” e **I** = “ái”. São bem diferentes do português!",
                            how="No **A**, comece em “ê” e deslize para um “i” curtinho. O **E** é um “i” longo, com os lábios esticados. No **I**, abra bem a boca em “á” e deslize para “i”.",
                            pt="Em português dizemos “á, é, i”. Por isso é comum confundir o **E** inglês (“i”) com o nosso **I**, e o **I** inglês (“ái”) com o nosso **A**."),
                 ex=[["A", "ÊI", "a letra A", "termina com um “i” leve: ê-i"], ["E", "ÍÍ", "a letra E", "é um “i” longo, sorrindo"], ["I", "ÁI", "a letra I", "abra a boca: á-i"]],
                 pairs=[["pay", "pie", "A = êi · I = ái"], ["may", "me", "A = êi · E = i"], ["tea", "tie", "E = i · I = ái"]],
                 tip="Para o E, sorria como numa foto. Para o I, comece com a boca bem aberta, como no “ai!” de dor.",
                 phrase=["What's your email? Spell it, please.", "Qual é o seu e-mail? Soletre, por favor."],
                 rounds=[RND("tie", ["tea", "tie"], 1, "**tie** (gravata) tem o som do I: “ái”. **Tea** (chá) tem o som do E: “i”."),
                         RND("may", ["may", "me"], 0, "**may** tem o som do A: “êi”. **Me** tem o som do E: “i”."),
                         RND("pie", ["pay", "pie"], 1, "**pie** (torta) tem o som do I: “ái”. **Pay** (pagar) tem o som do A: “êi”.")]),
        hunt=[HW("day", ["day", "die"], 0, "**day** (dia) tem o som do A: “êi”. **Die** (morrer) tem o som do I."),
              HP("tea", ["👔", "☕", "📅"], 1, "**tea** = chá. O som é o do E: “i”."),
              HW("my", ["may", "my"], 1, "**my** (meu) tem o som do I: “ái”. **May** tem o som do A."),
              HW("say", ["say", "see"], 0, "**say** (dizer) tem o som do A: “êi”. **See** (ver) tem o som do E: “i”.")])
    VB = dict(title="Verbos para o e-mail", tip="Quatro verbos: check, ask, call e send.",
              items=[VBI("check", "✅", "conferir", "I check the email.", "Kathleen check**s** the email.", ["I check the email.", "Eu confiro o e-mail."], "**check** = conferir. Com he/she: **checks**."),
                     VBI("ask", "❓", "perguntar, pedir", "I ask for the number.", "Joe ask**s** for the number.", ["I ask for the number.", "Eu peço o número."], "**ask** = perguntar, pedir. Com he/she: **asks**."),
                     VBI("call", "📞", "ligar", "I call Birdie.", "She call**s** Joe.", ["I call Birdie.", "Eu ligo para a Birdie."], "**call** = ligar. Com he/she: **calls**."),
                     VBI("send", "📤", "enviar", "I send an email.", "He send**s** an email.", ["I send an email.", "Eu envio um e-mail."], "**send** = enviar. Com he/she: **sends**.")])
    MR = dict(
        mold=[MOLD("Pedir uma informação", [("pergunta", [("What's your", "qual é o seu/a sua")]),
                                             ("informação", [("email", "e-mail"), ("phone number", "número de telefone"), ("name", "nome"), ("last name", "sobrenome"), ("job", "trabalho")])], ["?", "?"]),
              MOLD("Responder", [("começo", [("It's", "é")]),
                                 ("resposta", [("joe at fox dot com", "joe arroba fox ponto com"), ("shopgirl at mail dot com", "shopgirl arroba mail ponto com"), ("a secret", "um segredo"), ("new", "novo")])], [".", "."]),
              MOLD("Pedir com educação", [("pedido", [("Spell it,", "Soletre,"), ("Write it,", "Escreva,"), ("Say it,", "Diga,")]),
                                           ("educação", [("please", "por favor"), ("again, please", "de novo, por favor")])], [".", "."])],
        speak=[["What's your email? Spell it, please.", "Qual é o seu e-mail? Soletre, por favor."], ["Hang on a sec. You've got mail!", "Espere um instante. Você recebeu um e-mail!"]],
        trap=[TR("“You're all set” quer dizer…", ["Você está atrasado.", "Está tudo certo.", "Você está perdido."], 1, "**You're all set.** = está tudo certo / tudo pronto.", "You're all set."),
              TR("Qual frase está certa?", ["Hang up a sec.", "Hang on to sec.", "Hang on a sec."], 2, "Esperar um instante = **Hang on a sec.**")],
        gap=[MG("___ got mail!", "Você recebeu um e-mail!", ["Your", "You've", "Yours"], 1, "**You've** (You have) got mail! é o aviso famoso.", "You've got mail!"),
             MG("How do you ___ that?", "Como se escreve isso?", ["speak", "spell", "spells"], 1, "**Spell** = soletrar: How do you spell that?", "How do you spell that?")],
        expq=[EQ("Você quer que um amigo espere um pouco. O que diz?", ["Hang on a sec.", "You're all set.", "You've got mail!"], 0, "**Hang on a sec.** = espere um instante."),
              EQ("Você ajudou alguém e não falta mais nada.", ["Hang on a sec.", "How do you spell that?", "You're all set."], 2, "**You're all set.** = está tudo certo."),
              EQ("Você não entendeu como se escreve um nome.", ["You've got mail!", "How do you spell that?", "You're all set."], 1, "**How do you spell that?** pede para soletrar.")],
        missions=[MS("📧", "Troque e-mails", "Peça o e-mail e peça para soletrar.",
                     "Você conhece uma pessoa nova. **Pergunte o e-mail dela com What's your…?, diga o seu com It's… (pode inventar) e peça para soletrar.**",
                     ["What's your", "It's", "Spell it"],
                     "What's your email? It's ana at mail dot com. Spell it, please.",
                     ["Usei What's your…?", "Disse o meu e-mail com It's…?", "Pedi para soletrar?"],
                     ["\\bwhat(?:['’]s| is)\\s+your\\b[^.!?]*\\?", "\\bit(?:['’]s| is)\\b[^.!?]*\\b(?:at|dot)\\b", "\\bspell\\b"],
                     [[["What's your email?", "Qual é o seu e-mail?"]], [["It's ana at mail dot com.", "É ana arroba mail ponto com."]], [["Spell it, please.", "Soletre, por favor."]]],
                     ["Pergunta certa! ❓", "E-mail dado! ✉️", "Soletrar ajuda! 🔤"],
                     ["Thanks! It's easy: A-N-A. Bye!", "Obrigada! É fácil: A-N-A. Tchau!"]),
                  MS("📞", "Telefone e computador", "Use as expressões do episódio.",
                     "Você precisa do telefone de um colega. **Pergunte o número de telefone, peça para ele esperar um instante e diga que está tudo certo.**",
                     ["What's your phone number?"],
                     "What's your phone number? Hang on a sec. You're all set!",
                     ["Perguntei o número de telefone?", "Pedi para esperar um instante?", "Disse que está tudo certo?"],
                     ["\\bwhat(?:['’]s| is)\\s+your\\s+phone number\\b", "\\bhang on a sec", "\\byou(?:['’]re| are) all set\\b"],
                     [[["What's your phone number?", "Qual é o seu número de telefone?"]], [["Hang on a sec.", "Espere um instante."]], [["You're all set.", "Está tudo certo."]]],
                     ["Pergunta certa! 📞", "Espera dada! ⏳", "Tudo certo! 👍"],
                     ["Okay, thanks! See you soon!", "Certo, obrigado! Até logo!"])])
    CX = [CXI("A, N, N, A. Please ___ the name, letter by letter.", "A, N, N, A. Por favor, soletre o nome, letra por letra.", ["spell", "pen", "computer"]),
          CXI("I write a message to Joe at joe@fox.com. It's an ___.", "Escrevo uma mensagem para o Joe em joe@fox.com. É um e-mail.", ["email", "pen", "number"]),
          CXI("Ring, ring! I talk to Joe on the ___.", "Trim, trim! Falo com o Joe no telefone.", ["phone", "pen", "computer"]),
          CXI("I write the name on the paper with a ___.", "Escrevo o nome no papel com uma caneta.", ["pen", "phone", "number"]),
          CXI("Joe asks: What's your phone ___? She says: 555-0123.", "O Joe pergunta: Qual é o seu número de telefone? Ela diz: 555-0123.", ["number", "spell", "email"]),
          CXI("I type a long email on the ___.", "Digito um e-mail longo no computador.", ["computer", "pen", "phone"])]
    return EP(B, X, XT, VB, MR, CX)


# ================================================================ pos 15 · Waldorf Astoria
ANA = "p:long:2b1b12:e8b48a:d35400:none:dress"
SAM = "p:short:1f1f1f:f4c7a1:1a3a6e:none:suit"
MAX = "p:cap:3b2a1a:c68642:9b2c2c:none:shirt"


def E15():
    B = dict(
        title="Your Room Key · my / your",
        sub="Check-in no hotel: my e your antes do nome (my room, your key)",
        pattern_label="my · your",
        why="Hoje você aprende a dizer de quem é a coisa: my (meu, minha) e your (seu, sua).",
        vocab=[["Room", "Quarto", "Soa como “RUM”."], ["Key", "Chave", "Soa como “KÍ”."], ["Passport", "Passaporte", "Soa como “PÉS-pórt”."],
               ["View", "Vista", "Soa como “VIÚ”."], ["Breakfast", "Café da manhã", "Soa como “BRÉK-fast”."], ["Chair", "Cadeira", "Soa como “TCHÉR”."]],
        balloons=[["🛏️", "room"], ["🔑", "key"], ["🛂", "passport"], ["🌆", "view"], ["🥞", "breakfast"], ["🪑", "chair"]],
        cover_art=ART('lobby2', [("🔑", 104, 56, 20), ("🛂", 138, 44, 12), ("🌆", 84, 34, 12)], 'wa1'),
        cover_sub="my e your. Em 10 minutos você faz o check-in em um hotel de Nova York",
        cover_say="A Ana chega ao Waldorf Astoria, em Nova York. O recepcionista pede o passaporte e entrega a chave. De quem é cada coisa? Vamos descobrir.",
        wrap_recap=[["Here is your room key.", "Aqui está a chave do seu quarto."], ["Here is my passport.", "Aqui está o meu passaporte."],
                    ["Is my view nice?", "A minha vista é bonita?"], ["Your breakfast is in the restaurant.", "O seu café da manhã é no restaurante."]],
        teaser=dict(t="Eloise", d="Próximo padrão: Can I…? e Can you…? para pedir e oferecer ajuda"),
        cast={"Ana": ["👩", "#d35400"], "Sam": ["🧑‍💼", "#2b6cb0"], "Max": ["👨", "#9b2c2c"]},
        lines=[["Sam", "Good morning! What's your name, please?", "Bom dia! Qual é o seu nome, por favor?"],
               ["Ana", "I'm Ana Silva. Here is my passport.", "Eu sou a Ana Silva. Aqui está o meu passaporte."],
               ["Sam", "Thank you, Ana. Here is your room key.", "Obrigado, Ana. Aqui está a chave do seu quarto."],
               ["Ana", "Thanks! Is my view nice?", "Obrigada! A minha vista é bonita?"],
               ["Sam", "Yes! Your view is great. Your breakfast is in the restaurant.", "Sim! A sua vista é ótima. O seu café da manhã é no restaurante."],
               ["Ana", "Wonderful! Is my bag here?", "Maravilha! A minha mala está aqui?"],
               ["Max", "Yes! Your bag is here. Right this way!", "Sim! A sua mala está aqui. Por aqui!"],
               ["Ana", "Great! My room, my key, my view!", "Ótimo! O meu quarto, a minha chave, a minha vista!"]],
        quiz=[Q("What does Ana show?", "O que a Ana mostra?", [("🔑", "A key"), ("🛂", "A passport"), ("🧳", "A bag")], 1, 1, "Ana diz: “Here is my passport.”"),
              Q("Is Ana's view nice?", "A vista da Ana é bonita?", [("✅", "Yes, it is"), ("❌", "No, it isn't"), ("🤷", "Maybe")], 0, 4, "Sam diz: “Your view is great.”"),
              Q("Breakfast is in the…", "O café da manhã é no…", [("🛏️", "room"), ("🛋️", "lobby"), ("🍽️", "restaurant")], 2, 4, "Sam diz: “Your breakfast is in the restaurant.”")],
        rdg_q=dict(q="A Ana mostra o passaporte dela. O que ela diz?", o=["Here is your passport.", "Here is my passport.", "Here is I passport."], a=1,
                   why="O passaporte é de quem fala, então use **my**: Here is **my** passport."),
        dictate=[["Here is your room key.", "Aqui está a chave do seu quarto."], ["Here is my passport.", "Aqui está o meu passaporte."],
                 ["Is my view nice?", "A minha vista é bonita?"], ["Your bag is here.", "A sua mala está aqui."]],
        produce=PR("O Sam pergunta: *What's your name? Is your room okay?* **Responda com I'm…, fale de uma coisa sua com my… e elogie o hotel dele com your…**",
                   "Ex.: I'm Ana. My room is great. Your hotel is very nice!",
                   ["I'm", "my…", "your…"],
                   "I'm Ana. My room is great. Your hotel is very nice!",
                   ["Disse o meu nome com I'm?", "Usei my + nome?", "Usei your + nome?"],
                   ["\\bI(?:['’]m| am)\\s+(?!not\\b)\\w+", "\\bmy\\s+\\w+", "\\byour\\s+\\w+"],
                   [[["I'm Ana.", "Eu sou a Ana."], ["I'm from Brazil.", "Sou do Brasil."]],
                    [["My room is great.", "O meu quarto é ótimo."], ["My bag is here.", "A minha mala está aqui."]],
                    [["Your hotel is very nice!", "O seu hotel é muito bonito!"], ["Your view is great!", "A sua vista é ótima!"]]],
                   ["Nome dito! 🙋", "Meu! 🧳", "Seu! 🏨"],
                   ["Thank you, Ana! Have a nice stay!", "Obrigado, Ana! Boa estadia!"]),
        rs=RSD('lobby2', 'lobby', 'lobby1', 'hall', 'counter', 'cafe2', 'bedroom', 'lobby', 'hall', 'lobby2', 'counter', 'bedroom', 'office', 'lobby1', 'kitchen'),
        sc='lobby2')
    X = dict(
        n=30003, review=True, names=("Ana", "Sam"),
        stage=dict(rs='lobby2', chars=[[ANA, 26, 0, 1.0], [SAM, 56, 1, 1.0], [MAX, 84, 1, 0.95]]),
        obra=dict(name="Waldorf Astoria New York", kind="🏨 Hotel histórico · 1931", year="1931",
                  text="Hotel de luxo na Park Avenue, em Nova York. O prédio atual, em estilo Art Déco, abriu em 1931 e tem 47 andares. Muitos presidentes americanos já se hospedaram lá.",
                  line=["Here is your room key.", "Aqui está a chave do seu quarto."],
                  pa=PA('plaza', ['🏨', '🔑', '🛎️'], 'f', 0)),
        gancho=["Sam", "Good morning! Show your passport, please.", "Bom dia! Mostre o seu passaporte, por favor."],
        hot=[H("🔑", 14, 16, "key", "chave", "Here is your room key.", "Aqui está a chave do seu quarto."),
             H("🛂", 40, 14, "passport", "passaporte", "Here is my passport.", "Aqui está o meu passaporte."),
             H("🌆", 66, 14, "view", "vista", "Is my view nice?", "A minha vista é bonita?"),
             H("🥞", 88, 16, "breakfast", "café da manhã", "Your breakfast is in the restaurant.", "O seu café da manhã é no restaurante."),
             H("🪑", 12, 82, "chair", "cadeira", "My chair is nice.", "A minha cadeira é boa.")],
        gap=[G("Here is ___ passport.", "Aqui está o meu passaporte.", ["my", "I", "me"], 0, "Quem fala diz **my** antes do nome: my passport."),
             G("Here is ___ room key.", "Aqui está a chave do seu quarto.", ["I", "you", "your"], 2, "Falando com a pessoa, use **your** antes do nome: your room key."),
             G("___ view is nice.", "A minha vista é bonita.", ["Me", "My", "Mine"], 1, "Antes do nome, use **My**: My view is nice."),
             G("Show ___ passport, please.", "Mostre o seu passaporte, por favor.", ["your", "you", "yours"], 0, "Use **your** + nome: your passport.")],
        trap=[T(["I key is here.", "My key is here.", "Me key is here."], 1, "Antes do nome, use **my**: my key (nunca “I key” ou “me key”)."),
              T(["Here is you room.", "Here is yours room.", "Here is your room."], 2, "Use **your** antes do nome: your room.")],
        sticker=dict(title="Ana no hotel", sub="Waldorf Astoria New York · 1931", rs='lobby2', chars=[[ANA, 34, 0, 1.0], [SAM, 68, 1, 1.0]]),
        speakers={"Ana": ANA, "Sam": SAM, "Max": MAX},
        rule=dict(
            who=ANA, head="my · your", sub="De quem é? Meu ou seu.",
            say=["Here is my passport. Here is your key.", "Aqui está o meu passaporte. Aqui está a sua chave."],
            formula=[dict(from_=[["I", 0]], to=[["my", 0]], say="my key", note="**I** (eu) vira **my** (meu, minha) antes do nome."),
                     dict(from_=[["you", 1]], to=[["your", 1]], say="your key", note="**you** (você) vira **your** (seu, sua) antes do nome.")],
            uses=[dict(ico="🔑", tag="Dar", en="Here is your key.", pt="Aqui está a sua chave."),
                  dict(ico="🛂", tag="Mostrar", en="Here is my passport.", pt="Aqui está o meu passaporte."),
                  dict(ico="🌆", tag="Perguntar", en="Is my view nice?", pt="A minha vista é bonita?"),
                  dict(ico="🍽️", tag="Informar", en="Your breakfast is in the restaurant.", pt="O seu café da manhã é no restaurante.")],
            rules=[dict(tag="my", c=0, text="Para o que é **seu** (de quem fala).", ex="my room · my key"),
                   dict(tag="your", c=1, text="Para o que é **da pessoa com quem você fala**.", ex="your room · your key"),
                   dict(tag="sem the", c=2, text="Em inglês **não** se usa **the** antes de my ou your.", ex="✗ the my room  →  ✓ my room")],
            tips=["**my** e **your** não mudam: my key, my keys; your room, your rooms. Não existe masculino nem feminino."]),
        mission_ic="🔑")
    XT = dict(
        exp=[EXP("👌", "Sure thing.", "Informal", "Pois não. / Claro.", "Resposta simpática quando alguém **pede algo** e você vai fazer.", ["Your key, please. Sure thing!", "A sua chave, por favor. Pois não!"]),
             EXP("🛎️", "Anything else?", "Expressão", "Mais alguma coisa?", "O atendente pergunta isso **depois de ajudar**, para ver se falta algo.", ["Anything else, Ana?", "Mais alguma coisa, Ana?"]),
             EXP("👉", "Right this way.", "Expressão", "Por aqui, por favor.", "Para **guiar alguém** até um lugar: o quarto, a mesa, a sala.", ["Right this way, Ana.", "Por aqui, Ana."]),
             EXP("🙂", "No problem.", "Informal", "Sem problema.", "Resposta natural a um **obrigado** ou a um pedido.", ["Thanks, Max! No problem.", "Obrigada, Max! Sem problema."])],
        exp_scene=dict(rs='lobby2', lines=[["Sam", "Thank you, Ana. Here is your room key. **Anything else**?", "Obrigado, Ana. Aqui está a chave do seu quarto. Mais alguma coisa?"],
                                           ["Ana", "Yes, please. My bag is heavy.", "Sim, por favor. A minha mala é pesada."],
                                           ["Max", "**Sure thing**! I'm Max. **Right this way**.", "Pois não! Eu sou o Max. Por aqui."],
                                           ["Ana", "Thank you, Max! Your hotel is beautiful.", "Obrigada, Max! O seu hotel é lindo."],
                                           ["Max", "Thanks, Ana! **No problem**.", "Obrigado, Ana! Sem problema."],
                                           ["Sam", "Have a nice stay, Ana!", "Tenha uma boa estadia, Ana!"]]),
        lab=dict(short="ee × i", title="Laboratório de sons: key × kit",
                 say="Key, see, three… O som “ii” longo do inglês é diferente do “i” curto de sit!",
                 intro=dict(what="O **ee** de **key** e **three** é um “i” longo. O **i** de **sit** e **ship** é curto e relaxado.",
                            how="Para o **ee**, estique os lábios num sorriso e segure o som. Para o **i** curto, relaxe a boca e solte um som rápido, quase um “é” bem fechado.",
                            pt="Em português só temos um “i”. Em inglês, **seat** (assento) e **sit** (sentar) mudam de sentido, assim como **sheep** (ovelha) e **ship** (navio)."),
                 ex=[["key", "KÍÍ", "chave", "sorria e segure o som"], ["see", "SÍÍ", "ver", "sorria e segure o som"], ["sit", "SIT", "sentar", "curto e relaxado, sem sorrir"]],
                 pairs=[["seat", "sit", "assento × sentar"], ["sheep", "ship", "ovelha × navio"], ["leave", "live", "partir × morar"]],
                 tip="Sorria para o ee longo (key). Para o i curto (sit), relaxe a boca.",
                 phrase=["Sit on your chair, please.", "Sente na sua cadeira, por favor."],
                 rounds=[RND("sit", ["seat", "sit"], 1, "**sit** (sentar) tem o “i” curto. **Seat** (assento) tem o “ii” longo."),
                         RND("sheep", ["sheep", "ship"], 0, "**sheep** (ovelha) tem o “ii” longo. **Ship** (navio) tem o “i” curto."),
                         RND("live", ["leave", "live"], 1, "**live** (morar) tem o “i” curto. **Leave** (partir) tem o “ii” longo.")]),
        hunt=[HW("seat", ["seat", "sit"], 0, "**seat** (assento) tem o “ii” longo."),
              HP("ship", ["🐑", "🚢", "🪑"], 1, "**ship** = navio, com o “i” curto."),
              HW("leave", ["leave", "live"], 0, "**leave** (partir) tem o “ii” longo."),
              HW("sheep", ["sheep", "ship"], 0, "**sheep** (ovelha) tem o “ii” longo.")])
    VB = dict(title="Verbos do check-in", tip="Quatro verbos: show, give, sign e open.",
              items=[VBI("show", "👉", "mostrar", "I show my passport.", "Sam show**s** the room.", ["I show my passport.", "Eu mostro o meu passaporte."], "**show** = mostrar. Com he/she: **shows**."),
                     VBI("give", "🎁", "dar", "I give the key to Ana.", "Sam give**s** the key to Ana.", ["I give the key to Ana.", "Eu dou a chave para a Ana."], "**give** = dar. Com he/she: **gives**."),
                     VBI("sign", "✍️", "assinar", "I sign the card.", "Ana sign**s** the card.", ["I sign the card.", "Eu assino o cartão."], "**sign** = assinar. Com he/she: **signs**."),
                     VBI("open", "🚪", "abrir", "I open the door.", "Max open**s** the door.", ["I open the door.", "Eu abro a porta."], "**open** = abrir. Com he/she: **opens**.")])
    MR = dict(
        mold=[MOLD("Aqui está…", [("começo", [("Here is", "aqui está")]), ("de quem", [("my", "meu/minha"), ("your", "seu/sua")]),
                                  ("coisa", [("room key", "chave do quarto"), ("passport", "passaporte"), ("bag", "mala"), ("card", "cartão")])], [".", "."]),
              MOLD("Perguntar", [("pergunta", [("Is my", "o meu… é"), ("Is your", "o seu… é")]), ("coisa", [("room", "quarto"), ("breakfast", "café da manhã"), ("bag", "mala")]),
                                 ("como", [("nice", "bom/boa"), ("great", "ótimo(a)")])], ["?", "?"]),
              MOLD("Pedir ao hóspede", [("começo", [("Please,", "por favor,")]),
                                        ("pedido", [("show your passport", "mostre o seu passaporte"), ("sign your card", "assine o seu cartão"), ("open your bag", "abra a sua mala")])], [".", "."])],
        speak=[["Here is my passport. Here is your key.", "Aqui está o meu passaporte. Aqui está a sua chave."], ["Right this way. Anything else?", "Por aqui. Mais alguma coisa?"]],
        trap=[TR("“Anything else?” quer dizer…", ["Mais alguma coisa?", "Qualquer lugar?", "Mais alguém?"], 0, "**Anything else?** = mais alguma coisa?", "Anything else?"),
              TR("Qual frase está certa?", ["Light this way.", "Right these way.", "Right this way."], 2, "Para guiar alguém: **Right this way.**")],
        gap=[MG("Sure ___!", "Pois não!", ["thing", "place", "time"], 0, "**Sure thing!** = pois não, claro.", "Sure thing!"),
             MG("Right ___ way, Ana.", "Por aqui, Ana.", ["it", "here", "this"], 2, "**Right this way.** = por aqui.", "Right this way, Ana.")],
        expq=[EQ("Você quer saber se o hóspede precisa de mais alguma coisa.", ["Right this way.", "Anything else?", "Sure thing."], 1, "**Anything else?** = mais alguma coisa?"),
              EQ("Você leva o hóspede até o quarto.", ["No problem.", "Sure thing.", "Right this way."], 2, "**Right this way.** = por aqui."),
              EQ("Alguém agradece e você responde com simpatia.", ["No problem.", "Anything else?", "Right this way."], 0, "**No problem.** = sem problema.")],
        missions=[MS("🛂", "Check-in", "Apresente-se e entregue seus documentos.",
                     "Você chega ao hotel. **Diga o seu nome com I'm…, mostre o seu passaporte com my e peça a chave do quarto com your.**",
                     ["I'm", "my passport", "your room key"],
                     "I'm Ana. Here is my passport. Your room key, please.",
                     ["Disse o meu nome com I'm?", "Falei do meu passaporte com my?", "Pedi a chave com your?"],
                     ["\\bI(?:['’]m| am)\\s+(?!not\\b)\\w+", "\\bmy\\s+passport\\b", "\\byour\\s+(?:room\\s+)?key\\b"],
                     [[["I'm Ana.", "Eu sou a Ana."]], [["Here is my passport.", "Aqui está o meu passaporte."]], [["Your room key, please.", "A chave do quarto, por favor."]]],
                     ["Nome dito! 🙋", "Meu passaporte! 🛂", "Chave pedida! 🔑"],
                     ["Here you go, Ana! Welcome!", "Aqui está, Ana! Bem-vinda!"]),
                  MS("🌆", "Tudo no quarto", "Pergunte sobre as suas coisas no hotel.",
                     "Você está na recepção. **Pergunte duas coisas com Is my…? (a vista, o café da manhã) e agradeça.**",
                     ["Is my"],
                     "Is my view nice? Is my breakfast great? Thank you!",
                     ["Perguntei com Is my…?", "Fiz duas perguntas?", "Agradeci?"],
                     ["\\bis my\\s+\\w+[^.!?]*\\?", "(?:\\bis my\\s+\\w+[^.!?]*\\?[\\s\\S]*){2}", "\\bthank(?:s| you)\\b"],
                     [[["Is my view nice?", "A minha vista é bonita?"]], [["Is my breakfast great?", "O meu café da manhã é ótimo?"]], [["Thank you!", "Obrigado(a)!"]]],
                     ["Pergunta certa! ❓", "Duas perguntas! ✌️", "Educação! 🙏"],
                     ["Yes, they are great! Enjoy your stay!", "Sim, são ótimos! Aproveite a estadia!"])])
    CX = [CXI("I sleep in a ___ at the hotel.", "Eu durmo em um quarto no hotel.", ["room", "key", "chair"]),
          CXI("Use the ___ to open the door.", "Use a chave para abrir a porta.", ["key", "view", "breakfast"]),
          CXI("At the airport, show your ___.", "No aeroporto, mostre o seu passaporte.", ["passport", "chair", "room"]),
          CXI("From the window I see the city. The ___ is nice.", "Da janela vejo a cidade. A vista é bonita.", ["view", "key", "passport"]),
          CXI("Pancakes and coffee in the morning: that's ___.", "Panquecas e café de manhã: é o café da manhã.", ["breakfast", "room", "chair"]),
          CXI("I sit on a ___ near the table.", "Sento em uma cadeira perto da mesa.", ["chair", "key", "view"])]
    return EP(B, X, XT, VB, MR, CX)


# ================================================================ pos 16 · Eloise
ELO = "p:long:e8c35a:f4c7a1:f2a1c2:bow:dress"
NAN = "p:bun:7f7f7f:f4c7a1:2c3e50:glasses:dress"


def E16():
    B = dict(
        title="Can I Have My Key? · Can I…? Can you…?",
        sub="Pedir e pedir ajuda: Can I have…? Can you open…? Yes, I can. / No, I can't.",
        pattern_label="Can I…? Can you…?",
        why="Hoje você aprende a pedir como a Eloise: Can I…? para pedir licença e Can you…? para pedir ajuda. E a responder com Yes, I can / No, I can't.",
        vocab=[["Door", "Porta", "Soa como “DÓR”."], ["Window", "Janela", "Soa como “UÍN-dou”."], ["Bed", "Cama", "Soa como “BÉD”."],
               ["Soap", "Sabonete", "Soa como “SÔUP”."], ["Elevator", "Elevador", "Soa como “É-le-vêi-ter”."], ["Lamp", "Abajur, lâmpada", "Soa como “LÉMP”."]],
        balloons=[["🚪", "door"], ["🪟", "window"], ["🛏️", "bed"], ["🧼", "soap"], ["🛗", "elevator"], ["💡", "lamp"]],
        cover_art=ART('bedroom', [("🛗", 104, 56, 20), ("🧼", 138, 44, 12), ("🚪", 84, 34, 12)], 'el1'),
        cover_sub="Can I…? Can you…? Em 10 minutos você pede de tudo, como a Eloise",
        cover_say="A Eloise mora num hotel de Nova York e pede tudo à babá. Ela quer a chave, a janela e o elevador. Como pedir em inglês?",
        wrap_recap=[["Can I have my key?", "Posso pegar a minha chave?"], ["Can you open the door?", "Você pode abrir a porta?"],
                    ["Yes, I can.", "Sim, eu posso."], ["No, I can't.", "Não, eu não posso."]],
        teaser=dict(t="The Grand Budapest Hotel", d="Próximo padrão: his e her para falar das coisas dele e dela"),
        cast={"Eloise": ["👧", "#e75480"], "Nanny": ["👵", "#34495e"]},
        lines=[["Eloise", "Nanny, can I have my room key?", "Babá, posso pegar a chave do meu quarto?"],
               ["Nanny", "Yes, you can. Here is your key.", "Sim, pode. Aqui está a sua chave."],
               ["Eloise", "Thanks! Can you open the door?", "Obrigada! Você pode abrir a porta?"],
               ["Nanny", "Sure thing. I can open it.", "Claro. Eu posso abrir."],
               ["Eloise", "Can I open the window?", "Posso abrir a janela?"],
               ["Nanny", "No, you can't. It's cold. Sit on the bed.", "Não, não pode. Está frio. Sente na cama."],
               ["Eloise", "Oh, please! Can I ride the elevator?", "Ah, por favor! Posso andar de elevador?"],
               ["Nanny", "Okay, you can. But wash with soap first!", "Tá bom, pode. Mas lave-se com sabonete antes!"]],
        quiz=[Q("Can Eloise have the key?", "A Eloise pode pegar a chave?", [("✅", "Yes, she can"), ("❌", "No, she can't"), ("🤷", "Maybe")], 0, 1, "Nanny diz: “Yes, you can.”"),
              Q("Can Eloise open the window?", "A Eloise pode abrir a janela?", [("✅", "Yes, she can"), ("❌", "No, she can't"), ("🤷", "Maybe")], 1, 5, "Nanny diz: “No, you can't. It's cold.”"),
              Q("What can Eloise ride?", "O que a Eloise pode andar?", [("🚌", "A bus"), ("🚲", "A bike"), ("🛗", "The elevator")], 2, 7, "Nanny diz: “Okay, you can.”")],
        rdg_q=dict(q="Qual é a resposta curta certa para “Can you open the door?”", o=["Yes, I do.", "Yes, I can.", "Yes, I am."], a=1,
                   why="A resposta curta repete o verbo da pergunta: Can you…? → Yes, I **can**."),
        dictate=[["Can I have my key?", "Posso pegar a minha chave?"], ["Can you open the door?", "Você pode abrir a porta?"],
                 ["Yes, I can.", "Sim, eu posso."], ["No, I can't.", "Não, eu não posso."]],
        produce=PR("A Eloise pergunta: *Can you open the window? Can I have a snack?* **Faça um pedido com Can I…?, uma pergunta com Can you…? e responda com Yes, I can ou No, I can't.**",
                   "Ex.: Can I open the window? Can you ask Nanny? No, I can't.",
                   ["Can I…?", "Can you…?", "Yes, I can."],
                   "Can I open the window? Can you ask Nanny? No, I can't.",
                   ["Fiz um pedido com Can I…?", "Perguntei com Can you…?", "Respondi com I can ou I can't?"],
                   ["\\bcan i\\b[^.!?]*\\?", "\\bcan you\\b[^.!?]*\\?", "\\b(?:yes,?\\s*i can|no,?\\s*i can(?:['’]?t|not))\\b"],
                   [[["Can I have a snack?", "Posso pegar um lanche?"], ["Can I open the window?", "Posso abrir a janela?"]],
                    [["Can you open the door?", "Você pode abrir a porta?"], ["Can you help me?", "Você pode me ajudar?"]],
                    [["Yes, I can.", "Sim, eu posso."], ["No, I can't.", "Não, eu não posso."]]],
                   ["Pedido feito! 🙋", "Boa pergunta! ❓", "Resposta curta certa! ✅"],
                   ["Okay! Yes, you can. Thank you!", "Certo! Sim, pode. Obrigada!"]),
        rs=RSD('bedroom', 'hall', 'lobby2', 'home1', 'kitchen', 'living', 'bath', 'lobby', 'bedroom', 'lobby2', 'hall', 'living', 'lobby1', 'bedroom', 'home1'),
        sc='bedroom')
    X = dict(
        n=7030003, review=True, names=("Eloise", "Nanny"),
        stage=dict(rs='bedroom', chars=[[ELO, 30, 0, 0.95], [NAN, 62, 1, 1.0], ["e:🐶", 88, 1, 0.8]]),
        obra=dict(name="Eloise", kind="📖 Livro ilustrado · 1955", year="1955",
                  text="Livro ilustrado da americana Kay Thompson, com desenhos de Hilary Knight, de 1955. Eloise é uma menina que mora num grande hotel de Nova York, o Plaza, com a babá, o cachorro Weenie e a tartaruga Skipperdee. Ela faz muitos pedidos e muita bagunça.",
                  line=["Can I have a key, please?", "Posso pegar uma chave, por favor? (frase do tema)"],
                  pa=PA('rooftop', ['👧', '🏨', '🐢'], 'g', 1)),
        gancho=["Eloise", "Nanny, can I have my room key?", "Babá, posso pegar a chave do meu quarto?"],
        hot=[H("🚪", 14, 16, "door", "porta", "Can you open the door?", "Você pode abrir a porta?"),
             H("🪟", 40, 14, "window", "janela", "Can I open the window?", "Posso abrir a janela?"),
             H("🛏️", 66, 14, "bed", "cama", "Can I sit on the bed?", "Posso sentar na cama?"),
             H("🧼", 88, 16, "soap", "sabonete", "Can I have soap, please?", "Posso pegar sabonete, por favor?"),
             H("🛗", 12, 82, "elevator", "elevador", "Can I ride the elevator?", "Posso andar de elevador?")],
        gap=[G("___ I have my key?", "Posso pegar a minha chave?", ["Can", "Do", "Am"], 0, "Para pedir licença: **Can** I…?"),
             G("___ you open the door?", "Você pode abrir a porta?", ["Are", "Can", "Is"], 1, "Para pedir ajuda: **Can** you…?"),
             G("Yes, you ___.", "Sim, você pode.", ["do", "are", "can"], 2, "A resposta curta repete o verbo: Yes, you **can**."),
             G("No, I ___.", "Não, eu não posso.", ["can't", "don't", "isn't"], 0, "Negativa: **can't** (cannot).")],
        trap=[T(["Can you opens the door?", "Can you open the door?", "Can you to open the door?"], 1, "Depois de **can**, o verbo fica sem -s e sem **to**: Can you **open**…?"),
              T(["Yes, I can open.", "Yes, I cans.", "Yes, I can."], 2, "A resposta curta é **Yes, I can.** O **can** nunca ganha -s.")],
        sticker=dict(title="Eloise e a Babá", sub="Eloise · 1955", rs='bedroom', chars=[[ELO, 34, 0, 1.0], [NAN, 68, 1, 1.0]]),
        speakers={"Eloise": ELO, "Nanny": NAN},
        rule=dict(
            who=ELO, head="Can I…? Can you…?", sub="Can não muda e vem antes do outro verbo.",
            say=["Can I have my key? Can you open the door?", "Posso pegar a minha chave? Você pode abrir a porta?"],
            formula=[dict(from_=[["I", 0], ["open", 1], ["the door.", 3]], to=[["Can", 2], ["I", 0], ["open", 1], ["the door?", 3]], say="Can I open the door?", note="**Can** vem na frente. O verbo **open** fica igual."),
                     dict(from_=[["You", 0], ["open", 1], ["the door.", 3]], to=[["Can", 2], ["you", 0], ["open", 1], ["the door?", 3]], say="Can you open the door?", note="Com **you** também: **Can you** open…? O verbo não leva -s.")],
            uses=[dict(ico="🙋", tag="Pedir licença", en="Can I have my key?", pt="Posso pegar a minha chave?"),
                  dict(ico="🤝", tag="Pedir ajuda", en="Can you open the door?", pt="Você pode abrir a porta?"),
                  dict(ico="✅", tag="Responder sim", en="Yes, I can. / Yes, you can.", pt="Sim, eu posso. / Sim, você pode."),
                  dict(ico="❌", tag="Responder não", en="No, I can't.", pt="Não, eu não posso.")],
            rules=[dict(tag="Can I", c=0, text="Para **pedir licença**: posso fazer isso?", ex="Can I open the window?"),
                   dict(tag="Can you", c=1, text="Para **pedir ajuda** a alguém.", ex="Can you open the door?"),
                   dict(tag="sem -s", c=2, text="Depois de **can** o verbo fica no básico. Nada de -s nem **to**.", ex="✗ Can she opens  →  ✓ Can she open")],
            tips=["Em português “posso?” e “pode?” são formas do mesmo verbo. Em inglês é sempre **Can** + I ou you + verbo."]),
        mission_ic="🙋")
    XT = dict(
        exp=[EXP("👍", "Of course!", "Expressão", "Claro!", "Para dizer **sim** de forma simpática a um pedido.", ["Can I have the key? Of course!", "Posso pegar a chave? Claro!"]),
             EXP("😌", "No worries.", "Informal", "Sem problema.", "Para tranquilizar alguém: **tudo bem, não foi nada**.", ["Sorry, Nanny! No worries.", "Desculpe, babá! Sem problema."]),
             EXP("⏱️", "Just a minute.", "Expressão", "Só um minutinho.", "Para pedir que alguém **espere um pouco**.", ["Just a minute, Eloise.", "Só um minutinho, Eloise."]),
             EXP("🙋", "Can I help you?", "Expressão", "Posso ajudar?", "Para **oferecer ajuda** a quem parece precisar.", ["Can I help you, Eloise?", "Posso ajudar você, Eloise?"])],
        exp_scene=dict(rs='bedroom', lines=[["Nanny", "**Can I help you**, Eloise?", "Posso ajudar você, Eloise?"],
                                            ["Eloise", "Yes! Can you open the window?", "Sim! Você pode abrir a janela?"],
                                            ["Nanny", "**Just a minute**.", "Só um minutinho."],
                                            ["Eloise", "Thanks, Nanny. Can I ride the elevator?", "Obrigada, babá. Posso andar de elevador?"],
                                            ["Nanny", "**Of course**! Go with Weenie.", "Claro! Vá com o Weenie."],
                                            ["Eloise", "Thanks! **No worries**, Nanny. I'm fast!", "Obrigada! Sem preocupação, babá. Eu sou rápida!"]]),
        lab=dict(short="a de bag", title="Laboratório de sons: o “a” de bag",
                 say="Em bag, can e man, o “a” inglês não é “á” nem “é”. Fica no meio! Vamos treinar.",
                 intro=dict(what="O **a** de **bag**, **can** e **man** é um som aberto e curto, entre o “é” e o “á” do português.",
                            how="Abra bem a boca, como se fosse dizer “é”, e baixe o queixo. A língua fica baixa. Não feche a boca num “e” pequeno.",
                            pt="Muitos brasileiros dizem “beg” (implorar) em vez de **bag** (mala). Abra mais a boca para o **a**!"),
                 ex=[["bag", "BÉÉG", "mala", "boca bem aberta"], ["can", "KÉN", "poder", "queixo para baixo"], ["man", "MÉN", "homem", "boca aberta, língua baixa"]],
                 pairs=[["bag", "beg", "mala × implorar"], ["pan", "pen", "panela × caneta"], ["bad", "bed", "ruim × cama"]],
                 tip="Para o a de bag, pense em “é” com a boca bem aberta, como no médico: “abra a boca”.",
                 phrase=["Can I have my bag?", "Posso pegar a minha mala?"],
                 rounds=[RND("bag", ["bag", "beg"], 0, "**bag** (mala) tem o “a” aberto. **Beg** (implorar) tem o “e”."),
                         RND("pen", ["pan", "pen"], 1, "**pen** (caneta) tem o “e”. **Pan** (panela) tem o “a” aberto."),
                         RND("bad", ["bed", "bad"], 1, "**bad** (ruim) tem o “a” aberto. **Bed** (cama) tem o “e”.")]),
        hunt=[HW("pan", ["pan", "pen"], 0, "**pan** (panela) tem o “a” aberto."),
              HP("bed", ["👜", "🛏️", "🖊️"], 1, "**bed** = cama, com o “e”."),
              HW("beg", ["bag", "beg"], 1, "**beg** (implorar) tem o “e”."),
              HW("bad", ["bad", "bed"], 0, "**bad** (ruim) tem o “a” aberto.")])
    VB = dict(title="Verbos do hotel", tip="Quatro verbos: sit, wait, see e love.",
              items=[VBI("sit", "🪑", "sentar", "I sit on the bed.", "Eloise sit**s** on the bed.", ["I sit on the bed.", "Eu sento na cama."], "**sit** = sentar. Com he/she: **sits**."),
                     VBI("wait", "⏳", "esperar", "I wait for the elevator.", "Nanny wait**s** for the elevator.", ["I wait for the elevator.", "Eu espero o elevador."], "**wait** = esperar. Com he/she: **waits**."),
                     VBI("see", "👀", "ver", "I see the window.", "She see**s** the street.", ["I see the window.", "Eu vejo a janela."], "**see** = ver. Com he/she: **sees**."),
                     VBI("love", "❤️", "adorar", "I love the hotel.", "Eloise love**s** the hotel.", ["I love the hotel.", "Eu adoro o hotel."], "**love** = adorar, amar. Com he/she: **loves**.")])
    MR = dict(
        mold=[MOLD("Pedir licença com Can I…?", [("pergunta", [("Can I", "posso eu")]),
                                                  ("pedido", [("have a key", "pegar uma chave"), ("open the window", "abrir a janela"), ("sit on the bed", "sentar na cama"), ("use the soap", "usar o sabonete"), ("ride the elevator", "andar de elevador")])], ["?", "?"]),
              MOLD("Pedir ajuda com Can you…?", [("pergunta", [("Can you", "você pode")]),
                                                  ("pedido", [("open the door", "abrir a porta"), ("close the window", "fechar a janela"), ("wait here", "esperar aqui"), ("help me", "me ajudar")])], ["?", "?"]),
              MOLD("Responder", [("resposta", [("Yes, I can.", "Sim, eu posso."), ("Yes, you can.", "Sim, você pode."), ("No, I can't.", "Não, eu não posso."), ("No, you can't.", "Não, você não pode.")]),
                                 ("depois", [("Sorry.", "Desculpe."), ("Thanks!", "Obrigado!"), ("Of course!", "Claro!")])], ["", ""])],
        speak=[["Can I have my key? Of course!", "Posso pegar a minha chave? Claro!"], ["Can you open the door? Just a minute.", "Você pode abrir a porta? Só um minutinho."]],
        trap=[TR("“Can I help you?” quer dizer…", ["Posso ajudar você?", "Você pode me ajudar?", "Eu estou ajudando?"], 0, "**Can I help you?** = posso ajudar você? (quem oferece ajuda)", "Can I help you?"),
              TR("Qual frase está certa?", ["Can she opens the door?", "Can she open the door?", "Can she to open the door?"], 1, "Depois de **can**, o verbo fica sem -s e sem **to**: Can she **open**…?")],
        gap=[MG("___ I have a key?", "Posso pegar uma chave?", ["Do", "Can", "Am"], 1, "Para pedir licença: **Can** I…?", "Can I have a key?"),
             MG("No ___, Eloise. It's fine.", "Sem problema, Eloise. Está tudo bem.", ["worries", "worry", "worried"], 0, "**No worries.** = sem problema.", "No worries, Eloise.")],
        expq=[EQ("Você quer dizer “sem problema” de forma informal.", ["Of course!", "Just a minute.", "No worries."], 2, "**No worries.** = sem problema."),
              EQ("Você quer oferecer ajuda a um hóspede.", ["Can I help you?", "No worries.", "Of course!"], 0, "**Can I help you?** = posso ajudar?"),
              EQ("Você precisa de um minuto antes de ajudar.", ["No worries.", "Just a minute.", "Can I help you?"], 1, "**Just a minute.** = só um minutinho.")],
        missions=[MS("🧼", "Peça ao hotel", "Peça coisas e ajuda com educação.",
                     "Você está no hotel. **Peça sabonete com Can I have…?, peça para abrirem a janela com Can you…? e diga please.**",
                     ["Can I have", "Can you", "please"],
                     "Can I have soap, please? Can you open the window?",
                     ["Pedi algo com Can I have…?", "Pedi ajuda com Can you…?", "Fui educado com please?"],
                     ["\\bcan i have\\b", "\\bcan you\\b[^.!?]*\\?", "\\bplease\\b"],
                     [[["Can I have soap?", "Posso pegar sabonete?"]], [["Can you open the window?", "Você pode abrir a janela?"]], [["Please.", "Por favor."]]],
                     ["Pedido feito! 🧼", "Ajuda pedida! 🤝", "Educação! 🙏"],
                     ["Of course! Here you are.", "Claro! Aqui está."]),
                  MS("🛗", "Pode ou não pode?", "Responda com respostas curtas.",
                     "Um amigo pergunta: *Can you open the door? Can you ride the elevator?* **Responda uma com Yes, I can e outra com No, I can't, e termine com uma expressão simpática.**",
                     ["Yes, I can.", "No, I can't."],
                     "Yes, I can open the door. No, I can't ride the elevator. No worries!",
                     ["Disse Yes, I can?", "Disse No, I can't?", "Usei uma expressão simpática?"],
                     ["\\byes,?\\s*i can\\b", "\\bno,?\\s*i can(?:['’]?t|not)\\b", "\\b(?:of course|no worries|thank(?:s| you)|please)\\b"],
                     [[["Yes, I can.", "Sim, eu posso."]], [["No, I can't.", "Não, eu não posso."]], [["No worries!", "Sem problema!"], ["Of course!", "Claro!"]]],
                     ["Sim! ✅", "Não! ❌", "Simpatia! 😊"],
                     ["Great! Thanks for your help!", "Ótimo! Obrigado pela ajuda!"])])
    CX = [CXI("Knock, knock! Open the ___, please.", "Toc, toc! Abra a porta, por favor.", ["door", "bed", "lamp"]),
          CXI("It's warm. Open the ___ and let the air in.", "Está quente. Abra a janela e deixe o ar entrar.", ["window", "soap", "elevator"]),
          CXI("I'm tired. I sleep in my ___.", "Estou cansado. Eu durmo na minha cama.", ["bed", "door", "soap"]),
          CXI("Wash your hands with ___.", "Lave as mãos com sabonete.", ["soap", "lamp", "window"]),
          CXI("The room is high up. Take the ___, not the stairs.", "O quarto é bem no alto. Pegue o elevador, não a escada.", ["elevator", "bed", "door"]),
          CXI("It's dark in the room. Turn on the ___.", "Está escuro no quarto. Ligue o abajur.", ["lamp", "soap", "window"])]
    return EP(B, X, XT, VB, MR, CX)


EPS = [E14(), E15(), E16()]
