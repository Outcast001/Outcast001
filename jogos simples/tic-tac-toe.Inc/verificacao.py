class Check():
    def __init__(self, num) -> None:
        self.num = num

    def checkNum(self):
        """
        Verifica se o numero esta dentro do intervalo entre as casas do tabuleiro.
        """
        while self.num < 1 or self.num > 9:
            self.num = int(input("Entrada inválida!\nDigite uma casa diferente de {}: "
            .format(self.num)))
        else: 
            print(f"Done!")
            print("Casa escolhida:", self.num)
            return(self.num)