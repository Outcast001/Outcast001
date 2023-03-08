# Casas do tabuleiro.
class Tabela():
    """ Uma classe que imprime a tabela do jogo tic-tac-toe. """

    def __init__(self, table) -> None:
        self.table = table

    def printTable(self):
        """ Como o tabuleiro se parece """
        print(self.table[0], end='\r')
        print()
        print(self.table[1], end='\r')
        print()
        print(self.table[2])
        print()
        