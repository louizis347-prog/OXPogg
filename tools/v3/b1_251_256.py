# B1 · episódios 251–256: aparelhos da casa, let/make/help, preposição + -ing.
from v3.b1h import *

from v3.ovrb1 import install
EPS = []
install(globals(), 'S')

def mk(n, title, sub, pat, why, names, ids, rs, obra, scenes, cover, teaser, rule, fm, vocab, lab, verbs, mold, prod, m2, hot, gaps, traps, lines, quiz, exps):
    return S(n=n, title=title, sub=sub, pattern=pat, why=why, names=names, ids=ids, rs=rs, obra=(obra, obra),
             hot=hot, gaps=gaps, traps=traps, rule=rule, fm=fm, cover=cover, vocab=vocab, lines=lines, quiz=quiz,
             teaser=teaser, exps=exps, lab=lab, verbs=verbs, mold=mold, prod=prod, m2=m2, scenes=scenes)

# ---------- 251 / 252 · aparelhos ----------
AP_VOCAB = [('🍞', 'toaster', 'torradeira', 'Soa como “TÔU-ster”.'), ('🥤', 'blender', 'liquidificador', 'Soa como “BLÉN-der”.'), ('🔌', 'extension cord', 'extensão', 'Soa como “ik-STÉN-shon KÓRD”.'),
            ('🔁', 'adapter', 'adaptador', 'Soa como “a-DÉP-ter”.'), ('🍊', 'juicer', 'espremedor', 'Soa como “DJU-ser”.'), ('🧹', 'vacuum', 'aspirador', 'Soa como “VÉ-kium”.')]
AP_LAB = dict(short='ap', title='Laboratório de sons: toaster, blender e vacuum', pt='oa soa ôu; e soa é; a soa é.', tip='Em toaster, o oa soa ôu.',
              words=[('toaster', 'TÔU-ster', 'torradeira', 'oa = ôu', 'tester', 'TÉS-ter'), ('blender', 'BLÉN-der', 'liquidificador', 'e = é', 'binder', 'BÁIN-der'), ('vacuum', 'VÉ-kium', 'aspirador', 'a = é', 'value', 'VÉ-liu')])
AP_VERBS = [('plug', '🔌', 'ligar na tomada', 'Plug it in.', 'Plug in it.', 'I plugged.', 'Liguei na tomada.', 'plug it **in**.'),
            ('turn', '🔛', 'ligar', 'Turn it on.', 'Turn on it.', 'I turned.', 'Liguei.', 'turn it **on**.'),
            ('switch', '📴', 'desligar', 'Switch it off.', 'Switch off it.', 'I switched.', 'Desliguei.', 'switch it **off**.'),
            ('break', '💥', 'quebrar', 'It broke down.', 'It broke up.', 'I break.', 'Eu quebro.', 'break **down**.')]

def ap(n, title, sub, pat, why, names, ids, rs, scenes, cover, teaser, rule, fm, mold, prod, m2, hot, gaps, traps, lines, quiz, exps):
    return mk(n, title, sub, pat, why, names, ids, rs, 'Modern Family', scenes, cover, teaser, rule, fm, AP_VOCAB, AP_LAB, AP_VERBS, mold, prod, m2, hot, gaps, traps, lines, quiz, exps)

