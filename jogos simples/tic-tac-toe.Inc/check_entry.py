from tabela import Tabela
from indice_Inc import Indice

class SelectCasa():
    """ Requisita e trata um valor inteiro ('int') da casa selecionada pelo usuário. """
    def __init__(self, playChoice) -> None:
        self.playChoice = playChoice
        
    def CheckType(self):
        """ Ativa a porra de um loop enquanto a entrada não for um número inteiro. """
        while (type(self.playChoice) == str):
            try:
                self.playChoice = int(self.playChoice)
                return(int(self.playChoice))
            
            except:
                print(f"A variável do tipo {type(self.playChoice)} ", end='\b' )
                print(' não pode ser convertida para "int"')
                self.playChoice = input("\nEscolha uma casa entre 1 e 9: ")
                print(self.playChoice, type(self.playChoice))if type(
                    self.playChoice) == str else print(self.playChoice, type(self.playChoice))
    
        return(int(self.playChoice))

    def CheckInterval(self):
        """
        Verifica se o numero esta dentro do intervalo entre as casas do tabuleiro.
        """
        while self.playChoice < 1 or self.playChoice > 9:
            self.playChoice = int(input("Entrada inválida!\nDigite uma casa diferente de {}: "
            .format(self.playChoice)))
            print(self.playChoice, type(self.playChoice))if type(
                self.playChoice) == str else print(self.playChoice, type(self.playChoice))
        else:
            return(int(self.playChoice))
    
    def checkTrapassa(self, table): # Incompleta.
        """ Função que verifica se a casa já foi marcada."""
        tabela = Tabela()
        # instância da classe "Indice".
        entry = 0 # Na prática, representa o valor de entrada do usuário.
        indice = Indice(x=entry) 

        # Obtem a posição e o índice da posição do valor de entrada.
        posicao, indice_posicao = indice.get_index()
        # Substitui o valor da posição por "O".
        table[posicao][indice_posicao] = "O"