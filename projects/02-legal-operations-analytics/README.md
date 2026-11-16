# Projeto 02 — Legal Operations Analytics

Estudo demonstrativo de indicadores operacionais aplicados a uma carteira fictícia de demandas jurídicas. O objetivo é mostrar como organização e análise de dados podem apoiar o acompanhamento de operações.

![Demandas em andamento por área — dados sintéticos](outputs/demandas_por_area.png)

## Objetivo

Estruturar uma base fictícia de demandas e explorar indicadores de volume, distribuição, antiguidade e valores referenciais.

## Perguntas analisadas

- Quantas demandas estão em andamento?
- Quantas possuem prazo de referência vencido na data-base?
- Como as demandas se distribuem por área, etapa e responsável?
- Qual é o valor referencial agregado da carteira aberta?
- Qual é a antiguidade média das demandas em andamento?

## Tecnologias e ferramentas

Python, Pandas, Matplotlib, PostgreSQL, SQL e exemplos introdutórios de MongoDB.

## Dados e privacidade

O arquivo `data/demandas_sinteticas.csv` contém 180 registros artificiais. A data-base utilizada é 13/11/2026. Não há dados de clientes, escritórios ou processos reais.

## Execução

Na raiz do repositório:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r projects/02-legal-operations-analytics/requirements.txt
python projects/02-legal-operations-analytics/src/analise_legal_ops.py
```

Em Linux/macOS, ative o ambiente com `source .venv/bin/activate`.

## Estrutura

- `data/`: base sintética.
- `src/`: código de validação e geração de indicadores.
- `sql/`: estrutura e consultas PostgreSQL.
- `mongodb/`: exemplos de documentos e consultas NoSQL.
- `outputs/`: gráfico e resultados da análise.

## Limitações e interpretação

O campo `prazo_referencia` é um atributo fictício utilizado para exercício analítico. Não corresponde a prazo processual calculado conforme legislação, intimações, suspensões ou calendário forense. O projeto não realiza análise jurídica nem recomenda decisões sobre processos reais.
