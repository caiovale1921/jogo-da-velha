
#Módulo resposável por validar o fim de jogo

from pickle import FALSE, TRUE
import Tabuleiro
import Pecas

def ValidarJogo(cont, player1, player2):
    
    if(cont > 4):
        testeAzuis = ValidarPecaAzuis()
        testeVermelhas = ValidarPecaVermelhas()
        if(testeAzuis == TRUE) or (testeVermelhas == TRUE):
            print('-=' *30)
            if((cont - 1) % 2 == 0):
                print('Quem ganhou foi: ' + player1)
            else:
                print('Quem ganhou foi: '+ player2)
            return TRUE
        else:
            return FALSE
    else:
        return FALSE


#Modulo para testar a peca que esta na posicao

def ValidarPecaVermelhas():
    #verificacao de linhas
    if((Tabuleiro.tab[0][0] == Pecas.PecaRed0 or
     Tabuleiro.tab[0][0] == Pecas.PecaRed1 or
     Tabuleiro.tab[0][0] == Pecas.PecaRed2) and
     (Tabuleiro.tab[0][1] == Pecas.PecaRed0 or
     Tabuleiro.tab[0][1] == Pecas.PecaRed1 or
     Tabuleiro.tab[0][1] == Pecas.PecaRed2) and
     (Tabuleiro.tab[0][2] == Pecas.PecaRed0 or
     Tabuleiro.tab[0][2] == Pecas.PecaRed1 or
     Tabuleiro.tab[0][2] == Pecas.PecaRed2)):
        return TRUE
    elif((Tabuleiro.tab[1][0] == Pecas.PecaRed0 or
     Tabuleiro.tab[1][0] == Pecas.PecaRed1 or
     Tabuleiro.tab[1][0] == Pecas.PecaRed2) and
     (Tabuleiro.tab[1][1] == Pecas.PecaRed0 or
     Tabuleiro.tab[1][1] == Pecas.PecaRed1 or
     Tabuleiro.tab[1][1] == Pecas.PecaRed2) and
     (Tabuleiro.tab[1][2] == Pecas.PecaRed0 or
     Tabuleiro.tab[1][2] == Pecas.PecaRed1 or
     Tabuleiro.tab[1][2] == Pecas.PecaRed2)):
        return TRUE
    elif((Tabuleiro.tab[2][0] == Pecas.PecaRed0 or
     Tabuleiro.tab[2][0] == Pecas.PecaRed1 or
     Tabuleiro.tab[2][0] == Pecas.PecaRed2) and
     (Tabuleiro.tab[2][1] == Pecas.PecaRed0 or
     Tabuleiro.tab[2][1] == Pecas.PecaRed1 or
     Tabuleiro.tab[2][1] == Pecas.PecaRed2) and
     (Tabuleiro.tab[2][2] == Pecas.PecaRed0 or
     Tabuleiro.tab[2][2] == Pecas.PecaRed1 or
     Tabuleiro.tab[2][2] == Pecas.PecaRed2)):
        return TRUE
    
#verificacao de colunas
    elif((Tabuleiro.tab[0][0] == Pecas.PecaRed0 or
     Tabuleiro.tab[0][0] == Pecas.PecaRed1 or
     Tabuleiro.tab[0][0] == Pecas.PecaRed2) and
     (Tabuleiro.tab[1][0] == Pecas.PecaRed0 or
     Tabuleiro.tab[1][0] == Pecas.PecaRed1 or
     Tabuleiro.tab[1][0] == Pecas.PecaRed2) and
     (Tabuleiro.tab[2][0] == Pecas.PecaRed0 or
     Tabuleiro.tab[2][0] == Pecas.PecaRed1 or
     Tabuleiro.tab[2][0] == Pecas.PecaRed2)):
        return TRUE
    elif((Tabuleiro.tab[0][1] == Pecas.PecaRed0 or
     Tabuleiro.tab[0][1] == Pecas.PecaRed1 or
     Tabuleiro.tab[0][1] == Pecas.PecaRed2) and
     (Tabuleiro.tab[1][1] == Pecas.PecaRed0 or
     Tabuleiro.tab[1][1] == Pecas.PecaRed1 or
     Tabuleiro.tab[1][1] == Pecas.PecaRed2) and
     (Tabuleiro.tab[2][1] == Pecas.PecaRed0 or
     Tabuleiro.tab[2][1] == Pecas.PecaRed1 or
     Tabuleiro.tab[2][1] == Pecas.PecaRed2)):
        return TRUE
    elif((Tabuleiro.tab[0][2] == Pecas.PecaRed0 or
     Tabuleiro.tab[0][2] == Pecas.PecaRed1 or
     Tabuleiro.tab[0][2] == Pecas.PecaRed2) and
     (Tabuleiro.tab[1][2] == Pecas.PecaRed0 or
     Tabuleiro.tab[1][2] == Pecas.PecaRed1 or
     Tabuleiro.tab[1][2] == Pecas.PecaRed2) and
     (Tabuleiro.tab[2][2] == Pecas.PecaRed0 or
     Tabuleiro.tab[2][2] == Pecas.PecaRed1 or
     Tabuleiro.tab[2][2] == Pecas.PecaRed2)):
        return TRUE
    
