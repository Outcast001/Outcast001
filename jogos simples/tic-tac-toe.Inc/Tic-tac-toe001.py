""" 
Adryan - Última atualização: 02 de Março de 2023, ás 18:18
Classes que realizam algumas features relativas ao projeto. 
"""
from tabela import Tabela
from verificacao import Check
from escolhaXouY import PlayChoice

# instância do tabuleiro de TTT (Jogo da Velha)
tabela = Tabela()

# solicita entrada do usuário
playChoice = PlayChoice().playChoice

# Verifica se a entrada do usuário é válida
Check(playChoice).checkNum()

def loopMarc(table):
    entry = "funEntry()" # Referencia 'PlayChoice()'
    for j in range(0, 3):
        if entry in table[j]:
            table[j][table[j].index(entry)] = "X"
            "funTable()"
            "checkWin(table)"
            "loopMarc(table)"

# Imprime o tabuleiro de TTT 
tabela.printTable()

""" - PROBLEMAS:

QUESTÃO 01: Como fazer com que um usuário marque uma casa por vez?
    - Loop de repetição (laço for... in ...?)
    - Vide 'tests' (sub-pasta do projeto)

QUESTÃO 02: Como marcar as casas no tabuleiro?
    - utilizar método insert?
    R: Usar estrutura "IF/ELIF/ELSE"

QUESTÃO 03: Como identificar uma derrota, vitória ou um empate?
    -   listar todos os casos possíveis e usar 
        um laço for... in... para varrer a lista e 
        determinar os resultados possíveis (VITÓRIA || DERROTA)

OBSERVAÇÃO DA QUESTÃO 03: Observa-se que a representação de cada caso possível é,
resumidamente, inviável. Dispendiosa.
"""
