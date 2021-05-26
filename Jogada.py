#Módulo responsável por realizar e validar as jogadas do jogo
import Tabuleiro

#realiza as jogadas de cada jogador
def jogada(cont, player1, player2):
    teste = 'False'
    while(teste == 'False'):
        if(cont % 2 == 0):
            print(f'Quem joga é: {player1}')
        else:
            print(f'Quem joga é: {player2}')
        
        l = input('Informe a linha que deseja jogar: ')
        c = input('Informe a coluna que deseja jogar: ')

        l = int(l)
        c = int(c)

        teste = ValidarJogada(l, c)
    Tabuleiro.tab[l][c] = 1

#validaa a jogada realiza anteriormente
def ValidarJogada(l, c):
    if(l >= 0 and l <= 2 ):
        if(c >= 0 and c <= 2):
            return('True')
        else:
            return('False')
    else:
        return('False')
