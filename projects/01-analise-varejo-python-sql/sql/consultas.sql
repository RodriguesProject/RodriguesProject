-- 1. Receita, custo e margem bruta por mês
SELECT DATE_TRUNC('month', data_pedido)::date AS mes,
       SUM(quantidade * preco_unitario) AS receita,
       SUM(quantidade * custo_unitario) AS custo,
       SUM(quantidade * (preco_unitario - custo_unitario)) AS margem_bruta
FROM vendas
GROUP BY 1
ORDER BY 1;

-- 2. Desempenho por categoria
SELECT categoria,
       SUM(quantidade * preco_unitario) AS receita,
       SUM(quantidade) AS unidades
FROM vendas
GROUP BY categoria
ORDER BY receita DESC;

-- 3. Participação de cada canal na receita
WITH receita_canal AS (
    SELECT canal, SUM(quantidade * preco_unitario) AS receita
    FROM vendas GROUP BY canal
)
SELECT canal, receita,
       ROUND(100.0 * receita / NULLIF(SUM(receita) OVER (), 0), 2) AS participacao_pct
FROM receita_canal
ORDER BY receita DESC;

-- 4. Regiões por margem bruta
SELECT regiao,
       SUM(quantidade * (preco_unitario - custo_unitario)) AS margem_bruta
FROM vendas
GROUP BY regiao
ORDER BY margem_bruta DESC;
