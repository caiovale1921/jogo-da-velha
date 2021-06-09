
from pickle import FALSE, TRUE
from colorama import Fore
import Tabuleiro 
import FimJogo 
import Jogada
import os

os.system('cls')
print()
print()

print("-=" *34)
print( "                       JOGO DA VELHA 2.0" )
print("-=" *34)

print()
print()

#solicita o nome de um jogador
player1 = input("  Informe o nome do Jogador 1: ")
print("-=" *34)
print()
print()

#solicita o nome de um jogador
player2 = input("  Informe o nome do Jogador 2: ")
print("-=" *34)
os.system('cls')

#altera as cores dos nomes dos jogadores
player2 = (Fore.RED + f'{player2}' + Fore.RESET)
player1 = (Fore.BLUE + f'{player1}' + Fore.RESET)

VitoriaP1 = int(0)
VitoriaP2 = int(0)

cont = int(0)
jogo = FimJogo.ValidarJogo(cont, player1, player2)
Tabuleiro.tabuleiro()

while( jogo == FALSE):

    Jogada.jogada(cont, player1, player2)
    os.system('cls')
    cont = cont + 1
    jogo = FimJogo.ValidarJogo(cont, player1, player2)
    Tabuleiro.tabuleiro()

    if(jogo == TRUE):
        print()
        reset = input("  Deseja jogar novamente (S/N): ")
        if((reset == "S") or (reset == "s")):
            if(cont % 2 == 0): VitoriaP2 = VitoriaP2 + 1
            else: VitoriaP1 = VitoriaP1 + 1
            jogo = FALSE
            cont = int(0)
            Tabuleiro.tab = [["     " , "     "  , "     " ], ["     " , "     "  , "     " ],["     " , "     "  , "     " ]]
            Tabuleiro.tab1 = [["     " , "     "  , "     " ], ["     " , "     "  , "     " ],["     " , "     "  , "     " ]]
            Tabuleiro.tab2 = [["     " , "     "  , "     " ], ["     " , "     "  , "     " ],["     " , "     "  , "     " ]]
            Jogada.PecaSelect = int(0)
            Jogada.Peca1Blue = int(2) 
            Jogada.Peca2Blue = int(2) 
            Jogada.Peca3Blue = int(2) 
            Jogada.Peca1Red = int(2) 
            Jogada.Peca2Red = int(2) 
            Jogada.Peca3Red = int(2)
            os.system('cls')
            print(f'  Vitorias {player1}: {VitoriaP1}')
            print(f'  Vitorias {player2}: {VitoriaP2}')
            Tabuleiro.tabuleiro()
        else:
            if(cont % 2 == 0): VitoriaP2 = VitoriaP2 + 1
            else: VitoriaP1 = VitoriaP1 + 1
            print()
            print()
            print(f'  Vitorias: {player1} -> {VitoriaP1}')
            print(f'  Vitorias: {player2} -> {VitoriaP2}')
            print()
            print("                         !Obrigado por jogar!")
            print()
            print("-=" *34)
            teste = input()

