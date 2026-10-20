#!/bin/bash
# uso: tools/ship.sh "mensagem"  — incrementa caches, valida JSON, commit e push (branch + main)
set -e
cd "$(dirname "$0")/.."
python3 - <<'P'
import re,json,glob
for f in glob.glob('data/*.json'): json.load(open(f))
s=open('sw.js').read()
s=re.sub(r"pogglot-shell-v(\d+)",lambda m:"pogglot-shell-v%d"%(int(m.group(1))+1),s,1)
s=re.sub(r"pogglot-data-v(\d+)",lambda m:"pogglot-data-v%d"%(int(m.group(1))+1),s,1)
open('sw.js','w').write(s)
h=open("app.html").read()
h=re.sub(r"(data/'\+file\+'\?v=)(\d+)",lambda m:m.group(1)+str(int(m.group(2))+1),h,1)
open("app.html","w").write(h)
P
git add -A
git commit -q -m "$1

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_012y94Tg755hdo5CTiZ4igZT"
git push -q -u origin claude/great-ride-yry4ly
git push -q origin HEAD:main
