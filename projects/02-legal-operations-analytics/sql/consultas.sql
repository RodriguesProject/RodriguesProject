-- Exemplo didático. A data-base é fixa para reprodutibilidade.
-- Prazo de referência não equivale a prazo processual legal.
WITH base AS (
    SELECT *, DATE '2026-11-13' AS data_base
    FROM demandas_juridicas
)
SELECT COUNT(*) AS demandas_abertas,
       COUNT(*) FILTER (WHERE prazo_referencia < data_base) AS prazos_referencia_vencidos,
       SUM(valor_referencia_brl) AS valor_referencial_aberto
FROM base
WHERE status = 'Em andamento';

-- Distribuição das demandas em andamento por área
SELECT area, COUNT(*) AS quantidade,
       AVG((DATE '2026-11-13' - data_abertura)) AS media_dias_abertas
FROM demandas_juridicas
WHERE status = 'Em andamento'
GROUP BY area
ORDER BY quantidade DESC;
