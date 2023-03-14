""" 
Adryan - Última atualização: 13 de Março de 2023, ás 15:22 (P.M.)
"""

# Imports de algumas features do projeto. 
from tabela import Tabela
from verificacao import Check
from escolhaXouY import PlayChoice
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
    if x > o:
        x = 0
        o = 1
                
        # solicita entrada do usuário
        playChoice = PlayChoice().playChoice

        # Verifica se a entrada do usuário é válida
        playChoice = Check(playChoice).checkNum()
        
        # Valor de entrada do jogador.
        entry = playChoice 

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

    if x < o:
        o = 0
  
        # solicita entrada do usuário
        playChoice = PlayChoice().playChoice

        # Verifica se a entrada do usuário é válida
        playChoice = Check(playChoice).checkNum()
        
        # Valor de entrada do jogador.
        entry = playChoice 

        # instância da classe "Indice".
        indice = Indice(x=entry) 

        # Obtem a posição e o índice da posição do valor de entrada.
        posicao, indice_posicao = indice.get_index()

        # Substitui o valor da posição por "O".
        table[posicao][indice_posicao] = "O"
        
        # Imprime a tabela
        tabela.printTable()
        
        # Verifica se há um padrão 
        checkResult = CheckWin()
        checkResult.checkWin(table=tabela.table)

    # Reinicia função. Todas as alterações foram salvas.
    loopMarc(tabela.table)

loopMarc(table=tabela.table)

""" 
>>> IDÉIA: Utilizar um laço de repetição ('while statment'), para executar o jogo até
que dada condição seja atendida - condição de parada.
"""
