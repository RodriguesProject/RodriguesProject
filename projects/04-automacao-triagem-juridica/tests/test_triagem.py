import sys, tempfile, unittest
from pathlib import Path
PROJECT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(PROJECT/"src"))
from triagem import validate_and_split,run

def valid_row(request_id="REQ-TEST-01"):
    return {"request_id":request_id,"received_at":"2026-10-01","requester":"Solicitante teste","category":"Contratos","description":"Solicitação fictícia.","priority_reported":"Normal","owner":"Equipe A","internal_due_date":"2026-10-08"}

class TriageTests(unittest.TestCase):
    def test_valid_record_is_accepted(self):
        accepted,review=validate_and_split([valid_row()])
        self.assertEqual(len(accepted),1);self.assertEqual(review,[])
    def test_missing_requester_goes_to_review(self):
        row=valid_row();row["requester"]=""
        accepted,review=validate_and_split([row])
        self.assertEqual(accepted,[]);self.assertIn("campo_obrigatorio_ausente:requester",review[0]["validation_errors"])
    def test_invalid_date_goes_to_review(self):
        row=valid_row();row["received_at"]="not-a-date"
        accepted,review=validate_and_split([row])
        self.assertEqual(accepted,[]);self.assertIn("data_recebimento_invalida",review[0]["validation_errors"])
    def test_duplicate_protocols_both_go_to_review(self):
        accepted,review=validate_and_split([valid_row(),valid_row()])
        self.assertEqual(accepted,[]);self.assertEqual(len(review),2)
        self.assertTrue(all("protocolo_duplicado" in r["validation_errors"] for r in review))
    def test_unknown_category_goes_to_review(self):
        row=valid_row();row["category"]="Categoria desconhecida"
        accepted,review=validate_and_split([row])
        self.assertEqual(accepted,[]);self.assertIn("categoria_fora_do_catalogo",review[0]["validation_errors"])
    def test_internal_date_before_received_goes_to_review(self):
        row=valid_row();row["internal_due_date"]="2026-09-30"
        accepted,review=validate_and_split([row])
        self.assertEqual(accepted,[]);self.assertIn("data_interna_anterior_ao_recebimento",review[0]["validation_errors"])
    def test_pipeline_writes_three_outputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            metrics=run(PROJECT/"data"/"solicitacoes_sinteticas.csv",Path(tmp)/"outputs")
            self.assertEqual(metrics["total_recebido"],18)
            for name in ["solicitacoes_validadas.csv","solicitacoes_para_revisao.csv","indicadores_triagem.csv"]:
                self.assertTrue((Path(tmp)/"outputs"/name).exists())

if __name__=="__main__": unittest.main()
