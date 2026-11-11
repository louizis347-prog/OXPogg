#!/bin/bash
cd /home/user/OXPogg/professor
N="$*"
./tools/finish.sh $N 2>&1 | tail -1
cp /tmp/gen/pt.js _p.js; NODE_PATH=$(npm root -g) timeout 900 node _p.js $N 2>&1 | tail -1 | tr -d '\n' | cut -c1-900; echo; rm -f _p.js
python3 tools/vocab_registry.py $N 2>&1 | awk '{print $1,$2,$4}' | tr '\n' ';'
