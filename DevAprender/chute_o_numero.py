import random


class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 0
        self.valor_maximo = 100
        self.tentar_novamente = True
        self.tentativas = 0

    def Iniciar(self):
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()

        while self.tentar_novamente:
            self.tentativas += 1
            if int(self.chute) > self.valor_aleatorio:
                print("Chute um valor mais baixo!")
                self.PedirValorAleatorio()
            elif int(self.chute) < self.valor_aleatorio:
                print("Chute um valor mais alto!")
                self.PedirValorAleatorio()
            elif int(self.chute) == self.valor_aleatorio:
                self.tentar_novamente = False
                print("PARABENS VOCÊ ACERTOU!!!")
                print(f"Tentativas {self.tentativas}")

    def PedirValorAleatorio(self):
        self.chute = input("Chute um número [0 a 100]: ")

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)


chute_numero = ChuteONumero()
chute_numero.Iniciar()
