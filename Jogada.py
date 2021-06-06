#Módulo responsável por realizar e validar as jogadas do jogo
from pickle import FALSE, PUT, TRUE
import re
import Tabuleiro
import Pecas
import os
from colorama import Fore

l = int(0)
c = int(0)
PecaSelect = int(0)
Peca1Blue = int(2) 
Peca2Blue = int(2) 
Peca3Blue = int(2) 
Peca1Red = int(2) 
Peca2Red = int(2) 
Peca3Red = int(2) 
trava = FALSE

#realiza as jogadas de cada jogador
def jogada(cont, player1, player2):
    global PecaSelect
    global trava
    teste = FALSE
    cont = int(cont)
    while(teste == FALSE):
        if(cont % 2 == 0):
            print('Quem joga é: ' + player1)
            print(f'A quantidade de peças disponiveis é: Peça 1 {Peca1Blue}, Peça 2 {Peca2Blue} e Peça 3 {Peca3Blue}')
        else:
            print('Quem joga é: ' + player2)
            print(f'A quantidade de peças disponiveis é: Peça 1 {Peca1Red}, Peça 2 {Peca2Red} e Peça 3 {Peca3Red}')
        
        l = input('Informe a linha que deseja jogar ou da peça que deseja mover: ')
    
        c = input('Informe a coluna que deseja jogar ou da peça que deseja mover: ')

        teste = ValidarJogada(l, c, cont)

    l = int(l)
    c = int(c)
    if(trava == FALSE):
        trava = FALSE
        if(cont % 2 ==0):
            if(PecaSelect == 1):
                Tabuleiro.tab[l][c] = Pecas.PecaBlue0
            elif(PecaSelect == 2):
                Tabuleiro.tab[l][c] = Pecas.PecaBlue1
            else:
                Tabuleiro.tab[l][c] = Pecas.PecaBlue2
        else:
            if(PecaSelect == 1):
                Tabuleiro.tab[l][c] = Pecas.PecaRed0
            elif(PecaSelect == 2):
                Tabuleiro.tab[l][c] = Pecas.PecaRed1
            else:
                Tabuleiro.tab[l][c] = Pecas.PecaRed2

    
    

#validaa a jogada realiza anteriormente
def ValidarJogada(l, c, cont):
    global trava
    try:
        l = int(l)
        c = int(c)
    except ValueError:
        os.system('cls')
        print(Fore.YELLOW +"Posição invalida, informe um número inteiro para as posições!" + Fore.RESET)
        Tabuleiro.tabuleiro()
        return FALSE
    cont = int(cont) 
    if(l >= 0 and l <= 2 ) and (c >= 0 and c <= 2):
        if(Tabuleiro.tab[l][c] == "     "):
            trava = FALSE
            return ValidarPeca(cont)
        else:
            return MovimentarPeca(l, c, cont)
    else:
        os.system('cls')
        print(Fore.YELLOW + "JOGADA INVÁLIDA, FAVOR REALIZAR UM MOVIMENTO VALIDO!" + Fore.RESET)
        Tabuleiro.tabuleiro()
        return FALSE   

