#Módulo resposável por validar o fim de jogo
import JogoDaVelha

def ValidarJogo(cont):
    if(cont > 3):
        print('-=' *30)
        if(cont % 2 == 0):
            print(f'Quem ganhou foi: {JogoDaVelha.player1}')
        else:
            print(f'Quem ganhou foi: {JogoDaVelha.player2}')
        return('True')
    else:
        return('False')

