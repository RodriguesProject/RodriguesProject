CREATE TABLE IF NOT EXISTS demandas_juridicas (
    demanda_id              VARCHAR(20) PRIMARY KEY,
    area                    VARCHAR(40) NOT NULL,
    etapa                   VARCHAR(60) NOT NULL,
    data_abertura           DATE NOT NULL,
    ultima_atualizacao      DATE,
    prazo_referencia        DATE,
    valor_referencia_brl    NUMERIC(14,2) NOT NULL CHECK (valor_referencia_brl >= 0),
    responsavel             VARCHAR(40),
    status                  VARCHAR(30) NOT NULL
);
