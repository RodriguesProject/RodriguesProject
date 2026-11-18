# Estudo 03 — Business Operations e Legal Operations Analytics

**Tipo:** análise de negócios aplicada a operações / indicadores / BI  
**Repositórios:** [Business Operations Analytics](https://github.com/RodriguesProject/business-operations-analytics) · [Legal Operations Analytics no portfólio](projects/02-legal-operations-analytics/README.md)

## A pergunta de negócio

Como transformar registros de demandas em informação gerencial sobre volume, andamento, tempo de ciclo e itens que exigem atenção? O foco não é apenas calcular números, mas definir corretamente cada indicador e suas limitações.

## A. Business Operations Analytics — `src/analise_operacional.py`

| Bloco / função | O que precisa explicar |
|---|---|
| Imports | `json`, `Path`, Matplotlib e Pandas: exportação, caminhos, gráficos e tabelas |
| `ROOT`, `DATA_FILE`, `OUTPUT_DIR` | Localização da base e pasta de resultados |
| `DATA_REFERENCIA` | Data fixa usada para reproduzir o cálculo de atraso |
| `carregar_dados()` | Lê CSV e converte datas e valores |
| `validar_dados(df)` | Confere colunas, IDs vazios/duplicados, datas e ordem temporal |
| `calcular_indicadores(df)` | Separa concluídas e abertas, calcula tempo de ciclo, taxa de conclusão e atrasos |
| `por_area` | Agrega volume de demandas por área |
| `fluxo_mensal` | Compara entradas e conclusões por mês |
| `gerar_visualizacoes(...)` | Salva gráficos por área e fluxo mensal |
| `main()` | Orquestra execução e exporta JSON/CSV |

**Atenção conceitual:** o código considera como abertas todas as demandas cujo status não seja exatamente `concluida`. Você deve discutir se os valores de status são controlados e padronizados. A data de referência é fixa, então o indicador não se atualiza sozinho com o calendário.

## B. Legal Operations Analytics — `projects/02-legal-operations-analytics/src/analise_legal_ops.py`

| Bloco / função | O que precisa explicar |
|---|---|
| Caminhos e `AS_OF` | Localização da base e data-base fixa da análise |
| Leitura do CSV | Conversão dos campos de data |
| `required` / `missing` | Contrato de colunas obrigatórias |
| Deduplicação por `demanda_id` | Critério de unicidade; explicar impacto de registros repetidos |
| Conversão de valor | Converte referência monetária para número |
| `em_andamento` | Identifica status igual a “Em andamento” |
| `prazo_referencia_vencido` | Marca prazo anterior à data-base para demandas em andamento |
| `dias_desde_abertura` | Calcula idade do registro na data-base |
| Indicadores | Volume, abertas, vencidas e valores referenciais |
| Agrupamentos | Demandas abertas por área e etapa |
| Gráfico | Distribuição das demandas abertas por área |

**Cuidado:** prazo de referência sintético não equivale a prazo processual, prazo legal, SLA contratual ou aconselhamento jurídico.

## Exercícios práticos

1. Acrescente taxa de demandas abertas por área.
2. Calcule mediana de dias em aberto e compare com a média.
3. Crie uma validação para status fora do catálogo permitido.
4. Altere a data-base por parâmetro de execução, sem editar o código.
5. Explique por que comparar entradas e conclusões no mesmo mês não significa que as mesmas demandas foram concluídas no mês em que entraram.
6. Escreva uma consulta SQL equivalente a uma agregação por área.

## Perguntas de entrevista

1. Como você escolheu os indicadores?
2. Qual a diferença entre volume, produtividade e tempo de ciclo?
3. Por que uma data-base fixa pode ser útil? Qual sua desvantagem?
4. Como impediria que status inconsistentes distorcessem a taxa de conclusão?
5. Como apresentaria esses indicadores a um gestor não técnico?
6. O que você faria se a área tivesse poucas demandas e uma média muito alta?

## Critério de conclusão

Explique um indicador desde sua definição de negócio até sua fórmula, fonte, validação e limitação. Depois altere o código e prove a mudança com uma execução controlada.