#verificacao de diagonais
    elif((Tabuleiro.tab[0][0] == Pecas.PecaRed0 or
     Tabuleiro.tab[0][0] == Pecas.PecaRed1 or
     Tabuleiro.tab[0][0] == Pecas.PecaRed2) and
     (Tabuleiro.tab[1][1] == Pecas.PecaRed0 or
     Tabuleiro.tab[1][1] == Pecas.PecaRed1 or
     Tabuleiro.tab[1][1] == Pecas.PecaRed2) and
     (Tabuleiro.tab[2][2] == Pecas.PecaRed0 or
     Tabuleiro.tab[2][2] == Pecas.PecaRed1 or
     Tabuleiro.tab[2][2] == Pecas.PecaRed2)):
        return TRUE
    elif((Tabuleiro.tab[0][2] == Pecas.PecaRed0 or
     Tabuleiro.tab[0][2] == Pecas.PecaRed1 or
     Tabuleiro.tab[0][2] == Pecas.PecaRed2) and
     (Tabuleiro.tab[1][1] == Pecas.PecaRed0 or
     Tabuleiro.tab[1][1] == Pecas.PecaRed1 or
     Tabuleiro.tab[1][1] == Pecas.PecaRed2) and
     (Tabuleiro.tab[2][0] == Pecas.PecaRed0 or
     Tabuleiro.tab[2][0] == Pecas.PecaRed1 or
     Tabuleiro.tab[2][0] == Pecas.PecaRed2)):
        return TRUE
    else:
        return FALSE

def ValidarPecaAzuis():
    #verificacao de linhas
    if((Tabuleiro.tab[0][0] == Pecas.PecaBlue0 or
     Tabuleiro.tab[0][0] == Pecas.PecaBlue1 or
     Tabuleiro.tab[0][0] == Pecas.PecaBlue2) and
     (Tabuleiro.tab[0][1] == Pecas.PecaBlue0 or
     Tabuleiro.tab[0][1] == Pecas.PecaBlue1 or
     Tabuleiro.tab[0][1] == Pecas.PecaBlue2) and
     (Tabuleiro.tab[0][2] == Pecas.PecaBlue0 or
     Tabuleiro.tab[0][2] == Pecas.PecaBlue1 or
     Tabuleiro.tab[0][2] == Pecas.PecaBlue2)):
        return TRUE
    elif((Tabuleiro.tab[1][0] == Pecas.PecaBlue0 or
     Tabuleiro.tab[1][0] == Pecas.PecaBlue1 or
     Tabuleiro.tab[1][0] == Pecas.PecaBlue2) and
     (Tabuleiro.tab[1][1] == Pecas.PecaBlue0 or
     Tabuleiro.tab[1][1] == Pecas.PecaBlue1 or
     Tabuleiro.tab[1][1] == Pecas.PecaBlue2) and
     (Tabuleiro.tab[1][2] == Pecas.PecaBlue0 or
     Tabuleiro.tab[1][2] == Pecas.PecaBlue1 or
     Tabuleiro.tab[1][2] == Pecas.PecaBlue2)):
        return TRUE
    elif((Tabuleiro.tab[2][0] == Pecas.PecaBlue0 or
     Tabuleiro.tab[2][0] == Pecas.PecaBlue1 or
     Tabuleiro.tab[2][0] == Pecas.PecaBlue2) and
     (Tabuleiro.tab[2][1] == Pecas.PecaBlue0 or
     Tabuleiro.tab[2][1] == Pecas.PecaBlue1 or
     Tabuleiro.tab[2][1] == Pecas.PecaBlue2) and
     (Tabuleiro.tab[2][2] == Pecas.PecaBlue0 or
     Tabuleiro.tab[2][2] == Pecas.PecaBlue1 or
     Tabuleiro.tab[2][2] == Pecas.PecaBlue2)):
        return TRUE
    
