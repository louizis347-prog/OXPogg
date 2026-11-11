#!/bin/bash
cd /home/user/OXPogg/professor/src
for n in "$@"; do
 o=$(python3 /tmp/gen/g$n.py 2>&1 | tail -2)
 r=""; for v in x y z v5; do r="$r$(python3 validate_$v.py $n 2>&1 | grep -v -e '^aulas com erro' -e '^AULA' -e '^ok$' | head -3)"; done
 [ -z "$r" ] && [ -z "$o" ] && echo "$n ok" || echo "$n FAIL: $o $r"
done
