# https://www.youtube.com/watch?v=DCBlt_z2UOE

'''
    faça um programa que tenha uma funcao chamada
    contador(), que receba 3 parametros: inicio,
    fim e passo. Seu programa tem que realizar 3 contagens
    atravez da funcao criada:
        a) de 1 ate 10, de 1 em 1
        b) de 10 ate 0, de 2 em 2
        c) uma contagem personalizada.
'''

from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    elif passo == 0:
        passo = 1

    print('-=' * 20)
    print(f"contagem de {inicio} ate {fim} de {passo} em {passo}")
    sleep(2.5)

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f"{cont}", end=" ", flush=True)
            cont += passo
            sleep(0.5)
        print("FIM")
    else:
        cont = inicio
        while cont >= fim:
            print(f"{cont}", end=" ", flush=True)
            cont -= passo
            sleep(0.5)
        print("FIM")


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim:    '))
passo = int(input('Passo:  '))

contador(inicio, fim, passo)
