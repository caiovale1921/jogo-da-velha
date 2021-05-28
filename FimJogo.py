#Módulo resposável por validar o fim de jogo

def ValidarJogo(cont, player1, player2):
    if(cont >= 9):
        print('-=' *30)
        if((cont - 1) % 2 == 0):
            print('Quem ganhou foi: ' + player1)
        else:
            print('Quem ganhou foi: '+ player2)
        return('True')
    else:
        return('False')