EPS.append(ap(930036, 'Plug It In, Turn It On', "eletrodomésticos e gadgets: plug in, turn on, switch off, break down (toaster, blender, adapter)",
    "phrasal verbs de aparelhos: plug in · turn on · switch off · break down", "Hoje você aprende phrasal verbs de aparelhos: Plug it in. Turn it on. Switch it off. It broke down.",
    ('Woman', 'Man'), ['polly', 'tom'], 'kitchen', ['kitchen', 'home1', 'living', 'shop', 'cafe2', 'hall'],
    ('Plug It In, Turn It On: em 10 minutos você usa os aparelhos da casa em inglês', 'Na cozinha, a mulher e o homem testam a torradeira nova.'), ('Mais aparelhos', 'Próximo: Aparelhos da casa'),
    ('Aparelhos', 'O pronome vai no meio.', 'Em português “ligue na tomada”. Em inglês: **plug it in**.'),
    [('Tomada', 'Plug', 'it in.', 'Plug it in.', 'plug it in.'), ('Ligar', 'Turn', 'it on.', 'Turn it on.', 'turn it on.')],
    [('Plug it in', 'Plug it', 'ligue na tomada', [(' in.', ' agora.'), (' in, please.', ' por favor.'), (' in here.', ' aqui.')]), ('Turn it on', 'Turn it', 'ligue', [(' on.', ' agora.'), (' on, please.', ' por favor.'), (' on first.', ' primeiro.')]), ('Switch it off', 'Switch it', 'desligue', [(' off.', ' agora.'), (' off, please.', ' por favor.'), (' off at night.', ' à noite.')])],
    ('🔌', 'Aparelhos', 'Use plug it in, turn it on e switch it off', 'Fale. **Diga ligue na tomada, ligue e depois desligue.**', 'turn it on', 'Plug it in. Turn it on. Switch it off.',
     [('Usei plug it in?', r"\bplug\s+it\s+in\b", 'Plug it in.', 'Ligue na tomada.', 'Plug! 🔌'), ('Usei turn it on?', r"\bturn\s+it\s+on\b", 'Turn it on.', 'Ligue.', 'On! 🔛'), ('Usei switch it off?', r"\bswitch\s+it\s+off\b", 'Switch it off.', 'Desligue.', 'Off! 📴')]),
    ('💥', 'Fixas', 'Use out of order, on the blink e as good as new', 'Fale. **Diga fora de serviço, com defeito e como novo.**', 'as good as new', 'It is out of order. The toaster is on the blink. It works as good as new.',
     [('Disse out of order?', r"\bout\s+of\s+order\b", 'It is out of order.', 'Está fora de serviço.', 'Order! 💥'), ('Disse on the blink?', r"\bon\s+the\s+blink\b", 'The toaster is on the blink.', 'A torradeira está com defeito.', 'Blink! 🍞'), ('Disse as good as new?', r"\bas\s+good\s+as\s+new\b", 'It works as good as new.', 'Funciona como nova.', 'New! ✨')],),
    [('🔌', 'plug in', 'ligar na tomada', 'Plug it in.', 'Ligue na tomada.'), ('🔛', 'turn on', 'ligar', 'Turn it on.', 'Ligue.'), ('📴', 'switch off', 'desligar', 'Switch it off.', 'Desligue.'), ('💥', 'break down', 'quebrar', 'It broke down.', 'Quebrou.'), ('🍞', 'toaster', 'torradeira', 'The toaster is new.', 'A torradeira é nova.')],
    [('Plug it ___.', 'Ligue na tomada.', ['in', 'on', 'up'], 0, 'plug it **in**.'), ('Turn it ___.', 'Ligue.', ['on', 'in', 'at'], 0, 'turn it **on**.'), ('Switch it ___.', 'Desligue.', ['off', 'out to', 'over'], 0, 'switch it **off**.'), ('It broke ___.', 'Quebrou.', ['down', 'in', 'on'], 0, 'broke **down**.')],
    [('Qual frase está certa?', ['Plug it in.', 'Plug in it.', 'Plugs it in.'], 0, 'plug it in.'), ('Qual está certa?', ['Turn it on.', 'Turn on it.', 'Turns it on.'], 0, 'turn it on.')],
    [['Woman', 'Is the toaster plugged in?', 'A torradeira está ligada na tomada?'], ['Man', 'No. Plug it in.', 'Não. Ligue na tomada.'], ['Woman', 'Now turn it on.', 'Agora ligue.'], ['Man', 'It does not work. It broke down.', 'Não funciona. Quebrou.'],
     ['Woman', 'Switch it off first.', 'Desligue primeiro.'], ['Man', 'Okay, it is off.', 'Certo, está desligada.'], ['Woman', 'Use the blender instead.', 'Use o liquidificador.'], ['Man', 'Good idea.', 'Boa ideia.']],
    [('What must he do first?', 'O que ele deve fazer primeiro?', [('🔌', 'Plug it in'), ('🍞', 'Eat'), ('🧹', 'Clean')], 0, 1, 'Diz: “Plug it in.”'), ('What happened to it?', 'O que aconteceu com ela?', [('💥', 'It broke down'), ('🔥', 'It burned'), ('💧', 'It fell')], 0, 3, 'Diz: “It broke down.”'),
     ('What do they use instead?', 'O que usam no lugar?', [('🥤', 'The blender'), ('🍊', 'The juicer'), ('🧹', 'The vacuum')], 0, 6, 'Diz: “the blender.”')],
    [('💥', 'Out of order', 'Fora de serviço', 'quebrado', 'It is out of order.', 'Está fora de serviço.'), ('🍞', 'On the blink', 'Com defeito', 'falhando', 'The toaster is on the blink.', 'A torradeira está com defeito.'),
     ('✨', 'As good as new', 'Como novo', 'consertado', 'It works as good as new.', 'Funciona como nova.'), ('🔧', 'Fix it up', 'Consertar', 'arrumar', 'I will fix it up.', 'Vou consertar.')]))

