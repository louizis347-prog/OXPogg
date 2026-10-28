#!/usr/bin/env python3
"""Aplica a trava editorial da ponte cultural em todo o inglês regular.

Cada episódio precisa explicar, em linguagem editorial, como a obra leva ao
foco da aula. A1–B2 usam a descrição da obra como ponte; C1–C2 também têm um
quadro ``bridge``, que recebe texto contextualizado e não apenas um rótulo
genérico. O script também reutiliza as variações de boilerplate do auditor.
"""
from __future__ import annotations

import glob
import json
import os
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "audit"))
import fix_en_editorial as base  # noqa: E402

COURSES = ("en-a1", "en-a2", "en-b1", "en-b2", "en-c1", "en-c2")

# Variações específicas da camada cultural que ainda era fixa em C1/C2.
base.VARIANTS.update(
    {
        "A obra de hoje": [
            "A referência desta aula",
            "O ponto de partida cultural",
            "A obra que abre a missão",
            "A lente cultural de hoje",
            "A história por trás da língua",
            "A obra em foco",
            "O contexto que inicia a aula",
            "A primeira pista cultural",
        ],
        "Conheça a obra de hoje!": [
            "Conheça a referência que abre a missão!",
            "Entre no contexto cultural da aula!",
            "Veja de onde nasce a situação de hoje!",
            "Descubra a obra que ilumina o foco!",
            "Comece pela história por trás da língua!",
            "Observe a referência antes de praticar!",
            "A cultura abre o caminho: conheça a obra!",
            "Veja a obra que dá contexto ao episódio!",
        ],
        "Por dentro da obra": [
            "Contexto e detalhes da obra",
            "O que a obra revela",
            "Uma camada a mais da referência",
            "A obra em perspectiva",
            "Detalhes para observar",
            "A história por trás da cena",
            "Leia a referência com mais atenção",
            "O contexto que sustenta a aula",
        ],
        "Curiosidade": [
            "O que vale observar",
            "Um detalhe para levar",
            "Pista cultural",
            "Você sabia?",
            "Contexto em foco",
            "Uma camada histórica",
            "Olhar de pesquisador",
            "Detalhe que muda a leitura",
        ],
        "Como entrar": [
            "Como se aproximar da obra",
            "Uma porta de entrada",
            "Para continuar explorando",
            "Aproxime-se do contexto",
            "Se quiser ver mais",
            "Próximo passo cultural",
            "Uma sugestão de exploração",
            "Leve a obra para fora da aula",
        ],
        "Abra cada cartão e descubra mais!": [
            "Abra os cartões e escolha uma pista para investigar!",
            "Explore cada cartão e encontre um detalhe novo!",
            "Toque nos cartões para ampliar o contexto!",
            "Passe pelos cartões e conecte as ideias!",
            "Descubra o que cada cartão acrescenta à obra!",
            "Leia os cartões na ordem que fizer sentido para você!",
            "Cada cartão guarda uma pista cultural: explore!",
            "Abra uma pista e leve-a para a conversa!",
        ],
        "Cena da obra": [
            "A obra em uma situação",
            "Cena e contexto",
            "O momento cultural",
            "Uma cena para interpretar",
            "A referência em movimento",
            "Da obra para a situação",
            "O contexto ganha voz",
            "Leia a cena pela lente da obra",
        ],
        "Situações novas": [
            "O foco em novas situações",
            "Transferência para outros contextos",
            "A mesma ideia, outro cenário",
            "Prática além da obra",
            "Quando o foco muda de lugar",
            "Leve a linguagem adiante",
            "Novos contextos para o mesmo recurso",
            "Use o que aprendeu em outra situação",
        ],
        "Ouça cada situação e complete com as palavras certas.": [
            "Escute cada contexto e complete a fala que falta.",
            "Ouça as situações e recupere as palavras-chave.",
            "Acompanhe o áudio e preencha cada lacuna.",
            "Identifique as palavras no contexto de cada cena.",
            "Escute, reconstrua e confira as frases.",
            "Use o áudio para completar as situações.",
            "Descubra pelo som qual palavra fecha cada fala.",
            "Preste atenção ao contexto e complete as frases.",
        ],
        "Bridge to the lesson": [
            "Da obra para a linguagem",
            "A ponte para o foco",
            "Onde cultura e língua se encontram",
            "Do contexto à prática",
            "A ideia que vira linguagem",
            "Cultura em uso",
            "Por que esta obra entra na aula",
            "Da cena ao objetivo",
        ],
        "Carry it forward": [
            "Leve a ideia adiante",
            "Continue a linha cultural",
            "Transfira o foco para outra situação",
            "Faça a ponte para o próximo passo",
            "Use a linguagem fora da obra",
            "O que continua na próxima missão",
            "Da referência para o cotidiano",
            "Próxima aplicação",
        ],
        "Next episode": [
            "Next mission",
            "Next situation",
            "What comes next",
            "On to the next scene",
            "Your next challenge",
            "The next cultural stop",
            "Keep the thread going",
            "Next step",
        ],
        "Ouça e toque na imagem certa": [
            "Escute e escolha a imagem que corresponde",
            "Ligue o áudio à figura certa",
            "Ouça a pista e toque na imagem",
            "Qual imagem combina com o som?",
            "Encontre a figura no áudio",
            "A imagem certa está no contexto",
            "Reconheça a cena pela escuta",
            "Escute e aponte para a figura",
        ],
        "Missão da obra! Vamos jogar com o que você acabou de conhecer?": [
            "Missão cultural: use o que acabou de descobrir!",
            "Desafio da obra: qual pista você leva?",
            "Jogue com o contexto e com a língua!",
            "Teste sua leitura da referência!",
            "A obra virou missão: vamos praticar!",
            "Mostre o que você percebeu na obra!",
            "Use a referência para resolver o desafio!",
            "Cultura em jogo: escolha seu caminho!",
        ],
        "Qual opção nomeia a figura?": [
            "Qual palavra nomeia a figura?",
            "Que opção corresponde à imagem?",
            "Escolha o nome que combina com a figura.",
            "Qual item você reconhece na imagem?",
            "Encontre a palavra representada.",
            "Que palavra aparece nesta figura?",
            "Ligue a imagem ao vocabulário.",
            "Qual é o nome certo para a cena?",
        ],
        "Escolha a palavra certa": [
            "Selecione a palavra que encaixa.",
            "Qual palavra completa a ideia?",
            "Escolha o vocabulário adequado.",
            "Que palavra faz sentido aqui?",
            "Marque a opção correta.",
            "Encontre a palavra que combina.",
            "Qual termo você usaria?",
            "Complete com a palavra certa.",
        ],
        "Qual é o item da cena?": [
            "Que elemento aparece na cena?",
            "Qual objeto você identifica?",
            "Encontre o item do contexto.",
            "Que palavra descreve a cena?",
            "Qual elemento está em foco?",
            "Reconheça o item mostrado.",
            "O que aparece neste cenário?",
            "Qual pista visual você encontrou?",
        ],
        "Identifique a palavra": [
            "Reconheça a palavra",
            "Encontre o termo",
            "Nomeie o vocabulário",
            "Qual palavra aparece?",
            "Descubra o item",
            "Localize a palavra na cena",
            "Diga qual é o termo",
            "Faça a identificação",
        ],
        "Encontre o vocabulário": [
            "Localize as palavras-chave",
            "Ache o vocabulário da cena",
            "Descubra os termos importantes",
            "Procure as palavras da missão",
            "Mapeie o vocabulário",
            "Reúna as palavras do contexto",
            "Qual vocabulário você encontra?",
            "Siga as pistas de palavras",
        ],
    }
)


