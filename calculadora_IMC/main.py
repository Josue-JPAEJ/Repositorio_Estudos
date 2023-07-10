# Calculo de IMC - Índice de Massa corporal IMC = peso / altura * altura

'''
ENTRADAS:
    Qual é a sua Altura (cm)
    Qual é o seu peso (Kg)
SAIDA:
    menor que 18,5      -   Magreza
    entre 18,5 e 24,9   -   Normal
    entre 25,0 e 29,9   -   Sobrepeso
    entre 30,0 e 39,9   -   Obesidade
    maior que 40,0      -   Obesidade grave
'''


def calculo_imc(altura, peso):
    return peso / (altura/100)**2


def iniciar():
    try:
        altura = float(input("Qual é a sua altura (cm)? "))
        peso = float(input("Qual é a seu peso (Kg)? "))
        imc = calculo_imc(altura, peso)
        if imc < 18.5:
            print(f"Seu IMC é {imc}. Seu perfil é MAGREZA")
        elif imc < 24.9:
            print(f"Seu IMC é {imc}. Seu perfil é NORMAL")
        elif imc < 29.9:
            print(f"Seu IMC é {imc}. Seu perfil é SOBREPESO")
        elif imc < 39.9:
            print(f"Seu IMC é {imc}. Seu perfil é OBESIDADE")
        else:
            print(f"Seu IMC é {imc}. Seu perfil é OBESIDADE GRAVE")

    except Exception as err:
        print(err)


if __name__ == '__main__':
    iniciar()
