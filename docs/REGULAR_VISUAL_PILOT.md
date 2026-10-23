# Piloto visual: primeiros cinco episódios do inglês regular

Escopo: en-a1, IDs 9801, 7009801, 70001, 7070001 e 30001, na ordem da trilha. O marcador `presentation: regular-pilot-v1` ativa a apresentação. Conteúdo, IDs e progresso foram preservados.

Direção visual: paleta azul-petróleo, superfícies claras, bordas discretas e sombras suaves. Compatibilizado com a main 960db7a3: preserva o novo elenco ilustrado das obras e adiciona iluminação suave aos desenhos, contornos nítidos e movimento reduzido. Os perfis estáveis do renderizador anterior continuam disponíveis quando utilizados. O acabamento fica restrito aos cinco episódios marcados.

O balão do Pog passou de uma posição absoluta sobre a aula para uma célula própria no rodapé compartilhado. Em telas estreitas, fica acima dos controles. Textos longos têm rolagem interna e foco por teclado. A área da aula mantém sua própria rolagem.

Validação local: `python tools/check_regular_pilot_browser.py`, com servidor HTTP na porta 8767. Percorre os quadros dos cinco episódios em 1280×900, 800×500, 390×844 e 390×560; verifica limites do rodapé, presença dos retratos e isolamento do sexto episódio. Áudio real não é avaliado por esse teste. Inspeção visual complementar por capturas de tela.

Durante a validação foi corrigido um callback do player de diálogo que tentava atualizar o botão após a cena ser removida.

Este piloto é uma referência visual para futura expansão; não representa revisão editorial dos demais cursos nem publicação em produção.
