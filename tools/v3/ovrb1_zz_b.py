# Camada B do B1 (cinema: filmes, animações, musicais, documentários): troca completa de episódios que repetiam obra com outro episódio do curso.
# Dados em zzb1_d*.py; obras gravadas em obras_new_b1_zz_b.json (lib.OB lê o glob obras_new_b1_*.json). Ver zzb1_lib.py.
from v3 import zzb1_lib as Z
from v3 import zzb1_d1, zzb1_d2, zzb1_d3, zzb1_d4  # noqa: F401
Z.install()
Z.write_works()
