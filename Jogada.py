#Classe responsavel por realizar todas as funcoes referentes as jogadas do usuario
from pickle import FALSE, TRUE
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

#responsavel por solicitar a jogada aos usuarios e chamar a funcao ValidarJogada
def jogada(cont, player1, player2):
    global PecaSelect
    global trava
    teste = FALSE
    cont = int(cont)
    while(teste == FALSE):
        print()
        if(cont % 2 == 0):
            print('  Quem joga é: ' + player1)
            print('  A quantidade de peças disponiveis é: ' + Fore.BLUE + 'Peça1 ' + Fore.RESET + f'{Peca1Blue}, ' + Fore.BLUE + 'Peça2 ' + Fore.RESET + f'{Peca2Blue} e ' + Fore.BLUE + 'Peça3 ' + Fore.RESET + f'{Peca3Blue}')
        else:
            print('  Quem joga é: ' + player2)
            print('  A quantidade de peças disponiveis é: ' + Fore.RED + 'Peça1 ' + Fore.RESET + f'{Peca1Red}, ' + Fore.RED + 'Peça2 ' + Fore.RESET + f'{Peca2Red} e ' + Fore.RED + 'Peça3 ' + Fore.RESET + f'{Peca3Red}')

        print()
        l = input('  Informe a linha que deseja jogar ou da peça que deseja mover: ')
    
        c = input('  Informe a coluna que deseja jogar ou da peça que deseja mover: ')

        teste = ValidarJogada(l, c, cont)

    l = int(l)
    c = int(c)

    #a trava funciona para impedir uma nova jogada, em xaso do usuario querer apenas movimentar uma peca no tabuleiro e nao inserir uma nova
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

    
    

#validaa se a jogada realizada e valida, para isso utliza as funcoes MovintarPeca e ValidarPeca
def ValidarJogada(l, c, cont):
    global trava
    try:
        l = int(l)
        c = int(c)
    except ValueError:
        os.system('cls')
        print()
        print(Fore.YELLOW +"  Posição invalida, informe um número inteiro para as posições!" + Fore.RESET)
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
        print()
        print(Fore.YELLOW + "  JOGADA INVÁLIDA, FAVOR REALIZAR UM MOVIMENTO VALIDO!" + Fore.RESET)
        Tabuleiro.tabuleiro()
        return FALSE   

#responsavel por vaidar qaulquer movimento de peca, seja esta peca nova ou não
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
            PecaSelect = input('  Selecione qual o tamanho da peça da jogada (1 - 2 - 3): ')
            try:
                PecaSelect = int(PecaSelect)
            except ValueError:
                os.system('cls')
                print()
                print(Fore.YELLOW +"  Peça invalida, favor refazer a jogada!" + Fore.RESET)
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
                        print()
                        print(Fore.YELLOW + "  Você não pode comer essa peça!" + Fore.RESET)
                        Tabuleiro.tabuleiro()
                        
                        if(PecaSelect == 1):
                            if(Peca1Blue > 0): Peca1Blue = Peca1Blue + 1
                        elif(PecaSelect == 2):
                            if(Peca2Blue > 0): Peca2Blue = Peca2Blue + 1
                        else:
                            if(Peca3Blue > 0): Peca3Blue = Peca3Blue + 1
                        
                        return FALSE
                else:
                    os.system('cls')
                    print()
                    print(Fore.YELLOW +"  Peça Selecionada já acabou, favor refazer a jogada!" + Fore.RESET)
                    Tabuleiro.tabuleiro()
                    
                    if(PecaSelect == 1):
                        if(Peca1Blue > 0): Peca1Blue = Peca1Blue + 1
                    elif(PecaSelect == 2):
                        if(Peca2Blue > 0): Peca2Blue = Peca2Blue + 1
                    else:
                        if(Peca3Blue > 0): Peca3Blue = Peca3Blue + 1
                    
                    return FALSE
            else:
                os.system('cls')
                print()
                print(Fore.YELLOW +"  Peça invalida, favor refazer a jogada!" + Fore.RESET)
                Tabuleiro.tabuleiro()
                return FALSE 
    else:
        if((Tabuleiro.tab[l][c] == Pecas.PecaBlue0) or (Tabuleiro.tab[l][c] == Pecas.PecaBlue1) or (Tabuleiro.tab[l][c] == Pecas.PecaBlue2)):
            PecaSelect = input('  Selecione qual o tamanho da peça da jogada (1 - 2 - 3): ')
            try:
                PecaSelect = int(PecaSelect)
            except ValueError:
                os.system('cls')
                print()
                print(Fore.YELLOW +"  Peça invalida, favor refazer a jogada!" + Fore.RESET)
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
                        print()
                        print(Fore.YELLOW +"  Você não pode comer essa peça!" + Fore.RESET)
                        Tabuleiro.tabuleiro()
                        
                        if(PecaSelect == 1):
                            if(Peca1Red > 0): Peca1Red = Peca1Red + 1
                        elif(PecaSelect == 2):
                            if(Peca2Red > 0): Peca2Red = Peca2Red + 1
                        else:
                            if(Peca3Red > 0): Peca3Red = Peca3Red + 1
                        
                        return FALSE
                else:
                    os.system('cls')
                    print()
                    print(Fore.YELLOW +"  Peça Selecionada já acabou, favor refazer a jogada!" + Fore.RESET)
                    Tabuleiro.tabuleiro()
                    
                    if(PecaSelect == 1):
                        if(Peca1Red > 0): Peca1Red = Peca1Red + 1
                    elif(PecaSelect == 2):
                        if(Peca2Red > 0): Peca2Red = Peca2Red + 1
                    else:
                        if(Peca3Red > 0): Peca3Red = Peca3Red + 1
                    
                    return FALSE
    l1 = input('  Informe a linha da nova posição da peça:')
    c1 = input('  Informe a coluna da nova posição da peça: ')
    try:
        l1 = int(l1)
        c1 = int(c1)
    except ValueError:
        os.system('cls')
        print()
        print(Fore.YELLOW +"  Posição invalida, informe um número inteiro para as posições!" + Fore.RESET)
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
                print()
                print(Fore.YELLOW +"  JOGADA INVÁLIDA, VOCÊ NÃO PODE COMER ESTA PEÇA!" + Fore.RESET)
                Tabuleiro.tabuleiro()
                return FALSE
    else:
        os.system('cls')
        print()
        print(Fore.YELLOW + "  JOGADA INVÁLIDA, FAVOR REALIZAR UM MOVIMENTO VALIDO!" + Fore.RESET)
        Tabuleiro.tabuleiro()
        return FALSE   
        
