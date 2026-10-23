# Exemplo completo e válido de uma especificação (episódio 2: Are you…? · Alice).
# Copie a estrutura; mude TODO o conteúdo.
import json
EXAMPLE = json.loads(r'''{
 "B": {
  "title": "Quem está aí? · Are you…?",
  "sub": "Fazer perguntas com Are you…? e responder com Yes, I am / No, I'm not",
  "pattern_label": "Are you…?",
  "why": "Hoje você aprende a perguntar como a Alice: Are you…? e a responder com Yes, I am / No, I'm not.",
  "vocab": [
   [
    "Late",
    "Atrasado",
    "Soa como “LÊIT”."
   ],
   [
    "Hurry",
    "Pressa",
    "Soa como “RÂ-ri”."
   ],
   [
    "New",
    "Novo(a)",
    "Soa como “NIÚ”."
   ],
   [
    "Lost",
    "Perdido(a)",
    "Soa como “LÓST”."
   ],
   [
    "Cat",
    "Gato",
    "Soa como “KÉT”."
   ],
   [
    "Rabbit",
    "Coelho",
    "Soa como “RÉ-bit”."
   ]
  ],
  "balloons": [
   [
    "🐇",
    "rabbit"
   ],
   [
    "⏰",
    "late"
   ],
   [
    "🧭",
    "lost"
   ],
   [
    "🆕",
    "new"
   ],
   [
    "🐱",
    "cat"
   ],
   [
    "🏃",
    "hurry"
   ]
  ],
  "cover_art": {
   "s": "park",
   "items": [
    [
     "🐇",
     104,
     56,
     20,
     "bob"
    ],
    [
     "⏰",
     138,
     44,
     12,
     "bob"
    ],
    [
     "❓",
     84,
     34,
     12,
     "bob"
    ]
   ],
   "seed": "al1"
  },
  "cover_sub": "Are you…? Em 10 minutos você faz perguntas como a Alice",
  "cover_say": "A Alice vê um coelho correndo com um relógio. Ela quer saber: ele está com pressa? Como perguntar?",
  "wrap_recap": [
   [
    "Are you in a hurry?",
    "Você está com pressa?"
   ],
   [
    "Yes, I am.",
    "Sim, estou."
   ],
   [
    "No, I'm not.",
    "Não, não estou."
   ],
   [
    "Are you new here?",
    "Você é nova aqui?"
   ]
  ],
  "teaser": {
   "t": "O Mágico de Oz",
   "d": "Próximo padrão: He's e She's para falar de outras pessoas"
  },
  "cast": {
   "Alice": [
    "👧",
    "#2b6cb0"
   ],
   "Rabbit": [
    "🐰",
    "#C0392B"
   ],
   "Cat": [
    "🐱",
    "#7C4DFF"
   ]
  },
  "lines": [
   [
    "Rabbit",
    "Oh dear! I'm late!",
    "Meu Deus! Estou atrasado!"
   ],
   [
    "Alice",
    "Wait! Are you in a hurry?",
    "Espere! Você está com pressa?"
   ],
   [
    "Rabbit",
    "Yes, I am! Are you new here?",
    "Sim, estou! Você é nova aqui?"
   ],
   [
    "Alice",
    "Yes, I am. I'm Alice.",
    "Sim, sou. Eu sou a Alice."
   ],
   [
    "Cat",
    "Hello, Alice! Are you lost?",
    "Olá, Alice! Você está perdida?"
   ],
   [
    "Alice",
    "No, I'm not. Are you a cat?",
    "Não, não estou. Você é um gato?"
   ],
   [
    "Cat",
    "Yes, I am. And we're all mad here!",
    "Sim, sou. E aqui somos todos loucos!"
   ],
   [
    "Alice",
    "Then I'm in the right place!",
    "Então estou no lugar certo!"
   ]
  ],
  "quiz": [
   {
    "q": "Who is late?",
    "pt": "Quem está atrasado?",
    "opts": [
     [
      "🐰",
      "The Rabbit"
     ],
     [
      "🐱",
      "The Cat"
     ],
     [
      "👧",
      "Alice"
     ]
    ],
    "a": 0,
    "line": 0,
    "why": "O Coelho diz: “I’m late!”"
   },
   {
    "q": "Is Alice lost?",
    "pt": "A Alice está perdida?",
    "opts": [
     [
      "❌",
      "No, she isn't"
     ],
     [
      "✅",
      "Yes, she is"
     ],
     [
      "🤷",
      "Maybe"
     ]
    ],
    "a": 0,
    "line": 5,
    "why": "Alice diz: “No, I’m not.”"
   },
   {
    "q": "What is the Cat?",
    "pt": "O que é o Gato?",
    "opts": [
     [
      "🐱",
      "A cat"
     ],
     [
      "🐇",
      "A rabbit"
     ],
     [
      "🎩",
      "A hat"
     ]
    ],
    "a": 0,
    "line": 6,
    "why": "O Gato diz: “Yes, I am.”"
   }
  ],
  "rdg_q": {
   "q": "Qual é a resposta curta certa para “Are you new here?”",
   "o": [
    "Yes, I am.",
    "Yes, I'm.",
    "Yes, I do."
   ],
   "a": 0,
   "why": "Na resposta curta afirmativa, use **Yes, I am.** (nunca “Yes, I’m”)."
  },
  "dictate": [
   [
    "Are you in a hurry?",
    "Você está com pressa?"
   ],
   [
    "Yes, I am.",
    "Sim, estou."
   ],
   [
    "No, I'm not.",
    "Não, não estou."
   ],
   [
    "Are you new here?",
    "Você é nova aqui?"
   ]
  ],
  "produce": {
   "prompt": "A Alice pergunta: *Are you tired? Are you from Brazil?* **Responda com Yes, I am ou No, I'm not, diga algo sobre você com I'm e faça uma pergunta para ela com Are you…?**",
   "ph": "Ex.: Yes, I am. I'm from Brazil. Are you lost?",
   "chips": [
    "Yes, I am.",
    "No, I'm not.",
    "Are you…?"
   ],
   "model": "Yes, I am. I'm a little tired. No, I'm not from Portugal. I'm from Brazil. Are you lost, Alice?",
   "check": [
    "Respondi com Yes, I am ou No, I'm not?",
    "Disse algo sobre mim com I'm?",
    "Fiz uma pergunta com Are you…?"
   ],
   "kw": [
    "\\b(?:yes,?\\s*i am|no,?\\s*i(?:['’]m| am) not)\\b",
    "\\bI(?:['’]m| am)\\s+(?!not\\b)\\w+",
    "\\bare you\\b[^.!?]*\\?"
   ],
   "tips": [
    [
     [
      "Yes, I am.",
      "Sim, estou."
     ],
     [
      "No, I'm not.",
      "Não, não estou."
     ]
    ],
    [
     [
      "I'm from Brazil.",
      "Eu sou do Brasil."
     ],
     [
      "I'm a little tired.",
      "Estou um pouco cansada."
     ]
    ],
    [
     [
      "Are you lost?",
      "Você está perdida?"
     ],
     [
      "Are you new here?",
      "Você é nova aqui?"
     ]
    ]
   ],
   "ok": [
    "Resposta curta certa! ✅",
    "Você falou de si! 🙋",
    "Boa pergunta! ❓"
   ],
   "reply": [
    "Oh, nice! I'm not lost. I'm just late! See you later!",
    "Que bom! Eu não estou perdido. Só atrasado! Até mais!"
   ]
  },
  "rs": {
   "rdg": "pier",
   "pat": "yard",
   "vplay": "hall",
   "sbuild": "lake",
   "build": "home1",
   "order": "cafe3",
   "balloons": "park2",
   "dictate": "living",
   "soundlab": "school",
   "scene": "park",
   "dquiz": "street",
   "scenebuild": "kitchen",
   "produce": "cafe2",
   "review": "station",
   "wrap": "bedroom"
  },
  "sc": "park"
 },
 "X": {
  "n": 7009801,
  "review": true,
  "names": [
   "Alice",
   "Rabbit"
  ],
  "stage": {
   "rs": "park",
   "chars": [
    [
     "alice",
     28,
     0,
     1.0
    ],
    [
     "rabbit",
     56,
     1,
     1.0
    ],
    [
     "cat",
     84,
     1,
     0.95
    ]
   ]
  },
  "obra": {
   "name": "Alice's Adventures in Wonderland",
   "kind": "📖 Livro · 1865",
   "year": "1865",
   "text": "Livro do escritor inglês Lewis Carroll, de 1865. A menina Alice segue um coelho branco, cai em uma toca e chega a um mundo de personagens estranhos. Ela faz muitas perguntas, como você vai fazer hoje.",
   "line": [
    "Who are you?",
    "Quem é você? (pergunta da Lagarta à Alice)"
   ],
   "pa": {
    "t": "library",
    "e": [
     "🐇",
     "📖",
     "⏰"
    ],
    "p": "c",
    "v": 0
   }
  },
  "gancho": [
   "Alice",
   "Wait! Are you in a hurry?",
   "Espere! Você está com pressa?"
  ],
  "hot": [
   {
    "e": "⏰",
    "x": 14,
    "y": 16,
    "en": "late",
    "pt": "atrasado",
    "say": "Oh dear! I'm late!",
    "sayPt": "Meu Deus! Estou atrasado!"
   },
   {
    "e": "🏃",
    "x": 40,
    "y": 14,
    "en": "hurry",
    "pt": "pressa",
    "say": "Are you in a hurry?",
    "sayPt": "Você está com pressa?"
   },
   {
    "e": "🧭",
    "x": 66,
    "y": 14,
    "en": "lost",
    "pt": "perdido",
    "say": "Are you lost?",
    "sayPt": "Você está perdida?"
   },
   {
    "e": "🆕",
    "x": 88,
    "y": 16,
    "en": "new",
    "pt": "novo(a)",
    "say": "Are you new here?",
    "sayPt": "Você é nova aqui?"
   },
   {
    "e": "🎩",
    "x": 12,
    "y": 82,
    "en": "hat",
    "pt": "chapéu",
    "say": "Are you a hat? No, I am not!",
    "sayPt": "Você é um chapéu? Não, não sou!"
   }
  ],
  "gap": [
   {
    "q": "___ you in a hurry?",
    "pt": "Você está com pressa?",
    "opts": [
     "Are",
     "Is",
     "Am"
    ],
    "a": 0,
    "why": "Com **you**, o verbo é **are**: **Are** you…?"
   },
   {
    "q": "Yes, I ___.",
    "pt": "Sim, estou.",
    "opts": [
     "am",
     "are",
     "is"
    ],
    "a": 0,
    "why": "A resposta curta repete o verbo: Yes, I **am**."
   },
   {
    "q": "___ you new here?",
    "pt": "Você é nova aqui?",
    "opts": [
     "Do",
     "Are",
     "Is"
    ],
    "a": 1,
    "why": "Para ser/estar, use **Are you…?**"
   },
   {
    "q": "No, I'm ___.",
    "pt": "Não, não estou.",
    "opts": [
     "no",
     "not",
     "don't"
    ],
    "a": 1,
    "why": "Negativa: I'm **not**."
   }
  ],
  "trap": [
   {
    "q": "Qual frase está certa?",
    "opts": [
     "You are tired?",
     "Are you tired?",
     "Do you tired?"
    ],
    "a": 1,
    "why": "Na pergunta o verbo vem primeiro: **Are you** tired?"
   },
   {
    "q": "Qual resposta está certa?",
    "opts": [
     "Yes, I'm.",
     "Yes, I am.",
     "Yes, I are."
    ],
    "a": 1,
    "why": "Na resposta curta afirmativa não se contrai: Yes, I **am**."
   }
  ],
  "sticker": {
   "title": "Alice e o Coelho Branco",
   "sub": "Alice's Adventures in Wonderland · 1865",
   "rs": "park",
   "chars": [
    [
     "alice",
     34,
     0,
     1.0
    ],
    [
     "rabbit",
     68,
     1,
     1.0
    ]
   ]
  },
  "speakers": {
   "Alice": "alice",
   "Rabbit": "rabbit",
   "Cat": "cat"
  },
  "rule": {
   "who": "alice",
   "head": "Are you…?",
   "sub": "Para perguntar, o verbo vem primeiro.",
   "say": [
    "Wait! Are you in a hurry?",
    "Espere! Você está com pressa?"
   ],
   "formula": [
    {
     "from_": [
      [
       "You",
       0
      ],
      [
       "are",
       1
      ],
      [
       "tired.",
       3
      ]
     ],
     "to": [
      [
       "Are",
       1
      ],
      [
       "you",
       0
      ],
      [
       "tired?",
       3
      ]
     ],
     "say": "Are you tired?",
     "note": "Na pergunta, **are** passa para a frente de **you**."
    }
   ],
   "uses": [
    {
     "ico": "❓",
     "tag": "Perguntar",
     "en": "Are you lost?",
     "pt": "Você está perdida?"
    },
    {
     "ico": "✅",
     "tag": "Responder sim",
     "en": "Yes, I am.",
     "pt": "Sim, estou."
    },
    {
     "ico": "❌",
     "tag": "Responder não",
     "en": "No, I'm not.",
     "pt": "Não, não estou."
    }
   ],
   "rules": [
    {
     "tag": "Are you",
     "c": 0,
     "text": "Pergunta com **você**: Are you late? Are you new here?",
     "ex": "Are + you + palavra?"
    },
    {
     "tag": "Yes, I am",
     "c": 2,
     "text": "Resposta curta **sim**: repita o verbo. Não se contrai.",
     "ex": "✗ Yes, I'm  →  ✓ Yes, I am"
    },
    {
     "tag": "No, I'm not",
     "c": 1,
     "text": "Resposta curta **não**: contrai com I'm + not.",
     "ex": "No, I'm not."
    }
   ],
   "tips": [
    "Em português a pergunta só muda a entonação. Em inglês, **troque a ordem**: You are → Are you."
   ]
  },
  "mission_ic": "👋"
 },
 "XT": {
  "exp": [
   {
    "ic": "🤨",
    "en": "Are you kidding?",
    "tag": "Informal",
    "pt": "Você está brincando?",
    "use": "Quando algo parece **bom demais ou absurdo** para ser verdade.",
    "ex": [
     "Are you kidding? That's my hat!",
     "Está brincando? Esse é o meu chapéu!"
    ]
   },
   {
    "ic": "🫶",
    "en": "Are you okay?",
    "tag": "Expressão",
    "pt": "Você está bem?",
    "use": "Pergunta com **cuidado**, quando alguém parece mal ou assustado.",
    "ex": [
     "Are you okay? You look lost.",
     "Você está bem? Parece perdida."
    ]
   },
   {
    "ic": "⏰",
    "en": "I'm running late.",
    "tag": "Expressão",
    "pt": "Estou atrasado.",
    "use": "Jeito natural de avisar que você vai **chegar tarde**.",
    "ex": [
     "Sorry, I'm running late!",
     "Desculpe, estou atrasado!"
    ]
   },
   {
    "ic": "🏃",
    "en": "Hurry up!",
    "tag": "Informal",
    "pt": "Anda logo! / Depressa!",
    "use": "Para **apressar** alguém. Soa um pouco mandão, use com amigos.",
    "ex": [
     "Hurry up, Alice!",
     "Depressa, Alice!"
    ]
   }
  ],
  "exp_scene": {
   "rs": "cafe3",
   "lines": [
    [
     "Rabbit",
     "Oh dear! **I'm running late**!",
     "Meu Deus! Estou atrasado!"
    ],
    [
     "Alice",
     "**Are you okay**?",
     "Você está bem?"
    ],
    [
     "Rabbit",
     "I'm fine! But **hurry up**, Alice!",
     "Estou bem! Mas anda logo, Alice!"
    ],
    [
     "Alice",
     "**Are you kidding**? Where are we going?",
     "Está brincando? Para onde vamos?"
    ],
    [
     "Cat",
     "To the tea party! Are you ready?",
     "Para a festa do chá! Você está pronta?"
    ],
    [
     "Alice",
     "No, I'm not ready!",
     "Não, não estou pronta!"
    ]
   ]
  },
  "lab": {
   "short": "r inicial",
   "title": "Laboratório de sons: o “r” de rabbit",
   "say": "O “r” inglês é bem diferente do nosso! Vamos treinar com o Coelho Branco.",
   "intro": {
    "what": "O **r** inglês, em **rabbit**, **right** e **road**, é um som suave e “redondo”: a língua não encosta em nenhum lugar da boca.",
    "how": "Arredonde os lábios como para assobiar, levante a ponta da língua sem encostar no céu da boca e puxe a língua um pouco para trás. Não vibre a língua.",
    "pt": "Em português o r inicial é forte (rato, rua) e sai da garganta ou vibra. Em inglês ele é macio. Cuidado para não trocar por **l**: **right** (certo) ≠ **light** (luz)."
   },
   "ex": [
    [
     "rabbit",
     "RÉ-bit",
     "coelho",
     "lábios arredondados já no começo"
    ],
    [
     "right",
     "RÁIT",
     "certo",
     "língua solta, sem encostar"
    ],
    [
     "road",
     "RÔUD",
     "estrada",
     "comece com o “r” redondo"
    ]
   ],
   "pairs": [
    [
     "right",
     "light",
     "r: língua solta · l: a ponta da língua toca atrás dos dentes de cima"
    ],
    [
     "road",
     "load",
     "“estrada” × “carga”"
    ],
    [
     "rock",
     "lock",
     "“pedra” × “trancar”"
    ]
   ],
   "tip": "Diga “ru” assobiando: os lábios redondos ajudam o r certo. No “l” a ponta da língua encosta; no “r”, não.",
   "phrase": [
    "Are you in a hurry, rabbit?",
    "Você está com pressa, coelho?"
   ],
   "rounds": [
    {
     "fig": "🎧",
     "say": "right",
     "ask": "Qual palavra você ouviu?",
     "opts": [
      "right",
      "light"
     ],
     "a": 0,
     "why": "Em **right** a língua não encosta. **Light** (luz) começa tocando atrás dos dentes."
    },
    {
     "fig": "🎧",
     "say": "lock",
     "ask": "Qual palavra você ouviu?",
     "opts": [
      "rock",
      "lock"
     ],
     "a": 1,
     "why": "**Lock** (trancar) começa com “l”, a língua toca. **Rock** (pedra) começa com “r” redondo."
    },
    {
     "fig": "🎧",
     "say": "load",
     "ask": "Qual palavra você ouviu?",
     "opts": [
      "road",
      "load"
     ],
     "a": 1,
     "why": "**Load** (carga) começa com “l”. **Road** (estrada) começa com “r”."
    }
   ]
  },
  "hunt": [
   {
    "fig": "🎧",
    "say": "light",
    "ask": "Ouça e toque na palavra.",
    "opts": [
     "right",
     "light"
    ],
    "a": 1,
    "why": "**light** (luz) começa com “l”: a língua encosta."
   },
   {
    "fig": "🎧",
    "say": "rabbit",
    "ask": "Ouça e toque na figura.",
    "opts": [
     [
      "🐇",
      ""
     ],
     [
      "🔒",
      ""
     ],
     [
      "🛣️",
      ""
     ]
    ],
    "a": 0,
    "why": "**rabbit** = coelho.",
    "pic": 1
   },
   {
    "fig": "🎧",
    "say": "road",
    "ask": "Ouça e toque na palavra.",
    "opts": [
     "road",
     "load"
    ],
    "a": 0,
    "why": "**road** (estrada) começa com “r” redondo."
   },
   {
    "fig": "🎧",
    "say": "rock",
    "ask": "Ouça e toque na palavra.",
    "opts": [
     "rock",
     "lock"
    ],
    "a": 0,
    "why": "**rock** (pedra) começa com “r”, sem encostar a língua."
   },
   {
    "fig": "🎧",
    "say": "lock",
    "ask": "Ouça e toque na figura.",
    "opts": [
     [
      "🛣️",
      ""
     ],
     [
      "🔒",
      ""
     ],
     [
      "🐇",
      ""
     ]
    ],
    "a": 1,
    "why": "**lock** = trancar / cadeado.",
    "pic": 1
   }
  ]
 },
 "VB": {
  "title": "Verbos para seguir o Coelho",
  "tip": "Quatro verbos: run, ask, follow e fall.",
  "items": [
   {
    "v": "run",
    "ic": "🏃",
    "pt": "correr",
    "f": [
     [
      "eu",
      "I run to the tea party."
     ],
     [
      "ele/ela",
      "The Rabbit run**s** fast."
     ]
    ],
    "ex": [
     "I run to the tea party.",
     "Eu corro para a festa do chá."
    ],
    "note": "**run** = correr. Com he/she: **runs**."
   },
   {
    "v": "ask",
    "ic": "❓",
    "pt": "perguntar",
    "f": [
     [
      "eu",
      "I ask a question."
     ],
     [
      "ele/ela",
      "Alice ask**s** many questions."
     ]
    ],
    "ex": [
     "I ask a question.",
     "Eu faço uma pergunta."
    ],
    "note": "**ask** = perguntar. Com he/she: **asks**."
   },
   {
    "v": "follow",
    "ic": "👣",
    "pt": "seguir",
    "f": [
     [
      "eu",
      "I follow the White Rabbit."
     ],
     [
      "ele/ela",
      "She follow**s** the rabbit."
     ]
    ],
    "ex": [
     "I follow the White Rabbit.",
     "Eu sigo o Coelho Branco."
    ],
    "note": "**follow** = seguir. Com he/she: **follows**."
   },
   {
    "v": "fall",
    "ic": "⬇️",
    "pt": "cair",
    "f": [
     [
      "eu",
      "I fall down the hole."
     ],
     [
      "ele/ela",
      "Alice fall**s** slowly."
     ]
    ],
    "ex": [
     "I fall down the hole.",
     "Eu caio na toca."
    ],
    "note": "**fall** = cair. Com he/she: **falls**."
   }
  ]
 },
 "MR": {
  "mold": [
   {
    "label": "Perguntar com Are you…?",
    "slots": [
     {
      "cat": "pergunta",
      "opts": [
       [
        "Are you",
        "você está/é"
       ]
      ]
     },
     {
      "cat": "palavra",
      "opts": [
       [
        "tired",
        "cansado(a)"
       ],
       [
        "lost",
        "perdido(a)"
       ],
       [
        "hungry",
        "com fome"
       ],
       [
        "ready",
        "pronto(a)"
       ],
       [
        "late",
        "atrasado(a)"
       ],
       [
        "new here",
        "novo(a) aqui"
       ],
       [
        "a teacher",
        "professor(a)"
       ],
       [
        "from Brazil",
        "do Brasil"
       ]
      ]
     }
    ],
    "end": [
     "?",
     "?"
    ]
   },
   {
    "label": "Responder",
    "slots": [
     {
      "cat": "sim ou não",
      "opts": [
       [
        "Yes,",
        "sim,"
       ],
       [
        "No,",
        "não,"
       ]
      ]
     },
     {
      "cat": "resposta curta",
      "opts": [
       [
        "I am.",
        "eu sou/estou."
       ],
       [
        "I'm not.",
        "eu não sou/estou."
       ]
      ]
     }
    ],
    "end": [
     ".",
     "."
    ]
   },
   {
    "label": "Onde você está?",
    "slots": [
     {
      "cat": "pergunta",
      "opts": [
       [
        "Are you",
        "você está"
       ]
      ]
     },
     {
      "cat": "lugar",
      "opts": [
       [
        "at home",
        "em casa"
       ],
       [
        "at work",
        "no trabalho"
       ],
       [
        "at school",
        "na escola"
       ],
       [
        "at the station",
        "na estação"
       ],
       [
        "in a hurry",
        "com pressa"
       ]
      ]
     }
    ],
    "end": [
     "?",
     "?"
    ]
   }
  ],
  "speak": [
   [
    "Are you tired? No, I'm not.",
    "Você está cansado? Não, não estou."
   ],
   [
    "Are you kidding? Hurry up!",
    "Está brincando? Anda logo!"
   ]
  ],
  "trap": [
   {
    "ask": "“Are you kidding?” quer dizer…",
    "opts": [
     "Você está brincando?",
     "Você está com frio?",
     "Você está perdido?"
    ],
    "a": 0,
    "why": "**Are you kidding?** = está brincando? (surpresa).",
    "say": "Are you kidding?"
   },
   {
    "ask": "Qual frase está certa?",
    "opts": [
     "I am late running.",
     "I'm running late.",
     "I running late."
    ],
    "a": 1,
    "why": "Estou atrasado = **I'm running late.**"
   }
  ],
  "gap": [
   {
    "text": "___ you okay?",
    "pt": "Você está bem?",
    "opts": [
     "Are",
     "Is",
     "Do"
    ],
    "a": 0,
    "why": "Com you: **Are** you…?",
    "say": "Are you okay?"
   },
   {
    "text": "Hurry ___, we're late!",
    "pt": "Anda logo, estamos atrasados!",
    "opts": [
     "up",
     "on",
     "in"
    ],
    "a": 0,
    "why": "**Hurry up!** = anda logo!",
    "say": "Hurry up, we're late!"
   }
  ],
  "expq": [
   {
    "ask": "Seu amigo parece muito triste. O que você pergunta?",
    "opts": [
     "Are you okay?",
     "Are you kidding?",
     "Hurry up!"
    ],
    "a": 0,
    "why": "**Are you okay?** = você está bem?"
   },
   {
    "ask": "Você vai chegar tarde e quer avisar.",
    "opts": [
     "I'm running late.",
     "Hurry up!",
     "Are you okay?"
    ],
    "a": 0,
    "why": "**I'm running late.** = estou atrasado."
   },
   {
    "ask": "Alguém diz algo absurdo e você não acredita.",
    "opts": [
     "Are you kidding?",
     "I'm running late.",
     "Are you okay?"
    ],
    "a": 0,
    "why": "**Are you kidding?** mostra surpresa."
   }
  ],
  "missions": [
   {
    "ic": "👋",
    "name": "Colega novo",
    "desc": "Faça perguntas e responda com respostas curtas.",
    "data": {
     "prompt": "Você encontra uma pessoa nova na escola. **Faça duas perguntas com Are you…? e responda uma delas com Yes, I am ou No, I'm not.**",
     "ph": "Escreva a sua resposta aqui…",
     "chips": [
      "Are you"
     ],
     "model": "Are you new here? Yes, I am. Are you from Brazil?",
     "check": [
      "Fiz uma pergunta com Are you…?",
      "Fiz duas perguntas?",
      "Usei a resposta curta?"
     ],
     "kw": [
      "\\bare you\\b[^.!?]*\\?",
      "(?:\\bare you\\b[^.!?]*\\?[\\s\\S]*){2}",
      "\\b(?:yes,?\\s*i am|no,?\\s*i(?:['’]m| am) not)\\b"
     ],
     "tips": [
      [
       [
        "Are you new here?",
        "Você é novo aqui?"
       ]
      ],
      [
       [
        "Are you from Brazil?",
        "Você é do Brasil?"
       ]
      ],
      [
       [
        "Yes, I am.",
        "Sim, sou."
       ],
       [
        "No, I'm not.",
        "Não, não sou."
       ]
      ]
     ],
     "ok": [
      "Pergunta com Are you! ❓",
      "Duas perguntas! ✌️",
      "Resposta curta certa! ✅"
     ],
     "reply": [
      "Yes, I am! Nice to meet you!",
      "Sim, sou! Prazer em conhecer você!"
     ]
    }
   },
   {
    "ic": "🏃",
    "name": "Atrasado de novo!",
    "desc": "Use as expressões do episódio.",
    "data": {
     "prompt": "Seu amigo está atrasado e parece nervoso. **Pergunte se ele está bem, avise que você também está atrasado e peça para ele andar logo.**",
     "ph": "Escreva a sua resposta aqui…",
     "chips": [
      "Are you okay?"
     ],
     "model": "Are you okay? I'm running late too. Hurry up!",
     "check": [
      "Perguntei se ele está bem?",
      "Avisei que estou atrasado?",
      "Pedi para andar logo?"
     ],
     "kw": [
      "\\bare you (?:okay|ok)\\b",
      "\\brunning late\\b",
      "\\bhurry up\\b"
     ],
     "tips": [
      [
       [
        "Are you okay?",
        "Você está bem?"
       ]
      ],
      [
       [
        "I'm running late.",
        "Estou atrasado."
       ]
      ],
      [
       [
        "Hurry up!",
        "Anda logo!"
       ]
      ]
     ],
     "ok": [
      "Cuidado com o amigo! 🫶",
      "Aviso dado! ⏰",
      "Anda logo! 🏃"
     ],
     "reply": [
      "I'm fine! Let's run!",
      "Estou bem! Vamos correr!"
     ]
    }
   }
  ]
 },
 "CX": [
  {
   "text": "It has long ears and it jumps. In the story, the White ___ has a clock.",
   "pt": "Tem orelhas compridas e pula. Na história, o Coelho Branco tem um relógio.",
   "opts": [
    "rabbit",
    "cat",
    "hurry"
   ],
   "a": 0
  },
  {
   "text": "The class starts at eight. It's eight thirty. I'm ___.",
   "pt": "A aula começa às oito. São oito e meia. Estou atrasado.",
   "opts": [
    "late",
    "new",
    "lost"
   ],
   "a": 0
  },
  {
   "text": "I don't know the way and I have no map. I'm ___.",
   "pt": "Não sei o caminho e não tenho mapa. Estou perdida.",
   "opts": [
    "lost",
    "new",
    "late"
   ],
   "a": 0
  },
  {
   "text": "It's my first day at school. I'm ___ here.",
   "pt": "É meu primeiro dia na escola. Sou nova aqui.",
   "opts": [
    "new",
    "lost",
    "cat"
   ],
   "a": 0
  },
  {
   "text": "It says meow, it has whiskers and it sleeps a lot. It is a ___.",
   "pt": "Faz miau, tem bigodes e dorme muito. É um gato.",
   "opts": [
    "cat",
    "rabbit",
    "hurry"
   ],
   "a": 0
  },
  {
   "text": "The train leaves in two minutes! We are in a ___.",
   "pt": "O trem sai em dois minutos! Estamos com pressa.",
   "opts": [
    "hurry",
    "late",
    "lost"
   ],
   "a": 0
  }
 ]
}
''')
