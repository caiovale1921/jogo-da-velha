import Tabuleiro 
import FimJogo 
import Jogada
import os

cores = {'limpa': '\033[m',
        'vermelho': '\033[1;31m' ,
        'azul': '\033[1;34m'
    }

player1 = input("Informe o nome do Jogador 1: ")
print("-=" *30)

player2 = input("Informe o nome do Jogador 2: ")
print("-=" *30)

cont = int(0)
jogo = FimJogo.ValidarJogo(cont, player1, player2)
Tabuleiro.tabuleiro()

while( jogo == 'False'):
    Jogada.jogada(cont, player1, player2)
    os.system('cls')
    cont = cont + 1
    jogo = FimJogo.ValidarJogo(cont, player1, player2)
    Tabuleiro.tabuleiro()
    
teste = input()
    
