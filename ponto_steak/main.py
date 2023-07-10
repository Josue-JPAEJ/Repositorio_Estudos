# Desafio com If, Elif, Else

'''
    Criar um programa que dependendo da temperatura (ºC) do steak
    ele retorna o ponto de cozimento em portugues. O Usuário deverá fornecer a
    temperatura.

TEMPERATURA    -    COZIMENTO
120ºF ou 48ºC   -   Rare (Selada)
130ºF ou 54ºC   -   Medium rare (ao ponto para mal passada)
140ºF ou 60ºC   -   medium (ao ponto)
150ºF ou 65ºC   -   Medium well (ao ponto para bem passada)
160ºF ou 71ºC   -   Well done (bem passada)
'''


def PontoDaCarne(temperatura):
    if temperatura < 48:
        return "Cozinhar mais alguns minutos"
    elif temperatura < 54:
        return "Selada"
    elif temperatura < 60:
        return "Ao ponto para mal passada"
    elif temperatura < 65:
        return "Ao ponto"
    elif temperatura < 71:
        return "Ao ponto para bem passada"
    elif temperatura < 90:
        return "Bem passada"
    else:
        return "Carne queimada"


if __name__ == "__main__":
    try:
        temperatura = int(input("Qual é a temperatura [ºC] da carne?"))
        print(PontoDaCarne(temperatura))
    except Exception as err:
        print(err)
