from ast import For
from colorama import Fore
import Tabuleiro 
import FimJogo 
import Jogada
import os

player1 = input("Informe o nome do Jogador 1: ")
print("-=" *30)

player2 = input("Informe o nome do Jogador 2: ")
print("-=" *30)
os.system('cls')

player2 = (Fore.RED + f'{player2}' + Fore.RESET)
player1 = (Fore.BLUE + f'{player1}' + Fore.RESET)

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
    
