#!/usr/bin/env python3
"""Corrige inconsistências editoriais do inglês regular (A1–B2).

O escopo é o pedido de auditoria: episódios com ``o >= 6``. O script é
idempotente e mantém os arquivos compactos como já estão no repositório.
"""
from __future__ import annotations

import copy
import glob
import json
import os
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSES = ("en-a1", "en-a2", "en-b1", "en-b2")


# Instruções que eram copiadas literalmente para quase todos os episódios.
# As alternativas preservam a função pedagógica e dão variedade visual/textual.
VARIANTS = {
    "Abra cada bolso da mochila e relembre o episódio anterior!": [
        "Abra a mochila e recupere o que ficou do episódio anterior!",
        "Vamos puxar da mochila as pistas da aula passada!",
        "Reveja os cartões da mochila antes de avançar!",
        "Comece reabrindo a mochila da memória!",
        "Que tal revisitar o episódio anterior pela mochila?",
        "Abra os bolsos e reative as palavras que você já encontrou!",
        "A mochila traz a ponte para a missão de hoje.",
        "Recupere as pistas guardadas e siga para a nova situação!",
    ],
    "Bora relembrar o episódio anterior antes de seguir!": [
        "Vamos recuperar a última situação antes de seguir!",
        "Primeiro, puxe da memória a missão anterior!",
        "Faça uma retomada rápida e entre na nova cena!",
        "A aula começa com uma ponte para o episódio passado.",
        "Reative as palavras anteriores e prepare a próxima missão!",
        "Antes da nova situação, confira o que já está na sua mochila!",
        "Vamos ligar a cena passada à missão de agora!",
        "Uma retomada curta prepara o próximo passo.",
    ],
    "Explore a cena": [
        "Entre na cena",
        "Veja a situação de perto",
        "Passeie pela cena",
        "Descubra o cenário",
        "Observe o momento",
        "Comece pelo cenário",
        "Encontre as pistas da cena",
        "Olhe ao redor",
    ],
    "Toque nos objetos brilhantes para ouvir o nome em inglês.": [
        "Toque nos objetos destacados e ouça seus nomes em inglês.",
        "Explore os pontos luminosos para escutar cada palavra.",
        "Aponte para os objetos e descubra como são chamados em inglês.",
        "Toque em cada pista visual e ouça a pronúncia.",
        "Os objetos acesos guardam palavras da situação: toque para ouvir.",
        "Passe pelos objetos brilhantes e confira o inglês de cada um.",
        "Ouça o nome em inglês de cada objeto destacado.",
        "Toque nas pistas do cenário e escute com atenção.",
    ],
    "Toque nos objetos brilhantes!": [
        "Toque nas pistas iluminadas!",
        "Explore os objetos destacados!",
        "Veja o que está brilhando no cenário!",
        "Encontre os objetos da situação!",
        "Comece pelas pistas visuais!",
        "Descubra os objetos escondidos na cena!",
        "Passeie pelo cenário e toque nas pistas!",
        "Observe, toque e ouça!",
    ],
    "Ouça a cena e leia junto.": [
        "Escute a cena acompanhando o texto.",
        "Leia junto enquanto a conversa acontece.",
        "Siga as falas com os olhos e com os ouvidos.",
        "Ouça primeiro; depois confira cada linha.",
        "Acompanhe a conversa no seu ritmo.",
        "Escute os personagens e leia as falas.",
        "Deixe o áudio conduzir a leitura.",
        "Ouça, leia e perceba a intenção de cada fala.",
    ],
    "Você entendeu?": [
        "Confira sua compreensão",
        "O que ficou claro?",
        "Teste o que você captou",
        "Vamos verificar a cena",
        "Hora de checar o entendimento",
        "Que detalhes você percebeu?",
        "Revise a situação",
        "Mostre o que você entendeu",
    ],
    "What do you remember?": [
        "What stands out from the scene?",
        "Which detail do you remember?",
        "What did you catch?",
        "Let’s check your recall.",
        "What can you bring back?",
        "Which line stayed with you?",
        "Can you reconstruct the moment?",
        "What do you remember from the scene?",
    ],
    "De que você se lembra?": [
        "Qual detalhe ficou na memória?",
        "O que você captou da cena?",
        "Qual fala você consegue recuperar?",
        "Vamos conferir sua lembrança.",
        "Que parte da situação voltou à memória?",
        "Você consegue reconstruir o momento?",
        "Qual pista você levaria adiante?",
        "O que ficou mais marcante?",
    ],
    "Veja o padrão com figuras e ouça os exemplos.": [
        "Observe o padrão nas figuras e escute os exemplos.",
        "As imagens revelam a estrutura; ouça como ela funciona.",
        "Veja a forma em ação e acompanhe os exemplos.",
        "Use as figuras para perceber o padrão no áudio.",
        "A estrutura aparece nas imagens e nas frases faladas.",
        "Escute os exemplos enquanto identifica o padrão.",
        "Descubra a lógica pelas figuras e pelos exemplos.",
        "Compare as imagens e ouça a construção.",
    ],
    "Molde de frases": [
        "Oficina de frases",
        "Como montar a frase",
        "Peças da estrutura",
        "Frases em construção",
        "Arquitetura da frase",
        "Monte o padrão",
        "Estrutura em movimento",
        "Frase por frase",
    ],
    "Toque nas peças e veja várias frases.": [
        "Mova as peças e compare as frases.",
        "Troque os blocos e observe o que muda.",
        "Monte combinações e veja o padrão funcionando.",
        "Experimente as peças em frases diferentes.",
        "Alterne os blocos para criar novas frases.",
        "Toque nas peças e descubra outras combinações.",
        "Construa frases e perceba a ordem das palavras.",
        "Teste a estrutura com novas combinações.",
    ],
    "Swap the pieces and build sentences!": [
        "Move the pieces and build a sentence!",
        "Change one block and watch the sentence shift!",
        "Try a new combination of pieces!",
        "Build several sentences from the same pattern!",
        "Reorder the pieces and hear the difference!",
        "Mix the blocks and test the structure!",
        "Use the pieces to make a fresh sentence!",
        "Experiment with the sentence pattern!",
    ],
    "Troque as peças e monte frases!": [
        "Mova os blocos e construa uma frase!",
        "Troque uma peça e veja a frase mudar!",
        "Teste outra combinação de peças!",
        "Monte várias frases com o mesmo padrão!",
        "Reordene os blocos e ouça a diferença!",
        "Misture as peças e confira a estrutura!",
        "Use os blocos para criar uma frase nova!",
        "Experimente o molde em outra situação!",
    ],
    "Palavras da cena": [
        "Vocabulário da situação",
        "Palavras em contexto",
        "Banco de palavras",
        "O vocabulário da missão",
        "Palavras para levar",
        "Pistas de vocabulário",
        "Palavras que aparecem na cena",
        "Vocabulário em ação",
    ],
    "Listen and choose the word!": [
        "Listen and pick the word!",
        "Hear it and choose the word!",
        "Which word did you hear?",
        "Listen for the right word!",
        "Match the sound to the word!",
        "Hear the clue and choose!",
        "Find the word in the audio!",
        "Listen closely and pick one!",
    ],
    "Ouça e escolha a palavra da figura!": [
        "Ouça e escolha a palavra certa para a figura!",
        "Escute a pista e toque na palavra!",
        "Qual palavra combina com a imagem?",
        "Relacione o som à figura!",
        "Encontre no áudio a palavra mostrada!",
        "Ouça com atenção e escolha uma opção!",
        "A figura dá a pista: qual palavra você ouviu?",
        "Ligue a palavra ao objeto da cena!",
    ],
    "Vamos ver os verbos de hoje!": [
        "Agora, coloque os verbos em ação!",
        "Vamos conhecer os verbos desta missão!",
        "Que verbos movem a cena?",
        "Hora de observar os verbos!",
        "Os verbos entram em cena agora!",
        "Vamos praticar as ações de hoje!",
        "Descubra os verbos que sustentam a situação!",
        "Veja como os verbos funcionam no contexto!",
    ],
    "These are today's verbs!": [
        "Here are the verbs for today!",
        "Let’s put today’s verbs to work!",
        "Which verbs drive this scene?",
        "Now let’s focus on the actions!",
        "These verbs carry the situation!",
        "Time to practise today’s verbs!",
        "See how the verbs work in context!",
        "Let’s bring the key verbs to life!",
    ],
    "Estes são os verbos de hoje!": [
        "Aqui estão os verbos da aula!",
        "Vamos colocar os verbos de hoje em ação!",
        "Quais verbos movem esta cena?",
        "Agora, atenção às ações!",
        "Estes verbos sustentam a situação!",
        "Hora de praticar os verbos da missão!",
        "Veja os verbos funcionando em contexto!",
        "Vamos dar vida aos verbos principais!",
    ],
    "Missão dos verbos": [
        "Desafio dos verbos",
        "Verbos em movimento",
        "Rota dos verbos",
        "Laboratório de ações",
        "Trilha dos verbos",
        "Ações em foco",
        "Jogo dos verbos",
        "Oficina de ações",
    ],
    "Missão dos verbos: 7 passos. Eu ajudo você!": [
        "Sete passos para praticar os verbos — eu acompanho você!",
        "Vamos cumprir sete desafios de verbos juntos!",
        "A trilha tem sete passos; conte comigo!",
        "Pratique os quatro verbos em sete movimentos!",
        "Sete escolhas colocam os verbos em ação!",
        "Siga a rota dos verbos em sete passos!",
        "Uma missão curta para dominar as ações de hoje!",
        "Complete os sete passos e use os verbos na cena!",
    ],
    "Verb mission! I will help you.": [
        "Verb challenge! I’ll guide you.",
        "Seven verb steps — I’m with you.",
        "Let’s put the four verbs into action.",
        "Follow the verb trail with me.",
        "A short mission for today’s actions.",
        "Complete the verb route one step at a time.",
        "Use the verbs in the situation.",
        "Let’s practise the verbs through the scene.",
    ],
    "Missão dos verbos! Eu ajudo você.": [
        "Desafio dos verbos! Eu acompanho você.",
        "Sete passos de verbos — vamos juntos.",
        "Vamos colocar os quatro verbos em ação.",
        "Siga comigo a trilha dos verbos.",
        "Uma missão curta para as ações de hoje.",
        "Complete a rota dos verbos passo a passo.",
        "Use os verbos dentro da situação.",
        "Vamos praticar os verbos pela cena.",
    ],
    "Expressões e gírias": [
        "Expressões em contexto",
        "Jeitos naturais de dizer",
        "Frases que soam naturais",
        "Linguagem da situação",
        "Expressões para levar",
        "Como as pessoas dizem",
        "Falas úteis da cena",
        "Expressões em ação",
    ],
    "Toque para ouvir cada expressão.": [
        "Toque em cada expressão para escutar.",
        "Ouça como cada expressão soa.",
        "Escute as frases e perceba o uso.",
        "Dê play em cada expressão.",
        "Confira o áudio de cada fala útil.",
        "Ouça uma expressão por vez.",
        "Compare as expressões no áudio.",
        "Toque, escute e leve a frase para a conversa.",
    ],
    "This is how people really talk!": [
        "This is how the phrase sounds in real life!",
        "Hear the expression in a natural exchange!",
        "These are phrases people actually use!",
        "Listen for the everyday wording!",
        "The scene shows the expression in action!",
        "Here’s the natural way to say it!",
        "Notice how the phrase works in conversation!",
        "Take these real-life expressions with you!",
    ],
    "É assim que as pessoas falam de verdade!": [
        "É assim que a frase aparece numa conversa real!",
        "Ouça a expressão dentro de uma troca natural!",
        "Estas são frases que as pessoas realmente usam!",
        "Repare no jeito cotidiano de dizer isso!",
        "A cena mostra a expressão funcionando!",
        "Aqui está uma forma natural de falar!",
        "Observe como a frase entra na conversa!",
        "Leve estas expressões para situações reais!",
    ],
    "Na conversa de verdade": [
        "No diálogo do dia a dia",
        "Quando a conversa acontece",
        "Expressões dentro da cena",
        "A fala em contexto",
        "Na situação real",
        "Conversa em movimento",
        "Veja a expressão funcionando",
        "Do vocabulário para a conversa",
    ],
    "Veja as expressões em uso. Elas estão destacadas.": [
        "Observe as expressões dentro do diálogo; elas estão marcadas.",
        "As expressões aparecem destacadas na conversa.",
        "Repare onde cada expressão entra na cena.",
        "A conversa ilumina as frases que você acabou de estudar.",
        "Veja as expressões funcionando em contexto.",
        "As falas destacadas mostram o uso natural.",
        "Siga as marcações e encontre as expressões na cena.",
        "O diálogo dá vida às expressões desta aula.",
    ],
    "Complete as falas": [
        "Termine as falas",
        "Preencha a conversa",
        "Complete o que foi dito",
        "Escolha a peça que falta",
        "Reconstrua as frases",
        "Feche as lacunas da cena",
        "Monte as falas",
        "Recupere as palavras que faltam",
    ],
    "Complete the sentences!": [
        "Finish the lines!",
        "Fill in the conversation!",
        "Choose the missing piece!",
        "Rebuild the sentences!",
        "Complete the scene!",
        "Close the gaps in the dialogue!",
        "Put the lines back together!",
        "Recover the missing words!",
    ],
    "Complete as frases!": [
        "Termine as falas!",
        "Preencha a conversa!",
        "Escolha a peça que falta!",
        "Reconstrua as frases!",
        "Complete a cena!",
        "Feche as lacunas do diálogo!",
        "Monte as falas novamente!",
        "Recupere as palavras que faltam!",
    ],
    "Careful! Only one is right.": [
        "Look closely — one option fits.",
        "Check the details; only one works.",
        "Read the whole sentence before choosing.",
        "One answer matches the pattern.",
        "Watch the grammar — one choice is right.",
        "Compare the options carefully.",
        "Which sentence keeps the meaning?",
        "Choose the line that sounds natural.",
    ],
    "Cuidado! Só uma está certa.": [
        "Olhe com atenção: uma opção se encaixa.",
        "Confira os detalhes; só uma funciona.",
        "Leia a frase inteira antes de escolher.",
        "Uma resposta combina com o padrão.",
        "Atenção à gramática: uma escolha está certa.",
        "Compare as alternativas com calma.",
        "Qual frase mantém o sentido?",
        "Escolha a opção que soa natural.",
    ],
    "Let's train our ears!": [
        "Let’s tune in to the sounds!",
        "Time for an ear workout!",
        "Listen for the small differences!",
        "Let’s sharpen your listening!",
        "Train your ear with the scene!",
        "Hear the contrast clearly!",
        "Now focus on the sound!",
        "Let’s make the pronunciation visible to your ear!",
    ],
    "Vamos treinar o ouvido!": [
        "Vamos afinar a escuta!",
        "Hora de exercitar o ouvido!",
        "Ouça as pequenas diferenças!",
        "Vamos deixar a escuta mais precisa!",
        "Treine o ouvido com a cena!",
        "Perceba o contraste no som!",
        "Agora, atenção à pronúncia!",
        "Vamos tornar o som mais claro para você!",
    ],
    "Caça-sons": [
        "Busca do som",
        "Rastreador de pronúncia",
        "Detetive dos sons",
        "Ouvido em ação",
        "Pistas de pronúncia",
        "Desafio de escuta",
        "Mapa dos sons",
        "Caçada sonora",
    ],
    "Listen and hunt the sound!": [
        "Listen and track the sound!",
        "Find the sound you hear!",
        "Be a sound detective!",
        "Follow the pronunciation clue!",
        "Put your ear to work!",
        "Spot the sound in the word!",
        "Track the contrast!",
        "Catch the sound in the scene!",
    ],
    "Ouça e cace o som certo!": [
        "Siga a pista sonora!",
        "Encontre o som que você ouviu!",
        "Seja detetive da pronúncia!",
        "Acompanhe a pista de som!",
        "Coloque o ouvido para trabalhar!",
        "Ache o som dentro da palavra!",
        "Rastreie o contraste!",
        "Capture o som na cena!",
    ],
    "Sua vez de falar": [
        "Agora é com você",
        "Hora de produzir",
        "Fale a sua versão",
        "Pratique em voz alta",
        "Sua voz entra na cena",
        "Produção guiada",
        "Diga você",
        "Leve a frase para a sua voz",
    ],
    "Ouça cada frase e repita em voz alta.": [
        "Escute cada frase e repita com ritmo.",
        "Ouça, pause e diga a frase em voz alta.",
        "Repita as frases acompanhando a pronúncia.",
        "Deixe o áudio servir de modelo para a sua voz.",
        "Fale cada linha depois de ouvi-la.",
        "Treine a frase inteira, não só a palavra.",
        "Escute e produza a frase no seu ritmo.",
        "Agora, diga cada exemplo por conta própria.",
    ],
    "Missão: sua vez!": [
        "Missão de produção",
        "Desafio: fale você",
        "Sua resposta entra em cena",
        "Hora da missão aberta",
        "Agora, use o que aprendeu",
        "Desafio de fala",
        "Produza a sua resposta",
        "Leve a língua para a ação",
    ],
    "Cena da obra": [
        "Recrie a situação",
        "Fale pela personagem",
        "Entre no momento da obra",
        "Responda dentro da cena",
        "Aplique o foco à narrativa",
        "Use a referência como cenário",
        "Dê voz à situação",
        "Interprete a missão",
    ],
    "Fale como os personagens.": [
        "Responda como alguém da cena.",
        "Use a voz de uma personagem.",
        "Entre no papel e responda.",
        "Diga a fala como ela aconteceria.",
        "Interprete a situação em inglês.",
        "Assuma um ponto de vista e fale.",
        "Continue a conversa pela personagem.",
        "Faça a cena avançar com a sua resposta.",
    ],
    "Escolha uma missão e mostre o que você aprendeu!": [
        "Escolha uma missão e coloque o inglês em ação!",
        "Selecione um desafio e mostre sua produção!",
        "Agora você decide como continuar a situação!",
        "Escolha um caminho e use o que aprendeu!",
        "Mostre sua resposta em uma missão real!",
        "Leve o foco da aula para uma nova situação!",
        "Escolha um desafio e faça a conversa avançar!",
        "Sua vez de transformar o conteúdo em fala!",
    ],
    "Pick a mission! Which one do you want?": [
        "Choose a mission — which path will you take?",
        "Pick a challenge and keep the scene moving!",
        "Which mission fits your next step?",
        "Choose your task and use the language!",
        "Select a challenge for your response!",
        "Where will you take the conversation?",
        "Pick one mission and make it yours!",
        "Choose a path and keep speaking!",
    ],
    "Escolha uma missão! Qual você quer?": [
        "Escolha um desafio — qual caminho você segue?",
        "Pegue uma missão e faça a cena avançar!",
        "Qual missão combina com seu próximo passo?",
        "Escolha uma tarefa e use a língua!",
        "Selecione um desafio para responder!",
        "Para onde você leva a conversa?",
        "Escolha uma missão e deixe sua marca!",
        "Pegue um caminho e continue falando!",
    ],
    "Para levar": [
        "Leve com você",
        "O que fica da aula",
        "Síntese da missão",
        "Fechamento em movimento",
        "Pistas para a próxima situação",
        "Seu kit de saída",
        "Antes de seguir",
        "O que você leva daqui",
    ],
    "Qual é a palavra?": [
        "Qual palavra combina?",
        "Que palavra você vê?",
        "Escolha a palavra certa",
        "Qual é o item da cena?",
        "Que palavra aparece aqui?",
        "Identifique a palavra",
        "Qual opção nomeia a figura?",
        "Encontre o vocabulário",
    ],
    "Qual palavra você ouviu?": [
        "Que palavra chegou ao seu ouvido?",
        "Qual palavra foi dita?",
        "O que você escutou?",
        "Identifique o som",
        "Qual opção corresponde ao áudio?",
        "Que palavra apareceu na escuta?",
        "Reconheça a palavra falada",
        "Qual som você captou?",
    ],
    "Ouça e toque na palavra.": [
        "Escute e selecione a palavra.",
        "Ouça o áudio e toque na opção.",
        "Reconheça o som e escolha.",
        "Qual palavra você identifica? Toque nela.",
        "Siga a pronúncia e marque a palavra.",
        "Escute com cuidado e selecione.",
        "Encontre no áudio a palavra certa.",
        "Toque na palavra que você ouviu.",
    ],
    "Ouça e toque na figura.": [
        "Escute e selecione a figura.",
        "Qual imagem corresponde ao áudio?",
        "Ligue a pronúncia à figura.",
        "Ouça a pista e toque na imagem.",
        "Encontre o objeto que foi dito.",
        "Reconheça o som e escolha a figura.",
        "Qual figura combina com a palavra?",
        "Toque no objeto que você ouviu.",
    ],
    "Escreva a sua resposta aqui…": [
        "Digite sua resposta aqui…",
        "Escreva como você responderia…",
        "Registre sua frase aqui…",
        "Agora, produza sua resposta…",
        "Coloque sua versão no campo…",
        "Diga por escrito o que você faria…",
        "Monte sua resposta aqui…",
        "Experimente sua própria frase…",
    ],
    "Qual está certa?": [
        "Qual frase mantém o sentido?",
        "Qual opção está bem formada?",
        "Que frase soa natural?",
        "Qual construção você escolheria?",
        "Qual alternativa está correta?",
        "Que versão funciona nesta situação?",
        "Qual frase segue o padrão?",
        "Qual resposta combina com a cena?",
    ],
    "Qual frase está certa?": [
        "Qual frase mantém o sentido?",
        "Qual opção está bem formada?",
        "Que frase soa natural?",
        "Qual construção você escolheria?",
        "Qual alternativa está correta?",
        "Que versão funciona nesta situação?",
        "Qual frase segue o padrão?",
        "Qual resposta combina com a cena?",
    ],
    "Veja o padrão na cena da obra.": [
        "Observe o padrão dentro da cena.",
        "A cena mostra a estrutura em uso.",
        "Encontre o padrão nas falas da obra.",
        "Veja como a estrutura aparece no contexto.",
        "Use a cena para reconhecer o padrão.",
        "A referência cultural dá forma à estrutura.",
        "Repare na construção enquanto a cena avança.",
        "Descubra o padrão no momento da narrativa.",
    ],
}


