"""
Adryan - última atualização: 01 de Maio de 2023, às 14:47(PM)
"""
# IMPORTS
from indice_Inc import Indice
from tabela import Tabela

# Tabuleiro (formato)
table = [[1,2,3],
         [4,5,6],
         [7,8,9]]

# Instância do tabuleiro de Tic-Tac-toe
tabuleiro = Tabela(table=table)

token = "X"
entry = ""

"""
Executa um laço de repetição até o usuário digitar um 
número maior que 0 e menor ou igual a 9.
"""
while not entry.isnumeric() or int(entry) < 1 or int(entry) > 9:
    entry = input("Escolha uma casa entre 1 e 9: ")
    try:
        input_x = int(entry) # Casa do jogador "X"
    except:
        print("Entrada inválida!")
        entry = ""

# Instância da classe "Indice"
indice = Indice(x=input_x)

# obtem a posicao e o indice da posicao da entrada
posicao, indice_posicao = indice.get_index()

print(f"Posição: ({posicao}, {indice_posicao})")
print(f"valor: ({table[posicao][indice_posicao]})")
