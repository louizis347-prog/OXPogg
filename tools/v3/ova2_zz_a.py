# Lote A (ova2): obras novas (livros infantis, contos, fábulas, cantigas, clássicos, poemas) para episódios 1-240 que repetiam obra. Ver zz_a_lib.py.
from v3 import zz_a_lib as Z
import v3.zz_a_d1 as D1
import v3.zz_a_d2 as D2
for _n in sorted(Z.SPECS):
    if _n in D1.OVA2 or _n in D2.OVA2: Z.put_ova2(_n)
