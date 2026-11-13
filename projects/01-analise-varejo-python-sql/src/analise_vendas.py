from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "vendas_sinteticas.csv"
OUT = ROOT / "outputs"


def main() -> None:
    if not DATA.exists():
        raise FileNotFoundError(f"Arquivo de entrada não encontrado: {DATA}")
    OUT.mkdir(exist_ok=True)
    df = pd.read_csv(DATA, parse_dates=["data_pedido"])
    required = {"pedido_id", "data_pedido", "regiao", "canal", "categoria", "quantidade", "preco_unitario", "custo_unitario"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Colunas obrigatórias ausentes: {sorted(missing)}")
    df = df.drop_duplicates(subset=["pedido_id"]).copy()
    numeric = ["quantidade", "preco_unitario", "custo_unitario"]
    for col in numeric:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=numeric + ["data_pedido"])
    df = df[(df["quantidade"] > 0) & (df["preco_unitario"] >= 0) & (df["custo_unitario"] >= 0)]
    df["receita"] = df["quantidade"] * df["preco_unitario"]
    df["custo"] = df["quantidade"] * df["custo_unitario"]
    df["margem_bruta"] = df["receita"] - df["custo"]
    df["mes"] = df["data_pedido"].dt.to_period("M").astype(str)

    resumo = pd.DataFrame({"indicador": ["pedidos", "unidades", "receita", "custo", "margem_bruta"], "valor": [df["pedido_id"].nunique(), int(df["quantidade"].sum()), round(df["receita"].sum(), 2), round(df["custo"].sum(), 2), round(df["margem_bruta"].sum(), 2)]})
    resumo.to_csv(OUT / "indicadores_gerais.csv", index=False, encoding="utf-8")
    df.groupby("categoria", as_index=False).agg(receita=("receita", "sum"), margem_bruta=("margem_bruta", "sum"), unidades=("quantidade", "sum")).sort_values("receita", ascending=False).to_csv(OUT / "por_categoria.csv", index=False, encoding="utf-8")
    df.groupby("mes", as_index=False).agg(receita=("receita", "sum"), margem_bruta=("margem_bruta", "sum")).sort_values("mes").to_csv(OUT / "por_mes.csv", index=False, encoding="utf-8")

    mensal = df.groupby("mes")["receita"].sum().sort_index()
    ax = mensal.plot(kind="bar", figsize=(11, 5), title="Receita mensal — base sintética")
    ax.set_xlabel("Mês")
    ax.set_ylabel("Receita (R$)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(OUT / "receita_mensal.png", dpi=160)
    plt.close()
    print(f"Análise concluída. {len(df)} registros válidos. Resultados em: {OUT}")


if __name__ == "__main__":
    main()
