# B1 · episódios 275–280: phrasal verbs com take, collocations com keep, phrasal verbs com give.
from v3.b1h import *

from v3.ovrb1 import install
EPS = []
install(globals(), 'S')

def mk(n, title, sub, pat, why, names, ids, rs, obra, scenes, cover, teaser, rule, fm, vocab, lab, verbs, mold, prod, m2, hot, gaps, traps, lines, quiz, exps):
    return S(n=n, title=title, sub=sub, pattern=pat, why=why, names=names, ids=ids, rs=rs, obra=(obra, obra),
             hot=hot, gaps=gaps, traps=traps, rule=rule, fm=fm, cover=cover, vocab=vocab, lines=lines, quiz=quiz,
             teaser=teaser, exps=exps, lab=lab, verbs=verbs, mold=mold, prod=prod, m2=m2, scenes=scenes)

# ---------- take ----------
TK_VOCAB = [('🛫', 'take off', 'decolar', 'Soa como “TÊIK ÓF”.'), ('🎨', 'take up', 'começar (hobby)', 'Soa como “TÊIK ÂP”.'), ('👔', 'take over', 'assumir', 'Soa como “TÊIK ÔU-ver”.'),
            ('👨‍👦', 'take after', 'puxar (família)', 'Soa como “TÊIK ÉF-ter”.'), ('↩️', 'take back', 'devolver', 'Soa como “TÊIK BÉK”.'), ('📤', 'take out', 'tirar', 'Soa como “TÊIK ÁUT”.')]
TK_LAB = dict(short='tk', title='Laboratório de sons: take, plane e after', pt='a soa êi; a soa é em after; ou soa áu.', tip='Em take, o a soa êi.',
              words=[('take', 'TÊIK', 'pegar', 'a = êi', 'tick', 'TÍK'), ('plane', 'PLÊIN', 'avião', 'a = êi', 'plan', 'PLÉN'), ('after', 'ÉF-ter', 'depois', 'a = é', 'offer', 'Ó-fer')])
TK_VERBS = [('take', '🛫', 'decolar', 'The plane will take off.', 'The plane will take of.', 'It took off.', 'Decolou.', 'take **off**.'),
            ('take', '🎨', 'começar', 'She took up painting.', 'She took on painting up.', 'I took up.', 'Comecei.', 'take **up** + hobby.'),
            ('take', '👔', 'assumir', 'He took over the shop.', 'He took the shop over to.', 'I took over.', 'Assumi.', 'take **over**.'),
            ('take', '👨‍👦', 'puxar', 'She takes after her mum.', 'She takes like her mum.', 'I take after.', 'Eu puxo.', 'take **after** + família.')]

def tk(n, title, sub, pat, why, names, ids, rs, scenes, cover, teaser, rule, fm, mold, prod, m2, hot, gaps, traps, lines, quiz, exps):
    return mk(n, title, sub, pat, why, names, ids, rs, 'Top Gun', scenes, cover, teaser, rule, fm, TK_VOCAB, TK_LAB, TK_VERBS, mold, prod, m2, hot, gaps, traps, lines, quiz, exps)

