#!/usr/bin/env python3
"""Trava das capas por ficha: nos cursos de tools/ficha/gate_cursos.json toda obra (exceto as de arte à mão) precisa ter ficha válida,
sem combinação repetida (personagens + objeto + cenário); e js/fichas-<curso>.js precisa estar sincronizado com tools/ficha/work/.
Uso: python3 tools/audit/ficha_gate.py"""
import json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE)); FH = os.path.join(ROOT, 'tools', 'ficha')
cursos = json.load(open(os.path.join(FH, 'gate_cursos.json')))['cursos']
bad = 0
for c in cursos:
    r = subprocess.run([sys.executable, os.path.join(FH, 'validate.py'), '--curso', c, '--todos'], capture_output=True, text=True)
    print(r.stdout.strip().splitlines()[-1] if r.stdout.strip() else '(sem saída)')
    if r.returncode: print(r.stdout[-2000:]); bad += 1
    js = os.path.join(ROOT, 'js', 'fichas-%s.js' % c)
    before = open(js, encoding='utf-8').read() if os.path.exists(js) else ''
    subprocess.run([sys.executable, os.path.join(FH, 'build.py'), c], capture_output=True)
    after = open(js, encoding='utf-8').read() if os.path.exists(js) else ''
    if before != after:
        open(js, 'w', encoding='utf-8').write(before); print('ERRO: js/fichas-%s.js desatualizado (rode tools/ficha/build.py %s)' % (c, c)); bad += 1
    r = subprocess.run(['node', os.path.join(FH, 'check_render.js'), c], capture_output=True, text=True)
    print(r.stdout.strip())
    if r.returncode: bad += 1
print('trava das capas por ficha:', 'FALHOU' if bad else 'ok (%d curso(s))' % len(cursos))
sys.exit(1 if bad else 0)