def MovimentarPeca(l, c, cont):
    i = int(cont)
    global trava
    global PecaSelect
    global Peca1Blue
    global Peca2Blue
    global Peca3Blue
    global Peca1Red
    global Peca2Red
    global Peca3Red
    if(i % 2 == 0):
        if((Tabuleiro.tab[l][c] == Pecas.PecaRed0) or (Tabuleiro.tab[l][c] == Pecas.PecaRed1) or (Tabuleiro.tab[l][c] == Pecas.PecaRed2)):
            PecaSelect = input('Selecione qual o tamanho da peça da jogada (1 - 2 - 3): ')
            try:
                PecaSelect = int(PecaSelect)
            except ValueError:
                os.system('cls')
                print(Fore.YELLOW +"Peça invalida, favor refazer a jogada!" + Fore.RESET)
                Tabuleiro.tabuleiro()
                return FALSE

            if(PecaSelect > 0 and PecaSelect < 4):    
                #teste de se ainda a peca selecionada esta disponivel para jogar
                teste = QuantPecasBlue()
                if(teste == TRUE):
                    if(Tabuleiro.tab[l][c] == Pecas.PecaRed0):
                        PecaAntiga = int(1)
                    elif(Tabuleiro.tab[l][c] == Pecas.PecaRed1):
                        PecaAntiga = int(2)
                    else:
                        PecaAntiga = int(3)
                    if(PecaSelect > PecaAntiga):
                        aux = Tabuleiro.tab[l][c]
                        if(PecaSelect == 1):
                            Tabuleiro.tab[l][c] = Pecas.PecaBlue0
                        elif(PecaSelect == 2):
                            Tabuleiro.tab[l][c] = Pecas.PecaBlue1
                        else:
                            Tabuleiro.tab[l][c] = Pecas.PecaBlue2
                        #passar a peca comida para o outro tabuleiro
                        if(Tabuleiro.tab1[l][c] == "     "):
                            Tabuleiro.tab1[l][c] = aux
                        else:
                            Tabuleiro.tab2[l][c] = Tabuleiro.tab1[l][c]
                            Tabuleiro.tab1[l][c] = aux
                        return TRUE
                    else:
                        os.system('cls')
                        print(Fore.YELLOW + "Você não pode comer essa peça!" + Fore.RESET)
                        print('Entrei aqui')
                        Tabuleiro.tabuleiro()
                        if(PecaSelect == 1):
                            Peca1Blue = Peca1Blue + 1
                        elif(PecaSelect == 2):
                            Peca2Blue = Peca2Blue + 1
                        else:
                            Peca3Blue = Peca3Blue + 1
                        return FALSE
                else:
                    os.system('cls')
                    print(Fore.YELLOW +"Peça Selecionada já acabou, favor refazer a jogada!" + Fore.RESET)
                    Tabuleiro.tabuleiro()
                    if(PecaSelect == 1):
                        Peca1Blue = Peca1Blue + 1
                    elif(PecaSelect == 2):
                        Peca2Blue = Peca2Blue + 1
                    else:
                        Peca3Blue = Peca3Blue + 1
                    return FALSE
            else:
                os.system('cls')
                print(Fore.YELLOW +"Peça invalida, favor refazer a jogada!" + Fore.RESET)
                Tabuleiro.tabuleiro()
                return FALSE 
    else:
        if((Tabuleiro.tab[l][c] == Pecas.PecaBlue0) or (Tabuleiro.tab[l][c] == Pecas.PecaBlue1) or (Tabuleiro.tab[l][c] == Pecas.PecaBlue2)):
            PecaSelect = input('Selecione qual o tamanho da peça da jogada (1 - 2 - 3): ')
            try:
                PecaSelect = int(PecaSelect)
            except ValueError:
                os.system('cls')
                print(Fore.YELLOW +"Peça invalida, favor refazer a jogada!" + Fore.RESET)
                Tabuleiro.tabuleiro()
                return FALSE
            if(PecaSelect > 0 and PecaSelect < 4):    
                #teste de se ainda a peca selecionada esta disponivel para jogar
                teste = QuantPecasRed()
                if(teste == TRUE):
                    if(Tabuleiro.tab[l][c] == Pecas.PecaBlue0):
                        PecaAntiga = int(1)
                    elif(Tabuleiro.tab[l][c] == Pecas.PecaBlue1):
                        PecaAntiga = int(2)
                    else:
                        PecaAntiga = int(3)
                    if(PecaSelect > PecaAntiga):
                        aux = Tabuleiro.tab[l][c]
                        if(PecaSelect == 1):
                            Tabuleiro.tab[l][c] = Pecas.PecaRed0
                        elif(PecaSelect == 2):
                            Tabuleiro.tab[l][c] = Pecas.PecaRed1
                        else:
                            Tabuleiro.tab[l][c] = Pecas.PecaRed2
                        #passar a peca comida para o outro tabuleiro
                        if(Tabuleiro.tab1[l][c] == "     "):
                            Tabuleiro.tab1[l][c] = aux
                        else:
                            Tabuleiro.tab2[l][c] = Tabuleiro.tab1[l][c]
                            Tabuleiro.tab1[l][c] = aux
                        return TRUE
                    else:
                        os.system('cls')
                        print(Fore.YELLOW +"Você não pode comer essa peça!" + Fore.RESET)
                        print('Entrei aqui')
                        Tabuleiro.tabuleiro()
                        if(PecaSelect == 1):
                            Peca1Red = Peca1Red + 1
                        elif(PecaSelect == 2):
                            Peca2Red = Peca2Red + 1
                        else:
                            Peca3Red = Peca3Red + 1
                        return FALSE
                else:
                    os.system('cls')
                    print(Fore.YELLOW +"Peça Selecionada já acabou, favor refazer a jogada!" + Fore.RESET)
                    Tabuleiro.tabuleiro()
                    if(PecaSelect == 1):
                        Peca1Red = Peca1Red + 1
                    elif(PecaSelect == 2):
                        Peca2Red = Peca2Red + 1
                    else:
                        Peca3Red = Peca3Red + 1
                    return FALSE
    l1 = input('Informe a linha da nova posição da peça:')
    c1 = input('Informe a coluna da nova posição da peça: ')
    try:
        l1 = int(l1)
        c1 = int(c1)
    except ValueError:
        os.system('cls')
        print(Fore.YELLOW +"Posição invalida, informe um número inteiro para as posições!" + Fore.RESET)
        Tabuleiro.tabuleiro()
        return FALSE
    if((l1 >= 0 and l1 <= 2) and (c1 >= 0 and c1 <= 2)):

        if(Tabuleiro.tab[l1][c1] == "     "):
            Tabuleiro.tab[l1][c1] = Tabuleiro.tab[l][c]
            if(Tabuleiro.tab1[l][c] != "     "):
                Tabuleiro.tab[l][c] = Tabuleiro.tab1[l][c]
                if(Tabuleiro.tab2[l][c] != "     "):
                    Tabuleiro.tab1[l][c] = Tabuleiro.tab2[l][c]
                    Tabuleiro.tab2[l][c] = "     "
                else:
                    Tabuleiro.tab1[l][c] = "     "
            else:
                Tabuleiro.tab[l][c] = "     "

            trava = TRUE
            return TRUE
        else:
            if((Tabuleiro.tab[l][c] == Pecas.PecaBlue0) or (Tabuleiro.tab[l][c] == Pecas.PecaRed0)):
                PecaAntiga = 1
            elif((Tabuleiro.tab[l][c] == Pecas.PecaBlue1) or (Tabuleiro.tab[l][c] == Pecas.PecaRed1)):
                PecaAntiga = 2
            else:
                PecaAntiga = 3
            
            if((Tabuleiro.tab[l1][c1] == Pecas.PecaBlue0) or (Tabuleiro.tab[l1][c1] == Pecas.PecaRed0)):
                PecaNova = 1
            elif((Tabuleiro.tab[l1][c1] == Pecas.PecaBlue1) or (Tabuleiro.tab[l1][c1] == Pecas.PecaRed1)):
                PecaNova = 2
            else:
                PecaNova = 3
            
            if(PecaNova < PecaAntiga):
                aux = Tabuleiro.tab[l1][c1]
                Tabuleiro.tab[l1][c1] = Tabuleiro.tab[l][c]
                #passar a peca comida para o outro tabuleiro
                if(Tabuleiro.tab1[l1][c1] == "     "):
                    Tabuleiro.tab1[l1][c1] = aux
                else:
                    Tabuleiro.tab2[l1][c1] = Tabuleiro.tab1[l1][c1]
                    Tabuleiro.tab1[l1][c1] = aux
                #passar a peca do outro tabuleiro para o principal
                if(Tabuleiro.tab1[l][c] != "     "):
                    Tabuleiro.tab[l][c] = Tabuleiro.tab1[l][c]
                    if(Tabuleiro.tab2[l][c] != "     "):
                        Tabuleiro.tab1[l][c] = Tabuleiro.tab2[l][c]
                        Tabuleiro.tab2 = "     "
                    else:
                        Tabuleiro.tab1[l][c] = "     "
                else:
                    Tabuleiro.tab[l][c] = "     "
                
                trava = TRUE
                return TRUE
            else:
                os.system('cls')
                print(Fore.YELLOW +"JOGADA INVÁLIDA, VOCÊ NÃO PODE COMER ESTA PEÇA!" + Fore.RESET)
                Tabuleiro.tabuleiro()
                return FALSE
    else:
        os.system('cls')
        print(Fore.YELLOW + "JOGADA INVÁLIDA, FAVOR REALIZAR UM MOVIMENTO VALIDO!" + Fore.RESET)
        Tabuleiro.tabuleiro()
        return FALSE   
        

