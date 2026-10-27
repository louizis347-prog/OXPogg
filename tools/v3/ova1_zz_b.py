# Lote B (cinema) do A1: obras novas para episódios que repetiam obra. Dados em zz_b_d*.py (formato em zz_b_lib.py); instala na camada ova2.
import glob, importlib, os
from v3 import zz_b_lib as Z
_here = os.path.dirname(os.path.abspath(__file__))
for _f in sorted(glob.glob(os.path.join(_here, 'zz_b_d*.py'))):
    importlib.import_module('v3.' + os.path.basename(_f)[:-3])
for _n in sorted(Z.SPECS):
    Z.put_layer(_n)
