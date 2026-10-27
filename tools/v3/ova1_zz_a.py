# Lote A (A1): obras novas de literatura infantil, contos, fábulas, cantigas, clássicos e poemas para episódios que repetiam obra. Ver zz1_lib.py.
from v3 import zz1_lib as Z
Z.load()
for _n in sorted(Z.SPECS):
    if _n not in Z.FULL: Z.put_layer(_n)
