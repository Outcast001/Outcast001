"""
Adryan - última atualização: 01 de Maio de 2023, às 18:28(PM)
"""
# IMPORTS
from indice_Inc import Indice
from tabela import Tabela
from gameResult import CheckWin
from check_entry import HouseSelected

# Tabuleiro (formato)
table = [[1,2,3],
         [4,5,6],
         [7,8,9]]

# Instância do tabuleiro de Tic-Tac-toe
tabuleiro = Tabela(table=table)

# Instância do módulo "HouseSelected"
h_selected = HouseSelected(x="x", o='o')

# Por padrão, arquivos começam vazios
HouseSelected(x='', o='').wrote_in_X()

while not (CheckWin().checkWin(table=table)):
    """ Laço executa enquanto não houver um vencedor ou empate. """
    entry = ''
    """ Trata a entrada do usuário. """
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

    print("____________________________________________________")
    print(f"Valor do módulo juíz: {CheckWin().checkWin(table=table)}")
    print("____________________________________________________")

    mark_one = f'{table[posicao][indice_posicao]}'
    if not mark_one.isnumeric():
        print("Entrada inválida! 2")

    else:
        table[posicao][indice_posicao] = "x"
        tabuleiro.beatyPrint()
        