#Módulo resposável por validar o fim de jogo

def ValidarJogo(cont, player1, player2):
    if(cont >= 3):
        print('-=' *30)
        if(cont % 2 == 0):
            print(f'Quem ganhou foi: {player1}')
        else:
            print(f'Quem ganhou foi: {player2}')
        return('True')
    else:
        return('False')

