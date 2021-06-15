
from pickle import FALSE, TRUE
from colorama import Fore
import Tabuleiro 
import FimJogo 
import Jogada
import os

os.system('cls')
print()

print( "        =" + "-=" *34)
print( "         " + Fore.YELLOW + "                       JOGO DA VELHA 2.0" + Fore.RESET )
print( "        =" + "-=" *34)

print()

print(Fore.YELLOW + """       Assim como no jogo da velha o seu objetivo é ser o primeiro a alinhar três 
    peças para vencer, seja na diagonal ou na octogonal. A diferença é que cada 
    jogador recebe seis peças, sendo: duas peças de tamanho 1 (Peça1), duas 
    peças de tamanho 2 (Peça2) e duas peças de tamanho 3 (Peça3). Em seu 
    turno o jogador pode posicionar uma peça em um local vazio ou em um local 
    com uma peça menor que a selecionada para jogar, sendo a peça do 
    adversário ou não, sobrepondo essa peça. Também pode deslocar uma peça 
    sua que já esteja posicionada no tabuleiro, para uma posição vazia ou para a 
    posição de uma peça eu possa sobrepor. Lembrando, as peças sobrepostas 
    ainda continuam no jogo, ou seja, caso a peça que sobrepôs seja movida, a 
    peça sobreposta assume esta posição.""" + Fore.RESET)

print()
print("-=" *34)
print()
#solicita o nome de um jogador
player1 = input("  Informe o nome do Jogador 1: ")
print("-=" *34)
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
jogo = FALSE
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

