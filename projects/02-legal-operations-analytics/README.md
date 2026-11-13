# Projeto 02 — Legal Operations Analytics

**Objetivo:** demonstrar como dados operacionais podem apoiar o acompanhamento de uma carteira fictícia de demandas jurídicas.

## Perguntas de negócio

- Quantas demandas estão em andamento?
- Quantas demandas abertas possuem prazo de referência vencido na data-base?
- Como as demandas se distribuem por área e etapa?
- Qual o valor referencial agregado da carteira aberta?
- Qual é o tempo médio desde a abertura das demandas em andamento?

## Tecnologias

Python, Pandas, Matplotlib, PostgreSQL/SQL e conceitos de qualidade de dados.

## Dados e privacidade

`data/demandas_sinteticas.csv` contém 180 registros artificiais. Identificadores, equipes, áreas, datas e valores são fictícios. Não há dados pessoais, clientes ou processos reais. A data-base da análise é 13/11/2026.

## Execução

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python src/analise_legal_ops.py
```

## Estrutura

- `data/`: base sintética.
- `src/analise_legal_ops.py`: validação e indicadores.
- `sql/`: estrutura e consultas PostgreSQL.
- `mongodb/`: exemplos de documentos JSON para estudo NoSQL.
- `outputs/`: relatórios gerados na execução.

## Indicadores

Demandas em andamento, prazos de referência vencidos, valor referencial aberto, idade média das demandas em andamento e distribuição por área.

## Limitações

O campo `prazo_referencia` é apenas um atributo de dados fictício para exercício analítico. Não representa prazo processual calculado conforme lei, calendário forense, intimação, suspensão ou regra processual. Este projeto não realiza análise jurídica nem recomenda decisões sobre processos reais.
