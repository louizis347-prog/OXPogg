# Auditoria das aulas Quest A1 (1–200)

Gerada ao fechar a aula 200. Dados medidos nos arquivos `professor/src/supp5` e `professor/data/v4`.

## Números
- 200 aulas, todas com 45–47 quadros (média 47).
- 1156 palavras de vocabulário ensinadas (6 por aula, mais algumas extras nas aulas 1–50).
- 303 verbos diferentes; nenhum verbo aparece em mais de 8 aulas (wear, take, show, send, ride, pick, open e leave estão no teto).
- Episódios do curso regular (R): nenhum repetido entre as aulas 51–200.
- Testes: aulas 1–200 sem rolagem e sem erro de JavaScript no computador; no celular testado por amostra.

## Problemas encontrados
1. **Vocabulário repetido nas aulas 1–50** (34 palavras, feitas antes do registro): tomato (2, 24, 41), pound, dollar, name, neighbor, building, phone, speak, birthday, cook, driver, minute, pizza, park, fish, milk, toast, breakfast, ticket, hot, invite, drink, snack, sandwich, cheese, bread, water, rice, beans, apple, card, cash, change. Nas aulas 51–200 não há repetição.
2. **Vocabulário acima do A1** (julgamento manual; os agentes tinham limite de 1–2 palavras de A2 por aula, mas algumas aulas passam disso):
   - 52 conductor · 60 pedestrian · 61 landmark, brochure, souvenir · 64 lease, deposit · 65 tenant, basement
   - 66 mattress, cushion · 67 cabinet, kettle, toaster · 68 hamper, hanger · 69 frosting, apron · 70 mop, dustpan, sponge
   - 71 router · 72 compost, cardboard · 76 zipper, collar · 77 policy, gadget · 79 thermometer, prescription · 80 clippers, trim
   - 82 vase · 84 treadmill · 86 trailer · 87 cooler · 89 firewood · 90 exhibit · 92 pitcher, batter, inning · 93 shrimp
   - 94 username, follower · 97 gravy, stuffing · 98 sparkler · 99 ornament · 100 resolution, confetti · 101 touchdown, halftime
   - 106 paperclip · 108 whiteboard, projector · 110 attachment, draft · 111 extension, voicemail · 113 tuition, semester
   - 119 resume · 122 deadline, happy hour · 123 stomachache · 127 broccoli, protein · 129 floss, gums · 130 squint
   - 132 teller · 133 keypad · 135 permit · 136 renewal · 137 wrinkle, tailor · 138 heel, sole, thread, hammer, polish
   - 139 wax, hose, foam · 140 turnstile · 141 gust · 142 detour, commute, ramp · 144 skeleton, fossil · 146 okra, trumpet
   - 147 usher, intermission, applause, spotlight · 148 geyser, bison · 149 saddle, barrel · 150 admissions, scholarship, freshman, dean
   - 154 bookcase, mover · 161 crib, stroller · 176 doorstep, crispy · 179 locksmith, doorknob · 180 boiler, faucet, knob
   - 182 bulb · 185 leash · 191 perfume · 193 screwdriver, toolbox · 195 gutter, nachos · 196 headset · 197 windmill · 200 hoodie
   - Proposta: manter como "palavra de sobrevivência" as que o aluno precisa reconhecer na situação (prescription, voicemail, permit, ramp) e trocar as demais por palavras A1 da mesma cena.
3. **Papéis no diálogo base:** em muitas aulas o diálogo original do Neighbors coloca o aluno como atendente. O `dlg` foi mantido; o `convo`, o `role` e o `mini` colocam o aluno como cliente. Em alguns `mini` o nome do atendente é o do personagem que no `dlg` era o cliente (exigência do validador). Fica levemente inconsistente.
4. **Episódios regulares fracos:** algumas aulas ficaram com o episódio R pouco ligado ao tema (por exemplo 130, 140, 153, 154, 185). A ligação é leve na leitura.
5. **Fatos culturais:** escritos com cautela, mas sem revisão humana. Pontos a conferir: regras de aluguel de carro e de devolução, imposto não incluso no preço, distâncias de segurança em Yellowstone, objetivo de 8 segundos na montaria, tarifas e cartões de metrô, rodízio de coleta de lixo.
6. **Traduções PT-BR:** escritas pelos agentes, sem revisão por falante nativo. Alguns trocas `{a|b}` ficaram com tradução quase igual nas duas opções, e algumas formas soam forçadas (ex.: "meinhas pequenas" na aula 161).
7. **Laboratório de sons:** em algumas aulas há pares pouco naturais (ex.: "Key pit" na 197).
8. **Cenários:** as cenas disponíveis são as do dicionário `RS`; aulas de escritório, aeroporto, casa de festa e academia usam cenas aproximadas.

## Próximos passos sugeridos
1. Trocar o vocabulário acima do A1 (item 2), aula por aula.
2. Revisar as traduções e os fatos culturais (itens 5 e 6).
3. Escrever as aulas 201–300 para chegar às 300 aulas de A1.
