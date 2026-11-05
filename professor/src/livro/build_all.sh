#!/bin/bash
# Reconstrói todas as aulas na ordem do currículo (apaga as aulas geradas e roda os lotes em sequência)
set -e
cd "$(dirname "$0")"
rm -f ../../data/livro/lessons/[AB]*.json
for f in a0_u1 a0_b1 a0_rv1 a0_b2 a0_rv2 a0_b3a a0_b3b a1_b1 a1_b2 a1_b3 a1_b4 a1_b5 a1_b6 a1_b7 a1_b8 a1_b9 a1_b10 a1_b11 a2_b1 a2_b2 a2_b3 a2_b4 a2_b5 a2_b6 a2_b7 a2_b8 a2_b9 a2_b10 b1_a b1_b b1_c b1_d b1_e b1_f b1_g b1_h b1_i b1_j $EXTRA; do python3 $f.py >/dev/null || { echo "FALHOU em $f"; exit 1; }; done
python3 -c "from card import *;build_index()"
ls ../../data/livro/lessons | wc -l