EPS.append(ap(7930036, 'Aparelhos da casa', "mais aparelhos: plug in, turn on, switch off e break down na prática (extension cord, juicer, vacuum)",
    "aparelhos: turn up · turn down · hook up · run out of", "Hoje você pratica mais verbos de aparelhos: Turn it up. Turn it down. Hook it up. We ran out of power.",
    ('Man', 'Girl'), ['tom', 'polly'], 'living', ['living', 'kitchen', 'home1', 'shop', 'hall', 'cafe2'],
    ('Aparelhos da casa: em 10 minutos você controla volume, cabo e energia em inglês', 'Na sala, o homem e a menina arrumam a extensão e o aspirador.'), ('Mais aparelhos', 'Próximo: Let, make, help'),
    ('Aparelhos', 'Mais quatro verbos.', 'Em português “aumente”. Em inglês: **turn it up**.'),
    [('Aumentar', 'Turn', 'it up.', 'Turn it up.', 'turn it up.'), ('Conectar', 'Hook', 'it up.', 'Hook it up.', 'hook it up.')],
    [('Turn up', 'Turn it', 'aumente', [(' up.', ' o som.'), (' up, please.', ' por favor.'), (' up a bit.', ' um pouco.')]), ('Turn down', 'Turn it', 'diminua', [(' down.', ' o som.'), (' down, please.', ' por favor.'), (' down a bit.', ' um pouco.')]), ('Hook up', 'Hook it', 'conecte', [(' up.', ' agora.'), (' up here.', ' aqui.'), (' up first.', ' primeiro.')])],
    ('🔊', 'Aparelhos', 'Use turn it up, turn it down e hook it up', 'Fale. **Diga aumente, diminua e conecte.**', 'hook it up', 'Turn it up. Turn it down. Hook it up.',
     [('Usei turn it up?', r"\bturn\s+it\s+up\b", 'Turn it up.', 'Aumente.', 'Up! 🔊'), ('Usei turn it down?', r"\bturn\s+it\s+down\b", 'Turn it down.', 'Diminua.', 'Down! 🔉'), ('Usei hook it up?', r"\bhook\s+it\s+up\b", 'Hook it up.', 'Conecte.', 'Hook! 🔌')]),
    ('🧹', 'Fixas', 'Use run out of, plug and play e hit the switch', 'Fale. **Diga ficar sem, ligar e usar e apertar o interruptor.**', 'run out of', 'We ran out of power. It is plug and play. Hit the switch.',
     [('Disse run out of?', r"\bran\s+out\s+of\b", 'We ran out of power.', 'Ficamos sem energia.', 'Out! 🔋'), ('Disse plug and play?', r"\bplug\s+and\s+play\b", 'It is plug and play.', 'É ligar e usar.', 'Play! 🔌'), ('Disse hit the switch?', r"\bhit\s+the\s+switch\b", 'Hit the switch.', 'Aperte o interruptor.', 'Switch! 💡')]),
    [('🔊', 'turn up', 'aumentar', 'Turn it up.', 'Aumente.'), ('🔉', 'turn down', 'diminuir', 'Turn it down.', 'Diminua.'), ('🔌', 'hook up', 'conectar', 'Hook it up.', 'Conecte.'), ('🔋', 'run out of', 'ficar sem', 'We ran out of power.', 'Ficamos sem energia.'), ('🧹', 'vacuum', 'aspirador', 'The vacuum is loud.', 'O aspirador é barulhento.')],
    [('Turn it ___.', 'Aumente.', ['up', 'in', 'at'], 0, 'turn it **up**.'), ('Turn it ___.', 'Diminua.', ['down', 'on', 'of'], 0, 'turn it **down**.'), ('Hook it ___.', 'Conecte.', ['up', 'for', 'to'], 0, 'hook it **up**.'), ('We ran ___ of power.', 'Ficamos sem energia.', ['out', 'off', 'up'], 0, 'ran **out** of.')],
    [('Qual frase está certa?', ['Turn it up.', 'Turn up it.', 'Turns it up.'], 0, 'turn it up.'), ('Qual está certa?', ['We ran out of power.', 'We ran off power.', 'We run out of power yesterday.'], 0, 'ran out of.')],
    [['Man', 'The vacuum is loud. Turn it down.', 'O aspirador é barulhento. Diminua.'], ['Girl', 'I need the extension cord.', 'Preciso da extensão.'], ['Man', 'Hook it up here.', 'Conecte aqui.'], ['Girl', 'Now turn it up.', 'Agora aumente.'],
     ['Man', 'Wait. We ran out of power.', 'Espere. Ficamos sem energia.'], ['Girl', 'Hit the switch.', 'Aperte o interruptor.'], ['Man', 'It is plug and play.', 'É ligar e usar.'], ['Girl', 'Great!', 'Ótimo!']],
    [('How is the vacuum?', 'Como é o aspirador?', [('🔊', 'Loud'), ('🤫', 'Silent'), ('💤', 'Sleepy')], 0, 0, 'Diz: “The vacuum is loud.”'), ('What do they run out of?', 'Do que ficam sem?', [('🔋', 'Power'), ('💧', 'Water'), ('🍞', 'Bread')], 0, 4, 'Diz: “ran out of power.”'),
     ('What is it?', 'O que é?', [('🔌', 'Plug and play'), ('🛠️', 'Hard to use'), ('🕰️', 'Old')], 0, 6, 'Diz: “plug and play.”')],
    [('🔋', 'Run out of steam', 'Perder o gás', 'cansar', 'I ran out of steam.', 'Perdi o gás.'), ('💡', 'Hit the switch', 'Apertar o interruptor', 'ligar', 'Hit the switch.', 'Aperte o interruptor.'),
     ('🔌', 'Plug and play', 'Ligar e usar', 'fácil', 'It is plug and play.', 'É ligar e usar.'), ('🔧', 'Wired up', 'Ligado', 'conectado', 'It is wired up.', 'Está ligado.')]))

# ---------- 253 / 254 · let / make / help ----------
LM_VOCAB = [('🔓', 'let', 'deixar', 'Soa como “LÉT”.'), ('💪', 'make', 'obrigar', 'Soa como “MÊIK”.'), ('🤝', 'help', 'ajudar', 'Soa como “RÉLP”.'),
            ('📜', 'rules', 'regras', 'Soa como “RUULZ”.'), ('✅', 'allowed', 'permitido', 'Soa como “a-LÁUD”.'), ('🫡', 'obey', 'obedecer', 'Soa como “o-BÊI”.')]
LM_LAB = dict(short='lm', title='Laboratório de sons: let, make e obey', pt='e soa é; a soa êi; ey soa êi.', tip='Em obey, o ey soa êi.',
              words=[('let', 'LÉT', 'deixar', 'e = é', 'lit', 'LÍT'), ('make', 'MÊIK', 'obrigar', 'a = êi', 'mock', 'MÓK'), ('obey', 'o-BÊI', 'obedecer', 'ey = êi', 'obese', 'o-BIS')])
LM_VERBS = [('let', '🔓', 'deixar', 'They let me stay out.', 'They let me to stay out.', 'I let.', 'Deixei.', 'let + obj + **verbo**.'),
            ('make', '💪', 'obrigar', 'They make me study.', 'They make me to study.', 'I made.', 'Obriguei.', 'make + obj + **verbo**.'),
            ('help', '🤝', 'ajudar', 'They help me learn.', 'They help me learning.', 'I helped.', 'Ajudei.', 'help + obj + **verbo**.'),
            ('obey', '🫡', 'obedecer', 'I obey the rules.', 'I obey to the rules.', 'I obeyed.', 'Obedeci.', 'obey + **objeto**.')]
