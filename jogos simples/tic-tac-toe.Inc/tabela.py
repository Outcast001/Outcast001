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

    def beautyPrint(self):
        """Imprime a tabela num formato bonitinho."""
        print(
            "\n",
            f"| {self.table[0][0]}  |" + f"|  {self.table[0][1]}  |" + f"|  {self.table[0][2]} |", '\n',

            f"| {self.table[1][0]}  |" + f"|  {self.table[1][1]}  |" + f"|  {self.table[1][2]} |", '\n',

            f"| {self.table[2][0]}  |" + f"|  {self.table[2][1]}  |" + f"|  {self.table[2][2]} |", '\n',
            end="\n"
        )
