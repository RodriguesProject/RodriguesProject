# Estudo 02 — Qualidade, Limpeza e Modularização de Dados

**Tipo:** preparação de dados / validação / automação reutilizável  
**Repositórios:** [módulo de limpeza](https://github.com/RodriguesProject/Modulariza-o-em-Python-para-Limpeza-e-Tratamento-de-dados) · [testes do módulo](https://github.com/RodriguesProject/Modulariza-o-em-Python-para-Limpeza-e-Tratamento-de-dados/tree/main/tests)

## Problema

Dados cadastrais podem chegar com pontuação, espaços, formatos diferentes e valores inválidos. O módulo cria campos normalizados e indicadores de validação, sem sobrescrever os valores de origem.

## Leitura orientada de `limpeza.py`

| Trecho / função | Explicação linha a linha por bloco |
|---|---|
| Docstring inicial | Documenta a finalidade do módulo |
| `import re` | Biblioteca padrão para expressões regulares |
| `import pandas as pd` | Biblioteca para dados tabulares e valores ausentes |
| `OBRIGATORIAS` | Conjunto de nomes de colunas exigidas |
| `limpar_numero(valor)` | Trata nulo, converte para texto e remove tudo que não é dígito com regex |
| `normalizar_telefone(valor)` | Remove formatação e prefixo 55 apenas quando o comprimento indica o padrão internacional informado |
| `telefone_tamanho_valido(valor)` | Verifica se o número normalizado tem 10 ou 11 dígitos; não confirma que a linha existe |
| `email_valido(valor)` | Aplica uma expressão regular estrutural; não verifica entrega ou existência da caixa postal |
| `cpf_valido(valor)` | Remove pontuação, rejeita tamanho incorreto e sequências repetidas; calcula os dois dígitos verificadores |
| `tratar_clientes(df)` | Verifica colunas, cria cópia e acrescenta colunas normalizadas/indicadores |
| `gerar_relatorio_clientes(df)` | Confere a presença das colunas de indicadores e soma os casos aprovados |

## CPF: lógica que precisa saber explicar

A validação percorre duas etapas:
1. Calcula o primeiro dígito verificador a partir dos nove primeiros dígitos e pesos decrescentes.
2. Calcula o segundo dígito usando os nove dígitos e o primeiro verificador, com a sequência de pesos correspondente.

O resultado comprova apenas consistência matemática dos dígitos verificadores. Não confirma titularidade, situação cadastral, autenticidade de documento nem regularidade perante a Receita Federal.

## Exercícios práticos

1. Escreva uma função que normalize CEP mantendo apenas dígitos e valide oito dígitos.
2. Acrescente uma regra que identifique telefone com DDD ausente.
3. Modifique `tratar_clientes` para criar uma coluna `cadastro_requer_revisao` se qualquer indicador falhar.
4. Faça um teste com CPF válido, inválido, sequência repetida, nulo e quantidade de dígitos incorreta.
5. Teste que o DataFrame original permanece idêntico depois de `tratar_clientes`.
6. Adicione uma coluna com a lista dos motivos de revisão, em vez de apenas verdadeiro/falso.

## Testes automatizados

Leia `tests/test_limpeza.py`:
- cada método `test_...` representa um cenário;
- `assertEqual` compara resultado esperado e obtido;
- `assertTrue` / `assertFalse` verificam regras booleanas;
- `assertRaises` confirma que uma entrada inválida gera exceção;
- `assert_frame_equal` confirma que o DataFrame de origem não foi modificado.

Execute:

```bash
python -m unittest discover -s tests -v
```

## Perguntas de entrevista

1. Por que separar as rotinas em funções?
2. Qual a diferença entre limpar, normalizar e validar?
3. O que uma regex faz neste projeto?
4. Como os dígitos verificadores do CPF são calculados?
5. Por que a função retorna uma cópia?
6. O que os testes cobrem e o que não cobrem?
7. Como evitar falsos positivos em validação de e-mail?

## Critério de conclusão

Você deve implementar uma nova regra, escrever pelo menos dois testes para ela e explicar por que a validação é apenas estrutural.