BRIDGE_MARKERS = re.compile(
    r"\b(a aula|a referência|a cena|a obra|a pintura|o filme|o livro|a série|a canção|o poema|"
    r"o contexto da obra|a relação entre obra e foco|a relação com|o elo com|conversa diretamente|"
    r"ponto de partida|serve de ponte|the scene|the reference|connect)\b",
    re.I,
)

# Os níveis avançados ainda carregavam frases de fechamento e instruções
# idênticas em muitos cartões.  A variação abaixo mantém a mesma orientação
# pedagógica, mas muda a formulação e preserva o foco específico do episódio.
PATTERN_VARIANTS = [
    (
        "closing",
        re.compile(r"^Fechamento do episódio: retome (.+) e prepare a próxima situação\.$"),
        [
            "Feche a aula retomando {topic}; depois, leve essa ideia para a próxima situação.",
            "Antes de sair, recupere {topic} e antecipe o próximo contexto.",
            "Síntese: retome {topic}. Na próxima missão, você verá a ideia em outro cenário.",
            "Volte a {topic}, diga uma frase sua e prepare-se para continuar.",
            "Última parada: {topic}. Guarde a estratégia para a próxima situação.",
            "Recupere {topic} com uma frase e siga para o próximo desafio.",
            "Fechamento: o que {topic} muda na prática? A próxima situação parte daí.",
            "Retome {topic} e observe como o próximo episódio desloca o foco.",
        ],
    ),
    (
        "culture_entry",
        re.compile(r"^Para entrar na obra: Procure o trailer ou uma cena curta com legendas em inglês\. Depois, assista ao filme inteiro com pipoca!$"),
        [
            "Para entrar na obra: veja um trecho curto com legendas em inglês e observe o contexto antes de praticar.",
            "Uma porta de entrada: assista a uma cena breve com legendas em inglês e anote um detalhe que chamou sua atenção.",
            "Explore a referência: comece por um trecho legendado e volte à cena quando a linguagem aparecer na aula.",
            "Antes da prática, conheça a obra em movimento: escolha uma cena curta com legendas em inglês.",
            "Leve a obra para fora da tela: veja um trecho com legendas e compare a situação com a missão do episódio.",
            "Para ampliar o contexto, procure uma cena curta legendada e repare no tom dos personagens.",
        ],
    ),
    (
        "culture_entry_short",
        re.compile(r"^Procure o trailer ou uma cena curta com legendas em inglês\. Depois, assista ao filme inteiro com pipoca!$"),
        [
            "Veja um trecho curto com legendas em inglês e observe o contexto antes de praticar.",
            "Comece por uma cena breve com legendas; depois, retome a referência ao revisar a linguagem.",
            "Escolha um trecho legendado e anote um detalhe que ajude a entender a situação.",
            "Explore a obra em uma cena curta e preste atenção ao tom e às relações entre os personagens.",
        ],
    ),
    (
        "why",
        re.compile(r"^Hoje vamos entender o porquê do que você aprendeu!$"),
        [
            "Agora descubra por que essa escolha funciona no contexto.",
            "Vamos voltar ao exemplo e entender o efeito da linguagem.",
            "Hora de ligar a forma ao sentido que ela produz.",
            "Releia a situação e perceba o motivo de cada escolha.",
            "O próximo passo é explicar por que a frase soa natural aqui.",
            "Conecte a regra à intenção comunicativa da cena.",
        ],
    ),
    (
        "review_dialogue",
        re.compile(r"^Ouça o diálogo do episódio anterior no player\. Depois toque numa fala-peça e no espaço onde ela encaixa\.$"),
        [
            "Reouça o diálogo anterior e encaixe cada fala no lugar em que ela completa a situação.",
            "Volte ao áudio da missão passada: escolha uma fala e descubra onde ela entra na conversa.",
            "Escute o episódio anterior, selecione um trecho e reconstrua a ordem da interação.",
            "Use o player para recuperar a conversa anterior e posicione cada fala no contexto certo.",
        ],
    ),
    (
        "listen_words",
        re.compile(r"^Leia e ouça\. As palavras sublinhadas são as de hoje!$"),
        [
            "Leia acompanhando o áudio e note as palavras destacadas nesta missão.",
            "Ouça a frase, acompanhe a leitura e localize o vocabulário em foco.",
            "Siga o áudio com os olhos: as palavras marcadas reaparecem na prática.",
            "Leia junto com a gravação e observe como o vocabulário funciona na frase.",
        ],
    ),
    (
        "hidden_word",
        re.compile(r"^Cada frase esconde uma palavra de hoje\. Toque na figura para revelar!$"),
        [
            "Cada frase guarda uma palavra da missão. Toque na figura para descobri-la.",
            "Encontre o vocabulário escondido em cada frase e revele a pista na imagem.",
            "As frases trazem uma palavra em foco: toque na figura e confira o sentido.",
            "Procure a palavra da aula em cada frase; a imagem mostra quando você acertar.",
        ],
    ),
    (
        "produce",
        re.compile(r"^Produzir é a melhor forma de lembrar: fale em voz alta e depois escreva\.$"),
        [
            "Fale a sua resposta em voz alta e depois registre-a por escrito.",
            "Transforme a compreensão em produção: diga a frase e escreva uma versão sua.",
            "Use a linguagem ativamente: primeiro pronuncie, depois escreva e revise.",
            "Agora é sua vez: produza a frase oralmente e confira a forma escrita.",
        ],
    ),
]


