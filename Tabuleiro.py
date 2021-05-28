#Módulo responsável por gerar o tabuleiro do jogo
tab = [['     ' , '     '  , '     ' ], ['     ' , '     '  ,'     ' ],['     ' , '     '  ,'     ' ]]

def tabuleiro():
    print("-=" *30)
    print("       0           1           2  ")
    print("             ||         ||       ")
    print(f'0    {tab[0][0]}   ||  {tab[0][1]}  ||   {tab[0][2]}')
    print("             ||         ||       ")
    print("   =" *9)
    print("             ||         ||       ")
    print(f'1    {tab[1][0]}   ||  {tab[1][1]}  ||   {tab[1][2]}')
    print("             ||         ||       ")
    print("   =" *9)
    print("             ||         ||       ")
    print(f'2    {tab[2][0]}   ||  {tab[2][1]}  ||   {tab[2][2]}')
    print("             ||         ||       ")
    print()
    print('-=' *30)
    