EPS.append(tk(82177, 'Take Off, Take Up', "aprender phrasal verbs com take: take off, take up, take over, take after (decolar, hobby, assumir)",
    "phrasal verbs: take off · take up · take over · take after", "Hoje você aprende phrasal verbs com take: The plane will take off. She took up painting. He took over the shop. She takes after her mum.",
    ('Man', 'Woman'), ['tom', 'polly'], 'cafe2', ['cafe2', 'street', 'lobby1', 'park', 'hall', 'living'],
    ('Take Off, Take Up: em 10 minutos você decola e começa hobbies em inglês', 'No café, o piloto e a mulher falam de hobbies e da família.'), ('Mais com take', 'Próximo: Phrasal verbs com take'),
    ('Take', 'Quatro sentidos novos.', 'Em português “o avião decola”. Em inglês: **the plane takes off**.'),
    [('Take off', 'The plane will', 'take off.', 'The plane will take off.', 'take off.'), ('Take up', 'She', 'took up painting.', 'She took up painting.', 'take up.')],
    [('Take off', 'The plane will', 'o avião vai', [(' take off.', ' decolar.'), (' take off soon.', ' decolar logo.'), (' take off at ten.', ' decolar às dez.')]), ('Take up', 'She took up', 'ela começou', [(' painting.', ' a pintar.'), (' tennis.', ' tênis.'), (' yoga.', ' yoga.')]), ('Take after', 'She takes after', 'ela puxa', [(' her mum.', ' a mãe.'), (' her dad.', ' o pai.'), (' her gran.', ' a avó.')])],
    ('🛫', 'Take', 'Use take off, take up e take after', 'Fale. **Diga o avião vai decolar, ela começou a pintar e ela puxa a mãe.**', 'take after', 'The plane will take off. She took up painting. She takes after her mum.',
     [('Usei take off?', r"\btake\s+off\b", 'The plane will take off.', 'O avião vai decolar.', 'Off! 🛫'), ('Usei take up?', r"\btook\s+up\b", 'She took up painting.', 'Ela começou a pintar.', 'Up! 🎨'), ('Usei take after?', r"\btakes\s+after\b", 'She takes after her mum.', 'Ela puxa a mãe.', 'After! 👨‍👦')]),
    ('📤', 'Fixas', 'Use take it easy, take your time e take a break', 'Fale. **Diga vá com calma, sem pressa e faça uma pausa.**', 'take a break', 'Take it easy. Take your time. Take a break.',
     [('Disse take it easy?', r"\btake\s+it\s+easy\b", 'Take it easy.', 'Vá com calma.', 'Easy! 😌'), ('Disse take your time?', r"\btake\s+your\s+time\b", 'Take your time.', 'Sem pressa.', 'Time! ⏳'), ('Disse take a break?', r"\btake\s+a\s+break\b", 'Take a break.', 'Faça uma pausa.', 'Break! ☕')]),
    [('🛫', 'take off', 'decolar', 'The plane will take off.', 'O avião vai decolar.'), ('🎨', 'take up', 'começar', 'She took up painting.', 'Ela começou a pintar.'), ('👔', 'take over', 'assumir', 'He took over the shop.', 'Ele assumiu a loja.'), ('👨‍👦', 'take after', 'puxar', 'She takes after her mum.', 'Ela puxa a mãe.'), ('↩️', 'take back', 'devolver', 'I will take it back.', 'Vou devolver.')],
    [('The plane will take ___.', 'O avião vai decolar.', ['off', 'out', 'of'], 0, 'take **off**.'), ('She took ___ painting.', 'Ela começou a pintar.', ['up', 'off', 'in'], 0, 'took **up**.'), ('He took ___ the shop.', 'Ele assumiu a loja.', ['over', 'out', 'in'], 0, 'took **over**.'), ('She takes ___ her mum.', 'Ela puxa a mãe.', ['after', 'for', 'like to'], 0, 'takes **after**.')],
    [('Qual frase está certa?', ['She takes after her mum.', 'She takes like her mum.', 'She take after her mum.'], 0, 'takes after.'), ('Qual está certa?', ['She took up painting.', 'She took painting up.', 'She take up painting.'], 0, 'took up painting.')],
    [['Man', 'The plane will take off in ten minutes.', 'O avião vai decolar em dez minutos.'], ['Woman', 'Are you nervous?', 'Você está nervoso?'], ['Man', 'No. Take it easy.', 'Não. Vá com calma.'], ['Woman', 'My daughter took up painting.', 'Minha filha começou a pintar.'],
     ['Man', 'Does she take after you?', 'Ela puxa você?'], ['Woman', 'No, she takes after her father.', 'Não, ela puxa o pai.'], ['Man', 'He took over the shop, right?', 'Ele assumiu a loja, certo?'], ['Woman', 'Yes.', 'Sim.']],
    [('When will the plane take off?', 'Quando o avião decola?', [('🔟', 'In ten minutes'), ('1️⃣', 'In one hour'), ('🌙', 'Tonight')], 0, 0, 'Diz: “in ten minutes.”'), ('What did her daughter take up?', 'O que a filha começou?', [('🎨', 'Painting'), ('🎾', 'Tennis'), ('🎵', 'Music')], 0, 3, 'Diz: “took up painting.”'),
     ('Who does she take after?', 'Quem ela puxa?', [('👨', 'Her father'), ('👩', 'Her mother'), ('👵', 'Her gran')], 0, 5, 'Diz: “after her father.”')],
    [('😌', 'Take it easy', 'Vá com calma', 'relaxar', 'Take it easy.', 'Vá com calma.'), ('⏳', 'Take your time', 'Sem pressa', 'tranquilizar', 'Take your time.', 'Sem pressa.'), ('☕', 'Take a break', 'Faça uma pausa', 'descansar', 'Take a break.', 'Faça uma pausa.'), ('🧠', 'Take it in', 'Absorver', 'entender', 'I take it in.', 'Eu absorvo.')]))

