# História de usuário e critérios de aceite

## História de usuário

Como integrante da equipe de triagem, quero registrar e classificar solicitações em um fluxo padronizado, para que cada demanda tenha responsável, status e histórico rastreável.

## Critérios de aceite

**Cenário 1 — Cadastro completo**
- Dado que o usuário preenche todos os campos obrigatórios;
- Quando envia a solicitação;
- Então o sistema gera um identificador único e apresenta confirmação.

**Cenário 2 — Cadastro incompleto**
- Dado que falta um campo obrigatório;
- Quando o usuário tenta enviar;
- Então o sistema impede o envio e identifica o campo pendente.

**Cenário 3 — Mudança de responsável**
- Dado que a solicitação está registrada;
- Quando a coordenação altera o responsável;
- Então o sistema registra responsável anterior, novo responsável, data e usuário que realizou a alteração.

**Cenário 4 — Consulta gerencial**
- Dado que existem solicitações registradas;
- Quando a coordenação filtra por período e status;
- Então o relatório apresenta a quantidade correspondente aos filtros aplicados.
