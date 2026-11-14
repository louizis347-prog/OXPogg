#!/usr/bin/env python3
"""Registra a referência cultural ('Cena da obra') de uma aula A2.
Uso: python3 /tmp/gen/obra.py NNNN "Título da obra" ANO "Nota em português (150–360 caracteres)"
A nota deve resumir a obra (filme, livro, música, série, pintura, prédio, festa, tradição) e ligá-la à situação da aula."""
import sys,json,os,glob,re
def titles(skip=None):
    s={}
    for f in glob.glob('/home/user/OXPogg/professor/data/v4/[0-9]*.json'):
        try:
            d=json.load(open(f))
            if d['n']==skip: continue
            for p in d['pages']:
                if p['kind']=='work': s.setdefault(p['work']['title'].lower(),d['n'])
        except Exception: pass
    return s
def register(n,w,y,note,write=True):
    SUF=' A cena desta aula é original; não reproduz a obra.'
    err=[]
    note=note.strip()
    if SUF.strip() not in note:
        note=note.rstrip()+SUF
    if len(note)>420: err.append('nota longa demais (%d); máx. 420 com a frase final'%len(note))
    if len(note)<150: err.append('nota curta demais')
    if y and not re.fullmatch(r'\d{3,4}',y): err.append('ano deve ter 3–4 dígitos ou ser vazio')
    used=titles(skip=n)
    for f in glob.glob('/tmp/gen/obras/*.json'):
        if os.path.basename(f)!='%d.json'%n:
            o=json.load(open(f)); used.setdefault(o['w'].lower(),os.path.basename(f))
    if w.lower() in used: err.append('obra já usada em %s: escolha outra'%used[w.lower()])
    if err: print('OBRA?',n,err); return False
    if write: json.dump({'w':w,'y':y,'d':note},open('/tmp/gen/obras/%d.json'%n,'w'),ensure_ascii=False)
    return True
if __name__=='__main__':
    n=int(sys.argv[1]); ok=register(n,sys.argv[2],sys.argv[3],sys.argv[4])
    print('obra %d ok'%n if ok else 'FALHOU')