EPS.append(tk(7082177, 'Phrasal verbs com take', "mais phrasal verbs com take: take back, take out, take in, take apart (devolver, tirar, absorver)",
    "phrasal verbs: take back · take out · take in · take apart", "Hoje você aprende mais quatro com take: I will take it back. Take out the trash. He could not take it in. They took the clock apart.",
    ('Girl', 'Man'), ['polly', 'tom'], 'shop', ['shop', 'kitchen', 'home1', 'living', 'street', 'cafe2'],
    ('Phrasal verbs com take: em 10 minutos você devolve, tira e desmonta em inglês', 'Na loja, a menina e o homem trocam um relógio quebrado.'), ('Mais com take', 'Próximo: Guardar segredo'),
    ('Take', 'Mais quatro sentidos.', 'Em português “vou devolver”. Em inglês: **I will take it back**.'),
    [('Take back', 'I will', 'take it back.', 'I will take it back.', 'take it back.'), ('Take out', 'Take', 'out the trash.', 'Take out the trash.', 'take out.')],
    [('Take back', 'I will take', 'vou devolver', [(' it back.', ' isso.'), (' them back.', ' eles.'), (' it back today.', ' hoje.')]), ('Take out', 'Take out', 'tire', [(' the trash.', ' o lixo.'), (' the clock.', ' o relógio.'), (' your phone.', ' o celular.')]), ('Take apart', 'They took', 'eles desmontaram', [(' the clock apart.', ' o relógio.'), (' the toy apart.', ' o brinquedo.'), (' it apart.', ' isso.')])],
    ('↩️', 'Take', 'Use take back, take out e take apart', 'Fale. **Diga vou devolver, tire o lixo e eles desmontaram o relógio.**', 'take apart', 'I will take it back. Take out the trash. They took the clock apart.',
     [('Usei take back?', r"\btake\s+it\s+back\b", 'I will take it back.', 'Vou devolver.', 'Back! ↩️'), ('Usei take out?', r"\btake\s+out\b", 'Take out the trash.', 'Tire o lixo.', 'Out! 📤'), ('Usei take apart?', r"\btook\s+the\s+clock\s+apart\b", 'They took the clock apart.', 'Eles desmontaram o relógio.', 'Apart! 🔧')]),
    ('📤', 'Fixas', 'Use take part, take place e take care', 'Fale. **Diga participar, acontecer e cuide-se.**', 'take care', 'I take part. It takes place today. Take care!',
     [('Disse take part?', r"\btake\s+part\b", 'I take part.', 'Eu participo.', 'Part! 🙋'), ('Disse take place?', r"\btakes\s+place\b", 'It takes place today.', 'Acontece hoje.', 'Place! 📅'), ('Disse take care?', r"\btake\s+care\b", 'Take care!', 'Cuide-se!', 'Care! 👋')]),
    [('↩️', 'take back', 'devolver', 'I will take it back.', 'Vou devolver.'), ('📤', 'take out', 'tirar', 'Take out the trash.', 'Tire o lixo.'), ('🧠', 'take in', 'absorver', 'He could not take it in.', 'Ele não conseguiu absorver.'), ('🔧', 'take apart', 'desmontar', 'They took the clock apart.', 'Eles desmontaram o relógio.'), ('🛫', 'take off', 'tirar (roupa)', 'Take off your coat.', 'Tire o casaco.')],
    [('I will take it ___.', 'Vou devolver.', ['back', 'up', 'by'], 0, 'take it **back**.'), ('Take ___ the trash.', 'Tire o lixo.', ['out', 'up', 'on'], 0, 'take **out**.'), ('He could not take it ___.', 'Ele não conseguiu absorver.', ['in', 'at', 'to'], 0, 'take it **in**.'), ('They took the clock ___.', 'Eles desmontaram o relógio.', ['apart', 'away to', 'over'], 0, 'took it **apart**.')],
    [('Qual frase está certa?', ['I will take it back.', 'I will take back it.', 'I will taking it back.'], 0, 'take it back.'), ('Qual está certa?', ['They took the clock apart.', 'They took apart the clock apart.', 'They take the clock apart yesterday.'], 0, 'took it apart.')],
    [['Girl', 'This clock is broken. I will take it back.', 'Este relógio está quebrado. Vou devolver.'], ['Man', 'Why?', 'Por quê?'], ['Girl', 'They took it apart and it did not work.', 'Eles o desmontaram e não funcionou.'], ['Man', 'Take out the receipt.', 'Tire o recibo.'],
     ['Girl', 'Here it is.', 'Aqui está.'], ['Man', 'Take your time.', 'Sem pressa.'], ['Girl', 'Thank you. Take care!', 'Obrigada. Cuide-se!'], ['Man', 'You too.', 'Você também.']],
    [('What does she do with the clock?', 'O que faz com o relógio?', [('↩️', 'Takes it back'), ('🎁', 'Gives it'), ('🔥', 'Burns it')], 0, 0, 'Diz: “take it back.”'), ('What must she take out?', 'O que deve tirar?', [('🧾', 'The receipt'), ('🗑️', 'The trash'), ('📱', 'The phone')], 0, 3, 'Diz: “Take out the receipt.”'),
     ('What does she say at the end?', 'O que ela diz no fim?', [('👋', 'Take care'), ('😡', 'Go away'), ('🤷', 'Nothing')], 0, 6, 'Diz: “Take care!”')],
    [('🙋', 'Take part', 'Participar', 'envolver-se', 'I take part.', 'Eu participo.'), ('📅', 'Take place', 'Acontecer', 'realizar-se', 'It takes place today.', 'Acontece hoje.'), ('👋', 'Take care', 'Cuide-se', 'despedir', 'Take care!', 'Cuide-se!'), ('🔧', 'Take a look', 'Dar uma olhada', 'olhar', 'Take a look.', 'Dê uma olhada.')]))

# ---------- keep ----------
KP_VOCAB = [('🤐', 'sworn to secrecy', 'jurado ao silêncio', 'Soa como “SUÓRN tu SÍ-kri-si”.'), ('🗞️', 'rumour mill', 'fábrica de boatos', 'Soa como “RU-mer MÍL”.'), ('🕵️', 'tip-off', 'aviso secreto', 'Soa como “TÍP-óf”.'),
            ('👎', 'snitch', 'dedo-duro', 'Soa como “SNÍTCH”.'), ('🧒', 'tattletale', 'fofoqueiro', 'Soa como “TÉ-tol-têil”.'), ('👂', 'eavesdrop', 'escutar escondido', 'Soa como “IVZ-dróp”.')]
KP_LAB = dict(short='kp', title='Laboratório de sons: keep, secret e snitch', pt='ee soa i; c soa k; tch soa tch.', tip='Em keep, o ee soa i longo.',
              words=[('keep', 'KIP', 'manter', 'ee = i', 'kip', 'KÍP'), ('secret', 'SI-krit', 'segredo', 'e = i', 'sacred', 'SÊI-krid'), ('snitch', 'SNÍTCH', 'dedo-duro', 'tch', 'sketch', 'SKÉTCH')])
KP_VERBS = [('keep', '🤫', 'guardar', 'Can you keep a secret?', 'Can you hold a secret?', 'I kept.', 'Guardei.', 'keep a **secret**.'),
            ('keep', '📞', 'manter contato', 'Keep in touch.', 'Keep on touch.', 'I kept.', 'Mantive.', 'keep in **touch**.'),
            ('keep', '😌', 'manter', 'Keep calm.', 'Keep calmly.', 'I kept.', 'Mantive.', 'keep **calm**.'),
            ('keep', '🏃', 'continuar', 'Keep going!', 'Keep to go!', 'I kept.', 'Continuei.', 'keep **going**.')]