LM_MOLD = [('Let', 'My parents let me', 'meus pais me deixam', [(' stay out.', ' ficar fora.'), (' play games.', ' jogar.'), (' go alone.', ' ir sozinho.')]),
           ('Make', 'They make me', 'eles me obrigam a', [(' study.', ' estudar.'), (' clean up.', ' arrumar.'), (' wake up early.', ' acordar cedo.')]),
           ('Help', 'They help me', 'eles me ajudam a', [(' learn.', ' aprender.'), (' cook.', ' cozinhar.'), (' relax.', ' relaxar.')])]
LM_RULE = ('Let, make, help', 'Verbo sem to depois do objeto.', 'Em português “me deixam sair”. Em inglês: **let me go**.')
LM_FM = [('Let', 'My parents let me', 'stay out.', 'My parents let me stay out.', 'sem to.'), ('Make', 'They make me', 'study.', 'They make me study.', 'sem to.')]
LM_TRAPS = [('Qual frase está certa?', ['They let me stay out.', 'They let me to stay out.', 'They let me staying out.'], 0, 'let me + verbo.'), ('Qual está certa?', ['They make me study.', 'They make me to study.', 'They make me studying.'], 0, 'make me + verbo.')]

EPS.append(mk(82165, 'Let, Make, Help', "usar verbos causativos let, make e help (rules, allowed, obey)",
    "causativos: let me · make me · help me + verbo", "Hoje você aprende let, make e help: My parents let me stay out. They make me study. They help me learn.",
    ('Woman', 'Boy'), ['misshoney', 'tommy'], 'cafe2', 'Matilda', ['cafe2', 'school', 'home1', 'living', 'park', 'street'],
    ('Let, Make, Help: em 10 minutos você fala de regras de casa', 'No café, a professora e o menino falam das regras dos pais.'), ('Mais causativos', 'Próximo: Let, make, help na prática'),
    LM_RULE, LM_FM, LM_VOCAB, LM_LAB, LM_VERBS, LM_MOLD,
    ('🔓', 'Regras', 'Use let me, make me e help me', 'Fale. **Diga eles me deixam ficar fora, me obrigam a estudar e me ajudam a aprender.**', 'make me', 'They let me stay out. They make me study. They help me learn.',
     [('Usei let me?', r"\blet\s+me\s+stay\b", 'They let me stay out.', 'Eles me deixam ficar fora.', 'Let! 🔓'), ('Usei make me?', r"\bmake\s+me\s+study\b", 'They make me study.', 'Eles me obrigam a estudar.', 'Make! 💪'), ('Usei help me?', r"\bhelp\s+me\s+learn\b", 'They help me learn.', 'Eles me ajudam a aprender.', 'Help! 🤝')]),
    ('📜', 'Fixas', 'Use let go, make sure e help yourself', 'Fale. **Diga soltar, garantir e fique à vontade.**', 'make sure', 'Let go! Make sure you obey. Help yourself.',
     [('Disse let go?', r"\blet\s+go\b", 'Let go!', 'Solte!', 'Go! 🔓'), ('Disse make sure?', r"\bmake\s+sure\b", 'Make sure you obey.', 'Garanta que obedece.', 'Sure! ✅'), ('Disse help yourself?', r"\bhelp\s+yourself\b", 'Help yourself.', 'Fique à vontade.', 'Yourself! 🤝')]),
    [('🔓', 'let me', 'me deixar', 'They let me stay out.', 'Eles me deixam ficar fora.'), ('💪', 'make me', 'me obrigar', 'They make me study.', 'Eles me obrigam a estudar.'), ('🤝', 'help me', 'me ajudar', 'They help me learn.', 'Eles me ajudam a aprender.'), ('📜', 'rules', 'regras', 'The rules are fair.', 'As regras são justas.'), ('🫡', 'obey', 'obedecer', 'I obey the rules.', 'Eu obedeço às regras.')],
    [('They ___ me stay out.', 'Eles me deixam ficar fora.', ['let', 'allow', 'permit'], 0, '**let** me + verbo.'), ('They ___ me study.', 'Eles me obrigam a estudar.', ['make', 'let', 'help to'], 0, '**make** me + verbo.'), ('They help me ___.', 'Eles me ajudam a aprender.', ['learn', 'to learning', 'learned'], 0, 'help me **learn**.'), ('I ___ the rules.', 'Eu obedeço às regras.', ['obey', 'obeys', 'obeying'], 0, 'I **obey**.')],
    LM_TRAPS,
    [['Woman', 'What are your rules at home?', 'Quais são as regras em casa?'], ['Boy', 'My parents let me stay out until ten.', 'Meus pais me deixam ficar fora até as dez.'], ['Woman', 'And homework?', 'E o dever?'], ['Boy', 'They make me study first.', 'Eles me obrigam a estudar primeiro.'],
     ['Woman', 'Do they help you?', 'Eles ajudam você?'], ['Boy', 'Yes, they help me learn.', 'Sim, me ajudam a aprender.'], ['Woman', 'Do you obey the rules?', 'Você obedece às regras?'], ['Boy', 'Always!', 'Sempre!']],
    [('Until when can he stay out?', 'Até quando pode ficar fora?', [('🔟', 'Ten'), ('8️⃣', 'Eight'), ('1️⃣', 'One')], 0, 1, 'Diz: “until ten.”'), ('What do they make him do?', 'O que o obrigam a fazer?', [('📚', 'Study first'), ('🧹', 'Clean'), ('🍳', 'Cook')], 0, 3, 'Diz: “make me study.”'),
     ('Does he obey?', 'Ele obedece?', [('🫡', 'Always'), ('🙅', 'Never'), ('🤷', 'Sometimes')], 0, 7, 'Diz: “Always!”')],
    [('🔓', 'Let it go', 'Deixar para lá', 'esquecer', 'Let it go.', 'Deixe para lá.'), ('✅', 'Make sure', 'Garantir', 'checar', 'Make sure you obey.', 'Garanta que obedece.'), ('🤝', 'Help yourself', 'Fique à vontade', 'oferecer', 'Help yourself.', 'Fique à vontade.'), ('💪', 'Make do', 'Se virar', 'improvisar', 'We make do.', 'Nós nos viramos.')]))

