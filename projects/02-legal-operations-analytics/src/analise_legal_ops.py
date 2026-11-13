from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "demandas_sinteticas.csv"
OUT = ROOT / "outputs"
AS_OF = pd.Timestamp("2026-11-13")


def main() -> None:
    if not DATA.exists():
        raise FileNotFoundError(f"Arquivo de entrada não encontrado: {DATA}")
    OUT.mkdir(exist_ok=True)
    df = pd.read_csv(DATA, parse_dates=["data_abertura", "ultima_atualizacao", "prazo_referencia"])
    required = {"demanda_id", "area", "etapa", "data_abertura", "prazo_referencia", "valor_referencia_brl", "status"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Colunas obrigatórias ausentes: {sorted(missing)}")
    df = df.drop_duplicates(subset=["demanda_id"]).copy()
    df["valor_referencia_brl"] = pd.to_numeric(df["valor_referencia_brl"], errors="coerce")
    df = df.dropna(subset=["data_abertura", "prazo_referencia", "valor_referencia_brl"])
    df = df[df["valor_referencia_brl"] >= 0]
    df["em_andamento"] = df["status"].eq("Em andamento")
    df["prazo_referencia_vencido"] = df["em_andamento"] & (df["prazo_referencia"] < AS_OF)
    df["dias_desde_abertura"] = (AS_OF - df["data_abertura"]).dt.days
    abertas = df[df["em_andamento"]]

    indicadores = pd.DataFrame({"indicador": [
        "total_demandas", "demandas_em_andamento", "demandas_com_prazo_referencia_vencido",
        "valor_referencial_demandas_abertas_brl", "media_dias_desde_abertura_demandas_abertas"
    ], "valor": [
        len(df), len(abertas), int(df["prazo_referencia_vencido"].sum()),
        round(abertas["valor_referencia_brl"].sum(), 2),
        round(abertas["dias_desde_abertura"].mean(), 1) if len(abertas) else 0
    ]})
    indicadores.to_csv(OUT / "indicadores_gerais.csv", index=False, encoding="utf-8")
    abertas.groupby("area", as_index=False).agg(demandas_abertas=("demanda_id", "count"), valor_referencial_brl=("valor_referencia_brl", "sum")).sort_values("demandas_abertas", ascending=False).to_csv(OUT / "abertas_por_area.csv", index=False, encoding="utf-8")
    abertas.groupby("etapa", as_index=False).agg(demandas=("demanda_id", "count")).sort_values("demandas", ascending=False).to_csv(OUT / "abertas_por_etapa.csv", index=False, encoding="utf-8")

    por_area = abertas.groupby("area")["demanda_id"].count().sort_values(ascending=False)
    ax = por_area.plot(kind="bar", figsize=(10, 5), title="Demandas em andamento por área — dados sintéticos")
    ax.set_xlabel("Área")
    ax.set_ylabel("Quantidade de demandas")
    plt.xticks(rotation=35, ha="right")
    plt.tight_layout()
    plt.savefig(OUT / "demandas_por_area.png", dpi=160)
    plt.close()
    print(f"Análise concluída. {len(df)} registros válidos. Data-base: {AS_OF.date()}. Resultados em: {OUT}")


if __name__ == "__main__":
    main()