def kp(n, title, sub, pat, why, names, ids, rs, scenes, cover, teaser, rule, fm, mold, prod, m2, hot, gaps, traps, lines, quiz, exps):
    return mk(n, title, sub, pat, why, names, ids, rs, 'Pretty Little Liars', scenes, cover, teaser, rule, fm, KP_VOCAB, KP_LAB, KP_VERBS, mold, prod, m2, hot, gaps, traps, lines, quiz, exps)

EPS.append(kp(930039, 'Keep It a Secret', "collocations com keep: keep a secret, keep in touch, keep calm, keep going (snitch, rumour mill)",
    "collocations: keep a secret · keep in touch · keep calm · keep going", "Hoje você aprende collocations com keep: Can you keep a secret? Keep in touch. Keep calm. Keep going!",
    ('Girl', 'Boy'), ['polly', 'tommy'], 'school', ['school', 'hall', 'yard', 'cafe2', 'park', 'street'],
    ('Keep It a Secret: em 10 minutos você guarda segredos e mantém contato em inglês', 'Na escola, a menina e o menino trocam segredos e boatos.'), ('Mais com keep', 'Próximo: Guardar segredo'),
    ('Keep', 'Collocations muito úteis.', 'Em português “guardar um segredo”. Em inglês: **keep a secret**.'),
    [('Secret', 'Can you', 'keep a secret?', 'Can you keep a secret?', 'keep a secret.'), ('Touch', 'Please', 'keep in touch.', 'Please keep in touch.', 'keep in touch.')],
    [('Keep a secret', 'Can you keep', 'você consegue guardar', [(' a secret?', ' um segredo?'), (' it quiet?', ' isso em silêncio?'), (' it to yourself?', ' isso só para você?')]), ('Keep in touch', 'Please keep', 'por favor, mantenha', [(' in touch.', ' contato.'), (' in touch with us.', ' contato conosco.'), (' calm.', ' a calma.')]), ('Keep going', 'Keep', 'continue', [(' going!', ' firme!'), (' trying!', ' tentando!'), (' smiling!', ' sorrindo!')])],
    ('🤫', 'Keep', 'Use keep a secret, keep in touch e keep going', 'Fale. **Diga você guarda um segredo, mantenha contato e continue firme.**', 'keep in touch', 'Can you keep a secret? Keep in touch. Keep going!',
     [('Usei keep a secret?', r"\bkeep\s+a\s+secret\b", 'Can you keep a secret?', 'Você guarda um segredo?', 'Secret! 🤫'), ('Usei keep in touch?', r"\bkeep\s+in\s+touch\b", 'Keep in touch.', 'Mantenha contato.', 'Touch! 📞'), ('Usei keep going?', r"\bkeep\s+going\b", 'Keep going!', 'Continue firme!', 'Going! 🏃')]),
    ('👂', 'Fixas', 'Use keep an eye on, keep it down e keep quiet', 'Fale. **Diga fique de olho, fale baixo e fique quieto.**', 'keep an eye on', 'Keep an eye on him. Keep it down. Keep quiet.',
     [('Disse keep an eye on?', r"\bkeep\s+an\s+eye\s+on\b", 'Keep an eye on him.', 'Fique de olho nele.', 'Eye! 👀'), ('Disse keep it down?', r"\bkeep\s+it\s+down\b", 'Keep it down.', 'Fale baixo.', 'Down! 🔉'), ('Disse keep quiet?', r"\bkeep\s+quiet\b", 'Keep quiet.', 'Fique quieto.', 'Quiet! 🤐')]),
    [('🤫', 'keep a secret', 'guardar segredo', 'Can you keep a secret?', 'Você guarda um segredo?'), ('📞', 'keep in touch', 'manter contato', 'Keep in touch.', 'Mantenha contato.'), ('😌', 'keep calm', 'manter a calma', 'Keep calm.', 'Mantenha a calma.'), ('🏃', 'keep going', 'continuar', 'Keep going!', 'Continue firme!'), ('👎', 'snitch', 'dedo-duro', 'He is a snitch.', 'Ele é um dedo-duro.')],
    [('Can you keep a ___?', 'Você guarda um segredo?', ['secret', 'secretly', 'secrecy'], 0, 'keep a **secret**.'), ('Keep in ___.', 'Mantenha contato.', ['touch', 'touching', 'contact on'], 0, 'keep in **touch**.'), ('Keep ___.', 'Mantenha a calma.', ['calm', 'calmly', 'calming'], 0, 'keep **calm**.'), ('Keep ___!', 'Continue firme!', ['going', 'to go', 'gone'], 0, 'keep **going**.')],
    [('Qual frase está certa?', ['Can you keep a secret?', 'Can you hold a secret?', 'Can you keeping a secret?'], 0, 'keep a secret.'), ('Qual está certa?', ['Keep in touch.', 'Keep on touch.', 'Keep at touch.'], 0, 'in touch.')],
    [['Girl', 'Can you keep a secret?', 'Você consegue guardar um segredo?'], ['Boy', 'Of course. I am not a snitch.', 'Claro. Não sou dedo-duro.'], ['Girl', 'I heard it from the rumour mill.', 'Ouvi na fábrica de boatos.'], ['Boy', 'Keep it down. Someone may eavesdrop.', 'Fale baixo. Alguém pode escutar.'],
     ['Girl', 'Keep calm. Nobody is here.', 'Calma. Não há ninguém.'], ['Boy', 'Keep an eye on the door.', 'Fique de olho na porta.'], ['Girl', 'Keep in touch after school.', 'Mantenha contato depois da aula.'], ['Boy', 'I will.', 'Vou manter.']],
    [('What does she ask?', 'O que ela pede?', [('🤫', 'To keep a secret'), ('🍕', 'Pizza'), ('📚', 'A book')], 0, 0, 'Diz: “keep a secret?”'), ('Is he a snitch?', 'Ele é dedo-duro?', [('🙅', 'No'), ('✅', 'Yes'), ('🤷', 'Unknown')], 0, 1, 'Diz: “I am not a snitch.”'),
     ('What must he watch?', 'O que ele deve vigiar?', [('🚪', 'The door'), ('🪟', 'The window'), ('🚗', 'The car')], 0, 5, 'Diz: “eye on the door.”')],
    [('👀', 'Keep an eye on', 'Ficar de olho', 'vigiar', 'Keep an eye on him.', 'Fique de olho nele.'), ('🔉', 'Keep it down', 'Falar baixo', 'silêncio', 'Keep it down.', 'Fale baixo.'), ('🤐', 'Keep quiet', 'Ficar quieto', 'calar', 'Keep quiet.', 'Fique quieto.'), ('🤫', 'Keep it under your hat', 'Guardar segredo', 'sigilo', 'Keep it under your hat.', 'Guarde segredo.')]))