EPS.append(mk(7082165, 'Let, make, help', "let, make e help na passiva e com adjetivo: be allowed to, be made to, make someone happy",
    "causativos 2: be allowed to · be made to · make + adjetivo", "Hoje você pratica: I am allowed to go. I was made to wait. The rules make me happy.",
    ('Girl', 'Man'), ['polly', 'tom'], 'school', 'Matilda', ['school', 'hall', 'cafe2', 'office', 'street', 'park'],
    ('Let, make, help: em 10 minutos você diz o que é permitido e o que é obrigado', 'Na escola, a menina e o homem falam do que podem e não podem.'), ('Mais causativos', 'Próximo: Preposição + ing'),
    ('Passiva e adjetivo', 'Allowed to e made to.', 'Em português “tenho permissão”. Em inglês: **I am allowed to go**.'),
    [('Allowed', 'I am', 'allowed to go.', 'I am allowed to go.', 'be allowed to + verbo.'), ('Made to', 'I was', 'made to wait.', 'I was made to wait.', 'be made to + verbo.')],
    LM_VOCAB, LM_LAB, LM_VERBS, [('Allowed', 'I am allowed', 'tenho permissão', [(' to go.', ' de ir.'), (' to play.', ' de brincar.'), (' to stay.', ' de ficar.')]), ('Made to', 'I was made', 'me obrigaram', [(' to wait.', ' a esperar.'), (' to clean.', ' a limpar.'), (' to leave.', ' a sair.')]), ('Make + adj', 'The rules make me', 'as regras me deixam', [(' happy.', ' feliz.'), (' tired.', ' cansada.'), (' calm.', ' calma.')])],
    ('✅', 'Permissão', 'Use allowed to, made to e make me', 'Fale. **Diga tenho permissão de ir, me obrigaram a esperar e as regras me deixam feliz.**', 'allowed to', 'I am allowed to go. I was made to wait. The rules make me happy.',
     [('Usei allowed to?', r"\ballowed\s+to\s+go\b", 'I am allowed to go.', 'Tenho permissão de ir.', 'Allowed! ✅'), ('Usei made to?', r"\bmade\s+to\s+wait\b", 'I was made to wait.', 'Me obrigaram a esperar.', 'Made! 💪'), ('Usei make me?', r"\bmake\s+me\s+happy\b", 'The rules make me happy.', 'As regras me deixam feliz.', 'Happy! 😊')]),
    ('📜', 'Fixas', 'Use make up your mind, make friends e make a difference', 'Fale. **Diga decida-se, fazer amigos e fazer diferença.**', 'make a difference', 'Make up your mind. We make friends. You make a difference.',
     [('Disse make up your mind?', r"\bmake\s+up\s+your\s+mind\b", 'Make up your mind.', 'Decida-se.', 'Mind! 🧠'), ('Disse make friends?', r"\bmake\s+friends\b", 'We make friends.', 'Fazemos amigos.', 'Friends! 🤝'), ('Disse make a difference?', r"\bmake\s+a\s+difference\b", 'You make a difference.', 'Você faz diferença.', 'Difference! ✨')]),
    [('✅', 'be allowed to', 'ter permissão', 'I am allowed to go.', 'Tenho permissão de ir.'), ('💪', 'be made to', 'ser obrigado', 'I was made to wait.', 'Me obrigaram a esperar.'), ('😊', 'make me happy', 'me deixar feliz', 'The rules make me happy.', 'As regras me deixam feliz.'), ('📜', 'rules', 'regras', 'Read the rules.', 'Leia as regras.'), ('🫡', 'obey', 'obedecer', 'Obey the teacher.', 'Obedeça ao professor.')],
    [('I am ___ to go.', 'Tenho permissão de ir.', ['allowed', 'let', 'made'], 0, 'be **allowed** to.'), ('I was ___ to wait.', 'Me obrigaram a esperar.', ['made', 'let', 'helped'], 0, 'was **made** to.'), ('The rules make me ___.', 'As regras me deixam feliz.', ['happy', 'happily', 'happiness'], 0, 'make me **happy**.'), ('Read the ___.', 'Leia as regras.', ['rules', 'rule is', 'ruling'], 0, 'the **rules**.')],
    [('Qual frase está certa?', ['I am allowed to go.', 'I am allowed go.', 'I allowed to go.'], 0, 'allowed to go.'), ('Qual está certa?', ['I was made to wait.', 'I was made wait.', 'I made to wait.'], 0, 'was made to.')],
    [['Girl', 'Am I allowed to go out?', 'Tenho permissão de sair?'], ['Man', 'Yes, you are allowed to go.', 'Sim, você tem permissão de ir.'], ['Girl', 'Yesterday I was made to wait.', 'Ontem me obrigaram a esperar.'], ['Man', 'That is not fair.', 'Isso não é justo.'],
     ['Girl', 'The new rules make me happy.', 'As novas regras me deixam feliz.'], ['Man', 'Read the rules again.', 'Leia as regras de novo.'], ['Girl', 'I will obey them.', 'Vou obedecê-las.'], ['Man', 'Good.', 'Bom.']],
    [('Is she allowed to go out?', 'Ela pode sair?', [('✅', 'Yes'), ('🚫', 'No'), ('🤷', 'Unknown')], 0, 1, 'Diz: “you are allowed to go.”'), ('What was she made to do?', 'O que a obrigaram a fazer?', [('⏳', 'Wait'), ('🏃', 'Run'), ('🧹', 'Clean')], 0, 2, 'Diz: “made to wait.”'),
     ('How do the rules make her feel?', 'Como as regras a fazem sentir?', [('😊', 'Happy'), ('😠', 'Angry'), ('😴', 'Sleepy')], 0, 4, 'Diz: “make me happy.”')],
    [('🧠', 'Make up your mind', 'Decida-se', 'escolher', 'Make up your mind.', 'Decida-se.'), ('🤝', 'Make friends', 'Fazer amigos', 'socializar', 'We make friends.', 'Fazemos amigos.'), ('✨', 'Make a difference', 'Fazer diferença', 'impactar', 'You make a difference.', 'Você faz diferença.'), ('🚪', 'Make way', 'Abrir caminho', 'dar passagem', 'Make way, please.', 'Dê passagem, por favor.')]))

