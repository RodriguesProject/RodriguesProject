import csv, unittest
from datetime import date
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
def read_csv(path):
    with path.open(encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
class PortfolioDataQualityTests(unittest.TestCase):
    def test_retail_shape_unique_ids(self):
        rows=read_csv(ROOT/"01-analise-varejo-python-sql/data/vendas_sinteticas.csv")
        self.assertEqual(len(rows),600)
        ids=[r["pedido_id"] for r in rows];self.assertEqual(len(ids),len(set(ids)))
    def test_retail_dates_and_numeric_values(self):
        rows=read_csv(ROOT/"01-analise-varejo-python-sql/data/vendas_sinteticas.csv")
        for r in rows:
            date.fromisoformat(r["data_pedido"]);self.assertGreater(int(r["quantidade"]),0)
            self.assertGreaterEqual(float(r["preco_unitario"]),0);self.assertGreaterEqual(float(r["custo_unitario"]),0)
    def test_legal_shape_unique_ids(self):
        rows=read_csv(ROOT/"02-legal-operations-analytics/data/demandas_sinteticas.csv")
        self.assertEqual(len(rows),180)
        ids=[r["demanda_id"] for r in rows];self.assertEqual(len(ids),len(set(ids)))
    def test_legal_dates_status_and_values(self):
        rows=read_csv(ROOT/"02-legal-operations-analytics/data/demandas_sinteticas.csv")
        for r in rows:
            date.fromisoformat(r["data_abertura"]);date.fromisoformat(r["ultima_atualizacao"]);date.fromisoformat(r["prazo_referencia"])
            self.assertIn(r["status"],{"Em andamento","Encerrado"});self.assertGreaterEqual(float(r["valor_referencia_brl"]),0)
if __name__=="__main__":unittest.main()