EPS.append(kp(7930039, 'Guardar segredo', "collocations com keep: keep up, keep away, keep off, keep on, keep out (tip-off, tattletale)",
    "keep + partícula: keep up · keep away · keep off · keep on", "Hoje você aprende keep com partícula: Keep up the good work. Keep away from him. Keep off the grass. Keep on trying.",
    ('Man', 'Woman'), ['tom', 'misshoney'], 'school', ['school', 'park', 'hall', 'cafe2', 'yard', 'street'],
    ('Guardar segredo: em 10 minutos você usa keep com partículas', 'Na escola, o professor e a diretora combinam regras e avisos.'), ('Mais com keep', 'Próximo: Phrasal verbs com give'),
    ('Keep + partícula', 'Keep up, away, off, on.', 'Em português “continue assim”. Em inglês: **keep up the good work**.'),
    [('Keep up', 'Keep up', 'the good work.', 'Keep up the good work.', 'keep up.'), ('Keep off', 'Keep off', 'the grass.', 'Keep off the grass.', 'keep off.')],
    [('Keep up', 'Keep up', 'continue com', [(' the good work.', ' o bom trabalho.'), (' the pace.', ' o ritmo.'), (' the effort.', ' o esforço.')]), ('Keep away', 'Keep away', 'fique longe', [(' from him.', ' dele.'), (' from the road.', ' da estrada.'), (' from fire.', ' do fogo.')]), ('Keep off', 'Keep off', 'não pise em', [(' the grass.', ' a grama.'), (' the stage.', ' o palco.'), (' the ice.', ' o gelo.')])],
    ('🚧', 'Avisos', 'Use keep up, keep away e keep off', 'Fale. **Diga continue o bom trabalho, fique longe dele e não pise na grama.**', 'keep off', 'Keep up the good work. Keep away from him. Keep off the grass.',
     [('Usei keep up?', r"\bkeep\s+up\b", 'Keep up the good work.', 'Continue o bom trabalho.', 'Up! 👍'), ('Usei keep away?', r"\bkeep\s+away\b", 'Keep away from him.', 'Fique longe dele.', 'Away! 🚫'), ('Usei keep off?', r"\bkeep\s+off\b", 'Keep off the grass.', 'Não pise na grama.', 'Off! 🌱')]),
    ('👂', 'Fixas', 'Use keep on trying, keep out e keep track', 'Fale. **Diga continue tentando, proibida a entrada e acompanhar.**', 'keep track', 'Keep on trying. Keep out! Keep track of time.',
     [('Disse keep on?', r"\bkeep\s+on\s+trying\b", 'Keep on trying.', 'Continue tentando.', 'On! 🔁'), ('Disse keep out?', r"\bkeep\s+out\b", 'Keep out!', 'Proibida a entrada!', 'Out! 🚪'), ('Disse keep track?', r"\bkeep\s+track\b", 'Keep track of time.', 'Acompanhe o tempo.', 'Track! ⏱️')]),
    [('👍', 'keep up', 'manter', 'Keep up the good work.', 'Continue o bom trabalho.'), ('🚫', 'keep away', 'ficar longe', 'Keep away from him.', 'Fique longe dele.'), ('🌱', 'keep off', 'não pisar', 'Keep off the grass.', 'Não pise na grama.'), ('🔁', 'keep on', 'continuar', 'Keep on trying.', 'Continue tentando.'), ('🕵️', 'tip-off', 'aviso secreto', 'We got a tip-off.', 'Recebemos um aviso secreto.')],
    [('Keep ___ the good work.', 'Continue o bom trabalho.', ['up', 'on to', 'at'], 0, 'keep **up**.'), ('Keep ___ from him.', 'Fique longe dele.', ['away', 'off to', 'back to'], 0, 'keep **away**.'), ('Keep ___ the grass.', 'Não pise na grama.', ['off', 'out', 'up'], 0, 'keep **off**.'), ('Keep ___ trying.', 'Continue tentando.', ['on', 'in', 'to'], 0, 'keep **on**.')],
    [('Qual frase está certa?', ['Keep off the grass.', 'Keep of the grass.', 'Keep the grass off.'], 0, 'keep off.'), ('Qual está certa?', ['Keep on trying.', 'Keep on to try.', 'Keep trying on.'], 0, 'keep on trying.')],
    [['Man', 'Keep up the good work, class.', 'Continuem o bom trabalho, turma.'], ['Woman', 'And keep off the grass.', 'E não pisem na grama.'], ['Man', 'We got a tip-off about a fight.', 'Recebemos um aviso sobre uma briga.'], ['Woman', 'Keep away from him.', 'Fiquem longe dele.'],
     ['Man', 'Keep out of the hall.', 'Não entrem no salão.'], ['Woman', 'Keep on trying to be kind.', 'Continuem tentando ser gentis.'], ['Man', 'Keep track of your time.', 'Acompanhem o tempo.'], ['Woman', 'Good advice.', 'Bom conselho.']],
    [('What should the class keep up?', 'O que a turma deve manter?', [('👍', 'The good work'), ('🏃', 'The speed'), ('🎵', 'The music')], 0, 0, 'Diz: “good work.”'), ('Where should they not walk?', 'Onde não devem andar?', [('🌱', 'On the grass'), ('🛣️', 'On the road'), ('🏖️', 'On the beach')], 0, 1, 'Diz: “keep off the grass.”'),
     ('What did they get?', 'O que receberam?', [('🕵️', 'A tip-off'), ('🎁', 'A gift'), ('📦', 'A box')], 0, 2, 'Diz: “a tip-off.”')],
    [('🔁', 'Keep on', 'Continuar', 'persistir', 'Keep on trying.', 'Continue tentando.'), ('🚪', 'Keep out', 'Proibida a entrada', 'aviso', 'Keep out!', 'Proibida a entrada!'), ('⏱️', 'Keep track', 'Acompanhar', 'monitorar', 'Keep track of time.', 'Acompanhe o tempo.'), ('🤝', 'Keep your word', 'Cumprir a palavra', 'promessa', 'I keep my word.', 'Cumpro minha palavra.')]))

