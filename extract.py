# importação da biblioteca requests

import requests

# url do site

url = "https://api.coingecko.com/api/v3/simple/price"

# dict de parametros

params = {
    'ids': 'bitcoin,solana',
    'vs_currencies': 'usd'
} 

# fazer a requisição agora

request = requests.get(url, params=params)

# transformar a resposta em json

dados = request.json()

# exibição na tela

print(dados)

print(dados['bitcoin']['usd'])
print(dados['solana']['usd'])