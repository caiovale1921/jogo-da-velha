#Classe responsavel por gerar os tabuleiros dos jogos
from colorama import Fore

#tabuleiro principal, que e utlizado para verificar o fim de jogo e que aparece para os usuarios
tab = [["     " , "     "  , "     " ], ["     " , "     "  , "     " ],["     " , "     "  , "     " ]]

#tabuleiro responsavel por guardar as pecas comidas uma vez durante o jogo, tabuleiro auxiliar
tab1 = [["     " , "     "  , "     " ], ["     " , "     "  , "     " ],["     " , "     "  , "     " ]]

#tabuleiro responsavel por guardar as pecas comidas duas vezes durante o jogo, tabuleiro auxiliar
tab2 = [["     " , "     "  , "     " ], ["     " , "     "  , "     " ],["     " , "     "  , "     " ]]

#funcao responsavel por imprimir o tabuleiro principal na tela
def tabuleiro():
    print()
    print("-=" *34)
    print()
    print(Fore.YELLOW +"                        0           1           2  " + Fore.RESET)
    print("                              ||         ||       ")
    print(Fore.YELLOW + '                 0' + Fore.RESET + f'    {tab[0][0]}   ||  {tab[0][1]}  ||   {tab[0][2]}')
    print("                              ||         ||       ")
    print("                     " + "=" *31)
    print("                              ||         ||       ")
    print(Fore.YELLOW + '                 1' + Fore.RESET +f'    {tab[1][0]}   ||  {tab[1][1]}  ||   {tab[1][2]}')
    print("                              ||         ||       ")
    print("                     " + "=" *31)
    print("                              ||         ||       ")
    print(Fore.YELLOW + '                 2' + Fore.RESET + f'    {tab[2][0]}   ||  {tab[2][1]}  ||   {tab[2][2]}')
    print("                              ||         ||       ")
    print()
    print("-=" *34)
    