# ---------- give ----------
GV_VOCAB = [('🏳️', 'give up', 'desistir', 'Soa como “GUIV ÂP”.'), ('🤲', 'give in', 'ceder', 'Soa como “GUIV IN”.'), ('🎁', 'give away', 'doar', 'Soa como “GUIV a-UÊI”.'),
            ('↩️', 'give back', 'devolver', 'Soa como “GUIV BÉK”.'), ('📬', 'give out', 'distribuir', 'Soa como “GUIV ÁUT”.'), ('🌸', 'give off', 'emitir', 'Soa como “GUIV ÓF”.')]
GV_LAB = dict(short='gv', title='Laboratório de sons: give, never e dreams', pt='i soa i curto; ea soa i longo; ea soa i.', tip='Em give, o i é curto.',
              words=[('give', 'GUIV', 'dar', 'i = i', 'gave', 'GUÊIV'), ('never', 'NÉ-ver', 'nunca', 'e = é', 'nerve', 'NÂRV'), ('dreams', 'DRIMZ', 'sonhos', 'ea = i', 'drums', 'DRÂMZ')])
GV_VERBS = [('give', '🏳️', 'desistir', 'Never give up!', 'Never give out!', 'I gave up.', 'Desisti.', 'give **up**.'),
            ('give', '🤲', 'ceder', 'He gave in.', 'He gave up in.', 'I gave in.', 'Cedi.', 'give **in**.'),
            ('give', '🎁', 'doar', 'We give away clothes.', 'We give out away clothes.', 'I gave away.', 'Doei.', 'give **away**.'),
            ('give', '↩️', 'devolver', 'Give it back.', 'Give back it.', 'I gave back.', 'Devolvi.', 'give it **back**.')]

def gv(n, title, sub, pat, why, names, ids, rs, scenes, cover, teaser, rule, fm, mold, prod, m2, hot, gaps, traps, lines, quiz, exps):
    return mk(n, title, sub, pat, why, names, ids, rs, 'Rocky', scenes, cover, teaser, rule, fm, GV_VOCAB, GV_LAB, GV_VERBS, mold, prod, m2, hot, gaps, traps, lines, quiz, exps)

