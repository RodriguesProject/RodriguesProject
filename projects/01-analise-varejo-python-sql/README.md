# Projeto 01 — Análise de Varejo com Python e SQL

**Objetivo:** demonstrar um fluxo introdutório de análise de dados, desde a leitura e validação de uma base até a geração de indicadores e consultas SQL.

## Perguntas de negócio

1. Qual foi a receita e a margem bruta por mês?
2. Quais categorias geraram maior receita?
3. Como os canais de venda se comparam?
4. Quais regiões concentram as vendas?

## Tecnologias

Python, Pandas, Matplotlib, PostgreSQL e SQL.

## Dados

`data/vendas_sinteticas.csv` contém 600 registros artificiais gerados para este projeto. Não são dados de clientes ou empresas reais. Os valores não representam desempenho de mercado.

## Como executar

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python src/analise_vendas.py
```

Os resultados serão gravados em `outputs/` (resumos CSV e gráfico PNG).

## Estrutura

- `data/`: base sintética de entrada.
- `src/analise_vendas.py`: limpeza, métricas e visualização.
- `sql/schema.sql`: estrutura PostgreSQL.
- `sql/consultas.sql`: exemplos de consultas analíticas.
- `outputs/`: resultados produzidos ao executar o script.

Para carregar no PostgreSQL, execute `sql/schema.sql` e depois use `\copy vendas FROM 'projects/01-analise-varejo-python-sql/data/vendas_sinteticas.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',')` no `psql`, ajustando o caminho conforme seu diretório de trabalho.

## Indicadores calculados

Receita bruta, custo estimado, margem bruta, volume vendido, receita por categoria, canal, região e mês.

## Limitações

É um exercício de portfólio com dados artificiais. Não aborda impostos, devoluções, frete, descontos complexos ou sazonalidade validada. Os indicadores são didáticos e não devem ser usados para decisões comerciais reais.
