
from escolhaXouY import PlayChoice
from verificacao import Check
from tabela import Tabela
tabuleiro = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

tabela = Tabela(table=tabuleiro) # printTable() - Descartar?
entry = PlayChoice().userChoice()

def loopMarc(entry):
    entry = entry
    for j in range(0, 3):
        if entry in tabuleiro[j]:
            tabuleiro[j][tabuleiro[j].index(entry)] = "X"
            print("Tabela: \n")
            print(tabela.printTable())
            "checkWin(table)" # Será implementada uma estrutura de controle (IF/ELIF/ELSE)
            # loopMarc(table)
        else:
            print("Error..")
            
print("\n______Area-de-Test______\n")
loopMarc(entry)
print(tabela.printTable())
print("\n______Area-de-Test______\n")

"""
Lembrete: Implementar mecanismo de que marque as casas por vez ('X' ou 'O').
"""