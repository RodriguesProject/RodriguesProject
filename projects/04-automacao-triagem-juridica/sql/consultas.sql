-- Volume por categoria e situação de triagem
SELECT category, triage_status, COUNT(*) AS quantidade
FROM solicitacoes GROUP BY category, triage_status ORDER BY category, triage_status;

-- Distribuição da fila por responsável
SELECT owner, COUNT(*) AS quantidade
FROM solicitacoes WHERE triage_status <> 'Validada'
GROUP BY owner ORDER BY quantidade DESC;

-- Referências internas próximas; não são prazos processuais
SELECT request_id, category, owner, internal_due_date
FROM solicitacoes
WHERE triage_status <> 'Validada'
  AND internal_due_date BETWEEN CURRENT_DATE AND CURRENT_DATE + INTERVAL '5 days'
ORDER BY internal_due_date;