#responsavel por validar as pecas, ou seja, verifica se o valor inserido corresponde a uma peca ainda disponivel
def ValidarPeca(cont):
    global PecaSelect
    global Peca1Blue
    global Peca2Blue
    global Peca3Blue
    global Peca1Red
    global Peca2Red
    global Peca3Red
    PecaSelect = input('  Selecione qual o tamanho da peça da jogada (1 - 2 - 3): ')
    try:
        PecaSelect = int(PecaSelect)
    except ValueError:
        os.system('cls')
        print()
        print(Fore.YELLOW +"  Peça invalida, favor refazer a jogada!" + Fore.RESET)
        Tabuleiro.tabuleiro()
        return FALSE
    if(PecaSelect > 0 and PecaSelect < 4):    
            if(cont % 2 == 0):
                teste = QuantPecasBlue()
                if(teste == TRUE):
                   return TRUE
                else:
                    os.system('cls')
                    print()
                    print(Fore.YELLOW +"  Peça Selecionada já acabou, favor refazer a jogada!" + Fore.RESET)
                    Tabuleiro.tabuleiro()
                    
                    if(PecaSelect == 1):
                        if(Peca1Blue > 0): Peca1Blue = Peca1Blue + 1
                    elif(PecaSelect == 2):
                        if(Peca2Blue > 0): Peca2Blue = Peca2Blue + 1
                    else:
                        if(Peca3Blue > 0): Peca3Blue = Peca3Blue + 1
                    
                    return FALSE
            else:
                teste = QuantPecasRed()
                if(teste == TRUE):
                   return TRUE
                else:
                    os.system('cls')
                    print()
                    print(Fore.YELLOW +"  Peça Selecionada já acabou, favor refazer a jogada!" + Fore.RESET)
                    Tabuleiro.tabuleiro()
                    
                    if(PecaSelect == 1):
                        if(Peca1Red > 0): Peca1Red = Peca1Red + 1
                    elif(PecaSelect == 2):
                        if(Peca2Red > 0): Peca2Red = Peca2Red + 1
                    else:
                        if(Peca3Red > 0): Peca3Red = Peca3Red + 1
                    
                    return FALSE
    else:
        os.system('cls')
        print()
        print(Fore.YELLOW +"  Peça invalida, favor refazer a jogada!" + Fore.RESET)
        Tabuleiro.tabuleiro()
        return FALSE

#responsavel por armarzenar a quantidade pecas azuis disponiveis
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
#responsavel por armarzenar a quantidade pecas veremlhas disponiveis
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