def ValidarPeca(cont):
    global PecaSelect
    global Peca1Blue
    global Peca2Blue
    global Peca3Blue
    global Peca1Red
    global Peca2Red
    global Peca3Red
    PecaSelect = input('Selecione qual o tamanho da peça da jogada (1 - 2 - 3): ')
    try:
        PecaSelect = int(PecaSelect)
    except ValueError:
        os.system('cls')
        print(Fore.YELLOW +"Peça invalida, favor refazer a jogada!" + Fore.RESET)
        Tabuleiro.tabuleiro()
        return FALSE
    if(PecaSelect > 0 and PecaSelect < 4):    
            if(cont % 2 == 0):
                teste = QuantPecasBlue()
                if(teste == TRUE):
                   return TRUE
                else:
                    os.system('cls')
                    print(Fore.YELLOW +"Peça Selecionada já acabou, favor refazer a jogada!" + Fore.RESET)
                    Tabuleiro.tabuleiro()
                    if(PecaSelect == 1):
                        Peca1Blue = Peca1Blue + 1
                    elif(PecaSelect == 2):
                        Peca2Blue = Peca2Blue + 1
                    else:
                        Peca3Blue = Peca3Blue + 1
                    return FALSE
            else:
                teste = QuantPecasRed()
                if(teste == TRUE):
                   return TRUE
                else:
                    os.system('cls')
                    print(Fore.YELLOW +"Peça Selecionada já acabou, favor refazer a jogada!" + Fore.RESET)
                    Tabuleiro.tabuleiro()
                    if(PecaSelect == 1):
                        Peca1Red = Peca1Red + 1
                    elif(PecaSelect == 2):
                        Peca2Red = Peca2Red + 1
                    else:
                        Peca3Red = Peca3Red + 1
                    return FALSE
    else:
        os.system('cls')
        print(Fore.YELLOW +"Peça invalida, favor refazer a jogada!" + Fore.RESET)
        Tabuleiro.tabuleiro()
        return FALSE

def QuantPecasBlue():
    global PecaSelect
    global Peca1Blue
    global Peca2Blue
    global Peca3Blue
    if(PecaSelect == 1):
        if(Peca1Blue != 0):
            Peca1Blue = Peca1Blue - 1
            return TRUE
        else:
            
            return FALSE
    elif(PecaSelect == 2):
        if(Peca2Blue != 0):
            Peca2Blue = Peca2Blue - 1
            return TRUE
        else:
            
            return FALSE
    else:
        if(Peca3Blue != 0):
            Peca3Blue = Peca3Blue - 1
            return TRUE
        else:
            
            return FALSE

def QuantPecasRed():
    global PecaSelect
    global Peca1Red
    global Peca2Red
    global Peca3Red
    if(PecaSelect == 1):
        if(Peca1Red != 0):
            Peca1Red = Peca1Red - 1
            return TRUE
        else:
            
            return FALSE
    elif(PecaSelect == 2):
        if(Peca2Red != 0):
            Peca2Red = Peca2Red - 1
            return TRUE
        else:

            return FALSE
    else:
        if(Peca3Red != 0):
            Peca3Red = Peca3Red - 1
            return TRUE
        else:
            
            return FALSE




