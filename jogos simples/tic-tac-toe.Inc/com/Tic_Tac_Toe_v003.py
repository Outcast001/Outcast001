# IMPORTS
from indice_Inc import Indice
from tabela import Tabela
from gameResult import CheckWin

class Player():
    """ Classe que simula o jogador de T3. """
    def __init__(self, table, simbolo) -> None:
        self.table = table
        self.simbolo = simbolo

    def select_field(self):
        def loop(simbolo):
            """
            Requisita e marca a casa selecionada \n
            pelo usuário de acordo com os critérios, \n
            regras ou limitações impostas pelo jogo da velha.
            """
            tabuleiro = Tabela(table=self.table)
            entry = ''
            while not entry.isnumeric() or int(entry) < 1 or int(entry) > 9:
                entry = input("Escolha uma casa entre 1 e 9: ")
                try:
                    input_x = int(entry)
                except:
                    print("Entrada inválida!")
                    entry = ""
            
            # Instância da classe "Indice"
            indice = Indice(x=input_x)

            """ Obtém a posicao e o indice da posicao da entrada. """
            posicao, indice_posicao = indice.get_index()
            casa = f"{self.table[posicao][indice_posicao]}"
            
            """ Marca a casa selecionada pelo usuário se ela estiver livre (não ocupada)."""
            if casa.isnumeric():
                self.table[posicao][indice_posicao] = simbolo
                tabuleiro.beautyPrint()
                
                return (f"Sucessfully: {200}", table)
            else:
                """Executa novamente. """
                loop(simbolo=self.simbolo)
                return "Error: {404}"
            
        return_value = loop(simbolo=self.simbolo)
        return(return_value, table)

table = [[1,2,3],
         [4,5,6],
         [7,8,9]]

while not (CheckWin().checkWin(table=table)):
    """ Laço executa enquanto não houver um vencedor ou um empate. """
    jogador_X = Player(table=table, simbolo="X")
    jogador_O = Player(table=table, simbolo="O")

    jogador_X.select_field()
    ''' Verifica o resultado do jogo após a vez do jogador "X".'''
    CheckWin().checkWin(table=table)

    jogador_O.select_field()
    ''' Verifica o resultado do jogo após a vez do jogador "O".'''
    CheckWin().checkWin(table=table)
