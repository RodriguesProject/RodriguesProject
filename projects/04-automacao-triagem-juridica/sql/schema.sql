CREATE TABLE IF NOT EXISTS solicitacoes (
 request_id VARCHAR(30) PRIMARY KEY,
 received_at DATE NOT NULL,
 requester VARCHAR(100) NOT NULL,
 category VARCHAR(40) NOT NULL CHECK (category IN ('Contratos','Cível','Consumidor','Imobiliário','Empresarial','Trabalhista','Outros')),
 description TEXT NOT NULL,
 priority_reported VARCHAR(20) NOT NULL CHECK (priority_reported IN ('Baixa','Normal','Alta','Urgente')),
 owner VARCHAR(60) NOT NULL,
 internal_due_date DATE NOT NULL,
 triage_status VARCHAR(20) NOT NULL DEFAULT 'Pendente' CHECK (triage_status IN ('Pendente','Validada','Em revisão'))
);
CREATE INDEX IF NOT EXISTS idx_solicitacoes_status ON solicitacoes (triage_status);
CREATE INDEX IF NOT EXISTS idx_solicitacoes_categoria ON solicitacoes (category);
CREATE INDEX IF NOT EXISTS idx_solicitacoes_responsavel ON solicitacoes (owner);
