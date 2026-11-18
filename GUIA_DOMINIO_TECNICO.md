# Guia de Domínio Técnico do Portfólio

Este guia organiza o estudo dos repositórios por tipo de projeto. O objetivo é que você consiga explicar o problema, percorrer o código, alterar regras, testar o comportamento e discutir limitações em entrevistas.

> **Regra de honestidade técnica:** os projetos são estudos de portfólio. Parte usa dados sintéticos. O código publicado deve ser entendido e testado por você antes de ser apresentado como domínio próprio. Não memorize respostas: execute os exercícios.

## Mapa do portfólio por tipo

| Tipo | Repositório / pasta | O que precisa saber defender |
|---|---|---|
| Perfil e curadoria do portfólio | [RodriguesProject](README.md) | Posicionamento, organização, evidências e limites das competências |
| Análise de negócios e operações | [Business Operations Analytics](https://github.com/RodriguesProject/business-operations-analytics) | Perguntas de negócio, indicadores, datas, validação e visualização |
| Análise de dados de varejo | [Projeto varejo Python](projects/01-analise-varejo-python-sql/README.md) e [repositório de estudo](https://github.com/RodriguesProject/Thiago_Rodrigues_Analise_Varejo_T8) | CSV, Pandas, qualidade, agregações, gráficos e SQL |
| Legal Operations Analytics | [Projeto Legal Ops](projects/02-legal-operations-analytics/README.md) | Fluxo de demandas, prazos de referência, métricas e limites de interpretação |
| Business Analysis e processos | [Mapeamento AS-IS/TO-BE](projects/03-business-analysis-processos/README.md) | Problema, stakeholders, processo atual/futuro, requisitos e critérios de aceite |
| Automação administrativa | [Triagem de solicitações](projects/04-automacao-triagem-juridica/README.md) | Regras de validação, filas, erros e revisão humana |
| Preparação e qualidade de dados | [Modularização de limpeza](https://github.com/RodriguesProject/Modulariza-o-em-Python-para-Limpeza-e-Tratamento-de-dados) | Funções, regex, CPF, telefone, e-mail, testes e preservação da origem |

## Como estudar cada arquivo (método linha por linha)

Para cada arquivo-fonte:
1. Leia 10–20 linhas por vez.
2. Explique em voz alta o propósito de cada importação, constante, função, parâmetro e retorno.
3. Reescreva o bloco sem copiar e compare.
4. Mude um comportamento pequeno e preveja a saída antes de executar.
5. Rode o teste correspondente.
6. Registre em suas palavras: entrada, processamento, saída, regra de negócio e limitação.

Não avance se só consegue reconhecer o código visualmente. O critério é conseguir explicar sem consultar a resposta.

## Trilha de aprendizagem sugerida

| Etapa | Conteúdo | Evidência para avançar |
|---|---|---|
| 1 | Python básico: variáveis, tipos, listas, dicionários, condições, laços e funções | Escrever funções pequenas sem copiar |
| 2 | Arquivos, CSV, exceções, módulos e caminhos | Ler arquivo, validar estrutura e tratar erro |
| 3 | Pandas: DataFrame, filtros, tipos, nulos, groupby e agregações | Reproduzir uma tabela de indicadores |
| 4 | Visualização: gráficos, eixos, rótulos e interpretação | Explicar o que o gráfico mostra e não mostra |
| 5 | SQL: SELECT, WHERE, GROUP BY, JOIN e agregações | Responder uma pergunta de negócio com consulta |
| 6 | Testes e GitHub Actions | Criar teste para uma regra nova e observar o CI |
| 7 | Business Analysis | Descrever problema, AS-IS, TO-BE, requisito e aceite |
| 8 | Entrevista técnica | Apresentar um projeto em 2 e 5 minutos e responder perguntas de aprofundamento |

## Rotina de estudo por projeto

- **Sessão A — entendimento:** problema, dados, fluxo e arquitetura.
- **Sessão B — código:** leitura orientada de cada função e execução.
- **Sessão C — alteração:** implementar um exercício sem solução pronta.
- **Sessão D — validação:** escrever ou adaptar testes, executar e interpretar.
- **Sessão E — entrevista:** responder perguntas sem ler o README.

## Critério de domínio

Use a escala:
- **0 — Não conheço:** não sei explicar o termo.
- **1 — Reconheço:** entendo a explicação, mas não consigo aplicar.
- **2 — Aplico com consulta:** consigo executar e adaptar com documentação.
- **3 — Aplico sozinho:** consigo escrever, testar e corrigir.
- **4 — Defendo tecnicamente:** consigo explicar escolhas, alternativas, riscos e limitações.

Só apresente como competência consolidada aquilo que estiver no nível 3 ou 4. Nível 1 ou 2 é conhecimento em desenvolvimento.

## Links oficiais de estudo

- [Tutorial oficial de Python](https://docs.python.org/3/tutorial/)
- [Documentação oficial do Pandas](https://pandas.pydata.org/docs/)
- [Documentação oficial do Matplotlib](https://matplotlib.org/stable/users/index.html)
- [Documentação do PostgreSQL](https://www.postgresql.org/docs/)
- [GitHub Actions](https://docs.github.com/en/actions)

## Registro de domínio

Ao concluir cada módulo, registre:
- O que consigo explicar sem consulta?
- Que alteração implementei?
- Qual teste prova que a alteração funciona?
- Que erro encontrei e como corrigi?
- O que ainda não sei?
