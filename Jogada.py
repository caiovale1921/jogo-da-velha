#Módulo responsável por realizar e validar as jogadas do jogo

from multiprocessing.sharedctypes import Value
from pickle import FALSE, TRUE
import Tabuleiro
import Pecas
import os

l = int(0)
c = int(0)

#realiza as jogadas de cada jogador
def jogada(cont, player1, player2):
    teste = FALSE
    while(teste == FALSE):
        if(cont % 2 == 0):
            print('Quem joga é: ' + player1)
        else:
            print('Quem joga é: ' + player2)
        
        l = input('Informe a linha que deseja jogar: ')
    
        c = input('Informe a coluna que deseja jogar: ')

        teste = ValidarJogada(l, c)

    l = int(l)
    c = int(c)
    if(cont % 2 == 0):
        Tabuleiro.tab[l][c] = Pecas.PecasAzuis[0]
    else:
        Tabuleiro.tab[l][c] = Pecas.PecasVermelhas[0]
    
    

#validaa a jogada realiza anteriormente
def ValidarJogada(l, c):
    try:
        teste1 = int(l)
        teste2 = int(c)
    except ValueError:
        os.system('cls')
        print("Posição invalida, informe um número inteiro para as posições!")
        Tabuleiro.tabuleiro()
        return FALSE

    l = int(l)
    c = int(c)
    if(l >= 0 and l <= 2 ) and (c >= 0 and c <= 2):
        if(Tabuleiro.tab[l][c] == "     "):
            return TRUE
        else:
            os.system('cls')
            print("JOGADA INVÁLIDA, VOCÊ NÃO PODE COMER ESTA PEÇA!")
            Tabuleiro.tabuleiro()
            return FALSE
    else:
        os.system('cls')
        print("JOGADA INVÁLIDA, FAVOR REALIZAR UM MOVIMENTO VALIDO!")
        Tabuleiro.tabuleiro()
        return FALSE   