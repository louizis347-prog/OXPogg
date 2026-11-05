"""Complementos por aula (palavras, verbos, phrasal verbs e expressões extras) para cumprir as cotas. Os dados ficam em ext_*.py."""
EXT={}
def A(id,words='',expr='',verbs='',pv=''):
    """words: linhas 'w;pt;ex;expt' · expr: 'en=pt|en=pt' · verbs: linhas 'v;pt;I ...;He ...' · pv: linhas 'pv;pt;ex;expt'"""
    d=EXT.setdefault(id,dict(add=[],expr=[],verbs=[],pv=[]))
    d['add']+=[l.strip() for l in words.strip().splitlines() if l.strip()]
    d['expr']+=[tuple(x.split('=',1)) for x in expr.split('|') if x.strip()]
    d['verbs']+=[tuple(l.strip().split(';')) for l in verbs.strip().splitlines() if l.strip()]
    d['pv']+=[tuple(l.strip().split(';')) for l in pv.strip().splitlines() if l.strip()]
import importlib,glob,os
for _f in sorted(glob.glob(os.path.join(os.path.dirname(__file__),'ext_*.py'))):
    importlib.import_module(os.path.basename(_f)[:-3])
