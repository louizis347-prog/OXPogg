#!/usr/bin/env python3
"""Valida um arquivo de base de obras: python3 tools/cult/check_kb.py tools/cult/kb/en-a1_0.json [chunk]"""
import json,sys
MODES={'page','quote','scene'}
def check(kb,chunk=None):
    err=[]
    names=[w['work'] for w in chunk] if chunk else None
    if names:
        for n in names:
            if n not in kb: err.append('falta: '+n)
        for n in kb:
            if n not in names: err.append('obra desconhecida: '+n)
    for n,w in kb.items():
        p=lambda m:err.append('%s: %s'%(n,m))
        for k in('kind','by','blurb','cena','q'):
            if k not in w: p('sem '+k)
        if not isinstance(w.get('y1'),int): p('y1 inteiro')
        if not isinstance(w.get('pd'),bool): p('pd booleano')
        if len(w.get('blurb',''))>130: p('blurb >130')
        c=w.get('cena') or {}
        m=c.get('mode')
        if m not in MODES: p('mode inválido');continue
        L=c.get('lines') or []
        if m=='page' and not(2<=len(L)<=6): p('page pede 2-6 linhas')
        if m=='page' and not w.get('pd'): p('page só para domínio público')
        if m=='quote' and not(1<=len(L)<=2): p('quote pede 1-2 linhas')
        if m=='scene' and L: p('scene não tem linhas')
        for l in L:
            if len(l)!=3 or not l[0] or not l[1]: p('linha malformada %r'%(l,))
            elif m=='quote' and len(l[0].split())>18: p('fala longa: '+l[0])
        if not c.get('ctx'): p('sem ctx')
        if m!='scene' and not c.get('src'): p('sem src')
        for h in c.get('hl') or []:
            if not any(h.lower() in l[0].lower() for l in L): p('hl fora das linhas: '+h)
        q=w.get('q') or {}
        if not(q.get('q') and isinstance(q.get('o'),list) and len(q['o'])==3 and isinstance(q.get('a'),int) and 0<=q['a']<3 and q.get('why')): p('q malformada')
    return err
if __name__=='__main__':
    kb=json.load(open(sys.argv[1]));chunk=json.load(open(sys.argv[2])) if len(sys.argv)>2 else None
    e=check(kb,chunk)
    print('ok %d obras'%len(kb) if not e else 'ERROS:\n'+'\n'.join(e[:40]));sys.exit(1 if e else 0)
