# Estudo 05 — Automação Administrativa e Triagem

**Tipo:** automação de regras / qualidade de dados / controles operacionais  
**Projeto:** [Automação de Triagem Jurídica](projects/04-automacao-triagem-juridica/README.md)

## Objetivo e limite

O script verifica campos obrigatórios, datas, categorias, prioridades e protocolos duplicados. Ele separa registros validados daqueles que precisam de revisão humana. Não interpreta o mérito jurídico, não decide direitos e não substitui análise profissional.

## Leitura orientada de `src/triagem.py`

| Bloco / função | O que significa |
|---|---|
| Docstring | Delimita explicitamente a automação administrativa |
| Imports | argparse, csv, Counter, datas, caminhos e tipos |
| `REQUIRED_FIELDS` | Contrato de dados de entrada |
| `ALLOWED_CATEGORIES` / `ALLOWED_PRIORITIES` | Catálogos de valores aceitos |
| `clean(value)` | Converte nulo em string vazia e remove espaços nas extremidades |
| `parse_iso_date(value)` | Tenta converter data ISO; retorna None quando inválida |
| `validate_and_split(rows)` | Normaliza campos, detecta IDs repetidos, valida campos, datas e catálogos e separa filas |
| `write_csv(...)` | Cria diretório e grava CSV com cabeçalho |
| `run(input_path, output_dir)` | Lê o arquivo, valida cabeçalho, processa linhas e grava saídas |
| `main()` | Define caminhos padrão e parâmetros CLI |

## Exercícios práticos

1. Acrescente uma categoria permitida e crie teste para ela.
2. Acrescente validação de e-mail administrativo, sem afirmar que o endereço existe.
3. Crie um motivo de revisão para descrição muito curta.
4. Faça com que o script gere contagem de cada tipo de erro.
5. Teste protocolo duplicado com diferenças de maiúsculas/minúsculas.
6. Adicione um teste de data interna anterior à data de recebimento.
7. Explique como evitar que um registro seja aprovado quando possui um campo obrigatório vazio.

## Perguntas de entrevista

1. Que tarefas você automatizou e quais ficaram sob revisão humana?
2. Como tratou dados incompletos?
3. Por que separar registros aprovados e pendentes?
4. Como evita que a automação tome uma decisão jurídica?
5. Como manteria o catálogo de categorias?
6. Que logs e indicadores adicionaria para operação real?
7. Como protegeria dados pessoais em um sistema produtivo?

## Critério de conclusão

Você deve conseguir adicionar uma regra, criar testes de caso válido e inválido, executar a triagem e explicar por que a decisão final continua sob responsabilidade humana.
