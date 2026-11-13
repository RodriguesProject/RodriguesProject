CREATE TABLE IF NOT EXISTS vendas (
    pedido_id       VARCHAR(20) PRIMARY KEY,
    data_pedido     DATE NOT NULL,
    regiao          VARCHAR(30) NOT NULL,
    canal           VARCHAR(30) NOT NULL,
    categoria       VARCHAR(50) NOT NULL,
    produto         VARCHAR(100) NOT NULL,
    quantidade      INTEGER NOT NULL CHECK (quantidade > 0),
    preco_unitario  NUMERIC(12,2) NOT NULL CHECK (preco_unitario >= 0),
    custo_unitario  NUMERIC(12,2) NOT NULL CHECK (custo_unitario >= 0)
);