#verificacao de colunas
    elif((Tabuleiro.tab[0][0] == Pecas.PecaBlue0 or
     Tabuleiro.tab[0][0] == Pecas.PecaBlue1 or
     Tabuleiro.tab[0][0] == Pecas.PecaBlue2) and
     (Tabuleiro.tab[1][0] == Pecas.PecaBlue0 or
     Tabuleiro.tab[1][0] == Pecas.PecaBlue1 or
     Tabuleiro.tab[1][0] == Pecas.PecaBlue2) and
     (Tabuleiro.tab[2][0] == Pecas.PecaBlue0 or
     Tabuleiro.tab[2][0] == Pecas.PecaBlue1 or
     Tabuleiro.tab[2][0] == Pecas.PecaBlue2)):
        return TRUE
    elif((Tabuleiro.tab[0][1] == Pecas.PecaBlue0 or
     Tabuleiro.tab[0][1] == Pecas.PecaBlue1 or
     Tabuleiro.tab[0][1] == Pecas.PecaBlue2) and
     (Tabuleiro.tab[1][1] == Pecas.PecaBlue0 or
     Tabuleiro.tab[1][1] == Pecas.PecaBlue1 or
     Tabuleiro.tab[1][1] == Pecas.PecaBlue2) and
     (Tabuleiro.tab[2][1] == Pecas.PecaBlue0 or
     Tabuleiro.tab[2][1] == Pecas.PecaBlue1 or
     Tabuleiro.tab[2][1] == Pecas.PecaBlue2)):
        return TRUE
    elif((Tabuleiro.tab[0][2] == Pecas.PecaBlue0 or
     Tabuleiro.tab[0][2] == Pecas.PecaBlue1 or
     Tabuleiro.tab[0][2] == Pecas.PecaBlue2) and
     (Tabuleiro.tab[1][2] == Pecas.PecaBlue0 or
     Tabuleiro.tab[1][2] == Pecas.PecaBlue1 or
     Tabuleiro.tab[1][2] == Pecas.PecaBlue2) and
     (Tabuleiro.tab[2][2] == Pecas.PecaBlue0 or
     Tabuleiro.tab[2][2] == Pecas.PecaBlue1 or
     Tabuleiro.tab[2][2] == Pecas.PecaBlue2)):
        return TRUE
    
#verificacao de diagonais
    elif((Tabuleiro.tab[0][0] == Pecas.PecaBlue0 or
     Tabuleiro.tab[0][0] == Pecas.PecaBlue1 or
     Tabuleiro.tab[0][0] == Pecas.PecaBlue2) and
     (Tabuleiro.tab[1][1] == Pecas.PecaBlue0 or
     Tabuleiro.tab[1][1] == Pecas.PecaBlue1 or
     Tabuleiro.tab[1][1] == Pecas.PecaBlue2) and
     (Tabuleiro.tab[2][2] == Pecas.PecaBlue0 or
     Tabuleiro.tab[2][2] == Pecas.PecaBlue1 or
     Tabuleiro.tab[2][2] == Pecas.PecaBlue2)):
        return TRUE
    elif((Tabuleiro.tab[0][2] == Pecas.PecaBlue0 or
     Tabuleiro.tab[0][2] == Pecas.PecaBlue1 or
     Tabuleiro.tab[0][2] == Pecas.PecaBlue2) and
     (Tabuleiro.tab[1][1] == Pecas.PecaBlue0 or
     Tabuleiro.tab[1][1] == Pecas.PecaBlue1 or
     Tabuleiro.tab[1][1] == Pecas.PecaBlue2) and
     (Tabuleiro.tab[2][0] == Pecas.PecaBlue0 or
     Tabuleiro.tab[2][0] == Pecas.PecaBlue1 or
     Tabuleiro.tab[2][0] == Pecas.PecaBlue2)):
        return TRUE
    else:
        return FALSE