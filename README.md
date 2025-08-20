# Projeto de Análise de Preços de Combustíveis no Brasil
📌 Uma análise de dados utilizando o PySpark de uma base de dados pública (do governo) sobre o preço dos combustíveis no Brasil.

## 🎯 Objetivo
Criar um pipeline simples de análise de dados usando PySpark para extrair insights sobre preços de combustíveis no Brasil.

## 🛠️ Tecnologias usadas
- Python
- PySpark
- Google Colab

## 📊 Análises feitas
- Produto mais barato e mais caro.
- Preço médio por estado.
- Preço médio por bandeira.
- Preço médio por combustível em um único estado.
- Coletas de preços foram registradas por município

## 💡 Justificativa Técnica
Para esse projeto, eu decidi utilizar o PySpark por que é mais rápido e mais prático de utilizar do que outros frameworks (como o Pandas), por combinar Apache Spark com Python, basicamente tudo fica mais fácil para realizar análises de dados concretos. Dito isso, trouxe aqui algumas vantagens do PySpark:

- Processamento de grandes volumes de dados.
- Compatibilidade com Python.
- Integração com o ecossistema Spark.
- Flexibilidade.

Além dessas considerações, também adotei algumas boas práticas, como comentários para "identificar" o que um determinado comando faz (por exemplo para importar os dados da base de dados), também deixei os códigos das análises "separados" para ficar mais legível e fácil de entender o que cada comando efetua, priorizando sempre a boa legibilidade do código. Com essas práticas, acredito que deixou o projeto melhor e fácil de absorver, evitando que o leitor se perca e não consiga entender o código.

## 📎 Dataset
O dataset utilizado foi `precos-gasolina-etanol-10.csv`, com dados sobre os preços dos combustíveis por estado e municipio.

## 👨‍💻 Autor
Lucas Gabriel Lopes Costa — 16 anos, estudante de Desenvolvimento de Sistemas na Etec de Itaquera.
