# Projeto 04 — Automação de Triagem Jurídico-Administrativa

**Objetivo:** demonstrar automação introdutória de recebimento e validação de solicitações administrativas em um contexto jurídico fictício.

> Estudo de aprendizagem. O script valida campos e formatos. Não interpreta documentos, não classifica mérito jurídico, não calcula prazos processuais e não substitui revisão humana.

## Problema demonstrativo
Solicitações recebidas por diferentes canais podem chegar com campos ausentes, identificadores repetidos, categorias não padronizadas ou datas inválidas. O projeto organiza uma fila inicial para registros completos e encaminha inconsistências para conferência humana.

## O que a automação faz
1. Lê um CSV.
2. Padroniza espaços e identificadores.
3. Verifica campos obrigatórios.
4. Identifica protocolos duplicados.
5. Valida datas ISO e consistência entre recebimento e data interna informada.
6. Confere categoria e prioridade contra listas de referência.
7. Gera filas validadas, pendentes e indicadores de triagem.

## Tecnologias
Python 3 e biblioteca padrão: csv, argparse, datetime, pathlib e unittest.

## Dados
A base `data/solicitacoes_sinteticas.csv` contém 18 registros artificiais. Alguns foram intencionalmente criados com inconsistências para demonstrar a validação. Não há clientes ou processos reais.

## Execução
```bash
python src/triagem.py
```

Ou indique caminhos:
```bash
python src/triagem.py --input data/solicitacoes_sinteticas.csv --output outputs
```

## Testes
A partir da raiz do repositório:
```bash
python -m unittest discover -s projects/04-automacao-triagem-juridica/tests -v
python -m unittest discover -s projects/04-automacao-triagem-juridica -p "test_data_quality.py" -v
```

## Estrutura
- `data/`: solicitações sintéticas.
- `src/triagem.py`: validação e relatórios.
- `tests/`: testes unitários, integração CSV e integridade das bases anteriores.
- `sql/`: modelo relacional e consultas de acompanhamento.

## Limitações e governança
A prioridade é informada na entrada; o script apenas valida o catálogo. A data interna é uma referência administrativa informada no CSV, não prazo legal. Nenhuma conclusão jurídica é gerada. Registros pendentes devem ser revisados por pessoa autorizada. Uma implantação real exigiria controles de acesso, retenção, auditoria e proteção de dados.
