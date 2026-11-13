# Requisitos

## Requisitos funcionais

- RF01: permitir registrar uma nova solicitação.
- RF02: validar os campos obrigatórios antes do envio.
- RF03: gerar identificador único para cada solicitação.
- RF04: permitir classificar categoria, prioridade e responsável.
- RF05: registrar alterações de status com data e usuário.
- RF06: permitir consulta por identificador, categoria, status e responsável.
- RF07: disponibilizar relatório de volume por período, categoria e status.

## Requisitos não funcionais

- RNF01: restringir acesso conforme perfil autorizado.
- RNF02: registrar histórico de alterações.
- RNF03: apresentar mensagens claras de validação.
- RNF04: permitir exportação de relatórios em formato aberto.
- RNF05: evitar exposição de dados pessoais em relatórios de acesso amplo.

## Regras de negócio propostas

- RN01: toda solicitação deve possuir identificador único.
- RN02: solicitações incompletas retornam para complementação.
- RN03: alteração de responsável deve ser registrada.
- RN04: prioridade deve seguir matriz aprovada pela coordenação.
