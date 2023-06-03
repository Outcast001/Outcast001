# passo 1
training_data = []

# passo 2
def coletar_dados_de_treinamento():
    tabuleiro = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

    jogador_atual = 'X'  # Ou 'O'

    while True:
        # Exibir o tabuleiro para o jogador atual
        'exibir_tabuleiro'(tabuleiro)

        # Obter a próxima jogada do jogador atual
        jogada = 'obter_jogada'()

        # Atualizar o tabuleiro com a jogada
        tabuleiro[jogada[0]][jogada[1]] = jogador_atual

        # Verificar se o jogador atual venceu
        if 'jogador_venceu'(tabuleiro, jogador_atual):
            # Armazenar a configuração do tabuleiro e a jogada vencedora na lista de dados de treinamento
            training_data.append((tabuleiro, jogada))
            break

        # Alternar para o próximo jogador
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

# passo 3
coletar_dados_de_treinamento()
coletar_dados_de_treinamento()
coletar_dados_de_treinamento()
