
table = [[1,2,3], 
         [4,5,6], 
         [7,8,9]]

class Indice():
    def __init__(self, x) -> None:
        self.x = x

    def get_index(self):
        """ Identifica o índice do número inputado na tabela. """
        try:
            for j in range(0, 3):
                if (table[0][j] == self.x) == True:
                    var = table[0]
                    posicao = table.index(var)
                    indice_posicao = var.index(self.x)
                    return(posicao, indice_posicao)

                elif (table[1][j] == self.x) == True:
                    var = table[1]
                    posicao = table.index(var)
                    indice_posicao = var.index(self.x)
                    return(posicao, indice_posicao)

                elif (table[2][j] == self.x) is True:
                    var = table[2]
                    posicao = table.index(var)
                    indice_posicao = var.index(self.x)
                    return(posicao, indice_posicao)
                
                else:
                    pass
        except:
            print("pass")

"""
>>> Observação: Necessário retornar o valor do índice: ->>> "var.index(x)"<<<-  
"""
