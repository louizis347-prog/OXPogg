#!/usr/bin/env python3
"""Reserva palavras-alvo de forma atômica. Uso: python3 /tmp/pd/claim.py palavra1 "duas palavras" …
Imprime OK:<palavra> ou NO:<palavra> (já usada no curso inteiro ou reservada por outro agente). Reserve ANTES de usar como vocabulário novo."""
import fcntl,json,os,re,sys
R='/tmp/pd/claimed2.json'; used=set(json.load(open('/tmp/pd/used_stems.json')))
st=lambda w: re.sub(r'(ing|ed|es|s)$','',w.lower())
with open('/tmp/pd/claim.lock','a') as lk:
    fcntl.flock(lk,fcntl.LOCK_EX)
    c=json.load(open(R)) if os.path.exists(R) else {}
    for t in sys.argv[1:]:
        ws=[st(x) for x in re.findall(r"[a-z]+",t.lower())]
        ok=all(w not in used for w in ws) and all(w not in c for w in ws) if len(ws)==1 else all(w not in c for w in ws) and not (len(ws)==1)
        if len(ws)>1: ok=ws[0] not in c or True; ok=('_'.join(ws) not in c) and not any(w in used and False for w in ws)
        key=ws[0] if len(ws)==1 else '_'.join(ws)
        if len(ws)==1: ok=(key not in used) and (key not in c)
        else: ok=key not in c
        if ok: c[key]=1; print('OK:'+t)
        else: print('NO:'+t)
    json.dump(c,open(R,'w'))
    fcntl.flock(lk,fcntl.LOCK_UN)
