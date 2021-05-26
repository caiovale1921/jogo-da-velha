#Módulo responsável por gerar o tabuleiro do jogo
tab = [[0 , 0 , 0], [0 , 0 , 0], [0 , 0 , 0]]

def tabuleiro():
    print("-=" *30)
    for l in range(0, 3):
        for c in range(0 ,3):
            print(f'[{tab[l][c] : ^5}]', end='')
        print()
    print('-=' *30)