def num_o(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def in_scope(e):
    o = num_o(e.get("o"))
    return o is not None and o >= 6


def walk_replace(value, seed):
    """Substitui textos de interface, alternando dentro do mesmo episódio."""
    counter = Counter()

    def rec(x):
        if isinstance(x, str) and x in VARIANTS:
            pool = VARIANTS[x]
            pos = (seed + counter[x]) % len(pool)
            counter[x] += 1
            return pool[pos]
        if isinstance(x, list):
            return [rec(y) for y in x]
        if isinstance(x, dict):
            return {k: rec(v) for k, v in x.items()}
        return x

    return rec(value)


def active_vocab(e):
    for fr in e.get("fr", []):
        # O título do quadro varia de episódio para episódio; a grade de
        # vocabulário é identificada pelas figuras e pelo campo ``say``.
        if fr.get("k") == "pgsheet" and (
            fr.get("layout") == "grid"
            or any(isinstance(item, dict) and "fig" in item and "say" in item for item in fr.get("items", []))
        ):
            words = [str(item.get("say", "")).strip() for item in fr.get("items", [])]
            return [w for w in words if w]
    return [str(item[0]).strip() for item in e.get("v", []) if isinstance(item, list) and item]


def focus_mismatch(e):
    s = str(e.get("s", ""))
    m = re.search(r"\(([^)]*)\)", s)
    if not m:
        return []
    focus = [x.strip().lower() for x in re.split(r",| e ", m.group(1)) if x.strip()]
    words = [x.lower() for x in active_vocab(e)]
    return [x for x in focus if not any(x in w or w in x for w in words)]


def align_summary_with_vocab(e):
    """Em desvios claros, deixa o resumo apontar para o vocabulário realmente praticado."""
    if len(focus_mismatch(e)) < 3:
        return False
    s = str(e.get("s", ""))
    m = re.search(r"\(([^)]*)\)", s)
    if not m:
        return False
    words = active_vocab(e)
    if len(words) < 3:
        return False
    replacement = "(" + ", ".join(words[:6]) + ")"
    e["s"] = s[: m.start()] + replacement + s[m.end() :]
    return True


def add_bridge(e, seed):
    d = str(e.get("a", {}).get("d", ""))
    p = str(e.get("p", "")).strip().rstrip(".")
    if not p:
        return False
    # O foco vira uma citação curta dentro da frase de ponte. Remover apenas
    # a abertura “Hoje você aprende” evita construções como “transforma em
    # hoje você aprende…”, que apareciam em alguns registros antigos.
    p = re.sub(r"^Hoje você aprende\s+", "", p, flags=re.I)
    p = re.sub(r"^a\s+", "", p, flags=re.I)
    p = re.sub(r"^Você vai treinar\s+", "treinar ", p, flags=re.I)
    p = p[:1].lower() + p[1:] if p else p
    phrases = [
        "A obra conversa com o foco da aula: “{focus}”.",
        "A cena transforma a referência em prática linguística: “{focus}”.",
        "O elo com a língua fica claro na atividade “{focus}”.",
        "A referência abre a situação para praticar “{focus}”.",
        "A obra dá contexto à missão linguística — “{focus}”.",
        "O estudante usa a referência para trabalhar “{focus}”.",
        "A cena cultural serve de ponte para o foco “{focus}”.",
        "A aula retorna à obra para explorar “{focus}”.",
    ]
    sentence = phrases[seed % len(phrases)].format(focus=p)
    markers = (
        "A obra conversa com", "O elo com", "A obra não fica", "A referência funciona",
        "A cena cultural", "O contexto da obra", "A aula parte", "A relação entre obra",
        "A cena transforma", "A referência abre", "A obra dá", "O estudante usa",
        "A aula retorna",
    )
    parts = d.split(". ")
    if parts and parts[-1].startswith(markers):
        parts[-1] = sentence.rstrip(".")
        e.setdefault("a", {})["d"] = ". ".join(parts) + "."
        return True
    # Descrições editoriais que não terminam com uma ponte já estão boas.
    if re.search(r"\b(a aula|a referência|a cena|a obra|a pintura|o filme|o livro|a série|a canção|o poema|o contexto da obra|a relação entre obra e foco|a relação com|o elo com|the scene|the reference)\b", d, re.I):
        return False
    if d and not d.endswith((".", "!", "?")):
        d += "."
    e.setdefault("a", {})["d"] = (d + " " + sentence).strip()
    return True


def fix_scene_lines(e):
    changed = False
    for fr in e.get("fr", []):
        if fr.get("k") != "pgscene":
            continue
        fixed = []
        for line in fr.get("lines", []):
            # Corrige o formato acidental [speaker, speaker, en, pt].
            if isinstance(line, list) and len(line) >= 4 and line[0] == line[1]:
                line = [line[0], line[2], line[3], *line[4:]]
                changed = True
            fixed.append(line)
        fr["lines"] = fixed
    # Três cenas A1 estavam com sete falas na segunda situação. A fala nova
    # fecha o intercâmbio sem alterar o foco do episódio.
    additions = {
        70020: ["Mr. Bumble", "Good morning, Oliver. Snack is ready.", "Bom dia, Oliver. O lanche está pronto."],
        910011: ["Phin", "Thanks, Mom. I’ll do my best.", "Obrigado, mãe. Vou fazer o meu melhor."],
        30013: ["Tess", "Great. Let’s begin on time.", "Ótimo. Vamos começar na hora."],
    }
    if e.get("n") in additions:
        scenes = [fr for fr in e.get("fr", []) if fr.get("k") == "pgscene"]
        for fr in scenes:
            if len(fr.get("lines", [])) == 7:
                fr["lines"].append(additions[e["n"]])
                changed = True
                break
    return changed


def unique_titles(records):
    groups = defaultdict(list)
    for e in records:
        groups[str(e.get("t", ""))].append(e)
    changed = 0
    for title, group in groups.items():
        if len(group) < 2:
            continue
        for e in group[1:]:
            work = str(e.get("a", {}).get("w", "")).strip()
            if work and work not in title:
                e["t"] = f"{title} · {work}"
            else:
                e["t"] = f"{title} · episódio {int(num_o(e.get('o')) or 0)}"
            changed += 1
    return changed


def process_file(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    records = [e for e in data if in_scope(e)]
    stats = Counter()
    stats["episodes"] = len(records)
    stats["titles"] = unique_titles(records)
    for e in records:
        seed = int(abs(float(e.get("n", 0))))
        if add_bridge(e, seed):
            stats["bridges"] += 1
        if align_summary_with_vocab(e):
            stats["focus_vocab"] += 1
        if fix_scene_lines(e):
            stats["scenes"] += 1
        # Alguns registros já traziam a ponte editorial e receberam a mesma
        # frase uma segunda vez em uma geração anterior. Remova apenas
        # sentenças adjacentes literalmente duplicadas.
        d = str(e.get("a", {}).get("d", ""))
        parts = d.split(". ")
        if len(parts) >= 2 and parts[-1].rstrip(".") == parts[-2].rstrip("."):
            cleaned = ". ".join(parts[:-1]).rstrip()
            e.setdefault("a", {})["d"] = cleaned if cleaned.endswith((".", "!", "?")) else cleaned + "."
            stats["dedup_descriptions"] += 1
        elif d and not d.endswith((".", "!", "?")):
            e.setdefault("a", {})["d"] = d + "."
            stats["description_punctuation"] += 1
        before = json.dumps(e, ensure_ascii=False, separators=(",", ":"))
        e2 = walk_replace(e, seed)
        after = json.dumps(e2, ensure_ascii=False, separators=(",", ":"))
        if before != after:
            stats["boilerplate_episodes"] += 1
        e.clear()
        e.update(e2)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    os.replace(tmp, path)
    return stats


def main():
    total = Counter()
    for course in COURSES:
        for path_str in sorted(glob.glob(str(ROOT / "data" / f"{course}_*.json"))):
            stats = process_file(Path(path_str))
            total.update(stats)
            print(Path(path_str).name, dict(stats))
    print("TOTAL", dict(total))


if __name__ == "__main__":
    main()
