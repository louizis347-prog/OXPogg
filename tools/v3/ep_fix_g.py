# Episódio 52 refeito: ele repetia 5 das 6 palavras do 51; agora fala de horários de transporte e eventos.
from v3.short import *
from v3.oldn import N

EPS = []
from v3.zz1_lib import full as zz1_full

EPS.append(zz1_full(7030010, pattern='What time is…? · at + hora', teaser=('Lanche e hora de dormir', 'Próximo: What time do we…? com lanches e hora de dormir.')))

