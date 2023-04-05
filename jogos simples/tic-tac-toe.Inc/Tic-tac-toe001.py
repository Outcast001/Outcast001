""" 
Adryan - Última atualização: 05 de Abril de 2023, ás 14:25(PM)
"""

# Imports de algumas features do projeto. 
from tabela import Tabela
from check_entry import SelectCasa
from indice_Inc import Indice
from gameResult import CheckWin

# Tabuleiro (formato)
table = [[1,2,3],
         [4,5,6],
         [7,8,9]]

# instância do tabuleiro de TTT (Jogo da Velha)
tabela = Tabela(table)

def loopMarc(table):
    o = 0
    x = 1
    while True:
        if  x > o:
            # solicita entrada do usuário
            playerEntry = input("\nEscolha uma casa entre 1 e 9: ")
            playerChoice = SelectCasa(playChoice=playerEntry)

            # Verifica se a entrada do usuário é válida
            ChoiceValid = playerChoice.CheckType()
            ChoiceValid = playerChoice.CheckInterval()
            
            # Valor de entrada do jogador.
            entry = ChoiceValid 

            # instância da classe "Indice".
            indice = Indice(x=entry) 

            # Obtem a posição e o índice da posição do valor de entrada.
            posicao, indice_posicao = indice.get_index()

            # Substitui o valor da posição por "X".
            table[posicao][indice_posicao] = 'X' 

            # Imprime a tabela
            tabela.printTable()

            # Verifica se há um padrão
            checkResult = CheckWin()
            checkResult.checkWin(table=tabela.table)
            x = 0
            o = 1

        if o > x:
            # solicita entrada do usuário
            playerEntry = input("\rEscolha uma casa entre 1 e 9: ")
            playerChoice = SelectCasa(playChoice=playerEntry)
            
            # Verifica se a entrada do usuário é válida
            ChoiceValid = playerChoice.CheckType()
            ChoiceValid = playerChoice.CheckInterval()
            
            # Valor de entrada do jogador.
            entry = ChoiceValid 

            # instância da classe "Indice".
            indice = Indice(x=entry) 

            # Obtem a posição e o índice da posição do valor de entrada.
            posicao, indice_posicao = indice.get_index()

            # Substitui o valor da posição por "O".
            table[posicao][indice_posicao] = "O"
            
            # Imprime a tabela
            tabela.printTable()

            # Verifica se há um padrão (OBS: Substituir por estrutura IF/ELSE/ELIF).
            checkResult = CheckWin()
            
            checkResult.checkWin(table=tabela.table)
            o = 0
            x = 1

loopMarc(table=tabela.table)
