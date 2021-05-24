cores = {'limpa': '\033[m',
        'vermelho': '\033[1;31m' ,
        'azul': '\033[1;34m'
    }

player1 = input("Informe o nome do Jogador 1: ")
print('{} joga com as peças {}vermelhas{}'.format(player1, cores['vermelho'], cores['limpa']))
print("-=" *30)

player2 = input("Informe o nome do Jogador 2: ")
print('{} joga com as peças {}azuis{}'.format(player2, cores['azul'], cores['limpa']))
print("-=" *30)

import Tabuleiro 
import Jogada
import FimJogo 
import os #módulo urilizado para limpar a tela

cont = int(0)
jogo = FimJogo.ValidarJogo(cont)
Tabuleiro.tabuleiro()


while( jogo == 'False'):
    Jogada.jogada(cont)
    os.system('clear')
    jogo = FimJogo.ValidarJogo(cont)
    Tabuleiro.tabuleiro()
    cont = cont + 1
    
    
