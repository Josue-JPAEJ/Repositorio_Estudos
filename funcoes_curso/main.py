# Desafio 24
print('Desafio 24')


def quadrado(numero: float) -> float:
    return float(numero) ** 2


try:
    num = float(input('Digite um numero: \n'))
    print(f'O quadrado de {num} é {quadrado(num)}')
except Exception as err:
    print(err)

# Desafio 25
print('\nDesafio 25')


def soma(num1: float, num2: float) -> float:
    return num1 + num2


try:
    user_num1 = float(input('Digite o primeiro numero: '))
    user_num2 = float(input('Digite o segundo numero: '))

    print(f'A soma dos dois numeros é igual a: {soma(user_num1, user_num2)}')
except Exception as err:
    print(err)

# Desafio 26
print('\nDesafio 26')


def potencia(base: float, expoente=2) -> float:
    return base ** expoente


try:
    base_usuario = float(input('Digite o numero da base: \n'))
    expo_usuario = input('Digite o expoente(default 2): \n')
    if expo_usuario:
        print(f'A potencia do numero {base_usuario} é {potencia(base_usuario, float(expo_usuario))}')
    else:
        print(f'A potencia do numero {base_usuario} é {potencia(base_usuario)}')
except Exception as err:
    print(err)

# Desafio 27
print('\nDesafio 27')


def fatorial(numero: int) -> int:
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero - 1)


try:
    num = int(input('Digite um numero: \n'))
    print(f'O fatorial de {num} é {fatorial(num)}')
except Exception as err:
    print(err)

# Desafio 28
print('\n Desafio 28')


def dobrar(numero: float) -> float:
    return numero * 2


def quadrado(numero: float) -> float:
    return dobrar(numero) ** 2


try:
    num = float(input('Digite um numero: \n'))
    print(f'O quadrado do dobro do numero {num} é : {quadrado(num)}')
except Exception as err:
    print(err)

# Desafio 29
print('\n Desafio 29')
try:
    numero_usuario = int(input('Digite um numero que será elevado ao cubo: \n'))
    cubo = lambda x: x ** 3
    print(f'O cubo de {numero_usuario} é {cubo(numero_usuario)}')
except Exception as err:
    print(err)

# Desafio 30
print('\nDesafio 30')
multiplicar = lambda x, y: x * y

try:
    num1 = float(input('Digite o multiplicador: '))
    num2 = float(input('Digite o multiplicando: '))
    print(f'O resultado da multilicacao é : {multiplicar(num1, num2)}')
except Exception as err:
    print(err)
