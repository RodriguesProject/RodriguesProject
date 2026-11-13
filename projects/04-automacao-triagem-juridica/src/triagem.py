"""Validação administrativa de solicitações fictícias; não realiza análise jurídica."""
from __future__ import annotations
import argparse, csv
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Iterable

REQUIRED_FIELDS=("request_id","received_at","requester","category","description","priority_reported","owner","internal_due_date")
ALLOWED_CATEGORIES={"Contratos","Cível","Consumidor","Imobiliário","Empresarial","Trabalhista","Outros"}
ALLOWED_PRIORITIES={"Baixa","Normal","Alta","Urgente"}
OUTPUT_FIELDS=list(REQUIRED_FIELDS)+["validation_errors"]

def clean(value: object)->str:
    return "" if value is None else str(value).strip()

def parse_iso_date(value: str)->str|None:
    try: return date.fromisoformat(value).isoformat()
    except (TypeError,ValueError): return None

def validate_and_split(rows: Iterable[dict[str,object]])->tuple[list[dict[str,str]],list[dict[str,str]]]:
    normalized=[{field:clean(row.get(field,"")) for field in REQUIRED_FIELDS} for row in rows]
    ids=[r["request_id"].upper() for r in normalized if r["request_id"]]
    duplicates={identifier for identifier,count in Counter(ids).items() if count>1}
    categories={x.casefold():x for x in ALLOWED_CATEGORIES}
    priorities={x.casefold():x for x in ALLOWED_PRIORITIES}
    accepted=[]; review=[]
    for row in normalized:
        errors=[]
        for field in REQUIRED_FIELDS:
            if not row[field]: errors.append(f"campo_obrigatorio_ausente:{field}")
        request_id=row["request_id"].upper()
        if request_id in duplicates: errors.append("protocolo_duplicado")
        received=parse_iso_date(row["received_at"])
        due=parse_iso_date(row["internal_due_date"])
        if row["received_at"] and received is None: errors.append("data_recebimento_invalida")
        if row["internal_due_date"] and due is None: errors.append("data_interna_invalida")
        if received and due and due<received: errors.append("data_interna_anterior_ao_recebimento")
        category=categories.get(row["category"].casefold())
        if row["category"] and category is None: errors.append("categoria_fora_do_catalogo")
        priority=priorities.get(row["priority_reported"].casefold())
        if row["priority_reported"] and priority is None: errors.append("prioridade_fora_do_catalogo")
        row["request_id"]=request_id
        if received: row["received_at"]=received
        if due: row["internal_due_date"]=due
        if category: row["category"]=category
        if priority: row["priority_reported"]=priority
        (review if errors else accepted).append({**row,"validation_errors":";".join(errors)})
    return accepted,review

def write_csv(path:Path,rows:list[dict[str,str]])->None:
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",encoding="utf-8-sig",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=OUTPUT_FIELDS);writer.writeheader();writer.writerows(rows)

def run(input_path:Path,output_dir:Path)->dict[str,int]:
    if not input_path.exists(): raise FileNotFoundError(f"Arquivo não encontrado: {input_path}")
    with input_path.open("r",encoding="utf-8-sig",newline="") as f:
        reader=csv.DictReader(f)
        if reader.fieldnames is None: raise ValueError("CSV sem cabeçalho.")
        missing=set(REQUIRED_FIELDS).difference(reader.fieldnames)
        if missing: raise ValueError(f"Colunas ausentes: {sorted(missing)}")
        rows=list(reader)
    accepted,review=validate_and_split(rows)
    write_csv(output_dir/"solicitacoes_validadas.csv",accepted)
    write_csv(output_dir/"solicitacoes_para_revisao.csv",review)
    summary=[{"indicador":"total_recebido","valor":len(rows)},
             {"indicador":"registros_validados","valor":len(accepted)},
             {"indicador":"registros_para_revisao","valor":len(review)}]
    with (output_dir/"indicadores_triagem.csv").open("w",encoding="utf-8-sig",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=["indicador","valor"]);writer.writeheader();writer.writerows(summary)
    return {"total_recebido":len(rows),"registros_validados":len(accepted),"registros_para_revisao":len(review)}

def main()->None:
    root=Path(__file__).resolve().parents[1]
    parser=argparse.ArgumentParser(description="Valida solicitações administrativas fictícias.")
    parser.add_argument("--input",type=Path,default=root/"data"/"solicitacoes_sinteticas.csv")
    parser.add_argument("--output",type=Path,default=root/"outputs")
    args=parser.parse_args();metrics=run(args.input,args.output)
    print(f"Triagem concluída: {metrics['total_recebido']} recebidas, {metrics['registros_validados']} validadas, {metrics['registros_para_revisao']} para revisão humana.")

if __name__=="__main__": main()
