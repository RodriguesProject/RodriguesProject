# Projeto 04 — Automação de Triagem Jurídico-Administrativa

Demonstração de automação introdutória em Python para recebimento, validação e organização de solicitações em um cenário jurídico-administrativo fictício.

> **Escopo:** o script valida campos e formatos e organiza registros para conferência. Não interpreta documentos, não avalia mérito jurídico, não calcula prazos processuais e não substitui revisão humana.

## Problema demonstrativo

Solicitações recebidas por diferentes canais podem apresentar campos ausentes, identificadores repetidos, categorias não padronizadas ou datas inválidas. O projeto propõe uma validação inicial para separar registros completos daqueles que exigem conferência.

## Funcionalidades

1. Leitura de arquivo CSV.
2. Padronização de espaços e identificadores.
3. Verificação de campos obrigatórios.
4. Identificação de protocolos duplicados.
5. Validação de datas ISO e consistência entre datas informadas.
6. Conferência de categoria e prioridade com listas de referência.
7. Geração de filas de registros validados e pendentes, além de indicadores de triagem.

## Tecnologias

Python 3 e biblioteca padrão: `csv`, `argparse`, `datetime`, `pathlib` e `unittest`.

## Dados

A base `data/solicitacoes_sinteticas.csv` contém 18 registros artificiais. Algumas inconsistências foram inseridas intencionalmente para demonstrar as regras de validação. Não há clientes ou processos reais.

## Execução

A partir da raiz do repositório:

```bash
python projects/04-automacao-triagem-juridica/src/triagem.py
```

Para informar caminhos explicitamente:

```bash
python projects/04-automacao-triagem-juridica/src/triagem.py --input projects/04-automacao-triagem-juridica/data/solicitacoes_sinteticas.csv --output projects/04-automacao-triagem-juridica/outputs
```

## Testes automatizados

```bash
python -m unittest discover -s projects/04-automacao-triagem-juridica/tests -v
python -m unittest discover -s projects/04-automacao-triagem-juridica -p "test_data_quality.py" -v
```

Os testes cobrem registros completos, campos obrigatórios ausentes, datas inválidas, protocolos duplicados, categorias fora do catálogo e consistência entre datas. Há também verificações de integridade das bases sintéticas dos projetos de Varejo e Legal Operations.

## Estrutura

- `data/`: solicitações sintéticas.
- `src/triagem.py`: regras de validação e geração de relatórios.
- `tests/`: testes unitários, integração CSV e verificações de integridade.
- `sql/`: modelo relacional e consultas de acompanhamento.

## Limitações e governança

A prioridade é informada na entrada; o script apenas valida se ela pertence ao catálogo. A data interna é uma referência administrativa informada no CSV, não um prazo legal. Nenhuma conclusão jurídica é gerada. Registros pendentes devem ser revisados por pessoa autorizada.

Uma implantação real exigiria controles de acesso, retenção, auditoria, segurança e proteção de dados. Este repositório apresenta apenas um exercício de aprendizagem com dados artificiais.
