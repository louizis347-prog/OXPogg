#!/bin/bash
# uso: ship.sh "mensagem"  — reconstrói, atualiza disponibilidade, versiona dados, commita e publica
cd /home/user/OXPogg
python3 tools/pocket/build.py >/dev/null
N=$(python3 -c "import json;print(sum(len(json.load(open(f))) for f in __import__('glob').glob('data/pk-a1_*.json')))")
N2=$(python3 -c "import json;print(sum(len(json.load(open(f))) for f in __import__('glob').glob('data/pk-a2_*.json')))")
python3 - <<P
import json
p='data/availability.json'; d=json.load(open(p)); d['pk-a1']={'total':$N,'available':$N}; d['pk-a2']={'total':$N2,'available':$N2}
json.dump(d,open(p,'w'),ensure_ascii=False,separators=(',',':'))
P
V=$(grep -o "pogglot-data-v[0-9]*" sw.js | head -1 | grep -o "[0-9]*$"); sed -i "s/pogglot-data-v$V/pogglot-data-v$((V+1))/" sw.js
git add -A && git commit -qm "$1

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_013v8eLp8o41uwZPfWEpThz4"
git fetch -q origin main
if ! git merge origin/main >/dev/null 2>&1; then
  git checkout --theirs data/manifest.json data/counts.json; python3 tools/pocket/build.py >/dev/null
  git add -A; git commit -qm "Merge origin/main

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_013v8eLp8o41uwZPfWEpThz4"
fi
git push -q origin HEAD:claude/nifty-mendel-y3nbxt && git push -q origin HEAD:main && echo "enviado: $N episódios"
