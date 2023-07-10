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

