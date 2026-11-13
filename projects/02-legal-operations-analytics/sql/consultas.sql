-- Data-base fixa para reprodutibilidade.
-- prazo_referencia nao equivale a prazo processual legal.
WITH base AS (SELECT *,DATE '2026-11-13' AS data_base FROM demandas_juridicas)
SELECT COUNT(*) AS demandas_abertas,
 COUNT(*) FILTER(WHERE prazo_referencia<data_base) AS prazos_referencia_vencidos,
 SUM(valor_referencia_brl) AS valor_referencial_aberto
FROM base WHERE status='Em andamento';

-- Distribuição por área e idade média
SELECT area,COUNT(*) AS quantidade,
 AVG(DATE '2026-11-13'-data_abertura) AS media_dias_abertas
FROM demandas_juridicas WHERE status='Em andamento'
GROUP BY area ORDER BY quantidade DESC;

-- Carga por responsável
SELECT responsavel,COUNT(*) AS demandas_em_andamento,
 SUM(valor_referencia_brl) AS valor_referencial
FROM demandas_juridicas WHERE status='Em andamento'
GROUP BY responsavel ORDER BY demandas_em_andamento DESC;

-- Faixas de antiguidade
WITH abertas AS (
 SELECT demanda_id,DATE '2026-11-13'-data_abertura AS dias_aberta
 FROM demandas_juridicas WHERE status='Em andamento'
)
SELECT CASE WHEN dias_aberta<=30 THEN '0-30 dias'
 WHEN dias_aberta<=90 THEN '31-90 dias'
 WHEN dias_aberta<=180 THEN '91-180 dias'
 ELSE 'Mais de 180 dias' END AS faixa_antiguidade,COUNT(*) AS quantidade
FROM abertas GROUP BY 1 ORDER BY MIN(dias_aberta);
