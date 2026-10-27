# Lote A (ova2b): obras novas (livros infantis, contos, fábulas, cantigas, clássicos, poemas) para episódios 241+ que repetiam obra. Ver zz_a_lib.py.
from v3 import zz_a_lib as Z
import v3.zz_a_d3 as D3
import v3.zz_a_d4 as D4
import v3.zz_a_d5 as D5
for _n in sorted(Z.SPECS):
    if _n in D3.OVA2B or _n in D4.OVA2B or _n in D5.OVA2B: Z.put_ova2b(_n)
