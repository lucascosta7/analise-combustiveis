from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import os

app = FastAPI(title="Análise de Combustíveis API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

CSV_PATH = os.path.join(os.path.dirname(__file__), "../data/precos-gasolina-etanol-10.csv")

# Carrega o CSV uma única vez
df = pd.read_csv(CSV_PATH, sep=";", decimal=",", low_memory=False)

# Prepara o DataFrame
df = df[['Estado - Sigla', 'Municipio', 'Produto', 'Valor de Venda', 'Bandeira']].copy()
df['Valor de Venda'] = pd.to_numeric(df['Valor de Venda'].astype(str).str.replace(',', '.'), errors='coerce')
df = df.dropna(subset=['Valor de Venda'])


@app.get("/")
def root():
    return {"status": "API de Análise de Combustíveis rodando!"}


@app.get("/produtos")
def preco_por_produto():
    resultado = (
        df.groupby("Produto")["Valor de Venda"]
        .agg(menor_preco="min", maior_preco="max", preco_medio="mean")
        .round(2)
        .reset_index()
    )
    return resultado.to_dict(orient="records")


@app.get("/media-estado")
def media_por_estado():
    resultado = (
        df.groupby("Estado - Sigla")["Valor de Venda"]
        .mean()
        .round(2)
        .reset_index()
        .rename(columns={"Estado - Sigla": "estado", "Valor de Venda": "preco_medio"})
        .sort_values("preco_medio")
    )
    return resultado.to_dict(orient="records")


@app.get("/media-bandeira")
def media_por_bandeira():
    resultado = (
        df.groupby("Bandeira")["Valor de Venda"]
        .mean()
        .round(2)
        .reset_index()
        .rename(columns={"Valor de Venda": "preco_medio"})
        .sort_values("preco_medio")
    )
    return resultado.to_dict(orient="records")


@app.get("/media-estado/{sigla}")
def media_por_combustivel_estado(sigla: str):
    filtrado = df[df["Estado - Sigla"] == sigla.upper()]
    if filtrado.empty:
        return {"erro": f"Estado '{sigla.upper()}' não encontrado ou sem dados."}
    resultado = (
        filtrado.groupby("Produto")["Valor de Venda"]
        .mean()
        .round(2)
        .reset_index()
        .rename(columns={"Valor de Venda": "preco_medio"})
    )
    return {"estado": sigla.upper(), "dados": resultado.to_dict(orient="records")}


@app.get("/municipios")
def coletas_por_municipio():
    resultado = (
        df.groupby("Municipio")
        .size()
        .reset_index(name="count")
        .sort_values("count", ascending=False)
        .head(20)
    )
    return resultado.to_dict(orient="records")