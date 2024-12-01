import requests

# URL da API para listar todos os mercados na CoinEx
url = "https://api.coinex.com/v1/market/list"

# Fazendo a requisição para a API
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    data = response.json()
    
    # Verificando se a resposta contém dados de mercados
    if data['code'] == 0:
        markets = data['data']
        
        # Lista para armazenar mercados que terminam com 'USDT'
        usdt_markets = []
        
        # se market (string) terminar com 'USDT' (pares de criptomoedas com 'USDT'), então salva ele na lista de criptomoeda de interesse
        for market in markets:
            if market.endswith('USDT'):
                usdt_markets.append(market)
        
        # Exibindo os mercados que terminam com 'USDT'
        print("Mercados que terminam com 'USDT':")
        for usdt_market in usdt_markets:
            print(usdt_market)
    else:
        print("Erro ao obter os dados:", data['message'])
else:
    print("Erro na requisição. Status:", response.status_code)
