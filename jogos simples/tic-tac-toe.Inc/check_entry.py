class HouseSelected():
    """ Solução para o problema do "Doubt-Mark" """
    def __init__(self, x, o) -> None:
        self.value_X = x
        self.value_O = o
        
    # Escreve e lê em "X"
    def wrote_in_X(self):
        with open("C:/Users/Adrya/Data-Science-Introduction/entry_X.csv", 'w') as arq:
            arq.write(f"{self.value_X}")
    
    def readX(self):
        with open("C:/Users/Adrya/Data-Science-Introduction/entry_X.csv", 'r') as arq:
            arq.read()


    # Escreve e lê em "O"
    def wrote_in_O(self):
        with open("C:/Users/Adrya/Data-Science-Introduction/entry_X.csv", 'w') as arq:
            arq.write(f"{self.value_O}")
    
    def readO(self):
        with open("C:/Users/Adrya/Data-Science-Introduction/entry_O.csv", 'r') as arq:
            arq.read()
