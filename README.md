# ⛽ Análise de Preços de Combustíveis no Brasil

> Dashboard interativo com dados públicos do governo federal, processados com PySpark e servidos via FastAPI.

🌐 **[Acesse o Dashboard ao vivo](https://lucascosta7.github.io/analise-combustiveis)**

---

## 📌 Sobre o Projeto

Uma análise de dados sobre os preços de combustíveis no Brasil utilizando dados públicos da ANP (Agência Nacional do Petróleo). O projeto evoluiu de um notebook exploratório no Google Colab para uma aplicação completa com API REST e dashboard interativo hospedado na web.

---

## 🖥️ Screenshots

> Dashboard principal com cards de preços, gráfico por estado e filtro por combustível.

![Dashboard](docs/screenshot.png)

---

## 🎯 Objetivo

Criar um pipeline de análise de dados usando PySpark para extrair insights sobre os preços de combustíveis no Brasil, expondo os resultados via API FastAPI e visualizando-os em um dashboard interativo.

---

## 🛠️ Tecnologias Utilizadas

**Análise de Dados**
- Python 3.11
- PySpark — processamento distribuído dos dados
- Pandas — versão leve para deploy

**Backend**
- FastAPI — API REST com documentação automática
- Uvicorn — servidor ASGI

**Frontend**
- HTML5 / CSS3 / JavaScript
- Chart.js — gráficos interativos

**Infraestrutura**
- Google Colab — exploração inicial dos dados
- Render — hospedagem do backend
- GitHub Pages — hospedagem do frontend

---

## 📊 Análises Disponíveis

| Análise | Endpoint | Visualização |
|---|---|---|
| Preço mínimo, médio e máximo por produto | `GET /produtos` | Cards |
| Preço médio por estado | `GET /media-estado` | Gráfico de barras |
| Preço médio por bandeira | `GET /media-bandeira` | Gráfico horizontal |
| Preço médio por combustível em um estado | `GET /media-estado/{sigla}` | Gráfico de rosca |
| Top 20 municípios com mais coletas | `GET /municipios` | Tabela |

---

## 📎 Dataset

O dataset utilizado foi `precos-gasolina-etanol-10.csv`, disponibilizado publicamente pela ANP (Agência Nacional do Petróleo, Gás Natural e Biocombustíveis) com dados sobre os preços dos combustíveis por estado e município em todo o Brasil.

---

## 🚀 Como Rodar Localmente

### Pré-requisitos

- Python 3.11
- Java 17 (necessário para o PySpark)

### Backend

```bash
# Clone o repositório
git clone https://github.com/lucascosta7/analise-combustiveis.git
cd analise-combustiveis/backend

# Instale as dependências
pip install -r requirements.txt

# Inicie a API
python -m uvicorn main:app --reload
```

A API estará disponível em `http://localhost:8000`.
Documentação interativa em `http://localhost:8000/docs`.

### Frontend

Abra o arquivo `docs/index.html` diretamente no navegador.

> Certifique-se de que a API está rodando antes de abrir o frontend.

---

## 📁 Estrutura do Projeto

```
analise-combustiveis/
├── data/
│   └── precos-gasolina-etanol-10.csv   # Dataset da ANP
├── backend/
│   ├── main.py                          # API FastAPI
│   ├── requirements.txt
│   └── Procfile
├── docs/
│   └── index.html                       # Dashboard frontend
└── analise_combustiveis.ipynb           # Notebook exploratório (PySpark)
```

---

## 💡 Justificativa Técnica

O PySpark foi escolhido na fase de exploração por ser mais rápido e prático para analisar grandes volumes de dados, combinando o Apache Spark com Python. Suas principais vantagens:

- Processamento distribuído de grandes volumes de dados
- Compatibilidade nativa com Python
- Integração com o ecossistema Spark
- Flexibilidade para diferentes tipos de análise

Para o deploy, o backend foi adaptado para usar **Pandas**, que oferece o mesmo resultado analítico com menor consumo de memória — ideal para servidores gratuitos.

O código foi organizado com separação clara entre análises, comentários explicativos e boa legibilidade, facilitando a compreensão por outros desenvolvedores.

---

## 👨‍💻 Autor

**Lucas Gabriel Lopes Costa**
17 anos · Estudante de Desenvolvimento de Sistemas · Etec de Itaquera, São Paulo

[![GitHub](https://img.shields.io/badge/GitHub-lucascosta7-181717?style=flat&logo=github)](https://github.com/lucascosta7)
