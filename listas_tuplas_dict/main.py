frutas = ['maça', 'morango', 'uva']

# loop
for fruta in frutas: print(f'Eu gosto de {fruta}')

print(frutas)

frutas.insert(2, 'abacaxi')  # inseriu no index informado
print(frutas)

frutas.append('abacate')  # add no final da lista
print(frutas)

# Desafio 18
print('\n Desafio 18')
estoque_loja = ['BMW X6', 'BMW i5', 'BMW i8']
print('Lista de carros')
print(estoque_loja)

try:
    carro_selecionado = input('Selecione um dos carros na lista: ')
    if carro_selecionado in estoque_loja:
        print('Este carro está disponível')
    else:
        print('Desculpe, este carro não está disponível.')
except Exception as err:
    print(err)

# Desafio 21
print('\n Desafio 21\n')
cidades = ('penha', 'piçarras', 'itajaí')
print(cidades)
cidade = input('Informe o nome de uma cidade: \n')
if cidade.lower() in cidades:
    print(f'A cidade {cidade} está na lista de cidades')
else:
    print(f'A cidade {cidade} não está na lista de cidades')

# Desafio 22
print('\n Desafio 22 \n')
paises = {
    'Brasil': 'Brasília',
    'China': 'Pequim',
    'Japão': 'Tóquio',
    'Israel': 'Jerusalém',
    'Russia': 'Moscou'
}
print(f'\n {paises.keys()} \n')
pais_usuario = input('Digite o nome de um país: \n')
if pais_usuario in paises:
    print(f'A capital de {pais_usuario} é {paises[pais_usuario]}')
else:
    print('Desculpe, não temos informações sobre a capital desse país.')


# Desafio 23
print('\nDesafio 23\n')
friends1 = {'Thimoteo', 'Luiz', 'Aurelio', 'Sebastião', 'Guilherme'}
friends2 = {'Thimoteo', 'Leonardo', 'Junior', 'Sebastião', 'Lucas'}

print('intersection: Retorna os comuns nos dois sets')
print(set(friends1).intersection(friends2))

print('\ndifference: Retorna os que são incomuns nos dois sets')
print(set(friends1).difference(friends2))

print('\nunion: une os dois sets sem duplicar (diferente de listas e tuplas)')
print(set(friends1).union(friends2))