# ---------- 255 / 256 · preposição + -ing ----------
PI_VOCAB = [('👍', 'good at', 'bom em', 'Soa como “GUD ÉT”.'), ('😨', 'afraid of', 'com medo de', 'Soa como “a-FRÊID ÓV”.'), ('🚫', 'without', 'sem', 'Soa como “ui-DHÁUT”.'),
            ('🤔', 'interested in', 'interessado em', 'Soa como “ÍN-tris-tid IN”.'), ('😩', 'tired of', 'cansado de', 'Soa como “TÁI-erd ÓV”.'), ('🤥', 'honest', 'honesto', 'Soa como “Ó-nist”.')]
PI_LAB = dict(short='pi', title='Laboratório de sons: afraid, without e honest', pt='ai soa êi; th soa dh; h é mudo.', tip='Em honest, o h é mudo.',
              words=[('afraid', 'a-FRÊID', 'com medo', 'ai = êi', 'a fried', 'a-FRÁID'), ('without', 'ui-DHÁUT', 'sem', 'th = dh', 'within', 'ui-DHÍN'), ('honest', 'Ó-nist', 'honesto', 'h mudo', 'harvest', 'RÁR-vist')])
PI_VERBS = [('tell', '🗣️', 'contar', 'good at telling stories', 'good at tell stories', 'I told.', 'Contei.', 'at + **telling**.'),
            ('lie', '🤥', 'mentir', 'afraid of lying', 'afraid of lie', 'I lied.', 'Menti.', 'of + **lying**.'),
            ('leave', '🚪', 'sair', 'without leaving', 'without to leave', 'I left.', 'Saí.', 'without + **leaving**.'),
            ('read', '📚', 'ler', 'interested in reading', 'interested in read', 'I read.', 'Li.', 'in + **reading**.')]
PI_MOLD = [('Good at', 'He is good at', 'ele é bom em', [(' telling stories.', ' contar histórias.'), (' swimming.', ' nadar.'), (' cooking.', ' cozinhar.')]),
           ('Afraid of', 'She is afraid of', 'ela tem medo de', [(' lying.', ' mentir.'), (' flying.', ' voar.'), (' falling.', ' cair.')]),
           ('Without', 'He left without', 'ele saiu sem', [(' saying a word.', ' dizer uma palavra.'), (' waiting.', ' esperar.'), (' looking back.', ' olhar para trás.')])]
PI_RULE = ('Preposição + -ing', 'Depois de preposição, o verbo vai em -ing.', 'Em português “bom em contar”. Em inglês: **good at telling**.')
PI_FM = [('Good at', 'He is good at', 'telling stories.', 'He is good at telling stories.', 'at + -ing.'), ('Without', 'He left without', 'saying a word.', 'He left without saying a word.', 'without + -ing.')]
PI_TRAPS = [('Qual frase está certa?', ['He is good at telling stories.', 'He is good at tell stories.', 'He is good at to tell stories.'], 0, 'at + -ing.'), ('Qual está certa?', ['He left without saying a word.', 'He left without say a word.', 'He left without to say a word.'], 0, 'without + -ing.')]

