#!/usr/bin/env python3
"""Conta quantos arquivos o Cloudflare publica (arquivos do git que não casam com .assetsignore).
O plano gratuito do Workers aceita no máximo 20.000 arquivos de ativos estáticos por versão (erro 10304).
Uso: python3 tools/count_assets.py [commit]   (padrão: HEAD).  Precisa de: pip install pathspec"""
import os, subprocess, sys
import pathspec
root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sha = sys.argv[1] if len(sys.argv) > 1 else 'HEAD'
files = [f for f in subprocess.run(['git', '-C', root, 'ls-tree', '-r', '--name-only', sha], capture_output=True, text=True).stdout.split('\n') if f]
rules = subprocess.run(['git', '-C', root, 'show', sha + ':.assetsignore'], capture_output=True, text=True).stdout.split('\n')
spec = pathspec.PathSpec.from_lines('gitwildmatch', rules)
kept = [f for f in files if not spec.match_file(f)]
tops = {}
for f in kept: tops[f.split('/')[0] + ('/' + f.split('/')[1] if f.count('/') > 1 else '')] = tops.get(f.split('/')[0] + ('/' + f.split('/')[1] if f.count('/') > 1 else ''), 0) + 1
print('arquivos publicados:', len(kept), '(limite 20.000)')
for k, v in sorted(tops.items(), key=lambda x: -x[1])[:8]: print('  ', v, k)
