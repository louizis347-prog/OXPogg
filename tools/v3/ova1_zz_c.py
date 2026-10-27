# Lote C (A1): obras novas (séries, teatro, quadrinhos, videogames, óperas/balés, mitos, músicas) para episódios que repetiam obra. Ver zzc1_lib.py.
import glob as _g, os as _o, importlib as _i
from v3 import zzc1_lib as Z
for _f in sorted(_g.glob(_o.path.join(_o.path.dirname(_o.path.abspath(__file__)), 'zzc1_d*.py'))):
    _i.import_module('v3.' + _o.path.basename(_f)[:-3])
for _n in sorted(Z.SPECS):
    Z.put(_n)
