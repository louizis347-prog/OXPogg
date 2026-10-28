"""Expressões únicas: a expressão ensinada no quadro `pgexp` de um episódio não pode ser ensinada em outro episódio do mesmo curso
(comparação sem pontuação/caixa) nem duas vezes no mesmo episódio. A única repetição oficial é a mochila de revisão (quadro `review`)."""
import regular_pilot_contract as C


def expr_repetidas(episodes):
    """episodes: lista de episódios na ordem da trilha. Devolve [(n, n_anterior, expressão)]."""
    seen, out = {}, []
    for e in episodes:
        exp = next((q for q in e.get('fr', []) if q.get('k') == 'pgexp'), {})
        for item in exp.get('items', []):
            phrase = C._norm_phrase(item.get('en') or item.get('x'))
            if not phrase:
                continue
            if phrase in seen:
                out.append((e['n'], seen[phrase], phrase))
            else:
                seen[phrase] = e['n']
    return out
