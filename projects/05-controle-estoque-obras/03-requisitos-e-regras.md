# 03 — Requisitos funcionais e regras de negócio

## Requisitos funcionais

| ID | Requisito |
|---|---|
| RF-01 | Manter catálogo mestre com identificador interno único e código de referência do fornecedor |
| RF-02 | Registrar descrição, categoria, família, especificação e informação de embalagem |
| RF-03 | Permitir validação da unidade de controle por produto |
| RF-04 | Controlar saldos separados para depósito e veículo |
| RF-05 | Registrar entradas, saídas, transferências e ajustes |
| RF-06 | Validar SKU, quantidade, tipo de movimento e locais |
| RF-07 | Restringir o catálogo do veículo aos grupos autorizados |
| RF-08 | Parametrizar estoque mínimo e estoque-alvo por SKU e local |
| RF-09 | Sinalizar itens abaixo do mínimo e sugerir quantidade de reposição |
| RF-10 | Registrar checklist de aquisição com obra, solicitante, prioridade e quantidade |
| RF-11 | Registrar fornecedor, cotação, aprovação, pedido e recebimento |
| RF-12 | Registrar contagem física e divergência de inventário |
| RF-13 | Disponibilizar filtros e relatórios operacionais e gerenciais |
| RF-14 | Consolidar os saldos sem duplicar quantidades transferidas entre locais |

## Regras de negócio

| ID | Regra |
|---|---|
| RN-01 | O SKU interno deve ser único, mesmo que o catálogo de origem repita um código em famílias diferentes |
| RN-02 | O código original deve ser preservado em coluna separada |
| RN-03 | Quantidade por embalagem não equivale automaticamente à unidade de controle |
| RN-04 | O saldo atual é o saldo inicial somado aos impactos válidos de movimentação |
| RN-05 | Transferências debitam a origem e creditam o destino |
| RN-06 | Um SKU fora da lista autorizada não pode movimentar o estoque veicular |
| RN-07 | Status de reposição depende dos parâmetros definidos pelo responsável |
| RN-08 | Quantidade sugerida de reposição deve considerar o estoque-alvo menos o saldo atual, quando abaixo do mínimo |
| RN-09 | Custo e valor do estoque não devem ser presumidos a partir do catálogo comercial |
| RN-10 | Ajustes devem registrar motivo e responsável |

## Requisitos não funcionais

- interface compreensível para usuários administrativos e operacionais;
- tabelas filtráveis e cabeçalhos padronizados;
- integridade das fórmulas;
- consistência de SKU e unidades;
- trilha de movimentação;
- possibilidade de cópia de segurança e controle de versão;
- proteção contra edição acidental de fórmulas críticas.

## Critérios de aceite essenciais

1. Uma entrada válida aumenta o saldo do local de destino.
2. Uma saída válida reduz o saldo do local de origem.
3. Uma transferência reduz a origem e aumenta o destino na mesma quantidade.
4. Um SKU não autorizado no veículo é bloqueado.
5. Item abaixo do mínimo recebe status de reposição.
6. Recebimentos parciais mantêm saldo a receber.
7. Inventário evidencia divergência entre contagem e saldo sistêmico.
