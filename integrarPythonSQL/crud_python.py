import mysql.connector

user_bd = 'root'
senha_bd = '#128035#jpa&J'

conexao = mysql.connector.connect(
    host='localhost',
    user=user_bd,
    password=senha_bd,
    database='bdpython',
)
cursor = conexao.cursor()

#CRUD (Digitar um dos CRUD aqui)________________________





#-------------------------------------------------------

#Sempre finalizar com esses dois
cursor.close()
conexao.close()

#CREAT
"""
nome_produto = 'chocolate'
valor = 15
comando = f"INSERT INTO vendas (nome_produto, valor) VALUES ('{nome_produto}', '{valor}')"
cursor.execute(comando)
conexao.commit()  # Utilizar no final do codigo quando alterar/editar o BD
"""

#READ
"""
comando = f'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall()   # Le o banco de dados
print(resultado)    #[(1, 'todynho', 3), (2, 'chocolate', 15)] lista de tuplas
"""

#UPDATE
"""
valor = 6
idvendas = 1
comando = f'UPDATE vendas SET valor = {valor} WHERE idVendas = "{idvendas}"'
cursor.execute(comando)
conexao.commit()  # Utilizar no final do codigo quando alterar/editar o BD
"""

#DELETE
"""
idvendas = 2
comando = f'DELETE FROM vendas WHERE idVendas = "{idvendas}"'
cursor.execute(comando)
conexao.commit()  # Utilizar no final do codigo quando alterar/editar o BD
"""