def num_o(e):
    try:
        return float(e.get("o"))
    except (TypeError, ValueError):
        return None


def focus_text(e):
    p = str(e.get("p", "") or e.get("s", "") or e.get("t", "")).strip().rstrip(".")
    p = re.sub(r"^Hoje você aprende\s+", "", p, flags=re.I)
    p = re.sub(r"^a\s+", "", p, flags=re.I)
    p = re.sub(r"^Você vai treinar\s+", "treinar ", p, flags=re.I)
    return p[:320]


def ensure_description_bridge(e, seed):
    a = e.setdefault("a", {})
    d = str(a.get("d", "")).strip()
    if not d:
        return False
    if BRIDGE_MARKERS.search(d):
        return False
    work = str(a.get("w", "a obra") or "a obra").strip()
    focus = focus_text(e)
    if not focus:
        return False
    templates = [
        "A referência {work} conversa com o foco da aula: “{focus}”.",
        "A cena cultural de {work} vira prática linguística quando o estudante trabalha “{focus}”.",
        "O contexto de {work} prepara a situação para praticar “{focus}”.",
        "A obra {work} oferece uma ponte concreta para “{focus}”.",
        "O episódio parte de {work} e leva o estudante a usar “{focus}” em contexto.",
        "A relação com {work} aparece na missão: transformar “{focus}” em linguagem de uso.",
        "A referência {work} dá sentido à prática de “{focus}” nesta situação.",
        "A aula retorna a {work} para explorar “{focus}” de forma aplicada.",
    ]
    sentence = templates[seed % len(templates)].format(work=work, focus=focus)
    a["d"] = d + (" " if d.endswith((".", "!", "?")) else ". ") + sentence
    return True


