#!/usr/bin/env python3
"""Diversifica o parceiro de conversa do Painel: troca o nome exibido do parceiro (ex.: Kofi, que aparece em 75 aulas)
por outro personagem do elenco, fixo por aula, do MESMO gênero, em todo o texto da aula (falas, vocativos, capa, roteiro).
- Mantém o parceiro em aulas com mais de um parceiro e em aulas cujo nome também é palavra comum (Grace, Hope, Will, May…).
- Evita nomes que já aparecem no texto da aula (inclui a aprendiz, ver diversify_learner.py).
- Registro em data/partner_names.json (idempotente).
Rodar DEPOIS de diversify_learner.py (e depois de validate_x|y|z, apply_live.py e da correção de nomes).
Uso: python3 tools/diversify_partner.py [N ...]"""
import glob, json, os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
D = os.path.join(ROOT, 'data'); V4 = os.path.join(D, 'v4'); REG = os.path.join(D, 'partner_names.json')
AMB = {'Joy', 'Rose', 'Grace', 'Hope', 'Ray', 'Max', 'Mark', 'Bill', 'Sue', 'Will', 'May', 'Pog', 'You'}
FEM = re.compile(r"\b(she|her|hers|herself|ela|dela|nela|girl|a menina)\b", re.I)
MAS = re.compile(r"\b(he|his|him|himself|ele|dele|nele|boy|o menino)\b", re.I)
FEMSET = set('Mia Elena Rosa Tess Alma Dana Nell Lena Fay Grace Eva Bia Zoe Nina Clara Luisa Ana Sara Lily Emma Maya Lucia Mei Kate Nora Amy Hana Ida Suri Ruth Nadia Kira Mona Naomi Yuki Dani Lia Rita Jade Lara Sofia Kai Hanna Ines Lea Lola Maria Anna Julia Helen Alice Jess Meg Beth Amina Leila Amara Priya Chloe Nia Camila Aisha Hannah Zara Isabel Fatima Elsa Rina Tamara Bianca Dalia Esther Freya Gita Imani Keisha Lina Marta Noor Olivia Paloma Selma Thais Uma Vera Wanda Ximena Yara Zainab Ingrid Mina Carmen Tara Sade'.split())
MALESET = set('Hal Blake Carl Gabe Dirk Felix Cal Theo Leo Ben Dan Max Rui Paulo Sam Tom Ken Cody Marco Will Kofi Diego Jack Omar Raj Carlos Ali Paul Joe Luis Ivan Sami Hugo Tariq Evan Mark Bill Ray Lucas Kenji Andre Mateo Samir Noah Ravi Tomas Victor Wei Yusuf Zane Amir Bruno Chen Dario Emeka Felipe Gael Hiro Idris Jonas Kwame Luca Mohamed Nico Oscar Pedro Jin Kim Ola Tim'.split())

def walk(x, out):
    if isinstance(x, str): out.append(x)
    elif isinstance(x, list):
        for i in x: walk(i, out)
    elif isinstance(x, dict):
        for v in x.values(): walk(v, out)

def hsh(s):
    x = 2166136261
    for ch in str(s): x = ((x ^ ord(ch)) * 16777619) & 0xFFFFFFFF
    return x

def gender_of(name, e):
    if e and e.get('g') in ('f', 'm'): return e['g']
    if name in FEMSET: return 'f'
    if name in MALESET: return 'm'
    look = (e or {}).get('look', {})
    if look.get('outfit') == 'dress' or look.get('hs') in ('pigtails', 'braids', 'ponytail', 'long', 'bun', 'bob'): return 'f'
    return None

def main(ns):
    el = json.load(open(os.path.join(D, 'elenco.json'), encoding='utf-8')); E = {e['name']: e for e in el}
    pool = [(n, gender_of(n, E[n])) for n in E if n not in AMB]
    reg = json.load(open(REG)) if os.path.exists(REG) else {}
    changed = skipped_amb = skipped_multi = 0
    for f in sorted(glob.glob(os.path.join(V4, '[0-9]*.json'))):
        n = int(re.search(r'(\d+)\.json$', f).group(1))
        if ns and n not in ns: continue
        raw = open(f, encoding='utf-8').read(); d = json.loads(raw); sp = d['dialog']['speakers']
        npc = [k for k in sp if k != 'You']
        if len(npc) != 1: skipped_multi += 1; continue
        old = sp[npc[0]]['name']; key = str(n); r = reg.get(key)
        if r:
            if r['old'] != old and r['new'] == old: continue          # já trocado
            if r['old'] != old: r = None
        if not r:
            if old in AMB: skipped_amb += 1; continue
            ss = []; walk(d, ss); near = [s for s in ss if re.search(r'\b%s\b' % re.escape(old), s)]
            g = 'f' if any(FEM.search(s) for s in near) else ('m' if any(MAS.search(s) for s in near) else gender_of(old, E.get(old)))
            if any(FEM.search(s) for s in near) and any(MAS.search(s) for s in near): g = gender_of(old, E.get(old)) or g
            cands = [p for p in pool if (g is None or p[1] == g or p[1] is None and False) and p[0] != old]
            start = hsh('partner%s' % n) % len(cands); new = None
            for k in range(len(cands)):
                c = cands[(start + k) % len(cands)][0]
                if not re.search(r'\b%s\b' % re.escape(c), raw): new = c; break
            if not new: continue
            r = {'old': old, 'new': new}; reg[key] = r
        text = re.sub(r'\b%s\b' % re.escape(r['old']), r['new'], raw)
        if text != raw: open(f, 'w', encoding='utf-8').write(text); changed += 1
    json.dump(reg, open(REG, 'w', encoding='utf-8'), ensure_ascii=False, indent=0, sort_keys=True)
    print('aulas alteradas:', changed, '| mantidas (nome ambíguo):', skipped_amb, '| mantidas (vários parceiros):', skipped_multi)

if __name__ == '__main__':
    main({int(a) for a in sys.argv[1:]})
