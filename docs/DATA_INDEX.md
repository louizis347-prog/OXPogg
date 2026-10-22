# Manifesto e contadores (data/manifest.json e data/counts.json)

Não edite esses dois arquivos à mão. Eles são **gerados** a partir dos blocos `data/<curso>_NN.json` que existem no disco.

- Criou, apagou ou renomeou um bloco/curso? Rode `python3 tools/build_data_index.py` e commite o resultado.
- Para só conferir: `python3 tools/build_data_index.py --check`.
- Ao trabalhar numa cópia antiga da `main`, **não** leve os dois arquivos para o PR; rode o script depois de atualizar a branch.
- O fluxo `.github/workflows/data-index.yml` regrava os dois arquivos automaticamente quando algo em `data/` muda e eles ficam fora de sincronia.
- O app ignora blocos ausentes (404) e descarta contadores de cursos sem manifesto, então um manifesto antigo não derruba o site, mas pode inflar totais.
