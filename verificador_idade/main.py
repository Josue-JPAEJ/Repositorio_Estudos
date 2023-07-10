# desafio 17
'''
ENTRADA
    idade
SAIDA
    se idade for menor que 13 imprimir: Voce é uma criança
    se idade estiver entre 13 e 19 imprimir: Voce é um adolescente
    se idade for maior ou igual a 20 imprimir: Voce é um adulto
'''

try:
    idade = int(input('Digite a sua idade: '))
    if idade < 13:
        print('Voce é uma criança')
    elif idade < 19:
        print('Voce é um adolescente')
    else:
        print('Voce é um adulto')

except Exception as err:
    print(err)
