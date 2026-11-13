# Kit Power BI — Análise de Varejo

Este diretório contém os recursos para montar um relatório interativo no Power BI Desktop a partir da base sintética do projeto.

> **Transparência:** este repositório fornece CSV, medidas DAX, tema e instruções. Um arquivo `.pbix` não está incluído; o relatório final deve ser montado e salvo pelo usuário no Power BI Desktop.

## 1. Arquivo de origem

Importe:

`../data/vendas_sinteticas.csv`

Na etapa de transformação, renomeie a consulta/tabela para **Vendas** e ajuste os tipos:

| Campo | Tipo no Power BI |
|---|---|
| pedido_id | Texto |
| data_pedido | Data |
| regiao | Texto |
| canal | Texto |
| categoria | Texto |
| produto | Texto |
| quantidade | Número inteiro |
| preco_unitario | Número decimal fixo |
| custo_unitario | Número decimal fixo |

Crie as colunas Receita, Custo e Margem no modelo por meio das medidas DAX, não alterando a fonte original.

## 2. Criar a tabela calendário

No Power BI Desktop, selecione Modelagem > Nova tabela e cole a expressão de `CALENDARIO.dax`.

Depois:
1. Marque a tabela Calendario como tabela de datas, usando a coluna `Date`.
2. Crie relacionamento um-para-muitos entre `Calendario[Date]` e `Vendas[data_pedido]`.
3. Deixe o filtro fluir de Calendario para Vendas.

## 3. Medidas DAX

Crie as medidas em `MEDIDAS.dax`. As medidas usam a tabela `Vendas` e a tabela `Calendario`.

As medidas incluem receita bruta, custo, margem bruta, margem percentual, pedidos, unidades, ticket médio, receita do mês anterior e variação mensal.

## 4. Layout recomendado — uma página

**Faixa superior — indicadores**
- Receita Bruta
- Margem Bruta
- Margem %
- Quantidade de Pedidos

**Faixa central**
- Gráfico de linhas: Receita Bruta por mês
- Gráfico de barras: Receita Bruta por categoria

**Faixa inferior**
- Matriz: Região × Canal com Receita Bruta e Margem Bruta
- Tabela: Produto, Unidades, Receita Bruta e Margem %

**Segmentadores**
- Ano/mês
- Categoria
- Canal
- Região

## 5. Tema visual

Em Exibir > Temas > Procurar temas, importe `TEMA_RODRIGUES.json`.

O tema usa azul-marinho, azul e ciano. Ajuste a tipografia e tamanhos conforme o padrão de acessibilidade da equipe.

## 6. Validação antes de publicar

- Compare os totais do Power BI com `outputs/indicadores_gerais.csv`.
- Confira a receita por mês com `outputs/por_mes.csv`.
- Confira categoria com `outputs/por_categoria.csv`.
- Teste os quatro filtros.
- Verifique se a margem é calculada como receita menos custo.
- Identifique moeda como BRL (R$).
- Mantenha visível que a base é sintética.

## 7. Limitações

Os valores são artificiais, não representam uma empresa real e servem exclusivamente para aprendizagem. Não use o painel como demonstração de resultados comerciais reais.
