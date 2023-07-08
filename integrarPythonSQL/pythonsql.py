import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=JOSUE_NOTEBOOK;"
    "Database=PythonSQL;"
)

conexao = pyodbc.connect(dados_conexao)
print('Conexão bem sucedida')

cursor = conexao.cursor()

id = 3
cliente = 'Liliane'
produto = 'Carro'
data = '2012/01/14'
preco = 9000
quantidade = 1

comando = f"""INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES
    ({id}, '{cliente}', '{produto}', '{data}', {preco}, {quantidade})"""

cursor.execute(comando)
cursor.commit()
