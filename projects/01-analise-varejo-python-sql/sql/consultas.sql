-- 1. Receita, custo e margem por mês
SELECT DATE_TRUNC('month',data_pedido)::date AS mes,
 SUM(quantidade*preco_unitario) AS receita,
 SUM(quantidade*custo_unitario) AS custo,
 SUM(quantidade*(preco_unitario-custo_unitario)) AS margem_bruta
FROM vendas GROUP BY 1 ORDER BY 1;

-- 2. Desempenho por categoria
SELECT categoria,SUM(quantidade*preco_unitario) AS receita,SUM(quantidade) AS unidades
FROM vendas GROUP BY categoria ORDER BY receita DESC;

-- 3. Participação de cada canal na receita
WITH receita_canal AS (
 SELECT canal,SUM(quantidade*preco_unitario) AS receita FROM vendas GROUP BY canal
)
SELECT canal,receita,
 ROUND(100.0*receita/NULLIF(SUM(receita) OVER(),0),2) AS participacao_pct
FROM receita_canal ORDER BY receita DESC;

-- 4. Regiões por margem bruta
SELECT regiao,SUM(quantidade*(preco_unitario-custo_unitario)) AS margem_bruta
FROM vendas GROUP BY regiao ORDER BY margem_bruta DESC;

-- 5. Variação mensal da receita com LAG
WITH mensal AS (
 SELECT DATE_TRUNC('month',data_pedido)::date AS mes,SUM(quantidade*preco_unitario) AS receita
 FROM vendas GROUP BY 1
)
SELECT mes,receita,LAG(receita) OVER(ORDER BY mes) AS receita_mes_anterior,
 ROUND(100.0*(receita-LAG(receita) OVER(ORDER BY mes))/NULLIF(LAG(receita) OVER(ORDER BY mes),0),2) AS variacao_pct
FROM mensal ORDER BY mes;

-- 6. Produto de maior receita em cada categoria
WITH ranking AS (
 SELECT categoria,produto,SUM(quantidade*preco_unitario) AS receita,
 ROW_NUMBER() OVER(PARTITION BY categoria ORDER BY SUM(quantidade*preco_unitario) DESC) AS posicao
 FROM vendas GROUP BY categoria,produto
)
SELECT categoria,produto,receita FROM ranking WHERE posicao=1 ORDER BY categoria;
