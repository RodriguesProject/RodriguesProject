# Projeto 05 — Sistema de Controle de Estoque para Construção Civil

Documentação funcional de uma solução de controle de materiais para operações de construção civil, com foco em edificações de pequeno e médio porte.

O projeto parte de uma experiência profissional prévia do autor com estruturação de controles de estoque em uma empresa do setor. A documentação organiza o problema de negócio, os processos, as regras operacionais e os requisitos de uma solução demonstrativa em Excel.

> **Transparência:** esta publicação documenta o modelo de processo e a especificação funcional. Não contém dados internos da empresa em que a experiência ocorreu, nem reproduz um sistema proprietário. Os saldos, custos, parâmetros e cenários de demonstração devem ser fictícios ou preenchidos com dados autorizados. O arquivo PDF integral do fornecedor e sua base integral de produtos não são redistribuídos neste repositório.

## 1. Problema de negócio

A operação de obras de pequeno e médio porte demanda disponibilidade de materiais em locais diferentes, visibilidade sobre entradas e saídas, reposição tempestiva e acompanhamento de compras. Sem procedimentos padronizados, surgem riscos de divergência de saldo, compras emergenciais, duplicidade de cadastro e falta de rastreabilidade.

## 2. Objetivo

Especificar um controle estruturado que permita:
- catalogar e padronizar os materiais;
- manter separado o estoque do depósito e o estoque móvel do veículo;
- registrar entradas, saídas, transferências e ajustes;
- acompanhar níveis mínimos e necessidades de reposição;
- organizar a solicitação, cotação, aprovação, compra e recebimento;
- registrar inventários físicos e tratar divergências;
- apoiar a gestão por indicadores e relatórios.

## 3. Escopo funcional

| Módulo | Finalidade |
|---|---|
| Catálogo mestre | Código, descrição, família, especificação, embalagem e unidade de controle validada |
| Estoque do depósito | Controle geral dos materiais usados nas obras |
| Estoque veicular | Controle independente e restrito dos itens de atendimento operacional/emergencial |
| Movimentações | Entradas, saídas, transferências e ajustes rastreáveis |
| Reposição | Comparação entre saldo, mínimo e estoque-alvo |
| Checklist de aquisição | Solicitação, cotação, aprovação, pedido e recebimento |
| Fornecedores | Cadastro e seleção padronizada de fornecedores |
| Inventário | Contagem física, conciliação e identificação de divergências |
| Painel gerencial | Indicadores operacionais e visão de reposição |

## 4. Estoque móvel do veículo

O estoque móvel não é uma cópia do depósito. Seu cadastro deve limitar-se aos grupos de consumo operacional definidos para o veículo:
- conexões e acessórios hidráulicos;
- adesivos e colas para PVC;
- fita veda-rosca;
- fitas isolantes;
- fios elétricos flexíveis nas bitolas autorizadas, na faixa definida pela operação (referência de 2,5 a 4,0 mm²).

A inclusão de qualquer item adicional depende de autorização operacional. Tubos longos, materiais de construção geral, acabamentos, ferramentas, gás, disjuntores e itens fora do escopo não devem ser incluídos automaticamente.

## 5. Fornecedores cadastrados

O processo contempla a lista inicial informada para seleção no checklist de compras:
- Casas d'Água
- Balaroti
- Cassol
- Pedra Boa

Contatos, condições comerciais, preços e disponibilidade devem ser cadastrados e confirmados diretamente com cada fornecedor.

## 6. Regras essenciais

1. Cada produto possui identificador interno único; o código de origem do fornecedor é preservado em campo separado.
2. O fator/quantidade por embalagem não deve ser confundido com a unidade de controle do estoque.
3. A unidade de controle deve ser validada antes do primeiro lançamento (por exemplo: unidade, metro, quilograma, saco, caixa ou rolo).
4. Toda movimentação deve identificar data, tipo, SKU, quantidade, responsável e local aplicável.
5. Uma transferência reduz o saldo de origem e aumenta o saldo de destino na mesma quantidade.
6. O veículo só recebe SKUs autorizados para seu catálogo restrito.
7. O estoque mínimo e o estoque-alvo são parâmetros da operação, não dados inferidos do catálogo comercial.
8. Custo unitário e valor do estoque só devem ser calculados após cadastro de preço válido.
9. Ajustes de inventário devem ter justificativa e responsável.
10. Solicitações de compra devem manter trilha desde a necessidade até a conferência do recebimento.

## 7. Indicadores propostos

- SKUs cadastrados e ativos;
- itens abaixo do estoque mínimo por local;
- itens sem saldo;
- quantidade sugerida para reposição;
- valor estimado do estoque, quando houver custos cadastrados;
- movimentações por período e tipo;
- solicitações de compra por etapa;
- pedidos parcialmente recebidos ou em atraso;
- divergências entre saldo sistêmico e contagem física.

## 8. Artefatos desta pasta

| Arquivo | Conteúdo |
|---|---|
| [01-contexto-e-problema.md](01-contexto-e-problema.md) | Contexto, problema e objetivos |
| [02-processo-as-is-to-be.md](02-processo-as-is-to-be.md) | Processo atual e processo proposto |
| [03-requisitos-e-regras.md](03-requisitos-e-regras.md) | Requisitos funcionais, regras e validações |
| [04-checklist-aquisicoes.md](04-checklist-aquisicoes.md) | Fluxo de solicitação e aquisição |
| [05-catalogo-e-governanca.md](05-catalogo-e-governanca.md) | Fonte do catálogo, qualidade e governança |
| [06-fluxo-operacional.mmd](06-fluxo-operacional.mmd) | Fluxo Mermaid do processo |

## 9. Tecnologias e competências relacionadas

**Ferramenta de prototipação:** Microsoft Excel.

**Competências demonstradas:** análise de negócios, levantamento de requisitos, gestão de processos, controles operacionais, gestão de estoque, planejamento de compras, qualidade de dados, indicadores e documentação funcional.

## 10. Limitações e evolução

A solução descrita é adequada como modelo de controle e prototipação. Uma implantação produtiva requer validação de unidades de medida, inventário inicial, política de acesso, rotina de backup, trilha de auditoria, conferência de saldos e definição de responsáveis. Evoluções possíveis incluem Power BI para análise gerencial, automações com Python e persistência em banco de dados SQL.

## Natureza e uso dos dados

A descrição do problema parte de experiência profissional anteriormente relatada pelo autor. Os documentos publicados são uma organização demonstrativa dos processos e requisitos, não um relato de resultados quantitativos auditados. Não são publicados dados empresariais, saldos reais, custos internos ou informações confidenciais.