def cultural_anchor(e):
    # A cena/curiosidade costuma trazer a ligação mais concreta; prefira-a ao
    # registro bibliográfico curto de alguns episódios legados.
    frames = e.get("fr", [])
    # ``cultcena.ctx`` é a formulação editorial curta e já foi escrita para
    # caber no cartão.  Usá-la primeiro evita que um parágrafo de leitura seja
    # cortado no meio de uma palavra quando entra no link da ponte.
    for key in ("cultcena", "cultx", "cultob"):
        fr = next((x for x in frames if x.get("k") == key), None)
        if not fr:
            continue
        if key == "cultx":
            tiles = fr.get("tiles") or []
            if tiles and isinstance(tiles[0], dict) and tiles[0].get("t"):
                raw = str(tiles[0]["t"])
            else:
                raw = ""
        elif key == "cultob":
            panels = fr.get("panels") or []
            raw = str(panels[0]) if panels else str(fr.get("hook") or "")
        else:
            raw = str(fr.get("ctx") or "")
        if raw:
            raw = re.split(r"\s+Aqui(?:,| a obra| a referência)|\s+Na aula", raw, maxsplit=1, flags=re.I)[0]
            raw = re.sub(r"\s+", " ", raw).strip().rstrip(".")
            if raw:
                # Mantém a última frase inteira se uma fonte legada ainda
                # trouxer um contexto mais longo.
                if len(raw) > 300:
                    raw = raw[:300].rsplit(" ", 1)[0].rstrip(" ,;:—-")
                return raw
    return str(e.get("a", {}).get("d", "")).strip()[:300]


