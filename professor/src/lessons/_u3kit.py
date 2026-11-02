"""Pecas comuns da Unidade 3 (aulas 17-24): mapa da unidade, rubrica e montagem. Uso interno das aulas l017-l024."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from rl_common import PLAN, teach, finish

NAME = 'Eating out & shopping'
MAP = ['Ordering in a restaurant', 'Fast food and takeout', 'At the supermarket', 'At the market: quantities', 'Asking for the bill and paying', 'Food likes and dislikes', 'Following a simple recipe', 'Real-Life Mission Day 3']
CRIT = [dict(k='flu', name='Fluency', desc='Mantém a comunicação sem interrupções excessivas.'), dict(k='lan', name='Language use', desc='Utiliza adequadamente padrões, vocabulário e expressões.'), dict(k='pro', name='Pronunciation', desc='É compreensível e usa ritmo e entonação adequados.'), dict(k='int', name='Interaction', desc='Responde, pergunta, esclarece e desenvolve a conversa.')]
INTERP = [dict(max=8, text='Needs more support. Revisit the main patterns with guided practice before the next lesson.'), dict(max=13, text='Functional performance. Work on the lowest criteria in the next lesson.'), dict(max=17, text='Good control. Raise complexity and speed; add follow-up questions.'), dict(max=20, text='Strong performance. Move to a more demanding situation.')]
LV_NOTE = 'This progression is illustrative: complex sentences do not define a level on their own. CEFR also considers comprehension, autonomy, fluency, accuracy, interaction and appropriateness.'


def unit_open(k):
    return dict(n=3, k=k, of=8, name=NAME, map=MAP)


def feedback(well, improve, nxt, tg=None):
    return dict(t='rl_feedback', stage='write', title='Feedback & review — Speaking Performance Check', criteria=CRIT, interpret=INTERP, prompts=dict(well=well, improve=improve, next=nxt),
        teach=tg or teach(goal='Avaliar o que o aluno conseguiu comunicar, não só os erros gramaticais.',
            solo=['O estudante se autoavalia primeiro; depois você.', 'Feche com os três blocos: What you did well · What to improve · Your next challenge.'],
            group=['Dê um comentário por critério a cada estudante.', 'Cada um escolhe o próprio próximo desafio.'],
            answers='A rubrica é uma ferramenta interna de acompanhamento, não uma certificação CEFR.'))


def levels(you, ladder, tg=None):
    return dict(t='rl_levels', stage='exit', title='Level up — the same situation from A1 to C2', you=you,
        intro='You do not need six different methods: the structure stays, while language complexity and autonomy grow.',
        ladder=[dict(lv=l, say=s, goal=g) for l, s, g in zip(['A1', 'A2', 'B1', 'B2', 'C1', 'C2'], *zip(*ladder))], note=LV_NOTE,
        teach=tg or teach(goal='Mostrar a progressão sem criar seis metodologias.', solo=['Mostre onde o estudante está e a próxima etapa.'], group=['Cada um escolhe a frase do próprio nível e a do próximo.']))


def assemble(n, k, topic, title, pt, scene, cast, dialog, pages, tod='day'):
    L = dict(n=n, topic=topic, level='A1', title=title, pt=pt, unit=dict(n=3, k=k, of=8, name=NAME), minutes=60, cast=cast, scene=scene, tod=tod, plan=PLAN, dialog=dialog, pages=pages)
    return L
