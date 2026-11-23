# 05 — Catálogo e governança de dados

## Fonte de referência

Foi indicado como referência o arquivo **SEM-FUNCAO-PESQUISA-Catalogo-Digital.pdf**, Catálogo de Produtos da Pedra Boa, Edição 04. O documento identifica endereço e contato comercial da empresa e indica atualização de maio de 2022 no rodapé das páginas consultadas.

O catálogo organiza famílias como Hidráulica, Ferramentas Elétricas e Acessórios, Ferragens, Fixadores, Elétrica, Ferramentas Manuais, Jardinagem, Químicos, Pinturas e Acessórios, Segurança, Abrasivos, Fitas e Adesivos, Utilidades, Parafusos e Gás.

Nas páginas consultadas, os registros apresentam código, descrição/variante e embalagem. A embalagem é uma informação comercial do catálogo e não deve ser tratada automaticamente como unidade de movimentação do estoque.

## Política de uso da fonte

- preservar a referência do catálogo, edição e data;
- manter o código de origem em campo separado do SKU interno;
- validar possíveis códigos repetidos em famílias diferentes;
- não presumir preços, disponibilidade ou condições atuais;
- confirmar especificação, embalagem e código vigente com o fornecedor;
- não redistribuir o PDF integral nem reproduzir o catálogo comercial completo sem autorização do titular.

## Modelo de dados recomendado

| Campo | Origem / regra |
|---|---|
| SKU interno | Gerado para distinguir cada variante de produto |
| Código Pedra Boa | Transcrito da referência comercial, quando aplicável |
| Categoria | Família de produtos do catálogo ou classificação interna |
| Família | Grupo comercial do produto |
| Descrição | Descrição do catálogo, complementada apenas quando confirmada |
| Variante | Dimensão, bitola, capacidade ou apresentação |
| Embalagem comercial | Quantidade por embalagem informada na fonte |
| Unidade de controle | Validada com a operação; não presumida |
| Estoque mínimo/alvo | Definido pela gestão com base no consumo e prazo de reposição |
| Custo unitário | Obtido por cotação/nota de compra válida |
| Fornecedor | Preferencial ou efetivamente utilizado, conforme compra |

## Qualidade e manutenção

1. Conferir duplicidades por código, descrição e variante.
2. Não fundir produtos de famílias distintas apenas por terem o mesmo código.
3. Padronizar unidades e dimensões.
4. Registrar a data da última conferência.
5. Manter histórico de alterações relevantes.
6. Desativar itens descontinuados sem apagar histórico de movimentação.
7. Realizar revisão periódica dos mínimos, alvos e fornecedores.

## Estoque veicular

O catálogo móvel deve ser uma lista autorizada e derivada do catálogo mestre. O recorte deve contemplar apenas conexões hidráulicas, adesivos/colas para PVC, fita veda-rosca, fitas isolantes e fios nas bitolas permitidas pela operação. Qualquer SKU novo exige validação explícita.

## Nota de responsabilidade

O catálogo consultado é uma referência datada de 2022. Sua consulta não confirma que o produto, código, embalagem, preço ou disponibilidade permaneça vigente.