def update_bridge_frame(e, seed):
    frames = e.get("fr", [])
    bridge = next((x for x in frames if x.get("k") == "bridge"), None)
    if bridge is None:
        return False
    work = str(e.get("a", {}).get("w", "") or bridge.get("work", "a obra")).strip()
    topic = str(bridge.get("topic") or e.get("s") or e.get("t") or "o objetivo da aula").strip().rstrip(".")
    anchor = cultural_anchor(e)
    templates = [
        "{work} oferece este contexto: {anchor}. A aula transforma essa situação em prática de {topic}.",
        "A referência {work} apresenta {anchor}. O estudante leva essa ideia para uma situação de {topic}.",
        "Partimos de {work}: {anchor}. Depois, a linguagem de {topic} entra em uma tarefa concreta.",
        "A cena de {work} ajuda a perceber {anchor}. Esse contexto sustenta a prática de {topic}.",
        "Em {work}, {anchor}. Na aula, essa tensão/ideia vira uso de {topic}.",
        "A obra {work} não fica como decoração: {anchor}. Por isso, praticamos {topic} em contexto.",
        "A ponte é explícita: {work} mostra {anchor}, e a missão trabalha {topic} a partir daí.",
        "Do contexto de {work} — {anchor} — passamos à linguagem de {topic}.",
    ]
    text = templates[seed % len(templates)].format(work=work, anchor=anchor, topic=topic)
    coach_templates = [
        "Relacione a obra {work} ao foco {topic}; peça ao estudante que explique essa ligação.",
        "Mostre como {work} dá contexto para {topic} antes da produção livre.",
        "Use a situação de {work} para justificar a escolha linguística em {topic}.",
        "Peça uma frase que atravesse a ponte entre {work} e {topic}.",
        "Compare a situação de {work} com uma situação real em que {topic} seja necessário.",
        "Faça o estudante nomear o detalhe de {work} que torna {topic} relevante.",
        "Retome {work} durante a prática e conecte cada exemplo a {topic}.",
        "Encerre pedindo uma aplicação de {topic} inspirada pelo contexto de {work}.",
    ]
    changed = False
    if bridge.get("work") != work:
        bridge["work"] = work; changed = True
    new_title = base.VARIANTS["Bridge to the lesson"][seed % len(base.VARIANTS["Bridge to the lesson"])]
    if bridge.get("title") != new_title:
        bridge["title"] = new_title; changed = True
    if bridge.get("text") != text:
        bridge["text"] = text; changed = True
    coach = coach_templates[seed % len(coach_templates)].format(work=work, topic=topic)
    if bridge.get("coach") != coach:
        bridge["coach"] = coach; changed = True
    # A cena cultural deve repetir a mesma ponte no campo mostrado ao aluno.
    cult = next((x for x in frames if x.get("k") == "cultcena"), None)
    if cult is not None:
        link = f"Na lição, {work} conversa diretamente com {topic}: {anchor}."
        if cult.get("link") != link:
            cult["link"] = link; changed = True
        ccoach = f"Interprete a situação de {topic}; depois explique como ela nasce do contexto de {work}."
        if cult.get("coach") != ccoach:
            cult["coach"] = ccoach; changed = True
    for key in ("cultob", "cultx", "cultgame"):
        fr = next((x for x in frames if x.get("k") == key), None)
        if fr is not None:
            coach2 = f"Conecte {work} ao foco {topic} e diga qual detalhe cultural sustenta essa escolha."
            if fr.get("coach") != coach2:
                fr["coach"] = coach2; changed = True
    return changed


def vary_boilerplate(value, seed):
    counters = Counter()

    def rec(x):
        if isinstance(x, str):
            for key, pattern, pool in PATTERN_VARIANTS:
                match = pattern.match(x)
                if not match:
                    continue
                pos = (seed + counters[key]) % len(pool)
                counters[key] += 1
                topic = match.group(1).strip() if match.groups() else ""
                return pool[pos].format(topic=topic)
            return x
        if isinstance(x, list):
            return [rec(y) for y in x]
        if isinstance(x, dict):
            return {k: rec(v) for k, v in x.items()}
        return x

    return rec(value)


def process(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    stats = Counter(episodes=len(data))
    for e in data:
        seed = int(abs(float(e.get("n", 0)))) if num_o(e) is not None else 0
        if ensure_description_bridge(e, seed):
            stats["description_bridges"] += 1
        if update_bridge_frame(e, seed):
            stats["bridge_frames"] += 1
        before = json.dumps(e, ensure_ascii=False, separators=(",", ":"))
        updated = base.walk_replace(e, seed)
        updated = vary_boilerplate(updated, seed)
        after = json.dumps(updated, ensure_ascii=False, separators=(",", ":"))
        if before != after:
            stats["boilerplate_episodes"] += 1
        e.clear(); e.update(updated)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    os.replace(tmp, path)
    return stats


def main():
    total = Counter()
    for course in COURSES:
        for name in sorted(glob.glob(str(ROOT / "data" / f"{course}_*.json"))):
            stats = process(Path(name))
            total.update(stats)
            print(Path(name).name, dict(stats))
    print("TOTAL", dict(total))


if __name__ == "__main__":
    main()