EPS.append(gv(82178, 'Give Up, Give In', "aprender phrasal verbs com give: give up, give in, give away, give back (desistir, ceder, doar)",
    "phrasal verbs: give up · give in · give away · give back", "Hoje você aprende phrasal verbs com give: Never give up! He gave in. We give away clothes. Give it back.",
    ('Man', 'Boy'), ['tom', 'tommy'], 'cafe2', ['cafe2', 'school', 'yard', 'park', 'street', 'hall'],
    ('Give Up, Give In: em 10 minutos você desiste, cede e doa em inglês', 'No café, o treinador e o menino falam de nunca desistir.'), ('Mais com give', 'Próximo: Phrasal verbs com give'),
    ('Give', 'Quatro sentidos novos.', 'Em português “nunca desista”. Em inglês: **never give up**.'),
    [('Give up', 'Never', 'give up!', 'Never give up!', 'give up.'), ('Give back', 'Give it', 'back.', 'Give it back.', 'give it back.')],
    [('Give up', 'Never give up', 'nunca desista', [(' on your dreams.', ' dos seus sonhos.'), (' now.', ' agora.'), (' hope.', ' da esperança.')]), ('Give in', 'He gave in', 'ele cedeu', [(' to the pain.', ' à dor.'), (' at last.', ' por fim.'), (' too soon.', ' cedo demais.')]), ('Give away', 'We give away', 'nós doamos', [(' clothes.', ' roupas.'), (' food.', ' comida.'), (' toys.', ' brinquedos.')])],
    ('🏳️', 'Give', 'Use give up, give in e give away', 'Fale. **Diga nunca desista, ele cedeu e nós doamos roupas.**', 'give in', 'Never give up! He gave in. We give away clothes.',
     [('Usei give up?', r"\bgive\s+up\b", 'Never give up!', 'Nunca desista!', 'Up! 🏳️'), ('Usei give in?', r"\bgave\s+in\b", 'He gave in.', 'Ele cedeu.', 'In! 🤲'), ('Usei give away?', r"\bgive\s+away\b", 'We give away clothes.', 'Nós doamos roupas.', 'Away! 🎁')]),
    ('🌸', 'Fixas', 'Use give it a try, give a hand e give it your all', 'Fale. **Diga experimente, dê uma mão e dê tudo de si.**', 'give it your all', 'Give it a try. Give me a hand. Give it your all.',
     [('Disse give it a try?', r"\bgive\s+it\s+a\s+try\b", 'Give it a try.', 'Experimente.', 'Try! 🎯'), ('Disse give a hand?', r"\bgive\s+me\s+a\s+hand\b", 'Give me a hand.', 'Dê-me uma mão.', 'Hand! 🤝'), ('Disse give it your all?', r"\bgive\s+it\s+your\s+all\b", 'Give it your all.', 'Dê tudo de si.', 'All! 🔥')]),
    [('🏳️', 'give up', 'desistir', 'Never give up!', 'Nunca desista!'), ('🤲', 'give in', 'ceder', 'He gave in.', 'Ele cedeu.'), ('🎁', 'give away', 'doar', 'We give away clothes.', 'Nós doamos roupas.'), ('↩️', 'give back', 'devolver', 'Give it back.', 'Devolva.'), ('🥊', 'dream', 'sonho', 'Follow your dream.', 'Siga seu sonho.')],
    [('Never give ___!', 'Nunca desista!', ['up', 'out', 'off'], 0, 'give **up**.'), ('He gave ___.', 'Ele cedeu.', ['in', 'on', 'at'], 0, 'gave **in**.'), ('We give ___ clothes.', 'Nós doamos roupas.', ['away', 'off', 'at'], 0, 'give **away**.'), ('Give it ___.', 'Devolva.', ['back', 'again to', 'on'], 0, 'give it **back**.')],
    [('Qual frase está certa?', ['Never give up!', 'Never give out!', 'Never gives up!'], 0, 'give up.'), ('Qual está certa?', ['Give it back.', 'Give back it.', 'Gave it back now.'], 0, 'give it back.')],
    [['Man', 'Round ten. Never give up!', 'Décimo round. Nunca desista!'], ['Boy', 'I am tired. I want to give in.', 'Estou cansado. Quero ceder.'], ['Man', 'Give it your all.', 'Dê tudo de si.'], ['Boy', 'Okay. I will not give up on my dream.', 'Certo. Não vou desistir do meu sonho.'],
     ['Man', 'After the fight we give away old gloves.', 'Depois da luta doamos luvas velhas.'], ['Boy', 'Give me a hand with the box.', 'Dê-me uma mão com a caixa.'], ['Man', 'Sure.', 'Claro.'], ['Boy', 'Thanks, coach!', 'Obrigado, treinador!']],
    [('What must he never do?', 'O que nunca deve fazer?', [('🏳️', 'Give up'), ('🏃', 'Run'), ('😴', 'Sleep')], 0, 0, 'Diz: “Never give up!”'), ('What does the boy want?', 'O que o menino quer?', [('🤲', 'To give in'), ('🍕', 'To eat'), ('🎮', 'To play')], 0, 1, 'Diz: “want to give in.”'),
     ('What do they give away?', 'O que doam?', [('🥊', 'Old gloves'), ('👟', 'Shoes'), ('🎒', 'Bags')], 0, 4, 'Diz: “old gloves.”')],
    [('🎯', 'Give it a try', 'Experimente', 'tentar', 'Give it a try.', 'Experimente.'), ('🤝', 'Give a hand', 'Dar uma mão', 'ajudar', 'Give me a hand.', 'Dê-me uma mão.'), ('🔥', 'Give it your all', 'Dar tudo de si', 'esforçar-se', 'Give it your all.', 'Dê tudo de si.'), ('🗣️', 'Give a speech', 'Fazer discurso', 'falar em público', 'He gave a speech.', 'Ele fez um discurso.')]))