EPS.append(mk(82166, 'Prepositions + -ing', "usar -ing depois de preposição: good at, afraid of, without, interested in (honest, tired of)",
    "preposição + -ing: good at · afraid of · without · interested in", "Hoje você aprende -ing depois de preposição: He is good at telling stories. She is afraid of lying. He left without waiting.",
    ('Woman', 'Man'), ['polly', 'tom'], 'cafe2', 'Pinocchio', ['cafe2', 'park', 'living', 'street', 'hall', 'school'],
    ('Prepositions + -ing: em 10 minutos você acerta o verbo depois de at, of e without', 'No café, a mulher e o homem falam de um menino que mente.'), ('Mais -ing', 'Próximo: Preposição + -ing na prática'),
    PI_RULE, PI_FM, PI_VOCAB, PI_LAB, PI_VERBS, PI_MOLD,
    ('👍', 'Preposição', 'Use good at, afraid of e without com -ing', 'Fale. **Diga ele é bom em contar histórias, ela tem medo de mentir e ele saiu sem esperar.**', 'afraid of', 'He is good at telling stories. She is afraid of lying. He left without waiting.',
     [('Usei good at?', r"\bgood\s+at\s+telling\b", 'He is good at telling stories.', 'Ele é bom em contar histórias.', 'At! 👍'), ('Usei afraid of?', r"\bafraid\s+of\s+lying\b", 'She is afraid of lying.', 'Ela tem medo de mentir.', 'Of! 😨'), ('Usei without?', r"\bwithout\s+waiting\b", 'He left without waiting.', 'Ele saiu sem esperar.', 'Without! 🚪')]),
    ('🤥', 'Fixas', 'Use instead of, in spite of e by the way', 'Fale. **Diga em vez de, apesar de e a propósito.**', 'instead of', 'Instead of lying, tell the truth. In spite of being small, he is brave. By the way, who is he?',
     [('Disse instead of?', r"\binstead\s+of\s+lying\b", 'Instead of lying, tell the truth.', 'Em vez de mentir, diga a verdade.', 'Instead! 🔁'), ('Disse in spite of?', r"\bin\s+spite\s+of\s+being\b", 'In spite of being small, he is brave.', 'Apesar de pequeno, ele é corajoso.', 'Spite! 🦁'), ('Disse by the way?', r"\bby\s+the\s+way\b", 'By the way, who is he?', 'A propósito, quem é ele?', 'Way! ❓')]),
    [('👍', 'good at', 'bom em', 'He is good at telling stories.', 'Ele é bom em contar histórias.'), ('😨', 'afraid of', 'com medo de', 'She is afraid of lying.', 'Ela tem medo de mentir.'), ('🚪', 'without', 'sem', 'He left without waiting.', 'Ele saiu sem esperar.'), ('🤔', 'interested in', 'interessado em', 'I am interested in reading.', 'Tenho interesse em ler.'), ('😩', 'tired of', 'cansado de', 'I am tired of waiting.', 'Estou cansado de esperar.')],
    [('He is good at ___ stories.', 'Ele é bom em contar histórias.', ['telling', 'tell', 'to tell'], 0, 'at + **-ing**.'), ('She is afraid of ___.', 'Ela tem medo de mentir.', ['lying', 'lie', 'to lie'], 0, 'of + **-ing**.'), ('He left without ___.', 'Ele saiu sem esperar.', ['waiting', 'wait', 'to wait'], 0, 'without + **-ing**.'), ('I am tired of ___.', 'Estou cansado de esperar.', ['waiting', 'wait', 'to wait'], 0, 'of + **-ing**.')],
    PI_TRAPS,
    [['Woman', 'Do you know Pinocchio? He is good at telling stories.', 'Você conhece Pinóquio? Ele é bom em contar histórias.'], ['Man', 'But he lies. He is not honest.', 'Mas ele mente. Não é honesto.'], ['Woman', 'He is not afraid of lying.', 'Ele não tem medo de mentir.'], ['Man', 'I am tired of hearing it.', 'Estou cansado de ouvir isso.'],
     ['Woman', 'He left without saying goodbye.', 'Ele saiu sem se despedir.'], ['Man', 'Are you interested in reading it?', 'Você tem interesse em ler?'], ['Woman', 'Yes!', 'Sim!'], ['Man', 'I will lend it to you.', 'Vou emprestar para você.']],
    [('What is he good at?', 'Em que ele é bom?', [('🗣️', 'Telling stories'), ('🏊', 'Swimming'), ('🍳', 'Cooking')], 0, 0, 'Diz: “good at telling stories.”'), ('Is he afraid of lying?', 'Ele tem medo de mentir?', [('🙅', 'No'), ('😨', 'Yes'), ('🤷', 'Unknown')], 0, 2, 'Diz: “not afraid of lying.”'),
     ('What does he lend?', 'O que ele empresta?', [('📚', 'The book'), ('🚗', 'The car'), ('💰', 'Money')], 0, 7, 'Diz: “lend it to you.”')],
    [('🔁', 'Instead of', 'Em vez de', 'substituir', 'Instead of lying, tell the truth.', 'Em vez de mentir, diga a verdade.'), ('🦁', 'In spite of', 'Apesar de', 'contrastar', 'In spite of being small, he is brave.', 'Apesar de pequeno, ele é corajoso.'), ('👍', 'Look forward to', 'Esperar ansioso', 'expectativa', 'I look forward to reading.', 'Espero ansioso para ler.'), ('🤷', 'Be used to', 'Estar acostumado', 'hábito', 'I am used to waiting.', 'Estou acostumado a esperar.')]))

