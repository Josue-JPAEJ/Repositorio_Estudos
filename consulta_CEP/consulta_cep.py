import requests

def consulta(cep):
    url = 'https://viacep.com.br/ws/%s/json/' % cep
    response = requests.get(url)
    response_json = response.json()
    print(response_json)
    return response_json
