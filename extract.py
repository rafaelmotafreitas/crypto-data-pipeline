# modulos e importacao

import os
import requests
from datetime import datetime, timezone
import psycopg2
from dotenv import load_dotenv

# setup de inicializacao das senhas
load_dotenv()
senhaBancoDeDados = os.getenv("DB_PASSWORD")

# extracao de dados da api

print('Buscando precos na CoinGecko....')
url = 'https://api.coingecko.com/api/v3/simple/price'
params = {
    'ids':'bitcoin,ethereum',
    'vs_currencies':'usd'
}
# pegando os dados e transformando em json
resposta = requests.get(url, params=params)
dadosBrutos = resposta.json()

dataExtracao = datetime.now(timezone.utc).isoformat()

dadosTransformados = []

# preenchimento com os dados

for moeda, valores in dadosBrutos.items():
    dadosTransformados.append({
        "moeda": moeda,
        "valor": valores["usd"],
        "data_extracao": dataExtracao
    })


# carregamento dos dados no postgre

print("Conectando ao PostgreSQL....")

try:
    conexao = psycopg2.connect(
        host="localhost",
        database="crypto_pipeline",
        user="postgres",
        password=senhaBancoDeDados
    )
    cursor = conexao.cursor()

    # O comando SQL com os %s (Placeholders) para segurança contra injeção de código
    sql_insert = """
        INSERT INTO precos_cripto (moeda, valor, data_extracao)
        VALUES (%s, %s, %s);
    """

    print("Inserindo dados no banco...")
    for item in dadosTransformados:
        # Executa o SQL trocando os %s pelos valores reais da nossa lista
        cursor.execute(sql_insert, (item["moeda"], item["valor"], item["data_extracao"]))

    # Salva as alterações definitivamente
    conexao.commit()
    print("Sucesso! O Pipeline ETL rodou perfeitamente. 🎉")

    # Fecha as portas
    cursor.close()
    conexao.close()

except Exception as erro:
    print(f"Ops! Deu algum erro no banco: {erro}")