# Estudo 01 — Análise de Dados de Varejo

**Tipo:** análise exploratória / analytics / dados tabulares  
**Repositórios:** [projeto de varejo no portfólio](projects/01-analise-varejo-python-sql/README.md) · [repositório com notebook e pipeline](https://github.com/RodriguesProject/Thiago_Rodrigues_Analise_Varejo_T8)

## Objetivo de negócio

Investigar uma base transacional de varejo e produzir descrições confiáveis de volume, categorias e comportamento dos registros. Antes de falar em insights, é necessário compreender a granularidade: uma linha pode representar um item de uma compra, e não uma compra ou um cliente.

## Arquivos a estudar

### A. Repositório principal do portfólio: `projects/01-analise-varejo-python-sql/src/analise_vendas.py`

| Trecho / bloco | Explicação que você deve dominar |
|---|---|
| Imports (`Path`, `pandas`, `matplotlib.pyplot`) | Bibliotecas e responsabilidades: caminhos, manipulação tabular e gráficos |
| `ROOT`, `DATA`, `OUT` | Construção de caminhos relativos ao arquivo, evitando depender do diretório atual |
| `main()` | Ponto de entrada e sequência completa da análise |
| `DATA.exists()` | Pré-condição: verificar se o arquivo existe antes de ler |
| `pd.read_csv(..., parse_dates=...)` | Leitura do CSV e conversão de data; entender delimitador, encoding e tipos |
| `required` e `missing` | Contrato mínimo da base e validação de esquema |
| `drop_duplicates(subset=["pedido_id"])` | Remove duplicidade por identificador de pedido; discutir risco se um pedido puder ter várias linhas legítimas |
| `pd.to_numeric(..., errors="coerce")` | Converte valores e transforma entradas inválidas em nulos |
| `dropna` e filtros | Critérios de exclusão; explicar quais registros deixam de participar dos resultados |
| Receita, custo e margem | Receita = quantidade × preço unitário; custo = quantidade × custo unitário; margem bruta = receita − custo |
| Coluna `mes` | Agrupamento temporal por mês |
| DataFrame `resumo` | Construção de indicadores gerais |
| `groupby` por categoria/mês | Agregação de métricas por dimensão |
| `plot`, rótulos e `savefig` | Criação e gravação do gráfico |
| `if __name__ == "__main__"` | Permite importar o módulo sem executar automaticamente a análise |

**Ponto crítico:** o código deduplica por `pedido_id`. Se o modelo de dados permitir vários itens por pedido, essa regra pode apagar itens válidos. Você precisa conferir a granularidade da fonte e justificar a chave correta antes de usar o resultado.

### B. Repositório de estudo: `analise_varejo.py`

| Função / bloco | O que significa |
|---|---|
| `COLUNAS` e `ESTADO_CIVIL` | Esquema esperado e dicionário de códigos |
| `validar_estrutura(df)` | Confere colunas necessárias e impede análise de base vazia |
| `carregar_base(...)` | Confere caminho, lê CSV com separador/encoding configuráveis e valida estrutura |
| `preparar_dados(df)` | Cria cópia, normaliza textos, converte datas e códigos numéricos |
| `gerar_relatorio_qualidade(df)` | Conta nulos e textos vazios por coluna |
| `_distribuicao(serie, nome)` | Calcula frequências e percentual sobre o total de linhas |
| `gerar_tabelas(preparado)` | Filtra segmento A e agrega clientes distintos, compras distintas e registros |
| `analisar_dataframe(df, diretorio_saida)` | Orquestra preparação, qualidade, tabelas, JSON, CSV e gráficos |
| `main()` e argparse | Recebe caminhos e parâmetros pela linha de comando |

### Conceitos que precisam ficar claros

- **Registro/item:** linha da tabela.
- **Compra/pedido:** transação identificada por um ID.
- **Cliente:** entidade identificada por um ID de cliente.
- **Nulos x textos vazios:** são situações diferentes; um campo pode conter string vazia sem ser nulo.
- **Duplicidade exata x duplicidade por chave:** linhas idênticas não são a mesma coisa que repetição de ID.
- **Correção x normalização:** padronizar texto não prova que o valor original era incorreto.
- **Percentual de linhas:** não deve ser apresentado como percentual de clientes quando a tabela está no nível de item.

## Exercícios práticos

1. Acrescente contagem de produtos distintos e explique por que ela pode diferir da quantidade de linhas.
2. Gere uma tabela de vendas por categoria e mês.
3. Crie um indicador de participação percentual por categoria.
4. Acrescente uma verificação para datas que não puderam ser convertidas.
5. No projeto de portfólio, investigue se `pedido_id` é único por linha. Se houver múltiplos itens por pedido, proponha uma chave de linha ou agregue os itens antes de deduplicar.
6. Crie um teste com uma linha inválida e confirme que o pipeline sinaliza o problema sem alterar o DataFrame original.

## Perguntas de entrevista

1. Qual era a pergunta de negócio que orientou sua análise?
2. Qual é a granularidade da base?
3. Por que você usou Pandas?
4. Como lidou com valores ausentes e duplicidades?
5. Como calculou receita, custo e margem?
6. Por que uma soma de linhas não equivale necessariamente a uma contagem de pedidos?
7. Quais conclusões a base permite e quais não permite?
8. Como tornaria a análise reproduzível?

**Resposta-guia:** explique a sequência problema → estrutura dos dados → validação → transformação → agregação → visualização → limitação. Não atribua resultados comerciais reais a uma base sintética.

## Critério de conclusão

Você deve conseguir abrir o script, explicar cada função sem ler esta tabela, modificar um indicador, executar novamente e explicar como validou o resultado.
