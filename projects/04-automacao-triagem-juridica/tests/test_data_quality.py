import csv
import unittest
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
PROJECTS = REPO_ROOT / "projects"


def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


class PortfolioDataQualityTests(unittest.TestCase):
    def test_retail_shape_unique_ids(self):
        path = PROJECTS / "01-analise-varejo-python-sql/data/vendas_sinteticas.csv"
        rows = read_csv(path)
        self.assertEqual(len(rows), 600)
        ids = [row["pedido_id"] for row in rows]
        self.assertEqual(len(ids), len(set(ids)))

    def test_retail_dates_and_numeric_values(self):
        path = PROJECTS / "01-analise-varejo-python-sql/data/vendas_sinteticas.csv"
        rows = read_csv(path)
        for row in rows:
            date.fromisoformat(row["data_pedido"])
            self.assertGreater(int(row["quantidade"]), 0)
            self.assertGreaterEqual(float(row["preco_unitario"]), 0)
            self.assertGreaterEqual(float(row["custo_unitario"]), 0)

    def test_legal_shape_unique_ids(self):
        path = PROJECTS / "02-legal-operations-analytics/data/demandas_sinteticas.csv"
        rows = read_csv(path)
        self.assertEqual(len(rows), 180)
        ids = [row["demanda_id"] for row in rows]
        self.assertEqual(len(ids), len(set(ids)))

    def test_legal_dates_status_and_values(self):
        path = PROJECTS / "02-legal-operations-analytics/data/demandas_sinteticas.csv"
        rows = read_csv(path)
        for row in rows:
            date.fromisoformat(row["data_abertura"])
            date.fromisoformat(row["ultima_atualizacao"])
            date.fromisoformat(row["prazo_referencia"])
            self.assertIn(row["status"], {"Em andamento", "Encerrado"})
            self.assertGreaterEqual(float(row["valor_referencia_brl"]), 0)


if __name__ == "__main__":
    unittest.main()
