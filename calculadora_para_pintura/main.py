# desafio com funções

'''
Criar um programa que calcula a quantidade de tinta necessaria para
pintar uma parede. O usuário deverá fornecer as seguintes informaçoes:
    a) rendimento
    b) altura
    c) largura

O programa deve mostrar na tela a mensagem:
    'Voce necessita de x lata(s) de tinta.
'''


def area_metro_quadrado(altura, largura):
    return altura * largura


def total_de_latas_de_tinta(rendimento, altura, largura):
    return f"Você necessita de {area_metro_quadrado(altura, largura) / rendimento} lata(s) de tinta."


if __name__ == '__main__':
    try:
        rendimento = float(input("Qual o rendimento (m²) de uma lata de tinta? "))
        altura = float(input("Qual é a altura (m) da parede? "))
        largura = float(input("Qual é a largura (m) da parede? "))

        print(total_de_latas_de_tinta(rendimento, altura, largura))

    except Exception as err:
        print(err)

