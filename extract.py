# importação da biblioteca requests

import requests
from datetime import datetime, timezone

def extrair_dados_crypto():

    # url do site 
    url = "https://api.coingecko.com/api/v3/simple/price"

    # parametros
    params = {
        'ids':'bitcoin,solana',
        'vs_currencies':'usd'
    }

    # fazendo a requisicao
    request = requests.get(url, params=params)

    #convertendo para json

    dados = request.json()

    # atribuindo o tempo
    tempoDaExtracao = datetime.now(timezone.utc)

    #exibição na tela
    print(f"Moedas solicitadas: {dados}")

    # dicionario de de dados 

    dadosTratados = [
        {
            "moeda": "bitcoin",
            "valor": dados['bitcoin']['usd'],
            "data_extracao": tempoDaExtracao.isoformat()
        },
        {
            "moeda": "solana",
            "valor": dados['solana']['usd'],
            "data_extracao": tempoDaExtracao.isoformat()
        }
    ]

    # retorno do dicionario

    return dadosTratados


resultado = extrair_dados_crypto()

print(resultado)



