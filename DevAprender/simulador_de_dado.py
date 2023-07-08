# Simulador de dados https://www.youtube.com/watch?v=7U3-pJZkN-o
# Simular o uso de um dado gerando um valor de 1 até 6

import random
import PySimpleGUI as sg
from time import sleep


class SimuladorDeDado:

    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = "Você gostaria de gerar um novo valor para o dado?"

        #Layout
        self.layout = [
            [sg.Text("Jogar o dado?", key='label')],
            [sg.Button("Sim"), sg.Button("Não")]
        ]

    def Iniciar(self):

        # Criar uma janela
        self.janela = sg.Window("Simulador de Dado", layout=self.layout)

        while True:
            # Ler os valores da tela
            self.eventos, self.valores = self.janela.read()

            try:
                resposta = self.eventos
                if resposta == "Sim":
                    sg.Popup(self.GerarValorDoDado())
                elif resposta == "Não":
                    self.janela["label"].update("Ate logo")
                    sg.Popup("Obrigado!")
                    break

            except Exception as erro:
                sg.Popup(f"Ocorreu um erro ao receber sua resposta {erro}")
                break

    def GerarValorDoDado(self):
        return random.randint(self.valor_minimo, self.valor_maximo)


simulador = SimuladorDeDado()
simulador.Iniciar()
