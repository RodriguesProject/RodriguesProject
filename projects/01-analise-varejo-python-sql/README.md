# Projeto 01 — Análise de Varejo com Python e SQL

Estudo demonstrativo de análise de dados aplicado a um cenário de varejo fictício. O projeto percorre etapas introdutórias de leitura, validação, exploração e apresentação de indicadores.

![Receita mensal — base sintética](outputs/receita_mensal.png)

## Objetivo

Explorar uma base de vendas e produzir indicadores que ajudem a responder perguntas básicas de negócio.

## Perguntas analisadas

- Como receita, custo estimado e margem bruta variam por mês?
- Quais categorias apresentam maior receita?
- Como os canais de venda se comparam?
- Como as vendas se distribuem entre regiões?

## Tecnologias e ferramentas

Python, Pandas, Matplotlib, PostgreSQL e SQL.

## Dados utilizados

O arquivo `data/vendas_sinteticas.csv` contém 600 registros artificiais, criados para fins didáticos. Não representa transações, clientes ou empresas reais.

## Execução

Na raiz do repositório:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r projects/01-analise-varejo-python-sql/requirements.txt
python projects/01-analise-varejo-python-sql/src/analise_vendas.py
```

Em Linux/macOS, ative o ambiente com `source .venv/bin/activate`.

## Estrutura

- `data/`: base sintética utilizada na análise.
- `src/analise_vendas.py`: leitura, validação, métricas e visualização.
- `sql/schema.sql`: estrutura relacional para PostgreSQL.
- `sql/consultas.sql`: consultas de análise.
- `outputs/`: gráfico e resultados gerados.
- `powerbi/`: guia e recursos para montagem de painel no Power BI.

## Consultas SQL

O conjunto de consultas inclui funções de janela, como `LAG` e `ROW_NUMBER`, variação mensal e identificação do produto de maior receita por categoria.

## Power BI

O diretório `powerbi/` contém guia de montagem, medidas DAX, tabela calendário e tema visual. Os arquivos são recursos para construção do painel; não há um arquivo `.pbix` pronto nesta entrega.

- [Guia de montagem](powerbi/README.md)
- [Medidas DAX](powerbi/MEDIDAS.dax)
- [Tabela calendário](powerbi/CALENDARIO.dax)
- [Tema visual](powerbi/TEMA_RODRIGUES.json)

## Limitações

Trata-se de um exercício com dados artificiais. A análise não contempla integralmente impostos, devoluções, frete, descontos complexos ou sazonalidade validada. Os indicadores são didáticos e não devem ser interpretados como resultados comerciais reais.
