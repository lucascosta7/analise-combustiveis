from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import os

app = FastAPI(title="Análise de Combustíveis API")

# Permite o frontend acessar a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Caminho do CSV
CSV_PATH = os.path.join(os.path.dirname(__file__), "../data/precos-gasolina-etanol-10.csv")

# Inicia o Spark uma única vez
spark = (
    SparkSession
    .builder
    .appName("Analise-Combustiveis-API")
    .config("spark.ui.enabled", "false")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

# Carrega e prepara o DataFrame uma única vez
def carregar_df():
    df = spark.read.csv(CSV_PATH, header=True, inferSchema=True, sep=";")
    df_precos = (
        df
        .select('Estado - Sigla', 'Municipio', 'Produto', 'Valor de Venda', 'Bandeira')
        .withColumn(
            "Valor de Venda",
            F.regexp_replace(F.col("Valor de Venda"), ",", ".")
            .cast("float")
        )
    )
    return df, df_precos

df_raw, df_precos = carregar_df()


# ── Endpoints ──────────────────────────────────────────

@app.get("/")
def root():
    return {"status": "API de Análise de Combustíveis rodando!"}


@app.get("/produtos")
def preco_por_produto():
    """Preço mínimo e máximo por produto."""
    resultado = (
        df_precos
        .groupBy("Produto")
        .agg(
            F.round(F.min("Valor de Venda"), 2).alias("menor_preco"),
            F.round(F.max("Valor de Venda"), 2).alias("maior_preco"),
            F.round(F.avg("Valor de Venda"), 2).alias("preco_medio"),
        )
        .orderBy("Produto")
    )
    return resultado.toPandas().to_dict(orient="records")


@app.get("/media-estado")
def media_por_estado():
    """Preço médio por estado (todas as regiões)."""
    resultado = (
        df_precos
        .groupBy("Estado - Sigla")
        .agg(
            F.round(F.avg("Valor de Venda"), 2).alias("preco_medio")
        )
        .orderBy("preco_medio")
    )
    return resultado.toPandas().rename(columns={"Estado - Sigla": "estado"}).to_dict(orient="records")


@app.get("/media-bandeira")
def media_por_bandeira():
    """Preço médio por bandeira."""
    resultado = (
        df_precos
        .groupBy("Bandeira")
        .agg(
            F.round(F.avg("Valor de Venda"), 2).alias("preco_medio")
        )
        .orderBy("preco_medio")
    )
    return resultado.toPandas().to_dict(orient="records")


@app.get("/media-estado/{sigla}")
def media_por_combustivel_estado(sigla: str):
    """Preço médio por combustível em um estado específico."""
    resultado = (
        df_precos
        .filter(F.col("Estado - Sigla") == sigla.upper())
        .groupBy("Produto")
        .agg(
            F.round(F.avg("Valor de Venda"), 2).alias("preco_medio")
        )
        .orderBy("Produto")
    )
    dados = resultado.toPandas().to_dict(orient="records")
    if not dados:
        return {"erro": f"Estado '{sigla.upper()}' não encontrado ou sem dados."}
    return {"estado": sigla.upper(), "dados": dados}


@app.get("/municipios")
def coletas_por_municipio():
    """Top 20 municípios com mais coletas registradas."""
    resultado = (
        df_raw
        .groupBy("Municipio")
        .count()
        .orderBy(F.col("count").desc())
        .limit(20)
    )
    return resultado.toPandas().to_dict(orient="records")