EPS.append(gv(7082178, 'Phrasal verbs com give', "mais phrasal verbs com give: give out, give off, give way, give over (distribuir, emitir, ceder lugar)",
    "phrasal verbs: give out · give off · give way · give over", "Hoje você aprende mais quatro com give: She gives out leaflets. The flowers give off a scent. Give way to the bus. Give over!",
    ('Girl', 'Man'), ['polly', 'tom'], 'street', ['street', 'park', 'cafe2', 'shop', 'hall', 'lake'],
    ('Phrasal verbs com give: em 10 minutos você distribui, emite e cede a vez', 'Na rua, a menina e o homem distribuem folhetos e cheiram flores.'), ('Mais com give', 'Próximo: Phrasal verbs com come'),
    ('Give', 'Mais quatro sentidos.', 'Em português “distribuir”. Em inglês: **give out**.'),
    [('Give out', 'She', 'gives out leaflets.', 'She gives out leaflets.', 'give out.'), ('Give off', 'The flowers', 'give off a scent.', 'The flowers give off a scent.', 'give off.')],
    [('Give out', 'She gives out', 'ela distribui', [(' leaflets.', ' folhetos.'), (' free tickets.', ' ingressos grátis.'), (' water.', ' água.')]), ('Give off', 'It gives off', 'emite', [(' a scent.', ' um cheiro.'), (' heat.', ' calor.'), (' light.', ' luz.')]), ('Give way', 'Give way', 'dê passagem', [(' to the bus.', ' ao ônibus.'), (' to traffic.', ' ao trânsito.'), (' to him.', ' a ele.')])],
    ('📬', 'Give', 'Use give out, give off e give way', 'Fale. **Diga ela distribui folhetos, as flores emitem um cheiro e dê passagem ao ônibus.**', 'give way', 'She gives out leaflets. The flowers give off a scent. Give way to the bus.',
     [('Usei give out?', r"\bgives?\s+out\b", 'She gives out leaflets.', 'Ela distribui folhetos.', 'Out! 📬'), ('Usei give off?', r"\bgive\s+off\b", 'The flowers give off a scent.', 'As flores emitem um cheiro.', 'Off! 🌸'), ('Usei give way?', r"\bgive\s+way\b", 'Give way to the bus.', 'Dê passagem ao ônibus.', 'Way! 🚌')]),
    ('🌸', 'Fixas', 'Use give or take, give rise to e give and take', 'Fale. **Diga mais ou menos, dar origem a e dar e receber.**', 'give and take', 'It costs ten, give or take. It gave rise to a debate. Marriage is give and take.',
     [('Disse give or take?', r"\bgive\s+or\s+take\b", 'It costs ten, give or take.', 'Custa dez, mais ou menos.', 'Take! ➕'), ('Disse give rise to?', r"\bgave\s+rise\s+to\b", 'It gave rise to a debate.', 'Deu origem a um debate.', 'Rise! 📈'), ('Disse give and take?', r"\bgive\s+and\s+take\b", 'Marriage is give and take.', 'Casamento é dar e receber.', 'Give! 🤝')]),
    [('📬', 'give out', 'distribuir', 'She gives out leaflets.', 'Ela distribui folhetos.'), ('🌸', 'give off', 'emitir', 'The flowers give off a scent.', 'As flores emitem um cheiro.'), ('🚌', 'give way', 'dar passagem', 'Give way to the bus.', 'Dê passagem ao ônibus.'), ('🤲', 'give in', 'ceder', 'Do not give in.', 'Não ceda.'), ('🎁', 'give away', 'doar', 'I give away books.', 'Eu doo livros.')],
    [('She gives ___ leaflets.', 'Ela distribui folhetos.', ['out', 'in', 'on'], 0, 'give **out**.'), ('The flowers give ___ a scent.', 'As flores emitem um cheiro.', ['off', 'up', 'at'], 0, 'give **off**.'), ('Give ___ to the bus.', 'Dê passagem ao ônibus.', ['way', 'out', 'back'], 0, 'give **way**.'), ('It costs ten, give or ___.', 'Custa dez, mais ou menos.', ['take', 'make', 'get'], 0, 'give or **take**.')],
    [('Qual frase está certa?', ['She gives out leaflets.', 'She gives in leaflets.', 'She give out leaflets.'], 0, 'gives out.'), ('Qual está certa?', ['Give way to the bus.', 'Give way for the bus to.', 'Gave way the bus.'], 0, 'give way to.')],
    [['Girl', 'I give out leaflets on this street.', 'Eu distribuo folhetos nesta rua.'], ['Man', 'How many?', 'Quantos?'], ['Girl', 'A hundred, give or take.', 'Cem, mais ou menos.'], ['Man', 'These flowers give off a lovely scent.', 'Estas flores emitem um cheiro lindo.'],
     ['Girl', 'Look! Give way to the bus.', 'Olhe! Dê passagem ao ônibus.'], ['Man', 'Sorry. It is give and take.', 'Desculpe. É dar e receber.'], ['Girl', 'Do not give in to the rush.', 'Não ceda à pressa.'], ['Man', 'Okay.', 'Certo.']],
    [('What does she give out?', 'O que ela distribui?', [('📄', 'Leaflets'), ('🍎', 'Apples'), ('🎟️', 'Tickets')], 0, 0, 'Diz: “give out leaflets.”'), ('How many?', 'Quantos?', [('💯', 'About a hundred'), ('1️⃣', 'One'), ('🔟', 'Ten')], 0, 2, 'Diz: “A hundred, give or take.”'),
     ('What do the flowers give off?', 'O que as flores emitem?', [('🌸', 'A lovely scent'), ('🔥', 'Heat'), ('💡', 'Light')], 0, 3, 'Diz: “lovely scent.”')],
    [('➕', 'Give or take', 'Mais ou menos', 'aproximar', 'It costs ten, give or take.', 'Custa dez, mais ou menos.'), ('📈', 'Give rise to', 'Dar origem a', 'causar', 'It gave rise to a debate.', 'Deu origem a um debate.'), ('🤝', 'Give and take', 'Dar e receber', 'equilíbrio', 'Marriage is give and take.', 'Casamento é dar e receber.'), ('🎤', 'Give someone a call', 'Ligar para alguém', 'telefonar', 'Give me a call.', 'Ligue para mim.')]))
