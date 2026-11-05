#!/bin/bash
# Reconstrói todas as aulas na ordem do currículo (apaga as aulas geradas e roda os lotes em sequência)
set -e
cd "$(dirname "$0")"
rm -f ../../data/livro/lessons/[ABC]*.json
for f in a0_u1 a0_b1 a0_rv1 a0_b2 a0_rv2 a0_b3a a0_b3b a1_b1 a1_b2 a1_b3 a1_b4 a1_b5 a1_b6 a1_b7 a1_b8 a1_b9 a1_b10 a1_b11 a2_b1 a2_b2 a2_b3 a2_b4 a2_b5 a2_b6 a2_b7 a2_b8 a2_b9 a2_b10 b1_a b1_b b1_c b1_d b1_e b1_f b1_g b1_h b1_i b1_j b1_k b1_l b1_m b1_n b1_o b2_a b2_b b2_c b2_d b2_e b2_f x1_a x1_b x1_c x1_d x1_e x1_f x1_g x2_a x2_b x2_c x2_d x2_e x2_f x3_a x3_b x3_c x3_d x3_e x3_f x3_g x3_h x3_i x3_j x3_k x4_a x4_b x4_c x4_d x4_e x4_f y1_a y1_b y1_c y1_d y2_a y2_b y2_c y2_d y2_e y2_f y3_a y3_b y3_c y3_d y3_e $EXTRA; do python3 $f.py >/dev/null || { echo "FALHOU em $f"; exit 1; }; done
python3 -c "from card import *;build_index()"
ls ../../data/livro/lessons | wc -l
