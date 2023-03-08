""" 
Adryan - Última atualização: 08 de Março de 2023, ás 16:06 (P.M.)
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

""" - PROBLEMAS:

>>> QUESTÃO 01: Como fazer com que um usuário marque uma casa por vez?
    - Loop de repetição (laço for... in ...?)
    - Vide 'tests' (sub-pasta do projeto)
    >>> - DONE

>>> QUESTÃO 02: Como marcar as casas no tabuleiro?
    - utilizar método insert?
    >>> - DONE

>>> QUESTÃO 03: Como identificar uma derrota, vitória ou um empate?
    -   listar todos os casos possíveis e usar 
        um laço for... in... para varrer a lista e 
        determinar os resultados possíveis (VITÓRIA || DERROTA)

>>> - OBSERVAÇÃO DA QUESTÃO 03: Observa-se que a representação de cada caso possível é,
resumidamente, inviável. Dispendiosa.

>>> - SOLUÇÃO DA QUESTÃO 3: Utilizar estrutura de controle "IF/ELIF/ELSE"

>>> IDÉIA: Transformar linhas "33" a "52" em funções/métodos e usar num bloco de código
em outras linhas.
    - Isso tornaria o código mais legível e facilitaria a manutenção.

>>> IDÉIA 2: Utilizar um laço de repetição ('while statment'), para executar o jogo até
que dada condição seja atendida - condição de parada.
"""
