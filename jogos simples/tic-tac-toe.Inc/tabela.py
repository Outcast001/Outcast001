class Tabela():
    """ Uma classe que imprime a tabela do jogo tic-tac-toe. """
    table = [[1,2,3],
            [4,5,6],
            [7,8,9]]

    def __init__(self, table):
        self.table = table

    def printTable(self):
        """ Como o tabuleiro se parece """
        print(self.table[0])
        print(self.table[1])
        print(self.table[2])