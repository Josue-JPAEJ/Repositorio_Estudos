import requests


def consulta(cnpj):
    url = 'https://receitaws.com.br/v1/cnpj/' + str(cnpj)
    headers = {"Content-Type": "application/json"}
    response = requests.get(url, headers=headers)
    response_json = response.json()
    return response_json
