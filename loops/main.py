# desafio 11 usar range em loop for para imprimir de 1 a 10
print("desafio 11 usar range em loop for para imprimir de 1 a 10")

for numero in range(1, 11): print(numero)

# desafio 12 for loop aninhado (nested for loop)
print("\ndesafio 12 for loop aninhado (nested for loop)")

frutas = ['maca', 'laranja', 'pera']
vegetais = ['pepino', 'chuchu', 'alface']

for fruta in frutas:
    for vegetal in vegetais:
        print(fruta, vegetal)

# desafio 13 imprimir na tela de 1 a 10 sem usar for
print("\ndesafio 13 imprimir na tela de 1 a 10 sem usar for")

numero = 1
while numero <= 10:
    print(numero)
    numero += 1

# desafio 14 imprimir na tela de 1 a 10 mas com break no numero 5
# segundo loop de 1 a 10 mas pular a impressao do numero 5 com o 'continue'
print("\ndesafio 14 imprimir na tela de 1 a 10 mas com break no numero 5")

for numero in range(1, 10):
    if numero > 5: break
    print(numero)


print("\nsegundo loop de 1 a 10 mas pular a impressao do numero 5 com o 'continue'")
for num in range(1, 10):
    if num == 5: continue
    print(num)

print("\n desafio 15 contar quantas vezes um item aparece na mesma lista")
frutas = ['maca', 'banana', 'maca', 'maca', 'abacate', 'uva']
contador = 0

for fruta in frutas:
    if fruta == 'maca': contador += 1

print(f'\nNumero de maças na lista: {contador}')
print(frutas)

print("\n desafio 16. Entrada de um numero do usuario")
# se a entrada do usuario for maior que 10 imprimir:
#   o numero é maior que 10
# caso contrario imprimir
#   o numero é menor ou igual a 10

try:
    numero = int(input("Digite um numero: \n"))
    if numero < 10:
        print(f"o numero {numero} é menor que 10.")
    elif numero > 10:
        print(f"o numero {numero} é maior que 10.")
    else:
        print(f"o numero é igual a 10.")
except Exception as err:
    print(err)

# Desafio 19
print('\nDesafio 19')
fruta_usuario = input('Desafio da fruta. Digite o nome de uma fruta: ')
while fruta_usuario.lower() != 'abacate':
    fruta_usuario = input('Resposta errada. Digite o nome de uma fruta: ')

print('Parabens, você acertou a fruta.')

# Desafio 20
print('\n Desafio 20')
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = list(range(1, 11))
for i in num:
    if i % 2 == 0:
        print(f'O numero {i} é   par.')
    else:
        print(f'O numero {i} é impar.')
