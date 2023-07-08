import game
import easygui
import time
from random import randint

msg = ['Ta maluco é',
       'Bateu a cabeça',
       'Se extribufou',
       'Mano, tenta não se machucar',
       'Que que isso, digo mais nada',
       'Pra que isso meuuuuuu',
       'Aiiiiiiii essa doeu',
       'Não viu o obstaculo é? ta precisando de Oculos????'
       ]


def chamar_game(vida, nome_gamer):
    mensagem = ''
    while vida > 0:
        mensagem = game.game(vida, nome_gamer)
        vida -= 1
        if vida <= 0: break
        time.sleep(1)
        rdn_msg = randint(0, (len(msg)-1))
        botao = easygui.buttonbox(f'{msg[rdn_msg]} {nome_gamer} {mensagem} Você tem {vida} vida(s) deseja continuar?', 'Fim do Jogo', ('Continuar', 'Sair'))

        if botao == 'Continuar':
            game.continuar_game()
        else:
            return

    rdn_msg = randint(0, (len(msg)-1))
    botao = easygui.buttonbox(f'{msg[rdn_msg]} {nome_gamer} {mensagem} deseja recomeçar?', 'Fim do Jogo', ('Recomeçar', 'Sair'))
    if botao == 'Recomeçar':
        nome_gamer = easygui.enterbox('Digite seu nome jogador: ', 'Nome do Jogador', nome_gamer)
        if not nome_gamer == None and not nome_gamer == '':
            game.zerar_game()
            vida = 3
            chamar_game(vida, nome_gamer)


if __name__ == '__main__':
    vida = 3
    record = 0
    nome_gamer = easygui.enterbox('Digite seu nome jogador: ', 'Nome do Jogador', 'Jogador1')

    if not nome_gamer == None and not nome_gamer == '':
        chamar_game(vida, nome_gamer)
