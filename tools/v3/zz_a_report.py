#!/usr/bin/env python3
"""Relatório do lote A: (1) nenhuma obra nova colide com obras_em_uso nem entre si; (2) nenhum quadro cita a obra/elenco antigos.
Rodar da raiz: COURSE=en-a2 python3 tools/v3/zz_a_report.py"""
import json, os, re, sys, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE)); sys.path.insert(0, HERE)
SCR = '/tmp/claude-0/-home-user-OXPogg/aa240b69-cc21-5263-8573-be2969435207/scratchpad/a2_targets_a.json'
d = json.load(open(SCR))
norm = lambda s: re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', s.lower()).encode('ascii', 'ignore').decode())
use = {norm(o) for o in d['obras_em_uso']}
from v3 import zz_a_lib as Z
import v3.zz_a_d1, v3.zz_a_d2, v3.zz_a_d3, v3.zz_a_d4, v3.zz_a_d5
T = [t['n'] for t in d['targets']]
miss = [n for n in T if n not in Z.SPECS]; extra = [n for n in Z.SPECS if n not in T]
print('alvos:', len(T), '| feitos:', len(Z.SPECS), '| faltam:', miss, '| fora da lista:', extra)
seen = {}; bad = 0
for n in T:
    if n not in Z.SPECS: continue
    nm = Z.SPECS[n]['ob'][0]; k = norm(nm)
    if ':' in nm: print('TITULO COM DOIS-PONTOS', n, nm); bad += 1
    if k in use: print('COLIDE com obras_em_uso:', n, nm); bad += 1
    if k in seen: print('REPETIDA entre alvos:', n, seen[k], nm); bad += 1
    seen[k] = n
print('obras novas distintas:', len(seen), '| problemas:', bad)

# --- (2) nenhum quadro do episódio cita a obra, o elenco ou as palavras do texto antigo ---
import glob, importlib, json as _j
STOP = set('the and with from that this have what when your you are for not but can will was were all its his her they them their who how where which there here some more most very just about into over than then also only each other every'.split())
tk = lambda t: set(w for w in re.findall(r"[a-zà-ú']+", t.lower()) if len(w) > 3 and w not in STOP)
from v3 import ova2, ova2b
mods = {}
for f in sorted(glob.glob(os.path.join(HERE, 'a2_*.py'))):
    mods[os.path.basename(f)[:-3]] = f
new = {}; old = {}
for m in mods:
    mod = importlib.import_module('v3.' + m)
    for e in mod.EPS:
        if e['n'] in T: new[e['n']] = _j.dumps(e, ensure_ascii=False, default=str)
saved = (dict(ova2.OVR), dict(ova2b.OVR), dict(ova2b.GX))
ova2.OVR.clear(); ova2b.OVR.clear(); ova2b.GX.clear()
for m in mods:
    mod = importlib.reload(importlib.import_module('v3.' + m))
    for e in mod.EPS:
        if e['n'] in T: old[e['n']] = _j.dumps(e, ensure_ascii=False, default=str)
leaks = 0
for n in T:
    S = Z.SPECS[n]
    o = old[n]
    m_ = re.search(r"'name': '([^']+)'|\"name\": \"([^\"]+)\"", o)
    oldobra = (m_.group(1) or m_.group(2)) if m_ else ''
    oldtok = tk(oldobra)
    keep = tk(_j.dumps(S, ensure_ascii=False))
    hit = sorted((oldtok - keep) & tk(new[n]))
    if hit: leaks += 1; print('CITA-OBRA-ANTIGA', n, oldobra, hit)
print('episódios cujo texto ainda cita a obra antiga:', leaks)
nm = [n for n in T if Z.SPECS[n]['ob'][0] not in new[n]]
print('episódios cuja obra nova NÃO aparece na montagem:', nm)