EPS.append(mk(7082166, 'Preposição + -ing', "preposição + -ing na prática: before, after, by, for e on (lying, honest, tired of)",
    "before/after/by + -ing: before leaving · after eating · by practising", "Hoje você pratica: Before leaving, call me. After eating, rest. You learn by practising.",
    ('Girl', 'Man'), ['polly', 'tom'], 'park', 'Pinocchio', ['park', 'yard', 'cafe2', 'school', 'street', 'living'],
    ('Preposição + -ing: em 10 minutos você usa before, after e by com -ing', 'No parque, a menina e o homem falam de como aprender mais.'), ('Mais -ing', 'Próximo: Used to'),
    ('Before/after/by', 'Também pedem -ing.', 'Em português “antes de sair”. Em inglês: **before leaving**.'),
    [('Before', 'Before', 'leaving, call me.', 'Before leaving, call me.', 'before + -ing.'), ('By', 'You learn by', 'practising.', 'You learn by practising.', 'by + -ing.')],
    PI_VOCAB, PI_LAB, PI_VERBS, [('Before', 'Before', 'antes de', [(' leaving, call me.', ' sair, ligue para mim.'), (' eating, wash up.', ' comer, lave as mãos.'), (' sleeping, read.', ' dormir, leia.')]), ('After', 'After', 'depois de', [(' eating, rest.', ' comer, descanse.'), (' working, relax.', ' trabalhar, relaxe.'), (' reading, sleep.', ' ler, durma.')]), ('By', 'You learn by', 'você aprende', [(' practising.', ' praticando.'), (' listening.', ' ouvindo.'), (' reading.', ' lendo.')])],
    ('⏰', 'Tempo', 'Use before, after e by com -ing', 'Fale. **Diga antes de sair ligue, depois de comer descanse e você aprende praticando.**', 'by practising', 'Before leaving, call me. After eating, rest. You learn by practising.',
     [('Usei before?', r"\bbefore\s+leaving\b", 'Before leaving, call me.', 'Antes de sair, ligue para mim.', 'Before! ⏰'), ('Usei after?', r"\bafter\s+eating\b", 'After eating, rest.', 'Depois de comer, descanse.', 'After! 🍽️'), ('Usei by?', r"\bby\s+practi[sc]ing\b", 'You learn by practising.', 'Você aprende praticando.', 'By! 💡')]),
    ('🤥', 'Fixas', 'Use on arriving, for example e in doing so', 'Fale. **Diga ao chegar, por exemplo e ao fazer isso.**', 'on arriving', 'On arriving, call me. For example, call at six. In doing so, you help me.',
     [('Disse on arriving?', r"\bon\s+arriving\b", 'On arriving, call me.', 'Ao chegar, ligue para mim.', 'Arriving! 🛬'), ('Disse for example?', r"\bfor\s+example\b", 'For example, call at six.', 'Por exemplo, ligue às seis.', 'Example! 📌'), ('Disse in doing so?', r"\bin\s+doing\s+so\b", 'In doing so, you help me.', 'Ao fazer isso, você me ajuda.', 'Doing! 🤝')]),
    [('⏰', 'before leaving', 'antes de sair', 'Before leaving, call me.', 'Antes de sair, ligue para mim.'), ('🍽️', 'after eating', 'depois de comer', 'After eating, rest.', 'Depois de comer, descanse.'), ('💡', 'by practising', 'praticando', 'You learn by practising.', 'Você aprende praticando.'), ('🤥', 'honest', 'honesto', 'Be honest.', 'Seja honesto.'), ('😩', 'tired of', 'cansado de', 'I am tired of lying.', 'Estou cansado de mentir.')],
    [('___ leaving, call me.', 'Antes de sair, ligue para mim.', ['Before', 'Since', 'Until to'], 0, '**Before** + -ing.'), ('After ___, rest.', 'Depois de comer, descanse.', ['eating', 'eat', 'to eat'], 0, 'after + **-ing**.'), ('You learn by ___.', 'Você aprende praticando.', ['practising', 'practise', 'to practise'], 0, 'by + **-ing**.'), ('Be ___.', 'Seja honesto.', ['honest', 'honestly', 'honesty'], 0, 'be **honest**.')],
    [('Qual frase está certa?', ['Before leaving, call me.', 'Before to leave, call me.', 'Before leave, call me.'], 0, 'before leaving.'), ('Qual está certa?', ['You learn by practising.', 'You learn by practise.', 'You learn by to practise.'], 0, 'by practising.')],
    [['Girl', 'How do I learn English?', 'Como aprendo inglês?'], ['Man', 'You learn by practising.', 'Você aprende praticando.'], ['Girl', 'And before leaving home?', 'E antes de sair de casa?'], ['Man', 'Before leaving, listen to a song.', 'Antes de sair, ouça uma música.'],
     ['Girl', 'After eating?', 'Depois de comer?'], ['Man', 'After eating, read a page.', 'Depois de comer, leia uma página.'], ['Girl', 'I am tired of lying about my time.', 'Estou cansada de mentir sobre meu tempo.'], ['Man', 'Be honest, then.', 'Seja honesta, então.']],
    [('How do you learn?', 'Como se aprende?', [('💡', 'By practising'), ('😴', 'By sleeping'), ('🎮', 'By gaming')], 0, 1, 'Diz: “learn by practising.”'), ('What to do before leaving?', 'O que fazer antes de sair?', [('🎵', 'Listen to a song'), ('📺', 'Watch TV'), ('🍰', 'Eat cake')], 0, 3, 'Diz: “listen to a song.”'),
     ('What does he tell her?', 'O que ele diz a ela?', [('🤥', 'Be honest'), ('🏃', 'Run'), ('💤', 'Sleep')], 0, 7, 'Diz: “Be honest.”')],
    [('🛬', 'On arriving', 'Ao chegar', 'quando chegar', 'On arriving, call me.', 'Ao chegar, ligue para mim.'), ('📌', 'For example', 'Por exemplo', 'ilustrar', 'For example, call at six.', 'Por exemplo, ligue às seis.'), ('🤝', 'In doing so', 'Ao fazer isso', 'consequência', 'In doing so, you help me.', 'Ao fazer isso, você me ajuda.'), ('⏰', 'Upon leaving', 'Ao sair', 'formal', 'Upon leaving, sign here.', 'Ao sair, assine aqui.')]))
