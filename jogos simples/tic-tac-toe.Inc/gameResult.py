# Tabuleiro de exemplo.
table = [["X",'X',"X"],
         [4,'X',6],
         ["O","O","X"]]

class CheckWin():
    """ 
    Verifica os casos nos quais 'X' ou 'O' vencem (ou empatam) no jogo da velha.
    """
    
    def __init__(self) -> None:
        pass

    def checkWin(self, table):      

        # COLUNAS
        if (table[0][0] == "X" and table[0][1] == "X" and table[0][2] == "X"):
            print('"X" Win! (linha superior)')
            quit()

        elif (table[1][0] == "X" and table[1][1] == "X" and table[1][2] == "X"):
            print('"X" Win! (linha do meio)')
            quit()
            
        elif (table[2][0] == "X" and table[2][1] == "X" and table[2][2] == "X"):
            print('"X" Win! (linha inferior)')
            quit()
            
        elif (table[0][0] == "O" and table[0][1] == "O" and table[0][2] == "O"):
            print('"O" Win! (linha superior)')
            quit()
            
        elif (table[1][0] == "O" and table[1][1] == "O" and table[1][2] == "O"):
            print('"O" Win! (linha do meio)')
            quit()
            
        elif (table[2][0] == "O" and table[2][1] == "O" and table[2][2] == "O"):
            print('"O" Win! (linha inferior)')
            quit()
            
        # LINHAS
        elif (table[0][0] == "X" and table[1][0] == "X" and table[2][0] == "X"):
            print('"X" Win! (1° COLUNA)')
            quit()
            
        elif (table[0][1] == "X" and table[1][1] == "X" and table[2][1] == "X"):
            print('"X" Win! (2° COLUNA)')
            quit()
            
        elif (table[0][2] == "X" and table[1][2] == "X" and table[2][2] == "X"):
            print('"X" Win! (3° COLUNA)')
            quit()
            
        elif (table[0][0] == "O" and table[1][0] == "O" and table[2][0] == "O"):
            print('"O" Win! (1° COLUNA)')
            quit()
            
        elif (table[0][1] == "O" and table[1][1] == "O" and table[2][1] == "O"):
            print('"X" Win! (2° COLUNA)')
            quit()
            
        elif (table[0][2] == "O" and table[1][2] == "O" and table[2][2] == "O"):
            print('"O" Win! (3° COLUNA)')
            quit()
            

        # DIAGONAIS 
        elif (table[0][0] == "X" and table[1][1] == "X" and table[2][2] == "X"):
            print('"X" Win! (diagonal principal)')
            quit()
            
        elif (table[0][2] == "X" and table[1][1] == "X" and table[2][0] == "X"):
            print('"X" Win! (diagonal secundária)')
            quit()
            
        elif (table[0][0] == "O" and table[1][1] == "O" and table[2][2] == "O"):
            print('"O" Win! (diagonal principal)')
            quit()
            
        elif (table[0][2] == "O" and table[1][1] == "O" and table[2][0] == "O"):
            print('"O" Win! (diagonal secundária)')
            quit()

        # REPRESENTANDO UM EMPATE
        lista = []

        for i in range(0, 3):
            for casa in table[i]:

                if casa == str(casa):
                    lista.append(str(i))
                
                if len(lista) == 9:
                    print("EMPATE!")
                    quit()
